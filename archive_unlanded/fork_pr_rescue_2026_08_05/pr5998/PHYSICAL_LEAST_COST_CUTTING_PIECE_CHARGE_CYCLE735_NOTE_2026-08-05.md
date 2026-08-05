# A charge on the pieces of the single cell's least-cost cuttings — Cycle 735

Date: 2026-08-05

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

The object is one cell of the lattice carried through one tick of emergent time: the
four-cube on the sixteen corners of `{0,1}^4`, whose three spatial columns and single
tick column are the columns the axioms of
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supply, with nearest
neighbour adjacency only and the proper cubic rotations alone kept. A piece is a five
corner simplex of the cell of least volume; the cost of a piece counts the pairs of its
corners more than one lattice step apart, and the cost of a cutting is the sum over its
pieces. Earlier cycles measured the floor of that cost on this cell and the smallest cost
keeping change a cutting at the floor admits: that change replaces four pieces and flips
one region between its two cuts at the floor, so the local freedom of such a cutting is a
switch for each region it happens to fill. Whether those switches can be thrown
independently was left open. This cycle answers that they cannot, and finds what the
population carries in place of independence: free switch behaviour survives only to
dimension two, the coupling is exhibited as two switches sharing a piece, and every
cutting at the floor carries a two sided charge that is a sum over its own pieces, which
the smallest move always reverses and the next smallest move always keeps. Every statement
below is a check in whole numbers over an explicit finite set; no solver is used, and the
charge is exhibited as a weight on the pieces rather than asserted.

## The cell, the floor, and the regions

Of the 4368 five element subsets of the 16 corners, 2672 have the least volume and are the
pieces. They carry 2736 sample points with no collision between them and none on any
boundary, so containment is decided in whole numbers. The cell has 48 symmetries, counting
the 24 proper rotations against the tick flip, and the pieces fall into 57 orbits under
them.

The cost of a piece is 6 at the floor and 400 pieces reach it. A complete search over those
400 visits 502838 nodes and returns 15800 cuttings of 24 pieces each, which between them
use 192 of the 400. Every cutting therefore sits at cost 24 times 6.

The smallest cost keeping change replaces four pieces, and it occurs in 46128 ways across
the population. Those changes recut 120 regions. Each region holds exactly two cuts at the
floor, and the two cuts of a region share no piece, so a region is a genuine two way
switch rather than a family of overlapping fills.

## How many switches a cutting offers at once

Counting for each cutting how many of the 120 regions it fills gives

    0: 144    1: 192    2: 624    3: 1600    4: 2304    5: 1920    6: 4448
    7: 1344   8: 672    9: 1728  10: 192    12: 432   15: 192    24: 8

for 92256 region fillings in all, which is twice the 46128 smallest moves, as it must be
when every move joins two cuttings. Cutting by cutting the count of regions filled equals
the number of smallest moves leading out of that cutting, and no cutting holds both cuts of
any region. The population is wide: 144 cuttings have no local freedom at all, while 8 fill
24 regions at once, the most any cutting reaches.

## The switches are not independent

Joining two cuttings whenever a smallest move carries one to the other breaks the 15800
into 349 groups, of sizes

    1: 144    2: 96    4: 36    7: 48    236: 24    9320: 1

If the switches a cutting offers were independent, a group would be a cube on them: with
d switches free it would hold 2 to the power d cuttings and every cutting in it would meet
d moves. That happens 276 times, covering 480 cuttings, and every such group has dimension
0, 1 or 2. No other group has a number of cuttings that is a power of two at all, so the
free switch picture does not survive past dimension two anywhere in this population.

The smallest group in which the switches interact holds 7 cuttings spread over 4 regions
with 8 moves between them; one of its cuttings meets 4 of those moves and the rest meet 2,
against the 16 cuttings that four free switches would give.

The obstruction is visible piece by piece. Of the 273936 pairs of switches that some
cutting offers at once, 54912 are pairs whose two moves share a piece, so the two cannot
both be thrown; 8880 cuttings offer no such pair. The largest group holds 9320 of the
15800 cuttings with 33216 moves inside it, and its farthest member is 16 smallest moves
from the first, so more than half the population is one connected object under the
smallest move rather than a product of small independent ones.

