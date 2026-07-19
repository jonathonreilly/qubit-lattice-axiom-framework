# Physical mass-clock-to-active-source/receiver tournament — Cycle 438

Date: 2026-07-19
Authority: none
Audit: unset

## Result

Cycle 438 is a positive physical law tournament on one declared bounded physical code.  It composes the same physical M64 rest-sector coordinate used by Cycle 437 with both its Ramsey/clock latch and the Cycle-426/429 recoil-field-distinct-receiver network.  The two candidates are the principal-phase law and the Cayley-unwrapped law.  Three unaliased training sectors agree with no refit; one held alias sector makes different complete clock-word predictions at a distinct physical receiver.

The supplied scalar maps are

```text
chi = M/8
theta_source = 0.05 M.
```

The held principal coordinate is `-1.835710462685637`, whereas the held Cayley coordinate is `17.013845458853122`.  Thus the held source angles are `-0.09178552313428186` and `0.8506922729426561`; these remain different modulo `2 pi`.  The complete clock dark-word weights are `0.013105752602130078` and `0.7638685896374829`.  After three declared network applications, the receiver reservoir weights are `6.114983482422386e-07` and `0.0025367020589446253`.  These are candidate-law code weights, not occurrences or probabilities.

Neither active-source law is selected.  In particular, the executable passes a precomputed beta-specific scalar `theta_source` into a supplied code-restricted gate family.  It does not construct autonomous physical extraction of `M` from the controller, a coherent multi-beta compiler, a generated spectrum, or an autonomous common law.  Sector population, beta-specific gate parameters, both coordinate formulas, both scales, preparation, and factor order remain supplied.

## Exact executable results

| control | final cold maximum or count |
|---|---:|
| final cold summary | `7 pass, 0 fail` |
| maximum train clock/receiver law difference | `9.26442286059391e-23` |
| held clock dark-weight difference | `0.7507628370353528` |
| held distinct-receiver difference | `0.002536090560596383` |
| maximum network forward E/G residual | `3.647211839880937e-14` |
| maximum implicit-tensor forward E/G bound | `3.751311437932894e-14` |
| maximum network physical inverse residual | `4.2254226402175646e-14` |
| maximum implicit-tensor inverse bound | `4.3424906438917493e-14` |
| maximum logical inverse residual | `4.3406350753075e-15` |
| maximum joint norm drift | `1.0473844014313727e-12` |
| maximum network-code leakage | `9.616303857269633e-15` |
| maximum clock-controller leakage | `3.492097889037037e-16` |
| maximum raw Gram residual | `7.771561172376096e-16` |
| `theta+2 pi` source-vertex residual | `14.628397306332463` |
| held-law source-vertex residual | `12.120923779132651` |
| law-swap receiver residual | `0.0` |
| source/receiver path frame failures | `0` |
| maximum all-frame recoil/rest/projector residual | `0.0` |
| Cycle-219 mass-fixture residual | `0.0` |
| contact nontrivial columns | `645` |
| lawful-domain rejections | `7` |

The `7/0` result in the table is from the final cold rerun after all controls
were frozen.

## Declared code and exact map

For each beta fixture separately, the declared code is the factor product

```text
Cycle-437 one-dimensional physical M64 rest-controller sector
tensor
Cycle-429 988 x Q1 physical receiver network
tensor
Cycle-437 complete one-hot oscillator and blank reversible latch.
```

The L4 controller is used for the three training fixtures and the L6 controller for the held fixture.  The receiver network uses held-out sizes L5 and L6 respectively.  This is factorwise/tensor composition on each declared one-dimensional rest-controller sector.  A full Kronecker array is not materialized.

Let `E_c,G_c` denote the Cycle-437 controller/clock encoding and update, and `E_r,G_r` the Cycle-429 receiver encoding and update at the supplied beta-specific angle.  The executable checks factorwise and implicit-tensor exact E/G and inverse:

```text
(E_c G_c) tensor (E_r G_r)
  = (G_c,physical E_c) tensor (G_r,physical E_r),
```

