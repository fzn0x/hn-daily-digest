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
### Latest: [2026-11-05](archive/2026/11/2026-11-05.md)

Top 10 of 70 stories so far, last updated 2026-11-05 23:46 UTC. **7** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [sshole](https://sshhole.com) <sub>sshhole.com</sub> | 2221 | [557](https://news.ycombinator.com/item?id=50378228) |
| 2 | [AI is forcing us to pay off 40 years of technical debt](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability) <sub>spectrum.ieee.org</sub> | 1147 | [666](https://news.ycombinator.com/item?id=50364336) |
| 3 | [Residential proxies detected on White House network](https://layer3intel.com/blog/residential-proxies-white-house-network) <sub>layer3intel.com</sub> | 910 | [276](https://news.ycombinator.com/item?id=50371246) |
| 4 | [Alpine Linux Security Advisory: OpenSSH-server password authentication bypass](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/) <sub>alpinelinux.org</sub> | 549 | [114](https://news.ycombinator.com/item?id=50379704) |
| 5 | [Kimi K3.1 Pro model weights are out](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) <sub>huggingface.co</sub> | 472 | [134](https://news.ycombinator.com/item?id=50366999) |
| 6 | [Search for everyone](https://kagi.com/changelog#11820) <sub>kagi.com</sub> | 411 | [207](https://news.ycombinator.com/item?id=50383740) |
| 7 | [Motorola Signature 27 with GrapheneOS support](https://motorolanews.com/motorola-signature-27-2/) <sub>motorolanews.com</sub> | 376 | [281](https://news.ycombinator.com/item?id=50380810) |
| 8 | [Lemmings CSS Animation](https://markblah.github.io/lemmings/) <sub>markblah.github.io</sub> | 345 | [69](https://news.ycombinator.com/item?id=50375354) |
| 9 | [Goodbye from Salon](https://www.salon.com/2026/11/05/goodbye-from-salon/) <sub>salon.com</sub> | 343 | [119](https://news.ycombinator.com/item?id=50383739) |
| 10 | [Guerrilla bike lanes: San Francisco makes illicit infrastructure permanent (2016)](https://99percentinvisible.org/article/guerrilla-bike-lanes-san-francisco-makes-illicit-infrastructure-permanent/) <sub>99percentinvisible.org</sub> | 284 | [206](https://news.ycombinator.com/item?id=50366522) |
<!-- digest:end -->
