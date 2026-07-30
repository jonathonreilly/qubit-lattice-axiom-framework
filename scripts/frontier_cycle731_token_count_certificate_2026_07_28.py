#!/usr/bin/env python3
"""Cycle 731: a bounded A-rail occupancy counter/comparator certificate.

A clean binary counter is reversibly incremented once for every occupied
Cycle-719 A station.  A fixed equality comparison with a supplied expected
A-rail occupancy sets one mismatch latch.  That latch is the eighth input to
every Cycle-730 refusal OR.  Comparison and count are then uncomputed before
the unchanged R suffix.  The emitted circuit is a fixed X/CNOT/TOF word:
Python is used only to unroll the word from (ring size, expected occupancy).

The counter is one fixed global logical register.  This runner does not claim
that it is physically transported, that it counts the B rail, or that the
integrated word is a global parity acceptor.
"""
from __future__ import annotations

import ast
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter

import frontier_cycle730_charge_row_enforcement_2026_07_28 as E730
import frontier_cycle724_local_token_row_enforcement_2026_07_28 as E724
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
DIRECT_INPUT_PATHS = (
    NOTE_PATH,
    "scripts/frontier_cycle730_charge_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle724_local_token_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
AUDIT_INPUT_PATHS = (
    "docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md",
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

A = K.A
B = K.B
M = K.M
DATA_WIDTH = E730.DATA_WIDTH
EXPECTED_COUNT = 1
EXPECTED_CYCLE730_PADDED_GATES = 99_310
EXPECTED_CYCLE730_PADDED_SHA256 = (
    "7d4b7fac14c0606f7210a1b99da997cecdf13885471c37d5ae55597b742c5433"
)
COUNT_LOCAL_ROW_INPUTS = 8
COUNT_OR_INTERMEDIATES_PER_STATION = 6
STDOUT_LIMIT_CHARACTERS = 20_000
RING11_STATIONS = 11

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []
REPO_ROOT = Path(__file__).resolve().parents[1]


def declared_input_closure(
    direct_paths: tuple[str, ...],
) -> tuple[str, ...]:
    """Recursively recover literal mutable-input declarations, fail closed."""

    seen: set[str] = set()
    pending = list(direct_paths)
    while pending:
        relative = pending.pop()
        if relative in seen:
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


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def counter_width(stations: int) -> int:
    """Exactly ceil(log2(stations + 1)) for positive station counts."""

    if stations < 1:
        raise ValueError(("stations", stations))
    return stations.bit_length()


def register_layout(data_wires: int, stations: int) -> dict[str, int]:
    width = counter_width(stations)
    mcx_width = max(0, width - 2)
    a_base = data_wires
    b_base = a_base + stations
    work_base = b_base + stations
    syndrome_base = work_base + stations
    scratch_base = syndrome_base + stations
    or_scratch_base = (
        scratch_base + E730.MCX_SCRATCH_PER_STATION * stations
    )
    ref_base = (
        or_scratch_base
        + COUNT_OR_INTERMEDIATES_PER_STATION * stations
    )
    charge_base = ref_base + stations
    h_wire = charge_base + stations
    counter_base = h_wire + 1
    increment_scratch_base = counter_base + width
    comparison_scratch_base = increment_scratch_base + mcx_width
    refusal_latch = comparison_scratch_base + mcx_width
    return {
        "data_width": data_wires,
        "stations": stations,
        "a_base": a_base,
        "b_base": b_base,
        "work_base": work_base,
        "syndrome_base": syndrome_base,
        "scratch_base": scratch_base,
        "or_scratch_base": or_scratch_base,
        "ref_base": ref_base,
        "charge_base": charge_base,
        "h_wire": h_wire,
        "counter_base": counter_base,
        "counter_width": width,
        "increment_scratch_base": increment_scratch_base,
        "increment_scratch_width": mcx_width,
        "comparison_scratch_base": comparison_scratch_base,
        "comparison_scratch_width": mcx_width,
        "refusal_latch": refusal_latch,
        "full_width": refusal_latch + 1,
    }


def station_mcx_scratch(
    layout: dict[str, int], station: int
) -> tuple[int, ...]:
    return tuple(
        layout["scratch_base"]
        + E730.MCX_SCRATCH_PER_STATION * station
        + slot
        for slot in range(E730.MCX_SCRATCH_PER_STATION)
    )


def station_or_scratch(
    layout: dict[str, int], station: int
) -> tuple[int, ...]:
    return tuple(
        layout["or_scratch_base"]
        + COUNT_OR_INTERMEDIATES_PER_STATION * station
        + slot
        for slot in range(COUNT_OR_INTERMEDIATES_PER_STATION)
    )


def increment_scratch(layout: dict[str, int]) -> tuple[int, ...]:
    return tuple(
        layout["increment_scratch_base"] + slot
        for slot in range(layout["increment_scratch_width"])
    )


def comparison_scratch(layout: dict[str, int]) -> tuple[int, ...]:
    return tuple(
        layout["comparison_scratch_base"] + slot
        for slot in range(layout["comparison_scratch_width"])
    )


def counter_wires(layout: dict[str, int]) -> tuple[int, ...]:
    return tuple(
        layout["counter_base"] + bit
        for bit in range(layout["counter_width"])
    )


def or_into(left: int, right: int, target: int) -> tuple[object, ...]:
    return (
        A.cn(left, target),
        A.cn(right, target),
        A.tof(left, right, target),
    )


def local_or_compute(
    inputs: tuple[int, ...],
    intermediates: tuple[int, ...],
    syndrome: int,
) -> tuple[object, ...]:
    if len(inputs) != COUNT_LOCAL_ROW_INPUTS:
        raise ValueError(("count refusal inputs", len(inputs)))
    if len(intermediates) != COUNT_OR_INTERMEDIATES_PER_STATION:
        raise ValueError(("count OR intermediates", len(intermediates)))
    outputs = intermediates + (syndrome,)
    word = list(or_into(inputs[0], inputs[1], outputs[0]))
    for index, source in enumerate(inputs[2:], start=1):
        word.extend(or_into(outputs[index - 1], source, outputs[index]))
    return tuple(word)


def controlled_increment_word(
    control: int,
    counter: tuple[int, ...],
    scratch: tuple[int, ...],
) -> tuple[object, ...]:
    """Add control to a clean-width binary counter, high carry first."""

    word: list[object] = []
    for bit in reversed(range(1, len(counter))):
        controls = (control,) + counter[:bit]
        word.extend(
            A.mcx(
                controls,
                counter[bit],
                scratch[:max(0, len(controls) - 2)],
            )
        )
    word.append(A.cn(control, counter[0]))
    return tuple(word)


def count_compute_word(
    layout: dict[str, int],
) -> tuple[tuple[object, ...], tuple[dict[str, int], ...]]:
    counter = counter_wires(layout)
    scratch = increment_scratch(layout)
    word: list[object] = []
    blocks = []
    for station in range(layout["stations"]):
        start = len(word)
        word.extend(
            controlled_increment_word(
                layout["a_base"] + station, counter, scratch
            )
        )
        blocks.append(
            {"station": station, "start": start, "stop": len(word)}
        )
    return tuple(word), tuple(blocks)


def comparison_compute_word(
    layout: dict[str, int], expected_count: int
) -> tuple[object, ...]:
    width = layout["counter_width"]
    if not 0 <= expected_count <= layout["stations"]:
        raise ValueError(("expected count", expected_count))
    counter = counter_wires(layout)
    latch = layout["refusal_latch"]
    zero_bits = tuple(
        counter[bit]
        for bit in range(width)
        if not ((expected_count >> bit) & 1)
    )
    word: list[object] = [A.x(wire) for wire in zero_bits]
    word.append(A.x(latch))
    word.extend(A.mcx(counter, latch, comparison_scratch(layout)))
    word.extend(A.x(wire) for wire in reversed(zero_bits))
    return tuple(word)


@lru_cache(maxsize=None)
def count_certified_controller_build(
    program: tuple[object, ...],
    data_wires: int,
    expected_count: int = EXPECTED_COUNT,
) -> tuple[
    tuple[object, ...],
    dict[str, int],
    tuple[dict[str, object], ...],
    dict[str, object],
]:
    """Compile count, mismatch-fed Cycle-730 Q, exact uncompute, and R."""

    stations = len(program)
    layout = register_layout(data_wires, stations)
    count_compute, increment_blocks = count_compute_word(layout)
    compare_compute = comparison_compute_word(layout, expected_count)
    word: list[object] = list(count_compute + compare_compute)
    q_start = len(word)
    blocks = []
    extra_or_gates: list[object] = []
    for station, row in enumerate(program):
        start = len(word)
        macro = K.mapped_macro(row)
        charge_compute = (
            E730.charge_compute_word(layout, station) if macro else ()
        )
        left = (station - 1) % stations
        right = (station + 1) % stations
        dirty_inputs = (
            layout["b_base"] + station,
            layout["work_base"] + station,
            layout["a_base"] + left,
            layout["b_base"] + left,
            layout["a_base"] + right,
            layout["b_base"] + right,
            layout["charge_base"] + station,
            layout["refusal_latch"],
        )
        syndrome = layout["syndrome_base"] + station
        or_compute = (
            local_or_compute(
                dirty_inputs, station_or_scratch(layout, station), syndrome
            )
            if macro
            else ()
        )
        lifted = (
            E730.lifted_refusing_macro(
                macro,
                layout["a_base"] + station,
                syndrome,
                station_mcx_scratch(layout, station),
            )
            if macro
            else ()
        )
        charge_start = len(word)
        word.extend(charge_compute)
        charge_stop = len(word)
        or_start = len(word)
        word.extend(or_compute)
        or_stop = len(word)
        if macro:
            word.append(A.x(syndrome))
            word.extend(lifted)
            word.append(A.x(syndrome))
        or_uncompute_start = len(word)
        word.extend(reversed(or_compute))
        or_uncompute_stop = len(word)
        charge_uncompute_start = len(word)
        word.extend(reversed(charge_compute))
        charge_uncompute_stop = len(word)
        if macro:
            extra_or_gates.extend(or_compute[-3:])
            extra_or_gates.extend(tuple(reversed(or_compute))[:3])
        blocks.append(
            {
                "station": station,
                "nonidentity": bool(macro),
                "start": start,
                "stop": len(word),
                "charge_compute_start": charge_start,
                "charge_compute_stop": charge_stop,
                "or_compute_start": or_start,
                "or_compute_stop": or_stop,
                "or_uncompute_start": or_uncompute_start,
                "or_uncompute_stop": or_uncompute_stop,
                "charge_uncompute_start": charge_uncompute_start,
                "charge_uncompute_stop": charge_uncompute_stop,
            }
        )
    q_stop = len(word)
    compare_uncompute_start = len(word)
    word.extend(reversed(compare_compute))
    compare_uncompute_stop = len(word)
    count_uncompute_start = len(word)
    word.extend(reversed(count_compute))
    count_uncompute_stop = len(word)
    r_start = len(word)
    r1 = tuple(
        gate
        for station in range(stations)
        for gate in K.swap_word(
            layout["a_base"] + station,
            layout["b_base"] + station,
        )
    )
    r2 = tuple(
        gate
        for station in range(stations)
        for gate in K.swap_word(
            layout["b_base"] + station,
            layout["a_base"] + (station + 1) % stations,
        )
    )
    word.extend(r1 + r2)
    certificate_word = (
        count_compute
        + compare_compute
        + tuple(extra_or_gates)
        + tuple(reversed(compare_compute))
        + tuple(reversed(count_compute))
    )
    metadata: dict[str, object] = {
        "count_compute_start": 0,
        "count_compute_stop": len(count_compute),
        "increment_blocks": increment_blocks,
        "comparison_compute_start": len(count_compute),
        "comparison_compute_stop": len(count_compute) + len(compare_compute),
        "q_start": q_start,
        "q_stop": q_stop,
        "comparison_uncompute_start": compare_uncompute_start,
        "comparison_uncompute_stop": compare_uncompute_stop,
        "count_uncompute_start": count_uncompute_start,
        "count_uncompute_stop": count_uncompute_stop,
        "r_start": r_start,
        "count_compute_word": count_compute,
        "comparison_compute_word": compare_compute,
        "certificate_word": certificate_word,
    }
    return tuple(word), layout, tuple(blocks), metadata


def controller_full_input(
    data_value: int,
    layout: dict[str, int],
    *,
    a: tuple[int, ...] = (),
    b: tuple[int, ...] = (),
    work: tuple[int, ...] = (),
    refs: tuple[int, ...] | None = None,
    h: int = 0,
) -> int:
    output = data_value
    for station in a:
        output |= 1 << (layout["a_base"] + station)
    for station in b:
        output |= 1 << (layout["b_base"] + station)
    for station in work:
        output |= 1 << (layout["work_base"] + station)
    if refs is None:
        refs = (0,) * layout["stations"]
    if len(refs) != layout["stations"]:
        raise ValueError(("refs", len(refs), layout["stations"]))
    for station, bit in enumerate(refs):
        if bit:
            output |= 1 << (layout["ref_base"] + station)
    if h:
        output |= 1 << layout["h_wire"]
    return output


def controller_rows(
    value: int, layout: dict[str, int]
) -> dict[str, object]:
    stations = layout["stations"]

    def row(base: int, width: int = stations) -> tuple[int, ...]:
        return tuple((value >> (base + index)) & 1 for index in range(width))

    return {
        "data": value & ((1 << layout["data_width"]) - 1),
        "A": row(layout["a_base"]),
        "B": row(layout["b_base"]),
        "work": row(layout["work_base"]),
        "syndrome": row(layout["syndrome_base"]),
        "scratch": row(
            layout["scratch_base"],
            E730.MCX_SCRATCH_PER_STATION * stations,
        ),
        "or_scratch": row(
            layout["or_scratch_base"],
            COUNT_OR_INTERMEDIATES_PER_STATION * stations,
        ),
        "refs": row(layout["ref_base"]),
        "charge": row(layout["charge_base"]),
        "h": (value >> layout["h_wire"]) & 1,
        "counter": row(layout["counter_base"], layout["counter_width"]),
        "increment_scratch": row(
            layout["increment_scratch_base"],
            layout["increment_scratch_width"],
        ),
        "comparison_scratch": row(
            layout["comparison_scratch_base"],
            layout["comparison_scratch_width"],
        ),
        "refusal_latch": (value >> layout["refusal_latch"]) & 1,
    }


def all_auxiliary_clean(rows: dict[str, object]) -> bool:
    return not any(
        bit
        for key in (
            "syndrome",
            "scratch",
            "or_scratch",
            "charge",
            "counter",
            "increment_scratch",
            "comparison_scratch",
        )
        for bit in rows[key]
    ) and rows["refusal_latch"] == 0


def literal_apply(
    values: tuple[int, ...],
    word: tuple[object, ...],
    width: int,
    iterations: int,
) -> tuple[int, ...]:
    return E724.F723.apply_literal_bitplanes(
        values, word, width, iterations
    )


def input_contract_certificate() -> dict[str, object]:
    recovered = declared_input_closure(DIRECT_INPUT_PATHS)
    existence = {
        path: (REPO_ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
    }

    def manifest_digest(
        paths: tuple[str, ...],
        replacement: tuple[str, bytes] | None = None,
    ) -> str:
        digest = sha256()
        for relative in paths:
            payload = (REPO_ROOT / relative).read_bytes()
            if replacement is not None and replacement[0] == relative:
                payload = replacement[1]
            digest.update(relative.encode())
            digest.update(b"\0")
            digest.update(payload)
            digest.update(b"\0")
        return digest.hexdigest()

    missing_rejected = False
    try:
        declared_input_closure(
            DIRECT_INPUT_PATHS
            + ("scripts/__cycle731_missing_input_control__.py",)
        )
    except FileNotFoundError:
        missing_rejected = True
    extra_recovered = declared_input_closure(
        DIRECT_INPUT_PATHS + ("docs/CANONICAL_HARNESS_INDEX.md",)
    )
    transitive_path = (
        "scripts/"
        "frontier_cycle719_local_handshake_controller_core_2026_07_26.py"
    )
    transitive_payload = (REPO_ROOT / transitive_path).read_bytes()
    mutated_payload = transitive_payload + b"\n# cycle731 mutation control\n"
    observed_manifest = manifest_digest(recovered)
    mutated_manifest = manifest_digest(
        recovered, (transitive_path, mutated_payload)
    )
    return {
        "direct_paths": DIRECT_INPUT_PATHS,
        "all_exist": all(existence.values()),
        "note_required": True,
        "note_in_closure": NOTE_PATH in recovered,
        "pure_literal_tuple": DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS,
        "declared_mutable_input_paths": len(AUDIT_INPUT_PATHS),
        "declared_input_closure_exact": recovered == AUDIT_INPUT_PATHS,
        "missing_file_control_rejected": missing_rejected,
        "extra_file_control_detected":
            extra_recovered != AUDIT_INPUT_PATHS
            and "docs/CANONICAL_HARNESS_INDEX.md" in extra_recovered,
        "transitive_control_path": transitive_path,
        "transitive_control_is_not_direct":
            transitive_path not in DIRECT_INPUT_PATHS,
        "manifest_sha256": observed_manifest,
        "transitive_mutation_changes_manifest":
            mutated_manifest != observed_manifest,
    }


def cycle730_regression_anchor() -> dict[str, object]:
    word, _layout, _blocks, _q_stop = E730.extended_controller_build(
        E730.R719.PROGRAM, DATA_WIDTH
    )
    repeated, _layout2, _blocks2, _q_stop2 = (
        E730.extended_controller_build(E730.R719.PROGRAM, DATA_WIDTH)
    )
    digest = K.gate_digest(word)
    frozen = E730.lawful_extended_case(
        "held_2", 2, K.interleaved_program(2)
    )
    frozen_keys = (
        "data_allocator_match",
        "A0_return",
        "B_return",
        "work_return",
        "syndrome_return",
        "mcx_scratch_return",
        "or_scratch_return",
        "charge_scratch_return",
        "refs_return",
        "h_return",
        "literal_reverse_exact",
    )
    return {
        "expected_semantic_gates": EXPECTED_CYCLE730_PADDED_GATES,
        "observed_semantic_gates": len(word),
        "expected_word_sha256": EXPECTED_CYCLE730_PADDED_SHA256,
        "observed_word_sha256": digest,
        "recomputed_word_sha256": K.gate_digest(repeated),
        "count_match": len(word) == EXPECTED_CYCLE730_PADDED_GATES,
        "digest_match": digest == EXPECTED_CYCLE730_PADDED_SHA256,
        "repeat_exact": word == repeated,
        "frozen_lawful_case": frozen,
        "frozen_lawful_case_pass": all(frozen[key] for key in frozen_keys),
    }


def structure_certificate() -> dict[str, object]:
    program = E730.R719.PROGRAM
    word, layout, blocks, metadata = count_certified_controller_build(
        program, DATA_WIDTH, EXPECTED_COUNT
    )
    old_word, _old_layout, _old_blocks, old_q_stop = (
        E730.extended_controller_build(program, DATA_WIDTH)
    )
    certificate_word = metadata["certificate_word"]
    ref_h_wires = set(
        range(layout["ref_base"], layout["ref_base"] + len(program))
    )
    ref_h_wires.add(layout["h_wire"])
    ref_h_touch_failures = sum(
        any(wire in ref_h_wires for wire in gate.wires)
        for gate in certificate_word
    )
    allowed_kinds = {"X", "CNOT", "TOF"}
    runtime_gate_kind_failures = sum(
        gate.kind not in allowed_kinds for gate in word
    )
    logical_register_scope_failures = 0
    count_compute = metadata["count_compute_word"]
    for block in metadata["increment_blocks"]:
        station = int(block["station"])
        allowed = {
            layout["a_base"] + station,
            *counter_wires(layout),
            *increment_scratch(layout),
        }
        logical_register_scope_failures += sum(
            not set(gate.wires) <= allowed
            for gate in count_compute[int(block["start"]):int(block["stop"])]
        )
    compare_allowed = {
        *counter_wires(layout),
        *comparison_scratch(layout),
        layout["refusal_latch"],
    }
    logical_register_scope_failures += sum(
        not set(gate.wires) <= compare_allowed
        for gate in metadata["comparison_compute_word"]
    )
    new_r = word[int(metadata["r_start"]):]
    old_r = old_word[old_q_stop:]
    nonidentity = sum(bool(row["nonidentity"]) for row in blocks)
    delta = len(word) - len(old_word)
    return {
        "stations": len(program),
        "expected_count": EXPECTED_COUNT,
        "counter_width": layout["counter_width"],
        "counter_width_formula": "ceil(log2(N+1))",
        "semantic_gates": len(word),
        "word_sha256": K.gate_digest(word),
        "Cycle730_semantic_gates": len(old_word),
        "added_semantic_gates": delta,
        "certificate_semantic_gates": len(certificate_word),
        "delta_equals_certificate_word": delta == len(certificate_word),
        "nonidentity_stations": nonidentity,
        "extra_OR_gates": 6 * nonidentity,
        "R_literal_suffix_unchanged": new_r == old_r,
        "exact_comparison_uncompute":
            word[
                int(metadata["comparison_uncompute_start"]):
                int(metadata["comparison_uncompute_stop"])
            ]
            == tuple(reversed(metadata["comparison_compute_word"])),
        "exact_counter_uncompute":
            word[
                int(metadata["count_uncompute_start"]):
                int(metadata["count_uncompute_stop"])
            ]
            == tuple(reversed(metadata["count_compute_word"])),
        "count_certificate_ref_h_touch_failures": ref_h_touch_failures,
        "compiled_gate_kind_failures": runtime_gate_kind_failures,
        "fixed_global_register_scope_failures":
            logical_register_scope_failures,
        "physical_transport_compilation_claimed": False,
        "full_width": layout["full_width"],
    }


def lawful_case(
    label: str, bank_count: int, program: tuple[object, ...]
) -> dict[str, object]:
    stations = len(program)
    old_word, old_layout, _old_blocks, _old_q_stop = (
        E730.extended_controller_build(program, DATA_WIDTH)
    )
    word, layout, _blocks, _metadata = count_certified_controller_build(
        program, DATA_WIDTH, EXPECTED_COUNT
    )
    refs, h = E730.lawful_reference_rails(stations)
    banks, links = B.chain_genesis(bank_count)
    before = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    data_value = E724.F723.tuple_to_int(before)
    old_source = E730.controller_full_input(
        data_value, old_layout, a=(0,), refs=refs, h=h
    )
    source = controller_full_input(
        data_value, layout, a=(0,), refs=refs, h=h
    )
    old_observed = literal_apply(
        (old_source,), old_word, old_layout["full_width"], stations
    )[0]
    observed = literal_apply(
        (source,), word, layout["full_width"], stations
    )[0]
    restored = literal_apply(
        (observed,), tuple(reversed(word)), layout["full_width"], stations
    )[0]
    old_rows = E730.controller_rows(old_observed, old_layout)
    rows = controller_rows(observed, layout)
    common_equal = (
        rows["data"] == old_rows["data"]
        and rows["A"] == old_rows["A"]
        and rows["B"] == old_rows["B"]
        and rows["work"] == old_rows["work"]
        and rows["refs"] == old_rows["refs"]
        and rows["h"] == old_rows["h"]
    )
    return {
        "label": label,
        "banks": bank_count,
        "stations": stations,
        "Cycle730_semantic_gates": len(old_word),
        "Cycle731_semantic_gates": len(word),
        "Cycle731_word_sha256": K.gate_digest(word),
        "data_and_rails_equal_Cycle730": common_equal,
        "A0_return":
            rows["A"] == (1,) + (0,) * (stations - 1),
        "B_work_return": not any(rows["B"]) and not any(rows["work"]),
        "refs_h_return": rows["refs"] == refs and rows["h"] == h,
        "all_auxiliaries_return_clean": all_auxiliary_clean(rows),
        "literal_reverse_exact": restored == source,
    }


def lawful_behavior_certificate() -> dict[str, object]:
    cases = (
        lawful_case("held_2", 2, K.interleaved_program(2)),
        lawful_case("held_5", 5, K.interleaved_program(5)),
        lawful_case("padded_130", 12, E730.R719.PROGRAM),
    )
    keys = (
        "data_and_rails_equal_Cycle730",
        "A0_return",
        "B_work_return",
        "refs_h_return",
        "all_auxiliaries_return_clean",
        "literal_reverse_exact",
    )
    return {
        "cases": cases,
        "trajectories": len(cases),
        "failure_census": sum(
            not bool(row[key]) for row in cases for key in keys
        ),
    }


def canonical_refs(
    a_mask: int, b_mask: int, h: int, stations: int
) -> tuple[int, ...]:
    refs, obstruction = E730.F728.canonical_reference_extension(
        a_mask, b_mask, h, stations
    )
    if obstruction:
        raise AssertionError(
            ("matched-parity canonical reference obstruction", a_mask, b_mask)
        )
    return E730.mask_to_tuple(refs, stations)


def residual_witness_certificate() -> dict[str, object]:
    program = K.interleaved_program(2)
    stations = len(program)
    word, layout, _blocks, _metadata = count_certified_controller_build(
        program, DATA_WIDTH, EXPECTED_COUNT
    )
    banks, links = B.chain_genesis(2)
    before = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    initial_data = E724.F723.tuple_to_int(before)
    placements = tuple(
        (left, right)
        for left in range(stations)
        for right in range(left + 1, stations)
    )
    sources = []
    refs_rows = []
    for placement in placements:
        a_mask = sum(1 << station for station in placement)
        refs = canonical_refs(a_mask, 0, 0, stations)
        refs_rows.append(refs)
        sources.append(
            controller_full_input(
                initial_data,
                layout,
                a=placement,
                refs=refs,
                h=0,
            )
        )
    observed_values = literal_apply(
        tuple(sources), word, layout["full_width"], 1
    )
    refusal_failures = return_failures = 0
    witness_row: dict[str, object] | None = None
    event_hasher = sha256()
    for placement, refs, source, observed_value in zip(
        placements, refs_rows, sources, observed_values
    ):
        rows = controller_rows(observed_value, layout)
        a = tuple(int(station in placement) for station in range(stations))
        rotated_a, rotated_b = E730.rotate_forward(
            a, (0,) * stations
        )
        event = {
            "step": 0,
            "station": placement[0],
            "reason": "count_mismatch",
            "observed_A_count": len(placement),
            "expected_count": EXPECTED_COUNT,
        }
        event_hasher.update(
            json.dumps(event, sort_keys=True, separators=(",", ":")).encode()
        )
        refusal_failures += rows["data"] != initial_data
        return_failures += rows["A"] != rotated_a
        return_failures += rows["B"] != rotated_b
        return_failures += rows["refs"] != refs or rows["h"] != 0
        return_failures += not all_auxiliary_clean(rows)
        if placement == (0, 5):
            refs_mask = E730.tuple_to_mask(refs)
            witness_row = {
                "ring_stations": stations,
                "A_mask": 33,
                "B_mask": 0,
                "h": 0,
                "token_sites": placement,
                "canonical_refs": refs_mask,
                "frozen_refs_match": refs_mask == 62,
                "refusal_event": event,
                "data_refused": rows["data"] == initial_data,
                "registers_return_clean": all_auxiliary_clean(rows),
            }
    if witness_row is None:
        raise AssertionError("frozen witness absent from pair sweep")
    return {
        "frozen_witness": witness_row,
        "two_token_placements": len(placements),
        "expected_two_token_placements": 55,
        "refusal_failures": refusal_failures,
        "return_cleanliness_failures": return_failures,
        "all_two_token_placements_refused":
            len(placements) == 55
            and refusal_failures == 0
            and return_failures == 0,
        "refusal_event_table_sha256": event_hasher.hexdigest(),
    }


def a_rail_counter_comparator_certificate() -> dict[str, object]:
    """Evaluate the actual counter/comparator gates on bounded exhaustive sets."""

    cases = 0
    behavior_failures = 0
    reverse_failures = 0
    scratch_failures = 0
    gate_kind_failures = 0
    outcome_hasher = sha256()
    ring_summaries: list[dict[str, object]] = []

    for stations in range(1, 13):
        layout = register_layout(0, stations)
        count_word, _blocks = count_compute_word(layout)
        ring_cases = 0
        ring_failures = 0
        for expected_count in range(stations + 1):
            compare_word = comparison_compute_word(layout, expected_count)
            word = count_word + compare_word
            gate_kind_failures += sum(
                gate.kind not in {"X", "CNOT", "TOF"} for gate in word
            )
            sources = tuple(range(1 << stations))
            observed = literal_apply(
                sources, word, layout["full_width"], 1
            )
            restored = literal_apply(
                observed, tuple(reversed(word)), layout["full_width"], 1
            )
            for a_mask, result, recovered in zip(
                sources, observed, restored
            ):
                rows = controller_rows(result, layout)
                observed_count = sum(
                    bit << index for index, bit in enumerate(rows["counter"])
                )
                expected_latch = int(
                    a_mask.bit_count() != expected_count
                )
                behavior_ok = (
                    rows["A"]
                    == tuple(
                        (a_mask >> station) & 1
                        for station in range(stations)
                    )
                    and observed_count == a_mask.bit_count()
                    and rows["refusal_latch"] == expected_latch
                    and not any(rows["B"])
                    and not any(rows["refs"])
                    and rows["h"] == 0
                )
                scratch_ok = (
                    not any(rows["increment_scratch"])
                    and not any(rows["comparison_scratch"])
                )
                behavior_failures += not behavior_ok
                scratch_failures += not scratch_ok
                reverse_failures += recovered != a_mask
                ring_failures += not (
                    behavior_ok and scratch_ok and recovered == a_mask
                )
                outcome_hasher.update(
                    bytes(
                        (
                            stations,
                            expected_count,
                            a_mask.bit_count(),
                            observed_count,
                            rows["refusal_latch"],
                        )
                    )
                )
                cases += 1
                ring_cases += 1
        ring_summaries.append(
            {
                "stations": stations,
                "counter_width": layout["counter_width"],
                "cases": ring_cases,
                "failures": ring_failures,
            }
        )

    width_failures = sum(
        counter_width(stations) != (stations + 1).bit_length() - (
            int(stations + 1).bit_count() == 1
        )
        for stations in range(1, 130)
    )
    overflow_failures = sum(
        stations >= (1 << counter_width(stations))
        for stations in range(1, 130)
    )
    invalid_expected_rejections = 0
    ring11_layout = register_layout(0, RING11_STATIONS)
    for invalid in (-1, RING11_STATIONS + 1):
        try:
            comparison_compute_word(ring11_layout, invalid)
        except ValueError:
            invalid_expected_rejections += 1
    ring11_count, _blocks = count_compute_word(ring11_layout)
    ring11_compare = comparison_compute_word(
        ring11_layout, EXPECTED_COUNT
    )
    ring11_word = ring11_count + ring11_compare
    allowed = {
        *range(
            ring11_layout["a_base"],
            ring11_layout["a_base"] + RING11_STATIONS,
        ),
        *counter_wires(ring11_layout),
        *increment_scratch(ring11_layout),
        *comparison_scratch(ring11_layout),
        ring11_layout["refusal_latch"],
    }
    wire_scope_failures = sum(
        not set(gate.wires) <= allowed for gate in ring11_word
    )
    return {
        "claim": (
            "clean reversible A-rail occupancy counter and supplied-value "
            "equality comparator"
        ),
        "counted_rail": "A only",
        "B_is_counted": False,
        "references_or_h_are_counted": False,
        "global_parity_acceptor_claimed": False,
        "counter_genesis_is_supplied_clean": True,
        "expected_occupancy_is_supplied": True,
        "exhaustive_station_range": [1, 12],
        "exhaustive_cases": cases,
        "behavior_failures": behavior_failures,
        "scratch_cleanliness_failures": scratch_failures,
        "literal_reverse_failures": reverse_failures,
        "gate_kind_failures": gate_kind_failures,
        "wire_scope_failures": wire_scope_failures,
        "width_range_checked": [1, 129],
        "width_failures": width_failures,
        "overflow_capacity_failures": overflow_failures,
        "invalid_expected_rejections": invalid_expected_rejections,
        "expected_invalid_expected_rejections": 2,
        "ring_summaries": ring_summaries,
        "outcome_table_sha256": outcome_hasher.hexdigest(),
        "ring11_expected1_gate_count": len(ring11_word),
        "ring11_expected1_gate_stream_schema":
            "sha256(concat(gate.kind + repr(gate.wires)))",
        "ring11_expected1_gate_stream_sha256":
            K.gate_digest(ring11_word),
    }


def global_parity_scope_boundary() -> dict[str, object]:
    """Freeze a concrete input showing that no global parity iff is claimed."""

    program = K.interleaved_program(2)
    stations = len(program)
    word, layout, _blocks, _metadata = count_certified_controller_build(
        program, DATA_WIDTH, EXPECTED_COUNT
    )
    banks, links = B.chain_genesis(2)
    before = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    initial_data = E724.F723.tuple_to_int(before)
    refs_mask = 2
    refs = E730.mask_to_tuple(refs_mask, stations)
    source = controller_full_input(
        initial_data, layout, a=(0,), refs=refs, h=0
    )
    after_one = literal_apply(
        (source,), word, layout["full_width"], 1
    )[0]
    after_orbit = literal_apply(
        (source,), word, layout["full_width"], stations
    )[0]
    one_rows = controller_rows(after_one, layout)
    orbit_rows = controller_rows(after_orbit, layout)
    one_restored = literal_apply(
        (after_one,), tuple(reversed(word)), layout["full_width"], 1
    )[0]
    orbit_restored = literal_apply(
        (after_orbit,),
        tuple(reversed(word)),
        layout["full_width"],
        stations,
    )[0]
    return {
        "input": {
            "A_mask": 1,
            "B_mask": 0,
            "refs_mask": refs_mask,
            "h": 0,
            "expected_A_occupancy": EXPECTED_COUNT,
        },
        "A_occupancy_matches": True,
        "two_rail_parity_matches_h": False,
        "data_changes_after_one_word":
            one_rows["data"] != initial_data,
        "data_changes_after_full_orbit":
            orbit_rows["data"] != initial_data,
        "auxiliaries_clean_after_one":
            all_auxiliary_clean(one_rows),
        "auxiliaries_clean_after_full_orbit":
            all_auxiliary_clean(orbit_rows),
        "refs_h_return_after_one":
            one_rows["refs"] == refs and one_rows["h"] == 0,
        "refs_h_return_after_full_orbit":
            orbit_rows["refs"] == refs and orbit_rows["h"] == 0,
        "literal_reverse_exact_after_one": one_restored == source,
        "literal_reverse_exact_after_full_orbit":
            orbit_restored == source,
        "scope_statement": (
            "The integrated word is not a global parity acceptor; the "
            "certificate proves only A-rail counter/comparator behavior and "
            "the separately stated fixed 55-placement refusal fixture."
        ),
    }


def register_dirty_weight(rows: dict[str, object]) -> int:
    return sum(
        int(bit)
        for key in (
            "syndrome",
            "scratch",
            "or_scratch",
            "charge",
            "counter",
            "increment_scratch",
            "comparison_scratch",
        )
        for bit in rows[key]
    ) + int(rows["refusal_latch"])


def deletion_controls_certificate(
    residual: dict[str, object],
) -> dict[str, object]:
    program = K.interleaved_program(2)
    word, layout, _blocks, metadata = count_certified_controller_build(
        program, DATA_WIDTH, EXPECTED_COUNT
    )
    refs, h = E730.lawful_reference_rails(len(program))
    banks, links = B.chain_genesis(2)
    before = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    initial_data = E724.F723.tuple_to_int(before)
    source = controller_full_input(
        initial_data, layout, a=(0,), refs=refs, h=h
    )
    correct = literal_apply(
        (source,), word, layout["full_width"], 1
    )[0]
    correct_rows = controller_rows(correct, layout)

    first_block = metadata["increment_blocks"][0]
    increment_index = int(first_block["stop"]) - 1
    deleted_increment_word = (
        word[:increment_index] + word[increment_index + 1:]
    )
    increment_output = literal_apply(
        (source,), deleted_increment_word, layout["full_width"], 1
    )[0]
    increment_rows = controller_rows(increment_output, layout)

    comparison_start = int(metadata["comparison_compute_start"])
    comparison_stop = int(metadata["comparison_compute_stop"])
    comparison_index = next(
        index
        for index in range(comparison_start, comparison_stop)
        if word[index].kind != "X"
        and word[index].wires[-1] == layout["refusal_latch"]
    )
    deleted_comparison_word = (
        word[:comparison_index] + word[comparison_index + 1:]
    )
    comparison_output = literal_apply(
        (source,), deleted_comparison_word, layout["full_width"], 1
    )[0]
    comparison_rows = controller_rows(comparison_output, layout)

    count_compute_size = int(metadata["count_compute_stop"])
    uncompute_start = int(metadata["count_uncompute_start"])
    uncompute_index = (
        uncompute_start + count_compute_size - 1 - increment_index
    )
    deleted_uncompute_word = (
        word[:uncompute_index] + word[uncompute_index + 1:]
    )
    uncompute_output = literal_apply(
        (source,), deleted_uncompute_word, layout["full_width"], 1
    )[0]
    uncompute_rows = controller_rows(uncompute_output, layout)

    return {
        "correct_lawful_auxiliary_return": all_auxiliary_clean(correct_rows),
        "correct_word_refuses_all_two_token_violations":
            residual["all_two_token_placements_refused"],
        "deleted_increment_gate": (
            word[increment_index].kind,
            word[increment_index].wires,
        ),
        "deleted_increment_detected":
            increment_output != correct
            or register_dirty_weight(increment_rows) > 0,
        "deleted_increment_dirty_weight":
            register_dirty_weight(increment_rows),
        "deleted_comparison_gate": (
            word[comparison_index].kind,
            word[comparison_index].wires,
        ),
        "deleted_comparison_detected":
            comparison_output != correct
            or register_dirty_weight(comparison_rows) > 0,
        "deleted_comparison_dirty_weight":
            register_dirty_weight(comparison_rows),
        "deleted_uncompute_gate": (
            word[uncompute_index].kind,
            word[uncompute_index].wires,
        ),
        "deleted_uncompute_detected":
            uncompute_output != correct
            or register_dirty_weight(uncompute_rows) > 0,
        "deleted_uncompute_dirty_weight":
            register_dirty_weight(uncompute_rows),
    }


def main() -> int:
    started = perf_counter()

    manifest = input_contract_certificate()
    check(
        "INPUT_recursive_mutable_closure_fail_closed",
        manifest["all_exist"]
        and manifest["note_required"]
        and manifest["note_in_closure"]
        and manifest["pure_literal_tuple"]
        and manifest["declared_input_closure_exact"]
        and manifest["missing_file_control_rejected"]
        and manifest["extra_file_control_detected"]
        and manifest["transitive_control_is_not_direct"]
        and manifest["transitive_mutation_changes_manifest"],
    )

    anchor = cycle730_regression_anchor()
    check(
        "A_Cycle730_regression_anchor",
        anchor["count_match"]
        and anchor["digest_match"]
        and anchor["repeat_exact"]
        and anchor["frozen_lawful_case_pass"],
    )

    structure = structure_certificate()
    check(
        "B_fixed_global_register_structure_and_uncompute",
        structure["delta_equals_certificate_word"]
        and structure["R_literal_suffix_unchanged"]
        and structure["exact_comparison_uncompute"]
        and structure["exact_counter_uncompute"]
        and structure["compiled_gate_kind_failures"] == 0
        and structure["fixed_global_register_scope_failures"] == 0
        and structure["count_certificate_ref_h_touch_failures"] == 0
        and not structure["physical_transport_compilation_claimed"],
    )

    counter = a_rail_counter_comparator_certificate()
    check(
        "C_actual_A_rail_counter_comparator_exhaustive",
        counter["exhaustive_cases"] > 0
        and counter["behavior_failures"] == 0
        and counter["scratch_cleanliness_failures"] == 0
        and counter["literal_reverse_failures"] == 0
        and counter["gate_kind_failures"] == 0
        and counter["wire_scope_failures"] == 0
        and counter["width_failures"] == 0
        and counter["overflow_capacity_failures"] == 0
        and counter["invalid_expected_rejections"]
        == counter["expected_invalid_expected_rejections"]
        and counter["counted_rail"] == "A only"
        and not counter["B_is_counted"]
        and not counter["global_parity_acceptor_claimed"],
    )

    lawful = lawful_behavior_certificate()
    check(
        "D_integrated_lawful_fixture_regression",
        lawful["failure_census"] == 0,
    )

    residual = residual_witness_certificate()
    witness = residual["frozen_witness"]
    check(
        "E_fixed_ring11_zeroB_h0_all_55_pairs_refused",
        witness["frozen_refs_match"]
        and witness["data_refused"]
        and witness["registers_return_clean"]
        and residual["two_token_placements"] == 55
        and residual["all_two_token_placements_refused"],
    )

    parity_boundary = global_parity_scope_boundary()
    check(
        "F_global_parity_nonclaim_counterexample",
        parity_boundary["A_occupancy_matches"]
        and not parity_boundary["two_rail_parity_matches_h"]
        and parity_boundary["data_changes_after_one_word"]
        and parity_boundary["data_changes_after_full_orbit"]
        and parity_boundary["auxiliaries_clean_after_one"]
        and parity_boundary["auxiliaries_clean_after_full_orbit"]
        and parity_boundary["refs_h_return_after_one"]
        and parity_boundary["refs_h_return_after_full_orbit"]
        and parity_boundary["literal_reverse_exact_after_one"]
        and parity_boundary["literal_reverse_exact_after_full_orbit"],
    )

    deletions = deletion_controls_certificate(residual)
    check(
        "G_counter_comparator_deletion_controls",
        deletions["correct_lawful_auxiliary_return"]
        and deletions["correct_word_refuses_all_two_token_violations"]
        and deletions["deleted_increment_detected"]
        and deletions["deleted_comparison_detected"]
        and deletions["deleted_uncompute_detected"],
    )

    claim_boundary = {
        "positive_scope": (
            "actual reversible A-rail counter/comparator gates, exhaustively "
            "checked for N=1..12 and every expected occupancy; fixed ring-11 "
            "zero-B, h=0 canonical-reference 55-placement refusal fixture"
        ),
        "counted_rail": "A only",
        "fixed_global_logical_register": True,
        "expected_occupancy_is_supplied": True,
        "clean_auxiliary_genesis_is_supplied": True,
        "inventory_is_derived": False,
        "global_parity_acceptor_claimed": False,
        "total_two_rail_inventory_claimed": False,
        "recurrent_admission_claimed": False,
        "physical_transport_or_NN_compilation_claimed": False,
        "audit_grade_claimed": False,
    }
    check(
        "H_honest_narrow_claim_boundary",
        claim_boundary["counted_rail"] == "A only"
        and claim_boundary["expected_occupancy_is_supplied"]
        and claim_boundary["clean_auxiliary_genesis_is_supplied"]
        and not claim_boundary["inventory_is_derived"]
        and not claim_boundary["global_parity_acceptor_claimed"]
        and not claim_boundary["total_two_rail_inventory_claimed"]
        and not claim_boundary["recurrent_admission_claimed"]
        and not claim_boundary[
            "physical_transport_or_NN_compilation_claimed"
        ]
        and not claim_boundary["audit_grade_claimed"],
    )

    elapsed = perf_counter() - started
    semantic_report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "pass": all(CHECKS.values()),
        "input_contract": manifest,
        "Cycle730_regression_anchor": anchor,
        "circuit_structure": structure,
        "A_rail_counter_comparator": counter,
        "lawful_behavior": lawful,
        "fixed_ring11_pair_sweep": residual,
        "global_parity_scope_boundary": parity_boundary,
        "deletion_controls": deletions,
        "word_size_comparison": {
            "Cycle730_semantic_gates": EXPECTED_CYCLE730_PADDED_GATES,
            "Cycle731_semantic_gates": structure["semantic_gates"],
            "added_semantic_gates": structure["added_semantic_gates"],
            "Cycle731_to_Cycle730_ratio":
                structure["semantic_gates"]
                / EXPECTED_CYCLE730_PADDED_GATES,
        },
        "claim_boundary": claim_boundary,
        "terminal": (
            "CYCLE731_A_RAIL_COUNTER_COMPARATOR_PASS"
            if all(CHECKS.values())
            else "CYCLE731_A_RAIL_COUNTER_COMPARATOR_HONEST_FAIL"
        ),
    }
    preliminary = json.dumps(
        semantic_report, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_20000_characters",
        len(preliminary) + 4096 < STDOUT_LIMIT_CHARACTERS,
    )
    semantic_report["checks"] = dict(sorted(CHECKS.items()))
    semantic_report["checks_failed"] = sum(
        not value for value in CHECKS.values()
    )
    semantic_report["checks_passed"] = sum(CHECKS.values())
    semantic_report["pass"] = all(CHECKS.values())
    semantic_report["terminal"] = (
        "CYCLE731_A_RAIL_COUNTER_COMPARATOR_PASS"
        if semantic_report["pass"]
        else "CYCLE731_A_RAIL_COUNTER_COMPARATOR_HONEST_FAIL"
    )
    semantic_json = json.dumps(
        semantic_report, sort_keys=True, separators=(",", ":"), default=str
    )
    report = dict(semantic_report)
    report["runtime_seconds"] = round(elapsed, 6)
    report["semantic_report_sha256"] = sha256(
        semantic_json.encode()
    ).hexdigest()
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(text) >= STDOUT_LIMIT_CHARACTERS:
        raise AssertionError(("stdout bound", len(text)))
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
