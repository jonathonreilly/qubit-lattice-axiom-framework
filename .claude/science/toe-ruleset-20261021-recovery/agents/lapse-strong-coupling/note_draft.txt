---
claim_id: a_nonzero_dark_constant_gives_the_read_lapse_a_gradient_unstable_cell_strain_scalar_and_a_zero_dark_constant_leaves_a_slicing_of_gr_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's read lapse N = sin(eps0)/sqrt(sum_a gamma^aa), not varied, with the shift stationary and the momentum constraints kept, in the continuum ADM limit: the dark constant c = N H is the conserved tick energy of the edges; in vacuum Bianchi I cells with c = 0 the read lapse is a slicing of general relativity at nonlinear order (Kasner directions fixed), while c != 0 bends the solution off it; at linear order on flat cells every k != 0 scalar solution has zeta = 0 for every kinetic coefficient lambda, unlike the projectable lapse. In the decoupling limit around a dark constant c0 (Stueckelberg tick and labels, k >> H_D): on isotropic cells the medium is rigid (the scalar kinetic coefficient cancels exactly and no mode exists at any frequency); on cells with an anisotropic strain d one scalar returns with omega^2 = 2 k^2/(9 khat.S.khat) at leading order in d, which has omega^2 < 0 along some direction for every strain tested (diagonal, axial, off-diagonal, d = 1e-2 to 1e-4), a gradient instability; with c0 = 0 exactly the medium has no mode. That every order of the c = 0, H_k = 0 sector is preserved is argued from the constraint algebra, not computed; the strong-coupling scale k_s ~ rho_D^(1/4) d^(5/8) and the comparisons with measurement are power-counting estimates with supplied inputs. Not computed: the nonlinear endpoint of the growth and lattice (Regge or register) preservation of H = 0."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_nonzero_dark_constant_gives_the_read_lapse_a_gradient_unstable_cell_strain_scalar_and_a_zero_dark_constant_leaves_a_slicing_of_gr_2026_10_22.py
---

# A nonzero dark constant gives the read lapse a gradient-unstable cell-strain scalar, and a zero dark constant leaves a slicing of general relativity

