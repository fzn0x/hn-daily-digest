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
### Latest: [2026-11-27](archive/2026/11/2026-11-27.md)

Top 10 of 30 stories so far, last updated 2026-11-27 01:54 UTC. **29** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Holy shit holy shit holy shit holy shit: The magnitude of what’s now happening](https://scottaaronson.blog/?p=10379) <sub>scottaaronson.blog</sub> | 1986 | [1814](https://news.ycombinator.com/item?id=50646108) |
| 2 | [Tell HN: Happy Thanksgiving](https://news.ycombinator.com/item?id=50655664) <sub>news.ycombinator.com</sub> | 599 | [136](https://news.ycombinator.com/item?id=50655664) |
| 3 | [Intel One Mono font (2023)](https://github.com/intel/intel-one-mono) <sub>github.com</sub> | 466 | [238](https://news.ycombinator.com/item?id=50653667) |
| 4 | [Nextcloud Office Desktop app](https://nextcloud.com/blog/euro-office-comes-to-your-desktop-with-the-nextcloud-office-desktop-app/) <sub>nextcloud.com</sub> | 398 | [203](https://news.ycombinator.com/item?id=50654289) |
| 5 | [AI made self-hosting fun again](https://janlukas.blog/posts/ai-self-hosting) <sub>janlukas.blog</sub> | 304 | [158](https://news.ycombinator.com/item?id=50660180) |
| 6 | [AMD-specific fork of llama.cpp](https://devnull.land/amd-specific-llama-cpp) <sub>devnull.land</sub> | 285 | [71](https://news.ycombinator.com/item?id=50657265) |
| 7 | [OpenAI may be in cost control mode](https://micjm.com/blog/openai-is-in-cost-control-mode/) <sub>micjm.com</sub> | 274 | [270](https://news.ycombinator.com/item?id=50652527) |
| 8 | [YouTube Ad Punisher – Auto-reloads YouTube pages when an ad plays](https://github.com/antonpictures/youtube-punisher) <sub>github.com</sub> | 268 | [335](https://news.ycombinator.com/item?id=50657530) |
| 9 | [Moat: OpenRouter replacement](https://commandcode.ai/moat) <sub>commandcode.ai</sub> | 247 | [141](https://news.ycombinator.com/item?id=50652184) |
| 10 | [Google Will Make AI Agents Use Its MCP Servers. The Gmail One Can't Send Email](https://techstackups.com/articles/google-workspace-ai-agents-mcp/) <sub>techstackups.com</sub> | 241 | [205](https://news.ycombinator.com/item?id=50653477) |
<!-- digest:end -->
