# Physical cell cutting: two-tile group form, forced sign symmetry, and an exact finite label-sum census

Date: 2026-08-14

Authority: none.

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
claim_type_reason: "Exact finite enumeration, group action, tiling, orbit, and label-sum statements on one declared unit-four-cube construction."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Scope: after exact rational certification that the enumerated simplex collections are geometric
cuttings of the open unit four-cube cell, the cuttings are identified with partitions of an
order-192 group into left translates of two eight-element tiles. In that model the label sum
becomes a signed permutation sum. The sign symmetry and per-profile halving are forced by the
order-384 symmetry group; the numeric census over the 15800 cuttings is an exact finite
enumeration assembled from measured orbit-profile data.

This note adds no citation edges. Sibling artifacts are named in backticks for context only, never
as dependencies:
`PHYSICAL_CELL_CUTTING_LABEL_SUM_SIZE_BOUND_CYCLE781_NOTE_2026-08-14`,
`PHYSICAL_CELL_CUTTING_DIAGONAL_PARITY_CYCLE782_NOTE_2026-08-14`.

Paired runner:

- [physical_cell_cutting_group_tiling_census_cycle783_2026_08_14.py](../scripts/physical_cell_cutting_group_tiling_census_cycle783_2026_08_14.py)

Framework premise edges: 0.

This finite construction imports zero framework premises. The current Minimal
Axioms file, `MINIMAL_AXIOMS_2026-06-29.md`, is a scope marker and supplies zero
premises to the theorem.

## Imports and provenance

- Scientific file, literature, observational, fitted, predecessor, sibling,
  and framework inputs: none.
- Declared construction choices: the sixteen binary corners, determinant-one
  simplex rule, non-edge adjacency cost and its minimum, the shifted five-value
  sample on each axis, signed coordinate action, minimal naming rule, table
  ordering, and the two tiles selected by the stated peak-shadow rule.
- Package-local reads: the canonical cache records a run; the runner input set
  is empty. All mathematical gates use Python integers and exact `Fraction`
  arithmetic. Wall time and peak memory occur only in the support-budget gate.
- Implementation provenance: the exact rational pair-intersection routine was
  adapted from the current-main runner
  `scripts/physical_cell_cutting_sign_pattern_blocks_cycle773_2026_08_11.py`,
  then included and gated self-contained here. No result is read from it.

## Exact target and obligation graph

Let `P` be the 192 used determinant-one simplices, `D` the 15800 geometric
24-simplex cuttings, `C` the 192 chamber labels, `E` the order-192 even-mask
group, and `G` the order-384 signed-coordinate symmetry group constructed
below. The exact finite target is to certify `D` geometrically, identify `P`
with the left translates of two eight-element subsets of `E`, and establish
the stated label covariance, tiling census, profile orbits, and sign-halving
identities.

The acyclic proof obligations are:

- `P0` [proved here]: enumerate the determinant-one candidates, the declared
  adjacency-cost floor, and all exact covers of the generic rational sample
  (`K1`).
- `P1` [proved here; depends on `P0`]: certify every co-occurring simplex pair
  by exact rational facet separation or intersection dimension. Interior
  disjointness plus 24 simplex volumes `1/24` makes every sample cover a
  geometric cutting (`K1G`).
- `P2` [proved here; depends on `P0`, `P1`]: construct the chamber incidence,
  compare it with direct rational representative membership, and verify that
  every cutting partitions the chambers (`K1`, `K1C`).
- `P3` [proved here; depends on `P2`]: construct `G`, compare its induced
  chamber action with direct action on simplex vertices, and prove label
  covariance (`K2`).
- `P4` [proved here; depends on `P2`, `P3`]: establish the free transitive
  `E`-relabelling, group law, two tiles, stabilizers, and translate-to-piece
  bijection (`K3`-`K5`).
- `P5` [proved here; depends on `P4`]: recount the group tilings and prove their
  objectwise, label-preserving bijection with `D` (`K6`, `K7`).
- `P6` [proved here; depends on `P4`, `P5`]: enumerate positions, all coarse
  profiles, realized profiles, and the modulo-two rank (`K8`, `K9`).
- `P7` [proved here; depends on `P3`, `P5`, `P6`]: establish profile orbits,
  sign-character stabilizers, every per-profile sign symmetry, census
  assembly, and the independent extreme-orbit cross-check (`K10`-`K13`).
- `P8` [proved here]: exercise three wrong-construction controls and enforce
  the declared runtime, memory, and output budget (`K14`-`K17`).

Every obligation in this finite target is closed. Physical interpretation,
multi-cell extension, classification of arbitrary tile pairs, and a closed
formula for the enumerated per-profile counts lie outside the target.

