# Forced subsets in a declared finite cutting-incidence table — Cycle 740

Date: 2026-08-05

Cycle: 740

Authority: none

Audit: unset.

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [primary forced-subset, quarter/block, certificate, and hostile-check runner](../scripts/physical_cell_cutting_forced_certificate_cycle740_2026_08_05.py)
- [independent opposite-pivot and least-pivot GF(2) reconstruction](../scripts/physical_cell_cutting_forced_certificate_cycle740_independent_check_2026_08_05.py)

Direct finite-data dependency:
[Cycle 737](PHYSICAL_CELL_CUTTING_LEAST_COMPUTING_SETS_CYCLE737_NOTE_2026-08-05.md)
binds the same supplied 15,800-row population and ordered 192-piece support universe.
The present runners reconstruct those bytes and compare row-order-invariant hashes.

Framework boundary:
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) does **not**
supply this cell model, its simplices, its cost, its ordering, or its finite readings.

Constitutional effect: none. This package changes no axiom, framework
Admissibility rule, primitive, registry, policy, audit result, or audit status.
It measures finite structure on a supplied finite object, and
nothing in it claims authority beyond its own scope.

## Result

The supplied object is the incidence table of the declared least-cost
normalized-volume-one corner-simplex dissections of one unit four-cube:
15,800 rows, 24 pieces per row, and 192 used pieces over GF(2). Every
co-occurring pair has an exact integer separating plane, so the sample-cover
enumeration is checked as a geometric dissection census rather than merely
called one. The table has row rank 88 and kernel dimension 104; all 15,800 rows
are pairwise distinct.

