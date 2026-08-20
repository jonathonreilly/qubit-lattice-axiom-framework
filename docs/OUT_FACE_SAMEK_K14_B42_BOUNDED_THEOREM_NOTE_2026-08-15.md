---
claim_id: out_face_samek_k14_b42_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=14 under the named out-face hop-cost on B_42(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/out_face_samek_k14_b42_2026_08_15.py
---

# Named Out-Face Same-k Reverse At k=14 On B_42(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_42(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=14`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/out_face_samek_k14_b42_2026_08_15.py`](../scripts/out_face_samek_k14_b42_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

This is the first display of the named out-face hop-cost `ω` at the
`k=14` wall. Mid-leave is empty on six-neighbor hops, so it agrees with
the ridge-slide rule `ρ3` on that graph. The named rule `ω` is `ρ3` plus
cost `3` on a `2→2` hop whose destination has strictly larger max
absolute coordinate than the source (growing the box on a face). Same-`k`
reverse under `ρ3` fails at `k=14` (`26` versus `46`). The residual scored
here is whether `ω` restores reverse at `k=14` on `B_42(0)`. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_42(0)`, the displayed
rule `ω` is

`ω(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|)`, else `1`,

where `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly
two `|w_i|` equal `1)`, else `1`,
`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`, and
`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first three clauses are seed-exit, both weights `1`, and support drop.
The fourth clause is the axis-hugging `2→2` corridor slide. The fifth
clause is the unit-height ridge slide. The sixth clause is the out-face
`2→2` that grows the max absolute coordinate. Those six clauses are the
whole rule.

One Dijkstra from the origin on `B_42(0)` (102425 sites; 102424 nonzero) gives

`t(14,0,0) = 30`, `t(14,14,14) = 46`.

The displayed same-`k` comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

which is `900/196` versus `2116/588`, or equivalently `2700 > 2116`. The
inequality holds. Same-`k` reverse at `k=14` under `ω` is yes.
Independently, the new axis site is `t(42,0,0) = 64`. The shared axis
site `t(39,0,0) = 55` is a `ω` score on this ball.

The same-`k` pair under `ρ3` is `26` versus `46`. That mismatch on the
axis is not a leftover of a `ρ3` table: the extra out-face clause is live
on the ball. On the out-face hop `(2,2,0) → (3,2,0)` one has `|σ| : 2 → 2`
and `max |w_i| = 3 > max |v_i| = 2`, while the least nonzero `|w_i|` is
`2`, so `ρ3 = 1` while `ω = 3`. Therefore `ρ3` cannot price the out-face
grow. The same hop is a `ω` cost-`3` step, and `t(3,2,0) = 11` under `ω`.
The corridor hop `(1,1,0) → (2,1,0)` also grows the max absolute
coordinate, but it is already `ρ3 = 3` by the hugging clause. A cheapest
`ω` walk to `(14,14,14)` uses no out-face `2→2` grow, so the body arrival
stays `46`. The site `(14,14,14)` has ℓ¹ norm `42`, so it is absent from
`B_39(0)`. The `B_42(0)` table is therefore not leftover of the `B_39(0)` times.

The rule is displayed, not adopted. Do not write `ω` into Admissibility.
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
the least-nonzero-coordinate clause, the unit-height ridge clause, the
out-face grow clause, and the arrival function `t` are separately displayed
mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_42(0) = { v ∈ Z^3 : |v|_1 ≤ 42 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_42(0)`,
`t(v)` is the least sum of `ω` along a directed path from `0` to `v` in
that graph.

The comparator `ρ3` uses only the first five clauses of `ω`. On the
out-face hop `(2,2,0) → (3,2,0)` one has `|σ| : 2 → 2` and a strictly
larger dest max absolute coordinate, so `ρ3 = 1` while `ω = 3`. Therefore
`ρ3` cannot price the out-face grow, and the `ω` scores below are not a
leftover of `ρ3`. On the corridor hop `(1,1,0) → (2,1,0)` both `ρ3` and
`ω` cost `3`. On the interior body hop `(14,14,1) → (14,14,2)` the hop
is `3→3` with only one absolute coordinate equal to `1`, so both `ρ3`
and `ω` cost `1`.

## Theorem 1 — Arrivals `t(14,0,0)` And `t(14,14,14)` On `B_42(0)`

One origin Dijkstra on `B_42(0)` returns the integer arrivals

| site | `t_ω` |
|---|---:|
| `(14,0,0)` | `30` |
| `(14,14,14)` | `46` |

Every listed site lies in `B_42(0)`. The site `(14,14,14)` has ℓ¹ norm `42`,
so it is absent from `B_39(0)`. The pair is computed on `B_42(0)`, not
copied from a smaller-ball table and not copied from a `ρ3` table. These
values are Dijkstra outputs, not fitted scalars.

A witness axis walk of cost `30` is seed-exit `3` onto `(1,0,0)`,
leave-axis `1` onto `(1,1,0)`, enter-body `1` onto `(1,1,1)`, ridge-slide
`3` onto `(2,1,1)`, support-preserving cost-`1` hop onto `(2,2,1)`, twelve
support-preserving cost-`1` body hops to `(14,2,1)`, ridge-slide `3` onto
`(14,1,1)`, support-drop `3` onto `(14,1,0)`, and support-drop `3` onto
`(14,0,0)`, summing to `30`. That walk is a witness of cost `30`, not a
uniqueness claim. The pure axis 1-skeleton walk costs `42` and is not
cheapest.

A witness body walk of cost `46` is the same prefix of cost `9` to
`(2,2,1)`, twelve cost-`1` body hops to `(14,2,1)`, twelve cost-`1` body
hops to `(14,14,1)`, and thirteen support-preserving cost-`1` body hops to
`(14,14,14)`, summing to `46`. Those last hops have dest with only one
absolute coordinate equal to `1`, or with all three coordinates large, so
they are not unit-height ridges and are not out-face `2→2` grows. That
walk is a witness of cost `46`, not a uniqueness claim.

## Theorem 2 — Reverse At The Same-`k` Scale `k=14`

The Euclidean-normalized comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

equivalently `3 t(14,0,0)^2 ? t(14,14,14)^2`. Substituting the computed times
gives `3 · 30^2 = 2700` and `46^2 = 2116`, so

`2700 > 2116` is true; `2700 > 2116` holds.

Arrival per Euclidean length is larger at `(14,0,0)` than at
`(14,14,14)`. Same-`k` reverse at `k=14` under `ω` is yes. The comparison
is displayed, not adopted. The inequality holds.

## Theorem 3 — Displayed, Not Adopted

The rule `ω` is a displayed scoring device on `B_42(0)`. Do not write `ω`
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
conditional_surface_status: "exact on B_42(0) for the displayed rule ω at k=14; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ω` among hop-costs that reverse the same-`k` pair at `k=14`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_42(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=14`.
- Any reuse of a `ρ3` arrival table as a substitute for the `ω` Dijkstra.
