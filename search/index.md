---
layout: default
title: 搜索
permalink: /search/
---

# 🔍 搜索

输入关键词搜索网站内容。

<div class="search-container">
  <input type="text" id="search-input" placeholder="输入关键词搜索..." class="search-input">
  <button onclick="performSearch()" class="btn btn-primary">搜索</button>
</div>

<div id="search-results" class="search-results">
  <!-- 搜索结果将显示在这里 -->
</div>

<script src="/assets/js/search.js"></script>
<script>
  // 页面加载时初始化搜索
  document.addEventListener('DOMContentLoaded', function() {
    initSearch();
    
    // 绑定回车键
    document.getElementById('search-input').addEventListener('keypress', function(e) {
      if (e.key === 'Enter') {
        performSearch();
      }
    });
  });
</script>
