# Ten of the cell's eleven nearest-neighbour costs obey a parity law, and the eleventh forces which pieces a dissection may use

Status: unaudited source note. Cycle 733 of the emergent-geometry lane.

## What this settles

The previous cycle proved that one particular cost — the adjacency charge, which reads
the three lattice columns of the cell and ignores the tick — is even on every dissection.
That proof exhibited a certificate. It did not say whether the evenness is a property of
that one cost or of the way costs of this kind are built.

This note settles that by measuring the whole family at once. A cost is fixed by choosing
a set of columns of the cell and counting, for each piece, the pairs of its corners that
are more than one step apart when only those columns are read. There are fifteen such
sets. The four single columns give the cost that is zero on everything, so eleven costs
remain, and not one of them is blind to how the cell is cut: each takes at least two
values on the thirteen dissections exhibited here.

Ten of the eleven obey a parity law, each with its own certificate produced by exact
elimination and verified against all 2672 pieces. The eleventh does not, and the eleventh
is exactly the one that reads all four columns at once — the cost that sees the lattice
and the tick together. Its failure is not a failure to find a certificate. Four pieces
are exhibited that cover 228 sample points exactly twice and everything else not at all,
with costs summing to the odd number 25, and no parity rule can survive that.

So the parity law is a property of the proper subsets of the columns, and the full
spacetime cost is the single member of the family that escapes it. Where the escape lives
can be said exactly. On every one of the 2672 pieces the full cost splits as the spatial
cost plus the number of corner pairs that step in the tick and in exactly one lattice
direction; drop that second term and the identity survives on only 64 pieces. The spatial
part is even on every dissection. The odd part of the spacetime cost is carried entirely
by the tick-coupled pairs.

The cost that breaks the law is also the one that behaves best under minimisation, and
that is the second result here. Its floor needs no certificate at all: no piece costs
under 6, so no dissection costs under 144, and 144 is reached — by the dissection built
from the 24 monotone paths through the cell, one for each ordering of the four columns. A
complete search then shows the minimum is rigid. There are 15800 dissections of least
spacetime cost. They draw their pieces from 192 of the 400 pieces of least cost — four
whole orbits of the cell's symmetry — and each of the four is needed: drop any one and
the remaining 352 pieces admit no dissection at all. The other 208 pieces of least cost
never appear in any minimiser.

The rigidity goes one level further. Take a dissection of least spacetime cost and remove
any single piece; the hole left behind is filled by the piece just removed and by nothing
else in the cell. Over all 15800 minimisers that is 379200 holes with no alternative.

Finally, the exclusion of those 208 pieces is invisible to the symmetric costs and
visible to the rest. Exactly two of the eleven costs are constant on the cell's piece
orbits — the spatial cost and the spacetime cost — and the pair of values they take on
the pieces that survive is a strict subset of what they take on the pieces excluded, so
they cannot tell the two sets apart. The full family can: the 192 surviving pieces carry
12 distinct vectors of the eleven costs, the 208 excluded ones carry 13, and no vector
occurs in both.

All of this concerns the single cell. Its inputs are the lattice adjacency of
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) and nothing else.

## Objects

The cell is the 4-cube on 16 corners: three lattice coordinates and one tick, each corner
a point of `{0,1}^4`. A piece is a set of five corners; 4368 exist and 2672 have least
nonzero volume. Those 2672 are the pieces a dissection may use, and a dissection uses 24
of them, because the cell has volume 1 and each such piece has volume one twenty-fourth.

For a set of columns, the cost of a piece counts the pairs of its five corners whose
distance exceeds one when only those columns are read. Because every coordinate is 0 or
1, that is the number of pairs differing in at least two of the chosen columns — which is
why each single column gives the zero cost. The cost of a dissection is the sum over its
24 pieces. On the three lattice columns this is the adjacency charge of earlier cycles,
with spectrum `[(3, 64), (4, 384), (5, 1152), (6, 768), (7, 304)]`; on all four columns
it is the spacetime cost, with spectrum `[(6, 400), (7, 1216), (8, 864), (9, 192)]`. The
family is monotone: adding a column never lowers the cost, on all 15 sets.

