#!/usr/bin/env python3
"""Bounded supplied-model controls. The canonical claim card and complete corrected argument define the current claim boundary. Finite obstruction certificates do not promote deferred terminal exclusions. Optional branches count only when executed.

Historical technical inventory (read with those corrected scope qualifications):
Heat-kernel saddle versus Wilson: one-loop Lambda ratio and the two-dimensional 7/4 (2026-10-18).

Self-contained consolidated runner for block B12 (native transfer / spatial gauge lane) of the
scale-ladder campaign (.claude/science/physics-loops/scale-ladder-campaign-20261018/B12_*).
Code adapted from B12_native_lambda_ratio/b12_lambda_ratio.py, b12_literature_compare.py and
B12_check/b12_check_tadpole_hk.py, b12_check_2d_weyl.py. Perturbative (one-loop) scope only;
no physical identification. Literature numbers are NOT retrieved and are not tested.

Conventions: SU(N), Haar measure, one class function per plaquette, X = -i log U_P,
tr T^a T^b = delta^ab / 2, C2(F) = (N^2-1)/(2N).
  Wilson      w_W(U)  = exp[(beta_W/N) Re tr U],                    g_W^-2  = beta_W/(2N)
  heat kernel w_HK(U) = sum_lam d_lam chi_lam(U) exp(-tau C2(lam)),  tau = g_HK^2/2
For SU(3) the native packet saddle multiplier d_lam exp(-3 C2/beta) is w_HK at tau = 3/beta = g^2/2.

PART A (exact). Native packet recurrence = Wilson character recurrence (Pieri rule), so the native
  operator's Lambda ratio to Wilson is 1; repo C2 / dimension formulas; tree-level tau = g^2/2.
PART B (exact up to exponentially small winding terms; numerical certificate). Heat-kernel small field:
  -log K = trX^2/(2 tau) - sum_{i<j} log(theta_ij/sin theta_ij) + const, hence trX^2 coefficient
  1/(2tau) - N/24 and no O(1/g^2) quartic term. Wilson: g^-2[trX^2 - trX^4/12].
PART C (one loop). Tadpole contractions, gauge-invariant plaquette tadpole w = (2/d) g^2 (projector
  on tori + momentum sum), and the shift c(d) = (d N^2 - 8 N^2 + 12)/(24 N d); Lambda ratios.
PART D (exact d = 2, numerical certificate). Single-plaquette factorisation: fundamental-character
  matching gives tau_eff = (N/beta)(1 + k/beta), k = -2N c(2) = (N^2-2)/4, by Bessel determinants
  and, separately, by direct Weyl integration; SU(3) non-Casimir residues and the repo multiplier W2.
PART E (exact algebra). W2 = (3 - 7Q/4 + Q^2/4) W decomposed as saddle scalar + d=2 shift + residue;
  the >= 7/16 coefficient algebra of the full-top note; literature-composition algebra (inputs recalled).

Thresholds were fixed from the campaign reports before this consolidated run. Runtime: a few minutes.
"""

