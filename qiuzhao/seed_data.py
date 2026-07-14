"""种子数据 — 2027 届秋招已开放职位（已验证+分类+公司简介）。

分类体系:
  internet   = 互联网/科技
  ai_hardtech = AI/硬科技
  gaming     = 游戏
  ev         = 新能源汽车
  foreign    = 外企科技
  finance    = 金融/银行
  consulting = 咨询/四大
  fmcg       = 快消
  soe        = 国企/央企

每条记录新增 verified 字段: 是否已通过搜索验证
"""

from datetime import date

# ===== 公司简介库 =====
COMPANY_INTRO = {
    "字节跳动": "全球最大独角兽，旗下抖音/TikTok/飞书等产品，AI岗位需求旺盛",
    "腾讯": "中国最大互联网公司之一，微信/QQ/游戏帝国，产品类扩招39%",
    "阿里巴巴": "电商+云计算巨头，淘宝/天猫/阿里云，AI岗位占比超80%",
    "百度": "AI先行者，文心大模型/自动驾驶Apollo，AIDU计划为顶尖人才通道",
    "美团": "本地生活超级平台，外卖/到店/出行，北斗计划聚焦大模型/自动驾驶",
    "京东": "自营电商+物流帝国，TET管培生计划含金量极高，TGT面向顶尖技术人才",
    "快手": "短视频+直播双雄之一，快Star计划面向顶尖AI人才",
    "拼多多": "社交电商巨头+Temu海外增长，云弧计划聚焦大模型/商业分析",
    "小红书": "生活方式社区+电商，增长迅猛，扁平化年轻文化",
    "滴滴": "出行平台，自动驾驶+国际化业务",
    "哔哩哔哩": "Z世代视频社区，二次元/游戏/知识内容生态",
    "大疆": "全球无人机霸主，AI算法+机器人前沿",
    "商汤科技": "AI四小龙之一，大模型+计算机视觉",
    "科大讯飞": "智能语音国家队，星火大模型+AI教育",
    "米哈游": "《原神》《崩坏》开发商，全球Top游戏公司，高薪+高福利",
    "网易游戏": "《梦幻西游》《永劫无间》等，自研能力顶级",
    "莉莉丝": "《万国觉醒》《剑与远征》开发商，出海SLG王者",
    "蔚来": "高端新能源车企，用户服务标杆，换电模式开创者",
    "理想汽车": "增程式新能源SUV销冠，智能座舱领先",
    "小鹏汽车": "智能驾驶技术派，XNGP全场景智驾",
    "比亚迪": "全球新能源车销冠，电池+整车垂直整合，校招规模巨大",
    "特斯拉": "全球电动车+能源巨头，FSD自动驾驶+Optimus机器人",
    "微软": "全球科技巨头，Windows/Azure/Office，WLB标杆",
    "亚马逊": "全球电商+云计算(AWS)巨头，中国主要招AWS+跨境电商方向",
    "Shopee": "东南亚电商龙头，母公司Sea集团，深圳研发中心",
    "Apple": "全球消费电子霸主，中国主要招供应链+零售+研发",
    "招商银行": "股份行龙头，零售之王，金融科技投入行业领先",
    "工商银行": "宇宙行，全球最大商业银行，总行管培含金量高",
    "建设银行": "国有大行，基建金融+金融科技双轮驱动",
    "中国银行": "国际化程度最高的国有银行，跨境金融+管培项目",
    "农业银行": "服务三农+数字化转型，总行管培+金融科技双通道",
    "交通银行": "国有大行，总部上海，金融科技转型先锋",
    "兴业银行": "绿色金融+同业之王，总行在福州，金融科技投入大",
    "中金公司": "投行贵族，IPO/并购头部券商，薪酬行业天花板",
    "华泰证券": "科技驱动券商龙头，涨乐财富通+机构业务双强",
    "东北证券": "中型券商，投行/研究/金融科技多元发展",
    "同花顺": "A股金融科技龙头，AI+量化+数据产品",
    "麦肯锡": "全球战略咨询Top1，薪资天花板，竞争极度激烈",
    "波士顿咨询": "MBB之一，战略咨询+数字化转型双轮驱动",
    "贝恩": "MBB之一，以消费品/私募咨询见长，文化温和",
    "德勤": "四大会计事务所之一，咨询业务规模全球第一",
    "普华永道": "四大之一，审计+咨询+税务全覆盖",
    "安永": "四大之一，审计+咨询双强，近年科技咨询增长快",
    "毕马威": "四大之一，审计+咨询+税务，金融服务行业优势明显",
    "宝洁": "快消黄埔军校，品牌管理/市场管培体系化培养",
    "联合利华": "全球快消Top2，旗下清扬/力士/梦龙等品牌，管培生项目成熟",
    "欧莱雅": "全球美妆霸主，SeedZ管培11个方向，巴黎总部轮岗机会",
    "玛氏": "全球最大食品公司之一，旗下德芙/士力架/M&M's，管培生培养体系完善",
    "可口可乐": "全球饮料巨头，品牌/市场管培+数字化营销方向",
    "百事": "全球食品饮料Top2，旗下百事可乐/乐事/桂格，市场/销售管培",
    "凯捷中国": "全球IT咨询巨头，数字化咨询+IT实施+数据分析",
    "IBM": "百年科技巨头，咨询+AI+云计算，蓝色巨人",
    "SAP": "全球最大企业管理软件公司，ERP/云计算/AI",
    "中国移动": "全球最大运营商，政企数字化+移动互联网",
    "中国电信": "三大运营商之一，天翼云+数字化转型",
    "中国联通": "三大运营商之一，混改先锋+产业互联网",
    "南方电网": "两大电网之一，数字化转型+智能电网",
}


