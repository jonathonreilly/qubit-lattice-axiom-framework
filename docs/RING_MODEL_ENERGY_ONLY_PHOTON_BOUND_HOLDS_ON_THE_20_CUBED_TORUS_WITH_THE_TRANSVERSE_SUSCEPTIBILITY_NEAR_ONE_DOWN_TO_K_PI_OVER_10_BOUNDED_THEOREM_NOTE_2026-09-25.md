---
claim_id: ring_model_energy_only_photon_bound_holds_on_the_20_cubed_torus_with_the_transverse_susceptibility_near_one_down_to_k_pi_over_10_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Supplied link-qubit ice model with the exact vertex Gauss law and the ring clause -g (U + U^dag) at V = 0, g = 1, on the 16^3 and 20^3 tori, walkers from loop-move samples of the zero-winding sector. Exact (restated from open PR 9236): for the cyclic triple of transverse modes, m_1 = 2 u s^2 and log-convexity give omega_min <= 2 s (u/chi)^(1/2) and S_T <= s (u chi)^(1/2). Finite projector estimates with resampling every dtau = 0.02 (960 walkers, projection 30, two seeds; errors are the larger of seed scatter and bin error, a heuristic): the exact 2^3 control in a probe field agrees with eight independent runs per field; on 16^3 at k = pi/8, chi = 1.022 +- 0.059 against open PR 9236's 1.038 +- 0.029 at dtau = 0.05; on 20^3, chi = 0.990 +- 0.032 at k = pi/10 and 1.096 +- 0.038 at pi/5, so the bounds are omega_min <= 1.074 s and 1.021 s and S_T <= 0.532 s and 0.560 s, and the comparator combination (1/(chi u))^(1/2) / (2 pi) is 0.299 and 0.284. No limit, phase, velocity of a physical field or comparison value is claimed."
upstream_dependencies:
  - minimal_axioms
  - ring_model_winding_sector_splittings_resolved_on_the_small_tori_and_a_multi_exponential_relaxation_at_the_pure_ring_point_bounded_theorem_note_2026-09-24
  - gaussian_lattice_maxwell_comparator_gives_a_linear_size_independent_transverse_structure_factor_and_misses_the_pure_ring_level_step_bounded_theorem_note_2026-09-24
runner: scripts/ring_model_energy_only_photon_bound_on_the_20_cubed_torus_2026_09_25.py
---

# The energy-only photon bound holds on the 20³ torus, with the transverse susceptibility near one down to k = π/10

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** exact inequalities of the supplied model (restated), with finite projector estimates on 16³ and 20³; unaudited.

## Result

Open PR 9236 bounded the lowest transverse excitation of the pure-ring
point from ground-state energies alone, on tori up to 16³, and left larger
tori open because the projector's effective sample size per generation
falls with the number of plaquettes. Resampling every `dτ = 0.02` instead
of `0.05` keeps it near 0.76 on 20³. This block measures the susceptibility
there.

- **The susceptibility stays near one.** On 20³, `χ̄ = 0.990 ± 0.032` at
  `k = π/10` and `1.096 ± 0.038` at `k = π/5`. On 16³, open PR 9236 found
  `1.038 ± 0.029` at `π/8` and `1.114 ± 0.020` at `π/4`; the 20³ values lie
  1.1 and 0.4 standard errors from those at the neighbouring momenta. The
  ratio `χ̄(π/10)/χ̄(π/5) = 0.903 ± 0.043` gives an exponent
  `p = −0.15 ± 0.07` in `χ̄ ∝ k^{−p}`, within one standard error of open PR
  9236's `−0.080 ± 0.011`; a residual constant in the structure factor
  would need `p = 1`, a quadratic mode `p = 2`.
- **The bounds on 20³.** With `u = 0.28579`, the lowest transverse
  excitation is at most `0.336` at `π/10` and `0.631` at `π/5`, that is
  `1.074 s(k)` and `1.021 s(k)`, and the triple-averaged structure factor
  is at most `0.532 s(k)` and `0.560 s(k)`.
- **The finer resampling does not move the 16³ value.** At `k = π/8` on
  16³, `dτ = 0.02` gives `1.022 ± 0.059` against `1.038 ± 0.029` at
  `dτ = 0.05` (−0.2 σ).
- **The comparator combination.** `(1/(χ̄ u))^{1/2} / (2π)` is `0.299` at
  `π/10` and `0.284` at `π/5`, against `0.286` on 8³ (open PR 9258).

Supplied model, finite estimates with two seeds on 20³: the numbers extend
the flat susceptibility of open PR 9236 by one torus size; they are
estimates of bounds, not certified enclosures, and no limit is claimed.

## Setting and decision points

- **D-gauss, D-ring (landed).** Link qubits with the exact vertex Gauss
  law and the covariant plaquette clause `−g (U + U†)` at `V = 0`, `g = 1`,
  on `L³` tori, walkers started from loop-move samples of the zero-winding
  sector
  (`RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24.md`).
- **The mode triple, the probe and the bounds (open PR 9236).** The
  cyclic triple of transverse modes (`a`-links modulated along `a + 1`), the
  diagonal probe field `−h Σ cos(k x_b) σ`, the susceptibility `χ̄` from
  `E(0)`, `E(h)`, `E(2h)` with the `h⁴` term eliminated, and the moment chain
  `ω_min ≤ 2 s (u/χ̄)^{1/2}`, `S̄_T ≤ s (u χ̄)^{1/2}` with `s = 2 sin(k/2)` and
  `u = −E_0/N_p`.
