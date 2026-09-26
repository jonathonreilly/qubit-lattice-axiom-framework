---
claim_id: ring_model_with_single_link_charge_hopping_changes_rapidly_between_weak_and_strong_hopping_and_its_moment_bound_stays_finite_at_small_momentum_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Supplied link-qubit model on L^3 tori with the ring clause -g (U + U^dag) at V = 0, g = 1, a single-link term -t sigma^x on every link and a charge mass M Q_v^2, Q_v = div_v / 2 (the single-link term and charge mass are a new supplied clause, not adopted). Exact: the model is sign-free in the sigma^z basis; Hellmann-Feynman gives <sigma^x> and <Q^2> from energy differences in t and M; degree-one homogeneity of E0 in (g, t, M) gives the ring expectation u; the triple-averaged f-sum gains 2 t <sigma^x>, so the moment-chain bound on the lowest transverse excitation, 2 ((u s^2 + t <sigma^x>) / chi)^(1/2), keeps the momentum-independent part 2 (t <sigma^x> / chi)^(1/2) as k -> 0. Finite projector estimates at M = 2 (fixed populations of 1920 walkers, projection 30, three or four seeds; errors heuristic): the exact 2^3 control agrees within 1.8 standard errors and the t = 0 limit agrees with the ring-model projector on 4^3; <sigma^x> and <Q^2> rise fastest between t = 0.25 and 0.5 (6^3: <sigma^x> 0.102, 0.456, 0.667, 0.759 at t = 0.25, 0.5, 0.75, 1), the size dependence of <sigma^x> at t = 0.5 (0.438, 0.456, 0.470 on 4^3, 6^3, 8^3) lies within the guide dependence that open PR 9268 measured at these populations (link expectations up to 0.08 apart on 6^3 between two charge penalties at t = 0.30-0.50) and is not established; on 6^3 chi at the smallest momentum is 1.044, 1.080, 1.043 at t = 0, 0.25, 0.5 and 0.908, 0.796 at t = 0.75, 1, u falls from 0.290 to 0.233 and alpha_G = (1/(chi u))^(1/2) / (2 pi) rises from 0.289 to 0.370; on 8^3 chi is 1.071 and 0.995 +- 0.042 at t = 0 and 0.5. No limit, phase, transition, mass, coupling of a physical field or comparison value is claimed."
upstream_dependencies:
  - minimal_axioms
  - gaussian_lattice_maxwell_comparator_gives_a_linear_size_independent_transverse_structure_factor_and_misses_the_pure_ring_level_step_bounded_theorem_note_2026-09-24
runner: scripts/ring_model_dynamical_charges_on_the_pure_ring_photon_from_energies_2026_09_25.py
---

# Ring model with single-link charge hopping: a rapid change between weak and strong hopping, and a moment bound that stays finite at small momentum

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** exact identities of the supplied model, with finite projector estimates; unaudited.

## Result

Open PR 9236 bounded the pure-ring photon with ground-state energies alone,
and open PR 9244 placed static test charges in it. Here the charges move: a
single-link term flips one link and so creates, moves or removes a pair of
unit charges, and a charge mass `M Q²` prices them. The same energy-only
tools apply, and one of them changes character.

- **The moment bound keeps a constant part.** With the single-link term the
  averaged f-sum of the transverse triple is `2 u s² + 2 t ⟨σ^x⟩`, so the
  moment chain bounds the lowest transverse excitation by
  `2 ((u s² + t ⟨σ^x⟩) / χ̄)^{1/2}`. The added part does not vanish as
  `k → 0`: the energy-only argument that forced a linear bound at `t = 0` no
  longer does, and at small momentum it bounds the excitation by
  `2 (t ⟨σ^x⟩ / χ̄)^{1/2}` instead. The bound neither shows nor excludes a gap.
