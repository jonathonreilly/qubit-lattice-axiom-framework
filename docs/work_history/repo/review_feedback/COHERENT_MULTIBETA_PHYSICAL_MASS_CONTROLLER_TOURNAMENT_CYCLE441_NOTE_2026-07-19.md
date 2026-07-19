# Coherent multi-beta physical mass-controller tournament — Cycle 441

Date: 2026-07-19
Authority: none
Audit: unset

## Result

Cycle 441 is a positive coherent multi-beta physical tournament. It physicalizes the abstract Cycle-220/221 nine-state phase register as the complete Q=1 sector of nine hard-core M2 and joins it to the Cycle-311 constrained one-particle M64 code. One common physical M64 x register coin then acts on four coherent beta/rest sectors. Matrix functions of the same represented register drive both the Cycle-437 clock/latch and Cycle-429 active-source/distinct-receiver law.

The result removes the beta-specific host lookup used in Cycles 437 and 438 for two supplied candidate coordinate laws. It does not select those laws or the physical register. The nine-cycle, its internal orientation, one-hot population, Cayley resolvent, principal logarithm, conversion scales, source preparation, and bounded dense completions remain supplied.

Route A: operator functional calculus constructs every candidate operator from the represented nine-cycle before spectral analysis. Route B: explicit finite lookup table constructs projector sums only after beta eigenpairs are available. The distinction is executable, not rhetorical.

Route A is constructed before spectral analysis. It supplies a held alias prediction without refit. The separate Cycle-219 mass fixture remains a preservation control.

The construction tests four coherent beta/rest sectors: three unaliased train sectors and the held alias sector `beta=-8 pi/9`. Both functional coordinates predict the held clock and receiver responses without refit. Principal-phase and Cayley coordinates remain unselected.

## Exact executable results

| control | final cold maximum or count |
|---|---:|
| final cold summary | `12 pass, 0 fail` |
| nine-M2 menu Gram residual | `2.6665449647222835e-15` |
| deleted register-amplitude Gram residual | `0.2939723678960654` |
| complete 54D physical M64-register E/G/inverse maximum | `8.036692772324701e-15` |
| clock E/G/inverse/norm maximum | `1.1778237642499913e-15` |
| local physical recoil E/G/family maximum | `7.994332677118645e-15` |
| full receiver physical E/G/inverse/leakage/norm maximum | `8.555378627761456e-13` |
| coherent full-receiver forward E/G bound | `2.0314578631174372e-14` |
| coherent full-receiver inverse bound | `2.2506428754180096e-14` |
| three-application coherent receiver inverse | `3.5712526367486405e-15` |
| maximum train functional clock difference | `3.469446951953614e-16` |
| maximum train functional receiver difference | `4.743384504624082e-19` |
| held clock dark-weight difference | `0.7507628370353518` |
| held receiver difference | `0.002536090560596383` |
| B4/A Cayley four-sector operator residual | `2.6836573245561836e-14` |
| all-frame coin/recoil/encoder maximum | `0.0` |
| proper-cubic frames | `24` |
| Cycle-219 mass-fixture residual | `0.0` |
| Cycle-230 contact nontrivial columns | `645` |
| lawful-domain rejections | `9` |

The `12/0` summary is from the final cold rerun after the note and runner were frozen.

## What is physicalized

The register is a literal nine-M2 hard-core block. Its declared mass-controller code is

```text
Q_register = 1,
span{|100000000>, ..., |000000001>}.
```

The fixed cyclic unitary `S` maps internal site `j` to `j+1 modulo 9`. An explicit supplied nearest-neighbor implementation uses the eight-SWAP sequence

```text
(7,8), (6,7), (5,6), (4,5), (3,4), (2,3), (1,2), (0,1).
```

The orientation and sequential SWAP schedule are supplied internal structure. Proper-cubic covariance treats the register as a scalar internal block; it does not derive the ring from cubic geometry or make the schedule autonomous.

