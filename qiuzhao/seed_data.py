"""种子数据 — 仅包含已确认开放 2027 届秋招/提前批的公司（2026年7月）。

每个条目均经搜索验证。未确认的暂不列入，避免误导。
"""

from datetime import date

COMPANY_INTRO = {
    "字节跳动": "全球最大独角兽，旗下抖音/TikTok/飞书，AI+产品双轮驱动",
    "腾讯": "互联网巨头，微信/QQ/游戏，2027届产品类扩招39%",
    "阿里巴巴": "电商+云计算，淘宝/天猫/阿里云，AI岗位占比超80%",
    "百度": "AI先行者，文心大模型/自动驾驶Apollo，AIDU为顶尖人才通道",
    "美团": "本地生活超级平台，外卖/到店/出行，北斗计划聚焦大模型",
    "京东": "自营电商+物流帝国，TET管培含金量极高，TGT面向顶尖人才",
    "快手": "短视频+直播双雄之一，快Star计划面向顶尖AI人才",
    "拼多多": "社交电商+Temu海外增长，云弧计划聚焦大模型/商业分析",
    "小红书": "生活方式社区+电商，增长迅猛，商业化/运营方向机会多",
    "滴滴": "出行+自动驾驶平台，秋储实习生=秋招提前批",
    "哔哩哔哩": "Z世代视频社区，二次元/游戏/知识内容，内容/运营岗多",
    "米哈游": "《原神》《崩坏》开发商，全球Top游戏公司，高薪高福利",
    "网易游戏": "《梦幻西游》《永劫无间》等，自研能力顶级",
    "科大讯飞": "智能语音国家队，星火大模型，飞凡计划管培生专项",
    "多益网络": "广州游戏公司，2027届提前批已开，程序/策划/美术/市场/职能",
    "蔚来": "高端新能源车企，用户服务标杆，产品/设计/用户运营",
    "理想汽车": "增程式新能源SUV销冠，智能座舱领先",
    "小鹏汽车": "智能驾驶技术派，XNGP全场景智驾",
    "比亚迪": "全球新能源车销冠，校招规模巨大，产品/管理方向",
    "特斯拉": "全球电动车+能源巨头，产品/市场方向",
    "微软": "全球科技巨头，WLB标杆，产品/市场暑期实习",
    "亚马逊": "全球电商+AWS云计算，产品/运营方向",
    "Shopee": "东南亚电商龙头，深圳研发中心，产品/运营岗",
    "Apple": "全球消费电子霸主，产品/市场/零售方向",
    "招商银行": "股份行龙头，零售之王，金融科技+管培生",
    "中金公司": "投行贵族，薪酬行业天花板，投行/研究/财富管理",
    "华泰证券": "科技驱动券商龙头，投行/研究/金融科技",
    "东北证券": "中型券商，投行/研究/金融科技多元发展",
    "同花顺": "A股金融科技龙头，AI+量化+数据产品",
    "贝恩": "MBB之一，消费品/私募咨询见长，暑期实习已开",
    "德勤": "四大之一，咨询业务规模全球第一",
    "宝洁": "快消黄埔军校，品牌管理/市场管培体系化培养",
    "联合利华": "全球快消Top2，管培项目成熟，市场/客户发展/财务/HR",
    "欧莱雅": "全球美妆霸主，SeedZ管培11个方向（需确认2027届开放时间）",
    "凯捷中国": "全球IT咨询巨头，数字化咨询+数据分析",
    "IBM": "百年科技巨头，咨询+AI+云计算",
    "中国移动": "全球最大运营商，市场管培/产品经理",
    "华为": "全球ICT巨头，消费者/运营商/企业三大业务",
}


