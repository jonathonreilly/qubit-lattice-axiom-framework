# Complementary sets of cell orbits are blind to the same directions, and the 96 cell orbits are the partner pairs of a single cover — Cycle 768

Date: 2026-08-11

Authority: none

Audit: unset.

Status: two derived structure theorems on the cell-orbit lattice, with the
complete rank spectrum at the four smallest set sizes and, by the first
theorem, at the four largest

Claim type: bounded_theorem

Runner:

- [`physical_cell_cutting_complement_spaces_cycle768_2026_08_11.py`](../scripts/physical_cell_cutting_complement_spaces_cycle768_2026_08_11.py)

Axioms:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

Constitutional effect: none. This note changes no axiom, primitive, registry,
policy, audit verdict, effective status, or framework claim.

## 1. What this responds to

Cycles 764 to 766 mapped the rank band of the cover table: a ceiling of 144, a
floor of 48 on the blind space, a measured rank of 105 with an 87-dimensional
blind space, and therefore an excess of 39 that is pure cancellation, born on
pairs of cell orbits rather than on any single one. Cycle 767 added that a set
of cell orbits and its complement carry equal rank, and cut the 96 orbits into
25 corner strata.

Two questions were left standing. First, whether that equality of rank is an
accident of counting — two subspaces that happen to have the same dimension —
or an equality of the subspaces themselves. Second, what the 96 cell orbits
actually are as objects, rather than as indices into a table.

Both are answered here, and neither answer needed a new axiom or a new input.
The runner prints every check as one of a list of computational identities,
with no floating point entering any gate.

## 2. The setting

The object is the one inherited from cycle 764 and unchanged since. Inside the
unit four-cube there are 2672 candidate pieces, of which 400 sit at the
adjacency-cost floor of 6; there are 15800 cuttings of 24; 192 of the pieces
are used, and they assemble into 192 covers. A cover is 8 pieces that meet
every cutting exactly once.

A group of 384 maps acts on this object. It is one orbit on the 192 pieces and
one orbit on the 192 covers, and it acts freely on the 36864 cover-piece cells,
so those cells fall into exactly 96 orbits. Each cell orbit is a 192 by 192
zero-one table, and the cover table — the one whose rank is 105 — is the sum of
4 of these 96.

Two facts about the 96 tables, both already gated in the runner, carry
everything below. Each of the 96 has exactly two ones in every row and in every
column, which is 384 ones per table. And the 96 add entrywise to the all-ones
table, which has rank 1.

## 3. The same blind space, not merely the same dimension

**Theorem A.** Let `S` be any set of cell orbits with `1 <= |S| <= 95`, let
`T_S` be the entrywise sum of the orbit tables in `S`, and let `S^c` be the
complement of `S` among the 96. Then `T_S` and `T_{S^c}` have the same right
kernel, the same left kernel, and the same image.

The proof is short enough to give in words. Because each orbit table has two
ones in every row and every column, `T_S` has every row sum and every column
sum equal to twice the size of `S`. Because the 96 add to the all-ones table,
`T_S + T_{S^c}` is the all-ones table. Now take a vector `v` in the right
kernel of `T_S`. Add up the entries of `T_S v`: the total is twice the size of
`S` times the sum of the entries of `v`, and it is zero. Since the size of `S`
is between 1 and 95, that factor is not zero, so the entries of `v` sum to
zero, so the all-ones table kills `v` as well. Then
`T_{S^c} v = (all-ones) v - T_S v = 0`. The argument runs the same way starting
from `S^c`, so the two right kernels are equal. Repeating on the transposes
gives the same left kernel, and equal kernels on a square table give equal
rank, so the images agree too.

The step that carries the weight — every blind vector sums to zero — has an
exact linear-algebra form as well: the all-ones vector lies in the row space of
`T_S` and in its column space. The runner checks that form in exact rational
arithmetic, by comparing the rank of `T_S` with the rank of `T_S` with the
all-ones row appended, and likewise on the transpose. Across 16 test sets there
were 0 misses, and the largest exact rank seen among them was 144, the ceiling.

The subspace equality itself is checked directly, over a prime field, by
building kernel bases for `T_S` and for `T_{S^c}` and comparing the span of
each with the span of the two stacked together. Across the same 16 sets there
were 0 kernel mismatches and 0 image mismatches, and in all 16 the two tables
genuinely differ from one another, so the equality is not the trivial one. A
deliberately corrupted table — one zero entry lifted to a one — was fed through
the same comparison and was rejected, which is what makes the check a check.