# Owner capture binds these complete source/context identities before and after execution.
AUDIT_TIMEOUT_SEC = 1200
AUDIT_INPUT_PATHS = (
    'docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md',
    'docs/ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_A_BODYS_CHANGE_OF_ENERGY_ACTS_AT_ONCE_UNLESS_FORMATION_KEEPS_ENERGY_LOCAL_BOUNDED_THEOREM_NOTE_2026-09-23.md',
    'docs/ADMISSIBILITY_RULE_ONE_LIGHT_CONE_EXACTLY_ON_THE_LATTICE_THE_TWO_STEP_CONTENT_MEETS_THE_MEMBERS_IDENTITY_FOR_EVERY_STATE_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md',
    'docs/ADMISSIBILITY_RULE_ONE_LIGHT_CONE_FROM_THE_SOURCE_LINK_THE_WALKERS_SMOOTH_STATES_MEET_THE_MEMBERS_IDENTITY_AT_LEADING_ORDER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md',
    'docs/ADMISSIBILITY_RULE_ONLY_THE_TWO_STEP_CURRENT_CAN_SOURCE_BLOCK_62S_SYMMETRIC_MEMBER_NO_LOCAL_PLACEMENT_OF_THE_FRAME_RESPONSE_OR_OF_THE_ONE_STEP_CURRENT_KEEPS_ITS_DIVERGENCE_CONDITION_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/ADMISSIBILITY_RULE_THE_BLIND_WALK_A_SCALAR_HOP_WEIGHTED_BY_THE_TWIST_OF_THE_COIN_ALONG_THE_BOND_MAKES_A_VARYING_ROTATION_OF_THE_COIN_AXES_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-21.md',
    'docs/ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA_AND_THERE_THE_WALKERS_OWN_STATES_CANNOT_BE_ITS_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/A_ONE_DIMENSIONAL_LATTICE_HAMILTONIAN_CONSTRAINT_WITHOUT_LOCAL_DEGREES_OF_FREEDOM_IS_FIRST_CLASS_BUT_LATTICE_PARAMETRISED_FIELD_THEORY_IS_ANOMALOUS_AND_FIRST_CLASSNESS_IS_LOCAL_ZERO_CURVATURE_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md',
    'docs/CORNER_FERMION_COVARIANT_MONOMIAL_SHIFT_LETTERS_ARE_ONLY_THE_DIAGONAL_SHIFT_POWERS_AND_THEIR_ANTIPODAL_TWINS_AND_THE_SETTLED_MOMENTUM_SHIFTING_AND_ANTIUNITARY_SUBCLASSES_REDUCE_TO_OLD_WORDS_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/CORNER_FERMION_EIGHT_CUBE_NODES_CANNOT_BE_SELECTIVELY_GAPPED_UNDER_FULL_OCTAHEDRAL_SYMMETRY_PAIRING_IS_ALL_OR_NOTHING_AND_THE_DOUBLERS_CARRY_A_Z2_WEYL_DIPOLE_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/CORNER_FERMION_INTERACTION_CHANNELS_FAVOUR_CHIRAL_TERM_OVER_DIRAC_MASS_AND_QUBIT_BUILD_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/CORNER_FERMION_MASSLESS_DIRAC_PAIR_PROTECTED_BY_CUBE_ROTATIONS_AND_PSEUDOSCALAR_DIRAC_MASS_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/CORNER_FERMION_ODD_FILLING_IS_FORCED_GAPLESS_BY_ANTICOMMUTING_GAUGE_DRESSED_C2_LIFTS_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/CORNER_FERMION_QUBIT_CODE_GENUINE_CUBE_ROTATION_ACTION_EMERGENT_FERMION_CARRIES_SPIN_HALF_CLASS_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/CORNER_FERMION_STEP_SPEED_AT_THE_FULL_OCTAHEDRAL_NODE_IS_A_SUM_OF_PER_LETTER_COEFFICIENTS_AND_GENERIC_LETTERS_SPLIT_THE_FOUR_FOLD_DIRAC_LEVEL_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md',
    'docs/CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md',
    'docs/CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md',
    'docs/CURVATURE_MEMBER_CLOSURE_PUTS_A_LATTICE_WEYL_FIELD_AND_A_LATTICE_MAXWELL_FIELD_ON_THE_SCALARS_CONE_AND_REJECTS_ANISOTROPIC_CONES_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/CURVATURE_MEMBER_CLOSURE_WITH_MATTER_FORCES_ONE_COMMON_CONE_AND_THE_LORENTZIAN_SIGN_AND_HAS_AN_ORDER_A_SQUARED_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/CURVATURE_MEMBER_CLOSURE_WITH_THE_WALKER_AS_MATTER_FORCES_ALPHA_EQUALS_K2_OVER_FOUR_AND_ONE_CURVATURE_COEFFICIENT_IN_THE_WALKERS_FRAME_NORMALISATION_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/FINITE_ACTION_FUNCTIONAL_TYPED_ADMISSIBILITY_RECORD_IDENTIFICATION_DECISION_BOUNDED_THEOREM_NOTE_2026-09-02.md',
    'docs/GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md',
    'docs/HEAT_KERNEL_SADDLE_VERSUS_WILSON_ONE_LOOP_LAMBDA_RATIO_AND_THE_TWO_DIMENSIONAL_SEVEN_QUARTERS_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08.md',
    'docs/IID_PRIORITY_FORMATION_IS_A_FINITARY_FACTOR_OF_IID_NOISE_WITH_FACTORIAL_CODING_RADIUS_TAIL_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/IID_PRIORITY_FORMATION_SPATIAL_FREQUENCY_CONSISTENCY_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/LATTICE_GRAVITON_KERNELS_ONE_TT_CONE_DEWITT_CLOSURE_AND_INDUCED_BUBBLE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'docs/NATIVE_GAUGE_TRANSFER_A2_REFLECTION_UNIFORM_HALF_LINE_GAP_THEOREM_NOTE_2026-09-02.md',
    'docs/NATIVE_GAUGE_TRANSFER_BETA_IDENTIFICATION_PHYSICAL_PLAQUETTE_RELATIONSHIP_BOUNDED_NOTE_2026-06-12.md',
    'docs/NATIVE_GAUGE_TRANSFER_FULL_TOP_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-07.md',
    'docs/NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12.md',
    'docs/NATIVE_GAUGE_TRANSFER_WILSON_SECOND_ORDER_MULTIPLIER_BOUNDED_THEOREM_NOTE_2026-09-07.md',
    'docs/NATIVE_RECORD_SUPPORT_PRESERVING_PRIORITY_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md',
    'docs/NATIVE_WEYL_CANONICAL_METRIC_CONSTRAINTS_BOUNDED_THEOREM_NOTE_2026-09-13.md',
    'docs/NO_EQUIVARIANT_FACTOR_OF_IID_NOISE_REGISTERS_A_COARSE_BLOCK_LATTICE_AND_THE_CORNER_FLUX_IS_A_FREE_SECTOR_LABEL_OF_ITS_LOCAL_FERMIONIZATION_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/NO_TRANSLATION_COVARIANT_LATTICE_RELABELLING_ALGEBRA_OF_ANY_RANGE_CLOSES_LIKE_THE_CONTINUUM_AND_THE_UNIFORM_LAPSE_BRACKET_NEEDS_A_NON_LOCAL_LEIBNIZ_RULE_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/SCALE_LADDER_CROSS_RUNG_INVARIANTS_CORNER_FERMION_BOUNDED_THEOREM_NOTE_2026-10-18.md',
    'docs/THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/UNIVERSAL_GR_CUBIC_DIFFEO_WARD_OPERATOR_TELESCOPE_BOUNDED_THEOREM_NOTE_2026-06-08.md',
    'docs/UNIVERSAL_GR_GRAVITON_DISPERSION_LORENTZ_ISOTROPY_BOUNDED_THEOREM_NOTE_2026-06-08.md',
    'docs/UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/CURRENT_PARENTS.json',
    'outputs/scale_ladder_continuations_review_2026_10_18/HISTORICAL_SOURCE_MAP.json',
    'outputs/scale_ladder_continuations_review_2026_10_18/corner_fermion_doubler_gapping_selection_rule_and_weyl_dipole_2026_10_18_full_argument.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/corner_fermion_generalised_speed_law_per_letter_additivity_2026_10_18_full_argument.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/corner_fermion_interaction_channels_and_qubit_build_2026_10_18_full_argument.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/corner_fermion_odd_filling_forced_gapless_anticommuting_c2_lifts_2026_10_18_full_argument.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/corner_fermion_symmetric_shift_letter_classification_2026_10_18_full_argument.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/curvature_member_closure_spin_half_and_spin_one_common_cone_2026_10_18_full_argument.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/curvature_member_closure_with_matter_common_cone_2026_10_18_full_argument.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/curvature_member_closure_with_the_walker_forces_alpha_k2_over_four_2026_10_18_full_argument.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/equivariant_iid_factor_registration_lemma_and_corner_flux_sector_freedom_2026_10_18_full_argument.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/heat_kernel_saddle_versus_wilson_one_loop_lambda_ratio_2026_10_18_full_argument.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B11_qubit_circuit/FINDINGS.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B11_qubit_circuit/Wref_check.npy',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B11_qubit_circuit/circuit.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B11_qubit_circuit/circuit.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B11_qubit_circuit/exact_field.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B11_qubit_circuit/exact_field.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B11_qubit_circuit/qubit_part.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B11_qubit_circuit/qubit_part.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B12_check/REPORT.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B12_check/b12_check_2d_weyl.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B12_check/b12_check_2d_weyl.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B12_check/b12_check_tadpole_hk.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B12_check/b12_check_tadpole_hk.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B12_native_lambda_ratio/FINDINGS.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B12_native_lambda_ratio/b12_lambda_ratio.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B12_native_lambda_ratio/b12_lambda_ratio.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B12_native_lambda_ratio/b12_literature_compare.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B12_native_lambda_ratio/b12_literature_compare.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B12_native_lambda_ratio/consolidated_runner_2026_10_18.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B13_ring_model_phase/b13_analyze.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B13_ring_model_phase/b13_scan.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B13_ring_model_phase/b13_scan.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B13_ring_model_phase/b13_scan2.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B13_ring_model_phase/b13_validate_2cubed.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B13_ring_model_phase/b13_validate_2cubed.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B13_ring_model_phase/b13_validate_2cubed_results.json',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B13_ring_model_phase/dmclib.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B13_ring_model_phase/jobs.txt',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B13_ring_model_phase/jobs2.txt',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B13_ring_model_phase/pqmclib.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B13_ring_model_phase/results/L4_V+0.00_N4000_s1.json',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B13_ring_model_phase/results/L4_V+0.50_N4000_s2.json',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B13_ring_model_phase/results/L4_V+1.00_N4000_s3.json',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_check/check_item6.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_check/check_item6.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_check/dp_vmax.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_check/necessity_probe.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/FINDINGS.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/S_110_0.npy',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/axis_pairs.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/best_weyl.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/best_weyl2.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/clean_rank2.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/clean_rank2.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/clean_weyl.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/clifford_family.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/cone.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/constspec.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/corner_walk0.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/corner_walk1.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/corner_walk10.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/corner_walk11.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/corner_walk12.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/corner_walk13.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/corner_walk2.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/corner_walk3.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/corner_walk4.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/corner_walk5.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/corner_walk6.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/corner_walk7.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/corner_walk8.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/corner_walk9.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/cube_scan.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/cube_scan.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/dbg.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/dbg2.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/dense_check.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/expH_search.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/expH_search.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/gapcheck.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/gapcheck2.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/orbits.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/pi6_search.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/pi6_search.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/refine_H39.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/runner_PASS18.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/runner_PASS19.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/runner_PASS20.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/shift.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/shift_clean.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/shift_walk.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/stabilizers.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/walk_b.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/walk_b2.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/walklib.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/weyl_qca.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/weyl_qca_corner.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/weyl_scan.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/word_search.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B1_parameter_free_corner_step/word_search.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B3_check/REPORT.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B3_check/independent_check.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B3_check/independent_check.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B3_formation_coding_radius/DRAFT_NOTE.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B3_formation_coding_radius/runner_formation_coding_radius.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B3_formation_coding_radius/runner_full.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4_check/REPORT.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4_check/check_a_forms.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4_check/check_a_forms_part1.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4_check/check_a_forms_part2.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4_check/check_c_closure.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4_check/check_c_closure.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4_gravity_g3/FINDINGS.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4_gravity_g3/b4_curvature_member_g3.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4_gravity_g3/b4_curvature_member_g3.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4_gravity_g3/b4_regge_background_metric.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4_gravity_g3/b4_regge_background_metric.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4_gravity_g3/b4_regge_symbol_g3.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4_gravity_g3/b4_regge_symbol_g3.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4_gravity_g3/common_spin2.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/M2_m0.250_N28.npy',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/M2_m0.350_N20.npy',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/M2_m0.500_N16.npy',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/M2_m0.700_N12.npy',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/M2_m1.000_N12.npy',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/M2_n.npy',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/REPORT.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/Tmeas_m0.7_N12.npy',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/check1.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/check2.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/check3_b4.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/check4_mass.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/check4_mass.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/check5_ct.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/check6_2comp.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/check7_S.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_check/indep_bubble.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_induced_graviton_ward/FINDINGS.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_induced_graviton_ward/b4b_variantS_and_mass.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_induced_graviton_ward/b4b_variantS_and_mass.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_induced_graviton_ward/b4b_ward_symbol.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_induced_graviton_ward/b4b_ward_symbol.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_induced_graviton_ward/stag_kernel.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B4b_induced_graviton_ward/symbol_T6_D_m0.7.npy',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_check/b5c_emitter.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_check/b5c_emitter.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_check/b5c_fast.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_check/b5c_fast.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/FINDINGS.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/b5_adversarial_mediator.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/b5_adversarial_mediator.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/b5_analyze.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/b5_analyze.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/b5_device.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/b5_repo_scale_arithmetic.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/b5_repo_scale_arithmetic.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/b5_tolerance_scan.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/scan_A.json',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/scan_A.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/scan_B.json',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/scan_B.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/scan_C.json',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/scan_C.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/scan_D.json',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/scan_D.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/scan_E.json',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B5_record_clock/scan_E.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B6_maxwell_winding/FINDINGS.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B6_maxwell_winding/b6_analyze.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B6_maxwell_winding/b6_analyze.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B6_maxwell_winding/b6_exact_ed.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B6_maxwell_winding/b6_exact_ed.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B6_maxwell_winding/b6_exact_ed_results.json',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B6_maxwell_winding/ringlib.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_check/REPORT.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_check/chk_a.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_check/chk_a_kstar.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_check/chk_c.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_check/chk_c_gap.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_check/chk_core.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_check/chk_d.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_check/chk_d_twist.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_check/chk_e.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_check/chk_e_pair.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_corner_LSM/FINDINGS.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_corner_LSM/b7_free_fermion_filling.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_corner_LSM/b7_inversion_wannier.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_corner_LSM/b7_many_body_lsm.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_corner_LSM/b7_model.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_corner_LSM/b7_staggered_class.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_corner_LSM/b7_subgroups.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_corner_LSM/run_free_fermion.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_corner_LSM/run_inversion_wannier.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_corner_LSM/run_many_body.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_corner_LSM/run_staggered.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_corner_LSM/run_subgroups.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_corner_LSM/runner_PASS25.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B8_check/REPORT.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B8_check/independent_check.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B8_check/independent_check.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B8_frequency_ergodicity/DRAFT_NOTE.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B8_frequency_ergodicity/REPORT.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B8_frequency_ergodicity/runner_frequency_consistency.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/B8_frequency_ergodicity/runner_full.log',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/C20_check/c2_out.txt',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/C20_check/chk_Tscan.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/C20_check/chk_c2.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/C20_check/chk_common.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/C20_check/chk_count.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/C20_check/chk_gap.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/C20_check/chk_lindhard.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/C20_check/chk_qubit.py',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/C20_check/gap_out.txt',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/C20_check/lindhard_out.txt',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/C20_check/qubit_out.txt',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/C20_check/runner_out.txt',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/GOAL.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/HANDOFF.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/OPPORTUNITY_QUEUE.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/STATE.yaml',
    'outputs/scale_ladder_continuations_review_2026_10_18/historical_sources/.claude/science/physics-loops/scale-ladder-campaign-20261018/TRACE_GATE.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/iid_priority_formation_finitary_factor_coding_radius_2026_10_18_full_argument.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/iid_priority_formation_spatial_frequency_consistency_2026_10_18_full_argument.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/lattice_graviton_kernels_one_cone_dewitt_closure_induced_bubble_seagull_2026_10_18_full_argument.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/lattice_hamiltonian_constraint_first_class_and_zero_curvature_2026_10_18_full_argument.md',
    'outputs/scale_ladder_continuations_review_2026_10_18/lattice_relabelling_algebra_no_go_arc_lemma_and_non_local_leibniz_2026_10_18_full_argument.md',
    'scripts/corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17.py',
    'scripts/corner_fermion_qubit_code_genuine_cube_rotation_action_spin_half_class_2026_10_17.py',
    'scripts/curvature_member_closure_with_matter_common_cone_2026_10_18.py',
)