Everything quoted below is recomputed from scratch inside that runner, from the corner coordinates
of the cell upward; no value is read in from a sibling artifact, and the note quotes no number
that the runner's stdout does not print. Gate tags in square brackets name the line of stdout that
carries the measurement.

## The object

The cell is the open unit four-cube with its sixteen corners. A piece is a five-corner simplex
whose edge matrix at its first corner has determinant of size one; there are 2672 such candidates,
the adjacency cost over them has floor 6, and the pieces at that floor number 400. Testing
membership on a generic rational sample lattice of 625 points, the depth-first exact cover finds
15800 sample covers, every one of them by 24 pieces, and the pieces that occur in at least one
cover number 192. [K1]

The geometric upgrade is separate from the sample search. Of the 15168 pairs of pieces that
co-occur in a cover, 13632 are separated by a simplex facet. Exact rational vertex enumeration of
the remaining pair intersections gives affine dimension zero for 864 pairs and one for 672 pairs.
Thus the simplex interiors in every cover are disjoint. Each determinant-one simplex has volume
`1/24`, so 24 such simplices inside the unit four-cube have total volume one; their closed union
fills the cube. These 15800 certified geometric covers are the cuttings used below. [K1G]

Naming a piece means walking its corners: a start corner together with an order of the four axes.
Raw enumeration gives 384 walk namings, each piece carries exactly two of them, and the minimal
naming is the one whose start corner has the lower binary index of the opposite-corner pair. [K1,
and the namings line of stdout]

The twelve cut walls of the cell carve its interior into 192 chambers, each recorded as an axis
order together with three signs. Every used piece is a walk simplex, whose interior facet equations
belong to this wall arrangement, so membership is constant on each chamber. The sign-pattern deal
assigns 8 chambers to every piece; dually every chamber lies in 8 of the 192 pieces. Direct exact
membership of a rational representative of each chamber agrees with the deal for all 192 pieces.
Every cutting meets every chamber in exactly one piece: over all 15800 cuttings the count of
partition failures is 0. [K1, K1C]

The label of a piece is taken on its minimal naming: the sign of the axis order, times minus one
to the parity of the start corner. The label sum of a cutting adds that label over its 24 pieces.
Measured over the whole collection, the label sum takes the values zero, plus or minus 4, and plus
or minus 8, with counts 9896, 2832 on each side, and 120 on each side. [census line of stdout]

## The symmetry group and the sign character

The symmetry group of the cell has order 384: an element is a pair, an axis permutation p composed
with a per-axis reflection mask m acting by x -> 1 - x on each masked axis. Acting on exact
rational interior points and reading the image chamber back off the size order and the signs of
its offsets, each of the 384 elements permutes the 192 chambers, hence permutes the 192 pieces.
The induced map agrees on all 73728 element-piece pairs with direct transformation of the five
simplex vertices; the 384 piece maps are pairwise distinct, so the action is faithful. [K2]

The sign character of an element is eps = sgn(p) times minus one to the parity of the reflection
mask. It takes the value minus one on exactly 192 of the 384 elements. [K2]

Covariance of the label: for every element g and every piece P, the label of gP equals eps(g)
times the label of P. This is checked on all 73728 element-piece pairs, with 0 failures. [K2]

Two consequences are then derivations, not measurements. First, the label sum is covariant: the
label sum of the image cutting equals eps(g) times the label sum of the cutting, because the image
of a cutting is a cutting and the label of each piece picks up the same factor. Second, any fixed
element with eps equal to minus one gives a bijection from cuttings with label sum `s` to cuttings
with label sum `-s`; its inverse has the same negative character. Therefore the census is symmetric
under a change of sign. The measured census respects that symmetry exactly: 2832 on each side at
size 4, and 120 on each side at size 8.

## The free transitive relabelling

Restrict to the elements whose reflection mask has even parity. There are 8 such masks and 192
such elements, and this even-mask subgroup relabels the chambers freely and transitively: fixing a
base chamber, the map that sends a subgroup element to the image of the base chamber lands on each
of the 192 chambers exactly once. [K3]

The subgroup is also handled abstractly, as pairs consisting of an axis permutation and an even
mask, with the product of two pairs given by composing the permutations and combining the masks
through the permuted-mask operation. The abstract product agrees with composition of cell maps on
all 36864 ordered pairs, with 0 failures, and the relabelling dictionary is equivariant on all
36864 ordered pairs as well, again with 0 failures. [K3] So chambers may be replaced by subgroup
elements once and for all: a change of bookkeeping whose value is that pieces become subsets of a
group.

## The tiling dictionary

Pulling the 8 chambers of a piece back through the relabelling gives an eight-element subset of
the subgroup. The permutation parts of those 8 elements are pairwise distinct, so each piece casts
a shadow of 8 axis orders. [K4, K8]

