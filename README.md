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
### Latest: [2026-11-06](archive/2026/11/2026-11-06.md)

Top 10 of 51 stories so far, last updated 2026-11-06 16:47 UTC. **8** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [sshole](https://sshhole.com) <sub>sshhole.com</sub> | 2873 | [700](https://news.ycombinator.com/item?id=50378228) |
| 2 | [Claude Code sends your email address to websites](https://github.com/anthropics/claude-code/issues/107757) <sub>github.com</sub> | 1455 | [453](https://news.ycombinator.com/item?id=50385272) |
| 3 | [MS Paint Remote Code Execution Vulnerability](https://www.cve.org/CVERecord?id=CVE-2026-83844) <sub>cve.org</sub> | 660 | [248](https://news.ycombinator.com/item?id=50384233) |
| 4 | [Search for everyone](https://kagi.com/changelog#11820) <sub>kagi.com</sub> | 630 | [326](https://news.ycombinator.com/item?id=50383740) |
| 5 | [Goodbye from Salon](https://www.salon.com/2026/11/05/goodbye-from-salon/) <sub>salon.com</sub> | 542 | [200](https://news.ycombinator.com/item?id=50383739) |
| 6 | [Dutch 'idealist' bank ASN blocks non-Google Android, including GrapheneOS](https://github.com/PrivSec-dev/banking-apps-compat-report/issues/105) <sub>github.com</sub> | 505 | [306](https://news.ycombinator.com/item?id=50390124) |
| 7 | [Blender's UI and Runtime: Much Faster Than GPUI](https://github.com/ppmpreetham/BUI) <sub>github.com</sub> | 505 | [202](https://news.ycombinator.com/item?id=50389333) |
| 8 | [Britain to make salary disclosure in job ads mandatory](https://www.reuters.com/business/world-at-work/britain-make-salary-disclosure-job-ads-mandatory-2026-11-05/) <sub>reuters.com</sub> | 480 | [376](https://news.ycombinator.com/item?id=50389222) |
| 9 | [Motorola Signature 27 with GrapheneOS support](https://motorolanews.com/motorola-signature-27-2/) <sub>motorolanews.com</sub> | 446 | [325](https://news.ycombinator.com/item?id=50380810) |
| 10 | [Window Sweaters](https://github.com/saragordic/window-sweaters) <sub>github.com</sub> | 423 | [125](https://news.ycombinator.com/item?id=50381383) |
<!-- digest:end -->
