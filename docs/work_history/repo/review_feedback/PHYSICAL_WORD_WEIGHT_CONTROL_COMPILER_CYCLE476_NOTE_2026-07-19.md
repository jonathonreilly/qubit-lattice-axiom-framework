# Physical word-weight/control compiler — Cycle 476

Date: 2026-07-19

Authority: none

Audit: unset

Constitutional effect: none. No axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit-status surface is edited.

Companion runner:

```text
scripts/physical_word_weight_control_compiler_cycle476_2026_07_19.py
```

Contract shorthand: exact inverse and work uncompute.

## Result up front

Cycle 476 supplies a bounded constructive primitive-law bridge from the six
249-bit neighbor words already present at Cycle-467 ports to a fixed-precision
control of the Cycle-426/Cycle-472 weighted even-CAR response.

For each direction `d`, it computes

```text
S = sum_d n_d,
A_d = floor(2^P sqrt(6 n_d/S)),
P = 8,
```

with an explicit all-zero code `S=0 -> A_d=0`. The six retained coefficient
registers have ten bits each. One complete reversible NCT circuit contains
`6,169,944` gates, uses 1,890 work M2, returns every work bit to zero, and has
an exact reverse circuit. Its fixed precision P=8 error obeys

```text
0 <= sqrt(6 n_d/S) - A_d/256 < 1/256
```

on every nonzero lawful row. The largest measured coefficient error across all
14 Cycle-472 train and held unseen word rows is
`0.0037624671720912772`, below `1/256 = 0.00390625`.

The output bits then control an explicit eight-step symmetric product formula
for the local q1 source-star sector. Each controlled two-level rotation is
decomposed to Gray-path multi-controlled X ladders, one multi-controlled local
rotation, two CNOTs, and onsite `H/Rz` rotations. The largest support is 26 M2.
The compiled product has exact adjoint return and zero q1 leakage. Its largest
measured residual from the exact exponential of the **quantized** generator is
`6.218643109354876e-05`; coefficient quantization contributes at most
`0.0010505454416850502` on the tested vectors. Both residuals are reported
separately.

This is the strongest positive result. It retires Cycle 472's explicit
word-to-weight/control implementation import at declared fixed precision for
one bounded local q1 response block. It does not select `P=8`, the floor rule,
the angle primitives, or the response law as fundamental physics. It does not
compose a whole relaxation layer, recurrent source dynamics, time, energy,
force, acceleration, probability, P2, or gravity.

## Exact target and lawful code

### Input and output

Input is six computational-basis unsigned words

```text
n_d in {0,...,2^249-1}, d=0,...,5,
```

already resident at the declared Cycle-467 port wires. Output is six blank
ten-M2 registers. Arithmetic work must begin blank. The lawful reversible map
is

```text
|n_0,...,n_5>|0_A>|0_work>
  -> |n_0,...,n_5>|A_0,...,A_5>|0_work>.
```

Malformed word count, negative values, 249-bit overflow, wrong direction, and
out-of-range padded arithmetic are refused. A nonblank output or work register
is outside the declared encoder domain. The inverse is the complete trace in
reverse and is not a reset operation.

### Fixed-point definition without division ambiguity

For `S>0`, `A_d` is equivalently the largest ten-bit integer satisfying

```text
A_d^2 S <= 6 n_d 2^(2P).
```

This comparison definition removes any intermediate rounding ambiguity. Since
`sqrt(6)*256 < 2^10`, every lawful output fits ten bits. For `S=0`, all input
words are zero and the declared output is six zero coefficients. This all-zero
code is tested literally, with zero work leakage.

`P=8`, truncation toward zero, and the all-zero convention are supplied
candidate-law/compiler choices. Other precisions or rounding modes are not
excluded.

## Complete reversible arithmetic

### Registers

The fixed circuit uses:

