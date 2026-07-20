# Physical M64-payload solver-compiler tournament — Cycle 499

Date: 2026-07-20

Authority: none

Audit: unset

## Frozen before Cycle499 target outputs

Cycle 499 asks whether Cycle 495's host construction of `raw_fields` and
`completed_state` can be replaced by an actual linear physical map carrying
the unknown signed M64 matrix payload emitted by Cycle 491.  The decisive
intertwiner is required on a declared code space,

```text
E G_solver = G_physical E,
```

without cloning the payload, a recurrent host `K+`, a runtime state query,
per-matrix-row amplitude injection, postselection, hidden amplitude
amplification, or an undeclared inverse readout scale.

This contract and the train/held split were frozen after reading the inherited
Cycle 495 results but before executing any new Cycle499 target, compiler, or
packet output.  The inherited Cycle495 rows are fixed comparators, not tuning
data.  No gate, scale, code basis, tolerance, or route disposition may change
after a Cycle499 held output is observed.

The domain is the periodic `L=13` Cycle491 source-compiled field code.  For
each geometry the 18 active directional field modes, tensored with every M64
matrix entry, define the physical input.  The declared carrier code is the
rank-16 column space actually produced by the frozen local Cycle490 source
vertices.  This is a compile-time code declaration, not a runtime state query.
The train `a=1` and held `a=2` geometries occupy two invariant blocks of one
fixed direct-sum apparatus.  Their geometry-sector preparation and separate
compiled coefficients remain supplied structure.  Arbitrary basis vectors
and coherent superpositions inside each rank-16 carrier code, tensored with
arbitrary M64 payload vectors, must be transported linearly.

## Frozen routes

### A — local Jacobi96 LCU/block encoding (priority route)

Let `P=A/6` be the normalized periodic six-neighbour adjacency.  Cycle495's
Jacobi response is

```text
J_96 = (1/2) sum_(k=0)^95 P^k.
```

The physical signal block frozen here is the honest contraction

```text
K_A = J_96 / 48 = (1/96) sum_(k=0)^95 P^k.
```

One 97-label one-hot clock and 96 fresh six-direction coin tensor factors are
required.  Encoding each six-way factor in three binary M2 gives the formal
allowance `97 + 96*3 = 385` M2 per cell, but their joint walker register has
dimension at least `6^96`.  A spatially moving payload must carry that entire
clock/history register; clocks left at the departure cell do not implement
the convolution.  The runner therefore requires an exact small-cubic
top-left-block/inverse test and inventories controlled whole-register motion,
but **does not claim a literal M2 synthesis of that moving register**.  Route A
is an abstract bounded-depth block-encoding resource upper bound with a named
placement/scheduling wall.  There is no shared global clock or address
service hidden in the positive signal algebra.  Every proposed failure
clock/coin factor would have to carry the same M64 payload and receive the same
global matter/contact factors as the signal rail.

Because the unscaled `J_96` has ambient mean-zero operator norm greater than
one on `L13`, it cannot itself be a deterministic unitary signal block.  The
runner must report both the physical `1/48` signal packet and the inherited
unscaled Cycle495 packet.  Multiplying the signal by 48 is a supplied inverse
diagnostic scale only; it is not a physical update, postselection, amplitude
amplification, or new packet prediction.

### B — finite code-restricted Stinespring / adjacent-Givens upper bound

For each frozen geometry, let `Q_g` be the orthonormal rank-16 carrier-code
basis and let `T_B` be local uniform-direction projection, the fixed Q48
Chebyshev64 periodic convolution, and uniform-direction lift.  The runner
must first verify

```text
||T_B Q_g|| <= 1.
```

It then builds the full signed complex-amplitude isometry

```text
V_g = [T_B Q_g ; sqrt(I - Q_g^dagger T_B^dagger T_B Q_g)].
```

This preserves phase and every M64 payload entry; it is not Cycle460's
positive receiver-weight channel.  Adjacent-row QR compiles both `Q_g` and
`V_g`; their schedules compose as `U_V U_Q^dagger`.  Every primitive is an
onsite phase or a two-M2 number-preserving adjacent Givens on a supplied
Hamiltonian-line routing of the finite apparatus.  Train and held blocks are
disjoint parts of one frozen schedule and no input column is queried during
update.

