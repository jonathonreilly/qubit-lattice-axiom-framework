# Physical local-bond / translation-character A/B science train — Cycle 509

Date: 2026-07-20

Authority: **none**

Audit: **unset**
Disposition: **valid train packet; Route A partially constructive; Route B
outside its frozen observable domain; Route C and held open**

## Result up front

The repaired, independently reviewed Cycle-509 evaluator executed the frozen
34-row A/B train manifest exactly once and atomically published a complete
packet.  Packet integrity passes: the receipt/hash DAG, dependency bundle,
strict JSON surfaces, manifest, row identities, artifact schemas, all 408
nonmetadata logical-array hashes, and aggregate-gate recomputations agree.

The science result is mixed and bounded:

1. Route A's physical local bond-current field is constructive on the declared
   finite apparatus.  All 17 Route-A rows pass their numerical, inverse,
   covariance, exact-Boolean mask, leakage, resource, and row-level controls.
   Six of the nine mass-grid rows have a sustained preregistered response;
   every row with probe `beta=-4pi/9`, plus its mirror, is instead
   `transient-unresolved`.  Thus Route A passes `6/10` primary-plus-mirror
   response gates, not the required `10/10`.
2. All seven Route-A deletions are valid and primary-sensitive.  In particular,
   the local field resolves emitter, collision, mediator stream, contact,
   probe coin, source-mass factor, and probe-mass factor on the frozen middle-
   mass comparison.  This is positive local interaction/source-response
   evidence; it is not yet a selected universal law.
3. The measured update-1 active-mediator ledger is probe independent and has
   source-mass exponent `1.9978283424419019` against target `2 +/- 0.15`.
   The composed Route-A response nevertheless misses the frozen scaling gates:
   `R/F` population CV is `0.2618097060407261 > 0.25`, and the maximum
   nontrivial source/probe swap-log residual is `0.6427776809657473 > 0.25`.
4. Route B is not a null response.  Its global translation-character
   observable is **undefined on every train row under its own frozen law
   domain**: every row has `8/12` update-axis character pairs below the `0.05`
   magnitude floor (`136/204` overall; row minima range from zero to
   `0.0019055163373704878`).  The evaluator consequently emits no Route-B
   response statistic and makes all Route-B deletion/scaling claims
   ineligible.  The raw carried character/phasor covariance remains at
   roundoff; the reported response-covariance value `1.0` and derived response
   floor `10.0` are explicit invalid-domain sentinels, not measured residuals
   or physical response thresholds.
5. The Cycle-219 one-particle mass fixture and both route mirror relations pass.
   Route C remains unimplemented (`8` train rows), and no held row ran.  The
   A/B candidate-law result therefore cannot establish a route-independent
   obstruction, no-go, minimum content, or axiom pressure.

`active_mediator_weight_update1` is a dimensionless ledger weight, not energy.
The local bond current is not force or gravity.  A translation-character phase
is not momentum, energy, time, or a rate.  Update count is not time.

## Frozen evidence and replay identity

| item | exact value |
|---|---|
| repaired science runner SHA-256 | `970deb948966b8fc9b8d16233225356871f287d16ce34500897cb2cb441fe667` |
| A/B train manifest SHA-256 | `f6dfdbd48ef38a10f2b7659ef5192950a0c17c257c042be8515da355999a44b2` |
| ordered row-identity SHA-256 | `9dbdd66166e329aa3b3f3f36ca1926a77fb73349fa4b3c69d39fdf6b4d4591a4` |
| dependency-bundle SHA-256 | `79d57efb95a221ec7aa6735a981b1f6a99852eb8c068d671b7e847157f7c251e` |
| science-result SHA-256 | `fed10c31661cc1d2e5a3f0f2b04a9e06dcb32913621b032b39c177d35b41a7ba` |
| run-receipt SHA-256 | `efa4e44da10bb2f5d968ededc5db8b2e9a6e9ec34bbfed278443271411b1d413` |
| artifact-index SHA-256 | `6974e078649be33bddade6bb6f3598aab909ffd68b6301a75e53bb707d38cffe` |
| accepted row artifacts | `34` (`17` Route A, `17` Route B) |
| row-artifact bytes | `454763 <= 67108864` |
| nonmetadata logical members verified | `408` |
| verdict | `science-train-complete-with-failed-gates` |

