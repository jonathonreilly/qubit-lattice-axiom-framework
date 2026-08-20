---
claim_id: ridge_enter_isochrone_types_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Isochrone type counts of the t(2,2,2) and t(4,4,4) shells under the named ridge-enter hop-cost on B_12(0) are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ridge_enter_isochrone_types_b12_2026_08_15.py
---

# Isochrone Type Counts Of The t(2,2,2) And t(4,4,4) Shells On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_12(0)`,
scored only for G+ type counts and distinct `|v|_2^2` on the arrivals
`t(2,2,2)` and `t(4,4,4)` under ridge-enter.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/ridge_enter_isochrone_types_b12_2026_08_15.py`](../scripts/ridge_enter_isochrone_types_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The residual here is the first display of the isochrone type counts of
the `t(2,2,2)` and `t(4,4,4)` shells under the named ridge-enter hop-cost
`κ` on `B_12(0)`.

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_12(0)`, the displayed
comparator `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The displayed comparator `μ` is

`μ(v→w) = 3` if `ν(v→w)` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`.

The displayed comparator `ρ3` is

`ρ3(v→w) = 3` if `μ(v→w)` would be `3` or `(|σ_v|=|σ_w|=3` and exactly
two `|w_i|` equal `1)`, else `1`.

The displayed rule `κ` is

`κ(v→w) = 3` if `ρ3(v→w)` would be `3` or `(|σ_v|=2` and `|σ_w|=3` and
exactly two `|w_i|` equal `1)`, else `1`.

The extra clause is a ridge enter: support rises `2 → 3`, and the
destination has exactly two unit coordinates. It is not the displayed
body last hop into `(1,1,1)`, whose destination has three unit
coordinates. Those clauses are the whole rule. Uniqueness is not claimed.

The proper cubic group `G+` is the 24 signed-permutation rotations of
determinant `+1`. A G+ type is one `G+` orbit. The representative of an
orbit is its lexicographically maximal first-octant triple (the
lex-sorted list of those abs-sorted 3-tuples is the type list).

One Dijkstra from the origin on `B_12(0)` (2625 sites; 2624 nonzero) gives

`t(2,2,2) = 10`, `t(4,4,4) = 16`.

| `t` | site count | G+ types | distinct `|v|_2^2` |
|---:|---:|---:|---:|
| `10` | `116` | `6` | `5` |
| `16` | `572` | `25` | `13` |

So the `t(2,2,2)` and `t(4,4,4)` shells remain mixed.

The body diagonal `(2,2,2)` sits in the `t=10` shell. The doubled body
diagonal `(4,4,4)` sits in the `t=16` shell.

The pair is not leftover of `ρ3`: on the ridge-enter hop
`(2,1,0) → (2,1,1)` one has `|σ| : 2 → 3` and exactly two `|w_i| = 1`,
so `ρ3 = 1` while `κ = 3`. On the displayed body last hop
`(1,1,0) → (1,1,1)` the destination has three unit coordinates, so both
`ρ3` and `κ` cost `1`. On the ridge slide `(1,1,1) → (2,1,1)` both
already cost `3`. On the interior `3→3` hop `(2,2,2) → (3,2,2)` the
destination has no unit coordinate, so both cost `1`. Therefore `ρ3`
cannot price the ridge enter, and the `κ` type table is not a leftover
of a `ρ3` hop-cost identity.

The census is displayed, not adopted. Do not write κ into Admissibility.
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
the unit-coordinate test, and the arrival function `t` are separately
displayed mathematical inputs. No axiom text is edited.

## Named Rule And Type Convention

Let `B_12(0) = { v ∈ Z^3 : |v|_1 ≤ 12 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_12(0)`,
`t(v)` is the least sum of `κ` along a directed path from `0` to `v` in
that graph.

The comparator `ρ3` uses the support-drop clauses, the axis-hugging
`2→2` slide, and the ridge `3→3` slide. On the ridge-enter hop
`(2,1,0) → (2,1,1)` one has `|σ_v|=2`, `|σ_w|=3` and exactly two
`|w_i|=1`, so `ρ3 = 1` while `κ = 3`. Therefore `ρ3` cannot price the
ridge enter. On the displayed body last hop `(1,1,0) → (1,1,1)` the
destination has three unit coordinates, so the extra clause does not
fire and both costs stay `1`.

A G+ type is represented by the lexicographically maximal first-octant
member of its orbit. The type list of a shell is those representatives
sorted in lexicographic order. Absolute-coordinate first-octant form
does not merge chiral pairs: `(3,1,2)` and `(3,2,1)` remain distinct `G+`
orbits, as do the chiral pairs on the `t=16` shell.

## Theorem 1 — Type Counts On The `t(2,2,2)` And `t(4,4,4)` Shells

Let `t2 = t(2,2,2)` and `t4 = t(4,4,4)` under `κ`. One origin Dijkstra
on `B_12(0)` reaches every site and returns `t2 = 10` and `t4 = 16`. The
`t=10` shell has 116 sites, 6 G+ types, and 5 distinct values of
`|v|_2^2`. The `t=16` shell has 572 sites, 25 G+ types, and 13 distinct
values of `|v|_2^2`.

