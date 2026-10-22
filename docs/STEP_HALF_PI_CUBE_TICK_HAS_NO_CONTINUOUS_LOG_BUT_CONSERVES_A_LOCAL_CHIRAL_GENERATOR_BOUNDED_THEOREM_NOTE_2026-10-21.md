---
claim_id: step_half_pi_cube_tick_has_no_continuous_log_but_conserves_a_local_chiral_generator_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the cube tick of the candidate laws register, a wrap of quasi-energy to 2 pi needs at least ceil(pi/(2 eps)) particle-hole pairs, so step pi/2 fails the vacuum bound; at step pi/2 the tick has no continuous logarithm, but it conserves the strictly local generator H' = (i/2)[W_o, W_e], which keeps the sublattice sign exactly at every flow time and has isotropic cones at Gamma and R = pi(1,1,1), four Dirac tastes in all; on 2^3 cubes no small-band word of chirality-keeping layers gives an isotropic cone and no covariant chiral mass gaps the R doubler; no tick update, flow reading, chirality or matter content is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/step_half_pi_cube_tick_has_no_continuous_log_but_conserves_a_local_chiral_generator_2026_10_21.py
---

# The step-pi/2 cube tick has no continuous logarithm but conserves a local chiral generator

Claim type: bounded_theorem.
Primary runner: `scripts/step_half_pi_cube_tick_has_no_continuous_log_but_conserves_a_local_chiral_generator_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its cube tick has an exact sublattice chirality only at step pi/2, where the vacuum is unstable. This note asks whether the vacuum bound survives other readings of the tick, and whether a small-step update can keep an exact chirality. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the ticks or generators used.

## Statement

1. The tick and its Courant-matched photon have band maximum 2 eps, so a wrap to 2 pi needs at least ceil(pi/(2 eps)) pairs: 40 at eps = 0.04 and 1 at step pi/2.
2. At step pi/2 no continuous Hermitian H(K) satisfies exp(-iH) = U. For eps < pi/2 a quasi-local logarithm H_F exists, but eps H_F eps = -H_F, so it carries no conserved chiral charge.
3. The step-pi/2 tick conserves H' = (i/2)[W_o, W_e] = (i/2)(U - U^+). H' commutes with the sublattice sign eps and with all 24 turns, has bands +-sqrt(1 - S^2) that vanish only at Gamma and R, and has an isotropic cone of speed 1/sqrt3 block at each node, with gamma5 flipped at R. Each eps-sector holds one L and one R Weyl at each node, so there are four Dirac tastes.
4. On 2^3 cubes, small-band eps-exact words of covariant layers give no isotropic cone at Gamma, and no covariant chiral mass gaps the R doubler.

## Derivation

Rank lemma (B2). At step pi/2, U(0) = 1 and U(R) = -1 with conical fourfold bands +-w. Off the two nodes each multiplicity m_(+-,n) of the branch +-w + 2 pi n is constant. Near Gamma, Im tr(U G_n) = -(m_(+,n) - m_(-,n)) sin w; the left side is even in q and the leading term of U is odd, so m_(+,n) = m_(-,n). Near R the clusters pair (+,n) with (-,n+1), so m_(+,n) = m_(-,n+1). Then m_(+,n) is constant in n while summing to 4, which is impossible.

H'. Two half-tick generators that both anticommute with eps give only the spectral antisymmetry eps U eps = U^-1, not a conserved current. Their commutator commutes with eps. In real space each site s carries one term moving a mode from the 3 neighbours of s in its even cube to the 3 in its odd cube: straight 2-steps of amplitude 1/6 and face diagonals of amplitude 1/3, with no on-site term and no hop inside one cube. The flow exp(-i tau H') keeps eps exactly at every tau with band maximum at most tau, and its strict cone becomes a Lieb-Robinson cone.

Cube layers (C1 to C3). The site-local charges covariant under the 12 even turns are span{1, eps}. A two-layer tick whose layers are both sublattice-odd never returns a mode to its site, so the zone average of tr U is 0 and some quasi-energy reaches |w| >= pi/2. Any eps-conserving word of definite-parity layers obeys U(K+R) = sigma U(K): the Gamma content recurs at R at quasi-energy pi (sigma = -1, band reaching pi/2) or at 0 (sigma = +1, doubled light content). With the cited Floquet Nielsen-Ninomiya result applied per sector, this gives at least 4 Dirac tastes.

## Checks

The runner gives `TOTAL: PASS=15 FAIL=0` in 0.6 s.

- A1: pairs needed at eps = 0.04, 0.3, pi/4, pi/2: 40, 6, 2, 1.
- A2: two pairs at total momentum 0 at step pi/2 have mismatch to 2 pi changing sign on a fraction 0.500 of the sample (open resonance); at eps = 0.04 the maximum stays at -5.976.
- B1: at eps = 0.3 the principal log has shells 2e-1, 9e-4, 5e-6, 4e-8, 2e-10, and eps H_F eps + H_F = 3e-15.
- B2: at step pi/2 the principal log jumps by 3.628 at R (q = 1e-4) against 7e-5 at Gamma, and its shell ratios stay at least 0.24.
- B3: H' commutes with the tick, eps and the 24 turns, with H'(K+R) = -H'(K) (residual 4e-15).
- B4: cone speed 0.577350.
- B5: on a 6^3 torus the hops are {(0,0,2): 0.1667, (0,1,1): 0.3333}, intra-cube 0.
- B6: at tau = 0.04 the band maximum is 0.0400 and the shells beyond the range of H' are 2e-5, 1e-7, 8e-11.
- C1, C2, C3: charge uniqueness; on-site amplitude 2e-16 and <cos w> = 8e-17 at step pi/2; the R-image law on 60 random words (2e-15).
- C4: every K-linear term at Gamma lies in the span of Q_a = -i[C_a, G5] (rank 2 under O, 4 under T); sum_a Q_a has a 2-dimensional kernel in each eps-sector, so zero modes run along the body diagonals and there is no isotropic cone.
- C5: e^(i d G5)_o W_e e^(i d G5)_o W_e keeps eps at every d with band maximum 1.886 d, but its Gamma node has zero velocity (1e-10): quadratic, not a cone.
- D1: the chirality-keeping masses span 4 dimensions with none invariant under the 12 even turns; the register's mass term vanishes at R.
- D2: the CPT-odd term b G5 is allowed by eps and rotations; only the product PW, which keeps eps, forbids it.

Estimates (not checks). If wraps cost 2 pi hbar/tau each, the critical density over the cosmic age caps the wrap rate at 1.1e-180 per cell-tick. With a rate exp(-kappa pi/eps), eps must be at most 0.0076, 0.0152 or 0.0373 for kappa = 1, 2, ln 137, and step pi/2, at a rate near alpha^2, misses by about 1e175. With H' as the chiral generator, 4 tastes per species give N_nu = 6 after mirror gapping, 377 sigma from 2.984 +- 0.008 unless the R doubler is gapped. SU(2)_odd is as exact as SU(2)_even, so a massless W_R is allowed, against M_WR > 5 to 6.4 TeV. Every fermion mass is sublattice-odd and so needs a field charged under both SU(2)s.

## Boundary

Supplied: the tick, W, the filling of one arc, quantised links, the rate model and kappa, the unit map, the covariance group, the continuous-time reading, the choice of H', and the identification of SU(2)_even with the weak group. Cited, not rederived: the Floquet Nielsen-Ninomiya result (net chirality at 0 equals that at pi equals -W3), and the SMG conjecture. C4 is sampled; cones at non-invariant K are not excluded. Updating by the flow of H' changes the half-ticks, the strict cone premise and the record clocking, and the reading of "nearest neighbour" at the level of generator terms is not decided. Negative results: step pi/2 fails the vacuum bound in every reading tested; H' as it stands fails N_nu and W_R. No tick update, chirality or matter content is established.