The final packet is
[`outputs/physical_local_bond_character_ab_train_cycle509_2026_07_20`](../../../../outputs/physical_local_bond_character_ab_train_cycle509_2026_07_20).
It contains exactly 34 content-addressed row NPZ files plus the artifact index,
science result, transcript, preserved qualified-resource transcript, and run
receipt.

Attempt 1 had sealed all rows before failing in outcome-independent host
post-processing.  The accepted replay pairs all 34 complete row identities
one to one with those quarantined artifacts.  All 408 nonmetadata logical
hashes are exact.  Differences are confined to
`science_runner_sha256` and `dependency_bundle_sha256`; the corresponding 34
metadata-member hashes, NPZ container hashes, and content-addressed filenames
change as required.  The compact comparison receipt is preserved at
[`outputs/physical_local_bond_character_ab_science_train_cycle509_replay_comparison_2026_07_20.log`](../../../../outputs/physical_local_bond_character_ab_science_train_cycle509_replay_comparison_2026_07_20.log).
No attempt-1 response value was used to repair or refit the evaluator.

## Exact execution and technical controls

The manifest contains 18 primary mass-grid rows, two mirrors, and 14 selected
deletions.  It performs 1,734 forward trajectories, 8,670 forward update calls,
34 inverse trajectories, and 170 inverse update calls.  Route C and held both
execute zero rows; no refit occurs.

Every row remains below the 600-second / 3,000,000,000-byte / zero-swap resource
contract.  Maxima over all 34 rows are:

| control | maximum |
|---|---:|
| per-row elapsed including compression/reopen | `105.45870508404914 s` |
| parent elapsed including spawn/compression/reopen | `106.00401962501928 s` |
| maximum RSS | `2128003072 B` |
| swaps | `0` |
| norm residual | `1.892930256985892e-13` |
| mediator-charge residual | `1.892930256985892e-13` |
| CAR-number residual | `4.884981308350689e-15` |
| CAR-kernel residual | `1.1966678176173787e-14` |
| lawfulness residual | `6.708098480166867e-16` |
| post-stream continuity residual | `1.4849232954361469e-15` |
| inverse residual | `1.7385100217872207e-15` |
| all-24 full-state covariance residual | `3.0557789129187147e-16` |
| elementwise exact-mask mismatch count | `0` |
| mass-fixture residual | `4.440892098500626e-16` |
| source-ledger update-1 residual | `1.3877787807814457e-17` |
| boundary-shell weight | `0` |
| Route-A structural-cone leakage | `5.273559366969494e-16` |
| Route-B post-word structural-cone leakage | `8.326672684688674e-17` |

The aggregate `technical=false` is exactly the conjunction of all 34
`row_pass` fields: Route A is `17/17`, while Route B is `0/17` because the
frozen all-axis character-domain gate is false and its response-covariance
summary uses the declared invalid-domain sentinel.  It does not mean that the
NPZ artifacts, resources, state covariance, masks, or numerical evolution
failed.

## Route A — local bond-current field

The nine primary morphology classifications form a probe-beta-dependent
pattern:

| probe beta | sustained | transient-unresolved |
|---|---:|---:|
| `-2pi/9` | `3/3` | `0/3` |
| `-4pi/9` | `0/3` | `3/3` |
| `-2pi/3` | `3/3` | `0/3` |

The `-4pi/9` mirror is also transient-unresolved.  Its carried-response and
laboratory-axis sign-reversal residuals are both
`4.2869353900076845e-16`, so the classification is not a covariance failure.
The transient rows miss the frozen final-two signed-coherence gate (about
`0.74849 < 0.90`) rather than the numerical or support controls.

Primary response statistics across the nine grid rows range from
`1.2146336640280473e-08` to `9.251041398031538e-07`.  The seven middle/middle
deletions have the following literal dispositions:

| deletion | valid | contract pass | disposition |
|---|---:|---:|---|
| emitter | yes | yes | `primary-sensitive` |
| collision | yes | yes | `primary-sensitive` |
| mediator stream | yes | yes | `primary-sensitive` |
| contact | yes | yes | `primary-sensitive` |
| probe coin | yes | yes | `primary-sensitive` |
| source-mass factor | yes | yes | `primary-sensitive`; factor effect observed |
| probe-mass factor | yes | yes | `primary-sensitive`; factor effect observed |

