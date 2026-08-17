---
claim_id: ridge_slide_doubled_pairing_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Doubled-axis versus body-diagonal reverse under the named ridge-slide hop-cost on B_12(0) is reported for available k=1..4. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ridge_slide_doubled_pairing_b12_2026_08_15.py
---

# Named Ridge-Slide Doubled Pairing On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_12(0)`,
scored only for the doubled pairing `((2k,0,0),(k,k,k))` at each
available integer `k=1,2,3,4`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/ridge_slide_doubled_pairing_b12_2026_08_15.py`](../scripts/ridge_slide_doubled_pairing_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named ridge-slide hop-cost `ρ3` is the already scored corridor-slide
rule `μ` plus cost `3` on a `3→3` hop whose destination has exactly two
coordinates of absolute value `1`. Doubled pairing reverse under `μ`
holds at every available `k=1..4`. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_12(0)`, the displayed
comparator `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The displayed comparator `μ` is

`μ(v→w) = 3` if `ν(v→w)` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`.

The displayed rule `ρ3` is

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

The extra clause is a ridge slide: both ends have support `3`, and the
destination has exactly two unit coordinates. It is not the all-`3→3`
body-slide tax. Those clauses are the whole rule.

For each `k=1,2,3,4` both `(2k,0,0)` and `(k,k,k)` lie in `B_12(0)`, so
no pair is omitted. One Dijkstra from the origin on `B_12(0)` (2625 sites;
2624 nonzero) gives

| `k` | site axis | `t(2k,0,0)` | site body | `t(k,k,k)` | `t(2k,0,0)^2/(4k^2)` | `t(k,k,k)^2/(3k^2)` | reverse |
|---|---|---:|---|---:|---|---|---|
| `1` | `(2,0,0)` | `6` | `(1,1,1)` | `5` | `36/4` | `25/3` | yes |
| `2` | `(4,0,0)` | `12` | `(2,2,2)` | `10` | `144/16` | `100/12` | yes |
| `3` | `(6,0,0)` | `18` | `(3,3,3)` | `13` | `324/36` | `169/27` | yes |
| `4` | `(8,0,0)` | `20` | `(4,4,4)` | `16` | `400/64` | `256/48` | yes |

Equivalently, `3 t(2k,0,0)^2 ? 4 t(k,k,k)^2` is `108 > 100`, `432 > 400`,
`972 > 676`, and `1200 > 1024`. The inequality holds at every available
`k=1..4`. Independently, the new axis site is `t(12,0,0) = 28`.

The pair table is not leftover of `μ`: the same sites under `μ` are
`6,12,16,18` versus `5,8,11,14`. The extra ridge-slide clause changes
the body arrivals at `k=2,3,4` and the axis arrivals at `k=3,4`. On the
ridge hop `(1,1,1) → (2,1,1)` one has `|σ_v|=|σ_w|=3` and exactly two
`|w_i|=1`, so `μ = 1` while `ρ3 = 3`. Therefore `μ` cannot price the
ridge slide. On the interior `3→3` hop `(2,2,2) → (3,2,2)` the destination
has no unit coordinate, so both `μ` and `ρ3` cost `1`. The site `(4,4,4)`
has ℓ¹ norm `12`, so it is absent from `B_11(0)`. The `B_12(0)` table is
therefore not leftover of a smaller-ball table.

