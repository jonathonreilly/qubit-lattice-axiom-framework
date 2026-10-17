#!/usr/bin/env python3
"""Finite corroboration controls for ten conditional analytical publications.

These checks do not certify contour estimates, continuum spectra, propagation,
physical realization, or all inherited proof premises. Analytical proofs control
those claims. Input hashes identify the summaries whose displayed identities and
ceilings are corroborated here; historical review labels confer no authority.
"""
import hashlib
import json
from pathlib import Path

AUDIT_TIMEOUT_SEC = 120
# Hashes below bind proof provenance; hashing is not proof verification.
AUDIT_INPUT_PATHS = (
    'docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/AUTONOMOUS_LOCAL_RECORD_FINITE_WINDOW_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/CRITICAL_PRODUCT_SOURCE_SPECTRAL_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/HOPPING_CONTROLLED_FINITE_OUTPUT_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/NOMINAL_BANDCENTER_CONVERTER_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/SLOW_OUTPUT_COMPLETE_STATE_ONSET_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/SLOW_OUTPUT_LOCAL_RECORD_FINITE_WINDOW_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/STRUCTURED_SOURCE_TOLERANCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/THREE_SITE_PRODUCT_SOURCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/UNIFORM_SLOW_OUTPUT_RESOURCE_FAMILY_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/WIDE_SLOW_OUTPUT_COMPLETE_STATE_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'outputs/attached_record_2026_10_17/COPY_VALIDATION.json',
    'outputs/attached_record_2026_10_17/INTEGRATION_REVIEW.md',
    'outputs/attached_record_2026_10_17/SOURCES.json',
    'outputs/attached_record_2026_10_17/VALIDATION.json',
    'outputs/attached_record_2026_10_17/citation_graph.log',
    'outputs/attached_record_2026_10_17/source_checks/autonomous_record_route/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/autonomous_record_route_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_bandwidth_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_bandwidth_extension/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_converter_composition/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_converter_composition_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_converter_endpoint/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_converter_endpoint_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_reference_measure_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_resources/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_resources_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_weighted_profile/ENDPOINT_ERRATUM_REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_weighted_profile/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/bandcenter_weighted_profile_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/output_lead_weight/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/output_lead_weight_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_alltime_composition/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_alltime_composition_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_alltime_composition_check/REVIEW_v1.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_emitter_bound/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_emitter_bound_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_kernel/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_kernel_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_outgoing_profile/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_outgoing_profile/PROPOSAL_v1.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_outgoing_profile_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_recovery_bound/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_recovery_bound/PROPOSAL_v1.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_recovery_sharp/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_recovery_sharp_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_seed_mass/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_attached_seed_mass_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_core_operator_difference/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_core_operator_difference_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_finite_herald_transfer/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_finite_herald_transfer/PROPOSAL_v1.md',
    'outputs/attached_record_2026_10_17/source_checks/record_finite_herald_transfer_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_center_inverse/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_center_inverse/RESULT.json',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_center_inverse/check.py',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_center_inverse_check/EVIDENCE.md',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_center_inverse_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_center_inverse_check/continuant_check.py',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_center_inverse_check/continuant_stdout.txt',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_closed_spectrum/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_gate_closed_spectrum_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_incoming_alltime/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_incoming_alltime_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_reference_outgoing_onset/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_reference_outgoing_onset_check/REVIEW.md',
    'outputs/attached_record_2026_10_17/source_checks/record_seed_matrix_mass/PROPOSAL.md',
    'outputs/attached_record_2026_10_17/source_checks/record_seed_matrix_mass_check/REVIEW.md',
    'outputs/bandcenter_converter_2026_10_17/AUTHOR_MECHANICAL_CHECK.json',
    'outputs/bandcenter_converter_2026_10_17/INTEGRATION_REVIEW.md',
    'outputs/bandcenter_converter_2026_10_17/SOURCES.json',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_bandwidth_check/REVIEW.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_bandwidth_extension/PROPOSAL.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_converter_composition/PROPOSAL.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_converter_composition_check/REVIEW.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_converter_endpoint/PROPOSAL.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_converter_endpoint_check/REVIEW.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_reference_measure_check/REVIEW.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_resources/PROPOSAL.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_resources_check/REVIEW.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_temporal_check/REVIEW.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_temporal_route/PROPOSAL.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_weighted_profile/ENDPOINT_ERRATUM_REVIEW.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_weighted_profile/PROPOSAL.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_weighted_profile_check/REVIEW.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_wide_temporal/PROPOSAL.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/bandcenter_wide_temporal_check/REVIEW.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/converter_finite_composition/PROPOSAL.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/converter_finite_composition_check/REVIEW.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/original_hopping_transfer/PROPOSAL.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/original_hopping_transfer_check/REVIEW.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/output_lead_weight/PROPOSAL.md',
    'outputs/bandcenter_converter_2026_10_17/source_checks/output_lead_weight_check/REVIEW.md',
    'outputs/critical_source_2026_10_17/INTEGRATION_REVIEW.md',
    'outputs/critical_source_2026_10_17/SOURCES.json',
    'outputs/critical_source_2026_10_17/source_checks/three_site_actual_attachment/PROPOSAL.md',
    'outputs/critical_source_2026_10_17/source_checks/three_site_actual_attachment_check/REVIEW.md',
    'outputs/critical_source_2026_10_17/source_checks/three_site_loaded_inverse/PROPOSAL.md',
    'outputs/critical_source_2026_10_17/source_checks/three_site_loaded_inverse_check/REVIEW.md',
    'outputs/critical_source_2026_10_17/source_checks/three_site_product_source/PROPOSAL.md',
    'outputs/critical_source_2026_10_17/source_checks/three_site_product_source_check/REVIEW.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_actual_attachment/PROPOSAL.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_actual_attachment_check/REVIEW.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_loaded_inverse/PROPOSAL.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_loaded_inverse_check/REVIEW.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_loaded_mass/PROPOSAL.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_loaded_mass_check/REVIEW.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_product_source/PROPOSAL.md',
    'outputs/critical_source_2026_10_17/source_checks/two_site_product_source_check/REVIEW.md',
    'outputs/hopping_finite_transfer_2026_10_17/AUTHOR_MECHANICAL_CHECK.json',
    'outputs/hopping_finite_transfer_2026_10_17/INTEGRATION_REVIEW.md',
    'outputs/hopping_finite_transfer_2026_10_17/SOURCE_MANIFEST.json',
    'outputs/hopping_finite_transfer_2026_10_17/source_checks/bandcenter_resources/PROPOSAL.md',
    'outputs/hopping_finite_transfer_2026_10_17/source_checks/bandcenter_resources_check/REVIEW.md',
    'outputs/hopping_finite_transfer_2026_10_17/source_checks/hopping_only_finite_transfer/PROPOSAL.md',
    'outputs/hopping_finite_transfer_2026_10_17/source_checks/hopping_only_finite_transfer/PROPOSAL_v1.md',
    'outputs/hopping_finite_transfer_2026_10_17/source_checks/hopping_only_finite_transfer_check/REVIEW.md',
    'outputs/hopping_finite_transfer_2026_10_17/source_checks/hopping_only_finite_transfer_check/REVIEW_v1.md',
    'outputs/hopping_finite_transfer_2026_10_17/source_checks/original_hopping_transfer/PROPOSAL.md',
    'outputs/hopping_finite_transfer_2026_10_17/source_checks/original_hopping_transfer_check/REVIEW.md',
    'outputs/hopping_finite_transfer_2026_10_17/source_checks/output_lead_weight/PROPOSAL.md',
    'outputs/hopping_finite_transfer_2026_10_17/source_checks/output_lead_weight_check/REVIEW.md',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/CANONICAL_RESULT.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/EXECUTION_REVIEW.md',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/INTEGRATION_REVIEW.md',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/MUTATION_SUMMARY.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/RESOURCE_PLAN.md',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/canonical/PRELAUNCH.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/canonical/RESULT.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/canonical/stderr.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/canonical/stdout.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_closed_powers/PRELAUNCH.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_closed_powers/RESULT.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_closed_powers/stderr.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_closed_powers/stdout.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_endpoint_shift/PRELAUNCH.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_endpoint_shift/RESULT.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_endpoint_shift/stderr.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_endpoint_shift/stdout.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_excess_strip/PRELAUNCH.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_excess_strip/RESULT.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_excess_strip/stderr.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_excess_strip/stdout.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_finite_length/PRELAUNCH.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_finite_length/RESULT.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_finite_length/stderr.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_finite_length/stdout.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_projected_forcing/PRELAUNCH.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_projected_forcing/RESULT.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_projected_forcing/stderr.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_projected_forcing/stdout.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_short_time/PRELAUNCH.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_short_time/RESULT.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_short_time/stderr.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_short_time/stdout.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_side_budget/PRELAUNCH.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_side_budget/RESULT.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_side_budget/stderr.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_side_budget/stdout.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_whole_core_forcing/PRELAUNCH.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_whole_core_forcing/RESULT.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_whole_core_forcing/stderr.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/mutation_whole_core_forcing/stdout.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_endpoint_forcing_validation/run_validation.py.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/ARTIFACT_MANIFEST.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/endpoint_forcing/APPENDIX.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/endpoint_forcing/ARITHMETIC_BLOCK.py.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/endpoint_forcing/CHECK_MAP.md',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/endpoint_forcing/PROPOSAL.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/endpoint_forcing/REVIEW.md.txt',
    'outputs/slow_complete_2026_10_17/INTEGRATION_REVIEW.md',
    'outputs/slow_complete_2026_10_17/SOURCES.json',
    'outputs/slow_complete_2026_10_17/VALIDATION.json',
    'outputs/slow_complete_2026_10_17/citation_graph.log',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_background_derivative/PROPOSAL.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_background_derivative_check/REVIEW.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_complete_onset_frontier/PROPOSAL.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_complete_onset_frontier_check/REVIEW.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_complete_quantitative/PROPOSAL.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_complete_quantitative_check/REVIEW.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_direct_forcing_refinement/PROPOSAL.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_direct_forcing_refinement_check/REVIEW.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_forced_derivative_sharp/PROPOSAL.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_forced_derivative_sharp_check/REVIEW.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_incoming_late/PROPOSAL.md',
    'outputs/slow_complete_2026_10_17/source_checks/slow_lead_incoming_late_check/REVIEW.md',
    'outputs/slow_family_2026_10_17/COPY_VALIDATION.json',
    'outputs/slow_family_2026_10_17/INTEGRATION_REVIEW.md',
    'outputs/slow_family_2026_10_17/SOURCES.json',
    'outputs/slow_family_2026_10_17/VALIDATION.json',
    'outputs/slow_family_2026_10_17/citation_graph.log',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_coefficient_robustness/PROPOSAL.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_coefficient_robustness_check/REVIEW.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_family_example/PROPOSAL.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_family_example_check/REVIEW.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_fixed_dimensionless_scaling/PROPOSAL.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_fixed_dimensionless_scaling_check/REVIEW.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_composition/PROPOSAL.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_composition_check/REVIEW.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_endpoint/PROPOSAL.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_endpoint_check/REVIEW.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_reference/PROPOSAL.md',
    'outputs/slow_family_2026_10_17/source_checks/slow_lead_uniform_reference_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/COPY_VALIDATION.json',
    'outputs/slow_record_2026_10_17/INTEGRATION_REVIEW.md',
    'outputs/slow_record_2026_10_17/SOURCES.json',
    'outputs/slow_record_2026_10_17/VALIDATION.json',
    'outputs/slow_record_2026_10_17/citation_graph.log',
    'outputs/slow_record_2026_10_17/source_checks/same_carrier_slow_lead/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/same_carrier_slow_lead_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_alltime_composition/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_alltime_composition_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_emitter/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_emitter_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_gate_load/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_gate_load_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_outgoing_profile/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_outgoing_profile_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_recovery/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_recovery_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_reference_packet/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_reference_packet_check/REVIEW.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_resources/PROPOSAL.md',
    'outputs/slow_record_2026_10_17/source_checks/slow_lead_resources_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/INTEGRATION_REVIEW.md',
    'outputs/slow_wide_2026_10_17/SOURCES.json',
    'outputs/slow_wide_2026_10_17/VALIDATION.json',
    'outputs/slow_wide_2026_10_17/citation_graph.log',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_centered_background/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_centered_background_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_complete/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_complete_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_derivative/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_derivative_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_endpoint/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_endpoint/PROPOSAL_v1.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_endpoint_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_outgoing/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_outgoing_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_reference/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_reference_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_seed_mass/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_seed_mass_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_sharp/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_sharp_check/REVIEW.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wider_receiver_band/PROPOSAL.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wider_receiver_band/PROPOSAL_v1.md',
    'outputs/slow_wide_2026_10_17/source_checks/slow_lead_wider_receiver_band_check/REVIEW.md',
    'outputs/source_tolerance_2026_10_17/INTEGRATION_REVIEW.md',
    'outputs/source_tolerance_2026_10_17/SOURCES.json',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_attachment__PROPOSAL.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_attachment_check__REVIEW.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_local_core__PROPOSAL.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_local_core_check__REVIEW.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_local_reference__PROPOSAL.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_local_reference_check__REVIEW.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_outgoing__PROPOSAL.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_perturbed_outgoing_check__REVIEW.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_positive_hopping_reexpression__PROPOSAL.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_positive_hopping_reexpression_check__REVIEW.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_source_robustness__PROPOSAL.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_source_robustness_check__REVIEW.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_source_tolerance_complete__PROPOSAL.md',
    'outputs/source_tolerance_2026_10_17/proofs/three_site_source_tolerance_complete_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/INTEGRATION_REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/SOURCES.json',
    'outputs/three_site_temporal_2026_10_17/proofs/prepared_core_composition_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/prepared_core_dwell_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/prepared_core_recovery__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_compact_receiver__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_compact_receiver_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_complete_candidate__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_complete_candidate_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_local_escape__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_local_escape_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_outgoing__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_outgoing_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_reference_tail__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_reference_time__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_reference_time_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_traveling_interface__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_traveling_interface_check__REVIEW.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_weighted_reference_time__PROPOSAL.md',
    'outputs/three_site_temporal_2026_10_17/proofs/three_site_weighted_reference_time_check__REVIEW.md',
)


