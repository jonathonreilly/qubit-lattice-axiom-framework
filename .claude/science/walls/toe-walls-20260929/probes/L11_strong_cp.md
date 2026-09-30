# Lane L11: Strong CP and theta (theta-bar = 0, determinant and readout obligations) — walls

Repo snapshot: `origin/main` at `7146fe17a7` (checkout `.../scratchpad/main_wt`). All paths below are relative to it. Labels: proved = landed or referee-confirmed; checked = a test I ran; suggested = argument not yet checked; reading = interpretation.

## Lane map (under 200 words, plain language first)

Strong CP asks why the strong force treats a world and its mirror-and-time-reversed twin alike. Physics allows one twist angle, theta-bar = theta_gauge + arg det(M_quark). Experiment says it is below 1e-10.

Best result: a bounded theorem that theta-bar = 0 exactly on a *selected* surface (real-positive Wilson-type gauge weight, real scalar staggered quark masses, K-real determinant). The runner passes 55/55 (checked). The last audit (2026-07-13, `audited_conditional`) said the surface is chosen, not derived. Today all 5299 ledger rows are `unaudited` after the axiom-epoch resets, so history is the only status signal.

The gauge half closes only because the gauge weight is imported as real and positive. The mass half rests on two registered open obligations. No theta note is dated after 2026-07-18. The 2026-08-05 axiom text (Admissibility is a probability distribution) and the 2026-08-13 text (readout additivity removed) have not been applied to any theta note.

Reading: the axioms hold probabilities, not actions or amplitudes. "A theta term in the action" has no home until the source/action gate closes.

## Walls

### L11-W1: The theta-free gauge weight (real, positive, Wilson-type) is imported, not derived
- Plain: The gauge half of the answer works only for a gauge-field weight that is assumed real and positive. Such a weight cannot carry a twist angle. The axioms do not say the weight has that form. A two-plaquette term that does carry the twist passes every symmetry test the lane tried. So the zero comes from the chosen class, not from the axioms.
- Precise: Target: from the four axioms, show the emergent gauge weight has no CP-odd F∧F (theta) term. Holds only in the "canonical imported Wilson + staggered-Wilson class": real-positive Boltzmann branch (P4/P5), beta = 6 (g_bare^2 = 1), single-plaquette class. Inside it, for every emergent integer sector functional Q with adjacent populated sectors, any relative weighting e^{i theta q} m~(q) with m~ > 0 forces theta = 0 mod 2 pi (Theorem T, proved). Outside it nothing is excluded: the clover/two-field-strength `i theta q` slot is gauge-invariant, local, CPT-even and reflection-positivity-compatible, so reality, positivity, CPT, RP, locality and gauge invariance cannot remove it. The per-plaquette license that would confine the action needs `(P-FUND-1TICK)`, which is open. The action form is not unique (Wilson, heat-kernel, Manton). Quantifiers: for all Q inside the class (proved); there exists an admissible weight outside it (not excluded).
- Evidence:
  - `docs/WILSON_REAL_POSITIVE_MEASURE_BOUNDED_PREMISE_BRIDGE_NOTE_2026-06-03.md:29-37` (real-positive branch and beta=6 are a row-local premise, "not derived here")
  - `docs/THETA_GAUGE_NATIVE_POSITIVE_CLASS_EMERGENT_SECTOR_WEIGHTING_NARROW_THEOREM_NOTE_2026-07-04.md:134-196,240,249` (Theorem T; scope is the imported class; a signed native class "would need its own analysis")
  - `docs/STRONG_CP_GAUGE_THETA_MULTIPLAQUETTE_FTF_IS_ADMISSIBLE_NOT_CLEAN_CLOSEABLE_BOUNDED_NOTE_2026-06-07.md:38-41,56-57`
  - `docs/STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md:38-50`
  - `docs/STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md:43-62`
  - `docs/PER_PLAQUETTE_LICENSE_ONE_TICK_REACHABILITY_DERIVATION_NARROW_THEOREM_NOTE_2026-07-12.md:62-64`
  - `docs/BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md:11,30`
  - `docs/STRONG_CP_THETA_ZERO_NOTE.md:4,496-513`; ledger `docs/audit/data/ledger/st/strong_cp_theta_zero_note.json` (previous_audits, 2026-07-13)
  - `docs/MINIMAL_AXIOMS_2026-06-29.md:60,187`
- Axioms / supplied / proved:
  - Axioms: Admissibility gives a real, non-negative probability distribution over one-site possibilities (`MINIMAL_AXIOMS_2026-06-29.md:60`). No gauge field, action or complex weight. "Source/action" is a listed open gate (`:187`).
  - Supplied: Wilson class, beta = 6, real-positive branch (P4/P5), per-plaquette class, license `(P-FUND-1TICK)`.
  - Proved: Theorem T inside the class (audited_clean 2026-07-05; runner 8/8, checked). A single plaquette has no cross-plane F∧F. The multi-plaquette slot is admissible.