This is an explicit finite nearest-neighbour upper bound.  Its Fourier/kernel
coefficients, geometry blocks, Hamiltonian-line embedding, QR order, and
roughly quadratic gate count are supplied compile-time structure.  It is not
a homogeneous recurrent law, not an autonomous program synthesizer, and not
constant-overhead compilation as volume grows.

### C — local Cycle425 three-defect filter64 LCU

For each frozen geometry, `U_g` is the exact Cycle425 coin/three-local-vertex/
stream update used by Cycle495.  The physical signal block is

```text
K_C = P_uniform (1/64) sum_(k=0)^63 exp(-i k phi_0) U_g^k P_reservoir,
phi_0 = Cycle425.ANGLE / 13^(3/2).
```

A 65-label one-hot clock is represented on all seven reservoir/field modes at
every cell, for `65*7=455` clock-labelled carrier M2 per cell.  The stream
moves a field rail and its clock label together; no clock is left behind.
Clock-conditioned powers of the bounded-local `U_g`
and reverse clock preparation implement the average of unitaries.  The input
uniform projection, reservoir injection, output uniform projection, other
reservoir/directional components, and nonzero clock labels are all parts of
one unitary block encoding.  They are not host accumulation.  In a completed
compiler the failure modes would be physical auxiliary payload rails that
bypass field coin/stream and receive the identical global M64 matter/contact
update.

The executable constructs and tests the exact local factors and signal block,
but it does **not** materialize the complete 455-rail clock unitary or feed its
actual clock/reservoir/directional failure space through the receiver.  Its
16-rail square-root completion is only a minimal code-space diagnostic.
Therefore Route C, like Route A, is an abstract local-factor/block-encoding
upper bound with a named placement/completion wall.  It cannot receive a
literal bounded-local or full-decisive disposition in this cycle.

The three defect positions, angle, phase, 64 layers, clock labels, and
geometry-sector block remain supplied.  A spectral phase is not energy or a
rate, filter depth is not time, and the signal is not called a prepared
dressed eigenstate.

## Frozen acceptance and deletion contract

The runner must report, without held tuning:

1. exact dependency hashes and the rank of both declared carrier codes;
2. ambient and code-restricted singular values, with every signal contraction
   checked before forming a completion;
3. input/output Gram, signal-block E/G, full-isometry E/G, adjoint inverse,
   signal leakage, and completion norm;
4. all 16 carrier-code basis columns, a selected span of two actual nonzero
   coordinates in the 216-by-18 M64 payload, and complex coherent
   superpositions, including interference-linearity and no-cloning diagnostics;
5. a zero-mode refusal where required and malformed geometry/code/route
   refusals;
6. deletions of source projection, one solver layer/power, completion,
   receiver, field stream, packet stream, and global matter factor; contact
   must be reported as an exact spectator on the declared restricted
   one-particle auxiliary code, while the independent Cycle230 two-particle
   seam must retain a nontrivial contact deletion;
7. carried covariance under all 24 proper-cubic frames for all 16 carrier
   columns, including Route B's basis-label conjugacy and explicit body-frame
   Hamiltonian-line manifest; this is signal-operator/body-frame covariance,
   not a homogeneous cubic schedule;
8. the unchanged Cycle219 one-particle mass fixture and nontrivial Cycle230
   contact fixture;
9. raw physical signal packet rows, inherited unscaled Cycle495 rows, any
   diagnostic inverse scale kept in a separate field, and the Cycle230 seam
   block; and
10. M2, gate, depth, coefficient, memory, compile-time host-operation, and
    update-time host-operation inventories.

Passing E/G does not make the response gravity.  The bounded weak-field far
shore still supplies the candidate variational action, density readout,
Green-law selection, lattice units, and receiver functional.  There is no
physical `G_Newton`, stress-energy tensor, nonlinear backreaction, metric,
proper-time calibration, occurrence law, Record, or Born interpretation.

## Supplied / derived / open boundary frozen in advance

