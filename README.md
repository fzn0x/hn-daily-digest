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
### Latest: [2026-11-10](archive/2026/11/2026-11-10.md)

Top 10 of 30 stories so far, last updated 2026-11-10 03:34 UTC. **12** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Foldable Flight: The Best Paper Airplanes](https://www.foldableflight.com) <sub>foldableflight.com</sub> | 877 | [141](https://news.ycombinator.com/item?id=50424581) |
| 2 | [USPS now offers official ZIP Code boundary polygons](https://postalpro.usps.com/zcb) <sub>postalpro.usps.com</sub> | 516 | [266](https://news.ycombinator.com/item?id=50431058) |
| 3 | [Payments Canada announces launch of Canada's Real-Time Rail (RTR) payment system](https://www.payments.ca/canada-launches-real-time-rail-bringing-247-payment-infrastructure-national-economy) <sub>payments.ca</sub> | 482 | [266](https://news.ycombinator.com/item?id=50427362) |
| 4 | [Google Gemini routes personal Drive files and emails to human annotators](https://github.com/thisisme6598/gemini_files/) <sub>github.com</sub> | 461 | [111](https://news.ycombinator.com/item?id=50429426) |
| 5 | [Claude Fable 5.2 scores 65 on Artificial Analysis, highest so far](https://artificialanalysis.ai/models/claude-fable-5-2) <sub>artificialanalysis.ai</sub> | 301 | [226](https://news.ycombinator.com/item?id=50431144) |
| 6 | [E-means: Outperforming k-means in one-tenth the epochs](https://e-means.github.io/) <sub>e-means.github.io</sub> | 295 | [22](https://news.ycombinator.com/item?id=50429734) |
| 7 | [Semi-transparent, colored cadmium telluride photovoltaic panels in agrivoltaics](https://www.anthropocenemagazine.org/2026/10/magenta-solar-panels-may-be-agrivoltaics-cleverest-trick-yet/) <sub>anthropocenemagazine.org</sub> | 286 | [185](https://news.ycombinator.com/item?id=50426175) |
| 8 | [Muse Ember: Our smallest, most efficient model](https://research.meta.ai/blog/muse-ember) <sub>research.meta.ai</sub> | 259 | [109](https://news.ycombinator.com/item?id=50429024) |
| 9 | [Claude Fable 5.2 and Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2) <sub>anthropic.com</sub> | 251 | [626](https://news.ycombinator.com/item?id=50429068) |
| 10 | [Show HN: Every satellite that passed over any place this week, and its photos](https://www.watched.earth) <sub>watched.earth</sub> | 246 | [45](https://news.ycombinator.com/item?id=50428907) |
<!-- digest:end -->
