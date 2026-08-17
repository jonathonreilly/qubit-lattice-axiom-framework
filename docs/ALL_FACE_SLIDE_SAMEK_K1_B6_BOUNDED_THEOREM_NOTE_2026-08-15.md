---
claim_id: all_face_slide_samek_k1_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=1 under the named all-face-slide hop-cost on B_6(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/all_face_slide_samek_k1_b6_2026_08_15.py
---

# Named All-Face-Slide Same-k Reverse At k=1 On B_6(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_6(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=1`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/all_face_slide_samek_k1_b6_2026_08_15.py`](../scripts/all_face_slide_samek_k1_b6_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named all-face-slide hop-cost `φ` is scored on `B_6(0)` at the first
same-`k` scale `k=1`. One origin Dijkstra is run on this ball.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. Let `ν`
be the named support-drop rule

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

On a directed nearest-neighbor hop `v → w` still inside `B_6(0)`, the
displayed rule `φ` is

`φ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2)`, else `1`.

Equivalently, `φ` is `ν` plus cost `3` on every `2→2` hop. The first
inherited clause is seed-exit. The second is both weights `1`. The third
is support drop. The extra clause prices every face-parallel slide. Those
four clauses are the whole rule. Uniqueness is not claimed.

One Dijkstra from the origin on `B_6(0)` (377 sites; 376 nonzero) gives

`t(1,0,0) = 3`, `t(1,1,1) = 5`.

The displayed same-`k` comparison at `k=1` is

`t(1,0,0)^2 / 1  ?  t(1,1,1)^2 / 3`,

which is `9/1` versus `25/3`, or equivalently `27 > 25`. The inequality
holds. Same-`k` reverse holds at `k=1` under `φ`. Independently, the far
axis site is `t(6,0,0) = 18`.

The same-`k` pair at `k=1` does not use a `2→2` hop on a geodesic, so the
two arrivals coincide with the `ν` arrivals. The rule is still not leftover of `ν`:
on the face slide `(2,2,0) → (3,2,0)` one has `|σ| : 2 → 2`, so
`ν = 1` while `φ = 3`. The corridor-slide comparator `μ` prices a `2→2`
hop only when the least nonzero `|w_i|` equals `1`; on that same hop
`μ = 1` while `φ = 3`. Therefore `μ` cannot price every face slide, and
the `φ` scores below are not a leftover of `μ`.

The rule is displayed, not adopted. Do not write `φ` into Admissibility.
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
`t(v)` is the least sum of `φ` along a directed path from `0` to `v` in
that graph.

The site `(1,0,0)` has ℓ¹ norm `1`. The site `(1,1,1)` has ℓ¹ norm `3`.
Both lie in `B_6(0)`. The table is computed by one origin Dijkstra on
`B_6(0)`, not copied from a smaller-ball table.

## Theorem 1 — Arrivals `t(1,0,0)` And `t(1,1,1)` On `B_6(0)`

One origin Dijkstra on `B_6(0)` returns the integer arrivals

| site | `t_φ` |
|---|---:|
| `(1,0,0)` | `3` |
| `(1,1,1)` | `5` |

Every listed site lies in `B_6(0)`. The pair is computed on `B_6(0)`, not
copied from a smaller-ball table. These values are Dijkstra outputs, not
fitted scalars.

## Theorem 2 — Reverse At The Same-`k` Scale `k=1`

The Euclidean-normalized comparison at `k=1` is

`t(1,0,0)^2 / 1  ?  t(1,1,1)^2 / 3`,

equivalently `3 t(1,0,0)^2 ? t(1,1,1)^2`. Substituting the computed times
gives `3 · 3^2 = 27` and `5^2 = 25`, so

`27 > 25`.

Arrival per Euclidean length is larger at `(1,0,0)` than at `(1,1,1)`.
Same-`k` reverse at `k=1` is yes. The comparison is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `φ` is a displayed scoring device on `B_6(0)`. Do not write `φ`
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
conditional_surface_status: "exact on B_6(0) for the displayed rule φ at k=1; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `φ` among hop-costs that reverse the same-`k` pair at `k=1`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_6(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=1`.
- Any reuse of a smaller-ball arrival table as a substitute for the
  radius-`6` Dijkstra.
- Any adoption of `φ` as a physical law, or any identification with the
  support-drop rule `ν` or the corridor-slide rule `μ`.
