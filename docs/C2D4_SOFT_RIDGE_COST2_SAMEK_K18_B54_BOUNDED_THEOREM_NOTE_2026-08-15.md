---
claim_id: c2d4_soft_ridge_cost2_samek_k18_b54_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=18 under the named c2d4-plus-soft-ridge hop-cost on B_54(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/c2d4_soft_ridge_cost2_samek_k18_b54_2026_08_15.py
---

# Named C2d4-Plus-Soft-Ridge Same-`k` Reverse At `k=18` On `B_54(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_54(0)`,
scored only for the same-`k` pair `t(18,0,0)` versus `t(18,18,18)`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/c2d4_soft_ridge_cost2_samek_k18_b54_2026_08_15.py`](../scripts/c2d4_soft_ridge_cost2_samek_k18_b54_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_54(0)`, the stacked
rules `ν`, `μ`, `ρ3`, and `c2d4` are

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
`|w_i|` equals `1)`, else `1`;

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`;

`c2d4(v→w) = 3` if `ρ3` would be `3`, else `2` if `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 4)`, else `1`.

The displayed c2d4-plus-soft-ridge rule `s2` is `c2d4` except that `ρ3`'s
`3→3` ridge-stay (exactly two `|w_i|=1`) costs `2` (not `3`):

`s2(v→w) = 3` if `μ` would be `3`, else `2` if `(|σ_v|=|σ_w|=3` and
exactly two `|w_i|` equal `1)` or (`c2d4` would be `2`), else `1`.

Those clauses are the whole rule. Uniqueness is not claimed. This note is
the first display of same-`k` reverse at `k=18` under `s2`. The body site
`(19,19,19)` has ℓ¹ norm `57` and is absent from `B_54(0)`.

On `(1,1,1) → (2,1,1)` one has `|σ|=3→3` and exactly two `|w_i|=1`, and
`μ=1`, so `s2=2` while `ρ3=3` and `c2d4=3`. Therefore `ρ3` cannot price
the soft ridge-stay, and `c2d4` cannot price the soft ridge-stay. The `s2`
scores below are not leftover of `ρ3` and not leftover of `c2d4`. The
max≥4 out-face hop `(4,2,0) → (5,2,0)` still has `s2=2` because `c2d4`
would be `2`. The source-max floor still skips `(3,2,0) → (4,2,0)` at
cost `1`. The unit-out-face hop `(1,1,0) → (2,1,0)` stays `s2=3` by
corridor-slide (`μ`).

One Dijkstra from the origin on `B_54(0)` (215929 sites; 215928 nonzero)
returns

| site | `t_{s2}` |
|---|---:|
| `(18,0,0)` | `32` |
| `(18,18,18)` | `57` |

The same-`k` comparison at `k=18` is

`t(18,0,0)^2 / 324  ?  t(18,18,18)^2 / 972`,

which is `1024/324` versus `3249/972`, or equivalently `3 t(18,0,0)^2 ?
t(18,18,18)^2`. Substituting the computed times gives `3 · 32^2 = 3072`
and `57^2 = 3249`, so `3072 < 3249`. The inequality does not hold.
Same-`k` reverse at `k=18` under `s2` is no.

The same Dijkstra keeps `t(1,0,0) = 3` versus `t(1,1,1) = 5`.
Independently, `t(1,2,1) = 7`, `t(2,1,1) = 7`, `t(3,2,0) = 9`,
`t(4,2,0) = 10`, and `t(5,2,0) = 12`. The new axis site is
`t(54,0,0) = 73`. The shared axis site `t(51,0,0) = 65` is an `s2` score
on this ball. The site `(18,18,18)` has ℓ¹ norm `54`, so it is absent from
`B_51(0)`. The `B_54(0)` table is therefore not leftover of the `B_51(0)`
times.

A cheapest body walk uses one soft ridge-stay then cost-`1` body hops, so
the body arrival is `57`. A cheapest axis walk uses two soft ridge-stay
hops and two terminal support drops, so the axis arrival is `32`. Soft
ridge-stay cheapens both legs; the axis saving is larger, and reverse at
`k=18` fails.

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
none of the hop costs. The integers `3`, `2`, and `1`, the support-size and
ridge-stay clauses, the max-coordinate floor, and the arrival function `t`
are separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_54(0) = { v ∈ Z^3 : |v|_1 ≤ 54 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_54(0)`,
`t(v)` is the least sum of `s2` along a directed path from `0` to `v` in
that graph.

