---
claim_id: ring_model_with_single_link_charge_hopping_changes_rapidly_between_weak_and_strong_hopping_and_its_moment_bound_stays_finite_at_small_momentum_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: 'Supplied finite sign-free ring plus single-link and charge-mass Hamiltonian: conditional Hellmann-Feynman,
  positive-scaling homogeneity and cyclic moment identities. Full finite projector scan is diagnostic only, with
  uncontrolled guide/population/projection and difference biases. No small-momentum finite bound, gap, phase, rapid-change
  location, size trend or physical coupling is established.'
upstream_dependencies:
- minimal_axioms
- ring_model_energy_only_bounds_on_the_pure_ring_photon_from_the_mode_averaged_transverse_susceptibility_bounded_theorem_note_2026-09-25
- ring_model_winding_sector_energies_give_an_electric_coupling_that_agrees_with_the_transverse_susceptibility_on_8_cubed_and_the_comparator_coupling_constant_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_dynamical_charges_on_the_pure_ring_photon_from_energies_2026_09_25.py
---

# Supplied single-link charge hopping: energy identities and finite estimator scan

**Type:** bounded_theorem
**Status:** conditional model identities and numerical diagnostics; unaudited.

## Setting

Supply H=-g sum R_p-t sum sigma_x+M sum Q_v², Q=div(sigma_z)/2 on a finite cubic torus, with g,t>=0 and the charge mass specified. At t=0 the restriction to the ice block recovers the ring Hamiltonian; the full Hilbert space also contains other charge blocks and its global ground need not be the ice ground. At t>0 the full-link flip graph is connected; the six-link control below instead uses its stated reachable component. None of these model clauses is a framework premise.

Nonpositive off-diagonal entries allow a nonnegative component ground vector. A positive guide gives an exact mixed-energy identity only for the correctly projected distribution, not at finite projection/population. The supplied guide exp(0.2 N_flip-gamma sum Q²+b dot sigma) uses externally tuned gamma=1.2,0.7,0.5,0.3 at t=0.25,0.5,0.75,1. Calibration is a supplied method choice, not an independently reproduced prediction. Each local difference stencil fixes its central gamma, but gamma changes between central hopping values.

## Conditional identities

For a differentiable ground branch, dE/dt=-sum <sigma_x> and dE/dM=sum <Q²>. Finite differences approximate these with truncation error; at crossings use one-sided slopes and the corresponding ground states. For lambda>0, E(lambda g,lambda t,lambda M)=lambda E(g,t,M). Euler's identity where differentiable yields u=(-E-t N_l <sigma_x>+M N_v <Q²>)/(g N_p), g>0.

The link double commutator is [sigma_z,[-t sigma_x,sigma_z]]=4t sigma_x; the diagonal charge term contributes zero. With g=1, the parent's cyclic complex transverse modes, centered real ground spectral measure and equal normalization give averaged m1=2u s²+2t <sigma_x>, s²=2-2cos k. For arbitrary g the ring term is2g u s². No spatial symmetry is required for the averaged double-commutator identity, but converting the runner's real-field energy curvature to the complex-mode m-1 additionally requires the parent symmetry and field-reversal hypotheses. For positive finite chi=2m-1 and nonzero coupled weight, omega_min<=2 sqrt((u s²+t <sigma_x>)/chi). A momentum-independent numerator does not establish a finite nonzero limit: chi(k) and the state also need control. This upper bound proves no gap and excludes no softer weak-weight mode.

## Estimator boundary

The full stated grid uses1920walkers, projection30 and3/4seeds, with finite t,M and probe-field stencils. All quoted errors are heuristic seed/bin scatter. Guide, finite-population/projection, initialization and truncation biases, and covariance from shared reference energies, are not bounded. A fixed guide does not remove a bias that changes with t or M. Changes in these estimates cannot locate a ground-state crossover, establish a size trend or identify a physical coupling. alpha_G is only the supplied comparator combination, not a model equivalence. Tables below preserve the author's run; fresh stdout is the reproduction record.

## Diagnostic 1 — exact control on 2³

With the single-link term on all 24 links the `2³` space has `2^24`
configurations, so the control puts the term on the six links at one vertex. Plaquette
flips and flips of those six links reach 184320 configurations from the ice
seed, and the ground state of that space is computed in floating-point arithmetic with and without
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

- **Pattern in the finite estimates.** On 6³ the steps of
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

The estimated bound `2 ((u s² + t ⟨σ^x⟩) / χ̄)^{1/2}` on the lowest transverse excitation
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


## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite Hamiltonian and stated grid.
- **N2:** independent review controls are distinct from primary reproduction.
- **N3:** clauses, guide and comparator remain supplied.
- **N4:** actual linked parent scope controls.
- **N5:** floating-point and finite stochastic evidence; heuristic errors.
- **N6:** guide/population/projection and finite-difference control remain open.
- **N7:** alternative guides, components and soft spectral weights remain possible.
- **N8:** no physical identification, new premise or audit verdict.

## Actual inputs

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [RING_MODEL_WINDING_SECTOR_ENERGIES_GIVE_AN_ELECTRIC_COUPLING_THAT_AGREES_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_ON_8_CUBED_AND_THE_COMPARATOR_COUPLING_CONSTANT_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_WINDING_SECTOR_ENERGIES_GIVE_AN_ELECTRIC_COUPLING_THAT_AGREES_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_ON_8_CUBED_AND_THE_COMPARATOR_COUPLING_CONSTANT_BOUNDED_THEOREM_NOTE_2026-09-25.md)
