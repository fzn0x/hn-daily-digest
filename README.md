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

Top 10 of 30 stories so far, last updated 2026-11-04 06:30 UTC. **6** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Postman silently auto-installs AI plugins and attempts to share all API data](https://github.com/postmanlabs/postman-app-support/issues/14370) <sub>github.com</sub> | 1167 | [383](https://news.ycombinator.com/item?id=50354960) |
| 2 | [The 'Astra can read and write weights to improve Qwen' post is misleading](https://honnibal.dev/blog/astra-read-write-misleading) <sub>honnibal.dev</sub> | 951 | [197](https://news.ycombinator.com/item?id=50351111) |
| 3 | [Jailbreaking my car's navigation system just so I can change the time](https://blog.nns.ee/2026/11/02/renault-hack/) <sub>blog.nns.ee</sub> | 721 | [295](https://news.ycombinator.com/item?id=50339288) |
| 4 | [Qwen 3.8 27B on my laptop can interpret model weights, too](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) <sub>simonwillison.net</sub> | 564 | [172](https://news.ycombinator.com/item?id=50355251) |
| 5 | [Stringman, an $800 open-source room scale gripper robot](https://neufangled.com/) <sub>neufangled.com</sub> | 497 | [173](https://news.ycombinator.com/item?id=50354358) |
| 6 | [Fujifilm to boost tape production 5x as AI fuels archiving demand](https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/) <sub>arstechnica.com</sub> | 435 | [181](https://news.ycombinator.com/item?id=50336918) |
| 7 | [Safari introduces Adaptive Dark Mode in 27.3](https://webkit.org/blog/18541/introducing-adaptive-dark-mode/) <sub>webkit.org</sub> | 382 | [209](https://news.ycombinator.com/item?id=50358562) |
| 8 | [Mac at any scale](https://namespace.so/blog/mac-at-any-scale) <sub>namespace.so</sub> | 357 | [202](https://news.ycombinator.com/item?id=50352758) |
| 9 | [The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer](https://arxiv.org/abs/2605.29713) <sub>arxiv.org</sub> | 300 | [49](https://news.ycombinator.com/item?id=50358582) |
| 10 | [Show HN: HackerTV – HN's most-recommended Youtube videos as 24/7 TV channels](https://hackertv.org) <sub>hackertv.org</sub> | 268 | [54](https://news.ycombinator.com/item?id=50346755) |
<!-- digest:end -->
