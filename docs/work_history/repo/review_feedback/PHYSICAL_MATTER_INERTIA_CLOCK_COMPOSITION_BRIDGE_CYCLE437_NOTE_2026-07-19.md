# Physical matter/inertia-to-clock composition bridge — Cycle 437

Date: 2026-07-19
Authority: none
Audit: unset

## Result

Cycle 437 is a positive bounded physical composition of the Cycle-311 physical M64 one-particle rest ray and Cycle-219 free coin with the Cycle-428 sixteen-M2 one-hot oscillator and its reversible physical latch. The declared code retains the locally enforced role-gauge constraint of the physical M64 compiler. The oscillator, Ramsey pair, calibration control, bus, and latch are literal M2 degrees of freedom.

Two mass-phase-to-clock laws are compiled on the same physical code and no refit is made:

- the principal-phase calibration uses `M_phase = 3 Arg(lambda_rest)`;
- the Cayley-unwrapped calibration uses `M_C = -3 tan(beta/2)`.

The common supplied conversion is `chi=M_coordinate/8`. Three unaliased training sectors give `M_phase=M_C`, so the two laws make the same complete clock/latch prediction. On the held alias sector `beta=-8 pi/9`, the physical rest eigenvalue has the principal coordinate `-1.8357104626856369` while the Cayley coordinate is `17.013845458853122`. The two laws then predict sharply different coherent weights on the same pair of complete latched clock words.

Neither law is selected. The sector population, coordinate formula, conversion scale, calibration application, and latch trigger are supplied candidate-law content. There is no proper time or inertia-law selection.

## Exact executable results

| control | cold maximum or count |
|---|---:|
| final cold summary | `7 pass, 0 fail` |
| canonical mass-code residual | `2.7668703491380404e-16` |
| rest-ray Gram residual | `2.220446049250313e-16` |
| forward `E G = G_physical E` | `1.0409959805196598e-15` |
| logical inverse | `1.998532698689832e-15` |
| physical inverse | `1.2324694507930868e-15` |
| output norm drift | `1.7763568394002505e-15` |
| matter-code leakage | `3.690030447952667e-16` |
| clock-Hamming failures | `0` |
| latch-decode failures | `0` |
| blank-bus failures | `0` |
| all-24 rest-ray covariance | `0.0` |
| all-24 rest-projector covariance | `0.0` |
| all-24 free-coin covariance | `1.922215274510871e-15` |
| frame branch failures | `0` |
| clock/latch layout failures | `0` |
| lawful-domain rejections | `6` |
| physical M64 patch union | `44 M2` |
| Cycle-428 oscillator/latch inventory | `62 M2` |
| combined bounded installation | `106 M2` |
| compiled mass-clock control support | `45 M2` |
| oscillator/Ramsey primitive support | `2 M2` |
| latch primitive support | `3 M2` |

The residual maxima range over all sixteen input clock words, both laws, one and two applications, three training sectors, and the held alias sector unless a row names a narrower control. The `7/0` summary is reported by the final cold rerun.

## Reconnaissance and exact target

Cycle 204 makes the clock map load-bearing through the conditional surface

```text
a/g = M_passive / M_inertial.
```

It also shows why a principal phase and a nonlinear `tan` coordinate cannot be treated as mere notation: they can change finite response and composition. Cycle 219 supplies the six-direction cubic free coin and its rest/curvature/inertial mass family, while leaving the beta spectrum and clock reading open. Cycle 221 gives the exact alias warning: three positive sectors are unaliased, but its fourth positive sector has Cayley mass `17.013845458853126` and principal-phase mass `-1.83571046`; its additive mass rule is supplied rather than derived.

Cycles 319 and 396 show that the Cycle-219 `0.4534056541748851` one-particle mass fixture survives the physical M2 compiler, including held size. Cycle 426 preserves that mass fixture on the recoil/field code but does not calibrate it as time, energy, source, or gravity. Cycle 428 supplies the physical oscillator and reversible full-word latch. Cycle 431 demonstrates that distinct local physical response laws can give different complete clock words without either law being selected.

Cycle 437 targets only the physical mass-to-clock calibration seam. The exact Cycle-204 common-lapse, source, and trajectory flags remain false.

## Declared physical code

The matter factor begins with the Cycle-311 rank-64 physical M64 input code. Cycle 437 restricts its logical matter input to the uniform one-particle rest ray

```text
|rest> = (1/sqrt(6)) sum_d |n=1,d>.
```

Its physical representation lies in the 510-dimensional relational-role microsector shell and obeys

```text
C_role |rest_physical> = |rest_physical>,
C_role = K_exchange X_r.
```

The clock/latch factor is

```text
complete Q_clock=1 sector of sixteen oscillator M2
tensor
blank 21-M2 latch bus
tensor
blank 21-M2 latched-word/event/valid sidecar.
```

