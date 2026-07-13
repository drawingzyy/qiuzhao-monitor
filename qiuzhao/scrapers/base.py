"""基础爬虫抽象类。"""

import random
import asyncio
from abc import ABC, abstractmethod
from loguru import logger

import httpx

from qiuzhao.config import REQUEST_DELAY_MIN, REQUEST_DELAY_MAX, MAX_RETRIES

# User-Agent 池
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
]


class BaseScraper(ABC):
    """所有爬虫的抽象基类。

    提供：
    - httpx AsyncClient 管理
    - UA 随机轮换
    - 请求间隔控制
    - 指数退避重试
    - 结构化日志
    """

    def __init__(self, name: str = "base"):
        self.name = name
        self._client: httpx.AsyncClient | None = None

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(
                timeout=httpx.Timeout(30.0),
                follow_redirects=True,
                headers={"User-Agent": random.choice(USER_AGENTS)},
            )
        return self._client

    async def close(self) -> None:
        if self._client:
            await self._client.aclose()
            self._client = None

    def _random_ua(self) -> str:
        return random.choice(USER_AGENTS)

    async def _delay(self) -> None:
        """随机延迟，避免请求过快。"""
        seconds = random.uniform(REQUEST_DELAY_MIN, REQUEST_DELAY_MAX)
        await asyncio.sleep(seconds)

    async def _fetch(
        self,
        url: str,
        headers: dict | None = None,
        retries: int | None = None,
    ) -> httpx.Response | None:
        """带重试的 GET 请求。"""
        if retries is None:
            retries = MAX_RETRIES

        client = await self._get_client()
        req_headers = {"User-Agent": self._random_ua()}
        if headers:
            req_headers.update(headers)

        last_error = None
        for attempt in range(retries):
            try:
                logger.debug(f"[{self.name}] GET {url} (attempt {attempt + 1}/{retries})")
                resp = await client.get(url, headers=req_headers)
                if resp.status_code == 429:
                    wait = 2 ** attempt * 5
                    logger.warning(f"[{self.name}] 429 rate limited, waiting {wait}s")
                    await asyncio.sleep(wait)
                    continue
                resp.raise_for_status()
                return resp
            except httpx.HTTPStatusError as e:
                last_error = e
                if e.response.status_code >= 500:
                    wait = 2 ** attempt
                    logger.warning(f"[{self.name}] HTTP {e.response.status_code}, retrying in {wait}s")
                    await asyncio.sleep(wait)
                else:
                    logger.error(f"[{self.name}] HTTP {e.response.status_code}: {url}")
                    return None
            except Exception as e:
                last_error = e
                wait = 2 ** attempt
                logger.warning(f"[{self.name}] Request failed: {e}, retrying in {wait}s")
                await asyncio.sleep(wait)

        logger.error(f"[{self.name}] All {retries} retries exhausted for {url}: {last_error}")
        return None

    @abstractmethod
    async def scrape(self) -> list[dict]:
        """执行爬取，返回标准化职位信息列表。

        每条记录格式:
        {
            "company": str,    # 公司名
            "title": str,      # 职位标题
            "url": str,        # 详情链接
            "source": str,     # 数据来源标识
        }
        """
        ...
