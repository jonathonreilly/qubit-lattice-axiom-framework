---
claim_id: c2d4_interior_cost2_samek_k14_b42_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=14 under the named c2d4-plus-interior hop-cost on B_42(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/c2d4_interior_cost2_samek_k14_b42_2026_08_15.py
---

# Named C2d4-Plus-Interior Same-k Reverse At k=14 On B_42(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_42(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=14`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/c2d4_interior_cost2_samek_k14_b42_2026_08_15.py`](../scripts/c2d4_interior_cost2_samek_k14_b42_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named c2d4-plus-interior hop-cost `i2` is the already scored cost-2
max≥4 out-face rule `c2d4` plus cost `2` on a `3→3` hop whose destination
has least absolute coordinate at least `2`. That extra clause taxes
interior body hops. This is the first display of whether same-`k` reverse
still holds at the `ρ3`/`κ` wall under that interior tax. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_42(0)`, the displayed
rule `i2` is

`i2(v→w) = 3` if `ρ3` would be `3`, else `2` if `c2d4` would be `2` or
`(|σ_v|=|σ_w|=3` and `min_i |w_i| ≥ 2)`, else `1`,

where
`c2d4(v→w) = 3` if `ρ3` would be `3`, else `2` if `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 4)`, else `1`,
`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`,
`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`, and
`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first three clauses are seed-exit, both weights `1`, and support drop.
The fourth clause is the axis-hugging `2→2` corridor slide. The fifth
clause is the ridge slide. Those five clauses stay at cost `3`. The sixth
clause is max≥4 out-face priced at `2`: grow the box on a face only after
height four. The seventh clause is interior `3→3` priced at `2`: dest min
absolute coordinate at least two. Those seven clauses are the whole rule.
The hop `(3,2,0) → (4,2,0)` has source max `3`, so it is not in the sixth
clause; it stays at cost `1`. The hop `(4,2,0) → (5,2,0)` has source max
`4` and a growing dest max, so it is cost `2`. The hop `(3,3,2) → (3,3,3)`
is fully supported with dest min `3`, so it is cost `2`. The hop
`(4,2,2) → (5,2,2)` is a height-`2` ridge and is also cost `2`. The hop
`(4,3,1) → (5,3,1)` has dest min `1`, so it is not interior and stays at
cost `1`.

One Dijkstra from the origin on `B_42(0)` (102425 sites; 102424 nonzero)
gives

`t(14,0,0) = 30`, `t(14,14,14) = 59`.

The displayed same-`k` comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

which is `900/196` versus `3481/588`, or equivalently `2700 < 3481`. The
inequality does not hold. Same-`k` reverse at `k=14` under `i2` is no.
Reverse does not hold at the `ρ3`/`κ` wall under `i2`. Independently, the
new axis site is `t(42,0,0) = 63`. The shared axis site `t(39,0,0) = 55`
is an `i2` score on this ball, not a smaller-ball leftover.

The same-`k` pair under `c2d4` is `30` versus `46`. The integers `59`
versus `46` coincide with a raised body relative to that pair. That
mismatch on the body is not a leftover of a `c2d4` table: the extra
interior `3→3` clause is live on the ball. On the last body hop
`(13,14,14) → (14,14,14)` one has `|σ| : 3 → 3` and dest min `14`, so
`c2d4 = 1` while `i2 = 2`. Therefore `c2d4` cannot price interior 3→3.
Independently, `t(14,14,14) = 59` and `t(14,14,2) = 35`. A cheapest `c2d4`
walk to `(14,14,14)` of cost `46` becomes cost `59` once those thirteen
late interior hops are priced at `2`. Independently, `t(14,14,1) = 33`.

The same-`k` pair under `ρ3` is `26` versus `46`. The integers `30` versus
`26` coincide with a raised axis relative to that wall pair. That mismatch
on the axis is not a leftover of a `ρ3` table: the extra max≥4 out-face
clause is live on the ball. On the later out-face hop `(4,2,0) → (5,2,0)`
one has `|σ| : 2 → 2`, `max |w_i| = 5 > max |v_i| = 4`, and source max
`4`, while the least nonzero `|w_i|` is `2`, so `ρ3 = 1` while `i2 = 2`.
Therefore `ρ3` cannot price max≥4 out-face. Independently,
`t(5,2,0) = 12` under `i2`. The skipped hop `(3,2,0) → (4,2,0)` also grows
the max absolute coordinate, but its source max is `3`, so it is not
max≥4 out-face; it stays `i2 = 1` while `d3 = 3`. Independently,
`t(4,2,0) = 10` under `i2`. The hop `(2,2,0) → (3,2,0)` also grows the
max absolute coordinate, but its source max is `2`, so it is not max≥4
out-face; it stays `i2 = 1` while `df = 3`. Independently,
`t(3,2,0) = 9` under `i2`. The corridor hop `(1,1,0) → (2,1,0)` also
grows the max absolute coordinate, but its source max is `1`, so it is not
max≥4 out-face; it is already `ρ3 = 3` by the hugging clause.

