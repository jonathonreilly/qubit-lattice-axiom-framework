---
claim_id: the_cube_tick_sea_induces_neither_a_lorentz_invariant_maxwell_term_nor_a_newtonian_sector_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the free filled sea of the register's cube tick with supplied site-phase links and a supplied reading of edge lengths, the induced Maxwell term has the standard logarithm 2/(6 pi^2) per species but electric and magnetic finite parts that differ for every eps < pi/2, the induced static scalar sector depends only on Phi + Psi and so has no Newtonian part, and the massless vacuum phase is stationary only at eps = pi/2, where light decouples from the lapse; so the response law cannot be reduced to stationarity of the matter phase alone; no adopted response clause is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_cube_tick_sea_induces_neither_a_lorentz_invariant_maxwell_term_nor_a_newtonian_sector_2026_10_21.py
---

# The cube tick's sea induces neither a Lorentz-invariant Maxwell term nor a Newtonian sector

Claim type: bounded_theorem.
Primary runner: `scripts/the_cube_tick_sea_induces_neither_a_lorentz_invariant_maxwell_term_nor_a_newtonian_sector_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its response law has three parts: the matter phase, the hinge sum and the links' plaquette phase. This note asks whether the last two can be induced by the free filled sea of the register's cube tick, so that the law reduces to stationarity of the matter phase alone. They cannot. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the readings or fields used.

## Theorems

1. In the cube tick U(K) + U(K)^dag = 2 cos w times the identity, so the filled-sea projector has a closed form.
2. Every link response satisfies F(eps, mu) = -F(pi/2 - mu/2, pi - 2 eps), which swaps the light-cone mass mu with the pi-cone mass pi - 2 eps. The induced 1/e^2 vanishes at mu = pi - 2 eps and is a ghost beyond it.
3. det U is unchanged at second order, so filling the other half of the spectrum flips the sign of every induced coefficient. Positive-energy photons select the usual filling.
4. For a massless species the vacuum phase Phi(eps) per block per tick decreases strictly and is stationary only at eps = pi/2. There Phi = -2 pi for every uniform hop anisotropy and every mode has dw/deps = 0, so the zero is a decoupling of light from the lapse, not a cancellation.
5. In a massless tick the static lapse Phi and spatial conformal factor Psi enter only through N/l, about 1 + Phi + Psi. So the induced k^2 scalar action depends on Phi + Psi alone and the vacuum stress is traceless. Einstein's static sector needs no Phi^2 term and a nonzero grad Phi . grad Psi term, so it cannot be induced.
6. In the Hamiltonian limit eps -> 0, second-order perturbation theory makes the lapse response at most 0 at every q, so an induced lapse term is never attractive.

## Checks

The runner gives 17 PASS and 0 FAIL. These are finite diagnostics of a supplied free sea, with exact sums on twisted tori extrapolated in q -> 0 and then m -> 0.

- All 8 bands obey the band law and the projector is rank 4, to 2.6e-13. Bloch second-order sums match exact diagonalisation of an (8 site)^3 torus to 1.9e-7. The determinant identity holds to 6.7e-9, a pure-gauge link field gives 3.8e-13 against 1.6, and the exchange antisymmetry holds to 2.5e-15 (3.0e-13 at the exchange point).
- Maxwell term (one species is two Dirac copies): the log coefficient is 0.986 (electric) and 1.021 (magnetic) times 2/(6 pi^2) at eps = 0.05. The finite parts extrapolate to C_E = 1.3807 and C_B = 1.2647, a split of 0.1160, so the induced photon speed squared is c^2 (L + C_B)/(L + C_E). At m = 0.35 the split is 0.1443, 0.1429, 0.0845 and 0.0247 at eps = 0.05, 0.6, 1.2 and 1.4. It stays positive for every eps < pi/2. Near pi/2 the pi-cone acts as a Pauli-Villars image: C_E - ln(m_pi) = +0.038 at eps = 1.4. Beyond the exchange point 1/e^2 is negative (-0.0145, -0.0135).
- Gravity (units c0 = sin(eps)/sqrt 3 per block per h^2): the TT gradient term is R2 = 0.00945 and 0.00956 at m = 0.35 and 0.25, extrapolating to 0.00967 (0.00998 with cube sampling), the sign of GR. The uniform TT term is R0 = -0.3137. In the static scalar sector the gradient terms are -0.00007 (lapse, bond sampling), +0.00077 (dilation) and -0.07187 (lapse, cube sampling), where Einstein needs (0, -4, +4) times R2_TT. At eps = 1.45, R0 = -0.1066 and R2 = 0.00202.
- Vacuum phase: eps dPhi/deps runs from -0.110 at eps = 0.02 through -3.831 at 0.90 to 0 at pi/2. At pi/2, Phi + 2 pi = 0 and max dw/deps = 0, against 2.00 at eps = 0.04. Theorem 4 holds to 8.9e-16 for anisotropic hops. With mass, Phi + 2 pi = -I0 mu^2 with I0 = 1.1563, and the Hamiltonian-limit sea energy is -9.5504 c0 per block.

## Against measurement (estimates)

Supplied Standard Model charges and masses, measured hadronic running and a = sqrt(8 pi) l_P.

- alpha: the needed 1/e^2 is 10.905. As eps -> 0 one light copy gives 5.926 (1/alpha = 74.5) and two copies 11.853 (1/alpha = 148.9). Two copies match only at eps = pi/2 - 0.0344, with the pi-cone at 1.5e17 GeV, outside the register's bound eps < 0.04. One light and one heavy copy match with a second-copy mass near 479 GeV.
- Photon speed: a fully induced photon has dc/c = -1.4e-3, and a bare photon plus one loop with one copy -7.2e-4, against |dc/c| < 1e-11 from LEP electrons at 104.5 GeV. A fully induced photon misses by more than 1e6.
- G: the induced TT term is 0.00483 c0 per Dirac copy against the Regge term 0.5 c0 at the site rung. Standard Model content (24 Dirac) adds 23% to the TT coefficient and nothing to the Newtonian one, so G_TT/G_N = 0.81, against 0.998 +- 0.002 from Hulse-Taylor.
- Vacuum: as eps -> 0 the sea gives rho = -2.1e73 GeV^4, radiation-like. At eps = pi/2 the massless part is zero, but the top quark with 3 colours leaves -8.9e40 GeV^4 against the measured 2.5e-47.

## Boundary

Supplied: the tick parameters, the sea branch, the site-phase coupling, straight links, the reading of edge lengths in the matter phase (bond hop scaled by 1/length, generator by proper time, bond or cube sampling), the angle reading of a lapse at finite eps (the pi/2 stationarity holds only under it), static fields, a free sea, classical links, the fit forms of the extrapolation, the Standard Model content and all measured numbers. The response law cannot be reduced to stationarity of the matter phase: the plaquette and hinge terms are not induced by this sea. Consequences for the register, such as letting the sea act only through links or applying the symmetric-stress clause to the dressed photon, are proposals and are not adopted here. No adopted response clause is established.
