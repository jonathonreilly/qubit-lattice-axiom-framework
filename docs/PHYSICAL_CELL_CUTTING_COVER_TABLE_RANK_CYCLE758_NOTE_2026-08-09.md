# Why the cuttings are blind in 104 directions: it is the rank of the cover table, less the all-ones direction — Cycle 758

Date: 2026-08-09

Authority: none

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_cover_table_rank_cycle758_2026_08_09.py)

Scope: computational identities of the finite cutting system. Every number
below is machine-checked by the paired runner, which rebuilds the cell
complex, the least-volume pieces, the cuttings at the adjacency cost floor,
the eight-piece exact covers, the cover-by-piece table, its exact rational
rank and nullity, the exact ranks of the two products of that table with its
transpose, and the exact whole-number part of the spectrum of those products,
gating each quantity in place. Two of the gates are controls whose job is to
show the spectrum scan is neither vacuous nor canned. Constitutional effect:
none. This package changes no axiom, no framework Admissibility rule, no
primitive, no policy, and no audit status, and it adds no import and no
assumption to `MINIMAL_AXIOMS_2026-06-29.md`.

## What this answers

The object is the unit four-cube on sixteen corners, cut into least-volume
pieces at the adjacency cost floor. There are 15800 such cuttings; between
them they draw on 192 pieces, 24 pieces to a cutting, and each piece lies on
1975 cuttings. A vector on the pieces is *blind* to the cuttings when every
cutting sums it to zero. Two cycles back the blind space was measured at
exactly 104 dimensions and identified with the span of the differences of the
192 eight-piece exact covers; since then, three separate attempts to explain
that 104 through the symmetries of the cube have each fallen short, the last
of them finding that no symmetry orbit reaches across it at all. The
preceding cycle left the question open in its own words: why the covers
differ inside exactly 104 dimensions.

This cycle answers it, in the sense that a question is answered when it is
reduced to a smaller one. **104 is not an independent number.** It is the
rank of the 192 by 192 cover-by-piece table, less one, and the one is the
all-ones direction on the pieces. Both steps are derived below from gated
inputs, not measured; what is measured is the rank, 105, and every input the
derivations use. The question "why 104" is now the question "why 105", asked
of a 192 by 192 table instead of a 15800 by 192 one.

The second half of the cycle takes the sharing table apart spectrally, since
that is where a rank of 105 would have to come from. The whole-number part of
the spectrum is settled exactly: ten eigenvalues with exact multiplicities,
accounting for 136 of the 192, with the remaining 56 not rational.

## The blind space is the cover table applied to the zero-sum covers

Write M for the cover-by-piece table: 192 rows, one per exact cover, 192
columns, one per piece, a one where the cover uses the piece. The runner
gates that M is 8-regular on both sides, row sums and column sums alike (C2).

**Derived here, from gated inputs.** Every cover meets every cutting exactly
once (C1), so the difference of two covers is summed to zero by every cutting:
the differences are blind. A general element of their span is a combination
of covers whose coefficients add to zero, so the span is exactly the image of
the zero-sum coefficient vectors under M transposed. Its dimension is
therefore 191 less the dimension of the part of the kernel of M transposed
that lies among the zero-sum vectors.

**That kernel lies wholly among the zero-sum vectors, by row-regularity.**
If a combination of covers is annihilated by M transposed, add up its 192
piece entries: each cover contributes its coefficient once for each of the 8
pieces it holds, so the total is 8 times the sum of the coefficients, and it
is zero. Hence the sum of the coefficients is zero. The runner gates this in
its dual form (C6): stacking one all-ones cover row onto M transposed leaves
the rank at 105, so that row already sits in the row space, and every kernel
vector is orthogonal to it.

The dimension of the blind space is then 191 less the whole nullity of M
transposed, with nothing to subtract off. The runner measures that nullity as
87 (C7), and 191 less 87 is 104 — the same 104 the preceding cycles measured
two other ways. Equivalently, since the nullity is 192 less the rank,

> dimension of the blind space = rank of the cover-by-piece table, less one.

## The one extra dimension is the all-ones piece direction

The step above leaves one dimension unexplained: the row space of M has 105
dimensions and the blind space, which sits inside it, has 104. What is the
extra one?

