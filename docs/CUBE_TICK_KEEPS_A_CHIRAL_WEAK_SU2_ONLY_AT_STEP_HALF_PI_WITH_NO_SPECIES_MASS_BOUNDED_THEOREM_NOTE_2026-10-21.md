---
claim_id: cube_tick_keeps_a_chiral_weak_su2_only_at_step_half_pi_with_no_species_mass_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the cube tick of the candidate laws register, the sublattice sign commutes with the tick iff the step is pi/2 and the species mass is 0, so a chiral SU(2) exists only there, the copy factor breaks it at every step, and at small step the exact one-body group is a single vector-like U(8); with a supplied Spin(10) pair square as the mirror term the linked group would be su(4)+su(2)+su(2); given a chiral link, Yang-Mills forces one coupling, the contact limit gives m^5 rates and V-A Michel parameters, and fermion bilinears give rho = 1; no exact chiral weak SU(2) at the register's step, no breaking scale and no 125 GeV scalar are established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/cube_tick_keeps_a_chiral_weak_su2_only_at_step_half_pi_with_no_species_mass_2026_10_21.py
---

# The cube tick keeps a chiral weak SU(2) only at step pi/2 with no species mass

Claim type: bounded_theorem.
Primary runner: `scripts/cube_tick_keeps_a_chiral_weak_su2_only_at_step_half_pi_with_no_species_mass_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. This note asks under what rule a left-handed weak SU(2) is exact on the register's cube tick, what the weak-decay data then require, and whether the symmetry can break without a fundamental scalar. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix no gauge group. The answer is a wall with named conditions, not a working rule.

## Statement

1. U - sUs = 2i(sin th_o cos th_e W_o(K) - cos th_o sin th_e W_e), with th = eps +- mu/2. So the sublattice sign s commutes with the tick iff eps = pi/2 and mu = 0.
2. The one-body commutant is span{1, s} at (pi/2, 0) and scalars elsewhere. With the (4,2) cell index carried in parallel, the exact group is U(8)_even x U(8)_odd at step pi/2 and one vector-like U(8) otherwise (g_A = 0).
3. The register's copy factor breaks s at every step except M = pi, so the register as written has no chiral SU(2) at any step.
4. The block inversion swaps SU(2)_even and SU(2)_odd, so if both are linked, g_L = g_R.
5. With the Spin(10) pair square on the mirror 16 as the mirror term, the symmetry in gl(16) is so(10) (dimension 45), and inside u(8)_e + u(8)_o it is su(4) + su(2) + su(2) (dimension 21), with no U(1). The linked group equals the symmetry of the mirror term.

## Derivation

Statements 1 to 4 are direct algebra on the tick. At step pi/2, s = -g5 s3 on the light algebra, and the s = +1 cells hold (L, copy w) + (R, copy w^2), so an SU(2) acting as T x (1+s)/2 links one copy's L and the other copy's R. A copy mass is s-odd. The commuting version of the Spin(10) pair square vanishes by a Fierz identity; the Grassmann version does not.

Given a chiral link. A doublet with generators lambda T^a keeps the covariant derivative covariant only for lambda = 1, with defect i g lambda(1 - lambda) eps^abc a^b A^c T^a psi, so a non-abelian link gives every doublet one coupling. Dirac traces and exact three-body phase space give Gamma = G^2 m^5/(192 pi^3) f(m_e^2/m^2) in the contact limit. A chiral link gives Michel parameters (rho, xi, delta) = (3/4, 1, 3/4); a vector-like link gives (3/8, 0).

Breaking without a scalar. Every bilinear psi_R^dag psi_L of chiral content is a |Y| = 1/2 doublet, so any EM-neutral pattern of dynamical masses leaves a massless photon and rho = 1 exactly. If SU(2)_R is also linked, bidoublet condensates leave 4 massless links (isospin-symmetric) or 2 (photon and B-L); an extra B-L = 2 nu_R-pair condensate leaves the photon alone. All 11 colour- and Fermi-allowed four-mode products of one family hold an even number of doublets, so none is a doublet; the three with Y = 0 are exactly the |B| = |L| = 1 operators. So the four-mode mirror sector cannot break the electroweak symmetry.

## Checks

The runner gives `TOTAL: PASS=19 FAIL=0` in 2.3 s.

- A1: closed form, residual 3e-16; |[s,U]| = 1e-16 at (pi/2, 0) against at least 0.09 elsewhere.
- A2: commutant dimensions [2, 1, 1, 1, 1, 1].
- A3: traces (L1, L2, R1, R2) on s = +1 are 2, 0, 0, 2.
- A4: |[s,U]| = 0.76, 1.20, 6e-11 at M = 0.5, 1, pi.
- A5: the inversion V is unique and V s V^+ = -s.
- A6: stabiliser dimensions 45 and 21; block U(1) residual at least 0.25.
- A7: band maximum 3.1416 at step pi/2 against 0.0740 at the vacuum bound eps < 0.037.
- B1: the covariance defect (sympy).
- B2: rate ratio 1.000000000000, m^5 scaling x32.000000, f = 0.99981295 at m_e/m_mu.
- B3: Michel parameters 0.7500, 1.0000, 0.7500 (chiral) and 0.3750, 0.0000 (vector-like).
- B4, B5: the tau/mu universality and W-mass comparisons below.
- C1: rho = 1.000000000000 on 24 random condensates; a T = 1 order parameter gives 0.9943 (Y = 1) or 1.0115 (Y = 0).
- C2: rho = 0.999928 at v_R = 40 v for the nu_R-pair condensate.
- C3, C4, C5, D1, D2: the estimates and the four-mode product count below.

Comparisons with measurement (estimates). The vector-like link is off the measured rho = 0.74977(26) and xi = 1.0009(16) by 1441 and 626 sigma. One coupling and m^5 predict a tau/mu ratio of 1.00040 against 1.0026 +- 0.0029 (0.8 sigma), which needs M_W > 15.2 GeV at 2 sigma; colour-only breaking gives M_W near 52 MeV, below the muon mass. With g_L = g_R and g_4 = g_3, the couplings meet at M_R = 5.1e13 GeV at one loop; breaking at the cell scale gives sin^2 theta_W = 0.193 against 0.2312. A top condensate on the step-pi/2 tick (I0 = 1.15672, g_c = 1/(4 I0)) needs g/g_c - 1 = 6e-32 and gives m_t = 103 to 202 GeV and m_H = 206 to 215 GeV, against 172.69 and 125.20, so no 125 GeV scalar appears. With three families and no scalar, b0 is 7 for SU(3), 10/3 for SU(2)_L and 32/3 for SU(4); the measured couplings at the cell confine at about 5e-2 GeV and 3e-24 GeV, while v needs b0 alpha_cell = 0.171, which no group in the content has. At small step the mass zero is unprotected, so each species mass is tuned (electron about 4e-19 against O(alpha/4pi) dressing).

## Boundary

Supplied: the cube tick with its step, species mass and copy factor; the rung-1 index in parallel; the Spin(10) mirror term, whose symmetry chooses the group; Dirac and Fermi contact forms or the W propagator; the SM one-loop beta functions; the QED correction; f_pi and measured values. Cited, not rederived: Vafa-Witten, anomaly matching, the existence of a symmetric gapped mirror phase, and the chirality-graded wall that keeps U(8)_A x U(8)_B at small step. The commutant result covers block-local generators only; a quasi-local Ginsparg-Wilson-type chirality is not excluded. Negative results: at the register's step there is no exact chiral SU(2); setting all species massless alone gives a vector-like group; no computed route gives a confining sector near v or the 125 GeV scalar. Necessary conditions found, not adopted: no per-species mass in the update, copies told apart only by a four-mode term, an exact chirality grading at small step, and a sector with b0 alpha_cell near 0.17.
