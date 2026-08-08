# Twelve pieces: the six charges need at least fourteen — Cycle 739

Date: 2026-08-05

Cycle: 739

Authority: none

Audit: unset.

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`physical_cell_cutting_twelve_frontier_cycle739_2026_08_05.py`](../scripts/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05.py)

Standing framework: [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

Constitutional effect: none. This package changes no axiom, primitive,
registry, policy, queue, audit result, or audit status. It records one finite
measurement.

## Result

The object is the unit four-cube on its 16 corners, cut into pieces at the floor
of the adjacency cost. There are 15800 such cuttings, each using 24 pieces, drawn
from 192 pieces in all. A set of pieces carries a reading when, on every one of
the 15800 cuttings, the parity of how many of its pieces that cutting uses
reproduces the reading.

A complete search of every set of exactly twelve pieces, against eighteen
readings at once, gives the counts

```
7808,3072,0,0,0,0,0,0,661,25,38,38,1,1,1,2,1,0
```

in the order: the constant zero reading, the constant one reading, the two sides
of each of the three charges, the four controls of the previous cycle, the five
planted twelve-piece controls, and one synthetic reading whose forced total
parity is odd.

The six charge entries are all 0. The complete searches at every set of at most
eight pieces, at exactly ten, and now at exactly twelve are all empty for those
six, and each of the six forces an even total parity, which bars every odd size.
So no set of twelve or fewer pieces carries any of them, and the floor for all
six moves from twelve to fourteen.

The bound is not vacuous. Measured apart from the search, every one of the
readings except the synthetic one lies in the column space of the incidence
table, so each of the six charges is carried by some piece set; what this cycle
measures is that no such set has twelve or fewer pieces. The synthetic reading
lies outside the column space, which is why it is empty at every size.

## The certificate tree

Every one of the 192 pieces is used by exactly 1975 of the cuttings, an odd
count; the incidence table has rank 88 and kernel dimension 104; the 15800
cuttings are pairwise distinct as piece sets.

The 192 columns in their canonical ordering split into four quarters of 48 and
eight blocks of 24. The internal dimension of a block is the dimension of the
space of parity functionals supported entirely inside it; the column rank is the
rank of that block's columns as vectors on the pivot cuttings.

| block family | internal dimension | column rank |
| --- | --- | --- |
| the eight blocks of 24 | 0,0,0,0,0,0,1,2 | 19,24,24,24,24,24,24,24 |
| the four quarters of 48 | 0,0,6,13 | 34,48,48,48 |
| first half, second half | 13, 33 | 55, 75 |
| the four mixed quarter pairs | 9,13,15,22 | — |
| the complements of the quarters | 54,40,40,40 | — |

For all 22 of those blocks and unions the internal dimension plus the rank of the
complementary columns is 88, so the two sides of the table determine each other.

The left and right halves are strongly asymmetric: the first half carries
internal dimension 13 against 33 for the second, and the first quarter is the one
degenerate block, its 48 columns having rank only 34. That rank drop is exactly a
subcode: the piece sets inside the first quarter met evenly by every cutting form
a space of dimension 14 = (48 - 34). All 16384 of its words were verified to have
zero syndrome, with weight distribution

```
{0:1,8:30,12:63,14:164,16:395,18:929,20:1846,22:3017,24:3456,26:2962,28:1891,30:974,32:470,34:141,36:40,38:5}
```

Its least nonzero weight is 8, with 30 words there and 63 at weight 12. Inside
the first block of 24 the same construction gives dimension 5 and 32 words, with
distribution `{0:1,8:9,12:12,16:9,24:1}`; every one of those 32 words also lies in
the first quarter's subcode, as the column containment requires.

Of the 15 block indicators, exactly 5 lie in the row space — the whole set, its
two halves, and the two quarters of the second half — so those blocks carry a
forced parity on every reading. The other 10 are free. Each of the two forced
quarters forces, on the first twelve readings, the parity vector

```
0,0,0,0,0,0,0,0,1,1,0,0
```

while the whole set and both halves force even parity on all twelve; the
synthetic reading forces an odd whole.

## Method

A cell is the profile of how many of a candidate set's pieces come from each of
the four quarters. The forced parities license only some cells: for a reading
with all-even forced parities the licensed cells at sizes two, four, six, eight,
ten and twelve number

```
5,14,30,55,91,140
```

whose consecutive differences are the squares 9,16,25,36,49. At twelve the
licensed-cell count per reading, in the order above, is

```
140,140,140,140,140,140,140,140,91,91,140,140,91,91,91,140,140,0
```

Each licensed cell is planned into A and B parts. When no quarter takes more than
6 pieces the cell has a single split: A is the quarter holding the largest part
and B is the other three. When one quarter takes more, that quarter is split into
its two blocks of 24 and the cell yields one split for each way of dividing its
pieces between them — the eighth split — with A the heavier of the two blocks.

Within a split, the B part tables and their sorted join keys are built once and
reused for every reading still live on that cell. At the closing B join the keys
are the parities the A side can no longer change — the internal space of the
complement of A, of dimension 54,40,40,40 for the four quarters — so a B
combination survives only when those parities already agree with the reading;
earlier joins key on the internal space of the columns joined so far. The folded
roots of all live readings are then matched exactly against the A table, streamed
in chunks. No intermediate or final table reached the cap of
30000000 entries.

Three sweeps were run: every set of at most eight pieces, every set of exactly
ten, and every set of exactly twelve. At twelve, every licensed cell was met
exactly once per reading and the 1167 splits were all distinct.

## Verification

The runner carries 38 gates and reports `TOTAL: PASS=38 FAIL=0`.

- Known answer, at most eight pieces: 648 sets carry the constant zero reading,
  in 22 orbits of the cell symmetries — 17 of size 24 and 5 of size 48 — and 192
  carry the constant one reading, in 5 orbits, 2 of size 24 and 3 of size 48. The
  six charges and the synthetic odd reading are empty there. All 845 recorded
  sets recompute to their own reading.
- Known answer at ten: the first twelve readings give 0,0,0,0,0,0,0,0,108,1,2,0,
  reproducing the previous cycle exactly; 111 recorded sets verified; the
  synthetic odd reading licenses no cell at ten.
- Recorded sets at twelve: all 11648 of them recompute to their own reading, have
  weight 12, and are pairwise distinct.
- Planted recovery: five twelve-piece sets were drawn from fixed quarter
  profiles and their readings handed to the search blind, two of them with
  profiles that force the eighth split. All five were recovered, at counts
  1,1,1,2,1.
- Orbit structure at twelve: the zero-reading sets fall into 174 orbits,
  `{8:2,16:1,24:18,48:153}`, and the one-reading sets into 70 orbits,
  `{8:2,16:2,24:6,48:60}`, under the symmetries that fix the reading. Every other
  nonempty reading has a trivial stabilizer, so each of its sets is its own
  orbit.
- Subcode cross-validation, apart from the search: all 30 weight-8 words of the
  first quarter's subcode are among the 648 found at eight or fewer, and all 63
  weight-12 words are among the 7808 found at twelve.
- Column-space membership, by an elimination that never consults the search: the
  192 columns span a space of dimension 88, the first 17 readings lie in it, and
  the synthetic one does not — `1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0`. Since the
  search compares a candidate's syndrome on the 88 pivot cuttings, and those 88
  rows separate the readings the table can carry, agreement there is agreement on
  all 15800 cuttings for every reading the object admits.
- Budgets: under 90 s elapsed against a 900 second ceiling, peak memory under
  1600 MB, output under 5500 characters.

## Boundary / honest read

One engine produced the twelve sweep. The planted recovery — five sets drawn
blind to the search, covering both the quarter-split and the eighth-split code
paths — and the independent subcode enumeration, which reproduces all 30 weight-8
and all 63 weight-12 words without consulting the search at all, narrow that
single-engine dependence but do not remove it. An independent re-implementation
at twelve is not part of this package.

The block profile is relative to the fixed canonical ordering of the 192 columns.
Which blocks are forced, the internal dimensions 0,0,0,0,0,0,1,2 and 0,0,6,13,
and the rank drop at the first quarter are measured, not derived: a different
ordering of the same 192 pieces would relabel the table, and nothing here shows
that the ordering is forced.

The floor statement is a lower bound and nothing more. Sizes above twelve were
not searched, so this says the six charges need at least fourteen pieces, not
that fourteen suffices.

The four controls of the previous cycle are nonempty at twelve, at 661, 25, 38
and 38, and the constant readings at 7808 and 3072. Those counts are what a
search able to find things looks like on this object; they are recorded here, not
otherwise interpreted.

## Claim type

Claim type: bounded_theorem

## Audit

Audit: unset.
