# The space of charges on the single cell's least-cost cuttings — Cycle 736

Date: 2026-08-05

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

The object is one cell of the lattice carried through one tick of emergent time: the
four-cube on the sixteen corners of `{0,1}^4`, whose three spatial columns and single tick
column are the columns the axioms of
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supply, with nearest
neighbour adjacency only and the proper cubic rotations alone kept. A piece is a five
corner simplex of the cell of least volume; the cost of a piece counts the pairs of its
corners more than one lattice step apart, and the cost of a cutting is the sum over its
pieces. The previous cycle exhibited one two sided charge on the cuttings at the floor of
that cost: a weight on the pieces, read as a sum over the twenty four pieces of a cutting,
which the smallest move always reverses and the next smallest always keeps. It did not say
whether that charge stands alone, nor what picks it out. This cycle answers both by putting
the question to every size of move at once. Reversing every move of one size is a linear
demand on the weight, so the sizes at which a charge of that kind can exist are decided by a
rank, and where none exists the reason is handed back as a family of exchanges of odd size
summing to zero. The charges that answer the smallest move uniformly turn out to form a
space of dimension three, so there are eight of them: the two constants, and three more once
the two sides of a charge are counted as one. Those three are the previous cycle's charge, a
sister that keeps the seven piece move instead, and their sum, which keeps the smallest move
outright. That last one is the
indicator of a single orbit of the cell's symmetries acting on the groups the smallest move
leaves behind, so what the population carries is fixed by the cell and not by any choice
made while solving. Every statement below is a check in whole numbers over an explicit
finite set; no solver is used, and where a charge does not exist the obstruction is
exhibited rather than asserted.

## The cell, the floor, and the moves between cuttings

Of the 4368 five element subsets of the 16 corners, 2672 have the least volume and are the
pieces. They carry 2736 sample points with no collision between them and none on any
boundary, so containment is decided in whole numbers. The cell has 48 symmetries, counting
the 24 proper rotations against the tick flip, and the pieces fall into 57 orbits under
them.

The cost of a piece is 6 at the floor and 400 pieces reach it. A complete search over those
400 visits 502838 nodes and returns 15800 cuttings of 24 pieces each, which between them
use 192 of the 400. Every cutting therefore sits at cost 24 times 6.

A move carries one cutting to another and is measured by how many pieces it replaces. Over
all pairs of the 15800 the counts are

    four 46128     five 0         six 31968      seven 60096
    eight 151704   nine 119808    ten 281376

so no move at all replaces five pieces, while the smallest move replaces four. That the
five piece count is zero is a measurement and not a parity effect: a move replacing k
pieces changes 2k of them in all, so it is the change and not k that is forced even, and
sizes of either parity are otherwise present. Different moves can exchange the same set of
pieces; reducing each move to the pieces it takes out and puts in leaves 120, 528, 1152,
4212, 6144 and 25248 distinct exchanges at four, six, seven, eight, nine and ten pieces.
The 120 at four are as many as the 120 regions the earlier cycle recut.

## Which sizes of move a weight on the pieces can reverse

Read a weight as a choice of one of two signs on each of the 192 pieces in use, and read
the charge of a cutting as the count of its pieces the weight marks, taken modulo two. A
move changes that reading exactly when the weight marks an odd number of the pieces the
move exchanges. So demanding a charge that every move of one size reverses is a demand made
of the exchanges alone, and it is linear: the weight must mark an odd number of pieces in
each of them.

The runner settles the demand by adding one extra coordinate to the pool and setting it on
every exchange of the size in question. A weight reversing all of them exists exactly when
that extra coordinate does not lie in the span of the enlarged exchanges. When it does lie
in the span, elimination hands back the reason directly: a family of the original exchanges,
of odd size, summing to zero. A weight marking an odd number of pieces in each member of
such a family would have to mark an odd number in their sum, which is empty, so no such
weight exists.

