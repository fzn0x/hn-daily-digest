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
### Latest: [2026-11-05](archive/2026/11/2026-11-05.md)

Top 10 of 59 stories so far, last updated 2026-11-05 17:27 UTC. **7** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [sshole](https://sshhole.com) <sub>sshhole.com</sub> | 1342 | [364](https://news.ycombinator.com/item?id=50378228) |
| 2 | [AI is forcing us to pay off 40 years of technical debt](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability) <sub>spectrum.ieee.org</sub> | 1147 | [666](https://news.ycombinator.com/item?id=50364336) |
| 3 | [Residential proxies detected on White House network](https://layer3intel.com/blog/residential-proxies-white-house-network) <sub>layer3intel.com</sub> | 910 | [276](https://news.ycombinator.com/item?id=50371246) |
| 4 | [Kimi K3.1 Pro model weights are out](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) <sub>huggingface.co</sub> | 472 | [134](https://news.ycombinator.com/item?id=50366999) |
| 5 | [Lemmings CSS Animation](https://markblah.github.io/lemmings/) <sub>markblah.github.io</sub> | 345 | [69](https://news.ycombinator.com/item?id=50375354) |
| 6 | [Guerrilla bike lanes: San Francisco makes illicit infrastructure permanent (2016)](https://99percentinvisible.org/article/guerrilla-bike-lanes-san-francisco-makes-illicit-infrastructure-permanent/) <sub>99percentinvisible.org</sub> | 284 | [206](https://news.ycombinator.com/item?id=50366522) |
| 7 | [A new Go API for JSON](https://go.dev/blog/jsonv2) <sub>go.dev</sub> | 278 | [126](https://news.ycombinator.com/item?id=50369106) |
| 8 | [Ripple-65B Preview: U.S. Open-Weight SOTA on Agentic Coding](https://www.ricursive.com/ripple) <sub>ricursive.com</sub> | 274 | [99](https://news.ycombinator.com/item?id=50369925) |
| 9 | [A thousand fewer paths to root](https://openai.com/index/a-thousand-fewer-paths-to-root/) <sub>openai.com</sub> | 265 | [158](https://news.ycombinator.com/item?id=50372929) |
| 10 | [Ask HN: What's your current AI agentic setup?](https://news.ycombinator.com/item?id=50366117) <sub>news.ycombinator.com</sub> | 259 | [249](https://news.ycombinator.com/item?id=50366117) |
<!-- digest:end -->
