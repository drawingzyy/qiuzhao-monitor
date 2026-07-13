"""去重模块 — URL 精确去重 + 标题相似度模糊去重。"""

import hashlib
from difflib import SequenceMatcher
from loguru import logger

from qiuzhao.db import get_all_url_hashes


def _url_hash(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()


def _title_similar(a: str, b: str, threshold: float = 0.85) -> bool:
    """判断两个标题是否相似。"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio() >= threshold


def deduplicate_by_url(
    items: list[dict],
    existing_hashes: set[str] | None = None,
) -> list[dict]:
    """基于 URL hash 去重。

    1. 与数据库中已有记录对比
    2. 当前批次内部去重

    Args:
        items: 待去重条目
        existing_hashes: 数据库中已存在的 URL hash 集合

    Returns:
        去重后的新条目
    """
    if existing_hashes is None:
        existing_hashes = get_all_url_hashes()

    seen = set()
    new_items = []

    for item in items:
        h = _url_hash(item["url"])

        # 数据库已有 → 跳过
        if h in existing_hashes:
            continue

        # 当前批次已有 → 跳过
        if h in seen:
            continue

        seen.add(h)
        item["url_hash"] = h
        new_items.append(item)

    dup_count = len(items) - len(new_items)
    if dup_count > 0:
        logger.info(f"URL 去重: 移除 {dup_count} 条重复")

    return new_items


def deduplicate_by_title(
    items: list[dict],
    threshold: float = 0.85,
) -> list[dict]:
    """基于标题相似度去重。

    同一公司 + 标题相似度 > threshold → 视为重复，保留第一条。
    """
    result = []
    for item in items:
        is_dup = False
        for existing in result:
            if item["company"] == existing["company"] and _title_similar(
                item["title"], existing["title"], threshold
            ):
                # 合并来源
                sources = set(existing.get("sources", [existing["source"]]))
                sources.add(item["source"])
                existing["sources"] = list(sources)
                existing["source"] = ", ".join(sources)
                is_dup = True
                break
        if not is_dup:
            item["sources"] = [item["source"]]
            result.append(item)

    dup_count = len(items) - len(result)
    if dup_count > 0:
        logger.info(f"标题去重: 移除 {dup_count} 条相似")

    return result
