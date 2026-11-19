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

Top 10 of 46 stories so far, last updated 2026-11-19 11:44 UTC. **21** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Unauthenticated remote code execution in Nginx](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities) <sub>wiz.io</sub> | 1408 | [605](https://news.ycombinator.com/item?id=50547374) |
| 2 | [Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/) <sub>blog.google</sub> | 860 | [684](https://news.ycombinator.com/item?id=50552424) |
| 3 | [Inside Deutsche Bank](https://www.inside-db.com/) <sub>inside-db.com</sub> | 710 | [241](https://news.ycombinator.com/item?id=50547620) |
| 4 | [DNS resolvers are the wrong place to fight piracy](https://techstackups.com/articles/quad9-leaves-france-dns-blocking/) <sub>techstackups.com</sub> | 611 | [226](https://news.ycombinator.com/item?id=50545958) |
| 5 | [Seven new models at scalable price-performance](https://microsoft.ai/news/microsoft-ignite-2026/) <sub>microsoft.ai</sub> | 548 | [355](https://news.ycombinator.com/item?id=50548021) |
| 6 | [AI agents ask better questions than KPMG accountants in audit trial](https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/) <sub>europeanbusinessmagazine.com</sub> | 372 | [165](https://news.ycombinator.com/item?id=50547777) |
| 7 | [The Cambridge Dictionary has named ‘human’ as the Word of the Year 2026](https://www.cam.ac.uk/news/cambridge-dictionary-reveals-word-of-the-year-2026) <sub>cam.ac.uk</sub> | 281 | [214](https://news.ycombinator.com/item?id=50546914) |
| 8 | [Multiple vulnerabilities in Regexp and String case conversion](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/) <sub>ruby-lang.org</sub> | 281 | [96](https://news.ycombinator.com/item?id=50554038) |
| 9 | [Genie 4 is now available](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/) <sub>blog.google</sub> | 263 | [170](https://news.ycombinator.com/item?id=50550415) |
| 10 | [Anthropic prices initial public offering](https://www.anthropic.com/news/anthropic-prices-initial-public-offering) <sub>anthropic.com</sub> | 255 | [453](https://news.ycombinator.com/item?id=50553843) |
<!-- digest:end -->
