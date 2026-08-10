# Twenty small matrices carry every covariant table, and the 39 resolves into eight named rank drops — Cycle 765

Date: 2026-08-09

Authority: none

Audit: unset.

Status: derived reduction, complete census of the covariant band, and the residual named part by part

Claim type: bounded_theorem

Runner:

- [`physical_cell_cutting_small_matrix_census_cycle765_2026_08_09.py`](../scripts/physical_cell_cutting_small_matrix_census_cycle765_2026_08_09.py)

Axioms:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

Constitutional effect: none. This note changes no axiom, primitive, registry,
policy, audit verdict, effective status, or framework claim.

## What this responds to

Cycle 764 derived a ceiling of 144 on the rank of any table covariant under the
cell's own symmetry, a floor of 48 on its blind space, and showed the ceiling
attained by an exact rational witness. The cover table sits at rank 105 with
blind space 87, so 39 of the available rank goes unused. Cycle 764 could say
which twenty parts the room is distributed over, but not where the 39 goes, and
it ended by naming that as a finite and small question: which small matrices lose
rank, and by how much.

This cycle answers that question, and then measures the whole band the ceiling
bounds.

## The object

The unit four-cube on sixteen corners, cut into least-volume pieces at the
adjacency-cost floor: 2672 candidate pieces of determinant one, 400 of them at
cost floor 6, 15800 cuttings of 24 pieces, 192 pieces actually used and 192
eight-piece covers.

The symmetry permutes the four coordinates and flips any of them: 384 maps,
closed over all 147456 products, acting transitively on the 192 pieces and on the
192 covers. It has 104 orbits on ordered pairs of pieces, 120 on ordered pairs of
covers and 96 on the cells of the cover-by-piece square. By exact rational
arithmetic the cutting table has rank 88 with kernel 104, and the cover table has
rank 105 with kernel 87.

## The reduction

The twenty parts of cycle 764 are the eigenspaces of one central element acting
on the 192 piece directions. Each part carries a degree d, a piece-side
multiplicity m and a cover-side multiplicity mc. Written out, the piece side is a
sum over parts of a degree-d space times an m-dimensional multiplicity space, and
the cover side is the same sum with mc in place of m. A covariant table therefore
acts on each part as the identity on the degree-d space times a single mc by m
matrix. Its rank is the sum over parts of d times the rank of that small matrix,
and its blind space the sum of d times m minus that rank.

The runner builds those matrices rather than assuming them. Restricted to a part,
the commuting basis acts through m by m matrices; a deterministic small-integer
combination of them has a minimal polynomial of degree at most m, whose roots are
found by scanning every residue of the prime 1000003 with nested evaluation. A
root whose eigenspace has dimension exactly d picks out a one-dimensional line in
the multiplicity space, so every vector of that eigenspace is a pure tensor and
the multiplicity coordinates can be read off directly. All 20 of 20 parts pass
all five of the runner's conditions on this construction. Five of the twenty
matrices are empty, because those five parts have no cover-side copy at all.

The correspondence runs both ways. The 96 cell-orbit coefficients stack into a
matrix of width 96 whose rank is 96, so a covariant table is exactly one list of
twenty small matrices and every list is a covariant table. The reduction is
checked against the direct rank on 62 of 62 tables, and on the cover table itself
it returns rank 105 with blind space 87 — the same values the exact rational
computation gives.

## Where the 39 goes

Eight of the twenty small matrices fail to have full rank. Their rows, as degree,
piece-side multiplicity, cover-side multiplicity, rank of the small matrix, and
the rank the part gives up:

    2/2/2/1/2   4/2/3/1/4   6/2/3/1/6   8/4/6/3/8
    6/4/3/2/6   6/2/3/1/6   6/4/3/2/6   1/1/1/0/1

The last entry of each row is d times min(m, mc) minus d times the rank: the
rank that part forgoes against the ceiling's own per-part allowance. Those eight
numbers sum to exactly 39.

They are exactly cycle 764's eight excess parts, reached here by an independent
route. Cycle 764 identified them as the parts whose blind space exceeds what the
multiplicities force; this cycle identifies them as the parts whose small matrix
is rank-deficient, and the two lists agree. On all twenty parts the blind space
equals d times m minus the rank, so the cover table's blind space of 87 is now
accounted for part by part rather than in aggregate.

One entry deserves separate mention. The row 1/1/1/0/1 is a 1 by 1 matrix that is
simply zero — the class label cycle 764 showed to be blind, now visible as a
vanishing matrix entry rather than as a refuted candidate.

There are two parts whose small matrix is 1 by 1. One of them assigns plus to 48
of the 96 cell orbits and minus to the other 48, so a four-subset of cell orbits
is blind to it exactly when two of its signs are plus and two minus: 1272384 of
3321960, matching C(48,2) times C(48,2) in closed form. The other assigns plus to
all 96 and minus to 0, so no four-subset can cancel and 0 are blind to it.

