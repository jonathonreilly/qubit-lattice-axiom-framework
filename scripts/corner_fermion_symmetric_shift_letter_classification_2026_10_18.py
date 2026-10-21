#!/usr/bin/env python3
"""Bounded supplied-model controls. The canonical claim card and complete corrected argument define the current claim boundary. Finite obstruction certificates do not promote deferred terminal exclusions. Optional branches count only when executed.

Historical technical inventory (read with those corrected scope qualifications):
Corner fermion: classification of O-covariant shift letters.  The translation-invariant monomial letters are exactly
z S^a (A1) and z A0 S^a (A2); momentum-shifting letters (settled subclasses) and antiunitary letters (conjugation-closed
palette) reduce to old words;
among the pi/4 exponentials examined, only E+- = exp(+-i pi/4 R_L) is new.

Supplied model only (12-mode corner fermion; flux square = plaquette = tube = pi, triangle = 0; translation-invariant
gauge; gauge-dressed rotation lifts). No physical identification.

Self-contained: the model build is the campaign's from-scratch build (scale-ladder campaign, B26 check, mymodel.py), as
already ported into scripts/corner_fermion_generalised_speed_law_per_letter_additivity_2026_10_18.py; it is copied here,
not imported. Nothing is imported from the repository or from campaign packs.

Conventions: modes |v, c>, v in Z^3, c = {d, e} a corner (perpendicular unit pair); f_c = d + e.  A translation-invariant
operator is a block dict a -> X_a, X|v,c> = sum_a |v+a> X_a|c>, Bloch X(k) = sum_a X_a e^{+ik.a}.  A dressed rotation
acts by G|v,c> = (-1)^{lam.v + tau(c)} |Rv, Rc>, i.e. X_a -> (-1)^{lam.a} U_R X_a U_R^T at displacement Ra.

Sections
  0  model build and sanity
  1  B26 theorem: composition of the dressed lifts up to a global sign (connected hopping graph), chi in {A1, A2};
     stabiliser {1, C2'} of every corner; fixed corners {c, -c}, fixed displacements Z f_c; the two sign facts, and
     their gauge invariance under random gauge changes; Frobenius multiplicities; enumeration by twisted group
     averaging of single-entry seeds (a different algorithm from the check's orbit propagation)
  2  identities (exact block-dict equalities), palette maps, even-A reduction on random words, A_a X A_b formula,
     n_eff, D+ <-> D- swap
  3  C8 class 1: O-fixed momenta; D_Q covariance; D_Pi (anti)commutation and the Pi relation of old words; doubled-cell
     orbits and pieces; G0 (524,288 letters, 8 translation-invariant); a R_L b lemma (support over 128^2 perm pairs,
     Z4 enumeration, Smith normal form and kernel argument for U(1) phases)
  4  C8 class 2: reality of the letters, conjugation-closed palette, (VK)^2 = V V*, spectral pairing
  5  C8 class 3: exp(pi/4 A0) and exp(pi/4 A_a) only T-covariant; on-site involution exponentials in PC; E+-
     identities, O-symmetry, non-monomiality; Rt exponentials; E(k+Pi) = E-+(k); broken exact Pi relation; spectral
     Pi-taste of slot-free versus generic-slot E-words; exp(i theta R_L); D_Pi exponential; E at +-k*
Usage:  python3 <this file> [--slow]    default ~15 s on 2 threads; --slow (~20 s) enumerates to range 4 and
        enlarges samples.
Companion: docs/CORNER_FERMION_COVARIANT_MONOMIAL_SHIFT_LETTERS_ARE_ONLY_THE_DIAGONAL_SHIFT_POWERS_AND_THEIR_ANTIPODAL_TWINS_AND_THE_SETTLED_MOMENTUM_SHIFTING_AND_ANTIUNITARY_SUBCLASSES_REDUCE_TO_OLD_WORDS_BOUNDED_THEOREM_NOTE_2026-10-18.md
"""

# Owner capture binds these complete source/context identities before and after execution.
AUDIT_TIMEOUT_SEC = 600
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

import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "2")
import collections, itertools, sys, time
import numpy as np
from scipy.linalg import expm
import scipy.sparse as sp
import sympy
from sympy.matrices.normalforms import smith_normal_form

SLOW = '--slow' in sys.argv
T0 = time.time()
PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    ok = bool(ok); PASS += ok; FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


rng = np.random.default_rng(20261018)

# =====================================================================================================================
# Section 0: model build (copied from the campaign's independent build)
# =====================================================================================================================
print("=== 0. model build ===", flush=True)
DIRS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def neg(a): return tuple(-x for x in a)
def add(a, b): return tuple(x + y for x, y in zip(a, b))
CORN = sorted({frozenset((d, e)) for d in DIRS for e in DIRS if dot(d, e) == 0},
              key=lambda c: tuple(-x for x in add(*tuple(c))))
CI = {c: i for i, c in enumerate(CORN)}
FACE = np.array([add(*tuple(c)) for c in CORN])
ANTI = [CI[frozenset(neg(x) for x in c)] for c in CORN]
Z0 = (0, 0, 0)
def other(c, x): return [y for y in c if y != x][0]
def perp2(a, b): return [f for f in DIRS if dot(f, a) == 0 and dot(f, b) == 0]


def ekey(c1, c2, s):
    a = (CI[c1], CI[c2], tuple(s)); b = (CI[c2], CI[c1], neg(s)); return min(a, b)


ET = {}; ONSITE = []; LINK = []
for c in CORN:
    for x in c:
        y = other(c, x)
        for f in perp2(x, y):
            k_ = ekey(c, frozenset((x, f)), Z0)
            if k_ not in ET: ET[k_] = len(ET); ONSITE.append(k_)
        k_ = ekey(c, frozenset((neg(x), y)), x)
        if k_ not in ET: ET[k_] = len(ET); LINK.append(k_)
NT = len(ET)


def gf2_solve(A, b):
    A = np.array(A, np.uint8) % 2; b = np.array(b, np.uint8) % 2
    m, n = A.shape; M = np.concatenate([A, b[:, None]], 1); piv = []; r = 0
    for col in range(n):
        nz = [i for i in range(r, m) if M[i, col]]
        if not nz: continue
        M[[r, nz[0]]] = M[[nz[0], r]]
        for i in range(m):
            if i != r and M[i, col]: M[i] ^= M[r]
        piv.append(col); r += 1
        if r == m: break
    if M[r:, n].any(): return None, r, None
    x = np.zeros(n, np.uint8)
    for i, col in enumerate(piv): x[col] = M[i, n]
    kern = []
    for f in [j for j in range(n) if j not in piv]:
        v = np.zeros(n, np.uint8); v[f] = 1
        for i, col in enumerate(piv): v[col] = M[i, f]
        kern.append(v)
    return x, r, kern


def loop_row(seq):
    row = np.zeros(NT, np.uint8)
    for (c1, p1), (c2, p2) in zip(seq, seq[1:] + seq[:1]):
        row[ET[ekey(c1, c2, tuple(y - x for x, y in zip(p1, p2)))]] ^= 1
    return row


def ring(d):
    a0 = [f for f in DIRS if dot(f, d) == 0][0]; b0 = [f for f in DIRS if dot(f, d) == 0 and dot(f, a0) == 0][0]
    return [a0, b0, neg(a0), neg(b0)]


LOOPS = []   # (row, flux in units of pi)
for d in DIRS:
    rg = ring(d)
    LOOPS.append((loop_row([(frozenset((d, r)), Z0) for r in rg]), 1))                                  # square
    for i in range(4):
        p, q = rg[i], rg[(i + 1) % 4]
        LOOPS.append((loop_row([(frozenset((d, p)), Z0), (frozenset((neg(d), p)), d),
                                (frozenset((neg(d), q)), d), (frozenset((d, q)), Z0)]), 1))             # tube
for s in itertools.product((1, -1), repeat=3):
    x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
    LOOPS.append((loop_row([(frozenset((x, y)), Z0), (frozenset((y, z)), Z0), (frozenset((z, x)), Z0)]), 0))  # triangle
for d in DIRS:
    for e in DIRS:
        if dot(d, e) != 0: continue
        LOOPS.append((loop_row([(frozenset((d, e)), Z0), (frozenset((neg(d), e)), d),
                                (frozenset((neg(d), neg(e))), add(d, e)), (frozenset((d, neg(e))), e)]), 1))  # plaquette
u, LOOP_RANK, _ = gf2_solve([r for r, _ in LOOPS], [f for _, f in LOOPS])
# coboundary of translation-invariant gauge transformations (-1)^{mu.v + eps(c)}: edge (i1, i2, s) -> mu.s + eps(i1) + eps(i2)
COB = np.zeros((NT, 15), np.uint8)
for (i1, i2, s), t in ET.items():
    COB[t, :3] = np.array(s) % 2; COB[t, 3 + i1] ^= 1; COB[t, 3 + i2] ^= 1
_, COB_RANK, _ = gf2_solve(COB.T.copy(), np.zeros(15, np.uint8))
check("0.1 12 corners, 36 edge types (24 on-site, 12 link); the flux system (square = plaquette = tube = pi, triangle = 0) "
      "has a translation-invariant Z2 solution; loop rank 22 = 36 - 14 = 36 - rank(gauge coboundary), so every "
      "translation-invariant solution is gauge-equivalent to it",
      len(CORN) == 12 and NT == 36 and len(ONSITE) == 24 and len(LINK) == 12 and u is not None
      and all((r @ u) % 2 == f for r, f in LOOPS) and LOOP_RANK == 22 and COB_RANK == 14, f"loop rank {LOOP_RANK}, coboundary rank {COB_RANK}")


