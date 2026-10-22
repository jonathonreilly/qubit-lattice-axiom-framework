---
claim_id: the_split_is_polar_because_nested_children_share_no_inversion_centre_with_their_parent_and_its_diagonal_is_a_convention_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's two tilings at every rung (cubes offset by (1,1,1), triangulated with diagonals between even-sum corners) and its split (eight children per block, each a child even cube): (A) the half-tick order selects no direction: the odd offset (1,1,1) equals all 8 body-diagonal offsets mod 2; all 48 cube operations about a block centre keep both tilings, the half-tick order and the block's causal past over 1-4 half-ticks; under either reading of 'settled' (all edges, or only edges outside even cubes) the settled edge set keeps T_d about the block centre, which maps +x faces to -x faces. (B) Over all 125 child-lattice offsets in eighths of a parent cell: a parent site is a child vertex only in the 8 coincident nestings; every parent axis and diagonal edge is a union of child edges, so that a parent hinge's deficit can sit on child hinges, exactly for 4 of them (the parent sites on even-sum child sites); every coincident nesting keeps only a C3v of the parent background (one fixed vector, no inversion), whatever the split, collar or ownership rule; the reason is that inversion centres are cell centres at every rung and coincident child cell centres sit a quarter parent cell off every parent cell centre; the centred nesting keeps T_d but its parent sites lie inside child tetrahedra and no parent edge is a union of child edges; the 4 nested choices form one orbit of the parent background, with offsets along the 4 tetrahedral diagonals summing to zero, so the choice of (1,1,1) is a coordinate convention; one child per residue mod 2^k is never symmetric about a lattice point, so no number of generations restores inversion. (C) Every exclusive block ownership of parent edges is polar (at most C3 by end-blocks, C3v by nearby blocks; exhaustive over the 30 subgroups of T_d); a shared-boundary split is well defined (pass-once raises commute and are injective) but keeps the same C3v; cycling the corner over the 4 choices keeps only the identity. (D) On every non-uniform pattern of a 2^3-block torus the even cubes are single-level and tick, the parent odd cubes are mixed, and an isolated split's child odd cubes never tick; a 2^3 split cluster ticks 1 of its 27 complete child odd cubes. (E) The vertex and cell readings share the index map, so the polar passing is a rigid translation of a quarter parent cell per axis for every state. Supplied: the copy mass's symmetry and the exclusion of a copy mass on both tilings (Crab bound, register); the junction rule; the locality radius for nearby owners; H0 and l_P in the estimates."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_split_is_polar_because_nested_children_share_no_inversion_centre_with_their_parent_and_its_diagonal_is_a_convention_2026_10_22.py
---

# The split is polar because nested children share no inversion centre with their parent, and its diagonal is a convention

Claim type: bounded_theorem.
Primary runner: `scripts/the_split_is_polar_because_nested_children_share_no_inversion_centre_with_their_parent_and_its_diagonal_is_a_convention_2026_10_22.py`

## Question

The update law's split is polar: its children sit at its sites as least corners, it owns its forward edges, and its trigger reads a collar on its +x, +y and +z faces. Together these keep only C3v of the (1,1,1) diagonal. The copy mass acts on even cubes only. The owner accepts both choices if there is a reason for them. Does a structure already in the framework force them, or is a symmetric rule possible?

## Result

1. **The half-tick order gives no reason (A1-A3).** The odd tiling's offset is the same as all eight body-diagonal offsets mod 2. All 48 cube operations about a block centre keep both tilings, the order of the half-ticks, and the causal past. Whichever edges count as settled at the middle of an even half-tick, the settled set keeps T_d. T_d contains maps that send +x faces to -x faces. Causality therefore cannot pick a one-sided collar.

2. **The nesting forces polarity (B1-B5).** A split must carry the parent's piecewise-flat geometry onto the children: the children's edges along a parent edge each take the parent's value minus s, and the deficit at a parent hinge must sit on child hinges, since a flat child tetrahedron holds no curvature. That requires every parent site to be a child vertex and every parent edge to be a union of child edges. Of 125 offsets of the child lattice, only 4 nestings do this, all coincident. The update law's two tilings recur at every rung, and their inversion centres are the cell centres. In a coincident nesting, the child cell centres sit (1/4)(+-1,+-1,+-1) of a parent cell from every parent cell centre, so no point inverts both rungs. The background's symmetry falls to C3v, with one fixed vector. This holds for any split, collar or ownership rule, because it comes from the children's tilings alone. The polar vector is the quarter-cell offset between the parent's and the children's inversion centres.

3. **The diagonal is a convention (B6).** The four nested choices are conjugate under the parent background, and their vectors are the four tetrahedral diagonals. Choosing "least corner", that is (1,1,1), is a choice of coordinates, not physics.

4. **No symmetric nested rule exists (B3, B7, C1-C3).** The centred (cell) nesting keeps T_d, but the parent sites lie inside child tetrahedra, so it cannot pass a curved geometry. No coincident nesting regains inversion at any depth, because a complete residue system mod 2^k is never symmetric about a lattice point. Exclusive ownership is polar in its own right (C3 or C3v at most). That rederives the earlier ownership result, but it is not needed for the polarity. A shared-boundary split with a symmetric collar is well defined but keeps the same C3v. Cycling the corner choice by generation removes the drift but leaves only the identity as an exact symmetry.

5. **The copy mass follows from the same ownership (D1-D2).** The split acts on whole even cubes, so even cubes are always single-level and tick on every pattern. The odd cubes carry the junction: parent odd cubes are mixed, and child odd cubes near an interface do not tick (an isolated split ticks 0 of its child odd cubes; a 2^3 cluster ticks 1 of 27). A copy mass on odd cubes would therefore be missing in every interface shell. A copy mass on both tilings is excluded by the measured Crab bound, which is supplied from the register.

6. **There is no observable direction (E1-E3).** The polar passing is the cell passing plus a rigid translation of a quarter parent cell per axis, for every state. It has no dispersion and no birefringence, and its drift of 7e-61 c lies far below every bound on Lorentz violation.

## Verdict

This is a derivation of the C3v up to a convention. Nested geometry plus self-similar tilings force the polar form. The four directions are conjugate, so +(1,1,1) is a coordinate label. The copy mass on even cubes is forced by the junction rule, given that the even tiling owns the split (the earlier hanging-nodes result A2), together with the supplied Crab exclusion.

## Smuggling review

- Supplied: the self-similar two tilings (CL-1 text), the parity of the triangulation diagonals, the exact passing of the geometry (CL-1's edge passing plus Regge hinges), the junction rule, the copy mass's symmetry and its Crab exclusion, and H0 and l_P.
- Forced: coincidence, the C3v, the conjugacy of the four directions, the polarity of ownership, and the single-level even cubes.
- Not tested: the 2:1 held LP for the other three conjugate choices (they are images of the tested one, so it holds by symmetry), the Gauss endings of links for a shared-boundary split, and the band-level helicity effect of other copy-mass placements.

## Boundary

Finite exact enumeration on period cells and tori. No claim about non-lattice child placements beyond 1/8 offsets. Measured numbers enter only the estimates.
