---
layout: default
title: Review 报告归档
---

<h1>openEuler Kernel Review 报告</h1>

<p>按月份归档的 AI 辅助内核补丁 Review 报告。</p>

{% assign reviews = site.openeuler_reviews | sort: 'date' | reverse %}

{% if reviews.size == 0 %}
  <p>暂无 Review 报告。</p>
{% else %}
  {% assign month_groups = reviews | group_by_exp: 'item', 'item.date | slice: 0, 7' %}
  
  {% for group in month_groups %}
    <h2>{{ group.name }}</h2>
    <p>共 {{ group.items | size }} 份报告</p>
    
    <ul class="post-list">
      {% for review in group.items %}
        <li>
          <span class="post-date">{{ review.date | date: "%Y-%m-%d" }}</span>
          <a href="{{ review.url | relative_url }}">{{ review.title }}</a>
          {% if review.pr_id %}
            <span class="post-tag">PR {{ review.pr_id }}</span>
          {% endif %}
          {% if review.overall_verdict %}
            <span class="badge {{ review.overall_verdict | slugify }}">{{ review.overall_verdict }}</span>
          {% endif %}
        </li>
      {% endfor %}
    </ul>
  {% endfor %}
{% endif %}
