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

Top 10 of 42 stories so far, last updated 2026-11-12 11:17 UTC. **14** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Tim Peters has died](https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028) <sub>discuss.python.org</sub> | 1234 | [135](https://news.ycombinator.com/item?id=50450488) |
| 2 | [Nvidia is preparing to oust Jensen Huang](https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad) <sub>wsj.com</sub> | 1060 | [1419](https://news.ycombinator.com/item?id=50459703) |
| 3 | [My AI agents found an unmapped Maya site?](https://pietromiotti.com/latest/maya-site) <sub>pietromiotti.com</sub> | 995 | [365](https://news.ycombinator.com/item?id=50452455) |
| 4 | [AWS emulator](https://github.com/aws/aws-emulator) <sub>github.com</sub> | 862 | [237](https://news.ycombinator.com/item?id=50456631) |
| 5 | [United Airlines bans AI agents from booking flights on behalf of travelers](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/) <sub>cbsnews.com</sub> | 563 | [565](https://news.ycombinator.com/item?id=50458900) |
| 6 | [A false smoke alarm almost drowned Jane Street's only NYC datacenter](https://michael.bacarella.com/2026/11/10/false-smoke-alarm-jane-street-datacenter/) <sub>michael.bacarella.com</sub> | 499 | [238](https://news.ycombinator.com/item?id=50455394) |
| 7 | [93% of paint splatters are valid Perl programs (2019)](https://www.mcmillen.dev/sigbovik/) <sub>mcmillen.dev</sub> | 449 | [58](https://news.ycombinator.com/item?id=50459745) |
| 8 | [Gemini Decisions API](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/) <sub>blog.google</sub> | 444 | [135](https://news.ycombinator.com/item?id=50456791) |
| 9 | [Hyper-Realistic Sand with WebGL2](https://av.github.io/safe-sand/) <sub>av.github.io</sub> | 391 | [74](https://news.ycombinator.com/item?id=50453288) |
| 10 | [Using voltage glitching to unleash the A100 in my mining card](https://blog.kate.land/posts/using-voltage-glitching-to-unlock-the-a100/) <sub>blog.kate.land</sub> | 309 | [123](https://news.ycombinator.com/item?id=50451903) |
<!-- digest:end -->
