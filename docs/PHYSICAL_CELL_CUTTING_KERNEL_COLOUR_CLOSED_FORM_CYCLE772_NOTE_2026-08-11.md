# Physical cell cutting: the 96 orbit tables carry exactly two kernels, and the colour is a closed form (cycle 772)

Date: 2026-08-11
Authority: none
Audit: unset.
Claim type: bounded_theorem
Constitutional effect: none.

## 1. Status

The unit four-cube has 2672 five-corner subsets of unit determinant. 400 of them sit at
the adjacency cost floor 6, and those 400 admit 15800 exact cuttings of the cell into 24
pieces. Exactly 192 distinct pieces occur, each in 1975 of the cuttings, and 24 x 15800 =
379200 = 192 x 1975. There are also 192 eight-piece covers, each meeting every cutting
exactly once, so 8 x 1975 = 15800. The group of 384 signed coordinate maps acts by 384
distinct bijections on the pieces and on the covers, transitively on each, and freely on
the 36864 pairs made of one piece and one cover, so those pairs fall into 96 orbits of
size 384. Read as a zero-one table over covers by pieces, each orbit is a 192 by 192
matrix, and those 96 matrices are the subject here.

Three things are proved. First, the 96 tables carry exactly 2 kernels: the kernel of each
table has dimension 48, and reducing all 96 of them to canonical form leaves exactly 2
distinct subspaces, each shared by 48 tables, at each of the two primes 1000003 and
1000033. Second, each of the 2 kernels is a submodule for the whole group of 384, which
forces a stack rule: all 48 tables of one colour stack to rank 144, while a table of each
colour stacks to 180. Third, the colour has a closed form in the geometry of the cell:
each cover carries one axis, each piece carries a pair of axes, and the colour of an orbit
is decided by whether the cover axis lies in the piece pair, on all 36864 pairs.

The runner
[physical_cell_cutting_kernel_colour_closed_form_cycle772_2026_08_11.py](../scripts/physical_cell_cutting_kernel_colour_closed_form_cycle772_2026_08_11.py)
rebuilds every one of those objects from nothing: the 16 corners, the pieces, the
cuttings, the covers, the group, the orbits and the kernels are all constructed in the
run, and no cached data is read. It reports 31 gates, all passing, of which 7 are
labelled rejectors or honest negatives, and 3 more carry a control that fails where the
real object passes. Everything is exact over the integers and the two fixed
primes; no floating point enters any gate and no constant is fitted. No axiom is added to
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## 2. The two kernels

The kernel of an orbit table is exhibited rather than inferred. Every table has exactly 2
ones in each row and 2 in each column, so its bipartite graph is a disjoint union of
cycles; across the 96 tables there are 4608 cycles and every one has length 8, hence
visits 4 pieces. On each cycle put the vector that is plus and minus one alternately on
those pieces and zero elsewhere. Each such vector is killed by its table over the
integers, and the supports of the vectors of one table are disjoint, so the 48 of them are
independent and span the kernel.

Reducing those 48 vectors to canonical row-reduced form and comparing the results gives
exactly 2 distinct subspaces, of dimension 48 each, with class sizes 48 and 48, and the
split is the same at 1000003 and at 1000033. That 2 is not an artefact of the tables being
few or alike: the 96 tables are pairwise distinct as matrices, and 20 copies of one kernel
with two piece coordinates swapped all keep dimension 48 while matching neither class.

The 2 kernels span 84, so they meet in 48 + 48 - 84 = 12, and the meet has a name. The 16
pure flips act freely on the 192 pieces, leaving 12 orbits. On each orbit put the vector
whose value at the image of the base piece is the sign of the flip that moved it, plus one
for an even flip word and minus one for an odd one. Those 12 vectors have rank 12, lie
inside every one of the 96 kernels, and are killed by every one of the 96 tables over the
integers: the meet is the sign-anti-invariant space of the flips. The sign is what carries
this. The invariant space for the trivial character has rank 12 as well, but it meets
every kernel in 0 and all 96 tables leave it alive.

## 3. Submodules and the stack rule

7 of the 384 maps generate the whole group. Permuting the coordinates of any of the 96
kernel basis vectors by any of those 7 generators lands back inside the same kernel: 672
checks, 0 outside. Each kernel is therefore a submodule for the whole group, and the
two-valued colour is a property of the group action and not of a chosen table.

The stack rule follows at once. Tables of one colour share a kernel of dimension 48, so
stacking all 48 of them gives 9216 rows of rank 144, which is exactly the rank of every
single table. Stacking one table of each colour leaves only the meet, so the rank is 180 =
192 - 12. Both readings are measured, not argued: all 2304 cross-colour stacks have rank
180 and all 2256 same-colour pairs stay at 144.

The submodule statement is sharp rather than automatic. Dropping a single basis vector
from one kernel leaves a subspace of rank 47 that is no longer stable: 5 of its 329
generator images fall outside it.

## 4. The sums and their block factorisation

Let A be the entrywise sum of the 48 tables of one colour and B the sum of the other 48.
A + B is the all-ones matrix and every row and column sum of A and of B is 96. That much
is forced by the tables being 2-regular and carries no information: splitting the 96
orbits in index order instead gives a matrix with the same all-ones sum and the same
regularity, but rank 133.

