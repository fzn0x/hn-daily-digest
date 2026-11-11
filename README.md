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

Top 10 of 30 stories so far, last updated 2026-11-11 06:22 UTC. **13** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Smart home devices should work without the internet](https://docodethatmatters.com/home-automation-overnight-success/) <sub>docodethatmatters.com</sub> | 835 | [298](https://news.ycombinator.com/item?id=50441707) |
| 2 | [.name Grandfathered](https://neil.fraser.name/news/2026/11/10/) <sub>neil.fraser.name</sub> | 756 | [169](https://news.ycombinator.com/item?id=50442736) |
| 3 | [AlphaProof Code](https://deepmind.google/blog/introducing-alphaproof-code/) <sub>deepmind.google</sub> | 606 | [181](https://news.ycombinator.com/item?id=50439193) |
| 4 | [AI usage generates a fragile codebase](https://evanxmerz.com/post/ai-usage-generates-a-fragile-codebase/) <sub>evanxmerz.com</sub> | 467 | [457](https://news.ycombinator.com/item?id=50438318) |
| 5 | [Scion is back and is going to sell a kei truck in America](https://www.theautopian.com/scion-is-back-and-its-going-to-sell-a-freaking-kei-truck-in-america/) <sub>theautopian.com</sub> | 423 | [288](https://news.ycombinator.com/item?id=50445401) |
| 6 | [Tracking Anthropic-discovered vulnerabilities](https://www.vulncheck.com/blog/anthropic-glasswing-november-update) <sub>vulncheck.com</sub> | 370 | [169](https://news.ycombinator.com/item?id=50447074) |
| 7 | [Starlink Mini 2](https://starlink.com/mini-2) <sub>starlink.com</sub> | 358 | [362](https://news.ycombinator.com/item?id=50444129) |
| 8 | [Synaptics patent claims stop work on DisplayLink drivers](https://lwn.net/SubscriberLink/1102549/acbc92e00cee3a3f/) <sub>lwn.net</sub> | 354 | [207](https://news.ycombinator.com/item?id=50443824) |
| 9 | [Val Town is winding down](https://blog.val.town/winding-down) <sub>blog.val.town</sub> | 352 | [91](https://news.ycombinator.com/item?id=50443427) |
| 10 | [Show HN: Get your coding agent off ~2019 JavaScript, onto modern web primitives](https://github.com/GoogleChrome/modern-web-guidance) <sub>github.com</sub> | 326 | [101](https://news.ycombinator.com/item?id=50443812) |
<!-- digest:end -->
