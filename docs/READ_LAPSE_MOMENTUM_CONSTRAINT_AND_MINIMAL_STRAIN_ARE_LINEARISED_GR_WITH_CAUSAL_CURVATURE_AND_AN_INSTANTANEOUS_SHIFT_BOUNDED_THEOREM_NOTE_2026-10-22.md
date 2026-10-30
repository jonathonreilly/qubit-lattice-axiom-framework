---
claim_id: read_lapse_momentum_constraint_and_minimal_strain_are_linearised_gr_with_causal_curvature_and_an_instantaneous_shift_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "At linear order on flat cells (continuum-form ADM quadratic action with the consistent lattice derivative d_j -> i 2 sin(k_j/2), conserved test sources, k along a lattice axis with any K = |kt|^2 > 0, by rotation covariance of the construction any k != 0): with the update law's read lapse (dN = tr h/6), the shift varied so that its equation is the momentum constraint including matter, and the minimal-strain shift (d_j of the edge rate = 0), the scalar and vector sectors have no mode at any omega != 0 and the tensor sector keeps omega^2 = K twice: no scalar, no vector, no ghost (with the shift held at zero the ghost-normal double root omega^2 = K/3 returns); with four independent lattice multipliers the scalar sector still has no mode. For every conserved source the system has a unique solution that obeys the dropped Hamiltonian constraint and all ten linearised Einstein equations, and its linearised Riemann tensor equals the de Donder (covariant, retarded) one, so curvature observables are causal. The shift solves the elliptic equation (K delta + kt kt^T) beta = source with non-polynomial inverse (delta - kt kt^T/2K)/K, so it and every edge value read in its frame respond instantaneously; the scalar part of the minimal-strain edges is the Bardeen potential rho/(4K). Local drivers: a Gamma-driver with the read lapse has gauge speeds omega^2 = K(1 + 4 mu)/3 and mu K (causal iff mu <= 1/2), a strain driver K(1 + 6 mu)/3 and mu K (causal iff mu <= 1/3); damping makes every gauge root decay and driver modes are pure gauge. Supplied model, finite diagnostic: linearised continuum-form ADM, test sources, a 1D dispersion toy and supplied driver forms; no register-level insertion into the update law, no nonlinear minimal strain."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/read_lapse_momentum_constraint_and_minimal_strain_are_linearised_gr_with_causal_curvature_and_an_instantaneous_shift_2026_10_22.py
---

# The read lapse, the momentum constraint and minimal strain are linearised GR, with causal curvature and an instantaneous shift