Across the sizes measured the demand is met at four and at no other size. A weight is
exhibited whose reading changes across every one of the 46128 smallest moves. At six,
seven, eight, nine and ten pieces the obstruction is exhibited in its place, as families of
7, 5, 5, 7 and 5 exchanges summing to zero, each of odd size. The obstruction is therefore
a small and checkable object at every size where it appears: five or seven exchanges,
against move counts in the tens and the hundreds of thousands.

## How the exchange spans sit inside one another

The 15800 cuttings, each read as its list of pieces, span 88 dimensions, and their
differences span 87. The differences of the exchanges of a single size span 85 at four,
rising to 87 at eight, nine and ten, so the moves on eight pieces already reach everything
the differences of the population reach. At seven they do not: a difference of two cuttings
lying outside the seven piece span is exhibited.

The spans of the small sizes sit in a definite pattern. The four piece span lies inside both
the six piece and the seven piece span, and neither of those two holds the other. Their sum
is the eight piece span, which is also the nine piece and the ten piece span, and their meet
has dimension 85. Since that is the dimension of the four piece span, and the four piece
span lies inside both, the four piece span is exactly the overlap of the six piece and the
seven piece spans. The smallest move is thus not an outlier among the sizes but the common
part of the next two.

That pattern controls what mixed demands can do. Of the 63 non-empty sets of move sizes,
exactly 3 admit more than one answer pattern — four alone, four with six, and four with
seven — and each of those admits 2. Every other set, the whole of them included, admits
exactly one. So the freedom in the whole question lives entirely at the smallest move and
in the two sizes that share it.

## The three charges

Weights that answer the smallest move uniformly, keeping the reading on every one of the
46128 or reversing it on every one, form a space of dimension 107. Pushed forward onto the
cuttings, those weights induce 8 charges, spanning dimension 3, of which 2 are constant.
Up to swapping the two sides that is 3 charges, and each of them keeps exactly one of the
four, six and seven piece moves:

    keeps           split  rigid side     at 4     at 6     at 7     at 8     at 9    at 10
    four      5664/10136        10136        0     9504    26880    32640    48960   124224
    six       7704/8096          7704    46128        0    26880    28608    87552   190848
    seven     7424/8376          8376    46128     9504        0    21312   102336   183744

read as the two sides of the charge, the side carrying the 48 cuttings that admit no move
on at most eight pieces, and how many moves of each size the charge reverses. The middle row
is the previous cycle's charge, recovered here as one member of a space rather than as a
single solve: the 7704 against 8096 split, the 26880 of the 60096 moves at seven that it
flips, and the 48 rigid cuttings all sitting on the 7704 side are the numbers that cycle
measured. The bottom row is its sister and is new — a charge that keeps the seven piece move
and reverses every one of the smallest. The top row keeps the smallest move outright.

The three are not independent as functions. A space of dimension 3 that holds the two
constants leaves exactly 3 charges once the two sides of each are counted as one, and any
one of those is then the sum of the other two; here the top row is the sum of the middle and
the bottom. So the sister charges and the charge keeping the smallest move arrive as a
single triple rather than as three separate finds.

Demanding uniformity at six and at seven together, rather than at four, leaves a weight
space of dimension 105, and every charge those weights put on the cuttings is constant. So
the two demands that can be added to the smallest one cannot be added to each other: the
sister charges are alternatives, not a pair.

The exhibited weight sits tightly on its demand rather than loosely satisfying it: moving
it on a single piece already destroys uniformity at the smallest move.

## The groups the smallest move leaves, and which charge names them

Join two cuttings whenever a smallest move carries one to the other. The population falls
into 349 groups, of sizes 1, 2, 4, 7, 236 and 9320, with 144, 96, 36, 48, 24 and 1 groups
at each size. The 349 groups and the 144 of size one are counts the earlier cycles measured;
they are reproduced here because the charges are read against them.

No symmetry of the cell splits a group, so the 48 symmetries permute the 349 groups, and
under that action the groups fall into 14 orbits — again a count the earlier cycle measured.
Two features of that action carry the result. The 24 groups of size 236 form a single orbit,
whose stabiliser has order 2. The one group of size 9320 is held fixed by all 48.

