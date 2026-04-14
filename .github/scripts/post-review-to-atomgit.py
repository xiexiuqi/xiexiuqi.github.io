#!/usr/bin/env python3
"""
Post AI review reports to atomgit MR comments.

This is a helper script to automate posting review reports as comments
on the corresponding atomgit merge requests.

PREREQUISITES:
- You need an atomgit personal access token with repo/comment permissions.
- Set it as environment variable: ATOMGIT_TOKEN

USAGE:
    ATOMGIT_TOKEN=xxx python post-review-to-atomgit.py --pr-id 19935
    ATOMGIT_TOKEN=xxx python post-review-to-atomgit.py --all --dry-run

NOTES:
- AtomGit API endpoint for MR comments:
  POST https://api.atomgit.com/api/v5/repos/openeuler/kernel/pulls/{number}/comments
- Or via the versioned API:
  POST https://api.atomgit.com/repos/openeuler/kernel/change-requests/{number}/comments
- Rate limit: 10 req/s, 5000/hour for authenticated users.
"""
import argparse
import json
import os
import sys
import textwrap
from pathlib import Path

try:
    import requests
except ImportError:
    print("Please install requests: pip install requests")
    sys.exit(1)

OWNER = "openeuler"
REPO = "kernel"
API_BASE = "https://api.atomgit.com"
REPORTS_DIR = Path.home() / "git/openEuler-kernel/review-reports"


def html_to_markdown(html_text):
    """Very basic HTML to markdown conversion for review reports."""
    md = html_text
    md = md.replace("<h1>", "# ").replace("</h1>", "")
    md = md.replace("<h2>", "## ").replace("</h2>", "")
    md = md.replace("<h3>", "### ").replace("</h3>", "")
    md = md.replace("<strong>", "**").replace("</strong>", "**")
    md = md.replace("<em>", "*").replace("</em>", "*")
    md = md.replace("<ul>", "").replace("</ul>", "")
    md = md.replace("<ol>", "").replace("</ol>", "")
    md = md.replace("<li>", "- ").replace("</li>", "")
    md = md.replace("<br>", "\n").replace("<br/>", "\n")
    md = md.replace("<p>", "\n").replace("</p>", "\n")
    md = md.replace("<div class='section'>", "\n---\n").replace("</div>", "")
    md = md.replace("<div class=\"section\">", "\n---\n").replace("</div>", "")
    md = md.replace("<table class='findings'>", "\n").replace("</table>", "\n")
    md = md.replace("<table>", "\n").replace("</table>", "\n")
    md = md.replace("<tr>", "").replace("</tr>", "\n")
    md = md.replace("<th>", "| **").replace("</th>", "** ")
    md = md.replace("<td>", "| ").replace("</td>", " ")
    md = md.replace("<thead>", "").replace("</thead>", "")
    md = md.replace("<tbody>", "").replace("</tbody>", "")
    return textwrap.shorten(md, width=65000) if len(md) > 65000 else md


def post_comment(pr_id, body, token, dry_run=False):
    url = f"{API_BASE}/api/v5/repos/{OWNER}/{REPO}/pulls/{pr_id}/comments"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Api-Version": "2023-02-21",
    }
    payload = {"body": body}

    if dry_run:
        print(f"[DRY RUN] Would POST to {url}")
        print(f"[DRY RUN] Body preview ({len(body)} chars):")
        print(body[:500] + "..." if len(body) > 500 else body)
        return True

    resp = requests.post(url, headers=headers, json=payload, timeout=30)
    if resp.status_code in (200, 201):
        print(f"✅ Posted comment to PR {pr_id}")
        return True
    else:
        print(f"❌ Failed to post comment to PR {pr_id}: {resp.status_code}")
        print(resp.text)
        return False


def main():
    parser = argparse.ArgumentParser(description="Post review reports to atomgit MRs")
    parser.add_argument("--pr-id", type=str, help="Target PR ID")
    parser.add_argument("--all", action="store_true", help="Post all available reports")
    parser.add_argument("--dry-run", action="store_true", help="Preview without posting")
    args = parser.parse_args()

    token = os.environ.get("ATOMGIT_TOKEN")
    if not token and not args.dry_run:
        print("Error: ATOMGIT_TOKEN environment variable is required.")
        sys.exit(1)

    if args.all:
        html_files = sorted(REPORTS_DIR.glob("PR*.html"))
        for html_path in html_files:
            pr_id = html_path.stem.split("-")[0].replace("PR", "")
            html_content = html_path.read_text(encoding="utf-8")
            body = html_to_markdown(html_content)
            post_comment(pr_id, body, token, dry_run=args.dry_run)
    elif args.pr_id:
        html_path = REPORTS_DIR / f"PR{args.pr_id}-*.html"
        matches = list(REPORTS_DIR.glob(f"PR{args.pr_id}*.html"))
        if not matches:
            print(f"Report not found for PR {args.pr_id}")
            sys.exit(1)
        html_content = matches[0].read_text(encoding="utf-8")
        body = html_to_markdown(html_content)
        post_comment(args.pr_id, body, token, dry_run=args.dry_run)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