| register | M2 |
|---|---:|
| six input ports | `1,494` |
| six retained coefficient outputs | `60` |
| 252-bit total `S` | `252` |
| shared padded addend | `272` |
| shared controlled-add mask | `272` |
| candidate square | `20` |
| candidate-square times `S` | `272` |
| comparison target | `272` |
| equality prefix | `273` |
| nonzero prefix | `253` |
| carry/flags/MCX auxiliary | `4` |
| **work total** | **`1,890`** |
| **all logical ports/output/work wires** | **`3,444`** |

The 252-bit total cannot overflow because it is below `6*2^249 < 2^252`.
The 20-bit square contains every ten-bit candidate square. The 272-bit product
cannot overflow because it is below `2^20*2^252 = 2^272`.

### Gate construction

The circuit first adds all six words into `S` with the Cycle-467 Cuccaro
adder. A reversible OR prefix produces the `S != 0` flag. For each direction
and each candidate bit from most to least significant, it:

1. tentatively sets the output bit;
2. computes the candidate square by controlled shifted additions;
3. multiplies that square by `S` using 20 controlled shifted additions;
4. compares the product lexicographically with `6 n_d 2^(16)`;
5. ANDs the comparison with `S != 0`;
6. reverses the comparison, product, and square work;
7. retains the trial bit exactly when the predicate is true; and
8. clears the predicate flag from the retained bit.

A controlled add first Toffoli-loads the selected addend into a blank mask,
applies the unchanged Cycle-467 Cuccaro adder, and unloads the mask. The
lexicographic comparison constructs reversible equality prefixes using
three-control NOTs decomposed into three Toffolis with one clean auxiliary.
All target, prefix, total, mask, product, square, carry, and predicate work is
then reversed.

The full NCT transcript is:

| primitive | count |
|---|---:|
| NOT | `326,820` |
| CNOT | `2,749,056` |
| Toffoli | `3,094,068` |
| **total** | **`6,169,944`** |
| trace SHA-256 | `84402e1a70d8d1f7f38d6beb6af41e7d894505179d8f55c9c5f9d007cde2c4f3` |

The executable exhausts all `4^6=4,096` six-word inputs of a two-bit/fraction-
three model against a direct inequality search, with zero failures. It then
executes the complete 6.17-million-gate full-width circuit and inverse on one
training and one held row:

| row | expected/output coefficients | work leakage | inverse failures |
|---|---|---:|---:|
| train adjacent endpoint | `(0,450,218,218,218,218)` | `0` | `0` |
| held boundary endpoint | `(0,359,257,257,257,257)` | `0` | `0` |

All 14 actual Cycle-472 endpoint rows are independently checked against the
same exact integer definition, including the held off-axis `(2,2,0)`,
`(3,2,1)`, and `(1,1,1)` relative geometries. These all-row checks do not
replay six million gates 14 times; the two literal representatives and
exhaustive small-width certificate expose that performance distinction.

## Controlled source rotation

### Route falsified before the retained construction

The first route attempted exact factorization

```text
exp(i theta sum_d c_d H_d) ?= product_d exp(i theta c_d H_d).
```

It fails even on the local q1 star. The largest cross-direction commutator norm
is `2.8284271247461903`, the largest cross-direction product norm is `2.0`, and
a single directional pass differs from the exact quantized exponential by
about `5.3e-2` on the tested vectors. Reusing the same negative-angle order is
also not its inverse. This route-specific failure is retained as evidence for
the symmetric schedule; it is not a substrate obstruction or no-go.

### Eight-step symmetric product

Let `c_d=A_d/256`. Cycle 476 compiles

```text
U_8(c) = [
  product_(d=0)^5 exp(i theta c_d H_d/16)
  product_(d=5)^0 exp(i theta c_d H_d/16)
]^8.
```

The exact adjoint reverses every elementary factor and changes every angle
sign. The direction order is a supplied target-relative schedule. Under a
proper-cubic frame the six coefficient lanes and the entire ordered schedule
are carried together; the schedule is not re-sorted by a preferred global
axis.