The cell keeps 24 proper rotations, and with the tick flip the symmetry group has 48
elements, acting on the pieces with 57 orbits of sizes 16 and 48. Each of the 48
permutes the 2672 pieces. Because the group permutes the three lattice columns and fixes
the tick, it also acts on the eleven costs, splitting them into 5 classes by how many
lattice columns the set holds and whether it holds the tick, of sizes `[1, 1, 3, 3, 3]`;
all 29 ordered pairs inside a class are joined by an exhibited symmetry. Exactly 2 of the
eleven are constant on the piece orbits, and they are the two sets no column permutation
can move: `(0, 1, 2)` and `(0, 1, 2, 3)`.

Sample points are placed so that none lies on a piece boundary. Superincreasing weights
with total 12810 and barycentric bound 3 give 2736 of them, none on a boundary, in 57
orbits of size 48. Each piece contains between 6 and 409 of them, and each point lies in
between 90 and 224 pieces, so the incidence has no empty row and no empty column. That no
point lies on a boundary is the load-bearing property: every sample point is interior to
exactly one piece of any dissection whatsoever, so a congruence that holds piece by piece
sums over a dissection with no hypothesis about how that dissection was built.

## Method: certificates, complete searches, and no solver

The runner exhibits objects and checks them. It calls no optimiser.

A parity certificate for a cost is a set of sample points together with a constant such
that, for every piece of least volume, the number of certificate points inside the piece
plus the constant is congruent modulo 2 to that piece's cost. Each of the ten
certificates here is produced inside the runner by exact Gaussian elimination over the
field of two elements — no list of point indices is transcribed by hand — and then
checked against all 2672 pieces, with 0 wrong rows.

The step from the piece congruence to the dissection statement carries no constant
bookkeeping. A dissection has 24 pieces and 24 is even, so the copies of the constant
contribute an even amount whatever the constant is. The law is therefore that the cost of
any dissection agrees modulo 2 with the size of the certificate's point set, and all ten
sizes are even: `[234, 232, 212, 210, 214, 234, 168, 238, 270, 246]`.

Because the certificate is produced by elimination rather than exhibited from a list, the
runner also produces a second one for each of the ten by eliminating the columns in the
opposite order. It differs from the first on all 10 sets, reproduces every piece row just
as well, and always has a support of the same parity. The law does not depend on which
certificate is picked.

The refutation at the full column set is exhibited, not inferred from a failed search.
Four pieces are given whose incidence with the sample points covers 228 of them exactly
twice and the rest not at all. Any parity rule would have to give that doubled cover an
even total; the four spacetime costs sum to 25. Dropping any one of the four destroys the
even cover, so the witness is minimal as given.

The dissections are pinned as twelve explicit 24-tuples, and a thirteenth — the monotone
stencil — is built inside the runner from the 24 orderings of the four columns, each
ordering giving the path from the all-zero corner to the all-one corner that switches the
columns on in that order. All thirteen are verified from scratch: 24 distinct pieces of
least volume, pairwise disjoint by an exhibited integer separating direction, and every
one of the 2736 sample points covered. Volume and disjointness together make the cover
exact without a solver being asked anything.

The search over the 400 pieces of least spacetime cost is complete, not sampled: it
visits 502838 nodes and returns all 15800 dissections. The same search with one orbit of
pieces removed is run four times and returns nothing each time.

The rigidity test is exact and needs no search at all. In a dissection the 24 pieces are
disjoint and cover the cell, so a piece filling the hole left by removing one of them
must have a footprint equal to the complement of the pieces that remain, not merely
contained in it. All 2672 footprints are distinct, so a single dictionary lookup answers
the question for each hole, and the lookup is confirmed to return the removed piece every
time.

Exact elimination over a finite field, verification of exhibited integer objects, and
complete enumeration over explicit finite sets are all arithmetic, not search.

## Results

