---
layout: default
title: 特性深度分析
permalink: /features/
---

# 🔧 特性深度分析

Linux 核心子系统的深度技术剖析。

## 调度器 (Scheduler)

<div class="card">
  <h3>⚡ CFS 调度器优化</h3>
  <p>完全公平调度器的实现原理与性能优化分析，包括 vruntime 计算、负载均衡等核心机制。</p>
  <a href="/features/scheduler/scheduler_performance_analysis.html">查看详情 →</a>
</div>

<div class="card">
  <h3>🎯 sched-ext 调度框架</h3>
  <p>Linux 内核的可扩展调度框架，允许用户空间实现自定义调度策略。</p>
  <a href="/features/scheduler/sched-ext.html">查看详情 →</a>
</div>

## 文件系统

<div class="card">
  <h3>💾 ext4 性能优化</h3>
  <p>ext4 文件系统的性能特性、优化技巧与最佳实践。</p>
  <a href="/features/ext4/ext4_performance_analysis.html">查看详情 →</a>
</div>

## 其他特性

<div class="grid">
  <div class="card">
    <h3>🧠 内存管理</h3>
    <p>内存分配、回收、压缩等机制分析。</p>
    <a href="/features/memory/">查看 →</a>
  </div>
  
  <div class="card">
    <h3>📡 网络性能</h3>
    <p>网络栈优化与协议性能分析。</p>
    <a href="/features/network/">查看 →</a>
  </div>
  
  <div class="card">
    <h3>💾 IO 子系统</h3>
    <p>块设备层与 IO 调度优化。</p>
    <a href="/features/io/">查看 →</a>
  </div>
  
  <div class="card">
    <h3>🖥️ 虚拟化</h3>
    <p>KVM、容器等虚拟化技术分析。</p>
    <a href="/features/virtualization/">查看 →</a>
  </div>
  
  <div class="card">
    <h3>🚀 Wave - SmartNIC卸载</h3>
    <p>将资源管理卸载到 SmartNIC 核心，节省 16-24 主机核心，性能损耗仅 1.1%-7.4%。</p>
    <span class="tag" style="background-color: var(--color-accent-orange);">🆕 深度报告</span>
    <a href="/reports/features/wave/" style="display: block; margin-top: 1rem;">查看详情 →</a>
  </div>
</div>
