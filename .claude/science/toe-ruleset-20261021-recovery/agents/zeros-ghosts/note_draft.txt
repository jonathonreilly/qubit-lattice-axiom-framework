---
claim_id: propagator_zeros_sit_on_the_dirac_partners_line_and_give_no_ghosts_on_a_positive_norm_lattice_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For an elementary field b Dirac-paired (mass m) with a charged partner chi: the propagator G_bb = (z - h_chi)/((z - h_b)(z - h_chi) - m^2) has its zero exactly on the partner's bare line z = h_chi, the self-energy m^2/(z - h_chi) carries the partner's pole, and det(z - H) = (z - h_chi) G_bb^-1, so the inverse of the zero is the partner's determinant (symbolic). In a free toy (two-band Wilson pair, L = 400 antiperiodic, m0 = 0.5, r = 1) the full pair's stiffness is 0 and its current weight below the pair gap is 0, while the truncation that drops the partner (full minus partner) has stiffness -1/pi and a sign-flipped low-frequency current response equal to minus the partner's: the ghost-like response is the subtracted partner. On the interacting filtered 3450 Wilson ladder (L = 3 antiperiodic, sector dimension 64444) with an exact on-site U(1) twist on every hop, the twisted Hamiltonian is Hermitian to 2.8e-17, the Kohn decomposition matches the ground-energy curvature to 2.7e-3 (stiffness about 16.7), every current spectral weight is non-negative (minimum at roundoff) and the weights sum to the norm, at couplings g = 0, 8, 16; the stiffness ratio stays positive (1.0, 0.991, 0.959). An estimate compares the measured R ratio near 30-35 GeV (about 3.9) with three response classes. Supplied model, finite diagnostic: free toy masses, the 3450 charges, the six-fermion interaction vectors, the two-site filter, L = 3, the twist on one charge; L = 3 cannot separate light and mirror shares; the Golterman-Shamir argument is engaged at the level of its abstract only."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/propagator_zeros_sit_on_the_dirac_partners_line_and_give_no_ghosts_on_a_positive_norm_lattice_2026_10_22.py
---

# Propagator zeros sit on the Dirac partner's line and give no ghosts on a positive-norm lattice

