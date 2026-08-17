---
claim_id: support_drop_t6axis_path_b8_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "A shortest 0→(6,0,0) path under the named support-drop hop-cost on B_8(0) is exhibited and sums to 12. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_t6axis_path_b8_2026_08_15.py
---

# Lex-First Shortest Axis Path To (6,0,0) On B_8(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_8(0)`,
restricted to exhibiting a lex-first shortest walk from `0` to `(6,0,0)`
and comparing the same destination on `B_6(0)`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_t6axis_path_b8_2026_08_15.py`](../scripts/support_drop_t6axis_path_b8_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside the working ball, the
displayed rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not
claimed.

One origin Dijkstra on `B_8(0)` (833 sites) gives `t(6,0,0) = 12`. Among
all walks of that cost, the lexicographically first sequence of sites is

`(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (5,-1,0) → (6,-1,0) → (6,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 3` summing to `12`. The site
`(6,-1,0)` has `|v|_1 = 7 > 6`, so the walk leaves `B_6(0)`. The arrival
`12` is therefore not leftover of the arrival number on the smaller ball.

The same destination on `B_6(0)` has `t(6,0,0) = 14`. That comparator is
displayed, not adopted.

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

Let `B_R(0) = { v ∈ Z^3 : |v|_1 ≤ R }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v` in the
working ball, `t(v)` is the least sum of `ν` along a directed path from `0`
to `v` in that graph.

A walk is lex-first among shortest walks when its sequence of sites is
the least tuple of integer triples, compared coordinatewise, among all
walks of cost `t(6,0,0)`.

## Theorem 1 — Lex-First Shortest Walk On B_8(0)

On `B_8(0)` the computed arrival is `t(6,0,0) = 12`. The lex-first walk
of that cost is the nine-site walk recorded above. The eight hop-costs are
seed-exit `3`, six support-preserving cost-`1` steps along the line
`y = -1`, and a final support-drop `3` from `(6,-1,0)` onto `(6,0,0)`.

The same cost is realized by later walks that stay in the positive
half-space, for example

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (6,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 3`. That walk is also shortest, but
`(0,-1,0)` precedes `(1,0,0)`, so it is not lex-first.

The site `(6,-1,0)` lies outside `B_6(0)`. The exhibited walk is therefore
not a walk of `B_6(0)`, and the integer `12` is not leftover of the
arrival number on the radius-`6` ball.

## Theorem 2 — The Same Destination On B_6(0)

On `B_6(0)` the site `(6,1,0)` and the site `(6,-1,0)` both have
`|v|_1 = 7`, so they are absent. The only in-ball neighbor of `(6,0,0)`
is `(5,0,0)`. One origin Dijkstra on that smaller ball gives
`t(6,0,0) = 14`. The last hop is the both-weights-`1` axis step of cost
`3`. That `14` is displayed, not adopted. It is a comparator, not a
substitute for the `B_8(0)` walk.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_8(0)`. Do not write `ν`
into Admissibility. Do not attach L1. The exhibited walk is one shortest
path under that displayed rule. Uniqueness is not claimed among hop-costs,
and the walk is not offered as a replacement for unit-cost first arrival.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "An exhibited lex-first shortest walk on the finite ball B_8(0) under one named hop-cost, with a displayed B_6(0) comparator. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_8(0) for the displayed rule ν; no Admissibility edit; not attached to L1"
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
- Any statement off `B_8(0)` except the displayed `B_6(0)` comparator
  `t(6,0,0) = 14`.
- Any reuse of the integer `12` as a substitute for exhibiting the walk.
