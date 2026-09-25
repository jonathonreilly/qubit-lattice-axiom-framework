---
claim_id: gaussian_lattice_maxwell_comparator_gives_a_linear_size_independent_transverse_structure_factor_and_misses_the_pure_ring_level_step_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "In the supplied ring model (spin-1/2 link fields on the cubic L^3 torus, exact vertex Gauss law, H = -sum_p (U_p + U_p^dag) at V = 0, g = 1, transverse mode O_a(k) = N^{-1/2} sum_x e^{ikx} sigma(x,a), all supplied and none adopted), a supplied non-compact lattice Maxwell comparator H_G = (U/2) sum E_l^2 + (K/2) sum B_p^2 in its zero-winding ground state has (i) the exact equal-time covariance S_ab(k) = A |s(k)| (delta_ab - g_a g_b^*), A = sqrt(K/U)/2, s^2 = sum_a (2 - 2 cos k_a), dispersion omega = sqrt(UK) |s(k)|, hence on-axis S_T(k) = A |s(k)| with no dependence on L at fixed k (certified on 4^3 and 8^3 tori to 1e-9); (ii) the spin-1/2 sum rule gives N^{-1} sum_{k != 0} sum_lambda |O_lambda(k)|^2 = 3 exactly in the zero-winding sector and the per-flip identity |Delta O|^2 = (4/N) s^2 behind the f-sum <O^dag (H - E_0) O> = 2 u_0 s^2, so matching the f-sum fixes K = 4 u_0 and an ansatz c + A |s| with c >= 0 on every mode is bounded by A <= 3/(2 m_L) = 0.628, U >= 0.73; (iii) as a finite diagnostic, no size-independent c + A |s(k)| fits today's six pure-ring numbers (best chi^2/dof = 33.1/4, residuals up to 3.1 standard errors), the 6^3 -> 8^3 level step at k_min contradicts the 8^3 slope by 2.9 standard errors, and S_T(pi/2) grows from 4^3 to 8^3 by 2.7-3.4 standard errors where any Gaussian gives zero; (iv) the classical pinch-point constant of the landed calibration is 3N/(2N+1) = 1.4884, 1.4965, 1.4985 on 4^3, 6^3, 8^3; (v) 10^3 and 12^3 predictions for S_T(k_min) are 0.46/0.43 (linear photon), 0.575 (level residual), 0.375/0.263 (quadratic), separable at 3.8 and 4.9 standard errors with a 0.03 error. No phase, no physical photon, no bias in the Monte Carlo inputs and no value of U is claimed; every modelling choice is a recorded decision point and the numbers are supplied-model finite diagnostics with no physical reading."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_rk_photon_single_mode_bound_is_quadratic_with_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
  - uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
runner: scripts/gaussian_lattice_maxwell_comparator_linear_structure_factor_misses_the_pure_ring_level_step_2026_09_24.py
---

# A Gaussian lattice Maxwell comparator gives a linear, size-independent transverse structure factor and misses the pure-ring level step

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite certificates under supplied decision points; unaudited.

Everything below is a supplied model, a finite diagnostic, and carries no physical reading. The ring model, the Gaussian comparator and the Monte Carlo inputs are not derived from the repository axioms and nothing here is adopted.

## Result

