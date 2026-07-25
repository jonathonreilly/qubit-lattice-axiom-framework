#!/usr/bin/env python3
"""Adversarial boundary checks for the owned-seam execution ladder.

The component baselines are direct-ROM commit 315788cd7e and routed-transition
commit 483b24693e.  The successor checks cover the actual common-E direct and
finite gauge-corrected words, fixed-interface commit 928eeb641d, and literal
decoded-interface commit bc377db727.  The finite positives are kept distinct
from the remaining recurrent/no-preferred-order and physical-binding gaps.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
import inspect
import json
from pathlib import Path

import numpy as np
from scipy import sparse

import frontier_owned_seam_carrier_givens_refresh_2026_07_25 as direct_rom
import frontier_common_e_ordered_physical_rom_composition_2026_07_25 as common_direct
import frontier_common_e_gauge_corrected_physical_rom_composition_2026_07_25 as common_gauge
import frontier_two_star_fixed_register_local_executor_2026_07_25 as fixed
import frontier_two_star_literal_m2_reachable_executor_2026_07_25 as literal
import frontier_two_star_literal_m2_deletion_domain_2026_07_25 as literal_delete
import frontier_two_star_routed_transition_physical_word_2026_07_25 as routed


TOL = 1.0e-10
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def direct_descriptor_audit():
    """Capture the direct runner's descriptor/control dictionaries at L=5."""

    instances = []
    ordinary = direct_rom.defaultdict

    class CapturingDefaultDict(defaultdict):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            instances.append(self)

    direct_rom.defaultdict = CapturingDefaultDict
    try:
        result = direct_rom.physical_two_level_primitive_audit(5)
    finally:
        direct_rom.defaultdict = ordinary
    large = [row for row in instances if len(row) == result["distinct_controlled_two_level_rows"]]
    descriptors = next(
        row for row in large if len(next(iter(next(iter(row.values()))))) == 4
    )
    coefficients = next(
        row
        for row in large
        if len(next(iter(next(iter(row.values()))))) == 5
        and isinstance(next(iter(next(iter(row.values()))))[0], str)
    )
    observation_rows = next(
        row
        for row in large
        if len(next(iter(next(iter(row.values()))))) == 5
        and isinstance(next(iter(next(iter(row.values()))))[0], tuple)
    )
    if len(descriptors) != result["distinct_controlled_two_level_rows"]:
        raise AssertionError((len(descriptors), result))
    return result, descriptors, coefficients, observation_rows


