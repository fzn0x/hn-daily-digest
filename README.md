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
### Latest: [2026-11-01](archive/2026/11/2026-11-01.md)

Top 10 of 30 stories so far, last updated 2026-11-01 06:08 UTC. **3** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [HackerTube: YouTube built from videos recommended by HN](https://karpathy.bearblog.dev/hacker-tube/) <sub>karpathy.bearblog.dev</sub> | 1002 | [307](https://news.ycombinator.com/item?id=50319510) |
| 2 | [TCP Use-After-Free: CVE-2026-98432 / CVSS 9.8](https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf) <sub>atlasum.net</sub> | 440 | [205](https://news.ycombinator.com/item?id=50319143) |
| 3 | [Do the math: How we took over ChatGPT accounts](https://www.parameter.ai/labs/we-found-a-gap-at-openai) <sub>parameter.ai</sub> | 316 | [157](https://news.ycombinator.com/item?id=50314699) |
| 4 | [Anthropic blocks users for anything touching training larger models](https://twitter.com/jiahaoshao1/status/2116475922190922088) <sub>twitter.com</sub> | 290 | [162](https://news.ycombinator.com/item?id=50319358) |
| 5 | [An Italian farmer found some unknown seeds in his attic and planted them](https://www.smithsonianmag.com/science-nature/italian-farmer-found-unknown-seeds-attic-with-nothing-lose-planted-them-result-biblical-180989644/) <sub>smithsonianmag.com</sub> | 283 | [77](https://news.ycombinator.com/item?id=50320963) |
| 6 | [Jepsen: ParticleDB 1.1.4](https://jepsen.io/analyses/particledb-1.1.4) <sub>jepsen.io</sub> | 236 | [127](https://news.ycombinator.com/item?id=50316100) |
| 7 | [Simple circuits can create complex behaviors](https://aatishb.com/myriad/lets-build-a-brain/) <sub>aatishb.com</sub> | 231 | [75](https://news.ycombinator.com/item?id=50261253) |
| 8 | [It's the memory latency, stupid](https://pivotlake.io/blog/its-the-memory-latency-stupid/) <sub>pivotlake.io</sub> | 171 | [46](https://news.ycombinator.com/item?id=50318720) |
| 9 | [Memdoor: A team of 5 Qwen3.8-27B models beats Fable 5 on LiveCodeBench Hard](https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve) <sub>github.com</sub> | 163 | [90](https://news.ycombinator.com/item?id=50320995) |
| 10 | [The Duty of a Scholar](https://www.daemonology.net/blog/2026-10-31-The-Duty-of-a-Scholar.html) <sub>daemonology.net</sub> | 107 | [31](https://news.ycombinator.com/item?id=50319061) |
<!-- digest:end -->
