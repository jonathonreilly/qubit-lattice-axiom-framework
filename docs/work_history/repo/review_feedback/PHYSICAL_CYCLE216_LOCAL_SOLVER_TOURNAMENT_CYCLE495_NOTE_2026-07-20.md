# Physical Cycle216 local-solver tournament — Cycle 495

Date: 2026-07-20
Authority: none
Audit: unset

This note was frozen before Cycle495 target outputs.  It asks whether the
held-clean Cycle216 scalar identity `K+ = 3 L+` can be prepared by bounded
local physical operations and handed to the already frozen Cycle491 M64
receiver without another amplitude fit.  A response profile is not gravity,
an iteration depth is not time, a spectral phase is not energy or a rate,
word occupancy is not a Record, and norm weight is not probability.

## Frozen tournament

The domain is the periodic L13 cube.  Training is Cycle453's a1 geometry and
held is its a2 geometry.  Both use the exact signed (+1,-2,+1) scalar source
payload extracted from the Cycle490 word256 source column, four receiver
updates, both physical occupations, and all four absolute packet rows.  The
held rows never refit.  A single train-only common scale is

`min(1, sqrt(train compiled-field weight / maximum train raw-route weight))`.

It is selected only from the three train columns, never from a packet target,
and is reused unchanged for held.  Missing column norm is completed in one
ordinary reservoir M2 at cell (10,10,10), not a negative logical key.  The
completion channel is outside every declared source/receiver vertex and is
therefore source-vertex/field-stream inert, but the receiver matter factors
act globally on its carried matrix block.  It supplies a free/uncoupled,
load-bearing receiver contribution; it is not called inert during the M64
join.  Geometry order means
that each held a2 width shift is strictly larger than the corresponding train
a1 shift.

### A — retained divide-six / Jacobi adapter

Run exactly 96 synchronous layers of

`x_(n+1)(r) = (sum_{six neighbours} x_n + 3 rho(r))/6`

from zero.  This is Cycle479's local law adapted from a finite Dirichlet bulk
to the periodic zero-sum L13 quadrupole.  Before the Cycle216 factor 3, the
signed source has four unit occurrences (+,+,-,-), with the middle -2 encoded
as two negative occurrences.  Multiplying by 3 therefore requires twelve
unit-weight unsigned Cycle467 compiler instances: six positive and six
negative, compressed in the runner by linearity to the three spatial word
histories with decoded multiplicities (+3,-6,+3).  Exact word checks use
D=6^96; every unsigned instance is exactly divisible through all 96 layers,
and their decoded difference is the signed response.  The retained Cycle467
divider is tested on actual nonnegative numerators.  It is not silently
claimed to accept signed words or matrix-valued source payloads.

Cycle474's mod-3 schedule is not valid unchanged across an odd L13 wrap.
Cycle495 therefore freezes a double-buffered 5x5x5 colour schedule: 125
rounds per layer, one update per cell per layer, old slice read-only and new
slice write-only.  Equal-colour radius-one stars are disjoint on C13; round
order cannot change a synchronous layer.  Its one-axis word is
`(0,3,1,0,2,1,3,4,1,2,0,1,4)` and reversal acts by the exact colour
permutation `(0,1,2,4,3)`.  Coordinate signed permutations therefore map
each complete colour class to exactly one complete colour class in all 24
proper-cubic frames.  This is a bounded schedule
adapter.  A literal source-payload preparation/interference circuit from the
Cycle490 M2 column into the four retained unsigned word compilers remains
open, so this route may be an exact bounded adapter without being a completed
physical recurrent solver.

The domain/interface map is explicit.  Cycle479's 15^3 box, exterior trace,
Dirichlet bulk, boundary-drive matrix, and Schur complement are not imported
as the Cycle216 solver.  Only its six-neighbour divide-six local law and the
frozen Cycle467/470 arithmetic/delivery identities are retained.  Cycle495
replaces the domain by all 13^3 periodic cells, replaces boundary drive by the
three internal Cycle453 source cells, and replaces the finite-box schedule by
the 125-colour double-buffer schedule.  The (+1,-2,+1) source has exactly zero
sum; zero initial words and every synchronous Jacobi layer therefore remain
mean-zero.  Comparison is only to Cycle216's mean-zero periodic pseudoinverse.
Thus the Cycle479 Schur result is supplied but interface-mismatched, while the
local recurrence is adapted and retested rather than silently identified.

### B — Q48 Chebyshev local adapter

Freeze the exact nonzero L13 Laplacian interval before rows.  Run 64
Chebyshev semi-iterations from zero.  Every alpha and beta coefficient is
rounded once to the nearest Q48 rational and is then immutable.  Each layer
uses the radius-one Laplacian, the source, and two retained field slices.
The runner records coefficient hashes, solver and exact-3L+ residuals,
reverse-recurrence residuals, word denominator/growth bounds, and the
difference from unquantized coefficients.  Retaining both slices and the
source makes every beta-nonzero recurrence algebraically invertible.

The Q48 multiply/add word law is an exact bounded rational program, but no
retained nearest-neighbour M2 multiplier for those coefficients is imported.
Chebyshev depth is preparation/iteration depth, not time.  CG with runtime
inner products is deliberately not substituted because its global reductions
would be a new host service.