def direct_route_checks() -> dict[str, object]:
    primitive, descriptors, coefficient_rows, observation_rows = direct_descriptor_audit()
    held_primitive = direct_rom.physical_two_level_primitive_audit(6)
    physical_directed = defaultdict(set)
    physical_directed_with_hidden_pairs = defaultdict(set)
    physical_unordered = defaultdict(set)
    source_fan = defaultdict(set)
    descriptor_value_widths = set()
    for (owner, source_observation, source_pair, target_pair), values in descriptors.items():
        if len(values) != 1:
            continue
        target_observation, phase, x_word, z_word = next(iter(values))
        descriptor_value_widths.add(len(next(iter(values))))
        physical_key = (owner, source_observation, target_observation)
        physical_directed[physical_key].add((phase, x_word, z_word))
        physical_directed_with_hidden_pairs[physical_key].add(
            (source_pair, target_pair, phase, x_word, z_word)
        )
        physical_unordered[
            (owner, tuple(sorted((source_observation, target_observation))))
        ].add((source_pair, target_pair, phase, x_word, z_word))
        source_fan[(owner, source_observation)].add(
            (target_observation, target_pair, phase, x_word, z_word)
        )

    physically_rekeyed_conflicts = sum(
        len(values) > 1 for values in physical_directed.values()
    )
    hidden_pair_variants = sum(
        len(values) > 1 for values in physical_directed_with_hidden_pairs.values()
    )
    overpaired_unordered_rows = sum(
        len(values) > 2 for values in physical_unordered.values()
    )
    check(
        "direct-ROM descriptors remain conflict-free after hidden ray-pair keys are removed",
        len(descriptors) == 46306
        and len(physical_directed) == 46306
        and physically_rekeyed_conflicts == 0
        and hidden_pair_variants == 0
        and len(physical_unordered) == 23153
        and overpaired_unordered_rows == 0
        and primitive["observation_only_control_conflicts"] == 0
        and primitive["observation_only_control_rows"] == 46306,
        {
            "directed_rows": len(physical_directed),
            "physically_rekeyed_conflicts": physically_rekeyed_conflicts,
            "hidden_pair_variants": hidden_pair_variants,
            "unordered_reverse_pairs": len(physical_unordered),
        },
    )

    primitive_source = inspect.getsource(direct_rom.physical_two_level_primitive_audit)
    action_counts = Counter()
    coefficient_unitarity = 0.0
    for key, values in coefficient_rows.items():
        if len(values) != 1:
            continue
        action, _stage, cosine, sine_real, sine_imag = next(iter(values))
        action_counts[action] += 1
        coefficient_unitarity = max(
            coefficient_unitarity,
            abs(cosine * cosine + sine_real * sine_real + sine_imag * sine_imag - 1.0),
        )
    check(
        "direct-ROM coefficient, action and stage association is complete",
        descriptor_value_widths == {4}
        and len(coefficient_rows) == 46306
        and len(observation_rows) == 46306
        and all(len(values) == 1 for values in coefficient_rows.values())
        and primitive["coefficient_association_conflicts"] == 0
        and primitive["descriptors_without_coefficients"] == 0
        and set(action_counts)
        == {"left_carrier_givens", "right_carrier_givens", "occupation_FSWAP"}
        and coefficient_unitarity < TOL
        and "givens_factors" in primitive_source
        and "coefficient_associations" in primitive_source,
        {
            "associated_rows": len(coefficient_rows),
            "action_counts": dict(action_counts),
            "maximum_coefficient_unitarity_residual": coefficient_unitarity,
            "coefficient_conflicts": primitive["coefficient_association_conflicts"],
            "missing_coefficients": primitive["descriptors_without_coefficients"],
        },
    )

    direct_path = Path(direct_rom.__file__)
    direct_source = direct_path.read_text(encoding="utf-8")
    composition_source = inspect.getsource(direct_rom.composed_update_controls)
    check(
        "direct-ROM physical rows now carry bounded coarse diameter and owner radius",
        primitive["maximum_coarse_L1_diameter"] == 3
        and held_primitive["maximum_coarse_L1_diameter"] == 3
        and primitive["maximum_owner_coarse_L1_radius"] == 1
        and held_primitive["maximum_owner_coarse_L1_radius"] == 1
        and "support_coarse_cells" in primitive_source
        and "periodic_l1" in primitive_source,
        {
            "L5_diameter_radius": (
                primitive["maximum_coarse_L1_diameter"],
                primitive["maximum_owner_coarse_L1_radius"],
            ),
            "L6_diameter_radius": (
                held_primitive["maximum_coarse_L1_diameter"],
                held_primitive["maximum_owner_coarse_L1_radius"],
            ),
        },
    )

    translations = tuple(
        direct_rom.translated_two_star_fixture_control(length) for length in (5, 6)
    )
    check(
        "the finite direct ROM is hash-inventoried and translation-audited",
        primitive["finite_control_ROM_retained"]
        and held_primitive["finite_control_ROM_retained"]
        and len(primitive["finite_rotation_ROM_sha256"]) == 64
        and len(held_primitive["finite_rotation_ROM_sha256"]) == 64
        and primitive["diagonal_collision_phase_rows"] == 11
        and held_primitive["diagonal_collision_phase_rows"] == 11
        and all(row["all_torus_translations_tested"] for row in translations)
        and all(row["translation_chart_ambiguities"] == 0 for row in translations)
        and all(row["translation_carrier_coefficient_mismatches"] == 0 for row in translations)
        and "rom_rows" in primitive_source
        and "rom_sha256" in primitive_source,
        {
            "rows": (primitive["observation_only_control_rows"], held_primitive["observation_only_control_rows"]),
            "ROM_sha256": (
                primitive["finite_rotation_ROM_sha256"],
                held_primitive["finite_rotation_ROM_sha256"],
            ),
            "translated_owner_fixtures": tuple(
                row["translated_owner_fixtures"] for row in translations
            ),
        },
    )

    check(
        "the 315 direct-ROM baseline stops at a composition bound and finite translation audit",
        "11 * maximum_local_intertwiner" in composition_source
        and "11 * maximum_local_leakage" in composition_source
        and "physical_two_level_primitive_audit" not in composition_source
        and not primitive["translation_invariant_recurrent_law_derived"]
        and not held_primitive["translation_invariant_recurrent_law_derived"]
        and not primitive["recurrent_volume_update_claimed"]
        and not held_primitive["recurrent_volume_update_claimed"],
        {
            "baseline_commit": "315788cd7e",
            "common_physical_product_applied": False,
            "reported_composition": "11*max(local residual)",
            "finite_ROMs_are_volume_specific": (
                primitive["finite_rotation_ROM_sha256"]
                != held_primitive["finite_rotation_ROM_sha256"]
            ),
            "recurrent_law_derived": False,
        },
    )
    return {
        "exact_baseline_commit": "315788cd7e",
        "descriptor_rows": len(descriptors),
        "physical_rekey_conflicts": physically_rekeyed_conflicts,
        "coefficient_association_executed": True,
        "observation_only_control_rows_supplied": True,
        "geometric_diameter_measured": True,
        "finite_ROM_hash_inventoried": True,
        "all_torus_translations_tested": True,
        "common_all_eleven_operator_executed_in_this_baseline": False,
        "translation_invariant_recurrent_law_derived": False,
        "source_contains_old_decoder_tautology": "0 ^ decoded ^ decoded" in direct_source,
        "candidate_sha256": sha256(direct_path.read_bytes()).hexdigest(),
    }


