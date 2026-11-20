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

Top 10 of 77 stories so far, last updated 2026-11-20 20:20 UTC. **22** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Levent Alpöge claims proof of the Generalized Riemann Hypothesis \[pdf\]](https://alpo.ge/remark.pdf) <sub>alpo.ge</sub> | 1975 | [1327](https://news.ycombinator.com/item?id=50574968) |
| 2 | [Anthropic’s Nasdaq debut](https://www.reuters.com/business/finance/anthropics-historic-debut-put-ais-promise-peril-wall-st-test-2026-11-19/) <sub>reuters.com</sub> | 926 | [1828](https://news.ycombinator.com/item?id=50562754) |
| 3 | [Pancreatic cancer halted by virus injection in three patients](https://www.newscientist.com/article/2528235-pancreatic-cancer-halted-by-virus-injection-in-three-patients/) <sub>newscientist.com</sub> | 792 | [137](https://news.ycombinator.com/item?id=50563066) |
| 4 | [Garage Door Spam](https://blog.harrison.page/garage-door-spam/) <sub>blog.harrison.page</sub> | 762 | [318](https://news.ycombinator.com/item?id=50519231) |
| 5 | [I'll never buy Framework hardware again](https://poolp.org/posts/2026-11-20/ill-never-buy-framework-hardware-again/) <sub>poolp.org</sub> | 714 | [470](https://news.ycombinator.com/item?id=50576855) |
| 6 | [How the European Commission rolled out Matrix to more than 40k staff](https://element.io/blog/how-the-european-commission-rolled-out-matrix-to-more-than-40-000-staff/) <sub>element.io</sub> | 666 | [323](https://news.ycombinator.com/item?id=50558533) |
| 7 | [Hurried Announcement: Alessandro Masullo GRH](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/) <sub>math216.wordpress.com</sub> | 628 | [267](https://news.ycombinator.com/item?id=50579568) |
| 8 | [Frostbite: A new CPU architecture discovered, designed and verified by AI](https://architectlabs.com/blog/frostbite) <sub>architectlabs.com</sub> | 549 | [295](https://news.ycombinator.com/item?id=50572503) |
| 9 | [If you can't explain something in simple terms, you don't understand it (2017)](https://kottke.org/17/06/if-you-cant-explain-something-in-simple-terms-you-dont-understand-it) <sub>kottke.org</sub> | 531 | [268](https://news.ycombinator.com/item?id=50572355) |
| 10 | [UK government forced to admit it issued Apple a secret encryption order](https://macanorak.com/uk-government-forced-to-admit-it-issued-apple-a-secret-encryption-order/) <sub>macanorak.com</sub> | 515 | [235](https://news.ycombinator.com/item?id=50562113) |
<!-- digest:end -->
