---
claim_id: ridge_slide_samek_k5_b16_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=5 under the named ridge-slide hop-cost on B_16(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ridge_slide_samek_k5_b16_2026_08_15.py
---

# Named Ridge-Slide Same-k Reverse At k=5 On B_16(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_16(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=5`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/ridge_slide_samek_k5_b16_2026_08_15.py`](../scripts/ridge_slide_samek_k5_b16_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named ridge-slide hop-cost `ρ3` already reverse-holds at neighboring
`k`. The residual scored here is the first display of the same named
rule on `B_16(0)` at `k=5`. The ball is not leftover of a larger-ball
table: one origin Dijkstra is run on this ball.

Under the corridor-slide rule `μ`, the same-`k` pair at `k=5` is `15` versus `17`.
The residual is whether `ρ3` still reverses at `k=5` after
those ridge `3→3` hops whose destination has exactly two coordinates of
absolute value `1` are priced at `3`.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_16(0)`, let `ν` be
the support-drop rule that costs `3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or
`|σ_w| < |σ_v|`, else `1`. Let `μ` be the corridor-slide rule

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`.

The displayed rule `ρ3` is

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

The extra clause is a ridge slide: both ends have support `3`, and the
destination has exactly two unit coordinates. It is not the all-`3→3`
body-slide tax. Uniqueness is not claimed.

One Dijkstra from the origin on `B_16(0)` (6017 sites; 6016 nonzero) gives

`t(5,0,0) = 15`, `t(5,5,5) = 19`.

The displayed same-`k` comparison at `k=5` is

`t(5,0,0)^2 / 25  ?  t(5,5,5)^2 / 75`,

which is `225/25` versus `361/75`, or equivalently `675 > 361`. The
inequality holds. Same-`k` reverse holds at `k=5`. The
displayed rule is not adopted. Independently, the axis
endpoint of this ball is `t(16,0,0) = 32`.

The `k=5` axis arrival coincides with the `μ` axis arrival on the same
ball. The body arrival does not: a least-cost walk to `(5,5,5)` uses a
ridge `3→3` hop. The extra clause is live on the ball: `t(5,5,5)` is `19`
under `ρ3` and `17` under `μ`, so `19` versus `17`. Independently,
`t(2,2,2)` is `10` under `ρ3` and `8` under `μ`, so `10` versus `8`. The
scores are therefore not leftover of a larger-ball table.

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
and the arrival function `t` are separately displayed mathematical inputs.
No axiom text is edited.

## Named Rule

Let `B_16(0) = { v ∈ Z^3 : |v|_1 ≤ 16 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_16(0)`,
`t(v)` is the least sum of `ρ3` along a directed path from `0` to `v` in
that graph.

The comparator `μ` uses the three support-drop clauses and the
axis-hugging `2→2` slide. On the ridge slide `(1,1,1) → (2,1,1)` one has
`|σ_v|=|σ_w|=3` and exactly two `|w_i|=1`, so `μ = 1` while `ρ3 = 3`.
Therefore `μ` cannot price the ridge slide. The same extra clause prices
the corridor hop `(1,-1,-1) → (2,-1,-1)` at `3`. On the body hop
`(1,0,0) → (1,1,0)` both `μ` and `ρ3` cost `1`. On the interior `3→3`
hop `(2,2,2) → (3,2,2)` the destination has no unit coordinate, so both
`μ` and `ρ3` cost `1`.

## Theorem 1 — Arrivals `t(5,0,0)` And `t(5,5,5)` On `B_16(0)`

One origin Dijkstra on `B_16(0)` returns the integer arrivals

| site | `t_ρ3` |
|---|---:|
| `(5,0,0)` | `15` |
| `(5,5,5)` | `19` |

Every listed site lies in `B_16(0)`. The pair is computed on `B_16(0)`, not
copied from a larger-ball table. These values are Dijkstra outputs, not
fitted scalars.

A witness walk to `(5,0,0)` is seed-exit of cost `3` onto `(1,0,0)` and
four both-weights-`1` hops of cost `3` onto `(5,0,0)`, summing to `15`.
A witness walk to `(5,5,5)` is seed-exit `3` onto `(1,0,0)`, body `1→2`
of cost `1` onto `(1,1,0)`, `2→3` of cost `1` onto `(1,1,1)`, ridge
`3→3` of cost `3` onto `(2,1,1)`, then eleven support-preserving cost-`1`
hops onto `(5,5,5)`, summing to `19`. Those walks are witnesses, not a
uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=5`

The Euclidean-normalized comparison at `k=5` is

`t(5,0,0)^2 / 25  ?  t(5,5,5)^2 / 75`,

equivalently `3 t(5,0,0)^2 ? t(5,5,5)^2`. Substituting the computed times
gives `3 · 15^2 = 675` and `19^2 = 361`, so

`675 > 361` is true; `675 > 361` holds.

Arrival per Euclidean length is larger at `(5,0,0)` than at `(5,5,5)`.
Same-`k` reverse at `k=5` is yes. The comparison is
displayed, not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `ρ3` is a displayed scoring device on `B_16(0)`. Do not write `ρ3`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_16(0) for one named hop-cost at k=5. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_16(0) for the displayed rule ρ3 at k=5; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ρ3` among hop-costs that score the same-`k` pair at `k=5`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_16(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=5`.
- Any reuse of a larger-ball arrival table as a substitute for the
  radius-`16` Dijkstra.
- Membership of `ρ3` as a physical hop-cost. Reverse at `k=5` on this ball
  is a displayed comparison, not an adoption.
