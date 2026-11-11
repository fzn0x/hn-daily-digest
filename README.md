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
### Latest: [2026-11-11](archive/2026/11/2026-11-11.md)

Top 10 of 56 stories so far, last updated 2026-11-11 17:10 UTC. **13** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Smart home devices should work without the internet](https://docodethatmatters.com/home-automation-overnight-success/) <sub>docodethatmatters.com</sub> | 835 | [298](https://news.ycombinator.com/item?id=50441707) |
| 2 | [.name Grandfathered](https://neil.fraser.name/news/2026/11/10/) <sub>neil.fraser.name</sub> | 756 | [169](https://news.ycombinator.com/item?id=50442736) |
| 3 | [Google SWE points 48 AI agents at NASA Lidar, finds unmapped Maya pyramid in 72h](https://pietromiotti.com/latest/maya-site/?maya) <sub>pietromiotti.com</sub> | 696 | [258](https://news.ycombinator.com/item?id=50452455) |
| 4 | [AlphaProof Code](https://deepmind.google/blog/introducing-alphaproof-code/) <sub>deepmind.google</sub> | 606 | [181](https://news.ycombinator.com/item?id=50439193) |
| 5 | [Scion is back and is going to sell a kei truck in America](https://www.theautopian.com/scion-is-back-and-its-going-to-sell-a-freaking-kei-truck-in-america/) <sub>theautopian.com</sub> | 540 | [373](https://news.ycombinator.com/item?id=50445401) |
| 6 | [AI usage generates a fragile codebase](https://evanxmerz.com/post/ai-usage-generates-a-fragile-codebase/) <sub>evanxmerz.com</sub> | 467 | [457](https://news.ycombinator.com/item?id=50438318) |
| 7 | [Apple has new Mac app coming to make running local AI models easy](https://9to5mac.com/2026/11/10/apple-has-new-mac-app-coming-to-make-running-local-ai-models-easy/) <sub>9to5mac.com</sub> | 448 | [464](https://news.ycombinator.com/item?id=50446520) |
| 8 | [Tracking Anthropic-discovered vulnerabilities](https://www.vulncheck.com/blog/anthropic-glasswing-november-update) <sub>vulncheck.com</sub> | 370 | [169](https://news.ycombinator.com/item?id=50447074) |
| 9 | [Starlink Mini 2](https://starlink.com/mini-2) <sub>starlink.com</sub> | 358 | [362](https://news.ycombinator.com/item?id=50444129) |
| 10 | [Synaptics patent claims stop work on DisplayLink drivers](https://lwn.net/SubscriberLink/1102549/acbc92e00cee3a3f/) <sub>lwn.net</sub> | 354 | [207](https://news.ycombinator.com/item?id=50443824) |
<!-- digest:end -->
