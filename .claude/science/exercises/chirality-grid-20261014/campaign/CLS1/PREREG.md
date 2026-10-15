# CLS-1 pre-registration (written 14:55Z 2026-10-15, before any run)

Worker: Claude Opus 5.5 (xhigh), same family as supervisor and OBS-1..4. Cap 0.4 GB (scripts/capped.sh). Deadline 18:30Z.
SUPERVISOR_OWN_THREAD.md for CLS1 exists on the packet branch; I have NOT read it and will not until results are in.

## Item and FIXED readings (TESTS.md, "Campaign wave 2d", copied in substance, not editable)
CLS-1: does class S (lattice-scale electroweak-singlet condensate at the three hw2 momenta, breaking unit translations to BCC) destroy X2's light generations?
- CLS-SAFE: (i) holds, (ii) leaves light gapless, (iii) within bounds, for every f in the range the up-sector Yukawas need (g f a ~ 0.33, g <= 4 pi, so f a >= 0.026).
- CLS-PRICE: safe only for part of that range, or with a named extra tuning or structure; state its size.
- CLS-KILL: for every f in that range the light generations are gapped, or modified beyond a bound by more than 10x.
- OPEN: otherwise.
Scope to state: mirror-gap model, dimension, order.

## Inputs read before writing (path:line cited in report)
X2 COMBO_REPORT (all), OBS-4 REPORT/REFEREE_VERDICT/referee REFEREE.md sec.5, OBS-3 REPORT + referee verdict in TESTS.md, NT-3 REPORT + REFEREE_VERDICT, K1 KILL_REPORT, MINIMAL_AXIOMS (all 233 lines), TESTS.md waves 2a-2d.
Prior art on main (grep done): THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10 (generations = distinct joint characters of T_x,T_y,T_z); CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10 (abstract C P K algebra for staggered D; precedent only). No BCC / class-S analysis found.

## Pre-run analytic expectations (written now so they cannot be fitted later)
E1. BCC = {n : n_x = n_y = n_z mod 2} contains d = (1,1,1); T_d acts on corner Q as (-1)^hw(Q), which equals the walker node chirality prod_a cos Q_a. So I expect the BCC label to coincide with chirality: sectors {hw0,hw2} (4 R) and {hw1,hw3} (4 L).
E2. Same translation charge: a corner-changing Yukawa psi_c psi_c' H0 S_K and a corner-changing hopping psi_c^dag psi_c' S_K carry the same momentum (Q_c + Q_c' = Q_c' - Q_c mod 2pi). So class S allows light-LIGHT corner mixing (hw1_x <-> hw1_y via K_z), not only light-hw3. I expect this to matter more than theta.
E3. Spin-scalar on-site density coupling S_K psi^dag psi splits the odd-sector Weyl nodes in energy (a-type, dimension 3): eigenvalues eps*(J_4 - 1) -> {3eps, -eps x3}. Expect Fermi pockets, i.e. flavour-dependent a_0 in the light sector.
E4. A lattice antiunitary Theta (psi(x) -> psi^dag(-x)^T, particle-hole x site inversion) is a symmetry of the free walker and forces h(-k) = -h(k) for every Theta-even one-body term; it pins all TRIM points of the BCC zone (which include both folded corner points) at E = 0. Theta is NOT axiom content (AX:37-38 proper rotations + translations only; K1 scope line 133; AX:169 K/CPT is downstream). If used, it is named structure.
E5. With Theta, bond-modulated walker hopping (Theta-even) still mixes light corners at linear order in q (c-type, dimension 4, flavour off-diagonal). Expect O(eta) flavour-dependent speeds.
These are expectations, not results.