- **A rapid change between weak and strong hopping.** At `M = 2` the link
  expectation `⟨σ^x⟩` and the charge density `⟨Q²⟩` rise fastest between
  `t = 0.25` and `t = 0.5` (on 6³, `⟨σ^x⟩` gains 0.35 there against 0.10
  and 0.21 in the neighbouring steps). The printed values at `t = 0.5`
  move with size (0.438, 0.456, 0.470 on 4³, 6³, 8³), but open PR 9268
  later measured link expectations in this window that differ by up to
  0.08 on 6³ between two guide penalties at these populations, so neither
  that size dependence nor where the rise is steepest is established here.
- **Weak hopping leaves the transverse response; strong hopping moves it.**
  On 6³ the susceptibility at the smallest momentum is `1.044`, `1.080`,
  `1.043` at `t = 0`, `0.25`, `0.5` (within errors) and `0.908`, `0.796` at
  `t = 0.75`, `1`. The ring expectation falls from `0.290` to `0.233`, and the
  comparator's combination `α_G = (1/(χ̄ u))^{1/2} / (2π)` rises from
  `0.289` to `0.370`. On 8³, `χ̄` is `1.071 ± 0.011` at `t = 0` and
  `0.995 ± 0.042` at `t = 0.5`.

Supplied model, finite estimates on three small tori and five hopping
values: the rapid change is located, not classified as a crossover or a
transition, and `α_G` is a number of the comparator, not a coupling of any
physical field.

## Setting and decision points

- **D-gauss, D-ring (landed).** Spin-1/2 link fields `σ = ±1` on the cubic
  `L³` torus and the clause `−g Σ_p (U_p + U_p†)` at `V = 0`, `g = 1`.
- **D-hop (supplied here).** A single-link term `−t Σ_l σ^x_l`, the same on
  every link, and a charge mass `M Σ_v Q_v²`, with `Q_v = div_v / 2` the
  vertex charge (`div_v` the number of arrows out minus in). At `t = 0` the
  ice configurations, where every `Q_v = 0`, are decoupled from the rest and
  the model is the landed ring clause with the exact Gauss law. For `t > 0`
  one link flip creates, moves or removes a pair of unit charges. The term
  is covariant and acts on one link; it is a new clause of the supplied
  model, recorded as a decision point, not adopted.
- **The Gaussian comparator (landed).** The lattice Maxwell comparator of
  `GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24.md`
  with the matching rule `K = 4u` of that note, used for the combination
  `α_G = (U/u)^{1/2} / (2π)` with `U = 1/χ̄` (open PR 9258). The comparator
  has no charge sector; with moving charges `α_G` is only this combination.
- **The projector (method).** The compiled projector of open PR 9236,
  extended with link events: every off-diagonal element is `−g` or `−t`, so
  the walk stays sign-free. Guide
  `exp(0.2 N_flip − γ Σ_v Q_v² + Σ_l b_l σ_l)`. The charge penalty `γ` was
  tuned on 4³ at each `t` for the smallest energy variance, in calibration
  runs outside the runner (`γ = 1.2, 0.7, 0.5, 0.3` at `t = 0.25, 0.5, 0.75, 1`);
  the first-order guess `½ ln(2M/t)` gave a larger variance and a visible
  population bias there. The mixed energy estimator is exact for any guide;
  the fixed-population bias depends on it. Fixed populations of 1920
  walkers, time step 0.05, projection 30 per run, four seeds (three on 8³);
  errors are the larger of the seed scatter and the mean bin error, a
  heuristic.

None is adopted.

## Theorem 1 — what energies alone give

1. **Sign-free.** In the `σ^z` basis every off-diagonal element of the
   Hamiltonian is `−g` (a flippable plaquette) or `−t` (a link), so the
   ground state has non-negative amplitudes and the projector's weights are
   positive. The mixed energy estimator is exact for any guide.
2. **Hellmann–Feynman.** `∂E_0/∂t = −Σ_l ⟨σ^x_l⟩` and
   `∂E_0/∂M = Σ_v ⟨Q_v²⟩`, so the link expectation and the charge density
   follow from energy differences.
