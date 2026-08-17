---
claim_id: corridor_slide_samek_k8_b24_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=8 under the named corridor-slide hop-cost on B_24(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/corridor_slide_samek_k8_b24_2026_08_15.py
---

# Named Corridor-Slide Same-k Reverse At k=8 On B_24(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_24(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=8`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/corridor_slide_samek_k8_b24_2026_08_15.py`](../scripts/corridor_slide_samek_k8_b24_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named corridor-slide hop-cost `μ` is the already scored support-drop
rule `ν` plus cost `3` on a `2→2` hop whose destination has least nonzero
absolute coordinate equal to `1` (an axis-hugging slide). Same-`k` reverse
under `μ` holds at `k=7` (`17` versus `23`) and at `k=1` (`3` versus `5`).
Same-`k` reverse under `ν` fails at `k=8` (`14` versus `26`). The cheap
`ν` axis walk to `(8,0,0)` slides along a weight-`2` corridor with dest
height `1`, then drops onto the axis. That corridor hop costs `1` under
`ν`. `μ` prices that hop at `3`. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_24(0)`, the displayed
rule `μ` is

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`,

where `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first three clauses are seed-exit, both weights `1`, and support drop.
The fourth clause is the corridor slide. Those four clauses are the whole
rule.

One Dijkstra from the origin on `B_24(0)` (19649 sites; 19648 nonzero) gives

`t(8,0,0) = 18`, `t(8,8,8) = 26`.

The displayed same-`k` comparison at `k=8` is

`t(8,0,0)^2 / 64  ?  t(8,8,8)^2 / 192`,

which is `324/64` versus `676/192`, or equivalently `972 > 676`. The
inequality holds. Same-`k` reverse at `k=8` under `μ` is yes. Independently,
the new axis site is `t(24,0,0) = 38`. The shared axis site
`t(21,0,0) = 31` is a `μ` score on this ball, not a `ν` leftover.

The pair is not leftover of `ν`: the same sites under `ν` are `14` versus
`26`, and the extra corridor-slide clause is what changes the axis time.
The site `(8,8,8)` has ℓ¹ norm `24`, so it is absent from `B_21(0)`. The
`B_24(0)` table is therefore not leftover of the `B_21(0)` times.

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

Let `B_24(0) = { v ∈ Z^3 : |v|_1 ≤ 24 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_24(0)`,
`t(v)` is the least sum of `μ` along a directed path from `0` to `v` in
that graph.

The comparator `ν` uses only the first three clauses of `μ`. On the
corridor-slide hop `(1,1,0) → (2,1,0)` one has `|σ| : 2 → 2` and least
nonzero `|w_i| = 1`, so `ν = 1` while `μ = 3`. Therefore `ν` cannot price corridor slide,
and the `μ` scores below are not a leftover of `ν`.

## Theorem 1 — Arrivals `t(8,0,0)` And `t(8,8,8)` On `B_24(0)`

One origin Dijkstra on `B_24(0)` returns the integer arrivals

| site | `t_μ` |
|---|---:|
| `(8,0,0)` | `18` |
| `(8,8,8)` | `26` |

Every listed site lies in `B_24(0)`. The site `(8,8,8)` has ℓ¹ norm `24`,
so it is absent from `B_21(0)`. The pair is computed on `B_24(0)`, not
copied from a smaller-ball table and not copied from the `ν` pair
`14` versus `26`. These values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `18` is seed-exit `3` onto `(1,0,0)`,
support-increase `1` onto `(1,1,0)`, support-increase `1` onto `(1,1,1)`,
seven support-preserving cost-`1` body hops to `(8,1,1)`, and two
support-drops `3` then `3` onto `(8,0,0)`, summing to `18`. That walk is
a witness of cost `18`, not a uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=8`

The Euclidean-normalized comparison at `k=8` is

`t(8,0,0)^2 / 64  ?  t(8,8,8)^2 / 192`,

equivalently `3 t(8,0,0)^2 ? t(8,8,8)^2`. Substituting the computed times
gives `3 · 18^2 = 972` and `26^2 = 676`, so

`972 > 676`.

Arrival per Euclidean length is larger at `(8,0,0)` than at `(8,8,8)`.
Same-`k` reverse at `k=8` under `μ` is yes. The comparison is displayed,
not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `μ` is a displayed scoring device on `B_24(0)`. Do not write `μ`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_24(0) for one named hop-cost at k=8. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_24(0) for the displayed rule μ at k=8; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `μ` among hop-costs that reverse the same-`k` pair at `k=8`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_24(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=8`.
- Any reuse of the `ν` arrival table as a substitute for the `μ` Dijkstra.