## Model class (stated scope)
- 3D cubic lattice Z^3, continuous time, free-fermion (one-body) level per Spin(10) component; Spin(10)/Z4^F/B-L enter only through the exclusion of Majorana-type (F = 2) bilinears (16 x 16 has no singlet).
- Walker H0 = sum_k psi_k^dag sigma.sin k psi_k. Filter f_NN = (1 - sum cos k)/2 (primary), f_F1 not used unless time.
- Class-S condensate: S_K(x) = f cos(K.x), K in {K_x=(0,pi,pi), K_y=(pi,0,pi), K_z=(pi,pi,0)}; cubic-symmetric (equal amplitudes) primary; one anisotropic variant (amplitudes 1, 0.7, 0.4) as a check.
- BCC-allowed perturbations from S (amplitude eps = g' f, scanned eps*a in {0.003, 0.01, 0.03, 0.1, 0.33, 1}):
  P-a on-site density  eps sum_K cos(K.x) psi^dag psi;
  P-b on-site spin density eps sum_K cos(K.x) psi^dag sigma_{a(K)} psi (sigma_x with K_x, etc.);
  P-c bond-symmetric modulated walker hop eta sum_b cos(K_b.x)[psi^dag(x+b) sigma_b psi(x)/(2i) + h.c.], K_b = the hw2 vector with zero b component;
  P-d S-modulated filter psi_S = F psi + kappa sum_K cos(K.x) psi (light enters the interacting field).
  For each, Theta parity computed (script), and cubic invariance checked.
- Mirror gap model (primary): free-fermion auxiliary-partner proxy, the IR picture of SMG. Each site carries an auxiliary 2-spinor chi (per component), static (no kinetic term), coupled only through the filtered field: H_gap = Delta sum_x [chi^dag(x) psi_S(x) + h.c.]. At kappa = 0 this reproduces X2-L2: hw1 modes are exact zero modes with no chi weight; mirror corners gapped. Delta in {0.5, 1, 2}.
- Secondary (only if time): NT-3-style ED proxy. Not promised.

## Measurements
M1 (i) Brute force over the 8 corners: residual group = BCC residues mod 2; characters; node chirality = sign det of the velocity matrix (numerical derivative of sigma.sin k); sector index per component.
M2 (ii) Folded Bloch Hamiltonian (BCC zone, 4 corners x 2 spin for psi, plus 4 x 2 for chi): at the odd point P and Gamma, count exact zero modes; min |E| on a k-grid; Fermi-pocket volume; theta^2 = weight of each light zero mode outside the three hw1 corners (hw3 psi weight + chi weight, reported separately); w^2 = overlap of each light mode with psi_S (its weight in the interacting channel) -> induced light coupling W w^4 (four light legs) and W w^2 (mixed).
M3 (iii) Light effective Hamiltonian at small q (3 flavours x 2 spin): energies at q = 0 (a-type), eigen-speeds along 26 directions (c-type flavour spread and anisotropy), compare to bounds.
Controls (registered): C1 eps -> 0 recovers exact decoupling (zero modes with chi and hw3 weight <= 1e-12; X2-L2). C2 BCC label table by brute force. C3 theta cross-checked against direct real-space diagonalisation on an L = 4 and L = 6 torus (agreement <= 1e-8) and against the perturbative formula.

## SMG-threshold rule (comparator; fixed now)
The mirror corners hw0/hw2 enter psi_S with |f| = 1, hw3 with |f| = 2. X2 needs W >= W_c for them (W_c = O(1) lattice units, comparator). A light mode with interaction-channel weight w feels W w^4 (four light legs). Margin = 1/w^4 = the largest W/W_c at which that light mode stays below threshold.
- (ii)-pass: max light w^4 <= 0.1 (margin >= 10) at the stated eps.
- (ii)-fail: max light w^4 >= 1.
- between: conditional on X2's unknown W window (stated).
In the partner proxy a light mode counts as gapped only if its zero mode is lifted (no partner counting beyond the model).

## Bounds (iii) (recalled unless fetched; labelled in report)
- a-type (dimension 3) flavour off-diagonal / flavour-dependent: neutrino oscillation bounds of order 1e-23 to 1e-24 GeV (IceCube 2018); quark Delta a from neutral mesons of order 1e-20 GeV (K). Same lattice term acts on all 16 components, so the lepton rows apply.
- c-type (dimension 4) flavour off-diagonal / flavour-dependent speeds: neutrino of order 1e-27 (IceCube 2018); quark isotropic rows 1e-22 / 3e-23 as printed (OBS-3, D44).
- Lattice scale 1/a = M_Pl = 1.22e19 GeV primary; 2e16 GeV variant.

## Reading rules (application of the FIXED wording, fixed now)
R1. (i) holds iff the brute-force table gives two BCC sectors each of a single chirality.
R2. Natural size of each S-induced coefficient: eps*a = g' f a with g' = g (same strength as the Yukawa, so eps*a = 0.33 across the range) as central; the scan brackets g' in [0.1, 1] relative. If a coefficient is forbidden by a symmetry of X2 as written, it is zero; if forbidden only by an added symmetry (e.g. Theta), that is named structure.
R3. If at natural size every f in [0.026/a, 1/a] gives some light observable above a bound by > 10x, and NO symmetry-allowed choice of law coefficients (tuning) or named symmetry removes it: CLS-KILL. If a named tuning (size = bound / natural) or a named structure removes it: CLS-PRICE with that size. If (i) holds, (ii) passes and (iii) is within bounds at natural size for every f: CLS-SAFE. Otherwise OPEN.
R4. A tuned law coefficient counts as a tuning only if the coefficient is not protected; if radiative regeneration is not computed, that is stated (suggested), and the size estimate is labelled suggested.

## Deviations policy
Dated follow-ups only, in PREREG_FOLLOWUP_2026-10-15.md, times from date -u.
