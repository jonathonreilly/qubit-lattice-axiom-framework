# Physical full-layer fixed-P response composition — Cycle 481

Date: 2026-07-19

Authority: none

Audit: unset

Constitutional effect: none. No axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit-status surface is edited.

Companion runner:

```text
scripts/physical_full_layer_fixed_p_response_composition_cycle481_2026_07_19.py
```

Runner SHA-256:

```text
7155a82ca672f36f11791cd771515e5039970dec400293dd4e1c4e30e6e3ee13
```

## Result up front

Cycle 481 gives a bounded positive answer to the enlarged-block composition
question left separately by Cycles 476 and 477. Cycle 477's full-layer final
word delivery and local source flags now feed Cycle 476's **fixed precision
P=8** reversible word-to-coefficient circuit and its eight-step local-q1
product response in one explicit uniform all-cell schedule.

Every active R1/R2 cell has the same physical program and enlarged M2 layout.
The arithmetic/control/actuation/uncompute event ledger is explicit.
All six final words are delivered, copied coherently into a duplicate local
Cycle 476 bank, converted into ten-bit coefficients, used by a response vertex
conditioned jointly on the coefficient bit and the locally staged source flag,
and then exactly uncomputed. Only the two prepared local Q1 source flags are
one. There is **no host star selection** and no runtime coordinate query.

The resulting finite P8 update has its own tested physical seam:

```text
E G_coarse^(P8) = G_physical^(P8) E.
```

On the held global-Q2 branch, its forward E/G residual is
`6.646557258911768e-16`, code leakage is `1.5780867095526681e-15`, and exact
adjoint inverse residual is `2.5302371598018803e-15`. The P8 quantization plus
eight-step product changes the supplied exact Cycle 472 response by
`0.0013342416145462317` in state norm on that branch. That finite approximation
is exposed rather than folded into the exact Cycle 472 E/G residual.

The frozen exact Cycle 472 controls also rerun independently. They retain the
one-particle mass `0.4534056541748852`, all 4,047 nontrivial Cycle-230 contact
columns, exact contact deletion and seam inverse, physical E/G, leakage,
inverse, and all held branches. Cycle 476's fixed-P arithmetic, q1 product,
held rows, inverse, leakage, deletions, and malformed domains rerun unchanged.

This is a finite compiler result. The fixed precision, floor rule, product
order, continuous `H/Rz` angle primitives, word law, preparation, source
meaning, and scheduling barriers remain supplied. Cycle 480 is separately
complete and not imported; none of its discrete-angle gates, errors, or
resources enters the Cycle-481 manifest. Count, phase, and depth are not time.
Response is not force or gravity. Norm is not probability. Phase is not
energy.

## Direction-label interface correction

Cycle 470's six physical port lanes are stored in the order

```text
(-x, +x, -y, +y, -z, +z),
```

whereas the Cycle 472/476 response generators use

```text
(+x, -x, +y, -y, +z, -z).
```

Cycle 481 therefore contains an explicit **local direction-label adapter**.
For each response-generator lane it finds the physical Cycle 470 port bearing
the same signed direction, then routes that word into the corresponding Cycle
476 arithmetic input lane. It never equates raw tuple indices. The output
coefficient lane keeps that same physical direction and controls the matching
response generator.

This local adapter has no dynamic branch, preferred global axis, parity
service, or global Jordan-Wigner string. Under a proper-cubic frame its six
signed labels, port paths, coefficient lanes, response generators, and ordered
product schedule are carried together. Omitting this adapter would silently
reverse every signed-axis pair; Cycle 481's literal train and held word rows
test the corrected mapping.

## Uniform enlarged M2 layout

Cycle 477 uses 46,407 of 64,000 M2 per active scale-40 supercell, including
uniform 36-M2 matter/source endpoint banks. Cycle 481 appends:

| local physical region | Hamiltonian indices | M2 |
|---|---:|---:|
| coefficient staging control | `46,407` | 1 |
| source-flag staging control | `46,408` | 1 |
| clean rotation auxiliaries | `46,409..46,421` | 13 |
| duplicate complete Cycle 476 bank | `46,422..49,865` | 3,444 |
| **total used** | `0..49,865` | **49,866** |
| **remaining reserve** | `49,866..63,999` | **14,134** |

