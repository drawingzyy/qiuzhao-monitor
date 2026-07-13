# 🍂 秋招信息每日推送系统

每天自动扫描多个渠道的秋招/校招信息，通过微信推送给你，不错过任何一家公司的秋招开放。

## 数据来源

- ✅ **牛客网** — 校招讨论区
- 🚧 **Boss直聘** — 校招职位搜索 (开发中)
- 🚧 **公司官网** — 30+ 重点公司招聘页 (开发中)
- 🚧 **微信招聘号** — 公众号文章搜索 (开发中)
- 🚧 **小红书** — 招聘信息搜索 (开发中)

## 快速开始

### 1. 获取 PushPlus Token

访问 [pushplus.plus](http://pushplus.plus) 注册，获取你的 Token。

### 2. 配置

```bash
cp .env.example .env
# 编辑 .env，填入你的 PUSHPLUS_TOKEN
```

### 3. 本地运行

```bash
pip install -r requirements.txt
python -m qiuzhao.main
```

### 4. 部署到 GitHub Actions

1. Fork 本仓库
2. 在 Settings → Secrets and variables → Actions 中添加:
   - **Secret**: `PUSHPLUS_TOKEN` = 你的 PushPlus Token
3. GitHub Actions 会在每天北京时间 8:00 自动运行
4. 也可以手动触发: Actions → Daily Qiuzhao Scan → Run workflow

## 项目结构

```
qiuzhao-monitor/
├── .github/workflows/daily-scan.yml  # GitHub Actions 定时任务
├── qiuzhao/
│   ├── main.py                       # 主入口
│   ├── config.py                     # 配置加载
│   ├── db.py                         # SQLite 数据库
│   ├── scrapers/                     # 爬虫模块
│   │   ├── base.py                   # 基础爬虫类
│   │   └── nowcoder.py              # 牛客网爬虫
│   ├── pipeline/                     # 数据处理管道
│   │   ├── aggregator.py            # 数据汇聚
│   │   ├── dedup.py                 # 去重
│   │   └── formatter.py            # 消息格式化
│   └── notifiers/                    # 推送通知
│       ├── pushplus.py              # PushPlus 推送
│       └── wecom_bot.py            # 企业微信推送
└── data/qiuzhao.db                   # SQLite 数据库
```

## 推送渠道

### PushPlus（推荐）
- 免费 200 条/天
- 支持 Markdown
- 直达个人微信

### 企业微信 Bot（备选）
- 免费无限制
- 需创建企业微信群并添加机器人

## 许可证

MIT
