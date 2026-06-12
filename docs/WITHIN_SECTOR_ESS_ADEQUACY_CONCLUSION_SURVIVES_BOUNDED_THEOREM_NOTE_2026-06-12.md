# Under Effective-Sample-Size Adequacy the Within-Sector Conclusion Survives Where Testable — and One Seed Drops Out Entirely: 16/24 Sectors Adequate, Record Below Null on Both Surviving Seeds (Bounded)

**Date:** 2026-06-12
**Type:** bounded theorem (the ESS refinement of the within-sector note, in review — cross-referenced, not graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_within_sector_ess_adequacy_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_within_sector_ess_adequacy_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=15 FAIL=0` — the pinned landed machinery.

## Findings

Born weights make raw sector counts overstate power: with `ESS = (Σw)²/Σw²` and the
adequacy threshold `ESS ≥ 8`, **16/24 sectors survive** (seeds 4242 and 99: 8/8 each;
**seed 7: 0/8** — its depth-stable event sits on a 16-branch row, so the comparison is
**untested there**, stated plainly). On both testable seeds the weighted-mean
moment-relation deviation stays below the permutation null p95 (`0.205 < 0.300`,
`0.071 < 0.312`): the predecessor's power-limited-consistency conclusion **survives the
stricter adequacy filter where it can be tested at all**.

## Scope

One moment relation, ESS-adequate `k = 3` sectors, finite power; Born cap inherited.
No new axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
