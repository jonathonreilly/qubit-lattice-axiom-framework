# Minimum supports for finite binary readings of supplied one-cell cuttings — Cycle 737

Date: 2026-08-05

Claim type: bounded_theorem

Status: unaudited source note

Audit authority: none; audit status belongs only to the independent audit lane.

## Supplied model and premise boundary

This theorem concerns one supplied finite object. The object is the unit four-cube
`{0,1}^4`, with three coordinates labelled spatial and one labelled tick, cut into 24
normalized-volume-one five-corner simplices. The declared piece cost counts corner pairs
whose full four-coordinate `L1` separation exceeds one. The carried action consists of
24 proper spatial signed permutations with the optional labelled tick flip.

The [Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md) supply only the spatial `Z^3`
nearest-neighbour lattice and proper cubic rotations. The registered
[kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) supplies only
equal spatial/tick kinetic-form graining. Neither source selects this four-cube, simplex
class, cost, dissection rule, binary reading, physical assembly cell, or
tick–Admissibility realization.

[Cycle 736](PHYSICAL_CELL_CUTTING_CHARGE_SPACE_CYCLE736_NOTE_2026-08-05.md) is the direct
scientific dependency. Its hash-bound receipt supplies the same finite population and the
complete rank-three space of eight induced GF(2) functions: two constants and three
nonconstant complement pairs. The present primary and independent checker also reconstruct
the population and functions locally. Cycles 734 and 735 are chronological context only;
no count, certificate, witness, or receipt from them is consumed directly here.

The words “support” and “reading” below are deliberately finite. The support universe is
exactly the 192 pieces that occur in at least one of the 15,800 supplied cuttings. A piece
outside that universe has an identically zero incidence column and is not counted as a
support coordinate. The six nonconstant functions are not identified with physical
charges, observables, conserved quantities, or Record content.

## Exact theorem

Let `A` be the `15800 × 192` binary incidence matrix whose row records the pieces in one
cutting. For a support `S` among the 192 used pieces, its reading is `A 1_S` over
`GF(2)`. A support computes a named function `f` exactly when

`A 1_S = f`.

The exact finite results are:

- every used piece occurs in exactly 1,975 cuttings, and `rank_GF(2)(A)=88`;
- each of the eight Cycle-736 functions has an even number of ones, so every support
  computing one of them has even cardinality;
- the empty support computes constant zero; the smallest **nonempty** constant-zero
  supports have cardinality eight, and there are exactly 648;
- the smallest supports computing constant one have cardinality eight, and there are
  exactly 192;
- none of the six nonconstant readings has a support of cardinality at most eight;
  therefore every such support has cardinality at least ten;
- explicit supports of sizes 16, 20, 24, 24, 30, and 30 compute, respectively, the
  functions labelled `four`, `four_flip`, `six`, `six_flip`, `seven`, and
  `seven_flip`.

The last line is only a verified upper bound. Those witnesses were found by a seeded search
outside the proof runner. Nothing here proves their optimality or even tests cardinality
ten and above.

## Geometric population and direct dependency

There are 4,368 five-corner subsets of the 16 corners and 2,672 have normalized volume one.
The declared cost has floor six on 400 of them. The exact-cover reconstruction returns
15,800 covers of 24 floor pieces, using 192 pieces. All 15,168 piece pairs that co-occur in
a returned cover have an exact integer separating plane. Because the 24 normalized unit
volumes sum to the four-cube volume, the returned objects are genuine geometric
dissections, not merely sample-mask covers.

The Cycle-736 receipt is accepted only when its schema, pass status, zero failure count,
15,800 geometric cuttings, 192 used pieces, eight induced readings, rank three, and two
constants all match. The local reconstruction also checks the three nonconstant split
sizes `5664/10136`, `7704/8096`, and `7424/8376`.

## Parity and exhaustive support search

Summing all rows of `A` gives the all-ones vector because every column sum is 1,975. Thus

`|S| mod 2 = sum_i f_i mod 2`.

Every one of the eight target functions has even Hamming weight, so odd support sizes are
excluded exactly.

For even cardinalities two, four, six, and eight, the primary search compresses `A` to
88 independent rows and represents each column by its exact 88-bit syndrome. A row-space
certificate fixes even overlap with a declared 96-column half for all eight readings.
The search then exhausts every allowed half split:

- stored-table meets for light/light splits;
- streamed heavy/light meets for six-plus-zero and six-plus-two splits; and
- a complete two-quarter sweep for supports lying wholly inside one half, including the
  odd quarter splits that the half certificate does not eliminate.

