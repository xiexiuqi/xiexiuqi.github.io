# AGENTS.md - xiexiuqi.github.io

This repository hosts a GitHub Pages static website using Jekyll. Content is primarily in Chinese (zh-CN).

## Build/Development Commands

```bash
# Install dependencies (first time)
bundle install

# Serve site locally with auto-rebuild
bundle exec jekyll serve

# Serve with drafts and future posts
bundle exec jekyll serve --drafts --future

# Build site for production
bundle exec jekyll build

# Clean generated files
bundle exec jekyll clean

# Verify site health
bundle exec jekyll doctor
```

**Note**: There is no test suite configured for this project. Validation is done via `jekyll doctor` and successful `jekyll build`.

## Project Structure

```
.
├── _config.yml          # Jekyll configuration
├── _layouts/            # HTML layouts (default.html, post.html)
├── _includes/           # Reusable HTML snippets
├── _sass/               # SCSS partials
├── _posts/              # Blog posts (YYYY-MM-DD-title.md)
├── _drafts/             # Unpublished drafts
├── assets/              # CSS, JS, images
│   ├── css/style.css
│   └── js/search.js
├── daily/               # Daily reports (YYYY-MM/YYYY-MM-DD.md)
├── reports/             # Technical reports (6.x/, 7.x/, cpu/, papers/)
├── features/            # Feature deep-dives
├── cpu/                 # CPU architecture content
├── search/              # Search page
├── tags/                # Tag index pages
├── index.md             # Homepage
├── about.md             # About page
└── Gemfile              # Ruby dependencies
```

## File Naming Conventions

- **Posts**: `YYYY-MM-DD-title-in-lowercase.md` (e.g., `_posts/2026-04-01-hello-world.md`)
- **Daily reports**: `daily/YYYY-MM/YYYY-MM-DD.md`
- **Drafts**: `title-in-lowercase.md` (no date prefix)
- **Layouts**: `lowercase-with-dashes.html` (e.g., `post.html`, `default.html`)
- **Assets**: `lowercase.ext` (e.g., `style.css`, `logo.png`)

## Front Matter Format

```yaml
---
layout: post
 title: "Page Title"
date: 2026-04-01 10:00:00 +0800
categories: [category1, category2]
tags: [tag1, tag2]
permalink: /custom-url/
---
```

- `layout`: Use `default` for pages, `post` for blog posts.
- `date`: Use `YYYY-MM-DD HH:MM:SS +0800` format.
- `permalink`: Use relative paths without `.html` suffix.
- Automated daily reports may include `generated_by: linux-performance-insights`.

## Content Style Guidelines

- **Language**: Content is in Chinese (zh-CN). Keep `lang="zh-CN"` in `<html>`.
- **Markdown**: Use GitHub Flavored Markdown.
- **Images**: Place in `assets/images/`, reference with `![alt](assets/images/file.png)`.
- **Links**: Use relative paths (e.g., `/reports/`, `/daily/`) instead of full URLs.
- **Code blocks**: Always specify the language for syntax highlighting.
- **Line length**: Max 100 characters for readability.
- **AI Disclaimer**: All pages include an AI disclaimer in `default.html`. Do not duplicate it manually in content.

## HTML/Liquid Conventions

- Escape variables with `| escape` in HTML attributes and titles.
- Use `relative_url` filter for internal asset paths: `{{ "/assets/css/style.css" | relative_url }}`.
- Use Jekyll's built-in filters (`date`, `strip_html`, `truncate`, etc.) for content formatting.
- Layouts use YAML front matter to specify parent layouts.

## Error Handling / Validation

- Run `bundle exec jekyll doctor` before pushing.
- Run `bundle exec jekyll build` to catch Liquid syntax errors and missing includes.
- Resolve build warnings (deprecated features, unescaped HTML) promptly.

## Git Workflow

```bash
# Make changes
vim _posts/2026-04-01-new-post.md

# Test locally
bundle exec jekyll serve

# Commit and push (auto-deploys to GitHub Pages)
git add .
git commit -m "Add: new blog post about topic"
git push origin main
```

## CI / Automation

- `.github/workflows/auto-merge.yml` auto-merges PRs from `auto/insights` branches after the `Build Jekyll site` check passes.
- GitHub Pages builds and deploys automatically on pushes to `main`.

## Common Jekyll Variables

- `{{ site.title }}` - Site title from `_config.yml`
- `{{ page.title }}` - Current page title
- `{{ content }}` - Page content
- `{{ site.posts }}` - List of all posts
- `{{ page.date | date: "%Y-%m-%d" }}` - Format date
- `{{ "/path" | relative_url }}` - Relative URL respecting `baseurl`

## Troubleshooting

- Build errors: Run `bundle exec jekyll doctor`
- Gem conflicts: Delete `Gemfile.lock` and run `bundle install`
- Cache issues: Run `bundle exec jekyll clean`

## External Resources

- Jekyll docs: https://jekyllrb.com/docs/
- GitHub Pages: https://docs.github.com/en/pages
- Liquid syntax: https://shopify.github.io/liquid/
- Theme (minima): https://github.com/jekyll/minima
