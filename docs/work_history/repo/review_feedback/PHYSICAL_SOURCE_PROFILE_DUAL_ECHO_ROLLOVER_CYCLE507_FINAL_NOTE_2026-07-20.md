# Physical source/profile dual-echo rollover — Cycle 507 final note (2026-07-20)

Authority: none

Audit: unset
Disposition: **FINITE TRAIN + BLIND-HELD POSITIVE FOR SEPARATELY SUPPLIED D/A PROGRAMS; LAW GENESIS, SIZE-UNIFORM LOCALITY, OCCURRENCE, AND PROPER TIME REMAIN OPEN**

## Frozen evidence chain

### Preflight

- runner `scripts/physical_source_profile_dual_echo_rollover_preflight_cycle507_2026_07_20.py`
  - SHA-256 `228b37f92069117aac5a13023bbc11e32188bc4d3425815bdec366aa06ffa3c3`
- note `docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_PROFILE_DUAL_ECHO_ROLLOVER_PREFLIGHT_CYCLE507_NOTE_2026-07-20.md`
  - SHA-256 `3b81720d0589a4d523d2eeee5a9624132602a76aa7ee19caf32466279279cc9f`
- train manifest SHA-256 `7c98084fbc3ef6c64879e6994127984464a6c3cb625d9038d966b91bd7d36ed3`
- blind-held manifest SHA-256 `3a3814d2cac73bcf94ccc1f9ea2427fe098b2de861524dc02a5be84a91fc9e3f`

### Accepted train

- runner `scripts/physical_source_profile_dual_echo_rollover_train_cycle507_2026_07_20.py`
  - SHA-256 `03403653f941ec344db5045efe62ba2ea58151353caaca3a5e06e753964b39d6`
- train note `docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_PROFILE_DUAL_ECHO_ROLLOVER_TRAIN_CYCLE507_NOTE_2026-07-20.md`
  - SHA-256 `ec404d12805cf79bbc61c589317ab786e8b2b059100843db9a9e77016bb7dcd7`
- canonical train transcript `/tmp/cycle507_train_full_2026-07-20.txt`
  - SHA-256 `15e77c1723c58536272a8e286abfd8eb45be90361ae25c2523e4c82034920c51`

### Held evaluator and dry contract

- held-only evaluator `scripts/physical_source_profile_dual_echo_rollover_held_cycle507_2026_07_20.py`
  - eligible frozen SHA-256 `49c9dd6863dff860a90a55609c9246fe03ebf0aae66d22e5d5b0de7f352ad04f`
- repaired dry-contract transcript `/tmp/cycle507_held_dry_contract_2026-07-20.txt`
  - SHA-256 `cce46a39e7b5b593349602f398d3fd19a7f7e752d93de993421e583c0445ee73`
  - result `4/0`, held evolution `0`

### Invalid first held invocation — implementation evidence only

- transcript `/tmp/cycle507_held_full_2026-07-20.txt`
  - SHA-256 `d0a3be83a1f9fd8269b2612946c7399ce8542507cde0afc311e2909a7ebf19f6`

The first held invocation is **not scientific evidence**. It failed before any `HELD_ROW` or held control because the extra-clock helper used ascending adjacent swaps instead of the inherited Cycle-444 descending `CLOCK_FORWARD_SWAPS`. The resulting hot-clock permutation left an automorphism work carrier dirty. All row predictions, E/G residuals, inverse residuals, signatures, wrap indices, and carry counts from that invocation are unset.

Root classified this as a pre-row implementation error, not refit. The sole semantic repair imported the inherited Cycle-444 forward swap order exactly and reversed that order for inverse. A new cheap dry fixture then checked:

- K14 baseline-plus-extra forward response ends at K0 with work blank;
- K15 baseline-plus-extra forward response ends at K1 with work blank;
- both inverse words restore the initial clock and blank work.

No manifest, threshold, target ratio, response law, source sector, mass route, apparatus geometry, or decoder contract changed.

### Eligible held invocation

- transcript `/tmp/cycle507_held_full_eligible_2026-07-20.txt`
  - SHA-256 `98b6bbe4c88af6e9b5f64b0bfb382f41f1e89e6ae2f5b7870d243436f1b2d2ab`
- result `CYCLE507_HELD_CERTIFIED`
- suite checks `7/0`
- blind-held primary rows `2/2` accepted
- held controls `12/12` rejected
- train rows executed by the held runner `0`

