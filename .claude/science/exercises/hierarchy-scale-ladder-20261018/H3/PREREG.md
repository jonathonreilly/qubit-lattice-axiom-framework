# HIER-3 pre-registration (written 2026-10-18 12:16Z, before any run)

Item: HIER-3 of `.claude/science/exercises/hierarchy-scale-ladder-20261018/TESTS.md`
(local packet copy `hier/packet/TESTS.md:58-73`; identical to the branch copy at
12:14Z). Readings are FIXED: G-WINDOW / G-OUTSIDE / G-UNFIXED / OPEN.
Worker: Claude Opus 5.5 (test agent, same family as supervisor and H1 referee).
Deadline 18:30Z. Cap 0.4 GB, one process at a time, via `zsh scripts/capped.sh`.

## Sources read before this file

- `docs/MINIMAL_AXIOMS_2026-06-29.md`, whole (g_bare = 1 is an open gate, `:188`;
  admissibility supplies no weight values, `:118-125`).
- H1 `REPORT.md`, `REFEREE_SF.md` (15-decade one-loop edges g^2 <= 0.208 pure SU(3),
  <= 0.403 SU(3) N_f = 8; (b) open below g_bare = 1).
- PR #9702 note (rungs `:120-128`; Lambda_HK/Lambda_W = 1.819 `:206,:225`;
  "relevant couplings ... never fixed" `:367`).
- Main: `G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md` (convention,
  beta = 6), `G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-05-09.md`
  (conditional "forced" g_bare = 1), `G_BARE_RESCALING_FREEDOM_REMOVAL...`,
  `G_BARE_CONSTRAINT_VS_CONVENTION...`, `G_BARE_PARENT_PROMOTION_GATE_MAP...`,
  `G_BARE_DYNAMICAL_FIXATION_OBSTRUCTION...` (no feature at beta = 6),
  `HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md` (B1 <P> = 0.5934, u0, alpha_LM;
  corrigenda), `HIERARCHY_VALUE_FRONTIER_PROBE_2026-06-05.md` (one-loop decades 4.30 /
  2.74; needed 1/alpha(M_Pl) = 42.8; run-up 52.4), `HIERARCHY_ALPHA_LM_DIM_TRANS_REFRAMING...`
  (notation identity only), `ALPHA_S_DERIVED_NOTE.md` (alpha_s(v) = alpha_bare/u0^2 placed
  at mu = v by declared B4; C1 0.118233), `ALPHA_S_SOMMER_STATIC_POTENTIAL_ROOT_KERNEL...`
  (repo certificate r0/a = 5.0057 at beta = 6, a = 0.0999 fm with r0 = 0.5 fm),
  `CONFINEMENT_STRING_TENSION_NOTE.md:101-128`, `SOMMER_SCALE_FROM_WILSON_CHAIN...`,
  `YT_EW_COUPLING_BRIDGE_NOTE.md:145-158` (alpha_LM too strong for AF running over 38
  decades), `GAMMA_FULL_VS_GAMMA_CRIT_DECISIVE_NOGO_NOTE_2026-06-08.md:73-76`,
  `HIGGS_MASS_RETENTION_ANALYSIS_NOTE_2026-04-18.md:685` (g3(M_Pl) = 0.489 run-up),
  `YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md:543` (g_s(M_Pl)^2 = 1/u0),
  `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md` (colour on the 2^3 taste cube).
- COL-1 (branch `claude/chirality-grid-exercise-20261014`): `panelwork/COL1/REPORT.md`
  (cells of 19 / 35 qubits; link truncated to {1, (3bar,3)} `:66-74`), `PREREG.md`,
  `REFEREE_VERDICT.md`. X2' definition: chirality `TESTS.md:652-720` (3x16 at Gamma,
  mirrors gapped; 96 modes per site).

## Definitions (fixed now)

- **Cutoff of the first coloured rung.** M_cut = M_Pl / b, M_Pl = 1.2209e19 GeV (B2).
  b = 1 (grid; primary), 2 (graph-first taste cube), 5 (ladder rung-1 corner site),
  19, 35 (COL-1 cells).
- **Strong scale.** Lambda_* = the two-loop MSbar Lambda parameter of the flavour
  number active at the strong scale. Robustness readings: the 4-loop Lambda, and
  mu_1 = the scale where the two-loop MSbar alpha reaches 1. Spread is reported.