Against that, every one of the 8 charges is left where it is by all 48 symmetries, point by
point: not merely permuted among themselves, but each one fixed. The comparison that gives
this force is the indicator of a single group of 236 cuttings, which the same 48 symmetries
carry to 24 different functions. So being fixed by the symmetries is not automatic for
functions built out of the groups, and the charges pass a test that a group indicator fails.

The charge that keeps the smallest move is exactly the indicator of that one orbit of 24
groups, holding 5664 of the 15800 cuttings, which is 24 groups of 236. It is therefore not a
solution the elimination happened to return but a named subset of the population, picked out
by the cell's own symmetries acting on the groups the smallest move leaves. The 48 cuttings
that admit no move on at most eight pieces all sit off it, so the hard core of the population
is on the larger side of this charge as it was on the smaller side of the previous cycle's.

## Independent cross-checks performed

The numbers in this section come from checks run outside the paired runner, by methods the
runner does not use; the runner does not print them.

Each headline was re-derived a second way. The move census was recomputed from counts of
shared pieces, as an integer matrix product over the whole population, rather than from the
packed popcounts the runner uses, and returned the same six move counts and the same six
totals of distinct exchanges; the zero at five pieces is not among them, since that route
was asked only about the sizes that occur. The reversal ladder was recomputed as a question
about consistency rather than about a span: over the field with two elements the demand is a
system whose right hand side is all ones, so it is met exactly when adding that column
leaves the rank alone. The ranks came out 86, 86, 86, 87, 87 and 87 across the six sizes and
86, 87, 87, 88, 88 and 88 with the column added, so the demand is met at four and at no
other size, matching the runner's tag coordinate route with no shared machinery. The same
elimination gives 107 for the weights uniform at four.

The charges were found a third way, by solving inside the 88 dimensional image of the map
from pieces to cuttings rather than by taking an orthogonal complement in the 192
dimensional weight space and pushing it forward. That route reports 120 distinct response
columns at the smallest move, 3 solutions, 8 distinct readings, and the same three rows of
the table above, entry for entry. The groups were walked out again by breadth-first search
rather than by union find, giving 349 groups of the same sizes and counts, and the charge
keeping the smallest move names exactly the union of the 24 groups of 236 on the nose.

One structure was built that the runner never forms: the orbits of the 48 symmetries acting
on the cuttings themselves. There are 391 of them, of sizes 8, 12, 24 and 48 with counts 4,
14, 96 and 277. Every one of the 8 charges is constant on every orbit, and moving a charge
on a single cutting breaks that, so the charges are functions of the orbit and the test
discriminates.

The population itself was then built a second time, from the sixteen corners upward, sharing
no step with the paired runner. Volumes came from the sum over the twenty four orderings of a
piece's edges rather than from an expansion in two by two minors; the cost from counting the
pairs of corners one step apart rather than the pairs further off; the faces of a piece from
the three by three minors of its edges rather than from an inverted edge matrix; the sample
points by listing every plane a face lies in and then choosing, inside each piece, a point
verified to miss all of them, rather than by spreading one point per orbit of pieces over the
symmetries; the search by settling the last uncovered point rather than the first; and the
symmetries by permuting and flipping the four bits of a corner's label rather than by a
matrix acting on doubled coordinates. That route returns the same 4368 five-subsets of the
corners, the same smallest volume above nothing, the same 2672 pieces at it, the same least
cost of six with 400 pieces at it, and the same 15800 cuttings of 24 pieces using 192 between
them; the cuttings agree with the cached ones row for row as a set, and the 48 relabellings
agree as a set too. Along the way it measures that a five-subset of the corners takes one of
the volumes 0, 1, 2 and 3, with 1360, 2672, 320 and 16 subsets at each, and that the 400
pieces of least cost put their faces in 68 distinct planes. The first of those says the
smallest volume above nothing is one, and that is what leaves the inverse the paired runner
takes in floating point already whole before it rounds. The two searches
visit 586443 and 502838 nodes; a different set of sample points and a different branch order
need not agree there, and that pair of numbers is not offered as a check.