def all_oh():
    out = []
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3): M[i, p[i]] = sg[i]
            out.append(M)
    return out


OH = all_oh()
def rd(M, d): return tuple(int(x) for x in M @ np.array(d))
def rc(M, c): return frozenset(rd(M, d) for d in c)


def chiA2(M):
    p = [int(np.nonzero(M[i])[0][0]) for i in range(3)]
    return (-1) ** sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])


def psg(M, uu):
    A = []; b = []
    for (i1, i2, s), t in ET.items():
        row = np.zeros(15, np.uint8); row[:3] = np.array(s) % 2; row[3 + i1] ^= 1; row[3 + i2] ^= 1
        A.append(row); b.append(uu[t] ^ uu[ET[ekey(rc(M, CORN[i1]), rc(M, CORN[i2]), rd(M, s))]])
    x, _, kern = gf2_solve(A, b)
    return x, kern


PSG = []; psg_ok = True
for M in OH:
    x, kern = psg(M, u); psg_ok &= x is not None and len(kern) == 1
    PSG.append(dict(M=M, lam=x[:3].astype(int), tau=x[3:].astype(int)))
for g in PSG:
    U = np.zeros((12, 12))
    for c in CORN: U[CI[rc(g['M'], c)], CI[c]] = (-1.0) ** g['tau'][CI[c]]
    g['U'] = U; g['chi'] = chiA2(g['M']) if round(np.linalg.det(g['M'])) == 1 else None
    g['RC'] = [CI[rc(g['M'], CORN[c])] for c in range(12)]
PROPER = [g for g in PSG if round(np.linalg.det(g['M'])) == 1]
check("0.2 every one of the 48 O_h elements has a gauge-dressed lift (lam_R, tau_R) solving the PSG equations over GF(2), "
      "unique up to the global sign (kernel dimension 1)", psg_ok and len(PROPER) == 24)


def conjG(g, X):
    return {rd(g['M'], a): (-1.0) ** int(np.dot(g['lam'], a)) * g['U'] @ B @ g['U'].T for a, B in X.items()}


def bl_dist(X, Y, s=1.0):
    keys = set(X) | set(Y)
    return max([np.abs(X.get(a, 0) - s * Y.get(a, 0)).max() for a in keys] + [0.0])


def bl_eq(X, Y, s=1.0, tol=1e-12): return bl_dist(X, Y, s) < tol


def bloch(X, k):
    k = np.asarray(k, float); out = np.zeros((12, 12), complex)
    for a, B in X.items(): out += B * np.exp(1j * np.dot(k, a))
    return out


def bloch_grad(X, k):
    k = np.asarray(k, float)
    return [sum(B * 1j * a[j] * np.exp(1j * np.dot(k, a)) for a, B in X.items()) for j in range(3)]


def mul(*Xs):
    Z = Xs[0]
    for Y in Xs[1:]:
        W = {}
        for a, A in Z.items():
            for b, B in Y.items():
                c = add(a, b); W[c] = W.get(c, 0) + A @ B
        Z = {a: B for a, B in W.items() if np.abs(B).max() > 1e-13}
    return Z


def dag(X): return {neg(a): B.conj().T for a, B in X.items()}
def scal(z, X): return {a: z * B for a, B in X.items()}
I12 = np.eye(12, dtype=complex)
ONE = {Z0: I12}


def ham(kind):
    X = {}
    for (i1, i2, s) in (ONSITE if kind == 'on' else LINK):
        amp = -(-1.0) ** u[ET[(i1, i2, s)]]
        X.setdefault(s, np.zeros((12, 12), complex))[i2, i1] += amp
        X.setdefault(neg(s), np.zeros((12, 12), complex))[i1, i2] += amp
    return X


HON = ham('on'); HLINK = ham('link')
RL = {a: B / np.sqrt(2) for a, B in HLINK.items()}
LAM = np.zeros((12, 12), complex)
for sg in itertools.product((1, -1), repeat=3):
    x, y, z = (sg[0], 0, 0), (0, sg[1], 0), (0, 0, sg[2])
    cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
    if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
    for a_ in range(3):
        q, r = cy[a_], cy[(a_ + 1) % 3]
        amp = 1j * (-1.0) ** u[ET[ekey(q, r, Z0)]]
        LAM[CI[r], CI[q]] += amp; LAM[CI[q], CI[r]] += np.conj(amp)


def orbit_solve(target_of, chi_fn, c0=0):
    """Monomial letter: column c -> (row target_of(c)[0], displacement target_of(c)[1]), coefficient fixed by covariance."""
    z = {c0: 1.0 + 0j}; changed = True
    while changed:
        changed = False
        for g in PROPER:
            for c in list(z):
                i, a = target_of(c); Rc = g['RC'][c]
                val = (-1.0) ** (int(np.dot(g['lam'], a)) + g['tau'][c] + g['tau'][i]) * z[c] / chi_fn(g)
                i2, a2 = target_of(Rc)
                if (g['RC'][i], rd(g['M'], a)) != (i2, a2): return None
                if Rc in z:
                    if abs(z[Rc] - val) > 1e-12: return None
                else: z[Rc] = val; changed = True
    X = {}
    for c, zc in z.items():
        i, a = target_of(c); X.setdefault(a, np.zeros((12, 12), complex))[i, c] += zc
    return X


c_xy = CI[frozenset(((1, 0, 0), (0, 1, 0)))]
S1 = orbit_solve(lambda c: (c, tuple(FACE[c])), lambda g: 1, c0=c_xy)          # diagonal shift {d,e}@v -> v+d+e
A0X = orbit_solve(lambda c: (ANTI[c], Z0), lambda g: g['chi'], c0=c_xy)          # antipodal on-site map (A2)
SDIAG = np.array([S1[tuple(FACE[c])][c, c] for c in range(12)])
def Sk(k, p=1): return np.diag(SDIAG ** p * np.exp(1j * p * FACE @ np.asarray(k, float)))


def Spow(p):
    X = {}
    for c in range(12):
        a = tuple(int(x) for x in p * FACE[c]); X.setdefault(a, np.zeros((12, 12), complex))[c, c] = SDIAG[c] ** p
    return X


A0 = A0X[Z0]; A0i = A0.conj().T
A0D = {Z0: A0}; A0iD = {Z0: A0i}
RTX = mul(A0D, RL, A0iD)                                                         # Rt = A0 R_L A0^-1
HON0 = bloch(HON, np.zeros(3))
LAMD = {Z0: LAM}; HOND = {Z0: HON0}


def eigsp(M, lam):
    w, V = np.linalg.eigh(M); return V[:, np.abs(w - lam) < 1e-6]


def eproj(M):
    w, V = np.linalg.eigh(M); ls = sorted(set(np.round(w, 6)))
    return ls, [V[:, np.abs(w - l) < 1e-6] @ V[:, np.abs(w - l) < 1e-6].conj().T for l in ls]


DPM = eigsp(HON0, 2.0)
DP = DPM @ eigsp(DPM.conj().T @ LAM @ DPM, -2 * np.sqrt(2))
DM = DPM @ eigsp(DPM.conj().T @ LAM @ DPM, 2 * np.sqrt(2))
HEV, PH = eproj(HON0); LEV, PL = eproj(LAM)
PHASE = [1, 1j, -1, -1j]
PC = {f"H{a}{b}": PH[0] + PHASE[a] * PH[1] + PHASE[b] * PH[2] for a in range(4) for b in range(4)}
PC.update({f"L{a}{b}{c}": PL[0] + PHASE[a] * PL[1] + PHASE[b] * PL[2] + PHASE[c] * PL[3]
           for a in range(4) for b in range(4) for c in range(4)})
_sv = np.linalg.svd(np.vstack([np.kron(g['U'], g['U']) - np.eye(144) for g in PROPER]))
ONB = [v.reshape(12, 12) for v in _sv[2][np.sum(_sv[1] > 1e-9):].conj()]        # symmetric on-site algebra (commutant)


def rand_onsite_unitary(rng):
    H = sum(rng.normal() * B + rng.normal() * 1j * B for B in ONB); H = (H + H.conj().T) / 2
    w, V = np.linalg.eigh(H); return V @ np.diag(np.exp(1j * w * 3.0)) @ V.conj().T


kr = rng.uniform(-np.pi, np.pi, 3)
s3 = np.sqrt(3); s2 = np.sqrt(2)
evon = np.sort(np.linalg.eigvalsh(HON0)); evl = np.sort(np.linalg.eigvalsh(LAM))
ok_on = np.all(np.min(np.abs(evon[:, None] - np.array([-1 - s3, s3 - 1, 2.0])[None]), 1) < 1e-9)
ok_l = np.all(np.min(np.abs(evl[:, None] - np.array([-2 * s2, -s2, s2, 2 * s2])[None]), 1) < 1e-9)
check("0.3 H_on has spectrum {-1-sqrt3, sqrt3-1, 2}, Lambda has {+-sqrt2, +-2sqrt2}; R_L^2 = 1 exactly as a block dict; "
      "symmetric on-site algebra has dimension 6; D+ = {H_on = 2, Lambda = -2sqrt2}, D- = {H_on = 2, Lambda = +2sqrt2} are 2-dim",
      ok_on and ok_l and bl_eq(mul(RL, RL), ONE) and len(ONB) == 6 and DP.shape == (12, 2) and DM.shape == (12, 2))