The duplicate Cycle 476 bank contains its six 249-bit word inputs, sixty
ten-bit coefficient outputs, and 1,890 arithmetic-work M2. Duplication is a
deliberately conservative constructive route. It avoids overlap with Cycle
470's compiler registers, the 97 retained word-history banks, source flag,
clock bank, and Cycle 477 endpoint code. It is not claimed minimal; an in-place
or reused-work compiler is a live optimization route.

The duplicate input/output/work registers and both staging controls are
required blank at phase entry. Nonblank duplicate input is refused. Arithmetic
work returns to blank before actuation, and all coefficient outputs clear under
the exact inverse trace after actuation.

The active response gate support is 28 M2:

- 13 physical matter/source-star bits;
- one staged coefficient control;
- one staged local source flag; and
- thirteen clean multi-control auxiliaries.

Cycle 476 used 26 M2 for a coefficient-only 13-control rotation. Adding the
positive local source flag changes the central AND from 13 controls with 12
clean auxiliaries to 14 controls with 13 clean auxiliaries. No nonlocal flag or
host-selected coordinate enters the active gate.

## Exact phase schedule

The complete declared forward update has barriers between these phases:

1. compute the persistent local source flag from the uniform endpoint
   reservoir route in every active cell;
2. execute all 96 dual-source word layers in Cycle 474's 27 carried color
   rounds;
3. deliver all six final neighbor words to every active cell in 27 color
   rounds;
4. in all cells simultaneously, copy the six compact ports into the duplicate
   Cycle 476 input bank through occupied-path remote CNOTs;
5. in all cells simultaneously, execute the complete P8 arithmetic compute;
6. stage each persistent source flag into its local response scratch;
7. execute the same 960 direction/bit half-step blocks in every cell: stage one
   coefficient bit, run its sixteen source-flag-and-coefficient-controlled
   basis-pair rotations, and unstage the coefficient bit;
8. unstage the local source flag;
9. reverse the complete P8 arithmetic trace, clearing coefficients and work;
10. reverse the word-input staging paths;
11. return all final words in the reverse 27-color sequence; and
12. uncompute every persistent local source flag.

There is no conditional omission of an inactive cell. When the local source
flag is zero, the same 14-control gates execute but their central rotations are
disabled. This is coherent source-flag conditioning, not host star selection.

The exact inverse recomputes the same local data, applies every product factor
in reverse with the opposite angle, uncomputes local data, reverses all word
layers, and returns flags and histories to the declared input code. Scheduled
forward/inverse invocation is not autonomous recurrence.

## Overlap and conflict audit

The 96 word layers and final-word ingress/egress retain Cycle 474's mod-3-cubed
coloring. Same-color seven-cell stars are disjoint. Every layer visits every
target once, all R1/R2 predecessor dependencies are exact, and the held shell
is included without refit.

After the final delivery barrier, each target's word staging, arithmetic bank,
flag staging, coefficient staging, rotation scratch, and endpoint code stay
inside that target's own physical supercell. Different active cells therefore
have disjoint local-phase support and can execute those phases simultaneously.
Within one cell the manifest uses a strict serial schedule. Occupied-path
transport may cross occupied local sites but restores them; no blank corridor
ancilla is assumed.

The runner checks all same-color star pairs, all local paths, layout intervals,
blank destination codes, and the phase barriers. Simultaneous physical-M2,
path, port, scratch, arithmetic-bank, and endpoint conflicts are zero for both
R1 and R2. Maximum simultaneous word-star support remains 448,000 M2 in R1 and
3,584,000 M2 in R2. The enlarged local phases occupy one disjoint 49,866-M2
cell per target.

This barrier schedule is correct but not optimized. Pipelining colors with
local arithmetic, caching coefficients, and suppressing redundant inactive
work are open implementation routes.

## Exact port, flag, and coefficient staging

