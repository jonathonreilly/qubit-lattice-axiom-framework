---
claim_id: ridge_slide_samek_k4_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=4 under the named ridge-slide hop-cost on B_12(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ridge_slide_samek_k4_b12_2026_08_15.py
---

# Named Ridge-Slide Same-k Reverse At k=4 On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_12(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=4`. First display of this clause at this `k`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/ridge_slide_samek_k4_b12_2026_08_15.py`](../scripts/ridge_slide_samek_k4_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named ridge-slide hop-cost `ρ3` is scored independently on `B_12(0)`.
The ball is not leftover of a larger-ball table: one origin Dijkstra is run
on this ball.

Under the corridor-slide rule `μ`, the same-`k` pair at `k=4` is `12` versus `14`.
Neighboring `k=3` on this ball already reverses under `ρ3`.
The residual scored here is whether `ρ3` still reverses at `k=4` after those
ridge `3→3` hops whose destination has exactly two coordinates of absolute
value `1` are priced at `3`.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_12(0)`, let `ν` be the
support-drop rule that costs `3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or
`|σ_w| < |σ_v|`, else `1`. Let `μ` be the corridor-slide rule

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`.

The displayed rule `ρ3` is

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

The extra clause is a ridge slide: both ends have support `3`, and the
destination has exactly two unit coordinates. It is not the all-`3→3`
body-slide tax. Uniqueness is not claimed.

One Dijkstra from the origin on `B_12(0)` (2625 sites; 2624 nonzero) gives

`t(4,0,0) = 12`, `t(4,4,4) = 16`.

The displayed same-`k` comparison at `k=4` is

`t(4,0,0)^2 / 16  ?  t(4,4,4)^2 / 48`,

which is `144/16` versus `256/48`, or equivalently `432 > 256`. The
inequality holds. Same-`k` reverse holds at `k=4`. The
displayed rule is not adopted. Independently, the axis
endpoint of this ball is `t(12,0,0) = 28`.

The `k=4` pair does not coincide with the `μ` pair on the same ball,
because a least-cost walk to `(4,4,4)` uses a ridge `3→3` hop. The
extra clause is live on the ball: `t(4,4,4)` is `16` under `ρ3` and `14`
under `μ`, so `16` versus `14`. Independently, `t(2,2,2)` is `10` under
`ρ3` and `8` under `μ`, so `10` versus `8`. The scores are therefore not
leftover of a larger-ball table.

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

Let `B_12(0) = { v ∈ Z^3 : |v|_1 ≤ 12 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_12(0)`,
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

## Theorem 1 — Arrivals `t(4,0,0)` And `t(4,4,4)` On `B_12(0)`

One origin Dijkstra on `B_12(0)` returns the integer arrivals

| site | `t_ρ3` |
|---|---:|
| `(4,0,0)` | `12` |
| `(4,4,4)` | `16` |

Every listed site lies in `B_12(0)`. The pair is computed on `B_12(0)`, not
copied from a larger-ball table. These values are Dijkstra outputs, not
fitted scalars.

A witness walk to `(4,0,0)` is seed-exit of cost `3` onto `(1,0,0)` and
three both-weights-`1` hops of cost `3` onto `(4,0,0)`, summing to `12`.
A witness walk to `(4,4,4)` is seed-exit `3` onto `(1,0,0)`, body `1→2`
of cost `1` onto `(1,1,0)`, `2→3` of cost `1` onto `(1,1,1)`, ridge `3→3`
of cost `3` onto `(2,1,1)`, two support-preserving cost-`1` hops onto
`(2,2,2)`, and six interior `3→3` hops of cost `1` onto `(4,4,4)`,
summing to `16`. Those walks are witnesses, not a uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=4`

The Euclidean-normalized comparison at `k=4` is

`t(4,0,0)^2 / 16  ?  t(4,4,4)^2 / 48`,

equivalently `3 t(4,0,0)^2 ? t(4,4,4)^2`. Substituting the computed times
gives `3 · 12^2 = 432` and `16^2 = 256`, so

`432 > 256` is true; `432 > 256` holds.

Arrival per Euclidean length is larger at `(4,0,0)` than at `(4,4,4)`.
Same-`k` reverse at `k=4` is yes. The comparison is
displayed, not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `ρ3` is a displayed scoring device on `B_12(0)`. Do not write `ρ3`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_12(0) for one named hop-cost at k=4. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_12(0) for the displayed rule ρ3 at k=4; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ρ3` among hop-costs that score the same-`k` pair at `k=4`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_12(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=4`.
- Any reuse of a larger-ball arrival table as a substitute for the
  radius-`12` Dijkstra.
- Membership of `ρ3` as a physical hop-cost. Reverse at `k=4` on this ball
  is a displayed comparison, not an adoption.
