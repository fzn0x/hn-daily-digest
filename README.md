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
### Latest: [2026-11-22](archive/2026/11/2026-11-22.md)

Top 10 of 65 stories so far, last updated 2026-11-22 19:40 UTC. **24** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Hurried Announcement: Alessandro Masullo GRH](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/) <sub>math216.wordpress.com</sub> | 2424 | [1178](https://news.ycombinator.com/item?id=50579568) |
| 2 | [Inkling 2 Mini](https://thinkingmachines.ai/news/inkling-2-mini/) <sub>thinkingmachines.ai</sub> | 1383 | [280](https://news.ycombinator.com/item?id=50581260) |
| 3 | [Pill to treat pancreatic cancer hailed as 'biggest breakthrough in decades'](https://www.theguardian.com/society/2026/nov/20/pill-pancreatic-cancer-breakthrough-daraxonrasib) <sub>theguardian.com</sub> | 1293 | [276](https://news.ycombinator.com/item?id=50582069) |
| 4 | [Lean verification of the Riemann Hypothesis](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) <sub>leanprover-community.github.io</sub> | 1189 | [984](https://news.ycombinator.com/item?id=50589618) |
| 5 | [Toyota, Nissan, and Honda to standardize parts to lower costs](https://www.caranddriver.com/news/a74490092/toyota-nissan-honda-standardize-parts-lower-costs/) <sub>caranddriver.com</sub> | 1040 | [620](https://news.ycombinator.com/item?id=50596133) |
| 6 | [Brazil's tax authority open-sources its tax calculator on GitHub under MIT](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/novembro/receita-federal-publica-primeiro-codigo-fonte-aberto-no-github-e-amplia-transparencia-da-reforma-tributaria) <sub>gov.br</sub> | 744 | [238](https://news.ycombinator.com/item?id=50532613) |
| 7 | [87% of the Anthropic power will come from gas and 11% from coal in 2028](https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/) <sub>betterdatacenterproject.com</sub> | 651 | [713](https://news.ycombinator.com/item?id=50597612) |
| 8 | [Detonating a pile of lead azide](https://www.science.org/content/blog-post/detonating-huge-pile-lead-azide-really) <sub>science.org</sub> | 622 | [391](https://news.ycombinator.com/item?id=50588982) |
| 9 | [Ask HN: I have been unemployed for 2y. 15 years of experience, US. What to do?](https://news.ycombinator.com/item?id=50583761) <sub>news.ycombinator.com</sub> | 609 | [678](https://news.ycombinator.com/item?id=50583761) |
| 10 | [My monitor was cutting my download speed by 75%](https://blog.tymscar.com/posts/studiodisplayethernet/) <sub>blog.tymscar.com</sub> | 594 | [277](https://news.ycombinator.com/item?id=50587875) |
<!-- digest:end -->
