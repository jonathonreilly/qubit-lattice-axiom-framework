# Physical full-layer discrete response composition — Cycle 484

Date: 2026-07-19
Authority: none
Audit: unset

## Claim

Cycle 484 constructively composes three previously separate finite surfaces:

1. Cycle 481's direction-correct full-layer delivery, duplicate P8 arithmetic bank, local source flag, conflict barriers, and exact return;
2. Cycle 480's finite basis B20 and repeated Z20 words; and
3. the Cycle 472 global-Q2 physical encoding and exact retained response seam.

The selected Suzuki4 schedule is now a literal all-cell event manifest. Every supplied continuous `Rz` actuation event from Cycle 481 is replaced by a signed integer word in `{NOT, CNOT, Toffoli, H, Z20, Z20^-1}`, with `Z20 = Rz(2 pi / 2^20)`. Each coefficient-controlled pair rotation also receives the extra source-flag control required by the composed response law. The full train-R1 and held-R2 domains fit one uniform 49,866-M2 cell layout with 14,134 M2 reserve. There are no continuous `Rz` events left in this manifest.

This is a finite compiler result, not a calibration or fundamental-law derivation. The basis, exponent 20, P8 fixed-point rule, response angle, product ordering, Suzuki coefficients, and primitive gate calibration remain supplied.

## Frozen imports

- Cycle 480 runner: `39f2fb1c9d3e10bf8741b6f426bc0a7dbbd75dea7c4c66aedc75b8d8275fb743`
- Cycle 481 runner: `7155a82ca672f36f11791cd771515e5039970dec400293dd4e1c4e30e6e3ee13`
- Cycles 463, 467, 470, 472, 474, 476, and 477: the identities declared in the Cycle 484 runner.

The imported preservation run retains the one-particle mass fixture at `0.4534056541748852` with residual `1.1102230246251565e-16`, the 4,047 nontrivial Cycle-230 contact columns, and the complete Cycle 472 seam inverse, deletion, held-branch, leakage, and physical E/G controls.

## Frozen selection and scope

Route selection is frozen before held readout. On the six training rows the intrinsic product-plus-angle scores are:

| route | maximum training intrinsic residual |
|---|---:|
| retained direct Strang8 | `7.98149044671803e-05` |
| selected Suzuki4 | `1.9080216797967914e-05` |

Held rows do not reselect the route. All fourteen rows are abstract, direction-correct state-residual tests: six training endpoint rows and eight held endpoint rows. Literal delivery/arithmetic/actuation/cleanup is executed on one predeclared training representative and one predeclared held representative. The covariance lane executes one predeclared held response vector across all 24 proper-cubic frames, while structural path, color, port, P8-lane, flag, Suzuki-scale, phase-sign, and inverse manifests are audited across the two finite fixture domains. This is not an all14-by-24 literal execution claim.

## Separated all-fourteen residual ledger

The endpoint direction adapter is applied before these results: physical Cycle 470 ports `(-x,+x,-y,+y,-z,+z)` are mapped into response-generator order `(+x,-x,+y,-y,+z,-z)`.

| residual maximum | direct Strang8 | Suzuki4 |
|---|---:|---:|
| coefficient quantization | `1.1259673896622283e-03` | `1.1259673896622283e-03` |
| product-formula | `6.838309239442313e-05` | `9.551348132766513e-06` |
| discrete-angle | `6.971440007602758e-05` | `2.3565267598149933e-05` |
| intrinsic product plus angle | `9.442466936825169e-05` | `2.1410986536149105e-05` |
| total residual from the unquantized target | `1.138953989642712e-03` | `1.140957752743206e-03` |
| exact inverse | `8.103284262956571e-16` | `7.402551759360391e-16` |
| norm leakage | `0` | `0` |

This is a no cancellation-based claim. Suzuki4 wins the frozen training intrinsic criterion and lowers the held-set intrinsic maximum, but its all-fourteen total maximum is slightly worse than direct Strang8 because the dominant coefficient error combines differently with the intrinsic error. The total column is reported, not used to rewrite the selection rule.

## Literal discrete manifest

The source flag changes each coefficient-controlled AND from 13 to 14 controls and adds two Toffolis per rotation. It uses one additional staged flag and 13 clean rotation auxiliaries; maximum active rotation support is 28 M2 and no new angle auxiliary is introduced.

