# Physical cell cutting: parity constancy is a theorem of the sign characters, and the small class counts follow from coset blocks

Date: 2026-08-14
Authority: none.
Audit: unset.

Scope: the cuttings of the open unit four-cube cell, relabelled as arrangements of translates of
24 tile classes inside an order-192 group. Two debts left open by the census note are paid here.
The parity of a cutting's class counts is shown to lie in the intersection of the kernels of seven
sign characters, and every vector of that intersection is parity-constant, so parity constancy of
the realized profiles becomes a theorem. The per-profile counts 24, 20 and 16 of the three small
profile classes are then obtained from an independent enumeration of coset blocks together with an
equal-split argument that the symmetry group supplies.

This note adds no citation edges. Sibling artifacts are named in backticks for context only, never
as dependencies: `PHYSICAL_CELL_CUTTING_GROUP_TILING_CENSUS_CYCLE783_NOTE_2026-08-14.md`,
`PHYSICAL_CELL_CUTTING_TRACE_LAW_COMPLETION_CYCLE784_NOTE_2026-08-14.md`.

Paired runner:
`scripts/physical_cell_cutting_parity_and_small_class_derivation_cycle785_2026_08_14.py`.
Everything quoted below is recomputed from scratch inside that runner, from the corner coordinates
of the cell upward; no value is read in from a sibling artifact, no tile data is written into the
source by hand, and the note quotes no number that the runner's stdout does not print. Gate tags in
square brackets name the line of stdout that carries the measurement.

## Result

Three deliverables. First, parity constancy of the realized profiles is derived rather than
observed: for each of the seven nontrivial sign characters of the mask group the parity vector of a
cutting lies in the mod-two reduction of an exact integer kernel, the intersection of the seven
kernels has dimension 7 and 128 vectors, and every one of those 128 vectors is parity-constant
across the twelve positions. [K15] Second, the per-profile counts 24, 20 and 16 of the three small
classes are computed from coset-block structure: an independent exact cover by affine blocks
reproduces the coset-pure cuttings, whose class content covers the small classes entirely, and an
equal-split theorem turns the class totals 72, 120 and 96 into the per-profile counts. [K8] [K9]
[K10] [K12] Third, one of those families has a hand-sized closed form: for each of the three
four-element mask subgroups containing the all-axes flip, exactly 12 six-class choices admit a
consistent signed colouring and each admits 2 of them, so 12 x 2 = 24. [K14]

The census note recorded two debts in its own words. The first:

> The six per-profile tiling counts, 9368, 944, 160, 24, 20 and 16, are measured, not derived.

The second:

> Parity constancy of the realized profiles is measured.

The parity sentence is discharged in full by the sign-character theorem below. The counts sentence
is discharged for 24, 20 and 16 — the counts of the three small classes — and for those alone; the
counts 9368, 944 and 160 of the large classes are untouched by this note and remain measured.

## The relabelled cell

The cell is the open unit four-cube with its sixteen corners. A piece is a five-corner simplex
whose edge matrix at its first corner has determinant of size one; there are 2672 such candidates,
the adjacency cost over them has floor 6, and the pieces at that floor number 400. Testing
membership on a generic integer sample lattice of 625 points, the depth-first exact cover finds
15800 cuttings, every one of them by 24 pieces, and 192 distinct pieces occur across them.
[K1] [K2]

The twelve walls of the cut carve the cell into 192 chambers; every piece holds 8 of them and every
chamber lies in 8 pieces. The order-384 symmetry group of the cell, an axis permutation followed by
a reflection x to 1 - x on a subset of the axes, permutes chambers and pieces, and its even-mask
subgroup of order 24 x 8 = 192 acts freely and transitively on the chambers. Fixing one chamber
therefore names every chamber by a group element. [K3]

Read in that naming, each of the 192 used pieces is the graph of a function: its 8 chambers carry 8
distinct axis orderings, and the piece assigns to each of them one even mask. The set of axis
orderings is the piece's position; 12 positions occur, 16 pieces to a position, and inside a
position the pieces fall into 2 types of 8. The 24 position-and-type classes are exactly the orbits
of mask translation, each of them free of size 8, so a piece is named by its class offset function
f and a translation mask m, and it covers, at the axis ordering rho of its position, the chamber
(rho, m XOR f(rho)). The runner checks that value law against the geometric incidence for all 192
pieces. [K4]

