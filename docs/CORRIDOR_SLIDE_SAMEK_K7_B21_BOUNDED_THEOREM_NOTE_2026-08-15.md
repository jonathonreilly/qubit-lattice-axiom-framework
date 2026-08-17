---
claim_id: corridor_slide_samek_k7_b21_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=7 under the named corridor-slide hop-cost on B_21(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/corridor_slide_samek_k7_b21_2026_08_15.py
---

# Named Corridor-Slide Same-k Reverse At k=7 On B_21(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_21(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=7`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/corridor_slide_samek_k7_b21_2026_08_15.py`](../scripts/corridor_slide_samek_k7_b21_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named corridor-slide hop-cost `μ` is the already scored support-drop
rule `ν` plus cost `3` on a `2→2` hop whose destination has least nonzero
absolute coordinate equal to `1` (an axis-hugging face slide). Same-`k`
reverse under `ν` fails at `k=7` (`13` versus `23`). The leave-axis rule
`λ` restores reverse at `k=7` (`15` versus `25`) by pricing the `|σ|=1→2`
hop, but that same `1→2` clause hits the `k=1` body hop and not a long
corridor. The `1→2` hop is not an extra clause of `μ`.
Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_21(0)`, the displayed
comparator `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The displayed rule `μ` is

`μ(v→w) = 3` if `ν(v→w)` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`.

The first three clauses are those of `ν`: seed-exit, both weights `1`, and
support drop. The fourth clause is the axis-hugging `2→2` slide. Those four
clauses are the whole rule.

One Dijkstra from the origin on `B_21(0)` (13287 sites; 13286 nonzero) gives

`t(7,0,0) = 17`, `t(7,7,7) = 23`.

The displayed same-`k` comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

which is `289/49` versus `529/147`, or equivalently `867 > 529`. The
inequality holds. Same-`k` reverse at `k=7` under `μ` is yes. Independently,
the new axis site is `t(21,0,0) = 35`. The shared axis site
`t(18,0,0) = 28` is a `μ` score on this ball, not a `ν` leftover.

The pair is not leftover of `ν`: the same sites under `ν` are `13` and
`23`, and `507 > 529` fails. The extra corridor-slide clause is what
changes the axis arrival. On the hugging hop `(1,1,0) → (2,1,0)` one has
`|σ| : 2 → 2` and least nonzero `|w_i| = 1`, so `ν = 1` while `μ = 3`.
The leave-axis hop `(0,-1,0) → (1,-1,0)` stays at cost `1` under both
`ν` and `μ`. Therefore `ν` cannot price the axis-hugging slide, and the
`μ` scores below are not a leftover of `ν`. The site `(7,7,7)` has ℓ¹
norm `21`, so it is absent from `B_18(0)`. The `B_21(0)` table is
therefore not leftover of a smaller-ball table.

The rule is displayed, not adopted. Do not write `μ` or `ν` into Admissibility.
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
the least-nonzero-coordinate test, and the arrival function `t` are
separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_21(0) = { v ∈ Z^3 : |v|_1 ≤ 21 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_21(0)`,
`t(v)` is the least sum of `μ` along a directed path from `0` to `v` in
that graph.

The comparator `ν` uses only the first three clauses of `μ`. On the
axis-hugging slide `(1,1,0) → (2,1,0)` one has `|σ| : 2 → 2` and least
nonzero `|w_i| = 1`, so `ν = 1` while `μ = 3`. Therefore `ν` cannot price
the corridor slide, and the `μ` scores below are not a leftover of `ν`.

## Theorem 1 — Arrivals `t(7,0,0)` And `t(7,7,7)` On `B_21(0)`

One origin Dijkstra on `B_21(0)` returns the integer arrivals

| site | `t_μ` |
|---|---:|
| `(7,0,0)` | `17` |
| `(7,7,7)` | `23` |

Every listed site lies in `B_21(0)`. The site `(7,7,7)` has ℓ¹ norm `21`,
so it is absent from `B_18(0)`. The pair is computed on `B_21(0)`, not
copied from a smaller-ball table and not copied from the `ν` pair
`13` versus `23`. These values are Dijkstra outputs, not fitted scalars.

A witness walk of cost `17` from `0` to `(7,0,0)` is seed-exit `3` onto
`(0,-1,0)`, leave-axis `1` onto `(0,-1,-1)`, enter-body `1` onto
`(1,-1,-1)`, six support-preserving cost-`1` body hops to `(7,-1,-1)`,
support-drop `3` onto `(7,-1,0)`, and support-drop `3` onto `(7,0,0)`,
summing to `17`. That walk is a witness of cost `17`, not a uniqueness
claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=7`

The Euclidean-normalized comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

equivalently `3 t(7,0,0)^2 ? t(7,7,7)^2`. Substituting the computed times
gives `3 · 17^2 = 867` and `23^2 = 529`, so

`867 > 529` is true.

Arrival per Euclidean length is larger at `(7,0,0)` than at `(7,7,7)`.
Same-`k` reverse at `k=7` under `μ` is yes. The comparison is displayed,
not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `μ` is a displayed scoring device on `B_21(0)`. Do not write `μ` or `ν` into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_21(0) for one named hop-cost at k=7. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_21(0) for the displayed rule μ at k=7; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `μ` among hop-costs that reverse the same-`k` pair at `k=7`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_21(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=7`.
- Any reuse of the `ν` arrival table as a substitute for the `μ` Dijkstra.
- Any adoption of the leave-axis `1→2` clause as part of `μ`.
