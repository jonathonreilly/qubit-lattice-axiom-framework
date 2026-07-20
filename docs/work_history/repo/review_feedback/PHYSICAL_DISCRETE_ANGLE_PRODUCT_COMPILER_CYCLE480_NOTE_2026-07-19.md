# Physical discrete-angle/product compiler — Cycle 480

Date: 2026-07-19

Authority: none

Audit: unset

Constitutional effect: none. No axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit-status surface is edited.

Companion runner:

```text
scripts/physical_discrete_angle_product_compiler_cycle480_2026_07_19.py
```

Contract shorthand: the angle set, basis precision, both route formulas, and
training-only selection rule are **frozen before held-row evaluation**.

Frozen Cycle-476 runner SHA-256:
`2cb747b912ed92d6d19e067de9780e0a5899d3659d8defc2135612346cfd0963`.

## Result up front

Cycle 480 removes Cycle 476's runtime continuous-angle service for its local
q1 response schedule. It selects the one finite dyadic physical gate basis

```text
B20 = {NOT, CNOT, Toffoli, H, Z20, Z20^-1},
Z20 = Rz(2 pi / 2^20),
```

and replaces every `Rz(phi)` by a bounded integer repetition of `Z20` or its
inverse. The basis is supplied: this result neither derives its calibration
nor asserts that exponent 20 or this gate vocabulary is fundamental or
optimal. The emitted schedule uses coefficient M2 bits as physical controls
and has no runtime angle oracle, lookup call, parity service, or host-side
choice. `H`, NCT, and `Z20` calibration are explicit inputs.

The exact Cycle-476 direct route and a predeclared fourth-order Suzuki route
are both compiled. The training-only rule selects the route with the smaller
maximum intrinsic residual before any held residual is read; the resulting
choice is then locked. That rule selects **Suzuki4**: its training maximum
intrinsic state residual is `1.9080216797967914e-05`, versus
`7.98149044671803e-05` for direct Strang8. Every reported error keeps **coefficient quantization,
product-formula error, and discrete-angle synthesis error** distinct. State
and full 448-dimensional operator controls, exact adjoint return, held word
rows, deletions, capacity, and all 24 proper-cubic frames are executed.

Across all fourteen rows, Suzuki4 lowers the maximum product residual from
`6.838309239442313e-05` to `9.065620006515406e-06` and the maximum intrinsic
discrete residual from `9.482014065923607e-05` to
`1.991204285589438e-05`. It is not cheaper: its large positive and negative
substeps require `107,561,472` phase quanta versus `46,445,568` for direct
Strang8. Both routes succeed, exposing a real error-versus-gate-count tradeoff
rather than a necessity claim.

This is a positive bounded compiler result, not an exact-law selection. Phase
is not physical energy, a circuit or product ordinal is not a physical clock,
and the local response is not promoted to a force, occurrence law, Record, or
Born rule.

## Exact target contract

### Target statement

Given the six ten-bit `P=8` coefficient words produced by Cycle 476, compile
each coefficient-bit-controlled pair rotation in either of two frozen local
q1 schedules into the discrete basis `B20`, preserving the declared code
space and carried proper-cubic schedule. For compiled map `D_route(A)`, test

```text
D_route(A) ~= exp(i theta sum_d (A_d/256) H_d)
```

while retaining separate observables for coefficient, product, and angle
errors. The inverse is not a reset: the exact inverse convention is reverse
every emitted gate and replace every `Z20` by `Z20^-1` and conversely; H, NOT,
CNOT, and Toffoli are self-inverse.

### Domain and completion witness

The lawful input is exactly six unsigned ten-bit computational-basis words.
The direction order is one permutation of six lanes and the physical basis
has exponent 20. Wrong word count, negative or overflowing coefficient,
duplicate/missing direction, unknown route, and precision mismatch are
refused. All-zero coefficients must give the exact identity.

Completion requires:

1. one explicit finite basis and exact integer sequences for every frozen
   target angle;
2. bounded gate, support, auxiliary, and one-supercell capacity counts;
3. literal local state and operator residuals, with exact inverse and leakage
   controls;
4. training-only selection and no post-held optimization;
5. held-size, deletion, lawful-domain, and all-24 carried-schedule controls;
   and
6. an explicit supplied/derived/open inventory.

A small residual alone does not select the basis as physics, close the
augmented whole-layer schedule, establish a uniform theorem over every
249-bit input tuple, or extend the response beyond the local q1 block.

## Frozen angles and discrete physical basis

Cycle 476's eight-step symmetric route has ten positive onsite magnitudes

```text
alpha_j = theta 2^j / (16*256),  j=0,...,9,
theta = 0.3627245233399082.
```

They range from `theta/4096` to `theta/8`. Signs are supplied by the signed
source pair and inverse convention; they do not add calibrated magnitudes.
Cycle 480 freezes these ten values as module constants before loading any word
row.

The comparison route is the standard symmetric fourth-order composition

```text
S4(h) = S2(p h) S2(p h) S2(q h) S2(p h) S2(p h),
p = 1/(4 - 4^(1/3)),
q = 1 - 4p.
```

Its twenty signed bit targets, with multipliers `8p` and `8q` relative to the
Cycle-476 `alpha_j`, are also frozen before row evaluation. Thus the complete
calibration set has thirty listed route targets. No angle or precision is
changed after a held residual.

For every target `phi`, compilation is

```text
m(phi) = sign(phi) floor(|phi|/delta + 1/2),
delta = 2 pi / 2^20,
Rz(phi) -> Z20^m(phi).
```

No half tie occurs. Therefore

```text
|m delta - phi| <= delta/2.
```

The exact onsite operator error is

```text
||Rz(phi)-Rz(m delta)||_2 = 2 sin(|phi-m delta|/4),
```

and the signed-X pair-rotation error is `2 sin(|phi-m delta|/2)`. Repetition
can be long, but it is finite, constant for this compiler, contains no runtime
real-number operation, and consumes no new auxiliary M2.

## Two frozen product routes

### Direct angle approximation: Cycle-476 Strang8

The direct route preserves Cycle 476 literally:

```text
D8(A) = [prod_(d=0)^5 exp(i theta A_d H_d/(16*256))
         prod_(d=5)^0 exp(i theta A_d H_d/(16*256))]^8.
```

Each directional factor is split exactly across active coefficient bits, then
each bit angle is replaced by its nearest `Z20` word. Same-direction signed-X
blocks commute; the runner combines them only for fast matrix evaluation, not
for gate accounting.

### Higher-order alternative: Suzuki4

The comparison uses one five-block fourth-order composition at the full target
angle. It has ten directional half-passes rather than the direct route's
sixteen. Its negative `q` block is implemented with inverse phase words; its
adjoint reverses all ten passes and changes every quantum sign. This is a
route-level product comparison on the same basis, not an after-the-fact fit.

The selection rule is written before fixture evaluation:

```text
choose the lower maximum training intrinsic residual
||D_route - exp(i theta sum_d A_d H_d/256)||;
break a tie in the declared route order;
lock before held readout.
```

Both routes remain reported on every row regardless of the selected result.

## Physical decomposition and accounting

Cycle 476 proves that each direction has sixteen disjoint signed source pairs,
ninety-six pairs across six directions. Every coefficient-bit pair rotation
uses the existing Gray path, twelve clean controls, and

```text
H, Rz(-phi), CNOT, Rz(phi), CNOT, H.
```

Cycle 480 changes only each `Rz` word. It adds no wire, no routing service, and
no support. Both routes therefore retain 12 clean rotation auxiliaries and
**26-M2 support**. Starting from Cycle 476's composed placement, occupancy
remains `48,357 < 64,000` M2 in one scale-40 supercell. This is a local
capacity result; the augmented Cycle-476/Cycle-477 whole layer is not composed
here.