KST = np.array([1, -1, 1]) * np.pi / 2
PI3 = np.pi * np.ones(3)
def wrap(x): return np.angle(np.exp(1j * np.asarray(x)))
print(f"   section 0: {time.time() - T0:.1f}s")

# =====================================================================================================================
# Section 1: B26 theorem
# =====================================================================================================================
print("\n=== 1. B26: translation-invariant monomial letters covariant up to a 1-d character ===", flush=True)
t1 = time.time()
IDX = {tuple(g['M'].ravel()): n for n, g in enumerate(PROPER)}
def gmul(g, h): return PROPER[IDX[tuple((g['M'] @ h['M']).ravel())]]


okc = True
for g in PROPER:
    for h in PROPER:
        gh = gmul(g, h)
        lam = (h['lam'] + h['M'].T @ g['lam']) % 2
        tau = np.array([(h['tau'][c] + g['tau'][h['RC'][c]]) % 2 for c in range(12)])
        okc &= np.array_equal(lam, gh['lam'] % 2) and len(set((tau - gh['tau']) % 2)) == 1
check("1.1a the dressed lifts compose up to a GLOBAL sign: G_g G_h G_gh^-1 = (-1)^{(lam_h + R_h^T lam_g - lam_gh).v + "
      "(tau_h(c) + tau_g(R_h c) - tau_gh(c))} has zero lam part and constant tau part (all 24^2 pairs)", okc)
# mechanism: the defect is a gauge transformation preserving every edge sign; the hopping graph is connected
adj = {c: set() for c in range(12)}
for (i1, i2, s) in ONSITE: adj[i1].add(i2); adj[i2].add(i1)
seen = {0}; stack = [0]
while stack:
    c = stack.pop()
    for d_ in adj[c] - seen: seen.add(d_); stack.append(d_)
link_axes = {tuple(int(abs(x)) for x in s) for (_, _, s) in LINK}
check("1.1b the hopping graph is connected (the 12 corners are connected by on-site edges, and link edges run along all "
      "three axes), so a gauge transformation preserving every edge sign is constant: this is why the defect is global",
      len(seen) == 12 and link_axes == {(1, 0, 0), (0, 1, 0), (0, 0, 1)})
Xr = {a: rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12)) for a in itertools.product((-1, 0, 1), repeat=3)}
okrep = all(bl_eq(conjG(g, conjG(h, Xr)), conjG(gmul(g, h), Xr), tol=1e-10) for g in PROPER for h in PROPER)
comm = {tuple((g['M'] @ h['M'] @ g['M'].T @ h['M'].T).ravel()) for g in PROPER for h in PROPER}
grp = set(comm); changed = True
while changed:
    new = {tuple((np.array(a).reshape(3, 3) @ np.array(b).reshape(3, 3)).ravel()) for a in grp for b in grp} - grp
    changed = bool(new); grp |= new
kerA2 = {tuple(g['M'].ravel()) for g in PROPER if g['chi'] == 1}
okhom = all(gmul(g, h)['chi'] == g['chi'] * h['chi'] for g in PROPER for h in PROPER)
check("1.2 hence Ad(G) is a true representation on translation-invariant operators (random range-1 X); the commutator "
      "subgroup of O has order 12 and equals ker A2, so the 1-d characters of O are exactly A1 and A2; A2 is a homomorphism",
      okrep and grp == kerA2 and len(grp) == 12 and okhom)
okst = True; C2P = {}
for c in range(12):
    st = [g for g in PROPER if g['RC'][c] == c]
    h = [g for g in st if not np.array_equal(g['M'], np.eye(3, dtype=int))]
    if len(st) != 2 or len(h) != 1: okst = False; continue
    h = h[0]; C2P[c] = h; M = h['M']
    okst &= np.array_equal(M @ M, np.eye(3, dtype=int)) and round(np.trace(M)) == -1 and np.array_equal(M @ FACE[c], FACE[c])
    okst &= sorted(i for i in range(12) if h['RC'][i] == i) == sorted({c, ANTI[c]})
    fixed = [a for a in itertools.product(range(-4, 5), repeat=3) if rd(M, a) == a]
    okst &= set(fixed) == {tuple(int(x) for x in t * FACE[c]) for t in range(-4, 5)}
    okst &= h['chi'] == -1
check("1.3 for every corner c: Stab_O(c@0) = {1, h_c} with h_c the C2' about f_c = d + e (h^2 = 1, trace -1); its fixed "
      "corners are exactly {c, -c}; its fixed lattice vectors in [-4,4]^3 are exactly t f_c; A2(h_c) = -1", okst and len(C2P) == 12)


def sign_facts(PS):
    out = []
    for c in range(12):
        h = [g for g in PS if round(np.linalg.det(g['M'])) == 1 and g['RC'][c] == c and not np.array_equal(g['M'], np.eye(3, dtype=int))][0]
        out.append((int(np.dot(h['lam'], FACE[c])) % 2, (h['tau'][c] + h['tau'][ANTI[c]]) % 2))
    return out


SF = sign_facts(PROPER)
check("1.4 the two model sign facts, all 12 corners: (a) lam_{h_c}.f_c is even, so S^t is A1 for every t; (b) "
      "tau_{h_c}(c) + tau_{h_c}(-c) is odd, so with A2(h_c) = -1 the letter A0 S^t is A2 for every t",
      all(a == 0 and b == 1 for a, b in SF))
okg = True; nchanged = 0
for trial in range(3):
    mu = rng.integers(0, 2, 3); eps = rng.integers(0, 2, 12)
    u2 = np.array([u[t] ^ (int(np.dot(mu, np.array(s) % 2)) % 2) ^ eps[i1] ^ eps[i2] for (i1, i2, s), t in ET.items()], np.uint8)
    PS2 = []
    for g in PSG:
        x, _ = psg(g['M'], u2)
        PS2.append(dict(M=g['M'], lam=x[:3].astype(int), tau=x[3:].astype(int), RC=g['RC']))
    okg &= sign_facts(PS2) == SF
    nchanged += any(not np.array_equal(a['tau'], b['tau']) or not np.array_equal(a['lam'], b['lam']) for a, b in zip(PS2, PSG))
check("1.5 the sign facts are gauge-invariant: three random translation-invariant gauge changes (-1)^{mu.v + eps(c)} change "
      "the lifts (lam, tau) but not the two parities", okg and nchanged == 3)
okdec = True
for t in range(-2, 3):
    for tgt in ('same', 'anti'):
        def T_(c): return (c if tgt == 'same' else ANTI[c], tuple(int(x) for x in t * FACE[c]))
        Ms = []
        for g in PROPER:
            Mg = np.zeros((12, 12))
            for c in range(12):
                i, a = T_(c); Mg[g['RC'][c], c] = (-1.0) ** (int(np.dot(g['lam'], a)) + g['tau'][c] + g['tau'][i])
            Ms.append(Mg)
        rA1 = np.linalg.matrix_rank(sum(Ms) / 24); rA2 = np.linalg.matrix_rank(sum(g['chi'] * M for g, M in zip(PROPER, Ms)) / 24)
        okdec &= (rA1, rA2) == ((1, 0) if tgt == 'same' else (0, 1))
check("1.6 Frobenius: on each 12-dim support space (c -> c or c -> -c at displacement t f_c, t = -2..2) the (A1, A2) "
      "multiplicities are (1, 0) and (0, 1)", okdec)


def avg_seed(i, c0, a, chi_name):
    """twisted group average (1/24) sum_g chi(g) G_g E G_g^-1 of the single entry E = |a, i><0, c0|"""
    acc = {}
    for g in PROPER:
        ch = 1 if chi_name == 'A1' else g['chi']
        key = (g['RC'][i], g['RC'][c0], rd(g['M'], a))
        acc[key] = acc.get(key, 0) + ch * (-1.0) ** (int(np.dot(g['lam'], a)) + g['tau'][c0] + g['tau'][i]) / 24
    ent = {k_: v for k_, v in acc.items() if abs(v) > 1e-12}
    if not ent: return None
    cols = collections.Counter(k_[1] for k_ in ent)
    if sorted(cols) != list(range(12)) or max(cols.values()) != 1: return 'non-monomial'
    X = {}
    for (r, cc, aa), v in ent.items(): X.setdefault(aa, np.zeros((12, 12), complex))[r, cc] += v
    return X