if __name__ == "__main__":
    import signal as _capture_signal
    import sys as _capture_sys
    if not __debug__:
        raise RuntimeError("Optimized Python disables scientific assertions")
    _capture_sys.stdout.reconfigure(line_buffering=True)
    _capture_sys.stderr.reconfigure(line_buffering=True)
    def _capture_timeout(signum, frame):
        raise TimeoutError("Declared primary wall-clock cap exceeded")
    _capture_signal.signal(_capture_signal.SIGALRM, _capture_timeout)
    _capture_signal.setitimer(_capture_signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC)
    print("Execution scope: default and explicitly requested optional branches only; historical totals are not fresh evidence.", flush=True)
    print("per_element: algebraic entries and numerical fixtures below have their stated exact or floating arithmetic scope.", flush=True)
    print("per_site: only the explicitly supplied local sites and translation rules are exercised; no physical site law is inferred.", flush=True)
    print("per_mode: only displayed momentum, representation and coefficient sectors are checked; untested sectors remain unverified.", flush=True)
    print("per_block: finite matrix, graph and ansatz blocks below use their declared dimensions; optional blocks require explicit flags.", flush=True)
    print("lattice_wide: finite tori and written conditional proofs have distinct scope; numerical scans do not certify all sizes.", flush=True)

