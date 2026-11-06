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
### Latest: [2026-11-06](archive/2026/11/2026-11-06.md)

Top 10 of 30 stories so far, last updated 2026-11-06 06:47 UTC. **8** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [sshole](https://sshhole.com) <sub>sshhole.com</sub> | 2542 | [621](https://news.ycombinator.com/item?id=50378228) |
| 2 | [Claude Code sends your email address to websites](https://github.com/anthropics/claude-code/issues/107757) <sub>github.com</sub> | 871 | [288](https://news.ycombinator.com/item?id=50385272) |
| 3 | [Search for everyone](https://kagi.com/changelog#11820) <sub>kagi.com</sub> | 630 | [326](https://news.ycombinator.com/item?id=50383740) |
| 4 | [Goodbye from Salon](https://www.salon.com/2026/11/05/goodbye-from-salon/) <sub>salon.com</sub> | 542 | [200](https://news.ycombinator.com/item?id=50383739) |
| 5 | [MS Paint Remote Code Execution Vulnerability](https://www.cve.org/CVERecord?id=CVE-2026-83844) <sub>cve.org</sub> | 447 | [171](https://news.ycombinator.com/item?id=50384233) |
| 6 | [Motorola Signature 27 with GrapheneOS support](https://motorolanews.com/motorola-signature-27-2/) <sub>motorolanews.com</sub> | 446 | [325](https://news.ycombinator.com/item?id=50380810) |
| 7 | [I wish tech companies knew more about me](https://rakhim.exotext.com/i-wish-tech-companies-knew-more-about-me) <sub>rakhim.exotext.com</sub> | 369 | [319](https://news.ycombinator.com/item?id=50378942) |
| 8 | [Download your favourite YouTube videos](https://criminallyvulgar.dev/you-should-absolutely-download-your-favourite-youtube-videos/) <sub>criminallyvulgar.dev</sub> | 318 | [147](https://news.ycombinator.com/item?id=50378571) |
| 9 | [Window Sweaters](https://github.com/saragordic/window-sweaters) <sub>github.com</sub> | 292 | [92](https://news.ycombinator.com/item?id=50381383) |
| 10 | [MCP Explained](https://mcp-explained.com/) <sub>mcp-explained.com</sub> | 282 | [119](https://news.ycombinator.com/item?id=50379249) |
<!-- digest:end -->