**The family reduces to eleven costs in five classes.** Of the 15 column sets the 4
single columns give the zero cost. The remaining 11 fall into 5 classes of sizes
`[1, 1, 3, 3, 3]` under the cell's symmetries, with all 29 ordered pairs inside a class
joined by an exhibited symmetry. The family is monotone under adding columns, and every
one of the 11 takes at least two values on the 13 dissections, so none of them is a
quantity that a dissection cannot change.

**Parity is a law for all ten proper column sets.** Each of the 10 carries a certificate
over the field of two elements that reproduces the cost of every one of the 2672 pieces,
with even support. Every dissection therefore has even cost under each of the ten, and
this is confirmed directly on all 13 exhibited dissections. The law survives replacing
each certificate by the one obtained from the opposite elimination order, which differs
on all 10 sets while keeping the support parity.

**The law breaks exactly at the full column set, and the break is exhibited.** The
spacetime cost takes the values `[144, 163, 164, 165, 167, 168, 170]` on the 13
dissections — both parities occur, so no congruence modulo 2 can hold. Independently of
that, the four-piece doubled cover of 228 points with odd cost sum 25 rules out any
certificate whatsoever, and dropping any one of the four destroys it.

**The odd part is located.** On all 2672 pieces the spacetime cost equals the spatial
cost plus the count of corner pairs that step in the tick and in exactly one lattice
direction. Without that second term the identity holds on only 64 pieces. Since the
spatial cost is even on every exhibited dissection, the parity of the spacetime cost is
carried entirely by the second term. The cost that breaks the law is the one that couples
the tick to the lattice, and the coupling is where the breakage sits.

**The floor of the spacetime cost is exact and needs no certificate.** The cost of a
single piece runs over `[(6, 400), (7, 1216), (8, 864), (9, 192)]`. No piece costs under
6, so no dissection costs under 144 — that much is immediate from the spectrum. What is
measured is that 144 is attained, by the monotone stencil. Minimality alone pins the
floor, with no weight system involved.

**The minimum forces four whole orbits of pieces.** A complete search over the 400 pieces
of least cost visits 502838 nodes and finds 15800 dissections, falling into 391 orbits of
sizes `[8, 12, 24, 48]`. The pieces they use are 4 whole orbits of the symmetry, 192
pieces in all, and the other 208 pieces of least cost are never used by any minimiser.
Each of the four orbits is needed: with any one of them removed, the remaining 352 pieces
of least cost admit no dissection at all. The monotone stencil takes six pieces from each
of the four.

**Least spacetime cost implies least spatial cost.** Every one of the 15800 minimisers
splits as spatial cost 108 and second term 36, and every piece any of them uses sits on
the exhibited spatial floor support of 1792 pieces from the previous cycle. The
implication is one-way: an exhibited dissection has spatial cost 108 and spacetime cost
163, so a least spatial cost does not force a least spacetime cost.

**The minimisers are rigid piece by piece.** All 2672 footprints are distinct. Of the
379200 holes made by removing one piece from one of the 15800 minimisers, each is filled
by the piece just removed and by no other piece of the cell — not by another piece of
least cost, and not by any of the 2672 at all.

**The symmetric costs cannot see the exclusion; the rest of the family can.** The two
costs the symmetries keep fixed take values `[((4, 2), 96), ((5, 1), 96)]` on the 192
pieces that survive and `[((3, 3), 64), ((4, 2), 96), ((5, 1), 48)]` on the 208 excluded,
a strict superset, so no rule reading only those two can separate them. The whole family
separates them completely: 12 distinct vectors on the surviving pieces, 13 on the
excluded, 0 in common. Those 12 and 13 account for all 25 vectors carried by any piece of
least cost, so the surviving pool is exactly a union of level sets of the family. That is
not automatic — three other splits of the same 400 pieces into the same two sizes share
`[25, 12, 6]` vectors.

## Independent cross-checks performed

Every headline above was re-derived by a method the runner does not use, and every new
gate was tested against a perturbed object to confirm that it discriminates. These checks
were run in separate probes, not inside the artifact; the counts reported in this section
are therefore theirs, and are not among the numbers the runner prints.

