---
claim_id: corridor_slide_doubled_pairing_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Doubled-axis versus body-diagonal reverse under the named corridor-slide hop-cost on B_12(0) is reported for available k=1..4. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/corridor_slide_doubled_pairing_b12_2026_08_15.py
---

# Named Corridor-Slide Doubled Pairing On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_12(0)`,
scored only for the doubled pairing `((2k,0,0),(k,k,k))` at each
available integer `k=1,2,3,4`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/corridor_slide_doubled_pairing_b12_2026_08_15.py`](../scripts/corridor_slide_doubled_pairing_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The named corridor-slide hop-cost `μ` is the already scored support-drop
rule `ν` plus cost `3` on a `2→2` hop whose destination has least nonzero
absolute coordinate equal to `1` (an axis-hugging face slide). Doubled
pairing reverse under `ν` holds only at `k=1,2` and fails at `k=3+`.
Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_12(0)`, the displayed
comparator `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The displayed rule `μ` is

`μ(v→w) = 3` if `ν(v→w)` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`.

The first three clauses are those of `ν`: seed-exit, both weights `1`, and
support drop. The fourth clause is the axis-hugging `2→2` slide. Those four
clauses are the whole rule.

For each `k=1,2,3,4` both `(2k,0,0)` and `(k,k,k)` lie in `B_12(0)`, so
no pair is omitted. One Dijkstra from the origin on `B_12(0)` (2625 sites;
2624 nonzero) gives

| `k` | site axis | `t(2k,0,0)` | site body | `t(k,k,k)` | `t(2k,0,0)^2/(4k^2)` | `t(k,k,k)^2/(3k^2)` | reverse |
|---|---|---:|---|---:|---|---|---|
| `1` | `(2,0,0)` | `6` | `(1,1,1)` | `5` | `36/4` | `25/3` | yes |
| `2` | `(4,0,0)` | `12` | `(2,2,2)` | `8` | `144/16` | `64/12` | yes |
| `3` | `(6,0,0)` | `16` | `(3,3,3)` | `11` | `256/36` | `121/27` | yes |
| `4` | `(8,0,0)` | `18` | `(4,4,4)` | `14` | `324/64` | `196/48` | yes |

Equivalently, `3 t(2k,0,0)^2 ? 4 t(k,k,k)^2` is `108 > 100`, `432 > 256`,
`768 > 484`, and `972 > 784`. The inequality holds at every available
`k=1..4`. Independently, the new axis site is `t(12,0,0) = 26`.

The pair table is not leftover of `ν`: the same sites under `ν` are
`6,10,12,14` versus `5,8,11,14`, and reverse already fails at `k=3`
(`12` versus `11`; `432 > 484` fails). The extra corridor-slide clause is
what changes the axis arrivals at `k=2,3,4`. On the hugging hop
`(1,1,0) → (2,1,0)` one has `|σ| : 2 → 2` and least nonzero `|w_i| = 1`,
so `ν = 1` while `μ = 3`. The leave-axis hop `(0,-1,0) → (1,-1,0)` stays
at cost `1` under both `ν` and `μ`. Therefore `ν` cannot price the
axis-hugging slide, and the `μ` scores below are not a leftover of `ν`.
The site `(4,4,4)` has ℓ¹ norm `12`, so it is absent from `B_11(0)`. The
`B_12(0)` table is therefore not leftover of a smaller-ball table.

