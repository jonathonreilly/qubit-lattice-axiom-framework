---
claim_id: induced_gauge_couplings_from_three_families_on_the_hypercube_are_strong_at_the_cell_and_miss_alpha_gut_tenfold_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "On the four-dimensional Euclidean hypercubic reading of the update (Wilson r = 1 and naive/staggered lattice fermions, link phases and a TT vierbein on the hops), with no bare link plaquette term, the one-loop induced gauge coupling per Dirac of unit charge is 1/e^2 = (1/(6 pi^2))[ln(1/(a mu)) + C] with C = 0.793 (Wilson) and 0.311 (staggered, per taste), and the induced Einstein term is 1/(16 pi G) = c_G/a^2 per Dirac with c_G = 0.01032 (Wilson) and 0.004966 (staggered), both with the sign of GR. For three families of 16 Weyl (sum of Dynkin indices 6 per factor, equal for SU(3), SU(2), GUT-normalised U(1)_Y and Spin(10)) and the cutoff fixed by measured G, the induced 1/alpha is 0.50 (Wilson) or 0.20 (staggered) at the cell and about 4.2 at 1e16 GeV from fermion loops alone, against 34-51 and 38-46 from the measured couplings run with the Standard Model; the non-abelian factors are asymptotically free and would run strong at about 1e18 GeV. The Sakharov ratio alpha(1/a) a^2/G = 192 pi^2 c_G/C (24.7 or 30.3) is independent of the family count and exceeds the measured value at the same scale by a factor of 67-103 (Wilson). So the rule that the gauge kinetic term is wholly induced by the cell's matter fails measurement. Supplied model, finite diagnostic: the lattice actions and couplings to links and vierbein, the family count, the matching scale mu = 1/a, the measured G and alpha_i(M_Z) and the Standard Model one-loop coefficients."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/induced_gauge_couplings_from_three_families_on_the_hypercube_are_strong_at_the_cell_and_miss_alpha_gut_tenfold_2026_10_22.py
---

# Induced gauge couplings from three families on the hypercube are strong at the cell and miss alpha_GUT tenfold

