# Physical reversible cubic relaxation and clock compiler — Cycle 463 note (2026-07-19)

**Authority: none. Audit: unset.**

## Frozen question and answer

Can Cycle 461's hard-coded three-dimensional orbit profile and its 150
site/tree-specific preparation angles be removed in favor of one reversible
local rule starting from a central source and blank field registers?

Cycle 463 supplies a bounded positive answer for two finite cubes.  The
**train cube `[-1,1]^3`** and **held cube `[-2,2]^3`** use the same local
six-neighbor rule, source convention, fixed-point denominator, precision,
iteration count, clock coupling, and residual threshold.  There is **no host
Poisson solve**, profile table, normalization, or **site-specific angle table**
during update.  The held domain is not refit.

There is no site-specific angle table.

This is a **physical reversible cubic relaxation and clock compiler** for a
finite response fixture.  It is **not lapse, metric, proper time,
energy/stress, backreaction, or gravity**.  It does not derive a universal
source law.  Iteration count and schedule depth are not time.  Authority and
audit status remain unchanged.

“Compiler” is restricted here to an exact reversible word-block map and a
bounded physical-M2 allocation/support certificate.  There is **no
primitive-gate enumeration** for the 249-bit sum/divide block: no complete
Toffoli/CNOT/nearest-neighbor arithmetic trace and no primitive gate-count or
depth minimization.  The M2 counts below are capacity budgets, not a claim that
the arithmetic layout is fully gate-synthesized.

## Frozen rule and domains

Before execution the following were frozen:

| item | train | held |
|---|---:|---:|
| active domain | `[-1,1]^3`, 27 sites | `[-2,2]^3`, 125 sites |
| explicit blank Dirichlet shell | radius 2, 98 shell sites | radius 3, 218 shell sites |
| retained update layers | 96 | 96 |
| fixed denominator | `D = 6^96` | same |
| register width | 249-M2 | same |
| residual threshold | `1/10,000,000` | same |
| wall / RSS cap | 30 seconds / 768 MiB | same process |

The source register is one at the center and zero elsewhere.  All field
history and work registers begin blank.  For every active site `x` and every
layer `k`, the same operation reads the previous layer at all six cubic
neighbors, including explicit blank shell words, and XORs

\[
 Q_x^{k+1}=\frac{\sum_{|e|_1=1}Q_{x+e}^{k}+D s_x}{6}
\]

into a blank retained target word.  Every lawful numerator is exactly
divisible by six.  The map is a reversible basis permutation because the
inputs are retained and the computed word is XORed into the target.  Reverse
layer order applies the same XOR blocks and restores every target to blank.
Outside the exact-divisibility code the finite block permutation can be
totalized with quotient/remainder arithmetic, but the declared decoder refuses
such inputs.

The physical capacity budget reserves space for a site-independent Bennett
compute/XOR/uncompute realization: a `B+3` sum, a `B` quotient, bounded
remainder and carry words, and `3B+16 = 763` work M2 that enter and leave
blank at word-block level.  The executable does not enumerate the elementary
gate realization of that allowance.  The exact reversible word semantics,
the capacity allowance, and division by six are supplied structure.  They are
not a derived fundamental law.

The finite criterion at layer 96 is

\[
 r_x=6u_x-\sum_{|e|_1=1}u_{x+e}-s_x,
 \qquad u_x=Q_x^{96}/D.
\]

The executable evaluates every nonsource row exactly with rational integers,
checks `max |r_x| < 10^-7`, and separately checks that the central defect is
within `10^-7` of one.  Checkpoints at layers 0, 8, 16, 32, 64, and 96 expose
finite-iteration convergence rather than hiding it behind a fitted target.

## Explicit physical M2 layout

Each active or shell lattice cell is represented by a full `40^3` physical-M2
supercell: **supercell scale 40** and 64,000 M2 per cell.  An active block uses:

| component | M2 per active block |
|---|---:|
| 97 retained 249-bit history words | 24,153 |
| reversible arithmetic work | 763 |
| 249 complete dual-clock/rail/start words plus site sidecars | 19,710 |
| source bit | 1 |
| total used | 44,627 |

