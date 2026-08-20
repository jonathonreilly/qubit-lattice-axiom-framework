---
claim_id: cost2_max4_out_face_samek_k18_b54_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=18 under the named cost-2 max≥4 out-face hop-cost on B_54(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost2_max4_out_face_samek_k18_b54_2026_08_15.py
---

# Named Cost-2 Max≥4 Out-Face Same-`k` Reverse At `k=18` On `B_54(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_54(0)`,
scored only for the same-`k` pair `t(18,0,0)` versus `t(18,18,18)`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/cost2_max4_out_face_samek_k18_b54_2026_08_15.py`](../scripts/cost2_max4_out_face_samek_k18_b54_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_54(0)`, the stacked
rules `ν`, `μ`, and `ρ3` are

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
`|w_i|` equals `1)`, else `1`;

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

The displayed cost-2 max≥4 out-face rule `c2d4` is `ρ3` plus cost `2` (not `3`)
on a `2→2` hop whose destination has a larger max absolute
coordinate than the source and whose source max is at least `4`:

`c2d4(v→w) = 3` if `ρ3` would be `3`, else `2` if `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 4)`, else `1`.

Those clauses are the whole rule. Uniqueness is not claimed. This note is
the first display of same-`k` reverse at `k=18` under `c2d4`. That scale is
the last hold before the shared `k=19` wall: the body site `(19,19,19)` has
ℓ¹ norm `57` and is absent from `B_54(0)`.

The source-max floor skips `(3,2,0) → (4,2,0)` and fires, for example,
`(4,2,0) → (5,2,0)`. On `(3,2,0) → (4,2,0)` one has `|σ|=2→2` and
`max |w_i|=4 > max |v_i|=3`, but the source max is `3`, so the extra
clause is off and `c2d4=1`. The same hop has `ρ3=1`. On
`(4,2,0) → (5,2,0)` the extra clause is on, so `c2d4=2` while `ρ3=1`.
Therefore `ρ3` cannot price max≥4 out-face. The cost-3 max≥4 out-face
comparator `d4` prices that same fire hop at `3`, so `c2d4` is not leftover
of `d4`. The cost-2 max≥3 out-face comparator that drops the source-max
floor prices `(3,2,0) → (4,2,0)` at `2`, so `c2d4` is not leftover of that
comparator either. The unit-out-face hop `(1,1,0) → (2,1,0)` is already
`ρ3=3` by corridor-slide (`μ`), so the source-max floor does not change
that hop.

One Dijkstra from the origin on `B_54(0)` (215929 sites; 215928 nonzero)
returns

| site | `t_{c2d4}` |
|---|---:|
| `(18,0,0)` | `34` |
| `(18,18,18)` | `58` |

The same-`k` comparison at `k=18` is

`t(18,0,0)^2 / 324  ?  t(18,18,18)^2 / 972`,

which is `1156/324` versus `3364/972`, or equivalently `3 t(18,0,0)^2 ?
t(18,18,18)^2`. Substituting the computed times gives `3 · 34^2 = 3468`
and `58^2 = 3364`, so `3468 > 3364`. The inequality holds. Same-`k`
reverse at `k=18` under `c2d4` is yes.

The same Dijkstra restores `t(14,0,0) = 30` versus `t(14,14,14) = 46` and
keeps `t(17,0,0) = 33` versus `t(17,17,17) = 55`, `t(16,0,0) = 32` versus
`t(16,16,16) = 52`, `t(15,0,0) = 31` versus `t(15,15,15) = 49`, and
`t(1,0,0) = 3` versus `t(1,1,1) = 5`. Independently, `t(3,2,0) = 9`,
`t(4,2,0) = 10`, and `t(5,2,0) = 12`. The new axis site is
`t(54,0,0) = 75`. The shared axis site `t(51,0,0) = 67` is a `c2d4` score
on this ball. The site `(18,18,18)` has ℓ¹ norm `54`, so it is absent from
`B_51(0)`. The `B_54(0)` table is therefore not leftover of the `B_51(0)`
times.

A cheapest body walk uses no max≥4 out-face `2→2` grow, so the body
arrival stays `58`. The extra clause is still live: the cheapest walk to
`(5,2,0)` uses `(4,2,0) → (5,2,0)` at cost `2`. Pricing that hop at `2`
rather than `3` keeps reverse at `k=18`.

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
none of the hop costs. The integers `3`, `2`, and `1`, the support-size and
max-coordinate clauses, the source-max floor, and the arrival function `t`
are separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_54(0) = { v ∈ Z^3 : |v|_1 ≤ 54 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_54(0)`,
`t(v)` is the least sum of `c2d4` along a directed path from `0` to `v` in
that graph.

The first `ν` clause is seed-exit. The second is both weights `1`. The third
is support drop. The `μ` addendum taxes a `2→2` hop whose destination still
touches a unit coordinate. The `ρ3` addendum taxes a `3→3` hop whose
destination has exactly two unit coordinates. The `c2d4` addendum taxes a
`2→2` hop that grows the coordinate box on a face only after source max
at least `4`, and prices that hop at `2`.

The comparator `ρ3` uses only the first five clauses. On
`(4,2,0) → (5,2,0)` one has `|σ| : 2 → 2` and a growing max at source
height at least four, so `ρ3 = 1` while `c2d4 = 2`. Therefore `ρ3`
cannot price max≥4 out-face, and the `c2d4` scores below are not a leftover of
`ρ3`. Independently, `t(5,2,0) = 12`.

The comparator `d4` uses the same extra clause priced at `3`. On
`(4,2,0) → (5,2,0)` one has `c2d4 = 2` while `d4 = 3`. Therefore the
`c2d4` scores are not leftover of `d4`. Independently, `t(5,2,0) = 12`
under `c2d4` while a `d4` walk through that hop costs `13`.

The site `(18,0,0)` has ℓ¹ norm `18` and therefore also lies in `B_51(0)`.
The site `(18,18,18)` has ℓ¹ norm `54`, so it is absent from `B_51(0)`. The
`B_54(0)` table is therefore not leftover of the `B_51(0)` times.

## Theorem 1 — Arrivals At `k=18` Under `c2d4`

One origin Dijkstra on `B_54(0)` returns

```text
t(18,0,0) = 34
t(18,18,18) = 58
```

Both sites lie in `B_54(0)`. The site `(18,18,18)` has ℓ¹ norm `54`, so it
is absent from `B_51(0)`. The pair is computed on `B_54(0)`, not copied
from a smaller-ball table. These values are Dijkstra outputs, not fitted
scalars.

A witness axis walk of cost `34` is seed-exit `3` onto `(1,0,0)`, leave-axis
`1` onto `(1,1,0)`, enter-body `1` onto `(1,1,1)`, ridge-slide `3` onto
`(1,2,1)`, seventeen support-preserving cost-`1` body hops to `(18,2,1)`,
support-drop `3` onto `(18,2,0)`, corridor-slide `3` onto `(18,1,0)`, and
support-drop `3` onto `(18,0,0)`, summing to `34`. That walk never uses a
`2→2` dest whose max grows at source height at least four. That walk is a
witness of cost `34`, not a uniqueness claim.

A witness body walk of cost `58` is seed-exit `3` onto `(1,0,0)`, leave-axis
`1` onto `(1,1,0)`, corridor-slide `3` onto `(1,2,0)`, non-hugging face hop
`1` onto `(2,2,0)`, enter-body `1` onto `(2,2,1)`, seventeen
support-preserving cost-`1` body hops to `(2,2,18)`, sixteen cost-`1`
body hops to `(2,18,18)`, and sixteen cost-`1` body hops to
`(18,18,18)`, summing to `58`. That walk uses no max≥4 out-face `2→2`
grow. That walk is a witness of cost `58`, not a uniqueness claim.

A witness that the skipped hop is cheap is seed-exit `3` onto `(1,0,0)`,
leave-axis `1` onto `(1,1,0)`, corridor-slide `3` onto `(1,2,0)`,
non-hugging face hop `1` onto `(2,2,0)`, grow `1` onto `(3,2,0)`, and the
skipped grow `1` onto `(4,2,0)`, summing to `10`. Independently,
`t(4,2,0) = 10`. Independently, `t(3,2,0) = 9`. Continuing by
max≥4 out-face `2` onto `(5,2,0)` sums to `12`. Independently,
`t(5,2,0) = 12`. Replacing only that last hop by its `ρ3` price `1`
would yield `11`, which is not the `c2d4` arrival. Replacing it by the
`d4` price `3` would yield `13`, which is also not the `c2d4` arrival.

## Theorem 2 — Reverse At The Same-`k` Pair `k=18`

The Euclidean-normalized comparison at `k=18` is

`t(18,0,0)^2 / 324  ?  t(18,18,18)^2 / 972`.

The computed integers give `3 · 34^2 = 3468` and `58^2 = 3364`, so
`3468 > 3364`. Arrival per Euclidean length is larger at `(18,0,0)` than
at `(18,18,18)`. Same-`k` reverse at `k=18` under `c2d4` is yes. The
comparison is displayed, not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `c2d4` is a displayed scoring device on `B_54(0)`. Do not write
`c2d4` into Admissibility. Do not write c2d4 into Admissibility. Do not
attach L1. It is not a replacement for first arrival, and it is
not offered as the unique hop-cost with same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_54(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_54(0) for the displayed rule c2d4 at k=18; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `c2d4` among hop-costs that reverse any same-`k` pair.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_54(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=18`.
- Any reuse of a smaller-ball arrival table as a substitute for the
  radius-`54` Dijkstra.
- Any adoption of `c2d4` as an admissibility rule.
