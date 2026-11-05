---
claim_id: a_site_qubit_ice_photon_makes_margolus_fermions_neutral_dipoles_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "With one fermion mode per site, a site-valued electric flux must be E_s = n_s - 1/2 along the bond between the site's even and odd cube centres; its emergent charges sum to zero for every configuration, and a Margolus fermion is an emergent-neutral dipole, never a charge; the supplied tick and transport rule do not give the ice rule (every cube count 4), the tick has no flat band, and the half-filled sea has nonzero count variance; in a supplied model H = J sum (N-4)^2 + t sum c^dag W c, second order gives ring exchange with |K| = 2t^2/3J on planar and t^2/3J on skew loops, a Gaussian reading has a gapless transverse pair, and the classical ice ensemble has a pinch point. The count penalty, t/J << 1 and the Gaussian reading are supplied. No emergent photon with Margolus fermions as its charges, and no Coulomb phase on this lattice, is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_site_qubit_ice_photon_makes_margolus_fermions_neutral_dipoles_2026_10_21.py
---

# A site-qubit ice photon makes Margolus fermions neutral dipoles

Claim type: bounded_theorem.
Primary runner: `scripts/a_site_qubit_ice_photon_makes_margolus_fermions_neutral_dipoles_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. This note asks whether the sites' own qubits can carry an emergent photon through a charge-ice construction. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix one qubit per site; the energy function used below is supplied. The result is negative on the decisive question. The qubits can carry an emergent photon in a supplied model, but then the Margolus fermions are not its charges. The route fails in its one-qubit form.

## Statement

1. Forced flux variable. On one fermion mode the only parity-even operators are 1 and n. A site flux must therefore be E_s = n_s - 1/2, oriented from the site's even cube centre to its odd one. The sites are the bonds of the body-centred lattice of cube centres. The divergences are q_e = N_e - 4 and q_o = 4 - N_o, and the ice rule says every cube holds exactly 4 fermions.
2. The fermion is neutral. The emergent charges sum to zero for every configuration. Adding a fermion puts +1 on its even cube and -1 on its odd cube, so a Margolus fermion is a dipole of length sqrt 3 with net emergent charge 0.
3. The rules do not give the ice rule. A half-tick keeps its own partition's counts but changes the other partition's, so the full tick keeps no cube count. The tick has no flat band, so no finite region at any rung carries a conserved local count. The half-filled sea has count variance near that of independent sites. Any change inside one cube at fixed count creates at least two defects in the opposite partition, so no cube-local update moves within the ice states except by phases.
4. Supplied ice model. In H = J sum_cubes (N - 4)^2 + t sum_cubes c^dag W c, second-order perturbation gives ring exchange on 24 body-centred four-cycles per cell. On the 12 planar cycles, the fermion-exchange sign combines with the pi flux of the edge hop so that the two paths add, giving |K| = 2t^2/3J. On the 12 skew cycles, which have one pairing, |K| = t^2/3J. The planar terms alone are unfrustrated. With the skew terms, half of the three-cycle closed surfaces carry flux pi, so the full ring model is frustrated.
5. Photon in the supplied model. In a Gaussian (non-compact) reading, the planar terms give two gauge zeros and one massless transverse pair with omega^2 = 2 U_eff K k^2 in site units, isotropic. In the frustrated full model, the expansion about the best classical minimum keeps a gapless pair at this level. The classical ice ensemble shows an exact pinch point.
6. Charges. Count defects carry (q, n_F) = (+1, +1/2), (-1, -1/2), (-1, +1/2) and (+1, -1/2) for even-5, even-3, odd-5 and odd-3 cubes. Every local change of fermion number is emergent-neutral. Defects hop at first order, with amplitude t/sqrt 3, and are automatically minimally coupled.

## Derivation

Item 2 is a sum over cubes: each site is a corner of exactly one even and one odd cube, so the sum of N_e - 4 over even cubes equals the sum of N_o - 4 over odd cubes, and the total charge vanishes. Item 3 follows because an even half-tick is block-diagonal on even cubes, so it commutes with even counts and not with odd ones; a conserved local count would be a compact eigenvector, which requires a flat band. Item 4 is degenerate second-order perturbation theory inside the ice manifold. The amplitude of each four-cycle is -(h21 h43 - h41 h23)/J, where the minus sign comes from fermion exchange.

## Checks

The runner prints 15 PASS lines on an 8^3 torus, and its output ends `TOTAL: PASS=15 FAIL=0`.

- `A1` the parity-even span of one mode has dimension 2.
- `A2` the charges sum to zero on 200 random configurations, and one added fermion gives (+1, -1).
- `B1` the even half-tick keeps even counts (6.3e-15) and changes odd counts (norm 4.00); the full tick changes both.
- `B2` the smallest band widths are 2.842, 2.643 and 2.345 at (mu, b) = (0,0), (0.4,0) and (0.4,0.15), with the Bloch spectrum matching real space to 1.2e-15.
- `B3` from a generic ice configuration one even half-tick leaks 1.7569 per odd cube at a = 0. The parity configuration is special: W maps it to its complement, with leak -1.1e-15.
- `B4` Var(N_b) = 1.9068, 1.9951 and 1.0542 at (0.4,0), (0.4,0.15) and (pi-0.2,0), against 2 for eight independent half-filled sites.
- `B5` the eight sites of any cube lie in eight different opposite cubes.
- `C1` per cell there are 12 planar and 12 skew four-cycles.
- `C2` the planar flux is pi (1.000000), with |K| = 0.666667 (planar) and 0.333333 (skew) in units of t^2/J.
- `C3` exact four-mode diagonalisation gives splitting/(4t^2/3J) = 0.99993, 0.99940 and 0.99342 at t/J = 0.01, 0.03 and 0.1.
- `C4` there are 24 three-cycle surfaces per cell, 12 with flux pi, with best classical cost 4.147 of 12.00 per cell.
- `D1` omega^2/(U k^2) = 2.00000 for the planar model.
- `D2` in the full model there are 130 zeros (127 gauge plus 3 uniform-field), and the 12 lowest modes are 0.7388 to 0.7787 t^2/J against 0.7810 for planar alone.
- `D3` with 66321 ring flips, S_xx at k = (1,0,0) is 4.1e-34 and at (2,0,0) is 1.3e-65, while at (0,1,0) it is 0.393. The random control at (1,0,0) gives 0.252.
- `E1` the defect quantum numbers and their first-order hopping.

The runner also prints estimates for comparison. The photon speed is about (t/J) times the free fermion speed, and the ice regime needs t/J << 1. Measurement requires the electron and photon speeds to agree to about 1e-15, and a defect mass of order J against m_e/E_Planck of about 4e-23. Both would be fine-tunings.

## What is supplied and the boundary

Supplied: the edge coin and the partitions, the count penalty J sum (N - 4)^2 and t/J << 1 (neither is in the rules), second-order perturbation theory, the Gaussian reading of the compact ring model, and the branch of the sea. Coulomb phases are established in the literature for spin-1/2 quantum spin ice and for cubic quantum dimers. Those results are cited, not rederived, and none is on this lattice.

Not established: an emergent photon whose charges are the Margolus fermions, and a Coulomb phase on this lattice. The statement that a gauge field needs Z_N with N >= 5 or a rotor is narrower than it reads: a spin-1/2 link suffices in the supplied model, but only if the qubits serve as flux rather than as matter. A count penalty added to the tick would remove the Dirac band of the edge coin.