import itertools
import math
import sys
import time

import numpy as np
import sympy as sp
from mpmath import mp, besseli, matrix, det as mdet, log as mlog, mpf
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import expm_multiply

T0 = time.time()
PASS = 0
FAIL = 0
RNG = np.random.default_rng(20261018)


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok)
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""), flush=True)


def info(msg):
    print(f"[INFO] {msg}", flush=True)


def section(t):
    print(f"\n== {t}  (t = {time.time() - T0:.0f}s)", flush=True)


# ---------------------------------------------------------------- group-theory helpers
def gens(N):
    T = []
    for i in range(N):
        for j in range(i + 1, N):
            A = np.zeros((N, N), complex); A[i, j] = A[j, i] = 0.5; T.append(A)
            B = np.zeros((N, N), complex); B[i, j] = -0.5j; B[j, i] = 0.5j; T.append(B)
    for k in range(1, N):
        D = np.zeros((N, N), complex)
        for m in range(k):
            D[m, m] = 1
        D[k, k] = -k
        T.append(D / np.sqrt(2 * k * (k + 1)))
    return T


def C2_part(lam, N):
    s = sum(l * (l + N + 1 - 2 * (j + 1)) for j, l in enumerate(lam))
    return 0.5 * (s - sum(lam) ** 2 / N)


def dim_part(lam, N):
    d = 1.0
    for i in range(N):
        for j in range(i + 1, N):
            d *= (lam[i] - lam[j] + j - i) / (j - i)
    return d


def char(lam, phi):
    N = len(phi)
    num = np.linalg.det(np.array([[np.exp(1j * (lam[j] + N - 1 - j) * p) for p in phi] for j in range(N)]))
    den = np.linalg.det(np.array([[np.exp(1j * (N - 1 - j) * p) for p in phi] for j in range(N)]))
    return num / den


def dyn_to_part(p, q):
    return (p + q, q, 0)


# Wilson character coefficient of chi_lam in exp[(beta/N) Re tr U] (Bessel determinant sum)
def cW(lam, beta, N):
    x = mpf(beta) / N
    s = mpf(0)
    n = 0
    while n < 10000:
        tot = mpf(0)
        for m in ((n,) if n == 0 else (n, -n)):
            M = matrix(N, N)
            for i in range(N):
                for j in range(N):
                    M[i, j] = besseli(lam[j] + i - j + m, x)
            tot += mdet(M)
        s += tot
        if n > 3 and abs(tot) < mpf(10) ** (-(mp.dps - 5)) * abs(s):
            break
        n += 1
    else:
        raise RuntimeError("Wilson character series failed its convergence criterion within 10000 shells")
    return s


def c_d(N, d):
    return sp.Rational(N, 24) - sp.Rational(2, d) * sp.Rational(2 * N * N - 3, 12 * N)


