#!/usr/bin/env python3
"""Bounded supplied-model controls. The canonical claim card and complete corrected argument define the current claim boundary. Finite obstruction certificates do not promote deferred terminal exclusions. Optional branches count only when executed.

Historical technical inventory (read with those corrected scope qualifications):
Curvature-member constraint closure with a supplied site scalar: one common matter cone, the
Lorentzian curvature sign, and an O(a^2) lattice obstruction in {G, C}.

Companion runner of
docs/CURVATURE_MEMBER_CLOSURE_WITH_MATTER_FORCES_ONE_COMMON_CONE_AND_THE_LORENTZIAN_SIGN_AND_HAS_AN_ORDER_A_SQUARED_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-10-18.md

Self-contained (Python 3 + sympy). Adapted from the scale-ladder campaign block B14 scripts
(b14_lattice_closure.py, b14_continuum_leading_order.py) and its check scripts (chk_e2_cone.py,
chk_e5_obstruction.py). Every gating test is exact (Fraction / sympy QQ / symbolic).

Supplied models (nothing is adopted; no physical identification):
  gravity  : the 2026-09-24 curvature-member clauses (block-62 staggered placement: h_jj, P_jj on sites,
             h_ij, P_ij on faces, relabellings xi on bonds; R1; kinetic Legendre form at beta = -alpha;
             four-corner face timing), with a sign parameter s in C = kin + s K R1.
  matter   : H_m(N) = sum_x N_x (pi_x^2/2 + mu phi_x^2/2) + sum_b Nbar_b (c/2)(Delta_b phi)^2,
             Nbar_b = endpoint mean;  G_m[xi] = sum_b xi_b (Delta_b phi)(pi_x + pi_{x+e})/2.
  bracket  : {q, p} = 1 for (h, P) and (phi, pi).

Parts
  A  lattice order eps of {C(N), C(M)}: matter bracket, timing, total closure iff c = -sK/(4 alpha),
     two species iff c1 = c2; second implementation (matrix path, other constants) of the closure table.
  B  the sign: block 101's action has the linearised-GR sign, its Legendre transform carries -K R1.
  C  order phi^2 of {G[xi], C(N)}: exact rank certificates that no coupling in three ansatze closes the
     pi-pi sector into H_m(N'); positive control with the O(a^2) monomial removed.
  D  continuum leading order (sympy jet calculus): c = K/(4 alpha); metric-variational stress coupling.
Optional (not gating): `--e6 [L ...]` prints the floating-point long-wavelength diagnostic of the campaign
(default L = 6 8 12; one configuration). `--quick` skips the L = 4 repeats.
"""
from __future__ import annotations

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


import math
import random
import sys
import time
from fractions import Fraction as F
from itertools import combinations_with_replacement, product

import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix

PASS = FAIL = 0
T0 = time.time()


def check(name, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok)
    PASS += ok
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""), flush=True)


PAIRS = ((0, 1), (0, 2), (1, 2))


# =====================================================================================================
# Part A engine: sparse polynomials over Q with an exact Poisson bracket on an L^3 torus
# =====================================================================================================
class Lattice:
    def __init__(self, L, alpha, K, mu):
        self.L, self.ALPHA, self.KK, self.MU = L, alpha, K, mu
        self.SITES = list(product(range(L), repeat=3))
        self.VAR, self.CONJ, self.KIND = {}, {}, {}
        for x in self.SITES:
            for j in range(3):
                self.CONJ[self.var(("hd", x, j))] = self.var(("Pd", x, j))
            for ij in PAIRS:
                self.CONJ[self.var(("hf", x, ij))] = self.var(("Pf", x, ij))
            self.CONJ[self.var(("phi", x))] = self.var(("pi", x))
            self.CONJ[self.var(("chi", x))] = self.var(("pchi", x))
        self.Q_OF_P = {p: q for q, p in self.CONJ.items()}

    def var(self, name):
        if name not in self.VAR:
            self.VAR[name] = len(self.VAR)
            self.KIND[self.VAR[name]] = name[0]
        return self.VAR[name]

    def sh(self, x, j, s=1):
        return tuple((x[k] + (s if k == j else 0)) % self.L for k in range(3))


def padd(a, b, s=F(1)):
    out = dict(a)
    for m, c in b.items():
        v = out.get(m, 0) + s * c
        if v == 0:
            out.pop(m, None)
        else:
            out[m] = v
    return out


def pscale(a, s):
    return {m: s * c for m, c in a.items()} if s != 0 else {}


def pmul(a, b):
    out = {}
    for m1, c1 in a.items():
        for m2, c2 in b.items():
            m = tuple(sorted(m1 + m2))
            v = out.get(m, 0) + c1 * c2
            if v == 0:
                out.pop(m, None)
            else:
                out[m] = v
    return out


def term(c, *vs):
    return {tuple(sorted(vs)): F(c)} if c != 0 else {}


def deriv(a):
    d = {}
    for m, c in a.items():
        for k, v in enumerate(m):
            if k > 0 and m[k - 1] == v:
                continue
            rest = list(m)
            rest.remove(v)
            dv = d.setdefault(v, {})
            mm = tuple(rest)
            val = dv.get(mm, 0) + m.count(v) * c
            if val == 0:
                dv.pop(mm, None)
            else:
                dv[mm] = val
    return d


def bracket(lat, a, b):
    """{a,b} = sum_q (da/dq db/dp - da/dp db/dq), {q,p} = 1."""
    da, db = deriv(a), deriv(b)
    out = {}
    for v, dav in da.items():
        if v in lat.CONJ and lat.CONJ[v] in db:
            out = padd(out, pmul(dav, db[lat.CONJ[v]]))
        elif v in lat.Q_OF_P and lat.Q_OF_P[v] in db:
            out = padd(out, pmul(dav, db[lat.Q_OF_P[v]]), F(-1))
    return out


class Reducer:
    def __init__(self):
        self.basis = []

    def reduce(self, vec):
        vec = dict(vec)
        for piv, b in self.basis:
            if piv in vec:
                f = vec[piv]
                for r, val in b.items():
                    nv = vec.get(r, 0) - f * val
                    if nv == 0:
                        vec.pop(r, None)
                    else:
                        vec[r] = nv
        return vec

    def add(self, vec):
        vec = self.reduce(vec)
        if not vec:
            return
        piv = min(vec)
        pv = vec[piv]
        vec = {r: v / pv for r, v in vec.items()}
        self.basis = [(p2, padd(b2, vec, -b2[piv]) if piv in b2 else b2) for p2, b2 in self.basis] + [(piv, vec)]


