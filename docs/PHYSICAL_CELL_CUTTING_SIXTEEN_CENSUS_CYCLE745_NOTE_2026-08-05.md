# Bounded sixteen-piece census for the supplied cutting system — Cycle 745

Date: 2026-08-05

Authority: none

Audit: unset.

Status: proposed_retained

Claim type: bounded_theorem

Runner:

- [primary rebuild-and-gate runner](../scripts/physical_cell_cutting_sixteen_census_cycle745_2026_08_05.py)
- [independent opposite-pivot/CNF checker](../scripts/physical_cell_cutting_sixteen_census_cycle745_independent_check_2026_08_05.py)

Scope: exact finite identities of the supplied cutting system. The primary
rebuilds the cell complex, cuttings, named algebraic readings, symmetries and
anchored tables. The independent checker reconstructs the incidence table with
the opposite exact-cover pivot, verifies the group action semantically, and
uses an orthogonal exact-cardinality CNF search. Constitutional effect: none.
This package changes no axiom, no framework Admissibility rule, no primitive,
no policy, and no audit status, and it adds no import and no assumption to
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## Headline

The sixteen-piece carriers of the six named nonconstant algebraic readings are completely
enumerated. The four reading carries exactly 132 sixteen-piece sets and no
others in this supplied finite system, reconstructed as the group images of an 11-member anchored slice and
re-verified one by one directly against the incidence columns. The other five
readings carry none at size 16. Together with the complete Cycle 741 search
through size 14 and the exact even-parity restriction, this makes 18 the next
unsearched size; no size-18 witness or attainment is claimed. Under the 48 cutting symmetries the
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

Every element of that group carries cuttings to cuttings and fixes each named
algebraic reading, so it maps sixteen-piece carriers of a reading to
sixteen-piece carriers of the same reading. The group is transitive on the pieces, so every
carrier has at least one group image holding the chosen anchor piece. The
anchored slice — the carriers through the anchor — therefore meets every
group orbit of carriers, and the full census is recovered as the set of all
group images of the slice. Two measured facts pin the arithmetic: each of the
192 pieces lies in the same number of census sets as the anchor, and the
census holds exactly twelve sets for each anchored one.

## The anchored search

Parity licensing leaves the same cell list for every named nonconstant reading:
the licensed cells of such a reading number 5, 14, 30, 55, 91, 140, 204 and
285 at the even sizes two to sixteen, the steps being consecutive odd squares,
and all six readings license the same 285 cells at sixteen in one shared pass. Of those
285 cells, 204 hold a piece in the last quarter — and a subset through the
anchor must, since the anchor lies there; the five planted readings share
exactly that 204-cell list. The anchored tables enumerate exactly the
sixteen-piece subsets that hold the anchor, checked row for row against
direct column sums with binomial row counts.

Control at twelve: across 371 splits the anchored search returns no set for
any of the six named readings, reproducing the earlier complete result that twelve is empty.
The measurement at sixteen: across 2004 splits, all distinct, with every
anchored licensed cell covered for all eleven realizable live readings, the search
returns 11 anchored sets for the four reading, none for the other five
readings, and it finds all five
planted sixteen-piece controls, returning 2, 6, 12, 1 and 3 sets against the
five planted readings, in each case including the planted set itself.
The separately named `odd-ctl` target is the canonical one-row inconsistent
hostile control: augmented rank rejects it before carrier licensing or search,
so no carrier count is inferred for a target outside the column space.

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

## The other five named readings

The anchored slices of the five other named algebraic readings are empty at sixteen,
so by the completeness of the anchored slice their full sixteen census is
empty. [Cycle 741](PHYSICAL_CELL_CUTTING_FOURTEEN_FRONTIER_CYCLE741_NOTE_2026-08-05.md)
independently closes all allowed even sizes through 14, and forced parity keeps
every carrier size even, so 18 is the next unsearched size for each of the five.
The four reading attains 16. This is a lower-bound statement, not a size-18
attainment claim.

## Boundary and honest read

- Completeness of the census rests only on measured facts gated in this
  runner: the fifty generators carry cuttings to cuttings, fix the named algebraic
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
- The exact incidence ordering and eight algebraic reading identities are
  content-bound to [Cycle 737](PHYSICAL_CELL_CUTTING_LEAST_COMPUTING_SETS_CYCLE737_NOTE_2026-08-05.md).
  The complete through-14 lower bound is content-bound to
  [Cycle 741](PHYSICAL_CELL_CUTTING_FOURTEEN_FRONTIER_CYCLE741_NOTE_2026-08-05.md).
  Cycles 742--744 are historical ordering context only: this package rebuilds
  and semantically verifies the transitive group it actually uses and imports
  no full-automorphism classification.
