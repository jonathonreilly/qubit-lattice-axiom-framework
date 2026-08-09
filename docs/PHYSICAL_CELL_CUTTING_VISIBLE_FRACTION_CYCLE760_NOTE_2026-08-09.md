# Every piece is seen in the same fraction, and what makes that fraction whole is the number the two lattices already named — Cycle 760

Date: 2026-08-09

Authority: none

Audit: unset.

Status: computational identities of the finite cutting system

Claim type: computational identities

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_visible_fraction_cycle760_2026_08_09.py)

Scope: computational identities of the finite cutting system. Every number
below is machine-checked by the paired runner, which rebuilds the cell
complex, the least-volume pieces, the cuttings at the adjacency cost floor,
the cutting-by-piece table and the eight-piece exact covers, then builds the
relabellings got by permuting the four coordinates of the four-cube and
flipping any of them, measures the blocks they cut the pieces into, certifies
an exact whole-number multiple of the orthogonal projector onto the span of
the cuttings, reads its diagonal, finds the smallest whole multiplier that
clears it, sets that multiplier beside the invariant factors of the same
side's Gram matrix, and checks the exact identity tying the two sides
together, gating each quantity in place. Six of the gates carry
controls whose job is to show that each hypothesis the argument leans on is
doing work, and that the routines report something other than the answer
being looked for when the answer is not there. Constitutional effect: none.
This package changes no axiom, no framework Admissibility rule, no primitive,
no policy, and no audit status, and it adds no import and no assumption to
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## What this answers

The object is the unit four-cube on sixteen corners, cut into least-volume
pieces at the adjacency cost floor. There are 15800 such cuttings; between
them they draw on 192 pieces, 24 pieces to a cutting, and each piece lies on
1975 cuttings. Those same 192 pieces admit 192 eight-piece exact covers.

Ask how much of each piece the cuttings see. The answer measured here is the
same fraction at every one of the 192 pieces, 11 over 24, with no piece
favoured over any other. Separately, an earlier cycle of this lane measured
960 as the number controlling how two whole-number lattices built from this
object fail to glue, and read it as the smallest whole number carrying any
labelling of the pieces into a whole-number seen part plus a whole-number
blind part; its own boundary said the value was measured and not derived, and
that nothing there forced it.

This cycle shows two things about that pair of facts. The first fraction is
forced rather than merely measured: it could not have come out any other way
once two hypotheses hold, and both hypotheses are shown here to be doing
work. And the earlier cycle's reading of 960 turns out to be the denominator
of that same fraction, so the two facts are one fact seen twice. What is new
is the numerator, and that the numerator is the same at every piece.

## The symmetry the cost supplies, and the symmetry the answer has

The cost that defines this cutting system does not treat the four coordinates
alike. Adjacency is between nearest neighbours in space, so the cost is
written in the three spatial coordinates and the fourth, the tick, enters
differently. What the cost hands over directly is therefore the 48
relabellings that turn the three spatial coordinates among themselves and may
flip the tick.

Yet all 384 relabellings got by permuting the four coordinates of the
four-cube and flipping any of them carry the whole system onto itself: each
one sends the 15800 cuttings onto the 15800 cuttings and the 192 covers onto
the 192 covers (C2). The system is blind to which of the four coordinates is
called the tick.

The ladder of blocks on the 192 pieces:

| relabellings | what they are | blocks on the 192 pieces |
| --- | --- | --- |
| 24 | proper turns of the three spatial coordinates | 8 of 24 |
| 48 | those, with the tick flip allowed | 4 of 48 |
| 96 | everything that keeps the tick coordinate in place | 2 of 96 |
| 384 | all four-coordinate permutations and flips | 1 of 192 |

Read down the table: the 192 pieces fall into eight blocks of 24 under the
proper turns, four blocks of 48 once the tick flip is allowed, two blocks of
96 under everything that keeps the tick coordinate in place, and one block
only once relabellings that carry the tick coordinate onto a spatial one are
allowed.

