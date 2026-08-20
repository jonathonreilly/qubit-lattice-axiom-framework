---
claim_id: c2d4_deep_interior_cost2_samek_k19_b57_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=19 under the named c2d4-plus-deep-interior hop-cost on B_57(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/c2d4_deep_interior_cost2_samek_k19_b57_2026_08_15.py
---

# Named Cost-2 Dest-Min≥3 Interior `3→3` Same-`k` Reverse At `k=19` On `B_57(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_57(0)`,
scored only for the same-`k` pair `t(19,0,0)` versus `t(19,19,19)`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/c2d4_deep_interior_cost2_samek_k19_b57_2026_08_15.py`](../scripts/c2d4_deep_interior_cost2_samek_k19_b57_2026_08_15.py)
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

The parent cost-2 max≥4 out-face rule `c2d4` is `ρ3` plus cost `2` on a
`2→2` hop whose destination has a larger max absolute coordinate than the
source and whose source max is at least `4`:

`c2d4(v→w) = 3` if `ρ3` would be `3`, else `2` if `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 4)`, else `1`.

The comparator interior rule `i2` keeps those clauses and adds cost `2`
on a `3→3` hop whose destination min absolute coordinate is at least `2`.
The displayed c2d4-plus-deep-interior hop-cost `j2` keeps the `c2d4`
clauses and adds cost `2` only on a `3→3` hop whose destination min
absolute coordinate is at least `3`:

`j2(v→w) = 3` if `ρ3` would be `3`, else `2` if `c2d4` would be `2` or
`(|σ_v|=|σ_w|=3` and `min_i |w_i| ≥ 3)`, else `1`.

Those clauses are the whole rule. Uniqueness is not claimed. This note is
the first display of same-`k` reverse at `k=19` under `j2`.

The deep-interior addendum fires, for example, `(3,3,2) → (3,3,3)`. On
that hop one has `|σ|=3→3` and `min_i |w_i| = 3`, so `j2=2` while
`c2d4=1` and `ρ3=1`. The same addendum skips `(2,2,1) → (2,2,2)` and
`(2,2,2) → (3,2,2)`, whose destination min absolute coordinates equal
`2`, so `j2=1` while `i2=2`. It also skips `(2,2,1) → (3,2,1)`, whose
destination min absolute coordinate is `1`, so `j2=1`. Ridge-slide
`(1,1,1) → (2,1,1)` remains `ρ3=3`. The source-max floor of `c2d4` still
skips `(3,2,0) → (4,2,0)` (`j2=1`) and still fires `(4,2,0) → (5,2,0)`
(`j2=2`). The unit-out-face hop `(1,1,0) → (2,1,0)` is already `ρ3=3` by
corridor-slide (`μ`).

One Dijkstra from the origin on `B_57(0)` (253575 sites; 253574 nonzero)
returns

| site | `t_{j2}` |
|---|---:|
| `(19,0,0)` | `35` |
| `(19,19,19)` | `78` |

The same-`k` comparison at `k=19` is

`t(19,0,0)^2 / 361  ?  t(19,19,19)^2 / 1083`,

which is `1225/361` versus `6084/1083`, or equivalently `3 t(19,0,0)^2 ?
t(19,19,19)^2`. Substituting the computed times gives `3 · 35^2 = 3675`
and `78^2 = 6084`, so `3675 < 6084`. The inequality does not hold.
Same-`k` reverse at `k=19` is no.

Independently, `t(2,2,1) = 9`, `t(2,2,2) = 10`, `t(3,3,2) = 12`,
`t(3,3,3) = 14`, `t(19,19,1) = 43`, `t(19,19,2) = 44`, `t(3,2,0) = 9`,
`t(4,2,0) = 10`, and `t(5,2,0) = 12`. The new axis site is
`t(57,0,0) = 78`. The shared axis site `t(54,0,0) = 70` is a `j2` score
on this ball. The site `(19,19,19)` has ℓ¹ norm `57`, so it is absent
from `B_54(0)`. The `B_57(0)` table is therefore not leftover of the
`B_54(0)` times.

A cheapest body walk keeps one coordinate at absolute value `1` until
`(19,19,1)`, pays cost `1` onto `(19,19,2)`, then pays cost `2` on each
remaining dest-min≥3 grow. A named `c2d4` body walk that grows in the
interior from `(2,2,1)` has `c2d4` hop-sum `61` and `j2` hop-sum `78`.
The Dijkstra arrival `78` is therefore not leftover of `c2d4`. On
`(3,3,2) → (3,3,3)` one has `j2=2` while `c2d4=1`, so `c2d4` cannot price interior 3→3 dest-min≥3.

The same hugging body walk has `i2` hop-sum `79` and `j2` hop-sum `78`.
On `(2,2,1) → (2,2,2)` one has `i2=2` while `j2=1`, so `i2` cannot price dest-min=2 idle. The `j2` scores are therefore not leftover of `i2`.

The extra deep-interior clause is live: the cheapest walk to `(3,3,3)`
uses `(3,3,2) → (3,3,3)` at cost `2`. Pricing that hop at `2` rather
than `1` does not restore reverse at `k=19`. The axis arrival stays `35`
because the axis witness never uses a `3→3` destination with min
absolute coordinate at least `3`.

The rule is displayed, not adopted. Do not write `j2` into Admissibility.
Do not write j2 into Admissibility. Do not attach L1.

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
none of the hop costs. The integers `3`, `2`, and `1`, the support-size,
max-coordinate, and dest-min clauses, and the arrival function `t` are
separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_57(0) = { v ∈ Z^3 : |v|_1 ≤ 57 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_57(0)`,
`t(v)` is the least sum of `j2` along a directed path from `0` to `v` in
that graph.