### Port to duplicate P8 input

There are `6*249 = 1,494` direction-adapted remote-CNOT actions per cell. Their
path distances range from 28 to 100. One ingress costs 487,674 elementary CNOT
events and ingress plus unstage costs 975,348. The action digest is

```text
8ae9c285c43bc277de5ddaf26691ceef979977857647d74e241b5334186520ac.
```

### Persistent source flag to response scratch

The local source-flag path has distance 38 and costs 223 CNOT events each way,
446 for stage plus unstage. Its action digest is

```text
7fdc5d30dd5756ef34104f7795448be5bd28f12d2e93a5178a5a96fc005899d0.
```

Cycle 477's reservoir-to-persistent-flag route still costs 193 events each way,
386 per cell. Both routes execute in every active cell and restore exactly.

### Coefficient staging

The sixty unique coefficient-bit paths have distance 38 through 71 and cost
19,272 events for one traversal of all unique paths. The eight-step symmetric
schedule contains two directional half-passes per step, so every one of the
sixty direction/bit paths is staged and unstaged 16 times. The exact staging
total is

```text
32 * 19,272 = 616,704 events per cell.
```

The unique-path action digest is

```text
ee3fa212e376710ca6857094b1a41483c9e9f407c9f09809df2f00d56a7d5d95.
```

All staging is coherent CNOT compute/use/uncompute on locally constrained blank
destinations. It does not measure a coefficient, word, or source flag.

## Exact P8 arithmetic route

The frozen Cycle 476 logical trace has:

| primitive | logical count |
|---|---:|
| NOT | 326,820 |
| CNOT | 2,749,056 |
| Toffoli | 3,094,068 |
| **logical total** | **6,169,944** |
| logical trace SHA-256 | `84402e1a70d8d1f7f38d6beb6af41e7d894505179d8f55c9c5f9d007cde2c4f3` |

Cycle 481 places that trace on the contiguous 3,444-M2 duplicate Hamiltonian
bank. For every CNOT it stably gathers one wire beside the other, performs the
gate, and returns all swaps. For every Toffoli it gathers the three wires onto
three consecutive path vertices, performs the local Toffoli, and reverses the
gather. The exact analytic count over all 6,169,944 gates is:

| routed item | count |
|---|---:|
| adjacent SWAP macros, including gather and return | 5,826,300,408 |
| physical NOT | 326,820 |
| physical CNOT, including three per SWAP | 17,481,650,280 |
| physical Toffoli | 3,094,068 |
| **physical elementary events per compute** | **17,485,071,168** |
| maximum logical-wire span | 3,440 |
| stable-gather instruction digest | `1e2146b2a43ca8bbceeb4f3992b7ee255ecd4431af1bb3c1a4d2894b37a29f4c` |

The inverse has the same count and reverses every gather, primitive gate, and
return. Compute plus inverse therefore costs 34,970,142,336 physical events per
cell.

The 17.5-billion result is an exact count for the declared stable-gather
instruction manifest. The runner does not emit or falsely claim to execute
17.5 billion primitive events. It executes the full logical trace and inverse
on literal train and held 249-bit rows, computes every gather distance, and
hashes every logical gate with its exact gather count. Cycle 476's
184,577,059,128 number was a deliberately loose worst-case upper bound; Cycle
481 replaces that bound for this placement with an exact route count. Neither
count is an optimized depth or duration.

## Source-flag-controlled actuation manifest

Cycle 476's eight-step product has 15,360 coefficient-controlled physical
basis-pair rotations. Adding the positive local source-flag control changes
only the central multi-control AND ladder. The complete actuation manifest per
cell is:

| event | count |
|---|---:|
| Toffoli | 2,334,720 |
| CNOT | 30,720 |
| NOT | 1,889,280 |
| onsite H | 30,720 |
| onsite Rz | 30,720 |
| **total** | **4,316,160** |
| active support | **28 M2** |
| clean rotation auxiliaries | 13 M2 |

The flag-augmented manifest digest is

```text
d4984f61b8075255f83a788214eff19bb8b869b85d034f79cedb2c24efcf33a2.
```

