# Physical discrete quadrupole exact-strength bridge — Cycle 487

Date: 2026-07-20

Authority: none

Audit: unset

## Frozen question

Does replacing Cycle 453's continuous coefficient-two source/receiver vertex with the Cycle 484 P8/Suzuki4/B20 physical update preserve the passing quadrupole strength ratio, and does it repair any of Cycle 453's failing absolute rows, stronger `a=2` order, or L13 physical-shell resource boundary?

Cycle453 exact targets and direct inputs are frozen before the replacement. The Cycle484 P8/Suzuki4/B20 route changes only the six local recoil vertices in each depth step. It keeps the exact Cycle420 rows, Cycle453 occupations, train L13/a1/depth4 and held L13/a2/depth4 geometries, matter/field coins, streams, packet FSWAPs, contacts, initial phase quadrupole, and packet-width observable unchanged. Held rows do not refit or reselect anything.

The result is a `partial-attempt-with-named-untested-routes`. The discrete compiler succeeds exactly on its physical code and perturbs each width row by less than the already-frozen `5e-10` row tolerance. The strength ratio still passes. All four absolute rows and the stronger a=2 order remain outside their target contract. Those residuals are law/calibration/finite-domain evidence for this one supplied program, not compiler obstruction.

## Frozen identities and targets

The runner verifies these SHA-256 identities:

| input | SHA-256 |
|---|---|
| Cycle420 | `79eca68ca217277fa237d2420888b64ef7bfba801e8745925a8dfb14b7576d5c` |
| Cycle435 | `d0682c388411e3f2c4547e4703214ce70831382e12fe154da9a5349944a07ff7` |
| Cycle453 | `dd3004fe92203651fd7fe732d1253d49379b52075bd88159fa7712154c0f8557` |
| Cycle480 | `39f2fb1c9d3e10bf8741b6f426bc0a7dbbd75dea7c4c66aedc75b8d8275fb743` |
| Cycle481 | `7155a82ca672f36f11791cd771515e5039970dec400293dd4e1c4e30e6e3ee13` |
| Cycle484 | `7551a61dd61292cbeab685b55475e6d63c5223a9185891b4605fc7bcf151a86f` |
| Cycle487 runner | `b0e4ac4aea641dbf90f64ac6d944b639b983ec76e365c3a60377b1ea2b5cf091` |

The supplied occupations remain

```text
p_unit = 0.015003358529489008
p_two  = 0.07565725585107586
p_two / p_unit = 5.042687988984065
```

and the exact Cycle420 targets remain:

| row | target width shift |
|---|---:|
| a1/unit | `6.692829912502418e-7` |
| a1/coefficient two | `3.3757457469363317e-6` |
| a2/unit | `1.3197896109318208e-6` |
| a2/coefficient two | `6.656001151128521e-6` |

No held result changes an occupation, angle, route, precision, factor order, geometry, depth, observable, or tolerance.

## Literal adapter and compiler residuals

Cycle453 and Cycle484 use the same local six-mode CAR matter labels and the same dimensionless angle `0.3627245233399082`, but their seven-state source-star basis orders differ:

- Cycle484: `(direction0,...,direction5,reservoir)`;
- Cycle453/Cycle322: `(reservoir,direction0,...,direction5)`.

A fixed reservoir/direction basis adapter permutes those seven states inside every matter mask. It is unitary with residual zero. Rebuilding Cycle453's six restricted continuous source/receiver embeddings through this adapter gives maximum entrywise residual zero. No observable adapter is required: the output feeds the unchanged Cycle435 `packet_weights` and `packet_moments` functions.

The coefficient-two vertex is uniform. Supplied words `(1,1,1,1,1,1)` give literal P8 coefficients `(256,256,256,256,256,256)`, so coefficient quantization is zero to numerical precision. On the complete 448-dimensional local operator:

| compiler coordinate | residual |
|---|---:|
| adapter unitarity | `0` |
| coefficient quantization | `2.391960337907783e-16` |
| product-formula, exact P8 to continuous Suzuki4 | `1.4755175278576416e-05` |
| discrete-angle, continuous Suzuki4 to B20 | `1.7265242487962935e-05` |
| compiler total, exact Cycle453 vertex to B20 Suzuki4 | `1.8220829572073208e-05` |
| exact scheduled inverse | `1.913624072687692e-15` |
| unitarity | `1.9062267710571797e-15` |

