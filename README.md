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

Top 10 of 52 stories so far, last updated 2026-11-10 14:58 UTC. **12** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Foldable Flight: The Best Paper Airplanes](https://www.foldableflight.com) <sub>foldableflight.com</sub> | 1116 | [156](https://news.ycombinator.com/item?id=50424581) |
| 2 | [Claude Fable 5.2 and Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2) <sub>anthropic.com</sub> | 737 | [893](https://news.ycombinator.com/item?id=50429068) |
| 3 | [USPS now offers official ZIP Code boundary polygons](https://postalpro.usps.com/zcb) <sub>postalpro.usps.com</sub> | 680 | [345](https://news.ycombinator.com/item?id=50431058) |
| 4 | [Payments Canada announces launch of Canada's Real-Time Rail (RTR) payment system](https://www.payments.ca/canada-launches-real-time-rail-bringing-247-payment-infrastructure-national-economy) <sub>payments.ca</sub> | 559 | [321](https://news.ycombinator.com/item?id=50427362) |
| 5 | [Amazon saves millions by replacing Sonnet 4.6 with Strands Decider](https://strandsagents.com/blog/amazon-saves-millions-replacing-sonnet-with-strands-decider/) <sub>strandsagents.com</sub> | 474 | [173](https://news.ycombinator.com/item?id=50436640) |
| 6 | [Google Gemini routes personal Drive files and emails to human annotators](https://github.com/thisisme6598/gemini_files/) <sub>github.com</sub> | 461 | [111](https://news.ycombinator.com/item?id=50429426) |
| 7 | [E-means: Outperforming k-means in one-tenth the epochs](https://e-means.github.io/) <sub>e-means.github.io</sub> | 449 | [57](https://news.ycombinator.com/item?id=50429734) |
| 8 | [Semi-transparent, colored cadmium telluride photovoltaic panels in agrivoltaics](https://www.anthropocenemagazine.org/2026/10/magenta-solar-panels-may-be-agrivoltaics-cleverest-trick-yet/) <sub>anthropocenemagazine.org</sub> | 335 | [227](https://news.ycombinator.com/item?id=50426175) |
| 9 | [Claude Fable 5.2 scores 65 on Artificial Analysis, highest so far](https://artificialanalysis.ai/models/claude-fable-5-2) <sub>artificialanalysis.ai</sub> | 301 | [226](https://news.ycombinator.com/item?id=50431144) |
| 10 | [Muse Ember: Our smallest, most efficient model](https://research.meta.ai/blog/muse-ember) <sub>research.meta.ai</sub> | 259 | [109](https://news.ycombinator.com/item?id=50429024) |
<!-- digest:end -->
