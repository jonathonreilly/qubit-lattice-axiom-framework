# Block 39 — refuting pass and findings (2026-09-20)

1. Exact stationary laws by linear solve (disjoint from the runner's move-by-move checks): pair-weight transit = static law with one and with two vacancies; normalized transit differs by total variation `134813/674193` (one vacancy, reversible there) and `8639049/59119982` (two vacancies, detailed balance fails).
2. Clumping on the window: `P(2×2 clump)` is `0.1195` under normalized transit at both scales (random: `0.1333`), `0.2197` and `0.3969` under pair-weight transit at weights (3,1) and (6,2).
3. Simulator against a site-by-site reference (side 8): neighbour ratios `1.470/1.442`, `1.093/1.083`, `1.891/1.842`.
4. Simulator against the literature onset for content-less records: bracketed between `2.43` and `2.7`.
5. Finding folded: expected multiplier next to two orthogonal records at the neutral scale was wrong in the draft (`23/24`); exact value `1`.
6. Caveat recorded in the note: arrest at strong preference makes the large-scale structure factor understate clumping; neighbour ratio and aligned fraction are the primary indicators.
7. Finding added after the first gate run: reflection positivity of the law with vacancies holds exactly from the neutral scale up (T5); checked symbolically and by an explicit negative form below it; a scratch numerical check of the 7×7 kernel's smallest eigenvalue agrees (−0.646 at c = 1/4, 0 at 1/2 and 1 for (3,1,2); −0.118, 0, +0.704 at c = 1/4, 2/7, 1 for (12,1,2)).
