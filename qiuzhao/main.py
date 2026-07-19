"""主入口 — 调度所有爬虫，执行数据管道，发送推送。"""

import asyncio
from datetime import date
from loguru import logger

from qiuzhao.config import NOTIFIER_TYPES, DEBUG
from qiuzhao.db import init_db, insert_position, get_all_url_hashes, get_today_count, get_all_positions
from qiuzhao.scrapers.nowcoder import NowcoderScraper
from qiuzhao.scrapers.search import SearchScraper
from qiuzhao.seed_data import inject_seed_data, SEED_POSITIONS, CATEGORY_NAMES
from qiuzhao.pipeline.aggregator import aggregate
from qiuzhao.pipeline.dedup import deduplicate_by_url, deduplicate_by_title
from qiuzhao.pipeline.formatter import format_daily_report, format_empty_report, format_full_report
from qiuzhao.notifiers.desktop import DesktopNotifier
from qiuzhao.notifiers.email import EmailNotifier
from qiuzhao.notifiers.pushplus import PushPlusNotifier
from qiuzhao.notifiers.wecom_bot import WecomBotNotifier

# 导入 loguru，配置日志
import sys

logger.remove()
logger.add(
    sys.stderr,
    level="DEBUG" if DEBUG else "INFO",
    format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
)
logger.add(
    "logs/qiuzhao_{time:YYYY-MM-DD}.log",
    rotation="1 day",
    retention="7 days",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} | {message}",
)


async def run_scrapers() -> tuple[dict[str, list[dict]], list[str]]:
    """并行运行所有爬虫。

    Returns:
        ({source_name: [items]}, failed_sources) — failed_sources 是抓取失败的数据源名
    """
    scrapers = [
        ("search", SearchScraper()),
        ("nowcoder", NowcoderScraper()),
    ]

    results: dict[str, list[dict]] = {}
    failed_sources: list[str] = []

    # 并行执行所有爬虫
    tasks = [_run_one_scraper(name, scraper) for name, scraper in scrapers]
    gathered = await asyncio.gather(*tasks)

    for name, items, error in gathered:
        results[name] = items
        if error:
            failed_sources.append(name)
            logger.warning(f"{name}: 错误 - {error}")

    return results, failed_sources


async def _run_one_scraper(name: str, scraper) -> tuple[str, list[dict], str | None]:
    """运行单个爬虫，捕获异常。"""
    logger.info(f"开始抓取: {name}")
    try:
        items = await scraper.scrape()
        logger.info(f"{name}: 完成，{len(items)} 条")
        return name, items, None
    except Exception as e:
        logger.error(f"{name}: 抓取失败 - {e}")
        return name, [], str(e)
    finally:
        await scraper.close()


def _enrich(item: dict) -> dict:
    """给数据条目补上 category 和 verified 字段。"""
    company = item.get("company", "")
    # 从种子数据中查找匹配
    for cat, c, title, verified in SEED_POSITIONS:
        if c == company:
            item["category"] = cat
            item["verified"] = verified
            break
    if "category" not in item:
        # 从 source 字段推断 category（source 存的是分类名）
        item["category"] = "other"
    if "verified" not in item:
        item["verified"] = False
    return item


def get_notifiers() -> list:
    """根据配置获取通知器实例列表，支持多渠道同时推送。"""
    types = [t.strip() for t in NOTIFIER_TYPES.split(",") if t.strip()]
    notifiers = []
    for t in types:
        if t == "wecom_bot":
            notifiers.append(WecomBotNotifier())
        elif t == "pushplus":
            notifiers.append(PushPlusNotifier())
        elif t == "email":
            notifiers.append(EmailNotifier())
        elif t == "desktop":
            notifiers.append(DesktopNotifier())
    if not notifiers:
        notifiers.append(DesktopNotifier())
    return notifiers


async def main() -> None:
    """主流程。"""
    logger.info("=" * 50)
    logger.info(f"秋招扫描启动 — {date.today().isoformat()}")
    logger.info("=" * 50)

    # 1. 初始化数据库
    init_db()

    # 1.5 首次运行：注入种子数据（已知已开放秋招的公司）
    is_first_run = get_today_count() == 0
    if is_first_run:
        logger.info("首次运行，注入种子数据...")
        seed_count, seed_items = inject_seed_data(insert_position)
        logger.info(f"种子数据: {seed_count} 条已知秋招信息已入库")
        # 用新的分类格式化
        message = format_full_report(seed_items, is_daily=False)
        title = f"🍂 2027届秋招合集 — {seed_count} 个职位已开放"
        notifiers = get_notifiers()
        for n in notifiers:
            await n.send(title, message)
        logger.info(f"首次推送完成: {seed_count} 条种子数据 ✅")
        return

    # 2. 运行所有爬虫
    scraped, failed_sources = await run_scrapers()

    # 3. 汇聚标准化
    sources_list = [(name, items) for name, items in scraped.items()]
    all_items = aggregate(sources_list)
    logger.info(f"汇聚共 {len(all_items)} 条原始记录")

    # 4. 加载已有 URL hash → 去重
    existing_hashes = get_all_url_hashes()
    new_items = deduplicate_by_url(all_items, existing_hashes)
    new_items = deduplicate_by_title(new_items)
    logger.info(f"去重后剩余 {len(new_items)} 条新记录")

    # 5. 新记录写入数据库
    saved_count = 0
    for item in new_items:
        if insert_position(
            company=item["company"],
            title=item["title"],
            url=item["url"],
            source=item.get("source", ""),
            found_at=item.get("found_at"),
        ):
            saved_count += 1
    logger.info(f"新写入数据库 {saved_count} 条")

    # 6. 格式化推送消息 — 新增在前，全部累计在后
    if new_items:
        for item in new_items:
            item["is_new"] = True
            _enrich(item)
        all_positions = [_enrich(dict(p)) for p in get_all_positions()]
        for item in all_positions:
            item["is_new"] = False
        all_positions = new_items + all_positions
        message = format_full_report(all_positions, is_daily=True)
        title = f"🍂 秋招新增 {len(new_items)} 个 ({date.today().strftime('%m/%d')})"
    else:
        all_positions = [_enrich(dict(p)) for p in get_all_positions()]
        for item in all_positions:
            item["is_new"] = False
        message = format_full_report(all_positions, is_daily=True)
        title = f"🍂 秋招日报 ({date.today().strftime('%m/%d')})"

    # 7. 推送到所有渠道
    notifiers = get_notifiers()
    logger.info(f"推送渠道: {NOTIFIER_TYPES} ({len(notifiers)} 个)")
    for notifier in notifiers:
        channel = type(notifier).__name__
        success = await notifier.send(title, message)
        if success:
            logger.info(f"  [{channel}] 推送成功 ✅")
        else:
            logger.error(f"  [{channel}] 推送失败 ❌")

    logger.info(f"本次运行完成: 抓取 {len(all_items)} → 去重 {len(new_items)} → 入库 {saved_count}")


if __name__ == "__main__":
    asyncio.run(main())
