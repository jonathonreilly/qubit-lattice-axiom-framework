# Each Table's Row Space Is The Other Table's Space Of Additive Readings

**Date:** 2026-08-09
**Type:** science
**Runner:** [scripts/physical_cell_cutting_additive_reading_space_cycle762_2026_08_09.py](../scripts/physical_cell_cutting_additive_reading_space_cycle762_2026_08_09.py)
Audit: unset.

## What this is

The object is one cell, taken as the unit four-cube on its sixteen corners. A piece
is a five-corner sub-simplex whose four edge vectors from its first corner have
determinant of absolute value 1, so a piece has volume one twenty-fourth of the
cell; among those, the pieces at the adjacency cost floor are kept. A cutting is a
set of kept pieces with pairwise disjoint interiors that together fill the cell. A
cover is an eight-piece set no two of whose pieces ever share a cutting; gate G1
certifies that each such set meets every cutting exactly once, which is the
property an earlier cycle of this lane derived and which is re-verified, not
assumed, in the build below. An assignment
gives a number to each piece. A cutting reads an assignment by summing it over the
pieces of that cutting; a cover reads it by summing it over the pieces of that
cover. Two tables record which piece belongs to which family member: the cutting
table and the cover table.

The result is one sentence in two halves. The assignments whose cutting readings
are all equal to each other are exactly the row space of the cover table, and the
assignments whose cover readings are all equal to each other are exactly the row
space of the cutting table. Each table's row space is the other family's space of
additive readings, and the two dimensions are 105 and 88.

## What was already known

The preceding cycle of this lane established, as an exact whole-number identity, a
relation between the cover-side lifted projector, the cutting-side lifted
projector, the identity and the all-ones matrix, and it read that identity as
forcing the dimension count 105 = 192 - 88 + 1. That identity is the engine of
everything in this cycle. It is not new here.

The characterization stated below is a short consequence of that identity together
with the two dimensions this lane had already measured, and no part of its
mathematics is claimed as new. In one direction the identity says that an
assignment built from the cover table is read at a single level by every cutting;
in the other it says the same with the two families swapped; and once one direction
is in hand, equality of dimensions turns the containment into an equality, makes
the two row spaces span everything, and leaves their intersection at the constants.
A reader holding the preceding cycle's identity can reach every claim below in a
few lines, and this note does not pretend otherwise.

What this cycle contributes is therefore not the algebra. It is the statement in
reading language rather than in projector language; an independent rebuild of the
whole cell from scratch over the rationals, which re-measures every input number
instead of citing it; three negative controls that show the match is not automatic;
and the contact with the additivity clause of the fixed-reality axiom, together
with a plain account of where that contact stays open.

## The object

The runner builds the cell from scratch. Of the five-corner sub-simplices of the
four-cube, 2672 have determinant of absolute value 1; the adjacency cost floor
among them is 6, attained by 400 of them. Cuttings are found as exact covers of 625
sample points of divisor 80, chosen so that no sample point lies on a facet plane
of any kept piece; gate G0 checks that genericity condition directly rather than
assuming it. Genericity is what makes the sample search complete: with no sample
point on a facet plane, a genuine tiling of the cell covers each sample point
exactly once, so no tiling escapes the search over exact covers, and the search
over exact covers is itself complete. Gate G1 then certifies the other direction,
that what the search returns really is a tiling. The search returns 15800 cuttings,
each of 24 pieces. Exactly 192 of
the 400 floor pieces occur in a cutting at all, and each of those 192 lies in 1975
cuttings. There are 192 covers, and the cover table has every row sum and every
column sum equal to 8.

Gate G1 verifies that each cutting is a genuine tiling rather than an artifact of
the sampling: every piece has volume 1 over 24, every cutting holds 24 of them, and
all 15168 co-occurring piece pairs are certified interior-disjoint exactly, 13632
of them by a separating facet plane and the rest by an exact computation of the
affine dimension of the intersection. Twenty-four pieces of volume 1 over 24 with
pairwise disjoint interiors fill the cell.

## The characterization

Write the cutting table for the 15800 by 192 zero-one table of cuttings against
pieces, and the cover table for the 192 by 192 zero-one table of covers against
pieces.

Gate G4 measures rank 88 and kernel dimension 104 for the cutting table, and rank
105 and kernel dimension 87 for the cover table. Gate G5 measures that one over 24
times the constants reads 1 on every cutting, and one over 8 times the constants
reads 1 on every cover, so each side has a particular solution and the constants
lie in neither kernel. Gate G6 therefore measures the two solution sets: the
assignments with all cutting readings equal form a space of dimension 105, and the
assignments with all cover readings equal form a space of dimension 88.

Gate G7 measures that the first of those spaces and the row space of the cover
table have joint rank 105, which is the dimension of each; the two spaces are
therefore equal. Gate G8 measures that the second space and the row space of the
cutting table have joint rank 88, again the dimension of each, so those two are
equal as well. Both directions are computed here over the rationals, with no
floating point anywhere in the algebra, and neither is inferred from the other.

The rank of the cutting table is obtained without eliminating on a table of 15800
rows. Gate G3 justifies the substitution used: the 192 by 192 product of the
cutting table with itself is built twice by different routes and the two builds
agree, its kernel is checked to annihilate every one of the 15800 cutting rows, and
the rank is then recovered independently from the cutting table's own rows, two
evenly spread selections of 400 and of 800 rows both giving 88.

## The sum and the intersection

