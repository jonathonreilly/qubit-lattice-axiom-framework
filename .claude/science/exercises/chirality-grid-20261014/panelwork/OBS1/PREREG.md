# OBS-1 pre-registration: X2 observational sheet (written 2026-10-14 ~21:35Z, before any script run)

Agent: Claude Opus 5.5 (same family as supervisor, X2, K1 and panel D; not independent). Memory cap 0.3 GB per run, one process at a time, OMP_NUM_THREADS=2.

## FIXED readings (copied, not changed): packet TESTS.md, "Panel D work items", OBS-1

- R1 flavour-strain (X2-L8): FLAV-KILL (>10x over a bound on every allowed branch) / FLAV-NEAR (within 10x on some branch) / FLAV-SAFE (below 1e-2 of all bounds on every branch) / OPEN.
- R2 Z4^F on the light sector of the full X2 law incl. leakage operators and EW breaking: Z4-EXACT (=> Dirac neutrinos, no 0vbb, as a prediction) / Z4-BROKEN (name the operator) / OPEN.
- R3 proton decay floor on 1/a from X2 leakage vs Super-K: PDK-SAFE-AT-PLANCK (state the floor) / PDK-FAIL-AT-PLANCK / OPEN.

## Interpretation rules fixed now (my choices, consistent with the FIXED text)

- "ratio" = predicted rate / observational bound. "Within 10x" = ratio in [0.1, 10]. "More than 10x over" = ratio > 10.
- "Allowed branch" = a branch of the X2 law as specified plus a stated, unexcluded completion choice (flavour alignment, coupling set, strain reading, estimator). Branches that zero the coefficient only by an UNREGISTERED clause (panel F's primitive P-R19-34a', the gravity "counting rule" Q2) are reported separately and are NOT used for the primary reading (agents do not adopt clauses). I will also state what the reading would be if they were counted.
- If some branch is > 10x and some branch < 0.1x and none in [0.1, 10]: OPEN.

## R1 plan

