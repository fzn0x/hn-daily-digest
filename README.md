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
### Latest: [2026-11-28](archive/2026/11/2026-11-28.md)

Top 10 of 51 stories so far, last updated 2026-11-28 17:36 UTC. **30** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Farewell](https://github.com/p-e-w/heretic/issues/601) <sub>github.com</sub> | 794 | [330](https://news.ycombinator.com/item?id=50676672) |
| 2 | [Claude sabotaging ML research tasks?](https://twitter.com/RealAstropulse/status/2126119408997466389) <sub>twitter.com</sub> | 678 | [307](https://news.ycombinator.com/item?id=50664325) |
| 3 | [Credit card skimming scripts using WebRTC found on popular shopping sites](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) <sub>infohawk.com</sub> | 584 | [323](https://news.ycombinator.com/item?id=50668145) |
| 4 | [Google's DeepCrossAttention achieves comparable model quality up to 3x faster](https://research.google/blog/supercharging-transformer-residual-connections/) <sub>research.google</sub> | 535 | [184](https://news.ycombinator.com/item?id=50672565) |
| 5 | [Claude Code sabotage: preliminary benchmarking](https://xinyadu.github.io/blog/claude-code-sabotage.html) <sub>xinyadu.github.io</sub> | 523 | [171](https://news.ycombinator.com/item?id=50676390) |
| 6 | [The Balatro Timeline](https://localthunk.com/blog/balatro-timeline-3aarh) <sub>localthunk.com</sub> | 507 | [148](https://news.ycombinator.com/item?id=50657346) |
| 7 | [GPT 6.2 Astra Solves a Historical Mystery](https://generativehistory.substack.com/p/gpt-62-astra-solves-a-historical) <sub>generativehistory.substack.com</sub> | 503 | [318](https://news.ycombinator.com/item?id=50643158) |
| 8 | [Unkernel: Real Linux kernel, compiled to WebAssembly](https://unkernel.dev) <sub>unkernel.dev</sub> | 503 | [134](https://news.ycombinator.com/item?id=50674218) |
| 9 | [Michael Nielsen took down his book on neural nets](https://neuralnetworksanddeeplearning.com/) <sub>neuralnetworksanddeeplearning.com</sub> | 498 | [306](https://news.ycombinator.com/item?id=50670757) |
| 10 | [Audible removes download option for purchased audiobooks](https://consumerrights.wiki/w/Audible_removes_download_option_for_purchased_audiobooks) <sub>consumerrights.wiki</sub> | 486 | [201](https://news.ycombinator.com/item?id=50676723) |
<!-- digest:end -->