SPOW = {}; ASPOW = {}
RMAX = 4 if SLOW else 3
for t in range(-RMAX, RMAX + 1): SPOW[t] = Spow(t); ASPOW[t] = mul(A0D, Spow(t))
for R in range(1, RMAX + 1):
    found = []; nseed = 0; nnon = 0; nzero = 0
    for a in itertools.product(range(-R, R + 1), repeat=3):
        for i in range(12):
            nseed += 1
            for chn in ('A1', 'A2'):
                X = avg_seed(i, c_xy, a, chn)
                if X is None: nzero += 1
                elif isinstance(X, str): nnon += 1
                else: found.append((a, i, chn, X))
    okid = True; kinds = []
    for a, i, chn, X in found:
        t = int(round(np.dot(a, FACE[c_xy]) / 2)); ref = SPOW[t] if i == c_xy else ASPOW[t]
        z = X[a][i, c_xy] / ref[a][i, c_xy]
        okid &= bl_eq(X, ref, z) and all(bl_eq(conjG(g, X), X, 1 if chn == 'A1' else g['chi']) for g in PROPER)
        kinds.append((t, 'same' if i == c_xy else ('anti' if i == ANTI[c_xy] else 'other'), chn))
    expect = sorted([(t, 'same', 'A1') for t in range(-R, R + 1)] + [(t, 'anti', 'A2') for t in range(-R, R + 1)])
    check(f"1.7 range <= {R} (sup norm): {nseed} single-entry seeds x {{A1, A2}} twisted group averages -> exactly "
          f"{len(found)} monomial letters, = z S^t (A1) and z A0 S^t (A2) for |t| <= {R}",
          sorted(kinds) == expect and okid, f"{nzero} averages vanish, {nnon} non-monomial")
okSA = all(bl_eq(conjG(g, S1), S1) and bl_eq(conjG(g, A0D), A0D, g['chi']) for g in PROPER)
check("1.8 S is A1 and A0 is A2 under all 24 dressed rotations; S and A0 S^t are unitary (entries of modulus 1)",
      okSA and np.allclose(np.abs(SDIAG), 1) and np.allclose(A0 @ A0i, np.eye(12)))
print(f"   section 1: {time.time() - t1:.1f}s")

# =====================================================================================================================
# Section 2: identities, even-A reduction, D+- swap
# =====================================================================================================================
print("\n=== 2. identities (exact block-dict equalities) and the even-A reduction ===", flush=True)
t1 = time.time()
Sm1 = Spow(-1)
check("2.1 A0 is a real signed permutation c -> -c with A0^2 = -1 (real normalisation)",
      np.abs(A0.imag).max() == 0 and all(abs(A0[ANTI[c], c]) == 1 for c in range(12)) and np.allclose(A0 @ A0, -np.eye(12), atol=0))
dS = max(bl_dist(mul(A0D, Spow(p), A0iD), Spow(-p)) for p in (1, 2, 3))
check("2.2 A0 S^p A0^-1 = S^-p (p = 1, 2, 3)", dS < 1e-15, f"residual {dS:.0e}")
d1 = bl_dist(RTX, scal(-1, mul(S1, RL, Sm1))); d2 = bl_dist(RTX, scal(-1, mul(Sm1, RL, S1))); d3 = bl_dist(RTX, mul(S1, RL, Sm1))
check("2.3 A0 R_L A0^-1 = -S R_L S^-1 (the alternatives -S^-1 R_L S and +S R_L S^-1 fail)", d1 < 1e-15 and d2 > 0.5 and d3 > 0.5,
      f"residual {d1:.0e}; alternatives {d2:.2f}, {d3:.2f}")
dA = bl_dist(mul(A0D, RTX, A0iD), RL); dB = bl_dist(mul(Sm1, RTX, S1), scal(-1, RL))
dC = bl_dist(mul(RTX, RTX), ONE); dD = bl_dist(RTX, dag(RTX)); dE = min(bl_dist(RTX, RL), bl_dist(RTX, scal(-1, RL)))
check("2.4 Rt = A0 R_L A0^-1: A0 Rt A0^-1 = +R_L (from A0^2 = -1), S^-1 Rt S = -R_L (a restatement of 2.3), Rt^2 = 1, "
      "Rt Hermitian, Rt != +-R_L", max(dA, dB, dC, dD) < 1e-15 and dE > 0.5, f"{dA:.0e} {dB:.0e} {dC:.0e} {dD:.0e}; {dE:.2f}")
check("2.5 A0 H_on A0^-1 = H_on and A0 Lambda A0^-1 = -Lambda",
      np.abs(A0 @ HON0 @ A0i - HON0).max() < 1e-15 and np.abs(A0 @ LAM @ A0i + LAM).max() < 1e-15)


def find_in(M, pal):
    for n, B in pal.items():
        z = np.vdot(B.ravel(), M.ravel()) / 12
        if abs(abs(z) - 1) < 1e-10 and np.allclose(M, z * B): return n, z
    return None, None


okpal = True; zs = set()
for n, B in PC.items():
    m, z = find_in(A0 @ B @ A0i, PC); okpal &= m is not None
    if m is not None: zs.add(complex(np.round(z, 9)))
okalg = all(all(np.allclose(g['U'] @ (A0 @ B @ A0i) @ g['U'].T, A0 @ B @ A0i) for g in PROPER) for B in ONB)
check("2.6 A0 maps the 80-letter Clifford palette PC onto itself up to phases in {+-1, +-i}, and the 6-dim symmetric "
      "on-site algebra into itself", okpal and zs <= {1, -1, 1j, -1j} and okalg, f"phases {sorted(zs, key=lambda q: (q.real, q.imag))}")
PCL = list(PC)


def letter(tok, k):
    if tok[0] == 'S': return Sk(k, tok[1])
    if tok[0] == 'R': return bloch(RL, k)
    if tok[0] == 'Rt': return bloch(RTX, k)
    if tok[0] == 'A': return A0 @ Sk(k, tok[1])
    return tok[1]


def word(w, k):
    M = I12.copy()
    for t in w: M = M @ letter(t, k)
    return M


def reduce_word(w):
    """even-A word -> (sign, word in S^p, R_L, on-site) via A0 X A0 = -X~, Rt = -S R_L S^-1, R_L~ = Rt, Rt~ = R_L"""
    out = []; par = 0; sign = 1
    for t in w:
        if t[0] == 'A':
            if par == 1: sign *= -1
            par ^= 1; t = ('S', t[1])
        if par:
            if t[0] == 'S': out.append(('S', -t[1]))
            elif t[0] == 'R': sign *= -1; out += [('S', 1), ('R',), ('S', -1)]
            elif t[0] == 'Rt': out.append(('R',))
            else: out.append(('U', A0 @ t[1] @ A0i))
        else:
            if t[0] == 'Rt': sign *= -1; out += [('S', 1), ('R',), ('S', -1)]
            else: out.append(t)
    assert par == 0
    return sign, out


def neff(w):
    n = 0; par = 0
    for t in w:
        if t[0] == 'A': par ^= 1; n += (-1) ** par * t[1]
        elif t[0] == 'S': n += (-1) ** par * t[1]
    return n


def rand_word(rng, nA):
    L = rng.integers(3, 9); toks = []
    for _ in range(L):
        r = rng.integers(0, 4)
        if r == 0: toks.append(('S', int(rng.choice([-2, -1, 1, 2]))))
        elif r == 1: toks.append(('R',) if rng.random() < .5 else ('Rt',))
        else: toks.append(('U', rand_onsite_unitary(rng) if rng.random() < .5 else PC[PCL[rng.integers(80)]]))
    for _ in range(nA): toks.insert(int(rng.integers(0, len(toks) + 1)), ('A', int(rng.integers(-2, 3))))
    return toks


NRED = 600 if SLOW else 300
okred = True; maxd = 0; okn = True
for trial in range(NRED):
    w = rand_word(rng, 2 * int(rng.integers(1, 3)))
    s_, wo = reduce_word(w)
    for k in rng.uniform(-np.pi, np.pi, (3, 3)):
        maxd = max(maxd, np.abs(word(w, k) - s_ * word(wo, k)).max())
    okred &= all(t[0] in ('S', 'R', 'U') for t in wo)
    okn &= sum(t[1] for t in wo if t[0] == 'S') == neff(w)
check(f"2.7 even-A reduction: {NRED} random words with 2 or 4 letters A_a = A0 S^a (a = -2..2) among S^p, R_L, Rt and "
      "random symmetric on-site / PC letters equal +-(word in S^p, R_L and symmetric on-site letters); the reduced total "
      "S power is n_eff = sum (-1)^{#A0 to the left} p", okred and okn and maxd < 1e-12, f"max deviation {maxd:.1e}")
okf = True
for a, b in itertools.product(range(-2, 3), repeat=2):
    w = rand_word(rng, 0); k = rng.uniform(-np.pi, np.pi, 3)
    X = word(w, k); Xt = A0 @ X @ A0i
    okf &= np.allclose(A0 @ Sk(k, a) @ X @ A0 @ Sk(k, b), -Sk(k, -a) @ Xt @ Sk(k, b), atol=1e-12)
check("2.8 A_a X A_b = -S^-a X~ S^b with X~ = A0 X A0^-1 (random A-free words X, all a, b in -2..2)", okf)
okswap = True
for a in range(-2, 3):
    for k0 in (KST, -KST):
        A = A0 @ Sk(k0, a)
        okswap &= np.linalg.norm(DP.conj().T @ A @ DP) < 1e-12 and np.linalg.norm(DM.conj().T @ A @ DM) < 1e-12
        okswap &= abs(np.linalg.norm(DM.conj().T @ A @ DP) ** 2 - 2) < 1e-12 and abs(np.linalg.norm(DP.conj().T @ A @ DM) ** 2 - 2) < 1e-12
