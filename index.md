---
layout: default
title: 首页
---

<!-- Hero Section -->
<div class="hero">
  <h1>Linux内核与系统性能优化</h1>
  <p>专注 Linux 内核与系统性能优化技术</p>
  
  <!-- Tech Stack Tags -->
  <div class="tech-stack">
    <a href="/features/scheduler/" class="tech-tag primary">Linux Kernel</a>
    <a href="/features/scheduler/" class="tech-tag">Scheduler</a>
    <a href="/features/memory/" class="tech-tag">Memory</a>
    <a href="/features/ext4/" class="tech-tag">Filesystem</a>
    <a href="/features/network/" class="tech-tag">Network</a>
    <a href="/cpu/" class="tech-tag">eBPF</a>
    <a href="/features/io/" class="tech-tag">I/O</a>
  </div>
  
  <div style="margin-top: 2rem;">
    <a href="/reports/" class="btn btn-primary">浏览性能报告</a>
    <a href="/daily/" class="btn btn-secondary" style="margin-left: 1rem;">查看日报</a>
  </div>
</div>

<!-- Featured Reports -->
<div class="section-header">
  <h2>📊 性能报告</h2>
  <a href="/reports/">查看全部 →</a>
</div>

<div class="grid">
  <div class="card">
    <h3>🚀 Linux 7.x 内核分析</h3>
    <p>最新 Linux 7.0 内核完整技术报告，深入分析调度器、内存管理等核心子系统优化。</p>
    <a href="/reports/7.x/">查看报告 →</a>
  </div>
  
  <div class="card">
    <h3>🔧 Linux 6.x 内核分析</h3>
    <p>Linux 6.18/6.19 等版本的性能优化与特性分析，包含详细的技术解读。</p>
    <a href="/reports/6.x/">查看报告 →</a>
  </div>
  
  <div class="card">
    <h3>📅 性能日报</h3>
    <p>每日性能资讯汇总，跟踪 Linux 内核开发动态与社区讨论。</p>
    <a href="/daily/">查看日报 →</a>
  </div>
  
  <div class="card">
    <h3>🎯 专题周报</h3>
    <p>每周性能技术专题汇总，深度分析特定领域的优化方案。</p>
    <a href="/reports/weekly/">查看周报 →</a>
  </div>
</div>

<!-- Feature Analysis -->
<div class="section-header">
  <h2>🔧 特性深度分析</h2>
  <a href="/features/">查看全部 →</a>
</div>

<div class="grid">
  <div class="card">
    <h3>⚡ 调度器优化</h3>
    <p>CFS、sched-ext 等调度器机制与性能优化分析。</p>
    <a href="/features/scheduler/">查看详情 →</a>
  </div>
  
  <div class="card">
    <h3>💾 文件系统</h3>
    <p>ext4 文件系统性能优化与特性分析。</p>
    <a href="/features/ext4/">查看详情 →</a>
  </div>
  
  <div class="card">
    <h3>🖥️ CPU 架构</h3>
    <p>CPU 架构优化与性能调优技术文档。</p>
    <a href="/cpu/">查看详情 →</a>
  </div>
  
  <div class="card">
    <h3>📡 网络性能</h3>
    <p>Linux 网络栈性能优化与协议分析。</p>
    <a href="/features/network/">查看详情 →</a>
  </div>
</div>

<hr>

<!-- Latest Articles -->
<div class="section-header">
  <h2>📝 最新文章</h2>
  <a href="/posts/">查看全部 →</a>
</div>

<ul class="post-list">
  {% for post in site.posts limit:5 %}
    <li>
      <div class="post-date">{{ post.date | date: "%Y-%m-%d" }}</div>
      <a href="{{ post.url }}">{{ post.title }}</a>
      {% if post.excerpt %}
        <div class="post-excerpt">{{ post.excerpt | strip_html | truncate: 100 }}</div>
      {% endif %}
    </li>
  {% endfor %}
</ul>

<!-- Tags Cloud -->
<div class="section-header" style="margin-top: 3rem;">
  <h2>🏷️ 热门标签</h2>
</div>

<div>
  <a href="/tags/linux-kernel/" class="tag">Linux 内核</a>
  <a href="/tags/scheduler/" class="tag">调度器</a>
  <a href="/tags/performance/" class="tag">性能优化</a>
  <a href="/tags/memory/" class="tag">内存管理</a>
  <a href="/tags/filesystem/" class="tag">文件系统</a>
  <a href="/tags/network/" class="tag">网络</a>
  <a href="/tags/cpu/" class="tag">CPU</a>
</div>
