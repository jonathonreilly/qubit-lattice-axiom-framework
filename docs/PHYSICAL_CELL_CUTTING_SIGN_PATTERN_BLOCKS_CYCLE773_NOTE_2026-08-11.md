# Physical cell cutting: the sign-pattern blocks split every rank, and locate the 39 (cycle 773)

Date: 2026-08-11
Authority: none
Audit: unset.
Claim type: bounded_theorem
Constitutional effect: none.

## 1. What is measured

The object is the cell cutting family of the unit four-cube: its 16 corners, the 2672
five-corner subsets of unit determinant, the 400 of those at the adjacency cost floor 6,
the 15800 cuttings of the cell by 24 such pieces, the 192 pieces that actually occur (each
in 1975 cuttings, so 379200 piece slots counted either way), and the 192 covers of 8
pieces each that meet every cutting exactly once. The paired runner
[scripts/physical_cell_cutting_sign_pattern_blocks_cycle773_2026_08_11.py](../scripts/physical_cell_cutting_sign_pattern_blocks_cycle773_2026_08_11.py)
builds every one of those objects in-run from the corners upward; it reads no cached data
and no input file, works exactly over the integers and two fixed primes, and prints one
line per gate. Every one of those gate lines passes; 3 of them are labelled rejectors and
3 are labelled honest negatives. The honest negatives carry the sharpest content in this
note and are stated in section 8, not softened away.

## 2. Sixteen blocks of dimension twelve

The 384 signed coordinate maps act freely on the 36864 pairs made of one piece and one
cover, giving 96 orbits of 384, and each orbit read as a zero-one table over covers by
pieces is one of the 96 tables below. Inside that group sit the 16 pure flips, one per
subset of the 4 axes. They form a subgroup, they act freely on the 192 pieces, and they
leave 12 orbits of 16 pieces each.

Every sign pattern of the 4 axes is a subset s, and its character sends the flip f to plus
one when s and f overlap evenly and to minus one when they overlap oddly. Fix one piece per
flip orbit; the vector carrying the character value of s at f on the image of that piece
under f, and nothing elsewhere, is one basis vector, so the block of s has dimension 12.
Then 16 times 12 is 192, the whole piece count, and the 16 blocks together stack to rank
192, so they fill the piece coordinates rather than merely fitting inside them. The block
of the empty pattern is the flip-invariant space and the block of the all-axes pattern is
the space where every flip acts by its sign.

The identity this cycle runs on: when the kernel of a matrix over the pieces is held by the
16 flips, the rank of that matrix is the sum of its 16 per-block ranks. That recomposition
is the discriminating statistic. Constancy of the per-block rank inside each weight class
is not, and the runner shows it is not: the rejector builds a 48-row coordinate slice, four
pieces from each of the 12 flip orbits, whose per-block rank is 12 in every one of the 16
blocks and so is perfectly constant by weight, yet it recomposes to 192 while its actual
rank is 48. A second rejector swaps two pieces of the cover incidence: the rank is
unchanged at 105, but the hold of 15 of the 16 flips is broken and the recomposition
returns 121 instead.

## 3. The single-table nullity without linear algebra

Each of the 96 orbit tables is 2-regular in rows and in columns, so it falls into 48 cycles
of length 8, each visiting 4 pieces, and the vector alternating plus and minus one over
those 4 pieces is annihilated by the table. The 16 flips permute the 48 cycles of a table
with 12 classes of 4.

Each cycle is held by exactly 4 flips, and those 4 are precisely the flips supported on one
axis pair: the identity, the two single-axis flips of that pair, and their product. They
act simply transitively on the 4 pieces the cycle visits, which is why the holder is a
group of order 4 and not larger. That axis pair labelling is equivariant: pushing a cycle
by any of the 384 maps carries its pair to the image pair, with 0 of 18432 checks failing.
Since the maps reach all 6 axis pairs from any one of them, the 12 classes must be spread
evenly over the 6 pairs, so each pair carries exactly 12 divided by 6, that is 2 classes.
That count is forced by the transitivity before any table is looked at; the runner then
confirms that every measured fibre is 2, on all 96 tables.

A cycle survives into the block of s exactly when its axis pair sits inside s, so a pattern
of weight w receives 2 times the number of pairs inside it, that is w(w-1) kernel
dimensions. By weight class that is [0, 0, 2, 6, 12], which weights to 0 + 0 + 12 + 24 + 12
= 48, the full nullity of the table, and leaves per-block ranks 12 - w(w-1) = [12, 12, 10,
6, 0] recomposing to 144. Nothing in that derivation reduces a matrix. The rule really is
"pair inside the pattern" and not "pair meets the pattern": the third rejector uses the
weaker rule, which would give [0, 6, 10, 12, 12] and a nullity of 144, and misses the
measured 48 on every table.

## 4. Three kernels, three profiles