oksc = True
for X in (S1, RL, RTX, HOND, LAMD, {Z0: rand_onsite_unitary(rng)}):
    for k0 in (KST, -KST):
        M = bloch(X, k0)
        for D in (DP, DM):
            c = D.conj().T @ M @ D
            oksc &= np.linalg.norm(M @ D - D @ c) < 1e-12 and np.allclose(c, c[0, 0] * np.eye(2), atol=1e-12)
check("2.9 D+- swap: every A_a (a = -2..2) maps D+ onto D- and D- onto D+ at +k* and -k*; the A1 letters S, R_L, Rt, "
      "H_on, Lambda and a random symmetric on-site unitary act as scalars on D+ and on D-", okswap and oksc)
print(f"   section 2: {time.time() - t1:.1f}s")

# =====================================================================================================================
# Section 3: C8 class 1, momentum-shifting and doubled-cell letters
# =====================================================================================================================
print("\n=== 3. C8 class 1: momentum-shifting letters ===", flush=True)
t1 = time.time()
fixed = set()
for N in (8, 12):
    n = np.array(list(itertools.product(range(2 * N), repeat=3))); Q = n * np.pi / N
    ok_all = np.ones(len(Q), bool)
    for g in PROPER:
        diff = (Q @ g['M'].T - Q) / (2 * np.pi); ok_all &= np.all(np.abs(diff - np.round(diff)) < 1e-9, axis=1)
    fixed |= {tuple(np.round(q / np.pi, 6)) for q in Q[ok_all]}
check("3.1 O-fixed momenta on the (pi/8)Z^3 and (pi/12)Z^3 grids of R^3/2piZ^3 are exactly 0 and Pi = pi(1,1,1) (the "
      "general-Q statement is proved by hand: C4 about each axis forces Q_i in {0, pi} and Q_i = Q_j)",
      fixed == {(0.0, 0.0, 0.0), (1.0, 1.0, 1.0)}, f"{sorted(fixed)}")
# L = 4 torus, modes (v, c) -> 12 * site + c
L4 = 4
SITES = list(itertools.product(range(L4), repeat=3))
def sidx(v): return ((v[0] % L4) * L4 + v[1] % L4) * L4 + v[2] % L4
NM = len(SITES) * 12
MV = np.array([v for v in SITES for c in range(12)]); MC = np.array([c for v in SITES for c in range(12)])


def real4(X):
    rows, cols, vals = [], [], []
    for v in SITES:
        for a, B in X.items():
            w = sidx(add(v, a))
            for i, c in zip(*np.nonzero(np.abs(B) > 1e-14)):
                rows.append(12 * w + i); cols.append(12 * sidx(v) + c); vals.append(B[i, c])
    return sp.csr_matrix((vals, (rows, cols)), shape=(NM, NM), dtype=complex)


def elem(g, t=(0, 0, 0)):
    perm = np.zeros(NM, int); sg = np.zeros(NM)
    for v in SITES:
        w = add(rd(g['M'], v), t); lv = (-1.0) ** int(np.dot(g['lam'], v))
        for c in range(12):
            perm[12 * sidx(v) + c] = 12 * sidx(w) + g['RC'][c]; sg[12 * sidx(v) + c] = lv * (-1.0) ** g['tau'][c]
    return perm, sg


def sp_of(perm, sg): return sp.csr_matrix((sg, (perm, np.arange(NM))), shape=(NM, NM))
def DQ(q): return np.array([(-1.0) ** int(np.dot(q, v)) for v in SITES for c in range(12)])
SUBL = list(itertools.product((0, 1), repeat=3))
GEL = [elem(g) for g in PROPER]
okD = True
for (perm, sg), g in zip(GEL, PROPER):
    for q in SUBL:
        Rq = tuple(int(x) % 2 for x in g['M'] @ np.array(q)); D = DQ(q); Dr = np.zeros(NM); Dr[perm] = D
        okD &= np.array_equal(Dr, DQ(Rq))
orbs = {frozenset(tuple(int(x) % 2 for x in g['M'] @ np.array(q)) for g in PROPER) for q in SUBL}
check("3.2 G_g D_Q G_g^-1 = D_{RQ} exactly for 24 dressed rotations x 8 Q in pi{0,1}^3 (the gauge signs cancel); the "
      "O-orbits of pi{0,1}^3 have sizes [1, 1, 3, 3], so D_0 = 1 and D_Pi are the only O-invariant ones",
      okD and sorted(len(o) for o in orbs) == [1, 1, 3, 3])
DPI = sp.diags(DQ((1, 1, 1)))
LETS4 = {'S': real4(S1), 'A0': real4(A0D), 'H_on': real4(HOND), 'Lambda': real4(LAMD), 'PC L123': real4({Z0: PC['L123']}),
         'random on-site': real4({Z0: rand_onsite_unitary(rng)}), 'R_L': real4(RL), 'Rt': real4(RTX)}
def relD(M): return 'comm' if abs(DPI @ M - M @ DPI).max() < 1e-13 else ('anti' if abs(DPI @ M + M @ DPI).max() < 1e-13 else 'neither')
res = {n: relD(M) for n, M in LETS4.items()}
check("3.3 D_Pi commutes with S, A0, H_on, Lambda, PC and symmetric on-site letters, and anticommutes with R_L and Rt "
      "(S hops by f_c, of even coordinate sum; R_L hops by unit vectors)",
      res == {'S': 'comm', 'A0': 'comm', 'H_on': 'comm', 'Lambda': 'comm', 'PC L123': 'comm', 'random on-site': 'comm',
              'R_L': 'anti', 'Rt': 'anti'}, f"{res}")
okP = True
for _ in range(200):
    n = rng.integers(2, 7); toks = [str(x) for x in rng.choice(['R', 'Rt', 'S', 'Si', 'S2', 'A', 'o'], n)]
    w = []
    for t in toks:
        w.append({'R': ('R',), 'Rt': ('Rt',), 'S': ('S', 1), 'Si': ('S', -1), 'S2': ('S', 2), 'A': ('A', int(rng.integers(-2, 3)))}.get(t)
                 or ('U', rand_onsite_unitary(rng)))
    nR = sum(1 for t in w if t[0] in ('R', 'Rt')); k = rng.uniform(-np.pi, np.pi, 3)
    okP &= np.allclose(word(w, k + PI3), (-1) ** nR * word(w, k), atol=1e-12)
check("3.4 k* + Pi = -k* mod 2pi, and every word in S^p, R_L, Rt, A_a and symmetric on-site letters obeys W(k+Pi) = "
      "(-1)^{n_R} W(k) (200 random): the D_Pi relation is the known Pi-taste",
      np.allclose(wrap(KST + PI3 + KST), 0) and okP)
# ---------- doubled cell: O x (2Z/4Z)^3 on the L = 4 torus
ELEM = []
for g in PROPER:
    for t in itertools.product((0, 2), repeat=3):
        p, s_ = elem(g, t); ELEM.append((p, s_, g['chi']))
seen = np.zeros(NM, bool); ORB = []; ORBOF = np.zeros(NM, int)
for i in range(NM):
    if seen[i]: continue
    o = sorted(set(int(p[i]) for p, _, _ in ELEM)); seen[o] = True; ORBOF[o] = len(ORB); ORB.append(o)