Every returned support is re-evaluated on all 15,800 incidence rows, and duplicate-freedom
across search routes is checked. Four planted controls exercise the pair, heavy/light,
odd-quarter, and single-quarter paths. A synthetic target with forced odd half parity
confirms that the licensing test can reject a target rather than always returning “even.”

The independent checker imports and executes no primary implementation. It uses a Leibniz
determinant instead of the primary minor formula, the largest uncovered sample point
instead of the smallest in exact-cover recursion (496,849 nodes rather than 502,838), and
reversed traversal within both support halves. It independently reconstructs the same
population, geometric separation, readings, 648/192 octet families, empty nonconstant
search through eight, and all upper witnesses.

## The two octet families

The 648 minimum nonempty constant-zero supports form 22 orbits under the declared
48-element action: 17 of size 24 and five of size 48. The 192 minimum constant-one supports
form five orbits of sizes `24,24,48,48,48`. Each family is closed under the action and,
as a family, touches every one of the 192 support coordinates. This does not say that one
octet is itself a union of complete piece orbits.

The eight simplices in every octet share exactly two cell corners. For the constant-one
octets that pair is always one of the 32 cell edges; each edge supports exactly six
octets, and every octet collectively touches all 16 corners.

For the constant-zero octets every one of the 120 corner pairs occurs. Pairs at Hamming
distances one, two, three, and four occur with multiplicities nine, three, three, and
fifteen per pair. Their union contains 10, 12, or 16 corners in 240, 120, and 288 cases.

The 120 four-piece exchange masks from the finite move graph are disjoint from the 648
constant-zero octets. No declared 48-piece orbit indicator lies in the row space of
`A`, so orbit-parity is not fixed across all supports of a target. These are exact
linear-incidence facts, not physical locality or dynamics.

## Independent and hostile checks

Both runners reconstruct rather than merely trust the submitted transcript. The primary
has exact full-table verification, exact geometry, planted-route recovery, an odd-license
control, and dependency-schema checks. It also rejects a one-piece deletion from a
constant-zero octet, proves that a failed Cycle-736 receipt cannot satisfy the dependency
predicate, and exhibits sample-disjoint pieces that overlap so the geometric separator
gate is load-bearing.

The independent checker repeats the result with the alternate determinant, exact-cover
pivot, and traversal. Each runner is fail-closed, emits a generated receipt, and is bound
to the complete declared source closure by its canonical cache.

## Claim boundary

What is proved is exact finite coding and geometry for the declared 192-column incidence
system and the eight supplied Cycle-736 readings.

What is not proved:

- the exact minimum support above the lower bound ten for any nonconstant reading;
- a result for a different binary function, support universe, coefficient field,
  nonlinear readout, piece class, cost, action, or dissection population;
- physical selection of the cell, tick, simplex class, cost, reading, or support;
- a physical observable, conservation law, local process, memory mechanism, or Record
  interpretation;
- a multi-cell, arbitrary-extent, arbitrary-`L`, boundary, thermodynamic, continuum, or
  gravity statement.

Proof-obligation disposition: **CONDITIONAL**. The finite coding and geometry theorem is
closed on the supplied model. Any physical reading remains conditional on the explicitly
open selection and realization bridges above.

## No-Go Discipline Gate

Negative assertion class: `derived_no_go_boundary`. The only exact negative shipped is
that no support of cardinality at most eight computes any of the six fixed nonconstant
readings in this fixed 192-column finite system.

**N1 — alternative-route enumeration.** Six materially distinct attacks are executed.

1. `ATTEMPTED` — parity attack: derive the total support parity from all 15,800 rows and
   try every odd cardinality; the target weights force even support.
2. `ATTEMPTED` — light/light collision attack: reduce to 88 independent rows and join
   stored syndrome tables for every half split whose two sides have weight at most four.
3. `ATTEMPTED` — heavy/light streaming attack: generate each six-piece heavy support
   uniquely by prefix plus lexicographic tail and match it against the light-side table.
4. `ATTEMPTED` — unlicensed-quarter attack: explicitly sweep every quarter split for
   supports wholly inside one half, including the odd quarter splits that no license
   eliminates.
5. `ATTEMPTED` — independent-population/traversal attack: rebuild the 15,800 geometric
   rows using the opposite exact-cover pivot and repeat the support joins with both halves
   traversed in reverse.
6. `ATTEMPTED` — full-table falsification attack: evaluate every returned support on all
   15,800 rows and mutate a valid octet by one deletion; the mutation fails.

