# AGENTS.md - xiexiuqi.github.io

This repository hosts a GitHub Pages static website using Jekyll.

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

## Project Structure

```
.
├── _config.yml          # Jekyll configuration
├── _layouts/            # HTML layouts
├── _includes/           # Reusable HTML snippets
├── _sass/              # SCSS partials
├── _posts/             # Blog posts (YYYY-MM-DD-title.md)
├── _drafts/            # Unpublished drafts
├── assets/             # CSS, JS, images
├── index.md            # Homepage
└── Gemfile             # Ruby dependencies
```

## File Naming Conventions

- **Posts**: `YYYY-MM-DD-title-in-lowercase.md` (e.g., `2026-04-01-hello-world.md`)
- **Drafts**: `title-in-lowercase.md` (no date prefix)
- **Layouts**: lowercase-with-dashes.html (e.g., `post.html`, `default.html`)
- **Assets**: lowercase.ext (e.g., `style.css`, `logo.png`)

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

## Content Style Guidelines

- **Markdown**: Use GitHub Flavored Markdown
- **Images**: Place in `assets/images/`, reference with `![alt](assets/images/file.png)`
- **Links**: Use relative paths `/about/` instead of full URLs
- **Code blocks**: Specify language for syntax highlighting
- **Line length**: Max 100 characters for readability

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

## Common Jekyll Variables

- `{{ site.title }}` - Site title from _config.yml
- `{{ page.title }}` - Current page title
- `{{ content }}` - Page content
- `{{ site.posts }}` - List of all posts
- `{{ page.date | date: "%Y-%m-%d" }}` - Format date

## Troubleshooting

- Build errors: Run `bundle exec jekyll doctor`
- Gem conflicts: Delete `Gemfile.lock` and run `bundle install`
- Cache issues: Run `bundle exec jekyll clean`

## External Resources

- Jekyll docs: https://jekyllrb.com/docs/
- GitHub Pages: https://docs.github.com/en/pages
- Liquid syntax: https://shopify.github.io/liquid/