Physics set-up (all choices stated; nothing here is X2 content except the walker and corner assignment):
- Carrier: X2's walker h(k) = sum_a sigma_a sin k_a (continuous time). A Dirac mass needs two 16-components (e.g. Q and u^c); the second is particle-hole conjugated, chi with h_chi(k) = -sigma.s(k). Toy Dirac: H(k) = tau_z (x) sigma.s(k) + tau_x (x) m(k), with m(k) = m0 (on-site, cubic singlet; same mass at all three hw1 corners) + Delta f_NN(k), f_NN = (1 - sum cos k_a)/2 (mirror-gap proxy, zero at hw1). Branches Delta in {0, 0.5}.
- Gauge field: vector-like U(1), NN photon Omega^2 = sum 4 sin^2(q_a/2), Feynman gauge, continuous time, minimal coupling by per-axis divided differences (Ward-identity vertex) plus second-divided-difference tadpole. Couplings: e^2 = 0.1 (leptons), C_F g_s^2 = 0.4 (quarks), as TW-2/F1 (ESTIMATE); bracket x0.5-x2.
- Strain: SF (the root's rule as used by F1/F6/TW-2): each band's momenta flow with its own dispersion, time-1 map. Walker: tan phi = tan k e^{t h_aa/2}; photon: tan(phi/2) = tan(k/2) e^{t h_aa/2}. Mass symbol flows with the fermion flow (FB1). Inverse-metric perturbation s_ab = t h_ab; |s| = |h_GW| (reading, as F6).
- Quantity: at the hw1 corner e_x, delta ln m_pole = Sigma0_mass/m0 + c (c = identity part of dSigma/d(i omega)). C_par = d/dt for h = e_x e_x, C_perp = d/dt for h = e_y e_y; K = C_par - C_perp so that for traceless s: d ln m(corner c) = e^2 K s_cc. Also K_v (static velocity anisotropy at the corner, untuned): from Sigma0 at e_x + q e_x vs e_x + q e_y.
- Controls (checked before using K): (i) h_yy and h_zz responses agree at e_x (D4 symmetry); (ii) continuum log: [delta ln m](m0=0.05) - [delta ln m](m0=0.1) vs (3 e^2/8 pi^2) ln 2 = 0.0263 e^2, within 30% at the largest N; (iii) Ward identity of the vertex to < 1e-10; (iv) K independent of m0 (0.1 vs 0.05) within 20%.
- Grids: midpoint N^3, N = 32, 48, 64 (80 if time); strain step t = +-0.02, symmetric difference. Converged if N = 48 and 64 agree within 20%; otherwise quote the range and label "unconverged".
- Mapping (checked arithmetic; sizes conditional): generation g sits at one corner; a whole 16 (e, u, d, ...) sits at one corner. Flavour-alignment branches:
  - A, corner-aligned: every mass eigenstate ~ one corner (hierarchical, residual ~ D4-type).
  - B, minimal: up quarks and charged leptons T-aligned (C3-Fourier eigenvectors, corner weights 1/3, no first-order coupling), all CKM in the down sector, PMNS in neutrinos. Electron coefficient 0 at first order.
  - B', up quarks and neutrinos T-aligned; CKM in down sector, PMNS in charged leptons.
  - Weights from PDG central CKM/PMNS (RECALLED).
- Nucleon weights d ln m_p / d ln m_q (RECALLED/ESTIMATE): f_u = 0.02, f_d = 0.03, f_s = 0.04, f_c = f_b = f_t = (2/27)(1 - 0.09) = 0.0674.
- Clock: TW-2's estimator (copied function), slope of one orthonormal traceless component under NANOGrav 15-yr (A = 2.4e-15, gamma = 13/3): rate = S1 x ||kappa||_F; bound 3.6e-17/yr (Lange et al. PRL 126, 011102 (2021): -8(36)e-18/yr, 1 sigma). Both LS-slope and rms-hdot estimators, f_min 1/16 and 1/30 yr, T_obs 5 and 10 yr.
- SME mapping: (a) static c_jk of a mass eigenstate = sum_c w_c (gauge-loop corner anisotropy e^2 K_v) P_c, untuned; (b) after a cubic-invariant velocity counterterm per field type (set C's tuning, counted once), the generation-blind part cancels for every mixing; residual only from generation-dependent loops (suggested size y^2/16pi^2 x K_v). Bounds: electron c_jk ~1e-21 (Sanner et al. Nature 567, 204 (2019); Dreissen et al. Nat. Commun. 13, 7314 (2022)), neutron c_jk ~1e-29 (Smiciklas et al. PRL 107, 171604 (2011)). The strain coupling itself gives no static c_jk without a static traceless strain (structure; static registration is open).
- Also stated, not computed: H-cov (bond-strain) reading, where non-on-site generation-splitting symbols shift at tree level (O(1) coefficient); P-R19-34a'/counting-rule branch (zero by construction).

## R2 plan

Audit (proved/checked arithmetic with exact rationals): (1) Z4^F = centre of on-site Spin(10) = exp(i pi X/2) (K1:76; strategy z4 script, rechecked independently). (2) Every X2 term: walker, filter, W Q(psi_S) (Spin(10) singlet), G_SM links, leakage channels L4 (filter imperfection, link conversion, strain) -> charge. (3) EW breaking: doublet H with Yukawas forces H charge 2; show the vacuum <H> preserves Z4^F up to a hypercharge gauge rotation (gauge-invariant order parameters). (4) List every gauge-invariant operator class that breaks it (Delta(B-L) = 2 mod 4) and whether X2 contains or generates it. (5) Check whether U(1)_X (stronger) is exact in X2. Reading Z4-EXACT if (2)-(4) hold for the law as specified with any doublet EWSB; Z4-BROKEN if any X2 term or unavoidable EWSB effect breaks it; OPEN if X2's own content is ambiguous.

## R3 plan

Leading light-sector Delta B operators and their dimension (proved by selection rules: Z4/U(1)_X, corner labels, G_SM). Coefficient branches C = c_eff a^2: (i) link-pair conversion c = W eps^2, eps in [0.02, 0.13] (X2:155), W in [1, 10]; (ii) loop-renormalised filter offset c = W df^4; (iii) worst case allowed with a light light-sector, c = W <= 10; (iv) direct filtered quartic (dim 14). Rate Gamma = (m_p/32 pi)(1 - m_pi^2/m_p^2)^2 |C W0 A_R|^2, W0 in [0.10, 0.15] GeV^2 (lattice QCD, Yoo et al. PRD 105, 074501 (2022), pi0 by isospin; RECALLED range), A_R in [1, 2.5]; bound tau(p -> e+ pi0) > 2.4e34 yr (Super-K, PRD 102, 112011 (2020)). Floor 1/a_min = sqrt(c_eff C_bound^-1 ...). Reading PDK-SAFE-AT-PLANCK if 1/a_min < 1/l_P = 1.22e19 GeV on every branch. Recheck the skeptic's tau estimate (it omits phase space and W0).

## Scripts

`scripts/r1_loop.py` (one-loop K, K_v, controls), `scripts/sizes.py` (clock, SME, R3 floor, R2 arithmetic). Outputs `.out`, timing/memory `.err` via /usr/bin/time -l.
