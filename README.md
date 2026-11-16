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

Top 10 of 57 stories so far, last updated 2026-11-16 19:41 UTC. **18** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [How to make almost anything](https://pub.cba.mit.edu/863.26/site/) <sub>pub.cba.mit.edu</sub> | 767 | [128](https://news.ycombinator.com/item?id=50514470) |
| 2 | [Many of Amazon’s Black Friday and Cyber Monday “deals” offered no savings](http://groundworkcollaborative.org/news/amazons-decoy-deals-groundwork-investigation-reveals-nearly-1-in-3-black-friday-and-cyber-monday-deals-advertised-by-amazon-offered-no-savings-to-shoppers-nearly-1-in-10-w/) <sub>groundworkcollaborative.org</sub> | 635 | [388](https://news.ycombinator.com/item?id=50517488) |
| 3 | [Universal XSS in uBlock Origin from website-driven element picker](https://iter.ca/post/ubo-uxss/) <sub>iter.ca</sub> | 579 | [164](https://news.ycombinator.com/item?id=50513160) |
| 4 | [Microsoft 365 outage leads to chlorine gas poisoning of 15 hotel guests](https://www1.wdr.de/nrw/rheinland/rhein-erft-kreis/technischer-defekt-chlor-phantasialand-100.html) <sub>www1.wdr.de</sub> | 477 | [207](https://news.ycombinator.com/item?id=50509411) |
| 5 | [The MacBook Pro's OLED PWM problem](https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/) <sub>macanorak.com</sub> | 461 | [255](https://news.ycombinator.com/item?id=50506719) |
| 6 | [Claude Code and Codex reverse engineered my 1994 Jeep's ECU over a $3 Arduino \[video\]](https://www.youtube.com/watch?v=WPj3aQ-xxpI) <sub>youtube.com</sub> | 401 | [196](https://news.ycombinator.com/item?id=50463399) |
| 7 | [Qwen4-Max](https://qwen.ai/blog?id=qwen4-max) <sub>qwen.ai</sub> | 337 | [112](https://news.ycombinator.com/item?id=50513215) |
| 8 | [What is w2rt6byl5nf1opmc-a.com?](https://jack.cab/blog/siterate) <sub>jack.cab</sub> | 294 | [135](https://news.ycombinator.com/item?id=50517602) |
| 9 | [Protomaps: Self-hosting map tiles has gotten cheap and easy](https://bruceroettgers.eu/blog/protomaps/) <sub>bruceroettgers.eu</sub> | 266 | [51](https://news.ycombinator.com/item?id=50509837) |
| 10 | [The Secret ThinkPad Powerbutton Code to Bring Dead Laptops Back to Life (2007)](https://masnick.com/posts/the-secret-thinkpad-powerbutton-code-to-bring-dead-laptops-back-to-life/) <sub>masnick.com</sub> | 253 | [100](https://news.ycombinator.com/item?id=50516473) |
<!-- digest:end -->
