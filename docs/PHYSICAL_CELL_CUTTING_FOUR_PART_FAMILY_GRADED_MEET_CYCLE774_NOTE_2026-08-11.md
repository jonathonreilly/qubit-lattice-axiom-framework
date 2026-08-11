# Physical cell cutting: the four-part family, and how much of the graded meet is free (cycle 774)

Date: 2026-08-11
Authority: none
Audit: unset.
Claim type: bounded_theorem
Constitutional effect: none.

The finding is three-part.

(a) **The family is exactly counted.** The 96 orbit tables are pairwise disjoint and
sum entrywise to the all-ones matrix, so every 4-subset of them is a zero-one matrix
that is 8-regular in both directions, and there are exactly 3321960 such members. The
cover incidence is one of them.

(b) **12 of the 33 dimensions of the `cycle 773` meet are free.** Every single one of
the 96 tables annihilates the whole all-signs block, so every member of the family
agrees there automatically, whatever else it is. Only 21 of the 33 are earned.

(c) **The rest of the agreement is graded, and the grading does not pin the
incidence.** The per-block meet is `[3, 0, 3, 0, 12]` by sign-pattern weight and the
two kernels are transverse at the odd weights 1 and 3 — but that transversality is
shared with roughly half the family: of 366 sampled members whose weight-3 kernel has
dimension 6, 169 are transverse to the incidence's. The incidence's own weight-3
kernel is itself shared with 13 members of the sample. The graded kernel does not pin
the cover incidence.

## 1. What is measured

The object is the unit four-cube. Its 16 corners give 2672 five-corner subsets of unit
determinant, of which 400 sit at the adjacency cost floor 6. Those 400 pieces cut the
cube in 15800 ways, each cutting using 24 pieces. Exactly 192 distinct pieces occur,
each in 1975 of the cuttings, so the piece-slot count is 379200 read either way. There
are 192 covers of 8 pieces each, and each cover meets every cutting exactly once.

The paired runner is
[`../scripts/physical_cell_cutting_four_part_family_graded_meet_cycle774_2026_08_11.py`](../scripts/physical_cell_cutting_four_part_family_graded_meet_cycle774_2026_08_11.py).
It builds all of this in-run from the corners upward: it reads no cached data and no
input file, works exactly over the integers and two fixed primes, uses no floating
point in any gate, fits no constant, and prints one line per gate. All 31 gates pass.
Three are labelled `rejector:` and six are labelled `honest negative:`; the content of
those six is stated plainly in the final section and is not softened away.

The object is built from the lattice and admissibility content of the four axioms in
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) and imports nothing else.

## 2. The family

The group of 384 signed coordinate maps acts freely on the 36864 pairs made of one
piece and one cover, giving 96 orbits of size 384, each read as a zero-one table over
covers by pieces. Each of the 96 tables therefore carries exactly 384 entries; no two
of the 96 share an entry; and the 96 sum entrywise to the all-ones matrix, since 96
times 384 is 36864.

Hence any 4-subset of the 96 sums to a zero-one matrix with row sums 8 and column sums
8, and the family of such sums has exactly 3321960 members. The cover incidence is one
member, and so is the twin assembled from four of the tables outside it.

Two rejectors show that both halves of that statement are doing work. A four-part sum
that repeats one table has an entry 2, so it is the disjointness and not the count that
gives zero-one. The sum of 5 distinct tables is zero-one but has row sums 10, not 8,
so it is the count four that gives 8-regularity.

## 3. Twelve of the thirty-three are free

The 16 pure flips act freely on the 192 pieces with 12 orbits, so each of the 16 sign
patterns of the four axes carries a block of dimension 12, and the 16 blocks fill all
192 piece coordinates.

Every one of the 96 tables annihilates the whole block of the all-signs pattern: the
kernel of each single table inside that block has dimension 12, which is the full block
dimension. An entrywise sum of tables therefore annihilates it too, so any two members
of the family agree on at least those 12 dimensions, whatever else they are.

`cycle 773` measured the kernels of the cover incidence and of the twin at dimension 87
each, meeting in 33. This cycle deflates that 33 into 12 automatic plus 21 earned.

## 4. The meet is graded, and the odd weights are transverse