This is the strongest constructive Cycle-509 result: the physical dynamics
produce a covariant, contact-sensitive, deletion-resolving local response on
the exact structural cone.  The frozen all-grid sustained/scaling law is not
qualified.

## Route B — global translation character

The raw direction-carried data remain coherent: the mirror response-phasor
conjugacy residual is `1.2352503815958116e-16`; independent inspection of the
retained arrays gives raw carried character covariance at most
`6.3286e-15` and raw phasor covariance at most `7.2000e-16` wherever defined.

But the frozen observable requires both interacting and matched-free
characters to have magnitude at least `0.05` for every retained update-axis
pair.  The directed finite apparatus leaves transverse characters far below
that floor.  Consequently:

- `character_floor_valid=false` on `17/17` rows;
- primary-plus-mirror response gates pass `0/10`;
- the response statistic and scaling coordinates are undefined;
- all seven deletion dispositions are `invalid`; and
- no null, transient, sustained, swap-scaling, or source-law conclusion may be
  drawn from Route B.

This is a route-observable/domain failure.  It neither falsifies Route A nor
tests the localized multi-mediator Route C.

## Supplied, derived, and open inventory

Supplied:

1. the Cycle-219 coin family and mass coordinates, Cycle-230 contact, Cycle-501
   exchange, Cycle-441 source ray, emitter/collision angles, factor comparator,
   train geometries, response windows, thresholds, and selected deletions;
2. the source/probe beta grid, finite torus, source/probe locations, frame
   action, boundary, initial sector, and matched-free construction; and
3. the choice of local bond current for Route A and global translation
   character for Route B.

Derived on the frozen train domain:

1. exact full interacting-minus-free local/plane bond fields and their
   factorized symmetric Boolean structural cones;
2. exact all-24 state, response, and mask transport; inverse, continuity,
   leakage, resource, mirror, deletion, source-ledger, and one-particle checks;
3. the Route-A morphology/deletion/scaling dispositions above; and
4. the exact Route-B character-domain exclusion above.

Open:

1. the eight-row localized multi-mediator Route-C train implementation;
2. the frozen 12-row held evaluator, which must remain atomic across A/B/C;
3. a common source/response law that survives all masses, routes, deletions,
   held sizes, and covariance controls;
4. physical selection or genesis of beta, source/profile, contact, initial
   sector, apparatus, and observable;
5. additive conserved physical energy/stress/source, metric/lapse coupling,
   clock calibration, probability, Records, and realized history; and
6. arbitrary-volume bounded-radius compilation, preparation, recurrence, and
   protection.

## Six-wall ledger

| wall | exact movement | residual |
|---|---|---|
| `C_ref` | none claimed | preparation, phase/zero, coupling, and normalization remain supplied |
| `C_num` | the physical emitter ledger is measured and probe independent with exponent `1.9978283424419019` | no number reference, energy, probability, or source selection follows |
| `C_wrap` | none claimed | finite update index and character phase are not time, winding, or a rate |
| `C_int` | Route A locally resolves contact, collision, stream, coin, and both mass factors with exact deletions | uniform sustained morphology, occurrence/rate/protection, and law selection remain open |
| `C_local` | exact Boolean cones, retained local fields, bounded updates, and all-24 transport pass on A/B train | Route B's observable domain fails; Route C and held remain open |
| `C_source` | the emitter ledger has the target quadratic exponent and Route A produces a local response | the composed scaling comparator fails, and no selected conserved energy/stress/source or gravity meaning exists |

No TOE lane percentage moves on train-only, route-incomplete evidence.  The
fixed campaign scores remain operational quantum/Records `90/49/99`, causal
time `65/40/99`, matter/inertia `80/42/99`, gravity/source/resource
`59/30/94`, and Born/probability/realized history `76/44/99`, where each triple
is integrated / strict / conditional planning maturity rather than probability
or audit status.

## No-go discipline and next campaign

No impossibility, minimum-content, or axiom-pressure claim is made, so an N1-N8
no-go verdict is not applicable.  Route A survives constructively, Route B is
observable-specific, Route C remains unimplemented, and held data are absent.

The next decisive campaign is therefore constructive: implement Route C by
joining Cycle 419's local seven-mode field/port alphabet to the physical matter
compiler, execute its frozen eight-row train complement, and only then unlock
the atomic A/B/C held evaluator.  A route-independent statement remains
forbidden until all three constructive routes and held controls have actually
run.