The remainder is a fixed local routing/work capacity reserve.  A local relaxation
operation occupies at most the target and its six neighboring supercells,
`7 * 40^3 = 448,000` physical M2.  This support is large but bounded,
domain-independent, and its supercell envelope is connected on the physical
integer lattice.  No elementary route through that envelope is enumerated.  The
explicit blank shell makes the same six-input rule applicable at boundary and
interior sites.  The physical budgets are 8,000,000 M2 for the radius-2 train
envelope and 21,952,000 M2 for the radius-3 held envelope.  The executable is
a compact exact representation of those bits, not a dense `2^M` vector.

The rule schedule contains 2,592 train blocks and 12,000 held blocks.  Every
block has the same arithmetic program; only its carried lattice coordinate,
previous-layer inputs, and local source bit vary.  There is no host state query
and no site-dependent coefficient.

## Local clock response

No Q1 amplitude profile or Givens-angle preparation is performed.  Instead,
each final 249-M2 local value word controls the same 249-element bank of
Cycle-451 dual clocks.  For every bit, reference and probe clocks receive four
identical baseline sweeps.  A one bit controls the same local delay response
and a zero bit leaves the probe matched.  Writing `R_xj` for the probe/reference
interval ratio at site `x` and bit `j`, the exact site decoder is

\[
 u_x=D^{-1}\sum_{j=0}^{248}2^j\,4(1-R_{xj}).
\]

This is binary fixed-point reconstruction, not a Born or norm-weighted
probability assertion.  Each site carries complete start-reference and
start-probe clock words for every bit plus start/end event identity, epoch,
profile identity, unique reference/probe device identities, source identity
and calibration, event-ready, and predecessor sidecars.  The response law is
identical at every site and bit; no per-site response program exists.

## Exact compiler, inverse, leakage, and covariance tests

The runner constructs an integer coarse history `G_coarse`, encodes every
integer as a 249-M2 binary word with `E`, independently applies the physical
XOR rule, and checks exact equality

\[
 E G_{\rm coarse}=G_{\rm physical}E.
\]

It then reverses every physical and coarse layer and demands exact restoration
of the central-source/blank-history input.  Source number, register range,
divisibility, boundary blankness, arithmetic work blankness, complete clocks,
blank response rails, and sidecar consistency are all checked.  Insufficient
248-bit precision, a nondivisible word, a nonzero shell word, and an undeclared
radius are refused.

Two covariance statements are tested separately.  First, the output integer
field produced from the central source is exactly invariant under **all 24
proper-cubic frames**.  Second, the executable carries the source, active cube,
zero shell, six-neighbor word-block star, layer order, scale-40 support
envelopes, and clock layout through each frame and checks every word-schedule
row.  This is word-block/support-envelope covariance, not covariance of an
unenumerated elementary arithmetic-gate trace.  Schedule covariance is not
inferred from output invariance.

## Deletions

The executable exposes the following necessities within this fixture:

- deleting the source leaves every retained field word zero;
- deleting the final center rule or one of its six inputs changes the field;
- deleting the center clock response changes its decoded value;
- deleting a reference-clock sweep makes the decoder refuse;
- mutating each event/profile/device/source/readiness sidecar makes the decoder
  refuse;
- reducing the register to 248 M2 refuses `D`;
- injecting an indivisible prior word, a nonblank boundary word, or radius 3
  refuses the declared domain.

These are route-local deletion controls, not constitutional lower bounds.

## Complete supplied/imported inventory

Supplied in Cycle 463:

1. finite radii 1 and 2 and their zero shells;
2. a central unit source bit and the fixed local Jacobi/division-by-six rule;
3. 96 retained layers, `D=6^96`, 249-M2 value words, and 763-M2 arithmetic
   work words;
4. exact site-independent reversible word-block semantics and a Bennett
   capacity allowance, without primitive-gate synthesis;
5. scale-40 full-supercell support envelope and routing capacity reserve;
6. the `10^-7` residual/defect threshold and checkpoint list;
7. the identical bitwise delay-clock coupling and binary positional decoder;
8. event/profile/device/source/calibration sidecar constants;
9. 30-second wall and 768-MiB RSS caps.

