---
claim_id: kappa_late_leave_samek_k7_b21_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=7 under the named kappa-plus-late-leave hop-cost on B_21(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/kappa_late_leave_samek_k7_b21_2026_08_15.py
---

# Named Kappa-Plus-Late-Leave Same-k Reverse At k=7 On B_21(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_21(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=7`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/kappa_late_leave_samek_k7_b21_2026_08_15.py`](../scripts/kappa_late_leave_samek_k7_b21_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named kappa-plus-late-leave hop-cost `κλ` is stacked `κ` plus `λ2`:
`ρ3` plus the ridge-enter `2→3` clause of `κ` plus the late `1→2` clause
of `λ2`. This is the first display of same-`k` under `κλ` at `k=7`.
Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_21(0)`, let `ν` be
the support-drop rule that costs `3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or
`|σ_w| < |σ_v|`, else `1`. Let `μ` be the corridor-slide rule that costs
`3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero `|w_i|`
equals `1)`, else `1`. Let `ρ3` be the ridge-slide rule that costs `3` if
`μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two `|w_i|` equal `1)`,
else `1`. Let `κ` be the ridge-enter rule that costs `3` if `ρ3` would be
`3` or `(|σ_v|=2` and `|σ_w|=3` and exactly two `|w_i|` equal `1)`, else
`1`. Let `λ2` be the late-leave rule that costs `3` if `ρ3` would be `3`
or `(|σ_v|=1` and `|σ_w|=2` and `max_i |w_i| ≥ 2)`, else `1`. The
displayed stacked rule `κλ` is

`κλ(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=2` and `|σ_w|=3` and
exactly two `|w_i|` equal `1)` or `(|σ_v|=1` and `|σ_w|=2` and
`max_i |w_i| ≥ 2)`, else `1`.

Those clauses are the whole rule. The extra `1→2` clause is late
leave-axis: it taxes leaving the axis after the unit cube, and it
spares the unit-cube `1→2` hop.

The comparison uses one Dijkstra from the origin on `B_21(0)`
(13287 sites; 13286 nonzero) and gives

`t(7,0,0) = 19`, `t(7,7,7) = 25`.

The displayed same-`k` comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

which is `361/49` versus `625/147`, or equivalently `1083 > 625`. The
inequality holds. Same-`k` reverse at `k=7` under `κλ` is yes.
Independently, the new axis site is `t(21,0,0) = 37`. The shared axis
site `t(18,0,0) = 30` is a `κλ` score on this ball, not a leftover.

The pair is not leftover of `ρ3` as a rule: on the late-leave hop
`(2,0,0) → (2,1,0)` one has `|σ| : 1 → 2` and `max_i |w_i| = 2`, so
`ρ3 = 1` while `κλ = 3`. Therefore `ρ3` cannot price late leave. On the
unit-ridge enter `(2,1,0) → (2,1,1)` one has `|σ| : 2 → 3` and exactly
two `|w_i|` equal to `1`, so `ρ3 = 1` while `κλ = 3`. Therefore `ρ3`
cannot price ridge-enter. The unit-cube hop `(1,0,0) → (1,1,0)` has
`|σ| : 1 → 2` and `max_i |w_i| = 1`, so both `ρ3` and `κλ` price it at
`1`.

The pair is not leftover of `κ`: `κ` omits the late-leave clause, so
`(2,0,0) → (2,1,0)` has `κ = 1` while `κλ = 3`. The pair is not leftover
of `λ2`: `λ2` omits the ridge-enter clause, so `(2,1,0) → (2,1,1)` has
`λ2 = 1` while `κλ = 3`. The same-`k` arrivals at `k=7` happen to
coincide with the `ρ3` pair because a cheapest axis witness and a
cheapest body witness never take a late-leave hop or a ridge-enter hop.
The on-ball hops `(2,0,0) → (2,1,0)` and `(2,1,0) → (2,1,1)` record that
the new clause is live.

The site `(7,7,7)` has ℓ¹ norm `21`, so it is absent from `B_18(0)`. The
`B_21(0)` table is therefore not leftover of the `B_18(0)` times.

