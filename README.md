# hn-daily-digest

A daily archive of the [Hacker News](https://news.ycombinator.com) front page.

Every 3 hours a GitHub Actions job takes a snapshot of the front page and merges it into that day's archive. Stories that have dropped off are kept, and stories still on the page get fresh points and comment counts. By the end of the day the archive holds every story that reached the front page:

- `archive/YYYY/MM/YYYY-MM-DD.md`: a readable table of the day's stories, sorted by points
- `archive/YYYY/MM/YYYY-MM-DD.json`: the same data, ready for analysis

It uses the public [Algolia HN API](https://hn.algolia.com/api), falls back to the [official Firebase API](https://github.com/HackerNews/API), and has no dependencies beyond the Python standard library.

## Run it locally

```sh
python scripts/digest.py
```

<!-- digest:start -->
### Latest: [2026-11-17](archive/2026/11/2026-11-17.md)

Top 10 of 50 stories so far, last updated 2026-11-17 16:03 UTC. **19** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Carnegie Mellon is putting computer science courses on YouTube for free](https://www.cs.cmu.edu/learn/) <sub>cs.cmu.edu</sub> | 1997 | [268](https://news.ycombinator.com/item?id=50522980) |
| 2 | [Technical issue at JPMorgan Chase triggers online banking delays for US banks](https://apnews.com/article/bank-outage-chase-wells-fargo-truist-50fee2693c22f597fa6ca51a97ef2cda) <sub>apnews.com</sub> | 735 | [609](https://news.ycombinator.com/item?id=50521045) |
| 3 | [BugMeNot has closed](https://www.bugmenot.com/) <sub>bugmenot.com</sub> | 661 | [297](https://news.ycombinator.com/item?id=50523601) |
| 4 | [New Evidence Shows School Phone Bans Are Gradually Improving Test Scores](https://www.nytimes.com/2026/11/17/upshot/school-phone-bans-study-scores.html) <sub>nytimes.com</sub> | 612 | [310](https://news.ycombinator.com/item?id=50530163) |
| 5 | [Optimizely compromised, served malware on Zoom, GitLab](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) <sub>blog.report-uri.com</sub> | 524 | [208](https://news.ycombinator.com/item?id=50524767) |
| 6 | [Frame – 31.5" color ePaper display](https://trmnl.com/blog/introducing-frame) <sub>trmnl.com</sub> | 492 | [352](https://news.ycombinator.com/item?id=50519354) |
| 7 | [Jiff 1.0: A datetime library for Rust](https://burntsushi.net/jiff/) <sub>burntsushi.net</sub> | 419 | [91](https://news.ycombinator.com/item?id=50519744) |
| 8 | [Microsoft blames monster email outage on software defect introduced in July fix](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026) <sub>theregister.com</sub> | 405 | [302](https://news.ycombinator.com/item?id=50517321) |
| 9 | [What is w2rt6byl5nf1opmc-a.com?](https://jack.cab/blog/siterate) <sub>jack.cab</sub> | 390 | [155](https://news.ycombinator.com/item?id=50517602) |
| 10 | [Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use](https://xusheng.dev/posts/windows-coding-agent-telemetry/) <sub>xusheng.dev</sub> | 330 | [199](https://news.ycombinator.com/item?id=50524736) |
<!-- digest:end -->
