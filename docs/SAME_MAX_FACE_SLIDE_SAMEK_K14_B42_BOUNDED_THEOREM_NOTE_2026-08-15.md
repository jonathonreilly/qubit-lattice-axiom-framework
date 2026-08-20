---
claim_id: same_max_face_slide_samek_k14_b42_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=14 under the named same-max face-slide hop-cost on B_42(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/same_max_face_slide_samek_k14_b42_2026_08_15.py
---

# Named Same-Max Face-Slide Same-`k` Reverse At `k=14` On `B_42(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_42(0)`,
scored only for the same-`k` pair `t(14,0,0)` versus `t(14,14,14)`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/same_max_face_slide_samek_k14_b42_2026_08_15.py`](../scripts/same_max_face_slide_samek_k14_b42_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_42(0)`, the stacked
rules `ν`, `μ`, `ρ3`, and `ω` are

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
`|w_i|` equals `1)`, else `1`;

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`;

`ω(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|)`, else `1`.

The displayed same-max face-slide rule `ψ` is `ω` plus cost `3` on a
`2→2` hop whose destination max absolute coordinate equals the source max
(same-max face slide, not box-growth):

`ψ(v→w) = 3` if `ω` would be `3` or `(|σ_v|=|σ_w|=2` and
`max_i |w_i| = max_i |v_i|)`, else `1`.

Those clauses are the whole rule. Uniqueness is not claimed. This note is
the first display of same-`k` reverse under `ψ` at the `k=14` wall, the
body site of ℓ¹-norm `42`.

The same-max face-slide hop `(2,1,0) → (2,2,0)` does fire: `|σ|=2→2` and
`max |w_i|=2 = max |v_i|=2`, so `ψ=3`. Independently that hop is not
leftover of `ω`: `ω((2,1,0)→(2,2,0))=1`. The out-face box-growth hop
`(1,1,0) → (2,1,0)` already has `ω=3` and therefore `ψ=3`. The same-max
clause is live in the arrival table: `t(2,2,0) = 10`.

One Dijkstra from the origin on `B_42(0)` (102425 sites; 102424 nonzero)
returns

| site | `t_ψ` |
|---|---:|
| `(14,0,0)` | `30` |
| `(14,14,14)` | `46` |

The same-`k` comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

equivalently `3 t(14,0,0)^2 ? t(14,14,14)^2`. Substituting the computed times
gives `3 · 30^2 = 2700` and `46^2 = 2116`, so `2700 > 2116`. Same-`k`
reverse at `k=14` is yes. Independently the same table has `t(1,0,0) = 3`
and `t(1,1,1) = 5`.

The site `(14,14,14)` has ℓ¹ norm `42`, so it is absent from `B_39(0)`.
The `B_42(0)` table is therefore not leftover of a radius-`39` table.

A cheapest `ψ` walk to `(14,14,14)` uses no same-max `2→2` face-slide hop,
so the body arrival stays `46`. A cheapest `ψ` walk to `(14,0,0)` likewise
uses none, so the axis arrival stays `30`. The named rule is still not a
leftover of `ω`, because the same-max hop is live on the ball.

The rule is displayed, not adopted. Do not write `ψ` into Admissibility.
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
none of the hop costs. The integers `3` and `1`, the support-size and
max-coordinate clauses, and the arrival function `t` are separately displayed
mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_42(0) = { v ∈ Z^3 : |v|_1 ≤ 42 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_42(0)`,
`t(v)` is the least sum of `ψ` along a directed path from `0` to `v` in
that graph.

The first `ν` clause is seed-exit. The second is both weights `1`. The third
is support drop. The `μ` addendum taxes a `2→2` hop whose destination still
touches a unit coordinate. The `ρ3` addendum taxes a `3→3` hop whose
destination has exactly two unit coordinates. The `ω` addendum taxes a
`2→2` hop that grows the coordinate box on a face. The `ψ` addendum taxes
a `2→2` hop that slides on a face at constant max absolute coordinate.

## Theorem 1 — Arrivals At `k=14` Under `ψ`

One origin Dijkstra on `B_42(0)` returns `t(14,0,0) = 30` and
`t(14,14,14) = 46`. Both sites lie in `B_42(0)`. These values are Dijkstra
outputs, not fitted scalars.

A witness axis walk of cost `30` is seed-exit `3` onto `(1,0,0)`,
leave-axis `1` onto `(1,1,0)`, enter-body `1` onto `(1,1,1)`, ridge-slide
`3` onto `(2,1,1)`, support-preserving cost-`1` hop onto `(2,2,1)`, twelve
support-preserving cost-`1` body hops to `(14,2,1)`, ridge-slide `3` onto
`(14,1,1)`, support-drop `3` onto `(14,1,0)`, and support-drop `3` onto
`(14,0,0)`, summing to `30`. That walk uses no same-max `2→2` face-slide
hop. It is a witness of cost `30`, not a uniqueness claim. The pure axis
1-skeleton walk costs `42` and is not cheapest.

A witness body walk of cost `46` is the same prefix of cost `9` to
`(2,2,1)`, twelve cost-`1` body hops to `(14,2,1)`, twelve cost-`1` body
hops to `(14,14,1)`, and thirteen support-preserving cost-`1` body hops to
`(14,14,14)`, summing to `46`. Those last hops have dest with only one
absolute coordinate equal to `1`, or with all three coordinates large, so
they are not unit-height ridges, not out-face `2→2` grows, and not
same-max `2→2` slides. That walk is a witness of cost `46`, not a
uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Pair `k=14`

The Euclidean-normalized comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`.

The computed integers give `2700 > 2116`. Arrival per Euclidean length is
larger at `(14,0,0)` than at `(14,14,14)`. Same-`k` reverse at `k=14`
under `ψ` is yes. The comparison is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ψ` is a displayed scoring device on `B_42(0)`. Do not write `ψ`
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
conditional_surface_status: "exact on B_42(0) for the displayed rule ψ at k=14; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ψ` among hop-costs that reverse any same-`k` pair.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_42(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=14`.
- Any adoption of `ψ` as an admissibility rule.
- Any face-reverse score.
