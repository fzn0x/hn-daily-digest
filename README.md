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
### Latest: [2026-11-09](archive/2026/11/2026-11-09.md)

Top 10 of 58 stories so far, last updated 2026-11-09 19:57 UTC. **11** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Goodbye Claude, hello Pi](https://caleb.software/posts/claude-to-pi.html) <sub>caleb.software</sub> | 729 | [451](https://news.ycombinator.com/item?id=50410107) |
| 2 | [Goldman Sachs is pulling Claude Code from its bankers and traders](https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers) <sub>thestateofai.com</sub> | 696 | [386](https://news.ycombinator.com/item?id=50415628) |
| 3 | [Fold Epic Paper Airplanes](https://www.foldableflight.com) <sub>foldableflight.com</sub> | 661 | [119](https://news.ycombinator.com/item?id=50424581) |
| 4 | [Claude Code's "Don't Ask Again" exposes passwords in 1,122 public GitHub files](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) <sub>apiiro.com</sub> | 599 | [407](https://news.ycombinator.com/item?id=50407882) |
| 5 | [Is Opus 5.5 nerfed? Thinking patterns changed on November 3](https://twitter.com/shanemelaugh/status/2119192075505893695) <sub>twitter.com</sub> | 533 | [380](https://news.ycombinator.com/item?id=50422069) |
| 6 | [Nvidia CEO Jensen Huang's letter to staff about affair](https://nvidianews.nvidia.com/news/a-message-to-our-company) <sub>nvidianews.nvidia.com</sub> | 503 | [544](https://news.ycombinator.com/item?id=50418016) |
| 7 | [Declarative Dragging](https://declarative-dragging.github.io/) <sub>declarative-dragging.github.io</sub> | 458 | [60](https://news.ycombinator.com/item?id=50368481) |
| 8 | [Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU](https://github.com/synchopate/llama-modchip) <sub>github.com</sub> | 402 | [180](https://news.ycombinator.com/item?id=50411961) |
| 9 | [Claude Fable 5.2 and Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2) <sub>anthropic.com</sub> | 372 | [159](https://news.ycombinator.com/item?id=50429906) |
| 10 | [KetchUp – Open-source SketchUp alternative built with Rust and WebGPU](https://ketchup3d.github.io/app/) <sub>ketchup3d.github.io</sub> | 363 | [96](https://news.ycombinator.com/item?id=50418176) |
<!-- digest:end -->
