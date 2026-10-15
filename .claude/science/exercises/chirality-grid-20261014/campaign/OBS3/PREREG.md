# OBS-3 pre-registration (written 2026-10-15 12:09Z, before any run)

Agent: Claude Opus 5.5 at xhigh (same family as the supervisor, X2, OBS-1, OBS-2; not independent).
Cap 0.4 GB per run via `scripts/capped.sh`; one process at a time; OMP_NUM_THREADS=2. Deadline 15:30Z.

## FIXED readings (copied from packet TESTS.md:393-410, "Campaign wave 2a"; not changed)

- Question: over a stated family of X2-admissible realisations of the observed quark masses and CKM, what is
  the minimum flavour-pattern residual? The family must include at least: embeddings W_u, W_d with
  W_u^dag W_d = V_CKM (left-handed); free right-handed rotations; corner symbols of range <= 2; on-site and
  corner-selective vertices; off-diagonal entries carried by covariant tau_x sigma_c condensates or flavons;
  a nearest-neighbour Higgs. Residual = what remains after the per-field speed counterterm and the per-field
  tetragonal A1 counterterm (both allowed). Measured against the clean D44 rows (c°^d, d°^d, c°^u, d°^u,
  "> or < 1e-22 as printed") and the electron rows.
- TEXTURE-ESCAPE: some realisation in the family keeps every direct-row residual within its bound with no
  further counterterms.
- TEXTURE-FORCED: every realisation in the family exceeds some direct row by more than 10x. Give the minimum
  over the family and a lower-bound argument if one exists.
- OPEN: otherwise.
- Scope to state: one loop, symmetric-phase Higgs, the family as built, no running from 1/a.

## Interpretation rules fixed now (my choices; consistent with the FIXED text)