The logical code therefore has all sixteen one-hot clock columns for one fixed normalized physical rest ray and blank latch. The event identity is the supplied nonzero four-M2 word `7`; the latch control is a supplied calibration-event bit, not a matter source, detector occurrence, or Record.

Training uses the first three positive nine-cycle beta values

```text
-2 pi/9, -4 pi/9, -2 pi/3
```

on the physical L4 compiler. The held alias sector uses `-8 pi/9` on physical L6. The canonical Cycle-219 `beta=-0.3` mass fixture is separately preserved on both L4 and held L6.

## Fixed physical sequence

For either candidate law, one forward map is:

1. apply the actual physical Cycle-219 free coin to the physical M64 rest ray;
2. apply one Cycle-428 nearest-neighbor oscillator SWAP sweep;
3. apply a two-M2 number-preserving Ramsey beamsplitter on adjacent complete-word positions 3 and 4;
4. on the position-4 arm, apply the bounded physical rest-projector calibration with phase `exp(i chi)`;
5. apply the same Ramsey beamsplitter again;
6. reversibly latch the complete oscillator word and event identity.

The inverse reverses the latch, Ramsey pair, calibration, oscillator sweep, and matter coin. The executable checks exact E/G and inverse on every one-hot clock input for both laws, one and two calibration applications, all training sectors, and the held alias sector.

The oscillator sweep is distinct from the supplied chi calibration. The sweep advances the one-hot word by a fixed nearest-neighbor permutation. `chi` is the coefficient of a separate bounded interferometric gate. Neither the sweep nor `chi` supplies a clock unit.

## Candidate laws and complete-word predictions

The calibration table is explicit supplied content:

| fixture | beta | `M_phase` | `M_C` |
|---|---:|---:|---:|
| train 1 | `-2 pi/9` | `1.091910702798607` | `1.091910702798607` |
| train 2 | `-4 pi/9` | `2.5172988935318394` | `2.51729889353184` |
| train 3 | `-2 pi/3` | `5.19615242270663` | `5.19615242270663` |
| held alias | `-8 pi/9` | `-1.8357104626856369` | `17.013845458853122` |

Starting at oscillator position 2, the common oscillator sweep and Ramsey pair leave support only on complete words 3 and 4. For a calibration angle `chi`, the coherent word weights are

```text
w_3 = cos(chi/2)^2,
w_4 = sin(chi/2)^2.
```

These squared amplitudes are coherent code diagnostics, not occurrences, probabilities, or a Born law.

The one- and two-application predictions are:

| fixture | applications | principal word-4 weight | Cayley word-4 weight |
|---|---:|---:|---:|
| train 1 | 1 | `0.004650075052655326` | `0.004650075052655326` |
| train 1 | 2 | `0.01851380741864` | `0.01851380741864` |
| train 2 | 1 | `0.024549534686926625` | `0.024549534686926635` |
| train 2 | 2 | `0.09578742013432803` | `0.09578742013432806` |
| train 3 | 1 | `0.10181261542459147` | `0.10181261542459147` |
| train 3 | 2 | `0.36578722705998284` | `0.36578722705998284` |
| held alias | 1 | `0.013105752602130063` | `0.7638685896374819` |
| held alias | 2 | `0.05173596740344728` | `0.7214934696109045` |

The two-application row composes two identical fixed calibration factors before Ramsey recombination. It makes additive principal-phase versus additive Cayley-coordinate behavior operational on the clock/latch output. It is not a derived multiparticle composition law: the choice to add either supplied coordinate, the number of applications, and the common conversion scale remain inputs.

## Bounded support and geometry

For the selected M64 cell, the actual union of physical face, port, flag, and role-companion support is 44 M2; the largest individual representative has support 32 M2. The Cycle-428 active oscillator/latch inventory is 62 M2. The disjoint bounded installation therefore uses 106 M2.

The compiled matter-clock calibration has support on the 44-M2 matter patch plus one clock-arm M2, at most 45 M2. The oscillator sweep and Ramsey gates each use two adjacent M2. Each latch primitive uses at most three M2 with diameter at most two in the inherited `22 x 3 x 1` latch box. A designated matter boundary interface at `(4,1,1)` is adjacent to the word-4 oscillator M2 at `(4,1,0)`.

The 45-M2 rest-projector calibration is one supplied bounded control. It has no primitive sparse synthesis here. The all-frame check proves covariance and bounded patch support, not a nearest-neighbor primitive circuit for that 45-site operator. The result does not relabel a dense bounded compiler as a derived one- or two-M2 fundamental gate. The counts are observed support bounds, not minimum-content claims.

The runner rotates the M64 rest ray, its projector, free coin, oscillator sweep, Ramsey pair, matter-clock interface, and full latch schedule through all 24 proper-cubic frames. The scalar rest ray and projector are invariant, and every rotated clock/latch primitive retains its support and adjacency. The role-gauge constraint remains local.

