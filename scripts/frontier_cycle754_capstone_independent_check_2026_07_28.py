#!/usr/bin/env python3
"""Independent check of the Cycle 754 finite API composition.

This checker does not import the Cycle 754 primary. It reconstructs the
Boolean receiver, endpoint-support indicator, and relevant decision branch,
then compares those independent values with the current dependency APIs.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
PRIMARY_PATH = (
    "scripts/frontier_cycle754_composed_four_flag_acceptance_2026_07_28.py"
)
NOTE_PATH = (
    "docs/COMPOSED_FOUR_FLAG_ACCEPTANCE_CYCLE754_"
    "BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "docs/BINDER_FORMATION_ATTEMPT_CYCLE751_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/COMPOSED_FOUR_FLAG_ACCEPTANCE_CYCLE754_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/CYCLE332_RECEIVER_SUCCESS_CYCLE610_GATE_ADAPTER_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/connected_edge_autonomous_apparatus_law_cycle282_2026_07_17.py",
    "scripts/connected_edge_same_code_local_instrument_cycle278_2026_07_17.py",
    "scripts/contact_close_typed_record_dag_cycle287_2026_07_17.py",
    "scripts/contractible_lightcone_wilson_quotient_cycle271_2026_07_17.py",
    "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py",
    "scripts/frontier_cycle718_carrier_return_core_2026_07_26.py",
    "scripts/frontier_cycle718_cycle713_carrier_return_composition_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_export_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py",
    "scripts/frontier_cycle718_three_bank_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle747_receiver_success_gate_adapter_2026_07_30.py",
    "scripts/frontier_cycle751_binder_formation_attempt_2026_07_28.py",
    "scripts/frontier_cycle754_capstone_independent_check_2026_07_28.py",
    "scripts/frontier_cycle754_composed_four_flag_acceptance_2026_07_28.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/locally_matched_wilson_sector_states_cycle275_2026_07_17.py",
    "scripts/matter_coupling_faithful_close_record_candidate_cycle281_2026_07_17.py",
    "scripts/outgoing_carrier_nonrecurrence_cycle286_2026_07_17.py",
    "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py",
    "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py",
    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py",
    "scripts/physical_cycle269_coherent_cubic_pair_orbit_2026_07_17.py",
    "scripts/physical_cycle269_coin_stream_contact_common_refinement_cycle304_2026_07_17.py",
    "scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py",
    "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py",
    "scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py",
    "scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py",
    "scripts/physical_cycle269_joint_six_mode_coin_lift_cycle302_2026_07_17.py",
    "scripts/physical_cycle269_local_contact_intertwiner_2026_07_17.py",
    "scripts/physical_cycle269_local_fock_extension_cycle312_2026_07_18.py",
    "scripts/physical_cycle269_position_growing_recurrent_compiler_cycle307_2026_07_17.py",
    "scripts/physical_cycle269_reference_relative_localized_pair_lift_2026_07_17.py",
    "scripts/physical_cycle269_staggered_reservoir_catchup_2026_07_17.py",
    "scripts/physical_event_to_append_commit_candidate_cycle326_2026_07_18.py",
    "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_m64_reversible_event_sidecar_cycle314_2026_07_18.py",
    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py",
    "scripts/physical_support_matcher_predecessor_controls_cycle329_2026_07_18.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
    "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from itertools import product
import json
from pathlib import Path
from time import perf_counter

import frontier_cycle747_receiver_success_gate_adapter_2026_07_30 as C747
import frontier_cycle751_binder_formation_attempt_2026_07_28 as C751


ROOT = Path(__file__).resolve().parents[1]
CHECKS: dict[str, bool] = {}


def check(label: str, condition: bool, detail: object = "") -> None:
    if label in CHECKS:
        raise AssertionError(("duplicate check label", label))
    CHECKS[label] = bool(condition)
    print(
        f"{'PASS' if condition else 'FAIL'} {label} :: "
        f"{json.dumps(detail, sort_keys=True, default=str)}"
    )


def normalized_note() -> str:
    body = (ROOT / NOTE_PATH).read_text(encoding="utf-8").lower()
    return " ".join(body.replace("`", "").split())


def note_contract() -> dict[str, object]:
    required = (
        "claim type: bounded_theorem",
        "4 * 64 = 256",
        "not a common-event construction",
        "framework admissibility",
        "framework binder",
        "ships no authored pass transcript or claim-status receipt",
    )
    try:
        text = normalized_note()
    except OSError:
        return {"exists": False, "missing": required}
    return {
        "exists": True,
        "missing": tuple(phrase for phrase in required if phrase not in text),
    }


def source_contract() -> dict[str, object]:
    checker_source = Path(__file__).read_text(encoding="utf-8")
    checker_tree = ast.parse(checker_source)
    imported_modules = tuple(
        sorted(
            alias.name
            for node in ast.walk(checker_tree)
            if isinstance(node, ast.Import)
            for alias in node.names
        )
    )
    missing_inputs = tuple(
        relative
        for relative in AUDIT_INPUT_PATHS
        if not (ROOT / relative).is_file()
    )
    return {
        "primary_exists": (ROOT / PRIMARY_PATH).is_file(),
        "primary_imported": Path(PRIMARY_PATH).stem in imported_modules,
        "declared": len(AUDIT_INPUT_PATHS),
        "unique": len(set(AUDIT_INPUT_PATHS)),
        "missing_inputs": missing_inputs,
    }


def independent_status(receiver_success: int, binder: int) -> str:
    certificate = actuality = law_domain = fresh = capacity = 1
    if not (certificate and binder):
        return "no_opportunity"
    if not fresh:
        return "refused_fresh"
    if not (actuality and receiver_success and law_domain):
        return "refused_supplied"
    if not capacity:
        return "exhausted"
    return "admitted"


def reconstruct_composition() -> dict[str, object]:
    endpoint_rows = C751.trajectory(2)["rows"]
    if not isinstance(endpoint_rows, tuple):
        raise TypeError("Cycle 751 trajectory rows must be a tuple")

    endpoint_indicator_mismatches = 0
    receiver_mismatches = 0
    status_mismatches = 0
    observed_statuses: Counter[str] = Counter()
    expected_statuses: Counter[str] = Counter()
    direct_indicators: list[int] = []
    api_indicators: list[int] = []

    for endpoint in endpoint_rows:
        direct_indicator = int(bool(endpoint.support))
        api_indicator = C751.net_delta_nonempty(endpoint)
        direct_indicators.append(direct_indicator)
        api_indicators.append(api_indicator)
        endpoint_indicator_mismatches += direct_indicator != api_indicator

        for bits in product((0, 1), repeat=6):
            direct_receiver = int(all(bits))
            api_receiver, _certificate = C747.actual_receiver_success(bits)
            receiver_mismatches += direct_receiver != api_receiver

            expected_status = independent_status(
                direct_receiver,
                direct_indicator,
            )
            observed_status = C747.adapter_status(
                api_receiver,
                binder=api_indicator,
                certificate=1,
                actuality=1,
                law_domain=1,
            )
            status_mismatches += expected_status != observed_status
            expected_statuses[expected_status] += 1
            observed_statuses[observed_status] += 1

    return {
        "endpoint_rows": len(endpoint_rows),
        "rows": len(endpoint_rows) * 64,
        "direct_indicators": direct_indicators,
        "api_indicators": api_indicators,
        "endpoint_indicator_mismatches": endpoint_indicator_mismatches,
        "receiver_mismatches": receiver_mismatches,
        "status_mismatches": status_mismatches,
        "expected_status_counts": dict(sorted(expected_statuses.items())),
        "observed_status_counts": dict(sorted(observed_statuses.items())),
    }


def main() -> int:
    started = perf_counter()

    note = note_contract()
    check(
        "A_exact_note_boundary",
        note["exists"] and not note["missing"],
        note,
    )

    sources = source_contract()
    check(
        "B_independent_source_and_input_contract",
        (
            sources["primary_exists"]
            and not sources["primary_imported"]
            and not sources["missing_inputs"]
            and sources["declared"] == sources["unique"]
        ),
        sources,
    )

    result = reconstruct_composition()
    check(
        "C_direct_endpoint_support_reconstruction",
        (
            result["endpoint_rows"] == 4
            and result["direct_indicators"] == [1, 1, 1, 1]
            and result["direct_indicators"] == result["api_indicators"]
            and result["endpoint_indicator_mismatches"] == 0
        ),
        {
            "endpoint_rows": result["endpoint_rows"],
            "direct_indicators": result["direct_indicators"],
            "api_indicators": result["api_indicators"],
            "mismatches": result["endpoint_indicator_mismatches"],
        },
    )
    check(
        "D_complete_receiver_conjunction_reconstruction",
        result["rows"] == 256 and result["receiver_mismatches"] == 0,
        {
            "rows": result["rows"],
            "receiver_mismatches": result["receiver_mismatches"],
        },
    )
    check(
        "E_independent_decision_branch_matches_API",
        (
            result["status_mismatches"] == 0
            and result["expected_status_counts"]
            == {"admitted": 4, "refused_supplied": 252}
            and result["observed_status_counts"]
            == result["expected_status_counts"]
        ),
        {
            "status_mismatches": result["status_mismatches"],
            "expected": result["expected_status_counts"],
            "observed": result["observed_status_counts"],
        },
    )

    runtime = perf_counter() - started
    check(
        "F_runtime_within_declared_timeout",
        runtime <= AUDIT_TIMEOUT_SEC,
        {"runtime_sec": round(runtime, 6), "timeout_sec": AUDIT_TIMEOUT_SEC},
    )

    report = {
        "cycle": 754,
        "claim": "independent finite receiver/endpoint API reconstruction",
        "bounded": True,
        "result": result,
        "checks": CHECKS,
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "runtime_sec": round(runtime, 6),
    }
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE754_FINITE_API_INDEPENDENT_PASS"
        if report["pass"]
        else "CYCLE754_FINITE_API_INDEPENDENT_FAIL"
    )
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    print(report["terminal"])
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