Its frozen coefficient-only Cycle 476 parent is
`f8eebaaf506680d0e653362a707b24fb13d04901f05339d03fa59d5b2ee77810`.
The onsite `H/Rz` rotations and their continuous angles remain supplied
physical primitives here. Cycle 480's discrete-angle work is not silently
inserted into this count.

## Complete event and strict-depth ledger

One local final-response pipeline costs:

| phase | events per active cell |
|---|---:|
| persistent flag compute/uncompute | 386 |
| six-word final delivery/return | 1,143,936 |
| port-to-P8-input stage/unstage | 975,348 |
| P8 arithmetic compute/inverse | 34,970,142,336 |
| response flag stage/unstage | 446 |
| coefficient stage/unstage | 616,704 |
| source-flag-controlled actuation | 4,316,160 |
| **local pipeline total** | **34,977,195,316** |

Adding the complete 96-layer word compiler gives:

| quantity | train R1 | held R2 |
|---|---:|---:|
| active cells | 27 | 125 |
| prepared source cells | 2 | 2 |
| word-layer events | 36,132,875,280 | 167,281,830,000 |
| all-cell response-pipeline events | 944,384,273,532 | 4,372,149,414,500 |
| **complete forward events** | **980,517,148,812** | **4,539,431,244,500** |
| **strict parallel depth** | **71,139,812,932** | **71,139,812,932** |

The strict depth keeps each local pipeline serial while running disjoint cells
in parallel. Final word ingress and egress each retain 27 color rounds. A
complete scheduled forward-plus-inverse has twice the displayed event total
and strict depth. Count, phase, color round, product step, and depth are not
time, rate, or proper duration.

The arithmetic dominates this deliberately conservative route. That resource
cost is evidence for optimizing the compiler, not evidence against the shared
substrate.

## Literal train/held and deletion controls

Cycle 481 literally executes the combined delivery, direction adapter, P8
logical arithmetic trace, product actuation/adjoint, arithmetic inverse, input
unstaging, and final-word return on one train and one held representative. It
requires:

- exact equality of all six staged 249-bit words with their spatially labeled
  final neighbors;
- exact equality of all six ten-bit outputs with the P8 integer definition;
- zero arithmetic-work leakage;
- exact logical input/output/work restoration;
- product adjoint residual below `2.53e-15` on the physical held code and below
  `8e-16` on the literal local probes;
- bit-for-bit physical history/port/input/flag restoration; and
- zero path-adjacency failures.

All fourteen source endpoints from the three train and four held pairs are
checked without refit. Their maximum coefficient error remains
`0.0037624671720912772`, below the strict `1/256 = 0.00390625` bound. The
local flag-on versus flag-off actuation signal is at least `0.2226683683` on
the literal representatives.

Deletion controls include:

1. deleting an entire delivered word lane before the duplicate P8 input must
   change the retained coefficient row;
2. deleting a Cycle 476 root-trial segment changes a coefficient by 104
   register units;
3. deleting one active coefficient rotation changes a local state by
   `0.0014168925507746853`;
4. deleting the response coupling changes it by `0.5031983598576016`;
5. clearing the staged source flag makes the whole response actuation identity;
6. omitting return leaves populated staging or port bits;
7. deleting a Cycle 472 word source changes the later held history; and
8. deleting either exact response vertex or Cycle-230 contact seam retains its
   frozen nonzero residual.

Malformed word width/value, nonblank duplicate input, duplicate source pair,
wrong color round, invalid direction, and repeated/missing carried direction
order are refused. These are controls for the declared route, not minimum
constitutional content.

## Fixed-P physical E/G and preserved exact seam

Cycle 481 defines `G_coarse^(P8)` by the exact P8 integer coefficient map and
the same eight-step coefficient-bit product used by the physical gate
manifest. The intrinsic-M64 encoder then intertwines that same finite product
with the physical 13-M2 local q1 star. On the held `(1,1,1)` relative branch:

| diagnostic | residual |
|---|---:|
| P8 physical forward E/G | `6.646557258911768e-16` |
| P8 physical code leakage | `1.5780867095526681e-15` |
| P8 complete adjoint inverse | `2.5302371598018803e-15` |
| P8 product plus quantization versus exact Cycle 472 | `0.0013342416145462317` |

The integer coefficients at the two held endpoints are

```text
(277,229,271,240,271,240),
(241,272,229,278,229,278).
```

The exact Cycle 472 response is still rerun as an import, not relabeled as the
P8 update. It retains maximum exact E/G `8.185353026114583e-16`, leakage
`1.5110441311098406e-15`, inverse `2.256183082803949e-15`, mass residual
`1.1102230246251565e-16`, Cycle-230 contact deletion
`1.5332239522066473`, seam inverse `1.1859202370900672e-15`, held word
residual at most `1.1186600620779015e-7`, held response separation
`0.021283120229758912`, Schmidt tail `0.07289673325938074`, and rank four.

Thus Cycle 481 preserves the exact upstream fixture and states separately what
changes under its finite compiler. It does not call approximation error
leakage, occurrence, probability, force, or gravity.

## All 24 proper-cubic frames

The runner carries through all 24 proper-cubic frames:

- the complete 27-color reference sequence and every R1/R2 target set;
- the two source cells and their scalar local flags;
- all six signed final-word directions and physical ports;
- the local direction-label adapter;
- every port/input, flag, and coefficient staging path;
- the complete 3,444-M2 arithmetic Hamiltonian bank and stable-gather rule;
- all coefficient output lanes, matter/source basis pairs, and clean scratch;
- the forward/reverse symmetric-product direction order; and
- every branch manifest.

Every carried path edge remains nearest-neighbor. Every carried coefficient is
the exact coefficient of the carried word lane. Every carried color target set
equals the frame image of the reference set. The ordered color and product
sequences are carried directly, with **no global resort** into a preferred
coordinate order. All carried failures are zero and the 24 frame manifests are
distinct.

This proves covariance of one supplied reference phase program and its orbit.
It does not select a physical frame, clock, lapse, or autonomous causal order.

## Frozen imported identities

| imported runner | SHA-256 |
|---|---|
| Cycle 463 | `3ae259060c7d7f9e13088197cf022eef845241af20972e5496cede6b4344e9ad` |
| Cycle 467 | `7e562949be71a647d410c8a9624eb5cf5fdf2be30777fab93c6ed55824a5e402` |
| Cycle 470 | `287b72625b4bf7d29cb847e0a59ed5d64f58b3ec55e5b312942f96bbc0ea6674` |
| Cycle 472 | `6204ae34c7d42c5e61d797d5bb2039f8ea199499b46ef01f6b52b8951e8b557d` |
| Cycle 474 | `10a55ef2cb36f7d9f60b115911fc2bcffbffbe3ac0977db0ba319f6dcfd08755` |
| Cycle 476 | `2cb747b912ed92d6d19e067de9780e0a5899d3659d8defc2135612346cfd0963` |
| Cycle 477 | `0e0e0f8b5baa8ea0d00d9b24e7cc7a5d2167805158f96223e1f5d41a6e087afd` |

The runner refuses an identity mismatch. Cycle 480 is not in this import
table because its compiler is a separately completed result, not an input to
Cycle 481. Its current runner SHA-256 is
`39f2fb1c9d3e10bf8741b6f426bc0a7dbbd75dea7c4c66aedc75b8d8275fb743`;
that identity is recorded as an available next interface, not used as
authority or included in any event count or residual here.

## Prior-art and novelty boundary

Reversible compute/use/uncompute, duplicate work banks, SWAP gathering,
remote CNOT, residue coloring, multi-controlled rotation ladders, and symmetric
product formulas are standard compiler techniques. Cycle 481 claims none of
them as new, and it claims no optimal M2, route, gate, color, precision,
product, or depth count.