Earlier cycles of this lane established, and this cycle uses rather than
re-derives: that the group has order 384; that it is the complete symmetry
group of the cutting system; that it is transitive on the 192 pieces, which
is the bottom rung of the table; and that the 48 relabellings the cost
supplies act with four blocks of 48, which is the second rung. Those cycles
reached the group by a refinement search that produced two extra involutions
beyond the ones the cost hands over, and stated in their own boundary that no
coordinate assignment for any piece appeared in them.

What is new here is the plain identification of that group with permuting the
four coordinates of the four-cube and flipping any of them. That
identification gives the two searched-out involutions a reading: they are
relabellings that carry the tick coordinate onto a spatial one. It also
supplies the two rungs of the table that were not previously in hand, 24
giving eight blocks and 96 giving two. And it yields the consequence that the
table is arranged to display: what the cost supplies is 48 of the 384, and
neither 48 nor 96 is enough for one block. One block needs exactly the
relabellings the cost does not hand over.

## The visibility matrix, exactly

Write the cutting-by-piece table as a matrix on the 192 pieces, one row per
cutting, and let `P` be the orthogonal projector onto the span of its rows.
`P` is a matrix on the 192 pieces. Its diagonal entry at a piece is the
fraction of that piece the cuttings see, and the diagonal sums to the rank.

The rank over the rational numbers is 88, and the row lattice is saturated:
two independently chosen 88 by 88 minors both have absolute value 1, which
forces every invariant factor to be 1 (C4). The cover side is the same
statement at rank 105 with 105 by 105 minors of absolute value 1.

The runner certifies `N = 960 P` as an exact matrix of whole numbers. The
modular step only proposes the lift; what certifies it is arithmetic over the
whole numbers, carried out in Python integer arithmetic so nothing can
overflow:

- `N` is symmetric.
- `N N = 960 N`, which is the projector identity cleared by 960.
- applied to the selected basis rows, `N` returns 960 times them, so it fixes
  the span it is supposed to fix.
- `trace N = 84480`, which is 960 times 88.

Its entries run from -121 to 440 and take 23 different values. Every one of
the 192 diagonal entries is 440, and 440 times 192 is 84480 (C5, C6). The
cover side is certified the same way at multiplier 320 and rank 105: trace
33600, which is 320 times 105, with every diagonal entry 175, entries from
-42 to 175, and 23 different values (C12).

## Why the fraction is forced

The argument is two lines once the previous two sections are in hand.

A relabelling that carries the row set onto itself acts on the pieces by a
permutation matrix that commutes with the projector onto the span of those
rows, because it carries that span onto itself. A permutation matrix
commuting with `N` moves the diagonal of `N` along its own blocks, so the
diagonal is constant on each block. All 384 relabellings carry the row set
onto itself and `N` is unchanged by every one of them (C7). The 384 have one
block. So the diagonal is constant everywhere.

A constant diagonal on 192 pieces summing to 88 leaves no freedom: every
entry is 88 over 192, which in lowest terms is 11 over 24. The same two lines
on the cover side give 105 over 192, which is 35 over 64.

Both hypotheses are load-bearing, and the runner shows it by taking each one
away in turn.

Take away the one block. Two of the four blocks of the 48, taken as two
indicator rows with multiplier 96, give a row set that is carried onto itself
by the 48 but not by the 384. Its projector has rank 2, and its diagonal is 0
on 96 pieces and 2 on the other 96 — two values, not one, even though 96
times the rank over 192 is the whole number 1 (C8). With four blocks instead
of one, constancy fails.

Take away the row set being carried onto itself. The indicator of one single
piece, a coordinate vector rather than a table row, with multiplier 1, has
rank 1 and a diagonal that is 1 at that one piece and 0 at the other 191
(C9). The 384 still have one block; the diagonal is still not constant,
because this row set is not carried onto itself. Neither hypothesis is idle.

## The smallest whole multiplier is the glue exponent

960 clears the cutting-side projector and nothing smaller does: 192, 320 and
480 each leave a fraction (C10). On the cover side 320 clears it and 64 and
160 each leave a fraction (C12).

On each side that number is the largest invariant factor of that side's Gram
matrix, the exponent of the finite group by which two whole-number lattices
fail to glue: 960 on the cutting side, whose chain has 42 nontrivial factors,
and 320 on the cover side, whose chain has 41 (C13). The multiplier and the
exponent are computed by two separate routines, one a search over candidate
multipliers and the other an invariant-factor computation, and on each side
they land on the same number.

