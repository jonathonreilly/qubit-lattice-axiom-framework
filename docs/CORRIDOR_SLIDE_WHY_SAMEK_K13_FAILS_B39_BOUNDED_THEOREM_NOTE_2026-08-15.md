---
claim_id: corridor_slide_why_samek_k13_fails_b39_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Lex-first shortest paths to (13,0,0) and (13,13,13) under the named corridor-slide hop-cost on B_39(0) are named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/corridor_slide_why_samek_k13_fails_b39_2026_08_15.py
---

# Lex-First Shortest Paths To (13,0,0) And (13,13,13) On B_39(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_39(0)`,
restricted to naming a lex-first shortest walk from `0` to `(13,0,0)` and a
lex-first shortest walk from `0` to `(13,13,13)`, and displaying the same-`k`
reverse comparison at `k=13`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/corridor_slide_why_samek_k13_fails_b39_2026_08_15.py`](../scripts/corridor_slide_why_samek_k13_fails_b39_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The same named corridor-slide hop-cost `μ` already scored on `B_39(0)` is
scored independently here by naming lex-first shortest paths to both
same-`k` sites at `k=13`. Same-`k` reverse under `μ` holds at `k=1` through
`k=12` and fails at `k=13` (`23` versus `41`). The pair of walks is not leftover of the two
arrival integers: one origin Dijkstra is run on this ball, and the two
site sequences are named.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_39(0)`, the displayed
comparator `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The displayed rule `μ` is

`μ(v→w) = 3` if `ν(v→w)` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`.

The first three clauses are those of `ν`: seed-exit, both weights `1`, and
support drop. The fourth clause is the axis-hugging `2→2` slide. Those four
clauses are the whole rule. Uniqueness is not claimed.

One origin Dijkstra on `B_39(0)` (82239 sites; 82238 nonzero) gives

`t(13,0,0) = 23`, `t(13,13,13) = 41`.

The site `(13,13,13)` has ℓ¹ norm `39`, so it is absent from `B_36(0)`. The
`B_39(0)` table is therefore not leftover of a smaller-ball table.

Among all walks of cost `23` from `0` to `(13,0,0)`, the lexicographically
first sequence of sites is

`(0,0,0) → (0,-1,0) → (0,-1,-1) → (1,-1,-1) → (2,-1,-1) → (3,-1,-1) → (4,-1,-1) → (5,-1,-1) → (6,-1,-1) → (7,-1,-1) → (8,-1,-1) → (9,-1,-1) → (10,-1,-1) → (11,-1,-1) → (12,-1,-1) → (13,-1,-1) → (13,-1,0) → (13,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3` and running costs
`3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 23` summing to `23`. After the seed-exit
the walk leaves the axis into the body, travels along the line
`y = z = -1`, and then pays two support-drop hops of cost `3`.

Among all walks of cost `41` from `0` to `(13,13,13)`, the lexicographically
first sequence of sites is

`(0,0,0) → (0,0,1) → (0,1,1) → (1,1,1) → (1,1,2) → (1,1,3) → (1,1,4) → (1,1,5) → (1,1,6) → (1,1,7) → (1,1,8) → (1,1,9) → (1,1,10) → (1,1,11) → (1,1,12) → (1,1,13) → (1,2,13) → (1,3,13) → (1,4,13) → (1,5,13) → (1,6,13) → (1,7,13) → (1,8,13) → (1,9,13) → (1,10,13) → (1,11,13) → (1,12,13) → (1,13,13) → (2,13,13) → (3,13,13) → (4,13,13) → (5,13,13) → (6,13,13) → (7,13,13) → (8,13,13) → (9,13,13) → (10,13,13) → (11,13,13) → (12,13,13) → (13,13,13)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1`
and running costs
`3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41`
summing to `41`. That walk never uses the support-drop clause and never uses
the axis-hugging `2→2` slide.

The displayed same-`k` comparison at `k=13` is

`t(13,0,0)^2 / 169  ?  t(13,13,13)^2 / 507`,

which is `529/169` versus `1681/507`, or equivalently `1587 > 1681`. The
inequality does not hold: `1587 < 1681`. Same-`k` reverse at `k=13` under
`μ` is no. The comparison is displayed, not adopted.

