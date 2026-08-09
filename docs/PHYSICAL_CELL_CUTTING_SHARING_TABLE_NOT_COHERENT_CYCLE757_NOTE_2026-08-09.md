# The sharing table of the eight-piece exact covers is regular, and its products do not stay inside its span — Cycle 757

Date: 2026-08-09

Authority: none

Audit: unset.

Status: computational identities of the finite cutting system

Claim type: computational identities

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_sharing_table_not_coherent_cycle757_2026_08_09.py)

Scope: computational identities of the finite cutting system. Every number
below is machine-checked by the paired runner, which rebuilds the cell
complex, the least-volume pieces, the cuttings at the adjacency cost floor,
the eight-piece exact covers, the table of how many pieces two covers share,
the products of the classes of that table, the refinement of those classes
with the fewest parts that carries its own products, and the exact ranks of
the differences of the covers, gating each quantity in place. Two of the
gates are controls whose job is to show the closure test is not vacuous on
either side. Constitutional effect: none. This package changes no axiom, no
framework Admissibility rule, no primitive, no policy, and no audit status,
and it adds no import and no assumption to
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## What this answers

The object is the unit four-cube on sixteen corners, cut into least-volume
pieces at the adjacency cost floor. There are 15800 such cuttings; between
them they draw on 192 pieces, 24 pieces to a cutting, and each piece lies on
1975 of the cuttings. Exactly 192 sets of eight pieces are used at most once
by any cutting, and each of those meets every one of the 15800 cuttings
exactly once, so each is an exact cover of the cutting system. The preceding
cycle showed that the differences of those 192 exact covers are precisely the
space the cutting table cannot see, and then asked for the profile of how many
pieces two of them share to be derived rather than measured, on the reading
that the profile is the cover family's multiplication table and would carry
the space with it.

This cycle goes to that table. It reports two things the table gives up for
free and one thing it refuses to be.

## Eight is forced, and eight is the largest size at which it can happen

The runner gates the three inputs — 15800 cuttings, 1975 cuttings through each
piece, and the 192 sets of eight pieces no cutting uses twice. The counting
step below is done here in the note from those gated inputs; the runner does
not perform it, since its search is over sets of eight only.

Call a set of pieces *free* when no cutting uses two of them. Each piece of a
free set lies on 1975 cuttings, and freeness says that for two pieces of the
set those two collections of cuttings are disjoint. So a free set of size k
occupies 1975 times k distinct cuttings out of the 15800 available, which
forces 1975 times k to be at most 15800. Since 15800 is 8 times 1975 exactly,
a free set has at most 8 pieces.

At exactly 8 the inequality is tight. The eight disjoint collections of 1975
cuttings then account for all 15800 cuttings with nothing left over, so every
cutting is met, and disjointness says it is met exactly once. **A free set of
eight pieces is therefore an exact cover automatically, and eight is the
largest size at which a free set can exist at all.** The exact-cover property
the preceding cycle measured is not a coincidence of this geometry; it is
forced by 15800 being 8 times 1975.

The same reasoning fixes the other side of the table. Fix a cutting; it uses
24 pieces, and each of the 192 covers contains exactly one of them, so sending
a cover to its unique piece on that cutting is a well-defined map from the 192
covers onto those 24 pieces. A cover through a given piece meets the cutting
at that piece and nowhere else, so the covers landing on a given piece are
exactly the covers containing it. The 192 covers therefore split into 24
equal parts, and each piece lies in 8 covers. **The cover-by-piece table being
8-regular on the piece side is forced too, not a second coincidence.** The
runner measures both row sums and column sums to be 8 and finds them so.

## The table is as regular as it could be

Two exact covers share 0, 1, 2 or 4 pieces and never 3. The counts are 157,
20, 10 and 4, and they are **the same for every one of the 192 covers**, not
merely the same on average: standing on any cover, the view of the rest of the
family is identical. The runner checks all 192 rows rather than reading one
off.

The piece side of the same table is regular too and is a different shape: two
pieces share 0, 1, 2, 3 or 4 covers with counts 158, 18, 10, 2 and 3, the same
for every piece. The value 3, missing between covers, is present between
pieces.

That difference does more than break an aesthetic parallel. The cover-by-piece
table has 192 rows, 192 columns, and 8 in every row sum and every column sum,
which invites the guess that some relabelling of the pieces makes it
symmetric — that covers and pieces are the same objects seen twice. **No
relabelling does.** If a permutation T made the table symmetric after
relabelling, then the cover-side sharing matrix would equal T transpose times
the piece-side sharing matrix times T, so the two would be permutation-similar
and would have the same off-diagonal multiset. Those multisets are 0 with
multiplicity 30144, 1 with 3840, 2 with 1920 and 4 with 768 on the cover side,
against 0 with 30336, 1 with 3456, 2 with 1920, 3 with 384 and 4 with 576 on
the piece side. They differ. This is a proof, not a search that came up empty.

## The products do not stay inside the span

Write AI for the identity relation and A0, A1, A2, A4 for the relations "share
exactly this many pieces". The runner gates that these five are symmetric,
zero-one, pairwise disjoint, add up to the all-ones matrix, and that AI is
exactly the "share 8" relation, with valencies 1, 157, 20, 10 and 4. That is
everything one would want of a multiplication table except the multiplication.

