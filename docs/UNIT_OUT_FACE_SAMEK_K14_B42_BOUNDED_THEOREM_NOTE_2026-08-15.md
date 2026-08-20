---
claim_id: unit_out_face_samek_k14_b42_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=14 under the named unit-out-face hop-cost on B_42(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/unit_out_face_samek_k14_b42_2026_08_15.py
---

# Named Unit-Out-Face Same-k Reverse At k=14 On B_42(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_42(0)`,
scored only for the same-`k` axis versus body-diagonal arrival ratio at
`k=14`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/unit_out_face_samek_k14_b42_2026_08_15.py`](../scripts/unit_out_face_samek_k14_b42_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

This is the first display of the named unit-out-face hop-cost `uf` at the
`k=14` residual where ridge-slide `ρ3` fails same-`k` reverse. The named
rule `uf` is `ρ3` plus cost `3` on a `2→2` hop whose destination max
absolute coordinate grows and whose source max equals `1`. That extra
clause names the unit-out-face hop `(1,1,0) → (2,1,0)` and skips every
later face grow, including `(2,2,0) → (3,2,0)`. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_42(0)`, the displayed
rule `uf` is

`uf(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|` and `max_i |v_i| = 1)`, else `1`,

where `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly
two `|w_i|` equal `1)`, else `1`,
`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equal `1)`, else `1`, and
`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first three clauses are seed-exit, both weights `1`, and support drop.
The fourth clause is the axis-hugging `2→2` corridor slide. The fifth
clause is the unit-height ridge slide. The sixth clause is unit-out-face:
grow the box on a face only from source max `1`. Those six clauses are
the whole rule.

On the six-neighbor graph the sixth clause does not change any hop cost.
The unit-out-face hop `(1,1,0) → (2,1,0)` has `|σ| : 2 → 2`, dest max
strictly larger, and source max `1`, so the sixth predicate holds, but
the least nonzero dest coordinate is `1`, so corridor-slide already
prices the hop at `3`. Independently, the deep-out-face hop
`(2,2,0) → (3,2,0)` has source max `2`, so it is not unit-out-face;
`uf = 1` there while a deep-out-face grow would be `3`. Therefore `uf`
agrees with `ρ3` on every six-neighbor hop, and unit-out-face alone does
not restore the `ρ3` same-`k` failure at `k=14`.

One Dijkstra from the origin on `B_42(0)` (102425 sites; 102424 nonzero)
gives

`t(14,0,0) = 26`, `t(14,14,14) = 46`.

The displayed same-`k` comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

which is `676/196` versus `2116/588`, or equivalently `2028 > 2116`. The
inequality does not hold. Same-`k` reverse at `k=14` under `uf` is no.
Independently, the new axis site is `t(42,0,0) = 58`. The shared axis
site `t(39,0,0) = 51` is a `uf` score on this ball.

The pair agrees with the `ρ3` pair `26` versus `46` because the extra
unit-out-face clause is already priced by corridor-slide. That agreement
is a hop-cost identity on the six-neighbor graph, not a copied `ρ3`
table: the `uf` scores below are Dijkstra outputs under `uf`. On
`(1,1,0) → (2,1,0)` both `ρ3` and `uf` cost `3`, and the sixth predicate
is already priced. On `(2,2,0) → (3,2,0)` both `ρ3` and `uf` cost `1`,
so `uf` cannot price deep out-face. Independently, `t(3,2,0) = 9` under
`uf`. A cheapest `uf` walk to `(14,14,14)` uses no unit-out-face grow
beyond the corridor hop already in `ρ3`, so the body arrival stays `46`.
The site `(14,14,14)` has ℓ¹ norm `42`, so it is absent from `B_39(0)`.
The `B_42(0)` table is therefore not leftover of the `B_39(0)` times.

The rule is displayed, not adopted. Do not write `uf` into Admissibility.
Do not write uf into Admissibility. Do not attach L1.

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
unit-out-face source-max clause, and the arrival function `t` are
separately displayed mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_42(0) = { v ∈ Z^3 : |v|_1 ≤ 42 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_42(0)`,
`t(v)` is the least sum of `uf` along a directed path from `0` to `v` in
that graph.

The comparator `ρ3` uses only the first five clauses of `uf`. On the
unit-out-face hop `(1,1,0) → (2,1,0)` the sixth predicate holds and
corridor-slide already returns `3`, so `ρ3 = uf = 3`. On the deep-out-face
hop `(2,2,0) → (3,2,0)` the sixth predicate fails and `ρ3 = uf = 1`.
Therefore the extra named clause does not change any six-neighbor cost
relative to `ρ3`, and unit-out-face alone does not restore reverse at
`k=14`.