The profile of a cutting is the vector of position multiplicities of its 24 pieces. 25 profiles are
realized; they fall into 6 orbits of the symmetry group, of sizes 1, 6, 3, 3, 6, 6, with
per-profile counts 9368, 944, 160, 24, 20 and 16, and the weighted total is 15800. Following the
census note, name the orbits U, O, A, B, C, D in that order; the small classes are B, C and D, with
totals 72, 120 and 96. [K5]

## The base fact

The even masks form a group of order 8 inside the 16 masks. Three of its four-element subgroups
contain the all-axes flip 15: they are 0,3,12,15 and 0,5,10,15 and 0,6,9,15. The fact that makes
the rest of this note possible is that every one of the 24 class offset functions takes its values
inside exactly one of those three subgroups, with 8 classes assigned to each. [K6]

A class is therefore compatible with one distinguished subgroup, and since that subgroup has index
two in the eight-element mask group, the coset of a class inside it is a single bit.

## Coset purity and block partitions

Call a cutting coset-pure when, for every class it meets, the set of translation masks it uses in
that class is a coset of a nontrivial subgroup of the mask group. The affine subsets of the
eight-element mask group number 43: 28 pairs, 14 four-element cosets and the whole group. Attaching
one to a class gives a block, a set of chambers; over 24 classes there are 1032 blocks. [K7]

Now run a second exact cover, of the 192 chambers by blocks, with at most one block used per class.
This search never consults the list of cuttings. It returns 1224 block partitions, every one of
them a cutting, all distinct. [K8] Enumerating the coset-pure cuttings directly among the 15800
also returns 1224, and the two sets are equal, tested in both directions. [K9]

The class content of the 1224 is the operative fact: B 72 of 72, C 120 of 120, D 96 of 96, A 144 of
480, U 792 of 9368, and O 0 of 5664. [K10] The three small classes are carried entirely, class A
partially, class O not at all.

## The small classes and the equal-split theorem

The theorem in one line: the symmetry group carries cuttings to cuttings and acts transitively on
the profiles of a single class, so the fibers over the profiles of one class have equal size.

Both premises are checked. All 384 group elements carry all 15800 cuttings to cuttings; the induced
action on profiles has 6 orbits covering the 25 realized profiles, and the per-profile count is
constant on each orbit. [K11] Since a class total is the sum of its per-profile counts and those
counts are equal, the total divides by the orbit size. The block enumeration supplies the totals of
the three small classes, and the division gives 72/3 = 24, 120/6 = 20 and 96/6 = 16, matching the
measured per-profile counts of B, C and D exactly. [K12]

That is the sense in which the three small counts are computed here: the enumeration that produces
them is combinatorial in the tile coordinates and never inspects the per-profile census, and the
last step from class total to per-profile count is forced by symmetry rather than counted.

## The class C closed form

Fix one of the three subgroups V and ask for the cuttings all of whose class mask sets are cosets
of V. There are 24 of them for each V, every one in class C, and a four-element coset determines
its subgroup, so the three families are disjoint: 3 x 24 = 72 of the 120 cuttings of class C.
[K13]

The count 24 has a closed form small enough to check by hand. A class whose masks form a V-coset
covers, at each axis ordering of its position, exactly one of the two cosets of V; since the 8
masks at an axis ordering must be covered once each, exactly two of the classes containing that
axis ordering are used, and they must supply the two different cosets. So a cutting of this shape
is a choice of six classes whose positions two-cover the 24 axis orderings, together with a colour
x_k in GF(2) naming the coset of each chosen class. Writing phi_k(rho) = 1 exactly when f_k(rho)
lies outside V, the requirement that the two classes a and b at rho supply different cosets is the
edge constraint x_a + x_b = phi_a(rho) + phi_b(rho) + 1. There are 512 two-covering six-class
choices; exactly 12 of them make the constraint consistent, each is connected as a single part, so
each carries 2 colourings, and 12 x 2 = 24. [K14]

## The sign-character theorem

Identify the eight even masks with triples over GF(2) by reading off the first three bits; the
fourth is determined because the mask is even. The seven nontrivial sign characters pair with masks
through the GF(2) product, and each takes its two signs equally often, so every one of them sums to
zero over the mask group.