The 349 groups fall into 14 orbits of the cell symmetry. The 144 cuttings with no smallest
move lie in 6 of them, and the largest group is carried to itself by all 48 symmetries.

## A two sided charge carried by the pieces

Ask for a weight on the 192 pieces in play, valued in the field with two elements, whose
sum over the 24 pieces of a cutting reverses under every smallest move. Because a smallest
move exchanges the two cuts of one region, this is one demand per region: the eight pieces
of a region's two cuts must carry an odd total weight. The 120 demands have rank 86 on the
192 pieces, they are consistent, they leave 106 weights free, and the labels they permit on
the cuttings reach 2 to the power 2. Asking as well that the sum be kept by every move on
six pieces raises the rank to 87, leaves 105 weights free, and cuts the labels to 2 to the
power 1.

The remaining freedom is not a second charge. The two labels differ on every one of the
15800 cuttings, so one is the complement of the other and they name the same two sided
split, of sizes 7704 and 8096. The partition is therefore determined; what is free is only
which side is called which.

The 120 region demands are not independent, and they are also not individually load
bearing. Drop any single one of them and the rank of what is left is still 86, so no
region pins the charge by itself. The 120 regions fall into 5 families under the cell
symmetry, and dropping a whole family does lower the rank: the family sizes against the
rank that survives run 12 against 84, 12 against 84, 24 against 75, 24 against 83, and 48
against 64. The charge is thus a global object held up by the symmetry families jointly,
not by any one region.

One solution of the system sits on 56 of the 192 pieces and puts the two cuts of all 120
regions on opposite sides. It is not slack: drop any single piece from that weight and at
least one region is left unsplit, the best single-piece weakening still separating 115 of
the 120.

## What the charge does on larger moves

Read back off the pieces, the charge meets both demands it was built from: every one of the
46128 smallest moves reverses it, and none of the 31968 moves on six pieces does. On larger
moves it was never told what to do, and it does both. Of the 60096 moves on seven pieces
26880 reverse it, and of the 151704 on eight pieces 28608 do. So the charge is not simply
reversed by every cost keeping move, nor kept by every one; among the move sizes measured
here it behaves uniformly at four pieces and at six, and is mixed at seven and at eight.

Reversal at six pieces is not merely absent but impossible. Asking instead that a move on
six pieces reverse the charge, with the same demand at four pieces kept, gives a system with
no solution over the field with two elements, so no weight on the pieces produces that
behaviour.

## What the charge is not

It is not free of the demand that it be a sum over pieces; that demand is what makes it a
single object. Dropping the requirement that the label be read off the pieces, and
asking only that it reverse at four and be kept at six, leaves one free sign for each of
the 157 groups the moves on four and six pieces produce together, that is 2 to the power
157 labellings. Reading it off the pieces is what cuts that down to a single partition.

It is not an accident of a chosen frame: all 48 symmetries of the cell carry the charge to
itself, and the 157 groups fall into 5 orbits under them.

It is not local in the pieces' own classification. No weight constant on the 4 families of
pieces will do: over all 16 such weights the best separates 48 of the 120 regions, and the
5 labels read from the parity of a coordinate sum separate 0. The charge distinguishes
pieces the natural coordinates do not.

It is not concentrated in one part of the population. Inside each group the split runs

    size 1 → 0 (144 groups)      size 2 → 1 (96)       size 4 → 2 (36)
    size 7 → 3 (48)              size 236 → 104 (24)   size 9320 → 4616 (1)

written as the size of the group, the smaller side of the charge inside it, and how many
groups do that. Only the singletons are unsplit, and they cannot be otherwise.

## The next move up, and the cuttings that cannot move at all

Of the 31968 moves on six pieces, 21696 join two cuttings already in the same group under
the smallest move, and every one of those joins a pair exactly two smallest moves apart, so
inside a group the six piece move adds nothing new. The other 10272 join two different
groups, and that is where the ladder tightens: allowing moves on four up to ten pieces
joins the cuttings into 349, 349, 157, 61, 61, 13 and 1 groups, of which 144, 144, 48, 48,
48, 0 and 0 hold a single cutting.