## Deletions, leakage, and lawful domain

These are leakage and lawful-domain controls on the declared code.

The runner performs matter, calibration, oscillator, Ramsey, and latch deletions. It also deletes the word-4 latch-copy gate and one active physical encoding amplitude. The controls distinguish:

- free-coin deletion from the represented coherent vector (a global-phase-sensitive operator control, not by itself an operational clock readout);
- calibration deletion, which returns zero word-4 dark-port weight;
- oscillator deletion, which leaves support on the wrong complete words;
- either Ramsey deletion, which gives an unrecombined half-weight arm;
- latch deletion, which leaves zero valid-latch weight;
- word-4 copy deletion, which invalidates that branch’s decoded latch; and
- physical encoding-amplitude deletion, which breaks both Gram normalization and the role constraint.

Output matter leakage from the one-particle rest code, clock-Hamming leakage, latch-bus residue, and inverse residual are checked on the whole declared code. Lawful-domain controls reject L3, an unknown law, three calibration applications, a malformed clock word, zero event identity, and a nonblank input latch.

## Cycle-204 comparator boundary

If one additionally supplies the Cycle-204 conditional identification that the chosen clock coordinate is `M_passive`, and assumes the Cayley coordinate as candidate `M_inertial`, then the comparator is

```text
a/g = M_passive / M_inertial.
```

On all three unaliased training sectors, both candidate ratios equal one to numerical precision. On the held alias sector:

```text
principal candidate: -0.10789509444676591,
Cayley candidate:     1.
```

The held aliased-sector `M_inertial=M_C` entry is an assumed candidate coordinate. It is not an independently measured inertial mass for that sector. Accordingly the Cayley `a/g=1` entry is a conditional comparator only. This is a falsifiable far-side discriminator, not an evolved acceleration. No common lapse is applied, no force or passive trajectory is evolved, and no active source map is installed. Therefore Cycle 204 is not closed end to end.

The runner keeps these flags explicit:

- Cycle-204 physical clock calibration candidates: true;
- Cycle-204 common lapse: false;
- Cycle-204 active source map: false;
- Cycle-204 passive force or trajectory: false;
- Cycle-204 end-to-end `a/g` prediction: false;
- proper time: false;
- inertia law selected: false.

Common-lapse, source, and trajectory flags remain false.

## Supplied, derived, and open

Supplied:

- the three unaliased beta populations and held alias beta population;
- principal and Cayley coordinate formulas, `CLOCK_SCALE=8`, and one/two applications;
- Ramsey arms, oscillator initial word, factor order, and nonwrapping readout domain;
- the Cycle-311 reference/role preparation and bounded matrix-unit completion;
- the latch trigger, event identity, blank bus, blank sidecar, and their placement;
- the conditional Cycle-204 identification of a selected clock coordinate with passive mass.

Derived on the declared code:

- preservation of the physical M64 rest ray, free coin, canonical mass fixture, and role gauge;
- exact physical E/G and inverse over the complete sixteen-word clock code;
- same predictions for three unaliased train sectors and distinct held alias predictions;
- exact one- and two-application complete clock/latch weights;
- bounded support, all-frame covariance, deletion sensitivity, leakage closure, and lawful-domain rejection.

Open:

- selection of either calibration and derivation of the conversion scale;
- a physical sector-population law and a multiparticle additive or deformed-composition law;
- a common lapse, active source law, passive force/trajectory, and full Cycle-204 response;
- an operational clock unit, metric or proper time, autonomous recurrence, Record formation, occurrence, Born law, and empirical selection;
- primitive sparse synthesis of the bounded 45-M2 calibration projector.

Eigenphase, generator, circuit layer, and update count are not time, rate, duration, or energy. Wrapped phase is not called physical energy. The reversible latch is not a Record. Pointer copying is not Record formation.

No no-go, minimum-content, shared-obstruction, or axiom-pressure claim is made. No axiom, foundation, Qualification, primitive, registry, policy, queue, or audit-status surface is edited. Authority remains none and audit remains unset.

## Prior-art and novelty boundary

Ramsey interferometry, phase kickback, Cayley transforms, one-hot clock registers, reversible fanout/latching, coined walks, and mass-as-an-internal-degree-of-freedom constructions are prior-art territory. Cycle 437 claims only the bounded repository-local composition of this physical M64 rest compiler with this physical oscillator/latch and the exact alias-sector discriminator between these two supplied calibration laws. Global novelty is not asserted.

## Verification

```bash
python3 -m py_compile \
  scripts/physical_matter_inertia_clock_composition_bridge_cycle437_2026_07_19.py

python3 -u \
  scripts/physical_matter_inertia_clock_composition_bridge_cycle437_2026_07_19.py
```
