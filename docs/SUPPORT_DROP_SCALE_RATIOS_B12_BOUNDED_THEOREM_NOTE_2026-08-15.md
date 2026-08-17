---
claim_id: support_drop_scale_ratios_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Axis and body-diagonal arrival ratios under the named support-drop hop-cost on B_12(0) are reported for k=1..4. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_scale_ratios_b12_2026_08_15.py
---

# Named Support-Drop Scale Ratios On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_12(0)`,
scored only for same-`k` axis versus body-diagonal arrival ratios at
`k=1,2,3,4`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_scale_ratios_b12_2026_08_15.py`](../scripts/support_drop_scale_ratios_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_12(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not claimed.

One Dijkstra from the origin on `B_12(0)` (2625 sites) gives the same-`k`
arrivals

| `k` | `t(k,0,0)` | `t(k,k,k)` | `t(k,0,0)^2 / k^2` | `t(k,k,k)^2 / (3k^2)` | reverse |
|---|---:|---:|---:|---:|---|
| `1` | `3` | `5` | `9` | `25/3` | yes |
| `2` | `6` | `8` | `9` | `16/3` | yes |
| `3` | `9` | `11` | `9` | `121/27` | yes |
| `4` | `10` | `14` | `25/4` | `49/12` | yes |

For every `k=1,2,3,4`,

`t(k,0,0)^2 / k^2 > t(k,k,k)^2 / (3k^2)`.

Every available same-`k` scale on this ball still reverses. The `k=3` and
`k=4` rows are not a leftover of a `B_8` table: `(3,3,3)` and `(4,4,4)` lie
outside `B_8(0)`.

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

Let `B_12(0) = { v ∈ Z^3 : |v|_1 ≤ 12 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_12(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph.

The axis-skeleton comparator `α` uses only the first two clauses of `ν`.
On the support-drop hop `(1,1,0) → (1,0,0)` one has `|σ| : 2 → 1`, so
`α = 1` while `ν = 3`. Therefore `α` cannot price support drop, and the
`ν` scores below are not a leftover of `α`.

## Theorem 1 — Same-`k` Arrival Table On `B_12(0)`

One origin Dijkstra on `B_12(0)` returns the integer arrivals

| site | `t_ν` |
|---|---:|
| `(1,0,0)` | `3` |
| `(1,1,1)` | `5` |
| `(2,0,0)` | `6` |
| `(2,2,2)` | `8` |
| `(3,0,0)` | `9` |
| `(3,3,3)` | `11` |
| `(4,0,0)` | `10` |
| `(4,4,4)` | `14` |

Every listed site lies in `B_12(0)`. The sites `(3,3,3)` and `(4,4,4)` have
ℓ¹ norms `9` and `12`, so they are absent from `B_8(0)`. The table is
computed on `B_12(0)`, not copied from a smaller-ball table.

## Theorem 2 — Reverse At Each Same-`k` Scale

For each `k=1,2,3,4` the Euclidean-normalized comparison is

`t(k,0,0)^2 / k^2  ?  t(k,k,k)^2 / (3k^2)`,

equivalently `3 t(k,0,0)^2 ? t(k,k,k)^2`. Substituting the computed times
gives

| `k` | `3 t(k,0,0)^2` | `t(k,k,k)^2` | reverse |
|---|---:|---:|---|
| `1` | `27` | `25` | `27 > 25` |
| `2` | `108` | `64` | `108 > 64` |
| `3` | `243` | `121` | `243 > 121` |
| `4` | `300` | `196` | `300 > 196` |

Arrival per Euclidean length is larger at `(k,0,0)` than at `(k,k,k)` for
every listed `k`. The comparison is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_12(0)`. It is not written
into Admissibility. It is not attached to L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparisons on the finite ball B_12(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_12(0) for the displayed rule ν at k=1..4; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ν` among hop-costs that reverse any same-`k` pair.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_12(0)`.
- Any score for a pair that is not a same-`k` axis / body-diagonal pair.
