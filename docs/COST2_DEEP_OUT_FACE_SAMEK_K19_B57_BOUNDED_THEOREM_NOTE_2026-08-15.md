---
claim_id: cost2_deep_out_face_samek_k19_b57_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=19 under the named cost-2 deep-out-face hop-cost on B_57(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost2_deep_out_face_samek_k19_b57_2026_08_15.py
---

# Same-k Reverse At k=19 Under The Named Cost-2 Deep-Out-Face Hop-Cost On B_57(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_57(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=19`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/cost2_deep_out_face_samek_k19_b57_2026_08_15.py`](../scripts/cost2_deep_out_face_samek_k19_b57_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

The named cost-2 deep-out-face hop-cost `c2df` is the already scored
ridge-slide rule `ρ3` plus cost `2` (not `3`) on a `2→2` hop whose
destination max absolute coordinate grows and whose source max is at least
`2`. That extra clause skips the unit-out-face hop `(1,1,0) → (2,1,0)` that
the cost-2 out-face rule `w2` writes into its grow clause. The unit-out-face
hop is already priced `3` by the corridor-slide clause of `μ`, so on the
six-neighbor graph the two extra predicates disagree while the hop-costs
agree. This note is the first display of same-`k` at `k=19` under `c2df`.
Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_57(0)`, the displayed
rule `c2df` is

`c2df(v→w) = 3` if `ρ3` would be `3`, else `2` if `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 2)`, else `1`,

where `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly
two `|w_i|` equal `1)`, else `1`,
`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`, and
`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first three clauses are seed-exit, both weights `1`, and support drop.
The fourth clause is the axis-hugging `2→2` corridor slide. The fifth
clause is the ridge slide. The sixth clause is deep out-face priced at
`2`: grow the box on a face only after height two. Those six clauses are
the whole rule. The unit-out-face hop `(1,1,0) → (2,1,0)` has source max
`1`, so it is not in the sixth clause; it stays at cost `3` by
corridor-slide.

One Dijkstra from the origin on `B_57(0)` (253575 sites; 253574 nonzero)
gives

`t(19,0,0) = 35`, `t(19,19,19) = 61`.

The displayed same-`k` comparison at `k=19` is

`t(19,0,0)^2 / 361  ?  t(19,19,19)^2 / 1083`,

which is `1225/361` versus `3721/1083`, or equivalently `3675 < 3721`. The
inequality does not hold. Same-`k` reverse at `k=19` under `c2df` is no.
Independently, the new axis site is `t(57,0,0) = 78`. The shared axis site
`t(54,0,0) = 70` is a `c2df` score on this ball, not a smaller-ball leftover.

The extra deep-out-face clause is live on the ball. On the deep-out-face
hop `(2,2,0) → (3,2,0)` one has `|σ| : 2 → 2`, `max |w_i| = 3 > max |v_i|
= 2`, and source max `2`, while the least nonzero `|w_i|` is `2`, so
`ρ3 = 1` while `c2df = 2`. Therefore `ρ3` cannot price deep out-face.
Independently, `t(3,2,0) = 10` under `c2df`. The corridor hop
`(1,1,0) → (2,1,0)` also grows the max absolute coordinate, but its
source max is `1`, so it is not deep out-face; it is already `ρ3 = 3` by
the hugging clause. A cheapest `c2df` walk to `(19,19,19)` uses no
deep-out-face `2→2` grow, so the body arrival is the interior-slide
count `61`. The site `(19,19,19)` has ℓ¹ norm `57`, so it is absent from
`B_54(0)`. The `B_57(0)` table is therefore not leftover of the `B_54(0)` times.

The cost-3 deep-out-face comparator `df` uses the same extra clause priced
at `3`. On `(2,2,0) → (3,2,0)` one has `c2df = 2` while `df = 3`. Therefore
the `c2df` scores are not leftover of `df`. Independently, `t(3,2,0) = 10`
under `c2df` while a `df` walk through that hop costs `11`.

On every six-neighbor hop the cost `c2df` equals the cost `w2`, because the
only grow hop that `w2` names and `c2df` skips is already priced `3` by `μ`.
The pair `35` versus `61` therefore coincides with the `w2` pair. The
named extra clause is still not leftover of `w2`: `w2` writes unit-out-face
into its grow clause, and `c2df` does not. The same hop has `ω = 3`, so
the `c2df` scores are not leftover of `ω`.

The rule is displayed, not adopted. Do not write `c2df` into Admissibility.
Do not write c2df into Admissibility. Do not attach L1.

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
clause, the deep-out-face source-max clause, and the arrival function `t`
are separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_57(0) = { v ∈ Z^3 : |v|_1 ≤ 57 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_57(0)`,
`t(v)` is the least sum of `c2df` along a directed path from `0` to `v` in
that graph.

The comparator `ρ3` uses only the first five clauses of `c2df`. On the
deep-out-face hop `(2,2,0) → (3,2,0)` one has `|σ| : 2 → 2` and a growing
max at source height at least two, so `ρ3 = 1` while `c2df = 2`. Therefore
`ρ3` cannot price deep out-face, and the `c2df` scores below are not a
leftover of `ρ3`.

The cost-3 deep-out-face comparator `df` uses the same grow test priced at
`3`. On `(2,2,0) → (3,2,0)` the hop-costs disagree: `c2df = 2` and `df = 3`.

