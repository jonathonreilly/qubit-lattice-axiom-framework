---
claim_id: qubit_cell_complex_emergent_gauge_fields_select_no_matter_multiplet_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "One qubit per site of Z^3, read at rung 2: the sites with 0, 1, 2, 3 odd coordinates are the vertices, edges, faces and cubes of 2Z^3 (1+3+3+1 per 2^3 block). Exact: X on the 6 nearest neighbours of each vertex site and Z on the 4 edge-site nearest neighbours of each face site commute, are invariant under all 24 cube rotations, and give log2 torus code dimension 3 (coarse L = 3, 4); the point charge is a boson (T-junction +1). The Bravyi-Kitaev superfast twist on the same edge sites makes the charge a fermion (T-junction -1) but has fine-lattice support diameter 4 and 6 and keeps 6 of 24 rotations for the ordering tested. Spin-1/2 ice on the edge sites keeps every vertex divergence under face-site ring flips; the equal-weight ice ensemble at coarse L = 6 has S_xx = 0 along x and S(1,1,0)/S(0,1,0) = 0.505 (finite diagnostic); the Gaussian reading has two transverse gapless modes. A seeded local two-band hop on Z^3 has Weyl charges summing to zero. With fermion parity in the emergent gauge group, the smallest cyclic group forbidding Majorana masses is Z4; SU(2) spin-j multiplets are mass-protected for half-integer j and, by the cited Witten and Wang-Wen-Witten anomalies, the smallest consistent one is j = 7/2 (8 Weyl); the Spin(10) 16 built from 5 modes has no invariant bilinear, zero cubic anomaly and a central element acting as i. The energy functions, the BKSF ordering, the RK ensemble, the Gaussian reading and the hop are supplied. No Coulomb phase of the spin-1/2 model, no chiral emergent fermion, no gauge group and no matter multiplet is selected."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/qubit_cell_complex_emergent_gauge_fields_select_no_matter_multiplet_2026_10_22.py
---

# One qubit per site carries emergent gauge fields at rung 2, but no matter multiplet is selected

