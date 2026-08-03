# Adjacency-admissible assembly and the excess-slot trade — Cycle 723

Date: 2026-08-03

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. No new axiom or
primitive is proposed or adopted.

Runner: `scripts/physical_adjacency_admissible_assembly_trade_cycle723_2026_08_03.py`
(34 PASS / 0 FAIL, exit 0). The combinatorial half is exact integer arithmetic
over complete enumerations; the assembly half reuses the open-coframe endpoint
compiler `scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py`.

## Why this exists

The assembly stencil of this lane — the Kuhn path stencil on the tick-extended
unit cell — carries 240 edge slots, of which 120 are purely spatial. Of those
120, 72 lie along the six nearest-neighbour axis directions named by the LATTICE
axiom and 48 do not. The 48 are the slots at which the construction reaches past
the axiom's own adjacency, and the natural question is whether some other
construction could be assembled from axiom-adjacency slots alone. If one could,
the frame-label structure measured in the preceding cycles would become entirely
axiom-internal.

This cycle answers in two halves. First, the excess is **forced**: over a complete
enumeration of corner assembly cells, none is adjacency-only, and a positive floor
holds simplex by simplex and globally. Second, removing the exceeding slots from
the assembled second-variation form does not remove their content — it either
discards more than half of the form or trades cell-locality for range — and in
every variant the frame label is unchanged.

## The seam is larger than 48

Give each edge slot its **spatial footprint weight**: the L1 weight of the spatial
part of its direction. Weight 0 is a same-site slot, weight 1 is a nearest-neighbour
slot of the axiom's 6-NN adjacency, and weight 2 or more exceeds that adjacency.
A tick-crossing slot still has a spatial part, so the correct count of "exceeds
adjacency" is by footprint, not by "purely spatial".

| spatial footprint weight | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| slot-uses in the stencil | 24 | 108 | 72 | 36 |
| distinct slot variables per cell | 8 | 36 | 18 | 3 |

So **108 of the 240 slot-uses, and 21 of the 65 distinct slot variables per cell,
exceed the axiom's 6-NN adjacency** — more than twice what the purely spatial
reading names. The 48 purely spatial exceeding slot-uses (36 face-diagonal and 12
body-diagonal) are one part of that seam, not the whole of it.

## No corner assembly stencil is adjacency-only

The obstruction is affine independence, and it is visible already at small size.
Among three cell corners spanning a nondegenerate triangle, at most 2 of the 3
slots are 6-NN. Among four affinely independent corners, at most 3 of the 6 slots
are 6-NN; reaching 4 requires an affinely **dependent** quadruple, which cannot be
a simplex. The runner carries that dependent quadruple as an explicit rejector, so
the bound is a measurement and not an assertion.

Over the complete enumeration of corner 5-subsets of the tick-extended cell —
4368 subsets, of which **3008 are nondegenerate** — every nondegenerate corner
4-simplex carries **at least 3 footprint-exceeding slots**, at each of the four
tick splits (1, 2, 3 or 4 of its corners at tick 0). The floor is positive at every
split, so no corner assembly stencil is adjacency-only. The Kuhn path stencil
carries 5/4/4/5 by tick split against that floor of 3/3/3/3, and attains the
purely spatial floor 3/1/1/3 exactly.

## The global floor, and a coincidence that carries no content

The per-simplex floor does not by itself bound a whole cell. The facet structure
supplies the rest.

**Facet forcing.** A nondegenerate corner 4-simplex meets the tick-0 hyperplane in
a 3-face exactly when 4 of its corners lie there, and then in exactly one such face.
So the tick-0 facet of the cell is dissected by the 4-corner family and the tick-1
facet by the 1-corner family, and no other simplex contributes to either facet.

**Cone relation.** For those two extreme families, and over the complete
enumeration, 24 times the simplex volume equals 6 times the volume of its base
facet tetrahedron. Each extreme family therefore consumes exactly the facet's own
6 volume units of the cell's 24.

**Facet census.** The 3-cube facet admits 58 nondegenerate corner tetrahedra, of
6-fold volume 1 and 2, and **182 corner dissections**, of sizes 5 and 6. Interior
disjointness is decided by an exact integer separating-axis test — face normals of
both tetrahedra and all edge-pair cross products — so the census is exact, not
sampled. Every one of the 182 dissections carries at least **18** exceeding slots.

**Bookkeeping.** Of the cell's 24 volume units, the two extreme families take 6
each, leaving 12 for middle-split simplices. A middle-split corner simplex has
24-fold volume at most 3, so at least 4 of them are needed, each carrying at least
3 exceeding slots. The floor for any corner stencil is therefore

> 18 + 18 + 3 x 4 = **48 footprint-exceeding slot-uses**, against the Kuhn path
> stencil's 108.

**Caution, stated plainly.** This floor of 48 and the Kuhn stencil's purely spatial
excess of 48 are counts of two different things — a lower bound over all corner
stencils on the full footprint-exceeding count, versus one particular stencil's
purely spatial count, whose own full count is 108. Their numerical agreement carries
no content and is gated in the runner as a distinctness check so that it cannot be
read as one.

## What removing the exceeding slots costs

Assemble the tick-resolved second-variation form Q on a spatially open box at tick
length 2, and split the slot variables by footprint weight into the
adjacency-admissible set A (weight at most 1) and the exceeding set D (weight at
least 2). At box size 3 this is 446 slot variables = 270 + 176.

Two properties of Q come first.

- **Q is cell-local.** Every nonzero coupling of Q joins two slots whose site
  supports fit in one unit cell; the largest entry at spatial extent 2 or more is
  exactly 0.000000e+00.