The direct route contains 15,360 coefficient-controlled pair rotations; the
Suzuki route contains 9,600. Structural H/NCT and repeated-`Z20` counts are
computed from the complete frozen manifest rather than from active fixture
bits. Consequently they describe the coherent controlled compiler, not a
classically pruned execution on one word row.

| route | pair rotations | Toffoli | CNOT | NOT | H | `Z20` or inverse | total discrete gates | manifest |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| direct Strang8 | `15,360` | `2,304,000` | `30,720` | `1,889,280` | `30,720` | `46,445,568` | `50,700,288` | `5281f3ae...e99ca` |
| Suzuki4 | `9,600` | `1,440,000` | `19,200` | `1,180,800` | `19,200` | `107,561,472` | `110,220,672` | `c8f26008...fc61e` |

The immutable thirty-target angle manifest is
`25f41f997da4a711de5343fd74239202fed7607d865656eb69adee4d4767276c`.
The maximum frozen signed target error is `2.754130464440894e-06`, below
`delta/2 = 2.996056226339143e-06`; the corresponding maximum pair-rotation
operator error is `2.754130464440024e-06`.

## Executable residuals

The runner evaluates all fourteen Cycle-472 word rows, including every held
off-axis and boundary geometry, using three deterministic normalized q1 probe
states. For one training and one held representative it also constructs the
complete 448-by-448 operators and measures spectral two-norm residuals.

For each route it reports four separate quantities:

```text
C_num   = ||U(exact coefficient)-U(P=8 coefficient)||,
C_prod  = ||continuous product-U(P=8 coefficient)||,
C_angle = ||discrete product-continuous product||,
C_total = ||discrete product-U(exact coefficient)||.
```

`C_total` is measured directly rather than inferred by adding the other three.
No cancellation is used to relabel one error as another. Exact inverse return,
q1 norm preservation, and operator unitarity are tested independently.

### State residual summary over all fourteen rows

| observable | direct Strang8 maximum | Suzuki4 maximum |
|---|---:|---:|
| product formula vs exact `P=8` target | `6.838309239442313e-05` | `9.065620006515406e-06` |
| discrete angle vs continuous product | `6.971440007602758e-05` | `2.2174169685011926e-05` |
| intrinsic discrete product vs exact `P=8` target | `9.482014065923607e-05` | `1.991204285589438e-05` |
| total vs exact unquantized-coefficient target | `0.0011351987204342787` | `0.0011460621750004692` |
| exact adjoint return | `7.554413953590242e-16` | `7.799174254744412e-16` |
| q1 norm leakage | `2.220446049250313e-16` | `0.0` |

The maximum coefficient-quantization state residual is
`0.0011296176321004602`. It dominates the total column and can cancel or add
against a route residual; this is why the frozen training selection uses the
intrinsic column rather than the total column. The held results do not change
the selected route or exponent.

### Complete-operator representatives

| representative | term | direct Strang8 | Suzuki4 |
|---|---|---:|---:|
| training adjacent | product | `1.88738867595268e-04` | `3.2993181564808985e-05` |
| training adjacent | angle | `6.365952268872528e-05` | `2.5074612727072616e-05` |
| training adjacent | intrinsic | `1.700953398843104e-04` | `4.0534297510757514e-05` |
| training adjacent | total | `9.68937718990619e-04` | `8.888059165149963e-04` |
| held off-axis | product | `1.9501835308984692e-04` | `2.762127359271507e-05` |
| held off-axis | angle | `4.474834779073499e-05` | `4.5413248788282124e-05` |
| held off-axis | intrinsic | `1.5365685384334472e-04` | `4.1979069208017e-05` |
| held off-axis | total | `2.174578510174911e-04` | `1.5628775847245863e-04` |