The uniform local physical compiler E/G residual is `1.0408340855860843e-16`; physical code leakage is `6.982127306007955e-16`. This is one local q1 source-star physical seam with identity off-code completion. The actual Cycle453 restricted source factors are `1512 x 1512`; receiver factors are `126 x 126`.

Coefficient, product, angle, compiler E/G, inverse, routing, and prediction residuals are not added or relabeled as one error. In particular, no cancellation-based accuracy claim is made.

## Actual discrete prediction rows

The runner evolves the unchanged Cycle453 Q0 and quadrupole Q1 sectors with the adapted discrete vertices. Their output key sets remain disjoint, so the supplied coherent strength state has exactly the convex packet-weight row obtained from linear propagation; this is not expectation feedback or a runtime branch.

| row | Cycle484-discrete width shift | Cycle453 continuous | compiler-induced delta | Cycle420 target | source-law/prediction residual |
|---|---:|---:|---:|---:|---:|
| a1/unit | `4.84588486629467e-7` | `4.846405339820059e-7` | `-5.2047352538941993e-11` | `6.692829912502418e-7` | `-1.8469450462077486e-7` |
| a1/coefficient two | `2.4436060479526844e-6` | `2.4438685030658824e-6` | `-2.624551131980013e-10` | `3.3757457469363317e-6` | `-9.321396989836472e-7` |
| a2/unit | `4.374646635496582e-7` | `4.3751148665061024e-7` | `-4.6823100952053665e-11` | `1.3197896109318208e-6` | `-8.823249473821626e-7` |
| a2/coefficient two | `2.2059794732576243e-6` | `2.20621558276457e-6` | `-2.3610950694585853e-10` | `6.656001151128521e-6` | `-4.450021677870897e-6` |

The maximum compiler-induced width delta is `2.624551131980013e-10`, below the frozen numeric row tolerance `5e-10`. The maximum source-law/prediction residual is `4.450021677870897e-6`, almost four orders larger than that tolerance. Exact compiler E/G therefore does not repair the prediction law, and failure of an absolute row after exact compiler E/G is not classified as compiler evidence.

The discrete quadrupole strength ratios are:

```text
a1: 5.042641571922343
a2: 5.042646085647134
target: 5.042687988984065
```

Both remain inside the frozen `1%` tolerance. The held/train ratios are

```text
unit:            0.9027549676064812
coefficient two: 0.9027557756725354
```

so stronger `a=2` order remains false. All row centroid shifts are below `8.7e-19`; maximum strength-row boundary norm-weight upper bound is `2.9034258909069712e-6`, below the frozen `0.10` ceiling. This is a trace/norm diagnostic, not a probability. One-step train and held discrete factors have inverse residual `4.028931043606939e-15` and zero norm error.

## Covariance, deletion, mass, and contact

The full 448-dimensional uniform discrete operator is carried through all 24 proper-cubic frames. Maximum operator covariance residual is zero. The scope is the complete local operator plus structural signed-direction schedule; rotated L13 width rows are inherited from the labelled Cycle435 family and are not rerun as a 24-by-four prediction Cartesian product. There is no global resort.

Independent deletion signals are:

| deletion | operator/state signal |
|---|---:|
| local source flag | `4.971078783477255` |
| one Z20 quantum | `3.389650679154598e-05` |
| one coefficient bit family | `2.029578078049524` |
| one Suzuki factor | `0.42513156597523016` |
| quadrupole sign column | `1.6329931618554523` |

Malformed group, cell, coefficient width, route, direction permutation, geometry, and strength inputs are refused. Field stream, packet FSWAP, and contact remain the unchanged Cycle453 factors; they are not silently absorbed into the actuation compiler.

The one-particle mass remains `0.4534056541748851` with eigen residual `3.534751832054436e-16`. The Cycle-230 contact retains 645 nontrivial columns per declared block and changes the declared two-particle probe by `0.36789306705608243`.

## L13 response resources and the still-open shell

For a conservative constant-overhead envelope, Cycle487 assigns one disjoint 64,000-M2 Cycle484 work block per L13 coarse cell. This is an explicit upper-bound construction, not a minimal layout and not a claim that Cycle453's size-dependent three-M64 shell/effect encoder has been built.

| resource | value |
|---|---:|
| L13 cells | `2197` |
| per-cell capacity | `64,000 M2` |
| total capacity | `140,608,000 M2` |
| used | `109,555,602 M2` |
| reserve | `31,052,398 M2` |
| selected per-cell pipeline | `35,082,887,764` events |
| one full response layer | `77,077,104,417,508` events |
| four-layer response schedule | `308,308,417,670,032` events |

