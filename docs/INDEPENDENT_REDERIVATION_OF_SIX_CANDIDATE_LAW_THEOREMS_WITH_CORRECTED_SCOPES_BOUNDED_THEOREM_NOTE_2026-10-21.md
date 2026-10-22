---
claim_id: independent_rederivation_of_six_candidate_law_theorems_with_corrected_scopes_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Independent rederivation of six candidate-law theorems with corrected scopes: spin-3/2 forcing and Born transport hold as stated under explicit premises; the universal step, the copy count and the cell factorisation hold only in narrower forms; the cubic-frustum Regge expansion law matches Friedmann only to first order in rho/rho* and has no bounce; the corrected statements are checked as finite diagnostics of the supplied models; no new law, adopted wording or physical identification is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/independent_rederivation_of_six_candidate_law_theorems_with_corrected_scopes_2026_10_21.py
---

# Independent rederivation of six candidate-law theorems with corrected scopes

Claim type: bounded_theorem.
Primary runner: `scripts/independent_rederivation_of_six_candidate_law_theorems_with_corrected_scopes_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update, following and expansion statements cite six theorems. This note rederives each from scratch, with its own code and without importing the earlier runners, and states the scope in which each holds. Where a statement is wrong, the runner checks the corrected one. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the supplied premises listed below.

| # | Theorem | Verdict |
|---|---|---|
| 1 | spin-3/2 forcing | holds, with premises stated |
| 2 | universal step | identity, bands, speed and photon match hold; equal limiting speed and the exclusion claim are narrower; one reading of "the same unitary" gives the wrong tick |
| 3 | copy count | narrower: the general statement fails for j other than 3/2 |
| 4 | Born transport | holds |
| 5 | cell factorisation | facts hold; the two rotation actions used together are incompatible |
| 6 | Friedmann from cubic Regge | holds to first order in rho/rho* only; no bounce |

## 1. Spin-3/2 forcing

Statement. Assume one mode per site, a block unitary supported on sites and cube edges with nonzero hopping, and covariance under the 24 rotations through some local lift to the site modes. Then every face carries pi flux, the lift is spinorial with the order-6 lift of a corner's C3 acting on that corner by -1, and the block unitary is e^{i phi}(cos a + i sin a W) with W^2 = 1.

Derivation. For every corner character j = 0, 1/2, ..., 6 the covariant operators on sites and edges are the identity and one hop X, with X a phase times a Hermitian operator of equal moduli and face phase exp(-+2 pi i j/3). A hopping covariant unitary exists iff j = 3/2 mod 3. An equal-modulus Hermitian W has W^2 = 1 iff all six faces carry -1, which needs no rotations. The nearest-neighbour premise carries the result; without it every character admits covariant hopping unitaries. One mode cannot carry spin 3/2: the eight corners form 2G3/2 = (spin 1/2) x E, so "spin 3/2" names one sign. No integer-j action admits a covariant hopping nearest-neighbour unitary, so the double cover is forced. Non-Hermitian unitary equal-modulus hops with W^2 not 1 exist, but none is covariant.

## 2. Universal step

The identity V(mu/2 + b) = i exp(-i(eps - mu/2)W), V(mu/2 - b) = -i exp(+i(eps + mu/2)W) is exact, and the phases i and -i cancel per particle per full tick. The band law holds when each site keeps one overlap state used by both of its cubes. Reading "every cube applies the same unitary" as the same 8x8 matrix in each cube's own corner labels, in the overlap gauge, gives the wrong tick; it is right only in an inversion-symmetric gauge, which exists. The massless speed is sin(eps)/sqrt 3 blocks per tick. Equal limiting speed holds exactly only for massless species: c(mu)^2/c(0)^2 - 1 = mu^2(1/6 - 1/(4 cos^2 b)) + O(mu^4). A Yee photon's transverse band equals the massless fermion band at every K iff C = cos(b)/sqrt 3 = sin(eps)/sqrt 3, a matching condition on the link update that a shared eps does not supply. In lattice kinematics a shared step closes photon decay and vacuum Cherenkov emission, a faster photon opens only gamma -> f fbar and a slower one only f -> f gamma; measurements bound the speed difference rather than exclude it.

## 3. Copy count

At Gamma (and at R) the corner content is A1+A2+T1+T2 for j = 0, E1/2+E5/2+G3/2 for j = 1/2 and 5/2, E+T1+T2 for j = 1 and 2, and 2G3/2 for j = 3/2. A k-linear invariant and a mass exist within E1/2 but not between E1/2 and E5/2, and G3/2 = E1/2 x E. Corrected statement: for every site character, a translation-invariant covariant free 2^3 tick has no room for exactly one massive Dirac copy at Gamma or R, and for j = 3/2 any Dirac sector there has exactly two copies. For j = 1/2 and 5/2 there is no massive copy at all, and E1/2+E5/2 can carry two Weyl cones with mass forbidden. Block unitaries varying with period 4, or a 4^3 cell, give 4E1/2+4E5/2+12G3/2, which has room. "No covariant term splits the copies" holds only at rest: the covariant commutant is U(2) x 1 of dimension 4, generic covariant ticks are fourfold at Gamma with 8 levels at generic K, and only the nearest-neighbour family stays fourfold at every K.

## 4. Born transport

Every target set S has q(S) <= p(N^-1(S)), so max-flow gives a transport for any unitary in any basis, and its marginals are the old and new odds. Fewest occupation changes alone is degenerate, and a vertex of that face moves when configurations are relabelled. The greatest-entropy plan is unique by strict concavity and relabelling-equivariant. Counting changed occupations gives two unentangled relays the exact product plan; counting changed configurations couples them. "Label-free" means equivariant under relabelling configurations; the plan still depends on the mode basis, the half-tick and the global configuration.

## 5. Cell factorisation

The plain corner permutation gives A1+A2+T1+T2, while the forced site action of section 1 gives 2G3/2, so the plain action on the cell index is supplied. Parity x body diagonal is the only rotation-invariant product of corner sets, but as a tensor factorisation there is a one-parameter family, all sharing T3 and B-L. The rotation commutant on C^8 has 3 traceless generators: T3, B-L and T3(B-L), equivalently the four species numbers. T3 and B-L are unique only among one-factor generators, so four abelian charges, not three, are rotation-blind. Under the geometric rotation the rung-1 cell is 4E1/2+4E5/2+12G3/2; "every cell state is spin 1/2" (16G3/2) needs a rotation that fixes the cell index, under which nothing singles out T3 or B-L. One rotation action cannot give both the charges and the spin.

## 6. Friedmann from cubic Regge

The explicit Minkowski frustum has trapezoid deficit 4 asin(u^2/(1 - u^2)), area (l + l')T sqrt(1 - 2u^2)/2 and square boosts atanh u, and Schlaefli fixes the relative sign. The lapse equation is E = 6 kappa (l + l') A(u) with A(u) = asin(u^2/(1 - u^2))/sqrt(1 - 2u^2). With u = Hl/2 and x = rho/rho*, the exact law is (8 pi G/3) rho l^2/4 = A(Hl/2), which expands as H^2 = (8 pi G/3) rho [1 - x + (13/12) x^2 - ...]. It increases monotonically with rho and saturates at Hl -> sqrt 2, with no zero at rho*, so there is no bounce. Dust gives l ~ t^(2/3) and radiation l ~ t^(1/2) at late times; early times coast at l ~ t.

## Checks

The runner gives 33 PASS and 0 FAIL. These are finite diagnostics of supplied models.

- The double cover 2O is built with 8 irreducible characters. Induction is a homomorphism to 5e-14 for every j. Face phases over pi are 0, +0.33, +0.67, +1.00, -0.67, -0.33, 0 for j = 0 to 3. W^2 = 1 holds for 128 of 4096 sign patterns, one gauge class, and is checked on 3000 complex assignments.
- Step identity to 6e-15. On a 6^3 torus all 216 quasi-energies obey the band law to 4e-15 and are covariant about even and odd centres to 5e-15. The cube-frame reading deviates by 0.57 with asymmetry 0.78, and by 9e-15 in the inversion-symmetric gauge. Speed to 2e-13 on three directions. Massive speed deviations -2.68e-4, -8.33e-4, -2.76e-4 match the formula. Yee match to 5e-15, and C x 1.01 is off by 0.17.
- Gamma and R ticks commute with the corner action to 8e-15, with all 8 Gamma states at +-mu.
- Supply-demand on 20,000 sets with max excess 2e-15. A many-body tick on a 4^3 torus with 2 particles in an entangled state (2016 configurations) has a support-confined plan with error 1e-16. The optimal face has dimension 10 at mu = 0; the greatest-entropy plan meets its optimality form to 2e-14, with entropy 3.9593 against 3.5964 for a vertex. The product plan holds to 2e-16, against 2.4e-2 with configuration counting.
- 1 of 35 x 105 corner-set products is rotation-invariant; T3(B-L) has eigenvalues -1, -1/3, 1/3, 1.
- The frustum holds to 7e-15 and Schlaefli to 4e-10 with one sign (3.9 with the other). The x^2 coefficient is 1.081. The exact ratio H^2/((8 pi G/3) rho) is 0.990, 0.673, 0.510, 0.345 at x = 0.01, 0.5, 1, 2, against 1 - x = 0.99, 0.50, 0, -1. Late exponents are 0.6667 and 0.5000, early 1.0000.

## Against measurement (estimates)

1.4 PeV photons bound only a faster photon, dc/c < 2(m_e/E)^2, about 2.7e-19. SN1987A gives |c_nu - c|/c below about 2e-9.

## Boundary

Supplied: nearest-neighbour support and the existence of a local rotation lift, a shared eps, the site-attached reading of W on odd cubes, translation invariance per tiling, the occupation-count cost and entropy tie-break, the plain internal action and the naming of irreps as particles, the homogeneous cubic frusta, the matter phase -E T, kappa and the central tick as proper time. This is a review of results stated elsewhere in the register; the corrected wordings it implies are proposals and are not adopted here. No new law, adopted wording or physical identification is established.
