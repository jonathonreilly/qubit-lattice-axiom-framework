# The forced piece sets form a space, and the block lattice it cuts out — Cycle 740

Date: 2026-08-05

Cycle: 740

Authority: none

Audit: unset.

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [forced-certificate subspace, quarter and block lattices, witnesses, planted controls](../scripts/physical_cell_cutting_forced_certificate_cycle740_2026_08_05.py)

Standing framework: [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

Constitutional effect: none. This package changes no axiom, framework
Admissibility rule, primitive, registry, policy, audit result, or audit status.
It measures finite structure on an object the previous cycles already built, and
nothing in it is promoted above its own scope.

## Result

The object is the incidence table of the least-cost cuttings of the unit
four-cube into pieces of least volume: 15800 cuttings, 24 pieces to a cutting,
192 pieces in all, over the field with two elements. Row rank 88, kernel
dimension 104, all 15800 rows pairwise distinct. A piece set is *forced* when its
indicator lies in the row space, so that the parity of any carrier's meet with it
is fixed by the readings and cannot be moved. The previous cycle tested the 15
single-block indicators of the fixed canonical piece order and found exactly
`whole`, `L`, `R`, `Q2`, `Q3` forced. This cycle asks what that answer is a
shadow of.

**The forced sets are a space, and this is what the previous cycle's five
answers encode.** Restricted to the 256 unions of the eight blocks of 24, the
forced family contains the empty set and is closed under symmetric difference,
and it has exactly 8 members. The planted-forced control carries the same
statement off the block lattice: a piece set built by folding 30 cuttings
together is forced, and so is its symmetric difference with the first half.

**The quarter-parity image is exactly the two words `0000` and `1100`,
dimension 1.** Sending a kernel word to its four quarter meet parities lands in
the annihilator of the forced quarters, because no kernel word can meet a forced
set oddly; and the generator `1100` is present because kernel words do meet the
first quarter oddly. Both directions are checked, not assumed.

**Of the 16 unions of quarters, exactly 8 are forced**, namely the empty set,
`Q3`, `Q2`, `R`, `L`, the complement of `Q2`, the complement of `Q3`, and the
whole set. The two complements are tested here for the first time; they are
forced, as the annihilator of the quarter image says they must be. Every one of
the 16 is settled twice, once by direct membership in the row space and once by
the annihilator, and the two answers agree union by union.

**The block-parity image has measured dimension 5, with 32 words**, spanned by
`00000011`, `00001100`, `00110000`, `01100000`, `11000000`. That is the largest
dimension the previous cycle's answer allows: the image must annihilate the block
words of the 5 sets that cycle found forced, which bounds its dimension by 5, and
the measurement attains that bound. Equivalently, and checked word by word, every
kernel word pairs the two blocks inside each quarter of the second half and keeps
the first half even overall. Accordingly **exactly 8 of the 256 block unions are
forced**, two to the 8 less 5, and the direct-membership sweep agrees with the
annihilator on all 256.

**Every forced block union is a union of quarters.** No block of 24 pieces is
forced alone, and the two quarters of the first half are forced only together.
Read back on the 15 indicators the previous cycle tested, the sweep returns the
previous cycle's answer exactly: forced `L`, `Q2`, `Q3`, `R`, `whole`; free
`E0` through `E7`, `Q0`, `Q1`.

**The whole set is the symmetric difference of all 15800 cuttings.** Every piece
is used by exactly 1975 cuttings, an odd count, so folding every cutting together
fills all 24 packed bytes and leaves all 192 column counts odd. The same set is
also carried a second way, by an explicit combination of 48 pivot cuttings
verified piece by piece.

Explicit cutting combinations, each verified by folding the named cuttings and
comparing on all 192 piece coordinates: the first half `L` from 46 pivot
cuttings, the third quarter `Q2` from 26, the complement of `Q2` from 50, the
complement of `Q3` from 46.

## The witnesses

For each free block a kernel word with an odd meet, with zero syndrome on all
15800 cuttings checked in full, not on pivots:

| free block | witness weight |
| --- | --- |
| `E0` | 8 |
| `E1` | 8 |
| `E2` | 8 |
| `E3` | 8 |
| `E4` | 8 |
| `E5` | 8 |
| `E6` | 8 |
| `E7` | 8 |
| `Q0` | 8 |
| `Q1` | 8 |

The reduced kernel basis has least weight 8 and greatest weight 20, and no
symmetric difference of two basis words comes in below 8 either, so 8 is the
floor this search reaches from every direction it can afford. The block-parity
words of the first two witnesses are `10011100` and `01011100`; every witness
parity word lies in the measured block image and is odd on the block it was found
for, the two free quarters included.

## Method

Two eliminations over the field with two elements, run on the same table from
opposite sides and never compared against each other's internals:

- *Over the cuttings.* Each cutting is a 192-bit word; the elimination keeps, for
  every pivot, the set of cuttings whose symmetric difference produced it. That
  bookkeeping is what turns a membership answer into an explicit list of
  cuttings. Row rank 88.
- *Over the pieces.* Each piece is a 15800-bit word; the elimination returns 104
  independent kernel words, and each is checked against all 15800 cuttings by an
  integer product before anything is asked of it. Column rank 88.

Membership of a piece set is decided by reducing its indicator against the first
elimination: success returns a combination of pivot cuttings, failure returns
nothing. The annihilator route never touches that elimination: it maps the 104
kernel words to their quarter or block meet parities, takes the span, and
declares a union forced when the union's parity word is orthogonal to the whole
span. The gates are the agreements — all 16 quarter unions, all 256 block
unions — not either route alone.

Every forced answer carries a combination that is folded and compared on all 192
piece coordinates. Every free answer carries a named kernel word that meets the
set oddly. The witnesses are reduced by adding kernel words of even meet while
the weight drops.

The controls are seeded at 74000 and drawn with the same generator every run. The
planted-forced control folds 30 cuttings into a piece set of weight 96 and hands
the runner nothing else; the runner recovers it blind as forced from a
combination of 44 pivot cuttings, which is not the planting set. Its symmetric
difference with the first half, a set that is no block union, is forced too, by
44 pivot cuttings verified the same way. The planted-free control draws 20 pieces
and finds a weight-8 kernel word meeting them oddly, after 0 redraws.

## Verification

29 gates, `TOTAL: PASS=29 FAIL=0`, every number below printed by the runner.

- G01 the table is 15800 by 192 with 24 pieces to a cutting, in the exact-cover
  search and in the table alike.
- G02 every one of the 192 pieces is used by exactly 1975 cuttings, an odd count.
- G03 the elimination over the cuttings and the independent elimination over the
  pieces return the same rank 88, leaving a kernel of dimension 104.
- G04 the 15800 cuttings are pairwise distinct as piece sets.
- G05 all 104 kernel words meet every one of the 15800 cuttings evenly and are
  independent.
- G06 the 48 symmetries permute cuttings and pieces leaving the table fixed,
  which is what fixes the canonical piece order the blocks are cut from.
- G07 the symmetric difference of all 15800 cuttings is the whole piece set: all
  24 packed bytes come out full and all 192 column counts come out odd.
- G08 the whole set is carried a second way, by an explicit combination of 48
  pivot cuttings checked on all 192 piece coordinates.
- G09 no kernel word meets the whole set, either half or either quarter of the
  second half oddly — the previous cycle's forcing pattern seen from the kernel.
- G10 the quarter-parity image is exactly `0000` and `1100`: inside the
  annihilator of the forced quarters, and with its generator present.
- G11 of the 16 quarter unions exactly the 8 annihilating the image are forced,
  the two quarter complements among them, and direct membership agrees with the
  annihilator one for one.
- G12 each of the 16 quarter unions carries its own certificate.
- G13 the block-parity image annihilates the block words of the 5 sets the
  previous cycle found forced, which bounds its dimension by 5; the measurement
  attains that bound at 5 with 32 words.
- G14 on all 256 block unions the two routes return the same answer.
- G15 exactly 8 of the 256 block unions are forced, two to the 8 less 5.
- G16 each of the 256 block unions carries its own certificate.
- G17 read back on the 15 block indicators the sweep returns the previous cycle's
  answer.
- G18 the forced block unions contain the empty set and are closed under
  symmetric difference, a space of 8 sets.
- G19 every forced block union is a union of quarters: no block of 24 pieces is
  forced alone, and the two quarters of the first half are forced only together.
- G20 the first half and the third quarter are the symmetric differences of 46
  and 26 pivot cuttings, each checked on all 192 piece coordinates.
- G21 the two quarter complements are the symmetric differences of 50 and 46
  pivot cuttings, checked the same way.
- G22 each of the 10 free blocks has a kernel witness with zero syndrome on all
  15800 cuttings and an odd meet with its own block.
- G23 the reduction reaches weight 8 for every free block, which is also the
  least weight in the reduced basis and the least weight any pair of basis words
  reaches.
- G24 every witness parity word lies in the measured block image and is odd on
  the block it was found for.
- G25 the planted forced set is recovered blind, by a combination of 44 pivot
  cuttings that is not the 30 cuttings planted, checked piece by piece.
- G26 its symmetric difference with the first half, a set that is no block union,
  is forced too, by 44 pivot cuttings checked the same way.
- G27 the planted 20-piece set is not forced: a weight-8 kernel word with zero
  syndrome meets it oddly, after 0 redraws.
- G28 the runner finishes under 900 seconds; it runs under 10 s at under 200 MB.
- G29 the output stays under 5500 characters.

## Boundary and honest read

The eight blocks of 24 and the four quarters of 48 are cut from the fixed
canonical piece order that the exact-cover search and the 48 symmetries produce.
That partition is measured, not derived: a different canonical order would cut
different blocks out of the same 192 pieces, and the block lattice reported here
is a statement about this order. The quarter-level statement is the more robust
one, since the quarters are the coarser cut; the eight-block statement inherits
whatever the ordering supplies.

The combination sizes — 48 for the whole set, 46 for `L`, 26 for `Q2`, 50 and 46
for the two complements, 44 in the planted control — are measured, not derived.
They are the sizes the pivot choice of this elimination happens to give. They are
certificates of forcedness, verified coordinate by coordinate; they are not
minimal representations and no minimality is claimed.

The membership sweep runs on a single elimination engine. What narrows it is that
the annihilator route is built from the other elimination, so the agreement on
all 16 quarter unions and all 256 block unions is a check between two engines
rather than a restatement of one; and that both planted controls are answered
blind, one positive and one negative. Both engines still read the same incidence
table, so a fault in the table itself would not be caught by their agreement, nor
by the certificate gates, which re-verify against whatever table they are handed.
It is caught earlier instead: a single flipped incidence bit takes down the piece
count per cutting, the column counts, the rank agreement between the two
eliminations, the symmetry fixation and the whole-set identity.

Witness weight 8 is what a reduction over the reduced kernel basis reaches,
supported by a complete scan of the pairs of basis words. It is not a proof that
no kernel word of lower weight meets a given free block oddly; minimum weight
over the full kernel is not searched here and is not claimed.

The subspace *shape* is derived given the previous cycle's measured forcing
pattern. That whole, both halves and the two quarters of the second half are
forced is the input; that the quarter image is then forced into the annihilator
`{0000, 1100}`, that the forced quarter unions are exactly the 8 annihilating it,
and that no forced union can separate `Q0` from `Q1`, is the consequence, and the
runner checks each step rather than assuming it. The measured value of the
block-image dimension, 5, was not predicted in advance beyond the bound of 5 that
the quarter constraints supply; it is reported as measured, and the note is
written from the measurement.

Nothing here supplies a physical reading, a dynamics, a metric, or a selection
among cuttings. It says which piece sets have a parity no reading can move, on
this finite object, in this canonical order.

## Claim type

`Claim type: bounded_theorem`. The claims are finite, integer and
field-with-two-elements statements about an explicitly constructed 15800 by 192
table, each one carrying a certificate that is checked in the runner. The
conditionality is stated above: the shape is derived from the previous cycle's
measured forcing pattern, and the block partition is relative to the fixed
canonical order.

## Audit

`Audit: unset.` This note sets no audit verdict and predicts none. The
independent audit lane is the sole authority on audit language for this package.
