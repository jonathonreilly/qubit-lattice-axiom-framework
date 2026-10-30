---
claim_id: link_registers_built_from_rishon_fermion_mode_sites_carry_exact_u1_and_su3_gauss_laws_and_sit_covariantly_from_zoom_three_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "With each bond's link register built from one-mode fermion sites at the two bond ends (rishons; 2S modes per end for a spin-S U(1) link): U = b^+ a and E = (n_b - n_a)/2 obey the spin-1/2 link algebra on the one-rishon sector, and on a cubic site div E = 3 - N_rishon exactly, so Gauss's law is conservation of each vertex cluster's fermion number; the rishon-dressed hop and the 8-rishon plaquette commute with every cluster number, so exp(i sum alpha_x G_x) is an exact continuous U(1) gauge group although E has finitely many levels; three colour rishons per end give an exact SU(3) colour Gauss law, and the colour-singlet det term breaks the extra cluster U(1), leaving SU(3) rather than U(3); rishon occupations do not commute with colour generators, so rishon sites must carry no records. The six bond ends of a vertex carry A1 + E + T1 of the 24 rotations, and site-centred blocks of odd side b >= 3 host one rishon per bond end covariantly on a face 6-orbit, while even blocks need a 24-site orbit. Tiny-chain spectra (4 sites, spin 1/2 and spin 1; one plaquette) are finite diagnostics of a supplied model. The Coulomb phase of 3+1D U(1) quantum links, dimensional reduction of SU(N) quantum links and the compact U(1) transition are cited, not computed; couplings against measurement are estimates. No role assignment, spin S, coupling or continuum limit is derived."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/link_registers_built_from_rishon_fermion_mode_sites_carry_exact_u1_and_su3_gauss_laws_and_sit_covariantly_from_zoom_three_2026_10_22.py
---

# Link registers built from rishon fermion-mode sites carry exact U(1) and SU(3) Gauss laws and sit covariantly from zoom three