### C — three-reservoir dressed-filter attempt

At the three declared quadrupole cells, install three disjoint Cycle425 local
reservoir vertices in the same coin-vertex-stream update.  The update remains
unitary, radius-one, exactly invertible, and covariant when the complete
source geometry is carried through each of the 24 proper-cubic frames.  From
each local reservoir seed, form the frozen 64-step Cesaro spectral filter

`F = (1/64) sum_(n=0)^63 exp(-i n phi0) U^n`,

with `phi0 = Cycle425.ANGLE / 13^(3/2)`.  Its scalar field projection is the
route-C candidate handed to the common column adapter.  The local powers are
physical; coherent accumulation, normalization, eigenpair selection, and
preparation are not.  The runner reports the normalized candidate's eigen
residual and shifted-profile residual rather than calling it a stationary
dressed eigenstate by fiat.  Spectral-filter depth is not time.

## Required controls and disposition rule

Every route gets train and held solver residuals, raw/completed norm weights,
the one common scale, four packet rows, geometry order, held-no-refit, source
and layer/filter deletion, receiver inverse/deletions, lawful-domain checks,
and a resource manifest.  Route A additionally gets exact word divisibility,
Cycle467 agreement, the periodic schedule, and all24 covariance.  Route B
gets Q48 coefficient and reverse-word controls.  Route C gets full-update
unitarity/inverse, local support, all24 carried-geometry covariance, and its
preparation residual.  The Cycle219 one-particle mass fixture and Cycle230
contact remain spectators.  `E G = G_physical E` is asserted only at a scope
where an actual retained encoding and update are both present.  No host K+
evaluation is called a recurrent gate.

A route is `PHYSICAL_COMPLETE` only if its local preparation, finite-M2
arithmetic/update, physical load-bearing completion, packet rows/order, inverse, leakage,
deletion, all24, mass/contact, and resources all close.  Otherwise it is an
exact bounded adapter or a partial attempt with named walls.  An unfinished
implementation is not a shared substrate obstruction.

## Supplied / derived / open

Supplied: Cycle216's local coin stiffness and exact scalar `3 L+` identity;
Cycle479's 96-layer/D=6^96 relaxation; Cycle467/470/474 unsigned divider,
delivery and finite-box schedule; Cycle425's reservoir/coin/stream update;
Cycle490's word256 signed source column; Cycle491's M64 receiver, occupations,
targets, and factor order; the periodic L13 geometries; tolerances and the
train-only scale rule.

Derived here: the periodic L13 double-buffer schedule; exact four-rail Jacobi
words; the Q48/64 local Chebyshev adapter; the three-reservoir update and
fixed spectral-filter attempt; physical-reservoir completion; train/held M64
rows and route-specific dispositions.

Open unless explicitly closed by output: physical preparation of signed
matrix payloads into the retained unsigned word code; a retained finite-M2
Q48 multiply/add compiler; physical coherent spectral-filter accumulation
and dressed-state selection/preparation; a complete simultaneously
materialized L13 shell and fault model; recurrent source renewal, recoil/work,
energy-stress identity, physical time, gravity/metric, Records, and a Born
occurrence law.

## N1–N8 no-go discipline

N1 — normalized alternative families: (1) retained divide-six/Jacobi words,
(2) fixed-coefficient Chebyshev/rational recurrence, (3) three-reservoir
Cycle425 dressed filtering, (4) conjugate-gradient with a physical reduction
tree, (5) multigrid with local restriction/prolongation, (6) quantum-walk or
QSP resolvent, and (7) direct finite-volume spectral synthesis.  The first
three are attempted; the others remain actionable.

N2 — pairwise wall independence: signed-payload preparation, Q48 arithmetic,
spectral-filter accumulation, complete-shell materialization, and source
renewal are audited pairwise.  Closing any one does not by itself close the
others.  A route-specific miss cannot be promoted across routes.

N3 — hidden-wall scan: the source basis, zero-mode cancellation, 3 factor,
96/64 depths, D and Q48 precision, periodic wrap, double buffers, colour
origin, phase target, factor order, common-scale formula, completion cell,
occupations, packet observable, target rows, tolerances, host normalization,
and readout are explicit.  No appeal to standard, obvious, natural, or
by-construction physics carries a missing interface.

N4 — residual matching: Cycle479's exact word witness at
`scripts/physical_3d_laplacian_s3_generator_provenance_cycle479_2026_07_19.py:270`
matches local divide-six arithmetic but not signed Cycle490 payload
preparation.  Cycle467's divider at
`scripts/physical_elementary_divsix_nn_compiler_cycle467_2026_07_19.py:391`
matches unsigned division but not Q48 multiplication.  Cycle425's stationary
witness at
`scripts/common_cubic_transient_stationary_update_cycle425_2026_07_19.py:420`
matches one-defect local update/eigenstate diagnostics but not a three-defect
physical preparation.  Cycle491's logical spectator at
`scripts/physical_geometry_changing_carrier_tournament_cycle491_2026_07_20.py:244`
matches norm accounting but not the physical-reservoir completion built here.

