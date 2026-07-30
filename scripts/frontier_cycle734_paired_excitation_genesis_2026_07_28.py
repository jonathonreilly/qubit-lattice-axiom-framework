#!/usr/bin/env python3
"""Cycle 734: an externally positioned translation-covariant pair template.

On the held ring-11 register, one three-gate template creates adjacent
controller excitations and their one-edge reference segment from the blank
state.  The application position remains an explicit supplied parameter.
Cycle 731's public compiler is reused with expected_count=2, and the h=0/B=0
static sector is recounted.

The adjacent pair is also probed against the current Cycle-731 composition's
inherited Cycle-724 radius-one guard.  This records one guard-specific finite
observation; it is not a Cycle-719 exclusion result or a multi-token no-go.
"""
from __future__ import annotations

import ast
from hashlib import sha256
import inspect
import json
from pathlib import Path
import sys
from time import perf_counter

import frontier_cycle734_paired_excitation_independent_check_2026_07_28 as INDEPENDENT_CHECK
import frontier_cycle732_genesis_word_self_verification_2026_07_28 as G732
import frontier_cycle731_token_count_certificate_2026_07_28 as C731
import frontier_cycle724_local_token_row_enforcement_2026_07_28 as C724
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/PAIRED_EXCITATION_GENESIS_CYCLE734_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
SELF_PATH = (
    "scripts/frontier_cycle734_paired_excitation_genesis_2026_07_28.py"
)
INDEPENDENT_PATH = (
    "scripts/frontier_cycle734_paired_excitation_independent_check_2026_07_28.py"
)
DIRECT_INPUT_PATHS = (
    NOTE_PATH,
    INDEPENDENT_PATH,
    "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/GENESIS_WORD_SELF_VERIFICATION_CYCLE732_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py",
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
AUDIT_INPUT_PATHS = (
    "docs/CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md",
    "docs/GENESIS_WORD_SELF_VERIFICATION_CYCLE732_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md",
    "docs/PAIRED_EXCITATION_GENESIS_CYCLE734_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/PHYSICAL_CYCLE704_FSWAP_ENDPOINT_CUBE_BRIDGE_CYCLE708_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_SPATIAL_ACK_CYCLE612_INTERVAL_BRIDGE_CYCLE718_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/RECURRENT_DIRECTIONAL_PACKET_BANK_CYCLE715_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/REFUSAL_WRAPPED_CONTROLLER_CYCLE723_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/work_history/repo/review_feedback/CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md",
    "docs/work_history/repo/review_feedback/INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
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
    "scripts/frontier_cycle709_local_seam_clifford_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_independent_route_replay_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py",
    "scripts/frontier_cycle718_carrier_return_core_2026_07_26.py",
    "scripts/frontier_cycle718_cycle612_interval_bridge_2026_07_26.py",
    "scripts/frontier_cycle718_cycle713_carrier_return_composition_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_export_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py",
    "scripts/frontier_cycle718_three_bank_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle723_refusal_wrapped_controller_2026_07_28.py",
    "scripts/frontier_cycle724_local_token_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle728_bksf_holonomy_compression_2026_07_28.py",
    "scripts/frontier_cycle730_charge_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
    "scripts/frontier_cycle732_genesis_independent_check_2026_07_28.py",
    "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py",
    "scripts/frontier_cycle734_paired_excitation_independent_check_2026_07_28.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/infinite_reversible_record_export_qca_cycle11_2026_07_14.py",
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
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

RING_STATIONS = 11
FIXTURE_BANKS = 2
EXPECTED_COUNT = 2
EXPECTED_PAIR_GATES = 3
EXPECTED_PAIR_POSITION0_SHA256 = (
    "475fd2363c92ddd7cde5d45790c5602eab56566e744f49fe098ea0345009a9df"
)
EXPECTED_COUNT2_CONTROLLER_GATES = 11_206
EXPECTED_COUNT2_CONTROLLER_SHA256 = (
    "3c1316fc5e83112093ed7bca9d61779d4a90a9ba5265fc8d2145b65be6c902a3"
)
EXPECTED_CYCLE732_COMPOSED_GATES = 123_293
EXPECTED_CYCLE732_COMPOSED_SHA256 = (
    "23ad4b292a23095afdffd7337059a4276cf87d2c00a0670f63c4a1269e02194d"
)
EXPECTED_PAIR_CONTROLLER_OUTPUT_SHA256 = (
    "10d40bdc3e9e367d1e3569abbf4e97c4dceef85a5253653a257ddc3ede96c87c"
)
STDOUT_LIMIT_BYTES = 150 * 1024
REPO_ROOT = Path(__file__).resolve().parents[1]

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def tuple_to_int(bits: tuple[int, ...]) -> int:
    return sum(int(bit) << wire for wire, bit in enumerate(bits))


def tuple_to_mask(bits: tuple[int, ...]) -> int:
    return sum(int(bit) << station for station, bit in enumerate(bits))


def declared_input_closure(
    direct_paths: tuple[str, ...],
) -> tuple[str, ...]:
    """Recover recursive literal input declarations, excluding this runner."""

    seen: set[str] = set()
    pending = list(direct_paths)
    while pending:
        relative = pending.pop()
        if relative == SELF_PATH or relative in seen:
            continue
        path = REPO_ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        seen.add(relative)
        if not (relative.startswith("scripts/") and relative.endswith(".py")):
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        nested: tuple[str, ...] = ()
        for node in tree.body:
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            targets = (
                node.targets if isinstance(node, ast.Assign) else (node.target,)
            )
            if not any(
                isinstance(target, ast.Name)
                and target.id == "AUDIT_INPUT_PATHS"
                for target in targets
            ):
                continue
            value = ast.literal_eval(node.value)
            if (
                not isinstance(value, (tuple, list))
                or not value
                or not all(isinstance(item, str) for item in value)
            ):
                raise ValueError(("invalid AUDIT_INPUT_PATHS", relative))
            nested = tuple(value)
            break
        pending.extend(nested)
    return tuple(sorted(seen))


def input_contract_certificate() -> dict[str, object]:
    recovered = declared_input_closure(DIRECT_INPUT_PATHS)
    all_exist = all((REPO_ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
    missing_rejected = False
    try:
        declared_input_closure(
            DIRECT_INPUT_PATHS
            + ("scripts/__cycle734_missing_input_control__.py",)
        )
    except FileNotFoundError:
        missing_rejected = True

    def digest(paths: tuple[str, ...], replacement: bytes | None = None) -> str:
        output = sha256()
        mutation_path = (
            "scripts/"
            "frontier_cycle719_local_handshake_controller_core_2026_07_26.py"
        )
        for relative in paths:
            payload = (REPO_ROOT / relative).read_bytes()
            if replacement is not None and relative == mutation_path:
                payload = replacement
            output.update(relative.encode())
            output.update(b"\0")
            output.update(payload)
            output.update(b"\0")
        return output.hexdigest()

    mutation_path = (
        REPO_ROOT
        / "scripts"
        / "frontier_cycle719_local_handshake_controller_core_2026_07_26.py"
    )
    payload = mutation_path.read_bytes()
    base_digest = digest(recovered)
    mutated_digest = digest(recovered, payload + b"\n# mutation control\n")
    required_parent_notes = (
        "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
        "docs/LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md",
        "docs/CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md",
        "docs/TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md",
        "docs/GENESIS_WORD_SELF_VERIFICATION_CYCLE732_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    )
    return {
        "declared_count": len(AUDIT_INPUT_PATHS),
        "recovered_count": len(recovered),
        "exact_recursive_closure": recovered == AUDIT_INPUT_PATHS,
        "all_exist": all_exist,
        "note_in_closure": NOTE_PATH in recovered,
        "independent_runner_in_closure": INDEPENDENT_PATH in recovered,
        "independent_runner_registered":
            INDEPENDENT_CHECK.SELF_PATH == INDEPENDENT_PATH,
        "all_parent_notes_in_closure":
            all(path in recovered for path in required_parent_notes),
        "missing_path_rejected": missing_rejected,
        "transitive_mutation_changes_digest":
            base_digest != mutated_digest,
        "input_manifest_sha256": base_digest,
    }


def occupied_sites(bits: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(station for station, bit in enumerate(bits) if bit)


def pair_creation_word(
    layout: dict[str, int], position: int
) -> tuple[object, ...]:
    """Three fixed X placements; position is external and state is not read."""

    stations = layout["stations"]
    return (
        K.A.x(layout["a_base"] + position % stations),
        K.A.x(layout["a_base"] + (position + 1) % stations),
        K.A.x(layout["ref_base"] + (position + 1) % stations),
    )


def pair_expected_value(layout: dict[str, int], position: int) -> int:
    stations = layout["stations"]
    following = (position + 1) % stations
    return (
        (1 << (layout["a_base"] + position % stations))
        | (1 << (layout["a_base"] + following))
        | (1 << (layout["ref_base"] + following))
    )


def translate_ring_wire(
    wire: int, layout: dict[str, int], shift: int
) -> int:
    stations = layout["stations"]
    for key in (
        "a_base",
        "b_base",
        "work_base",
        "syndrome_base",
        "ref_base",
        "charge_base",
    ):
        base = layout[key]
        if base <= wire < base + stations:
            return base + ((wire - base + shift) % stations)
    return wire


def conjugate_pair_word_by_translation(
    word: tuple[object, ...],
    layout: dict[str, int],
    shift: int,
) -> tuple[object, ...]:
    """Passive ring relabeling T_shift word T_shift^-1."""

    return tuple(
        K.A.x(translate_ring_wire(gate.wires[0], layout, shift))
        for gate in word
    )


def charge_syndrome(
    a_mask: int, b_mask: int, refs_mask: int, h: int
) -> int:
    return int(
        C731.E730.F728.twisted_local_syndrome_mask(
            a_mask,
            b_mask,
            refs_mask,
            h,
            RING_STATIONS,
        )
    )


def pair_word_exactness_certificate(
    layout: dict[str, int],
) -> dict[str, object]:
    rows_out = []
    failures = []
    for position in range(RING_STATIONS):
        word = pair_creation_word(layout, position)
        observed = C731.literal_apply(
            (0,), word, layout["full_width"], 1
        )[0]
        expected = pair_expected_value(layout, position)
        rows = C731.controller_rows(observed, layout)
        a_mask = tuple_to_mask(rows["A"])
        b_mask = tuple_to_mask(rows["B"])
        refs_mask = tuple_to_mask(rows["refs"])
        syndrome = charge_syndrome(
            a_mask, b_mask, refs_mask, int(rows["h"])
        )
        following = (position + 1) % RING_STATIONS
        conditions = {
            "bit_exact": observed == expected,
            "data_blank": rows["data"] == 0,
            "A_pair":
                occupied_sites(rows["A"]) == (position, following)
                if position < following
                else occupied_sites(rows["A"]) == (following, position),
            "B_work_blank":
                not any(rows["B"]) and not any(rows["work"]),
            "reference_segment":
                occupied_sites(rows["refs"]) == (following,),
            "h_zero": rows["h"] == 0,
            "token_count_two": sum(rows["A"]) == EXPECTED_COUNT,
            "even_parity":
                (sum(rows["A"]) + sum(rows["B"])) % 2 == rows["h"],
            "charge_rows_lawful": syndrome == 0,
            "auxiliaries_clean": C731.all_auxiliary_clean(rows),
        }
        if not all(conditions.values()):
            failures.append(position)
        rows_out.append(
            {
                "position_parameter": position,
                "A_sites": occupied_sites(rows["A"]),
                "reference_sites": occupied_sites(rows["refs"]),
                "h": rows["h"],
                "charge_syndrome_mask": syndrome,
                "bit_exact": conditions["bit_exact"],
                "word_sha256": K.gate_digest(word),
            }
        )
    base_word = pair_creation_word(layout, 0)
    return {
        "stations": RING_STATIONS,
        "initial_state": "all blank",
        "adjacent_pair_convention": (
            "positive-oriented pair (position, position+1 mod 11), "
            "with reference segment at position+1 and h=0"
        ),
        "semantic_gates": len(base_word),
        "gate_census": {
            kind: sum(gate.kind == kind for gate in base_word)
            for kind in ("X", "CNOT", "TOF")
        },
        "position0_word_sha256": K.gate_digest(base_word),
        "expected_position0_word_sha256":
            EXPECTED_PAIR_POSITION0_SHA256,
        "positions": tuple(rows_out),
        "failure_positions": tuple(failures),
        "all_positions_bit_exact_and_lawful":
            not failures and len(rows_out) == RING_STATIONS,
    }


def translation_covariance_certificate(
    layout: dict[str, int],
) -> dict[str, object]:
    failures = []
    identities = 0
    for position in range(RING_STATIONS):
        source = pair_creation_word(layout, position)
        for shift in range(RING_STATIONS):
            conjugated = conjugate_pair_word_by_translation(
                source, layout, shift
            )
            translated = pair_creation_word(
                layout, (position + shift) % RING_STATIONS
            )
            identities += 1
            if conjugated != translated:
                failures.append((position, shift))
    base = pair_creation_word(layout, 0)
    normalized_failures = tuple(
        position
        for position in range(RING_STATIONS)
        if conjugate_pair_word_by_translation(
            pair_creation_word(layout, position), layout, -position
        )
        != base
    )
    return {
        "identity": (
            "T_shift W(position) T_shift^-1 "
            "= W(position+shift mod 11)"
        ),
        "positions": RING_STATIONS,
        "shifts_per_position": RING_STATIONS,
        "identities_tested": identities,
        "expected_identities": RING_STATIONS ** 2,
        "identity_failures": tuple(failures),
        "translation_normalization_failures": normalized_failures,
        "translation_family_exact": (
            not failures
            and not normalized_failures
            and identities == RING_STATIONS ** 2
        ),
        "covariance_kind": (
            "exact passive conjugation under supplied oriented ring "
            "translation"
        ),
    }


def cycle732_regression_anchor() -> dict[str, object]:
    fixture = G732.declared_fixture()
    word = G732.genesis_word(
        len(fixture["program"]), fixture["layout"]
    )
    composed_word = (
        word
        + fixture["controller_word"] * len(fixture["program"])
    )
    rerun = G732.composed_certificate(fixture, word)
    rerun_keys = (
        "target_accepted",
        "literal_composed_matches_stepwise",
        "data_expected_transition",
        "controller_registers_return",
        "all_auxiliaries_return_clean",
        "literal_reverse_exact",
    )
    return {
        "Cycle732_genesis_gates": len(word),
        "Cycle732_genesis_sha256": K.gate_digest(word),
        "Cycle732_expected_genesis_gates":
            G732.EXPECTED_GENESIS_GATES,
        "Cycle732_expected_genesis_sha256":
            G732.EXPECTED_GENESIS_SHA256,
        "composed_semantic_gates": len(composed_word),
        "expected_composed_semantic_gates":
            EXPECTED_CYCLE732_COMPOSED_GATES,
        "composed_word_sha256": K.gate_digest(composed_word),
        "expected_composed_word_sha256":
            EXPECTED_CYCLE732_COMPOSED_SHA256,
        "composed_pin_match": (
            len(composed_word) == EXPECTED_CYCLE732_COMPOSED_GATES
            and K.gate_digest(composed_word)
            == EXPECTED_CYCLE732_COMPOSED_SHA256
        ),
        "one_lawful_rerun": rerun,
        "one_lawful_rerun_pass": (
            all(bool(rerun[key]) for key in rerun_keys)
            and rerun["transient_refusal_count"] == 0
            and rerun["composed_semantic_gates"]
            == EXPECTED_CYCLE732_COMPOSED_GATES
            and rerun["composed_word_sha256"]
            == EXPECTED_CYCLE732_COMPOSED_SHA256
        ),
    }


def independent_reference_from_q(
    q_mask: int, h: int, stations: int
) -> int:
    """Independent r_0=0 closure recount for the marked-edge charge law."""

    marked = C731.E730.F728.marked_station(stations)
    current = 0
    refs = 0
    closure = 0
    for station in range(stations):
        refs |= current << station
        following = (
            current
            ^ ((q_mask >> station) & 1)
            ^ (h if station == marked else 0)
        )
        if station == stations - 1:
            closure = following
        else:
            current = following
    return refs if closure == 0 else -1


def h0_b0_theorem_recount() -> dict[str, object]:
    rail_states = 1 << RING_STATIONS
    parity_pass = 0
    count_pass = 0
    full_pass = 0
    exceptions = 0
    recurrence_failures = 0
    pair_pass = 0
    outcome = bytearray()
    adjacent_masks = {
        (1 << position) | (1 << ((position + 1) % RING_STATIONS))
        for position in range(RING_STATIONS)
    }
    for a_mask in range(rail_states):
        refs = independent_reference_from_q(
            a_mask, 0, RING_STATIONS
        )
        charge_law = refs >= 0
        count_law = a_mask.bit_count() == EXPECTED_COUNT
        expected_charge = a_mask.bit_count() % 2 == 0
        static_conjunction = count_law and charge_law
        expected_static = (
            a_mask.bit_count() == EXPECTED_COUNT
            and a_mask.bit_count() % 2 == 0
        )
        parity_pass += charge_law
        count_pass += count_law
        full_pass += static_conjunction
        exceptions += charge_law != expected_charge
        exceptions += static_conjunction != expected_static
        pair_pass += a_mask in adjacent_masks and static_conjunction
        if charge_law:
            recurrence_failures += charge_syndrome(
                a_mask, 0, refs, 0
            ) != 0
        outcome.append(
            int(count_law)
            | (int(charge_law) << 1)
            | (int(static_conjunction) << 2)
            | (int(expected_static) << 3)
        )
    return {
        "ring_stations": RING_STATIONS,
        "sector": "all A masks, B=0, h=0",
        "cases": rail_states,
        "expected_cases": 2_048,
        "count2_pass_cases": count_pass,
        "expected_count2_pass_cases": 55,
        "even_parity_charge_pass_cases": parity_pass,
        "expected_even_parity_charge_pass_cases": 1_024,
        "static_count2_and_charge_pass_cases": full_pass,
        "expected_static_count2_and_charge_pass_cases": 55,
        "adjacent_pair_masks": len(adjacent_masks),
        "adjacent_pair_pass_cases": pair_pass,
        "iff_exceptions": exceptions,
        "charge_recurrence_failures": recurrence_failures,
        "outcome_table_sha256": sha256(outcome).hexdigest(),
        "static_count_and_charge_law": (
            "A_count=2 AND popcount(A) mod 2=h in the B=0,h=0 "
            "sector"
        ),
    }


def count2_enforcement_certificate(
    layout: dict[str, int],
) -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    word, built_layout, _blocks, metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, EXPECTED_COUNT
        )
    )
    if built_layout != layout:
        raise AssertionError(("layout disagreement", built_layout, layout))

    comparison_stop = int(metadata["comparison_compute_stop"])
    prefix = word[:comparison_stop]
    pair_sources = tuple(
        pair_expected_value(layout, position)
        for position in range(RING_STATIONS)
    )
    compared_pairs = C731.literal_apply(
        pair_sources, prefix, layout["full_width"], 1
    )
    restored_pairs = C731.literal_apply(
        compared_pairs,
        tuple(reversed(prefix)),
        layout["full_width"],
        1,
    )
    pair_rows = tuple(
        C731.controller_rows(value, layout)
        for value in compared_pairs
    )
    pair_acceptance = tuple(
        {
            "position": position,
            "counter_value": tuple_to_mask(rows["counter"]),
            "refusal_latch": rows["refusal_latch"],
            "accepted":
                tuple_to_mask(rows["counter"]) == EXPECTED_COUNT
                and rows["refusal_latch"] == 0,
            "prefix_reverse_exact":
                restored_pairs[position] == pair_sources[position],
        }
        for position, rows in enumerate(pair_rows)
    )

    witness_counts = (0, 1, 3, 4)
    witness_sources = []
    witness_specs = []
    for count in witness_counts:
        a_mask = (1 << count) - 1
        h = count & 1
        refs = C731.canonical_refs(
            a_mask, 0, h, RING_STATIONS
        )
        witness_sources.append(
            C731.controller_full_input(
                0,
                layout,
                a=tuple(range(count)),
                refs=refs,
                h=h,
            )
        )
        witness_specs.append((count, h, tuple_to_mask(refs)))
    compared_witnesses = C731.literal_apply(
        tuple(witness_sources),
        prefix,
        layout["full_width"],
        1,
    )
    refused_rows = []
    for specification, value in zip(
        witness_specs, compared_witnesses
    ):
        count, h, refs_mask = specification
        rows = C731.controller_rows(value, layout)
        refused_rows.append(
            {
                "A_count": count,
                "h": h,
                "canonical_refs_mask": refs_mask,
                "charge_syndrome_mask":
                    charge_syndrome(
                        (1 << count) - 1, 0, refs_mask, h
                    ),
                "counter_value": tuple_to_mask(rows["counter"]),
                "refusal_latch": rows["refusal_latch"],
                "count_refused": rows["refusal_latch"] == 1,
            }
        )

    certificate_ref_h_wires = set(
        range(
            layout["ref_base"],
            layout["ref_base"] + RING_STATIONS,
        )
    )
    certificate_ref_h_wires.add(layout["h_wire"])
    ref_h_touch_failures = sum(
        any(wire in certificate_ref_h_wires for wire in gate.wires)
        for gate in metadata["certificate_word"]
    )
    comparison2 = tuple(metadata["comparison_compute_word"])
    theorem = h0_b0_theorem_recount()
    return {
        "compiler_api": (
            "C731.count_certified_controller_build("
            "program, DATA_WIDTH, expected_count=2)"
        ),
        "reused_parameterized_public_api": True,
        "expected_count": EXPECTED_COUNT,
        "stations": len(program),
        "counter_width": layout["counter_width"],
        "controller_semantic_gates": len(word),
        "expected_controller_semantic_gates":
            EXPECTED_COUNT2_CONTROLLER_GATES,
        "controller_word_sha256": K.gate_digest(word),
        "expected_controller_word_sha256":
            EXPECTED_COUNT2_CONTROLLER_SHA256,
        "comparison_stage_matches_public_constructor":
            comparison2
            == C731.comparison_compute_word(layout, EXPECTED_COUNT),
        "comparison_stage_differs_from_expected_count1":
            comparison2 != C731.comparison_compute_word(layout, 1),
        "certificate_ref_h_touch_failures": ref_h_touch_failures,
        "count_comparison_does_not_write_reference_or_h":
            ref_h_touch_failures == 0,
        "pair_acceptance": pair_acceptance,
        "all_11_templates_count_prefix_accepted": all(
            row["accepted"] and row["prefix_reverse_exact"]
            for row in pair_acceptance
        ),
        "refused_count_witnesses": tuple(refused_rows),
        "all_0_1_3_4_count_witnesses_refused": all(
            row["count_refused"] for row in refused_rows
        ),
        "witness_charge_rows_lawful": all(
            row["charge_syndrome_mask"] == 0
            for row in refused_rows
        ),
        "h0_B0_ring11_recount": theorem,
    }


def supplied_position_template_certificate(
    layout: dict[str, int],
) -> dict[str, object]:
    tree = ast.parse(inspect.getsource(pair_creation_word))
    function = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
        and node.name == "pair_creation_word"
    )
    branch_nodes = tuple(
        type(node).__name__
        for node in ast.walk(function)
        if isinstance(
            node,
            (
                ast.If,
                ast.IfExp,
                ast.For,
                ast.While,
                ast.Match,
                ast.Try,
                ast.ListComp,
                ast.SetComp,
                ast.DictComp,
                ast.GeneratorExp,
            ),
        )
    )
    integer_constants = tuple(
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, int)
        and not isinstance(node.value, bool)
    )
    arguments = tuple(arg.arg for arg in function.args.args)
    state_names = {
        "data",
        "input",
        "state",
        "value",
        "basis",
        "bits",
    }
    runtime_state_parameters = tuple(
        argument for argument in arguments if argument in state_names
    )
    position_loads = sum(
        isinstance(node, ast.Name)
        and node.id == "position"
        and isinstance(node.ctx, ast.Load)
        for node in ast.walk(function)
    )
    base_word = pair_creation_word(layout, 0)
    all_words = tuple(
        pair_creation_word(layout, position)
        for position in range(RING_STATIONS)
    )
    gate_census = {
        kind: sum(gate.kind == kind for gate in base_word)
        for kind in ("X", "CNOT", "TOF")
    }
    no_site_constants = (
        set(integer_constants) <= {1}
        and not any(
            site in integer_constants
            for site in range(2, RING_STATIONS)
        )
    )
    return {
        "template_function_parameters": arguments,
        "external_position_parameter": "position" in arguments,
        "runtime_state_parameters": runtime_state_parameters,
        "runtime_branch_or_iteration_nodes": branch_nodes,
        "integer_constants": integer_constants,
        "position_parameter_loads": position_loads,
        "distinguished_site_constants": tuple(
            site
            for site in range(2, RING_STATIONS)
            if site in integer_constants
        ),
        "no_hardcoded_absolute_site": no_site_constants,
        "fixed_unrolling_gate_count": len(base_word),
        "all_position_words_same_size":
            all(len(word) == len(base_word) for word in all_words),
        "gate_census": gate_census,
        "only_literal_M2_X_gates":
            all(
                gate.kind == "X"
                for word in all_words
                for gate in word
            ),
        "orientation_remains_supplied": True,
        "ring_geometry_remains_supplied": True,
        "program_content_order_untouched": True,
        "audit_pass": (
            arguments == ("layout", "position")
            and not runtime_state_parameters
            and not branch_nodes
            and no_site_constants
            and position_loads == 3
            and len(base_word) == EXPECTED_PAIR_GATES
            and all(len(word) == EXPECTED_PAIR_GATES for word in all_words)
            and gate_census
            == {"X": EXPECTED_PAIR_GATES, "CNOT": 0, "TOF": 0}
        ),
    }


def ownership_violations(
    a: tuple[int, ...],
    b: tuple[int, ...],
    work: tuple[int, ...],
) -> tuple[dict[str, object], ...]:
    stations = len(a)
    failures = []
    for station, occupied in enumerate(a):
        if not occupied:
            continue
        left = (station - 1) % stations
        right = (station + 1) % stations
        dirty = {
            "own_B": b[station],
            "own_work": work[station],
            "left_A": a[left],
            "left_B": b[left],
            "right_A": a[right],
            "right_B": b[right],
        }
        reasons = tuple(key for key, bit in dirty.items() if bit)
        if reasons:
            failures.append(
                {
                    "station": station,
                    "left": left,
                    "right": right,
                    "reasons": reasons,
                }
            )
    return tuple(failures)


def controller_two_token_probe(
    layout: dict[str, int],
) -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    data = K.M.prepare_endpoint(
        K.M.pack_state(banks, links), (1, 0)
    )
    expected_one = K.A.apply_semantic(
        data, K.M.global_allocator_word(FIXTURE_BANKS)
    )
    one_output, one_a, one_b, _one_trace = K.run_orbit(
        data, program, token_positions=(0,)
    )
    pair_output, pair_a, pair_b, pair_trace = K.run_orbit(
        data, program, token_positions=(0, 1)
    )
    reverse_output, reverse_a, reverse_b, _reverse_trace = K.run_orbit(
        pair_output,
        program,
        token_positions=(0, 1),
        reverse=True,
    )

    a = (1, 1) + (0,) * (RING_STATIONS - 2)
    b = (0,) * RING_STATIONS
    work = (0,) * RING_STATIONS
    current_data = data
    violation_trace = []
    controller_trace = []
    cycle724_guard_agreement = True
    for step in range(RING_STATIONS):
        violations = ownership_violations(a, b, work)
        cycle724_dirty_sites = tuple(
            station
            for station, occupied in enumerate(a)
            if occupied and C724.local_dirty(a, b, work, station)
        )
        cycle724_guard_agreement = (
            cycle724_guard_agreement
            and cycle724_dirty_sites
            == tuple(row["station"] for row in violations)
        )
        violation_trace.append(
            {
                "step": step,
                "A_sites": occupied_sites(a),
                "B_sites": occupied_sites(b),
                "Cycle724_dirty_occupied_sites": cycle724_dirty_sites,
                "violations": violations,
            }
        )
        before_a = occupied_sites(a)
        current_data, a, b = K.apply_controller_step(
            current_data, program, a, b
        )
        controller_trace.append(
            {
                "step": step,
                "A_before": before_a,
                "A_after": occupied_sites(a),
                "B_after": occupied_sites(b),
            }
        )

    single_token_violations = sum(
        len(
            ownership_violations(
                tuple(
                    int(index == position)
                    for index in range(RING_STATIONS)
                ),
                (0,) * RING_STATIONS,
                (0,) * RING_STATIONS,
            )
        )
        for position in range(RING_STATIONS)
    )

    count_word, count_layout, blocks, metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, EXPECTED_COUNT
        )
    )
    if count_layout != layout:
        raise AssertionError(("probe layout", count_layout, layout))
    data_value = tuple_to_int(data)
    pair_source = C731.controller_full_input(
        data_value,
        layout,
        a=(0, 1),
        refs=tuple(int(station == 1) for station in range(RING_STATIONS)),
        h=0,
    )
    comparison_value = C731.literal_apply(
        (pair_source,),
        count_word[:int(metadata["comparison_compute_stop"])],
        layout["full_width"],
        1,
    )[0]
    comparison_rows = C731.controller_rows(
        comparison_value, layout
    )
    syndrome_probes = []
    for station in (0, 1):
        probe_value = C731.literal_apply(
            (pair_source,),
            count_word[:int(blocks[station]["or_compute_stop"])],
            layout["full_width"],
            1,
        )[0]
        probe_rows = C731.controller_rows(probe_value, layout)
        syndrome_probes.append(
            {
                "step": 0,
                "station": station,
                "syndrome": probe_rows["syndrome"][station],
                "reason":
                    "neighboring A ownership uniqueness violation",
            }
        )
    enforced_value = C731.literal_apply(
        (pair_source,), count_word, layout["full_width"], 1
    )[0]
    enforced_rows = C731.controller_rows(enforced_value, layout)

    pair_output_sha = sha256(repr(pair_output).encode()).hexdigest()
    total_violations = sum(
        len(row["violations"]) for row in violation_trace
    )
    first = violation_trace[0]
    guard_witness = {
        "name": "ownership_uniqueness_at_adjacent_Q_sites",
        "guard_layer": (
            "Cycle724 radius-one Q guard inherited by the Cycle731 "
            "composition"
        ),
        "invariant": (
            "an occupied A station requires own B/work and both "
            "neighboring A/B rails blank at the Q boundary"
        ),
        "first_step": first["step"],
        "first_stations": tuple(
            row["station"] for row in first["violations"]
        ),
        "minimal_reproducing_census": {
            "ring_stations": RING_STATIONS,
            "A_count": 2,
            "A_sites": first["A_sites"],
            "B_count": len(first["B_sites"]),
            "work_count": 0,
            "single_token_control_violations":
                single_token_violations,
        },
        "count2_comparison_accepts":
            tuple_to_mask(comparison_rows["counter"])
            == EXPECTED_COUNT
            and comparison_rows["refusal_latch"] == 0,
        "local_syndrome_probes": tuple(syndrome_probes),
        "all_11_steps_dirty_at_two_occupied_sites":
            total_violations == 2 * RING_STATIONS,
        "Cycle724_guard_agrees_with_local_recount":
            cycle724_guard_agreement,
        "bare_Cycle719_pair_output_sha256": pair_output_sha,
        "expected_bare_Cycle719_pair_output_sha256":
            EXPECTED_PAIR_CONTROLLER_OUTPUT_SHA256,
    }
    guard_witness_exact = (
        guard_witness["first_step"] == 0
        and guard_witness["first_stations"] == (0, 1)
        and guard_witness["minimal_reproducing_census"]["A_count"] == 2
        and guard_witness["minimal_reproducing_census"]["A_sites"] == (0, 1)
        and guard_witness["minimal_reproducing_census"]["B_count"] == 0
        and guard_witness["minimal_reproducing_census"][
            "single_token_control_violations"
        ]
        == 0
        and guard_witness["count2_comparison_accepts"]
        and all(row["syndrome"] == 1 for row in syndrome_probes)
        and guard_witness["all_11_steps_dirty_at_two_occupied_sites"]
        and guard_witness["Cycle724_guard_agrees_with_local_recount"]
        and pair_output_sha
        == EXPECTED_PAIR_CONTROLLER_OUTPUT_SHA256
    )
    return {
        "outcome": "inherited_guard_witness",
        "bare_Cycle719_single_token_reference": {
            "full_orbit_equals_global_allocator_word":
                one_output == expected_one,
            "A_token_returns": one_a
            == (1,) + (0,) * (RING_STATIONS - 1),
            "B_rail_returns_blank": not any(one_b),
        },
        "bare_Cycle719_two_token_observations": {
            "token_count_conserved":
                sum(pair_a) + sum(pair_b) == EXPECTED_COUNT,
            "A_pair_returns": pair_a
            == (1, 1) + (0,) * (RING_STATIONS - 2),
            "B_rail_returns_blank": not any(pair_b),
            "literal_reverse_restores_data": reverse_output == data,
            "literal_reverse_restores_A": reverse_a == pair_a,
            "literal_reverse_restores_B": reverse_b == pair_b,
            "pair_output_differs_from_one_token_law":
                pair_output != expected_one,
            "pair_output_sha256": pair_output_sha,
            "K_run_orbit_trace": pair_trace,
            "direct_step_trace": tuple(controller_trace),
            "direct_steps_match_K_run_orbit":
                current_data == pair_output
                and a == pair_a
                and b == pair_b,
        },
        "Cycle731_expected2_enforcement_reproduction": {
            "comparison_counter":
                tuple_to_mask(comparison_rows["counter"]),
            "comparison_refusal_latch":
                comparison_rows["refusal_latch"],
            "local_syndrome_probes": tuple(syndrome_probes),
            "data_macro_refused":
                enforced_rows["data"] == data_value,
            "A_after_one_R_step":
                occupied_sites(enforced_rows["A"]),
            "B_after_one_R_step":
                occupied_sites(enforced_rows["B"]),
            "all_auxiliaries_return_clean":
                C731.all_auxiliary_clean(enforced_rows),
        },
        "ownership_violation_trace": tuple(violation_trace),
        "inherited_guard_witness": guard_witness,
        "inherited_guard_witness_exact": guard_witness_exact,
        "adjacent_data_macros_executed":
            enforced_rows["data"] != data_value,
    }


