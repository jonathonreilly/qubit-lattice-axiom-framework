#!/usr/bin/env python3
"""Bounded supplied-model controls. The canonical claim card and complete corrected argument define the current claim boundary. Finite obstruction certificates do not promote deferred terminal exclusions. Optional branches count only when executed.

Historical technical inventory (read with those corrected scope qualifications):
Curvature-member constraint closure with a lattice Weyl/Dirac field (spin 1/2) and a lattice U(1) Maxwell
field (spin 1): both land on the scalar's cone K/(4 alpha); exact lattice obstructions; anisotropic cones rejected.

Companion runner of
docs/CURVATURE_MEMBER_CLOSURE_PUTS_A_LATTICE_WEYL_FIELD_AND_A_LATTICE_MAXWELL_FIELD_ON_THE_SCALARS_CONE_AND_REJECTS_ANISOTROPIC_CONES_BOUNDED_THEOREM_NOTE_2026-10-18.md

Companion runner of the scalar note, same PR (imported for its exact polynomial Poisson engine, the 09-24 gravity clauses and the supplied
site scalar): scripts/curvature_member_closure_with_matter_common_cone_2026_10_18.py.

Consolidated from the scale-ladder campaign blocks B15 (fermion), B16 (Maxwell), B17 (anisotropic cones) and
their fresh-context checks (B15_check, B16_check, B17_check). Where it was cheap the runner keeps two
implementations of a load-bearing step (marked "path 2" in the output): position-space sparse operators vs
momentum-space Laurent symbols for the fermion; polynomial Poisson engine vs the closed incidence formula for
Maxwell; two component extractions for the anisotropic cone. Both paths are written by the same model family.

Every gating test is exact (Fraction / Gaussian rationals / sympy). Supplied models only; nothing is adopted;
no physical identification.

Parts
  W  spin 1/2: naive nearest-neighbour Weyl field h_N = sum_b wbar_b (-iv/2)(sigma^j |x><x+e| - h.c.),
     wbar_b = wa N_x + wb N_(x+e); naive Dirac with mass / Wilson term.
  X  spin 1: lattice U(1) field, H_EM(N) = sum_l Nlink (g^2/2) E^2 + sum_p Nplaq (cB/2g^2) F^2, generator
     G_A[xi] = sum xi_(y,i) E_(y+i,j) F_ij(y), Gauss_x = div E.
  Y  anisotropic cones (continuum leading order + runner-added lattice and loophole checks).
  N  what {G,G} closure fixes about generator normalisations (continuum, runner-added; cf. campaign blocks B16 check and B19).
Flags
  --full  also run the slower exact parts (3D Taylor-expanded lattice fermion path; continuum Maxwell
          structure function / shared lambda (M3b-M6); independent Function-based stress check (C4a/C4b);
          Maxwell incidence-path uniform-shift identity at L = 4).  About 6 more minutes.
  --diag  print the floating-point, non-gating smooth-field diagnostics (Maxwell uniform-shift defect order,
          staggered-generator ratio).  About 2 minutes.
"""
from __future__ import annotations

# Owner capture binds these complete source/context identities before and after execution.
AUDIT_TIMEOUT_SEC = 1800
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


import importlib.util
import itertools
import os
import random
import sys
import time
from fractions import Fraction as F
from itertools import product

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
_CM = os.path.join(HERE, "curvature_member_closure_with_matter_common_cone_2026_10_18.py")
_spec = importlib.util.spec_from_file_location("cm_scalar_companion", _CM)
cm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cm)
padd, pscale, pmul, term, pbracket, in_span, Reducer = cm.padd, cm.pscale, cm.pmul, cm.term, cm.bracket, cm.in_span, cm.Reducer

ARGS = sys.argv[1:]
FULL = "--full" in ARGS
DIAG = "--diag" in ARGS
PASS = FAIL = 0
T0 = time.time()
I = sp.I
PAIRS = ((0, 1), (0, 2), (1, 2))


def check(name, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok)
    PASS += ok
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""), flush=True)


def section(title):
    print(f"\n=== {title} ({time.time() - T0:.0f}s) ===", flush=True)


SIGS = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
E2 = sp.eye(2)


# =====================================================================================================
# Part W engine 1: position-space sparse one-particle operators over Gaussian rationals (after B15)
# =====================================================================================================
ZC = (F(0), F(0))


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cz(a):
    return a[0] == 0 and a[1] == 0


def C(re, im=0):
    return (F(re), F(im))


def oadd(A, B, s=C(1)):
    out = dict(A)
    for k, v in B.items():
        nv = cadd(out.get(k, ZC), cmul(s, v))
        if cz(nv):
            out.pop(k, None)
        else:
            out[k] = nv
    return out


def omul(A, B):
    rows = {}
    for (i, j), v in B.items():
        rows.setdefault(i, []).append((j, v))
    out = {}
    for (i, k), v in A.items():
        for j, w in rows.get(k, ()):
            nv = cadd(out.get((i, j), ZC), cmul(v, w))
            if cz(nv):
                out.pop((i, j), None)
            else:
                out[(i, j)] = nv
    return out


def ocomm(A, B):
    return oadd(omul(A, B), omul(B, A), C(-1))


SIGC = [((C(0), C(1)), (C(1), C(0))), ((C(0), C(0, -1)), (C(0, 1), C(0))), ((C(1), C(0)), (C(0), C(-1)))]
ID2C = ((C(1), C(0)), (C(0), C(1)))


