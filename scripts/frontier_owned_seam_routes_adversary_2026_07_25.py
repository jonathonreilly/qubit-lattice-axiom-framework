#!/usr/bin/env python3
"""Adversarial boundary checks for the two owned-seam repair routes.

The direct-ROM target is commit 315788cd7e.  The sparse routed-transition
target is commit 483b24693e.  This companion retains their executed positive
results and checks the remaining all-seam physical composition boundary.
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
        "direct-ROM common-E composition and recurrent law remain explicitly unexecuted",
        "11 * maximum_local_intertwiner" in composition_source
        and "11 * maximum_local_leakage" in composition_source
        and "physical_two_level_primitive_audit" not in composition_source
        and not primitive["translation_invariant_recurrent_law_derived"]
        and not held_primitive["translation_invariant_recurrent_law_derived"]
        and not primitive["recurrent_volume_update_claimed"]
        and not held_primitive["recurrent_volume_update_claimed"],
        {
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
        "descriptor_rows": len(descriptors),
        "physical_rekey_conflicts": physically_rekeyed_conflicts,
        "coefficient_association_executed": True,
        "observation_only_control_rows_supplied": True,
        "geometric_diameter_measured": True,
        "finite_ROM_hash_inventoried": True,
        "all_torus_translations_tested": True,
        "common_all_eleven_operator_executed": False,
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


def main() -> None:
    direct = direct_route_checks()
    sparse_result = sparse_route_checks()
    missing = {
        "direct_ROM": (
            "the directly measured eleven-owner common-E product residual using the supplied "
            "coefficient-tagged finite ROMs, plus a volume-independent translated generator and "
            "overlapping-fixture composition theorem before any recurrent/autonomous-law claim"
        ),
        "sparse_route": (
            "embed the finite encoding in a declared fixed tensor-product M2 register ambient and "
            "replace global FOCK-label block lifts by the 378 routed local factors, eleven local "
            "seam words, onsite contact and chart/work erase-return operands; then compute the "
            "same-E residual and covariance of that physical operand. Free coin and mass remain "
            "separate unless they are also included in the claimed word"
        ),
    }
    summary = {
        "authority": "none",
        "audit": "unset",
        "status": "finite-primitive-positive-full-physical-compositions-open",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "direct_ROM": direct,
        "sparse_route": sparse_result,
        "missing_executed_objects": missing,
        "claim_ceiling": (
            "The direct route supplies coefficient-tagged, observation-only, bounded-diameter, "
            "hash-inventoried finite ROM primitives with full torus-translation audits. Its common-E "
            "all-owner composition and recurrent law remain open. The sparse route supplies an exact "
            "nearest-neighbor 224-CZ transition word and an algebraically square global-label direct-"
            "sum completion, with the transition synthesized offline from the target inversion set, "
            "but not a local-M2 tensor-product signed-seam physical composition."
        ),
        "terminal": "OWNED_SEAM_TRANSITIONS_POSITIVE_FULL_PHYSICAL_COMPOSITIONS_OPEN",
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    print("RESULT", summary["terminal"] if FAIL == 0 else "UNFINISHED_ADVERSARIAL_CHECK")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
