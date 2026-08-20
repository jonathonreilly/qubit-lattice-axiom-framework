---
claim_id: out_face_samek_k1_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=1 under the named out-face hop-cost on B_6(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/out_face_samek_k1_b6_2026_08_15.py
---

# Named Out-Face Same-`k` Reverse At `k=1` On `B_6(0)`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_6(0)`,
scored only for the same-`k` pair `t(1,0,0)` versus `t(1,1,1)`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/out_face_samek_k1_b6_2026_08_15.py`](../scripts/out_face_samek_k1_b6_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_6(0)`, the stacked
rules `ν`, `μ`, and `ρ3` are

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
`|w_i|` equals `1)`, else `1`;

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`.

The displayed out-face rule `ω` is `ρ3` plus cost `3` on a `2→2` hop whose
destination has a larger max absolute coordinate than the source:

`ω(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=|σ_w|=2` and
`max_i |w_i| > max_i |v_i|)`, else `1`.

Those clauses are the whole rule. Uniqueness is not claimed. This note is
the first display of `ω`.

A mid-leave clause that would cost `3` on a `1→2` hop with destination max
absolute coordinate `1` and source max at least `2` cannot fire on the
six-neighbor graph: a cubic step never realizes both of those max conditions
together with `|σ_v|=1` and `|σ_w|=2`. The out-face hop
`(1,1,0) → (2,1,0)` does fire: `|σ|=2→2` and `max |w_i|=2 > max |v_i|=1`,
so `ω=3`.

One Dijkstra from the origin on `B_6(0)` (377 sites; 376 nonzero) returns

| site | `t_ω` |
|---|---:|
| `(1,0,0)` | `3` |
| `(1,1,1)` | `5` |

The same-`k` comparison at `k=1` is

`t(1,0,0)^2 / 1  ?  t(1,1,1)^2 / 3`,

equivalently `3 t(1,0,0)^2 ? t(1,1,1)^2`. Substituting the computed times
gives `27 > 25`. Same-`k` reverse at `k=1` is yes.

The `k=1` geodesic `0 → (1,0,0) → (1,1,0) → (1,1,1)` uses `ω` costs
`3,1,1` and never takes a `2→2` face-growth hop. Independently, `ω` is not
leftover of `ρ3`: the interior face-growth hop `(2,2,0) → (3,2,0)` has
`ρ3=1` and `ω=3`.

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
none of the hop costs. The integers `3` and `1`, the support-size and
max-coordinate clauses, and the arrival function `t` are separately displayed
mathematical inputs. No axiom text is edited.

## Named Rule

Let `B_6(0) = { v ∈ Z^3 : |v|_1 ≤ 6 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_6(0)`,
`t(v)` is the least sum of `ω` along a directed path from `0` to `v` in
that graph.

The first `ν` clause is seed-exit. The second is both weights `1`. The third
is support drop. The `μ` addendum taxes a `2→2` hop whose destination still
touches a unit coordinate. The `ρ3` addendum taxes a `3→3` hop whose
destination has exactly two unit coordinates. The `ω` addendum taxes a
`2→2` hop that grows the coordinate box on a face.

## Theorem 1 — Arrivals At `k=1` Under `ω`

One origin Dijkstra on `B_6(0)` returns `t(1,0,0) = 3` and `t(1,1,1) = 5`.
Both sites lie in `B_6(0)`. These values are Dijkstra outputs, not fitted
scalars.

## Theorem 2 — Reverse At The Same-`k` Pair `k=1`

The Euclidean-normalized comparison at `k=1` is

`t(1,0,0)^2 / 1  ?  t(1,1,1)^2 / 3`.

The computed integers give `27 > 25`. Arrival per Euclidean length is larger
at `(1,0,0)` than at `(1,1,1)`. The comparison is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ω` is a displayed scoring device on `B_6(0)`. Do not write `ω`
into Admissibility. Do not attach L1. It is not a replacement for
unit-cost first arrival, and it is not offered as the unique hop-cost with
same-`k` reverse.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer same-k arrivals and reverse comparison on the finite ball B_6(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_6(0) for the displayed rule ω at k=1; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ω` among hop-costs that reverse any same-`k` pair.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_6(0)`.
- Any score for a pair that is not the same-`k` axis / body-diagonal pair
  at `k=1`.
- Any adoption of `ω` as an admissibility rule.
