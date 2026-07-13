"""配置加载模块。

从 .env 文件和 os.environ 加载所有配置项。
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# 加载项目根目录的 .env 文件
_project_root = Path(__file__).resolve().parent.parent
load_dotenv(_project_root / ".env")


# --- 推送配置 ---
# 推送渠道: desktop, email, pushplus, wecom_bot — 逗号分隔可同时用多个
NOTIFIER_TYPES: str = os.getenv("NOTIFIER_TYPES", "desktop,email")

PUSHPLUS_TOKEN: str = os.getenv("PUSHPLUS_TOKEN", "")
WECOM_WEBHOOK_URL: str = os.getenv("WECOM_WEBHOOK_URL", "")

# --- 邮件配置 ---
SMTP_HOST: str = os.getenv("SMTP_HOST", "smtp.163.com")
SMTP_PORT: int = int(os.getenv("SMTP_PORT", "465"))
SMTP_USER: str = os.getenv("SMTP_USER", "")
SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")
EMAIL_FROM: str = os.getenv("EMAIL_FROM", "")
EMAIL_TO: str = os.getenv("EMAIL_TO", "")

# --- 数据库 ---
DB_PATH: Path = _project_root / "data" / "qiuzhao.db"

# --- 爬虫配置 ---
REQUEST_DELAY_MIN: float = float(os.getenv("REQUEST_DELAY_MIN", "1.0"))
REQUEST_DELAY_MAX: float = float(os.getenv("REQUEST_DELAY_MAX", "3.0"))
MAX_RETRIES: int = int(os.getenv("MAX_RETRIES", "3"))
SCRAPE_PAGES: int = int(os.getenv("SCRAPE_PAGES", "5"))  # 牛客网翻页数

# --- 调试 ---
DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

# --- 日志 ---
LOG_LEVEL: str = "DEBUG" if DEBUG else "INFO"

# 确保 data 目录存在
(_project_root / "data").mkdir(parents=True, exist_ok=True)
(_project_root / "logs").mkdir(parents=True, exist_ok=True)
