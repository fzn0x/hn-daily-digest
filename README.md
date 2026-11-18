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
### Latest: [2026-11-18](archive/2026/11/2026-11-18.md)

Top 10 of 30 stories so far, last updated 2026-11-18 01:06 UTC. **20** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [New Evidence Shows School Phone Bans Are Gradually Improving Test Scores](https://www.nytimes.com/2026/11/17/upshot/school-phone-bans-study-scores.html) <sub>nytimes.com</sub> | 1149 | [575](https://news.ycombinator.com/item?id=50530163) |
| 2 | [GPT‑6.2 Astra and Sol](https://openai.com/index/introducing-gpt-6-2-astra-sol/) <sub>openai.com</sub> | 1064 | [679](https://news.ycombinator.com/item?id=50535230) |
| 3 | [Apple Services Down](https://developer.apple.com/system-status/) <sub>developer.apple.com</sub> | 619 | [343](https://news.ycombinator.com/item?id=50535238) |
| 4 | [Java4Shell: RCE in OpenJDK when processing Base64](https://calif.io/java4shell/) <sub>calif.io</sub> | 472 | [125](https://news.ycombinator.com/item?id=50538240) |
| 5 | [Highly classified US national security communications network goes down](https://www.cnn.com/2026/11/17/politics/highly-classified-national-security-communications-network-goes-down) <sub>cnn.com</sub> | 455 | [538](https://news.ycombinator.com/item?id=50532849) |
| 6 | [Nvidia stopped disclosing Singapore sales as revenues hit $104B](https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf) <sub>ft.com</sub> | 377 | [181](https://news.ycombinator.com/item?id=50534631) |
| 7 | [What is the best harness for each model?](https://runta.com/blog/introducing-frontierharness-eval-v1-1/) <sub>runta.com</sub> | 332 | [114](https://news.ycombinator.com/item?id=50532191) |
| 8 | [MAI Code 2 and Code 2 Flash](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/) <sub>microsoft.ai</sub> | 277 | [130](https://news.ycombinator.com/item?id=50535885) |
| 9 | [Phrack 73 Released](https://phrack.org/issues/73/introduction_md) <sub>phrack.org</sub> | 262 | [29](https://news.ycombinator.com/item?id=50535992) |
| 10 | [How the Claude Code team thinks about verification](https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/) <sub>claude.dev</sub> | 261 | [202](https://news.ycombinator.com/item?id=50529612) |
<!-- digest:end -->
