---
claim_id: support_drop_hopcost_b16_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On B_16(0), the named support-drop hop-cost is scored for same-k, doubled, and k=5 face reverse. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_hopcost_b16_2026_08_15.py
---

# Named Support-Drop Hop-Cost On B_16(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_16(0)`,
scored only for same-`k` reverse at `k=4`, doubled pairing, and the `k=5`
face reverse, together with the original `(4,0,0)` versus `(2,2,2)` diamond
comparison.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_hopcost_b16_2026_08_15.py`](../scripts/support_drop_hopcost_b16_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The same named support-drop hop-cost `ν` already scored on `B_12(0)` is
scored independently on `B_16(0)`. The ball is not leftover of the `B_12(0)` times:
one origin Dijkstra is run on this ball, and the site `(16,0,0)` is
absent from `B_12(0)`.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_16(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not claimed.

One Dijkstra from the origin on `B_16(0)` (6017 sites; 6016 nonzero) gives

`t(4,0,0) = 10`, `t(8,0,0) = 14`, `t(4,4,4) = 14`, `t(2,2,2) = 8`,
`t(10,0,0) = 16`, `t(5,5,0) = 12`.

For `k=4`, those same arrivals are `t(k,0,0) = 10` and `t(k,k,k) = 14`.
The new axis site is `t(16,0,0) = 24`.

Then `12 t(4,0,0)^2 = 1200` and `16 t(2,2,2)^2 = 1024`, so

`12 t(4,0,0)^2 > 16 t(2,2,2)^2`

holds. The doubled-scale pair is `12 t(8,0,0)^2 = 2352` and
`16 t(4,4,4)^2 = 3136`, so

`12 t(8,0,0)^2 > 16 t(4,4,4)^2`

fails. Same-`k` at `k=4` is `t(4,0,0)^2/16 = 100/16` and
`t(4,4,4)^2/48 = 196/48`, so

`t(4,0,0)^2/16 > t(4,4,4)^2/48`

holds. The `k=5` face pair is `t(10,0,0)^2/100 = 256/100` and
`t(5,5,0)^2/50 = 144/50`, so

`t(10,0,0)^2/100 > t(5,5,0)^2/50`

fails.

On `B_16(0)`, same-`k` reverse at `k=4` still holds; the doubled pairing
and the `k=5` face bit stay fail. The rule is displayed, not adopted.
Do not write `ν` into Admissibility. Do not attach L1.

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

The named interior sites `(4,0,0)`, `(8,0,0)`, `(4,4,4)`, `(2,2,2)`,
`(10,0,0)`, and `(5,5,0)` all have ℓ¹ norm at most `12`. They lie in
`B_12(0)` as well. Independently, the `B_16(0)` Dijkstra returns the same
integers at those six sites; that numerical coincidence is not a reuse of
the smaller-ball table. The `B_16(0)` table is therefore not leftover of the `B_12(0)` times.

## Theorem 1 — Arrivals On `B_16(0)`

One origin Dijkstra on `B_16(0)` returns the integer arrivals

| site | `t_ν` |
|---|---:|
| `(4,0,0)` | `10` |
| `(8,0,0)` | `14` |
| `(4,4,4)` | `14` |
| `(2,2,2)` | `8` |
| `(10,0,0)` | `16` |
| `(5,5,0)` | `12` |

For `k=4`, `t(k,0,0) = 10` and `t(k,k,k) = 14`. These values are Dijkstra
outputs, not fitted scalars.

Witnessing paths of those `ν`-costs exist. The walk

`0 → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (4,0,0)`

has hop-costs `3,1,1,1,1,3` and sum `10`. The walk

`0 → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (7,1,0) → (8,1,0) → (8,0,0)`

has hop-costs `3,1,1,1,1,1,1,1,1,3` and sum `14`. The walk

`0 → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (2,2,1) → (2,2,2) → (3,2,2) → (3,3,2) → (3,3,3) → (4,3,3) → (4,4,3) → (4,4,4)`

has hop-costs `3,1,1,1,1,1,1,1,1,1,1,1` and sum `14`. The walk

`0 → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (2,2,1) → (2,2,2)`

has hop-costs `3,1,1,1,1,1` and sum `8`. The walk

`0 → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (7,1,0) → (8,1,0) → (9,1,0) → (10,1,0) → (10,0,0)`

has hop-costs `3,1,1,1,1,1,1,1,1,1,1,3` and sum `16`. The walk

`0 → (1,0,0) → (1,1,0) → (1,2,0) → (1,3,0) → (1,4,0) → (1,5,0) → (2,5,0) → (3,5,0) → (4,5,0) → (5,5,0)`

has hop-costs `3,1,1,1,1,1,1,1,1,1` and sum `12`.

The only in-ball neighbor of `(16,0,0)` is `(15,0,0)`, so the last hop is
the both-weights-`1` axis step of cost `3`. That site is not in `B_12(0)`.

## Theorem 2 — Same-`k`, Doubled, And `k=5` Face Reverse

The four displayed comparisons on `B_16(0)` are whether

`12 t(4,0,0)^2 > 16 t(2,2,2)^2`,

`12 t(8,0,0)^2 > 16 t(4,4,4)^2`,

`t(4,0,0)^2/16 > t(4,4,4)^2/48`,

and

`t(10,0,0)^2/100 > t(5,5,0)^2/50`.

Substituting the computed times gives

- `1200 > 1024` holds,
- `2352 > 3136` fails,
- `100/16 > 196/48` holds, equivalently `300 > 196`,
- `256/100 > 144/50` fails, equivalently `12800 > 14400` fails.

Same-`k` reverse at `k=4` still holds. The doubled pairing stays fail. The
`k=5` face bit stays fail. Displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_16(0)`. Do not write `ν` into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse, doubled pairing, or a `k=5` face bit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer arrivals and four displayed reverse comparisons on the finite ball B_16(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_16(0) for the displayed rule ν; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ν` among hop-costs that reverse any named pair.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_16(0)`.
- Any reuse of the `B_12(0)` arrival table as a substitute for the
  radius-`16` Dijkstra.
