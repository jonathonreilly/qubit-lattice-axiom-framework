---
claim_id: ridge_slide_samek_k12_b36_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=12 under the named ridge-slide hop-cost on B_36(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ridge_slide_samek_k12_b36_2026_08_15.py
---

# Named Ridge-Slide Same-k Reverse At k=12 On B_36(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_36(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=12`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/ridge_slide_samek_k12_b36_2026_08_15.py`](../scripts/ridge_slide_samek_k12_b36_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named ridge-slide hop-cost `ρ3` is the already scored corridor-slide
rule `μ` plus cost `3` on a `3→3` hop whose destination has exactly two
absolute coordinates equal to `1` (a ridge slide). Same-`k` reverse under
`μ` holds at `k=12` (`22` versus `38`), the last `μ`-hold scale. The
residual scored here is whether `ρ3` still reverses at `k=12` on
`B_36(0)`. First display. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_36(0)`, the displayed
rule `ρ3` is

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`,

where `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`, and
`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first three clauses are seed-exit, both weights `1`, and support drop.
The fourth clause is the axis-hugging `2→2` corridor slide. The fifth
clause is the ridge slide. Those five clauses are the whole rule.

One Dijkstra from the origin on `B_36(0)` (64897 sites; 64896 nonzero) gives

`t(12,0,0) = 24`, `t(12,12,12) = 40`.

The displayed same-`k` comparison at `k=12` is

`t(12,0,0)^2 / 144  ?  t(12,12,12)^2 / 432`,

which is `576/144` versus `1600/432`, or equivalently `1728 > 1600`. The
inequality holds. Same-`k` reverse at `k=12` under `ρ3` is yes.
Independently, the axis endpoint of this ball is `t(36,0,0) = 52`. The
ball is not leftover of a larger-ball table: one origin Dijkstra is run
on this ball.

The pair is not leftover of `μ`: the same sites under `μ` are `22` versus
`38`, and the extra ridge-slide clause is what changes both arrivals. On
the ridge hop `(1,1,1) → (2,1,1)` one has `|σ| : 3 → 3` and exactly two
`|w_i| = 1`, so `μ = 1` while `ρ3 = 3`. Therefore `μ` cannot price the ridge slide,
and the `ρ3` scores below are not a leftover of `μ`. The extra clause is
live on the ball: `t(2,2,2)` is `10` under `ρ3` and `8` under `μ`, so
`10` versus `8`. The site `(12,12,12)` has ℓ¹ norm `36`, so it is absent
from `B_35(0)`. The `B_36(0)` table is therefore not leftover of a
smaller-ball table.

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

Let `B_36(0) = { v ∈ Z^3 : |v|_1 ≤ 36 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_36(0)`,
`t(v)` is the least sum of `ρ3` along a directed path from `0` to `v` in
that graph.

The comparator `μ` uses only the first four clauses of `ρ3`. On the
ridge-slide hop `(1,1,1) → (2,1,1)` one has `|σ| : 3 → 3` and exactly two
`|w_i| = 1`, so `μ = 1` while `ρ3 = 3`. Therefore `μ` cannot price the ridge slide,
and the `ρ3` scores below are not a leftover of `μ`. On the interior
`3→3` hop `(2,2,2) → (3,2,2)` the destination has no unit coordinate, so
both `μ` and `ρ3` cost `1`.

## Theorem 1 — Arrivals `t(12,0,0)` And `t(12,12,12)` On `B_36(0)`

One origin Dijkstra on `B_36(0)` returns the integer arrivals

| site | `t_ρ3` |
|---|---:|
| `(12,0,0)` | `24` |
| `(12,12,12)` | `40` |

Every listed site lies in `B_36(0)`. The site `(12,12,12)` has ℓ¹ norm `36`,
so it is absent from `B_35(0)`. The pair is computed on `B_36(0)`, not
copied from a larger-ball table and not copied from the `μ` pair
`22` versus `38`. These values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `24` is seed-exit `3` onto `(1,0,0)`,
leave-axis `1` onto `(1,1,0)`, hugging corridor-slide `3` onto `(2,1,0)`,
non-hugging face hop `1` onto `(2,2,0)`, ten support-preserving
cost-`1` face hops to `(12,2,0)`, hugging slide `3` onto `(12,1,0)`, and
support-drop `3` onto `(12,0,0)`, summing to `24`. That walk is a witness
of cost `24`, not a uniqueness claim.

A witness body walk of cost `40` is the same prefix of cost `8` to
`(2,2,0)`, ten cost-`1` face hops to `(12,2,0)`, ten cost-`1` face
hops to `(12,12,0)`, enter-body `1` onto `(12,12,1)`, and eleven
support-preserving cost-`1` body hops to `(12,12,12)`, summing to `40`.
Those last hops have dest with only one absolute coordinate equal to `1`
or with none, so they are not ridge slides. That walk is a witness of
cost `40`, not a uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=12`

The Euclidean-normalized comparison at `k=12` is

`t(12,0,0)^2 / 144  ?  t(12,12,12)^2 / 432`,

equivalently `3 t(12,0,0)^2 ? t(12,12,12)^2`. Substituting the computed times
gives `3 · 24^2 = 1728` and `40^2 = 1600`, so

`1728 > 1600` is true; `1728 > 1600` holds.

Arrival per Euclidean length is larger at `(12,0,0)` than at `(12,12,12)`.
Same-`k` reverse at `k=12` under `ρ3` is yes. The comparison is displayed,
not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `ρ3` is a displayed scoring device on `B_36(0)`. Do not write `ρ3`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_36(0) for one named hop-cost at k=12. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_36(0) for the displayed rule ρ3 at k=12; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ρ3` among hop-costs that reverse the same-`k` pair at `k=12`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_36(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=12`.
- Any reuse of the `μ` arrival table as a substitute for the `ρ3` Dijkstra.
- Any reuse of a larger-ball arrival table as a substitute for the
  radius-`36` Dijkstra.
- Membership of `ρ3` as a physical hop-cost. Reverse at `k=12` on this ball
  is a displayed comparison, not an adoption.