- The non-compact lattice Maxwell theory on the L^3 torus, with the same exact vertex Gauss law and in the zero-winding sector, has the exact equal-time covariance S_ab(k) = A |s(k)| (delta_ab - g_a g_b^*), A = sqrt(K/U)/2, g_a = (1 - e^{-i k_a})/|s(k)|, s(k)^2 = sum_a (2 - 2 cos k_a), and dispersion omega(k) = sqrt(UK) |s(k)|. On an axis the two transverse polarisations are exactly the other two axes and S_T(k) = A |s(k)| = sqrt(K/U) |sin(k/2)|. Its finite-torus content is the discrete momentum set and the removal of k = 0; it has no dependence on L at fixed k (certified: S_T(pi/2) = 0.594089 on both 4^3 and 8^3 at U = 1.7, K = 1.2).
- The spin-1/2 sum rule sum_l sigma_l^2 = 3N, the Fourier Gauss law and the zero-winding sector give N^{-1} sum_{k != 0} sum_lambda |O_lambda(k)|^2 = 3 exactly for every state in the sector. Matching the exact f-sum <O^dag (H - E_0) O> = 2 u_0 s^2 (recovered below from the per-flip identity |Delta O|^2 = (4/N) s^2) to the Gaussian's K |s|^2 / 2 fixes K = 4 u_0, so the Gaussian has one free coupling U with S_T = sqrt(u_0/U) |s| and omega = 2 u_0 s^2 / S_T (the Feynman quotient is saturated). For the ansatz c + A |s(k)| on every transverse mode with c >= 0, the sum rule bounds A <= 3/(2 m_L) = 0.6302, 0.6286, 0.6284 (L = 4, 6, 8) and U >= 0.737, 0.731, 0.729.
- Finite diagnostic on today's certified pure-ring numbers (open PR 9161): no size-independent c + A |s(k)| fits the six numbers at k < pi (best c = 0.260 +- 0.048, A = 0.327 +- 0.037, chi^2/dof = 33.1/4, residuals up to +3.1 standard errors); the pure Gaussian c = 0 is worse (chi^2/dof = 62.8/5); the 8^3 zone alone is fitted exactly by c = 0.266 +- 0.066, A = 0.403 +- 0.060, but that slope predicts a fall of 0.095 from 6^3 to 8^3 at k_min where the inputs show -0.018 +- 0.036 (a 2.9 standard-error contradiction); and S_T(pi/2) grows from 4^3 to 8^3 by 3.35 (120 walkers) or 2.66 (240 walkers) standard errors, where any Gaussian gives zero difference.
- The classical pinch-point constant of the landed calibration K_cont = (2N+1)/(3N) is 1/K_cont = 3N/(2N+1) = 1.4884, 1.4965, 1.4985 on 4^3, 6^3, 8^3, against the uniform-ice inputs 1.51, 1.53, 1.50 and the limit 1.5.
- For the next run: at k_min a linear photon gives S_T = 0.46 (10^3) and 0.43 (12^3) from the six-number fit, 0.464 and 0.389 from the pure line through the 8^3 point; a level residual gives 0.575 at both; a quadratic fall gives 0.375 and 0.263; with a 0.03 error the level and the linear cases separate by 3.8 and 4.9 standard errors.

## Setting and decision points

The ring model is the one of open PRs 9066, 9072 and 9161: link fields sigma = +-1 on the positive-axis links of the cubic L^3 torus (N = L^3 vertices, 3N links), the exact vertex Gauss law "three in, three out" (lattice divergence zero), H = -sum_p (U_p + U_p^dag) at V = 0 and g = 1, energy per plaquette e_0 = -u_0 with u_0 = 0.2926, 0.2889, 0.2880 on 4^3, 6^3, 8^3 (inputs). The mode is O_a(k) = N^{-1/2} sum_x e^{i k x} sigma(x, a), k = 2 pi m / L along one axis, a a transverse axis; S_T(k) is the mean of <|O|^2> over the three axes and both transverse polarisations. The decision points are:

