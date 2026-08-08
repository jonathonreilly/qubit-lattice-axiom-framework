# Ten pieces compute no charge — Cycle 738

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
the population of the last cycles. The previous cycle proved that every set of pieces
computing any of the eight charges — the two constants and the three two sided charges
with their flips — has even size, found the smallest sets every cutting meets evenly and
the smallest it meets oddly at exactly eight pieces, 648 and 192 of them, and left the six
physical charges with a floor of ten: none is computable from eight pieces or fewer. This
cycle searches ten completely. Exact elimination inside the runner certifies which
parities a computing set must carry — among the whole set, the two halves, the four
quarters and the eight blocks of twenty four pieces of the fixed column ordering, a forced
parity exists for exactly the whole, the halves and the two quarters of the second half —
and the cells of quarter splits those certificates license are then covered in full, 146
of them across the eighteen readings in play. The search returns nothing: no set of
exactly ten pieces computes any of the six physical charges, and there is no even set and
no odd set of ten pieces at all. With parity, every one of the six charges needs at least
twelve pieces, and both octet families are isolated — the next even set and the next odd
set lie at twelve pieces or beyond. The search is not trusted on its word: the sizes below
ten are rerun by the same engine first and return exactly the previous cycle's answers,
control readings built from explicit sets are carried at ten by exactly 108, 1, 2 and 0
sets, five planted ten piece readings are each recovered, and every verified return is
checked against all 15800 cuttings. Every statement below is a check in whole numbers over
an explicit finite set; no solver is used, and completeness of the search is certified
inside the runner rather than assumed.

## The cell, the cuttings, and the charges

Of the 4368 five element subsets of the 16 corners, 2672 have the least volume and are the
pieces. The adjacency cost has floor 6 over the pieces, 400 pieces attain it, and the
complete search of the previous cycles cuts the cell into 24 such pieces in 15800 ways,
using 192 of the 400. The 48 symmetries of the cell — the 24 proper spatial rotations,
each with and without the tick flip — act on the cuttings and on the pieces; on the 192
used pieces the action is free, with four orbits of 48. The three two sided charges and
their flips take the value one on 7704, 8096, 7424, 8376, 5664 and 10136 cuttings for six,
six flipped, seven, seven flipped, four and four flipped respectively; the constants zero
and one hold on 0 and 15800. As rows over the field with two elements the 15800 cuttings
span 88 dimensions, and the sets that carry the constant zero form a space of dimension
104. These counts, the population and the charge space are the previous cycles' results
and are reproduced here because the question is asked of them.

## What it means for a set of pieces to compute a charge

Write the population as its use table: one row per cutting, one column per used piece, an
entry marking use. A set of pieces computes a two valued function on cuttings — a reading
— when the parity of each row's overlap with the set equals the function's value on that
row. Two sets compute the same reading exactly when their symmetric difference is met
evenly by every cutting: the even sets compute the constant zero, the odd sets the
constant one, and the computing sets of any fixed charge form a single class under
symmetric difference with even sets. The previous cycle found the smallest even sets and
the smallest odd sets at exactly eight pieces — the even and odd octets — and nothing for
the six charges through eight. This cycle asks for the next size: whether ten pieces
compute a charge, and whether any even or odd set of ten pieces exists.

## Sizes are even

Each of the 192 used pieces is used by exactly 1975 cuttings, an odd count. Summing all
15800 rows of the use table therefore gives the all ones vector: the whole population,
taken together, meets every set of pieces with the parity of the set's size. All eight
readings take the value one on an even count of cuttings — 0, 15800, 5664, 10136, 7704,
8096, 7424 and 8376 — so every computing set of any of them has even size, and odd sizes
are settled before any search. The sizes in question are ten and twelve, not nine or
eleven.

## Which parities are forced

The search at ten stands on certificates produced before it runs. Fix the column ordering
of the 192 pieces once, and cut it into two halves, four quarters and eight blocks of
twenty four. A block carries a forced parity against a reading when its indicator is a sum
of cutting rows over the field with two elements: any computing set must then meet the
block with the parity those rows' reading values add to, whatever else the set does. Exact
elimination decides membership for every one of these blocks. A forced parity exists for
exactly the whole set, the two halves and the two quarters of the second half; the whole
and the halves force even overlap on all 17 readings the certificate covers, and each of
the two forced quarters forces the pattern [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1,
0, 1] over them — even on the eight readings, even or odd on the controls as their
construction dictates. Neither quarter of the first half nor any of the eight blocks of
twenty four carries a forced parity, so a search may split those freely: 10 free blocks.
The machinery is exercised in both directions. Each of the five planted ten piece readings
forces exactly the whole, half and quarter parities its own construction has. A synthetic
reading of odd total parity forces an odd whole, which no set of ten pieces can meet: it
licenses 0 cells and the sweep returns 0 sets — the license can fail, so the licenses that
pass discriminate.

## The rerun below ten

The engine that will run ten is checked against the previous cycle's complete search
first, through the same licensed cell machinery. Sizes two, four and six license 5, 14 and
30 cells and return nothing for any of the eight readings. Size eight licenses 55 cells
and returns exactly the 648 even octets, the 192 odd octets, and nothing for any of the
six charges. Each of the 840 returned octets is verified piece by piece against all 15800
cuttings with 0 mismatched. The two families close under the 48 symmetries exactly, in
orbits of sizes 24 and 48 — seventeen and five of them for the even family, two and three
for the odd — and the 648 even octets span the full 104 dimensional space of even sets, as
do the differences of the 192 odd octets. The engine reproduces the previous cycle's floor
before it is trusted at the frontier.

