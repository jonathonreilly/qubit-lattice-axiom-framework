# Under Effective-Sample-Size Adequacy the Within-Sector Conclusion Survives Where Testable — and One Seed Drops Out Entirely: 16/24 Sectors Adequate, Record Below Null on Both Surviving Seeds (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (the effective-sample-size refinement of the within-sector note; cross-referenced, not graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_within_sector_ess_adequacy_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_within_sector_ess_adequacy_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=15 FAIL=0` — the pinned finite machinery.

## Findings

Born weights make raw sector counts overstate power: with `ESS = (Σw)²/Σw²` and the
adequacy threshold `ESS ≥ 8`, **16/24 sectors survive** (seeds 4242 and 99: 8/8 each;
**seed 7: 0/8** — its depth-stable event sits on a 16-branch row, so the comparison is
**untested there**, stated plainly). On both testable seeds the weighted-mean
moment-relation deviation stays below the fixed seeded 300-draw permutation-null p95
diagnostic (`0.205 < 0.300`,
`0.071 < 0.312`): the predecessor's power-limited-consistency conclusion **survives the
stricter adequacy filter where it can be tested at all**.

## Scope

One moment relation, effective-sample-size-adequate `k = 3` sectors, finite
power, and the fixed seeded 300-draw null diagnostic implemented by the runner.
This is not an all-permutations null theorem. Context only:
`WITHIN_SECTOR_MOMENT_RELATION_WRAPPED_GAUSSIAN_CONSISTENT_BOUNDED_THEOREM_NOTE_2026-06-12.md`.
No new axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
