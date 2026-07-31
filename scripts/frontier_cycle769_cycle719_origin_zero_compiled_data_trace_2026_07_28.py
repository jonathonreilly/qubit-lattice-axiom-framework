#!/usr/bin/env python3
"""Cycle 769: exact data trace for one fixed Cycle-719 software fixture.

This runner makes no physical interpretation of the Cycle-719 ``EventCell``
API. It enumerates six support keys, records every data transition of the
fixed compiled controller, checks the final API decode, and reverses the word.
"""

from __future__ import annotations

from dataclasses import asdict
from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as C719


AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = (
    "docs/CYCLE719_ORIGIN_ZERO_COMPILED_DATA_TRACE_CYCLE769_"
    "BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "docs/CYCLE719_ORIGIN_ZERO_COMPILED_DATA_TRACE_CYCLE769_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "docs/PHYSICAL_M2_SPATIAL_ACK_CYCLE612_INTERVAL_BRIDGE_CYCLE718_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/RECURRENT_DIRECTIONAL_PACKET_BANK_CYCLE715_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/work_history/repo/review_feedback/CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
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
    "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py",
    "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py",
    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py",
    "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)

EXPECTED_MODES = [0, 2, 3, 4, 5, 6]
EXPECTED_CELL = {
    "identity": 0,
    "rotor": 15,
    "carry": 0,
    "predecessor": None,
    "binder": 1,
    "valid": 1,
    "orientation": 1,
}
EXPECTED_TRANSITIONS = [
    {
        "step": 0,
        "kind": "source",
        "program_index": 0,
        "changed_data_bits": 3,
        "decode_status": "refused",
        "decoded_cells": [],
    },
    {
        "step": 1,
        "kind": "bank",
        "program_index": 1,
        "changed_data_bits": 32,
        "decode_status": "refused",
        "decoded_cells": [],
    },
    {
        "step": 125,
        "kind": "finalizer",
        "program_index": 125,
        "changed_data_bits": 3,
        "decode_status": "decoded",
        "decoded_cells": [EXPECTED_CELL],
    },
]

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(canonical_json(value).encode()).hexdigest()


def source_keys() -> list[int]:
    banks, links = C719.B.chain_genesis(C719.BANKS)
    initial = sum(
        int(bit) << wire
        for wire, bit in enumerate(C719.M.pack_state(banks, links, matter=1))
    )
    state = C719.C713.apply_sparse_word(
        {initial: 1.0 + 0.0j}, C719.MATTER_WORD
    )
    return sorted(state)


def mode_of(source: int) -> int:
    return (source & 4095).bit_length() - 1


def controller_registers(value: int) -> dict[str, object]:
    stations = C719.CONTROLLER_STATIONS
    return {
        "data": value & C719.CONTROLLER_DATA_MASK,
        "A": [
            (value >> (C719.CONTROLLER_A_BASE + index)) & 1
            for index in range(stations)
        ],
        "B": [
            (value >> (C719.CONTROLLER_B_BASE + index)) & 1
            for index in range(stations)
        ],
        "work": [
            (value >> (C719.CONTROLLER_WORK_BASE + index)) & 1
            for index in range(stations)
        ],
    }


def api_decode(data_basis: int) -> tuple[str, list[dict[str, object]]]:
    bits = tuple(
        (data_basis >> wire) & 1
        for wire in range(C719.M.R12.TOTAL_WIRES)
    )
    banks, links = C719.M.unpack_state(bits, C719.BANKS)
    try:
        chain, _order = C719.B.decode_local_graph(banks, links)
    except ValueError:
        return "refused", []
    return "decoded", [asdict(cell) for cell in chain.cells]


def trace_source(source: int, word: tuple[tuple[int, ...], ...]) -> dict[str, object]:
    full = source | (1 << C719.CONTROLLER_A_BASE)
    start = full
    transitions: list[dict[str, object]] = []
    for step in range(C719.CONTROLLER_STATIONS):
        before = controller_registers(full)
        live = [index for index, bit in enumerate(before["A"]) if bit]
        program_index = live[0] if len(live) == 1 else -1
        kind = (
            C719.PROGRAM[program_index][0]
            if program_index >= 0
            else "invalid-token-sector"
        )
        full = C719.apply_fast_int(full, word)
        after = controller_registers(full)
        before_data = int(before["data"])
        after_data = int(after["data"])
        if before_data == after_data:
            continue
        decode_status, cells = api_decode(after_data)
        transitions.append({
            "step": step,
            "kind": kind,
            "program_index": program_index,
            "changed_data_bits": (before_data ^ after_data).bit_count(),
            "decode_status": decode_status,
            "decoded_cells": cells,
        })

    final = controller_registers(full)
    final_status, final_cells = api_decode(int(final["data"]))
    restored = full
    inverse_word = tuple(reversed(word))
    for _step in range(C719.CONTROLLER_STATIONS):
        restored = C719.apply_fast_int(restored, inverse_word)
    expected_a = [1] + [0] * (C719.CONTROLLER_STATIONS - 1)
    return {
        "mode": mode_of(source),
        "transitions": transitions,
        "final_decode_status": final_status,
        "final_cells": final_cells,
        "cleanup": {
            "A0_return": final["A"] == expected_a,
            "B_vacuum_return": not any(final["B"]),
            "work_return": not any(final["work"]),
        },
        "inverse_exact": restored == start,
    }


def trace_payload(
    word: tuple[tuple[int, ...], ...] = C719.CONTROLLER_H_FAST,
    selected_sources: list[int] | None = None,
) -> dict[str, object]:
    sources = source_keys() if selected_sources is None else selected_sources
    rows = [trace_source(source, word) for source in sources]
    return {"modes": [row["mode"] for row in rows], "rows": rows}


def trace_contract(payload: dict[str, object]) -> bool:
    rows = payload["rows"]
    mode6 = next(row for row in rows if row["mode"] == 6)
    other = [row for row in rows if row["mode"] != 6]
    cleanup = {"A0_return": True, "B_vacuum_return": True, "work_return": True}
    return (
        payload["modes"] == EXPECTED_MODES
        and all(row["transitions"] == [] for row in other)
        and all(row["final_cells"] == [] for row in other)
        and mode6["transitions"] == EXPECTED_TRANSITIONS
        and mode6["final_decode_status"] == "decoded"
        and mode6["final_cells"] == [EXPECTED_CELL]
        and all(row["cleanup"] == cleanup for row in rows)
        and all(row["inverse_exact"] for row in rows)
    )


def word_with_deleted_program_row(index: int) -> tuple[tuple[int, ...], ...]:
    program = list(C719.PROGRAM)
    _kind, local_index, _word = program[index]
    program[index] = ("identity", local_index, ())
    semantic = C719.K.controller_word(
        tuple(program), C719.CONTROLLER_DATA_WIDTH
    )
    return C719.fast_classical_word(semantic)


def main() -> int:
    expected_inputs = (NOTE_PATH,) + C719.AUDIT_INPUT_PATHS
    input_declaration_exact = (
        AUDIT_INPUT_PATHS == expected_inputs
        and len(AUDIT_INPUT_PATHS) == 65
        and len(set(AUDIT_INPUT_PATHS)) == 65
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
    )

    first = trace_payload()
    second = trace_payload()
    sources = source_keys()
    mode6_source = [source for source in sources if mode_of(source) == 6]
    mutation_rows = {}
    for label, index in (("source", 0), ("bank", 1), ("finalizer", 125)):
        mutated = trace_payload(
            word_with_deleted_program_row(index), mode6_source
        )
        mutation_rows[label] = {
            "program_index": index,
            "trace_changed": mutated["rows"][0]
            != next(row for row in first["rows"] if row["mode"] == 6),
        }

    mode6 = next(row for row in first["rows"] if row["mode"] == 6)
    altered_cell = dict(EXPECTED_CELL)
    altered_cell["rotor"] ^= 1
    checks = {
        "declared_inputs_exact": input_declaration_exact,
        "six_support_modes_exact": first["modes"] == EXPECTED_MODES,
        "five_empty_traces_exact": all(
            row["transitions"] == [] and row["final_cells"] == []
            for row in first["rows"] if row["mode"] != 6
        ),
        "mode6_transition_contract_exact": (
            mode6["transitions"] == EXPECTED_TRANSITIONS
        ),
        "final_api_cell_exact": mode6["final_cells"] == [EXPECTED_CELL],
        "register_cleanup_exact": all(
            all(row["cleanup"].values()) for row in first["rows"]
        ),
        "inverse_exact_all_six": all(
            row["inverse_exact"] for row in first["rows"]
        ),
        "deterministic_trace": first == second and digest(first) == digest(second),
        "source_bank_finalizer_deletions_active": all(
            row["trace_changed"] for row in mutation_rows.values()
        ),
        "expected_field_mutation_detected": mode6["final_cells"] != [altered_cell],
        "full_contract": trace_contract(first),
    }
    for label, condition in checks.items():
        check(label, condition)

    report = {
        "authority": "none",
        "audit": "unset",
        "claim_type": "bounded_theorem",
        "checks": checks,
        "mutations": mutation_rows,
        "trace_sha256": digest(first),
    }
    print("TRACE_JSON", canonical_json(first))
    print("REPORT_JSON", canonical_json(report))
    print("SUMMARY", {"PASS": PASS, "FAIL": FAIL})
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