Both matrices are held by all 16 flips, so both kernels split over the 16 blocks. The
per-block kernel dimensions are `[3, 3, 6, 6, 12]` by pattern weight, constant within
each weight class, recomposing to 87 at both primes. The per-block meet is
`[3, 0, 3, 0, 12]`, recomposing to exactly the 33 measured in the full 192 dimensions.
The incidence-only directions are `[0, 3, 3, 6, 0]`, recomposing to 54, and 54 plus 33
is 87.

At all 4 sign patterns of weight 3 the two kernels have dimension 6 apiece, meet in 0,
and stack to rank 12, the full block dimension. Because both kernels are submodules for
the flip action, constancy across a weight class is forced: those four agreements are
one fact, not four. At weight 1 the two are transverse but span only 6 of the 12
available; at weight 2 they share 3 of 6.

A rejector guards the method. Swapping two pieces of the incidence leaves only 1 of the
16 flips holding it, and the sum of its per-block kernel dimensions is then 71 while its
true kernel has dimension 87. The block-by-block split is a real check, valid only for a
matrix that the flips hold.

## 5. The weight-zero reduction

The flips act on the 192 covers with stabiliser of order 2, giving 24 orbits of 8. The
quotient by that action is 24 by 12 with entries 0 and 2, row sums 8, column sums 16,
and 12 distinct rows each occurring 2 times. Halving one row per pair gives a 12 by 12
zero-one matrix, 4-regular in rows and in columns, of rank 9 at both primes and corank
3. Its integer kernel, computed by exact rational reduction with denominators cleared
and the content divided out, is 3 vectors with entries in minus one, zero and one,
whose supports have size 4, are pairwise disjoint, and partition the 12 piece orbits,
each with 2 entries up and 2 down.

## 6. How far apart the two actually are

The incidence and the twin share no piece in any of the 192 rows. Their difference has
entries in minus one, zero and one, with 3072 nonzero entries, which is 192 times 16.
Its per-block rank is `[6, 9, 6, 6, 0]` by weight, constant within each weight class,
recomposing to 102, and it vanishes on the all-signs block.

## 7. The sweep and the wider sample

The one-swap sweep replaces exactly one of the four parts of the cover incidence by one
of the tables outside it, giving 368 members. They realise 185 distinct signatures,
where a signature is the pair of by-weight profiles together with their totals. Kernel
totals run from 48 to 120; every meet with the incidence kernel is graded, constant
within each weight class, and has all-signs entry 12 in every case. The meets
themselves run from 12 to 59 and none reaches 87.

A wider deterministic sample of 460 members — the 368 one-swap sums, 23 disjoint
quadruples, and all 70 four-subsets of an eight-table base, deduplicated — is measured
at the first sign pattern of weight 3. Of the 460, 366 have a kernel of dimension 6
there, and 169 of those 366 are transverse to the incidence's. The 460 members realise
only 130 distinct kernels at that pattern, 103 of them of dimension 6, the commonest
shared by 27 members, so the kernels repeat heavily across the sample.

## 8. Boundary and honest auditor read

The six honest negatives, stated plainly.

(a) Zero-one and 8-regular does not make a member of the family a cover incidence. All
192 rows of the incidence are covers; 0 of the twin's 192 rows is one, though the twin
is zero-one and 8-regular.

(b) 12 of the 33 shared kernel dimensions are automatic and carry no information. The
idea that agreement on the all-signs block was a clue is dropped.

(c) The halved quotients of the incidence and of the twin differ: 0 of the 24 rows agree
in place and the row multisets differ, and the halved 12 by 12 matrices are different
too, yet the two share a null space of dimension 3. The weight-zero reduction does not
tell them apart.

(d) The sweep covers 368 of the 3321960 members and the meets it finds reach only 59,
so it is a probe of the family and not a census.

(e) Transversality at weight 3 is common. Of the 366 sampled members with a
6-dimensional kernel there, 169 are transverse to the incidence's, so transversality is
not a marker of the cover incidence.

(f) The incidence's own kernel at that pattern is shared by 13 of the 460 sampled
members, and the twin's by 2, so the graded kernel at weight 3 does not pin the cover
incidence either.

What this note does not do: it does not determine what pins the cover incidence inside
the family of 3321960 members. If there is a pin, it is finer than the graded kernel.
The measurement that says where to look next is the count of distinct kernels — the 460
sampled members realise only 130 distinct kernels at a weight-3 pattern, 103 of them of
dimension 6, so the kernels are highly structured even where transversality is common.
The structure of those 103, and how the incidence sits inside it, is the next thing to
measure.