Claim type: bounded_theorem.
Primary runner: `scripts/propagator_zeros_sit_on_the_dirac_partners_line_and_give_no_ghosts_on_a_positive_norm_lattice_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. One route to a chiral spectrum on the lattice gaps the mirror fields by interactions (symmetric mass generation) rather than by a bilinear mass. Golterman and Shamir (arXiv:2311.12790) argue that in such a gapped mirror sector the fermion propagator develops zeros, and that once the sector is gauged these zeros act like ghost states. That reading is taken here from the paper's abstract and summary only; its detailed derivations were not reproduced. This note asks what a propagator zero is in a positive-norm lattice model, and whether the gauged current response can carry negative spectral weight. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Exact algebra (symbolic).

1. Let b (bare line h_b) be Dirac-paired with mass m to a charged partner chi (bare line h_chi). Then G_bb = (z - h_chi)/((z - h_b)(z - h_chi) - m^2): the zero of G_bb sits exactly on the partner's bare line z = h_chi(k), and the self-energy Sigma = m^2/(z - h_chi) has the partner's pole. A zero is the pole of the composite partner, not an absence.
2. det(z - H) = (z - h_chi) G_bb^-1. The nonlocal kernel m^2 psi (1/D^chi) psi obtained by integrating out chi has determinant det(full)/det(D^chi): the inverse of the zero ("bosonic spinor" factor) is exactly the dropped partner's fermion determinant. Keeping the partner, the gauged sector is an ordinary massive Dirac fermion.

B. Free toy (two-band Wilson pair, L = 400 antiperiodic, m0 = 0.5, r = 1, charge 1 on b and chi, Peierls twist).

3. The gapped pair has stiffness (the 1+1D photon mass squared per e^2) D_full = 0: a gapped charged sector decouples.
4. The partner alone (a naive chain with two Weyl nodes) has D_chi = 1/pi. The truncation that keeps the elementary field and drops the partner, D_full - D_chi, is -1/pi: a negative stiffness, which is exactly minus the subtracted partner's.
5. At q = 2 pi/L the full pair has no current spectral weight below its gap; the partner alone has positive weight at omega about q. The truncated response, full minus partner, therefore has negative absorptive weight at low omega, and that weight is the partner's particle-hole line with its sign removed.

C. Interacting filtered 3450 Wilson ladder (four Weyl fields with charges Q_A = (3, 4, 5, 0), Q_B = (2, 1, 2, -1), chiralities (-1, -1, 1, 1); two six-fermion interaction patterns on the filtered leg; two-site filter (1 + e^{ik})/2; L = 3 antiperiodic, zone corners kept; sector (Q_A, Q_B, K) = (36, 12, 0), dimension 64444), with an exact U(1) twist in Q_A on every hop (the free terms, the filter and the interaction phases).

6. The twisted Hamiltonian is Hermitian and keeps (Q_A, Q_B, K) at every twist, so the gauge coupling is exact on the lattice.
7. At couplings g = 0, 8, 16 the Kohn decomposition D = L(<d^2 H> - 2 <J (H - E0)^-1 J>) equals the curvature of E0(theta): the induced gauge action is the current spectral sum.
8. Every current spectral weight of J|0> is non-negative and the weights sum to |J|0>|^2, as positivity of a positive-norm Hilbert space requires (Kallen-Lehmann). No negative-weight (ghost) state occurs. The runner states, and does not compute, that for an update step U = exp(-i eps H) the same weights give a positive-definite Toeplitz autocorrelation.
9. The stiffness ratio D(g)/D(0) stays positive at g = 8, 16. At L = 3 the light and mirror shares cannot be separated, so this bounds the mirror share's sign class; it does not decide between decoupling and sign flip.

## Derivation

Items 1-2 invert the 2 x 2 matrix z - H with sympy. Items 3-4 take second differences of the filled-band energies in the twist (step 0.05). Item 5 sums squared current matrix elements between occupied and empty bands at momenta k and k + q, and separately the partner's node particle-hole terms. Items 6-9 build the ladder sector by Jordan-Wigner bit-strings (inlined from an earlier filtered-ladder computation, with the twist added), find E0 and the first excited state by Lanczos at twists 0 and +-0.02, solve (H - E0) y = J|0> by conjugate gradients for the paramagnetic part, and obtain the spectral weights of J|0> from an 80-step Lanczos tridiagonalisation.

## Finite checks

Exact or closed-form checks (the runner asserts each):
- G_bb, Sigma and det(z - H) = (z - h_chi) G_bb^-1: symbolic identities.
- Free toy: D_full = 0.0e+00 (asserted below 1e-6), pair gap 1.00; D_chi = 0.31831 against 1/pi = 0.31831; D_full - D_chi = -0.31831.
- Free toy current weight: full pair below the gap 0.0e+00 (total 5.000e-01); partner at the node 5.00e-03.
- Ladder Hermiticity defect 2.8e-17.

Finite diagnostics (supplied model, finite diagnostic):

| g | gap | D_curv | D_Kohn | diamagnetic | paramagnetic | J weight below omega = 1 | lowest J pole |
|---|---|---|---|---|---|---|---|
| 0 | 2.000 | 16.6664 | 16.6690 | 33.331 | 16.662 | 0.000 | 2.000 |
| 8 | 1.961 | 16.5207 | 16.5234 | 33.328 | 16.805 | 0.000 | 1.961 |
| 16 | 1.712 | 15.9814 | 15.9840 | 33.428 | 17.444 | 0.000 | 1.712 |

- max |D_curv - D_Kohn| = 2.7e-03 (asserted below 2e-3 relative).
- Minimum spectral weight at roundoff (order 1e-35; this printed digit varies between runs because the Lanczos start vectors are not seeded); weight sum equal to |J|0>|^2 to 1e-8.
- D(g)/D(0) = 1.0, 0.991, 0.959.

## Estimates against measurement

The absorptive part of the electromagnetic current two-point function is measured as R(e+e- -> hadrons). Near sqrt(s) = 30-35 GeV (five quark flavours, alpha_s = 0.145, both supplied):
- decoupling class (light chiral content, mirror gapped above): (11/3)(1 + alpha_s/pi) = 3.84;
- ghost class (zeros cancel the light share): 0;
- light mirror: 7.67.

Measured about 3.9 (PETRA/TRISTAN, quoted approximately, uncertainty taken as 0.05). The runner asserts the decoupling class within 3 sigma and the other two more than 50 sigma away. This is an estimate with supplied inputs.

## Boundary

Not claimed: any statement about the full Golterman-Shamir analysis beyond its abstract-level summary; a separation of the light and mirror shares of the stiffness (L = 3 is too small); the thermodynamic or continuum limit of the ladder; the interacting model in more than 1+1 dimensions; any statement about the update law's finite step beyond the stated Toeplitz remark; a derivation of the 3450 charges or the interaction vectors from the register.

## Supplied vs forced

Supplied: the Wilson ladder, the 3450 charges, the six-fermion interaction vectors, the two-site filter, the couplings g, L = 3 antiperiodic, the twist on Q_A; free toy masses m0 = 0.5, r = 1; alpha_s and the measured R. Forced, given those: the location of the zero on the partner's line; the determinant identity; the vanishing stiffness of the gapped free pair and the negative stiffness of the truncation; the exactness of the lattice gauge twist; the Kohn equality; the non-negativity of every current spectral weight on the positive-norm space.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the unitary update law (positive-norm Hilbert space, U = exp(-i eps H)) and its on-site gauge registers. Zero premise weight; results using it are conditional on it.
- Literature: M. Golterman and Y. Shamir, arXiv:2311.12790 (read at abstract/summary level only).

## How to run

```
python3 scripts/propagator_zeros_sit_on_the_dirac_partners_line_and_give_no_ghosts_on_a_positive_norm_lattice_2026_10_22.py
```

Needs numpy (2.0 or later, for `np.bitwise_count`), scipy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 7 to 8 s with about 260 MB resident, prints about 4.1 kB and ends with `TOTAL: PASS=10 FAIL=0`. Two repeated runs gave identical output apart from the build and elapsed time lines and the roundoff-level minimum spectral weight (2.4e-35 against 3.2e-36).
