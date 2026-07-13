"""搜索引擎爬虫 — 通过 Bing 搜索最新的秋招信息。"""

import re
from datetime import date
from bs4 import BeautifulSoup
from loguru import logger
from urllib.parse import quote_plus

from qiuzhao.scrapers.base import BaseScraper
from qiuzhao.companies import COMPANIES

SEARCH_QUERIES = [
    '2027届 秋招 校招 提前批',
    '2027届 校招 正式批',
    '2027届 应届生 校园招聘',
]

KNOWN_COMPANIES = {c["name"] for c in COMPANIES}


class SearchScraper(BaseScraper):
    """通过 Bing 搜索发现新的秋招信息。"""

    BASE_URL = "https://www.bing.com/search"

    def __init__(self):
        super().__init__(name="search")

    def _extract_company(self, text: str) -> str:
        """从文本中提取已知公司名，按长度降序匹配避免短名误匹配。"""
        for name in sorted(KNOWN_COMPANIES, key=len, reverse=True):
            if name in text:
                return name
        return ""

    def _is_qiuzhao_related(self, text: str) -> bool:
        keywords = ["2027届", "秋招", "校招", "提前批", "应届", "校园招聘", "毕业生"]
        return any(kw.lower() in text.lower() for kw in keywords)

    async def _search_one(self, query: str) -> list[dict]:
        results = []
        params = {
            "q": query,
            "setmkt": "zh-CN",
            "count": 20,
        }
        # 拼接 URL
        qs = "&".join(f"{k}={quote_plus(str(v))}" for k, v in params.items())
        url = f"{self.BASE_URL}?{qs}"

        resp = await self._fetch(
            url,
            headers={
                "Accept-Language": "zh-CN,zh;q=0.9",
            },
        )
        if resp is None:
            logger.warning(f"[search] Bing 搜索失败: {query}")
            return results

        soup = BeautifulSoup(resp.text, "lxml")

        # Bing 搜索结果：li.b_algo 内包含 h2 > a
        for item in soup.select("li.b_algo"):
            link_el = item.select_one("h2 a")
            if not link_el:
                continue

            title = link_el.get_text(strip=True)
            href = link_el.get("href", "")

            if not title or not href:
                continue

            if not self._is_qiuzhao_related(title):
                continue

            # 摘要
            snippet_el = item.select_one(".b_caption p, .b_lineclamp2")
            snippet = snippet_el.get_text(strip=True) if snippet_el else ""

            company = self._extract_company(title + " " + snippet)

            results.append({
                "company": company,
                "title": title,
                "url": href,
                "source": "搜索发现",
            })

        return results

    async def scrape(self) -> list[dict]:
        all_results = []
        today = date.today().isoformat()

        for query in SEARCH_QUERIES:
            items = await self._search_one(query)
            logger.info(f"[search] '{query}' → {len(items)} 条")
            for item in items:
                item["found_at"] = today
            all_results.extend(items)
            await self._delay()

        # 去重
        seen_urls = set()
        unique = []
        for item in all_results:
            if item["url"] not in seen_urls:
                seen_urls.add(item["url"])
                unique.append(item)

        logger.info(f"[search] 共发现 {len(unique)} 条（去重后）")
        return unique
