---
claim_id: a_site_tick_count_and_a_site_density_answer_the_hinge_sum_through_one_operator_so_light_bends_twice_the_newtonian_amount_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Static weak field of a count geometry in which a site may skip ticks (lapse N = 1 + Phi, the fraction of ticks a site takes) and the site density sets the spatial factor (Omega = 1 + psi). The response is the hinge sum (CL-3 of the originating three-law register, a supplied conditional definition with zero premise weight, not adopted), reduced to static prisms: S/dt = (1/8 pi G) sum_e N_e l_e delta_e (spatial edges e, 3D deficits delta_e), plus a rest-mass record whose phase advances once per taken tick, -m N(source). Exact (continuum, sympy): the lapse variation gives lap psi = -4 pi G rho and the density variation gives lap(Phi + psi) = 0, so psi = -Phi = GM/r outside the source: PPN gamma = 1 with no tuning, and G drops out of gamma. Exact (discrete, linearised, any triangulation, any common edge-averaging): the Phi-psi and psi-psi blocks of the static Regge Hessian are the same operator K = D^T J D, so the density equation reads K(Phi + psi) = 0 and every spatial-edge equation reads J D(Phi + psi) = 0. Finite diagnostic (Kuhn-triangulated 14^3 grid, Dirichlet box): the full nonlinear action confirms the shared operator to 2.5e-7, K tends to -2 lap isotropically to 0.5%, the solved point source has psi/(-Phi) = 1 to 1e-12 on every shell, and one-bond-per-taken-tick light gives Shapiro delay and deflection 2.0000 times the Newtonian part. The tied tick (N = Omega) instead gives a single conformal field of the wrong sign: Phi = +GM/(3r), repulsive, gamma = -1. A per-edge lapse would require delta_e = 0 on every edge (3D flatness); on the solved exterior edge l*delta stays nonzero off-source (Ricci != 0) while its site sums vanish, so the site lapse is the variable that gives the Hamiltonian constraint here. N enters only as a continuous site field; whether a discrete local tick-or-skip rule realises it is open. Not derived: the hinge coefficient (G) in SI units, the second-order beta, the vector and tensor sectors."
upstream_dependencies:
  - minimal_axioms
runner: scripts/a_site_tick_count_and_a_site_density_answer_the_hinge_sum_through_one_operator_so_light_bends_twice_the_newtonian_amount_2026_10_23.py
---

# A site tick count and a site density answer the hinge sum through one operator, so light bends twice the Newtonian amount

Claim type: bounded_theorem.
Primary runner: `scripts/a_site_tick_count_and_a_site_density_answer_the_hinge_sum_through_one_operator_so_light_bends_twice_the_newtonian_amount_2026_10_23.py` (20 PASS, 0 FAIL, ~13 s, ~210 MB; exits nonzero if any counted check fails).

Model status (2026-11-14). The update law (CL-1), the response law's hinge sum and unit map (CL-3) and the tick-skip repair R-a are used here as supplied conditional model definitions with zero premise weight, stated in the Setup below. The originating register text ("CANDIDATE_LAWS_v3") is not in this repository, and these clauses are not the entries of the same number in [docs/CANDIDATE_LAWS.md](CANDIDATE_LAWS.md). No clause is adopted. The sources named by alias (agents/random-connectivity = logged #10036, agents/geometry-as-count = logged #10032) are not in this repository; they are recorded only in the consolidation map, and what is said of them is a historical reported result, unverified here.

## Question