Five gates were then fed objects they should turn away. The reversal test, given the true
smallest exchanges, says reversal is available; given those same exchanges with the sum of
two of them added it says the opposite, since that addition creates a family of odd size
summing to zero. Given the six piece exchanges it says the opposite, and given an
independent subset of them, 86 of the 528, it says reversal is available again — so the
test is reading the linear structure and not the size. The claim that the four piece span is
the overlap of the six and seven piece spans was checked by containment as well as by
dimension, and the five other pairs of sizes tried do not meet in it. The count of three
charges was asked of each other move size by the same code and comes out otherwise every
time, and adding a single six piece move to the smallest ones already changes it.

The support test needed care. Being uniform at the smallest move is far too weak to name the
keeping charge: any union of groups is uniform there, and the first three of the four near
misses tried below are unions of groups, so they pass that weaker test as well. What pins
the charge is that a weight on the 192 pieces can produce it, so that is
the test applied. The union of all 24 groups of 236 comes from a weight; 23 of those 24 does
not; those 24 with a group of seven added does not; 24 groups of size seven instead does not;
and the 24 groups of 236 with a single cutting removed does not. A last check pair confirms
that the 46128 smallest moves carry only 120 distinct constraints, the rarest of them
realised 10 times, of which 86 already carry the whole demand — so dropping one move from the
census cannot change the count of charges, while dropping one of those 86 constraints does.
Finally the group structure was fed relabellings of the cuttings that are not symmetries of
the cell: a shift by one, and a swap exchanging a cutting of a smallest group with one of the
largest group. Both are turned away, while all 48 real symmetries pass.

## Boundary and honest read

The pool of 192 pieces, the 120 exchanges at the smallest move and the group structure they
leave are measured by the search, not derived from a symmetry statement. They are complete
for this cell and this cost, and the note claims nothing beyond that.

The counts of moves and of distinct exchanges, the ranks, and the group sizes are all
measurements over an explicit finite population; none of them is forced by a general
argument given here. Two of the statements above are reproductions rather than discoveries
and are labelled as such where they appear: the group profile with its 349 groups and 144
singletons, and the 14 orbits of groups, were measured by earlier cycles and enter here only
so the charges can be read against them. The content of this cycle is elsewhere — that
reversal is available at four and at no other size measured, with the obstruction exhibited
at each of the others; that the four piece span is precisely the overlap of the six and
seven piece spans; that the charges form a space of dimension three rather than a single
solution; that the sister charge keeping the seven piece move exists at all; and that the
charge keeping the smallest move is the indicator of one symmetry orbit of groups.

The range of move sizes measured runs from four to ten pieces. Nothing is measured about
moves on eleven or more, and the statement that reversal is available at four and at no
other size is scoped to that range; a larger range would need its own measurement. Likewise
the count of 63 sets of sizes is a count of subsets of the same range.

Every count here is scoped to the single cell of one lattice step and one tick, with the
adjacency cost and the least volume as defined above. No statement is made about cells of
other extent, other adjacency, other costs, or about the lattice as a whole; a claim of that
kind would need its own measurement. In particular the dimension three of the charge space,
the two sides of each charge, and the 24 groups of 236 are properties of this population of
15800 cuttings.

The charges are two valued functions on cuttings, arrived at as weights on pieces. Nothing
here identifies any of them with a physical quantity, and nothing here says any of them is
conserved by a process; each is reversed by moves of some sizes and kept by moves of others,
and the population the sizes are drawn from is fixed by the cost alone. What a space of
charges of this kind would mean for a lattice of many cells is not measured and is not
claimed.

Time enters only as the fourth column of the cell. Nothing in this cycle selects a direction
along it, and the tick flip is kept in the symmetry group throughout, so no result here
depends on an arrow.
