---
claim_id: leave_axis_samek_k1_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=1 under the named leave-axis hop-cost on B_6(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/leave_axis_samek_k1_b6_2026_08_15.py
---

# Named Leave-Axis Same-k Reverse At k=1 On B_6(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_6(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=1`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/leave_axis_samek_k1_b6_2026_08_15.py`](../scripts/leave_axis_samek_k1_b6_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named leave-axis hop-cost `λ` is scored independently on `B_6(0)`. The
ball is not leftover of a larger-ball table: one origin Dijkstra is run on
this ball.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_6(0)`, the displayed
rule `λ` is

`λ(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|` or
`(|σ_v|=1` and `|σ_w|=2)`, else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. The fourth is the leave-axis `1→2` hop. Those four clauses are
the whole rule. Uniqueness is not claimed.

One Dijkstra from the origin on `B_6(0)` (377 sites; 376 nonzero) gives

`t(1,0,0) = 3`, `t(1,1,1) = 7`.

The displayed same-`k` comparison at `k=1` is

`t(1,0,0)^2 / 1  ?  t(1,1,1)^2 / 3`,

which is `9/1` versus `49/3`, or equivalently `27 > 49`. The inequality
does not hold. Same-`k` reverse does not hold at `k=1`. The small-`k` bar is
not killed. Independently, the axis endpoint of this ball is `t(6,0,0) = 16`.

The rule is displayed, not adopted. Do not write `λ` into Admissibility.
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
`t(v)` is the least sum of `λ` along a directed path from `0` to `v` in
that graph.

The support-drop comparator `ν` uses only the first three clauses of `λ`.
On the leave-axis hop `(1,0,0) → (1,1,0)` one has `|σ| : 1 → 2`, so
`ν = 1` while `λ = 3`. Therefore `ν` cannot price the leave-axis hop, and
the `λ` scores below are not a leftover of `ν`.

## Theorem 1 — Arrivals `t(1,0,0)` And `t(1,1,1)` On `B_6(0)`

One origin Dijkstra on `B_6(0)` returns the integer arrivals

| site | `t_λ` |
|---|---:|
| `(1,0,0)` | `3` |
| `(1,1,1)` | `7` |

Every listed site lies in `B_6(0)`. The pair is computed on `B_6(0)`, not
copied from a larger-ball table. These values are Dijkstra outputs, not
fitted scalars.

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

The rule `λ` is a displayed scoring device on `B_6(0)`. Do not write `λ`
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
conditional_surface_status: "exact on B_6(0) for the displayed rule λ at k=1; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `λ` among hop-costs that score the same-`k` pair at `k=1`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_6(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=1`.
- Any reuse of a larger-ball arrival table as a substitute for the
  radius-`6` Dijkstra.
- Membership of `λ` as a physical hop-cost. The small-`k` bar is not
  killed on this ball; that is a displayed exclusion test, not an adoption.
