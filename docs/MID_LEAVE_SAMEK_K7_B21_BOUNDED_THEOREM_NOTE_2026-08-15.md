---
claim_id: mid_leave_samek_k7_b21_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=7 under the named mid-leave hop-cost on B_21(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/mid_leave_samek_k7_b21_2026_08_15.py
---

# Named Mid-Leave Same-k Reverse At k=7 On B_21(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_21(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=7`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/mid_leave_samek_k7_b21_2026_08_15.py`](../scripts/mid_leave_samek_k7_b21_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named mid-leave hop-cost `μλ` is `ρ3` plus cost `3` on a `1→2` hop
whose destination has `max_i |w_i| = 1` and whose source has
`max_i |v_i| ≥ 2`. The extra clause is the dest-max-`1` leave after the
source has already left the origin. It spares the unit-cube `1→2` hop,
whose source has `max_i |v_i| = 1`. This is the first display of `μλ` at
the same-`k` scale `k=7`. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_21(0)`, let `ν` be
the support-drop rule that costs `3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or
`|σ_w| < |σ_v|`, else `1`. Let `μ` be the corridor-slide rule that costs
`3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero `|w_i|`
equals `1)`, else `1`. Let `ρ3` be the ridge-slide rule that costs `3` if
`μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two `|w_i|` equal `1)`,
else `1`. The displayed rule `μλ` is

`μλ(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=1` and `|σ_w|=2` and
`max_i |w_i| = 1` and `max_i |v_i| ≥ 2)`, else `1`.

Those clauses are the whole rule.

One Dijkstra from the origin on `B_21(0)` (13287 sites; 13286 nonzero)
gives

`t(7,0,0) = 19`, `t(7,7,7) = 25`.

The displayed same-`k` comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

which is `361/49` versus `625/147`, or equivalently `1083 > 625`. The
inequality holds. Same-`k` reverse at `k=7` under `μλ` is yes.
Independently, the new axis site is `t(21,0,0) = 37`. The shared axis
site `t(18,0,0) = 30` is a `μλ` score on this ball, not a leftover.

The extra clause is idle on every nearest-neighbor hop in `B_21(0)`. A
dest with `|σ_w|=2` and `max_i |w_i| = 1` is a unit-cube face diagonal.
Every support-`1` neighbor of such a dest has `max_i |v_i| = 1`. The two
extra predicates therefore never co-occur on a nearest-neighbor hop, so
`μλ` agrees with `ρ3` on this ball. The pair is still a `μλ` Dijkstra
output, not a copied `ρ3` table.

The pair is not leftover of `λ2` as a rule: on the late-leave hop
`(2,0,0) → (2,1,0)` one has `|σ| : 1 → 2` and `max_i |w_i| = 2`, so
`λ2 = 3` while `μλ = 1` and `ρ3 = 1`. Therefore `λ2` cannot price late leave
as `μλ` does. The unit-cube hop `(1,0,0) → (1,1,0)` has `|σ| : 1 → 2`
and `max_i |w_i| = 1` with `max_i |v_i| = 1`, so `μλ` spares the unit-cube
`1→2` at cost `1`.

The site `(7,7,7)` has ℓ¹ norm `21`, so it is absent from `B_18(0)`. The
`B_21(0)` table is therefore not leftover of the `B_18(0)` times.

The rule is displayed, not adopted. Do not write `μλ` into Admissibility.
Do not write μλ into Admissibility. Do not attach L1.

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

Let `B_21(0) = { v ∈ Z^3 : |v|_1 ≤ 21 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_21(0)`,
`t(v)` is the least sum of `μλ` along a directed path from `0` to `v` in
that graph.

The comparator `λ2` taxes `1→2` hops whose dest has `max_i |w_i| ≥ 2`.
On the late-leave hop `(2,0,0) → (2,1,0)` one has `|σ| : 1 → 2` and
`max_i |w_i| = 2`, so `λ2 = 3` while `μλ = 1`. Therefore `λ2` cannot
price late leave. On the unit-cube hop `(1,0,0) → (1,1,0)` the extra
clause is idle, so the unit-cube `1→2` is spared.

## Theorem 1 — Arrivals `t(7,0,0)` And `t(7,7,7)` On `B_21(0)`

One origin Dijkstra on `B_21(0)` returns the integer arrivals

| site | `t_μλ` |
|---|---:|
| `(7,0,0)` | `19` |
| `(7,7,7)` | `25` |

Every listed site lies in `B_21(0)`. The site `(7,7,7)` has ℓ¹ norm `21`,
so it is absent from `B_18(0)`. The pair is computed on `B_21(0)`, not
copied from a smaller-ball table. These values are Dijkstra outputs, not
fitted scalars.

A witness axis walk of cost `19` is seed-exit `3` onto `(0,-1,0)`,
unit-cube support-increase `1` onto `(1,-1,0)`, corridor-slide `3` onto
`(1,-2,0)`, six support-preserving cost-`1` height-`2` face slides to
`(7,-2,0)`, corridor-slide `3` onto `(7,-1,0)`, and support-drop `3`
onto `(7,0,0)`, summing to `19`. That walk never takes a dest-max-`1`
source-max-`≥2` hop. A witness body walk of cost `25` is seed-exit `3`
onto `(0,0,1)`, support-increase `1` onto `(0,1,1)`, corridor-slide `3`
onto `(0,1,2)`, eleven support-preserving cost-`1` face hops to
`(0,7,7)`, support-increase `1` onto `(1,7,7)`, and six
support-preserving cost-`1` body hops onto `(7,7,7)`, summing to `25`.
Those walks are witnesses, not a uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=7`

The Euclidean-normalized comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

equivalently `3 t(7,0,0)^2 ? t(7,7,7)^2`. Substituting the computed times
gives `3 · 19^2 = 1083` and `25^2 = 625`, so

`1083 > 625`.

Arrival per Euclidean length is larger at `(7,0,0)` than at `(7,7,7)`.
Same-`k` reverse at `k=7` under `μλ` is yes. The comparison is displayed,
not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `μλ` is a displayed scoring device on `B_21(0)`. Do not write
`μλ` into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_21(0) for one named hop-cost at k=7. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_21(0) for the displayed rule μλ at k=7; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `μλ` among hop-costs that reverse the same-`k` pair at `k=7`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_21(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=7`.
- Any reuse of a `ρ3` or `λ2` arrival table as a substitute for the `μλ`
  Dijkstra.
- Any reuse of the `B_18(0)` arrival table as a substitute for the
  radius-`21` Dijkstra.
- Membership of `μλ` as a physical hop-cost. Reverse at `k=7` on this ball
  is a displayed comparison, not an adoption.
