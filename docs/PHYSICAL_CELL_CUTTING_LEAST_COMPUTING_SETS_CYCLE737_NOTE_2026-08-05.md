# The fewest pieces that compute a charge — Cycle 737

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
corner simplex of the cell of least volume, the cost of a piece counts the pairs of its
corners more than one lattice step apart, and the cuttings at the floor of that cost are
the population of the last cycles. The previous cycle showed that the two valued charges
answering the smallest move uniformly form a space of dimension three — the two constants
and three two sided charges, named four, six and seven for the move size each keeps — and
that each is carried by a weight over all 192 pieces the cuttings use. This cycle asks how
little of the cell a charge actually needs. A set of pieces computes a charge when, for
every one of the 15800 cuttings, the parity of the count of its pieces falling in the set
is the charge's value on that cutting. The answers are exact where the search is complete
and bracketed where it is not. Every computing set of any of the eight
charges has even size, because each of the 192 pieces is used by an odd number of
cuttings and every charge takes the value one on an even count of them. A complete search
of every set of at most
eight pieces finds the smallest sets a cutting cannot see — sets met evenly by every
cutting — at exactly eight pieces, 648 of them, and the smallest sets met oddly by every
cutting, likewise at eight, 192 of them; both families are unions of full symmetry orbits
and each touches all 192 pieces. The eight pieces of any octet share exactly two corners
of the cell, and for the odd family the shared pair is always an edge, six octets on each
of the 32 edges. No physical charge is computable from eight pieces or
fewer, so with parity every one of the six needs at least ten. Explicit computing sets of
sizes 16, 20, 24, 24, 30 and 30 are exhibited and verified, so the least sizes lie
between ten and those numbers. The 648 eight piece sets met evenly by every cutting are
disjoint from the 120
exchange masks of the smallest move, and no indicator of a symmetry orbit of pieces is
expressible from cutting rows at all, so the octet families are new objects, neither the
moves nor the orbits. Every statement below is a check in whole numbers over an explicit
finite set; no solver is used, and completeness of the search is certified inside the
runner rather than assumed.

## The cell, the cuttings, and the charges

Of the 4368 five element subsets of the 16 corners, 2672 have the least volume and are the
pieces. The adjacency cost has floor 6 over the pieces, 400 pieces attain it, and the
complete search of the previous cycles cuts the cell into 24 such pieces in 15800 ways,
using 192 of the 400. The 48 symmetries of the cell — the 24 proper spatial rotations,
each with and without the tick flip — act on the cuttings and on the pieces; on the 192
used pieces the action is free, with four orbits of 48. The three two sided charges and
their flips take the value one on 7704, 8096, 7424, 8376, 5664 and 10136 cuttings for six,
six flipped, seven, seven flipped, four and four flipped respectively. These counts, the
population and the charge space are the previous cycle's results and are reproduced here
because the question is asked of them.

## What it means for a set of pieces to compute a charge

Write the population as its use table: one row per cutting, one column per used piece, an
entry marking use. A set of pieces computes a two valued function when the parity of each
row's overlap with the set equals the function's value on that row. Two sets compute the
same function exactly when their symmetric difference is met evenly by every cutting, so
the sets a cutting cannot see are the ambiguity of the whole question: call a set every
cutting meets evenly an even set, and a set every cutting meets oddly an odd set. The even
sets compute the constant zero, the odd sets compute the constant one, and the computing
sets of any fixed charge form a single class under symmetric difference with even sets.
The charges themselves are columns of the previous cycle's charge space, so at least one
computing set exists for each; the question is the least size.

## Sizes are even

Each of the 192 used pieces is used by exactly 1975 cuttings, an odd count. Summing all
15800 rows of the use table therefore gives the all ones vector: the whole population,
taken together, meets every set of pieces with the parity of the set's size. So a set of
even size computes a function taking the value one on an even number of cuttings, and a
set of odd size a function taking one on an odd number. All eight charges take the value
one on an even count of cuttings — 0, 15800, 5664, 10136, 7704, 8096, 7424 and 8376 —
so every computing set of any of them has even size. Odd sizes are settled before any
search: nine pieces can no more compute a charge than one piece can.

## The complete search below ten

All sets of at most eight pieces are searched. Completeness does not rest on trying the
sets one by one: the runner first certifies, by exhibiting the combinations of rows that
realize them, that the all ones indicator over the 192 pieces and the indicator of a fixed
half of the columns are both sums of cutting rows with even overlap forced against every
target searched, which confines solutions to even counts on each half of a fixed ordering; the
search then covers every such split by three routes — two stored tables met in the middle,
a streamed heavy side against a stored light side, and a within half sweep over quarter
splits including the odd ones, which the certificate does not cover. Each route is
exercised on planted sets rebuilt from their own rows before the real targets are run, a
deliberately odd synthetic target is shown to force odd overlap — so the certificate can
fail — and every set the search returns is verified against all 15800 rows.

The search returns, for the constant zero, no even set of size two, four or six, and
exactly 648 even sets of size eight. For the constant one it returns no odd set below
eight and exactly 192 odd sets of size eight. For the six charges it returns nothing at
all through size eight. With parity, the least size of a computing set of every physical
charge is at least ten.

## The two octet families