Two base pieces are singled out without reference to any target. Among the 8 pieces holding the
base chamber, exactly two have the shadow consisting of the axis orders that rise to a peak and
then fall; the smaller-indexed of those two is base piece 9. Under the even-mask subgroup the 192
pieces fall into two classes of 96, and the smaller-indexed piece at the base chamber outside the
class of piece 9 is base piece 73. [K4]

Their transported subsets are the two tiles, printed in full by the runner as an axis order
followed by its reflection mask:

- tile zero: `0123:0 0132:12 0231:12 0321:12 1230:12 1320:12 2310:12 3210:15`
- tile one: `0123:0 0132:12 0231:12 0321:12 1023:0 1032:12 2013:0 3012:0`

The translate dictionary is the following statement. For every element w of the subgroup and each
of the two tiles, the left translate of the tile by w is again the transported subset of a piece;
the number of distinct left translates of the two tiles is 192, split 96 and 96; each distinct
translate arises from exactly 2 translating elements; and the resulting map from translates to
pieces is a bijection onto the 192 pieces. [K4]

The count is closed by hand from the two measured ingredients. The stabilizer of each tile inside
the subgroup has order two: tile zero is fixed by `3210:15` and tile one by `1032:12`, and in both
cases the permutation part has sign plus. Orbit size times stabilizer order is 96 times 2, that is
192, the order of the subgroup, checked directly rather than quoted. Hence the 192 translating
elements produce 96 distinct translates per tile, 192 in all; the map to pieces is injective
because a translate is exactly the transported chamber set of the piece it names, and the target
has 192 elements; an injection between finite sets of equal size is onto. So every piece is a left
translate of one of the two tiles, and the two tiles suffice. Each element of the subgroup lies in
exactly 8 of the 192 translates, matching the dual incidence of the chambers. [K4]

The partition property of the object now reads: a cutting is a partition of the 192-element
subgroup into 24 left translates of the two tiles. That is the sense in which the cuttings are
exact tilings of a group by two tiles.

## The label sum as a signed permutation sum

On the even-mask subgroup the reflection parity is even, so the sign character reduces to the sign
of the axis permutation alone. Both base pieces carry label plus one. Combining that with
covariance gives the label of a translate directly: the label of the piece named by the translate
of a tile by w equals the sign of the permutation part of w, independently of which of the two
tiles was translated. The runner checks the identity on all 192 pieces, with 0 failures. [K5]

Well-definedness needs the stabilizer fact and nothing more. The two elements that produce a given
translate differ by the order-two stabilizer of the tile, whose permutation part has sign plus;
multiplying by it leaves the sign of the permutation part unchanged, so the label read off from
either representative is the same.

Therefore the label sum of a cutting is a signed permutation sum: add the sign of the permutation
part over the 24 translating elements of the tiling, one per tile of the partition. Nothing
geometric survives in that formula, which is why the census can be recovered from the abstract
data alone.

## The abstract recount

The recount is run over the abstract model only: 192 group elements, 192 tiles given as an
eight-element mask together with an integer label, and a depth-first exact cover that never
touches a coordinate, a chamber, or a simplex. It finds 15800 tilings, and their label sums have
exactly the measured census: 120 at minus 8, 2832 at minus 4, 9896 at zero, 2832 at 4, and 120 at
8. [K6]

The two collections then agree object by object. Mapping each abstract tiling through the
dictionary to a set of 24 pieces gives a bijection onto the 15800 cuttings, and on each pair the
signed permutation sum equals the geometric label sum; failures on both counts are 0. [K7]

The abstract search is not a re-derivation of the geometry: it uses the tile data that the
geometry produced. What it does establish is that the count and the census are consequences of the
group-tiling data alone, so any further argument about the census may be conducted there.

## Positions, profiles, and parity

The shadow of a translate is its set of 8 axis permutations. Only 12 distinct shadows occur; call
them positions. Each of the 24 axis permutations lies in 4 of the 12 positions, each position
carries 16 of the 192 tiles, and inside a position the two tile types contribute 8 each. The label
is constant on a position-and-type class, and the two types of a position carry opposite labels.
[K8]

The profile of a tiling is the vector of position multiplicities of its 24 tiles. Counting the
tiles that contain a fixed axis permutation gives the abstract system: for each of the 24
permutations, the multiplicities of the 4 positions containing it sum to 8. Over the nonnegative
integers that system has 125 solutions: 8 with all entries odd, 27 with all entries even, and 90
with entries of mixed parity. [K9]

Of the 125, exactly 25 are realized by tilings: 6 of the all-odd solutions and 19 of the all-even
ones. No parity-mixed solution is realized, though 90 of them satisfy the coarse linear system.
Separately, reducing its 24 defining rows modulo two gives rank 6 and hence a kernel of dimension 6
in the 12 profile coordinates. These are exhaustive finite measurements of the coarse system and
the realized tilings. Whether a different argument derives parity constancy from the full tiling
constraints lies outside this note's target. [K9]