Because rotations generated by the same `H_d` commute, each factor is further
split exactly by the ten binary coefficient bits:

```text
exp(i theta c_d H_d/16)
 = product_(j: A_d[j]=1)
     exp(i theta 2^j H_d/(16*256)).
```

Only the symmetric product between different directions is approximate.
Coefficient quantization and product-formula error are therefore separately
observable.

On three train/held probes, the residuals are:

| row | product formula vs exact quantized exponential | quantized vs exact coefficient exponential | adjoint inverse |
|---|---:|---:|---:|
| train adjacent | `5.929983821423026e-05` | `0.00040864642654518966` | `1.4045435895666439e-15` |
| held boundary | `6.218643109354876e-05` | `7.672279661862691e-05` | `1.050034224302645e-15` |
| held unseen off-axis | `5.7531490316618736e-05` | `0.0010505454416850502` | `2.2194175996419953e-15` |

Maximum q1 norm leakage is `2.220446049250313e-16`. The runner also checks
one-, two-, four-, and eight-step symmetric schedules and requires strict
residual decrease:

| symmetric steps | residual from exact quantized exponential |
|---:|---:|
| 1 | `0.0036961831133787734` |
| 2 | `0.0009213533694725851` |
| 4 | `0.00023016851386506684` |
| 8 | `5.7531490316618736e-05` |

This is finite executable convergence evidence, not a uniform product-formula
theorem.

### Physical two-level decomposition

Each direction generator contains 16 disjoint source/recoil basis pairs, 96
pairs total. A pair differs on four of the thirteen physical bits: two matter
directions, the reservoir bit, and one directional field bit.

For each coefficient bit and symmetric half-step, Cycle 476:

1. uses six 12-control Gray-path X operations to bring the pair to two basis
   states differing on one bit;
2. computes the AND of the other twelve basis conditions and the coefficient
   bit with a clean Toffoli ladder;
3. applies the two-M2 controlled rotation through
   `H, Rz(-phi), CNOT, Rz(phi), CNOT, H`;
4. uncomputes the AND ladder; and
5. reverses the Gray path.

The 12-control X uses `2*12-3=21` Toffolis. The 13-control rotation uses 24
Toffolis around the two-CNOT/onsite-rotation block. Negative controls are
implemented by surrounding NOTs. The complete eight-step manifest contains:

| item | count |
|---|---:|
| coefficient-controlled pair rotations | `15,360` |
| Toffoli | `2,304,000` |
| CNOT | `30,720` |
| NOT | `1,889,280` |
| onsite H | `30,720` |
| onsite Rz | `30,720` |
| clean rotation auxiliaries | `12 M2` |
| maximum local support | **`26 M2`** |
| manifest SHA-256 | `f8eebaaf506680d0e653362a707b24fb13d04901f05339d03fa59d5b2ee77810` |

The `H/Rz` angle calibration is supplied. The displayed decomposition reaches
onsite and nearest-neighbor two-M2 primitives; it does not claim a selected
fault-tolerant discrete gate set or an optimal rotation count.

## Physical placement and capacity

The arithmetic wires fit on the first 3,444 vertices of a Hamiltonian snake
inside one scale-40 physical-M2 supercell. Every NOT is onsite. Every CNOT and
Toffoli can be stably gathered by the same occupied-path SWAP construction used
by Cycle 467, then returned. This gives a constructive, deliberately loose
nearest-neighbor event upper bound of `184,577,059,128` and maximum supercell
diameter `117`. The upper bound is not an enumerated transcript or depth
optimum.

Starting from Cycle 470's existing 46,371-M2 active-supercell placement, the
new arithmetic/output wires beyond the six already-counted input ports plus
one 36-M2 Cycle-426 source cell add 1,986 M2:

```text
46,371 + 1,986 = 48,357 < 64,000.
```

For source actuation, one coefficient bit at a time is endpoint-staged to a
local control port beside the 13-M2 matter/source star and the twelve clean
rotation auxiliaries. The occupied path is restored after each coefficient
bit. The maximum live rotation neighborhood remains 26 M2.

