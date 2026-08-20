---
claim_id: cost2_max4_out_face_samek_k17_b51_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=17 under the named cost-2 max≥4 out-face hop-cost on B_51(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost2_max4_out_face_samek_k17_b51_2026_08_15.py
---

# Named Cost-2 Max≥4 Out-Face Same-k Reverse At k=17 On B_51(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_51(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=17`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/cost2_max4_out_face_samek_k17_b51_2026_08_15.py`](../scripts/cost2_max4_out_face_samek_k17_b51_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named cost-2 max≥4 out-face hop-cost `c2d4` is the already scored
ridge-slide rule `ρ3` plus cost `2` on a `2→2` hop whose destination max
absolute coordinate grows and whose source max is at least `4`. That extra
clause cheapens the corresponding max≥4 out-face hops of the cost-3 rule
`d4` from `3` to `2`. The extra clause skips the height-three out-face hop
`(3,2,0) → (4,2,0)` that the max≥3 out-face rule `d3` writes into its grow
clause, and it fires on later hops such as `(4,2,0) → (5,2,0)`. This is
the first display of same-`k` reverse at `k=17` under that cheapened later
tax. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_51(0)`, the displayed
rule `c2d4` is

`c2d4(v→w) = 3` if `ρ3` would be `3`, else `2` if `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 4)`, else `1`,

where `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly
two `|w_i|` equal `1)`, else `1`,
`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`, and
`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first three clauses are seed-exit, both weights `1`, and support drop.
The fourth clause is the axis-hugging `2→2` corridor slide. The fifth
clause is the ridge slide. Those five clauses stay at cost `3`. The sixth
clause is max≥4 out-face priced at `2`: grow the box on a face only after
height four. Those six clauses are the whole rule. The hop `(3,2,0) →
(4,2,0)` has source max `3`, so it is not in the sixth clause; its least
nonzero destination coordinate is `2`, so it is also not a corridor slide,
and it stays at cost `1`. The hop `(4,2,0) → (5,2,0)` has source max `4`
and a growing dest max, so it is cost `2`.

One Dijkstra from the origin on `B_51(0)` (182207 sites; 182206 nonzero)
gives

`t(17,0,0) = 33`, `t(17,17,17) = 55`.

The displayed same-`k` comparison at `k=17` is

`t(17,0,0)^2 / 289  ?  t(17,17,17)^2 / 867`,

which is `1089/289` versus `3025/867`, or equivalently `3267 > 3025`. The
inequality holds. Same-`k` reverse at `k=17` under `c2d4` is yes. Reverse
still holds past the restored `k=14` wall. Independently, the new axis site
is `t(51,0,0) = 72`. The shared axis site `t(48,0,0) = 64` is a `c2d4`
score on this ball, not a smaller-ball leftover.

On the later out-face hop `(4,2,0) → (5,2,0)` one has `|σ| : 2 → 2`,
`max |w_i| = 5 > max |v_i| = 4`, and source max `4`, while the least
nonzero `|w_i|` is `2`, so `ρ3 = 1` while `c2d4 = 2`. Therefore `ρ3`
cannot price max≥4 out-face. Independently, `t(5,2,0) = 12` under `c2d4`.
The skipped hop `(3,2,0) → (4,2,0)` also grows the max absolute
coordinate, but its source max is `3`, so it is not max≥4 out-face; it
stays `c2d4 = 1` while `d3 = 3`. Independently, `t(4,2,0) = 10` under
`c2d4`. The hop `(2,2,0) → (3,2,0)` also grows the max absolute
coordinate, but its source max is `2`, so it is not max≥4 out-face; it
stays `c2d4 = 1` while `df = 3`. Independently, `t(3,2,0) = 9` under
`c2d4`. The corridor hop `(1,1,0) → (2,1,0)` also grows the max absolute
coordinate, but its source max is `1`, so it is not max≥4 out-face; it is
already `ρ3 = 3` by the hugging clause. A cheapest `c2d4` walk to
`(17,17,17)` uses no max≥4 out-face `2→2` grow, so the body arrival stays
`55`. The site `(17,17,17)` has ℓ¹ norm `51`, so it is absent from `B_48(0)`.
The `B_51(0)` table is therefore not leftover of the `B_48(0)` times.

The cost-3 max≥4 out-face comparator `d4` uses the same extra clause but
prices it at `3`. On `(4,2,0) → (5,2,0)` one has `c2d4 = 2` while
`d4 = 3`. Therefore the `c2d4` scores are not leftover of `d4`. The live
hop still differs.

The same-`k` pair `33` versus `55` also coincides with the `ω` pair. The
named extra clause is still not leftover of `ω`: that rule prices
`(2,2,0) → (3,2,0)` at `3`, and `c2d4` prices it at `1`. Independently it
is not leftover of `d3`: that rule prices `(3,2,0) → (4,2,0)` at `3`, and
`c2d4` prices it at `1`. Independently it is not leftover of `df`: that
rule prices `(2,2,0) → (3,2,0)` at `3`, and `c2d4` prices it at `1`.

The rule is displayed, not adopted. Do not write `c2d4` into Admissibility.
Do not write c2d4 into Admissibility. Do not attach L1.

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
clause, the max≥4 out-face source-max clause, and the arrival function `t`
are separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_51(0) = { v ∈ Z^3 : |v|_1 ≤ 51 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_51(0)`,
`t(v)` is the least sum of `c2d4` along a directed path from `0` to `v` in
that graph.