**Derived here, from gated inputs.** Adding up all 192 rows of M gives 8 at
every piece (C3), because each piece lies in 8 covers — itself a forced count
from the preceding cycle, where 192 equals 24 times 8. So the all-ones piece
vector is one eighth of a combination of covers, and lies in the row space.
It is not blind: the cutting table sends it to the single value 24 at every
one of the 15800 cuttings (C4), and 24 is not zero. So the row space of M is
the blind space together with the all-ones piece direction, and the two meet
only at the origin:

> 105 = 104 + 1.

The two steps use opposite regularities, which is worth recording. The first
uses row-regularity, that each cover holds 8 pieces. The second uses
column-regularity, that each piece lies in 8 covers — the count the preceding
cycle showed to be forced rather than accidental. The blind space is bounded
above by the covers and pinned from below by the all-ones direction, one
regularity at each end.

## The rational part of the sharing spectrum, exactly

Write S for the cover-side sharing table, M times M transposed, whose entry
counts the pieces two covers share, and N for the piece-side table, M
transposed times M. The runner gates that M, S and N all have exact rational
rank 105 (C5, C8), so the rank question can be asked of a symmetric table.

Three facts make the whole-number part of the spectrum of S exactly
determinable in finite work, and the runner states each in place before using
it (C9):

- S is an integer table times its own transpose, so no eigenvalue is below 0.
- The largest row sum of S is 64, so no eigenvalue is above 64.
- A rational eigenvalue of an integer symmetric table is a root of a monic
  integer polynomial, hence an algebraic integer, hence a whole number.

So a scan of the whole numbers 0 to 64 settles the rational part in full: it
is a complete test, not a sample of one. The scan is made cheap by a fourth
fact, also stated in place: the rank over the prime field 1000003 never exceeds the rank over the
rationals, so a whole number with zero nullity over that field is ruled out
with no exact work at all. Every whole number that survives the cheap pass is
then confirmed by fraction-free integer elimination, and only the exact
multiplicity is reported. The prime field rules candidates out; it never
rules one in.

The result:

| eigenvalue | 0 | 2 | 4 | 8 | 10 | 12 | 16 | 20 | 24 | 64 |
|---|---|---|---|---|---|---|---|---|---|---|
| multiplicity | 87 | 8 | 8 | 3 | 8 | 6 | 2 | 10 | 3 | 1 |

Counted with multiplicity these are 136 of the 192 eigenvalues, so **56 of
them are not rational**. The 0 with multiplicity 87 is the nullity used
above; the 64 with multiplicity 1 is the largest row sum, taken once.

Two independent totals confirm the list rather than restate it. The trace of
S is 1536: each diagonal entry counts the pieces a cover shares with itself,
which is 8, over 192 covers, and the whole-number eigenvalues supply 592 of
that, leaving 944. The trace of the square is 36096, of which the whole
numbers supply 12352, leaving 23744. Both leftovers are strictly positive, as
they must be when eigenvalues that are not rational are present, and neither
total is reached by the whole numbers alone (C11). A list that had missed an
eigenvalue or inflated a multiplicity would have to miss these two totals in
a coordinated way.

The scan itself is controlled on both sides (C12, C13). On the positive side
it is run against the sixteen corners of the four-cube joined when they differ
in one coordinate, whose spectrum is fixed before any measurement is taken:
eigenvalue 4 once, 2 four times, 0 six times, -2 four times, -4 once, all 16
whole. The scan recovers exactly that. On the negative side, adding 1 at one
symmetric pair of that control changes the whole-number spectrum and drops the
count of whole eigenvalues to 8 of the 16; the gate requires only that the
spectrum change and the count fall, hard-coding no perturbed answer. So the
scan is not returning a canned list, and it is sharp enough to notice a
single-pair change.

## The two sharing tables have one spectrum, and the spectrum cannot see the difference

The piece-side table N returns the same whole-number spectrum as S, entry for
entry and multiplicity for multiplicity (C10). This is forced, not found: a
table times its transpose and the transpose times the table share their
nonzero spectrum, and both are 192 by 192 here, so the multiplicity at 0
agrees as well. The gate is a consistency check on the machinery.

