---
claim_id: support_drop_why_t500_is_11_b16_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "A lex-first shortest path to (5,0,0) under the named support-drop hop-cost on B_16(0) is named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_why_t500_is_11_b16_2026_08_15.py
---

# Lex-First Shortest Path To (5,0,0) On B_16(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_16(0)`,
restricted to naming a lex-first shortest walk from `0` to `(5,0,0)`, the
first support-drop or seed-exit hop on that walk, and whether the walk
leaves the axis 1-skeleton.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_why_t500_is_11_b16_2026_08_15.py`](../scripts/support_drop_why_t500_is_11_b16_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_16(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not
claimed.

The same-`k` axis arrivals under this rule on `B_16(0)` are `3,6,9,10,11`
for `k=1..5`. The `k=4,5` axis times break the `3k` pattern. This note is
not leftover of the table: it names a lex-first path to `(5,0,0)`.

One origin Dijkstra on `B_16(0)` (6017 sites) gives `t(5,0,0) = 11`. Among
all walks of that cost, the lexicographically first sequence of sites is

`(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (5,-1,0) → (5,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 3` and running costs
`3, 4, 5, 6, 7, 8, 11` summing to `11`.

The first support-drop or seed-exit hop on that path is the seed-exit
`(0,0,0) → (0,-1,0)` of cost `3`. The later support-drop is
`(5,-1,0) → (5,0,0)` of cost `3`. The path leaves the axis 1-skeleton: the
first off-axis site is `(1,-1,0)`, reached by `(0,-1,0) → (1,-1,0)`.

The on-axis-only walk `(0,0,0) → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0) → (5,0,0)`
costs `15 = 3·5` and is displayed, not adopted.

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

Let `B_16(0) = { v ∈ Z^3 : |v|_1 ≤ 16 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_16(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph.

The axis 1-skeleton is the set of sites with at most one nonzero coordinate.
A walk is lex-first among shortest walks when its sequence of sites is
the least tuple of integer triples, compared coordinatewise, among all
walks of cost `t(5,0,0)`.

## Theorem 1 — Lex-First Shortest Walk To (5,0,0)

On `B_16(0)` the computed arrival is `t(5,0,0) = 11`. The lex-first walk
of that cost is the eight-site walk recorded above. The seven hop-costs
are seed-exit `3` from `(0,0,0)` onto `(0,-1,0)`, one support-increase
cost-`1` step `(0,-1,0) → (1,-1,0)`, four support-preserving cost-`1`
steps along the line `y = -1` from `(1,-1,0)` to `(5,-1,0)`, and a final
support-drop `3` from `(5,-1,0)` onto `(5,0,0)`. The running costs after
each hop are `3, 4, 5, 6, 7, 8, 11`.

The same cost is realized by later walks that stay in the positive
half-space, for example

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (5,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 3`. That walk is also shortest, but
`(0,-1,0)` precedes `(1,0,0)`, so it is not lex-first.

This names a path. It is not leftover of the table.

## Theorem 2 — First Support-Drop Or Seed-Exit Hop

On the lex-first walk the first support-drop or seed-exit hop is the
seed-exit `(0,0,0) → (0,-1,0)` of cost `3`. The only later cost-`3` hop
is the support-drop `(5,-1,0) → (5,0,0)`. Displayed, not adopted.

The path leaves the axis 1-skeleton. Every site through `(0,-1,0)` has
exactly one nonzero coordinate or is the origin. The next site `(1,-1,0)`
has two nonzero coordinates. The leaving hop is `(0,-1,0) → (1,-1,0)`.

The integer `11` is therefore not `3k` for `k=5`. The on-axis-only walk
of five both-weights-`1` continuations after the seed-exit would cost
`15`.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_16(0)`. Do not write `ν`
into Admissibility. Do not attach L1. The exhibited walk is one shortest
path under that displayed rule. Uniqueness is not claimed among hop-costs,
and the walk is not offered as a replacement for unit-cost first arrival.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "An exhibited lex-first shortest walk on the finite ball B_16(0) under one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_16(0) for the displayed rule ν; no Admissibility edit; not attached to L1"
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
- Any statement off `B_16(0)`.
- Any reuse of the integer `11` as a substitute for exhibiting the walk.
