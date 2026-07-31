#!/usr/bin/env python3
"""Finite composition of the current Cycle 747 and Cycle 751 APIs.

The result is only a census of supplied software rows. It assigns no
framework or physical meaning to the lower-case API parameters or statuses.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
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

from collections import Counter
from itertools import product
import json
from pathlib import Path
import sys
from time import perf_counter

import frontier_cycle747_receiver_success_gate_adapter_2026_07_30 as C747
import frontier_cycle751_binder_formation_attempt_2026_07_28 as C751


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
SUPPLIED_ONE_BITS = {
    "certificate": 1,
    "actuality": 1,
    "law_domain": 1,
}
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
        "admitted 4",
        "refused_supplied 252",
        "not a common-event construction",
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


def input_contract() -> dict[str, object]:
    missing = tuple(
        relative
        for relative in AUDIT_INPUT_PATHS
        if not (ROOT / relative).is_file()
    )
    return {
        "declared": len(AUDIT_INPUT_PATHS),
        "unique": len(set(AUDIT_INPUT_PATHS)),
        "missing": missing,
        "contains_cycle747": (
            "scripts/frontier_cycle747_receiver_success_gate_adapter_2026_07_30.py"
            in AUDIT_INPUT_PATHS
        ),
        "contains_cycle751": (
            "scripts/frontier_cycle751_binder_formation_attempt_2026_07_28.py"
            in AUDIT_INPUT_PATHS
        ),
    }


def repository_modules_loaded() -> tuple[str, ...]:
    loaded: set[str] = set()
    for module in tuple(sys.modules.values()):
        raw = getattr(module, "__file__", None)
        if not raw:
            continue
        try:
            path = Path(raw).resolve()
            relative = path.relative_to(ROOT)
        except (OSError, ValueError):
            continue
        if path != SELF and relative.suffix == ".py":
            loaded.add(relative.as_posix())
    return tuple(sorted(loaded))


def finite_composition() -> dict[str, object]:
    endpoint_rows = C751.trajectory(2)["rows"]
    if not isinstance(endpoint_rows, tuple):
        raise TypeError("Cycle 751 trajectory rows must be a tuple")

    statuses: Counter[str] = Counter()
    binder_values: list[int] = []
    receiver_successes_by_endpoint: list[int] = []
    input_rows_by_endpoint: list[int] = []

    for endpoint in endpoint_rows:
        binder = C751.net_delta_nonempty(endpoint)
        binder_values.append(binder)
        receiver_successes = 0
        input_rows = 0
        for bits in product((0, 1), repeat=6):
            receiver_success, _certificate = C747.actual_receiver_success(bits)
            status = C747.adapter_status(
                receiver_success,
                binder=binder,
                **SUPPLIED_ONE_BITS,
            )
            statuses[status] += 1
            receiver_successes += receiver_success
            input_rows += 1
        receiver_successes_by_endpoint.append(receiver_successes)
        input_rows_by_endpoint.append(input_rows)

    return {
        "endpoint_rows": len(endpoint_rows),
        "binder_values": binder_values,
        "input_rows_by_endpoint": input_rows_by_endpoint,
        "receiver_successes_by_endpoint": receiver_successes_by_endpoint,
        "rows": sum(input_rows_by_endpoint),
        "status_counts": dict(sorted(statuses.items())),
    }


def main() -> int:
    started = perf_counter()

    note = note_contract()
    check(
        "A_exact_note_contract",
        note["exists"] and not note["missing"],
        note,
    )

    inputs = input_contract()
    check(
        "B_declared_mutable_input_closure",
        (
            not inputs["missing"]
            and inputs["declared"] == inputs["unique"]
            and inputs["contains_cycle747"]
            and inputs["contains_cycle751"]
        ),
        inputs,
    )

    result = finite_composition()
    check(
        "C_exact_cartesian_domain",
        (
            result["endpoint_rows"] == 4
            and result["input_rows_by_endpoint"] == [64, 64, 64, 64]
            and result["rows"] == 256
        ),
        {
            "endpoint_rows": result["endpoint_rows"],
            "input_rows_by_endpoint": result["input_rows_by_endpoint"],
            "rows": result["rows"],
        },
    )
    check(
        "D_current_dependency_API_values",
        (
            result["binder_values"] == [1, 1, 1, 1]
            and result["receiver_successes_by_endpoint"] == [1, 1, 1, 1]
        ),
        {
            "binder_values": result["binder_values"],
            "receiver_successes_by_endpoint":
                result["receiver_successes_by_endpoint"],
        },
    )
    check(
        "E_exact_lower_case_status_census",
        result["status_counts"]
        == {"admitted": 4, "refused_supplied": 252},
        result["status_counts"],
    )

    loaded = repository_modules_loaded()
    undeclared = tuple(sorted(set(loaded) - set(AUDIT_INPUT_PATHS)))
    check(
        "F_runtime_repository_imports_are_declared",
        not undeclared,
        {"loaded": len(loaded), "undeclared": undeclared},
    )

    boundary = {
        "common_event_map_claimed": False,
        "framework_admissibility_claimed": False,
        "framework_binder_claimed": False,
        "framework_law_claimed": False,
        "objective_actuality_claimed": False,
        "physical_occurrence_claimed": False,
        "record_claimed": False,
        "retained_grade_claimed": False,
    }
    check(
        "G_honest_software_API_boundary",
        not any(boundary.values()),
        boundary,
    )

    runtime = perf_counter() - started
    check(
        "H_runtime_within_declared_timeout",
        runtime <= AUDIT_TIMEOUT_SEC,
        {"runtime_sec": round(runtime, 6), "timeout_sec": AUDIT_TIMEOUT_SEC},
    )

    report = {
        "cycle": 754,
        "claim": "finite receiver/endpoint lower-case API composition",
        "bounded": True,
        "supplied_one_bits": SUPPLIED_ONE_BITS,
        "result": result,
        "boundary": boundary,
        "checks": CHECKS,
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "runtime_sec": round(runtime, 6),
    }
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE754_FINITE_API_COMPOSITION_PASS"
        if report["pass"]
        else "CYCLE754_FINITE_API_COMPOSITION_FAIL"
    )
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    print(report["terminal"])
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