**N2 — wall-independence audit.** The raw population, used-piece universe, and six target
functions are not counted separately: the used universe and targets are defined from the
declared finite data, so they collapse into D (the supplied finite data). The remaining
collapsed walls are C (binary additive-incidence readout), H (the cardinality window
through eight), and X (physical or multi-cell extension).

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| D–C | no | no | yes |
| D–H | no | no | yes |
| D–X | no | no | yes |
| C–H | no | no | yes |
| C–X | no | no | yes |
| H–X | no | no | yes |

The finite theorem closes H only for D/C as declared. It closes none of the other
walls and does not inflate them into a universal obstruction.

**N3 — hidden-wall scan.** The scan covers “assume,” “by construction,” “framework
provides,” “naturally,” “canonical,” “physical,” “all,” and “no.” The cell, cost, piece
class, support universe, target functions, coefficient field, additivity, exact-cover
predicate, acting group, and cardinality window are explicit. “Canonical cache” is
non-load-bearing evidence packaging. No hidden model choice is promoted to an axiom.

**N4 — residual matching.** Cycle 736 is cited only for the exact same supplied geometric
population and eight induced functions, which the local runners reconstruct and compare.
No previous negative or wall is used to prove the support lower bound. Cycles 734 and 735
are context only, so no mismatched residual is inherited.

**N5 — rhetoric audit.** The primary canonical cache lands five resolution lines.
Per-element resolves all 192 used columns; per-site resolves one supplied coordinate cell;
per-mode is not executed because there is no spectral or field-mode object; per-block
resolves all 15,800 rows and every support through size eight; lattice-wide is not
executed and no lattice-wide negative is asserted.

**N6 — partial-closure paths.** Sizes ten and above can be enumerated in the same finite
system without a new axiom. Other targets, coefficient fields, and nonlinear readouts can
be posed as separate finite problems. A physical or multi-cell interpretation needs an
explicit supplied bridge and its own theorem. These routes remain open extensions.

**N7 — steelman.** A hostile reviewer should expect supports at cardinality ten or twelve,
because the proof deliberately stops at eight and already exhibits larger witnesses.
They should also expect a different target, larger support universe, or nonlinear rule to
change the minimum. That is a concrete attack on any broader claim, which is why no exact
minimum, universal coding bound, physical obstruction, or lattice-wide statement ships.
It does not challenge the completed finite search through eight.

**N8 — cross-cycle echo.** Cycle 734 showed that pairwise co-occurrence cliques need not be
genuine shared-cutting triples, and Cycle 735 showed that whole-component cube dimension
need not bound embedded cube dimension. The present proof therefore distinguishes sample
cover from geometry, checks the full row table after syndrome compression, and states only
the searched cardinality window. No broader negative is inferred from a compressed proxy.

**Status: PASS.** All N1–N8 items land with the note, the five N5 resolution lines land in
the primary canonical cache, and the negative remains confined to the exact finite window.

## Artifacts

- Primary runner:
  [`scripts/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.py`](../scripts/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.py)
- Independent checker:
  [`scripts/physical_cell_cutting_least_computing_sets_cycle737_independent_check_2026_08_05.py`](../scripts/physical_cell_cutting_least_computing_sets_cycle737_independent_check_2026_08_05.py)
- Primary cache:
  [`logs/runner-cache/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.txt`](../logs/runner-cache/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05.txt)
- Independent cache:
  [`logs/runner-cache/physical_cell_cutting_least_computing_sets_cycle737_independent_check_2026_08_05.txt`](../logs/runner-cache/physical_cell_cutting_least_computing_sets_cycle737_independent_check_2026_08_05.txt)
- Primary receipt:
  [`outputs/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05_receipt_2026-08-05.json`](../outputs/physical_cell_cutting_least_computing_sets_cycle737_2026_08_05_receipt_2026-08-05.json)
- Independent receipt:
  [`outputs/physical_cell_cutting_least_computing_sets_cycle737_independent_check_2026_08_05_receipt_2026-08-05.json`](../outputs/physical_cell_cutting_least_computing_sets_cycle737_independent_check_2026_08_05_receipt_2026-08-05.json)

## Review-loop record

On 2026-08-12 review corrected the submitted premise and theorem boundary: the model is
supplied rather than axiom-derived; “physical charges” became finite binary readings; the
support universe became explicitly the 192 used pieces; and the constant-zero statement
became the minimum **nonempty** kernel support. Review also added the direct Cycle-736
binding, exact geometric separation, an independent checker, fail-closed receipts and
canonical caches, hostile controls, and the landed N1–N8/N5 packet. This is review
provenance, not an audit verdict.
