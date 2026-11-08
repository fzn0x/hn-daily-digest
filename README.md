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
### Latest: [2026-11-08](archive/2026/11/2026-11-08.md)

Top 10 of 43 stories so far, last updated 2026-11-08 10:27 UTC. **10** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Need for Speed Underground 2 online in the browser](https://nfsu2.xyz/) <sub>nfsu2.xyz</sub> | 992 | [250](https://news.ycombinator.com/item?id=50403052) |
| 2 | [Every Mac comes with an (undocumented) family member classifier](https://8rank.ai/game/apple-intelligence-personal-knowledge-graph) <sub>8rank.ai</sub> | 733 | [385](https://news.ycombinator.com/item?id=50403097) |
| 3 | [What I run on my $10 USD OpenStick homelab](https://blog.bosscher.ch/posts/openstick/) <sub>blog.bosscher.ch</sub> | 589 | [110](https://news.ycombinator.com/item?id=50406670) |
| 4 | [Apple’s grey list: Words and phrases your iPhone won’t help you spell](https://www.theguardian.com/technology/2026/nov/06/struggling-to-spell-male-chauvinist-pig-apple-grey-list-means-your-iphone-wont-help-you) <sub>theguardian.com</sub> | 465 | [293](https://news.ycombinator.com/item?id=50406111) |
| 5 | [The end of Microsoft Research's AI Frontiers group](https://hunch.net/?p=13764006) <sub>hunch.net</sub> | 457 | [277](https://news.ycombinator.com/item?id=50406563) |
| 6 | [Claude Code's "Don't Ask Again" exposes passwords in 1,122 public GitHub files](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) <sub>apiiro.com</sub> | 397 | [273](https://news.ycombinator.com/item?id=50407882) |
| 7 | [Asahi Linux Progress Linux 7.3](https://asahilinux.org/2026/11/progress-report-7-3/) <sub>asahilinux.org</sub> | 381 | [331](https://news.ycombinator.com/item?id=50401867) |
| 8 | [Every Windows 11 app should kill Electron, and Discord just showed why](https://www.windowslatest.com/2026/11/06/every-windows-11-app-should-kill-electron-and-discord-just-showed-why-no-starting-screen-and-70-less-ram-even-with-two-accounts-signed-in/) <sub>windowslatest.com</sub> | 330 | [304](https://news.ycombinator.com/item?id=50403507) |
| 9 | [Goodbye Claude, Hello Pi](https://caleb.software/posts/claude-to-pi.html) <sub>caleb.software</sub> | 318 | [191](https://news.ycombinator.com/item?id=50410107) |
| 10 | [MaxxBench – "Nice DeepSWE score. But is it true?"](https://maxxbench.unlap.ai/research/why-maxxbench/) <sub>maxxbench.unlap.ai</sub> | 313 | [83](https://news.ycombinator.com/item?id=50406222) |
<!-- digest:end -->
