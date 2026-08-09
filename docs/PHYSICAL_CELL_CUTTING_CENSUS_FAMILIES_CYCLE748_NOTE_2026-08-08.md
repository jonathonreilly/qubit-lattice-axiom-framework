# The smallest carriers of a charge, counted and sorted into families — Cycle 748

Date: 2026-08-08

Authority: none

Audit: unset.

Status: computational identities of the finite cutting system

Claim type: computational identities

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_census_families_cycle748_2026_08_08.py)

Scope: computational identities of the finite cutting system. Every number
below is machine-checked by the paired runner, which rebuilds the cell
complex, the cuttings, the readings and the block bookkeeping from scratch and
gates each quantity in place. Constitutional effect: none. This package
changes no axiom, no framework Admissibility rule, no primitive, no policy,
and no audit status, and it adds no import and no assumption to
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## Headline

An earlier cycle measured that the charge called four needs sixteen pieces to
carry it, and found eleven sixteen-piece carriers through one fixed anchor
piece. That was an anchored count: it said what passes through one piece, not
what the system contains. This cycle answers the whole-system question.

The symmetries of the incidence table close into a group of 384 which is
transitive on the 192 pieces and permutes the 192 eight-piece carriers of the
all-marked reading among themselves. Carrying the anchored eleven around by
that group produces 132 sixteen-piece carriers of four, each checked back
against the incidence directly, and every one of the 192 pieces sits on exactly
eleven of them. Eleven is the same count the anchored sweep returned, so every
piece stands to the 132 exactly as the anchor does, and the 132 are all of
them: the census is complete, not a sample.

The 132 are not one family. The group cuts them into six, of sizes 12, 12, 12,
24, 24 and 48. This is a real structural fact about the object and not a
bookkeeping artifact: the symmetries of the table do not carry every smallest
carrier of the charge onto every other one, even though they carry every piece
onto every other one. Transitivity on pieces does not descend to transitivity
on the smallest carriers.

The overlap ceiling of the previous cycle now holds for the system rather than
for the anchor. Across all 25344 pairs of a smallest carrier of four with an
eight-piece carrier of the all-marked reading, the overlap is 0 in 14592 cases,
1 in 4608 and 2 in 6144, never more; each of the 132 meets those carriers 128
times with multiplicity. The 6144 pairs at the cap give 6144 different
twenty-piece carriers of the flip partner of four, one per pair with no
collisions, every one of the 192 pieces on exactly 640 of them, falling into
twenty families of 192 and six of 384.

The same two measurements constrain the one size still undecided. Were an
eighteen-piece carrier of the flip partner to exist, it could share at most 4
pieces with any eight-piece carrier of the all-marked reading.

## The rebuilt system

The runner rebuilds the incidence table of the cutting system from scratch:
15800 distinct cuttings on 192 pieces, each cutting using 24 pieces, each piece
sitting in 1975 cuttings. A set of pieces carries a reading when the cuttings it
meets an odd number of times are exactly the ones the reading marks. The
all-marked reading marks all 15800; the charge called four marks 5664; the flip
partner of four marks the remaining 10136.

The all-marked reading needs exactly 8 pieces, and its eight-piece carriers are
exactly the 192 sets of eight pieces that no cutting uses twice, one for each
piece of the object. Each piece lies on 8 of them, and two of them share 0, 1, 2
or 4 pieces, never 3, with counts 15072, 1920, 960 and 384. These facts are
re-derived and re-gated here rather than carried over.

## Why the anchored eleven decide the system

Two measurements license the transfer. The symmetries of the table that fix a
basic reading number 48 and carry any piece to any other, which is what makes an
anchored sweep a whole-system statement. Adjoining the two extra symmetries the
table admits gives a group of 384, still transitive on the pieces, and every one
of its elements sends an eight-piece carrier of the all-marked reading to
another one, so the family of 192 is stable under it.

Because the group fixes the reading, it sends a carrier of four to a carrier of
four. The images of the anchored eleven are therefore carriers of four, and the
runner does not take that on trust: it recomputes the incidence sum of every
image directly and reports zero failures.

Completeness follows from the count rather than from a further search. Any
sixteen-piece carrier of four contains some piece; a group element carries that
piece to the anchor; the image is a sixteen-piece carrier of four through the
anchor, hence one of the eleven the anchored sweep found; so the original is in
the census. The arithmetic confirms it in place: every one of the 192 pieces
sits on exactly eleven members of the 132, the same eleven the anchored sweep
returned at the anchor.

## Six families, five profiles