Supplied: periodic `L13`; train/held quadrupole positions and direct-sum
sectors; Cycle216/Jacobi, Q48/Chebyshev, and Cycle425/filter candidate laws;
all depths, phases, word/clock labels, Fourier/kernel and Givens coefficients;
the rank-16 source-code declaration; blank auxiliary rails; Hamiltonian-line
routing and compilation order; Cycle491 receiver, packet, occupations,
targets, tolerances, and readout; and all source/matter preparation.

Derived here if the tests pass: a payload-linear signal map tensored with
identity on all 3,888 M64 coordinates; one explicit Route-B physical
completion channel plus diagnostic minimal completions for A/C; code-space
E/G and inverse; exact finite Givens upper bound for the unscaled Chebyshev map;
abstract local-factor/LCU manifests for the normalized Jacobi and filter signals;
all-24 carried covariance; and packet/deletion/resource residuals.

Open regardless of a positive bounded compiler: selection of a solver law;
retirement of supplied clocks, coefficients, geometry sectors, and programs;
a homogeneous recurrent unscaled Jacobi/Chebyshev amplitude mechanism;
autonomous source renewal and conservation; noise/fault tolerance and
large-volume scaling; mass/stress normalization; asymptotic/continuum control;
physical coupling and duration; nonlinear gravity/backreaction; operational
records, occurrence, Born probability, and realized history.

## No-Go Discipline gate frozen in advance

No broad impossibility, minimum-content, shared-obstruction, or axiom-pressure
claim is licensed.  Full N1-N8 is mandatory because the result will be
bounded with named walls.

### N1 — normalized alternative families

| normalized family | object / mechanism / terminal obligation | status before outputs |
|---|---|---|
| local Jacobi block encoding | periodic scalar carrier / clocked products of normalized adjacency / local solver signal | ATTEMPTED HERE |
| finite Stinespring/Givens | declared Cycle491 carrier code / dense code isometry and NN routing / unscaled payload map | ATTEMPTED HERE |
| local reservoir-filter LCU | Q1 reservoir/field carrier / clocked Cycle425 powers / physical filter signal | ATTEMPTED HERE |
| reversible multigrid | nested signed fields / restriction-prolongation / scale-stable local response | OPEN — NOT ATTEMPTED |
| reduction-tree Krylov/CG | local words plus reductions / residual-controlled solve / unscaled arbitrary source | OPEN — NOT ATTEMPTED |
| gauge/link mediator | link registers / autonomous recurrent exchange / conserved source response | OPEN — NOT ATTEMPTED |
| direct scattering/exchange | two-body sector / on-shell phase / calibrated interaction | OPEN — NOT ATTEMPTED |
| operational instrument | source, clock, receiver, records / calibrated intervention / realized discriminator | OPEN — NOT ATTEMPTED |

### N2 — wall-independence audit

Collapse the live walls to `Wa` arbitrary-input unscaled local amplitude,
`Wp` autonomous program/coefficient preparation, `Ws` source conservation and
mass/stress meaning, `Wt` physical duration/coupling, `Wi` infrared/continuum
control, and `Wo` operational occurrence.  Every one of the 15 pairs remains
independent here: closing either member does not close the other.  In
particular, a finite Givens compiler does not select a law; a local block
encoding does not supply its inverse amplitude; source calibration does not
derive time; time does not prove an infrared law; and an infrared law does
not create Records.

### N3 — hidden-wall scan

The load-bearing imports are explicit: finite torus, zero-mode convention,
three source positions, geometry sector, source-code SVD/basis convention,
uniform coin projection, solver choice and depth, clock initialization and
label order, fresh local histories, phase, completion rail, Hamiltonian path,
Fourier/kernel/Givens coefficients, QR order, exact arithmetic, blank work,
receiver factors, occupations, packet functional, targets, tolerances, and
host diagnostic readout.  `Physical completion` means payload-carrying M2
rails with identical matter/contact action, not a host-added scalar norm.

### N4 — residual matching

