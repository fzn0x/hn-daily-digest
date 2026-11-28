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
### Latest: [2026-11-28](archive/2026/11/2026-11-28.md)

Top 10 of 30 stories so far, last updated 2026-11-28 07:56 UTC. **30** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Claude sabotaging ML research tasks?](https://twitter.com/RealAstropulse/status/2126119408997466389) <sub>twitter.com</sub> | 678 | [307](https://news.ycombinator.com/item?id=50664325) |
| 2 | [Credit card skimming scripts using WebRTC found on popular shopping sites](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) <sub>infohawk.com</sub> | 503 | [260](https://news.ycombinator.com/item?id=50668145) |
| 3 | [Michael Nielsen took down his book on neural nets](https://neuralnetworksanddeeplearning.com/) <sub>neuralnetworksanddeeplearning.com</sub> | 498 | [306](https://news.ycombinator.com/item?id=50670757) |
| 4 | [GPT 6.2 Astra Solves a Historical Mystery](https://generativehistory.substack.com/p/gpt-62-astra-solves-a-historical) <sub>generativehistory.substack.com</sub> | 421 | [260](https://news.ycombinator.com/item?id=50643158) |
| 5 | [Show HN: bouncemarket – a live prediction market game for a bouncing ball](https://bouncemarket.minhanhday.com/) <sub>bouncemarket.minhanhday.com</sub> | 366 | [124](https://news.ycombinator.com/item?id=50667726) |
| 6 | [States sue SpaceX to stop Grok from generating child sex images, revenge porn](https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform) <sub>oag.state.va.us</sub> | 363 | [209](https://news.ycombinator.com/item?id=50670855) |
| 7 | [Google's DeepCrossAttention achieves comparable model quality up to 3x faster](https://research.google/blog/supercharging-transformer-residual-connections/) <sub>research.google</sub> | 325 | [134](https://news.ycombinator.com/item?id=50672565) |
| 8 | [Convex skills send the user's app idea to a remote server without telling them](https://github.com/convex/convex-backend-skill/issues/64) <sub>github.com</sub> | 289 | [92](https://news.ycombinator.com/item?id=50669765) |
| 9 | [The Balatro Timeline](https://localthunk.com/blog/balatro-timeline-3aarh) <sub>localthunk.com</sub> | 284 | [63](https://news.ycombinator.com/item?id=50657346) |
| 10 | [False computer-checked proofs](https://cr.yp.to/proofs/falseccp.html) <sub>cr.yp.to</sub> | 218 | [84](https://news.ycombinator.com/item?id=50667989) |
<!-- digest:end -->
