# OBS-4 pre-registration (written 2026-10-15 13:46Z, before any run)

Agent: Claude Opus 5.5 at xhigh (same family as the supervisor, X2, OBS-1, OBS-2, OBS-3; not independent).
Cap 0.4 GB per run via `scripts/capped.sh`; one process at a time; OMP_NUM_THREADS=2. Deadline 17:00Z.
Nothing has been computed yet. Read so far: campaign_common.txt; packet SUMMARY.md; TESTS.md (wave 1, 2a, 2b);
OBS3 REPORT / REFEREE_VERDICT / referee REFEREE.md (full); OBS2 REPORT / REFEREE_VERDICT / referee REFEREE.md (full);
OBS1 REPORT (full); X2 COMBO_REPORT (full); docs/MINIMAL_AXIOMS_2026-06-29.md (full); OBS3 PREREG and
scripts/univ.py, obs3_core.py:145-170. Literature already fetched (abstract/table level only):
Isidori-Nir-Perez arXiv:1002.0900 Table 1; UTfit (Bona et al.) arXiv:0707.0636 Table 4 and eqs. 6-9;
Harnik-Kopp-Zupan arXiv:1209.1397 Table 2; FLAG 2024 (arXiv:2411.04268) kaon BSM B-parameters (search summary).

## FIXED readings (copied from packet TESTS.md:441-453, "Campaign wave 2b"; not changed)

- Question: For B-gen and B-gen120, and for any other exact OBS-3 escape realisation the worker builds:
  derive the tree-level dF = 2 couplings of the carrier scalars in the mass basis; compare them with K-Kbar
  (eps_K, dm_K), B_d, B_s and D mixing bounds (state the sources); find the minimum carrier mass M* that passes
  every bound; say whether the construction can give those carriers mass M* while their condensate supplies the
  electroweak-scale off-diagonal Yukawas (for example: no tuning; a tuning of a stated size; or forced to be light).
- FCNC-SAFE: some exact escape realisation passes every dF = 2 bound with carrier masses the construction
  supplies without new tuning.
- FCNC-PRICE: passing needs M* above a stated scale, or alignment, and that costs a named tuning or structure;
  state its size.
- FCNC-KILL: every escape realisation built violates some dF = 2 bound by more than 10x for every carrier mass
  the construction allows.
- OPEN: otherwise.
- Scope to state: tree level, the carrier model, the meson matrix elements used, and the running.

## Interpretation rules fixed now (my choices; consistent with the FIXED text)

1. **Exact escape realisations ("realisations").** Corner-basis quark mass matrices M_u, M_d (corners x,y,z =
   hw1 momenta Q_x=(pi,0,0), Q_y, Q_z) that reproduce the quark masses and CKM and meet OBS-3's exact
   escape conditions:
   - **B-gen**: rebuilt from the stored parameter vector p by the exact formula univ.py:78-85 (common complex
     diagonal, six equal off-diagonal moduli), not from the rounded stored matrices (OBS-3 referee 2.4).
   - **B-gen120**: same with the cubic-character diagonal phases (univ.py:84).
   - **B-gen#k**: further exact B-gen solutions from re-running OBS-3's own fit (same residual function, new seeds),
     accepted if every mass-ratio and |V_ij| pull <= 1e-6 and | |J|-J_PDG | <= 1e-3 sigma.
   - **A-M1#0..2**: OBS-3's M1 diagonal-equalised realisations (univ_A_M1.npz: W_u = F, random, E1), escape in the
     M1 carrier model only (referee: numerical construction).
   - If a fit gives J < 0 (PDG definition J = Im(V_us V_cb V_ub* V_cs*)), its complex conjugate (all moduli
     unchanged, hence the same escape) is the physical realisation; both are evaluated, the conjugate is primary.
2. **Selection rule (to be proved, S1).** With exact unit translations, a Yukawa entry psi_c^T ... psi_c' Phi needs
   the scalar to carry lattice momentum Q_c + Q_c' (mod 2pi): diagonal entries <-> momentum 0 (H_0), the pair
   {(c',c''),(c'',c')} <-> K_c = Q_c' + Q_c'' in hw2.  So the corner-basis carrier supports are disjoint.