The interior-slide comparator `ι` taxes a non-ridge `3 → 3` hop whose
destination has `min |w_i| ≥ 2` at cost `3`, and it leaves a height-`m`
ridge at cost `1`. On `(3,3,2) → (3,3,3)` one has `i2 = 2` while `ι = 3`.
On `(4,2,2) → (5,2,2)` one has `i2 = 2` while `ι = 1`. Therefore the `i2`
scores are not leftover of `ι`. Independently, `t(5,2,2) = 14`,
`t(2,2,2) = 11`, and `t(3,3,3) = 15`. The `ι` pair `26` versus `72` is
not the `i2` pair.

The cost-3 max≥4 out-face comparator `d4` uses the same out-face clause
but prices it at `3`. On `(4,2,0) → (5,2,0)` one has `i2 = 2` while
`d4 = 3`. Independently, `t(5,2,0) = 12` under `i2` and `t(42,0,0) = 63`
under `i2`. Therefore the `i2` scores are not leftover of `d4`.

The same-`k` pair `30` versus `59` does not coincide with the `d3` pair,
the `df` pair, or the `ω` pair. The named extra clauses are still not leftover of `d3`: that rule prices `(3,2,0) → (4,2,0)` at `3`, and `i2`
prices it at `1`. Independently it is not leftover of `df` or of `ω`:
those rules price `(2,2,0) → (3,2,0)` at `3`, and `i2` prices it at `1`.

The site `(14,14,14)` has ℓ¹ norm `42`, so it is absent from `B_39(0)`.
The `B_42(0)` table is therefore not leftover of the `B_39(0)` times.

The rule is displayed, not adopted. Do not write `i2` into Admissibility.
Do not write i2 into Admissibility. Do not attach L1.

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
none of the hop costs. The integers `3`, `2`, and `1`, the support-size
clauses, the least-nonzero-coordinate clause, the two-unit-height ridge
clause, the max≥4 out-face source-max clause, the interior dest-min clause,
and the arrival function `t` are separately displayed mathematical inputs.
No axiom text is edited.

## Named Rule

Let `B_42(0) = { v ∈ Z^3 : |v|_1 ≤ 42 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_42(0)`,
`t(v)` is the least sum of `i2` along a directed path from `0` to `v` in
that graph.

The comparator `c2d4` uses only the first six clauses of `i2`. On the
interior hop `(13,14,14) → (14,14,14)` one has `|σ| : 3 → 3` and dest min
at least two, so `c2d4 = 1` while `i2 = 2`. Therefore `c2d4` cannot price
interior `3→3`, and the `i2` scores below are not a leftover of `c2d4`.

The comparator `ρ3` uses only the first five clauses. On
`(4,2,0) → (5,2,0)` one has `|σ| : 2 → 2` and a growing max at source
height at least four, so `ρ3 = 1` while `i2 = 2`. Therefore `ρ3` cannot
price max≥4 out-face. On `(3,3,2) → (3,3,3)` one has `ρ3 = 1` while
`i2 = 2`. Therefore `ρ3` cannot price interior `3→3`.

The parent cost-3 comparator `d4` uses the same grow test with cost `3`.
On `(4,2,0) → (5,2,0)` both grow predicates hold and the hop costs
disagree. Therefore the `i2` scores are not leftover of `d4`.

The max≥3 out-face comparator `d3` uses the same grow test with source-max
floor three. On `(3,2,0) → (4,2,0)` the `d3` grow predicate holds and the
`i2` grow predicate fails. The rule skips the height-three out-face hop.

The deep-out-face comparator `df` uses the same grow test with source-max
floor two. On `(2,2,0) → (3,2,0)` the `df` grow predicate holds and the
`i2` grow predicate fails.

The cost-3 out-face comparator `ω` uses the same grow test without a
source-max floor. On `(3,2,0) → (4,2,0)` the `ω` grow predicate holds and
the `i2` grow predicate fails.

The cost-3 ridge-enter comparator `κ` prices `(2,1,0) → (2,1,1)` at `3`
while `i2` leaves it at `1`. Therefore the `i2` scores are not leftover of `κ`.

The interior-slide comparator `ι` taxes a non-ridge interior `3 → 3` hop
at cost `3` and leaves a height-`m` ridge at cost `1`. On
`(3,3,2) → (3,3,3)` one has `i2 = 2` while `ι = 3`. On
`(4,2,2) → (5,2,2)` one has `i2 = 2` while `ι = 1`. Therefore the `i2`
scores are not leftover of `ι`.