Cycle470 is available prior art for one seven-supercell delivery block. Its
ingress/egress program is not replayed by this runner. **Inter-supercell
delivery is not replayed.** Cycle 474 separately
supplies a whole-layer mod-three schedule for the original Cycle-470 block.
Cycle 476 makes **no whole-layer composition claim** for the enlarged
delivery-plus-weight-plus-actuation block. Its augmented support/congestion
audit and a recurrent all-cell response schedule remain open.

## Proper-cubic covariance

The arithmetic map is symmetric under permutation of its six input/output
lanes. The sum is invariant, while each inequality/root result follows its
lane. On a held unseen word row, all 24 proper-cubic frames give exact integer
lane covariance with maximum residual `0`.

The runner carries every occupied Hamiltonian edge under all 24 affine
scale-40 frames, with zero adjacency failures. For the response block it also
carries:

- matter and field direction bits;
- coefficient lanes;
- source/recoil basis pairs and fermionic signs;
- the target-relative forward/reverse direction schedule; and
- every symmetric-product factor.

The maximum all-24 carried product-schedule residual is `0.0`. The carried
apparatus is covariant; the serial local-frame schedule is supplied and is not
claimed invariant without being carried.

## Deletions and lawful-domain controls

On the selected held boundary row:

| deletion | residual |
|---|---:|
| largest delivered neighbor word set to zero | `376.06515392947534` coefficient-register Euclidean units |
| one retained root trial segment | `104.0` coefficient-register units |
| one active controlled-rotation coefficient bit | `0.0014168925507746853` state norm |
| entire source coupling | `0.5031983598576016` state norm |

The runner refuses five malformed cases: wrong word count, negative word,
249-bit overflow, invalid padded placement, and invalid direction. The
all-zero input maps to all-zero output with zero leakage. These controls are
necessities of this declared route, not constitutional minima.

## Prior-art and novelty boundary

Reversible ripple addition, schoolbook multiplication, lexicographic
comparison, restoring square-root search, Gray-path two-level synthesis,
multi-control clean-ancilla ladders, and symmetric product formulas are
established techniques. Cycle 476 does not claim them as new and does not
claim optimal gate, work, precision, or depth counts.

Cycle 467 supplied a complete div-six NCT/nearest-neighbor circuit at six word
ports. Cycle 470 supplied bounded delivery into those ports for one serial
seven-supercell block. Cycle 426 supplied the physical hard-core recoil star.
Cycle 472 joined a dual-source relaxed field to a weighted generator but left
word normalization, square root, and controlled weighted exponential as
supplied implementation content.

The new repository result is the exact bounded composition at that residual:
a complete 249-bit word-to-fixed-coefficient NCT trace, exact inverse/cleanup,
strict coefficient error, and an explicit bit-controlled physical response
schedule with separated product-formula and quantization residuals. It is not
the first square-root circuit, Hamiltonian simulation, or controlled rotation,
and no global priority claim is made.

## Supplied, derived, and open inventory

Supplied:

1. six populated 249-bit Cycle-467 ports and blank output/work code;
2. precision `P=8`, ten output bits, floor convention, and all-zero convention;
3. Cuccaro/add-mask/multiply/compare/root order and serial lane order;
4. Cycle-426 local q1 matter/source-star law, angle, fermion ordering, and
   coefficient interpretation;
5. eight symmetric steps and the target-relative carried direction order;
6. onsite `H/Rz` primitives and their angle calibration;
7. Cycle-472 train/held word rows, finite probes, tolerances, and readouts; and
8. Cycle-470 placement/capacity as prior art, without consuming its whole
   delivery runner.

Derived and executed:

1. complete six-output NCT sum/nonzero/square/product/compare/root trace;
2. exact work uncompute and exact inverse on literal 249-bit representatives;
3. exhaustive small-width correctness and all-zero closure;
4. strict `2^-8` coefficient bound on all actual train/held rows;
5. falsification of naive exact directional factorization;
6. eight-step symmetric bit-controlled source schedule, exact adjoint, measured
   product/quantization residuals, and q1 leakage control;
7. explicit 15,360-rotation physical decomposition with 26-M2 support;
8. deletion, malformed-domain, capacity, and all-24 carried covariance
   controls.

Open:

1. selection of precision, rounding rule, product-formula order, and step
   count;
2. an analytic uniform product-formula error theorem or an exact full
   exponential synthesis;
3. synthesis of the onsite angles in a selected discrete/fault-tolerant gate
   set;
4. literal enumeration/optimization of the 184-billion-event arithmetic route;
5. Cycle-470 plus Cycle-476 whole-layer overlap, coloring, and recurrence;
6. local `q>1` response compilation and recurrent two-active-source dynamics;
7. physical source/mass/energy-stress calibration, duration, phase units,
   continuum/asymptotic control, or `G_Newton`; and
8. metric/lapse/curvature/gravity, operational instruments, occurrence,
   Records, Born weights, P2, or BMV.

Phase is not energy. A generator is not a rate. Iteration count is not time,
circuit depth is not time, and eight symmetric steps are not a duration.
Coherent norm is not probability. Pointer copying is not a Record.

## TOE dependency ledger

| wall | Cycle-476 change | remaining import |
|---|---|---|
| `C_ref` | fixed word ports now feed retained coefficient/control bits without a host weight query | precision, rounding, angle zero/calibration, schedule, and preparation remain supplied |
| `C_num` | exact finite-integer map and strict `2^-8` bound replace an unspecified normalization/root compiler | no selection of precision, physical number reference, units, or continuum error |
| `C_wrap` | unchanged | product steps and gate depth are not physical time; angle/eigenphase is not energy or rate |
| `C_int` | a complete local bit-controlled response schedule now exists with exact adjoint | product-formula selection, q>1/recurrent composition, physical coupling calibration remain open |
| `C_local` | narrowed strongly at one block: 3,444-wire arithmetic, 26-M2 rotation support, and 48,357/64,000 capacity; Cycle474 separately schedules the original delivery block | literal optimized route, angle synthesis, and augmented-block whole-layer composition remain open |
| `C_source` | word data now physically control the local recoil candidate without a host expectation | word law and weighted response are supplied; mass/stress/source meaning and conservation/calibration remain open |

No wall is declared closed and no pair collapses.

## Full no-go discipline

Cycle 476 is positive but bounded by named uncomposed surfaces. The current
no-go-discipline skill was refreshed from `origin/main`, including normalized
route families and proof-search governance. Full N1-N8 rejects any promotion
of the finite residuals to a broad negative or axiom-pressure claim.

### N1 — alternative route enumeration

The normalized family key is `(object/formulation, mechanism/invariant,
terminal obligation)`.

| family | object / mechanism / terminal obligation | status |
|---|---|---|
| restoring multiply/compare root | binary words / reversible candidate inequality / fixed-point coefficients | **ATTEMPTED — SUCCEEDS** |
| single directional exponential pass | q1 source star / presumed commuting directional blocks / exact weighted exponential | **ATTEMPTED — FAILS**, cross-products and `~5.3e-2` residual |
| symmetric product formula | q1 source star / eight carried Strang steps / bounded weighted exponential approximation | **ATTEMPTED — SUCCEEDS** with `6.22e-5` tested residual |
| nonrestoring digit-by-digit root | binary remainder/root automaton / shift-subtract recurrence / lower-work coefficient compiler | **OPEN — NOT ATTEMPTED** |
| reversible CORDIC | fixed-point vector registers / shift-add iterations / root or inverse-root coefficients | **OPEN — NOT ATTEMPTED** |
| QROM or piecewise lookup | normalized mantissa/exponent / bounded table plus interpolation / same coefficient accuracy | **OPEN — NOT ATTEMPTED** |
| polynomial/rational approximation | scaled word ratio / reversible Horner/Newton evaluation / same coefficient accuracy | **OPEN — NOT ATTEMPTED** |
| phase-estimation source exponential | encoded generator/eigenphase / coherent phase kickback / direct controlled exponential | **OPEN — NOT ATTEMPTED** |
| exact local Givens synthesis | 448-state q1 unitary / matrix decomposition controlled by coefficient word / exact quantized exponential | **OPEN — NOT ATTEMPTED** |