- **Primary target T_v.** Lambda_*/M_Pl = v/M_Pl = 246.22/1.2209e19 = 2.017e-17.
  **Window W_v:** Lambda_*/M_Pl in [2.0e-18, 2.0e-16] (one decade either way; covers the
  O(1) factor between Lambda and any physical scale, and a supplied link v = c Lambda
  with 0.1 <= c <= 10). The link from a colour scale to v is itself a SUPPLIED input
  (composite/technicolour-type); it is listed, not derived.
  Also reported: the HIER-1 edge Lambda_*/M_cut <= 1e-15.
- **Secondary target T_QCD (comparator; cannot change the reading).** The colour
  coupling at M_cut that reproduces observed QCD: Lambda^(5)_MSbar in [0.021, 2.1] GeV
  (centre 0.21 GeV), via SM running with thresholds from alpha_s(M_Z) = 0.1180.
- **Content.** A: pure SU(3). B: SM-like colour, SU(3) with n_f = 6 (T_v; massless
  above Lambda_*); for T_QCD the SM with thresholds m_c, m_b, m_t and the two-loop SM
  gauge system with one-loop top Yukawa above m_t. C: X2' = SM + 3 nu_R (colour and
  EW singlets) + 3 mirror generations gapped at M_mirror = kappa M_cut, kappa in
  {1, 0.3, 0.1} (mirrors add 6 colour flavours and 3 generations above M_mirror).
- **Schemes for window edges.** MSbar at mu = M_cut (primary). Pure gauge also in the
  Wilson bare scheme (Lambda_MS/Lambda_L = 28.809, comparator, Hasenfratz-Hasenfratz
  1980) and the heat-kernel scheme (Lambda_HK/Lambda_W = 1.819, PR #9702 `:206`).
- **"Derived without tuning".** A candidate counts only if its derivation consumes no
  target scale (v, r0 in fm, alpha_s(M_Z), any scale ratio below 1e-2) and has no
  adjustable parameter. A candidate that consumes one is reported as CIRCULAR.

## Candidates (task item 2) and how each is evaluated

C1 g_bare^2 = 1 (beta = 6). C2 mean-field / tadpole forms: g_MF^2 = 1/<P>,
4 pi alpha_LM = 1/u0, 4 pi alpha_s(v) = 1/u0^2, plaquette coupling
alpha_P = -3 ln<P>/(4 pi). C3 main's plaquette value (B1 0.5934; point estimate
0.59369) feeding C2. C4 COL-1 class-M cells. C5 rung 0 -> 1 matching that the ladder
makes computable (heat-kernel/Wilson Lambda ratio; one-loop block matching by b).
C6 alpha_s(v) = 0.1033 placed at mu = v (B4), run to M_cut. C7 the direct
Wilson-loop lane's ruler (r0 = 0.5 fm, a = 0.0999 fm).
Each perturbative candidate is read in its most favourable way (the larger of the
MSbar reading and the Wilson-bare reading of the same number). C1-C3 are also read
non-perturbatively from the repo's beta = 6 certificate (r0/a) with
Lambda_MS r0 = 0.602 (comparator, ALPHA collaboration).

## Runs (all via `zsh scripts/capped.sh OUT python3 ...`)

- **R1 `r1_window.py`.** Two-loop (and 1-, 3-, 4-loop) MSbar running with
  thresholds; window edges in g^2(M_cut) for A, B, C, at every b, for W_v, the
  HIER-1 edge, and W_QCD. Regression PASS criteria (must hold before any window is
  used): (i) one-loop 15-decade edges reproduce 0.208 (pure) and 0.403 (N_f = 8) to
  3 digits; (ii) one-loop b0 = 7: needed 1/alpha(M_Pl) = 42.8 and run-up from
  alpha_s(M_Z) = 0.118 gives 52.4 (value-frontier `:161-165`) to 0.1; (iii) the
  piecewise two-loop map alpha_s(v) = 0.10330382 -> alpha_s(M_Z) = 0.118233
  (ALPHA_S_DERIVED C1, n_f = 6 above 172.69 GeV, identity matching) to 1e-5;
  (iv) 2-loop Lambda formula is RG-invariant along a 2-loop trajectory to 1e-8.