- **Q_DD is singular in a structured way.** Its flat block has exactly one direction
  per cell per tick — 16, 24 and 54 flat directions at box size and tick length
  (3, 2), (3, 3) and (4, 2), matching the count of cells times ticks in each case.
  Those flat directions are annihilated by the mixed block Q_AD to below 1.0e-04,
  and the live part is well conditioned: softest live eigenvalue 1.5900e-01 at box
  size 3 and 4.8367e-02 at box size 4, condition numbers 1.83e+02 and 6.00e+02.
  Elimination is therefore well defined on the complement of the flat block.

**The deletion horn.** Restricting to Q_AA — simply dropping the exceeding
variables — discards 0.529 of the form's squared Frobenius weight at box size 3 and
0.547 at box size 4. More than half the assembled form lives in or across the
exceeding slots.

**The elimination horn.** Eliminating D by the Schur complement keeps the stationary
value exactly: the eliminated form reproduces the full form's value at its
stationary point to below 1.0e-12, while a uniformly shifted eliminated form breaks
that identity at 8.608e-04, so the gate discriminates. What it does not keep is
locality. Writing the eliminated form's Frobenius weight as shares by spatial extent
(squares summing to one), box size 3 gives 0.400 on-site, 0.886 at range 1 and 0.235
beyond one cell; box size 4 gives 0.428, 0.836, 0.160 at range 2 and 0.304 at range
3 — the full box diameter. The largest entry beyond one cell is 6.318 in the
eliminated form against exactly 0.000000e+00 in the assembled form, so this range is
**generated by the elimination, not inherited from the assembly**.

Either way the exceeding slots are traded, not removed: one horn pays in weight, the
other in range.

## The frame label survives both horns

The order-6 symmetry count and the 8-valued tick-resolved frame label measured in
the preceding cycles are read off three different matrices — the full assembled form,
the deleted form Q_AA, and the eliminated form — at box sizes 3 and 4. All six
readings give symmetry count 6 and 8 frame labels. The frame-label structure is
carried by the adjacency-admissible variables alone, and is insensitive to which of
the three forms one reads.

## Boundary

- The enumeration is over **corner** vertex sets: the 0/1 corners of the
  tick-extended cell. Constructions using vertices at other rational positions, or a
  coarser cell, are outside what is measured here, and nothing in this note bounds
  them.
- The global floor of 48 uses the facet census of one cell facet together with the
  volume bookkeeping; it is a floor on footprint-exceeding **slot-uses** of a corner
  stencil, not on distinct variables, and not on any quantity of a non-corner
  construction.
- The elimination measurements are at box sizes 3 and 4 only. "No decay in range" is
  a statement at these two sizes; no asymptotic claim is made, and the box is
  spatially open, so boundary effects are present at both sizes.
- The Frobenius shares are bookkeeping on the assembled matrix. They are not
  identified with any continuum quantity, and no continuum limit is taken.
- The comparison tolerance used for the symmetry and label counts, the flat-block
  threshold, and the compiler's finite-difference step are supplied constants of the
  runner, not measured quantities.
- Q is indefinite; nothing here is a positivity or stability statement about it.

## Honest auditor read

The strongest part is the combinatorial half: exact integer arithmetic, complete
enumerations at every stage, an explicit rejector for the affine-independence bound,
and a cone relation that is verified rather than asserted. The weakest part is the
step from the per-simplex floor to the global floor of 48, which chains the facet
census, the cone relation and the volume bookkeeping; each link is gated, but the
chain is the place to attack. The 48/48 agreement is flagged in the runner precisely
because it would otherwise invite a reading it does not support. The assembly half is
two box sizes, and the claim that the elimination generates range rather than
inheriting it rests on the assembled form's beyond-cell entries being exactly zero,
which is measured and not tolerance-limited.

## Dependencies

- [Tick-extension second variation](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md) — landed, unaudited: the tick-extended second-variation object assembled here.
- [Proper-cubic covariance ceiling](PHYSICAL_PROPER_CUBIC_COVARIANCE_CEILING_CYCLE690_NOTE_2026-07-24.md) — landed, unaudited: the covariance ceiling of unit-cell triangulations.
- [Direction set versus triangulation covariance](PHYSICAL_DIRECTION_SET_VS_TRIANGULATION_COVARIANCE_CYCLE695_NOTE_2026-07-25.md) — landed, unaudited: the direction-set reading of covariance, and the Kuhn edge-direction census.
- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) — the LATTICE axiom's 6-NN adjacency and proper cubic rotations, which define the admissible set here.

Context, cited without a dependency edge: the open-coframe endpoint compiler
`physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py`, and the
in-flight cycle 721 and cycle 722 frame-label measurements
`physical_stencil_derived_centrality_cycle721_2026_08_02` and
`physical_oriented_diagonal_stencil_orbit_cycle722_2026_08_02`.

## What this opens

1. **Non-corner constructions.** The floor proved here is over corner vertex sets.
   A construction on a refined cell, or with vertices at other rational positions,
   is untouched by this enumeration and is the natural next place to look for an
   adjacency-only assembly.
2. **The generated range.** The eliminated form reaches the full box diameter with
   no decay at these sizes. Measuring how that range behaves as the box grows would
   turn a two-size observation into a law.
3. **The 18 of the facet census.** Every facet dissection carries at least 18
   exceeding slots, and the two facet families are forced. Whether that 18 is itself
   forced by the facet's own adjacency graph, independently of the volume argument,
   is a self-contained question.
4. **Label insensitivity.** The frame label is identical across all three forms.
   Identifying the smallest sub-block of the admissible variables that still carries
   the 8-valued label would sharpen what the label actually depends on.
