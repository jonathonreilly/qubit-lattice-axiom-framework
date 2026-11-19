---
claim_id: gauging_the_spin10_centre_on_five_mode_sites_pins_the_spinor_charge_as_a_static_background_and_spinor_matter_needs_fractionalised_spinons_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Supplied model: five-mode fermion sites with on-site-bilinear Spin(10); Z4 link registers (two qubits per coarse
  edge, clock C, shift S) and Gauss operators G_v = z_v prod_out C prod_in C^dag, where z_v is the site's Spin(10) centre
  generator. (A, exact) z_v = -i (-1)^F_v, so z_v^2 = -1 is a c-number, and every matter operator has Z4 charge 0 or 2
  (512 + 512 of 1024 site operators, none with charge +-1). (B-C, exact) The Gauss operators commute, satisfy G^4 = 1, are
  Spin(10)-invariant, and are kept by the S^2-dressed Spin(10) and U(5) hops; the bare hop and the S-dressed hop are not
  gauge-invariant. prod_v G_v = z_global on any closed complex, so the hard-Gauss physical sector needs (-1)^F = i^N:
  it is empty for an odd site count (L = 3 torus) and otherwise fixes the fermion parity; on the dimer the physical
  content is 2 x (1 + 45 + 210), root class only. (D-E, exact) The Z4 ground-space count on L = 2, 3, 4 tori is 4^3;
  all 24 proper cubic rotations keep the Gauss operators and plaquettes when reversed links are relabelled e -> -e,
  which is a CNOT on the link's two qubits. (Theorem) The odd part of every site's centre charge is a static
  c-number background: no gauge-invariant dynamics moves it, a 16 is never a mobile gauge charge, and charge-1 Gauss
  defects (soft Gauss law) are made only by link shifts, which are Spin(10) singlets with Levin-Wen sign +1. (F,
  exact) 16 x 16 has no singlet, 16 x 16bar has one, 16^4 has two: the minimal singlet cluster of Mott (all-even)
  sites is 4, fixing Z4 fusion for unpaired-site spinons, and spinon x local fermion is a spinor-class object of
  opposite statistics. Not shown: any deconfined phase, spinon dynamics, statistics or spatial spin-1/2."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - spin10_mott_sites_carry_no_composite_sixteen_the_centre_fixes_every_fermion_to_the_vector_class_bounded_theorem_note_2026-10-22
  - gauss_laws_as_the_local_form_of_the_tick_charge_on_four_cubed_blocks_give_a_moving_z2_gauge_tick_bounded_theorem_note_2026-10-22
  - one_qubit_site_monomial_rotations_make_c4_invariant_charges_bosons_fermions_need_a_cluster_gauge_or_a_spread_charge_bounded_theorem_note_2026-10-22
runner: scripts/gauging_the_spin10_centre_on_five_mode_sites_pins_the_spinor_charge_as_a_static_background_and_spinor_matter_needs_fractionalised_spinons_2026_10_22.py
---

# Gauging the Spin(10) centre on five-mode sites pins the spinor charge as a static background; spinor matter needs fractionalised spinons

Claim type: bounded_theorem. Runner: runner.py (TOTAL: PASS=35 FAIL=0, 0.6 s, peak 119 MB, stdout 3163 characters,
seed 20261022). It was run through scripts/runner_cache.execute_runner under the unique filename
scripts/z4_spinons_agent_test_20261022.py (status ok, exit 0); the copy was removed afterwards. The minimal axioms are
unchanged, and the register carries no premise weight.

## Question

The composite-sixteen draft proved that on a fixed set of five-mode sites with bilinear Spin(10), the centre
generator is z = (-1)^F (-i)^n_sites, so every excitation relative to a vacuum is in the vector class and a 16 is
excluded. It named route 2: deconfined spinons carrying centre charge +-i, which needs an emergent Z4 or Z2 gauge
structure. This note tests route 2 in two forms.

- Form I (literal): add Z4 link registers and gauge the centre, with Gauss operators built as in Rule G-blocks.
- Form II (emergent): the five-mode lattice fractionalises by itself, and the spinon is an unpaired site.

## Setting (supplied)

