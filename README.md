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
### Latest: [2026-11-04](archive/2026/11/2026-11-04.md)

Top 10 of 72 stories so far, last updated 2026-11-04 23:40 UTC. **6** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Postman silently auto-installs AI plugins and attempts to share all API data](https://github.com/postmanlabs/postman-app-support/issues/14370) <sub>github.com</sub> | 1167 | [383](https://news.ycombinator.com/item?id=50354960) |
| 2 | [AI is forcing us to pay off 40 years of technical debt](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability) <sub>spectrum.ieee.org</sub> | 1008 | [607](https://news.ycombinator.com/item?id=50364336) |
| 3 | [The 'Astra can read and write weights to improve Qwen' post is misleading](https://honnibal.dev/blog/astra-read-write-misleading) <sub>honnibal.dev</sub> | 951 | [197](https://news.ycombinator.com/item?id=50351111) |
| 4 | [Stringman, an $800 open-source room scale gripper robot](https://neufangled.com/) <sub>neufangled.com</sub> | 734 | [226](https://news.ycombinator.com/item?id=50354358) |
| 5 | [Jailbreaking my car's navigation system just so I can change the time](https://blog.nns.ee/2026/11/02/renault-hack/) <sub>blog.nns.ee</sub> | 721 | [295](https://news.ycombinator.com/item?id=50339288) |
| 6 | [Tell HN: Gemini trains on chat history, even for subscribers (personal accounts)](https://news.ycombinator.com/item?id=50363461) <sub>news.ycombinator.com</sub> | 617 | [157](https://news.ycombinator.com/item?id=50363461) |
| 7 | [Nvidia RTX Spark encrypted firmware slows inference speed to 35% on Linux](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop) <sub>mindstudio.ai</sub> | 578 | [266](https://news.ycombinator.com/item?id=50362905) |
| 8 | [Qwen 3.8 27B on my laptop can interpret model weights, too](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) <sub>simonwillison.net</sub> | 564 | [172](https://news.ycombinator.com/item?id=50355251) |
| 9 | [North Korean fake job interview led to $6.3B Binance heist](https://www.theregister.com/security/2026/11/03/north-korean-fake-job-interview-led-to-63b-binance-heist/5307398) <sub>theregister.com</sub> | 557 | [342](https://news.ycombinator.com/item?id=50365755) |
| 10 | [Residential proxies detected on White House network](https://layer3intel.com/blog/residential-proxies-white-house-network) <sub>layer3intel.com</sub> | 484 | [140](https://news.ycombinator.com/item?id=50371246) |
<!-- digest:end -->
