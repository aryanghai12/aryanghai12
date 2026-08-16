#!/usr/bin/env python3
"""Regenerate the text stat blocks in README.md from live GitHub data.

Everything rendered here is plain text between HTML marker comments -- no SVG,
no external image service. Run locally with `python3 scripts/profile_stats.py`
or let .github/workflows/profile-stats.yml run it on a schedule.

Set GITHUB_TOKEN to lift the 60 req/hour anonymous rate limit.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USER = "aryanghai12"
README = Path(__file__).resolve().parent.parent / "README.md"

API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

# Languages that describe markup, config or build glue rather than authored logic.
NON_CODE_LANGS = {
    "HTML", "CSS", "SCSS", "TeX", "Makefile", "Dockerfile", "HCL",
    "Go Template", "Smarty", "Mustache", "Handlebars", "Batchfile",
}

# Forks kept purely as contribution workspaces -- they are not authored work.
CARD_WIDTH = 62


def api(path: str, params: dict | None = None, retries: int = 3):
    url = path if path.startswith("http") else f"{API}{path}"
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USER}-profile-stats",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"

    for attempt in range(retries):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            # Secondary rate limits and 202 (stats still computing) are retryable.
            if exc.code in (403, 429, 202) and attempt < retries - 1:
                time.sleep(2 ** attempt * 3)
                continue
            raise
    raise RuntimeError(f"exhausted retries for {url}")


def paged(path: str, params: dict | None = None, cap: int = 300):
    params = dict(params or {})
    params["per_page"] = 100
    out, page = [], 1
    while len(out) < cap:
        params["page"] = page
        batch = api(path, params)
        if not batch:
            break
        out.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return out


def search(query: str, cap: int = 300):
    """Paginate the issue/PR search API, returning (total_count, items)."""
    items, page, total = [], 1, 0
    while len(items) < cap:
        data = api("/search/issues", {"q": query, "per_page": 100, "page": page})
        total = data.get("total_count", 0)
        batch = data.get("items", [])
        items.extend(batch)
        if len(batch) < 100 or len(items) >= total:
            break
        page += 1
        time.sleep(2)  # search API is rate limited far more aggressively
    return total, items


def repo_of(item: dict) -> str:
    return item["repository_url"].replace(f"{API}/repos/", "")


def human_span(since: datetime, until: datetime) -> str:
    months = (until.year - since.year) * 12 + (until.month - since.month)
    if until.day < since.day:
        months -= 1
    years, months = divmod(max(months, 0), 12)
    parts = []
    if years:
        parts.append(f"{years} year{'s' if years != 1 else ''}")
    if months:
        parts.append(f"{months} month{'s' if months != 1 else ''}")
    return ", ".join(parts) or "brand new"


def collect() -> dict:
    now = datetime.now(timezone.utc)

    user = api(f"/users/{USER}")
    repos = paged(f"/users/{USER}/repos", {"sort": "updated"})
    sources = [r for r in repos if not r["fork"]]
    forks = [r for r in repos if r["fork"]]

    # --- language mix across authored (non-fork) repositories -----------------
    langs: dict[str, int] = {}
    for repo in sources:
        if repo.get("size", 0) == 0:
            continue
        for lang, size in api(f"/repos/{USER}/{repo['name']}/languages").items():
            if lang not in NON_CODE_LANGS:
                langs[lang] = langs.get(lang, 0) + size

    # --- pull requests --------------------------------------------------------
    opened_total, _ = search(f"author:{USER} type:pr")
    merged_total, merged = search(f"author:{USER} type:pr is:merged")
    issues_total, _ = search(f"author:{USER} type:issue")

    try:
        commits = api(
            "/search/commits", {"q": f"author:{USER}", "per_page": 1}
        ).get("total_count", 0)
    except urllib.error.HTTPError:
        commits = 0

    # --- diff volume across merged PRs ---------------------------------------
    additions = deletions = files = 0
    per_repo: dict[str, dict] = {}
    for item in merged:
        repo = repo_of(item)
        entry = per_repo.setdefault(
            repo, {"merged": 0, "add": 0, "del": 0, "last": item["closed_at"]}
        )
        entry["merged"] += 1
        entry["last"] = max(entry["last"], item["closed_at"])
        try:
            pr = api(f"/repos/{repo}/pulls/{item['number']}")
        except urllib.error.HTTPError:
            continue
        additions += pr.get("additions", 0)
        deletions += pr.get("deletions", 0)
        files += pr.get("changed_files", 0)
        entry["add"] += pr.get("additions", 0)
        entry["del"] += pr.get("deletions", 0)

    upstream = {k: v for k, v in per_repo.items() if not k.startswith(f"{USER}/")}

    return {
        "generated": now,
        "uptime": human_span(
            datetime.strptime(user["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=timezone.utc
            ),
            now,
        ),
        "joined": datetime.strptime(user["created_at"], "%Y-%m-%dT%H:%M:%SZ"),
        "repos": user["public_repos"],
        "sources": len(sources),
        "forks": len(forks),
        "commits": commits,
        "prs_opened": opened_total,
        "prs_merged": merged_total,
        "issues": issues_total,
        "additions": additions,
        "deletions": deletions,
        "files": files,
        "langs": langs,
        "upstream": upstream,
        "upstream_merged": sum(v["merged"] for v in upstream.values()),
        "upstream_repos": len(upstream),
        "upstream_orgs": len({k.split("/")[0] for k in upstream}),
    }


# --------------------------------------------------------------------------- #
# rendering
# --------------------------------------------------------------------------- #

def box(title: str, rows: list[tuple[str, str]]) -> list[str]:
    """A single-rule card, sized to its contents so nothing ever wraps."""
    label_w = max(len(label) for label, _ in rows) + 4
    body = [f"   {label:<{label_w}}{value}" for label, value in rows]

    width = max(CARD_WIDTH, max(len(line) for line in body) + 3)
    head = f"─ {title} "

    return [
        "┌" + head + "─" * (width - len(head)) + "┐",
        "│" + " " * width + "│",
        *("│" + line.ljust(width) + "│" for line in body),
        "│" + " " * width + "│",
        "└" + "─" * width + "┘",
    ]


def language_summary(langs: dict[str, int], top: int = 3) -> str:
    total = sum(langs.values()) or 1
    ranked = sorted(langs.items(), key=lambda kv: -kv[1])[:top]
    return "  ·  ".join(f"{name} {size / total * 100:.0f}%" for name, size in ranked)


def render_stats(s: dict) -> str:
    rows = [
        ("active", f"{s['uptime']}, since {s['joined']:%B %Y}"),
        ("repositories", f"{s['repos']} public  ·  {s['sources']} authored  ·  {s['forks']} forks"),
        ("commits", f"{s['commits']:,}"),
        ("pull requests", f"{s['prs_opened']} opened  ·  {s['prs_merged']} merged"),
        ("upstream", f"{s['upstream_merged']} merged across {s['upstream_repos']} external repositories"),
        ("lines shipped", f"+{s['additions']:,}  /  -{s['deletions']:,}  across {s['files']:,} files"),
        ("issues", f"{s['issues']} filed"),
        ("languages", language_summary(s["langs"])),
    ]
    return "\n".join(["```text", *box(f"{USER}@github", rows), "```"])


UPSTREAM_LABELS = {
    "kubescape": "Kubescape · CNCF incubating · Kubernetes security",
    "OWASP": "OWASP · Open Worldwide Application Security Project",
    "antiwork": "Antiwork · Gumroad",
    "kyverno": "Kyverno · CNCF policy engine",
    "openyurtio": "OpenYurt · CNCF edge Kubernetes",
    "Vanshikadahaliya": "Smart India Hackathon · team project",
}


def render_upstream(s: dict) -> str:
    grouped: dict[str, list[tuple[str, dict]]] = {}
    for repo, data in s["upstream"].items():
        grouped.setdefault(repo.split("/")[0], []).append((repo, data))

    order = sorted(
        grouped.items(),
        key=lambda kv: -sum(d["merged"] for _, d in kv[1]),
    )

    lines = [
        "| Where | Repository | Merged | Lines |",
        "| :-- | :-- | --: | :-- |",
    ]
    for org, repos in order:
        label = UPSTREAM_LABELS.get(org, org)
        for i, (repo, data) in enumerate(sorted(repos, key=lambda kv: -kv[1]["merged"])):
            org_cell = f"**{label}**" if i == 0 else ""
            lines.append(
                f"| {org_cell} | [`{repo.split('/')[1]}`](https://github.com/{repo}/pulls?q=is%3Apr+author%3A{USER}) "
                f"| {data['merged']} | `+{data['add']:,}` `-{data['del']:,}` |"
            )
    return "\n".join(lines)


def splice(text: str, key: str, body: str) -> str:
    start, end = f"<!--START:{key}-->", f"<!--END:{key}-->"
    pattern = re.compile(
        f"{re.escape(start)}.*?{re.escape(end)}", re.DOTALL
    )
    if not pattern.search(text):
        raise SystemExit(f"marker pair for '{key}' not found in README.md")
    return pattern.sub(f"{start}\n{body}\n{end}", text)


CACHE = Path(__file__).resolve().parent / ".stats-cache.json"


def save_cache(stats: dict) -> None:
    payload = dict(stats)
    payload["generated"] = stats["generated"].isoformat()
    payload["joined"] = stats["joined"].isoformat()
    CACHE.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def load_cache() -> dict:
    payload = json.loads(CACHE.read_text(encoding="utf-8"))
    payload["generated"] = datetime.fromisoformat(payload["generated"])
    payload["joined"] = datetime.fromisoformat(payload["joined"])
    return payload


def main() -> int:
    # --cached re-renders from the last API sweep, for iterating on layout
    # without spending rate limit.
    if "--cached" in sys.argv:
        stats = load_cache()
    else:
        stats = collect()
        save_cache(stats)

    readme = README.read_text(encoding="utf-8")
    readme = splice(readme, "stats", render_stats(stats))
    readme = splice(readme, "upstream", render_upstream(stats))
    readme = re.sub(
        r"(?<=<!--STAMP-->).*?(?=<!--/STAMP-->)",
        f"last synced {stats['generated']:%d %b %Y}",
        readme,
        flags=re.DOTALL,
    )
    README.write_text(readme, encoding="utf-8")
    print(f"README.md updated · {stats['prs_merged']} merged PRs · "
          f"+{stats['additions']:,}/-{stats['deletions']:,} lines")
    return 0


if __name__ == "__main__":
    sys.exit(main())
