---
claim_id: the_one_family_u1_anomaly_four_field_coefficient_in_admissible_backgrounds_at_wilson_mass_one_does_not_vanish_like_p_squared_bounded_theorem_note_2026-10-25
claim_type: bounded_theorem
claim_scope: "Pre-registered rerun of the single-mode test of the one-family 16's four-field coefficient c4 in the U(1)_Y covariant anomaly density of the Wilson-kernel overlap (r = 1, m0 = 1.0), with every background inside the Hernandez-Jansen-Luscher admissibility bound ||1 - U_p|| < 1/30 (supplied): eps = 0.01, 0.02, 0.03 (max plaquette deviation 0.0300), axis-restricted factorised single-mode backgrounds, L x T x L x T with L = 12, 16, 24 and T = 24, 32, exact block sign(H). Exact: block = full 4D density, symmetry-reduced block sums = full sums, C-evenness, evr = eigh (all < 1e-12). Finite diagnostics, pre-set criteria: the joint fit R16/eps^2 = c4 + c6 eps^2 is clean (residual <= 1.1e-3 |c4|; eps exponent 3.97-4.01); the doublet's intercept is 0.989 gamma_L. NOT met: the headline (c4 vanishing like p^2 with T-agreement) and the copied P5, P5'. At L = 24, c4 = +1.13e-4, +6.7e-5, -3.60e-4 at |p_hat| = 0.26, 0.52, 0.77 (T = 32; T = 24 within 8%), so it changes sign and does not fall like p^2; the pooled intercept is +5.4e-4. Not covered: the measure, non-abelian locality, the gauge-field integral, non-axis backgrounds, L > 24, momenta below |p_hat| = 0.26."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_one_family_u1_anomaly_at_wilson_mass_one_passes_luschers_kernel_locality_tests_but_its_small_momentum_four_field_coefficient_does_not_visibly_vanish_bounded_theorem_note_2026-10-25
  - the_one_family_u1_anomaly_passes_luschers_zero_momentum_tests_on_lattices_to_24_but_its_momentum_space_locality_test_is_scale_limited_at_m0_1p6_bounded_theorem_note_2026-10-24
runner: scripts/the_one_family_u1_anomaly_four_field_coefficient_in_admissible_backgrounds_at_wilson_mass_one_does_not_vanish_like_p_squared_2026_10_25.py
---

# The one-family U(1) anomaly's four-field coefficient in admissible backgrounds at Wilson mass 1 does not vanish like p^2

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [S] reading.

Runner facts:
- runner.py gives TOTAL: PASS=11 FAIL=0 in 6 s on the laptop, with 3.6 k characters of stdout.
- It is seeded, declares AUDIT_TIMEOUT_SEC = 120 and reads no data files: the Mac-mini results (243 jobs) are an embedded JSON literal.
- It was tested under a unique filename in the agent folder (exit 0).
- Each pre-set criterion prints MET or NOT MET. A PASS line certifies only that the recorded verdict reproduces from the data, so a PASS line can carry NOT MET.

Axioms unchanged; no rule proposed; no CL edit.

## Pre-registration

- criteria_pre_run.txt was written before any computation of this probe. The only things run first were timing benchmarks on random matrices.
- It discloses that luscher-m0-1's eps = 0.3/0.15 numbers had been seen.
- Admissibility bound, as supplied: Hernandez, Jansen, Luscher, Nucl. Phys. B552 (1999) 363 prove overlap locality when every plaquette has ||1 - U_p|| < eps_adm with eps_adm < 1/30. Luscher, Nucl. Phys. B549 (1999) 295 builds the abelian anomaly-current locality on this class.
- For U(1), ||1 - U_p|| = 2|sin(F_p/2)| and max|Y| = 1, so the bound requires eps < 0.03334. The chosen values are eps = 0.01, 0.02, 0.03. G1 checks every job: the largest deviation is 0.03000 < 0.03333.
- One cost addendum (15:25, before any observable): one real L = 24 block takes 8.3 s, so all tiers were kept and no threshold changed.
- Mini run: 4 single-thread workers at nice 10, about 6.2 h wall. It ran longer than projected because another user's load on the mini reached 50-200.

## Set-up

- The machinery is luscher-m0-1's (block construction unchanged), with three declared changes. Each is verified live (G0a, G0b).
  - (a) The background is th(x) = eps sin(p(x - 1/2)) / (2 sin(p/2)). This is luscher-m0-1's antiderivative minus the constant eps/2: the plaquettes are identical and only the holonomy constant changes. The odd profile makes the pi rotations in the (1,2) and (3,4) planes, and on the diagonal the (13)(24) swap, exact block symmetries. That gives a 4-8x reduction; reduced = full to 3e-14.
  - (b) q_Y[th] = q_1[Y th] (exact) together with C-evenness (8e-16). These build all five species from unit-charge runs at 9 amplitudes.
  - (c) The eigensolver is scipy evr (= numpy eigh to 2e-14). On the mini, the full 576-block numpy sum equals the reduced evr sum to 5e-15 on 12 x 24 x 12 x 24.