Claim type: bounded_theorem.
Primary runner: `scripts/link_registers_built_from_rishon_fermion_mode_sites_carry_exact_u1_and_su3_gauss_laws_and_sit_covariantly_from_zoom_three_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1 in the three-law numbering) gives each bond a link register whose odds evolve with the site odds. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) allow one qubit per site and nearest-neighbour admissibility, and nothing else. This note asks whether a link register can be made of the same one-mode fermion sites as matter, placed at the two ends of each coarse bond (rishons), and what gauge structure, Gauss law and placement then follow. Every result is conditional on the supplied role assignment (which fine sites are rishons) and on the supplied couplings.

## Statement

1. Spin-1/2 U(1) link. With two fermion modes a (tail end) and b (head end) per bond, U = b^+ a and E = (n_b - n_a)/2 obey [E, U] = U and [U, U^+] = 2E on the one-rishon sector n_a + n_b = 1. U is nilpotent (U^2 = 0), not unitary: this is a quantum link, not a group-valued clock.
2. Gauss's law is fermion-number conservation. On a cubic site with six bond ends, and with one rishon per link, div E = 3 - N_rishon(x) exactly, so n_psi - div E = (n_psi + N_rishon) - 3 is the fermion number of the vertex cluster (matter mode plus its own six bond ends). The source is the matter number, a charge.
3. Exact continuous gauge group. The rishon-dressed hop psi_x^+ b^+ a psi_y commutes with every cluster number G_x and every link number; the bare hop psi_x^+ psi_y does not. Hence exp(i sum_x alpha_x G_x) leaves the update generator invariant for all real alpha_x, an exact continuous U(1) gauge group, although E has only two levels. Gauss's law is preserved by the dynamics from any Gauss state, not imposed.
4. Plaquette. The product U1 U2 U3 U4 around a face is an 8-rishon term commuting with all corner numbers.
5. SU(3). With three colour rishons per bond end and quark triplets at both ends, the hop q_x^+a c_x^a c_y^b+ q_y^b commutes with all 16 generators G^A (8 per cluster, each the sum over quarks and the rishon end of f^+ T^A f). The det term, a colour-singlet rishon triple crossing the link, is SU(3)-invariant but changes the x-cluster's end number by 3, so it breaks the extra cluster U(1) the hop keeps: the gauge group is SU(3), not U(3). The one-rishon SU(3) link has 2N = 6 states, (3,1) + (1,3).
6. Records. If the actuality law (CL-2) records every mode's occupation, then on rishon sites it records the U(1) electric value (item 1) and, for colour, a number that does not commute with the colour generators. So rishon sites must carry no records; this is a requirement this construction places on the records clause.
7. Covariant placement. The six bond ends of a vertex carry the representation A1 + E + T1 of the 24 proper rotations. A site-centred block of odd side b has face 6-orbits, so one rishon per bond end sits covariantly from b = 3; an even (cube-centred) block has no 6-orbit, and its smallest orbit containing A1 + E + T1 has 24 sites (four per end). Only odd blocks have a rotation-fixed centre. At b = 3, with matter at the block centre and rishons at the six face centres, each axis reads matter(0)-rishon(1)-rishon(2)-matter(3) on adjacent fine sites, so the gauge-invariant hop is the product of two nearest-neighbour bilinears (psi_0^+ c_1)(c_2^+ psi_3), a 4-site line gate.

## Derivation

Item 1 is the Schwinger-boson form of a spin-1/2 operator restricted to one particle in two modes. Item 2: with partner ends fixed by n_own + n_partner = 1, the outgoing link along +i has E = 1/2 - n_(x,+i) and the incoming link along -i has E = n_(x,-i) - 1/2; summing the six gives div E = 3 - sum of own-end occupations. Item 3: the dressed hop moves one fermion from y to x and one rishon from a to b within the same link, so the cluster numbers at x and y and the link number are unchanged term by term; the gauge transformation is the exponential of commuting conserved numbers. Item 5: each factor q_x^+a c_x^a is a colour singlet bilinear in the x-cluster, and likewise at y; the det term is the antisymmetric (singlet) product of three rishons, which carries cluster U(1) charge 3. Item 7: the rotation characters of the six face points are reduced with the character table of the rotation group O; orbits are enumerated on doubled integer coordinates of the b^3 block.

## Checks

The runner ends with `TOTAL: PASS=20 FAIL=0` in about 0.5 s. The lines labelled theorem below are exact computations (operator commutators on bit-string Fock spaces, enumerations); one passing line records an argument without a numerical test, as noted.

- Spin-1/2 link algebra on n_a + n_b = 1, U^2 = 0, ||P(U U^+)P - P|| = 1.00.
- div E = 3 - N_rishon on all 64 end patterns of a cubic site.
- 1D chain, 4 matter sites (staggered mass m = 0.7, t = 1) and 3 spin-1/2 links (10 modes, dense 1024 states): [H, G_x] = 0 and [H, N_link] = 0 to machine zero, bare hop commutator 1.0; random gauge angles give ||V H V^+ - H|| = 2e-16; the sector reached from a Gauss state has dimension 5, every G_x fixed, E^2 = 1/4 on every link (no electric energy at S = 1/2), gap 2.234.
- 1D chain with spin-1 links (two rishon flavours per end, 16 modes, sector only): the flavour-singlet sector of one link has dimension 3 with E in {-1, 0, 1} and the su(2) relations; every term is flavour-blind ([H, F] = 0). Pure gauge without charges (g^2 = 1): the div-free fluxes are uniform, with energies {0, 1.5, 1.5} = (g^2/2) 3 e^2.
- One plaquette, four spin-1/2 links (8 modes): the plaquette commutes with all corner numbers; the div-free sector is the two circulating fluxes, split to -J, +J (J = 1).
- SU(3) link with quarks (12 modes): [H, G^A] = 6e-17, [det, G^A] = 6e-17, [det, N_x] = 3, [hop, N_x] = 0; the one-rishon link has 6 states (a count); ||[n_c1, G^A]|| = 0.50.
- Rotation census: A1 + E + T1 for the six bond ends; per block side b = 2..7 (number of face 6-orbits / smallest orbit containing A1 + E + T1 / number of fixed sites): b2 0/none/0, b3 1/6/1, b4 0/24/0, b5 2/6/1, b6 0/24/0, b7 3/6/1.
- The b = 3 line-gate layout (item 7, last sentence) is stated by the runner with check(True), not computed. The site budget is arithmetic: U(1) at S = 1/2 needs 1 + 6 of 27 sites at b = 3; SU(3) x SU(2) x U(1) rishons at hypercharge-link spin 2 (18 + 12 + 24 = 54 modes per coarse site) plus 16 matter modes fit 125 sites at b = 5.

Finite diagnostics (supplied model, tiny chains, no physical identification):

- Spin-1 chain, hopping t = 0.5, m = 0.1, g^2 = 2: the Gauss sector stays gapped, gap 1.697.
- Frozen matter (t = 0, g^2 = 1): an electric string of r links costs 0.500, 1.000, 1.500 for r = 1, 2, 3, linear in r (the 1D Coulomb law).
- Dynamical matter (t = 1, m = 0.1, g^2 = 4, 4 sites): every cluster number is conserved; the string costs E(r) - E_vac = 2.554, 3.056, 5.160 against frozen values 2, 4, 6. The 2- and 3-link strings cost less than frozen (pairs screen them); the 1-link string costs more, since it also blocks the sea's hopping. Four sites is far from any continuum statement.

## Estimates against measurement

These use supplied one-loop running and cited lattice values; none is a derivation.

- One-loop Standard Model running from MZ gives alpha_s(M_Pl) = 0.0191 (1/(4 pi alpha_s) = 4.17) and alpha_Y(M_Pl) = 0.0180; the same one-loop running gives alpha_s(m_tau) = 0.272 against the measured 0.314.
- Quantum SU(3) links fluctuate, so gluon loops contribute and b0 = 11 - 2 nf/3 > 0 for nf <= 16, the measured sign of asymptotic freedom. For links read as definite stationary values (the earlier reading of the response law) the gluon term is absent and b0 = -2 nf/3; the runner states this comparison, it computes only the sign of 11 - 4.
- Reaching alpha_s(M_Pl) by dimensional reduction of SU(3) quantum links, 1/g4^2 = N5/g5^2 with the cited, uncertain value g5^2 ~ 6/4.3 on the 5D Coulomb side of the bulk transition, needs N5 ~ 5.8 layers.
- A U(1) Coulomb phase needs bare alpha below about 1/(4 pi) (compact U(1), beta_c ~ 1.01, cited). The cited spin-1/2 quantum-link (spin-ice) estimate alpha ~ 0.08, from another lattice, exceeds alpha_Y(M_Pl) ~ 0.018 by about 4, so spin 1/2 is likely too strongly coupled for hypercharge, which then needs larger S (more rishon flavours per end).

## Boundary

Supplied: the role assignment of fine sites (matter versus rishon), the Gauss and flavour sectors chosen, the spin S (number of rishon flavours per end), the couplings t, m, g^2, J, the layer number N5 and the one-loop running inputs. Forced, given those: the link algebra, Gauss's law as cluster fermion-number conservation, an exact continuous U(1) (and exact SU(3) with the det term) on finitely many levels, the requirement that rishon sites carry no records, and the odd-block covariant placement from b = 3. Cited, not computed: the Coulomb phase of 3+1D U(1) quantum link models, dimensional reduction of SU(N) quantum link models, the compact U(1) transition coupling and the spin-ice coupling estimate. Not claimed: that the register's update law contains these terms with these couplings, any continuum limit, confinement or its absence in 3+1D, the value of any gauge coupling, or that the records clause already exempts rishon sites (item 6 states that it must).

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's link register per bond and the actuality law's records. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/link_registers_built_from_rishon_fermion_mode_sites_carry_exact_u1_and_su3_gauss_laws_and_sit_covariantly_from_zoom_three_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 0.5 s with about 60 MB resident, builds no dense Fock space of 2^11 or more, prints about 5.9 kB and ends with `TOTAL: PASS=20 FAIL=0`.
