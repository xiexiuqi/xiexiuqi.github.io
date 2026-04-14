// 简单的站内搜索功能
let searchIndex = [];
let searchIndexLoaded = false;

// 初始化搜索
async function initSearch() {
  try {
    // 尝试加载搜索索引
    const response = await fetch('/api/search-index.json');
    if (response.ok) {
      searchIndex = await response.json();
      searchIndexLoaded = true;
      console.log('搜索索引加载完成:', searchIndex.length, '条记录');
    } else {
      console.log('搜索索引未找到，使用备用方案');
      // 备用：从页面提取数据
      buildIndexFromPage();
    }
  } catch (error) {
    console.log('加载搜索索引失败:', error);
    buildIndexFromPage();
  }
}

// 从当前页面构建简单索引
function buildIndexFromPage() {
  const links = document.querySelectorAll('a[href^="/"]');
  searchIndex = Array.from(links).map(link => ({
    title: link.textContent.trim(),
    url: link.href,
    excerpt: ''
  })).filter(item => item.title.length > 0);
  searchIndexLoaded = true;
}

// 执行搜索
function performSearch() {
  const query = document.getElementById('search-input').value.trim().toLowerCase();
  const resultsContainer = document.getElementById('search-results');
  
  if (!query) {
    resultsContainer.innerHTML = '<p>请输入搜索关键词</p>';
    return;
  }
  
  resultsContainer.innerHTML = '<p>搜索中...</p>';
  
  // 简单搜索：匹配标题
  const results = searchIndex.filter(item => {
    const title = (item.title || '').toLowerCase();
    const excerpt = (item.excerpt || '').toLowerCase();
    return title.includes(query) || excerpt.includes(query);
  });
  
  displayResults(results, query);
}

// 显示搜索结果
function displayResults(results, query) {
  const container = document.getElementById('search-results');
  
  if (results.length === 0) {
    container.innerHTML = `<p>未找到与 "<strong>${escapeHtml(query)}</strong>" 相关的内容。</p>
      <p>建议：</p>
      <ul>
        <li>检查关键词拼写</li>
        <li>尝试使用更通用的关键词</li>
        <li>浏览 <a href="/daily/">日报</a> 或 <a href="/reports/">报告</a> 页面</li>
      </ul>`;
    return;
  }
  
  let html = `<h3>找到 ${results.length} 个结果：</h3><ul class="search-result-list">`;
  
  results.forEach(item => {
    html += `
      <li class="search-result-item">
        <a href="${escapeHtml(item.url)}" class="search-result-title">${highlightText(escapeHtml(item.title), query)}</a>
        ${item.excerpt ? `<p class="search-result-excerpt">${highlightText(escapeHtml(item.excerpt), query)}</p>` : ''}
      </li>
    `;
  });
  
  html += '</ul>';
  container.innerHTML = html;
}

// HTML 转义
function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

// 高亮匹配文本
function highlightText(text, query) {
  if (!query) return text;
  const regex = new RegExp(`(${escapeRegExp(query)})`, 'gi');
  return text.replace(regex, '<mark>$1</mark>');
}

// 转义正则特殊字符
function escapeRegExp(string) {
  return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}