The 16 sets are the four incidence orbits, a single orbit, the six incidence
pairs, and eight further sets drawn by the runner's own pseudo-random
recurrence, the largest of them 64 orbits.

Stated plainly: the cover table's 87-dimensional blind space is literally the
same subspace as the blind space of the 92 orbits the cover table leaves out.
The same directions, not merely as many of them. Whatever the cover table
cannot see, the complementary 92 orbits cannot see either.

## 4. The 96 cell orbits are one cover's partner pairs

**Theorem B.** Fix any cover `c`. The subgroup fixing `c` has order 2, and its
non-identity element acts on the 192 pieces without fixed points, so it splits
them into 96 partner pairs. The map sending a cell orbit to the partner pair it
meets in row `c` is a bijection from the 96 cell orbits onto those 96 partner
pairs.

Again the proof is short. The group is transitive on the 192 covers and has
order 384, so the subgroup fixing a cover has order 384 divided by 192, which
is 2. The group acts freely on cells, so the non-identity element of that
subgroup cannot fix any piece — fixing a piece would fix the cell in row `c` —
and being an involution without fixed points, it pairs the 192 pieces into 96
partners. A cell orbit meets row `c` in exactly two cells, because every orbit
table has exactly two ones in every row; those two cells are swapped by the
element, so they are a partner pair. Counting both ways, 96 orbits onto 96
pairs, gives the bijection.

The runner measures this on all 192 covers, not on one. Every cover has a
stabiliser of order exactly 2; the non-identity element fixes 0 pieces in every
case, is an involution in every case, and the orbit labelling of the cover's
row is constant on partners with 0 misses; every cover's row splits into
exactly 96 fibres of size two. As a discriminator, the 96 labels appearing in a
cover's row are all distinct, and a row whose labels were deliberately swapped
between two different orbits was put through the same fibre test and rejected.

The corollary needs one more line. The four orbits summing to the cover table
are exactly the cells where a cover meets its own pieces, so inside cover `c`'s
own row they are carried by its 8 blocks. Those 8 blocks therefore carry 4
labels, two blocks each, and the runner confirms that those 4 labels are
exactly the four incidence orbits. So both counts that this whole line of work
runs on — the 96 cell orbits and the 4 incidence orbits — are read off a single
cover: 96 partner pairs among its 192 pieces, and 4 partner pairs among its 8
blocks.

## 5. The complete spectrum at sizes two and three, and where that leaves the small sizes

Every pair of cell orbits was ranked. There are 4560 of them. The spectrum has
13 distinct values running from 48 to 144: 960 pairs sit at the ceiling of 144,
and 1104 sit at or below 105, the cover table's own rank.

Every triple was ranked as well, all 142880 of them. That spectrum has 18
distinct values running from 64 to 144, with 60960 at the ceiling and 1472 at
or below 105.

Three independent anchors hold these censuses down. The six incidence pairs
come out 72, 93, 117, 129, 144, 144 and the four incidence triples come out
114, 130, 142, 142, matching the exact rational ranks carried forward from
cycle 767 with 0 discrepancies. A sample of 25 pairs and 15 triples was
re-ranked from the full 192 by 192 tables rather than through the small-matrix
reduction, and every one agreed. The entire pair census was recomputed at a
second prime, 1000033 against 1000003, with 0 values off.

Theorem A carries each census to the opposite size at no cost, because equal
kernels give equal rank. The complete spectrum at size two is simultaneously
the complete spectrum at size 94, and the complete spectrum at size three is
simultaneously the complete spectrum at size 93.

Sizes one and four were settled before this cycle, and Theorem A carries them
across as well, so the four smallest set sizes and the four largest are all
complete. Cycle 763 derived the size-one spectrum rather than measuring it.
Read as a bipartite graph on covers and pieces, each of the 96 orbit tables is
a disjoint union of 48 cycles through 4 covers each; a cycle of even length
contributes one less than its length to the rank, over any field; so every
single orbit has rank exactly 144, the ceiling, with no exception among the 96
and no dependence on the modulus. This runner re-checks it, holding the cycle
rule, the prime-field elimination and the ceiling read off the parts against
one another. Cycle 765 ranked every four-subset of the 96 — the whole census,
not a sample — and that spectrum also runs up to 144.

That reading puts the two numbers of cycle 764 into a single picture at size
one. A single orbit sits at the ceiling of 144, so its blind space has
dimension 192 less 144, which is 48, the floor exactly; and the cycle rule says
where those 48 directions live, one for each of the 48 cycles. Why the ceiling
and the floor should add to 192 in the first place is not derived here.