- **The projector (method).** The compiled continuous-time projector of
  open PR 9236 with a fixed population of 960 walkers, projection 30 per
  run and resampling every `dτ = 0.02` (0.05 there). The effective sample
  size per generation falls roughly as `exp(−(0.17 N_p^{1/2} dτ)²)`; at
  `dτ = 0.02` it stays near 0.76 on 20³ (24000 plaquettes), where
  `dτ = 0.05` would leave about 0.18.
- **The comparator (landed).** The Gaussian comparator of
  `GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24.md`
  with `K = 4u`, for the combination `α_G = (1/(χ̄ u))^{1/2} / (2π)` (open
  PR 9258).

None is adopted.

## Theorem 1 — the bounds (restated from open PR 9236)

For the cyclic triple at momentum `k`, with `m_j` the moments of the
triple-averaged spectral weights: `m_1 = 2 u s²` exactly, without any
symmetry of the state; `m_{−1} = χ̄/2`; `m_0 = S̄_T`. Log-convexity of the
moments gives `ω_min ≤ (m_1/m_{−1})^{1/2} = 2 s (u/χ̄)^{1/2}` and
`S̄_T ≤ (m_1 m_{−1})^{1/2} = s (u χ̄)^{1/2}`. With exact energies these are
rigorous; with projector estimates they are estimates of bounds. A finite
`χ̄` as `k → 0` bounds the lowest transverse excitation by a linear law in
`s`. ∎

## Diagnostic 1 — the exact 2³ control at `dτ = 0.02`

On the exact 2³ component (864 states), eight independent runs per probe
field (400 walkers, 4000 generations each) give `−9.02489 ± 0.00252`,
`−9.22726 ± 0.00248` and `−9.86469 ± 0.00264` at `h = 0`, `0.15` and `0.30`,
against the exact `−9.026721`, `−9.227240` and `−9.869211` (`+0.7`, `−0.0`
and `+1.7` standard errors). The run-to-run scatter, `0.0070`–`0.0075`, is
about 15 per cent above the mean 10-bin error of a single run. A first
certifying run used one run per field with its 10-bin
error and missed at `h = 0.15` by 3.5 of those errors. Outside the runner,
24 independent runs per field at `dτ = 0.02` put the mean within 1.3
standard errors of exact diagonalization at `h = 0.15` and `0.30`: the miss
was the single run's error bar, not a bias of the finer resampling. The
control now uses independent runs, and the 16³ and 20³ runs, which use the
same seeds, reproduce the first run's values to every printed digit.

## Diagnostic 2 — the susceptibility and the bounds

960 walkers, projection 30, probe fields 0.15 and 0.30, two seeds; `u` from
the plain energy of each torus; `s = 2 sin(k/2)`.

| torus | `k` | `χ̄` (seeds) | bound on `ω_min` | bound / `s` | bound on `S̄_T` | bound / `s` | `(1/(χ̄u))^{1/2}/(2π)` |
|---|---|---|---|---|---|---|---|
| 16³ | π/8 | 1.022 ± 0.059 | — | — | — | — | — |
| 20³ | π/10 | 0.990 ± 0.032 (1.016, 0.964) | 0.3361 | 1.074 | 0.1665 | 0.532 | 0.2991 |
| 20³ | π/5 | 1.096 ± 0.038 (1.134, 1.058) | 0.6311 | 1.021 | 0.3459 | 0.560 | 0.2843 |

`u` is `0.28671` on 16³ and `0.28579` on 20³. The projector costs 7.9 and
18.7 ms per walker and unit of imaginary time on 16³ and 20³.

## What this does not do

- It claims no limit: one more torus size, two seeds on it, and heuristic
  errors.
- The bounds are evaluated with projector estimates and are estimates of
  bounds, not certified enclosures.
- The comparator combination is a number of the Gaussian comparator
  evaluated with the model's energies; it is not a coupling of any physical
  field and is compared with no measured value.
- It adopts no clause, Gauss law, comparator, matching rule or method.

## Prior art (not premises)

Hermele, Fisher and Balents 2004 and Benton, Sikora and Shannon 2012 (the
Coulomb phase of quantum ice); the f-sum rule and moment inequalities of
linear response; Trivedi and Ceperley 1990, Calandra Buonaura and Sorella
1998 (fixed-population projectors). All cited as prior art, not as
premises.

## Checks

The runner has three checks: the exact 2³ control at `dτ = 0.02` with
independent runs per field; the 16³ value at `k = π/8` against open PR
9236's; the susceptibility, bounds and comparator combination on 20³
(reported). The fresh run takes about one hour and fifty minutes.

## Independent check

None yet.

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** the supplied link-qubit ice model and clause on the stated tori and projector settings.
- **N2 — Independence:** self-checked; the 2³ control is internal to this runner.
- **N3 — Imports:** the Gauss law, clause, comparator and matching rule are supplied, not framework admissions.
- **N4 — Dependencies:** the landed parents' scopes govern; open PRs are cited, not relied on.
- **N5 — Resolution:** finite Monte Carlo with heuristic errors; two seeds on 20³.
- **N6 — Residuals:** larger tori, more seeds, smaller momenta and the structure factor itself remain open.
- **N7 — Counterroutes:** other mode sets, guides, populations and resampling intervals remain available.
- **N8 — Boundary:** source note, not an audit verdict.

## Premise authority

The framework boundary is [the current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).
