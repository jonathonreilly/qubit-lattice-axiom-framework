---
claim_id: ring_model_pure_ring_point_transverse_fluctuations_at_the_smallest_momentum_are_a_third_of_the_uniform_ice_constant_and_the_feynman_photon_bound_shows_no_resolved_power_on_small_tori_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: spin-1/2 link fields on the cubic lattice with the exact vertex Gauss law (cubic ice) and the covariant plaquette clause -g (U + U^dag) at V = 0, g = 1 (open PRs 9066, 9072); the guided continuous-time projector Monte Carlo of open PR 9148 in the zero-winding sector of open PR 9153. Exact: for the transverse field mode O_a(k) = N^{-1/2} sum_{a-links} e^{ikx} sigma (the landed uniform-ice normalisation) the sum rule <0|O^dag (H - E_0) O|0> = 2 u_0 s^2 holds in every state, u_0 = -E_0/N_p the ring expectation per plaquette and s^2 = 2 - 2 cos k, so the Feynman quotient omega_SMA(k) = 2 u_0 s^2 / S_T(k) needs only the energy and the pure structure factor; on the 2^3 torus (9600 ice states; flip component of the canonical state 864 states, E_0 = -9.026721) the sum rule holds to 1e-9, S_T(pi) = 1.012148, omega_SMA = 2.9728 against the lowest coupled level 2.5173, and the forward-walking estimators reproduce S_T and C(tau <= 1) within errors while the mixed estimator is 5.6 standard errors low. Finite diagnostics (120 walkers, projection 40, forward lag 2, ten-bin errors): uniform ice has S_T(k_min) = 1.51, 1.53, 1.50 on 4^3, 6^3, 8^3 (constant; quotient quadratic, 8^3 value 0.2034 against the landed 0.2027); the pure-ring ground state has S_T(k_min) = 0.692 +- 0.013, 0.557 +- 0.022, 0.575 +- 0.028 (lag 4 agrees within errors), a fall S(4)/S(8) - 1 = 0.20 at 3.2 standard errors, pairwise exponents 0.54 +- 0.11 (4^3-6^3) and -0.11 +- 0.22 (6^3-8^3), three-point 0.35 +- 0.07; along the 8^3 zone S_T = 0.575, 0.833, 1.019 at k = pi/4, pi/2, 3pi/4; omega_SMA(k_min) = 1.690 +- 0.032, 1.037 +- 0.041, 0.587 +- 0.029, omega_SMA L = 6.76, 6.22, 4.69 against the uniform-ice 2.71, 2.03, 1.63; the 8^3 bound at pi/4, pi/2, 3pi/4 is 0.587, 1.382, 1.775 (ratios 2.36, 3.03; linear 2, 3; quadratic 4, 9); the ground-state correlation C(tau) of the mode has early rates equal to the bound within errors and late rates 1.40 +- 0.15, 0.77 +- 0.21, 0.47 +- 0.18 on [0.5, 1.0], upper bounds on the lowest coupled excitation at k_min. Auxiliary runs (not in the runner): 60 walkers on 6^3 give S_T(k_min) = 0.589 +- 0.034 and 240 walkers on 8^3 give 0.541 +- 0.027 with energies within 0.0002 per plaquette of the 120-walker values. No gap value, no dispersion law, no phase and no thermodynamic limit is claimed; no power law in L or k is resolved on 4^3-8^3."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_rk_photon_single_mode_bound_is_quadratic_with_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
runner: scripts/ring_model_pure_ring_point_feynman_photon_bound_and_pure_structure_factor_at_the_smallest_momentum_2026_09_24.py
---

# At the pure-ring point the transverse fluctuations at the smallest momentum are a third of the uniform-ice constant, and the Feynman photon bound shows no resolved power on the small tori

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact identities with finite numerical diagnostics under supplied decision points; unaudited.

## Result

