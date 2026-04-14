# Draft: openEuler PR Review 栏目 + Dashboard 规划

## 已知信息（来自代码库扫描）
- Jekyll + GitHub Pages 静态站点，主题 minima
- 已有栏目：`reports/`、`daily/`、`features/`、`cpu/`
- `daily/` 目录混合使用 `.md` 和 `.html`，`daily/index.md` 通过 Liquid 自动列出 `daily/` 下的 `.html` 页面
- 存在 `daily/template.html` 作为日报的 HTML 模板
- `_layouts/default.html` 是站点导航母版，包含顶部导航栏
- GitHub Actions 只有一个 `auto-merge.yml`，无定时任务
- 无测试框架，验证靠 `bundle exec jekyll doctor` / `jekyll build`

## 用户需求（待细化）
1. 新增 openEuler 内核 Review 报告栏目
2. 存放 AI review openEuler PR 的 review 报告 HTML 版本
3. 提供汇总页面
4. 做一个 openEuler PR Review 状态的 dashboard
5. 每天定时更新（静态页面，定时刷新并提交）

## 待确认问题
- [ ] 目标仓库：openEuler 内核代码在哪个平台？（GitHub / Gitee / 其他）仓库地址？
- [ ] 数据获取方式：通过 API 拉取 PR 列表，还是已有本地生成的 HTML 报告？
- [ ] Dashboard 展示内容：PR 列表 / Review 状态 / 统计数字 / 趋势图？
- [ ] 更新频率：每天一次？固定时间点？
- [ ] URL 路径偏好：`/openeuler/`、`/reviews/openeuler/` 或其他？
- [ ] 栏目名称："openEuler Review"、"openEuler 内核 Review"？
- [ ] 自动化触发：GitHub Actions scheduled workflow？
- [ ] 报告保留策略：保留最近 N 天 / N 周？

## 初步技术方案设想
- 使用 Jekyll collection 或普通目录 `openeuler/` 存放报告
- Dashboard 使用静态 HTML + 少量 JS（GitHub Pages 兼容）
- 定时更新通过 GitHub Actions `schedule` 触发，生成 Markdown/HTML 后自动提交
- 汇总页可以是 Jekyll 的索引页，用 Liquid 遍历 collection