N5 — scope: only the frozen periodic L13 a1/a2 quadrupoles, two occupations,
four receiver updates, and three declared preparation routes are tested.  No
claim is made for arbitrary sources, volumes, accuracy, autonomous renewal,
or gravity.

N6 — partial closure paths: unsigned word source fanout/interference can be
compiled; Q48 arithmetic can be synthesized from retained reversible adders;
the filter can be replaced by phase estimation/QSP or a local adiabatic
preparation; multigrid and reduction-tree CG remain distinct live routes.

N7 — steelman: build a signed fixed-point source register plus reversible
Q48 multiply-add on the Cycle470 seven-port supercell, use a torus-valid
double-buffer schedule, and compare Jacobi, Chebyshev and a physically
prepared three-defect eigenstate at equal word error and shell resources.
This directly attacks every current adapter seam.

N8 — cross-cycle echo and claim gate: Cycles432→435, 447→450, 463→479, and
484→491 closed earlier walls by enlarging explicit physical constructions.
That history forbids turning the present compiler seams into a no-go.  Broad
no-go: FAIL.  Minimum-content: FAIL.  Shared obstruction: FAIL unless all
independent live routes later match the same residual.  Axiom pressure: FAIL.
There is no axiom pressure in Cycle495.

## Verification and disposition

The independent final cold replay used runner SHA256
`8519b863e28c7fc25ac9f7ce172dad38817b2792f86a21358d4a168976932550`
and exited cleanly with 16 PASS / 0 FAIL.  The measured runner-body time was
534.586848959 seconds; `/usr/bin/time` measured 620.99 seconds real time,
2,280,849,408 bytes maximum RSS (2,175.1875 MiB internally), and
6,234,444,648 bytes peak footprint.

The periodic interface audit preserved exact zero source sum and mean-zero
evolution.  The 125-round schedule passed 3,000 exact signed-permutation
colour-class tests across all 24 frames with maximum symmetric difference
zero.  It does not import Cycle479's Dirichlet trace/Schur result.  Route A's
word decode agreed with the 96-layer finite Jacobi recurrence to at most
`2.220446049250313e-16`; this is exactness only for that finite word
recurrence, not exact Cycle216 `K+` and not an exact prediction completion.
Its Cycle216 equation residual was `0.042075852596186195` on train and
`0.003074702110094298` on held.  Route B's Q48/64 equation residual was
`9.070438455167381e-7` on train and `7.324903842918493e-8` on held, but the
finite-M2 Q48 multiply/add compiler remains absent.  Route C's three-defect
update covariance residual was `7.570711667007543e-16`; its filter candidate
eigen residual remained about `9.45e-3` train and `9.99e-3` held, with
coherent accumulation/preparation still host-supplied.

| Route | stronger-a2 order | all rows within `5e-10` | maximum absolute row residual | disposition |
|---|---:|---:|---:|---|
| A — Jacobi96 | yes | no | `5.9802429130950685e-6` | exact bounded finite-recurrence adapter; signed matrix-payload preparation open |
| B — Q48 Chebyshev64 | yes | no | `5.9795955900388e-6` | partial attempt; Q48 physical arithmetic and preparation open |
| C — three-reservoir filter64 | no | no | `6.646169167623395e-6` | partial attempt; physical filter accumulation/dressed preparation open |

The one train-only common scale was exactly 1.0 and used neither held values
nor packet targets.  The physical completion reservoir was load-bearing and
receiver-active: its train/held norm weights were
`0.12070452948752182/0.11482336235600667` for A,
`0.12070169319960818/0.11480377893155831` for B, and
`0.12529502823782906/0.12532277308642045` for C.  Direct completion deletion
changed the state by `0.34742557402632684`.

Route deletion rows were all above the frozen `1e-12` signal floor while
zero-source/zero-seed outputs were exactly zero.  A source/final-layer signals
were `1.2180190398194684/0.007222525252187277` train and
`1.7791394987212408/0.0005296469244449061` held.  B signals were
`1.218351936293742/1.7713227843811835e-7` train and
`1.780712608314739/5.180269090582741e-8` held.  C seed/filter-layer signals
were `0.9607681642786731/0.005318401579591396` train and
`0.9517403590743805/0.005690969564336692` held.  Receiver, field-stream,
packet-stream, and completion deletion residuals were respectively
`0.00035780133536435595`, `0.09787540721307386`,
`0.6666666666666646`, and `0.34742557402632684`.  Maximum receiver inverse
state residual was `5.305373279256607e-15`; maximum one-step norm error was
`6.972200594645983e-14`.  Contact deletion was exactly zero on the carried
one-particle column, while the separate two-particle contact signal was
`0.36789306705608243`.

No route is `PHYSICAL_COMPLETE`.  The strongest result is A's exact bounded
periodic finite-Jacobi word adapter plus physical load-bearing completion and
held-clean geometry order.  The remaining A source-payload preparation, B
Q48 arithmetic/preparation, and C spectral accumulation/preparation walls
are materially different.  Full N1–N8 therefore finds no route-independent
obstruction, minimum-content result, or axiom pressure.
