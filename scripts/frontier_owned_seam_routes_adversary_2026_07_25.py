#!/usr/bin/env python3
"""Adversarial boundary checks for the two owned-seam repair routes.

The direct-ROM target is commit 16a550601d.  The sparse routed-transition
target is commit 1f75a79e4f.  This companion retains their executed positive
results and checks whether either runner actually supplies the coefficient-
tagged all-seam physical word used by its terminal claim.
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


def direct_descriptor_audit() -> tuple[dict[str, object], dict[object, object]]:
    """Capture the direct runner's ephemeral descriptor dictionary at L=5."""

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
    descriptors = max(instances, key=len)
    if len(descriptors) != result["distinct_controlled_two_level_rows"]:
        raise AssertionError((len(descriptors), result))
    return result, descriptors


def direct_route_checks() -> dict[str, object]:
    primitive, descriptors = direct_descriptor_audit()
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
        and overpaired_unordered_rows == 0,
        {
            "directed_rows": len(physical_directed),
            "physically_rekeyed_conflicts": physically_rekeyed_conflicts,
            "hidden_pair_variants": hidden_pair_variants,
            "unordered_reverse_pairs": len(physical_unordered),
        },
    )

    primitive_source = inspect.getsource(direct_rom.physical_two_level_primitive_audit)
    pair_source = inspect.getsource(direct_rom.pair_control)
    check(
        "direct-ROM Givens coefficients are not associated with physical transition rows",
        descriptor_value_widths == {4}
        and "givens_coefficients" not in primitive_source
        and "landed_complex_givens_coefficients" in pair_source
        and primitive["distinct_controlled_two_level_rows"] == 46306,
        {
            "descriptor_value": "(target_observation, phase, x_word, z_word)",
            "coefficient_or_stage_field_present": False,
            "source_projectors_with_multiple_sequential_targets": sum(
                len(values) > 1 for values in source_fan.values()
            ),
            "maximum_target_fan": max(map(len, source_fan.values())),
        },
    )

    direct_path = Path(direct_rom.__file__)
    direct_source = direct_path.read_text(encoding="utf-8")
    composition_source = inspect.getsource(direct_rom.composed_update_controls)
    check(
        "direct-ROM locality and all-eleven residuals remain support-count and scalar claims",
        primitive["maximum_transition_Pauli_support"] == 26
        and "diameter" not in primitive_source
        and "11 * maximum_local_intertwiner" in composition_source
        and "11 * maximum_local_leakage" in composition_source
        and "physical_two_level_primitive_audit" not in composition_source,
        {
            "maximum_transition_Pauli_support": primitive[
                "maximum_transition_Pauli_support"
            ],
            "maximum_control_plus_transition_tensor_M2": primitive[
                "maximum_control_plus_transition_tensor_M2"
            ],
            "geometric_diameter_measured": False,
            "common_physical_product_applied": False,
        },
    )

    check(
        "the 46,306 direct rows are host-derived ephemeral data, not a supplied fixed ROM word",
        "for label in direct.LABELS" in primitive_source
        and "descriptor_rows" not in primitive
        and "descriptor_sha256" not in primitive
        and "givens_coefficients" not in primitive_source
        and '"physical_M2_primitive_supplied": descriptor_conflicts == 0'
        in primitive_source,
        {
            "rows": primitive["distinct_controlled_two_level_rows"],
            "serialized_rows": False,
            "coefficient_tagged_rows": False,
            "autonomous_local_rule_executed": False,
            "candidate_sha256": sha256(direct_path.read_bytes()).hexdigest(),
        },
    )
    return {
        "descriptor_rows": len(descriptors),
        "physical_rekey_conflicts": physically_rekeyed_conflicts,
        "coefficient_association_executed": False,
        "geometric_diameter_measured": False,
        "common_all_eleven_operator_executed": False,
        "source_contains_old_decoder_tautology": "0 ^ decoded ^ decoded" in direct_source,
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

    candidate_stream = routed.logical_permutation_matrix(routed.CANDIDATE)
    target_stream = routed.logical_permutation_matrix(routed.TARGET)
    transition = sparse.diags(
        [
            routed.adjacent.phase_from_pairs(
                sum(1 << mode for mode in label), routed.TRANSITION
            )
            for label in routed.route_c.FOCK_BASIS
        ],
        format="csc",
        dtype=complex,
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

    encoding_row, encoding = routed.refresh.patch_branch_rows(5)
    wrong_diagonal = np.ones(encoding.shape[1], dtype=complex)
    wrong_diagonal[0] = -1
    wrong_logical = sparse.diags(wrong_diagonal, format="csc")
    vacuous = routed.refresh.factorized_intertwiner(encoding, wrong_logical)
    factorized_source = inspect.getsource(routed.refresh.factorized_intertwiner)
    check(
        "same-E factorized residual is only the Gram-isometry identity",
        max(vacuous.values()) < TOL
        and "logical @ (identity - gram)" in factorized_source
        and "physical" not in inspect.signature(
            routed.refresh.factorized_intertwiner
        ).parameters
        and "encoding" in inspect.signature(
            routed.refresh.factorized_intertwiner
        ).parameters,
        {
            "wrong_nontrivial_unitary_residual": vacuous,
            "wrong_logical_vs_identity_raw": 2.0,
            "physical_word_argument_present": False,
            "E_Gram_raw": encoding_row["Gram_raw_maximum"],
        },
    )

    seam_source = inspect.getsource(routed.signed_seam_resources)
    same_e_source = inspect.getsource(routed.same_encoding_certificate)
    check(
        "all eleven signed carriers are resource-censused rather than composed on E_refresh",
        "signed_carrier_census" in seam_source
        and "local_seam_matrices" not in seam_source
        and "factorized_intertwiner" in same_e_source
        and "execute_transition_word" not in same_e_source
        and "signed_seam_resources" not in same_e_source,
        {
            "resource_rows": 11,
            "physical_signed_seam_product_applied": False,
            "transition_plus_seams_plus_contact_operator_applied": False,
        },
    )

    covariance_source = inspect.getsource(routed.covariance_certificate)
    deletion_source = inspect.getsource(routed.deletion_certificate)
    check(
        "shared-chart preservation and physical covariance are not tested after the full word",
        encoding_row["shared_copy_equality_failures"] == 0
        and "transform_word" in covariance_source
        and "frame_and_translation_controls" in covariance_source
        and "execute_transition_word" not in covariance_source
        and "patch_branch_rows" not in covariance_source
        and "tuple(2.0 for _term in ROUTED_TERMS)" in deletion_source,
        {
            "initial_shared_chart_equality_failures": encoding_row[
                "shared_copy_equality_failures"
            ],
            "post_full_word_shared_chart_check_present": False,
            "physical_routed_unitary_covariance_residual_present": False,
            "macro_deletion_residuals_are_literal": True,
        },
    )
    return {
        "transition_word_executed": True,
        "transition_order_closed": True,
        "dirty_transit_reuse_closed": True,
        "physical_signed_seam_product_executed": False,
        "postword_shared_chart_preservation_executed": False,
        "physical_covariance_executed": False,
        "factorized_intertwiner_is_gram_identity": True,
        "candidate_sha256": sha256(Path(routed.__file__).read_bytes()).hexdigest(),
    }


def main() -> None:
    direct = direct_route_checks()
    sparse_result = sparse_route_checks()
    missing = {
        "direct_ROM": (
            "a serialized or autonomously generated ordered ROM row (owner, stage, source/target "
            "physical observations, Pauli transition, complex Givens coefficient), with geometric "
            "diameter, followed by the directly measured eleven-owner common-E product residual"
        ),
        "sparse_route": (
            "one executed U_physical on the 59,941-row E_refresh ambient that composes free coin, "
            "the routed 224-CZ correction, all eleven signed-carrier seam words, shared-chart "
            "updates, contact and clean return, followed by U_physical E-E G and rotated-word residuals"
        ),
    }
    summary = {
        "authority": "none",
        "audit": "unset",
        "status": "transition-positive-full-physical-compositions-open",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "direct_ROM": direct,
        "sparse_route": sparse_result,
        "missing_executed_objects": missing,
        "claim_ceiling": (
            "The direct route supplies conflict-free finite Pauli descriptors without coefficient-"
            "tagged ordered ROM execution. The sparse route supplies an exact nearest-neighbor "
            "224-CZ transition word, but not the advertised full signed-seam physical composition."
        ),
        "terminal": "OWNED_SEAM_TRANSITIONS_POSITIVE_FULL_PHYSICAL_COMPOSITIONS_OPEN",
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    print("RESULT", summary["terminal"] if FAIL == 0 else "UNFINISHED_ADVERSARIAL_CHECK")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
