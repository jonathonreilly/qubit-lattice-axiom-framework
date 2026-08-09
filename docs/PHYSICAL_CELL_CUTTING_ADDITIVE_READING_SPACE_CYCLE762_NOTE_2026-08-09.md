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
next_trace_action: "independently audit the exact finite-cell row-space theorem; any physical use must separately construct a cutting-independent map from pieces to pairwise-disjoint Record content"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
conditional_surface_status: "open: physical Record interpretation awaits a supplied piece-to-Record-content map"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the runner certifies exact equalities for one stipulated finite cell, while the physical Record bridge and any multi-cell extension remain open"
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
- The Record/additivity wording in
  `docs/MINIMAL_AXIOMS_2026-06-29.md` is non-load-bearing physical context. Its
  use requires the open bridge stated below.
- The runner reads its own source for an integrity check. That package-local
  read is not an external scientific input.

## Review record (review loop iteration 1, 2026-08-09)

Review preserved the exact finite-cell theorem and narrowed the physical
interpretation. Interior-disjoint pieces were not shown to be pairwise-disjoint
Records, so the required piece-to-Record-content map is now stated explicitly as
open. The measured corner-incidence counts remain; conclusions about untested
allocation constructions were removed. The runner was made fail-closed, given an
explicit timeout, and its ambiguous letter-number gate labels were replaced by
domain-explicit names. No hard landing condition remains beyond the checks named
in this note.

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
features carry the match; and the contact with the additivity clause of the
fixed-reality axiom, together with a plain account of where that contact stays
open.

## The object

The runner builds the cell from scratch. Of the five-corner sub-simplices of the
four-cube, 2672 have determinant of absolute value 1; the adjacency cost floor
among them is 6, attained by 400 of them. Cuttings are found as exact covers of 625
sample points of divisor 80, chosen so that no sample point lies on a facet plane
of any kept piece; `OBJECT` checks that genericity condition directly rather than
assuming it. Genericity is what makes the sample search complete: with no sample
point on a facet plane, a genuine tiling of the cell covers each sample point
exactly once, so no tiling escapes the search over exact covers, and the search
over exact covers is itself complete. `TILING` then certifies the other direction,
that what the search returns really is a tiling. The search returns 15800 cuttings,
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

The fixed-reality axiom in `docs/MINIMAL_AXIOMS_2026-06-29.md`
says, verbatim:

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

That clause supplies arithmetic only after its Record-level hypotheses are met.
`TILING` certifies that each cutting's 24 geometric simplices have pairwise-disjoint
interiors and fill the cell, but geometric interior-disjointness is not itself
pairwise disjointness of Records. A physical use therefore needs a
cutting-independent map from every piece to Record content such that the 24 images
in every cutting are pairwise-disjoint finite Record collections and have the same
whole-cell union. No such map is supplied here. If a future construction supplies
one, additivity makes every cutting return the same total, which is exactly the
condition characterized by the cover-table row space.

`CORNER-INCIDENCE` records that the 24 pieces of each cutting use 120
simplex-corner incidences on 16 corners, with multiplicities from 4 through 24.
This is a finite incidence statement. Raw simplex-corner incidence has overlaps;
the gate neither tests nor classifies alternative ownership or allocation maps.

The piece-to-Record-content map is a named open bridge, not a result of this
cycle. The four finite claims stand on their own as exact statements about the
constructed cell and do not depend on that bridge.

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

- The piece-to-Record-content map is open. Claims 1 through 4 are computational
  identities about this cell and are independent of that bridge; the axiom contact
  is conditional on it.
- Raw simplex-corner incidence uses 120 slots on 16 corners, with multiplicities
  from 4 through 24. A Record-level application needs a separate ownership or
  allocation map satisfying the axiom's disjointness premise; none is tested here.
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
