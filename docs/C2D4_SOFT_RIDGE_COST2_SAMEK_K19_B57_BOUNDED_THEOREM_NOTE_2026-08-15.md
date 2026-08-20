---
claim_id: c2d4_soft_ridge_cost2_samek_k19_b57_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=19 under the named c2d4-plus-soft-ridge hop-cost on B_57(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/c2d4_soft_ridge_cost2_samek_k19_b57_2026_08_15.py
---

# Named C2d4-Plus-Soft-Ridge Same-`k` Reverse At `k=19` On `B_57(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_57(0)`,
scored only for the same-`k` pair `t(19,0,0)` versus `t(19,19,19)`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/c2d4_soft_ridge_cost2_samek_k19_b57_2026_08_15.py`](../scripts/c2d4_soft_ridge_cost2_samek_k19_b57_2026_08_15.py)
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

The displayed c2d4-plus-soft-ridge rule `s2` keeps every `μ=3` hop at cost
`3`, cheapens `ρ3`'s `3→3` ridge-stay (exactly two destination unit
coordinates) from `3` to `2`, and keeps the `c2d4` extra hop at cost `2`:

`s2(v→w) = 3` if `μ` would be `3`, else `2` if `(|σ_v|=|σ_w|=3` and exactly
two `|w_i|` equal `1)` or (`c2d4` would be `2`), else `1`.

Those clauses are the whole rule. Uniqueness is not claimed. This note is
the first display of same-`k` reverse at `k=19` under `s2`.

The ridge-stay clause fires, for example, on `(1,1,1) → (2,1,1)`: support
stays `3` and the destination has exactly two unit coordinates, so `μ=1`,
`ρ3=3`, `c2d4=3`, and `s2=2`. The same clause fires on the axis-landing hop
`(19,2,1) → (19,1,1)`. Interior `3→3` with destination min abs at least `2`
is not ridge-stay: `(2,2,2) → (3,2,2)` has `s2=1`. Corridor-slide remains
cost `3`: `(1,1,0) → (2,1,0)` is already `μ=3`. The source-max floor still
skips `(3,2,0) → (4,2,0)` (`s2=1`) and fires `(4,2,0) → (5,2,0)` (`s2=2`
because `c2d4` would be `2`). Because `ρ3` and `c2d4` price ridge-stay at
`3`, they cannot cheapen ridge-stay to `2`, so the `s2` scores below are
not leftover of `c2d4`.

One Dijkstra from the origin on `B_57(0)` (253575 sites; 253574 nonzero)
returns

| site | `t_{s2}` |
|---|---:|
| `(19,0,0)` | `33` |
| `(19,19,19)` | `60` |

The same-`k` comparison at `k=19` is

`t(19,0,0)^2 / 361  ?  t(19,19,19)^2 / 1083`,

which is `1089/361` versus `3600/1083`, or equivalently `3 t(19,0,0)^2 ?
t(19,19,19)^2`. Substituting the computed times gives `3 · 33^2 = 3267`
and `60^2 = 3600`, so `3267 < 3600`. The inequality does not hold.
Same-`k` reverse at `k=19` is no.

Independently, `t(1,1,1) = 5`, `t(2,1,1) = 7`, `t(3,2,0) = 9`,
`t(4,2,0) = 10`, and `t(5,2,0) = 12`. The new axis site is
`t(57,0,0) = 76`. The shared axis site `t(54,0,0) = 68` is an `s2` score
on this ball. The site `(19,19,19)` has ℓ¹ norm `57`, so it is absent from
`B_54(0)`. The `B_57(0)` table is therefore not leftover of the `B_54(0)`
times.

A cheapest body walk uses one ridge-stay hop of cost `2` and then interior
cost-`1` hops. A cheapest axis walk uses one outbound ridge-stay of cost
`2` and one landing ridge-stay of cost `2`. Cheapening ridge-stay therefore
moves both arrivals; the same-`k` comparison at `k=19` still fails.

The rule is displayed, not adopted. Do not write `s2` into Admissibility.
Do not write s2 into Admissibility. Do not attach L1.

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
unit-count, and max-coordinate clauses, the ridge-stay cheapening, and the
arrival function `t` are separately displayed mathematical inputs. No axiom
text is edited.

## Named Rule

Let `B_57(0) = { v ∈ Z^3 : |v|_1 ≤ 57 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_57(0)`,
`t(v)` is the least sum of `s2` along a directed path from `0` to `v` in
that graph.

The first `ν` clause is seed-exit. The second is both weights `1`. The third
is support drop. The `μ` addendum taxes a `2→2` hop whose destination still
touches a unit coordinate. The `ρ3` addendum taxes a `3→3` hop whose
destination has exactly two unit coordinates. The `c2d4` addendum taxes a
`2→2` hop that grows the coordinate box on a face only after source max
at least `4`, and prices that hop at `2`. The `s2` addendum keeps `μ=3`
hops at `3`, prices that same `ρ3` ridge-stay at `2` rather than `3`, and
keeps the `c2d4` extra hop at `2`.

On `(1,1,1) → (2,1,1)` one has `|σ| : 3 → 3` and exactly two destination
unit coordinates, so `ρ3 = 3` and `c2d4 = 3` while `s2 = 2`. Therefore
`ρ3` and `c2d4` cannot cheapen ridge-stay to `2`. Independently,
`t(1,1,1) = 5` and `t(2,1,1) = 7`.

On `(4,2,0) → (5,2,0)` one has `|σ| : 2 → 2` and a growing max at source
height at least four, so `c2d4 = 2` and `s2 = 2` while `ρ3 = 1`. The
soft-ridge clause is idle there; the cost-`2` price is the kept `c2d4`
extra. Independently, `t(5,2,0) = 12`.

The site `(19,0,0)` has ℓ¹ norm `19` and therefore also lies in `B_54(0)`.
The site `(19,19,19)` has ℓ¹ norm `57`, so it is absent from `B_54(0)`. The
`B_57(0)` table is therefore not leftover of the `B_54(0)` times.

## Theorem 1 — Arrivals At `k=19` Under `s2`

One origin Dijkstra on `B_57(0)` returns

```text
t(19,0,0) = 33
t(19,19,19) = 60
```

Both sites lie in `B_57(0)`. The site `(19,19,19)` has ℓ¹ norm `57`, so it
is absent from `B_54(0)`. The pair is computed on `B_57(0)`, not copied
from a smaller-ball table. These values are Dijkstra outputs, not fitted
scalars.

A witness axis walk of cost `33` is seed-exit `3` onto `(1,0,0)`, leave-axis
`1` onto `(1,1,0)`, enter-body `1` onto `(1,1,1)`, ridge-stay `2` onto
`(1,2,1)`, eighteen support-preserving cost-`1` body hops to `(19,2,1)`,
landing ridge-stay `2` onto `(19,1,1)`, support-drop `3` onto `(19,1,0)`,
and support-drop `3` onto `(19,0,0)`, summing to `33`. That walk is a
witness of cost `33`, not a uniqueness claim.

A witness body walk of cost `60` is seed-exit `3` onto `(1,0,0)`, leave-axis
`1` onto `(1,1,0)`, enter-body `1` onto `(1,1,1)`, ridge-stay `2` onto
`(2,1,1)`, cost-`1` hop onto `(2,2,1)`, cost-`1` hop onto `(2,2,2)`,
seventeen support-preserving cost-`1` body hops to `(2,2,19)`, seventeen
cost-`1` body hops to `(2,19,19)`, and seventeen cost-`1` body hops to
`(19,19,19)`, summing to `60`. That walk uses one ridge-stay hop and no
max≥4 out-face `2→2` grow. That walk is a witness of cost `60`, not a
uniqueness claim.

A witness that the skipped hop is cheap is seed-exit `3` onto `(1,0,0)`,
leave-axis `1` onto `(1,1,0)`, corridor-slide `3` onto `(1,2,0)`,
non-hugging face hop `1` onto `(2,2,0)`, grow `1` onto `(3,2,0)`, and the
skipped grow `1` onto `(4,2,0)`, summing to `10`. Independently,
`t(4,2,0) = 10`. Independently, `t(3,2,0) = 9`. Continuing by
max≥4 out-face `2` onto `(5,2,0)` sums to `12`. Independently,
`t(5,2,0) = 12`.

## Theorem 2 — Reverse At The Same-`k` Pair `k=19`

The Euclidean-normalized comparison at `k=19` is

`t(19,0,0)^2 / 361  ?  t(19,19,19)^2 / 1083`.

The computed integers give `3 · 33^2 = 3267` and `60^2 = 3600`, so
`3267 < 3600`. Arrival per Euclidean length is larger at `(19,19,19)` than
at `(19,0,0)`. Same-`k` reverse at `k=19` under `s2` is no. The comparison
is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `s2` is a displayed scoring device on `B_57(0)`. Do not write
`s2` into Admissibility. Do not write s2 into Admissibility. Do not
attach L1. It is not a replacement for unit-cost first arrival, and it is
not offered as the unique hop-cost with same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_57(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_57(0) for the displayed rule s2 at k=19; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `s2` among hop-costs that reverse any same-`k` pair.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_57(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=19`.
- Any reuse of a smaller-ball arrival table as a substitute for the
  radius-`57` Dijkstra.
- Any adoption of `s2` as an admissibility rule.
