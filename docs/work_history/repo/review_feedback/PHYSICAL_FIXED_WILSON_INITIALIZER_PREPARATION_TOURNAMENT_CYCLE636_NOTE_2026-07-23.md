# Physical fixed-Wilson initializer preparation tournament — Cycle 636

Classification: **positive state-carried preparation of three auxiliary plus-reference rails; no full Cycle532/Cycle537 code isometry or full-M64 physical E/G**

Authority: **none**

Audit: **unset**

Author artifact status accepted: **false**

Breakthrough bar met: **false**

## Result up front

Cycle 636 does not re-solve raw Wilson fixing and does not duplicate Cycle
637's independent physical-cap embedding probe.  Cycle537 already proves that
the exact three Cycle532 Wilson words are products of bounded fill-face checks
and that the abstract filled code is `target_full-Fock tensor gauge_(N-1)`.
The live preparation question is whether local physical operations generate a
lawful state/isometry in that code without a supplied spin or gauge vacuum.

The strongest new construction is Route B.  One supplied oriented plus seed
per axis launches a onehot head around a Wilson reference rail.  The head
applies one local `H`, nearest-neighbor CNOT growth, visited-bit copying, and
head SWAPs.  Uncontrolled Clifford/head gates have support at most two M2;
head-controlled data action has support at most three.  The three axes run
in parallel and exactly prepare three `+` GHZ/Wilson reference rails:

| size | data+head+visited M2 | parallel depth | CNOT calls | GHZ rank/axis | inverse/deletion |
|---|---:|---:|---:|---:|---:|
| L3 | 27 | 7 | 6 | 3 | yes |
| L6 | 54 | 16 | 15 | 6 | yes |
| L7 | 63 | 19 | 18 | 7 | yes |

All CNOT deletions remove the full `X` Wilson from the stabilizer span; deleting
the seed `H` does likewise.  Reversing the schedule restores every blank data,
head, and visited input.  Oriented loop schedules close under all 24
proper-cubic frames and all 576 products at L3/L6/L7.  After the seed is
present the local head state carries branch control; there is no outcome
postselection or host branch selection.  It is nevertheless not a fully
autonomous initializer: the seed position/orientation/plus state and global
tick/edge schedule remain supplied.  Schedule depth is compiler latency, not
physical time.  The prepared GHZ reference leakage is exactly zero on the
declared onehead code, but forward head/visited work has unit leakage from the
blank-work subspace and returns to blank only under the inverse schedule.

This is an **O(L) local preparation**, not a bounded local encoding `E` per
coarse cell.  The rails are auxiliary references, not the Cycle532 rough-code
state.  Coupling them to an unknown rough sector returns the Route-A reset
problem; it does not create the complete physical code isometry.

## Route A — retained-exhaust syndrome/reset

The exact coherent dilation copies a Wilson sign into a retained exhaust M2,
applies the physical sign-flipping membrane conditional on that exhaust, and
resets the Wilson character to plus.  It is unitary and uses no postselection,
host outcome choice, or erased syndrome.  Its plus-output residual is
`0.000e+00` and its exhaust copy residual is
`0.000e+00`.

Retaining exhaust does not repair the Cycle535 matter action.  On a crossed
target seam observable the exact Heisenberg identity remains `A -> W A`.
The target intertwiner residual is `2.0`,
while the twisted-identity residual is
`0.000e+00`.  Fixed-cut feedback
therefore still fails the Cycle230 seam and full-Fock `Gamma(P)`.  Averaging
cuts gives exact residual `2/L`—`0.666666666667`,
`0.333333333333`, and
`0.285714285714` at L3/L6/L7.

Route A2 tests local pumping on Cycle537's fill checks.  The cap-interior
edge/face incidence has rank `L^2-1`; every even syndrome is correctable and
every single odd syndrome is refused at all three sizes.  This is positive
conditional preparation when the boundary Wilson is already plus.  It cannot
change an unknown boundary sign because each cap-only edge flips two faces
and the total face syndrome equals the boundary Wilson.  A host-free pairing
or convergence law is not silently supplied.