## Orbits, equivariance, and the halving

The symmetry group acts on positions, hence on profiles: each of the 384 elements induces a
well-defined permutation of the 12 positions, with 0 consistency failures across the pieces. The
25 realized profiles fall into 6 orbits, of sizes 1, 6, 3, 3, 6, 6. Profiles in a common orbit
carry equal tiling counts and equal censuses, as they must by equivariance, and the weighted total
over the orbits returns 15800. [K10]

Labelling the orbits by decreasing tiling count, the per-profile data is:

- class U, orbit size 1, count 9368, census 24 at minus 8, 9320 at zero, 24 at 8
- class O, orbit size 6, count 944, census 472 at minus 4 and 472 at 4
- class A, orbit size 3, count 160, census 8 at minus 8, 144 at zero, 8 at 8
- class B, orbit size 3, count 24, census 12 at minus 8 and 12 at 8
- class C, orbit size 6, count 20, census 6 at minus 8, 8 at zero, 6 at 8
- class D, orbit size 6, count 16, census 16 at zero

The halving is a derivation. Each of the 25 realized profiles is fixed by at least one group
element of sign character minus one; such an element maps the tilings of that profile to
themselves while negating the label sum, so each per-profile census is symmetric in the sign of
the label sum. The runner checks the stabilizer condition on all 25 profiles and the symmetry on
every per-profile census. [K11]

Two purity facts sharpen the picture and are measured: class O is pure at size 4, that is every
tiling with an all-odd profile has label sum plus or minus 4; class B is pure at size 8. [K11]

## Census assembly and the extreme cross-check

The three census entries now assemble from the orbit data as computational identities.

- At size 4 the whole population is the odd class: 2832 = 6 times 472, orbit size times the
  per-profile count on one side.
- At size 8 the population is collected from the classes with extreme tilings, each profile
  contributing its two-sided extreme total and each orbit its size: 48 from class U, 16 from
  each of the 3 profiles of class A, 24 from each of the 3 profiles of class B, and 12 from
  each of the 6 profiles of class C. The total is 240, and halving gives 120 on each side.
- The zero entry is the remainder: 9896 = 15800 - 5664 - 240, where 5664 is the whole odd
  class and 240 the whole extreme population. [K12]

The extreme population is then cross-checked directly against the group action, without reference
to profiles. The 240 cuttings of label sum of size 8 fall into 7 orbits under the full symmetry
group: 4 orbits of size 24, whose stabilizers have order 16, and 3 orbits of size 48, whose
stabilizers have order 8. In each case orbit size times stabilizer order is 384, checked directly.
Every one of those stabilizers consists of elements of sign character plus one, which is exactly
what allows an orbit to sit entirely at size 8, and each orbit splits evenly between the two
signs. [K13]

## Claim boundary and exhaustive data

The derived statements are the covariance of the label under the symmetry group and hence the sign
symmetry of the census; the free transitive relabelling of chambers by the even-mask subgroup; the
well-definedness of the translate label and the identity that makes the label sum a signed
permutation sum; the upgrade of the translate dictionary from injective to bijective by the
equal-count argument; and the halving of every per-profile census from a sign-character
stabilizer.

The following exact enumerations are inputs consumed by those derivations:

- The six per-profile tiling counts, 9368, 944, 160, 24, 20 and 16, are direct
  enumeration outputs consumed by the orbit assembly.
- The per-profile extreme counts, 48, 16, 24 and 12 on the classes that carry them, are
  measured; the assembly identities consume them rather than producing them.
- Parity constancy of the realized profiles and the dimension-6 kernel of the coarse system are
  separately measured.
- The purity of the odd class at size 4, and the fact that the small class B is entirely
  extreme, are measured.
- The recount equality at 15800 is measured; the bijection between tilings and cuttings is
  derived from it together with injectivity, not the other way round.

The gates are computational identities: each one recomputes both sides from the rebuilt object and
compares, and none of them is allowed to read its comparison target from the value it is testing.
Three of the gates are rejectors, present so that a silent drift in the construction would show up
as a failure rather than as agreement:

- Moving a single element of tile zero to another even mask leaves 288 distinct translates, of
  which only 96 coincide with actual pieces, short of the 192 that the true tile achieves. [K14]
- Negating the labels of one tile type changes the census at 3 of its values; the count at
  minus 8 moves from 120 to 108. [K15]
- A concrete parity-mixed solution of the abstract system, the profile 4 0 4 0 3 1 0 0 1 4 3
  4, is realized by 0 of the 15800 tilings. [K16]

The next path opened by this note is the count itself. With the cuttings identified as partitions
of a group into left translates of two tiles, the per-profile counts are questions about that
group and those two tiles alone, and no geometric input remains to be eliminated.