3. **Homogeneity.** At `V = 0`, `E_0(λg, λt, λM) = λ E_0(g, t, M)`, so
   `g ∂_g E_0 + t ∂_t E_0 + M ∂_M E_0 = E_0`, and the ring expectation per
   plaquette is `u = (−E_0 − t ⟨σ^x⟩ N_l + M ⟨Q²⟩ N_v) / (g N_p)`.
4. **The f-sum with charges.** For the cyclic triple of transverse modes of
   open PR 9236, the averaged first moment gains a term from the single-link
   flips, `f̄ = 2 u s² + 2 t ⟨σ^x⟩`, since `[σ^z, [−t σ^x, σ^z]] = 4t σ^x`
   link by link, and the charge mass commutes with `σ^z`; the ring part
   `2 u s²` holds in any state, as in open PR 9236. The moment chain of open
   PR 9236 then bounds the lowest transverse excitation by
   `2 ((u s² + t ⟨σ^x⟩) / χ̄)^{1/2}`. The added term does not vanish as
   `k → 0`, so the bound stays finite there.

The runner checks the homogeneity identity and the projector's energies with
and without a probe field against exact diagonalization on the `2³` torus. ∎

## Diagnostic 1 — exact control on 2³

With the single-link term on all 24 links the `2³` space has `2^24`
configurations, so the control puts the term on the six links at one vertex. Plaquette
flips and flips of those six links reach 184320 configurations from the ice
seed, and the ground state of that space is found exactly with and without
the probe field `h = 0.15` of the transverse triple.

| `(t, M)` | exact `E_0` | projector | exact `E(h)` | projector | `Σ ⟨σ^x⟩` (six links) | `Σ ⟨Q²⟩` | homogeneity residual |
|---|---|---|---|---|---|---|---|
| (0.8, 1.5) | −9.955241 | −9.94032 ± 0.00830 (+1.8 σ) | −10.161516 | −10.15202 ± 0.00764 (+1.2 σ) | 2.40178 | 0.43179 | 5.5 × 10⁻¹⁴ |
| (1.5, 2.0) | −11.808063 | −11.81068 ± 0.01352 (−0.2 σ) | −12.031475 | −12.02009 ± 0.01019 (+1.1 σ) | 3.77285 | 0.94845 | 3.4 × 10⁻¹⁴ |

With the single-link term switched off, the new projector gives
`−0.29322 ± 0.00003` per plaquette on 4³ against the ring-model projector's
`−0.29315 ± 0.00008` (−0.8 σ), and the Hellmann–Feynman charge density in
`M` is `−0.0004 ± 0.0019` per site.

## Diagnostic 2 — the scan in the hopping at `M = 2`

Per plaquette `e_0`, per link `⟨σ^x⟩`, per site `⟨Q²⟩` (both
Hellmann–Feynman, differences `±0.1` in `t` and `M`), `u` from homogeneity,
`χ̄` at the smallest momentum `k = 2π/L`. Errors of `u` and `α_G` are
propagated from the printed errors of `⟨σ^x⟩`, `⟨Q²⟩` and `χ̄`.