## Theorem 1 — Arrivals `t(14,0,0)` And `t(14,14,14)` On `B_42(0)`

One origin Dijkstra on `B_42(0)` returns the integer arrivals

| site | `t_i2` |
|---|---:|
| `(14,0,0)` | `30` |
| `(14,14,14)` | `59` |

Every listed site lies in `B_42(0)`. The site `(14,14,14)` has ℓ¹ norm `42`,
so it is absent from `B_39(0)`. The pair is computed on `B_42(0)`, not
copied from a smaller-ball table and not copied from the `c2d4` pair
`30` versus `46` or from the `ρ3` pair `26` versus `46`. These values are
Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `30` is seed-exit `3` onto `(1,0,0)`,
unit-cube leave `1` onto `(1,1,0)`, unit-cube enter `1` onto `(1,1,1)`,
ridge-slide `3` onto `(2,1,1)`, support-preserving `1` onto `(2,2,1)`,
twelve support-preserving cost-`1` body hops to `(14,2,1)`, ridge-slide
`3` onto `(14,1,1)`, support-drop `3` onto `(14,1,0)`, and support-drop
`3` onto `(14,0,0)`, summing to `30`. Those twelve body hops have dest min
`1`, so they are not interior. That walk never uses a `2→2` dest whose
max grows at source height at least four. That walk is a witness of cost
`30`, not a uniqueness claim.

A witness body walk of cost `59` is the same prefix of cost `9` to
`(2,2,1)`, twelve cost-`1` hops to `(14,2,1)`, twelve cost-`1` hops to
`(14,14,1)`, and thirteen interior cost-`2` body hops to `(14,14,14)`,
summing to `59`. Those last hops have dest min at least `2`, so they are
interior `3→3`. They have dest with only one absolute coordinate equal to
`1` or none, so they are not ridge slides. That walk is a witness of cost
`59`, not a uniqueness claim.

A witness that the skip is live is the walk seed-exit `3` onto `(1,0,0)`,
unit-cube leave `1` onto `(1,1,0)`, corridor-slide `3` onto `(1,2,0)`,
support-preserving `1` onto `(2,2,0)`, support-preserving `1` onto
`(3,2,0)`, and skipped height-three out-face `1` onto `(4,2,0)`, summing
to `10`. Replacing only the last hop by its `d3` price `3` yields `12`.
Independently, `t(4,2,0) = 10`.

A witness that the max≥4 out-face clause is live is that same prefix of
cost `10` to `(4,2,0)` followed by max≥4 out-face `2` onto `(5,2,0)`,
summing to `12`. Replacing only the last hop by its `ρ3` price `1` yields
`11`. Replacing only the last hop by its `d4` price `3` yields `13`.
Independently, `t(5,2,0) = 12`.

A witness that the interior clause is live is the body prefix of cost `33`
to `(14,14,1)` followed by interior `2` onto `(14,14,2)`, summing to `35`.
Replacing only that last hop by its `c2d4` price `1` yields `34`.
Independently, `t(14,14,1) = 33` and `t(14,14,2) = 35`.

## Theorem 2 — Reverse At The Same-`k` Scale `k=14`

The Euclidean-normalized comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

equivalently `3 t(14,0,0)^2 ? t(14,14,14)^2`. Substituting the computed times
gives `3 · 30^2 = 2700` and `59^2 = 3481`, so

`2700 < 3481`.

Arrival per Euclidean length is larger at `(14,14,14)` than at `(14,0,0)`.
Same-`k` reverse at `k=14` under `i2` is no. Reverse does not hold at the
`ρ3`/`κ` wall under `i2`. The comparison is displayed, not adopted. The
inequality does not hold.

## Theorem 3 — Displayed, Not Adopted

The rule `i2` is a displayed scoring device on `B_42(0)`. Do not write `i2`
into Admissibility. Do not write i2 into Admissibility. Do not attach L1.
It is not a replacement for unit-cost first arrival, and it is not offered
as the unique hop-cost with same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_42(0) for one named hop-cost at k=14. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_42(0) for the displayed rule i2 at k=14; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `i2` among hop-costs that reverse or fail to reverse the
  same-`k` pair at `k=14`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_42(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=14`.
- Any reuse of the `c2d4` arrival table as a substitute for the `i2` Dijkstra.
- Any reuse of the `ρ3` arrival table as a substitute for the `i2` Dijkstra.
- Any reuse of the `ι`, `d4`, `d3`, `df`, or `ω` arrival table as a
  substitute for the `i2` Dijkstra.
- Membership of `i2` as a physical hop-cost. Reverse at `k=14` on this ball
  is a displayed comparison, not an adoption.
