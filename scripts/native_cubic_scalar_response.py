from pathlib import Path
from neutral_continuation_runtime_2026_10_18 import Execution
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
    'archive/neutral_composite_continuation_review_2026_10_18/MANIFEST.json',
    'docs/NATIVE_BULK_SEGMENT_RESONANCE_NOTE_2026-10-18.md',
    'docs/NATIVE_COLUMN_COLLECTIVE_MODE_NOTE_2026-10-18.md',
    'docs/NATIVE_COLUMN_PLAQUETTE_SELECTION_NOTE_2026-10-18.md',
    'docs/NATIVE_CORRECTED_FAST_STRIP_NOTE_2026-10-18.md',
    'docs/NATIVE_CUBIC_SCALAR_RESPONSE_NOTE_2026-10-18.md',
    'docs/NATIVE_DERIVED_COLLECTIVE_INTERACTION_NOTE_2026-10-18.md',
    'docs/NATIVE_FOUR_COLUMN_COMPETITION_NOTE_2026-10-18.md',
    'docs/NATIVE_INFRARED_READOUT_NOTE_2026-10-18.md',
    'docs/NATIVE_LARGE_COLUMN_DYNAMICS_NOTE_2026-10-18.md',
    'docs/NATIVE_LOCAL_NORMALFORM_NOTE_2026-10-18.md',
    'docs/NATIVE_LOCAL_NORMAL_FORM_NOTE_2026-10-18.md',
    'docs/NATIVE_LOOP_INTERACTION_NOTE_2026-10-18.md',
    'docs/NATIVE_NEUTRAL_DOMAIN_RESONANCE_NOTE_2026-10-18.md',
    'docs/NATIVE_SCALAR_BAND_LOCAL_PROOF_NOTE_2026-10-18.md',
    'docs/NATIVE_SLOW_BULK_COMPOSITE_NOTE_2026-10-18.md',
    'docs/NATIVE_SLOW_COMPOSITE_CONTROL_NOTE_2026-10-18.md',
    'docs/NATIVE_ZONE_BOUNDARY_COMPOSITE_NOTE_2026-10-18.md',
    'docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/INPUT_CLOSURE.json',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9717/compass_sector_basis.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9717/neutral_boundary_vertex.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9717/neutral_rung_effective.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9717/neutral_rung_fourth.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9717/neutral_rung_linked_fourth.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9717/neutral_rung_model.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9717/neutral_rung_sixth.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9717/neutral_rung_sixth_exact.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9717/neutral_rung_u1_probe.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9717/neutral_tube_rung_control.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9720/neutral_anisotropy_comparison.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9720/neutral_open_xy_comparison.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9720/neutral_rung_discrete_symmetry.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9720/neutral_rung_model.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9720/neutral_xy_readout.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9722/neutral_exact_internal_factor.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9722/neutral_rung_model.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9722/neutral_strong_spectrum.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9722/neutral_strong_symmetry.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9722/neutral_strong_tunnel.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9724/neutral_dark_bound_math.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9724/neutral_kink_core.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9724/neutral_kink_dark_fourth_action.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9724/neutral_kink_dark_fourth_diagonal.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9724/neutral_kink_dark_rational.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9724/neutral_kink_dark_resonance.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9724/neutral_kink_dark_third.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9724/neutral_kink_fourth_overlap.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9724/neutral_kink_fourth_rational.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9724/neutral_kink_full_third_check.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9724/neutral_kink_physical_q_source.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9724/neutral_kink_q_certificate.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9724/neutral_kink_source_dressing.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9724/neutral_rung_model.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9726/compass_sector_basis.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9726/compass_sector_solve.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9726/neutral_band_scalar_reflection_sector.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9726/neutral_domain_boundary_local.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9726/neutral_extra_sector.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9726/neutral_kink_core.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9726/neutral_rung_model.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9726/neutral_scalar_explicit_basis.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9726/neutral_wall_connected.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9726/neutral_wall_full_kernel.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9727/compass_sector_basis.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9727/compass_sector_solve.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9727/neutral_extra_sector.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9727/neutral_kink_core.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9727/neutral_rung_model.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9727/neutral_scalar_explicit_basis.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9727/neutral_zone_boundary.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9727/neutral_zone_exact_math.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9727/neutral_zone_large_feature.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9727/neutral_zone_local_second.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9728/neutral_kink_core.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9728/neutral_local_normal_form.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9728/neutral_packet_control.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9728/neutral_rung_model.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9730/neutral_column_parity_native.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9730/neutral_column_plaquette.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9732/neutral_column_six_mode.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9732/neutral_column_source_derivative.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/helpers/pr9732/neutral_rectangle_six.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/inputs/pr9717/tube_4.json',
    'outputs/neutral_composite_continuation_review_2026_10_18/inputs/pr9720/neutral_tube_anisotropy.json',
    'outputs/neutral_composite_continuation_review_2026_10_18/inputs/pr9724/neutral_kink_dark_fourth_action.json',
    'outputs/neutral_composite_continuation_review_2026_10_18/inputs/pr9724/neutral_kink_fourth_overlap.json',
    'outputs/neutral_composite_continuation_review_2026_10_18/inputs/pr9726/neutral_native_periodic_pole.json',
    'outputs/neutral_composite_continuation_review_2026_10_18/inputs/pr9727/neutral_native_periodic_pi_pole.json',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9717/DEFERRED_TERMINAL_PROMOTION.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9717/DERIVED_RUNG_COLLECTIVE.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9717/INDEPENDENT_BOUNDARY_VERTEX_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9717/INDEPENDENT_DERIVED_COLLECTIVE_REVIEW.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9717/INDEPENDENT_RUNG_EFFECTIVE_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9717/INDEPENDENT_RUNG_HIGHER_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9717/INDEPENDENT_SIXTH_CHARGE_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9717/INDEPENDENT_TUBE_RUNG_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9717/NATIVE_BOUNDARY_VERTEX.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9717/SIXTH_ORDER_COLLECTIVE_PROCESS.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9717/TUBE_RUNG_REDUCTION.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9720/DEFERRED_TERMINAL_PROMOTION.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9720/DERIVED_INFRARED_ROUTE.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9720/INDEPENDENT_ANISOTROPY_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9720/INDEPENDENT_DISCRETE_INFRARED_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9720/INDEPENDENT_INFRARED_FINAL_REVIEW.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9720/INDEPENDENT_XY_READOUT_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9722/DEFERRED_TERMINAL_PROMOTION.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9722/EXACT_INTERNAL_FACTOR.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9722/INDEPENDENT_EXACT_INTERNAL_FACTOR_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9722/INDEPENDENT_LARGE_COLUMN_AUX_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9722/INDEPENDENT_LARGE_COLUMN_FINAL_REVIEW.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9722/INDEPENDENT_STRONG_READOUT_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9722/INDEPENDENT_STRONG_TUNNEL_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9722/STRONG_COLUMN_FEATURE.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9724/INDEPENDENT_DARK_BOUND_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9724/INDEPENDENT_DARK_FOURTH_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9724/INDEPENDENT_DOMAIN_RESONANCE_FINAL_REVIEW.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9724/INDEPENDENT_KINK_FOURTH_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9724/INDEPENDENT_KINK_MOMENTUM_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9724/INDEPENDENT_KINK_RESONANCE_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9724/INDEPENDENT_KINK_SECOND_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9724/INDEPENDENT_KINK_THIRD_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9726/INDEPENDENT_LOCAL_BOUNDARY_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9726/INDEPENDENT_LOCAL_WALL_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9726/INDEPENDENT_NATIVE_PERIODIC_POLE_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9726/INDEPENDENT_SCALAR_BAND_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9726/LOCAL_PROOF_FINAL_REVIEW.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9727/DEFERRED_TERMINAL_PROMOTION.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9727/INDEPENDENT_NATIVE_PI_POLE_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9727/INDEPENDENT_ZONE_BOUNDARY_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9727/INDEPENDENT_ZONE_CROSSOVER_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9727/INDEPENDENT_ZONE_LARGE_FEATURE_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9727/INDEPENDENT_ZONE_LOCAL_SECOND_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9727/ZONE_BOUNDARY_FINAL_REVIEW.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9728/INDEPENDENT_PACKET_FILTER_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9728/INDEPENDENT_SOURCE_GRAM_FIBER_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9728/INDEPENDENT_UNIFORM_NORMAL_FORM_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9728/NORMAL_FORM_FINAL_REVIEW.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9730/COLUMN_PLAQUETTE_FINAL_REVIEW.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9730/INDEPENDENT_COLUMN_PLAQUETTE_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9730/INDEPENDENT_COLUMN_READOUT_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9732/COLUMN_COLLECTIVE_FINAL_REVIEW.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9732/DEFERRED_TERMINAL_PROMOTION.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9732/INDEPENDENT_COLUMN_SOURCE_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9732/INDEPENDENT_COLUMN_STAR_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/proofs/pr9732/INDEPENDENT_SIX_LOOP_CHECK.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/provenance/pr9720/compass_sector_basis.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/provenance/pr9720/compass_sector_solve.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/provenance/pr9720/neutral_extra_sector.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/provenance/pr9720/neutral_tube_anisotropy.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/provenance/pr9722/compass_sector_basis.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/provenance/pr9722/compass_sector_solve.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/provenance/pr9722/neutral_extra_sector.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/provenance/pr9722/neutral_internal_occupation.json',
    'outputs/neutral_composite_continuation_review_2026_10_18/provenance/pr9722/neutral_internal_occupation.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/provenance/pr9722/stationary_2x2x8_plus.json',
    'outputs/neutral_composite_continuation_review_2026_10_18/provenance/pr9726/LOCAL_PROOF_PROVENANCE.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/provenance/pr9726/neutral_native_periodic_pole.py',
    'outputs/neutral_composite_continuation_review_2026_10_18/provenance/pr9727/ZONE_BOUNDARY_PROVENANCE.md',
    'outputs/neutral_composite_continuation_review_2026_10_18/provenance/pr9727/neutral_native_periodic_pi_pole.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/FOUR_COLUMN_FINAL_REVIEW.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/INDEPENDENT_COLUMN_SOURCE_ALL_LENGTH.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/INDEPENDENT_FOUR_COLUMN_CHARGES.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/INDEPENDENT_FOUR_COLUMN_COEFFICIENT.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/INDEPENDENT_FOUR_COLUMN_DROPLET.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/INDEPENDENT_FOUR_COLUMN_QUOTIENT.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/column_four_results/PROVENANCE.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/column_four_results/neutral_four_column_5x5.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/column_four_results/neutral_four_column_5x6.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/column_four_results/neutral_four_column_6x6.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/column_four_results/neutral_four_column_charges_5x5.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/column_four_results/neutral_four_column_charges_5x6.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/column_four_results/neutral_four_column_droplet.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/column_four_results/neutral_four_column_momentum_5x5_t0.8889.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/column_four_results/neutral_four_column_momentum_5x5_t4.0000.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/column_four_results/neutral_four_column_momentum_6x6_t0.8889.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/column_four_results/neutral_four_column_native.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/neutral_four_column_charges.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/neutral_four_column_droplet.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/neutral_four_column_model.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/neutral_four_column_model_v2.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/neutral_four_column_momentum.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/neutral_four_column_momentum_six.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9735/native/neutral_four_column_native.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/BULK_SEGMENT_FINAL_REVIEW.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/INDEPENDENT_BULK_AIRY.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/INDEPENDENT_BULK_CHANNEL.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/INDEPENDENT_BULK_DISPERSION.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/INDEPENDENT_BULK_SECOND.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/INDEPENDENT_BULK_SOURCE.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/INDEPENDENT_BULK_TENSION.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/neutral_bulk_dispersion_check.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/neutral_bulk_dispersion_check.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/neutral_bulk_resonance.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/neutral_bulk_resonance.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/neutral_bulk_resonance_dynamic.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/neutral_bulk_resonance_dynamic.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/neutral_bulk_second.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/neutral_bulk_second.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/neutral_bulk_source_check.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/neutral_bulk_source_check.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9736/native/neutral_bulk_tension_check.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/INDEPENDENT_AXIAL_TWO_CHANNEL.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/INDEPENDENT_CONFINED_FAST_STRIP.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/INDEPENDENT_COUPLED_STRIP.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/INDEPENDENT_FAST_SECOND.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/INDEPENDENT_SLOW_HOST.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/INDEPENDENT_SLOW_RESPONSE.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/INDEPENDENT_SLOW_SOURCE.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/REVIEW_SLOW_BULK_COMPOSITE.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_bulk_second_boundary.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_bulk_second_boundary.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_bulk_second_other.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_bulk_second_other.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_bulk_source_check.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_confined_fast_source.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_confined_fast_source.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_coupled_slow_pole.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_coupled_slow_pole.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_outgoing_host.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_slow_dispersion.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_slow_dispersion.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_slow_host.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_slow_host.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_slow_resonance.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_slow_resonance.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_slow_response.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_slow_response.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_slow_source_check.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9738/native/neutral_slow_source_check.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/INDEPENDENT_SLOW_FOURTH_DIAGONAL.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/INDEPENDENT_SLOW_FOURTH_KERNEL.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/INDEPENDENT_SLOW_PARITY.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/INDEPENDENT_SLOW_RESTRICTED_BOUND.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/INDEPENDENT_SLOW_SUPPORT.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/INDEPENDENT_SLOW_THIRD.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/REVIEW_SLOW_NATIVE_CONTROL.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/neutral_slow_fourth_diagonal.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/neutral_slow_fourth_diagonal.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/neutral_slow_fourth_kernel.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/neutral_slow_fourth_kernel.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/neutral_slow_fourth_kernel_y.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/neutral_slow_fourth_kernel_y.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/neutral_slow_fourth_local_independent.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/neutral_slow_fourth_local_independent.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/neutral_slow_third.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9740/native/neutral_slow_third.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/INDEPENDENT_CUBIC_RESPONSE.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/INDEPENDENT_CUBIC_SECTORS.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/INDEPENDENT_NATIVE_Q.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/INDEPENDENT_RECT_ENGINE.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/INDEPENDENT_RECT_TRANSLATIONS.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/INDEPENDENT_SPACEGROUP.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/REVIEW_CUBIC_NATIVE_RESPONSE.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/cubic_results/IDENTITIES.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/cubic_results/REPRODUCTION.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/cubic_results/neutral_cube_low_spectrum.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/cubic_results/neutral_cube_native_scalar.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/cubic_results/neutral_cube_probe.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/cubic_results/neutral_cube_response_check.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/cubic_results/neutral_cube_sectors.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/cubic_results/neutral_rect_data_ground.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/cubic_results/neutral_rect_data_observables.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/cubic_results/neutral_rect_data_original_source_rejected_nodes.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/cubic_results/neutral_rect_data_response_rejected_nodes.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/cubic_results/neutral_rect_spacegroup_data_low.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/cubic_results/neutral_rect_spacegroup_data_response.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/cubic_results/neutral_rect_spacegroup_data_response_before_Q_projection_fix.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_cube_low_spectrum.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_cube_map_independent.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_cube_model.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_cube_native_scalar.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_cube_probe.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_cube_response_check.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_cube_sectors.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_rect_ground.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_rect_independent_check.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_rect_model.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_rect_original_source.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_rect_response.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_rect_spacegroup.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_rect_spacegroup_response.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_spacegroup_check.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_spacegroup_model.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9743/native/neutral_translation_model.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/CORRECTED_FAST_SCHUR_PROOF.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/CORRECTED_FAST_STRIP_PROOF.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/INDEPENDENT_CORRECTED_FAST_HOST.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/INDEPENDENT_CORRECTED_FAST_SCHUR.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/INDEPENDENT_CORRECTED_FAST_STRIP.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/INDEPENDENT_NATIVE_K4_POLE.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/REVIEW_CORRECTED_FAST.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/neutral_corrected_coupled_slow_pole.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/neutral_corrected_coupled_slow_pole.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/neutral_corrected_fast_boundary.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/neutral_corrected_fast_boundary.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/neutral_corrected_fast_host.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/neutral_corrected_fast_host.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/neutral_corrected_strip_algebra.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/neutral_corrected_strip_algebra.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/neutral_native_order4_pole.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/neutral_native_order4_pole.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/neutral_outgoing_host.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9744/native/neutral_slow_host.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9745/native/INDEPENDENT_RECTANGLE_RANGE.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9745/native/INDEPENDENT_SIMPLE_LOOP.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9745/native/LOOP_INTERACTION_PRIOR_ART.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9745/native/REVIEW_LOOP_INTERACTION.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9745/native/neutral_rectangle_closed.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9745/native/neutral_rectangle_closed.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9745/native/neutral_rectangle_range.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9745/native/neutral_rectangle_range.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9745/native/neutral_simple_loop.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9745/native/neutral_simple_loop.py',
    'outputs/neutral_continuation_review_2026_10_18/pr9747/native/DRESSED_SOURCE_BOUND.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9747/native/INDEPENDENT_DRESSED_READOUT.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9747/native/INDEPENDENT_LOCAL_DYNAMICS.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9747/native/INDEPENDENT_LOCAL_NORMALFORM.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9747/native/REVIEW_LOCAL_NORMALFORM.md',
    'outputs/neutral_continuation_review_2026_10_18/pr9747/native/neutral_local_normalform.json',
    'outputs/neutral_continuation_review_2026_10_18/pr9747/native/neutral_local_normalform.py',
    'scripts/native_bulk_segment_resonance.py',
    'scripts/native_column_collective_mode.py',
    'scripts/native_column_plaquette_selection.py',
    'scripts/native_corrected_fast_strip.py',
    'scripts/native_derived_collective_interaction.py',
    'scripts/native_four_column_competition.py',
    'scripts/native_infrared_readout.py',
    'scripts/native_large_column_dynamics.py',
    'scripts/native_local_normal_form.py',
    'scripts/native_local_normalform.py',
    'scripts/native_loop_interaction.py',
    'scripts/native_neutral_domain_resonance.py',
    'scripts/native_scalar_band_local_proof.py',
    'scripts/native_slow_bulk_composite.py',
    'scripts/native_slow_composite_control.py',
    'scripts/native_zone_boundary_composite.py',
    'scripts/neutral_continuation_runtime_2026_10_18.py',
)
SOURCE_PACK=ROOT/'outputs/neutral_continuation_review_2026_10_18/pr9743/native'
EXEC=Execution(SOURCE_PACK,AUDIT_TIMEOUT_SEC)
PACK=EXEC.pack
"""Finite native qubit Hamiltonian controls; no empirical or bulk scalar claim."""
from pathlib import Path
import sys, json, hashlib
import numpy as np
from scipy.sparse.linalg import eigsh
sys.path.insert(0, str(PACK))
from neutral_rect_model import sector, op, mult
from neutral_spacegroup_model import translation_tables, orbits, orbit_op
from collections import defaultdict

