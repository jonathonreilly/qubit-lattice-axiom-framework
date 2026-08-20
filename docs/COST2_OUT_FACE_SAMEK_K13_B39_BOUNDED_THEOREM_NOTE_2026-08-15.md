---
claim_id: cost2_out_face_samek_k13_b39_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=13 under the named cost-2 out-face hop-cost on B_39(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost2_out_face_samek_k13_b39_2026_08_15.py
---

# Named Cost-2 Out-Face Same-`k` Reverse At `k=13` On `B_39(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_39(0)`,
scored only for the same-`k` pair `t(13,0,0)` versus `t(13,13,13)`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/cost2_out_face_samek_k13_b39_2026_08_15.py`](../scripts/cost2_out_face_samek_k13_b39_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_39(0)`, the stacked
rules `ν`, `μ`, and `ρ3` are

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
`|w_i|` equals `1)`, else `1`;

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

The displayed cost-2 out-face rule `w2` is `ρ3` plus cost `2` (not `3`) on
a `2→2` hop whose destination has a larger max absolute coordinate than
the source:

`w2(v→w) = 3` if `ρ3` would be `3`, else `2` if `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|)`, else `1`.

Those clauses are the whole rule. Uniqueness is not claimed. This note is
the first display of same-`k` at `k=13` under `w2`. The same origin
Dijkstra also returns the already displayed `k=1` pair `t(1,0,0) = 3` and
`t(1,1,1) = 5`, so `w2` keeps `k=1`.

The parent box-growth hop `(1,1,0) → (2,1,0)` still has `|σ|=2→2` and
`max |w_i|=2 > max |v_i|=1`, but `μ` already taxes it (`ρ3=3`), so
`w2=3`. The new cost-`2` clause is not leftover of `ρ3`: the interior
face-growth hop `(2,2,0) → (3,2,0)` has `ρ3=1` and `w2=2`. The same hop
is a `w2` cost-`2` step, and `t(3,2,0) = 10`.

One Dijkstra from the origin on `B_39(0)` (82239 sites; 82238 nonzero)
returns

| site | `t_{w2}` |
|---|---:|
| `(13,0,0)` | `29` |
| `(13,13,13)` | `43` |

The same-`k` comparison at `k=13` is

`t(13,0,0)^2 / 169  ?  t(13,13,13)^2 / 507`,

which is `841/169` versus `1849/507`, or equivalently `3 t(13,0,0)^2 ?
t(13,13,13)^2`. Substituting the computed times gives `3 · 29^2 = 2523`
and `43^2 = 1849`, so `2523 > 1849`. The inequality holds. Same-`k`
reverse at `k=13` is yes.

A cheapest body walk uses no `2→2` face-growth hop, so the body arrival
stays `43`. The `k=1` geodesic `0 → (1,0,0) → (1,1,0) → (1,1,1)` uses
`w2` costs `3,1,1` and never takes a `2→2` face-growth hop.

The site `(13,13,13)` has ℓ¹ norm `39`, so it is absent from `B_36(0)`.
The `B_39(0)` table is therefore not leftover of the `B_36(0)` times.
Independently, the new axis site is `t(39,0,0) = 60`. The shared axis
site `t(36,0,0) = 52` is a `w2` score on this ball.

The rule is displayed, not adopted. Do not write `w2` into Admissibility.
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
none of the hop costs. The integers `3`, `2`, and `1`, the support-size and
max-coordinate clauses, and the arrival function `t` are separately displayed
mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_39(0) = { v ∈ Z^3 : |v|_1 ≤ 39 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_39(0)`,
`t(v)` is the least sum of `w2` along a directed path from `0` to `v` in
that graph.

The first `ν` clause is seed-exit. The second is both weights `1`. The third
is support drop. The `μ` addendum taxes a `2→2` hop whose destination still
touches a unit coordinate. The `ρ3` addendum taxes a `3→3` hop whose
destination has exactly two unit coordinates. The `w2` addendum taxes a
`2→2` hop that grows the coordinate box on a face at cost `2` rather than
cost `3`.

The sites `(13,0,0)` and `(13,13,13)` both lie in `B_39(0)`: their ℓ¹
norms are `13` and `39`. The pair is computed on this ball by one origin
Dijkstra. These values are Dijkstra outputs, not fitted scalars.

## Theorem 1 — Arrivals At `k=13` Under `w2`

One origin Dijkstra on `B_39(0)` returns `t(13,0,0) = 29` and
`t(13,13,13) = 43`. Both sites lie in `B_39(0)`. The site `(13,13,13)`
has ℓ¹ norm `39`, so it is absent from `B_36(0)`. The pair is computed
on `B_39(0)`, not copied from a smaller-ball table and not copied from a
`ρ3` table. These values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `29` is seed-exit `3` onto `(1,0,0)`,
leave-axis `1` onto `(1,1,0)`, enter-body `1` onto `(1,1,1)`, ridge-slide
`3` onto `(2,1,1)`, support-preserving cost-`1` hop onto `(2,2,1)`, eleven
support-preserving cost-`1` body hops to `(13,2,1)`, ridge-slide `3` onto
`(13,1,1)`, support-drop `3` onto `(13,1,0)`, and support-drop `3` onto
`(13,0,0)`, summing to `29`. That walk is a witness of cost `29`, not a
uniqueness claim. The pure axis 1-skeleton walk costs `39` and is not
cheapest.

A witness body walk of cost `43` is the same prefix of cost `9` to
`(2,2,1)`, eleven cost-`1` body hops to `(13,2,1)`, eleven cost-`1` body
hops to `(13,13,1)`, and twelve support-preserving cost-`1` body hops to
`(13,13,13)`, summing to `43`. Those last hops have dest with only one
absolute coordinate equal to `1`, or with all three coordinates large, so
they are not unit-height ridges and are not out-face `2→2` grows. That
walk is a witness of cost `43`, not a uniqueness claim.

A witness walk of cost `10` to `(3,2,0)` is seed-exit `3` onto `(1,0,0)`,
leave-axis `1` onto `(1,1,0)`, corridor-slide `3` onto `(2,1,0)`,
equalize `1` onto `(2,2,0)`, and out-face grow `2` onto `(3,2,0)`.

## Theorem 2 — Reverse At The Same-`k` Pair `k=13`

The Euclidean-normalized comparison at `k=13` is

`t(13,0,0)^2 / 169  ?  t(13,13,13)^2 / 507`,

equivalently `3 t(13,0,0)^2 ? t(13,13,13)^2`. Substituting the computed
times gives `3 · 29^2 = 2523` and `43^2 = 1849`, so

`2523 > 1849`.

Arrival per Euclidean length is larger at `(13,0,0)` than at
`(13,13,13)`. Same-`k` reverse at `k=13` does hold. The comparison is
displayed, not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `w2` is a displayed scoring device on `B_39(0)`. Do not write `w2`
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
conditional_surface_status: "exact on B_39(0) for the displayed rule w2 at k=13; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `w2` among hop-costs that reverse any same-`k` pair.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_39(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=13`.
- Any adoption of `w2` as an admissibility rule.
- Any reuse of a `ρ3` arrival table as a substitute for the `w2` Dijkstra.