- **D-gauss** (comparator): the non-compact lattice Maxwell theory H_G = (U/2) sum_l E_l^2 + (K/2) sum_p B_p^2 with [A_l, E_l'] = i delta_ll', B = curl A, the same vertex Gauss law, and E in place of sigma in the mode.
- **D-wind** (sector): the three uniform fields E_a(k = 0) commute with H_G and are the conserved fluxes; they are set to zero, matching the zero-winding sector of the ring model.
- **D-fsum** (identification): K is fixed by matching the exact double commutator [O^dag, [H, O]] of the ring model to that of H_G, K = 4 u_0; U stays free.
- **D-ansatz** (fit family): S_lambda(k) = c + A |s(k)| on every transverse mode, c a k-independent short-range part, c >= 0 when the sum-rule bound is used.
- **D-inputs** (data): the certified numbers of open PR 9161 (guided projector Monte Carlo, 120 walkers, ten-bin errors), plus its auxiliary 240-walker 8^3 run, are inputs; their errors are treated as independent Gaussian standard errors in the weighted fits.
- **D-prec** (next run): a standard error of 0.03 on S_T(k_min) at 10^3 and 12^3 is assumed when separations are quoted.

None is adopted. Every result is "supplied model, finite diagnostic, no physical reading".

## Theorem 1 — the exact transverse structure factor of the Gaussian comparator on the torus

Let D (N x 3N) be the lattice divergence, div(x) = sum_a [E(x, a) - E(x - a, a)], and C (3N x 3N) the plaquette curl with circulation +E(x, a) + E(x + a, b) - E(x + b, a) - E(x, b) on the plaquette (x; a < b). Then:

1. D C^T = 0 (integer identity). The kernel of C^T C has dimension N + 2 (N - 1 gradients and 3 harmonic uniform 1-forms), so its range has dimension 2(N - 1) and is divergence free; the divergence-free space is that range plus the three uniform fields E_a(0).
2. The nonzero spectrum of C^T C is {|s(k)|^2 : k != 0}, each value twice; the normal modes of H_G on the divergence-free space are two transverse polarisations per k != 0 with omega(k) = sqrt(UK) |s(k)|, and the three k = 0 modes have no restoring term (they are the fluxes of D-wind).
3. In the sector E_a(0) = 0 the ground state is Gaussian with covariance Sigma_E = (1/2) sqrt(K/U) (C^T C)^{1/2}, whose Fourier transform S_ab(k) = N^{-1} sum_{x,y} e^{ik(x - y)} Sigma_E[(x,a),(y,b)] equals A |s(k)| (delta_ab - g_a g_b^*) with A = sqrt(K/U)/2 and g_a = (1 - e^{-i k_a})/|s(k)| for every k != 0, and S(0) = 0.
4. For k along an axis c the vector g has only its c component, so the transverse polarisations are exactly the two other axes, the axis component vanishes, the two polarisations are degenerate, and S_T(k) = A |s(k)| = sqrt(K/U) |sin(k/2)|; per mode this is omega(k)/(2U). The value at a given k is the same on every torus whose zone contains k.

*Proof.* (1) is the boundary-of-a-boundary identity, checked as an integer matrix product in the runner. Translation invariance block-diagonalises C^T C by Fourier transform; the Fourier Gauss law reads sum_a (1 - e^{i k_a}) O_a(k) = 0, so the constraint vector is g^* and the transverse subspace at k is the orthogonal complement of g; on it the lattice Laplacian C^dag C acts as |s(k)|^2, which gives (2). For H = (U/2) p^T p + (1/2) x^T M x with M = K C^T C restricted to the range of C^T, the ground-state momentum covariance is (1/2) (M/U)^{1/2}, which is (3); its Fourier transform is diagonal in k and, on the transverse subspace, equals A |s(k)| times the transverse projector 1 - g g^dag. (4) follows because 1 - e^{i k_a} = 0 for the two axes a transverse to k. The runner certifies each statement on the 4^3 and 8^3 tori: |D C^T| = 0, kernel dimensions 66 = 64 + 2 and 514 = 512 + 2, spectrum against {|s(k)|^2 x 2} to 1e-9, every column of Sigma_E divergence free to 1e-9, |S(k) - A |s| (1 - g g^dag)| below 1e-9 at all k != 0, S(0) below 1e-12, exact on-axis polarisations, trace Sigma_E = 2A sum_{k != 0} |s(k)|, and S_T(pi/2) = 0.594089 on both sizes at U = 1.7, K = 1.2. ∎

What the comparator can and cannot have on a finite torus: it has the discrete momentum set 2 pi m / L and the removal of k = 0 by the sector; it cannot have any dependence on L at fixed k != 0, any splitting of the two transverse polarisations, any anisotropy beyond the transverse projector, or any sector dependence beyond the three k = 0 modes.

## Theorem 2 — the spin-1/2 sum rule, the f-sum identification, and the bound it leaves a Gaussian fit

For every configuration sigma in {+-1}^{3N} obeying the vertex Gauss law:

1. sum_k sum_a |O_a(k)|^2 = 3N (Parseval with sigma_l^2 = 1).
2. sum_a (1 - e^{i k_a}) O_a(k) = 0 for every k, so the lattice-longitudinal component vanishes; for k on axis c, O_c(k e_c) = 0.
3. O_a(0) = Phi_a / L^{1/2} with Phi_a the plane flux, conserved by the Gauss law and zero in the zero-winding sector.
4. Hence in the zero-winding sector N^{-1} sum_{k != 0} sum_lambda |O_lambda(k)|^2 = 3 exactly, configuration by configuration and therefore for every state and every expectation in the sector.
5. Flipping a flippable plaquette in the (a, c) plane changes O_a(k e_c) by |Delta O|^2 = (4/N) s(k)^2; flipping any other plaquette leaves it unchanged. On the ice space this is the operator identity [O^dag, [H, O]] = (4/N) s^2 (-H_ac), H_ac the ring energy of the (a, c) plaquettes, and for a cubic-symmetric eigenstate with <-H_ac> = N u_0 it gives <O^dag (H - E_0) O> = (1/2) <[O^dag, [H, O]]> = 2 u_0 s^2, the sum rule of open PR 9161.
6. In the comparator, [O^dag, [H_G, O]] = K |s(k)|^2 per transverse mode, so D-fsum sets K = 4 u_0; then S_T(k) = sqrt(u_0/U) |s(k)|, omega(k) = 2 sqrt(u_0 U) |s(k)| = 2 u_0 s^2 / S_T(k), and the Feynman quotient is an equality.
7. Under D-ansatz with c >= 0, item 4 reads 2c (N - 1)/N + 2A m_L = 3 with m_L = N^{-1} sum_{k != 0} |s(k)|, so A <= 3/(2 m_L) and U = u_0/A^2 >= u_0 (2 m_L/3)^2.

*Proof.* Items 1-3 are Parseval, the Fourier transform of the divergence, and the plane-flux identity; item 4 combines them with item 2 (the longitudinal weight is zero, so the two transverse modes carry all of |O(k)|^2). Item 5: the two a-links of an (a, c) plaquette at x and x + c carry opposite signs on a flippable plaquette, so the flip changes O by 2 N^{-1/2} (e^{ikx} - e^{ik(x + c)}) up to sign, of modulus squared (4/N)|1 - e^{ik}|^2 = (4/N) s^2; an (a, b) plaquette with b transverse to k changes O by 2 N^{-1/2} e^{ikx} (1 - 1) = 0; a plaquette without a-links does not touch O. For a diagonal O the double commutator has matrix elements (O_i - O_j)^2 H_ij, which is the displayed identity; the half of it equals <O^dag (H - E_0) O> for an eigenstate with O(-k) = O(k)^dag and inversion symmetry. Item 6 is the double commutator [E_l', [H_G, E_l]] = K (C^T C)_{ll'} Fourier transformed on the transverse subspace. Item 7 is arithmetic. The runner certifies items 1-5 on 24 sampled zero-winding ice states of the 4^3 torus (400 plaquette flips apart; worst divergence 0, worst winding 0, all defects below 1e-10) and evaluates m_L = 2.3803, 2.3863, 2.3872, 2.3874, 2.3875 for L = 4, 6, 8, 10, 12 (2.3876 on 60^3), A_max = 0.6302, 0.6286, 0.6284, 0.6283, 0.6283, U_min = 0.737, 0.731, 0.729, 0.730, 0.730. ∎

## Diagnostic — fits to today's numbers and predictions for the next tori

Inputs (open PR 9161; ten-bin standard errors): S_T = 0.692 +- 0.013 (4^3, pi/2), 0.557 +- 0.022 (6^3, pi/3), 0.575 +- 0.028 (8^3, pi/4), 0.833 +- 0.040 (8^3, pi/2), 1.019 +- 0.085 (8^3, 3pi/4), 0.98 +- 0.05 (6^3, 2pi/3); zone edge 1.16 +- 0.03 (6^3, pi), 1.19 +- 0.04 (4^3, pi); auxiliary 240-walker 8^3 run 0.541 +- 0.027 (pi/4), 0.751 +- 0.018 (pi/2). The inputs' quotients 2 u_0 s^2 / S_T at k_min are reproduced as 1.691, 1.037, 0.587.

| fit (S_T = c + A|s|, no size dependence) | c | A | U = u_0/A^2 | chi^2/dof | residuals (standard errors, input order) |
|---|---|---|---|---|---|
| six numbers at k < pi | 0.260 +- 0.048 | 0.327 +- 0.037 | 2.70 | 33.1/4 | -2.3, -1.3, +2.3, +2.8, +1.8, +3.1 |
| all eight (with k = pi) | 0.046 +- 0.036 | 0.509 +- 0.026 | 1.11 | 81.3/6 | -5.7, +0.1, +5.0, +1.7, +0.4, +1.1, +3.2, +3.2 |
| 8^3 zone alone (three points) | 0.266 +- 0.066 | 0.403 +- 0.060 | 1.77 | 0.0/1 | +0.0, -0.1, +0.1 |
| pure Gaussian c = 0, six numbers | 0 | 0.522 +- 0.008 | 1.06 | 62.8/5 | -3.6, +1.6, +6.3, +2.4, +0.6, +1.5 |

Two size comparisons that any Gaussian fixes: (a) the level step, Delta S_T(6^3 -> 8^3) at k_min = -0.018 +- 0.036, would need A_level = -0.08 +- 0.15, against A = 0.40 +- 0.06 from the 8^3 zone (2.9 standard errors) or 0.33 +- 0.04 from the six numbers (2.6); (b) at fixed k = pi/2 the 8^3 value exceeds the 4^3 value by 3.35 (120 walkers) or 2.66 (240 walkers) standard errors, where the comparator gives zero; the two 8^3 runs differ by 1.87 (pi/2) and 0.87 (k_min) standard errors. A pure Gaussian fitted size by size to S_T(k_min) alone needs U = 1.22, 0.93, 0.51 on 4^3, 6^3, 8^3 where one number is required. The measured decay rate of the k_min mode per |s| falls with L, [0.99, 1.13], [0.80, 1.00], [0.65, 0.78], where the comparator has the single constant sqrt(UK).

| torus | \|s(k_min)\| | linear, six-number fit | linear, pure line through 8^3 | linear, sum-rule saturating (c = 0) | level residual | quadratic fall | level vs linear at 0.03 |
|---|---|---|---|---|---|---|---|
| 10^3 (k_min = pi/5) | 0.6180 | 0.462 | 0.464 | 0.388 | 0.575 | 0.375 | 3.8 standard errors |
| 12^3 (k_min = pi/6) | 0.5176 | 0.429 | 0.389 | 0.325 | 0.575 | 0.263 | 4.9 standard errors |

The Feynman quotient 2 u_0 s^2 / S_T at k_min would be 0.383 (level) or 0.477 (linear fit) on 10^3 and 0.268 or 0.360 on 12^3: with a residual constant the quotient falls quadratically at small k exactly as in the landed uniform-ice case, so the quotient's power alone does not separate a photon from a constant; the value of S_T(k_min) does.

Forward-walking factors (finite diagnostic only): with the open PR's forward-walking lags tau_f <= 4 and the measured k_min decay-rate windows, e^{-omega tau_f} lies in [1.7e-3, 3.7e-3] (4^3), [1.8e-2, 4.1e-2] (6^3) and [9.1e-2, 1.4e-1] (8^3); the two-mode factor e^{-2 omega tau_f} lies in [2.8e-6, 1.4e-5], [3.4e-4, 1.7e-3] and [8.2e-3, 1.8e-2]. A mixed-estimator residual of a diagonal observable that decays with the lowest coupled excitation would therefore grow with L at fixed tau_f, in the same direction as the observed growth; this is a testable hypothesis, not a finding.

## What this means for the lanes

- Photon lane (open PRs 9146, 9148, 9161): the Gaussian comparator is a sharp instrument. It fixes the whole transverse structure factor by one coupling U once K = 4 u_0 is matched to the exact f-sum, and it forbids two things the inputs show: a level S_T(k_min) between 6^3 and 8^3 and a growth of S_T at fixed k with L. The tensions are 2.6-3.4 standard errors, from ten-bin errors of a 120-walker projector run; they are not yet a finding about the pure-ring point.
- The fixed-k growth has three candidate readings, each with a test: a non-Gaussian finite-size effect (test: the 4^3 and 8^3 values at k = pi/2 stay apart when the forward-walking lag is doubled to tau_f = 8 and the walker count to 480); an estimator effect that grows with L (test: the 8^3 values move toward the 4^3 value under the same doubling, in the direction of the 240-walker run); a statistical fluctuation (test: independent seeds; a 2.7-3.4 standard-error effect recurring in two runs is unlikely under this reading).
- The next tori decide the small-k form: 0.43-0.46 (linear) against 0.575 (level) at 10^3 and 12^3 with a 0.03 error, before any statement about a photon is attempted.
- Uniform-ice reference: the landed calibration reproduces the 1.5 constant to within 0.03 of the inputs, so the uniform-ice control of the projector runs is consistent with the classical pinch-point value.

## What stays open

- The phase of the ring model at V = 0 and whether S_T(k) is linear, level or otherwise at small k.
- Whether the constant c = 0.26 of the fits is a short-range part of the ground state or an estimator effect of the inputs.
- The value of U, or any statement that a single U exists; the size-by-size values 1.22, 0.93, 0.51 exclude one Gaussian but do not point to another model.
- Off-axis momenta, the two polarisations separately, and the k = pi structure (1.16-1.19 against the pinch-point 1.5).
- The winding-sector dependence of the ring model's ground state beyond the zero sector assumed in D-wind.

## Prior art

Hermele, Fisher and Balents 2004 (an emergent U(1) gauge field with a linearly dispersing photon on the pyrochlore); Benton, Sikora and Shannon 2012 (suppressed pinch points in quantum spin ice, structure factor proportional to |k| at zero temperature); Feynman 1954 (the single-mode variational bound). Cited as prior art, not as premises; none of them is used to fix any number above.

## Checks

| check | result |
|---|---|
| Gaussian lattice Maxwell on 4^3 and 8^3: D C^T = 0, kernel dim N + 2 (66, 514), spectrum {\|s\|^2 x 2} to 1e-9, covariance = A\|s\|(1 - g g^dag) to 1e-9, S(0) = 0, on-axis polarisations, S_T(pi/2) = 0.594089 on both | PASS |
| spin-1/2 sum rule on 24 sampled zero-winding ice states (4^3): Parseval 3N, Fourier Gauss law, on-axis longitudinal zero, zone sum 3 exactly, per-flip (4/N) s^2, defects below 1e-10 | PASS |
| zone means m_L = 2.3803, 2.3863, 2.3872, 2.3874, 2.3875 (L = 4-12), 2.3876 (60^3); A_max = 0.630-0.628; U_min = 0.729-0.737 | PASS |
| weighted fits: six numbers chi^2/dof = 33.1/4 (c = 0.260 +- 0.048, A = 0.327 +- 0.037); pure Gaussian 62.8/5; 8^3 zone c = 0.266 +- 0.066, A = 0.403 +- 0.060; level step 2.9 (2.6) standard errors; input quotients 1.691, 1.037, 0.587 | PASS |
| pinch-point constant 3N/(2N+1) = 1.4884, 1.4965, 1.4985 vs 1.51, 1.53, 1.50; identity sum_{k != 0} P_zz = 2(N - 1)/3 to 1e-9 | PASS |
| 10^3, 12^3 predictions: linear 0.462/0.464 and 0.429/0.389, sum-rule saturating 0.388 and 0.325, level 0.575, quadratic 0.375 and 0.263; separation 3.8 and 4.9 standard errors at 0.03 | PASS |
| fixed k = pi/2 growth 3.35 and 2.66 standard errors; 120 vs 240 walkers 1.87 and 0.87; rate per \|s\| windows fall with L; forward-walking factors at tau_f = 4 | PASS |

Runner: `scripts/gaussian_lattice_maxwell_comparator_linear_structure_factor_misses_the_pure_ring_level_step_2026_09_24.py`, `TOTAL: PASS=7 FAIL=0`, about 10 s single-threaded, peak memory about 0.2 GB, `AUDIT_TIMEOUT_SEC = 600`, stdout under 6000 characters; cache `logs/runner-cache/gaussian_lattice_maxwell_comparator_linear_structure_factor_misses_the_pure_ring_level_step_2026_09_24.txt`.

## Independent check: none

The runner was written and run by the author in one session; no separate reviewer, audit or reproduction is claimed.

## What this does not do

- It does not place the ring model in a phase, does not claim a photon, a Coulomb phase, a crystal or a gap, and does not read any number physically.
- It does not adopt the Gaussian comparator, the f-sum identification K = 4 u_0, the fit family, or the zero-winding sector; each is a recorded decision point.
- It does not claim that the Monte Carlo inputs are biased: the forward-walking factors are a hypothesis with a stated test, and the tensions are 2.6-3.4 standard errors from ten-bin error estimates treated as independent.
- It does not determine U or K of any effective theory, does not fit off-axis modes, and does not extend the sum-rule bound beyond the ansatz c + A |s| with c >= 0.
- It does not add an axiom, an import, a comparator to the framework or a framing; literature appears as prior art only.
