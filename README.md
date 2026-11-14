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

Top 10 of 30 stories so far, last updated 2026-11-14 01:34 UTC. **16** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [FAA issues national ground stop](https://www.nbcnews.com/news/us-news/faa-orders-nationwide-ground-stop-departing-flights-reasons-safety-rcna609247) <sub>nbcnews.com</sub> | 1297 | [786](https://news.ycombinator.com/item?id=50489641) |
| 2 | [Reverse engineering my Coway air purifier to ditch the cloud](https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/) <sub>scottjg.com</sub> | 673 | [199](https://news.ycombinator.com/item?id=50474959) |
| 3 | [Doomsday: Friday, 13 November, A.D. 2026 (1960)](https://www.science.org/doi/10.1126/science.132.3436.1291) <sub>science.org</sub> | 449 | [308](https://news.ycombinator.com/item?id=50482379) |
| 4 | [AI unlocks Gödel's notebooks, said to contain hundreds of proved theorems](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths) <sub>theguardian.com</sub> | 326 | [91](https://news.ycombinator.com/item?id=50486748) |
| 5 | [$11.4M in Nvidia hardware vanishes during shipment from CA to TX](https://www.freightwaves.com/news/11-4-million-in-nvidia-hardware-vanishes-during-shipment-from-california-to-texas) <sub>freightwaves.com</sub> | 287 | [162](https://news.ycombinator.com/item?id=50487864) |
| 6 | [It Takes 16 Clicks for a Student to Open a PowerPoint on an iPad](https://www.reddit.com/r/Teachers/comments/1xuup7a/technology_sucks_it_literally_takes_16_clicks_for/) <sub>reddit.com</sub> | 282 | [141](https://news.ycombinator.com/item?id=50487522) |
| 7 | [After 600 experiments, here's what I discovered about JEPA world models](https://haddyalchaer.com/jepa) <sub>haddyalchaer.com</sub> | 214 | [35](https://news.ycombinator.com/item?id=50487185) |
| 8 | [Live airband on all frequencies from KORS. Victoria, CA also ground stopped](https://orcasairband.com/) <sub>orcasairband.com</sub> | 188 | [45](https://news.ycombinator.com/item?id=50490593) |
| 9 | [FM-1 Workbench](https://open.m-vave.com/fm1-workbench) <sub>open.m-vave.com</sub> | 180 | [106](https://news.ycombinator.com/item?id=50488325) |
| 10 | [A technical vision for the Haskell ecosystem](https://discourse.haskell.org/t/a-technical-vision-for-the-haskell-ecosystem/15078) <sub>discourse.haskell.org</sub> | 180 | [84](https://news.ycombinator.com/item?id=50484235) |
<!-- digest:end -->
