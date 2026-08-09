# A smallest carrier of a charge carries its own family label — Cycle 749

Date: 2026-08-08

Authority: none

Audit: unset.

Status: computational identities of the finite cutting system

Claim type: computational identities

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_family_separator_cycle749_2026_08_08.py)

Scope: computational identities of the finite cutting system. Every number
below is machine-checked by the paired runner, which rebuilds the cell
complex, the cuttings, the readings and the block bookkeeping from scratch and
gates each quantity in place. Constitutional effect: none. This package
changes no axiom, no framework Admissibility rule, no primitive, no policy,
and no audit status, and it adds no import and no assumption to
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## Headline

The unit four-cube cuts into least-volume pieces at the adjacency cost floor
in 15800 ways, and those cuttings use 192 pieces between them, 24 to a cutting
and 1975 cuttings through each piece. The charge called four needs sixteen
pieces to carry it, and the system holds exactly 132 such carriers, every
piece on eleven of them. The symmetries of the incidence table close into a
group of 384 which does not carry every one of the 132 onto every other: they
fall into six families, of sizes 12, 12, 12, 24, 24 and 48.

A family is a fact about a carrier's place in the system — which other
carriers the symmetries take it to. The question this cycle asks is whether
the family is also a fact about the sixteen pieces themselves, readable
without looking at the rest of the system. It is.

Take a smallest carrier of four and throw away everything except the
incidence table restricted to its sixteen pieces. For each pair of its pieces,
count the cuttings that use both. The list of those counts, sorted, is
different for every one of the six families. No two families share it. So a
smallest carrier of four already carries its family label in itself, and the
group is not needed to read it off.

## Four readings that do not separate, and one that does

The separating list did not arrive alone. Four coarser readings of the same
sixteen pieces were measured beside it, and the five nest: each tells apart
everything the one before it does, and more. The runner checks the nesting
directly, group by group, and prints what each reading holds together.

| reading of the sixteen pieces | groups | families held together |
| --- | --- | --- |
| how often it meets the marked cuttings | 1 | 12+12+12+24+24+48 |
| pairs of its pieces no cutting shares | 2 | 12+12+12+24 \| 24+48 |
| the total of its pair counts | 4 | 12 \| 12 \| 12+24 \| 24+48 |
| its meetings with the eight-piece carriers | 5 | 12 \| 12 \| 12+24 \| 24 \| 48 |
| the whole list of its pair counts | 6 | 12 \| 12 \| 12 \| 24 \| 24 \| 48 |

The fourth row is the reading an earlier cycle used. That cycle recorded that
it leaves two families sharing one value, so it does not tell them apart, and
that "finding one is open" — an invariant that does. The fifth row is one. The
first four rows are what makes the fifth a result rather than a definition:
the same construction applied four other ways lands short, at one, two, four
and five groups, so arriving at six is measured and not arranged. The gate
pins the whole sequence 1, 2, 4, 5, 6 and requires the last reading to give
one group per family while each of the other four holds at least two families
together.

Two of these readings are the same quantity wearing different clothes. Summing
the pair counts over pairs of pieces is summing the squares of the numbers of
pieces each cutting contributes, with a fixed diagonal removed, so the third
row is the spread of the second row's meeting numbers. They land in different
places because the spread keeps information the count of never-sharing pairs
throws away.

## Two laws the same computation returns

**The marked cuttings are met identically by all of them.** Four marks 5664 of
the 15800 cuttings. Every one of the 132 smallest carriers meets 2832 of those
marked cuttings once and the other 2832 three times, and meets none of them
twice or more than three times. That is not merely a coarse reading; it is a
constant one. Half of 5664 is 2832, so the two halves account for the marked
cuttings exactly.

**Each carrier comes with a pairing of its own sixteen pieces.** Within a
smallest carrier of four, the largest pair count is reached on exactly 8 pairs,
and those 8 pairs cover all 16 pieces — a pairing of the set, read off the
restricted table with nothing else in hand. The largest value is 433 on 60 of
the carriers and 666 on the other 72, and 60 and 72 make 132. This is not
automatic for sixteen pieces: taking sixteen pieces evenly spaced through the
table's own ordering, in four different spacings, gives 768 sets of which just
1 has the property, against 132 of 132 for the carriers.

**Overlaps between two smallest carriers take five values.** Two of the 132
share 0, 1, 2, 4 or 8 pieces and never 3, 5, 6 or 7, with counts 4926, 960,
1440, 960 and 360. The missing values mirror the same gap the eight-piece
carriers of the all-marked reading show, where overlaps of 3 are likewise
absent.

## Boundary and honest read

- Every statement here is about the finite cutting system. No physical reading
  of the readings, the carriers, the families or the pairings is claimed.
- The six families are the families of the group of 384 recorded in this
  runner, generated by the 48 together with the two extra symmetries the table
  admits. This note does not claim that group is the full symmetry group of the
  table; that question is handled by a separate in-flight package and is not
  assumed here.
- The separating reading is measured to separate, not proved to. The runner
  checks that no two of the six families share a sorted list of pair counts;
  it derives no reason why they cannot, and gives no closed-form description of
  which list belongs to which family.
- The five readings are five that were tried, ordered by how much they
  separate, and the nesting between them is checked. Nothing here says they are
  the natural five, and a sixth reading finer than the last is not ruled out.
- The pairing is exhibited, not explained. This note does not say what the two
  largest values 433 and 666 count, nor why exactly two of them occur, nor what
  distinguishes the 60 carriers from the 72.
- The control on the pairing is a control, not a proof of rarity: 1 of 768 is
  what four spacings through the table's ordering give, and a different family
  of sixteen-piece sets could give a different rate.
- Nothing here bounds the least size for the other charges or for their flip
  partners, and nothing here settles whether an eighteen-piece carrier of the
  flip partner of four exists. That bracket is unchanged by this package.
- The runner prints 37 gate lines, all passing, and every count above appears
  in that output.
- Earlier-cycle artifacts are named in backticks because their packages are in
  flight, and nothing here links to them:
  `PHYSICAL_CELL_CUTTING_SIXTEEN_ATTAINED_CYCLE742_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_HIDDEN_THREE_BIT_GEOMETRY_CYCLE743_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_FULL_SYMMETRY_CERTIFIED_CYCLE744_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_SIXTEEN_CENSUS_CYCLE745_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md`,
  `PHYSICAL_CELL_CUTTING_FLIP_PARTNER_CARRIER_BRACKET_CYCLE747_NOTE_2026-08-08.md`,
  `PHYSICAL_CELL_CUTTING_CENSUS_FAMILIES_CYCLE748_NOTE_2026-08-08.md`.
