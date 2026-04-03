---
layout: default
title: 技术报告库
permalink: /reports/
---

# 📚 技术报告库

系统化的 Linux 性能技术调研报告，涵盖 CPU 架构、内核特性、学术顶会论文等多个维度。

## 🖥️ CPU 架构调研

深入分析各类服务器 CPU 架构设计与性能特性。

<div class="grid">
  <div class="card">
    <h3>🚀 Arm 架构</h3>
    <p>Neoverse 系列、AGI CPU、Grace 等 Arm 服务器处理器深度分析。</p>
    <a href="/reports/cpu/arm/agi-cpu/">Arm AGI CPU 报告 →</a>
    <br><small style="color: var(--color-text-muted);">1 篇报告</small>
  </div>
  
  <div class="card">
    <h3>🔥 AMD 架构</h3>
    <p>EPYC 系列 Zen 架构演进、性能优化与数据中心部署分析。</p>
    <a href="/reports/cpu/amd/">查看目录 →</a>
    <br><small style="color: var(--color-text-muted);">暂无报告</small>
  </div>
  
  <div class="card">
    <h3>💙 Intel 架构</h3>
    <p>Xeon 系列、至强可扩展处理器架构与性能调优指南。</p>
    <a href="/reports/cpu/intel/">查看目录 →</a>
    <br><small style="color: var(--color-text-muted);">暂无报告</small>
  </div>
</div>

[查看全部 CPU 架构报告 →](/reports/cpu/)

---

## ⚙️ 内核特性深度分析

Linux 内核核心子系统的实现原理与优化策略。

<div class="grid">
  <div class="card">
    <h3>⚡ 调度器</h3>
    <p>CFS、RT、sched-ext、EAS 等调度算法与性能优化。</p>
    <span class="tag" style="background-color: var(--color-accent-green);">新增深度报告</span>
    <a href="/features/scheduler/" style="display: block; margin-top: 1rem;">查看详情 →</a>
  </div>
  
  <div class="card">
    <h3>🧠 内存管理</h3>
    <p>页面分配、内存回收、NUMA、大页等机制分析。</p>
    <a href="/features/memory/">查看详情 →</a>
  </div>
  
  <div class="card">
    <h3>💾 文件系统</h3>
    <p>ext4、XFS、btrfs 及新型文件系统性能对比。</p>
    <a href="/features/ext4/">查看详情 →</a>
  </div>
  
  <div class="card">
    <h3>📡 网络性能</h3>
    <p>TCP/IP 协议栈、DPDK、XDP 等网络性能优化。</p>
    <a href="/features/network/">查看详情 →</a>
  </div>
  
  <div class="card">
    <h3>⏱️ rseq 时间片扩展</h3>
    <p>Linux rseq 时间片扩展机制深度分析，金融与电信行业应用。</p>
    <span class="tag" style="background-color: var(--color-accent-blue);">🆕 深度报告</span>
    <a href="/reports/features/rseq/" style="display: block; margin-top: 1rem;">阅读报告 →</a>
  </div>
</div>

[查看全部特性分析 →](/features/)

---

## 📖 论文解读

顶会论文深度解读与工程实践结合。

<div class="grid">
  <div class="card">
    <h3>🎯 OSDI</h3>
    <p>操作系统设计与实现顶会论文精选解读。</p>
    <a href="/reports/papers/osdi/">查看目录 →</a>
    <br><small style="color: var(--color-text-muted);">暂无报告</small>
  </div>
  
  <div class="card">
    <h3>🔬 SOSP</h3>
    <p>操作系统原理研讨会经典论文分析。</p>
    <a href="/reports/papers/sosp/">查看目录 →</a>
    <br><small style="color: var(--color-text-muted);">暂无报告</small>
  </div>
  
  <div class="card">
    <h3>🌍 EuroSys</h3>
    <p>欧洲系统会议论文与技术创新。</p>
    <a href="/reports/papers/eurosys/">查看目录 →</a>
    <br><small style="color: var(--color-text-muted);">暂无报告</small>
  </div>
  
  <div class="card">
    <h3>⚡ ATC</h3>
    <p>USENIX 年度技术会议系统论文。</p>
    <a href="/reports/papers/atc/">查看目录 →</a>
    <br><small style="color: var(--color-text-muted);">暂无报告</small>
  </div>
</div>

---

## 📊 内核版本报告

按 Linux 内核版本整理的完整分析报告。

<div class="grid">
  <div class="card">
    <h3>🚀 Linux 7.x</h3>
    <p>最新 Linux 7.0 内核完整技术报告，深入分析调度器、内存管理等核心子系统优化。</p>
    <a href="/reports/7.x/">查看报告 →</a>
  </div>
  
  <div class="card">
    <h3>🔧 Linux 6.x</h3>
    <p>Linux 6.18/6.19 等版本的性能优化与特性分析，包含详细的技术解读。</p>
    <a href="/reports/6.x/">查看报告 →</a>
  </div>
</div>

---

## 📅 定期报告

<div class="grid">
  <div class="card">
    <h3>📊 性能日报</h3>
    <p>每日 Linux 内核与性能优化资讯汇总。</p>
    <a href="/daily/">查看日报 →</a>
  </div>
  
  <div class="card">
    <h3>📈 周报汇总</h3>
    <p>每周性能技术专题汇总，深度分析特定领域的优化方案。</p>
    <a href="/reports/weekly/">查看周报 →</a>
  </div>
</div>

---

## 🏷️ 按标签浏览

<div>
  <a href="/tags/linux-kernel/" class="tag">Linux 内核</a>
  <a href="/tags/scheduler/" class="tag">调度器</a>
  <a href="/tags/performance/" class="tag">性能优化</a>
  <a href="/tags/memory/" class="tag">内存管理</a>
  <a href="/tags/filesystem/" class="tag">文件系统</a>
  <a href="/tags/network/" class="tag">网络</a>
  <a href="/tags/cpu/" class="tag">CPU</a>
  <a href="/tags/arm/" class="tag">Arm</a>
  <a href="/tags/amd/" class="tag">AMD</a>
  <a href="/tags/intel/" class="tag">Intel</a>
</div>

[查看全部标签 →](/tags/)
