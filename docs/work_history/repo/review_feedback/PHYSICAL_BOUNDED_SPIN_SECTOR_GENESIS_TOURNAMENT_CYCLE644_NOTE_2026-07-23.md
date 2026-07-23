# Physical bounded spin-sector genesis tournament — Cycle 644

Status: **PASS — exact rooted three-sign seed and reversible plaquette; replicated/full periodic preparation remains open**  
Authority: **none**  
Audit: **unset**  
Accepted: **false**  
Constitutional effect: **none**

## Question

Can the exact Cycle-641 `Q=+1` charge-ribbon code acquire its periodic spin
sector without applying a growing Wilson word, reading a global parity, or
using host-side sector selection, while preserving bounded physical support
and the L3/L6/L7 target?

Cycle 644 obtains a positive theorem for a globally rooted seed of the three
displayed Wilson signs and falsifies the tested replicated fixed-defect tensor
seed for all translated loops.  It does not prepare every bounded local
stabilizer and therefore does not supply the requested full periodic
`E/preparation/G` compiler.

## Strongest constructive result

For each axis and every transverse coordinate, translate the Cycle-532 Wilson
loop.  There are exactly `3 L^2` such loops.  On L3/L6/L7:

- all translated loops commute;
- adding every translated loop to the bounded local stabilizers increases
  rank by exactly three, the same increment as the three displayed base
  Wilson loops;
- the translated all-plus constraints are consistent and select the same
  fixed-spin code;
- the single-M2 axis conflicts in the tested factorized ansatz occur on four
  fixed internal-face roles per coarse cell;
- those `4 L^3` conflicts split into disjoint four-M2 blocks of physical L1
  diameter 8, but the Wilson restrictions on successive blocks are not all
  the same commuting local operator.

Prepare each block as two Bell pairs with a phase gate on the second member of
each pair:

```text
H(q0), CNOT(q0,q1), S(q1),
H(q2), CNOT(q2,q3), S(q3).
```

Every remaining Wilson-support factor is prepared in its local X/Y/Z
eigenstate.  One unique single-M2 sign marker per translated loop corrects the
length-dependent Hermitian phase.  This replicated tensor seed succeeds for
only `L^2` translated loops and has zero expectation for the other `2L^2`.
The maximum residual from the all-plus target is exactly 1 on L3/L6/L7.  Thus
the fixed-size repeated defect tested here does **not** prepare the translated
family.

A narrower positive construction survives: restrict to the three displayed
Wilson loops rooted at the macro-origin.  Their only crossing is one four-M2
diameter-8 block.  Single-M2 axis states along the three noncontractible paths
plus three unique sign markers prepare all three signs with residual 0 on
L3/L6/L7.

No Wilson operator is applied or measured in the rooted triplet seed.  Every
elementary preparation gate touches at most two M2 factors, and the crossing
block has diameter 8.  Parallel gate depth is bounded by 6, but the union of
prepared path factors grows with L: weights `51,105,123` on L3/L6/L7, with
three Wilson weights `21,39,45` and union physical L1 diameters
`96,192,224`.  Coordinate axes, the macro-origin, three
noncontractible paths, compile-time L/parity, and three sign markers are
supplied.  This is locally gated, globally rooted inflow; because its path
length grows, it is not a bounded-neighborhood `E` or root-free genesis.

The crucial residual boundary is equally explicit: most bounded local
stabilizers have expectation zero in this factor/block seed.  The seed fixes
the spin sector, not the full code state.

This narrows Cycle 641 carefully: the three displayed signs need no
growing-*support* gate, but their exact seed still occupies three growing
rooted paths.  The remaining task is both to remove that rooted path import
and to compose the result with every bounded local stabilizer.

## Route A — replicated boundary inflow

Disposition:
`ATTEMPTED_REPLICATED_FIXED_DEFECT_FAIL__POSITIVE_ROOTED_BASE_TRIPLET_SEED`.

Route A uses the rough-terminal physical face graph and tests every translated
Wilson loop rather than only the displayed three.  The four crossing roles per
cell identify all local X/Y/Z conflicts, but identical Bell/S blocks do not
resolve the varying segment restrictions along two axis families.  The exact
expectation census is `L^2` plus and `2L^2` zero at every size.

The preparation resources scale as follows:

