---
layout: default
title: Home
---

# 欢迎来到我的博客

这里是我的技术博客，主要分享：

- **Linux 内核** - 性能优化、新特性分析
- **性能调优** - 系统性能分析与优化实践
- **技术探索** - 前沿技术研究与应用

## 最新文章

<ul>
  {% for post in site.posts limit:5 %}
    <li>
      <span>{{ post.date | date: "%Y-%m-%d" }}</span>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

[查看所有文章](/posts/)

## 关于我

我是 Xie Xiuqi，专注于 Linux 系统与内核技术研究。

- GitHub: [@xiexiuqi](https://github.com/xiexiuqi)