Claim type: bounded_theorem.
Primary runner: `scripts/a_nonzero_dark_constant_gives_the_read_lapse_a_gradient_unstable_cell_strain_scalar_and_a_zero_dark_constant_leaves_a_slicing_of_gr_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1 in the three-law numbering) reads each cube's lapse from its edges, N(gamma) = s/sqrt(sum_a gamma^aa) with s = sin eps0, and does not vary it; the Hamiltonian constraint is then not imposed by the response law (CL-3), and its value per cell, the dark constant c = N H, is conserved. A lapse that is a fixed function of the metric and is not varied resembles the projectable Horava-Lifshitz lapse, which carries a strongly coupled extra scalar. This note asks whether the read lapse, with the shift stationary and the momentum constraints kept, has such a scalar, and how its presence depends on the dark constant. The register's current response law admits only odds obeying the Hamiltonian and momentum constraints, so its dark constant is zero in every cube; this note computes both the c = 0 sector that clause selects and the c != 0 sector it excludes. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Zero dark constant and the linear flat sector.

1. The dark constant c = N H is the tick energy of the edges and is conserved. In vacuum Bianchi I cells, c = 0 data evolve as a slicing of general relativity at nonlinear order: the Kasner direction ratios stay fixed. Data with c != 0 feel the extra stress -c dN/dgamma and leave the general-relativity solution.
2. In the continuum, d_t H and d_t H_k are linear in (H, dH, H_k, dH_k), by the deformation algebra plus the extra force -(dN/dgamma) H. So c = 0 with H_k = 0 is preserved at every order: no extra scalar and no strong coupling. This item is argued, not computed.
3. On flat cells with kinetic term K_ij K^ij - lambda K^2 (lambda = 1 is general relativity), the read lapse with a stationary shift leaves zeta = 0 for every k != 0 solution and every lambda. For lambda != 1 the determinant is omega-free and nonzero (rigid); at lambda = 1 the null vector is gauge with zeta = 0. The projectable control (N = N(t)) instead has omega^2 = -(lambda - 1)/(3 lambda - 1) k^2.

B. Decoupling limit around a dark constant c0 (k >> H_D; a Stueckelberg tick T and labels X^a carry the broken time and space reparametrisations).

4. Isotropic cells: the first-order term is f1 = -2 dpi0/dt + (2/3) div pi and the second-order term has no (dpi^a/dt)^2. After the tick constraint the pi0 kinetic coefficient is 3 - 6 + 3 = 0 exactly (the lambda = 1 cancellation) and L2 = -(4/3) c0 k^2 pi0^2. The medium is rigid: the determinant is omega-independent and there is no mode at any omega, including no static pattern.
5. Strained cells (labels X = (1 + S) x, S = diag(d, -d, 0)), first order in d: one scalar returns with omega^2 = 2 k^2/(9 khat.S.khat) at leading order in d. One sign of khat.S.khat gives omega^2 < 0, so for either sign of d some direction is gradient-unstable, with growth rate about k sqrt(2/(9|d|)). The kinetic coefficient read from this, c0 (9/2)(khat.S.khat), is small while the gradient term is of order c0; that the cubic terms are also of order c0 is stated, not computed.
6. Every anisotropic strain tested (diagonal, axial, off-diagonal) has directions with omega^2 < 0, and omega^2 d is fixed over two decades of d.
7. With c0 = 0 exactly, the medium matrix has rank 2: the multiplier and the tick constraint; the other three directions are pure gauge, as in general relativity. There is no mode, no instability and nothing to couple.

## Derivation

Item 1. For Bianchi I cells with alpha_i = ln a_i and N = 1/sqrt(sum_i e^{-2 alpha_i}), only alpha is varied: L = (sqrt(gamma)/N) v.M.v with M = 1 - J (J the all-ones matrix). The tick energy of this L is c; it is conserved because L has no explicit tick dependence. For c = 0 the extra force from dN/dalpha is proportional to c and vanishes, so the solution is a reparametrisation of the Kasner solution.

Item 3. The linear Lagrangian is (3 - 9 lambda) zeta_t^2 + (6 lambda - 2) K zeta_t X + (1 - lambda) K^2 X^2 + 2 K zeta^2 + 4 K phi zeta with X = E_t - B and K = k^2. The read lapse sets phi = zeta - K E/3; the projectable control sets phi = 0 and drops E.

Items 4 to 7. With F = N^2 sum gamma^aa/sigma^2 written through the Stueckelberg fields, the quadratic Lagrangian is c0 (1/2) dpi.Hess(F).dpi + dlam grad(F).dpi for a plane wave (omega, k). On isotropic cells the scalar sector reduces symbolically; on strained cells the determinant of the 5x5 medium matrix is expanded to first order in d, and omega^2 is the ratio of its omega^0 and omega^2 coefficients.

## Checks

The runner ends with `TOTAL: PASS=9 FAIL=0` in about 3 s.

Exact checks and identities (checked symbolically):
- Flat sector with the read lapse: det = 32 K^6 (lambda - 1)/9, with no omega dependence; at lambda = 1 the null vector has zeta = 0. Projectable control: omega^2/k^2 = (1 - lambda)/(3 lambda - 1). The projectable kinetic coefficient 2(3 lambda - 1)/(lambda - 1) is stated.
- Isotropic cells: f1 = 2(P00 + P11 + P22)/3 - 2 p0t (label gradients P, tick derivative p0t); no (dpi^a/dt)^2 in f2; reduced L2 = -4 c0 k^2 pi0^2/3; the determinant's omega^0, omega^1, omega^2 coefficients -0.25, 0, 0 (three wavevectors checked for omega-independence).
- Strained cells, first order in d: k along x, omega^2 = k^2 (5d + 2)/(9d); k along y, omega^2 = k^2 (5d - 2)/(9d); limits of d omega^2 are +2k^2/9 and -2k^2/9. The O(1) part is not controlled at this series order.

Finite diagnostics (supplied model, finite diagnostic, no physical identification):
- Vacuum Bianchi I, integrated to tick 1.2 (rtol 1e-11): c = 0 data, c at the end 0e+00 and direction drift 0e+00; c != 0 data, relative change of c 5e-13 and direction drift 0.08.
- Strain scan, omega^2/k^2 along x, y, z and (0.6, 0.8, 0) at d = 1e-3: diagonal 223, -222, -6.67e+05, -794; axial 223, 223, -111, 223; off-diagonal 1.33e+06, 1.33e+06, -6.67e+05, 232. Every strain at d = 1e-2, 1e-3, 1e-4 has a negative entry; for the off-diagonal strain along (0.6, 0.8, 0), d omega^2 varies by less than 5% over the three values of d. Directions with khat.S.khat = 0 have |omega^2|/k^2 of order 1/d^2 rather than 1/d (stated in the runner; only the d = 1e-3 values are printed).
- c0 = 0 on a strained background (d = 1e-2): rank 2 at all six tested (omega, k) points. Only this one background is tested.

## Estimates against measurement

Estimates with supplied inputs (photon and neutrino densities today, an N_eff bound of 0.04 of radiation for the dark density, H0, the critical density, and the ambient cell strain d taken as the Newtonian potential Phi):
- Strong-coupling momentum from canonical power counting with kinetic term c0 d and cubic term c0, k_s ~ rho_D^(1/4) d^(5/8) (the exponent is not computed from the full cubic vertex): rho_D^(1/4) = 1.08e-04 eV (1/0.18 cm); k_s = 1/2.44 m for d = 1e-5 (cosmic), 1/183 m for d = 1e-8 (the Sun at the Earth), 1/2.44e+10 m for d = 1e-21 (a LIGO strain). Each is far below 1/mm (2e-4 eV); in an exactly isotropic vacuum k_s = 0.
- At linear order the sector's exchange between masses is (H_D/k)^2/d of the graviton's: with Omega_D <= 3.6e-06 and H_D = 2.7e-36 eV, about 4e-28 at 1 AU. The danger is the nonlinear endpoint of the growth, not linear tests; the growth time at the cell scale is about sqrt(9d/2) cell crossings (6.7e-03 at d = 1e-5).
- The register's split rule already makes c0 != 0 after the start: each split kicks c by (HL)^2/8 of the density, and crushes and density contrasts make per-cube constants. So zero dark constant at the start does not keep c = 0, and a selection rule that splits and crushes respect is needed. This line is a reading of the register text before its constraint clause (the current text has splits and crushes carry constraint-obeying odds into constraint-obeying odds); the runner records it with no computation.

## Boundary

Supplied: the continuum ADM limit; lambda = 1 (lambda != 1 is covered at linear order only); the decoupling limit (flat metric, k >> H_D); the strained backgrounds and tested directions; the ambient strain d ~ Phi as the lattice-coordinate anisotropy (not computed in the rules' own gauge); the power-counting exponent 5/8; every input of the estimates. Forced, given those: conservation of the dark constant; the Bianchi I slicing at c = 0; zeta = 0 at k != 0 on flat cells for every lambda; rigidity of the isotropic medium; the strained-cell dispersion at leading order in d and its gradient instability; the absence of any mode at c0 = 0. Not claimed: that the c = 0 sector is preserved at every order on the lattice (it is argued in the continuum only); the nonlinear endpoint of the growth; lattice (Regge or register) preservation of H = 0; the cubic vertex and so the strong-coupling scale beyond power counting; that the estimates are predictions beyond their supplied inputs.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the read lapse and split of the update law and the hinge sum of the response law. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/a_nonzero_dark_constant_gives_the_read_lapse_a_gradient_unstable_cell_strain_scalar_and_a_zero_dark_constant_leaves_a_slicing_of_gr_2026_10_22.py
```

Needs numpy, scipy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 3 s with about 130 MB resident, prints about 4.5 kB and ends with `TOTAL: PASS=9 FAIL=0`. It uses no random numbers; two repeated runs gave identical output apart from the elapsed-time line.