def sparse_route_checks() -> dict[str, object]:
    routing = routed.routing_truth_tables()
    physical = routed.full_word_certificate()
    check(
        "sparse route executes the 224-CZ transition and safely reuses dirty transit M2",
        routing["distance_two_terms"] == 77
        and routing["route_basis_cases_including_dirty_transit"] == 616
        and routing["routed_data_return_failures"] == 0
        and routing["routed_transit_return_failures"] == 0
        and routing["routed_phase_failures"] == 0
        and physical["transition_terms"] == 224
        and physical["physical_factor_counts"] == {"CZ": 224, "SWAP": 154}
        and physical["n_le_2_dirty_transit_integration_cases"] == 10516
        and physical["transition_work_return_failures"] == 0,
        {
            "remote_macros": routing["distance_two_terms"],
            "dirty_macro_cases": routing["route_basis_cases_including_dirty_transit"],
            "full_word_dirty_cases": physical["n_le_2_dirty_transit_integration_cases"],
            "factors": physical["physical_factor_counts"],
        },
    )

    gate_rows, candidate_stream, transition, seam_gates = routed.decoded_gate_product()
    target_stream = routed.route_c.patch_stream(
        routed.route_c.BASE_CELLS, routed.route_c.BASE_EDGES
    )
    before = candidate_stream @ transition - target_stream
    after = transition @ candidate_stream - target_stream
    after_mismatch_columns = sum(
        after.getcol(column).nnz > 0 for column in range(after.shape[1])
    )
    check(
        "sparse transition order is genuinely fixed before the signed seam product",
        before.nnz == 0
        and after_mismatch_columns == 100
        and routed.raw_maximum(after) == 2.0,
        {
            "transition_before_seams_raw": routed.raw_maximum(before),
            "transition_after_seams_mismatch_columns": after_mismatch_columns,
            "transition_after_seams_raw": routed.raw_maximum(after),
        },
    )

    square_row = routed.square_decoded_certificate(
        5, gate_rows, candidate_stream, transition, seam_gates
    )
    check(
        "sparse repair is algebraically square/unitary and closes on the same finite E",
        square_row["U_decoded_ambient_shape"] == (125749, 125749)
        and square_row["U_decoded_ambient_unitarity_raw_maximum"] < TOL
        and square_row["intertwiner_raw_maximum"] < TOL
        and square_row["intertwiner_opnorm"] < TOL
        and square_row["code_leakage_raw_maximum"] < TOL
        and square_row["code_leakage_opnorm"] < TOL
        and gate_rows["ordered_seam_gates"] == 11
        and gate_rows["transition_CZ_gates"] == 224
        and gate_rows["corrected_product_vs_target_raw_maximum"] < TOL
        and gate_rows["routed_transition_corrected_mismatch_columns"] == 0,
        {
            "shape": square_row["U_decoded_ambient_shape"],
            "nonzeros": square_row["U_decoded_ambient_nonzeros"],
            "unitarity_raw": square_row[
                "U_decoded_ambient_unitarity_raw_maximum"
            ],
            "intertwiner_raw": square_row["intertwiner_raw_maximum"],
            "leakage_raw": square_row["code_leakage_raw_maximum"],
        },
    )

    block_counts = Counter(len(label) for label in routed.route_c.FOCK_BASIS)
    block_dimensions = {
        routed.packet_dimension(label) for label in routed.route_c.FOCK_BASIS
    }
    ambient_rows_from_blocks = sum(
        routed.packet_dimension(label) for label in routed.route_c.FOCK_BASIS
    )
    ambient_is_power_of_two = (
        ambient_rows_from_blocks > 0
        and ambient_rows_from_blocks & (ambient_rows_from_blocks - 1) == 0
    )
    ambient_source = inspect.getsource(routed.ambient_square_model)
    lift_source = inspect.getsource(routed.lift_logical_operand)
    check(
        "the square matrix is a global-label direct sum, not a fixed tensor-product M2 ambient",
        block_counts == Counter({2: 2556, 1: 72, 0: 1})
        and block_dimensions == {1, 7, 49}
        and ambient_rows_from_blocks == 125749
        and not ambient_is_power_of_two
        and "for column, label in enumerate(route_c.FOCK_BASIS)" in ambient_source
        and "sparse.block_diag(prepare_blocks" in ambient_source
        and "column = logical.getcol(source)" in lift_source
        and "target = int(column.indices[0])" in lift_source
        and "offsets[target] + packet" in lift_source,
        {
            "global_label_counts": dict(sorted(block_counts.items())),
            "label_conditioned_block_dimensions": sorted(block_dimensions),
            "direct_sum_dimension": ambient_rows_from_blocks,
            "power_of_two_dimension": ambient_is_power_of_two,
            "local_M2_tensor_factorization_executed": False,
        },
    )

    decoded_source = inspect.getsource(routed.decoded_gate_product)
    square_source = inspect.getsource(routed.square_decoded_certificate)
    same_e_source = inspect.getsource(routed.same_encoding_certificate)
    check(
        "the candidate is independent but the transition discloses offline target synthesis",
        "candidate = sparse.eye" in decoded_source
        and decoded_source.index("candidate = sparse.eye")
        < decoded_source.index("target_stream = route_c.patch_stream")
        and "decoded_ambient = (prepare @ decoded_correct @ unprepare).tocsc()"
        in square_source
        and "expected = encoding @ target_contact" in square_source
        and "target_contact" not in square_source.split(
            "decoded_ambient = (prepare @ decoded_correct @ unprepare).tocsc()"
        )[1].split("wrong_decoded =", maxsplit=1)[0]
        and "_target_update" in same_e_source
        and "square_decoded_certificate" in same_e_source
        and not gate_rows["candidate_target_derived"]
        and gate_rows["transition_synthesized_offline_from_target_inversion_set"],
        {
            "candidate_target_derived": gate_rows["candidate_target_derived"],
            "transition_synthesized_offline_from_target_inversion_set": gate_rows[
                "transition_synthesized_offline_from_target_inversion_set"
            ],
            "comparison_target_matrix_injected_as_runtime_operand": False,
            "prior_runtime_target_injection_defect": "closed",
        },
    )

    qutrit_position = square_source.index("qutrit = route_c.qutrit_module_controls()")
    physical_position = square_source.index(
        "decoded_ambient = (prepare @ decoded_correct @ unprepare).tocsc()"
    )
    check(
        "the square word lifts aggregate logical monomials instead of the declared local factors",
        len(square_row["stage_rows"]) == 14
        and "transition_lift = lift_logical_operand(transition, offsets)"
        in square_source
        and "seam_lifts = tuple(lift_logical_operand(gate, offsets)" in square_source
        and "contact_lift = lift_logical_operand(contact, offsets)" in square_source
        and "for term in ROUTED_TERMS" not in square_source
        and "execute_routed_term" not in square_source
        and "patch_coin" not in square_source
        and qutrit_position > physical_position,
        {
            "aggregate_transition_lifts": 1,
            "aggregate_seam_lifts": len(seam_gates),
            "aggregate_contact_lifts": 1,
            "routed_378_local_factors_applied_to_square_ambient": False,
            "qutrit_chart_XOR_matrix_operand_present": False,
            "physical_coin_operand_present": False,
            "physical_mass_operand_present": False,
        },
    )

    logical, target_update = routed.logical_composition_certificate()
    covariance = routed.covariance_certificate(target_update)
    covariance_source = inspect.getsource(routed.covariance_certificate)
    logical_covariance_source = inspect.getsource(
        routed.route_c.frame_and_translation_controls
    )
    deletion_source = inspect.getsource(routed.deletion_certificate)
    check(
        "24/576 and translation checks remain geometric/logical rather than square-word covariance",
        logical["routed_transition_stream_raw_maximum"] < TOL
        and covariance["proper_cubic_frames"] == 24
        and covariance["ordered_frame_products"] == 576
        and covariance["rotated_route_failures"] == 0
        and covariance["frame_product_word_failures"] == 0
        and "transform_word" in covariance_source
        and "frame_and_translation_controls" in covariance_source
        and "square_physical_certificate" not in covariance_source
        and "lift_logical_operand" not in covariance_source
        and "translation_rows" in logical_covariance_source
        and "translated_cells" in logical_covariance_source
        and "physical" not in logical_covariance_source
        and "tuple(2.0 for _term in ROUTED_TERMS)" in deletion_source,
        {
            "proper_frames": covariance["proper_cubic_frames"],
            "frame_products": covariance["ordered_frame_products"],
            "physical_square_word_covariance_residual_present": False,
            "translated_square_operand_executed": False,
            "macro_deletion_residuals_are_literal": True,
        },
    )
    return {
        "transition_word_executed": True,
        "transition_order_closed": True,
        "dirty_transit_reuse_closed": True,
        "five_Givens_coefficient_provenance_executed": True,
        "abstract_direct_sum_square_unitary_executed": True,
        "same_finite_encoding_intertwiner_executed": True,
        "candidate_target_derived": False,
        "transition_synthesized_offline_from_target_inversion_set": True,
        "comparison_target_matrix_injected_as_runtime_operand": False,
        "fixed_tensor_product_M2_ambient_executed": False,
        "declared_local_factors_applied_to_square_ambient": False,
        "aggregate_global_label_seam_lifts_executed": True,
        "postword_shared_chart_preservation_executed": False,
        "physical_covariance_executed": False,
        "candidate_sha256": sha256(Path(routed.__file__).read_bytes()).hexdigest(),
    }


