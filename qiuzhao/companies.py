"""公司列表配置 — 200+ 重点公司的校招页面信息。

支持三种类型:
- moka: 使用 Moka 招聘系统 (可直调 JSON API)
- api: 有可用的内嵌 API
- html: 需要 HTML 解析 (默认)
"""

COMPANIES = [
    # ===== 互联网/科技 =====
    {"name": "字节跳动", "url": "https://jobs.bytedance.com/campus/", "type": "api"},
    {"name": "腾讯", "url": "https://join.qq.com/", "type": "html"},
    {"name": "阿里巴巴", "url": "https://talent.alibaba.com/campus/", "type": "html"},
    {"name": "蚂蚁集团", "url": "https://talent.antgroup.com/campus/", "type": "html"},
    {"name": "美团", "url": "https://zhaopin.meituan.com/web/campus", "type": "moka"},
    {"name": "百度", "url": "https://talent.baidu.com/jobs/campus", "type": "html"},
    {"name": "京东", "url": "https://campus.jd.com/", "type": "html"},
    {"name": "网易", "url": "https://campus.163.com/", "type": "html"},
    {"name": "快手", "url": "https://zhaopin.kuaishou.cn/", "type": "moka"},
    {"name": "小红书", "url": "https://job.xiaohongshu.com/campus", "type": "html"},
    {"name": "拼多多", "url": "https://careers.pinduoduo.com/campus", "type": "html"},
    {"name": "滴滴", "url": "https://campus.didiglobal.com/", "type": "html"},
    {"name": "哔哩哔哩", "url": "https://jobs.bilibili.com/campus/", "type": "html"},
    {"name": "携程", "url": "https://campus.ctrip.com/", "type": "html"},
    {"name": "SHEIN", "url": "https://app.mokahr.com/campus-recruitment/shein/", "type": "moka"},
    {"name": "猿辅导", "url": "https://hr.yuanfudao.com/campus/", "type": "moka"},

    # ===== 硬件/通信 =====
    {"name": "华为", "url": "https://career.huawei.com/", "type": "html"},
    {"name": "荣耀", "url": "https://www.hihonor.com/cn/career/", "type": "html"},
    {"name": "小米", "url": "https://xiaomi.jobs.f.mioffice.cn/campus/", "type": "moka"},
    {"name": "OPPO", "url": "https://career.oppo.com/campus/", "type": "html"},
    {"name": "vivo", "url": "https://hr.vivo.com/campus/", "type": "html"},
    {"name": "大疆", "url": "https://we.dji.com/cn/campus", "type": "html"},
    {"name": "中兴通讯", "url": "https://job.zte.com.cn/campus/", "type": "html"},
    {"name": "联想", "url": "https://talent.lenovo.com.cn/campus", "type": "html"},
    {"name": "海康威视", "url": "https://campushr.hikvision.com/", "type": "html"},
    {"name": "科大讯飞", "url": "https://campus.iflytek.com/", "type": "html"},
    {"name": "商汤科技", "url": "https://www.sensetime.com/cn/careers", "type": "html"},
    {"name": "旷视科技", "url": "https://www.megvii.com/careers/", "type": "html"},

    # ===== 新能源汽车 =====
    {"name": "比亚迪", "url": "https://job.byd.com/", "type": "html"},
    {"name": "蔚来", "url": "https://www.nio.com/cn/careers", "type": "html"},
    {"name": "理想汽车", "url": "https://www.lixiang.com/careers", "type": "html"},
    {"name": "小鹏汽车", "url": "https://xiaopeng.com/careers", "type": "html"},
    {"name": "特斯拉", "url": "https://www.tesla.cn/careers", "type": "html"},
    {"name": "宁德时代", "url": "https://www.catl.com/careers/", "type": "html"},
    {"name": "吉利汽车", "url": "https://campus.geely.com/", "type": "html"},
    {"name": "长城汽车", "url": "https://www.gwm.com.cn/careers", "type": "html"},

    # ===== 金融/银行 =====
    {"name": "招商银行", "url": "https://career.cmbchina.com/", "type": "html"},
    {"name": "工商银行", "url": "https://job.icbc.com.cn/", "type": "html"},
    {"name": "中国银行", "url": "https://campus.chinahr.com/pages/boc/", "type": "html"},
    {"name": "建设银行", "url": "https://job.ccb.com/", "type": "html"},
    {"name": "农业银行", "url": "https://career.abchina.com/", "type": "html"},
    {"name": "交通银行", "url": "https://job.bankcomm.com/", "type": "html"},
    {"name": "兴业银行", "url": "https://campus.cib.com.cn/", "type": "html"},
    {"name": "中金公司", "url": "https://www.cicc.com/careers", "type": "html"},
    {"name": "华泰证券", "url": "https://www.htsc.com.cn/recruitment/", "type": "html"},
    {"name": "中信证券", "url": "https://www.citics.com/careers/", "type": "html"},
    {"name": "蚂蚁集团", "url": "https://talent.antgroup.com/campus/", "type": "html"},
    {"name": "同花顺", "url": "https://job.10jqka.com.cn/", "type": "html"},

    # ===== 外企科技 =====
    {"name": "微软", "url": "https://careers.microsoft.com/", "type": "html"},
    {"name": "Google", "url": "https://careers.google.com/", "type": "html"},
    {"name": "亚马逊", "url": "https://www.amazon.jobs/zh/", "type": "html"},
    {"name": "Apple", "url": "https://www.apple.com/careers/cn/", "type": "html"},
    {"name": "英特尔", "url": "https://www.intel.cn/content/www/cn/zh/jobs/", "type": "html"},
    {"name": "高通", "url": "https://www.qualcomm.com/company/careers", "type": "html"},
    {"name": "PayPal", "url": "https://www.paypal.com/us/webapps/mpp/jobs", "type": "html"},
    {"name": "Shopee", "url": "https://careers.shopee.cn/", "type": "html"},
    {"name": "惠普", "url": "https://jobs.hp.com/", "type": "html"},
    {"name": "戴尔", "url": "https://jobs.dell.com/", "type": "html"},
    {"name": "IBM", "url": "https://www.ibm.com/careers/cn-zh/", "type": "html"},
    {"name": "SAP", "url": "https://www.sap.cn/about/careers.html", "type": "html"},

    # ===== 咨询 =====
    {"name": "麦肯锡", "url": "https://www.mckinsey.com.cn/careers/", "type": "html"},
    {"name": "波士顿咨询", "url": "https://careers.bcg.com/", "type": "html"},
    {"name": "贝恩", "url": "https://www.bain.com/careers/", "type": "html"},
    {"name": "德勤", "url": "https://www.deloitte.com/cn/zh/careers.html", "type": "html"},
    {"name": "普华永道", "url": "https://www.pwccn.com/zh/careers.html", "type": "html"},
    {"name": "安永", "url": "https://www.ey.com/zh_cn/careers", "type": "html"},
    {"name": "毕马威", "url": "https://home.kpmg/cn/zh/home/careers.html", "type": "html"},

    # ===== 快消 =====
    {"name": "宝洁", "url": "https://www.pgcareers.com/", "type": "html"},
    {"name": "联合利华", "url": "https://careers.unilever.com.cn/", "type": "html"},
    {"name": "欧莱雅", "url": "https://careers.loreal.com/", "type": "html"},
    {"name": "玛氏", "url": "https://careers.mars.com/", "type": "html"},
    {"name": "可口可乐", "url": "https://www.coca-colacompany.com/careers", "type": "html"},
    {"name": "百事", "url": "https://www.pepsicojobs.com/", "type": "html"},

    # ===== 国企/央企 =====
    {"name": "国家电网", "url": "https://zhaopin.sgcc.com.cn/", "type": "html"},
    {"name": "南方电网", "url": "https://zhaopin.csg.cn/", "type": "html"},
    {"name": "中国移动", "url": "https://job.10086.cn/", "type": "html"},
    {"name": "中国电信", "url": "https://zhaopin.chinatelecom.com.cn/", "type": "html"},
    {"name": "中国联通", "url": "https://zglt.iguopin.com/", "type": "html"},
    {"name": "中石油", "url": "https://zhaopin.cnpc.com.cn/", "type": "html"},
    {"name": "中石化", "url": "https://job.sinopec.com/", "type": "html"},
    {"name": "中国建筑", "url": "https://cscec.iguopin.com/", "type": "html"},
    {"name": "中国航天", "url": "https://zhaopin.spacechina.com/", "type": "html"},

    # ===== 生物医药 =====
    {"name": "药明康德", "url": "https://www.wuxiapptec.com/careers", "type": "html"},
    {"name": "恒瑞医药", "url": "https://www.hengrui.com/careers", "type": "html"},
    {"name": "百济神州", "url": "https://www.beigene.com.cn/careers/", "type": "html"},

    # ===== 游戏 =====
    {"name": "米哈游", "url": "https://campus.mihoyo.com/", "type": "html"},
    {"name": "腾讯游戏", "url": "https://join.qq.com/", "type": "html"},
    {"name": "网易游戏", "url": "https://game.campus.163.com/", "type": "html"},
    {"name": "同花顺", "url": "https://job.10jqka.com.cn/", "type": "html"},
    {"name": "宁德时代", "url": "https://www.catl.com/careers/", "type": "html"},
    {"name": "莉莉丝", "url": "https://lilithgames.com/careers/", "type": "html"},
    {"name": "鹰角网络", "url": "https://ak.hypergryph.com/", "type": "html"},
    {"name": "大疆", "url": "https://we.dji.com/cn/campus", "type": "html"},

    # ===== 制造业/工业 =====
    {"name": "施耐德电气", "url": "https://www.se.com/cn/zh/about-us/careers/", "type": "html"},
    {"name": "凯捷中国", "url": "https://www.capgemini.com/cn-zh/careers/", "type": "html"},
    {"name": "宝钢股份", "url": "https://zhaopin.baosteel.com/", "type": "html"},
    {"name": "东北证券", "url": "https://www.nesc.cn/recruitment/", "type": "html"},
]
