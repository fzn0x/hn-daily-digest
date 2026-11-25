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
### Latest: [2026-11-25](archive/2026/11/2026-11-25.md)

Top 10 of 30 stories so far, last updated 2026-11-25 08:42 UTC. **27** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Matrix Multiplication is Θ(n^2.25) \[pdf\]](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) <sub>github.com</sub> | 561 | [274](https://news.ycombinator.com/item?id=50637220) |
| 2 | [The Spray Bottle](https://mechanical-pencil.com/products/spray-bottle) <sub>mechanical-pencil.com</sub> | 467 | [108](https://news.ycombinator.com/item?id=50598555) |
| 3 | [Ternary Bonsai 2.5 27B](https://prismml.com/news/bonsai-2-5-27b) <sub>prismml.com</sub> | 437 | [137](https://news.ycombinator.com/item?id=50633922) |
| 4 | [GTA 6 Running on Windows](https://twitter.com/raul_bs3/status/2125213756238291075) <sub>twitter.com</sub> | 376 | [462](https://news.ycombinator.com/item?id=50627783) |
| 5 | [Button Sounds – collection of professionally-recorded button clicks and presses](https://buttons.joshwcomeau.com/) <sub>buttons.joshwcomeau.com</sub> | 305 | [33](https://news.ycombinator.com/item?id=50638032) |
| 6 | [Active intrusion campaign against Check Point security management servers](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign) <sub>greynoise.io</sub> | 282 | [140](https://news.ycombinator.com/item?id=50630594) |
| 7 | [Ask HN: Anthropic is accusing my company of distilling. How can I prove I'm not?](https://news.ycombinator.com/item?id=50630809) <sub>news.ycombinator.com</sub> | 261 | [198](https://news.ycombinator.com/item?id=50630809) |
| 8 | [GPT-6 models demonstrate intrinsic protein-design capabilities](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) <sub>openai.com</sub> | 252 | [76](https://news.ycombinator.com/item?id=50634658) |
| 9 | [PenGPT: A Generative Transformer for Handwriting and Sketches](https://greydanus.github.io/2026/11/12/pengpt/) <sub>greydanus.github.io</sub> | 222 | [39](https://news.ycombinator.com/item?id=50637056) |
| 10 | [Models Can Communicate via Inference Servers Despite Being Sandboxed](https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being) <sub>lesswrong.com</sub> | 199 | [76](https://news.ycombinator.com/item?id=50637686) |
<!-- digest:end -->
