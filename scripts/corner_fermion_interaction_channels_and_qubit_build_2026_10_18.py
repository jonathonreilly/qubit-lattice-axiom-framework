#!/usr/bin/env python3
"""Bounded supplied-model controls. The canonical claim card and complete corrected argument define the current claim boundary. Finite obstruction certificates do not promote deferred terminal exclusions. Optional branches count only when executed.

Historical technical inventory (read with those corrected scope qualifications):
Corner fermion: interaction channels, clean-vacuum obstruction, and the qubit build of the C19 terms.

Supplied model only (corner fermion, flux square = plaquette = tube = pi, triangle = 0, translation-invariant
gauge, L = 4 torus); number-conserving; no physical identification.

Sections (each prints [PASS]/[FAIL] lines):
  A  qubit build: Pauli images of one-fermion bilinears c^dag_q c_r in the 48-qubit-per-site corner code
     (flux 1011) with the three noncontractible Wilson loops fixed to the fermion gauge's holonomies;
     exact Pauli-algebra checks on sampled instances, including the supports of the C19 terms X and M.
  B  interaction channels: the site-charge interaction (U/2) N_v^2 is invariant under the on-site U(12), so its
     Fock (exchange) energy is the same in all 143 traceless on-site channels (exact); static bare
     susceptibilities chi_ab(q) at q = 0 and Q = (pi,pi,pi) on the supplied metallic model, resolved into
     O_h irreps; RPA / Landau thresholds U_c = 1 / chi.  Numerical evidence on a supplied model, not a
     theorem about spontaneous symmetry breaking.
  C  clean vacuum: the dressed C2x, C2y lifts anticommute and fix the eight momenta (+-pi/2)^3, so every
     translation-invariant O-symmetric model has even levels there; hence a pocket-free state at node
     filling nu = 1 has its Fermi level on even-degenerate touchings at all eight points, and +-k* cannot
     be the only Fermi-level feature (exact corollary).  C0: exact orbit count of the invariant range-1 terms
     (38 conjugation-even + 43 conjugation-odd); the best supplied-parameter optimisation point (embedded
     below as orbit coefficients) has its only residual pocket at the forced six-point doublet.
  D  the C19-type staggered pseudoscalar mass on the same models: numerical global gaps (grid + local
     refinement, not certified) compared with the direct Dirac gap at k*.
Companion: docs/CORNER_FERMION_INTERACTION_CHANNELS_FAVOUR_CHIRAL_TERM_OVER_DIRAC_MASS_AND_QUBIT_BUILD_BOUNDED_THEOREM_NOTE_2026-10-18.md
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

import itertools, os, random, sys, time
from collections import deque
for _v in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ.setdefault(_v, '1')          # many tiny matrix products: threading only adds overhead
import numpy as np
from scipy.optimize import minimize
from scipy.special import expit

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


def conj(Xm, P, s):
    """U X U^dag for the signed permutation U: c_q -> (-1)^s(q) c_P(q)."""
    sg = (-1.0) ** s; Y = np.zeros_like(Xm); Y[np.ix_(P, P)] = Xm * np.outer(sg, sg); return Y


def compose(a, b):
    """signed permutation a after b"""
    Pa, sa = a; Pb, sb = b
    return Pa[Pb], sb ^ sa[Pb]


# ============================================================ model layer (repo definitions, as in the C19 runner)
def build_model():
    import corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17 as _model
    C = _model._run_reviewed_program(definitions_only=True)
    L = C['L']; VERTS = C['VERTS']; nV = len(VERTS); CORN = C['CORNERS']; ROTS = C['ROTS']; DIRS = C['DIRS']
    F = dict(square=1, triangle=0, plaquette=1, tube=1)
    def dmod(x): return ((x + 1) % L) - 1
    def neg(d): return tuple(-x for x in d)
    def perp(d, e): return sum(a * b for a, b in zip(d, e)) == 0 and d != e
    etypes = []; ekey = {}
    def addt(c1, c2, sh):
        if (c1, c2, sh) in ekey or (c2, c1, neg(sh)) in ekey: return
        ekey[(c1, c2, sh)] = ekey[(c2, c1, neg(sh))] = len(etypes); etypes.append((c1, c2, sh))
    Z0 = (0, 0, 0)
    for c in CORN:
        d, e = tuple(c)
        for a, b in ((d, e), (e, d)):
            for f in DIRS:
                if perp(f, a) and perp(f, b) and f != neg(b) and f != neg(a):
                    addt(c, frozenset((a, f)), Z0)
            addt(c, frozenset((neg(a), b)), a)
    nT = len(etypes)
    def cyc(seq):
        return [ekey[(c1, c2, tuple(y - x for x, y in zip(p1, p2)))] for (c1, p1), (c2, p2) in zip(seq, seq[1:] + seq[:1])]
    def vadd(a, b): return tuple(x + y for x, y in zip(a, b))
    cell = {'square': [], 'triangle': [], 'plaquette': [], 'tube': []}
    for d in DIRS:
        a = [f for f in DIRS if perp(f, d) and f != neg(d)]; a0 = a[0]
        b0 = [f for f in a if perp(f, a0) and f != neg(a0)][0]; ring = [a0, b0, neg(a0), neg(b0)]
        cell['square'].append(cyc([(frozenset((d, r)), Z0) for r in ring]))
        for i in range(4):
            p, q = ring[i], ring[(i + 1) % 4]
            cell['tube'].append(cyc([(frozenset((d, p)), Z0), (frozenset((neg(d), p)), d),
                                     (frozenset((neg(d), q)), d), (frozenset((d, q)), Z0)]))
    for s in itertools.product((1, -1), repeat=3):
        x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
        cell['triangle'].append(cyc([(frozenset((x, y)), Z0), (frozenset((y, z)), Z0), (frozenset((z, x)), Z0)]))
    for d, e in (((1, 0, 0), (0, 1, 0)), ((0, 1, 0), (0, 0, 1)), ((0, 0, 1), (1, 0, 0))):
        cell['plaquette'].append(cyc([(frozenset((d, e)), Z0), (frozenset((neg(d), e)), d),
                                      (frozenset((neg(d), neg(e))), vadd(d, e)), (frozenset((d, neg(e))), e)]))
    rows = []; rhs = []
    for k, cs in cell.items():
        for c in cs: rows.append(c); rhs.append(F[k])
    ucell = C['gf2_solve'](rows, rhs, nT)
    u = np.zeros(C['nE'], np.uint8)
    for key, i in C['EID'].items():
        a, b = tuple(key); (v, c), (w, c2) = VERTS[a], VERTS[b]
        u[i] = ucell[ekey[(c, c2, tuple(dmod(y - x) for x, y in zip(v, w)))]]
    INVM = -np.eye(3, dtype=int)
    psg = lambda f: C['psg_sign'](f, u)
    rots = [psg(lambda q, M=R: C['rot_vert'](M, q)) for R in ROTS]
    invs = [psg(lambda q, M=R @ INVM: C['rot_vert'](M, q)) for R in ROTS]
    TV = list(itertools.product(range(L), repeat=3))
    trans = [psg(lambda q, t=t: C['trans_vert'](t, q)) for t in TV]
    def w1(R):
        p = [DIRS.index(tuple(int(x) for x in R @ np.array(d))) for d in DIRS]; sgn = 1
        for i in range(6):
            while p[i] != i:
                j = p[i]; p[i], p[j] = p[j], p[i]; sgn = -sgn
        return 0 if sgn == 1 else 1
    W1 = [w1(R) for R in ROTS]
    loc0 = [C['VID'][((0, 0, 0), c)] for c in CORN]; CI = {c: i for i, c in enumerate(CORN)}
    def H0(t1, t2):
        H = np.zeros((nV, nV))
        for key in C['EDGES']:
            i, j = tuple(key); t = t1 if C['edges'][key] == 'onsite' else t2
            H[i, j] = H[j, i] = -t * (-1.0) ** u[C['EID'][key]]
        return H
    def blocks_from(Hr):
        bl = {}
        for a, v in enumerate(VERTS):
            sh = tuple(dmod(x) for x in v[0])
            for bi, j in enumerate(loc0):
                if abs(Hr[a, j]) > 1e-12: bl.setdefault(sh, np.zeros((12, 12), complex))[CI[v[1]], bi] += Hr[a, j]
        return bl
    def Hk(bl, k):
        H = np.zeros((12, 12), complex)
        for sh, M in bl.items(): H += M * np.exp(1j * np.dot(k, sh))
        return H
    def sym(Xm, Qmom=False, a2=False, inversion=False):
        Y = np.zeros_like(Xm)
        for (P, s), t in zip(trans, TV): Y += ((-1.0) ** sum(t) if Qmom else 1.0) * conj(Xm, P, s)
        Z = np.zeros_like(Xm)
        for (P, s), w in zip(rots, W1): Z += ((-1.0) ** w if a2 else 1.0) * conj(Y, P, s)
        if inversion: Z = (Z + conj(Z, *invs[0])) / 2
        return Z
    return dict(C=C, L=L, VERTS=VERTS, nV=nV, CORN=CORN, ROTS=ROTS, DIRS=DIRS, u=u, rots=rots, invs=invs, TV=TV,
                trans=trans, W1=W1, loc0=loc0, CI=CI, dmod=dmod, F=F, H0=H0, blocks_from=blocks_from, Hk=Hk, sym=sym,
                kst=np.array([1, -1, 1]) * np.pi / 2, Q=np.array([np.pi] * 3), ekey=ekey)


# ============================================================ A. qubit build
def part_A(Mdl, X, Mm):
    print("\nPart A: Pauli images of the one-fermion terms in the 48-qubit-per-site corner code (flux 1011, L = 4)")
    import corner_fermion_qubit_code_genuine_cube_rotation_action_spin_half_class_2026_10_17 as qc
    argv = sys.argv; sys.argv = ['qcode', '4', '1011']
    qc.FAIL = 0                             # its checks are guarded by __name__; only the closing SystemExit runs
    try:
        qc._run_reviewed_program()
    except SystemExit:
        pass
    finally:
        sys.argv = argv
    random.seed(3)
    VERTS = qc.VERTS; INC = qc.INC; A = qc.A; Bop = qc.Bop; pmul = qc.pmul; pcomm = qc.pcomm
    G = qc.Group(qc.NQ)
    stabs = [qc.Rop(v, h) for v in qc.SITES for h in qc.HALF if sum(h[1]) > 0] + \
            [qc.loop_op(seq, qc.FLUX[kind]) for kind, seq in qc.cycles()]
    for P in stabs: G.add(P)
    def dkey(q): v, c = q; return (v, frozenset(c))
    dl_index = {(v, c): i for i, (v, c) in enumerate(Mdl['VERTS'])}
    EIDf = Mdl['C']['EID']; uf = Mdl['u']
    def u_dl(q, r):
        a = dl_index[dkey(q)]; b = dl_index[dkey(r)]
        return (-1.0) ** uf[EIDf[frozenset((a, b))]]
    def path(src, dst):
        prev = {src: None}; dq = deque([src])
        while dq:
            x = dq.popleft()
            if x == dst: break
            for _, _, nb in INC[x]:
                if nb not in prev: prev[nb] = x; dq.append(nb)
        p = [dst]
        while p[-1] != src: p.append(prev[p[-1]])
        return p[::-1]
    def wilson(a):
        v0 = (0, 0, 0); c0 = [c for c in qc.CORN if a not in c and qc.neg(a) not in c][0]
        q = (v0, c0); seq = [q]
        for step in range(qc.L):
            nxt = (tuple((x + y) % qc.L for x, y in zip(q[0], a)), c0)
            seq += path(q, nxt)[1:]; q = nxt
        n = len(seq) - 1; S = (0, 0, n % 4); up = 1.0
        for i in range(n): S = pmul(S, A(seq[i], seq[i + 1])); up *= u_dl(seq[i], seq[i + 1])
        if up < 0: S = (S[0], S[1], (S[2] + 2) % 4)
        return S
    def canon(P):
        v = G.vec(P); comb = P
        while True:
            hit = False
            for c in sorted(G.piv, reverse=True):
                if (v >> c) & 1:
                    pv, pP = G.piv[c]; v ^= pv; comb = pmul(comb, pP); hit = True; break
            if not hit or not any((v >> c) & 1 for c in G.piv): break
        return (comb[0], comb[1]), comb[2] % 4
    def pauli_op(P, coef=1.0): return {(P[0], P[1]): coef * (1j ** P[2])}
    def omul(a, b):
        out = {}
        for (x1, z1), c1 in a.items():
            for (x2, z2), c2 in b.items():
                s = (-1) ** bin(z1 & x2).count('1'); k = (x1 ^ x2, z1 ^ z2); out[k] = out.get(k, 0) + c1 * c2 * s
        return {k: v for k, v in out.items() if abs(v) > 1e-12}
    def oadd(a, b, s=1.0):
        out = dict(a)
        for k, v in b.items(): out[k] = out.get(k, 0) + s * v
        return {k: v for k, v in out.items() if abs(v) > 1e-12}
    def ocanon(a):
        out = {}
        for (x, z), c in a.items():
            k, ph = canon((x, z, 0)); out[k] = out.get(k, 0) + c * (1j ** ph)
        return {k: v for k, v in out.items() if abs(v) > 1e-9}
    def odag(a):
        out = {}
        for (x, z), c in a.items():
            out[(x, z)] = out.get((x, z), 0) + np.conj(c) * (-1) ** bin(x & z).count('1')
        return out
    def Gop(q, r, p=None):
        p = p or path(q, r); n = len(p) - 1; S = (0, 0, n % 4); uprod = 1.0
        for i in range(n): S = pmul(S, A(p[i], p[i + 1])); uprod *= u_dl(p[i], p[i + 1])
        return pauli_op(S, 1.0 / uprod)
    def single(q, r, p=None):
        """image of c^dag_q c_r (q != r): G_P (1 + B_q)(1 - B_r)/4"""
        one = {(0, 0): 1.0}
        t = omul(omul(Gop(q, r, p), oadd(one, pauli_op(Bop(q)))), oadd(one, pauli_op(Bop(r)), -1.0))
        return {k: v / 4 for k, v in t.items()}
    for a in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
        W = wilson(a); r = G.add(W)
        check(f"Wilson loop along {a} (holonomy of the fermion gauge) is Hermitian and an independent, consistent generator",
              qc.herm(W) and r is True)
    verts = random.sample(VERTS, 40)
    ok = True
    for _ in range(20):
        q, r = random.sample(verts, 2); T = single(q, r)
        for S in random.sample(stabs, 150):
            for (x, z) in T:
                if not pcomm((x, z, 0), S): ok = False
    check("images of c^dag_q c_r commute with all sampled stabilizers (loops and repetition terms)", ok)
    bad = 0
    for _ in range(25):
        a, b, c = random.sample(verts, 3)
        comm = oadd(omul(single(a, b), single(b, c)), omul(single(b, c), single(a, b)), -1.0)
        if ocanon(oadd(comm, single(a, c), -1.0)): bad += 1
    check("fermionic algebra [Q(c+_a c_b), Q(c+_b c_c)] = Q(c+_a c_c) on the code space (random triples, mod stabilizers)",
          bad == 0, f"{25 - bad}/25")
    bad = 0
    for _ in range(15):
        a, b = random.sample(verts, 2); c_, d_ = random.sample([v for v in verts if v not in (a, b)], 2)
        if ocanon(oadd(omul(single(a, b), single(c_, d_)), omul(single(c_, d_), single(a, b)), -1.0)): bad += 1
    check("disjoint bilinears commute on the code space (15 random pairs)", bad == 0)
    def dens(q): return oadd({(0, 0): 0.5}, pauli_op(Bop(q)), -0.5)
    bad = 0
    for _ in range(15):
        a, b = random.sample(verts, 2)
        comm = oadd(omul(dens(a), single(a, b)), omul(single(a, b), dens(a)), -1.0)
        if ocanon(oadd(comm, single(a, b), -1.0)): bad += 1
    check("[Q(n_a), Q(c+_a c_b)] = Q(c+_a c_b) on the code space (15 random pairs)", bad == 0)
    # path independence on the code space (the Wilson loops make noncontractible path differences trivial)
    bad = 0; tested = 0
    for _ in range(8):
        q, r = random.sample(verts, 2); p1 = path(q, r)
        # a second path: go around one step of a different neighbour first
        nb = [n for _, _, n in INC[q] if n != p1[1]][0]; p2 = [q] + path(nb, r)
        if len(set(p2)) != len(p2): continue
        tested += 1
        if ocanon(oadd(single(q, r, p1), single(q, r, p2), -1.0)): bad += 1
    check("the image of c^dag_q c_r is path independent on the code space (two different paths, random pairs)",
          bad == 0 and tested >= 5, f"{tested - bad}/{tested}")
    # the supports of the C19 terms: X (range <= 1 site) and M (on-site, staggered); images of their bilinears
    qv = {i: (v, tuple(sorted(c))) for i, (v, c) in enumerate(Mdl['VERTS'])}
    def term_pairs(Hm, n):
        loc0 = Mdl['loc0']; prs = []
        for j in loc0:
            for i in np.nonzero(np.abs(Hm[:, j]) > 1e-12)[0]:
                if i != j: prs.append((int(i), int(j)))
        random.shuffle(prs); return prs[:n]
    def herm_term(Hm, prs):
        out = {}
        for i, j in prs:
            t = {k: v * Hm[i, j] for k, v in single(qv[i], qv[j]).items()}
            out = oadd(out, oadd(t, odag(t)))
        return out
    okX = True; nprs = 0
    for Hm, lab in ((X, 'X'), (Mm, 'M')):
        prs = term_pairs(Hm, 6); nprs += len(prs)
        T = herm_term(Hm, prs)
        okX &= bool(T) and not ocanon(oadd(T, odag(T), -1.0))
        for S in random.sample(stabs, 200):
            okX &= all(pcomm((x, z, 0), S) for (x, z) in T)
    check("images of sampled entries of the C19 terms X and M (h c^dag_q c_r + h.c., complex h) are nonzero, Hermitian "
          "and commute with the sampled stabilizers", okX, f"{nprs} entries")
    EDGES = []; seen = set()
    for q in VERTS:
        for k, e, nb in INC[q]:
            key = frozenset((qc.VID[q], qc.VID[nb]))
            if key not in seen: seen.add(key); EDGES.append((q, nb) if qc.canon_first(q, nb) else (nb, q))
    def rot_op(R):
        perm = qc.qperm(R); cz = qc.cz_network(R); zf = 0
        for e in EDGES:
            img = qc.apply_cz(qc.apply_perm(A(*e), perm), cz); q, r = e
            Rq = (qc.rs(R, q[0]), qc.rc(R, q[1])); Rr = (qc.rs(R, r[0]), qc.rc(R, r[1]))
            tgt = A(Rq, Rr)
            if (img[2] - tgt[2]) % 4 == 2:
                if not qc.canon_first(Rq, Rr): Rq, Rr = Rr, Rq
                zf ^= 1 << qc.edge_zqubit(Rq, *[ed for k, ed, nb in INC[Rq] if nb == Rr][0])
        return perm, cz, zf
    def U_apply(rop, opr):
        perm, cz, zf = rop; out = {}
        for (x, z), c in opr.items():
            P = qc.apply_zfix(qc.apply_cz(qc.apply_perm((x, z, 0), perm), cz), zf)
            k = (P[0], P[1]); out[k] = out.get(k, 0) + c * (1j ** P[2])
        return out
    def d_index(R):
        for k, S in enumerate(Mdl['ROTS']):
            if (S == R).all(): return k
    bad = 0; tested = 0
    for R in [qc.ROTS[i] for i in random.sample(range(24), 6)]:
        rop = rot_op(R); P_, sg = Mdl['rots'][d_index(R)]
        for _ in range(6):
            q, r = random.sample(verts, 2)
            Rq = (qc.rs(R, q[0]), qc.rc(R, q[1])); Rr = (qc.rs(R, r[0]), qc.rc(R, r[1]))
            sq = (-1.0) ** sg[dl_index[dkey(q)]]; sr = (-1.0) ** sg[dl_index[dkey(r)]]
            lhs = U_apply(rop, single(q, r)); rhs = {k: v * sq * sr for k, v in single(Rq, Rr).items()}
            tested += 1
            if ocanon(oadd(lhs, rhs, -1.0)): bad += 1
    check("covariance U_R Q(c+_q c_r) U_R^dag = sigma_R(q) sigma_R(r) Q(c+_Rq c_Rr) with the fermion-level PSG signs "
          "(6 random rotations x 6 random bilinears)", bad == 0, f"{tested - bad}/{tested}")


# ============================================================ B. interaction channels
CHAR_O = {  # classes: E, C3, C2(axis), C4, C2'(edge)
    'A1': (1, 1, 1, 1, 1), 'A2': (1, 1, 1, -1, -1), 'E': (2, -1, 2, 0, 0), 'T1': (3, 0, -1, 1, -1), 'T2': (3, 0, -1, -1, 1)}


def o_class(R):
    tr = int(np.trace(R))
    if tr == 3: return 0
    if tr == 0: return 1
    if tr == 1: return 3
    return 2 if np.allclose(np.abs(np.diag(R)), 1) else 4


def part_B(Mdl, X, Mm, node):
    print("\nPart B: site-charge interaction (U/2) sum_v N_v^2 and the on-site particle-hole channels")
    loc0 = Mdl['loc0']; Hk = Mdl['Hk']; kst = Mdl['kst']; Q = Mdl['Q']
    # orthonormal Hermitian basis: 78 real symmetric, 66 imaginary antisymmetric
    basis = []; kinds = []
    for i in range(12):
        for j in range(i, 12):
            B = np.zeros((12, 12), complex)
            if i == j: B[i, i] = 1
            else: B[i, j] = B[j, i] = 1 / np.sqrt(2)
            basis.append(B); kinds.append('real')
    for i in range(12):
        for j in range(i + 1, 12):
            B = np.zeros((12, 12), complex); B[i, j] = -1j / np.sqrt(2); B[j, i] = 1j / np.sqrt(2)
            basis.append(B); kinds.append('imag')
    Bm = np.array(basis); isim = np.array([k == 'imag' for k in kinds])
    # B1: exact statements about the interaction
    rng = np.random.default_rng(5)
    def herm(n):
        A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); return (A + A.conj().T) / 2
    # Fock-space check on one site (12 modes, 4096 states): N commutes with every on-site bilinear
    dim = 1 << 12
    occ = np.array([[(x >> a) & 1 for a in range(12)] for x in range(dim)])
    Nop = occ.sum(1)
    ok_comm = True
    for _ in range(3):
        a, b = rng.choice(12, 2, replace=False)
        # c^dag_a c_b maps basis state x (b occupied, a empty) to x ^ (1<<a) ^ (1<<b) with a JW sign
        src = np.nonzero((occ[:, b] == 1) & (occ[:, a] == 0))[0]; dst = src ^ (1 << a) ^ (1 << b)
        ok_comm &= np.all(Nop[src] == Nop[dst])
    # Hartree-Fock energy of the site interaction for a quasi-free state with one-body matrix rho:
    # <(U/2) N^2> = (U/2) [ (tr rho)^2 + tr rho - tr rho^2 ];  second variation along a traceless direction:
    U = 1.0
    def Ehf(r): return U / 2 * (np.trace(r).real ** 2 + np.trace(r).real - np.trace(r @ r).real)
    ok_iso = True; vals = []
    for _ in range(20):
        r0 = herm(12); Xd = herm(12); Xd -= np.trace(Xd) / 12 * np.eye(12); Xd /= np.linalg.norm(Xd)
        h = 1e-3; d2 = (Ehf(r0 + h * Xd) - 2 * Ehf(r0) + Ehf(r0 - h * Xd)) / h ** 2; vals.append(d2)
        ok_iso &= abs(d2 + U) < 1e-6
    # direct Wick check of <N^2> on a random number-mixed quasi-free (thermal) state of the 12 modes
    hq = herm(12); e, V = np.linalg.eigh(hq); f = expit(-e)
    rho = (V * f) @ V.conj().T
    n2_exact = np.sum(f) ** 2 + np.sum(f * (1 - f))  # occupation-number variance of independent modes
    ok_wick = abs(n2_exact - (np.trace(rho).real ** 2 + np.trace(rho).real - np.trace(rho @ rho).real)) < 1e-12
    check("exact: N_v commutes with every on-site bilinear c^dag_a c_b (Fock space of one site); hence (U/2) N_v^2 is "
          "invariant under the on-site U(12) and its Fock energy (U/2)[(tr rho)^2 + tr rho - tr rho^2] has second "
          "variation -U ||delta rho||^2 in every traceless direction: equal exchange attraction in all 143 channels",
          ok_comm and ok_iso and ok_wick, f"second variations in [{min(vals):.6f}, {max(vals):.6f}] (U = 1)")
    # B2: the supplied metallic model
    bl = Mdl['blocks_from'](Mdl['H0'](-1.0, 0.2) + 0.05 * X)
    eK = np.linalg.eigvalsh(Hk(bl, kst)); eM = np.linalg.eigvalsh(Hk(bl, -kst)); mu = eK[0]
    check("supplied metallic model (t1 = -1, t2 = 0.2, 0.05 X): degenerate node doublets at k* and -k*; chemical "
          "potential at the node", abs(eK[0] - eK[1]) < 1e-10 and abs(eM[0] - eK[0]) < 1e-10, f"E_N = {mu:.6f}")
    # O_h action on the operator space (signed site-0 corner permutations; signs cancel in conjugation)
    def site_mat(Ps):
        P, s = Ps; Mt = np.zeros((12, 12))
        for bi, j in enumerate(loc0):
            Mt[loc0.index(P[j]), bi] = (-1.0) ** s[j]
        return Mt
    SR = [site_mat(x) for x in Mdl['rots']]; SI = [site_mat(x) for x in Mdl['invs']]
    def Dop(S):
        SBS = np.einsum('ij,bjk,lk->bil', S, Bm, S)
        return np.einsum('aij,bij->ab', Bm.conj(), SBS).real
    DR = [Dop(S) for S in SR]; DI = [Dop(S) for S in SI]
    cls = [o_class(R) for R in Mdl['ROTS']]
    projs = {}
    for name, ch in CHAR_O.items():
        for par, ps in (('g', 1), ('u', -1)):
            P = sum(ch[cls[k]] * (DR[k] + ps * DI[k]) for k in range(24)) * ch[0] / 48
            projs[name + par] = P
    mult = {k: int(round(np.trace(P) / CHAR_O[k[:-1]][0])) for k, P in projs.items()}
    check("the 144 on-site operators decompose under O_h (projectors from the O character table and the site "
          "inversion) with multiplicities summing to 144",
          sum(mult[k] * CHAR_O[k[:-1]][0] for k in mult) == 144 and np.allclose(sum(projs.values()), np.eye(144)),
          str(mult))
    grp = DR + [DI[k] for k in range(24)]
    def chi_matrix(Qv, N, T, off=0.037):
        g = np.linspace(-np.pi, np.pi, N, endpoint=False)
        chi = np.zeros((144, 144), complex)
        for k in itertools.product(g, g, g):
            k = np.array(k) + off
            e1, v1 = np.linalg.eigh(Hk(bl, k)); e2, v2 = np.linalg.eigh(Hk(bl, k + Qv))
            f1 = expit(-(e1 - mu) / T); f2 = expit(-(e2 - mu) / T)
            de = e2[None, :] - e1[:, None]; df = f1[:, None] - f2[None, :]
            with np.errstate(divide='ignore', invalid='ignore'):
                W = np.where(np.abs(de) > 1e-9, df / de, (f1 * (1 - f1) / T)[:, None] * np.ones_like(de))
            Om = (v1.conj().T @ (Bm @ v2)).reshape(144, -1)          # <n k| B_a |m k+q>
            chi += (Om * W.ravel()) @ Om.conj().T
        chi /= N ** 3
        chi = (chi + chi.conj().T) / 2
        asym = max(np.linalg.norm(D @ chi.real @ D.T - chi.real) for D in grp) / np.linalg.norm(chi.real)
        chis = sum(D @ chi.real @ D.T for D in grp) / 48   # O_h-symmetrized quadrature (operator basis is real)
        return chi, chis, asym
    idv = np.array([np.trace(B).real for B in Bm]) / np.sqrt(12); Pt = np.eye(144) - np.outer(idv, idv)
    def sector_max(chis, P):
        w, Vv = np.linalg.eigh(P); Vs = Vv[:, w > 0.5]
        Vs = Pt @ Vs; uu, ss, _ = np.linalg.svd(Vs, full_matrices=False); Vs = uu[:, ss > 1e-8]
        if Vs.shape[1] == 0: return None, None
        w2, V2 = np.linalg.eigh(Vs.T @ chis @ Vs); return w2[-1], Vs @ V2[:, -1]
    def Uc_full(chis):
        # Landau / RPA kernel incl. the Hartree term: U [12 P_0 - 1]; 1/U_c = largest eig of chi^1/2 (1 - 12 P_0) chi^1/2
        w, Vv = np.linalg.eigh(chis); s = Vv @ np.diag(np.sqrt(np.clip(w, 0, None))) @ Vv.T
        return 1 / np.linalg.eigvalsh(s @ (np.eye(144) - 12 * np.outer(idv, idv)) @ s)[-1]
    res = {}
    t0 = time.time()
    for lab, Qv in (('q=0', np.zeros(3)), ('Q', Q)):
        chi_raw, chis, asym = chi_matrix(Qv, 12, 0.01)
        wraw = np.linalg.eigvalsh(chi_raw)
        top = {}
        for name, P in projs.items():
            val, vec = sector_max(chis, P)
            if val is not None: top[name] = (val, vec)
        lead = max(top, key=lambda k: top[k][0])
        res[lab] = dict(top=top, lead=lead, chis=chis, asym=asym, Uc=Uc_full(chis), psd=wraw[0] > -1e-10,
                        allmax=np.linalg.eigvalsh(Pt @ chis @ Pt)[-1])
        print(f"   {lab}: leading susceptibility per O_h irrep (trace removed; N = 12, T = 0.01, symmetrized; raw "
              f"quadrature asymmetry {asym:.1e}):", flush=True)
        print("      " + ", ".join(f"{k} {v[0]:.4f}" for k, v in sorted(top.items(), key=lambda kv: -kv[1][0])))
    print(f"   ({time.time() - t0:.0f} s)")
    r0, rQ = res['q=0'], res['Q']
    check("the bare static susceptibility matrices are positive semidefinite (Lindhard form) at q = 0 and Q",
          r0['psd'] and rQ['psd'])
    lead0 = r0['lead']; v0 = r0['top'][lead0][1]
    imfrac0 = np.linalg.norm(v0[isim]) ** 2
    # the C18 chiral term: i lambda on the oriented on-site triangles (gauge signs), restricted to site 0
    Hl = np.zeros((12, 12), complex); CI = Mdl['CI']; ekey = Mdl['ekey']
    TRI = []
    for s in itertools.product((1, -1), repeat=3):
        x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
        cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
        if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
        TRI += [(cy[i], cy[(i + 1) % 3]) for i in range(3)]
    # gauge sign of an on-site edge from the L = 4 gauge u
    C = Mdl['C']
    for q, r in TRI:
        sgn = (-1.0) ** Mdl['u'][C['eid'](((0, 0, 0), q), ((0, 0, 0), r))]
        Hl[CI[r], CI[q]] += 1j * sgn; Hl[CI[q], CI[r]] += -1j * sgn
    lam_vec = np.array([np.vdot(B, Hl).real for B in Bm]); lam_vec /= np.linalg.norm(lam_vec)
    ov = abs(lam_vec @ v0)
    lam_in = np.linalg.norm(projs[lead0] @ lam_vec)
    check("q = 0: the leading channel over all traceless on-site channels is A1u (O-invariant, odd under the site "
          "inversion), purely imaginary (complex-conjugation odd); its 3-dimensional sector contains the C18 chiral "
          "triangle term i lambda, which has a large but not complete overlap with the leading vector",
          lead0 == 'A1u' and abs(r0['top'][lead0][0] - r0['allmax']) < 1e-8 and imfrac0 > 0.999 and lam_in > 0.999 and ov > 0.5,
          f"{lead0}: chi = {r0['top'][lead0][0]:.4f}, imaginary weight {imfrac0:.4f}, i-lambda term inside A1u: "
          f"{lam_in:.4f}, overlap with the leading vector {ov:.4f}")
    # Dirac-mass channel: A2 at Q, imaginary part; its leading vector gives a node-space mass
    a2 = [k for k in rQ['top'] if k.startswith('A2')]
    a2best = max(a2, key=lambda k: rQ['top'][k][0]); chiA2, vA2 = rQ['top'][a2best]
    # lattice operator for the leading A2 Q-channel and its node-space projection
    def lattice_op(vec, stag):
        Xs = np.tensordot(vec, Bm, 1); Hm = np.zeros((Mdl['nV'], Mdl['nV']), complex)
        for v in Mdl['C']['SITES']:
            idx = [Mdl['C']['VID'][(v, c)] for c in Mdl['CORN']]
            Hm[np.ix_(idx, idx)] = Xs * ((-1.0) ** sum(v) if stag else 1.0)
        return Hm
    MA2 = lattice_op(vA2, True)
    w4 = np.linalg.eigvalsh(node.conj().T @ MA2 @ node)
    check("Q: the leading A2 channel is the pseudoscalar Dirac-mass channel (imaginary; its node-space projection is "
          "+-m with two-fold degeneracy)",
          np.linalg.norm(vA2[isim]) ** 2 > 0.999 and np.allclose(w4[:2], w4[0], atol=1e-8) and np.allclose(w4[2:], -w4[0], atol=1e-8)
          and abs(w4[0]) > 1e-3, f"{a2best}: chi = {chiA2:.4f}, projected eigenvalues {np.round(w4, 4)}")
    leadQ = rQ['lead']
    check("ranking: chi(Dirac mass, Q) < chi(leading, q = 0) and < chi(leading, Q); so in this RPA/Landau "
          "treatment the Dirac mass is not the first instability",
          chiA2 < r0['top'][lead0][0] and chiA2 < rQ['top'][leadQ][0],
          f"U_c(leading q=0) = {1 / r0['top'][lead0][0]:.3f}, U_c(leading Q, {leadQ}) = {1 / rQ['top'][leadQ][0]:.3f}, "
          f"U_c(Dirac mass) = {1 / chiA2:.3f}; with the Hartree term kept: U_c(q=0) = {r0['Uc']:.3f}, U_c(Q) = {rQ['Uc']:.3f}")
    # the leading q = 0 order preserves translations and O: condensing it keeps the k* doublets (shifts them)
    O0 = lattice_op(v0, False)
    phi = 0.05
    bl2 = Mdl['blocks_from'](Mdl['H0'](-1.0, 0.2) + 0.05 * X + phi * O0)
    e2K = np.linalg.eigvalsh(Hk(bl2, kst)); e2M = np.linalg.eigvalsh(Hk(bl2, -kst))
    check("condensing the leading q = 0 channel (strength 0.05) keeps degenerate doublets at k* and -k* and shifts "
          "them oppositely: a valley (chiral-chemical-potential-like) splitting, not a gap",
          abs(e2K[0] - e2K[1]) < 1e-10 and abs(e2M[0] - e2M[1]) < 1e-10 and abs((e2K[0] - mu) + (e2M[0] - mu)) < 0.1 * abs(e2K[0] - e2M[0])
          and abs(e2K[0] - e2M[0]) > 1e-3, f"E(k*) - E_N = {e2K[0] - mu:+.5f}, E(-k*) - E_N = {e2M[0] - mu:+.5f}")
    # convergence control: finer grid and lower temperature for the two channels being ranked
    t0 = time.time()
    _, chis0, _ = chi_matrix(np.zeros(3), 16, 0.005, off=0.021)
    _, chisQ, _ = chi_matrix(Q, 16, 0.005, off=0.021)
    l0 = sector_max(chis0, projs[lead0])[0]; lA2 = sector_max(chisQ, projs[a2best])[0]
    lQ = max(v for v in (sector_max(chisQ, P)[0] for P in projs.values()) if v is not None)
    check("control (N = 16, T = 0.005, different grid offset): the ranking chi(leading q = 0) > chi(Dirac mass, Q) persists",
          l0 > lA2 and lQ > lA2, f"chi({lead0}, q=0) = {l0:.4f}, chi({a2best}, Q) = {lA2:.4f}, max at Q = {lQ:.4f} "
          f"({time.time() - t0:.0f} s)")
    return res


# ============================================================ C. clean vacuum
def part_C(Mdl, X, models):
    print("\nPart C: can the Dirac point be the only Fermi-level feature at node filling (nu = 1)?")
    nV = Mdl['nV']; L = Mdl['L']; Hk = Mdl['Hk']; kst = Mdl['kst']; ROTS = Mdl['ROTS']; rots = Mdl['rots']
    def rid(diag): return [k for k, R in enumerate(ROTS) if np.allclose(R, np.diag(diag))][0]
    gx, gy = rots[rid((1, -1, -1))], rots[rid((-1, 1, -1))]
    ab, ba = compose(gx, gy), compose(gy, gx)
    check("exact: the dressed lifts of the commuting half-turns C2x, C2y anticommute on the whole L = 4 one-particle "
          "space (same permutation, opposite sign on every corner mode)",
          np.array_equal(ab[0], ba[0]) and np.all(ab[1] ^ ba[1] == 1))
    # plane waves on the torus: momentum k, corner c
    VERTS = Mdl['VERTS']; VID = Mdl['C']['VID']; CORN = Mdl['CORN']
    pos = np.array([v for v, c in VERTS]); cidx = np.array([Mdl['CI'][c] for v, c in VERTS])
    def pw(k):
        B = np.zeros((nV, 12), complex)
        B[np.arange(nV), cidx] = np.exp(1j * pos @ k) / L ** 1.5
        return B
    def act(g, B):
        P, s = g; Y = np.zeros_like(B); Y[P] = B * ((-1.0) ** s)[:, None]; return Y
    pts = [np.array(sg) * np.pi / 2 for sg in itertools.product((1, -1), repeat=3)]
    fixed = True; anti = True
    for k in pts:
        Bk = pw(k)
        for g in (gx, gy):
            Y = act(g, Bk); fixed &= np.allclose(Bk @ (Bk.conj().T @ Y), Y)
        Ux = Bk.conj().T @ act(gx, Bk); Uy = Bk.conj().T @ act(gy, Bk)
        anti &= np.allclose(Ux @ Uy, -Uy @ Ux) and np.allclose(Ux @ Ux.conj().T, np.eye(12))
    check("the eight momenta (+-pi/2)^3 are fixed by both dressed half-turns, and there the restricted 12 x 12 "
          "unitaries anticommute; so every Bloch level there is even-degenerate for any translation-invariant H "
          "commuting with them", fixed and anti)
    # orbit structure of the eight points under the 24 affine rotation maps
    def image(g, k):
        Y = act(g, pw(k))
        for k2 in pts:
            if np.linalg.norm(pw(k2).conj().T @ Y) > 1e-6: return tuple(np.round(k2 / (np.pi / 2)).astype(int))
        return None
    def orbits(group):
        out = set()
        for k in pts: out.add(frozenset(image(g, k) for g in group))
        return sorted(len(o) for o in out), out
    kfix = tuple(np.round(kst / (np.pi / 2)).astype(int)); kneg = tuple(-x for x in kfix)
    sO, oO = orbits(rots); sOh, oOh = orbits(rots + Mdl['invs'])
    check("orbits of the eight points under the dressed affine maps: O gives {k*}, {-k*} and two triples; adding the "
          "site inversion joins the triples into one orbit of six (and k* with -k*)",
          sO == [1, 1, 3, 3] and frozenset([kfix]) in oO and frozenset([kneg]) in oO and sOh == [2, 6], f"O: {sO}, O_h: {sOh}")
    print("   corollary (exact): at nu = 1 a pocket-free filled band 0 needs E0(k) <= mu <= E1(k) everywhere; at the eight "
          "points E0 = E1, so all eight touch mu: six further touchings besides +-k*, never a two-node Fermi level")
    k6 = [k for k in pts if tuple(np.round(k / (np.pi / 2)).astype(int)) not in (kfix, tuple(-x for x in kfix))]
    out = {}
    for lab, bl in models.items():
        EN = np.linalg.eigvalsh(Hk(bl, kst))[0]
        lev = np.array([np.linalg.eigvalsh(Hk(bl, k))[:2] for k in pts])
        e6 = np.array([np.linalg.eigvalsh(Hk(bl, k))[0] for k in k6]) - EN
        f = lambda k: np.linalg.eigvalsh(Hk(bl, k))
        g = np.linspace(-np.pi, np.pi, 12, endpoint=False)
        G = np.array(list(itertools.product(g, g, g))) + 0.011
        E = np.array([f(k)[:2] for k in G])
        i0 = np.argsort(-E[:, 0])[:6]; i1 = np.argsort(E[:, 1])[:6]
        cands0 = [minimize(lambda k: -f(k)[0], G[i], method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-13, maxiter=3000)) for i in i0]
        cands1 = [minimize(lambda k: f(k)[1], G[i], method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-13, maxiter=3000)) for i in i1]
        top = max([-c.fun for c in cands0] + list(lev[:, 0])); bot = min([c.fun for c in cands1] + list(lev[:, 1]))
        out[lab] = (np.allclose(lev[:, 0], lev[:, 1], atol=1e-9), e6, top - EN, bot - EN)
        dk = 1e-5 * np.array([1.0, 2.0, 3.0]) / np.sqrt(14.0); ed = np.linalg.eigvalsh(Hk(bl, kst + dk))
        print(f"   {lab}: E_N = {EN:.5f}, Weyl velocity {(ed[1] - ed[0]) / 2e-5:.4f}; E_6 - E_N = {np.round(e6, 5)} ; "
              f"refined max band0 - E_N = {top - EN:+.4e} ; "
              f"min band1 - E_N = {bot - EN:+.4e}", flush=True)
    check("in every tested O_h-symmetric model the band-0/band-1 pairs are degenerate at all eight points and the "
          "six-point doublet energy E_6 is a single number above E_N, so each tested model has a hole pocket there",
          all(v[0] and np.ptp(v[1]) < 1e-9 and v[1][0] > 1e-4 for v in out.values()))
    vo = out['optimisation point']
    check("optimisation point: no electron pocket (min band 1 = E_N, at the node) and the only band-0 excess over E_N "
          "found by the refined search is the forced six-point doublet (max band 0 - E_N = E_6 - E_N)",
          abs(vo[3]) < 1e-9 and abs(vo[2] - vo[1][0]) < 1e-7, f"E_6 - E_N = {vo[1][0]:.4e}")
    return out


# ============================================================ supplied clean-vacuum optimisation point
# Supplied parameters: the best clean-vacuum optimisation point of the C20 campaign (L-BFGS on a band-overlap
# penalty, stopped by a time limit at penalty 1.4e-3), re-expressed exactly (fit residual 8e-14) in the
# deterministic orbit basis of orbit_basis().  Key = representative block entry (row shift sh, row corner index,
# column corner index in the PSG runner's CORNERS order, 're' or 'im'); the term is the O_h orbit sum of that entry
# with gauge-dressed signs plus its Hermitian partner.  The two 're' keys are the on-site and link hoppings.
OPT_POINT = {
    ((-1, -1, -1), 0, 1, 'im'): -8.794990853205e-03,
    ((-1, -1, -1), 0, 2, 'im'): 2.114791363471e-02,
    ((-1, -1, -1), 0, 3, 'im'): 1.271296915862e-05,
    ((-1, -1, -1), 0, 5, 'im'): -5.664366198661e-03,
    ((-1, -1, -1), 0, 6, 'im'): -1.183891941742e-02,
    ((-1, -1, -1), 0, 7, 'im'): 4.832206635463e-03,
    ((-1, -1, -1), 1, 0, 'im'): 1.031748666449e-02,
    ((-1, -1, -1), 1, 1, 'im'): -4.858532268022e-04,
    ((-1, -1, -1), 1, 2, 'im'): 1.404227882642e-03,
    ((-1, -1, -1), 1, 3, 'im'): -2.879595946092e-03,
    ((-1, -1, -1), 1, 4, 'im'): 1.187615800448e-03,
    ((-1, -1, -1), 1, 6, 'im'): -3.843894828917e-03,
    ((-1, -1, -1), 1, 8, 'im'): -1.142095795292e-02,
    ((-1, -1, -1), 1, 9, 'im'): -3.192280923985e-03,
    ((-1, -1, -1), 5, 0, 'im'): 7.223658556106e-03,
    ((-1, -1, -1), 5, 2, 'im'): -5.720794266215e-03,
    ((-1, -1, 0), 0, 0, 'im'): 4.827905466399e-03,
    ((-1, -1, 0), 0, 2, 'im'): -7.468193294692e-03,
    ((-1, -1, 0), 0, 6, 'im'): -5.943345605312e-04,
    ((-1, -1, 0), 1, 2, 'im'): 6.482854280170e-04,
    ((-1, -1, 0), 1, 4, 'im'): -1.121275656902e-03,
    ((-1, -1, 0), 1, 6, 'im'): -1.167981898323e-02,
    ((-1, -1, 0), 1, 8, 'im'): -7.481143450861e-03,
    ((-1, -1, 0), 1, 10, 'im'): 3.595551711844e-03,
    ((-1, -1, 0), 2, 0, 'im'): -1.120571533322e-02,
    ((-1, -1, 0), 2, 2, 'im'): 3.399353505620e-03,
    ((-1, -1, 0), 2, 3, 'im'): -2.884548180260e-03,
    ((-1, -1, 0), 2, 6, 'im'): 5.519031916504e-03,
    ((-1, -1, 0), 2, 7, 'im'): 1.543043875562e-03,
    ((-1, -1, 0), 2, 8, 'im'): 6.378773950058e-03,
    ((-1, -1, 0), 2, 9, 'im'): 1.128572134013e-02,
    ((-1, -1, 0), 5, 2, 'im'): 2.059251341011e-02,
    ((-1, -1, 0), 6, 2, 'im'): 4.243122238536e-03,
    ((-1, -1, 0), 6, 3, 'im'): 1.095545152966e-02,
    ((-1, 0, 0), 0, 1, 'im'): -1.020202543632e-02,
    ((-1, 0, 0), 0, 2, 'im'): 1.255891427111e-02,
    ((-1, 0, 0), 0, 4, 're'): -2.004924792527e-02,
    ((-1, 0, 0), 0, 6, 'im'): 1.161167062291e-03,
    ((-1, 0, 0), 0, 8, 'im'): -3.124885091682e-03,
    ((-1, 0, 0), 0, 10, 'im'): 6.258058171815e-03,
    ((-1, 0, 0), 4, 2, 'im'): 9.494321977399e-03,
    ((-1, 0, 0), 4, 8, 'im'): -2.021772735121e-02,
    ((-1, 0, 0), 4, 10, 'im'): -1.453085104304e-02,
    ((-1, 0, 0), 8, 11, 'im'): -5.792024445345e-03,
    ((0, 0, 0), 0, 2, 're'): 5.000000000000e-01,
}


def orbit_basis(Mdl):
    """Deterministic O_h x translation invariant Hermitian basis of range |shift|_inf <= 1 one-fermion terms, as
    column-site-0 Bloch blocks.  Returns list of (representative, dict sh -> 12x12 block)."""
    VERTS = Mdl['VERTS']; VID = Mdl['C']['VID']; CORN = Mdl['CORN']; L = Mdl['L']; loc0 = Mdl['loc0']; CI = Mdl['CI']
    dmod = Mdl['dmod']
    shifts = list(itertools.product((-1, 0, 1), repeat=3))
    grp = Mdl['rots'] + Mdl['invs']
    def vid(sh, ci): return VID[(tuple(x % L for x in sh), CORN[ci])]
    sh_of = {i: tuple(dmod(x) for x in VERTS[i][0]) for i in range(len(VERTS))}
    def orbit_sum(sh, c1, c2, part):
        val = 1.0 if part == 're' else 1j
        B = {}
        def add(sh_, a, b, z):
            B.setdefault(sh_, np.zeros((12, 12), complex))[a, b] += z
        i0, j0 = vid(sh, c1), vid((0, 0, 0), c2)
        for P, s in grp:
            i, j = P[i0], P[j0]
            z = val * (-1.0) ** (int(s[i0]) + int(s[j0]))
            # j is at site 0 (rotations about site 0); entry (row i, column j)
            a, b = CI[VERTS[i][1]], CI[VERTS[j][1]]; shi = sh_of[i]
            add(shi, a, b, z)
            add(tuple(-x for x in shi), b, a, np.conj(z))          # Hermitian partner, translated to column site 0
        return B
    return shifts, orbit_sum


def part_D(Mdl, Mm, cases):
    print("\nPart D: the staggered pseudoscalar mass (C19 type) on the same models: clean massive vacuum at nu = 1?")
    Hk = Mdl['Hk']; kst = Mdl['kst']; Q = Mdl['Q']; blM = Mdl['blocks_from'](Mm)
    g = np.linspace(-np.pi, np.pi, 12, endpoint=False)
    G = np.array(list(itertools.product(g, g, g))) + 0.013
    out = {}
    for lab, (bl, masses) in cases.items():
        for m in masses:
            def ff(k): return np.linalg.eigvalsh(np.block([[Hk(bl, k), m * Hk(blM, k).conj().T], [m * Hk(blM, k), Hk(bl, k + Q)]]))
            e0 = ff(kst); direct = e0[2] - e0[1]
            E = np.array([ff(k)[:3] for k in G])
            i1 = np.argsort(-E[:, 1])[:6]; i2 = np.argsort(E[:, 2])[:6]
            c1 = [minimize(lambda k: -ff(k)[1], G[i], method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-13, maxiter=3000)) for i in i1]
            c2 = [minimize(lambda k: ff(k)[2], G[i], method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-13, maxiter=3000)) for i in i2]
            b1 = max(c1, key=lambda r: -r.fun); b2 = min(c2, key=lambda r: r.fun)
            top, bot = max(-b1.fun, e0[1]), min(b2.fun, e0[2])
            out[(lab, m)] = (direct, bot - top, b1.x, b2.x)
            print(f"   {lab}, m = {m}: direct gap at k* 2 m_D = {direct:.5f}; global gap (grid + local refinement) = {bot - top:+.5f}; "
                  f"top of band 1 at k/pi = {np.round(((b1.x + np.pi) % (2 * np.pi) - np.pi) / np.pi, 3)}, bottom of band 2 at k/pi = "
                  f"{np.round(((b2.x + np.pi) % (2 * np.pi) - np.pi) / np.pi, 3)}", flush=True)
    o = [out[('optimisation point', m)] for m in cases['optimisation point'][1]]
    check("numerical (grid + local refinement, not certified): with the staggered mass the optimisation point becomes a "
          "clean insulator at nu = 1 for both tested masses, but its global gap is smaller than the direct Dirac gap "
          "2 m_D at k*: the lowest excitation is not the Dirac fermion",
          all(g > 1e-3 and g < d - 1e-3 for d, g, _, _ in o), str([(round(d, 4), round(g, 4)) for d, g, _, _ in o]))
    d, gp, _, _ = out[('C20 metallic model', cases['C20 metallic model'][1][0])]
    check("numerical: the C20 metallic model with the small mass m = 0.02 stays metallic (negative global gap)",
          gp < -1e-3, f"global gap {gp:+.4f}")
    return out


def main():
    t_start = time.time()
    Mdl = build_model()
    nV = Mdl['nV']; sym = Mdl['sym']; loc0 = Mdl['loc0']; Hk = Mdl['Hk']; kst = Mdl['kst']
    # ---- the C19 conjugation-odd term family and the C20 metallic-model combination
    rng = np.random.default_rng(0)
    nbr = [Mdl['C']['VID'][(tuple(x % Mdl['L'] for x in d), c)] for d in [(0, 0, 0)] + list(Mdl['DIRS']) for c in Mdl['CORN']]
    seeds = []
    for trial in range(6):
        A = np.zeros((nV, nV))
        for i in loc0:
            for j in nbr:
                v, w = Mdl['VERTS'][i][0], Mdl['VERTS'][j][0]
                if i != j and sum(abs(Mdl['dmod'](y - x)) for x, y in zip(v, w)) <= 1: A[i, j] = rng.normal()
        A = A - A.T
        seeds.append(sym(1j * A, inversion=True))
    xv = np.random.default_rng(11).normal(size=6); xv /= np.linalg.norm(xv)
    X = np.tensordot(xv, np.array(seeds), 1); X /= np.abs(X).max()
    # ---- a pseudoscalar (imaginary A2, staggered) on-site mass as in C19
    A_ = np.random.default_rng(42).normal(size=(12, 12)); A_ = A_ - A_.T
    S = np.zeros((nV, nV), complex); S[np.ix_(loc0, loc0)] = 1j * A_
    Mm = sym(S, Qmom=True, a2=True); Mm = (Mm + Mm.conj().T) / 2; Mm /= np.abs(Mm).max()
    Hb = Mdl['H0'](-1.0, 0.2) + 0.05 * X
    ev, V = np.linalg.eigh(Hb); EN = np.linalg.eigvalsh(Hk(Mdl['blocks_from'](Hb), kst))[0]
    node = V[:, np.where(np.abs(ev - EN) < 1e-6)[0]]
    print(f"model: L = 4, X = normalized combination of six sampled invariant conjugation-odd terms (seed 11); "
          f"node space dimension {node.shape[1]}")
    part_A(Mdl, X, Mm)
    part_B(Mdl, X, Mm, node)
    models = {'C20 metallic model (t2 = 0.2, 0.05 X)': Mdl['blocks_from'](Hb),
              'C19 model (t2 = 0.2, 0.05 X_C19)': Mdl['blocks_from'](Mdl['H0'](-1.0, 0.2) + 0.05 * seeds[0] / np.abs(seeds[0]).max())}
    print("\nPart C0: invariant one-fermion terms of range |shift|_inf <= 1 and the supplied optimisation point")
    shifts, orbit_sum = orbit_basis(Mdl)
    counts = {'re': 0, 'im': 0}; seen = {'re': set(), 'im': set()}; obasis = []
    for sh in shifts:
        for c1 in range(12):
            for c2 in range(12):
                for part in ('re', 'im'):
                    if (sh, c1, c2) in seen[part]: continue
                    B = orbit_sum(sh, c1, c2, part)
                    ks = {(s_, a, b) for s_, Mb in B.items() for a, b in zip(*np.nonzero(np.abs(Mb) > 1e-12))}
                    seen[part] |= ks
                    if ks: counts[part] += 1; obasis.append(B)
    def vec(bl): return np.concatenate([bl.get(sh, np.zeros((12, 12), complex)).ravel() for sh in shifts])
    Bv = np.array([vec(B) for B in obasis]).T
    def in_span(bl):
        v = vec(bl); c = np.linalg.lstsq(Bv, v, rcond=None)[0]; return np.linalg.norm(Bv @ c - v) / np.linalg.norm(v)
    res_span = max(in_span(Mdl['blocks_from'](Mdl['H0'](-1.0, 0.0))), in_span(Mdl['blocks_from'](Mdl['H0'](0.0, 1.0))),
                   in_span(Mdl['blocks_from'](X)))
    check("exact orbit count: the O_h x translation invariant Hermitian one-fermion terms of range |shift|_inf <= 1 "
          "form a space of dimension 81 = 38 conjugation-even + 43 conjugation-odd (orbit sums of block entries); "
          "the two hoppings and X lie in it", counts == {'re': 38, 'im': 43} and res_span < 1e-10,
          f"{counts}, span residual {res_span:.1e}")
    blo = {}
    for (sh, c1, c2, part), cval in OPT_POINT.items():
        for s_, Mb in orbit_sum(sh, c1, c2, part).items(): blo[s_] = blo.get(s_, 0) + cval * Mb
    # real-space image of the optimisation point and its symmetry
    VID = Mdl['C']['VID']; L = Mdl['L']; Ho = np.zeros((nV, nV), complex)
    for v in Mdl['C']['SITES']:
        for sh, Mb in blo.items():
            rows = [VID[(tuple((x + y) % L for x, y in zip(v, sh)), c)] for c in Mdl['CORN']]
            cols = [VID[(v, c)] for c in Mdl['CORN']]
            Ho[np.ix_(rows, cols)] += Mb
    okH = np.allclose(Ho, Ho.conj().T) and all(np.allclose(conj(Ho, P, s), Ho) for P, s in Mdl['rots'] + Mdl['invs'][:1] + Mdl['trans'][:8])
    nreal = sum(1 for k in OPT_POINT if k[3] == 're')
    check("the supplied optimisation point (45 orbit coefficients: the two hoppings + 43 conjugation-odd terms; "
          "no other conjugation-even term) is a Hermitian, O_h- and translation-invariant lattice Hamiltonian",
          okH and nreal == 2 and len(OPT_POINT) == 45)
    models['optimisation point'] = blo
    part_C(Mdl, X, models)
    part_D(Mdl, Mm, {'C20 metallic model': (models['C20 metallic model (t2 = 0.2, 0.05 X)'], (0.02, 0.1)),
                     'optimisation point': (blo, (0.02, 0.05))})
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   ({time.time() - t_start:.0f} s)")
    raise SystemExit(1 if FAIL else 0)


if __name__ == '__main__':
    main()
