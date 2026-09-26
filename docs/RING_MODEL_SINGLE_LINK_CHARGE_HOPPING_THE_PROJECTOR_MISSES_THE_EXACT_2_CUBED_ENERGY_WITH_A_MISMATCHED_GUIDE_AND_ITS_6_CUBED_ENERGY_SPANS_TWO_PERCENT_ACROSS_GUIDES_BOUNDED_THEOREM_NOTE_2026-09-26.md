---
claim_id: ring_model_single_link_charge_hopping_the_projector_misses_the_exact_2_cubed_energy_with_a_mismatched_guide_and_its_6_cubed_energy_spans_two_percent_across_guides_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "The supplied ring clause with the single-link charge term of open PR 9263, H = -g sum_p (U_p + U_p^dag) - t sum_l sigma^x_l + M sum_v Q_v^2 (g = 1, M = 2), and the fixed-population continuous-time projector of open PRs 9263 and 9268 with guide exp(alpha N_flip - gam sum_v Q_v^2), alpha = 0.2. Exact: the ground energies of the full 2^3 torus (the single-link term on all 24 links, 2^24 states) by matrix-free Lanczos, -9.631658548 at t = 0.35 and -10.430531975 at t = 0.5. Finite diagnostics: with gam = 0.8 the projector reproduces both within 0.01 at 1000 and 4000 walkers; at t = 0.5 with gam = 1.4 it sits 0.03 to 0.09 above the exact energy at 250, 1000 and 4000 walkers, from ice and random starts, in both halves of every run; on 6^3 at t = 0.35 with 1920 walkers its energy runs -199.7, -203.2, -203.8, -202.9, -201.1 for gam = 0.8, 1.1, 1.4, 1.7, 2.0 (spread 4.1), while the local-energy variance rises from 55 to 261; random starts reproduce the ice-start energies within errors. So this projector's energy grids carry guide-dependent errors of order one percent of the energy on 6^3 at these populations. No estimate of the model's link expectation, no phase and no physical reading."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ring_model_single_link_charge_hopping_projector_against_the_exact_full_2_cubed_torus_and_across_guides_2026_09_26.py
---

# Single-link charge hopping on the ring clause: the projector misses the exact 2³ energy with a mismatched guide, and its 6³ energy spans two percent across guides

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** exact reference energies and finite projector diagnostics; unaudited.

## Result

Open PR 9263 estimated the link expectation `⟨σ^x⟩(t)` of the ring clause with
single-link charge hopping from energies of a fixed-population projector.
Open PR 9268 then found that at a fixed guide the result still moves by
`0.04`–`0.08` on `6³` between two guide charge penalties. Its mixed energy is
exact for any positive guide only in the limit of an infinite population.
This block compares the projector with an exact result that has hopping on
every link, and measures how its `6³` energy depends on the guide.

- **An exact reference with hopping everywhere.** On the full `2³` torus,
  with the single-link term on all 24 links (`2²⁴` states), matrix-free
  Lanczos gives the ground energies `E₀ = -9.631658548` at `t = 0.35` and
  `-10.430531975` at `t = 0.5` (`M = 2`, `g = 1`), converged to `10⁻¹¹`. The control
  of open PR 9268 used the term on six links only.
- **A matched guide reproduces it.** With charge penalty `γ = 0.8`, the
  projector's energy is within `0.01` of both exact values with 1000 and
  4000 walkers (three independent runs each): biases `−0.0017` and `−0.0009` at `t = 0.35`, and `+0.0073` and `−0.0004` at `t = 0.5`, with 1000 and 4000 walkers.
- **A mismatched guide does not, at any population tried.** At `t = 0.5`
  with `γ = 1.4`, the projector's energy sits 0.03 to 0.09 above the exact one, at
  250, 1000 and 4000 walkers, from ice starts and from random starts, and in
  both halves of every run: averaged over three runs, the bias in the first and second halves is `+0.038` and `+0.093` with 250 walkers, `+0.088` and `+0.058` with 1000, `+0.059` and `+0.053` with 4000, and `+0.052` and `+0.029` with 4000 from random starts (mean `+0.059`). The effective sample size per
  generation is about 0.95, so the weights do not collapse within a
  generation. In a separate probe with 16 000 walkers, three runs scattered by
  `0.05`. Our reading, not a demonstration: a charge penalty that is too
  strong under-represents charged configurations that the ground state holds.
  The walkers reach those configurations rarely, and when they do the
  configurations carry large weights, so a fixed population misses them in
  most runs.
