---
claim_id: definite_stationary_links_give_classical_coulomb_colour_flat_vacuum_one_body_matter_and_undecaying_levels_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For a supplied definite-link ansatz (spatial links pure gauge, the time component in one Cartan subalgebra, occupation-basis colour charges, sourced by the actual configuration): the abelian Coulomb field is a stationary point of the Yang-Mills equations, the lattice Gauss law holds exactly, the static pair energy is bounded by the self-energy (zero string tension for this configuration), and every Wilson loop of its pure-gauge spatial links has normalised trace 1. Uniqueness of this stationary point is not shown. Two negative results are kept with witnesses: product unitarity does not give |W(C)| = 1 (U = diag(1, w, w^2) in SU(3) has tr U/3 = 0), and a sourceless stationary point need not be flat (a uniform Cartan flux on a periodic slice). Conditional lemmas: if c-number links enter only through bilinear terms, each history's matter update is one-body and Slater determinants stay Slater; with the supplied coupling a c-number link mediates no entanglement; with equal odds the fewest-change plan is the identity; any classical intensity gives g2(0) >= 1. A fluctuating-link contrast (SU(2), 3D Euclidean heat bath, 8^3) shows an area law (finite diagnostic). Comparisons of the ansatz with measurement are estimates with supplied inputs; they exclude no other definite-link configuration and do not show that links must carry odds. No register dynamics is computed here."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/definite_stationary_links_give_classical_coulomb_colour_flat_vacuum_one_body_matter_and_undecaying_levels_2026_10_22.py
---

# On a supplied Cartan pure-gauge ansatz, definite links give Coulomb colour; c-number links keep matter one-body and stationary levels unmoved