The rule is displayed, not adopted. Do not write `ρ3` into Admissibility.
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
the ridge unit-coordinate test, and the arrival function `t` are separately
displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_12(0) = { v ∈ Z^3 : |v|_1 ≤ 12 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_12(0)`,
`t(v)` is the least sum of `ρ3` along a directed path from `0` to `v` in
that graph.

The comparator `μ` uses the three support-drop clauses and the
axis-hugging `2→2` slide. On the ridge slide `(1,1,1) → (2,1,1)` one has
`|σ_v|=|σ_w|=3` and exactly two `|w_i|=1`, so `μ = 1` while `ρ3 = 3`.
Therefore `μ` cannot price the ridge slide, and the `ρ3` scores below are
not a leftover of `μ`. The same extra clause prices the corridor hop
`(1,-1,-1) → (2,-1,-1)` at `3`. On the interior `3→3` hop
`(2,2,2) → (3,2,2)` the destination has no unit coordinate, so both
`μ` and `ρ3` cost `1`.

The pairing is not the same-`k` axis / body pair `(k,0,0)` versus
`(k,k,k)`. It is the doubled pairing `((2k,0,0),(k,k,k))`.

## Theorem 1 — Arrivals For Each Available `k=1..4`

One origin Dijkstra on `B_12(0)` returns the integer arrivals

| site | `t_ρ3` |
|---|---:|
| `(2,0,0)` | `6` |
| `(1,1,1)` | `5` |
| `(4,0,0)` | `12` |
| `(2,2,2)` | `10` |
| `(6,0,0)` | `18` |
| `(3,3,3)` | `13` |
| `(8,0,0)` | `20` |
| `(4,4,4)` | `16` |

Every listed site lies in `B_12(0)`. The site `(4,4,4)` has ℓ¹ norm `12`,
so it is absent from `B_11(0)`. The pair is computed on `B_12(0)`, not
copied from a smaller-ball table and not copied from the `μ` table
`6,12,16,18` versus `5,8,11,14`. These values are Dijkstra outputs, not
fitted scalars.

A witness walk of cost `6` from `0` to `(2,0,0)` is seed-exit `3` onto
`(1,0,0)` and both-weights-`1` cost `3` onto `(2,0,0)`, summing to `6`.
A witness walk of cost `5` from `0` to `(1,1,1)` is seed-exit `3` onto
`(0,0,1)`, leave-axis `1` onto `(0,1,1)`, and enter-body `1` onto
`(1,1,1)`, summing to `5`. A witness walk of cost `12` from `0` to
`(4,0,0)` is four both-weights-`1` axis hops
`0 → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0)` of costs `3,3,3,3`, summing
to `12`. A witness walk of cost `10` from `0` to `(2,2,2)` is seed-exit
`3` onto `(0,0,1)`, leave-axis `1` onto `(0,1,1)`, corridor-slide `3` onto
`(0,1,2)`, non-hugging `2→2` of cost `1` onto `(0,2,2)`, enter-body `1`
onto `(1,2,2)`, and support-preserving cost-`1` body hop onto `(2,2,2)`,
summing to `10`. A witness walk of cost `18` from `0` to `(6,0,0)` is
six both-weights-`1` axis hops
`0 → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0) → (5,0,0) → (6,0,0)` of
costs `3,3,3,3,3,3`, summing to `18`. A witness walk of cost `13` from
`0` to `(3,3,3)` is seed-exit `3` onto `(0,0,1)`, leave-axis `1` onto
`(0,1,1)`, corridor-slide `3` onto `(0,1,2)`, three non-hugging `2→2`
hops of cost `1` to `(0,3,3)`, enter-body `1` onto `(1,3,3)`, and two
support-preserving cost-`1` body hops to `(3,3,3)`, summing to `13`.
A witness walk of cost `20` from `0` to `(8,0,0)` is seed-exit `3` onto
`(0,-1,0)`, leave-axis `1` onto `(1,-1,0)`, corridor-slide `3` onto
`(1,-2,0)`, seven non-hugging `2→2` hops of cost `1` to `(8,-2,0)`,
corridor-slide `3` onto `(8,-1,0)`, and support-drop `3` onto `(8,0,0)`,
summing to `20`. A witness walk of cost `16` from `0` to `(4,4,4)` is
seed-exit `3` onto `(0,0,1)`, leave-axis `1` onto `(0,1,1)`,
corridor-slide `3` onto `(0,1,2)`, five non-hugging `2→2` hops of cost
`1` to `(0,4,4)`, enter-body `1` onto `(1,4,4)`, and three
support-preserving cost-`1` body hops to `(4,4,4)`, summing to `16`.
Those walks are witnesses of the listed costs, not uniqueness claims.

## Theorem 2 — Reverse At Each Available Doubled Pair

For each available `k=1,2,3,4` the Euclidean-normalized comparison is

`t(2k,0,0)^2 / (4k^2)  ?  t(k,k,k)^2 / (3k^2)`,

equivalently `3 t(2k,0,0)^2 ? 4 t(k,k,k)^2`. Substituting the computed
times gives

| `k` | `3 t(2k,0,0)^2` | `4 t(k,k,k)^2` | reverse |
|---|---:|---:|---|
| `1` | `108` | `100` | `108 > 100` |
| `2` | `432` | `400` | `432 > 400` |
| `3` | `972` | `676` | `972 > 676` |
| `4` | `1200` | `1024` | `1200 > 1024` |

Arrival per Euclidean length is larger at `(2k,0,0)` than at `(k,k,k)` for
every available `k=1..4`. Doubled pairing reverse under `ρ3` is yes at each
of those four scales. The comparison is displayed, not adopted. The
inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `ρ3` is a displayed scoring device on `B_12(0)`. Do not write `ρ3`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
doubled-pairing reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer doubled-pairing arrivals and reverse comparison on the finite ball B_12(0) for one named hop-cost at available k=1..4. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_12(0) for the displayed rule ρ3 at available k=1..4 on ((2k,0,0),(k,k,k)); no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ρ3` among hop-costs that reverse the doubled pairing at
  any available `k`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_12(0)`.
- Any score for a pair that is not `((2k,0,0),(k,k,k))`.
- Any reuse of the `μ` arrival table as a substitute for the `ρ3` Dijkstra.
- Any omitted pair among `k=1..4`: both sites of each pair lie in `B_12(0)`.
