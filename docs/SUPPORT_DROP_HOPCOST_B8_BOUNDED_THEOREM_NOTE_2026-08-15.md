---
claim_id: support_drop_hopcost_b8_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_8(0), the named support-drop hop-cost is scored for diamond reverse and for var(|v|_2/t) vs ℓ¹. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_hopcost_b8_2026_08_15.py
---

# Named Support-Drop Hop-Cost On B_8(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_8(0)`,
scored only for diamond reverse at `(4,0,0)` versus `(2,2,2)` and for
population variance of `|v|_2/t` against unit-cost ℓ¹ arrival.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_hopcost_b8_2026_08_15.py`](../scripts/support_drop_hopcost_b8_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The same named support-drop hop-cost `ν` already scored on `B_6(0)` is
scored independently on `B_8(0)`. The ball is not a leftover of the
radius-`6` arrival table: `t(6,0,0)` on this ball is not the radius-`6`
value, and `t(8,0,0)` is a new site.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_8(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not
claimed.

One Dijkstra from the origin on `B_8(0)` (833 sites; 832 nonzero) gives

`t(4,0,0) = 10`, `t(6,0,0) = 12`, `t(8,0,0) = 16`, `t(2,2,2) = 8`.

Then `12 t(4,0,0)^2 = 1200` and `16 t(2,2,2)^2 = 1024`, so

`12 t(4,0,0)^2 > 16 t(2,2,2)^2`.

The diamond comparison still reverses. Population variances of `|v|_2/t` on
`B_8(0) \ {0}` are

`var_ν = 0.00634967516547`, `var_ℓ¹ = 0.01133940495651`.

So `var_ν < var_ℓ¹`. The `ν` variance is strictly smaller.

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

Let `B_8(0) = { v ∈ Z^3 : |v|_1 ≤ 8 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_8(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph. Unit-cost ℓ¹ arrival is the closed form `t_ℓ¹(v) = |v|_1`; it
is not obtained from a second Dijkstra.

On the smaller ball `B_6(0)` the same local rule gives `t(6,0,0) = 14`,
because `(6,1,0)` lies outside that ball and the only in-ball last step onto
`(6,0,0)` is the axis hop from `(5,0,0)`. On `B_8(0)` the site `(6,1,0)`
is interior, the support-drop last step is available, and
`t(6,0,0) = 12`. The site `(8,0,0)` is not in `B_6(0)` at all. The
`B_8(0)` table is therefore not leftover of the `B_6(0)` times.

## Theorem 1 — Arrivals And Diamond Reverse

One origin Dijkstra on `B_8(0)` returns the integer arrivals

| site | `t_ν` | `t_ℓ¹` |
|---|---:|---:|
| `(4,0,0)` | `10` | `4` |
| `(6,0,0)` | `12` | `6` |
| `(8,0,0)` | `16` | `8` |
| `(2,2,2)` | `8` | `6` |

Witnessing paths of those `ν`-costs exist. The walk

`0 → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (4,0,0)`

has hop-costs `3,1,1,1,1,3` and sum `10`. The walk

`0 → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (2,2,1) → (2,2,2)`

has hop-costs `3,1,1,1,1,1` and sum `8`. The walk

`0 → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (6,0,0)`

has hop-costs `3,1,1,1,1,1,1,3` and sum `12`. The only in-ball neighbor of
`(8,0,0)` is `(7,0,0)`, so the last hop is the both-weights-`1` axis step
of cost `3`. The walk

`0 → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (7,1,0) → (7,0,0) → (8,0,0)`

has hop-costs `3,1,1,1,1,1,1,1,3,3` and sum `16`.

The Euclidean-normalized comparison is `t^2 / |v|_2^2`, equivalently

`12 t(4,0,0)^2 ? 16 t(2,2,2)^2`.

Substituting the computed times gives `1200 > 1024`. The inequality
reverses: arrival per Euclidean length is larger at `(4,0,0)` than at
`(2,2,2)`. Under unit-cost ℓ¹ the same comparison is `192 > 576`, which
fails.

## Theorem 2 — Population Variance Of `|v|_2/t`

On the 832 nonzero sites of `B_8(0)`, let `r(v) = |v|_2 / t(v)` and write
population variance `(1/n) ∑ (r − mean)^2`. The runner computes

`var_ν = 0.00634967516547`, `var_ℓ¹ = 0.01133940495651`.

So `var_ν < var_ℓ¹`. The named rule is more nearly Euclidean-isotropic
than unit-cost ℓ¹ on this ball, in the population-variance sense stated
here. No uniqueness among hop-costs is claimed.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_8(0)`. Do not write `ν`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
diamond reverse or with variance below ℓ¹.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer arrivals and a population-variance comparison on the finite ball B_8(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_8(0) for the displayed rule ν; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ν` among hop-costs that reverse the diamond or beat ℓ¹
  variance.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_8(0)`.
- Any reuse of the `B_6(0)` arrival table as a substitute for the
  radius-`8` Dijkstra.
