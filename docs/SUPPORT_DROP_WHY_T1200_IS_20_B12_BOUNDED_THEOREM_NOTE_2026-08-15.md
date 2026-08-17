---
claim_id: support_drop_why_t1200_is_20_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "A lex-first shortest path to (12,0,0) under the named support-drop hop-cost on B_12(0) is named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_why_t1200_is_20_b12_2026_08_15.py
---

# Lex-First Shortest Path To (12,0,0) On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_12(0)`,
restricted to naming a lex-first shortest walk from `0` to `(12,0,0)` and
the first site of that walk with `|v|_1 > 8`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_why_t1200_is_20_b12_2026_08_15.py`](../scripts/support_drop_why_t1200_is_20_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_12(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not
claimed.

One origin Dijkstra on `B_12(0)` (2625 sites) gives `t(12,0,0) = 20`. Among
all walks of that cost, the lexicographically first sequence of sites is

`(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (5,-1,0) → (6,-1,0) → (7,-1,0) → (8,-1,0) → (9,-1,0) → (10,-1,0) → (11,-1,0) → (11,0,0) → (12,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3` and running
costs `3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17, 20` summing to `20`.
The first site with `|v|_1 > 8` is `(8,-1,0)`, where `|v|_1 = 9`. The hop
that first leaves `B_8(0)` is therefore `(7,-1,0) → (8,-1,0)`. The integer
`20` is not leftover of the arrival number.

The only in-ball neighbor of `(12,0,0)` is `(11,0,0)`, so the last hop is
the both-weights-`1` axis step of cost `3`. The site `(12,-1,0)` lies
outside `B_12(0)`.

The rule is displayed, not adopted. Do not write `ν` into Admissibility.
Do not attach L1.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Lattice supplies the six-neighbor graph and the ball. Admissibility supplies
none of the hop costs. The integers `3` and `1`, the support-size clauses,
and the arrival function `t` are separately displayed mathematical inputs.
No axiom text is edited.

## Named Rule

Let `B_12(0) = { v ∈ Z^3 : |v|_1 ≤ 12 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_12(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph.

A walk is lex-first among shortest walks when its sequence of sites is
the least tuple of integer triples, compared coordinatewise, among all
walks of cost `t(12,0,0)`.

## Theorem 1 — Lex-First Shortest Walk To (12,0,0)

On `B_12(0)` the computed arrival is `t(12,0,0) = 20`. The lex-first walk
of that cost is the fifteen-site walk recorded above. The fourteen
hop-costs are seed-exit `3`, eleven support-preserving cost-`1` steps
along the line `y = -1` from `(0,-1,0)` to `(11,-1,0)`, a support-drop
`3` from `(11,-1,0)` onto `(11,0,0)`, and a final both-weights-`1` axis
step `3` from `(11,0,0)` onto `(12,0,0)`. The running costs after each
hop are `3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17, 20`.

The same cost is realized by later walks that stay in the positive
half-space, for example

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (7,1,0) → (8,1,0) → (9,1,0) → (10,1,0) → (11,1,0) → (11,0,0) → (12,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3`. That walk is
also shortest, but `(0,-1,0)` precedes `(1,0,0)`, so it is not lex-first.

This names a path. It is not leftover of the arrival number.

## Theorem 2 — First Site With `|v|_1 > 8`

On the lex-first walk every site through `(7,-1,0)` has `|v|_1 ≤ 8`. The
next site is `(8,-1,0)` with `|v|_1 = 9 > 8`. That is the first site of
the walk outside `B_8(0)`. Displayed, not adopted. The walk does not stay
in `B_8`.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_12(0)`. Do not write `ν`
into Admissibility. Do not attach L1. The exhibited walk is one shortest
path under that displayed rule. Uniqueness is not claimed among hop-costs,
and the walk is not offered as a replacement for unit-cost first arrival.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "An exhibited lex-first shortest walk on the finite ball B_12(0) under one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_12(0) for the displayed rule ν; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ν` among hop-costs with this arrival or this walk.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_12(0)`.
- Any reuse of the integer `20` as a substitute for exhibiting the walk.