Two constructive families succeed, one narrower route fails, and at least six
material alternatives remain open. A broad no-go or minimum-content claim
therefore fails N1.

### N2 — wall-independence audit

The collapsed open set is `Wp`, precision/rounding/product-law selection;
`Wa`, primitive onsite angle synthesis; `Wl`, whole-layer overlap/delivery
composition; `Wq`, q-sector/recurrent source dynamics; `Wc`, physical
source/time/energy calibration; and `Wo`, operational occurrence/instrument.

| pair | first closes second? | reverse? | independent? |
|---|---:|---:|---:|
| `Wp/Wa` | no | no | yes |
| `Wp/Wl` | no | no | yes |
| `Wp/Wq` | no | no | yes |
| `Wp/Wc` | no | no | yes |
| `Wp/Wo` | no | no | yes |
| `Wa/Wl` | no | no | yes |
| `Wa/Wq` | no | no | yes |
| `Wa/Wc` | no | no | yes |
| `Wa/Wo` | no | no | yes |
| `Wl/Wq` | no | no | yes |
| `Wl/Wc` | no | no | yes |
| `Wl/Wo` | no | no | yes |
| `Wq/Wc` | no | no | yes |
| `Wq/Wo` | no | no | yes |
| `Wc/Wo` | no | no | yes |

Choosing `P` does not synthesize an angle. An angle gate does not color a
whole layer. A whole-layer schedule does not extend the local q sector. A
recurrent q-sector law does not calibrate physical time/energy/source. Such a
calibration does not create occurrences or Records.

### N3 — hidden-wall scan

The hidden-condition scan exposes six populated ports, blank outputs/work,
unsigned basis encoding, widths, `P`, floor/zero convention, serial lane and
root-bit order, eight symmetric steps, carried local frame, Cycle-426 angle,
onsite rotations, q1 restriction, held probes, tolerances, capacity placement,
unreplayed Cycle-470 ingress, and absent whole-layer composition. “Physical”
means the displayed M2 gate supports, not a selected energy/time or probability
interpretation. No standard-method phrase discharges a physics obligation.

### N4 — residual matching

| witness | witness residual | Cycle-476 residual | match? |
|---|---|---|---:|
| Cycle 472 note, open inventory | word normalization/root/controlled weighted exponential supplied | fixed-P local compiler | yes |
| Cycle 467 note | arithmetic at six declared word ports | consumes those exact six 249-bit ports | yes |
| Cycle 470 note | delivery into Cycle-467 ports for one serial star; whole-layer overlap open | delivery is prior art only; no layer closure | partial, not cited as closed |
| Cycle 474 note | conflict-free whole-layer schedule for the original Cycle-470 block | available separately; enlarged Cycle-476 block not composed | partial, not cited as closed |
| Cycle 426 note | bounded q1/q2 hard-core source vertex; primitive exponential open | q1 coefficient-bit source schedule only | partial, q2/exact exponential not claimed |
| Accessible P1/P2 | calibrated mass-density/Poisson law and mutual physical phase | dimensionless local weight control | no |
| gravity weak-field/asymptotic ledgers | physical source scale, nonlinear closure, infrared law | finite arithmetic/control block | no |

Only exact matches support the positive compiler claim. Nonmatches are
boundaries rather than evidence for a negative.

### N5 — rhetoric audit

