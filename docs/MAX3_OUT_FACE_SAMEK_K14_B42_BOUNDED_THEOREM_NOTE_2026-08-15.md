---
claim_id: max3_out_face_samek_k14_b42_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=14 under the named max≥3 out-face hop-cost on B_42(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/max3_out_face_samek_k14_b42_2026_08_15.py
---

# Named Max≥3 Out-Face Same-k Reverse At k=14 On B_42(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_42(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=14`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/max3_out_face_samek_k14_b42_2026_08_15.py`](../scripts/max3_out_face_samek_k14_b42_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named max≥3 out-face hop-cost `d3` is the already scored ridge-slide
rule `ρ3` plus cost `3` on a `2→2` hop whose destination max absolute
coordinate grows and whose source max is at least `3`. That extra clause
skips the height-two out-face hop `(2,2,0) → (3,2,0)` that the deep-out-face
rule `df` writes into its grow clause, and it fires on later hops such as
`(3,2,0) → (4,2,0)`. This is the first display of whether same-`k` reverse
still holds at the `ρ3`/`κ` wall under that later tax. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_42(0)`, the displayed
rule `d3` is

`d3(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 3)`, else `1`,

where `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly
two `|w_i|` equal `1)`, else `1`,
`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`, and
`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first three clauses are seed-exit, both weights `1`, and support drop.
The fourth clause is the axis-hugging `2→2` corridor slide. The fifth
clause is the ridge slide. The sixth clause is max≥3 out-face: grow the
box on a face only after height three. Those six clauses are the whole
rule. The hop `(2,2,0) → (3,2,0)` has source max `2`, so it is not in the
sixth clause; its least nonzero destination coordinate is `2`, so it is
also not a corridor slide, and it stays at cost `1`. The hop
`(3,2,0) → (4,2,0)` has source max `3` and a growing dest max, so it is
cost `3`.

One Dijkstra from the origin on `B_42(0)` (102425 sites; 102424 nonzero)
gives

`t(14,0,0) = 30`, `t(14,14,14) = 46`.

The displayed same-`k` comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

which is `900/196` versus `2116/588`, or equivalently `2700 > 2116`. The
inequality holds. Same-`k` reverse at `k=14` under `d3` is yes. Reverse
still holds at the `ρ3`/`κ` wall. Independently, the new axis site is
`t(42,0,0) = 64`. The shared axis site `t(39,0,0) = 55` is a `d3` score
on this ball, not a smaller-ball leftover.

The same-`k` pair under `ρ3` is `26` versus `46`. That mismatch on the
axis is not a leftover of a `ρ3` table: the extra max≥3 out-face clause is
live on the ball. On the later out-face hop `(3,2,0) → (4,2,0)` one has
`|σ| : 2 → 2`, `max |w_i| = 4 > max |v_i| = 3`, and source max `3`, while
the least nonzero `|w_i|` is `2`, so `ρ3 = 1` while `d3 = 3`. Therefore
`ρ3` cannot price max≥3 out-face. Independently, `t(4,2,0) = 12` under
`d3`. The skipped hop `(2,2,0) → (3,2,0)` also grows the max absolute
coordinate, but its source max is `2`, so it is not max≥3 out-face; it
stays `d3 = 1` while `df = 3`. Independently, `t(3,2,0) = 9` under `d3`.
The corridor hop `(1,1,0) → (2,1,0)` also grows the max absolute
coordinate, but its source max is `1`, so it is not max≥3 out-face; it is
already `ρ3 = 3` by the hugging clause. A cheapest `d3` walk to
`(14,14,14)` uses no max≥3 out-face `2→2` grow, so the body arrival stays
`46`. The site `(14,14,14)` has ℓ¹ norm `42`, so it is absent from
`B_39(0)`. The `B_42(0)` table is therefore not leftover of the `B_39(0)` times.

The same-`k` pair `30` versus `46` coincides with the `df` pair and with
the `ω` pair. The named extra clause is still not leftover of `df` or of
`ω`: those rules price `(2,2,0) → (3,2,0)` at `3`, and `d3` prices it at
`1`.

The rule is displayed, not adopted. Do not write `d3` into Admissibility.
Do not write d3 into Admissibility. Do not attach L1.

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
the least-nonzero-coordinate clause, the two-unit-height ridge clause, the
max≥3 out-face source-max clause, and the arrival function `t` are
separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_42(0) = { v ∈ Z^3 : |v|_1 ≤ 42 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_42(0)`,
`t(v)` is the least sum of `d3` along a directed path from `0` to `v` in
that graph.

The comparator `ρ3` uses only the first five clauses of `d3`. On the
max≥3 out-face hop `(3,2,0) → (4,2,0)` one has `|σ| : 2 → 2` and a growing
max at source height at least three, so `ρ3 = 1` while `d3 = 3`. Therefore
`ρ3` cannot price max≥3 out-face, and the `d3` scores below are not a
leftover of `ρ3`.

The deep-out-face comparator `df` uses the same grow test with source-max
floor two. On `(2,2,0) → (3,2,0)` the `df` grow predicate holds and the
`d3` grow predicate fails. On `(3,2,0) → (4,2,0)` both grow predicates
hold. Final six-neighbor costs therefore disagree on the skipped hop.

The cost-3 out-face comparator `ω` uses the same grow test without a
source-max floor. On `(2,2,0) → (3,2,0)` the `ω` grow predicate holds and
the `d3` grow predicate fails.

The cost-3 ridge-enter comparator `κ` prices `(2,1,0) → (2,1,1)` at `3`
while `d3` leaves it at `1`. Therefore the `d3` scores are not leftover of `κ`.

The interior-slide comparator `ι` taxes a `3 → 3` hop whose destination
has `min |w_i| ≥ 2` and is not a height-`m` ridge. On `(3,3,2) → (3,3,3)`
one has `d3 = 1` while `ι = 3`. Therefore the `d3` body arrival `46` is
not leftover of `ι`.

## Theorem 1 — Arrivals `t(14,0,0)` And `t(14,14,14)` On `B_42(0)`

One origin Dijkstra on `B_42(0)` returns the integer arrivals

| site | `t_d3` |
|---|---:|
| `(14,0,0)` | `30` |
| `(14,14,14)` | `46` |

Every listed site lies in `B_42(0)`. The site `(14,14,14)` has ℓ¹ norm `42`,
so it is absent from `B_39(0)`. The pair is computed on `B_42(0)`, not
copied from a smaller-ball table and not copied from the `ρ3` pair
`26` versus `46`. These values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `30` is seed-exit `3` onto `(1,0,0)`,
unit-cube leave `1` onto `(1,1,0)`, unit-cube enter `1` onto `(1,1,1)`,
ridge-slide `3` onto `(2,1,1)`, support-preserving `1` onto `(2,2,1)`,
twelve support-preserving cost-`1` body hops to `(14,2,1)`, ridge-slide
`3` onto `(14,1,1)`, support-drop `3` onto `(14,1,0)`, and support-drop
`3` onto `(14,0,0)`, summing to `30`. That walk never uses a `2→2` dest
whose max grows at source height at least three. That walk is a witness of
cost `30`, not a uniqueness claim.

A witness body walk of cost `46` is the same prefix of cost `9` to
`(2,2,1)`, twelve cost-`1` hops to `(14,2,1)`, twelve cost-`1` hops to
`(14,14,1)`, and thirteen support-preserving cost-`1` body hops to
`(14,14,14)`, summing to `46`. Those last hops have dest with only one
absolute coordinate equal to `1` or none, so they are not ridge slides.
That walk is a witness of cost `46`, not a uniqueness claim.

A witness that the skip is live is the walk seed-exit `3` onto `(1,0,0)`,
unit-cube leave `1` onto `(1,1,0)`, corridor-slide `3` onto `(1,2,0)`,
support-preserving `1` onto `(2,2,0)`, and skipped height-two out-face
`1` onto `(3,2,0)`, summing to `9`. Replacing only the last hop by its
`df` price `3` yields `11`. Independently, `t(3,2,0) = 9`.

A witness that the max≥3 out-face clause is live is that same prefix of
cost `9` to `(3,2,0)` followed by max≥3 out-face `3` onto `(4,2,0)`,
summing to `12`. Replacing only the last hop by its `ρ3` price `1` yields
`10`. Independently, `t(4,2,0) = 12`.

## Theorem 2 — Reverse At The Same-`k` Scale `k=14`

The Euclidean-normalized comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

equivalently `3 t(14,0,0)^2 ? t(14,14,14)^2`. Substituting the computed times
gives `3 · 30^2 = 2700` and `46^2 = 2116`, so

`2700 > 2116`.

Arrival per Euclidean length is larger at `(14,0,0)` than at `(14,14,14)`.
Same-`k` reverse at `k=14` under `d3` is yes. Reverse still holds at the
`ρ3`/`κ` wall. The comparison is displayed, not adopted. The inequality
holds.

## Theorem 3 — Displayed, Not Adopted

The rule `d3` is a displayed scoring device on `B_42(0)`. Do not write `d3`
into Admissibility. Do not write d3 into Admissibility. Do not attach L1.
It is not a replacement for unit-cost first arrival, and it is not offered
as the unique hop-cost with same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_42(0) for one named hop-cost at k=14. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_42(0) for the displayed rule d3 at k=14; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `d3` among hop-costs that reverse the same-`k` pair at `k=14`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_42(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=14`.
- Any reuse of the `ρ3` arrival table as a substitute for the `d3` Dijkstra.
- Any reuse of the `df` or `ω` arrival table as a substitute for the `d3` Dijkstra.
- Membership of `d3` as a physical hop-cost. Reverse at `k=14` on this ball
  is a displayed comparison, not an adoption.