# ================================================================ PART A
def run_part_A():
    section("PART A: native packet recurrence = Wilson character recurrence; saddle multiplier = heat kernel")
    # A1 Pieri rule: chi_(1,0) chi_(p,q) = chi_(p+1,q) + chi_(p-1,q+1) + chi_(p,q-1) (negative labels dropped),
    #    and its conjugate. Hence J = (chi_F + chi_Fbar)/6 is the native six-neighbour recurrence / 6.
    worst = 0.0
    for _ in range(4):
        ph = RNG.uniform(-np.pi, np.pi, 3); ph[2] = -ph[0] - ph[1]
        chF = char((1, 0, 0), ph); chFb = char((1, 1, 0), ph)
        for p in range(7):
            for q in range(7):
                ch = lambda a, b: char(dyn_to_part(a, b), ph) if a >= 0 and b >= 0 else 0.0
                r1 = chF * ch(p, q) - (ch(p + 1, q) + ch(p - 1, q + 1) + ch(p, q - 1))
                r2 = chFb * ch(p, q) - (ch(p, q + 1) + ch(p + 1, q - 1) + ch(p - 1, q))
                worst = max(worst, abs(r1), abs(r2))
    check("A1 SU(3) Pieri rule: (chi_F + chi_Fbar) chi_(p,q) = six-neighbour sum, negative labels omitted "
          "(4 random eigenphase points, p,q <= 6)", worst < 1e-9, f"[max residual {worst:.1e}]")
    # A2 exp(beta J)|0> on a truncated Dynkin box reproduces the Wilson coefficients c_lam/c_0 = d_lam a_lam
    mp.dps = 30
    P = 70
    idx = lambda p, q: p * P + q
    J = lil_matrix((P * P, P * P))
    for p in range(P):
        for q in range(P):
            for dp, dq in ((1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (-1, 0)):
                a, b = p + dp, q + dq
                if 0 <= a < P and 0 <= b < P:
                    J[idx(a, b), idx(p, q)] = 1.0 / 6.0
    J = J.tocsr()
    worst = 0.0
    for beta in (6.0, 12.0):
        e0 = np.zeros(P * P); e0[0] = 1.0
        v = expm_multiply(beta * J, e0)
        c0 = cW((0, 0, 0), beta, 3)
        for p in range(4):
            for q in range(4):
                nat = v[idx(p, q)] / v[0]
                wil = float(cW(dyn_to_part(p, q), beta, 3) / c0)
                worst = max(worst, abs(nat / wil - 1))
    check("A2 native exp(beta J)|0> coefficients c_(p,q)/c_(0,0) = Wilson character coefficients of "
          "exp[(beta/3) Re tr U] (beta = 6, 12; p,q <= 3): native/Wilson Lambda ratio is 1",
          worst < 1e-10, f"[max relative deviation {worst:.1e}]")
    # A3 repo C2(p,q) and d_(p,q) equal the partition formulas; C2(F) = 4/3 (tr T^aT^b = delta/2)
    ok = True
    for p in range(8):
        for q in range(8):
            lam = dyn_to_part(p, q)
            ok &= abs(C2_part(lam, 3) - (p * p + q * q + p * q + 3 * p + 3 * q) / 3) < 1e-12
            ok &= abs(dim_part(lam, 3) - (p + 1) * (q + 1) * (p + q + 2) / 2) < 1e-9
    ok &= abs(C2_part((1, 0, 0), 3) - 4 / 3) < 1e-15
    check("A3 repo C2(p,q) = (p^2+q^2+pq+3p+3q)/3 and d_(p,q) = (p+1)(q+1)(p+q+2)/2 match the partition "
          "formulas (p,q <= 7); C2(F) = 4/3", ok)
    # A4 tree level: -log w_W = const + g^-2 [trX^2 - trX^4/12] + O(X^6) with beta = 2N/g^2, and the heat
    #    kernel Gaussian term trX^2/(2 tau) equals g^-2 trX^2 iff tau = g^2/2; SU(3): tau = 3/beta.
    x1, x2, x3, g, beta = sp.symbols("x1 x2 x3 g beta", positive=True)
    xs = (x1, x2, x3)
    Nn = 3
    bW = 2 * Nn / g ** 2
    ser = sum(sp.series(-(bW / Nn) * sp.cos(x), x, 0, 6).removeO() for x in xs)
    target = -bW + (sum(x ** 2 for x in xs) - sum(x ** 4 for x in xs) / 12) / g ** 2
    check("A4 Wilson: -log w_W = const + g^-2 [trX^2 - trX^4/12] + O(X^6) (beta_W = 2N/g^2, SU(3) eigenvalues)",
          sp.simplify(ser - target) == 0)
    tau = sp.symbols("tau", positive=True)
    sol = sp.solve(sp.Eq(1 / (2 * tau), 1 / g ** 2), tau)[0]
    check("A4 tree-level matching tau = g^2/2, so tau = 3/beta for SU(3) (g^2 = 6/beta): the saddle multiplier "
          "d_lam exp(-3 C2/beta) is the heat-kernel weight", sp.simplify(sol - g ** 2 / 2) == 0
          and sp.simplify(sol.subs(g, sp.sqrt(6 / beta)) - 3 / beta) == 0)


# ================================================================ PART B
def partitions(N, lmax):
    for lam in itertools.product(range(lmax + 1), repeat=N - 1):
        if all(lam[i] >= lam[i + 1] for i in range(N - 2)):
            yield tuple(lam) + (0,)


def logK(phi, tau, N, lmax):
    s = sum(dim_part(l, N) * char(l, phi) * math.exp(-tau * C2_part(l, N)) for l in partitions(N, lmax))
    return math.log(s.real)


def logK2(phi, tau, jmax=4000):
    j = np.arange(0, jmax) / 2
    n = 2 * j + 1
    return math.log(np.sum(n * np.sin(n * phi) / np.sin(phi) * np.exp(-tau * j * (j + 1))))


def logK3(p1, p2, tau, M=160):
    ph = np.array([p1, p2, -p1 - p2])
    a = np.arange(M)[:, None]; b = np.arange(M)[None, :]
    C2 = (a * a + b * b + a * b + 3 * a + 3 * b) / 3
    dm = (a + 1) * (b + 1) * (a + b + 2) / 2
    den = np.linalg.det(np.exp(1j * np.outer([2, 1, 0], ph)))
    lam = np.stack([a + b + 2 + 0 * b, b + 1 + 0 * a, 0 * a + 0 * b], -1)  # (M, M, 3)
    E = np.exp(1j * lam[..., :, None] * ph[None, None, None, :])          # (M, M, 3, 3)
    ch = (np.linalg.det(E) / den).real
    w = np.where(tau * C2 > 60, 0.0, dm * np.exp(-tau * C2))
    return math.log(np.sum(w * ch))


def run_part_B():
    section("PART B: heat-kernel small-field expansion")
    # B1 closed form (character sum vs Gaussian x Jacobian) at several tau
    for N, tau, lmax in ((2, 0.05, 80), (3, 0.08, 55), (3, 0.04, 75)):
        consts = []
        for _ in range(5):
            p = RNG.uniform(-0.9, 0.9, N); p -= p.mean()
            th = [(p[i] - p[j]) / 2 for i in range(N) for j in range(i + 1, N)]
            jac = sum(math.log(t / math.sin(t)) for t in th if abs(t) > 1e-12)
            consts.append(logK(p, tau, N, lmax) + (p @ p) / (2 * tau) - jac)
        spread = max(consts) - min(consts)
        check(f"B1 SU({N}) tau={tau}: log K + trX^2/(2tau) - sum_(i<j) log(theta/sin theta) is X-independent "
              "(5 random X)", spread < 1e-7, f"[spread {spread:.1e}]")
    # B2 Jacobian expansion: sum_(i<j) theta_ij^2/6 = N trX^2/24 (exact, symbolic, general N = 2..5)
    ok = True
    for N in range(2, 6):
        ps = sp.symbols(f"p0:{N}")
        sub = {ps[-1]: -sum(ps[:-1])}
        lhs = sum(((ps[i] - ps[j]) / 2) ** 2 / 6 for i in range(N) for j in range(i + 1, N))
        rhs = sp.Rational(N, 24) * sum(x ** 2 for x in ps)
        ok &= sp.expand((lhs - rhs).subs(sub)) == 0
    th = sp.symbols("theta")
    jser = sp.series(sp.log(th / sp.sin(th)), th, 0, 8).removeO()
    ok &= sp.simplify(jser - (th ** 2 / 6 + th ** 4 / 180 + th ** 6 / 2835)) == 0
    check("B2 log(theta/sin theta) = theta^2/6 + theta^4/180 + ...; sum_(i<j) theta_ij^2/6 = N trX^2/24 "
          "(N = 2..5): trX^2 coefficient of -log K is 1/(2tau) - N/24, quartic terms tau-independent "
          "(no O(1/g^2) quartic)", ok)
    # B3 independent route: direct fit of the trX^2 coefficient from character sums
    ts = np.linspace(0.02, 0.25, 12)

    def fit(fun, trX2, ts_):
        y = np.array([-(fun(t) - fun(1e-4)) for t in ts_]); x = np.array([trX2(t) for t in ts_])
        A = np.vstack([x, x ** 2, x ** 3]).T
        return np.linalg.lstsq(A, y, rcond=None)[0]
    for tau in (0.05, 0.1):
        a2 = fit(lambda f: logK2(f, tau), lambda f: 2 * f * f, ts)
        check(f"B3 SU(2) tau={tau}: fitted trX^2 coefficient = 1/(2tau) - 2/24", abs(a2[0] - (1 / (2 * tau) - 1 / 12)) < 1e-4,
              f"[{a2[0]:.8f} vs {1 / (2 * tau) - 1 / 12:.8f}; (trX^2)^2 coefficient {a2[1]:.2e}, tau-independent O(1)]")
    ts3 = np.linspace(0.05, 0.35, 8)
    for tau in (0.06, 0.12):
        a3 = fit(lambda f: logK3(f, 0.37 * f, tau), lambda f: f * f + (0.37 * f) ** 2 + (1.37 * f) ** 2, ts3)
        check(f"B3 SU(3) tau={tau}: fitted trX^2 coefficient = 1/(2tau) - 3/24", abs(a3[0] - (1 / (2 * tau) - 1 / 8)) < 1e-5,
              f"[{a3[0]:.8f} vs {1 / (2 * tau) - 1 / 8:.8f}]")


# ================================================================ PART C
def incidence(L, d):
    V = L ** d
    idx = lambda x: sum(c * L ** i for i, c in enumerate(x))
    link = lambda x, mu: idx(x) * d + mu
    rows = []; cols = []; vals = []; P = 0
    for x in itertools.product(range(L), repeat=d):
        for mu in range(d):
            for nu in range(mu + 1, d):
                xm = list(x); xm[mu] = (xm[mu] + 1) % L
                xn = list(x); xn[nu] = (xn[nu] + 1) % L
                for l, s in ((link(x, mu), 1), (link(xm, nu), 1), (link(xn, mu), -1), (link(x, nu), -1)):
                    rows.append(P); cols.append(l); vals.append(s)
                P += 1
    B = np.zeros((P, V * d))
    for r, c, v in zip(rows, cols, vals):
        B[r, c] += v
    return B


def run_part_C():
    section("PART C: tadpole and the one-loop coupling shift c(d)")
    # C1 contractions by exact generator sums
    tr4 = lambda X: np.trace(X @ X @ X @ X)
    tr22 = lambda X: np.trace(X @ X) ** 2

    def quad_coeff(f, B, T):
        ts = np.array([-2, -1, 0, 1, 2], float)
        vals = [f(B + t * T).real for t in ts]
        return np.polyfit(ts, vals, 4)[2]
    for N in (2, 3, 4):
        T = gens(N)
        gram = np.array([[np.trace(a @ b).real for b in T] for a in T])
        b = RNG.normal(size=N * N - 1); B = sum(x * t for x, t in zip(b, T)); trB2 = np.trace(B @ B).real
        s4 = sum(quad_coeff(tr4, B, t) for t in T) / trB2
        s22 = sum(quad_coeff(tr22, B, t) for t in T) / trB2
        check(f"C1 SU({N}): Gram = 1/2, <trX^4>_qq = (2N^2-3)/N w trB^2, <(trX^2)^2>_qq = (N^2+1) w trB^2",
              np.allclose(gram, 0.5 * np.eye(N * N - 1)) and abs(s4 - (2 * N * N - 3) / N) < 1e-8
              and abs(s22 - (N * N + 1)) < 1e-8, f"[{s4:.10f}, {s22:.10f}]")
    # C2 gauge-invariant plaquette tadpole from the projector diag (no gauge fixing)
    for L, d in ((4, 2), (4, 3), (3, 4)):
        B = incidence(L, d)
        Pr = B @ np.linalg.pinv(B.T @ B) @ B.T
        dg = np.diag(Pr); V = L ** d
        counting = (d * V - (V - 1) - d) / (V * d * (d - 1) / 2)
        check(f"C2 d={d}, L={L}: <q_P^2>/g^2 = diag of the plaquette projector = (links - gauge - harmonic)/plaquettes "
              f"-> 2/d", abs(dg.mean() - counting) < 1e-5 and abs(counting - 2 / d) < 2 * d / V + 1e-12,
              f"[mean diag {dg.mean():.6f}, counting {counting:.6f}, 2/d = {2 / d:.4f}]")
    # C3 momentum-space route in 4D (Feynman gauge, zero mode removed)
    L = 16
    k = 2 * np.pi * np.arange(L) / L; kh2 = 4 * np.sin(k / 2) ** 2
    K = np.meshgrid(kh2, kh2, kh2, kh2, indexing="ij"); den = sum(K); msk = den > 0
    w4 = np.mean((K[0] + K[1])[msk] / den[msk])
    check("C3 d=4 momentum sum: w/g^2 = <(khat_mu^2 + khat_nu^2)/khat^2> = 1/2 (L = 16)", abs(w4 - 0.5) < 1e-12,
          f"[{w4:.12f}]")
    # C4 textbook first-order plaquette <1-P> = (N^2-1) w/(4N) with w = g^2/2
    ok = True
    for N, lit in ((2, lambda b: 3 / (4 * b)), (3, lambda b: 2 / b)):
        bb = 10.0; g2 = 2 * N / bb
        ok &= abs((N * N - 1) * (g2 / 2) / (4 * N) - lit(bb)) < 1e-15
    check("C4 w = g^2/2 reproduces the standard 4D weak-coupling <1-P> = (N^2-1) g^2/(8N) (SU(2): 3/(4beta), "
          "SU(3): 2/beta)", ok)
    # C5 symbolic c(d) from the contraction identity sum_a T^a M T^a = (tr M - M/N)/2
    N, d, g = sp.symbols("N d g", positive=True)
    w = 2 * g ** 2 / d
    CF = (N ** 2 - 1) / (2 * N)
    tr4_qq = 4 * w * CF + 2 * w * (-1 / (2 * N))       # coefficient of trB^2 in <tr(B+q)^4>_qq
    c = sp.simplify(N / 24 + sp.Rational(-1, 12) * tr4_qq / g ** 2)
    ok = sp.simplify(c - (d * N ** 2 - 8 * N ** 2 + 12) / (24 * N * d)) == 0
    ok &= sp.simplify(c.subs(d, 4) - (3 - N ** 2) / (24 * N)) == 0
    ok &= sp.simplify(sp.simplify(tr4_qq / w) - (2 * N ** 2 - 3) / N) == 0
    check("C5 g_HK^-2 = g_W^-2 + c(d), c(d) = N/24 - (2/d)(2N^2-3)/(12N) = (dN^2 - 8N^2 + 12)/(24Nd); "
          "c(4) = (3-N^2)/(24N)", ok, f"[c(d) = {sp.factor(c)}]")
    # C6 SU(3): beta_HK = beta_W - 1/2; Lambda ratios from exp(-c/(2 b0)) vs the closed form
    ok = sp.simplify(2 * 3 * c.subs({d: 4, N: 3}) + sp.Rational(1, 2)) == 0
    check("C6 SU(3): c(4) = -1/12, beta_HK = beta_W + 2N c(4) = beta_W - 1/2", ok)
    expect = {2: 1.2515, 3: 1.8188, 4: 2.0730}
    for n in (2, 3, 4):
        b0 = 11 * n / (48 * math.pi ** 2)
        cc = float(c.subs({d: 4, N: n}))
        R = math.exp(-cc / (2 * b0))
        Rc = math.exp(math.pi ** 2 * (n * n - 3) / (11 * n * n))
        check(f"C6 SU({n}): Lambda_HK/Lambda_W = exp(-c/(2b0)) = exp[pi^2 (N^2-3)/(11N^2)] = {expect[n]:.4f}",
              abs(R - Rc) < 1e-12 and abs(R - expect[n]) < 5e-5, f"[{R:.6f}; c = {cc:.6f}, b0 = 11N/(48 pi^2)]")
    # Hamiltonian variant: printed only, provisional and unchecked
    def Iabs(Lm):
        kk = 2 * np.pi * (np.arange(Lm) + 0.5) / Lm; s = 4 * np.sin(kk / 2) ** 2
        return sum(np.sqrt(a + s[:, None] + s[None, :]).sum() for a in s) / Lm ** 3
    ws = Iabs(192) / 3
    for n in (2, 3):
        b0 = 11 * n / (48 * math.pi ** 2)
        dW = -ws * (2 * n * n - 3) / (12 * n); dHK = -n / 24; cH = 0.5 * (dW - dHK)
        info(f"PROVISIONAL, UNCHECKED Hamiltonian variant SU({n}): w_s/g^2 = {ws:.6f}, c_H = {cH:.6f}, "
             f"ratio {math.exp(-cH / (2 * b0)):.4f}, one-loop speed shift v^2-1 = {dW - dHK:.5f} g^2 (needs retuning)")


# ================================================================ PART D
def alt(lam, ph):
    A = np.exp(1j * np.einsum("j,km->jkm", np.array(lam, float), ph))
    return np.linalg.det(np.moveaxis(A, 2, 0))


def weyl_coeffs(N, beta, lams, M, chunk=400000):
    """a_lam = <chi_lam>/d_lam under exp((beta/N) Re tr U), by periodic trapezoid on the eigenphase torus."""
    g = 2 * np.pi * np.arange(M) / M - np.pi
    rho = list(range(N - 1, -1, -1))
    Z = 0.0
    acc = {lam: 0.0 for lam in lams}
    total = M ** (N - 1)
    for start in range(0, total, chunk):
        ids = np.arange(start, min(total, start + chunk))
        coords = []
        r = ids.copy()
        for _ in range(N - 1):
            coords.append(g[r % M]); r //= M
        ph = np.array(coords); ph = np.vstack([ph, -ph.sum(0)])
        w = np.exp((beta / N) * (np.cos(ph).sum(0) - N))
        D0 = alt(rho, ph)
        Z += np.sum(w * np.abs(D0) ** 2)
        for lam in lams:
            acc[lam] += np.sum(w * alt([l + r_ for l, r_ in zip(lam, rho)], ph) * np.conj(D0)).real
    out = {}
    for lam in lams:
        dim = dim_part(lam, N)
        out[lam] = (acc[lam] / Z / dim, dim)
    return out


def rich(xs):  # betas doubling; model x0 + a/beta + b/beta^2
    r1 = [2 * xs[i + 1] - xs[i] for i in range(len(xs) - 1)]
    return [(4 * r1[i + 1] - r1[i]) / 3 for i in range(len(r1) - 1)]


def run_part_D():
    section("PART D: d = 2 exact single-plaquette matching, k = (N^2-2)/4")
    # D1 Bessel determinants (route 1)
    mp.dps = 50
    for N in (2, 3, 4):
        CF = mpf(N * N - 1) / (2 * N); ks = []
        for beta in (100, 200, 400, 800):
            aF = cW((1,) + (0,) * (N - 1), beta, N) / (N * cW((0,) * N, beta, N))
            tau = -mlog(aF) / CF
            ks.append(beta * (tau * beta / N - 1))
        est = rich(ks)[-1]
        pred = -2 * N * c_d(N, 2)
        check(f"D1 SU({N}) Bessel determinants: k = -2N c(2) = (N^2-2)/4 = {float(pred):.4f}",
              abs(float(est) - float(pred)) < 2e-3 and pred == sp.Rational(N * N - 2, 4),
              f"[raw k(800) = {float(ks[-1]):.5f}, Richardson {float(est):.6f}]")
    # D2 direct Weyl integration (route 2)
    for N, betas, M in ((2, (200, 400, 800, 1600), 2048), (3, (200, 400, 800, 1600), 1000), (4, (100, 200, 400), 180)):
        F = (1,) + (0,) * (N - 1); CF = (N * N - 1) / (2 * N); kk = []
        for b in betas:
            aF = weyl_coeffs(N, b, [F], M)[F][0]
            kk.append(b * ((-math.log(aF) / CF) * b / N - 1))
        est = rich(kk)[-1]
        check(f"D2 SU({N}) Weyl integration: k -> (N^2-2)/4 = {(N * N - 2) / 4}", abs(est - (N * N - 2) / 4) < 5e-3,
              f"[raw {['%.5f' % x for x in kk]}, Richardson {est:.6f}]")
    # D3 SU(3) non-Casimir residues and the repo multiplier W2 by Weyl integration
    N = 3; CF = 4 / 3; F = (1, 0, 0)
    reps = {"8": (2, 1, 0), "6": (2, 0, 0), "10": (3, 0, 0), "27": (4, 2, 0)}
    betas = (200, 400, 800, 1600); res = {k: [] for k in reps}; mult = []
    for b in betas:
        co = weyl_coeffs(3, b, [F] + list(reps.values()), 1000)
        for nm, l in reps.items():
            res[nm].append(b ** 3 * (math.log(co[l][0]) - C2_part(l, 3) / CF * math.log(co[F][0])))
        for l in [F] + list(reps.values()):
            p, q = l[0] - l[1], l[1] - l[2]
            x, y = (p + 1) / math.sqrt(b), (q + 1) / math.sqrt(b)
            Q = x * x + x * y + y * y; H = x * y * (x + y) / 2; W = H * math.exp(-Q); W2 = (3 - 7 * Q / 4 + Q * Q / 4) * W
            v = b ** -1.5 * co[l][1] * co[l][0]
            mult.append((b, b * (v - W) / W - W2 / W))
    for nm, l in reps.items():
        c2 = C2_part(l, 3); pred = 9 / 4 * (c2 * c2 - c2 * CF); r = rich(res[nm])[-1]
        check(f"D3 SU(3) d=2 residue beta^3[log a_lam - (C2/C_F) log a_F], rep {nm} -> (9/4)(C2^2 - C2 C_F) = {pred:.2f}",
              abs(r - pred) < 0.02 * pred, f"[raw {['%.3f' % x for x in res[nm]]}, Richardson {r:.4f}]")
    e = {b: max(abs(m[1]) for m in mult if m[0] == b) for b in betas}
    check("D3 repo W2 = (3 - 7Q/4 + Q^2/4) W reproduced: max_lam |beta(v-W)/W - W2/W| -> 0 like 1/beta",
          e[1600] < 0.05 and e[1600] < 0.6 * e[800] < 0.6 * 0.6 * e[400],
          f"[{', '.join(f'beta={b}: {e[b]:.4f}' for b in betas)}]")


# ================================================================ PART E
def run_part_E():
    section("PART E: reconciliation algebra")
    b, Q, Cs = sp.symbols("beta Q C2", positive=True)
    # E1 W2 = saddle scalar 3 + d=2 shift (k = 7/4) + non-Casimir residue kappa = 9/4, at fixed Q
    C2 = (b * Q - 3) / 3                       # C2(p,q) at x_p = (p+1, q+1)/sqrt(beta)
    tau_eff = (3 / b) * (1 + sp.Rational(7, 4) / b)
    expo = -tau_eff * C2 + sp.Rational(9, 4) * C2 ** 2 / b ** 3
    # beta^-3/2 d_(p,q) = H exactly; so v/W = exp(expo + Q)
    u = sp.symbols("u", positive=True)                       # u = 1/beta
    ser = sp.series(sp.exp(sp.expand(expo + Q).subs(b, 1 / u)), u, 0, 2).removeO()
    check("E1 beta^-3/2 d exp[-tau_eff C2 + (9/4) C2^2/beta^3], tau_eff = (3/beta)(1 + 7/(4beta)), "
          "= W [1 + (3 - 7Q/4 + Q^2/4)/beta + O(beta^-2)]: the -7Q/4 of the repo W2 is the d = 2 shift",
          sp.simplify(sp.expand(ser) - (1 + u * (3 - sp.Rational(7, 4) * Q + Q ** 2 / 4))) == 0)
    p_, q_ = sp.symbols("p q", nonnegative=True)
    x = (p_ + 1) / sp.sqrt(b); y = (q_ + 1) / sp.sqrt(b)
    ok = sp.simplify(b ** sp.Rational(3, 2) * x * y * (x + y) / 2 - (p_ + 1) * (q_ + 1) * (p_ + q_ + 2) / 2) == 0
    ok &= sp.simplify(3 * (p_ ** 2 + q_ ** 2 + p_ * q_ + 3 * p_ + 3 * q_) / 3 / b
                      - ((x ** 2 + x * y + y ** 2) - 3 / b)) == 0
    check("E1 scaling: beta^(3/2) H(x_p) = d_(p,q) and 3 C2(p,q)/beta = Q(x_p) - 3/beta (source of the 3 in W2)", ok)
    # E2 the full-top note's coefficient algebra: f = W2 - 3W = Q(Q-7)W/4, E_nu Q = 3/2 + kappa
    kap, var, l2 = sp.symbols("kappa Var L2", real=True)
    EQ = sp.Rational(3, 2) + kap
    d0 = (var + EQ ** 2 - 7 * EQ) / 4
    cfull = d0 + 3 + l2 / 4
    ok = sp.simplify(d0 - (var + (kap + sp.Rational(3, 2)) * (kap - sp.Rational(11, 2))) / 4) == 0
    ok &= sp.simplify(cfull - (sp.Rational(7, 16) + (var + (l2 - kap ** 2) + 2 * (kap - 1) ** 2) / 4)) == 0
    check("E2 full-top note algebra: d0/mu = [Var + (kappa+3/2)(kappa-11/2)]/4, c_full/mu = 7/16 + "
          "[Var + (|L phi|^2 - kappa^2) + 2(kappa-1)^2]/4 (a Perron-vector spectral functional, not a coupling shift)", ok)
    ks = sp.symbols("k_s", positive=True)
    d0k = (var + EQ ** 2 - 4 * ks * EQ) / 4
    floor = sp.simplify((d0k + 3 + l2 / 4 - (var + (l2 - kap ** 2)) / 4).subs(kap, sp.solve(sp.diff(d0k + kap ** 2 / 4, kap), kap)[0]))
    check("E2 with W2 - 3W = (-k_s Q + Q^2/4) W the same bound gives floor(k_s) = 105/32 - 3k_s/4 - k_s^2/2; "
          "k_s = 7/4 gives 7/16: the d = 2 shift feeds the floor, but the floor is a spectral functional",
          sp.simplify(floor - (sp.Rational(105, 32) - 3 * ks / 4 - ks ** 2 / 2)) == 0
          and sp.simplify(floor.subs(ks, sp.Rational(7, 4)) - sp.Rational(7, 16)) == 0, f"[floor(k_s) = {sp.expand(floor)}]")
    # E3 literature-composition algebra (inputs recalled, not retrieved): the non-planar 1/(8N) cancels
    N = sp.symbols("N", positive=True)
    ok = sp.simplify(1 / (8 * N) - (3 - N ** 2) / (24 * N) - N / 24) == 0
    check("E3 1/(8N) - c(4) = N/24 for all N: composing c(4) with the (recalled) Hasenfratz-Hasenfratz form "
          "ln(Lambda_W/Lambda_MS) = [1/(8N) - 0.16995599 N]/(2b0) leaves only a planar term", ok)
    for n in (2, 3, 4):
        b0 = 11 * n / (48 * math.pi ** 2)
        info(f"recalled-input composition SU({n}): Lambda_MS/Lambda_W = {38.853 * math.exp(-3 * math.pi ** 2 / (11 * n * n)):.3f}, "
             f"Lambda_MS/Lambda_HK = {38.853 * math.exp(-math.pi ** 2 / 11):.3f} (38.853 recalled, NOT retrieved)")


if __name__ == "__main__":
    print("Heat-kernel saddle versus Wilson: one-loop Lambda ratio and the 2D seven quarters (2026-10-18)")
    run_part_A()
    run_part_B()
    run_part_C()
    run_part_D()
    run_part_E()
    print(f"\nelapsed {time.time() - T0:.0f}s")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    sys.exit(0 if FAIL == 0 else 1)