3. **Carrier models** (fields that carry the corner-off-diagonal entries):
   - **D3 (type-III, primary doublet class):** one SU(2)xU(1) doublet, Y = 1/2, at each hw2 momentum K_c
     (c = x,y,z), coupling to the up pair (via Phi~) and the down pair (via Phi); H_0 (momentum 0) carries the
     diagonals. Four doublets. This is OBS-3's M2 covariant tau_x sigma_c doublet carrier and its
     "Higgs degenerate at hw2" mechanism 2 (same EFT content).
   - **D6:** separate up and down carrier doublets at each K_c (six) plus the H_0 diagonal carrier(s).
   - **S (singlet-flavon class):** EW-singlet, Spin(10)-singlet scalars S_K at hw2 condensing at scale f; the
     off-diagonal entries come from the lattice operator psi psi H_0 S_K, so only one EW doublet (H_0) exists.
     This is the "single light Higgs through a lattice-scale operator" alternative of the task.
   Vevs: <phi_K^0> = v_K (complex-field normalisation, v = 174.1 GeV as OBS-3), sum_K |v_K|^2 = v^2 over
   doublets. Coupling of carrier K: Y^(K) = P_K(M)/v_K, P_K = projection of M on K's support.
4. **dF = 2 effective Hamiltonian.** Mass basis M = W diag(m) X^dag, carriers rotated Yhat^(K) = W^dag Y^(K) X.
   Primary spectrum: decoupling limit, every heavy Higgs-basis doublet with H_k, A_k (and H_k^+-) degenerate at a
   common mass M; then only the LR operator Q4 = (qbar_R^i q_L^j)(qbar_L^i q_R^j) is generated, with
   C4^{ij} = - sum_{k heavy} N_k,ij N_k,ji^* / M^2 = - sum_K Yhat^K_ij Yhat^K_ji^* / M^2 (the aligned light
   direction drops out in the mass basis; to be proved, S2). Light-h misalignment (O(v^2/M^2)) neglected.
   Robustness (not the reading): H/A split per heavy doublet, giving C2, C2~ = -(Yhat^2/4)(1/M_H^2 - 1/M_A^2);
   compared with UTfit 0707.0636 Table 4 |C2| rows.
   Systems and index pairs (mass basis): K: (s,d); B_d: (b,d); B_s: (b,s) [down]; D: (c,u) [up].
