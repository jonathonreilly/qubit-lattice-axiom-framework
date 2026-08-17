---
claim_id: support_drop_why_samek_k7_fails_b21_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Lex-first shortest paths to (7,0,0) and (7,7,7) under the named support-drop hop-cost on B_21(0) are named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_why_samek_k7_fails_b21_2026_08_15.py
---

# Lex-First Shortest Paths To (7,0,0) And (7,7,7) On B_21(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_21(0)`,
restricted to naming a lex-first shortest walk from `0` to `(7,0,0)` and a
lex-first shortest walk from `0` to `(7,7,7)`, and displaying the same-`k`
reverse comparison at `k=7`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_why_samek_k7_fails_b21_2026_08_15.py`](../scripts/support_drop_why_samek_k7_fails_b21_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The same named support-drop hop-cost `ν` already scored on `B_21(0)` is
scored independently here by naming lex-first shortest paths to both
same-`k` sites at `k=7`. The pair of walks is not leftover of the no bit:
one origin Dijkstra is run on this ball, and the two site sequences are
named.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_21(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not claimed.

One origin Dijkstra on `B_21(0)` (13287 sites; 13286 nonzero) gives

`t(7,0,0) = 13`, `t(7,7,7) = 23`.

The site `(7,7,7)` has ℓ¹ norm `21`, so it is absent from `B_18(0)`. The
`B_21(0)` table is therefore not leftover of a smaller-ball table.

Among all walks of cost `13` from `0` to `(7,0,0)`, the lexicographically
first sequence of sites is

`(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (5,-1,0) → (6,-1,0) → (7,-1,0) → (7,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 3` and running costs
`3, 4, 5, 6, 7, 8, 9, 10, 13` summing to `13`. The last hop is the
support-drop `(7,-1,0) → (7,0,0)` of cost `3`.

Among all walks of cost `23` from `0` to `(7,7,7)`, the lexicographically
first sequence of sites is

`(0,0,0) → (0,0,1) → (0,1,1) → (0,1,2) → (0,1,3) → (0,1,4) → (0,1,5) → (0,1,6) → (0,1,7) → (0,2,7) → (0,3,7) → (0,4,7) → (0,5,7) → (0,6,7) → (0,7,7) → (1,7,7) → (2,7,7) → (3,7,7) → (4,7,7) → (5,7,7) → (6,7,7) → (7,7,7)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1`
and running costs
`3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23`
summing to `23`. That walk never uses the support-drop clause.

The displayed same-`k` comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

which is `169/49` versus `529/147`, or equivalently `507 > 529`. The
inequality does not hold. Same-`k` reverse at `k=7` is no. The comparison
is displayed, not adopted.

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

Let `B_21(0) = { v ∈ Z^3 : |v|_1 ≤ 21 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_21(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph.

A walk is lex-first among shortest walks to a named site when its sequence
of sites is the least tuple of integer triples, compared coordinatewise,
among all walks of cost `t` of that site.

The axis-skeleton comparator `α` uses only the first two clauses of `ν`.
On the support-drop hop `(7,-1,0) → (7,0,0)` one has `|σ| : 2 → 1`, so
`α = 1` while `ν = 3`. Therefore `α` cannot price support drop, and the
`ν` scores below are not a leftover of `α`.

## Theorem 1 — Arrivals And Lex-First Shortest Paths

One origin Dijkstra on `B_21(0)` returns the integer arrivals

| site | `t_ν` |
|---|---:|
| `(7,0,0)` | `13` |
| `(7,7,7)` | `23` |

Every listed site lies in `B_21(0)`. The site `(7,7,7)` has ℓ¹ norm `21`,
so it is absent from `B_18(0)`. The pair is computed on `B_21(0)`, not
copied from a smaller-ball table. These values are Dijkstra outputs, not
fitted scalars.

The lex-first walk of cost `13` to `(7,0,0)` is the ten-site walk recorded
above. The nine hop-costs are seed-exit `3` from `(0,0,0)` onto `(0,-1,0)`,
one support-increase cost-`1` step `(0,-1,0) → (1,-1,0)`, six
support-preserving cost-`1` steps along the line `y = -1` from
`(1,-1,0)` to `(7,-1,0)`, and a final support-drop `3` from
`(7,-1,0)` onto `(7,0,0)`. The running costs after each hop are
`3, 4, 5, 6, 7, 8, 9, 10, 13`.

The same axis cost is realized by later walks that stay in the positive
half-space, for example

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (7,1,0) → (7,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 3`. That walk is also shortest, but
`(0,-1,0)` precedes `(1,0,0)`, so it is not lex-first.

The lex-first walk of cost `23` to `(7,7,7)` is the twenty-two-site walk
recorded above. The twenty-one hop-costs are seed-exit `3` from `(0,0,0)`
onto `(0,0,1)`, one support-increase cost-`1` step `(0,0,1) → (0,1,1)`,
and then nineteen support-preserving or support-increase cost-`1` steps
that fill the remaining coordinates of `(7,7,7)`. No hop on that walk
drops support. The running costs after each hop are
`3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23`.

The same body-diagonal cost is realized by later walks that start into
the positive `x` half-space, for example

`(0,0,0) → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (3,1,1) → (4,1,1) → (5,1,1) → (6,1,1) → (7,1,1) → (7,2,1) → (7,3,1) → (7,4,1) → (7,5,1) → (7,6,1) → (7,7,1) → (7,7,2) → (7,7,3) → (7,7,4) → (7,7,5) → (7,7,6) → (7,7,7)`

with hop-costs `3` then twenty cost-`1` steps. That walk is also shortest,
but `(0,0,1)` precedes `(1,0,0)`, so it is not lex-first.

This names the two paths. It is not leftover of the no bit.

## Theorem 2 — Reverse At The Same-`k` Scale `k=7`

The Euclidean-normalized comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

equivalently `3 t(7,0,0)^2 ? t(7,7,7)^2`. Substituting the computed times
gives `3 · 13^2 = 507` and `23^2 = 529`, so

`507 > 529` is false; `507 < 529`.

Arrival per Euclidean length is smaller at `(7,0,0)` than at `(7,7,7)`.
Same-`k` reverse at `k=7` is no. The comparison is displayed, not adopted.

The named walks show why the no bit is not a bare integer comparison: the
axis lex-first walk pays seed-exit `3` and a final support-drop `3`, while
the body-diagonal lex-first walk pays only the seed-exit `3` and then
twenty cost-`1` steps.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_21(0)`. Do not write `ν`
into Admissibility. Do not attach L1. The exhibited walks are one shortest
path to each named site under that displayed rule. Uniqueness is not claimed
among hop-costs, and the walks are not offered as a replacement
for unit-cost first arrival.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exhibited lex-first shortest walks to (7,0,0) and (7,7,7) on the finite ball B_21(0) under one named hop-cost, with the displayed same-k reverse comparison at k=7. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_21(0) for the displayed rule ν at k=7; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ν` among hop-costs that reverse or fail to reverse the
  same-`k` pair at `k=7`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_21(0)`.
- Any reuse of the no bit as a substitute for exhibiting the two walks.
- Any second Dijkstra.
