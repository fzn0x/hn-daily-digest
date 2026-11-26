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

Top 10 of 30 stories so far, last updated 2026-11-26 03:40 UTC. **28** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [1Password Security Incident](https://1password.com/blog/update-on-nov-2026-security-incident) <sub>1password.com</sub> | 1236 | [522](https://news.ycombinator.com/item?id=50644817) |
| 2 | [Holy shit holy shit holy shit holy shit: The magnitude of what’s now happening](https://scottaaronson.blog/?p=10379) <sub>scottaaronson.blog</sub> | 1016 | [866](https://news.ycombinator.com/item?id=50646108) |
| 3 | [Google releases Cogentic papers on integer factorization, discrete logs and more](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) <sub>github.com</sub> | 457 | [340](https://news.ycombinator.com/item?id=50642086) |
| 4 | [A few questions for the guy who went snorkeling in a Home Depot retention pond](https://www.vox.com/down-to-earth/511999/home-depot-retention-pond-snorkel-joseph-ricketts) <sub>vox.com</sub> | 449 | [111](https://news.ycombinator.com/item?id=50643129) |
| 5 | [Windows Loudness Equalization, reverse-engineered and ported to PipeWire](https://github.com/xoxorwr/pw-loudness-eq) <sub>github.com</sub> | 324 | [181](https://news.ycombinator.com/item?id=50641171) |
| 6 | [Much shorter version of GRH Lean verification from Anthropic](https://github.com/lsernau/grh-lean) <sub>github.com</sub> | 323 | [152](https://news.ycombinator.com/item?id=50648050) |
| 7 | [Smart people who give a shit use tools](https://www.iankduncan.com/engineering/2026-11-19-smart-people-who-give-a-shit-use-tools) <sub>iankduncan.com</sub> | 292 | [234](https://news.ycombinator.com/item?id=50639698) |
| 8 | [GPT-6.2 Astra is the first model to beat Googlers' code golf records](https://bjin.github.io/go-codegolf-benchmark/#leaderboard) <sub>bjin.github.io</sub> | 275 | [80](https://news.ycombinator.com/item?id=50601280) |
| 9 | [Jev is probably Qwen3.5-35B-A3B](https://modaic.dev/blog/latency-doesnt-lie) <sub>modaic.dev</sub> | 251 | [71](https://news.ycombinator.com/item?id=50648823) |
| 10 | [The New York Times warns photographers not to update Photoshop over AI features](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features) <sub>theverge.com</sub> | 242 | [197](https://news.ycombinator.com/item?id=50647673) |
<!-- digest:end -->
