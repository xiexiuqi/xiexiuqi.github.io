---
layout: default
title: 性能报告
permalink: /reports/
---

# 📊 性能报告

深入分析 Linux 内核各版本的性能优化与特性变化。

## Linux 7.x 内核

{% assign reports_7x = site.pages | where_exp: "page", "page.path contains 'reports/7.x'" | where_exp: "page", "page.name != 'index.md'" | sort: "title" %}

{% if reports_7x.size > 0 %}
<ul class="post-list">
  {% for report in reports_7x limit:10 %}
    <li>
      <a href="{{ report.url }}">{{ report.title | default: report.name }}</a>
      {% if report.description %}
        <div class="post-excerpt">{{ report.description }}</div>
      {% endif %}
    </li>
  {% endfor %}
</ul>
{% else %}
<div class="card">
  <p>🚀 Linux 7.x 性能报告即将上线，敬请期待！</p>
</div>
{% endif %}

## Linux 6.x 内核

{% assign reports_6x = site.pages | where_exp: "page", "page.path contains 'reports/6.x'" | where_exp: "page", "page.name != 'index.md'" | sort: "title" %}

{% if reports_6x.size > 0 %}
<ul class="post-list">
  {% for report in reports_6x limit:10 %}
    <li>
      <a href="{{ report.url }}">{{ report.title | default: report.name }}</a>
      {% if report.description %}
        <div class="post-excerpt">{{ report.description }}</div>
      {% endif %}
    </li>
  {% endfor %}
</ul>
{% else %}
<div class="card">
  <p>🔧 Linux 6.x 性能报告即将上线，敬请期待！</p>
</div>
{% endif %}

## 周报汇总

<div class="card">
  <h3>📅 性能周报</h3>
  <p>每周性能技术专题汇总，深度分析特定领域的优化方案。涵盖调度器、内存管理、文件系统等核心子系统。</p>
  <a href="/reports/weekly/">查看周报 →</a>
</div>

---

<div class="grid">
  <div class="card">
    <h3>📖 报告归档</h3>
    <p>查看所有历史报告与文档。</p>
    <a href="/daily/archive/">进入归档 →</a>
  </div>
  
  <div class="card">
    <h3>📊 性能日报</h3>
    <p>每日性能资讯汇总。</p>
    <a href="/daily/">查看日报 →</a>
  </div>
</div>
