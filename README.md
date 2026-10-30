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
### Latest: [2026-10-30](archive/2026/10/2026-10-30.md)

Top 10 of 30, captured 2026-10-30 20:42 UTC. **1** day archived so far.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Backdoor in Claude Code for VS Code extension on the Cursor Marketplace](https://phorion.io/blog/offical-claude-code-vsx-compromise/) <sub>phorion.io</sub> | 614 | [411](https://news.ycombinator.com/item?id=50300683) |
| 2 | [AI isn't replacing SREs, it's deskilling them](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling) <sub>newsletter.signoz.io</sub> | 388 | [297](https://news.ycombinator.com/item?id=50305693) |
| 3 | [Northflank Breached](https://status.northflank.com) <sub>status.northflank.com</sub> | 266 | [183](https://news.ycombinator.com/item?id=50305025) |
| 4 | [Azure's Weakest Link – Five Full Cross-Tenant Compromises](https://www.binarysecurity.no/posts/2026/10/one-root-case) <sub>binarysecurity.no</sub> | 230 | [40](https://news.ycombinator.com/item?id=50301854) |
| 5 | [Anthropic may not secure investment-grade rating after IPO, Blackstone says](https://www.ft.com/content/59383c7f-8d82-493f-bf01-d2e862a1018f) <sub>ft.com</sub> | 178 | [123](https://news.ycombinator.com/item?id=50307219) |
| 6 | [The federated code forge](https://tangled.org/blog/forge/) <sub>tangled.org</sub> | 161 | [58](https://news.ycombinator.com/item?id=50305573) |
| 7 | [Blockchain intelligence firms link North Korea to $6.3B hack on Binance](https://www.npr.org/2026/10/30/g-s1-150902/blockchain-intelligence-firms-link-north-korea-to-6-3b-hack-on-binance) <sub>npr.org</sub> | 155 | [99](https://news.ycombinator.com/item?id=50305480) |
| 8 | [My favourite PowerMac is a Nintendo Wii](https://virtuallyfun.com/2026/10/29/my-favourite-powermac-is-a-nintendo-wii/) <sub>virtuallyfun.com</sub> | 144 | [34](https://news.ycombinator.com/item?id=50307190) |
| 9 | [Florilegium: Procedural Flowers in LaTeX](https://github.com/kevinraymond/florilegium) <sub>github.com</sub> | 144 | [25](https://news.ycombinator.com/item?id=50305637) |
| 10 | [Show HN: A working Nintendo in ~1GB of Qwen weights](https://github.com/dbreunig/nesformer) <sub>github.com</sub> | 129 | [93](https://news.ycombinator.com/item?id=50306442) |
<!-- digest:end -->