Open PR 9153 left the photon itself open at the pure-ring point `V = 0`:
its dispersion or its gap, which the relaxation estimator could not give.
The landed note
`UNIFORM_ICE_RK_PHOTON_SINGLE_MODE_BOUND_IS_QUADRATIC_WITH_THE_SUM_RULE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md`
bounds the excitation of the uniform-ice (RK) state at momentum `k` by the
Feynman quotient `2 n_f s²/S_T(k)` and finds it quadratic, because the
transverse structure factor of uniform ice is constant at small `k`. This
note computes the same quotient in the pure-ring ground state.
- **The numerator is exact.** In every state,
  `⟨O†(H − E_0)O⟩ = 2 u_0 s²` with `u_0 = −E_0/N_p` the ring expectation
  per plaquette (Theorem 1). The projector's mixed energy, which is
  unbiased, fixes it; the whole content of the bound is the pure structure
  factor `S_T(k)` of the true ground state.
- **The mixed estimator will not do; forward walking does.** On the exact
  2³ torus the mixed `S_T` is 5.6 standard errors low and the lineage
  (forward-walking) estimator reproduces `S_T` and the correlation function
  `C(τ ≤ 1)` within errors (Theorem 2 and Method). On 4³ the mixed value is
  25 % above the pure one.
- **Uniform ice is flat in `L` and in `k`; the pure-ring state is neither.**
  Uniform ice has `S_T(k_min) = 1.51, 1.53, 1.50` on 4³, 6³, 8³ and the
  same value across the zone. The pure-ring ground state has
  `S_T(k_min) = 0.692 ± 0.013, 0.557 ± 0.022, 0.575 ± 0.028`: about a third
  of the uniform-ice constant, falling from 4³ to 6³ (five standard errors)
  and level between 6³ and 8³ (pairwise exponents `0.54 ± 0.11` and
  `−0.11 ± 0.22`); along the 8³ zone it rises, `0.575, 0.833, 1.019` at
  `k = π/4, π/2, 3π/4`.
- **The bound is three times the uniform-ice bound and falls faster than
  `1/L`.** `ω_SMA(k_min) = 1.690 ± 0.032, 1.037 ± 0.041, 0.587 ± 0.029`, so
  `ω_SMA·L = 6.76, 6.22, 4.69` against `2.71, 2.03, 1.63` for uniform ice;
  on 8³ the bound at `π/4, π/2, 3π/4` is `0.587, 1.382, 1.775`, ratios
  `2.36` and `3.03` between the linear values (2, 3) and the quadratic ones
  (4, 9).
- **The mode is close to a single excitation.** The ground-state
  correlation `C(τ)` of the mode has effective rates equal to the bound
  within errors on `[0, 0.3]`, as the identity `−C′(0)/C(0) = ω_SMA`
  requires, and late rates `1.40 ± 0.15, 0.77 ± 0.21, 0.47 ± 0.18` on
  `[0.5, 1.0]`, each an upper bound on the lowest coupled excitation at
  `k_min`; on 4³ and 6³ the rates are flat to `τ ≈ 1.5`.
- **Population control is not the story.** 60 against 120 walkers on 6³
  and 240 against 120 on 8³ move `S_T(k_min)` by less than 1.2 standard
  errors (`0.589 ± 0.034` vs `0.557 ± 0.022`; `0.541 ± 0.027` vs
  `0.575 ± 0.028`) and the energies by 0.0002 and 0.0001 per plaquette.

Supplied model, finite diagnostics: no gap value, no dispersion law, no
phase and no thermodynamic limit is claimed. What the small tori show is
that the pure-ring point differs from the RK point in the momentum
dependence of its transverse field fluctuations, suppressed to a third at
the smallest momenta and rising toward the zone boundary, and that its
Feynman bound falls faster than `1/L` between 6³ and 8³ without settling
on a power: the fall from 4³ to 6³ is weaker than a linear photon's, and a
level step from 6³ to 8³ would, if it persisted, make the bound quadratic
like uniform ice with a three times smaller constant. Larger tori decide.

## Setting and decision points

