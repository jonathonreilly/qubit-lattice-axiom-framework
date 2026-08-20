---
claim_id: kappa_late_leave_samek_k1_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=1 under the named kappa-plus-late-leave hop-cost on B_6(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/kappa_late_leave_samek_k1_b6_2026_08_15.py
---

# Named Kappa-Plus-Late-Leave Same-k Reverse At k=1 On B_6(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_6(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=1`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/kappa_late_leave_samek_k1_b6_2026_08_15.py`](../scripts/kappa_late_leave_samek_k1_b6_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named kappa-plus-late-leave hop-cost `κλ` is scored independently on
`B_6(0)`. The ball is not leftover of a larger-ball table: one origin
Dijkstra is run on this ball.

The residual scored here is the first display of `κλ`: the already scored
ridge-slide rule `ρ3`, plus the ridge-enter `2→3` clause of `κ`, plus the
late `1→2` clause of `λ2`. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_6(0)`, let `ν` be the
support-drop rule that costs `3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or
`|σ_w| < |σ_v|`, else `1`. Let `μ` be the corridor-slide rule

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`.

The ridge-slide rule `ρ3` is

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

The displayed rule `κλ` is

`κλ(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=2` and `|σ_w|=3` and
exactly two `|w_i|` equal `1)` or `(|σ_v|=1` and `|σ_w|=2` and
`max_i |w_i| ≥ 2)`, else `1`.

The extra clauses are a ridge-enter `2→3` hop whose destination has
exactly two unit coordinates, and a late `1→2` hop whose destination
already has a coordinate of size at least `2`. They are not a tax on
the early `1→2` hop into `(1,1,0)` and not a tax on the small `2→3` hop
into `(1,1,1)`.

One Dijkstra from the origin on `B_6(0)` (377 sites; 376 nonzero) gives

`t(1,0,0) = 3`, `t(1,1,1) = 5`.

The displayed same-`k` comparison at `k=1` is

`t(1,0,0)^2 / 1  ?  t(1,1,1)^2 / 3`,

which is `9/1` versus `25/3`, or equivalently `27 > 25`. The
inequality holds. Same-`k` reverse holds at `k=1`. The
displayed rule is not adopted. Independently, the axis
endpoint of this ball is `t(6,0,0) = 18`.

The `k=1` pair is `3` versus `5`. A least-cost walk to `(1,0,0)` or
`(1,1,1)` never needs a ridge-enter hop or a late `1→2` hop. The extra
clauses are live on the ball: on `(2,1,0) → (2,1,1)` one has `|σ| : 2 → 3`
and exactly two `|w_i|=1`, so `ρ3 = 1` while `κλ = 3`. Therefore `ρ3`
cannot price the ridge-enter hop. On `(2,0,0) → (2,1,0)` one has
`|σ| : 1 → 2` and `max_i |w_i| = 2`, so `ρ3 = 1` while `κλ = 3`.
Therefore `ρ3` cannot price the late 1→2 hop.

The rule is displayed, not adopted. Do not write `κλ` into Admissibility.
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

Let `B_6(0) = { v ∈ Z^3 : |v|_1 ≤ 6 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_6(0)`,
`t(v)` is the least sum of `κλ` along a directed path from `0` to `v` in
that graph.

The comparator `ρ3` uses the three support-drop clauses, the axis-hugging
`2→2` slide, and the ridge `3→3` slide. On the ridge-enter hop
`(2,1,0) → (2,1,1)` one has `|σ_v|=2`, `|σ_w|=3`, and exactly two
`|w_i|=1`, so `ρ3 = 1` while `κλ = 3`. On the late `1→2` hop
`(2,0,0) → (2,1,0)` one has `|σ_v|=1`, `|σ_w|=2`, and `max_i |w_i| ≥ 2`,
so `ρ3 = 1` while `κλ = 3`. On the early 1→2 hop `(1,0,0) → (1,1,0)` one
has `max_i |w_i| = 1`, so both `ρ3` and `κλ` cost `1`. On the small 2→3 hop
`(1,1,0) → (1,1,1)` the destination has three unit coordinates, so both
`ρ3` and `κλ` cost `1`. On the interior `3→3` hop `(2,2,2) → (3,2,2)` the
destination has no unit coordinate, so both cost `1`.

## Theorem 1 — Arrivals `t(1,0,0)` And `t(1,1,1)` On `B_6(0)`

One origin Dijkstra on `B_6(0)` returns the integer arrivals

| site | `t_κλ` |
|---|---:|
| `(1,0,0)` | `3` |
| `(1,1,1)` | `5` |

Every listed site lies in `B_6(0)`. The pair is computed on `B_6(0)`, not
copied from a larger-ball table. These values are Dijkstra outputs, not
fitted scalars.

A witness walk to `(1,0,0)` is seed-exit of cost `3` onto `(1,0,0)`,
summing to `3`. A witness walk to `(1,1,1)` is seed-exit `3` onto
`(1,0,0)`, early 1→2 of cost `1` onto `(1,1,0)`, and small 2→3 of cost `1`
onto `(1,1,1)`, summing to `5`. Those walks are witnesses, not a
uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=1`

The Euclidean-normalized comparison at `k=1` is

`t(1,0,0)^2 / 1  ?  t(1,1,1)^2 / 3`,

equivalently `3 t(1,0,0)^2 ? t(1,1,1)^2`. Substituting the computed times
gives `3 · 3^2 = 27` and `5^2 = 25`, so

`27 > 25` is true; `27 > 25` holds.

Arrival per Euclidean length is larger at `(1,0,0)` than at `(1,1,1)`.
Same-`k` reverse at `k=1` is yes. The comparison is
displayed, not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `κλ` is a displayed scoring device on `B_6(0)`. Do not write `κλ`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_6(0) for one named hop-cost at k=1. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_6(0) for the displayed rule κλ at k=1; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `κλ` among hop-costs that score the same-`k` pair at `k=1`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_6(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=1`.
- Any reuse of a larger-ball arrival table as a substitute for the
  radius-`6` Dijkstra.
- Membership of `κλ` as a physical hop-cost. Reverse at `k=1` on this ball
  is a displayed comparison, not an adoption.