- Sites carry five complex modes. M_ab = (i/2) sum_s g_a^s g_b^s, and z_v = exp(i pi sum_a (n_{v,a} - 1/2)).
- Each coarse edge carries a Z4 register |e>, e = b1 + 2 b2, with C|e> = i^e |e> and S|e> = |e+1>. At coarse
  spacing 3 a coarse edge has exactly two interior fine sites, so the register is a two-site composite.
- Gauss operator: G_v = z_v prod_{out} C_l prod_{in} C_l^dag. The plaquette is B_p = prod S^{+-1} around p.
- Gauge-invariant hop: K_st S_l^2, where K_st = i sum_a g_a^s g_a^t.

## A. Site centre (exact)

- A1-A2. z = -i (-1)^F. So z^2 = -1 is a c-number and z^4 = 1.
- A3. z commutes with all 45 generators.
- A4. Ad_z on the 1024-dimensional site operator algebra has eigenvalue +1 (512 operators) and -1 (512), and never
  +-i. A5. Ad_z c_a = -c_a.
- Consequence: every matter operator, of any order, carries Z4 charge 0 or 2. The odd Z4 charge of a site is
  carried entirely by the c-number factor -i.

## B. Link register (exact)

- B1. C S = i S C, and C^4 = S^4 = 1.
- B2-B3. C is a phase gate on b1 times Z on b2. S^2 = X on b2 and C^2 = Z on b1. These are single-qubit Paulis.
- B4. The orientation flip e -> -e is CNOT(b1 -> b2). It sends C to C^dag and S to S^dag.
- B5. S is a two-qubit Clifford but not a Pauli.

## C. Gauss law on a dimer with one link (exact, 4096 states)

- C1. [G_s, G_t] = 0 and G^4 = 1.
- C2. K_st S^2 and the U(5) hop c^dag_{s,a} c_{t,a} S^2 commute with both Gauss operators.
- C3 (controls). The bare K_st anticommutes with G_s, and K_st S picks up -i: matter cannot couple to odd link
  powers.
- C4. The Gauss operators commute with total Spin(10), and the link is a Spin(10) singlet.
- C5. G_s G_t = z_global: the link factors cancel.
- C6. The physical subspace (G_s = G_t = 1) has dimension 512. Every physical state has (-1)^F = -1 = i^2 and
  z_global = 1, exactly one odd site, and flux e = 1 (s even) or e = 3 (s odd).
- C7. Physical Spin(10) content: Casimir values 0, 16, 24 with multiplicities 2, 90, 420, which is 2 x (1 + 45 +
  210). Root class only.
- C8. A bare S makes Gauss defects (G_s, G_t) = (i, -i) and commutes with all of Spin(10).

## D. Tori (exact)

- D1. On L^3 tori (L = 2, 3, 4) every link appears in exactly two Gauss operators with opposite exponents, so
  prod_v G_v = z_global = (-1)^F (-i)^N. The physical sector therefore requires (-1)^F = i^N:
  - N odd (L = 3, N = 27): the physical Hilbert space is EMPTY;
  - N even: fermion parity is fixed (N = 8 and 64 give (-1)^F = +1).
- D2. Z4 ground-space count 4^(E - rank d0 - rank d1) = 4^3 = 64 for L = 2, 3, 4. The cokernels are torsion-free, so
  rational ranks suffice. A fixed background charge does not change the count when the sector is non-empty.
