---
claim_id: ridge_slide_samek_k14_b42_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=14 under the named ridge-slide hop-cost on B_42(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ridge_slide_samek_k14_b42_2026_08_15.py
---

# Named Ridge-Slide Same-k Reverse At k=14 On B_42(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_42(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=14`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/ridge_slide_samek_k14_b42_2026_08_15.py`](../scripts/ridge_slide_samek_k14_b42_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named ridge-slide hop-cost `ρ3` is the already scored corridor-slide
rule `μ` plus cost `3` on a `3→3` hop whose destination has exactly two
absolute coordinates equal to `1` (a ridge slide). Same-`k` reverse under
`ρ3` holds at `k=13` (`25` versus `43`). The residual scored here is
whether `ρ3` still reverses at `k=14` on `B_42(0)`. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_42(0)`, the displayed
rule `ρ3` is

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`,

where `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`, and
`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first three clauses are seed-exit, both weights `1`, and support drop.
The fourth clause is the axis-hugging `2→2` corridor slide. The fifth
clause is the ridge slide. Those five clauses are the whole rule.

One Dijkstra from the origin on `B_42(0)` (102425 sites; 102424 nonzero)
gives

`t(14,0,0) = 26`, `t(14,14,14) = 46`.

The displayed same-`k` comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

which is `676/196` versus `2116/588`, or equivalently `2028 > 2116`. The
inequality does not hold. Same-`k` reverse at `k=14` under `ρ3` is no.
Independently, the new axis site is `t(42,0,0) = 58`. The shared axis site
`t(39,0,0) = 51` is a `ρ3` score on this ball, not a `μ` leftover.

The pair is not leftover of `μ`: the same sites under `μ` are `24` versus
`44`, and the extra ridge-slide clause is what changes both arrivals. On
the ridge hop `(1,1,1) → (2,1,1)` one has `|σ| : 3 → 3` and exactly two
`|w_i| = 1`, so `μ = 1` while `ρ3 = 3`. Therefore `μ` cannot price the ridge slide,
and the `ρ3` scores below are not a leftover of `μ`. The site `(14,14,14)`
has ℓ¹ norm `42`, so it is absent from `B_39(0)`. The `B_42(0)` table is
therefore not leftover of the `B_39(0)` times.

The rule is displayed, not adopted. Do not write `ρ3` into Admissibility.
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
the least-nonzero-coordinate clause, the two-unit-height ridge clause, and
the arrival function `t` are separately displayed mathematical inputs. No
axiom text is edited.

## Named Rule

Let `B_42(0) = { v ∈ Z^3 : |v|_1 ≤ 42 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_42(0)`,
`t(v)` is the least sum of `ρ3` along a directed path from `0` to `v` in
that graph.

The comparator `μ` uses only the first four clauses of `ρ3`. On the
ridge-slide hop `(1,1,1) → (2,1,1)` one has `|σ| : 3 → 3` and exactly two
`|w_i| = 1`, so `μ = 1` while `ρ3 = 3`. Therefore `μ` cannot price the ridge slide,
and the `ρ3` scores below are not a leftover of `μ`.

## Theorem 1 — Arrivals `t(14,0,0)` And `t(14,14,14)` On `B_42(0)`

One origin Dijkstra on `B_42(0)` returns the integer arrivals

| site | `t_ρ3` |
|---|---:|
| `(14,0,0)` | `26` |
| `(14,14,14)` | `46` |

Every listed site lies in `B_42(0)`. The site `(14,14,14)` has ℓ¹ norm `42`,
so it is absent from `B_39(0)`. The pair is computed on `B_42(0)`, not
copied from a smaller-ball table and not copied from the `μ` pair
`24` versus `44`. These values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `26` is seed-exit `3` onto `(1,0,0)`,
leave-axis `1` onto `(1,1,0)`, hugging corridor-slide `3` onto `(2,1,0)`,
non-hugging face hop `1` onto `(2,2,0)`, twelve support-preserving
cost-`1` face hops to `(14,2,0)`, hugging slide `3` onto `(14,1,0)`, and
support-drop `3` onto `(14,0,0)`, summing to `26`. That walk is a witness
of cost `26`, not a uniqueness claim.

A witness body walk of cost `46` is the same prefix of cost `8` to
`(2,2,0)`, twelve cost-`1` face hops to `(14,2,0)`, twelve cost-`1` face
hops to `(14,14,0)`, enter-body `1` onto `(14,14,1)`, and thirteen
support-preserving cost-`1` body hops to `(14,14,14)`, summing to `46`.
Those last hops have dest with only one absolute coordinate equal to `1`,
so they are not ridge slides. That walk is a witness of cost `46`, not a
uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=14`

The Euclidean-normalized comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

equivalently `3 t(14,0,0)^2 ? t(14,14,14)^2`. Substituting the computed times
gives `3 · 26^2 = 2028` and `46^2 = 2116`, so

`2028 > 2116` is false; `2028 < 2116`.

Arrival per Euclidean length is larger at `(14,14,14)` than at `(14,0,0)`.
Same-`k` reverse at `k=14` under `ρ3` is no. The comparison is displayed,
not adopted. The inequality does not hold.

## Theorem 3 — Displayed, Not Adopted

The rule `ρ3` is a displayed scoring device on `B_42(0)`. Do not write `ρ3`
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
conditional_surface_status: "exact on B_42(0) for the displayed rule ρ3 at k=14; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ρ3` among hop-costs that score the same-`k` pair at `k=14`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_42(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=14`.
- Any reuse of the `μ` arrival table as a substitute for the `ρ3` Dijkstra.
- Membership of `ρ3` as a physical hop-cost. Reverse at `k=14` on this ball
  is a displayed comparison, not an adoption.