def in_span(target, cols):
    red = Reducer()
    for c in cols:
        red.add(c)
    return not red.reduce(target)


# ---- gravity sector (09-24 clauses) -----------------------------------------------------------------
def kin(lat, n, ck=F(1, 2)):
    out = {}
    for x in lat.SITES:
        tr = {}
        sq = {}
        for j in range(3):
            tr = padd(tr, term(1, lat.var(("Pd", x, j))))
            sq = padd(sq, term(1, lat.var(("Pd", x, j)), lat.var(("Pd", x, j))))
        out = padd(out, pscale(padd(sq, pmul(tr, tr), -ck), n[x] / (4 * lat.ALPHA)))
    for y in lat.SITES:
        for (i, j) in PAIRS:
            c4 = [y, lat.sh(y, i), lat.sh(y, j), lat.sh(lat.sh(y, i), j)]
            pv = lat.var(("Pf", y, (i, j)))
            out = padd(out, term(sum((n[z] for z in c4), F(0)) / 4 / (8 * lat.ALPHA), pv, pv))
    return out


def r1(lat, n):
    """sum_x N_x R1_x, R1 = p^2 tr h - p.h.p (block 62 T3), i.e. d_i d_j h_ij - lap tr h in position space."""
    out = {}
    for x in lat.SITES:
        second = [n[lat.sh(x, i)] - 2 * n[x] + n[lat.sh(x, i, -1)] for i in range(3)]
        for j in range(3):
            out = padd(out, term(-sum(second) + second[j], lat.var(("hd", x, j))))
    for y in lat.SITES:
        for (i, j) in PAIRS:
            mixed = n[y] - n[lat.sh(y, i)] - n[lat.sh(y, j)] + n[lat.sh(lat.sh(y, i), j)]
            out = padd(out, term(2 * mixed, lat.var(("hf", y, (i, j)))))
    return out


def g_grav(lat, xi):
    out = {}
    for x in lat.SITES:
        for j in range(3):
            out = padd(out, term(2 * (xi[(x, j)] - xi[(lat.sh(x, j, -1), j)]), lat.var(("Pd", x, j))))
    for y in lat.SITES:
        for (i, j) in PAIRS:
            out = padd(out, term(xi[(lat.sh(y, i), j)] - xi[(y, j)] + xi[(lat.sh(y, j), i)] - xi[(y, i)],
                                 lat.var(("Pf", y, (i, j)))))
    return out


def xi_tilde(lat, n, m):
    return {(x, j): n[lat.sh(x, j)] * m[x] - n[x] * m[lat.sh(x, j)] for x in lat.SITES for j in range(3)}


# ---- matter sector (supplied) -----------------------------------------------------------------------
def dfield(lat, f, x, j):
    return padd(term(1, lat.var((f, lat.sh(x, j)))), term(-1, lat.var((f, x))))


def h_matter(lat, n, c, f="phi", p="pi", mu=None, bond="mean"):
    mu = lat.MU if mu is None else mu
    out = {}
    for x in lat.SITES:
        out = padd(out, term(n[x] / 2, lat.var((p, x)), lat.var((p, x))))
        out = padd(out, term(n[x] * mu / 2, lat.var((f, x)), lat.var((f, x))))
        for j in range(3):
            w = (n[x] + n[lat.sh(x, j)]) / 2 if bond == "mean" else n[x]
            d = dfield(lat, f, x, j)
            out = padd(out, pscale(pmul(d, d), w * c / 2))
    return out


def g_matter(lat, xi, f="phi", p="pi", side="sym"):
    out = {}
    for x in lat.SITES:
        for j in range(3):
            if xi[(x, j)] == 0:
                continue
            if side == "sym":
                pb = padd(term(F(1, 2), lat.var((p, x))), term(F(1, 2), lat.var((p, lat.sh(x, j)))))
            else:  # one-sided: pi at the far endpoint
                pb = term(1, lat.var((p, lat.sh(x, j))))
            out = padd(out, pscale(pmul(dfield(lat, f, x, j), pb), xi[(x, j)]))
    return out


def unit_bond(lat, x, j):
    return {(z, l): F(1) if (z, l) == (x, j) else F(0) for z in lat.SITES for l in range(3)}