One number in the pair spectrum deserves its own line. The least pair rank over
all 4560 pairs is 48, well below the least incidence-pair rank of 72. So the
four orbits that build the cover table are not the extreme cancellers:
somewhere among the 96 there are two orbits that lose far more rank together
than any two of those four. Which two, and why, is not settled here. The
theorem of cycle 764 puts a floor of 48 on the blind space and no floor at all
on the rank, so nothing forces the least pair rank to be any particular value,
and the coincidence of the two numbers is not claimed to mean anything. It
should not be confused with the 48 of the paragraph above, which counts the
cycles in a single orbit and equals the floor by the arithmetic given there.

## 6. The cancellation degree, and one prediction tested

Define the degree of a cell orbit as the number of partners with which it forms
a pair of rank strictly below the ceiling of 144 — the number of ways it takes
part in cancellation. Read off the pair census, the degree is 75 for every one
of the 96 orbits: 1 distinct value, minimum 75, maximum 75. The four incidence
orbits are 75, 75, 75, 75.

That the degree is the same for every orbit is measured, not derived; nothing
here explains why 75 and not another number. It does mean the question the
degree was built to ask — do the four incidence orbits stand out in the
cancellation order? — has a degenerate answer. They sit at the top, but so do
all 96, and no weight should be put on that flag. As an independent check that
the degree really is what it says, one orbit's degree was recomputed from
scratch by ranking all 95 of its pairs on the full 192 by 192 tables, and it
agreed.

Cycle 767 found that the corner-overlap stratum cuts out the incidence set
exactly but does not decide which orbit repairs the rank. The natural next
question is whether the *pair* of strata determines the pair rank. It does not.
Of the 325 stratum pairs realised among the 4560 pairs, 313 carry more than one
rank value, and the worst single stratum pair carries 13 distinct values. The
prediction going in was that the stratum pair would not determine the rank, and
that prediction held. The corner strata classify the orbits, but they do not
classify what happens when two orbits are added together.

## 7. Boundary

This note touches no axiom, no primitive, and no framework claim. Nothing here
derives a physical quantity, and nothing here is a step toward one on its own.

It does not decide the rank of the cover table beyond what cycles 764 to 766
already measured: 105, with an 87-dimensional blind space and an excess of 39
below the ceiling of 144. Theorem A explains why a complementary set has the
same rank, but it does not say what that rank is.

It says nothing about the set sizes between the four smallest and the four
largest. Sizes one, two, three and four are complete, and so are 92, 93, 94 and
95 — the first four from cycle 763, cycle 765 and this cycle's two censuses,
the last four by Theorem A. The sizes in between are not, and the number of
subsets there is far past what a complete census can reach.

Two of the runner's readings are redundant rather than discriminating, and no
claim above leans on them. The first is the degree-order flag discussed in
section 6: with all 96 degrees equal it cannot come out any other way. The
second is the relationship between the exact all-ones test and the prime-field
subspace test — they are two proofs of the same theorem rather than evidence
for two different facts, so passing both is one result checked twice, not two
results.

## 8. Honest auditor read

Here is what I would push on if I were reading this cold. The subspace equality
in section 3 is decided over a prime field, not in exact arithmetic: what is
exact is the all-ones membership test, run through rational forward
elimination at all 16 sets, and the incidence-set ranks inherited from cycle
767; what is modular is the kernel and image comparison and both censuses.
The theorem itself is an argument on the integers and does not depend on the
prime, but the direct verification of it does. The size-one spectrum is the one
rank statement here that escapes the prime entirely, and it is not new work:
the cycle rule settles it in any characteristic, cycle 763 derived it, and this
runner only re-checks it against the elimination and against the parts. Second,
the triple census rests
on the small-matrix reduction, which is cross-checked against the full 192 by
192 table on 15 triples out of 142880 and against the second prime not at all;
the pair census is the better-anchored of the two, having both the full-table
sample of 25 and a complete recomputation at the second prime. Third, each of
the two rejectors is a single corrupted object, so they show the checks are not
vacuous but do not survey the space of ways to be wrong. Fourth, the degree
result is a flat spectrum, and a flat spectrum is exactly the shape a bug that
overwrote a computation with a constant would produce — the independent
recomputation of one degree from the full tables is what rules that out, and it
covers one orbit, not 96. Finally, two conditions I had expected to hold came
out false and were removed rather than accommodated: I had assumed the least
pair rank over all 4560 pairs would be the least incidence-pair rank of 72, and
that the least triple rank would be the least incidence-triple rank of 114.
The measured minima are 48 and 64. The incidence sets are not extremal in the
lattice, and section 5 says so.