Claim type: bounded_theorem.
Primary runner: `scripts/induced_gauge_couplings_from_three_families_on_the_hypercube_are_strong_at_the_cell_and_miss_alpha_gut_tenfold_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. A working ruleset reads its relabelling-only clause as saying that links carry no bare kinetic term: the gauge kinetic term, like the Einstein term, would then be induced by the loops of the lattice fermions (Sakharov's induced gravity, applied to the links as well). If so, the cell's matter content fixes 1/g^2 at the cell with no free parameter, and the same loops fix G, so the cutoff is not free either. This note computes both numbers exactly on the lattice and compares them with measurement. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Machinery (exact).

1. The second-order term of -ln det D for a link-phase wave A_1(x_2) = eps cos(q x_2) equals the momentum-space tadpole plus bubble with the lattice vertices. A real-space log det on a 12-site chain agrees to 1.6e-6. Gauge invariance makes the q = 0 term vanish.
2. The q^2 coefficient is an exact Brillouin-zone integral, -(1/2) tr(dS V dS V) with dS the k_2-derivative of the propagator. Splitting it with a smooth radial bump around the light corner makes it converge spectrally down to m = 1e-5. The result does not depend on the bump or the grid, to 5e-5.
3. The naive integrand is pi-periodic in every direction, because gamma_mu -> -gamma_mu is a Clifford automorphism. So each doubler contributes equally, and a staggered taste equals one naive doubler, for both the link and the TT vertex.
4. At one loop the induced term is quadratic in the gauge field, so for any group 1/g^2 = sum over representations of T(R) times the U(1) value per unit charge^2. On the hypercube F_munu F_munu is the only gauge-invariant term of dimension four, so the induced Maxwell term is Lorentz invariant. This differs from the cube tick, where the electric and magnetic parts differ (see the cube-tick sea note).
5. For one family of 16 Weyl the index sums are T = 2 for SU(3), SU(2), GUT-normalised U(1)_Y and Spin(10). The induced couplings are therefore equal at the cell for every lattice constant C, which gives sin^2 theta_W = 3/8 there.
6. An induced non-abelian coupling stays weak below the cell only if sum T_W >= (11/2) C_A. That needs 16.5 for SU(3), 11 for SU(2) and 44 for Spin(10). Three families give 6.

B. Lattice constants (finite diagnostics, m -> 0). Per Dirac of unit charge, 1/e^2 = (1/(6 pi^2))[ln(1/(a mu)) + C], and 1/(16 pi G) = c_G/a^2.

- Wilson r = 1. The log coefficient is 1.0010 times 1/(6 pi^2), and C = 0.7925 at m = 1e-5 (0.7902 at 1e-4). The approach is slow, through m ln m terms: C(0.3) = -0.009 and C(0.01) = 0.659. The TT term is c_G = 0.010324, which equals the heat-kernel form Lambda^2/(96 pi^2) with Lambda = 3.13/a, close to pi/a.
- Staggered, per taste. The log coefficient is 1.0000 and C = 0.3108. The TT term is c_G = 0.004966, an effective Lambda of 2.17/a.
- C is regulator-dependent, but it is O(1) in both cases. So 1/g^2 at the cell is a lattice number of order C/(12 pi^2) per unit index.

## Against measurement (estimates)

These use the measured G, alpha_i(M_Z), the Standard Model one-loop b_i and the matching scale mu = 1/a. Three families give sum T = 6 and 24 Dirac-equivalents.

- Cutoff from G. Setting 1/(16 pi G) = 24 c_G/a^2 gives 1/a = 3.46e18 GeV (Wilson) or 4.99e18 GeV (staggered). The register's unit map gives 2.44e18 GeV.
- At the cell, 1/alpha = (2/pi) C = 0.505 (Wilson) or 0.198 (staggered), so alpha is about 2 to 5. The measured couplings run up to 3.5e18 GeV give 1/alpha_1,2,3 = 34.1, 48.8 and 51.0.
- At 1e16 GeV, fermion loops alone give 1/alpha = 4.23 (Wilson) or 4.15 (staggered), against 37.9, 45.9 and 44.5. The induced coupling is too strong by a factor of about ten.
- With the gauge fields' own loops below the cell, b0 = 7, 3.33 and 25.3 for SU(3), SU(2) and Spin(10). The induced couplings then run strong at 2.2e18, 1.3e18 and 3.1e18 GeV. Colour would confine at the cell, not at 0.2 GeV.
- The Sakharov ratio alpha(1/a) a^2/G = 192 pi^2 c_G/C is 24.7 (Wilson) or 30.3 (staggered), independent of the family count. The measured alpha at the same scale gives 0.24 to 0.37.
- Reaching the measured 1/alpha at the cell would need sum T = 3 pi/(alpha C), about 406 to 607 units of charged index for Wilson (2.55 times more for staggered). That is 200 to 300 families' worth of charged cell-scale content, fermion or link register, before the cutoff shift that the extra content would itself cause.

## Boundary

Supplied: the 4D Euclidean hypercubic reading of the update rather than the cube tick, the Wilson and naive actions, the link phase on the hops, the vierbein on the hops with (1 -+ h) on the Wilson terms, the family count N_f = 3, the matching scale mu = 1/a (choosing pi/a shifts the logarithm by 1.14), one loop, and all measured numbers.

Not computed: the cube tick itself. Its Maxwell constants C_E = 1.38 and C_B = 1.26 per species of two Dirac copies, from the cube-tick sea note, are also O(1) and do not change the conclusion. Also not computed: gapped mirror or rishon content, which adds about C per unit index, and two loops.

The negative is robust because it needs C of about 70, or hundreds of families, and no O(1) lattice constant supplies that. The rule "no bare link term" fails measurement. No adopted clause changes here.