The content is elsewhere. Rank A = rank B = 4 at both primes, nullity 188, and A stacked
on B still measures 4, so the two sums share their row space. A and B each have exactly 4
distinct rows, each shared by 48 covers, and exactly 6 distinct columns, each shared by 32
pieces, and each is constant on all 24 blocks those partitions cut out. The resulting 4 by
6 pattern has 12 ones of 24, row sums all 3, column sums all 2, and rank 4 at both primes,
and the two patterns are complementary. A and B each kill all 96 kernel basis vectors over
the integers, including the kernel of the other colour, while the index-order control
fails on all 48 of each class. Both sums are covariant under all 384 maps on all 36864
pairs; swapping two pieces inside A breaks that covariance for 382 of the 384 maps.

## 5. The closed form

The 4 row blocks and the 6 column blocks are named by the geometry of the cell, and once
they are named the colour is a closed form.

Each cover has a unique non-identity fixer in the group of 384, and that fixer is a single
flip. The axis of that flip takes 4 values with 48 covers each, and those 4 classes are
exactly the 4 row blocks of A. Each piece has 5 corners; for each axis count the corners k
on one side of it and read min(k, 5 - k). That profile attains its maximum on exactly 2
axes for every piece, and the resulting unordered pair takes 6 values with 32 pieces each,
which are exactly the 6 column blocks. Both labels are equivariant for the induced action
on axes: 0 failures in 73728 cover checks and 0 in 73728 piece checks.

The closed form is then this. On all 36864 pairs, the colour of the orbit of a pair is
decided by whether the cover axis lies in the piece pair. The test is constant on each of
the 96 orbits and splits them 48 and 48, and it agrees with the canonical kernel class up
to one global choice of which class is called which. Exactly 16 of the 384 maps hold every
row block and every column block, and they are precisely the 16 pure flips, which is the
same group of 16 whose sign character named the meet in section 2.

Two rejectors keep this from being vacuous. Shifting every piece pair by one axis
disagrees with the colour on 24576 of the 36864 pairs, and shifting every cover axis by
one disagrees on 24576. The shifted piece label also fails equivariance, on 57344 of the
same 73728 checks.

Two candidate labels were tried and are reported as they came out. Labelling a piece by
how many of its corner pairs are adjacent gives 1 label for all 192 pieces. Labelling it
by the flip weight of its own fixer gives 3. Neither can reach 6 classes, so neither can
name the column blocks.

## 6. The incidence read

The cover incidence table, the 192 by 192 zero-one table recording which pieces lie in
which cover, is itself a sum of orbits: it is the entrywise sum of exactly 4 of the 96,
carrying 3 of one colour and 1 of the other. Through the closed form the same fact is
local and uniform: every cover holds 8 pieces of which exactly 6 carry the cover's own
axis, and every piece lies in 8 covers of which exactly 6 carry the axis of that piece.

The two ways of reading those 4 orbits give different answers. Stacked, they have rank
180, which is the cross-colour value of section 3. Added entrywise, they have rank 105 at
both primes, and 192 - 105 = 87. The gap between 180 and 105 is cancellation inside the
sum.

## 7. What is new and what is not

New here: that the 96 kernels collapse to exactly 2 subspaces; the naming of their meet as
the sign-anti-invariant space of the 16 flips; the submodule property and the stack rule
it forces; the block factorisation of A and B and their rank 4; the closed form for the
colour together with its 2 rejectors and its 2 rejected candidates; and the reading of the
incidence as 4 orbits carrying 3 of one colour and 1 of the other.

Not new: that every one of the 96 orbit tables has rank 144. The previous cycle
established that for all 96 tables from a single 4 by 4 determinant, and this cycle does
not repeat that derivation; the rank enters here only as the value the stack of a whole
colour has to match, and the runner re-measures it directly inside that gate rather than
citing it. `PHYSICAL_CELL_CUTTING_CELL_ORBIT_CYCLES_CYCLE771_NOTE_2026-08-11` is a
companion cycle of this lane that is still in flight and not on main at the time of
writing; nothing here reads it or depends on it.

## 8. Boundary and honest auditor read

The closed form describes which colour an orbit carries. It does not by itself say which 4
of the 96 orbits the geometry selects to build the incidence: that selection is read off
the object here and is not derived from the colour rule.

The rank drop from 144 to 105 is localised to the sum and is not explained here. The same
4 orbits stacked have rank 180, and each of them alone has rank 144, so the drop to 105
happens only when they are added, and this note offers no mechanism for it.

The names 0 and 1 for the 2 colours come from canonical form, so which class is called
which is a convention; only the partition of the 96 orbits into 48 and 48 is intrinsic,
and the agreement between the kernel class and the geometric test is stated up to that one
global choice. All ranks are measured at 2 fixed primes, and the annihilation statements
are over the integers; nothing here is measured in any other characteristic.

No axiom, import or literature comparator is used. The object is rebuilt in the run from
the 16 corners of the unit four-cube and the group of 384 signed coordinate maps, and
every number in this note is a number the runner prints.
