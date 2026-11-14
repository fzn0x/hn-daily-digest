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
### Latest: [2026-11-14](archive/2026/11/2026-11-14.md)

Top 10 of 75 stories so far, last updated 2026-11-14 22:27 UTC. **16** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [FAA issues national ground stop – lifted 4.5 hours later](https://www.nbcnews.com/news/us-news/faa-orders-nationwide-ground-stop-departing-flights-reasons-safety-rcna609247) <sub>nbcnews.com</sub> | 1622 | [1251](https://news.ycombinator.com/item?id=50489641) |
| 2 | [Nvidia allegedly engineered scarcity by funding AI startups to buy its GPUs](https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus) <sub>techpowerup.com</sub> | 952 | [576](https://news.ycombinator.com/item?id=50493251) |
| 3 | [Reverse engineering my Coway air purifier to ditch the cloud](https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/) <sub>scottjg.com</sub> | 751 | [213](https://news.ycombinator.com/item?id=50474959) |
| 4 | [Lovable apps expose passport details and more than 200K private messages](https://www.crissyfield.de/research/lovable-en/) <sub>crissyfield.de</sub> | 509 | [184](https://news.ycombinator.com/item?id=50499017) |
| 5 | [Why get an expensive Pi when I have an old phone?](https://so.long.thanks.fish/why-pi-when-i-have-an-old-phone/) <sub>so.long.thanks.fish</sub> | 473 | [268](https://news.ycombinator.com/item?id=50440709) |
| 6 | [Doomsday: Friday, 13 November, A.D. 2026 (1960)](https://www.science.org/doi/10.1126/science.132.3436.1291) <sub>science.org</sub> | 449 | [308](https://news.ycombinator.com/item?id=50482379) |
| 7 | [Monkey Island: all 13 versions side by side](https://monkeyisland.pages.dev/) <sub>monkeyisland.pages.dev</sub> | 445 | [141](https://news.ycombinator.com/item?id=50493904) |
| 8 | [Tech Companies Are Trying to Shift the Concept of Privacy (Again)](https://www.eff.org/deeplinks/2026/11/tech-companies-are-trying-shift-entire-concept-privacy-again) <sub>eff.org</sub> | 405 | [152](https://news.ycombinator.com/item?id=50496602) |
| 9 | [Terminal borders that don't cost a cell](https://www.joshka.net/cell-borders/) <sub>joshka.net</sub> | 384 | [165](https://news.ycombinator.com/item?id=50491423) |
| 10 | [Ggml v1.0.0](https://github.com/ggml-org/ggml/releases/tag/v1.0.0) <sub>github.com</sub> | 380 | [64](https://news.ycombinator.com/item?id=50493062) |
<!-- digest:end -->