- **R2 `r2_candidates.py`.** Values of C1-C3, C5, C6, C7; their strong scales in every
  reading; distance to W_v in decades and in g^2 ratio; C6 run-up; non-perturbative
  beta = 6 strong scale from the certificate (read from `origin/main`).
- **R3 `r3_truncated_plaquette.py`** (C4). (i) Haar Monte Carlo check of the SU(3)
  character integrals used. (ii) Exact maximum of the compressed operator
  Re Tr(U1 U2 U3^dag U4^dag)/3 on four truncated links, T10 = {1, (3bar,3)} (COL-1 as
  built; analytic prediction 1/18) and T19 = {1, (3bar,3), (3,3bar)}. (iii) Isolated
  gauge-invariant plaquette ceiling c(n) for links truncated to irreps with p+q <= n,
  with the per-link register size sum dim^2 and its qubit count; the smallest n whose
  ceiling reaches the Wilson plaquette at beta = 6 (0.5934) and at the window coupling
  (weak-coupling plaquette 1 - 2/beta - 1.2208/beta^2, comparator).
  PASS criteria: Haar integrals within 4 sigma; T10 maximum = 1/18 to 1e-10; c(n)
  increasing in n with c({1,F}) = 1/6 and c({1,F,Fbar}) = 1/3.

## Decision rule (fixed now)

- **G-WINDOW** iff some candidate that counts as derived (definition above) has its
  most favourable strong scale inside W_v, robust across the loop-order and
  strong-scale definitions.
- **G-OUTSIDE** iff every candidate that counts lands outside W_v in every reading
  (CIRCULAR candidates are reported and do not count either way).
- **G-UNFIXED** iff no candidate is derivable at all; then the primitive is stated as
  "the colour coupling g^2(M_cut) in [window]" with its precision requirement.
- **OPEN** otherwise (e.g. a candidate inside in one reading and outside in another).
- Because g_bare = 1 is currently an admitted convention (with a conditional "forced"
  reading), the report will state both: the reading over the listed candidates, and
  what the hierarchy reduces to if the convention is dropped.

## Worker's expectation (before runs)

G-OUTSIDE: every framework candidate sits at g^2 >= 1 (alpha >= 0.08), the window is
near g^2 ~ 0.15-0.3; the beta = 6 lattice confines about one decade below its cutoff
(r0/a = 5). Inside values appear only by placing the coupling at mu = v (circular).

## Follow-up (12:22Z, after R1-R3 ran; nothing above is changed)

- R1 9/0, R2 8/0, R3 11/0 PASS. One addition, R4 `r4_scheme_direction.py`, decided now:
  main's `GAMMA_FULL_VS_GAMMA_CRIT_DECISIVE_NOGO_NOTE_2026-06-08.md:73-76` says the
  beta = 6 bare alpha 0.08 "is not the MSbar continuum value (alpha_s(M_Pl) ~ 0.019,
  smaller)". R4 checks the direction: (i) one-loop Wilson-bare -> MSbar at mu = 1/a
  with Lambda_MS/Lambda_L = 28.809 (comparator); (ii) the non-perturbative MSbar
  coupling at mu = 1/a of the beta = 6 theory from the repo certificate r0/a and
  Lambda_MS r0 = 0.602 (comparator), two-loop and four-loop inversion, n_f = 0;
  (iii) the Wilson beta that the observed colour coupling at M_Pl (g^2 = 0.237, r1.log)
  corresponds to, under the pure-gauge one-loop conversion (labelled as such).
  PASS criteria: (i) and (ii) both give alpha_MS(1/a) > 0.0796 (direction), and (iii)
  gives beta > 6.
- Note on r2.log: the line "inside the W_v g^2 band? True" for C6 compares with the
  union of all contents' bands (0.167-0.361); the pre-registered criterion is the
  strong scale for C6's own content (n_f = 6), which is outside W_v (next lines).

## Follow-up (12:24Z)

- R4 4/0 PASS. After R4 the 4-loop Lambda integrand in `rgcommon.py` was rewritten in
  an exact rational form (the first form cancelled 1/x^2 terms and gave scipy
  roundoff warnings). R1 and R4 were rerun: every number is unchanged (old logs kept as
  `r1_v1.log`, `r4_v1.log`); only the 4-loop invariance residual moved
  (2.53e-12 -> 3.57e-12). R2 and R3 do not use the 4-loop path.