Its content is the contrast. The preceding cycle proved that S and N are *not*
related by any relabelling of the 192 covers onto the 192 pieces, by exhibiting
off-diagonal multisets that differ. So the two tables are cospectral and not
permutation-similar. **The spectrum is blind to exactly the asymmetry that the
sharing counts detect.** Anything built on the spectrum alone — including any
future account of the rank 105 built that way — will not distinguish the cover
side from the piece side, and must not be read as having done so.

## Runner

`physical_cell_cutting_cover_table_rank_cycle758_2026_08_09.py` rebuilds the
object from the four-cube and gates 15 quantities. The construction is the
preceding cycle's, byte for byte, through the exact covers; everything after
is new.

- C0, C1, C2 — the object: pieces per cutting and cuttings per piece each
  constant; each of the 192 sets meets every cutting exactly once; the
  cover-by-piece table 8-regular on both sides.
- C3, C4 — the inputs to the second derivation: all 192 rows add to 8 at every
  piece, so the all-ones piece vector is in the row space; the cutting table
  sends it to the single nonzero value 24.
- C5 — exact rational rank of the cover-by-piece table 105, of its 191 cover
  differences 104, difference exactly 1.
- C6, C7 — the input to the first derivation: the all-ones cover row raises no
  rank when stacked on the transposed table; exact nullity 87, and 191 less 87
  is 104.
- C8 — exact rank 105 for the cover-side and piece-side sharing tables alike.
- C9, C10 — the whole-number spectrum of both sharing tables, by a complete
  scan over 0 to 64 with prime-field rejection and exact confirmation; 136 of
  192 whole, 56 not rational.
- C11 — the trace 1536 splitting as 592 plus 944 and the trace of the square
  36096 splitting as 12352 plus 23744, with both leftovers positive.
- C12, C13 — positive and negative controls on the scan.
- C14 — time and memory inside allowance, both measured in the run.

`TOTAL: PASS=15 FAIL=0`.

## Boundary

- **The rank 105 is measured, not derived.** This cycle reduces 104 to it and
  supplies the one-dimensional gap exactly; it does not say why the table has
  that rank. Read the result as a reduction, not an explanation.
- **The two derivations are done in this note, not by the runner.** The runner
  gates their inputs — the two regularities, the row-space memberships, the
  nullity, the nonzero image — and the counting step from those inputs to
  "104 equals rank less one" is prose here. The prose is short and the inputs
  are each gated in place, but the arithmetic itself is not machine-checked.
- **Cospectrality of the two sharing tables is forced,** and is gated only as
  a consistency check on the machinery. It is not evidence about the object.
- **The 56 eigenvalues that are not rational are not identified here.** Their
  count and their contribution to the two totals are exact; their values,
  their fields, and their multiplicities individually are untouched.
- The whole-number scan settles the *rational* part of the spectrum only, and
  its completeness rests on the three stated facts, each of which is a
  property of this table rather than a general one.
- Nothing here bears on any physical claim. The object is a finite
  combinatorial one and every statement about it is a count.

## Next

The rank question is now sharper than it was, and smaller in three ways.

It lives on a 192 by 192 table rather than a 15800 by 192 one. It can be asked
of a symmetric table, since the cover-by-piece table and both sharing tables
carry the one rank. And it is entirely a question about the kernel: the rank
is 192 less the multiplicity of 0, that multiplicity is exactly 87, and the 56
eigenvalues that are not rational are therefore all nonzero and play no part
in it. **Why is 0 an eigenvalue of the sharing table exactly 87 times?** —
that single question now carries the whole of the 104.

Two structural leads sit next to it. The whole-number eigenvalues come with
multiplicities 8, 8, 3, 8, 6, 2, 10, 3 and 1 away from the kernel, and a
decomposition of the cover space that explains those multiplicities would very
likely name the kernel too. Separately, the preceding cycle found the closed
refinement of the sharing classes with the fewest parts; whether the products
of that refinement carry the 104-dimensional span is still open, and it is the
natural place to look for the decomposition, since the sharing classes
themselves are known not to close under multiplication while that refinement
does.

Also still open from the preceding cycles: the combinatorial symmetry group of
the sharing structure, and whether it exceeds the cube symmetries that have now
been shown three separate ways to be too coarse for this rank.