together with adjoint restoration, norm, Gram, and code-leakage controls.  The implicit tensor residual is evaluated by a stable factorwise triangle bound so that subtraction of nearly equal unit norms does not manufacture a false residual.

The 69-M2 coordinate-source control is a supplied gate on the fixed code sector: 44 M2 for the rest-sector projector plus the 25-M2 local recoil vertex.  The 45-M2 clock control is likewise supplied: 44 M2 plus one Ramsey arm.  No primitive sparse synthesis of either bounded control is claimed.  The construction does not test a coherent superposition of beta sectors.

## Candidate table and complete predictions

The common coordinates and source angles are:

| fixture | `M_phase` | `M_C` | principal `theta_source` | Cayley `theta_source` |
|---|---:|---:|---:|---:|
| train 1 | `1.0919107027986072` | `1.091910702798607` | `0.054595535139930366` | `0.05459553513993035` |
| train 2 | `2.51729889353184` | `2.51729889353184` | `0.125864944676592` | `0.125864944676592` |
| train 3 | `5.19615242270663` | `5.19615242270663` | `0.2598076211353315` | `0.2598076211353315` |
| held alias | `-1.835710462685637` | `17.013845458853122` | `-0.09178552313428186` | `0.8506922729426561` |

Starting at complete oscillator word 2, one clock update leaves coherent support on bright word 3 and dark word 4.  The complete clock-word and receiver predictions are:

| fixture | law | clock word-3 weight | clock word-4 weight | receiver weight after three applications |
|---|---|---:|---:|---:|
| train 1 | principal | `0.995349924947346` | `0.004650075052655334` | `7.688807414145487e-08` |
| train 1 | Cayley | `0.995349924947346` | `0.004650075052655334` | `7.688807414145478e-08` |
| train 2 | principal | `0.9754504653130751` | `0.02454953468692667` | `2.149246178285634e-06` |
| train 2 | Cayley | `0.9754504653130751` | `0.02454953468692667` | `2.149246178285634e-06` |
| train 3 | principal | `0.8981873845754096` | `0.10181261542459161` | `3.740860270404842e-05` |
| train 3 | Cayley | `0.8981873845754096` | `0.10181261542459161` | `3.740860270404842e-05` |
| held alias | principal | `0.9868942473978712` | `0.013105752602130078` | `6.114983482422386e-07` |
| held alias | Cayley | `0.23613141036251836` | `0.7638685896374829` | `0.0025367020589446253` |

The maximum train clock-or-receiver law difference is `9.26442286059391e-23`.  The held dark-word difference is `0.7507628370353528`, and the held receiver difference is `0.002536090560596383`.

## Source depletion, field gain, and receiver ledger

The fixed hard-core recoil vertex transfers reservoir occupation into the physically distinct field track while applying the Cycle-426 direction ledger.  For each row the runner checks source depletion and field gain, source direction change plus twice the field direction change, the corresponding receiver ledger, and network norm.

The held principal source depletion/field gain is `0.008400950953324715 / 0.00840095095332738`; the held Cayley value is `0.5651086878972271 / 0.565108687897228`.  Maximum ledger residuals are numerical roundoff.  The receiver is a distinct physical M64 cell reached only through both transport factors and its local recoil vertex.  Source-angle, receiver, transport, calibration, oscillator, and latch deletions are all explicit.

The three applications are a declared factor count, not elapsed time.  The factor order, initial reservoir, blank field, matter column, path, contact, and readout are supplied.  A gate angle, eigenphase, occupation, circuit layer, and update count are not energy, stress, rate, time, force, or gravity.  A latched word is not a Record.

## Covariance, support, and preserved fixtures

The rest ray, rest projector, fixed recoil generator, and source/receiver path are audited in all 24 proper-cubic frames.  The source and receiver geometry rotates with the frame; there is no preferred cubic direction in the declared family.  The L4/L6 role-gauge constraints remain locally enforced by the inherited physical M64 code.

