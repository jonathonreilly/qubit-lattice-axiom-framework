# Twelve-piece exclusion for six finite algebraic readings — Cycle 739

Date: 2026-08-05

Cycle: 739

Claim type: bounded_theorem

Authority: none.

Audit: unset.

Constitutional effect: none. No axiom or primitive is proposed or adopted.
Audit status is set only by the independent
audit lane, and effective status is pipeline-derived.

Primary runner:

- [`physical_cell_cutting_twelve_frontier_cycle739_2026_08_05.py`](../scripts/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05.py)

Independent checker:

- [`physical_cell_cutting_twelve_frontier_cycle739_independent_check_2026_08_05.py`](../scripts/physical_cell_cutting_twelve_frontier_cycle739_independent_check_2026_08_05.py)

## Supplied model and direct dependencies

This is a theorem only about a supplied finite model: the four-cube on the
sixteen corners of `{0,1}^4`, with three labelled spatial columns, one labelled
tick column, normalized-volume-one corner 4-simplices, the supplied
four-coordinate L1-pair cost, and the declared 48-element spatial-rotation /
tick-flip action. A cutting is 24 such pieces with disjoint interiors and total
normalized volume 24. A reading is a fixed GF(2) function on the resulting
15,800 cuttings. None of those choices is asserted to be physically selected.

[Cycle 737](PHYSICAL_CELL_CUTTING_LEAST_COMPUTING_SETS_CYCLE737_NOTE_2026-08-05.md)
is a direct dependency. Its generated receipt binds the certified geometric
population, stable 192-piece order, exact identities of the eight constant and
nonconstant algebraic readings, and the complete support search through size
eight. [Cycle 738](PHYSICAL_CELL_CUTTING_SIZE_TEN_FRONTIER_CYCLE738_NOTE_2026-08-05.md)
is also direct: its primary and independent receipts bind exact-weight-ten
UNSAT for those same readings. The Cycle 739 primary reconstructs the finite
population and readings, then refuses a positive result unless their canonical
hashes and both predecessor receipts match.

