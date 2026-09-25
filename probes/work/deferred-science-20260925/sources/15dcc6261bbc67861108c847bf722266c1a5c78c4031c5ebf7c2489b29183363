---
claim_id: ring_model_between_the_rokhsar_kivelson_and_pure_ring_points_small_torus_and_variational_diagnostics_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: spin-1/2 link fields on the cubic lattice in doubled coordinates with the exact vertex Gauss law (three arrows in, three out: cubic ice), the covariant plaquette clause -g (U + U^dag) and the Rokhsar-Kivelson potential V counting flippable plaquettes (open PRs 9066, 9072). Finite diagnostics. (i) The fine Z_4^3 torus has 9600 ice states in 937 flip classes with a largest class of 864 (open PR 9072's counts reproduced), and the global ground state at V = 0 lies in that class. In it, along V/g = 0, 1/4, 1/2, 3/4, 1: ground energy per plaquette -0.3761, -0.2738, -0.1773, -0.0861, 0; gap 2.2258, 1.9417, 1.5934, 1.2758, 0.9696; fidelity with the uniform state 0.807, 0.885, 0.945, 0.984, 1; mean flippable number 10.12, 9.53, 9.01, 8.52, 8.00; total variation of the record measure from uniform 0.345, 0.263, 0.184, 0.099, 0. (ii) On the same class the Jastrow family exp(alpha N_flip) has, at V = 0, its optimum at alpha = 0.14 with energy per plaquette -0.3704 against the exact -0.3761 (relative excess 0.0153) and fidelity 0.9689 with the exact ground state; the uniform state has -0.3333. (iii) Loop-update variational Monte Carlo at V = 0 on the coarse 4^3, 6^3 and 8^3 tori: energy per plaquette at alpha = 0 is -0.2568(5), -0.2589(5), -0.2597(10), equal to minus the flippable density as it must be; the optimum is alpha = 0.2 on 4^3 (-0.2776(4)) and on 6^3 (-0.2796(3)), with -0.2797(3) on 8^3; the flippable density rises from 0.257-0.260 to 0.298-0.299; the connected flippable-plaquette structure factor per plaquette at (pi, pi, pi) is 0.315/0.298, 0.299/0.306, 0.303/0.263 at alpha = 0 / optimum on 4^3, 6^3, 8^3, and on 8^3 at the optimum it is 0, 0.091, 0.200, 0.263 at (0,0,0), (pi,0,0), (pi,pi,0), (pi,pi,pi). No phase of the pure-ring point is claimed; the Rokhsar-Kivelson point's Coulomb-class correlations are those of the uniform ice measure in the landed cubic-ice notes; no physical identification is made."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ring_model_pure_ring_point_small_torus_and_variational_diagnostics_2026_09_24.py
---

# The ring model between the Rokhsar–Kivelson and pure-ring points: small-torus and variational diagnostics

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** finite diagnostics of a supplied model; unaudited.

## Result

Open PR 9072 placed the covariant plaquette clause's Rokhsar–Kivelson point:
at `V = g` the ground states are the uniform superpositions of the flip
classes, so their record law is the uniform ice measure, whose long-wavelength
correlations the landed
`CUBIC_ICE_LONG_WAVELENGTH_STIFFNESS_STAYS_ABOVE_THE_SUM_RULE_FROM_L12_TO_L24_BOUNDED_THEOREM_NOTE_2026-09-24.md`
and its sibling note measure: the Coulomb class. The pure-ring point `V = 0`,
where the soft-Gauss route of open PR 9066 lands, has no such placement, and
the prior art does not settle it for this lattice. This note reports what
finite diagnostics say about the interval between the two points.
- **On the smallest torus the pure-ring ground state is far from uniform.**
  Its fidelity with the uniform state is 0.807, its record measure is 0.345
  in total variation from uniform, and it favours flippable plaquettes
  (10.12 against 8.00). All three move smoothly to the uniform values as
  `V/g → 1`.
- **A one-parameter family captures it.** The Jastrow state `exp(α N_flip)`
  reaches fidelity 0.969 with the exact pure-ring ground state at
  `α = 0.14`, within 1.5% in energy.
- **On larger tori the family's optimum is size-stable and shows no
  ordering signal.** Variational Monte Carlo on the 4³, 6³ and 8³ coarse tori
  puts the optimum at `α = 0.2` with energy per plaquette −0.278, −0.280,
  −0.280, a flippable density of 0.30, and a connected flippable-plaquette
  structure factor at `(π, π, π)` of 0.26–0.31 per plaquette on all three
  sizes, with no growth.

So, as far as a weighted-ice variational family can see, the pure-ring
ground state is a mildly re-weighted ice ensemble rather than a plaquette
crystal. That is a diagnostic, not a phase determination: the family cannot
represent a state outside the ice-measure class, and three sizes do not fix
a limit.

## Setting and decision points

- **D-gauss, D-roles (open PR 9066).** Link qubits at link sites of the
  doubled lattice; the soldered link field `E_l = s_l·e_l`; the exact vertex
  Gauss law, three in and three out.
- **D-ring (open PR 9072).** The covariant plaquette clause `−g (U + U†)`,
  which flips a flippable plaquette.
- **D-RK (open PR 9072).** The potential `V N_flip`, positive on flippable
  plaquettes; `V = g` is the Rokhsar–Kivelson point.
- **The variational family (supplied here).** `ψ(c) ∝ exp(α N_flip(c))` on
  ice states, `α ≥ 0`.

None is adopted.

## Theorem 1 — the smallest torus along `V/g`

The fine `Z_4³` torus (coarse `2×2×2`) has 9600 ice states in 937 flip
classes, the largest of size 864: open PR 9072's counts, reproduced by direct
enumeration. The global ground state at `V = 0` lies in the largest class.
Within it:

| `V/g` | `E₀`/plaquette | gap | fidelity with uniform | `⟨N_flip⟩` | TV from uniform |
|---|---|---|---|---|---|
| 0 | −0.3761 | 2.2258 | 0.807 | 10.12 | 0.345 |
| 1/4 | −0.2738 | 1.9417 | 0.885 | 9.53 | 0.263 |
| 1/2 | −0.1773 | 1.5934 | 0.945 | 9.01 | 0.184 |
| 3/4 | −0.0861 | 1.2758 | 0.984 | 8.52 | 0.099 |
| 1 | 0 | 0.9696 | 1.000 | 8.00 | 0 |

The gap is a two-cell quantity and says nothing about the thermodynamic
limit; the monotone approach of the record measure to the uniform one is the
content. ∎

## Theorem 2 — the Jastrow family on the same class

For `ψ(c) ∝ exp(α N_flip(c))` on the 864 states, at `V = 0` the variational
energy is minimal at `α = 0.14`: −0.3704 per plaquette against the exact
−0.3761 (relative excess 0.0153), and the optimal state has fidelity 0.9689
with the exact ground state. The uniform state (`α = 0`) has −0.3333. ∎

## Diagnostic — loop-update variational Monte Carlo at `V = 0`

Ice configurations on the coarse `L³` torus are sampled with weight
`exp(2α N_flip)` by directed-loop reversals with Metropolis acceptance; the
energy estimator sums, over flippable plaquettes, the amplitude ratio of the
flipped configuration. At `α = 0` the estimator must equal minus the
flippable density, and does: −0.2568(5), −0.2589(5), −0.2597(10) on 4³, 6³,
8³.
- **Energy against `α` on 4³**: −0.2568(5), −0.2719(5), −0.2776(4),
  −0.2768(8), −0.2712(6), −0.2632(22), −0.2363(52), −0.0297(92) at
  `α = 0, 0.1, 0.2, 0.25, 0.3, 0.35, 0.4, 0.6`. Optimum `α = 0.2`.
- **6³**: −0.2589(5), −0.2796(3), −0.2547(18) at `α = 0, 0.2, 0.4`; optimum
  0.2. **8³** at `α = 0.2`: −0.2797(3).
- **Flippable density** at `α = 0` / optimum: 0.257 / 0.298 (4³),
  0.260 / 0.299 (8³).
- **Connected structure factor per plaquette of the flippable indicator**, on
  8³ at the optimum: 0, 0.091, 0.200, 0.263 at `(0,0,0), (π,0,0), (π,π,0),
  (π,π,π)`. At `(π,π,π)`, `α = 0` / optimum by size: 0.315 / 0.298 (4³),
  0.299 / 0.306 (6³), 0.303 / 0.263 (8³).

A Bragg peak would grow with the number of plaquettes; these values do not
grow between 4³ and 8³. Loop acceptance at the optimum is 0.64.

## What this means for the lanes

- **Photon lane.** Between the Rokhsar–Kivelson point and the pure-ring
  point the small-torus ground state moves continuously from the uniform ice
  measure, and on larger tori the best weighted-ice state at `V = 0` is a
  mild re-weighting with no ordering signal at the high-symmetry wavevectors.
  A phase determination needs a method that can leave the ice-measure class
  and control the limit: a sign-free quantum Monte Carlo of the ring model
  (the Hamiltonian is stoquastic in the ice basis), which stays open.
- **Prior art for orientation, not as premise.** The diamond-lattice quantum
  dimer model is ordered at pure kinetic coupling and a U(1) liquid only for
  `V/g ≳ 0.75` (Sikora, Pollmann, Shannon, Penc and Fulde 2011); pyrochlore
  quantum spin ice is a U(1) liquid at pure ring exchange (Shannon, Sikora,
  Pollmann, Penc and Fulde 2012). For the cubic-lattice spin-1/2 ice model at
  `V = 0` this note knows of no prior determination.

## What stays open

- The phase of the pure-ring point, and the extent of the Coulomb phase in
  `V/g`.
- Whether the record measure of the pure-ring ground state, which is
  positive by the stoquastic form, is selected by any positive rule in the
  sense of the landed
  `COULOMB_MEASURE_SELECTION_HARD_STATIC_ICE_RULES_ADMIT_EVERY_ICE_MEASURE_POSITIVE_RULES_SELECT_THE_UNIFORM_ONE_BOUNDED_THEOREM_NOTE_2026-09-22.md`.
- Photon dispersion and its speed at `V = 0`.

## Prior art

Rokhsar and Kivelson 1988; Hermele, Fisher and Balents 2004; Huse, Krauth,
Moessner and Sondhi 2003; Henley 2010; Sikora, Pollmann, Shannon, Penc and
Fulde 2009 and 2011; Shannon, Sikora, Pollmann, Penc and Fulde 2012; Benton,
Sikora and Shannon 2012; Wiese 2013. All cited as prior art, not as premises.

## Checks

The runner has 3 checks and all pass in about 45 seconds, single-threaded.

| Check | Result |
|---|---|
| Fine torus | 9600 / 937 / 864; global `V = 0` ground state in the 864 class; the table above. |
| Jastrow, exact | `α* = 0.14`; −0.3704 vs −0.3761; fidelity 0.9689; uniform −0.3333. |
| Monte Carlo | Energies above; optimum 0.2 on 4³ and 6³; densities 0.257 → 0.298, 0.260 → 0.299; `S(π,π,π)/N_p` 0.26–0.31 on all sizes; acceptance 0.64. |

## Independent check

None yet. The runner was rerun from a clean shell; seeded Monte Carlo
reproduces the cached numbers; no independent checker has reviewed this
block.

**Correction (same day).** The first version's loop sampler counted only
counter-clockwise flippable plaquettes in its acceptance step and kinetic
estimator (`np.abs(c == 4)` where `np.abs(c) == 4` was meant). The `α = 0`
numbers were unaffected; the `α > 0` energies, densities and structure
factors were wrong and are corrected above. The optimum `α = 0.2` and the
absence of growth in `S(π,π,π)` stand. The error was found by comparing this
sampler with a second, independently written one against the exact
all-states average on the fine torus at `α = 0.2` (0.3339; the corrected
sampler gives 0.326, the old one 0.268).

## What this does not do

- It adopts no clause, potential, Gauss law or variational family.
- It claims no phase for the pure-ring point and no thermodynamic limit.
- It measures plaquette order at four wavevectors only, on three sizes.