- Tried already:
  - RP route: `STRONG_CP_RP_HALF_...NO_GO_...2026-05-16.md` (RP cannot forbid the CP-odd imaginary half).
  - Reality/positivity/CPT route: `STRONG_CP_GAUGE_THETA_NOT_FORCED_...2026-06-07.md:38-50` (none forces theta = 0).
  - Single-plaquette minimality: `NEWPHYSICS_NP_STRONG_CP_THETA_NOTE_2026-05-10_npCP.md:68` (class is "admitted, not derived").
  - Adjacency license: `PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_...2026-06-09.md:24`, multi-plaquette narrowing 2026-06-11, one-tick derivation 2026-07-12 (all conditional on `(P-FUND-1TICK)`).
  - Axiom-update shortcut: `THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md:58-70`. It quotes superseded axiom wording ("finite scalar additivity" line 72, "availability" line 78; checked by grep). The audit lane records its runner failing live, 151 pass / 6 fail (`docs/audit/N5_DRAIN_REPAIR_BACKLOG_2026-08-08.md:68`).
- Same wall elsewhere:
  - Gauge action and coupling lane (action-form ambiguity; "g_bare = 1 convention handling" is in the axioms' open-gate list, `MINIMAL_AXIOMS_2026-06-29.md:188`).
  - Source/action gate.
  - Koide r and CKM delta: `ARROW_CPT_ORIENTATION_DO_NOT_SOURCE_CP_ODD_ACTION_COEFFICIENTS_NO_GO_NOTE_2026-06-08.md:51-58` says r, delta, theta are the same kind of unsourced action coefficient; the multiplaquette note (`:56-57`) calls theta_gauge "structurally parallel" to Koide r = 1/2.
  - The non-negative-weights premise POS in the kernel/induced-law lane (parked, `docs/repo/DEFERRED_DECISIONS.md` section 3).
- Why it matters: Without it theta_gauge is a free parameter. The TOE cannot claim to explain theta-bar = 0. Reading: the framework's own waves need signed weights (`docs/ADMISSIBILITY_RULE_WAVES_NEED_SIGNED_WEIGHTS_...2026-09-24.md` claim scope: non-negative-weight rules cannot make undamped waves). A phase-carrying (amplitude-layer) gauge weight is then the expected case, and the positivity argument does not cover it. That tension is not discussed in any theta note.
- Cheapest known test or next step: (suggested) Re-run the axiom-update no-go against the current Admissibility text. Ask whether a complex weight e^{i theta Q} can be a distribution "determined by nearest-neighbor conditions" (a probability is real and >= 0). If the emergent gauge weight must be a pushforward of that distribution, the class is derived rather than imported. The blocker is the identification of link weights with the local-possibility distribution (the open source/action gate). No theta note mentions the 2026-08-05 wording (grep, checked). Alternative: derive `(P-FUND-1TICK)`.
- Severity: blocking
- Status: priced (equivalent to the named premise "the gauge weight is real-positive and single-plaquette Wilson-type")

### L11-W2: One unsupplied orientation bit sits under both halves of theta-bar
- Plain: A twist angle needs a sense of handedness: which way is right-handed, and which way records are ordered. The axioms supply rotations but not mirror reflections, so they do not say whether the law can tell left from right. Mirror-asymmetric rules are allowed. The same missing bit sits under the mass half, because flipping handedness is complex conjugation on the qubit algebra. The real weak force is handed, so "the law is mirror-symmetric" cannot simply be assumed.
- Precise: Target: show the law is blind to the orientation bit (spatial orientation times record-order orientation). That would give theta_gauge = 0 (Q = e·b flips sign under it) and a K-real mass (arg det in {0, pi}) in one step. Fails: Lattice and Admissibility name only proper rotations; Q -> det(S) Q under improper operations; no orientation datum is in the supplied structure (Theorem 3, proved); orientation swap = complex conjugation on the one-site algebra (Theorem 4, proved; runner 20/20, checked). Handed admissibility rules exist under all three covariance readings (Burnside dimensions 90 / 43 / 4540). The owner decision on whether "distinguished by the supplied algebraic structure alone" makes every rule achiral is parked with default "not adopted either way". Reading: even if adopted, the weak sector's handedness and CKM delta would then have to be state-level, i.e. a Nelson-Barr-type structure, which is a separate unsolved item.
- Evidence:
  - `docs/MINIMAL_AXIOMS_2026-06-29.md:38,58`
  - `archive/notes/docs/THETA_NATIVE_RECORD_TIME_SPATIAL_SPLIT_ORIENTATION_IMPORT_LOCALIZATION_CONJUGATION_PARITY_BRIDGE_BOUNDED_THEOREM_NOTE_2026-07-03.md:84-127,197`
  - `docs/STRONG_CP_PARITY_MEASURE_CORRECTION_ORIENTATION_GATE_NO_GO_NOTE_2026-06-08.md:27-40` (parity-invariant color action gives theta_gauge = 0, but "not forced by the minimal axioms"; runner 7/7, checked)
  - `docs/ADMISSIBILITY_HANDED_RULE_PSEUDOSCALAR_INVARIANT_CENSUS_AND_PARITY_ODD_RECORD_CORRELATORS_BOUNDED_THEOREM_NOTE_2026-09-13.md:25-34`
  - `docs/repo/DEFERRED_DECISIONS.md:50-77` (section 2, wake condition 2 at `:73`)
  - `docs/audit/AXIOM_MINIMALITY_POLICY.md:344-347` (the qualification "does not by itself establish theta = 0")
  - `archive/chains/july-theta-era.md:26-31`
- Axioms / supplied / proved:
  - Axioms: proper cubic rotations only; the Qubit sentence "distinguished by the supplied algebraic structure alone"; no orientation, no time order.
  - Supplied: an ordered spatial frame or a parity-even color action, or the achiral reading (parked, not adopted).
  - Proved: Q = e·b; Q is odd under each unsupplied flip separately; a swap-closed ensemble sums the theta seed to zero; handed rules exist (unaudited, bounded).
- Tried already:
  - Parity gate `STRONG_CP_PARITY_MEASURE_...2026-06-08.md`: parity-even color action gives theta = 0, but its premise is not derived.
  - Epsilon-pseudotensor bridge `STRONG_CP_EPSILON_PSEUDOTENSOR_OH_SIGN_BRIDGE_...2026-05-26.md`.
  - Native split 2026-07-03: localized both halves to this single bit.
  - Handed-rule census 2026-09-13: showed handed laws are allowed. No note I found computes whether a handed rule seeds an E·B (theta-type) coefficient.
- Same wall elsewhere: Weak-sector handedness/chirality lane (`docs/repo/DEFERRED_DECISIONS.md:73`; viability map "Handedness" row: nothing in the free lattice prefers a hand). Charged-lepton generation count and Brannen phase chirality (`KOIDE_DELTA_PHASE_AND_GENERATION_COUNT_SHARE_ONE_Z2_ORIENTATION_...2026-06-08.md:24,137`, "does the framework force a global handedness selection?"). CKM delta.
- Why it matters: This is the only single premise that would close both halves at once. It is also the premise that determines whether the weak CP phase must be spontaneous. Leaving it open leaves W1 and W4-W7 all needed.
- Cheapest known test or next step: (suggested) For the handed rules W_0 and W_X in the 2026-09-13 census, compute whether the induced gauge-sector kernel acquires a parity-odd two-field-strength (E·B) coefficient at leading order. If it does, handedness maps to theta != 0. If it does not, the parity worry may be moot for theta. This is a finite computation on the existing seven-site-window code. Deciding parked decision 2 is the owner's call, not this lane's.
- Severity: major
- Status: priced (equivalent to the parked structuralist/achiral reading)

### L11-W3: No emergent topological charge Q; the positive route G1-G4 is stalled
- Plain: To say "the twist angle has a value" you need a whole-number charge counting how the gauge field is wound. On the lattice as given there is nothing to wind: the gauge group at each site is connected, and the only whole-number label found is a three-valued one. Four sub-steps toward a real charge are all open. The lane re-scoped this as not needed for theta-bar = 0. That is true only if W1's premise holds.
- Precise: Target: derive an integer sector functional Q with non-vacuous weighting and physical registration from a 3+1 native history. Steps: G1 defect closure dn = 0 (or suppression); G2 non-abelian sector/readout registration; G3 phase-type F∪F insertion (selected functional, phase coefficient, physical registration); G4 assembly with arg det M. Fails: finite per-site gauge groups are connected, so the Hamiltonian pi_0 carrier is empty; the per-plaquette class has no Q density; an integer Q needs a branch/section choice Record does not supply; the only finite sharp additive label is the center Z_3 grading (no Z-valued label, nullity 0); G1 and G3 are "not derived on the current surface". The four gauge steps are independently closable (N2).
- Evidence:
  - `docs/THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md:23,41-75`
  - `docs/GAUGE_CENTER_SECTOR_RECORD_CONTEXT_AND_THETA_Q_CHARACTER_GRADING_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-01.md:47-65`
  - `docs/THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md:62-90,124-136`
  - `docs/THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md:132-145,162-172`
  - `archive/notes/docs/THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md:19-70`
  - `archive/notes/docs/THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md:19-60`
  - `docs/STRONG_CP_THETA_ZERO_NOTE.md:391`
  - `archive/notes/docs/THETA_RETIREMENT_BASIS_REMATCH_2026-07-04.md:131-145`
  - `docs/ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md:33-50`
- Axioms / supplied / proved:
  - Axioms: Z^3 with nearest-neighbor adjacency; no gauge group, no fourth lattice direction, no topology.
  - Supplied: closed-branch T^4 flux template (Q = intersection pairing) and fixed-grading paired-shift bookkeeping (witness surfaces, not native).
  - Proved: substrate carriers are empty (bounded); center grading is the only finite additive label; G1 and G3 are not supplied by the axioms or primitives.
- Tried already: G1 and G3 no-goes 2026-07-04 (both runners fail one live check per the audit backlog, `N5_DRAIN_REPAIR_BACKLOG_2026-08-08.md:66-67`). Positive-route stretch ranks G3 next (`THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md:124-136`). Weyl label-shift slot obstructed. Link-star gluing is orientation-even. 2D U(1) supplier works and the 4D template is conditional.
- Same wall elsewhere: ABJ anomaly lane (`ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_...2026-05-30.md`: the staggered epsilon-index vanishes on a balanced periodic Z^4 torus, so (P1') is unmet). Topological-susceptibility and instanton-infrastructure material. Gauge-structure lane (SU(3) star reduction).
- Why it matters: If W1's premise is refused, this is the only handle for saying what theta does. It also carries the physical meaning of theta-bar (the axial-anomaly link in theta_bar = theta_gauge + arg det M).
- Cheapest known test or next step: (suggested) G1 as a finite check on the existing `T^4_2` cochain code: does a nearest-neighbor admissibility support restriction generate closed 2-cochains (dn = 0)? The N5 runner already enumerates this space. Otherwise follow the lane's own plan (G3 first).
- Severity: minor (rises to blocking if W1's premise is refused)
- Status: open

### L11-W4: The mass side is closed only on a supplied surface: real scalar mass, K-real operator, positive orientation
- Plain: The mass half is closed only if quark masses are plain real numbers on a special hopping operator whose eigenvalues come in plus/minus pairs. The axioms contain no quark masses, Yukawa couplings or Higgs. The July sign-independence proof was marked failed by the audit: at zero mass with a zero mode the determinant vanishes and its phase is undefined.
- Precise: Target: derive M = m·I (no pseudoscalar M_eps, no complex phase), the K-real Case-A structure (real antisymmetric hopping, bipartite grading) and arg det = 0 from the axioms. Fails: the scalar-mass class is a "row-local bounded premise ... not derived here". The pairing identity det(K + mI) = prod(m^2 + lambda^2) m^{2z} >= 0 fixes arg det = 0 only where det != 0. Audit `audited_failed` (2026-07-10) on the headline covering m = 0 with zero modes. Scope excludes Wilson shifts, non-commuting flavor couplings and non-K-real flavor blocks. Leg B ("axial rotation exits the class") is a definition of the class. The runner sets the quark masses real and positive by construction (`y_t = 0.9176` with the check `y_t > 0`, lines 935-936).
- Evidence:
  - `docs/STAGGERED_SCALAR_MASS_CLASS_BOUNDED_PREMISE_BRIDGE_NOTE_2026-06-03.md:19,27,54`
  - `docs/STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md:36-52`
  - `docs/THETA_MASS_ORIENTATION_ZERO_BRANCH_PAIRING_FORCED_ON_K_REAL_SURFACE_NARROW_THEOREM_NOTE_2026-07-01.md:4-20` (runner 18/18, checked); ledger `theta_mass_orientation_zero_branch_...2026-07-01` previous_audits, 2026-07-10 `audited_failed`
  - `archive/chains/july-theta-era.md:38-45` (arg det undefined at m = 0 with a zero mode)
  - `docs/STRONG_CP_THETA_ZERO_NOTE.md:15,130-158,504-509`
  - `scripts/frontier_strong_cp_theta_zero.py:935-939`
  - `docs/MINIMAL_AXIOMS_2026-06-29.md:178`
- Axioms / supplied / proved:
  - Axioms: M_2(C) one-site algebra; no mass term, no Higgs, no Yukawa, no staggered kinetic operator.
  - Supplied: scalar-mass class, positive convention, K-real Case-A determinant channel.
  - Proved: on the supplied surface det >= 0 for both mass signs; arg det = 0 on the nonzero-determinant locus (checked in scratch: `L11_scratch/checks.py` C4; parent runner 55/55). The scalar-mass class itself is not derived.
- Tried already: Operator-basis note 2026-05-19 (audit chain: failed 2026-05-29, then conditional). Scalar-mass premise bridge 2026-06-03. Pairing note 2026-07-01. Composition close 2026-07-03. Epsilon-hermiticity reality bridge 2026-06-11.
- Same wall elsewhere: Staggered-Dirac / finite-Grassmann realization gate (`MINIMAL_AXIOMS_2026-06-29.md:178`). Quark-mass and Yukawa lanes (y_t is an input). Koide K-real circulant (same C_3 object; `THETA_RETIREMENT_BASIS_REMATCH_2026-07-04.md:59-68`).
- Why it matters: Without a derived mass class, "arg det M_q = 0" is a statement about a chosen mass matrix. The framework has no mechanism that keeps the physical Yukawa couplings inside the class.
- Cheapest known test or next step: (suggested) Restate the pairing theorem with m = 0 and z >= 1 excluded explicitly, and compute whether the physical mass (m > 0) locus is protected against the zero-mode boundary under the lattice's own spectral flow. This is a scope fix, not new physics. The deeper item is deriving M_eps = 0, which reduces to W2 (a pseudoscalar mass is odd under improper operations).
- Severity: major
- Status: priced (equivalent to the named premise "quark mass term is a real scalar on a K-real staggered operator")

### L11-W5: Quark-determinant cross-sector readout (registered open obligation)
- Plain: Registered open problem: is the object that fixes the charged-lepton counting rule the same physical channel that controls the quark mass determinant, and does that force the quark determinant phase to zero? Nobody has constructed the quark mass carrier or shown the link. What exists is conditional algebra: if the two are the same channel, the phase vanishes.
- Precise: Target (`derivation_obligations.json`): derive whether the charged-lepton K/CPT occupancy carrier is the same channel as the quark determinant readout, and whether that forces arg det(M_q) = 0. Closure needs: construct the quark mass/determinant carrier, identify the physical readout map, prove the cross-sector correspondence; "algebraic similarity, shared notation and historical decision text are insufficient". Two minimal forcing pairs exist (conjugate-pair cancellation + orbit constancy => h = 0; character law + orbit constancy => k = 0), with witnesses that neither member can be dropped. Cancellation is a supplied condition, not a Record consequence. Nothing derives that the quark channel belongs to either class.
- Evidence:
  - `docs/THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md:9-36`
  - `docs/audit/data/derivation_obligations.json` (id `theta_quark_determinant_cross_sector_readout_derivation_obligation`, status `open_gate`)
  - `docs/KEY_SCIENCE.md:35-38`
  - `archive/notes/docs/THETA_CROSS_SECTOR_DETERMINANT_FORCING_PROPERTY_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md:4,55-76,138-160`
  - `archive/notes/docs/THETA_MASS_SIDE_COMPOSITION_CLOSE_ON_SHARED_OCCUPANCY_BRIDGE_BOUNDED_NOTE_2026-07-03.md:18-30,74-84`
  - ledger `theta_quark_determinant_cross_sector_readout_derivation_obligation`, previous audit 2026-07-25 `audited_conditional` ("target-equivalent")
- Axioms / supplied / proved:
  - Axioms: none of K/CPT structure, quark carrier, determinant channel or physical readout (K/CPT left Record on 2026-06-29: `MINIMAL_AXIOMS_2026-06-29.md:142,169` and `KCPT_ORBIT_CONSTANCY_...2026-07-04.md:11-13`).
  - Supplied: the identification itself (as a hypothesis); orbit constancy; block multiplicativity.
  - Proved: conditional forcing algebra only. Composition `arg det M_q = 0` holds given both bridges (W5 and W6).
- Tried already: Composition close 2026-07-03 (splits W5 from W6). Axiom-update mass no-go 2026-07-04 (four independent mass walls; `THETA_MASS_DETERMINANT_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md:136-148`; runner 109 pass / 8 fail live per the audit backlog, `N5_DRAIN_REPAIR_BACKLOG_2026-08-08.md:90`). Forcing characterization 2026-07-17. Post-erasure log equivalence 2026-07-18.
- Same wall elsewhere: Charged-lepton lane (the occupancy carrier being tested). Flavor/CKM quark-sector lane ("quark-sector transport remains separate", `STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md:75-78,90-95`).
- Why it matters: This is the exact named blocker for the mass half. While it stands, every theta result using the identification is "conditional or pending-chain".
- Cheapest known test or next step: (suggested) Build the quark mass/determinant carrier explicitly in the C_3 generation model and test whether the quark mass block and the charged-lepton block share the same K/CPT orbit indexing. This needs the quark-sector carrier that the flavor lane already constructs (QUARK_CP_CARRIER_COMPLETION notes); no theta note has tried it.
- Severity: blocking
- Status: open

### L11-W6: Charged-lepton occupancy grain (registered obligation, owned by the charged-lepton lane; the theta mass side rides on it)
- Plain: Registered open problem: does the matter action count a particle/antiparticle pair once or twice? Both counts extend the same four-axiom model, so the axioms do not choose. The mass half of strong CP was written to reuse the "once" answer, so it is conditional on it.
- Precise: Target: derive the physical matter action and measure and distinguish the count-once det_C (holomorphic) realization from the count-twice |det_C|^2 (realified) one without inserting the desired value. No-go: F_C = log|det A| and F_R = 2 F_C are both additive, similarity-invariant and conjugation-invariant on the same record model. The 2026-08-22 selector-boundary probe found that a real-linear map into positive blocks is zero and separating |z| from |z|^2 needs a comparison domain with |z| outside {0,1}. The named closer is a running "kappa/counting" program; no landed result.
- Evidence:
  - `docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md:9-34`
  - `docs/ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md:16-70`
  - `docs/ACPHILAMBDA_RECORD_POSITIVITY_DETERMINANT_POWER_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-22.md:4`
  - `docs/STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md:59-64`
  - `docs/audit/data/derivation_obligations.json`; `docs/audit/AXIOM_MINIMALITY_POLICY.md:572-595` (2026-07-11 correction: theta mass side "conditional on the occupancy obligation")
- Axioms / supplied / proved:
  - Axioms: nothing about determinant power, Grassmann measure or matter action.
  - Supplied: count-once reading (hypothesis).
  - Proved: non-supply (both horns extend the same model, bounded).
- Tried already: The three AC notes above. The staggered-Dirac realization gate note (`docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`, audited_clean 2026-07-06 as a bounded theorem) exposes labeling as a no-go plus a convention, so it does not close this.
- Same wall elsewhere: This is the charged-lepton (Koide / AC_phi_lambda) lane's own wall. Also the taste/species-reduction question for staggered fermions.
- Why it matters: The 2026-07-05 theta "retirement" relied on this piece as a premise; the 2026-07-11 owner correction reopened it as an obligation.
- Cheapest known test or next step: Owned by the charged-lepton lane. For theta, a useful test is whether the mass-side conclusion is sensitive to the counting at all. (Reading, unchecked: a squared modulus carries no phase, so the two counts differ in whether a phase can survive; the lane has not tested this.)
- Severity: blocking
- Status: open

### L11-W7: The determinant-readout interface is entirely supplied, and it is a statement about record readouts, not about the action
- Plain: The mass-half "phase erasure" is algebra inside a made-up class of readouts: blocks multiply, conjugate outcomes count the same, the readout is additive and reads the determinant. Each was supplied. The additivity clause was deleted from the Record axiom on 2026-08-13, and K/CPT left the axioms on 2026-06-29. Also, the theorem concerns what records can register; strong CP concerns a phase in the dynamics.
- Precise: Target: show the physical arg det(M_u M_d) contribution is exhausted by a determinant-character readout with k = 0. Supplied context: (i) the note's "W2" physical registrability (additivity + orbit constancy); (ii) action-level theta_eff determinant entry; (iii) ORBIT-INDEXING; (iv) determinant-character/log-character homomorphism; (v) conjugate-pair cancellation. Hostile guard: cos(arg det M) is K-even, phase-sensitive and excluded only by (iv). Additive-readout algebra (Record finite additivity) no longer exists in the axiom text, so the whole character route needs a fresh supplier. Post-erasure: product-to-sum has only the zero solution for non-negative readouts, and log is the signed solution.
- Evidence:
  - `docs/THETA_P2_DETERMINANT_READOUT_EXHAUSTION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md:57-70`
  - `docs/KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md:16-17,63,70-71`
  - `docs/STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md:40-57,116-118` (runner 19/19, checked)
  - `docs/MINIMAL_AXIOMS_2026-06-29.md:220-224` (2026-08-13 removal of `I` and finite additivity); `docs/repo/DEFERRED_DECISIONS.md:105` (July legs consuming the removed sentence are flagged)
  - `docs/OBSERVABLE_PRINCIPLE_P2_PHASE_BLINDNESS_SECTOR_RESOLVED_NARROW_THEOREM_NOTE_2026-06-04.md:42` (residual routes to the determinant identification)
  - `archive/notes/docs/THETA_POST_ERASURE_ODD_SIDE_LOG_EQUIVALENCE_AND_ADDITIVITY_INCOMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-18.md:4`
  - `docs/MINIMAL_AXIOMS_2026-06-29.md:180` (open gate "P2/modulus/phase-blindness and any log-det readout theorem")
- Axioms / supplied / proved:
  - Axioms: "Only records are readable; a readout value is determined by record content alone" (`:82`). No additivity, no K/CPT, no determinant.
  - Supplied: (i)-(v) above.
  - Proved: k = 0 and h = 0 inside the supplied classes (checked, runner 19/19); non-removability witnesses.
- Tried already: P2 exhaustion note (2026-06-11, audited_conditional three times, 2026-06-13 to 06-19). Determinant-readout bridge 2026-06-12. K/CPT supplied-context bridge 2026-07-04. Forcing pairs 2026-07-17. Log equivalence 2026-07-18.
- Same wall elsewhere: The P2/log-det open gate (`MINIMAL_AXIOMS_2026-06-29.md:180`) and observable-principle lane. Charged-lepton R-eta readout is the same kind of wall (a physical readout identified with a supplied algebraic object) but a different object.
- Why it matters: Without (ii) the mass-half theorem may address the wrong object. A phase erased from record readouts is not shown to be erased from the vacuum weight that generates CP-odd observables.
- Cheapest known test or next step: (suggested) Re-derive the k = 0 argument using only the current Record text ("readout determined by record content alone", no additivity). Either it survives with a weaker supplied premise, or the route needs a new supplier. Then attack (ii): compute whether the vacuum weight's phase enters records only through the determinant channel on the supplied Gaussian per-plaquette class.
- Severity: major
- Status: possibly misframed (reading: erasure of a record-readout phase is not the same object as the action's CP-odd phase; the lane itself flags (ii) as unsupplied)

### L11-W8: No link between the two halves of theta-bar
- Plain: Theta-bar is the sum of a gauge part and a mass part, and physics sees only the sum. The lane closes each part with a different, unrelated assumption and has no reason that ties them. The natural tie (one shared real basis for both) was tested and fails because the two operations act on different factors. Without a tie, changing either assumption reopens theta-bar.
- Precise: Target: a mechanism (joint basis, common symmetry, or anomaly-covariant assembly G4) that fixes theta_gauge + arg det M jointly. Fails: gauge OS reflection and generation conjugation-parity act on disjoint tensor factors, the pure entrywise-K constraint is not a symmetry of the tested complex-b Hermitian circulant, and the reflection-composed parity makes the tested density even. So the joint bridge does not force theta-bar = 0, and the residual is a missing holomorphic/chiral generation structure. G4 (anomaly-covariant paired shift) needs a supplier class not derived. The runner's "no CKM-to-theta leakage" check is |det V_CKM| = 1, true for every unitary matrix (checked: 1000 random unitaries all give 1.000000000000).
- Evidence:
  - `docs/STRONG_CP_JOINT_BRIDGE_FAILS_HOLOMORPHIC_RESIDUAL_2026-06-04.md:35-80,110-114`
  - `docs/THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md:77-81`
  - `docs/STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md:75-95`
  - `docs/STRONG_CP_THETA_ZERO_NOTE.md:258-278`; `scripts/frontier_strong_cp_theta_zero.py:913-933`
  - `docs/historic_intake/HISTORIC_THETA_BAR_RESIDUAL_COLLAPSES_INTO_THE_FLAVOR_CP_PHASE_NARROW_NOTE_2026_06_05_INTAKE_NOTE_2026-08-05.md:38` (extraction: "controlled smallness (theta-bar ~ 0 with an O(1) CKM phase) remains the unsolved Nelson-Barr problem")
- Axioms / supplied / proved:
  - Axioms: none of gauge action, mass operator, anomaly, or generation structure.
  - Supplied: the gauge class (W1) and the mass class (W4) separately.
  - Proved: joint-basis bridge does not force theta-bar = 0 (no-go on a finite matrix model). Also checked in scratch (C2): positive-definite Hermitian up/down mass matrices give arg det = 0 with Jarlskog J = -1.35e-2, so a CP-violating CKM phase and arg det = 0 coexist at tree level. That is why the leakage question is about loops and the weak sector, which the selected surface omits.
- Tried already: Joint-basis bridge 2026-06-04 (failed). Shared-residual lead with Koide holomorphic readout. Doublet complex structure J exists (`FLAVOR_SPLIT_THE_BRICK_DOUBLET_COMPLEX_STRUCTURE_2026-06-04.md`, positive theorem) but "does not close a strong-CP theorem".
- Same wall elsewhere: Koide holomorphic/chiral readout gate and generation identification (`STRONG_CP_JOINT_BRIDGE_FAILS_...:72-80`, "candidate shared residual class", not a proven identity). ABJ/anomaly lane for G4.
- Why it matters: Standard strong CP is exactly this: no reason the two parts cancel. The lane replaces the reason by two separate assumptions.
- Cheapest known test or next step: (suggested) Test whether the orientation swap of W2 acts on the generation circulant as the sign flip of the doublet complex structure J. If so, pure-K exists and the holomorphic residual reduces to W2. Then compute the weak-sector radiative contribution to arg det using the framework's own CKM carrier (untried; the selected surface excludes it).
- Severity: major
- Status: open

## Walls considered and rejected

- AC R-eta h-class/h-unit readout obligation (`docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md`): registered next to the theta obligation, but no theta note consumes it (the theta notes only echo it as a "same non-laundering rule" in `THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md:217`). The theta mass side rides on the occupancy part (i) only. It belongs to the charged-lepton delta-readout lane.
- Single-plaquette CP-odd slot `i theta sum Im Tr U_P`: excluded inside the class (`STRONG_CP_OPERATOR_BASIS_...2026-05-19.md:23`). The open question is the class itself (W1).
- Positive-mass sign convention: replaced by the K-real pairing (both signs give det >= 0) on the nonzero-determinant locus. The remaining hole is folded into W4.
- theta = pi branch: excluded as non-vacuous content when both parities are populated; a single-parity support makes it a vacuous alias (`THETA_GAUGE_NATIVE_POSITIVE_CLASS_...:183-190`). Solved inside the class.
- Finite-lattice winding / pi_0 route: shown vacuous (`THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_...`); folded into W3.
- CKM-phase coexistence and radiative stability: an untried check, not a stuck route. Tree-level coexistence is fine (checked). Folded into W8's next step.
- Stale runners: four theta no-go runners fail live against cached (`N5_DRAIN_REPAIR_BACKLOG_2026-08-08.md:66-68,90`), the composition-close and mass-determinant runners point at notes that moved to `archive/notes/`, and the gauge-winding runner needs an untracked `docs/audit/data/audit_ledger.json` (checked: all three fail to start). Routine repair. The science-relevant part (superseded axiom wording) is in W1 and W5.
- Neutron EDM and d_n(CKM): the framework predicts theta_eff = 0 exactly, with a downstream CKM EDM estimate that is "EFT-bridged" (`STRONG_CP_THETA_ZERO_NOTE.md:435-444`). No fitting and no tuning is involved. Not a wall.
- Axion or Peccei-Quinn route: not attempted; the lane states it makes no axion claim (`STRONG_CP_THETA_ZERO_NOTE.md:397-399`). Not a wall.
- Name collisions (theta as an angle, not strong CP): `STRONG_CYCLE_LETTERS_*`, `SIGMA_TERMINAL_THETA_CORE_EMPTY_*`, `COMPARATOR_RECOVERED_THETA_*`, `PMNS_THETA*`, `THETA13_*`, `THE_SMALL_MIXING_ANGLES_THETA_C_*`, `S3_TIME_THETA_TO_SLICE_*`, `EW_LATTICE_COS_SQ_THETA_W_*`, `SIN2THETAW_*`, `KOIDE_THETA_HIERARCHY_*`.
- `DM_STRONG_CP_GAMMA_TRANSFER_NO_GO_NOTE_2026-04-15.md`: about the dark-matter neutrino carrier gamma, not the theta-bar problem.
- Open PRs: none of the 36 open PRs concerns theta or strong CP (`gh pr list`, checked). The viability map (`origin/claude/toe-viability-probes-20260927`) does not mention strong CP; its handedness row bears on W2.

## Checks I ran (scratch: `L11_scratch/`)

- Parent runner `scripts/frontier_strong_cp_theta_zero.py`: THEOREM 13/0, COMPUTE 42/0, TOTAL 55/0.
- Companion runners passing: native positive class 8/8; determinant-readout bridge 19/19; parity orientation gate 7/7; mass-orientation pairing 18/18; native record-time split 20/20.
- Scratch numerics (`checks.py`): |det V| = 1 for 1000 random unitaries; Hermitian positive-definite M_u, M_d give arg det = 0 with J != 0; m = 0 with zero modes gives det = 0 (arg undefined); a complex-phase relative weighting stays real-positive only at theta = 0 among 720 grid angles.
- Not run or not runnable: the gauge-winding axiom-update runner needs an untracked `docs/audit/data/audit_ledger.json`; the mass-determinant and composition-close runners point at notes that moved to `archive/notes/`; the G1/G3 runners were not run. Their live failures are taken from the audit lane's own backlog (`N5_DRAIN_REPAIR_BACKLOG_2026-08-08.md`).
