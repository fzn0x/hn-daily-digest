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
### Latest: [2026-11-16](archive/2026/11/2026-11-16.md)

Top 10 of 30 stories so far, last updated 2026-11-16 06:34 UTC. **18** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Microsoft 365 outage leads to chlorine gas poisoning of 15 hotel guests](https://www1.wdr.de/nrw/rheinland/rhein-erft-kreis/technischer-defekt-chlor-phantasialand-100.html) <sub>www1.wdr.de</sub> | 477 | [207](https://news.ycombinator.com/item?id=50509411) |
| 2 | [The MacBook Pro's OLED PWM problem](https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/) <sub>macanorak.com</sub> | 461 | [255](https://news.ycombinator.com/item?id=50506719) |
| 3 | [Claude Code and Codex reverse engineered my 1994 Jeep's ECU over a $3 Arduino \[video\]](https://www.youtube.com/watch?v=WPj3aQ-xxpI) <sub>youtube.com</sub> | 401 | [196](https://news.ycombinator.com/item?id=50463399) |
| 4 | [Qwen4-Max](https://qwen.ai/blog?id=qwen4-max) <sub>qwen.ai</sub> | 337 | [112](https://news.ycombinator.com/item?id=50513215) |
| 5 | [Protomaps: Self-hosting map tiles has gotten cheap and easy](https://bruceroettgers.eu/blog/protomaps/) <sub>bruceroettgers.eu</sub> | 266 | [51](https://news.ycombinator.com/item?id=50509837) |
| 6 | [Old Bitly links are being hijacked](https://ransomnews.com/burger-king-tweet-bitly-link-hijack-2026/) <sub>ransomnews.com</sub> | 243 | [127](https://news.ycombinator.com/item?id=50511395) |
| 7 | [Universal XSS in uBlock Origin from website-driven element picker](https://iter.ca/post/ubo-uxss/) <sub>iter.ca</sub> | 243 | [61](https://news.ycombinator.com/item?id=50513160) |
| 8 | [Things That Turbo Pascal Is Smaller Than (2011)](https://prog21.dadgum.com/116.html) <sub>prog21.dadgum.com</sub> | 221 | [116](https://news.ycombinator.com/item?id=50506894) |
| 9 | [A short explainer on how El Niño works \[video\]](https://www.youtube.com/watch?v=7_JF3etiAv8) <sub>youtube.com</sub> | 216 | [92](https://news.ycombinator.com/item?id=50509308) |
| 10 | [Handwriting, as a Font](https://ductus.sorenblank.com) <sub>ductus.sorenblank.com</sub> | 215 | [44](https://news.ycombinator.com/item?id=50509972) |
<!-- digest:end -->
