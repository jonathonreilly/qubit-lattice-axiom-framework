---
claim_id: plane_hug_samek_k1_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=1 under the named plane-hug hop-cost on B_6(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/plane_hug_samek_k1_b6_2026_08_15.py
---

# Named Plane-Hug Same-k Reverse At k=1 On B_6(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_6(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=1`. First display of `π`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/plane_hug_samek_k1_b6_2026_08_15.py`](../scripts/plane_hug_samek_k1_b6_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named plane-hug hop-cost `π` is scored independently on `B_6(0)`.
The ball is not leftover of a larger-ball table: one origin Dijkstra is run
on this ball.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_6(0)`, let `ν` be the
support-drop rule that costs `3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or
`|σ_w| < |σ_v|`, else `1`. Let `μ` be the corridor-slide rule

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`.

The displayed rule `π` is

`π(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and
`min_i |w_i| = 1)`, else `1`.

The extra clause is a plane-hugging `3→3` slide: both ends have support
`3`, and the destination has one or more unit coordinates. A comparator
`ρ3` taxes only a support-`3` destination with exactly two unit
coordinates; `π` also taxes a `3→3` hop whose destination has a single
unit coordinate. Uniqueness is not claimed.

`π` does not price the body `1→2` hop. On `(1,0,0) → (1,1,0)` one has
`|σ| : 1 → 2`, so `π = 1`. The residual is whether `π` still reverses at
`k=1`.

One Dijkstra from the origin on `B_6(0)` (377 sites; 376 nonzero) gives

`t(1,0,0) = 3`, `t(1,1,1) = 5`.

The displayed same-`k` comparison at `k=1` is

`t(1,0,0)^2 / 1  ?  t(1,1,1)^2 / 3`,

which is `9/1` versus `25/3`, or equivalently `27 > 25`. The inequality
holds. Same-`k` reverse holds at `k=1`. The small-`k` bar is kept. The
displayed rule is not adopted. Independently, the axis
endpoint of this ball is `t(6,0,0) = 18`.

The `k=1` pair coincides with the `μ` pair on the same ball, because a
least-cost walk to `(1,1,1)` never needs a plane-hugging `3→3` slide. The
extra clause is live on the ball: `t(2,1,1)` is `8` under `π`. The scores
are therefore not leftover of a larger-ball table.

The rule is displayed, not adopted. Do not write `π` into Admissibility.
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
`t(v)` is the least sum of `π` along a directed path from `0` to `v` in
that graph.

The comparator `μ` uses the three support-drop clauses and the
axis-hugging `2→2` slide. On the plane-hugging slide
`(2,1,1) → (2,2,1)` one has `|σ_v|=|σ_w|=3` and `min_i |w_i|=1`, so
`μ = 1` and `ρ3 = 1` while `π = 3`. Therefore `μ` and `ρ3` cannot price the plane-hugging 3-slide.
On the two-unit destination hop `(1,1,1) → (2,1,1)` both `ρ3` and `π`
cost `3` while `μ` costs `1`. On the body hop `(1,0,0) → (1,1,0)` both
`μ` and `π` cost `1`.

## Theorem 1 — Arrivals `t(1,0,0)` And `t(1,1,1)` On `B_6(0)`

One origin Dijkstra on `B_6(0)` returns the integer arrivals

| site | `t_π` |
|---|---:|
| `(1,0,0)` | `3` |
| `(1,1,1)` | `5` |
| `(2,1,1)` | `8` |

Every listed site lies in `B_6(0)`. The pair is computed on `B_6(0)`, not
copied from a larger-ball table. These values are Dijkstra outputs, not
fitted scalars.

A witness walk to `(1,0,0)` is the seed-exit of cost `3`. A witness walk
to `(1,1,1)` is seed-exit `3` onto `(1,0,0)`, body `1→2` of cost `1` onto
`(1,1,0)`, and `2→3` of cost `1` onto `(1,1,1)`, summing to `5`. A witness
walk to `(2,1,1)` is that same walk of cost `5` followed by the `3→3` hop
`(1,1,1) → (2,1,1)` of cost `3`, summing to `8`. Those walks are
witnesses, not a uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=1`

The Euclidean-normalized comparison at `k=1` is

`t(1,0,0)^2 / 1  ?  t(1,1,1)^2 / 3`,

equivalently `3 t(1,0,0)^2 ? t(1,1,1)^2`. Substituting the computed times
gives `3 · 3^2 = 27` and `5^2 = 25`, so

`27 > 25` is true; `27 > 25` holds.

Arrival per Euclidean length is larger at `(1,0,0)` than at `(1,1,1)`.
Same-`k` reverse at `k=1` is yes. The small-`k` bar is kept. The
displayed rule is not adopted. The comparison is
displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `π` is a displayed scoring device on `B_6(0)`. Do not write `π`
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
conditional_surface_status: "exact on B_6(0) for the displayed rule π at k=1; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `π` among hop-costs that score the same-`k` pair at `k=1`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_6(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=1`.
- Any reuse of a larger-ball arrival table as a substitute for the
  radius-`6` Dijkstra.
- Membership of `π` as a physical hop-cost. The small-`k` bar is kept
  on this ball; that is a displayed comparison, not an adoption.