The cost-2 out-face comparator `w2` uses the same grow test without the
source-max floor. On `(1,1,0) → (2,1,0)` the `w2` grow predicate holds and
the `c2df` grow predicate fails. On `(2,2,0) → (3,2,0)` both grow
predicates hold and both hop-costs equal `2`. Final six-neighbor costs
still agree.

The cost-3 out-face comparator `ω` prices `(2,2,0) → (3,2,0)` at `3`
while `c2df` prices it at `2`. Therefore the `c2df` scores are not leftover of `ω`.

The cost-3 ridge-enter comparator `κ` prices `(2,1,0) → (2,1,1)` at `3`
while `c2df` leaves it at `1`. Therefore the `c2df` scores are not leftover of `κ`.

The interior-slide comparator `ι` taxes a `3 → 3` hop whose destination
has `min |w_i| ≥ 2` and is not a height-`m` ridge. On `(3,3,2) → (3,3,3)`
one has `c2df = 1` while `ι = 3`. Therefore the `c2df` body arrival `61` is
not leftover of `ι`.

## Theorem 1 — Arrivals `t(19,0,0)` And `t(19,19,19)` On `B_57(0)`

Under `c2df` on `B_57(0)`,

```text
t(19,0,0) = 35
t(19,19,19) = 61
```

Every listed site lies in `B_57(0)`. The site `(19,19,19)` has ℓ¹ norm `57`,
so it is absent from `B_54(0)`. The pair is computed on `B_57(0)`, not
copied from a smaller-ball table. These values are Dijkstra outputs, not
fitted scalars.

A witness axis walk of cost `35` is seed-exit `3` onto `(1,0,0)`,
unit-cube leave `1` onto `(1,1,0)`, unit-cube enter `1` onto `(1,1,1)`,
ridge-slide `3` onto `(2,1,1)`, support-preserving `1` onto `(2,2,1)`,
seventeen support-preserving cost-`1` body hops to `(19,2,1)`, ridge-slide
`3` onto `(19,1,1)`, support-drop `3` onto `(19,1,0)`, and support-drop
`3` onto `(19,0,0)`, summing to `35`. That walk never uses a `2→2` dest
whose max grows at source height at least two. That walk is a witness of
cost `35`, not a uniqueness claim.

A witness body walk of cost `61` is the same prefix of cost `9` to
`(2,2,1)`, seventeen cost-`1` hops to `(19,2,1)`, seventeen cost-`1` hops
to `(19,19,1)`, and eighteen support-preserving cost-`1` body hops to
`(19,19,19)`, summing to `61`. Those last hops have dest with only one
absolute coordinate equal to `1` or none, so they are not ridge slides.
That walk is a witness of cost `61`, not a uniqueness claim.

A witness that the deep-out-face clause is live at cost `2` is the walk
seed-exit `3` onto `(1,0,0)`, unit-cube leave `1` onto `(1,1,0)`,
corridor-slide `3` onto `(1,2,0)`, support-preserving `1` onto `(2,2,0)`,
and deep out-face `2` onto `(3,2,0)`, summing to `10`. Replacing only the
last hop by its `ρ3` price `1` yields `9`. Replacing only the last hop by
its `df` price `3` yields `11`. Independently, `t(3,2,0) = 10`.

## Theorem 2 — Reverse At The Same-`k` Scale `k=19`

The Euclidean-normalized comparison at `k=19` is

`t(19,0,0)^2 / 361  ?  t(19,19,19)^2 / 1083`,

equivalently `3 t(19,0,0)^2 ? t(19,19,19)^2`. Substituting the computed times
gives `3 · 35^2 = 3675` and `61^2 = 3721`, so

`3675 < 3721`.

Arrival per Euclidean length is not larger at `(19,0,0)` than at
`(19,19,19)`. Same-`k` reverse at `k=19` under `c2df` is no. The comparison
is displayed, not adopted. The inequality does not hold.

## Theorem 3 — Displayed, Not Adopted

The rule `c2df` is a displayed scoring device on `B_57(0)`. Do not write `c2df`
into Admissibility. Do not write c2df into Admissibility. Do not attach L1.
It is not a replacement for unit-cost first arrival, and it is not offered
as the only hop-cost with a same-`k` score at this scale.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_57(0) for one named hop-cost at k=19. The rule is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: cost2_deep_out_face_samek_k19_b57
target_blocker_text: "whether same-k reverse at k=19 still holds after deep-out-face 2-to-2 hops are priced at 2"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded arrival comparison"
conditional_surface_status: "exact on B_57(0) for the displayed rule c2df at k=19; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `c2df` among hop-costs that score the same-`k` pair at `k=19`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_57(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=19`.
- Any reuse of a `ρ3`, `df`, `ω`, or `w2` arrival table as a substitute for
  the `c2df` Dijkstra.
- Membership of `c2df` as a physical hop-cost. Reverse at `k=19` on this ball
  is a displayed comparison, not an adoption.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

Their dependency role is limited to the repository's site graph and the
refusal to treat a named hop-cost as axiom content.

## Runner Contract

The companion runner builds `B_57(0)`, evaluates the named hop-cost, and
runs one Dijkstra from the origin. It reports `t(19,0,0)` and `t(19,19,19)`,
checks the integer form of Theorem 2, checks that the extra `2→2` clause is
live on in-host hops at cost `2` and skips the unit-out hop as a new tax,
checks that the live Admissibility wording does not name `c2df`, and
records the import boundary. Declared review inputs are this note and the
axiom memo only.