def part_A(L, seed):
    print(f"\n=== Part A: lattice order eps of {{C(N),C(M)}}, L = {L} (exact rationals) ===", flush=True)
    lat = Lattice(L, F(3, 7), F(5, 11), F(2, 3))
    rng = random.Random(seed)
    rf = lambda: {x: F(rng.randint(-3, 3)) for x in lat.SITES}
    KK, AL = lat.KK, lat.ALPHA
    kappa = KK / (4 * AL)

    # A1 gravity alone, both signs (09-24 T1; s = +1 is the 09-24 runner's convention)
    ok = True
    for s in (F(-1), F(1)):
        for _ in range(2):
            n, m = rf(), rf()
            br = bracket(lat, padd(kin(lat, n), pscale(r1(lat, n), s * KK)), padd(kin(lat, m), pscale(r1(lat, m), s * KK)))
            xi = {k: v * s * kappa for k, v in xi_tilde(lat, n, m).items()}
            ok = ok and not padd(br, g_grav(lat, xi), F(-1))
    check(f"A1 (L={L}) gravity alone", ok,
          "{kin(N)+sK R1(N), kin(M)+sK R1(M)} = G_g[(sK/(4alpha)) xi~] exactly for s = -1 and s = +1, xi~_b = N_(x+e)M_x - N_x M_(x+e) "
          "(09-24 T1 closes for either sign; the 09-24 runner's closing field +K/(4alpha) is s = +1)")

    n, m = rf(), rf()
    xt = xi_tilde(lat, n, m)
    c = F(7, 5)
    # A2 matter bracket
    br = bracket(lat, h_matter(lat, n, c), h_matter(lat, m, c))
    check(f"A2 (L={L}) matter bracket", not padd(br, g_matter(lat, {k: -c * v for k, v in xt.items()}), F(-1)),
          "{H_m(N), H_m(M)} = G_m[-c xi~] exactly (mass term cancels; endpoint-mean bond lapse, symmetric G_m)")
    # A3 one-endpoint bond lapse: outside symmetric G_m span, equal to the one-sided relabelling
    br1 = bracket(lat, h_matter(lat, n, c, bond="one"), h_matter(lat, m, c, bond="one"))
    mcols = [g_matter(lat, unit_bond(lat, x, j)) for x in lat.SITES for j in range(3)]
    ok_out = not in_span(br1, mcols)
    ok_one = not padd(br1, g_matter(lat, {k: -c * v for k, v in xt.items()}, side="one"), F(-1))
    check(f"A3 (L={L}) bond timing is paired with G_m", ok_out and ok_one,
          f"one-endpoint lapse N_x on the bond term: bracket NOT in span of symmetric G_m ({ok_out}) but EQUAL to the one-sided "
          f"relabelling sum_b (-c xi~_b)(Delta_b phi) pi_(x+e) ({ok_one}): the timing is fixed only relative to the supplied G_m")
    # A4 total closure table
    tcols = [padd(g_grav(lat, unit_bond(lat, x, j)), g_matter(lat, unit_bond(lat, x, j))) for x in lat.SITES for j in range(3)]
    res = {}
    for s in (F(-1), F(1)):
        for r in (F(1), F(2), F(1, 3), F(-1)):
            cn = padd(padd(kin(lat, n), pscale(r1(lat, n), s * KK)), h_matter(lat, n, r * kappa))
            cm = padd(padd(kin(lat, m), pscale(r1(lat, m), s * KK)), h_matter(lat, m, r * kappa))
            res[(int(s), str(r))] = in_span(bracket(lat, cn, cm), tcols)
    expect = {k: (F(k[1]) == -k[0]) for k in res}
    check(f"A4 (L={L}) total closure iff c = -sK/(4alpha)", res == expect,
          f"table {{(s, c/kappa): closes into one G_g[xi]+G_m[xi]}} = {res}; with c > 0 only s = -1 (C = kin - K R1 + H_m) closes; "
          f"the 09-24 runner's s = +1 closes only with c = -kappa < 0")
    # A5 two species
    bonds = [(x, j) for x in lat.SITES for j in range(3)]
    ccols = [padd(tcols[k], g_matter(lat, unit_bond(lat, *bonds[k]), "chi", "pchi")) for k in range(len(bonds))]
    out = {}
    for r2 in (F(1), F(2), F(1, 3)):
        cn = padd(padd(padd(kin(lat, n), pscale(r1(lat, n), -KK)), h_matter(lat, n, kappa)), h_matter(lat, n, r2 * kappa, "chi", "pchi", mu=F(0)))
        cm = padd(padd(padd(kin(lat, m), pscale(r1(lat, m), -KK)), h_matter(lat, m, kappa)), h_matter(lat, m, r2 * kappa, "chi", "pchi", mu=F(0)))
        out[str(r2)] = in_span(bracket(lat, cn, cm), ccols)
    check(f"A5 (L={L}) one common cone", out == {"1": True, "2": False, "1/3": False},
          f"two scalars, s = -1, c_phi = kappa: closes iff c_chi = kappa = K/(4alpha); {{c_chi/kappa: closes}} = {out}")


# ---- A6: second implementation (matrix path, different constants), after chk_e2_cone.py -------------
def part_A6(L=3):
    ALPHA, K, MU = F(2, 5), F(7, 3), F(5, 2)
    KAP = K / (4 * ALPHA)
    S = list(product(range(L), repeat=3))
    BIDX = {(x, j): 3 * i + j for i, x in enumerate(S) for j in range(3)}
    NB = 3 * len(S)

    def sh(x, j, s=1):
        y = list(x)
        y[j] = (y[j] + s) % L
        return tuple(y)
    HIDX = [("d", x, j) for x in S for j in range(3)] + [("f", y, ij) for y in S for ij in PAIRS]

    def kin_grad(n, P):
        out = {}
        for x in S:
            tr = sum(P.get(("d", x, j), 0) for j in range(3))
            for j in range(3):
                out[("d", x, j)] = n[x] / (2 * ALPHA) * (P.get(("d", x, j), 0) - tr / 2)
        for y in S:
            for (i, j) in PAIRS:
                fm = (n[y] + n[sh(y, i)] + n[sh(y, j)] + n[sh(sh(y, i), j)]) / 4
                out[("f", y, (i, j))] = fm / (4 * ALPHA) * P.get(("f", y, (i, j)), 0)
        return out

    def r1_coeffs(n):  # position-space second differences, built independently of Part A
        out = {k: F(0) for k in HIDX}
        for x in S:
            for j in range(3):
                for i in range(3):
                    if i != j:
                        for z, w in ((sh(x, i), -1), (x, 2), (sh(x, i, -1), -1)):
                            out[("d", z, j)] += n[x] * w
            for (i, j) in PAIRS:
                for z, w in ((x, 1), (sh(x, i, -1), -1), (sh(x, j, -1), -1), (sh(sh(x, i, -1), j, -1), 1)):
                    out[("f", z, (i, j))] += 2 * n[x] * w
        return out

    def D_of_bond(x, j):
        col = {}
        def add(k, v):
            col[k] = col.get(k, 0) + v
        add(("d", x, j), 2)
        add(("d", sh(x, j), j), -2)
        for (a, b) in PAIRS:
            if j == b:
                add(("f", sh(x, a, -1), (a, b)), 1)
                add(("f", x, (a, b)), -1)
            if j == a:
                add(("f", sh(x, b, -1), (a, b)), 1)
                add(("f", x, (a, b)), -1)
        return col

    def matter_Q(n, m, c):
        def W(nn):
            w = {}
            for x in S:
                w[(x, x)] = w.get((x, x), 0) + MU * nn[x]
                for j in range(3):
                    y = sh(x, j)
                    nb = (nn[x] + nn[y]) / 2 * c
                    for (a, b, v) in ((x, x, 1), (y, y, 1), (x, y, -1), (y, x, -1)):
                        w[(a, b)] = w.get((a, b), 0) + nb * v
            return w
        q = {}
        for (la, lb, sg) in ((n, m, 1), (m, n, -1)):
            for (a, b), v in W(la).items():
                q[(a, b)] = q.get((a, b), 0) + sg * v * lb[b]
        return {k: v for k, v in q.items() if v != 0}

    def B_of_bond(x, j):
        y = sh(x, j)
        return {(y, x): F(1, 2), (y, y): F(1, 2), (x, x): F(-1, 2), (x, y): F(-1, 2)}

    def qq(v):
        v = F(v)
        return QQ(v.numerator, v.denominator)

    def closes(n, m, s, cs):
        rn, rm = r1_coeffs(n), r1_coeffs(m)
        am, an = kin_grad(m, rn), kin_grad(n, rm)
        rows, rhs = {}, {}
        for (x, j), bi in BIDX.items():
            for k, v in D_of_bond(x, j).items():
                rows.setdefault(("g", k), {})[bi] = rows.get(("g", k), {}).get(bi, 0) + v
            for sp_ in range(len(cs)):
                for k, v in B_of_bond(x, j).items():
                    rows.setdefault(("m", sp_, k), {})[bi] = rows.get(("m", sp_, k), {}).get(bi, 0) + v
        for k in HIDX:
            rhs[("g", k)] = s * K * (am[k] - an[k])
        for sp_, c in enumerate(cs):
            for k, v in matter_Q(n, m, c).items():
                rhs[("m", sp_, k)] = v
        keys = sorted(set(rows) | set(rhs), key=str)
        A = [[qq(rows.get(r, {}).get(b, 0)) for b in range(NB)] for r in keys]
        Ab = [row + [qq(rhs.get(r, 0))] for row, r in zip(A, keys)]
        return DomainMatrix(A, (len(keys), NB), QQ).rank() == DomainMatrix(Ab, (len(keys), NB + 1), QQ).rank()

    rng = random.Random(777)
    n, m = ({x: F(rng.randint(-4, 4)) for x in S} for _ in range(2))
    tab = {(s, str(r)): closes(n, m, s, [r * KAP]) for s in (1, -1) for r in (F(1), F(-1), F(2), F(1, 2))}
    exp = {k: F(k[1]) == -k[0] for k in tab}
    two = {str(r): closes(n, m, -1, [KAP, r * KAP]) for r in (F(1), F(2), F(1, 3))}
    check(f"A6 (L={L}) second implementation", tab == exp and two == {"1": True, "2": False, "1/3": False},
          f"matrix-form brackets, independently built R1, alpha=2/5, K=7/3, mu=5/2: closure table {tab}; two species {two}")