Imported from Cycles 444/445/451: the 16-M2 one-hot clock, reversible local
clock sweep, 15-M2 fan/controlled-swap/unfan delay, and relational-clock
decoder boundary.

Removed relative to Cycle 461: fourteen supplied orbit-profile rationals, 150
site/tree-specific Givens ratios and angles, the asymmetric spanning-tree
profile preparation, and norm-based profile reconstruction.

Still not derived: why this relaxation law or source scale is fundamental;
finite-boundary removal; an infinite-volume or continuum Green limit; a
matter/energy-stress source identification; occurrence, Records, Born weights,
metric/lapse/proper time, curvature, backreaction, empirical calibration, or a
universal gravitational law.  Also not supplied is a complete elementary
Toffoli/CNOT/nearest-neighbor synthesis of the arithmetic word block.  No
axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit status is edited.

## Refreshed no-go discipline

The freshness procedure was run against `origin/main`; this section follows
the newer N1-N8 wording there.  Because the result is constructive but bounded
with explicit imports, the gate is recorded in full.  It rejects every broad
negative or axiom-pressure promotion.

### N1 — Alternative route enumeration

The normalized family key is `(object, mechanism, terminal obligation)`.

| family | object / mechanism / obligation | honesty | consequence for a broad no-go |
|---|---|---|---|
| retained-history Jacobi | integer layer field / reversible XOR relaxation / finite residual | **ATTEMPTED** | succeeds on both finite cubes, directly defeating a local-compiler no-go |
| checkerboard or over-relaxation | parity-partitioned field / locally reversible accelerated iteration / same residual | **OPEN — NOT ATTEMPTED** | cannot be ruled out; the mandatory `ATTEMPTED` or `RULED OUT BY PRIOR` marker is unavailable |
| reversible multigrid | nested cubic fields / local restriction-prolongation cycles / scale-uniform residual | **OPEN — NOT ATTEMPTED** | cannot be ruled out |
| quantum-walk path sum | unitary walker plus history / accumulated lattice paths / Green response | **OPEN — NOT ATTEMPTED** | cannot be ruled out; Cycle 459 explicitly left it open |
| dynamical mediator/gauge | local mediator or link variables / source-driven field dynamics / backreacting source-response law | **OPEN — NOT ATTEMPTED** | cannot be ruled out |

Thus N1 fails for any broad impossibility claim.  The cycle ships only the
positive finite construction and the exact remaining imports.

### N2 — Wall-independence audit

The collapsed import set is `Wb` finite boundary/domain, `Ws` source meaning
and scale, `Wa` supplied reversible word arithmetic/relaxation law plus its
not-yet-enumerated primitive-gate realization, `Wc` binary
clock coupling/decoder, and `Wg` physical gravity interpretation/backreaction.

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| Wb/Ws | no | no | yes |
| Wb/Wa | no | no | yes |
| Wb/Wc | no | no | yes |
| Wb/Wg | no | no | yes |
| Ws/Wa | no | no | yes |
| Ws/Wc | no | no | yes |
| Ws/Wg | no | no | yes |
| Wa/Wc | no | no | yes |
| Wa/Wg | no | no | yes |
| Wc/Wg | no | no | yes |

Precision, iteration count, history retention, and block routing are parts of
`Wa`, not inflated as additional independent physics walls.  Device/event
sidecars are part of `Wc`.

### N3 — Hidden-wall scan

The phrases `we assume`, `as is standard`, `the framework provides`, `bridge
context`, `background`, `naturally`, `obviously`, `standard QFT`, `registered`,
and `canonical` are not used as load-bearing steps.  “Supplied structure” marks
an explicit import.  “The map is a reversible basis permutation” follows from
the displayed retained-input XOR definition and is tested by exact inversion.
The hidden-condition scan promoted fixed precision/count, zero shell,
supercell support/routing reserve, missing elementary arithmetic synthesis,
and history retention into
the inventory above.

### N4 — Residual matching