Call the 648 smallest even sets and the 192 smallest odd sets the even octets and the odd
octets. Both families are closed under the 48 symmetries exactly: the even octets fall
into 22 orbits, seventeen of size 24 and five of size 48, and the odd octets into five
orbits, two of size 24 and three of size 48. Each family, taken together, touches all 192
used pieces. Across the four symmetry classes of pieces the even octets spread as
(0,0,4,4) in 120 cases, (0,2,2,4) in 48, (1,1,3,3) in 192 and (2,2,2,2) in 288, each
spread the ordered counts smallest first without naming the classes; the odd octets show
the same four spreads with exactly 48 sets at each.

Geometry pins both families further. Over the 192 used pieces every corner of the cell
lies on exactly 60 and every edge, tick or spatial, on exactly 24; constancy within each
kind is forced by the symmetries, which carry any corner to any corner and any edge of a
kind to any edge of the same kind, while the shared value 24 across the two kinds is
measured, not forced. In both families the eight pieces of an octet share exactly two
corners of the cell. For the odd octets the shared pair is always an edge: each of the 32
edges carries exactly six of the 192 odd octets, evenly across the four directions, and
each odd octet's pieces together touch all sixteen corners. For the even octets every one
of the 120 corner pairs occurs as a shared pair, and the count of octets on a pair depends
only on the number of coordinates in which its corners differ: nine on each of the 32
pairs differing in one coordinate, the edges; three on each of the 48 pairs differing in
two coordinates and each of the 32 differing in three; fifteen on each of the eight pairs
differing in all four, the opposite corners of the cell. The corners an even octet touches
number ten, twelve or sixteen — in
240, 120 and 288 cases — and follow the shared pair: pairs differing in two or three
coordinates always give ten, edge pairs give twelve in 96 cases and sixteen in 192, and
opposite pairs give twelve in 24 cases and sixteen in 96.

## The charges need ten or more

Through size eight the search is complete and empty for all six physical targets, and odd
sizes are excluded by parity, so 10 is a floor. From above, explicit computing sets are
exhibited: a set of 16 pieces computes the four charge and a set of 20 its flip, sets of
24 compute the six charge and its flip, and sets of 30 the seven charge and its flip.
Each is verified against all 15800 cuttings inside the runner. The least sizes therefore
lie in the even numbers from ten to the exhibited sizes.
The exhibited sets were found by a seeded randomized basis search outside the runner; the
runner verifies them and claims only what verification shows, that the sizes suffice.

## What the octets are not

The previous cycle's smallest move exchanges four pieces for four others, and the 120
distinct exchange masks each involve eight pieces. None of the 120 is an even set — every
one is seen by some cutting — and none of the 648 even octets is an exchange mask; the
overlap of the two eight piece families is empty. The smallest sets the population cannot
see are not the moves.

The four symmetry orbits of pieces are the cell's natural classes, and one could ask
whether every computing set of a given charge meets each orbit with a forced parity. It
does not: no orbit indicator is a sum of cutting rows, so no such constraint exists, and
computing sets can shift weight between orbits freely. The forced parities that do exist —
the total and the certified half — do not include any symmetry orbit.

The three two sided charges satisfy one relation worth recording at the level of
functions: the four charge equals the sum of the six charge, the seven charge and the
constant one, and not the bare sum of six and seven; the offset by the constant is real
and is checked both ways.

## Independent cross-checks performed

The runner re-derives the machinery it stands on — pieces, floor, cuttings, symmetries,
charge values — rather than loading any of it. The membership certificates are produced by
exact elimination over the integers modulo two, and their forced parities are printed and
gated; the deliberately odd synthetic target shows the same machinery returning odd, so
the even verdicts discriminate. Four planted sets are recovered by the same code paths
that report the real counts, covering every search route, the odd quarter split inside a
half among them. Every returned set is checked against the full use table, the families
are checked to be duplicate free across routes, orbit closure is checked exactly — the
image of every returned set under all 48 symmetries is again a returned set — and the
witness sets are pinned to the cell by their pieces' corner tuples and checked against
the full table, with their sizes' parity confirmed even.
The split counts of the octet families across the certified halves are printed by the
runner as bookkeeping of the search's coverage.

## Boundary and honest read

The search is complete for sets of at most eight pieces and for the twelve targets named;
nothing is measured about size ten and above except the exhibited witnesses, so for each
physical charge the least size is known only to lie between ten and its witness size. The
witnesses come from a randomized search whose seed and sample count are fixed outside the
runner; the runner's claim about them is verification, not optimality. The population, the
floor, the 192 pieces, the charge values and the 120 exchange masks are reproductions of
earlier cycles' measurements, derived again inside the runner where they appear; the
content of this cycle is the parity law, the completeness certificates, the two octet
families with their orbit structure, spread and geometry, the ten piece floor for all six
charges, the verified upper sizes, and the two separations — octets from exchange masks,
and forced parities from orbit indicators.

The halves and quarters of the column ordering are bookkeeping of the search, not objects
of the cell: no symmetry exchanges the halves, and the certified half indicator is a
property of the use table under one fixed ordering, exhibited inside the runner for the
sake of a complete search and claimed for nothing else.

Every count here is scoped to the single cell of one lattice step and one tick, with the
adjacency cost and the least volume as defined above. No statement is made about cells of
other extent, other adjacency, other costs, or about the lattice as a whole. The charges
are two valued functions on cuttings arrived at as parities of piece use; nothing here
identifies any of them with a physical quantity, and what a least computing set would mean
for a lattice of many cells is not measured and is not claimed.

Time enters only as the fourth column of the cell. Nothing in this cycle selects a
direction along it, and the tick flip is kept in the symmetry group throughout, so no
result here depends on an arrow.