Earlier work (logged #10036) reported two independent counts under the tick-skip repair (R-a): the lapse N = 1 - U (the fraction of ticks a site takes) and the spatial factor Omega = 1 + gamma U (site density). Kinematics allows any gamma. The tied tick of the split clause (logged #10032, item 4) was reported to force gamma = -1. The question here is whether the framework's own response law fixes gamma.

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
   - Consequences: K(Phi + psi) = 0 at every free site. Every individual spatial-edge equation is J D (Phi + psi) = 0, so at linear order the isotropic (N, Omega) ansatz is a consistent truncation: no other edge strain is sourced. (Logged #10048, not in this repository, reports that at second order the anisotropic edge equation fixes C = 2A, so the truncation is not consistent beyond first order; a historical reported result, unverified here.)
3. Tied tick (A5, C5). Setting Phi = psi leaves (3/2) psi^T K psi; in the continuum the Euler-Lagrange coefficient is -12 (A5, computed). The source then gives Phi = psi = +GM/(3r), so the tied count geometry is REPULSIVE at one third strength. This is the conformal-mode sign of the hinge sum, and it is stronger than the earlier reported "gamma = -1, no bending" verdict: in this supplied static setting the tied tick fails Newton too, not only light bending.
4. The lapse as a site count (C3). Off the source, edge l*delta is about 2e-4 at q = 1e-3, while the site sums are about 6e-10. Varying a per-EDGE lapse would demand delta_e = 0 on every edge, which is 3D flatness, and that is overdetermined (the exterior has R3 = 0 but Ricci != 0). R-a's per-site tick fraction is the variable that gives the Hamiltonian constraint in this setting. N enters every equation here only as a continuous site field. Whether a discrete local tick-or-skip rule can realise it is open; logged #10057 reports a pair-creation estimate against skip rules, which rests on a supplied one-dimensional yield and derives no three-dimensional yield (historical, unverified here; no exclusion is drawn in this note).

### Finite diagnostics (14^3 Kuhn grid, 13182 tets, 1000 free sites, Dirichlet)

- K is symmetric (1.2e-10) and positive definite (eigenvalues 0.49 to 23.5). Its plane-wave symbol is 2k^2 x (0.995, 0.995, 0.997, 0.998) along 100, 001, 110 and 111 at |k| = 0.25.
- Continuum point source (A4, sympy): with the lapse and density coefficients read from A2 and A3 (both -4), Gauss's law gives psi = GM/r and Phi = -GM/r, gamma = 1; control: a record phase that also counts sites, -rho(Phi + psi), gives Phi = 0. Tied tick (A5): coefficient -12, Phi = psi = GM/(3r).
- Rescaling the hinge coefficient by 0.5 and 3 leaves psi/(-Phi) = 1 to 1e-15 and scales Phi by 1/c (E).
- Point source: psi/(-Phi) = 1.000000000000 on all shells with r < 4.6. -Phi r/(Gm) = 0.75 at r = 2 and 0.51 at r = 3; this is Dirichlet-box screening (INFO only).
- Light hopping one bond per taken tick (coordinate speed N/Omega) at b = 2, 3: Shapiro delay/Newtonian = 2.0000, deflection/Newtonian = 2.0001. Under the tied tick both are zero by definition (Omega/N = 1), printed as an uncounted IDENTITY line.

### Against measurement

- gamma = 1 meets Cassini (gamma - 1 = (2.1 +- 2.3)e-5) and the VLBI deflection. The solar deflection, 1.75 arcsec, follows with no fitted parameter.

## What fixes G

- Given the supplied CL-3 unit map, the hinge coefficient fixes G in lattice units with nothing fitted: 8 pi G = L^2, with L the cell rung. Converting to SI NAMES L = sqrt(8 pi) l_P; it does not predict it. gamma is independent of the coefficient (computed, E).
- Open tension (INFO). The count-Jacobson reading G = a^2/(4 eta), with eta = 0.0393 per bond (SUPPLIED, from logged #10036 B6, unverified here), gives 6.36 a^2. Coefficient one gives a^2/(8 pi) = 0.0398 a^2, a factor of about 160 apart if a is the same length. The two readings agree on the field equations, and so on gamma, but not on the coefficient. Reconciling them needs eta = 2 pi per bond, or a cell rung about 12.6 site spacings.

## Proposed working rule (R-a completion) and gate

> "A site's tick fraction is a response variable: like the edges, it takes the value that makes the total phase stationary."

- Bends: CL-1 (every site updates every tick) via R-a. The axioms are unchanged.
- Gate:
  - (1) no measured number is chosen; G stays the coefficient-one value;
  - (2) no observed structure is inserted; the rule names only sites, ticks and edges;
  - (3) predictions it was not built for: gamma = 1, so deflection and Shapiro are twice the Newtonian part; the tied-tick alternative is repulsive; a per-edge lapse would over-determine the solved exterior (C3). Second-order beta is UNTESTED;
  - (4) bends CL-1.
- Within the supplied static linear setting, the gate's gamma prediction holds.

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
- that a per-edge lapse is over-determined on the solved exterior (C3).

Not used: the gamma readout of [ACTION_NORMALIZATION_NOTE](ACTION_NORMALIZATION_NOTE.md) (a different, field-identification route).

## Boundary

- No nonlinear beta.
- No frame dragging: the shift and TT sectors still come from CL-3's edge registers, not from counts.
- No dynamics of how a site decides to skip.
- Light hops are kinematic (one bond per taken tick), not a CL-1 wave-packet computation.
- The Lorentzian sign is taken as the attractive one of [LORENTZIAN_REGGE_CONTINUATION_AND_THE_ATTRACTIVE_GEOMETRY_PHASE_SIGN_BOUNDED_THEOREM_NOTE_2026-10-21](LORENTZIAN_REGGE_CONTINUATION_AND_THE_ATTRACTIVE_GEOMETRY_PHASE_SIGN_BOUNDED_THEOREM_NOTE_2026-10-21.md) (on main and on this branch); gamma does not depend on that sign.

## Uses / narrows

- Uses: the R-a repair reported by logged #10036 and the CL-3 hinge sum and unit map of the originating register (CANDIDATE_LAWS_v3, not in this repository), both stated in the Setup as supplied definitions.
- Relation to logged #10036 (historical, unverified here): it reported "gamma = 1 iff Ricci-flat (assumed)"; here the hinge sum supplies the Ricci-flat exterior in the static linear sector.
- Relation to logged #10032 item 4 (historical, unverified here): in this setting the tied tick is repulsive, not merely non-bending.
