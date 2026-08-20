---
claim_id: out_face_samek_k17_b51_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=17 under the named out-face hop-cost on B_51(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/out_face_samek_k17_b51_2026_08_15.py
---

# Named Out-Face Same-`k` Reverse At `k=17` On `B_51(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_51(0)`,
scored only for the same-`k` pair `t(17,0,0)` versus `t(17,17,17)`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/out_face_samek_k17_b51_2026_08_15.py`](../scripts/out_face_samek_k17_b51_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_51(0)`, the stacked
rules `ν`, `μ`, and `ρ3` are

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
`|w_i|` equals `1)`, else `1`;

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

The displayed out-face rule `ω` is `ρ3` plus cost `3` on a `2→2` hop whose
destination has a larger max absolute coordinate than the source:

`ω(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|)`, else `1`.

Those clauses are the whole rule. Uniqueness is not claimed. This note is
the first display of same-`k` reverse at `k=17` under `ω`.

A mid-leave clause that would cost `3` on a `1→2` hop with destination max
absolute coordinate `1` and source max at least `2` cannot fire on the
six-neighbor graph: a cubic step never realizes both of those max conditions
together with `|σ_v|=1` and `|σ_w|=2`. The out-face hop
`(1,1,0) → (2,1,0)` does fire: `|σ|=2→2` and `max |w_i|=2 > max |v_i|=1`,
so `ω=3`. Independently, `ω` is not leftover of `ρ3`: the interior
face-growth hop `(2,2,0) → (3,2,0)` has `ρ3=1` and `ω=3`.

One Dijkstra from the origin on `B_51(0)` (182207 sites; 182206 nonzero)
returns

| site | `t_ω` |
|---|---:|
| `(17,0,0)` | `33` |
| `(17,17,17)` | `55` |

The same-`k` comparison at `k=17` is

`t(17,0,0)^2 / 289  ?  t(17,17,17)^2 / 867`,

equivalently `3 t(17,0,0)^2 ? t(17,17,17)^2`. Substituting the computed times
gives `3267 > 3025`. Same-`k` reverse at `k=17` is yes.

The site `(17,17,17)` has ℓ¹ norm `51`, so it is absent from `B_48(0)`.
The `B_51(0)` table is therefore not leftover of the `B_48(0)` times.
Independently, the new axis site is `t(51,0,0) = 73`. The shared axis site
`t(48,0,0) = 64` is an `ω` score on this ball.

The rule is displayed, not adopted. Do not write `ω` into Admissibility.
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
none of the hop costs. The integers `3` and `1`, the support-size and
max-coordinate clauses, and the arrival function `t` are separately displayed
mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_51(0) = { v ∈ Z^3 : |v|_1 ≤ 51 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_51(0)`,
`t(v)` is the least sum of `ω` along a directed path from `0` to `v` in
that graph.

The first `ν` clause is seed-exit. The second is both weights `1`. The third
is support drop. The `μ` addendum taxes a `2→2` hop whose destination still
touches a unit coordinate. The `ρ3` addendum taxes a `3→3` hop whose
destination has exactly two unit coordinates. The `ω` addendum taxes a
`2→2` hop that grows the coordinate box on a face.

The site `(17,0,0)` has ℓ¹ norm `17` and therefore also lies in `B_48(0)`.
The site `(17,17,17)` has ℓ¹ norm `51`, so it is absent from `B_48(0)`. The
`B_51(0)` table is therefore not leftover of the `B_48(0)` times.

## Theorem 1 — Arrivals At `k=17` Under `ω`

One origin Dijkstra on `B_51(0)` returns `t(17,0,0) = 33` and
`t(17,17,17) = 55`. Both sites lie in `B_51(0)`. The site `(17,17,17)` has
ℓ¹ norm `51`, so it is absent from `B_48(0)`. The pair is computed on
`B_51(0)`, not copied from a smaller-ball table. These values are Dijkstra
outputs, not fitted scalars.

A witness axis walk of cost `33` is seed-exit `3` onto `(1,0,0)`, leave-axis
`1` onto `(1,1,0)`, enter-body `1` onto `(1,1,1)`, ridge-slide `3` onto
`(1,2,1)`, sixteen support-preserving cost-`1` body hops to `(17,2,1)`,
support-drop `3` onto `(17,2,0)`, corridor-slide `3` onto `(17,1,0)`, and
support-drop `3` onto `(17,0,0)`, summing to `33`. That walk is a witness of
cost `33`, not a uniqueness claim.

A witness body walk of cost `55` is seed-exit `3` onto `(1,0,0)`, leave-axis
`1` onto `(1,1,0)`, corridor-slide `3` onto `(1,2,0)`, non-hugging face hop
`1` onto `(2,2,0)`, enter-body `1` onto `(2,2,1)`, sixteen support-preserving
cost-`1` body hops to `(2,2,17)`, fifteen cost-`1` body hops to `(2,17,17)`,
and fifteen cost-`1` body hops to `(17,17,17)`, summing to `55`. That walk
is a witness of cost `55`, not a uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Pair `k=17`

The Euclidean-normalized comparison at `k=17` is

`t(17,0,0)^2 / 289  ?  t(17,17,17)^2 / 867`.

The computed integers give `3 · 33^2 = 3267` and `55^2 = 3025`, so
`3267 > 3025`. Arrival per Euclidean length is larger at `(17,0,0)` than at
`(17,17,17)`. Same-`k` reverse at `k=17` under `ω` is yes. The comparison
is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ω` is a displayed scoring device on `B_51(0)`. Do not write `ω`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_51(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_51(0) for the displayed rule ω at k=17; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ω` among hop-costs that reverse any same-`k` pair.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_51(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=17`.
- Any reuse of a smaller-ball arrival table as a substitute for the
  radius-`51` Dijkstra.
- Any adoption of `ω` as an admissibility rule.
