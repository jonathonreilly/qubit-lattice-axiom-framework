# Finite-field sign-pattern block ranks for the unit-four-cube dissection family (cycle 773)

Date: 2026-08-11

Authority: none

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Machine status:

```yaml
actual_current_surface_status: candidate-retained-grade
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Send the self-contained finite theorem and runner to independent audit; no downstream consumer is yet known."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Exact rational dissection certificate and finite-field block-rank, kernel-intersection, and comparator censuses on one declared unit-four-cube object."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Runner:

- [physical_cell_cutting_sign_pattern_blocks_cycle773_2026_08_11.py](../scripts/physical_cell_cutting_sign_pattern_blocks_cycle773_2026_08_11.py)

Framework premise edges: 0.

This finite construction imports zero framework premises. The current Minimal
Axioms file, `MINIMAL_AXIOMS_2026-06-29.md`, is a scope marker and supplies zero
premises to the theorem.

## Imports and provenance

- Scientific file inputs: none. The sixteen binary corners, determinant-one
  simplex rule, non-edge adjacency cost and its minimum, divisor-80 shifted
  sample with five values per coordinate, signed coordinate action, table
  ordering, fields `F_1000003`, `F_1000033`, and comparator field `F_2` are
  declared finite construction choices.
- Comparator convention: the first four tables in `OUTI`, in deterministic
  enumeration order, define the four-table comparator. The four incidence
  parts retain their deterministic `IORB` order for the intersection census.
- Measured, fitted, literature, predecessor, sibling-branch, and framework
  inputs: none. Every count, matrix, character block, rank, and intersection is
  rebuilt by the runner.
- Implementation provenance: the exact rational pair-intersection algorithm
  was adapted from the current-main runner
  `physical_cell_cutting_sign_labellings_cycle770_2026_08_11.py`, then included
  and gated self-contained here. Values and certificates are recomputed here.
- Package-local reads: the canonical cache records a run; the runner input set
  is empty. Arithmetic gates use Python integers, exact `Fraction`
  arithmetic, and the three declared finite fields. Wall time and peak memory
  occur only in the support-budget gate.

## Exact target and obligation graph

Let `P` be the 192 used determinant-one simplices, `K` the 15800 geometric
24-simplex dissections, `C` the 192 eight-piece covers, `G` the 384 signed
coordinate maps, and `T` the 96 orbit tables constructed below. The exact
finite target is: certify `K` by exact rational interior-disjointness; decompose
the piece coordinates into sixteen 12-dimensional flip-character blocks; and
establish the stated ranks, kernel profiles, kernel intersections, and finite
comparators over their explicitly named fields.

The acyclic proof obligations are:

- `P0` [proved here]: enumerate the determinant-one pieces, adjacency-cost
  minimum, and generic rational sample (`D0`).
- `P1` [proved here; depends on `P0`]: exhaust the sample exact covers and
  certify every co-occurring pair by rational facet separation or intersection
  dimension zero or one. Interior disjointness plus 24 simplex volumes `1/24`
  yields each geometric dissection (`D0`).
- `P2` [proved here; depends on `P1`]: enumerate the used pieces and covers,
  with every cover meeting every dissection once (`D0`, `D1`).
- `P3` [proved here; depends on `P0`-`P2`]: build `G`, its free pair action,
  flip subgroup, and sixteen 12-dimensional character blocks (`D2`-`D4`).
- `P4` [proved here; depends on `P3`]: derive the cycle/axis-pair description
  and the single-table profile over `F_1000003` (`D7`-`D12`).
- `P5` [proved here; depends on `P2`-`P4`]: compute the incidence and two-part
  profiles over `F_1000003`, with the incidence profile corroborated over
  `F_1000033` (`D14`-`D19`).
- `P6` [proved here; depends on `P5`]: compute the common four-part kernel and
  the four incidence-kernel/part-kernel intersections over both declared large
  fields (`D22`-`D25`).
- `P7` [proved here; depends on `P4`, `P5`]: record the specified four-table
  and one-part-swap comparators over `F_1000003`, plus the two kernel-subspace
  classes and their common block profile (`D20`, `D21`, `D26`, `D27`).
- `P8` [proved here]: record the separate `F_2` rank comparator and enforce the
  declared runtime, memory, and output budget (`D13`, `D28`).

Every obligation in the finite target is proved here. Strongest missing lemma
within target: none. Physical interpretation, Record content, multi-cell
extension, and arbitrary coefficient domains lie outside this target.

## 1. Finite object and exact geometric certificate

Write the cube corners as `V = {0,1}^4`. A candidate piece is a five-corner
simplex with determinant magnitude one and volume `1/24`. Of 2672 candidates,
400 attain the minimum declared adjacency cost 6.

The shifted 625-point rational sample gives 15800 exact covers of size 24. The
runner then checks every pair of pieces co-occurring in any cover. Among 15168
pairs, 13632 are separated by a simplex facet; the other intersections have
affine dimension zero for 864 pairs and one for 672 pairs. All co-occurring
simplex interiors are disjoint. Each cover contains 24 simplices of volume
`1/24` inside the unit cube, so its closed union fills the cube and is a
geometric simplex dissection.

Lower-dimensional boundary contacts are admitted. In particular, the cube
center is shared by crossing boundary edges of one co-occurring pair. The
target is a geometric simplex dissection; face-to-face triangulation lies
outside the target.

Exactly 192 pieces occur, each in 1975 dissections. The runner enumerates 192
eight-piece covers and checks that every cover meets every dissection once.

## 2. Signed-coordinate action and character blocks

Permuting four coordinates and flipping any subset gives 384 maps. They act
transitively on the 192 pieces and covers and freely on the 36864 piece-cover
pairs, producing 96 orbits and hence 96 zero-one orbit tables (`D2`).

The sixteen pure flips form a subgroup acting freely on pieces with twelve
orbits. For every sign pattern, transporting its character from one
representative of each flip orbit gives a 12-dimensional block. The sixteen
blocks span all 192 piece coordinates over each declared large field (`D3`,
`D4`).

When a matrix kernel is invariant under the flips, its rank is the sum of its
sixteen block ranks. Gates `D5` and `D6` are positive controls: a coordinate
slice and a column-swapped incidence matrix display which hypotheses the
recomposition uses.

## 3. Orbit-table profile over `F_1000003`

Every orbit table is two-regular and decomposes into 48 eight-cycles on four
pieces. Each cycle is held by the four flips on one axis pair. The flip action
has twelve cycle classes, with two classes for each of the six axis pairs
(`D7`-`D9`).

A cycle contributes a kernel direction to sign pattern `s` exactly when its
axis pair lies inside `s`. For pattern weight `w`, this supplies `w(w-1)`
directions. The kernel profile is therefore `[0,0,2,6,12]`, weighting to 48,
and the rank profile is `[12,12,10,6,0]`, weighting to 144. All 96 tables share
this profile over `F_1000003` (`D10`-`D12`, `D27`).

## 4. Incidence decomposition over the declared fields

Over `F_1000003`, the cover incidence matrix `M` has rank 105, kernel dimension
87, kernel profile `[3,3,6,6,12]`, and rank profile `[9,9,6,6,0]`. Gate `D14`
corroborates the same incidence values over `F_1000033`.

Split `M` using the cover-axis and piece-axis-pair labels. The axis-in-pair part
`U` has rank 114 and kernel profile `[2,2,4,8,12]`; the complementary part `V`
has rank 144 and kernel profile `[0,0,2,6,12]`, all over `F_1000003`. The part
`V` is one orbit table, and `U` is the sum of the other three incidence parts
(`D15`-`D17`).

Subtracting profiles locates the rank difference `144-105=39` in weights zero,
one, and two: `[3,3,4,0,0]`. Factoring through `U` gives the two profile changes
`[2,2,2,2,0]` and `[1,1,2,-2,0]`, of weighted sizes 30 and 9 (`D18`, `D19`).

## 5. Common kernel and per-part intersections

The incidence is the entrywise sum of four orbit tables. Their common kernel
has dimension 12 and profile `[0,0,0,0,12]` over `F_1000003`; it is the
all-axes character block. Stacking the four parts has rank 180 over both large
fields (`D22`, `D23`, `D25`).

For the four parts in deterministic `IORB` order, the dimensions
`dim(ker(M) intersect ker(T_i))` are `[12,12,12,20]` over both large fields.
After quotienting by the 12-dimensional common kernel, the corresponding
dimensions are `[0,0,0,8]` (`D24`). This is the complete claimed mechanism
census; it replaces a basis-vector count with subspace intersections.

## 6. Positive finite comparators

- Over `F_2`, the stacked character bases have rank 12 while every enumerated
  orbit table has rank 144 (`D13`).
- Over `F_1000003`, the specified first four `OUTI` tables sum to a zero-one
  table with rank 105 and profile difference `[3,3,4,0,0]`; its kernel meets
  the incidence kernel in dimension 33 (`D20`, `D21`).
- Replacing one incidence part gives rank 93 and profile difference
  `[3,3,4,3,0]` over `F_1000003` (`D21`).
- The 96 orbit tables form two kernel-subspace classes of 48 tables each. Both
  classes have kernel dimension 48 over the two large fields and share the
  profile `[0,0,2,6,12]` over `F_1000003` (`D26`).

These are enumerated comparator facts on the declared family. They carry zero
universal pruning conclusion.

## 7. Boundary and validation

The rank and profile claims use only the fields named beside them. The exact
rational geometry claim concerns the declared 400 simplices and the exhaustive
sample-cover family. Determinant magnitudes beyond one, adjacency costs beyond
six, face-to-face triangulations, other fields, multi-cell objects, and physical
interpretations lie outside the target.

Gates `D0`-`D27` carry the finite mathematics and controls. Gate `D28` is an
environment-dependent support budget, bound to the declared 300-second timeout,
2500 MB peak-memory ceiling, and 6000-byte output ceiling. The runner exits
nonzero whenever any gate is false. A successful canonical run ends with:

```text
TOTAL: PASS=29 FAIL=0
```

Independent review separately checks exact rational ranks and finite
mutations. Those review checks are provenance controls rather than theorem
premises. This package adds zero methodology change, audit verdict, effective
status, or physical-law interpretation.
