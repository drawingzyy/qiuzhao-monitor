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

    # ===== 互联网大厂 - 管培/专项计划 =====
    {"company": "京东", "title": "2027届TET管培生（综合/物流/技术/产品方向）", "source": "官方招聘"},
    {"company": "京东", "title": "2027届TGT天才青年计划 - 多模态大模型/云计算", "source": "官方招聘"},
    {"company": "百度", "title": "2027届AIDU顶尖人才计划 - 大模型算法/自动驾驶/AI", "source": "官方招聘"},
    {"company": "快手", "title": "2027届快Star顶尖技术计划 - 大模型/音视频/推荐系统", "source": "官方招聘"},
    {"company": "拼多多", "title": "2027届云弧计划 - 大模型底层研发/商业分析", "source": "官方招聘"},
    {"company": "大疆", "title": "2027届校招提前批 - AI算法/嵌入式/机器人", "source": "官方招聘"},

    # ===== 外企科技 =====
    {"company": "微软", "title": "2027届暑期实习 - Software Engineer Intern", "source": "官方招聘"},
    {"company": "亚马逊", "title": "2027届校招 - AWS软件开发/后端", "source": "官方招聘"},
    {"company": "Shopee", "title": "2027届校招 - 研发/产品", "source": "官方招聘"},

    # ===== 金融/银行 =====
    {"company": "同花顺", "title": "2027届提前批 - AI/算法/研发/产品/数据", "source": "官方招聘"},
    {"company": "招商银行", "title": "2027届校招 - 金融科技/管培生", "source": "官方招聘"},
    {"company": "工商银行", "title": "2027届校招 - 总行管培/金融科技", "source": "官方招聘"},
    {"company": "建设银行", "title": "2027届校招 - 总行管培/科技岗", "source": "官方招聘"},
    {"company": "中国银行", "title": "2027届校招 - 管培生/信科岗", "source": "官方招聘"},
    {"company": "东北证券", "title": "2027届暑期实习暨提前批 - 金融/研究/投行/IT", "source": "官方招聘"},
    {"company": "中金公司", "title": "2027届校招 - 投行/研究/科技", "source": "官方招聘"},

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
    {"company": "麦肯锡", "title": "2027届校招 - 商业分析/咨询顾问", "source": "官方招聘"},
    {"company": "波士顿咨询", "title": "2027届校招 - 战略咨询", "source": "官方招聘"},
    {"company": "贝恩", "title": "2027届暑期实习", "source": "官方招聘"},
    {"company": "德勤", "title": "2027届科技咨询实习", "source": "官方招聘"},

    # ===== 快消管培 =====
    {"company": "联合利华", "title": "2027届管培生 - 市场/供应链/财务/研发", "source": "官方招聘"},
    {"company": "宝洁", "title": "2027届校招 - 品牌/市场/销售/研发管培生", "source": "官方招聘"},
    {"company": "欧莱雅", "title": "2027届SeedZ管培项目 - 市场/电商/财务/IT等11个方向", "source": "官方招聘"},
    {"company": "玛氏", "title": "2027届管培生 - 市场/销售/供应链", "source": "官方招聘"},
    {"company": "可口可乐", "title": "2027届管培生 - 市场/财务/供应链", "source": "官方招聘"},
    {"company": "百事", "title": "2027届校招 - 市场/销售管培生", "source": "官方招聘"},

    # ===== 外企咨询/科技管培 =====
    {"company": "施耐德电气", "title": "2027届校招 - 电气研发/自动化/财务/供应链", "source": "官方招聘"},
    {"company": "凯捷中国", "title": "2027届校招 - 管理咨询/数字化咨询/IT实施/数据分析", "source": "官方招聘"},
    {"company": "IBM", "title": "2027届校招 - 咨询/技术/研发", "source": "官方招聘"},
    {"company": "SAP", "title": "2027届校招 - 技术/产品/咨询", "source": "官方招聘"},

    # ===== 国企/央企 =====
    {"company": "国家电网", "title": "2027届校招 - 电力/信通/管理岗", "source": "官方招聘"},
    {"company": "中国移动", "title": "2027届校招 - 技术/政企/市场管培", "source": "官方招聘"},
    {"company": "中国电信", "title": "2027届校招 - 技术/产品/市场", "source": "官方招聘"},
    {"company": "中国联通", "title": "2027届校招 - IT/网络/市场", "source": "官方招聘"},

    # ===== 制造业 =====
    {"company": "宝钢股份", "title": "2027届校招 - 自动化/AI数字化/大数据（中国宝武）", "source": "官方招聘"},
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