# =====================================================================================================
# Part B: the sign of block 101's curvature term (sympy)
# =====================================================================================================
def part_B():
    print("\n=== Part B: the curvature-term sign of block 101's action ===", flush=True)
    # B1: linearised scalar curvature of g = delta + eps h(x) equals R1 = d_i d_j h_ij - lap tr h
    X = sp.symbols("x0:3")
    eps = sp.Symbol("eps")
    hf = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(i, 3):
            hf[i][j] = hf[j][i] = sp.Function(f"h{i}{j}")(*X)
    g = sp.Matrix(3, 3, lambda i, j: (1 if i == j else 0) + eps * hf[i][j])
    ginv = sp.Matrix(3, 3, lambda i, j: (1 if i == j else 0) - eps * hf[i][j])  # inverse to O(eps)
    Gam = [[[sp.expand(sum(ginv[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                           for d in range(3)) / 2) for c in range(3)] for b in range(3)] for a in range(3)]
    ric = lambda b, c: (sum(sp.diff(Gam[a][b][c], X[a]) for a in range(3)) - sum(sp.diff(Gam[a][b][a], X[c]) for a in range(3))
                        + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for a in range(3) for d in range(3)))
    R = sum(ginv[b, c] * ric(b, c) for b in range(3) for c in range(3))
    R1lin = sp.expand(R).coeff(eps, 1)
    target = sum(sp.diff(hf[i][j], X[i], X[j]) for i in range(3) for j in range(3)) - sum(sp.diff(hf[k][k], X[j], X[j]) for k in range(3) for j in range(3))
    check("B1 R1 is the linearised scalar curvature", sp.simplify(R1lin - target) == 0,
          "for g = delta + eps h: R(g) = eps (d_i d_j h_ij - lap tr h) + O(eps^2) = eps R1 (block 62's symbol p^2 tr h - p.h.p); "
          "so with N = 1 + u the O(u h) part of K wbar N sqrt(g) R - N rho is K wbar u R1 - e u, the sign of block 101's u-coupling "
          "(its R2 is not re-derived here)")
    # B2: Legendre transform of block 101's mode Lagrangian, lapse coefficient
    al, be, K, wb, P, v, u, e, R1s, R2s = sp.symbols("alpha beta K wbar P v u e R1 R2")
    Lag = (al + be) * v ** 2 / wb + K * wb * (u * R1s + R2s) - e * u  # one velocity component suffices for the u-coefficient
    vsol = sp.solve(sp.Eq(sp.diff(Lag, v), P), v)[0]
    H = sp.expand((P * v - Lag).subs(v, vsol))
    check("B2 Hamiltonian carries -K R1", sp.simplify(sp.diff(H, u) - (-K * wb * R1s + e)) == 0,
          f"H = P qdot - L for L = kin + K wbar (u R1 + R2) - e u gives dH/du = {sp.diff(H, u)}: the lapse constraint is kin - K R1 + e, "
          "i.e. s = -1; the 09-24 runner's +K R1 (s = +1) is opposite to its own action (harmless for gravity alone, A1)")


