---
claim_id: mid_leave_samek_k13_b39_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=13 under the named mid-leave hop-cost on B_39(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/mid_leave_samek_k13_b39_2026_08_15.py
---

# Named Mid-Leave Same-k Reverse At k=13 On B_39(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_39(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=13`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/mid_leave_samek_k13_b39_2026_08_15.py`](../scripts/mid_leave_samek_k13_b39_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

This is the first display of same-`k` reverse at `k=13` under the named
mid-leave hop-cost `μλ`. The pair is computed by one origin Dijkstra on
`B_39(0)`. The site `(13,13,13)` has ℓ¹ norm `39` and therefore lies on
the boundary of this ball.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_39(0)`, the displayed
rules are

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`.

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

`μλ(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=1` and `|σ_w|=2` and
`max_i |w_i|=1` and `max_i |v_i| ≥ 2)`, else `1`.

The last clause is the mid-leave tax: a `1→2` hop whose destination has
maximum absolute coordinate `1` after the source already has maximum
absolute coordinate at least `2`. The same clause spares the unit-cube
`1→2` hop, whose source has `max_i |v_i| = 1`. Those clauses are the whole
rule. Uniqueness is not claimed.

The extra mid-leave clause does not fire on nearest-neighbor hops. A hop
with `|σ_v|=1` and `|σ_w|=2` must keep the unique source axis coordinate
and add a unit perpendicular coordinate, so the destination maximum is at
least the source maximum. The source-maximum condition `≥ 2` then forbids
destination maximum `1`. The displayed `μλ` scores on this graph therefore
coincide with the `ρ3` scores. That identity is a property of the
six-neighbor graph, not a uniqueness claim among hop-costs.

One Dijkstra from the origin on `B_39(0)` (82239 sites; 82238 nonzero) gives

`t(13,0,0) = 25`, `t(13,13,13) = 43`.

The displayed same-`k` comparison at `k=13` is

`t(13,0,0)^2 / 169  ?  t(13,13,13)^2 / 507`,

which is `625/169` versus `1849/507`, or equivalently `1875 > 1849`. The
inequality holds.

The rule is displayed, not adopted. Do not write μλ into Admissibility.
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
the mid-leave clause, and the arrival function `t` are separately displayed
mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_39(0) = { v ∈ Z^3 : |v|_1 ≤ 39 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_39(0)`,
`t(v)` is the least sum of `μλ` along a directed path from `0` to `v` in
that graph.

The comparator `ρ3` uses every clause of `μλ` except the extra mid-leave
tax. On this six-neighbor graph that extra clause does not fire, so
`μλ = ρ3` as functions on the directed edges of `B_39(0)`. The `μλ`
scores below are still a named displayed rule, scored independently by
one origin Dijkstra.

A witness axis walk of cost `25` is seed-exit `3` onto `(1,0,0)`, leave-axis
`1` onto `(1,1,0)`, corridor-slide `3` onto `(2,1,0)`, non-hugging face hop
`1` onto `(2,2,0)`, eleven support-preserving cost-`1` face hops to
`(13,2,0)`, corridor-slide `3` onto `(13,1,0)`, and support-drop `3` onto
`(13,0,0)`. That walk is a witness of cost `25`, not a uniqueness claim.

A witness body walk of cost `43` is the same prefix of cost `8` to
`(2,2,0)`, eleven cost-`1` face hops to `(13,2,0)`, eleven cost-`1` face
hops to `(13,13,0)`, enter-body `1` onto `(13,13,1)`, and twelve
support-preserving cost-`1` body hops to `(13,13,13)`. That walk is a
witness of cost `43`, not a uniqueness claim.

## Theorem 1 — Arrivals `t(13,0,0)` And `t(13,13,13)` On `B_39(0)`

One origin Dijkstra on `B_39(0)` returns the integer arrivals

| site | `t_μλ` |
|---|---:|
| `(13,0,0)` | `25` |
| `(13,13,13)` | `43` |

Every listed site lies in `B_39(0)`. The site `(13,13,13)` has ℓ¹ norm `39`
and sits on the boundary of this ball. These values are Dijkstra outputs,
not fitted scalars.

## Theorem 2 — Reverse At The Same-`k` Scale `k=13`

The Euclidean-normalized comparison at `k=13` is

`t(13,0,0)^2 / 169  ?  t(13,13,13)^2 / 507`,

equivalently `3 t(13,0,0)^2 ? t(13,13,13)^2`. Substituting the computed times
gives `3 · 25^2 = 1875` and `43^2 = 1849`, so

`1875 > 1849`.

Arrival per Euclidean length is larger at `(13,0,0)` than at `(13,13,13)`.
Same-`k` reverse at `k=13` holds under `μλ`. The comparison is displayed,
not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `μλ` is a displayed scoring device on `B_39(0)`. Do not write μλ
into Admissibility. Do not attach L1. It is not a replacement for
first arrival under equal hop weights, and it is not offered as the unique
hop-cost with same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_39(0) for one named hop-cost at k=13. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_39(0) for the displayed rule μλ at k=13; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `μλ` among hop-costs that score the same-`k` pair at `k=13`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_39(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=13`.
- Any write of `μλ` into Admissibility.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.