The comparator `ρ3` uses only the first five clauses of `c2d4`. On the
max≥4 out-face hop `(4,2,0) → (5,2,0)` one has `|σ| : 2 → 2` and a growing
max at source height at least four, so `ρ3 = 1` while `c2d4 = 2`. Therefore
`ρ3` cannot price max≥4 out-face, and the `c2d4` scores below are not a
leftover of `ρ3`.

The parent cost-3 comparator `d4` uses the same grow test with cost `3`.
On `(4,2,0) → (5,2,0)` both grow predicates hold and the hop costs
disagree. Therefore the `c2d4` scores are not leftover of `d4`.

The max≥3 out-face comparator `d3` uses the same grow test with source-max
floor three. On `(3,2,0) → (4,2,0)` the `d3` grow predicate holds and the
`c2d4` grow predicate fails. On `(4,2,0) → (5,2,0)` both grow predicates
hold. Final six-neighbor costs therefore disagree on the skipped hop.

The deep-out-face comparator `df` uses the same grow test with source-max
floor two. On `(2,2,0) → (3,2,0)` the `df` grow predicate holds and the
`c2d4` grow predicate fails. On `(4,2,0) → (5,2,0)` both grow predicates
hold.

The cost-3 out-face comparator `ω` uses the same grow test without a
source-max floor. On `(3,2,0) → (4,2,0)` the `ω` grow predicate holds and
the `c2d4` grow predicate fails.

The cost-3 ridge-enter comparator `κ` prices `(2,1,0) → (2,1,1)` at `3`
while `c2d4` leaves it at `1`. Therefore the `c2d4` scores are not leftover of `κ`.

The interior-slide comparator `ι` taxes a `3 → 3` hop whose destination
has `min |w_i| ≥ 2` and is not a height-`m` ridge. On `(3,3,2) → (3,3,3)`
one has `c2d4 = 1` while `ι = 3`. Therefore the `c2d4` body arrival `55` is
not leftover of `ι`.

## Theorem 1 — Arrivals `t(17,0,0)` And `t(17,17,17)` On `B_51(0)`

One origin Dijkstra on `B_51(0)` returns the integer arrivals

| site | `t_c2d4` |
|---|---:|
| `(17,0,0)` | `33` |
| `(17,17,17)` | `55` |

Every listed site lies in `B_51(0)`. The site `(17,17,17)` has ℓ¹ norm `51`,
so it is absent from `B_48(0)`. The pair is computed on `B_51(0)`, not
copied from a smaller-ball table. These values are Dijkstra outputs, not
fitted scalars.

A witness axis walk of cost `33` is seed-exit `3` onto `(1,0,0)`,
unit-cube leave `1` onto `(1,1,0)`, unit-cube enter `1` onto `(1,1,1)`,
ridge-slide `3` onto `(2,1,1)`, support-preserving `1` onto `(2,2,1)`,
fifteen support-preserving cost-`1` body hops to `(17,2,1)`, ridge-slide
`3` onto `(17,1,1)`, support-drop `3` onto `(17,1,0)`, and support-drop
`3` onto `(17,0,0)`, summing to `33`. That walk never uses a `2→2` dest
whose max grows at source height at least four. That walk is a witness of
cost `33`, not a uniqueness claim.

A witness body walk of cost `55` is the same prefix of cost `9` to
`(2,2,1)`, fifteen cost-`1` hops to `(17,2,1)`, fifteen cost-`1` hops to
`(17,17,1)`, and sixteen support-preserving cost-`1` body hops to
`(17,17,17)`, summing to `55`. Those last hops have dest with only one
absolute coordinate equal to `1` or none, so they are not ridge slides.
That walk is a witness of cost `55`, not a uniqueness claim.

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

## Theorem 2 — Reverse At The Same-`k` Scale `k=17`

The Euclidean-normalized comparison at `k=17` is

`t(17,0,0)^2 / 289  ?  t(17,17,17)^2 / 867`,

equivalently `3 t(17,0,0)^2 ? t(17,17,17)^2`. Substituting the computed times
gives `3 · 33^2 = 3267` and `55^2 = 3025`, so

`3267 > 3025`.

Arrival per Euclidean length is larger at `(17,0,0)` than at `(17,17,17)`.
Same-`k` reverse at `k=17` under `c2d4` is yes. Reverse still holds at this
first display past face `1..8`. The comparison is displayed, not adopted.
The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `c2d4` is a displayed scoring device on `B_51(0)`. Do not write `c2d4`
into Admissibility. Do not write c2d4 into Admissibility. Do not attach L1.
It is not a replacement for unit-cost first arrival, and it is not offered
as the unique hop-cost with same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_51(0) for one named hop-cost at k=17. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_51(0) for the displayed rule c2d4 at k=17; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `c2d4` among hop-costs that reverse the same-`k` pair at `k=17`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_51(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=17`.
- Any reuse of the `ρ3` arrival table as a substitute for the `c2d4` Dijkstra.
- Any reuse of the `d4` arrival table as a substitute for the `c2d4` Dijkstra.
- Any reuse of the `d3`, `df`, or `ω` arrival table as a substitute for the
  `c2d4` Dijkstra.
- Membership of `c2d4` as a physical hop-cost. Reverse at `k=17` on this ball
  is a displayed comparison, not an adoption.
