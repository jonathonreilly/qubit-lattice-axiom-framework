# The spectrum of the eight-piece Gram is fixed by the arithmetic of the tables, not by the symmetry — Cycle 761

Date: 2026-08-09

Authority: none

Audit: unset.

Status: computational identities of the finite cutting system

Claim type: computational identities

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_cover_spectrum_cycle761_2026_08_09.py)

Scope: computational identities of the finite cutting system. Every number
below is machine-checked by the paired runner, which rebuilds the cell
complex, the least-volume pieces, the cuttings at the adjacency cost floor,
the cutting-by-piece table and the eight-piece sets, forms the eight-set-by-piece
table and its Gram matrix, reads the whole spectrum of that Gram exactly by
fraction-free integer elimination, builds the relabellings got by permuting the
four coordinates of the four-cube and flipping any of them, certifies exact
whole-number multiples of the orthogonal projectors onto the row spaces of both
tables, and averages the counting functions over those relabellings. The note
reports what the runner measured and nothing else, and it adds no import and no
assumption to [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## What this cycle adds

The eight-piece sets are pinned down here for what they are. Each of the 192 is a
set of eight pieces no two of which share a cutting, and each of them meets every
one of the 15800 cuttings exactly once. Counting the meetings two ways gives both
double-counts at once: 192 = 24 times 8 and 15800 = 8 times 1975. So an eight-piece
set does not cut the cube up: what it partitions is the set of cuttings, into the
8 families of 1975 cuttings that run through each of its pieces.

The numbers 105 and 87 that say how much of the piece space those sets see are
arithmetic facts about this one finite object and not consequences of its
symmetry. Averaging the counting functions over the relabellings gives a cross
term of 21 on both tables, so the seen space and the unseen space carry copies of
the same patterns and neither is a union of whole pattern types; the averaging
route measured here therefore cannot by itself produce 88, 105 or 87.
Independently, the eight-piece Gram carries no whole-number spectrum: 56 of its 192
eigenvalues are not whole numbers, and they are identified here exactly, as three
quadratic families and one cubic family, by a certificate that leaves nothing out.

## What is already known and is not claimed here

Earlier cycles of this lane measured all of the following, and none of it is
claimed here. The maps got by permuting the four coordinates of the four-cube and
flipping any of them number 384 and are the complete symmetry of the system, and
they are transitive on the 192 pieces. The eight-set-by-piece table has rank 105
and nullity 87. The spectrum of its Gram has 136 whole values and 56 that are not
whole. The counts of pieces shared between two of the sets are regular, and the
matrices built
from them do not have products staying inside their own span. Those results belong
to the earlier cycles that measured them.

What the runner establishes here, over and above rerunning those measurements:
(1) the 56 non-whole eigenvalues are identified exactly, as three quadratic
families and one cubic family with the multiplicities stated below, certified by a
squarefree polynomial of degree 19 that annihilates the matrix over the whole
numbers together with fourteen nullities adding to 192; (2) the trace split, as an
independent cross-check on those multiplicities; (3) that the split of the piece
space into what a table sees and what it does not is not a split into whole
pattern types, on both tables, alongside a control that shows what a genuine such
split looks like.

## The spectrum

The whole part of the spectrum is ten values with multiplicities: 0 with
multiplicity 87, 2 with 8, 4 with 8, 8 with 3, 10 with 8, 12 with 6, 16 with 2, 20
with 10, 24 with 3, and 64 with 1. Those account for 136 of the 192 eigenvalues.

The remaining 56 are the roots of four factors, written with the high coefficient
first, each repeated at the multiplicity given: `1 -20 80` at multiplicity 6, with
discriminant 80; `1 -44 400` at multiplicity 6, with discriminant 336; `1 -52 320`
at multiplicity 4, with discriminant 1424; and the cubic `1 -44 516 -1280` at
multiplicity 8, with discriminant 8640512. None of those four discriminants is a
perfect square, so none of the four factors breaks up over the whole numbers: for
the three quadratics that is immediate, and for the cubic the runner tries all 36
divisors of the constant term taken with both signs and 0 of them is a root.
Counting each factor once for each of its roots gives 19 distinct eigenvalues, 10
whole and 9 not.

The certificate works like this. The fourteen factors are pairwise different and
none of them can be broken up over the whole numbers, so no two of them share a
root and their product is squarefree. The runner measures the nullity of each
factor evaluated at the Gram matrix, exactly, by fraction-free integer
elimination, and those fourteen nullities add to 192, the full size of the matrix.
The runner then multiplies the fourteen factors one at a time into a running
matrix, in exact integer arithmetic, and the result has 0 nonzero entries. A
squarefree polynomial that annihilates the matrix admits no eigenvalue outside its
own roots, and the nullities adding to the full 192 leave no multiplicity
unaccounted for, so the list above is the entire spectrum with nothing left out
and nothing double-counted.

Control G10 is what makes that argument bite rather than restate itself. Moving
the cubic's constant term by one and rebuilding the same product leaves 33024
nonzero entries instead of 0, so the product gate does discriminate against a
factor list that is nearly right. And the nullity of the Gram matrix shifted by 20
is measured to be 10; had it been 9 instead, the fourteen nullities would have
added to 191 and not 192, and the completeness half of the certificate would have
failed.

## The trace cross-check

The sum of the roots of each factor, weighted by its measured multiplicity, splits
the trace as 592 + 592 + 352 = 1536, and 1536 is 192 times 8, the measured trace of
the Gram matrix. This is an independent check because it uses only the second
coefficient of each factor and the number of ones in each row of the eight-set table,
and it touches neither the nullity measurements nor the product. Almost any wrong
multiplicity would move one of the three parts and break the total.

The whole part and the quadratic part both come out 592. Nothing here is built on
that, and it is not claimed to mean anything.

## No whole-number structure organizes the eight-piece sets

For each ordered pair of different eight-piece sets, count how many pieces they
share. That count is exactly the matching off-diagonal entry of the Gram matrix,
and it takes 4 distinct values: 0, 1, 2 and 4. For every one of the 192 rows the
counts of the other 191 sets at each value are the same: 157 at 0, 20 at 1, 10 at 2
and 4 at 4, and 157 + 20 + 10 + 4 = 191. So the sharing counts are regular in the
strong sense
that the row profile does not depend on the row.

Now take the identity together with one zero-one graph per distinct value: 5
matrices in all. If products of those 5 matrices stayed inside their own span, the
Gram matrix would satisfy a polynomial of degree at most 5 and could have at most 5
distinct eigenvalues. It has 19. No set of matrices that small can have products
staying inside its own span here.

An earlier cycle of this lane measured that non-closure directly, by checking the
products themselves. This is a stronger and independent route to the same
conclusion, not a new fact: it rules out closure from the eigenvalue count alone,
without inspecting any product.

## Symmetry does not pick out what is seen

For each relabelling, count the pieces it fixes; call that c_perm. For each table,
certify an exact whole-number multiple of the orthogonal projector onto its row
space and read the same count restricted to what the table sees; call that c_vis,
and call the difference c_blind. Averaging products of those counts over the 384
relabellings gives, on the cutting side at rank 88: 29 for seen against seen, 33
for unseen against unseen, and 21 for the cross term, with 1 for seen against the
constant and 0 for unseen against it. On the eight-set side at rank 105 the same
averages are 34, 28 and 21, again with 1 and 0. Both sides satisfy the sum check
29 + 33 + 2 times 21 = 104 and 34 + 28 + 2 times 21 = 104, which is the average of
c_perm against itself. Every one of those divisions leaves remainder 0, so every
average is a whole number.

Control G15 fixes what the cross term would look like if the split were the good
kind. Take the all-ones direction and everything perpendicular to it. That is a
split into whole pattern types, and its cross average comes out 0, against 1 for
the all-ones part against itself and 103 for the perpendicular part against
itself. So 0 is what a genuine split gives, and 21 is not 0.

Because 21 is not 0, the seen space and the unseen space contain copies of the same
patterns, on both tables. Neither is a union of whole pattern types, so the
averaging route measured here cannot by itself produce 88, 105 or 87: these
averages are blind to the very distinction those numbers make. What this leaves
open is where the numbers do come from. They are fixed by the arithmetic of the
tables themselves, and that is where to look next.

## Runner

The runner rebuilds the cell complex, the least-volume pieces, the cuttings at the
adjacency cost floor, the cutting-by-piece table and the eight-piece sets, forms
the eight-set-by-piece table and its Gram matrix, and then runs twenty gates. They
are listed here in the order the runner emits them.

- G0 the object: cuttings, pieces, pieces to a cutting, cuttings through a piece.
- G1 the eight-set-by-piece table is zero-one with every row sum 8 and every column sum 8.
- G18 all 2672 piece frames invert exactly over the whole numbers, and the 24
  rotations behind the sample points have determinant 1.
- G19 every eight-piece set meets every cutting exactly once, so 192 = 24 times 8
  and 15800 = 8 times 1975.
- G2 the Gram matrix is symmetric with diagonal 8, row sum 64 and trace 1536.
- G3 the ten whole eigenvalues carry the multiplicities stated, adding to 136.
- G4 the three quadratic factors have nullity twice their multiplicities, adding to 32.
- G5 the cubic factor has nullity 24, three times its multiplicity 8.
- G6 the fourteen nullities add to 192, the full size of the Gram matrix.
- G7 the fourteen factors multiplied one at a time give the zero matrix.
- G8 the fourteen factors are pairwise different and none of the four non-whole ones
  breaks up over the whole numbers.
- G9 the trace split from the sums of the roots reproduces the measured trace.
- G10 CONTROL: the wrong cubic constant leaves 33024 nonzero entries, and the wrong
  multiplicity at 20 would give 191 rather than 192.
- G11 the shared-piece counts match the Gram matrix off the diagonal, are regular,
  and give 5 matrices against 19 distinct eigenvalues, 10 whole and 9 not.
- G12 the 384 relabellings are distinct, transitive on the 192 pieces, and average
  c_perm against itself to 104.
- G13 cutting side at rank 88: 29, 33, 21, 1, 0 and the sum check 104.
- G14 eight-set side at rank 105: 34, 28, 21, 1, 0 and the sum check 104.
- G15 CONTROL: the all-ones split is a whole split and its cross average is 0.
- G16 every counting value and every average divides through with remainder 0.
- G17 elapsed and peak memory are measured in the run and inside their limits.

Not every gate is mathematically discriminating, and the note does not lean on the
ones that are not. G2 follows from G1 once the row and column sums are fixed, the
first half of G11 restates how the Gram matrix is built, and G17 measures the run
rather than the object. The certificate rests on G3 to G10 and on the two controls.

Measured totals: 20 gates, `TOTAL: PASS=20 FAIL=0`, elapsed under 300 s and peak
resident memory under 500 MB as gated in the run, stdout 2956 characters.

## Boundary

These are computational identities of one finite rebuilt system: they are
measured, not derived from the axioms. Nothing here changes any axiom, primitive
or policy, and
nothing here is offered as physics. No coordinate assignment for any piece appears
in this note or in the runner's output; the pieces are handled by index throughout.

The result in the section on symmetry is a negative result about one route only:
it says that averaging over the relabellings cannot by itself produce 88, 105 or
87, because the seen and unseen spaces are not unions of whole pattern types. It
does not bound what any other route may reach, and it is not evidence that those
numbers lack a structural account. It says where such an account will not be
found, and points at the arithmetic of the tables as the place that stays open.
