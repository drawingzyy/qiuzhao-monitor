"""牛客网校招讨论区爬虫。

抓取 https://www.nowcoder.com/discuss?type=7 中与秋招相关的帖子。
"""

import re
from datetime import datetime, timedelta, date
from bs4 import BeautifulSoup
from loguru import logger

from qiuzhao.scrapers.base import BaseScraper
from qiuzhao.config import SCRAPE_PAGES

# 秋招关键词（用于筛选帖子标题）
QIYZHAO_KEYWORDS = [
    "秋招", "校招", "2027届", "提前批", "正式批",
    "应届", "校园招聘", "管培生", "毕业生",
]

# 公司别名映射（帖子中的俗称 → 正式名称）
COMPANY_ALIASES: dict[str, str] = {
    "字节": "字节跳动",
    "bytedance": "字节跳动",
    "鹅厂": "腾讯",
    "腾讯": "腾讯",
    "tencent": "腾讯",
    "阿里": "阿里巴巴",
    "alibaba": "阿里巴巴",
    "淘天": "阿里巴巴",
    "蚂蚁": "蚂蚁集团",
    "开水团": "美团",
    "美团": "美团",
    "meituan": "美团",
    "熊厂": "百度",
    "百度": "百度",
    "baidu": "百度",
    "狗厂": "京东",
    "京东": "京东",
    "jd": "京东",
    "猪厂": "网易",
    "网易": "网易",
    "netease": "网易",
    "福报厂": "阿里巴巴",
    "宇宙厂": "字节跳动",
    "快手": "快手",
    "kuaishou": "快手",
    "小红书": "小红书",
    "red": "小红书",
    "拼多多": "拼多多",
    "pdd": "拼多多",
    "滴滴": "滴滴",
    "didi": "滴滴",
    "华为": "华为",
    "huawei": "华为",
    "小米": "小米",
    "xiaomi": "小米",
    "oppo": "OPPO",
    "vivo": "vivo",
    "B站": "哔哩哔哩",
    "bilibili": "哔哩哔哩",
    "哔哩哔哩": "哔哩哔哩",
    "携程": "携程",
    "ctrip": "携程",
    "大疆": "大疆",
    "dji": "大疆",
    "比亚迪": "比亚迪",
    "byd": "比亚迪",
    "理想": "理想汽车",
    "蔚来": "蔚来",
    "小鹏": "小鹏汽车",
    "shein": "SHEIN",
    "商汤": "商汤科技",
    "旷视": "旷视科技",
    "微软": "微软",
    "microsoft": "微软",
    "谷歌": "Google",
    "google": "Google",
    "亚马逊": "亚马逊",
    "amazon": "亚马逊",
    "apple": "Apple",
    "苹果": "Apple",
    "shopee": "Shopee",
    "虾皮": "Shopee",
}

# 已知公司名列表（用于从未匹配别名中提取）
KNOWN_COMPANIES = sorted(set(COMPANY_ALIASES.values()))


class NowcoderScraper(BaseScraper):
    """牛客网校招讨论区爬虫。"""

    BASE_URL = "https://www.nowcoder.com"

    def __init__(self):
        super().__init__(name="nowcoder")

    def _is_qiuzhao_related(self, title: str) -> bool:
        """判断标题是否与秋招相关。"""
        title_lower = title.lower()
        return any(kw.lower() in title_lower for kw in QIYZHAO_KEYWORDS)

    def _extract_company(self, title: str) -> str:
        """从标题中提取公司名。"""
        title_lower = title.lower()
        # 先检查别名
        for alias, full_name in COMPANY_ALIASES.items():
            if alias.lower() in title_lower:
                return full_name
        # 再检查已知公司名
        for company in KNOWN_COMPANIES:
            if company.lower() in title_lower:
                return company
        return ""

    def _parse_relative_time(self, text: str) -> bool:
        """判断相对时间是否在 24 小时内。

        牛客网常见格式: "1小时前", "30分钟前", "1天前", "2天前"
        返回 True 表示在 24 小时内。
        """
        if not text:
            return False
        text = text.strip()
        # 分钟前 / 小时前 → 24 小时内
        if "分钟前" in text or "小时前" in text:
            return True
        # "刚刚" → 24 小时内
        if "刚刚" in text:
            return True
        # "1天前" → 24 小时内
        if text == "1天前":
            return True
        # "昨天" → 24 小时内
        if "昨天" in text:
            return True
        # "今天" → 24 小时内
        if "今天" in text:
            return True
        # "N天前" (N >= 2) → 超过 24 小时
        days_match = re.match(r"(\d+)天前", text)
        if days_match:
            return int(days_match.group(1)) <= 1
        return False

    async def scrape(self) -> list[dict]:
        """爬取牛客网校招讨论区。"""
        results: list[dict] = []
        today = date.today().isoformat()

        async for page_results in self._scrape_pages():
            for item in page_results:
                item["found_at"] = today
                results.append(item)

        logger.info(f"[nowcoder] 共抓取 {len(results)} 条秋招相关帖子")
        return results

    async def _scrape_pages(self):
        """逐页抓取。"""
        for page in range(1, SCRAPE_PAGES + 1):
            url = f"{self.BASE_URL}/discuss?type=7&order=1&page={page}"
            resp = await self._fetch(url)
            if resp is None:
                logger.warning(f"[nowcoder] 第 {page} 页请求失败，停止翻页")
                break

            soup = BeautifulSoup(resp.text, "lxml")
            items = soup.select("li.discuss-item, div.discuss-main")

            if not items:
                logger.debug(f"[nowcoder] 第 {page} 页无帖子")
                break

            page_results = []
            for item in items:
                # 标题和链接
                title_el = item.select_one("a[href*='/discuss/']")
                if not title_el:
                    continue

                title = title_el.get_text(strip=True)
                if not self._is_qiuzhao_related(title):
                    continue

                href = title_el.get("href", "")
                if href and not href.startswith("http"):
                    href = self.BASE_URL + href

                # 发帖时间
                time_el = item.select_one("time, .post-time, .discuss-time, span.time")
                time_text = time_el.get_text(strip=True) if time_el else ""

                if time_text and not self._parse_relative_time(time_text):
                    continue

                company = self._extract_company(title)
                page_results.append({
                    "company": company,
                    "title": title,
                    "url": href,
                    "source": "牛客网",
                })

            logger.debug(f"[nowcoder] 第 {page} 页: {len(page_results)} 条匹配")
            yield page_results

            if len(items) < 10:
                # 最后一页
                break

            await self._delay()
