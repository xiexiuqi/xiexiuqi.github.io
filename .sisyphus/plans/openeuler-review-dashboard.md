# openEuler Kernel Review 栏目 + Dashboard 建设计划

## TL;DR

> 在现有 Jekyll 站点中新增 `openEuler Kernel` 栏目，支持存放 AI Review 报告的 HTML 版本，并提供一个静态 Dashboard 展示 PR Review 状态、统计数据和趋势。配套自动化脚本读取本地仓库 `~/git/openEuler-kernel` 生成数据，GitHub Actions 定时任务每天更新站点内容。
>
> **Deliverables**:
> - `openeuler/` 目录结构（reviews/、dashboard/、archive/、data/）
> - Jekyll collection `_openeuler_reviews`
> - Dashboard 页面（`/openeuler/dashboard/`）
> - 主入口页面（`/openeuler/`）
> - Review 归档页（`/openeuler/reviews/`）
> - 自动化脚本 `.github/scripts/update-openeuler.py`
> - GitHub Actions Workflow `.github/workflows/openeuler-daily.yml`
> - 顶部导航更新
>
> **Estimated Effort**: Medium-Large
> **Parallel Execution**: YES - 3 waves
> **Critical Path**: Wave 1 (scaffolding) → Wave 2 (automation scripts) → Wave 3 (dashboard + integration) → Final Verification

---

## Context

### Original Request
用户希望新增一个 **openEuler 内核 Review 报告** 栏目，专门存放使用 AI review openEuler PR 的 review 报告 HTML 版本，并提供汇总。同时为 openEuler 的 PR Review 状态做一个 dashboard，每天定时更新（静态页面，定时刷新并提交）。

### Interview Summary
**关键讨论结果**:
- **本地仓库**: `~/git/openEuler-kernel`（已存在，包含内核源码和 review 相关文件）
- **报告来源**: 本地已生成 HTML 报告；脚本从本地仓库读取信息生成/更新数据
- **展示内容**: Dashboard 包含 PR 列表、Review 状态、统计数字、趋势图
- **更新频率**: 每天一次，固定时间点
- **URL 路径**: 所有 openEuler 相关内容放在 `/openeuler/` 下，子目录归类（`reviews/`、`dashboard/` 等）
- **栏目名称**: **openEuler Kernel**
- **自动化**: GitHub Actions 定时触发，希望用大模型辅助 review（配置 skills）
- **归档策略**: 报告长期保留，按月/季度归档；Dashboard 只显示最新状态

### Local Repo Findings
本地仓库 `~/git/openEuler-kernel` 已确认存在，包含：
- `内核补丁Review检查脚本.sh` - 现有的 review 辅助脚本
- `内核补丁Review指南.md` - review 指南文档
- 标准 Linux 内核源码结构

**设计决策**：
- 自动化脚本以 `~/git/openEuler-kernel` 为默认输入源
- 脚本通过本地 `git log`、`git branch` 等命令读取仓库信息
- 如果本地仓库不存在，脚本生成示例数据并打印警告（graceful degradation）
- GitHub Actions 中可选择 clone 仓库或仅使用示例数据/已提交的静态数据

### Metis Review
**识别到的缺口及解决方案**:
- **本地数据源对齐**: 脚本需要知道如何从这个特定仓库结构中提取有用的 review 数据
- **术语对齐**: 使用 "PR" 在用户界面中，"patch" 或 "commit" 在技术层（因为内核补丁 review 通常对应 patch series）
- **大补丁处理**: 变更文件过多的 patch 需要截断并标记为 "partial review"
- **自动化更新**: 定时触发后脚本读取本地仓库并生成新的 Markdown/HTML 报告

---

## Work Objectives

### Core Objective
构建一个完整的 openEuler Kernel Review 栏目，包括 HTML 报告托管、静态 Dashboard 展示和每日自动更新的 GitHub Actions 流水线。数据源为本地 `~/git/openEuler-kernel` 仓库。

### Concrete Deliverables
1. Jekyll collection 配置与目录结构
2. 主入口页 `/openeuler/index.md`
3. Dashboard 页面 `/openeuler/dashboard/index.html`
4. 自动化数据获取脚本 `.github/scripts/update-openeuler.py`
5. GitHub Actions Workflow `.github/workflows/openeuler-daily.yml`
6. 导航栏更新 `_layouts/default.html`
7. 数据文件 `openeuler/data/pr-status.json`