The complete register shift preserves Q=0, all 36 Q=2 basis states, and every other Hamming sector. The mass-controller functions are declared only on Q=1. A real mask validator accepts all nine one-hot masks and rejects actual Q=0 and Q=2 masks. The runner does not pretend that an unconditional exception is a domain test.

The matter factor is the Cycle-311 L6 constrained M64 code restricted to its six-dimensional `n=1` input slice. The full declared physical controller code is the complete nine-dimensional Q=1 register tensor this six-dimensional matter slice, so it has logical dimension 54. The scientific prediction subspace used below contains the four positive beta eigenrays tensored with the uniform M64 rest ray. Its physical rest support is 44 M2 plus the nine register M2, or 53 M2. Arbitrary coherent amplitudes across all four prediction sectors are tested explicitly.

The Q=1 population is supplied. No update here generates, selects, changes, combines, thermalizes, or measures beta populations.

## Route A: functional construction before spectral analysis

Route A receives only the represented operator `S`. Its constructor first checks that `S` is finite, odd-dimensional, unitary, and has no `-1` eigenvalue. It then constructs

```text
M_C(S) = 3 i (S-I)(S+I)^-1,
R(S)   = exp(i M_C(S)/3),
M_P(S) = -3 i Log_principal(R(S)).
```

The common register-direction coin is constructed directly as

```text
C(S)
 = R(S) tensor (P_scalar-P_even)
 + R(S) S tensor P_vector.
```

The two common clock controls are

```text
U_clock,C = exp(i M_C/8),
U_clock,P = exp(i M_P/8),
```

and the active recoil controls are

```text
U_source,C = exp(i 0.05 M_C tensor H_recoil),
U_source,P = exp(i 0.05 M_P tensor H_recoil).
```

These objects are built by linear solve, principal matrix logarithm, matrix exponential, and Kronecker product. No beta value, eigenvector, sector loop, projector, or coefficient table appears in the Route-A constructor. Only after the functional objects exist does the runner diagonalize `S` to prepare and analyze the four test sectors.

The anti-lookup audit inspects the constructor dependencies, enforces the construction-event order, and compares Route A with B3/B4. This is what makes Route A more than a disguised table.

The principal operator is a second common matrix function, not a beta loop. It recovers the Cycle-437/438 principal-phase alias on the held sector while the Cayley operator remains unwrapped. Constructing both does not select one.

## Route B: explicit tables

B3 explicitly loops over the three training eigenvectors and builds

```text
M_B3 = sum over train j of m_j |beta_j><beta_j|.
```

It has zero coordinate on the held ray. Consequently its held receiver weight is `6.563048884760345e-35`, numerical zero; it makes no held mass-law prediction.

B4 adds the held projector and its supplied coefficient. It then agrees with Route-A Cayley on the four-sector code to residual `2.6836573245561836e-14`, but it has consumed the held datum. This is interpolation by an explicit finite table, not a no-refit prediction.

Because the spectrum is finite, a sufficiently complete table can reproduce any function on the listed eigenrays. The scientific distinction is the supplied dependency: Route A defines one operator law for the entire supplied register before the test sectors exist; B4 imports every tested eigencoefficient separately.

## One common physical M64-register coin

Let `E_1` be the Cycle-311 constrained physical encoding of the six one-particle directions. The logical common code has dimension `9 x 6 = 54`. Its physical ambient vector has dimension `9 x 510 = 4590`.

The physical coin is the bounded encoded completion

```text
G_coin,physical(x)
 = x + E_1 [C(S)-I] E_1^dagger x,
```

with the register identity implicit in `E_1`. The 4590-by-4590 array is not materialized. The runner applies the physical completion columnwise to all 54 logical basis columns. Its full-matrix forward intertwiner, inverse, leakage, common-coin unitarity, and encoding-Gram residuals are respectively `3.272904068203772e-15`, `8.036692772324701e-15`, `2.374476422939924e-15`, `6.033455901590725e-15`, and `2.447531919918933e-15`.