The `35,082,887,764` per-cell pipeline is inherited verbatim from the exact frozen Cycle484 selected manifest; Cycle487 multiplies that literal count by the predeclared L13 cell count and depth without changing the gate decomposition.

The same controlled trace executes in every block; local source flags, not a host list of active cells, determine the active branch. The uniform P8 word preparation is supplied initial program data. Resource depth is not time.

This closes only the response-actuation sublayer's bounded schedule. Cycle484 does not provide Cycle453's size-dependent three-M64 shell encoding, field/effect encoding, or total emitted schedule. The prior L13 run remains a physical-shell resource refusal: it was stopped at `862.84 s`, maximum RSS `1,504,165,888` bytes, and peak footprint `3,892,677,920` bytes. The L13 physical-shell resource boundary is unchanged, not converted into an E/G failure.

## Supplied, derived, and open

Supplied:

- Cycle453 exact targets, route strengths, Q0/Q1 occupations, phase quadrupole, L13 geometries, factor order, packet preparation, and width observable;
- Cycle484 P8/floor rule, Suzuki4 factors and order, B20 basis and calibration, exact H/NCT premise, source flag, and fixed event manifest;
- uniform coefficient-two words, the fixed basis-order convention, initial program state, finite norms, thresholds, and readouts.

Derived:

- the exact local basis permutation and six actual Cycle453 discrete embeddings;
- actual train/held discrete prediction rows with compiler-induced delta separated from source-law/prediction residual;
- uniform local physical E/G, inverse, leakage, all24 covariance, deletions, mass/contact preservation, and bounded L13 response resources.

Open:

- four absolute Cycle420 rows and stronger-a2 order for a changed normalization, law, calibration, or finite domain;
- the complete L13 three-M64 physical shell/effect encoding and total resource schedule;
- retained Strang8 prediction rerun, basis/angle derivation, a fault model, optimized phase words, autonomous preparation, and recurrence;
- source/energy-stress calibration, physical duration, gravity, Records, Born/occurrence, and realized history.

Response is not gravity. Phase is not energy. A generator is not a rate. Depth is not time. A packet label is not a Record, and coherent norm is not an occurrence frequency.

## No-Go Discipline Gate

Gate status: **FAIL for any broad compiler, quadrupole, gravity, source-law, or axiom negative**. Only the selected finite L13/depth4 occupation-normalized Suzuki4 route is disposed against the four named rows and held order. There is no axiom pressure.

### N1 — Alternative route enumeration

Families are normalized by mathematical object, load-bearing mechanism, and terminal obligation.

| family | object / mechanism / terminal obligation | status and concrete evidence |
|---|---|---|
| adapted P8/Suzuki4/B20 occupation route | q1 fixed-point source star / discrete symmetric product / reproduce four rows and a2 order | `ATTEMPTED`; this runner reports all rows and misses the target |
| adapted P8/Strang8 occupation route | q1 fixed-point source star / retained eight-step product / reproduce four rows and a2 order | `ATTEMPTED` locally only; local compiler closes, but prediction terminal obligation is untested |
| source-angle strength encoding | fixed Q1 source / encode route strength in vertex angle / predict held rows without refit | `UNTESTED`; Cycle453 explicitly names this live normalization |
| coherent many-Q source | finite many-excitation source / mean occupation and recurrence / reproduce scale and order | `UNTESTED`; Cycle453 names this distinct state-space route |
| retarded-field packet join | Cycle213 field / retarded propagation / reproduce signed-profile detector rows | `UNTESTED`; different primary field object |
| reversible static-field packet join | Cycle216 field / static reversible approximation / reproduce four width rows | `UNTESTED`; different propagation invariant |
| held-out calibrated coupling | Cycle435 packet / train-only coupling map / predict three held-out coordinates | `UNTESTED`; different calibration obligation |
| larger or nonperiodic packet family | enlarged finite domain / boundary and readout convergence / stabilize a2 order | `UNTESTED`; different finite-domain obligation |

Only one family reaches the prediction terminal obligation. N1 therefore defeats every broad negative; the result stays a partial attempt.

### N2 — Wall-independence audit

The collapsed conditions are `N`, normalization/calibration; `D`, propagation/geometry; `C`, L13 shell/effect compilation; and `R`, operational readout. Exact prediction is the target, not another wall.

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| N,D | no | no | yes |
| N,C | no | no | yes |
| N,R | no | no | yes |
| D,C | no | no | yes |
| D,R | no | no | yes |
| C,R | no | no | yes |