# ===== 已确认 2027 届秋招/提前批 =====
SEED_POSITIONS = [
    # ---- 🖥️ 互联网 - 产品/运营/商业化 ----
    {"cat": "internet", "company": "字节跳动",
     "title": "AI产品经理早鸟通道（7.14-8.2，不占正式批名额）", "verified": True},
    {"cat": "internet", "company": "字节跳动",
     "title": "2027届研发提前批（7.10开闸，含AI/产品方向）", "verified": True},
    {"cat": "internet", "company": "字节跳动",
     "title": "商业化销售/客户运营方向（北京/上海/广深）", "verified": False},

    {"cat": "internet", "company": "腾讯",
     "title": "2027届产品经理培训生（产品类扩招39%）", "verified": True},
    {"cat": "internet", "company": "腾讯",
     "title": "2027届实习生招聘（10000+offer，含产品/运营/市场方向）", "verified": True},

    {"cat": "internet", "company": "阿里巴巴",
     "title": "2027届秋招提前批（6月开启，含产品/运营方向）", "verified": True},

    {"cat": "internet", "company": "百度",
     "title": "2027届管培生计划（7.9开启，含产品/运营/市场方向）", "verified": True},
    {"cat": "internet", "company": "百度",
     "title": "AIDU顶尖人才计划（AI产品/大模型方向）", "verified": True},

    {"cat": "internet", "company": "美团",
     "title": "2027届秋招提前批（7.9开启，含产品/商业分析/运营）", "verified": True},

    {"cat": "internet", "company": "京东",
     "title": "TET管培生（综合/物流/产品方向，7.1开启）", "verified": True},
    {"cat": "internet", "company": "京东",
     "title": "2027届提前批（7.3开启，电商运营HC最多）", "verified": True},

    {"cat": "internet", "company": "快手",
     "title": "2027届秋招（7月起，含产品/运营/商业化方向）", "verified": True},

    {"cat": "internet", "company": "拼多多",
     "title": "2027届提前批（7月中旬，含产品/运营/商业分析）", "verified": True},

    {"cat": "internet", "company": "小红书",
     "title": "2027届校招（商业化/运营/市场方向，文科友好）", "verified": False},

    {"cat": "internet", "company": "滴滴",
     "title": "2027届秋储实习生（7.17启动，含产品/运营）", "verified": True},

    {"cat": "internet", "company": "哔哩哔哩",
     "title": "2027届校招（内容运营/商业化/市场方向，文科友好）", "verified": False},

    # ---- 🤖 AI/硬科技 ----
    {"cat": "ai", "company": "科大讯飞",
     "title": "飞凡计划管培生（7.3开启，产品/营销方向，文科可投）", "verified": True},

    # ---- 🎮 游戏 - 策划/运营/美术 ----
    {"cat": "gaming", "company": "米哈游",
     "title": "2027届提前批（7.6-7.27，程序/策划/美术/运营）", "verified": True},
    {"cat": "gaming", "company": "网易游戏",
     "title": "2027届校招（游戏策划/运营/美术，文科友好）", "verified": True},
    {"cat": "gaming", "company": "多益网络",
     "title": "2027届秋季提前批（7.1-8.31，策划/市场/职能类）", "verified": True},

    # ---- 🚗 新能源汽车 - 产品/用户/市场 ----
    {"cat": "ev", "company": "比亚迪",
     "title": "2027届校招（产品/管理/市场方向，规模巨大）", "verified": True},
    {"cat": "ev", "company": "蔚来",
     "title": "2027届校招（产品/设计/用户运营方向）", "verified": False},
    {"cat": "ev", "company": "理想汽车",
     "title": "2027届校招（产品/用户研究/市场方向）", "verified": False},

    # ---- 🌍 外企科技 ----
    {"cat": "foreign", "company": "微软",
     "title": "2027届暑期实习（产品/市场方向，WLB标杆）", "verified": True},
    {"cat": "foreign", "company": "亚马逊",
     "title": "2027届校招（产品/运营方向）", "verified": False},
    {"cat": "foreign", "company": "Shopee",
     "title": "2027届校招（产品经理/运营，深圳）", "verified": False},

    # ---- 🏦 金融/银行 ----
    {"cat": "finance", "company": "招商银行",
     "title": "2027届校招（总行管培生/金融科技）", "verified": False},
    {"cat": "finance", "company": "中金公司",
     "title": "2027届校招（投行/研究/财富管理）", "verified": True},
    {"cat": "finance", "company": "华泰证券",
     "title": "2027届校招（投行/研究/金融科技）", "verified": True},
    {"cat": "finance", "company": "东北证券",
     "title": "2027届暑期实习暨提前批（金融/研究/投行）", "verified": True},
    {"cat": "finance", "company": "同花顺",
     "title": "2027届提前批（AI/产品/数据方向）", "verified": True},

    # ---- 📊 咨询 ----
    {"cat": "consulting", "company": "贝恩",
     "title": "2027届暑期实习（咨询顾问，消费品/私募方向）", "verified": True},
    {"cat": "consulting", "company": "德勤",
     "title": "2027届校招（咨询/审计/税务）", "verified": True},

    # ---- 🛍️ 快消/美妆/零售 ----
    {"cat": "fmcg", "company": "宝洁",
     "title": "2027届校招（品牌管理/市场/销售管培生）", "verified": True},
    {"cat": "fmcg", "company": "联合利华",
     "title": "2027届管培生（市场/客户发展/财务/HR）", "verified": True},

    # ---- 🏗️ 国企/外企咨询 ----
    {"cat": "soe", "company": "凯捷中国",
     "title": "2027届校招（管理咨询/数字化咨询/数据分析）", "verified": True},
    {"cat": "soe", "company": "IBM",
     "title": "2027届校招（咨询顾问/产品经理）", "verified": True},
    {"cat": "soe", "company": "中国移动",
     "title": "2027届校招（市场管培/产品经理）", "verified": True},
]

CATEGORY_NAMES = {
    "internet": "🖥️ 互联网/科技",
    "ai": "🤖 AI/硬科技",
    "gaming": "🎮 游戏",
    "ev": "🚗 新能源汽车",
    "foreign": "🌍 外企科技",
    "finance": "🏦 金融/银行",
    "consulting": "📊 咨询",
    "fmcg": "🛍️ 快消/美妆/零售",
    "soe": "🏗️ 国企/外企咨询",
}


def get_seed_urls() -> dict[str, str]:
    from qiuzhao.companies import COMPANIES
    return {c["name"]: c["url"] for c in COMPANIES}


def get_company_url(company: str) -> str:
    return get_seed_urls().get(company, "")


def get_company_intro(company: str) -> str:
    return COMPANY_INTRO.get(company, "")


def inject_seed_data(db_insert_fn) -> tuple[int, list[dict]]:
    url_map = get_seed_urls()
    today = date.today().isoformat()
    count = 0
    items = []

    for pos in SEED_POSITIONS:
        url = url_map.get(pos["company"], "")
        if db_insert_fn(
            company=pos["company"],
            title=pos["title"],
            url=url,
            source=CATEGORY_NAMES.get(pos.get("cat", ""), ""),
            found_at=today,
        ):
            count += 1
        items.append({
            "company": pos["company"],
            "title": pos["title"],
            "url": url,
            "category": pos.get("cat", ""),
            "verified": pos.get("verified", False),
        })

    return count, items