The hard core is 48 cuttings that admit no cost keeping move on eight pieces or fewer.
They form a single orbit of the cell symmetry, so the core is one shape, not a scattering.
Of the 144 cuttings with no smallest move, 96 gain one at six pieces and 48 do not; over
those 144 the count of moves on ten pieces or fewer takes the values 20, 60 and 80, each on
48 cuttings. All 48 of the core sit on the smaller side of the charge, so the charge places
the least free cuttings canonically.

## Independent cross-checks performed

The numbers in this section come from checks run outside the paired runner, by methods the
runner does not use; the runner does not print them.

Each headline was re-derived a second way. The move census was recomputed for all 124812100
pairs of cuttings by packed-bit exclusive-or against a popcount table rather than by the
Gram product the runner uses, giving 46128, 0, 31968, 60096 and 151704 moves on four
through eight pieces and the identical lists of pairs. The counts of cuttings with no move
at a given size were recomputed from that census and gave 144, 48 and 48. The groups were
found again by breadth-first search rather than by union find, giving 349 of the same sizes.
The two demands were met a third way by colouring the move graph by hand, which meets no
clash and needs 157 free signs. The ranks were recomputed by dense elimination on small
integer arrays rather than by big-integer bit masks, giving 86 and 87 with no inconsistent
row, and the flipped demand at six pieces leaves 480 inconsistent rows. The solution that
elimination finds for itself sits on 56 pieces, splits the cuttings 7704 against 8096, and
agrees with the runner's weight on every one of the 192 pieces. The 120 regions were
rebuilt from the move census alone, by reducing each smallest move to the unordered pair
of four piece sets it exchanges: that returns 120 regions, the same partition of the 46128
moves the runner builds, each region two cuts of four pieces sharing none, and carrying
them by the cell symmetry gives 5 families of sizes 12, 12, 24, 24 and 48.

Three checks were run to break the gates rather than to confirm them. Moving one piece out
of the exhibited weight drops the smallest moves it reverses from 46128 to 44206, so the
demand is a real test of the weight and not satisfied by any weight of that size. Applying
the free sign turns the charge into its own complement on every cutting, and the result
meets both demands and gives the same two sizes, confirming that the freedom names nothing
new. Of the 4 labels the demand at four pieces alone allows, 2 survive the demand at six,
so the second demand is not free.

## Boundary and honest read

The pool of 192 pieces, the 120 regions and their 5 families are measured by the search,
not derived from a symmetry statement. They are complete for this cell and this cost, and
the note claims nothing beyond that.

Two of the statements above are checks that the solve realised what was asked of it rather
than discoveries: that the charge reverses under all 46128 smallest moves and splits all
120 regions is what the system demanded. The content is elsewhere — that the system is
consistent at all, that adding the demand at six pieces keeps it consistent while the
reversed demand at six pieces does not, that the behaviour at seven and eight pieces was
never demanded and is mixed, that the 56 piece weight has no slack, and that no single
region demand is load bearing while every symmetry family is.

Every count here is scoped to the single cell of one lattice step and one tick, with the
adjacency cost and the least volume as defined above. No statement is made about cells of
other extent, other adjacency, other costs, or about the lattice as a whole; a claim of
that kind would need its own measurement. In particular the group sizes, the dimension two
ceiling on free switch behaviour, and the two sides 7704 and 8096 are properties of this
population of 15800 cuttings.

The charge is a two valued function on cuttings, arrived at as a weight on pieces. Nothing
here identifies it with a physical quantity, and nothing here says it is conserved by any
process; it is reversed by one class of moves and kept by another, and both classes are
defined by the cost alone. What a charge of this kind would mean for a lattice of many
cells is not measured and is not claimed.

Time enters only as the fourth column of the cell. Nothing in this cycle selects a
direction along it, and the tick flip is kept in the symmetry group throughout, so no
result here depends on an arrow.
