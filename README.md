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

Top 10 of 58 stories so far, last updated 2026-11-03 17:10 UTC. **5** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Astra can read and write weights to improve Qwen](https://rikiyat.github.io/blog/weight-space-programming/) <sub>rikiyat.github.io</sub> | 2370 | [741](https://news.ycombinator.com/item?id=50341174) |
| 2 | [WTF Ubuntu?](https://chalmovsky.com/posts/wtf-ubuntu) <sub>chalmovsky.com</sub> | 1428 | [606](https://news.ycombinator.com/item?id=50337608) |
| 3 | [The 'Astra can read and write weights to improve Qwen' post is misleading](https://honnibal.dev/blog/astra-read-write-misleading) <sub>honnibal.dev</sub> | 646 | [147](https://news.ycombinator.com/item?id=50351111) |
| 4 | [Show HN: Subvocal – Talk to your computer without making noise](https://news.ycombinator.com/item?id=50340088) <sub>news.ycombinator.com</sub> | 640 | [326](https://news.ycombinator.com/item?id=50340088) |
| 5 | [If you love a website, back it up](https://blog.mistys-internet.website/post/2026/10/29/if-you-love-a-website-back-it-up/) <sub>blog.mistys-internet.website</sub> | 485 | [108](https://news.ycombinator.com/item?id=50336518) |
| 6 | [Show HN: Hacker Times, a New York Times-inspired version of Hacker News](https://hackertimes.ca/) <sub>hackertimes.ca</sub> | 429 | [131](https://news.ycombinator.com/item?id=50346981) |
| 7 | [Ubuntu still has not released patch for Linux 0day RCE in almost 3 weeks](https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432) <sub>freenode.net</sub> | 425 | [125](https://news.ycombinator.com/item?id=50341462) |
| 8 | [US boy names that became girl names and vice versa](https://namedaisy.com/blog/boy-names-that-became-girl-names) <sub>namedaisy.com</sub> | 346 | [343](https://news.ycombinator.com/item?id=50339397) |
| 9 | [DiscImageStudio: burn visible artwork onto CDs, DVDs and Blu-ray discs](https://github.com/JiaFeiMiao-K-Cat/DiscImageStudio) <sub>github.com</sub> | 329 | [74](https://news.ycombinator.com/item?id=50346849) |
| 10 | [The SEC Should Block Anthropic's IPO to Protect the Public](https://www.techpolicy.press/the-sec-should-block-anthropics-ipo-to-protect-the-public/) <sub>techpolicy.press</sub> | 290 | [226](https://news.ycombinator.com/item?id=50344919) |
<!-- digest:end -->