def fixed_register_route_checks() -> dict[str, object]:
    """Attack the hardened decoded-interface boundary at exact commit 928eeb641d."""

    registers = fixed.register_and_constraint_certificate()
    binding = fixed.source_identity_and_physical_binding()
    factors = fixed.factor_inventory(True)
    coin_unitarity = max(
        float(np.linalg.norm(gate.matrix.conj().T @ gate.matrix - np.eye(gate.matrix.shape[0])))
        for gate in fixed.COIN_GATES
    )
    check(
        "the fixed executor genuinely acts on 72 data bits and the supplied local coin matrices",
        registers["fixed_data_M2"] == 72
        and len(fixed.COIN_GATES) == 11
        and {len(gate.wires) for gate in fixed.COIN_GATES} == {1, 2}
        and coin_unitarity < TOL
        and factors["transition_synthesized_offline_from_target_inversion_set"],
        {
            "data_bits": registers["fixed_data_M2"],
            "coin_factors_per_cell": len(fixed.COIN_GATES),
            "maximum_coin_factor_unitarity_residual": coin_unitarity,
            "transition_synthesized_offline_from_target_inversion_set": True,
        },
    )

    stream = fixed.route_c.patch_stream(fixed.CELLS, fixed.EDGES)
    identity = sparse.eye(len(fixed.FOCK_BASIS), format="csc")
    column = next(
        index
        for index in range(len(fixed.FOCK_BASIS))
        if (stream.getcol(index) - identity.getcol(index)).nnz
    )
    source = fixed.encoded_column(fixed.FOCK_BASIS[column], 5, 0)
    observed, stages = fixed.execute_word(source, False)
    contact = fixed.route_c.patch_contact(fixed.CELLS)
    correct = fixed.encoded_logical_column(contact @ stream, column, 5, 0)
    wrong = fixed.encoded_logical_column(contact, column, 5, 0)
    correct_raw, correct_norm = fixed.state_difference(observed, correct)
    wrong_raw, wrong_norm = fixed.state_difference(observed, wrong)
    add_source = inspect.getsource(fixed.add_term)
    check(
        "the finite code-sector macro result is target-discriminating and collision-safe as a sparse map",
        correct_raw < TOL
        and correct_norm < TOL
        and wrong_raw > 0.4
        and wrong_norm > 1.4
        and all(fixed.chart_xor(fixed.chart_xor(key)) == key for key in source)
        and "output.get(key" in add_source
        and "del output[key]" in add_source
        and min(abs(value) for value in observed.values()) > 1e-3
        and stages["chart_after_erase_maximum"] == 0
        and stages["nonsentinel_role_rays_before_seams"] == 0
        and stages["dirty_work_rays_after_seams"] == 0,
        {
            "probe_column": column,
            "correct_target_residual": (correct_raw, correct_norm),
            "wrong_target_residual": (wrong_raw, wrong_norm),
            "minimum_observed_amplitude": min(abs(value) for value in observed.values()),
            "dict_collisions_accumulate_before_cancellation": True,
            "chart_XOR_is_involutive": True,
        },
    )

    role_source = inspect.getsource(fixed.role_refresh)
    executor_source = inspect.getsource(fixed.execute_word)
    carrier_sector_dimension = 7 ** len(fixed.CELLS)
    carrier_full_M2_dimension = 2 ** registers["fixed_carrier_rail_M2"]
    check(
        "the executed carrier/matcher word remains compressed to a host-selected one-hot macro",
        carrier_sector_dimension < carrier_full_M2_dimension
        and set(fixed.FixedBasis.__dataclass_fields__)
        == {"data", "roles", "charts", "matcher_work", "edge_work", "transit"}
        and "bypass" not in fixed.FixedBasis.__dataclass_fields__
        and "supplied = local_data_word(key, cell)" in role_source
        and "occupied = supplied.bit_length() - 1" in role_source
        and "matrix = routed.ROLE_GATE_MATRICES[occupied]" in role_source
        and "matcher_trace(" not in role_source
        and "apply_role_factor(" not in role_source
        and "matcher_work" not in role_source
        and registers["fixed_matcher_work_M2"] == 96
        and factors["fixed_schedule_macro_factors"][
            "controlled_two_rail_role_Givens"
        ] == 720,
        {
            "represented_carrier_sector_dimension": carrier_sector_dimension,
            "declared_seven_rail_M2_dimension": carrier_full_M2_dimension,
            "bypass_register_field_present": False,
            "matcher_or_bypass_operands_executed_in_role_refresh": False,
            "counted_controlled_role_factors": factors["fixed_schedule_macro_factors"][
                "controlled_two_rail_role_Givens"
            ],
            "executed_role_operation": "one host-selected 7x7 block per cell/stage",
        },
    )

    file_source = Path(fixed.__file__).read_text(encoding="utf-8")
    contact_source = inspect.getsource(fixed.apply_contact)
    seam_source = inspect.getsource(fixed.apply_seam)
    check(
        "the hardened successor accurately separates the decoded interface from its supplied physical binding",
        binding["executed_encoding_name"] == "E_fixed_decoded"
        and not binding["executed_encoding_equals_landed_E_refresh"]
        and binding["decoded_interface_M2_count"] == 323
        and binding["Cycle655_semantic_M2_per_cell"] == 61
        and binding["Cycle655_decoder_encoder_GF2_residual"] == 0
        and binding["bound_physical_fixture_M2_count"] == 983
        and not binding["Cycle655_binding_executed_end_to_end_in_this_runner"]
        and binding["physical_site_claim_requires_supplied_Cycle655_binding"]
        and not binding["new_axiom_or_primitive_claimed"],
        binding,
    )

    deletions = fixed.deletion_and_domain_certificate()
    check(
        "the successor adds active component deletion and local-domain witnesses",
        deletions["coin_deleted_factor_witnesses"] == 11
        and deletions["minimum_delete_coin_factor_residual"] > 0.05
        and deletions["transition_deleted_CZ_witnesses"] == 224
        and deletions["minimum_delete_transition_CZ_residual"] > 1.9
        and deletions["route_delete_first_SWAP_failed_cases"] > 0
        and deletions["route_delete_CZ_failed_cases"] > 0
        and deletions["route_delete_last_SWAP_failed_cases"] > 0
        and deletions["edge_role_phase_delete_witnesses"] == 11
        and deletions["delete_endpoint_seam_update_residual"] > 1.9
        and deletions["delete_contact_update_residual"] > 0.3
        and deletions["delete_carrier_Givens_residual"] > 0.4
        and deletions["delete_chart_CNOT_column_residual"] > 1.4
        and deletions["dirty_match_false_fires"] > 0
        and deletions["dirty_bypass_change"] > 1.4
        and deletions["maximum_two_rail_unitarity_residual"] < TOL
        and deletions["off_code_vacuum_change"] < TOL
        and deletions["off_code_double_occupation_change"] < TOL
        and not deletions["dirty_edge_or_matcher_in_declared_code"],
        deletions,
    )

    deletion_source = inspect.getsource(fixed.deletion_and_domain_certificate)
    check(
        "component controls do not substitute for a literal whole-word inverse or deletion trace",
        "np.exp(1j * route_c.c230.COUPLING * pairs)" in contact_source
        and "for mode in intermediate" in seam_source
        and "state = apply_contact(state)" in executor_source
        and "minimum_delete_transition_CZ_residual\": 2.0" in deletion_source
        and "minimum_delete_edge_role_phase_residual\": 2.0" in deletion_source
        and "routed.routing_truth_tables()" in deletion_source
        and "route_c.build_patch_update" in deletion_source
        and "refresh.matcher_and_role_resources()" in deletion_source
        and "route_c.unlawful_domain_controls()" in deletion_source
        and "execute_word(" not in deletion_source
        and "U_dagger_U" not in file_source
        and "execute_inverse" not in file_source,
        {
            "contact_execution": "aggregate basis-phase formula",
            "seam_execution": "aggregate parity/FSWAP macro",
            "full_2^323_off_code_execution": False,
            "whole_word_inverse_executed": False,
            "component_deletion_controls_executed": True,
            "whole_literal_word_deletions_executed": False,
            "literal_transition_and_edge_phase_minima": True,
            "global_n_le_2_constraint_is_local": registers[
                "global_n_le_2_constraint_is_local"
            ],
        },
    )

    covariance = fixed.covariance_and_translation_certificate()
    covariance_source = inspect.getsource(fixed.covariance_and_translation_certificate)
    check(
        "fixed-register covariance remains a partial coordinate census, not executed-word covariance",
        covariance["proper_cubic_frames"] == 24
        and covariance["ordered_frame_products"] == 576
        and covariance["rotated_operand_locality_failures"] == 0
        and covariance["operand_frame_composition_failures"] == 0
        and all(row["operand_collision_failures"] == 0 for row in covariance["translation_rows"])
        and not covariance["coin_operand_factorization_covariant_gate_by_gate"]
        and not covariance["E_fixed_columns_transformed_and_compared"]
        and not covariance["executed_operand_matrices_rebuilt_under_frames"]
        and not covariance["full_fixed_register_covariance_claimed"]
        and covariance["translation_test_level"] == "fixed operand addresses only"
        and "execute_word" not in covariance_source
        and "apply_contact" not in covariance_source
        and "apply_coin" not in covariance_source
        and "role_refresh" not in covariance_source
        and "failures += len(translated) != len(set(translated))" in covariance_source,
        {
            "coordinate_operand_families": covariance["physical_operand_families"],
            "executed_word_covariance_residual_present": False,
            "E_fixed_columns_transformed_and_compared": False,
            "contact_role_matcher_coin_operands_in_coordinate_family": False,
            "translation_test": covariance["translation_test_level"],
            "coin_gate_by_gate_covariance": covariance[
                "coin_operand_factorization_covariant_gate_by_gate"
            ],
        },
    )
    return {
        "exact_target_commit": "928eeb641d688a8774fbf885fc5fdd556246ca02",
        "finite_code_sector_macro_intertwiner_positive": True,
        "wrong_target_rejected": True,
        "fixed_data_bits_executed": True,
        "decoded_interface_M2_count": binding["decoded_interface_M2_count"],
        "bound_physical_fixture_M2_count": binding["bound_physical_fixture_M2_count"],
        "source_identity_and_physical_binding_boundary_accurate": True,
        "Cycle655_binding_executed_end_to_end": False,
        "literal_323_M2_tensor_product_word_executed": False,
        "matcher_controlled_Givens_composed": False,
        "full_off_code_unitarity_executed": False,
        "component_deletion_and_domain_controls_executed": True,
        "whole_literal_word_deletions_executed": False,
        "executed_word_covariance_residual_present": False,
        "candidate_sha256": sha256(Path(fixed.__file__).read_bytes()).hexdigest(),
    }


