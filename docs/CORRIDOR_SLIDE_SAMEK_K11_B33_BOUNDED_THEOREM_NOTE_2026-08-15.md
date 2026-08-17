---
claim_id: corridor_slide_samek_k11_b33_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=11 under the named corridor-slide hop-cost on B_33(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/corridor_slide_samek_k11_b33_2026_08_15.py
---

# Named Corridor-Slide Same-k Reverse At k=11 On B_33(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_33(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=11`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/corridor_slide_samek_k11_b33_2026_08_15.py`](../scripts/corridor_slide_samek_k11_b33_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named corridor-slide hop-cost `μ` is the already scored support-drop
rule `ν` plus cost `3` on a `2→2` hop whose destination has least nonzero
absolute coordinate equal to `1` (an axis-hugging slide). Same-`k` reverse
under `μ` holds at `k=10` (`20` versus `32`) and at `k=1` through `k=9`.
The linear pair `k+10` versus `3k+2` predicts hold through `k=12`.
Same-`k` reverse under `ν` fails at `k=11` (`17` versus `35`). The cheap
`ν` axis walk to `(11,0,0)` slides along a weight-`2` corridor with dest
height `1`, then drops onto the axis. That corridor hop costs `1` under
`ν`. `μ` prices that hop at `3`. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_33(0)`, the displayed
rule `μ` is

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`,

where `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first three clauses are seed-exit, both weights `1`, and support drop.
The fourth clause is the corridor slide. Those four clauses are the whole
rule.

One Dijkstra from the origin on `B_33(0)` (50183 sites; 50182 nonzero) gives

`t(11,0,0) = 21`, `t(11,11,11) = 35`.

The displayed same-`k` comparison at `k=11` is

`t(11,0,0)^2 / 121  ?  t(11,11,11)^2 / 363`,

which is `441/121` versus `1225/363`, or equivalently `1323 > 1225`. The
inequality holds. Same-`k` reverse at `k=11` under `μ` is yes. Independently,
the new axis site is `t(33,0,0) = 47`. The shared axis site
`t(30,0,0) = 40` is a `μ` score on this ball, not a `ν` leftover.

The pair is not leftover of `ν`: the same sites under `ν` are `17` versus
`35`, and the extra corridor-slide clause is what changes the axis time.
The site `(11,11,11)` has ℓ¹ norm `33`, so it is absent from `B_30(0)`. The
`B_33(0)` table is therefore not leftover of the `B_30(0)` times.

The rule is displayed, not adopted. Do not write `μ` into Admissibility.
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
the least-nonzero-coordinate clause, and the arrival function `t` are
separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_33(0) = { v ∈ Z^3 : |v|_1 ≤ 33 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_33(0)`,
`t(v)` is the least sum of `μ` along a directed path from `0` to `v` in
that graph.

The comparator `ν` uses only the first three clauses of `μ`. On the
corridor-slide hop `(1,1,0) → (2,1,0)` one has `|σ| : 2 → 2` and least
nonzero `|w_i| = 1`, so `ν = 1` while `μ = 3`. Therefore `ν` cannot price corridor slide,
and the `μ` scores below are not a leftover of `ν`.

## Theorem 1 — Arrivals `t(11,0,0)` And `t(11,11,11)` On `B_33(0)`

One origin Dijkstra on `B_33(0)` returns the integer arrivals

| site | `t_μ` |
|---|---:|
| `(11,0,0)` | `21` |
| `(11,11,11)` | `35` |

Every listed site lies in `B_33(0)`. The site `(11,11,11)` has ℓ¹ norm `33`,
so it is absent from `B_30(0)`. The pair is computed on `B_33(0)`, not
copied from a smaller-ball table and not copied from the `ν` pair
`17` versus `35`. These values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `21` is seed-exit `3` onto `(1,0,0)`,
support-increase `1` onto `(1,1,0)`, support-increase `1` onto `(1,1,1)`,
ten support-preserving cost-`1` body hops to `(11,1,1)`, and two
support-drops `3` then `3` onto `(11,0,0)`, summing to `21`. That walk is
a witness of cost `21`, not a uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=11`

The Euclidean-normalized comparison at `k=11` is

`t(11,0,0)^2 / 121  ?  t(11,11,11)^2 / 363`,

equivalently `3 t(11,0,0)^2 ? t(11,11,11)^2`. Substituting the computed times
gives `3 · 21^2 = 1323` and `35^2 = 1225`, so

`1323 > 1225`.

Arrival per Euclidean length is larger at `(11,0,0)` than at `(11,11,11)`.
Same-`k` reverse at `k=11` under `μ` is yes. The comparison is displayed,
not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `μ` is a displayed scoring device on `B_33(0)`. Do not write `μ`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_33(0) for one named hop-cost at k=11. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_33(0) for the displayed rule μ at k=11; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `μ` among hop-costs that reverse the same-`k` pair at `k=11`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_33(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=11`.
- Any reuse of the `ν` arrival table as a substitute for the `μ` Dijkstra.