| witness | exact residual addressed here | not matched here |
|---|---|---|
| Cycle495 runner, `raw_fields` / `completed_state` | host matrix-payload convolution and host scalar completion | source-law selection or gravity |
| Cycle491 runner, `split_compiled` | actual signed M64 scalar payload and receiver shell | autonomous source renewal |
| Cycle460 runner, adjacent QR compiler | bounded finite signed-amplitude isometry and inverse | homogeneous cubic recurrence |
| Cycle479/467/470 | local divide-six law, arithmetic, and one-star routing provenance | amplitude block normalization and recurrent shell |
| Cycle425 runner | local coin/vertex/stream factors and covariance | physical filter-clock preparation before this cycle |
| weak-field/source far shore | response/source interface vocabulary | `G_Newton`, stress tensor, nonlinear metric, empirical gravity |

### N5 — rhetoric audit

Evidence is restricted to periodic L13, two supplied geometry sectors,
rank-16 source carrier codes, depth 96/64, exact payload-linear maps, and four
receiver updates.  `Signal block` is not deterministic output; `diagnostic
inverse scale` is not a physical amplifier; `finite NN routed` is not
homogeneous or constant-overhead; response is not gravity; wrapped phase is
not energy; a generator element is not a rate; clock depth is not time; norm
weight is not probability; and an auxiliary payload rail is not a Record.

### N6 — partial-closure path scan

Positive partial paths need no axiom edit: synthesize a locally normalized
QSVT/resolvent, add reversible multigrid or reductions, replace direct-sum
geometry programs by a homogeneous mediator, compile coefficient/clock
preparation, add recurrent source conservation, then test asymptotic and
operational surfaces independently.

### N7 — hostile steelman

A hostile reviewer should demand one homogeneous local unitary whose
deterministic code-space action produces the unscaled Cycle216 response for
arbitrary lawful sources, with no geometry block, dense coefficient program,
postselection, or inverse-scale readout.  They should require an explicit
source-conserving recurrence, controlled large-distance law, physical clock
and coupling calibration, and an operational receiver.  A decisive next
construction is a locally normalized QSVT or reversible multigrid solver
whose success rail is coherently reused inside the receiver rather than
renormalized by a host.

### N8 — cross-cycle echo and claim gate

Cycles 425, 460, 463–479, 490–491, and 495 repeatedly show that local
arithmetic, routing, finite isometries, source actuation, and packet response
close different residuals.  Cycle460's positive-weight Givens schedule does
not settle signed amplitudes; Cycle467/470 word arithmetic does not settle
amplitude synthesis; Cycle495's solver profiles do not settle preparation.
Conversely, any Cycle499 positive route defeats a substrate-wide compiler
no-go.  Therefore broad no-go: FAIL; minimum-content claim: FAIL; shared
obstruction: FAIL; axiom pressure: FAIL.  There is no axiom pressure.

## Frozen reproduction envelope

The runner must finish below 1,200 seconds and 3,072 MiB process RSS.  Its
expected success token will be
`PHYSICAL_M64_PAYLOAD_SOLVER_COMPILER_TOURNAMENT_CYCLE499_CERTIFIED` only if
all bounded claims and all explicit negative dispositions pass.  Authority
remains none and audit remains unset.  No protected framework surface is
changed.

## First-cold-run disclosure and bounded contract correction

The first immutable full cold run of runner SHA
`62a1751ebb6df12cc4d1e6a8412ae5fe67f35ab95ad9b00af588968090b924fc`
returned `15 PASS / 1 FAIL`.  Its external transcript SHA256 is
`42636f0aeb5bcab3e99ddccf53d5cb5ca8cdc7b50588a74babd47f146f75e463`.
The sole failed assertion demanded a nonzero contact deletion on an
auxiliary matrix selected inside the declared 216-by-18 restricted
one-particle payload code.  The deterministic follow-up scan selected column
zero and again returned zero because **every** restricted source/receiver
contact column is the identity on this code.

This exposed an incorrect acceptance claim, not a failed physical contact
factor.  The revised runner reports

```text
||source_contact - I_216|| = 0,
||receiver_contact - I_18|| = 0,
auxiliary completion contact residual = 0,
```

and separately retains the actual Cycle230 two-particle seam with 645
nontrivial columns and deletion signal `0.36789306705608243`.  Route B's
completion receives the same restricted contact factor as its signal, but
this demonstrates exact spectator carriage only; it does **not** demonstrate
a nontrivial contact action on Route-B auxiliary rails.  No gate, route,
scale, code, tolerance, prediction, disposition, or scientific terminal was
changed by this correction.  Route C wording was also aligned with its
already-frozen demotion to an abstract local-factor/filter diagnostic rather
than an executed clock-rail compiler.