The separate Cycle-219 one-particle mass fixture `0.4534056541748851` is preserved, as is the Cycle-230/319 contact block with `645` nontrivial columns.  The contact remains a separate factor; the candidate source law does not redefine it.

The training controller/clock plus receiver patch count is `106+142=248 M2`; the held count is `106+146=252 M2`.  The local recoil vertex uses 25 M2 and the latch primitives at most 3 M2.  These are bounded observed supports, not minimum-content claims.

## Alias, deletion, leakage, and lawful-domain controls

The periodic-angle alias audit checks the local source vertex at `theta` and `theta+2 pi`, while also checking that the two held source vertices are genuinely distinct.  Its `theta+2 pi` vertex residual is `14.628397306332463`: the recoil-vertex parameter is not a wrapped U(1) phase and must not be silently reduced modulo `2 pi`.  The held principal/Cayley vertex residual is `12.120923779132651`.  Swapping the principal and Cayley coordinate lookup swaps both held receiver predictions without refitting.

The deletion suite removes the source angle, receiver vertex, either transport edge, contact factor, preparation, clock calibration, oscillator, latch, and one dominant rest-projector component.  It also tests a blank network input.  The expected receiver or clock response disappears or changes, and deleting the projector component breaks both Gram normalization and the local role constraint.

Leakage and lawful-domain controls cover the controller rest code, complete clock/latch code, receiver-network encoding, adjoint restoration, malformed angles, invalid source cells, unknown laws, unsupported calibration counts, malformed physical sites/states, and invalid clock words.

## Typed dependency boundary

Cycle-204 common-lapse and passive-trajectory flags remain false.  The bounded candidate is an active-source/recoil response law only after the stated supplied preparation and beta-specific parameter are installed.  It does not yield a common lapse, passive response, end-to-end `a/g`, metric, proper time, or gravity law.

Cycle-420 named prediction flags remain false: there is no autonomous physical source E/G extracted from controller occupation, host profile join, host packet/centroid join, or named prediction closure.  The Cycle-429 physical test-matter readout is reused, but this tournament does not close the larger host/source dependency chain.

Supplied structure:

- principal/Cayley formulas, beta-sector populations, and beta-specific gate parameters;
- `chi=M/8` and `theta_source=0.05 M`, including signs, zeros, and invocation;
- the 45-M2 clock control and 69-M2 coordinate-source control;
- source preparation, matter column, blank field, factor order, path, contact, and readouts;
- clock initial word, Ramsey arms, latch trigger, event identity, and blank sidecar.

Derived on each declared sector:

- the common-coordinate clock plus recoil/receiver factor composition;
- train agreement and held alias disagreement in both complete readouts;
- source depletion and field gain, plus source/receiver direction ledgers;
- exact E/G and inverse, all-frame covariance, bounded support, deletions, leakage, and domain controls.

Open:

- selection or derivation of either coordinate law and both conversion scales;
- autonomous physical extraction of `M`, coherent cross-sector population, and primitive projector-control synthesis;
- autonomous source preparation, recurrence, physical energy/stress/source calibration, and passive response;
- common lapse, metric/proper time, Record formation, occurrence, Born law, and empirical selection.

This is a bounded positive construction, not constitutional evidence.  No no-go, minimum-content, shared-obstruction, or axiom-pressure claim is made.  No axiom, foundation, Qualification, primitive, registry, policy, queue, or audit-status surface is edited.

## Prior-art and novelty boundary

Controlled rotations, Ramsey interferometry, Cayley transforms, coined walks, hard-core source vertices, local recoil ledgers, tensor-product encodings, and reversible latches are prior-art territory.  Cycle 438 claims only this repository-local bounded composition and the exact no-refit held-alias discriminator across both its complete clock latch and physically distinct receiver.  Global novelty is not asserted.

## Verification

```bash
python3 -m py_compile \
  scripts/physical_mass_clock_active_source_receiver_tournament_cycle438_2026_07_19.py

python3 -u \
  scripts/physical_mass_clock_active_source_receiver_tournament_cycle438_2026_07_19.py
```