### Definition of Done
- [ ] `bundle exec jekyll build` 成功，无报错
- [ ] `/openeuler/` 页面可正常访问并导航到子页面
- [ ] Dashboard 展示最新 PR/Patch 列表和统计卡片
- [ ] GitHub Actions workflow 能成功触发并提交变更
- [ ] 脚本能正确读取本地仓库 `~/git/openEuler-kernel` 并生成/更新文件

### Must Have
- [ ] Jekyll 目录和 collection 正确配置
- [ ] Dashboard 至少展示：PR/Patch 列表、统计数字、最近 7 天趋势
- [ ] 自动化脚本支持本地仓库路径配置、错误处理、示例数据 fallback
- [ ] 顶部导航添加 "openEuler Kernel" 入口
- [ ] 按月归档目录结构（`openeuler/reviews/YYYY-MM/` 和 `_openeuler_reviews/YYYY-MM/`）

### Must NOT Have (Guardrails)
- [ ] MVP 阶段不引入远程 API 认证（使用本地仓库）
- [ ] Dashboard 不过度依赖 Jekyll 插件（GitHub Pages 安全插件限制）
- [ ] 不引入复杂后端或数据库存储
- [ ] 不修改本地 `~/git/openEuler-kernel` 仓库内容（只读）

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** - ALL verification is agent-executed.

### Test Decision
- **Infrastructure exists**: NO（需要新建脚本和 workflow）
- **Automated tests**: NO（Jekyll 无测试框架）
- **Validation method**: `bundle exec jekyll doctor` + `bundle exec jekyll build`
- **Agent-Executed QA**: 使用 Bash 和 Playwright 验证页面构建和渲染

### QA Policy
Every task MUST include agent-executed QA scenarios. Evidence saved to `.sisyphus/evidence/task-{N}-{scenario-slug}.{ext}`.

- **Frontend/UI**: Playwright - Navigate, assert DOM, screenshot
- **Backend/Script**: Bash (python) - Assert script execution and output
- **Automation**: Bash (act/yq) - Validate workflow syntax

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Foundation - Scaffolding + Config):
├── Task 1: Create openeuler/ directory structure
├── Task 2: Add Jekyll collection _openeuler_reviews to _config.yml
├── Task 3: Add openEuler Kernel to top navigation
└── Task 4: Create openeuler index page

Wave 2 (Automation - Scripts + Workflow):
├── Task 5: Design local data source interface
├── Task 6: Build Python update script (.github/scripts/update-openeuler.py)
├── Task 7: Build GitHub Actions workflow (openeuler-daily.yml)
└── Task 8: Create dashboard data schema and sample data

Wave 3 (Dashboard + Integration):
├── Task 9: Build dashboard page (HTML + JS)
├── Task 10: Build monthly archive listing page
├── Task 11: Integrate script + workflow end-to-end
└── Task 12: Jekyll build validation and fix any issues