The first `ν` clause is seed-exit. The second is both weights `1`. The third
is support drop. The `μ` addendum taxes a `2→2` hop whose destination still
touches a unit coordinate. The `ρ3` addendum taxes a `3→3` hop whose
destination has exactly two unit coordinates. The `c2d4` addendum taxes a
`2→2` hop that grows the coordinate box on a face only after source max
at least `4`, and prices that hop at `2`. The `j2` addendum taxes a `3→3`
hop whose destination min absolute coordinate is at least `3`, and prices
that hop at `2`.

The comparator `c2d4` uses only the first six clauses. On
`(3,3,2) → (3,3,3)` one has `|σ| : 3 → 3` and dest-min at least three, so
`c2d4 = 1` while `j2 = 2`. Therefore `c2d4` cannot price interior 3→3 dest-min≥3, and the `j2` scores below are not leftover of `c2d4`.
Independently, `t(3,3,3) = 14`. Replacing only that last hop by its
`c2d4` price `1` would yield `13`, which is not the `j2` arrival.

The comparator `i2` uses dest-min at least two. On `(2,2,1) → (2,2,2)`
one has `i2 = 2` while `j2 = 1`. Therefore `i2` cannot price dest-min=2 idle, and the `j2` scores are not leftover of `i2`. Independently,
`t(2,2,2) = 10`. Replacing only that last hop by its `i2` price `2`
would yield `11`, which is not the `j2` arrival.

The site `(19,0,0)` has ℓ¹ norm `19` and therefore also lies in `B_54(0)`.
The site `(19,19,19)` has ℓ¹ norm `57`, so it is absent from `B_54(0)`. The
`B_57(0)` table is therefore not leftover of the `B_54(0)` times.

## Theorem 1 — Arrivals At `k=19` Under `j2`

One origin Dijkstra on `B_57(0)` returns

```text
t(19,0,0) = 35
t(19,19,19) = 78
```

Both sites lie in `B_57(0)`. The site `(19,19,19)` has ℓ¹ norm `57`, so it
is absent from `B_54(0)`. The pair is computed on `B_57(0)`, not copied
from a smaller-ball table. These values are Dijkstra outputs, not fitted
scalars.