The invalid and eligible transcripts are intentionally distinct. Only the eligible transcript supports the held result below.

## Strongest constructive result

Cycle 507 supplies a finite, size-specific, reversible compiler family joining:

1. the actual coherent Cycle-441/451 nine-M2 register x eight-M2 local-mode source controller;
2. a separately supplied physical two-M2 D/A program;
3. a supplied five-M2 common profile identity;
4. two independently prepared equal `ell=2` Cycle-504 echo/clock/rollover corridors;
5. retained register/local/program/profile endpoint bindings, response receipts, carry receipts, epoch rollover, and predecessor lineage.

The receiver-zero and local-mode-7 sectors are never replaced by a selected classical receiver bit. They remain together in the same coherent joint state. Receiver squared norms are diagnostics only; they are not probabilities, occurrences, branch selections, Records, or actuality.

On the declared code spaces, the represented physical update satisfies

`E G_coarse = G_physical E`

with exact represented-state residual zero and exact inverse residual zero in every executed train and blind-held primary row.

The construction uses no host-selected corridor length, host cadence, decoder schedule, beta-to-program lookup, squared-norm threshold, or receiver lookup. It therefore answers the narrow Cycle-507 question positively for this finite conditional compiler family. It does **not** derive why D is prepared on train or A on held, and it does not derive lapse, proper time, occurrence, a Record, or actuality.

## Train result — supplied D

Train freezes:

- horizon `N=8`;
- start clock `K1`;
- two equal `ell=2` corridors;
- three source sectors `{-2pi/9, -4pi/9, -2pi/3}`;
- both `{cayley, principal}` mass routes;
- physical `one_hot_2(DELAY)` program.

All six primary rows retain, in one coherent state:

- receiver-zero reference/probe totals `32/32`, ratio `1`;
- local-mode-7 reference/probe totals `32/24`, ratio `3/4`.

Across all six rows:

- E/G residual `0`;
- inverse residual `0`;
- controller-population residual `0`;
- response work residual `0`;
- endpoint-binding failures `0`;
- response-receipt failures `0`;
- maximum floating norm residual `2.4424906541753444e-15`.

All thirteen frozen train controls reject. The train extra-wrap control was only a schema-level pre-held rejection because D did not exercise the A trajectory. The eligible held run below upgrades that one narrow control to trajectory-level evidence.

## Blind-held result — supplied A

Blind-held freezes:

- horizon `N=16`;
- start clock `K2`;
- two equal `ell=2` corridors;
- source sector `-8pi/9`;
- both `{cayley, principal}` mass routes;
- physical `one_hot_2(ADVANCE)` program;
- no refit.

Both held rows retain receiver-zero and local-mode-7 histories together:

| Mass route | receiver-zero squared norm diagnostic | local-mode-7 squared norm diagnostic | receiver-zero signature | local-mode-7 signature | norm residual |
|---|---:|---:|---|---|---:|
| Cayley | `0.9058152186837951` | `0.09418478131620465` | `(64,64,1)` | `(64,80,5/4)` | `3.3306690738754696e-16` |
| principal | `0.9985998415077789` | `0.001400158492221208` | `(64,64,1)` | `(64,80,5/4)` | `2.220446049250313e-16` |

For both routes:

- E/G residual `0`;
- inverse residual `0`;
- response-work exhaust residual `0`;
- endpoint-binding failures `0`;
- response-receipt failures `0`;
- reference carries `4`;
- local-mode-7 probe carries `5`.

The physical A trajectory exercises both wrap kinds. Application indices are zero-based:

- ordinary response wrap at application `11`;
- extra response-step wrap at application `23`.

The ordinary K15 load and the A-enabled extra K14 load are mutually exclusive and feed the same Cycle-504 carry/epoch conveyor. Final K0/K1 clears return the work carrier blank. The exact coarse map independently reproduces the five probe carries and endpoint epoch/clock words.

## Held deletion and comparator controls

All twelve held controls reject:

| Control | Eligible held disposition |
|---|---|
| label courier | binding failures; rejected |
| reference profile binding | reference binding failures; rejected |
| probe profile binding | probe binding failures; rejected |
| receiver control | mode-7 becomes `64/64`; rejected |
| ADVANCE enable | mode-7 becomes `64/64`; rejected |
| extra-clock word | mode-7 becomes `64/64`; rejected |
| response receipt | receipt failures; rejected |
| ordinary-wrap carry | dirty physical work/domain rejection |
| extra-wrap carry | dirty physical work/domain rejection |
| reference RETURN | endpoint lineage/payload domain rejection |
| probe RETURN | endpoint lineage/payload domain rejection |
| host length/cadence/source lookup comparator | lacks equal-geometry receipts, physical A carrier, and schedule-free decoder |

