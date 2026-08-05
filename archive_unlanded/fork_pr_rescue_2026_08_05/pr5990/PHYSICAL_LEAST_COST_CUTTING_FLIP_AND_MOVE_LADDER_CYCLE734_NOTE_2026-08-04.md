# The local move structure of the single cell's least-cost cuttings — Cycle 734

Date: 2026-08-04

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

The object is one cell of the lattice carried through one tick of emergent time: the
four-cube on the sixteen corners of `{0,1}^4`, whose three spatial columns and single
tick column are the columns the axioms of
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supply, with nearest
neighbour adjacency only and the proper cubic rotations alone kept. A piece is a five
corner simplex of the cell of least volume; the cost of a piece counts the pairs of its
corners more than one lattice step apart, and the cost of a cutting is the sum over its
pieces. Earlier cycles measured the floor of that cost on this cell. This cycle asks what
freedom a cutting has once it sits at the floor, and answers by complete search: the floor
is not locally adjustable on two pieces or on three, the smallest cost keeping change
replaces exactly four, that change is a flip between the two least cuts of one of five
regions, and the cuttings at the floor stay in separate groups until moves on ten pieces
are allowed. Every statement below is a check in whole numbers over an explicit finite
set; no solver is used, and no two pieces are called separate without a plane exhibited
and verified in whole numbers.

## The least volume forces the piece count

Over all 4368 five corner subsets of the cell the volumes run
`[(0, 1360), (1, 2672), (2, 320), (3, 16)]` in units of one over 24. The least nonzero
value is one such unit, so a piece of least volume is one part in 24 of the cell, and a
cutting of the cell into pieces of least volume has exactly 24 of them. This is measured
over the whole set of five corner subsets, not imposed: the 2672 pieces are the ones the
spectrum selects. The same fact fixes the shape of any local move — a hole left by
removing `k` pieces can only be refilled by `k` pieces.

The adjacency charge over the 2672 pieces runs
`[(3, 64), (4, 384), (5, 1152), (6, 768), (7, 304)]`, and every piece matrix inverts
exactly over the integers.

## A corner inside a piece is a corner of that piece, and what buys it

Because a piece matrix inverts exactly over the integers, a corner of the cell read
against a piece gives whole numbers. A corner lying in the closed piece then has all but
one of those numbers zero, so it is one of the piece's own corners. Over all 2672 pieces
the corners lying inside are exactly the five of the piece itself. This makes a candidate
filter on the sixteen corner bits exactly sound, which is what the searches below rely on.

The scope of that argument was tested rather than assumed, and the test moved the claim.
The whole numbers are what the least volume buys: all 336 five corner sets of volume two
or three read some corner in fractions, so the route through integrality does belong to
the least volume. The conclusion does not. Of those same 336 sets, 0 reach past their own
corners. So the containment statement holds at every nondegenerate volume here, and only
the proof by whole numbers is special. The note claims the narrower fact.

## The floor, the cuttings that reach it, and that they really cut the cell

One piece costs `[(6, 400), (7, 1216), (8, 864), (9, 192)]`. A complete search over the
400 pieces of least cost visits 502838 nodes and finds 15800 cuttings, each of 24 pieces,
so the floor 144 is reached. Those cuttings between them use 192 of the 400 pieces of
least cost, filling 4 whole families of the cell symmetry; the remaining pieces of least
cost appear in no cutting at the floor.

An exact cover of sample points is not by itself a cutting of the cell. It becomes one
here: each of the 15168 pairs of pieces sharing a cutting is pushed apart by a plane
exhibited and checked in whole numbers, so the 24 pieces of a cutting meet only on their
boundaries, and, carrying between them the volume of the cell, they fill it.

## No move on two pieces keeps the cost

Over the 15168 pairs the corners in common run
`[(0, 2976), (1, 5280), (2, 5376), (3, 1248), (4, 288)]`. Exactly 288 of the pairs can be
refilled a second way, and they are exactly the pairs meeting in four corners. The six
corners of such a pair carry one relation, and that relation puts two corners of weight
one on each side and leaves two out, recorded as `[((2, 2, 2), 288)]`: the four corners
that move are the corners of a flat square, and the move re-cuts that square along its
other diagonal. Recutting it always costs more, by `[(1, 192), (2, 96)]`. So the square
re-cut, the one local move the cell offers on two pieces, never preserves the floor.

## No move on three pieces keeps the cost, and the fills that exist cost more

Of the 649600 triples of pieces sharing a cutting, 40512 admit a second refill at all,
and 0 admit one by three pieces of least cost. This is stated as a positive measurement
rather than an absence: the second refills that do exist cost
`[(19, 27264), (20, 14592), (21, 384)]`, every one of them strictly above the floor 18 for
three pieces of least cost. Every three piece re-cut therefore costs more, and by at
least one unit.

Taken with the previous section this fixes the local picture. A move that exchanges two
pieces for two, or three for three, is the only kind the volume permits at those sizes,
since the hole from `k` pieces takes exactly `k` back. Both are measured here and neither
keeps the cost. So the smallest cost keeping change is not a single local re-cut of that
kind; it is a composite.

## The smallest change replaces four pieces, and the population is wide