## The band the ceiling bounds

With the reduction in hand, the rank of a covariant table is cheap, so the runner
censuses every four-subset of the 96 cell orbits — all 3321960 of them, not a
sample. There are 79 distinct ranks. The least is 24. The greatest is 144, the
ceiling itself, and 511872 four-subsets attain it.

Against that band the cover table is low, not typical. At or below its rank of
105 sit 106536 four-subsets: 24768 equal to 105 and 81768 strictly below, with 72
at the least. Far more four-subsets reach the ceiling than sit at or below 105.

Three points of the band are pinned exactly, by rational arithmetic with no
modulus: the four-subset 0/2/12/14 has rank 24, the four-subset 0/1/2/7 has rank
144, and the cover table's own 0/1/2/3 has rank 105, each agreeing with its
census value. The extremes of the band are therefore exact, and the greatest one
meets the derived ceiling.

As an independent rebuild, all twenty small matrices are constructed again from
scratch at the second prime 1000033, and reproduce the census rank on 200000 of
200000 sampled four-subsets.

## Runner

`physical_cell_cutting_small_matrix_census_cycle765_2026_08_09.py`, 41 gates,
`TOTAL: PASS=41 FAIL=0`. Every gate number is an exact integer computation and no
floating point enters any gate; the numbers are computational identities. The run
finishes well inside its budget of 900 seconds of wall time and 2500 MB of peak
resident memory, both checked by the run itself.

Controls carried inside the run: the stacked coefficient matrix having full rank
96, which is what makes the reduction a correspondence rather than a one-way map;
the reduction matched against the direct rank on 62 of 62 tables; the closed-form
count 1272384 matched against the brute count from the census; the whole
construction repeated from scratch at a second prime; exact rational ranks at
three named four-subsets; and the requirement that all 20 of 20 parts pass all
five construction conditions, so a non-generic choice fails its gate rather than
passing quietly.

## Boundary

Every census rank is computed modulo 1000003, and a modular rank can only fall
below the true rank, never rise above it. What follows from that, precisely:

- The greatest census rank, 144, meets the ceiling cycle 764 derived, so the
  maximum over the band is exactly 144 and nothing modular is being trusted for
  it.
- The least, 24, is confirmed by an exact rational rank at 0/2/12/14, so the
  minimum is exact as well.
- The counts at or below 105 — 106536, 24768, 81768 and 72 — are upper bounds,
  and the 511872 attaining the ceiling is a lower bound. Both bounds run in the
  direction that supports the reading above, but they are bounds.
- The 79 distinct ranks is neither an upper nor a lower bound on the number of
  distinct true ranks: modular reduction can merge two true values or separate
  two tables of equal true rank. It is a count of distinct modular values.

Two lines in the runner are bookkeeping rather than evidence, and are named as
such here. The part table is rebuilt at 1000003 and at 1000033 and matched
against cycle 764 row for row; the 1000003 rebuild uses the same prime cycle 764
used, so that half is bookkeeping and only the 1000033 rebuild is independent.
And the at-or-below line reporting 106536, 24768, 81768 and 72 partitions a
census that is checked elsewhere; its own conditions are weak, so it should be
read as a report of the census, not as a test of it.

The cover table's rank of 105 remains measured, not derived. The ceiling above it
and the floor below it are derived; the value in between is not, and this cycle
does not change that. What it changes is the shape of the residual: the 39 is no
longer a single unexplained number but eight named rank drops on eight named
parts, and the census says that a covariant table at or below 105 is uncommon
while one at the ceiling is not. Both sharpen the question rather than dissolving
it — we now know which eight small matrices lose rank and by how much, but not
why those eight, at those ranks.

The weights inside the construction are arbitrary deterministic choices carrying
no meaning. Their only role is to be generic, and each is gated by requiring the
eigenspace dimension to come out exactly d, so a choice that failed to be generic
would fail its gate rather than pass quietly.

The symmetry used throughout is the full symmetry of the four-cube, which is
larger than the proper cubic rotations the admissibility axiom names. A ceiling
derived from a larger group is still a ceiling, but the smaller group would give
a weaker one, so nothing here should be read as a statement about the axiom's own
covariance.

What remains is to say why the incidence relation of the cover-by-piece square
lands where it does. The census supplies a concrete handle the earlier cycles did
not have: the four-subset 0/1/2/7 reaches the ceiling of 144 while the cover
table's own 0/1/2/3 gives 105, sharing three of their four cell orbits and
differing in one. Naming the linear relations that the swap creates or destroys
is the next step opened by this cycle.