Unlike train, held physically traverses both ordinary and extra response-wrap columns. The extra-wrap deletion is therefore now trajectory-level rather than schema-only evidence.

## Locality, covariance, and resource boundary

| Split | M2 sites | logical terminal gates | maximum support | compact forward-plus-restoration SWAPs | compact elementary operations | all-24 adjacency failures |
|---|---:|---:|---:|---:|---:|---:|
| train N8 | `1562` | `1451` | `3` | `6,742,818` | `20,230,291` | `0` |
| held N16 | `2882` | `2833` | `3` | `24,543,536` | `73,634,083` | `0` |

The source/mass target residual is zero for both mass routes. The maximum inherited all-24 source-operator covariance residual is `8.830824800525959e-16`.

The eligible held invocation used:

- `130.87 s` real time under `/usr/bin/time -lp`;
- `941,441,024` bytes maximum resident set size;
- `1,025,770,672` bytes peak memory footprint;
- zero swaps.

This resource statement has two mandatory qualifications:

1. `evolved_joint`/`joint_state` and the courier helpers evaluate the optimized exact logical CNOT/Toffoli effect on each coherent label component. They do not replay every courier gate separately for every amplitude.
2. Restored-line locality is a compact exact route certificate. Operand existence, support at most three, route counts, restoration by construction, and all-24 carried line adjacency are checked, but tens of millions of adjacent elementary operations are not materialized and replayed.

The result is a finite size-specific restored circuit, not a bounded-depth or bounded-radius arbitrary-N QCA and not the Cycle-230 M64-to-physical-M2 compiler.

## Supplied, derived, and open inventory

### Supplied

- one common opportunity interval delta and finite N8/N16 apparatus members;
- Cycle-441 source-sector preparations and Cayley/principal candidate mass routes;
- actual Cycle-451 source compiler and selected-rail transport;
- physical D on train and physical A on held;
- profile identity, distinguished probe edge, equal `ell=2` corridor preparations;
- blank finite endpoint/carry/receipt banks, restored line placement, and noiseless reversible gates.

### Derived on the frozen finite domains

- coherent receiver-zero `4:4` and local-mode-7 D `3:4` retained train histories;
- coherent receiver-zero `4:4` and local-mode-7 A `5:4` blind-held histories;
- exact represented E/G equality, inverse, work exhaust, binding, receipt, lineage, and carry behavior;
- physical ordinary and extra response wraps through one epoch conveyor;
- exact finite resource counts and all-24 carried line covariance;
- train and held deletion/comparator dispositions above.

### Still open

- genesis or selection of source sector, mass route, D/A program, profile, delta, identities, and apparatus;
- a local interaction deriving D versus A rather than accepting a supplied program;
- bounded-radius arbitrary-N physical-M2 compilation and noise protection;
- a universal clock metric, synchronization theorem, continuum/Lorentz limit, lapse, or proper time;
- occurrence, framework Record formation, permanence, realized-history selection, or actuality;
- conserved physical energy/stress/source and gravity meaning;
- Born/probability interpretation of receiver squared norms.

## Six-wall dependency ledger

| Wall | Exact Cycle-507 movement | Residual |
|---|---|---|
| `C_ref` | actual source/register/local/program/profile carriers are coherently transported and retained at both corridor endpoint families | physical preparation/genesis and why D versus A is selected remain supplied |
| `C_num` | no movement is claimed; both receiver sectors remain coherent and their squared norms are diagnostics only | number reference, cross-number observability, Born/probability, and occurrence remain open |
| `C_wrap` | materially advances on the finite apparatus: N16 executes four reference and five probe carries, including ordinary and extra response wraps with retained epoch/endpoint consistency | finite conveyor order is not time; universal unwrapped clock coordinate and proper time remain open |
| `C_int` | supplied D/A response words are compiled into reversible local clock-step controls with exact deletions | the response law, physical rate, stability/protection, and interaction-based D/A selection are not derived |
| `C_local` | every represented terminal gate has support at most three with exact finite restored routing and all-24 covariance | routing is size-specific/global; no bounded-radius arbitrary-N QCA and no M64 CAR-cell compiler follows |
| `C_source` | the inherited physical source controller is coherently compiled, transported, and bound to retained histories | no conserved physical energy/stress/source ledger or gravity coupling is obtained |

