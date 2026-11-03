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

Top 10 of 30 stories so far, last updated 2026-11-03 06:56 UTC. **5** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Astra can read and write weights to improve Qwen](https://rikiyat.github.io/blog/weight-space-programming/) <sub>rikiyat.github.io</sub> | 2370 | [741](https://news.ycombinator.com/item?id=50341174) |
| 2 | [WTF Ubuntu?](https://chalmovsky.com/posts/wtf-ubuntu) <sub>chalmovsky.com</sub> | 1428 | [606](https://news.ycombinator.com/item?id=50337608) |
| 3 | [Show HN: Subvocal – Talk to your computer without making noise](https://news.ycombinator.com/item?id=50340088) <sub>news.ycombinator.com</sub> | 640 | [326](https://news.ycombinator.com/item?id=50340088) |
| 4 | [If you love a website, back it up](https://blog.mistys-internet.website/post/2026/10/29/if-you-love-a-website-back-it-up/) <sub>blog.mistys-internet.website</sub> | 485 | [108](https://news.ycombinator.com/item?id=50336518) |
| 5 | [Ubuntu still has not released patch for Linux 0day RCE in almost 3 weeks](https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432) <sub>freenode.net</sub> | 425 | [125](https://news.ycombinator.com/item?id=50341462) |
| 6 | [US boy names that became girl names and vice versa](https://namedaisy.com/blog/boy-names-that-became-girl-names) <sub>namedaisy.com</sub> | 346 | [343](https://news.ycombinator.com/item?id=50339397) |
| 7 | [The SEC Should Block Anthropic's IPO to Protect the Public](https://www.techpolicy.press/the-sec-should-block-anthropics-ipo-to-protect-the-public/) <sub>techpolicy.press</sub> | 290 | [226](https://news.ycombinator.com/item?id=50344919) |
| 8 | [Show HN: Warsaw in voxels – An interactive 3D map of the city centre](https://p.migdal.pl/warsaw-vibe-voxel/) <sub>p.migdal.pl</sub> | 243 | [40](https://news.ycombinator.com/item?id=50339221) |
| 9 | [Ask HN: Who is hiring? (November 2026)](https://news.ycombinator.com/item?id=50338728) <sub>news.ycombinator.com</sub> | 203 | [163](https://news.ycombinator.com/item?id=50338728) |
| 10 | [Intel stock collapse worsens as $3.5T chip rout spreads](https://finance.yahoo.com/markets/article/the-intel-stock-collapse-is-getting-worse--and-the-37-trillion-chip-rout-is-spreading-212154947.html) <sub>finance.yahoo.com</sub> | 182 | [129](https://news.ycombinator.com/item?id=50346153) |
<!-- digest:end -->
