---
claim_id: named_hopcost_face_diagonal_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Face-diagonal versus axis arrival order under the named hop-cost on B_6(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/named_hopcost_face_diagonal_b6_2026_08_15.py
---

# Face-Diagonal Versus Axis Arrival Order On B_6 Under The Named Hop-Cost

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one Dijkstra first-arrival table on the radius-6 integer ball
`B_6(0)` for the named equal-weight hop-cost `ρ`, restricted to the five
requested sites and three face-versus-axis ratio comparisons.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/named_hopcost_face_diagonal_b6_2026_08_15.py`](../scripts/named_hopcost_face_diagonal_b6_2026_08_15.py)

## Result Up Front

On the one-seed front, the inward occupancy weight `|σ_v|` of a site `v` is
the number of six-neighbors of `v` that are strictly closer to the seed in
cubic nearest-neighbor graph distance. Equivalently, `|σ_0|=0` and, for
`v ≠ 0`, `|σ_v|` equals the number of nonzero coordinates of `v`.

The named hop-cost `ρ` on a directed six-neighbor edge `v → w` that remains
inside `B_6(0)` is

```text
ρ(v → w) = 3  if |σ_v| = |σ_w| or |σ_v| = 0,
         = 1  otherwise.
```

This is the same local-in-weights rule used to name the eight inward-weight
orbits on the radius-3 ball (seed-exit and equal inward weight cost 3;
unequal inward weight cost 1). It is a displayed scoring rule. It is not
written into Admissibility. Do not attach L1.

`B_6(0)` is the 377-site set `{v ∈ Z^3 : |v|_1 ≤ 6}`. Arrival `t` is the
minimum `ρ`-path cost from the seed `0` through directed six-neighbor edges
that stay in `B_6(0)`. One Dijkstra computation on that finite directed
graph yields the exact integer times

```text
t(4,0,0)=12
t(6,0,0)=18
t(3,3,0)=16
t(4,2,0)=16
t(2,2,2)=14
```

For a nonzero site `v`, write `q(v) := t(v)^2 / |v|_2^2`. Reverse of the
diamond (ℓ¹) order on an ordered pair `(axis, more-diagonal)` means
`q(more-diagonal) < q(axis)`. The three requested pairs do **not** reverse:

| pair | `q` on the axis site | `q` on the more-diagonal site | reverse? |
|---|---|---|---|
| `((4,0,0),(3,3,0))` | `144/16 = 9` | `256/18 = 128/9` | no: `128/9 > 9` |
| `((4,0,0),(4,2,0))` | `144/16 = 9` | `256/20 = 64/5` | no: `64/5 > 9` |
| `((6,0,0),(3,3,0))` | `324/36 = 9` | `256/18 = 128/9` | no: `128/9 > 9` |

The body-diagonal time `t(2,2,2)=14` is reported only because it is among the
five requested sites. The face-versus-axis comparisons above are not a
restatement of that body-diagonal number.

The five times and the three non-reversals are displayed, not adopted.

## Exact Theorem

Let `B_6(0) := {v ∈ Z^3 : |v|_1 ≤ 6}`. Let `E` be the set of directed
six-neighbor edges `v → w` with both ends in `B_6(0)`. Let `|σ_v|` and `ρ`
be as above. Let `t(v)` be the minimum of `∑ ρ` over directed `E`-paths from
`(0,0,0)` to `v`.

**Theorem 1.** The arrival times on the five requested sites are
`t(4,0,0)=12`, `t(6,0,0)=18`, `t(3,3,0)=16`, `t(4,2,0)=16`, and
`t(2,2,2)=14`.

**Theorem 2.** For each pair
`((4,0,0),(3,3,0))`, `((4,0,0),(4,2,0))`, `((6,0,0),(3,3,0))`, the
more-diagonal site is the second entry. None of the three pairs reverses
diamond order: `128/9 > 9`, `64/5 > 9`, and `128/9 > 9` respectively.
Displayed, not adopted.

**Theorem 3.** Do not write `ρ` into Admissibility. Do not attach L1.

## Proof Sketch

The directed graph `(B_6(0), E)` is finite (377 vertices, at most six
outgoing edges each) and every edge cost is a positive integer in `{1,3}`.
Dijkstra's algorithm therefore returns the exact integer minimum-path
function `t`. The paired runner performs that single Dijkstra computation
and reads off the five sites.

The axis times are additionally visible on the unique coordinate-axis
geodesics. Each hop `(k,0,0) → (k+1,0,0)` for `k ≥ 0` is either seed-exit
(`k=0`) or equal inward weight `1 → 1` (`k ≥ 1`), hence has cost 3, so
`t(n,0,0) = 3n` is an explicit upper bound. Dijkstra matches it:
`t(4,0,0)=12` and `t(6,0,0)=18`.

The three ratio comparisons are exact rational arithmetic from those times
and the Euclidean squared lengths `| (4,0,0) |_2^2 = 16`,
`| (6,0,0) |_2^2 = 36`, `| (3,3,0) |_2^2 = 18`, and `| (4,2,0) |_2^2 = 20`.

The eight inward-weight pairs that already appear on the radius-3 ball are
`(0,1)`, `(1,0)`, `(1,1)`, `(1,2)`, `(2,1)`, `(2,2)`, `(2,3)`, `(3,2)`.
Evaluating `ρ` on those pairs recovers the eight-tuple `(3,1,3,1,1,3,1,1)`.
The pair `(3,3)` that first appears on a larger ball also has equal inward
weight, so `ρ(3,3)=3`. Those identities identify the displayed rule; they
are not a new axiom clause.

## Framework Boundary

The Lattice axiom supplies the cubic lattice `Z^3` and nearest-neighbor
adjacency. Admissibility supplies one fixed nearest-neighbor admissibility
rule and says that, for each site, the probability distribution over the
possibilities is determined by, and varies with, the nearest-neighbor
conditions. Neither clause names a hop-cost, an arrival time, or a
comparison of `t^2 / |v|_2^2` across site types.

This note therefore treats `ρ` as a separately named scoring rule on
inward-weight pairs. Theorem 3 forbids writing `ρ` into Admissibility.
The diamond (ℓ¹) order is used only as the comparison baseline requested
by the three pairs. Do not attach L1.

No Euclidean spacetime metric, clock map, or continuum null cone is adopted.
The quantity `|v|_2^2` is the ordinary integer sum of squares of the three
coordinates, used only to form the displayed ratio `q(v)`.

## Imports And Claim Boundary

| Item | Role | Provenance / status |
|---|---|---|
| cubic lattice `Z^3` and six-neighbor adjacency | ambient graph | Lattice axiom |
| nearest-neighbor condition domain | identification only; no kernel values used | Admissibility axiom |
| inward weight `|σ_v|` | one-seed front labeling | declared from the six-neighbor graph |
| hop-cost `ρ` | displayed scoring rule | named equal-weight / seed-exit clause; not an axiom |
| `B_6(0)` | declared finite ball | 377 sites with `|v|_1 ≤ 6` |
| `t` | minimum path cost | one Dijkstra on the induced directed graph |
| reverse | `q(more-diagonal) < q(axis)` | displayed comparison, not adopted |

There are no measured, fitted, literature, or observational inputs. The
rule `ρ` is not unique among maps `{1,3}` on inward-weight pairs, and no
uniqueness claim is made. Face-diagonal versus axis arrival order under
this displayed rule is the entire scientific content.

## Machine Status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_6(0) closes the five integer arrival times and the three exact rational face-versus-axis comparisons; the hop-cost is displayed, not adopted, and is not written into Admissibility."
trace_class: upstream_support
target_claim_id: named_hopcost_face_diagonal_b6_bounded_theorem_note_2026-08-15
target_blocker_text: "name a hop-cost that is retained-derived rather than displayed, if any later lane requires one"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep ρ displayed. Do not write it into Admissibility. Do not attach L1. Use the three non-reversals as the face-diagonal residual, not as a restatement of t(2,2,2)."
conditional_surface_status: "exact on B_6(0) for the named hop-cost; not adopted"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Primary Runner

The paired runner builds `B_6(0)`, assigns `ρ` from inward weights, runs
one Dijkstra computation from the seed, reports the five times and three
ratio comparisons, and checks agreement with this note. It writes no
runner cache.