def main():
    import mpmath as mp
    import sympy as s
    mp.mp.dps = 70
    records = []

    def check(pr, name, condition, detail=None):
        if not bool(condition):
            raise AssertionError(f'{pr}: {name}: {detail}')
        records.append({'pr': pr, 'check': name, 'detail': detail})

    def budget(pr, name, rows, ceiling):
        value = sum(map(s.Rational, rows))
        check(pr, name, value < s.Rational(ceiling), str(value))

    def equal(pr, name, lhs, rhs):
        delta = lhs-rhs
        ok = all(s.simplify(x)==0 for x in delta) if isinstance(delta, s.MatrixBase) else s.simplify(delta)==0
        check(pr, name, ok)

    def cut(pr, g, T, M, allowance):
        # Log comparison avoids underflow and never allocates M sites.
        log_bound = mp.log(mp.mpf('1.2'))-M+4*mp.mpf(g)*mp.mpf(T)*mp.sinh(1)
        check(pr, 'finite cut logarithmic ceiling', log_bound < mp.log(mp.mpf(allowance)), mp.nstr(log_bound, 25))

    J=mp.mpf('.030021107107032'); q0=mp.mpf('4.510351185997098')
    C0=(q0*q0-1)/(q0*q0+1); S0=2*q0/(q0*q0+1); j=J*(1-C0)
    check(9674,'calibrated j enclosure',mp.mpf('.0027')<j<mp.mpf('.003'))
    n=s.diag(0,1); I2=s.eye(2); I4=s.eye(4)
    nx=s.kronecker_product(n,I2); ny=s.kronecker_product(I2,n)
    X=s.zeros(4); X[1,2]=X[2,1]=1
    q,a,L,t,gamma=s.symbols('q a L t gamma',positive=True)
    phi=(s.exp(gamma*t)-1)/gamma
    equal(9673,'Duhamel integral including zero growth',s.limit(phi,gamma,0),t)
    equal(9673,'one oriented cut has norm q', (s.Matrix([[0,q],[0,0]]).T*s.Matrix([[0,q],[0,0]]))[1,1],q*q)
    # Compression onto a blank outside qubit retains the inside occupation.
    Q=q*(nx+ny-X)
    equal(9673,'exact blank-site cap compression',Q.extract([0,2],[0,2]),q*n)
    check(9673,'output-ray prefactor',mp.e/(2*mp.sinh(1))<mp.mpf('1.2'))
    cut(9673,str(J),'3e17',60000000000000000,'1e-3')
    tau,jj=s.symbols('tau j',positive=True)
    converter=tau*(nx+ny-X)+(tau-jj)*(2*I4-nx-ny)
    equal(9674,'full-space converter vacancy identity',converter,2*(tau-jj)*I4+jj*(nx+ny)-tau*X)
    tc=mp.sqrt(j*J*S0)
    check(9674,'converter vacancy positive',tc>j)
    tt=mp.mpf('1e17'); ss=mp.mpf('.0053')*tt-64
    eloc=mp.mpf('1.26e13')*mp.exp(-mp.mpf('5.3e-16')*tt)+mp.mpf('1.21e11')/tt
    qin=mp.mpf('.003')*mp.exp(-mp.mpf('2e-6')*ss)+mp.mpf('.75')/mp.sqrt(ss)
    qm=mp.mpf('1.5e6')*mp.exp(-ss/mp.mpf('3.6e11'))+mp.mpf('.75')/mp.sqrt(ss)
    check(9674,'displayed all-time envelope at onset',mp.mpf('.001512')+eloc+qin+qm**2<mp.mpf('.001514'))
    cut(9674,str(j),'1e17',1500000000000000,'1e-6')

    # Exact rational noncommuting resolvent test: no simultaneous diagonalization.
    D=s.Matrix([[4,1],[1,6]]); Gp=s.Matrix([[1,2],[3,-1]])/11; Gm=s.Matrix([[2,-1],[4,1]])/13
    k=s.Rational(1,7); Tp=(D-k*k*Gp).inv(); Tm=(D-k*k*Gm).inv()
    Lp=s.Matrix([[1,2],[0,3],[2,-1]]); Lm=s.Matrix([[2,0],[1,4],[-1,2]])
    check(9675,'test genuinely noncommuting',D*Gp!=Gp*D)
    equal(9675,'ordered emitter resolvent difference',Tp-Tm,k*k*Tp*(Gp-Gm)*Tm)
    equal(9675,'ordered recovered-column difference',-k*Lp*Tp+k*Lm*Tm,-k*(Lp-Lm)*Tm-k**3*Lp*Tp*(Gp-Gm)*Tm)
    budget(9675,'record branch composition',['.001057','.00216','.00105','.000005'],'.0045')
    check(9675,'finite success consequence',(s.Rational('.9999994')-s.Rational('.004501'))**2>s.Rational('.991'))

    g=mp.mpf('1e-6'); ts=mp.sqrt(j*g)
    check(9676,'slow-interface positive occupations',min(j-ts,2*j-ts-g,2*(j-g))>0)
    equal(9676,'one-site receiver cap diagonal',s.Symbol('tau')+(2*jj-s.Symbol('tau')-s.Symbol('g'))+s.Symbol('g'),2*jj)
    # Scalar interface flux conservation away from center; both physical momenta.
    for offset in ['-.000003','0','.000003']:
        qq=mp.pi/2+mp.mpf(offset); kk=mp.acos(j*mp.cos(qq)/g)
        w=mp.exp(1j*qq); v=mp.exp(1j*kk)
        rr=(w-v)/(v-1/w); tl=mp.sqrt(j/g)*v*(1+rr)
        tf=mp.sqrt(g*mp.sin(kk)/(j*mp.sin(qq)))*tl
        check(9676,'interface flux conservation '+offset,abs(abs(rr)**2+abs(tf)**2-1)<mp.mpf('1e-60'))
    budget(9676,'all-time branch budget',['.00129','.000410','.0016','.000082'],'.0034')
    check(9676,'finite success',(mp.mpf('.9999984')-mp.mpf('.003401'))**2>mp.mpf('.9932'))
    check(9676,'complete branch-derived ceiling',mp.sqrt(2*(1-mp.mpf('.9999984')+mp.mpf('.003401')))<mp.mpf('.083'))
    cut(9676,'1e-6','1e15',5000000000,'1e-6')

    # Independent positive quadrature for the exact reference mass. The change
    # tan(u)=alpha*x resolves the extremely narrow Lorentzian core.
    kap=mp.mpf('1e-8'); h=mp.mpf('4e-6'); gam=kap**2/j; A=2*j-gam; alpha=gam/A
    xmax=mp.tan(h)/alpha
    pformula=4*kap**2/(mp.pi*A*A*(1-alpha*alpha))*(mp.atan(xmax)/alpha-h)
    integrand=lambda x:4*kap**2/(mp.pi*A*A*alpha)/((1+x*x)*(1+alpha*alpha*x*x))
    pquad=mp.quad(integrand,[0,1,10,100,1000,xmax])
    check(9677,'positive quadrature versus exact reference mass',abs(pquad-pformula)<mp.mpf('1e-55'))
    check(9677,'reference mass interval',0<pformula<1)
    H0=mp.mpf('1e6'); LL=mp.mpf('1e8'); kap0=mp.mpf('1e-10'); gam0=kap0**2/j
    g0=mp.mpf('1e-12')/j; h0=mp.asin(mp.mpf('1e-14')/(2*j*j)); T0=40/gam0
    for aa in map(mp.mpf,['1','.5','.01']):
        ga=(aa*kap0)**2/j; gg=aa*aa*g0; hh=mp.asin(aa*aa*mp.sin(h0)); TT=T0/(aa*aa)
        check(9677,'fixed dimensionless scaling '+str(aa),max(abs(2*j*mp.sin(hh)/ga-H0),abs(gg/ga-LL),abs(ga*TT-40),abs(gg*TT-g0*T0))<mp.mpf('1e-50'))
    budget(9677,'common family envelope',['.000905','.0000041','.001095','.0000236','.000000001'],'.00204')
    check(9677,'family success consequence',(s.Rational('.9999993')-s.Rational('.00204'))**2>s.Rational('.9959'))

    budget(9678,'first complete onset budget',['.00190588324','.0000016','.000001'],'.00191')
    budget(9678,'second complete onset budget',['.003194071','.000110','.000001'],'.00331')
    for eps,success,normalized in [('.00191','.9999963519','.001912'),('.00331','.9999890439','.003316')]:
        ee=mp.mpf(eps)
        check(9678,'complete metric consequence '+eps,abs((1-ee*ee)-mp.mpf(success))<mp.mpf('1e-60') and ee+1-mp.sqrt(1-ee*ee)<mp.mpf(normalized))
    cut(9678,'1e-6','3e14',1500000000,'1e-6')
    x,z,delta=s.symbols('x z delta')
    equal(9679,'scalar centered resolvent remainder',1/(delta-x-z)-1/(delta-x),z/(delta-x)**2+z*z/((delta-x)**2*(delta-x-z)))
    dg=mp.mpf('1.00068')*(mp.mpf('6.47e17')+mp.mpf('3.31e7')/mp.mpf('5e-8'))+3600
    check(9679,'wide derivative arithmetic',dg<mp.mpf('6.49e17'))
    budget(9679,'wide complete budget',['.00125','.000011781','.000250','.000394','.00000022','.00000062','.000001'],'.00191')
    cut(9679,'5e-8','1e15',250000000,'1e-6')

    # Source chain includes an arbitrary downstream diagonal and edge: neither
    # enters its third power on the seed. The port-reaching term is retained.
    a1,a2,kk,b,c=s.symbols('a1 a2 kappa b c',real=True)
    H=s.zeros(5)
    for u,v,amp in [(0,1,a1),(1,2,a2),(2,3,kk),(3,4,c)]: H[u,v]=H[v,u]=-amp
    H[3,3]=b; H[4,4]=3*b
    seed=s.eye(5)[:,0]; v3=H**3*seed
    equal(9680,'installed third power',v3,s.Matrix([0,-a1*(a1*a1+a2*a2),0,-a1*a2*kk,0]))
    mu=a1*a1*(a1*a1+a2*a2)**2+a1*a1*a2*a2*kk*kk
    equal(9680,'installed sixth moment', (v3.T*v3)[0],mu)
    lam,jj=s.symbols('lambda j',positive=True)
    equal(9680,'nominal sixth moment',mu.subs({a1:lam/s.sqrt(3),a2:lam*s.sqrt(s.Rational(8,3)),kk:s.sqrt(3*jj*lam)}),3*lam**6+s.Rational(8,3)*jj*lam**5)
    aa=s.Rational(1,3); bb=s.Rational(2,5); cc=s.Rational(1,7); A2=D-cc**2*Gp
    Q2=(D**2-aa**2*s.eye(2))*A2-bb**2*D
    S=D.row_join(aa*s.eye(2)).row_join(s.zeros(2)); S=S.col_join((aa*s.eye(2)).row_join(D).row_join(bb*s.eye(2))); S=S.col_join(s.zeros(2).row_join(bb*s.eye(2)).row_join(A2))
    col=((D*A2-bb**2*s.eye(2))*Q2.inv()).col_join(-aa*A2*Q2.inv()).col_join(aa*bb*Q2.inv())
    equal(9680,'noncommuting three-source inverse column',S*col,s.eye(2).col_join(s.zeros(4,2)))
    y=s.symbols('y',real=True)
    equal(9680,'cubic conditioning polynomial',(1+y*y)**3-9*(y*y-s.Rational(1,3))**2,y*y*(y*y-3)**2)
    check(9680,'spectral tail squared enclosure',s.Rational('1.600000006e-57')<s.Rational('4.1e-6')**2*s.Rational('2.15e-8')**6)
    budget(9681,'larger complete budget',['4.1e-11','.000003','.000505','.0000216','.0000691','2.46e-9','1e-8'],'.0006')
    budget(9681,'compact complete budget',['.0000051','.000119','.000506','.001074','.000016','4e-9','1e-9'],'.001722')
    cut(9681,'5e-8','2e14',50000000,'1e-8'); cut(9681,'1e-9','2e14',1000000,'1e-9')

    # Full four-head 16-dimensional identities, including zero/multiple heads.
    ns=[]; xs=[]
    for site in range(4): ns.append(s.kronecker_product(*[n if i==site else I2 for i in range(4)]))
    for u,v in [(0,1),(1,2),(2,3)]:
        xx=s.zeros(16)
        for state in range(16):
            if ((state>>u)&1)!=((state>>v)&1): xx[state,state^(1<<u)^(1<<v)]=1
        # Bits here run opposite the Kronecker indices; map occupations likewise.
        xs.append(xx)
    ns=list(reversed(ns)); ident=s.eye(16); d0,d1,d2=s.symbols('d0 d1 d2',real=True)
    old=jj*(ns[2]+ns[3])-kk*xs[2]+a2*(ns[1]+ns[2]-xs[1])+a1*(ns[0]+ns[1]-xs[0])+(jj+d2-a2)*ns[2]+(2*jj+d1-a1-a2)*ns[1]+(2*jj+d0-a1)*ns[0]
    new=kk*(ident-xs[2])+a2*(ident-xs[1])+a1*(ident-xs[0])+jj*ns[3]+(2*jj+d2)*ns[2]+(2*jj+d1)*ns[1]+(2*jj+d0)*ns[0]
    equal(9683,'full-space seven-block scalar identity',new-old,(kk+a1+a2)*ident)
    check(9683,'positive pair spectrum',(I4-X).eigenvals()=={s.Integer(0):1,s.Integer(1):2,s.Integer(2):1})
    budget(9683,'structured tolerance complete budget',['4.1e-11','.000082','.000505','.0000285','.00004301','3.1e-7','3e-12','1e-10'],'.000660')
    cut(9683,'5e-8','2e14',50000000,'1e-10')
    root=Path(__file__).resolve().parents[1]
    inputs={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
    print(json.dumps({'status':'PASS','scope':'finite corroboration only; analytical proof obligations remain controlling', 'checks':records,'input_sha256':inputs},indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
