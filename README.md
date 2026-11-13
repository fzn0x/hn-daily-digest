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

Top 10 of 42 stories so far, last updated 2026-11-13 11:08 UTC. **15** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Jensen Huang resigns](https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f) <sub>apnews.com</sub> | 3598 | [3168](https://news.ycombinator.com/item?id=50467087) |
| 2 | [Anthropic IPO](https://ipo.anthropic.com/us/) <sub>ipo.anthropic.com</sub> | 941 | [869](https://news.ycombinator.com/item?id=50465829) |
| 3 | [Service degradation on Microsoft 365](https://status.cloud.microsoft/) <sub>status.cloud.microsoft</sub> | 922 | [800](https://news.ycombinator.com/item?id=50471731) |
| 4 | [Rust 1.100](https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/) <sub>blog.rust-lang.org</sub> | 701 | [262](https://news.ycombinator.com/item?id=50472038) |
| 5 | [Nvidia employees petition to bring back Jensen Huang](https://www.wired.com/story/nvidia-employees-petition-for-jensen-huangs-return/) <sub>wired.com</sub> | 614 | [455](https://news.ycombinator.com/item?id=50477231) |
| 6 | [Show HN: My $300 embroidery machine needed a subscription, so I built my own app](https://github.com/simpsoka/zigzag) <sub>github.com</sub> | 539 | [184](https://news.ycombinator.com/item?id=50470488) |
| 7 | [Gemini 4 Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) <sub>blog.google</sub> | 532 | [334](https://news.ycombinator.com/item?id=50471431) |
| 8 | [Gemini 4 Hydrogen and Orchestrator](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/) <sub>antigravity.google</sub> | 422 | [117](https://news.ycombinator.com/item?id=50472260) |
| 9 | [I'm making LLMs work on small and old devices](https://github.com/hyperionaidev/smolmaxxing/) <sub>github.com</sub> | 380 | [135](https://news.ycombinator.com/item?id=50468888) |
| 10 | [Writing correct software is hard and math alone won’t help us (2016)](https://pron.github.io/posts/correctness-and-complexity) <sub>pron.github.io</sub> | 358 | [168](https://news.ycombinator.com/item?id=50465352) |
<!-- digest:end -->
