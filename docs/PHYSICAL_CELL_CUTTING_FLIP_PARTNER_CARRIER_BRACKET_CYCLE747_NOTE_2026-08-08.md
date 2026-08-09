# How few pieces can carry the flip partner of a charge — Cycle 747

Date: 2026-08-08

Authority: none

Audit: unset.

Status: computational identities of the finite cutting system

Claim type: computational identities

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_flip_partner_carrier_bracket_cycle747_2026_08_08.py)

Scope: computational identities of the finite cutting system. Every number
below is machine-checked by the paired runner, which rebuilds the cell
complex, the cuttings, the readings and the block bookkeeping from scratch and
gates each quantity in place. Constitutional effect: none. This package
changes no axiom, no framework Admissibility rule, no primitive, no policy,
and no audit status, and it adds no import and no assumption to
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## Headline

Each of the eight basic readings of the cut object has a flip partner: the
reading that marks exactly the cuttings it leaves unmarked. An earlier cycle
measured that the charge called four needs sixteen pieces to carry it. This
cycle asks the same question of the flip partner of four, and brackets the
answer between eighteen and twenty.

The ceiling comes from a small theorem the runner proves outright. The
all-marked reading, which marks every one of the 15800 cuttings, needs exactly
eight pieces, and its eight-piece carriers are exactly the 192 sets of eight
pieces that no cutting uses twice — one such set for every piece of the cut
object. Adding one of those to a sixteen-piece carrier of four gives a carrier
of the flip partner, and because the eleven anchored sixteen-piece carriers of
four never share more than two pieces with one of them, the smallest sum built
that way has twenty pieces. There are 512 distinct such sets and every one of
them checks back against the incidence.

The floor comes from search. Every search here is anchored, asking only for
carriers through one fixed piece, and that costs nothing: the runner checks that
the symmetries fixing a reading carry any piece to any other, so an empty
anchored sweep is an empty sweep for the whole system. The anchored search finds
no carrier of the flip partner at any even size from two up to sixteen, and at
sixteen it is asked of exactly the cells and splits that deliver the eleven
anchored sixteen-piece carriers of four, so the two sweeps are a matched pair at
the same size rather than a negative result standing on its own. At eighteen
the anchored search meets every anchored cell the flip partner licenses and
records no carrier, but 26 of its 4796 splits are refused
by the table guard, so eighteen is a measurement with a stated gap and not a
proof of emptiness. The least size is therefore at least eighteen and at most
twenty.

## The rebuilt system

The runner rebuilds the incidence table of the cutting system from scratch:
15800 distinct cuttings on 192 pieces, each cutting using 24 pieces, each
piece used in exactly 1975 cuttings. The two ways of counting the incidences
agree, 24 times 15800 against 1975 times 192. A set of pieces carries a
reading when, on every cutting, the parity of how many of its pieces that
cutting uses is exactly what the reading asks for. The eight basic readings
are the all-marked reading, the empty reading, the three charges four, six and
seven, and the flip partners of those three.

Each reading marks a definite number of cuttings, and since every piece meets
1975 cuttings, a carrier must have at least as many pieces as it takes for
1975 of them to cover the marks. The all-marked reading marks all 15800, which
forces at least eight pieces; four marks 5664, which forces at least three;
the flip partner of four marks the remaining 10136, which forces at least six.
Those two mark counts add to 15800, as flip partners must.

## The all-marked reading needs exactly eight pieces

The counting floor of eight is attained, and the runner shows more than that:
it identifies every eight-piece carrier. Eight pieces meet 1975 times eight,
which is 15800, cuttings counted with multiplicity, and there are exactly
15800 cuttings each of which must be met an odd number of times. So an
eight-piece carrier meets every cutting exactly once, which is the same thing
as saying no cutting uses two of its pieces.

Reading that condition off the incidence directly, the runner builds the
relation "no cutting uses both of these pieces" — each piece stands in that
relation to exactly 33 others — and enumerates every set of eight pieces that
are pairwise in it. There are 192 such sets, and all 192 do meet every cutting
exactly once, so the two descriptions agree exactly. Each piece lies in
exactly 8 of them. Two of them share 0, 1, 2 or 4 pieces and never 3: the
counts by shared size are 15072, 1920, 960 and 384, and those four counts run
over every pair of the 192, as the runner checks.

## Why a flip partner cannot be far from its reading

The eight basic readings close into an addition group of order 8 under
parity addition, and in that group each flip partner is its reading plus the
all-marked reading. Adding carriers adds readings, and the sum of two carriers
has at most the sum of their sizes, so the least size of a reading and the
least size of its flip partner differ by at most eight, which is the least
size of the all-marked reading. The subgroup reachable from four and the
all-marked reading is a four-element group, so this cycle's bracket speaks for
four and its flip partner and says nothing about six or seven.

## The ceiling at twenty

The eleven anchored sixteen-piece carriers of four are checked against all 192
eight-piece carriers of the all-marked reading. Every pair of one of the eleven
with one of the 192 shares 0, 1 or 2 pieces, with counts 1216, 384 and 512, and
each of the eleven meets the 192 in 128 pieces counted with multiplicity, which
is 8 times its own size, exactly as the fact that each piece lies in 8 of them
requires. Five distinct overlap profiles occur among the eleven.