A witness axis walk of cost `35` is seed-exit `3` onto `(1,0,0)`, leave-axis
`1` onto `(1,1,0)`, enter-body `1` onto `(1,1,1)`, ridge-slide `3` onto
`(1,2,1)`, eighteen support-preserving cost-`1` body hops to `(19,2,1)`,
support-drop `3` onto `(19,2,0)`, corridor-slide `3` onto `(19,1,0)`, and
support-drop `3` onto `(19,0,0)`, summing to `35`. Every body hop on that
walk has destination min absolute coordinate `1`, so the deep-interior
addendum is idle. That walk is a witness of cost `35`, not a uniqueness
claim.

A witness body walk of cost `78` is seed-exit `3` onto `(1,0,0)`, leave-axis
`1` onto `(1,1,0)`, enter-body `1` onto `(1,1,1)`, ridge-slide `3` onto
`(2,1,1)`, leave-ridge `1` onto `(2,2,1)`, seventeen cost-`1` hugging body
hops to `(19,2,1)`, seventeen cost-`1` hugging body hops to `(19,19,1)`,
one dest-min=`2` cost-`1` hop onto `(19,19,2)`, and seventeen dest-min≥3
cost-`2` body hops to `(19,19,19)`, summing to `78`. Independently,
`t(19,19,1) = 43`. Independently, `t(19,19,2) = 44`. That walk is a
witness of cost `78`, not a uniqueness claim.

A witness that the deep-interior hop is live is seed-exit `3` onto
`(1,0,0)`, leave-axis `1` onto `(1,1,0)`, enter-body `1` onto `(1,1,1)`,
ridge-slide `3` onto `(2,1,1)`, leave-ridge `1` onto `(2,2,1)`, dest-min=`2`
idle `1` onto `(2,2,2)`, dest-min=`2` idle `1` onto `(3,2,2)`, dest-min=`2`
idle `1` onto `(3,3,2)`, and dest-min≥3 grow `2` onto `(3,3,3)`, summing
to `14`. Independently, `t(3,3,2) = 12`. Independently, `t(3,3,3) = 14`.
Replacing only that last hop by its `c2d4` price `1` would yield `13`,
which is not the `j2` arrival.

A witness that dest-min=`2` is idle is the same prefix through `(2,2,1)`
and dest-min=`2` idle `1` onto `(2,2,2)`, summing to `10`. Independently,
`t(2,2,1) = 9`. Independently, `t(2,2,2) = 10`. Replacing only that last
hop by its `i2` price `2` would yield `11`, which is not the `j2`
arrival.

A witness that the skipped out-face hop is cheap is seed-exit `3` onto
`(1,0,0)`, leave-axis `1` onto `(1,1,0)`, corridor-slide `3` onto
`(1,2,0)`, non-hugging face hop `1` onto `(2,2,0)`, grow `1` onto
`(3,2,0)`, and the skipped grow `1` onto `(4,2,0)`, summing to `10`.
Independently, `t(4,2,0) = 10`. Independently, `t(3,2,0) = 9`. Continuing
by max≥4 out-face `2` onto `(5,2,0)` sums to `12`. Independently,
`t(5,2,0) = 12`.

## Theorem 2 — Reverse At The Same-`k` Pair `k=19`

The Euclidean-normalized comparison at `k=19` is

`t(19,0,0)^2 / 361  ?  t(19,19,19)^2 / 1083`.

The computed integers give `3 · 35^2 = 3675` and `78^2 = 6084`, so
`3675 < 6084`. Arrival per Euclidean length is larger at `(19,19,19)` than
at `(19,0,0)`. Same-`k` reverse at `k=19` under `j2` is no. The comparison
is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `j2` is a displayed scoring device on `B_57(0)`. Do not write
`j2` into Admissibility. Do not write j2 into Admissibility. Do not
attach L1. It is not a replacement for unit-cost first arrival, and it is
not offered as the unique hop-cost with same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_57(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_57(0) for the displayed rule j2 at k=19; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `j2` among hop-costs that reverse any same-`k` pair.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_57(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=19`.
- Any reuse of a smaller-ball arrival table as a substitute for the
  radius-`57` Dijkstra.
- Any adoption of `j2` as an admissibility rule.
