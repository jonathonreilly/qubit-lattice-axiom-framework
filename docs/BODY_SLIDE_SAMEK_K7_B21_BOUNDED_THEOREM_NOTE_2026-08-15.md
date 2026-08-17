---
claim_id: body_slide_samek_k7_b21_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=7 under the named body-slide hop-cost on B_21(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/body_slide_samek_k7_b21_2026_08_15.py
---

# Named Body-Slide Same-k Reverse At k=7 On B_21(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_21(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=7`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/body_slide_samek_k7_b21_2026_08_15.py`](../scripts/body_slide_samek_k7_b21_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named body-slide hop-cost `β` is scored on `B_21(0)`. The ball is not
leftover of a smaller-ball table: one origin Dijkstra is run on this ball,
and the site `(7,7,7)` is absent from `B_18(0)`.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_21(0)`, the displayed
support-drop rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The named corridor-slide rule `μ` is

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`.

The displayed body-slide rule `β` is

`β(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3)`, else `1`.

The new clause is body slide: both weights `3`. Uniqueness is not claimed.

One Dijkstra from the origin on `B_21(0)` (13287 sites; 13286 nonzero) gives

`t(7,0,0) = 19`, `t(7,7,7) = 37`.

Those arrivals are not the previously scored corridor-slide / all-face-slide
pair `17` versus `23` at this same scale. On the body-slide hop
`(1,1,1) → (2,1,1)` one has `|σ| : 3 → 3`, so `μ = 1` and `φ = 1` while
`β = 3`. Therefore `μ` and `φ` cannot price body slide, and the `β`
scores below are not a leftover of those rules.

The displayed same-`k` comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

which is `361/49` versus `1369/147`, or equivalently `1083 > 1369`. The
inequality does not hold. Same-`k` reverse at `k=7` does not survive the
body-slide clause. Independently, the new axis site is `t(21,0,0) = 37`.

The rule is displayed, not adopted. Do not write `β` into Admissibility.
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

Let `B_21(0) = { v ∈ Z^3 : |v|_1 ≤ 21 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_21(0)`,
`t(v)` is the least sum of `β` along a directed path from `0` to `v` in
that graph.

The site `(7,0,0)` has ℓ¹ norm `7` and therefore also lies in `B_18(0)`.
The site `(7,7,7)` has ℓ¹ norm `21`, so it is absent from `B_18(0)`. The
`B_21(0)` table is therefore not leftover of the `B_18(0)` times.

## Theorem 1 — Arrivals `t(7,0,0)` And `t(7,7,7)` On `B_21(0)`

One origin Dijkstra on `B_21(0)` returns the integer arrivals

| site | `t_β` |
|---|---:|
| `(7,0,0)` | `19` |
| `(7,7,7)` | `37` |

Every listed site lies in `B_21(0)`. The site `(7,7,7)` has ℓ¹ norm `21`,
so it is absent from `B_18(0)`. The pair is computed on `B_21(0)`, not
copied from a smaller-ball table. These values are Dijkstra outputs, not
fitted scalars.

## Theorem 2 — Reverse At The Same-`k` Scale `k=7`

The Euclidean-normalized comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

equivalently `3 t(7,0,0)^2 ? t(7,7,7)^2`. Substituting the computed times
gives `3 · 19^2 = 1083` and `37^2 = 1369`, so

`1083 > 1369` is false; `1083 < 1369`.

Arrival per Euclidean length is smaller at `(7,0,0)` than at `(7,7,7)`.
Same-`k` reverse at `k=7` is no. The comparison is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `β` is a displayed scoring device on `B_21(0)`. Do not write `β`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_21(0) for one named hop-cost at k=7. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_21(0) for the displayed rule β at k=7; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `β` among hop-costs that reverse the same-`k` pair at `k=7`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_21(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=7`.
- Any reuse of a smaller-ball arrival table as a substitute for the
  radius-`21` Dijkstra.
- Any adoption of `β` as the corridor-slide rule `μ` or the all-face-slide
  rule `φ`.
