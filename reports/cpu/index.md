---
layout: default
title: CPU 架构调研
permalink: /reports/cpu/
---

# 🖥️ CPU 架构调研

深入分析各类服务器 CPU 架构设计与性能特性。

## Arm 架构

{% assign arm_reports = site.pages | where_exp: "page", "page.path contains 'reports/cpu/arm/'" | where_exp: "page", "page.name == 'index.html'" | sort: "date" | reverse %}

{% if arm_reports.size > 0 %}
<div class="grid">
  {% for report in arm_reports %}
    <div class="card">
      <h3>{{ report.title | default: report.name }}</h3>
      <p>{{ report.description | default: "点击查看详情" }}</p>
      <a href="{{ report.url }}">阅读报告 →</a>
    </div>
  {% endfor %}
</div>
{% else %}
<div class="card">
  <h3>Arm AGI CPU</h3>
  <p>Arm首款直接面向数据中心销售的自研CPU，采用136核Neoverse V3架构，专为AI代理编排优化。</p>
  <a href="/reports/cpu/arm/agi-cpu/">阅读报告 →</a>
</div>
{% endif %}

## AMD 架构

<div class="card">
  <p>🔥 AMD EPYC 系列处理器调研报告即将上线...</p>
</div>

## Intel 架构

<div class="card">
  <p>💙 Intel Xeon 系列处理器调研报告即将上线...</p>
</div>

---

[← 返回报告库](/reports/)
