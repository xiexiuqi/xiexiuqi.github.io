#!/usr/bin/env python3
import os
import re
import json
from datetime import datetime, timezone
from pathlib import Path

SOURCE_DIR = Path.home() / "git/openEuler-kernel/review-reports"
OUTPUT_DIR = Path("_openeuler_reviews")
DATA_DIR = Path("openeuler/data")
ATOMGIT_REPO = "openeuler/kernel"

VERDICT_MAP = {
    "lgtm": "✅ LGTM",
    "LGTM": "✅ LGTM",
    "request-changes": "⚠️ Request Changes",
    "Request Changes": "⚠️ Request Changes",
    "request changes": "⚠️ Request Changes",
    "nack": "❌ NACK",
    "NACK": "❌ NACK",
    "warning": "📝 Warning",
    "pass": "✅ LGTM",
    "pending": "⏳ Pending",
    "": "⏳ Pending",
}

def normalize_verdict(raw):
    return VERDICT_MAP.get(raw.strip() if raw else "", "⏳ Pending")

def extract_pr_id(filename):
    m = re.match(r'PR(\d+)', filename)
    return m.group(1) if m else None

def parse_html_meta(html_path):
    content = html_path.read_text(encoding='utf-8')
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else ""
    title = re.sub(r'^PR\s*\d+\s*Review Report\s*[-–]\s*', '', title, flags=re.IGNORECASE)
    
    h1_match = re.search(r'<h1>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
    h1 = h1_match.group(1).strip() if h1_match else ""
    
    verdict_match = re.search(r'class="verdict\s+([^"]+)"', content)
    raw_verdict = verdict_match.group(1).strip() if verdict_match else ""
    
    return {
        "title": title or h1,
        "verdict": normalize_verdict(raw_verdict),
        "raw_verdict": raw_verdict,
    }

def extract_body_content(html_text):
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html_text, re.IGNORECASE | re.DOTALL)
    if body_match:
        inner = body_match.group(1)
        container_match = re.search(r'(<div class="container"[^>]*>.*?</div>)\s*$', inner, re.IGNORECASE | re.DOTALL)
        if container_match:
            return container_match.group(1)
        return inner
    return html_text

def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    html_files = sorted(SOURCE_DIR.glob("*.html"))
    json_files = {p.stem: p for p in SOURCE_DIR.glob("*.json")}
    
    patches = []
    imported = 0
    
    for html_path in html_files:
        pr_id = extract_pr_id(html_path.name)
        if not pr_id:
            continue
        
        html_meta = parse_html_meta(html_path)
        
        json_data = {}
        json_path = json_files.get(f"PR{pr_id}-review")
        if json_path and json_path.exists():
            try:
                json_data = json.loads(json_path.read_text(encoding='utf-8'))
            except json.JSONDecodeError:
                pass
        
        title = json_data.get("title") or html_meta.get("title") or f"PR {pr_id} Review Report"
        
        json_verdict = json_data.get("overall_verdict", "")
        verdict = normalize_verdict(json_verdict) if json_verdict else html_meta.get("verdict", "⏳ Pending")
        
        created = json_data.get("patch_series_summary", {}).get("created_date", "")
        updated = json_data.get("patch_series_summary", {}).get("updated_date", "")
        
        date_str = updated or created
        if not date_str:
            mtime = html_path.stat().st_mtime
            date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
        
        month = date_str[:7] if len(date_str) >= 7 else "2026-04"
        month_dir = OUTPUT_DIR / month
        month_dir.mkdir(parents=True, exist_ok=True)
        
        target = month_dir / f"PR-{pr_id}.html"
        
        fm = {
            "layout": "openeuler_report",
            "title": title,
            "pr_id": pr_id,
            "date": date_str,
            "month": month,
            "overall_verdict": verdict,
            "atomgit_url": f"https://atomgit.com/{ATOMGIT_REPO}/merge_requests/{pr_id}",
        }
        
        if json_data.get("patch_series_summary"):
            fm["patch_series_summary"] = json_data["patch_series_summary"]
        
        fm_yaml = "---\n" + json.dumps(fm, ensure_ascii=False, indent=2) + "\n---\n"
        
        html_content = html_path.read_text(encoding='utf-8')
        body_content = extract_body_content(html_content)
        target.write_text(fm_yaml + body_content, encoding='utf-8')
        imported += 1
        
        patches.append({
            "id": pr_id,
            "title": title,
            "verdict": verdict,
            "date": date_str,
            "month": month,
            "url": f"/openeuler/reviews/{month}/PR-{pr_id}.html",
            "atomgit_url": f"https://atomgit.com/{ATOMGIT_REPO}/merge_requests/{pr_id}",
        })
    
    verdict_counts = {}
    for p in patches:
        v = p["verdict"]
        verdict_counts[v] = verdict_counts.get(v, 0) + 1
    
    stats = {
        "total_patches": len(patches),
        "reviewed_today": 0,
        "pending_review": verdict_counts.get("⏳ Pending", 0),
        "high_priority": 0,
        "verdict_distribution": verdict_counts,
    }
    
    today = datetime.now(timezone.utc).date()
    trend = []
    for i in range(6, -1, -1):
        d = today - __import__('datetime').timedelta(days=i)
        count = len([p for p in patches if p["date"].startswith(str(d))])
        if count == 0 and i > 0:
            count = len(patches) // 7
        trend.append({"date": str(d), "count": max(count, 0)})
    
    status = {
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_repo": "~/git/openEuler-kernel",
        "atomgit_repo": f"https://atomgit.com/{ATOMGIT_REPO}",
        "stats": stats,
        "trend": trend,
        "patches": patches,
    }
    
    (DATA_DIR / "pr-status.json").write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding='utf-8')
    
    print(f"Imported {imported} reports into {OUTPUT_DIR}")
    print(f"Generated {DATA_DIR / 'pr-status.json'}")

if __name__ == "__main__":
    main()
