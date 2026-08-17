---
claim_id: ridge_slide_samek_k11_b33_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=11 under the named ridge-slide hop-cost on B_33(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ridge_slide_samek_k11_b33_2026_08_15.py
---

# Named Ridge-Slide Same-k Reverse At k=11 On B_33(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_33(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=11`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/ridge_slide_samek_k11_b33_2026_08_15.py`](../scripts/ridge_slide_samek_k11_b33_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named ridge-slide hop-cost `ρ3` is scored independently on `B_33(0)`.
The ball is not leftover of a larger-ball table: one origin Dijkstra is run
on this ball. Same-`k` reverse under `ρ3` is already scored at `k=10` and
`k=12`. The residual scored here is whether `ρ3` still reverses at `k=11`
on `B_33(0)`. First display. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_33(0)`, let `ν` be the
support-drop rule that costs `3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or
`|σ_w| < |σ_v|`, else `1`. Let `μ` be the corridor-slide rule

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`.

The displayed rule `ρ3` is

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

The extra clause is a ridge slide: both ends have support `3`, and the
destination has exactly two unit coordinates. It is not the all-`3→3`
body-slide tax.

One Dijkstra from the origin on `B_33(0)` (50183 sites; 50182 nonzero) gives

`t(11,0,0) = 23`, `t(11,11,11) = 37`.

The displayed same-`k` comparison at `k=11` is

`t(11,0,0)^2 / 121  ?  t(11,11,11)^2 / 363`,

which is `529/121` versus `1369/363`, or equivalently `1587 > 1369`. The
inequality holds. Same-`k` reverse holds at `k=11`. The
displayed rule is not adopted. Independently, the axis
endpoint of this ball is `t(33,0,0) = 49`. The shared axis site
`t(30,0,0) = 42` is a `ρ3` score on this ball, not a `μ` leftover.

The pair is not leftover of `μ`: the same sites under `μ` are `21` versus
`35`, and the extra ridge-slide clause is what changes both arrivals. On
the ridge hop `(1,1,1) → (2,1,1)` one has `|σ| : 3 → 3` and exactly two
`|w_i| = 1`, so `μ = 1` while `ρ3 = 3`. Therefore `μ` cannot price the ridge slide,
and the `ρ3` scores below are not a leftover of `μ`. The extra clause is
live on the ball: `t(2,2,2)` is `10` under `ρ3` and `8` under `μ`, so
`10` versus `8`. The site `(11,11,11)` has ℓ¹ norm `33`, so it is absent
from `B_30(0)`. The `B_33(0)` table is therefore not leftover of the `B_30(0)` times.

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
the least-nonzero-coordinate clause, the two-unit-height ridge clause, and
the arrival function `t` are separately displayed mathematical inputs. No
axiom text is edited.

## Named Rule

Let `B_33(0) = { v ∈ Z^3 : |v|_1 ≤ 33 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_33(0)`,
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

## Theorem 1 — Arrivals `t(11,0,0)` And `t(11,11,11)` On `B_33(0)`

One origin Dijkstra on `B_33(0)` returns the integer arrivals

| site | `t_ρ3` |
|---|---:|
| `(11,0,0)` | `23` |
| `(11,11,11)` | `37` |

Every listed site lies in `B_33(0)`. The site `(11,11,11)` has ℓ¹ norm `33`,
so it is absent from `B_30(0)`. The pair is computed on `B_33(0)`, not
copied from a smaller-ball table and not copied from the `μ` pair
`21` versus `35`. These values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `23` is seed-exit `3` onto `(1,0,0)`,
leave-axis `1` onto `(1,1,0)`, hugging corridor-slide `3` onto `(2,1,0)`,
non-hugging face hop `1` onto `(2,2,0)`, nine support-preserving
cost-`1` face hops to `(11,2,0)`, hugging slide `3` onto `(11,1,0)`, and
support-drop `3` onto `(11,0,0)`, summing to `23`. That walk is a witness
of cost `23`, not a uniqueness claim.

A witness body walk of cost `37` is the same prefix of cost `8` to
`(2,2,0)`, nine cost-`1` face hops to `(11,2,0)`, nine cost-`1` face
hops to `(11,11,0)`, enter-body `1` onto `(11,11,1)`, and ten
support-preserving cost-`1` body hops to `(11,11,11)`, summing to `37`.
Those last hops have dest with only one absolute coordinate equal to `1`,
so they are not ridge slides. That walk is a witness of cost `37`, not a
uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=11`

The Euclidean-normalized comparison at `k=11` is

`t(11,0,0)^2 / 121  ?  t(11,11,11)^2 / 363`,

equivalently `3 t(11,0,0)^2 ? t(11,11,11)^2`. Substituting the computed times
gives `3 · 23^2 = 1587` and `37^2 = 1369`, so

`1587 > 1369` is true; `1587 > 1369` holds.

Arrival per Euclidean length is larger at `(11,0,0)` than at `(11,11,11)`.
Same-`k` reverse at `k=11` is yes. The comparison is
displayed, not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `ρ3` is a displayed scoring device on `B_33(0)`. Do not write `ρ3`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_33(0) for one named hop-cost at k=11. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_33(0) for the displayed rule ρ3 at k=11; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ρ3` among hop-costs that score the same-`k` pair at `k=11`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_33(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=11`.
- Any reuse of a larger-ball arrival table as a substitute for the
  radius-`33` Dijkstra.
- Any reuse of the `μ` arrival table as a substitute for the `ρ3` Dijkstra.
- Membership of `ρ3` as a physical hop-cost. Reverse at `k=11` on this ball
  is a displayed comparison, not an adoption.
