# T28 pre-registration (written BEFORE running any script; Sonnet 5.5, same family as supervisor)

Wall: the gauge action and g_bare = 1 (beta = 6) are supplied.

## Prior art found before the test (so the test is not a repeat)
- archive/notes/docs/WILSON_TEMPORAL_KERNEL_CASIMIR_GENERATOR_BETA_GBARE_TRANSPORT_THEOREM_NOTE_2026-07-01.md
  proves only the beta -> infinity statement beta * g_{E,R}^2(beta) -> 2 N_c (K2, K3). Its Boundary (lines 187-189)
  disclaims finite-beta equalities. K4 says beta = 6 is "where the leading per-step generator is (1/2) Delta".
  Nobody has printed g_{E,R}^2(beta) AT beta = 6 for several R. That is the gap this test fills.
- docs/EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_...2026-06-08.md:52-55: the CLT limit is the heat semigroup with only
  the rate c free ("the g_bare=1/beta=6 scale (retained convention)").

## TEST A (main): is the operator-side "unit point" a property of the actual Wilson kernel at beta = 6?
Objects (July-1 note definitions): plane kernel W_beta(U) = exp[(beta/N) Re Tr U] on SU(N);
w_R(beta) = int W chi_R^* dU / d_R ; eps_R = -ln(w_R/w_0) ; g_{E,R}^2(beta) := 2 eps_R / C_2(R),
C_2 in the half-trace normalisation (SU(3): 4/3, 3, 10/3, 16/3, 6 for 3, 8, 6, 15, 10).
For the unit heat kernel exp(t Delta/2), t = 1, g_{E,R}^2 = 1 for every R exactly.
Also: beta_R := the beta solving g_{E,R}^2(beta) = 1.  Hessian law (09-02 note, W1): beta_H = 2 N_c = 6 exactly.

PASS reading (unit point is robust at the pin; Wilson and unit heat kernel agree well at beta = 6):
  for R in {3, 8, 6}: |g_{E,R}^2(6) - 1| <= 0.10 AND max(beta_R)/min(beta_R) <= 1.20.
FAIL reading (unit point is an asymptotic-jet statement, not a property of the beta = 6 kernel):
  any of the three has |g_{E,R}^2(6) - 1| > 0.10, OR beta_R spread > 1.20.
Sanity gate (code check): at beta = 96 the product beta * g_{E,3}^2 must be within 5% of 6 (July-1 K3).
My prior guess (recorded so it can be wrong): FAIL, with g_{E,3}^2(6) about 1.2 and R-dependence growing with C_2.

## TEST B (side, analytic + tiny numeric): does "electric coeff = magnetic coeff" (g = 1 in the 09-02 note's H_g family)
sit at Euclidean Wilson beta = 6 under the standard weak-coupling Kogut-Susskind dictionary?
Method: harmonic expansion of e*H_E + m*H_B with the note's operators (H_E = -Laplacian in half-trace metric,
H_B = sum_p (1 - Re Tr U_p / N)); derive the light-speed condition c^2 = e m / N; insert KS e = g^2/2, m = 2N/g^2;
find the g at which the note's member g'=1 sits.
PASS (supports "g'=1 <-> beta=6"): beta_eq within 10% of 6.  FAIL: otherwise. Prediction: beta_eq = sqrt(N) = 1.73.

## TEST C (side, route "induced action"): counting check
On a 3^4 periodic lattice with random SU(2) links, check that the plaquette part of tr D^4 (staggered hopping D) is
-8 Re Tr U_p per plaquette, so that ln det(1 + kappa D) contains +2 kappa^4 Re Tr U_p, i.e. beta_ind = N * N_f * kappa^4 / 2
per (rooted) flavour with kappa = 1/(2m). PASS = coefficient -8.0 +- 1e-9. Then state the mass at which beta_ind = 6
and compare with the hopping-expansion convergence radius (kappa < ~1/8).

## TEST D (tiny, added before running): can a lattice-native finite step supply the tick kernel?
Route "native finite step": the one-tick kernel is the uniform distribution on the lattice's own smallest rotations
(Lattice axiom: proper cubic rotations): the 6 quarter-turns (+-pi/2 about x, y, z), lifted to SU(2) (eigenphases +-pi/4).
Convolution eigenvalue on spin j: lambda_j = chi_j / (2j+1), chi_j = sin((2j+1) pi/4) / sin(pi/4).
PASS (usable tick kernel): all lambda_j >= 0 for j = 1/2..3 AND tau_j = 2(-ln lambda_j)/C_2(j) within 10% of 1 for j = 1/2 and 1.
FAIL: any lambda_j < 0 (not a positive kernel; RP fails), or tau outside 10%.
Prediction: FAIL (lambda_2 = -1/5).

## Extra checks added to Test A's run (arithmetic only, no new pass/fail)
- Hessian identity W1 by finite differences: -d^2/dx^2 ln K along exp(i x T_3) at 0 equals beta/(2 N_c).
- Agreement of w_3/w_0 at beta = 6 with the repo's <P>_W = 0.4225317396 (docs/ACTION_FORM_NO_GO_EQUIVALENCE_...:64).
- Sensitivity: (6/beta_R)^16 = factor by which v_cand (which goes as g^32) moves if g_bare^2 := 6/beta_R.

## Deviations recorded after running (honesty log)
- Test C: the first run used a 3^4 lattice and FAILED (fit slope -2.70, residual 3e2). Cause: odd L breaks the staggered
  phase sign (-1 per plaquette) across the periodic boundary. Re-run on 4^4 with the straight-line (Polyakov) loop as a
  second regressor: slope -8.000000000, Polyakov coefficient 2, residual 5e-8. Verdict PASS on the corrected lattice only.
- Test A: pre-registered rule was "FAIL if any criterion fails". Criterion 1 failed (max |g^2-1| = 0.292 > 0.10);
  criterion 2 passed (beta_R spread 1.052 <= 1.20). Reported as FAIL, with the nuance that the Wilson kernel at beta=6
  is nearly Casimir-scaling (R-spread of g_E^2 is 1.12-1.29): the error is in the VALUE (unit point 6.8-7.6), not the FORM.
- Test B: PASS/FAIL as predicted (beta_eq = sqrt(N) = 1.732). Test D: FAIL as predicted.
