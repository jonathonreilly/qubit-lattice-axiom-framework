---
claim_id: height_ridge_samek_k7_b21_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=7 under the named height-ridge hop-cost on B_21(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/height_ridge_samek_k7_b21_2026_08_15.py
---

# Named Height-Ridge Same-k Reverse At k=7 On B_21(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_21(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=7`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/height_ridge_samek_k7_b21_2026_08_15.py`](../scripts/height_ridge_samek_k7_b21_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named body-slide hop-cost `β` (every `3→3` hop costs `3`) kills same-`k`
reverse at `k=7` by `19` versus `37`. The residual scored here is the named
height-ridge hop-cost `ζ` on `B_21(0)`: `ρ3` plus cost `3` on a `3→3` hop
whose destination has exactly two coordinates of absolute value `m`, with
`m` equal to the least `|w_i|` and `m ≥ 2`. The new clause taxes only
height-`m` ridges with `m ≥ 2`, not every `3→3`. This is the first display
of `ζ` at `k=7`. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_21(0)`, let `ν` be
the support-drop rule that costs `3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or
`|σ_w| < |σ_v|`, else `1`. Let `μ` be the corridor-slide rule that costs
`3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero `|w_i|`
equals `1)`, else `1`. Let `ρ3` be the ridge-slide rule that costs `3` if
`μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two `|w_i|` equal `1)`,
else `1`. The displayed rule `ζ` is

`ζ(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `m` and `m = min_j |w_j|` and `m ≥ 2)`, else `1`.

The extra clause is a height-`m` ridge: both ends have support `3`, and
the destination has exactly two coordinates at the least absolute value,
with that least value at least `2`. Those clauses are the whole rule.

One Dijkstra from the origin on `B_21(0)` (13287 sites; 13286 nonzero)
gives

`t(7,0,0) = 19`, `t(7,7,7) = 25`.

The displayed same-`k` comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

which is `361/49` versus `625/147`, or equivalently `1083 > 625`. The
inequality holds. Same-`k` reverse at `k=7` under `ζ` is yes.
Independently, the new axis site is `t(21,0,0) = 37`. The shared axis
site `t(18,0,0) = 30` is a `ζ` score on this ball, not a leftover.

The pair is not leftover of `β`: the same sites under `β` are `19` versus `37`,
and `β` prices every `3→3` hop at `3`. On the generic body hop
`(2,7,7) → (3,7,7)` one has `|σ| : 3 → 3` with least `|w_i|` attained only
once, so `ζ = 1` while `β = 3`. Therefore `β` cannot be identified with
`ζ`. The pair is not leftover of `ρ3` as a rule: on the height-2 ridge hop
`(2,2,2) → (3,2,2)` one has `|σ| : 3 → 3`, least `|w_i|` equal to `2`, and
exactly two coordinates equal to that least value, so `ρ3 = 1` while
`ζ = 3`. Therefore `ρ3` cannot price height-m ridge. The same-`k` arrivals
at `k=7` happen to coincide with the `ρ3` pair because a cheapest body
witness never takes a height-`m` ridge hop. The on-ball site `(3,2,2)`
arrives at `13`, which records that the new clause is live.

The site `(7,7,7)` has ℓ¹ norm `21`, so it is absent from `B_18(0)`. The
`B_21(0)` table is therefore not leftover of the `B_18(0)` times.

The rule is displayed, not adopted. Do not write `ζ` into Admissibility.
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
none of the hop costs. The integers `3` and `1`, the support-size clauses,
the least-coordinate clause, the two-equal-to-minimum clause, and the
arrival function `t` are separately displayed mathematical inputs. No
axiom text is edited.

## Named Rule

Let `B_21(0) = { v ∈ Z^3 : |v|_1 ≤ 21 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_21(0)`,
`t(v)` is the least sum of `ζ` along a directed path from `0` to `v` in
that graph.

The comparator `ρ3` uses only the first five clauses of `ζ`. On the
height-2 ridge hop `(2,2,2) → (3,2,2)` one has `|σ| : 3 → 3` and exactly
two `|w_i|` equal to the least value `2`, so `ρ3 = 1` while `ζ = 3`.
Therefore `ρ3` cannot price height-m ridge. The comparator `β` uses every
`3→3` hop. On `(2,7,7) → (3,7,7)` one has `|σ| : 3 → 3` but the least
absolute coordinate is attained only once, so `ζ = 1` while `β = 3`.
Therefore `ζ` taxes only height-m ridges, not every `3→3`.

## Theorem 1 — Arrivals `t(7,0,0)` And `t(7,7,7)` On `B_21(0)`

One origin Dijkstra on `B_21(0)` returns the integer arrivals

| site | `t_ζ` |
|---|---:|
| `(7,0,0)` | `19` |
| `(7,7,7)` | `25` |

Every listed site lies in `B_21(0)`. The site `(7,7,7)` has ℓ¹ norm `21`,
so it is absent from `B_18(0)`. The pair is computed on `B_21(0)`, not
copied from a smaller-ball table and not copied from the `β` pair
`19` versus `37`. These values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `19` is seed-exit `3` onto `(0,-1,0)`,
support-increase `1` onto `(1,-1,0)`, corridor-slide `3` onto `(1,-2,0)`,
six support-preserving cost-`1` height-`2` slides to `(7,-2,0)`,
corridor-slide `3` onto `(7,-1,0)`, and support-drop `3` onto `(7,0,0)`,
summing to `19`. A witness body walk of cost `25` is seed-exit `3` onto
`(0,0,1)`, support-increase `1` onto `(0,1,1)`, corridor-slide `3` onto
`(0,1,2)`, eleven support-preserving cost-`1` face hops to `(0,7,7)`,
support-increase `1` onto `(1,7,7)`, and six support-preserving cost-`1`
body hops onto `(7,7,7)`, summing to `25`. Those body hops land on
`(n,7,7)`, where the least absolute coordinate is attained once, so they
are not height-`m` ridges. Those walks are witnesses, not a uniqueness
claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=7`

The Euclidean-normalized comparison at `k=7` is

`t(7,0,0)^2 / 49  ?  t(7,7,7)^2 / 147`,

equivalently `3 t(7,0,0)^2 ? t(7,7,7)^2`. Substituting the computed times
gives `3 · 19^2 = 1083` and `25^2 = 625`, so

`1083 > 625`.

Arrival per Euclidean length is larger at `(7,0,0)` than at `(7,7,7)`.
Same-`k` reverse at `k=7` under `ζ` is yes. The comparison is displayed,
not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `ζ` is a displayed scoring device on `B_21(0)`. Do not write
`ζ` into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_21(0) for one named hop-cost at k=7. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_21(0) for the displayed rule ζ at k=7; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ζ` among hop-costs that reverse the same-`k` pair at `k=7`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_21(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=7`.
- Any reuse of the `β` arrival table as a substitute for the `ζ` Dijkstra.
- Any reuse of the `B_18(0)` arrival table as a substitute for the
  radius-`21` Dijkstra.