| torus | `t` | `e_0` | `⟨σ^x⟩` | `⟨Q²⟩` | `u` | `χ̄` | `α_G` |
|---|---|---|---|---|---|---|---|
| 4³ | 0 | −0.29322 | 0 | −0.0004(19) | 0.2930(13) | 0.806(10) | 0.3275(22) |
| 4³ | 0.25 | −0.30585 | 0.1065(10) | 0.0152(14) | 0.2893(10) | 0.873(23) | 0.3166(42) |
| 4³ | 0.5 | −0.36116 | 0.4378(28) | 0.1972(17) | 0.2737(18) | 1.106(22) | 0.2892(30) |
| 4³ | 0.75 | −0.50730 | 0.6681(6) | 0.3603(15) | 0.2464(11) | 0.920(18) | 0.3342(34) |
| 4³ | 1 | −0.68735 | 0.7591(2) | 0.4569(5) | 0.2328(4) | 0.810(11) | 0.3664(25) |
| 6³ | 0 | −0.28934 | 0 | 0.0014(18) | 0.2903(12) | 1.044(10) | 0.2891(15) |
| 6³ | 0.25 | −0.30186 | 0.1016(20) | 0.0147(14) | 0.2863(11) | 1.080(35) | 0.2862(47) |
| 6³ | 0.5 | −0.36024 | 0.4562(15) | 0.2021(21) | 0.2669(16) | 1.043(27) | 0.3017(40) |
| 6³ | 0.75 | −0.50691 | 0.6668(11) | 0.3593(14) | 0.2464(12) | 0.908(18) | 0.3365(34) |
| 6³ | 1 | −0.68711 | 0.7593(2) | 0.4577(7) | 0.2329(5) | 0.796(8) | 0.3695(19) |
| 8³ | 0 | −0.28868 | 0 | 0.0000(9) | 0.2887(6) | 1.071(11) | 0.2862(15) |
| 8³ | 0.5 | −0.35954 | 0.4703(12) | 0.2062(28) | 0.2618(20) | 0.995(42) | 0.3119(67) |

- **Where the ground state changes fastest.** On 6³ the steps of
  `⟨σ^x⟩` between successive `t` are 0.10, 0.35, 0.21, 0.09, and of `⟨Q²⟩`
  0.013, 0.187, 0.157, 0.098; 4³ shows the same pattern. At weak hopping
  the link expectation sits near the second-order estimate with the bare
  pair cost `2M`, `⟨σ^x⟩ ≈ t/M` (0.125 at `t = 0.25`, measured 0.10–0.11);
  at `t = 0.5` the measured 0.44–0.47 is nearly twice that estimate (0.25).
- **Size dependence (not established).** `⟨σ^x⟩` changes between 4³ and
  6³ by `−2.2 σ` at `t = 0.25`, `+5.8 σ` at `0.5`, `−1.0 σ` at `0.75` and
  `+0.7 σ` at `1`; from 6³ to 8³ at `t = 0.5` it changes by `+7.3 σ`. These
  are statistical errors only; the guide dependence measured in open PR 9268
  is larger on 6³ in the window `t = 0.30–0.50`.
- **The transverse response.** On 6³, `χ̄` is flat within errors up to
  `t = 0.5` and falls by 13 and 24 per cent at `t = 0.75` and `1`. On 4³,
  where the smallest momentum is `π/2`, `χ̄` is not monotone in `t`, with
  its largest value at `t = 0.5`; this is not interpreted. On 8³, `χ̄` at
  `t = 0.5` lies 1.8 standard errors below `t = 0`.
- **For comparison.** At `t = 0` the new kernel's `χ̄` agrees with open PR
  9258's re-measurement on 6³ and 8³ (1.060 ± 0.013, 1.072 ± 0.014) within
  one standard error and lies 2.3 standard errors below it on 4³
  (0.868 ± 0.025).

## Diagnostic 3 — the moment bound

The bound `2 ((u s² + t ⟨σ^x⟩) / χ̄)^{1/2}` on the lowest transverse excitation
at `k = 2π/L`, with `s² = 2 − 2 cos k`, split into its ring part
`2 (u s² / χ̄)^{1/2}` and its momentum-independent part `2 (t ⟨σ^x⟩ / χ̄)^{1/2}`
(the two add in quadrature).

| torus | `t` | ring part | momentum-independent part | bound |
|---|---|---|---|---|
| 4³ | 0 | 1.705 | 0 | 1.705 |
| 4³ | 0.25 | 1.628 | 0.349 | 1.665 |
| 4³ | 0.5 | 1.407 | 0.890 | 1.665 |
| 4³ | 0.75 | 1.464 | 1.476 | 2.078 |
| 4³ | 1 | 1.516 | 1.936 | 2.459 |
| 6³ | 0 | 1.055 | 0 | 1.055 |
| 6³ | 0.25 | 1.030 | 0.307 | 1.074 |
| 6³ | 0.5 | 1.012 | 0.935 | 1.378 |
| 6³ | 0.75 | 1.042 | 1.484 | 1.813 |
| 6³ | 1 | 1.082 | 1.953 | 2.233 |
| 8³ | 0 | 0.795 | 0 | 0.795 |
| 8³ | 0.5 | 0.785 | 0.972 | 1.250 |

