---
claim_id: a_stationary_shift_removes_the_inhomogeneous_volume_mode_of_the_read_lapse_and_a_fixed_shift_leaves_a_ghost_pair_at_c_over_sqrt3_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's read lapse N = sin(eps0)/sqrt(sum_a gamma^aa), read from the edges and not varied, in the continuum ADM limit of the hinge sum linearised around flat space with supplied lattice multipliers K (hops) and K_R (slice curvature): the lapse varies as dN/N0 = tr h/6 at first order and -h_ab h_ab/6 on traceless h at second order; a read lapse N = a^n turns the dropped Hamiltonian constraint into a conserved fluid with w = n/3 (n = 1 for the read lapse: dark radiation); the momentum constraints are kept only if d_k(N H) = 0 on isotropic cells. (A) With the shift stationary, every k != 0 solution of the linear scalar sector has zeta = 0 and the leftover direction is gauge: there is no inhomogeneous volume mode at linear order, and around a uniform dark constant the kept constraints fix its perturbation to a static pattern (4/3) c0 d^2 E, forbid transverse vector strains and leave the tensors free. (B) With the shift not varied, two scalars remain with det = -(16K^2/9)(K_R - 3 omega^2)^2: a double root omega^2 = K_R/3 (continuum omega = k/sqrt3) with kinetic signature (+,-), a ghost paired with a normal scalar, which in exact linear evolution of 16^3 lattice modes grows linearly at fixed total energy. The exclusion of (B) by vacuum decay and the tensor mass bounds for (A) are estimates with supplied inputs. Not computed: the lattice momentum constraints on edge registers, nonlinear order, the sign of the dark density from the lattice phase."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_stationary_shift_removes_the_inhomogeneous_volume_mode_of_the_read_lapse_and_a_fixed_shift_leaves_a_ghost_pair_at_c_over_sqrt3_2026_10_22.py
---

# A stationary shift removes the inhomogeneous volume mode of the read lapse, and a fixed shift leaves a ghost pair at c/sqrt3