1. **Measured rows ("direct rows" of the reading).** Kostelecky-Russell arXiv:0801.0287 v19, Table D44 part 3
   (source key 2017Schreck*, M. Schreck, PRD 96, 095026 (2017), arXiv:1702.03171), as printed in the v19 LaTeX
   source (`ref_OBS2/paper.tex:10426-10441`):
   - u: c°^u - (3/4)k_tr - (3/8)(f°^u)^2 > -3e-23 ; |d°^u| < 3e-23  (printed value is 3e-23, not 1e-22;
     "as printed" governs);
   - d: c°^d - ... > -1e-22 ; |d°^d| < 1e-22.
   In the Yukawa-only one-loop comparison the photon k_tr and f are zero (as in the OBS-2 referee's reading).
   SME map: c_TT = (3/4) c°, c_TT = -(3/4) dv_iso, hence c° = -dv_iso(vector), d° = -dv_iso(axial), with
   vector = (L + R)/2, axial = (L - R)/2 (OBS-2 sizes2.py:75-76; referee REFEREE.md:39-47).
   - Electron rows: as used by OBS-2 (Table D6: c_TT > -5e-21 astrophysics; anisotropic c ~5-9e-21 trapped
     Yb+), from OBS-2 `sizes2.py:37` (secondary citation).
   - Ratio = |violating value| / bound; a one-sided row counts only its excluded sign.
2. **Side rows (reported, NOT used for the reading):** the neighbouring D44 part-3 anisotropic rows
   c^(4)_33 (u: > -6e-22, |d^(4)u_33| < 6e-22; d: > -3e-21, |d^(4)d_33| < 3e-21; frame convention as printed,
   not verified by me); D44 parts 1-2 direct DIS/Drell-Yan rows; heavy-quark and meson-mapped rows as in OBS-2
   (mapping suggested). If the reading rests on rows that these side rows would overturn, I say so.
3. **Counterterms.** Per field f in {Q, u^c, d^c, L, e^c}: subtract the 9-entry mean of the corner/axis
   velocity table (speed counterterm) and the corner-covariant tetragonal component (OBS-2 `sizes2.py:55-59`).
4. **Realisation vs bracket.** Realisation choices: W_u (then W_d = W_u V), X_u, X_d, symbol realisation
   (on-site part, range-1 vs range-2 selective symbols), vertex placement (sym/int/ext), off-diagonal carrier
   (M1 frozen condensate / M2 covariant tau_x sigma_c flavon). Bracket (uncertainty) variables: IR regulator
   m0 = mH in {0.1, 0.05, 0.025}, mirror proxy Delta in {0, 0.5}, coupling scale (low-scale; Planck bracket
   x0.45 quarks). A realisation "keeps a row within its bound" only if it does so over the whole bracket.
   I report separately whether an escape (if any) is **structural** (independent of every loop tensor) or
   **tuned** (zero only on a hypersurface of realisation parameters; tuning level stated).
5. **TEXTURE-FORCED test.** Numerical minimisation (multi-start Nelder-Mead/Powell over the continuous
   parameters, enumeration over discrete ones) of the max fixed-row ratio; FORCED requires the minimum over
   the family to exceed 10 over the bracket AND a lower-bound argument or a stable numerical minimum. A
   numerical minimum alone is labelled checked, not proved.
6. **Restricted family "up sector flat"** (asked for): W_u has all |W_ci|^2 = 1/3 and the up data are
   corner-universal (X_u = W_u, Hermitian circulant up texture; variant X_u = W_u D with D diagonal phases).
   Its minimum is reported separately; the reading is on the full family.

## Model (copied from OBS-2 unless stated)

- Carrier, Dirac embedding, NN Higgs, symmetric phase, one loop, self-energy and velocity formulas:
  OBS-2 `scripts/yuk_lv.py:1-18` (code copied, not edited, into my `scripts/`). Loop tables: OBS-2's archived
  N = 24..96 `yuk_kin_*` (Higgs, symbols {1, g_x, g_y, g_z}) and `yuk_flav_*` (flavon at Q, tau_x sigma_c and
  spin-blind) JSON files.
- **New tables (range-2 symbols):** a copy `yuk_lv3.py` adds g2_c(k) = g_c(k)^2 = ((1 - cos k_c)/2)^2 (range 2,
  equal to g_c at every hw1 corner) to the symbol set; kin runs at N = 48 and 96 (N = 96 used; 48 for
  convergence), m0 in {0.1, 0.05, 0.025}, Delta in {0, 0.5}.
- **Corner-basis Yukawas.** Y_u = W_u diag(m_u) X_u^dag / v, Y_d = W_d diag(m_d) X_d^dag / v,
  W_d = W_u V_CKM. Diagonal entries Y_cc are carried by the q ~ 0 NN Higgs through symbols: Y(p,k) = y_0 +
  sum_c [(1 - theta) y_c g_c + theta y_c g2_c] with y_0 + y_c = Y_cc (complex); y_0 (complex) and theta in
  [0, 1] are realisation parameters (OBS-2's "trace" = y_0 = mean diag, theta = 0; "selective" = y_0 = 0).
  Loop: T(c,a) = sum_{ss'} Re(eta_s eta_s'^*) I_ss'(c,a). For a right-handed field the 'int' and 'ext'
  placements are swapped (the internal leg of the L loop is the external leg of the R loop) -- a refinement of
  OBS-2, which used the same variant for both; 'sym' is unaffected.
- **Off-diagonal entries** Y_cc' (c != c', Q = c - c' in hw2): M1 = frozen tau_x sigma_c condensate, no
  one-loop term (OBS-2 primary); M2 = covariant tau_x sigma_c doublet carrier light at Q with coupling
  |lambda_cc'| = |Y_cc'| (all vevs set to v: the minimum coupling allowed by sum_A v_A^2 <= v^2, hence an
  under-estimate of M2 loop sizes), kernel K_fl(c, c', a) from OBS-2's flav tables by cubic covariance.
  L field at corner c: sum_{c'} |lambda_cc'|^2 K_fl(c,c'); R field at corner c': sum_c |lambda_cc'|^2 K_fl(c',c).
- Multiplicities (OBS-2): Q: u + d sectors; u^c: 2 x up; d^c: 2 x down; L: e + nu; e^c: 2 x e.
  Leptons fixed to OBS-2 branch B (Y_e circulant, Y_nu = F U_PMNS).
- Mass eigenstate i of a chiral field: dv_i(a) = sum_c |W_ci|^2 r_c(a) (left) or |X_ci|^2 (right); flavour-
  off-diagonal kinetic entries reported, not in the reading.
- **Inputs.** PDG 2024 (RPP, S. Navas et al., PRD 110, 030001 (2024)), RECALLED: m_u = 2.16 MeV, m_d = 4.70 MeV,
  m_s = 93.5 MeV (MS-bar, 2 GeV), m_c = 1.2730 GeV, m_b = 4.183 GeV (MS-bar at own mass), m_t = 172.57 GeV;
  CKM global fit lambda = 0.22501, A = 0.826, rho-bar = 0.1591, eta-bar = 0.3523; direct moduli for the
  circulant test |V_ub| = 3.82(20)e-3, |V_cb| = 41.1(1.2)e-3, |V_td| = 8.6(2)e-3, |V_ts| = 41.5(9)e-3,
  |V_us| = 0.2243(8), |V_cd| = 0.221(4), |V_ud| = 0.97367(32), |V_cs| = 0.975(6), |V_tb| = 1.010(27). If a quick
  check finds a different printed value I record it in a dated follow-up. v = 174.1 GeV (OBS-2). The OBS-2
  reproduction control uses OBS-2's own inputs (`sizes2.py:23-33`).

## Analytic programme (labels: proved / checked / suggested)

- S1 Translation invariance => kinetic counterterm-level LV is corner-diagonal; mass eigenstate coefficient =
  |W|^2-weighted corner average (first order).
- S2 Write T_f(c,a) in terms of the corner-basis Yukawa entries and kernels; state when only (W y^2 W^dag)_cc
  enters (all carriers share one kernel) and when off-diagonal entries enter individually.
- S3 Cancellation condition (residual = 0 for a field) and the per-row conditions.
- S4 Conjecture: both W_u, W_d flat <=> V equivalent to a circulant (Haagerup 1996 classification of 3x3
  complex Hadamard matrices). CKM moduli vs the Latin-square pattern forced by a circulant.
- S5 Any partial-flatness alternative (e.g. only the first-generation columns flat) and its consequences
  for the measured rows; lower bounds within "up sector flat".

## Runs (in order)

- C1 (control, before anything new): reproduce OBS-2 branch-B c_TT^d = -2.1067e-8 at N = 24, m0 = 0.1,
  Delta = 0, sym, trace split, OBS-2 inputs, with my own assembly code (`obs3_core.py`) from OBS-2's N = 24 table.
  Pass: within 1e-4 relative of -2.10666e-8 (worker) / -2.10667e-8 (referee).
- C2: circulant inputs (W = X = F for u and d, Hermitian circulant textures; and V = 1) give zero residual in
  every field for M1 and M2, |residual| <= 1e-12 x |universal part|.
- C3: cubic covariance: (a) the archived tables satisfy C3[111] covariance (<= 1e-12 abs); (b) the assembly is
  covariant: permuting corners by C3 in the realisation permutes the per-corner residual accordingly.
- C4: N-convergence of any headline number: N = 48 vs 96 (<= 20% else labelled unconverged).
- R1: escape constructions suggested by S5 (if any), checked over the full bracket and all realisation
  discrete choices.
- R2: minimisation over the full family (fixed rows), then over "up sector flat".
- R3: side rows for the minimising realisations.