- **On 6³ the energy spans two percent across guides.** At `t = 0.35` with
  1920 walkers the energy is `−199.67 ± 0.25`, `−203.20 ± 0.16`, `−203.80 ± 0.12`, `−202.94 ± 0.12` and `−201.10 ± 0.19` at `γ = 0.8`, `1.1`, `1.4`, `1.7` and `2.0`, a spread of `4.1` (2 % of the energy); the local-energy variance is `55`, `78`, `103`, `171` and `261`, and the effective sample size per generation `0.88`, `0.79`, `0.78`, `0.66` and `0.50`. The lowest energy falls inside the
  range. The weighted variance of the local energy rises steadily with `γ`
  and the effective sample size per generation falls, so the guide with the
  smallest variance does not give the lowest energy.
- **Neither a trapped start nor a short run.** On `6³`, random starts
  reproduce the ice-start energies within errors at `γ = 0.8` and `1.1`, and
  every run is stationary from its first blocks: random starts give `−200.13 ± 0.14` against `−199.67 ± 0.25` from ice at `γ = 0.8` (`−1.6σ`) and `−203.29 ± 0.12` against `−203.20 ± 0.16` at `γ = 1.1` (`−0.5σ`); with 960 walkers the energies are `−199.82 ± 0.27` and `−202.42 ± 0.21`, so halving the population is not resolved at `γ = 0.8` and raises the energy by `0.78 ± 0.26` at `γ = 1.1`.

**Consequence for the link expectation.** A guide-dependent error of order
one percent of the energy, varying with `t`, can move the finite-difference
`⟨σ^x⟩` on `6³` by more than the `0.04`–`0.08` that open PR 9268 found between
two penalties. So the `6³` values of open PRs 9263 and 9268 are guide-dependent
diagnostics of this projector, not estimates of the model's `⟨σ^x⟩` with a
controlled error. The exact `2³` values, `⟨σ^x⟩ = 0.1600` at `t = 0.35` and
`0.2978` at `t = 0.5` (central differences of the Lanczos energy at
`t ± 0.002`, computed separately), are unaffected.

## Setting and decision points

- **D-clause and D-hopping (supplied, open PR 9263).** The ring clause and
  the single-link charge term, as there; nothing is adopted.
- **D-guide (method choice).** The guide `exp(α N_flip − γ Σ_v Q_v²)` is a
  calculational device. It fixes the sampling, not the model, and it enters
  the result only through finite-population error, which is the subject here.
- **D-projector (method choice).** A continuous-time walk with rates
  `|H_{σ'σ}| ψ(σ')/ψ(σ)`, a weight `exp(−∫ E_L)` and comb resampling to a
  fixed population every `dτ = 0.05`, as in open PRs 9263 and 9268. Separate
  checks (not in this runner) confirmed that the incremental rate tables
  equal a fresh recomputation after thousands of events, and that every rate
  equals the brute-force ratio on 2³ and 4³.

## Relation to other work

- Open PR 9266 (draft) and open PR 9268 found the guide dependence of
  energy differences at fixed `t`. This block shows it in the energy itself
  against an exact result, and on `6³` across five penalties.
- **Prior art (not premises).** Population-control and guide-quality
  effects in fixed-population and branching projector Monte Carlo are
  standard; see C. J. Umrigar, M. P. Nightingale, K. J. Runge, J. Chem. Phys.
  99, 2865 (1993), and M. Calandra Buonaura, S. Sorella, Phys. Rev. B 57,
  11446 (1998).

## What would settle the link expectation

- A guide with the ground state's charge statistics, for example with
  correlations between nearby charges, tuned by variance or energy on the
  exact `2³` torus at several `t`, and accepted only if two different guides
  then agree on each torus within errors.
- Or a sampler with no guide and no population, such as a world-line method
  whose updates reach every closed walk.

## Boundary

- Finite tori (`2³` exact, `6³` projector) and one hopping value each on
  `6³`. No estimate of the model's `⟨σ^x⟩` on `6³`, no size trend, no phase.
- The reading of the mismatched-guide bias as rare heavy configurations is
  an interpretation, not a demonstration.
- Supplied model, finite diagnostics, no physical reading.

## Reproduction

```bash
python3 scripts/ring_model_single_link_charge_hopping_projector_against_the_exact_full_2_cubed_torus_and_across_guides_2026_09_26.py
```

Five checks; prints `TOTAL: PASS=5 FAIL=0` in about 15 min.
