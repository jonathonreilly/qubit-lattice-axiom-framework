---
claim_id: a_site_tick_count_and_a_site_density_answer_the_hinge_sum_through_one_operator_so_light_bends_twice_the_newtonian_amount_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Static weak field of a count geometry in which a site may skip ticks (lapse N = 1 + Phi, the fraction of ticks a site takes) and the site density sets the spatial factor (Omega = 1 + psi). The response is the hinge sum (CL-3), reduced to static prisms: S/dt = (1/8 pi G) sum_e N_e l_e delta_e (spatial edges e, 3D deficits delta_e), plus a rest-mass record whose phase advances once per taken tick, -m N(source). Exact (continuum, sympy): the lapse variation gives lap psi = -4 pi G rho and the density variation gives lap(Phi + psi) = 0, so psi = -Phi = GM/r outside the source: PPN gamma = 1 with no tuning, and G drops out of gamma. Exact (discrete, linearised, any triangulation, any common edge-averaging): the Phi-psi and psi-psi blocks of the static Regge Hessian are the same operator K = D^T J D, so the density equation reads K(Phi + psi) = 0 and every spatial-edge equation reads J D(Phi + psi) = 0. Finite diagnostic (Kuhn-triangulated 14^3 grid, Dirichlet box): the full nonlinear action confirms the shared operator to 2.5e-7, K tends to -2 lap isotropically to 0.5%, the solved point source has psi/(-Phi) = 1 to 1e-12 on every shell, and one-bond-per-taken-tick light gives Shapiro delay and deflection 2.0000 times the Newtonian part. The tied tick (N = Omega) instead gives a single conformal field of the wrong sign: Phi = +GM/(3r), repulsive, gamma = -1. The lapse must be a SITE variable: edge l*delta stays nonzero off-source (Ricci != 0) while its site sums vanish. Not derived: the hinge coefficient (G) in SI units, the second-order beta, the vector and tensor sectors."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_site_tick_count_and_a_site_density_answer_the_hinge_sum_through_one_operator_so_light_bends_twice_the_newtonian_amount_2026_10_23.py
---

# A site tick count and a site density answer the hinge sum through one operator, so light bends twice the Newtonian amount

Claim type: bounded_theorem.
Primary runner: `scripts/a_site_tick_count_and_a_site_density_answer_the_hinge_sum_through_one_operator_so_light_bends_twice_the_newtonian_amount_2026_10_23.py` (21 PASS, 0 FAIL, ~13 s, ~210 MB).

## Question

Earlier work found two independent counts under the tick-skip repair (R-a; agents/random-connectivity): the lapse N = 1 - U (the fraction of ticks a site takes) and the spatial factor Omega = 1 + gamma U (site density). Kinematics allows any gamma. The tied tick of the split clause (agents/geometry-as-count, item 4) forces gamma = -1. The question here is whether the framework's own response law fixes gamma.

## Setup (rules used, rederived where used)

- CL-3 response: the hinge sum, (1/8 pi G) sum_hinges A_h delta_h (coefficient one in cell units, from the CL-3 unit map).
- Static reduction. On static prisms (each spatial simplex swept through one taken tick), the timelike hinges are spatial edge x time. Their areas are N_e l_e dt and their deficits are the 3D deficits delta_e. The spacelike hinges have zero deficit (no extrinsic curvature). So S/dt = (1/8 pi G) sum_e N_e l_e delta_e. This is the discrete form of the integral of N sqrt(h) R3 (static Gauss-Codazzi; Regge: the integral of sqrt(h) R3 is 2 sum l delta).
- R-a counts: N_v = 1 + Phi_v per site, and l_e = l0_e (1 + psi_e) with psi = the site-density factor. N_e and psi_e are endpoint averages.
- Source: the copy-mass phase of a record at rest advances once per TAKEN tick, so S_m = -m sum_ticks N = -m N(source) dt. It contains no Omega, because a static lump's phase counts ticks, not sites (T_ij = 0 at rest).

## Results

### Theorems

1. Continuum (A1-A5, sympy). R3 = -e^(-2 psi)(4 lap psi + 2|grad psi|^2). The second-order density is equivalent to 4 grad Phi . grad psi + 2|grad psi|^2.
   - The lapse Euler-Lagrange equation is -4 lap psi. With the source this gives lap psi = -4 pi G rho.
   - The density Euler-Lagrange equation is -4 lap(Phi + psi). It has no source, so Phi + psi is harmonic and vanishes at infinity.
   - Result: psi = GM/r, Phi = -GM/r, gamma = 1, attractive. Both gravity terms carry 1/G, so gamma does not depend on G.
2. Discrete shared operator (B2, B4, C4). F = sum l delta has gradient delta (Schlafli) and Hessian J at flat. At flat delta = 0, so the cross term is Phi^T D^T J D psi and the psi psi term is (1/2) psi^T D^T J D psi, with D = diag(l0) A. Both blocks equal K = D^T J D. This holds for any triangulation, provided lapse and density use the same edge-averaging map. The runner confirms it on the FULL nonlinear action by mixed second differences, without using Schlafli (relative deviation 2.5e-7).
   - Consequences: K(Phi + psi) = 0 at every free site. Every individual spatial-edge equation is J D (Phi + psi) = 0, so the isotropic (N, Omega) ansatz is a consistent truncation: no other edge strain is sourced.