- **D-gauss, D-roles, D-ring (open PRs 9066, 9072).** Link qubits at link
  sites of the doubled lattice; the exact vertex Gauss law, three in and
  three out; the covariant plaquette clause `−g (U + U†)`; `V = 0`; `g = 1`
  sets the unit of energy.
- **The projector (method).** The guided continuous-time Green's function
  Monte Carlo of open PR 9148, guiding function `exp(0.2 N_flip)`, walkers
  started in the zero-winding sector from the canonical ice state of open
  PR 9153 after winding-preserving loop equilibration.
- **The observable (method).** The transverse field mode
  `O_a(k) = N^{−1/2} Σ_{a-links} e^{i k x} σ_l`, `a = y, z`, `k = 2πm/L`
  along `x`, `σ_l = ±1` the link arrow, `N = L³` vertices — the same
  normalisation as the landed note
  `UNIFORM_ICE_RK_PHOTON_SINGLE_MODE_BOUND_IS_QUADRATIC_WITH_THE_SUM_RULE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md`,
  so that its uniform-ice numbers and these are on one scale. The two
  polarisations are averaged.

None is adopted.

## Theorem 1 — the Feynman quotient at the pure-ring point is fixed by the energy and one structure factor

Let `|0⟩` be the ground state of `H = −Σ_p (U_p + U_p†)` on the flip
component of the walkers, `E_0` its energy, `u_0 = −E_0/N_p` the mean ring
expectation per plaquette (`N_p = 3N`), and `s² = 2 − 2 cos k`.

1. **Sum rule.** For every state, the double commutator is a ring operator
   with a form factor: a flip of the `xy`-plaquette at `v` changes `O_y(k)` by
   `∓2 N^{−1/2} e^{ikv_x}(e^{ik} − 1)`, and `xz`-plaquettes do the same for
   `O_z`, while the other plaquettes leave both modes unchanged. Hence
   `f(k) := ⟨0|O†(H − E_0)O|0⟩ = ½ ⟨0|[O†,[H,O]]|0⟩ = 2 u_0 s²`
   — the same identity as the landed uniform-ice sum rule
   (`2 n_f s²`, where `n_f` is the flippable fraction), with the ring
   expectation `u_0` of the pure-ring ground state in place of the uniform
   flippable fraction. The energy per plaquette, which the projector's mixed
   estimator gives without bias, therefore fixes the numerator exactly.
2. **Quotient.** Since `O` is diagonal, `O|0⟩` lives on the same
   configurations as `|0⟩`; if the component is translation-invariant then
   `⟨0|O|0⟩ = 0` for `k ≠ 0` and, the ground state of a connected stoquastic
   component being unique,
   `ω_SMA(k) := f(k)/S(k) ≥ Δ_min(k)`, `S(k) = ⟨0|O†O|0⟩`,
   where `Δ_min(k)` is the lowest excitation energy of the component with
   non-zero weight `|⟨n|O|0⟩|²`.
3. **Correlation chain.** `C(τ) = ⟨0|O† e^{−(H − E_0)τ} O|0⟩ = Σ_n |⟨n|O|0⟩|² e^{−(E_n − E_0)τ}`
   has `C(0) = S(k)`, `−C′(0)/C(0) = ω_SMA(k)`, and a non-increasing
   effective rate `−d ln C/dτ` (a positive mixture of exponentials is
   log-convex) that tends to `Δ_min(k)`. So every effective rate on a fixed
   window is an upper bound on `Δ_min(k)` and a lower bound on `ω_SMA(k)`.

The content of the quotient at the pure-ring point is thus one number per
momentum: the structure factor `S(k)` of the true ground state, which needs
a pure (not mixed) estimator.

## Theorem 2 — the exact 2³ torus