def deletion_controls_certificate(
    layout: dict[str, int],
) -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    count_word, _count_layout, _blocks, metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, EXPECTED_COUNT
        )
    )
    prefix = count_word[:int(metadata["comparison_compute_stop"])]
    cases = []
    deleted_outputs = []
    case_specs = []
    for position in range(RING_STATIONS):
        word = pair_creation_word(layout, position)
        expected = pair_expected_value(layout, position)
        for deleted_index in range(len(word)):
            damaged = word[:deleted_index] + word[deleted_index + 1:]
            observed = C731.literal_apply(
                (0,), damaged, layout["full_width"], 1
            )[0]
            deleted_outputs.append(observed)
            case_specs.append(
                (
                    position,
                    deleted_index,
                    word[deleted_index],
                    expected,
                    observed,
                )
            )
    compared = C731.literal_apply(
        tuple(deleted_outputs), prefix, layout["full_width"], 1
    )
    for specification, comparison in zip(case_specs, compared):
        position, deleted_index, deleted_gate, expected, observed = (
            specification
        )
        rows = C731.controller_rows(observed, layout)
        comparison_rows = C731.controller_rows(comparison, layout)
        a_mask = tuple_to_mask(rows["A"])
        b_mask = tuple_to_mask(rows["B"])
        refs_mask = tuple_to_mask(rows["refs"])
        count_ok = sum(rows["A"]) == EXPECTED_COUNT
        parity_ok = (
            sum(rows["A"]) + sum(rows["B"])
        ) % 2 == rows["h"]
        charge_ok = (
            charge_syndrome(
                a_mask, b_mask, refs_mask, int(rows["h"])
            )
            == 0
        )
        reasons = tuple(
            name
            for name, passed in (
                ("count2", count_ok),
                ("h_parity", parity_ok),
                ("charge_rows", charge_ok),
            )
            if not passed
        )
        cases.append(
            {
                "position": position,
                "deleted_gate_index": deleted_index,
                "deleted_gate": (
                    deleted_gate.kind,
                    deleted_gate.wires,
                ),
                "output_changed": observed != expected,
                "count2_comparison_refusal":
                    comparison_rows["refusal_latch"] == 1,
                "law_refusal_reasons": reasons,
                "count_charge_parity_law_refused":
                    not (count_ok and parity_ok and charge_ok),
            }
        )
    return {
        "positions": RING_STATIONS,
        "deletions_per_word": EXPECTED_PAIR_GATES,
        "cases": len(cases),
        "expected_cases": RING_STATIONS * EXPECTED_PAIR_GATES,
        "output_change_detections": sum(
            row["output_changed"] for row in cases
        ),
        "count2_comparison_refusals": sum(
            row["count2_comparison_refusal"] for row in cases
        ),
        "count_charge_parity_law_refusals": sum(
            row["count_charge_parity_law_refused"]
            for row in cases
        ),
        "case_census": tuple(cases),
        "every_deletion_detected_and_refused": (
            len(cases) == RING_STATIONS * EXPECTED_PAIR_GATES
            and all(
                row["output_changed"]
                and row["count_charge_parity_law_refused"]
                for row in cases
            )
        ),
    }