def literal_register_route_checks() -> dict[str, object]:
    """Source-instrument the literal decoded-interface successor bc377db727."""

    cells = len(literal.base.CELLS)
    inventory = {
        "data": literal.base.MODE_COUNT,
        "role_rails": 7 * cells,
        "charts": 2 * len(literal.base.FEATURES),
        "tokens": cells,
        "matcher_scratch": 5 * cells,
        "matcher_flags": cells,
        "bypass": 2 * cells,
        "edge_work": len(literal.base.EDGES),
        "transit": cells,
    }
    local = literal.local_literal_controls()
    check(
        "the literal successor stores all 335 decoded-interface M2 bits and uses a real token control",
        set(literal.LiteralBasis.__dataclass_fields__) == set(inventory)
        and sum(inventory.values()) == 335
        and local["literal_decoded_interface_M2"] == 335
        and local["matcher_cases"] == 384
        and local["matcher_failures"] == 0
        and local["matcher_return_failures"] == 0
        and local["token_zero_block_cases"] == 384
        and local["token_zero_block_failures"] == 0
        and local["token_zero_return_failures"] == 0
        and local["maximum_two_rail_unitarity_residual"] < TOL
        and local["off_code_vacuum_change"] < TOL
        and local["off_code_double_change"] < TOL,
        {"inventory": inventory, "local_controls": local},
    )

    primitive_names = (
        "x_data",
        "toffoli_token_data_to_scratch",
        "toffoli_scratch_data_to_scratch",
        "toffoli_scratch_data_to_flag",
        "fredkin_role_bypass",
        "two_bypass_matrix",
        "chart_word",
        "apply_data_gate",
        "swap_data_transit",
        "cz_data_pair",
        "cz_transit_data",
        "cnot_data_edge",
        "cz_data_edge",
        "swap_data",
        "swap_role_rail",
        "role_refresh",
        "coin_word",
        "transition_word",
        "seam_word",
        "contact_word",
    )
    originals = {name: getattr(literal, name) for name in primitive_names}
    counts: Counter[str] = Counter()

    def counted(name, operation):
        def wrapper(*args, **kwargs):
            counts[name] += 1
            return operation(*args, **kwargs)

        return wrapper

    for name, operation in originals.items():
        setattr(literal, name, counted(name, operation))
    try:
        vacuum = literal.encoded_column((), 5)
        vacuum_output, vacuum_stages = literal.execute(vacuum, True)
    finally:
        for name, operation in originals.items():
            setattr(literal, name, operation)

    expected_counts = {
        "apply_data_gate": 312,
        "chart_word": 2,
        "cnot_data_edge": 112,
        "coin_word": 1,
        "contact_word": 1,
        "cz_data_edge": 22,
        "cz_data_pair": 158,
        "cz_transit_data": 77,
        "fredkin_role_bypass": 2880,
        "role_refresh": 2,
        "seam_word": 11,
        "swap_data": 11,
        "swap_data_transit": 154,
        "swap_role_rail": 77,
        "toffoli_scratch_data_to_flag": 288,
        "toffoli_scratch_data_to_scratch": 1152,
        "toffoli_token_data_to_scratch": 288,
        "transition_word": 1,
        "two_bypass_matrix": 720,
        "x_data": 1440,
    }
    check(
        "every declared literal program family is invoked with the advertised bounded count",
        dict(counts) == expected_counts
        and 2 * 2 * len(literal.base.FEATURES) == 96
        and all(value == 0 for value in vacuum_stages.values())
        and len(vacuum) == len(vacuum_output) == 1,
        {
            "source_instrumented_call_counts": dict(sorted(counts.items())),
            "chart_CNOTs_inside_two_chart_words": 96,
            "coin_plus_contact_apply_data_gate_calls": counts["apply_data_gate"],
            "vacuum_stage_failures": vacuum_stages,
        },
    )

    stream = literal.base.route_c.patch_stream(literal.base.CELLS, literal.base.EDGES)
    contact = literal.base.route_c.patch_contact(literal.base.CELLS)
    identity = sparse.eye(len(literal.base.FOCK_BASIS), format="csc")
    column = next(
        index
        for index in range(len(literal.base.FOCK_BASIS))
        if (stream.getcol(index) - identity.getcol(index)).nnz
    )
    source = literal.encoded_column(literal.base.FOCK_BASIS[column], 5)
    observed, stages = literal.execute(source, False)
    correct = literal.expected(contact @ stream, column, 5, 0)
    wrong = literal.expected(contact, column, 5, 0)
    correct_raw, correct_norm = literal.difference(observed, correct)
    wrong_raw, wrong_norm = literal.difference(observed, wrong)
    execute_source = inspect.getsource(literal.execute)
    check(
        "the literal candidate is runtime-target-independent and rejects an identity-stream target",
        correct_raw < TOL
        and correct_norm < TOL
        and wrong_raw > 0.4
        and wrong_norm > 1.4
        and "expected(" not in execute_source
        and "patch_stream" not in execute_source
        and "patch_contact" not in execute_source
        and all(value == 0 for value in stages.values()),
        {
            "probe_column": column,
            "correct_target_residual": (correct_raw, correct_norm),
            "wrong_identity_stream_residual": (wrong_raw, wrong_norm),
            "runtime_target_operand_present": False,
            "transition_synthesized_offline_from_target_inversion_set": True,
        },
    )

    held_pairs = ((0, 1), (0, 6), (1, 31), (17, 44), (70, 71))
    held_columns = (
        0,
        *range(1, 1 + literal.base.MODE_COUNT),
        *(literal.base.FOCK_INDEX[pair] for pair in held_pairs),
    )
    main_source = inspect.getsource(literal.main)
    check(
        "held L6 and literal coin closure are explicitly bounded samples and inverse execution remains open",
        len(held_columns) == 78
        and len(held_pairs) == 5
        and len(literal.base.FOCK_BASIS) == 2629
        and "intertwiner(5, False, full_columns)" in main_source
        and "intertwiner(6, False, tuple(held_columns))" in main_source
        and "intertwiner(5, True, coin_columns)" in main_source
        and "intertwiner(6, True, coin_columns)" in main_source
        and "complete literal L6 stream/contact sweep" in main_source
        and "complete inverse macrostep" in main_source
        and "execute_inverse" not in main_source,
        {
            "L5_stream_contact_columns": len(literal.base.FOCK_BASIS),
            "L6_stream_contact_sample_columns": len(held_columns),
            "L6_two_particle_sample_columns": len(held_pairs),
            "available_two_particle_columns": 2556,
            "literal_coin_columns_per_size": len(held_columns),
            "whole_literal_word_inverse_executed": False,
        },
    )

    deletion_rows = {
        "coin": literal_delete.coin_deletions(),
        "transition": literal_delete.transition_deletions(),
        "seam": literal_delete.seam_deletions(),
        "contact": literal_delete.contact_deletions(),
        "carrier": literal_delete.carrier_factor_deletions(),
        "tokens": literal_delete.token_control_deletions(),
        "charts": literal_delete.chart_deletions(),
        "dirty_domain": literal_delete.dirty_domain(),
    }
    deletion_source = Path(literal_delete.__file__).read_text(encoding="utf-8")
    check(
        "literal component words now have active primitive deletions, but no complete-word omission residual",
        deletion_rows["coin"]["literal_coin_factor_deletions"] == 11
        and deletion_rows["coin"]["minimum_maximum_column_delete_residual"] > 0.005
        and deletion_rows["transition"]["literal_transition_terms"] == 224
        and deletion_rows["transition"]["literal_routed_SWAP_primitives"] == 154
        and deletion_rows["transition"]["minimum_delete_CZ_residual"] > 1.9
        and deletion_rows["seam"]["literal_seam_edges"] == 11
        and all(
            value > 0.9
            for value in deletion_rows["seam"][
                "minimum_maximum_witness_by_category"
            ].values()
        )
        and deletion_rows["contact"]["literal_contact_factor_deletions"] == 180
        and deletion_rows["carrier"]["literal_carrier_factor_deletions"] == 30
        and deletion_rows["tokens"]["literal_token_control_pairs_deleted"] == 12
        and deletion_rows["charts"]["literal_chart_control_deletions"] == 48
        and not deletion_rows["dirty_domain"]["dirty_auxiliary_in_declared_code"]
        and "literal.execute(" not in deletion_source
        and "intertwiner(" not in deletion_source
        and "execute_inverse" not in deletion_source,
        {
            "coin_gate_types": deletion_rows["coin"][
                "literal_coin_factor_deletions"
            ],
            "transition_terms": deletion_rows["transition"][
                "literal_transition_terms"
            ],
            "routed_SWAP_primitives": deletion_rows["transition"][
                "literal_routed_SWAP_primitives"
            ],
            "seam_edges": deletion_rows["seam"]["literal_seam_edges"],
            "contact_instances": deletion_rows["contact"][
                "literal_contact_factor_deletions"
            ],
            "carrier_factor_types_at_one_cell": deletion_rows["carrier"][
                "literal_carrier_factor_deletions"
            ],
            "token_control_pairs": deletion_rows["tokens"][
                "literal_token_control_pairs_deleted"
            ],
            "chart_control_types": deletion_rows["charts"][
                "literal_chart_control_deletions"
            ],
            "complete_335_M2_word_omission_residual_executed": False,
        },
    )
    return {
        "exact_literal_commit": "bc377db727",
        "exact_deletion_commit": "2476b30563",
        "literal_decoded_interface_M2": sum(inventory.values()),
        "all_declared_program_families_invoked": True,
        "runtime_target_operand_present": False,
        "complete_L5_stream_contact_columns": 2629,
        "L6_stream_contact_sample_columns": len(held_columns),
        "literal_coin_sample_columns_per_size": len(held_columns),
        "complete_literal_L6_stream_contact_executed": False,
        "complete_literal_coin_sweep_executed": False,
        "literal_component_deletion_witnesses_executed": True,
        "complete_335_M2_word_omission_residual_executed": False,
        "whole_literal_word_inverse_executed": False,
        "Cycle655_binding_executed_end_to_end": False,
        "candidate_sha256": sha256(Path(literal.__file__).read_bytes()).hexdigest(),
    }


