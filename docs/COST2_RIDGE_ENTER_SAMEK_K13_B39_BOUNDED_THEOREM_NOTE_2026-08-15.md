---
claim_id: cost2_ridge_enter_samek_k13_b39_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=13 under the named cost-2 ridge-enter hop-cost on B_39(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost2_ridge_enter_samek_k13_b39_2026_08_15.py
---

# Named Cost-2 Ridge-Enter Same-k Reverse At k=13 On B_39(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_39(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=13`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/cost2_ridge_enter_samek_k13_b39_2026_08_15.py`](../scripts/cost2_ridge_enter_samek_k13_b39_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named cost-2 ridge-enter hop-cost `c2` is scored on `B_39(0)` by one
Dijkstra from the origin. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_39(0)`, the displayed
rule `c2` is the ridge-slide rule `ρ3` except that a ridge-enter hop is
priced at `2` rather than `3`:

`c2(v→w) = 3` if `ρ3` would be `3`,
else `2` if `|σ_v|=2` and `|σ_w|=3` and exactly two `|w_i|` equal `1`,
else `1`.

Here `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1`), else `1`; and `μ(v→w) = 3` if `ν` would be `3` or
`(|σ_v|=|σ_w|=2` and the least nonzero `|w_i|` equals `1`), else `1`; and
`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`.

Equivalently, `c2(v→w) = 3` on seed-exit, axis 1-skeleton, support drop,
corridor-slide (`2→2` with least nonzero `|w_i|=1`), and ridge-slide
(`3→3` with exactly two `|w_i|=1`); `c2(v→w) = 2` on ridge-enter
(`2→3` with exactly two `|w_i|=1`); and `c2(v→w) = 1` otherwise.

One Dijkstra from the origin on `B_39(0)` (82239 sites; 82238 nonzero) gives

`t(13,0,0) = 25`, `t(13,13,13) = 43`.

The displayed same-`k` comparison at `k=13` is

`t(13,0,0)^2 / 169  ?  t(13,13,13)^2 / 507`,

which is `625/169` versus `1849/507`, or equivalently `1875 > 1849`. The
inequality does hold. Same-`k` reverse at `k=13` is reported yes.

The rule is displayed, not adopted. Do not write `c2` into Admissibility.
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
none of the hop costs. The integers `3`, `2`, and `1`, the support-size
clauses, the ridge-enter clause, and the arrival function `t` are separately
displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_39(0) = { v ∈ Z^3 : |v|_1 ≤ 39 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_39(0)`,
`t(v)` is the least sum of `c2` along a directed path from `0` to `v` in
that graph.

The sites `(13,0,0)` and `(13,13,13)` both lie in `B_39(0)`: their ℓ¹
norms are `13` and `39`. The pair is computed on this ball by one origin
Dijkstra. These values are Dijkstra outputs, not fitted scalars.

The ridge-enter hop `(2,1,0) → (2,1,1)` has `|σ| : 2 → 3` and exactly two
coordinates of the destination equal to `1` in absolute value, so `ρ3 = 1`
while `c2 = 2`. The hop `(1,1,0) → (1,1,1)` is not ridge-enter (three unit
coordinates) and costs `1`.

## Theorem 1 — Arrivals `t(13,0,0)` And `t(13,13,13)` On `B_39(0)`

One origin Dijkstra on `B_39(0)` returns the integer arrivals

| site | `t_{c2}` |
|---|---:|
| `(13,0,0)` | `25` |
| `(13,13,13)` | `43` |

Every listed site lies in `B_39(0)`. The pair is computed on `B_39(0)`.
These values are Dijkstra outputs, not fitted scalars.

## Theorem 2 — Reverse At The Same-`k` Scale `k=13`

The Euclidean-normalized comparison at `k=13` is

`t(13,0,0)^2 / 169  ?  t(13,13,13)^2 / 507`,

equivalently `3 t(13,0,0)^2 ? t(13,13,13)^2`. Substituting the computed
times gives `3 · 25^2 = 1875` and `43^2 = 1849`, so

`1875 > 1849`.

Arrival per Euclidean length is larger at `(13,0,0)` than at `(13,13,13)`.
Same-`k` reverse at `k=13` does hold. The comparison is displayed, not
adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `c2` is a displayed scoring device on `B_39(0)`. Do not write `c2`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_39(0) for one named hop-cost at k=13. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_39(0) for the displayed rule c2 at k=13; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `c2` among hop-costs that reverse the same-`k` pair at `k=13`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_39(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=13`.