def ckron(A, B):
    n, m = len(A), len(B)
    return tuple(tuple(cmul(A[i // m][j // m], B[i % m][j % m]) for j in range(n * m)) for i in range(n * m))


def cneg(A):
    return tuple(tuple(cmul(C(-1), a) for a in r) for r in A)


OFFC = ((C(0), C(1)), (C(1), C(0)))
DIAGC = ((C(1), C(0)), (C(0), C(-1)))
ALPHAC = [ckron(OFFC, SIGC[j]) for j in range(3)]
BETAC = ckron(DIAGC, ID2C)


class WLat:
    def __init__(self, L):
        self.L = L
        self.SITES = list(product(range(L), repeat=3))
        self.IDX = {x: n for n, x in enumerate(self.SITES)}

    def sh(self, x, d):
        return tuple((x[k] + d[k]) % self.L for k in range(3))

    def put(self, op, x, y, mat, coef, nc):
        for a in range(nc):
            for b in range(nc):
                v = cmul(coef, mat[a][b])
                if cz(v):
                    continue
                k = (self.IDX[x] * nc + a, self.IDX[y] * nc + b)
                nv = cadd(op.get(k, ZC), v)
                if cz(nv):
                    op.pop(k, None)
                else:
                    op[k] = nv

    def hop(self, n, wa, wb, mats, nc, v=F(1)):
        op = {}
        for x in self.SITES:
            for j in range(3):
                y = self.sh(x, unit(j))
                w = wa * n.get(x, 0) + wb * n.get(y, 0)
                if w == 0:
                    continue
                self.put(op, x, y, mats[j], C(0, -v * w / 2), nc)
                self.put(op, y, x, mats[j], C(0, v * w / 2), nc)
        return op

    def mass(self, n, m, nc):
        op = {}
        for x, val in n.items():
            if val:
                self.put(op, x, x, BETAC, C(m * val), nc)
        return op

    def wilson(self, n, wa, wb, r):
        op = {}
        for x in self.SITES:
            for j in range(3):
                y = self.sh(x, unit(j))
                w = wa * n.get(x, 0) + wb * n.get(y, 0)
                if w == 0:
                    continue
                c = C(r * w / 2)
                self.put(op, x, x, BETAC, c, 4)
                self.put(op, y, y, BETAC, c, 4)
                self.put(op, x, y, BETAC, cmul(C(-1), c), 4)
                self.put(op, y, x, BETAC, cmul(C(-1), c), 4)
        return op

    def delta(self, y, val=F(1)):
        return {tuple(c % self.L for c in y): val}

    def weyl_B(self, n, m, wa, wb, mats=None):
        mats = SIGC if mats is None else mats
        return ocomm(self.hop(n, wa, wb, mats, 2), self.hop(m, wa, wb, mats, 2))


def unit(j, s=1):
    return tuple(s if k == j else 0 for k in range(3))


O3 = (0, 0, 0)
NN = [unit(j, s) for j in range(3) for s in (1, -1)]
COLL = [unit(j, 2 * s) for j in range(3) for s in (1, -1)]
DIAGP = [tuple(unit(j, s)[k] + unit(k2, t)[k] for k in range(3)) for j in range(3) for k2 in range(3) if j < k2 for s in (1, -1) for t in (1, -1)]
NNN = COLL + DIAGP


def w0_grassmann():
    """B15 T0: graded Poisson bracket dictionary on a 4-mode Grassmann algebra (exact)."""
    nm = 4

    def gadd(a, b, s=C(1)):
        out = dict(a)
        for k, v in b.items():
            nv = cadd(out.get(k, ZC), cmul(s, v))
            if cz(nv):
                out.pop(k, None)
            else:
                out[k] = nv
        return out

    def gmul(a, b):
        out = {}
        for m1, c1 in a.items():
            for m2, c2 in b.items():
                if set(m1) & set(m2):
                    continue
                seq = list(m1 + m2)
                sign = 1
                for i in range(len(seq)):
                    for k in range(len(seq) - 1 - i):
                        if seq[k] > seq[k + 1]:
                            seq[k], seq[k + 1] = seq[k + 1], seq[k]
                            sign = -sign
                out = gadd(out, {tuple(seq): cmul(C(sign), cmul(c1, c2))})
        return out

    def dleft(a, g):
        out = {}
        for m, c in a.items():
            if g in m:
                p = m.index(g)
                out = gadd(out, {m[:p] + m[p + 1:]: cmul(C((-1) ** p), c)})
        return out

    def dright(a, g):
        out = {}
        for m, c in a.items():
            if g in m:
                p = m.index(g)
                out = gadd(out, {m[:p] + m[p + 1:]: cmul(C((-1) ** (len(m) - 1 - p)), c)})
        return out

    def pb(Fp, Gp):
        out = {}
        for a in range(nm):
            out = gadd(out, gmul(dright(Fp, a), dleft(Gp, nm + a)))
            out = gadd(out, gmul(dright(Fp, nm + a), dleft(Gp, a)))
        return {k: cmul(C(0, -1), v) for k, v in out.items()}

    def quad(A):
        out = {}
        for a in range(nm):
            for b in range(nm):
                if not cz(A[a][b]):
                    out = gadd(out, gmul({(nm + a,): C(1)}, {(b,): A[a][b]}))
        return out

    rng = random.Random(15)

    def herm():
        A = [[ZC] * nm for _ in range(nm)]
        for a in range(nm):
            A[a][a] = C(rng.randint(-3, 3))
            for b in range(a + 1, nm):
                re, im = rng.randint(-3, 3), rng.randint(-3, 3)
                A[a][b], A[b][a] = C(re, im), C(re, -im)
        return A

    def mmul(A, B):
        out = []
        for i in range(nm):
            row = []
            for j in range(nm):
                acc = ZC
                for k in range(nm):
                    acc = cadd(acc, cmul(A[i][k], B[k][j]))
                row.append(acc)
            out.append(row)
        return out
    ok = True
    for _ in range(3):
        A, B = herm(), herm()
        AB, BA = mmul(A, B), mmul(B, A)
        Cm = [[cmul(C(0, -1), cadd(AB[i][j], cmul(C(-1), BA[i][j]))) for j in range(nm)] for i in range(nm)]
        ok = ok and pb(quad(A), quad(B)) == quad(Cm)
        for a in range(nm):
            r2 = {(b,): cmul(C(0, -1), A[a][b]) for b in range(nm) if not cz(A[a][b])}
            ok = ok and pb({(a,): C(1)}, quad(A)) == r2
    check("W0 Grassmann dictionary", ok,
          "{psi_a, psibar_b} = -i delta: {psibar A psi, psibar B psi} = -i psibar[A,B]psi and {psi, psibar A psi} = -i A psi "
          "(exact, 4 modes, random Gaussian-integer Hermitian A, B); so G_f[u] = psibar (i L_u) psi has {psi, G_f[u]} = L_u psi and "
          "{H_f(N), H_f(M)} = -i psibar [h_N, h_M] psi")


# =====================================================================================================
# Part W engine 2: exact momentum-space lattice symbols (after B15_check), Laurent polynomials in
# X = e^{iak}, Y = e^{iaq}, P = e^{iap}; exponent slots (X1..3, Y1..3, P1..3, power of 1/a)
# =====================================================================================================
SOFF = {"k": 0, "q": 3, "p": 6}
KAP = sp.symbols("c1:4")  # relative lapse momentum
OFFD = sp.Matrix([[0, 1], [1, 0]])
DGM = sp.Matrix([[1, 0], [0, -1]])
ALPS = [sp.kronecker_product(OFFD, s) for s in SIGS]
BETS = sp.kronecker_product(DGM, E2)


def smadd(D, e, M):
    D[e] = D[e] + M if e in D else M


def sclean(D):
    out = {}
    for e, M in D.items():
        M2 = M.applyfunc(sp.expand)
        if any(x != 0 for x in M2):
            out[e] = M2
    return out


def spexp(psi_mom, j, n):
    e = [0] * 9
    for lbl in psi_mom:
        e[SOFF[lbl] + j] += n
    return e


def H_sym(lap, psi_mom, mats, v, wa, wb, beta=None, r=0, mass=0):
    D = {}
    lo = SOFF[lap]
    for j in range(3):
        for (xe, pe, coef) in ((0, 1, wa), (1, 1, wb), (-1, -1, -wa), (0, -1, -wb)):
            e = spexp(psi_mom, j, pe)
            e[lo + j] += xe
            smadd(D, tuple(e) + (1,), (-I * v / 2) * coef * mats[j])
        if r:
            for (xe, pe, coef) in ((0, 0, wa), (1, 0, wb), (0, 1, -wa), (1, 1, -wb), (-1, 0, wa), (0, 0, wb), (-1, -1, -wa), (0, -1, -wb)):
                e = spexp(psi_mom, j, pe)
                e[lo + j] += xe
                smadd(D, tuple(e) + (1,), sp.Rational(r) / 2 * coef * beta)
    if mass:
        smadd(D, tuple([0] * 9) + (0,), mass * beta)
    return sclean(D)


def smul(P, Q):
    D = {}
    for e1, M1 in P.items():
        for e2, M2 in Q.items():
            smadd(D, tuple(x + y for x, y in zip(e1, e2)), M1 * M2)
    return sclean(D)


def ssub(P, Q):
    D = dict(P)
    for e, M in Q.items():
        smadd(D, e, -M)
    return sclean(D)


def sbracket(**kw):
    return ssub(smul(H_sym("k", ["q", "p"], **kw), H_sym("q", ["p"], **kw)), smul(H_sym("q", ["k", "p"], **kw), H_sym("k", ["p"], **kw)))


def untag(B):
    out = {}
    for e, M in B.items():
        smadd(out, e[:9], M)
    return sclean(out)


def to_XZ(B):
    """Y = Z/X; group by X-exponent. Translation-covariant G_f on xi~ has symbol sum_j (X_j - Y_j) g_j(XY, P)."""
    G = {}
    for e, M in untag(B).items():
        ex = tuple(e[j] - e[3 + j] for j in range(3))
        G.setdefault(ex, {})
        smadd(G[ex], tuple(e[3:9]), M)
    return {k: sclean(v) for k, v in G.items() if sclean(v)}


def expand_a(B, K, p, nmax, flip=(1, 1, 1)):
    """B = sum_n a^n B_n with k = K/2 + kappa, q = K/2 - kappa; flip_j = -1: doubler P_j -> -P_j."""
    dim = next(iter(B.values())).shape[0]
    out = {n: sp.zeros(dim, dim) for n in range(-2, nmax + 1)}
    for e, M in B.items():
        eX, eY, eP, pw = e[0:3], e[3:6], e[6:9], e[9]
        sign = 1
        for j in range(3):
            if flip[j] == -1 and eP[j] % 2:
                sign = -sign
        th = sum(sp.Rational(eX[j] + eY[j], 2) * K[j] + eP[j] * p[j] for j in range(3))
        lam = sum((eX[j] - eY[j]) * KAP[j] for j in range(3))
        for nn in range(0, nmax + pw + 1):
            out[nn - pw] += sign * M * sp.expand((I * (th + lam)) ** nn / sp.factorial(nn))
    return {n: Mx.applyfunc(sp.expand) for n, Mx in out.items()}


def kdeg_parts(Mx):
    parts = {}
    for idx, ent in enumerate(Mx):
        if ent == 0:
            continue
        for mon, cf in sp.Poly(ent, *KAP).terms():
            d = sum(mon)
            parts.setdefault(d, sp.zeros(*Mx.shape))
            parts[d][idx] += cf * sp.prod([KAP[i] ** mon[i] for i in range(3)])
    return parts


def is_zero(Mx):
    return all(sp.expand(x) == 0 for x in Mx)


def nonlinear_part(Mx):
    out = sp.zeros(*Mx.shape)
    for d, Q in kdeg_parts(Mx).items():
        if d != 1:
            out += Q
    return out


def kosmann_sym(K, p, v, spin, dim=2):
    kv, Kv, pv = sp.Matrix(KAP), sp.Matrix(K), sp.Matrix(p)
    w = -2 * I * kv
    div = (I * Kv).dot(w)
    curl = (I * Kv).cross(w)
    Lm = (w.dot(I * pv) + div / 2) * E2
    for j in range(3):
        Lm += I / 4 * curl[j] * spin[j]
    Lm = Lm.applyfunc(sp.expand)
    if dim == 4:
        Lm = sp.kronecker_product(E2, Lm)
    return (-v ** 2 * Lm).applyfunc(sp.expand)


def g0_cubic(B0):
    return sum((B0.diff(KAP[j]) * KAP[j] ** 3 / 6 for j in range(3)), sp.zeros(*B0.shape)).applyfunc(sp.expand)


def clifford_odd(Mx):
    U, Lo = Mx[0:2, 0:2], Mx[2:4, 2:4]
    return not (is_zero(Mx[0:2, 2:4]) and is_zero(Mx[2:4, 0:2]) and is_zero(U - Lo))


def even_part(Mx):
    X = (Mx[0:2, 0:2] + Mx[2:4, 2:4]) / 2
    return sp.kronecker_product(E2, X).applyfunc(sp.expand)


# =====================================================================================================
# Part W: tests
# =====================================================================================================
XS = sp.symbols("x y z", real=True)


def lie_pos(u, psi, b=I / 4):
    div = sum(sp.diff(u[k], XS[k]) for k in range(3))
    curl = [sp.diff(u[2], XS[1]) - sp.diff(u[1], XS[2]), sp.diff(u[0], XS[2]) - sp.diff(u[2], XS[0]), sp.diff(u[1], XS[0]) - sp.diff(u[0], XS[1])]
    out = sp.zeros(2, 1)
    for k in range(3):
        out += u[k] * psi.diff(XS[k])
    out += div / 2 * psi
    for k in range(3):
        out += b * curl[k] * (SIGS[k] * psi)
    return out


def mzero(m):
    return all(sp.simplify(sp.expand(e)) == 0 for e in m)


def part_W_continuum():
    section("Part W1: spin 1/2, continuum leading order")
    v = sp.Symbol("v", real=True)
    Nf, Mf = sp.Function("N")(*XS), sp.Function("M")(*XS)
    PSI = sp.Matrix([sp.Function("psi1")(*XS), sp.Function("psi2")(*XS)])
    # W1 Kosmann coefficient, two paths
    b = sp.Symbol("b")
    om = sp.symbols("o1 o2 o3")
    xi = [om[1] * XS[2] - om[2] * XS[1], om[2] * XS[0] - om[0] * XS[2], om[0] * XS[1] - om[1] * XS[0]]

    def weylop(psi):
        out = sp.zeros(2, 1)
        for k in range(3):
            out += SIGS[k] * psi.diff(XS[k])
        return out
    commu = lie_pos(xi, weylop(PSI), b) - weylop(lie_pos(xi, PSI, b))
    sol = sp.solve(sp.expand(commu[0].subs({om[0]: 0, om[1]: 0, om[2]: 1}).subs(PSI[0], 0)), b)
    ok1 = sol == [I / 4] and mzero(lie_pos(xi, weylop(PSI), I / 4) - weylop(lie_pos(xi, PSI, I / 4)))
    omv, Xv = sp.Matrix(om), sp.Matrix(sp.symbols("x1:4"))
    f = sp.Function("f")(*Xv)
    uu = sp.Matrix(sp.symbols("u1:3"))
    xiv = omv.cross(Xv)

    def Lxi(ps):
        return sum((xiv[j] * ps.diff(Xv[j]) for j in range(3)), sp.zeros(2, 1)) + 2 * b * sum((omv[j] * SIGS[j] for j in range(3)), sp.zeros(2, 2)) * ps

    def Dw(ps):
        return sum((SIGS[j] * ps.diff(Xv[j]) for j in range(3)), sp.zeros(2, 1))
    sol2 = sp.solve(list((Lxi(Dw(f * uu)) - Dw(Lxi(f * uu))).applyfunc(sp.expand)), b, dict=True)
    check("W1 Kosmann spin coefficient (two paths)", ok1 and sol2 == [{b: I / 4}],
          f"rotation invariance [L_xi, sigma.grad] = 0 for rigid rotations fixes L_xi = xi.grad + (1/2) div xi + b (curl xi).sigma at b = {sol} "
          f"(path 1, position space) and {sol2} (path 2, operator form): the Kosmann value, fixed before any bracket is computed")
    # W2 continuum bracket, two paths
    def hcont(n, psi):
        out = sp.zeros(2, 1)
        for k in range(3):
            out += SIGS[k] * (n * psi.diff(XS[k]) + sp.diff(n, XS[k]) / 2 * psi)
        return -I * v * out
    w = [Nf * sp.diff(Mf, xx) - Mf * sp.diff(Nf, xx) for xx in XS]
    okp = mzero(hcont(Nf, hcont(Mf, PSI)) - hcont(Mf, hcont(Nf, PSI)) + v ** 2 * lie_pos(w, PSI))
    k = sp.Matrix(sp.symbols("k1:4"))
    q = sp.Matrix(sp.symbols("q1:4"))
    p = sp.Matrix(sp.symbols("p1:4"))

    def Hc(kk, pp, G):
        return sum(((-I * v) * G[j] * (I * pp[j] + I * kk[j] / 2) for j in range(3)), sp.zeros(2, 2))

    def kos(kk, qq, pp, spin=SIGS):
        ww = I * (qq - kk)
        Kt = kk + qq
        out = (ww.dot(I * pp) + (I * Kt).dot(ww) / 2) * E2
        cu = (I * Kt).cross(ww)
        for j in range(3):
            out += I / 4 * cu[j] * spin[j]
        return out
    Bc = (Hc(k, q + p, SIGS) * Hc(q, p, SIGS) - Hc(q, k + p, SIGS) * Hc(k, p, SIGS)).applyfunc(sp.expand)
    oks = (Bc + v ** 2 * kos(k, q, p)).applyfunc(sp.expand) == sp.zeros(2, 2)
    check("W2 continuum Weyl bracket (two paths)", okp and oks,
          "h_N = -iv(N sigma.grad + (1/2) grad N.sigma): [h_N, h_M] = -v^2 L_w exactly, w = N grad M - M grad N, L_w the Kosmann "
          "derivative (spin term produced by the bracket); path 1 sympy Functions, path 2 plane-wave symbols. With W0: "
          "{H_f(N), H_f(M)} = G_f[v^2 w]")
    Ga = [I * s for s in SIGS]
    Bg = (Hc(k, q + p, Ga) * Hc(q, p, Ga) - Hc(q, k + p, Ga) * Hc(k, p, Ga)).applyfunc(sp.expand)
    check("W3 Clifford-signature control", (Bg - v ** 2 * kos(k, q, p)).applyfunc(sp.expand) == sp.zeros(2, 2),
          "with anti-Hermitian generators gamma^j = i sigma^j (h_N then non-Hermitian) the bracket is +v^2 L_w: the coefficient's sign is the "
          "Clifford signature; Hermitian generators square to +1, so for Hermitian h_N with real v the coefficient v^2 is > 0")
    # W5 position-dependent mass drops out (continuum, 1D Dirac)
    x = XS[0]
    n1, m1 = sp.Function("N")(x), sp.Function("M")(x)
    mu = sp.Function("mu")(x)
    psi1 = sp.Matrix([sp.Function("psi1")(x), sp.Function("psi2")(x)])
    s1_, s3_ = SIGS[0], SIGS[2]

    def hcm(nn, g):
        return -I * v * s1_ * (nn * g.diff(x) + sp.diff(nn, x) / 2 * g) + s3_ * mu * nn * g

    def hc0(nn, g):
        return -I * v * s1_ * (nn * g.diff(x) + sp.diff(nn, x) / 2 * g)
    check("W4 continuum mass drops out", mzero((hcm(n1, hcm(m1, psi1)) - hcm(m1, hcm(n1, psi1))) - (hc0(n1, hc0(m1, psi1)) - hc0(m1, hc0(n1, psi1)))),
          "1D Dirac with an arbitrary position-dependent mass mu(x) N beta: [h_N, h_M] is the massless bracket exactly (alpha beta = -beta alpha)")


def jet_gravity_field_check():
    """continuum gravity bracket: {kin(N)+sK R1(N), kin(M)+sK R1(M)} = G_g[-(sK/(4 alpha)) w], w = N grad M - M grad N."""
    s = sp.Symbol("s")
    JE.reset()
    CN = JE.N * (JE.kin() + s * JE.K * JE.r1())
    CM = JE.M * (JE.kin() + s * JE.K * JE.r1())
    w = [JE.N * gm - JE.M * gn for gn, gm in zip(JE.grad("N"), JE.grad("M"))]
    res = JE.euler(JE.bracket(CN, CM) - JE.gg_vec([-(s * JE.K / (4 * JE.al)) * x for x in w]), "N")
    return sp.expand(res) == 0


def part_W_cone():
    section("Part W2: spin 1/2 cone condition")
    okg = jet_gravity_field_check()
    s, K, al, v2 = sp.symbols("s K alpha v2", real=True)
    sol = sp.solve(sp.Eq(v2, -s * K / (4 * al)), v2)
    a = sp.Symbol("a")
    kk, qq = sp.symbols("kk qq")
    xit = sp.series(sp.exp(I * a * kk) - sp.exp(I * a * qq), a, 0, 2).removeO()
    lead_ok = sp.simplify(xit / a + I * (qq - kk)) == 0
    pos = [sv for sv in (-1, 1) if (-sv * sp.Rational(5, 11) / (4 * sp.Rational(3, 7))) > 0]
    check("W5 one cone for spin 1/2: v^2 = -sK/(4 alpha) (assembled; the final solve is arithmetic)", okg and lead_ok and sol == [-s * K / (4 * al)] and pos == [-1],
          "the iff is assembled from W2/W6 (fermion bracket) and the computed gravity bracket (continuum, exact jet calculus, both signs s): "
          "{kin(N)+sK R1(N), kin(M)+sK R1(M)} = G_g[-(sK/(4alpha)) w]; lattice "
          "xi~/a -> -w (symbol); W2 gives {H_f,H_f} = G_f[v^2 w] at leading order (lattice: W6). One total relabelling with one common "
          f"orientation needs v^2 = {sol[0]} = the scalar's c (companion note). Hermitian h_N (W3) gives v^2 > 0, so with K, alpha > 0 only s = {pos[0]} closes")


def part_W_lattice_symbols():
    section("Part W3: spin 1/2 lattice symbols (exact)")
    rng = random.Random(1518)

    def rq():
        return sp.Rational(rng.randint(-9, 9), rng.randint(1, 7))
    V, HALF = sp.Rational(4, 5), sp.Rational(1, 2)
    PTS = [([rq() for _ in range(3)], [rq() for _ in range(3)]) for _ in range(2)]
    Bh = sbracket(mats=SIGS, v=V, wa=HALF, wb=HALF)
    tl = {tv: sbracket(mats=SIGS, v=V, wa=tv, wb=1 - tv) for tv in (sp.Integer(1), sp.Rational(1, 4))}
    ok_lead = ok_h1 = ok_h2dev = ok_h2obs = ok_t1dev = ok_t1cub = True
    for (Kv, pv) in PTS:
        eh = expand_a(Bh, Kv, pv, 2)
        kos = kosmann_sym(Kv, pv, V, SIGS)
        ok_lead &= is_zero(eh[-2]) and is_zero(eh[-1]) and is_zero(eh[0] - kos)
        for Bt in tl.values():
            e1 = expand_a(Bt, Kv, pv, 1)
            ok_lead &= is_zero(e1[-2]) and is_zero(e1[-1]) and is_zero(e1[0] - kos)
            ok_t1dev &= not is_zero(e1[1])
            kp = kdeg_parts(e1[1])
            ok_t1cub &= 3 in kp and not is_zero(kp[3])
        ok_h1 &= is_zero(eh[1])
        ok_h2dev &= not is_zero(eh[2])
        ok_h2obs &= not is_zero(nonlinear_part(eh[2] + g0_cubic(eh[0])))
    check("W6 lattice leading order (symbol path)", ok_lead,
          "naive lattice Weyl, timings (1/2,1/2), (1,0), (1/4,3/4), exact symbols at two rational (K, p): O(a^-2), O(a^-1) vanish and "
          "O(a^0) = -v^2 L_w (Kosmann, sigma): every two-endpoint timing has the continuum leading order")
    check("W7 endpoint mean: O(a^2) obstruction", ok_h1 and ok_h2dev and ok_h2obs,
          "t = 1/2: O(a) part = 0; O(a^2) part nonzero and not absorbable by any translation-covariant linear G_f on gravity's bond field "
          "(any range, any 2x2 structure): B_2 + sum_j kappa_j^3 dB_0/dkappa_j / 6 is not linear in the relative momentum kappa")
    check("W8 other timings: O(a) obstruction", ok_t1dev and ok_t1cub,
          "t = 1 and t = 1/4: the O(a) part has a kappa-cubic component, so no O(a)-corrected translation-covariant G_f of any range absorbs it")
    # doublers
    ok, ok2 = True, True
    for flip in product((1, -1), repeat=3):
        if flip == (1, 1, 1):
            continue
        sigp = [flip[j] * SIGS[j] for j in range(3)]
        nflip = sum(1 for f_ in flip if f_ == -1)
        tau = [(-1 if nflip % 2 else 1) * s_ for s_ in sigp]
        Bp = sbracket(mats=sigp, v=V, wa=HALF, wb=HALF)
        Kv, pv = PTS[0]
        ed, ep = expand_a(Bh, Kv, pv, 2, flip=flip), expand_a(Bp, Kv, pv, 2)
        ok &= all(is_zero(ed[n] - ep[n]) for n in ed) and is_zero(ed[0] - kosmann_sym(Kv, pv, V, tau)) and is_zero(ed[1])
        ok2 &= (not is_zero(ed[0] - kosmann_sym(Kv, pv, V, SIGS))) if nflip < 3 else is_zero(ed[0] - kosmann_sym(Kv, pv, V, SIGS))
    check("W9 doublers: one v^2, own spin set (symbol path)", ok,
          "all 7 doublers (P_j -> -P_j): bracket = bracket with sigma' = (+-sigma^j) exactly; leading order -v^2 L_w with the doubler's own "
          "proper spin set tau (sigma' or -sigma'); O(a) = 0")
    check("W10 doubler spin caveat", ok2,
          "tau = sigma only at (pi,pi,pi); at the 6 doublers with one or two pi components tau != sigma, so a G_f with the on-site spin term "
          "(i/4)(curl xi).sigma fails there at O(1): the lattice G_f needs momentum-dependent spin structure")
    # bracket content with symbolic timing
    v, wa, wb = sp.symbols("v w_a w_b")
    B = sbracket(mats=SIGS, v=v, wa=wa, wb=wb)
    G = to_XZ(B)
    units = {unit(j, s_) for j in range(3) for s_ in (1, -1)}
    coll = set(COLL)
    diag = {kx for kx in G if sum(abs(t) for t in kx) == 2 and kx not in coll}

    def polys(keys):
        out = set()
        for kx in keys:
            for M in G[kx].values():
                for ent in M:
                    if ent != 0:
                        out.add(sp.factor(sp.expand(ent / v ** 2)))
        return out
    pc, pd = polys(coll & set(G)), polys(diag)
    mixed = {kx for kx in diag if sorted(kx) == [-1, 0, 1]}
    okc = coll <= set(G) and all(sp.expand(pp).has(wa) and sp.expand(pp).has(wb) and sp.expand(pp.subs(wa, wb)) != 0 for pp in pc)
    okd = len(diag) == 6 and diag == mixed and all(sp.expand(pp.subs(wa, wb)) == 0 and sp.expand(pp.subs(wa, -wb)) == 0 for pp in pd)
    others = set(G) - units - coll - diag
    allp = set()
    for kx, Dd in G.items():
        if kx in units:
            continue
        for M in Dd.values():
            for ent in M:
                if ent != 0:
                    allp.add(sp.expand(ent))
    solt = sp.solve(list(allp), [wa, wb], dict=True)
    check("W11 bracket content, general timing (symbol path)", okc and okd and not others and solt == [{wa: 0, wb: 0}],
          f"wbar = wa N_x + wb N_(x+e): besides nearest-neighbour lapse pairs, B contains the 6 collinear range-2 pairs (coefficient "
          f"{sorted(map(str, pc))} v^2) and the 6 mixed diagonal pairs +-(e_j - e_k) (coefficient ~ (wa^2 - wb^2)); same-sign diagonal pairs are "
          f"absent at every timing; nothing else. The non-nearest-neighbour part vanishes only at {solt}")
    Gh = to_XZ({e: M.subs({wa: HALF, wb: HALF, v: V}) for e, M in B.items()})
    bad = [kx for kx in Gh if kx not in units]
    rel_ok = True
    for j in range(3):
        up, dn = unit(j), unit(j, -1)
        shf = {}
        for ee, M in Gh.get(up, {}).items():
            e2 = list(ee)
            e2[j] += 1
            smadd(shf, tuple(e2), -M)
        rel_ok &= sclean(shf) == sclean(Gh.get(dn, {}))
    tgt = {e[:6]: M.subs({wa: HALF, wb: HALF}) for e, M in untag(B).items() if e[6:9] == (2, 0, 0)}
    okm = tgt.get((0, 0, 0, 2, 0, 0)) == -v ** 2 / 16 * E2 and tgt.get((2, 0, 0, 0, 0, 0)) == v ** 2 / 16 * E2
    check("W12 no translation-covariant G_f of any range (symbol path)", bad and set(bad) == coll and rel_ok and okm,
          "endpoint mean: the nearest-neighbour part has exactly the form sum_j (X_j - Y_j) g_j(XY, P) of a G_f acting on gravity's xi~, "
          "but the range-2 monomials X_j^(+-2) lie outside that span for every g_j; their position-space coefficient is "
          "-(v^2/16)(N_x M_(x+2e) - N_(x+2e) M_x)(|x><x+2e| - h.c.), spin-independent")
    # Dirac: mass and Wilson
    m = sp.Rational(13, 10)
    Bd = sbracket(mats=ALPS, v=V, wa=HALF, wb=HALF, beta=BETS, mass=m)
    Bw = sbracket(mats=SIGS, v=V, wa=HALF, wb=HALF)
    check("W13 Dirac mass drops out at the endpoint mean (symbol path)", untag(Bd) == untag({e: sp.kronecker_product(E2, M) for e, M in Bw.items()}),
          "naive Dirac + on-site mass m N beta, t = 1/2: exact symbol identity [h_N, h_M] = 1_2 (x) [Weyl bracket]")
    t = sp.Symbol("t")
    cross = ssub(sbracket(mats=ALPS, v=V, wa=t, wb=1 - t, beta=BETS, mass=m), sbracket(mats=ALPS, v=V, wa=t, wb=1 - t))
    Gc = {}
    for e, M in cross.items():
        ex = tuple(e[j] - e[3 + j] for j in range(3))
        Gc.setdefault(ex, {})
        smadd(Gc[ex], tuple(e[3:9]) + (e[9],), M)
    Gc = {kx: sclean(Dd) for kx, Dd in Gc.items() if sclean(Dd)}
    form_ok = set(Gc) <= units
    for j in range(3):
        shf = {}
        for ee, M in Gc.get(unit(j), {}).items():
            e2 = list(ee)
            e2[j] += 1
            smadd(shf, tuple(e2), -M)
        form_ok &= sclean(shf) == Gc.get(unit(j, -1), {})
    vanish = {tv: not sclean({e: M.subs(t, tv) for e, M in cross.items()}) for tv in (0, sp.Rational(1, 4), HALF, 1)}
    lin_t = all(sp.degree(sp.expand(ent), t) <= 1 and sp.expand(ent.subs(t, HALF)) == 0 for M in cross.values() for ent in M if ent != 0)
    odd = all(is_zero(even_part(M.subs(t, 0))) for M in cross.values()) and any(clifford_odd(M.subs(t, 0)) for M in cross.values())
    check("W14 Dirac mass cross terms", vanish == {0: False, sp.Rational(1, 4): False, HALF: True, 1: False} and form_ok and odd and lin_t,
          f"every entry of the cross-term symbol is affine in t and zero at t = 1/2, i.e. proportional to (2t - 1) ({lin_t}; samples "
          f"{ {str(kq): vq for kq, vq in vanish.items()} }); for t != 1/2 they are exactly sum_j xi~_j g_j with Clifford-odd "
          "(alpha beta type) g_j: an obstruction only relative to a Clifford-even (Kosmann-class) G_f")
    Bwil = sbracket(mats=ALPS, v=V, wa=HALF, wb=HALF, beta=BETS, r=1)
    Kv, pv = PTS[0]
    e = expand_a(Bwil, Kv, pv, 2)
    okw = is_zero(e[0] - kosmann_sym(Kv, pv, V, SIGS, dim=4)) and not is_zero(e[1]) and clifford_odd(e[1]) and is_zero(nonlinear_part(e[1]))
    okobs = not is_zero(nonlinear_part(e[2] + g0_cubic(e[0])))
    check("W15 Wilson term: O(a) Clifford-odd but absorbable, O(a^2) obstruction", okw and okobs,
          "Dirac + Wilson (r = 1, t = 1/2): O(a^0) = Kosmann; the O(a) term is nonzero and Clifford-odd (it blocks a Kosmann-class G_f) but "
          "linear in kappa, so a G_f with a Clifford-odd O(a) correction absorbs it; the O(a^2) part is non-absorbable by any "
          "translation-covariant G_f")


def part_W_lattice_position():
    section("Part W4: spin 1/2 lattice, position space (exact Gaussian rationals)")
    lat = WLat(5)
    half = F(1, 2)
    nnn = {d: lat.weyl_B(lat.delta(O3), lat.delta(d), half, half) for d in NNN}
    ok1 = all(lat.weyl_B(lat.delta(O3), lat.delta(d), half, half) for d in NN)
    ok2 = all(nnn[d] for d in COLL) and not any(nnn[d] for d in DIAGP)
    far = [z for z in lat.SITES if sum(min(z[k], lat.L - z[k]) for k in range(3)) > 2]
    ok3 = all(not lat.weyl_B(lat.delta(O3), lat.delta(z), half, half) for z in far[:40])
    b = nnn[unit(0, 2)]
    el = {(i % 2, j % 2): v for (i, j), v in b.items() if i // 2 == lat.IDX[O3] and j // 2 == lat.IDX[unit(0, 2)]}
    okc = el == {(0, 0): C(F(-1, 16)), (1, 1): C(F(-1, 16))}
    check("W16 lattice bracket support (position path, L=5)", ok1 and ok2 and ok3 and okc,
          "t = 1/2: B(delta_0, delta_d) != 0 for nearest neighbours and for the 6 collinear d = +-2e_j, = 0 for the 12 diagonal d = e_j +- e_k "
          "and for graph distance > 2 (40 sites); <0|B(delta_0, delta_2e1)|2e1> = -(1/16) 1_2 (v = 1): agrees with W11/W12")
    wa, wb = sp.symbols("w_a w_b")
    pol = set()
    for d in NNN:
        Xo, Zo, So = (lat.weyl_B(lat.delta(O3), lat.delta(d), F(1), F(0)), lat.weyl_B(lat.delta(O3), lat.delta(d), F(0), F(1)),
                      lat.weyl_B(lat.delta(O3), lat.delta(d), F(1), F(1)))
        for kk in set(Xo) | set(Zo) | set(So):
            x_, z_, s_ = Xo.get(kk, ZC), Zo.get(kk, ZC), So.get(kk, ZC)
            for part in (0, 1):
                pp = sp.Rational(x_[part]) * wa ** 2 + sp.Rational(s_[part] - x_[part] - z_[part]) * wa * wb + sp.Rational(z_[part]) * wb ** 2
                if pp != 0:
                    pol.add(sp.expand(pp))
    sols = sp.solve(list(pol), [wa, wb], dict=True)
    check("W17 no two-endpoint timing removes the non-nearest-neighbour part (position path)", sols == [{wa: 0, wb: 0}],
          f"B is quadratic in (wa, wb); exact interpolation over the 18 next-neighbour lapse pairs gives {len(pol)} distinct polynomials, "
          f"common zero only {sols}")
    # gravity relabelling kernel, exact, L = 3, 4, 5
    dims = {}
    for LL in (3, 4, 5):
        S = list(product(range(LL), repeat=3))
        col = {(x, j): n for n, (x, j) in enumerate((x, j) for x in S for j in range(3))}
        shl = lambda x, j, s=1, LL=LL: tuple((x[k] + (s if k == j else 0)) % LL for k in range(3))
        red = Reducer()
        for x in S:
            for j in range(3):
                red.add({col[(x, j)]: F(2), col[(shl(x, j, -1), j)]: F(-2)})
            for (i, j) in PAIRS:
                vec = {}
                for kq, vq in ((col[(shl(x, i), j)], 1), (col[(x, j)], -1), (col[(shl(x, j), i)], 1), (col[(x, i)], -1)):
                    vec[kq] = vec.get(kq, 0) + F(vq)
                red.add({kq: vq for kq, vq in vec.items() if vq})
        dims[LL] = len(col) - len(red.basis)
    check("W18 gravity relabelling kernel = constant shifts", all(d_ == 3 for d_ in dims.values()),
          f"exact rank of xi -> G_g[xi] (09-24 clause: diag 2(xi_(x,j) - xi_(x-e_j,j)), faces D_i xi_j + D_j xi_i): kernel dimension {dims} = 3, "
          "the constant shifts; so a closing total xi equals gravity's (sK/(4alpha)) xi~ up to a constant")
    # any linear G_f: brackets with xi_g = 0 must lie in G_f[constants] (dim <= 3); off-site parts exclude on-site constraints
    out = {}
    for (twa, twb, ds, lbl) in ((half, half, [unit(0, 2), unit(1, 2), unit(2, 2)], "t=1/2, d = 2e_j"),
                                (F(1), F(0), [(1, -1, 0), (0, 1, -1), (1, 0, -1)], "t=1, d = e_j - e_k")):
        red = Reducer()
        nvec = 0
        for z in lat.SITES[: len(lat.SITES) // 2]:
            for d in ds:
                bz = lat.weyl_B(lat.delta(z), lat.delta(lat.sh(z, d)), twa, twb)
                vec = {}
                for (i, j), cv in bz.items():
                    if i // 2 != j // 2:  # off-site entries only
                        if cv[0]:
                            vec[(i, j, 0)] = cv[0]
                        if cv[1]:
                            vec[(i, j, 1)] = cv[1]
                red.add(vec)
                nvec += 1
        out[lbl] = (nvec, len(red.basis))
    check("W19 no linear G_f of any range closes exactly (rank path)", all(nv == rk and rk > 4 for nv, rk in out.values()),
          f"L=5, lapse pairs (delta_z, delta_(z+d)) with gravity's xi~ = 0: off-site parts of the brackets have exact rank {out} "
          "(count, rank), far above dim G_f[constant] <= 3; on-site internal constraints cannot touch off-site entries. "
          "A C(lambda) term cannot help either: kin(lambda) is the only P^2 term at this order, so lambda = 0")
    # T4 translation-covariant support argument
    def xi_g(n, mm):
        return {(x, j): n.get(lat.sh(x, unit(j)), 0) * mm.get(x, 0) - n.get(x, 0) * mm.get(lat.sh(x, unit(j)), 0) for x in lat.SITES for j in range(3)}
    ok = True
    for (twa, twb) in ((half, half), (F(1), F(0)), (F(0), F(1)), (F(1, 3), F(2, 3))):
        found = False
        for d in NNN:
            bz = lat.weyl_B(lat.delta(O3), lat.delta(d), twa, twb)
            if all(vv == 0 for vv in xi_g(lat.delta(O3), lat.delta(d)).values()) and bz:
                sup = {lat.SITES[i // 2] for (i, _) in bz} | {lat.SITES[j // 2] for (_, j) in bz}
                if 0 < len(sup) < len(lat.SITES):
                    found = True
                    break
        ok &= found
    check("W20 translation-covariant support argument (position path)", ok,
          "for timings (1/2,1/2), (1,0), (0,1), (1/3,2/3) a lapse pair with xi~ = 0 gives a nonzero, localised bracket; a translation-invariant "
          "G_f[constant] has full support or none: no translation-covariant linear G_f closes")
    # mass and Wilson (position space)
    m = F(3, 7)
    vals = {}
    for at in (F(0), F(1, 4), F(1, 2), F(1)):
        tz = True
        for d in NN:
            n, mm = lat.delta(O3), lat.delta(d)
            cr = oadd(ocomm(lat.mass(n, m, 4), lat.hop(mm, at, 1 - at, ALPHAC, 4)), ocomm(lat.hop(n, at, 1 - at, ALPHAC, 4), lat.mass(mm, m, 4)))
            tz = tz and not cr
        vals[str(at)] = tz
    check("W21 Dirac mass cross terms vanish iff endpoint mean (position path)", vals == {"0": False, "1/4": False, "1/2": True, "1": False}, f"{vals}")
    ok = True
    for d in NN + NNN[:6]:
        n, mm = lat.delta(O3), lat.delta(d)
        bd = ocomm(oadd(lat.hop(n, half, half, ALPHAC, 4), lat.mass(n, m, 4)), oadd(lat.hop(mm, half, half, ALPHAC, 4), lat.mass(mm, m, 4)))
        bw = lat.weyl_B(n, mm, half, half)
        exp = {}
        for (i, j), vv in bw.items():
            si, ai = divmod(i, 2)
            sj, aj = divmod(j, 2)
            for blk in (0, 1):
                exp[(si * 4 + 2 * blk + ai, sj * 4 + 2 * blk + aj)] = vv
        ok = ok and bd == exp
    nonrel = False
    for d in NN:
        n, mm = lat.delta(O3), lat.delta(d)
        bd = ocomm(oadd(lat.hop(n, half, half, ALPHAC, 4), lat.wilson(n, half, half, F(1))), oadd(lat.hop(mm, half, half, ALPHAC, 4), lat.wilson(mm, half, half, F(1))))
        for (i, j), vv in bd.items():
            si, ai = divmod(i, 4)
            sj, aj = divmod(j, 4)
            if (ai // 2) != (aj // 2) or bd.get((si * 4 + (ai + 2) % 4, sj * 4 + (aj + 2) % 4), ZC) != vv:
                nonrel = True
    check("W22 Dirac at endpoint mean: mass drops out, Wilson leaves the relabelling Clifford span (position path)", ok and nonrel,
          "[h_N, h_M] = 1_2 (x) [Weyl bracket] exactly with mass (12 lapse pairs); with a Wilson term (r = 1) components outside {1 (x) X} appear")
    lat4 = WLat(4)
    rng = random.Random(7)
    n = {x: F(rng.randint(-2, 2)) for x in lat4.SITES}
    mm = {x: F(rng.randint(-2, 2)) for x in lat4.SITES}
    bb = lat4.weyl_B(n, mm, half, half)
    bf = lat4.weyl_B(n, mm, half, half, mats=[cneg(SIGC[0]), SIGC[1], SIGC[2]])
    conj = {(i, j): cmul(C((-1) ** (lat4.SITES[i // 2][0] + lat4.SITES[j // 2][0])), vv) for (i, j), vv in bb.items()}
    check("W23 doubler map (position path, L=4)", conj == bf,
          "staggering (-1)^(x_1) maps B[sigma] to B[-sigma^1, sigma^2, sigma^3] exactly for random lapses: the (pi,0,0) doubler obeys the same "
          "bracket with its own Pauli set; sigma^j sigma^j (v^2) terms invariant")


def part_W_1d():
    section("Part W5: spin 1/2, 1D gradient expansion (exact sympy)")
    a, v = sp.symbols("a v", real=True)
    x = XS[0]
    n, m = sp.Function("N")(x), sp.Function("M")(x)
    ps = sp.Function("psi")(x)
    p, Kq = 2, 4

    def trunc(expr, pp):
        expr = sp.expand(expr)
        return sum(expr.coeff(a, qq) * a ** qq for qq in range(-2, pp + 1))

    def sh1(e, s):
        return sum(((s * a) ** k / sp.factorial(k)) * sp.diff(e, x, k) for k in range(Kq + 1))

    def Dop(nn, f):
        wp, wm = (nn + sh1(nn, 1)) / 2, (sh1(nn, -1) + nn) / 2
        return trunc((wp * sh1(f, 1) - wm * sh1(f, -1)) / (2 * a), p)
    br = trunc(Dop(n, Dop(m, ps)) - Dop(m, Dop(n, ps)), p)
    w = n * sp.diff(m, x) - m * sp.diff(n, x)

    def ell(u, f):
        return u * sp.diff(f, x) + sp.diff(u, x) * f / 2

    def shh(e, s):
        return sum(((s * a / 2) ** k / sp.factorial(k)) * sp.diff(e, x, k) for k in range(Kq + 2))
    lead_ok = sp.simplify(br.coeff(a, 0) - ell(w, ps)) == 0
    u = trunc(-(shh(n, 1) * shh(m, -1) - shh(n, -1) * shh(m, 1)) / a, p)
    u_ok = sp.simplify(u.coeff(a, 0) - w) == 0 and u.coeff(a, 1) == 0
    R = sp.expand(br.coeff(a, 2) - ell(u.coeff(a, 2), ps))
    cc = sp.symbols("c1:5")
    Xw = cc[0] * w * sp.diff(ps, x, 3) + cc[1] * sp.diff(w, x) * sp.diff(ps, x, 2) + cc[2] * sp.diff(w, x, 2) * sp.diff(ps, x) + cc[3] * sp.diff(w, x, 3) * ps
    reps = {}
    for f_, nm in ((n, "n"), (m, "m"), (ps, "p")):
        for k in range(8, -1, -1):
            reps[sp.diff(f_, x, k) if k else f_] = sp.Symbol(f"{nm}{k}")

    def solve_in(expr, unk):
        rs = sp.expand(expr.subs(reps))
        syms = [s_ for s_ in rs.free_symbols if s_.name[0] in "nmp"]
        return sp.solve(sp.Poly(rs, *syms).coeffs(), unk, dict=True)
    sol = solve_in(R - Xw, cc)
    qv = sp.symbols("q1:3")
    alt = qv[0] * (n * sp.diff(m, x, 3) - m * sp.diff(n, x, 3)) + qv[1] * (sp.diff(n, x) * sp.diff(m, x, 2) - sp.diff(m, x) * sp.diff(n, x, 2))
    sol2 = solve_in(sp.expand(br.coeff(a, 2) - ell(alt, ps) - Xw), list(cc) + list(qv))
    check("W24 1D endpoint mean: O(a^2) remainder not absorbable, control absorbable", lead_ok and u_ok and sol == [] and sol2 != [],
          "1D: O(a^0) of [D_N, D_M] = L_w and gravity's bond bilinear u = -xi~/a = w + O(a^2); the O(a^2) remainder is not absorbed by any "
          "O(a^2)-corrected relabelling L_u + a^2(c1 u d^3 + c2 u' d^2 + c3 u'' d + c4 u''') (solve -> []); control: if the O(a^2) part of "
          "the shift were a free bilinear it would be absorbable, so the obstruction is the mismatch with gravity's nearest-neighbour xi~")
    # 1D Wilson: Clifford-odd sigma^2 component at O(a)
    r = sp.Symbol("r", real=True)
    s1_, s3_ = SIGS[0], SIGS[2]
    pw, Kw = 1, 4
    f = sp.Function("f")(x)

    def sh2(e, s):
        return sum(((s * a) ** k / sp.factorial(k)) * sp.diff(e, x, k) for k in range(Kw + 1))

    def hw(nn, g):
        wp, wm = (nn + sh2(nn, 1)) / 2, (sh2(nn, -1) + nn) / 2
        gp, gm = g.applyfunc(lambda e: sh2(e, 1)), g.applyfunc(lambda e: sh2(e, -1))
        hop = s1_ * (wp * gp - wm * gm) * (-I * v / (2 * a))
        wil = s3_ * (wp * (g - gp) + wm * (g - gm)) * (r / (2 * a))
        return (hop + wil).applyfunc(lambda e: trunc(e, pw + 1))
    b1 = (hw(n, hw(m, sp.Matrix([f, 0]))) - hw(m, hw(n, sp.Matrix([f, 0])))).applyfunc(lambda e: trunc(e, pw))
    b2 = (hw(n, hw(m, sp.Matrix([0, f]))) - hw(m, hw(n, sp.Matrix([0, f])))).applyfunc(lambda e: trunc(e, pw))
    sig2 = sp.expand((b1[1] - b2[0]) / (2 * I))
    wp_ = sp.diff(w.subs(ps, f), x)
    target = sp.expand(-(r * v / 2) * (wp_ * sp.diff(f, x) + sp.diff(wp_, x) * f / 2))
    check("W25 1D Wilson: O(a) sigma^2 (Clifford-odd) component", sig2.coeff(a, 0) == 0 and sp.simplify(sp.expand(sig2.coeff(a, 1)) - target) == 0,
          "1D naive Dirac + Wilson (t = 1/2): the bracket's sigma^2 (= i alpha beta) component is 0 at O(a^0) and -(r v a/2)(w' d + w''/2) at O(a): "
          "Clifford-odd, outside a Kosmann-class relabelling (absorbable only by a Clifford-odd correction, W15)")


def part_W_taylor3d():
    """--full: B15 C3a/C3b, 3D Taylor-expanded position-space lattice operator (path 2 for W6)."""
    section("Part W6 (--full): spin 1/2, 3D Taylor-expanded lattice operator")
    a, v, t = sp.symbols("a v t", real=True)
    Nf, Mf = sp.Function("N")(*XS), sp.Function("M")(*XS)
    PSI = sp.Matrix([sp.Function("psi1")(*XS), sp.Function("psi2")(*XS)])

    def shift(expr, k, s, Kq):
        return sum(((s * a) ** n / sp.factorial(n)) * sp.diff(expr, XS[k], n) for n in range(Kq + 1))

    def trunc(expr, p):
        expr = sp.expand(expr)
        return sum(expr.coeff(a, q) * a ** q for q in range(-2, p + 1))

    def hlat(n, psi, p):
        Kq = p + 2
        out = sp.zeros(2, 1)
        for k in range(3):
            wb_ = t * n + (1 - t) * shift(n, k, 1, Kq)
            wbm = t * shift(n, k, -1, Kq) + (1 - t) * n
            fwd = psi.applyfunc(lambda e: shift(e, k, 1, Kq))
            bwd = psi.applyfunc(lambda e: shift(e, k, -1, Kq))
            out += (SIGS[k] * (wb_ * fwd - wbm * bwd)) * (-I * v / (2 * a))
        return out.applyfunc(lambda e: trunc(e, p))
    br = (hlat(Nf, hlat(Mf, PSI, 1), 1) - hlat(Mf, hlat(Nf, PSI, 1), 1)).applyfunc(lambda e: trunc(e, 1))
    w = [Nf * sp.diff(Mf, xx) - Mf * sp.diff(Nf, xx) for xx in XS]
    lead = br.applyfunc(lambda e: sp.expand(e).coeff(a, 0))
    neg = br.applyfunc(lambda e: sp.expand(e).coeff(a, -1))
    first = br.applyfunc(lambda e: sp.expand(e).coeff(a, 1))
    check("W26 (--full) lattice leading order (Taylor path)", mzero(neg) and mzero(lead + v ** 2 * lie_pos(w, PSI)),
          "3D naive Weyl, symbolic timing t: O(a^-1) = 0 and O(a^0) = -v^2 L_w (path 2 for W6)")
    check("W27 (--full) O(a) part affine in t, zero only at t = 1/2 (Taylor path)",
          all(sp.expand(sp.diff(e, t, 2)) == 0 for e in first) and all(sp.expand(e.subs(t, sp.Rational(1, 2))) == 0 for e in first)
          and not mzero(first.applyfunc(lambda e: e.subs(t, 1))), "")


# =====================================================================================================
# continuum jet engine (after B14 / the upstream runner's Part D), module level, extended by A/E
# =====================================================================================================
class Jet:
    DIM = 3

    def __init__(self):
        self.JET, self.S2K = {}, {}
        self.HD = [f"hd{j}" for j in range(3)]
        self.HF = {ij: f"hf{ij[0]}{ij[1]}" for ij in PAIRS}
        self.PD = [f"Pd{j}" for j in range(3)]
        self.PF = {ij: f"Pf{ij[0]}{ij[1]}" for ij in PAIRS}
        self.AN = [f"A{k}" for k in range(3)]
        self.EN = [f"E{k}" for k in range(3)]
        self.al, self.K, self.c, self.mu = sp.symbols("alpha K c mu", positive=True)
        self.g2, self.cB = sp.symbols("g2 cB", positive=True)
        self.reset()

    def reset(self, with_em=False, with_phi=True):
        self.CONJ = {**({"phi": "pi"} if with_phi else {}), **{self.HD[j]: self.PD[j] for j in range(3)}, **{self.HF[ij]: self.PF[ij] for ij in PAIRS}}
        if with_em:
            for k in range(3):
                self.CONJ[self.AN[k]] = self.EN[k]

    def J(self, field, a=(0, 0, 0)):
        key = (field, tuple(a))
        if key not in self.JET:
            self.JET[key] = sp.Symbol(field + "_" + "".join(map(str, a)))
            self.S2K[self.JET[key]] = key
        return self.JET[key]

    @property
    def N(self):
        return self.J("N")

    @property
    def M(self):
        return self.J("M")

    def D(self, expr, k):
        expr = sp.expand(expr)
        out = 0
        for s in expr.free_symbols:
            if s in self.S2K:
                f, a = self.S2K[s]
                b = list(a)
                b[k] += 1
                out += sp.diff(expr, s) * self.J(f, b)
        return sp.expand(out)

    def Dalpha(self, expr, a):
        for k in range(3):
            for _ in range(a[k]):
                expr = self.D(expr, k)
        return expr

    def euler(self, expr, field):
        expr = sp.expand(expr)
        out = 0
        for s in list(expr.free_symbols):
            if s in self.S2K and self.S2K[s][0] == field:
                a = self.S2K[s][1]
                out += (-1) ** sum(a) * self.Dalpha(sp.diff(expr, s), a)
        return sp.expand(out)

    def ev(self, i):
        return tuple(1 if k == i else 0 for k in range(3))

    def grad(self, f):
        return [self.J(f, self.ev(i)) for i in range(3)]

    def d2(self, f, i, j):
        a = [0, 0, 0]
        a[i] += 1
        a[j] += 1
        return self.J(f, a)

    def bracket(self, f, g):
        out = 0
        for q, p in self.CONJ.items():
            fq, fp = self.euler(f, q), self.euler(f, p)
            if fq == 0 and fp == 0:
                continue
            out += fq * self.euler(g, p) - fp * self.euler(g, q)
        return sp.expand(out)

    def kin(self):
        tr = sum(self.J(p) for p in self.PD)
        return (sum(self.J(p) ** 2 for p in self.PD) - tr ** 2 / 2) / (4 * self.al) + sum(self.J(self.PF[ij]) ** 2 for ij in PAIRS) / (8 * self.al)

    def r1(self):
        out = 0
        for j in range(3):
            out += self.d2(self.HD[j], j, j) - sum(self.d2(self.HD[j], k, k) for k in range(3))
        for (i, j) in PAIRS:
            out += 2 * self.d2(self.HF[(i, j)], i, j)
        return out

    def gg_vec(self, xi):
        out = 0
        for j in range(3):
            out += self.J(self.PD[j]) * 2 * self.D(xi[j], j)
        for (i, j) in PAIRS:
            out += self.J(self.PF[(i, j)]) * (self.D(xi[j], i) + self.D(xi[i], j))
        return out

    def gg_names(self, names):
        return self.gg_vec([self.J(n) for n in names])

    def hm(self, cc=None):
        cc = self.c if cc is None else cc
        return self.J("pi") ** 2 / 2 + cc * sum(g ** 2 for g in self.grad("phi")) / 2 + self.mu * self.J("phi") ** 2 / 2

    def gm_vec(self, xv):
        return self.J("pi") * sum(xv[k] * self.grad("phi")[k] for k in range(3))

    def coeffs(self, expr):
        expr = sp.expand(expr)
        if expr == 0:
            return []
        jets = [s for s in expr.free_symbols if s in self.S2K]
        if not jets:
            return [expr]
        return [e for e in (sp.expand(cf) for cf in sp.Poly(expr, *jets).coeffs()) if e != 0]

    # Maxwell
    def Fij(self, i, j):
        return self.J(self.AN[j], self.ev(i)) - self.J(self.AN[i], self.ev(j))

    def hem(self, cb=None):
        cb = self.cB if cb is None else cb
        return self.g2 / 2 * sum(self.J(e) ** 2 for e in self.EN) + cb / (2 * self.g2) * sum(self.Fij(*ij) ** 2 for ij in PAIRS)

    def poynting(self, xi):
        return sum(xi[i] * self.J(self.EN[j]) * self.Fij(i, j) for i in range(3) for j in range(3) if i != j)

    def lie_gen_vec(self, xi):
        out = 0
        for j in range(3):
            out += self.J(self.EN[j]) * sum(xi[i] * self.J(self.AN[j], self.ev(i)) + self.J(self.AN[i]) * self.D(xi[i], j) for i in range(3))
        return out

    def divE(self):
        return sum(self.J(self.EN[k], self.ev(k)) for k in range(3))

    def on_gauss(self, expr):
        """restrict to d_k E^k = 0: eliminate every jet of E2 carrying a d_2."""
        expr = sp.expand(expr)
        while True:
            subs = {}
            for s in expr.free_symbols:
                key = self.S2K.get(s)
                if key and key[0] == self.EN[2] and key[1][2] >= 1:
                    a0, a1 = list(key[1]), list(key[1])
                    a0[2] -= 1
                    a0[0] += 1
                    a1[2] -= 1
                    a1[1] += 1
                    subs[s] = -self.J(self.EN[0], a0) - self.J(self.EN[1], a1)
            if not subs:
                return expr
            expr = sp.expand(expr.xreplace(subs))


JE = Jet()


# =====================================================================================================
# Part N: generator normalisation from {G,G} closure (continuum, runner-added)
# =====================================================================================================
def part_N():
    section("Part N: generator normalisation from {G,G} closure (continuum, exact)")
    JE.reset(with_em=True)
    XI, ETA = ["xi0", "xi1", "xi2"], ["eta0", "eta1", "eta2"]
    xi, eta = [JE.J(n) for n in XI], [JE.J(n) for n in ETA]
    lieb = [sum(xi[k] * JE.J(ETA[i], JE.ev(k)) - eta[k] * JE.J(XI[i], JE.ev(k)) for k in range(3)) for i in range(3)]
    Hm = [[None] * 3 for _ in range(3)]
    for j in range(3):
        Hm[j][j] = JE.J(JE.HD[j])
    for (i, j) in PAIRS:
        Hm[i][j] = Hm[j][i] = JE.J(JE.HF[(i, j)])

    def lie_metric(xv, lam1=1):  # (L_xi g)_ij for g = delta + h, the delta (linear-shift) part weighted by lam1
        out = {}
        for i in range(3):
            for j in range(i, 3):
                out[(i, j)] = (sum(xv[k] * JE.D(Hm[i][j], k) for k in range(3)) + sum(Hm[k][j] * JE.D(xv[k], i) + Hm[i][k] * JE.D(xv[k], j) for k in range(3))
                               + lam1 * (JE.D(xv[j], i) + JE.D(xv[i], j)))
        return out

    def gg_full(xv, lam1=1):
        lm = lie_metric(xv, lam1)
        return sum(JE.J(JE.PD[j]) * lm[(j, j)] for j in range(3)) + sum(JE.J(JE.PF[ij]) * lm[ij] for ij in PAIRS)
    sig = sp.Symbol("sigma")

    def sector_sign(G_of):
        res = JE.bracket(G_of(xi), G_of(eta)) - sig * G_of(lieb)
        eqs = []
        for n in ETA:
            eqs += JE.coeffs(JE.euler(res, n))
        return sp.solve(eqs, sig, dict=True)
    sg = sector_sign(gg_full)
    sm = sector_sign(JE.gm_vec)
    sa = sector_sign(JE.lie_gen_vec)
    # fermion: Kosmann derivatives form the Lie algebra: [L_xi, L_eta] = L_[xi,eta]  (G_f = psibar i L psi)
    X3 = sp.symbols("x0:3")
    xf = [sp.Function(f"xi{k}")(*X3) for k in range(3)]
    ef = [sp.Function(f"eta{k}")(*X3) for k in range(3)]
    psi = sp.Matrix([sp.Function("psi1")(*X3), sp.Function("psi2")(*X3)])

    def Lk(u, ps):
        div = sum(sp.diff(u[k], X3[k]) for k in range(3))
        cu = [sp.diff(u[2], X3[1]) - sp.diff(u[1], X3[2]), sp.diff(u[0], X3[2]) - sp.diff(u[2], X3[0]), sp.diff(u[1], X3[0]) - sp.diff(u[0], X3[1])]
        out = sum((u[k] * ps.diff(X3[k]) for k in range(3)), sp.zeros(2, 1)) + div / 2 * ps
        return out + sum((I / 4 * cu[k] * (SIGS[k] * ps) for k in range(3)), sp.zeros(2, 1))
    lbf = [sum(xf[k] * sp.diff(ef[i], X3[k]) - ef[k] * sp.diff(xf[i], X3[k]) for k in range(3)) for i in range(3)]
    rem = (Lk(xf, Lk(ef, psi)) - Lk(ef, Lk(xf, psi)) - Lk(lbf, psi)).applyfunc(sp.expand)
    Sx = sp.Matrix(3, 3, lambda i, j: (sp.diff(xf[j], X3[i]) + sp.diff(xf[i], X3[j])) / 2)
    Se = sp.Matrix(3, 3, lambda i, j: (sp.diff(ef[j], X3[i]) + sp.diff(ef[i], X3[j])) / 2)
    PS = Sx * Se
    om = [sum(sp.LeviCivita(k, i, j) * PS[i, j] for i in range(3) for j in range(3)) for k in range(3)]
    pred = (-I / 2) * sum((om[k] * SIGS[k] for k in range(3)), sp.zeros(2, 2)) * psi
    okf = mzero(rem - pred) and not mzero(rem)
    same = sg == sm == sa == [{sig: 1}]
    # total with relative normalisations: gravity lam1 G1 + G2 (G1 = linear shift 2 d xi, G2 = the O(h) part), scalar lam_m G_m,
    # Maxwell lam_A G_Lie. {G,G} = G[nu [xi,eta]] for one nu.
    l1, lm_, la_, nu = sp.symbols("lam_1 lam_m lam_A nu")
    tot = lambda xv: gg_full(xv, l1) + lm_ * JE.gm_vec(xv) + la_ * JE.lie_gen_vec(xv)
    res = JE.bracket(tot(xi), tot(eta)) - tot([nu * x for x in lieb])
    eqs = []
    for n in ETA:
        eqs += JE.coeffs(JE.euler(res, n))
    sol = sp.solve(eqs, [lm_, la_, nu], dict=True)
    l1_free = all(l1 not in s_ and all(not sp.sympify(v).has(l1) for v in s_.values()) for s_ in sol)
    want = {frozenset({lm_: a_, la_: b_, nu: 1}.items()) for a_ in (0, 1) for b_ in (0, 1)}
    got = {frozenset((k, sp.sympify(v)) for k, v in s_.items()) for s_ in sol}
    check("N1 {G,G} fixes matter normalisations to one structure constant, not against gravity's linear shift", same and got == want and len(sol) == 4 and l1_free,
          f"unit generators obey {{G_s[xi], G_s[eta]}} = sigma G_s[[xi,eta]] with one sigma for gravity (delta h = L_xi g at O(h)) {sg}, scalar {sm} "
          f"and Maxwell G_Lie {sa}; for G = lam_1 G1 + G2 + lam_m G_m + lam_A G_Lie the closure conditions give {sol} with lam_1 free: every "
          "nonzero matter sector shares the structure constant of gravity's O(h) part, but the weight lam_1 of the linear shift delta h = 2 d xi "
          "(which sets the cone relative to K/(4alpha)) is not fixed by {G,G} (agrees with campaign block B19, unchecked)")
    check("N2 spin 1/2: Kosmann relabellings close only up to an on-site rotation", okf,
          "[L_xi, L_eta] = L_[xi,eta] - (i/2) eps_kij (S_xi S_eta)_ij sigma_k exactly, S_xi = symmetric part of grad xi (sympy Functions); so "
          "{lam G_f[xi], lam G_f[eta]} = lam^2 (G_f[[xi,eta]] + rotation term): the transport part behaves as in N1, but the "
          "remainder vanishes also for conformal or commuting symmetric strains; it is a local spin rotation that this fixed flat lift does not carry as a "
          "constraint; a metric-dependent polar-frame connection supplies another lift without an independent triad, as in the stated continuum construction")


# =====================================================================================================
# Part X engine 1: polynomial Poisson engine with A/E (after B16, on the upstream runner's engine)
# =====================================================================================================
class MLat(cm.Lattice):
    def __init__(self, L, alpha=F(3, 7), K=F(5, 11), mu=F(2, 3)):
        super().__init__(L, alpha, K, mu)
        for x in self.SITES:
            for j in range(3):
                a, e = self.var(("A", x, j)), self.var(("E", x, j))
                self.CONJ[a] = e
                self.Q_OF_P[e] = a
        self.FC = {}
        self.SUB = {}
        self.build_sub()

    def inv(self):
        return {i: nm for nm, i in self.VAR.items()}

    def Av(self, x, j):
        return term(1, self.var(("A", x, j)))

    def Ev(self, x, j):
        return term(1, self.var(("E", x, j)))

    def Fpl(self, y, i, j):
        key = (y, i, j)
        if key not in self.FC:
            sh = self.sh
            self.FC[key] = padd(padd(self.Av(sh(y, i), j), self.Av(y, j), F(-1)), padd(self.Av(sh(y, j), i), self.Av(y, i), F(-1)), F(-1))
        return self.FC[key]

    def lapse(self, n, x):
        if isinstance(n, str):
            return term(1, self.var(("lap", n, x)))
        v = n[x]
        return {(): F(v)} if v != 0 else {}

    def build_sub(self):
        inv = self.inv()
        for y in self.SITES:
            for ij in PAIRS:
                b = term(1, self.var(("bt", y, ij)))
                for mo, cf in self.Fpl(y, *ij).items():
                    nm = inv[mo[0]]
                    e = self.var(("E", nm[1], nm[2]))
                    self.SUB[e] = padd(self.SUB.get(e, {}), pscale(b, cf))
        for j in range(3):
            h = term(1, self.var(("ht", j)))
            for x in self.SITES:
                e = self.var(("E", x, j))
                self.SUB[e] = padd(self.SUB.get(e, {}), h)

    def subst(self, poly):
        out = {}
        for mo, c in poly.items():
            acc = {(): c}
            for v in mo:
                acc = pmul(acc, self.SUB[v] if v in self.SUB else {(v,): F(1)})
            out = padd(out, acc)
        return out

    def gauss(self, x):
        out = {}
        for j in range(3):
            out = padd(padd(out, self.Ev(x, j)), self.Ev(self.sh(x, j, -1), j), F(-1))
        return out


def scheme(link, plaq):
    lw = {"mean": (F(1, 2), F(1, 2)), "tail": (F(1), F(0)), "head": (F(0), F(1))}
    pw = {"four": (F(1, 4),) * 4, "diagonal": (F(1, 2), 0, 0, F(1, 2)), "antidiagonal": (0, F(1, 2), F(1, 2), 0),
          "c00": (1, 0, 0, 0), "c10": (0, 1, 0, 0), "c01": (0, 0, 1, 0), "c11": (0, 0, 0, 1)}
    links = link if isinstance(link, tuple) else (link,) * 3
    lws = {d: lw[links[d]] for d in range(3)}
    if plaq == "oriented":
        pws = {}
        for (i, j) in PAIRS:
            ci, cj = (0 if links[i] == "tail" else 1), (0 if links[j] == "tail" else 1)
            w = [0, 0, 0, 0]
            w[{(0, 0): 0, (1, 0): 1, (0, 1): 2, (1, 1): 3}[(ci, cj)]] = 1
            pws[(i, j)] = tuple(F(v) for v in w)
    else:
        pws = {ij: tuple(F(v) for v in pw[plaq]) for ij in PAIRS}
    return lws, pws


FWD = scheme("tail", "c00")


def h_em(lat, n, cb, g2, sch=FWD):
    out = {}
    for x in lat.SITES:
        for j in range(3):
            ut, uh = sch[0][j]
            ll = padd(pscale(lat.lapse(n, x), ut), pscale(lat.lapse(n, lat.sh(x, j)), uh))
            out = padd(out, pmul(pscale(ll, g2 / 2), pmul(lat.Ev(x, j), lat.Ev(x, j))))
    for y in lat.SITES:
        for (i, j) in PAIRS:
            cs = [y, lat.sh(y, i), lat.sh(y, j), lat.sh(lat.sh(y, i), j)]
            pl = {}
            for w, cz_ in zip(sch[1][(i, j)], cs):
                if w != 0:
                    pl = padd(pl, pscale(lat.lapse(n, cz_), w))
            f = lat.Fpl(y, i, j)
            out = padd(out, pmul(pscale(pl, cb / (2 * g2)), pmul(f, f)))
    return out


def h_em_general(lat, n, u, w, cb, g2, ilat):
    """position-dependent timing: u[k] = {site: weight} per link k, w[p] = {site: weight} per plaquette p (ilat ordering)."""
    out = {}
    for k, (x, j) in enumerate(ilat.links):
        ll = {}
        for s, wt in u[k].items():
            ll = padd(ll, pscale(lat.lapse(n, s), wt))
        out = padd(out, pmul(pscale(ll, g2 / 2), pmul(lat.Ev(x, j), lat.Ev(x, j))))
    for p, (y, (i, j)) in enumerate(ilat.plaqs):
        pl = {}
        for s, wt in w[p].items():
            pl = padd(pl, pscale(lat.lapse(n, s), wt))
        f = lat.Fpl(y, i, j)
        out = padd(out, pmul(pscale(pl, cb / (2 * g2)), pmul(f, f)))
    return out


def g_A(lat, xi):
    out = {}
    for y in lat.SITES:
        for i in range(3):
            v = xi[(y, i)]
            v = v if isinstance(v, dict) else ({(): F(v)} if v != 0 else {})
            if not v:
                continue
            for j in range(3):
                if j != i:
                    out = padd(out, pmul(v, pmul(lat.Ev(lat.sh(y, i), j), lat.Fpl(y, i, j))))
    return out


def theta_of(lat, xi):
    th = {}
    for w in lat.SITES:
        acc = {}
        for i in range(3):
            v = xi[(lat.sh(w, i, -1), i)]
            v = v if isinstance(v, dict) else ({(): F(v)} if v != 0 else {})
            if v:
                acc = padd(acc, pmul(v, lat.Av(lat.sh(w, i, -1), i)))
        th[w] = acc
    return th


def gauss_poly(lat, theta):
    out = {}
    for x in lat.SITES:
        v = theta[x]
        v = v if isinstance(v, dict) else ({(): F(v)} if v != 0 else {})
        if v:
            out = padd(out, pmul(v, lat.gauss(x)))
    return out


def g_L(lat, xi):
    return padd(g_A(lat, xi), gauss_poly(lat, theta_of(lat, xi)), F(-1))


def is_bond(L, c, d):
    diff = [(c[k] - d[k]) % L for k in range(3)]
    nz = [k for k in range(3) if diff[k] != 0]
    return len(nz) == 1 and diff[nz[0]] in (1, L - 1)


def classify_poly(lat, sch, cb=F(3, 2), g2=F(5, 7)):
    br = pbracket(lat, h_em(lat, "N", cb, g2, sch), h_em(lat, "M", cb, g2, sch))
    inv = lat.inv()
    groups = {}
    for mn, cf in br.items():
        ln = [v for v in mn if lat.KIND[v] == "lap"]
        rest = tuple(v for v in mn if lat.KIND[v] != "lap")
        cN = [inv[v][2] for v in ln if inv[v][1] == "N"][0]
        cM = [inv[v][2] for v in ln if inv[v][1] == "M"][0]
        key = (min(cN, cM), max(cN, cM))
        sgn = 1 if cN <= cM else -1
        g = groups.setdefault(key, {})
        g[rest] = g.get(rest, 0) + sgn * cf
    nonbond = {k: {r: v for r, v in g.items() if v != 0} for k, g in groups.items() if not is_bond(lat.L, *k) and k[0] != k[1]}
    nonbond = {k: g for k, g in nonbond.items() if g}
    return br, not nonbond, all(not lat.subst(g) for g in nonbond.values()), len(nonbond)


# =====================================================================================================
# Part X engine 2: closed incidence formula (after B16_check chk_lat), exact Fractions
# {H(N),H(M)} = c sum_{k,p} dF_p/dA_k E_k F_p [m_p(N) n_k(M) - n_k(N) m_p(M)]
# =====================================================================================================
class ILat:
    def __init__(self, L):
        self.L = L
        self.sites = list(product(range(L), repeat=3))
        self.sidx = {x: i for i, x in enumerate(self.sites)}
        self.links = [(x, j) for x in self.sites for j in range(3)]
        self.lidx = {l: i for i, l in enumerate(self.links)}
        self.plaqs = [(y, ij) for y in self.sites for ij in PAIRS]
        self.pidx = {p: i for i, p in enumerate(self.plaqs)}
        self.Fp = []
        for (y, (i, j)) in self.plaqs:
            d = {}
            for lk, s in (((self.sh(y, i), j), 1), ((y, j), -1), ((self.sh(y, j), i), -1), ((y, i), 1)):
                k = self.lidx[lk]
                d[k] = d.get(k, 0) + s
            self.Fp.append({k: v for k, v in d.items() if v})
        self.inc = {k: [] for k in range(len(self.links))}
        for pi_, d in enumerate(self.Fp):
            for k, s in d.items():
                self.inc[k].append((pi_, s))

    def sh(self, x, j, s=1):
        return tuple((x[k] + (s if k == j else 0)) % self.L for k in range(3))

    def corners(self, p):
        y, (i, j) = self.plaqs[p]
        return {"00": y, "10": self.sh(y, i), "01": self.sh(y, j), "11": self.sh(self.sh(y, i), j)}

    def is_bond(self, a, b):
        return is_bond(self.L, a, b)


def em_pair_coeffs(lat, u, w, c=F(1)):
    out = {}

    def acc(s, t, key, v):
        if v == 0:
            return
        d = out.setdefault((s, t), {})
        d[key] = d.get(key, 0) + v
        if d[key] == 0:
            del d[key]
    for k in range(len(lat.links)):
        for (p, sg) in lat.inc[k]:
            for s, ws in w[p].items():
                for t, ut in u[k].items():
                    for a, fa in lat.Fp[p].items():
                        v = c * sg * ws * ut * fa
                        acc(s, t, (k, a), v)
                        acc(t, s, (k, a), -v)
    return {k: v for k, v in out.items() if v}


def uniform_timing(lat, link_w, plaq_w):
    u = []
    for (x, j) in lat.links:
        d = {}
        for s, wt in ((x, link_w[j][0]), (lat.sh(x, j), link_w[j][1])):
            if wt:
                d[s] = d.get(s, 0) + wt
        u.append(d)
    w = []
    for p in range(len(lat.plaqs)):
        cs = lat.corners(p)
        y, ij = lat.plaqs[p]
        d = {}
        for name, wt in plaq_w[ij].items():
            if wt:
                d[cs[name]] = d.get(cs[name], 0) + wt
        w.append(d)
    return u, w


def fwd_timing(lat):
    return uniform_timing(lat, {j: (F(1), F(0)) for j in range(3)}, {ij: {"00": F(1)} for ij in PAIRS})


def staggered(lat, par=0):
    u = []
    for (x, j) in lat.links:
        y = lat.sh(x, j)
        u.append({x: F(1)} if sum(x) % 2 == par else {y: F(1)})
    w = []
    for p in range(len(lat.plaqs)):
        w.append({s: F(1, 2) for s in lat.corners(p).values() if sum(s) % 2 != par})
    return u, w


def transverse(lat, d):
    """exact restriction of an E.A bilinear {(k,a): v} to E = curl^T b + h (= ker div): coefficients of (b_p, A_a), (h_j, A_a)."""
    out = {}
    for (k, a), v in d.items():
        for (p, s) in lat.inc[k]:
            key = ("b", p, a)
            out[key] = out.get(key, 0) + s * v
        key = ("h", lat.links[k][1], a)
        out[key] = out.get(key, 0) + v
    return {k: v for k, v in out.items() if v}


def bondsupport(lat, u, w, gauss=False):
    co = em_pair_coeffs(lat, u, w)
    bad = 0
    for (s, t), d in co.items():
        if s == t or lat.is_bond(s, t):
            continue
        if gauss and not transverse(lat, d):
            continue
        bad += 1
    return bad, co


def induced_generator(lat, u, w, c=F(1)):
    co = em_pair_coeffs(lat, u, w, c)
    X = {}
    for (s, t), d in co.items():
        if s == t:
            continue
        assert lat.is_bond(s, t)
        for i in range(3):
            if lat.sh(s, i) == t:
                X[(s, i)] = {k: v / (-c) for k, v in co[(t, s)].items()}
    return X


def fwd_GA(lat):
    X = {}
    for y in lat.sites:
        for i in range(3):
            d = {}
            for j in range(3):
                if j == i:
                    continue
                ij = (min(i, j), max(i, j))
                sgn = 1 if i < j else -1
                p = lat.pidx[(y, ij)]
                k = lat.lidx[(lat.sh(y, i), j)]
                for a, f in lat.Fp[p].items():
                    d[(k, a)] = d.get((k, a), 0) + sgn * f
            X[(y, i)] = {kk: F(v) for kk, v in d.items() if v}
    return X


# =====================================================================================================
# Part X: tests
# =====================================================================================================
def part_X_timing():
    section("Part X1: spin 1, timing classification (exact)")
    lat = MLat(3)
    # X0 transverse parametrisation
    ok_div = all(not lat.subst(lat.gauss(x)) for x in lat.SITES)
    red = Reducer()
    params = [v for nm, v in lat.VAR.items() if nm[0] in ("bt", "ht")]
    for p in params:
        vec = {e: poly[(p,)] for e, poly in lat.SUB.items() if poly.get((p,), 0)}
        red.add(vec)
    check("X0 Gauss surface parametrisation", ok_div and len(red.basis) == 2 * 27 + 1,
          f"E = curl^T b + h: div = 0 identically ({ok_div}); rank {len(red.basis)} = dim ker(div) = 2L^3+1 (L=3): 'mod Gauss' below allows Gauss "
          "terms with arbitrary, even nonlocal, field-dependent multipliers")
    table = {}
    for link in ("mean", "tail", "head"):
        for plaq in ("four", "diagonal", "antidiagonal", "c00", "c10", "c01", "c11"):
            _, ex, mg, nb = classify_poly(lat, scheme(link, plaq))
            table[(link, plaq)] = (ex, mg, nb)
    closing = sorted(k for k, v in table.items() if v[0])
    closing_g = sorted(k for k, v in table.items() if v[1])
    check("X1 21 uniform timings (polynomial path, symbolic lapses, L=3)", closing == [("head", "c11"), ("tail", "c00")] and closing_g == closing,
          f"{{H_EM(N), H_EM(M)}} depends on (N, M) only through bond xi~ exactly for {closing}, also mod Gauss; the reflection-symmetric "
          f"(mean, four) leaves {table[('mean', 'four')][2]} non-bond lapse pairs")
    oks = [classify_poly(lat, scheme(o, "oriented"))[1] for o in product(("tail", "head"), repeat=3)]
    _, exw, mgw, _ = classify_poly(lat, scheme(("tail", "head", "tail"), "c00"))
    check("X2 the 8 one-sided classes close, a mismatched corner fails", all(oks) and not exw and not mgw,
          "each axis timed at its tail or its head, each plaquette at the corner where its two axes' chosen endpoints meet: all 8 bond-supported; "
          "a mismatched corner fails even mod Gauss")
    red = Reducer()
    for x in lat.SITES:
        red.add(lat.gauss(x))
    rk = len(red.basis)
    inv = lat.inv()
    added = 0
    for mo in lat.Fpl(lat.SITES[0], 0, 1):
        nm = inv[mo[0]]
        before = len(red.basis)
        red.add(lat.Ev(nm[1], nm[2]))
        added += len(red.basis) > before
    check("X3 Gauss cannot rescue a plaquette residual", rk == 26 and added == 4,
          f"span{{Gauss_x}} (rank {rk} = L^3-1) meets span{{E_l: l on one plaquette}} only in 0")
    # T2e hand-derived local equations (sympy)
    u = {d: sp.symbols(f"u{d}t u{d}h") for d in range(3)}
    w = {ij: sp.symbols(f"w{ij[0]}{ij[1]}_00 w{ij[0]}{ij[1]}_10 w{ij[0]}{ij[1]}_01 w{ij[0]}{ij[1]}_11") for ij in PAIRS}
    eqs = [u[d][0] + u[d][1] - 1 for d in range(3)]
    for (i, j) in PAIRS:
        W = dict(zip(["00", "10", "01", "11"], w[(i, j)]))
        eqs.append(sum(W.values()) - 1)
        for (tl, hd, ax) in (("00", "10", i), ("01", "11", i), ("00", "01", j), ("10", "11", j)):
            U = {tl: u[ax][0], hd: u[ax][1]}
            for (c1, d1) in (("00", "11"), ("10", "01")):
                eqs.append(sp.expand(U.get(c1, 0) * W[d1] - U.get(d1, 0) * W[c1]))
    unk = [s for d in range(3) for s in u[d]] + [s for ij in PAIRS for s in w[ij]]
    sols = sp.solve(eqs, unk, dict=True)
    full = [s for s in sols if len(s) == len(unk)]
    sym_ok = all(not (s[u[d][0]] == s[u[d][1]]) for s in full for d in range(3))
    check("X4 local classification (hand-derived equations, sympy)", len(sols) == 8 and len(full) == 8 and sym_ok,
          "over all translation-invariant corner-supported timings (2 weights per link axis, 4 per plaquette plane, normalised) the diagonal-pair "
          "conditions u_ls w_pt = u_lt w_ps (s, t opposite corners) have exactly 8 solutions: one-sided on every axis, matching corner")
    # path 2: classification from the computed incidence-formula bracket at L = 4, exact, with exact mod-Gauss restriction
    il = ILat(4)
    ut = {j: sp.Symbol(f"u{j}t") for j in range(3)}
    uh = {j: sp.Symbol(f"u{j}h") for j in range(3)}
    wn = {ij: {n: sp.Symbol(f"w{ij[0]}{ij[1]}_{n}") for n in ("00", "10", "01", "11")} for ij in PAIRS}
    usyms = [ut[j] for j in range(3)] + [uh[j] for j in range(3)]
    wsyms = [wn[ij][n] for ij in PAIRS for n in ("00", "10", "01", "11")]
    mons = [(ai, bi) for ai in range(len(usyms)) for bi in range(len(wsyms))]
    mid = {m: i for i, m in enumerate(mons)}
    rows_e, rows_g = {}, {}
    for ai, us in enumerate(usyms):
        for bi, ws in enumerate(wsyms):
            lw = {j: (F(int(us == ut[j])), F(int(us == uh[j]))) for j in range(3)}
            pw = {ij: {n: F(int(ws == wn[ij][n])) for n in wn[ij]} for ij in PAIRS}
            uu, ww = uniform_timing(il, lw, pw)
            for (s, t), d in em_pair_coeffs(il, uu, ww).items():
                if s != O3 or il.is_bond(s, t) or s == t:
                    continue
                for key, v in d.items():
                    rows_e.setdefault((t, key), {})[mid[(ai, bi)]] = v
                for key, v in transverse(il, d).items():
                    rows_g.setdefault((t, key), {})[mid[(ai, bi)]] = v
    mon_expr = [usyms[a] * wsyms[b] for (a, b) in mons]
    norm = [ut[j] + uh[j] - 1 for j in range(3)] + [sum(wn[ij].values()) - 1 for ij in PAIRS]

    def solve_rows(rows):
        red = Reducer()
        for r in rows.values():
            red.add(r)
        eqs_ = [sum(sp.Rational(v.numerator, v.denominator) * mon_expr[c] for c, v in b.items()) for _, b in red.basis]
        return len(eqs_), sp.solve(eqs_ + norm, usyms + wsyms, dict=True)
    ne, sol_e = solve_rows(rows_e)
    ng, sol_g = solve_rows(rows_g)
    canon = lambda ss: sorted(tuple(sorted((str(k), str(v)) for k, v in s.items())) for s in ss)
    good = len(sol_e) == 8 and all(len(s) == len(usyms) + len(wsyms) for s in sol_e)
    for s in sol_e:
        for j in range(3):
            good &= {s[ut[j]], s[uh[j]]} == {0, 1}
        for (i, j) in PAIRS:
            cij = ("0" if s[ut[i]] == 1 else "1") + ("0" if s[ut[j]] == 1 else "1")
            for n in ("00", "10", "01", "11"):
                good &= s[wn[(i, j)][n]] == (1 if n == cij else 0)
    check("X5 classification from the computed bracket (incidence path, L=4, exact and mod Gauss)", good and canon(sol_e) == canon(sol_g),
          f"{ne} independent bilinear conditions exactly, {ng} mod Gauss (exact transverse restriction); both give the same 8 one-sided classes "
          "and no reflection-symmetric timing in this class")
    return il


def random_timing(lat, rng, sweeps=6):
    OPP = {"00": "11", "11": "00", "10": "01", "01": "10"}

    def plaq_ok(u, p):
        cs = lat.corners(p)
        inv = {v: k for k, v in cs.items()}
        U = {inv[s] for a in lat.Fp[p] for s in u[a]}
        return [n for n in cs if OPP[n] not in U]
    o = [rng.choice("th") for _ in range(3)]
    u = [{x: F(1)} if o[j] == "t" else {lat.sh(x, j): F(1)} for (x, j) in lat.links]
    for _ in range(sweeps * len(lat.links)):
        k = rng.randrange(len(lat.links))
        x, j = lat.links[k]
        y = lat.sh(x, j)
        ch = rng.choice(["t", "h", "b"])
        a = F(rng.randint(1, 3), 4)
        new = {x: F(1)} if ch == "t" else ({y: F(1)} if ch == "h" else {x: a, y: 1 - a})
        old = u[k]
        u[k] = new
        if not all(plaq_ok(u, p) for (p, s) in lat.inc[k]):
            u[k] = old
    w = []
    for p in range(len(lat.plaqs)):
        cs = lat.corners(p)
        allowed = plaq_ok(u, p)
        pick = rng.sample(allowed, rng.randint(1, len(allowed)))
        wt = [F(rng.randint(1, 4)) for _ in pick]
        tot = sum(wt)
        w.append({cs[n]: v / tot for n, v in zip(pick, wt)})
    return u, w, sum(len(d) == 2 for d in u), plaq_ok


def part_X_local_rule(il, nsamp=12):
    section("Part X2: spin 1, local timing rule and the staggered counterexample (exact)")
    rng = random.Random(11)
    OPP = {"00": "11", "11": "00", "10": "01", "01": "10"}
    ok_obey, both = True, 0
    for _ in range(nsamp):
        u, w, nb2, _ = random_timing(il, rng)
        both += nb2
        ok_obey &= bondsupport(il, u, w)[0] == 0
    fails, tried = 0, 0
    while tried < nsamp:
        u, w, _, _ = random_timing(il, rng, sweeps=2)
        p = rng.randrange(len(il.plaqs))
        cs = il.corners(p)
        inv = {v: k for k, v in cs.items()}
        U = {inv[s] for a in il.Fp[p] for s in u[a]}
        bad = [n for n in cs if OPP[n] in U]
        if not bad:
            continue
        tried += 1
        n = rng.choice(bad)
        w[p] = {k: v / 2 for k, v in w[p].items()}
        w[p][cs[n]] = w[p].get(cs[n], 0) + F(1, 2)
        fails += bondsupport(il, u, w, gauss=True)[0] > 0
    check("X6 exact local rule (random position-dependent timings, L=4)", ok_obey and fails == nsamp,
          f"{nsamp} random timings obeying 'each plaquette weights only corners whose opposite corner is not covered by its links' timing supports' "
          f"(mean {both / nsamp:.1f} two-sided links each) are all bond-supported; {fails}/{nsamp} timings violating it at one plaquette fail, "
          "even mod Gauss (exact transverse restriction)")
    ok = True
    for i in range(3):
        for other in ("t", "h"):
            u = []
            for (x, j) in il.links:
                y = il.sh(x, j)
                u.append({x: F(1, 2), y: F(1, 2)} if j == i else ({x: F(1)} if other == "t" else {y: F(1)}))
            for p, (y0, (a, b)) in enumerate(il.plaqs):
                if i in (a, b):
                    cs = il.corners(p)
                    inv = {v: k for k, v in cs.items()}
                    ok &= len({inv[s] for aa in il.Fp[p] for s in u[aa]}) == 4
    check("X7 a two-sided axis leaves no admissible plaquette weight", ok,
          "translation-invariant timing with any two-sided axis i: every (i,j) plaquette has all 4 corners covered, so by the local rule only the "
          "8 one-sided classes survive (agrees with X1-X5)")
    u, w = uniform_timing(il, {j: (F(1, 2), F(1, 2)) for j in range(3)}, {ij: {n: F(1, 4) for n in ("00", "10", "01", "11")} for ij in PAIRS})
    nb_sym, _ = bondsupport(il, u, w)
    nb_sym_g, _ = bondsupport(il, u, w, gauss=True)
    u, w = staggered(il, 0)
    nb, _ = bondsupport(il, u, w)

    def refl(x):
        return tuple((-x[k]) % il.L for k in range(3))
    sym_ok = True
    for k, (x, j) in enumerate(il.links):
        sym_ok &= {refl(s): v for s, v in u[k].items()} == u[il.lidx[(il.sh(refl(x), j, -1), j)]]
    for p, (y, (i, j)) in enumerate(il.plaqs):
        sym_ok &= {refl(s): v for s, v in w[p].items()} == w[il.pidx[(il.sh(il.sh(refl(y), i, -1), j, -1), (i, j))]]
    for ax in range(3):
        ra = lambda x, ax=ax: tuple((-x[k]) % il.L if k == ax else x[k] for k in range(3))
        for k, (x, j) in enumerate(il.links):
            x2 = il.sh(ra(x), j, -1) if j == ax else ra(x)
            sym_ok &= {ra(s): v for s, v in u[k].items()} == u[il.lidx[(x2, j)]]
        for p, (y, (i, j)) in enumerate(il.plaqs):
            y2 = il.sh(ra(y), ax, -1) if ax in (i, j) else ra(y)
            sym_ok &= {ra(s): v for s, v in w[p].items()} == w[il.pidx[(y2, (i, j))]]
    check("X8 staggered reflection-symmetric timing closes (outside the translation-invariant class)", nb_sym > 0 and nb_sym_g == nb_sym and nb == 0 and sym_ok,
          f"L=4: (mean, four) leaves {nb_sym // 2} unordered non-bond pairs, none removed mod Gauss; links at their even endpoint and plaquettes at "
          "the mean of their two odd corners give an exactly bond-supported bracket, invariant under every axis reflection and the point "
          "reflection about an even site; it breaks unit translations to the even sublattice (its generator: X13, caveat in --diag)")
    return u, w


def part_X_bracket_cone(il, stag):
    section("Part X3: spin 1, bracket, cone and normalisation (exact)")
    lat = MLat(3)
    cb, g2 = F(3, 2), F(5, 7)
    br = pbracket(lat, h_em(lat, "N", cb, g2), h_em(lat, "M", cb, g2))
    xs = {}
    for y in lat.SITES:
        for i in range(3):
            xs[(y, i)] = pscale(padd(pmul(lat.lapse("N", lat.sh(y, i)), lat.lapse("M", y)), pmul(lat.lapse("N", y), lat.lapse("M", lat.sh(y, i))), F(-1)), -cb)
    check("X9 exact Maxwell bracket (polynomial path, symbolic lapses)", not padd(br, g_A(lat, xs), F(-1)),
          "forward timing: {H_EM(N), H_EM(M)} = G_A[-cB xi~] exactly, xi~_(y,i) = N_(y+i) M_y - N_y M_(y+i); g cancels (g^2 x cB/g^2)")
    i4 = ILat(4)
    u, w = fwd_timing(i4)
    Xf, Xb = induced_generator(i4, u, w, F(3, 2)), fwd_GA(i4)
    check("X10 induced generator = G_A (incidence path, L=4)", all(Xf.get(b, {}) == Xb.get(b, {}) for b in set(Xf) | set(Xb)),
          "the generator the forward-timed bracket induces, bracket / (-cB), equals the stated G_A[xi] = sum xi_(y,i) E_(y+i,j) F_ij(y) bond by bond")
    rng = random.Random(20261018 + 16)
    rf = lambda: {x: F(rng.randint(-3, 3)) for x in lat.SITES}
    n, m = rf(), rf()
    UB = [cm.unit_bond(lat, x, j) for x in lat.SITES for j in range(3)]
    cols = [padd(cm.g_grav(lat, xi), g_A(lat, xi)) for xi in UB]
    KK, AL = lat.KK, lat.ALPHA
    kappa = KK / (4 * AL)
    res = {}
    for s in (F(-1), F(1)):
        cg, cmm = padd(cm.kin(lat, n), pscale(cm.r1(lat, n), s * KK)), padd(cm.kin(lat, m), pscale(cm.r1(lat, m), s * KK))
        for gg in (F(1), F(9, 4)):
            for cbv in (kappa, 2 * kappa, kappa / 3, -kappa):
                res[(int(s), str(gg), str(cbv / kappa))] = in_span(pbracket(lat, padd(cg, h_em(lat, n, cbv, gg)), padd(cmm, h_em(lat, m, cbv, gg))), cols)
    expect = {k: (F(k[2]) == -k[0]) for k in res}
    check("X11 one cone for spin 1: cB = -sK/(4 alpha), g-independent", res == expect,
          f"gravity + Maxwell (forward timing): the order-eps bracket closes into ONE G_g[xi] + G_A[xi] iff cB = -sK/(4alpha) for both g^2 = 1, 9/4; "
          f"the Maxwell mode's speed^2 = g^2 (cB/g^2) = cB; table {{(s, g^2, cB/kappa): closes}} = {res}")
    cols2 = [padd(cm.g_grav(lat, xi), pscale(g_A(lat, xi), F(2))) for xi in UB]
    cg, cmm = padd(cm.kin(lat, n), pscale(cm.r1(lat, n), -KK)), padd(cm.kin(lat, m), pscale(cm.r1(lat, m), -KK))
    r2 = {str(cbv / kappa): in_span(pbracket(lat, padd(cg, h_em(lat, n, cbv, F(1))), padd(cmm, h_em(lat, m, cbv, F(1)))), cols2) for cbv in (kappa, 2 * kappa)}
    xi_u = {(x, j): F(1) if j == 0 else F(0) for x in lat.SITES for j in range(3)}
    ga = g_A(lat, xi_u)
    ok = True
    for z in lat.SITES:
        for j in range(3):
            exp = padd(lat.Av(z, j), lat.Av(lat.sh(z, 0, -1), j), F(-1))
            exp = padd(exp, padd(lat.Av(lat.sh(lat.sh(z, j), 0, -1), 0), lat.Av(lat.sh(z, 0, -1), 0), F(-1)), F(-1))
            ok = ok and not padd(pbracket(lat, lat.Av(z, j), ga), exp, F(-1))
    gm = cm.g_matter(lat, xi_u)
    ok2 = all(not padd(pbracket(lat, term(1, lat.var(("phi", z))), gm), padd(term(F(1, 2), lat.var(("phi", lat.sh(z, 0)))), term(F(-1, 2), lat.var(("phi", lat.sh(z, 0, -1))))), F(-1)) for z in lat.SITES)
    check("X12 the cone is tied to the generator normalisation, which is the unit translation", r2 == {"1": False, "2": True} and ok and ok2,
          f"rescaling G_A -> 2 G_A moves closure to cB = 2 kappa ({r2}); {{A_(z,j), G_A[e_0 uniform]}} = A_(z,j) - A_(z-e0,j) + gauge gradient "
          "(unit backward translation) and {phi_z, G_m[e_0]} = (phi_(z+e0) - phi_(z-e0))/2 (unit central translation): both sectors carry the "
          "same unit normalisation (N1: {G,G} forces matter sectors to share one structure constant; their ratio to gravity's linear shift is supplied)")
    tcols = [padd(c_, cm.g_matter(lat, xi)) for c_, xi in zip(cols, UB)]
    t4 = {}
    for c in (kappa, 2 * kappa):
        for cbv in (kappa, 2 * kappa):
            t4[(str(c / kappa), str(cbv / kappa))] = in_span(pbracket(lat, padd(padd(cg, cm.h_matter(lat, n, c)), h_em(lat, n, cbv, F(4, 9))),
                                                                       padd(padd(cmm, cm.h_matter(lat, m, c)), h_em(lat, m, cbv, F(4, 9)))), tcols)
    check("X12b scalar + Maxwell + gravity: one common cone (L=3)", t4 == {("1", "1"): True, ("1", "2"): False, ("2", "1"): False, ("2", "2"): False},
          f"s = -1, scalar (endpoint-mean timing, G_m) + Maxwell (forward timing, G_A): one total relabelling G_g + G_m + G_A iff "
          f"c_phi = cB = K/(4alpha); {{(c/kappa, cB/kappa): closes}} = {t4}")
    # staggered: closure relative to its own induced generator (L=4)
    us, ws = stag
    Xs = induced_generator(il, us, ws, F(1))
    lat4 = MLat(4)

    def gpoly(X, xi):
        out = {}
        for b, d in X.items():
            if xi.get(b, 0) == 0:
                continue
            for (k, a), v in d.items():
                (x1, j1), (x2, j2) = il.links[k], il.links[a]
                out = padd(out, term(xi[b] * v, lat4.var(("E", x1, j1)), lat4.var(("A", x2, j2))))
        return out
    rng4 = random.Random(5)
    n4 = {x: F(rng4.randint(-3, 3)) for x in lat4.SITES}
    m4 = {x: F(rng4.randint(-3, 3)) for x in lat4.SITES}
    k4 = lat4.KK / (4 * lat4.ALPHA)
    cols4 = []
    for x in lat4.SITES:
        for j in range(3):
            ub = cm.unit_bond(lat4, x, j)
            cols4.append(padd(cm.g_grav(lat4, ub), gpoly(Xs, ub)))
    gb = pbracket(lat4, padd(cm.kin(lat4, n4), pscale(cm.r1(lat4, n4), -lat4.KK)), padd(cm.kin(lat4, m4), pscale(cm.r1(lat4, m4), -lat4.KK)))
    rs = {}
    for r in (F(1), F(2)):
        emb = pbracket(lat4, h_em_general(lat4, n4, us, ws, r * k4, F(1), il), h_em_general(lat4, m4, us, ws, r * k4, F(1), il))
        rs[str(r)] = in_span(padd(gb, emb), cols4)
    check("X13 staggered timing: same cone relative to its induced generator (L=4; consistency check)", rs == {"1": True, "2": False},
          f"s = -1: gravity + staggered Maxwell closes into one G_g[xi] + G'[xi] iff cB = kappa ({rs}); automatic once the bracket is bond-supported, "
          "since G' is the generator the bracket induces; the cone value has content only through G''s normalisation, whose "
          "smooth-field normalisation carries an O(1) doubler component (campaign check, floating point; --diag)")


def part_X_gauss_compact_obstruction():
    section("Part X4: spin 1, Gauss multipliers, compact U(1), uniform-shift obstruction (exact)")
    lat = MLat(3)
    rng = random.Random(20261018 + 160)
    rf = lambda: {x: F(rng.randint(-3, 3)) for x in lat.SITES}
    n, m, th, th2 = rf(), rf(), rf(), rf()
    xi = {k: F(rng.randint(-3, 3)) for k in cm.unit_bond(lat, lat.SITES[0], 0)}
    KK, AL = lat.KK, lat.ALPHA
    kappa = KK / (4 * AL)
    cb, g2 = kappa, F(9, 4)
    gth = gauss_poly(lat, th)
    a1 = not pbracket(lat, gth, h_em(lat, n, cb, g2))
    a2 = not pbracket(lat, gth, g_A(lat, xi))
    a3 = not pbracket(lat, gth, gauss_poly(lat, th2))
    a4 = in_span(pbracket(lat, gth, g_L(lat, xi)), [lat.gauss(x) for x in lat.SITES])
    check("X14 Gauss is first class", a1 and a2 and a3 and a4,
          "{Gauss[theta], H_EM(N)} = {Gauss[theta], G_A[xi]} = {Gauss, Gauss} = 0 exactly; {Gauss[theta], G_L[xi]} is a pure Gauss term")
    xt = cm.xi_tilde(lat, n, m)
    xin = {k: -cb * v for k, v in xt.items()}
    br_em = pbracket(lat, h_em(lat, n, cb, g2), h_em(lat, m, cb, g2))
    t5b = not padd(br_em, padd(g_L(lat, xin), gauss_poly(lat, theta_of(lat, xin))), F(-1))
    cg = padd(padd(cm.kin(lat, n), pscale(cm.r1(lat, n), -KK)), h_em(lat, n, cb, g2))
    cmm = padd(padd(cm.kin(lat, m), pscale(cm.r1(lat, m), -KK)), h_em(lat, m, cb, g2))
    br = pbracket(lat, cg, cmm)
    UB = [cm.unit_bond(lat, x, j) for x in lat.SITES for j in range(3)]
    colsL = [padd(cm.g_grav(lat, u), g_L(lat, u)) for u in UB]
    no = in_span(br, colsL)
    yes_t = in_span(lat.subst(br), [lat.subst(c) for c in colsL])
    loc = colsL + [pmul(lat.gauss(w), lat.Av(lat.sh(w, i, -1), i)) for w in lat.SITES for i in range(3)] + [pmul(lat.gauss(w), lat.Av(w, i)) for w in lat.SITES for i in range(3)]
    check("X15 Gauss enters {C,C} with a field-dependent multiplier unless G_A is used", t5b and (not no) and yes_t and in_span(br, loc),
          "with the pure-translation generator G_L = G_A - Gauss[theta(xi, A)]: {H_EM(N), H_EM(M)} = G_L[-cB xi~] + Gauss[lambda], "
          "lambda_w = -cB sum_i xi~_(w-i,i) A_(w-i,i) exactly; the full algebra with G_g + G_L does not close into relabellings, closes on the "
          "Gauss surface, and closes exactly once local terms Gauss_w A_l are allowed")
    # compact U(1)
    Asym = {(x, j): sp.Symbol(f"A_{x[0]}{x[1]}{x[2]}_{j}") for x in lat.SITES for j in range(3)}
    Esym = {(x, j): sp.Symbol(f"E_{x[0]}{x[1]}{x[2]}_{j}") for x in lat.SITES for j in range(3)}
    sh = lat.sh
    Fs = lambda y, i, j: Asym[(sh(y, i), j)] - Asym[(y, j)] - Asym[(sh(y, j), i)] + Asym[(y, i)]
    cbs, g2s = sp.Rational(3, 2), sp.Rational(5, 7)

    def Hc(nn):
        out = 0
        for x in lat.SITES:
            for j in range(3):
                out += sp.Rational(nn[x]) * g2s / 2 * Esym[(x, j)] ** 2
        for y in lat.SITES:
            for (i, j) in PAIRS:
                out += sp.Rational(nn[y]) * cbs / g2s * (1 - sp.cos(Fs(y, i, j)))
        return out
    Hn, Hm_ = Hc(n), Hc(m)
    brc = sum(sp.diff(Hn, Asym[k]) * sp.diff(Hm_, Esym[k]) - sp.diff(Hn, Esym[k]) * sp.diff(Hm_, Asym[k]) for k in Asym)
    rhs = 0
    for y in lat.SITES:
        for i in range(3):
            vv = -cbs * sp.Rational(xt[(y, i)])
            if vv:
                for j in range(3):
                    if j != i:
                        rhs += vv * Esym[(sh(y, i), j)] * sp.sin(Fs(y, i, j))
    check("X16 compact U(1)", sp.expand(brc - rhs) == 0,
          "H_B = sum Nplaq (cB/g^2)(1 - cos F_p): {H(N), H(M)} = G_A^c[-cB xi~], G_A^c[xi] = sum xi_(y,i) E_(y+i,j) sin F_ij(y), exactly to all "
          "orders in the field: timing selection and cone unchanged by compactness")
    # uniform shift
    one = {x: F(1) for x in lat.SITES}
    xi_u = {(x, j): F(1) if j == 0 else F(0) for x in lat.SITES for j in range(3)}
    R1 = pbracket(lat, g_A(lat, xi_u), h_em(lat, one, cb, g2))
    dE, dF, gt = {}, {}, {}
    for x in lat.SITES:
        for j in range(3):
            d = padd(lat.Ev(x, j), lat.Ev(sh(x, 0, -1), j), F(-1))
            dE = padd(dE, pmul(d, d))
    for y in lat.SITES:
        for ij in PAIRS:
            d = padd(lat.Fpl(y, *ij), lat.Fpl(sh(y, 0, -1), *ij), F(-1))
            dF = padd(dF, pmul(d, d))
    for w in lat.SITES:
        gt = padd(gt, pmul(lat.Ev(sh(w, 0, -1), 0), lat.gauss(w)))
    ident = padd(padd(pscale(dE, g2 / 2), pscale(dF, -cb / (2 * g2))), pscale(gt, g2))
    check("X17 exact uniform-shift defect identity (polynomial path, L=3)", (not cm.g_grav(lat, xi_u)) and not padd(R1, ident, F(-1)),
          "G_g[uniform shift] = 0 identically, so no h- or P-coupling enters {G[e0], C(N)} at order (matter^2, h^0); and "
          "{G_A[e0], H_EM(1)} = (g^2/2) sum_l (E_l - E_(l-e0))^2 - (cB/(2g^2)) sum_p (F_p - F_(p-e0))^2 + g^2 sum_w E_(w-e0,0) Gauss_w")
    ok_id2 = all(incidence_identity(LL) for LL in ((3, 4) if FULL else (3,)))
    check("X18 uniform-shift identity (incidence/quadratic-form path)", ok_id2,
          f"same identity from the closed bilinear forms of the second engine at L = {'3, 4' if FULL else '3 (L = 4 with --full)'}")
    hcols = [lat.subst(h_em(lat, {z: F(1) if z == x else F(0) for z in lat.SITES}, cb, g2)) for x in lat.SITES]
    Rn = pbracket(lat, g_A(lat, xi_u), h_em(lat, n, cb, g2))
    sm1 = pbracket(lat, cm.g_matter(lat, xi_u), cm.h_matter(lat, one, kappa))
    smn = pbracket(lat, cm.g_matter(lat, xi_u), cm.h_matter(lat, n, kappa))
    scols = [cm.h_matter(lat, {z: F(1) if z == x else F(0) for z in lat.SITES}, kappa) for x in lat.SITES]
    check("X19 coupling-independent lattice {G,C} obstruction; scalar comparison",
          (not in_span(lat.subst(R1), hcols)) and (not in_span(lat.subst(Rn), hcols)) and (not sm1) and not in_span(smn, scols),
          "{G_A[uniform], H_EM(N)} is not H_EM(N') for any N', even on the Gauss surface, at N = 1 and random N; the scalar has "
          "{G_m[uniform], H_m(1)} = 0 but {G_m[uniform], H_m(N)} is not H_m(N') either, so the upstream O(a^2) obstruction also occurs where "
          "G_g = 0 and does not depend on the coupling ansatz")
    # cause: one-sided (non-antisymmetric) action on F vs central action on phi
    okF = all(not padd(pbracket(lat, lat.Fpl(y, *ij), g_A(lat, xi_u)), padd(lat.Fpl(y, *ij), lat.Fpl(sh(y, 0, -1), *ij), F(-1)), F(-1)) for y in lat.SITES for ij in PAIRS)
    okEf = all(not padd(pbracket(lat, lat.Ev(z, j), g_L(lat, xi_u)), padd(lat.Ev(sh(z, 0), j), lat.Ev(z, j), F(-1)), F(-1)) for z in lat.SITES for j in range(3))
    check("X20 cause of the O(a) defect: G_A acts by one-sided differences", okF and okEf and not sm1,
          "{F_p, G_A[e0]} = F_p - F_(p-e0) (backward) and {E_l, G_L[e0]} = E_(l+e0) - E_l (forward): the one-sided operator D = 1 - T^-1 is not "
          "antisymmetric, D + D^T = 2 - T - T^-1, which is exactly the sum of squared differences in X17; the scalar's central G_m is "
          "antisymmetric and gives 0. With D ~ a d, the defect is O(a) relative to H(xi.grad N) (power count; --diag measures it)")


def incidence_identity(L):
    lat = ILat(L)
    g2, cb = F(9, 4), F(35, 132)
    X = fwd_GA(lat)
    G = {}
    for b, d in X.items():
        if b[1] == 0:
            for ka, v in d.items():
                G[ka] = G.get(ka, 0) + v

    def qadd(Q, i, j, v):
        key = (min(i, j), max(i, j))
        Q[key] = Q.get(key, 0) + v
        if Q[key] == 0:
            del Q[key]
    QE, QA, CE, CA = {}, {}, {}, {}
    for (k, a), v in G.items():
        qadd(QE, k, a, g2 * v)
        for (p, s) in lat.inc[k]:
            for a2, f in lat.Fp[p].items():
                qadd(QA, a, a2, -(cb / g2) * v * s * f)
    for k, (x, j) in enumerate(lat.links):
        km = lat.lidx[(lat.sh(x, 0, -1), j)]
        for (i1, s1) in ((k, 1), (km, -1)):
            for (i2, s2) in ((k, 1), (km, -1)):
                if i1 <= i2:
                    qadd(CE, i1, i2, (g2 / 2) * s1 * s2 * (1 if i1 == i2 else 2))
    for p, (y, ij) in enumerate(lat.plaqs):
        pm = lat.pidx[(lat.sh(y, 0, -1), ij)]
        diff = dict(lat.Fp[p])
        for a, f in lat.Fp[pm].items():
            diff[a] = diff.get(a, 0) - f
        items = [(a, f) for a, f in diff.items() if f]
        for x1, (a1, f1) in enumerate(items):
            for x2, (a2, f2) in enumerate(items):
                if x1 <= x2:
                    qadd(CA, a1, a2, -(cb / (2 * g2)) * f1 * f2 * (1 if a1 == a2 else 2))
    for w in lat.sites:
        kq = lat.lidx[(lat.sh(w, 0, -1), 0)]
        for j in range(3):
            qadd(CE, kq, lat.lidx[(w, j)], g2)
            qadd(CE, kq, lat.lidx[(lat.sh(w, j, -1), j)], -g2)
    return QE == CE and QA == CA


def part_X_continuum():
    section("Part X5: spin 1, continuum leading order (exact jet calculus)")
    JE.reset(with_em=True)
    J, K, al, g2, cB = JE.J, JE.K, JE.al, JE.g2, JE.cB
    kappa = K / (4 * al)
    N, M = JE.N, JE.M
    XI0 = [N * gm - M * gn for gn, gm in zip(JE.grad("N"), JE.grad("M"))]
    CN = N * (JE.kin() - K * JE.r1() + JE.hem())
    CM = M * (JE.kin() - K * JE.r1() + JE.hem())
    br = JE.bracket(CN, CM)
    xi = [kappa * x for x in XI0]
    sol = sp.solve(JE.coeffs(JE.euler(br - JE.gg_vec(xi) - JE.poynting(xi), "N")), cB, dict=True)
    check("X21 continuum cone", sol == [{cB: K / (4 * al)}],
          f"{{C(N), C(M)}} = G_g[xi0] + P_A[xi0], xi0 = kappa (N grad M - M grad N), C = kin - K R1 + H_EM, exactly (no Gauss term) iff {sol}; g drops out")
    rr = sp.Symbol("rr")
    base = br.subs(cB, kappa) - JE.gg_vec(xi) - JE.lie_gen_vec(xi)
    res0 = JE.euler(base, "N")
    xa = sum(xi[k] * J(JE.AN[k]) for k in range(3))
    solr = sp.solve(JE.coeffs(JE.euler(base - rr * xa * JE.divE(), "N")), rr, dict=True)
    check("X22 continuum: with the Lie generator {C,C} needs Gauss[xi0.A]", bool(JE.coeffs(res0)) and not JE.coeffs(JE.on_gauss(res0)) and solr == [{rr: 1}],
          f"{{C,C}} - G_g[xi0] - G_Lie[xi0] != 0 but vanishes on div E = 0, and equals Gauss[r xi0.A] with {solr}")
    # metric-variational comparator (exact O(eps) expansions)
    eps = sp.Symbol("eps")
    HV = [J(JE.HD[j]) for j in range(3)] + [J(JE.HF[ij]) for ij in PAIRS]
    hmat = sp.Matrix([[HV[0], HV[3], HV[4]], [HV[3], HV[1], HV[5]], [HV[4], HV[5], HV[2]]])
    FPH = {ij: sp.Symbol(f"Fph{ij[0]}{ij[1]}") for ij in PAIRS}
    TOFV = {FPH[ij]: JE.Fij(*ij) for ij in PAIRS}
    EV = [J(e) for e in JE.EN]
    Ev = sp.Matrix(EV)
    Fm = sp.zeros(3, 3)
    for (i, j), f in FPH.items():
        Fm[i, j], Fm[j, i] = f, -f
    gm_ = sp.eye(3) + eps * hmat
    gi = sp.eye(3) - eps * hmat
    trh = hmat.trace()
    dens = g2 / 2 * (Ev.T * gm_ * Ev)[0] * (1 - eps * trh / 2) + cB / (4 * g2) * (1 + eps * trh / 2) * (gi * Fm * gi * Fm.T).trace()
    lin = sp.expand(sp.diff(sp.expand(dens), eps).subs(eps, 0))
    form = g2 / 2 * (sum(hmat[i, j] * EV[i] * EV[j] for i in range(3) for j in range(3)) - trh * sum(e ** 2 for e in EV) / 2) \
        + cB / g2 * (trh * sum(f ** 2 for f in FPH.values()) / 4 - sp.Rational(1, 2) * sum(hmat[i, j] * Fm[i, k] * Fm[j, k] for i in range(3) for j in range(3) for k in range(3)))
    check("X23 comparator: metric-variational Maxwell stress", sp.expand(lin - form) == 0,
          "O(h) part of (g^2/2) g_ij E^i E^j/sqrt g + (cB/4g^2) sqrt g g^ik g^jl F_ij F_kl (E a vector density, A a one-form) = "
          "(g^2/2)(h_ij E^i E^j - tr h E^2/2) + (cB/g^2)(tr h sum_(i<j) F^2/4 - h_ij F_ik F_jk/2)")
    VARS6 = EV + [FPH[ij] for ij in PAIRS]
    MONOS = [VARS6[a] * VARS6[b] for a in range(6) for b in range(a, 6)]
    QC = [[sp.Symbol(f"q{c_}_{k}") for k in range(len(MONOS))] for c_ in range(6)]
    QALL = [s for row in QC for s in row]
    coup = sp.expand(sum(HV[c_] * sum(QC[c_][k] * MONOS[k] for k in range(len(MONOS))) for c_ in range(6)).xreplace(TOFV))
    s1, s2, lam = sp.symbols("s1 s2 lam")
    XIN = ["xi0", "xi1", "xi2"]
    xiv = [J(n_) for n_ in XIN]
    brg = JE.bracket(JE.poynting(xiv), N * JE.hem()) + JE.bracket(JE.gg_names(XIN), N * coup)
    nprime = s1 * sum(xiv[k] * JE.grad("N")[k] for k in range(3)) + s2 * N * sum(J(XIN[k], JE.ev(k)) for k in range(3))
    eqs2 = JE.coeffs(JE.on_gauss(JE.euler(brg - nprime * JE.hem(), "N")))
    sol2 = sp.solve(eqs2, QALL + [s1, s2], dict=True)

    def coupling_values(d):
        poly = sp.Poly(sp.expand(d), *(HV + VARS6))
        return {QC[c_][k]: sp.expand(poly.coeff_monomial(HV[c_] * MONOS[k])) for c_ in range(6) for k in range(len(MONOS))}
    expv = coupling_values(lin)
    hem_ph = g2 / 2 * sum(e ** 2 for e in EV) + cB / (2 * g2) * sum(f ** 2 for f in FPH.values())
    lamv = coupling_values(sp.expand(lam * trh * hem_ph))
    ok2 = False
    if len(sol2) == 1:
        s_ = sol2[0]
        free = sorted(set(QALL + [s1, s2]) - set(s_), key=str)
        if len(free) == 1:
            sub = {free[0]: sp.solve(sp.Eq(sp.sympify(s_.get(s2, s2)), -2 * lam), free[0])[0]}
            fullv = {k: sp.simplify(sp.sympify(s_.get(k, k)).subs(sub)) for k in QALL + [s1, s2]}
            ok2 = all(sp.simplify(fullv[k] - expv[k] - lamv[k]) == 0 for k in QALL) and fullv[s1] == 1
    check("X24 {G,C} selects the Maxwell metric stress + lambda (126-coefficient ansatz, mod Gauss)", ok2,
          "{P_A[xi] + G_g[xi], H_EM(N) + int N h.Q(E,F)} at O(E^2, F^2) = H_EM(s1 xi.grad N + s2 N div xi) mod Gauss over a general quadratic "
          "Q per strain component (6 x 21 coefficients, no isotropy imposed): ONE-parameter family = metric stress (X23) + lam tr h H_EM, "
          "s1 = 1, s2 = -2 lam")
    coup_exp = lin.xreplace(TOFV)
    xE = sum(xiv[k] * J(JE.EN[k]) for k in range(3))
    npr = sum(xiv[k] * JE.grad("N")[k] for k in range(3))
    out = {}
    for name, gen in (("P_A", JE.poynting(xiv)), ("G_Lie", JE.lie_gen_vec(xiv))):
        brx = JE.bracket(gen, N * JE.hem()) + JE.bracket(JE.gg_names(XIN), N * coup_exp)
        exact = not JE.coeffs(JE.euler(brx - npr * JE.hem(), "N"))
        rs = sp.solve(JE.coeffs(JE.euler(brx - npr * JE.hem() - rr * g2 * N * xE * JE.divE(), "N")), rr, dict=True)
        out[name] = (exact, rs)
    check("X25 continuum: where Gauss enters {G,C}", out["P_A"][0] is False and out["P_A"][1] == [{rr: 1}] and out["G_Lie"][0] is True and out["G_Lie"][1] == [{rr: 0}],
          "with the metric stress: {P_A[xi], C(N)} = H_EM(xi.grad N) + Gauss[g^2 N xi.E] (E-dependent multiplier), {G_Lie[xi], C(N)} = H_EM(xi.grad N); "
          "for {C,C} it is the reverse (X21, X22): either way the algebra closes only with Gauss first class")
    th = J("theta")
    ETA = ["eta0", "eta1", "eta2"]
    eta = [J(n_) for n_ in ETA]
    gth = th * JE.divE()
    ok1 = sp.expand(JE.euler(JE.bracket(gth, N * JE.hem()), "theta")) == 0
    ok2b = sp.expand(JE.euler(JE.bracket(gth, N * coup_exp), "theta")) == 0
    ok3 = sp.expand(JE.euler(JE.bracket(gth, JE.poynting(xiv)), "theta")) == 0
    comm = [sum(xiv[j] * J(ETA[i], JE.ev(j)) - eta[j] * J(XIN[i], JE.ev(j)) for j in range(3)) for i in range(3)]
    a_, b_ = sp.symbols("a_ b_")
    fxe = sum(xiv[i] * eta[j] * JE.Fij(i, j) for i in range(3) for j in range(3) if i != j)
    res = JE.bracket(JE.poynting(xiv), JE.poynting(eta)) - a_ * JE.poynting(comm) - b_ * fxe * JE.divE()
    eqs = []
    for n_ in ETA:
        eqs += JE.coeffs(JE.euler(res, n_))
    solP = sp.solve(eqs, [a_, b_], dict=True)
    res3 = JE.bracket(gth, JE.lie_gen_vec(xiv)) - b_ * sum(xiv[k] * J("theta", JE.ev(k)) for k in range(3)) * JE.divE()
    sol3 = sp.solve(JE.coeffs(JE.euler(res3, "theta")), [b_], dict=True)
    check("X26 continuum Gauss algebra", ok1 and ok2b and ok3 and len(solP) == 1 and solP[0][b_] != 0 and abs(solP[0][a_]) == 1 and len(sol3) == 1 and abs(sol3[0][b_]) == 1,
          f"Gauss first class against N H_EM, N h.T_stress and P_A; {{P_A[xi], P_A[eta]}} = a P_A[[xi,eta]] + b Gauss[F_ij xi^i eta^j] with {solP} "
          f"(F-dependent structure function); {{Gauss[theta], G_Lie[xi]}} = b' Gauss[xi.grad theta], {sol3} (Gauss an ideal; G_Lie a subalgebra, N1)")
    if FULL:
        part_X_continuum_full(eqs2, QALL, s1, s2, lam, expv, lamv, HV, MONOS, QC, coup, XI0)


def part_X_continuum_full(eqs2, QALL, s1, s2, lam, expv, lamv, HV, MONOS, QC, coup, XI0):
    section("Part X6 (--full): spin 1, structure function and shared lambda")
    J, K, al, cB = JE.J, JE.K, JE.al, JE.cB
    kappa = K / (4 * al)
    N, M = JE.N, JE.M
    r1, r2 = sp.symbols("r1 r2")
    hk = JE.hem(kappa)
    brh = JE.bracket(N * coup, M * hk) + JE.bracket(N * hk, M * coup)
    Hm = [[None] * 3 for _ in range(3)]
    for j in range(3):
        Hm[j][j] = J(JE.HD[j])
    for (i, j) in PAIRS:
        Hm[i][j] = Hm[j][i] = J(JE.HF[(i, j)])
    trh = sum(Hm[j][j] for j in range(3))
    xip = [kappa * sum((r1 * Hm[i][j] + (r2 * trh if i == j else 0)) * XI0[j] for j in range(3)) for i in range(3)]
    eqs3 = JE.coeffs(JE.on_gauss(JE.euler(brh - JE.poynting(xip), "N")))
    zero = {v: 0 for v in QALL + [r1, r2]}
    check("X27 (--full) {C,C} alone does not fix the Maxwell coupling", all(sp.simplify(e.subs(zero)) == 0 for e in eqs3), "T = 0, xi' = 0 solves the h E F order")
    eqs2k = [sp.expand(e.subs(cB, kappa)) for e in eqs2]
    sol4 = sp.solve([e.subs(s2, 0) for e in eqs2k] + eqs3, QALL + [s1, r1, r2], dict=True)
    expk = {k: sp.expand(v.subs(cB, kappa)) for k, v in expv.items()}
    ok4 = len(sol4) == 1 and all(sp.simplify(sp.sympify(sol4[0].get(k, k)) - expk[k]) == 0 for k in QALL) and sol4[0].get(r1) == -1 and sol4[0].get(r2) == 0 and sol4[0].get(s1) == 1
    check("X28 (--full) scalar-lapse rule: unique coupling, structure function g^ij = delta - h", ok4, "")
    sol5 = sp.solve([e.subs(s2, -2 * lam) for e in eqs2k] + eqs3, QALL + [s1, r1, r2], dict=True)
    r2l = sp.simplify(sol5[0].get(r2, r2)) if len(sol5) == 1 else None
    check("X29 (--full) trace weight shifts the structure function: r2 = -s2", len(sol5) == 1 and r2l == 2 * lam and sol5[0].get(r1) == -1, f"r2 = {r2l} at s2 = -2 lam (stress = metric stress + lam delta H)")
    # combined scalar + Maxwell, scalar coupling ansatz (upstream nine-coefficient form)
    A = sp.symbols("A1:8")
    B = sp.symbols("B1:3")
    gp = JE.grad("phi")
    lp = sum(JE.d2("phi", k, k) for k in range(3))
    phi, pi = J("phi"), J("pi")
    scoup = 0
    for j in range(3):
        scoup += J(JE.HD[j]) * (A[0] * pi ** 2 + A[1] * sum(g_ ** 2 for g_ in gp) + A[2] * gp[j] ** 2 + A[3] * phi ** 2 + A[4] * phi * pi + A[5] * phi * JE.d2("phi", j, j) + A[6] * phi * lp)
    for (i, j) in PAIRS:
        scoup += J(JE.HF[(i, j)]) * (B[0] * gp[i] * gp[j] + B[1] * phi * JE.d2("phi", i, j))
    c = JE.c
    CN = N * (JE.kin() - K * JE.r1() + JE.hm() + JE.hem())
    CM = M * (JE.kin() - K * JE.r1() + JE.hm() + JE.hem())
    xi = [kappa * x for x in XI0]
    solc = sp.solve(JE.coeffs(JE.euler(JE.bracket(CN, CM) - JE.gg_vec(xi) - JE.poynting(xi) - JE.gm_vec(xi), "N")), [c, cB], dict=True)
    XIN = ["xi0", "xi1", "xi2"]
    xiv = [J(n_) for n_ in XIN]
    nprime = s1 * sum(xiv[k] * JE.grad("N")[k] for k in range(3)) + s2 * N * sum(J(XIN[k], JE.ev(k)) for k in range(3))
    brs = JE.bracket(JE.gm_vec(xiv), N * JE.hm()) + JE.bracket(JE.gg_names(XIN), N * scoup)
    eqs_s2 = [sp.expand(e.subs(c, kappa)) for e in JE.coeffs(JE.euler(brs - nprime * JE.hm(), "N"))]
    hmk = JE.hm(kappa)
    brh_s = JE.bracket(N * scoup, M * hmk) + JE.bracket(N * hmk, M * scoup)
    eqs_s3 = JE.coeffs(JE.euler(brh_s - JE.gm_vec(xip), "N"))
    unk = list(A) + list(B) + QALL + [s1, s2, r1, r2]
    solall = sp.solve(eqs_s2 + eqs_s3 + eqs2k + eqs3, unk, dict=True)
    ok6 = len(solc) == 1 and solc[0] == {c: kappa, cB: kappa} and len(solall) == 1
    if ok6:
        free = sorted(set(unk) - set(solall[0]), key=str)
        ok6 = len(free) == 1 and sp.simplify(sp.sympify(solall[0].get(r1, r1)) + 1) == 0
        if ok6:
            sub = {free[0]: sp.solve(sp.Eq(sp.sympify(solall[0].get(s2, s2)), -2 * lam), free[0])[0]}
            fullv = {k: sp.simplify(sp.sympify(solall[0].get(k, k)).subs(sub)) for k in unk}
            ok6 = all(sp.simplify(fullv[k] - expk[k] - lamv[k].subs(cB, kappa)) == 0 for k in QALL) and sp.simplify(fullv[A[0]] - (-sp.Rational(1, 4) + lam / 2)) == 0 and sp.simplify(fullv[r2] - 2 * lam) == 0
    check("X30 (--full) scalar + Maxwell: common cone and ONE shared lambda", ok6,
          f"O(eps) {{C,C}} closes iff (c, cB) = (kappa, kappa) {solc}; with shared N' and shared structure function the coupled solution space is "
          "one parameter: both metric stresses plus the same lam tr h H")
    stress_check_functions()


def stress_check_functions():
    """--full: B16_check chk4 port. Independent Function-based Euler operators; mod Gauss via E = curl W."""
    section("Part X7 (--full): independent stress check (sympy Functions, E = curl W)")
    X = sp.symbols("x0 x1 x2")
    g2, cB = sp.symbols("g2 cB", positive=True)
    A = [sp.Function(f"A{i}")(*X) for i in range(3)]
    Ef = [sp.Function(f"E{i}")(*X) for i in range(3)]
    W = [sp.Function(f"W{i}")(*X) for i in range(3)]
    N = sp.Function("N")(*X)
    XI = [sp.Function(f"xi{i}")(*X) for i in range(3)]
    SYMP = [(i, j) for i in range(3) for j in range(i, 3)]
    H = {ij: sp.Function(f"h{ij[0]}{ij[1]}")(*X) for ij in SYMP}
    PP = {ij: sp.Function(f"P{ij[0]}{ij[1]}")(*X) for ij in SYMP}
    d = lambda f, i: sp.diff(f, X[i])
    Fij = lambda i, j: d(A[j], i) - d(A[i], j)

    def euler(f, u):
        f = sp.expand(f)
        out = 0
        ders = set(a for a in f.atoms(sp.Derivative) if a.expr == u)
        for jet in [u] + sorted(ders, key=sp.default_sort_key):
            df = sp.diff(f, jet)
            if df == 0:
                continue
            if jet == u:
                out += df
            else:
                t = df
                for v in jet.variables:
                    t = -sp.diff(t, v)
                out += t
        return sp.expand(out)
    CANON = [(A[i], Ef[i]) for i in range(3)] + [(H[ij], PP[ij]) for ij in SYMP]

    def bracket(f, g):
        out = 0
        for q, p in CANON:
            fq, fp = euler(f, q), euler(f, p)
            if fq == 0 and fp == 0:
                continue
            out += fq * euler(g, p) - fp * euler(g, q)
        return sp.expand(out)

    def hem(Ne):
        return Ne * (g2 / 2 * sum(e ** 2 for e in Ef) + cB / (2 * g2) * sum(Fij(i, j) ** 2 for (i, j) in PAIRS))

    def coeff_eqs(expr):
        expr = sp.expand(expr)
        if expr == 0:
            return []
        atoms = sorted(expr.atoms(sp.Derivative), key=sp.default_sort_key) + sorted(expr.atoms(sp.core.function.AppliedUndef), key=sp.default_sort_key)
        rep = {a: sp.Symbol(f"j{n}") for n, a in enumerate(atoms)}
        e = expr.xreplace({a: rep[a] for a in atoms if isinstance(a, sp.Derivative)})
        e = e.xreplace({a: rep[a] for a in atoms if not isinstance(a, sp.Derivative)})
        syms = [s for s in rep.values() if e.has(s)]
        return [cf for cf in sp.Poly(e, *syms).coeffs() if cf != 0]
    vars6 = Ef + [Fij(*ij) for ij in PAIRS]
    quad = [(a, b) for a in range(6) for b in range(a, 6)]
    unk, Q = [], {}
    for ij in SYMP:
        Q[ij] = 0
        for (a, b) in quad:
            s = sp.Symbol(f"q{ij[0]}{ij[1]}_{a}{b}")
            unk.append(s)
            Q[ij] += s * vars6[a] * vars6[b]
    s1, s2 = sp.symbols("s1 s2")
    unknowns = unk + [s1, s2]
    coupling = N * sum(H[ij] * Q[ij] for ij in SYMP)
    PA = sum(XI[i] * Ef[j] * Fij(i, j) for i in range(3) for j in range(3) if i != j)
    GLie = sum(Ef[j] * sum(XI[i] * d(A[j], i) + A[i] * d(XI[i], j) for i in range(3)) for j in range(3))
    Gg = sum(PP[(i, j)] * (d(XI[j], i) + d(XI[i], j)) for (i, j) in SYMP)
    rhs = hem(s1 * sum(XI[i] * d(N, i) for i in range(3)) + s2 * N * sum(d(XI[i], i) for i in range(3)))
    results = {}
    for gname, Gm in (("P_A", PA), ("G_Lie", GLie)):
        lhs0 = sp.expand(bracket(Gm + Gg, hem(N) + coupling).subs({H[ij]: 0 for ij in SYMP}).doit())
        dens = sp.expand(lhs0 - rhs)
        for gauss in (True, False):
            dd, fields = dens, A + Ef + [N] + XI
            if gauss:
                cw = [sum(sp.LeviCivita(i, j, k) * d(W[k], j) for j in range(3) for k in range(3)) for i in range(3)]
                dd = sp.expand(dens.subs({Ef[i]: cw[i] for i in range(3)}).doit())
                fields = A + W + [N] + XI
            eqs = []
            for u in fields:
                eqs += coeff_eqs(euler(dd, u))
            results[(gname, gauss)] = sp.solve(eqs, unknowns, dict=True)
    hm = sp.Matrix(3, 3, lambda i, j: H[(min(i, j), max(i, j))])
    ep = sp.Symbol("epsl")
    gm_, gi = sp.eye(3) + ep * hm, sp.eye(3) - ep * hm
    Fm = sp.Matrix(3, 3, lambda i, j: Fij(i, j) if i != j else 0)
    Ev = sp.Matrix(Ef)
    dg = g2 / 2 * (Ev.T * gm_ * Ev)[0] * (1 - ep * hm.trace() / 2) + cB / (4 * g2) * (1 + ep * hm.trace() / 2) * sum(gi[i, k] * gi[j, l] * Fm[i, j] * Fm[k, l] for i in range(3) for j in range(3) for k in range(3) for l in range(3))
    stress = sp.expand(sp.diff(sp.expand(dg), ep).subs(ep, 0))
    lam = sp.Symbol("lam")
    expected = sp.expand(stress + lam * sum(H[(i, i)] for i in range(3)) * (g2 / 2 * sum(e ** 2 for e in Ef) + cB / (2 * g2) * sum(Fij(i, j) ** 2 for (i, j) in PAIRS)))

    def matches(sol):
        if len(sol) != 1 or len([s for s in unknowns if s not in sol[0]]) != 1:
            return False
        cpl = sp.expand(sum(H[ij] * Q[ij] for ij in SYMP).xreplace(sol[0]))
        sl = sp.solve(coeff_eqs(sp.expand(cpl - expected)), [lam], dict=True)
        return len(sl) == 1 and sp.simplify(sol[0].get(s1, s1) - 1) == 0 and sp.simplify(sol[0].get(s2, s2) + 2 * sl[0][lam]) == 0
    check("X31 (--full) independent path for X24: mod Gauss via E = curl W", matches(results[("P_A", True)]),
          "sympy-Function Euler operators, total-divergence test in A, W, N, xi: one-parameter metric stress + lam tr h H_EM, s1 = 1, s2 = -2 lam")
    check("X32 (--full) without Gauss P_A has no solution; G_Lie closes with the same family", len(results[("P_A", False)]) == 0 and matches(results[("G_Lie", False)]) and len(results[("G_Lie", True)]) == 1, "")


# =====================================================================================================
# Part Y: anisotropic cones
# =====================================================================================================
def part_Y():
    section("Part Y: anisotropic cones are rejected (exact)")
    X = XS
    N, M = sp.Function("N")(*X), sp.Function("M")(*X)
    f1, f2 = sp.Function("f1")(*X), sp.Function("f2")(*X)
    psi = sp.Matrix([f1, f2])
    Dd = lambda u, j: sp.diff(u, X[j])

    def h(Lp, E, ps, B=None):
        out = sp.zeros(2, 1)
        for a in range(3):
            for j in range(3):
                if E[a, j] == 0:
                    continue
                out += E[a, j] * sp.Rational(1, 2) * (Lp * (SIGS[a] * (-I) * ps.applyfunc(lambda u: Dd(u, j))) + SIGS[a] * (-I) * (Lp * ps).applyfunc(lambda u: Dd(u, j)))
        if B is not None:
            for j in range(3):
                out += Dd(Lp, j) * (B[j] * ps)
        return out

    def comm(E, B=None):
        return (h(N, E, h(M, E, psi, B), B) - h(M, E, h(N, E, psi, B), B)).applyfunc(sp.expand)
    w = [N * Dd(M, j) - M * Dd(N, j) for j in range(3)]

    def kosmann_E(E, ps):
        g = E.T * E
        xi = [sum(g[k, j] * w[j] for j in range(3)) for k in range(3)]
        div = sum(Dd(xi[k], k) for k in range(3))
        Ew = [sum(E[c, l] * w[l] for l in range(3)) for c in range(3)]
        Ed = lambda u, b: sum(E[b, j] * Dd(u, j) for j in range(3))
        spin = sp.zeros(2, 2)
        for a, b, c in itertools.permutations(range(3)):
            spin += sp.LeviCivita(a, b, c) * Ed(Ew[c], b) * SIGS[a]
        out = sum((xi[k] * ps.applyfunc(lambda u: Dd(u, k)) for k in range(3)), sp.zeros(2, 1))
        return out + sp.Rational(1, 2) * div * ps + I / 4 * spin * ps

    def dsymbol(Cm):
        return [sp.Matrix(2, 2, lambda r, c_: sp.expand(Cm[r]).coeff(Dd([f1, f2][c_], k))) for k in range(3)]
    va, vt = sp.symbols("v_a v_t", positive=True)
    Es = {"uniaxial": sp.diag(vt, vt, va),
          "generic triad": sp.Matrix([[sp.Rational(3, 2), sp.Rational(1, 3), 0], [-sp.Rational(1, 2), 1, sp.Rational(2, 5)], [sp.Rational(1, 4), -sp.Rational(1, 3), sp.Rational(5, 4)]]),
          "reflected triad": sp.Matrix([[1, sp.Rational(1, 2), 0], [0, -1, sp.Rational(1, 3)], [sp.Rational(1, 5), 0, 2]])}
    ok_full = ok_der = True
    for nm, E in Es.items():
        Cm = comm(E)
        ok_full &= (Cm + kosmann_E(E, psi)).applyfunc(sp.simplify) == sp.zeros(2, 1)
        g = E.T * E
        Dk = dsymbol(Cm)
        ok_der &= all(sp.simplify(Dk[k] + sum(g[k, j] * w[j] for j in range(3)) * sp.eye(2)) == sp.zeros(2, 2) for k in range(3))
    check("Y1 anisotropic Weyl bracket (constant triad E)", ok_full and ok_der,
          "h_N = (1/2) sum E_aj {N, sigma^a (-i d_j)} for a uniaxial, a generic and a reflected (det < 0) triad: [h_N, h_M] = -(xi.grad + (1/2) div xi + "
          "frame-E spin term), xi = g w, g = E^T E, exactly; its derivative part is the scalar -g^kj w_j d_k")
    Cu = comm(sp.diag(vt, vt, va))
    coef = [sp.simplify(sp.expand(Cu[0]).coeff(sp.diff(f1, X[j]))) for j in range(3)]
    kap = sp.Symbol("kappa", positive=True)
    sol = sp.solve([sp.expand(coef[j] + kap * w[j]).coeff(sp.diff(M, X[j]) * N) for j in range(3)], [kap, va], dict=True)
    check("Y2 uniaxial component extraction (path 2)", all(sp.simplify(coef[j] + [vt, vt, va][j] ** 2 * w[j]) == 0 for j in range(3)) and sol == [{kap: vt ** 2, va: vt}],
          f"coefficient of d_j f1 in component 1 = -v_j^2 w_j (direction-weighted shift); matching -kappa w_j for all lapses gives {sol}")
    gsym = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"g{min(i, j)}{max(i, j)}"))
    # derivative part -g^kj w_j d_k must equal -kappa w^k d_k for all lapses: extract the coefficients of d_j M from the lapse expression
    exprs = [sp.expand(sum((gsym[k, j] - (kap if j == k else 0)) * w[j] for j in range(3))) for k in range(3)]
    eqs = [e.coeff(sp.Derivative(M, X[j])).subs(N, 1) for e in exprs for j in range(3)]
    solg = sp.solve(eqs, list(gsym.free_symbols), dict=True)
    check("Y3 closure against the isotropic structure function forces g = kappa I", len(solg) == 1 and all(sp.simplify(gsym.subs(solg[0])[i, j] - (kap if i == j else 0)) == 0 for i in range(3) for j in range(3)),
          "coefficients of d_j M in sum_j (g^kj - kappa delta^kj) w_j, w = N grad M - M grad N (w takes any value at a point): "
          f"-g^kj w_j d_k = -kappa w^k d_k for all lapses iff g = kappa I (any symmetric cone metric); solve -> {solg}")
    E = sp.diag(vt, vt, va)
    zeroth = sp.Matrix(2, 2, lambda r, c_: sp.expand(Cu[r].subs({sp.Derivative(f1, X[k]): 0 for k in range(3)}).subs({sp.Derivative(f2, X[k]): 0 for k in range(3)})).coeff([f1, f2][c_]))
    curl = [Dd(w[2], 1) - Dd(w[1], 2), Dd(w[0], 2) - Dd(w[2], 0), Dd(w[1], 0) - Dd(w[0], 1)]
    divx = sum(Dd(sum((E.T * E)[k, j] * w[j] for j in range(3)), k) for k in range(3))
    spin_pred = I / 4 * (vt * va * curl[0] * SIGS[0] + vt * va * curl[1] * SIGS[1] + vt ** 2 * curl[2] * SIGS[2])
    check("Y4 the spin part independently forces v_a = v_t", (zeroth + sp.Rational(1, 2) * divx * sp.eye(2) + spin_pred).applyfunc(sp.simplify) == sp.zeros(2, 2),
          "uniaxial spin part (i/4)(vt va curl_x w sigma_x + vt va curl_y w sigma_y + vt^2 curl_z w sigma_z): equal to kappa (i/4) curl w . sigma "
          "only if vt^2 = vt va = kappa")
    bm = [sp.Matrix([[sp.Symbol(f"p{j}"), sp.Symbol(f"r{j}") + I * sp.Symbol(f"i{j}")], [sp.Symbol(f"r{j}") - I * sp.Symbol(f"i{j}"), sp.Symbol(f"q{j}")]]) for j in range(3)]
    Ci = comm(E, B=bm)
    Dk = dsymbol(Ci)
    g = E.T * E
    tr_ok = all(sp.simplify(Dk[k].trace() / 2 + sum(g[k, j] * w[j] for j in range(3))) == 0 for k in range(3))
    check("Y5 density improvements cannot rescue an anisotropic cone", tr_ok,
          "h_N + d_j N psi^dag B^j psi with general Hermitian B^j: the spin trace of the derivative part is still -g^kj w_j d_k (the extra "
          "derivative term is traceless)")
    res = []
    for sv in product((1, -1), repeat=3):
        Ed = sp.diag(*sv)
        Cm = comm(Ed)
        z0 = sp.Matrix(2, 2, lambda r, c_: sp.expand(Cm[r].subs({sp.Derivative(f1, X[k]): 0 for k in range(3)}).subs({sp.Derivative(f2, X[k]): 0 for k in range(3)})).coeff([f1, f2][c_]))
        divw = sum(Dd(w[k], k) for k in range(3))
        tau = [sv[a] * SIGS[a] for a in range(3)]
        det = sv[0] * sv[1] * sv[2]
        own = (z0 + sp.Rational(1, 2) * divw * sp.eye(2) + det * I / 4 * sum((curl[a] * tau[a] for a in range(3)), sp.zeros(2, 2))).applyfunc(sp.simplify) == sp.zeros(2, 2)
        onsite = (z0 + sp.Rational(1, 2) * divw * sp.eye(2) + I / 4 * sum((curl[a] * SIGS[a] for a in range(3)), sp.zeros(2, 2))).applyfunc(sp.simplify) == sp.zeros(2, 2)
        der = all(sp.simplify(dsymbol(Cm)[k] + w[k] * sp.eye(2)) == sp.zeros(2, 2) for k in range(3))
        res.append((sv, der, own, onsite))
    check("Y6 naive species: one isotropic cone, own spin sets (continuum path for W9/W10)",
          all(r[1] and r[2] for r in res) and sorted(r[0] for r in res if r[3]) == [(-1, -1, -1), (1, 1, 1)],
          "E = diag(s), s in {+-1}^3: all eight species have derivative part -w.grad (one isotropic cone); spin part det(s)(i/4)(curl w).tau, "
          "tau_a = s_a sigma_a; the on-site Kosmann term holds only at k = 0 and (pi,pi,pi)")
    # runner-added: lattice anisotropic scalar
    lat = cm.Lattice(3, F(3, 7), F(5, 11), F(2, 3))
    rng = random.Random(171)
    n, m = ({x: F(rng.randint(-3, 3)) for x in lat.SITES} for _ in range(2))
    kappa = lat.KK / (4 * lat.ALPHA)

    def h_aniso(nn, cs):
        out = {}
        for x in lat.SITES:
            out = padd(out, term(nn[x] / 2, lat.var(("pi", x)), lat.var(("pi", x))))
            out = padd(out, term(nn[x] * lat.MU / 2, lat.var(("phi", x)), lat.var(("phi", x))))
            for j in range(3):
                d = cm.dfield(lat, "phi", x, j)
                out = padd(out, pscale(pmul(d, d), (nn[x] + nn[lat.sh(x, j)]) / 2 * cs[j] / 2))
        return out
    xt = cm.xi_tilde(lat, n, m)
    cs0 = (F(7, 5), F(7, 5), F(2, 9))
    okb = not padd(pbracket(lat, h_aniso(n, cs0), h_aniso(m, cs0)), cm.g_matter(lat, {(x, j): -cs0[j] * v for (x, j), v in xt.items()}), F(-1))
    tcols = [padd(cm.g_grav(lat, cm.unit_bond(lat, x, j)), cm.g_matter(lat, cm.unit_bond(lat, x, j))) for x in lat.SITES for j in range(3)]
    gb = pbracket(lat, padd(cm.kin(lat, n), pscale(cm.r1(lat, n), -lat.KK)), padd(cm.kin(lat, m), pscale(cm.r1(lat, m), -lat.KK)))
    tab = {}
    for cs in ((kappa, kappa, kappa), (kappa, kappa, 2 * kappa), (2 * kappa, kappa, kappa), (kappa / 2, kappa / 2, kappa / 2)):
        tab[tuple(str(c / kappa) for c in cs)] = in_span(padd(gb, pbracket(lat, h_aniso(n, cs), h_aniso(m, cs))), tcols)
    check("Y7 lattice anisotropic scalar (runner-added, L=3)", okb and tab == {("1", "1", "1"): True, ("1", "1", "2"): False, ("2", "1", "1"): False, ("1/2", "1/2", "1/2"): False},
          f"per-axis gradient coefficients c_j: {{H(N), H(M)}} = G_m[-c_j xi~] bond by bond, exactly; with gravity (s = -1) one total relabelling "
          f"iff c_0 = c_1 = c_2 = K/(4alpha); {{c_j/kappa: closes}} = {tab}")
    # runner-added: anisotropic relabelling loophole
    Am = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"a{i}{j}"))
    nu = sp.Symbol("nu")
    xs = sp.symbols("x0:3")
    cfx, cfe = sp.symbols("p0:30"), sp.symbols("q0:30")
    monos = [1] + list(xs) + [xs[i] * xs[j] for i in range(3) for j in range(i, 3)]
    xi = [sum(cfx[10 * i + k] * monos[k] for k in range(10)) for i in range(3)]
    et = [sum(cfe[10 * i + k] * monos[k] for k in range(10)) for i in range(3)]
    lieb = lambda U, V: [sum(U[k] * sp.diff(V[i], xs[k]) - V[k] * sp.diff(U[i], xs[k]) for k in range(3)) for i in range(3)]
    Ax, Ae = list(Am * sp.Matrix(xi)), list(Am * sp.Matrix(et))
    red_ = [sum(Ax[k] * sp.diff(et[i], xs[k]) - Ae[k] * sp.diff(xi[i], xs[k]) for k in range(3)) for i in range(3)]
    ident = all(sp.expand(l_ - r_) == 0 for l_, r_ in zip(lieb(Ax, Ae), list(Am * sp.Matrix(red_))))
    allv = list(xs) + list(cfx) + list(cfe)
    eqs = []
    for i, e_ in enumerate(lieb(xi, et)):
        eqs += sp.Poly(sp.expand(red_[i] - nu * e_), *allv).coeffs()
    sol = sp.solve(eqs, list(Am) + [nu], dict=True)
    okA = ident and len(sol) == 1 and sp.simplify(Am.subs(sol[0]) - nu * sp.eye(3)) == sp.zeros(3, 3)
    check("Y8 an anisotropic matter relabelling breaks {G,G} (runner-added)", okA,
          f"a matter generator moving fields along A xi (constant invertible A) closes with gravity's [xi, eta] only if [A xi, A eta] = nu A [xi, eta]; "
          f"since [A xi, A eta] = A((A xi).grad eta - (A eta).grad xi) exactly ({ident}), this is linear in A: solution {sol} (quadratic "
          "polynomial fields), A = nu I, and gravity fixes nu = 1")
    # runner-added: cubic-invariant symmetric tensors are isotropic
    S = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"t{min(i, j)}{max(i, j)}"))
    Rz = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    Rx = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    eqsS = list(Rz * S * Rz.T - S) + list(Rx * S * Rx.T - S)
    solS = sp.solve(eqsS, list(S.free_symbols), dict=True)
    Ss = S.subs(solS[0])
    check("Y9 an O-symmetric gravity sector has an isotropic structure function", Ss.is_diagonal() and Ss[0, 0] == Ss[1, 1] == Ss[2, 2],
          f"symmetric 2-tensors invariant under the 90-degree rotations about z and x: {Ss.tolist()} (one free parameter)")


# =====================================================================================================
# --diag: floating-point smooth-field diagnostics (not gating), after B16_check chk3b / chk3c
# =====================================================================================================
def diag():
    import numpy as np
    import scipy.sparse as spm
    print("\n--diag: floating-point smooth-field diagnostics (NOT gating; one configuration each)")
    TP = 2 * np.pi

    def fmat(lat):
        r, c, v = [], [], []
        for p, d in enumerate(lat.Fp):
            for a, s in d.items():
                r.append(p)
                c.append(a)
                v.append(s)
        return spm.csr_matrix((v, (r, c)), shape=(len(lat.plaqs), len(lat.links)))

    def sparse_gen(lat, X):
        rows, cols, vals = [], [], []
        for b, d in X.items():
            if b[1] != 0:
                continue
            for (k, a), v in d.items():
                rows.append(k)
                cols.append(a)
                vals.append(float(v))
        nL = len(lat.links)
        return spm.csr_matrix((vals, (rows, cols)), shape=(nL, nL))

    def smear(lat, u, w, Nv):
        nl = np.array([sum(float(v) * Nv[lat.sidx[s]] for s, v in u[k].items()) for k in range(len(lat.links))])
        mp = np.array([sum(float(v) * Nv[lat.sidx[s]] for s, v in w[p].items()) for p in range(len(lat.plaqs))])
        return nl, mp

    def dlapse(lat, Nv, kind):
        out = np.zeros_like(Nv)
        for x in lat.sites:
            i = lat.sidx[x]
            f, bk = Nv[lat.sidx[lat.sh(x, 0)]], Nv[lat.sidx[lat.sh(x, 0, -1)]]
            out[i] = {"backward": Nv[i] - bk, "forward": f - Nv[i], "central": (f - bk) / 2}[kind]
        return out
    env = lambda r: 1 + 0.6 * np.sin(TP * r[0])

    def em_run(name, L):
        g2, cb = 0.9, 1.7
        lat = ILat(L)
        if name == "FWD":
            u, w = fwd_timing(lat)
            X = fwd_GA(lat)
        else:
            u, w = staggered(lat, 0)
            X = induced_generator(lat, u, w, F(1))
        G = sparse_gen(lat, X)
        a = 1.0 / L
        Ac = lambda j, r: env(r) * [np.sin(TP * r[1]) + 0.5 * np.cos(TP * r[2] + 0.3), np.cos(TP * (r[0] + 0.2)) * np.sin(TP * r[2]), 0.7 * np.sin(TP * (r[0] - r[1]))][j]
        Wc = lambda q, r: env(r) * [np.cos(TP * (r[0] + r[2])) + 0.4 * np.sin(TP * r[1]), 0.8 * np.sin(TP * (r[1] - 0.1)) * np.cos(TP * r[0]), np.cos(TP * r[2] + 0.7)][q]
        A = np.zeros(len(lat.links))
        for k, (x, j) in enumerate(lat.links):
            r = np.array(x, float)
            r[j] += 0.5
            A[k] = a * Ac(j, r * a)
        b = np.zeros(len(lat.plaqs))
        for p, (y, (i, j)) in enumerate(lat.plaqs):
            r = np.array(y, float)
            r[i] += 0.5
            r[j] += 0.5
            b[p] = a * Wc(PAIRS.index((i, j)), r * a)
        Fm = fmat(lat)
        E = Fm.T @ b
        Fv = Fm @ A

        def br(Nv):
            nl, mp = smear(lat, u, w, Nv)
            return (G.T @ E) @ (g2 * nl * E) - (G @ A) @ ((cb / g2) * (Fm.T @ (mp * Fv)))

        def H(Nv):
            nl, mp = smear(lat, u, w, Nv)
            return (g2 / 2) * np.sum(nl * E * E) + (cb / (2 * g2)) * np.sum(mp * Fv * Fv)
        Nv = np.array([np.exp(0.5 * np.cos(TP * x[0] * a)) for x in lat.sites])
        B = br(Nv)
        lead = H(dlapse(lat, Nv, "central"))
        R = min(abs(B - H(dlapse(lat, Nv, k))) for k in ("backward", "forward", "central"))
        return br(np.ones(len(lat.sites))), lead, B, R
    Ls = [8, 12, 16, 24]
    rows = {nm: [(L,) + em_run(nm, L) for L in Ls] for nm in ("FWD", "STAG")}
    for nm, rr in rows.items():
        for (L, D, lead, B, R) in rr:
            print(f"  {nm:5s} L={L:3d}  Lead={lead: .4e}  B/Lead={B / lead: .5f}  D/Lead={D / lead: .3e}  R/Lead={R / lead: .3e}", flush=True)
    sl = np.polyfit(np.log(Ls), np.log([abs(r[1] / r[2]) for r in rows["FWD"]]), 1)[0]
    print(f"  FWD: log-log slope of D/Lead = {sl:.2f} (campaign check, L = 8..40: -1.03; O(a))")
    print(f"  STAG: max |D| = {max(abs(r[1]) for r in rows['STAG']):.1e}; B/Lead does not approach 1 (campaign check to L = 56: 1.000 -> 1.072), "
          "consistent with an O(1) defect of the staggered generator")


if __name__ == "__main__":
    print(f"flags: full={FULL} diag={DIAG}")
    w0_grassmann()
    part_W_continuum()
    part_W_cone()
    part_W_lattice_symbols()
    part_W_lattice_position()
    part_W_1d()
    if FULL:
        part_W_taylor3d()
    part_N()
    il = part_X_timing()
    stag = part_X_local_rule(il)
    part_X_bracket_cone(il, stag)
    part_X_gauss_compact_obstruction()
    part_X_continuum()
    part_Y()
    if DIAG:
        diag()
    print(f"\nelapsed {time.time() - T0:.0f}s")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    sys.exit(0 if FAIL == 0 else 1)
