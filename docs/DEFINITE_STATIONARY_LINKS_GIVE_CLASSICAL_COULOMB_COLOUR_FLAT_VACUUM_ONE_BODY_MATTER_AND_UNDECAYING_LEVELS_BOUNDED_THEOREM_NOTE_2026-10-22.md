---
claim_id: definite_stationary_links_give_classical_coulomb_colour_flat_vacuum_one_body_matter_and_undecaying_levels_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Under the response law read with links set to definite stationary values sourced by the actual configuration (the earlier reading of the register): colour is classical Coulomb, since with occupation-basis colour charges in one Cartan the abelian Coulomb field is an exact stationary point of the Yang-Mills equations, the static pair energy is bounded by the self-energy (zero string tension) and every Wilson loop has modulus 1; the vacuum links are flat, with zero topological charge in every history; each history's matter update is one-body, so Slater determinants stay Slater and the links mediate no correlation or entanglement; a stationary excited level never decays under the fewest-change transport; and any definite or classically mixed field gives g2(0) >= 1. A fluctuating-link contrast (SU(2), 3D Euclidean heat bath, 8^3) shows an area law (finite diagnostic). Comparisons with the QCD running sign, the proton and eta' masses, the hydrogen 2p lifetime, the Lamb shift and a_e are estimates with supplied inputs. Conclusion: definite links are excluded by measurement, so links must carry odds, as the register's link registers do. No register dynamics is computed here."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/definite_stationary_links_give_classical_coulomb_colour_flat_vacuum_one_body_matter_and_undecaying_levels_2026_10_22.py
---

# Definite stationary links give classical Coulomb colour, a flat vacuum, one-body matter and undecaying levels

