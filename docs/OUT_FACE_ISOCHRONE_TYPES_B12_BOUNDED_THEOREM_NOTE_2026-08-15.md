---
claim_id: out_face_isochrone_types_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Isochrone type counts of the t(2,2,2) and t(4,4,4) shells under the named out-face hop-cost on B_12(0) are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/out_face_isochrone_types_b12_2026_08_15.py
---

# Named Out-Face Isochrone Type Counts Of The t(2,2,2) And t(4,4,4) Shells On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_12(0)`,
scored only for G+ type counts and distinct `|v|_2^2` on the arrivals
`t(2,2,2)` and `t(4,4,4)` under out-face.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/out_face_isochrone_types_b12_2026_08_15.py`](../scripts/out_face_isochrone_types_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The investment is that the displayed out-face rule `ω` holds through
`k=15` and is rounder than the ridge-enter rule `κ`. The residual here
is the first display of the isochrone type counts of the `t(2,2,2)` and
`t(4,4,4)` shells under `ω` on `B_12(0)`. Uniqueness is not claimed.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_12(0)`, the stacked
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

Those clauses are the whole rule. The extra clause is an out-face hop:
both ends have support `2`, and the destination grows the coordinate box
on a face. The named out-face hop `(1,1,0) → (2,1,0)` fires: `|σ|=2→2`
and `max |w_i|=2 > max |v_i|=1`, so `ω=3`. Independently, `ω` is not
leftover of `ρ3` or of `κ`: the interior face-growth hop
`(2,2,0) → (3,2,0)` has `ρ3=1`, `κ=1`, and `ω=3`. The ridge-enter hop
`(2,1,0) → (2,1,1)` has `ω=1` while `κ=3`. Therefore neither `ρ3` nor
`κ` can price out-face.

The proper cubic group `G+` is the 24 signed-permutation rotations of
determinant `+1`. A G+ type is one `G+` orbit. The representative of an
orbit is its lexicographically maximal first-octant triple (the
lex-sorted list of those abs-sorted 3-tuples is the type list).

One Dijkstra from the origin on `B_12(0)` (2625 sites; 2624 nonzero) gives

`t(2,2,2) = 10`, `t(4,4,4) = 16`.

| `t` | site count | G+ types | distinct `|v|_2^2` |
|---:|---:|---:|---:|
| `10` | `80` | `4` | `3` |
| `16` | `524` | `23` | `14` |

So the `t(2,2,2)` and `t(4,4,4)` shells remain mixed. Versus the `κ`
counts `6/5` on the `t=10` shell and `25/13` on the `t=16` shell, the
pair on `t=10` is `4/3` and the pair on `t=16` is `23/14`. The type
counts do not stay.

The body diagonal `(2,2,2)` sits in the `t=10` shell. The doubled body
diagonal `(4,4,4)` sits in the `t=16` shell.

The census is displayed, not adopted. Do not write `ω` into Admissibility.
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

## Named Rule And Type Convention

Let `B_12(0) = { v ∈ Z^3 : |v|_1 ≤ 12 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_12(0)`,
`t(v)` is the least sum of `ω` along a directed path from `0` to `v` in
that graph.

The first `ν` clause is seed-exit. The second is both weights `1`. The third
is support drop. The `μ` addendum taxes a `2→2` hop whose destination still
touches a unit coordinate. The `ρ3` addendum taxes a `3→3` hop whose
destination has exactly two unit coordinates. The `ω` addendum taxes a
`2→2` hop that grows the coordinate box on a face.

On the interior face-growth hop `(2,2,0) → (3,2,0)` one has `|σ|=2→2` and
`max |w_i|=3 > max |v_i|=2`, so `ρ3 = 1` and `κ = 1` while `ω = 3`.
Therefore `ρ3` cannot price out-face, and `κ` cannot price out-face. On
the ridge-enter hop `(2,1,0) → (2,1,1)` one has `|σ|: 2 → 3` and exactly
two `|w_i|=1`, so `ω = 1` while `κ = 3`. On the interior `3→3` hop
`(2,2,2) → (3,2,2)` the destination has no unit coordinate, so `ω` costs
`1`.