## N1-N8 no-go discipline and route disposition

### N1 — normalized routes

1. **Actual joint controller + equal corridors.** Mechanism: local-mode-7 and a physical D/A word control a distinguished response step. Terminal obligation: train D `3:4`, held A `5:4`, receiver-zero `4:4`, inverse, rollover, couriers, receipts. **Finite train + held positive.**
2. **Fixed short/neutral/long supergraph.** Mechanism: transported label controls a reversible local route switch. Terminal obligation: restored switch and equal external endpoints. **Open/untested.**
3. **Edge-token transducer.** Mechanism: reversible source-labelled 3/4/5 token accumulator. Terminal obligation: renewable blank work and retained lineage. **Open/untested.**
4. **Joint source x dual-clock block operator.** Mechanism: operator-first coherent accumulator control. Terminal obligation: sparse physical compiler without beta/projector lookup. **Open/untested.**
5. **Common-profile handshake.** Mechanism: transported rendezvous certificate admits suppressed/extra step. Terminal obligation: autonomous certificate genesis/consumption. **Open/untested.**
6. **Source mediator collision.** Mechanism: local boundary scattering changes certified probe emissions with mediator ledger. Terminal obligation: size-stable source/clock scattering compiler. **Open/untested.**

### N2 — wall independence

Finite response compilation, D/A law genesis, bounded-radius scaling, Record occurrence, continuum metric/proper time, and conserved stress/source remain independent. The positive finite route does not collapse the others.

### N3 — hidden-wall scan

Common delta, finite apparatus size, equal corridor preparations, source sector, mass route, D/A word, profile identity, distinguished edge, blank banks, exact gate order, restored routing, and noiseless gates are supplied.

### N4 — residual matching

The finite Cycle-451 joined-response and Cycle-504 source-conditioned rollover residuals are matched for the frozen D and A inputs. D/A genesis, arbitrary-N physical locality, Record/actuality, continuum proper time, and conserved source/stress are not matched.

### N5 — rhetoric audit

“No host-selected length” applies to this equal-geometry classifier, not every possible physical switch. “No host cadence” applies to this retained decoder, not every autonomous transducer. “No beta lookup” means the program is physically supplied, not that the source derives D/A. “Held positive” means two frozen N16 rows, not a scaling theorem.

### N6 — partial-closure paths

Replace supplied D/A preparation with a local source interaction; test the supergraph and token routes; compile the finite circuit into a bounded-radius tiling; add independent occurrence/Record laws; and seek a synchronization/continuum metric only after those carriers exist.

### N7 — hostile steelman

A fixed supergraph remains a viable alternative: one immutable geometry can contain every route while a transported local label operates a reversible switch. It could remove the present step-control implementation and restored-line scaling wall without changing host corridor length.

### N8 — cross-cycle echo

Cycle 451 introduced a co-registered dual clock; Cycle 504 introduced renewable endpoint and rollover carriers; Cycle 507 composes them with an actual coherent source controller and physical response word. Prior closures came from adding explicit physical carriers. A future failure of size-uniform compilation therefore could not establish a broad no-go while the supergraph, transducer, operator, handshake, and mediator routes remain live.

Broad no-go gate: **FAIL / DO NOT SHIP**.

Shared substrate obstruction: **not established**.
Axiom pressure: **none**.

## Final disposition

The priority equal-corridor/controller route is positive on both frozen finite splits. Cycle 507 now supplies a conditional coherent source/profile/response compiler whose retained histories reproduce train `3:4` and blind-held `5:4`, while receiver-zero remains `4:4`, without host length, cadence, decoder schedule, source lookup, or branch selection.

The optimal next campaign is to remove the separately supplied D/A law interface: attempt a local source/controller interaction that physically generates the response word while keeping the current equal-corridor E/G, rollover, inverse, deletion, and held-size controls frozen. In parallel scientific terms, the fixed-supergraph route remains the strongest independent alternative to the present step-control mechanism.

No axiom, foundation, Qualification, primitive, registry, policy, queue, or audit-status file was edited. No stage, commit, push, merge, or PR action occurred in this lane.
