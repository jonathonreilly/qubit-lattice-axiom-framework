---
claim_id: unequal_radius_k_equals_tick_census_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On a prefix of mixed-t unequal-radius weight-4 stars, whether occupied-NN count equals lock-tick is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/unequal_radius_k_equals_tick_census_2026_08_15.py
---

# Occupied-NN Count Versus Lock-Tick On Mixed-t Unequal-Radius Stars

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** a 2000-star prefix of unread weight-4 stars with not-all-equal
occupied lock-ticks in the uneqrad three-ball box. Occupied-NN count is
compared with lock-tick on occupied slots only. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/unequal_radius_k_equals_tick_census_2026_08_15.py`](../scripts/unequal_radius_k_equals_tick_census_2026_08_15.py)

## Result Up Front

The uneqrad box is the family of unions
`U = B_{r_1}(s_1) ∪ B_{r_2}(s_2) ∪ B_{r_3}(s_3)` with distinct centers
`s_i ∈ [−2,2]^3` and radii `r_i ∈ {1,2,3}` not all equal. An unread site
`v ∉ U` with `‖v‖_∞ ≤ 4` carries a six-star occupancy `σ` and lock-ticks
`t(w) = min_i ‖w − s_i‖_1` on occupied neighbors. This note scores only
weight-4 stars whose occupied ticks are not all equal.

On each occupied neighbor `w`, write `k(w)` for the number of nearest
neighbors of `w` that lie in `U`. Compare the occupied 4-tuples `k` and `t`.

The prefix has `N_prefix = 2000` mixed-t stars and `N_eq = 27` equalities.
So `N_eq` is not 0: occupied-NN count equals lock-tick on some scored stars
and fails on the rest. The lex-first disagreement is recorded below. The
already uneqsrc breaker is a later disagreement on the same prefix. The
census is not leftover of uneqsrc (one star).

Displayed, not adopted. Do not write `k` as `t` into Admissibility. Do not attach L1.

## Current Premise Boundary

The Lattice, Qubit, Admissibility, and Record premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). This note
authors no axiom edit.

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Admissibility names a nearest-neighbor rule for the content law. It does not
name a radius triple, a seed-distance clock, or an identification of
occupied-NN count with lock-tick. Record locks one admissible possibility at
a formed site and supplies no clock field. Unread `v` has no record.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite prefix counts N_prefix and N_eq, the lex-first k versus t disagreement, and the already uneqsrc disagreement are exact listings in a declared box; no Admissibility identification of k with t is derived."
trace_class: negative_route_pruning
target_claim_id: lock_tick_from_occupied_nn_count
target_blocker_text: "occupied-NN count is not a derived lock-tick law on mixed-t unequal-radius weight-4 stars"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Keep k and t as separately displayed 4-tuples. Do not adopt k as t."
conditional_surface_status: "exact for the declared 2000-star mixed-t prefix in the uneqrad box"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Centers run over combinations of three distinct points of `[−2,2]^3` in
lexicographic order. Radii run over the 24 triples in `{1,2,3}^3` that are
not all equal. Sites `v` run over `[−4,4]^3` in lexicographic order. A star
is scored when `v ∉ U`, `wt(σ) = 4`, and the occupied 4-tuple `t` is not a
constant. The prefix is the first 2000 such stars, or the whole family if
shorter.

Directions are `(+x, −x, +y, −y, +z, −z)`. Occupied slots are the four
neighbors of `v` that lie in `U`. On those slots,

- `t_μ = min_i ‖v + e_μ − s_i‖_1`,
- `k_μ` is the occupied-NN count of that neighbor inside `U`.

Equality means `k = t` as occupied 4-tuples.

## Theorem 1 — Prefix Counts

The mixed-t family reaches the cap, so `N_prefix = 2000`. Of those stars,
`N_eq = 27` have `k = t` on the occupied slots.

The first equality is star 342:

- centers `((−2,−2,−2), (−2,−2,−1), (−2,1,1))`,
- radii `(2, 2, 1)`,
- `v = (−2,0,0)`,
- `σ = (0, 0, 1, 1, 1, 1)`,
- `k = t = (1, 2, 1, 2)`.

That coincidence is a listing, not a law. The other 1973 scored stars have
`k ≠ t`.

## Theorem 2 — `N_eq` Is Not Zero; Disagreements Recorded

Because `N_eq` is not 0, occupied-NN count equals lock-tick on a nonempty
subset of the prefix. It is not the case that the prefix has no `k = t`
star.

The lex-first disagreement is star 1:

- centers `((−2,−2,−2), (−2,−2,−1), (−2,−2,0))`,
- radii `(2, 1, 2)`,
- `v = (−3,−3,−1)`,
- `σ = (1, 0, 1, 0, 1, 1)`,
- `t = (1, 1, 2, 2)`,
- `k = (3, 3, 2, 2)`.

The already uneqsrc star is star 21 of the same prefix:

- centers `((−2,−2,−2), (−2,−2,−1), (−2,−2,1))`,
- radii `(2, 1, 3)`,
- `v = (−3,−3,−1)`,
- `σ = (1, 0, 1, 0, 1, 1)`,
- `t = (1, 1, 3, 2)`,
- `k = (3, 3, 3, 2)`.

That is the leftover uneqsrc pair `k = (3, 3, 3, 2)` versus `t = (1, 1, 3, 2)`.
The present census is not leftover of uneqsrc: it scores a 2000-star prefix,
not one star.

## Theorem 3 — Displayed, Not Adopted

The counts, the first equality, and both recorded disagreements are
displayed finite listings. Do not write `k` as `t` into Admissibility. The
27 coincidences do not promote occupied-NN count to a lock-tick rule. Do
not attach L1. No fourth ball is added. The axiom memo is unedited.

## Claim Scope

claim_scope: "On a prefix of mixed-t unequal-radius weight-4 stars, whether occupied-NN count equals lock-tick is reported. Displayed, not adopted."