Since the largest overlap is 2, the smallest sum of one of the eleven and an
eight-piece carrier of the all-marked reading has 16 plus 8 less twice 2, that
is 20, pieces. There are 512 distinct such sets, every one of
them has exactly 20 pieces, and every one of them recomputes to the flip
partner of four when checked back against the incidence. So the least size for
the flip partner is at most twenty.

This also rules the two shortest routes to eighteen out on their own terms. An
eighteen-piece sum built from one of the eleven would need an overlap of 3, and
the measured largest overlap is 2. A sum built from a ten-piece carrier of the
all-marked reading would need one to exist, and the search at ten finds none
anywhere in the system.

## Why one fixed piece is enough

Every sweep in this cycle is anchored: it asks only for carriers that contain
one fixed piece. That is a saving, not a restriction. The symmetries of the
incidence table that fix a reading carry any piece to any other, and the runner
checks that separately for each of the eight basic readings, finding in each
case that all 48 cube symmetries fix the reading. So if any set of pieces
anywhere in the system carried a reading at some size, a symmetry fixing
that reading would carry one of its pieces onto the anchor, giving a carrier of
the same reading at the same size through the anchor. An anchored sweep that
comes back empty at a size is therefore empty for the whole system at that
size, which is what the floor below rests on. Counts are a different matter and
this note reports them anchored, as measured.

## Nothing below eighteen

The anchored search sweeps the even sizes 2, 4, 6, 8, 10, 12, 14 and 16, asking
for carriers of four and of its flip partner. Odd sizes need no search: both
readings force an even total. The flip partner has no carrier at any even size
swept. Four has none below sixteen and eleven at sixteen.

Two things make that emptiness meaningful rather than blind. First, at sizes
8 and 10 the search also asks for the all-marked reading, and it returns
exactly the eight-piece carriers of it that pass through the anchor piece —
each of them one of the 192 already identified above, and there are 8 of them
because each piece lies in 8 — and nothing at ten. A search that finds what is
known to be there is a search whose silence carries information. Second, at
sixteen the two questions are asked in the same pass:
the same 204 licensed cells, the same 2004 splits. Four comes back with
eleven, the flip partner with none. The negative sits at the same size, over
the same work, as the positive.

Every carrier the search recorded — 19 of them across all sizes — is checked
back against the incidence directly rather than trusted from the bookkeeping
of the search, and none fails.

## Eighteen, measured with a stated gap

Eighteen is the size the bracket turns on, and it is reported here exactly as
it measured.

The flip partner forces an even total size, so eighteen is the only even size
between the emptiness at sixteen and the carriers at twenty. The anchored
search at eighteen meets all 285 anchored cells the flip partner licenses
there, an independent recount of them agreeing with what the sweep met, and
processes 4796 splits. It records no carrier.

But 4770 of those splits were searched and 26 were refused. Each refusal is a
join whose intermediate table would need more rows than the guard allows: the
guard sits at 30 million rows, and the refused joins asked for between 31 and
21766 million, the largest more than 700 times the guard. The refusals sit in
11 of the 285 cells. That residue is 26 splits out of 4796, and it is not
reachable by relaxing the guard — the largest refused join is far beyond what
the machine can hold.

So the eighteen result is that a complete pass over every licensed cell, with
26 of its 4796 splits refused, found nothing. That is evidence, carefully
bounded, and it is not an emptiness certificate. The least size that can carry
the flip partner of four is at least eighteen and at most twenty.

## Boundary and honest read

- Every statement here is about the finite cutting system. No physical reading
  of the readings, the carriers or the bracket is claimed.
- The bracket is {18, 20}, not a single value. The eighteen sweep found
  nothing but did not search 26 of its 4796 splits, so this note does not
  assert that eighteen is empty.
- The searches at every size are anchored, and this note checks in place that
  the symmetries fixing a reading carry any piece to any other, so an empty
  anchored sweep at a size is empty for the whole system at that size. The
  bracket is a whole-system statement, not an anchored-only one.
- The eight-piece characterization of the all-marked reading's carriers is
  complete and is a theorem, not a search result: the counting floor and the
  converse both hold outright, and the enumeration of the 192 covers every set
  of eight pieces that the relation admits, with none left out.
- The ceiling of twenty is exact for sums of one of the eleven anchored
  sixteen-piece carriers of four with an eight-piece carrier of the all-marked
  reading, and the overlap cap of two is measured on those eleven. It does not
  claim that every twenty-piece carrier of the flip partner arises that way.
- The reachable subgroup from four and the all-marked reading has four
  elements, so nothing here bounds the least size for six, for seven, or for
  either of their flip partners.
- Counting arguments were tried against eighteen and did not settle it. A
  carrier of the flip partner can meet an eight-piece carrier of the all-marked
  reading in at most four pieces, but the resulting total over the 192 of them
  is consistent with a carrier of eighteen pieces existing, so that bound does
  not decide the question; and the 192 sets do not form a balanced pair design,
  so the second-moment step is unavailable. Only the search speaks to eighteen,
  and its residue is stated above.
- Earlier-cycle artifacts are named in backticks because their packages are in
  flight, and nothing here links to them:
  `PHYSICAL_CELL_CUTTING_SIXTEEN_ATTAINED_CYCLE742_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_HIDDEN_THREE_BIT_GEOMETRY_CYCLE743_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_FULL_SYMMETRY_CERTIFIED_CYCLE744_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_SIXTEEN_CENSUS_CYCLE745_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md`.
