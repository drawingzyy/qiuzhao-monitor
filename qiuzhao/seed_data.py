"""种子数据 — 基于 2026 年 7 月已知的 2027 届秋招开放情况。

这些数据来自多渠道搜索结果，作为首次运行的初始数据。
后续每日扫描会在此基础上检测新增。
"""

from datetime import date

# 已知已开放 2027 届秋招/提前批的公司及其信息
SEED_POSITIONS = [
    # ===== 互联网大厂 - 提前批已开 =====
    {"company": "字节跳动", "title": "2027届秋招提前批 - 研发岗（7.10全面开闸）", "source": "官方招聘"},
    {"company": "字节跳动", "title": "2027届ByteIntern实习转正（研发类4800+岗位）", "source": "官方招聘"},
    {"company": "腾讯", "title": "2027届秋招提前批 - TEG技术岗（7.11开启）", "source": "官方招聘"},
    {"company": "腾讯", "title": "2027届产品经理培训生", "source": "官方招聘"},
    {"company": "阿里巴巴", "title": "2027届秋招提前批 - 技术岗（6月开启）", "source": "官方招聘"},
    {"company": "阿里巴巴", "title": "2027届阿里星顶尖人才计划（7.2启动）", "source": "官方招聘"},
    {"company": "美团", "title": "2027届秋招提前批 - 3000+转正实习岗（7.9开启）", "source": "官方招聘"},
    {"company": "美团", "title": "2027届北斗计划 - 大模型/自动驾驶", "source": "官方招聘"},
    {"company": "百度", "title": "2027届秋招提前批 - 技术/产品/设计/AI方向（7.9开启）", "source": "官方招聘"},
    {"company": "京东", "title": "2027届秋招提前批 - JD YOUNG实习生计划（7.3开启）", "source": "官方招聘"},
    {"company": "拼多多", "title": "2027届秋招提前批 - 研发实习岗（7月中旬）", "source": "官方招聘"},
    {"company": "快手", "title": "2027届秋招正式批（7月起）", "source": "官方招聘"},
    {"company": "华为", "title": "2027届实习生招聘（3.15已启动）", "source": "官方招聘"},
    {"company": "滴滴", "title": "2027届秋储实习生（7.17启动）", "source": "官方招聘"},

    # ===== 外企科技 =====
    {"company": "微软", "title": "2027届暑期实习 - Software Engineer Intern", "source": "官方招聘"},
    {"company": "亚马逊", "title": "2027届校招 - AWS软件开发/后端", "source": "官方招聘"},
    {"company": "Shopee", "title": "2027届校招 - 研发/产品", "source": "官方招聘"},

    # ===== 金融科技 =====
    {"company": "同花顺", "title": "2027届提前批 - AI/算法/研发/产品/数据", "source": "官方招聘"},

    # ===== 新能源汽车 =====
    {"company": "蔚来", "title": "2027届校招 - 研发/产品/设计", "source": "官方招聘"},
    {"company": "理想汽车", "title": "2027届校招 - 智能驾驶/座舱", "source": "官方招聘"},
    {"company": "小鹏汽车", "title": "2027届校招 - 自动驾驶/智能座舱", "source": "官方招聘"},
    {"company": "比亚迪", "title": "2027届校招 - 研发/工程/管理", "source": "官方招聘"},
    {"company": "宁德时代", "title": "2027届校招 - 电池研发/工程", "source": "官方招聘"},

    # ===== 游戏公司 =====
    {"company": "米哈游", "title": "2027届校招 - 研发/美术/策划", "source": "官方招聘"},
    {"company": "网易游戏", "title": "2027届校招 - 游戏研发/策划/美术", "source": "官方招聘"},

    # ===== 咨询 =====
    {"company": "贝恩", "title": "2027届暑期实习", "source": "官方招聘"},
    {"company": "德勤", "title": "2027届科技咨询实习", "source": "官方招聘"},

    # ===== 快消 =====
    {"company": "联合利华", "title": "2027届管培生 - 市场/供应链/财务/研发", "source": "官方招聘"},
    {"company": "宝洁", "title": "2027届校招 - 管培生", "source": "官方招聘"},
]


def get_seed_urls() -> dict[str, str]:
    """返回公司名 → 校招官网 URL 的映射表。"""
    from qiuzhao.companies import COMPANIES

    url_map = {}
    for c in COMPANIES:
        url_map[c["name"]] = c["url"]
    return url_map


def get_company_url(company: str) -> str:
    """获取公司的校招官网链接（备选：手动映射）。"""
    url_map = get_seed_urls()
    return url_map.get(company, "")


def inject_seed_data(db_insert_fn) -> tuple[int, list[dict]]:
    """注入种子数据到数据库。

    Returns:
        (成功插入条数, 含 URL 的完整条目列表)
    """
    url_map = get_seed_urls()
    today = date.today().isoformat()
    count = 0
    items_with_url = []

    for pos in SEED_POSITIONS:
        url = url_map.get(pos["company"], "")
        if db_insert_fn(
            company=pos["company"],
            title=pos["title"],
            url=url,
            source=pos["source"],
            found_at=today,
        ):
            count += 1
        items_with_url.append({
            "company": pos["company"],
            "title": pos["title"],
            "url": url,
            "source": pos["source"],
        })

    return count, items_with_url
