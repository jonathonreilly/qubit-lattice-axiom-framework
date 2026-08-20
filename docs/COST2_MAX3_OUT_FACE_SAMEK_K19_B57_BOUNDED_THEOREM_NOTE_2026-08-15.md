---
claim_id: cost2_max3_out_face_samek_k19_b57_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=19 under the named cost-2 max≥3 out-face hop-cost on B_57(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost2_max3_out_face_samek_k19_b57_2026_08_15.py
---

# Named Cost-2 Max≥3 Out-Face Same-`k` Reverse At `k=19` On `B_57(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_57(0)`,
scored only for the same-`k` pair `t(19,0,0)` versus `t(19,19,19)`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/cost2_max3_out_face_samek_k19_b57_2026_08_15.py`](../scripts/cost2_max3_out_face_samek_k19_b57_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_57(0)`, the stacked
rules `ν`, `μ`, and `ρ3` are

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
`|w_i|` equals `1)`, else `1`;

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

The displayed cost-2 max≥3 out-face rule `c2d3` is `ρ3` plus cost `2` (not `3`)
on a `2→2` hop whose destination has a larger max absolute
coordinate than the source and whose source max is at least `3`:

`c2d3(v→w) = 3` if `ρ3` would be `3`, else `2` if `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 3)`, else `1`.

Those clauses are the whole rule. Uniqueness is not claimed. This note is
the first display of same-`k` reverse at `k=19` under `c2d3`.

The source-max floor skips `(2,2,0) → (3,2,0)` and fires, for example,
`(3,2,0) → (4,2,0)`. On `(2,2,0) → (3,2,0)` one has `|σ|=2→2` and
`max |w_i|=3 > max |v_i|=2`, but the source max is `2`, so the extra
clause is off and `c2d3=1`. The same hop has `ρ3=1`. On
`(3,2,0) → (4,2,0)` the extra clause is on, so `c2d3=2` while `ρ3=1`.
The cost-3 max≥3 out-face comparator `d3` prices that same fire hop at
`3`, so `c2d3` is not leftover of `d3`. The cost-3 out-face comparator
that drops the source-max floor prices `(2,2,0) → (3,2,0)` at `3`, so
`c2d3` is not leftover of that comparator either. The unit-out-face hop
`(1,1,0) → (2,1,0)` is already `ρ3=3` by corridor-slide (`μ`), so the
source-max floor does not change that hop.

One Dijkstra from the origin on `B_57(0)` (253575 sites; 253574 nonzero)
returns

| site | `t_{c2d3}` |
|---|---:|
| `(19,0,0)` | `35` |
| `(19,19,19)` | `61` |

The same-`k` comparison at `k=19` is

`t(19,0,0)^2 / 361  ?  t(19,19,19)^2 / 1083`,

which is `1225/361` versus `3721/1083`, or equivalently `3 t(19,0,0)^2 ?
t(19,19,19)^2`. Substituting the computed times gives `3 · 35^2 = 3675`
and `61^2 = 3721`, so `3675 < 3721`. The inequality does not hold.
Same-`k` reverse at `k=19` is no.

Independently, `t(3,2,0) = 9` and `t(4,2,0) = 11`. The new axis site is
`t(57,0,0) = 78`. The shared axis site `t(54,0,0) = 70` is a `c2d3` score
on this ball. The site `(19,19,19)` has ℓ¹ norm `57`, so it is absent
from `B_54(0)`. The `B_57(0)` table is therefore not leftover of the
`B_54(0)` times.

A cheapest body walk uses no max≥3 out-face `2→2` grow, so the body
arrival stays `61`. The extra clause is still live: the cheapest walk to
`(4,2,0)` uses `(3,2,0) → (4,2,0)` at cost `2`. Pricing that hop at `2`
rather than `3` does not restore reverse at `k=19`.

The rule is displayed, not adopted. Do not write `c2d3` into Admissibility.
Do not write c2d3 into Admissibility. Do not attach L1.

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
max-coordinate clauses, the source-max floor, and the arrival function `t`
are separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_57(0) = { v ∈ Z^3 : |v|_1 ≤ 57 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_57(0)`,
`t(v)` is the least sum of `c2d3` along a directed path from `0` to `v` in
that graph.

The first `ν` clause is seed-exit. The second is both weights `1`. The third
is support drop. The `μ` addendum taxes a `2→2` hop whose destination still
touches a unit coordinate. The `ρ3` addendum taxes a `3→3` hop whose
destination has exactly two unit coordinates. The `c2d3` addendum taxes a
`2→2` hop that grows the coordinate box on a face only after source max
at least `3`, and prices that hop at `2`.

The comparator `ρ3` uses only the first five clauses. On
`(3,2,0) → (4,2,0)` one has `|σ| : 2 → 2` and a growing max at source
height at least three, so `ρ3 = 1` while `c2d3 = 2`. Therefore `ρ3`
cannot price max≥3 out-face, and the `c2d3` scores below are not a leftover of
`ρ3`. Independently, `t(4,2,0) = 11`.

The comparator `d3` uses the same extra clause priced at `3`. On
`(3,2,0) → (4,2,0)` one has `c2d3 = 2` while `d3 = 3`. Therefore the
`c2d3` scores are not leftover of `d3`. Independently, `t(4,2,0) = 11`
under `c2d3` while a `d3` walk through that hop costs `12`.

The site `(19,0,0)` has ℓ¹ norm `19` and therefore also lies in `B_54(0)`.
The site `(19,19,19)` has ℓ¹ norm `57`, so it is absent from `B_54(0)`. The
`B_57(0)` table is therefore not leftover of the `B_54(0)` times.

## Theorem 1 — Arrivals At `k=19` Under `c2d3`

One origin Dijkstra on `B_57(0)` returns

```text
t(19,0,0) = 35
t(19,19,19) = 61
```

Both sites lie in `B_57(0)`. The site `(19,19,19)` has ℓ¹ norm `57`, so it
is absent from `B_54(0)`. The pair is computed on `B_57(0)`, not copied
from a smaller-ball table. These values are Dijkstra outputs, not fitted
scalars.

A witness axis walk of cost `35` is seed-exit `3` onto `(1,0,0)`, leave-axis
`1` onto `(1,1,0)`, enter-body `1` onto `(1,1,1)`, ridge-slide `3` onto
`(1,2,1)`, eighteen support-preserving cost-`1` body hops to `(19,2,1)`,
support-drop `3` onto `(19,2,0)`, corridor-slide `3` onto `(19,1,0)`, and
support-drop `3` onto `(19,0,0)`, summing to `35`. That walk never uses a
`2→2` dest whose max grows at source height at least three. That walk is a
witness of cost `35`, not a uniqueness claim.

A witness body walk of cost `61` is seed-exit `3` onto `(1,0,0)`, leave-axis
`1` onto `(1,1,0)`, corridor-slide `3` onto `(1,2,0)`, non-hugging face hop
`1` onto `(2,2,0)`, enter-body `1` onto `(2,2,1)`, eighteen
support-preserving cost-`1` body hops to `(2,2,19)`, seventeen cost-`1`
body hops to `(2,19,19)`, and seventeen cost-`1` body hops to
`(19,19,19)`, summing to `61`. That walk uses no max≥3 out-face `2→2`
grow. That walk is a witness of cost `61`, not a uniqueness claim.

A witness that the skipped hop is cheap is seed-exit `3` onto `(1,0,0)`,
leave-axis `1` onto `(1,1,0)`, corridor-slide `3` onto `(1,2,0)`,
non-hugging face hop `1` onto `(2,2,0)`, and the skipped grow `1` onto
`(3,2,0)`, summing to `9`. Independently, `t(3,2,0) = 9`. Continuing by
max≥3 out-face `2` onto `(4,2,0)` sums to `11`. Independently,
`t(4,2,0) = 11`. Replacing only that last hop by its `ρ3` price `1`
would yield `10`, which is not the `c2d3` arrival. Replacing it by the
`d3` price `3` would yield `12`, which is also not the `c2d3` arrival.

## Theorem 2 — Reverse At The Same-`k` Pair `k=19`

The Euclidean-normalized comparison at `k=19` is

`t(19,0,0)^2 / 361  ?  t(19,19,19)^2 / 1083`.

The computed integers give `3 · 35^2 = 3675` and `61^2 = 3721`, so
`3675 < 3721`. Arrival per Euclidean length is larger at `(19,19,19)` than
at `(19,0,0)`. Same-`k` reverse at `k=19` under `c2d3` is no. The comparison
is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `c2d3` is a displayed scoring device on `B_57(0)`. Do not write
`c2d3` into Admissibility. Do not write c2d3 into Admissibility. Do not
attach L1. It is not a replacement for unit-cost first arrival, and it is
not offered as the unique hop-cost with same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_57(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_57(0) for the displayed rule c2d3 at k=19; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `c2d3` among hop-costs that reverse any same-`k` pair.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_57(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=19`.
- Any reuse of a smaller-ball arrival table as a substitute for the
  radius-`57` Dijkstra.
- Any adoption of `c2d3` as an admissibility rule.
