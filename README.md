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
### Latest: [2026-11-23](archive/2026/11/2026-11-23.md)

Top 10 of 30 stories so far, last updated 2026-11-23 01:47 UTC. **25** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Toyota, Nissan, and Honda to standardize parts to lower costs](https://www.caranddriver.com/news/a74490092/toyota-nissan-honda-standardize-parts-lower-costs/) <sub>caranddriver.com</sub> | 1190 | [680](https://news.ycombinator.com/item?id=50596133) |
| 2 | [Perplexity and Intelligence](https://openai.com/index/perplexity-and-intelligence/) <sub>openai.com</sub> | 482 | [334](https://news.ycombinator.com/item?id=50601525) |
| 3 | [What Happened to Silicon Valley?](https://www.oreilly.com/radar/what-happened-to-silicon-valley/) <sub>oreilly.com</sub> | 420 | [241](https://news.ycombinator.com/item?id=50602947) |
| 4 | [The Birds of GTA 6: A Field Guide to Vice City and Leonida's Wildlife](https://www.audubon.org/magazine/birds-of-gta-6-field-guide-vice-city-wildlife) <sub>audubon.org</sub> | 349 | [157](https://news.ycombinator.com/item?id=50602843) |
| 5 | [Show HN: I built a game where you are an LLM's subagent](https://github.com/gulivan/worker755) <sub>github.com</sub> | 271 | [64](https://news.ycombinator.com/item?id=50599762) |
| 6 | [Open Social Web Alliance](https://osw-alliance.net/en/) <sub>osw-alliance.net</sub> | 222 | [215](https://news.ycombinator.com/item?id=50600511) |
| 7 | [A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth) <sub>gpupartner.com</sub> | 217 | [75](https://news.ycombinator.com/item?id=50603845) |
| 8 | [Progress map for the Lean formalization of Alessandro Masullo's manuscript](https://claude.ai/artifact/CtQyX8qfYAF822bgHJHHE3) <sub>claude.ai</sub> | 149 | [115](https://news.ycombinator.com/item?id=50605045) |
| 9 | [A miniature San Francisco with live buses, planes and boats](https://smallsf.com/) <sub>smallsf.com</sub> | 142 | [55](https://news.ycombinator.com/item?id=50603589) |
| 10 | [I joined the NTP Pool, but not with my Stratum 1 Pi](https://www.jeffgeerling.com/blog/2026/i-joined-the-ntp-pool/) <sub>jeffgeerling.com</sub> | 126 | [37](https://news.ycombinator.com/item?id=50600622) |
<!-- digest:end -->