def comm(a, b):
    out = defaultdict(float)
    for u in a:
        for v in b:
            x, z, c = mult(u, v)
            out[x, z] += c
            x, z, c = mult(v, u)
            out[x, z] -= c
    return [(x, z, c) for (x, z), c in out.items() if c]

def run():
    d = sector(2)
    W = np.zeros((256, d['dim']))
    for j in range(d['dim']):
        v = {d['solve'](j): 1.0}
        for x, z, p in d['all_generators']:
            out = dict(v)
            for s, c in v.items():
                out[s ^ x] = out.get(s ^ x, 0) + p * (-1) ** (s & z).bit_count() * c
            v = {s: c for s, c in out.items() if c}
        norm = sum((c * c for c in v.values())) ** 0.5
        for s, c in v.items():
            W[s, j] = c / norm
    physical = op(sum(d['physical_H'], []), 256)
    reduced = op(sum(d['H'], []), d['dim'])
    rng = np.random.default_rng(318)
    v = rng.normal(size=d['dim'])
    v /= np.linalg.norm(v)
    error = float(np.linalg.norm(physical @ (W @ v) - W @ (reduced @ v)))
    EXEC.check('P9743-C001 sampled physical action and full Gram', error < 1e-12 and np.linalg.norm(W.T @ W - np.eye(d['dim'])) < 1e-12)
    d = sector(3)
    T, R, C = translation_tables(d)
    data = orbits(d['dim'], T, R, C)
    H = orbit_op(sum(d['H'], []), data)
    E, V = eigsh(H, k=16, which='SA', tol=1e-12, ncv=40, v0=np.random.default_rng(319).normal(size=H.shape[0]))
    g = V[:, 0]
    ht = sum(d['H'], [])
    qt = []
    for a in d['H']:
        qt += comm(a, comm(ht, a))
    S = orbit_op(d['S'], data)
    Q = orbit_op(qt, data)
    B = orbit_op([(x, z, c * (1 if a == 2 else -0.5)) for a, terms in enumerate(d['H']) for x, z, c in terms], data)
    rows = []
    for name, O in [('S', S), ('Q', Q), ('B', B)]:
        src = O @ g
        mean = g @ src
        src -= mean * g
        weights = (V.T @ src) ** 2
        rows.append(dict(source=name, mean=float(mean), variance=float(src @ src), lines=[dict(gap=float(E[i] - E[0]), weight=float(weights[i]), residual=float(np.linalg.norm(H @ V[:, i] - E[i] * V[:, i]))) for i in range(1, len(E)) if weights[i] > 1e-08]))
    sline = min(rows[0]['lines'], key=lambda r: r['gap'])
    qline = min(rows[1]['lines'], key=lambda r: r['gap'])
    bline = min(rows[2]['lines'], key=lambda r: r['gap'])
    EXEC.check('P9743-C002 selected cube lowest eigenpair energy', abs(E[0] + 38.19164989239814) < 1e-09)
    EXEC.check('P9743-C003 finite S source line', abs(sline['gap'] - 3.763565915973) < 1e-08 and abs(sline['weight'] - 58.3365873118) < 1e-06)
    EXEC.check('P9743-C004 finite Q source line', abs(qline['gap'] - sline['gap']) < 1e-09 and abs(qline['weight'] - 7094.98109499) < 1e-05)
    EXEC.check('P9743-C005 finite B source line', abs(bline['gap'] - 1.423237955386) < 1e-08)
    EXEC.check('P9743-C006 selected line residuals', max((x['residual'] for row in rows for x in row['lines'])) < 1e-08)
    identities = json.loads((SOURCE_PACK / 'cubic_results/IDENTITIES.json').read_text())
    for name, digest in identities['source_sha256'].items():
        EXEC.check('P9743-C007 frozen producer identities', hashlib.sha256((SOURCE_PACK / name).read_bytes()).hexdigest() == digest)
    for name, digest in identities['result_sha256'].items():
        EXEC.check('P9743-C008 frozen large result identities', hashlib.sha256((SOURCE_PACK / 'cubic_results' / name).read_bytes()).hexdigest() == digest)
    result = dict(status='PASS', physical8site_sampled_vector_intertwiner_error=error, cube27_ground=float(E[0]), cube27_reduced_dimension=H.shape[0], responses=rows, frozen_large_results='SHA256 verified; not replayed by this short runner', scope='Supplied nativeH finite model development; physicalmeasurement, lightmass and thermodynamiclimit open')
    out = EXEC.root / 'aggregate.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
if __name__ == '__main__':
    run()

if __name__ == "__main__":
    EXEC.finish("Finite declared models and conditional analytical hypotheses only; full microscopic resonance and physical interpretation remain open.", required=())