Flipping a single weight of any one of the ten certificates breaks 137 of the 2672 piece
congruences, so the row check is not satisfied by accident. Perturbing the target parity
vector instead — flipping every third entry — leaves all ten uncertifiable, so the
elimination genuinely sees the target rather than solving something trivially consistent.

The four-piece refutation was tested against every single-piece substitution: of the
10672 ways to replace one of the four by some other piece, none again gives a doubled
cover with odd total.

The claim that the second term is the right one was tested by replacing it with the count
of pairs stepping in the tick and in two lattice directions, and again in three. The
identity then holds on 816 and 384 of the 2672 pieces respectively, against 2672 for the
term used.

Each of the nine costs that are not constant on the piece orbits was given an explicit
orbit on which it takes more than one value, so the count of exactly two orbit-constant
costs is witnessed on both sides.

The claim that the family separates the surviving pool was tested for genericity. Three
deterministic splits of the same 400 pieces into groups of 192 and 208 — by piece index,
by spatial cost, and by orbit label — share 25, 12 and 6 vectors. A clean separation is
therefore a property of the pool the minimum principle selects, not of the sizes.

Four checks changed the artifact rather than confirming it, and they are worth recording.
The first draft took the stencil to be one of the pinned dissections that happened to
have spatial cost 108; nothing established that it was the monotone one, so the stencil is
now constructed from the 24 orderings of the columns and gated as a dissection in its own
right. The floor gate originally also asserted that no piece costs below the minimum,
which is true by definition of a minimum and measures nothing; it was removed. The
rigidity gate originally counted only alternative pieces filling a hole, which would have
read zero had the lookup been malformed; it now also confirms that the removed piece is
found, on all 379200 holes. And an earlier check of rigidity covered 8 of the 391 orbit
representatives rather than all 15800 minimisers; the artifact now does the complete
version, which is affordable because the exact footprint test costs one lookup per hole.

One planned claim was refuted outright by measurement and the note states the narrower
truth instead. The intention was to report that no quantity in this family can see which
pieces the minimum principle keeps out. That is false: the family separates the two sets
completely, with no vector in common. What is true, and is what the note claims, is that
the two costs invariant under the cell's symmetries cannot see the exclusion, while the
nine that break the symmetry do.

## Boundary and honest read

The parity law is about this cell. It is proved by exhibiting certificates for this
cell's 2672 pieces and says nothing about any other object. An earlier cycle's attempt at
a parity law across objects was refuted, and nothing here revives it.

The certificates were found by elimination, so this note does not claim any of them is
the smallest. What is claimed is that they work, and that the law they establish does not
change when the certificate does.

The floor of the spacetime cost at 144 is exact. Its ceiling is not addressed here at
all; this note says nothing about how large the spacetime cost of a dissection can be,
and the 13 exhibited values are not a spectrum claim.

The forcing result is about the pieces, not about a rule that predicts them. Knowing a
piece's vector of eleven costs does determine whether it lies in the surviving pool, but
the note exhibits no rule that produces the pool without running the search. The pool is
measured, not derived.

The 15800 minimisers are counted for the spacetime cost only. That every one of them also
has least spatial cost is measured on all of them; the converse is refuted by an
exhibited dissection, so the two minimum principles are not the same principle.

That the spatial floor support of 1792 pieces contains every piece the minimisers use is
inherited from the previous cycle's weight system and re-verified here, not re-derived.

## Artifacts

- Runner:
  `scripts/physical_column_family_parity_law_forced_orbits_cycle733_2026_08_04.py`
- Recorded output:
  `outputs/physical_column_family_parity_law_forced_orbits_cycle733_2026_08_04_cold_2026-08-04.txt`
- Receipt:
  `outputs/physical_column_family_parity_law_forced_orbits_cycle733_2026_08_04_receipt_2026-08-04.json`

The runner reports `TOTAL: PASS=41 FAIL=0`. Every number quoted above appears in that
output, apart from the cross-check counts named as such in their own section.
