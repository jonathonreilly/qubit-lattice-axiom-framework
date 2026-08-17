---
claim_id: height_ridge_samek_k13_b39_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=13 under the named height-ridge hop-cost on B_39(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/height_ridge_samek_k13_b39_2026_08_15.py
---

# Named Height-Ridge Same-k Reverse At k=13 On B_39(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_39(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=13`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/height_ridge_samek_k13_b39_2026_08_15.py`](../scripts/height_ridge_samek_k13_b39_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named height-ridge hop-cost `ζ` is the already scored ridge-slide
rule `ρ3` plus cost `3` on a `3→3` hop whose destination has exactly two
absolute coordinates equal to `m`, with `m` the least absolute coordinate
and `m ≥ 2` (a height-`m` ridge). Same-`k` reverse under `ρ3` holds at
`k=13` (`25` versus `43`). The residual scored here is whether `ζ` still
reverses at `k=13` on `B_39(0)`. First display of `ζ` at `k=13`.
Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_39(0)`, the displayed
rule `ζ` is

`ζ(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `m` and `m = min_j |w_j|` and `m ≥ 2)`, else `1`,

where `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly
two `|w_i|` equal `1)`, else `1`,
`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`, and
`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first three clauses are seed-exit, both weights `1`, and support drop.
The fourth clause is the axis-hugging `2→2` corridor slide. The fifth
clause is the unit-height ridge slide. The sixth clause is the height-`m`
ridge for `m ≥ 2`. Those six clauses are the whole rule.

One Dijkstra from the origin on `B_39(0)` (82239 sites; 82238 nonzero) gives

`t(13,0,0) = 25`, `t(13,13,13) = 43`.

The displayed same-`k` comparison at `k=13` is

`t(13,0,0)^2 / 169  ?  t(13,13,13)^2 / 507`,

which is `625/169` versus `1849/507`, or equivalently `1875 > 1849`. The
inequality holds. Same-`k` reverse at `k=13` under `ζ` is yes.
Independently, the new axis site is `t(39,0,0) = 55`. The shared axis
site `t(36,0,0) = 48` is a `ζ` score on this ball.

The same-`k` pair under `ρ3` is also `25` versus `43`. That match is not
a leftover of a `ρ3` table: the extra height-`m` ridge clause is live on
the ball. On the height-`2` ridge hop `(2,2,2) → (3,2,2)` one has
`|σ| : 3 → 3`, exactly two `|w_i|` equal to `2`, and `min_j |w_j| = 2`,
so `ρ3 = 1` while `ζ = 3`. Therefore `ρ3` cannot price the height-`m`
ridge. The same hop is a `ζ` cost-`3` step, and `t(3,2,2) = 13` under
`ζ`. A cheapest `ζ` walk to `(13,13,13)` uses no height-`m` ridge hop,
so the same-`k` pair stays `25` versus `43`. The site `(13,13,13)` has
ℓ¹ norm `39`, so it is absent from `B_36(0)`. The `B_39(0)` table is
therefore not leftover of the `B_36(0)` times.

The rule is displayed, not adopted. Do not write `ζ` into Admissibility.
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
the least-nonzero-coordinate clause, the unit-height ridge clause, the
height-`m` ridge clause for `m ≥ 2`, and the arrival function `t` are
separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_39(0) = { v ∈ Z^3 : |v|_1 ≤ 39 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_39(0)`,
`t(v)` is the least sum of `ζ` along a directed path from `0` to `v` in
that graph.

The comparator `ρ3` uses only the first five clauses of `ζ`. On the
height-`2` ridge hop `(2,2,2) → (3,2,2)` one has `|σ| : 3 → 3` and
exactly two `|w_i|` equal to the least absolute coordinate `2`, so
`ρ3 = 1` while `ζ = 3`. Therefore `ρ3` cannot price the height-`m`
ridge, and the `ζ` scores below are not a leftover of `ρ3`. On the
unit-height ridge hop `(1,1,1) → (2,1,1)` both `ρ3` and `ζ` cost `3`.
On the interior body hop `(13,13,1) → (13,13,2)` the destination has
only one absolute coordinate equal to its least absolute coordinate, so
both `ρ3` and `ζ` cost `1`.

## Theorem 1 — Arrivals `t(13,0,0)` And `t(13,13,13)` On `B_39(0)`

One origin Dijkstra on `B_39(0)` returns the integer arrivals

| site | `t_ζ` |
|---|---:|
| `(13,0,0)` | `25` |
| `(13,13,13)` | `43` |

Every listed site lies in `B_39(0)`. The site `(13,13,13)` has ℓ¹ norm `39`,
so it is absent from `B_36(0)`. The pair is computed on `B_39(0)`, not
copied from a smaller-ball table and not copied from a `ρ3` table. These
values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `25` is seed-exit `3` onto `(1,0,0)`,
leave-axis `1` onto `(1,1,0)`, hugging corridor-slide `3` onto `(2,1,0)`,
non-hugging face hop `1` onto `(2,2,0)`, eleven support-preserving
cost-`1` face hops to `(13,2,0)`, hugging slide `3` onto `(13,1,0)`, and
support-drop `3` onto `(13,0,0)`, summing to `25`. That walk is a witness
of cost `25`, not a uniqueness claim.

A witness body walk of cost `43` is the same prefix of cost `8` to
`(2,2,0)`, eleven cost-`1` face hops to `(13,2,0)`, eleven cost-`1` face
hops to `(13,13,0)`, enter-body `1` onto `(13,13,1)`, and twelve
support-preserving cost-`1` body hops to `(13,13,13)`, summing to `43`.
Those last hops have dest with only one absolute coordinate equal to the
least absolute coordinate, or with all three equal, so they are not
height-`m` ridges. That walk is a witness of cost `43`, not a uniqueness
claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=13`

The Euclidean-normalized comparison at `k=13` is

`t(13,0,0)^2 / 169  ?  t(13,13,13)^2 / 507`,

equivalently `3 t(13,0,0)^2 ? t(13,13,13)^2`. Substituting the computed times
gives `3 · 25^2 = 1875` and `43^2 = 1849`, so

`1875 > 1849` is true; `1875 > 1849` holds.

Arrival per Euclidean length is larger at `(13,0,0)` than at
`(13,13,13)`. Same-`k` reverse at `k=13` under `ζ` is yes. The comparison
is displayed, not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `ζ` is a displayed scoring device on `B_39(0)`. Do not write `ζ`
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
conditional_surface_status: "exact on B_39(0) for the displayed rule ζ at k=13; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ζ` among hop-costs that reverse the same-`k` pair at `k=13`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_39(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=13`.
- Any reuse of a `ρ3` arrival table as a substitute for the `ζ` Dijkstra.