These are spectral two-norms of literal `448 x 448` matrices. The largest
unitarity residual is `2.224032786022276e-15`. The coefficient-quantization
operator residuals for the same representatives are
`8.718381495067757e-04` and `1.2227032794217188e-04`.

## Proper-cubic covariance

The discrete basis is onsite/nearest-neighbor and direction blind. Under each
proper-cubic frame, Cycle 480 carries together:

- six coefficient lanes;
- the matter and field direction bits;
- the signed source pairs;
- the entire forward/reverse direction list;
- every Suzuki scale position, including the negative central block; and
- every fixed phase word and its inverse convention.

The carried list is not re-sorted against a global axis. All 24 proper-cubic
frames are tested on a held word row. Covariance of a carried target-relative
schedule does not derive the schedule or promote its serial order to a
preferred physical ordering.

## Deletions and lawful-domain controls

The executable deletes independently:

1. one `Z20` quantum from one emitted factor;
2. the full schedule contribution of one active coefficient bit; and
3. one symmetric directional factor.

All three changes must produce a state residual above the declared signal
floor. Both routes must be exactly identity on the all-zero coefficient code.
Six malformed domains are refused. These are controls for the declared
compiler, not claims that its basis, precision, or schedule is necessary.

| deletion/control | residual |
|---|---:|
| one `Z20` quantum | `1.5463940309641876e-06` |
| one active coefficient-bit family | `3.588945174261862e-04` |
| one symmetric directional factor | `2.719157006925245e-02` |
| all-zero direct / Suzuki identity | `0.0 / 0.0` |
| malformed domains refused | `6 / 6` |

## Prior art and novelty boundary

Dyadic phase grids, repeated fixed rotations, Gray-path two-level synthesis,
clean-ancilla multi-control ladders, Strang splitting, and fourth-order Suzuki
composition are established methods. Cycle 480 claims no invention or
optimality for them, no fault-tolerance threshold, and no shortest phase word.

Cycle 476 supplied the exact reversible word-to-`P=8` coefficient circuit and
the continuous-angle Strang8 source schedule. Cycle 477 independently supplied
complete final-word delivery/return for its declared full layer while leaving
the enlarged arithmetic/response composition and discrete angles open. The
new result is the bounded executable composition at the narrower Cycle-476
angle wall: a literal single-basis phase-word compiler, an orthogonal
higher-order product comparison, and separated state/operator errors under
held, deletion, inverse, capacity, and all-24 controls.

It does not claim to be the first Hamiltonian-simulation or rotation-synthesis
construction, and it does not compose a whole layer.

## Supplied, derived, and open inventory

Supplied:

1. Cycle 476's six ten-bit coefficient words, `P=8` floor rule, and all-zero
   code;
2. the Cycle-426 local q1 signed source-pair generator, response angle,
   fermion convention, and code basis;
3. exact NOT, CNOT, Toffoli, and H plus calibrated `Z20` and `Z20^-1`;
4. phase exponent 20 and symmetric nearest-integer rounding;
5. target-relative direction order and the two predeclared product formulas;
6. blank clean controls, one-supercell placement, fixture split, tolerances,
   and readout norms.

Derived and executed:

1. the ten Cycle-476 targets and twenty Suzuki comparison targets, with one
   immutable manifest digest;
2. bounded integer `Z20` or inverse words for all thirty targets;
3. complete direct and higher-order structural/phase gate counts;
4. exact inverse convention, no added angle auxiliary, and retained 26-M2
   support;
5. separate coefficient, product, angle, intrinsic, and total state/operator
   residuals;
6. training-only selection plus held word rows, deletion, all-zero, malformed,
   capacity, and all-24 controls.

Open:

1. a physical selection or derivation of `B20`, exponent 20, and its
   calibration;
2. fault/noise thresholds, optimal synthesis, and a uniform analytic error
   theorem over every lawful input word;
3. exact coefficient-controlled small-block/Givens, phase-gradient kickback,
   Clifford-plus-T, qubitization/QSP, and randomized alternatives;