def desc(o):
    v = MV[o[0]]; c = MC[o[0]]; s_ = tuple(int(x) % 2 for x in v); w = sum(s_)
    if w in (0, 3): typ = 'none'
    else:
        ax = [i for i in range(3) if s_[i] == (1 if w == 1 else 0)][0]
        typ = 'par' if any(abs(d[ax]) == 1 for d in CORN[c]) else 'perp'
    stab = sum(1 for p, _, _ in ELEM if p[o[0]] == o[0])
    return (w, typ, len(o) // 8, stab)


DESC = [desc(o) for o in ORB]
print("   orbits (sublattice weight, corner type, modes per doubled cell, stabiliser order):", sorted(DESC))
okc2 = True
for o, d_ in zip(ORB, DESC):
    if d_[2] != 12: continue
    Ms = [PROPER[k_ // 8]['M'] for k_, (p, _, _) in enumerate(ELEM) if p[o[0]] == o[0]]
    nt = [M for M in Ms if not np.array_equal(M, np.eye(3, dtype=int))]
    okc2 &= len(nt) == 1 and np.array_equal(nt[0] @ nt[0], np.eye(3, dtype=int)) and round(np.trace(nt[0])) == -1 and np.count_nonzero(nt[0]) == 3 and not np.array_equal(np.abs(nt[0]), np.eye(3, dtype=int))
check("3.5 doubled cell (O x 2Z^3, 192 signed permutations): 6 mode orbits per doubled cell, sizes 12, 12, 12, 12, 24, 24 "
      "(000, 111, 100-perp, 110-perp with stabiliser {1, C2'}; 100-par, 110-par free)",
      len(ELEM) == 192 and sorted(DESC) == sorted([(0, 'none', 12, 2), (3, 'none', 12, 2), (1, 'perp', 12, 2), (2, 'perp', 12, 2),
                                                   (1, 'par', 24, 1), (2, 'par', 24, 1)]) and okc2)


def piece(src, tgt, twist):
    col = {}
    for p, sg, ch in ELEM:
        w = (ch if twist else 1) * sg[tgt] * sg[src]
        a, b = int(p[src]), int(p[tgt])
        if a in col:
            if col[a][0] != b or abs(col[a][1] - w) > 1e-9: return None
        else: col[a] = (b, w)
    rows = [b for b, _ in col.values()]
    return col if len(set(rows)) == len(rows) else None


cnt = {}; R0 = {}
for oi, o in enumerate(ORB):
    src = o[0]; vs = tuple(MV[src]); n = 0; n0 = collections.Counter(); r0 = collections.defaultdict(list)
    for a in itertools.product((-1, 0, 1), repeat=3):
        for c in range(12):
            tgt = 12 * sidx(add(vs, a)) + c
            for tw in (False, True):
                pc = piece(src, tgt, tw)
                if pc is not None:
                    n += 1
                    if a == Z0: n0[tw] += 1; r0[tw].append(pc)
    cnt[oi] = (n, dict(n0)); R0[oi] = r0
okp = all((cnt[oi][0] == 6 and cnt[oi][1] == {False: 1, True: 1}) if DESC[oi][2] == 12 else
          (cnt[oi][0] == 336 and cnt[oi][1] == {False: 8, True: 8}) for oi in range(6))
okid = all(MC[R0[oi][tw][0][ORB[oi][0]][0]] == (ANTI[MC[ORB[oi][0]]] if tw else MC[ORB[oi][0]])
           for oi in range(6) if DESC[oi][2] == 12 for tw in (False, True))
check("3.6 doubled-cell pieces (orbit propagation): range <= 1 gives 6 per C2' orbit and 336 per free orbit; range 0 gives "
      "one per character on each C2' orbit (identity for A1, antipodal for A2) and 8 per character on each free orbit",
      okp and okid, f"{[cnt[oi] for oi in range(6)]}")
FREE = [oi for oi in range(6) if DESC[oi][2] == 24]; C2O = [oi for oi in range(6) if DESC[oi][2] == 12]
SITE_S = [sidx(s_) for s_ in SUBL]
PERMS = []
for tw in (False, True):
    for choice in itertools.product(range(8), repeat=2):
        col = {}
        for oi in C2O: col.update(R0[oi][tw][0])
        for oi, ch in zip(FREE, choice): col.update(R0[oi][tw][ch])
        tc = np.zeros((64, 12), int); wv = np.zeros((64, 12)); ob = np.zeros((64, 12), int); onsite = True
        for i in range(NM):
            tg, w = col[i]; onsite &= MV[tg].tolist() == MV[i].tolist()
            tc[i // 12, i % 12] = MC[tg]; wv[i // 12, i % 12] = w; ob[i // 12, i % 12] = ORBOF[i]
        assert onsite
        # 2Z^3 covariance: data depend only on the sublattice
        sub = np.array([sidx(tuple(int(x) % 2 for x in v)) for v in SITES])
        assert np.array_equal(tc, tc[sub]) and np.array_equal(wv, wv[sub]) and np.array_equal(ob, ob[sub])
        PERMS.append(dict(tw=tw, choice=choice, tc=tc[SITE_S], w=wv[SITE_S], orb=ob[SITE_S]))
indep = [n for n, P_ in enumerate(PERMS) if np.all(P_['tc'] == P_['tc'][0])]
PH4 = np.array(list(itertools.product(range(4), repeat=6)))
ntinv = 0; tinv_ops = []
for n in indep:
    P_ = PERMS[n]
    vals = P_['w'][None] * (1j ** PH4[:, P_['orb']])                               # (4096, 8, 12)
    good = np.all(np.abs(vals - vals[:, :1]) < 1e-12, axis=(1, 2))
    ntinv += int(good.sum())
    for ph in PH4[good]:
        M = np.zeros((12, 12), complex)
        for c in range(12): M[P_['tc'][0, c], c] = P_['w'][0, c] * 1j ** ph[P_['orb'][0, c]]
        tinv_ops.append(M)
iden = set()
for M in tinv_ops:
    for z in PHASE:
        if np.allclose(M, z * np.eye(12)): iden.add(('1', z))
        if np.allclose(M, z * A0): iden.add(('A0', z))
check("3.7 G0 (range-0 doubled-cell letters: 2 characters x 64 free-orbit choices x 4^6 orbit phases = 524,288): exactly one "
      "perm part per character is sublattice-independent, and exactly 8 letters are translation-invariant: z 1 and z A0",
      len(PERMS) * 4 ** 6 == 524288 and len(indep) == 2 and {PERMS[n]['tw'] for n in indep} == {False, True}
      and ntinv == 8 and len(iden) == 8, f"{ntinv} translation-invariant")
# ---------- a R_L b lemma
RLKEYS = sorted(RL); DIDX = {d: n for n, d in enumerate(RLKEYS)}
HOPS = []                                                                            # per corner c': [(d index, row, value)]
for cp in range(12):
    HOPS.append(sorted((DIDX[d], int(r), RL[d][r, cp].real) for d in RLKEYS for r in np.nonzero(np.abs(RL[d][:, cp]) > 1e-12)[0]))
check("3.8a R_L has exactly two nonzero entries per column, at the two unit displacements along the directions of the "
      "column's corner", all(len(h) == 2 for h in HOPS) and all({RLKEYS[d] for d, _, _ in HOPS[c]} == set(CORN[c]) for c in range(12)))
HD = np.array([[h[0] for h in HOPS[c]] for c in range(12)]); HR = np.array([[h[1] for h in HOPS[c]] for c in range(12)])
HV = np.array([[h[2] for h in HOPS[c]] for c in range(12)])
SPD = np.array([[SUBL.index(tuple(int(x) % 2 for x in add(s_, RLKEYS[d]))) for d in range(len(RLKEYS))] for s_ in SUBL])
TA = np.array([P_['tc'] for P_ in PERMS])                                            # (128, 8, 12)
adm = []
for jb, Pb in enumerate(PERMS):
    tb = Pb['tc']; d2 = HD[tb]; r2 = HR[tb]                                           # (8, 12, 2)
    sd = SPD[np.arange(8)[:, None, None], d2]                                         # target sublattice
    rows = TA[:, sd, r2]                                                              # (128, 8, 12, 2)
    code = np.sort(d2[None] * 12 + rows, axis=-1)
    okA = np.all(code == code[:, :1], axis=(1, 2, 3))
    adm += [(ia, jb) for ia in np.nonzero(okA)[0]]
check("3.8b a R_L b support: of all 128^2 = 16,384 (perm part of a, perm part of b) pairs in G0, exactly 4 give a "
      "translation-invariant support, namely both perm parts sublattice-independent",
      len(adm) == 4 and {(ia, jb) for ia, jb in adm} == {(ia, jb) for ia in indep for jb in indep}, f"{len(adm)} admissible")
REFW = {'R_L': RL, 'Rt': RTX, 'A0 R_L': mul(A0D, RL), 'R_L A0': mul(RL, A0D)}


def word_blocks(Pa, Pb, xa, xb):
    """translation-invariant a R_L b blocks (source sublattice 0) for orbit phases exp(2 pi i x)"""
    def blk(P_, x, s_):
        M = np.zeros((12, 12), complex)
        for c in range(12): M[P_['tc'][s_, c], c] = P_['w'][s_, c] * np.exp(2j * np.pi * x[P_['orb'][s_, c]])
        return M
    return {RLKEYS[d]: blk(Pa, xa, SPD[0, d]) @ RL[RLKEYS[d]] @ blk(Pb, xb, 0) for d in range(len(RLKEYS))}


def ident(blk):
    for nm, X in REFW.items():
        k_ = next(iter(X)); r, c = np.unravel_index(np.argmax(np.abs(X[k_])), (12, 12))
        z = blk.get(k_, np.zeros((12, 12)))[r, c] / X[k_][r, c]
        if abs(abs(z) - 1) < 1e-9 and bl_eq(blk, X, z, tol=1e-9): return nm, z
    return None, None


allw = set(); okcont = True; oksnf = True; oku1 = True; info = []
for ia, jb in adm:
    Pa, Pb = PERMS[ia], PERMS[jb]
    rows_, C_, base = [], [], []
    for c in range(12):
        for j in range(2):
            vecs = []; bits = []
            for s_ in range(8):
                cb = Pb['tc'][s_, c]; d = HD[cb, j]; r = HR[cb, j]; sa = SPD[s_, d]
                vec = np.zeros(12, int); vec[Pa['orb'][sa, r]] += 1; vec[6 + Pb['orb'][s_, c]] += 1
                sgn = Pa['w'][sa, r] * HV[cb, j] * Pb['w'][s_, c]
                vecs.append(vec); bits.append(0 if sgn > 0 else 1)
            base.append(vecs[0])
            for s_ in range(1, 8): rows_.append(vecs[s_] - vecs[0]); C_.append((bits[s_] - bits[0]) % 2)
    A_ = np.array(rows_); C_ = np.array(C_)
    uniq = {}
    for r_, cc in zip(map(tuple, A_), C_):
        if r_ in uniq and uniq[r_] != cc: uniq[r_] = None
        else: uniq.setdefault(r_, cc)
    assert None not in uniq.values()
    Au = np.array([r_ for r_ in uniq]); Cu = np.array([uniq[r_] for r_ in uniq])
    rk = np.linalg.matrix_rank(Au.astype(float))
    snf = smith_normal_form(sympy.Matrix(Au.tolist()), domain=sympy.ZZ)
    inv = sorted({int(abs(snf[i, i])) for i in range(min(snf.shape)) if snf[i, i] != 0})
    oksnf &= inv == [1]
    K = np.linalg.svd(Au.astype(float))[2][rk:]                                     # real kernel
    img = np.array(base) @ K.T
    okcont &= np.linalg.matrix_rank(np.hstack([img, np.ones((len(base), 1))]), tol=1e-8) == 1
    free = [i for i in range(12) if i not in (0, 6)]
    X4 = np.array(list(itertools.product(range(4), repeat=10)), dtype=np.int16).T    # (10, 4^10)
    good = np.ones(X4.shape[1], bool)
    for r_, cc in zip(Au, Cu):
        good &= ((r_[free].astype(np.int16) @ X4) - 2 * cc) % 4 == 0
    sols = X4[:, good].T
    words = set()
    for xs in sols:
        x = np.zeros(12); x[free] = xs / 4
        nm, z = ident(word_blocks(Pa, Pb, x[:6], x[6:]))
        for zg in PHASE: words.add((nm, complex(np.round(z * zg, 9)) if nm else None))
    x0 = np.zeros(12); x0[free] = sols[0] / 4
    nm0, z0 = ident(word_blocks(Pa, Pb, x0[:6], x0[6:]))
    for _ in range(5):                                                              # U(1): x0 + kernel + Z^12
        x = x0 + K.T @ rng.normal(size=K.shape[0]) + rng.integers(-3, 4, 12)
        nm, z = ident(word_blocks(Pa, Pb, x[:6], x[6:])); oku1 &= nm == nm0
    info.append((PERMS[ia]['tw'], PERMS[jb]['tw'], rk, inv, int(good.sum()), sorted({w[0] for w in words if w[0]})))
    allw |= words
for x in info: print(f"   twist (a, b) = {x[:2]}: rank {x[2]}, SNF invariants {x[3]}, Z4 solutions {x[4]}, words {x[5]}")
check("3.8c a R_L b phases: for each admissible pair the constraint matrix has Smith invariants all 1 (no torsion beyond "
      "Z^12) and every real-kernel direction moves all entries of the word by one common phase; so with U(1) orbit phases "
      "the solutions are x0 + ker + Z^12 and each pair gives one word up to a U(1) scalar (5 random U(1) solutions each)",
      oksnf and okcont and oku1)
check("3.8d the translation-invariant a R_L b (a, b in G0, Z4 phases enumerated, x Z4 global) are exactly z {R_L, Rt, "
      "A0 R_L, R_L A0}, z in {+-1, +-i}: 16 words", None not in {w[0] for w in allw} and len(allw) == 16
      and {w[0] for w in allw} == set(REFW), f"{len(allw)} words")
print(f"   section 3: {time.time() - t1:.1f}s")

# =====================================================================================================================
# Section 4: C8 class 2, antiunitary letters
# =====================================================================================================================
print("\n=== 4. C8 class 2: antiunitary letters ===", flush=True)
t1 = time.time()
realok = all(np.abs(B.imag).max() == 0 for X in (S1, RL, RTX, A0D) for B in X.values()) and all(np.abs(g['U'].imag).max() == 0 for g in PSG)
check("4.1 S, R_L, Rt, A0 and all 48 dressed lift matrices are real in the real-space mode basis (K commutes with them)", realok)
conjok = True
for n, B in PC.items():
    m, z = find_in(B.conj(), PC); conjok &= m is not None and complex(np.round(z, 9)) in (1, -1, 1j, -1j)
check("4.2 the Clifford palette PC is closed under complex conjugation up to phases in {+-1, +-i}", conjok)


def specdist(A, B):
    a = np.linalg.eigvals(A); b = list(np.linalg.eigvals(B)); d = 0
    for x in a:
        j = int(np.argmin([abs(x - y) for y in b])); d = max(d, abs(x - b[j])); b.pop(j)
    return d


okv = okp = True
for _ in range(100):
    w = rand_word(rng, 2 * int(rng.integers(0, 2)))
    wc = [t if t[0] != 'U' else ('U', t[1].conj()) for t in w]
    k = rng.uniform(-np.pi, np.pi, 3)
    U2 = word(w, k) @ word(w, -k).conj()                                             # Bloch form of (VK)^2 = V V*
    okv &= np.allclose(U2, word(w, k) @ word(wc, k), atol=1e-12)
    okp &= specdist(word(w, -k) @ word(w, k).conj(), U2.conj()) < 1e-8
check("4.3 (VK)^2 = V V*, and V* is the same word with every on-site slot conjugated, so for a conjugation-closed palette "
      "the square is an old-palette word up to a phase (100 random words with 0 or 2 A letters)", okv)
check("4.4 spec (VK)^2(-k) = conj spec (VK)^2(k) (the only constraint the antiunitary class adds)", okp)
print(f"   section 4: {time.time() - t1:.1f}s")

# =====================================================================================================================
# Section 5: C8 class 3, non-permutation letters
# =====================================================================================================================
print("\n=== 5. C8 class 3: exponential letters ===", flush=True)
t1 = time.time()
okT = True; nT = []
for a in (0, 1, 2):
    X = mul(A0D, Spow(a)); X2 = mul(X, X)
    okT &= bl_eq(X2, scal(-1, ONE))                                                  # A_a^2 = -1
    E = {k_: B / np.sqrt(2) for k_, B in X.items()}; E[Z0] = E.get(Z0, 0) + I12 / np.sqrt(2)   # exp(pi/4 A_a) = (1 + A_a)/sqrt2
    okT &= bl_eq(mul(E, dag(E)), ONE)
    n = 0
    for g in PROPER:
        Y = conjG(g, E)
        Em = {k_: g['chi'] * B / np.sqrt(2) for k_, B in X.items()}; Em[Z0] = Em.get(Z0, 0) + I12 / np.sqrt(2)
        okT &= bl_eq(Y, Em)
        z = Y[Z0][0, 0] / E[Z0][0, 0] if abs(E[Z0][0, 0]) > 1e-12 else None
        cov = z is not None and abs(abs(z) - 1) < 1e-9 and bl_eq(Y, E, z, tol=1e-9)
        n += cov; okT &= cov == (g['chi'] == 1)
    nT.append(n)
check("5.1 A_a^2 = -1 and exp(pi/4 A_a) = (1 + A_a)/sqrt2 is unitary (a = 0, 1, 2); G exp(pi/4 A_a) G^-1 = "
      "exp(chi(g) pi/4 A_a), which is a phase times exp(pi/4 A_a) exactly for the 12 rotations of ker A2 = T: only T-covariant",
      okT and nT == [12, 12, 12], f"covariant rotations {nT}")
k = rng.uniform(-np.pi, np.pi, 3)
check("5.2 S^a (a != 0) is not an involution: S(k)^2 has k-dependent, non-real spectrum", not np.allclose(Sk(k, 2), np.eye(12)) and
      np.abs(np.linalg.eigvals(Sk(k, 2)).imag).max() > 0.1)
okinv = True
for Ps in (PH, PL):
    for r in range(1, len(Ps)):
        for sub in itertools.combinations(range(len(Ps)), r):
            P_ = sum(Ps[i] for i in sub); Ex = expm(1j * np.pi / 4 * (np.eye(12) - 2 * P_))
            okinv &= find_in(Ex, PC)[0] is not None or find_in(Ex * np.exp(-1j * np.pi / 4), PC)[0] is not None
check("5.3 exp(i pi/4 (1 - 2P)) for every sum P of H_on- or Lambda-eigenprojectors lies in PC up to a phase", okinv)
EPD = {a: 1j * B / np.sqrt(2) for a, B in RL.items()}; EPD[Z0] = EPD.get(Z0, 0) + I12 / np.sqrt(2)
EMD = {a: -1j * B / np.sqrt(2) for a, B in RL.items()}; EMD[Z0] = EMD.get(Z0, 0) + I12 / np.sqrt(2)
ok = bl_eq(mul(EPD, dag(EPD)), ONE) and bl_eq(mul(EPD, EMD), ONE) and bl_eq(mul(EPD, EPD), scal(1j, RL)) and bl_eq(mul(EPD, RL), scal(1j, EMD))
ok &= np.allclose(expm(1j * np.pi / 4 * bloch(RL, k)), bloch(EPD, k))
check("5.4 E+- = (1 +- i R_L)/sqrt2 = exp(+-i pi/4 R_L) (block dicts): unitary, E+ E- = 1, E+^2 = i R_L, E+ R_L = i E-", ok)
nnz = collections.Counter(); vals = set()
for c in range(12):
    nnz[sum(int(np.sum(np.abs(B[:, c]) > 1e-12)) for B in EPD.values())] += 1
    for B in EPD.values(): vals |= set(np.round(np.abs(B[:, c][np.abs(B[:, c]) > 1e-12]), 6))
check("5.5 E+ is O-symmetric (all 24 dressed rotations) and translation-invariant, but not monomial: 3 nonzeros per "
      "column, |entries| in {1/sqrt2, 1/2}", all(bl_eq(conjG(g, EPD), EPD) for g in PROPER) and dict(nnz) == {3: 12}
      and vals == {0.707107, 0.5}, f"{dict(nnz)} {sorted(vals)}")
okrt = all(np.allclose(expm(1j * s_ * np.pi / 4 * bloch(RTX, q)), Sk(q, 1) @ bloch(EMD if s_ > 0 else EPD, q) @ Sk(q, -1))
           for s_ in (1, -1) for q in rng.uniform(-np.pi, np.pi, (4, 3)))
check("5.6 exp(+-i pi/4 Rt) = S E-+ S^-1 (from Rt = -S R_L S^-1): nothing new", okrt)
okr = True
for q in rng.uniform(-np.pi, np.pi, (5, 3)):
    okr &= np.allclose(bloch(EPD, q + PI3), bloch(EMD, q)) and np.allclose(bloch(EPD, q).T, bloch(EPD, -q)) and np.allclose(bloch(RL, q + PI3), -bloch(RL, q))
check("5.7 R_L(k+Pi) = -R_L(k), hence E+-(k+Pi) = E-+(k); E(k)^T = E(-k)", okr)


def Wt(w, q):
    M = I12.copy()
    for t in w:
        if not isinstance(t, str): M = M @ t
        elif t == 'R': M = M @ bloch(RL, q)
        elif t == 'Rt': M = M @ bloch(RTX, q)
        elif t in ('S', 'Si', 'S2', 'S2i'): M = M @ Sk(q, {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2}[t])
        elif t == 'E+': M = M @ bloch(EPD, q)
        elif t == 'E-': M = M @ bloch(EMD, q)
    return M


def hygienic(w):
    """reduced word: cyclically no adjacent pair that merges or cancels -- E-E, E-R_L, R_L-E (E+E+ = i R_L, E+E- = 1,
    E+R_L = i E-), R_L-R_L, Rt-Rt, S-S^-1, S^-1-S -- and no adjacent slots"""
    n = len(w)
    for i in range(n):
        a, b = w[i], w[(i + 1) % n]
        if isinstance(a, str) and isinstance(b, str):
            if (a[0] == 'E' and (b[0] == 'E' or b == 'R')) or (b[0] == 'E' and a == 'R'): return False
            if (a, b) in (('R', 'R'), ('Rt', 'Rt'), ('S', 'Si'), ('Si', 'S')): return False
        if not isinstance(a, str) and not isinstance(b, str): return False
    return True


okrel = True; brk = 0; NW = 0; nunh = 0; brk_unh = 0
for _ in range(400 if SLOW else 300):
    n = int(rng.integers(2, 6)); toks = [str(x) for x in rng.choice(['S', 'Si', 'S2', 'R', 'Rt', 'E+', 'E-', 'o'], n)]
    if not any(t[0] == 'E' for t in toks): continue
    w = [rand_onsite_unitary(rng) if t == 'o' else t for t in toks]
    wp = [{'E+': 'E-', 'E-': 'E+'}.get(t, t) if isinstance(t, str) else t for t in w]
    nR = sum(1 for t in toks if t in ('R', 'Rt')); q = rng.uniform(-np.pi, np.pi, 3)
    okrel &= np.allclose(Wt(w, q + PI3), (-1) ** nR * Wt(wp, q), atol=1e-12)
    b_ = min(np.abs(Wt(w, q + PI3) - Wt(w, q)).max(), np.abs(Wt(w, q + PI3) + Wt(w, q)).max()) > 1e-6
    if hygienic(w): brk += b_; NW += 1
    else: brk_unh += b_; nunh += 1
w0 = ['E+', 'S']; q = rng.uniform(-np.pi, np.pi, 3)
d0 = min(np.abs(Wt(w0, q + PI3) - Wt(w0, q)).max(), np.abs(Wt(w0, q + PI3) + Wt(w0, q)).max())
check("5.8 for E-words W(k+Pi) = (-1)^{n_R} W'(k), with W' = W with E+ <-> E- (all sampled words); the exact relation "
      "W(k+Pi) = +-W(k) is broken for the witness E+ S and for every sampled hygienic E-word (in the sample it survives "
      "only in non-hygienic words, e.g. those whose E letters merge, E+ E+ = i R_L)", okrel and d0 > 0.1 and brk == NW and NW > 50,
      f"hygienic: {brk}/{NW} broken; non-hygienic: {brk_unh}/{nunh} broken; E+ S residual {d0:.2f}")


def nS(toks): return sum({'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2}.get(t, 0) for t in toks)


NPI = 160 if SLOW else 80
cnt = collections.Counter(); tries = 0
while min(cnt['free'], cnt['slot']) < NPI and tries < 20000:
    tries += 1
    n = int(rng.integers(3, 7)); toks = [str(x) for x in rng.choice(['S', 'Si', 'S2', 'R', 'Rt', 'E+', 'E-', 'o'], n)]
    if not any(t[0] == 'E' for t in toks) or nS(toks) == 0: continue
    kind = 'slot' if 'o' in toks else 'free'
    if cnt[kind] >= NPI: continue
    w = [rand_onsite_unitary(rng) if t == 'o' else t for t in toks]
    if not hygienic(w): continue
    qs = rng.uniform(-np.pi, np.pi, (3, 3))
    keep = any(all(specdist(Wt(w, q + PI3), om * Wt(w, q)) < 1e-7 for q in qs) for om in (1, -1))
    cnt[kind] += 1; cnt[(kind, keep)] += 1
check(f"5.9 spectral Pi-taste (numerical): spec W(k+Pi) = omega spec W(k), omega = +-1, holds for all {cnt['free']} sampled "
      f"slot-free E-words and fails for all {cnt['slot']} sampled E-words with a generic symmetric on-site slot "
      "(reduced words with an E letter and n_S != 0; see hygienic())",
      cnt[('free', True)] == cnt['free'] == NPI and cnt[('slot', False)] == cnt['slot'] == NPI,
      f"free kept {cnt[('free', True)]}/{cnt['free']}, slot kept {cnt[('slot', True)]}/{cnt['slot']}")
th = np.pi / 6
E6 = {a: 1j * np.sin(th) * B for a, B in RL.items()}; E6[Z0] = E6.get(Z0, 0) + np.cos(th) * I12
E6m = {a: -1j * np.sin(th) * B for a, B in RL.items()}; E6m[Z0] = E6m.get(Z0, 0) + np.cos(th) * I12
q = rng.uniform(-np.pi, np.pi, 3); M6 = bloch(E6, q)
gen = [np.exp(1j * np.pi * m / 12) * np.linalg.matrix_power(bloch(EPD, q), n) for n in range(8) for m in range(24)]
check("5.10 exp(i pi/6 R_L) is unitary, O-symmetric, flips to exp(-i pi/6 R_L) under k -> k + Pi, and is not z E+^n "
      "(z a 24th root of unity, n = 0..7)", bl_eq(mul(E6, dag(E6)), ONE) and all(bl_eq(conjG(g, E6), E6) for g in PROPER)
      and np.allclose(bloch(E6, q + PI3), bloch(E6m, q)) and not any(np.allclose(M6, G_) for G_ in gen))
F = (sp.identity(NM, dtype=complex, format='csr') + 1j * DPI) / np.sqrt(2); Finv = F.conj().T
okF = abs(F @ Finv - sp.identity(NM)).max() < 1e-14 and abs(F @ F - 1j * DPI).max() < 1e-14
okF &= abs(F @ LETS4['R_L'] - LETS4['R_L'] @ Finv).max() < 1e-14 and abs(F @ LETS4['S'] - LETS4['S'] @ F).max() < 1e-14
T1 = sp.csr_matrix((np.ones(NM), ([12 * sidx(add(v, (1, 0, 0))) + c for v in SITES for c in range(12)], np.arange(NM))), shape=(NM, NM))
okF &= abs(T1 @ F @ T1.T - F).max() > 0.5
check("5.11 F = exp(i pi/4 D_Pi) = (1 + i D_Pi)/sqrt2 on the L = 4 torus: unitary, F^2 = i D_Pi, F R_L = R_L F^-1, "
      "F S = S F, and F is not translation-invariant (so words reduce to old word x F^m, invariant only for F^m = +-1)", okF)
okE = True
for X in (EPD, EMD, E6, RL):
    for k0 in (KST, -KST):
        M = bloch(X, k0); G = bloch_grad(X, k0)
        for D in (DP, DM):
            c = D.conj().T @ M @ D
            okE &= np.linalg.norm(M @ D - D @ c) < 1e-12 and np.allclose(c, c[0, 0] * np.eye(2), atol=1e-12)
            okE &= max(np.abs(D.conj().T @ g_ @ D).max() for g_ in G) < 1e-12
check("5.12 E+-, exp(i pi/6 R_L) and R_L are scalars on D+ and D- at +-k* with zero compressed derivative P d_i X P "
      "(analytic Bloch derivative): no velocity source", okE)
rows = []
for q in rng.uniform(-np.pi, np.pi, (4, 3)):
    R_ = bloch(RL, q); rows.append(np.array([(R_ @ B - B @ R_).ravel() for B in ONB]).T)
svc = np.linalg.svd(np.vstack(rows), compute_uv=False)
check("5.13 the symmetric on-site elements commuting with R_L(k) for all k are only the scalars, so no involution "
      "R_L P + (1 - P) with P a symmetric on-site projector exists", int(np.sum(svc < 1e-9)) == 1)
print(f"   section 5: {time.time() - t1:.1f}s")

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - T0:.0f}s]")
sys.exit(0 if FAIL == 0 else 1)