The repository advance is their exact composition on the retained physical
objects: Cycle 477's every-cell word delivery and local flags, Cycle 476's
complete P8 arithmetic/product block, an explicit signed-direction adapter,
uniform nonoverlapping layout, exact stable-gather event counts, a genuinely
local source-flag control added to every actuation, complete phase/inverse
ledger, held literal tests, new P8 physical E/G seam, and all-24 no-resort
covariance.

Cycle 481 retires Cycle 476's named enlarged-block whole-layer composition
residual and Cycle 477's primitive-response residual at one declared finite
precision/product order. Cycle 480 separately retires the runtime continuous-
angle service at its supplied `B20` precision, but the two manifests have not
yet been joined. Precision/product/basis selection, recurrence, calibration,
asymptotics, occurrence, and gravity remain. Thirring is not used and is not
a novelty anchor.

## Supplied / constructed / open inventory

Supplied:

1. Cycle 463's finite word law, R1/R2 boundary/shells, retained histories,
   precision, iteration count, and dual-source fixtures;
2. Cycle 467's local divide-by-six circuit and Cycle 470's delivery placement,
   ports, paths, and occupied-path primitive;
3. Cycle 472's intrinsic-M64 encoding, mass/contact seam, q1 response law,
   source preparation, angle/sign, branch menu, readouts, and tolerances;
4. Cycle 474's 27 colors, reference order, layer barriers, and event-lockstep
   convention;
5. Cycle 476's P8/floor/all-zero rule, ten-bit outputs, 6,169,944-gate trace,
   eight-step product order, continuous onsite `H/Rz`, and error caps;
6. Cycle 477's uniform endpoint banks, final response-delivery program, and
   reservoir-to-persistent-flag path;
7. Cycle 481's conservative duplicate-bank placement, 15-M2 scratch, serial
   local phase barriers, resource caps, authority none, and audit unset.

Constructed and tested:

1. direction-label-correct Cycle 470 port to Cycle 476 input mapping;
2. uniform 49,866-M2 enlarged layout with 14,134-M2 reserve;
3. exact 17,485,071,168-event stable-gather arithmetic count and inverse;
4. literal coherent port/input, flag, and coefficient staging/uncompute;
5. source-flag-augmented 28-M2, 4,316,160-event actuation manifest;
6. complete R1/R2 phase, event, strict-depth, capacity, and conflict ledger;
7. exact all-fourteen-endpoint P8 coefficient bound and held deletion controls;
8. a P8 global-Q2 physical E/G, leakage, inverse, and exact-response comparison;
9. full frozen Cycle 472/476 preservation and all-24 carried covariance.

Open:

1. selecting or deriving `P`, floor/rounding, all-zero convention, product
   order, and product step count;
2. composition of Cycle 480's separately completed `B20` angle words and
   Suzuki4 product with the full Cycle-481 layer, including a separated
   coefficient/product/angle error and event ledger;
3. emitted or optimized execution of the 17.5-billion-event route, in-place
   work reuse, cached coefficients, and pipelining;
4. exact full exponential, uniform analytic product error, q>1 response, and
   recurrent source/matter transport;
5. removal/compression of retained histories and autonomous phase scheduling;
6. physical source magnitude, mass/energy-stress conservation, coupling/time
   calibration, continuum and infrared/asymptotic control;
7. lapse, metric, curvature, backreaction, gravity, operational instruments,
   occurrence, Records, Born weights, P2, or BMV.

## TOE dependency ledger

| wall | Cycle 481 disposition |
|---|---|
| `C_ref` | unchanged in authority: finite pair menu, preparation, P8/floor/product choices, boundary, reference colors, barriers, and inverse calls remain supplied |
| `C_num` | constructively narrowed: exact finite words now reach an exact P8 integer coefficient trace on every R1/R2 cell with a strict `2^-8` bound; no physical number reference, units, precision selection, or continuum guarantee is derived |
| `C_wrap` | unchanged: iteration, color, phase, product step, event count, and depth are compiler ordinals, not winding, duration, rate, or physical time |
| `C_int` | materially narrowed: one complete P8 coefficient-bit response with local source control, explicit physical gates, exact adjoint, and tested P8 E/G is composed; Cycle 480 separately supplies fixed-basis angles, while product/basis selection and exact/q>1/recurrent update remain open |
| `C_local` | strongly narrowed: complete delivery, direction adapter, enlarged layout, routing, arithmetic, actuation, uncompute, capacity/conflicts, held controls, and all-24 schedule now compose for the full finite layers; Cycle-480/Cycle-481 angle-manifest composition, route optimization, recurrence, and history removal remain |
| `C_source` | narrowed at control locality: the same all-cell circuit responds only where a coherently staged local reservoir flag is one, with no host star list; source meaning, magnitude, conservation, calibration, stress, and backreaction remain open |