The cutting-side 960 re-measures what the preceding cycle already stated in
its own terms. What is new is the equality itself, that the least clearing
multiplier and the largest invariant factor are the same number, that this
needs saturation, and that it holds on the cover side too at 320. What the
constant diagonal adds on top of it is the numerator. Divide each piece into
960 parts and the cuttings see 440 of them, and it is 440 at every piece
rather than 440 on average.

The agreement between multiplier and exponent needs the row lattice to be
saturated, and the runner shows it fails without that. The line through
(1, 2) is saturated, and its largest invariant factor 5 equals its smallest
whole multiplier 5. The line through (2, 0) is not saturated, and gives 4
against 1, which do not agree (C14).

The two sides are not two separate tables whose agreement is a coincidence,
and this note does not claim they are. Gate C17 checks, entry by entry over the whole
numbers, that

    3 N2 = 960 I - N + 5 J

with `I` the identity on the 192 pieces and `J` the all-ones matrix. In
words: what the covers see is exactly what the cuttings do not see, together
with the all-ones direction. The cover-side rank is therefore forced,
105 = 192 - 88 + 1, and with it the cover-side fraction 35 over 64. It is not
a second confirmation of the cutting-side fraction; it is the same fact seen
from the complement.

Why the tie holds is visible in three steps, and the runner gates the first
of them. The all-ones vector is seen by the cuttings: `N` times the all-ones
vector is 960 times the all-ones vector (C17). An earlier cycle of this lane
measured that the blind space of the cuttings — the labellings of the pieces
on which every cutting sums to zero — is exactly the span of the differences
of the 192 exact covers; that measurement is carried in the preceding
cycle's package,
`physical_cell_cutting_blind_lattice_generation_cycle759_2026_08_09.py`.
Differences are perpendicular to the all-ones vector. So what the covers span
is the blind space together with the all-ones direction, which is the
identity above. The 5 in it is 960 divided by 192 and the 3 is 960 divided by
320. The control inside C17 shows the identity discriminates: with 4 J in
place of 5 J it fails.

What the two sides do still give the multiplier claim is two different values
to check it at: 960 and 320 are read off the invariant factors of two
different Gram matrices built from two different pairs of lattices, and the
identity above does not make those two numbers equal. Two values, two linked
spaces.

## Runner

`physical_cell_cutting_visible_fraction_cycle760_2026_08_09.py` rebuilds the
object from the cell complex up and gates eighteen quantities, printing
`TOTAL: PASS=18 FAIL=0`. The construction is inherited from the preceding
cycle's runner, so the pieces, the cuttings, the cutting-by-piece table and
the covers are the same objects, re-derived here rather than imported. Exact
ranks and determinants are computed by fraction-free elimination; basis rows
are selected over a prime field and the resulting whole-number identities are
then checked exactly in Python integer arithmetic.

- C0 the object: 15800 cuttings, 192 pieces, 24 pieces to a cutting, 1975
  cuttings through a piece, 192 exact covers.
- C1 the 384 relabellings exist, are pairwise distinct, and permute the 192
  pieces; they come from the 16 corners of the four-cube.
- C2 each of the 384 carries the 15800 cuttings onto themselves and the 192
  covers onto themselves. Control: one of them followed by a swap of two
  pieces does not.
- C3 the four rungs of the ladder: 8 of 24, 4 of 48, 2 of 96, 1 of 192.
- C4 saturation on both sides: 88 by 88 and 105 by 105 minors of absolute
  value 1, two independent choices each.
- C5 the cutting-side certificate: symmetric, `N N = 960 N`, fixes the rows,
  trace 84480.
- C6 every one of the 192 diagonal entries is 440, so every piece is seen in
  the fraction 11 over 24.
- C7 `N` is unchanged by every one of the 384 relabellings.
- C8 control: two blocks of the 48 with multiplier 96 give rank 2, kept by
  the 48 and not by the 384, diagonal 0 on 96 pieces and 2 on 96.
- C9 control: one piece's indicator with multiplier 1 gives rank 1 and
  diagonal 1 at one piece, 0 at the other 191.