4. local q greater than one and recurrent response/source behavior;
5. the augmented Cycle-476/Cycle-477 full-layer coloring and execution;
6. autonomous law/preparation selection, operational occurrence, continuum
   control, and physical calibration.

## TOE dependency ledger

| wall | Cycle-480 change | remaining import |
|---|---|---|
| `C_ref` | one finite basis, inverse convention, and immutable angle manifest replace a runtime angle oracle | basis/precision/calibration and product-route selection remain supplied candidate-law choices |
| `C_num` | every frozen target has an exact integer phase word and explicit operator error | Cycle-476 `P=8` coefficient choice, physical units/reference, and uniform all-word theorem remain open |
| `C_wrap` | unchanged; phase-grid and product indices are compiler labels only | no physical clock or wrapping interpretation is derived |
| `C_int` | materially narrowed: both direct and fourth-order local products now have literal discrete gates and separated errors | response-law selection, q greater than one, recurrence, and physical calibration remain open |
| `C_local` | narrowed at the Cycle-476 angle surface: no added work M2, 26-M2 support, exact counts, capacity, inverse, deletion, held, and all-24 controls | augmented whole-layer composition, fault control, and optimized routing remain open |
| `C_source` | the already-physical coefficient bits now control fixed primitive words without a host angle service | coefficient/source meaning, conservation, recurrence, and calibration remain supplied/open |

No wall is declared universally closed and no pair collapses.

## Full no-go discipline

The current no-go-discipline skill was refreshed from `origin/main`; the
normalized family key and proof-search governance are applied. This positive
probe makes no impossibility, minimum-content, shared-obstruction, or axiom
claim, but full N1-N8 is still recorded before shipping.

### N1 — Alternative route enumeration

| normalized family | object / mechanism / terminal obligation | status |
|---|---|---|
| dyadic direct Strang8 | ten Cycle-476 angles / nearest repeated `Z20` / bounded discrete version of the retained schedule | **ATTEMPTED — SUCCEEDS** |
| dyadic fourth-order Suzuki | thirty predeclared targets / five symmetric S2 blocks / lower product residual on the same basis | **ATTEMPTED — SUCCEEDS** |
| Clifford-plus-T | each frozen single-qubit rotation / arithmetic synthesis words / selected fault-tolerant finite basis | **OPEN — NOT ATTEMPTED** |
| phase-gradient kickback | angle integer plus phase-gradient register / modular add and uncompute / coherent bounded rotation | **OPEN — NOT ATTEMPTED** |
| exact controlled Givens | small signed-star components / coherent norm and Givens arithmetic / exact quantized local exponential | **OPEN — NOT ATTEMPTED** |
| qubitization or QSP | block encoding of the local generator / signal polynomial / uniform response approximation | **OPEN — NOT ATTEMPTED** |
| randomized or multi-product formula | same local generator / randomized cancellation or linear combination / alternative product bound | **OPEN — NOT ATTEMPTED** |
| alternative finite calibration basis | local M2 gates / different discrete phase vocabulary / lower physical cost at fixed error | **OPEN — NOT ATTEMPTED** |

These families differ in primary object, load-bearing mechanism, and terminal
obligation. Success of the two dyadic families cannot establish their
necessity or exclude the six live alternatives.

### N2 — Wall-independence audit

`Wc`, coefficient precision; `Wp`, product formula/order; `Wa`, primitive
angle basis/synthesis; `Wl`, augmented whole-layer composition; `Wq`, larger
q/recurrent response; `Wk`, physical calibration; and `Wo`, operational
occurrence are independent. A finer coefficient does not select a product
formula. A higher product order does not synthesize its angles. A finite gate
basis does not color the whole layer or extend q. None of those supplies
recurrence, calibration, or occurrence.

### N3 — Hidden-wall scan

