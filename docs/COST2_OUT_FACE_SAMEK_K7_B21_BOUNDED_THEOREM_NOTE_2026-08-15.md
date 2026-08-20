---
claim_id: cost2_out_face_samek_k7_b21_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=7 under the named cost-2 out-face hop-cost on B_21(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost2_out_face_samek_k7_b21_2026_08_15.py
---

# Named Cost-2 Out-Face Same-k Reverse At k=7 On B_21(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_21(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=7`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/cost2_out_face_samek_k7_b21_2026_08_15.py`](../scripts/cost2_out_face_samek_k7_b21_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_21(0)`, the stacked
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

Those clauses are the whole rule. Uniqueness is not claimed. This is the
first display of same-`k` under `w2` at `k=7`. Independently, the same
Dijkstra keeps the `k=1` pair at `t(1,0,0) = 3` and `t(1,1,1) = 5`.

The parent box-growth hop `(1,1,0) → (2,1,0)` still has `|σ|=2→2` and
`max |w_i|=2 > max |v_i|=1`, but `μ` already taxes it (`ρ3=3`), so
`w2=3`. The new cost-`2` clause is not leftover of `ρ3`: the interior
face-growth hop `(2,2,0) → (3,2,0)` has `ρ3=1` and `w2=2`. The same hop
has `ω=3`, so `w2` is not leftover of `ω`.

The comparison uses one Dijkstra from the origin on `B_21(0)`
(13287 sites; 13286 nonzero) and gives

`t(7,0,0) = 21`, `t(7,7,7) = 25`.

The displayed same-`k` comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

which is `441/49` versus `625/147`, or equivalently `1323 > 625`. The
inequality holds. Same-`k` reverse at `k=7` under `w2` is yes.
Independently, the new axis site is `t(21,0,0) = 42`. The shared axis
site `t(18,0,0) = 34` is a `w2` score on this ball, not a leftover.

The pair is not leftover of `ρ3` as a rule: the axis arrivals under `w2`
and `ρ3` are `21` versus `19`, because a cheapest `ρ3` axis witness
uses height-two face growth. On the out-face hop `(2,2,0) → (3,2,0)`
one has `|σ| : 2 → 2` and `max_i |w_i| = 3 > max_i |v_i| = 2`, and the
least nonzero destination coordinate is `2`, so `ρ3 = 1` while
`w2 = 2`. Therefore `ρ3` cannot price out-face. The same walk that
scores `19` under `ρ3` — seed-exit onto `(0,-1,0)`, unit-cube leave,
corridor-slide to height two, six height-two slides to `(7,-2,0)`,
corridor return, and support-drop — scores `24` under `w2`, because five
of those height-two slides grow the max coordinate at cost `2`. The
on-ball hop `(2,2,0) → (3,2,0)` records that the new clause is live.
The body arrival `t(7,7,7) = 25` happens to coincide with the `ρ3`
body time because a cheapest body witness enters three-support at
`(2,2,2)` before any further face growth.

The pair is not leftover of `ω`: `ω` taxes the same out-face hop at
cost `3`. On `(2,2,0) → (3,2,0)` one has `ω = 3` while `w2 = 2`. The
same-`k` arrivals at `k=7` happen to coincide with the `ω` pair because
a cheapest axis or body witness never takes a cost-`2` out-face hop.
The on-ball site `(3,2,0)` arrives at `10` under `w2`. The same walk
with the last hop priced by `ω` costs `11`, and with the last hop priced
by `ρ3` costs `9`, which records that the new clause is live. The far
axis site `t(21,0,0) = 42` differs from the `ω` far-axis time `43`.

The site `(7,7,7)` has ℓ¹ norm `21`, so it is absent from `B_18(0)`. The
`B_21(0)` table is therefore not leftover of the `B_18(0)` times.

The rule is displayed, not adopted. Do not write `w2` into Admissibility.
Do not write w2 into Admissibility. Do not attach L1.

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

Let `B_21(0) = { v ∈ Z^3 : |v|_1 ≤ 21 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_21(0)`,
`t(v)` is the least sum of `w2` along a directed path from `0` to `v` in
that graph.

The first `ν` clause is seed-exit. The second is both weights `1`. The third
is support drop. The `μ` addendum taxes a `2→2` hop whose destination still
touches a unit coordinate. The `ρ3` addendum taxes a `3→3` hop whose
destination has exactly two unit coordinates. The `w2` addendum taxes a
`2→2` hop that grows the coordinate box on a face at cost `2` rather than
cost `3`.

The comparator `ρ3` uses only the inherited ridge-slide clauses. On
`(2,2,0) → (3,2,0)` one has `|σ| : 2 → 2` and a growing max absolute
coordinate at height two, so `ρ3 = 1` while `w2 = 2`. On
`(1,1,0) → (2,1,0)` the destination still has a unit coordinate, so
both `μ` and `w2` price the hop at `3`. On `(1,-2,0) → (2,-2,0)` the
max absolute coordinate stays `2`, so both `ρ3` and `w2` price the hop
at `1`. The comparator `ω` uses the same extra hop but at cost `3`. On
that hop `ω = 3` while `w2 = 2`. Therefore `ω` cannot be identified with
`w2`.

## Theorem 1 — Arrivals `t(7,0,0)` And `t(7,7,7)` On `B_21(0)`

One origin Dijkstra on `B_21(0)` returns the integer arrivals

| site | `t_{w2}` |
|---|---:|
| `(7,0,0)` | `21` |
| `(7,7,7)` | `25` |

Every listed site lies in `B_21(0)`. The site `(7,7,7)` has ℓ¹ norm `21`,
so it is absent from `B_18(0)`. The pair is computed on `B_21(0)`, not
copied from a smaller-ball table and not copied from a `ρ3` or `ω` table.
These values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `21` is the seven axis hops from `0` onto
`(7,0,0)`, each of cost `3`, summing to `21`. A witness body walk of
cost `25` is seed-exit `3` onto `(1,0,0)`, unit-cube leave `1` onto
`(1,1,0)`, unit-cube enter `1` onto `(1,1,1)`, ridge-slide `3` onto
`(2,1,1)`, two support-preserving cost-`1` body hops onto `(2,2,2)`,
and fifteen support-preserving cost-`1` body hops onto `(7,7,7)`,
summing to `25`. Those walks are witnesses, not a uniqueness claim.

A witness that the out-face clause is live is the walk seed-exit `3`
onto `(1,0,0)`, unit-cube leave `1` onto `(1,1,0)`, corridor-slide `3`
onto `(1,2,0)`, support-preserving `1` onto `(2,2,0)`, and out-face `2`
onto `(3,2,0)`, summing to `10`. Replacing only the last hop by its
`ω` price `3` yields `11`. Replacing only the last hop by its `ρ3`
price `1` yields `9`. Independently, `t(3,2,0) = 10`.

## Theorem 2 — Reverse At The Same-`k` Scale `k=7`

The Euclidean-normalized comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

equivalently `3 t(7,0,0)^2 ? t(7,7,7)^2`. Substituting the computed times
gives `3 · 21^2 = 1323` and `25^2 = 625`, so

`1323 > 625`.

Arrival per Euclidean length is larger at `(7,0,0)` than at `(7,7,7)`.
Same-`k` reverse at `k=7` under `w2` is yes. The comparison is displayed,
not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `w2` is a displayed scoring device on `B_21(0)`. Do not write
`w2` into Admissibility. Do not write w2 into Admissibility. Do not attach
L1. It is not a replacement for coordinate-sum first arrival, and it is
not offered as the unique hop-cost with same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_21(0) for one named hop-cost at k=7. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_21(0) for the displayed rule w2 at k=7; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `w2` among hop-costs that reverse the same-`k` pair at `k=7`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_21(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=7`.
- Any reuse of the `ω` or `ρ3` arrival table as a substitute for the `w2`
  Dijkstra.
- Any reuse of the `B_18(0)` arrival table as a substitute for the
  radius-`21` Dijkstra.