- C10 960 is the smallest whole multiplier on the cutting side; 192, 320 and
  480 each leave a fraction.
- C11 `N` is constant on each of the 104 classes of ordered piece pairs and
  takes 23 different values.
- C12 the cover side: certificate at rank 105, diagonal 175, trace 33600,
  fraction 35 over 64, smallest multiplier 320 with 64 and 160 leaving a
  fraction, constant on the same 104 classes, 23 values.
- C13 the largest invariant factor of each Gram matrix: 960 with 42
  nontrivial on the cutting side, 320 with 41 on the cover side.
- C14 control: the saturated line agrees at 5 and 5; the line that is not
  saturated gives 4 against 1.
- C15 control: the invariant-factor routine returns 1 6 from the diagonal
  2 3 and 2 12 from the diagonal 4 6, which are not its own entries.
- C16 elapsed and peak memory, both measured in the run.
- C17 the tie `3 N2 = 960 I - N + 5 J` over the whole numbers, `N` times the
  all-ones vector equal to 960 times it, and 192 - 88 + 1 = 105. Control:
  the same identity with 4 J in place of 5 J fails.

Measured totals: 18 gates, `TOTAL: PASS=18 FAIL=0`, elapsed under 300 s, peak
resident memory under 500 MB, stdout 2982 characters.

## Boundary

- **Everything here is a count about one finite object.** The cutting system
  is a finite combinatorial object and every statement made about it is a
  count or a whole-number identity between counts. Nothing here bears on any
  physical claim.
- **The one-block fact is used, not claimed as new.** That the group has
  order 384, that it is the complete symmetry group of the cutting system,
  that it is transitive on the 192 pieces, and that the 48 relabellings the
  cost supplies give four blocks of 48 were all established in earlier cycles
  of this lane. This cycle measures those rungs again in its own runner so
  that the argument stands on gated numbers, but claims none of them as new.
  What is new is the identification of the group with the coordinate
  permutations and flips of the four-cube, and the two rungs at 24 and 96.
- **The identification is a statement about this cutting system.** That the
  full symmetry group is the coordinate permutations and flips of the
  four-cube says something about this object and carries no claim about the
  framework's Admissibility rule, about any primitive, or about any other
  object.
- **The reading of 960 is a reading of a whole-number fact, and it is not new
  here.** That 960 is the smallest number of parts a piece must be divided
  into was already stated by the preceding cycle of this lane in its own
  terms, and is re-measured here rather than first established here. It is
  measured, not derived from anything outside the object, and nothing here
  says why the exponent is 960 rather than some other number. What this cycle
  adds to it is the numerator 440 and the fact that the numerator is the same
  at every piece.
- **The tie between the sides rests on one imported measurement.** The
  identity `3 N2 = 960 I - N + 5 J` is gated here directly, so it stands on
  its own. The account of why it holds uses the earlier cycle's measurement
  that the blind space is the span of the cover differences, which is not
  re-derived here.
- **Saturation is checked by a sufficient condition.** A minor of absolute
  value 1 proves the lattice is saturated; failing to find one would prove
  nothing. Every witness reported here succeeded, so the asymmetry does not
  bite, but it bounds what the technique could be used to deny.
- **No claim is made that the cost's indifference to which coordinate is the
  tick has any consequence for emergent time.** What is shown is that this
  particular finite system does not record the distinction: the 384
  relabellings carry it onto itself, and the fraction each piece is seen in
  is the same whether or not a relabelling moves the tick.

## Next

Three things are open and reachable from here.

Which of the 23 entry values of `N` sit on which of the 104 classes of
ordered piece pairs. `N` is constant on every class, so the 23 values
partition the 104 classes, and the shape of that partition is a direct next
measurement.

Whether the 104 classes and the 104 blind dimensions the preceding cycle
measured are related or merely numerically coincident. Two counts of 104
arising from the same table over different constructions is the kind of
agreement that either has a reason or does not, and nothing here decides
which.

The structure behind the parts of the glue group. The cutting side has 42
nontrivial invariant factors and the cover side 41, with the two largest
being 960 and 320. A decomposition of the 192-dimensional space that named
those parts one by one would say what the exponent counts, which is the
question the reading of 960 leaves open.