Claim type: bounded_theorem.
Primary runner: `scripts/read_lapse_momentum_constraint_and_minimal_strain_are_linearised_gr_with_causal_curvature_and_an_instantaneous_shift_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1 in the three-law numbering) reads the lapse from each cube's edges with one fixed step, which at linear order is dN = tr h/6 (Bona-Masso f = 1/3). Its response law (CL-3) takes the shift as the multiplier of the momentum constraint, matter included, in the minimal-strain frame. An earlier result showed that the tied lapse leaves the shift free and that a momentum constraint built from the edges alone excludes moving sources. This note asks what the resulting system is at linear order: which modes propagate, whether it agrees with general relativity with matter, whether its observables are causal, and how fast the shift and edge values read in its frame respond. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Mode count (units 16 pi G = 1; k along z with any lattice K = kappa^2).

1. Control: the quadratic ADM form is diffeomorphism invariant (4 gauge directions at generic omega, k) and the tensor modes obey omega^2 = K.
2. With the read lapse, the shift varied (momentum constraint kept) and minimal strain, the helicity sectors decouple; the scalar and vector sectors have no mode at any omega != 0 and any K > 0 (the gcd of all maximal minors is a monomial in omega and kappa); the tensor sector keeps omega^2 = K twice. No propagating scalar, no ghost, no vector.
3. Control: the same lapse with the shift held at zero and its equation dropped gives the double root omega^2 = K/3, the ghost-normal pair; the method sees ghosts when they exist.
4. At omega = 0 minimal strain is empty; the static kernel is a slice tilt t -> t + f(x) (a static longitudinal shift, which leaves the read lapse unchanged) and a static transverse relabelling: initial-data gauge, not modes.
5. With four independent positive lattice multipliers (hops, curvature, lapse, gauge) the scalar sector still has no mode at omega != 0.

B. Matter, the dropped Hamiltonian constraint, and causality.

6. For every conserved source (built from free stresses S_ij) the nine equations, including the momentum constraint with matter, plus minimal strain have a unique solution; it satisfies the dropped Hamiltonian constraint and all ten linearised Einstein equations. It is the general-relativity solution in the minimal-strain, fixed-step slicing.
7. Control: de Donder gauge gives hbar_mu nu = c T_mu nu/(omega^2 - K) with one constant c for all components, a covariant, retarded response.
8. The linearised Riemann tensor of the minimal-strain solution equals the de Donder one for every source and every K (12 independent components checked along z). Tidal fields, frame dragging and waves are retarded; gauge-invariant observables do not see the elliptic shift. (Extension to every lattice direction is by rotation covariance of the construction in kt, stated, not computed.)
9. Minimal strain is the elliptic equation (K delta + kt kt^T) beta = i kt tr(kappa) - J, with inverse (delta - kt kt^T/2K)/K, not polynomial in kt: the shift at a point depends instantaneously on the whole slice (a Kelvin-type kernel), sourced by the matter current through the momentum constraint.
10. On a 32^3 periodic lattice, the minimal-strain shift of a unit current at the origin is already nonzero 8 cubes away, falling roughly as 1/r, while the edge light cone advances sin(eps0)/sqrt3 <= 0.022 cube per tick: the shift, and every edge value read in its frame, changes outside the cone. (The lattice computation is the elliptic solve; the per-tick reading is the comparison with the cone.)
11. The minimal-strain edges are transverse (kt_j h_ij = 0), and their scalar part is the gauge-invariant Bardeen potential Psi = rho/(4K), a Poisson functional of the energy density. So the floor and the split trigger, read in this frame, respond at once to distant rearrangements.

C. Local hyperbolic alternatives (driver equations; sectors along z, every K).

12. A Gamma-driver with the read lapse has one longitudinal gauge pair at omega^2 = K(1 + 4 mu)/3 and a transverse pair at omega^2 = mu K; the standard mu = 3/4 moves gauge at 2/sqrt3 times c; every gauge speed is at most c iff mu <= 1/2.
13. A strain driver (which relaxes to minimal strain) has omega^2 = K(1 + 6 mu)/3 and mu K; every gauge speed is at most c iff mu <= 1/3 (at mu = 1/3 the longitudinal speed is exactly c).
14. With damping eta > 0 every gauge root has Im omega < 0; as eta grows the slow root tends to the lapse speed 1/sqrt3.
15. The driver modes are pure gauge: their linearised Riemann tensor vanishes.

D. Variational and Euler-Lagrange readings of minimal strain (uniform expansion).

16. Uniform expansion has no component along any interior site displacement, so the Euler-Lagrange form is satisfied by zero shift; but on an open block the least summed squared edge rate removes it completely with beta = -H x (a dilation is a displacement gradient), so the variational reading would freeze every edge in an expanding region. On the torus the two readings agree (beta = 0).
17. The Euler-Lagrange operator K delta + kt kt^T is positive at every k != 0. Its kernel on Z^3 is the affine shifts, and boundedness (at most one cube per tick) leaves only uniform translations, so the cap makes the elliptic shift unique on the infinite lattice. (Positivity is computed on the 32^3 grid; the kernel and the uniqueness argument are stated, not computed.)

E. Gauge carries no signal (ring of 256 cells).

18. A displacement generated by the constraint itself leaves the relational state (matter relative to edges) unchanged to machine precision; a matter transport whose dispersion differs from the edge displacement at O(k^2) (lattice momentum sin p against p) leaks linearly in the shift, at a size set by the packet's momentum spread.

## Derivation

Section A builds the linearised ADM Lagrangian (1/4)(|kappa_ij|^2 - |tr kappa|^2) plus the curvature terms and the lapse times the linearised scalar curvature as a 10 x 10 symbolic Hermitian form in (h_ij, beta_i, phi) with d_j -> i kt_j, inserts phi = tr h/6, projects onto helicity sectors about z, imposes minimal strain (h13 = h23 = h33 = 0 for omega != 0) and takes the gcd of maximal minors with sympy; item 5 repeats the scalar sector with four independent symbols. Section B solves the system with symbolic conserved sources, substitutes into GR's ten equations, solves de Donder gauge for comparison, and compares 12 linearised Riemann components. Item 10 solves the elliptic shift by FFT on 32^3. Section C appends the driver rows and factors the sector determinants, with numerical roots for item 14. Section D solves least squares for the displacement field of a 6^3 block of Z^3 edges (axis edges and even face diagonals), open and periodic. Section E evolves a Gaussian packet on a 256-cell ring.

## Finite checks

Exact or closed-form checks (the runner asserts each; all symbolic unless stated):
- Control: 4 gauge directions at (omega, kappa) = (7/5, 3/4); tensor determinant (kappa - omega)^2 (kappa + omega)^2/8.
- Read lapse, momentum constraint, minimal strain: sectors decouple; scalar gcd kappa omega; vector gcd kappa; tensor determinant (kappa - omega)^2 (kappa + omega)^2/4.
- Shift held at zero: determinant -(kappa^2 - 3 omega^2)^2/36.
- Static kernel: scalar (h11 + h22, h33, b3) = (0, 0, 1); vector (h13, b1) = (1, 0).
- Four independent multipliers: gcd of 3 x 3 minors K K_g omega.
- Conserved sources: 1 solution; Hamiltonian residual 0; all ten Einstein equations hold.
- de Donder: one constant, c = -1.
- 12 Riemann components equal (residual 0).
- (K delta + kt kt^T)^-1 = (delta - kt kt^T/2K)/K exactly; solved shift residual 0.
- Bardeen potential: Psi = S33/(4 omega^2), rho = S33 kappa^2/omega^2, so Psi = rho/(4K).
- Gamma-driver: scalar factor omega^2 (4 kappa^2 mu + kappa^2 - 3 omega^2)/4, vector omega (kappa^2 mu - omega^2). Strain driver: omega^2 (6 kappa^2 mu + kappa^2 - 3 omega^2)/6, omega (kappa^2 mu - omega^2).
- Driver modes: kernel dimension 1, Riemann zero.
- Uniform expansion on an open 6^3 block: least-squares residual 4.2e-15, interior J^T rate 3e-20, shift spread 0.0050; periodic residual 1.000.
- Euler-Lagrange operator minimum eigenvalue above 0.03 on the 32^3 grid (the runner's label gives 4 sin^2(pi/32) = 0.038).
- Constraint-generated displacement leak 0e+00.

Finite diagnostics (supplied model, finite diagnostic, no physical identification):
- Elliptic shift on 32^3: |beta_x| = 0.0381, 0.0147, 0.0046 at r = 2, 4, 8 cubes; light moves 0.0216 cube per tick at eps0 = 0.0375.
- Damped strain driver (K = 1, mu = 1/3): eta = 1/2: roots -0.96 - 0.16i, -0.18i, +0.96 - 0.16i; eta = 5: -0.58 - 0.07i, -4.86i, +0.58 - 0.07i; eta = 50: -0.58 - 0.01i, -49.99i, +0.58 - 0.01i.
- Mismatched transport leak: b = 0.5: 1.51e-03; b = 0.25: 7.55e-04; packet width doubled: 7.13e-04.

Gauge speeds of the drivers (from the factored determinants):

| driver | longitudinal omega^2/K | transverse omega^2/K | all speeds <= c iff |
|---|---|---|---|
| Gamma-driver with read lapse | (1 + 4 mu)/3 | mu | mu <= 1/2 |
| strain driver | (1 + 6 mu)/3 | mu | mu <= 1/3 |
| strain driver, eta -> infinity | slow root -> 1/3 | | |

## Estimates against measurement

Estimates with supplied inputs (eps0 = 0.0075 and 0.0375, Painleve-Gullstrand shift sqrt(r_s/r) c, G = 6.674e-11, a 1 kg mass moved 1 m and read 1 m away):
- The one-cube-per-tick cap is 231 c (eps0 = 0.0075) and 46 c (eps0 = 0.0375); it binds only at r < (sin^2 eps0/3) r_s, 1.87e-05 to 4.69e-04 r_s, deep inside horizons, matching the shift-saturation radius found for Oppenheimer-Snyder collapse. It does not bind in cosmology (Euler-Lagrange reading, beta = 0).
- An instantaneous frame-read edge change from a laboratory rearrangement is of order G m/(c^2 r) = 7.4e-28 per edge: acausal in principle, far below any test.

## Boundary

Supplied: the continuum-form linearised ADM quadratic action with the consistent lattice derivative (item 5 relaxes the single multiplier); flat cells; conserved test sources; the 1D dispersion toy of section E; the Gamma and strain driver forms with mu and eta; the estimates' inputs. Forced, given those: the absence of scalar, vector and ghost modes at every sampled K with the read lapse, momentum constraint and minimal strain; the return of the ghost pair when the shift is held at zero; the agreement with all of linearised GR for conserved sources; the equality of the Riemann tensor with the retarded de Donder one; the elliptic, instantaneous shift and the Bardeen-potential scalar part of the frame-read edges; the driver gauge speeds and causality bounds; the open-block freezing of the variational reading. Not claimed: insertion into the update law at register level; nonlinear minimal strain; the lattice momentum-constraint algebra off flat cells; a choice between minimal strain and a hyperbolic driver; any statement beyond linear order.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's fixed-step (read) lapse and one-cube-per-tick cap; the response law's momentum constraint with matter and the minimal-strain shift. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/read_lapse_momentum_constraint_and_minimal_strain_are_linearised_gr_with_causal_curvature_and_an_instantaneous_shift_2026_10_22.py
```

Needs numpy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1 s with about 120 MB resident, prints about 4.6 kB and ends with `TOTAL: PASS=20 FAIL=0`. It uses no random draws; two repeated runs gave identical output apart from the elapsed-time line.