The runner additionally reports exact E/G and inverse on each of the four beta/rest prediction rays and a seeded coherent superposition with all four amplitudes nonzero; their maximum is `1.478306064075587e-15`. The local Cycle-311 role-gauge constraint residual is zero. Thus sampled prediction rays are not being used as a substitute for the complete 54-dimensional common-coin check.

This is one physical common coin built from `S`, not four beta blocks assembled after spectral analysis. It is restricted to the declared one-particle controller code; it is not a new full-M64 multi-beta exterior-power theorem.

## Clock predictions

The same coherent register controls the complete Cycle-437 oscillator/Ramsey/latch code. Physical E/G and adjoint inverse are checked on the seeded four-sector coherent state. Projecting only for final analysis gives:

| sector | Cayley dark-word weight | principal dark-word weight |
|---|---:|---:|
| train 1 | `0.004650075052655355` | `0.004650075052655348` |
| train 2 | `0.024549534686926635` | `0.02454953468692671` |
| train 3 | `0.10181261542459183` | `0.10181261542459148` |
| held alias | `0.7638685896374817` | `0.0131057526021299` |

The complete support lies on bright word 3 and dark word 4. These coherent squared amplitudes are code diagnostics, not occurrences, probabilities, or a Born law. The reversible latch is not a Record.

## Active source and distinct receiver

The common operator recoil exponential acts jointly on the nine-M2 register and inherited 448-dimensional local recoil block. For every tested eigenray, the runner proves

```text
exp(i 0.05 M tensor H_recoil) (|beta> tensor |x>)
 = |beta> tensor exp(i theta_beta H_recoil)|x>
```

for both Cayley and principal functional coordinates. The maximum sectorwise equality residual against the inherited Cycle-429 scalar local vertex family is `1.186271949078011e-15`; the maximum operator-eigenvalue residual is `7.994332677118645e-15`.

The local physical recoil compiler uses the complete Cycle-311 M64 input encoding and checks E/G, inverse, norm, and leakage on all four basis rays plus their coherent superposition. The full receiver evolution carries a joint register/network state, not a classical beta label. After three declared applications:

| sector | Cayley receiver weight | principal receiver weight | B3 receiver weight |
|---|---:|---:|---:|
| train 1 | `7.688807414145454e-08` | `7.688807414145589e-08` | `7.688807414145532e-08` |
| train 2 | `2.149246178285616e-06` | `2.1492461782856412e-06` | `2.1492461782856213e-06` |
| train 3 | `3.7408602704048065e-05` | `3.740860270404854e-05` | `3.7408602704048404e-05` |
| held alias | `0.0025367020589446253` | `6.114983482422266e-07` | `6.563048884760345e-35` |

The receiver is read at `reservoir_site(receiver_cell)`, not at a source-local field index. The held functional difference is `0.002536090560596383`.

For a direct physical-network control, the runner applies the full Cycle-429 physical update separately to the four orthogonal operator eigenrays on one common held L6 encoding. These sectorwise scalar physical-network executions verify the implicit common functional lift; they are analysis of one already-constructed operator and are not the update's beta lookup. Orthogonality makes the coherent direct-sum squared residual exactly the amplitude-weighted sum of sector residuals. No enormous register-times-261328 Kronecker array is materialized. This gives basis rays and coherent superpositions exact E/G and inverse, with maximum residual `8.555378627761456e-13`.

The three applications are a declared factor count, not elapsed time. Active recoil is not gravity, force, energy, stress, or a source law selected by Nature.

## Covariance and bounded support

The register carries the scalar proper-cubic action `I_9`. The common 54-dimensional coin, Cycle-311 physical one-particle encoder, and inherited recoil generator pass all 24 proper-cubic frames with maximum covariance residual zero. This covariance does not derive the internal ring orientation.

Observed bounded supports are:

| object | support |
|---|---:|
| register plus M64 rest controller | `53 M2` |
| common M64-register coin control | `53 M2` |
| register-clock-arm control | `10 M2` |
| register-local-recoil control | `34 M2` |
| train clock/receiver installation | `257 M2` |
| held clock/receiver installation | `261 M2` |

The nine-site mass functions, 53-site common coin completion, and 34-site controller-source exponential are supplied bounded dense controls. Primitive synthesis remains open. The support counts are not minimum-content claims.

## Deletions, leakage, and lawful domain

The runner performs independent mass-observable, functional-law, controller-source, clock, and receiver deletions. It also deletes the latch and one register-code amplitude. Results include:

- deleting the mass observable gives zero dark-port and receiver response;
- retaining the observable but deleting functional invocation gives zero dark-port response;
- deleting only controller-source coupling gives zero receiver response while leaving the clock law available;
- deleting clock calibration gives zero dark-port response;
- deleting the distinct receiver vertex gives zero receiver reservoir response;
- deleting the latch gives zero valid-latch weight; and
- deleting one register amplitude gives Gram residual `0.2939723678960654`.

Lawful-domain controls reject an even register, a Cayley-singular `-1` register, nonsquare and nonfinite registers, an invalid lookup length, an invalid source cell, a malformed network state, and actual Q=0/Q=2 register masks. Lawful Q=1 masks are positively accepted.

The canonical Cycle-219 one-particle mass fixture remains `0.4534056541748851` with residual zero. The independent Cycle-230 contact block retains `645` nontrivial columns. Neither is redefined by the new controller.

## Supplied, derived, and open

Supplied:

- the existence and dimension of the nine-M2 register, its one-hot population, internal orientation, and eight-SWAP schedule;
- the Cayley resolvent, principal logarithm, `CLOCK_SCALE=8`, `SOURCE_SCALE=0.05`, signs, zeros, and invocation;
- the Cycle-311 reference/role preparation and dense bounded common-coin completion;
- source reservoir preparation, blank field, receiver matter column, factor order, path, contact, and readouts;
- the oscillator initial word, Ramsey arms, latch trigger, event identity, and blank sidecar.

Derived on the declared finite code:

- the physical nine-M2 Q=1 register and common coherent M64-register controller;
- functional Cayley/principal controls constructed before beta preparation;
- held alias clock and receiver predictions without beta-specific refit;
- the B3/B4 lookup distinction;
- basis/coherent E/G and inverse, scalar-family equality, covariance, support, deletions, leakage, and domain controls.

Open:

- selection or derivation of the register, ring orientation, either coordinate law, both scales, and initial population;
- autonomous creation, selection, change, or combination of beta populations;
- primitive sparse synthesis of the dense bounded matrix functions and common coin;
- autonomous source preparation, common lapse, passive response, physical energy/stress calibration, metric/proper time, and empirical selection;
- gravity, Record formation, occurrence, Born law, and observed spectrum/species interpretation.

Cycle 441 closes beta lookup only conditional on the supplied `S` and selected candidate matrix function. It does not select Cayley over principal and does not derive an observed mass spectrum. Phase is not energy. Update count is not time. A latch is not a Record. Active recoil is not gravity.

No no-go, minimum-content, shared-obstruction, or axiom-pressure claim is made. No axiom, foundation, Qualification, primitive, registry, policy, queue, or audit-status surface is edited.

## Prior-art and novelty boundary

Cayley transforms, principal matrix logarithms, internal mass registers, functional calculus, controlled exponentials, block encodings, one-hot registers, coined walks, and reversible latches are prior-art territory. Mass as an internal quantum-walk degree of freedom is prior work. Cycle 441 claims only this repository-local bounded M2 physicalization, exact functional-versus-table dependency audit, and coherent clock-plus-receiver composition. Global novelty is not asserted.

## Verification

```bash
python3 -m py_compile \
  scripts/coherent_multibeta_physical_mass_controller_tournament_cycle441_2026_07_19.py

python3 -u \
  scripts/coherent_multibeta_physical_mass_controller_tournament_cycle441_2026_07_19.py
```