Explicit supplied structure includes six populated coefficient words, `P=8`,
floor and zero conventions, the dimensionless response angle, fermion signs,
exact H/NCT gates, calibrated `Z20`, phase exponent 20, nearest rounding,
clean controls, serial target-relative direction order, fourth-order
coefficients, fixture split, error norms, capacity placement, and an omitted
fault model. “Discrete” does not mean derived or selected by the substrate.

### N4 — Residual matching

Cycle 476 names primitive onsite angle synthesis and product selection as open.
This probe matches that local q1 surface directly. Cycle 477 separately closes
final-word delivery for its declared layer but leaves the enlarged
weight/response composition open; Cycle 480 does not cite it as composed.
Larger-q, recurrent, continuum, occurrence, and weak-field ledgers require
different witnesses and are not claimed matched.

### N5 — Rhetoric audit

The tested resolutions are thirty frozen angles, ten-bit coefficients,
fourteen finite train/held word rows, a 448-dimensional q1 block, one
scale-40 supercell, and carried 24-frame schedules. Exactness is restricted to
integer phase words, inverse convention, and basis-gate accounting. No
lattice-wide exact exponential, optimal synthesis, law selection, physical
clock, force, Record, Born, or continuum claim is made.

### N6 — Partial-closure path scan

Repeated dyadic words constructively close the runtime angle service at fixed
precision; Suzuki composition constructively lowers the separate product
surface without changing coefficient precision. Exact controlled Givens,
phase kickback, Clifford-plus-T, qubitization, alternate bases, augmented
whole-layer coloring, and larger-q compilation remain live import-retirement
paths. None calls for axiom language.

### N7 — Hostile steelman

A hostile reviewer should reject any suggestion that `B20`, repeated phase
words, or Suzuki4 are fundamental or efficient. They can demand a physical
basis-selection law, calibrated fault model, analytic uniform error bound,
shorter Clifford-plus-T or phase-kickback words, coherent exact-small-block
arithmetic, and literal augmented-layer execution. Cycle 480 supplies a
bounded compiler witness, not those stronger results.

### N8 — Cross-cycle echo and claim gate

The required phrase and ledger search was repeated. Cycles 467, 470, and 474
turned arithmetic, delivery, and overlap imports into bounded constructions;
Cycle 476 did the same for fixed-precision word weighting and local control;
Cycle 477 independently closed final-response delivery at its declared layer
surface. Cycle 480 follows that constructive pattern for discrete angles and
a higher-order product comparison. Earlier route-local failures therefore do
not echo into a shared substrate obstruction.

Broad no-go: **FAIL**. Minimum-content claim: **FAIL**. Shared-obstruction
claim: **FAIL**. Axiom-pressure claim: **FAIL**. There is **no axiom pressure**.

## Disposition and next campaign

The runner is green and retains the finite-basis compiler as a bounded positive
closure of Cycle 476's runtime angle import. Preserve the training-selected
route and all residual columns; do not use held cancellation to select a new
precision or schedule.

The optimal next campaign is the still-unmade augmented physical layer:
compose Cycle 477's complete six-word delivery/return, Cycle 476's 3,444-wire
arithmetic/output block, coefficient-bit staging, Cycle 480's selected
discrete response words, exact reverse/uncompute, and enlarged conflict
coloring. In parallel, exact controlled small-star/Givens synthesis is the
highest-value independent attack on the remaining product and long-word cost.
Neither route licenses a minimum-content or axiom-pressure claim.

The verified run reports `RESULT pass=7 fail=0` and
`RESULT PHYSICAL_DISCRETE_ANGLE_PRODUCT_COMPILER_CERTIFIED`. Its final
synchronized controlled body takes `1.2054558329982683` seconds and peaks at
`694.5 MiB`; an independent complete cold process, including the inherited
import chain, takes `78.08` seconds. Both are inside the declared caps. Runner SHA-256:
`39f2fb1c9d3e10bf8741b6f426bc0a7dbbd75dea7c4c66aedc75b8d8275fb743`.
