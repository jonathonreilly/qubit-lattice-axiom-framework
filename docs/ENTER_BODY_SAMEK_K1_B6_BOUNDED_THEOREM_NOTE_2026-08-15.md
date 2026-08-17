---
claim_id: enter_body_samek_k1_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=1 under the named enter-body hop-cost on B_6(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/enter_body_samek_k1_b6_2026_08_15.py
---

# Named Enter-Body Same-k Reverse At k=1 On B_6(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_6(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=1`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/enter_body_samek_k1_b6_2026_08_15.py`](../scripts/enter_body_samek_k1_b6_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named enter-body hop-cost `ε` is the already scored corridor-slide
rule `μ` plus cost `3` on a `2→3` hop. `φ` matches `μ` at `k=1`, `7`,
`13`. Cheap large-`k` axis walks can use interior 3-support, so pricing
the enter-body hop is the named residual. The ball is
not leftover of a larger-ball table: one origin Dijkstra is run on this
ball.
Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_6(0)`, let `ν` be the
support-drop rule that costs `3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or
`|σ_w| < |σ_v|`, else `1`. The corridor-slide rule `μ` is

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`.

The displayed rule `ε` is

`ε(v→w) = 3` if `μ` would be `3` or `(|σ_v|=2` and `|σ_w|=3)`, else `1`.

The extra clause is the enter-body `2→3` hop. Those clauses are the whole
rule.

One Dijkstra from the origin on `B_6(0)` (377 sites; 376 nonzero) gives

`t(1,0,0) = 3`, `t(1,1,1) = 7`.

The displayed same-`k` comparison at `k=1` is

`t(1,0,0)^2 / 1  ?  t(1,1,1)^2 / 3`,

which is `9/1` versus `49/3`, or equivalently `27 > 49`. The inequality
does not hold. Same-`k` reverse does not hold at `k=1`. The small-`k` bar
is not killed. Independently, the axis endpoint of this ball is
`t(6,0,0) = 18`.

The pair is not leftover of `μ` or of `φ`. Under both `μ` and `φ` the same
sites are `3` and `5`, and `27 > 25` holds. On the enter-body hop
`(1,1,0) → (1,1,1)` one has `|σ| : 2 → 3`, so `μ = 1` and `φ = 1` while
`ε = 3`. Therefore `μ` cannot price the enter-body hop, `φ` cannot price
the enter-body hop, and the `ε` scores below are not a leftover of `μ` or
`φ`.

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

Let `B_6(0) = { v ∈ Z^3 : |v|_1 ≤ 6 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_6(0)`,
`t(v)` is the least sum of `ε` along a directed path from `0` to `v` in
that graph.

The comparator `μ` uses the three support-drop clauses of `ν` plus the
axis-hugging `2→2` slide. On the enter-body hop `(1,1,0) → (1,1,1)` one
has `|σ| : 2 → 3`, so `μ = 1` while `ε = 3`. Therefore `μ` cannot price
the enter-body hop. The all-face-slide comparator `φ` prices every
`2→2` hop at `3` and still prices this `2→3` hop at `1`, so `φ` cannot
price the enter-body hop.

## Theorem 1 — Arrivals `t(1,0,0)` And `t(1,1,1)` On `B_6(0)`

One origin Dijkstra on `B_6(0)` returns the integer arrivals

| site | `t_ε` |
|---|---:|
| `(1,0,0)` | `3` |
| `(1,1,1)` | `7` |

Every listed site lies in `B_6(0)`. The pair is computed on `B_6(0)`, not
copied from a larger-ball table and not copied from the `μ` pair
`3` versus `5`. These values are Dijkstra outputs, not fitted scalars.

A witness walk to `(1,0,0)` is the seed-exit of cost `3`. A witness walk
to `(1,1,1)` is seed-exit `3` onto `(1,0,0)`, body `1→2` of cost `1` onto
`(1,1,0)`, and enter-body `2→3` of cost `3` onto `(1,1,1)`, summing to
`7`. Those walks are witnesses, not a uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=1`

The Euclidean-normalized comparison at `k=1` is

`t(1,0,0)^2 / 1  ?  t(1,1,1)^2 / 3`,

equivalently `3 t(1,0,0)^2 ? t(1,1,1)^2`. Substituting the computed times
gives `3 · 3^2 = 27` and `7^2 = 49`, so

`27 > 49` is false; `27 < 49`.

Arrival per Euclidean length is smaller at `(1,0,0)` than at `(1,1,1)`.
Same-`k` reverse at `k=1` is no. The small-`k` bar is not killed. The
comparison is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ε` is a displayed scoring device on `B_6(0)`. Do not write `ε`
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
conditional_surface_status: "exact on B_6(0) for the displayed rule ε at k=1; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ε` among hop-costs that score the same-`k` pair at `k=1`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_6(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=1`.
- Any reuse of a larger-ball arrival table, or of the `μ` or `φ` pair, as
  a substitute for the radius-`6` Dijkstra.
- Membership of `ε` as a physical hop-cost. The small-`k` bar is not
  killed on this ball; that is a displayed exclusion test, not an adoption.