| per-cell actuation | direct Strang8 | selected Suzuki4 |
|---|---:|---:|
| symmetric S2 blocks | 8 | 5 |
| directional half-passes | 16 | 10 |
| controlled pair rotations | 15,360 | 9,600 |
| Toffoli | 2,334,720 | 1,459,200 |
| CNOT | 30,720 | 19,200 |
| NOT | 1,889,280 | 1,180,800 |
| H | 30,720 | 19,200 |
| repeated `Z20` or `Z20^-1` | 46,445,568 | 107,561,472 |
| total discrete actuation gates | 50,731,008 | 110,239,872 |

The exact selected per-cell phase ledger is:

| phase | events |
|---|---:|
| persistent source-flag compute and return | 386 |
| response delivery and return | 1,143,936 |
| port-to-duplicate-input stage and return | 975,348 |
| P8 arithmetic compute and inverse | 34,970,142,336 |
| rotation-flag stage and return | 446 |
| ten Suzuki half-pass coefficient staging | 385,440 |
| discrete Suzuki4 actuation | 110,239,872 |
| total selected per cell | 35,082,887,764 |

The selected whole-domain event totals are `983,370,844,908` for the 27 active R1 cells and `4,552,642,800,500` for the 125 active R2 cells. Strict scheduled depth is `71,245,505,380`. The retained direct Strang8 control uses `35,023,610,164` events per cell, `981,770,349,708` events over R1, `4,545,233,100,500` over R2, and depth `71,186,227,780`. Thus selected Suzuki4 costs `59,277,600` more events per cell under this unoptimized repeated-word ledger despite its better frozen intrinsic error.

The phase order is explicit: persistent flags; 96 by 27 word rounds; 27-color word ingress; direction-correct input stage; P8 arithmetic; local flag stage; 600 Suzuki scale/direction/bit blocks with repeated Z20 words; flag unstage; arithmetic inverse; input unstage; reverse-27-color egress; persistent flag uncompute. Same-phase conflicts are zero. Routing depth is not time.

## Physical P8, product, and angle seam

For the held pair `((-1,0,0),(0,1,1))`, the endpoint coefficient words are `(277,229,271,240,271,240)` and `(241,272,229,278,229,278)`.

The exact comparison exponentiates the literal, slightly non-normalized P8 coefficient generator. It does not renormalize through Cycle 472's exact-weight API; doing so would erase part of the coefficient quantization residual. On the global-Q2 retained state the decomposition is:

| global-Q2 residual | direct Strang8 | selected Suzuki4 |
|---|---:|---:|
| coefficient quantization | `1.3342416145463805e-03` | `1.3342416145463805e-03` |
| product-formula | `9.28333584933522e-16` | `6.353097611517748e-16` |
| discrete-angle | `6.912888097480166e-05` | `2.2524927482222215e-05` |
| intrinsic product plus angle | `6.91288809747572e-05` | `2.252492748228495e-05` |
| total from exact unquantized response | `1.3364958506980995e-03` | `1.3528307732474357e-03` |
| inverse | `2.2351631338691837e-15` | `2.472260630386629e-15` |
| norm leakage | `2.220446049250313e-15` | `2.6645352591003757e-15` |

For selected Suzuki4, `|| E G_discrete - G_physical E || = 6.611002205514151e-16` and code leakage is `1.7215686428689391e-15`. This is exact intertwining of the selected finite update on its code space. It is distinct from approximation to the unquantized response law.

## Deletion, domain, and return controls

The literal representatives restore every response port, P8 input/output/work bit, staged coefficient, staged source flag, delivery wire, logical probe, and physical placement after the exact reverse schedule. The discrete quantum inverse residuals are below `4.0e-16` on those representatives.

Independent deletions remove one consumed word lane (`1.625129931671068e-01`), one `Z20` quantum (`1.8684193664168422e-06`), one active coefficient bit family (`4.418453732370119e-04`), one Suzuki direction factor (`3.285401721869596e-02`), or the local source flag (`2.433828804677343e-01`). Every deletion produces a signal above `1e-9`. Malformed coefficient width/value, route, exponent, lane permutation, nonblank duplicate P8 input, duplicate source pair, and malformed color round are refused. The all-zero coefficient tuple remains the exact identity.

## Supplied, constructed, and open

Supplied structure:

- Cycle 472 physical matter encoding, retained branch state, mass/contact fixtures, response angle, and exact unquantized word weights;
- Cycle 481 delivery, duplicate-bank P8 arithmetic, source flags, 27 colors, barriers, and inverse schedule;
- P8/floor arithmetic, ten coefficient bits, source-pair generator, CAR signs, matter/field basis, and frame representations;
- finite basis B20, exponent 20, exact H/NCT assumption, nearest rounding, Suzuki factors and order, finite fixtures, norms, tolerances, initial state, and readouts.

