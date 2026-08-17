---
claim_id: support_drop_body_reverse_vs_k_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Body-diagonal reverse versus integer scale k under the named support-drop hop-cost on B_12(0) is reported for k=1..4. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_body_reverse_vs_k_b12_2026_08_15.py
---

# Named Support-Drop Body Reverse Versus Scale k On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_12(0)`,
scored only for the face-orthogonal body census pairing
`((2k,0,0),(k,k,k))` at every integer `k=1,2,3,4`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_body_reverse_vs_k_b12_2026_08_15.py`](../scripts/support_drop_body_reverse_vs_k_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_12(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not claimed.

One Dijkstra from the origin on `B_12(0)` (2625 sites) gives the body-census
arrivals

| `k` | site axis | `t(2k,0,0)` | site body | `t(k,k,k)` | `12 t(2k,0,0)^2` | `16 t(k,k,k)^2` | reverse |
|---|---|---:|---|---:|---:|---:|---|
| `1` | `(2,0,0)` | `6` | `(1,1,1)` | `5` | `432` | `400` | yes |
| `2` | `(4,0,0)` | `10` | `(2,2,2)` | `8` | `1200` | `1024` | yes |
| `3` | `(6,0,0)` | `12` | `(3,3,3)` | `11` | `1728` | `1936` | no |
| `4` | `(8,0,0)` | `14` | `(4,4,4)` | `14` | `2352` | `3136` | no |

Equivalently, `t(2k,0,0)^2 / (4k^2) > t(k,k,k)^2 / (3k^2)` holds at
`k=1` (`9 > 25/3`) and at `k=2` (`25/4 > 16/3`), and fails at `k=3`
(`4 > 121/27` fails) and at `k=4` (`49/16 > 49/12` fails). Reverse is
not leftover of the two named pairs `((4,0,0),(2,2,2))` and
`((8,0,0),(4,4,4))`: the `k=1` and `k=3` rows are additional scales.

The rule is displayed, not adopted. It is not written into Admissibility.
It is not attached to L1. Do not write `ν` into Admissibility.
Do not attach L1.

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

The pairing is not the same-`k` axis / body pair `(k,0,0)` versus
`(k,k,k)`. It is the face-orthogonal body census
`((2k,0,0),(k,k,k))`.

## Theorem 1 — Arrivals For Each `k=1..4`

One origin Dijkstra on `B_12(0)` returns the integer arrivals

| site | `t_ν` |
|---|---:|
| `(2,0,0)` | `6` |
| `(1,1,1)` | `5` |
| `(4,0,0)` | `10` |
| `(2,2,2)` | `8` |
| `(6,0,0)` | `12` |
| `(3,3,3)` | `11` |
| `(8,0,0)` | `14` |
| `(4,4,4)` | `14` |

Every listed site lies in `B_12(0)`. Witnessing paths of those `ν`-costs
exist. The walk

`0 → (1,0,0) → (2,0,0)`

has hop-costs `3,3` and sum `6`. The walk

`0 → (1,0,0) → (1,1,0) → (1,1,1)`

has hop-costs `3,1,1` and sum `5`. The walk

`0 → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (4,0,0)`

has hop-costs `3,1,1,1,1,3` and sum `10`. The walk

`0 → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (2,2,1) → (2,2,2)`

has hop-costs `3,1,1,1,1,1` and sum `8`. The walk

`0 → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (6,0,0)`

has hop-costs `3,1,1,1,1,1,1,3` and sum `12`. The walk

`0 → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (2,2,1) → (2,2,2) → (3,2,2) → (3,3,2) → (3,3,3)`

has hop-costs `3,1,1,1,1,1,1,1,1` and sum `11`. The walk

`0 → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (7,1,0) → (8,1,0) → (8,0,0)`

has hop-costs `3,1,1,1,1,1,1,1,1,3` and sum `14`. The walk

`0 → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (2,2,1) → (2,2,2) → (3,2,2) → (3,3,2) → (3,3,3) → (4,3,3) → (4,4,3) → (4,4,4)`

has hop-costs `3,1,1,1,1,1,1,1,1,1,1,1` and sum `14`.

The table is computed on `B_12(0)`, not copied from two named pairs.

## Theorem 2 — Reverse Bit At Each Scale

For each `k=1,2,3,4` the Euclidean-normalized comparison is

`t(2k,0,0)^2 / (4k^2)  ?  t(k,k,k)^2 / (3k^2)`,

equivalently `12 t(2k,0,0)^2 ? 16 t(k,k,k)^2`. Substituting the computed
times gives

| `k` | `12 t(2k,0,0)^2` | `16 t(k,k,k)^2` | reverse |
|---|---:|---:|---|
| `1` | `432` | `400` | `432 > 400` |
| `2` | `1200` | `1024` | `1200 > 1024` |
| `3` | `1728` | `1936` | `1728 > 1936` fails |
| `4` | `2352` | `3136` | `2352 > 3136` fails |

Arrival per Euclidean length is larger at `(2k,0,0)` than at `(k,k,k)` for
`k=1,2` and is not larger for `k=3,4`. Fail is already present at `k=3`;
it is not isolated at the doubled diamond. The comparison is displayed,
not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_12(0)`. It is not written
into Admissibility. It is not attached to L1. Do not write `ν` into
Admissibility. Do not attach L1. It is not a replacement for unit-cost
first arrival, and it is not offered as the unique hop-cost with
body-census reverse at any `k`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer body-census arrivals and reverse bits on the finite ball B_12(0) for one named hop-cost at k=1..4. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_12(0) for the displayed rule ν at k=1..4 on ((2k,0,0),(k,k,k)); no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ν` among hop-costs that reverse any body-census pair.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_12(0)`.
- Any score for a pair that is not `((2k,0,0),(k,k,k))`.
- Any leftover of the two named pairs `((4,0,0),(2,2,2))` and
  `((8,0,0),(4,4,4))` as a substitute for the four-scale census.
