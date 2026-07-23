# Abstract fill-disk full-tableau isometry — Cycle 643

Classification: **positive literal abstract Cycle537 Clifford isometry; physical 3D placement and autonomous genesis remain separate and unclaimed**

Authority: **none**

Audit: **unset**

Author artifact status accepted: **false**

Breakthrough bar met: **false**

## Result up front

Cycle 643 closes Cycle537's state-preparation/isometry omission on the exact
**abstract enlarged fill-disk code**.  It does not consume Cycle642 or any
dirty Cycle532/Cycle537 bytes.  The runner loads the committed source blobs at
`c27f72ff8b1058d872695829c05e95da415813bc`, verifies all nine shore hashes, and synthesizes an exact
Clifford isometry

```text
E : (C^2)^(6N target) tensor (C^2)^(N-1 gauge)
    tensor |0>^(rank S_fill)  ->  H_fill
```

from only `H`, `S`, and `CNOT`.  Work M2 count is zero.  Every factor has
support at most two in the abstract cap adjacency/factor grammar.  The full
factor lists are materialized, iterated, and hashed at all three sizes:

| size | split | physical M2 | target | gauge | blank stabilizer M2 | factors | factors/cell | H / S / CNOT |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| L3 | construction | 630 | 162 | 26 | 442 | 19414 | 719.037 | 4309 / 5922 / 9183 |
| L6 | train | 4932 | 1296 | 215 | 3421 | 218515 | 1011.644 | 43631 / 44319 / 130565 |
| L7 | held-out-no-refit | 7798 | 2058 | 342 | 5398 | 394819 | 1151.076 | 76137 / 69285 / 249397 |

The held L7 list is fully materialized, not replaced by a symbolic recurrence.
Its `394819` factors have digest
`8ecfcae8378294fd9625e725d191eb7138e91aec0b70f74fde2661cfd6be550f`.

The observed factor counts per cell are
`719.037`,
`1011.644`, and
`1151.076`.  They increase across the tested
sizes.  Generic Gaussian elimination supplies no all-L linear-size,
constant-factors-per-cell, or bounded-depth theorem.  The spatial M2 count per
cell is bounded on the declared finite rows; factor/program scaling is not
established, and held L7 is not asymptotic locality evidence.

## Physical-distance audit

Support arity and physical range are kept separate.  For CNOT endpoints that
both lie on the committed Cycle532 rough graph, the runner computes exact
edge-line distance.  Any factor touching an added cap-sheet M2 is counted as
**unplaced** because no Cycle642 embedding is admitted; it is not assigned a
fake distance.

| size | two-qubit factors | rough/rough measured | cap-unplaced | distance 1 | distance >1 | max | p50/p90/p99 |
|---|---:|---:|---:|---:|---:|---:|---|
| L3 | 9183 | 8234 | 949 | 1414 | 6820 | 8 | [4, 6, 8] |
| L6 | 130565 | 125965 | 4600 | 12305 | 113660 | 20 | [7, 12, 16] |
| L7 | 249397 | 242812 | 6585 | 19761 | 223051 | 20 | [8, 14, 18] |

Thus the emitted list is explicitly nonlocal in the committed rough-graph
metric and partly unplaced.  Cycle643 certifies exact abstract factor arity,
not bounded physical 3D locality.

## Literal synthesis grammar

The decoder first selects an independent signed basis of every Cycle537 local
and fill stabilizer.  Deterministic Pauli-column elimination uses `H` to swap
X/Z, `S` to clear Y, and `CNOT` to clear remote support.  Row multiplication
is only a classical synthesis operation: the emitted quantum factor list
contains no row-operation oracle.  Each selected stabilizer becomes one exact
`+Z` reference pivot.  Every dependent displayed stabilizer is then run
through the complete circuit and checked to be a phase-zero product of those
reference `Z`s.

On the remaining `7N-1` wires, symplectic Gram-Schmidt gives `6N-1` matter
pairs, `N-1` gauge pairs, and the common matter/gauge parity radical.  One
explicit supplied parity conjugate completes the 6N-qubit full-Fock target
chart.  A second H/S/CNOT elimination maps that complete frame to input
coordinates.  Reversing the total decoder—with `S^-1 = S S S`—is the literal
encoder `E`.

This charges the pivot/root, row and factor order, parity-conjugate selector,
blank `+Z` stabilizer state, optional gauge-vacuum reference, and compile
schedule.  None is hidden as a dynamical law.

## Complete stabilizer, matter, gauge, and parity certificate

At L3/L6/L7 the exact code dimensions are respectively `188`, `1511`, and
`2400`, equal to `6N + (N-1)` in every row.  The circuit conjugates
`687` /
`5367` /
`8487` displayed stabilizers,
with zero plus-reference failures.  It also conjugates all
`567` /
`4536` /
`7203` matter generators and
`108` /
`864` /
`1372` explicit gauge generators.
Matter-to-gauge, gauge-partition, and ancilla-X leakage failures are all zero.

The matter and gauge parity rows decode to the same target parity coordinate.
The final target parity input may be zero or one, so both matter parities are
in the isometry domain.  A physical generator may retain a product of blank
ancilla `Z`s; this is enumerated explicitly and acts as identity on the
declared input code.  Thus conjugation is exact on the declared code space,
not an equality silently extended off code.

## Two elimination orders

