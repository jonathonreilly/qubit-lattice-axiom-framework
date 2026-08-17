---
claim_id: ridge_slide_samek_k6_b18_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=6 under the named ridge-slide hop-cost on B_18(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ridge_slide_samek_k6_b18_2026_08_15.py
---

# Named Ridge-Slide Same-k Reverse At k=6 On B_18(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_18(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=6`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/ridge_slide_samek_k6_b18_2026_08_15.py`](../scripts/ridge_slide_samek_k6_b18_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named ridge-slide hop-cost `ρ3` already reverse-holds at `k=1` and at
`k=7`. The residual scored here is the same named rule on `B_18(0)` at
`k=6`. The comparator corridor-slide rule `μ` holds same-`k` reverse at
`k=6` by `16` versus `20`. The displayed extra clause of `ρ3` is cost `3`
on a `3→3` hop whose destination has exactly two coordinates of absolute
value `1`. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_18(0)`, let `ν` be
the support-drop rule that costs `3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or
`|σ_w| < |σ_v|`, else `1`. Let `μ` be the corridor-slide rule that costs
`3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero `|w_i|`
equals `1)`, else `1`. The displayed rule `ρ3` is

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

The extra clause is a ridge slide: both ends have support `3`, and the
destination still has exactly two unit coordinates. Those clauses are the
whole rule.

One Dijkstra from the origin on `B_18(0)` (8473 sites; 8472 nonzero)
gives

`t(6,0,0) = 18`, `t(6,6,6) = 22`.

The displayed same-`k` comparison at `k=6` is

`t(6,0,0)^2 / 36  ?  t(6,6,6)^2 / 108`,

which is `324/36` versus `484/108`, or equivalently `972 > 484`. The
inequality holds. Same-`k` reverse at `k=6` under `ρ3` is yes.
Independently, the new axis site is `t(18,0,0) = 34`. The shared axis
site `t(16,0,0) = 28` is a `ρ3` score on this ball, not a `μ` leftover.

The pair is not leftover of `μ`: the same sites under `μ` are `16` versus `20`,
and the extra ridge-slide clause is what changes both times. The
site `(6,6,6)` has ℓ¹ norm `18`, so it is absent from `B_16(0)`. The
`B_18(0)` table is therefore not leftover of the `B_16(0)` times.

The rule is displayed, not adopted. Do not write `ρ3` into Admissibility.
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
the least-nonzero-coordinate clause, the two-unit-coordinate clause, and
the arrival function `t` are separately displayed mathematical inputs. No
axiom text is edited.

## Named Rule

Let `B_18(0) = { v ∈ Z^3 : |v|_1 ≤ 18 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_18(0)`,
`t(v)` is the least sum of `ρ3` along a directed path from `0` to `v` in
that graph.

The comparator `μ` uses only the first four clauses of `ρ3`. On the
ridge-slide hop `(1,1,1) → (2,1,1)` one has `|σ| : 3 → 3` and exactly two
`|w_i|` equal `1`, so `μ = 1` while `ρ3 = 3`. Therefore `μ` cannot price ridge slide,
and the `ρ3` scores below are not a leftover of `μ`.

## Theorem 1 — Arrivals `t(6,0,0)` And `t(6,6,6)` On `B_18(0)`

One origin Dijkstra on `B_18(0)` returns the integer arrivals

| site | `t_ρ3` |
|---|---:|
| `(6,0,0)` | `18` |
| `(6,6,6)` | `22` |

Every listed site lies in `B_18(0)`. The site `(6,6,6)` has ℓ¹ norm `18`,
so it is absent from `B_16(0)`. The pair is computed on `B_18(0)`, not
copied from a smaller-ball table and not copied from the `μ` pair
`16` versus `20`. These values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `18` is seed-exit `3` onto `(0,-1,0)`,
support-increase `1` onto `(1,-1,0)`, corridor-slide `3` onto `(1,-2,0)`,
five support-preserving cost-`1` height-`2` slides to `(6,-2,0)`,
corridor-slide `3` onto `(6,-1,0)`, and support-drop `3` onto `(6,0,0)`,
summing to `18`. A witness body walk of cost `22` is seed-exit `3` onto
`(0,0,1)`, support-increase `1` onto `(0,1,1)`, corridor-slide `3` onto
`(0,1,2)`, nine support-preserving cost-`1` face hops to `(0,6,6)`,
support-increase `1` onto `(1,6,6)`, and five support-preserving cost-`1`
body hops onto `(6,6,6)`, summing to `22`. Those walks are witnesses, not
a uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=6`

The Euclidean-normalized comparison at `k=6` is

`t(6,0,0)^2 / 36  ?  t(6,6,6)^2 / 108`,

equivalently `3 t(6,0,0)^2 ? t(6,6,6)^2`. Substituting the computed times
gives `3 · 18^2 = 972` and `22^2 = 484`, so

`972 > 484`.

Arrival per Euclidean length is larger at `(6,0,0)` than at `(6,6,6)`.
Same-`k` reverse at `k=6` under `ρ3` is yes. The comparison is displayed,
not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `ρ3` is a displayed scoring device on `B_18(0)`. Do not write
`ρ3` into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_18(0) for one named hop-cost at k=6. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_18(0) for the displayed rule ρ3 at k=6; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ρ3` among hop-costs that reverse the same-`k` pair at `k=6`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_18(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=6`.
- Any reuse of the `μ` arrival table as a substitute for the `ρ3` Dijkstra.
- Any reuse of the `B_16(0)` arrival table as a substitute for the
  radius-`18` Dijkstra.