The pair is not leftover of `ν`: the same sites under `ν` are `19` versus
`41`, and `1083 > 1681` fails. The extra corridor-slide clause is what
changes the axis arrival. On the hugging hop `(1,1,0) → (2,1,0)` one has
`|σ| : 2 → 2` and least nonzero `|w_i| = 1`, so `ν = 1` while `μ = 3`.
The face corridor that stays at `|σ|=2` with a unit transverse coordinate
is therefore priced by `μ` and not by `ν`. The leave-axis hop
`(0,-1,0) → (1,-1,0)` stays at cost `1` under both `ν` and `μ`. Therefore
`ν` cannot price the axis-hugging slide, and the `μ` walks below are not
a leftover of `ν`.

The rule is displayed, not adopted. Do not write `μ` into Admissibility.
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
the least-nonzero-coordinate test, and the arrival function `t` are
separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_39(0) = { v ∈ Z^3 : |v|_1 ≤ 39 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_39(0)`,
`t(v)` is the least sum of `μ` along a directed path from `0` to `v` in
that graph.

A walk is lex-first among shortest walks to a named site when its sequence
of sites is the least tuple of integer triples, compared coordinatewise,
among all walks of cost `t` of that site.

The comparator `ν` uses only the first three clauses of `μ`. On the
axis-hugging slide `(1,1,0) → (2,1,0)` one has `|σ| : 2 → 2` and least
nonzero `|w_i| = 1`, so `ν = 1` while `μ = 3`. Therefore `ν` cannot price
the corridor slide, and the `μ` scores below are not a leftover of `ν`.

## Theorem 1 — Arrivals And Lex-First Shortest Paths

One origin Dijkstra on `B_39(0)` returns the integer arrivals

| site | `t_μ` |
|---|---:|
| `(13,0,0)` | `23` |
| `(13,13,13)` | `41` |

Every listed site lies in `B_39(0)`. The site `(13,13,13)` has ℓ¹ norm `39`,
so it is absent from `B_36(0)`. The pair is computed on `B_39(0)`, not
copied from a smaller-ball table and not copied from the `ν` pair
`19` versus `41`. These values are Dijkstra outputs, not fitted scalars.

The lex-first walk of cost `23` to `(13,0,0)` is the eighteen-site walk recorded
above. The seventeen hop-costs are seed-exit `3` from `(0,0,0)` onto
`(0,-1,0)`, one support-increase cost-`1` step `(0,-1,0) → (0,-1,-1)`
into the face, one support-increase cost-`1` step
`(0,-1,-1) → (1,-1,-1)` into the body, twelve support-preserving cost-`1`
body hops along `y = z = -1` from `(1,-1,-1)` to `(13,-1,-1)`, a
support-drop `3` from `(13,-1,-1)` onto `(13,-1,0)`, and a support-drop
`3` from `(13,-1,0)` onto `(13,0,0)`. The running costs after each hop are
`3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 23`.

That route is forced by the corridor-slide clause. The two-coordinate
face walk that is cheapest under `ν`,

`(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (5,-1,0) → (6,-1,0) → (7,-1,0) → (8,-1,0) → (9,-1,0) → (10,-1,0) → (11,-1,0) → (12,-1,0) → (13,-1,0) → (13,0,0)`,

has hop-costs `3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3` under `μ` and sums to `43`.
Each hop `(n,-1,0) → (n+1,-1,0)` for `n ≥ 1` is a `2→2` slide whose
destination has least nonzero absolute coordinate `1`, so `μ` prices it
at `3` while `ν` prices it at `1`. The lex-first `μ` walk therefore
enters the body, where those slides are not charged, and pays two
support-drops at the end instead of a cheap face corridor.

The same axis cost is realized by later walks that stay in the positive
half-space, for example

`(0,0,0) → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (3,1,1) → (4,1,1) → (5,1,1) → (6,1,1) → (7,1,1) → (8,1,1) → (9,1,1) → (10,1,1) → (11,1,1) → (12,1,1) → (13,1,1) → (13,1,0) → (13,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3`. That walk is also shortest, but
`(0,-1,0)` precedes `(1,0,0)`, so it is not lex-first.

The lex-first walk of cost `41` to `(13,13,13)` is the forty-site walk
recorded above. The thirty-nine hop-costs are seed-exit `3` from `(0,0,0)`
onto `(0,0,1)`, two support-increase cost-`1` steps
`(0,0,1) → (0,1,1) → (1,1,1)`, and then thirty-six support-preserving or
support-increase cost-`1` steps that fill the remaining coordinates of
`(13,13,13)`. No hop on that walk drops support, and no hop is an
axis-hugging `2→2` slide. The running costs after each hop are
`3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41`.

The same body-diagonal cost is realized by later walks that start into
the positive `x` half-space, for example

`(0,0,0) → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (3,1,1) → (4,1,1) → (5,1,1) → (6,1,1) → (7,1,1) → (8,1,1) → (9,1,1) → (10,1,1) → (11,1,1) → (12,1,1) → (13,1,1) → (13,2,1) → (13,3,1) → (13,4,1) → (13,5,1) → (13,6,1) → (13,7,1) → (13,8,1) → (13,9,1) → (13,10,1) → (13,11,1) → (13,12,1) → (13,13,1) → (13,13,2) → (13,13,3) → (13,13,4) → (13,13,5) → (13,13,6) → (13,13,7) → (13,13,8) → (13,13,9) → (13,13,10) → (13,13,11) → (13,13,12) → (13,13,13)`

with hop-costs `3` then thirty-eight cost-`1` steps. That walk is also shortest,
but `(0,0,1)` precedes `(1,0,0)`, so it is not lex-first.

A walk that starts toward `-x` is lex-smaller than the named axis walk,
but it is not shortest. The twenty-site walk

`(0,0,0) → (-1,0,0) → (-1,-1,0) → (-1,-1,-1) → (0,-1,-1) → (1,-1,-1) → (2,-1,-1) → (3,-1,-1) → (4,-1,-1) → (5,-1,-1) → (6,-1,-1) → (7,-1,-1) → (8,-1,-1) → (9,-1,-1) → (10,-1,-1) → (11,-1,-1) → (12,-1,-1) → (13,-1,-1) → (13,-1,0) → (13,0,0)`

pays an extra support-drop `3` on `(-1,-1,-1) → (0,-1,-1)` when it
crosses the plane `x = 0` and briefly drops from three nonzero
coordinates to two. Its hop-costs sum to `27`, which is strictly larger
than `t(13,0,0) = 23`.

This names the two paths. It is not leftover of the two arrival integers.

## Theorem 2 — Reverse At The Same-`k` Scale `k=13`

The Euclidean-normalized comparison at `k=13` is

`t(13,0,0)^2 / 169  ?  t(13,13,13)^2 / 507`,

equivalently `3 t(13,0,0)^2 ? t(13,13,13)^2`. Substituting the computed times
gives `3 · 23^2 = 1587` and `41^2 = 1681`, so

`1587 > 1681` is false; `1587 < 1681`.

Arrival per Euclidean length is not larger at `(13,0,0)` than at
`(13,13,13)`. Same-`k` reverse at `k=13` under `μ` is no. The comparison
is displayed, not adopted. The inequality does not hold.

The named walks show why reverse fails under `μ` at `k=13`: the axis
lex-first walk under `μ` cannot use the cheap `|σ|=2` face corridor that
produces `t(13,0,0) = 19` under `ν`. It must enter the body and pay two
support-drops, raising the axis arrival to `23` while the body-diagonal
arrival stays `41`. That raise is enough for reverse through `k=12` and
not enough at `k=13`. Then `1587 < 1681`.

## Theorem 3 — Displayed, Not Adopted

The rule `μ` is a displayed scoring device on `B_39(0)`. Do not write `μ`
into Admissibility. Do not attach L1. The exhibited walks are one shortest
path to each named site under that displayed rule. Uniqueness is not claimed
among hop-costs, and the walks are not offered as a replacement
for unit-cost first arrival.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exhibited lex-first shortest walks to (13,0,0) and (13,13,13) on the finite ball B_39(0) under one named hop-cost, with the displayed same-k reverse comparison at k=13. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_39(0) for the displayed rule μ at k=13; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `μ` among hop-costs that score the same-`k` pair at `k=13`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_39(0)`.
- Any reuse of the two arrival integers as a substitute for exhibiting the
  two walks.
- Any reuse of the `ν` arrival table as a substitute for the `μ` Dijkstra.
- Any second Dijkstra.
- Any adoption of the leave-axis `1→2` clause as part of `μ`.