def common_e_successor_checks() -> dict[str, object]:
    """Separate the exact direct common-E failure from finite gauge closure."""

    direct_execute_source = inspect.getsource(common_direct.execute_composition)
    direct_main_source = inspect.getsource(common_direct.main)
    gauge_execute_source = inspect.getsource(common_gauge.execute)
    gauge_main_source = inspect.getsource(common_gauge.main)
    check(
        "the direct successor actually multiplies eleven physical owner ROMs on the 59941x2629 common E",
        "state = (operator @ state).tocsc()" in direct_execute_source
        and "target = fixture.encoding @ logical" in direct_execute_source
        and "contact @ state" in direct_execute_source
        and "physical_rows\"] == 59941" in direct_main_source
        and "logical_columns\"] == 2629" in direct_main_source
        and "len(row[\"stage_rows\"]) == 11" in direct_main_source
        and "U_physical_E_minus_E_G_target_norm\"] > 30.0" in direct_main_source
        and "U_physical_E_minus_E_G_target_opnorm\"] > 1.9" in direct_main_source
        and "physical_code_leakage_norm\"] < TOL" in direct_main_source
        and "Gram_or_isometry_used_as_intertwiner" in direct_execute_source
        and "dense_EUE_completion_used" in direct_execute_source,
        {
            "actual_common_E_shape": (59941, 2629),
            "physical_owner_ROMs_multiplied": 11,
            "canonical_replay_terminal": (
                "ROUTE_A_ACTUAL_COMMON_E_COMPOSITION_FALSIFIED_BY_"
                "UNSUPPLIED_CAR_PARITY_COCYCLE"
            ),
            "direct_target_closes": False,
            "final_missing_signed_columns": 240,
        },
    )

    direct_missing, direct_pairs = common_gauge.direct_missing_pair_set()
    local_repair = direct_pairs ^ common_gauge.SIGNED_CANDIDATE
    check(
        "the finite gauge successor adds the disclosed order-derived correction and closes the actual common E",
        len(direct_missing) == 240
        and len(common_gauge.TRANSITION) == 224
        and len(local_repair) == 110
        and common_gauge.TRANSITION
        == common_gauge.SIGNED_CANDIDATE ^ common_gauge.TARGET_PAIRS
        and "owner_physical @ correction_physical @ corrected_state" in gauge_execute_source
        and "target_state = fixture.encoding @ target_update" in gauge_execute_source
        and "corrected_mismatch_columns\"] == 0" in gauge_main_source
        and "U_physical_E_minus_E_G_target_norm\"] < TOL" in gauge_main_source
        and "candidate_without_transition_opnorm\"] > 1.9" in gauge_main_source
        and "transition_target_derived_offline" in gauge_execute_source
        and "runtime_target_lookup_used" in gauge_execute_source,
        {
            "direct_missing_columns": len(direct_missing),
            "transition_CZ_pairs": len(common_gauge.TRANSITION),
            "local_signed_repair_pairs": len(local_repair),
            "transition_equals_candidate_XOR_target": True,
            "canonical_replay_terminal": (
                "ACTUAL_59941_ROW_GAUGE_CORRECTED_CAR_COMPILER_CLOSED"
            ),
        },
    )

    chain, corner = common_gauge.three_center_extension_audit()
    check(
        "common-E gauge closure is finite and order-derived rather than recurrent or full-covariant",
        chain["transition_CZ_pairs"] == 328
        and chain["maximum_transition_cell_distance"] == 2
        and chain["current_one_transit_routing_supported"]
        and corner["transition_CZ_pairs"] == 454
        and corner["maximum_transition_cell_distance"] == 3
        and corner["distance_gt_2_pairs"] == 56
        and not corner["current_one_transit_routing_supported"]
        and "preferred_finite_order_encoded_in_supplied_ROM\"]" in gauge_main_source
        and "ambient_59941_row_physical_matrices_rebuilt_per_frame\": False"
        in gauge_main_source,
        {
            "transition_target_derived_offline": True,
            "preferred_finite_order_supplied": True,
            "chain_extension": chain,
            "L_corner_extension": corner,
            "ambient_physical_covariance_rebuilt": False,
            "recurrent_rule_closed": False,
        },
    )
    return {
        "exact_direct_commit": "8e873bb244",
        "exact_gauge_commit": "0c9e7ce3a2",
        "actual_common_E_shape": (59941, 2629),
        "direct_actual_common_E_executed": True,
        "direct_actual_common_E_target_closes": False,
        "direct_missing_signed_columns": len(direct_missing),
        "finite_gauge_corrected_common_E_executed": True,
        "finite_gauge_corrected_common_E_closes": True,
        "transition_target_derived_offline": True,
        "preferred_finite_order_supplied": True,
        "recurrent_no_preferred_order_law_closed": False,
        "ambient_physical_covariance_rebuilt": False,
        "direct_candidate_sha256": sha256(
            Path(common_direct.__file__).read_bytes()
        ).hexdigest(),
        "gauge_candidate_sha256": sha256(
            Path(common_gauge.__file__).read_bytes()
        ).hexdigest(),
    }


