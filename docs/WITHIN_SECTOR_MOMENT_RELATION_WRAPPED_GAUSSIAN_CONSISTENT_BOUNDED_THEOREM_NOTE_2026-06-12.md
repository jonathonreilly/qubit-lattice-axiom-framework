# The Within-Sector Remainder Is Consistent With One Wrapped-Normal Moment Relation Relative to the Finite Permutation Control: the Deviation Sits Below the Null p95 at Every Seed (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_within_sector_moment_relation_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_within_sector_moment_relation_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=19 FAIL=0` — the pinned landed machinery (anchor reproduced).

## Inputs and dependency boundary

This packet consumes the supplied `L = 3` depth-stable event and named-instrument
context from
[`CONDITIONAL_LAW_DEPTH_AXIS_DEPTH_STABLE_EVENT_BOUNDED_THEOREM_NOTE_2026-06-12.md`](CONDITIONAL_LAW_DEPTH_AXIS_DEPTH_STABLE_EVENT_BOUNDED_THEOREM_NOTE_2026-06-12.md)
and the record-mixture/within-sector-remainder event from
[`CENTERED_U1_FLUCTUATION_LAW_RECORD_MIXTURE_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-06-11.md`](CENTERED_U1_FLUCTUATION_LAW_RECORD_MIXTURE_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-06-11.md).
Those links supply the finite packet being characterized here; this note only tests
one centered circular-moment relation on that supplied packet.

## Findings

At each seed's depth-stable most-spread event (`k = 3` sectors, raw sector-size adequacy gated), the within-sector centered circular moments are tested against the wrapped-normal
relation `|E e^{2iθ}| = |E e^{iθ}|⁴`: the raw per-sector deviations are **sizeable**
(|δ| > 0.05 on 20/24 sectors — gated as the observed pattern), yet the
**weighted mean |deviation| sits below the sampled label-permutation null p95 at every seed**
(`0.205 < 0.297`, `0.071 < 0.312`, `0.207 < 0.289` — gated directly as the claim, per
seed). This is a **finite permutation-control consistency statement,
not evidence of Gaussianity**: one moment relation, finite power, raw sector-size
adequacy only (effective-sample-size refinements are the named follow-on).

## Scope

Fixed period `L = 3`, the depth-stable events, `k = 3` adequate sectors, one moment relation
(second vs first); power-limited (stated — finer relations and larger trees are the named
follow-ons). Born cap + named instruments inherited; trajectories are realized-state data.
No new axiom/primitive/measure/weight; `r` untouched. The audit lane grades.
