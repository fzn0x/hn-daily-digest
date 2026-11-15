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

Top 10 of 51 stories so far, last updated 2026-11-15 16:22 UTC. **17** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [SpaceX catches the Starship to end Flight 15](https://www.spacex.com/launches/starship-flight-15) <sub>spacex.com</sub> | 1456 | [981](https://news.ycombinator.com/item?id=50500963) |
| 2 | [Lovable apps expose passport details and more than 200K private messages](https://www.crissyfield.de/research/lovable-en/) <sub>crissyfield.de</sub> | 938 | [358](https://news.ycombinator.com/item?id=50499017) |
| 3 | [Why get an expensive Pi when I have an old phone?](https://so.long.thanks.fish/why-pi-when-i-have-an-old-phone/) <sub>so.long.thanks.fish</sub> | 600 | [318](https://news.ycombinator.com/item?id=50440709) |
| 4 | [KDE: The documentary \[video\]](https://tube.kockatoo.org/w/fFinNHfanLT7aBEb2B8y4c) <sub>tube.kockatoo.org</sub> | 539 | [122](https://news.ycombinator.com/item?id=50496976) |
| 5 | [Nvidia deliberately kept GPU prices high through circular financing deals](https://www.techspot.com/news/114558-nvidia-deliberately-kept-gpu-prices-high-through-circular.html) <sub>techspot.com</sub> | 401 | [198](https://news.ycombinator.com/item?id=50501631) |
| 6 | [A family tree of software job titles](https://zwischenzugs.com/2026/11/03/a-family-tree-of-software-job-titles/) <sub>zwischenzugs.com</sub> | 383 | [190](https://news.ycombinator.com/item?id=50499038) |
| 7 | [Court denies motion to dismiss DRAM price fixing case](https://litnews.ai/articles/garciaguirre-samsung-sk-hynix-micron-dram-conspiracy-suit-survives-dismissal) <sub>litnews.ai</sub> | 361 | [151](https://news.ycombinator.com/item?id=50502988) |
| 8 | [How did Woz write the Apple 1 BASIC before building the computer?](https://retrocomputing.stackexchange.com/questions/17957) <sub>retrocomputing.stackexchange.com</sub> | 271 | [142](https://news.ycombinator.com/item?id=50501594) |
| 9 | [PyPI's redesigned project pages with clearer security signals are now live](https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/) <sub>blog.pypi.org</sub> | 228 | [99](https://news.ycombinator.com/item?id=50497892) |
| 10 | [Project Zero will disclose vulnerabilities 90 days after reporting](https://projectzero.google/2026/11/disclosure-policy.html) <sub>projectzero.google</sub> | 223 | [84](https://news.ycombinator.com/item?id=50496051) |
<!-- digest:end -->