| resource | scaling |
|---|---|
| physical code layout | 22 M2/cell, inherited |
| attempted replicated conflict block | four existing M2/cell; translated target fails |
| largest elementary gate support | two M2 |
| largest interacting diameter | 8 |
| parallel block/axis gate depth | constant |
| rooted triplet path-factor count | `51,105,123` on L3/L6/L7 |
| rooted triplet sign markers | 3 |
| growing-support gate or measurement | none |
| supplied global structure | axes, origin sheets, L parity |

The fixed all-plus code retains Cycle-532's all-24/all-576 covariance.  No
all24 preparation-circuit family is proved for the rooted triplet seed.
Macro-origin, paths, and marker inflow are supplied, not autonomously
generated.

Route A fails the replicated translated-loop target and, even on the exact
rooted triplet, is not in the `+1` eigenspace of any displayed bounded local
stabilizer in the expectation census.  It is not called a bounded-neighborhood
full `E`.

## Route B — reversible local ancilla

Disposition:
`EXACT_REVERSIBLE_ONE_PLAQUETTE_DATA_LINK_ENCODER__ELEMENTARY_AND_PERIODIC_EXTENSION_OPEN`.

Route B separates four data M2 factors from four Cycle-641 link M2 factors.
For every lawful even data word `n`, a controlled link unitary maps

```text
|n>_data |0000>_link -> |n>_data E_641|n>_link.
```

The executable synthesizes one fixed support-eight unitary and its inverse.
On this code:

- one ordinary data SWAP times the Cycle-641 link FSWAP gives the fermionic
  edge action;
- the ordinary data permutation `(02)(13)` times either Cycle-641 link
  exchange path gives the exterior/Fock exchange action;
- code leakage is zero at tolerance;
- prepare-update-unprepare returns the four link factors to blank and leaves
  the exact fermionic data target;
- deleting the link exchange gives a nonzero signal.

This is an exact autonomous reversible **one-plaquette** encoder.  The
controlled support-eight unitary has not been factorized into a literal
one/two-M2 circuit, and shared-link periodic composition has not been
constructed.  Support eight is constant, but it is not called elementary.

## Route C — local measurement/reset

Disposition:
`ATTEMPTED_L3_LOCAL_RESET_DUALS__INCOMPLETE_GENERATOR_COVERAGE`.

Route C selects an actual independent basis of the L3 bounded local
stabilizers, then enumerates every single-M2 X/Y/Z syndrome.  A generator can
be pumped independently by the local Kraus rule

```text
K0=P_plus,
K1=R P_minus
```

when a correction `R` anticommutes with that generator, commutes with every
other selected generator, and commutes with all three Wilson operators.  The
runner searches weight-one corrections and weight-two corrections of physical
diameter at most 64.

The route resolves a strict subset of the 403 independent L3 generators and
leaves the remainder explicit.  It separately reruns the search after
deleting Wilson preservation to distinguish the spin-sector constraint from
the local-pump architecture.  Measurement outcomes feed only the local
correction; no global sector value is read.  Because coverage is incomplete,
no L6/L7 pump is executed and no dissipative convergence claim is made.

Alternative independent bases, weight-three/four corrections, and a
multi-round cellular automaton that transports syndrome to punctures remain
open.

## Held-size, covariance, and fixture controls

Route A executes the translated-Wilson rank, conflict, failed replicated
preparation, exact rooted-triplet preparation, marker, and expectation tests
on L3, held L6, and held-out L7.  It also reruns the fixed-code all24/all576
covariance surface; preparation covariance itself is not established.  The
L3/L6/L7 layouts retain
22 M2/cell, maximum mapped B-FSWAP support 13, and three seam blocks per cell.

The Cycle-219 mass, Cycle-230 contact, and logical seam comparators are
re-executed through the immutable Cycle-532 surface.  These are preserved
comparators, not a newly enumerated full rough-code seam matrix.  Cycle-639's
onsite A2 content is compatible through the same fixed matter factor; Cycle
644 does not construct a new A2 matrix lift.

Deletion and leakage boundaries are route-specific:

- Route A exposes the translated-loop residual 1 and that all local-stabilizer
  expectations are zero; the exact base seed retains growing rooted paths,
  and flipping one prescribed base marker gives residual 2.
- Route B has exact code leakage and a deleted-link-exchange signal.
- Route C records every unresolved generator rather than treating a partial
  pump as full preparation.