- The order-eps^2 density cancels exactly in R16 = sum m Y^3 r(|Y| eps). c4 comes from the joint fit R16/eps^2 = c4 + c6 eps^2 over the three eps (one dof).

## Results against the pre-set criteria

| criterion | outcome | numbers |
|---|---|---|
| G0 exactness (a, b, c) | MET (PASS) | 4D 5e-15, GW 2e-15, reduced 3e-14, C 8e-16; laptop = mini 6e-11 |
| G1 admissibility < 1/30 | MET | max 0.03000 over 243 jobs |
| N joint-fit residual <= 5% abs(c4) | MET | max 1.1e-3 |
| A HEADLINE: c4 one sign, abs(p)-exponent >= 1.8 at T = 24 and 32, T-agreement 10% | NOT MET | c4 (T32) +1.127e-4, +6.72e-5, -3.599e-4; exponent 0.87 (T32), 0.95 (T24) with a sign change; T24/T32 differ 7.9%, 1.5%, 0.05% (T part met) |
| P5' L = 24 T = 32 one sign, exponent >= 1.8 | NOT MET | as above |
| P5 pooled intercept small; L16 diagonal exponent in [1.6, 2.4] | NOT MET | intercept +5.4e-4 (limits 1.3e-4, 7.5e-5); c4(16,1,1) +1.37e-4 and c4(16,2,2) -3.60e-4 have opposite signs |
| P5b eps exponent within 0.3 of 4 | MET | 3.971, 3.993, 4.003, 4.014 |
| D doublet intercept within 3% of gamma_L | MET | 0.9893 |

Reported, no criterion:
- Diagonal c4 at T = 24, in order of increasing s:

  | s | L | c4 |
  |---|---|---|
  | 0.038 | 16 | +1.37e-4 |
  | 0.067 | 12 | +5.5e-5 |
  | 0.146 | 16 | -3.60e-4 |
  | 0.25 | 12 | -8.7e-4 |
  | 0.31 | 16 | -1.07e-3 |
  | 0.5 | 12, 16 | -1.51e-3 |

- Admissible c4 against luscher-m0-1's eps = 0.3/0.15 split: (24,1) 1.13e-4 vs 1.42e-4; (16,1) 1.37e-4 vs 1.28e-4; (12,1) 5.5e-5 vs 4.8e-5; (16,2) -3.60e-4 vs -3.6e-4. The above-bound split was therefore qualitatively right; its L = 24 value carried a T = 16 / higher-order bias of about 25%.
- K3: the unit-charge 9-amplitude fit gives sum m Y^5 r4 = c4 to 1.6e-3.
- H1 [F, post-hoc]: at fixed momentum, c4 is L-converged at s = 0.146 (L16 -3.6018e-4 vs L24 -3.6012e-4). It is not converged at s = 0.067 (L12 +5.5e-5 vs L24 +6.6e-5, 20%).

## Answer

- Inside Luscher's admissibility bound, with three eps, clean eps^4 scaling and T-convergence (T = 24 vs 32 within 8%), the 16's four-field coefficient does NOT vanish like p^2 on the three smallest L = 24 momenta.
  - It changes sign between |p_hat| = 0.52 and 0.77.
  - At |p_hat| = 0.26 it stays at +1.1e-4, about 0.9% of abs(gamma_L).
- This removes luscher-m0-1's caveats (i) admissibility, (ii) T = 16 at L = 24 and (iii) the two-eps split. Its NOT MET finding stands.
- [S] Remaining readings, from luscher-m0-1:
  - (a) A turnover below |p_hat| = 0.26. A sign change already sits near s ~ 0.1, and c4 would need a second zero or a curve to 0 below s = 0.017.
  - (b) A finite-L effect at small momentum. H1 shows a 20% L-dependence at s = 0.067 while s = 0.146 is converged, so this reading is live.
  - (c) A genuine non-local piece. Supplied perturbative locality argues against (c).
  - The next discriminating test is c4 at fixed s = 0.017 and 0.038 on L = 32 and 48, at T >= 24, inside the bound. The symmetry reduction makes L = 32 at T = 24 about 91 blocks of dim 4096 per amplitude.

## Smuggling review

- Supplied:
  - U(1)_Y and the 16's hypercharges (test inputs);
  - the kernel and m0 = 1.0 (kernel parameters);
  - the HJL/Luscher admissibility bound and theorems;
  - the eps values, T and the criteria (pre-set).
- Forced:
  - GW, sum m Y^3 = 0 (the exact order-eps^2 cancellation), C-evenness, the block symmetries, and the eps^4 leading order (P5b).
- Post-hoc (labelled): H1 and the [S] readings.
- Gate: N/A (no rule).
- Route A's U(1) locality premise for the 16's four-field term is still NOT supported by measurement at L <= 24.

Uses: luscher-m0-1 (machinery, criteria P5/P5'/P5b, c4 split), luscher-L8 (Polyakov-loop fix).
Narrows: luscher-m0-1's caveat that the eps = 0.3 backgrounds lie above the admissibility bound. The c4 plateau persists inside the bound.
Caveats: U(1) only; finite lattices (L <= 24, T <= 32); axis-restricted backgrounds; not the non-abelian measure; not the gauge-field integral.
