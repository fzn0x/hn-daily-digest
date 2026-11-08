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

Top 10 of 30 stories so far, last updated 2026-11-08 00:36 UTC. **10** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Need for Speed Underground 2 online in the browser](https://nfsu2.xyz/) <sub>nfsu2.xyz</sub> | 783 | [223](https://news.ycombinator.com/item?id=50403052) |
| 2 | [Every Mac comes with an (undocumented) family member classifier](https://8rank.ai/game/apple-intelligence-personal-knowledge-graph) <sub>8rank.ai</sub> | 582 | [333](https://news.ycombinator.com/item?id=50403097) |
| 3 | [The end of Microsoft Research's AI Frontiers group](https://hunch.net/?p=13764006) <sub>hunch.net</sub> | 343 | [198](https://news.ycombinator.com/item?id=50406563) |
| 4 | [Apple’s grey list: Words and phrases your iPhone won’t help you spell](https://www.theguardian.com/technology/2026/nov/06/struggling-to-spell-male-chauvinist-pig-apple-grey-list-means-your-iphone-wont-help-you) <sub>theguardian.com</sub> | 331 | [224](https://news.ycombinator.com/item?id=50406111) |
| 5 | [Asahi Linux Progress Linux 7.3](https://asahilinux.org/2026/11/progress-report-7-3/) <sub>asahilinux.org</sub> | 309 | [253](https://news.ycombinator.com/item?id=50401867) |
| 6 | [What I run on my $10 USD OpenStick homelab](https://blog.bosscher.ch/posts/openstick/) <sub>blog.bosscher.ch</sub> | 304 | [75](https://news.ycombinator.com/item?id=50406670) |
| 7 | [Running a law firm on Free software](https://decoded.legal/blog/2026/11/running-a-law-firm-on-free-software-2026-edition/) <sub>decoded.legal</sub> | 229 | [108](https://news.ycombinator.com/item?id=50403066) |
| 8 | [A barbarian tribe's mythic origin story is true, ancient DNA reveals](https://www.science.org/content/article/barbarian-tribe-s-mythic-origin-story-true-ancient-dna-reveals) <sub>science.org</sub> | 206 | [184](https://news.ycombinator.com/item?id=50401740) |
| 9 | [Every Windows 11 app should kill Electron, and Discord just showed why](https://www.windowslatest.com/2026/11/06/every-windows-11-app-should-kill-electron-and-discord-just-showed-why-no-starting-screen-and-70-less-ram-even-with-two-accounts-signed-in/) <sub>windowslatest.com</sub> | 199 | [196](https://news.ycombinator.com/item?id=50403507) |
| 10 | [The $8 Linux Computer (2022)](http://thelittleengineerthatcould.blogspot.com/2022/12/the-8-linux-computer.html) <sub>thelittleengineerthatcould.blogspot.com</sub> | 192 | [84](https://news.ycombinator.com/item?id=50404599) |
<!-- digest:end -->
