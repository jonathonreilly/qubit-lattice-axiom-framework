---
claim_id: no_shortcut_support_drop_hopcost_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_6(0), the named support-drop hop-cost is scored for diamond reverse at (4,0,0) vs (2,2,2) and for var(|v|_2/t) vs ℓ¹. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/no_shortcut_support_drop_hopcost_b6_2026_08_15.py
---

# Named Support-Drop Hop-Cost On B_6(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_6(0)`,
scored only for diamond reverse at `(4,0,0)` versus `(2,2,2)` and for
population variance of `|v|_2/t` against unit-cost ℓ¹ arrival.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/no_shortcut_support_drop_hopcost_b6_2026_08_15.py`](../scripts/no_shortcut_support_drop_hopcost_b6_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The axis-skeleton rule that prices only seed-exit and axis 1-skeleton hops
is undercut by a cheap off-axis detour: return-to-axis hops stay cheap, so
`t(4,0,0)` falls to the same value as `t(2,2,2)`. The residual is a named
rule that also prices support drop.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_6(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not
claimed.

One Dijkstra from the origin on `B_6(0)` (377 sites; 376 nonzero) gives

`t(4,0,0) = 10`, `t(2,2,2) = 8`.

Then `12 t(4,0,0)^2 = 1200` and `16 t(2,2,2)^2 = 1024`, so

`12 t(4,0,0)^2 > 16 t(2,2,2)^2`.

The diamond comparison reverses. Population variances of `|v|_2/t` on
`B_6(0) \ {0}` are

`var_ν = 0.00590563902870`, `var_ℓ¹ = 0.01350203761919`.

The `ν` variance is strictly smaller.

The rule is displayed, not adopted. It is not written into Admissibility.
It is not attached to L1.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

Lattice supplies the six-neighbor graph and the ball. Admissibility supplies
none of the hop costs. The integers `3` and `1`, the support-size clauses,
and the arrival function `t` are separately displayed mathematical inputs.
No axiom text is edited.

## Named Rule

Let `B_6(0) = { v ∈ Z^3 : |v|_1 ≤ 6 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_6(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph. Unit-cost ℓ¹ arrival is the closed form `t_ℓ¹(v) = |v|_1`; it
is not obtained from a second Dijkstra.

The axis-skeleton comparator `α` uses only the first two clauses of `ν`.
On the support-drop hop `(1,1,0) → (1,0,0)` one has `|σ| : 2 → 1`, so
`α = 1` while `ν = 3`. Therefore `α` cannot price support drop, and the
`ν` scores below are not a leftover of `α`.

## Theorem 1 — Diamond Reverse At `(4,0,0)` Versus `(2,2,2)`

One origin Dijkstra on `B_6(0)` returns the integer arrivals

| site | `t_ν` | `t_ℓ¹` |
|---|---:|---:|
| `(4,0,0)` | `10` | `4` |
| `(2,2,2)` | `8` | `6` |

The Euclidean-normalized comparison is `t^2 / |v|_2^2`, equivalently

`12 t(4,0,0)^2 ? 16 t(2,2,2)^2`.

Substituting the computed times gives `1200 > 1024`. The inequality
reverses: arrival per Euclidean length is larger at `(4,0,0)` than at
`(2,2,2)`. Under unit-cost ℓ¹ the same comparison is `192 > 576`, which
fails.

## Theorem 2 — Population Variance Of `|v|_2/t`

On the 376 nonzero sites of `B_6(0)`, let `r(v) = |v|_2 / t(v)` and write
population variance `(1/n) ∑ (r − mean)^2`. The runner computes

`var_ν = 0.00590563902870`, `var_ℓ¹ = 0.01350203761919`.

So `var_ν < var_ℓ¹`. The named rule is more nearly Euclidean-isotropic
than unit-cost ℓ¹ on this ball, in the population-variance sense stated
here. No uniqueness among hop-costs is claimed.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_6(0)`. It is not written
into Admissibility. It is not attached to L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
diamond reverse or with variance below ℓ¹.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer arrivals and a population-variance comparison on the finite ball B_6(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_6(0) for the displayed rule ν; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ν` among hop-costs that reverse the diamond or beat ℓ¹
  variance.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_6(0)`.