Frozen runner SHA256: f3478bd7253f2f72c6bda4cb4f78f6267576820a0f703c791809b464703c892c

## Accepted refrozen result

The accepted full cold replay returned

```text
SUMMARY {'pass': 16, 'fail': 0}
RESULT PHYSICAL_M64_PAYLOAD_SOLVER_COMPILER_TOURNAMENT_CYCLE499_CERTIFIED
```

The exact artifact and replay identities are:

```text
runner SHA256     f3478bd7253f2f72c6bda4cb4f78f6267576820a0f703c791809b464703c892c
transcript SHA256 f8cee3a0d9b463e4ec78e5117990fdce1ed6ae86a06453b9a86882e1b285955a
```

The runner body took `571.0968123750063 s` and reported
`2670.78125 MiB` maximum RSS.  External `/usr/bin/time -l` reported
`656.91 s` real, `569.36 s` user, `52.43 s` system,
`2,800,517,120` bytes maximum resident set, `6,185,391,072` bytes peak
footprint, and zero swaps.  Both the 1,200-second and 3,072-MiB runner caps
passed.

### Strongest constructive result — Route B

Route B is the strongest physical compiler produced.  On each frozen
rank-16 Cycle491 carrier-code block it maps the complete signed complex
216-by-18 matrix payload through the unscaled Q48/Chebyshev64 response and a
coherent square-root completion.  It queries zero payload rows and performs
zero update-time host solves.  Multiple carrier columns, two actual nonzero
M64 coordinates, and coherent superpositions preserve norms and overlaps;
the minimum no-cloning overlap gap is approximately `0.25`.

| block | physical M2 modes | adjacent Givens/phases | E/G | inverse | signal E/G |
|---|---:|---:|---:|---:|---:|
| train `a=1` | 13,198 | 284,043 | `5.2290514189455264e-14` | `4.148839075136603e-14` | `9.058368820736697e-15` |
| held `a=2` | 13,198 | 284,034 | `1.2853941315047637e-14` | `1.4642753329113793e-14` | `1.0537277944079071e-14` |

The total is **568,077 adjacent Givens/onsite phases**, with zero non-NN
gates in the supplied Hamiltonian-line embedding.  All 16 carrier columns
pass all 24 proper-cubic body-frame manifests; the maximum signal covariance
residual is `9.242371766729047e-16`.  This is one finite,
geometry-specific, compile-time QR upper bound.  It is not a homogeneous
cubic recurrence, not an arbitrary-spatial-source compiler, and not
constant-overhead scaling.

### Route dispositions and packet residuals

| route | constructive status | held stronger-`a2` order | maximum absolute packet residual | decisive success |
|---|---|---:|---:|---:|
| A — Jacobi96 | normalized `/48` signal algebra; exact small-cubic LCU block, but literal moving `6^96` history-register placement and actual failure rails open | pass | `6.655707852451509e-6` | no |
| B — Chebyshev64 | finite rank-16 signed-amplitude Stinespring/Givens compiler with physical completion | pass | `5.979595590024922e-6` | no |
| C — Cycle425 filter64 | abstract local-factor/filter signal diagnostic; complete 455-rail clock unitary and actual failure rails not materialized | fail | `6.6461691676372725e-6` | no |

All routes fail the frozen `5e-10` packet tolerance.  The exact physical
width shifts were:

| route | train unit | train coefficient-two | held unit | held coefficient-two |
|---|---:|---:|---:|---:|
| A | `2.0801693700889246e-11` | `1.0489649426848047e-10` | `5.8163154847967746e-11` | `2.9329867701211043e-10` |
| B | `4.79144663390052e-8` | `2.4161748397866223e-7` | `1.341362555196124e-7` | `6.764055611035991e-7` |
| C | `2.294436474148398e-9` | `1.1570126814963722e-8` | `1.9497505832077877e-9` | `9.831983491248586e-9` |