Compiler E/G closes neither the source normalization nor the finite prediction law. The failing rows therefore cannot be promoted into compiler evidence.

### N3 — Hidden-wall scan

The artifact is scanned for the trigger families “we assume,” “by construction,” “as is standard,” “framework provides,” “bridge context,” “background,” “naturally,” “obviously,” “standard QFT,” “registered,” and “canonical.” No phrase supplies an undeclared premise. P8, B20, exact H/NCT, Suzuki order, uniform words, basis permutation, state preparation, geometry, factor order, targets, tolerances, initial program data, and missing fault model are explicit. The independent-block resource envelope is labelled supplied and nonminimal.

### N4 — Residual matching

| witness | witness residual | Cycle487 residual | match? |
|---|---|---|---:|
| `PHYSICAL_EXACT_STRENGTH_QUADRUPOLE_PREDICTION_BRIDGE_CYCLE453_NOTE_2026-07-19.md`, result table | four L13/depth4 absolute rows and a2 order | same targets, states, geometries, depths, and observable with only vertex changed | yes |
| Cycle453 L13 resource section | size-dependent three-M64 physical shell/effect encoding | complete L13 shell/effect remains unbuilt | yes |
| Cycle484 compiler note | P8/Suzuki4/B20 coefficient/product/angle/physical E/G | uniform local actuation compiler | yes |
| Cycle435 compiler | L7/L9 local physical block | L13 full shell | no; predecessor evidence only |
| Cycle420 impact-parameter surface | positive `b=(5,6,7,8,10)` exponent | quadrupole width | no; dropped |

No nonmatching citation is used to support the narrow disposition.

### N5 — Rhetoric audit

“Not repaired” means only the four finite L13/depth4 scalar rows and their held/train order. The local 448-dimensional operator, six restricted blocks, two L13 logical prediction geometries, and four scalar outputs are tested. A complete L13 physical shell, other source states, other product routes, larger domains, continuum limits, gravity semantics, and occurrence are not tested. No lattice-wide negative is stated.

### N6 — Partial-closure path scan

The retained Strang8 prediction, source-angle encoding, coherent many-Q source, retarded/static field joins, held-out coupling calibration, cached/localized shell, and larger-domain routes use existing candidate primitives and executable surfaces. They are import-retirement or implementation paths, not evidence for a new axiom.

### N7 — Steelman

A hostile reviewer should reject a source-law negative. Cycle487 shows that changing a continuous vertex to an exact physical discrete compiler barely changes the rows; it does not show that the Q1 occupation map or finite packet law is forced. Encoding strength in the source angle, using a coherent many-Q source, joining the Cycle213/216 field, or calibrating one train coordinate and predicting held coordinates can change absolute scale and separation order while retaining this exact compiler. The concrete terminal obligation is to reproduce all four frozen rows and a2 order without held refit. Those routes remain open.

### N8 — Cross-cycle echo and claim gate

Cycle432's two-source phase seam became Cycle435's three-source packet, and Cycle447's L9 boundary norm-weight failure became a Cycle450 L17 boundary norm-weight pass without changing the local law. Finite residuals have therefore been retired by composition and domain enlargement. The same mechanisms remain applicable here. Broad no-go, shared-obstruction, minimum-content, and axiom-pressure claims all fail; no axiom pressure is licensed.

## Reproduction

```bash
python3 -m py_compile scripts/physical_discrete_quadrupole_exact_strength_bridge_cycle487_2026_07_20.py
python3 scripts/physical_discrete_quadrupole_exact_strength_bridge_cycle487_2026_07_20.py
```

Acceptance requires zero failed checks, exact frozen input identities, the stated compiler/prediction separation, no held refit, and the declared wall/RSS caps. No axiom, foundation, Qualification, primitive, registry, policy, queue, audit, or control-plane surface is edited.

The definitive cold run reports `15` passes, `0` failures, `8.947971458081156` seconds elapsed, and `855.515625 MiB` peak RSS under the frozen `700 s / 3072 MiB` caps.

An independent root cold rerun returned the same `15 PASS / 0 FAIL`. Its
complete process measured `91.56 s` real, `87.88 s` user, and `1.07 s` system,
with `899,481,600` bytes maximum resident set size. The controlled runner body
measured `8.070723333046772 s` and `857.8125 MiB` peak RSS. The packaged runner
SHA-256 is
`b0e4ac4aea641dbf90f64ac6d944b639b983ec76e365c3a60377b1ea2b5cf091`.
