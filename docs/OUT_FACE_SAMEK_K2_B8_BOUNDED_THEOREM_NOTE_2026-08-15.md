---
claim_id: out_face_samek_k2_b8_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=2 under the named out-face hop-cost on B_8(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/out_face_samek_k2_b8_2026_08_15.py
---

# Named Out-Face Same-`k` Reverse At `k=2` On `B_8(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_8(0)`,
scored only for the same-`k` pair `t(2,0,0)` versus `t(2,2,2)`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/out_face_samek_k2_b8_2026_08_15.py`](../scripts/out_face_samek_k2_b8_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_8(0)`, the stacked
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
the first display of same-`k` under `ω` at `k=2`.

A mid-leave clause that would cost `3` on a `1→2` hop with destination max
absolute coordinate `1` and source max at least `2` cannot fire on the
six-neighbor graph: a cubic step never realizes both of those max conditions
together with `|σ_v|=1` and `|σ_w|=2`. The out-face hop
`(1,1,0) → (2,1,0)` does fire: `|σ|=2→2` and `max |w_i|=2 > max |v_i|=1`,
so `ω=3`. Independently, `ω` is not leftover of `ρ3`: the interior
face-growth hop `(2,2,0) → (3,2,0)` has `ρ3=1` and `ω=3`, so `ρ3`
cannot price out-face. The new clause is live.

The comparison uses one Dijkstra from the origin on `B_8(0)`
(833 sites; 832 nonzero). One Dijkstra returns

| site | `t_ω` |
|---|---:|
| `(2,0,0)` | `6` |
| `(2,2,2)` | `10` |

The same-`k` comparison at `k=2` is

`t(2,0,0)^2 / 4  ?  t(2,2,2)^2 / 12`,

equivalently `3 t(2,0,0)^2 ? t(2,2,2)^2`. Substituting the computed times
gives `108 > 100`. Same-`k` reverse at `k=2` is yes. Independently, the
new axis site is `t(8,0,0) = 24`.

The `k=2` geodesic `0 → (1,0,0) → (1,1,0) → (1,1,1) → (2,1,1) → (2,2,1) → (2,2,2)`
uses `ω` costs `3,1,1,3,1,1`. The axis geodesic `0 → (1,0,0) → (2,0,0)`
uses `ω` costs `3,3`. Those walks are witnesses, not a uniqueness claim.

The rule is displayed, not adopted. Do not write `ω` into Admissibility.
Do not write ω into Admissibility. Do not attach L1.

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

Let `B_8(0) = { v ∈ Z^3 : |v|_1 ≤ 8 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_8(0)`,
`t(v)` is the least sum of `ω` along a directed path from `0` to `v` in
that graph.

The first `ν` clause is seed-exit. The second is both weights `1`. The third
is support drop. The `μ` addendum taxes a `2→2` hop whose destination still
touches a unit coordinate. The `ρ3` addendum taxes a `3→3` hop whose
destination has exactly two unit coordinates. The `ω` addendum taxes a
`2→2` hop that grows the coordinate box on a face.

## Theorem 1 — Arrivals At `k=2` Under `ω`

One origin Dijkstra on `B_8(0)` returns `t(2,0,0) = 6` and `t(2,2,2) = 10`.
Both sites lie in `B_8(0)`. These values are Dijkstra outputs, not fitted
scalars.

A witness axis walk of cost `6` is the two axis hops from `0` onto
`(2,0,0)`, each of cost `3`. A witness body walk of cost `10` is seed-exit
`3` onto `(1,0,0)`, unit-cube leave `1` onto `(1,1,0)`, unit-cube enter `1`
onto `(1,1,1)`, ridge-slide `3` onto `(2,1,1)`, and two support-preserving
cost-`1` body hops onto `(2,2,2)`. A witness that the out-face clause is
live is the walk seed-exit `3` onto `(1,0,0)`, unit-cube leave `1` onto
`(1,1,0)`, corridor-slide `3` onto `(1,2,0)`, support-preserving `1` onto
`(2,2,0)`, and out-face `3` onto `(3,2,0)`, summing to `11`. Independently,
`t(3,2,0) = 11`.

## Theorem 2 — Reverse At The Same-`k` Pair `k=2`

The Euclidean-normalized comparison at `k=2` is

`t(2,0,0)^2 / 4  ?  t(2,2,2)^2 / 12`.

The computed integers give `3 · 6^2 = 108` and `10^2 = 100`, so
`108 > 100`. Arrival per Euclidean length is larger at `(2,0,0)` than at
`(2,2,2)`. Same-`k` reverse at `k=2` under `ω` is yes. The comparison is
displayed, not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `ω` is a displayed scoring device on `B_8(0)`. Do not write `ω`
into Admissibility. Do not write ω into Admissibility. Do not attach L1.
It is not a replacement for unit-cost first arrival, and it is not offered
as the unique hop-cost with same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_8(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_8(0) for the displayed rule ω at k=2; no Admissibility edit; not attached to L1"
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
- Any statement off `B_8(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=2`.
- Any adoption of `ω` as an admissibility rule.
- Any reuse of a `ρ3` arrival table as a substitute for the `ω` Dijkstra.
