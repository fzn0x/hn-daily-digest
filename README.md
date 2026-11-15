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
### Latest: [2026-11-15](archive/2026/11/2026-11-15.md)

Top 10 of 70 stories so far, last updated 2026-11-15 22:51 UTC. **17** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [SpaceX catches the Starship to end Flight 15](https://www.spacex.com/launches/starship-flight-15) <sub>spacex.com</sub> | 1616 | [1188](https://news.ycombinator.com/item?id=50500963) |
| 2 | [All AI-generated code should be Open Source](https://jakub.jankiewicz.org/blog/ai-code-open-source/) <sub>jakub.jankiewicz.org</sub> | 1014 | [561](https://news.ycombinator.com/item?id=50507303) |
| 3 | [Lovable apps expose passport details and more than 200K private messages](https://www.crissyfield.de/research/lovable-en/) <sub>crissyfield.de</sub> | 938 | [358](https://news.ycombinator.com/item?id=50499017) |
| 4 | [Why get an expensive Pi when I have an old phone?](https://so.long.thanks.fish/why-pi-when-i-have-an-old-phone/) <sub>so.long.thanks.fish</sub> | 600 | [318](https://news.ycombinator.com/item?id=50440709) |
| 5 | [KDE: The documentary \[video\]](https://tube.kockatoo.org/w/fFinNHfanLT7aBEb2B8y4c) <sub>tube.kockatoo.org</sub> | 539 | [122](https://news.ycombinator.com/item?id=50496976) |
| 6 | [Lutnick Pushed to Weaken Chip Rules That Overlap with His Family Business](https://www.nytimes.com/2026/11/15/us/politics/lutnick-pushed-to-weaken-chip-rules-that-overlap-with-his-family-business.html) <sub>nytimes.com</sub> | 440 | [189](https://news.ycombinator.com/item?id=50506180) |
| 7 | [Nvidia deliberately kept GPU prices high through circular financing deals](https://www.techspot.com/news/114558-nvidia-deliberately-kept-gpu-prices-high-through-circular.html) <sub>techspot.com</sub> | 401 | [198](https://news.ycombinator.com/item?id=50501631) |
| 8 | [A family tree of software job titles](https://zwischenzugs.com/2026/11/03/a-family-tree-of-software-job-titles/) <sub>zwischenzugs.com</sub> | 383 | [190](https://news.ycombinator.com/item?id=50499038) |
| 9 | [The MacBook Pro's OLED PWM problem](https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/) <sub>macanorak.com</sub> | 373 | [202](https://news.ycombinator.com/item?id=50506719) |
| 10 | [Court denies motion to dismiss DRAM price fixing case](https://litnews.ai/articles/garciaguirre-samsung-sk-hynix-micron-dram-conspiracy-suit-survives-dismissal) <sub>litnews.ai</sub> | 361 | [151](https://news.ycombinator.com/item?id=50502988) |
<!-- digest:end -->
