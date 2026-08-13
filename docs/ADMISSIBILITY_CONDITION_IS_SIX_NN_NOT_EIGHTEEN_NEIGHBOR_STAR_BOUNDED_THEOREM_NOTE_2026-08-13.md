---
claim_id: admissibility_condition_is_six_nn_not_eighteen_neighbor_star_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On Z^3 with nearest-neighbor adjacency, the Admissibility condition tuple is the six graph-distance-1 neighbor sites, not the eighteen-site star that adjoins the twelve edge-diagonal sites of graph distance 2. A law that depends on an edge-diagonal occupancy uses extra data. The note does not select the values of any six-neighbor law, does not adopt L_phys, and does not claim gravity or a Laplacian."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_condition_is_six_nn_not_eighteen_neighbor_star_2026_08_13.py
---

# Admissibility Condition Is The Six-Neighbor Star, Not The Eighteen-Neighbor Star

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact neighbor-set cardinalities and graph distances on `Z^3`,
read against the current Lattice and Admissibility wording.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/admissibility_condition_is_six_nn_not_eighteen_neighbor_star_2026_08_13.py`](../scripts/admissibility_condition_is_six_nn_not_eighteen_neighbor_star_2026_08_13.py)
**Parents:** the live axiom memo
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Lattice names nearest-neighbor adjacency on `Z^3`. Admissibility names one
fixed nearest-neighbor rule whose distribution at a site is determined by,
and varies with, the nearest-neighbor conditions. The nearest-neighbor set
of the origin is the six-point star

`S6 = {±e1, ±e2, ±e3}`.

The twelve edge-diagonal displacements

`D = {±e_i ± e_j : i < j}`

sit at graph distance 2. The eighteen-point union `S18 = S6 ∪ D` is therefore
not the named condition domain. A law `μ18` that depends on an occupancy in
`D` uses extra data. The axioms name the domain of a six-neighbor law `μ6`,
not the values of `μ6` and not the larger domain of `μ18`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer cardinalities and graph distances for the declared Z^3 neighbor sets, plus a displayed extra-data pair of laws. No selection of law values, no L_phys adoption, no gravity or Laplacian claim."
trace_class: negative_route_pruning
target_claim_id: admissibility_condition_tuple_is_six_nn
target_blocker_text: "decide whether Admissibility's named condition is the six nearest-neighbor sites or an eighteen-site star"
source_of_blocker_text: frontier_question
reachability_to_target: closes
artifact_role: theorem
conditional_surface_status: "exact for the neighbor-set theorem and the extra-data pair; values of any six-neighbor law remain open"
hypothetical_axiom_status: "no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `e1 = (1,0,0)`, `e2 = (0,1,0)`, `e3 = (0,0,1)` for the standard
generators of `Z^3`. Graph distance is the nearest-neighbor path metric: the
graph distance of a displacement `v` from the origin is the `l^1` norm
`|v1| + |v2| + |v3|`.

Define

```text
S6 = {±e1, ±e2, ±e3},
D  = {±e_i ± e_j : 1 ≤ i < j ≤ 3},
S18 = S6 ∪ D.
```

An occupancy of the eighteen-star is a map `ω : S18 → {0,1}`. Two integer
laws of occupancy are displayed below: `μ6` reads only `S6`, and `μ18` reads
one edge-diagonal slot.

## Theorem 1

`|S6| = 6`, `|D| = 12`, and `|S18| = 18`. The three axis pairs that generate
`S6` are disjoint, so the six signed generators are distinct. The three
coordinate planes each contribute four signed sums `±e_i ± e_j`, and those
twelve vectors are distinct from one another and from every element of `S6`
because every vector in `D` has two nonzero coordinates. Therefore
`S6 ∩ D = ∅` and `|S18| = 6 + 12 = 18`.

Every `v ∈ S6` has graph distance 1. Every `w ∈ D` has graph distance 2.
Edge-diagonal sites are not nearest neighbors of the origin.

## Theorem 2

The Lattice axiom states that physical sites are the points of the cubic
lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and
proper cubic rotations about each site.

The Admissibility axiom states that there is one fixed nearest-neighbor
admissibility rule, and that for each site the probability distribution over
the possibilities is determined by, and varies with, the nearest-neighbor
conditions.

Nearest-neighbor adjacency is exactly the graph-distance-1 relation. At the
origin that relation names the six-site tuple with slots in `S6`, not the
eighteen-site tuple with slots in `S18`. The named condition is a 6-tuple,
not an 18-tuple.

## Theorem 3

A law of occupancy that depends on an edge-diagonal slot is extra relative
to the named condition.

Define integer laws

```text
μ6(ω)  = Σ_{v ∈ S6} ω(v),
μ18(ω) = μ6(ω) + ω(e1 + e2).
```

`μ6` ignores `D`. `μ18` depends on the single edge-diagonal occupancy
`ω(e1 + e2)`.

Display the pair of occupancies that agree on `S6` and differ on `D`:

- `ω0` occupies `e1` only;
- `ω1` occupies `e1` and `e1 + e2` only.

Then `μ6(ω0) = μ6(ω1) = 1`, while `μ18(ω0) = 1` and `μ18(ω1) = 2`. The
axioms name the domain of `μ6`, not the domain of `μ18`.

## Theorem 4

This note does not select the values of `μ6`. The displayed pair is a
domain witness, not a proposed physical law. The note does not adopt
`L_phys`. It does not claim gravity. It does not claim a Laplacian.

## Theorem 5

The note does not force a distinguished half-weight `r = 1/2`. The displayed
integer values of `μ6` and `μ18` on `{ω0, ω1}` are `1` and `2`. Neither
witness is a half-weight, and no later selector is forbidden from choosing
some other six-neighbor table.

## Hostile Predicates

The predicate "edge-diagonals are nearest neighbors" fails: every vector in
`D` has graph distance 2. The predicate "`|S6| = 18`" fails: `nn_count()`
returns 6. Identity gates call `nn_count()` and `graph_distance(e1+e2)` and
read `6` and `2` respectively.

## Negative Scope

The result is a condition-domain theorem. It does not derive a unique
Admissibility table, a kinetic operator, a continuum Laplacian coefficient,
a gravitational identification, or a physical law `L_phys`. It does not
edit an axiom.
