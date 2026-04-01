---
layout: default
title: 性能日报
permalink: /daily/
---

# 📅 性能日报

每日 Linux 内核与性能优化资讯汇总。

## 最新日报

{% assign daily_reports = site.pages | where_exp: "page", "page.path contains 'daily/'" | where_exp: "page", "page.name contains '.html'" | sort: "name" | reverse %}

{% if daily_reports.size > 0 %}
<ul class="post-list">
  {% for report in daily_reports limit:20 %}
    {% assign report_name = report.name | remove: '.html' %}
    {% assign report_date = report_name | slice: 0, 10 %}
    <li>
      <div class="post-date">{{ report_date }}</div>
      <a href="{{ report.url }}">{{ report.title | default: report_name }}</a>
    </li>
  {% endfor %}
</ul>
{% else %}
<div class="card">
  <p>📅 性能日报正在整理中，敬请期待！</p>
  <p>日报内容涵盖：</p>  
  <ul>
    <li>Linux 内核最新提交动态</li>
    <li>性能优化补丁分析</li>
    <li>社区技术讨论汇总</li>
    <li>前沿技术资讯</li>
  </ul>
</div>
{% endif %}

## 按月份浏览

<div class="grid">
  <div class="card">
    <h3>2026年3月</h3>
    <a href="/daily/2026-03/">查看 →</a>
  </div>
  
  <div class="card">
    <h3>2025年3月</h3>
    <a href="/daily/2025-03/">查看 →</a>
  </div>
</div>

## 日报模板

<div class="card">
  <h3>📝 日报模板</h3>
  <p>标准化日报格式模板，确保报告内容的一致性。</p>
  <a href="/daily/template.html">查看模板 →</a>
</div>