| witness | witness residual | Cycle 463 residual | match/use |
|---|---|---|---|
| Cycle 420 physical source-prediction contract | field/detector values remained host arrays or host solvers | replace a host static solve with retained local M2 relaxation | yes, used only for this import |
| Cycle 459 line-field note | local 3D relaxation and quantum-walk routes remained open | attempt local 3D relaxation | yes, route match |
| Cycle 461 cubic-shell note | rational profile and Givens angles remained supplied | generate the field locally without either table | yes, direct match |
| lattice-Green asymptotic ledger | uniform infinite-distance asymptotic and tail bound | finite-cube residual | no; not cited as closed |
| gravity weak-field ledger | nonlinear self-gravity, Einstein equation, physical Newton constant | finite response fixture | no; not cited as closed |

### N5 — Rhetoric audit

The local rule and decoder are tested per bit, word, site, seven-supercell
support envelope, and complete finite cube.  The arithmetic block is not
tested as an enumerated elementary-gate circuit.  The result is not tested in an infinite lattice,
continuum limit, dynamical geometry, or empirical system.  Therefore negative
phrases are restricted to exact implementation facts: this executable has no
host solve, profile table, angle table, or site-specific response program.
The broader physical labels are boundaries on what is claimed, not universal
impossibility theorems.

### N6 — Partial-closure path scan

Cycle 463 follows the import-retirement shape at word-block level: Cycle 461
made the table/angles explicit; Cycle 463 supplies a bounded local word-law
theorem; a later cycle must enumerate the elementary arithmetic compiler and
an audit can test whether the replacement law itself is retired.  No “new
axiom required” or “no
retained primitive supplies this” statement is made, so the primitive-registry
subcheck is not invoked.  Removing the table import constructively creates no
axiom pressure.

### N7 — Steelman

A hostile reviewer should press further, not declare closure: a reversible
multigrid or quantum-walk path-sum can plausibly reduce the enormous 96-layer
history and scale-40 overhead while preserving locality, and a genuine local
mediator/gauge model could make the source and response dynamical rather than
supplied.  The terminal obligation is to derive a scale-stable source-response
law with backreaction and an infrared limit, then connect it to operational
matter and clocks.  Cycle 463 has not attempted that obligation.

### N8 — Cross-cycle echo and claim gate

The prescribed repository search and all available `NO_GO_LEDGER.md` paths
were revisited.  The `lattice-greens-asymptotic-boundary-20260608` ledger warns
that finite fixed-parameter checks do not prove the required uniform
infinite-distance asymptotic; Cycle 463 does not repeat that mistake.  The
`gravity-weak-field-sign-repair-20260611` ledger preserves nonlinear
self-gravity, Einstein-equation, and physical-Newton-constant gaps; none is
claimed here.  Cycle 459's local-relaxation reopening mechanism is precisely
what this cycle attempts, illustrating why the earlier route-specific boundary
could not support a no-go.

**Broad gravity or no-go claim: FAIL.**  No minimum-content theorem and no
axiom-pressure claim survives N1-N8.  The admissible result is the finite local
reversible construction with its remaining imports.

## Frozen executable result

The final cold execution reports `RESULT pass=11 fail=0`.

| quantity | train R=1 | held R=2 |
|---|---:|---:|
| nonsource rows checked | 26 | 124 |
| maximum exact-rational row residual, printed decimal | `4.440892098500626e-16` | `5.5933003103895076e-08` |
| central defect | `0.9999999999999991` | `0.9999999254226626` |
| defect residual | `8.881784197001252e-16` | `7.45773374718601e-08` |
| local rule applications | 2,592 | 12,000 |
| physical M2 capacity represented | 8,000,000 | 21,952,000 |
| word-block schedule SHA-256 | `6eda2fb6e40f554bb3a5a9e21ab91d04f2db30b0ac0b020f42b58ede5b3b7ac8` | `2baa2a9210ae68d4018c5157fda220ead7a6c1770e553ae270cc517db683ac8d` |

Both E/G comparisons and both coarse/physical inverses are exact.  Work and
boundary leakage, divisibility remainders, decoder mismatches, clock inverse
failures, and all-24 covariance failures are zero.  The final cold run took
25.970 seconds and peaked at 207.89 MiB, below the frozen 30-second and
768-MiB caps.

## Disposition

Cycle 463 may be retained only if the executable freezes with zero failed
tests and remains under the declared resource caps.  It does not authorize an
audit verdict, axiom edit, or promotion to gravitational physics.
