---
layout: default
title: openEuler Kernel
---

<!-- Hero Section -->
<div class="hero">
  <h1>openEuler Kernel</h1>
  <p>openEuler 内核补丁 Review 报告与状态追踪</p>

  <div style="margin-top: 2rem;">
    <a href="/openeuler/dashboard/" class="btn btn-primary">Review Dashboard</a>
    <a href="/openeuler/reviews/" class="btn btn-secondary" style="margin-left: 1rem;">浏览报告</a>
  </div>
</div>

<!-- Stats Overview -->
<div class="section-header">
  <h2>📊 概览</h2>
</div>

<div class="grid">
  <div class="card">
    <h3>📝 Review 报告</h3>
    <p>基于 AI 辅助的 openEuler 内核补丁 Review 报告，涵盖代码质量、KABI 兼容性、安全性、回退正确性等多维度分析。</p>
    <a href="/openeuler/reviews/">查看全部报告 →</a>
  </div>

  <div class="card">
    <h3>📈 Dashboard</h3>
    <p>实时追踪 PR Review 状态、统计指标和趋势分析，每日自动更新。</p>
    <a href="/openeuler/dashboard/">进入 Dashboard →</a>
  </div>
</div>

<!-- Latest Reviews -->
<div class="section-header" style="margin-top: 3rem;">
  <h2>🆕 最新 Review 报告</h2>
  <a href="/openeuler/reviews/">查看全部 →</a>
</div>

<ul class="post-list">
  {% assign reviews = site.openeuler_reviews | sort: 'date' | reverse %}
  {% for review in reviews limit:10 %}
    <li>
      <div class="post-date">{{ review.date | date: "%Y-%m-%d" }}</div>
      <a href="{{ review.url | relative_url }}">{{ review.title }}</a>
      {% if review.pr_id %}
        <span class="post-tag">PR {{ review.pr_id }}</span>
      {% endif %}
      {% if review.overall_verdict %}
        <span class="badge {{ review.overall_verdict | slugify }}">{{ review.overall_verdict }}</span>
      {% endif %}
    </li>
  {% endfor %}
</ul>