Route A's diagnostic inverse scale is exactly 48 and is never applied as a
physical gate or packet rescaling.  The unscaled ambient Jacobi and
Chebyshev norms are `12.783470439847218` and `13.095401027620056`, so neither
is a deterministic whole-mean-zero-domain signal block.  Their declared-code
signal maxima are bounded: Route B is `0.4973900951752628` train and
`0.7269728781519389` held.  Route C's maxima are `0.1687603804900771` and
`0.1647961032395428`.

### Completion, inverse, deletions, mass, and contact

Every finite code-space completion is receiver-active under the identical
restricted global matter factors.  Route B's completion norm weights are
`0.12070169319960788` train and `0.11480377893155817` held.  Maximum
field-isometry norm residual is `2.4369395390522186e-14`; maximum receiver
step/inverse residual is `7.616129948928574e-14`.

Deletion residuals are:

```text
receiver             0.0003600433690314089
field stream          0.09790533067526545
packet global matter  0.6666666666666614
completion            0.3474214921383076
Cycle425 vertex       0.1687603804900728
```

On the declared auxiliary one-particle code,

```text
||source_contact-I_216||             = 0
||receiver_contact-I_18||            = 0
auxiliary contact spectator residual = 0.
```

Thus Route B carries the same contact factor on signal and completion, but
that factor is a spectator at this resolution.  Independently, the inherited
Cycle230 two-particle seam retains 645 nontrivial columns and contact-deletion
signal `0.36789306705608243`.  The Cycle219 mass is
`0.4534056541748851` with eigen residual `3.534751832054436e-16`.

### Dependency-ledger effect

| wall | Cycle499 change | remaining import |
|---|---|---|
| `C_ref` | narrows representation compatibility: the signed Cycle491 M64 payload admits one exact finite linear compiler | solver choice, rank-16 code basis, both geometry sectors, QR coefficients, receiver and targets remain supplied |
| `C_num` | exact finite E/G/inverse/covariance residuals and structured-completion packet rows replace host norm injection | every route misses the `5e-10` packet target; no empirical gravity number or continuum error law is derived |
| `C_wrap` | unchanged | no phase is energy, no generator element is a rate, and depth is not physical time |
| `C_int` | narrows one transport seam: unknown coherent payload and completion both reach the existing receiver factors | no homogeneous selected interaction, source renewal, recoil/work closure, or calibrated coupling |
| `C_local` | materially narrowed for a finite declared code by 568,077 NN/onsite primitives; A/C signal factorizations are explicit | Route B is dense and geometry-specific; A/C literal moving registers and actual failure rails remain open; no constant-overhead recurrent compiler |
| `C_source` | narrows matrix-amplitude carriage without cloning or row injection | source normalization, conservation, recurrence, energy/stress identity, asymptotics, backreaction, and metric remain open |

A conservative Cycle499-only maturity ledger is operational quantum/records
`2.5/5`, causal time `2.4/5`, inertia/matter `2.5/5`, gravity/source/resources
`2.4/5`, and Born/probability/realized history `2.0/5`.  Only the finite
source/resource compiler evidence moves; no gravity, time, Record, or Born
terminal closes.

### Shared obstruction and next campaign

There is **no shared obstruction and no axiom pressure**.  Route B proves
that the finite signed amplitude map is compatible with ordinary unitary M2
execution on the declared code, defeating a substrate-wide compiler no-go.
Its dense geometry program does not answer the bounded-local constant-
overhead question.  A/C expose different unfinished placement/completion
tasks, not one route-independent wall.  Full N1–N8 therefore leaves broad
no-go, minimum-content, shared-obstruction, and axiom-pressure claims failed.

The optimal next gravity/source compiler campaign is a literal locally
normalized QSVT/resolvent or reversible-multigrid route whose **actual**
failure rails are coherently reused inside the receiver, with arbitrary
lawful zero-mean spatial inputs, no geometry-sector QR program, and a
homogeneous bounded-local schedule.  It should preserve the present all-16
payload, inverse, deletion, all-24, mass/contact, packet, and resource
controls.  Only after that implementation wall closes should source
conservation/mass-stress calibration and infrared scaling be tested; neither
is implied by this finite compiler.
