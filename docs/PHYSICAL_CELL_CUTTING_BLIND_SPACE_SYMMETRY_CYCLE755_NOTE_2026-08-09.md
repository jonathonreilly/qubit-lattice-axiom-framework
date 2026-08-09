# The space the cuttings cannot see is not built from whole symmetry blocks — Cycle 755

Date: 2026-08-09

Authority: none

Audit: unset.

Status: computational identities of the finite cutting system

Claim type: computational identities

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_blind_space_symmetry_cycle755_2026_08_09.py)

Scope: computational identities of the finite cutting system. Every number
below is machine-checked by the paired runner, which rebuilds the cell
complex, the cuttings, the readings, the piece sharing table and the group of
symmetries from scratch and gates each quantity in place. Constitutional
effect: none. This package changes no axiom, no framework Admissibility rule,
no primitive, no policy, and no audit status, and it adds no import and no
assumption to [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## What this answers

The object is the unit four-cube on sixteen corners, cut into least-volume
pieces at the adjacency cost floor. There are 15800 such cuttings. Between
them they draw on 192 pieces, 24 pieces to a cutting, and each piece lies on
1975 of the cuttings. From that, the piece sharing table: the 192-by-192
integer table whose entry at a pair of pieces counts the cuttings using both,
its diagonal constant at 1975. Call a weighting of the 192 pieces seen if it
lies in the image of that table, and blind if the table sends it to zero —
blind meaning that every one of the 15800 cuttings, totalled piece by piece
against the weighting, comes out zero.

The preceding cycle measured the exact rational rank of the sharing table as
88, so the blind space has dimension 104 and the two add back to 192. That
cycle recorded the rank as a measurement and said in as many words that it did
not derive it. This cycle asks the next question: does the group of 384
symmetries of the whole system — the piece permutations that carry cuttings to
cuttings — single the blind space out on its own? Is the blind space a
symmetry object? The answer is no, and the obstruction is measured twice, by
two routes sharing no machinery, both returning 21.

## Two results against interest, first

**The blind space is not a symmetry object, so the route this cycle was opened
to walk does not go through.** The plan was to derive 88 from the group: if
the blind space were a sum of whole same-type blocks of the 384 symmetries,
its dimension would be fixed by the trace counts of the group alone, and 88
would follow as the complement. A subspace of a permutation module is a sum of
whole same-type blocks exactly when no same-type block appears both in it and
in its complement — exactly when the averaged product of the two trace counts
is zero. Here that averaged product is 21. Twenty-one same-type parts, counted
with multiplicity, are shared between the seen space and the blind space. So
the blind space is not a sum of whole blocks, and the trace counts of the 384
symmetries do not pick it out.

**The failure count of the natural basis overstated the obstruction.** The
maps commuting with every symmetry have the pair-orbit matrices as a basis. Of
those 104 matrices, only 2 carry the blind space into itself on their own, and
both of those are permutation matrices lying in the group of 384 already; the
other 102 miss, by as much as 12738 in a single entry. The first reading this
cycle made of its own probe was that 102 failures out of 104 means the space
of commuting maps preserving the blind space is tiny. That reading is wrong.
Of the 104 dimensions, 83 preserve the blind space. The natural basis is badly
adapted to the splitting, and the failure count of a basis is not the
dimension of a subspace. The correction is set down here rather than quietly
dropped, because the mistake was this cycle's own.

## Reading the trace of a symmetry on the blind space

Take a basis of the blind space in reduced row echelon form: 104 rows across
192 columns, with a set of pivot columns on which the basis restricts to the
identity. A symmetry acts by moving coordinates. The trace of that symmetry on
the blind space is then the sum, over the 104 basis rows, of the single basis
entry standing in the place the row's own pivot column was moved to — one
entry read per row, with no projector formed at all. The trace of each
symmetry costs 104 lookups. That is what makes this whole cycle cheap enough
to run inside its allowance.

The identity itself is elementary; it is what reduced row echelon form is for.
What the runner supplies is not the identity but the check on it — that the
basis really is in the form the identity needs, and that the one-entry-per-row
sum agrees with the trace of the formed matrix on every one of the 384
symmetries, with no disagreement anywhere.

## The pair-orbit count 104, by three routes

The group has 104 orbits on ordered pairs of pieces, and the runner reaches
that number three ways.

- The averaged square of the fixed-piece count over the 384 symmetries is 104.
- The direct count of orbits on ordered pairs is 104.
- The group has one orbit on the pieces, and the stabiliser of a piece has
  order 2 whose non-identity element fixes 16 pieces; so twice the pair-orbit
  count is 192 plus 16.

Three routes, one number. The third is the one worth keeping, because it ties
the count to the structure of the group — one orbit on the 192 pieces, a
stabiliser of order 2, that stabiliser's other element fixing 16 pieces —
rather than to a sweep over all 384 symmetries.

## What the seen and the blind space share

Averaging the products of the trace counts over the group, block by block,
gives three numbers: seen with seen 29, seen with blind 21, blind with blind
33. They rebuild the pair-orbit count, the cross term entering twice:
29 + 21 + 21 + 33 = 104. That the four add back to 104 is the arithmetic check
that the splitting of the 192 weightings into seen and blind is fully
accounted for, with no part of the module missing from the two sides.

The lead result is the middle number. 21 is not zero, so some same-type block
appears in both the seen space and the blind space, and the blind space is
therefore not a sum of whole same-type blocks of the 384 symmetries. The exact
consequence, and nothing past it: the splitting of the 192 weightings into
same-type blocks under the group is coarser than the seen/blind splitting; the
group data alone leaves the choice inside the 21 shared parts open; and so the
rank 88 is not fixed by the trace counts of the group. This is not a statement
that the group forbids a blind space of dimension 104 — the group plainly
permits this one, which exists and is carried into itself by every symmetry.
It is a statement that the group does not single this one out.

Also gated here: the symmetries have one orbit on the pieces, so the constant
weighting is the one symmetric weighting. It is seen and it is not blind, and
the blind space holds no constant weighting at all — the trivial part appears
once on the seen side and not at all on the blind side.

## The maps that commute with every symmetry

The linear maps on the 192 weightings that commute with every one of the 384
symmetries span 104 dimensions, and the pair-orbit matrices are a basis for
them. That is why the pair-orbit count is the number that matters here.
Splitting the module into blind plus seen splits that algebra into four
blocks: maps of blind to blind, maps of seen to seen, and the two cross
blocks. Their dimensions are exactly the four averaged products already
listed — 33, 29, 21 and 21. That the dimensions over the rationals are the
same numbers the averaged products give, rather than smaller ones, is because
a space of commuting maps is the solution set of a system of rational linear
equations, and the dimension of such a solution set does not change when the
field is widened.

A commuting map carries the blind space into itself exactly when its
blind-to-seen block vanishes. So the maps that both commute with every
symmetry and carry the blind space into itself form a subspace of dimension
104 minus 21, that is 83. Because the equivalence is exact, the 21 is the
whole of what stands in the way and not a symptom of something larger.

The second route reaches the same 21 without touching a trace count at all. In
coordinates, a map carries the blind space into itself exactly when the
sharing table, times the map, times the transpose of the blind basis is zero:
the blind space is what the sharing table kills, and the transpose of the
blind basis has the blind space as its column span. That condition is linear
in the map, so its rank on the 104-dimensional commuting algebra is
104 minus 83 = 21. The runner computes that rank by elimination over a prime
field on the flattened residuals of the 104 pair-orbit matrices, and gets 21.
A prime-field rank is a floor on the rational rank, hence a ceiling on the
preserving dimension, so this route meets the count from the other side.

The agreement is what discriminates here. One route averages products of trace
counts over 384 symmetries; the other does elimination on residual matrices in
a different arithmetic, and the two share none of their machinery. Either one
alone could be a coding error and still look clean. Both landing on 21 is the
check that neither is.

## One least exchange orbit reaches 60 of the 104 blind dimensions

A least exchange is a four-for-four: four pieces weighted plus one, four
pieces weighted minus one, every other piece zero. The preceding cycle settled
that no exchange of two pieces for two, and none of three for three, is blind,
so four for four is the smallest shape available. Take one such exchange. It
is blind — no cutting sees it. Its images under the 384 symmetries are 192
distinct signed vectors, and the runner checks every one of the 192 blind
against all 15800 cuttings.

Their span has dimension 60 of the 104 blind dimensions, which leaves 44. That
span is carried into itself by every symmetry and holds no constant weighting.
Its averaged products: with itself 13, with the rest of the blind space 8,
across 6, and with the seen space 11; and 13 + 6 + 6 + 8 = 33 rebuilds the
blind-with-blind count.

So blindness is not generated by this orbit. 44 dimensions of the blind space
are not reached by it, and what does reach those 44 is open — this cycle does
not name a generator for them. Whether a four-for-four exchange exists outside
this orbit was not swept, so the sharper statement, that least exchanges as a
class fall short of generating blindness, is not made here.

## What the runner gates

32 gates, `TOTAL: PASS=32 FAIL=0`, in under 100 s and under 2500 MB, with
output under 6000 characters. What is checked, and how:

- the group is rebuilt from scratch and its order 384 gated, along with its
  one orbit on the 192 pieces;
- the piece sharing table is built in exact integers, with the constant
  diagonal 1975 gated and the largest share of two pieces gated at 1266;
- the rank 88 comes from exact rational elimination, not from a numerical
  threshold;
- the symmetry check — that each of the 384 fixes the sharing table and
  carries the blind space into itself — runs in exact integers and again in a
  bounded second arithmetic, and the two agree;
- every averaged product is gated to come out a whole number with remainder
  zero, which a wrong trace count would not give;
- the prime-field elimination that returns 21 the second time is a separate
  arithmetic from everything else in the file.

## Boundary and honest read

**Derived, and holding for this system:** the four-block splitting of the
commuting algebra along the blind-plus-seen splitting, and hence the 83; the
equivalence between a commuting map carrying the blind space into itself and
the vanishing of its blind-to-seen block; the trace identity that reads one
basis entry per row; and the fact that a subspace of a permutation module is a
sum of whole same-type blocks exactly when the averaged product of its trace
count with its complement's is zero. These are the general parts, and they are
what the measured numbers are fed into.

**Measured on this object, and not claimed beyond it:** the group order 384;
the rank 88 and the blind dimension 104; the averaged products 29, 21 and
33 and the pair-orbit count 104; the span 60 and the gap 44; the 2 of 104 and
the 12738. As in the preceding cycle, the rank is a measurement and not a
derivation — and this cycle now adds that the trace counts of the symmetries
do not derive it either.

**Where a gate follows from its premise, that is disclosed.** The rebuild of
33 from 13, 6, 6 and 8 follows by algebra once the splitting is right; it is
not independent evidence for the splitting. The measured content there is that
every averaged product came out a whole number with remainder zero, which a
wrong trace count would not give. The same applies to the rebuild of 104 from
29, 21, 21 and 33.

**What is not swept.** Whether every blind vector supported on eight pieces
lies in the single orbit of 192 was not swept; the count of eight-piece
supports is far past what this runner would carry. What generates the 44 blind
dimensions the least exchanges do not reach is open. And nothing here derives
88 from anything — this cycle narrows where such a derivation could come from,
and that is the whole of what it does.

## Next

Three paths open from here. Find the smallest blind vectors lying outside the
60-dimensional span, since those are what name the missing generators, and
their supports are the first thing to look at. Ask whether the 60-dimensional
span is exactly the span of all blind vectors supported on eight pieces, which
would say the least exchange is not merely one generator among others but the
whole of the eight-piece blind content. And look for the rank 88 in the
structure of the incidence map itself — in how the 15800 cuttings meet the 192
pieces — rather than in the trace counts of the group, which this cycle shows
do not carry it.