Constructed here:

- extra source-flag control and its gate/resource delta;
- complete selected and retained discrete R1/R2 event, depth, capacity, conflict, and phase manifests;
- direction-correct all-fourteen coefficient/product/angle/total residuals with frozen training selection;
- literal train/held delivery-to-P8-to-discrete-actuation cleanup;
- one global-Q2 physical P8/product/angle E/G seam; and
- carried all24 structural covariance and one-sample response covariance with no global resort.

Open walls:

- physical selection or calibration of basis, P, product formula, exponent 20, primitive phase, and response angle;
- fault/noise thresholds, optimized phase words, and a uniform analytic bound over every lawful 249-bit word tuple;
- exact Givens, phase kickback, Clifford+T, QSP, alternate bases, in-place arithmetic, caching, and pipeline optimization;
- coherent word superpositions, recurrence/history removal, source calibration, physical duration, energy/stress, asymptotics, gravity, occurrence, Records, and Born probability.

## Interpretation firewalls

Depth is not time. Phase is not energy. Response is not force or gravity. Norm is not probability. A supplied local source flag is not a derived gravitational source. The result does not derive recurrence, energy-stress, metric, lapse, curvature, realized history, a Record, or the Born rule.

## N1–N8 discipline

### N1 — Alternative route enumeration

The selected B20/Suzuki4 and retained B20/Strang8 compositions both succeed. Clifford+T, phase-gradient kickback, exact controlled Givens, QSP/qubitization, alternate finite bases, in-place arithmetic, cached faces, and staggered pipelines remain live routes.

### N2 — Wall-independence audit

Basis calibration, P8 quantization, product error, angle synthesis, routing optimization, recurrence, source/time calibration, infrared control, gravity, occurrence, and probability remain separable.

### N3 — Hidden-wall scan

The runner exposes P8, floor/zero behavior, ten bits, B20, nearest rounding, exact H/NCT assumptions, Suzuki coefficients/order, source flags, duplicate bank, direction adapter, colors, barriers, finite boundaries, initial states, norms, tolerances, and the absent noise model.

### N4 — Residual matching

Cycle 484 matches Cycle 480's discrete-angle residual and Cycle 481's full-layer P8 product-and-quantization residual. It does not match basis selection, uniform-error, recurrence, source/time, gravity, Record, or Born residuals.

### N5 — Rhetoric audit

The claim stops at one finite P8/Suzuki4/B20 response layer. Coefficient, product, angle, intrinsic, total, routing, leakage, and inverse diagnostics remain distinct.

### N6 — Partial-closure path scan

The three-way composition closes constructively. Exact Givens, alternate bases, optimized routing, coherent controls, recurrence, calibration, and asymptotics remain direct campaigns.

### N7 — Steelman

A hostile reviewer can require uniform operator bounds, a physical fault model, optimal phase synthesis, removal of the duplicate bank, emitted full-domain traces, coherent nonbasis word tests, autonomous recurrence, and infrared control.

### N8 — Cross-cycle echo and claim gate

Cycles 476, 477, 480, and 481 independently closed fixed-P control, whole-layer delivery, finite-angle compilation, and fixed-P response composition. Cycle 484 closes their discrete composition. Remaining calibration, source/time, gravity, occurrence, and probability walls stay independent. Broad no-go, minimum-content, shared-obstruction, and axiom-pressure promotion fail. There is no axiom pressure.

## Reproduction

```bash
python3 scripts/physical_full_layer_discrete_response_composition_cycle484_2026_07_19.py
```

Acceptance requires zero exit status, exact frozen identities, zero failed checks, declared wall/RSS caps, and no note-contract omissions.

## Cold verification

The final independent command

```text
/usr/bin/time -lp python3 -u scripts/physical_full_layer_discrete_response_composition_cycle484_2026_07_19.py
```

returned `13 PASS / 0 FAIL`. The controlled body measured
`116.78761400002986 s` and `998.359375 MiB` peak RSS, within the declared
`700 s / 3072 MiB` caps. Complete cold-process accounting was `203.46 s`
real, `195.96 s` user, `1.63 s` system, and `1,046,855,680` bytes maximum
resident set size.

Runner SHA-256:
`7551a61dd61292cbeab685b55475e6d63c5223a9185891b4605fc7bcf151a86f`.
