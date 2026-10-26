---
claim_id: d4_route_predictions_under_finite_rung_zoom_matter_liv_falls_sixteenfold_per_rung_bounded_theorem_note_2026-10-26
claim_type: bounded_theorem
claim_scope: "D4 event set, root slicing, free supplied models: matter = factor-2 D4 zoom of the nearest-neighbour (NN) Wilson start with n finite rungs (rules 2-3), Borici slab (rule 5); links = NN triangle plaquettes, not zoomed (rule 7); graviton = d4-gravity hinge sum with the metric-only reading (rules 8-9). E* = hbar c/a, a = 2L, L = sqrt(8 pi) l_P (E* = 1.2177e18 GeV). (T) On shell p^2 = kappa J6 + O(p^8) with kappa = 1/540 (scalar), 1/90 (fermion), exact; photon 1/1440 (numerical, 1e-5); in the root slicing E = k(1 + beta (ka)^4), beta(n) = -2 kappa J6(i t + n). (T+F) Blocking keeps poles, so the rung-n light band is E_n(k) = 2^n E_0(k/2^n) (checked to 8e-12 for n <= 3) and beta_e(n) = beta_e(0)/16^n: body -0.1185, -7.41e-3, -4.63e-4, -2.89e-5 for n = 0..3; the exact fixed point has |beta| < 1e-8 (lowest band = |k| to 2e-11), i.e. it is exactly relativistic and only the finite-rung residual remains. The Borici residual mass adds anisotropy only at order mu^2. b_e/b_gamma = 16^(1-n). (E) gamma -> e+e- (1.9e20 eV at n = 0) is closed for every n >= 1; e -> e gamma is closed at n <= 1 and opens at 2.9e20 (n = 2) to 2.8e20 eV (n >= 3 and the fixed point); the nuclear wall moves from 9.7e20 to 1.53e21 A eV (composite flow to the link value, n >= 1); time of flight unmeasurable (E_QG,4 >= 1.75e18 GeV). Reconciled: graviton splitting at 100 Hz = 3.85e-80 (1e-62 is an eV/GeV slip; 1e-80 used a = L); cubic gamma -> e+e- threshold k_th(S) = (144(4S-1)/(3S-1)^2)^(1/4) sqrt(m_e E*) = 80.4 PeV on the axes (retired with the cubic rules); nucleon lifetime: 5.3e42 yr is the cubic worst case, 1.1e46 yr the cubic central nubar K+ value only; on the D4 map 2.5e41 yr (worst) to 6.5e43 yr (shortest central). The slab depth is not spectrum-inert: m_res < m_e needs Ls >= 46."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/d4_route_predictions_under_finite_rung_zoom_matter_liv_falls_sixteenfold_per_rung_2026_10_26.py
---

# D4 route predictions under the proposed rules: the matter LIV falls sixteenfold per zoom rung, so the electron/photon ratio is 16^(1-n)

Runner: runner.py. TOTAL: PASS=11 FAIL=0 in 6.5 s, 142 MB peak, seeded, AUDIT_TIMEOUT_SEC = 120, 3.3 k characters.
Re-run under a unique filename (scratchpad copy): identical output apart from the runtime line.
Pre-registration: criteria_pre_run.txt, written before any computation in this folder.
Labels: [T] exact, [F] finite diagnostic in a supplied free model, [E] estimate against measurement, [S] reading.
Axioms unchanged. No CL edit. Nothing adopted.

Deviations from pre-registration, stated:
- C3 FAILED on the first run because my code added a 1e-9 momentum offset (to dodge a zero that cannot occur at k != 0);
  that offset alone produced |E/k - 1| = 4e-9. Removed; the bar |E/k - 1| < 1e-7 passes at 1.9e-11. The "far below
  beta_3" clause was made explicit as |beta_inf| < 1e-2 |beta_3| (observed 1e-8 vs 2.9e-5).
- C4 passed its bar (5.7e-7 < 1e-6), but the hypothesis "no LIV" is only true to order mu^2: the anisotropy scales
  as mu^2 (ratio 4.01 on halving mu). Reported as found.
