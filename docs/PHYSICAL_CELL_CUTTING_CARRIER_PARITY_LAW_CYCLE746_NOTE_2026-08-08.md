# The parity law that decides which splits can carry a charge — Cycle 746

Date: 2026-08-08

Authority: none

Audit: unset.

Status: computational identities of the finite cutting system

Claim type: computational identities

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_carrier_parity_law_cycle746_2026_08_08.py)

Scope: computational identities of the finite cutting system. Every number
below is machine-checked by the paired runner, which rebuilds the cell
complex, the cuttings, the readings and the block bookkeeping from scratch and
gates each quantity in place. Constitutional effect: none. This package
changes no axiom, no framework Admissibility rule, no primitive, no policy,
and no audit status, and it adds no import and no assumption to
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## Headline

Carrying a charge is exactly three parity conditions. The 192 pieces of the
cut object sit in two halves and four quarters, and for each of the 18
readings the runner reads off the incidence which of those blocks the reading
fixes the parity of. The answer is the same five blocks for every reading: the
size, both halves, and quarters two and three. Quarters zero and one are never
fixed, and each half parity is the sum of the two quarter parities it covers,
so the five collapse to three. Those three sort the 18 readings into exactly
three classes, and all six charge readings land in the single class where the
three are even: every carrier of a charge has even size and meets quarters two
and three in an even number of pieces. Each class then has its own count of
licensed splits in closed form, and demanding a piece in the anchor quarter
costs exactly one size step.

## The rebuilt system

The runner rebuilds the incidence table of the cutting system from scratch:
15800 distinct cuttings on 192 pieces, each cutting using 24 pieces, each
piece used in exactly 1975 cuttings. The incidence has pivot rank 88 and
carries 18 readings, six of them charges. A set of pieces carries a reading
when, on every cutting, the parity of how many of its pieces that cutting uses
reproduces the reading.

## Which blocks a reading can fix

For a named block of pieces and a reading, either every carrier of that
reading meets the block in a fixed parity, or both parities occur. The runner
measures this for the size, both halves and all four quarters. Every block is
fixed by every reading or by none of them: the size, both halves and quarters
two and three are fixed by all 18, and quarters zero and one by none. The two
half parities are not independent of the quarters, since each half parity is
the sum of the parities it covers, so licensing a reading is exactly three
conditions on a split: the size, quarter two, and quarter three.

Two of those five determinations are then checked a second, independent way.

The first uses the piece sets no cutting can see. Row reduction over the field
with two elements on the 88 pivot cuttings yields 104 independent such sets,
built from the pivot rows alone and then each checked invisible directly
against the full incidence, so the check has to survive the 15800 cuttings and
not just the 88 it was built from. The ones the runner builds range in size
from 8 to 20 pieces. A block is left free exactly when one of those invisible
sets meets it in an odd number of pieces, and that happens for quarter zero
and quarter one and for no other block. So the free blocks are not read off
the bookkeeping twice; they are what invisibility forces.

The second recovers the size parity. The parity a reading fixes on the size is
the parity of how many cuttings the reading marks, which is what an odd number
of cuttings per piece already forces. That odd number is the measured 1975.

## The three classes

Sorting the 18 readings by the triple of fixed parities on the size, quarter
two and quarter three gives exactly three classes:

- even size, quarter two even, quarter three even: 15 readings, all six
  charges among them
- even size, quarter two odd, quarter three odd: 2 readings, no charges
- odd size, quarter two odd, quarter three odd: 1 reading, no charges

Exactly one class demands an odd size, and it holds no charge reading. Against
the search's own licensing test the three-parity rule agrees on all 191250
pairs of a split and a reading up to size twenty, with no disagreement.

## What each class costs the search

A split of a size across the four quarters is a unit of the anchored search's
budget. For a charge reading, at size two k the licensed splits number the sum
of the first k plus one squares, measured 5, 14, 30, 55, 91, 140, 204, 285,
385, 506 at sizes two through twenty; of those, the ones holding a piece in
the anchor quarter number the sum of the first k squares, measured 1, 5, 14,
30, 55, 91, 140, 204, 285, 385. Both agree with a direct enumeration that
never consults the incidence.

The anchored count at one size therefore equals the licensed count one size
below, so drawing every subset through the anchor costs exactly one size step
of the split budget. The splits a charge licenses that miss the anchor quarter
number k plus one, squared: 4, 9, 16, 25, 36, 49, 64, 81, 100, 121.

The class whose two fixed quarters are both odd licenses the sum of the first
k squares, one size step below a charge, measured 1, 5, 14, 30, 55, 91, 140,
204, 285, 385 at the same sizes; there every licensed split already holds a
piece in the anchor quarter, so anchoring is free. The reading that demands an
odd size licenses, at size two k plus one, twice the sum of the first k
triangular numbers, measured 0, 2, 8, 20, 40, 70, 112, 168, 240, 330 at sizes
one through nineteen. That reading licenses nothing at any even size, and no
charge licenses anything at any odd size.

## The counts belong to the parities

A closed form measured against the machinery that produced it can hold by
construction, so the runner also builds the count for each of the four parity
pairs on quarters two and three and asks which reproduces the charge count.
Only one does: 5, 14, 30, 55, 91, 140, 204, 285 for the even pair against 2,
8, 20, 40, 70, 112, 168, 240 for each mixed pair and 1, 5, 14, 30, 55, 91,
140, 204 for the odd pair. The test rejects a wrong parity instead of holding
whatever the parities are.

## Boundary and honest read

- Every statement here is about the finite cutting system. No physical reading
  of the parity classes or of the class counts is claimed.
- The parity law says which splits a carrier of a reading could occupy. It
  does not say a carrier of any given size exists; a licensed split can be
  empty of carriers, and at the sizes searched in earlier cycles many are.
  Licensing bounds the search's work, not the answer.
- The 104 invisible piece sets are one basis of the sets no cutting can see,
  chosen by the row reduction; the free-block conclusion does not depend on
  the choice, since a block met evenly by every member of a basis is met
  evenly by every combination.
- The sizes 8 to 20 quoted for those sets describe the basis the runner
  builds, not a bound on how small an invisible set can be.
- The class counts are measured through size twenty and stated as closed forms
  in the size; sizes beyond twenty are not measured here.
- Earlier-cycle artifacts are named in backticks because their packages are in
  flight, and nothing here links to them:
  `PHYSICAL_CELL_CUTTING_SIZE_TEN_FRONTIER_CYCLE738_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_SIXTEEN_ATTAINED_CYCLE742_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_HIDDEN_THREE_BIT_GEOMETRY_CYCLE743_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_FULL_SYMMETRY_CERTIFIED_CYCLE744_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_SIXTEEN_CENSUS_CYCLE745_NOTE_2026-08-05.md`.
