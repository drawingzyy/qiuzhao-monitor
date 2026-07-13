"""消息格式化模块 — 按公司分组生成 Markdown 推送消息。"""

from datetime import date


def format_daily_report(items: list[dict], footer_extra: str = "") -> str:
    """将职位列表格式化为每日推送 Markdown 消息。

    Args:
        items: 职位条目列表，每条含 company, title, url, source 等
        footer_extra: 页脚额外信息（如失败数据源）

    Returns:
        Markdown 格式的推送消息
    """
    today = date.today().strftime("%Y-%m-%d")

    if not items:
        return (
            f"📢 **秋招扫描日报** ({today})\n\n"
            f"今日暂无新增秋招职位。\n\n"
            f"> 系统正常运行中，有新增会立即推送 {footer_extra}"
        )

    # 按公司分组
    groups: dict[str, list[dict]] = {}
    for item in items:
        company = item.get("company") or "其他公司"
        groups.setdefault(company, []).append(item)

    # 公司排序：职位多的在前
    sorted_groups = sorted(groups.items(), key=lambda x: len(x[1]), reverse=True)

    # 构建消息
    lines = [
        f"📢 **今日秋招新增** ({today})",
        "",
        "---",
        "",
    ]

    for company, positions in sorted_groups:
        lines.append(f"### 🏢 {company}")
        for pos in positions:
            title = pos["title"]
            url = pos["url"]
            source = pos.get("source", "")
            source_tag = f" `[{source}]`" if source else ""
            lines.append(f"  • [{title}]({url}){source_tag}")
        lines.append("")

    lines.append("---")
    lines.append("")

    # 页脚统计
    total = len(items)
    companies_count = len(groups)
    sources = set()
    for item in items:
        for s in item.get("source", "").split(", "):
            if s:
                sources.add(s)

    lines.append(f"共 **{total}** 个新增职位，覆盖 **{companies_count}** 家公司")
    lines.append(f"来源: {', '.join(sorted(sources))}")

    if footer_extra:
        lines.append(f"\n{footer_extra}")

    return "\n".join(lines)


def format_empty_report(failed_sources: list[str] | None = None) -> str:
    """生成没有新职位时的日报。"""
    today = date.today().strftime("%Y-%m-%d")
    msg = f"📢 **秋招扫描日报** ({today})\n\n今日暂无新增秋招职位。\n\n> 系统正常运行中，有新增会立即推送 ⏰"
    if failed_sources:
        msg += f"\n\n⚠️ 以下数据源本次抓取失败: {', '.join(failed_sources)}"
    return msg