# =====================================================================================================
# Part C: order phi^2 of {G[xi], C(N)} -- exact rank certificates (after chk_e5_obstruction.py)
# =====================================================================================================
def part_C(L, which, seed=11, nconf=3):
    S = list(product(range(L), repeat=3))
    E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    add = lambda a, b, s=1: tuple((a[k] + s * b[k]) % L for k in range(3))

    def vec(*terms):
        w = [0, 0, 0]
        for c, k in terms:
            w[k] += c
        return tuple(w)
    STAR = [(0, 0, 0)] + [vec((s, k)) for k in range(3) for s in (1, -1)]
    STAR19 = STAR + [vec((s, k), (t, l)) for k in range(3) for l in range(k + 1, 3) for s in (1, -1) for t in (1, -1)]

    def corners(ij):
        i, j = ij
        return [(0, 0, 0), E[i], E[j], tuple(E[i][k] + E[j][k] for k in range(3))]

    def face_ext(ij):
        i, j = ij
        ext = set(corners(ij))
        for p in corners(ij):
            for k in (i, j):
                for s in (1, -1):
                    ext.add(tuple(p[mm] + (s if mm == k else 0) for mm in range(3)))
        return sorted(ext)
    mono = lambda z, w: (z, w) if z <= w else (w, z)

    def dxi(xi, kind, z, comp):
        if kind == "d":
            return 2 * (xi[(z, comp)] - xi[(add(z, E[comp], -1), comp)])
        a, b = comp
        return xi[(add(z, E[a]), b)] - xi[(z, b)] + xi[(add(z, E[b]), a)] - xi[(z, a)]

    ansatz, control = which
    ops = []
    for j in range(3):
        for uv in combinations_with_replacement(STAR19 if ansatz == "B" else STAR, 2):
            for lp in ([("site", w) for w in STAR] if ansatz == "C" else [("site", (0, 0, 0))]):
                ops.append(("d", j, uv, lp))
    for ij in PAIRS:
        for uv in combinations_with_replacement(face_ext(ij) if ansatz == "B" else corners(ij), 2):
            for lp in ([("site", w) for w in corners(ij)] if ansatz == "C" else [("mean4", None)]):
                ops.append(("f", ij, uv, lp))

    def lapse_val(n, z, comp, lp):
        if lp[0] == "site":
            return n[add(z, lp[1])]
        return sum(n[add(z, cc)] for cc in corners(comp)) / 4

    rng = random.Random(seed)
    nop = len(ops)
    cols, rhs, rowid = {}, {}, {}
    rid = lambda key: rowid.setdefault(key, len(rowid))
    ncol = nop + nconf * len(S)
    for cf in range(nconf):
        n = {x: F(rng.randint(-4, 4)) for x in S}
        xi = {(x, j): F(rng.randint(-4, 4)) for x in S for j in range(3)}
        # pi-pi part of {G_m[xi], H_m(N)} = sum_b (xi_b/2)(pi_x + pi_y)(N_y pi_y - N_x pi_x)
        for x in S:
            for j in range(3):
                y = add(x, E[j])
                b = xi[(x, j)]
                for mm, val in ((mono(y, y), b * n[y] / 2), (mono(x, x), -b * n[x] / 2), (mono(x, y), b * (n[y] - n[x]) / 2)):
                    rhs[rid((cf, mm))] = rhs.get(rid((cf, mm)), 0) + val
                if control:  # remove ob = (xi_b/2)(N_y - N_x)[pi_x pi_y - (pi_x^2 + pi_y^2)/2]
                    ob = b * (n[y] - n[x]) / 2
                    for mm, val in ((mono(x, y), -ob), (mono(x, x), ob / 2), (mono(y, y), ob / 2)):
                        rhs[rid((cf, mm))] = rhs.get(rid((cf, mm)), 0) + val
        # {G_g[xi], sum lapse h O} = sum lapse (delta_xi h) O
        for p, (kind, comp, (u, v), lp) in enumerate(ops):
            col = cols.setdefault(p, {})
            for z in S:
                d = dxi(xi, kind, z, comp)
                if d == 0:
                    continue
                w = d * lapse_val(n, z, comp, lp)
                if w:
                    r = rid((cf, mono(add(z, u), add(z, v))))
                    col[r] = col.get(r, 0) + w
        for zi, z in enumerate(S):  # free N'_z: (1/2) N'_z pi_z^2
            cols.setdefault(nop + cf * len(S) + zi, {})[rid((cf, mono(z, z)))] = F(1, 2)
    rows = [dict() for _ in range(len(rowid))]
    for c, col in cols.items():
        for r, v in col.items():
            if v:
                rows[r][c] = F(v)
    for r, v in rhs.items():
        if v:
            rows[r][ncol] = F(v)
    return (nop, len(rowid)) + solve_certificate(rows, ncol)


