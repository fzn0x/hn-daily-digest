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

Top 10 of 30 stories so far, last updated 2026-11-13 01:52 UTC. **15** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Jensen Huang resigns](https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f) <sub>apnews.com</sub> | 2955 | [2795](https://news.ycombinator.com/item?id=50467087) |
| 2 | [Anthropic IPO](https://ipo.anthropic.com/us/) <sub>ipo.anthropic.com</sub> | 821 | [806](https://news.ycombinator.com/item?id=50465829) |
| 3 | [Service degradation on Microsoft 365](https://status.cloud.microsoft/) <sub>status.cloud.microsoft</sub> | 511 | [466](https://news.ycombinator.com/item?id=50471731) |
| 4 | [Gemini 4 Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) <sub>blog.google</sub> | 464 | [297](https://news.ycombinator.com/item?id=50471431) |
| 5 | [Rust 1.100](https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/) <sub>blog.rust-lang.org</sub> | 421 | [172](https://news.ycombinator.com/item?id=50472038) |
| 6 | [Writing correct software is hard and math alone won’t help us (2016)](https://pron.github.io/posts/correctness-and-complexity) <sub>pron.github.io</sub> | 358 | [168](https://news.ycombinator.com/item?id=50465352) |
| 7 | [Show HN: My $300 embroidery machine needed a subscription, so I built my own app](https://github.com/simpsoka/zigzag) <sub>github.com</sub> | 341 | [138](https://news.ycombinator.com/item?id=50470488) |
| 8 | [Gemini 4 Hydrogen and Orchestrator](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/) <sub>antigravity.google</sub> | 304 | [72](https://news.ycombinator.com/item?id=50472260) |
| 9 | [I'm making LLMs work on small and old devices](https://github.com/hyperionaidev/smolmaxxing/) <sub>github.com</sub> | 279 | [95](https://news.ycombinator.com/item?id=50468888) |
| 10 | [Abandoned Quake 4 expansion finished by modders and now playable](https://www.moddb.com/mods/openq4/downloads/openq4-0141-windows-x64) <sub>moddb.com</sub> | 239 | [82](https://news.ycombinator.com/item?id=50467618) |
<!-- digest:end -->
