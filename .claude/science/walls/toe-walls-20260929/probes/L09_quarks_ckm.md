# Lane L09: Quarks and CKM — walls

## Lane map (under 200 words, plain language first)
This lane asks whether the theory can produce the six quark masses, the CKM matrix (how quark families mix) and the phase behind quark CP violation.

Best result: the "CKM atlas". It writes the mixing numbers as the strong coupling alpha_s(v) = 0.1033 times simple fractions (lambda^2 = alpha_s/2, |V_cb| = alpha_s/sqrt6, CP phase = arctan sqrt5 = 65.9 deg). Magnitudes land within 0.1-1.3% of the repo's own comparators; the CP invariant J is 8% above the standalone comparator. Status: landed with passing runners but unaudited. Main holds zero applied audit verdicts, so "proved" below means "landed, unaudited". The repo itself calls the atlas a conditional chain "whose identifications stay supplied".

No quark mass is derived. Down-type ratios are the CKM numbers restated through two bridge formulas. Up-type ratios need a partition fixed by data. The one "retained" mass, the top, has since been reduced to a bracket of about 114-197 GeV.

Work stopped in mid-2026 (last notes July-August). The flavour/Koide program is parked. No open pull request touches this lane.

## Walls

### L09-W1: The quarks themselves (content, colour, charges, Higgs, family labels) are supplied, not derived
- Plain: The four axioms speak of a lattice, a two-state system per site, a local rule and permanent records. They say nothing about quarks, colour, electric charge, a Higgs, or which family is which. Every quark and CKM result starts from a Standard Model table put in by hand, so the lane can only say "if quarks look like this, then...". Until that table is derived, nothing in the lane is a derivation from the axioms.
- Precise: Target: derive from Lattice/Qubit/Admissibility/Record the matter content Q_L:(3,2)_{+1/3}, u_R, d_R, one Higgs doublet (n_pair=2), N_c=3 (n_quark=2N_c=6), the hypercharge assignment, and the labelled map hw=1 triplet -> {u,c,t}, {d,s,b}. Fails: (a) the staggered-Dirac realization is an open gate outside the axioms; (b) the species-labelling bijection is a proved no-go (not derivable from the minimal baseline, enters as an external convention); (c) colour is re-bounded to eight open premises, Tier-A count 0; (d) hypercharge is reduced to one undischarged constant alpha=1/3; (e) one-Higgs gauge selection holds only for an explicitly supplied carrier and charge table. Quantifier: every L09 result is of the form "given this content". Many quark notes carry an 'Admitted context inputs' line naming the staggered-Dirac gate.
- Evidence:
  - docs/MINIMAL_AXIOMS_2026-06-29.md:173-190 (open gates outside the axioms)
  - docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md:17-22, :113-115, :200 (labelling no-go)
  - docs/SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md:6-12 (supplied one-Higgs carrier and charge table)
  - docs/QUARK_LANE3_STUCK_FANOUT_SYNTHESIS_2026-04-28.md:1-6, :121-135 (admitted context inputs, staggered-Dirac target)
  - docs/LEFT_HANDED_CHARGE_MATCHING_NOTE.md:20-45 (only the 1:(-3) ratio is load-bearing; SM hypercharge identification out of scope)
  - archive/chains/july-flavor-species-era.md:17-40, :86-110 (colour: eight premises; hypercharge alpha=1/3 undischarged)
  - docs/repo/STATE_OF_THE_THEORY_2026-07-16.md:120-126
- Axioms / supplied / proved:
  - Axioms: The four axioms say nothing about fermion fields, colour, charge, a Higgs or generation labels (MINIMAL_AXIOMS list these as downstream open gates).
  - Supplied: The Standard Model matter/Higgs table, N_c=3, n_pair=2, the hypercharge constant, the labelling convention for which family is u/c/t.
  - Proved: [proved: landed, unaudited] only abstract pieces: the hw=1 orbit is the unique lightest Wilson triplet with an M_3(C) structure on the admitted staggered surface; the 1:(-3) tracelessness ratio on the (6+2) state count; the labelling no-go itself.
- Tried already: Staggered-Dirac gate synthesis 2026-06-09/10 (docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md:1-25: closes the definition, leaves labelling external). July colour campaign, six blocks (archive/chains/july-flavor-species-era.md:41-58: colour NOT derived). Hypercharge Cycle-692 no-go (same memo, :59-66: no tested mechanism derives alpha=1/3). Result each time: an exact typed boundary, no derivation.
- Same wall elsewhere: L05 (fermions and the staggered gate), L06 (colour SU(3)), L07 (Higgs, hypercharge).
- Why it matters: The theory cannot say what a quark is. All CKM and mass numbers are conditional on a table the axioms do not contain.
- Cheapest known test or next step: [suggested] Bundle every L09 input into one named premise ('SM-content') and restate each L09 result as conditional on it, with a per-input sensitivity table (which output moves if n_pair, n_color, n_quark or the hypercharge constant change). Then any lane that derives the content discharges the whole lane at once. No L09-only physics test exists.
- Severity: blocking
- Status: open

