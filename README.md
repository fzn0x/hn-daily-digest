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

Top 10 of 53 stories so far, last updated 2026-11-04 17:22 UTC. **6** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Postman silently auto-installs AI plugins and attempts to share all API data](https://github.com/postmanlabs/postman-app-support/issues/14370) <sub>github.com</sub> | 1167 | [383](https://news.ycombinator.com/item?id=50354960) |
| 2 | [The 'Astra can read and write weights to improve Qwen' post is misleading](https://honnibal.dev/blog/astra-read-write-misleading) <sub>honnibal.dev</sub> | 951 | [197](https://news.ycombinator.com/item?id=50351111) |
| 3 | [Stringman, an $800 open-source room scale gripper robot](https://neufangled.com/) <sub>neufangled.com</sub> | 734 | [226](https://news.ycombinator.com/item?id=50354358) |
| 4 | [Jailbreaking my car's navigation system just so I can change the time](https://blog.nns.ee/2026/11/02/renault-hack/) <sub>blog.nns.ee</sub> | 721 | [295](https://news.ycombinator.com/item?id=50339288) |
| 5 | [AI is forcing us to pay off 40 years of technical debt](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability) <sub>spectrum.ieee.org</sub> | 645 | [415](https://news.ycombinator.com/item?id=50364336) |
| 6 | [Qwen 3.8 27B on my laptop can interpret model weights, too](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) <sub>simonwillison.net</sub> | 564 | [172](https://news.ycombinator.com/item?id=50355251) |
| 7 | [Tell HN: Gemini trains on chat history, even for subscribers (personal accounts)](https://news.ycombinator.com/item?id=50363461) <sub>news.ycombinator.com</sub> | 437 | [119](https://news.ycombinator.com/item?id=50363461) |
| 8 | [Fujifilm to boost tape production 5x as AI fuels archiving demand](https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/) <sub>arstechnica.com</sub> | 435 | [181](https://news.ycombinator.com/item?id=50336918) |
| 9 | [Nvidia RTX Spark encrypted firmware slows inference speed to 35% on Linux](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop) <sub>mindstudio.ai</sub> | 430 | [193](https://news.ycombinator.com/item?id=50362905) |
| 10 | [Show HN: HackerTV – HN's most-recommended Youtube videos as 24/7 TV channels](https://hackertv.org) <sub>hackertv.org</sub> | 418 | [78](https://news.ycombinator.com/item?id=50346755) |
<!-- digest:end -->
