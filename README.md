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
### Latest: [2026-11-19](archive/2026/11/2026-11-19.md)

Top 10 of 30 stories so far, last updated 2026-11-19 02:41 UTC. **21** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Unauthenticated remote code execution in Nginx](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities) <sub>wiz.io</sub> | 1168 | [516](https://news.ycombinator.com/item?id=50547374) |
| 2 | [DNS resolvers are the wrong place to fight piracy](https://techstackups.com/articles/quad9-leaves-france-dns-blocking/) <sub>techstackups.com</sub> | 611 | [226](https://news.ycombinator.com/item?id=50545958) |
| 3 | [Inside Deutsche Bank](https://www.inside-db.com/) <sub>inside-db.com</sub> | 567 | [190](https://news.ycombinator.com/item?id=50547620) |
| 4 | [Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/) <sub>blog.google</sub> | 496 | [459](https://news.ycombinator.com/item?id=50552424) |
| 5 | [Seven new models at scalable price-performance](https://microsoft.ai/news/microsoft-ignite-2026/) <sub>microsoft.ai</sub> | 458 | [321](https://news.ycombinator.com/item?id=50548021) |
| 6 | [AI agents ask better questions than KPMG accountants in audit trial](https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/) <sub>europeanbusinessmagazine.com</sub> | 372 | [165](https://news.ycombinator.com/item?id=50547777) |
| 7 | [We need smart people who give a shit](https://violetpixel.com/blog/2026-11-17-we-need-smart-people-who-give-a-shit/) <sub>violetpixel.com</sub> | 251 | [132](https://news.ycombinator.com/item?id=50554045) |
| 8 | [The Cambridge Dictionary has named ‘human’ as the Word of the Year 2026](https://www.cam.ac.uk/news/cambridge-dictionary-reveals-word-of-the-year-2026) <sub>cam.ac.uk</sub> | 242 | [173](https://news.ycombinator.com/item?id=50546914) |
| 9 | [Genie 4 is now available](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/) <sub>blog.google</sub> | 198 | [143](https://news.ycombinator.com/item?id=50550415) |
| 10 | [Show HN: ExitPath – Open-source ways out of Slack, Notion and Microsoft 365](https://exitpath-ruddy.vercel.app/) <sub>exitpath-ruddy.vercel.app</sub> | 172 | [50](https://news.ycombinator.com/item?id=50547980) |
<!-- digest:end -->