The first `ν` clause is seed-exit. The second is both weights `1`. The third
is support drop. The `μ` addendum taxes a `2→2` hop whose destination still
touches a unit coordinate. The `ρ3` addendum taxes a `3→3` hop whose
destination has exactly two unit coordinates. The `c2d4` addendum taxes a
`2→2` hop that grows the coordinate box on a face only after source max
at least `4`, and prices that hop at `2`. The `s2` change from `c2d4` is
only that the `ρ3` ridge-stay hop is priced at `2` rather than `3`.

The comparator `ρ3` prices `(1,1,1) → (2,1,1)` at `3`. The comparator
`c2d4` does the same, because `ρ3` would be `3`. Under `s2` that hop is
cost `2` (not `3`). Therefore the `s2` scores are not leftover of `ρ3`
and not leftover of `c2d4`. Independently, `t(1,2,1) = 7` and
`t(2,1,1) = 7`. Replacing only that hop by its `ρ3` price `3` would yield
walk cost `8`, which is not the `s2` arrival.

The site `(18,0,0)` has ℓ¹ norm `18` and therefore also lies in `B_51(0)`.
The site `(18,18,18)` has ℓ¹ norm `54`, so it is absent from `B_51(0)`. The
`B_54(0)` table is therefore not leftover of the `B_51(0)` times.

## Theorem 1 — Arrivals At `k=18` Under `s2`

One origin Dijkstra on `B_54(0)` returns

```text
t(18,0,0) = 32
t(18,18,18) = 57
```

Both sites lie in `B_54(0)`. The site `(18,18,18)` has ℓ¹ norm `54`, so it
is absent from `B_51(0)`. The pair is computed on `B_54(0)`, not copied
from a smaller-ball table. These values are Dijkstra outputs, not fitted
scalars.

A witness axis walk of cost `32` is seed-exit `3` onto `(1,0,0)`, leave-axis
`1` onto `(1,1,0)`, enter-body `1` onto `(1,1,1)`, soft ridge-stay `2` onto
`(1,2,1)`, seventeen support-preserving cost-`1` body hops to `(18,2,1)`,
soft ridge-stay `2` onto `(18,1,1)`, support-drop `3` onto `(18,1,0)`, and
support-drop `3` onto `(18,0,0)`, summing to `32`. That walk is a witness
of cost `32`, not a uniqueness claim.

A witness body walk of cost `57` is seed-exit `3` onto `(1,0,0)`, leave-axis
`1` onto `(1,1,0)`, enter-body `1` onto `(1,1,1)`, soft ridge-stay `2` onto
`(2,1,1)`, leave-ridge `1` onto `(2,2,1)`, interior body hop `1` onto
`(2,2,2)`, sixteen support-preserving cost-`1` body hops to `(18,2,2)`,
sixteen cost-`1` body hops to `(18,18,2)`, and sixteen cost-`1` body hops
to `(18,18,18)`, summing to `57`. That walk uses one soft ridge-stay and
no max≥4 out-face `2→2` grow. That walk is a witness of cost `57`, not a
uniqueness claim.

A witness that the skipped hop is cheap is seed-exit `3` onto `(1,0,0)`,
leave-axis `1` onto `(1,1,0)`, corridor-slide `3` onto `(1,2,0)`,
non-hugging face hop `1` onto `(2,2,0)`, grow `1` onto `(3,2,0)`, and the
skipped grow `1` onto `(4,2,0)`, summing to `10`. Independently,
`t(4,2,0) = 10`. Independently, `t(3,2,0) = 9`. Continuing by
max≥4 out-face `2` onto `(5,2,0)` sums to `12`. Independently,
`t(5,2,0) = 12`.

## Theorem 2 — Reverse At The Same-`k` Pair `k=18`

The Euclidean-normalized comparison at `k=18` is

`t(18,0,0)^2 / 324  ?  t(18,18,18)^2 / 972`.

The computed integers give `3 · 32^2 = 3072` and `57^2 = 3249`, so
`3072 < 3249`. Arrival per Euclidean length is not larger at `(18,0,0)`
than at `(18,18,18)`. Same-`k` reverse at `k=18` under `s2` is no. The
comparison is displayed, not adopted. The inequality does not hold.

## Theorem 3 — Displayed, Not Adopted

The rule `s2` is a displayed scoring device on `B_54(0)`. Do not write
`s2` into Admissibility. Do not write s2 into Admissibility. Do not
attach L1. It is not a replacement for first arrival, and it is
not offered as the unique hop-cost with same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_54(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_54(0) for the displayed rule s2 at k=18; no Admissibility edit; not attached to L1"
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
- Any statement off `B_54(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=18`.
- Any reuse of a smaller-ball arrival table as a substitute for the
  radius-`54` Dijkstra.
- Any adoption of `s2` as an admissibility rule.
