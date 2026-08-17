---
claim_id: four_law_variance_reverse_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_6(0), ρ, α, ν, and ℓ¹ are scored for diamond reverse and for var(|v|_2/t). Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/four_law_variance_reverse_b6_2026_08_15.py
---

# Four-Law Variance And Diamond Reverse On The Same B_6(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** four named nearest-neighbor hop-costs on the ℓ¹ ball `B_6(0)`,
scored on the same 376 nonzero sites for diamond reverse at `(4,0,0)` versus
`(2,2,2)` and for population variance of `|v|_2/t`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/four_law_variance_reverse_b6_2026_08_15.py`](../scripts/four_law_variance_reverse_b6_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named support-drop rule `ν` reverses the diamond comparison and beats
unit-cost ℓ¹ variance on `B_6(0)`. The named equal-weight rule `ρ` is
rounder on the same ball and does not reverse. Those one-law scores are not
the claim here. The residual is the joint score of `ρ`, `α`, `ν`, and ℓ¹ on
the same 376 nonzero sites: each law's reverse bit and each law's
population variance, together.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_6(0)`, the four
displayed rules are

`ρ(v→w) = 3` if `|σ_v|=0` or `|σ_v|=|σ_w|`, else `1`
(3 iff equal weight or seed-exit);

`α(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)`, else `1`
(3 iff seed-exit or both weights 1);

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`
(3 iff seed-exit or both weights 1 or support drop);

ℓ¹: every hop `1`.

Four origin Dijkstras on `B_6(0)` (377 sites; 376 nonzero) give

`t_ρ(4,0,0) = 12`, `t_ρ(2,2,2) = 14`;

`t_α(4,0,0) = 8`, `t_α(2,2,2) = 8`;

`t_ν(4,0,0) = 10`, `t_ν(2,2,2) = 8`;

`t_ℓ¹(4,0,0) = 4`, `t_ℓ¹(2,2,2) = 6`.

The ℓ¹ arrivals equal `|v|_1`. The diamond comparison
`12 t_axis^2 > 16 t_diag^2` holds only for `ν`. Population variances of
`|v|_2/t` on the same 376 nonzero sites are

`var_ρ = 0.00067960829822`,
`var_α = 0.00548987632086`,
`var_ν = 0.00590563902870`,
`var_ℓ¹ = 0.01350203761919`.

The order is `var_ρ < var_α < var_ν < var_ℓ¹`.

The four laws are displayed, not adopted. No law is written into
Admissibility. The four laws are not written into Admissibility. No law
is attached to L1. The scores are not leftover of one-law scores.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

Lattice supplies the six-neighbor graph and the ball. Admissibility supplies
none of the hop costs. The integers `3` and `1`, the support-size clauses,
and the arrival functions `t` are separately displayed mathematical inputs.
No axiom text is edited.

## Named Rules

Let `B_6(0) = { v ∈ Z^3 : |v|_1 ≤ 6 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For each displayed
law and each `v ∈ B_6(0)`, `t(v)` is the least sum of that law along a
directed path from `0` to `v` in that graph. The ℓ¹ law is unit hop cost,
so its Dijkstra arrival is the closed form `|v|_1`.

The four clauses are distinct. On the face-diagonal extension
`(1,1,0) → (2,1,0)` one has `|σ| : 2 → 2`, so `ρ = 3` while `α = ν = 1`.
On the support-drop hop `(1,1,0) → (1,0,0)` one has `|σ| : 2 → 1`, so
`ν = 3` while `α = 1`. Therefore the four scores below are a joint table
on one site set, not leftover of one-law scores.

## Theorem 1 — Diamond Reverse At `(4,0,0)` Versus `(2,2,2)`

Four origin Dijkstras on `B_6(0)` return the integer arrivals

| law | `t(4,0,0)` | `t(2,2,2)` | `12 t_axis^2` | `16 t_diag^2` | reverse |
|---|---:|---:|---:|---:|---|
| `ρ` | `12` | `14` | `1728` | `3136` | no |
| `α` | `8` | `8` | `768` | `1024` | no |
| `ν` | `10` | `8` | `1200` | `1024` | yes |
| ℓ¹ | `4` | `6` | `192` | `576` | no |

The Euclidean-normalized comparison is `t^2 / |v|_2^2`, equivalently
`12 t(4,0,0)^2 ? 16 t(2,2,2)^2`. Only `ν` satisfies
`12 t_axis^2 > 16 t_diag^2`. So only ν reverses.

## Theorem 2 — Population Variance Of `|v|_2/t`

On the same 376 nonzero sites of `B_6(0)`, let `r(v) = |v|_2 / t(v)` and
write population variance `(1/n) ∑ (r − mean)^2`. The four values are

`var_ρ = 0.00067960829822`,
`var_α = 0.00548987632086`,
`var_ν = 0.00590563902870`,
`var_ℓ¹ = 0.01350203761919`.

The order is `var_ρ < var_α < var_ν < var_ℓ¹`. The rule `ρ` is the
roundest of the four on this ball and does not reverse. The rule `ν`
reverses and is strictly below ℓ¹. These numbers are displayed, not
adopted.

## Theorem 3 — Displayed, Not Adopted

The four laws are displayed scoring devices on `B_6(0)`. No law is written
into Admissibility. No law is attached to L1. None is a replacement for
unit-cost first arrival, and none is offered as the unique hop-cost with
diamond reverse or with a stated variance rank.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer arrivals and a four-law population-variance comparison on the finite ball B_6(0). The laws are displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_6(0) for the displayed laws ρ, α, ν, and ℓ¹; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of any of the four laws among hop-costs that reverse the
  diamond or that occupy a stated variance rank.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_6(0)`.
- Any leftover of a one-law score in place of the joint four-law table.
