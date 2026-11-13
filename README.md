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
### Latest: [2026-11-13](archive/2026/11/2026-11-13.md)

Top 10 of 65 stories so far, last updated 2026-11-13 19:50 UTC. **15** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Jensen Huang resigns](https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f) <sub>apnews.com</sub> | 3982 | [3384](https://news.ycombinator.com/item?id=50467087) |
| 2 | [Anthropic IPO](https://ipo.anthropic.com/us/) <sub>ipo.anthropic.com</sub> | 941 | [869](https://news.ycombinator.com/item?id=50465829) |
| 3 | [Service degradation on Microsoft 365](https://status.cloud.microsoft/) <sub>status.cloud.microsoft</sub> | 922 | [800](https://news.ycombinator.com/item?id=50471731) |
| 4 | [Rust 1.100](https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/) <sub>blog.rust-lang.org</sub> | 862 | [310](https://news.ycombinator.com/item?id=50472038) |
| 5 | [Show HN: My $300 embroidery machine needed a subscription, so I built my own app](https://github.com/simpsoka/zigzag) <sub>github.com</sub> | 711 | [231](https://news.ycombinator.com/item?id=50470488) |
| 6 | [Nvidia employees petition to bring back Jensen Huang](https://www.wired.com/story/nvidia-employees-petition-for-jensen-huangs-return/) <sub>wired.com</sub> | 614 | [455](https://news.ycombinator.com/item?id=50477231) |
| 7 | [LibreOffice actually works 365 days a year](https://twitter.com/LibreOffice/status/2121205272479998268) <sub>twitter.com</sub> | 573 | [196](https://news.ycombinator.com/item?id=50486482) |
| 8 | [Reverse engineering my Coway air purifier to ditch the cloud](https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/) <sub>scottjg.com</sub> | 556 | [157](https://news.ycombinator.com/item?id=50474959) |
| 9 | [Gemini 4 Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) <sub>blog.google</sub> | 532 | [334](https://news.ycombinator.com/item?id=50471431) |
| 10 | [Elevated errors on claude.ai, Claude Code, and platform.claude.com](https://status.claude.com/incidents/nn11wk485zfn) <sub>status.claude.com</sub> | 460 | [373](https://news.ycombinator.com/item?id=50481187) |
<!-- digest:end -->
