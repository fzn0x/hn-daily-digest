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

Top 10 of 51 stories so far, last updated 2026-11-25 19:16 UTC. **27** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [The matrix multiplication exponent is nine fourths \[pdf\]](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) <sub>github.com</sub> | 926 | [522](https://news.ycombinator.com/item?id=50637220) |
| 2 | [Button Sounds – collection of professionally-recorded button clicks and presses](https://buttons.joshwcomeau.com/) <sub>buttons.joshwcomeau.com</sub> | 753 | [120](https://news.ycombinator.com/item?id=50638032) |
| 3 | [Ternary Bonsai 2.5 27B](https://prismml.com/news/bonsai-2-5-27b) <sub>prismml.com</sub> | 518 | [171](https://news.ycombinator.com/item?id=50633922) |
| 4 | [The Spray Bottle](https://mechanical-pencil.com/products/spray-bottle) <sub>mechanical-pencil.com</sub> | 467 | [108](https://news.ycombinator.com/item?id=50598555) |
| 5 | [Models Can Communicate via Inference Servers Despite Being Sandboxed](https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being) <sub>lesswrong.com</sub> | 408 | [175](https://news.ycombinator.com/item?id=50637686) |
| 6 | [Bypassing iOS Safari's 60 FPS Limit to Build Web Applications That Feel Native](https://rida.dev/blog/bypassing-ios-safari-60-fps-limit) <sub>rida.dev</sub> | 397 | [132](https://news.ycombinator.com/item?id=50637890) |
| 7 | [1Password Security Incident](https://1password.com/blog/update-on-nov-2026-security-incident) <sub>1password.com</sub> | 385 | [168](https://news.ycombinator.com/item?id=50644817) |
| 8 | [GTA 6 Running on Windows](https://twitter.com/raul_bs3/status/2125213756238291075) <sub>twitter.com</sub> | 376 | [462](https://news.ycombinator.com/item?id=50627783) |
| 9 | [Google releases Cogentic papers on integer factorization, discrete logs and more](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) <sub>github.com</sub> | 346 | [265](https://news.ycombinator.com/item?id=50642086) |
| 10 | [A few questions for the guy who went snorkeling in a Home Depot retention pond](https://www.vox.com/down-to-earth/511999/home-depot-retention-pond-snorkel-joseph-ricketts) <sub>vox.com</sub> | 326 | [84](https://news.ycombinator.com/item?id=50643129) |
<!-- digest:end -->
