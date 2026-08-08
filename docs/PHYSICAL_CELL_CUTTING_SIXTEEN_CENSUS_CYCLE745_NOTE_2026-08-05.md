# The complete sixteen census through an anchored slice — Cycle 745

Date: 2026-08-05

Authority: none

Audit: unset.

Status: computational identities of the finite cutting system

Claim type: computational identities

Runner:

- [paired rebuild-and-gate runner](../scripts/physical_cell_cutting_sixteen_census_cycle745_2026_08_05.py)

Scope: computational identities of the finite cutting system. Every number
below is machine-checked by the paired runner, which rebuilds the cell
complex, the cuttings, the readings, the symmetries and the anchored tables
from scratch and gates each quantity in place. Constitutional effect: none.
This package changes no axiom, no framework Admissibility rule, no primitive,
no policy, and no audit status, and it adds no import and no assumption to
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## Headline

The sixteen-piece carriers of the six charge readings are completely
enumerated. The four reading carries exactly 132 sixteen-piece sets and no
others, reconstructed as the group images of an 11-member anchored slice and
re-verified one by one directly against the incidence columns. The other five
charges carry none, and since forced parity bars every odd size, their least
possible carrier size rises to eighteen. Under the 48 cutting symmetries the
census splits into 15 orbits — ten of size 6, four of size 12 and one of size
24; under the full group of order 384 it splits into 6 orbits — three of size
12, two of size 24 and one of size 48.

## The rebuilt system

The runner rebuilds the incidence table of the cutting system from scratch:
15800 distinct cuttings on 192 pieces, each cutting using 24 pieces, each
piece used in exactly 1975 cuttings, the overlap table with constant diagonal
1975, and all 15800 piece supports pairwise distinct. The two seeded
order-two piece permutations of the earlier cycles are rebuilt by the same
seeded refinement; each is an involution lying outside the 48 cutting
symmetries, carrying cuttings to cuttings and fixing all eight readings, and
together with the 48 they act on the 192 pieces with a single orbit. Their
closure is then measured directly: the fifty generators close into a group of
order 384 whose images of the anchor piece reach all 192 pieces.

## Why an anchored slice is complete

Every element of that group carries cuttings to cuttings and fixes each
charge reading, so it maps sixteen-piece carriers of a charge to sixteen-piece
carriers of the same charge. The group is transitive on the pieces, so every
carrier has at least one group image holding the chosen anchor piece. The
anchored slice — the carriers through the anchor — therefore meets every
group orbit of carriers, and the full census is recovered as the set of all
group images of the slice. Two measured facts pin the arithmetic: each of the
192 pieces lies in the same number of census sets as the anchor, and the
census holds exactly twelve sets for each anchored one.

## The anchored search

Parity licensing leaves the same cell list for every charge: the licensed
cells of a charge number 5, 14, 30, 55, 91, 140, 204 and 285 at the even
sizes two to sixteen, the steps being consecutive odd squares, and all six
charges license the same 285 cells at sixteen in one shared pass. Of those
285 cells, 204 hold a piece in the last quarter — and a subset through the
anchor must, since the anchor lies there; the five planted readings share
exactly that 204-cell list. The anchored tables enumerate exactly the
sixteen-piece subsets that hold the anchor, checked row for row against
direct column sums with binomial row counts.

Control at twelve: across 371 splits the anchored search returns no set for
any charge, reproducing the earlier complete result that twelve is empty.
The measurement at sixteen: across 2004 splits, all distinct, with every
anchored licensed cell covered for all eleven live readings, the search
returns 11 anchored sets for the four reading, none for the other five
charges, and none for the synthetic odd-total reading, and it finds all five
planted sixteen-piece controls, returning 2, 6, 12, 1 and 3 sets against the
five planted readings, in each case including the planted set itself.

## The census and its folds

Every set recorded by the search holds the anchor piece, and the anchored
members of the reconstructed census are exactly the recorded slice, so the
slice is stable under the group. Each of the 132 census members is
re-verified directly against the incidence columns as a sixteen-piece carrier
of the four reading, and all 132 are pairwise distinct.

The census is a union of whole orbits under the 48 and under the full group.
Under the 48 it folds into 15 orbits: ten of size 6, four of size 12, one of
size 24. Under the full group of order 384 it folds into 6 orbits: three of
size 12, two of size 24, one of size 48. Even the full group needs 6 orbits
to cover the carriers, and no orbit reaches the group order, so every carrier
has a nontrivial stabilizer in the full group.

## The other five charges

The anchored slices of the five other charge readings are empty at sixteen,
so by the completeness of the anchored slice their full sixteen census is
empty. Forced parity keeps every carrier size even, so the least open size
for each of the five rises to eighteen. The four reading attains sixteen,
consistent with the landed floor.

## Boundary and honest read

- Completeness of the census rests only on measured facts gated in this
  runner: the fifty generators carry cuttings to cuttings, fix the charge
  readings, and act on the pieces with a single orbit. It does not rest on
  any claim that the group of order 384 is the full symmetry group of the
  system; that certification is the previous cycle's business and is not
  relied on here. A symmetry beyond the group, if any existed, could not add
  members to a complete census.
- The count 132 and the folds are statements about the finite cutting system
  only. No physical reading of the orbit structure is claimed here.
- The open witness minima on other readings recorded in earlier cycles remain
  open and are untouched by this cycle.
- The five planted controls are seeded constructions whose profiles are fixed
  in the runner source; they exist to prove the anchored search cannot miss a
  planted answer, and each is found.
- Earlier-cycle artifacts are named in backticks because their packages are
  in flight, and nothing here links to them:
  `PHYSICAL_CELL_CUTTING_FOURTEEN_FRONTIER_CYCLE741_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_SIXTEEN_ATTAINED_CYCLE742_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_HIDDEN_THREE_BIT_GEOMETRY_CYCLE743_NOTE_2026-08-05.md`,
  `PHYSICAL_CELL_CUTTING_FULL_SYMMETRY_CERTIFIED_CYCLE744_NOTE_2026-08-05.md`.