5. **Bounds (primary):** Isidori-Nir-Perez Table 1, LR rows, c = 1 at Lambda, Lambda in TeV:
   K Re 1.8e4 / Im 3.2e5; D Re 6.2e3 / Im 1.5e4; B_d Re 1.9e3 / Im 3.6e3; B_s |.| 3.7e2.
   M*_row = Lambda_row * sqrt(|Re or Im of sum_K Yhat^K_ij Yhat^K_ji^*|) (B_s: modulus); M* = max over rows.
   These bounds include UTfit's NLO running from Lambda and its matrix elements (0707.0636 eqs. 6-9, Table 2);
   residual scale mismatch (bound quoted at Lambda vs carrier at M*) is a log effect, stated not corrected.
   **Own cross-check (secondary, not the reading):** direct dm_K, eps_K, dm_Bd, dm_Bs, dm_D from
   <Q4> = (1/2)(m_P/(m_q1+m_q2))^2 m_P^2 f_P^2 B4 (FLAG convention, O4 = 4 Q4), M12 = <H>/(2 m_P);
   LO running of C4 with gamma_44 = -16 (alpha_s/4pi; magic-number exponent -8/beta0, = -1.143 at nf = 6, matching
   UTfit's a_4), one-loop alpha_s with alpha_s(M_Z) = 0.118, thresholds m_t, m_b. Inputs: FLAG 2024 Nf=2+1
   B4^K = 0.903 (MSbar, 3 GeV); B4 for B_d, B_s, D taken as 1.0 +- 0.15 (recalled FNAL/MILC 2016, HPQCD 2019,
   ETM 2015; not fetched); f_K = 155.7, f_D = 212, f_Bd = 190, f_Bs = 230 MeV (FLAG, recalled); MSbar masses at
   the hadronic scale (recalled). NP allowances: |dm_K^NP| <= dm_K^exp; |eps_K^NP| <= 0.2 |eps_K^exp|;
   |dm_Bd^NP| <= 0.3 dm_Bd^exp; |dm_Bs^NP| <= 0.3 dm_Bs^exp; |dm_D^NP| <= dm_D^exp (x_D ~ 0.4%), |Im| <= 0.1 of that.
   **Published-number cross-check:** reproduce Harnik-Kopp-Zupan 1209.1397 Table 2 rows (m_h = 125 GeV,
   type-III-like flavour-violating scalar) from the same C4 normalisation; and, if accessible in budget, one
   2HDM-type-III bound from the literature.
6. **Phase convention.** After the SVD, quark fields are rephased so that W_u^dag W_d equals the PDG standard
   parametrisation built from OBS-3's inputs (lambda = 0.22501, A = 0.826, rhobar = 0.1591, etabar = 0.3523);
   Im rows are evaluated in that convention.
7. **Vev distribution.** M* is minimised over (|v_0|, |v_x|, |v_y|, |v_z|) on sum = v^2 (D6: over the up and down
   carrier vevs too), subject to perturbative carrier Yukawas: every |Y^(K)| entry <= sqrt(4 pi). The equal-vev
   point is also reported.
8. **Coupling-scale bracket.** Low-scale couplings y = m/v (OBS-3 inputs) and x0.5 (quark Yukawas run down by
   roughly this factor between M_Z and 1e3-1e4 TeV; recalled, not computed). M* scales linearly.
9. **"Carrier masses the construction allows" (question 3).** Analysed for the renormalisable Z2xZ2-symmetric
   (lattice-translation) scalar potential at tree level, with quartics <= 4 pi and carrier Yukawas <= sqrt(4 pi):
   M_allowed is the largest heavy-carrier mass compatible with the off-diagonal masses B-gen needs. Because this
   is a tree-level, perturbative estimate, the reading is also tested at a generous cap M_cap = 10 TeV.
10. **Decision rules (applying the FIXED text).**
   - A class "passes" if at some allowed vev distribution and some carrier mass the construction supplies, every
     primary row has |coefficient| below its bound.
   - "The construction" = X2 as written: the law covariant under unit translations, and a vacuum that keeps exact
     single translations above the electroweak scale (X2-L1/X2-L2 use exact single translations,
     X2 COMBO_REPORT:84-95). A realisation that needs unit translations broken spontaneously above the electroweak
     scale (for example class S) is counted as **named structure**, not as something the construction supplies;
     if it passes, the reading is FCNC-PRICE with that structure and its scale stated (and any tuning stated).
   - FCNC-SAFE needs a pass inside the construction as written with no new tuning.
   - FCNC-KILL needs every realisation built (including class S, if built) to fail some row by > 10x at every
     carrier mass the construction allows.
   - FCNC-PRICE: passing needs M* (stated) above what the construction allows, or alignment, at a named tuning or
     structure (size stated).
   - OPEN: otherwise (including: M_allowed cannot be bounded, or controls fail).

## Analytic programme (labels: proved / checked / suggested)

- S1 selection rule and disjoint supports; physical-scalar count per class.
- S2 basis independence of the degenerate-heavy dF = 2 sum; no-alignment lemma (Pich-Tuzon alignment
  Y^(K) proportional to M/v for all K is impossible with disjoint supports; simultaneous bi-diagonalisation fails
  whenever a sector has invertible diagonal part and some nonzero off-diagonal entry).
- S3 natural flavour conservation (one doublet per charge sector) with exact translations gives monomial supports,
  hence |V_CKM| a permutation matrix (cf. main's Z_3 analogue, NEUTRINO_DIRAC_Z3_SUPPORT_TRICHOTOMY_NOTE.md,
  LEPTON_SINGLE_HIGGS_PMNS_TRIVIALITY_NOTE.md).
- S4 scalar potential: exact translations act as Z2xZ2 on (H_0, Phi_x, Phi_y, Phi_z); no tadpole for Phi_K from
  H_0; what bounds the carrier masses; the decoupling-limit alternative and its cost.
- S5 class S: one doublet => no dim-4 tree-level FCNC; flavon exchange size; what it costs.

## Runs (in order)

- C1 (control): rebuild B-gen, B-gen120 from p; reproduce mass ratios and |V_ij| (pulls <= 1e-9) and |J|; print
  sign of J.
- C2 (control): alignment control (fictitious Y^(K) = zeta_K M/v for all K): every off-diagonal Yhat <= 1e-12
  relative; single-doublet control (all of M on one field) the same.
- C3 (control): normalisation cross-check with HKZ Table 2 at m_h = 125 GeV (UTfit-derived rows reproduced within
  10%), and own direct bag-parameter computation of the K and D rows within a factor 2 of INP/UTfit.
- R1: carrier couplings in the mass basis, flavour-diagonal (aligned) part vs flavour-changing part, per
  realisation and carrier; M*_row and M* for D3 and D6 at the equal-vev point and minimised over vevs; both
  coupling scales.
- R2: B-gen#k robustness (several exact fits); A-M1 realisations.
- R3: H/A-split robustness against UTfit C2 rows.
- R4: question 3 numbers (M_allowed; violation factor (M*/M_allowed)^2 and at M_cap); class S estimate.
