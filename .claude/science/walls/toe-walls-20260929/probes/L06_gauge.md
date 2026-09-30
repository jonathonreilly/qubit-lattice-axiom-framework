# Lane L06: Gauge forces: photon, weak and strong — walls

## Lane map (under 200 words, plain language first)

This lane asks how electromagnetism, the weak force and the strong force could come out of the four axioms (one qubit per site, one nearest-neighbour rule, permanent records), and what fixes their strengths. Every ledger row has audit status "unaudited" (5,299 rows, checked), so "proved" below means a landed, runner-backed but unaudited note.

Best results, all conditional:
1. Local frame redundancy forces a link connection (kinematics only).
2. The 8-state taste cube carries a Clifford algebra, an su(2) and, after a supplied axis choice, an su(3).
3. A large U(1) programme: qubits on links, an ice rule, square-flip moves. It gives a gapless field pattern and, in the harmonic regime, a two-polarisation photon. Light-speed dispersion of the full quantum model is undecided (open PRs #9372 to #9392).
4. SU(3) Wilson at beta = 6 with plaquette 0.5934 admitted gives alpha_s(v) = 0.1033 and alpha_s(M_Z) = 0.1182, through four declared inputs.

Where it stands: no gauge group, colour carrier, coupling value or confinement scale is derived. Each is a named premise or open. Non-Abelian gauge structure has no formation-rule or record-readout account.

## Walls

### L06-W1: The gauge group is not selected from the carrier
- Plain: The axioms give each site one qubit, so the only symmetry they hand over is that qubit's su(2). The repo builds a six-state block (3 colours x 2 weak states) to reach SU(3)xSU(2)xU(1). On that block the algebra fits the far larger U(6) equally well. Choosing the product subgroup as "the forces" needs a rule the axioms do not contain.
- Precise: Target: show that the dynamically gauged algebra on the supplied carrier C^3(base) x C^2(fibre) is su(3)+su(2)+u(1) (dim 12), not u(6) (dim 36) or a non-factor-local conjugate.
  - Fails (proved, conditional): four discriminators (maximality, anomaly d-tensor, chirality grading, real-vs-complex) are blind or one-sided. No selector built only from conjugation-invariant data (irreducibility, scalar commutant) separates the factorwise embedding from its unitary conjugate or from u(6).
  - The factor-local normalizer theorem returns the factorwise algebra only after a factor-preservation rule (REGISTERED-FACTOR) is supplied.
  - The upstream taste-cube route needs a weak-axis selector that picks one of three cubic axes as a minimum of a supplied potential (reading: this is an S3 to Z2 breaking of the cubic covariance the Lattice axiom asks for).
  - Quantifiers: closed for all conjugation-invariant selectors (no-go); open for typed or dynamical selectors.
- Evidence: docs/GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md:62-64,80-96,114-155; docs/GAUGE_GAUGING_SELECTION_CONJUGATION_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md:77; docs/GAUGE_FACTOR_LOCAL_SELECTOR_NORMALIZER_THEOREM_NOTE_2026-06-18.md; docs/GAUGE_FACTOR_PRESERVATION_RECORD_TYPED_SELECTOR_CONDITIONAL_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-07-06.md:24,46,60; docs/GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md:10-45; docs/NATIVE_GAUGE_CLOSURE_NOTE.md (N1-N4); docs/MINIMAL_AXIOMS_2026-06-29.md:116-123,173-189.
- Axioms / supplied / proved:
  - Axioms: Z^3 with cubic covariance; an M_2(C) qubit per site; one nearest-neighbour rule. No gauge group, carrier factorization or gauging principle.
  - Supplied: the C^3 x C^2 carrier; the factor-preservation rule; the weak-axis selector; the gauging principle (which symmetry is dynamical).
  - Proved (unaudited): exact algebra of su(3)+su(2)+u(1) inside u(6); the normalizer theorem under a factor rule; native Cl(3) and su(2) on the taste cube; the four-discriminator and conjugation-independence negatives.
- Tried already: four discriminators (GAUGE_ALGEBRA...:80-96) all fail; conjugation-invariant selector route pruned (NO_GO note); normalizer theorem is positive but needs the rule; record-typed selector reduces to the named premise REGISTERED-FACTOR (2026-07-06 note:24); the note itself points to "a future local-dynamics theorem" as the only live route (note:60).
- Same wall elsewhere: L05 (the taste cube is a staggered-fermion object; the staggered-Dirac realization is an open gate in the axiom memo, line 178); L07 (chiral su(2)_L); L01 (REGISTERED-FACTOR has the same shape as the readout bridge MARGINAL-READ).
- Why it matters: without it the TOE cannot say why the forces are these three and not U(6).
- Cheapest known test or next step: suggested. Compute the full symmetry algebra of the actual nearest-neighbour hopping on the 8-state taste cube (the Gamma_i shifts plus the selected-axis swap) and check whether the factorwise algebra is forced with no supplied factor rule. This is a finite exact runner and would either derive REGISTERED-FACTOR from the hopping or exhibit a counterexample.
- Severity: blocking
- Status: priced (equivalent to three named premises: the colour carrier, REGISTERED-FACTOR, a gauging principle)

### L06-W2: The colour carrier (MR_color) is not derived
- Plain: A bond of two qubits naturally holds a 3-dimensional block plus a 1-dimensional block, and su(3) acts on the 3-block. Nothing yet says quarks live in that block, that readable records are colour-neutral, or that the colour index rides on the links. Three separate bridges are missing, and the July campaign split them into eight named premises.
- Precise: MR_color := (quark matter occupies the 3-dim symmetric-base fundamental) AND (physical records are colour singlets) AND (link variables carry the base-SU(3) index).
  - Five routes pruned: post-record append/count dynamics, endpoint-invariance profile, the one-qubit link algebra, dim Z^3 = 3 alone, and a stable dial location.
  - 2026-07-06 re-bounding: eight open premises (SUPPLIED-C3, MARGINAL-READ, WEIGHT-UNIFORMITY, FERMI-FILL, REGISTERED-FACTOR, SUPPLIED-BILINEAR, ARROW, SUCCESSION-ORIENT). Residual gaps: singlet-versus-indistinguishable, chiral, hypercharge.
  - A single C^3 x C^2 carrier has no second central u(1).
  - Bonded-pair arena: M_4(C) = Sym^2(C^2) + Anti. If the internal generators are identified with spin axes, the symmetric block is a spin-1 representation and the spatial-singlet obstruction returns. The axioms alone are compatible with a spatially trivial internal block.
- Evidence: docs/COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md:76-84,91-105,166-173; archive/notes/docs/COLOR_DERIVATION_CAMPAIGN_20260706_ASSEMBLY_AND_HONEST_REBOUNDING_META_NOTE_2026-07-06.md:51-92,100-131,144-158; docs/COLOR_ARENA_BONDED_PAIR_ADMISSIBILITY_CROSS_SITE_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-06.md (Summary); docs/COLOR_SU3_SYMMETRIC_BASE_BRIDGE_FROM_RECORD_INVARIANCE_BOUNDED_NOTE_2026-06-05.md:47-60; docs/COLOR_SINGLET_RECORDS_G2_FACTORIZATION_SITE_LOCAL_LOCKING_BOUNDED_THEOREM_NOTE_2026-07-06.md.
- Axioms / supplied / proved:
  - Axioms: one M_2(C) possibility domain per site, a nearest-neighbour rule, content-determined readout. No colour, no carrier, no quark assignment.
  - Supplied: the 3-dim carrier and its assignment to quarks; the marginal-readout bridge; the cross-site bilinear that routes the index onto links.
  - Proved (unaudited): the algebraic su(3) on Sym^2(C^2); the commutant statement "if records are singlets, the base SU(3) is the symmetry"; the exact polar-factor transport law; 3 is not equivalent to 3-bar.
- Tried already: the June-5 pruning map (:91-105); the July-6 blocks 01-06, verdict "NOT achieved" (meta note:159-165); the block-spin route shows colour is re-derived per scale, not transported (W3). The owner rule is Tier-A count 0, so colour must be derived or bounded (meta note:20-23).
- Same wall elsewhere: L05 (matter carrier, FERMI-FILL, the staggered-Dirac gate); L01 (MARGINAL-READ, the readout bridge, ARROW).
- Why it matters: without it there is no strong force, only an algebra that happens to contain su(3).
- Cheapest known test or next step: the campaign's own top pointer: one readout-bridge theorem (or one registered primitive) that supplies MARGINAL-READ and REGISTERED-FACTOR together (meta note:144-148). That needs an owner decision on a primitive, so it is not a worker task.
- Severity: blocking
- Status: priced (eight named premises)

### L06-W3: Non-Abelian gauge links have no account in one-qubit-per-site records
- Plain: A force-carrying link for SU(2) needs at least four states (two qubits), and one for SU(3) at least six (three qubits). When one is built, the readable pattern of which state each site holds cannot even represent a colour-neutral state in the tested model: none of 65,536 patterns satisfies the non-Abelian Gauss law. Readable content sees colour only through singlets.
- Precise: Under the supplied link definition (commuting nontrivial SU(N) actions at both ends) a link needs at least 2N states. A qubit cannot carry it for N >= 2. Independent U(1), SU(2), SU(3) links need 48 states; a joint (3,2)_Y direct sum needs 12.
  - On the declared four-corner SU(2) plaquette (65,536-dim carrier), 0 of the basis patterns lie in the Gauss kernel. The record-readable gauge-invariant algebra has 1,296 atoms generated by charges and Casimirs (colour-blind labels).
  - In the SU(3) one-rishon model, colour is visible only through triality and singlets.
  - No formation rule for multi-site links is given; the direct triangle is not a nearest-neighbour cubic subgraph; block-spin cannot be an algebra morphism (256 does not divide 2).
  - Quantifiers: statements are for the declared finite models, not all encodings.
- Evidence: docs/DYNAMICS_CLAUSE_NON_ABELIAN_GAUGE_LINKS_NEED_SEVERAL_QUBITS_ONE_QUBIT_CARRIES_NO_SU_N_LINK_SU2_NEEDS_TWO_SU3_THREE_BOUNDED_THEOREM_NOTE_2026-09-24.md:4,25-36; docs/A_NON_ABELIAN_GAUSS_LAW_HAS_NO_RECORD_PATTERN_SOLUTIONS_BOUNDED_THEOREM_NOTE_2026-09-03.md:4,46,60; docs/THE_RECORD_READABLE_GAUGE_INVARIANT_ALGEBRA_IS_COLOUR_BLIND_BOUNDED_THEOREM_NOTE_2026-09-03.md:4,46; docs/RECORDS_REGISTER_COLOUR_ONLY_THROUGH_TRIALITY_AND_SINGLETS_THE_SU3_CASE_BOUNDED_THEOREM_NOTE_2026-09-04.md:4,36-38; docs/BLOCK_SPIN_CP_COMPRESSION_COLOR_REEMERGENCE_NARROW_NO_GO_NOTE_2026-06-08.md:27,67.
- Axioms / supplied / proved:
  - Axioms: a record locks one possibility at one site; readout is by content alone.
  - Supplied: the multi-state links, the fermion (Jordan-Wigner) encoding, the occupation basis, the dephasing readout, Born weights.
  - Proved (unaudited): the state-count bounds; the zero-pattern and 1,296-atom results; triality-only visibility; the non-morphism block-spin theorem.
- Tried already: the three September notes above; the block-spin note (the choice of surviving isometry is called an "undelivered selection", line 67).
- Same wall elsewhere: L03 (which observables records can resolve; gauge-invariant effects are only P_3 and P_1, GAUGE_INVARIANT_EFFECT...:46-52); L01 (multi-site objects versus one record per site); L14 (tensor constraints need about 20 qubit slots, PR #9363 probe 10).
- Why it matters: the axioms read only records. If colour cannot be read there, the strong force is invisible to the theory's own readout, and there is no derived way to form a colour link.
- Cheapest known test or next step: reading plus suggested test. Colour-blind readable content is what a confining theory should show, so check whether the 1,296-atom algebra still resolves the ground energy and static-source separation energies of the model (partly available in the compact-cube static-source notes). If yes, the wall becomes "how multi-site links form", not "colour is invisible".
- Severity: major
- Status: open

### L06-W4: The gauge action and its normalization (g_bare = 1, beta = 6) are supplied
- Plain: The axioms say they are not a dynamics axiom, and list "g_bare = 1 convention handling" as an open gate. The repo sets the strong coupling to exactly 1 (beta = 6) by two conditional identifications. One matches the Wilson action's coefficient to a target. The other says a "slot" fixed by rigidity is the coupling. The action's form is also assumed.
- Precise: Target: derive the Wilson plaquette action and g_bare^2 = 1 (beta = 2N_c/g^2 = 6). The current chain gives beta = 6 only conditionally on W-PHYS (Wilson matching) and SLOT-ID (identify the label with the canonical slot). The 2026-05-28 panel names N_F = 1/2 "the single load-bearing admission".
  - Invariance is not uniqueness. Dynamical fixed point, maximum entropy, mean-field and lattice-beta selectors are no-go routes.
  - At operator level the electric/magnetic coefficient stays free: H_g = g^2 H_E + g^-2 H_B, and H_E is unbounded while H_B is bounded, so they cannot be exchanged.
  - A supplied one-tick fluctuation law (-Hess log K_tick = g_can) selects beta = 2N_c. That is a sufficient supplied law, not a derivation.
- Evidence: docs/MINIMAL_AXIOMS_2026-06-29.md:116-123,187-188; docs/G_BARE_DERIVATION_NOTE.md:12-30; docs/G_BARE_PARENT_PROMOTION_GATE_MAP_NOTE_2026-06-06.md:33-60,81-95; docs/GAUGE_INVARIANT_EFFECT_INSTRUMENT_AND_WILSON_GENERATOR_NORMALIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-02.md:26,46-70; docs/WILSON_REAL_POSITIVE_MEASURE_BOUNDED_PREMISE_BRIDGE_NOTE_2026-06-03.md:16-30; docs/G_BARE_DYNAMICAL_FIXATION_OBSTRUCTION_NOTE_2026-04-18.md.
- Axioms / supplied / proved:
  - Axioms: none of action, Hamiltonian or coupling; "g_bare = 1 convention handling" is listed as open.
  - Supplied: the Wilson action; N_F = 1/2 canonical normalization; W-PHYS; SLOT-ID; real-positive Euclidean measure.
  - Proved (unaudited): the Wilson small-a matching coefficient w s^2/(4n); conditional beta = 6; the Hessian identity (beta/2N_c) g_can; the free relative coefficient.
- Tried already: the gate map (:81-95) rules out promotion by algebra plus invariance; the effect/instrument note (:46-70) locates the exact sufficient law; older dynamical-fixation obstruction.
- Same wall elsewhere: L02 (source/action identification, listed open in the axiom memo line 187); L16 (dimensionless constants: g_bare).
- Why it matters: every strong-coupling number (alpha_s, string tension, the plaquette chain) inherits this one input.
- Cheapest known test or next step: the note's own next action: "Derive an independently fixed physical tick and fluctuation law, or keep the Wilson normalization conditional" (GAUGE_INVARIANT_EFFECT...:26). The gate map's alternative: close the staggered-Dirac realization gate (route 1, G_BARE_PARENT_PROMOTION_GATE_MAP...:74-77).
- Severity: blocking
- Status: priced (equivalent to N_F = 1/2 or the pair W-PHYS + SLOT-ID)

### L06-W5: The SU(2) and U(1) couplings come from a counting ansatz that does not fit SU(3)
- Plain: For the strong force the repo sets g = 1. For the weak and hypercharge forces it uses g^2 = 1/4 and 1/5, taken from counting generators of the Clifford algebra. Nothing derives that counting rule, and it is not applied to SU(3). An older route instead used one unified coupling at the Planck scale. The two routes disagree on the weak coupling's starting value by a factor of 4.6.
- Precise: CL3_SM_EMBEDDING asserts g_2^2 = 1/dim Cl+(3) = 1/4 and g_Y^2 = 1/5 by the reading "kinetic term implies g^2 proportional to 1/N_gen". This gives a bare sin^2(theta_W) = 4/9 (reading: not derived).
  - The SU(2) anchor note keeps g_2^2 = 1/4 (alpha_2 = 1/(16 pi) = 0.0199, beta_W = 16) as an assumed input.
  - g_2(v) lies in [0.659, 0.683] against 0.646 (2-6% high), from that anchor plus a single-plaquette u0 interval.
  - The superseded EW note used alpha_GUT = alpha_LM = 0.0907 for every factor; it gives g_1_GUT(v) = 0.590 (27% high) and a Landau pole for SU(2) at about 4e9 GeV. So two incompatible UV values of alpha_2 (0.0199, 0.0907) are on file.
  - The counting rule is not applied to SU(3) (g_3^2 = 1).
- Evidence: docs/CL3_SM_EMBEDDING_THEOREM.md:60-90; docs/SU2_WEAK_ALPHA_LATTICE_ONE_OVER_SIXTEEN_PI_ANCHOR_NARROW_THEOREM_NOTE_2026-05-28.md:8-30; docs/G_2_V_BOUNDED_INTERVAL_NARROW_THEOREM_NOTE_2026-05-17.md:1-40; docs/EW_COUPLING_DERIVATION_NOTE.md:3,20-26,135-175; docs/YT_EW_COUPLING_BRIDGE_NOTE.md:145-160; docs/CKM_EW_LATTICE_A4_BRIDGE_RETAINED_IDENTITY_NOTE_2026-04-25.md:58,71.
- Axioms / supplied / proved:
  - Axioms: no coupling of any factor.
  - Supplied: the counting rule for g_2^2 and g_Y^2; the SU(2) anchor; the SU(5) unification at M_Pl (older route).
  - Proved (unaudited): the dimension counts dim Cl+(3) = 4 and 5, the algebra of the Y eigenvalues, and the substitution arithmetic. The rule turning counts into couplings is not proved.
- Tried already: the anchor note (:27) says outright "It does not derive the coupling input itself"; the EW note (:81-95) lists the SU(2) running surface as open.
- Same wall elsewhere: L07 (Weinberg angle, electroweak couplings); L16 (couplings and unification).
- Why it matters: only the bare SU(3) coupling has a stated derivation route (W4). The weak and hypercharge values enter the electroweak claims by ansatz.
- Cheapest known test or next step: suggested and cheap. Apply the one-tick fluctuation law of W4 to N_c = 2. By the same Hessian identity it selects beta = 2N_c = 4 (g^2 = 1), against the anchor's beta_W = 16. That would show the SU(2) and SU(3) inputs follow different principles.
- Severity: major
- Status: possibly misframed (numerology-shaped inputs)

### L06-W6: The plaquette value <P>(beta = 6) = 0.5934 is admitted, not derived
- Plain: Everything in the strong-coupling chain rests on one number, the average plaquette at beta = 6. Monte Carlo gives it to about 0.06%. The repo has no proof or certified enclosure. The rigorous routes it looked at fail or cost too much.
- Precise: B1 in the alpha_s chain: <P> = 0.5934 is an "admitted comparison/reuse number".
  - Bracket program: <P>* = 1 + f'(6), with |f_L - f| <= 6 beta/L; a certified 0.01-wide three-point ln Z_L bracket needs L of about 3.7e5.
  - The standard Kotecky-Preiss certificate covers only beta <= 3.08e-4 and fails at beta = 6 by about 3.8e5 in activity.
  - Tensor-network route: exact in 2D. In D >= 3 it needs the non-abelian recoupling network (treewidth wall).
  - The 2026-05-29 map found zero closure-ready routes.
  - Numerics exist: finite-size scaling gives 0.59400 +/- 0.00037.
- Evidence: docs/ALPHA_S_DERIVED_NOTE.md:91-113; docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md:29-45; docs/BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md:27-50; docs/BETA6_PLAQUETTE_TENSOR_NETWORK_FINITE_IRREP_SUPPORT_AND_RECOUPLING_WALL_NOTE_2026-06-04.md:25-30; docs/PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md:9; docs/PLAQUETTE_ALPHA_S_CHAIN_AUDIT_MAP_SYNTHESIS_META_NOTE_2026-05-10.md:97-135.
- Axioms / supplied / proved:
  - Axioms: none.
  - Supplied: the value 0.5934 (licensed reuse); the Wilson surface at beta = 6.
  - Proved (unaudited): the existence and finite-volume rate of the thermodynamic limit; the KP failure factor; the 2D exact value; the Monte Carlo estimate as numerics.
- Tried already: the bracket program, KP certificate, tensor-network and bootstrap routes (BETA6_* and PLAQUETTE_BOOTSTRAP_* notes). None closes.
- Same wall elsewhere: none as a wall in another lane. L07 consumes the same number through alpha_LM.
- Why it matters: it is the input behind u_0 and alpha_LM. The physics value is known numerically, so this is mainly a rigor item.
- Cheapest known test or next step: certify the Monte Carlo number under the repo's own protocol (docs/PLAQUETTE_MC_CERTIFICATION_PROTOCOL_NOTE_2026-06-11.md), or run the bounded-bond-dimension TRG/HOTRG contraction that the tensor-network note names as the live compute path.
- Severity: minor (physics); the repo labels it its most-cited open quantitative gate
- Status: priced (equivalent to a certified numerical enclosure)

### L06-W7: The bridge from the Planck lattice to the physical strong coupling is missing
- Plain: The lattice coupling is set at the lattice scale. The repo reads it as the strong coupling at 246 GeV, then runs it to M_Z with standard QCD. Run instead from the lattice scale, an ordinary coupling of this size hits infinity far above 246 GeV. A beta = 6 lattice with spacing at the Planck scale would confine near 10^18 GeV, not 0.2 GeV. The 0.1182 match depends on two declared choices.
- Precise: alpha_s(v) = alpha_bare/u0^2 needs B3 (the tadpole power n_link = 2 chosen from a vacuum-polarization channel count) and B4 (identify it at mu = v, with a scheme conversion). Checked (my scratch script, reproduces the note's 0.118233):
  - One-loop Landau poles from alpha_LM = 0.0907 at M_Pl: SU(3) at 6.1e14 GeV, SU(2) at 3.8e9 GeV (the repo quotes 6e14 and 4e9).
  - Sensitivity: n_link = 1, 2, 3 give alpha_s(M_Z) = 0.1019, 0.1182, 0.1376; <P> = 0.55, 0.62 give 0.1235, 0.1153.
  - Two-loop asymptotic scaling at beta = 6, pure glue: a Lambda_L = 2.3e-3, so Lambda_L is about 2.9e16 GeV for a^-1 = M_Pl. With the repo's imported beta = 6 lattice datum sigma a^2 = 0.0465 (sqrt(sigma) a = 0.216) the string tension is about 2.6e18 GeV.
  - To get Lambda/M_Pl = 0.2 GeV/M_Pl one needs g^2 = 0.151 (beta about 39.7).
  - The approved scale primitive fixes a^-1 = M_Pl. The direct Wilson-loop route imports the Sommer scale r_0 = 0.5 fm, which sets a of about 0.09 fm.
  - The repo says the taste staircase / coupling-map theorem must supply "non-perturbative UV-IR matching". It is asserted, not proved.
  - The running kernel, thresholds and matter content (n_f = 6, 5) are external.
- Evidence: docs/ALPHA_S_DERIVED_NOTE.md:91-155,165-200; docs/ALPHA_S_CMT_COUPLING_MAP_DERIVATION_THEOREM_NOTE_2026-05-17.md:40-55; docs/EW_COUPLING_DERIVATION_NOTE.md:135-175; docs/FIXED_LATTICE_GAUGE_EXISTENCE_STRONG_COUPLING_SCOPE_NOTE_2026-06-09.md:62-72; docs/CONFINEMENT_STRING_TENSION_NOTE.md:27-31,95-125; docs/ALPHA_S_DIRECT_WILSON_LOOP_HONEST_STATUS_AUDIT_NOTE_2026-05-02.md:42; docs/HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_2026-05-30.md:15-40; docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md:17,39; scratchpad walls/L06_scratch/alpha_s_checks.py.
- Axioms / supplied / proved:
  - Axioms: none of the coupling map, scheme, scale or running. The scale primitive supplies a unit only and does not assert a/l_P = 1.
  - Supplied: B3 and B4; the running kernel and thresholds; the taste-staircase matching; Sommer scale in one route.
  - Proved (unaudited): the algebra alpha_s(v) = 1/(4 pi sqrt(P)) = 0.10330382 given B1-B4; the operator count of two link insertions in the vacuum-polarization channel.
- Tried already: B3 wording repair (ALPHA_S_DERIVED_NOTE:114-149); "No derivation of Lambda_QCD << a^-1 or dimensional transmutation from the axioms/primitives" (FIXED_LATTICE...:69); the hierarchy formula replaces exponential transmutation by alpha_LM^16, whose magnitude (4 pi)^-16 is itself an open gate (HIERARCHY_ALPHA_LM_MAGNITUDE...:33-40). The multiscale-flow route to a controlled bridge is W16.
- Same wall elsewhere: L07 (hierarchy formula and alpha_LM^16); L16 (a/l_P, dimensionless constants). L06-W8 is the confinement version of the same mismatch.
- Why it matters: the headline prediction alpha_s(M_Z) = 0.1182 versus 0.1180 observed is not a test of "g_bare = 1 on a Planck lattice" until this bridge is derived. Reading: the direct Wilson-loop route is standard quenched beta = 6 lattice physics with an imported physical scale.
- Cheapest known test or next step: checked and cheap. State which coupling is meant at a^-1 = M_Pl and where the 19 orders are absorbed. A finite check is to run the coupling-map theorem's taste-staircase from beta = 6 at a^-1 = M_Pl to v and compare it with the one-loop Landau poles above. That is a numerical runner on data the repo already has.
- Severity: blocking
- Status: open (the headline chain prices it as B3 + B4; the underlying transmutation gap is open)

### L06-W8: Confinement and the mass gap of the physical SU(3) theory are not derived
- Plain: The repo's confinement statement is "this is standard Yang-Mills at beta = 6", taken from the lattice literature. What is actually proved is narrower: a gap for one reduced operator, gap positivity on a small compact box, and toy one-plaquette checks. There is no proof of an area law or infinite-volume gap for the physical 3+1D environment.
- Precise: Target: SU(3) Wilson theory in 3+1D at beta = 6 has a mass gap and area law in infinite volume.
  - Available (proved, unaudited): a uniform half-line gap for the packet operator T_beta for all beta >= 0 (explicitly "not a theorem about the physical three-dimensional Wilson environment ... confinement, or the Clay mass gap"); an all-coupling gap on a finite compact cube; static-source separation bounds with no convergence of finite charged minima; toy one-plaquette sigma = -log(factor).
  - Four plaquette-environment identification rows are still "missing bridge theorem".
  - The KP convergent-expansion certificate fails at beta = 6.
  - The string-tension note takes confinement and Sommer-scale data as standard input, and says so.
- Evidence: docs/NATIVE_GAUGE_TRANSFER_A2_REFLECTION_UNIFORM_HALF_LINE_GAP_THEOREM_NOTE_2026-09-02.md:44-52; docs/GAUGE_WILSON_COMPACT_CUBE_ALL_COUPLING_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md:6; docs/GAUGE_WILSON_SELECTED_INFINITE_STATIC_SOURCE_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-07.md:6; docs/FIXED_LATTICE_GAUGE_EXISTENCE_STRONG_COUPLING_SCOPE_NOTE_2026-06-09.md:62-72; docs/CONFINEMENT_STRING_TENSION_NOTE.md:27-31,66-72; docs/PLAQUETTE_ALPHA_S_CHAIN_AUDIT_MAP_SYNTHESIS_META_NOTE_2026-05-10.md:97-135; docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md:38-45.
- Axioms / supplied / proved:
  - Axioms: no dynamics, no action, no confinement statement.
  - Supplied: the Wilson surface, beta = 6, and the imported lattice data.
  - Proved (unaudited): the items in Precise.
- Tried already: the W85 Wilson-to-saddle bound was an open gate in June (NATIVE_GAUGE_TRANSFER_W85_FINITE_WITNESS_OPEN_GATE_NOTE_2026-06-12.md) and was closed on 2026-09-02 for the packet operator only. Monte Carlo on 4^4 (30 checks) gives a qualitative area law only (CONFINEMENT_STRING_TENSION_NOTE:130-142).
- Same wall elsewhere: none in another lane. L06-W7 shares the scale mismatch.
- Why it matters: without it the TOE has no derived hadron-level output from the strong force.
- Cheapest known test or next step: suggested. Extend the packet-operator gap to the actual 3D spatial-environment transfer operator (the four missing rows above). A cheaper first step is a framework-run larger-lattice Monte Carlo for the string tension at beta = 6, replacing the imported Sommer numbers with the repo's own run.
- Severity: major
- Status: open

### L06-W9: The photon's light-speed dispersion in the qubit-link model is not established
- Plain: With an ice rule and square-loop flips on link qubits, the evidence says a wave exists that costs almost nothing at long wavelength. Whether its energy grows in step with wavenumber, like light, or with its square, is undecided. The methods in use give only upper limits on that energy, never a lower limit, so a slow mode with small weight cannot be ruled out.
- Precise: Target: for H = -K sum F_p + V sum F_p^2 at V < K, the lowest transverse excitation has omega proportional to |k| (two polarisations) in the thermodynamic limit, in the Coulomb phase.
  - At the RK point (V = K), S_T is flat at 3/2 and the single-mode bound goes as q^2.
  - Beyond RK on a 2x2x3 cluster (34,080 states) the mode stiffens, but linear versus quadratic is undecidable at those momenta. A 2x2x4 check (1.55 million states) suggests an ordering channel at V <= 0.
  - The pure-ring point (V = 0): the historical #7959 report of omega about 0.78 k^2 at L <= 12 is unverified. Energy-only moment bounds give estimated upper limits omega_min <= 2 s sqrt(u/chi).
  - The open PRs give late-window curvature (susceptibility) estimates of about 1.05 to 1.11 on 16^3 and 24^3. In moment-bound form that is an estimated upper limit of about 1.0 s on the lowest transverse frequency (s = 2 sin(k/2)). But there is a slow common drift of about 0.05 per 30 projection-time units of unknown source, and guide, population and projection biases are uncontrolled.
  - Two historical branches remain unjoined: a detuned branch (V = 0.95, 0.90) with positive spectral terms and the pure-ring branch with a quadratic mode; their protocols and limits are not connected (landing note 6.C).
  - The harmonic-regime photon is a separate approximation, not derived from the spin-1/2 model (E = +/-1 makes sum E^2 a constant).
  - Stability of the Coulomb phase away from RK, and monopole or confining sectors, are not attempted.
- Evidence: origin/claude/toe-viability-probes-20260927:docs/A_NEIGHBOURHOOD_CONSTRAINT_ON_Z3_QUBITS_EVIDENCE_OF_A_GAPLESS_FIELD_PATTERN_AND_A_PROTECTED_MASSLESS_PHOTON_IN_THE_HARMONIC_REGIME_BOUNDED_THEOREM_NOTE_2026-09-28.md:4,230-284,352-380; docs/THE_PURE_SPIN_HALF_LINK_MODEL_ON_THE_CUBIC_TORUS_IS_GAPLESS_DECONFINED_AND_UNORDERED_AT_L_12_WITH_A_QUADRATIC_TRANSVERSE_MODE_NOT_A_MAXWELL_PHOTON_BOUNDED_NOTE_2026-09-04.md:4; docs/RING_MODEL_ENERGY_ONLY_BOUNDS_ON_THE_PURE_RING_PHOTON_FROM_THE_MODE_AVERAGED_TRANSVERSE_SUSCEPTIBILITY_BOUNDED_THEOREM_NOTE_2026-09-25.md:4-25; docs/ROUND_FOUR_SYNTHESIS_THE_PURE_RING_PHOTON_FROM_ENERGIES_ALONE_BOUNDED_THEOREM_NOTE_2026-09-25.md:42-48; docs/U1_MAXWELL_LIGHT_LANE_LANDING_CORE_META_NOTE_2026-09-05.md:684-736,910-921; open PRs #9298, #9361, #9365, #9369, #9372, #9391, #9392, #9354; the tensor analogue: PR #9363 probes 10-11.
- Axioms / supplied / proved:
  - Axioms: no Hamiltonian; nothing forces the ice rule or the ring move.
  - Supplied: qubits on link sites, the ice rule, the ring exchange, the detuning V, the guide and projector settings.
  - Proved (unaudited): exact RK correlations; the moment inequalities; the harmonic-regime spectrum; finite-size numerics. None is a lower bound on a photon speed.
- Tried already: probe 9 (RK point, ED to 1.55M states); the September ring-model notes; PR series #9298 to #9392. The 24^3 curvature estimate moved from 0.81 to 1.05 with projection time (#9372) and matches 16^3 window by window (#9392). Each step exposed a new estimator bias.
- Same wall elsewhere: L14 (gravitons from the same exact-constraint class are slow, omega proportional to k^2 or k^3, in the regular compact class; probes 10-11); L04 (one light cone).
- Why it matters: without a linear photon the "force carriers are patterns of records" reading (owner, 2026-09-28) stops at a gapless but non-light-like mode.
- Cheapest known test or next step: the note's terminal obligation: quantum Monte Carlo of the ring-exchange model at V < K on the embedded lattice (probe 9 note, N7). Suggested concrete form: measure the k-resolved lowest coupled level directly from imaginary-time correlators C(tau, k) in the existing projector code (the effective mass converges to the level as tau grows and its convergence can be tested), instead of bounding it only through moment inequalities.
- Severity: major
- Status: open

### L06-W10: The Maxwell dynamics class is supplied, including energy conservation and the time rule
- Plain: Grant the ice rule. The photon's equations of motion (electric and magnetic fields updating by curl equations, energy conserved, time continuous) are still chosen. Within that choice Maxwell's equations are the unique answer, with one free speed. The choice itself is not derived, and the repo lists three competing ways to discretise time.
- Precise: The seven-item class: E on edge sites, B on face sites; real, linear, first-order, continuous time; nearest-neighbour reach; translation and cubic covariance; gauge-compatible; positive diagonal conserved energy; no extra payload.
  - Items 1, 2L, 6, 7 are "SUPPLIED IN THIS CONDITIONAL CLASS". Item 3 holds only if dynamics reads what Admissibility reads. Items 4 and 5 are mutually redundant.
  - Positive conserved energy is the load-bearing residual. Its nearest Record relative (the additive functional I) was removed from the axioms on 2026-08-13.
  - The three time rules of #7915 on one static kernel are inequivalent and unselected: a gradient sampler (relaxation proportional to k^2), a two-reflection spectral lift (phase proportional to |k|, tick-dependent speed), and the edge-face Maxwell generator (frequency proportional to |k|, conserves energy). The same static law does not select the time rule.
  - Orientation completion and a Record registration law are supplied for the Maxwell germ.
  - Gauge speed c is free; no coupling value.
- Evidence: docs/U1_DYNAMICS_CLASS_AXIOM_ADJUDICATION_BOUNDED_NOTE_2026-09-05.md:40-60; docs/U1_MAXWELL_LIGHT_LANE_LANDING_CORE_META_NOTE_2026-09-05.md:59-90,738-780,824-895,910-921; docs/MINIMAL_AXIOMS_2026-06-29.md:116-123,183-188; docs/U1_MAXWELL_LIGHT_LANE_LANDING_CORE_META_NOTE_2026-09-05.md:200-236 (the time-selection fork); .claude/science/physics-loops/u1-maxwell-landing-core-20260905/OPPORTUNITY_QUEUE.md.
- Axioms / supplied / proved:
  - Axioms: "Admissibility is not a dynamics axiom"; time metric, persistence dynamics, source/action are listed open.
  - Supplied: the seven-item class, the role compilation, the registration or overlap law, orientation completion.
  - Proved (unaudited): within the class the generator is a multiple of the oriented curl pair (unique up to sign and scale). Two conditional implications, (1,2L,3,4,7,OL) gives 5 and (1,2L,3,5,6,7) gives 4.
- Tried already: block 02 (2026-09-05) adjudicated item by item; block 03 collapsed vertex and cube payloads; the lane stopped budget-bounded with a ranked queue (conservation through reflection positivity; the time-selection fork).
- Same wall elsewhere: L02 (dynamics not supplied, action, Hamiltonian); L04 (time metric, single clock).
- Why it matters: "Maxwell from the axioms" is at best "Maxwell is the only member of a declared class".
- Cheapest known test or next step: queue item 1: carry conservation via reflection positivity to the payload level (two named supplies). The lane flagged the risk that this is target-equivalent.
- Severity: major
- Status: priced (equivalent to the declared class)

### L06-W11: The photon and matter need one light cone, and nothing forces it
- Plain: For relativity the photon and the fermions must travel at the same top speed. The approved primitive says the time tick is one lattice edge for matter, but it does not say this for the photon's field. In a tested toy (a walker plus a scalar with a Yukawa coupling) the two speeds drift apart by 0.026 g^2, and the gap does not shrink as the lattice is refined.
- Precise: The photon speed c = sqrt(UK) is free in the U(1) class. The kinetic-isotropy primitive supplies c_t = c_s for matter kinetics only, and the landing note says it does not identify the gauge speed with the matter speed.
  - Probe 3 of PR #9363 (numerical, two independent checks): v_psi - v_phi = +0.0263 g^2 in continuous time, regulator-dependent (12% shift under a retuned next-neighbour hop).
  - Hypercubic (Z^4) ticks are a sufficient protection: they force one cone for scalar and gauge-vector leading kernels. That is an added premise.
  - The gauge-to-matter coupling analogue for the qubit-link photon has not been computed.
- Evidence: docs/U1_MAXWELL_LIGHT_LANE_LANDING_CORE_META_NOTE_2026-09-05.md:78-82,864-870,910-921; docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md:20,38,69-72; origin/claude/toe-viability-probes-20260927:docs/TOE_VIABILITY_MAP_WHERE_THE_AXIOMS_ARE_EXPOSED_AND_THE_FASTEST_DECISIVE_TESTS_2026-09-27.md:168-178,253; docs/LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md; docs/EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md.
- Axioms / supplied / proved:
  - Axioms: none about speeds. Lattice is cubic; time is not in the axioms.
  - Supplied: c_t = c_s for matter (approved primitive); the gauge kernel's speed.
  - Proved (unaudited) or checked by others: the scalar-walker speed gap 0.0263 g^2; the one-cone result on the hypercubic surface for scalar and gauge-vector kernels.
- Tried already: June Collins-gate and naturalness-gap notes; probe 3.
- Same wall elsewhere: L04 (one light cone, Lorentz invariance); L14 (the graviton speed K/alpha is also free on the current surface).
- Why it matters: a U(1) with its own speed is not electromagnetism as observed. Observations bound speed differences very tightly.
- Cheapest known test or next step: suggested. Compute the analogue of the 0.0263 g^2 coefficient for a walker coupled to the link photon (one-loop, finite calculation). Or state the extension of the kinetic-isotropy primitive to the gauge action as an explicit owner decision.
- Severity: major
- Status: priced (equivalent to extending the kinetic-isotropy primitive to the gauge action)

### L06-W12: The link-and-role pattern breaks the axioms' one-qubit-everywhere covariance, and nearest-neighbour formation cannot build it
- Plain: The photon model puts qubits only on sites with exactly one odd coordinate and uses the rest as bookkeeping. The axioms have a qubit at every site and full cubic symmetry. A nearest-neighbour formation rule cannot make sites obey a balance rule around a neighbour: the chance of a completed pattern is at most 5/16 for the ice rule when formation order is arbitrary and the rule is unsoldered.
- Precise: The embedding is covariant only under translations by 2 sites and rotations about vertex or cube sites; qubits sit on 3/8 of sites.
  - Pair constraints are enforced in every formation order; star constraints (joint constraints on one site's neighbours, such as the ice rule) are not. Unsoldered bounds: role-letter link profile <= 16/243, Gauss parity 1/2, ice 5/16.
  - Four proper-cubic actions on qubit possibilities: only full soldering gives a covariant oriented link field, and then no nonconstant scalar charge exists (W14).
  - The role pattern is a next-nearest-neighbour support rule over roles, and "roles are not record values". Relational-letter constructions record the role pattern only under supplied extensions that covariance does not uniquely select.
- Evidence: the probe 9 note (full path in L06-W9):4,296-330,355-357; docs/STAR_CONSTRAINTS_UNDER_NEAREST_NEIGHBOUR_FORMATION_UNSOLDERED_BROADCAST_BOUNDS_AND_SOLDERED_REGISTRATION_OF_THE_PARITY_ROLE_SKELETON_BOUNDED_THEOREM_NOTE_2026-09-22.md:4; docs/THE_SOLDERING_MENU_FOUR_ACTIONS_OF_THE_PROPER_CUBIC_ROTATIONS_ON_QUBIT_POSSIBILITIES_AND_WHAT_EACH_LETS_FORMATION_BUILD_BOUNDED_THEOREM_NOTE_2026-09-22.md:4; docs/THE_SUPERLATTICE_ROLE_PATTERN_IS_A_NEXT_NEAREST_NEIGHBOUR_SUPPORT_RULE_OVER_ROLES_AND_ROLES_ARE_NOT_RECORD_VALUES_BOUNDED_THEOREM_NOTE_2026-09-04.md:4; docs/RELATIONAL_CYCLE_LETTERS_RECORD_THEIR_OCTANT_UNDER_THE_ROTATION_COVARIANT_STATIC_RULE_ON_THE_LANDED_ICE_TORUS_BOUNDED_THEOREM_NOTE_2026-09-23.md:4.
- Axioms / supplied / proved:
  - Axioms: a qubit at every site; full proper-cubic covariance; a single nearest-neighbour rule.
  - Supplied: the parity roles (vertex, edge, face, cube); the soldering action; the ice rule as a rule.
  - Proved (unaudited): the bounds above; the S4 character-table classification of the four actions; finite role-recording searches on side-2 to side-8 tori.
- Tried already: probe 9 records this as wall W_c; the September 22-23 notes; a "version with a qubit on every site and full Z^3 covariance" is queued but not built (map lines 314-318).
- Same wall elsewhere: L01 (formation order, unit and rate); L02 (Admissibility as a law); L14 (the tensor version inherits the same typing).
- Why it matters: the photon-from-records construction is not yet a model of the axioms as written.
- Cheapest known test or next step: build the qubit-on-every-site, fully covariant version named in the map (a finite model plus the ice-versus-formation-order bound check).
- Severity: major
- Status: open

### L06-W13: A field flip conflicts with permanent records unless records move with a fixed identity
- Plain: In the photon model a flip changes what a link holds, but the Record axiom says records are permanent. Read as records moving round a square, it needs a rule for which record is which. The rule is undefined so far, and different choices give different answers.
- Precise: A ring flip either (a) moves two records through a spectator vertex site by two nearest-neighbour steps, which needs an identity rule and passage through a site, or (b) deletes two and creates two, which violates permanence. Reading "up" as record content would change locked content. Probe 8 (as rewritten): which record carries a disturbance is a choice of identity. Hop-following lags behind it (1D ratios 0.20, 0.10, 0.05 at increasing size), whereas the Laplace identity travels with it (1.02 to 1.04).
  - An exact Gauss law freezes the link field under every two-site nearest-neighbour generator. The field moves only by rings and vertex-link-vertex hops inside one neighbourhood.
  - The number of records is conserved in the zero-winding sector (probe 7 consistency); per-vertex counts are 0/2/4/6.
- Evidence: the probe 9 note (full path in L06-W9):296-330; docs/DYNAMICS_CLAUSE_AN_EXACT_GAUSS_LAW_FREEZES_THE_LINK_FIELD_UNDER_EVERY_TWO_SITE_GENERATOR_THE_FIELD_MOVES_BY_RINGS_AND_HOPS_INSIDE_ONE_NEIGHBOURHOOD_BOUNDED_THEOREM_NOTE_2026-09-24.md:4; docs/HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md; owner memory viability-campaign-20260927.md items 12-14; owner memory records-move-owner-reading.md.
- Axioms / supplied / proved:
  - Axioms: "A site never carries more than one record; records are permanent"; motion is not stated (persistence dynamics is an open gate).
  - Supplied: the owner's moving-records reading; an identity rule (probe 8); ring moves.
  - Proved (unaudited): frozen-field theorem for two-site generators; hard-core motion generates ring terms; probe 8's identity dependence (checked).
- Tried already: probe 8 (rewritten after a referee round); the September 24 hard-core-record-motion and electric/magnetic-dynamics notes.
- Same wall elsewhere: L01 (moving records, formation and count); L03 (readout of position).
- Why it matters: "photon = records circulating around squares" needs it defined.
- Cheapest known test or next step: the map's item: "A records reading in which moves are arrivals, not content flips" (map lines ~314-318). That is a modelling decision plus a finite exact check of detailed balance with the pair-weight reading.
- Severity: major
- Status: open

### L06-W14: Electric charge and the strength of electromagnetism are not derived
- Plain: The strength of electromagnetism and the size of the unit charge are free. In the tested models the charged particle either cannot carry a charge that respects full cubic symmetry, or its coupling washes out the field's stiffness. A finite-size comparator estimate of the pure-ring model's own coupling is about 0.3, roughly 40 times the observed 1/137.
- Precise: No member of the U(1) lane assigns an electromagnetic unit or a fine-structure constant; the coupling normalization is named open by #7922 and #7932.
  - Charges are Gauss defects (a flip creates opposite unit defects at cost 2U). Under full soldering there is no nonconstant scalar one-qubit charge. Defects are bosons. Record phases are pure gauge.
  - The charged fermion's coupling screens the spin-half link field and supplies no transverse electric stiffness, so an induced (Sakharov-type) electric term is not available in that model; the pi-flux sea only selects the sign of the plaquette coupling.
  - The pure-ring comparator coupling estimate alpha_G is about 0.28 to 0.37 on 4^3 to 8^3 tori (finite, biased estimates, not certified).
  - Hypercharge scale alpha = 1/3 is supplied, and Q = T_3 + Y/2 holds on the left-handed surface only.
  - The owner treats the pair-weight scale as a free primitive-to-be, like the fine-structure constant.
- Evidence: docs/U1_MAXWELL_LIGHT_LANE_LANDING_CORE_META_NOTE_2026-09-05.md:879-884; docs/DYNAMICS_CLAUSE_CHARGES_ARE_GAUSS_DEFECTS_NO_QUBIT_CARRIES_A_COVARIANT_CHARGE_UNDER_FULL_SOLDERING_DEFECTS_ARE_BOSONS_AND_RECORD_PHASES_ARE_PURE_GAUGE_BOUNDED_THEOREM_NOTE_2026-09-24.md:4; docs/THE_FERMIONS_CHARGE_COUPLING_SCREENS_THE_SPIN_HALF_LINK_FIELD_AND_SUPPLIES_NO_TRANSVERSE_ELECTRIC_STIFFNESS_AND_THE_PI_FLUX_SEA_SELECTS_THE_SIGN_OF_THE_PLAQUETTE_COUPLING_BOUNDED_NOTE_2026-09-04.md:4,33-40; docs/RING_MODEL_WINDING_SECTOR_ENERGIES_GIVE_AN_ELECTRIC_COUPLING_THAT_AGREES_WITH_THE_TRANSVERSE_SUSCEPTIBILITY_ON_8_CUBED_AND_THE_COMPARATOR_COUPLING_CONSTANT_BOUNDED_THEOREM_NOTE_2026-09-25.md:76-90; docs/HYPERCHARGE_IDENTIFICATION_NOTE.md:44-56; owner memory records-move-owner-reading.md.
- Axioms / supplied / proved:
  - Axioms: no charge, no coupling.
  - Supplied: the Gauss rule with charges as defects; the detuning V; the coupling normalization; the hypercharge scale.
  - Proved (unaudited): the covariance and boson results; the screening result (finite sea tensors, not a universal exclusion); the comparator identities.
- Tried already: the September 3-4 fermion/U(1) notes; the September 24 charge notes; the ring-model winding-sector series.
- Same wall elsewhere: L05 (charged fermion, spin-statistics); L16 (alpha_EM as a dimensionless constant).
- Why it matters: alpha_EM and charge quantization are direct predictions a TOE should make.
- Cheapest known test or next step: suggested. Compute alpha_G in the ring model as a function of the supplied detuning V and see whether a natural V (RK, pure ring) can give about 1/137 (checks whether the value is a free parameter or a model number).
- Severity: major
- Status: open

### L06-W15: The chiral weak SU(2) and anomaly-complete hypercharge are added by premises
- Plain: The weak force acts only on left-handed particles. Here the su(2) comes from the same Clifford algebra as spin, and nothing makes it a left-handed gauge field. The right-handed partners and the anomaly-free hypercharge come from extra premises. The hypercharge pattern (+1/3, -1) is a left-handed eigenvalue pattern whose overall scale is set by hand.
- Precise: The qubit's internal su(2) equals the spatial spin su(2) only if the Clifford index is paired with the lattice edge direction (a conditional theorem). That pairing is not supplied by the tested structure; the qubit can spectate.
  - The finite normalizer theorem is blind to vector versus left-handed weak coupling; chiral su(2)_L is not derived.
  - Only the ratio 1:(-3) of the traceless abelian direction is forced; the absolute (+1/3, -1) pattern uses a supplied scale alpha = 1/3.
  - On the left-handed 8-state surface Tr Y = 0 but Tr Y^3 is nonzero. There are no weak singlets on it; u_R-like singlets do not appear until tensor degree 4.
  - The 3+1 and right-handed completion results depend on P-HY, P-ABJ, P-COMP and P-REC.
  - A single C^3 x C^2 carrier has no second central u(1) (colour campaign, block 04).
- Evidence: docs/SU2_DOUBLE_USE_REDUCES_TO_ONE_INDEX_PAIRING_ADMISSION_BOUNDED_NOTE_2026-06-08.md:16-40; docs/GAUGE_FACTOR_PRESERVATION_RECORD_TYPED_SELECTOR_CONDITIONAL_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-07-06.md:46; docs/HYPERCHARGE_IDENTIFICATION_NOTE.md:44-56; docs/LEFT_HANDED_CHARGE_MATCHING_NOTE.md:20-40; docs/GAUGE_MATTER_CLOSURE_GATES_2026-04-12.md:94-110; docs/ANOMALY_FORCES_TIME_THEOREM.md:12-25; docs/NATIVE_GAUGE_CLOSURE_NOTE.md (Boundary); archive/notes/docs/COLOR_DERIVATION_CAMPAIGN_20260706_ASSEMBLY_AND_HONEST_REBOUNDING_META_NOTE_2026-07-06.md:79-92.
- Axioms / supplied / proved:
  - Axioms: a qubit per site; nothing about chirality or hypercharge (chirality is an open gate; the staggered-Dirac realization is listed open).
  - Supplied: the index pairing; the taste-cube realization; P-HY, P-ABJ, P-COMP, P-REC; the scale 1/3.
  - Proved (unaudited): the structural ratio 1:(-3); Tr Y = 0; the su(3) cubic-anomaly and 3-bar completion theorem given the left-handed content.
- Tried already: chiral-completion search (no low-degree natural completion, GAUGE_MATTER_CLOSURE_GATES:100-110); the 2026-06 normalizer and no-go notes; the scale-bridge note that only proves an implication from a supplied packet.
- Same wall elsewhere: L05 (chirality, handedness; the viability handedness probe shows a free two-band walker is balanced, flowing or ticking); L07 (electroweak breaking, weak angle); L04 (anomaly-forces-time premises).
- Why it matters: without a chiral weak gauge field there is no weak interaction, and without anomaly-complete hypercharge the SM matter content is not fixed.
- Cheapest known test or next step: the parked-decision wake condition 2 (docs/repo/DEFERRED_DECISIONS.md entry 2) fires when a weak-sector result needs the orientation bit. Otherwise, suggested: test whether the tick-based chirality (a chiral free tick needs exponential tails; probe 2) is compatible with the taste-cube su(2) at all.
- Severity: blocking
- Status: priced (equivalent to four named premises plus the chirality supply)

### L06-W16: A controlled multiscale flow for gauge fields plus staggered matter exists only in a heavy-mass, zero-coupling corner
- Plain: The repo's most serious attempt to connect the lattice scale to physical scales runs the gauge field and the staggered fermions together through successive coarse-graining steps. It closes only in a corner (extremely heavy fermions, beta = 0). Six named obstacles remain, each independent of the others, so no controlled flow exists for the physical regime.
- Precise: The July 2026 Wilson-staggered series (24 notes) proves exact Schur and Berezin block identities, coefficient-norm repairs and counterterm ledgers for the SU(3), beta = 0 finite-sector grammar, with witness parameters such as m = 10^96.
  - Six deliberately non-absorbing open walls: same-domain return; generic generated-factor, source and provenance closure; perturbative centre update, gap and normalization; a retained-algebra two-mark Hessian and nonlinear estimate; physical taste and chart selection; a chart-relative critical trajectory and observables.
  - The latest notes are conditional on an unproved constant-one two-root cluster injection (Block 47), typed open_gate.
  - The extracted running centre is positive Hermitian, not the original staggered Dirac form, and does not restore taste.
- Evidence: docs/WILSON_STAGGERED_EXTRACTED_S2_FUTURE_CENTER_PRODUCT_REFERENCE_COUNTERTERM_PERSISTENT_GAP_BOUNDED_THEOREM_NOTE_2026-07-12.md:505-520,570,660-696; docs/WILSON_STAGGERED_ENHANCED_COMPLETED_JOINT_RUNNING_LOCAL_JET_TARGET_TO_NEXT_PRODUCT_SOURCE_RETURN_BOUNDED_THEOREM_NOTE_2026-07-13.md:3-20,467-470; docs/WILSON_STAGGERED_GAUSSIAN_ADAPTED_BEREZIN_HANDOFF_AND_SHORTEST_QUADRATIC_CENTER_BOUNDED_THEOREM_NOTE_2026-07-12.md:425-438; docs/MINIMAL_AXIOMS_2026-06-29.md:178.
- Axioms / supplied / proved:
  - Axioms: none; the staggered-Dirac and finite-Grassmann realization is itself a listed open gate.
  - Supplied: the Wilson-staggered grammar, the RG chart, the heavy-mass wedge and the finite regulators.
  - Proved (unaudited): the block identities and norm bounds inside that wedge; a repair is followed by a new obstruction in each note (N8 echoes).
- Tried already: the whole July 12-13 series; the September packet-operator gap (W8) covers the pure-gauge part only.
- Same wall elsewhere: L07 (hierarchy transport from the Planck lattice to the weak scale); L05 (physical taste selection is one of the six walls); L16 (constants).
- Why it matters: it is the only route in the repo that would give a controlled bridge for W7 and W8. Until it closes, both bridges are assumed.
- Cheapest known test or next step: the single named open obligation, the constant-one two-root cluster injection (pay the meeting-anchor, cut, support and routing multiplicities), docs/WILSON_STAGGERED_COMPLETED_JOINT_TWO_MARK_COVARIANCE_NONLINEAR_SOURCE_OUTPUT_TUBE_BOUNDED_THEOREM_NOTE_2026-07-13.md:5,12-16,154. Alternatively restate the target as a fixed-lattice statement, which the fixed-lattice scope note says has a different burden.
- Severity: major
- Status: open

## Walls considered and rejected

- Link connection has no origin: rejected as a wall. It is derived at kinematic level from local frame redundancy (docs/MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md:24-40), conditional on the registered surface. The action is W4.
- W85 Wilson-to-saddle uniform bound: was an open gate in June, closed for the packet operator on 2026-09-02 (NATIVE_GAUGE_TRANSFER_A2_REFLECTION_UNIFORM_HALF_LINE_GAP_THEOREM_NOTE_2026-09-02.md:48). Its limited scope is in W8.
- Finite-volume gap on the compact SU(3) cube: proved conditional (GAUGE_WILSON_COMPACT_CUBE_ALL_COUPLING_GAP...:6); finite volume gives a gap trivially. The infinite-volume statement is W8.
- Anomaly cancellation for SU(3)^3: algebraic given the left-handed content (SU3_ANOMALY_FORCED_3BAR_COMPLETION_THEOREM_NOTE_2026-05-02.md:1-20); the premises are in W15. A Witten SU(2) anomaly note exists (SU2_WITTEN_Z2_ANOMALY_THEOREM_NOTE_2026-04-24.md); not read here.
- Gluon tree-level masslessness (GLUON_TREE_LEVEL_MASSLESSNESS_THEOREM_NOTE_2026-05-02.md): standard tree-level Yang-Mills algebra on a supplied SU(3) field surface; it does not derive that surface (that is W1, W4), so it is routine, not a wall.
- Reflection positivity of the finite-volume SU(N) Wilson temporal-gauge slab: proved conditional by direct representation-ring argument (AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md:22-40). Not a wall; the time-direction premises are L04's.
- SU(3) Wigner-intertwiner block4/5 scope split and other May audit repairs: routine audit bookkeeping (PLAQUETTE_ALPHA_S_CHAIN_AUDIT_MAP...:97-135).
- Running-kernel imports (4-loop beta function, thresholds, Sommer scale): part of W7, not separate.
- Ring-model estimator engineering (guides, populations, projection age, resampling): routine numerics inside W9.
- Magnetic monopoles and compact-U(1) topological sectors: not attempted by the lane (restricted to the smooth zero-monopole branch), so no wall yet. Named as unattempted in W9.
- Strong CP angle theta: L11. Higgs, W/Z masses and the electroweak scale: L07. Staggered doublers and the number of generations: L05 and L08.
- N_c = d counterfactual for the colour count: support only (GAUGE_ALGEBRA...:66-76), not a wall.