Sorting the 132 by the group gives six families, of sizes 12, 12, 12, 24, 24
and 48. Sorting them instead by how they meet the 192 eight-piece carriers of
the all-marked reading gives only five profiles, of sizes 12, 12, 24, 36 and 48.

The profile is constant on a family, since the group permutes the eight-piece
carriers among themselves, so the profile is a coarsening of the family
structure. Five profiles from six families therefore means one profile is shared
by two families, and the sizes say which: the profile of size 36 covers a family
of 12 and a family of 24. The overlap pattern with the eight-piece carriers is a
genuine separator, but not a complete one.

## The ceiling at twenty, for the system

Adding an eight-piece carrier of the all-marked reading to a sixteen-piece
carrier of four gives a carrier of the flip partner of four, because a reading
and its flip partner differ by the all-marked reading. The size of the sum is 24
less twice the overlap, so the smallest sums come from the largest overlaps.

Every one of the 25344 pairs is measured here, not only those through the anchor. The
overlap takes the value 0 in 14592 pairs, 1 in 4608 and 2 in 6144, and never
exceeds 2. The cap of 2 is therefore a property of the whole system rather than
of the anchored eleven, and the smallest sum built this way has twenty pieces.

The 6144 pairs at the cap give 6144 distinct twenty-piece carriers: the map from
pair to sum is injective, with no two pairs landing on the same set. Every one of
them checks back against the incidence, every one of the 192 pieces sits on
exactly 640 of them, and the group sorts them into twenty families of 192 and
six of 384, which accounts for all 6144.

## What an eighteen-piece carrier would have to look like

The least size for the flip partner of four is bracketed between eighteen and
twenty by the previous cycle, with eighteen undecided. Suppose an eighteen-piece
carrier of the flip partner existed and met some eight-piece carrier of the
all-marked reading in k pieces. Their sum carries four and has 26 less twice k
pieces. For k at least 6 that is under sixteen, which no carrier of four
achieves. For k equal to 5 it is exactly sixteen, so the sum is a member of the
census, and it meets the eight-piece carrier in 8 less 5 pieces, which is 3 and
breaks the cap of 2. So k is at most 4.

This is a derivation from two measured inputs rather than a search: the least
size sixteen for four, and the whole-system cap of 2. The previous cycle stated
the same bound from the anchored cap; the input here is the system-wide one, so
the conclusion no longer inherits an anchored scope. It does not settle
eighteen — the totals it permits remain consistent with such a carrier existing
— but it is a shape constraint any construction or refutation at eighteen must
respect.

## Boundary and honest read

- Every statement here is about the finite cutting system. No physical reading
  of the readings, the carriers, the census or the families is claimed.
- The census of 132 is complete for the charge called four at size sixteen, and
  its completeness rests on two gated facts: the anchored sweep at sixteen is
  complete and returns eleven, and the group is transitive on the 192 pieces.
  Both are checked in place by this runner.
- The six families are the families of the group of 384 recorded in this
  runner, which is generated by the 48 together with the two extra symmetries
  the table admits. This note does not claim that group is the full symmetry
  group of the table; that question is handled by a separate in-flight package
  and is not assumed here.
- The cap of 2 and the resulting ceiling of twenty are exact for sums of a
  smallest carrier of four with an eight-piece carrier of the all-marked
  reading. This note does not claim that every twenty-piece carrier of the flip
  partner arises that way, and the 6144 counted here are the ones that do.
- The bound of 4 at eighteen is conditional on such a carrier existing. Nothing
  here asserts that one does, and nothing here asserts that none does. The
  bracket between eighteen and twenty is unchanged by this package.
- The families of the 132 and of the 6144 are counted, not classified. This note
  names no invariant that tells the two families sharing a profile of size 36
  apart, and finding one is open.
- Nothing here bounds the least size for the other charges or for their flip
  partners.
- The runner prints 36 gate lines, all passing, and every count above appears in
  that output.
- Earlier-cycle artifacts are named in backticks because their packages are in
  flight, and nothing here links to them:
  `PHYSICAL_CELL_CUTTING_SIXTEEN_ATTAINED_CYCLE742_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_HIDDEN_THREE_BIT_GEOMETRY_CYCLE743_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_FULL_SYMMETRY_CERTIFIED_CYCLE744_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_SIXTEEN_CENSUS_CYCLE745_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md`,
  `PHYSICAL_CELL_CUTTING_FLIP_PARTNER_CARRIER_BRACKET_CYCLE747_NOTE_2026-08-08.md`.