Claim type: bounded_theorem.
Primary runner: `scripts/definite_stationary_links_give_classical_coulomb_colour_flat_vacuum_one_body_matter_and_undecaying_levels_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. In its earlier reading the response law (CL-3 in the three-law numbering) set the links, like the edges, to definite values at which the total phase is stationary, sourced by the actual configuration of the actuality law (CL-2). This note asks what that reading gives for colour, the vacuum, matter correlations and light, and compares the results with measurement. The register has since adopted the alternative: each bond carries a link register in the update law (CL-1) whose odds evolve with the site odds, and the response law sets only the edges. This note records why. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix neither reading.

## Statement

With links definite, stationary and sourced by the actual configuration:

1. Colour is classical Coulomb. In the occupation basis every colour charge is a weight of one Cartan subalgebra (the three weights sum to zero and the two diagonal generators commute). With spatial links trivial and the time component in that Cartan, every commutator in the Yang-Mills equations vanishes, so the abelian Coulomb field is an exact stationary point; a quark-antiquark pair has parallel charges +-w for any colour orientation. The lattice Gauss law then holds exactly, the links are pure gauge in space and every plaquette is 1. The static pair energy is -g^2 |w|^2/(4 pi R) = -alpha_s/(3R) at large R and is bounded above by the self-energy at every separation, so the string tension is zero. A definite link configuration is a fixed product of unitaries around any loop, so |W(C)| = 1 for every loop and there is no area law at any coupling.
2. The vacuum links are flat. The response law measures every departure from the vacuum at the same configuration, so the vacuum is no source; definite vacuum links are then flat, F = 0, the topological charge is zero in every history, the topological susceptibility is zero and there is no gluon condensate.
3. Matter stays one-body. With c-number links each history's fermion update is a one-body unitary, so a Slater determinant stays a Slater determinant (its one-body density matrix stays idempotent), and a definite link sourced by the actual configuration gives, in every history, a product of one-body phases: two charges cannot be entangled through it.
4. Stationary levels never decay. If the odds are stationary, the fewest-change transport of the actuality law is to stay, so the actual configuration of an atom in a stationary excited level never moves, its current is zero, the definite link it sources stays static and the odds stay the eigenstate.
5. Any definite or classically mixed field gives g2(0) = <I^2>/<I>^2 >= 1 by the Cauchy-Schwarz inequality, so there is no antibunching.

## Derivation

Item 1. The two diagonal generators lambda3/2 and lambda8/2 commute, and the colour charges (1/2, 1/(2 sqrt3)), (-1/2, 1/(2 sqrt3)), (0, -1/sqrt3) are weights of their span with zero sum. Every term in the Yang-Mills equations that is not abelian is a commutator of fields in that span, so it vanishes and the equations reduce to two copies of Maxwell's. The static energy is |w|^2 (G(0) - G(R)) with G the lattice Green's function; G(R) > 0 gives the bound by the self-energy |w|^2 G(0), and G(R) -> 1/(4 pi R) gives the Coulomb form with |w|^2 = 1/3. The Wilson-loop statement holds because, without an average over link values, a loop is one unitary of determinant one.

Item 2. With the vacuum subtracted at the same configuration the vacuum has no source, and the stationary solution with no source is flat. A flat configuration has zero field strength, so its topological charge, susceptibility and condensate vanish.

Item 3. A c-number link enters each history's half-tick only through hop phases and on-site potentials, which are bilinear in the modes. A unitary generated by a bilinear maps a Slater determinant to a Slater determinant. A link sourced by the actual configuration gives, for each configuration of the two charges, a product of single-charge phases, which cannot create entanglement from a product state.

Item 4. With equal odds before and after the half-tick, the transport that keeps the configuration distributed as its odds and changes the fewest occupations is the identity, with zero changes. The configuration, its current and its source then stay fixed.

## Checks

The runner ends with `TOTAL: PASS=16 FAIL=0` in about 1 s. Two of the passing lines (|W(C)| = 1 for definite links and the flat vacuum) record the argument above without a numerical test; the commutation check behind item 1 verifies only that the diagonal generators commute and the weights sum to zero.

Exact checks and identities (checked numerically):
- Lattice Gauss law for the Cartan Coulomb field of a pair at separation 6 on a periodic 48^3 lattice: maximum residual 9.0e-17.
- Static energy V/g^2 from 0.0556 at R = 1 to 0.0820 at R = 12, below the self-energy bound 0.0827 at every separation; deviation from the Coulomb form 1.9% on R = 4 to 9; a fitted linear term sigma a^2/g^2 = -5.1e-05, consistent with zero string tension in a finite box.
- Six modes, one random one-body generator, three particles: maximum non-idempotency of the one-body density matrix 3.3e-16 after the one-body update, against 0.09 when a link-mediated n n term is added.
- Two charge qubits: a quantised link mode (an oscillator with 30 levels, coupling 0.4, returned to its vacuum, mediator purity 1.000) gives concurrence 0.771; the definite link sourced by each actual configuration gives at most 1.4e-17.
- Fewest-change transport (linear program on 5 configurations with random allowed transitions) for equal odds before and after: minimum changes 0.0.
- Minimum g2(0) over 200 random classical intensity mixtures: 1.0251 (>= 1).

Finite diagnostic (supplied contrast model, no error bars): fluctuating SU(2) links on an 8^3 Euclidean lattice at beta = 3.0 (heat bath, 60 sweeps to equilibrate, 20 measurements over 80 sweeps) give W11 = 0.626, W22 = 0.169 and Creutz ratios chi22 = 0.410, chi33 = 0.277, an area law; the definite-link value is exactly 0. This is a 3D SU(2) path sum over link odds, not the register's link registers.

## Estimates against measurement

All of these are estimates with supplied inputs (PDG masses, f_pi = 92.2 MeV, alpha_s(MZ) = 0.1180 with one-loop running and thresholds at m_b = 4.18 GeV, standard atomic constants):

- String tension: measured sqrt(sigma) = 440 MeV; definite links give 0 at every coupling. With no confinement, fractional charges would be free (bound below about 1e-22 per nucleon) and the proton would weigh about 2 m_u + m_d, about 9 MeV, against 938 MeV.
- QCD running: gluon loops need link fluctuations; matter loops alone give b0 = -2 nf/3, so alpha_s falls toward low energy, with no asymptotic freedom and no Lambda_QCD. alpha_s(m_tau) = 0.095 with matter loops only, 0.279 with gluon and quark loops at one loop, against 0.314(14) measured. For QED the one-loop running comes from matter loops alone, so the sea in c-number fields keeps it; photon lines first enter at two loops.
- eta': the Witten-Veneziano relation needs a topological susceptibility chi^(1/4) = 179 MeV; definite links give 0, leaving m_eta' <= sqrt3 m_pi = 239 MeV (the no-anomaly bound) against 957.8 MeV.
- Hydrogen 2p: quantised links (vacuum link odds, Wigner-Weisskopf, reduced mass) give tau(2p) = 1.5962 ns against 1.60 ns measured; definite links give no decay for the pure level. A definite field's radiation reaction acts only through the dipole coherence, dP/dt = -Gamma P (1 - P), so from P_e = 1 - 1e-6 the half time is 13.8/Gamma rather than ln 2/Gamma = 0.69/Gamma, against the measured exponential decays. Single-atom fluorescence measures g2(0) near 0.
- Entanglement: Coulomb-mediated trapped-ion gates and Rydberg blockade produce Bell states at fidelity above 0.99.
- Lamb shift: at leading order the self-energy (an internal photon propagator) and vacuum polarisation give 1069 MHz against 1057.845 MHz; definite links keep only the sea's vacuum polarisation, -27.1 MHz.
- a_e: Schwinger's alpha/2pi = 1.161410e-03 needs an internal photon, against 1.159652e-03 measured with uncertainty 1.3e-13; definite links leave a one-body Dirac electron in c-number fields, g = 2 up to lattice terms near 1e-63, missing by about 9e9 standard deviations.
- Kept in c-number fields: alpha's one-loop running, the Uehling term and Euler-Heisenberg light-by-light scattering. Not carried: the zero-temperature Casimir zero-point force, since the definite vacuum is flat.

On every count, definite links are excluded by measurement. Links must carry odds, which is the register's link-register clause: each bond's register holds odds valued in the update's symmetries and evolves with the site odds. The register now adopts quantised link registers in the update law, and the response law sets only the edges.

## Boundary

Supplied: the reading of the response law with definite links (now replaced in the register), colour SU(3) as the link group, the occupation-basis colour charges, the 48^3 periodic box, the 3D SU(2) contrast model and its coupling, the oscillator mediator and coupling used for the entanglement contrast, the random test models for the transport and for g2, and every input of the estimates. Forced, given the definite reading: classical Coulomb colour with zero string tension and unit-modulus Wilson loops, flat vacuum links with zero topological charge, one-body matter updates in every history, no link-mediated entanglement, no decay of stationary levels and g2(0) >= 1. Not claimed: any property of the register's link registers beyond the contrast models (their confinement, running, topology, emission rate, Lamb shift and a_e have not been computed on the lattice); that the 3D SU(2) area law carries over to 4D SU(3); any statement about the edges, which stay definite in the register. The heat-bath result is a sampled finite diagnostic of a supplied model, without error bars, not a theorem about the register's tick.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records; they fix none of the inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the response law's stationary phase measured from the vacuum, the actuality law's fewest-change transport, and the update law's link registers adopted in place of definite links. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/definite_stationary_links_give_classical_coulomb_colour_flat_vacuum_one_body_matter_and_undecaying_levels_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1 s, prints about 4.8 kB and ends with `TOTAL: PASS=16 FAIL=0`.
