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

Top 10 of 30 stories so far, last updated 2026-10-31 00:54 UTC. **2** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Backdoor in Claude Code for VS Code extension on the Cursor Marketplace](https://phorion.io/blog/offical-claude-code-vsx-compromise/) <sub>phorion.io</sub> | 757 | [472](https://news.ycombinator.com/item?id=50300683) |
| 2 | [AI isn't replacing SREs, it's deskilling them](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling) <sub>newsletter.signoz.io</sub> | 498 | [372](https://news.ycombinator.com/item?id=50305693) |
| 3 | [Northflank Breached](https://status.northflank.com) <sub>status.northflank.com</sub> | 348 | [271](https://news.ycombinator.com/item?id=50305025) |
| 4 | [Azure's Weakest Link – Five Full Cross-Tenant Compromises](https://www.binarysecurity.no/posts/2026/10/one-root-case) <sub>binarysecurity.no</sub> | 260 | [51](https://news.ycombinator.com/item?id=50301854) |
| 5 | [My favourite PowerMac is a Nintendo Wii](https://virtuallyfun.com/2026/10/29/my-favourite-powermac-is-a-nintendo-wii/) <sub>virtuallyfun.com</sub> | 229 | [61](https://news.ycombinator.com/item?id=50307190) |
| 6 | [The federated code forge](https://tangled.org/blog/forge/) <sub>tangled.org</sub> | 226 | [77](https://news.ycombinator.com/item?id=50305573) |
| 7 | [Florilegium: Procedural Flowers in LaTeX](https://github.com/kevinraymond/florilegium) <sub>github.com</sub> | 210 | [36](https://news.ycombinator.com/item?id=50305637) |
| 8 | [Bunny CDN Security Incident](https://status.bunny.net/incidents/p6gf1by9kr7m) <sub>status.bunny.net</sub> | 194 | [39](https://news.ycombinator.com/item?id=50308697) |
| 9 | [Through Captain Jean-Luc Picard, Patrick Stewart taught us the measure of a man](https://www.bostonglobe.com/2026/10/29/metro/patrick-stewart-picard-star-trek-the-next-generation/) <sub>bostonglobe.com</sub> | 186 | [105](https://news.ycombinator.com/item?id=50309647) |
| 10 | [Show HN: A working Nintendo in ~1GB of Qwen weights](https://github.com/dbreunig/nesformer) <sub>github.com</sub> | 183 | [109](https://news.ycombinator.com/item?id=50306442) |
<!-- digest:end -->
