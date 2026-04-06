#!/usr/bin/env python3
"""
PDF to HTML converter with formatting preservation
"""
import pdfplumber
import sys
from pathlib import Path

def convert_pdf_to_html(pdf_path, output_path):
    """Convert PDF to HTML with basic formatting"""
    
    html_content = []
    
    # HTML header with basic styling
    html_header = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>ASPLOS 2026 操作系统性能相关论文调研报告</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"/>
    <style>
        body {
            font-family: 'Inter', 'Noto Serif SC', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }
        .content-wrapper {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        .report-card {
            background: white;
            border-radius: 16px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        .report-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 3rem;
            text-align: center;
        }
        .report-title {
            font-family: 'Noto Serif SC', serif;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }
        .report-content {
            padding: 3rem;
            line-height: 1.8;
        }
        .pdf-page {
            background: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 8px;
            padding: 2rem;
            margin-bottom: 2rem;
        }
        .pdf-page-number {
            text-align: center;
            color: #6c757d;
            font-size: 0.875rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #dee2e6;
        }
        .text-content {
            font-size: 1rem;
            color: #333;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        .highlight-box {
            background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
            border-left: 4px solid #667eea;
            padding: 1.5rem;
            margin: 1.5rem 0;
            border-radius: 0 8px 8px 0;
        }
        @media (max-width: 768px) {
            .content-wrapper {
                padding: 1rem;
            }
            .report-title {
                font-size: 1.75rem;
            }
            .report-content {
                padding: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="content-wrapper">
        <article class="report-card">
            <header class="report-header">
                <h1 class="report-title">ASPLOS 2026 操作系统性能相关论文调研报告</h1>
                <p class="text-lg opacity-90">PDF转换版本 | 原始格式保留</p>
            </header>
            <div class="report-content">
"""
    
    html_content.append(html_header)
    
    # Extract content from PDF
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            html_content.append(f'                <div class="pdf-page">')
            html_content.append(f'                    <div class="pdf-page-number">第 {i} 页 / 共 {len(pdf.pages)} 页</div>')
            html_content.append('                    <div class="text-content">')
            
            # Extract text
            text = page.extract_text()
            if text:
                # Escape HTML special characters
                text = text.replace('&', '&amp;')
                text = text.replace('<', '&lt;')
                text = text.replace('>', '&gt;')
                html_content.append(text)
            else:
                html_content.append('<em class="text-gray-500">[本页主要为图表，请查看原始PDF]</em>')
            
            html_content.append('                    </div>')
            html_content.append('                </div>')
    
    # HTML footer
    html_footer = """            </div>
        </article>
    </div>
</body>
</html>"""
    
    html_content.append(html_footer)
    
    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_content))
    
    print(f"✅ PDF 转换完成！")
    print(f"📄 输出文件: {output_path}")

if __name__ == '__main__':
    pdf_path = "/mnt/c/Users/xiexiuqi/Downloads/ASPLOS 2026 操作系统性能相关论文调研报告.pdf"
    output_path = "/tmp/asplos_2026_pdf.html"
    convert_pdf_to_html(pdf_path, output_path)
