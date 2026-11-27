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

Top 10 of 38 stories so far, last updated 2026-11-27 12:20 UTC. **29** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Holy shit holy shit holy shit holy shit: The magnitude of what’s now happening](https://scottaaronson.blog/?p=10379) <sub>scottaaronson.blog</sub> | 1986 | [1814](https://news.ycombinator.com/item?id=50646108) |
| 2 | [1Password Security Incident](https://1password.com/blog/update-on-nov-2026-security-incident) <sub>1password.com</sub> | 1678 | [715](https://news.ycombinator.com/item?id=50644817) |
| 3 | [AI made self-hosting fun again](https://janlukas.blog/posts/ai-self-hosting) <sub>janlukas.blog</sub> | 780 | [393](https://news.ycombinator.com/item?id=50660180) |
| 4 | [Tell HN: Happy Thanksgiving](https://news.ycombinator.com/item?id=50655664) <sub>news.ycombinator.com</sub> | 699 | [153](https://news.ycombinator.com/item?id=50655664) |
| 5 | [Intel One Mono font (2023)](https://github.com/intel/intel-one-mono) <sub>github.com</sub> | 533 | [259](https://news.ycombinator.com/item?id=50653667) |
| 6 | [Nextcloud Office Desktop app](https://nextcloud.com/blog/euro-office-comes-to-your-desktop-with-the-nextcloud-office-desktop-app/) <sub>nextcloud.com</sub> | 444 | [228](https://news.ycombinator.com/item?id=50654289) |
| 7 | [YouTube Ad Punisher – Auto-reloads YouTube pages when an ad plays](https://github.com/antonpictures/youtube-punisher) <sub>github.com</sub> | 432 | [491](https://news.ycombinator.com/item?id=50657530) |
| 8 | [Company Culture = Slack Emoji ÷ √Headcount](https://lia.mg/posts/measuring-company-culture-with-slack-emoji/) <sub>lia.mg</sub> | 408 | [192](https://news.ycombinator.com/item?id=50659640) |
| 9 | [Kamil Khan Mumtaz: Pakistani architect, admired at home, almost invisible abroad](https://worksinprogress.co/issue/the-greatest-architect-youve-never-heard-of-is-in-pakistan/) <sub>worksinprogress.co</sub> | 395 | [98](https://news.ycombinator.com/item?id=50659841) |
| 10 | [Hard Drive pricing has gotten bad](https://blog.ktz.me/black-friday-hard-drive-prices-are-messed-up/) <sub>blog.ktz.me</sub> | 391 | [312](https://news.ycombinator.com/item?id=50661646) |
<!-- digest:end -->