**The multiplication is not there.** The product of A0 with itself, in exact
integer arithmetic, takes 11 different values on the class A0: 122, 124, 125,
126, 127, 128, 129, 130, 131, 132 and 134. Concretely, the pairs (0,20) and
(0,21) both share 0 pieces, yet the product carries 134 on one and 132 on the
other. So the number of covers sharing nothing with the first and nothing with
the second is not a function of how much the first and second share. There is
no table of numbers indexed by the five classes that reproduces these
products, because the products are not constant on the classes.

The algebra is not commutative either: A0 times A1 and A1 times A0 differ at
entry (0,6), 16 against 15.

Two controls establish that the test is discriminating on both sides. On the
positive side, the 16 corners of the four-cube with the five relations "differ
in exactly this many coordinates" are built from scratch inside the runner and
put through the same function; all 25 of its products come back constant on
all 5 classes, one of them the number 4, so the test can return that the
products stay inside the span. On the negative side, moving a single symmetric
pair of that control from the distance-2 relation to the distance-1 relation —
still a symmetric partition of all ordered pairs — makes the test report a
product taking 3 values on one class. The test neither accepts everything nor
refuses everything.

## How much finer a working table would have to be

If the five classes do not carry their own products, one can ask for the
coarsest partition that does. Refining each ordered pair by the multiset over
all intermediate covers of the pair of colours it sees, and repeating until
the count stops growing, gives classes by round of 5, then 76, then 120, then
120. **The closed refinement with the fewest classes has 120 classes**, of
sizes 192 with multiplicity 48 and 384 with multiplicity 72, and the five
original relations split into 1, 100, 10, 6 and 3 parts.

Since iterated refinement of this kind returns the coarsest stable partition
refining what it is given, 120 is a floor: no partition refining the five
sharing classes and carrying its own products has fewer than 120 classes. The
smallest working multiplication table on this family is 24 times as fine as
the sharing classes, and it splits every one of them except the identity. A
derivation of the sharing profile of the kind the preceding cycle asked for
would have to run through an object of that size, not through five numbers.

## What the symmetries reach

All 48 proper cube symmetries send exact covers to exact covers, and they
leave 5 orbits on the 192 covers, of sizes 24, 24, 48, 48 and 48. Taking the
differences of each orbit's covers against the first cover of that orbit and
computing the exact rank over the rationals by integer elimination — no
floating point and no bounded arithmetic anywhere — gives, as orbit size
against rank: 24 against 23, 48 against 47, 24 against 23, 48 against 35, and
48 against 29. All 192 covers together give exactly 104.

So no single orbit of the symmetry group reaches across the space the cuttings
cannot see. Three of the five already sit at the largest rank their size
permits and still fall short: an orbit of 24 covers cannot give more than 23
independent differences however it sits, and one of 48 cannot give more than
47. The other two size-48 orbits, at 35 and at 29, fall short of even that
ceiling. The preceding cycle
found that each *sharing class*, taken alone, already spans all 104
dimensions. Symmetry orbits do not; incidence classes do.

The 104 here is an exact rational rank computed by fraction-free integer
elimination, arrived at independently of the preceding cycle's two-sided
bounded-arithmetic argument, and it agrees with it.

## Runner

`TOTAL: PASS=15 FAIL=0`, 3345 characters of output, under 30 s and under
500 MB peak, both measured in the run. Fifteen gates, contiguous, each
measuring in place. What the gates defend:

- the cell complex, the pieces and the cuttings are rebuilt from scratch, and
  the two independent counts of the incidences are gated against each other;
- the exact-cover property is measured, not assumed: the eight-piece sets are
  found by the condition that no cutting uses two of their pieces, and then
  separately gated to meet every cutting exactly once;
- the regularity claims are gated across all 192 rows on each side, so a
  quantity read off one row cannot pass for a constant;
- the asymmetry of the two sides is gated on the two off-diagonal multisets
  differing, which is the exact hypothesis the permutation-similarity argument
  needs, with no search anywhere;
- the closure test is gated to discriminate on both sides, by a positive
  control built from scratch that it must accept and a one-pair perturbation
  of that same control that it must reject, so the negative result on the
  sharing classes is not a test that refuses everything;
- the refinement is gated on its round-by-round counts, its final class sizes
  with multiplicities, and how the five relations split, so a refinement that
  silently stopped early cannot pass;
- every rank is exact integer arithmetic, and the orbit ranks are gated both
  against the whole space and against each orbit's own size.

## Boundary

The negative is about the five sharing classes and is stated at that scope:
their products are not constant on them, so those five classes carry no
multiplication table. It is not a claim that the family has no useful algebra
— the 120-class refinement does carry its own products, and this note does not
measure how that refinement acts on the space the cuttings cannot see. Whether
that finer table carries the span is open and is the natural next object.

The 120 classes are not claimed to be the orbits of any group. The
combinatorial symmetry of the sharing structure is not measured here, so
whether it is larger than the 48 geometric symmetries is open. Why the covers
differ inside exactly 104 dimensions is still not derived; this cycle confirms
the number exactly and relocates none of it.

## Next

Measure whether the 120-class refinement's multiplication table carries the
span, which is the object this cycle's negative points at. Measure the
combinatorial symmetry group of the sharing structure and compare it with the
48 geometric ones. And take the forced count in this note further: 15800 being
8 times 1975 fixed the size of a free set and forced the exact-cover property
at that size, so ask which further counts of the cutting system are fixed the
same way rather than measured.
