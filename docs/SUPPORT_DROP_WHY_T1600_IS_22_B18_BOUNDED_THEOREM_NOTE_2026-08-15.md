---
claim_id: support_drop_why_t1600_is_22_b18_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "A lex-first shortest path to (16,0,0) under the named support-drop hop-cost on B_18(0) is named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_why_t1600_is_22_b18_2026_08_15.py
---

# Lex-First Shortest Path To (16,0,0) On B_18(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_18(0)`,
restricted to naming a lex-first shortest walk from `0` to `(16,0,0)` and
the first site on that walk with `|v|_1 > 16`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_why_t1600_is_22_b18_2026_08_15.py`](../scripts/support_drop_why_t1600_is_22_b18_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The same named support-drop hop-cost `ν` already scored on `B_16(0)` is
scored independently on `B_18(0)`. The ball is not leftover of the two
times: one origin Dijkstra is run on this ball, and a lex-first shortest
path is named.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_18(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not
claimed.

One origin Dijkstra on `B_18(0)` (8473 sites; 8472 nonzero) gives
`t(16,0,0) = 22`. Among all walks of that cost, the lexicographically first
sequence of sites is

`(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (5,-1,0) → (6,-1,0) → (7,-1,0) → (8,-1,0) → (9,-1,0) → (10,-1,0) → (11,-1,0) → (12,-1,0) → (13,-1,0) → (14,-1,0) → (15,-1,0) → (16,-1,0) → (16,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3` and
running costs `3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22`
summing to `22`.

The first site on that path with `|v|_1 > 16` is `(16,-1,0)`, which has
ℓ¹ norm `17`. It is reached by the support-preserving hop
`(15,-1,0) → (16,-1,0)` of cost `1`. The path does not stay in `B_16`.
The next hop is the support-drop `(16,-1,0) → (16,0,0)` of cost `3`.

On `B_16(0)` the site `(16,-1,0)` is absent. A displayed axis-parallel
comparison walk that stays in `B_16(0)` is

`(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (5,-1,0) → (6,-1,0) → (7,-1,0) → (8,-1,0) → (9,-1,0) → (10,-1,0) → (11,-1,0) → (12,-1,0) → (13,-1,0) → (14,-1,0) → (15,-1,0) → (15,0,0) → (16,0,0)`,

with hop-costs `3` then fifteen cost-`1` steps then support-drop `3` then
both-weights-`1` cost `3`, summing to `24`. That walk is displayed, not
adopted, and is not a second Dijkstra. The pair of integers `24` and `22`
is not the claim: the claim is the named path and the first site that
leaves `B_16`.

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

Let `B_18(0) = { v ∈ Z^3 : |v|_1 ≤ 18 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_18(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph.

A walk is lex-first among shortest walks when its sequence of sites is
the least tuple of integer triples, compared coordinatewise, among all
walks of cost `t(16,0,0)`.

The axis-skeleton comparator `α` uses only the first two clauses of `ν`.
On the support-drop hop `(16,-1,0) → (16,0,0)` one has `|σ| : 2 → 1`, so
`α = 1` while `ν = 3`. Therefore `α` cannot price support drop, and the
`ν` scores below are not a leftover of `α`.

## Theorem 1 — Arrival `t(16,0,0)` And A Lex-First Shortest Path

On `B_18(0)` the computed arrival is `t(16,0,0) = 22`. The lex-first walk
of that cost is the nineteen-site walk recorded above. The eighteen
hop-costs are seed-exit `3` from `(0,0,0)` onto `(0,-1,0)`, one
support-increase cost-`1` step `(0,-1,0) → (1,-1,0)`, fifteen
support-preserving cost-`1` steps along the line `y = -1` from
`(1,-1,0)` to `(16,-1,0)`, and a final support-drop `3` from
`(16,-1,0)` onto `(16,0,0)`. The running costs after each hop are
`3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22`.

The same cost is realized by later walks that stay in the positive
half-space, for example

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (7,1,0) → (8,1,0) → (9,1,0) → (10,1,0) → (11,1,0) → (12,1,0) → (13,1,0) → (14,1,0) → (15,1,0) → (16,1,0) → (16,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3`. That
walk is also shortest, but `(0,-1,0)` precedes `(1,0,0)`, so it is not
lex-first.

This names a path. It is not leftover of the two times.

## Theorem 2 — First Site With `|v|_1 > 16`

On the lex-first walk the first site with `|v|_1 > 16` is `(16,-1,0)`,
with ℓ¹ norm `17`. Every earlier site has ℓ¹ norm at most `16`. The
leaving hop is `(15,-1,0) → (16,-1,0)`. The path does not stay in
`B_16`. Displayed, not adopted.

The integer `22` is therefore not the `B_16(0)` axis arrival `24`. The
extra site `(16,-1,0)` is available only because the ball is `B_18(0)`.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_18(0)`. Do not write `ν`
into Admissibility. Do not attach L1. The exhibited walk is one shortest
path under that displayed rule. Uniqueness is not claimed among hop-costs,
and the walk is not offered as a replacement for unit-cost first arrival.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "An exhibited lex-first shortest walk on the finite ball B_18(0) under one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_18(0) for the displayed rule ν; no Admissibility edit; not attached to L1"
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
- Any statement off `B_18(0)`.
- Any reuse of the integers `22` and `24` as a substitute for exhibiting
  the walk.
- Any second Dijkstra on `B_16(0)`.