A G+ type is represented by the lexicographically maximal first-octant
member of its orbit. The type list of a shell is those representatives
sorted in lexicographic order. Absolute-coordinate first-octant form does
not merge chiral pairs: `(3,1,2)` and `(3,2,1)` remain distinct `G+`
orbits, as do the chiral pairs on the `t=16` shell.

## Theorem 1 — Type Counts On The `t(2,2,2)` And `t(4,4,4)` Shells

Let `t2 = t(2,2,2)` and `t4 = t(4,4,4)` under `ω`. One origin Dijkstra
on `B_12(0)` reaches every site and returns `t2 = 10` and `t4 = 16`. The
`t=10` shell has 80 sites, 4 G+ types, and 3 distinct values of
`|v|_2^2`. The `t=16` shell has 524 sites, 23 G+ types, and 14 distinct
values of `|v|_2^2`.

The lex-sorted abs-sorted G+ representatives at `t=10`, each with
`|v|_2^2` and orbit size, are

| representative | `|v|_2^2` | orbit size |
|---|---:|---:|
| `(2,2,2)` | 12 | 8 |
| `(3,1,0)` | 10 | 24 |
| `(3,1,2)` | 14 | 24 |
| `(3,2,1)` | 14 | 24 |

Those four orbits partition the 80 sites. The three squared radii are
`{10,12,14}`.

The lex-sorted abs-sorted G+ representatives at `t=16` are

| representative | `|v|_2^2` | orbit size |
|---|---:|---:|
| `(4,4,0)` | 32 | 12 |
| `(4,4,4)` | 48 | 8 |
| `(5,1,0)` | 26 | 24 |
| `(5,3,0)` | 34 | 24 |
| `(5,3,4)` | 50 | 24 |
| `(5,4,3)` | 50 | 24 |
| `(5,5,2)` | 54 | 24 |
| `(6,1,1)` | 38 | 24 |
| `(6,1,5)` | 62 | 24 |
| `(6,2,0)` | 40 | 24 |
| `(6,2,4)` | 56 | 24 |
| `(6,3,3)` | 54 | 24 |
| `(6,4,2)` | 56 | 24 |
| `(6,5,1)` | 62 | 24 |
| `(7,1,4)` | 66 | 24 |
| `(7,2,3)` | 62 | 24 |
| `(7,3,2)` | 62 | 24 |
| `(7,4,1)` | 66 | 24 |
| `(8,1,3)` | 74 | 24 |
| `(8,2,2)` | 72 | 24 |
| `(8,3,1)` | 74 | 24 |
| `(9,1,2)` | 86 | 24 |
| `(9,2,1)` | 86 | 24 |

Those twenty-three orbits partition the 524 sites. The fourteen squared
radii are `{26,32,34,38,40,48,50,54,56,62,66,72,74,86}`.

Versus the `κ` counts `6/5` and `25/13` on the `t=10` and `t=16` shells,
the `ω` pair on the `t(2,2,2)` and `t(4,4,4)` shells is `4/3` and
`23/14`. The type counts do not stay. That mismatch is a Dijkstra output
on this ball, not a reuse of the `κ` type table.

B_12(0) only. The type counts are displayed, not adopted.

## Theorem 2 — Body-Diagonal Membership Of `(2,2,2)`

The same Dijkstra gives `t(2,2,2) = 10` and `t(4,4,4) = 16`. So
`(2,2,2)` is in the `t=10` type list and `(4,4,4)` is in the `t=16`
type list.

A body-diagonal site is a nonzero site with `|x|=|y|=|z|`. The `t=10`
shell contains exactly the eight signed copies of `(2,2,2)` as
body-diagonal sites. No other body-diagonal type appears: `(1,1,1)`
arrives at `5` and `(3,3,3)` arrives at `13`. So `(2,2,2)` is the unique body-diagonal G+ type in its shell.

That uniqueness is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ω` is a displayed scoring device on `B_12(0)`. Do not write `ω`
into Admissibility. Do not attach L1. The isochrone type counts are not
offered as a unique hop-cost property and are not a replacement for
unit-cost first arrival.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact G+ type counts on the t(2,2,2) and t(4,4,4) shells of B_12(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_12(0) for the displayed rule ω; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ω` among hop-costs with these type counts.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_12(0)`.
- Any reuse of the `κ` type table as a substitute for the `ω` Dijkstra.
- Adoption of body-diagonal uniqueness in the `t=10` shell as a hop-cost
  selector.