Forward low-pivot and reverse high-pivot synthesis at L3 give different
factor lists: `19414` versus
`16441` factors and distinct digests.  Nevertheless
they give the same signed stabilizer code and identical complete matter/gauge
symplectic coordinates.  The runner solves one Pauli sign-frame correction
with target/gauge supports `117` /
`18`.  The only freedom in the odd
parity conjugate is multiplication by target parity.  Hence the two circuits
are equivalent modulo stabilizer and target/gauge chart, and elimination
order is not promoted to a preferred physical ordering.

## Inverse, deletion, malformed, and gauge-vacuum controls

The complete L3 `2n` canonical Pauli basis and deterministic L6/L7 held
samples round-trip through `E` and its decoder with zero failures; factorwise
inverse rules prove the remaining basis rows identically.  There are no work
M2s, so returned blank work is exact rather than postselected.

Deleting representative `H`, `S`, or `CNOT` factors is detected by stabilizer
or complete-generator failures.  Deleting one independent stabilizer lowers
rank `442 ->
441`.  Flipping one displayed
stabilizer sign produces `15`
phase inconsistencies and decodes to a minus reference.

The `N-1` gauge wires are arbitrary inputs in the full isometry.  For the
optional supplied plus gauge-vacuum fixture, L3 adds exactly
`26` independent `+Z` references; deleting
one lowers rank by one.  A minus gauge reference is algebraically consistent
but refused by that declared plus fixture.  This is a fixture check, not a
claim that gauge-vacuum genesis is derived.

## Full-Fock update composition

On the declared abstract code space the complete generator conjugation and
polynomial homomorphism give

```text
E G_coarse = G_abstract E.
```

This covers the inherited coin/onsite, FSWAP, contact, and B/Gamma(P) blocks.
The exact inherited controls retain onsite residual
`5.272e-15`, FSWAP matrix residual
`0.0e+00`, zero B coefficient failures,
Cycle219 mass residual `2.220e-16`, contact
deletion residual `0.367893067056082`, and Cycle230
seam `6` PASS / `0` FAIL.
This is `G_abstract` on Cycle537's cap code, not a Cycle642 physical update.

## Proper-cubic presentation covariance

The L3 construction, L6 train, and held L7 presentations each close under all
24 proper-cubic frames and all 576 products with zero label failures.  For a
frame `R`, the compile-time family is `E_R = F_R E C_R^dagger`.  This is the
same frame-specific retriangulated **abstract cap presentation** discipline as
Cycle537.  It is not one fixed cap embedding in ordinary 3D physical distance,
not a runtime frame selector, and not an autonomous schedule.

## Supplied, derived, and open

Supplied: committed Cycle532/Cycle537 algebra and inherited update fixtures;
three abstract fill disks and their adjacency; finite L3/L6/L7 domains;
pivot/root and row order; parity-conjugate selector; target/gauge input chart;
blank stabilizer state; optional gauge-vacuum reference; factor schedule; and
compile-time frame presentation.

Derived: complete factor lists; exact stabilizer `+Z` reduction; exact
`6N + N-1` logical chart; all displayed matter/gauge generator coordinates;
both matter parities; inverse and zero returned work; deletion/malformed
controls; two-order equivalence; abstract all24/all576; and generator/algebra
composition with the inherited full-Fock update.

Open and not tested: bounded-distance placement of these factors in a single
physical 3D M2 embedding; routing and returned routing work there; autonomous
blank/gauge-reference/pivot/root/order/schedule genesis; infinite-volume and
noise controls; and any time, Record, Born, gravity, or source interpretation.

Abstract support-two is not physical 3D locality.  A compiler factor count is
not time or a rate.  A blank stabilizer or gauge reference is not autonomous
genesis.  No phase is called energy and no gauge capacity is called source.

## N1-N8 scope discipline

N1 records five normalized ATTEMPTED families and lists the untested
physical-routing and autonomous-genesis families separately, without honesty
markers and without counting them as failures.  N2 retains the
two distinct open conditions and both directions.  N3 exposes every supplied
selector, reference, order, topology, and schedule.  N4 matches Cycle537 and
Cycle636 exactly, drops Cycle539's different patch residual, and never consumes
Cycle642.  N5 audits the
three negative boundary phrases at five resolutions.  N6 lists five concrete
partial-closure paths.  N7 gives the physical-routing/state-carried steelman.
N8 records five cross-cycle echoes.

Broad no-go: **not claimed**.  Minimum content: **not claimed**.  Shared
route-independent obstruction: **not established**.  Axiom pressure:
**none**.  The N1-N8 scope status is **PASS**; the broad-no-go,
minimum-content, shared-obstruction, and axiom-pressure promotion gates are all
**FAIL / DO NOT SHIP**.

## Six-wall ledger and terminal

| wall | Cycle643 movement | residual |
|---|---|---|
| `C_ref` | literal full E, both parities, inverse, two-order equivalence | pivot/root/chart/blank/gauge reference and schedule supplied |
| `C_num` | exact target-times-gauge dimensions and complete generator tables | no empirical unit; factor counts are not time/rates |
| `C_wrap` | every stabilizer is locally named in the abstract cap and inverse-visible | physical embedding, autonomous renewal, Records/history open |
| `C_int` | inherited coin/FSWAP/contact/B, mass and seam compose through E | no new physical interaction law; Cycle642 not consumed |
| `C_local` | every factor support <=2; abstract all24/all576 | bounded physical 3D distance/routing untested |
| `C_source` | all blank/gauge/work/schedule resources explicit; work=0 | no source/stress/gravity meaning or autonomous resource genesis |

Strongest honest terminal: a complete literal H/S/CNOT isometry for the exact
abstract Cycle537 fill-disk code at L3/L6/L7, with full generator/algebra
intertwining.  It is not yet a physical 3D M2 compiler.