- Added C9 (slab depth), not pre-registered.

## Builds on, uses, contradicts
- d4-time-blind-events (#10094): J6 pattern, root slicing, kappa ratios 1 : 6 : 3/8, threshold kinematics. Its n = 0
  numbers are REPRODUCED (1.91e20 eV; 9.9e20 A eV with the face coefficient, 9.7e20 with the body one). Its graviton
  "(E_GW/E*)^2 ~ 1e-62" is CONTRADICTED (unit slip, below).
- d4-zoom-fixed-point-fermion (#10098): G_rung, the blocking kernel and the fixed point are reused. Its 1g band test
  is extended to a dim-8 bound, and its 2d rung construction is read as rule 3's finite-rung weight.
- d4-zoom-chirality (#10099): the Borici identity D_eff = tau alpha (D* + mu) is reused for C4 and C9. Its
  "alpha, Ls inert for the spectrum" is NARROWED: Ls sets m_res (C9).
- d4-gravity (#10100): the A law (1/6, 1/8, 0) is reused; its 1e-80 used a = L, corrected to a = 2L.
- liv-surviving-observables, assumed-inputs-model, nuclear-vacuum-breakup: cubic coefficients c_g = -S/24 and
  c_q = -S/6 + 1/24 (S = sum n^4), the parent wall formula, and the exact two-body photon-decay form. Reused.
- proton-theta: lifetime formula and channel inputs. Reproduced and re-mapped.
- RULESET.md inconsistencies a, c, d, e are resolved below. b, f, g and h are untouched.

## Theorems and exact facts
- [T] C1. sympy, mod the ideal (p^2):
  - The scalar sum (1 - cos r.p) has degree-2 part 6p^2 and a degree-4 part divisible by p^2. Its degree-6 part is
    -6 J6/540 mod p^2.
  - The naive/Wilson vector s^2 has 144 p^2, a degree-4 part divisible by p^2, and degree 6 -144 J6/90 mod p^2.
  - Hence on shell p^2 = kappa J6 + O(p^8) with kappa = 1/540 and 1/90. The Wilson term enters at O(p^12) on the
    light branch.
  - The photon (triangle kernel with the 8 heavy link modes integrated out) gives kappa*1440 = 0.99999.
  - With p = iE t + k: E = k(1 + beta (ka)^4), beta(n) = -2 kappa J6(i t + n), with a = site = slice spacing.
    The direct root-slicing scalar solve agrees to 2e-4 (face, body). The value is 0 on the slice cube axes.
- [T] C2. A zoom rung is a positive sum of fine propagators at Q = (P + l)/2 plus a contact term, so every fine pole
  survives, and the light pole maps as E_coarse(P) = 2 E_fine(P/2). By induction E_n(k) = 2^n E_0(k/2^n), and so
  beta_n = beta_0/16^n EXACTLY.
  - [F] Slice-correlator poles of G_rung vs Newton poles of the NN start: rel 8e-12 (n = 0..3, body).
  - [F] Fitted beta_n 16^n/beta_0 = 1.005, 1.006, 1.006 (k^8 contamination at ka <= .35).
  - [F] NN beta_0 (body) = -0.11852 = 6 x scalar.
- [T] The fixed point is the n -> infinity limit. The #10098 residue formula gives poles E_K = |k + K| exactly, so the
  lowest band is the continuum cone at every order: the exact fixed-point fermion is exactly relativistic.
  - [F] C3: |E/k - 1| <= 1.9e-11 (face, body; k = .25, .5), so |beta_inf| < 1e-8.
  - Convergence is geometric, with ratio 1/16 per rung. Only the finite-rung residual remains.
- [F] C4. Borici slab: D_eff = tau alpha (D* + mu).
  - E^2 - k^2 of (D* + mu)^-1 is constant to 6.5e-7 at mu = 0.2.
  - The anisotropy at k = .5 is 5.7e-7 (mu .2) and 1.4e-7 (mu .1), i.e. order mu^2.
  - Physically mu ~ m a <= 4e-22, so the slab's LIV is < 1e-48. Negligible.

## Predictions (body ray = largest |beta|; all species keep the one J6 sky pattern, zero on the slice cube axes)
Per-rung numbers [E], from the runner:

| rung n | |b_e| (ka)^4 | b_e/b_gamma | gamma -> e+e- | e -> e gamma | nuclear wall, flow (frozen) | E_QG,4 (e) |
|---|---|---|---|---|---|---|
| 0 (NN) | 0.1185 | 16 | 1.91e20 eV | closed | 9.7e20 (9.7e20) A eV | 1.75e18 GeV |
| 1 | 7.41e-3 | 1 | closed | closed | 1.53e21 (1.53e21) | 3.49e18 |
| 2 | 4.63e-4 | 1/16 | closed | 2.88e20 eV | 1.53e21 (2.44e21) | 6.98e18 |
| 3 | 2.89e-5 | 1/256 | closed | 2.80e20 eV | 1.53e21 (3.87e21) | 1.40e19 |
| fixed point | < 1e-8 | 0 | closed | 2.79e20 eV | 1.53e21 (stable) | infinite |

Notes on the table:
- Photon: b_gamma = -7.41e-3 (body), -6.25e-3 (face), UNCHANGED, because links are not zoomed. E_QG,4 = 3.49e18 GeV.
- Graviton: the leading term is dim 6, pure birefringence, c = 1 +- A(n)(E/E*)^2 with A = 1/6 (axis), 1/8 (face),
  0 (body). The polarisation average is 0, so there is no time-of-flight shift. The splitting at 100 Hz is 3.85e-80.
- Nuclear wall:
  - "flow" assumes the composite reading (momentum flows to the most subluminal constituent, which is the gluon link
    for n >= 1): beta_N = max(beta_q, beta_link).
  - "frozen" treats the nucleon as one elementary fermion.
  - Both use the parent formula P/A = (m_p^2 E*^4/(20|beta|))^(1/6).
- e -> e gamma opens because the matter weight is zoomed and the links are not, so for n >= 2 the electron is faster
  than the photon.
  - No electron near 3e20 eV is observable, so nothing measured is crossed.
  - The same asymmetry makes a nucleon at n >= 2 marginally faster or slower than the photon, through the composite
    residual. p -> p gamma is NOT computed here (open).
- Time of flight is unmeasurable for every species: E_QG,4 >= 1.75e18 GeV.

Verdicts:

| Prediction | Old | Rules as proposed | Verdict |
|---|---|---|---|
| fermion dim-8 | b_e = 6 b_scalar, fixed | b_e(0)/16^n; 0 at the fixed point | CHANGED |
| photon dim-8 | -7.41e-3 J6 pattern | same | UNCHANGED |
| graviton dim-6 | 1e-62 / 1e-80 | 3.85e-80 at 100 Hz (law unchanged) | CHANGED (size) |
| e/gamma ratio | 16 | 16^(1-n): 1, 1/16, 1/256, 0 | CHANGED |
| gamma -> e+e- | 1.9e20 eV | closed for n >= 1 | RETRACTED (n >= 1) |
| e -> e gamma | closed | opens 2.8-2.9e20 eV for n >= 2 | CHANGED (new channel) |
| nuclear walls | ~1e21 A eV | 1.53e21 A eV (flow); <= 3.9e21 frozen | CHANGED (x1.6) |
| time of flight | none | none (E_QG,4 >= 1.75e18 GeV) | UNCHANGED |
| cubic gamma -> e+e- | 78-160 PeV | 80.4 PeV axis (cubic rules only) | RETRACTED on D4 |
| nucleon lifetime | 5e42 / 1e46 yr | D4 map: >= 2.5e41 yr (worst), 6.5e43 yr (central) | CHANGED |
| slab depth | "inert" | Ls >= 46 (m_e), >= 58 (0.45 eV) | new |

If the link weight is also zoomed by n rungs (the open "perfect link weight"): b_e/b_gamma = 16 at every n, and every
n = 0 threshold scales by 16^(n/6). [S, not run.]

## Reconciliations (flags a, c, d, e)
- a. The headline numbers ARE the rung-0 values of rule 3. Under rules 2-3 they hold only if the rung count is 0.
  For n >= 1 see the table. The one-rung case is degenerate (b_e = b_gamma exactly).
- e. Graviton dim-6 at 100 Hz. The correct value is 2A (E/E*)^2 = (1/3)(4.14e-13 eV / 1.218e27 eV)^2 = 3.85e-80 on
  the axes. ka = E/E* holds exactly with a = 2L, because the gravity runner's "cube edge" is the site spacing.
  - #10100's ~1e-80 used a = L = 8.1e-35 m, which gives 9.6e-81 (4x low).
  - #10094's ~1e-62 is reproduced only by dividing an eV energy by E* in GeV: 3e-63..1e-61 (h f vs hbar f). A 1e9
    slip in the ratio. #10100's order is right.
- d. Cubic photon decay, with exact two-body kinematics including the photon's own term:
  - Formula: k_th(S) = (144(4S-1)/(3S-1)^2)^(1/4) sqrt(m_e E*), with S = sum n_i^4.
  - Values: axis 80.4 PeV; sky-average ray (S = 3/5) 105 PeV; face 122 PeV; body diagonals closed.
  - The ONE correct number is the sky minimum, 80.4 PeV (axes), as a function of direction.
  - The quotes are samples of this one function: "0.8-1.1e17" is axis to the sky-average ray, and "80-122" is axis to
    face. "78" came from the register form that omits the photon term, and "160" corresponds to S = 0.41 or a crude
    estimate.
  - The whole prediction belongs to the retired cubic tick. On D4 it is RETRACTED (no dim-6 for spin <= 1).
- c. Nucleon lifetime. Both numbers come from proton-theta's formula, under different assumptions.
  - 5.3e42 yr is the WORST case: p -> pi+ nubar (uddn), 2x2x2-cell scale Lambda = 9.25e17 GeV, A = 3, largest
    lattice W.
  - 1.1e46 yr is the CENTRAL value of ONE channel, p -> nubar K+: site scale 2.62e18 GeV, A = 1.5, mean W. The
    shortest central lifetime is pi+ nubar, 1.4e45 yr. So "~1e46 yr" is not the nucleon lifetime, and ">~5e42 yr"
    is the correct lower bound on the cubic map.
  - On the D4 map, c dt = a (no tick constant) and Lambda = E* = 1.22e18 GeV per site 4-volume, down to E*/sqrt8 per
    event 4-volume 8a^4. That gives >~2.5e41 yr (worst) and 6.5e43 yr (shortest central). This passes every bound by
    >= 2e7 (pi+ nubar 3.9e32 yr).

## Smuggling review
- Forced or exact: kappa values; the beta formula; the pole-scaling identity; the 16^-n law; the exactness of the fixed
  point's band; the kinematic formulas; the k_th(S) closed form.
- Supplied:
  - free models;
  - the NN Wilson start (w = 1);
  - alpha = 1/2;
  - the rung count n and Ls;
  - the slab per-layer ratio 1/3 (#10099);
  - E* = hbar c/2L;
  - the parent nuclear formula and the composite-flow reading;
  - proton-theta's W, A and channel list;
  - m_e, m_p, the bounds, and KATRIN's 0.45 eV.
- Reading [S], load-bearing: rule 3's rung-n weight lives on the events, so its NN start sits on a 2^n-finer lattice
  (sub-site; the same axiom question as the image tower). If the NN start were pinned to the events, the rungs would be
  a redescription and the n = 0 numbers would stand.
- No rule is proposed. Nothing is fitted.

## Open
- p -> p gamma for n >= 2 (the composite residual against the unzoomed photon).
- Loop-level dim-8 species dependence (#10095), so the ratio 16^(1-n) is tree level.
- The perfect link weight, which would restore the ratio 16.
- Graviton dim 8.
- The slab with Ls >= 58 in a tick form.
