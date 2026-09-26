---
claim_id: ring_model_single_link_charge_hopping_the_energy_minimising_guide_matches_the_2_cubed_reference_but_its_6_cubed_energy_still_falls_when_the_population_doubles_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Supplied finite sign-free ring plus all-link hopping Hamiltonian, g = 1, M = 2, and the finite-population guided projector of the landed note with guide exp(0.2 N_flip - gam sum Q^2). Numerical Lanczos Ritz references for the full 2^3 torus (-9.631658548 at t = 0.35, -10.430531975 at t = 0.5). Finite diagnostics: on 2^3 with 2000 walkers the lowest projector energy over penalties 0.3-1.1 lies within 0.006 of the reference at both t, and all penalties but a clearly mismatched one within 0.01; on 6^3 at t = 0.35 the penalty 1.2 gives the lowest of three energies with 1920 and with 3840 walkers, and doubling the population lowers the energy at every penalty, by 0.61 at 1.2. So choosing the energy-minimising penalty does not remove the finite-population bias on 6^3 at these populations. No controlled 6^3 energy or link expectation, stationarity proof, phase or physical identification."
upstream_dependencies:
  - minimal_axioms
  - ring_model_single_link_charge_hopping_the_projector_misses_the_exact_2_cubed_energy_with_a_mismatched_guide_and_its_6_cubed_energy_spans_two_percent_across_guides_bounded_theorem_note_2026-09-26
runner: scripts/ring_model_single_link_charge_hopping_projector_with_the_energy_minimising_guide_2026_09_26.py
---

# Single-link charge hopping: the energy-minimising guide matches the 2³ reference, but its 6³ energy still falls when the population doubles

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** numerical references and finite projector diagnostics; unaudited.

## Supplied setting

Use the supplied sign-free ring clause with the single-link term on every
link, `g = 1`, `M = 2`, and the finite-population guided projector of the
landed note
`RING_MODEL_SINGLE_LINK_CHARGE_HOPPING_THE_PROJECTOR_MISSES_THE_EXACT_2_CUBED_ENERGY_WITH_A_MISMATCHED_GUIDE_AND_ITS_6_CUBED_ENERGY_SPANS_TWO_PERCENT_ACROSS_GUIDES_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
with guide `exp(0.2 N_flip − γ Σ_v Q_v²)`. That note found the projector's
energy guide-dependent: close to the 2³ reference for one penalty, above it
for another, and spread by 2 per cent across penalties on 6³. A natural
remedy is to take, at each hopping value, the penalty that minimises the
projector energy. This block tests that remedy.

## Finite diagnostics reproduced by the runner

- **References.** Matrix-free Lanczos on the full `2³` torus (24 links,
  `2²⁴` states) gives the Ritz references `−9.631658548` at `t = 0.35` and
  `−10.430531975` at `t = 0.5`, converged to `10⁻¹¹`.
- **On 2³ the minimising penalty lands on the reference.** With 2000
  walkers and three runs per penalty, the projector's energy minus the
  reference is `+0.0036`, `+0.0003`, `+0.0036`, `+0.0036` and `+0.0025` at
  `γ = 0.3`, `0.5`, `0.7`, `0.9` and `1.1` for `t = 0.35`, and `+0.0026`,
  `+0.0034`, `−0.0031`, `+0.0040` and `+0.0374` for `t = 0.5`. The lowest
  energy sits within `0.004` of the reference at both `t`, near the
  run-to-run scatter. The one clearly mismatched penalty (`1.1` at
  `t = 0.5`) is also clearly the highest.
- **On 6³ it does not settle.** At `t = 0.35` the penalty `1.2` gives the
  lowest of three energies with both 1920 and 3840 walkers. Doubling the
  population lowers every energy: `−203.48 → −204.08` at `1.2`,
  `−203.41 → −203.91` at `1.4` and `−203.20 → −203.52` at `1.6`, with block
  errors `0.11`–`0.21`. So at these populations even the energy-minimising
  penalty carries a finite-population bias of at least `0.6` on 6³, about
  0.3 per cent of the energy.

## What this does not establish

- No controlled 6³ energy or link expectation: the lowest energy over three
  penalties still moves by more than its error bar when the population
  doubles, and an extrapolation in the population is not tested here.
- No stationarity or equilibration proof, phase or physical identification.
- The 2³ comparison is against numerical Ritz references, not a certified
  error bound; its agreement at the minimising penalty says nothing about
  larger tori.

## What would settle the link expectation

A guide that matches the ground state's charge statistics closely enough
that two different guides agree on each torus at feasible populations, or
a sampler without guide and population whose updates reach every closed
walk.

## Reproduction

```bash
python3 scripts/ring_model_single_link_charge_hopping_projector_with_the_energy_minimising_guide_2026_09_26.py
```

Three checks; prints `TOTAL: PASS=3 FAIL=0` in about 16 min.
