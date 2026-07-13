"""数据库操作模块 — SQLite 存储与去重。"""

import sqlite3
import hashlib
from datetime import datetime, date
from pathlib import Path

from qiuzhao.config import DB_PATH


def _now_utc() -> str:
    return datetime.utcnow().isoformat()


def get_conn() -> sqlite3.Connection:
    """获取数据库连接（自动创建表）。"""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """初始化数据库表结构。"""
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS positions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL DEFAULT '',
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            url_hash TEXT NOT NULL UNIQUE,
            source TEXT NOT NULL DEFAULT '',
            found_at TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_positions_company
        ON positions(company)
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_positions_found_at
        ON positions(found_at)
    """)
    conn.commit()
    conn.close()


def url_exists(url: str) -> bool:
    """检查 URL 是否已存在于数据库。"""
    url_hash = hashlib.sha256(url.encode()).hexdigest()
    conn = get_conn()
    row = conn.execute(
        "SELECT 1 FROM positions WHERE url_hash = ?", (url_hash,)
    ).fetchone()
    conn.close()
    return row is not None


def insert_position(
    company: str,
    title: str,
    url: str,
    source: str,
    found_at: str | None = None,
) -> bool:
    """插入一条新职位记录。返回 True 表示新增，False 表示已存在。"""
    url_hash = hashlib.sha256(url.encode()).hexdigest()
    if found_at is None:
        found_at = date.today().isoformat()
    created_at = _now_utc()

    conn = get_conn()
    try:
        conn.execute(
            """INSERT INTO positions (company, title, url, url_hash, source, found_at, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (company, title, url, url_hash, source, found_at, created_at),
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # url_hash 冲突：已存在
        return False
    finally:
        conn.close()


def get_today_count() -> int:
    """获取今日已抓取的数量。"""
    today = date.today().isoformat()
    conn = get_conn()
    row = conn.execute(
        "SELECT COUNT(*) as cnt FROM positions WHERE found_at = ?", (today,)
    ).fetchone()
    conn.close()
    return row["cnt"] if row else 0


def get_all_url_hashes() -> set[str]:
    """获取所有已存储的 URL hash（用于批量去重）。"""
    conn = get_conn()
    rows = conn.execute("SELECT url_hash FROM positions").fetchall()
    conn.close()
    return {row["url_hash"] for row in rows}
