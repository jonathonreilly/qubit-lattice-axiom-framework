---
claim_id: plane_hug_samek_k14_b42_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=14 under the named plane-hug hop-cost on B_42(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/plane_hug_samek_k14_b42_2026_08_15.py
---

# Named Plane-Hug Same-k Reverse At k=14 On B_42(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_42(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=14`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/plane_hug_samek_k14_b42_2026_08_15.py`](../scripts/plane_hug_samek_k14_b42_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named plane-hug hop-cost `π` is the already scored corridor-slide
rule `μ` plus cost `3` on any `3→3` hop whose destination has
`min_i |w_i| = 1` (one or more unit coordinates). Same-`k` reverse under
the narrower ridge-slide rule `ρ3` dies at `k=14` (`26` versus `46`).
This note is the first display of `π`, scored at that same wall.
Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_42(0)`, the displayed
rule `π` is

`π(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and `min_i |w_i| = 1)`,
else `1`,

where `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`, and
`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first three clauses are seed-exit, both weights `1`, and support drop.
The fourth clause is the axis-hugging `2→2` corridor slide. The fifth
clause is the plane-hug: any interior hop whose destination still has a
unit-height coordinate. Those five clauses are the whole rule.

One Dijkstra from the origin on `B_42(0)` (102425 sites; 102424 nonzero)
gives

`t(14,0,0) = 26`, `t(14,14,14) = 46`.

The displayed same-`k` comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

which is `676/196` versus `2116/588`, or equivalently `2028 > 2116`. The
inequality does not hold. Same-`k` reverse at `k=14` under `π` is no.
The broader plane-hug clause does not restore reverse at the `ρ3` wall.
Independently, the new axis site is `t(42,0,0) = 58`. The shared axis site
`t(39,0,0) = 51` is a `π` score on this ball, not a `μ` leftover.

The pair is not leftover of `μ`: the same sites under `μ` are `24` versus
`44`, and the extra plane-hug clause together with the corridor-slide
clause is what changes both arrivals. On the plane-hug hop
`(2,2,1) → (3,2,1)` one has `|σ| : 3 → 3` and `min_i |w_i| = 1`, so
`μ = 1` while `π = 3`. Therefore `μ` cannot price the plane-hug hop,
and the `π` scores below are not a leftover of `μ`.

The pair is also not leftover of `ρ3`. The ridge-slide rule taxes a
`3→3` hop only when the destination has exactly two absolute coordinates
equal to `1`. The hop `(2,2,1) → (3,2,1)` has only one unit-height
coordinate, so `ρ3 = 1` while `π = 3`. Therefore `ρ3` cannot price the one-unit plane-hug.
The same-`k` arrivals at `k=14` happen to match the
already scored `ρ3` pair, because the `ρ3`-optimal witnesses never use a
one-unit plane-hug hop. Matching arrivals do not make the rule `ρ3`.

The site `(14,14,14)` has ℓ¹ norm `42`, so it is absent from `B_39(0)`.
The `B_42(0)` table is therefore not leftover of the `B_39(0)` times.

The rule is displayed, not adopted. Do not write `π` into Admissibility.
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
the least-nonzero-coordinate clause, the unit-height plane-hug clause, and
the arrival function `t` are separately displayed mathematical inputs. No
axiom text is edited.

## Named Rule

Let `B_42(0) = { v ∈ Z^3 : |v|_1 ≤ 42 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_42(0)`,
`t(v)` is the least sum of `π` along a directed path from `0` to `v` in
that graph.

The comparator `μ` uses only the first four clauses of `π`. On the
plane-hug hop `(2,2,1) → (3,2,1)` one has `|σ| : 3 → 3` and
`min_i |w_i| = 1`, so `μ = 1` while `π = 3`. Therefore `μ` cannot price
the plane-hug hop, and the `π` scores below are not a leftover of `μ`.

## Theorem 1 — Arrivals `t(14,0,0)` And `t(14,14,14)` On `B_42(0)`

One origin Dijkstra on `B_42(0)` returns the integer arrivals

| site | `t_π` |
|---|---:|
| `(14,0,0)` | `26` |
| `(14,14,14)` | `46` |

Every listed site lies in `B_42(0)`. The site `(14,14,14)` has ℓ¹ norm `42`,
so it is absent from `B_39(0)`. The pair is computed on `B_42(0)`, not
copied from a smaller-ball table and not copied from the `μ` pair
`24` versus `44`. These values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `26` is seed-exit `3` onto `(1,0,0)`,
leave-axis `1` onto `(1,1,0)`, hugging corridor-slide `3` onto `(2,1,0)`,
non-hugging face hop `1` onto `(2,2,0)`, twelve support-preserving
cost-`1` face hops to `(14,2,0)`, hugging slide `3` onto `(14,1,0)`, and
support-drop `3` onto `(14,0,0)`, summing to `26`. That walk is a witness
of cost `26`, not a uniqueness claim.

A witness body walk of cost `46` is the same prefix of cost `8` to
`(2,2,0)`, twelve cost-`1` face hops to `(14,2,0)`, twelve cost-`1` face
hops to `(14,14,0)`, enter-body `1` onto `(14,14,1)`, and thirteen
support-preserving cost-`1` body hops to `(14,14,14)`, summing to `46`.
Those last hops have dest with `min_i |w_i| = 2`, so they are not
plane-hug hops. That walk is a witness of cost `46`, not a uniqueness
claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=14`

The Euclidean-normalized comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

equivalently `3 t(14,0,0)^2 ? t(14,14,14)^2`. Substituting the computed times
gives `3 · 26^2 = 2028` and `46^2 = 2116`, so

`2028 > 2116` is false; `2028 < 2116`.

Arrival per Euclidean length is larger at `(14,14,14)` than at `(14,0,0)`.
Same-`k` reverse at `k=14` under `π` is no. The comparison is displayed,
not adopted. The inequality does not hold.

## Theorem 3 — Displayed, Not Adopted

The rule `π` is a displayed scoring device on `B_42(0)`. Do not write `π`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_42(0) for one named hop-cost at k=14. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_42(0) for the displayed rule π at k=14; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `π` among hop-costs that score the same-`k` pair at `k=14`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_42(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=14`.
- Any reuse of the `μ` or `ρ3` arrival table as a substitute for the `π`
  Dijkstra.
- Membership of `π` as a physical hop-cost. Reverse at `k=14` on this ball
  is a displayed comparison, not an adoption.
