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
  <h3>🚀 Arm AGI CPU</h3>
  <p>Arm首款直接面向数据中心销售的自研CPU，采用136核Neoverse V3架构，专为AI代理编排优化。</p>
  <a href="/reports/cpu/arm/agi-cpu/">阅读报告 →</a>
</div>
{% endif %}

## AMD 架构

<div class="grid">
  <div class="card">
    <h3>🔥 AMD ZEN6</h3>
    <p>首款台积电2nm GAA工艺x86处理器，256核配置，SPECINT 2017预估16.2分，2026年技术预览。</p>
    <span class="tag" style="background-color: var(--color-accent-orange);">未来架构</span>
    <a href="/reports/cpu/amd/zen6/" style="display: block; margin-top: 1rem;">阅读报告 →</a>
  </div>
  
  <div class="card">
    <h3>⚡ AMD Zen 5</h3>
    <p>2024年革命性x86架构，16% IPC提升，完整AVX-512支持，SPECint2017 12.6分。</p>
    <span class="tag" style="background-color: var(--color-accent-green);">深度分析</span>
    <a href="/reports/cpu/amd/zen5/" style="display: block; margin-top: 1rem;">阅读报告 →</a>
  </div>
</div>

## Intel 架构

<div class="card">
  <p>💙 Intel Xeon 系列处理器调研报告即将上线...</p>
</div>

---

[← 返回报告库](/reports/)
