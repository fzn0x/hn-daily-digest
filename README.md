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
### Latest: [2026-11-24](archive/2026/11/2026-11-24.md)

Top 10 of 30 stories so far, last updated 2026-11-24 02:14 UTC. **26** days archived.

| # | Story | Points | Comments |
|--:|---|--:|--:|
| 1 | [Nvidia Reinstates Jensen Huang as CEO](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html) <sub>cnbc.com</sub> | 2138 | [3173](https://news.ycombinator.com/item?id=50611576) |
| 2 | [Ladybird is now in alpha](https://ladybird.org/posts/alpha/) <sub>ladybird.org</sub> | 1460 | [337](https://news.ycombinator.com/item?id=50614249) |
| 3 | [Dario is hyping the dangers so OSS models are illegal and he stays in control](https://twitter.com/ylecun/status/2124550037912920090) <sub>twitter.com</sub> | 1185 | [663](https://news.ycombinator.com/item?id=50615308) |
| 4 | [GLM-5.4: Toward generalized coding with our first loop transformer](https://z.ai/blog/glm-5.4) <sub>z.ai</sub> | 1061 | [347](https://news.ycombinator.com/item?id=50609685) |
| 5 | [Free alternative TV network built from the Internet Archive's forgotten videos](https://spelunkr.tv) <sub>spelunkr.tv</sub> | 945 | [162](https://news.ycombinator.com/item?id=50606192) |
| 6 | [Per Arm's request, this site will be discontinued on 4 December 2026 :(](https://arm.jonpalmisc.com/) <sub>arm.jonpalmisc.com</sub> | 852 | [199](https://news.ycombinator.com/item?id=50617499) |
| 7 | [Kagi Mail (public beta)](https://blog.kagi.com/kagi-mail-public-beta) <sub>blog.kagi.com</sub> | 360 | [271](https://news.ycombinator.com/item?id=50615481) |
| 8 | [Spacecraft reaches Mercury on second-ever mission to enter its orbit](https://www.theguardian.com/science/2026/nov/20/spacecraft-mercury-second-ever-mission-orbit-bepicolombo) <sub>theguardian.com</sub> | 301 | [101](https://news.ycombinator.com/item?id=50587439) |
| 9 | [Nospeaker ─ Make your MacBook's trackpad talk using its haptic motor](https://github.com/os6/nospeaker) <sub>github.com</sub> | 281 | [163](https://news.ycombinator.com/item?id=50610318) |
| 10 | [Nespresso's project to reduce grams of coffee per capsule](https://alvinbunk.wordpress.com/2026/11/01/nespresso-project-olympus/) <sub>alvinbunk.wordpress.com</sub> | 269 | [285](https://news.ycombinator.com/item?id=50605479) |
<!-- digest:end -->
