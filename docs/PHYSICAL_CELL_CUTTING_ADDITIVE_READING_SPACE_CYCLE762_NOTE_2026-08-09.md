# Each Table's Row Space Is The Other Table's Space Of Additive Readings

**Date:** 2026-08-09
**Type:** bounded_theorem
**Runner:** [scripts/physical_cell_cutting_additive_reading_space_cycle762_2026_08_09.py](../scripts/physical_cell_cutting_additive_reading_space_cycle762_2026_08_09.py)
Audit: unset.

## Trace gate

```yaml
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "independently audit the exact finite-cell row-space theorem; any physical use must separately supply both a cutting-independent piece-to-Record-content map and a scalar finitely additive readout"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
conditional_surface_status: "open: physical interpretation awaits both a supplied piece-to-Record-content map and a scalar finitely additive readout"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the runner certifies exact equalities for one stipulated finite cell, while the Record-content map, scalar finite-additivity premise, and any multi-cell extension remain open"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports and provenance

- The finite theorem imports no measured value, literature value, fitted
  selector, external scientific dataset, or generated audit status. The unit
  four-cube, determinant-one simplex rule, adjacency-cost floor, and generic
  divisor-80 sample are declared construction choices; all counts, ranks, and
  incidences are recomputed exactly by the runner.
- The preceding cycle's projector identity is provenance context rather than a
  proof input: this runner rebuilds the object and rechecks both row-space
  equalities directly.
- The current [Record / Fixed Reality](MINIMAL_AXIOMS_2026-06-29.md) wording is
  non-load-bearing context for the finite theorem. It supplies neither a
  scalar readout functional nor finite additivity. Those structures and the
  piece-to-Record-content map are separate open premises for any physical use.
- The runner reads its own source for an integrity check. That package-local
  read is not an external scientific input.

## Review record (review loop repair iteration 1, 2026-08-15)

Review preserved the exact finite-cell theorem and narrowed the physical
interpretation. The piece-to-Record-content map and the scalar finitely additive
readout are both stated explicitly as open. The runner now binds sample visibility,
the exact tiling census, the exact corner range, and both exact control values.
The obligation graph below records every finite proof leaf. The canonical index
and dependency manifest are part of this repair; no audit status is changed.

## Exact target and obligation graph

Let `A` be the `15800 x 192` cutting-by-piece incidence matrix and `B` the
`192 x 192` cover-by-piece incidence matrix constructed by the runner. The
assignment field is `Q`, and the domain is `Q^192`. Define

- `E_A = {x in Q^192 : A x is constant across all cuttings}`;
- `E_B = {x in Q^192 : B x is constant across all covers}`.

The exact finite target is the conjunction of these four numbered claims:

1. `E_A = row(B)`, and both spaces have dimension 105.
2. `E_B = row(A)`, and both spaces have dimension 88.
3. `row(A) + row(B) = Q^192`, while
   `row(A) intersection row(B) = span{1}`.
4. The common `A`-reading on `E_A` is `sum(x)/8`, and the common `B`-reading
   on `E_B` is `sum(x)/24`.

The acyclic obligation graph is as follows. Every finite leaf is proved here;
none is imported from the preceding cycle.

- `P0` [proved here by explicit construction]: fix the labelled cube,
  assignment field, simplex and cost rules, cutting and cover rules, and the
  orientations of `A` and `B`.
- `P1` [proved here; depends on `P0`]: enumerate the determinant-one pieces,
  their volume, the cost floor, and the 400 kept pieces (`OBJECT`).
- `P2` [proved here; depends on `P1`]: certify facet avoidance and nonempty
  visibility of every kept piece, exhaust the sample exact-cover search, and
  bind the cutting, used-piece, and multiplicity censuses (`OBJECT`).
- `P3` [proved here; depends on `P1`, `P2`]: certify all 15168 co-occurring
  pairs, including the 1536 boundary-intersection cases, and conclude that each
  24-piece cutting tiles the cube (`TILING`).
- `P4` [proved here; depends on `P2`]: exhaust the size-eight noncooccurrence
  cliques and verify that every one meets every cutting exactly once (`TILING`).
- `P5` [proved here; depends on `P2`, `P4`]: validate the Gram substitution,
  kernels, ranks 88 and 105, and nullities 104 and 87 (`GRAM-RANK`,
  `TABLE-RANKS`).
- `P6` [proved here; depends on `P5`]: adjoin the nonkernel constant direction
  to each kernel and obtain the equal-reading dimensions (`CONSTANT-DIRECTION`,
  `READING-DIMENSIONS`).
- `P7` [proved here; depends on `P5`, `P6`]: verify both row-space containments
  independently and close Claims 1 and 2 by exact joint ranks
  (`CUTTING-READINGS`, `COVER-READINGS`).
- `P8` [proved here; depends on `P5`, `P7`]: bind joint rank 192 and constant
  column sums, then close Claim 3 by the dimension formula
  (`SPAN-INTERSECTION`).
- `P9` [proved here; depends on `P2`, `P4`, `P7`]: use both column-regularity
  identities, with nonzero-sum witnesses, to close Claim 4 (`COMMON-TOTALS`).
- `P10` [proved here; depends on `P2`, `P4`, `P5`]: bind the exact overlap set,
  zero-target dimensions, shifted joint rank, corner range, source hygiene, and
  resource envelope (the three control gates and the remaining runner gates).
- `P11` [open; outside the finite target]: construct a physical Record-content
  map and separately supply a scalar finitely additive readout.

Degenerate determinant-zero simplices are outside the piece definition. Facet
contacts are allowed and handled by exact relative-interior checks; empty sample
masks are rejected by `OBJECT`. The zero assignment and the constant direction
are included explicitly, and the exact positive cutting and cover counts exclude
empty-family edge cases. After `P1` through `P10` close, the strongest missing
lemma for the four finite claims is none. `P11` remains open and cannot be used to
promote those finite claims to a physical reading theorem.

## What this is

The object is one cell, taken as the unit four-cube on its sixteen corners. A piece
is a five-corner sub-simplex whose four edge vectors from its first corner have
determinant of absolute value 1, so a piece has volume one twenty-fourth of the
cell; among those, the pieces at the adjacency cost floor are kept. A cutting is a
set of kept pieces with pairwise disjoint interiors that together fill the cell. A
cover is an eight-piece set no two of whose pieces ever share a cutting; the
`TILING` gate certifies that each such set meets every cutting exactly once, which is the
property an earlier cycle of this lane derived and which is re-verified, not
assumed, in the build below. An assignment gives a number to each piece. A cutting
reads an assignment by summing it over the pieces of that cutting; a cover reads it
by summing it over the pieces of that cover. Two tables record which piece belongs
to which family member: the cutting table and the cover table.

The result is one sentence in two halves. The assignments whose cutting readings
are all equal to each other are exactly the row space of the cover table, and the
assignments whose cover readings are all equal to each other are exactly the row
space of the cutting table. Each table's row space is the other family's space of
additive readings, and the two dimensions are 105 and 88.

## What was already known

The preceding cycle of this lane recorded an exact whole-number identity relating
the cover-side lifted projector, the cutting-side lifted projector, the identity,
and the all-ones matrix, and read it as forcing the dimension count
105 = 192 - 88 + 1. That identity motivated this characterization. It is not an
input here: the runner rebuilds the cell and rechecks the relevant incidences,
kernels, ranks, and containments.

The characterization stated below is a short consequence of that identity together
with the two dimensions this lane had already measured, and no part of its
mathematics is claimed as new. In one direction the identity says that an
assignment built from the cover table is read at a single level by every cutting;
in the other it says the same with the two families swapped; and once one direction
is in hand, equality of dimensions turns the containment into an equality, makes
the two row spaces span everything, and leaves their intersection at the constants.
A reader holding the preceding cycle's identity can reach every claim below in a
few lines, and this note does not pretend otherwise.

What this cycle contributes is therefore not the algebra. It is the statement in
reading language rather than in projector language; an independent rebuild of the
whole cell from scratch over the rationals, which re-measures every input number
instead of citing it; three discriminating controls showing which structural
features carry the match; and a separation between current Record wording and
the additional map and scalar-additivity premises needed for a physical use.

## The object

The runner builds the cell from scratch. Of the five-corner sub-simplices of the
four-cube, 2672 have determinant of absolute value 1; the adjacency cost floor
among them is 6, attained by 400 of them. Cuttings are found as exact covers of 625
sample points of divisor 80. `OBJECT` checks both that no sample point lies on a
facet plane of any kept piece and that every kept piece contains at least five
sample points. Thus every piece of a genuine tiling is visible, while facet
avoidance makes its masks pairwise disjoint; the tiling therefore occurs in the
exhaustive exact-cover search. `TILING` then certifies the other direction, that
what the search returns really is a tiling. The search returns 15800 cuttings,
each of 24 pieces. Exactly 192 of the 400 floor pieces occur in a cutting at all,
and each of those 192 lies in 1975 cuttings. There are 192 covers, and the cover
table has every row sum and every column sum equal to 8.

`TILING` verifies that each cutting is a genuine tiling rather than an artifact of
the sampling: every piece has volume 1 over 24, every cutting holds 24 of them, and
all 15168 co-occurring piece pairs are certified interior-disjoint exactly, 13632
of them by a separating facet plane and the rest by an exact computation of the
affine dimension of the intersection. Twenty-four pieces of volume 1 over 24 with
pairwise disjoint interiors fill the cell.

## The characterization

Write the cutting table for the 15800 by 192 zero-one table of cuttings against
pieces, and the cover table for the 192 by 192 zero-one table of covers against
pieces.

`TABLE-RANKS` measures rank 88 and kernel dimension 104 for the cutting table, and
rank 105 and kernel dimension 87 for the cover table. `CONSTANT-DIRECTION`
measures that one over 24 times the constants reads 1 on every cutting, and one
over 8 times the constants reads 1 on every cover, so each side has a particular
solution and the constants lie in neither kernel. `READING-DIMENSIONS` therefore
measures the two solution sets: the assignments with all cutting readings equal
form a space of dimension 105, and the assignments with all cover readings equal
form a space of dimension 88.

`CUTTING-READINGS` measures that the first of those spaces and the row space of the
cover table have joint rank 105, which is the dimension of each; the two spaces are
therefore equal. `COVER-READINGS` measures that the second space and the row space
of the cutting table have joint rank 88, again the dimension of each, so those two
are equal as well. Both directions are computed here over the rationals, with no
floating point anywhere in the algebra, and neither is inferred from the other.

The rank of the cutting table is obtained without eliminating on a table of 15800
rows. `GRAM-RANK` justifies the substitution used: the 192 by 192 product of the
cutting table with itself is built twice by different routes and the two builds
agree, its kernel is checked to annihilate every one of the 15800 cutting rows, and
the rank is then recovered independently from the cutting table's own rows, two
evenly spread selections of 400 and of 800 rows both giving 88.

## The sum and the intersection

`SPAN-INTERSECTION` measures that the two row spaces together have joint rank 192,
so they span the whole assignment space. Since their dimensions are 88 and 105,
their intersection has dimension 88 + 105 - 192 = 1. The constants lie in both row
spaces, because the column sums of both tables are constant: the column sums of the
cutting table are all 1975 and those of the cover table are all 8. The intersection
is therefore exactly the constant assignments, and nothing else is shared.

`DIMENSION-CHECK` records the bookkeeping that follows: 105 is 192 minus 88 plus
1, 88 is 192 minus 105 plus 1, and 88 plus 105 is 192 plus 1.

Not every gate here is discriminating, and `DIMENSION-CHECK` is the clear case. It
is arithmetic on numbers the earlier gates have already measured, and it would
pass for any three numbers standing in that relation; it is a consistency record,
not evidence. The load-bearing gates are `CUTTING-READINGS`, `COVER-READINGS`,
`SPAN-INTERSECTION`, and `COMMON-TOTALS`. `COVER-CONTROL`, `ZERO-CONTROL`, and
`SHIFT-CONTROL` distinguish those results from coarse alternatives.

## The two totals

`COMMON-TOTALS` measures the two common readings. For an assignment in the
105-dimensional space, the common cutting reading is the plain sum of the
assignment divided by 8. For an assignment in the 88-dimensional space, the common
cover reading is the plain sum divided by 24. The gate checks this on 3 elements of
each space, each with nonzero sum, so the check is not the empty statement that 0
equals 0.

Both totals come from the column sums. Summing the cutting readings over all 15800
cuttings counts each piece 1975 times, giving 1975 times the sum of the assignment;
summing the same constant reading over 15800 cuttings gives 15800 times it; and
15800 is 8 times 1975. Summing the cover readings over all 192 covers counts each
piece 8 times, giving 8 times the sum; summing the constant over 192 covers gives
192 times it; and 192 is 24 times 8.

## The axiom contact

The current [Record / Fixed Reality](MINIMAL_AXIOMS_2026-06-29.md) text says:

> Only records are readable. A readout value is determined by record content
> alone. A site with no record cannot be read.

This supplies content determination and unreadability in the absence of a
Record. It does not supply a scalar readout functional, finite additivity, or an
empty-set normalization. The word "reading" in Claims 1 through 4 denotes only
the stipulated finite sums that define `A x` and `B x`.

`TILING` certifies that each cutting's 24 geometric simplices have pairwise-disjoint
interiors and fill the cell, but geometric interior-disjointness is not itself
pairwise disjointness of Records. A physical use therefore needs two separately
supplied structures: a cutting-independent map from every piece to Record content
whose 24 images in every cutting are pairwise-disjoint finite Record collections
with the same whole-cell union, and a scalar functional on those contents that is
finitely additive on those collections. Neither is supplied here. The finite
theorem never evaluates an empty collection, so it neither needs nor imports an
empty-set normalization; any extension that does use one must supply it separately.
Only conditional on both open structures would the equal-cutting condition acquire
the proposed physical reading.

`CORNER-INCIDENCE` records that the 24 pieces of each cutting use 120
simplex-corner incidences on 16 corners, with multiplicities from 4 through 24.
This is a finite incidence statement. Raw simplex-corner incidence has overlaps;
the gate neither tests nor classifies alternative ownership or allocation maps.

The piece-to-Record-content map and scalar finite additivity are named open
premises, not results of this cycle. The four finite claims stand on their own as
exact statements about the constructed cell and do not depend on either premise.

## Controls

Three discriminating controls test nearby coarse alternatives.

`COVER-CONTROL` takes a cover, which lies in the 105-dimensional space, and reads
it on the cover side. The values are 0, 1, 2, 4, and 8, directly distinguishing
the two reading conditions.

`ZERO-CONTROL` replaces the constants by the zero space and obtains dimensions
104 and 87. This certifies the extra constant direction used in the dimension
bookkeeping.

`SHIFT-CONTROL` applies a cyclic column shift to the cover table. The shifted table
still has rank 105 and every row sum and column sum equal to 8, so it matches the
original on every coarse feature; but its joint rank with the 105-dimensional
space is 191 rather than 105. Thus the equality depends on the incidence content,
not only the shifted table's rank and marginal sums.

## Measured totals

The runner has 17 gates and prints `TOTAL: PASS=17 FAIL=0`, exiting 0. Elapsed time
is under 300 seconds and peak resident memory is under 1500 MB; `RESOURCE-BOUND`
reports both as bounds rather than as timings. Total stdout is under 3000
characters. The runner carries no randomness and two runs give byte-identical
output. All ranks, kernels and joint ranks are computed exactly over the rationals.

## Boundary

- The piece-to-Record-content map and the scalar finitely additive readout are
  both open. Claims 1 through 4 are computational identities about this cell and
  are independent of both premises; physical contact is conditional on both.
- Raw simplex-corner incidence uses 120 slots on 16 corners, with multiplicities
  from 4 through 24. A Record-level application needs a separate ownership or
  allocation map and a scalar-additivity supplier; neither is tested here.
- The ranks 88 and 105 are measured by the complete search over this one cell. A
  structural derivation predicting those ranks from four-cube geometry remains an
  open question.
- This is a one-cell theorem. Multi-cell joining and the lane's whole-number
  bookkeeping are outside its target.
- The characterization is an equality of two subspaces of the 192-dimensional
  assignment space. It is not a correspondence between individual cuttings and
  individual covers, and it says nothing about which piece goes with which.
- The cuttings are found as exact covers of a sample point set, and the tiling
  property is then certified separately for all 15168 co-occurring piece pairs. That
  certificate is what makes the cuttings tilings of the cell rather than of the
  sample; the sampling itself proves nothing.
