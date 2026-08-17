---
claim_id: corridor_slide_samek_k14_b42_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=14 under the named corridor-slide hop-cost on B_42(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/corridor_slide_samek_k14_b42_2026_08_15.py
---

# Named Corridor-Slide Same-k Reverse At k=14 On B_42(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_42(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=14`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/corridor_slide_samek_k14_b42_2026_08_15.py`](../scripts/corridor_slide_samek_k14_b42_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named corridor-slide hop-cost `μ` is the already scored support-drop
rule `ν` plus cost `3` on a `2→2` hop whose destination has least nonzero
absolute coordinate equal to `1` (an axis-hugging slide). Linear arrivals
under `μ` for `k≥6` are `t(k,0,0)=k+10` and `t(k,k,k)=3k+2`, which already
predict that same-`k` reverse dies at `k=13` (`23` versus `41`). The same
formulas continue at `k=14` (`24` versus `44`). Same-`k` reverse under `ν`
fails at `k=14` (`20` versus `44`). The cheap `ν` axis walk to `(14,0,0)`
slides along a weight-`2` corridor with dest height `1`, then drops onto
the axis. That corridor hop costs `1` under `ν`. `μ` prices that hop at
`3`. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_42(0)`, the displayed
rule `μ` is

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`,

where `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first three clauses are seed-exit, both weights `1`, and support drop.
The fourth clause is the corridor slide. Those four clauses are the whole
rule.

One Dijkstra from the origin on `B_42(0)` (102425 sites; 102424 nonzero) gives

`t(14,0,0) = 24`, `t(14,14,14) = 44`.

The displayed same-`k` comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

which is `576/196` versus `1936/588`, or equivalently `1728 > 1936`. The
inequality does not hold. Same-`k` reverse at `k=14` under `μ` is no. The
fail continues at `k=14` on `B_42(0)`. Independently, the new axis site is
`t(42,0,0) = 56`. The shared axis site `t(39,0,0) = 49` is a `μ` score on
this ball, not a `ν` leftover.

The pair is not leftover of `ν`: the same sites under `ν` are `20` versus
`44`, and the extra corridor-slide clause is what changes the axis time.
The site `(14,14,14)` has ℓ¹ norm `42`, so it is absent from `B_39(0)`. The
`B_42(0)` table is therefore not leftover of the `B_39(0)` times.

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

Let `B_42(0) = { v ∈ Z^3 : |v|_1 ≤ 42 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_42(0)`,
`t(v)` is the least sum of `μ` along a directed path from `0` to `v` in
that graph.

The comparator `ν` uses only the first three clauses of `μ`. On the
corridor-slide hop `(1,1,0) → (2,1,0)` one has `|σ| : 2 → 2` and least
nonzero `|w_i| = 1`, so `ν = 1` while `μ = 3`. Therefore `ν` cannot price corridor slide,
and the `μ` scores below are not a leftover of `ν`.

## Theorem 1 — Arrivals `t(14,0,0)` And `t(14,14,14)` On `B_42(0)`

One origin Dijkstra on `B_42(0)` returns the integer arrivals

| site | `t_μ` |
|---|---:|
| `(14,0,0)` | `24` |
| `(14,14,14)` | `44` |

Every listed site lies in `B_42(0)`. The site `(14,14,14)` has ℓ¹ norm `42`,
so it is absent from `B_39(0)`. The pair is computed on `B_42(0)`, not
copied from a smaller-ball table and not copied from the `ν` pair
`20` versus `44`. These values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `24` is seed-exit `3` onto `(1,0,0)`,
support-increase `1` onto `(1,1,0)`, support-increase `1` onto `(1,1,1)`,
thirteen support-preserving cost-`1` body hops to `(14,1,1)`, and two
support-drops `3` then `3` onto `(14,0,0)`, summing to `24`. That walk is
a witness of cost `24`, not a uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=14`

The Euclidean-normalized comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

equivalently `3 t(14,0,0)^2 ? t(14,14,14)^2`. Substituting the computed times
gives `3 · 24^2 = 1728` and `44^2 = 1936`, so

`1728 > 1936` is false.

Arrival per Euclidean length is not larger at `(14,0,0)` than at
`(14,14,14)`. Same-`k` reverse at `k=14` under `μ` is no. The comparison
is displayed, not adopted. The inequality does not hold.

## Theorem 3 — Displayed, Not Adopted

The rule `μ` is a displayed scoring device on `B_42(0)`. Do not write `μ`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_42(0) for one named hop-cost at k=14. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_42(0) for the displayed rule μ at k=14; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `μ` among hop-costs that reverse the same-`k` pair at `k=14`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_42(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=14`.
- Any reuse of the `ν` arrival table as a substitute for the `μ` Dijkstra.