At `t = 0.25` the momentum-independent part is a third of the ring part on
6³; from `t = 0.75` on 4³ and 6³, and at `t = 0.5` on 8³, it is the larger.

## What this does not do

- **Guide-dependent bias.** A later fine scan (draft PR 9266) found that
  the fixed-population energy at fixed `t` depends on the guide's charge
  penalty beyond the errors quoted here: on 6³ at `t = 0.35`, penalties
  `1.0` and `1.2` give energies `1.22 ± 0.16` apart (0.6 per cent). The
  differences in this note use one penalty for all energies at a given `t`,
  which removes the part of the bias that does not change with `t` or `M`.
  A same-penalty probe there reproduces the `t = 0.25` link expectation on
  6³ (`0.1033` against `0.1016 ± 0.0020`). The absolute energies,
  the homogeneity value of `u` and `χ̄` carry a bias of the penalty's size that
  is not in the quoted errors. With one penalty for a whole grid, open PR
  9268 found link expectations on 6³ that still differ by 0.041–0.077 between
  penalties 0.8 and 1.1 at `t = 0.30–0.50`, and on 4³ by up to 0.032 at
  `t ≥ 0.4`; the values in that window here carry a guide dependence of that
  size.
- It claims no phase, transition, mass or limit: the rapid change is seen on
  three small tori at five hopping values and one charge mass.
- The moment bound is an upper bound. Its momentum-independent part neither
  shows nor excludes a gap of the transverse excitation.
- `α_G` was read in open PR 9258 as the comparator's static-pair tail over its
  velocity, with static charges. The comparator has no moving charges; here
  `α_G` is only the combination `(1/(χ̄ u))^{1/2} / (2π)` of two measured
  numbers. It is not a coupling of any physical field and is compared with no
  measured value.
- The static pair energy with moving charges is not measured here.
- It adopts no clause, charge mass, comparator, guide or method.

## Prior art (not premises)

Fradkin and Shenker 1979 (lattice gauge theories with unit-charge matter,
whose strong-hopping and confining regimes are continuously connected);
Hermele, Fisher and Balents 2004 (the Coulomb phase of quantum ice); Trivedi
and Ceperley 1990, Calandra Buonaura and Sorella 1998 (fixed-population
projectors). All cited as prior art, not as premises.

## Checks

The runner has three checks: the exact 2³ control with the single-link term
on six links, including the homogeneity identity; the `t = 0` limit against
the ring-model projector on 4³; the scan on 4³–8³ (reported). The fresh run
takes about two hours and thirteen minutes.

## Independent check

None yet.

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** the supplied link-qubit model with the ring clause, single-link term and charge mass on the stated tori and projector settings.
- **N2 — Independence:** self-checked; the 2³ control is internal to this runner.
- **N3 — Imports:** the clauses, charge mass, comparator and matching rule are supplied, not framework admissions.
- **N4 — Dependencies:** the landed comparator note's scope governs; open PRs are cited, not relied on.
- **N5 — Resolution:** finite Monte Carlo with heuristic errors; the guide was tuned outside the runner, and the fixed-population bias depends on it (draft PR 9266).
- **N6 — Residuals:** larger tori, finer hopping steps, other charge masses, the static pair with moving charges and the transverse gap remain open.
- **N7 — Counterroutes:** other hopping clauses, guides, populations and orders of limits remain available.
- **N8 — Boundary:** source note, not an audit verdict.

## Premise authority

The framework boundary is [the current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).
