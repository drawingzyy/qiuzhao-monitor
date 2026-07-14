"""种子数据 — 2027 届秋招已开放职位（已过滤纯工科技术岗）。

保留：产品、AI、管培、咨询、市场、金融、设计、运营等方向。
去除：嵌入式、硬件、电气、电池、自动化、电力等硬核工科岗。
"""

from datetime import date

SEED_POSITIONS = [
    # ===== 互联网 - 产品 & AI 方向 =====
    {"company": "腾讯", "title": "2027届产品经理培训生", "source": "join.qq.com"},
    {"company": "腾讯", "title": "2027届秋招提前批（7.11开启，含产品/AI方向）", "source": "join.qq.com"},
    {"company": "字节跳动", "title": "2027届秋招提前批（7.10开闸，含AI/产品方向）", "source": "jobs.bytedance.com"},
    {"company": "阿里巴巴", "title": "2027届阿里星顶尖人才计划 - AI方向（7.2启动）", "source": "talent.alibaba.com"},
    {"company": "阿里巴巴", "title": "2027届秋招提前批（6月开启，含AI/产品/运营）", "source": "talent.alibaba.com"},
    {"company": "百度", "title": "2027届秋招提前批 - AI/产品/设计方向（7.9开启）", "source": "talent.baidu.com"},
    {"company": "百度", "title": "2027届AIDU顶尖人才计划 - 大模型算法/AI产品", "source": "talent.baidu.com"},
    {"company": "美团", "title": "2027届秋招提前批 - 含产品/商业分析/AI方向（7.9开启）", "source": "zhaopin.meituan.com"},
    {"company": "美团", "title": "2027届北斗计划 - 大模型/自动驾驶（AI方向）", "source": "zhaopin.meituan.com"},
    {"company": "京东", "title": "2027届TET管培生（综合/物流/产品方向）", "source": "campus.jd.com"},
    {"company": "京东", "title": "2027届TGT天才青年计划 - 大模型/云计算", "source": "campus.jd.com"},
    {"company": "京东", "title": "2027届秋招提前批（7.3开启，含产品/运营）", "source": "campus.jd.com"},
    {"company": "快手", "title": "2027届快Star顶尖技术计划 - 大模型/推荐系统（AI方向）", "source": "zhaopin.kuaishou.cn"},
    {"company": "快手", "title": "2027届秋招正式批（7月起，含产品/运营/设计）", "source": "zhaopin.kuaishou.cn"},
    {"company": "拼多多", "title": "2027届云弧计划 - 大模型/商业分析", "source": "careers.pinduoduo.com"},
    {"company": "小红书", "title": "2027届秋招（含产品/运营/市场方向）", "source": "job.xiaohongshu.com"},
    {"company": "滴滴", "title": "2027届秋储实习生（7.17启动，含产品/运营）", "source": "campus.didiglobal.com"},
    {"company": "哔哩哔哩", "title": "2027届校招（含产品/运营/设计方向）", "source": "jobs.bilibili.com"},

    # ===== AI 专项 =====
    {"company": "大疆", "title": "2027届校招提前批 - AI算法/产品方向", "source": "we.dji.com"},
    {"company": "商汤科技", "title": "2027届校招 - 大模型/AI产品", "source": "sensetime.com"},
    {"company": "科大讯飞", "title": "2027届校招 - AI产品/运营", "source": "campus.iflytek.com"},

    # ===== 游戏 - 策划/美术/运营 =====
    {"company": "米哈游", "title": "2027届校招 - 策划/美术/运营", "source": "campus.mihoyo.com"},
    {"company": "网易游戏", "title": "2027届校招 - 游戏策划/美术/运营", "source": "game.campus.163.com"},
    {"company": "莉莉丝", "title": "2027届校招 - 游戏策划/运营", "source": "lilithgames.com"},

    # ===== 新能源汽车 - 产品/设计 =====
    {"company": "蔚来", "title": "2027届校招 - 产品/设计/用户运营", "source": "nio.com"},
    {"company": "理想汽车", "title": "2027届校招 - AI/产品/设计", "source": "lixiang.com"},
    {"company": "小鹏汽车", "title": "2027届校招 - AI产品/用户研究", "source": "xiaopeng.com"},
    {"company": "比亚迪", "title": "2027届校招 - 产品/管理培训生", "source": "job.byd.com"},
    {"company": "特斯拉", "title": "2027届校招 - 产品/市场方向", "source": "tesla.cn"},

    # ===== 外企科技 =====
    {"company": "微软", "title": "2027届暑期实习（含产品/市场方向）", "source": "careers.microsoft.com"},
    {"company": "亚马逊", "title": "2027届校招 - 产品/运营方向", "source": "amazon.jobs"},
    {"company": "Shopee", "title": "2027届校招 - 产品经理/运营", "source": "careers.shopee.cn"},
    {"company": "Apple", "title": "2027届校招 - 产品/市场方向", "source": "apple.com"},

    # ===== 金融/银行 =====
    {"company": "招商银行", "title": "2027届校招 - 总行管培生/金融科技", "source": "career.cmbchina.com"},
    {"company": "工商银行", "title": "2027届校招 - 总行管培生", "source": "job.icbc.com.cn"},
    {"company": "建设银行", "title": "2027届校招 - 总行管培生", "source": "job.ccb.com"},
    {"company": "中国银行", "title": "2027届校招 - 管培生/信科岗", "source": "campus.chinahr.com"},
    {"company": "农业银行", "title": "2027届校招 - 总行管培生", "source": "career.abchina.com"},
    {"company": "交通银行", "title": "2027届校招 - 管培生/金融科技", "source": "job.bankcomm.com"},
    {"company": "兴业银行", "title": "2027届校招 - 管培生/金融科技", "source": "campus.cib.com.cn"},
    {"company": "中金公司", "title": "2027届校招 - 投行/研究/财富管理", "source": "cicc.com"},
    {"company": "华泰证券", "title": "2027届校招 - 投行/研究/金融科技", "source": "htsc.com"},
    {"company": "东北证券", "title": "2027届暑期实习暨提前批 - 金融/研究/投行", "source": "nesc.cn"},
    {"company": "同花顺", "title": "2027届提前批 - AI/产品/数据", "source": "job.10jqka.com.cn"},

    # ===== 咨询 =====
    {"company": "麦肯锡", "title": "2027届校招 - 商业分析师/咨询顾问", "source": "mckinsey.com.cn"},
    {"company": "波士顿咨询", "title": "2027届校招 - 战略咨询", "source": "careers.bcg.com"},
    {"company": "贝恩", "title": "2027届暑期实习 - 咨询顾问", "source": "bain.com"},
    {"company": "德勤", "title": "2027届校招 - 咨询/审计/税务", "source": "deloitte.com"},
    {"company": "普华永道", "title": "2027届校招 - 咨询/审计", "source": "pwccn.com"},
    {"company": "安永", "title": "2027届校招 - 咨询/审计", "source": "ey.com"},
    {"company": "毕马威", "title": "2027届校招 - 咨询/审计", "source": "kpmg.com"},

    # ===== 快消管培 =====
    {"company": "宝洁", "title": "2027届校招 - 品牌管理/市场/销售管培生", "source": "pgcareers.com"},
    {"company": "联合利华", "title": "2027届管培生 - 市场/客户发展/财务/HR", "source": "careers.unilever.com.cn"},
    {"company": "欧莱雅", "title": "2027届SeedZ管培项目 - 市场/电商/财务/IT等11个方向", "source": "careers.loreal.com"},
    {"company": "玛氏", "title": "2027届管培生 - 市场/销售/供应链", "source": "careers.mars.com"},
    {"company": "可口可乐", "title": "2027届管培生 - 市场/财务/HR", "source": "coca-colacompany.com"},
    {"company": "百事", "title": "2027届校招 - 市场/销售管培生", "source": "pepsicojobs.com"},

    # ===== 外企咨询/综合管培 =====
    {"company": "凯捷中国", "title": "2027届校招 - 管理咨询/数字化咨询/数据分析", "source": "capgemini.com"},
    {"company": "IBM", "title": "2027届校招 - 咨询顾问/产品经理", "source": "ibm.com"},
    {"company": "SAP", "title": "2027届校招 - 产品/咨询/客户成功", "source": "sap.cn"},

    # ===== 国企/央企 - 管培方向 =====
    {"company": "中国移动", "title": "2027届校招 - 市场管培/产品经理", "source": "job.10086.cn"},
    {"company": "中国电信", "title": "2027届校招 - 产品/市场/运营", "source": "zhaopin.chinatelecom.com.cn"},
    {"company": "中国联通", "title": "2027届校招 - 产品/市场/运营", "source": "zglt.iguopin.com"},
    {"company": "中国银行", "title": "2027届校招 - 管培生（总行/分行）", "source": "campus.chinahr.com"},
    {"company": "南方电网", "title": "2027届校招 - 管理/经管类岗位", "source": "zhaopin.csg.cn"},
]


def get_seed_urls() -> dict[str, str]:
    """返回公司名 → 校招官网 URL 的映射表。"""
    from qiuzhao.companies import COMPANIES

    url_map = {}
    for c in COMPANIES:
        url_map[c["name"]] = c["url"]
    return url_map


def get_company_url(company: str) -> str:
    """获取公司的校招官网链接。"""
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
