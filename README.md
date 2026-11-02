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

Top 10 of 30 stories so far, last updated 2026-11-02 00:55 UTC. **4** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [HackerTube: YouTube built from videos recommended by HN](https://karpathy.bearblog.dev/hacker-tube/) <sub>karpathy.bearblog.dev</sub> | 2258 | [538](https://news.ycombinator.com/item?id=50319510) |
| 2 | [Show HN: HackerBooks – HackerTube, but for books mentioned on HN](https://hackerbooks.org) <sub>hackerbooks.org</sub> | 882 | [172](https://news.ycombinator.com/item?id=50326821) |
| 3 | [An Italian farmer found some unknown seeds in his attic and planted them](https://www.smithsonianmag.com/science-nature/italian-farmer-found-unknown-seeds-attic-with-nothing-lose-planted-them-result-biblical-180989644/) <sub>smithsonianmag.com</sub> | 768 | [197](https://news.ycombinator.com/item?id=50320963) |
| 4 | [Lenovo's 'encrypted' fingerprint USB is just an unencrypted SD card in a case](https://www.reddit.com/r/technology/comments/1xl2pr3/lenovos_encrypted_fingerprint_usb_drive_is_just/) <sub>reddit.com</sub> | 387 | [137](https://news.ycombinator.com/item?id=50326099) |
| 5 | [Patrick Stewart taught us what good men do with power](https://www.vox.com/politics/508526/patrick-stewart-jean-luc-picard-star-trek-liberalism) <sub>vox.com</sub> | 359 | [250](https://news.ycombinator.com/item?id=50327650) |
| 6 | [The AI cost of JavaScript frameworks](https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/) <sub>nolanlawson.com</sub> | 291 | [227](https://news.ycombinator.com/item?id=50323088) |
| 7 | [Mathematics has changed. Let's act like it](https://terrytao.wordpress.com/2026/11/01/mathematics-has-changed-lets-act-like-it/) <sub>terrytao.wordpress.com</sub> | 214 | [231](https://news.ycombinator.com/item?id=50328251) |
| 8 | [U.S. workers took home their smallest share of capital since at least 1947](https://fortune.com/article/why-did-us-workers-just-take-home-smallest-share-of-capital-since-1947-lowest-ever-recorded/) <sub>fortune.com</sub> | 170 | [65](https://news.ycombinator.com/item?id=50330939) |
| 9 | [Frontier Airlines Likely Breached](https://www.reddit.com/r/frontierairlines/comments/1xl20e8/psa_email_scam/) <sub>reddit.com</sub> | 167 | [60](https://news.ycombinator.com/item?id=50327266) |
| 10 | [Show HN: Point your camera at a landscape to learn about its geology](https://outcrop.rocks/) <sub>outcrop.rocks</sub> | 150 | [37](https://news.ycombinator.com/item?id=50290533) |
<!-- digest:end -->
