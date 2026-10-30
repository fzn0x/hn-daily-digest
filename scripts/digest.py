"""Snapshot the Hacker News front page into a dated Markdown + JSON archive."""

import json
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "archive"
README = ROOT / "README.md"
START, END = "<!-- digest:start -->", "<!-- digest:end -->"
LIMIT = 30
README_TOP = 10
HEADERS = {"User-Agent": "hn-daily-digest/1.0"}


def get_json(url, tries=4):
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=20) as resp:
                return json.load(resp)
        except Exception:
            if attempt == tries - 1:
                raise
            time.sleep(5 * 2**attempt)


def from_algolia():
    data = get_json(f"https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage={LIMIT}")
    return [
        {
            "id": int(hit["objectID"]),
            "title": hit["title"],
            "url": hit.get("url"),
            "points": hit.get("points") or 0,
            "comments": hit.get("num_comments") or 0,
            "by": hit.get("author"),
        }
        for hit in data["hits"]
    ]


def from_firebase():
    base = "https://hacker-news.firebaseio.com/v0"
    stories = []
    for story_id in get_json(f"{base}/topstories.json")[:LIMIT]:
        item = get_json(f"{base}/item/{story_id}.json")
        if not item or item.get("type") != "story":
            continue
        stories.append(
            {
                "id": item["id"],
                "title": item.get("title", ""),
                "url": item.get("url"),
                "points": item.get("score", 0),
                "comments": item.get("descendants", 0),
                "by": item.get("by"),
            }
        )
    return stories


def fetch_stories():
    try:
        stories = from_algolia()
    except Exception as exc:
        print(f"algolia failed ({exc}), falling back to firebase", file=sys.stderr)
        stories = []
    return stories or from_firebase()


def md_text(text):
    return text.replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")


def story_rows(stories):
    rows = ["| # | Story | Points | Comments |", "|--:|---|--:|--:|"]
    for rank, s in enumerate(stories, 1):
        thread = f"https://news.ycombinator.com/item?id={s['id']}"
        link = s["url"] or thread
        domain = urlparse(s["url"]).netloc.removeprefix("www.") if s["url"] else "news.ycombinator.com"
        rows.append(
            f"| {rank} | [{md_text(s['title'])}]({link}) <sub>{domain}</sub> "
            f"| {s['points']} | [{s['comments']}]({thread}) |"
        )
    return "\n".join(rows)


def main():
    now = datetime.now(timezone.utc)
    day = now.strftime("%Y-%m-%d")
    stamp = now.strftime("%Y-%m-%d %H:%M UTC")
    snapshot = fetch_stories()
    if not snapshot:
        raise SystemExit("no stories fetched")

    folder = ARCHIVE / now.strftime("%Y") / now.strftime("%m")
    folder.mkdir(parents=True, exist_ok=True)
    json_path = folder / f"{day}.json"

    # Merge into today's file: keep stories that dropped off, refresh stats on ones still up.
    previous = {"snapshots": 0, "stories": []}
    if json_path.exists():
        previous = json.loads(json_path.read_text(encoding="utf-8"))
    merged = {s["id"]: s for s in previous["stories"]}
    new = sum(s["id"] not in merged for s in snapshot)
    merged.update((s["id"], s) for s in snapshot)
    stories = sorted(merged.values(), key=lambda s: s["points"], reverse=True)
    snapshots = previous["snapshots"] + 1

    json_path.write_text(
        json.dumps(
            {"date": day, "updated_at": now.isoformat(timespec="seconds"), "snapshots": snapshots, "stories": stories},
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (folder / f"{day}.md").write_text(
        f"# Hacker News front page, {day}\n\n"
        f"Every story that reached the front page today, merged from {snapshots} "
        f"snapshot{'' if snapshots == 1 else 's'}. Last updated {stamp}, sorted by points.\n\n"
        f"{story_rows(stories)}\n",
        encoding="utf-8",
    )

    days = len(list(ARCHIVE.glob("*/*/*.md")))
    rel = f"archive/{now:%Y}/{now:%m}/{day}.md"
    block = (
        f"{START}\n"
        f"### Latest: [{day}]({rel})\n\n"
        f"Top {README_TOP} of {len(stories)} stories so far, last updated {stamp}. "
        f"**{days}** {'day' if days == 1 else 'days'} archived.\n\n"
        f"{story_rows(stories[:README_TOP])}\n"
        f"{END}"
    )
    readme = README.read_text(encoding="utf-8")
    head, rest = readme.split(START, 1)
    tail = rest.split(END, 1)[1]
    README.write_text(head + block + tail, encoding="utf-8")

    # Single stdout line; the workflow uses it as the commit message.
    print(f"{stamp}, {new} new, {len(stories)} today")


if __name__ == "__main__":
    main()
