# OBS-2 pre-registration (written 2026-10-15 00:42Z, before any run)

Agent: Claude Opus 5.5 (same family as supervisor, X2, OBS-1; not independent). Cap 0.4 GB per run via
`scripts/capped.sh`; one process at a time; OMP_NUM_THREADS=2. Deadline 03:30Z.

## FIXED readings (copied from packet TESTS.md:304-320, not changed)

- Setup: X2's walker carrier with corner-selective Yukawas and a lattice Higgs (nearest-neighbour), one loop.
  Branches A, B, B' as in OBS-1; B primary.
- Compute: each charged-fermion mass eigenstate's Yukawa-induced dimension-4 LV kinetic terms, split into
  (i) the part set C's existing counterterm removes (one cubic-invariant kinetic counterterm per SM field,
  OBS-1 REPORT:74-78) and (ii) the residual (flavour-pattern) part; compare (ii) with current SME bounds
  (Kostelecky-Russell data tables; table and row).
- LV-SAFE: on branch B every residual is within its bound with no further counterterms.
- LV-PRICE(n): some residual exceeds its bound, but n named, local, X2-symmetric counterterms remove it
  (state n and the tuning level).
- LV-KILL: a residual exceeds its bound and no local counterterm respecting X2's symmetries (unit
  translations, cubic rotations as realised on the corners, Spin(10) > G_SM) can remove it.
- OPEN: otherwise.
- T2g strain: add the T2g response to OBS-1's E_g; rate = m_p/m_e drift under the nHz GW background vs
  3.6e-17/yr. FLAV2-KILL: >10x over on every branch. FLAV2-NEAR: within 10x on some branch.
  FLAV2-SAFE: below 1e-2 of the bound on some branch. OPEN otherwise.

## Interpretation rules fixed now (my choices, consistent with the FIXED text)

- "within its bound" = |residual| <= the 1-sigma/95% bound quoted in the table row (whichever the row gives);
  a species with no bound row in the tables is reported as "no bound" and does not count as exceeding.