def main() -> None:
    direct = direct_route_checks()
    sparse_result = sparse_route_checks()
    fixed_result = fixed_register_route_checks()
    literal_result = literal_register_route_checks()
    common_e_result = common_e_successor_checks()
    missing = {
        "direct_and_gauge_common_E": (
            "the actual direct common-E product has now been measured and fails its target; the "
            "finite order-derived gauge correction closes that fixture. What remains is a fixed "
            "target-independent local gauge/chart generator that handles L-shaped and larger "
            "overlaps without a supplied global order, plus an ambient transformed-E covariance "
            "test before any recurrent/autonomous-law claim"
        ),
        "decoded_sparse_baseline": (
            "the old 125749-row direct sum remains an aggregate decoded baseline; use the literal "
            "335-M2 successor for factor-execution claims"
        ),
        "literal_register_successor": (
            "execute the supplied Cycle655 decode/interface/encode binding end to end; complete the "
            "literal L6 stream/contact and literal coin sweeps beyond the current 78-column samples; "
            "add omissions from the composed 335-M2 word, a whole-word inverse/off-code check, and "
            "transformed-E covariance. The recurrent transition still needs a no-preferred-order "
            "local replacement"
        ),
    }
    summary = {
        "authority": "none",
        "audit": "unset",
        "status": "finite-common-E-and-literal-interface-positive-recurrent-law-open",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "direct_ROM_baseline": direct,
        "decoded_sparse_baseline": sparse_result,
        "fixed_register_macro_successor": fixed_result,
        "literal_register_successor": literal_result,
        "actual_common_E_successors": common_e_result,
        "missing_executed_objects": missing,
        "claim_ceiling": (
            "The 315 baseline supplies coefficient-tagged finite ROM primitives but does not itself "
            "compose them. The 8e actual 59941x2629 common-E direct composition does, and falsifies "
            "the uncorrected target with 240 signed columns. The 0c finite gauge successor closes the "
            "same common E after an explicitly target/order-derived correction; recurrence and full "
            "ambient covariance remain open. The bc literal successor invokes every declared program "
            "family on a real 335-M2 decoded interface, closes all 2629 L5 stream/contact columns, and "
            "rejects a wrong target. Its L6 stream/contact and both literal coin checks cover only 78 "
            "columns, its Cycle655 physical binding is supplied, and literal-word deletion, inverse, "
            "full covariance, and the no-preferred-order recurrent law remain open. Cycle703 therefore "
            "starts from a positive finite compiler baseline, not from a recurrent closure."
        ),
        "terminal": "FINITE_COMMON_E_AND_LITERAL_INTERFACE_POSITIVE_RECURRENT_LAW_OPEN",
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    print("RESULT", summary["terminal"] if FAIL == 0 else "UNFINISHED_ADVERSARIAL_CHECK")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