3. Tied tick (A5, C5). Setting Phi = psi leaves (3/2) psi^T K psi. The source then gives Phi = psi = +GM/(3r), so the tied count geometry is REPULSIVE at one third strength. This is the conformal-mode sign of the hinge sum, and it is stronger than the earlier "gamma = -1, no bending" verdict: the tied tick fails Newton too, not only light bending.
4. The lapse is a site count (C3). Off the source, edge l*delta is about 2e-4 at q = 1e-3, while the site sums are about 6e-10. Varying a per-EDGE lapse would demand delta_e = 0 on every edge, which is 3D flatness, and that is overdetermined (the exterior has R3 = 0 but Ricci != 0). R-a's per-site tick fraction is exactly the variable that gives the Hamiltonian constraint.

### Finite diagnostics (14^3 Kuhn grid, 13182 tets, 1000 free sites, Dirichlet)

- K is symmetric (1.2e-10) and positive definite (eigenvalues 0.49 to 23.5). Its plane-wave symbol is 2k^2 x (0.995, 0.995, 0.997, 0.998) along 100, 001, 110 and 111 at |k| = 0.25.
- Point source: psi/(-Phi) = 1.000000000000 on all shells with r < 4.6. -Phi r/(Gm) = 0.75 at r = 2 and 0.51 at r = 3; this is Dirichlet-box screening (INFO only).
- Light hopping one bond per taken tick (coordinate speed N/Omega) at b = 2, 3: Shapiro delay/Newtonian = 2.0000, deflection/Newtonian = 2.0001. Under the tied tick both are exactly zero.

### Against measurement

- gamma = 1 meets Cassini (gamma - 1 = (2.1 +- 2.3)e-5) and the VLBI deflection. The solar deflection, 1.75 arcsec, follows with no fitted parameter.

## What fixes G

- The hinge coefficient fixes G in lattice units with nothing fitted: the CL-3 unit map gives 8 pi G = L^2, with L the cell rung. Converting to SI NAMES L = sqrt(8 pi) l_P; it does not predict it. gamma is independent of the coefficient.
- Open tension (INFO). The count-Jacobson reading G = a^2/(4 eta), with eta = 0.0393 per bond (SUPPLIED, from agents/random-connectivity B6), gives 6.36 a^2. Coefficient one gives a^2/(8 pi) = 0.0398 a^2, a factor of about 160 apart if a is the same length. The two readings agree on the field equations, and so on gamma, but not on the coefficient. Reconciling them needs eta = 2 pi per bond, or a cell rung about 12.6 site spacings.

## Proposed working rule (R-a completion) and gate

> "A site's tick fraction is a response variable: like the edges, it takes the value that makes the total phase stationary."

- Bends: CL-1 (every site updates every tick) via R-a. The axioms are unchanged.
- Gate:
  - (1) no measured number is chosen; G stays the coefficient-one value;
  - (2) no observed structure is inserted; the rule names only sites, ticks and edges;
  - (3) predictions it was not built for: gamma = 1, so deflection and Shapiro are twice the Newtonian part; the tied-tick alternative is repulsive; no per-edge lapse is possible. Second-order beta is UNTESTED;
  - (4) bends CL-1.
- PASSES the gate for gamma.

## Smuggling review

Supplied, not forced:
- the static prism reduction of the Lorentzian hinge sum (standard, but the zero spacelike deficits assume an exactly static tick pattern);
- the source coupling -m N (the copy-mass phase per taken tick; a record that also counted sites would add an Omega coupling and change gamma);
- the conformal edge-length assignment l = l0 (1 + psi), "density = proper length per reference bond", which equals R-a's "a/Omega coordinate spacing" only after coarse-graining;
- the Dirichlet box;
- eta (INFO only).

Forced:
- gamma = 1, given those inputs;
- the shared operator;
- the tied-tick repulsion;
- the lapse being a site variable.

Not used: ACTION_NORMALIZATION_NOTE's gamma readout (a different, field-identification route).

## Boundary

- No nonlinear beta.
- No frame dragging: the shift and TT sectors still come from CL-3's edge registers, not from counts.
- No dynamics of how a site decides to skip.
- Light hops are kinematic (one bond per taken tick), not a CL-1 wave-packet computation.
- The Lorentzian sign is taken as the attractive one of the register-cited LORENTZIAN_REGGE_CONTINUATION note (open PR, not on main); gamma does not depend on that sign.

## Uses / narrows

- Uses: agents/random-connectivity (R-a) and CANDIDATE_LAWS_v3 CL-3 (hinge sum, unit map).
- Narrows: agents/random-connectivity's "gamma = 1 iff Ricci-flat (assumed)". The hinge sum supplies the Ricci-flat exterior; it is now derived for the static sector.
- Sharpens: agents/geometry-as-count item 4. The tied tick is repulsive, not merely non-bending.
