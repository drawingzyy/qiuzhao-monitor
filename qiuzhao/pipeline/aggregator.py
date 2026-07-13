"""数据聚合模块 — 合并、标准化各爬虫返回的结果。"""

from datetime import date


def normalize(item: dict, source: str) -> dict:
    """将爬虫返回的原始条目标准化。

    Args:
        item: 原始条目 dict
        source: 来源标识（如 "牛客网"）

    Returns:
        标准化后的 dict，包含 company, title, url, source, found_at
    """
    return {
        "company": (item.get("company") or "").strip(),
        "title": (item.get("title") or "").strip(),
        "url": (item.get("url") or "").strip(),
        "source": (item.get("source") or source).strip(),
        "found_at": item.get("found_at") or date.today().isoformat(),
    }


def aggregate(results_by_source: list[tuple[str, list[dict]]]) -> list[dict]:
    """汇聚多个数据源的结果，标准化并过滤无效条目。

    Args:
        results_by_source: [(source_name, [items]), ...]

    Returns:
        标准化后的条目列表
    """
    all_items = []
    for source, items in results_by_source:
        for item in items:
            norm = normalize(item, source)
            # 过滤：标题不能为空，URL 不能为空
            if norm["title"] and norm["url"]:
                all_items.append(norm)
    return all_items
