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
### Latest: [2026-11-07](archive/2026/11/2026-11-07.md)

Top 10 of 42 stories so far, last updated 2026-11-07 13:02 UTC. **9** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Tesla to wind down Cybertruck production](https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817) <sub>nbcnews.com</sub> | 1048 | [1905](https://news.ycombinator.com/item?id=50391456) |
| 2 | [Libghostty 1.0](https://mitchellh.com/writing/libghostty-1-0) <sub>mitchellh.com</sub> | 737 | [121](https://news.ycombinator.com/item?id=50399933) |
| 3 | [A Jev that can ask Opus for help gives Opus accuracy at 4x lower cost](https://hightouch.com/blog/llm-judges-identity-resolution) <sub>hightouch.com</sub> | 508 | [122](https://news.ycombinator.com/item?id=50397429) |
| 4 | [US FAA says it will phase out floppy disks from air traffic control by 2028](https://www.reuters.com/world/us/us-faa-says-it-will-phase-out-floppy-disks-air-traffic-control-by-2028-2026-11-05/) <sub>reuters.com</sub> | 356 | [288](https://news.ycombinator.com/item?id=50388001) |
| 5 | [Gemini Omni 1.2 Flash](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/) <sub>blog.google</sub> | 346 | [233](https://news.ycombinator.com/item?id=50392118) |
| 6 | [AI is dramatically accelerating AI research](https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai) <sub>planned-obsolescence.org</sub> | 331 | [293](https://news.ycombinator.com/item?id=50397994) |
| 7 | [Firecracker VM Escape: PwnEscape Part 2](https://pwn.ai/blog/firecracker-escape) <sub>pwn.ai</sub> | 254 | [110](https://news.ycombinator.com/item?id=50397219) |
| 8 | [First steps in bare-metal programming using UEFI](https://kevinboone.me/efitest_index.html) <sub>kevinboone.me</sub> | 230 | [43](https://news.ycombinator.com/item?id=50394855) |
| 9 | [Every Mac comes with an (undocumented) family member classifier](https://8rank.ai/game/apple-intelligence-personal-knowledge-graph) <sub>8rank.ai</sub> | 180 | [97](https://news.ycombinator.com/item?id=50403097) |
| 10 | [Devvm.dev: One VM for every project](https://devvm.dev/) <sub>devvm.dev</sub> | 165 | [62](https://news.ycombinator.com/item?id=50395450) |
<!-- digest:end -->
