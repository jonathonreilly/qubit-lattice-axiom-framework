---
claim_id: enter_body_samek_k2_b8_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=2 under the named enter-body hop-cost on B_8(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/enter_body_samek_k2_b8_2026_08_15.py
---

# Named Enter-Body Same-k Reverse At k=2 On B_8(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_8(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=2`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/enter_body_samek_k2_b8_2026_08_15.py`](../scripts/enter_body_samek_k2_b8_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named enter-body hop-cost `ε` is the already scored corridor-slide
rule `μ` plus cost `3` on a `2→3` hop. `ε` kills same-`k` reverse at
`k=1` (`3` versus `7`) and holds at `k=7`. The residual scored here is
whether reverse recovers at `k=2` on `B_8(0)`. The ball is
not leftover of a larger-ball table: one origin Dijkstra is run on this
ball.
Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_8(0)`, let `ν` be the
support-drop rule that costs `3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or
`|σ_w| < |σ_v|`, else `1`. The corridor-slide rule `μ` is

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`.

The displayed rule `ε` is

`ε(v→w) = 3` if `μ` would be `3` or `(|σ_v|=2` and `|σ_w|=3)`, else `1`.

The extra clause is the enter-body `2→3` hop. Those clauses are the whole
rule.

One Dijkstra from the origin on `B_8(0)` (833 sites; 832 nonzero) gives

`t(2,0,0) = 6`, `t(2,2,2) = 10`.

The displayed same-`k` comparison at `k=2` is

`t(2,0,0)^2 / 4  ?  t(2,2,2)^2 / 12`,

which is `36/4` versus `100/12`, or equivalently `108 > 100`. The
inequality holds. Same-`k` reverse recovers at `k=2`. Independently, the
axis endpoint of this ball is `t(8,0,0) = 24`. The `B_8(0)` table is
not leftover of the `B_6(0)` times.

The pair is not leftover of `μ`. On the enter-body hop
`(1,1,0) → (1,1,1)` one has `|σ| : 2 → 3`, so `μ = 1` while `ε = 3`.
A `μ` witness to `(2,2,2)` along the same sites would sum to `8`; `ε`
scores `10`. The same sites under `μ` are `6` versus `8`. Therefore `μ`
cannot price the enter-body hop, and the `ε` scores below are not a
leftover of `μ`.

The rule is displayed, not adopted. Do not write `ε` into Admissibility.
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
`t(v)` is the least sum of `ε` along a directed path from `0` to `v` in
that graph.

The comparator `μ` uses the three support-drop clauses of `ν` plus the
axis-hugging `2→2` slide. On the enter-body hop `(1,1,0) → (1,1,1)` one
has `|σ| : 2 → 3`, so `μ = 1` while `ε = 3`. Therefore `μ` cannot price
the enter-body hop.

## Theorem 1 — Arrivals `t(2,0,0)` And `t(2,2,2)` On `B_8(0)`

One origin Dijkstra on `B_8(0)` returns the integer arrivals

| site | `t_ε` |
|---|---:|
| `(2,0,0)` | `6` |
| `(2,2,2)` | `10` |

Every listed site lies in `B_8(0)`. The site `(2,2,2)` has ℓ¹ norm `6`.
The pair is computed on `B_8(0)`, not copied from a larger-ball table,
not leftover of the `B_6(0)` times, and not copied from the `μ` pair
`6` versus `8`. These values are Dijkstra outputs, not fitted scalars.

A witness walk to `(2,0,0)` is seed-exit `3` onto `(1,0,0)` and the
both-weights-`1` hop of cost `3` onto `(2,0,0)`, summing to `6`. A
witness walk to `(2,2,2)` is seed-exit `3` onto `(1,0,0)`, body `1→2` of
cost `1` onto `(1,1,0)`, enter-body `2→3` of cost `3` onto `(1,1,1)`,
and three support-preserving cost-`1` body hops onto `(2,1,1)`,
`(2,2,1)`, and `(2,2,2)`, summing to `10`. Those walks are witnesses,
not a uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=2`

The Euclidean-normalized comparison at `k=2` is

`t(2,0,0)^2 / 4  ?  t(2,2,2)^2 / 12`,

equivalently `3 t(2,0,0)^2 ? t(2,2,2)^2`. Substituting the computed times
gives `3 · 6^2 = 108` and `10^2 = 100`, so

`108 > 100`.

Arrival per Euclidean length is larger at `(2,0,0)` than at `(2,2,2)`.
Same-`k` reverse at `k=2` under `ε` is yes. Reverse recovers at `k=2`.
The comparison is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ε` is a displayed scoring device on `B_8(0)`. Do not write `ε`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_8(0) for one named hop-cost at k=2. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_8(0) for the displayed rule ε at k=2; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ε` among hop-costs that score the same-`k` pair at `k=2`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_8(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=2`.
- Any reuse of a larger-ball arrival table, or of the `μ` pair, as a
  substitute for the radius-`8` Dijkstra.
- Membership of `ε` as a physical hop-cost. Reverse recovers at `k=2` on
  this ball; that is a displayed exclusion test, not an adoption.