## The complete search at ten

Every set of ten pieces splits its ten across the four quarters somehow. A split that
violates a forced parity for a reading carries no computing set of that reading, so the
licensed cells — the splits meeting every forced parity — cover every candidate, and
covering them all is a complete search. The eighteen readings license 146 cells at ten,
and the runner covers each in full, meeting stored quarter tables in the middle and
tallying every computing set of every reading licensed there.

The result is the count vector [0, 0, 0, 0, 0, 0, 0, 0, 108, 1, 2, 0, 2, 1, 1, 1, 1, 0]
over the eighteen readings: nothing for the constant zero, the constant one, or any of the
six physical charges, and for the ten control readings exactly what must be there. A
control reading built from an explicit set spread evenly across the two halves is carried
by exactly 108 sets of ten pieces; one built from a set spread unevenly across them, by 1;
one built from a set lying inside the first half, by 2; one built from a set inside a
single quarter of the second half, by 0 — that reading has computing sets, its own pieces
among them, but none of size ten. The five planted ten piece readings are carried by 2, 1,
1, 1 and 1 sets, and in every case the planted set itself is among the returns. Of the
returned sets, 109 — up to 100 per reading — are verified piece by piece against all 15800
cuttings with 0 mismatched, and no reading returns a set twice.

## The floor moves to twelve

For each of the six physical charges the search is now complete and empty at two, four,
six, eight and ten pieces, and every odd size is barred by parity, so every one of the six
needs at least twelve pieces. The previous cycle exhibited and verified explicit computing
sets for all six, so each least size lies in the even numbers from twelve up to its
witness size there. The floor the previous cycle set at ten stands at twelve.

## The octet families are isolated

The same completeness answers the octet question. The sets every cutting meets evenly
number 0 below eight pieces, 648 at eight, and 0 at ten; the sets every cutting meets
oddly number 0, 192 and 0. In the 104 dimensional space of even sets the least weight is
eight, and the next weight is not ten: the octets are followed by a gap, and the next even
set and the next odd set both have twelve pieces or more. Every one of the 48 symmetries
of the cell permutes the 15800 cuttings among themselves, 8 of the 18 readings are unmoved
by all of them, and the sets carrying those readings map onto one another under the action
— so the emptiness at ten and the two octet families are symmetry consistent verdicts,
checked exactly rather than assumed.

## Independent cross-checks performed

The runner re-derives the machinery it stands on — pieces, floor, cuttings, symmetries,
charge values, the rank of the use table — rather than loading any of it. The certificates
are produced by exact elimination over the integers modulo two, and their forced parities
are printed and gated. Two synthetic readings are shown to fail the license machinery
honestly: one, built from pieces 5, 17, 60 and 130, has forced left half parity odd, and
one of odd total parity licenses no cell at ten at all. The known answers below ten are
recomputed by the same engine that runs the frontier — 5, 14, 30 and 55 licensed cells,
nothing below eight, 648 and 192 at eight — so the engine is checked against a complete
search before its empty verdict at ten is believed. Five planted ten piece readings are
recovered through the same code paths that report the real counts, odd quarter splits
among their cells. Every verified return is checked piece by piece against all 15800
cuttings — 840 octets at eight, 109 ten piece sets, up to 100 per reading, all with 0
mismatched — the returns are duplicate free within each reading, and orbit closure under
all 48 symmetries is checked exactly on the families of the unmoved readings.

## Boundary and honest read

The search is complete for sets of exactly ten pieces and the eighteen readings named, on
top of the previous cycle's completeness through eight; nothing is measured above ten, so
for each physical charge the least size is known only to lie between twelve and the
witness size the previous cycle verified. The population, the floor, the 192 pieces, the
charge values, the parity law and the eight piece families are reproductions of the
previous cycle's measurements, derived again inside the runner where they appear; the
content of this cycle is the full forced parity certificate over halves, quarters and
blocks, the licensed cell coverage argument, the empty complete search at ten for all
eight readings, the floor of twelve for the six charges, and the isolation of both octet
families.

The ten level search is one engine design. Its coverage is certified by the licensing
argument, its known answers reproduce the previous cycle's complete search, its returns
are verified row by row and closed under symmetry where symmetry applies, and its planted
readings are recovered — but a second, independently designed search at ten is not among
this cycle's checks, and the empty verdict carries that residual.

The halves, quarters and blocks of the column ordering are bookkeeping of the search, not
objects of the cell: which blocks carry forced parities is a property of the use table
under one fixed ordering, exhibited inside the runner for the sake of a complete search
and claimed for nothing else.

Every count here is scoped to the single cell of one lattice step and one tick, with the
adjacency cost and the least volume as defined above. No statement is made about cells of
other extent, other adjacency, other costs, or about the lattice as a whole. The charges
are two valued functions on cuttings arrived at as parities of piece use; nothing here
identifies any of them with a physical quantity, and what a least computing set would mean
for a lattice of many cells is not measured and is not claimed.

Time enters only as the fourth column of the cell. Nothing in this cycle selects a
direction along it, and the tick flip is kept in the symmetry group throughout, so no
result here depends on an arrow.