## Route B2 — root-free defect pumping

Every basis word and every nearest-neighbor pair flip is exhausted through
L7.  Pair flips move or annihilate local defects and are translation/cubic
covariant, but preserve the loop character exactly.  Both sectors remain
nonempty.  This route is a useful root-free local motion algebra, not plus-sign genesis;
more general processes that leave this rail algebra are not excluded.

## Route C — boundary growth and doubled neutrality

On an open/punctured chain, the same local wavefront grows a pure plus rail
from a plus boundary seed.  Reversing that seed gives an orthogonal minus rail.
If the boundary sign is unfixed or discarded, the mixture has Wilson
expectation zero rather than plus one.  Closing the puncture therefore does
not derive the sign; it either retains or hides the supplied seed.

For two rough copies, three abstract relative constraints have exact rank three
in the six-character space.  They specify paired/neutral relative signs but
leave `3` diagonal
characters.  Deleting one relative constraint lowers the rank to
`2`.  A doubled
character algebra can relocate the three signs but does not derive six
absolute plus values without an anchor.  No physical local doubled initializer
is constructed here.

## Full isometry audit

| size | rough M2 | fixed rank | target qubits | gauge qubits | filled M2 | filled rank | full E built |
|---|---:|---:|---:|---:|---:|---:|---:|
| L3 | 594 | 406 | 162 | 26 | 630 | 442 | no |
| L6 | 4752 | 3241 | 1296 | 215 | 4932 | 3421 | no |
| L7 | 7546 | 5146 | 2058 | 342 | 7798 | 5398 | no |

At each size, `target + gauge = 7N-1`, exactly the Cycle532/Cycle537 code
exponent.  That equality is an interface contract, not a preparation circuit.
The three uncoupled auxiliary GHZ rails establish **zero** physical Cycle537
stabilizers and have zero mutual information with the physical code.  A full
arbitrary-gauge isometry must establish 442, 3421, and 5398 independent
physical stabilizer correlations at L3/L6/L7.  Fixing the gauge vacuum adds
26, 215, and 342 logical-gauge correlations, for totals 468, 3636, and 5740.
Even an ideal but unbuilt transfer of all three Wilson signs could remove at
most three obligations, leaving 465, 3633, and 5737 respectively.
None of the routes maps all `6N` target qubits plus a fixed `N-1` gauge input
into every physical stabilizer while returning head/work/exhaust and proving
the complete logical Pauli conjugation.  Cycle532/Cycle537's full-Fock `G`
remains exact only after the code space is supplied.  Therefore Cycle636 does
not establish a full-M64 `E G = G_physical E`.

`W_embed` and `W_prepare` remain independent.  Cycle636 addresses only
preparation; Cycle637 owns the independent one-fixed-physical-cap embedding
probe.  A preparation on an abstract cap supplies no substrate embedding, and
an embedding supplies no state/isometry.

## Resource, genesis, and semantic ledger

Supplied are the immutable Cycle532/535/537/539/598 shores, finite L3/L6/L7
domains, Route-A syndrome/correction schedule, GHZ seed origins/orientations
and plus states, blank head/visited rails, global ticks, cap pairing convention,
puncture seed, and doubled relative constraints.  The `N-1` gauge reference,
full stabilizer tableau circuit, and volume logical map are not derived.

## Deletion, leakage, and lawful domain

The exact lawful domains are L3 and L6 construction/training sizes and a held
L7 size; no fit parameter is changed for L7.  Route A has zero unitary-inverse
residual, but an input minus sector leaves unit worst-case exhaust leakage from
the blank-exhaust subspace.  Removing syndrome copy or reset gives Wilson
residual two; removing feedback gives zero target twist and therefore does not
implement the reset channel under test.  Route B has zero GHZ-code leakage on
the declared onehead input, every CNOT deletion and the seed-H deletion remove
the Wilson stabilizer, and forward head/visited work has unit leakage from its
blank subspace.  The inverse schedule returns that work exactly.  Zero-head
and multihead words—5, 58, and 121 at L3/L6/L7—are explicitly outside the
declared code.  Route C detects one deleted growth CNOT at every size.  The
all24/all576 audit acts on oriented schedule labels, not on a runtime frame
selector or on Cycle637's still-separate physical embedding.

