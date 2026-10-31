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
### Latest: [2026-10-31](archive/2026/10/2026-10-31.md)

Top 10 of 76 stories so far, last updated 2026-10-31 21:37 UTC. **2** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Backdoor in Claude Code for VS Code extension on the Cursor Marketplace](https://phorion.io/blog/offical-claude-code-vsx-compromise/) <sub>phorion.io</sub> | 948 | [542](https://news.ycombinator.com/item?id=50300683) |
| 2 | [Serbia just elected the world's brainiest parliament](https://www.science.org/content/article/serbia-just-elected-world-s-brainiest-parliament) <sub>science.org</sub> | 760 | [439](https://news.ycombinator.com/item?id=50314654) |
| 3 | [The $6.3B Binance hack was pulled off in just 20 minutes](https://www.wired.com/story/the-dollar63-billion-binance-hack-was-pulled-off-in-just-20-minutes/) <sub>wired.com</sub> | 542 | [387](https://news.ycombinator.com/item?id=50303172) |
| 4 | [AI isn't replacing SREs, it's deskilling them](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling) <sub>newsletter.signoz.io</sub> | 498 | [372](https://news.ycombinator.com/item?id=50305693) |
| 5 | [Northflank Breached](https://status.northflank.com) <sub>status.northflank.com</sub> | 464 | [343](https://news.ycombinator.com/item?id=50305025) |
| 6 | [Florilegium: Procedural Flowers in LaTeX](https://github.com/kevinraymond/florilegium) <sub>github.com</sub> | 355 | [51](https://news.ycombinator.com/item?id=50305637) |
| 7 | [My favourite PowerMac is a Nintendo Wii](https://virtuallyfun.com/2026/10/29/my-favourite-powermac-is-a-nintendo-wii/) <sub>virtuallyfun.com</sub> | 352 | [107](https://news.ycombinator.com/item?id=50307190) |
| 8 | [Tell HN: Scribd Breached](https://news.ycombinator.com/item?id=50312756) <sub>news.ycombinator.com</sub> | 311 | [112](https://news.ycombinator.com/item?id=50312756) |
| 9 | [Azure's Weakest Link – Five Full Cross-Tenant Compromises](https://www.binarysecurity.no/posts/2026/10/one-root-case) <sub>binarysecurity.no</sub> | 310 | [58](https://news.ycombinator.com/item?id=50301854) |
| 10 | [Breaking the open web won't stop the bad bots](https://www.techpolicy.press/breaking-the-open-web-wont-stop-the-bad-bots/) <sub>techpolicy.press</sub> | 308 | [133](https://news.ycombinator.com/item?id=50263837) |
<!-- digest:end -->
