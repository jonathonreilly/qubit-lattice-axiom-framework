---
claim_id: leave_axis_samek_k7_b21_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=7 under the named leave-axis hop-cost on B_21(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/leave_axis_samek_k7_b21_2026_08_15.py
---

# Named Leave-Axis Same-k Reverse At k=7 On B_21(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_21(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=7`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/leave_axis_samek_k7_b21_2026_08_15.py`](../scripts/leave_axis_samek_k7_b21_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named leave-axis hop-cost `λ` is the already scored support-drop
rule `ν` plus cost `3` on the leave-axis hop `|σ|=1→2`. Same-`k` reverse
under `ν` fails at `k=7` (`13` versus `23`) and at `k=8` (`14` versus
`26`). The whyk7 axis walk is seed-exit to `(0,-1,0)`, a slide along
`y = -1`, then the support-drop `(7,-1,0) → (7,0,0)`. The leave-axis
hop on that walk is `(0,-1,0) → (1,-1,0)`, which costs `1` under `ν`.
`λ` prices that hop at `3`. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_21(0)`, the displayed
rule `λ` is

`λ(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|` or
`(|σ_v|=1` and `|σ_w|=2)`, else `1`.

The first clause is seed-exit. The second is both weights `1`. The third
is support drop. The fourth is leave-axis. Those four clauses are the
whole rule.

One Dijkstra from the origin on `B_21(0)` (13287 sites; 13286 nonzero) gives

`t(7,0,0) = 15`, `t(7,7,7) = 25`.

The displayed same-`k` comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

which is `225/49` versus `625/147`, or equivalently `675 > 625`. The
inequality holds. Same-`k` reverse at `k=7` under `λ` is yes. Independently,
the new axis site is `t(21,0,0) = 31`. The shared axis site
`t(18,0,0) = 26` is a `λ` score on this ball, not a `ν` leftover.

The pair is not leftover of `ν`: the same sites under `ν` are `13` and
`23`, and `507 > 529` fails. The extra leave-axis clause is what changes
the pair. The site `(7,7,7)` has ℓ¹ norm `21`, so it is absent from
`B_18(0)`. The `B_21(0)` table is therefore not leftover of a smaller-ball
table.

The rule is displayed, not adopted. Do not write `λ` or `ν` into Admissibility.
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
`t(v)` is the least sum of `λ` along a directed path from `0` to `v` in
that graph.

The comparator `ν` uses only the first three clauses of `λ`. On the
leave-axis hop `(0,-1,0) → (1,-1,0)` one has `|σ| : 1 → 2`, so `ν = 1`
while `λ = 3`. Therefore `ν` cannot price leave-axis, and the `λ` scores
below are not a leftover of `ν`.

## Theorem 1 — Arrivals `t(7,0,0)` And `t(7,7,7)` On `B_21(0)`

One origin Dijkstra on `B_21(0)` returns the integer arrivals

| site | `t_λ` |
|---|---:|
| `(7,0,0)` | `15` |
| `(7,7,7)` | `25` |

Every listed site lies in `B_21(0)`. The site `(7,7,7)` has ℓ¹ norm `21`,
so it is absent from `B_18(0)`. The pair is computed on `B_21(0)`, not
copied from a smaller-ball table and not copied from the `ν` pair
`13` versus `23`. These values are Dijkstra outputs, not fitted scalars.

The whyk7 axis walk, re-scored under `λ`, is seed-exit `3` onto
`(0,-1,0)`, leave-axis `3` on `(0,-1,0) → (1,-1,0)`, six support-preserving
cost-`1` slides to `(7,-1,0)`, and support-drop `3` onto `(7,0,0)`,
summing to `15`. That walk is a witness of cost `15`, not a uniqueness
claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=7`

The Euclidean-normalized comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

equivalently `3 t(7,0,0)^2 ? t(7,7,7)^2`. Substituting the computed times
gives `3 · 15^2 = 675` and `25^2 = 625`, so

`675 > 625` is true.

Arrival per Euclidean length is larger at `(7,0,0)` than at `(7,7,7)`.
Same-`k` reverse at `k=7` under `λ` is yes. The comparison is displayed,
not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `λ` is a displayed scoring device on `B_21(0)`. Do not write `λ` or `ν` into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_21(0) for one named hop-cost at k=7. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_21(0) for the displayed rule λ at k=7; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `λ` among hop-costs that reverse the same-`k` pair at `k=7`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_21(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=7`.
- Any reuse of the `ν` arrival table as a substitute for the `λ` Dijkstra.
