---
claim_id: cost2_ridge_enter_samek_k14_b42_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=14 under the named cost-2 ridge-enter hop-cost on B_42(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost2_ridge_enter_samek_k14_b42_2026_08_15.py
---

# Named Cost-2 Ridge-Enter Same-k Reverse At k=14 On B_42(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_42(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=14`, with a first display of the same rule from `k=10` through that wall.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/cost2_ridge_enter_samek_k14_b42_2026_08_15.py`](../scripts/cost2_ridge_enter_samek_k14_b42_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named cost-2 ridge-enter hop-cost `c2` is scored independently on
`B_42(0)`. The ball is not leftover of the `B_39(0)` times: one origin
Dijkstra is run on this ball, and the site `(14,14,14)` is absent from
`B_39(0)`.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_42(0)`, the displayed
ancestors of `c2` are

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`;

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`;

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

The displayed rule `c2` is

`c2(v→w) = 3` if `ρ3` would be `3`, else `2` if `(|σ_v|=2` and `|σ_w|=3`
and exactly two `|w_i|` equal `1)`, else `1`.

The last clause is ridge-enter priced at `2`: a face-to-body hop whose
destination has exactly two unit coordinates. The hop `(1,1,0) → (1,1,1)`
has three unit coordinates at the destination, so it stays cost `1`.
Uniqueness is not claimed.

The cost-3 ridge-enter rule `κ` uses the same last clause but prices it at
`3`. On `(2,1,0) → (2,1,1)` one has `|σ| : 2 → 3` and exactly two `|w_i|`
equal `1`, so `c2 = 2` while `κ = 3` and `ρ3 = 1`.

One Dijkstra from the origin on `B_42(0)` (102425 sites; 102424 nonzero)
gives the first display of `c2` at 10→the wall

| `k` | `t(k,0,0)` | `t(k,k,k)` | reverse |
|---|---:|---:|---|
| `10` | `22` | `34` | yes |
| `11` | `23` | `37` | yes |
| `12` | `24` | `40` | yes |
| `13` | `25` | `43` | yes |
| `14` | `26` | `46` | no |

and the wall pair

`t(14,0,0) = 26`, `t(14,14,14) = 46`.

The displayed same-`k` comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

which is `676/196` versus `2116/588`, or equivalently `2028 > 2116`. The
inequality does not hold. Same-`k` reverse does not restore at `k=14`.
Independently, the new axis site is `t(42,0,0) = 58`. The shared axis site
`t(39,0,0) = 51` is an independent readout on this ball.

The integers `26` and `46` coincide with the named `κ` wall pair and with
the named `ρ3` wall pair. They are not leftover of `κ`: the ridge-enter hop
`(2,1,0) → (2,1,1)` has `c2 = 2` and `κ = 3`. They are not leftover of
`ρ3`: that hop has `ρ3 = 1`. They are also not leftover of `ι`: that
increment taxes interior `3 → 3` and is quoted as raising the body arrival
at this pair from `46` to `72`, while `c2` leaves `t(14,14,14) = 46`.
Pricing ridge-enter at `2` therefore does not raise the cheap body arrival
that sits at the wall, and does not restore reverse.

The rule is displayed, not adopted. Do not write `c2` into Admissibility.
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
none of the hop costs. The integers `3`, `2`, and `1`, the support-size
clauses, and the arrival function `t` are separately displayed mathematical
inputs. No axiom text is edited.

## Named Rule

Let `B_42(0) = { v ∈ Z^3 : |v|_1 ≤ 42 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_42(0)`,
`t(v)` is the least sum of `c2` along a directed path from `0` to `v` in
that graph.

The site `(14,0,0)` has ℓ¹ norm `14` and therefore also lies in `B_39(0)`.
The site `(14,14,14)` has ℓ¹ norm `42`, so it is absent from `B_39(0)`. The
`B_42(0)` table is therefore not leftover of the `B_39(0)` times.

The ridge-slide comparator `ρ3` uses every clause of `c2` except ridge-enter.
On the ridge-enter hop `(2,1,0) → (2,1,1)` one has `|σ| : 2 → 3` and
exactly two unit destination coordinates, so `ρ3 = 1` while `c2 = 2`.
Therefore `ρ3` cannot price ridge-enter, and the `c2` scores below are not
a leftover of `ρ3`.

The cost-3 ridge-enter comparator `κ` prices that same hop at `3`. Therefore
the `c2` scores are not a leftover of `κ`.

The interior-slide comparator `ι` taxes a `3 → 3` hop whose destination has
`min |w_i| ≥ 2` and is not a height-`m` ridge. On `(3,3,2) → (3,3,3)` one
has `c2 = 1` while `ι = 3`. Therefore the `c2` body arrival `46` is not
leftover of `ι`.

## Theorem 1 — Arrivals `t(14,0,0)` And `t(14,14,14)` On `B_42(0)`

One origin Dijkstra on `B_42(0)` returns the integer arrivals

| site | `t_{c2}` |
|---|---:|
| `(14,0,0)` | `26` |
| `(14,14,14)` | `46` |

Every listed site lies in `B_42(0)`. The site `(14,14,14)` has ℓ¹ norm `42`,
so it is absent from `B_39(0)`. The pair is computed on `B_42(0)`, not
copied from a smaller-ball table. These values are Dijkstra outputs, not
fitted scalars.

## Theorem 2 — Reverse At The Same-`k` Scale `k=14`

The Euclidean-normalized comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

equivalently `3 t(14,0,0)^2 ? t(14,14,14)^2`. Substituting the computed times
gives `3 · 26^2 = 2028` and `46^2 = 2116`, so

`2028 > 2116` is false; `2028 < 2116`.

Arrival per Euclidean length is smaller at `(14,0,0)` than at `(14,14,14)`.
Same-`k` reverse at `k=14` is no. Reverse does not restore at the wall. The
comparison is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `c2` is a displayed scoring device on `B_42(0)`. Do not write `c2`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_42(0) for one named hop-cost at k=14. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_42(0) for the displayed rule c2 at k=14; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `c2` among hop-costs that reverse the same-`k` pair at `k=14`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_42(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=14`, except the first display of `c2` from `k=10` through the wall
  under the same origin Dijkstra.
- Any reuse of the `B_39(0)` arrival table as a substitute for the
  radius-`42` Dijkstra.