- D3. The product of G over a 2^3 block is z_block times the electric flux through its 24 boundary links. A unit flux
  loop swept around a region therefore picks up i^(#even sites) (-i)^(#odd sites). Every site carries odd Z4
  charge, so flux loops see a background charge per site. This is the Z4 analogue of the odd Ising gauge theory
  (translation acts projectively on fluxes).

## E. Rotation covariance (exact, L = 4)

- E1. All 24 proper cubic rotations about a vertex map every Gauss operator and plaquette onto one, with e -> -e on
  links whose orientation reverses. The dressed hop K S^2 needs no relabel, since S^2 = S^-2.
- E2 (control). Without the relabel, 1344 of 1536 images fail.
- The relabel is a CNOT on the link's two qubits. At the fine level it is a two-site cluster Clifford, not a
  monomial map. At the Z4-register level it is a single-register relabelling.

## Theorem (Form I): gauging the centre pins the spinor charge (exact, from A4, C3, C8, D1)

1. The matter Z4 charge of site v is G-relevant only through z_v = -i (-1)^F_v. Its odd part, -i, is a c-number, and
   every matter operator carries charge 0 or 2 (A4). Gauge-invariant local operators can therefore change a site's
   charge only by 2 (with S^2 strings). The unit charge per site is a STATIC background.
   - Under any Gauss-conserving dynamics (a Hamiltonian, or a Rule-G-type tick, which conserves every G exactly),
     no 16 ever moves as a gauge charge.
   - Every site is permanently the end of a unit Z4 electric string. "Isolated 16s as ends of Z4 strings" is true,
     but only in the frozen sense that the sites themselves are the ends.
2. Hard Gauss law (physical states G = 1). z_global = 1 gives (-1)^F = i^N. Gauging the centre also gauges fermion
   parity: every physical state is bosonic and root class. Even the 10 leaves the physical spectrum (C7). An odd
   site count admits no physical state at all (D1).
3. Soft Gauss law (G violations allowed, as in an emergent gauge theory).
   - Charge-1 defects are made and moved only by odd powers of S.
   - S acts on links only and commutes with Spin(10) (C8). The defect carries no Spin(10) multiplet: its "centre
     charge" is a gauge label on C, not a 16.
   - All S commute, so the Levin-Wen exchange sign is +1 (G2): a boson.
   - It is C4-invariant and acted on monomially at the register level, so it is spatially a scalar. This is
     consistent with the identity theta = lambda_R sigma_R of the symmetric-emergent-fermion draft, read for Z4 Weyl
     operators.
   - The mobile charge-2 objects are the fermions c S^2 (Levin-Wen -1, G1). They are in the vector class.

Verdict on Form I: **NO.** Literal Z4 gauging of the centre is consistent and rotation-covariant, but it makes no
mobile 16. It freezes the spinor charge as a background, and with a hard Gauss law it removes all fermions. Added
link registers can only confine site 16s further (they add string energy); they cannot liberate them.

## Form II: emergent fractionalisation (exact kinematics; dynamics not shown)

The working version of route 2 needs no added links. The 16 is an unpaired site in a liquid of Spin(10)-singlet
clusters (an RVB analogue), and the emergent gauge field is the cluster-covering constraint.

- F0. Casimir identity C = 45n/4 + sum_{s<t} (10 - K_st^2)/4 re-verified against sum M^2 on the n = 2 sector.
- F1. 16 x 16 (both sites even): the weight-zero sector is empty. There is no singlet: 10 + 120 + 126.
- F2. 16 x 16bar: exactly one singlet per orientation.
- F3. 16^4 (all four sites even): exactly 2 Spin(10) singlets, out of 960 all-even weight-zero states.
- F4. An all-even cluster has centre class (-i)^n and can be a singlet only at n = 0 mod 4. In the Mott regime
  (U P_odd, every site a 16) the minimal singlet cluster is a tetramer. Unpaired-site spinons then obey Z4 fusion
  (e^4 = 1), and the spinon count is N mod 4. This is where Z4 rather than Z2 comes from: it is derived from the
  rep theory, not chosen.
- F5. Binding the local fermion c (Ad_z c = -c) to a spinon gives class (-i)(-1) = +i, a 16bar (and 144) in the same
  anyon sector. The spinor marker z^2 = -1 is kept, so the sector's invariant is the SO(10) spinor class.
- 3D statistics rule (cited, not rederived): point-particle statistics multiply, and mutual braiding is trivial.
  Since theta_c = -1 (G1), theta(e x c) = -theta(e). In each spinor sector, a 16-class and a 16bar-class object have
  OPPOSITE statistics. If the 16 spinon is a fermion, as measured matter needs, the sector also holds a bosonic
  spinor-class partner, split from it by the local fermion gap.
- LSM (cited: Oshikawa 2000; Hastings 2004; Po-Watanabe-Jian-Zaletel 2017). Every site carries a projective
  (spinor) representation of the SO(10) that acts faithfully on local operators (z^2 = -1 per site, A2). One
  spinor per unit cell forbids a unique, gapped, symmetric, short-range vacuum. A symmetric gapped vacuum must
  therefore be topologically ordered, with spinor-class anyons. The alternatives are a tetramer crystal or a
  gapless phase. This is consistent with the composite-sixteen 4-ring singlet (one tetramer). It contrasts with
  PR #9910, whose 32-mode cell has a trivial centre and a unique gapped singlet.

## Predictions of a deconfined phase (if realised)

- An extra discrete gauge field with topological order: a 4^3 = 64-fold (Z4) or 8-fold (Z2) ground space on a
  3-torus. This is not observable cosmologically.
- Stable flux lines (cosmic strings). A spinor-class object encircling one picks up i (Z4) or -1 (Z2), a 10-class
  pair picks up -1 or +1, and local bosons pick up nothing. This is an Aharonov-Bohm string felt by every 16-class
  fermion, as in the Z2 strings of SO(10) models (Kibble-Lazarides-Shafi 1982; Alford-Wilczek 1989). The string
  tension is not predicted, so there is no number to test against the CMB or pulsar-timing bounds.
- Bosonic 16bar-class partners in every fermion's anyon sector (from the statistics rule). They are not seen, so they
  must be heavy. UNTESTED.
- A background Z4 charge per site seen by flux loops (D3): crystal-momentum fractionalisation of fluxes.

## Gate

Rule "gauge the Spin(10) centre with Z4 link registers" (Form I):
1. Numbers: none.
2. Observed structure: the gauged group is the centre of the inherited Spin(10). Gauging it is a choice, and the
   link registers are supplied.
3. Unbuilt-for prediction: the physical states are all bosonic and root class, and an odd site count gives an empty
   Hilbert space. CONTRADICTED by measured fermions.
4. Axioms bent: Qubit (five modes per site, inherited). The links are two-qubit composites and bend nothing.

Result: **FAIL.** Not adopted.

Reading "matter = spinor-class anyons of a fractionalised five-mode lattice" (Form II):
1. Numbers: none.
2. Observed structure: nothing new by name. Z4 fusion follows from F1-F4, and the need for topological order from
   LSM.
3. Predictions: opposite-statistics spinor-class partners, AB flux strings, Z4 fusion of spinons. All UNTESTED.
   Nothing derives the spinon's fermion statistics or spatial spin-1/2. On monomially rotated sites the unpaired
   site is a spatial scalar; spin-1/2 would have to come from the spinon band (Dirac nodes of a flux state). Not
   computed.
4. Axioms bent: Qubit (five modes per site, inherited).

Result: **UNTESTED; not adopted.** It is the surviving form of route 2. Its open item is dynamics: a deconfined
spinon phase of a Spin(10) five-mode model in 3D, with fermionic spinons.

## Smuggling review

- Supplied: five modes per site and the bilinear Spin(10) (inherited); the Z4 link registers and the Gauss form;
  the S^2 dressing; coarse spacing 3 for two-site links; cluster sizes; seed.
- Forced (exact): A1-A5, B1-B5, C1-C8, D1-D3, E1-E2, F0-F5, G1-G2, and the Form-I theorem.
- Cited, not rederived: LSM-type theorems, 3D statistics composition, cosmic-string AB literature.
- Speculative: every item under "Predictions" and the spin-1/2 route.

## Used / narrowed / cited

- composite-sixteen: route 2 tested. The literal-gauging form fails. The emergent form survives, now with derived
  Z4 fusion and an LSM reason that a gapped symmetric vacuum must fractionalise. Its phrase "the only route keeping
  the axioms" is narrowed to "a route keeping the axioms".
- rule-g-blocks: the same Gauss construction lifted to Z4. Its exact conservation of every G implies here that the
  odd charges are frozen.
- symmetric-emergent-fermion: the theta = lambda sigma reading gives a bosonic, scalar charge-1 defect. Fermionic
  charges are the charge-2 c S^2 objects (vector class).
- PR #9910 (32-mode cell, trivial centre): consistent contrast.
- Literature: Oshikawa 2000; Hastings 2004; Po-Watanabe-Jian-Zaletel 2017; Moessner-Sondhi-Fradkin 2001 (odd gauge
  theories); Levin-Wen 2003; Kibble-Lazarides-Shafi 1982; Alford-Wilczek 1989.

## Boundary

- Dimer, single-mode Levin-Wen stars, n <= 4 Casimir sectors, coarse tori L <= 4 (combinatorial).
- No Hamiltonian phase diagram, no deconfinement, and no 3D spinon band.
- The LSM and statistics-composition statements are cited.