A subset indicator \(s\) is called *forced* here exactly when
\(s\in\operatorname{row}(I)=\ker(I)^\perp\). Equivalently, if two piece supports
\(x,x'\) produce the same fixed finite reading, then
\(I(x+x')=0\) and \(\langle s,x\rangle=\langle s,x'\rangle\). Thus “forced”
means invariant among supports of one fixed finite reading. It does not mean
physically forced, common to different readings, selected by dynamics, or
derived from the axioms.

The eight 24-piece blocks are consecutive slices of the explicitly declared
lexicographic order on the 192 used corner tuples. The four quarters are
consecutive pairs of those blocks. The 48 cell symmetries preserve the
incidence table but do not derive or canonize this partition.

**The forced subsets are a space, and the declared block sweep sees an
eight-element section of it.** Restricted to the 256 unions of the eight blocks of 24, the
forced family contains the empty set and is closed under symmetric difference,
and it has exactly 8 members. The planted-forced control carries the same
statement off the block lattice: a piece set built by folding 30 cuttings
together is forced, and so is its symmetric difference with the first half.

The first clause is automatic: the row space is a vector space. The measured
content is its intersection with the declared quarter/block union lattices,
the explicit positive and negative certificates, and the exact image dimensions.

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
dimension the five independently reconstructed forced indicators allow: their
block words span dimension 3, so orthogonality bounds the image dimension by 5,
and the measurement attains that bound. Equivalently, and checked word by word, every
kernel word pairs the two blocks inside each quarter of the second half and keeps
the first half even overall. Accordingly **exactly 8 of the 256 block unions are
forced**, two to the 8 less 5, and the direct-membership sweep agrees with the
annihilator on all 256.

**Every forced block union is a union of quarters.** No block of 24 pieces is
forced alone, and the two quarters of the first half are forced only together.
Read on the 15 named indicators, the sweep returns: forced `L`, `Q2`,
`Q3`, `R`, `whole`; free
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

The primary's reduced kernel basis has least weight 8 and greatest weight 20, and no
symmetric difference of two basis words comes in below 8 either, so 8 is the
smallest witness found by that explicitly bounded reduction. The block-parity
words of the first two witnesses are `10011100` and `01011100`; every witness
parity word lies in the measured block image and is odd on the block it was found
for, the two free quarters included.

## Method and independent reconstruction

The primary uses two eliminations over GF(2), run on the same table from
opposite sides:

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

The independent checker imports and executes no primary implementation. It uses
a Leibniz determinant rather than the primary minor formula, selects the largest
uncovered sample rather than the smallest in its exact-cover recursion, pivots
on least-significant rather than most-significant GF(2) bits, and constructs the
104-dimensional kernel from its reduced row space. It exhausts all 16 quarter
unions and 256 block unions and compares exact canonical population and census
identities with the primary receipt.

The controls are seeded at 74000 and drawn with the same generator every run. The
planted-forced control folds 30 cuttings into a piece set of weight 96 and hands
the runner nothing else; the runner recovers it blind as forced from a
combination of 44 pivot cuttings, which is not the planting set. Its symmetric
difference with the first half, a set that is no block union, is forced too, by
44 pivot cuttings verified the same way. The planted-free control draws 20 pieces
and finds a weight-8 kernel word meeting them oddly, after 0 redraws.

## Verification

Primary: 35 gates, `TOTAL: PASS=35 FAIL=0`. Independent reconstruction:
14 gates, `TOTAL: PASS=14 FAIL=0`.

- G01 the table is 15800 by 192 with 24 pieces to a cutting, in the exact-cover
  search and in the table alike.
- G02 every one of the 192 pieces is used by exactly 1975 cuttings, an odd count.
- G03 the elimination over the cuttings and the independent elimination over the
  pieces return the same rank 88, leaving a kernel of dimension 104.
- G04 the 15800 cuttings are pairwise distinct as piece sets.
- G05 all 104 kernel words meet every one of the 15800 cuttings evenly and are
  independent.
- G06 the 48 declared cell symmetries permute cuttings and pieces leaving the
  table fixed; they do not derive the lexicographic partition.
- G07 the symmetric difference of all 15800 cuttings is the whole piece set: all
  24 packed bytes come out full and all 192 column counts come out odd.
- G08 the whole set is carried a second way, by an explicit combination of 48
  pivot cuttings checked on all 192 piece coordinates.
- G09 no kernel word meets the whole set, either half or either quarter of the
  second half oddly — the five-set forcing profile reconstructed from the table.
- G10 the quarter-parity image is exactly `0000` and `1100`: inside the
  annihilator of the forced quarters, and with its generator present.
- G11 of the 16 quarter unions exactly the 8 annihilating the image are forced,
  the two quarter complements among them, and direct membership agrees with the
  annihilator one for one.
- G12 each of the 16 quarter unions carries its own certificate.
- G13 the block-parity image annihilates the block words of the 5 indicators
  reconstructed as forced, which bounds its dimension by 5; the measurement
  attains that bound at 5 with 32 words.
- G14 on all 256 block unions the two routes return the same answer.
- G15 exactly 8 of the 256 block unions are forced, two to the 8 less 5.
- G16 each of the 256 block unions carries its own certificate.
- G17 the 15 declared block indicators have exactly the named five-forced,
  ten-free profile.
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

Additional primary gates bind the exact geometric separation of all 15,168
co-occurring piece pairs, the Cycle-737 population/order receipt, and four
hostile controls: shifted support order, failed dependency status, a
sample-disjoint overlapping pair, and a flipped incidence bit. The independent
checker separately reconstructs the population, exact geometry, rank/kernel,
complete quarter/block censuses, named positive and negative certificates,
primary receipt identity, and order/incidence hostile controls.

## No-Go Discipline Gate

Negative assertion class: `derived_no_go_boundary`. The exact negatives are only
that, among the complete 16 unions of the declared quarters and 256 unions of
the declared eight blocks, the other 8 and 248 indicators are outside the GF(2)
row space; in particular no individual declared 24-piece block is forced.

**N1 — alternative-route enumeration.** Six attacks are executed:

1. `ATTEMPTED` — direct row-membership attack on every one of the 16 and 256
   indicators;
2. `ATTEMPTED` — kernel-annihilator attack built from the opposite-side column
   elimination;
3. `ATTEMPTED` — explicit positive certificates by folding named rows on all 192
   coordinates;
4. `ATTEMPTED` — explicit negative certificates via exact kernel words odd on
   every named free indicator;
5. `ATTEMPTED` — independent population and algebra attack using a Leibniz
   determinant, opposite exact-cover pivot, least-bit elimination, and a separately
   constructed kernel;
6. `ATTEMPTED` — partition and incidence mutations: a cyclic order shift changes
   the profile and a flipped incidence bit breaks exact regularity and identity.

**N2 — wall-independence audit.** D is the supplied 15,800 by 192 incidence
data, C is the binary additive subset/readout convention, O is the declared
lexicographic order together with its quarter/block union lattice (order and
partition collapse because the latter is defined from the former), and X is
physical or multi-cell extension.

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| D–C | no | no | yes |
| D–O | no | no | yes |
| D–X | no | no | yes |
| C–O | no | no | yes |
| C–X | no | no | yes |
| O–X | no | no | yes |

The finite census closes only the D/C/O question and leaves every X bridge open.

**N3 — hidden-wall scan.** The scan covers “canonical,” “symmetry,” “forced,”
“physical,” “all,” “only,” and “no.” “Canonical” was removed from the partition
claim: the blocks are declared lexicographic slices. “Forced” is defined as row
space membership and not physical necessity. “All” and “only” quantify just the
16 and 256 enumerated union lattices.

**N4 — residual matching.** Cycle 737 supplies only the exact finite population
and support-order identity, which both local runners reconstruct and hash-check.
Cycle 739 is chronological context only: no support-bound, search count, target
function, or certificate from it is consumed.

**N5 — rhetoric audit.** Both caches carry five resolution lines. Per-element
covers all 192 used columns; per-site covers one supplied coordinate cell;
per-mode is not executed; per-block covers all 16 and 256 declared unions; and
lattice-wide is not executed. No negative is stated beyond those scopes.

**N6 — partial-closure paths.** A different ordering or partition can be swept
with the same finite algebra; indeed the shifted-order hostile control changes
the result. Arbitrary subsets outside the block-union lattice, other coefficient
fields, nonlinear functionals, and other finite populations are separate
computable problems. Physical realization requires new bridge evidence.

**N7 — steelman.** A hostile reviewer should expect another support order to
produce a different block profile and should expect forced subsets outside this
256-member lattice. That attack succeeds against any universal reading and is
why none ships. It does not challenge the complete stated census for this
declared partition.

**N8 — cross-cycle echo.** Cycle 737 required an explicit used-piece universe
and exact geometric validation rather than trusting sample covers. This cycle
inherits both safeguards, binds the exact Cycle-737 population/order hashes,
and does not turn an enumeration convention into a symmetry or axiom.

**Status: PASS.** All N1–N8 items land with the note, and the five N5
resolution lines land in both canonical caches.

## Boundary and honest read

The eight blocks of 24 and four quarters of 48 are cut from the declared
lexicographic support order. The exact-cover search identifies the used pieces
and the 48 cell symmetries preserve the table, but neither supplies this
partition. A different order can cut different blocks from the same 192 pieces;
the shifted-order hostile control does so and changes the forced-union profile.
Both quarter and block statements are therefore order-relative.

The combination sizes — 48 for the whole set, 46 for `L`, 26 for `Q2`, 50 and 46
for the two complements, 44 in the planted control — are measured, not derived.
They are the sizes the pivot choice of this elimination happens to give. They are
certificates of forcedness, verified coordinate by coordinate; they are not
minimal representations and no minimality is claimed.

The primary membership sweep runs on one elimination engine. What narrows it is that
the annihilator route is built from the other elimination, so the agreement on
all 16 quarter unions and all 256 block unions is a check between two engines
rather than a restatement of one; and that both planted controls are answered
blind, one positive and one negative. Both engines still read the same incidence
table, so a fault in the table itself would not be caught by their agreement, nor
by the certificate gates, which re-verify against whatever table they are handed.
It is caught by exact geometry and regularity gates, row-order-invariant
Cycle-737 identity hashes, the flipped-bit hostile test, and an independent
reconstruction with different determinant, recursion, pivot, and kernel routes.

Witness weight 8 is what a reduction over the reduced kernel basis reaches,
supported by a complete scan of the pairs of basis words. It is not a proof that
no kernel word of lower weight meets a given free block oddly; minimum weight
over the full kernel is not searched here and is not claimed.

The five named forced indicators are reconstructed locally rather than assumed.
Given that profile, the quarter image lies in the annihilator
`{0000, 1100}`; the generator is then found explicitly, and direct membership
and annihilator routes agree on all 16 and 256 unions. The measured value of the
block-image dimension, 5, was not predicted in advance beyond the bound of 5 that
the quarter constraints supply; it is reported as measured, and the note is
written from the measurement.

Nothing here supplies a physical reading, a dynamics, a metric, or a selection
among cuttings. It says which declared subset indicators have invariant meet
parity among supports of one fixed finite reading, on this supplied finite
object and declared order. It does not classify arbitrary subsets outside the
quarter/block union lattices.

Proof-obligation disposition: **CONDITIONAL**. The finite GF(2) theorem is
closed for the supplied population and declared partition. Any physical,
order-independent, arbitrary-subset, or multi-cell interpretation remains open.

## Claim type

`Claim type: bounded_theorem`. The claims are finite, integer and
field-with-two-elements statements about an explicitly constructed 15800 by 192
table, each one carrying a certificate that is checked in the runner. The
conditionality is stated above: the cell/table/cost and binary functional are
supplied, and the quarter/block partition is relative to the declared
lexicographic support order.

## Artifacts

- Primary runner:
  [`scripts/physical_cell_cutting_forced_certificate_cycle740_2026_08_05.py`](../scripts/physical_cell_cutting_forced_certificate_cycle740_2026_08_05.py)
- Independent checker:
  [`scripts/physical_cell_cutting_forced_certificate_cycle740_independent_check_2026_08_05.py`](../scripts/physical_cell_cutting_forced_certificate_cycle740_independent_check_2026_08_05.py)
- Primary canonical cache:
  [`logs/runner-cache/physical_cell_cutting_forced_certificate_cycle740_2026_08_05.txt`](../logs/runner-cache/physical_cell_cutting_forced_certificate_cycle740_2026_08_05.txt)
- Independent canonical cache:
  [`logs/runner-cache/physical_cell_cutting_forced_certificate_cycle740_independent_check_2026_08_05.txt`](../logs/runner-cache/physical_cell_cutting_forced_certificate_cycle740_independent_check_2026_08_05.txt)
- Primary receipt:
  [`outputs/physical_cell_cutting_forced_certificate_cycle740_2026_08_05_receipt_2026-08-05.json`](../outputs/physical_cell_cutting_forced_certificate_cycle740_2026_08_05_receipt_2026-08-05.json)
- Independent receipt:
  [`outputs/physical_cell_cutting_forced_certificate_cycle740_independent_check_2026_08_05_receipt_2026-08-05.json`](../outputs/physical_cell_cutting_forced_certificate_cycle740_independent_check_2026_08_05_receipt_2026-08-05.json)

## Audit

`Audit: unset.` This note sets no audit verdict and predicts none. The
independent audit lane is the sole authority on audit language for this package.