Claim type: bounded_theorem.
Primary runner: `scripts/a_stationary_shift_removes_the_inhomogeneous_volume_mode_of_the_read_lapse_and_a_fixed_shift_leaves_a_ghost_pair_at_c_over_sqrt3_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1 in the three-law numbering) gives every cube a lapse read from its own edges, sqrt3 N rms(sqrt gamma^ii) = sin eps0, so N(gamma) = s/sqrt(Sigma) with Sigma = sum_a gamma^aa and s = sin eps0. The lapse is not varied, so the Hamiltonian constraint is not imposed by the response law (CL-3). A homogeneous volume mode then carries a conserved dark constant. This note asks whether an inhomogeneous volume (conformal) mode propagates, under the two readings of the shift that the register's text leaves open: (A) the shift is a stationary variable, so the momentum constraints hold; (B) the shift is not varied. The register's current response law takes the shift as stationary and admits only odds obeying both constraints, so its dark constant is zero; this note computes the read lapse without the constraint clause, which bears on why the clause is there. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

The lapse rule.

1. Linearised around flat cells, dN/N0 = tr h/6 exactly, with N0 = s/sqrt3: rotation-invariant at first order and blind to transverse-vector and tensor parts. On traceless h the second-order term is -N0 h_ab h_ab/6.
2. A lapse N = a^n that is read, not varied, turns the dropped constraint into a conserved fluid with w = n/3: n = 0 gives dust (the projectable Horava-Lifshitz case), n = 1 (the read lapse on isotropic cells, N proportional to the edge length) gives radiation, so the dark constant is dark radiation, and n = -3 (unimodular) gives a cosmological constant.
3. The read lapse is not a spatial scalar. The momentum constraints H_k = 0 are preserved only if d_i(H Pi^i_k) = 0 with Pi^i_k = 2 gamma_kj dN/dgamma_ij = s Sigma^(-3/2) gamma^ik = N gamma^ik/Sigma. On isotropic cells Pi = (N/3) delta, so d_k(N H) = 0: the dark pressure must be uniform. For a unimodular lapse the same identity gives the known d_k Lambda = 0.

Linear scalar sector on flat cells (h_ij = 2 zeta delta_ij + 2 d_i d_j E, shift d_i B, lapse perturbation from the read lapse).

4. Control (lapse varied, as in general relativity): the lapse equation forces zeta = 0 at every k != 0 and the rest is two gauge directions; there is no scalar degree of freedom.
5. (A) Fixed lapse, shift stationary: the shift equation is the momentum constraint d_t zeta = 0, and the E equation, which carries the dropped Hamiltonian constraint times dN/dE, gives d^2(d_t^2 zeta - K_R zeta/3) = 0. Together they force zeta = 0 at every k != 0. The leftover (E, B) direction is a gauge symmetry: a spatial shift xi combined with a time shift d_t alpha = -K xi/3 that keeps N = N(gamma). No inhomogeneous volume mode exists at linear order: no dispersion, no ghost.
6. (B) Fixed lapse, shift not varied: two scalars (zeta, E) remain with det = -(16 K^2/9)(K_R - 3 omega^2)^2, a double root omega^2 = K_R/3 (continuum omega = k/sqrt3, the Bona-Masso gauge speed sqrt(dlnN/dln sqrt(gamma)) made physical). The kinetic matrix has determinant -16 K^2 < 0, signature (+,-): a propagating ghost scalar paired with a normal one at the same frequency. The double root is a Jordan block, so the pair grows linearly in time at fixed total energy.

Background with a dark constant, case (A).

7. Around cells with a uniform dark constant c0 = N H, the kept momentum constraints fix the dark-constant perturbation to dc = (4/3) c0 d^2 E (zeta drops out), force transverse vector strains to vanish (c0 d^2 F_k = 0) and leave the tensors free. Since N H is conserved at each cell, d_t d^2 E = 0: the pattern is static and the dark constant does not propagate between cells.
8. The same constraint term gives the tensors a mass term from the dark constant, through the second-order lapse term of item 1: -N0 h_ab h_ab/6 per unit dark density, which corresponds to m^2 = (32 pi G/3) rho_D = 4 H_D^2 with H_D^2 = 8 pi G rho_D/3, in the frame of the cells. Its sign follows the sign of rho_D. The conversion to m^2 and the sign convention are stated, not lattice-checked.

## Derivation

Item 1. Expand Sigma = sum_a (gamma^{-1})^aa with gamma = 1 + e h: Sigma = 3 - e tr h + e^2 tr(h^2) + O(e^3), and N = s Sigma^(-1/2). The first order gives N0 tr h/6; on traceless h the second order collects to -N0 h_ab h_ab/6.

Item 2. For a homogeneous scale factor with L = -3 A Adot^2/A^n, the energy Adot dL/dAdot - L is conserved. Solving for Adot^2 and forming (Adot/(N A))^2 as a density, its logarithmic slope in a gives -3(1 + w) with w = n/3.

Item 3. The read lapse's failure to transform as a scalar under a spatial diffeomorphism xi, (dN/dgamma_ij) L_xi gamma_ij - xi^k d_k N, equals Pi^i_k d_i xi^k (checked at a point with a polynomial metric field and shift). The bracket of the momentum constraint with int N H is therefore int H Pi^i_k d_i xi^k, and preserving H_k = 0 for all xi requires d_i(H Pi^i_k) = 0.

Items 4 to 6. The linear Lagrangian (units 1/16 pi G) is -6 zeta_t^2 + 4 K zeta_t (E_t - B) + 2 K_R zeta^2 + 4 K_R phi zeta, with phi the lapse perturbation. The control varies phi. Case (A) substitutes phi = zeta - K E/3 from item 1 and varies B; case (B) substitutes the same phi and sets B = 0. The equations of motion at frequency omega give the matrices whose determinants and null vectors are stated.

Item 7. Write the constraint as d_i(c Sigma^-1 gamma^ik) with c = c0 + dc and expand to first order around flat cells for scalar and transverse-vector strains.

## Checks

The runner ends with `TOTAL: PASS=11 FAIL=0` in about 1 s.

Exact checks and identities (checked symbolically):
- Lapse expansion: first-order residual 0 against tr h/6; traceless second-order residual 0 against -h_ab h_ab/6.
- Fluid index: w = 0, 1/3, -1 for n = 0, 1, -3.
- Momentum-constraint identity: Pi against its closed form, maximum deviation 3e-16 at a random positive metric; the Lie-derivative identity at a point, residual 0e+00; isotropic Pi_11 at a = 2 equal to 0.384900 = N/3.
- Control: determinant 0, two gauge directions, each with zeta component 0.
- Case (A): zeta coefficients in the E and B rows -4 K (K_R - 3 omega^2)/3 and 4 i K omega; determinant 0; one null vector (zeta, E, B) = (0, -3 i omega/(K_R - 3 omega^2), 1).
- Case (B): det = -16 K^2 (K_R - 3 omega^2)^2/9; kinetic matrix determinant -16 K^2.
- Dark-constant background: dc = -(4/3) c0 (k1^2 + k2^2 + k3^2) E, that is (4/3) c0 d^2 E; transverse vector rows c0 k3^2 F1/3, c0 k3^2 F2/3, 0 for k along x3.
- The tensor mass term reuses the second-order lapse identity above; the mass formula itself is stated.

Finite diagnostics (supplied model, finite diagnostic, no physical identification):
- Case (B), exact linear evolution with K_R = K at the lowest, middle and highest lattice K on a periodic 16^3 lattice, from zeta(0) = 1e-3 at rest: K = 0.15: state norm x212 after 50 periods, x425 after 100, relative energy change 1e-11; K = 6.00: x1333, x2666, 1e-09; K = 12.00: x1885, x3770, 1e-09. The check asserts a growth ratio above 1.8 between 50 and 100 periods and conserved energy.

## Estimates against measurement

Estimates with supplied inputs (M_P = 1.22e19 GeV, cell length 2 sqrt(8 pi) l_P, the Cline-Jeon-Moore bound of about 3 MeV, the age 4.35e17 s, H0, and an N_eff bound of 0.04 of radiation):
- Case (B): a gravitationally coupled ghost with a Lorentz-violating cutoff makes the vacuum decay to photons and ghosts at Gamma ~ Lambda^8/M_P^4. With the cell cutoff Lambda = 1.2e+18 GeV the rate exceeds the bound by (Lambda/3 MeV)^8 = 7e+164; the cell-scale Jordan growth over the age of the universe is about 5e+59. Case (B) is excluded on these inputs. That the lattice terms leave the pair gapless is stated.
- Case (A): no scalar quanta, so no decay channel and no fifth force from this sector. The tensor mass today is m_g <~ 5e-36 eV against the LIGO bound 1.3e-23 eV; in the radiation era |m|/H <~ 0.40 (|m^2|/H^2 <~ 0.16), an untested superhorizon tensor effect whose sign is not fixed here.

## Boundary

Supplied: the continuum ADM limit of the hinge sum with lattice multipliers K and K_R (not the frustum hinge sum itself); flat background and linear order; the two readings of the shift; K_R = K in the time-domain diagnostic; every input of the estimates. Forced, given those: the lapse expansion; w = n/3; the momentum-constraint consistency condition; zeta = 0 at k != 0 with a stationary shift; the double ghost-normal root at omega^2 = K_R/3 with a fixed shift; the static dark-constant pattern and the vanishing of transverse vector strains around a uniform dark constant. Not claimed: lattice momentum constraints on the edge registers (Regge breaks diffeomorphisms off flat cells); nonlinear consistency with a dark constant; the sign of rho_D from the lattice phase; which shift reading the register adopts; that the estimates are predictions beyond their supplied inputs.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the read lapse of the update law and the hinge sum of the response law. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/a_stationary_shift_removes_the_inhomogeneous_volume_mode_of_the_read_lapse_and_a_fixed_shift_leaves_a_ghost_pair_at_c_over_sqrt3_2026_10_22.py
```

Needs numpy, scipy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1.5 s with about 100 MB resident, prints about 5.5 kB and ends with `TOTAL: PASS=11 FAIL=0`. Its random metric is seeded; two repeated runs gave identical output, including the elapsed-time line.