The [Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md) supply only the spatial
`Z^3` nearest-neighbour lattice and proper cubic rotations. The registered
[kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
supplies only equal spatial/tick kinetic-form graining. Neither source selects
this one-box domain, the corner-simplex class, the supplied cost, these
algebraic readings, a physical assembly cell, or a tick--Admissibility
realization.

## Result

The object is the supplied unit four-cube on its 16 corners, cut into pieces at
the floor of the supplied cost. There are 15800 such cuttings, each using 24
pieces, drawn from 192 pieces in all. A set of pieces carries a reading when, on every one of
the 15800 cuttings, the parity of how many of its pieces that cutting uses
reproduces the reading.

A complete search of every set of exactly twelve pieces, against eighteen
readings at once, gives the counts

```
7808,3072,0,0,0,0,0,0,661,25,38,38,1,1,1,2,1,0
```

in the order: the constant zero reading, the constant one reading, the two sides
of each of the three paired nonconstant readings, the four Cycle 738 controls,
the five planted twelve-piece controls, and one synthetic reading whose forced
total parity is odd.

The six nonconstant algebraic-reading entries are all 0. The complete searches
at every set of at most eight pieces, at exactly ten, and now at exactly twelve
are all empty for those six, and each of the six forces an even total parity,
which bars every odd size.
So no set of twelve or fewer pieces carries any of them, and the minimum
support for each is at least fourteen.

The bound is not vacuous. Measured apart from the search, every one of the
readings except the synthetic one lies in the column space of the incidence
table, so each of the six nonconstant readings is carried by some piece set;
what this cycle measures is that no such set has twelve or fewer pieces. The synthetic reading
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
ten, and every set of exactly twelve. At twelve, an expected-inventory ledger
is built independently of execution; every licensed cell was completed and all
1167 scheduled splits executed exactly once. A split is credited only after its
meet returns successfully.

## Verification

The primary carries 40 gates: 38 finite search/certificate gates plus two
direct-dependency identity gates. Its canonical cache records the exact total.

- Known answer, at most eight pieces: 648 sets carry the constant zero reading,
  in 22 orbits of the cell symmetries — 17 of size 24 and 5 of size 48 — and 192
  carry the constant one reading, in 5 orbits, 2 of size 24 and 3 of size 48. The
  six nonconstant readings and the synthetic odd reading are empty there. All
  845 recorded sets recompute to their own reading.
- Known answer at ten: the first twelve readings give 0,0,0,0,0,0,0,0,108,1,2,0,
  reproducing the direct Cycle 738 result exactly; 111 recorded sets verified; the
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
- Budgets: under the 900 second ceiling and 1600 MB ceiling; canonical stdout
  remains under the repo's 6000-character limit.

The independent checker imports and executes neither the primary nor its meet
engine. It rebuilds the piece population with the opposite exact-cover pivot,
binds the canonical row/order/function identities, selects an independent
88-row GF(2) basis, and encodes exact-weight-twelve syndrome equations using
Tseitin XOR clauses plus an exact cardinality totalizer. An independently
maintained CaDiCaL backend recovers exact-weight-twelve constant-reading SAT
controls and proves UNSAT for the six nonconstant targets; every returned SAT
support is checked against all 15,800 rows. It separately reconstructs the
certificate-tree ranks
and first-quarter kernel distribution.

Hostile controls make the negative result fail closed: a locally skipped
zero-yield primary split makes the expected/executed inventory gate fail; a
planted twelve-piece syndrome is SAT and is verified on all rows; a target-bit
mutation changes the solver result or canonical identity; local primary,
Cycle 737, and Cycle 738 mutations invalidate receipt hashes; and a failed
generated verdict cannot satisfy the checker acceptance predicate.

Canonical evidence:

- [primary cache](../logs/runner-cache/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05.txt)
- [independent cache](../logs/runner-cache/physical_cell_cutting_twelve_frontier_cycle739_independent_check_2026_08_05.txt)
- [primary receipt](../outputs/physical_cell_cutting_twelve_frontier_cycle739_2026_08_05_receipt_2026-08-05.json)
- [independent receipt](../outputs/physical_cell_cutting_twelve_frontier_cycle739_independent_check_2026_08_05_receipt_2026-08-05.json)

The required fresh sequence is primary first and independent checker second.
Both generated receipts must say `status: pass` with zero failures and current
content hashes.

## Boundary / honest read

The primary meet engine produces the detailed twelve-piece census and orbit
tables. The independent exact-cardinality solver removes single-engine
dependence from the load-bearing six UNSAT results and independently recovers
SAT controls for both constant readings. The five planted readings and local
subcode enumeration remain controls of the primary implementation, not a claim
of independence.

The block profile is relative to the fixed canonical ordering of the 192 columns.
Which blocks are forced, the internal dimensions 0,0,0,0,0,0,1,2 and 0,0,6,13,
and the rank drop at the first quarter are measured, not derived: a different
ordering of the same 192 pieces would relabel the table, and nothing here shows
that the ordering is forced.

The minimum-support statement is a lower bound and nothing more. Sizes above
twelve were not searched, so this says the six fixed nonconstant algebraic
readings need at least fourteen pieces, not that fourteen suffices.

The four Cycle 738 controls are nonempty at twelve, at 661, 25, 38
and 38, and the constant readings at 7808 and 3072. Those counts are what a
search able to find things looks like on this object; they are recorded here, not
otherwise interpreted.

No physical charge, conservation law, cell/tick selection, arbitrary piece
class, nonlinear or nonbinary observable, multi-cell gluing, boundary,
arbitrary-size, or continuum statement is made.

## No-Go Discipline Gate

Negative assertion class: `derived_no_go_boundary`. The only exclusion is the
minimum-support bound for six fixed algebraic functions on one supplied finite
15,800-row, 192-column GF(2) incidence system.

- **N1 — five normalized attack families.** (1) `ATTEMPTED`: the primary's
  quarter/eighth meet-in-the-middle formulation enumerates every licensed cell
  and scheduled split at weights through twelve; all six targets return zero.
  (2) `ATTEMPTED`: the independent checker uses an opposite exact-cover pivot,
  independent row basis, CNF XOR encoding, exact-cardinality totalizer, and
  CaDiCaL; all six exact-weight-twelve questions are UNSAT. (3) `ATTEMPTED`:
  whole-support row-space parity independently excludes every odd cardinality.
  (4) `ATTEMPTED`: canonical row/order/function hashes attack the wrong-target
  route and bind the searched bytes to Cycle 737. (5) `ATTEMPTED`: hostile
  skip, planted-SAT, target-bit, dependency, and failed-verdict mutations attack
  completeness accounting and fail-closed evidence transport. These families
  differ in formulation, invariant, and terminal obligation; they are not
  alternate descriptions of one implementation.
- **N2 — condition independence.** The conditions are `F`, the supplied finite
  model/population; `R`, the six fixed reading identities; and `K`, support
  cardinality at most twelve. Closing or changing any one does not close either
  other: `F↛R`, `R↛F`, `F↛K`, `K↛F`, `R↛K`, and `K↛R`. None is collapsed or
  presented as an independent physical wall.
- **N3 — hidden-condition scan.** “Supplied,” “fixed,” “canonical ordering,”
  and the search construction are load-bearing and are stated explicitly. The
  one-box domain, corner-simplex class, minimum-cost population, GF(2) reading,
  192-column support universe, labelled tick, 48-element action, and maximum
  searched cardinality are all named. “Canonical” means the receipt-bound
  finite column order, not framework selection. No hidden framework premise is
  used.
- **N4 — residual matching.** Cycle 737 supplies exactly the same population,
  column order, six function identities, and complete exclusion through size
  eight. Cycle 738 supplies exactly the same targets' exact-weight-ten UNSAT.
  Cycle 739 adds exact-weight-twelve UNSAT and the same whole-support even-parity
  certificate. The receipt hashes and canonical function hashes enforce these
  residual matches; no broader no-go is cited.
- **N5 — rhetoric audit.** The canonical primary cache lands substantive
  `per_element`, `per_site`, `per_mode`, `per_block`, and `lattice_wide`
  execution lines. The theorem is checked per element and on the full supplied
  finite block. Site-field, mode, and lattice-wide extensions are explicitly
  not executed and are not claimed.
- **N6 — partial-closure paths.** Exact weight fourteen can be searched to test
  sufficiency without adding an axiom. Other piece classes, costs, coefficient
  fields, and multi-cell transports are separate supplied finite models or
  bridge theorems. The registered primitives add none of them. These are open
  extensions, not impossibility claims or proposals for new primitives.
- **N7 — steelman.** A hostile reviewer should first suspect a skipped
  zero-yield partition, because positive-return verification alone cannot detect
  that omission; the explicit expected/executed split ledger and hostile skip
  mutation now expose it. The next actionable attack is an exact-cardinality
  formulation sharing neither pivot rule nor meet engine; the independent CNF
  checker performs that attack. A smaller support could still exist after
  changing the supplied piece universe, reading, or coefficient field, but that
  is a different terminal problem and is outside this narrow theorem.
- **N8 — cross-cycle echo.** Cycles 737 and 738 are the exact same minimum-
  support ladder at smaller cardinalities; both were strengthened by independent
  exact search and canonical identity binding rather than rhetoric. Cycle 736's
  negative move-response statements concern different equations and are not
  reused as support. The applicable prior repair mechanism—new exact search at
  the next cardinality plus hostile and identity controls—is the mechanism used
  here.

No-Go Discipline status: **PASS**, conditional on the canonical fresh
primary-then-independent execution recording zero failures.
