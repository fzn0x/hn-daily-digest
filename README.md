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
### Latest: [2026-11-03](archive/2026/11/2026-11-03.md)

Top 10 of 78 stories so far, last updated 2026-11-03 23:26 UTC. **5** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Astra can read and write weights to improve Qwen](https://rikiyat.github.io/blog/weight-space-programming/) <sub>rikiyat.github.io</sub> | 2370 | [741](https://news.ycombinator.com/item?id=50341174) |
| 2 | [WTF Ubuntu?](https://chalmovsky.com/posts/wtf-ubuntu) <sub>chalmovsky.com</sub> | 1428 | [606](https://news.ycombinator.com/item?id=50337608) |
| 3 | [Postman silently auto-installs AI plugins and attempts to share all API data](https://github.com/postmanlabs/postman-app-support/issues/14370) <sub>github.com</sub> | 928 | [300](https://news.ycombinator.com/item?id=50354960) |
| 4 | [The 'Astra can read and write weights to improve Qwen' post is misleading](https://honnibal.dev/blog/astra-read-write-misleading) <sub>honnibal.dev</sub> | 860 | [189](https://news.ycombinator.com/item?id=50351111) |
| 5 | [Show HN: Subvocal – Talk to your computer without making noise](https://news.ycombinator.com/item?id=50340088) <sub>news.ycombinator.com</sub> | 640 | [326](https://news.ycombinator.com/item?id=50340088) |
| 6 | [Jailbreaking my car's navigation system just so I can change the time](https://blog.nns.ee/2026/11/02/renault-hack/) <sub>blog.nns.ee</sub> | 552 | [219](https://news.ycombinator.com/item?id=50339288) |
| 7 | [If you love a website, back it up](https://blog.mistys-internet.website/post/2026/10/29/if-you-love-a-website-back-it-up/) <sub>blog.mistys-internet.website</sub> | 485 | [108](https://news.ycombinator.com/item?id=50336518) |
| 8 | [Qwen 3.8 27B on my laptop can interpret model weights, too](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) <sub>simonwillison.net</sub> | 434 | [138](https://news.ycombinator.com/item?id=50355251) |
| 9 | [Show HN: Hacker Times, a New York Times-inspired version of Hacker News](https://hackertimes.ca/) <sub>hackertimes.ca</sub> | 429 | [131](https://news.ycombinator.com/item?id=50346981) |
| 10 | [Could a modern chess engine on a Pentium have defeated Kasparov in 1996?](https://nicholas.carlini.com/writing/2026/algorithmic-improvements-chess.html) <sub>nicholas.carlini.com</sub> | 427 | [196](https://news.ycombinator.com/item?id=50349276) |
<!-- digest:end -->