The cover incidence, written M, has kernel 87. Its per-block kernel dimensions are
[3, 3, 6, 6, 12] by pattern weight, constant inside each weight class, and its per-block
ranks are [9, 9, 6, 6, 0] recomposing to its rank 105; both readings agree at both primes.

Split M by the two labels the object already carries, the axis kept by a cover and the
axis pair of a piece. The part where the piece carries the axis of its cover, written U,
has kernel 78, per-block dimensions [2, 2, 4, 8, 12] and per-block ranks [10, 10, 8, 4, 0]
recomposing to 114. The remaining part, written V, has kernel 48, per-block dimensions
[0, 0, 2, 6, 12] and per-block ranks [12, 12, 10, 6, 0] recomposing to 144; V is a single
orbit table, so its profile is exactly the single-table profile of section 3, and U is the
entrywise sum of the other 3 of the 4 orbit tables that make up M. Each of the three
recomposes exactly, so in all three cases the kernel is held by the 16 flips.

## 5. Where the shortfall sits

Subtracting the incidence profile from the single-table profile gives [3, 3, 4, 0, 0] by
weight, which weights to 3 + 12 + 24 = 39 = 144 - 105. The shortfall is therefore located,
not merely counted: it is 0 in both blocks of weight above 2, so every one of the 39 lost
dimensions sits in a block of weight at most 2.

Read in two steps it is not monotone block by block. Single table minus U is [2, 2, 2, 2,
0], weighting to 30. U minus M is [1, 1, 2, -2, 0], weighting to 9. The two weights add to
30 + 9 = 39, but the weight-3 entry rises by 2 on the second step, so the second step gives
rank back in one block while taking more of it in others.

## 6. Twelve killed by every part, seventy-five by cancellation

M is the entrywise sum of exactly 4 of the 96 orbit tables. The common kernel of those 4
has dimension 12, with per-block dimensions [0, 0, 0, 0, 12]: it is exactly one block, the
all-axes block, the space where every flip acts by its sign. M kills all 12 of it with 0
failures, and so does each of the 4 parts separately. Equivalently the stack of the 4
parts has rank 180 = 192 - 12 at both primes.

The other 75 = 87 - 12 kernel dimensions of M are of the opposite kind. Extending a basis
of the all-axes block to a basis of the kernel of M produces 75 further directions, and 0
of those 75 are killed by even one of the 4 parts. Not one of them is a near miss: no
single part kills any of them, so the kernel of M splits cleanly by mechanism, 12
dimensions killed part by part and 75 killed purely by the cancellation between the 4
parts.

## 7. Relation to work in flight

Two companion stems are in flight on the same object,
`PHYSICAL_CELL_CUTTING_CELL_ORBIT_CYCLES_CYCLE771_NOTE_2026-08-11` and
`PHYSICAL_CELL_CUTTING_KERNEL_COLOUR_CLOSED_FORM_CYCLE772_NOTE_2026-08-11`. Nothing here
reads them, cites a value from them, or depends on them in any way: the runner rebuilds the
cell, the pieces, the cuttings, the covers, the maps, the orbits and the incidence from
scratch, and every number in this note is measured in that run and printed by it. No axiom
and no import is added by this note; it stands on
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) alone.

## 8. Boundary

The block route divides by the order of the flip group, so it speaks at characteristic zero
and at odd characteristic only. At characteristic 2 all 16 block bases coincide and stack
to rank 12, and the route says nothing there; the value 144 for every orbit table at
characteristic 2 is a separate direct measurement, reported as such.

The per-block profiles of M and of U are reported as measured. No closed form is claimed
for either. Only the single-table profile has a derivation here, and it comes from the axis
pair labelling of section 3.

The block profile does not separate the 2 distinct kernel classes that sit among the 96
tables, 48 tables each: both classes give per-block [0, 0, 2, 6, 12]. Anything that
distinguishes them has to come from elsewhere.

This note says nothing about why M is the sum of those particular 4 orbit tables, and two
gates in the paired runner are aimed squarely at that question. The first sums the 4 orbit
tables that come next in index order after the 4 that make up M. That sum is not M, and
none of its 192 rows is a cover, yet it reaches the same rank 105 and the same per-block
drop [3, 3, 4, 0, 0], weighting to the same 39, and its kernel even has the same dimension
87. Keeping 3 of the parts of M and swapping only the fourth does move both readings, to
rank 93 and drop [3, 3, 4, 3, 0], so the comparison is not vacuous. The consequence is
stated plainly: rank 105 and the shortfall 39 are not by themselves a fingerprint of the
cover incidence among sums of 4 orbit tables, and no claim in this note should be read as
saying they are.

What does tell the two sums apart is the kernel as a subspace rather than as a number.
Both kernels have dimension 87, and they meet in 33 of those dimensions, so the two sums
annihilate genuinely different spaces. Every reading this note extracts from the block
split is a dimension count, and dimension counts are exactly what the two sums share.
Whatever pins the cover incidence inside this family is carried by the kernel it spans and
not by the size of that kernel.