Over all 124812100 pairs of cuttings at the floor the number of pieces they differ in
takes the values `[4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
24]` — never one, two, three or five. The smallest is 4, reached 46128 times. At the other
end of the same range 29069284 pairs share no piece at all, counted a second way by
listing which cuttings each piece belongs to.

The two absences have different standing and the note keeps them apart. That one, two and
three do not occur is proved by the two sections above, which examine every pair and every
triple. That five does not occur is measured, by a census that is complete because its
entries sum to the number of pairs of cuttings.

Allowing moves on up to four, then five, and so on to ten pieces, the cuttings at the
floor sit in `[349, 349, 157, 61, 61, 13, 1]` groups within reach of one another. The
ladder is flat from four to five and again from seven to eight, and reaches a single group
only at ten. So the floor is locally rigid and globally connected, and the two facts do
not conflict: nearly a quarter of all pairs of cuttings at the floor share no piece, while
no pair differs in fewer than four.

## The smallest move is a rigid flip on one of five regions

The 46128 smallest moves re-cut 120 regions with 120 distinct corner sets, each holding 8
corners and reaching both values in all four columns. Up to the symmetry of the cell there
are 5 such regions, in families of sizes `[12, 12, 24, 24, 48]`.

A region holds `[8, 32]` pieces and cuts into four in `[2, 24]` ways, of which exactly 2
reach its own floor 24. The regions of a family are used equally often, `[10, 478]` times
each; the family holding only 8 pieces is the rigid one, used 240 times in all, sitting at
the low end of both ranges above.

Swapping the two floor cuts of a region carries a cutting at the floor to another and back
46128 times, exactly the number of smallest moves. So every smallest move is that swap,
and the swap is an involution on the cuttings at the floor: the local freedom of a cutting
at the floor is a binary switch for each region it happens to fill. Whether those switches
can be thrown independently of one another is not measured here.

## Independent cross-checks performed

The numbers in this section come from checks run outside the paired runner, by methods the
runner does not use; the runner does not print them.

Each headline was re-derived a second way. The volume spectrum was recomputed by
fraction-free elimination rather than cofactor expansion and agreed. The corner statement
was recomputed by floating solve verified in whole numbers rather than by the adjugate,
giving 13360 corners inside and no mismatch. The cuttings were found again by a complete
search with the opposite pivot rule, which visits 496849 nodes rather than 502838 and
returns the identical set of 15800. Those cuttings decompose into 391 families of the cell
symmetry, of sizes 8, 12, 24 and 48, matching the family count measured in the previous
cycle by a different route. The triples were counted again as one sixth of the trace of
the cube of the co-occurrence matrix. The distance census was recomputed from posting
lists and the ladder by depth-first labelling rather than by merging. The region families
were recomputed from stabiliser orders, and the count of smallest moves recomputed by
counting the cuttings that contain one floor cut of each region.

Each check was also perturbed, to confirm it would fail if the object it tests were wrong.
A cost reading one column alone is not constant on the piece families — it varies inside
40 of the 57 — so constancy is a fact about the adjacency cost and not about the families.
Admitting the mirror turns as well gives a group of 96 elements and collapses the pieces
to 36 families rather than 57, so the family count depends on keeping only the proper
rotations, exactly as the lattice axiom does. The boundary test applied to the sixteen
corners flags 37680 of 42752 readings, well past the 13360 forced by a piece holding its
own corners. The fraction test that separates the volumes flags 0 of the 2672 pieces of
least volume, so flagging all 336 larger sets is a fact about those sets. The separation
test refuses every one of 159 sampled pairs of pieces that genuinely share an interior
point. Dropping the single most used piece, which carries 1975 cuttings, leaves 13825
rather than 15800. Of the 1248 pairs meeting in three corners, 0 admit a second fill.
There are 12862 eight corner sets reaching both values in all four columns, of which only
120 are regions, so being a region is a strong condition and not a generic one. In all 120
regions the two floor cuts hold four pieces each and share none, so the flip moves exactly
four. Finally the cuttings meet the pieces 379200 times, matching 15800 cuttings of 24.

The perturbation of the corner statement is the check that changed the note. Its first
form assumed the containment conclusion belonged to the least volume, and measurement
refuted that: the conclusion holds at volume two and three as well. What the least volume
buys is the reading in whole numbers. The claim in the body was narrowed to the measured
scope, and the runner now measures and prints both halves.

## Boundary and honest read

The pool of 192 pieces is measured by the search, not derived from a symmetry statement,
and the same holds for the 5 region shapes and their family sizes. They are complete for
this cell and this cost, and the note claims nothing beyond that.

Every count here is scoped to the single cell of one lattice step and one tick, with the
adjacency cost and the least volume as defined above. No statement is made about cells of
other extent, other adjacency, other costs, or about the lattice as a whole; a claim of
that kind would need its own measurement. In particular the flat ladder steps and the
group count 1 at ten pieces are properties of this population of 15800 cuttings.

The absence of a cost keeping move on two or three pieces is proved on this cell by
examining every pair and every triple. It does not by itself say what the largest local
re-cut is that a cutting away from the floor admits, nor whether the four piece flip is
the smallest move for costs above the floor. Both are open and neither is touched here.

Time enters only as the fourth column of the cell. Nothing in this cycle selects a
direction along it, and the tick flip is kept in the symmetry group throughout, so no
result here depends on an arrow.