### L09-W2: No rule makes the three generations of a quark type different (no species-differentiated Yukawa/Ward law)
- Plain: The one clean quark result fixes only the top quark's coupling to the Higgs. Nothing says why up, charm, down, strange and bottom couple with such different strengths. The family symmetry allows at most two distinct values, the gauge rules leave the coupling matrices completely free, and applying the top rule to every quark gets the bottom quark's mass wrong by a factor of about 35.
- Precise: Target (Lane-3 target 3C): derive y_u/y_t, y_c/y_t, y_d/y_t, y_s/y_t, y_b/y_t, i.e. the singular values of Y_u, Y_d in M_3(C). Fails: (a) one-Higgs gauge selection leaves Y_u, Y_d arbitrary complex 3x3 (no rank, hierarchy, texture); (b) any S_3-equivariant Hermitian Ward operator on hw=1 = A_1+E lies in aI+bJ, so at most two eigenvalues (scalar if diagonal); (c) the top Ward value y_t/g_s=1/sqrt6 is a colour x isospin normalisation, species-blind; applied to every species it gives m_b ~ 145 GeV (35x too large) and m_t ~ 102 GeV; (d) CKM fixes only the relative left rotation, not singular values (arbitrary positive diagonals D_u, D_d realise any CKM); (e) the oriented C3[111] circulant splitter has three real parameters and fits any real spectrum, so it is not predictive; (f) heavy-quark 'Wilson chain' probes m=M_Pl (7/8)^(1/4) u_0 alpha_LM^n (X, Y, Z, V) all negative: 21-57% absolute errors, 5-16% best ratio errors. Quantifier: for all S_3-symmetric sources the spectrum is at most 2-valued; a symmetry-breaking source/readout is needed and none is supplied.
- Evidence:
  - docs/QUARK_GENERATION_STRATIFIED_WARD_FREE_MATRIX_NO_GO_NOTE_2026-04-28.md:70-110
  - docs/QUARK_GENERATION_EQUIVARIANT_WARD_DEGENERACY_NO_GO_NOTE_2026-04-28.md:127-135
  - docs/YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md:1-40 (35x overshoot; species-privileged BC)
  - docs/QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md:137-146
  - docs/QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md
  - docs/QUARK_C3_A1_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md:119-128
  - docs/QUARK_LANE3_STUCK_FANOUT_SYNTHESIS_2026-04-28.md:33-45, :87-99
  - docs/QUARK_LANE3_BOUNDED_COMPANION_RETENTION_FIREWALL_NOTE_2026-04-27.md:38-52
  - docs/KOIDE_X_L1_THRESHOLD_HEAVY_QUARK_WILSON_NOTE_2026-05-08_probeX_L1_threshold.md:20-24; docs/KOIDE_V_QUARK_DYNAMICAL_SSB_NOTE_2026-05-08_probeV_quark_dynamical.md:20-40 (PRs #933, #946, #958)
  - docs/CHARGED_LEPTON_DIRECT_WARD_FREE_YUKAWA_NO_GO_NOTE_2026-04-26.md (same wall, leptons)
- Axioms / supplied / proved:
  - Axioms: Nothing about Yukawa couplings; the axioms name no Hamiltonian, weight values or coupling.
  - Supplied: The top Ward normalisation as a top-channel-only statement; a hand-set bottom Yukawa in the m_t chain; generation labels.
  - Proved: [proved: landed, unaudited] the commutant algebra (S_3-equivariant Ward operators are aI+bJ), the free-matrix statement, and the 35x overshoot of the species-uniform reading. These are negative results.
- Tried already: Fourteen exact negative or boundary notes dated 2026-04-27/28 (Lane-3 blocks 01-13) plus the four Wilson-chain probes of 2026-05-08/10. Each ends at a named missing edge: 'species-differentiated non-top Ward', 'C3 coefficient source law', 'physical channel assignment'. The lane's own re-open condition is a new source/readout/symmetry-breaking theorem, not more support.
- Same wall elsewhere: L08 (CHARGED_LEPTON_DIRECT_WARD_FREE_YUKAWA_NO_GO: same free-Yukawa wall for charged leptons), L10 (neutrino Yukawa), L07 (top Yukawa normalisation).
- Why it matters: No non-top quark mass, and no Yukawa hierarchy of any kind, can be derived while this stands. It is the wall behind 'five of six quark masses are effectively pinned to PDG values' (Lane 3 note, section 1).
- Cheapest known test or next step: [reading] The axioms are covariant under proper cubic rotations, which act on the three hw=1 corners as S_3; so no law-level source can split the generations, and any splitting must come either from a new law-level primitive or from the realized state. Under the realized-state primitive's own rule, a value that changes with the realized state is registered data, not derivation output. [suggested] Cheapest decisive step: decide which it is. Test whether any state-independent (law-level) S_3-breaking term exists in the admissibility rule; if only state-contingent breaking exists, record the quark hierarchy as registered data and stop seeking a Ward law.
- Severity: blocking
- Status: open

### L09-W3: The CKM atlas's building blocks are supplied identifications, not derivations (and the six-state block is the wrong space)
- Plain: The lane's best result writes the mixing numbers as alpha_s/2, 2/3 and 1/6 and matches data to about a percent. But the rules linking the strong coupling and the counts 2 and 3 to family mixing are stated, not derived, and the notes that prove pieces of it cite each other for the inputs. The "six states" are colour-times-isospin states of one family, while mixing is between three families.
- Precise: Target: derive lambda^2=alpha_s(v)/n_pair, A^2=n_pair/n_color, r^2=rho^2+eta^2=1/n_quark, the 1+5 projector weights and the bilinear carrier K_R from the axioms, and show they define the physical CKM matrix. Fails: (i) the narrow theorems prove only algebra given (I1) lambda^2=alpha_s/n_pair and (I2) A^2=n_pair/n_color and say they do not derive them; the parent atlas 'defines' them and says each subtheorem owns its derivation, while the CP-phase subtheorem imports its inputs from the parent: [reading] a citation loop with no derivation node. (ii) K_R is a class-A definition (open_gate) with three admitted gaps: delta_A1 decoupling, aligned-bright coordinate identification, and a bridge to any physical tensor primitive. (iii) delta_A1 = 1/6, 1/42, 6/7 come from a Dirichlet lattice Green's function on a 13^3 interior with a 7-site star source (gravity-tensor machinery); why that sets quark mixing is asserted. (iv) The archived typing theorem notes that the atlas places the 1+5 split on the six states of the weak-isospin x colour block Q_L=(2,3) [reading: a per-generation gauge block], while H_u, H_d act on 3-dim generation space; no cited theorem identifies or lifts one to the other. (v) alpha_s(v)=1/(4 pi sqrt<P>) uses <P>=0.5934 as an admitted comparison number plus a declared scheme/scale identification (B4).
- Evidence:
  - docs/CKM_ATLAS_AXIOM_CLOSURE_NOTE.md:16-40, :341-352 (conditional surface; review-safe statement)
  - docs/WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_THEOREM_NOTE_2026-04-24.md:103-107 ('parent atlas defines')
  - docs/WOLFENSTEIN_LAMBDA_A_STRUCTURAL_IDENTITIES_NARROW_THEOREM_NOTE_2026-05-10.md:164-172 (does not derive I1, I2)
  - docs/CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md:23-33 (1+5 split and radius imported from parent)
  - docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md:74-90, :299 (three admitted gaps)
  - docs/TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md:15-45 (13^3 Dirichlet box)
  - archive/notes/docs/CKM_MASS_OPERATOR_PROJECTOR_OVERLAP_TYPING_THEOREM_NOTE_2026-07-12.md:234-266 (carrier-type audit)
  - docs/ALPHA_S_DERIVED_NOTE.md:52-66, :86-110 (B1, B4)
  - docs/repo/STATE_OF_THE_THEORY_2026-07-16.md:120-126; docs/repo/FRONT_DOOR_STATUS.md:35 (0 applied audit verdicts)
- Axioms / supplied / proved:
  - Axioms: Nothing about mixing, couplings or flavour structure.
  - Supplied: n_pair=2, n_color=3, n_quark=6; alpha_s(v)=0.10330 (plaquette number and scheme/scale identification); the 1+5 split and radius 1/sqrt6; the bilinear carrier K_R; the identification of the 7-site Green-function support with quark mixing.
  - Proved: [proved: landed, unaudited] exact algebra: given the supplied inputs the closed forms follow (|V_us|_0=0.22727, |V_cb|=0.04217, |V_ub|_0=0.003913, J_0=3.42e-5, delta=65.905 deg; I reproduced them [checked]).
- Tried already: The atlas and about 20 subtheorems (magnitudes, rows, barred triangle, Jarlskog NLO, Thales, Brocard, number-theory characterisations). NP-CKM no-go (docs/NEWPHYSICS_NP_CKM_WOLFENSTEIN_NOTE_2026-05-10_npCKM.md:30-36; it tests the P-Heavy-A primitive of PR #1044): the circulant Koide primitive forces CKM = permutation matrix. Mass-basis NNI/Schur (docs/CKM_SCHUR_COMPLEMENT_THEOREM.md) is algebra only. None derives I1/I2.
- Same wall elsewhere: L06 and L16 (alpha_s(v), beta=6, <P>), L07 (n_pair=2 from the Higgs doublet), L14 (the 7-site tensor-support machinery is reused from the gravity lane).
- Why it matters: The only positive quantitative quark result is conditional on unproved identifications; the TOE cannot yet call any mixing angle a prediction.
- Cheapest known test or next step: [suggested] (1) Recompute the CKM moduli from the generation-space overlap Tr(P_i^u P_j^d) with the 1+5 split imposed on the 3-dim generation space, not the 6-dim gauge block; if the numbers change, the atlas depends on the category conflation. (2) Forward tests that were not used to pick the identifications: gamma (=delta) and the B_s mixing phase phi_s = -alpha_s sqrt5/6 = -0.0385 rad [checked arithmetic].
- Severity: major
- Status: priced

### L09-W4: Where the quark CP phase comes from, and why it is arctan sqrt5
- Plain: Quark CP violation hangs on one phase. The lane gets 65.9 degrees by saying one state out of six is special ("1 plus 5"). Other equally natural splits, 2+4 and 3+3, give 54.7 and 45 degrees. The count of six and the split are put in by hand. The older route instead solves for complex numbers so as to match data.
- Precise: Target: derive delta_CKM (cos^2 delta = 1/n_quark or an equivalent selector), and why the quark sector has a non-zero CP phase at all, from the axioms. Fails: the reduction is exact but conditional: cos^2 delta = w_sym = 1/n only after supplying n_quark=6, the CP-even/CP-odd channel assignment and the 1+5 split; radius cancels. The inverse-square count identity (eta^2 = 1/N_pair^2 - 1/N_color^2) is an exact re-encoding of the same (rho, eta), not an independent selector; K_R's physical meaning is asserted. Mass-basis route: the complex 1-3 carriers xi_u, xi_d are solved numerically against imported targets (Class G, 'numerical match'), are non-perturbative relative to the Schur base, small-correction reading closed negatively; the minimal Schur-NNI carrier leaves the Jarlskog area far below the atlas; arg det(M_u M_d)=0 is imposed by hand. Only the inter-sector Jarlskog is physical (per-sector orientation is gauge).
- Evidence:
  - docs/CKM_CP_PHASE_ARCTAN_SQRT5_BRIDGE_REDUCTION_OPEN_GATE_NOTE_2026-06-08.md:19-62
  - docs/CKM_CP_PHASE_STRUCTURAL_IDENTITY_THEOREM_NOTE_2026-04-24.md:82-110
  - docs/QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md:3-31 (existence-of-fit; Class G)
  - docs/QUARK_CP_SMALL_CORRECTION_BOUNDARY_NOTE_2026-06-17.md:14-22
  - docs/QUARK_CP_CARRIER_SLOT_MINIMALITY_THEOREM_NOTE_2026-06-17.md
  - docs/QUARK_MASS_RATIO_NOTE_2026-04-18.md:36-40
  - docs/FLAVOR_PER_SECTOR_ORIENTATION_IS_GAUGE_CP_IS_INTER_SECTOR_NARROW_THEOREM_NOTE_2026-06-08.md:19-31
- Axioms / supplied / proved:
  - Axioms: Nothing about complex phases of Yukawa matrices or CP.
  - Supplied: n_quark=6; the 1+5 channel split; CP radius 1/sqrt6; carrier phases in the mass-basis route; arg det(M_u M_d)=0.
  - Proved: [proved: landed, unaudited] the reduction cos^2 delta = 1/n given w_sym=1/n; the slot minimality (the 1-3 edge is the unique off-tree slot under fixed Schur-NNI/Hermitian assumptions). [checked] alternatives: 1+5 -> 65.905 deg, 2+4 -> 54.736 deg, 3+3 -> 45 deg.
- Tried already: Open-gate reduction 2026-06-08 (exhibits the residual, no derivation); complex-carrier completion 2026-04-18 (fit); projector-ray phase completion (docs/QUARK_PROJECTOR_RAY_PHASE_COMPLETION_NOTE_2026-04-18.md, bounded); small-correction boundary 2026-06-17 (negative).
- Same wall elsewhere: L11 (theta-bar and arg det M_q), L13 (CP violation is an input to baryogenesis), L10 (the PMNS delta_CP selector problem, ABCC sheet choice) [reading].
- Why it matters: The theory cannot say why quarks and antiquarks differ, or by how much.
- Cheapest known test or next step: [suggested] Forward test: the atlas gives gamma = arctan sqrt5 = 65.905 deg at leading order and 'protected' at NLO; the 2+4 alternative gives 54.7 deg. A gamma measurement at about 1 deg (LHCb/Belle II; current world averages are about 3 deg from my recollection, not re-checked) separates them. No cheaper derivation test is known.
- Severity: major
- Status: open

### L09-W5: Down-quark route: the 5/6 exponent, the GST relation and the choice of energy scale
- Plain: The lane predicts down-type mass ratios from the mixing numbers with two bridge formulas: |V_us|^2 = m_d/m_s and |V_cb| = (m_s/m_b)^(5/6). So these are the mixing predictions restated, not independent. The exponent 5/6 was the only one of nine group-theory candidates within 10% of the comparator, and only when the two masses are quoted at different energies; at one common energy it is 14% off.
- Precise: Target: derive V_cb = (m_s/m_b)^(C_F - T_F) and V_us^2 = m_d/m_s non-perturbatively at lattice strong coupling g=1, plus the scale rule. Fails: (i) 5/6 was found by a discriminator scan against the threshold-local comparator m_s(2 GeV)/m_b(m_b): +0.202% there, but +14.0% on the common-scale surface (one-loop transport factor 1.138 [checked]); the exponent implied by the atlas |V_cb| is 0.833 on the first surface and 0.805 on the second. (ii) The archived July work reduces the bridge to one invariant equation Tr(P_c^u P_b^d) = (m_s/m_b)^(5/3); fixed simple spectra leave the overlap free on [0,1] even on the Z_2 normal form; a determinant-neutral composite forces it only after a carrier, lift and block-weight dictionary are supplied. (iii) The down-only equivariant route is refuted. (iv) GST is a structural NNI bridge, not derived. (v) The mass ratios are predicted only by inverting the atlas |V_us|, |V_cb| through the two bridges; the 'independent path agreement' (path A vs path B) is an algebraic identity, not a second test [reading].
- Evidence:
  - docs/QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28.md:110-140 (scale wall, +15%)
  - archive/notes/docs/CKM_FIVE_SIXTHS_EXPONENT_DISCRIMINATOR_SUPPORT_NOTE_2026-07-02.md:44-80
  - archive/notes/docs/CKM_MASS_OPERATOR_PROJECTOR_OVERLAP_TYPING_THEOREM_NOTE_2026-07-12.md:30-51, :234-266
  - archive/notes/docs/CKM_COMPOSITE_POSITIVE_VOLUME_ALIGNMENT_SOURCE_ACTION_BOUNDARY_NOTE_2026-07-12.md:28-60
  - docs/QUARK_MASS_RATIOS_TASTE_STAIRCASE_SUPPORT_NOTE_2026-04-25.md:60-100, :207-220, :257-290
  - docs/DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md; docs/CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md; docs/CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md
  - docs/CKM_FROM_MASS_HIERARCHY_NOTE.md:19-25 (runner hard-codes PDG masses and bands)
  - archive/chains/july-flavor-species-era.md:33-40
- Axioms / supplied / proved:
  - Axioms: Nothing about exponents, running, or a preferred energy scale beyond the scale-reference primitive (units only).
  - Supplied: GST as an NNI structural bridge; the exponent C_F-T_F=5/6 at g=1; the 'threshold-local' scale convention; the lifts and dictionaries in the composite construction.
  - Proved: [proved: landed, unaudited] exact SU(3) arithmetic C_F-T_F=5/6; the projector-overlap typing |V_ij|^2 = Tr(P_i^u P_j^d); fixed-spectrum freedom of the overlap. [checked] the 9-exponent discriminator table and the +14.0% common-scale mismatch.
- Tried already: Down-type CKM-dual note (2026-04-17), taste-staircase support (2026-04-25), scale-selection boundary (2026-04-28), exponent discriminator (2026-07-02), overlap typing and composite constructions (2026-07-12). Each narrows or restates; none derives the exponent or the scale.
- Same wall elsewhere: L06 (strong-coupling g=1 exponentiation, non-perturbative QCD), L16 (scale selection).
- Why it matters: The lane's down-type 'mass predictions' are the CKM atlas inverted through two unproved bridges, so they add no independent support to the atlas and give no absolute mass.
- Cheapest known test or next step: [checked] common-scale test already run: +14.0% (and the natural exponent there is near 0.80, closest small rational 4/5, not 5/6). [suggested] Repeat the discriminator on a renormalisation-group-invariant mass ratio; if 5/6 is not singled out there, retire the bridge as a scale-convention coincidence.
- Severity: major
- Status: possibly misframed

### L09-W6: Up-quark route: the amplitude law, the up/down partition, and a 10x mismatch in m_c/m_t
- Plain: Each mixing number is the sum of an up-quark and a down-quark part. The lane gives almost all of the 2-3 mixing to the down quarks, which leaves so little for the up sector that the charm-to-top ratio comes out about ten times too small. A free "partition" repairs it, and one amplitude is chosen from a shortlist because it fits. No rule turns that amplitude into a mass.
- Precise: Target: derive m_u/m_c and m_c/m_t (two ratios) from the framework. Fails: (i) Phase-2 ansatz |V_cb|^2 = (m_s/m_b)^(5/3) + (m_c/m_t)^(5/3): with the observed m_s/m_b the down part already equals 99.7% of alpha_s^2/6, leaving an implied m_c/m_t = 7.3e-4 against 7.3e-3 observed (10x low); using both observed ratios the sum overshoots |V_cb|^2 by 15% [checked]. (ii) The partition (f_12, f_23) is free; the down-dominant edge sets the up ratios to zero. (iii) The reduced amplitude a_u is one scalar: shortlist 7/9, sqrt(3/5), atan sqrt5 - sqrt5/6, sqrt(5/6)(1-1/sqrt42) (all 'external empirical' or fit-anchored; 465 one-step and 20,934 two-step exact denominators; 212 two-step denominators beat sqrt7, 17 after simplification); the RPSR value a_u = sqrt(5/6)(1-48/(49 sqrt42)) = 0.77489 is a sum-rule with a 'unique minimal three-atom contraction', not a mass; the solved value is 0.7783 (0.4% away). (iv) RPSR does not fix two ratios: a continuum of ordered pairs is admissible; RPSR + C3 circulant is rank-deficient. (v) It rests on the scalar-comparison ray rho=1/sqrt42 that the atlas note itself says is not the leading 1->3 amplitude (rho=1/6).
- Evidence:
  - docs/UP_TYPE_MASS_RATIO_CKM_INVERSION_NOTE.md:14-35 (partition free; edge sets up ratios to zero)
  - docs/QUARK_MASS_RATIO_NOTE_2026-04-18.md:33-40, :57-72
  - docs/QUARK_PROJECTOR_PARAMETER_AUDIT_NOTE_2026-04-19.md:45-70
  - docs/QUARK_UP_AMPLITUDE_PROVENANCE_AUDIT_NOTE_2026-04-19.md:20-70
  - docs/QUARK_UP_AMPLITUDE_TENSOR_ENDPOINT_RESOLUTION_NOTE_2026-04-19.md:80-110
  - docs/QUARK_UP_AMPLITUDE_RPSR_CONDITIONAL_THEOREM_NOTE_2026-04-19.md:35-70, :150
  - docs/QUARK_UP_AMPLITUDE_RPSR_MASS_RETENTION_BOUNDARY_NOTE_2026-04-28.md:79-125
  - docs/QUARK_RPSR_SINGLE_SCALAR_READOUT_UNDERDETERMINATION_NOTE_2026-04-28.md:107-118
  - docs/QUARK_RPSR_C3_JOINT_READOUT_RANK_BOUNDARY_NOTE_2026-04-28.md:122-130
  - docs/CKM_ATLAS_AXIOM_CLOSURE_NOTE.md:163-176 (scalar comparison ray is not the leading amplitude)
- Axioms / supplied / proved:
  - Axioms: Nothing.
  - Supplied: The parallel-bridge + CP-orthogonal ansatz; the partition; the choice of a_u from a shortlist; the sector amplitude-to-Yukawa readout.
  - Proved: [proved: landed, unaudited] LO/NLO RPSR algebra given the projector ray; the exact endpoint-denominator class {6,7,sqrt6,sqrt7}; the mass-retention boundary (a_u is not a mass ratio).
- Tried already: Candidate scan, native-expression scan, native-affine no-go, two-step scan, scalar-comparison bridge, sqrt7 counterexample, provenance audit, RPSR, RPSR+C3 rank boundary, partition revisit (all 2026-04-19 to 04-28). Result: a shortlist and a boundary; no unique law.
- Same wall elsewhere: none found beyond the shared Yukawa wall (L09-W2).
- Why it matters: Up-type masses (and with them the light-quark masses that hadron physics needs) have no path.
- Cheapest known test or next step: [checked] the 10x and 15% arithmetic (scratch: L09_scratch/checks.py). [suggested] State the missing typed edge explicitly (amplitude a_u -> Yukawa eigenvalue ratios) and test one prediction it makes that was not used in the fit, for example the implied m_u/m_c at a common scale.
- Severity: major
- Status: open

### L09-W7: The Route-2 E-center readout (target triple -1, -2, 21/4): about 110 notes, no derivation, and the match may be a box-size artifact
- Plain: To fix the up-quark amplitude the lane tried to compute three ratios from how a small 3D lattice box responds to a point source. At one box size (15) they come out near -1, -2 and 5.25. At every other size they are wildly different. About 110 notes have tried to derive the third number; all end in "cannot be derived from what we have".
- Precise: Target: derive the readout-map triple (beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) = (-1, -2, 21/4), equivalently the E-center endpoint ratio q_E=15/8 or c_TE=-8/9. Fails: the triple is not derived; T-side values are supplied premises (ENDPOINT-RT, SHELL-MULT); rho_E is free under minimal naturality, blind to E-center constraints, has no typed source-domain bridge (R_conn=8/9 -> -R_conn), no source-excess primitive (needs b_E/a_E=7/2), no readout-only inverse-square coefficient law (9/4 available, coefficient bridge missing). The observable is a max-abs envelope of the trace-free Einstein tensor at three probe points (finite differences h=0.04), not an eigenvalue. Ladder over box size N: q_T = 0.902, 0.870, 0.83333, -0.197, -0.812, -1.316 (N=11..21); rho_E = -0.92, -6.2, +5.257, -41, -51, -58: matches only at N=15; the note's own verdict is TAIL_NOT_CONVERGENT. The exact T-side value is |b_T/a_T| = 1.0000308..., not a recognised low-degree number. [checked] I re-ran the ladder (reproduced) and two smooth replacements (fixed-component and Frobenius norm at the first probe): identical at N=15 by construction, but at N=17,19,21 q_T = 1.49, 1.03, 0.995, s_TE = 0.12, 0.49, 0.64 and rho_E = 2.0, 1.4, 1.2: no approach to (5/6, -2, 21/4) (three sizes only, so this is not an infinite-volume limit). A Frobenius sum over the three probes misses the triple at every size (N=15: q_T=0.897, s_TE=-14.8).
- Evidence:
  - docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md:124-150 (open_gate parent)
  - docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md:24-37, :92-110
  - docs/QUARK_ROUTE2_HONEST_GRAVITY_METRIC_RHOE_CHARACTERIZATION_NOTE_2026-07-02.md:56-125, :139 (ladder; geometry-pinned; TAIL_NOT_CONVERGENT)
  - docs/QUARK_ROUTE2_RHOE_FLOOR_FAMILY_SIZE_PARAMETRIZED_LADDER_NOTE_2026-07-02.md:60-90
  - docs/QUARK_ROUTE2_ETA_FLOOR_HF_BOUNDARY_NOTE.md:14-40 (nonspectral max-entry envelope)
  - docs/QUARK_ROUTE2_T_BALANCE_EXACT_ALGEBRAIC_VALUE_BOUNDED_NOTE_2026-06-12.md:20-35
  - docs/QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md:241-262
  - docs/QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md:72-110
  - docs/QUARK_ROUTE2_SOURCE_EXCESS_BANK_GAP_NO_GO_NOTE_2026-06-21.md:71-95
  - docs/QUARK_ROUTE2_READOUT_INVERSE_SQUARE_GATE_NO_GO_NOTE_2026-06-21.md:61-90
  - docs/QUARK_ROUTE2_SINGLE_ADJOINT_LINE_CURRENT_BANK_NO_GO_NOTE_2026-06-21.md
  - docs/QUARK_ENDPOINT_RATIO_CHAIN_LAW_NOTE_2026-04-19.md:51-70 (supplied premises)
  - L09_scratch/rhoE_ladder_run.txt; L09_scratch/rhoE_smooth_variants.py; L09_scratch/rhoE_smooth_variants_out.txt
- Axioms / supplied / proved:
  - Axioms: Nothing about a quark readout, a tensor response or a finite Dirichlet box.
  - Supplied: The T-side values -1 and -2; the fixed probe radius 4.25, envelope width 0.9, stencil h=0.04, EPS=0.005; the identification of a gravity-tensor box response with a quark up-sector amplitude.
  - Proved: [proved: landed, unaudited] the exact endpoint algebra, the carrier columns, delta_A1(e0)=1/6 (size-independent), and about 40 exact negative statements. The number 21/4 itself is not proved.
- Tried already: 28 notes in docs/ (2026-04-19 to 07-02) and 82 archived notes (archive/notes/docs/QUARK_ROUTE2_*, mostly 2026-06-10 to 06-21) plus 18 S3_TIME_* notes: E-center lift attempts, Hessian bridge, log-barrier, seven-eighths import, single adjoint line (also a 2026-09-19 probe-worker note, memory file probes-worker-campaign-20260918.md:149: chain exact, no fire), current/source dualisation, density-square, inverse-square. All end in the same boundary.
- Same wall elsewhere: none (L14 shares only the borrowed tensor/Regge machinery).
- Why it matters: It blocks the tensor route to the up-type scalar law (W6); it also shows a headline quark 'endpoint' number can be a finite-box coincidence.
- Cheapest known test or next step: [checked] smooth-functional test above: it does not converge to the triple. Decisive next step [suggested]: compute the readout in the infinite-volume limit with a fixed physical probe (Dirichlet wall far away) using a functional that is smooth in the source; if no rational triple emerges, retire Route 2 and the (-1,-2,21/4) target.
- Severity: major
- Status: possibly misframed

### L09-W8: The absolute-mass anchor: the top mass is no longer controlled, and there is no second anchor
- Plain: Ratios among quarks need one absolute mass to become masses. The lane's anchor was the top quark, quoted at 172.57 GeV within 0.07%, from a Planck-scale rule run down to the weak scale. A June 2026 correction found the lattice-to-continuum step was miscounted; that step is uncertain by about 50%, so the top mass is only bracketed at roughly 114-197 GeV. The bottom Yukawa was also set by hand.
- Precise: Target: an absolute quark-mass scale from the axioms plus the scale-reference primitive (units). Fails: (i) the exact lattice Ward value y_t(M_Pl)/g_s(M_Pl)=1/sqrt6 stands, but the matching Delta_R that carried it to 172.57 GeV was reported as -3.27% and is corrected to +49..+54%: the scalar C_F channel double-counted a /N_TASTE division and the fermion channel is log-divergent at all 16 doublers (only k=0 subtracted); it lies outside the framework's own 7.41% bound by 7-10x; m_t(pole) in ~[114, 197] GeV. (ii) The m_t chain uses a species-privileged boundary condition: y_t at the Ward value while y_b is held at its observed small value. (iii) The generic quasi-fixed-point attractor route caps m_t near 197-218 GeV but does not pin it. (iv) Ratios chain to absolute masses only if W2 and W5/W6 close.
- Evidence:
  - docs/YT_P1_DELTA_R_FERMION_REGULATOR_DEPENDENCE_AND_SCALAR_NTASTE_RESOLUTION_NOTE_2026-06-16.md:1-12, :91-136
  - docs/YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md:29-40, :84, :119 (species-privileged BC)
  - docs/QUARK_TOP_QFP_ATTRACTOR_ROUTE_NO_GO_NOTE_2026-05-10.md:1-30
  - docs/lanes/open_science/03_QUARK_MASS_RETENTION_OPEN_LANE_2026-04-26.md:54-58, :129-137 (older 'retained m_t' claim)
  - docs/QUARK_LANE3_BOUNDED_COMPANION_RETENTION_FIREWALL_NOTE_2026-04-27.md:97-108
- Axioms / supplied / proved:
  - Axioms: Nothing beyond units: the scale-reference primitive supplies a ruler, no dimensionless content.
  - Supplied: The Planck-scale boundary condition y_t/g_s=1/sqrt6 as a physical top-channel statement; the lattice-to-MSbar matching; the observed y_b.
  - Proved: [proved: landed, unaudited] the lattice-scale Ward identity (untouched by the correction) and the correction note's own numbers. The correction note (itself an unaudited source-note proposal) states that the 172.57 GeV precision claim is invalidated.
- Tried already: P1 / Delta_R chain (April) corrected 2026-06-16; QFP attractor scan 2026-05-10 (negative); Wilson-chain absolute masses (negative, PR #933).
- Same wall elsewhere: L07 (top Yukawa, Higgs mass, hierarchy), L16 (dimensionless constants; scale).
- Why it matters: Even a perfect set of mass ratios would give no masses. The lane's older statement 'the top mass is retained' no longer holds at its quoted precision.
- Cheapest known test or next step: [suggested] Redo the fermion-channel matching with all 16 doublers subtracted or an improved (smeared) staggered action, and report m_t as a bracket; or drop the retained label for m_t in the lane notes.
- Severity: blocking
- Status: open

### L09-W9: No native definition of a quark mass, and the lepton 'dial' does not transfer
- Plain: A quark's mass depends on the energy scale and scheme at which it is quoted, and light quarks are confined, so "the mass of the up quark" needs a definition the theory lacks. The dial that works (partly) for charged leptons, set to a special value, reads about 0.62 for down and 0.83 for up quarks versus 0.5 for leptons, and no rule sources that spread.
- Precise: Target: a scheme/scale-native quark mass definition and the quark-sector Brannen dial (amplitude ratio r=|b|^2/a^2 and phase). Fails: the open gate states the live blocker as 'sector-specific quark mass scheme/scale and quark dial theorem'. Comparators were mixed-convention (pole top with MSbar others, unequal scales); corrected common-scale dials are r_up = 0.831 +/- 0.002 and r_down = 0.621 +/- 0.008 (was 0.774, 0.597), against r=1/2 for charged leptons. Colour-representation functions give at most a colourless/coloured 2-class partition, so they cannot separate up from down; a common scalar rescaling cancels in r; the abelian charge channel is 'open' but would be a fit (ordering e<d<u is not monotone in |Q|). The quark BAE analog on the 6-dim host has the same (1,2) isotype ratio, barred at kappa=1 not 2. [checked] Numerology trial factor: 47 rationals with denominator <=12; 5/8 lies within 1 sigma of r_down and 5/6 within 2 sigma of r_up, but a random target has such a rational within 1 sigma with probability 0.63 (r_down) and 0.20 (r_up): no evidence.
- Evidence:
  - docs/QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26.md:39-49, :76-101
  - docs/SECTOR_DIAL_COMMON_SCALE_COMPARATOR_CORRECTION_META_NOTE_2026-08-07.md:46-53
  - docs/FLAVOR_GAUGE_REPRESENTATION_CHANNEL_CANNOT_SOURCE_THE_SECTOR_R_SPREAD_NARROW_NO_GO_NOTE_2026-06-15.md:27-60
  - docs/QUARK_BAE_ANALOG_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_quarkBAE.md
  - docs/repo/DEFERRED_DECISIONS.md:143-175 (sigma-reality bit: Q=1 premise-free vs Q=2/3; flavor/Koide parked)
  - L09_scratch/dial_trial.py
- Axioms / supplied / proved:
  - Axioms: Nothing about mass definitions or schemes.
  - Supplied: A scheme/scale for each quark mass; the sector dial values (registered data).
  - Proved: [proved: landed, unaudited] the C_3 circulant coordinate algebra (Q = (1+2r)/3) and the no-transfer discipline; the two non-abelian-channel counting arguments.
- Tried already: Quark-Koide open gate 2026-05-26/06-12; sector-spread no-go 2026-06-15; BAE analog 2026-05-10; comparator correction 2026-08-07. The Koide/flavor tail was stopped by the owner and parked.
- Same wall elsewhere: L08 (charged-lepton Koide dial r=1/2 and the AC_phi_lambda residual), L16.
- Why it matters: Without a mass definition no derived number can be compared with a measured quark mass except through a convention choice; the choice moves m_s/m_b by about 14% and r_up by 0.06.
- Cheapest known test or next step: [suggested] First fix a framework-native mass definition (for example a pole-like or RG-invariant mass) so comparators are unambiguous; then test whether any single rule assigns (r_lep, r_down, r_up) = (1/2, 0.62, 0.83) from electroweak charges without per-sector fits. The rational-trial check above says a match alone would not count.
- Severity: major
- Status: open

### L09-W10: Two flavour mechanisms that do not meet: the circulant (leptons) and the tensor/Schur atlas (quarks); small CKM vs large PMNS is a supplied contrast
- Plain: The lepton side uses a three-family cyclic structure. If quarks use the same structure, up and down sectors are diagonalised by the same matrix and there is no mixing at all. So the CKM atlas uses a different mechanism, and nothing says why quarks and leptons use different ones, or why quark mixing is small and neutrino mixing large.
- Precise: Target: one flavour carrier that yields lepton masses, quark masses, small CKM and large PMNS. Fails: on the sector-dependent circulant primitive, [H_up, H_dn]=0 for every parameter choice, so V_CKM is a permutation matrix and lambda, A, J are in {0,1} (NP-CKM no-go); the atlas uses a different carrier (7-site tensor support, Schur cascade, 1+5) and no theorem relates the two; the 'small CKM vs large PMNS' note is a conditional linear-algebra observation on supplied hypotheses (quark bases aligned, neutrino operator circulant) and assigns no physical role to either basis; the CKM/NNI atlas tools do not transfer to the neutrino sector (no-go); the generation labelling is external (W1).
- Evidence:
  - docs/NEWPHYSICS_NP_CKM_WOLFENSTEIN_NOTE_2026-05-10_npCKM.md:25-45, :78-90
  - docs/CKM_SMALL_VS_PMNS_LARGE_FROM_RECORD_READOUT_CONTEXT_NARROW_THEOREM_NOTE_2026-06-06.md:14-35, :62-72
  - docs/DM_NEUTRINO_CKM_TEXTURE_TRANSFER_NO_GO_NOTE_2026-04-15.md:1-12
  - docs/HUBBLE_LANE5_C2_CKM_PMNS_RIGHT_SENSITIVE_SELECTOR_STRETCH_NOTE_2026-04-29.md:1-8
  - docs/OPEN_KOIDE_FLAVOR_CLUSTER_CONSOLIDATION_MAP_2026-06-02.md:26-45, :75-85 (lepton cluster: one operator, one residual)
  - docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md:56-60 (CKM/PMNS alignment not supplied)
- Axioms / supplied / proved:
  - Axioms: Nothing about how flavour operators of different sectors relate.
  - Supplied: A relative alignment of the quark bases (small rotation) and a circulant neutrino operator; the sector-to-carrier map.
  - Proved: [proved: landed, unaudited] the commuting-circulant obstruction (CKM = permutation) and the aligned-basis linear algebra.
- Tried already: NP-CKM no-go 2026-05-10; small-vs-large observation 2026-06-06; neutrino texture-transfer no-go 2026-04-15; Hubble lane C2 selector stretch 2026-04-29.
- Same wall elsewhere: L08 (circulant Koide operator), L10 (PMNS mixing, neutrino sector).
- Why it matters: The TOE has two unconnected flavour mechanisms; unification of quark and lepton flavour cannot be claimed.
- Cheapest known test or next step: [suggested] The NP-CKM proof shows the obstruction is commutation. Cheapest probe: exhibit the smallest Hermitian extension of the circulant family that makes H_up and H_dn non-commuting, and ask which framework structure could source it with a derived coefficient. If none can, the two mechanisms stay separate and the lane should say so.
- Severity: major
- Status: open

### L09-W11: Registered obligation: does the quark determinant carrier equal the charged-lepton K/CPT carrier, forcing arg det M_q = 0?
- Plain: The strong-CP angle needs the overall phase of the quark mass matrix to vanish. The theory can show this only if the quark's determinant readout is the same physical channel as one already studied for charged leptons. That identification is registered as an open derivation obligation. Meanwhile the quark CP fits simply impose that the phase is zero.
- Precise: Target: construct the quark mass/determinant carrier, identify its physical readout, and prove the cross-sector correspondence with the charged-lepton K/CPT occupancy carrier, so that arg det(M_q)=0 follows without importing it. Fails: charged-lepton statistical-grain closure alone does not establish the identity; algebraic similarity is insufficient by the note's own closure criterion; the historical owner adoption of the occupancy statement was withdrawn as a supplied-premise channel (2026-07-04). The quark CP completions (W4) impose arg det(M_u M_d)=0 mod 2pi as a constraint.
- Evidence:
  - docs/THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md:9-35
  - docs/audit/data/derivation_obligations.json (theta_quark_determinant_cross_sector_readout_derivation_obligation, status open_gate)
  - docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md:33-40, :56-80
  - docs/KEY_SCIENCE.md:32-38
  - docs/MINIMAL_AXIOMS_2026-06-29.md:175-180 ('strong-CP theta gauge and mass-side derivation obligations')
  - docs/STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md
- Axioms / supplied / proved:
  - Axioms: Nothing about mass determinants or theta.
  - Supplied: arg det(M_u M_d) = 0 is imposed in the CP fits; the cross-sector identification is an open obligation (zero premise weight), not a supplied premise.
  - Proved: none for the cross-sector identity. The mass-orientation zero-branch statement on the K-real surface is landed, unaudited (docs/THETA_MASS_ORIENTATION_ZERO_BRANCH_PAIRING_FORCED_ON_K_REAL_SURFACE_NARROW_THEOREM_NOTE_2026-07-01.md).
- Tried already: Determinant readout bridge (2026-06-12), mass-side composition (2026-07-03), axiom-update no-go (2026-07-04); the obligation carries zero premise weight and self-liquidates on a retained derivation.
- Same wall elsewhere: L11 (strong CP and theta), L08 (charged-lepton K/CPT occupancy grain).
- Why it matters: Without it, theta-bar = 0 and the quark CP phase story are conditional on two open obligations.
- Cheapest known test or next step: [suggested] The obligation's own closure criterion: build the quark determinant carrier explicitly and check it equals the K/CPT orbit occupancy; no cheaper test is known. L11 owns this wall; it is logged here because the quark CP fits use it.
- Severity: major
- Status: open

### L09-W12: Leading-order numerics: comparator choice and imported scheme decide how well the atlas 'fits'
- Plain: The CKM atlas matches the data to about 1%, but it is a leading-order formula with an imported coupling. The comparator for the CP invariant J differs by 7% depending on how it is built, and |V_us| comes out 1.3% high. Without a derived scale and scheme for the coupling, higher-order corrections can be neither computed nor used to score the prediction.
- Precise: Target: an atlas whose higher-order corrections are derived, so agreement can be scored. Fails: atlas-leading |V_us|=0.22727 is +1.32% against the repo's comparator 0.2243 [checked]; J=3.33e-5 (finite lambda; leading J_0=3.42e-5) is +8% (+11%) over the standalone comparator 3.08e-5 but +0.8% over an angle-reconstructed 3.30e-5: 'there is a real observation-side split'; |V_cb|=0.04217 is compared with the 0.0422 comparator; the finite-lambda and NLO barred-triangle forms are 'guarded parent-atlas calculations'. lambda^2 = alpha_s/2 depends on alpha_s(v) at the scale v: the scheme/scale identification (B4) and <P>=0.5934 are declared inputs, and beta=6 is a named import. Sensitivity: d ln|V_us| / d ln alpha_s = 1/2, so a 2% shift in alpha_s(v) moves |V_us| by 1%.
- Evidence:
  - docs/CKM_ATLAS_AXIOM_CLOSURE_NOTE.md:260-306 (numerical read; observation comparator split)
  - docs/QUARK_MASS_RATIOS_TASTE_STAIRCASE_SUPPORT_NOTE_2026-04-25.md:150-165 (deviation table)
  - docs/ALPHA_S_DERIVED_NOTE.md:52-66, :86-110
  - docs/repo/STATE_OF_THE_THEORY_2026-07-16.md:157-160 (beta=6 is an import; postdictions)
  - L09_scratch/checks.py
- Axioms / supplied / proved:
  - Axioms: Nothing.
  - Supplied: alpha_s(v) scheme/scale (B4); <P>=0.5934; comparator packages.
  - Proved: [proved: landed, unaudited] the leading-order closed forms; [checked] my recomputation of all headline numbers.
- Tried already: Comparator-split paragraph in the atlas note (2026-04-15); boundary-input declaration in the alpha_s note (2026-06-10).
- Same wall elsewhere: L06 and L16 (alpha_s(v), beta=6).
- Why it matters: The strongest-looking quark result cannot yet be scored as a prediction versus a postdiction.
- Cheapest known test or next step: [suggested] Derive the alpha_s(v) scale/scheme identification (L06/L16), then compute the first correction to |V_us| and J; the sign and size of that correction is the test.
- Severity: minor
- Status: priced

## Walls considered and rejected
- ABCC / DM_ABCC_* (PMNS sheet selection and CP-phase exclusion): neutrino and dark-matter sector (L10, L12), not quarks; the T2K-based exclusion is conditional support there.
- FLAVOR_* value campaign (r=1/2, Q=2/3, delta=2/9, chirality gate, AC_phi_lambda): charged-lepton Koide, owned by L08; the quark-side consequences are logged in W9 and W10.
- Strong-CP gauge-side theta notes (STRONG_CP_*, THETA_GAUGE_*): L11; only the quark-determinant obligation is logged here (W11).
- CKM closed-form corollaries (barred-triangle Brocard/Napoleon/Pedoe/orthocenter forms, Vieta integers, Egyptian-Bernoulli closures, number-theory characterisations, Thales ratios): exact algebra on the supplied atlas; inherit W3/W4 and add no independent wall. The open-gate note says the inverse-square count identity is a re-encoding, not a selector.
- N_gen = N_color = 3 cross-sector 'closure' (docs/CKM_KOIDE_CROSS_SECTOR_Z3_CLOSURE_THEOREM_NOTE_2026-04-25.md): equality of two imported values; not a derivation and not a separate wall.
- Cross-sector Koide-V_cb bridge (Q_l alpha_s^2 = 4|V_cb|^2, docs/CROSS_SECTOR_A_SQUARED_KOIDE_VCB_BRIDGE_SUPPORT_NOTE_2026-04-25.md): conditional corollary; meaningful only if L08 closes Q_l=2/3.
- CKM moduli-only Jarlskog area certificate: a pure 3x3 unitarity identity; solved (docs/CKM_MODULI_ONLY_UNITARITY_JARLSKOG_AREA_CERTIFICATE_THEOREM_NOTE_2026-04-26.md).
- Hadron masses (m_p, pion via GMOR needing m_u+m_d): a consumer of W2/W5/W6/W9, not an L09 wall.
- Heavy-quark expansions and quark-mass running at all scales: excluded from the lane's own scope (docs/lanes/open_science/03_QUARK_MASS_RETENTION_OPEN_LANE_2026-04-26.md:176-183).
- Neutron EDM bound from the CKM phase (docs/CKM_NEUTRON_EDM_BOUND_NOTE.md): a prediction, not a wall.
- Top quasi-fixed-point attractor no-go: route foreclosure, folded into W8.
- All 5,299 ledger rows unaudited (docs/repo/FRONT_DOOR_STATUS.md:35): audit bookkeeping, not a physics wall; it only limits how strongly 'proved' can be read.
- CKM_FROM_MASS_HIERARCHY (GST/hierarchy reading): its own note lists the upstream bands and texture as conditional authorities; folded into W5.
- QUARK_JTS_* / QUARK_ISSR1_BICAC_* 'closed theorem' packets (2026-04-19): steps inside the RPSR chain; inherit W6.
- Exact endpoint algebra, projector-overlap typing, RPSR algebra, S_3 commutant: solved mathematics that the walls rest on, not walls.
