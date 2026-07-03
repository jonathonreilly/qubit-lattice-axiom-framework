# Both Wrapped-Normal Moment Relations Sit Below Their Permutation Nulls on the Two Landed Seeds and the Disclosed Probe (Real Tree Data, Anchor-Gated): the Within-Sector Consistency Extends to the Third Moment (Bounded)

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/frontier_within_sector_third_moment_2026_06_12.py`](../scripts/frontier_within_sector_third_moment_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/frontier_within_sector_third_moment_2026_06_12.txt`](../logs/runner-cache/frontier_within_sector_third_moment_2026_06_12.txt)
**Status:** source proposal; independent audit required. Runner `PASS=15 FAIL=0`.

## Dependencies

This note consumes the finite within-sector packet and mixed-event basis from:

- [`WITHIN_SECTOR_MOMENT_RELATION_WRAPPED_GAUSSIAN_CONSISTENT_BOUNDED_THEOREM_NOTE_2026-06-12.md`](WITHIN_SECTOR_MOMENT_RELATION_WRAPPED_GAUSSIAN_CONSISTENT_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- [`WITHIN_SECTOR_ESS_ADEQUACY_CONCLUSION_SURVIVES_BOUNDED_THEOREM_NOTE_2026-06-12.md`](WITHIN_SECTOR_ESS_ADEQUACY_CONCLUSION_SURVIVES_BOUNDED_THEOREM_NOTE_2026-06-12.md)
- [`WITHIN_SECTOR_K2_THREE_SEED_MIXED_EVENT_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md`](WITHIN_SECTOR_K2_THREE_SEED_MIXED_EVENT_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md)

## Provenance Guard

An earlier unlanded build used a synthetic wrapped-normal sampler in place of
the Born tree, which produced machine-zero deviations contradicting landed
values. This landed runner gates the anchor first (`0.5570/0.4694` reproduced
before any moment work) and then gates nonzero tree-data `|δ₂|` means
(`0.205/0.071/0.093`) before accepting the moment comparisons.

## Findings

On ESS-adequate `k = 3` sectors of the depth-stable events (seeds 4242, 99; the
disclosed seed-7 probe row): both `δ₂ = |z₂| − R₁⁴` and `δ₃ = |z₃| − R₁⁹` have
weighted mean `|δ|` **below their own permutation nulls on every tested basis** (two landed events + the disclosed seed-7 probe row)
(`δ₃`: `0.258 < 0.320`, `0.234 < 0.304`, `0.171 < 0.257`). The power-limited
consistency with the wrapped-normal moment family extends to the third moment,
everywhere testable.

## Scope

Two moment relations, adequate sectors, finite power, mixed-event basis (stated);
Born cap inherited. No new axiom/primitive/measure/weight; `r` untouched. The audit
lane grades.
