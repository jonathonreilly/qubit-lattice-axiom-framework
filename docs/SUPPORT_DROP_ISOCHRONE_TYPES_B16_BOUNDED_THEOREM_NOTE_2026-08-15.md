---
claim_id: support_drop_isochrone_types_b16_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Isochrone type counts of the t=8 and t=14 shells under the named support-drop hop-cost on B_16(0) are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_isochrone_types_b16_2026_08_15.py
---

# Isochrone Type Counts Of The t=8 And t=14 Shells On B_16(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_16(0)`,
scored only for G+ type counts and distinct `|v|_2^2` on the mixed arrivals
`t=8` and `t=14`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_isochrone_types_b16_2026_08_15.py`](../scripts/support_drop_isochrone_types_b16_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

The mixed-shell census on `B_16(0)` placed both `t=8` and `t=14` among the
mixed arrivals. That mixed bit is the investment, not the residual. The
residual here is the G+ type count and the number of distinct Euclidean
squared radii on those two shells, versus the `B_12(0)` counts `7/5` and
`26/15`.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_16(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not claimed.

The proper cubic group `G+` is the 24 signed-permutation rotations of
determinant `+1`. A G+ type is one `G+` orbit. The representative of an
orbit is its lexicographically maximal first-octant triple (the
lex-sorted list of those abs-sorted 3-tuples is the type list).

One Dijkstra from the origin on `B_16(0)` (6017 sites; 6016 nonzero) gives

| `t` | site count | G+ types | distinct `|v|_2^2` |
|---:|---:|---:|---:|
| `8` | `140` | `7` | `5` |
| `14` | `578` | `26` | `15` |

So `t=8` and `t=14` stay mixed. Versus the `B_12(0)` counts, the pair on
`t=8` is still `7/5` and the pair on `t=14` is still `26/15`. The
numerical coincidence is not leftover of the `B_12(0)` type table: one
origin Dijkstra is run on this ball, and the site `(16,0,0)` is not in `B_12(0)`.

The reverse-critical body diagonal `(2,2,2)` sits in the `t=8` shell.
The doubled body diagonal `(4,4,4)` and the axis site `(8,0,0)` sit in
the `t=14` shell.

The census is displayed, not adopted. Do not write `ν` into Admissibility.
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
and the arrival function `t` are separately displayed mathematical inputs.
No axiom text is edited.

## Named Rule And Type Convention

Let `B_16(0) = { v ∈ Z^3 : |v|_1 ≤ 16 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_16(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph.

A G+ type is represented by the lexicographically maximal first-octant
member of its orbit. The type list of a shell is those representatives
sorted in lexicographic order. Absolute-coordinate first-octant form does
not merge chiral pairs: `(3,1,2)` and `(3,2,1)` remain distinct `G+`
orbits, as do the chiral pairs on `t=14`.

## Theorem 1 — Type Counts On The `t=8` And `t=14` Shells

One origin Dijkstra on `B_16(0)` reaches every site. The `t=8` shell has
140 sites, 7 G+ types, and 5 distinct values of `|v|_2^2`. The `t=14`
shell has 578 sites, 26 G+ types, and 15 distinct values of `|v|_2^2`.

The lex-sorted abs-sorted G+ representatives at `t=8`, each with
`|v|_2^2` and orbit size, are

| representative | `|v|_2^2` | orbit size |
|---|---:|---:|
| `(2,2,2)` | 12 | 8 |
| `(3,1,2)` | 14 | 24 |
| `(3,2,1)` | 14 | 24 |
| `(3,3,0)` | 18 | 12 |
| `(4,1,1)` | 18 | 24 |
| `(4,2,0)` | 20 | 24 |
| `(5,1,0)` | 26 | 24 |

Those seven orbits partition the 140 sites. The five squared radii are
`{12,14,18,20,26}`.

The lex-sorted abs-sorted G+ representatives at `t=14` are

| representative | `|v|_2^2` | orbit size |
|---|---:|---:|
| `(4,4,4)` | 48 | 8 |
| `(5,3,4)` | 50 | 24 |
| `(5,4,3)` | 50 | 24 |
| `(5,5,2)` | 54 | 24 |
| `(6,1,5)` | 62 | 24 |
| `(6,2,4)` | 56 | 24 |
| `(6,3,3)` | 54 | 24 |
| `(6,4,2)` | 56 | 24 |
| `(6,5,1)` | 62 | 24 |
| `(6,6,0)` | 72 | 12 |
| `(7,1,4)` | 66 | 24 |
| `(7,2,3)` | 62 | 24 |
| `(7,3,2)` | 62 | 24 |
| `(7,4,1)` | 66 | 24 |
| `(7,5,0)` | 74 | 24 |
| `(8,0,0)` | 64 | 6 |
| `(8,1,3)` | 74 | 24 |
| `(8,2,2)` | 72 | 24 |
| `(8,3,1)` | 74 | 24 |
| `(8,4,0)` | 80 | 24 |
| `(9,1,2)` | 86 | 24 |
| `(9,2,1)` | 86 | 24 |
| `(9,3,0)` | 90 | 24 |
| `(10,1,1)` | 102 | 24 |
| `(10,2,0)` | 104 | 24 |
| `(11,1,0)` | 122 | 24 |

Those twenty-six orbits partition the 578 sites. The fifteen squared
radii are `{48,50,54,56,62,64,66,72,74,80,86,90,102,104,122}`.

Versus the `B_12(0)` counts `7/5` and `26/15`, the `B_16(0)` pair is the
same on both shells. That match is a Dijkstra output on this ball, not a
reuse of the smaller-ball type table.

B_16(0) only. The type counts are displayed, not adopted.

## Theorem 2 — Named Sites Sit In Those Shells

The same Dijkstra gives `t(2,2,2) = 8`, `t(4,4,4) = 14`, and
`t(8,0,0) = 14`. So `(2,2,2)` is in the `t=8` type list, and both
`(4,4,4)` and `(8,0,0)` are in the `t=14` type list.

Those three memberships are displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_16(0)`. Do not write `ν`
into Admissibility. Do not attach L1. The isochrone type counts are not
offered as a unique hop-cost property and are not a replacement for
unit-cost first arrival.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact G+ type counts on the t=8 and t=14 shells of B_16(0) for one named hop-cost. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_16(0) for the displayed rule ν; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ν` among hop-costs with these type counts.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_16(0)`.
- Any reuse of the `B_12(0)` type table as a substitute for the radius-`16`
  Dijkstra.
