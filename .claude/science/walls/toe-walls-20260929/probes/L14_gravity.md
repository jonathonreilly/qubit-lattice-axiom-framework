# Lane L14: Gravity — walls

> **Path key and labels (read once).**
> - `MAP` = `docs/TOE_VIABILITY_MAP_WHERE_THE_AXIOMS_ARE_EXPOSED_AND_THE_FASTEST_DECISIVE_TESTS_2026-09-27.md` on branch `origin/claude/toe-viability-probes-20260927` (PR #9363, open, not on main). `EX` = `.claude/science/exercises/gravity-wall-finite-records-20260929/` on the same branch (exercise run by an Opus 5.5 supervisor with Fable route/kill agents: same family, unrefereed). `P<n>` = probe n note in `docs/` on that branch; each note's `claim_scope` is line 4. Prefixes: P3 `ONE_LIGHT_CONE_UNDER_INTERACTIONS…`, P4 `IF_THE_MEMBERS_LEADING_ACTION_RESPECTS…`, P6 `THE_WALKERS_SEA_FEELS_THE_SHAPE…`, P10 `ONE_QUBIT_PER_SLOT…`, P11 `THE_INCOMPRESSIBLE_TENSOR_PATTERN…`, P12 `A_LAPSE_SET_BY_RECORD_EVENTS…`, P13 `THE_LAMBDA_ONE_QUESTION…`, P14 `A_QUANTUM_LINK_DEFORMATION…`, P15 `THE_SWAPPED_QUANTUM_LINK_ASSIGNMENT…`, P16 `THE_PHOTON_TRIPLET_COMPOSITES…`, P17 `AN_EXACT_ADDITIVE_GAUSS_LAW…`, P18 `BREAKING_THE_MOMENTUM_RULE…`, P19 `THE_OWNERS_FROZEN_BOX_READING…`, P20 `EVERY_GAUSS_LAW_COMPATIBLE_MOVE…`, P21 `THE_TENSOR_COMPLEX_ON_FINITE_SLOTS…`.
> - `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`. Two block-number series exist and both reach the 150s and 160s: the September admissibility induced-law series (`ADM-bN`, blocks 53-170; main has blocks up to 152, later ones are held branches) and the August Dirac–Kähler "toe-axiom-closure" series (called "August block N" below; blocks 103-173). `ADM-bN` = the landed block-N note on main, `docs/ADMISSIBILITY_RULE_<prefix>…` (claim scope line 4): b53 `NO_MASTER_CLOCK…`, b55 `ACTION_AND_REACTION…`, b59 `BOND_RATES_AND_LENGTHS…`, b60 `A_LEDGER_LINEAR_IN_THE_RATES…`, b62 `ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME…`, b69/72 `WHICH_SPECIES_FALL…`, b76 `THE_FILLED_SEAS_ENERGY…`, b97 `A_RECORD_THAT_CANNOT_READ_THE_FIELD…`, b100 `INERTIA_AND_THE_RULES_WEIGHTS…`, b105 `IN_DISCRETE_TICKS…`, b106 `NO_LOCAL_MOMENTUM_FALLS…`, b110 `AROUND_A_BODY_THE_WALKS_RAYS…`, b111 `RECORDS_IN_A_CLOCK_GRADIENT…`, b112 `THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA…`, b129 `BLOCK_60S_DECLARED_NUMBERS…`, b120 `ONLY_THE_TWO_STEP_CURRENT_CAN_SOURCE…`, b121 `UNDER_ONE_RECORD_PER_SITE_THE_SOURCE_IS_THE_COMPRESSED_DENSITY…`, b135 `ONE_LIGHT_CONE_EXACTLY…`, b137 `ONE_RECORD_PER_SITE_KEEPS…`, b141 `ONE_RECORD_PER_SITE_NO_POSSIBILITY_SHIFT…`, b143 `EXACT_BOOKS_NEED_RECORDS…`, b145 `BINDING_ENERGY_FALLS…`, b147 `THE_MEMBERS_ZERO_MODE…`, b150 `EVERY_CLOCK_PROFILE_A_RELABELLING…`, b151 `NO_FINITE_RANGE_INTERACTION…`, b152 `UNDER_ONE_RECORD_PER_SITE_A_COLLISION…`. Other `docs/…` names are shortened to an unambiguous prefix plus `…`.
> - Labels: **proved** = landed note (on main) or sol-confirmed on PR #9363; **checked** = a test I ran (scripts and outputs in `L14_scratch/`); **suggested** = argument not yet checked; **reading** = interpretation. Every gravity-family note is ledger-`unaudited` (formal audit is deferred by the owner until a solid TOE), so "proved" never means audited.

## Lane map (under 200 words, plain language first)

**What the lane is for.** To show that gravity (Newton's law and constant, bent light, gravity waves, Einstein's equations) comes out of a lattice of qubits with permanent records, instead of being put in by hand.

**Best result.** Given supplied clock rates and lengths per site, the walker's clocks slowed by records give a 1/r pull, and a declared "curvature member" doubles light bending and matches GR's static second-order terms (blocks 53–62, 112, 134–152: landed, conditional). With continuous numbers at each site the linearised Einstein spectrum is exact (2026-09-24 comparator).

**Where it stands.** The roughly 170 gravity-family notes are all unaudited, and none is a registered obligation. PR #9363's probes 10–21 and its exercise show that finite sites with exact local rules give gravity waves that are too slow, or light-fast with an extra helicity-1 wobble. The axioms say nothing about gravity (AX:116-123, 185-190): every route supplies its own metric, clock or tensor. The owner decision (continuous geometry per site, recorded adjacency, or neither) is pending.

## Walls

### L14-W1: No finite-site graviton with Einstein's spectrum (too slow, or a wobble comes with it)
- Plain: Einstein's gravity waves have two fingerprints: light speed, and one shape only, a stretch-and-squeeze across the direction of travel. Every way tried to build them from finite, record-like pieces on the fixed grid misses one. Strict local rules make the waves crawl. Loosening the rules makes them light-fast but adds a sideways wobble the double pulsar excludes unless it runs more than twelve times faster. Only continuous numbers at each site have worked.
- Precise: Target: a local (finite range, analytic symbols), stable (positive-semidefinite) harmonic model on the supplied tensor complex (vector stencil G, scalar stencil S, six slots per cell), finite-dimensional slots, time (scalar) rule exact, whose low-energy spectrum is exactly two pure-TT modes with ω ∝ |q| in every direction and no other gapless mode. Result at the harmonic level, both storage assignments (momentum stored, or metric stored): if every transverse slide is exact then ω_TT = O(q²) (O(q³) with the energy rule too); if both TT polarisations are linear in every direction then some linear mode carries helicity ±1 weight on a dense set of directions, whatever the residual symmetry; if both rules are soft, everything is gapped. Comparator: non-compact canonical pairs give exactly Einstein's linear spectrum, and no finite site carries an exact canonical pair (trace argument). Not shown: strongly correlated states, non-local terms, composite metrics beyond those tested, a softened scalar rule, and the axioms' own one-qubit site.
- Evidence: EX/WALL.md:41-114 (wall stated twice), :115-133 (three columns); EX/SUMMARY.md:14-55, :125-140; EX/ASSUMPTIONS.md:64-92 (reduction, price); P10:4, P15:4, P17:4, P18:4, P20:4, P21:4; MAP:396-416, :1011-1047; docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_…_2026-09-14.md:25-33; docs/TENSOR_LINEAR_DISPERSION_NEEDS_OSCILLATOR_SLOTS_…_2026-09-24.md:4; docs/NO_PER_SITE_BOSONIC_CCR_THEOREM_NOTE_2026-05-02.md.
- Axioms / supplied / proved:
  - Axioms: fixed Z³ with nearest-neighbour adjacency (AX:37); one-site domain M₂(C) (AX:47); Admissibility "is not a dynamics axiom" and defines no time metric (AX:116-123). Nothing on tensors, gravity or dynamics.
  - Supplied: the tensor complex with finite spin-S slots, harmonic stable local Hamiltonians, the exact time rule, and Einstein's spectrum as the target (EX/WALL.md:115-133).
  - Proved: the dichotomy above (bounded theorems, sol-confirmed on PR #9363, unaudited, not on main); the 09-14, 09-24 and 05-02 notes are landed (unaudited). Checked: I re-ran the exercise's T1 script and its output is identical to `EX/scripts/T1_output.txt` (`L14_scratch/ex/scripts/T1_rerun.txt`).
- Tried already: P10 (exact q⁴ sum rule), P11 (incompressible photon-triplet composite carries ±1 partners), P14 (quantum-link scalar constraint, not first class), P15 (swap: metric diagonal, still ω ~ q²), P16-P17, P18 (on-site stiffness: TT linear, ±1 partners move, c₁² = c₀²/2 + c₂²/4), P20-P21 (every move set, every residual symmetry) — EX/WALL.md:23-31. Five routes around the wall died in the exercise (EX/SUMMARY.md:58-66). Large-spin/Holstein–Primakoff: its Gaussian version meets the landed finite-penalty instability (MAP:975-980).
- Same wall elsewhere: the June "universal GR" lane ends at "a metric degree of freedom must be supplied" (EX/SUMMARY.md:98-101) = L14-W7; partner half = L14-W2; composite exit = L14-W3; L04 (one light cone, 3+1); L06 (the landed photon lane is the vector version of the same construction; MAP:801).
- Why it matters: while it stands the TOE has no graviton on finite sites: gravity waves, and Einstein's equations at wave level, cannot be derived from the qubit lattice as supplied. The owner is asked which premise moves (MAP:1154-1176).
- Cheapest known test or next step: (1) write the price once as a refereed note stating the three exits (EX/SUMMARY.md:103-110; 1-2 days; the corollary proof and check are in `EX/scripts/agents/`); (2) the owner's A/B/C decision (MAP:1069-1152); (3) the untested scope hole: a non-harmonic method for one qubit per site with exclusion instead of stiffness (P21:4).
- Severity: blocking
- Status: priced (three named exits: (a) continuous unbounded local variables, (b) rules broken at order one in the vacuum with no controlled model, (c) a composite graviton with an unnamed gapping mechanism; EX/SUMMARY.md:125-140). Scope caveat: possibly misframed at the level of the axioms, since the one-qubit site is untested.

### L14-W2: Einstein's wrong-sign conformal mode is needed, and a ground state cannot supply it
- Plain: Einstein's own theory has one direction, the overall size of space, whose energy runs backwards; his time rule hides it. To remove the wobble from a lattice graviton, the lattice would need that backwards-running direction too. A system in its lowest-energy state cannot have it. Forcing it gives a knife edge, a ghost and a flat gapless band. The same sign problem shows up in every gravity lane.
- Precise: Probe 11's isotropy identity 4v₁ = v₂ + 3v₀ makes a pure spin-2 light-like wave need a negative compression weight v₀ = −v₂/3. In probe 18's isotropic model this is α* = −β/2: helicity ±1 modes then have ω² = 0 to 1e-15 at every q up to 1.5 (a flat band, still gapless), the helicity-0 mode is a tachyon (growth 2.45 m at the zone corner) or, with a Fierz–Pauli stiffness, a frozen ghost; 1 % detuning brings back partners or an instability. The f-sum of a ground state is positive. Einstein's trace (conformal) direction has the wrong kinetic sign: at k = 0 the uniform dilation is negative, while at k ≠ 0 the λ = 1 DeWitt form is positive semidefinite on the momentum-constraint sector, with the negative direction removed by the scalar (time) constraint (P13 (A)); only λ = 1 closes the lapse algebra (b112: β = −α). June lane: the conformal channel has μ_conf < 0, and with a degenerate trace = shear supermetric one channel is always unhealthy. b129: positive rest-content forces the homogeneous kinetic coefficient c_k < 0. Scope: harmonic, one isotropic model, no interactions.
- Evidence: EX/TESTS.md:3-60; `EX/scripts/T1_output.txt`; EX/agents/kill2_nonground_a1.md (F3, items 1-7); EX/SUMMARY.md:74-84; P11:4, P12:4, P13:4; docs/UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_…_2026-06-08.md:1-40; docs/UNIVERSAL_GR_SAKHAROV_GNEWTON_INDUCED_RESIDUAL_…_2026-06-17.md:45-50; ADM-b112:4; ADM-b129:4.
- Axioms / supplied / proved:
  - Axioms: silent on state or dynamics; the `realized_state_primitive` supplies a state only as data and selects none (PRIMITIVE_REGISTRY_CHECK).
  - Supplied: a ground-state (positive-weight) or population-inverted channel; the DeWitt kinetic term.
  - Proved: T1 and the identity (bounded, sol-confirmed on the PR); checked by me (T1 rerun identical). Landed: the June degenerate-supermetric sign no-go (unaudited).
- Tried already: F3 (a pumped, non-ground state) is dead: EX/ROUTES.md:26, EX/TESTS.md:41-60. The Hojman–Kuchař–Teitelboim route makes the negative direction gauge rather than populated, which is option A again (EX/APPROACH_REGISTRY.md row F3). P14's quantum-link deformation keeps DeWitt weakly invariant but is not first class. The 06-09 3+1 fiber-metric note is a target-operator certificate only (docs/UNIVERSAL_GR_3PLUS1_CONSTRAINT_MULTIPLIER_…_2026-06-09.md:1-20).
- Same wall elsewhere: the June lane (G > 0 residual, L14-W12); the member programme (b112, b129, P12-P13); Gibbons–Hawking–Perry (reference only). L13 (conformal mode in cosmology).
- Why it matters: it is the mechanism that stops a finite-slot graviton from being pure, and the same sign underlies why gravity attracts (L14-W12).
- Cheapest known test or next step: specify and run test A1 (L14-W6); or find a rule that makes the trace direction gauge on finite slots (P13 says diagonal clock encodings cannot; P14 is partial); test the inverted channel's stability under matter coupling (EX/agents/kill2_nonground_a1.md item 5).
- Severity: blocking
- Status: open

### L14-W3: A composite graviton's extra modes have no known gapping mechanism
- Plain: One way out keeps finite sites and exact rules: build the graviton as a bound state of simpler fields, for example three photon-like fields. It can look light-speed and pure at first, but its unwanted partners then have to be removed by some strong-coupling effect. None is known. The one literature candidate, from Gu and Wen, is called unreliable by its own authors.
- Precise: With an exact additive rule on spin-type slots, the TT electric density is dipole-conserved and has no local conjugate. A linear TT mode with a local Einstein-normalised metric is then a composite (stored field a derivative of its momentum, as in P11's E = curl Ã), and its helicity ±1 (and 0) partners cannot be gapped by any gauge-invariant local harmonic term (P16). The terminal obligation is a non-perturbative mechanism that gaps the constituents' partners while TT stays linear. Cauchy–Schwarz cross-check: an O(1) local conjugate would force an anti-Newtonian static TT response (χ_h ≥ |⟨[h,E]⟩|²/(C_H q⁴)). Not excluded: beyond harmonic order.
- Evidence: EX/ROUTES.md:24-25; EX/agents/kill1_price_strong.md (F2, items 1-4); EX/APPROACH_REGISTRY.md (row 2); EX/SUMMARY.md:85-90; EX/OUTSIDE_VIEW.md (Gu–Wen, Xu–Hořava rows); P11:4; P16:4.
- Axioms / supplied / proved:
  - Axioms: silent.
  - Supplied: exact additive Gauss rule, photon-triplet composite, spin-type slots.
  - Proved: P11, P16 (sol-confirmed on PR, unaudited). Suggested: the dipole-conservation corollary and its Cauchy–Schwarz cross-check (same-family kill agent, unrefereed; `EX/scripts/agents/bogoliubov_check.py`).
- Tried already: P11 T1 and P16 (harmonic). An exact-diagonalisation test on ~20 slots cannot separate the tails (EX/agents/kill1_price_strong.md item 4).
- Same wall elsewhere: L14-W1 (exit c); L06 (the photon lane supplies the constituents).
- Why it matters: it is the only in-domain exit that keeps finite slots and exact rules; if it is empty, the owner's options reduce to the axiom changes in L14-W1 and L14-W4.
- Cheapest known test or next step: none known ("name a mechanism, or stop", EX/SUMMARY.md:103-110, route 3); reopen only with a named mechanism.
- Severity: major
- Status: open

### L14-W4: The two owner-level exits that keep the axioms' finite sites (recorded adjacency; strongly correlated or non-local gravity) have no bounded test
- Plain: If continuous numbers per site are refused, two choices remain: let the grid's connections themselves be the geometry, or say gravity is a strongly interacting many-body pattern with no simple wave description. For neither is there a test anyone can run. The first also makes the Record axiom circular, because records sit on sites that would then be made of records.
- Precise: Option B (changes Lattice): "which sites neighbour which is itself recorded"; needs Record and State reworded; as written it is circular; the relabelling trilemma of the 09-26 panel returns; no bounded test exists; quantum-graphity literature gives a lattice at low temperature and no graviton (reference only). Option C (no change): gravity is a strongly correlated or non-local pattern; no bounded test; the harmonic results do not cover it (P21:4 "Not shown").
- Evidence: MAP:1105-1152; EX/ASSUMPTIONS.md:21 (A1), :41-50 (routes B, C); EX/WALL.md:33-38 (not tried in the repo); EX/agents/agent2_quantum_gravity.md ("Known no-gos and escapes").
- Axioms / supplied / proved:
  - Axioms: fixed Z³ adjacency (AX:37); records lock one possibility per site and are "permanent" (AX:77-83), which presupposes sites.
  - Supplied: nothing for B or C.
  - Proved: nothing; no model exists.
- Tried already: nothing in the repo (EX/WALL.md:33-38).
- Same wall elsewhere: L01 (what a record is; the same circularity), L04 (a Z⁴ event-lattice reading of Lattice; MAP:650-660).
- Why it matters: these are the only routes that do not touch the Qubit axiom. If continuous geometry per site is refused, gravity has no route at all.
- Cheapest known test or next step: for B, find a minimal dynamical-graph model with a known graviton limit (EX/ASSUMPTIONS.md route B, first test); for C, a small-system test of TT incompressibility (route C, first test).
- Severity: major
- Status: open

### L14-W5: Gravity as an equation of state of entanglement does not work on the fixed cubic grid
- Plain: One way to avoid a graviton field is to get Einstein's equation from how entanglement grows with area. On this grid the entanglement per unit area differs by 16–18 % between cut orientations, so there is no single coefficient, and the derivation needs a metric and boosts the axioms do not supply. I reproduced the orientation difference with my own code.
- Precise: Jacobson-type derivation needs a Lorentzian metric to define diamonds and area, a boost-KMS temperature (Lorentz invariance of the vacuum), a rotation-invariant universal coefficient η, and CFT or holographic matter. Numerics: cubic Wilson–Dirac sea, lower band filled: S/Area for a (110) cut over a (100) cut is 1.161–1.175 for m = 0, 0.1, 0.5, converged in slab thickness. With a Fermi surface instead, S ~ L² ln L and there is no η. The area coefficient 1/4 itself is also not derived (L15).
- Evidence: EX/agents/kill3_entanglement_statics.md (F4, items 1-5); EX/ROUTES.md:27; EX/SUMMARY.md:91-97; `EX/scripts/agents/kill3_area_law_anisotropy.py`; docs/BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE.md; docs/PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md:199-276 (area-law family, Target 2).
- Axioms / supplied / proved:
  - Axioms: no metric, no boosts, no time metric (AX:116-123, 185).
  - Supplied: a free-fermion Wilson–Dirac sea and a bipartition; the Markov-field reading of records (an added premise).
  - Proved: nothing for the route. Checked (mine): `L14_scratch/area_law_anisotropy_check.py` (own code, own gamma matrices, Peschel method) gives a (110)/(100) ratio of 1.1747 at m = 0.5 (stable to 5 digits across transverse grids 16²-32² and blocks of 30-50 sites) and 1.1639 at m = 0.1, matching the kill agent's 1.175 and 1.164. The m = 0 value 1.161 was not re-run. Suggested: the list of Jacobson's required inputs.
- Tried already: kill3 numerics; route F4 retired (EX/APPROACH_REGISTRY.md row F4). The 04-25 area-law no-go family concerns the ¼ coefficient (L15).
- Same wall elsewhere: L15 (area law, the ¼ coefficient), L04 (boosts).
- Why it matters: it closes the escape that needs no lattice graviton mode.
- Cheapest known test or next step: none inside the axioms. Reopen only with a lattice whose η is isotropic (not Z³) or a derivation of boosts (EX/APPROACH_REGISTRY.md row F4).
- Severity: major
- Status: open

### L14-W6: Nonlinear closure of gravity's constraint algebra on the fixed lattice
- Plain: Einstein's theory hangs together only if its rules keep working when the field is strong, not just for small waves. On a fixed grid that is known to be hard, because the tools that guarantee it fail for lattice brackets. At small amplitude the clock rules close only at one special ratio. Beyond that the walker's clocks close only for uniform lapses. The test that would settle the next order is not yet specified.
- Precise: Target: a local lattice completion of the hypersurface-deformation algebra at second order in the fields, {C[N], C[M]} = G[ξ(N, M, fields)], with a cubic correction to the time rule, a quadratic correction to the momentum rule and a field-dependent structure function (range ≤ 2, cube symmetry). Known: at linear order the member's bracket closes exactly iff β = −α and each face term is timed symmetrically (b112: three symmetric timings coincide, one-corner timing fails); the walker's clock algebra matches only when one lapse is uniform, the defect for arbitrary pairs starts at third order in wave number, and no finite-support energy placement with the cube's rotations and time reversal closes it against nearest-neighbour relabellings (b150 T5(d), extreme-hop witness t = (4,2,2)); the full coupled algebra's cross terms are open. Test A1 is pre-registered, FAIL expected, and unspecified (bases, timing, criterion). The June Ward identities to quintic order are finite-lattice residual diagnostics at L = 6, 8, not an all-order closure.
- Evidence: MAP:255, :1161-1215; ADM-b112:4; ADM-b150:4, :43-52, :223; docs/UNIVERSAL_GR_EINSTEIN_HILBERT_CLOSURE_SYNTHESIS_…_2026-06-08.md:58-81 ("Boundaries", "What Is Not Claimed"); EX/agents/kill2_nonground_a1.md (F8); EX/agents/agent2_quantum_gravity.md (Route 3); EX/SUMMARY.md:111-124.
- Axioms / supplied / proved:
  - Axioms: no dynamics, no relabelling group, no Leibniz/Jacobi structure on lattice brackets (AX:116-123).
  - Supplied: the constraint stencils, the symmetric face timing, the walker's placements of energy and momentum.
  - Proved: b112 and b150 (landed, unaudited; b150's scope: "the full coupled algebra, whose cross terms remain open"). Literature (Hojman–Kuchař–Teitelboim, Bahr–Dittrich) is reference only.
- Tried already: b112 (step A0); b150 T5/T5(d); held blocks 157-164 (cubic completion at leading order; programme T closed at first order in the strain; unlanded, in memory `campaign-20260926-12h.md`); June cubic/quartic/quintic Ward diagnostics.
- Same wall elsewhere: L14-W2 (closure forces λ = 1), L14-W13 (books), L14-W7; L02 (dynamics).
- Why it matters: without nonlinear closure the lane has at most linearised gravity: no Einstein equations, no strong field, no self-consistent gravity waves.
- Cheapest known test or next step: fix A1's specification (monomial bases, supports, parity and time-reversal assumptions, one of b112's three face timings, treatment of null terms, the criterion), then run the finite linear-algebra PASS/FAIL (MAP:1178-1211). A FAIL at range ≤ 2 would not exclude longer-range or non-local corrections.
- Severity: blocking
- Status: open

### L14-W7: The geometric carrier (metric, clock rate, lengths, tensor slots) is supplied; there is no Record-to-geometry map
- Plain: Every working piece of gravity in the repository starts from something the axioms do not contain: a metric with continuous lengths and angles, a tick rate per site, or a tensor field. The step from records to geometry has never been built: no records-to-event-order map, no derived clock rate, no lengths from records. Gravity therefore comes out only relative to a supplied geometry.
- Precise: Target: derive from Lattice, Qubit, Admissibility and Record alone a Lorentzian conformal class (light cones), a conformal factor (clock rate) and dynamical lengths and angles, so that the metric is an output. (i) The 2026-06-06 note names six typed open bridges: record atom → formation event; event dependency order; common event set with the Lieb–Robinson bound; quasilocal LR composition with declared weight; LR envelope → exact causal relation; causal set → Lorentzian manifold; its earlier "records derive the conformal class" was withdrawn 2026-07-16, and the clock rate is a retained no-go. (ii) The June Sakharov lane induces the action but posits the metric degree of freedom. (iii) The September Regge notes state that the axioms "do not supply dynamical edge lengths, the Regge action or its orientation, a physical clock, Lorentzian reconstruction, or a Record-to-geometry map". (iv) The source-link lane's clauses C1-C3 (tick rates) and the tensor lane's continuous slots supply per-site continuous quantities that are not records.
- Evidence: docs/EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_…_2026-06-06.md:10, :77-100; docs/POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md; docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md; docs/UNIVERSAL_GR_SAKHAROV_…_2026-06-17.md:45-64; docs/THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_…_2026-09-03.md:26-29; docs/REGGE_EXACT_REDUCTION_POSITIVE_TENSOR_TRANSFER_…_2026-09-13.md:25; MAP:1059-1067; EX/SUMMARY.md:98-101; EX/WALL.md:115-133.
- Axioms / supplied / proved:
  - Axioms: no metric, no time metric, no record-production dynamics (AX:116-123, 185-186).
  - Supplied: tick rates (ADM-b53 clause C1-C3), lengths (b59-b61), vielbein/edge lengths (Regge notes), the tensor complex (09-14 note).
  - Proved: exact conformal/scale algebra (null cones fix a class, not a scale); the record-history order/rate firewall (a no-go). Stale dependency: docs/GRAVITY_CONFORMAL_SCALE_SPLIT_…_2026-06-06.md still cites the withdrawn conformal-class claim.
- Tried already: the June lane (2026-06-06 to 06-18); the July "energy sources gravity" proxies ("proxies typed, no bridge derived", archive/chains/july-mass-source-poisson-era.md:44-45); the causal-time lane (cycles 610-679, L04).
- Same wall elsewhere: L04 (time metric, causal order), L01 (record → event map), L14-W1, L14-W10.
- Why it matters: this is the axiom-level statement of the lane's wall. As long as the geometry is supplied, "gravity from the axioms" is a conditional statement.
- Cheapest known test or next step: the owner's A/B/C decision (MAP:1069-1152); price option A first by computing the induced helicity ±1 block in probe 6's runner (about a day, FAIL expected; EX/SUMMARY.md:103-110, route 2). The first bridge (`record_atom_to_formation_event_map`) needs L01's formation rule.
- Severity: blocking
- Status: open

### L14-W8: Einstein's action itself is not derived (direct route blocked; induction needs the metric posit and may not give the Einstein form)
- Plain: Even given a metric, the repository has not shown that the lattice produces Einstein's gravitational action. The direct route from the determinant of the Dirac operator lacks a step. The induced-gravity route needs the metric to exist as a field, and on a fixed lattice it may not give the Einstein form at all, only mass-like terms and direction-dependent speeds.
- Precise: Direct-universal route: no retained curvature-localisation operator Π_curv identifies the Hessian of W = log|det(D + J)| with Einstein/Regge dynamics on PL S³ × R; the route-exhaustion no-go closes five construction routes locally (not an absolute no-go). It rests on the axioms' open gates: log-det readout (AX:180) and the staggered-Dirac/finite-Grassmann realisation (AX:178). Induced route: Sakharov gives 1/(16πG) ~ Λ² N_f, needs a supplied metric field, and its sign is convention-sensitive; the sea's induced clock stiffness is not the curvature member (b76; landed scope says no induced stiffness is established); on the hypercubic surface any relabelling-invariant induced leading action must be Fierz–Pauli, and whether a lattice coupling achieves that is open; the induced TT block shows birefringence κ_E/κ_T = 3.9 and a q-independent (mass-type) block; with the metric as a fixed background nothing propagates (P6 T8: the sea's ⟨TT⟩ is a continuum, Im χ ∝ ω⁴, no pole; free walkers carry no spin-2 mode).
- Evidence: docs/UNIVERSAL_GR_PICURV_ROUTE_EXHAUSTION_NO_GO_NOTE_2026-06-18.md:13-47; docs/UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md:49-52, :172; docs/UNIVERSAL_GR_SAKHAROV_…_2026-06-17.md:26-50; ADM-b76:4; P6:4 (T3, T8); MAP:562-574, :707-745; EX/ROUTES.md:28; EX/agents/kill4_induced_purity.md (F5).
- Axioms / supplied / proved:
  - Axioms: neither the Dirac carrier nor a log-det readout (AX:178-181).
  - Supplied: the scalar generator W, the PL S³ × R lift, the tensor Hessian candidate, the conserved coupling D(P_eff) + √g, a vielbein background.
  - Proved (landed, unaudited): the exact scalar generator and A1 projector; the isotropic glue operator on invariant backgrounds; finite-lattice Ward-identity residuals to quintic order that fall from L = 6 to 8 (diagnostics only).
- Tried already: the Π_curv exhaustion (06-18); tensor-action blocker (04-14); λ-bypass; 3+1 fibre-metric note (06-09); Sakharov (06-17); block 76; probe 6 (T3, T8, T10).
- Same wall elsewhere: L14-W1 (induction = option A relabelled, EX/ROUTES.md:28); L14-W7; L02 (log-det readout and action).
- Why it matters: without the action the lane has kinematics (a spin-2 wave), not Einstein's equations.
- Cheapest known test or next step: compute the induced helicity ±1 block in P6's runner (one projector; EX/ROUTES.md rank 2); compute a lattice-regulated Einstein–Hilbert coefficient for a fixed matter content (MAP:572-574).
- Severity: major
- Status: open

### L14-W9: The curvature member (and so light bending by twice the Newtonian value) is declared, not forced
- Plain: The clock-only law bends light by half the Einstein value. Getting the full factor needs the lattice also to stretch space near a body, which the clock law does not do: a body at rest sources no lengths. The repository gets the factor 2 by declaring an action whose exponent, linearity in the clock rates, stiffness and sign are chosen rather than derived.
- Precise: Blocks 53-57 (clauses C1-C3, "no master clock", kept ledger) give bending/fall ratio 1 (half of GR). b59: the ratio is 1 + β with β a free stiffness ratio because a body at rest sources no length. b60: a ledger linear in the rates plus the declared bilinear member (p = 1, c = 8K) gives β = 1 (bending ×2); the member is declared, so linearity in the rates, the exponent p, K and the sign of c_k are not forced. b129: unit-free speeds force s = p + 2, positive content forces c_k < 0, p = d − 2, and only K and α/K stay supplied. b110: the walk's rays match the comparator's at every order exactly when its two charges agree, which happens only when hop energy balances the slowed clocks. P4 (conditional): if the member respects the hypercubic tick surface it is unique, with β = −α and α = K/4, but that is an added premise for the member. The static second-order terms (perihelion) are landed (b144, b145), conditional on the member.
- Evidence: ADM-b59:4, ADM-b60:4, ADM-b110:4, ADM-b129:4, ADM-b145:4; P4:4; MAP:254; MAP:507-522; EX/agents/kill3_entanglement_statics.md (F7, item 3); EX/ROUTES.md:30.
- Axioms / supplied / proved:
  - Axioms: silent on rates, lengths and actions.
  - Supplied: clauses C1-C3; the rate-and-length field; the member's exponent, K and sign; the walker's coupling.
  - Proved (landed, conditional, unaudited): the above identities. A held block 159 says static bending does not select the member (memory `campaign-20260926-12h.md`).
- Tried already: blocks 59-62, 110, 129, 144-145; P4; F7 (statics first) is dead because it is already landed (EX/ROUTES.md:30).
- Same wall elsewhere: L14-W8 (Einstein action), L14-W16 (α = K/4), L14-W11 (K versus G).
- Why it matters: light bending, perihelion and the graviton's speed all inherit these numbers; the TOE gets GR's static values only by declaration.
- Cheapest known test or next step: derive or exclude the declared numbers from a relabelling-invariance requirement on an induced action (the L14-W8 test), or adopt the hypercubic-tick premise for the member (MAP:507-522, owner decision 2).
- Severity: major
- Status: priced (equivalent to declaring the curvature member and the hypercubic-tick surface for it)

### L14-W10: The source/action bridge: what sources gravity, and with what absolute strength and unit
- Plain: Gravity has to know what makes it: energy, a record count, or a compressed density, and with what strength. The axioms list "source/action identification" as an open gate. The lattice lane assumes the source is the walkers' energy when a ledger is kept. Nobody has derived that assumption, and the strength is still free.
- Precise: Target: a derived map from records or possibilities to a gravitational source, with an absolute source-response-unit law consumed by the same gravity carrier. The physical source-action bridge "remains OPEN" (cycle 871 note). The August "pincer" note shows that homogeneous conservation, linear response with a free coupling and normalised shape do not choose a positive amplitude; the shortest remaining bridge is a branchwise Record source plus an absolute law. b55: the source is the amplitudes' energy density only if the (rate field, amplitudes) pair keeps a ledger, a supplied premise (the axioms contain no conserved energy). b121: for supplied position-excluding pair dynamics the source is the compressed local energy density (open chains; no exact momentum force, passive mass or action-reaction theorem). b120: only the two-step current can source b62's member (no real finite-range translation-invariant placement of the fixed site response or the one-step current works for all stationary plane-wave states). The gravity mainline / source-action program is named in wake conditions of two owner-decision entries (DEFERRED_DECISIONS entries 3 and 6).
- Evidence: docs/SOURCE_ACTION_BRIDGE_PRICING_CYCLE871_…_2026-07-28.md:44; docs/ADMISSIBILITY_D4_NORMALIZED_RECORD_PAIR_SOURCE_GRAVITY_PINCER_…_2026-08-31.md:38-39; docs/repo/DEFERRED_DECISIONS.md:21-49 (statistical bridge), :111-112 (entry 3 wake 1), :198-202 (entry 6 wake 1); AX:187; archive/chains/july-mass-source-poisson-era.md:44-45; archive/chains/july-source-era.md:56; ADM-b55:4; docs/ADMISSIBILITY_RULE_ONLY_THE_TWO_STEP_CURRENT_CAN_SOURCE_…_2026-09-24.md:4; docs/ADMISSIBILITY_RULE_UNDER_ONE_RECORD_PER_SITE_THE_SOURCE_IS_THE_COMPRESSED_DENSITY_…_2026-09-24.md:4.
- Axioms / supplied / proved:
  - Axioms: "source/action and physical-observable identification" is outside the axioms (AX:187).
  - Supplied: the kept ledger; energy density as source; a coupling γ = 1/(4K) with K free.
  - Proved: conditional identities (matched pulls iff S ∝ E, b55); the July source-and-response seam (archive, "the gravity lane does not rise").
- Tried already: July cycles 281-334 (common source/response code), the APS/Wald/Gauss signed-gravity bridge (`open_gate`), August D4 pincer, blocks 55, 120, 121.
- Same wall elsewhere: L02 (source/action and the action functional), L03 (Born readout), L06 (photon source-action).
- Why it matters: without it gravity cannot couple to matter quantitatively, and the parked statistical-bridge decision stays parked.
- Cheapest known test or next step: identify the branchwise Record source (pincer note's stated shortest bridge); the owner's "action ID before Bridge" rule governs any adoption.
- Severity: major
- Status: open

### L14-W11: The magnitude of Newton's constant in lattice units, and a = l_P, is not derived (three unreconciled candidates)
- Plain: The framework fixes only a ruler: the lattice spacing is set equal to the Planck length by definition of its one reference. Whether its own internal gravity has exactly that strength is called "a separate open gravity derivation". Three routes give three answers: Newton's constant of order the spacing squared over the number of species, exactly 1 under a supplied boundary-count premise, and a free stiffness. None is derived.
- Precise: Target: derive G_lat = G/a² (equivalently the member's stiffness K, or the induced coefficient), so that "a/l_P = 1" is a theorem, given the `scale_reference_primitive` (a⁻¹ = M_Pl, a units conversion with zero dimensionless content). (a) Sakharov: 1/(16πG) ~ Λ² N_f, so G ~ a²/N_f with Λ ~ 1/a (cutoff-scheme dependent). The note prints G ~ 48π³/(N_f Λ²), which is (4π)² = 157.9 times the 3π/(N_f Λ²) that its own matching line gives (checked). (b) Planck lane: a/l_P = 1 follows from c_cell = 1/4 and the premise (BP) that the primitive boundary count is the gravitational area/action carrier; (BP) is not derived, a 2026-04-30 obstruction says the event-cell P_A module is not the restriction of an irreducible Cl₄(C) carrier, and the lane predates the 2026-06-29 axiom reset. (c) Member programme: γ = 1/(4K), with K and α/K supplied (b129); a computed K relates the spacing to G only once the matter content is fixed.
- Evidence: AX:189-190; docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md:39-41; docs/PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md:143-158, :160-198 (Target 1), :372-403; docs/PLANCK_SCALE_CONDITIONAL_COMPLETION_NOTE_2026-04-24.md:8, :17-30; docs/PLANCK_PRIMITIVE_CLIFFORD_MAJORANA_EDGE_DERIVATION_THEOREM_NOTE_2026-04-30.md; docs/UNIVERSAL_GR_SAKHAROV_…_2026-06-17.md:10-11, :26-31; scripts/frontier_universal_gr_sakharov_gnewton_induced_scale_2026_06_17.py:19-21; `L14_scratch/arithmetic_checks.py`; MAP:572-574; ADM-b129:4.
- Axioms / supplied / proved:
  - Axioms: the natural unit equals the Planck length is an open gate (AX:189-190); the scale reference "does not assert a/l_P = 1 as a derived theorem" (SCALE_REFERENCE_PRIMITIVE_NOTE.md:39).
  - Supplied: the boundary-count carrier (BP), the cutoff Λ, the species count N_f, K.
  - Proved: only conditional implications (BP ⇒ a/l_P = 1) and an order-of-magnitude induced estimate; the printed coefficient is inconsistent with the note's own matching line (checked; the "~" leaves the order of magnitude intact, but l_P/a comes out 1.09 or 13.6 for N_f = 8 depending on which number is used).
- Tried already: the Planck lane's three targets (unit-map uniqueness, horizon entropy carrier, one-axiom information bridge) with no-go results: PLANCK_FINITE_RESPONSE_NO_GO, PLANCK_PARENT_SOURCE_HIDDEN_CHARACTER_NO_GO, PLANCK_TARGET3_PHASE_UNIT_EDGE_STATISTICS_BOUNDARY (a Hilbert-only surface cannot fix an absolute action unit).
- Same wall elsewhere: L16 (a/l_P, dimensionless constants), L15 (the ¼ coefficient), L07 (hierarchy).
- Why it matters: the TOE cannot say how strong gravity is, nor test its own "natural unit = Planck length" assumption.
- Cheapest known test or next step: compute one lattice-regulated induced Einstein–Hilbert coefficient for a fixed matter content in one stated scheme (a Brillouin-zone sum, no cutoff ambiguity) and compare with a = l_P; the June TT stiffness numbers (C ≈ 0.09-0.10 per staggered block, docs/UNIVERSAL_GR_GRAVITON_DISPERSION_LORENTZ_ISOTROPY_…_2026-06-08.md:43-47) are a start but their normalisation to G is not stated.
- Severity: major
- Status: open

### L14-W12: That gravity attracts (the sign of the coupling) is not derived
- Plain: Nothing in the repository derives that gravity attracts. Three natural arguments, from spectra, from stability and from the arrow of time, do not force it, and stability actually favours repulsion. Each lane reduces the sign to one supplied choice: an orientation datum, whether records slow the clocks around them, or the sign of the size-of-space kinetic term.
- Precise: June lane, on the Poisson surface attraction ⟺ G > 0. The spectral route is blind to sign; the energy-stability route favours repulsion (attraction is unbounded below); the arrow/entropy route is sign-agnostic. The sign reduces to the healthy spin-2 / conformal-trace orientation and hence to a shared orientation datum that Record's K/CPT cannot select; fixing G > 0 equals fixing the conformal-class admission. Member programme: b53 leaves κ (whether records slow the clocks, κ < 1) with its sign unfixed; with kept books records attract (b97, conditional); in the declared sea comparator c + 12κ < 0 gives a repulsive local sign (b76 T4, with declared inputs c = −1.193, κ = 0.095, which are not derived).
- Evidence: docs/GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_…_2026-06-08.md:23-42; docs/GRAVITY_SIGN_IS_NOT_A_NEW_ADMISSION_…_2026-06-18.md:7-30; docs/GRAVITY_SIGN_IS_ONE_RESIDUAL_AT_THE_TT_KERNEL_BLOCK_…_2026-06-08.md; docs/GRAVITY_ATTRACTION_SIGN_FROM_SOURCE_POSITIVITY_…_2026-06-08.md:25-26; docs/UNIVERSAL_GR_SAKHAROV_…_2026-06-17.md:45-50; ADM-b53:28, :82; ADM-b97:4; ADM-b76:4 (T4); docs/SIGNED_GRAVITY_RESPONSE_LANE_STATUS_NOTE_2026-04-26.md:13.
- Axioms / supplied / proved:
  - Axioms: silent on force signs.
  - Supplied: the healthy orientation of the spin-2 kinetic term; κ < 1; the ledger.
  - Proved (landed, unaudited): the three no-forcing results and the reduction of the sign to one residual; b97 conditional.
- Tried already: the three June routes (spectral, stability, arrow); the signed-gravity χ_g selector lane (39 notes; the selector is not derived, the lane is open); K/CPT selection (a no-go).
- Same wall elsewhere: L14-W2 (the conformal sign); L08 (the note says the sign is the same orientation object as the Koide Z₂), L05 (handedness).
- Why it matters: the TOE cannot state that gravity attracts; it has to be supplied.
- Cheapest known test or next step: a derivation of the conformal-sector sign (L14-W2) fixes G > 0 in the June lane; in the member programme, derive the sign of κ from a formation rule (b53 T4) and compute c + 12κ for the interacting sea.
- Severity: major
- Status: open

### L14-W13: Lattice matter has no exact local stress-energy books (momentum, angular momentum) once it interacts or excludes
- Plain: A graviton can couple consistently, and stay massless, only to matter whose energy and momentum are conserved exactly at each place. Lattice matter conserves energy locally but generally not momentum. Under the one-record-per-site rule or with scattering, the bookkeeping fails at third order or entirely, and angular momentum cannot be kept with momentum on six axes unless records never scatter.
- Precise: Gauss laws that protect a massless graviton, and the shift constraint, need exactly conserved local sources. Interacting Hamiltonian lattice matter: energy is local, momentum is not (P6 T9: a search of local charges of range ≤ 3 finds a conserved parity-odd charge only for free or integrable chains). Landed: no local momentum falls with weight one (b106); the walker's frame response is not divergence-free at second order in k (b62); the books hold for free walkers with the two-step content but only at leading order under one record per site (b137), no neighbour coin term restores them (b141), exact books need records that never scatter or bind (b143), no finite-range interaction keeps two excluded records' energy current on Z² or Z³ (b151), and a collision changes the two-step momentum at third order in the offsets (b152). The supplied moving-records clause of 2026-09-20 does conserve momentum exactly and locally with interactions, but not angular momentum (a pass-through exchange changes it by −s × s′, mean 0.2 per event over 20,000 events), so its stress cannot be made symmetric and the shape sector stays unprotected (MAP:927-940).
- Evidence: P6:4 (T9); MAP:538-542, :902-940; ADM-b106:4; ADM-b62:4; ADM-b137:4; ADM-b141:4; ADM-b143:4; ADM-b151:4; ADM-b152:4.
- Axioms / supplied / proved:
  - Axioms: one record per site, permanent (AX:78-80); no conserved energy or momentum is stated.
  - Supplied: the walker, its two-step content, the hard-core (exclusion) reading.
  - Proved (landed, unaudited): b106, b137, b143, b151, b152 as scoped in their claim scopes (e.g. b151 excludes infinite-range and non-additive forms).
- Tried already: b106, b137, b141, b143, b151, b152; programme T (spatial relabellings forced at first order; held blocks 158-164); coarse-grained "long-wave books" was the panel's proposed route (memory `panel-20260927-coupling-axis.md`).
- Same wall elsewhere: L02 (dynamics, conserved currents), L05 (fermion content, exclusion), L14-W14, L14-W15.
- Why it matters: without exact local books the graviton's mass is unprotected, the shift constraint fails, and static decoupling of the partner modes (EX/SUMMARY.md:67-73) is unproved.
- Cheapest known test or next step: the owner's reading choices named by the 09-27 panel (the price of a record, a moving record's energy, the zero of energy, the coupling's reach); test whether long-wave (coarse-grained) books suffice for the graviton's protection.
- Severity: major
- Status: open

### L14-W14: Universality of free fall (the equivalence principle) holds only under a list of conditions
- Plain: Gravity must pull every kind of matter the same way. In the lattice lane that holds only under conditions: the curvature member, first order in the field, a particular momentum definition, and for bound groups an extra "binding clause". Some species fall with minus their weight, and records in a clock gradient settle with a weight but do not drift alike.
- Precise: Target: passive gravitational mass equals inertial energy for every species, bound state and interacting record. (i) The continuum soft-graviton universality argument (Hertzberg–Sandora) is imported with the missing native lemma named: a controlled interacting qubit-lattice phase with the required spin-2 polarisations, source identity and scattering residues, including self-coupling. (ii) Lattice: a reflected species has minus its weight under reach two and all eight agree under reach three (b69/72); records in a clock gradient settle with weight (2a − 1)g each but do not drift alike, and groups need a binding clause (b111: "no universal fall, binding mechanism… is established"); binding energy falls with its weight only in the curvature member, and pull-bound pairs have weight one at first order (b144, b145); no local momentum falls with weight one (b106); inertia and the rule's weights do not mix locally (b100). (iii) Rest mass is supplied: in M₂(C) no matrix anticommutes with all three σ, so a single 3D walker is massless.
- Evidence: docs/SOFT_SPIN2_COLLISION_INVARIANTS_…_2026-09-14.md:35-56; ADM-b69/72:4; ADM-b111:4; ADM-b145:4; ADM-b106:4; ADM-b100:4; docs/ADMISSIBILITY_RULE_THE_MEMBERS_PULL_CARRIES_THE_VELOCITY_TERMS_…_2026-09-25.md:4.
- Axioms / supplied / proved:
  - Axioms: M₂(C) per site (AX:47); no mass, no coupling, no equivalence statement.
  - Supplied: the member, the walk with a staggered mass, the reach-three momentum, a binding clause.
  - Proved (landed, conditional, unaudited): the individual identities above; no universal statement.
- Tried already: blocks 66-72, 100, 106, 111, 144, 145; soft-spin-2 (09-14).
- Same wall elsewhere: L14-W13 (books), L05 (mass, M₄(C) enlargement is a parked owner decision: DEFERRED_DECISIONS.md:121-147), L07 (mass).
- Why it matters: if lattice matter does not fall alike, the gravity being derived is not gravity as observed.
- Cheapest known test or next step: state the equivalence principle as one pre-registered test on the comparator with all clauses (species, bound pair, interacting pair), and record which clause fails first.
- Severity: major
- Status: open

### L14-W15: A fixed regular lattice gives the graviton mass-type terms and destabilising shear energy unless several numbers are tuned
- Plain: A regular grid has a shape. Couple the walker's vacuum to a constant metric in the natural way and its energy changes when the metric shears the grid, which costs nothing in real gravity. That acts like a graviton mass of the vacuum's size unless several numbers are tuned, and for interacting matter the cancellation returns at the next order. I reproduced the basic numbers.
- Precise: Probe 6: sea energy E₀ = −1.19380 per cell; shape coefficients c_E = −0.17793 (axis shears) and c_T = −0.14667 (face shears, natural coupling) or −0.10882 (taste-universal coupling) per cell; flat is a maximum along shears; every fermion sea has c ≤ 0. For free matter a designed coupling removes it exactly; a nearest-neighbour interaction brings it back at first order (0.0019 V axis, 0.0037 V face) and, after cancelling that, at second order (+0.0025 V² per unit shear); no relabelling that keeps momentum addition is a small shear. Consequence: mass-type terms of the vacuum's size unless at least two numbers are tuned beyond the cosmological constant. Held blocks 155 and 167 (block 155 is open PR #9289; the 09-27 panel marks blocks 147, 155 and 167 conditional on block 62's frame until re-derived): the sea's energy falls under every uniform shear at fixed volume, and member plus sea lowers its static energy under every long TT shear at every K. Panel reading: the metric form of Lorentz-violation fine-tuning; the known consistent analogue is Lorentz-violating massive gravity. Only the Gu–Wen/Pretko gauge route protects the mass, at the price of universality.
- Evidence: P6:4; MAP:180-208, :524-560, :755-790, :902-926; PR #9289; memory `campaign-20260926-12h.md` (block 167).
- Axioms / supplied / proved:
  - Axioms: fixed regular Z³ (AX:37).
  - Supplied: the walker's natural coupling to a constant vielbein; a metric field over the grid.
  - Proved: P6 (sol-confirmed on the PR). Checked (mine): `L14_scratch/check_shape_coefficient.py` gives E₀ = −1.193801, c_E = −0.177931, c_T = −0.146670 for the natural coupling, matching P6:4. Naturalness judgement: reading.
- Tried already: P6 T1-T10 (designed coupling, boson-fermion matching, interacting second order); the second panel's lenses (MAP:755-790).
- Same wall elsewhere: L04 (Lorentz violation from a fixed lattice), L13 (vacuum energy), L14-W13, L14-W18.
- Why it matters: a massive or unstable graviton is not gravity. At an illustrative a = 10⁻¹⁹ m the terms are about 10²⁰ times the gravity-wave dispersion bound (MAP:193-195).
- Cheapest known test or next step: boson-fermion matching of zero-point shape energies at the lattice scale, exact lattice Ward identities, or geometry without a preferred shape (MAP:205-208); the E-irrep helicity ±1 block of the induced action (L14-W8).
- Severity: major
- Status: open

### L14-W16: The graviton's speed must equal the matter light speed, and only an added premise protects it
- Plain: Light and gravity waves must travel at the same speed to about one part in 10¹⁵. In the lattice comparator the speeds of two coupled fields drift apart at second order, by an amount that does not shrink as the grid gets finer. An added rule (a tick counts like a space step) protects them; it is approved for matter but not for the gravity field.
- Precise: P3: for the walker plus a scalar with a Lorentz-invariant Yukawa coupling in continuous time, v_ψ − v_φ = +0.0263 g², regulator-dependent (moves 12 % under retuned next-neighbour hopping; one counterterm per pair of species). Hypercubic ticks (`kinetic_isotropy_primitive`, approved for matter) force one cone for scalar and gauge-vector kinetic terms at leading order. For the member it is an added premise: with it the member's leading action is unique, β = −α and α = K/4 follow (P4); without it α = K/4 is a free condition (b134-b136 find the member's speed equals the walker's exactly iff α = K/4). The tick protects only leading order: a clocked walk keeps its frequency ratio only to relative ε² sin²k/3 (b105).
- Evidence: P3:4; P4:4; MAP:169-178, :232-236, :253, :507-522; docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md; ADM-b135:4; ADM-b105:4.
- Axioms / supplied / proved:
  - Axioms: none on speeds; `kinetic_isotropy_primitive` (c_t = c_s) is approved for matter, not for the member.
  - Supplied: the Yukawa comparator; the member on the tick surface.
  - Proved: P3, P4 (P4 conditional); b135 (own, unrefereed).
- Tried already: P3 (regulator dependence, check G); P4; blocks 134-136.
- Same wall elsewhere: L04 (one light cone).
- Why it matters: the observed equality of light and gravity-wave speeds is a hard constraint; the lattice gives only a conditional protection.
- Cheapest known test or next step: the owner's decision 2 (MAP:507-522): move the gravity campaign to the hypercubic tick surface for the member, an added premise.
- Severity: major
- Status: priced (equivalent to extending the kinetic-isotropy premise to the member)

### L14-W17: No positive physical reconstruction of a lattice gravity action has been found; the reflection-positivity route has only negative finite results and its bridge is parked
- Plain: The older "gravity mainline" tried to make a lattice gravity action pass a positivity test, so that it defines a real quantum theory with only positive-norm states. In every finite case tried it failed: the reflected-curvature action has wrong-sign spin-2 modes and an extra indefinite channel. The route was called closed, but the landed notes were corrected to claim only their finite fixtures. What remains is a parked owner decision.
- Precise: Reflected-curvature action Q_μ at μ = 1/1024: two real complete-edge poles with opposite residue signs at k = 1.25, complex pairs at k = 1.27-1.30; three spatial configuration channels with no Hamiltonian-constraint row, the extra one indefinite; in a momentum-orthogonal line-metric reduction 276 of 728 nonzero L = 9 modes have a negative static TT eigenvalue and 174 a negative kinetic estimate. Neither line-metric identification gives a positive complete reconstruction of Q_μ. Dirac–Kähler OS route (August blocks 167-170): corrected to finite-fixture statements — null-model corner identities, a 12x4 Schur identity with an 8x6 control, link and imposed-shift probes — the shim note says it is "not an all-cone theorem or a physical closure claim" and block 169's says "a bounded probe, not a completed or formal audit". The memory record calls this a three-theorem closure (corner, zero-diagonal, shim; #7104, #7106) audited twice, plus a closed-carrier Gauss obstruction (August block 121, memory only: positive matter forbids closed-carrier sourcing). The statistical bridge (slice-Gram weights = record frequencies) was "sealed non-supplied" at every theorem door (August blocks 172-173) and is parked with the owner (DEFERRED_DECISIONS entry 1).
- Evidence: docs/ADMISSIBILITY_REFLECTED_CURVATURE_GRAVITY_PHYSICAL_RECONSTRUCTION_CUT_GATE_…_2026-08-14.md:4, :43-70 (2026-09-08 correction); docs/ADMISSIBILITY_DIRAC_KAHLER_NULL_MODEL_CORNER_THEOREM_…_2026-08-21.md:1-12; docs/ADMISSIBILITY_DIRAC_KAHLER_SHIM_ZERO_DIAGONAL_…_2026-08-21.md:1-12 (line 9: "not an all-cone theorem or a physical closure claim"); docs/ADMISSIBILITY_DIRAC_KAHLER_CLOSURE_AUDIT_ONE_…_2026-08-21.md:1-12; docs/ADMISSIBILITY_DIRAC_KAHLER_CLOSURE_AUDIT_TWO_…_2026-08-21.md:1-10; docs/ADMISSIBILITY_DIRAC_KAHLER_EMBEDDING_RESIDUES_CAMPAIGN_CLOSE_…_2026-08-23.md:4; docs/repo/DEFERRED_DECISIONS.md:21-49; memory `gravity-source-lane-campaign.md` (August blocks 121, 167-173).
- Axioms / supplied / proved:
  - Axioms: no positivity structure beyond Record; Born weights and the statistical bridge are open gates (AX:181-184).
  - Supplied: the reflected-curvature action, the Dirac–Kähler carrier, the OS Gram construction, the reflection.
  - Proved (landed, finite-fixture, unaudited): the numbers above. The "route closed" wording is a memory-level summary; the landed notes do not prove it.
- Tried already: August blocks 103-173 (seam, dressing, transfer, positivity windows, census); the 2026-09-08 and 09-11 corrections narrowed them.
- Same wall elsewhere: L02 (statistical bridge, action), L03 (Born readout), L14-W10.
- Why it matters: the best-developed non-perturbative route to a gravity action with a physical Hilbert space has no positive result.
- Cheapest known test or next step: none proposed; the route is parked by the owner with wake conditions (DEFERRED_DECISIONS.md:21-49). Any restart begins from the finite-fixture scopes, not from "closed".
- Severity: major
- Status: open (the "closed" label overstates what the landed notes prove)

### L14-W18: What gravitates: the member's zero mode tests the zero of energy (vacuum energy)
- Plain: It is not settled whether gravity sees the vacuum. The walker's filled sea carries about one hop of negative energy per site. If the gravity field sees it, a closed lattice bounces or cannot move at all; if not, the framework has to supply the zero of energy by hand. This is the cosmological-constant problem in the lattice's own terms.
- Precise: b147: the member's zero mode tests the zero of energy; the half-filled sea has −I/ℓ per site (massless case), never constant per volume; if the member sees it, a closed lattice bounces at ℓ = I/m₀ or cannot move (needs m₀ > μ). The sea violates the null energy condition (ρ < 0, p < 0), so not seeing it needs a supplied zero of energy. June: the induced vacuum stress is O(1) in lattice units, proportional to the metric, with no cancellation inside the computed term. b139: a constant energy offset breaks the walker's books for every placement.
- Evidence: ADM-b147:4; docs/UNIVERSAL_GR_INDUCED_COSMOLOGICAL_CONSTANT_…_2026-06-08.md:12-40; MAP:258; memory `panel-20260927-coupling-axis.md`; docs/ADMISSIBILITY_RULE_THE_BOOKS_ADMIT_ONE_REST_ENERGY_…_2026-09-25.md:4.
- Axioms / supplied / proved:
  - Axioms: silent on energy or its zero.
  - Supplied: the zero of energy; the filling rule; whether the member couples to the sea.
  - Proved (landed, conditional): b147's scalar-action conclusion and the finite-lattice numbers.
- Tried already: b139, b147, the 09-27 panel (NEC reading), the June induced-Λ tadpole; mechanisms (unimodular, sequestering, counterterm) are not modelled (UNIVERSAL_GR_INDUCED_COSMOLOGICAL_CONSTANT…, Summary).
- Same wall elsewhere: L13 (cosmological constant), L14-W15.
- Why it matters: gravity cannot be quantitatively right if the vacuum's weight is ambiguous by O(1) in lattice units.
- Cheapest known test or next step: the owner's reading question, whether the member sees the sea's response at all (energy and inertia), named in the 09-25 panel.
- Severity: major
- Status: open

### L14-W19: Clause C1 (every site's clock ticks at a positive rate) conflicts with the owner's stopped-clock (frozen-box) reading
- Plain: The source-link lane assumes every site's clock ticks at a positive rate, which rules out a stopped clock. The owner's reading, that a box which can form no more records is frozen and that time is the making of records, needs a rate that can reach zero, as at a horizon. As they stand, the two readings do not fit together.
- Precise: C1 is a supplied clause (b53); the axioms do not force it. b60 T4 proves 0 < w ≤ 1 for its finite held-wall solution with positive rest masses, so nothing admitted by C1 stops a clock. A frozen box as stopped clock needs a rule in which the rate can vanish, for example rate = local event rate. P19: sealed boxes freeze into one state (upward-closed rules) or e^{cV} states (crowding rules), volume not area.
- Evidence: MAP:284-306; P19:4; ADM-b60:4; ADM-b53:4.
- Axioms / supplied / proved:
  - Axioms: silent on tick rates or horizons.
  - Supplied: C1; the frozen-box reading.
  - Proved: b60 T4 (bound 0 < w ≤ 1); P19 counts (bounded).
- Tried already: b60 T4; P19 (frozen counts).
- Same wall elsewhere: L01 (records count rises until frozen), L15 (black holes).
- Why it matters: without a rate that can vanish the lane has no horizons, hence no black hole in the clock picture.
- Cheapest known test or next step: write a rate law with rate = local event rate and rerun b60's T4.
- Severity: minor
- Status: possibly misframed (a conflict between two supplied readings, not a proved obstruction)

## Walls considered and rejected

- Weak-field Newton law (1/r potential, inverse-square force) from the lattice Laplacian: a conditional chain is landed (docs/GRAVITY_CLEAN_DERIVATION_NOTE.md:43-70; docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_…_2026-06-11.md). The remaining gap is the source/action bridge (L14-W10), not the law.
- Recomputing the static tests (light bending, perihelion): already landed in the member programme (b59, b60, b144, b145); the 0.834 × GR figure was a coordinate artefact (EX/agents/kill3_entanglement_statics.md, F7). The dependence on the declared member is L14-W9.
- Signed gravity / antigravity lane (SIGNED_GRAVITY_*, 39 notes): an optional extension (a physical repulsive sector is not derived: docs/SIGNED_GRAVITY_RESPONSE_LANE_STATUS_NOTE_2026-04-26.md:13); the TOE does not need it. Its orientation datum is the same object as L14-W12.
- Leading lattice correction to Newton's law, [5/(32π)] K₄(n̂)/r³ (docs/GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07.md): a positive theorem and a prediction, unobservable at a Planck-scale lattice. Not a wall.
- Black-hole entropy coefficient ¼ versus Widom ⅙: L15's wall (only the graviton-free route L14-W5 is here).
- g_bare = 1 and the N_F = ½ normalisation (G_BARE_*): a gauge-coupling convention, L06/L16.
- Closed-lattice expansion or bounce (b146, b148): cosmology, L13 (the zero-of-energy part is L14-W18).
- Gate B and SOURCE_RESOLVED_* wave-field families (April-June numerical lanes on generated graphs): superseded numerical experiments; they inherit L14-W10.
- Tensor composition needing local tomography (2026-06-03 no-go): L03, not gravity.
- Z⁴ event-lattice formulation of the gravity counting: untried, not a wall (EX/ASSUMPTIONS.md:34, S10).
- Regge second-variation and positive tensor transfer on finite odd tori: a positive finite result (docs/REGGE_EXACT_REDUCTION_POSITIVE_TENSOR_TRANSFER_…_2026-09-13.md), scoped to a supplied Regge action; its limits are L14-W7.
- Coverage note (not a wall). Read in full: the exercise packet's SUMMARY, WALL, ASSUMPTIONS, ROUTES, TESTS, APPROACH_REGISTRY, OUTSIDE_VIEW and eight agent texts; the viability map; the axioms and registry check. Claim scopes and open sections only: about 60 gravity-family notes on main and 20 probe notes on the PR branch. Not read beyond status lines: most of the 54 UNIVERSAL_GR_ notes, the SIGNED_GRAVITY_ notes, blocks 134-149 beyond their claim scopes, and the Regge lane beyond its scopes. Checks I ran are in `L14_scratch/`: T1 rerun (identical), probe 6 numbers (reproduced), the (110)/(100) area-law ratio (1.1747, reproduced), the double-pulsar floor arithmetic (12.4 and 19.7), and the Sakharov coefficient (printed value off by (4π)²).