SEED_POSITIONS = [
    # ==========================================
    # 🖥️ 互联网/科技
    # ==========================================
    {"category": "internet", "company": "字节跳动", "title": "AI产品经理早鸟通道（7.14-8.2，不占正式批名额）",
     "verified": True, "note": "官方已确认开放"},
    {"category": "internet", "company": "字节跳动", "title": "2027届研发提前批（7.10开闸，含AI/产品方向）",
     "verified": True},
    {"category": "internet", "company": "腾讯", "title": "2027届产品经理培训生（产品类扩招39%）",
     "verified": True, "note": "实习生招聘已启动，正式秋招预计8月"},
    {"category": "internet", "company": "腾讯", "title": "2027届实习生招聘（10000+offer，含AI产品/游戏策划/运营）",
     "verified": True},
    {"category": "internet", "company": "阿里巴巴", "title": "2027届阿里星顶尖人才计划 - AI方向",
     "verified": True},
    {"category": "internet", "company": "阿里巴巴", "title": "2027届秋招提前批（6月开启，含AI/产品/运营）",
     "verified": True},
    {"category": "internet", "company": "百度", "title": "2027届AIDU顶尖人才计划 - 大模型/AI产品",
     "verified": True},
    {"category": "internet", "company": "百度", "title": "2027届秋招提前批 - AI/产品/设计方向（7.9开启）",
     "verified": True},
    {"category": "internet", "company": "美团", "title": "2027届秋招提前批 - 含产品/商业分析/AI方向（7.9开启）",
     "verified": True},
    {"category": "internet", "company": "美团", "title": "2027届北斗计划 - 大模型/自动驾驶（顶尖人才通道）",
     "verified": True, "note": "全职岗7.3已截止，实习岗全年开放"},
    {"category": "internet", "company": "京东", "title": "2027届TET管培生（综合/物流/产品方向，含金量极高）",
     "verified": True},
    {"category": "internet", "company": "京东", "title": "2027届TGT天才青年计划 - 大模型/云计算",
     "verified": True},
    {"category": "internet", "company": "京东", "title": "2027届秋招提前批（7.3开启，含产品/运营方向）",
     "verified": True},
    {"category": "internet", "company": "快手", "title": "2027届快Star顶尖计划 - 大模型/推荐系统（AI方向）",
     "verified": True},
    {"category": "internet", "company": "快手", "title": "2027届秋招（7月起，含产品/运营/设计方向）",
     "verified": True},
    {"category": "internet", "company": "拼多多", "title": "2027届云弧计划 - 大模型/商业分析",
     "verified": True},
    {"category": "internet", "company": "小红书", "title": "2027届校招（含产品/运营/市场方向）",
     "verified": False},
    {"category": "internet", "company": "滴滴", "title": "2027届秋储实习生（7.17启动，含产品/运营方向）",
     "verified": True},
    {"category": "internet", "company": "哔哩哔哩", "title": "2027届校招（含产品/运营/设计方向）",
     "verified": False},

    # ==========================================
    # 🤖 AI/硬科技
    # ==========================================
    {"category": "ai_hardtech", "company": "大疆", "title": "2027届校招提前批 - AI算法/产品方向",
     "verified": True},
    {"category": "ai_hardtech", "company": "商汤科技", "title": "2027届校招 - 大模型/AI产品",
     "verified": False},
    {"category": "ai_hardtech", "company": "科大讯飞", "title": "2027届校招 - AI产品/运营（星火大模型方向）",
     "verified": False},

    # ==========================================
    # 🎮 游戏
    # ==========================================
    {"category": "gaming", "company": "米哈游", "title": "2027届校招 - 策划/美术/运营",
     "verified": True},
    {"category": "gaming", "company": "网易游戏", "title": "2027届校招 - 游戏策划/美术/运营",
     "verified": True},
    {"category": "gaming", "company": "莉莉丝", "title": "2027届校招 - 游戏策划/运营",
     "verified": False},

    # ==========================================
    # 🚗 新能源汽车
    # ==========================================
    {"category": "ev", "company": "蔚来", "title": "2027届校招 - 产品/设计/用户运营",
     "verified": False},
    {"category": "ev", "company": "理想汽车", "title": "2027届校招 - AI产品/用户研究",
     "verified": False},
    {"category": "ev", "company": "小鹏汽车", "title": "2027届校招 - AI产品/用户研究",
     "verified": False},
    {"category": "ev", "company": "比亚迪", "title": "2027届校招 - 产品/管理培训生",
     "verified": True},
    {"category": "ev", "company": "特斯拉", "title": "2027届校招 - 产品/市场方向",
     "verified": False},

    # ==========================================
    # 🌍 外企科技
    # ==========================================
    {"category": "foreign", "company": "微软", "title": "2027届暑期实习（含产品/市场方向）",
     "verified": True},
    {"category": "foreign", "company": "亚马逊", "title": "2027届校招 - 产品/运营方向",
     "verified": True},
    {"category": "foreign", "company": "Shopee", "title": "2027届校招 - 产品经理/运营",
     "verified": False},
    {"category": "foreign", "company": "Apple", "title": "2027届校招 - 产品/市场方向",
     "verified": False},

    # ==========================================
    # 🏦 金融/银行
    # ==========================================
    {"category": "finance", "company": "招商银行", "title": "2027届校招 - 总行管培生/金融科技",
     "verified": True},
    {"category": "finance", "company": "工商银行", "title": "2027届校招 - 总行管培生",
     "verified": False},
    {"category": "finance", "company": "建设银行", "title": "2027届校招 - 总行管培生",
     "verified": False},
    {"category": "finance", "company": "中国银行", "title": "2027届校招 - 管培生/信科岗",
     "verified": False},
    {"category": "finance", "company": "农业银行", "title": "2027届校招 - 总行管培生",
     "verified": False},
    {"category": "finance", "company": "交通银行", "title": "2027届校招 - 管培生/金融科技",
     "verified": False},
    {"category": "finance", "company": "兴业银行", "title": "2027届校招 - 管培生/金融科技",
     "verified": False},
    {"category": "finance", "company": "中金公司", "title": "2027届校招 - 投行/研究/财富管理",
     "verified": True},
    {"category": "finance", "company": "华泰证券", "title": "2027届校招 - 投行/研究/金融科技",
     "verified": True},
    {"category": "finance", "company": "东北证券", "title": "2027届暑期实习暨提前批 - 金融/研究/投行",
     "verified": True},
    {"category": "finance", "company": "同花顺", "title": "2027届提前批 - AI/产品/数据",
     "verified": True},

    # ==========================================
    # 📊 咨询/四大
    # ==========================================
    {"category": "consulting", "company": "麦肯锡", "title": "2027届校招 - 商业分析师/咨询顾问",
     "verified": False},
    {"category": "consulting", "company": "波士顿咨询", "title": "2027届校招 - 战略咨询",
     "verified": False},
    {"category": "consulting", "company": "贝恩", "title": "2027届暑期实习 - 咨询顾问",
     "verified": True},
    {"category": "consulting", "company": "德勤", "title": "2027届校招 - 咨询/审计/税务",
     "verified": True},
    {"category": "consulting", "company": "普华永道", "title": "2027届校招 - 咨询/审计",
     "verified": False},
    {"category": "consulting", "company": "安永", "title": "2027届校招 - 咨询/审计",
     "verified": False},
    {"category": "consulting", "company": "毕马威", "title": "2027届校招 - 咨询/审计",
     "verified": False},

    # ==========================================
    # 🛍️ 快消
    # ==========================================
    {"category": "fmcg", "company": "宝洁", "title": "2027届校招 - 品牌管理/市场/销售管培生",
     "verified": True},
    {"category": "fmcg", "company": "联合利华", "title": "2027届管培生 - 市场/客户发展/财务/HR",
     "verified": True},
    {"category": "fmcg", "company": "欧莱雅", "title": "2027届SeedZ管培 - 市场/电商/财务/IT等11个方向",
     "verified": True},
    {"category": "fmcg", "company": "玛氏", "title": "2027届管培生 - 市场/销售/供应链",
     "verified": False},
    {"category": "fmcg", "company": "可口可乐", "title": "2027届管培生 - 市场/财务/HR",
     "verified": False},
    {"category": "fmcg", "company": "百事", "title": "2027届校招 - 市场/销售管培生",
     "verified": False},

    # ==========================================
    # 🏗️ 国企/央企 + 外企咨询
    # ==========================================
    {"category": "soe", "company": "凯捷中国", "title": "2027届校招 - 管理咨询/数字化咨询/数据分析",
     "verified": True},
    {"category": "soe", "company": "IBM", "title": "2027届校招 - 咨询顾问/产品经理",
     "verified": True},
    {"category": "soe", "company": "SAP", "title": "2027届校招 - 产品/咨询/客户成功",
     "verified": False},
    {"category": "soe", "company": "中国移动", "title": "2027届校招 - 市场管培/产品经理",
     "verified": True},
    {"category": "soe", "company": "中国电信", "title": "2027届校招 - 产品/市场/运营",
     "verified": False},
    {"category": "soe", "company": "中国联通", "title": "2027届校招 - 产品/市场/运营",
     "verified": False},
    {"category": "soe", "company": "南方电网", "title": "2027届校招 - 管理/经管类岗位",
     "verified": False},
]

# 分类中文名映射
CATEGORY_NAMES = {
    "internet": "🖥️ 互联网/科技",
    "ai_hardtech": "🤖 AI/硬科技",
    "gaming": "🎮 游戏",
    "ev": "🚗 新能源汽车",
    "foreign": "🌍 外企科技",
    "finance": "🏦 金融/银行",
    "consulting": "📊 咨询/四大",
    "fmcg": "🛍️ 快消",
    "soe": "🏗️ 国企/外企咨询",
}


def get_seed_urls() -> dict[str, str]:
    from qiuzhao.companies import COMPANIES
    return {c["name"]: c["url"] for c in COMPANIES}


def get_company_url(company: str) -> str:
    url_map = get_seed_urls()
    return url_map.get(company, "")


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
            source=CATEGORY_NAMES.get(pos.get("category", ""), ""),
            found_at=today,
        ):
            count += 1
        items.append({
            "company": pos["company"],
            "title": pos["title"],
            "url": url,
            "category": pos.get("category", ""),
            "verified": pos.get("verified", False),
            "note": pos.get("note", ""),
        })

    return count, items
