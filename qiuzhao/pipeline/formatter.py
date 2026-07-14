"""消息格式化模块 — 按分类分组，区分新增/已有，含公司简介。"""

from datetime import date
from qiuzhao.seed_data import CATEGORY_NAMES, COMPANY_INTRO, get_company_intro

CATEGORY_ORDER = [
    "internet", "ai_hardtech", "gaming", "ev",
    "foreign", "finance", "consulting", "fmcg", "soe",
]


def _group_by_category(items: list[dict]) -> dict[str, list[dict]]:
    """按分类分组。"""
    groups: dict[str, list[dict]] = {}
    for item in items:
        cat = item.get("category", "other")
        groups.setdefault(cat, []).append(item)
    return groups


def _sorted_groups(groups: dict[str, list[dict]]) -> list[tuple[str, str, list[dict]]]:
    """排序分组，按预定义顺序。"""
    result = []
    for cat in CATEGORY_ORDER:
        if cat in groups:
            result.append((cat, CATEGORY_NAMES.get(cat, cat), groups[cat]))
    for cat, items in groups.items():
        if cat not in CATEGORY_ORDER:
            result.append((cat, CATEGORY_NAMES.get(cat, cat), items))
    return result


def format_full_report(items: list[dict], is_daily: bool = False) -> str:
    """格式化完整推送报告。

    - 首次运行：展示全部条目，按分类整理
    - 每日运行：区分【🆕 今日新增】和【📋 之前已开放】
    """
    today = date.today().strftime("%Y-%m-%d")
    lines = [
        f"## 🍂 2027届秋招日报 — {today}",
        "",
    ]

    if is_daily:
        # 区分新旧
        new_items = [i for i in items if i.get("is_new")]
        old_items = [i for i in items if not i.get("is_new")]

        if new_items:
            lines.append(f"### 🆕 今日新增 ({len(new_items)} 个)")
            lines.append("")
            lines.extend(_format_section(new_items, show_verified=True))

        if old_items and new_items:
            lines.append("---")
            lines.append("")
            lines.append(f"### 📋 之前已开放 ({len(old_items)} 个)")
            lines.append("")
            lines.extend(_format_section(old_items, show_verified=False))

        if not new_items and old_items:
            lines.append(f"今日暂无新增，共 {len(old_items)} 个已开放职位：")
            lines.append("")
            lines.extend(_format_section(old_items, show_verified=False))

        if not items:
            lines.append("今日暂无秋招信息，系统正常运行中 ⏰")
    else:
        # 首次运行：全部展示
        total = len(items)
        verified_count = sum(1 for i in items if i.get("verified"))
        lines.append(f"共 **{total}** 个职位，其中 ✅ {verified_count} 个已验证")
        lines.append("")
        lines.extend(_format_section(items, show_verified=True))

    lines.append("")
    lines.append("---")
    lines.append(f"📬 每天 8:00 自动推送 | 仅含产品/AI/管培/咨询/市场方向")
    return "\n".join(lines)


def _format_section(items: list[dict], show_verified: bool = True) -> list[str]:
    """格式化一个分组的全部条目，按分类组织。"""
    groups = _group_by_category(items)
    sorted_cats = _sorted_groups(groups)
    lines = []

    for cat_key, cat_name, cat_items in sorted_cats:
        # 公司去重合并（同一公司多个职位合并展示）
        company_items: dict[str, list[dict]] = {}
        for it in cat_items:
            company_items.setdefault(it["company"], []).append(it)

        lines.append(f"**{cat_name}** ({len(cat_items)} 个)")
        lines.append("")

        for company, positions in company_items.items():
            intro = get_company_intro(company)
            intro_str = f" — *{intro}*" if intro else ""
            lines.append(f"🏢 **{company}**{intro_str}")
            lines.append("")

            for pos in positions:
                # 链接
                url = pos.get("url", "")
                title = pos["title"]
                verified = pos.get("verified", False)

                # 验证标记
                v_mark = " ✅" if verified else ""
                note = pos.get("note", "")

                if url:
                    lines.append(f"  • [{title}]({url}){v_mark}")
                else:
                    lines.append(f"  • {title}{v_mark}")

                if note:
                    lines.append(f"    ⚠️ {note}")

            lines.append("")

    return lines


def format_daily_report(items: list[dict], footer: str = "") -> str:
    """旧版兼容接口 — 简单按公司分组。"""
    if not items:
        return f"📢 今日暂无新增秋招职位。\n\n> 系统正常运行中 {footer}"

    groups: dict[str, list[dict]] = {}
    for item in items:
        groups.setdefault(item.get("company", "其他"), []).append(item)

    sorted_gs = sorted(groups.items(), key=lambda x: len(x[1]), reverse=True)

    lines = [f"📢 **今日秋招新增** ({date.today().strftime('%Y-%m-%d')})", "", "---", ""]

    for company, positions in sorted_gs:
        lines.append(f"### 🏢 {company}")
        for pos in positions:
            url = pos.get("url", "")
            source = pos.get("source", "")
            if url:
                lines.append(f"  • [{pos['title']}]({url})")
            else:
                lines.append(f"  • {pos['title']}")
        lines.append("")

    lines.append("---")
    lines.append(f"共 **{len(items)}** 个新增职位 | 来源: {', '.join(set(i.get('source', '') for i in items))}")
    if footer:
        lines.append(footer)

    return "\n".join(lines)


def format_empty_report(failed_sources: list[str] | None = None) -> str:
    """无新职位时的日报。"""
    today = date.today().strftime("%Y-%m-%d")
    msg = f"📢 **秋招扫描日报** ({today})\n\n今日暂无新增秋招职位。\n\n> 系统正常运行中，有新增会立即推送 ⏰"
    if failed_sources:
        msg += f"\n\n⚠️ 抓取失败: {', '.join(failed_sources)}"
    return msg
