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
### Latest: [2026-11-20](archive/2026/11/2026-11-20.md)

Top 10 of 52 stories so far, last updated 2026-11-20 11:48 UTC. **22** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Anthropic’s Nasdaq debut](https://www.reuters.com/business/finance/anthropics-historic-debut-put-ais-promise-peril-wall-st-test-2026-11-19/) <sub>reuters.com</sub> | 926 | [1828](https://news.ycombinator.com/item?id=50562754) |
| 2 | [Pancreatic cancer halted by virus injection in three patients](https://www.newscientist.com/article/2528235-pancreatic-cancer-halted-by-virus-injection-in-three-patients/) <sub>newscientist.com</sub> | 792 | [137](https://news.ycombinator.com/item?id=50563066) |
| 3 | [Garage Door Spam](https://blog.harrison.page/garage-door-spam/) <sub>blog.harrison.page</sub> | 762 | [318](https://news.ycombinator.com/item?id=50519231) |
| 4 | [How the European Commission rolled out Matrix to more than 40k staff](https://element.io/blog/how-the-european-commission-rolled-out-matrix-to-more-than-40-000-staff/) <sub>element.io</sub> | 666 | [323](https://news.ycombinator.com/item?id=50558533) |
| 5 | [UK government forced to admit it issued Apple a secret encryption order](https://macanorak.com/uk-government-forced-to-admit-it-issued-apple-a-secret-encryption-order/) <sub>macanorak.com</sub> | 515 | [235](https://news.ycombinator.com/item?id=50562113) |
| 6 | [Claude solves two open problems in the physics of black holes](https://www.anthropic.com/research/claude-black-hole-physics) <sub>anthropic.com</sub> | 511 | [238](https://news.ycombinator.com/item?id=50563148) |
| 7 | [Someone reported java4shell bug in September 2026](https://github.com/openjdk/jdk/pull/32781) <sub>github.com</sub> | 374 | [96](https://news.ycombinator.com/item?id=50558906) |
| 8 | [The 98% Slot Machine: How Paid Advertising Became an Extraction Tax](https://globalcommercegraph.com/writing/the-ninety-eight-percent-slot-machine) <sub>globalcommercegraph.com</sub> | 307 | [155](https://news.ycombinator.com/item?id=50564159) |
| 9 | [How to CAD Almost Anything](https://ocw.mit.edu/courses/res-16-002-how-to-cad-almost-anything-january-iap-2024/) <sub>ocw.mit.edu</sub> | 283 | [96](https://news.ycombinator.com/item?id=50528119) |
| 10 | [What's New in PHP 8.6](https://www.php.net/releases/8.6/en.php) <sub>php.net</sub> | 276 | [127](https://news.ycombinator.com/item?id=50557870) |
<!-- digest:end -->
