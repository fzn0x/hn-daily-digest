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
### Latest: [2026-11-26](archive/2026/11/2026-11-26.md)

Top 10 of 50 stories so far, last updated 2026-11-26 16:57 UTC. **28** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Holy shit holy shit holy shit holy shit: The magnitude of what’s now happening](https://scottaaronson.blog/?p=10379) <sub>scottaaronson.blog</sub> | 1837 | [1679](https://news.ycombinator.com/item?id=50646108) |
| 2 | [1Password Security Incident](https://1password.com/blog/update-on-nov-2026-security-incident) <sub>1password.com</sub> | 1585 | [687](https://news.ycombinator.com/item?id=50644817) |
| 3 | [The New York Times warns photographers not to update Photoshop over AI features](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features) <sub>theverge.com</sub> | 536 | [454](https://news.ycombinator.com/item?id=50647673) |
| 4 | [Much shorter version of GRH Lean verification from Anthropic](https://github.com/lsernau/grh-lean) <sub>github.com</sub> | 512 | [327](https://news.ycombinator.com/item?id=50648050) |
| 5 | [Google releases Cogentic papers on integer factorization, discrete logs and more](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) <sub>github.com</sub> | 457 | [340](https://news.ycombinator.com/item?id=50642086) |
| 6 | [A few questions for the guy who went snorkeling in a Home Depot retention pond](https://www.vox.com/down-to-earth/511999/home-depot-retention-pond-snorkel-joseph-ricketts) <sub>vox.com</sub> | 449 | [111](https://news.ycombinator.com/item?id=50643129) |
| 7 | [GPT-6.2 Astra is the first model to beat Googlers' code golf records](https://bjin.github.io/go-codegolf-benchmark/#leaderboard) <sub>bjin.github.io</sub> | 437 | [124](https://news.ycombinator.com/item?id=50601280) |
| 8 | [Slow Ubuntu security response times](https://www.openwall.com/lists/oss-security/2026/11/25/9) <sub>openwall.com</sub> | 375 | [224](https://news.ycombinator.com/item?id=50647181) |
| 9 | [Tell HN: Lots of Ask HNs again](https://news.ycombinator.com/item?id=50649864) <sub>news.ycombinator.com</sub> | 355 | [143](https://news.ycombinator.com/item?id=50649864) |
| 10 | [Collection of preserved UI style guides](https://aresluna.org/ui-style-guides/) <sub>aresluna.org</sub> | 333 | [64](https://news.ycombinator.com/item?id=50649834) |
<!-- digest:end -->