Fix a cutting and an axis ordering rho. The pieces of the cutting whose position contains rho cover
the 8 chambers at rho, and by the value law the masks they supply are m XOR f_k(rho) for the class
k and translation mask m of each such piece. The cutting property says exactly that these masks are
the 8 even masks, once each. Applying a nontrivial character w and summing therefore gives zero,
and since the character is multiplicative the sum factors class by class:

  sum over classes k at rho of chi_w(f_k(rho)) times s_k(w) equals 0, where s_k(w) is the sum of
  chi_w(m) over the translation masks the cutting uses in class k.

This is an integer relation on the vector s(w), with coefficient matrix M_w of size 24 by 24 whose
entry at (rho, k) is chi_w(f_k(rho)) when the class k contains rho and 0 otherwise. Each term of
s_k(w) is a sign, so s_k(w) agrees mod two with the class count n_k. Hence the parity vector of
the cutting, the 24 class counts mod two, lies in the mod-two reduction of the integer kernel of
M_w, for every one of the seven characters.

The kernels are computed exactly, never numerically: fraction-free integer row reduction on the
transpose augmented with the identity, using row operations of determinant of size one, so the rows
that end with zero left part are a basis of the saturated integer kernel; their mod-two reduction
keeps the same dimension. The seven dimensions are three of 12 and four of 9, and the intersection
of the seven has dimension 7, that is 128 vectors. Every one of the 128 is parity-constant: the
per-position parity, the sum mod two of the two class counts at a position, is the same at all 12
positions. Parity constancy is therefore a property of every solution of the character conditions,
not of the realized cuttings alone. [K15]

Two consistency facts come with it. The parity vectors of all 15800 cuttings do lie in the
128-element space, and 124 distinct values occur there. And the conditions are redundant in a
specific way: dropping any single character leaves the intersection unchanged, so any six of the
seven suffice, while the intersection of the seven character conditions without the level-one
incidence condition is already the same space, so the incidence condition is implied. [K15]

## The rejectors

Two gates are present so that a silent drift in the construction would show up as a failure rather
than as agreement.

The parity rejector shows that the characters carry the argument. The level-one incidence condition
alone, which says only that the class counts at each axis ordering sum to 8, has kernel dimension
18 mod two, that is 262144 vectors, of which 253952 are not parity-constant. Incidence forces
nothing about parity by itself; the sign characters are what force it. [K16]

The purity rejector shows that coset purity is a genuine separating property rather than a
universal one: 1224 of the 15800 cuttings are coset-pure, strictly fewer than all of them, and
class A is pure at 144 of 480, strictly fewer than all of its cuttings. A property that everything
satisfied could not have singled the small classes out. [K16]

## Boundary

What is derived here: parity constancy of the realized profiles, from the seven sign characters and
the exact kernels; the equal split of a class total into its per-profile counts, from the
transitivity of the symmetry group on the profiles of a class; the base fact that every class
offset image lies in one four-element mask subgroup; and the closed form 12 x 2 = 24 for each
subgroup family inside class C.

What is not derived, and is reported as measured:

- The per-profile counts of the large classes, 9368, 944 and 160, are measured, not derived. This
  note touches the small classes and leaves the large ones exactly where the census note left them.
- The membership equality that drives the small-class result, namely that the three small classes
  are precisely the classes carried entirely by the coset-pure cuttings, is itself measured: both
  sides are enumerated and compared. The block enumeration is an independent structural
  reproduction of the totals 72, 120 and 96, not a count from first principles.
- Class A is pure at 144 of its 480 cuttings, so the route as stated does not extend unchanged to
  A; the coset-block picture describes part of A and stops.
- No structural characterization of the U and O fibers is offered here. Class O contributes 0 of
  its 5664 cuttings to the coset-pure set and class U contributes 792 of 9368, and neither number
  is explained by anything in this note.
- The parity theorem constrains parity and nothing finer: it says every solution of the character
  conditions is parity-constant, 128 vectors in all, and says nothing about which 124 of them are
  realized.

The gates are computational identities: each one recomputes both sides from the rebuilt object and
compares, and none of them is allowed to read its comparison target from the value it is testing.
The tile coordinates themselves are derived inside the runner from the piece-chamber incidence, so
the coset structure is not an input to the gates that use it.

The next path opened by this note is the lever it leaves exposed: what forces coset purity exactly
on the three small classes. Purity is the whole content of the small-class result, and at present
it is an observed coincidence between two enumerations rather than a property read off the tile
coordinates. An argument that predicts which profiles must be pure would carry the small counts
without the comparison step, and would say something immediately about the partial purity of class
A and about the large classes that are not pure at all.