Claim type: bounded_theorem.
Primary runner: `scripts/qubit_cell_complex_emergent_gauge_fields_select_no_matter_multiplet_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix one qubit per site of Z^3 and write no gauge group. This note asks whether gauge fields and matter can be COMPOSITE: collective excitations of qubit sites under a nearest-neighbour rule, with no group-valued link and no internal multiplet on one site. The answer is split. Emergent Z2 and U(1) gauge structure fit the axioms exactly at rung 2. Emergent fermions fit only with a lopsided, longer-range twist; they are vectorlike under any local hop; and the consistency conditions for emergent fermions do not select the 16 or Spin(10).

## Statement

1. Rung-2 cell complex (exact). In a 2^3 block of sites, the number of odd coordinates sorts the sites into 1 vertex, 3 edge, 3 face and 1 cube site of the coarse lattice 2Z^3. One qubit per site therefore already carries a full cell complex, and a qubit on every coarse edge, without bending the qubit axiom.
2. Emergent Z2, nearest-neighbour (exact). The rule "X on the six neighbours of a vertex site, Z on the four edge-site neighbours of a face site" uses only nearest-neighbour stars. All terms commute and the rule is invariant under the 24 cube rotations. The torus code dimension is log2 = 3 at coarse L = 3 and 4, the first Betti number of T^3, so the Z2 gauge theory is deconfined. Z on an edge site makes a charge pair and X makes a flux loop through four face sites. The charge hops commute, so the Levin-Wen T-junction sign is +1 and the charge is a boson.
3. Fermionic charges cost symmetry and range (exact). On the same edge sites, the Bravyi-Kitaev superfast operators obey the fermion-hopping algebra: they anticommute exactly when they share a vertex. Their loop products commute with everything, and the T-junction sign is -1, so the charge is a fermion. The price is threefold. The support diameters are 4 and 6 fine steps, against 2 for the stars, so the rule is not nearest-neighbour. It needs an ordering of the six directions. The code tested keeps only 6 of the 24 rotations. This reproduces the BKSF note on main. The rotation-covariant alternative on main, the Majorana-per-direction code, uses three qubits per site and so is atomic.
4. Emergent U(1) (exact constraint; finite diagnostic for the phase). Spin-1/2 ice on the edge sites (E = +-1/2, divergence zero at every vertex site) is preserved exactly by ring flips centred on face sites. In the equal-weight (RK) ice ensemble at coarse L = 6 (94446 accepted flips, 200 samples), S_xx(q) vanishes along x (exactly, because the field is divergence-free) and is finite and isotropic across the transverse directions (1.467 and 1.462). The ratio S(1,1,0)/S(0,1,0) = 0.505 sits near the transverse-projector value 1/2: Coulomb-type dipolar correlations. Under the Gaussian reading H = U E^2/2 + K (curl A)^2/2, every k has one pure-gauge zero and two degenerate transverse modes with omega^2 = UK sum 4 sin^2(k_i/2), linear at small k. These are two photon polarisations with one qubit per edge site.
5. Doubling (exact for the class tested). A seeded random local two-band hop on Z^3 has Weyl nodes (the slice Chern number jumps between 0 and 1), and their charges are +1 and -1, summing to zero. An emergent fermion that hops locally on the coarse lattice is a local lattice fermion, so it inherits Nielsen-Ninomiya: its chiralities pair.
6. Multiplet selection (exact arithmetic plus cited anomalies).
   - (a) Emergent fermions are string ends, so the fermion parity of the emergent sector is a gauge transformation, and the fermions carry odd charge under the emergent group. The smallest cyclic group that forbids every Majorana mass is Z4.
   - (b) SU(2) spin-j has no symmetric invariant bilinear for half-integer j, so the group alone forbids masses. Witten's anomaly removes j = 2r + 1/2. The new SU(2) anomaly (j = 4r + 3/2), which applies because fermion parity is the centre, is cited. The smallest consistent mass-protected irreducible multiplet is j = 7/2: 8 Weyl, not 16.
   - (c) The Spin(10) 16 built from five modes has no invariant bilinear and zero cubic anomaly, and exp(i pi Q) acts on it as the scalar i. The SU(16) fundamental is anomalous.
   - (d) Cited: of the simple groups with a 16-dimensional irrep, Spin(10) is the only one that is complex and anomaly-free. "Complex" and "dimension 16" are selector choices, not consequences of (a)-(b).
   - (e) Comparison with measurement: X = 5(B-L) - 4Y is 1 mod 4 on all 16 Weyl of a measured family including nu^c, so the family is a Z4-protected multiplet with nu = 16. By the cited Spin-Z4 bordism (Z16), the 15 without nu^c would be anomalous.

## Boundary

- Not established: a Coulomb phase of the spin-1/2 cubic ice model away from the RK ensemble, which needs dynamics; numerics exist for pyrochlore, and for the cubic lattice see the spin-half cubic ice RK note on main.
- Also not established: a nearest-neighbour, rotation-covariant fermionic charge on one qubit per site; any chiral emergent fermion; any non-abelian emergent group (which needs at least 2N states per link, per the SU(N) link note); any selection of SU(3)xSU(2)xU(1), Spin(10), the 16 or three families.
- The star, plaquette and ice energies are supplied. In this framework they would have to come from the update rule, which is not shown.
- The Z4 / Z16 statements do not derive 16 from the rules. They say that IF the emergent fermion's protection is the minimal cyclic one, THEN anomaly freedom demands nu = 0 mod 16 and nu^c. The protection requirement itself is chosen to match the observed light chiral fermions.

## Notes used

- Reproduced/narrowed: BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_MINIMAL_ORBIT_FOUR (fermion statistics, lack of O-invariance).
- Cited: MAJORANA_PER_DIRECTION_CUBIC_FERMION_CODE (covariant, three qubits per site); THREE_AXIS_QUBIT_SITE_STABILIZER_RULES (toric codes move, three qubits per site); SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS (RK correlations); DYNAMICS_CLAUSE_NON_ABELIAN_GAUGE_LINKS_NEED_SEVERAL_QUBITS (2N states per SU(N) link).
- Campaign drafts: emergent-photon (one-mode site flux makes Margolus fermions neutral; this note avoids that by putting the flux on separate edge sites); gauge-registers (no group selected by registers); qlm-coulomb (S ~ 300 links needed for the measured alpha).
- Literature: Kitaev 2003; Bravyi-Kitaev 2002; Levin-Wen PRB 67 245316; Wen PRD 68 065003; Hermele-Balents-Fisher PRB 69 064404; Chandrasekharan-Wiese 1997; Nielsen-Ninomiya 1981; Witten 1982; Wang-Wen-Witten 1810.00844; Garcia-Etxebarria-Montero 1808.00009; Wang-Wen 1809.11171.
