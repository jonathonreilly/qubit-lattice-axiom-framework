---
claim_id: ring_model_energy_only_photon_bound_on_the_24_cubed_torus_the_transverse_susceptibility_at_k_pi_over_12_stays_finite_with_a_softening_not_resolved_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Supplied link-qubit ice model with the exact vertex Gauss law and the ring clause -g (U + U^dag) at V = 0, g = 1, on the 16^3 and 24^3 tori, walkers from loop-move samples of the zero-winding sector, each probe field with its own guide field. Exact (restated from open PR 9236): for the cyclic triple of transverse modes, m_1 = 2 u s^2 and log-convexity give omega_min <= 2 s (u/chi)^(1/2) and S_T <= s (u chi)^(1/2). Finite projector estimates with resampling every dtau = 0.015 (960 walkers, projection 30, two seeds; errors are the larger of seed scatter and bin error, a heuristic): the exact 2^3 control in a probe field agrees with eight independent runs per field; on 16^3 at k = pi/8, chi = 1.039 +- 0.022 against open PR 9236's 1.038 +- 0.029 at dtau = 0.05; on 24^3 at k = pi/12, chi = 0.831 +- 0.077 (seeds 0.908 and 0.754, 1.7 standard errors below open PR 9265's 20^3 value at pi/10), so omega_min <= 1.171 s and S_T <= 0.487 s, and the comparator combination (1/(chi u))^(1/2) / (2 pi) is 0.327. No limit, phase, velocity of a physical field or comparison value is claimed."
upstream_dependencies:
  - minimal_axioms
  - ring_model_winding_sector_splittings_resolved_on_the_small_tori_and_a_multi_exponential_relaxation_at_the_pure_ring_point_bounded_theorem_note_2026-09-24
  - gaussian_lattice_maxwell_comparator_gives_a_linear_size_independent_transverse_structure_factor_and_misses_the_pure_ring_level_step_bounded_theorem_note_2026-09-24
runner: scripts/ring_model_energy_only_photon_bound_on_the_24_cubed_torus_2026_09_26.py
---

# The energy-only photon bound on the 24³ torus: the transverse susceptibility at k = π/12 stays finite, with a softening not resolved

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** exact inequalities of the supplied model (restated), with finite projector estimates on 16³ and 24³; unaudited.

## Result

Open PR 9236 bounded the lowest transverse excitation of the pure-ring
point from ground-state energies alone on tori up to 16³, and open PR 9265
carried the transverse susceptibility to 20³ (`0.990 ± 0.032` at `k = π/10`).
This block adds the 24³ torus (41 472 plaquettes), at the smallest momentum
yet, `k = π/12`, with resampling every `dτ = 0.015` so that the projector's
effective sample size per generation stays near 0.76.

- **The susceptibility at π/12 stays finite.** On 24³, `χ̄ = 0.831 ± 0.077`
  at `k = π/12`, from two seeds that give `0.908` and `0.754`. With
  `u = 0.28513` the bounds are `ω_min ≤ 0.3058 = 1.171 s(k)` and
  `S̄_T ≤ 0.1271 = 0.487 s(k)`: a finite susceptibility keeps the lowest
  transverse excitation under a linear law at this momentum as well.
- **A softening is not resolved.** The value lies 1.7 standard errors
  below open PR 9265's `0.990 ± 0.032` on 20³ at `k = π/10`. Two seeds
  cannot tell a gentle decrease of `χ̄` at the smallest momenta from
  scatter: the ratio `0.84 ± 0.08` is consistent with a flat susceptibility
  and with a mild fall. Each probe field uses its own guide field
  (`β = 0.5 h`), so the three energies of the fit do not share a guide.
  Open PR 9276 found, in the model with moving charges, that a
  fixed-population bias can depend on the guide. Whether that happens here
  at this population is not tested.
- **The finer resampling does not move the 16³ value.** At `k = π/8` on
  16³, `dτ = 0.015` gives `1.039 ± 0.022` against `1.038 ± 0.029` at
  `dτ = 0.05` (open PR 9236) and `1.022 ± 0.059` at `dτ = 0.02` (open PR
  9265).
- **The comparator combination.** `(1/(χ̄ u))^{1/2} / (2π) = 0.327` at
  `π/12`, against `0.299` on 20³ at `π/10`; it moves with `χ̄`.

Supplied model, finite estimates with two seeds on 24³: the number adds one
torus size and one smaller momentum to open PRs 9236 and 9265. It keeps the
susceptibility finite but does not settle whether it stays flat. These are
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
  run and resampling every `dτ = 0.015` (0.05 in open PR 9236, 0.02 in open
  PR 9265). The effective sample size per generation falls roughly as
  `exp(−(0.17 N_p^{1/2} dτ)²)`; at `dτ = 0.015` it stays near 0.76 on 24³.
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

## Diagnostic 1 — the exact 2³ control at `dτ = 0.015`

On the exact 2³ component (864 states), eight independent runs per probe
field (400 walkers, 4000 generations each) give `−9.02751 ± 0.00305`,
`−9.22237 ± 0.00347` and `−9.87066 ± 0.00301` at `h = 0`, `0.15` and `0.30`,
against the exact `−9.026721`, `−9.227240` and `−9.869211` (`−0.3`, `+1.4`
and `−0.5` standard errors), with run-to-run scatter `0.0047`–`0.0098`.

## Diagnostic 2 — the susceptibility and the bounds

960 walkers, projection 30, probe fields 0.15 and 0.30, two seeds; `u` from
the plain energy of each torus; `s = 2 sin(k/2)`.

| torus | `k` | `χ̄` (seeds) | bound on `ω_min` | bound / `s` | bound on `S̄_T` | bound / `s` | `(1/(χ̄u))^{1/2}/(2π)` |
|---|---|---|---|---|---|---|---|
| 16³ | π/8 | 1.039 ± 0.022 | — | — | — | — | — |
| 24³ | π/12 | 0.831 ± 0.077 (0.908, 0.754) | 0.3058 | 1.171 | 0.1271 | 0.487 | 0.3270 |

`u` is `0.28680` on 16³ and `0.28513` on 24³. The projector costs 8.4 and
46.4 ms per walker and unit of imaginary time on 16³ and 24³.

## What this does not do

- It claims no limit: one more torus size, one momentum, two seeds, and
  heuristic errors. It does not decide whether `χ̄` stays flat or softens
  at the smallest momenta.
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

The runner has three checks: the exact 2³ control at `dτ = 0.015` with
independent runs per field; the 16³ value at `k = π/8` against open PR
9236's; the susceptibility, bounds and comparator combination on 24³
(reported, with open PR 9265's 20³ value beside it). The fresh run takes
about two hours and forty minutes.

## Independent check

None yet.

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** the supplied link-qubit ice model and clause on the stated tori and projector settings.
- **N2 — Independence:** self-checked; the 2³ control is internal to this runner.
- **N3 — Imports:** the Gauss law, clause, comparator and matching rule are supplied, not framework admissions.
- **N4 — Dependencies:** the landed parents' scopes govern; open PRs are cited, not relied on.
- **N5 — Resolution:** finite Monte Carlo with heuristic errors; two seeds on 24³.
- **N6 — Residuals:** more seeds on 24³, one guide for all three probe fields, larger tori, smaller momenta and the structure factor itself remain open.
- **N7 — Counterroutes:** other mode sets, guides, populations and resampling intervals remain available.
- **N8 — Boundary:** source note, not an audit verdict.

## Premise authority

The framework boundary is [the current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).
