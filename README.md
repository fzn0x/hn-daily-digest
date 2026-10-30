# hn-daily-digest

A daily archive of the [Hacker News](https://news.ycombinator.com) front page.

Once a day a GitHub Actions job takes a snapshot of the front page, sorts the stories by points, and saves it as:

- `archive/YYYY/MM/YYYY-MM-DD.md`: a readable table of the day's stories
- `archive/YYYY/MM/YYYY-MM-DD.json`: the same data, ready for analysis

It uses the public [Algolia HN API](https://hn.algolia.com/api), falls back to the [official Firebase API](https://github.com/HackerNews/API), and has no dependencies beyond the Python standard library.

## Run it locally

```sh
python scripts/digest.py
```

<!-- digest:start -->
<!-- digest:end -->