No syndrome or visited rail is called a Record.  No compiler layer is called
time, no phase is called energy, no generator is called a rate, and no gauge
capacity is called stress/source/gravity.  No probability/Born or actuality
claim is made.

## Prior-art and novelty boundary

GHZ/CNOT wavefronts, stabilizer syndrome reset, defect motion, punctured
boundary growth, and doubled relative-sign constraints are standard mechanism
classes.  No general novelty or priority is claimed.  The repo-specific
contribution is their exact separation on the Cycle532/Cycle537 preparation
contract, the L3/L6/L7 resource/deletion/covariance audit, and the explicit
full-isometry/gauge-vacuum boundary.  No external theorem is used as runner
evidence.

## N1–N8 no-go discipline

N1 normalizes six actually attempted families and lists the untested
full-tableau encoder separately as an open route that is not counted.
N2 retains exactly two independent walls and both directional implications are
false.  N3 inventories every seed, sign, exhaust, schedule, cap, puncture,
relative constraint, gauge input, and tableau import.  N4 has eight exact
same-scope residual rows and two dropped nonmatches.  N5 has six complete
five-resolution rhetoric rows.  N6 has six structured partial-closure paths.
N7 gives the actionable full symplectic-tableau encoder steelman.  N8 gives
five row-wise exact cross-cycle echoes.

The N1 attempt threshold is met, but the concrete untested full-tableau route
keeps every broad conclusion open.  Broad no-go, minimum content, shared
obstruction, and axiom pressure are all withheld.

Shared route-independent obstruction: **not established**.

Axiom pressure: **none**.

## Six-wall ledger

| wall | Cycle636 movement | residual |
|---|---|---|
| `C_ref` | literal bounded-support O(L) plus-reference rails and retained provenance are constructed | seed plus state/origin/orientation, global schedule, and N-1 gauge reference remain supplied; no full E |
| `C_num` | exact L3/L6/L7 ranks, resources, character sectors, and deletion counts | dimension equality is not a tableau isometry |
| `C_wrap` | head/visited/exhaust rails retain preparation provenance and invert | they are not Records, time, actuality, or realized history |
| `C_int` | reset's exact seam twist is isolated; conditional Cycle532/Cycle537 G remains comparison-positive | no complete matter-preserving initializer or new interaction law |
| `C_local` | bounded-support head wavefront, local syndrome incidence, all24/all576, inverse/deletion/held tests pass | O(L) preparation is not bounded local E; embedding is independent Cycle637 work |
| `C_source` | seed, blank capacity, exhaust, and doubled overhead are explicit | no energy/stress/source/gravity meaning or autonomous resource genesis |

## Disposition and next campaign

**PASS** for the scheduled state-carried O(L) preparation of three auxiliary plus
reference rails, retained-exhaust reset accounting, conditional fill-syndrome
correction, and the root-free/boundary/doubled exact dispositions.

**FAIL / DO NOT CLAIM** for a bounded local Cycle532/Cycle537 encoding `E`, a
prepared gauge vacuum, a full-M64 physical compiler, autonomous initialization/seed genesis,
shared obstruction, minimum content, or axiom pressure.

The optimal next preparation campaign is the hostile steelman: materialize the
complete Cycle537 stabilizer/matter/gauge tableau, synthesize a routed Clifford
isometry from `6N` target plus `N-1` fixed gauge inputs, replace its root/order
by state-carried local control, return every work rail, and only then compose
the committed full-Fock `G`.  Keep Cycle637's embedding result as a separate
input rather than conflating physical placement with preparation.
