---
claim_id: enter_body_samek_k13_b39_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=13 under the named enter-body hop-cost on B_39(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/enter_body_samek_k13_b39_2026_08_15.py
---

# Named Enter-Body Same-k Reverse At k=13 On B_39(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_39(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=13`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/enter_body_samek_k13_b39_2026_08_15.py`](../scripts/enter_body_samek_k13_b39_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named enter-body hop-cost `ε` is the already scored corridor-slide
rule `μ` plus cost `3` on a `2→3` hop. Same-`k` reverse under `μ` fails at
`k=13` (`23` versus `41`). The cheap `μ` body walk to `(13,13,13)` enters
weight-`3` from a weight-`2` face at cost `1`. `ε` prices that hop at `3`.
Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_39(0)`, the displayed
rule `ε` is

`ε(v→w) = 3` if `μ` would be `3` or `(|σ_v|=2` and `|σ_w|=3)`, else `1`,

where `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`,

and `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first three clauses are seed-exit, both weights `1`, and support drop.
The fourth clause is the corridor slide. The fifth clause is enter-body.
Those five clauses are the whole rule.

One Dijkstra from the origin on `B_39(0)` (82239 sites; 82238 nonzero) gives

`t(13,0,0) = 25`, `t(13,13,13) = 43`.

The displayed same-`k` comparison at `k=13` is

`t(13,0,0)^2 / 169  ?  t(13,13,13)^2 / 507`,

which is `625/169` versus `1849/507`, or equivalently `1875 > 1849`. The
inequality holds. Same-`k` reverse at `k=13` under `ε` is yes. The `μ`
fail at the `k=13` wall does not continue under `ε`. Independently, the
new axis site is `t(39,0,0) = 55`. The shared axis site
`t(36,0,0) = 48` is an `ε` score on this ball, not a `μ` leftover.

The pair is not leftover of `μ`: the same sites under `μ` are `23` and
`41`, and the extra enter-body clause is what changes both times. The
site `(13,13,13)` has ℓ¹ norm `39`, so it is absent from `B_36(0)`. The
`B_39(0)` table is therefore not leftover of the `B_36(0)` times.

The rule is displayed, not adopted. Do not write `ε` into Admissibility.
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

Let `B_39(0) = { v ∈ Z^3 : |v|_1 ≤ 39 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_39(0)`,
`t(v)` is the least sum of `ε` along a directed path from `0` to `v` in
that graph.

The comparator `μ` uses only the first four clauses of `ε`. On the
enter-body hop `(1,1,0) → (1,1,1)` one has `|σ| : 2 → 3`, so `μ = 1`
while `ε = 3`. Therefore `μ` cannot price enter body, and the `ε` scores
below are not a leftover of `μ`.

## Theorem 1 — Arrivals `t(13,0,0)` And `t(13,13,13)` On `B_39(0)`

One origin Dijkstra on `B_39(0)` returns the integer arrivals

| site | `t_ε` |
|---|---:|
| `(13,0,0)` | `25` |
| `(13,13,13)` | `43` |

Every listed site lies in `B_39(0)`. The site `(13,13,13)` has ℓ¹ norm `39`,
so it is absent from `B_36(0)`. The pair is computed on `B_39(0)`, not
copied from a smaller-ball table and not copied from the `μ` pair
`23` versus `41`. These values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `25` is seed-exit `3` onto `(1,0,0)`,
support-increase `1` onto `(1,1,0)`, enter-body `3` onto `(1,1,1)`,
twelve support-preserving cost-`1` body hops to `(13,1,1)`, and two
support-drops `3` then `3` onto `(13,0,0)`, summing to `25`. That walk is
a witness of cost `25`, not a uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=13`

The Euclidean-normalized comparison at `k=13` is

`t(13,0,0)^2 / 169  ?  t(13,13,13)^2 / 507`,

equivalently `3 t(13,0,0)^2 ? t(13,13,13)^2`. Substituting the computed times
gives `3 · 25^2 = 1875` and `43^2 = 1849`, so

`1875 > 1849`.

Arrival per Euclidean length is larger at `(13,0,0)` than at `(13,13,13)`.
Same-`k` reverse at `k=13` under `ε` is yes. The inequality holds. The
comparison is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ε` is a displayed scoring device on `B_39(0)`. Do not write `ε`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_39(0) for one named hop-cost at k=13. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_39(0) for the displayed rule ε at k=13; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ε` among hop-costs that reverse the same-`k` pair at `k=13`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_39(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=13`.
- Any reuse of the `μ` arrival table as a substitute for the `ε` Dijkstra.