The rule is displayed, not adopted. Do not write `μ` into Admissibility.
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
the least-nonzero-coordinate test, and the arrival function `t` are
separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_12(0) = { v ∈ Z^3 : |v|_1 ≤ 12 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_12(0)`,
`t(v)` is the least sum of `μ` along a directed path from `0` to `v` in
that graph.

The comparator `ν` uses only the first three clauses of `μ`. On the
axis-hugging slide `(1,1,0) → (2,1,0)` one has `|σ| : 2 → 2` and least
nonzero `|w_i| = 1`, so `ν = 1` while `μ = 3`. Therefore `ν` cannot price
the corridor slide, and the `μ` scores below are not a leftover of `ν`.

The pairing is not the same-`k` axis / body pair `(k,0,0)` versus
`(k,k,k)`. It is the doubled pairing `((2k,0,0),(k,k,k))`.

## Theorem 1 — Arrivals For Each Available `k=1..4`

One origin Dijkstra on `B_12(0)` returns the integer arrivals

| site | `t_μ` |
|---|---:|
| `(2,0,0)` | `6` |
| `(1,1,1)` | `5` |
| `(4,0,0)` | `12` |
| `(2,2,2)` | `8` |
| `(6,0,0)` | `16` |
| `(3,3,3)` | `11` |
| `(8,0,0)` | `18` |
| `(4,4,4)` | `14` |

Every listed site lies in `B_12(0)`. The site `(4,4,4)` has ℓ¹ norm `12`,
so it is absent from `B_11(0)`. The pair is computed on `B_12(0)`, not
copied from a smaller-ball table and not copied from the `ν` table
`6,10,12,14` versus `5,8,11,14`. These values are Dijkstra outputs, not
fitted scalars.

A witness walk of cost `6` from `0` to `(2,0,0)` is seed-exit `3` onto
`(1,0,0)` and both-weights-`1` cost `3` onto `(2,0,0)`, summing to `6`.
A witness walk of cost `5` from `0` to `(1,1,1)` is seed-exit `3` onto
`(0,0,1)`, leave-axis `1` onto `(0,1,1)`, and enter-body `1` onto
`(1,1,1)`, summing to `5`. A witness walk of cost `12` from `0` to
`(4,0,0)` is four both-weights-`1` axis hops
`0 → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0)` of costs `3,3,3,3`, summing
to `12`. A witness walk of cost `8` from `0` to `(2,2,2)` is seed-exit
`3` onto `(0,0,1)`, leave-axis `1` onto `(0,1,1)`, enter-body `1` onto
`(1,1,1)`, and three support-preserving cost-`1` body hops to `(2,2,2)`,
summing to `8`. A witness walk of cost `16` from `0` to `(6,0,0)` is
seed-exit `3` onto `(0,-1,0)`, leave-axis `1` onto `(0,-1,-1)`, enter-body
`1` onto `(1,-1,-1)`, five support-preserving cost-`1` body hops to
`(6,-1,-1)`, support-drop `3` onto `(6,-1,0)`, and support-drop `3` onto
`(6,0,0)`, summing to `16`. A witness walk of cost `11` from `0` to
`(3,3,3)` is seed-exit `3` onto `(0,0,1)`, leave-axis `1` onto `(0,1,1)`,
enter-body `1` onto `(1,1,1)`, and six support-preserving cost-`1` body
hops to `(3,3,3)`, summing to `11`. A witness walk of cost `18` from `0`
to `(8,0,0)` is seed-exit `3` onto `(0,-1,0)`, leave-axis `1` onto
`(0,-1,-1)`, enter-body `1` onto `(1,-1,-1)`, seven support-preserving
cost-`1` body hops to `(8,-1,-1)`, support-drop `3` onto `(8,-1,0)`, and
support-drop `3` onto `(8,0,0)`, summing to `18`. A witness walk of cost
`14` from `0` to `(4,4,4)` is seed-exit `3` onto `(0,0,1)`, leave-axis `1`
onto `(0,1,1)`, enter-body `1` onto `(1,1,1)`, and nine support-preserving
cost-`1` body hops to `(4,4,4)`, summing to `14`. Those walks are
witnesses of the listed costs, not uniqueness claims.

## Theorem 2 — Reverse At Each Available Doubled Pair

For each available `k=1,2,3,4` the Euclidean-normalized comparison is

`t(2k,0,0)^2 / (4k^2)  ?  t(k,k,k)^2 / (3k^2)`,

equivalently `3 t(2k,0,0)^2 ? 4 t(k,k,k)^2`. Substituting the computed
times gives

| `k` | `3 t(2k,0,0)^2` | `4 t(k,k,k)^2` | reverse |
|---|---:|---:|---|
| `1` | `108` | `100` | `108 > 100` |
| `2` | `432` | `256` | `432 > 256` |
| `3` | `768` | `484` | `768 > 484` |
| `4` | `972` | `784` | `972 > 784` |

Arrival per Euclidean length is larger at `(2k,0,0)` than at `(k,k,k)` for
every available `k=1..4`. Doubled pairing reverse under `μ` is yes at each
of those four scales. The comparison is displayed, not adopted. The
inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `μ` is a displayed scoring device on `B_12(0)`. Do not write `μ`
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
conditional_surface_status: "exact on B_12(0) for the displayed rule μ at available k=1..4 on ((2k,0,0),(k,k,k)); no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `μ` among hop-costs that reverse the doubled pairing at
  any available `k`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_12(0)`.
- Any score for a pair that is not `((2k,0,0),(k,k,k))`.
- Any reuse of the `ν` arrival table as a substitute for the `μ` Dijkstra.
- Any omitted pair among `k=1..4`: both sites of each pair lie in `B_12(0)`.