Tested resolutions are individual bits, whole 249-bit words, the six-word
local block, local q1 source-star vectors, one scale-40 supercell, and carried
24-frame families. Not tested are q>1 local response synthesis, overlapping
stars across one layer, recurrent lattice dynamics, infinite volume,
continuum, physical calibration, or operational occurrence. Accordingly,
“complete” is restricted to the fixed-P local arithmetic trace and displayed
product schedule. No lattice-wide, exact-full-exponential, force, time, energy,
probability, P2, or gravity statement is licensed.

### N6 — partial-closure path scan

Cycle 472 made normalization/root/source control explicit as an import. Cycle
476 follows the legitimate import-retirement path by choosing a falsifiable
finite precision, proving its local compiler, and leaving selection/audit open.
Nonrestoring root, CORDIC, QROM, polynomial evaluation, exact Givens synthesis,
fault-tolerant angle compilation, Cycle-470 overlap coloring, and q-sector
extension are all actionable construction paths. None requires axiom language.

No statement equivalent to “no retained primitive supplies this” or “new axiom
required” is made, so no registry absence is used as evidence.

### N7 — hostile steelman

A hostile reviewer should reject any suggestion that the 6.17-million-gate
restoring circuit, P=8 floor convention, or eight-step product is necessary.
A reversible nonrestoring/CORDIC or normalized-mantissa QROM compiler can use
far less work and depth; an exact coefficient-controlled Givens decomposition
can eliminate product-formula error; a selected Clifford-plus-T synthesis can
replace the supplied continuous rotations; and Cycle 470's occupied-path
construction can plausibly be colored into an overlapping layer. Each route
has a concrete object, mechanism, and terminal obligation. This steelman
blocks any broad impossibility or minimum-content claim.

### N8 — cross-cycle echo and claim gate

The prescribed repository phrase search and all available `NO_GO_LEDGER`
files were revisited. Cycle 204 records how local fixed-point and finite-unitary
dilation laws retired earlier apparent mass/source walls; Cycle 215 preserves
multi-field, reservoir, dressed-state, and alternative-order escape routes.
More directly, Cycle 467 replaced an unsynthesized arithmetic block with a
literal compiler, Cycle 470 replaced an apparent nonlocal port service with
occupied-path delivery, and Cycle 474 scheduled the original block over whole
finite layers. Cycle 476 repeats that constructive pattern for
normalization/root/control while leaving the enlarged-block composition open.

The naive directional-factorization failure is therefore evidence about one
operator ordering only. The successful symmetric route already prevents it
from echoing into a substrate claim, while exact Givens and other Hamiltonian-
simulation families remain open.

**Broad no-go: FAIL. Minimum-content claim: FAIL. Shared-obstruction claim:
FAIL. Axiom-pressure claim: FAIL. There is no axiom pressure.**

## Disposition and optimal next campaign

The retained result should be the positive fixed-P word-weight/control
subcompiler with its exact arithmetic and measured rotation residuals.
Unfinished augmented-block whole-layer composition and continuous-angle synthesis are
implementation surfaces, not a shared substrate obstruction.

The highest-value next campaign is to extend Cycle 474's available coloring
and compose Cycle-470 ingress, Cycle-476 arithmetic, coefficient-bit staging,
and source actuation over one complete relaxation layer while keeping the
enlarged supports disjoint per phase. An orthogonal route should compile the finite `H/Rz` angle set into
a declared discrete physical gate basis and compare capacity/error. Neither
campaign should promote schedule depth to time or finite control to gravity.

Retention requires a cold run with zero failures under the declared 900-second
and 4-GiB caps. The final cold run reports `RESULT pass=6 fail=0` and
`RESULT PHYSICAL_WORD_WEIGHT_CONTROL_COMPILER_CERTIFIED`; it takes
`12.1471` seconds and peaks at `904.95 MiB`. Runner SHA-256:
`2cb747b912ed92d6d19e067de9780e0a5899d3659d8defc2135612346cfd0963`.
Authority remains none and audit remains unset.
