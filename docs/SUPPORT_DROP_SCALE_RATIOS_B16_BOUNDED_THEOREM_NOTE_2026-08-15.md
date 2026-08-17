---
claim_id: support_drop_scale_ratios_b16_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Axis and body-diagonal arrival ratios under the named support-drop hop-cost on B_16(0) are reported for k=1..5. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_scale_ratios_b16_2026_08_15.py
---

# Named Support-Drop Scale Ratios On B_16(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_16(0)`,
scored only for same-`k` axis versus body-diagonal arrival ratios at
`k=1,2,3,4,5`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_scale_ratios_b16_2026_08_15.py`](../scripts/support_drop_scale_ratios_b16_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The same named support-drop hop-cost `ν` already scored on `B_12(0)` is
scored independently on `B_16(0)`. The ball is not leftover of the `B_12(0)` times:
one origin Dijkstra is run on this ball, and the site `(5,5,5)` is
absent from `B_12(0)`.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_16(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not claimed.

One Dijkstra from the origin on `B_16(0)` (6017 sites; 6016 nonzero) gives
the same-`k` arrivals

| `k` | `t(k,0,0)` | `t(k,k,k)` | `t(k,0,0)^2 / k^2` | `t(k,k,k)^2 / (3k^2)` | reverse |
|---|---:|---:|---:|---:|---|
| `1` | `3` | `5` | `9` | `25/3` | yes |
| `2` | `6` | `8` | `9` | `16/3` | yes |
| `3` | `9` | `11` | `9` | `121/27` | yes |
| `4` | `10` | `14` | `25/4` | `49/12` | yes |
| `5` | `11` | `17` | `121/25` | `289/75` | yes |

For every `k=1,2,3,4,5`,

`t(k,0,0)^2 / k^2 > t(k,k,k)^2 / (3k^2)`.

Same-`k` reverse stays yes through `k=5`. The `k=5` row is not a leftover
of a `B_12` table: `(5,5,5)` has ℓ¹ norm `15`, so it is absent from
`B_12(0)`. Independently, the new axis site is `t(16,0,0) = 24`.

The rule is displayed, not adopted. Do not write `ν` into Admissibility.
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

Let `B_16(0) = { v ∈ Z^3 : |v|_1 ≤ 16 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_16(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph.

The named interior sites `(1,0,0)`, `(1,1,1)`, `(2,0,0)`, `(2,2,2)`,
`(3,0,0)`, `(3,3,3)`, `(4,0,0)`, and `(4,4,4)` all have ℓ¹ norm at most
`12`. They lie in `B_12(0)` as well. Independently, the `B_16(0)` Dijkstra
returns the same integers at those eight sites; that numerical coincidence
is not a reuse of the smaller-ball table. The `B_16(0)` table is therefore
not leftover of the `B_12(0)` times.

The axis-skeleton comparator `α` uses only the first two clauses of `ν`.
On the support-drop hop `(1,1,0) → (1,0,0)` one has `|σ| : 2 → 1`, so
`α = 1` while `ν = 3`. Therefore `α` cannot price support drop, and the
`ν` scores below are not a leftover of `α`.

## Theorem 1 — Same-`k` Arrival Table On `B_16(0)`

One origin Dijkstra on `B_16(0)` returns the integer arrivals

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
| `(5,0,0)` | `11` |
| `(5,5,5)` | `17` |

Every listed site lies in `B_16(0)`. The site `(5,5,5)` has ℓ¹ norm `15`,
so it is absent from `B_12(0)`. The table is computed on `B_16(0)`, not
copied from a smaller-ball table. These values are Dijkstra outputs, not
fitted scalars.

## Theorem 2 — Reverse At Each Same-`k` Scale

For each `k=1,2,3,4,5` the Euclidean-normalized comparison is

`t(k,0,0)^2 / k^2  ?  t(k,k,k)^2 / (3k^2)`,

equivalently `3 t(k,0,0)^2 ? t(k,k,k)^2`. Substituting the computed times
gives

| `k` | `3 t(k,0,0)^2` | `t(k,k,k)^2` | reverse |
|---|---:|---:|---|
| `1` | `27` | `25` | `27 > 25` |
| `2` | `108` | `64` | `108 > 64` |
| `3` | `243` | `121` | `243 > 121` |
| `4` | `300` | `196` | `300 > 196` |
| `5` | `363` | `289` | `363 > 289` |

Arrival per Euclidean length is larger at `(k,0,0)` than at `(k,k,k)` for
every listed `k`. The comparison is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_16(0)`. Do not write `ν`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparisons on the finite ball B_16(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_16(0) for the displayed rule ν at k=1..5; no Admissibility edit; not attached to L1"
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
- Any statement off `B_16(0)`.
- Any score for a pair that is not a same-`k` axis / body-diagonal pair.
- Any reuse of the `B_12(0)` arrival table as a substitute for the
  radius-`16` Dijkstra.