Gate G9 measures that the two row spaces together have joint rank 192, so they span
the whole assignment space. Since their dimensions are 88 and 105, their
intersection has dimension 88 + 105 - 192 = 1. The constants lie in both row spaces,
because the column sums of both tables are constant: the column sums of the cutting
table are all 1975 and those of the cover table are all 8. The intersection is
therefore exactly the constant assignments, and nothing else is shared.

Gate G14 records the bookkeeping that follows: 105 is 192 minus 88 plus 1, 88 is
192 minus 105 plus 1, and 88 plus 105 is 192 plus 1.

Not every gate here is discriminating, and G14 is the clear case. It is arithmetic
on numbers the earlier gates have already measured, and it would pass for any three
numbers standing in that relation; it is a consistency record, not evidence. The
load-bearing gates are G7, G8, G9 and G10. Gates G11, G12 and G13 are the ones that
show those four are not automatic.

## The two totals

Gate G10 measures the two common readings. For an assignment in the
105-dimensional space, the common cutting reading is the plain sum of the
assignment divided by 8. For an assignment in the 88-dimensional space, the common
cover reading is the plain sum divided by 24. The gate checks this on 3 elements of
each space, each with nonzero sum, so the check is not the empty statement that 0
equals 0.

Both totals come from the column sums. Summing the cutting readings over all 15800
cuttings counts each piece 1975 times, giving 1975 times the sum of the assignment;
summing the same constant reading over 15800 cuttings gives 15800 times it; and
15800 is 8 times 1975. Summing the cover readings over all 192 covers counts each
piece 8 times, giving 8 times the sum; summing the constant over 192 covers gives
192 times it; and 192 is 24 times 8.

## The axiom contact

The fixed-reality axiom in [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md)
says, verbatim:

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

That clause supplies exactly one piece of arithmetic about readings, and nothing
else. The cuttings of this cell are families to which the clause applies in form: a
cutting's 24 pieces have pairwise disjoint interiors and together are the whole
cell, and gate G1 measures that over all 15800 of them. So if a piece carries a
reading, additivity says every cutting of the cell returns the same total, which is
precisely the condition that the cutting table sends the assignment into the
constants. Under that identification the admissible assignments are exactly the row
space of the cover table.

The identification is open and is not derived here. The axiom places records at
sites and says only records are readable. A piece is a region, not a site. Nothing
in the axiom says a region carries a reading, and nothing in this note derives that
it does.

The naive repair fares worse. Gate G2 measures that the 24 pieces of a cutting
spend 120 corner slots on only 16 corners, one corner taking from 4 to 24 of them.
A reading carried by the corners is therefore not partitioned by a cutting at all,
and the additivity clause does not apply to it. So the obvious retreat from regions
to corners does not recover the argument; it loses the premise the clause needs.

The identification of a piece as a reading-bearing object is a named open
identification of this cycle, not a result of it. The four claims stand on their own
as exact statements about the object, independent of that identification.

## Controls

Three gates are built to come out negative, and each one did.

Gate G11 takes a cover, which lies in the 105-dimensional space, and reads it on
the cover side. That reading is not constant: it takes the values 0, 1, 2, 4 and 8.
Had it come out constant, the two spaces would not have been separated by the very
readings that define them, and the characterization would have been reporting one
space twice under two names.

Gate G12 replaces the constants by the zero space and measures what the two
dimensions become: they drop to 104 and 87. Had they not dropped, the constant
direction would already have been inside the two kernels, and the plus 1 in the
bookkeeping would have been an artifact of the construction rather than a real
extra direction.

Gate G13 applies a cyclic column shift to the cover table. The shifted table still
has rank 105 and still has every row sum and every column sum equal to 8, so it
matches the original on every coarse feature; but its joint rank with the
105-dimensional space is 191, not 105, so the correspondence fails for it. Had the
shifted table matched too, the joint-rank test in gates G7 and G8 would have been
passing on the shape of a table rather than on its content.

## Measured totals

The runner has 17 gates and prints `TOTAL: PASS=17 FAIL=0`, exiting 0. Elapsed time
is under 300 seconds and peak resident memory is under 1500 MB; gate G16 reports
both as bounds rather than as timings. Total stdout is 2278 characters. The runner
carries no randomness and two runs give byte-identical output. All ranks, kernels
and joint ranks are computed exactly over the rationals.

## Boundary

- The identification of a piece as an object that carries a reading is open. It is
  named here and not derived here. Claims 1 to 4 are computational identities about
  this cell and do not depend on the identification; the axiom contact does.
- A corner-carried reading is demonstrably not partitioned by a cutting: 120 corner
  slots fall on 16 corners, with one corner taking from 4 to 24 of them. The
  additivity clause does not apply to such a reading, and this note claims nothing
  about one.
- Nothing here says why the two ranks are 88 and 105 rather than other numbers.
  They are measured, not derived: they come out of the complete search over this one
  cell, and no argument in this note predicts either of them from the shape of the
  four-cube.
- This is one cell. Nothing here says how cells join to each other. The whole-number
  bookkeeping of this lane and the spatial joining of neighbouring cells are
  different questions, and this note does not relate them.
- The characterization is an equality of two subspaces of the 192-dimensional
  assignment space. It is not a correspondence between individual cuttings and
  individual covers, and it says nothing about which piece goes with which.
- The cuttings are found as exact covers of a sample point set, and the tiling
  property is then certified separately for all 15168 co-occurring piece pairs. That
  certificate is what makes the cuttings tilings of the cell rather than of the
  sample; the sampling itself proves nothing.
