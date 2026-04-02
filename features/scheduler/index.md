---
layout: default
title: 调度器优化
permalink: /features/scheduler/
---

# ⚡ 调度器优化

Linux 调度器是内核最核心的子系统之一，直接影响系统性能和响应性。本章节深入分析各类调度机制和优化策略。

## 核心调度器

<div class="grid">
  <div class="card">
    <h3>🎯 CFS (完全公平调度器)</h3>
    <p>Linux 默认的进程调度器，基于红黑树实现，确保所有进程公平分享 CPU 时间。</p>
    <a href="/features/scheduler/scheduler_performance_analysis.html">查看详情 →</a>
  </div>
  
  <div class="card">
    <h3>🔧 sched-ext</h3>
    <p>可扩展的 BPF 调度框架，允许用户空间实现自定义调度策略。</p>
    <a href="/features/scheduler/sched-ext.html">查看详情 →</a>
  </div>
</div>

## 调度优化技术

<div class="grid">
  <div class="card">
    <h3>💾 Cache Aware Scheduling</h3>
    <p>缓存感知调度技术，通过感知 CPU 缓存拓扑优化任务放置，减少缓存未命中，提升整体性能。</p>
    <span class="tag" style="background-color: var(--color-accent-green);">深度报告</span>
    <a href="/reports/features/scheduler/cache-aware/" style="display: block; margin-top: 1rem;">阅读完整报告 →</a>
  </div>
</div>

## 调度策略

<div class="grid">
  <div class="card">
    <h3>⚡ 实时调度 (RT)</h3>
    <p>SCHED_FIFO 和 SCHED_RR 策略，适用于需要严格时间保证的实时应用。</p>
    <span style="color: var(--color-text-muted);">内容整理中...</span>
  </div>
  
  <div class="card">
    <h3>🔋 能耗感知调度 (EAS)</h3>
    <p>在 ARM 移动设备上广泛使用的调度器，平衡性能与功耗。</p>
    <span style="color: var(--color-text-muted);">内容整理中...</span>
  </div>
  
  <div class="card">
    <h3>📊 负载均衡</h3>
    <p>跨 CPU 核心和 NUMA 节点的任务迁移与负载均衡算法。</p>
    <span style="color: var(--color-text-muted);">内容整理中...</span>
  </div>
</div>

---

## 📚 相关报告

- [Cache Aware Scheduling 深度报告](/reports/features/scheduler/cache-aware/) - 2026年3月发布

[← 返回特性分析](/features/)
