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
### Latest: [2026-11-21](archive/2026/11/2026-11-21.md)

Top 10 of 30 stories so far, last updated 2026-11-21 02:20 UTC. **23** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Levent Alpöge claims proof of the Generalized Riemann Hypothesis \[pdf\]](https://alpo.ge/remark.pdf) <sub>alpo.ge</sub> | 2384 | [1610](https://news.ycombinator.com/item?id=50574968) |
| 2 | [Hurried Announcement: Alessandro Masullo GRH](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/) <sub>math216.wordpress.com</sub> | 1598 | [725](https://news.ycombinator.com/item?id=50579568) |
| 3 | [Inkling 2 Mini](https://thinkingmachines.ai/news/inkling-2-mini/) <sub>thinkingmachines.ai</sub> | 698 | [115](https://news.ycombinator.com/item?id=50581260) |
| 4 | [If you can't explain something in simple terms, you don't understand it (2017)](https://kottke.org/17/06/if-you-cant-explain-something-in-simple-terms-you-dont-understand-it) <sub>kottke.org</sub> | 630 | [293](https://news.ycombinator.com/item?id=50572355) |
| 5 | [Restricting AI agents in mobile operating systems platforms from capturing data](https://signal.org/blog/protecting-your-privacy/) <sub>signal.org</sub> | 512 | [306](https://news.ycombinator.com/item?id=50572348) |
| 6 | [Unforced Navier-Stokes Singularity and the Generalized Riemann Hypothesis](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/) <sub>terrytao.wordpress.com</sub> | 350 | [142](https://news.ycombinator.com/item?id=50578358) |
| 7 | [Language Models Can Rewrite Their Own Weights](https://arxiv.org/abs/2611.21885) <sub>arxiv.org</sub> | 343 | [112](https://news.ycombinator.com/item?id=50577265) |
| 8 | [We promoted developers into architects without informing them](https://manidoraisamy.com/developer-to-architect.html) <sub>manidoraisamy.com</sub> | 310 | [188](https://news.ycombinator.com/item?id=50579331) |
| 9 | [Finite-time blow-up for the Navier–Stokes equations](https://github.com/tristanbuckmaster/navier-stokes/) <sub>github.com</sub> | 260 | [82](https://news.ycombinator.com/item?id=50576232) |
| 10 | [Show HN: I made an audio-to-MIDI model 60x more efficient](https://kobi.music/research/dettato) <sub>kobi.music</sub> | 243 | [51](https://news.ycombinator.com/item?id=50526023) |
<!-- digest:end -->
