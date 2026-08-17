---
claim_id: support_drop_samek_k6_b18_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=6 under the named support-drop hop-cost on B_18(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_samek_k6_b18_2026_08_15.py
---

# Named Support-Drop Same-k Reverse At k=6 On B_18(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_18(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=6`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_samek_k6_b18_2026_08_15.py`](../scripts/support_drop_samek_k6_b18_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The same named support-drop hop-cost `ν` already scored on `B_16(0)` is
scored independently on `B_18(0)`. The ball is not leftover of the `B_16(0)`
times: one origin Dijkstra is run on this ball, and the site `(6,6,6)` is
absent from `B_16(0)`.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_18(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not claimed.

One Dijkstra from the origin on `B_18(0)` (8473 sites; 8472 nonzero) gives

`t(6,0,0) = 12`, `t(6,6,6) = 20`.

The displayed same-`k` comparison at `k=6` is

`t(6,0,0)^2 / 36  ?  t(6,6,6)^2 / 108`,

which is `144/36` versus `400/108`, or equivalently `432 > 400`. The
inequality holds. Same-`k` reverse survives one more scale. Independently,
the new axis site is `t(18,0,0) = 26`. The shared axis site
`t(16,0,0) = 22` on this ball is not the `B_16(0)` value `24`.

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

Let `B_18(0) = { v ∈ Z^3 : |v|_1 ≤ 18 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_18(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph.

The site `(6,0,0)` has ℓ¹ norm `6` and therefore also lies in `B_16(0)`.
The site `(6,6,6)` has ℓ¹ norm `18`, so it is absent from `B_16(0)`. The
`B_18(0)` table is therefore not leftover of the `B_16(0)` times.

The axis-skeleton comparator `α` uses only the first two clauses of `ν`.
On the support-drop hop `(1,1,0) → (1,0,0)` one has `|σ| : 2 → 1`, so
`α = 1` while `ν = 3`. Therefore `α` cannot price support drop, and the
`ν` scores below are not a leftover of `α`.

## Theorem 1 — Arrivals `t(6,0,0)` And `t(6,6,6)` On `B_18(0)`

One origin Dijkstra on `B_18(0)` returns the integer arrivals

| site | `t_ν` |
|---|---:|
| `(6,0,0)` | `12` |
| `(6,6,6)` | `20` |

Every listed site lies in `B_18(0)`. The site `(6,6,6)` has ℓ¹ norm `18`,
so it is absent from `B_16(0)`. The pair is computed on `B_18(0)`, not
copied from a smaller-ball table. These values are Dijkstra outputs, not
fitted scalars.

## Theorem 2 — Reverse At The Same-`k` Scale `k=6`

The Euclidean-normalized comparison at `k=6` is

`t(6,0,0)^2 / 36  ?  t(6,6,6)^2 / 108`,

equivalently `3 t(6,0,0)^2 ? t(6,6,6)^2`. Substituting the computed times
gives `3 · 12^2 = 432` and `20^2 = 400`, so

`432 > 400`.

Arrival per Euclidean length is larger at `(6,0,0)` than at `(6,6,6)`.
Same-`k` reverse at `k=6` is yes. The comparison is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_18(0)`. Do not write `ν`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_18(0) for one named hop-cost at k=6. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_18(0) for the displayed rule ν at k=6; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ν` among hop-costs that reverse the same-`k` pair at `k=6`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_18(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=6`.
- Any reuse of the `B_16(0)` arrival table as a substitute for the
  radius-`18` Dijkstra.
