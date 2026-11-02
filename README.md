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
### Latest: [2026-11-02](archive/2026/11/2026-11-02.md)

Top 10 of 40 stories so far, last updated 2026-11-02 11:12 UTC. **4** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [HackerTube: YouTube built from videos recommended by HN](https://karpathy.bearblog.dev/hacker-tube/) <sub>karpathy.bearblog.dev</sub> | 2603 | [573](https://news.ycombinator.com/item?id=50319510) |
| 2 | [Show HN: HackerBooks – HackerTube, but for books mentioned on HN](https://hackerbooks.org) <sub>hackerbooks.org</sub> | 1422 | [237](https://news.ycombinator.com/item?id=50326821) |
| 3 | [An Italian farmer found some unknown seeds in his attic and planted them](https://www.smithsonianmag.com/science-nature/italian-farmer-found-unknown-seeds-attic-with-nothing-lose-planted-them-result-biblical-180989644/) <sub>smithsonianmag.com</sub> | 829 | [211](https://news.ycombinator.com/item?id=50320963) |
| 4 | [Lenovo's 'encrypted' fingerprint USB is just an unencrypted SD card in a case](https://www.reddit.com/r/technology/comments/1xl2pr3/lenovos_encrypted_fingerprint_usb_drive_is_just/) <sub>reddit.com</sub> | 497 | [166](https://news.ycombinator.com/item?id=50326099) |
| 5 | [Postgres 19 is late because so many more bugs are being found now](http://rhaas.blogspot.com/2026/10/postgres-19-is-late-and-its-ais-fault.html) <sub>rhaas.blogspot.com</sub> | 494 | [308](https://news.ycombinator.com/item?id=50312408) |
| 6 | [Ask HN: Which TV do you recommend for privacy?](https://news.ycombinator.com/item?id=50328896) <sub>news.ycombinator.com</sub> | 420 | [550](https://news.ycombinator.com/item?id=50328896) |
| 7 | [The AI cost of JavaScript frameworks](https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/) <sub>nolanlawson.com</sub> | 382 | [296](https://news.ycombinator.com/item?id=50323088) |
| 8 | [Patrick Stewart taught us what good men do with power](https://www.vox.com/politics/508526/patrick-stewart-jean-luc-picard-star-trek-liberalism) <sub>vox.com</sub> | 359 | [250](https://news.ycombinator.com/item?id=50327650) |
| 9 | [Mathematics has changed. Let's act like it](https://terrytao.wordpress.com/2026/11/01/mathematics-has-changed-lets-act-like-it/) <sub>terrytao.wordpress.com</sub> | 320 | [358](https://news.ycombinator.com/item?id=50328251) |
| 10 | [OccupySaaS](https://occupysaas.com/) <sub>occupysaas.com</sub> | 299 | [170](https://news.ycombinator.com/item?id=50331402) |
<!-- digest:end -->