Wave FINAL (Verification):
├── Task F1: Plan compliance audit (oracle)
├── Task F2: Jekyll build and link validation (unspecified-high)
├── Task F3: Dashboard UI verification with Playwright (unspecified-high)
└── Task F4: Workflow syntax and script test (deep)
-> Present results -> Get explicit user okay
```

### Dependency Matrix
- **1-4**: - → 9, 10, 12
- **5**: - → 6, 7, 8
- **6**: 5 → 11, 12
- **7**: 5 → 11
- **8**: 5 → 9
- **9**: 1, 8 → 12
- **10**: 1 → 12
- **11**: 6, 7 → 12
- **12**: 1, 9, 10, 11 → F1-F4

### Agent Dispatch Summary
- **W1**: 4 tasks → `quick`
- **W2**: 4 tasks → `unspecified-high`, `deep`
- **W3**: 4 tasks → `visual-engineering`, `unspecified-high`, `deep`
- **FINAL**: 4 tasks → `oracle`, `unspecified-high`, `deep`

---

## TODOs

- [ ] 1. Create openeuler/ directory structure

  **What to do**:
  - Create directory hierarchy: `openeuler/`, `openeuler/reviews/`, `openeuler/dashboard/`, `openeuler/archive/`, `openeuler/data/`
  - Create `_openeuler_reviews/` (Jekyll collection root) with subdirs pattern `YYYY-MM/`
  - Create placeholder `README.md` in `openeuler/data/` documenting data schema
  - Ensure directory names are lowercase with hyphens (existing convention)

  **Must NOT do**:
  - Do not create actual review HTML files yet (done by automation script later)
  - Do not add any Jekyll configuration here (separate task)

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: []
  - Reason: Simple directory creation and scaffolding

  **Parallelization**:
  - **Can Run In Parallel**: YES (Wave 1)
  - **Parallel Group**: With Tasks 2, 3, 4
  - **Blocks**: Task 9, 10, 12
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] All directories exist: `ls -la openeuler/ openeuler/reviews/ openeuler/dashboard/ openeuler/archive/ openeuler/data/ _openeuler_reviews/`

  **QA Scenarios**:
  ```
  Scenario: Directory structure exists
    Tool: Bash
    Steps:
      1. ls -la openeuler/ _openeuler_reviews/
    Expected Result: Shows all expected subdirectories
    Evidence: .sisyphus/evidence/task-1-dir-structure.txt
  ```

  **Commit**: YES
  - Message: `feat(openeuler): create directory structure for openEuler Kernel section`

- [ ] 2. Add Jekyll collection _openeuler_reviews to _config.yml

  **What to do**:
  - Add collection configuration to `_config.yml`:
    ```yaml
    collections:
      openeuler_reviews:
        output: true
        permalink: /openeuler/reviews/:path/
    ```
  - Add default front matter for collection items:
    ```yaml
    defaults:
      - scope:
          path: ""
          type: "openeuler_reviews"
        values:
          layout: "default"
    ```

  **Must NOT do**:
  - Do not modify other existing collections or configurations unnecessarily
  - Do not break existing site build

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES (Wave 1)
  - **Parallel Group**: With Tasks 1, 3, 4
  - **Blocks**: Task 9, 10, 12
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [ ] `bundle exec jekyll doctor` returns no errors
  - [ ] `bundle exec jekyll build` succeeds
  - [ ] Collection output directory exists in `_site/openeuler/reviews/`

  **QA Scenarios**:
  ```
  Scenario: Jekyll builds with new collection
    Tool: Bash
    Steps:
      1. Create _openeuler_reviews/test-pr.md with basic front matter
      2. Run bundle exec jekyll build
      3. Check _site/openeuler/reviews/test-pr.html exists
    Expected Result: Build succeeds and output file is generated
    Evidence: .sisyphus/evidence/task-2-collection-build.txt
  ```

  **Commit**: YES
  - Message: `config(jekyll): add openeuler_reviews collection`

- [ ] 3. Add openEuler Kernel to top navigation

  **What to do**:
  - Edit `_layouts/default.html`
  - Add navigation link:
    ```html
    <a href="{{ "/openeuler/" | relative_url }}">openEuler Kernel</a>
    ```
  - Place link between "特性分析" and "🔍"

  **Must NOT do**:
  - Do not remove or reorder existing navigation items

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES (Wave 1)
  - **Parallel Group**: With Tasks 1, 2, 4

  **Acceptance Criteria**:
  - [ ] Navigation link appears on homepage
  - [ ] `bundle exec jekyll build` succeeds

  **QA Scenarios**:
  ```
  Scenario: Navigation link renders correctly
    Tool: Bash + grep
    Steps:
      1. Run bundle exec jekyll build
      2. grep -o 'openeuler' _site/index.html
    Expected Result: Link is present in built HTML
    Evidence: .sisyphus/evidence/task-3-nav-check.txt
  ```

  **Commit**: YES
  - Message: `feat(layout): add openEuler Kernel to navigation`

- [ ] 4. Create openeuler index page

  **What to do**:
  - Create `openeuler/index.md` as main landing page
  - Front matter: `layout: default`, `title: "openEuler Kernel"`
  - Content sections:
    - Hero section with description
    - Link cards to `/openeuler/dashboard/` and `/openeuler/reviews/`
    - Brief explanation of what the section contains
    - Stats summary placeholder
  - Match existing design patterns from `index.md` and `features/index.md`

  **Must NOT do**:
  - Do not hardcode actual PR data (use placeholders for automation)
  - Do not duplicate AI disclaimer (handled by layout)

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES (Wave 1)
  - **Parallel Group**: With Tasks 1, 2, 3

  **Acceptance Criteria**:
  - [ ] Page renders at `/openeuler/` URL
  - [ ] Links to dashboard and reviews work
  - [ ] Uses `default` layout

  **QA Scenarios**:
  ```
  Scenario: Index page builds and renders
    Tool: Bash
    Steps:
      1. Run bundle exec jekyll build
      2. ls _site/openeuler/index.html
      3. grep -c 'openEuler' _site/openeuler/index.html
    Expected Result: File exists and contains content
    Evidence: .sisyphus/evidence/task-4-index-page.txt
  ```

  **Commit**: YES
  - Message: `feat(openeuler): add main index page`

- [ ] 5. Design local data source interface

  **What to do**:
  - Define how the Python script will interact with `~/git/openEuler-kernel`:
    - Read recent commits: `git log --oneline --since="7 days ago"`
    - Read branches/tags for version tracking
    - Parse existing review guide/check script outputs (if applicable)
  - Document the expected inputs and outputs in `.github/scripts/DATA_INTERFACE.md`
  - Define the JSON schema for `openeuler/data/pr-status.json`
  - Decide how HTML review reports will be ingested (manual copy vs script processing)

  **Must NOT do**:
  - Do not write to the local kernel repo
  - Do not assume specific branch names without checking

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: []
  - Reason: Architecture design for local data integration

  **Parallelization**:
  - **Can Run In Parallel**: YES (Wave 2)
  - **Blocks**: Task 6, 7, 8
  - **Blocked By**: Task 1

  **Acceptance Criteria**:
  - [ ] `DATA_INTERFACE.md` documents input sources and output schema
  - [ ] `pr-status.json` schema defined
  - [ ] Script can detect if local repo exists and gracefully fallback to sample data

  **QA Scenarios**:
  ```
  Scenario: Repo detection works
    Tool: Bash
    Steps:
      1. python -c "import os; print(os.path.isdir(os.path.expanduser('~/git/openEuler-kernel')))"
    Expected Result: Prints True or False
    Evidence: .sisyphus/evidence/task-5-repo-detect.txt
  ```

  **Commit**: YES
  - Message: `docs(automation): define local data source interface`

- [ ] 6. Build Python update script (.github/scripts/update-openeuler.py)

  **What to do**:
  - Create Python script at `.github/scripts/update-openeuler.py`
  - Features:
    - Accept `--repo-path` (default: `~/git/openEuler-kernel`)
    - Accept `--output-dir` (default: `_openeuler_reviews/`)
    - Accept `--data-dir` (default: `openeuler/data/`)
    - Accept `--dry-run` flag
    - Read git log from local repo to generate patch/PR entries
    - Generate HTML review report placeholder for each entry
    - Write reports to `_openeuler_reviews/YYYY-MM/PR-{id}.html`
    - Update `openeuler/data/pr-status.json` with current state
    - If repo doesn't exist, generate sample data and print warning
  - Include logging and error handling

  **Must NOT do**:
  - Do not modify the local kernel repo
  - Do not hardcode specific commit hashes
  - Do not make script dependent on external AI APIs yet (MVP uses placeholders)

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES (Wave 2)
  - **Parallel Group**: With Tasks 7, 8
  - **Blocks**: Task 11, 12
  - **Blocked By**: Task 5

  **Acceptance Criteria**:
  - [ ] Script runs without errors: `python .github/scripts/update-openeuler.py --dry-run`
  - [ ] Generates valid Jekyll HTML files with proper front matter
  - [ ] Creates `pr-status.json` with expected schema
  - [ ] Works with missing repo (generates sample data)

  **QA Scenarios**:
  ```
  Scenario: Script runs in dry-run mode
    Tool: Bash
    Steps:
      1. python .github/scripts/update-openeuler.py --dry-run --limit 5
    Expected Result: Completes, shows what it would do, no files created
    Evidence: .sisyphus/evidence/task-6-dry-run.log

  Scenario: Script generates valid HTML with local repo
    Tool: Bash
    Steps:
      1. python .github/scripts/update-openeuler.py --limit 3
      2. head -20 _openeuler_reviews/*/*.html
    Expected Result: HTML files with Jekyll front matter created
    Evidence: .sisyphus/evidence/task-6-html-output.html

  Scenario: Script falls back with missing repo
    Tool: Bash
    Steps:
      1. python .github/scripts/update-openeuler.py --repo-path /nonexistent --limit 3
    Expected Result: Generates sample data, prints warning, exits 0
    Evidence: .sisyphus/evidence/task-6-fallback.log
  ```

  **Commit**: YES
  - Message: `feat(automation): add openeuler local repo update script`
  - Files: `.github/scripts/update-openeuler.py`, `.github/scripts/requirements.txt`

- [ ] 7. Build GitHub Actions workflow (openeuler-daily.yml)

  **What to do**:
  - Create `.github/workflows/openeuler-daily.yml`
  - Workflow features:
    - Schedule trigger: `cron: '0 2 * * *'` (02:00 UTC daily)
    - Manual trigger: `workflow_dispatch:`
    - Steps:
      1. Checkout site repo
      2. Checkout/clone `openEuler-kernel` repo (if needed) or assume it's present in self-hosted runner
      3. Setup Python
      4. Install dependencies
      5. Run update script
      6. Commit and push changes (only if there are changes)
    - Configure git user: `github-actions[bot]`
  - Add concurrency control to prevent overlapping runs

  **Must NOT do**:
  - Do not run workflow on every push (only schedule + manual)
  - Do not fail silently - log errors properly
  - Do not commit if no changes detected

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES (Wave 2)
  - **Parallel Group**: With Tasks 6, 8
  - **Blocks**: Task 11
  - **Blocked By**: Task 5

  **Acceptance Criteria**:
  - [ ] Workflow file passes YAML validation
  - [ ] Workflow appears in GitHub Actions tab
  - [ ] Can be triggered manually

  **QA Scenarios**:
  ```
  Scenario: Workflow syntax is valid
    Tool: Bash (yq)
    Steps:
      1. yq '.on.schedule[0].cron' .github/workflows/openeuler-daily.yml
      2. yq '.jobs.update.steps[].name' .github/workflows/openeuler-daily.yml
    Expected Result: YAML parses correctly, schedule is '0 2 * * *'
    Evidence: .sisyphus/evidence/task-7-workflow-syntax.txt
  ```

  **Commit**: YES
  - Message: `ci(github): add daily openeuler update workflow`

- [ ] 8. Create dashboard data schema and sample data

  **What to do**:
  - Define JSON schema for `openeuler/data/pr-status.json`:
    ```json
    {
      "last_updated": "2026-04-14T02:00:00Z",
      "source_repo": "~/git/openEuler-kernel",
      "stats": {
        "total_patches": 42,
        "reviewed_today": 5,
        "pending_review": 37,
        "high_priority": 3
      },
      "trend": [
        {"date": "2026-04-08", "count": 38},
        {"date": "2026-04-14", "count": 42}
      ],
      "patches": [
        {
          "id": "abc1234",
          "title": "...",
          "author": "...",
          "review_status": "pending|in_review|completed",
          "priority": "low|medium|high",
          "created_at": "..."
        }
      ]
    }
    ```
  - Create sample data file for dashboard development
  - Document schema in `openeuler/data/README.md`

  **Must NOT do**:
  - Do not commit real patch data with sensitive information
  - Do not make schema too complex for MVP

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES (Wave 2)
  - **Parallel Group**: With Tasks 6, 7
  - **Blocks**: Task 9
  - **Blocked By**: Task 5

  **Acceptance Criteria**:
  - [ ] JSON schema documented
  - [ ] Sample data file created and valid
  - [ ] Schema supports all dashboard features

  **QA Scenarios**:
  ```
  Scenario: JSON is valid and parseable
    Tool: Bash (jq)
    Steps:
      1. jq '.' openeuler/data/pr-status-sample.json
      2. jq '.stats.total_patches' openeuler/data/pr-status-sample.json
    Expected Result: Valid JSON, can query fields
    Evidence: .sisyphus/evidence/task-8-json-valid.txt
  ```

  **Commit**: YES
  - Message: `feat(data): add dashboard data schema and sample`

- [ ] 9. Build dashboard page (HTML + JS)

  **What to do**:
  - Create `openeuler/dashboard/index.html`
  - Dashboard components:
    1. **Stats Cards**: Total Patches, Reviewed Today, Pending, High Priority
    2. **Patch List Table**: Sortable/filterable list with columns: ID、Title、Author、Review Status、Date
    3. **Trend Chart**: Last 7 days patch count (use lightweight Chart.js or simple CSS bars)
    4. **Last Updated**: Timestamp from `pr-status.json`
  - Use client-side JS to fetch `openeuler/data/pr-status.json`
  - Graceful degradation if JSON fails to load
  - Match site styling using existing CSS

  **Must NOT do**:
  - Do not require server-side processing
  - Do not use unsupported Jekyll plugins

  **Recommended Agent Profile**:
  - **Category**: `visual-engineering`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES (Wave 3)
  - **Parallel Group**: With Tasks 10, 11
  - **Blocks**: Task 12
  - **Blocked By**: Tasks 1, 8

  **Acceptance Criteria**:
  - [ ] Page renders at `/openeuler/dashboard/`
  - [ ] Stats cards visible with sample data
  - [ ] Patch list table renders
  - [ ] Trend chart displays
  - [ ] `bundle exec jekyll build` succeeds

  **QA Scenarios**:
  ```
  Scenario: Dashboard renders with sample data
    Tool: Playwright
    Steps:
      1. Run bundle exec jekyll serve --detach
      2. Navigate to http://localhost:4000/openeuler/dashboard/
      3. Screenshot the page
      4. Assert page contains "openEuler Kernel Dashboard"
      5. Assert stats cards are visible
    Expected Result: Dashboard loads, stats visible, no JS errors
    Evidence: .sisyphus/evidence/task-9-dashboard.png
  ```

  **Commit**: YES
  - Message: `feat(dashboard): add openeuler kernel dashboard page`

- [ ] 10. Build monthly archive listing page

  **What to do**:
  - Create `openeuler/reviews/index.md` as archive browser
  - Use Jekyll Liquid to list collection items grouped by month
  - Show month headings with count of reviews
  - List review links with title and PR/patch ID
  - Ensure this works for both manually uploaded and auto-generated HTML reports

  **Must NOT do**:
  - Do not use complex Jekyll plugins for pagination
  - Do not break if collection is empty

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES (Wave 3)
  - **Parallel Group**: With Tasks 9, 11
  - **Blocks**: Task 12
  - **Blocked By**: Task 1

  **Acceptance Criteria**:
  - [ ] Archive page renders at `/openeuler/reviews/`
  - [ ] Groups reviews by month
  - [ ] Works with empty collection (shows placeholder)

  **QA Scenarios**:
  ```
  Scenario: Archive page lists reviews by month
    Tool: Bash
    Steps:
      1. Create sample review files: _openeuler_reviews/2026-04/PR-001.html and _openeuler_reviews/2026-03/PR-002.html
      2. Run bundle exec jekyll build
      3. grep -c 'PR-001' _site/openeuler/reviews/index.html
    Expected Result: Sample PRs appear in built archive page
    Evidence: .sisyphus/evidence/task-10-archive.txt
  ```

  **Commit**: YES
  - Message: `feat(openeuler): add monthly archive listing page`

- [ ] 11. Integrate script + workflow end-to-end

  **What to do**:
  - Ensure Python script output paths match Jekyll collection expectations
  - Update workflow to install script dependencies and execute correctly
  - Add `.github/scripts/requirements.txt` with needed packages
  - Ensure generated files use `layout: default` front matter
  - Test end-to-end locally (simulate workflow steps)

  **Must NOT do**:
  - Do not commit real patch data with personal info
  - Do not let workflow fail if no new patches exist

  **Recommended Agent Profile**:
  - **Category**: `deep`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES (Wave 3)
  - **Parallel Group**: With Tasks 9, 10
  - **Blocks**: Task 12
  - **Blocked By**: Tasks 6, 7

  **Acceptance Criteria**:
  - [ ] `requirements.txt` exists and lists all dependencies
  - [ ] Local end-to-end test passes
  - [ ] Workflow file references correct script path

  **QA Scenarios**:
  ```
  Scenario: End-to-end local test
    Tool: Bash
    Steps:
      1. python -m venv .venv && source .venv/bin/activate
      2. pip install -r .github/scripts/requirements.txt
      3. python .github/scripts/update-openeuler.py --dry-run
    Expected Result: Dependencies install, script runs
    Evidence: .sisyphus/evidence/task-11-e2e.log
  ```

  **Commit**: YES
  - Message: `chore(integration): wire up script and workflow end-to-end`

- [ ] 12. Jekyll build validation and fix any issues

  **What to do**:
  - Run `bundle exec jekyll clean && bundle exec jekyll doctor && bundle exec jekyll build`
  - Fix any Liquid syntax errors, missing includes, or broken links
  - Verify all new paths are generated in `_site/`
  - Check for warnings

  **Must NOT do**:
  - Do not ignore build warnings
  - Do not break existing site pages

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Blocked By**: Tasks 1-4, 6-11
  - **Blocks**: F1-F4

  **Acceptance Criteria**:
  - [ ] `jekyll doctor` returns clean
  - [ ] `jekyll build` succeeds with exit code 0
  - [ ] All `/openeuler/` pages exist in `_site/`

  **QA Scenarios**:
  ```
  Scenario: Full Jekyll build succeeds
    Tool: Bash
    Steps:
      1. bundle exec jekyll clean
      2. bundle exec jekyll build
      3. echo $?
      4. find _site/openeuler -type f
    Expected Result: Exit code 0, files exist in _site/openeuler/
    Evidence: .sisyphus/evidence/task-12-build.txt
  ```

  **Commit**: YES (if fixes needed) or NO
  - Message: `fix(build): resolve jekyll build issues for openeuler section`

---

## Final Verification Wave

> 4 review agents run in PARALLEL. ALL must APPROVE. Present consolidated results to user and get explicit "okay" before completing.

- [ ] F1. **Plan Compliance Audit** — `oracle`
  Read the plan end-to-end. For each "Must Have": verify implementation exists. For each "Must NOT Have": search codebase for forbidden patterns. Check evidence files exist in `.sisyphus/evidence/`.
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT: APPROVE/REJECT`

- [ ] F2. **Jekyll Build and Link Validation** — `unspecified-high`
  Run `bundle exec jekyll clean && bundle exec jekyll build && bundle exec jekyll doctor`.
  Output: `Build [PASS/FAIL] | Doctor [PASS/FAIL] | Pages [N/N] | VERDICT`

- [ ] F3. **Dashboard UI Verification with Playwright** — `unspecified-high` (+ `playwright` skill)
  Navigate to `/openeuler/`, `/openeuler/dashboard/`, `/openeuler/reviews/`. Screenshot and assert.
  Output: `Pages [N/N pass] | Screenshots [N captured] | JS Errors [CLEAN/N] | VERDICT`

- [ ] F4. **Workflow Syntax and Script Test** — `deep`
  Validate YAML syntax, verify `--dry-run` support, check `requirements.txt`.
  Output: `Workflow [VALID/INVALID] | Script [PASS/FAIL] | Dependencies [OK/MISSING] | VERDICT`

---

## Commit Strategy

- Wave 1 commits: directory structure, collection config, navigation, index page
- Wave 2 commits: data interface docs, update script, workflow, data schema
- Wave 3 commits: dashboard, archive page, end-to-end integration
- Final fixes: build issues if any

---

## Success Criteria

```bash
# Jekyll build
bundle exec jekyll clean && bundle exec jekyll build
# Expected: exit code 0

# Local server verification
bundle exec jekyll serve --detach
# Expected: server starts, /openeuler/ accessible

# Script dry-run
python .github/scripts/update-openeuler.py --dry-run --limit 5
# Expected: completes without errors
```

---

## Notes for Executor

### Local Repo
- **Path**: `~/git/openEuler-kernel`
- **Access**: Read-only
- **Contents**: Linux kernel source + `内核补丁Review检查脚本.sh` + `内核补丁Review指南.md`
- **Behavior if missing**: Script generates sample data and prints warning

### Critical Decisions
- **UI Terminology**: Use "PR" in user-facing text, technical filenames use "PR-{id}"
- **Archive Pattern**: `_openeuler_reviews/YYYY-MM/PR-{id}.html`
- **Update Schedule**: Daily at 02:00 UTC (`0 2 * * *`)
- **Dashboard Data**: Stored in `openeuler/data/pr-status.json`, fetched client-side by JS