On the 2³ torus (8 vertices, 24 links, 24 plaquettes) there are 9600 ice
states; the flip component of the canonical zero-winding state has 864 states
and 6912 directed flips, ground energy `E_0 = −9.026721` (the value that
open PR 9148's control used), and `⟨0|O|0⟩ = 4·10⁻¹⁶` at `k = π`.
- The sum rule holds to all printed digits: `f = 3.008907 = 2 u_0 s²`.
- `S = 1.012148`, `ω_SMA = 2.97279`, while the three lowest excited
  multiplets (at 2.2258, 2.2919, 2.3415 above `E_0`) carry zero weight and
  the first that couples sits at `Δ_min = 2.5173`: the bound is 18 % above
  the true level at the zone boundary of the smallest torus.
- The exact `C(τ)`, from the matrix exponential on the component, has
  effective rates falling from 2.93 on `[0, 0.1]` to 2.52 on `[2, 3]`.

## Method — forward walking, and why the mixed estimator will not do

Each walker carries the history of `O` along its lineage; at a
reconfiguration the offspring inherit the parent's history. The estimate of
`S` at forward-walking lag `τ_f` averages `|O|²` recorded `τ_f` earlier on
the lineages of the current, weighted population, which converges to the
pure ground-state value as the excitations coupling the guiding function to
the ground state decay; `C(τ)` averages the lineage products
`O(t)·O*(t − τ)` with a further forward lag after `t`. Against the exact 2³
numbers (200 walkers, `τ = 40`, blocks of 0.05): the mixed `S` is
`0.984 ± 0.018` (1.5 standard errors low), the forward-walking values at
`τ_f = 0.5 … 4` are `1.018 ± 0.016 … 1.019 ± 0.048`, all within errors of
`1.0121`; the ten correlation values `C(τ ≤ 3)` agree within 1.4 standard
errors except at `τ = 1.0` (+2.7) and `τ = 2.0` (−2.3), where the signal
is at the noise level. Stated biases: population control (fixed
population, reconfiguration every 0.05, first order in the inverse walker
number); the remaining lag dependence of the forward-walking plateau (the
lag-4 values are reported next to lag-2); the dependence on the start
(the zero-winding sector, one flip component); and ten-bin standard errors
of correlated block estimates, which can understate the error at long
forward lags where lineages collapse onto few ancestors.

## Diagnostic — the pure-ring point on 4³, 6³, 8³

Walkers (120 per size) start in the zero-winding sector from the canonical
ice state of open PR 9153 after winding-preserving loop equilibration with
the guiding function, and are projected for `τ = 40` in blocks of 0.05; the
first 8 are discarded. `k_min = 2π/L`; the mode is averaged over the three
axes and both transverse polarisations; `S_T` pure means forward lag 2 (lag
4 in brackets); rates are chords of `ln C(τ)` on the stated windows, with
errors propagated as if the two ends were independent (conservative, since
they are positively correlated).

| torus | `e_0` per plaquette (open PR 9148) | `S_T(k_min)` mixed | `S_T(k_min)` pure | uniform ice | `ω_SMA` | `ω_SMA·L` | uniform-ice `ω·L` | rate `[0, 0.3]` | rate `[0.5, 1]` |
|---|---|---|---|---|---|---|---|---|---|
| 4³ | −0.29263 ± 0.00031 (−0.2926) | 0.862 | 0.692 ± 0.013 (0.688 ± 0.019) | 1.51 | 1.690 ± 0.032 | 6.76 ± 0.13 | 2.71 | 1.59 ± 0.12 | 1.40 ± 0.15 |
| 6³ | −0.28885 ± 0.00014 (−0.2883) | 0.702 | 0.557 ± 0.022 (0.567 ± 0.025) | 1.53 | 1.037 ± 0.041 | 6.22 ± 0.25 | 2.03 | 0.96 ± 0.23 | 0.77 ± 0.21 |
| 8³ | −0.28800 ± 0.00011 (−0.2871) | 0.636 | 0.575 ± 0.028 (0.564 ± 0.034) | 1.50 | 0.587 ± 0.029 | 4.69 ± 0.23 | 1.63 | 0.54 ± 0.24 | 0.47 ± 0.18 |

- **The level.** The pure-ring `S_T(k_min)` is 0.37–0.46 of the uniform-ice
  value on the same torus: the ring dynamics at `V = 0` removes about two
  thirds of the transverse field fluctuation at the smallest momentum. The
  guiding function alone (variational, `exp(0.2 N_flip)`) gets only part of
  the way (the mixed values above sit between).
- **The fall and the step.** `S(4³)/S(8³) − 1 = 0.20` at 3.2 standard
  errors; pairwise exponents `S ∝ L^{−ν}`: `ν = 0.54 ± 0.11` from 4³ to 6³
  and `−0.11 ± 0.22` from 6³ to 8³ (three-point fit `0.35 ± 0.07`, a poor
  summary of a fall followed by a level step). A linear photon has `ν = 1`
  (`S_T ∝ k`), uniform ice `ν = 0` (max/min ratio 1.02 here).
- **In `k` at fixed size.** On 8³, `S_T = 0.575 ± 0.028, 0.833 ± 0.040,
  1.019 ± 0.085` at `k = π/4, π/2, 3π/4`, rising toward the zone boundary
  where uniform ice stays near 1.5 at every `k`; at the shared momentum
  `π/2` the 8³ value exceeds the 4³ value `0.692 ± 0.013` by 3.4 standard
  errors, so the finite-size correction at fixed `k` grows with `L`. The
  two effects — smaller `k_min` lowers `S_T`, larger `L` at fixed `k` raises
  it — meet in the level step between 6³ and 8³.
- **The bound.** With `u_0 = 0.288–0.293` nearly size-independent,
  `ω_SMA ∝ s²/S_T`. The pure-ring bound is 2.5–3.0 times the uniform-ice
  bound at the same momentum; `ω_SMA·L` falls from 6.76 to 4.69 (8³ against
  4³: 7.9 standard errors), faster than `1/L` and slower than `1/L²`
  (uniform ice: 2.71 → 1.63). On 8³, `ω(2k)/ω(k) = 2.36` and
  `ω(3k)/ω(k) = 3.03` sit between the linear values (2, 3) and the
  quadratic ones (4, 9); the lattice form `2 sin(k/2)` gives 1.85, 2.41.
- **Single-mode character and the excitation itself.** The early rate
  equals the bound within errors on every size, as `−C′(0)/C(0) = ω_SMA`
  requires, and the late rate is at or below it: `1.40 ± 0.15`,
  `0.77 ± 0.21`, `0.47 ± 0.18` on `[0.5, 1]`, so `late·L = 5.6, 4.6, 3.8`.
  On 4³ and 6³ the rates are flat to `τ ≈ 1.5` (the mode decays as nearly
  one exponential); on 8³ the 120-walker correlation is resolved only to
  `τ ≈ 1`, while the 240-walker auxiliary run resolves it to `τ = 2` with
  rates 0.59, 0.54, 0.52 on `[0, 0.3]`, `[0.5, 1]`, `[1, 2]`. Every late
  rate is an upper bound on the lowest coupled excitation at `k_min`.
- **Population control (auxiliary runs, not in the runner).** 60 walkers on
  6³: `e_0 = −0.28864 ± 0.00025`, `S_T(k_min) = 0.589 ± 0.034`; 240 walkers
  on 8³: `e_0 = −0.28813 ± 0.00008`, `S_T(k_min) = 0.541 ± 0.027`,
  `S_T(π/2) = 0.751 ± 0.018`. The 8³ energies drift down with the walker
  number (−0.2871 at 60 in open PR 9148, −0.2874 at 80 in open PR 9153,
  −0.2880 at 120, −0.2881 at 240), a population-control bias of about 0.001
  per plaquette at 60 walkers; `S_T` moves by less than 1.2 standard errors.

A first pass of this block (two modes per size, 120/100/80 walkers,
`τ = 40/32/28`, another seed) gave `S_T(k_min) = 0.705 ± 0.024`,
`0.522 ± 0.031`, `0.459 ± 0.080`; its 8³ value is 1.4 standard errors
below the certified one, and the flat `ω_SMA·L` it suggested did not
survive the six-mode statistics. ∎

## What this means for the lanes

- **Photon lane.** The pure-ring point differs from the RK point exactly
  where a photon would show it — the momentum dependence of the transverse
  field fluctuations — and its Feynman bound falls faster than `1/L`, but
  the small tori resolve no power: the fall from 4³ to 6³ is weaker than a
  linear photon's, and the level step from 6³ to 8³ would, if it
  persisted, make the bound quadratic like uniform ice with a three times
  smaller constant. Together with no plaquette order to 8³ (open PRs 9146,
  9148) and a flux-quantum cost compatible with `1/L` (open PR 9153), the
  diagnostics lean toward a liquid and do not decide its photon.
- **What the framework supplied.** The Gauss law, the ring and the point
  `V = 0` are decision points; the mode, the projector, the forward walking
  and the Feynman quotient are methods; the landed uniform-ice bound is the
  comparison, cited by filename.

## What stays open

- A 10³ or 12³ torus at this precision, which decides between a continued
  fall of `S_T(k_min)` (a photon) and a level (a residual constant).
- The same quotient as `V/g` moves off the pure-ring point toward the RK
  point, where it must turn quadratic, and the finite-size correction at
  fixed `k`, which grows with `L` here.
- Whether the flip component the walkers occupy is the whole zero-winding
  sector on 4³–8³ (it is 864 of the sector's states on 2³).
- Independent checks of every number here.

## Prior art

Feynman 1954 and Feynman–Cohen 1956 (the single-mode bound); Rokhsar and
Kivelson 1988; Trivedi and Ceperley 1990 (Green's function Monte Carlo and
forward walking); Hermele, Fisher and Balents 2004; Sikora, Pollmann,
Shannon, Penc and Fulde 2011; Shannon, Sikora, Pollmann, Penc and Fulde
2012; Benton, Sikora and Shannon 2012 (suppressed pinch points in quantum
spin ice). All cited as prior art, not as premises.

## Checks

The runner has 5 checks and all pass in about 5 minutes, single-threaded.

| Check | Result |
|---|---|
| Exact 2³ torus | 9600 ice states; component 864 / 6912 flips; `E_0 = −9.026721`; sum rule to 1e-9; `⟨O⟩ = 0`; bound 2.9728 ≥ lowest coupled level 2.5173; exact rates non-increasing. |
| Estimators vs exact | Mixed energy, forward-walking `S_T` (lags 1, 2) and `C(τ ≤ 1)` within the stated standard errors of the exact values; the mixed `S_T` 5.6 standard errors low. |
| Uniform-ice reference | `S_T(k_min)` constant (ratio 1.02); `n_f` and the 8³ quotient (0.2034 vs 0.2027) reproduce the landed runner; `ω·L` falls. |
| Pure-ring point | Energies within 0.002 of open PR 9148; `S_T(k_min)` resolved (errors ≤ 12 %) with a lag-2/lag-4 plateau; the fall at 3.2 standard errors (threshold 2.5); three-point and pairwise exponents. |
| The bound | `ω_SMA·L` by size (reported); the 8³ dispersion; early rate ≤ bound and late rate ≤ early rate within errors. |

## Independent check

None yet. The runner was rerun from a clean shell to write the cache;
seeded Monte Carlo reproduces the numbers. The first pass quoted above is a
second seed at lower precision, and the two auxiliary walker-number runs
are a third and fourth.

## What this does not do

- It adopts no clause, Gauss law, method or comparison.
- It claims no gap value, no dispersion law, no phase and no thermodynamic
  limit; no power law in `L` or `k` is resolved, and the Feynman quotient
  is an upper bound.
- It does not resolve the late-time correlation on 8³ beyond `τ ≈ 2` and
  does not prove that the walkers' flip component is the whole
  zero-winding sector.
