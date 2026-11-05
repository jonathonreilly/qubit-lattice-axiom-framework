---
claim_id: curvature_squared_inflation_misses_the_act_tilt_and_no_rule_lifts_it_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For supplied single-field slow-roll models with second-order Hubble-flow tilts, exponential plateaus give n_s = 1 - 2/N for every steepness and power plateaus 1 - c phi^-k give 1 - 2(k+1)/((k+2)N); supplied curvature-squared inflation with the rules' colour-anomaly reheating gives n_s = 0.9617, estimated at -0.8, -4.1 and -4.5 sigma against Planck, ACT and DR2, and none of the rules' own terms estimated here shifts n_s by more than about 1e-10; no inflaton is derived."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/curvature_squared_inflation_misses_the_act_tilt_and_no_rule_lifts_it_2026_10_21.py
---

# Curvature-squared inflation misses the ACT tilt, and no rule lifts it

Claim type: bounded_theorem.
Primary runner: `scripts/curvature_squared_inflation_misses_the_act_tilt_and_no_rule_lifts_it_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight and supplies no field that rolls. Its tilt entry records that a supplied curvature-squared term would give n_s = 0.962. This note compares that and the other campaign readings with ACT and DR2 as well as Planck, and asks whether anything in the rules can lift the tilt. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose no inflaton.

## Statement

1. A phase of constant w from rho_end to rho_rh adds dN = (3w - 1) ln(rho_end/rho_rh)/(12(1 + w)) e-folds and boosts the gravitational-wave background of the modes entering during it by E, with ln E = 4 dN for every w.
2. At leading order in 1/N, V = 1 - c e^(-kappa phi) gives n_s = 1 - 2/N for every kappa, and V = 1 - c phi^-k gives n_s = 1 - 2(k+1)/((k+2)N).
3. With V = M^2 v(phi), eps, eta, n_s and r are M-free, so in pure curvature-squared inflation n_s depends on N* alone and no curvature-squared-type term can lift it.
4. Supplied curvature-squared inflation with the rules' colour-anomaly reheating gives N* = 50.3 and n_s = 0.9617. Against measurement this is estimated at -0.8 sigma (Planck), -4.1 sigma (ACT) and -4.5 sigma (DR2). None of the rules' own terms estimated here moves n_s by the +0.012 needed.

## Derivation

The stiff-phase relation follows from matching e-folds at the pivot k = 0.05/Mpc with rho scaling as a^(-3(1+w)) during the phase; the gravitational-wave boost follows from the same scaling of the modes entering during it. For the plateau families the slow-roll integrals give N in terms of phi at leading order, and substituting into n_s - 1 = 2 eta - 6 eps gives the two closed forms. ACT therefore asks for a power-law plateau with k = 0.88 at N* = 50.3 or 1.63 at N* = 55.7, while Planck was met by k of about 43, effectively exponential.

The runner's background solver and second-order Hubble-flow code reproduce 0.96489 at N* = 55. The N* that gives each measured n_s is 55.02, 74.84 and 78.55 for Planck, ACT and DR2 (leading order 57.0, 76.9, 80.6), with r = 0.0035, 0.0020 and 0.0018 there. Instant reheating gives N* = 55.7 and n_s = 0.9653; plain curvature-squared inflation reheats through its quadratic minimum (w = 0), so instant is its ceiling.

The rules' own forms:
- The hinge-sum plateau has eps_H = 3(1+w)(pi rho*/rho)^2 and n_s - 1 = -6(1+w). It needs w = -0.99415, -0.99567 or -0.99587, a fluid no rule supplies, and its tensor amplitude is at least 0.41, so it is excluded on every dataset regardless of n_s.
- A running coupling with n_s - 1 = gamma/N needs 57.0, 76.9 or 80.6 e-folds to the pole; on the ladder length L* = 133.28 the needed |gamma| is 4.68, 3.47 or 3.31, and gamma is supplied.
- A constant transfer per split gives n_s = 1 - q/(2N_e) with r = 8/N_e; ACT with q = 4 needs N_e = 76.9 and r = 0.104. Its Jordan-frame reading is curvature-squared inflation.
- A lattice curvature-squared remainder changes the coefficient c = 5.7e8 by about 2e-10 and n_s not at all (item 3).
- Hinge corrections to the Friedmann law have rho/rho* <= 7.2e-11, so |dn_s| is about 1e-10 at most.
- A cell-scale cubic curvature term with an O(1) coefficient gives lambda = 2.3e-18, against the needed -1.8e-4.
- Promoting the copy mass to a field puts it in the natural-inflation class, which never reaches 1 - 2/N at r < 0.036.

## Checks

The runner ends with `TOTAL: PASS=16 FAIL=0`. Among its lines:

- `[PASS] B1 N* that gives each n_s (2nd-order flow): Planck 55.02, ACT 74.84, DR2 78.55 (leading 2/(1-n_s): 57.0, 76.9, 80.6); r there 0.0035, 0.0020, 0.0018`.
- `[PASS] B2 reheating histories (e-fold matching at k = 0.05/Mpc): colour-anomaly decay (w = 0, T_rh = 1.5e+08 GeV) N* = 50.3, n_s = 0.9617 [Pl-0.8 ACT-4.1 DR2-4.5]; instant N* = 55.7, n_s = 0.9653 [Pl+0.1 ACT-2.9 DR2-3.3]`.
- `[PASS] B3 THEOREM (sympy): a phase of constant w from rho_end to rho_rh adds dN = (3w-1) ln(rho_end/rho_rh)/(12(1+w)) e-folds and boosts the GW background ... with ln E = 4 dN for every w`; kination to BBN gives N* = 69.6 and n_s = 0.9721.
- `[PASS] B4 ESTIMATE: ... caps any stiff phase at dN <= 6.6: N* <= 62.4, n_s <= 0.9689 [Pl+1.0 ACT-1.7 DR2-2.1]; ACT needs dN = 19.1, a GW boost e^77`.
- `[PASS] C1 hinge plateau ...: needs w = -0.99415 (Planck), -0.99567 (ACT), -0.99587 (DR2), a fluid no rule supplies; P_t >= 4/pi^2 = 0.41`.
- `[PASS] C2 N to the pole needed: 57.0 (Planck), 76.9 (ACT), 80.6 (DR2); on the ladder (N >= L* = 133.28) |gamma| = 4.68, 3.47, 3.31`.
- `[PASS] C3 constant transfer per split ...: ACT with q = 4 needs N_e = 76.9, r = 0.104 (excluded); r < 0.036 needs N_e > 222 and q = 11.6`.
- `[PASS] C4 legacy graph-growth notes on main ...: n_s = 1 - 2/N_e at N_e = 60 is 0.9667 [Pl+0.4 ACT-2.4 DR2-2.8]`.
- `[PASS] D1 THEOREM (leading order in 1/N, sympy): V = 1 - c e^(-kappa phi) gives n_s = 1 - 2/N for every kappa ...; V = 1 - c phi^-k gives n_s = 1 - 2(k+1)/((k+2)N)`.
- `[PASS] D2 at r < 0.036 the exponential plateaus (E/T alpha-attractors, any alpha) and natural inflation stay > 2 sigma below ACT at N* <= 55.7`, while power plateaus with k = 1, 2 and curvature-squared plus a cubic term reach it.
- `[PASS] E1 THEOREM: V = M^2 v(phi) makes eps, eta, n_s and r M-free ...: no R^2-type term can lift the tilt`.
- `[PASS] E2 ESTIMATE hinge Friedmann law ...: |dn_s| <~ 2 rho/rho* = 1e-10 vs the needed +0.012`.
- `[PASS] E3 cubic: a cell-scale c3 R^3 with c3 = O(1) a^4 gives lam = 72 M^4 c3 = 2.3e-18 c3 vs the needed -1.8e-04`; a loop of any field heavy enough to act locally gives |lambda| <= 4e-15 (estimate).
- `[PASS] E4 copy-mass promotion is the natural-inflation class ...: it never reaches 1 - 2/N at r < 0.036`; the SU(2) condensate hilltop would sit 5e11 times above the tensor bound.
- `[PASS] F1 11 campaign readings (all with a supplied piece) within 2 sigma: Planck 6, ACT 1, DR2 0 vs 4.6, 3.3, 3.3 by chance`.
- `[PASS] F2 shape grid (76 points, N* = 55.7): 32% fit ACT at 2 sigma with r < 0.036, 55% fit Planck; every fit spends >= 1 supplied shape parameter`.

## Estimates against measurement

All pulls are estimates. The Planck and ACT n_s values differ by 0.0091, about 1.8 sigma, a lower bound on their tension since P-ACT-LB includes Planck data; all three values are reported and no candidate was tuned to any one. Supplied curvature-squared inflation plus any post-inflation history allowed by the BBN bound on extra radiation stays at least 1.7 sigma below ACT, and 4.1 sigma below with the rules' own reheating. The legacy main-branch claim that n_s = 1 - 2/N_e at N_e = 60 matches Planck within 0.4 sigma is narrowed: it is -2.4 sigma against ACT. Meeting ACT needs a second supplied deformation (a power-law plateau with k of about 1 to 2, or a cubic curvature coefficient of about -1.2e-4 to -1.9e-4) or about 19 extra e-folds, which the BBN bound excludes. Because fits on the shape grid are common and each spends a supplied parameter, a fit is not evidence.

## Boundary

Supplied: the curvature-squared and cubic coefficients and the shape families; the pivot, g*, the colour running and top mass used for reheating; the gravitational-wave transfer prefactors, the BBN limit and a heat-kernel coefficient bound of 1e-2; the running-tilt constant C = 4.891 and the one-loop beta coefficients; and the measured n_s, r and A_s. Earlier campaign results on the inflaton background, the running tilt and the split schedule are cited, not rerun. No inflaton and no tilt are derived.
