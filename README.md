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
### Latest: [2026-11-12](archive/2026/11/2026-11-12.md)

Top 10 of 30 stories so far, last updated 2026-11-12 00:48 UTC. **14** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [My AI agents found an unmapped Maya site](https://pietromiotti.com/latest/maya-site) <sub>pietromiotti.com</sub> | 918 | [335](https://news.ycombinator.com/item?id=50452455) |
| 2 | [Tim Peters has died](https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028) <sub>discuss.python.org</sub> | 817 | [86](https://news.ycombinator.com/item?id=50450488) |
| 3 | [AWS emulator](https://github.com/aws/aws-emulator) <sub>github.com</sub> | 630 | [209](https://news.ycombinator.com/item?id=50456631) |
| 4 | [A false smoke alarm almost drowned Jane Street's only NYC datacenter](https://michael.bacarella.com/2026/11/10/false-smoke-alarm-jane-street-datacenter/) <sub>michael.bacarella.com</sub> | 396 | [196](https://news.ycombinator.com/item?id=50455394) |
| 5 | [Nvidia is preparing to oust Jensen Huang](https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad) <sub>wsj.com</sub> | 367 | [364](https://news.ycombinator.com/item?id=50459703) |
| 6 | [United Airlines bans AI agents from booking flights on behalf of travelers](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/) <sub>cbsnews.com</sub> | 315 | [292](https://news.ycombinator.com/item?id=50458900) |
| 7 | [Hyper-Realistic Sand with WebGL2](https://av.github.io/safe-sand/) <sub>av.github.io</sub> | 294 | [62](https://news.ycombinator.com/item?id=50453288) |
| 8 | [Using voltage glitching to unleash the A100 in my mining card](https://blog.kate.land/posts/using-voltage-glitching-to-unlock-the-a100/) <sub>blog.kate.land</sub> | 257 | [104](https://news.ycombinator.com/item?id=50451903) |
| 9 | [Gemini Decisions API](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/) <sub>blog.google</sub> | 242 | [76](https://news.ycombinator.com/item?id=50456791) |
| 10 | [Can a Linear Program Do Weight-Space Programming?](https://nathan.rs/posts/weight-space-lp/) <sub>nathan.rs</sub> | 236 | [35](https://news.ycombinator.com/item?id=50452655) |
<!-- digest:end -->