The lex-sorted abs-sorted G+ representatives at `t=10`, each with
`|v|_2^2` and orbit size, are

| representative | `|v|_2^2` | orbit size |
|---|---:|---:|
| `(2,2,2)` | 12 | 8 |
| `(3,1,0)` | 10 | 24 |
| `(3,1,2)` | 14 | 24 |
| `(3,2,1)` | 14 | 24 |
| `(3,3,0)` | 18 | 12 |
| `(4,2,0)` | 20 | 24 |

Those six orbits partition the 116 sites. The five squared radii are
`{10,12,14,18,20}`.

The lex-sorted abs-sorted G+ representatives at `t=16` are

| representative | `|v|_2^2` | orbit size |
|---|---:|---:|
| `(4,4,4)` | 48 | 8 |
| `(5,3,4)` | 50 | 24 |
| `(5,4,3)` | 50 | 24 |
| `(5,5,2)` | 54 | 24 |
| `(6,1,1)` | 38 | 24 |
| `(6,1,5)` | 62 | 24 |
| `(6,2,4)` | 56 | 24 |
| `(6,3,3)` | 54 | 24 |
| `(6,4,2)` | 56 | 24 |
| `(6,5,1)` | 62 | 24 |
| `(6,6,0)` | 72 | 12 |
| `(7,1,0)` | 50 | 24 |
| `(7,1,4)` | 66 | 24 |
| `(7,2,3)` | 62 | 24 |
| `(7,3,2)` | 62 | 24 |
| `(7,4,1)` | 66 | 24 |
| `(7,5,0)` | 74 | 24 |
| `(8,1,3)` | 74 | 24 |
| `(8,2,2)` | 72 | 24 |
| `(8,3,1)` | 74 | 24 |
| `(8,4,0)` | 80 | 24 |
| `(9,1,2)` | 86 | 24 |
| `(9,2,1)` | 86 | 24 |
| `(9,3,0)` | 90 | 24 |
| `(10,2,0)` | 104 | 24 |

Those twenty-five orbits partition the 572 sites. The thirteen squared
radii are `{38,48,50,54,56,62,66,72,74,80,86,90,104}`.

B_12(0) only. The type counts are displayed, not adopted.

## Theorem 2 — Body-Diagonal Membership Of `(2,2,2)`

The same Dijkstra gives `t(2,2,2) = 10` and `t(4,4,4) = 16`. So
`(2,2,2)` is in the `t=10` type list and `(4,4,4)` is in the `t=16`
type list.

A body-diagonal site is a nonzero site with `|x|=|y|=|z|`. The `t=10`
shell contains exactly the eight signed copies of `(2,2,2)` as
body-diagonal sites. No other body-diagonal type appears: `(1,1,1)`
arrives at `5` and `(3,3,3)` arrives at `13`. So `(2,2,2)` is the unique
body-diagonal G+ type in its shell.

That uniqueness is displayed, not adopted.

## Theorem 3 — Displayed, Not Adopted

The rule `κ` is a displayed scoring device on `B_12(0)`. Do not write κ
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
conditional_surface_status: "exact on B_12(0) for the displayed rule κ; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentence supplies nearest-neighbor
  adjacency on `Z^3`. It is quoted without rewrite. The hop-cost `κ` is not
  Lattice content.
- **Explicit theorem-domain condition:** the finite set `B_12(0)`, its
  nearest-neighbor edges, and the named directed costs `ν`, `μ`, `ρ3`, and
  `κ` are supplied mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** writing `κ` into Admissibility, selecting it as
  a physical cost, or lifting the census off `B_12(0)` remain separate
  obligations. This note does not close them.

## Exact Objects

All runner values are integers. No float is used in the comparison.

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The live Admissibility sentence, quoted and not rewritten:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

`κ` is a separately named hop-cost on directed nearest-neighbor hops. It is
not that admissibility rule.

Write `t(v)` for the Dijkstra arrival cost from the origin to `v` under
`κ`, using one Dijkstra on `B_12(0)`.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

Their dependency role is limited to the repository's site graph and the
refusal to treat a named hop-cost as axiom content.

## What This Note Does Not Claim

- Uniqueness of `κ` among hop-costs with these type counts.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_12(0)`.
- Any reuse of a `ρ3` type table as a substitute for the `κ` Dijkstra.
- Adoption of body-diagonal uniqueness in the `t=10` shell as a hop-cost
  selector.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Runner Contract

The companion runner builds `B_12(0)`, evaluates the named hop-cost, and
runs one Dijkstra from the origin. It reports site count, G+ type count,
and the number of distinct `|v|_2^2` on the `t(2,2,2)` and `t(4,4,4)`
shells, checks that `(2,2,2)` is the unique body-diagonal type in its
shell, checks that the extra `2→3` clause is live on in-host hops and
does not tax the displayed body last hop, checks that the live
Admissibility wording does not name `κ`, and records the import
boundary. Declared review inputs are this note and the axiom memo only.