- "Within 10x" = ratio in [0.1, 10]; "more than 10x over" = ratio > 10 (as OBS-1 PREREG:13).
- (i) is defined as: per SM field f, the part of the corner tensors that is the cubic image of ONE common
  corner tensor (isotropic speed shift + tetragonal v_par - v_perp at the corner's own axis). I report
  separately (a) the isotropic part, which set C's existing per-field speed counterterm removes, and (b) the
  corner-universal tetragonal part, and state whether the existing counterterm also removes (b) or whether a
  second cubic-invariant operator (e.g. sum_a sigma_a sin p_a (cos p_b + cos p_c)) is needed; if needed, it is
  counted as a price item, not hidden in (i).
- (ii) = corner tensors minus (i). Mass-eigenstate coefficients: c_jk(i) = sum_c |U_ci|^2 c^(c)_jk for the
  left (doublet) and right (singlet) fields separately; SME c = (cL+cR)/2, d = (cL-cR)/2 reported.
- LV-PRICE n counts independent tuned real coefficients (and I also list operators). An operator is
  "X2-symmetric" if it is invariant under unit translations, the 24 proper cubic rotations (with spin lift)
  and Spin(10), allowing flavour spurions/flavon fields that carry the breaking (stated per operator).
- Agents adopt no clauses. Branches that zero a coefficient only by an unregistered clause are reported
  separately and not used for the primary reading.

## Model (choices stated; only the walker, corners and symmetries are X2 content)

- Carrier: Weyl walker h(k) = sum_a sigma_a sin k_a per field component; Yukawa pair (psi_1 = doublet
  component, psi_2 = singlet) in OBS-1's Dirac embedding Psi = (psi_1, chi_2), H = tau_z sigma.s(k) +
  tau_x (m0 + Delta f_NN(k)); m0 = IR regulator (0.1, 0.05; m0 -> 0 extrapolated); Delta in {0, 0.5}
  (OBS-1's bilinear mirror-gap proxy; f_NN = (1 - sum cos k)/2).
- Higgs: complex doublet, NN lattice scalar Omega(q)^2 = sum_a 4 sin^2(q_a/2) + mH^2 (mH = m0 regulator).
  Symmetric phase (the dim-4 LV is generated at loop momenta ~ 1/a, where v a ~ 1e-17 is negligible).
  One complex scalar component per Weyl-Weyl pairing = one real scalar loop with coupling y (Dirac scalar
  vertex tau_x). Multiplicities: Q: Y_u Y_u^dag + Y_d Y_d^dag; u^c: 2 Y_u^dag Y_u; d^c: 2 Y_d^dag Y_d; L:
  Y_e Y_e^dag + Y_nu Y_nu^dag; e^c: 2 Y_e^dag Y_e (standard SM structure; checked against gamma_Q, gamma_u).
- Yukawa vertex (translation-invariant, Hermitian, symmetric): Y(p,k) = sum_s y_s [g_s(p) + g_s(k)]/2 with
  g_0 = 1 (on-site), g_c = (1 - cos k_c)/2 (corner-selective, = 1 at hw1 corner e_c, 0 at the other two).
  Comparator vertex: Y = sum_s y_s g_s(k) (Higgs at the psi-bar site). Loop is bilinear in y, so I compute
  I_ss'(corner) for s, s' in {0, x, y, z} and assemble any Yukawa pattern offline.
- Self-energy (Hamiltonian, T = 0, derived in the script docstring): Sigma0(p) = -sum_k w Gam M(k) Gam,
  M = H/(2 E Om (E + Om)); Sigma1(p) = d Sigma/d omega = -sum_k w Gam Gam / (2 Om (E + Om)^2). Velocity at
  corner c along axis a: v_a = 1 + B_a + Sigma1_11 with B_a = d b_a/d q_a / v_tree,a (psi_1 block).
  Off-diagonal d b_a/d q_b also computed (expected 0 by D2).
- Flavour mapping (as OBS-1 sizes.py): corner-basis mass matrices M = U diag(m) U^dag, branches A (U_u = 1,
  U_d = V, U_e = 1), B (F, F V, F), B' (F, F V, F U_PMNS^dag); splits "trace" (on-site tr/3 + selective
  deviations) and "selective" (all diagonal from selective symbols). Off-diagonal corner entries come from
  hw2-momentum vevs and add no symmetric-phase loop coupling in the primary model (M1); comparator M2 (if
  time): a separate covariant flavon triplet carrying them.
- Couplings: y = m/v with v = 174 GeV at low scale (OBS-1 inputs: y_t 0.99, y_b 0.024, y_tau 0.0102) and a
  Planck-scale bracket (RECALLED SM running: quark Yukawas roughly x0.4-0.5, leptons ~x1). Loop order: one.
- SME mapping (traceless c_mu nu, eta = diag(+,-,-,-)): v(p_hat) = 1 - c_00 - c_jk p_j p_k, so isotropic
  delta v = -(4/3) c_TT and the traceless spatial part c_jk = -(delta v_jk traceless).
- Bounds: Kostelecky-Russell 0801.0287 (latest version on arXiv), table and row cited; if I cannot read the
  table in budget I mark the bound RECALLED and say so.

## T2g plan

- Symmetry analysis at the hw1 corners (little group D4 about the corner axis; proper rotations only): which
  T2g strain components can couple at first order to (a) corner-diagonal masses, (b) the hw2-momentum
  off-diagonal entries, for each vertex spin structure.
- Numerical check of the symmetry statements on a covariant loop (the Yukawa loop with the SF flow
  dk_a/dt = (1/2) sum_b h_ab p_b(k), p = grad(E^2/2), applied to fermion, scalar and symbol (FB1)).
- Clock: OBS-1's E_g branch numbers plus the T2g part, combined in quadrature over orthonormal traceless
  components, TW-2's estimator unchanged (copied in OBS-1 sizes.py:59-79).

## Controls (must pass before any number is used)

1. Reproduce OBS-1: static leak L0 = 0.0820 (N = 32/48) or own-corner response 9.99e-3 with the copied code.
2. Ward: OBS-1's U(1) vertex Ward residual <= 1e-12 in the copied code; Yukawa equivalent: Y(p,p) =
   dM(p)/dv to roundoff, and the continuum log: [Sigma1](m0=0.05) - [Sigma1](m0=0.1) for the on-site vertex
   equals -(ln 4)/(32 pi^2) = -4.39e-3 per y^2 within 30% at the largest N.
3. Cubic covariance: I_ss'(e_y), I_ss'(e_z) equal the permuted I_s's'(e_x) to <= 1e-10 relative.
4. N-convergence: N = 24, 32, 48 (64 if time); converged if 32 -> 48 change <= 20% for every coefficient
   used; else quote the range and label unconverged.
5. Staggered-reflection check: the on-site vertex at Delta = 0 gives tetragonal K = 0 at the hw1 corner.

## Readings procedure

Compute residual (ii) per mass eigenstate for A, B, B', both splits, both coupling brackets, and compare to
bounds; apply the FIXED LV rule to branch B. For LV-PRICE, name the operators, count coefficients, give the
tuning level (residual/bound) and X2-symmetry status. Apply the FIXED FLAV2 rule to E_g + T2g.