The rule is displayed, not adopted. Do not write `κλ` into Admissibility.
Do not write κλ into Admissibility. Do not attach L1.

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
the ridge-enter clause, the late-leave clause, and the arrival function `t`
are separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_21(0) = { v ∈ Z^3 : |v|_1 ≤ 21 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_21(0)`,
`t(v)` is the least sum of `κλ` along a directed path from `0` to `v` in
that graph.

The comparator `ρ3` uses only the inherited ridge-slide clauses. On
`(2,0,0) → (2,1,0)` one has `|σ| : 1 → 2` and `max_i |w_i| = 2`, so
`ρ3 = 1` while `κλ = 3`. On `(2,1,0) → (2,1,1)` one has `|σ| : 2 → 3`
and exactly two unit destination coordinates, so `ρ3 = 1` while
`κλ = 3`. The comparator `κ` uses ridge-enter but not late leave. The
comparator `λ2` uses late leave but not ridge-enter. The stacked rule
uses both extra clauses.

## Theorem 1 — Arrivals `t(7,0,0)` And `t(7,7,7)` On `B_21(0)`

One origin Dijkstra on `B_21(0)` returns the integer arrivals

| site | `t_κλ` |
|---|---:|
| `(7,0,0)` | `19` |
| `(7,7,7)` | `25` |

Every listed site lies in `B_21(0)`. The site `(7,7,7)` has ℓ¹ norm `21`,
so it is absent from `B_18(0)`. The pair is computed on `B_21(0)`, not
copied from a smaller-ball table and not copied from a `ρ3`, `κ`, or
`λ2` table. These values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `19` is seed-exit `3` onto `(0,-1,0)`,
support-increase `1` onto `(1,-1,0)`, corridor-slide `3` onto `(1,-2,0)`,
six support-preserving cost-`1` height-`2` slides to `(7,-2,0)`,
corridor-slide `3` onto `(7,-1,0)`, and support-drop `3` onto `(7,0,0)`,
summing to `19`. The first support-increase lands on a unit-cube face, so
it is not a late-leave hop. A witness body walk of cost `25` is seed-exit
`3` onto `(0,0,1)`, support-increase `1` onto `(0,1,1)`, corridor-slide
`3` onto `(0,1,2)`, eleven support-preserving cost-`1` face hops to
`(0,7,7)`, support-increase `1` onto `(1,7,7)`, and six support-preserving
cost-`1` body hops onto `(7,7,7)`, summing to `25`. The body enter
`(0,7,7) → (1,7,7)` has a single unit destination coordinate, so it is
not a ridge-enter. Those walks are witnesses, not a uniqueness claim.

A witness that the ridge-enter clause is live is the walk seed-exit `3`
onto `(0,1,0)`, unit-cube support-increase `1` onto `(1,1,0)`,
corridor-slide `3` onto `(1,2,0)`, eighteen support-preserving cost-`1`
height-`2` slides to `(19,2,0)`, corridor-slide `3` onto `(19,1,0)`, and
ridge-enter `3` onto `(19,1,1)`, summing to `31`. Replacing only the last
hop by its `ρ3` price `1` yields `29`. The unit-cube leave is used so
the walk does not take a late-leave hop.

## Theorem 2 — Reverse At The Same-`k` Scale `k=7`

The Euclidean-normalized comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

equivalently `3 t(7,0,0)^2 ? t(7,7,7)^2`. Substituting the computed times
gives `3 · 19^2 = 1083` and `25^2 = 625`, so

`1083 > 625`.

Arrival per Euclidean length is larger at `(7,0,0)` than at `(7,7,7)`.
Same-`k` reverse at `k=7` under `κλ` is yes. The comparison is displayed,
not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `κλ` is a displayed scoring device on `B_21(0)`. Do not write
`κλ` into Admissibility. Do not write κλ into Admissibility. Do not attach
L1. It is not a replacement for coordinate-sum first arrival, and it is
not offered as the unique hop-cost with same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_21(0) for one named hop-cost at k=7. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_21(0) for the displayed rule κλ at k=7; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `κλ` among hop-costs that reverse the same-`k` pair at `k=7`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_21(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=7`.
- Any reuse of the `ρ3`, `κ`, or `λ2` arrival table as a substitute for
  the `κλ` Dijkstra.
- Any reuse of the `B_18(0)` arrival table as a substitute for the
  radius-`21` Dijkstra.