## N1-N8 discipline

The current origin-main `no-go-discipline` skill is followed.  Its hash is
`7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7`.

### N1 — normalized alternative routes

Executed:

1. replicated puncture/boundary inflow;
2. reversible data/link ancilla preparation and unpreparation;
3. local measurement/reset with isolated syndrome duals.

Open and not counted as failures:

4. a non-JW auxiliary Clifford Wilson resolver;
5. a multi-round puncture-directed cellular-automaton pump.

### N2 — directed wall-independence audit

Route A's supplied macro-origin and rooted paths do not imply Route B's support-eight
factorization wall.  Route B's periodic shared-link wall does not imply Route
C's isolated-dual coverage wall.  Route C's selected-basis failure does not
imply that Route A's Wilson seed cannot be completed by a different encoder.
All 20 ordered directions among the five collapsed walls are explicit in the
receipt with `from`, `to`, `closure_implied=false`, and scoped interface
evidence.  Logical independence beyond those executed interfaces remains
unestablished because no target-equivalent full route has been closed or
exhausted.

### N3 — hidden-wall scan

Supplied structure includes L and its parity, axes, coordinate-zero boundary
sheets, four internal-face roles per cell, Wilson-support axis eigenstates,
the immutable Cycle-532 code/runtime, the immutable Cycle-641 plaquette code,
Route B's synthesized support-eight block, and Route C's chosen independent
basis.  Preparation schedules are not physical time.  No energy, rate,
Record, source, stress, gravity, or autonomous resource genesis is imported.

### N4 — exact residual matching

Cycle 641 had Wilson rank increments `(3,3,3)` on L3/L6/L7.  All translated
loops add the same three ranks, but the replicated tensor seed has residual 1.
Only the displayed rooted triplet is prepared with residual 0.  That is an
exact match to the three-sign eigenvalue scope, not to a bounded-neighborhood
or full local-code preparation scope.  Route B's
prepare-update-unprepare residual is compared only with the same
one-plaquette Cycle-641 target.

### N5 — five-resolution rhetoric audit

- Element: Route A gates touch at most two M2s; Route B's synthesized block
  touches eight.
- Site: four M2 roles per cell identify crossings, but the repeated block does
  not resolve translated segment variation.
- Mode: Route B encodes the even four-mode data/link plaquette.
- Block: the rooted three-sign block is exact; the replicated translated seed
  has residual 1 and local stabilizers are not prepared.
- Lattice: no route supplies one full L3/L6/L7 `E/preparation/G`.

### N6 — partial-closure paths

The receipt lists exact file/status/what-closes rows for the immutable
Cycle-641 plaquette, the Route-A Wilson seed, the Route-B reversible block, and
the Route-C reset-dual audit.  Remaining actions are alternative stabilizer
bases, bounded weight-three/four duals, puncture-directed syndrome transport,
non-JW Clifford resolution, and elementary factorization of Route B.

### N7 — actionable steelman

The exact rooted-triplet seed might be replaced by a replicated crossing
tensor carrying the varying segment character, then followed by a local
Clifford or dissipative encoder whose defects flow to punctures without
changing Wilson signs.  The decisive certificate is a literal held-size
`E/preparation/G`, all local checks `+1`, no boundary-sign input, preparation
all24/all576, full seam/A2/contact/mass, deletion, and
prepare-update-unprepare.  The receipt cites the Cycle-641 and Cycle-247 notes
that make this route actionable.

### N8 — cross-cycle echo

Cycle 247 supplied one rough terminal per cell and obtained a local even
algebra with boundary multiplicity.  Cycle 532 typed the fixed factor with
three Wilson signs.  Cycle 641 made the contractible `Q=+1` preparation exact.
Cycle 644 shows only that the displayed triplet can be set without a
growing-support gate; its locally gated seed still occupies growing rooted
paths.  It does not retire replicated local genesis, local-code preparation,
or boundary genesis.  Mechanism and applicability are recorded row by row in
the receipt.

Therefore:

```text
broad negative gate: FAIL / DO NOT SHIP
minimum-content gate: FAIL / DO NOT SHIP
shared-obstruction gate: FAIL / DO NOT SHIP
axiom-pressure gate: FAIL / DO NOT SHIP
```

No impossibility, minimum-content, shared-obstruction, or axiom-pressure claim
is shipped.