Claim type: bounded_theorem.
Primary runner: `scripts/definite_stationary_links_give_classical_coulomb_colour_flat_vacuum_one_body_matter_and_undecaying_levels_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. In an earlier reading of the originating three-law register, the response law (CL-3 in the three-law numbering) set the links, like the edges, to definite values at which the total phase is stationary, sourced by the actual configuration of the actuality law (CL-2). A later version of that register proposes the alternative: each bond carries a link register in the update law (CL-1) whose odds evolve with the site odds. Both readings are supplied model choices with zero premise weight; neither is adopted. This note asks what one explicitly supplied definite-link configuration gives for colour, the vacuum, matter correlations and light, and compares that configuration with measurement. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix neither reading.

Local labels. CL-1, CL-2 and CL-3 here are the update, actuality and response laws of the originating three-law register, not the entries of the same number in `docs/CANDIDATE_LAWS.md`.

## Correction (2026-11-14)

The held version of this note stated, for every definite stationary link configuration, that |W(C)| = 1 for every loop, that the sourceless stationary solution is flat, and that definite links are excluded by measurement so that links must carry odds. Those statements are withdrawn. A product of unitaries is unitary, but its normalised trace need not have modulus 1, and the Cartan Coulomb stationary point was exhibited, not shown unique. The colour and vacuum statements below are now about the supplied ansatz only, and the two counterexamples are kept as negative results.

## Statement

The supplied ansatz: spatial links pure gauge, the time component A_0 in the Cartan subalgebra spanned by lambda3/2 and lambda8/2, colour charges in the occupation basis (weights of that Cartan), links sourced by the actual configuration.

1. Coulomb colour on the ansatz. Every commutator of A_0 values vanishes, so the Yang-Mills equations reduce to two copies of Maxwell's and the abelian Coulomb field is a stationary point; a quark-antiquark pair has charges +-w. The lattice Gauss law holds exactly and every spatial plaquette is 1. The static pair energy is -g^2 |w|^2/(4 pi R) = -alpha_s/(3R) at large R and is bounded above by the self-energy at every separation, so this configuration has zero string tension. Every Wilson loop of its pure-gauge spatial links has normalised trace exactly 1. Not shown: that this stationary point is unique, or that every definite stationary configuration lies in the ansatz.
2. The flat vacuum. The flat (pure-gauge) configuration is a sourceless stationary point with F = 0, so it has zero topological charge, zero susceptibility and no gluon condensate. That the definite vacuum is this configuration is a supplied selection.
3. Matter stays one-body (conditional lemma). If c-number links enter each history's half-tick only through hop phases and on-site potentials, which are bilinear in the modes, then each history's fermion update is a one-body unitary and a Slater determinant stays a Slater determinant (its one-body density matrix stays idempotent). For the supplied coupling (each charge couples through its own Z), a c-number link fixed by the actual configuration gives, in every history, a product of one-body phases, which cannot create entanglement from a product state.
4. Stationary levels stay (conditional on the supplied actuality law). If the odds are the same before and after a half-tick, the fewest-change transport is the identity, so the actual configuration, its current and its c-number source stay fixed.
5. Any classical (definite or classically mixed) intensity gives g2(0) = <I^2>/<I>^2 >= 1 by the Cauchy-Schwarz inequality.

Negative results kept (2026-11-14):

- N1. Product unitarity does not give |W(C)| = 1. Witness: U = diag(1, w, w^2) with w = exp(2 pi i/3) is in SU(3) and tr U/3 = 0. Inserting it on one link of a pure-gauge slice gives definite plaquettes with normalised trace 0.
- N2. A sourceless stationary point need not be flat. Witness: on a periodic L x L slice, the abelian configuration with plaquette angle 2 pi/L^2 on every plaquette, embedded in the Cartan as diag(e^{ia}, e^{-ia}, 1), satisfies the lattice Wilson-action equations with zero force and no source, with F != 0.

## Derivation

Item 1. The two diagonal generators commute, and the colour charges (1/2, 1/(2 sqrt3)), (-1/2, 1/(2 sqrt3)), (0, -1/sqrt3) are weights of their span with zero sum. On the ansatz every non-abelian term of the Yang-Mills equations is a commutator of fields in that span, so it vanishes. The static energy is |w|^2 (G(0) - G(R)) with G the lattice Green's function; G(R) > 0 gives the bound by the self-energy |w|^2 G(0), and G(R) -> 1/(4 pi R) gives the Coulomb form with |w|^2 = 1/3. For pure-gauge links U_mu(x) = g(x) g(x+mu)^dag, every closed product telescopes to g(x) g(x)^dag = 1. This telescoping is what gives trace 1; unitarity alone does not (N1).

Item 2. A configuration with every plaquette 1 has zero Wilson-action force and zero field strength. Item 2 does not say that the sourceless stationary solution is flat; N2 is a non-flat one.

Item 3. A unitary generated by a bilinear maps a Slater determinant to a Slater determinant. With the supplied coupling, the link value in each history multiplies the state by exp(-i c (Z x 1 + 1 x Z)), a product unitary.

Item 4. With cost 1 for every change, a plan with zero cost puts all mass on the diagonal, and equal marginals then force the diagonal to be p.

## Checks

The runner ends with `TOTAL: PASS=13 FAIL=0` in about 1 s and exits nonzero if any check fails. Estimates print as `ESTIMATE (not counted)` lines.

- A1: commutators of A_0 values on the ansatz 0; control: one source rotated out of the Cartan by a random SU(3) element gives nonzero commutators (0.07).
- A2: lattice Gauss law for a pair at separation 6 on a periodic 48^3 lattice, maximum residual 9.0e-17.
- A3: static energy V/g^2 from 0.0556 at R = 1 to 0.0820 at R = 12, below the self-energy bound 0.0827 at every separation; deviation from the Coulomb form 1.9% on R = 4 to 9; fitted linear term sigma a^2/g^2 = -5.1e-05 in the finite box.
- A4: every 1x1, 1x2 and 2x2 Wilson loop of a random pure-gauge SU(3) slice (5^2) has normalised trace 1 to 2e-15; Creutz ratio 0.
- A5 (N1): the witness diag(1, w, w^2) has determinant 1 and trace 0; inserted on one link it gives plaquettes of trace 0.
- C1: every plaquette of the pure-gauge slice is 1.
- C2 (N2): uniform flux on a 6 x 6 slice, plaquette angle 0.1745, maximum force 9e-16.
- E1: six modes, one random one-body generator, three particles: maximum non-idempotency 3.3e-16 after the update; control with a link-mediated n n term: 0.09.
- E2: two charge qubits: a quantised link mode (oscillator with 30 levels, coupling 0.4, mediator purity 1.000) gives concurrence 0.771; the c-number link gives at most 1.4e-17.
- F1: equal odds on 5 configurations with random allowed transitions: plan = diag(p), both marginals p, zero changes. F2 (control): unequal odds need at least the total-variation distance of changes.
- F3: minimum g2(0) over 200 random classical mixtures 1.0251; control: a one-photon Fock state gives 0.

Finite diagnostic (supplied contrast model, no error bars): fluctuating SU(2) links on an 8^3 Euclidean lattice at beta = 3.0 (heat bath, 60 sweeps to equilibrate, 20 measurements over 80 sweeps) give W11 = 0.626, W22 = 0.169 and Creutz ratios chi22 = 0.410, chi33 = 0.277, an area law; the pure-gauge ansatz value is exactly 0. This is a 3D SU(2) path sum over link odds, not the register's link registers.

## Estimates against measurement (the supplied ansatz only)

These compare the supplied ansatz with measurement, using supplied inputs (PDG masses, f_pi = 92.2 MeV, alpha_s(MZ) = 0.1180 with one-loop running and thresholds at m_b = 4.18 GeV, standard atomic constants). They are not counted as checks. They say the ansatz does not describe measured colour and light. They exclude no other definite-link configuration, and they do not show that links must carry odds.

- String tension: measured sqrt(sigma) = 440 MeV; the ansatz gives 0.
- QCD running: matter loops alone give b0 = -2 nf/3; alpha_s(m_tau) = 0.095 with matter loops only, 0.279 with gluon and quark loops at one loop, against 0.314(14) measured.
- eta': the Witten-Veneziano relation needs chi^(1/4) = 179 MeV; the flat vacuum gives 0, leaving m_eta' <= sqrt3 m_pi = 239 MeV against 957.8 MeV.
- Hydrogen 2p: quantised links (vacuum link odds, Wigner-Weisskopf, reduced mass) give tau(2p) = 1.5962 ns against 1.60 ns measured; a stationary pure level under c-number links does not decay. In a supplied classical model with radiation reaction through the dipole coherence, dP/dt = -Gamma P (1 - P), the half time from P_e = 1 - 1e-6 is 13.8/Gamma rather than 0.69/Gamma.
- Lamb shift: self-energy plus vacuum polarisation at leading order give 1069 MHz against 1057.845 MHz; c-number links keep only the vacuum polarisation, -27.1 MHz.
- a_e: alpha/2pi = 1.161410e-03 needs an internal photon, against 1.159652e-03 measured.

## Boundary

Supplied: the definite-link reading, the Cartan pure-gauge ansatz, colour SU(3) as the link group, the occupation-basis colour charges, the 48^3 periodic box, the 3D SU(2) contrast model and its coupling, the oscillator mediator and coupling used for the entanglement contrast, the random test models for the transport and for g2, the classical radiation-reaction model, and every input of the estimates. Not claimed: uniqueness of the Coulomb stationary point; any statement about definite link configurations outside the ansatz; that the definite vacuum is flat; any exclusion of definite links in general; that links must carry odds; any property of the register's link registers beyond the contrast models (their confinement, running, topology, emission rate, Lamb shift and a_e have not been computed on the lattice); that the 3D SU(2) area law carries over to 4D SU(3). The heat-bath result is a sampled finite diagnostic of a supplied model, without error bars, not a theorem about the register's tick.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records; they fix none of the inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the response law's stationary phase measured from the vacuum, the actuality law's fewest-change transport, and the proposed link registers of the update law, all from the originating three-law register. Zero premise weight; results using them are conditional on them.

## How to run

```
python3 scripts/definite_stationary_links_give_classical_coulomb_colour_flat_vacuum_one_body_matter_and_undecaying_levels_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1 s, ends with `TOTAL: PASS=13 FAIL=0` and exits 1 if any check fails.