# ---- exact certificates found by modular elimination, verified over Q ---------------------------------
def ratrec(a, p):
    """rational reconstruction of a mod p (|num|, den <= sqrt(p/2)); None if it fails."""
    a %= p
    bound = math.isqrt(p // 2)
    r0, r1, t0, t1 = p, a, 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1, t0, t1 = r1, r0 - q * r1, t1, t0 - q * t1
    if t1 == 0 or abs(t1) > bound:
        return None
    return F(r1, t1)


def solve_certificate(rows, ncol, primes=(2 ** 127 - 1, 2 ** 521 - 1, 2 ** 1279 - 1, 2 ** 2203 - 1)):
    """rows: exact sparse rows of [A|b] (b in column ncol). Gaussian elimination over GF(p) with pivot = lowest
    A-column, tracking row combinations. If some combination y kills A but not b, y is reconstructed over Q and
    VERIFIED exactly (y^T A = 0, y^T b != 0): an exact certificate that A x = b has no solution. Otherwise a solution
    x (free unknowns 0) is reconstructed and VERIFIED exactly (A x = b) for these rows.
    Returns (rank_p A, rank_p [A|b], verdict, verified); verdict in {'inconsistent', 'consistent'}.
    Modular ranks are lower bounds on the rational ranks; only the verified certificate is load-bearing."""
    for p in primes:
        modrows = []
        for rw in rows:
            modrows.append({c: (v.numerator * pow(v.denominator, -1, p)) % p for c, v in rw.items()})
        piv = {}  # col -> (row dict, tag dict), row normalised to 1 at col
        cert = None
        for i, rw in enumerate(modrows):
            vec, tag = dict(rw), {i: 1}
            while True:
                acols = [c for c in vec if c < ncol]
                if not acols:
                    break
                c0 = min(acols)
                if c0 not in piv:
                    inv = pow(vec[c0], -1, p)
                    vec = {c: v * inv % p for c, v in vec.items()}
                    tag = {t: v * inv % p for t, v in tag.items()}
                    piv[c0] = (vec, tag)
                    vec = None
                    break
                f = vec[c0]
                pv, pt = piv[c0]
                for c, v in pv.items():
                    nv = (vec.get(c, 0) - f * v) % p
                    if nv:
                        vec[c] = nv
                    else:
                        vec.pop(c, None)
                for t, v in pt.items():
                    nv = (tag.get(t, 0) - f * v) % p
                    if nv:
                        tag[t] = nv
                    else:
                        tag.pop(t, None)
            if vec is not None and vec.get(ncol, 0) and cert is None:
                cert = tag
        rank_a = len(piv)
        rank_ab = rank_a + (1 if cert is not None else 0)
        if cert is not None:
            y = {t: ratrec(v, p) for t, v in cert.items()}
            if any(v is None for v in y.values()):
                continue
            yA = {}
            yb = F(0)
            for t, v in y.items():
                for c, a in rows[t].items():
                    if c == ncol:
                        yb += v * a
                    else:
                        yA[c] = yA.get(c, 0) + v * a
            ok = yb != 0 and all(v == 0 for v in yA.values())
            if ok:
                return rank_a, rank_ab, "inconsistent", True
            continue
        # consistent mod p: back-substitute (free unknowns = 0), reconstruct, verify exactly
        x = {}
        for c0 in sorted(piv, reverse=True):
            pv, _ = piv[c0]
            val = pv.get(ncol, 0)
            for c, v in pv.items():
                if c != c0 and c != ncol:
                    val -= v * x.get(c, 0)
            x[c0] = val % p
        xq = {c: ratrec(v, p) for c, v in x.items() if v}
        if any(v is None for v in xq.values()):
            continue
        ok = all(sum((a * xq.get(c, 0) for c, a in rw.items() if c != ncol), F(0)) == rw.get(ncol, 0) for rw in rows)
        if ok:
            return rank_a, rank_ab, "consistent", True
    return None, None, "undetermined", False


def part_C_all(do_L4):
    print("\n=== Part C: order phi^2 of {G[xi], C(N)}, pi-pi sector, exact rank certificates ===", flush=True)
    # C0: the obstruction monomial is a squared difference (O(a^2))
    px, py, Nx, Ny, xb = sp.symbols("pi_x pi_y N_x N_y xi_b")
    ob = xb * (Ny - Nx) / 2 * (px * py - (px ** 2 + py ** 2) / 2)
    full = xb / 2 * (px + py) * (Ny * py - Nx * px)
    rest = sp.expand(full - ob)
    check("C0 obstruction monomial", sp.expand(ob + xb * (Ny - Nx) * (py - px) ** 2 / 4) == 0
          and sp.expand(rest - (xb / 2) * ((Ny * py ** 2 - Nx * px ** 2) + (Ny - Nx) * (px ** 2 + py ** 2) / 2)) == 0,
          "per bond, (xi_b/2)(pi_x+pi_y)(N_y pi_y - N_x pi_x) = [diagonal pi_z^2 terms] + ob, with "
          "ob = (xi_b/2)(N_y-N_x)[pi_x pi_y - (pi_x^2+pi_y^2)/2] = -(1/4) xi_b (N_(x+e)-N_x)(pi_(x+e)-pi_x)^2 "
          "(the pi_x pi_(x+e) xi_b (N_(x+e)-N_x) cross term; two differences, O(a^2) relative to xi.grad N pi^2)")
    cases = [((("A", True)), 3, "C1", "positive control, ansatz A (matched timing), obstruction removed", True),
             ((("A", False)), 3, "C2", "ansatz A (matched timing: site lapse on h_jj, four-corner mean on h_ij; 7-point star / face-corner pi pairs)", False),
             ((("C", False)), 3, "C3", "ansatz C (lapse placement free per term within star / face corners)", False),
             ((("B", False)), 3, "C4", "ansatz B (longer range: 19-point diag pairs, 12-point face pairs)", False)]
    if do_L4:
        cases += [((("A", True)), 4, "C5", "positive control, ansatz A, L = 4", True),
                  ((("A", False)), 4, "C6", "ansatz A, L = 4", False)]
    for which, L, tag, desc, want_close in cases:
        t = time.time()
        nop, nrow, ra, rb, verdict, verified = part_C(L, which)
        ok = verified and verdict == ("consistent" if want_close else "inconsistent")
        cert = ("exact solution x with A x = b verified over Q on the sampled configurations" if verdict == "consistent"
                else "exact left vector y with y^T A = 0, y^T b != 0 verified over Q")
        check(f"{tag} (L={L}) {'closes' if want_close else 'no closure'}", ok,
              f"{desc}: {nop} coupling ops, {nrow} eqs, GF(p) ranks A = {ra}, [A|b] = {rb}; certificate: {cert if verified else 'NONE'} "
              f"({time.time() - t:.0f}s)")


# =====================================================================================================
# Part D: continuum leading order (exact sympy jet calculus), after b14_continuum_leading_order.py
# =====================================================================================================
def part_D():
    print("\n=== Part D: continuum leading order (sympy jet calculus) ===", flush=True)
    DIM = 3
    JET, S2K = {}, {}

    def J(field, a=(0, 0, 0)):
        key = (field, tuple(a))
        if key not in JET:
            JET[key] = sp.Symbol(field + "_" + "".join(map(str, a)))
            S2K[JET[key]] = key
        return JET[key]

    def D(expr, k):
        expr = sp.expand(expr)
        out = 0
        for s in expr.free_symbols:
            if s in S2K:
                f, a = S2K[s]
                b = list(a)
                b[k] += 1
                out += sp.diff(expr, s) * J(f, b)
        return sp.expand(out)

    def Dalpha(expr, a):
        for k in range(DIM):
            for _ in range(a[k]):
                expr = D(expr, k)
        return expr

    def euler(expr, field):
        expr = sp.expand(expr)
        out = 0
        for s in list(expr.free_symbols):
            if s in S2K and S2K[s][0] == field:
                a = S2K[s][1]
                out += (-1) ** sum(a) * Dalpha(sp.diff(expr, s), a)
        return sp.expand(out)

    ev = lambda i: tuple(1 if k == i else 0 for k in range(DIM))
    grad = lambda f: [J(f, ev(i)) for i in range(DIM)]

    def d2(f, i, j):
        a = [0] * DIM
        a[i] += 1
        a[j] += 1
        return J(f, a)
    HD = [f"hd{j}" for j in range(DIM)]
    HF = {ij: f"hf{ij[0]}{ij[1]}" for ij in PAIRS}
    PD = [f"Pd{j}" for j in range(DIM)]
    PF = {ij: f"Pf{ij[0]}{ij[1]}" for ij in PAIRS}
    CONJ = {"phi": "pi", **{HD[j]: PD[j] for j in range(DIM)}, **{HF[ij]: PF[ij] for ij in PAIRS}}
    al, K, c, mu = sp.symbols("alpha K c mu", positive=True)
    A = sp.symbols("A1:8")
    B = sp.symbols("B1:3")
    s1, s2, r1, r2, lam = sp.symbols("s1 s2 r1 r2 lam")
    phi, pi = J("phi"), J("pi")
    N, M = J("N"), J("M")
    XI = [f"xi{k}" for k in range(DIM)]
    kap = K / (4 * al)

    hm = lambda cc=c: pi ** 2 / 2 + cc * sum(g_ ** 2 for g_ in grad("phi")) / 2 + mu * phi ** 2 / 2

    def coupling():
        gp = grad("phi")
        lp = sum(d2("phi", k, k) for k in range(DIM))
        out = 0
        for j in range(DIM):
            out += J(HD[j]) * (A[0] * pi ** 2 + A[1] * sum(g_ ** 2 for g_ in gp) + A[2] * gp[j] ** 2 + A[3] * phi ** 2
                               + A[4] * phi * pi + A[5] * phi * d2("phi", j, j) + A[6] * phi * lp)
        for (i, j) in PAIRS:
            out += J(HF[(i, j)]) * (B[0] * gp[i] * gp[j] + B[1] * phi * d2("phi", i, j))
        return out

    def r1d():
        out = 0
        for j in range(DIM):
            out += d2(HD[j], j, j) - sum(d2(HD[j], k, k) for k in range(DIM))
        for (i, j) in PAIRS:
            out += 2 * d2(HF[(i, j)], i, j)
        return out

    def kind():
        tr = sum(J(p) for p in PD)
        return (sum(J(p) ** 2 for p in PD) - tr ** 2 / 2) / (4 * al) + sum(J(PF[ij]) ** 2 for ij in PAIRS) / (8 * al)

    def br(f, g):
        out = 0
        for q, p in CONJ.items():
            out += euler(f, q) * euler(g, p) - euler(f, p) * euler(g, q)
        return sp.expand(out)

    def ggrav(xin):
        out = 0
        for j in range(DIM):
            out += J(PD[j]) * 2 * J(xin[j], ev(j))
        for (i, j) in PAIRS:
            out += J(PF[(i, j)]) * (J(xin[j], ev(i)) + J(xin[i], ev(j)))
        return out
    gmat = lambda xv: pi * sum(xv[k] * grad("phi")[k] for k in range(DIM))

    def coeffs(expr):
        expr = sp.expand(expr)
        jets = [s for s in expr.free_symbols if s in S2K]
        return [e for e in (sp.expand(cf) for cf in sp.Poly(expr, *jets).coeffs()) if e != 0] if jets else ([expr] if expr != 0 else [])

    # D0 comparator: O(h) part of the metric matter Hamiltonian
    e_ = sp.Symbol("eps")
    hs = sp.symbols("h00 h11 h22 h01 h02 h12")
    g = sp.Matrix([[1 + e_ * hs[0], e_ * hs[3], e_ * hs[4]], [e_ * hs[3], 1 + e_ * hs[1], e_ * hs[5]], [e_ * hs[4], e_ * hs[5], 1 + e_ * hs[2]]])
    gp = sp.Matrix(grad("phi"))
    sq = sp.sqrt(g.det())
    hmg = pi ** 2 / (2 * sq) + sq * (c * (gp.T * g.inv() * gp)[0, 0] + mu * phi ** 2) / 2
    lin1 = sp.expand(sp.series(hmg, e_, 0, 2).removeO().coeff(e_, 1))
    gl = grad("phi")
    tgt = sum(hs[j] * (-pi ** 2 / 4 + c * sum(x ** 2 for x in gl) / 4 - c * gl[j] ** 2 / 2 + mu * phi ** 2 / 4) for j in range(DIM)) \
        + sum(hs[3 + k] * (-c * gl[i] * gl[j]) for k, (i, j) in enumerate(PAIRS))
    check("D0 comparator stress", sp.simplify(lin1 - sp.expand(tgt)) == 0,
          "O(h) part of pi^2/(2 sqrt g) + sqrt g (c g^ij d phi d phi + mu phi^2)/2: T_jj = -pi^2/4 + c|grad phi|^2/4 - c(d_j phi)^2/2 + mu phi^2/4, U_ij = -c d_i phi d_j phi")

    # D1 {C,C} at O(eps): c = K/(4 alpha)
    CN = N * (kind() - K * r1d() + hm())
    CM = M * (kind() - K * r1d() + hm())
    xi0 = [N * gm - M * gn for gn, gm in zip(grad("N"), grad("M"))]
    gg = sum(J(PD[j]) * 2 * D(kap * xi0[j], j) for j in range(DIM)) + sum(J(PF[(i, j)]) * (D(kap * xi0[j], i) + D(kap * xi0[i], j)) for (i, j) in PAIRS)
    sol = sp.solve(coeffs(euler(br(CN, CM) - gg - gmat([kap * x for x in xi0]), "N")), c, dict=True)
    check("D1 continuum cone", sol == [{c: K / (4 * al)}],
          f"{{C(N),C(M)}} = G_g[xi0] + G_m[xi0], xi0 here is unscaled N grad M - M grad N; both G arguments are kappa*xi0, C = kin - K R1 + H_m: solve -> {sol}")

    # D2 {G,C} at O(phi^2): one-parameter family = metric-variational stress + lam * trace
    xi = [J(n_) for n_ in XI]
    nprime = s1 * sum(xi[k] * grad("N")[k] for k in range(DIM)) + s2 * N * sum(J(XI[k], ev(k)) for k in range(DIM))
    eqs2 = coeffs(euler(br(gmat(xi), N * hm()) + br(ggrav(XI), N * coupling()) - nprime * hm(), "N"))
    sol2 = sp.solve(eqs2, list(A) + list(B) + [s1, s2], dict=True)
    target = {A[0]: -sp.Rational(1, 4) + lam / 2, A[1]: c / 4 + lam * c / 2, A[2]: -c / 2, A[3]: mu / 4 + lam * mu / 2,
              A[4]: 0, A[5]: 0, A[6]: 0, B[0]: -c, B[1]: 0, s1: 1, s2: -2 * lam}
    ok2 = False
    if len(sol2) == 1:
        s_ = sol2[0]
        free = sorted(set(list(A) + list(B) + [s1, s2]) - set(s_), key=str)
        if len(free) == 1:
            sub = {free[0]: sp.solve(sp.Eq(sp.sympify(s_.get(A[0], A[0])), target[A[0]]), free[0])[0]}
            ok2 = all(sp.simplify(sp.sympify(s_.get(k, k)).subs(sub) - v) == 0 for k, v in target.items())
    check("D2 {G,C} selects the metric-variational stress", ok2,
          "{G_g[xi]+G_m[xi], H_m(N) + int N h.T} at O(phi^2) = H_m(s1 xi.grad N + s2 N div xi): the 9-coefficient ansatz has the one-parameter "
          "solution T = metric-variational stress of H_m(g) + lam delta_ij (H_m density), s1 = 1, s2 = -2 lam")

    # D3/D4: with the {C,C} O(h phi pi) equations; scalar lapse s2 = 0 -> unique; structure function g^ij = delta - h
    H = [[None] * DIM for _ in range(DIM)]
    for j in range(DIM):
        H[j][j] = J(HD[j])
    for (i, j) in PAIRS:
        H[i][j] = H[j][i] = J(HF[(i, j)])
    trh = sum(H[j][j] for j in range(DIM))
    hk = hm(kap)
    brh = br(N * coupling(), M * hk) + br(N * hk, M * coupling())
    xip = [kap * sum((r1 * H[i][j] + (r2 * trh if i == j else 0)) * xi0[j] for j in range(DIM)) for i in range(DIM)]
    eqs3 = coeffs(euler(brh - gmat(xip), "N"))
    zero = {v_: 0 for v_ in list(A) + list(B) + [r1, r2]}
    check("D3 {C,C} alone does not fix the coupling", all(sp.simplify(e.subs(zero)) == 0 for e in eqs3),
          "T = 0 with xi' = 0 solves the O(h phi pi) part of {C,C}: the source is selected by {G,C}, not by {C,C}")
    eqs2k = [sp.expand(e.subs(c, kap)) for e in eqs2]
    sol4 = sp.solve([e.subs(s2, 0) for e in eqs2k] + eqs3, list(A) + list(B) + [s1, r1, r2], dict=True)
    grk = {A[0]: -sp.Rational(1, 4), A[1]: kap / 4, A[2]: -kap / 2, A[3]: mu / 4, A[4]: 0, A[5]: 0, A[6]: 0, B[0]: -kap, B[1]: 0, s1: 1, r1: -1, r2: 0}
    ok4 = len(sol4) == 1 and all(sp.simplify(sp.sympify(sol4[0].get(k, k)) - v) == 0 for k, v in grk.items())
    check("D4 scalar lapse: unique coupling, GR structure function", ok4,
          f"s2 = 0 (scalar-lapse rule, supplied): unique solution {sol4}; coupling = metric-variational stress at c = K/(4alpha), "
          "xi'_i = -kappa h_ij xi0_j (g^ij = delta^ij - h^ij)")
    sol5 = sp.solve([e.subs(s2, -2 * lam) for e in eqs2k] + eqs3, list(A) + list(B) + [s1, r1, r2], dict=True)
    r2l = sp.simplify(sol5[0].get(r2, r2)) if len(sol5) == 1 else None
    check("D5 trace weight shifts the structure function", len(sol5) == 1 and r2l is not None and sp.simplify(r2l - 2 * lam) == 0,
          f"with T = T_metric + lam delta H and s2 = -2 lam the structure-function trace is r2 = {r2l}: species with different lam cannot share one xi', so lam is common")


# =====================================================================================================
# Optional E6 diagnostic (floating point, not gating)
# =====================================================================================================
def e6(L):
    lat = Lattice(L, F(3, 7), F(5, 11), F(2, 3))
    kappa = lat.KK / (4 * lat.ALPHA)
    tw = 2 * math.pi / L
    wave = lambda kv, ph=0.0: {x: math.cos(tw * sum(kv[i] * x[i] for i in range(3)) + ph) for x in lat.SITES}
    q1, q2, k1, k2 = (1, 0, 0), (0, 1, 0), (1, 1, 1), (0, -1, 2)
    k3 = tuple(-(q1[i] + q2[i] + k1[i]) for i in range(3))
    k4 = tuple(-(q1[i] + q2[i] + k2[i]) for i in range(3))
    wn, wx = wave(q1), wave(q2, 0.3)
    n = {x: 1.0 + 0.5 * wn[x] for x in lat.SITES}
    xi = {(x, j): (0.7 + 0.2 * j) * wx[x] for x in lat.SITES for j in range(3)}
    w1, w3, w2, w4 = wave(k1), wave(k3, 0.4), wave(k2, 0.1), wave(k4, 0.7)
    val = {}
    for nm, i in lat.VAR.items():
        if nm[0] == "phi":
            val[i] = w1[nm[1]] + w3[nm[1]]
        elif nm[0] == "pi":
            val[i] = w2[nm[1]] + w4[nm[1]]
    sh = lat.sh
    nprime = {x: 0.5 * sum(xi[(x, j)] * (n[sh(x, j)] - n[x]) + xi[(sh(x, j, -1), j)] * (n[x] - n[sh(x, j, -1)]) for j in range(3)) for x in lat.SITES}

    def evp(poly):
        tot = 0.0
        for m_, cv in poly.items():
            t = float(cv)
            for v in m_:
                t *= val[v]
            tot += t
        return tot
    # floating lapse/xi are used directly as coefficients (diagnostic only)
    base = evp(bracket(lat, g_matter(lat, xi), h_matter(lat, n, kappa)))
    rhs = evp(h_matter(lat, nprime, kappa))
    # lattice image of the metric-variational stress on h_jj (site) and h_ij (face);
    # {G_g[xi], sum lapse h O} = -sum lapse (delta_xi h) O with {h, P} = 1
    kf, muf = float(kappa), float(lat.MU)
    coup = 0.0
    for x in lat.SITES:
        phx, pix = val[lat.var(("phi", x))], val[lat.var(("pi", x))]
        S = []
        for k in range(3):
            f_ = val[lat.var(("phi", sh(x, k)))] - phx
            b_ = phx - val[lat.var(("phi", sh(x, k, -1)))]
            S.append((f_ * f_ + b_ * b_) / 2)
        for j in range(3):
            dh = 2 * (xi[(x, j)] - xi[(sh(x, j, -1), j)])
            T = -pix ** 2 / 4 + kf * sum(S) / 4 - kf * S[j] / 2 + muf * phx ** 2 / 4
            coup -= n[x] * dh * T
    for y in lat.SITES:
        for (i, j) in PAIRS:
            c4 = [y, sh(y, i), sh(y, j), sh(sh(y, i), j)]
            ph = [val[lat.var(("phi", z))] for z in c4]
            Bi, Bj = -ph[0] + ph[1] - ph[2] + ph[3], -ph[0] - ph[1] + ph[2] + ph[3]
            dh = xi[(sh(y, i), j)] - xi[(y, j)] + xi[(sh(y, j), i)] - xi[(y, i)]
            coup -= sum(n[z] for z in c4) / 4 * dh * (-kf / 4) * Bi * Bj
    print(f"  E6 L={L}: |base|={abs(base):.6e}  residual(stress)={base + coup - rhs:.6e}  ratio={abs((base + coup - rhs) / base):.6e}  "
          f"residual(no coupling)={base - rhs:.6e}", flush=True)


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--e6" in args:
        print("E6 diagnostic (floating point; NOT a gating test; one configuration):")
        sizes = [int(a) for a in args if a.isdigit()] or [6, 8, 12]
        for L in sizes:
            e6(L)
        sys.exit(0)
    quick = "--quick" in args
    part_A(3, 20261018)
    if not quick:
        part_A(4, 20261018)
    part_A6(3)
    part_B()
    part_C_all(do_L4=not quick)
    part_D()
    print(f"\nelapsed {time.time() - T0:.0f}s")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    sys.exit(0 if FAIL == 0 else 1)
