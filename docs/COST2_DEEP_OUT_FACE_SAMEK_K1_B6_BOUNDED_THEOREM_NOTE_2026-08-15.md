---
claim_id: cost2_deep_out_face_samek_k1_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=1 under the named cost-2 deep-out-face hop-cost on B_6(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost2_deep_out_face_samek_k1_b6_2026_08_15.py
---

# Named Cost-2 Deep-Out-Face Same-`k` Reverse At `k=1` On `B_6(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_6(0)`,
scored only for the same-`k` pair `t(1,0,0)` versus `t(1,1,1)`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/cost2_deep_out_face_samek_k1_b6_2026_08_15.py`](../scripts/cost2_deep_out_face_samek_k1_b6_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_6(0)`, the stacked
rules `ν`, `μ`, and `ρ3` are those of the ridge-slide same-`k` scoring:

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
`|w_i|` equals `1)`, else `1`;

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

The displayed cost-2 deep-out-face rule `c2df` is `ρ3` plus cost `2` (not
`3`) on a `2→2` hop whose destination max grows and whose source max is at
least `2`:

`c2df(v→w) = 3` if `ρ3` would be `3`, else `2` if (`|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 2`), else `1`.

Those clauses are the whole rule. Uniqueness is not claimed. This note is
the first display of `c2df`. The parent deep-out-face rule `df` uses the
same extra hop at cost `3`. The all-out-face cost-`2` rule taxes every
`2→2` dest-max growth; `c2df` taxes only the deep case `max |v_i| ≥ 2`.

The extra clause fires, for example, on `(2,2,0) → (3,2,0)` and not on the
unit-face hop `(1,1,0) → (2,1,0)`. The latter already has `ρ3 = 3` because
the destination still has a unit coordinate.

One Dijkstra from the origin on `B_6(0)` (377 sites; 376 nonzero) returns

| site | `t_c2df` |
|---|---:|
| `(1,0,0)` | `3` |
| `(1,1,1)` | `5` |

The same-`k` comparison at `k=1` is

`t(1,0,0)^2 / 1  ?  t(1,1,1)^2 / 3`,

equivalently `3 t(1,0,0)^2 ? t(1,1,1)^2`. Substituting the computed times
gives `9 > 25/3`, or `27 > 25`. Same-`k` reverse at `k=1` is yes.

The `k=1` geodesic `0 → (1,0,0) → (1,1,0) → (1,1,1)` uses `c2df` costs
`3,1,1` and never takes a deep-out-face hop. Independently, `c2df` is not leftover of `ρ3` or of `df`: the interior deep-out-face hop
`(2,2,0) → (3,2,0)` has `ρ3=1`, `df=3`, and `c2df=2`. Both ends lie in
`B_6(0)`. The ball is scored independently: one origin Dijkstra is run on
this ball, not leftover of a larger-ball table.

The rule is displayed, not adopted. Do not write c2df into Admissibility.
Do not write `c2df` into Admissibility. Do not attach L1.

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
max-coordinate clauses, and the arrival function `t` are separately displayed
mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_6(0) = { v ∈ Z^3 : |v|_1 ≤ 6 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_6(0)`,
`t(v)` is the least sum of `c2df` along a directed path from `0` to `v` in
that graph.

The first `ν` clause is seed-exit. The second is both weights `1`. The third
is support drop. The `μ` addendum taxes a `2→2` hop whose destination still
touches a unit coordinate. The `ρ3` addendum taxes a `3→3` hop whose
destination has exactly two unit coordinates. The `c2df` addendum prices a
deep `2→2` face-growth hop at `2` rather than leaving it at `1` or raising
it to `3`.

An explicit axis path is the single hop `(0,0,0) → (1,0,0)` of cost `3`.
An explicit body path is

```text
(0,0,0) → (1,0,0) → (1,1,0) → (1,1,1)
```

with costs `3+1+1=5`. Every path has first hop cost `3`, and every hop costs
at least `1`, so these paths are optimal once Dijkstra matches them.

## Theorem 1 — Arrivals At `k=1` Under `c2df`

One origin Dijkstra on `B_6(0)` returns

```text
t(1,0,0) = 3
t(1,1,1) = 5
```

Both sites lie in `B_6(0)`. These values are Dijkstra outputs, not fitted
scalars.

## Theorem 2 — Reverse At The Same-`k` Pair `k=1`

The displayed comparison is whether

```text
t(1,0,0)^2 / 1 > t(1,1,1)^2 / 3.
```

Substituting the computed times gives `9 > 25/3`, or equivalently
`27 > 25`. Arrival per Euclidean length is larger at `(1,0,0)` than at
`(1,1,1)`. Same-k reverse holds at k=1. The comparison is displayed, not
adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `c2df` is a displayed scoring device on `B_6(0)`. Do not write c2df
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the only hop-cost with
same-`k` reverse.

The live Admissibility wording names one fixed nearest-neighbor
admissibility rule and does not name `c2df`, `df`, `ρ3`, `μ`, or `ν`. This
note proposes no axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_6(0) for one named hop-cost at k=1. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_6(0) for the displayed rule c2df at k=1; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `c2df` among hop-costs that reverse any same-`k` pair.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_6(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=1`.
- Any adoption of `c2df` as an admissibility rule.
- Any reuse of a larger-ball arrival table as a substitute for the
  radius-`6` Dijkstra.
