# news-image-20261123 — Monday 23 November 2026 in one image

[![news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/c/news-image-20261123/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/meongs123/news-image-20261123/rank.svg)](https://make.fun/c/news-image-20261123/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/meongs123/news-image-20261123/reward.svg)](https://make.fun/c/news-image-20261123/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A make.fun bounty entry: a newspaper front page summing up the world's news
of **Monday 23 November 2026** — 44 stories, 7 regions, 13 drawn
illustrations, a dotted world map with numbered pins, one-line briefs, and a
DATE CHECK box naming the stories that are *not* 23 November news.

## The image

- Masthead: **Monday 23 November 2026**, with the count strip
  (44 stories · 7 regions · 13 illustrated), a numbers strip
  (258 Democrats' House seats, COP31 no deal, 720/9 India, 14 missing in
  Dymer, 24 body bags in Cikande, Nasdaq −5.28%) and a segmented region bar
  (Americas 10 · Asia 11 · Europe 9 · Africa 6 · Middle East 4 ·
  World/Global 3 · Oceania 1).
- Lead stories: **COP31 collapses with no deal in Antalya**, **Democrats win
  258 House seats** (AP/Reuters — not CNN's 259), and the **Russian corvette
  Merkury sunk at Benghazi**.
- 3 big + 10 small illustrated lead cards, a dotted world map with 13
  numbered pins, 31 numbered one-line briefs, and a red-bordered DATE CHECK
  box (Shenzhen summit, ICJ Rohingya verdict, PIF Tower hit, Senate
  war-powers vote — all Thu 19 Nov; BepiColombo Mercury arrival —
  Sat 21 Nov 18:24 UTC).
- Every picture is an original flat-vector drawing made in code. No
  photographs. Sources are tagged per story.

## Facts, frozen at build time (Mon 23 Nov ~12:00 WIB)

- Democrats: **258** seats (AP/Reuters). CNN's 259 is not used.
- Dymer: **at least 14** missing (wires split 14 vs 15); 2 bodies found.
- Cikande fire: **3 confirmed dead, dozens missing; 24 body bags
  recovered** — body bags are not deaths.
- Syria landmine: **4–5 children killed** (wires split 4 vs 5).
- The IRGC claim of 2 destroyed Patriot radars and the claim that the
  Khartoum drones launched from Bahir Dar, Ethiopia, are **attributed,
  not stated as fact**.
- Gauteng coalition: **agreed in principle; signing pending** — not signed.
- UK–EU reset: **deal agreed** — not signed.
- Friday/Saturday items (PIF Tower, Senate vote, BepiColombo, El Chapo
  Isidro capture, IG Metall announcement) are dated inside
  their decks.
- **Still developing at build time — freeze pass ~20:00 WIB Mon 23 Nov:**
  India Test day 5 (NZ 227/5 at research time — match live, no result
  claimed), Nepal–Modi talks, NATO emergency council, IG Metall Monday
  strike, Dymer and Cikande tolls, Monday markets.

## Files

- `main.ts` — the entrypoint (Node 22, stdlib only): copies `entry.png`
  to `/output/entry.png` and guards the PNG signature, the 1 MiB cap,
  the 1024×1024 size, and a byte-identical round trip.
- `entry.png` — the image (1024×1024), drawn by `compose.py`.
- `compose.py` — the deterministic renderer (PIL, no clock, no randomness,
  no network). It fails loudly instead of truncating: any headline, deck
  or brief that needs more lines than its box allows raises, and every
  illustration is audited to paint only inside its own box.
- `stories.py` — the 44-story slate with regions, fields and sources.

## Verify locally

```sh
python3 compose.py            # regenerates entry.png (deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see `LICENSE` (SPDX: MIT).