## Supplied structure

- immutable shore commit `40e8b5718ee92c0e1d0ec41386c0ff9cc84aefac`;
- compile-time L and L parity;
- three coordinate axes, one macro-origin, and three rooted noncontractible
  paths;
- three local sign markers for the exact rooted triplet;
- four named internal-face roles per coarse cell;
- one Bell/S crossing circuit per cell;
- single-M2 X/Y/Z eigenstates on translated Wilson supports;
- the Cycle-247 rough-terminal graph;
- the Cycle-532 local constraints, fixed code, layout, and mapped runtime;
- the Cycle-641 local charge-ribbon encoding/update;
- Route B's fixed support-eight controlled unitary;
- Route C's chosen L3 independent basis and local syndrome feed-forward.

Not supplied or claimed: a growing Wilson operation, global parity query,
runtime sector branch, autonomous boundary creation, full local-stabilizer
encoder, literal periodic seam matrix, physical time, energy, rate, Record,
source, stress, gravity, or Born law.

## Prior-art and novelty boundary

Preparing stabilizer eigenstates from local Pauli eigenstates and Bell blocks,
using boundary conditions to choose spin structure, reversible ancilla
encoders, and local syndrome-reset maps are established techniques.  Cycle
644 does not claim invention of those methods.

The new repository-local result is the executable decomposition and
falsification of the naive repeated four-M2 tensor seed for **all** `3L^2`
translated Cycle-532 Wilson loops, together with an exact locally gated seed
for the displayed rooted triplet.  It quantifies rank equivalence, the
`L^2/2L^2` plus/zero expectation split, diameter 8, path-factor growth
`51/105/123`, and why neither surface is a full code preparation.

Thirring is not used.

## Dependency ledger

| Wall | Cycle-644 disposition |
|---|---|
| `C_ref` | Narrowed: the displayed triplet has an exact locally gated but globally rooted path seed; the repeated per-cell translated seed fails. Axes, origin, paths, L parity, and markers are supplied. |
| `C_num` | Unchanged globally. Route B gives an exact eight-M2 reversible local even-CAR block; full periodic E remains open. |
| `C_wrap` | Narrowed: no growing-support Wilson operation is needed for the displayed triplet, but prepared path extent grows with L. Replicated genesis, local-code preparation, and literal seam-matrix EG remain open. |
| `C_int` | Cycle-219 mass, Cycle-230 contact/logical seam, Cycle-639 A2, and Cycle-641 exchange remain pinned comparators, not a new full update. |
| `C_local` | Advanced on spin-sector seed and local reversible unpreparation. Route C leaves explicit unresolved L3 generators and no held pump. |
| `C_source` | Unchanged: no energy, rate, source, stress, gravity, Record, or autonomous resource genesis. |

Maturity scores remain operational quantum/records `3.0/5`, time `1.5/5`,
inertia/matter `3.0/5`, gravity/source `1.0/5`, and Born/probability `2.0/5`.
The result sharpens `C_ref`, `C_wrap`, and `C_local`; it adds no Record, clock,
source, or probability law.

## Scope firewall

- A Wilson eigenstate is not a full fixed-code `E`.
- A rooted noncontractible path seed is not bounded-neighborhood or autonomous
  genesis.
- Constant elementary support does not make a globally rooted preparation
  root-free.
- Constant parallel depth does not remove growing rooted path extent or the
  path-factor counts `51/105/123`.
- A support-eight unitary is not a literal one/two-M2 circuit.
- Partial L3 reset coverage is not held-size preparation.
- A logical seam comparator is not a literal full rough-code seam matrix.
- A preparation schedule is not physical time.
- A phase is not energy; a generator is not a rate.
- A gauge seed is not a Record.
- No source or gravity claim is present.

## Optimal next campaign

Replace the failed identical replicated tensor by a direction-sensitive
crossing tensor, and compose the exact but rooted base-triplet seed with a
local stabilizer encoder.  First search alternative independent bases and
weight-three/four bounded duals; then construct a puncture-directed
multi-round syndrome automaton and test convergence on L3/L6/L7.  Require
boundary-marker deletion, preparation all24/all576, an elementary
factorization of Route B, full held-size prepare-update-unprepare, and literal
seam/A2/contact/mass surfaces before claiming periodic `E`.