No pair collapses. A P8 compiler does not select its physical precision,
angles, source meaning, duration, or occurrence. A source calibration would
not itself provide routing, local gates, or a conflict-free all-cell schedule.

## Full no-go discipline

The current no-go discipline is applied to every negative, minimality, shared-
obstruction, and axiom-pressure statement. The positive result makes a broad
negative especially unwarranted.

### N1 — Alternative route enumeration

| normalized route family | object / mechanism / terminal obligation | status |
|---|---|---|
| duplicate contiguous arithmetic bank | Cycle 476 trace / stable gather and exact return / complete all-cell P8 response | **ATTEMPTED — SUCCEEDS** |
| uniform all-cell local flag control | two prepared Q1 cells / coherent positive flag control / no host source-star selection | **ATTEMPTED — SUCCEEDS** |
| raw tuple-index port mapping | signed words / assume Cycle 470 and response lane orders coincide / correct directional coefficients | **FALSIFIED**; signed pairs reverse |
| explicit signed-direction adapter | labeled ports / local spatial-label lookup fixed at compile time / correct response lane | **ATTEMPTED — SUCCEEDS** |
| in-place/reused Cycle 467 work | existing blank post-word registers / liveness allocation / lower M2 and staging | **OPEN** |
| cached face or coefficient bank | repeated cell-local data / cache across product steps / lower staging count | **OPEN** |
| nonrestoring/CORDIC/QROM root | six words / alternate reversible arithmetic / same coefficient error | **OPEN** |
| exact local Givens response | 448-state q1 block / exact controlled decomposition / remove product error | **OPEN** |
| staggered/pipelined colors | full layer / overlap delivery with disjoint local work / lower strict depth | **OPEN** |
| packet or quantum-walk delivery | signed word registers / autonomous local network / same port obligation | **OPEN** |
| discrete-angle compilation | finite H/Rz set / Cycle 480 supplied `B20` basis and Suzuki4 comparison / bounded gate error | **SEPARATELY ATTEMPTED — SUCCEEDS; NOT COMPOSED HERE** |

Multiple constructive routes succeed, one narrow indexing shortcut fails, and
many material alternatives remain. No minimum bank, precision, control,
product, route, color, or axiom follows.

### N2 — Wall-independence audit

Let `Wl` be layout/routing composition, `Wp` precision/rounding/product-law
selection, `Wa` discrete angle synthesis, `Wr` recurrence/history removal,
`Ws` source/calibration/asymptotics, `Wt` physical time, `Wg` geometry/gravity,
and `Wo` occurrence/Records/Born. No one of these closes another in either
direction. In particular:

- a correct layout does not select P or an angle basis;
- discrete angles do not provide a layer scheduler;
- recurrence does not calibrate source magnitude or time;
- source calibration does not derive geometry or occurrence;
- an operational occurrence law does not compile local routing.

All pairs remain independent. The successful local composition cannot be
promoted into closure of time, source, gravity, or probability.

### N3 — Hidden-wall scan

Exposed supplied structure includes: duplicate blank inputs; 15 scratch M2;
249/10-bit widths; P8; floor and zero convention; the word law and finite
boundary; two prepared local Q1 reservoirs; direction labels; factor angle and
sign; eight product steps; serial bit/direction order; continuous H/Rz;
27 colors and barriers; stable-gather policy; strict depth convention; branch
menu; readouts; tolerances; and scheduled inverse. “Physical” refers only to
the displayed M2 code and gate supports, not to energy, time, force, gravity,
or occurrence.

