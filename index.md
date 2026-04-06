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
  <h2>📚 技术报告库</h2>
  <a href="/reports/">查看全部 →</a>
</div>

<div class="grid">
  <div class="card">
    <h3>🚀 Arm AGI CPU</h3>
    <p>Arm首款自研数据中心CPU，136核Neoverse V3架构，专为AI代理编排优化。</p>
    <a href="/reports/cpu/arm/agi-cpu/">阅读报告 →</a>
  </div>
  
  <div class="card">
    <h3>🖥️ CPU 架构调研</h3>
    <p>Arm、AMD、Intel 等服务器处理器架构设计与性能特性深度分析。</p>
    <a href="/reports/cpu/">查看全部 →</a>
    <br>
    <small style="color: var(--color-accent-green);">🆕 新增: AMD Zen 5 + ZEN6 报告</small>
  </div>
  
  <div class="card">
    <h3>📖 论文解读</h3>
    <p>OSDI、SOSP、EuroSys、ATC 等顶会论文深度解读与工程实践结合。</p>
    <a href="/reports/papers/">查看全部 →</a>
  </div>
  
  <div class="card">
    <h3>📅 定期报告</h3>
    <p>性能日报、周报，以及 Linux 6.x/7.x 内核版本完整分析报告。</p>
    <a href="/daily/">查看日报 →</a>
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
    <p>CFS、sched-ext 等调度器机制与性能优化分析。包含 Cache Aware Scheduling 和 rseq 时间片扩展报告。</p>
    <a href="/features/scheduler/">查看详情 →</a>
    <br>
    <small style="color: var(--color-accent-green);">🆕 新增: Cache Aware + rseq 报告</small>
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
    <h3>🔧 特性深度分析</h3>
    <p>Linux 核心子系统的深度技术剖析。包含 Wave SmartNIC 卸载等前沿技术。</p>
    <a href="/features/">查看全部 →</a>
    <br>
    <small style="color: var(--color-accent-orange);">🆕 新增: Wave 报告</small>
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