- Nothing here selects these algebraic functions as physical charges, extends
  the result to another incidence table or column order, or proves a multicell,
  arbitrary-size, continuum, dynamical, or framework-level statement.

## No-Go Discipline for the five size-16 empty censuses

The negative claim is deliberately narrow: on this exact 15800-by-192 supplied
incidence table, the five names `four-flip`, `six`, `six-flip`, `seven`, and
`seven-flip` have no exact weight-16 carrier. The claim is not that these
functions never occur, nor that weight 18 is empty.

### N1 — alternative routes

| Route | Test and result | Marker |
|---|---|---|
| Primary anchored syndrome join | Exhaust all 204 licensed anchor cells and the independently generated 2004-split inventory; all five counts are zero. | ATTEMPTED |
| Independent exact-cardinality CNF | Rebuild the incidence table with the opposite exact-cover pivot and solve each anchored weight-16 system with a separate CNF encoding; all five are UNSAT. | ATTEMPTED |
| Escape outside the anchored slice | Verify every generator is an incidence automorphism fixing each named reading, close the group to order 384, and verify the anchor orbit has all 192 columns; every nonempty carrier therefore has an anchored image. | ATTEMPTED |
| Omitted or redirected primary split | Delete one scheduled split and redirect one part; each hostile inventory differs from the mathematical 2004-split inventory and fails closed. | ATTEMPTED |
| Wrong reading or traversal order | Bind canonical row-with-bit hashes and reconstruct every realizable target from a support witness; define the odd rejector on the lexicographically least packed row. | ATTEMPTED |
| Lower weight hidden below 16 | Bind the primary and independent Cycle 741 receipts that exhaust every allowed even size through 14; parity excludes odd sizes. | RULED OUT BY PRIOR — [Cycle 741](PHYSICAL_CELL_CUTTING_FOURTEEN_FRONTIER_CYCLE741_NOTE_2026-08-05.md) |

### N2 — wall independence

There is one finite wall, not several: existence of a weight-16 solution to
the exact incidence equation for each named right-hand side. The anchored
search and transitive action are two obligations in one completeness proof;
neither is presented as an independent physical wall. The separate
through-14 predecessor is used only for the lower-bound corollary, not for
size-16 emptiness.

### N3 — hidden-wall scan

“By construction” is restricted to the five explicitly seeded controls.
“Framework provides,” “standard,” “canonical charge,” and physical bridge
language are not used as proof steps. Load-bearing conditions are explicit:
the supplied incidence bytes and column order, the six named algebraic
right-hand sides, the exact group generators, the chosen anchor, and the
Cycle 741 lower-size receipt.

### N4 — residual matching

| Citation | Witness residual | Residual used here | Match |
|---|---|---|---|
| [Cycle 737](PHYSICAL_CELL_CUTTING_LEAST_COMPUTING_SETS_CYCLE737_NOTE_2026-08-05.md) | Exact supplied incidence/order and eight function identities | Identity of the finite system and six searched functions | yes |
| [Cycle 741](PHYSICAL_CELL_CUTTING_FOURTEEN_FRONTIER_CYCLE741_NOTE_2026-08-05.md) | No carrier for the six nonconstant readings at allowed sizes through 14 | Exclusion below 16 in the lower-bound corollary | yes |

### N5 — rhetoric audit

- Per element: tested; every one of the 192 supplied columns is eligible.
- Per site: tested only for the one supplied 16-corner coordinate cell.
- Per mode: not applicable; no modal object is defined.
- Per block: tested against all 15800 supplied cutting rows.
- Lattice-wide: not tested and not claimed.

Both runners print these five resolution lines in their execution evidence.

### N6 — partial-closure scan

The residual does not require a new axiom or primitive. Weight 18 is a finite
next search on the same incidence object; alternative readings and other
incidence systems are separate finite inputs. The note therefore reports the
exact size-16 wall and leaves size 18 open without calling it structural.

### N7 — steelman

A hostile reviewer should object that an anchored solver can return zero
while silently omitting a licensed split, or that an alleged symmetry can
move columns without preserving cuttings or the target. That would destroy
the global negative conclusion. The repair answers this concrete attack twice:
the primary pins its exact 2004-split schedule, while the checker uses no such
schedule at all, verifies every group generator semantically on the rebuilt
incidence/targets, and solves the anchored equations through independent CNF.

### N8 — cross-cycle echo

Cycles 738 and 741 contain similar exact finite emptiness claims. Their lesson
is procedural, not a transitive theorem: a finite negative needs an independent
search, exact target identity, complete execution inventory, and explicit open
next size. No claim from those cycles is echoed into another incidence system,
arbitrary support size, or physical no-go.