### N4 — Residual matching

The result matches Cycle 476's named “Cycle-470 plus Cycle-476 whole-layer
overlap, coloring, and recurrence” residual only at the finite whole-layer
composition part; recurrence remains open. It matches Cycle 477's open
primitive response synthesis at fixed P and the inherited continuous-angle
basis. Cycle 480 separately matches the discrete-angle residual. Neither alone
matches their joined error/resource ledger, P/product/basis selection,
recurrent matter motion, source/time calibration, infrared/asymptotic gravity,
or Born residuals. Those nonmatches remain boundaries, not negative evidence.

### N5 — Rhetoric audit

Exact statements are restricted to finite integer arithmetic, routing counts,
inverse cleanup, code intertwining, layout, capacity, conflicts, and covariance.
Approximate statements retain their P8/product residual. “Complete” means the
declared finite forward/inverse compiler, not exact continuum dynamics. Count,
phase, and depth are not time. Response is not force or gravity. Norm is not
probability. Phase is not energy. A generator element is not a rate. A copied
word or flag is not a Record.

### N6 — Partial-closure path scan

The enlarged-block composition and Cycle 480's fixed-basis angle compiler close
constructively on separate manifests without an axiom edit. Direct next routes
are their three-way composition, in-place liveness allocation, route
optimization, coefficient caching, pipelined colors, exact Givens response,
and q>1 recurrence. Precision selection, calibration, asymptotics, and
occurrence each have their own constructive test obligations. None is replaced
by an impossibility statement.

### N7 — Steelman

A hostile reviewer should demand: elimination of the 1,494-M2 duplicate word
bank; literal emission or independently checked execution of the chosen
17.5-billion-event route; a uniform analytic P8/product error bound rather than
finite rows; coherent nonbasis word-register tests; a selected discrete gate
basis; lower staging/color depth; recurrent matter/source motion; derived
source magnitude and duration; and infrared/continuum control. They should
also reject any claim that 49,866 M2, P8, 27 colors, stable gather, or the
eight-step product is necessary. These are legitimate remaining routes and
objections, not substrate obstructions.

### N8 — Cross-cycle echo and claim gate

Cycle 467 compiled local arithmetic, Cycle 470 compiled bounded word delivery,
Cycle 474 supplied conflict-free whole-layer coloring, Cycle 476 compiled the
fixed-P local word/control block, and Cycle 477 composed delivery and local
source flags over both finite domains. Cycle 481 follows the same constructive
pattern and now composes those exact surfaces. The earlier separation was
unfinished implementation, not a shared substrate obstruction.

Cycle 480's discrete-angle campaign separately succeeds, while its composition
with this full-layer manifest is still unmade. Source/time, recurrence,
asymptotics, gravity, and occurrence likewise remain distinct.

Broad no-go: FAIL. Minimum-content claim: FAIL. Shared-obstruction claim: FAIL.
Axiom-pressure claim: FAIL. There is **no axiom pressure**.

## Optimal next campaign

The highest-value composition is now a three-way error/resource ledger joining
Cycle 480's reviewed discrete-angle approximation to Cycle 481's P8
quantization and full-layer product without changing the physical update
silently. The terminal obligation is one cold all-branch update with separated
coefficient, product, angle, routing, and physical E/G residuals.

In parallel, the most valuable local optimization is an in-place liveness
compiler that reuses blank Cycle 467/post-arithmetic work and caches coefficient
bits, while preserving the direction-label adapter, local source flag, exact
inverse, held branches, all-24 no-resort covariance, and explicit phase
barriers. Neither route licenses time, force, probability, gravity, or axiom
language.

## Frozen executable disposition

The final synchronized cold run reports `RESULT pass=12 fail=0` in
`157.35645008296706` seconds with peak RSS `657.546875 MiB`, below the
declared 600-second and 3,072-MiB caps. Runner SHA-256:
`7155a82ca672f36f11791cd771515e5039970dec400293dd4e1c4e30e6e3ee13`.
Authority remains none and audit remains unset.