The deep-out-face comparator `df` uses the grow test with source max at
least `2`. On `(2,2,0) → (3,2,0)` one has `df = 3` while `uf = 1`. On
`(1,1,0) → (2,1,0)` the `uf` grow predicate holds and the `df` grow
predicate fails, while both final costs stay `3` by corridor-slide.
Those hop-cost comparisons use the named rules only; they are not a
second Dijkstra.

On the interior body hop `(14,14,1) → (14,14,2)` the hop is `3→3` with
only one absolute coordinate equal to `1`, so both `ρ3` and `uf` cost
`1`.

## Theorem 1 — Arrivals `t(14,0,0)` And `t(14,14,14)` On `B_42(0)`

One origin Dijkstra on `B_42(0)` returns the integer arrivals

| site | `t_uf` |
|---|---:|
| `(14,0,0)` | `26` |
| `(14,14,14)` | `46` |

Every listed site lies in `B_42(0)`. The site `(14,14,14)` has ℓ¹ norm `42`,
so it is absent from `B_39(0)`. The pair is computed on `B_42(0)`, not
copied from a smaller-ball table. These values are Dijkstra outputs, not
fitted scalars.

A witness axis walk of cost `26` is seed-exit `3` onto `(1,0,0)`,
leave-axis `1` onto `(1,1,0)`, unit-out-face / corridor-slide `3` onto
`(2,1,0)`, non-hugging face hop `1` onto `(2,2,0)`, twelve
support-preserving cost-`1` face hops to `(14,2,0)`, hugging slide `3`
onto `(14,1,0)`, and support-drop `3` onto `(14,0,0)`, summing to `26`.
That walk is a witness of cost `26`, not a uniqueness claim. The pure
axis 1-skeleton walk costs `42` and is not cheapest.

A witness body walk of cost `46` is the same prefix of cost `8` to
`(2,2,0)`, twelve cost-`1` face hops to `(14,2,0)`, twelve cost-`1` face
hops to `(14,14,0)`, enter-body `1` onto `(14,14,1)`, and thirteen
support-preserving cost-`1` body hops to `(14,14,14)`, summing to `46`.
Those last hops have dest with only one absolute coordinate equal to `1`,
or with all three coordinates large, so they are not unit-height ridges
and are not unit-out-face `2→2` grows. That walk is a witness of cost
`46`, not a uniqueness claim.

A witness that deep out-face is not taxed by `uf` is the walk seed-exit
`3` onto `(1,0,0)`, leave-axis `1` onto `(1,1,0)`, corridor-slide `3`
onto `(1,2,0)`, support-preserving `1` onto `(2,2,0)`, and dest-max grow
`1` onto `(3,2,0)`, summing to `9`. Independently, `t(3,2,0) = 9`.

## Theorem 2 — Reverse At The Same-`k` Scale `k=14`

The Euclidean-normalized comparison at `k=14` is

`t(14,0,0)^2 / 196  ?  t(14,14,14)^2 / 588`,

equivalently `3 t(14,0,0)^2 ? t(14,14,14)^2`. Substituting the computed times
gives `3 · 26^2 = 2028` and `46^2 = 2116`, so

`2028 > 2116` is false; `2028 < 2116`.

Arrival per Euclidean length is larger at `(14,14,14)` than at `(14,0,0)`.
Same-`k` reverse at `k=14` under `uf` is no. Unit-out-face alone does not
restore the `ρ3` failure at `k=14`. The comparison is displayed, not
adopted. The inequality does not hold.

## Theorem 3 — Displayed, Not Adopted

The rule `uf` is a displayed scoring device on `B_42(0)`. Do not write `uf`
into Admissibility. Do not write uf into Admissibility. Do not attach L1.
It is not a replacement for unit-cost first arrival, and it is not offered
as the unique hop-cost with same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_42(0) for one named hop-cost at k=14. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_42(0) for the displayed rule uf at k=14; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `uf` among hop-costs that score the same-`k` pair at `k=14`.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_42(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=14`.
- Any reuse of a `ρ3` arrival table as a substitute for the `uf` Dijkstra.
- That the extra unit-out-face clause changes a six-neighbor hop cost
  relative to `ρ3`. It does not; the named hop is already priced.