def main() -> int:
    started = perf_counter()
    program = K.interleaved_program(FIXTURE_BANKS)
    _count_word, layout, _blocks, _metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, EXPECTED_COUNT
        )
    )

    anchor = cycle732_regression_anchor()
    check(
        "A_Cycle732_regression_anchor",
        anchor["Cycle732_genesis_gates"]
        == anchor["Cycle732_expected_genesis_gates"]
        and anchor["Cycle732_genesis_sha256"]
        == anchor["Cycle732_expected_genesis_sha256"]
        and anchor["composed_pin_match"]
        and anchor["one_lawful_rerun_pass"],
    )

    exactness = pair_word_exactness_certificate(layout)
    check(
        "B_pair_word_exactness",
        exactness["semantic_gates"] == EXPECTED_PAIR_GATES
        and exactness["position0_word_sha256"]
        == exactness["expected_position0_word_sha256"]
        and exactness["gate_census"]
        == {"X": EXPECTED_PAIR_GATES, "CNOT": 0, "TOF": 0}
        and exactness["all_positions_bit_exact_and_lawful"],
    )

    covariance = translation_covariance_certificate(layout)
    check(
        "C_translation_covariance",
        covariance["identities_tested"]
        == covariance["expected_identities"]
        and not covariance["identity_failures"]
        and not covariance["translation_normalization_failures"]
        and covariance["translation_family_exact"],
    )

    enforcement = count2_enforcement_certificate(layout)
    theorem = enforcement["h0_B0_ring11_recount"]
    check(
        "D_count2_enforcement",
        enforcement["reused_parameterized_public_api"]
        and enforcement["controller_semantic_gates"]
        == enforcement["expected_controller_semantic_gates"]
        and enforcement["controller_word_sha256"]
        == enforcement["expected_controller_word_sha256"]
        and enforcement["comparison_stage_matches_public_constructor"]
        and enforcement["comparison_stage_differs_from_expected_count1"]
        and enforcement["certificate_ref_h_touch_failures"] == 0
        and enforcement[
            "count_comparison_does_not_write_reference_or_h"
        ]
        and enforcement["all_11_templates_count_prefix_accepted"]
        and enforcement["all_0_1_3_4_count_witnesses_refused"]
        and enforcement["witness_charge_rows_lawful"]
        and theorem["cases"] == theorem["expected_cases"]
        and theorem["count2_pass_cases"]
        == theorem["expected_count2_pass_cases"]
        and theorem["even_parity_charge_pass_cases"]
        == theorem["expected_even_parity_charge_pass_cases"]
        and theorem["static_count2_and_charge_pass_cases"]
        == theorem["expected_static_count2_and_charge_pass_cases"]
        and theorem["adjacent_pair_pass_cases"]
        == theorem["adjacent_pair_masks"]
        == RING_STATIONS
        and theorem["iff_exceptions"] == 0
        and theorem["charge_recurrence_failures"] == 0,
    )

    template_audit = supplied_position_template_certificate(layout)
    check(
        "E_supplied_position_template_audit",
        template_audit["audit_pass"]
        and template_audit["external_position_parameter"]
        and not template_audit["runtime_state_parameters"]
        and not template_audit["runtime_branch_or_iteration_nodes"]
        and not template_audit["distinguished_site_constants"]
        and template_audit["no_hardcoded_absolute_site"]
        and template_audit["orientation_remains_supplied"]
        and template_audit["ring_geometry_remains_supplied"]
        and template_audit["program_content_order_untouched"],
    )

    controller = controller_two_token_probe(layout)
    single_reference = controller["bare_Cycle719_single_token_reference"]
    bare_pair = controller["bare_Cycle719_two_token_observations"]
    enforced_probe = controller[
        "Cycle731_expected2_enforcement_reproduction"
    ]
    check(
        "F_inherited_guard_and_bare_transport_probe",
        controller["outcome"] == "inherited_guard_witness"
        and not controller["adjacent_data_macros_executed"]
        and all(single_reference.values())
        and bare_pair["token_count_conserved"]
        and bare_pair["A_pair_returns"]
        and bare_pair["B_rail_returns_blank"]
        and bare_pair["literal_reverse_restores_data"]
        and bare_pair["literal_reverse_restores_A"]
        and bare_pair["literal_reverse_restores_B"]
        and bare_pair["pair_output_differs_from_one_token_law"]
        and bare_pair["direct_steps_match_K_run_orbit"]
        and enforced_probe["comparison_counter"] == EXPECTED_COUNT
        and enforced_probe["comparison_refusal_latch"] == 0
        and enforced_probe["data_macro_refused"]
        and enforced_probe["A_after_one_R_step"] == (1, 2)
        and not enforced_probe["B_after_one_R_step"]
        and enforced_probe["all_auxiliaries_return_clean"]
        and controller["inherited_guard_witness_exact"],
    )

    deletions = deletion_controls_certificate(layout)
    check(
        "G_pair_word_deletion_controls",
        deletions["cases"] == deletions["expected_cases"]
        and deletions["output_change_detections"]
        == deletions["expected_cases"]
        and deletions["count_charge_parity_law_refusals"]
        == deletions["expected_cases"]
        and deletions["every_deletion_detected_and_refused"],
    )

    manifest = input_contract_certificate()
    check(
        "I_recursive_input_and_paired_runner_closure",
        manifest["exact_recursive_closure"]
        and manifest["all_exist"]
        and manifest["note_in_closure"]
        and manifest["independent_runner_in_closure"]
        and manifest["independent_runner_registered"]
        and manifest["all_parent_notes_in_closure"]
        and manifest["missing_path_rejected"]
        and manifest["transitive_mutation_changes_digest"],
    )

    no_hardcoded_absolute_site = (
        CHECKS["B_pair_word_exactness"]
        and CHECKS["C_translation_covariance"]
        and CHECKS["E_supplied_position_template_audit"]
    )
    source_selection_remains_supplied = bool(
        template_audit["external_position_parameter"]
    )
    remaining_supplied_components = [
        "external application-position parameter",
        "finite oriented geometry",
        "program content/order",
        "passive-only covariance",
    ]
    exact_supplies = [
        "all-blank Cycle-731 ring-11 register with clean auxiliaries",
        "external application-position parameter p",
        "expected_count=2 comparison parameter",
        "finite oriented ring geometry (11 stations and positive adjacency)",
        "program content/order on the held two-bank fixture",
        "passive ring-translation relabeling/covariance",
        "held two-bank data genesis and direction for the controller probe",
    ]
    guard_boundary: dict[str, object] = {
        "adjacent_data_macros_executed":
            controller["adjacent_data_macros_executed"],
        "inherited_guard_witness":
            controller["inherited_guard_witness"]["name"],
        "guard_layer":
            controller["inherited_guard_witness"]["guard_layer"],
        "invariant":
            controller["inherited_guard_witness"]["invariant"],
        "first_step":
            controller["inherited_guard_witness"]["first_step"],
        "first_stations":
            controller["inherited_guard_witness"]["first_stations"],
        "minimal_reproducing_census":
            controller["inherited_guard_witness"][
                "minimal_reproducing_census"
            ],
    }
    boundary = {
        "no_hardcoded_absolute_site_in_template":
            no_hardcoded_absolute_site,
        "source_selection_remains_supplied":
            source_selection_remains_supplied,
        "guard_observation": guard_boundary,
        "generalized_controller_no_go_claimed": False,
        "remaining_supplied_components": remaining_supplied_components,
        "exact_supplies": exact_supplies,
        "orientation_untouched": True,
        "ring_geometry_untouched": True,
        "pair_position_is_external_parameter": True,
        "claim_scope": (
            "externally positioned translation-covariant logical pair "
            "template, static charge rows, and A-count-two comparator-prefix "
            "behavior on the supplied ring-11 fixture; plus one inherited "
            "Cycle724/Cycle731 adjacent-guard witness"
        ),
    }
    prior_labels = tuple(CHECKS)
    check(
        "H_honest_boundary_keys",
        all(CHECKS[label] for label in prior_labels)
        and boundary["no_hardcoded_absolute_site_in_template"]
        and boundary["source_selection_remains_supplied"]
        and isinstance(boundary["guard_observation"], dict)
        and not boundary["guard_observation"][
            "adjacent_data_macros_executed"
        ]
        and boundary["guard_observation"]["inherited_guard_witness"]
        == "ownership_uniqueness_at_adjacent_Q_sites"
        and not boundary["generalized_controller_no_go_claimed"]
        and boundary["remaining_supplied_components"]
        == [
            "external application-position parameter",
            "finite oriented geometry",
            "program content/order",
            "passive-only covariance",
        ]
        and len(boundary["exact_supplies"]) == 7
        and boundary["orientation_untouched"]
        and boundary["ring_geometry_untouched"]
        and boundary["pair_position_is_external_parameter"],
    )

    elapsed = perf_counter() - started
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
        "pair_word_size": EXPECTED_PAIR_GATES,
        "no_hardcoded_absolute_site_in_template":
            no_hardcoded_absolute_site,
        "source_selection_remains_supplied":
            source_selection_remains_supplied,
        "guard_observation": guard_boundary,
        "remaining_supplied_components": remaining_supplied_components,
        "exact_supplies": exact_supplies,
        "input_contract": manifest,
        "Cycle732_regression_anchor": anchor,
        "pair_word_exactness": exactness,
        "translation_covariance": covariance,
        "count2_enforcement": enforcement,
        "supplied_position_template_audit": template_audit,
        "controller_two_token_probe": controller,
        "pair_word_deletion_controls": deletions,
        "honest_boundary": boundary,
        "terminal": (
            "CYCLE734_PAIRED_EXCITATION_GENESIS_PASS"
            if all(CHECKS.values())
            else "CYCLE734_PAIRED_EXCITATION_GENESIS_HONEST_FAIL"
        ),
    }
    preliminary = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(preliminary.encode()) + 4096 < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE734_PAIRED_EXCITATION_GENESIS_PASS"
        if report["pass"]
        else "CYCLE734_PAIRED_EXCITATION_GENESIS_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(text.encode())))
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
