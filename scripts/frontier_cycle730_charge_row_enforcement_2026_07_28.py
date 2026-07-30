#!/usr/bin/env python3
"""Cycle 730: integrate supplied charge rows into a local refusal guard.

For every nonidentity station, this extends the Cycle-724 reversible refusal
sandwich by computing

    L_s = A_s XOR B_s XOR ref_s XOR ref_(s+1)

into one fresh charge bit, with the supplied h bit also entering the marked
edge s*=0.  L_s is the seventh dirty input, and both the enlarged OR cascade
and the charge computation are uncomputed exactly.  The reference chain and h
are static supplied rails; the unchanged Cycle-719 R layers touch only A/B.

This circuit statement is local: a dirty charge row refuses an active macro at
that station.  Separately, existential projection over reference chains obeys
the GF(2) parity theorem.  No global acceptance bit is constructed here.
"""
from __future__ import annotations

import ast
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter

import numpy as np

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle728_bksf_holonomy_compression_2026_07_28 as F728
import frontier_cycle724_local_token_row_enforcement_2026_07_28 as F724


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md"
DIRECT_INPUT_PATHS = (
    "scripts/frontier_cycle724_local_token_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle728_bksf_holonomy_compression_2026_07_28.py",
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

A = K.A
B = K.B
M = K.M
R719 = F724.R719
DATA_WIDTH = F724.DATA_WIDTH
MCX_SCRATCH_PER_STATION = F724.MCX_SCRATCH_PER_STATION
OR_INTERMEDIATE_PER_STATION = 5
LOCAL_ROW_INPUTS = 7
EXPECTED_CYCLE724_PADDED_GATES = 98_034
EXPECTED_CYCLE730_PADDED_GATES = 99_310
STDOUT_LIMIT_CHARACTERS = 20_000
FROZEN_MATCHED_PARITY_MULTITOKEN_WITNESS = (
    ("ring_stations", 11),
    ("A_mask", 33),
    ("B_mask", 0),
    ("refs_mask", 62),
    ("h", 0),
    ("token_sites", (0, 5)),
)

OUTPUT_LINES: list[str] = []
CHECKS: dict[str, bool] = {}
_PADDED_LITERAL_SHARED: dict[str, object] = {}
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
        seen.add(relative)
        if not (relative.startswith("scripts/") and relative.endswith(".py")):
            continue
        source_path = REPO_ROOT / relative
        tree = ast.parse(
            source_path.read_text(encoding="utf-8"),
            filename=str(source_path),
        )
        nested: tuple[str, ...] = ()
        for node in tree.body:
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            targets = (
                node.targets
                if isinstance(node, ast.Assign)
                else (node.target,)
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


def register_layout(data_wires: int, stations: int) -> dict[str, int]:
    """Cycle-724 layout plus a fifth OR bit, refs, charge bits, and one h."""

    a_base = data_wires
    b_base = a_base + stations
    work_base = b_base + stations
    syndrome_base = work_base + stations
    scratch_base = syndrome_base + stations
    or_scratch_base = (
        scratch_base + MCX_SCRATCH_PER_STATION * stations
    )
    ref_base = or_scratch_base + OR_INTERMEDIATE_PER_STATION * stations
    charge_base = ref_base + stations
    h_wire = charge_base + stations
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
        "full_width": h_wire + 1,
    }


def mcx_scratch_wires(
    layout: dict[str, int], station: int
) -> tuple[int, ...]:
    return tuple(
        layout["scratch_base"]
        + MCX_SCRATCH_PER_STATION * station
        + slot
        for slot in range(MCX_SCRATCH_PER_STATION)
    )


def or_scratch_wires(
    layout: dict[str, int], station: int
) -> tuple[int, ...]:
    return tuple(
        layout["or_scratch_base"]
        + OR_INTERMEDIATE_PER_STATION * station
        + slot
        for slot in range(OR_INTERMEDIATE_PER_STATION)
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
    if len(inputs) != LOCAL_ROW_INPUTS:
        raise ValueError(("local row inputs", len(inputs)))
    if len(intermediates) != OR_INTERMEDIATE_PER_STATION:
        raise ValueError(("OR intermediates", len(intermediates)))
    outputs = intermediates + (syndrome,)
    word = list(or_into(inputs[0], inputs[1], outputs[0]))
    for index, source in enumerate(inputs[2:], start=1):
        word.extend(or_into(outputs[index - 1], source, outputs[index]))
    return tuple(word)


def charge_compute_word(
    layout: dict[str, int], station: int
) -> tuple[object, ...]:
    stations = layout["stations"]
    charge = layout["charge_base"] + station
    sources = (
        layout["a_base"] + station,
        layout["b_base"] + station,
        layout["ref_base"] + station,
        layout["ref_base"] + (station + 1) % stations,
    )
    if station == F728.marked_station(stations):
        sources += (layout["h_wire"],)
    return tuple(A.cn(source, charge) for source in sources)


def lifted_refusing_macro(
    word: tuple[object, ...],
    control: int,
    syndrome: int,
    mcx_scratch: tuple[int, ...],
) -> tuple[object, ...]:
    lifted = []
    for gate in word:
        if gate.kind == "X":
            lifted.append(A.tof(control, syndrome, gate.wires[0]))
        elif gate.kind == "CNOT":
            lifted.extend(
                A.mcx(
                    (control, syndrome, gate.wires[0]),
                    gate.wires[1],
                    mcx_scratch,
                )
            )
        elif gate.kind == "TOF":
            lifted.extend(
                A.mcx(
                    (
                        control,
                        syndrome,
                        gate.wires[0],
                        gate.wires[1],
                    ),
                    gate.wires[2],
                    mcx_scratch,
                )
            )
        else:
            raise ValueError(gate.kind)
    return tuple(lifted)


@lru_cache(maxsize=None)
def extended_controller_build(
    program: tuple[object, ...],
    data_wires: int,
) -> tuple[
    tuple[object, ...],
    dict[str, int],
    tuple[dict[str, object], ...],
    int,
]:
    """Build locally charge-guarded Q, then untouched Cycle-719 R1/R2."""

    stations = len(program)
    layout = register_layout(data_wires, stations)
    q: list[object] = []
    station_segments = []
    for station, row in enumerate(program):
        start = len(q)
        macro = K.mapped_macro(row)
        charge_compute = charge_compute_word(layout, station) if macro else ()
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
        )
        syndrome = layout["syndrome_base"] + station
        or_compute = (
            local_or_compute(
                dirty_inputs,
                or_scratch_wires(layout, station),
                syndrome,
            )
            if macro
            else ()
        )
        lifted = (
            lifted_refusing_macro(
                macro,
                layout["a_base"] + station,
                syndrome,
                mcx_scratch_wires(layout, station),
            )
            if macro
            else ()
        )
        charge_compute_start = len(q)
        q.extend(charge_compute)
        charge_compute_stop = len(q)
        or_compute_start = len(q)
        q.extend(or_compute)
        or_compute_stop = len(q)
        if macro:
            q.append(A.x(syndrome))
            q.extend(lifted)
            q.append(A.x(syndrome))
        or_uncompute_start = len(q)
        q.extend(reversed(or_compute))
        or_uncompute_stop = len(q)
        charge_uncompute_start = len(q)
        q.extend(reversed(charge_compute))
        charge_uncompute_stop = len(q)
        station_segments.append(
            {
                "station": station,
                "nonidentity": bool(macro),
                "macro_gates": len(macro),
                "start": start,
                "stop": len(q),
                "charge_compute_start": charge_compute_start,
                "charge_compute_stop": charge_compute_stop,
                "or_compute_start": or_compute_start,
                "or_compute_stop": or_compute_stop,
                "or_uncompute_start": or_uncompute_start,
                "or_uncompute_stop": or_uncompute_stop,
                "charge_uncompute_start": charge_uncompute_start,
                "charge_uncompute_stop": charge_uncompute_stop,
            }
        )
    q_stop = len(q)
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
    return tuple(q) + r1 + r2, layout, tuple(station_segments), q_stop


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
    data_mask = (1 << layout["data_width"]) - 1

    def station_row(base: int) -> tuple[int, ...]:
        return tuple(
            (value >> (base + station)) & 1
            for station in range(stations)
        )

    return {
        "data": value & data_mask,
        "A": station_row(layout["a_base"]),
        "B": station_row(layout["b_base"]),
        "work": station_row(layout["work_base"]),
        "syndrome": station_row(layout["syndrome_base"]),
        "scratch": tuple(
            (
                value
                >> (
                    layout["scratch_base"]
                    + MCX_SCRATCH_PER_STATION * station
                    + slot
                )
            )
            & 1
            for station in range(stations)
            for slot in range(MCX_SCRATCH_PER_STATION)
        ),
        "or_scratch": tuple(
            (
                value
                >> (
                    layout["or_scratch_base"]
                    + OR_INTERMEDIATE_PER_STATION * station
                    + slot
                )
            )
            & 1
            for station in range(stations)
            for slot in range(OR_INTERMEDIATE_PER_STATION)
        ),
        "refs": station_row(layout["ref_base"]),
        "charge": station_row(layout["charge_base"]),
        "h": (value >> layout["h_wire"]) & 1,
    }


def tuple_to_mask(bits: tuple[int, ...]) -> int:
    return sum(bit << station for station, bit in enumerate(bits))


def mask_to_tuple(value: int, width: int) -> tuple[int, ...]:
    return tuple((value >> station) & 1 for station in range(width))


def lawful_reference_rails(stations: int) -> tuple[tuple[int, ...], int]:
    """Static chain that clears the active L_s as the token visits every s."""

    all_station_mask = (1 << stations) - 1
    h = stations & 1
    refs, obstruction = F728.canonical_reference_extension(
        all_station_mask, 0, h, stations
    )
    if obstruction:
        raise AssertionError(("lawful reference closure", stations))
    return mask_to_tuple(refs, stations), h


def charge_row_value(
    a: tuple[int, ...],
    b: tuple[int, ...],
    refs: tuple[int, ...],
    h: int,
    station: int,
) -> int:
    stations = len(a)
    return (
        a[station]
        ^ b[station]
        ^ refs[station]
        ^ refs[(station + 1) % stations]
        ^ (h if station == F728.marked_station(stations) else 0)
    )


def rotate_forward(
    a: tuple[int, ...], b: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    stations = len(a)
    return (
        tuple(a[(station - 1) % stations] for station in range(stations)),
        tuple(b[(station + 1) % stations] for station in range(stations)),
    )


def rotate_reverse(
    a: tuple[int, ...], b: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    stations = len(a)
    return (
        tuple(a[(station + 1) % stations] for station in range(stations)),
        tuple(b[(station - 1) % stations] for station in range(stations)),
    )


def apply_data_word(data: int, word: tuple[object, ...]) -> int:
    return F724.F723.apply_semantic_int(data, word)


def charge_host_orbit(
    data: int,
    program: tuple[object, ...],
    *,
    refs: tuple[int, ...],
    h: int,
    token_positions: tuple[int, ...] = (0,),
    b_positions: tuple[int, ...] = (),
    work_positions: tuple[int, ...] = (),
    reverse: bool = False,
) -> dict[str, object]:
    stations = len(program)
    a = tuple(int(s in token_positions) for s in range(stations))
    b = tuple(int(s in b_positions) for s in range(stations))
    work = tuple(int(s in work_positions) for s in range(stations))
    output = data
    refused = []
    for step in range(stations):
        if reverse:
            a, b = rotate_reverse(a, b)
            order = reversed(range(stations))
        else:
            order = range(stations)
        for station in order:
            if not a[station]:
                continue
            macro = K.mapped_macro(program[station])
            if not macro:
                continue
            dirty = F724.local_dirty(a, b, work, station)
            dirty = dirty or charge_row_value(a, b, refs, h, station)
            if dirty:
                refused.append((step, station))
            else:
                output = apply_data_word(
                    output,
                    tuple(reversed(macro)) if reverse else macro,
                )
        if not reverse:
            a, b = rotate_forward(a, b)
    return {
        "data": output,
        "A": a,
        "B": b,
        "work": work,
        "syndrome": (0,) * stations,
        "scratch": (0,) * (MCX_SCRATCH_PER_STATION * stations),
        "or_scratch": (0,) * (
            OR_INTERMEDIATE_PER_STATION * stations
        ),
        "refs": refs,
        "charge": (0,) * stations,
        "h": h,
        "refused": tuple(refused),
    }


def identity_substituted_prediction(
    data: int,
    program: tuple[object, ...],
    *,
    refs: tuple[int, ...],
    h: int,
    token_positions: tuple[int, ...] = (0,),
    b_positions: tuple[int, ...] = (),
    work_positions: tuple[int, ...] = (),
) -> dict[str, object]:
    """Independent walk replacing each locally dirty macro by identity."""

    stations = len(program)
    a = [int(s in token_positions) for s in range(stations)]
    b = [int(s in b_positions) for s in range(stations)]
    work = tuple(int(s in work_positions) for s in range(stations))
    output = data
    refused = []
    for step in range(stations):
        for station, row in enumerate(program):
            if not a[station]:
                continue
            macro = K.mapped_macro(row)
            if not macro:
                continue
            left = (station - 1) % stations
            right = (station + 1) % stations
            local_charge = (
                a[station]
                ^ b[station]
                ^ refs[station]
                ^ refs[(station + 1) % stations]
                ^ (
                    h
                    if station == F728.marked_station(stations)
                    else 0
                )
            )
            neighborhood = (
                b[station],
                work[station],
                a[left],
                b[left],
                a[right],
                b[right],
                local_charge,
            )
            if any(neighborhood):
                refused.append((step, station))
            else:
                output = apply_data_word(output, macro)
        old_a = tuple(a)
        old_b = tuple(b)
        a = [
            old_a[(station - 1) % stations]
            for station in range(stations)
        ]
        b = [
            old_b[(station + 1) % stations]
            for station in range(stations)
        ]
    return {
        "data": output,
        "A": tuple(a),
        "B": tuple(b),
        "work": work,
        "refs": refs,
        "h": h,
        "refused": tuple(refused),
    }


def expected_charge_refusals(
    program: tuple[object, ...],
    refs: tuple[int, ...],
    h: int,
) -> tuple[tuple[int, int], ...]:
    stations = len(program)
    a = (1,) + (0,) * (stations - 1)
    b = (0,) * stations
    refused = []
    for step in range(stations):
        station = next(index for index, bit in enumerate(a) if bit)
        if (
            K.mapped_macro(program[station])
            and charge_row_value(a, b, refs, h, station)
        ):
            refused.append((step, station))
        a, b = rotate_forward(a, b)
    return tuple(refused)


def cycle724_regression_anchor() -> dict[str, object]:
    (
        word,
        _layout,
        _station_segments,
        _q_stop,
    ) = F724.extended_controller_build(
        R719.PROGRAM, DATA_WIDTH
    )
    held = dict(
        F724.lawful_extended_case(
            "unpadded_2", 2, K.interleaved_program(2)
        )
    )
    held["wrapped_station_segments"] = held.pop("wrapped_blocks")
    held_keys = (
        "data_allocator_match",
        "A0_return",
        "B_return",
        "work_return",
        "syndrome_return",
        "mcx_scratch_return",
        "or_scratch_return",
        "literal_reverse_exact",
    )
    return {
        "expected_semantic_gates": EXPECTED_CYCLE724_PADDED_GATES,
        "observed_semantic_gates": len(word),
        "word_sha256": K.gate_digest(word),
        "count_match": len(word) == EXPECTED_CYCLE724_PADDED_GATES,
        "lawful_held_2": held,
        "lawful_held_2_pass": all(held[key] for key in held_keys),
    }


def lawful_q_time_charge_certificate(
    program: tuple[object, ...],
) -> dict[str, object]:
    stations = len(program)
    refs, h = lawful_reference_rails(stations)
    a = (1,) + (0,) * (stations - 1)
    b = (0,) * stations
    visited = []
    values = []
    for _step in range(stations):
        active = tuple(index for index, bit in enumerate(a) if bit)
        if len(active) != 1:
            raise AssertionError(("lawful active token", active))
        station = active[0]
        visited.append(station)
        values.append(charge_row_value(a, b, refs, h, station))
        a, b = rotate_forward(a, b)
    return {
        "stations": stations,
        "h": h,
        "q_time_active_rows_checked": len(values),
        "q_time_active_charge_failures": sum(values),
        "every_station_checked_once": tuple(visited) == tuple(range(stations)),
        "reference_mask": tuple_to_mask(refs),
    }


def lawful_extended_case(
    label: str,
    bank_count: int,
    program: tuple[object, ...],
) -> dict[str, object]:
    word, layout, station_segments, _q_stop = extended_controller_build(
        program, DATA_WIDTH
    )
    refs, h = lawful_reference_rails(len(program))
    banks, links = B.chain_genesis(bank_count)
    before = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    source = controller_full_input(
        F724.F723.tuple_to_int(before),
        layout,
        a=(0,),
        refs=refs,
        h=h,
    )
    digest = K.gate_digest(word)
    if (
        label == "padded_130"
        and _PADDED_LITERAL_SHARED.get("word_sha256") == digest
        and _PADDED_LITERAL_SHARED.get("lawful_source") == source
    ):
        observed = int(_PADDED_LITERAL_SHARED["lawful_observed"])
        shared = True
    else:
        observed = F724.F723.apply_literal_bitplanes(
            (source,), word, layout["full_width"], len(program)
        )[0]
        shared = False
    rows = controller_rows(observed, layout)
    expected = A.apply_semantic(before, K.program_word(program))
    restored = F724.F723.apply_literal_bitplanes(
        (observed,),
        tuple(reversed(word)),
        layout["full_width"],
        len(program),
    )[0]
    return {
        "label": label,
        "banks": bank_count,
        "stations": len(program),
        "nonidentity_stations": sum(
            bool(K.mapped_macro(row)) for row in program
        ),
        "semantic_gates": len(word),
        "word_sha256": digest,
        "data_allocator_match":
            rows["data"] == F724.F723.tuple_to_int(expected),
        "A0_return":
            rows["A"] == (1,) + (0,) * (len(program) - 1),
        "B_return": not any(rows["B"]),
        "work_return": not any(rows["work"]),
        "syndrome_return": not any(rows["syndrome"]),
        "mcx_scratch_return": not any(rows["scratch"]),
        "or_scratch_return": not any(rows["or_scratch"]),
        "charge_scratch_return": not any(rows["charge"]),
        "refs_return": rows["refs"] == refs,
        "h_return": rows["h"] == h,
        "literal_reverse_exact": restored == source,
        "shared_with_charge_census": shared,
        "wrapped_station_segments": sum(
            row["nonidentity"] for row in station_segments
        ),
    }


def lawful_behavior_certificate() -> dict[str, object]:
    cases = (
        lawful_extended_case(
            "held_2", 2, K.interleaved_program(2)
        ),
        lawful_extended_case(
            "held_5", 5, K.interleaved_program(5)
        ),
        lawful_extended_case("padded_130", 12, R719.PROGRAM),
    )
    boolean_keys = (
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
        "cases": cases,
        "failure_census": sum(
            not row[key] for row in cases for key in boolean_keys
        ),
    }


def charge_violation_cases(
    program: tuple[object, ...],
) -> tuple[dict[str, object], ...]:
    stations = len(program)
    baseline_refs, baseline_h = lawful_reference_rails(stations)
    rows = []
    for station, program_row in enumerate(program):
        if not K.mapped_macro(program_row):
            continue
        for kind, flipped_ref in (
            ("flip_ref_s", station),
            ("flip_ref_s_plus_1", (station + 1) % stations),
        ):
            refs = list(baseline_refs)
            refs[flipped_ref] ^= 1
            rows.append(
                {
                    "station": station,
                    "kind": kind,
                    "flipped_ref": flipped_ref,
                    "refs": tuple(refs),
                    "h": baseline_h,
                }
            )
    marked = F728.marked_station(stations)
    if K.mapped_macro(program[marked]):
        rows.append(
            {
                "station": marked,
                "kind": "flip_h",
                "flipped_ref": None,
                "refs": baseline_refs,
                "h": baseline_h ^ 1,
            }
        )
    return tuple(rows)


def charge_violation_census_certificate() -> dict[str, object]:
    program = R719.PROGRAM
    stations = len(program)
    word, layout, _station_segments, _q_stop = extended_controller_build(
        program, DATA_WIDTH
    )
    cases = charge_violation_cases(program)
    banks, links = B.chain_genesis(F724.BANKS)
    initial = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    initial_value = F724.F723.tuple_to_int(initial)
    sources = tuple(
        controller_full_input(
            initial_value,
            layout,
            a=(0,),
            refs=case["refs"],
            h=int(case["h"]),
        )
        for case in cases
    )

    matter_initial = F724.F723.tuple_to_int(
        M.pack_state(banks, links, matter=1)
    )
    matter = R719.C713.apply_sparse_word(
        {matter_initial: 1.0 + 0.0j}, R719.MATTER_WORD
    )
    compiled_source_bases = tuple(sorted(matter))
    lawful_refs, lawful_h = lawful_reference_rails(stations)
    compiled_sources = tuple(
        controller_full_input(
            value,
            layout,
            a=(0,),
            refs=lawful_refs,
            h=lawful_h,
        )
        for value in compiled_source_bases
    )
    lawful_source = controller_full_input(
        initial_value,
        layout,
        a=(0,),
        refs=lawful_refs,
        h=lawful_h,
    )
    combined = F724.F723.apply_literal_bitplanes(
        sources + compiled_sources + (lawful_source,),
        word,
        layout["full_width"],
        stations,
    )
    observed_values = combined[:len(sources)]
    compiled_stop = len(sources) + len(compiled_sources)
    _PADDED_LITERAL_SHARED.update(
        {
            "word_sha256": K.gate_digest(word),
            "compiled_source_bases": compiled_source_bases,
            "compiled_sources": compiled_sources,
            "compiled_observed": combined[len(sources):compiled_stop],
            "lawful_source": lawful_source,
            "lawful_observed": combined[-1],
        }
    )

    literal_prediction_mismatches = 0
    host_prediction_mismatches = 0
    event_mismatches = 0
    target_event_mismatches = 0
    rail_return_failures = 0
    auxiliary_return_failures = 0
    visible_violation_failures = 0
    predicted_refusals = 0
    observed_refusals = 0
    for case, observed_value in zip(cases, observed_values):
        refs = case["refs"]
        h = int(case["h"])
        prediction = identity_substituted_prediction(
            initial_value, program, refs=refs, h=h
        )
        host = charge_host_orbit(
            initial_value, program, refs=refs, h=h
        )
        direct = expected_charge_refusals(program, refs, h)
        rows = controller_rows(observed_value, layout)
        literal_prediction_mismatches += (
            rows["data"] != prediction["data"]
        )
        host_prediction_mismatches += (
            host["data"] != prediction["data"]
        )
        event_mismatches += host["refused"] != prediction["refused"]
        event_mismatches += host["refused"] != direct
        target = int(case["station"])
        target_events = tuple(
            event for event in host["refused"] if event[1] == target
        )
        target_event_mismatches += not target_events
        expected_a = (1,) + (0,) * (stations - 1)
        rail_return_failures += rows["A"] != expected_a
        rail_return_failures += any(rows["B"])
        rail_return_failures += any(rows["work"])
        rail_return_failures += rows["refs"] != refs
        rail_return_failures += rows["h"] != h
        auxiliary_return_failures += any(rows["syndrome"])
        auxiliary_return_failures += any(rows["scratch"])
        auxiliary_return_failures += any(rows["or_scratch"])
        auxiliary_return_failures += any(rows["charge"])
        visible_violation_failures += not (
            rows["refs"] != lawful_refs or rows["h"] != lawful_h
        )
        predicted_refusals += len(direct)
        observed_refusals += len(host["refused"])
    nonidentity = sum(bool(K.mapped_macro(row)) for row in program)
    return {
        "stations": stations,
        "nonidentity_stations": nonidentity,
        "ref_flip_cases": 2 * nonidentity,
        "h_flip_cases": 1,
        "census_size": len(cases),
        "literal_fixture_cases_compiled": len(observed_values),
        "literal_prediction_mismatches": literal_prediction_mismatches,
        "host_prediction_mismatches": host_prediction_mismatches,
        "refusal_event_mismatches": event_mismatches,
        "target_station_refusal_mismatches": target_event_mismatches,
        "rail_and_reference_return_failures": rail_return_failures,
        "syndrome_scratch_return_failures": auxiliary_return_failures,
        "visible_violation_failures": visible_violation_failures,
        "predicted_refusals": predicted_refusals,
        "observed_refusals": observed_refusals,
    }


def circuit_structure_certificate() -> dict[str, object]:
    program = R719.PROGRAM
    word, layout, station_segments, q_stop = extended_controller_build(
        program, DATA_WIDTH
    )
    active_segments = tuple(
        row for row in station_segments if row["nonidentity"]
    )
    marked = F728.marked_station(len(program))
    expected_r = tuple(
        gate
        for station in range(len(program))
        for gate in K.swap_word(
            layout["a_base"] + station,
            layout["b_base"] + station,
        )
    ) + tuple(
        gate
        for station in range(len(program))
        for gate in K.swap_word(
            layout["b_base"] + station,
            layout["a_base"] + (station + 1) % len(program),
        )
    )
    static_wires = set(
        range(layout["ref_base"], layout["ref_base"] + len(program))
    )
    static_wires.add(layout["h_wire"])
    r_controller_only_failures = sum(
        any(wire in static_wires for wire in gate.wires)
        for gate in word[q_stop:]
    )
    ref_h_target_failures = sum(
        gate.wires[-1] in static_wires for gate in word
    )
    charge_coverage_failures = 0
    exact_uncompute_failures = 0
    for segment in active_segments:
        station = int(segment["station"])
        charge_wire = layout["charge_base"] + station
        compute = word[
            int(segment["charge_compute_start"]):
            int(segment["charge_compute_stop"])
        ]
        or_compute = word[
            int(segment["or_compute_start"]):
            int(segment["or_compute_stop"])
        ]
        or_uncompute = word[
            int(segment["or_uncompute_start"]):
            int(segment["or_uncompute_stop"])
        ]
        charge_uncompute = word[
            int(segment["charge_uncompute_start"]):
            int(segment["charge_uncompute_stop"])
        ]
        expected_charge_gates = 5 if station == marked else 4
        charge_coverage_failures += len(compute) != expected_charge_gates
        charge_coverage_failures += not any(
            charge_wire in gate.wires[:-1] for gate in or_compute
        )
        exact_uncompute_failures += (
            or_uncompute != tuple(reversed(or_compute))
        )
        exact_uncompute_failures += (
            charge_uncompute != tuple(reversed(compute))
        )
    nonidentity = len(active_segments)
    expected_added = 14 * nonidentity + 2
    k_r_semantics = tuple(
        F728.verify_k_r_semantics(stations)
        for stations in (11, 35, 130)
    )
    return {
        "semantic_gates": len(word),
        "word_sha256": K.gate_digest(word),
        "full_width": layout["full_width"],
        "nonidentity_stations": nonidentity,
        "marked_station": marked,
        "or_gates_per_compute": 3 * (LOCAL_ROW_INPUTS - 1),
        "charge_compute_gates_unmarked": 4,
        "charge_compute_gates_marked": 5,
        "cycle724_to_cycle730_added_gates_expected": expected_added,
        "cycle724_to_cycle730_added_gates_observed":
            len(word) - EXPECTED_CYCLE724_PADDED_GATES,
        "count_match": len(word) == EXPECTED_CYCLE730_PADDED_GATES,
        "charge_coverage_failures": charge_coverage_failures,
        "exact_uncompute_failures": exact_uncompute_failures,
        "R_literal_suffix_match": word[q_stop:] == expected_r,
        "R_static_ref_h_touch_failures": r_controller_only_failures,
        "ref_h_target_failures": ref_h_target_failures,
        "K_R_semantics": k_r_semantics,
        "K_R_semantic_failures": sum(
            row["failures"] for row in k_r_semantics
        ),
        "controller_bits_per_station_excluding_global_h": 12,
        "global_h_bits": 1,
    }


def projection_and_local_guard_certificate() -> dict[str, object]:
    """Separate the existential row theorem from the local circuit guard."""

    exhaustive = F728.exhaustive_ring11()
    amended = exhaustive["amended_by_h"]
    ring_program = K.interleaved_program(2)
    word, layout, station_segments, _q_stop = extended_controller_build(
        ring_program, DATA_WIDTH
    )
    active_segments = tuple(
        row for row in station_segments if row["nonidentity"]
    )
    existential_projection_iff = all(
        row["projected_satisfied_states"]
        == row["token_parity_sector_states"]
        == 2_097_152
        and row["projected_exact_separation_failures"] == 0
        and row["canonical_extension_failures"] == 0
        and row["complement_extension_failures"] == 0
        and row["satisfying_reference_extensions"] == 4_194_304
        for row in amended
    )
    exactly_two_extensions = all(
        row["satisfying_reference_extensions"]
        == 2 * row["token_parity_sector_states"]
        for row in amended
    )
    fixed_reference_distinction = all(
        row["fixed_ref_satisfied_states"] == 2 ** 11
        and row["fixed_ref_matching_states"] == 2 ** 11
        for row in amended
    )
    local_guard_coverage = (
        len(active_segments) == len(ring_program) == 11
        and all(
            int(row["charge_compute_stop"])
            > int(row["charge_compute_start"])
            for row in active_segments
        )
        and all(
            int(row["or_compute_stop"]) - int(row["or_compute_start"])
            == 18
            for row in active_segments
        )
    )
    witness = dict(FROZEN_MATCHED_PARITY_MULTITOKEN_WITNESS)
    canonical_refs, obstruction = F728.canonical_reference_extension(
        witness["A_mask"],
        witness["B_mask"],
        witness["h"],
        witness["ring_stations"],
    )
    syndrome = F728.twisted_local_syndrome_mask(
        witness["A_mask"],
        witness["B_mask"],
        witness["refs_mask"],
        witness["h"],
        witness["ring_stations"],
    )
    token_sites = witness["token_sites"]
    distance = min(
        (token_sites[0] - token_sites[1]) % witness["ring_stations"],
        (token_sites[1] - token_sites[0]) % witness["ring_stations"],
    )
    static_witness_pass = (
        canonical_refs == witness["refs_mask"]
        and obstruction == 0
        and syndrome == 0
        and F728.token_parity(
            witness["A_mask"], witness["B_mask"]
        )
        == witness["h"]
        and witness["A_mask"].bit_count()
        + witness["B_mask"].bit_count()
        == 2
        and distance > 1
    )
    counterexample = {
        "A_mask": 1,
        "B_mask": 0,
        "refs_mask": 2,
        "h": 0,
        "active_station": 0,
    }
    counterexample_syndrome = F728.twisted_local_syndrome_mask(
        counterexample["A_mask"],
        counterexample["B_mask"],
        counterexample["refs_mask"],
        counterexample["h"],
        11,
    )
    global_guard_counterexample_pass = (
        F728.token_parity(
            counterexample["A_mask"], counterexample["B_mask"]
        )
        != counterexample["h"]
        and counterexample_syndrome != 0
        and (
            (
                counterexample_syndrome
                >> counterexample["active_station"]
            )
            & 1
        )
        == 0
    )
    return {
        "ring_stations": 11,
        "theorem_domain": "every finite oriented ring with n >= 1",
        "theorem_quantifiers": (
            "for every A,B,h there exists r with all L_s=0 iff "
            "XOR_s(A_s XOR B_s)=h"
        ),
        "rail_states_per_h": exhaustive["enumeration"]["rail_states"],
        "h_sectors": 2,
        "rail_h_cases": 2 * exhaustive["enumeration"]["rail_states"],
        "existentially_projected_pass_states_per_h": tuple(
            row["projected_satisfied_states"] for row in amended
        ),
        "token_parity_sector_states_per_h": tuple(
            row["token_parity_sector_states"] for row in amended
        ),
        "fixed_reference_pass_states_per_h": tuple(
            row["fixed_ref_satisfied_states"] for row in amended
        ),
        "reference_extensions_per_matching_rail_state": 2,
        "projected_exact_separation_failures": sum(
            row["projected_exact_separation_failures"]
            for row in amended
        ),
        "twist_telescope_failures": sum(
            row["twist_telescope_failures"] for row in amended
        ),
        "existential_reference_projection_iff_parity_equals_h":
            existential_projection_iff,
        "exactly_two_reference_extensions": exactly_two_extensions,
        "fixed_reference_is_not_whole_sector":
            fixed_reference_distinction,
        "all_ring11_active_macros_have_local_row_guard":
            local_guard_coverage,
        "ring11_semantic_gates": len(word),
        "ring11_full_width": layout["full_width"],
        "static_matched_parity_multitoken_row_witness": {
            **witness,
            "canonical_refs": canonical_refs,
            "closure_obstruction": obstruction,
            "charge_syndrome_mask": syndrome,
            "token_separation": distance,
            "all_local_rows_pass": syndrome == 0,
        },
        "static_row_witness_pass": static_witness_pass,
        "global_parity_acceptance_not_constructed": True,
        "global_guard_counterexample": {
            **counterexample,
            "charge_syndrome_mask": counterexample_syndrome,
            "active_charge_row_clean": (
                (
                    counterexample_syndrome
                    >> counterexample["active_station"]
                )
                & 1
            )
            == 0,
            "parity_mismatch": True,
        },
        "global_guard_counterexample_pass":
            global_guard_counterexample_pass,
    }


def deletion_controls_certificate() -> dict[str, object]:
    program = R719.PROGRAM
    word, layout, station_segments, _q_stop = extended_controller_build(
        program, DATA_WIDTH
    )
    segment = next(
        row
        for row in station_segments
        if row["nonidentity"]
        and row["station"] == F728.marked_station(len(program))
    )
    station = int(segment["station"])
    refs, lawful_h = lawful_reference_rails(len(program))
    hostile_h = lawful_h ^ 1
    banks, links = B.chain_genesis(F724.BANKS)
    initial = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    initial_value = F724.F723.tuple_to_int(initial)
    source = controller_full_input(
        initial_value,
        layout,
        a=(station,),
        refs=refs,
        h=hostile_h,
    )
    start = int(segment["start"])
    stop = int(segment["stop"])
    local = word[start:stop]
    correct = F724.F723.apply_semantic_int(source, local)
    correct_rows = controller_rows(correct, layout)

    charge_h_index = int(segment["charge_compute_stop"]) - start - 1
    deleted_charge = (
        local[:charge_h_index] + local[charge_h_index + 1:]
    )
    charge_output = F724.F723.apply_semantic_int(
        source, deleted_charge
    )
    charge_rows = controller_rows(charge_output, layout)

    charge_compute_size = (
        int(segment["charge_compute_stop"])
        - int(segment["charge_compute_start"])
    )
    deleted_or_index = charge_compute_size + 16
    deleted_or = (
        local[:deleted_or_index] + local[deleted_or_index + 1:]
    )
    or_output = F724.F723.apply_semantic_int(source, deleted_or)
    or_rows = controller_rows(or_output, layout)

    deleted_uncompute_index = (
        int(segment["or_uncompute_start"]) - start + 1
    )
    deleted_uncompute = (
        local[:deleted_uncompute_index]
        + local[deleted_uncompute_index + 1:]
    )
    uncompute_output = F724.F723.apply_semantic_int(
        source, deleted_uncompute
    )
    uncompute_rows = controller_rows(uncompute_output, layout)
    retained_auxiliary = (
        sum(uncompute_rows["syndrome"])
        + sum(uncompute_rows["or_scratch"])
        + sum(uncompute_rows["charge"])
    )
    return {
        "station": station,
        "correct_charge_violation_refused":
            correct_rows["data"] == initial_value,
        "correct_auxiliary_return": not any(
            bit
            for key in ("syndrome", "scratch", "or_scratch", "charge")
            for bit in correct_rows[key]
        ),
        "deleted_charge_compute_gate":
            F724.F723.fast_classical_word(
                (local[charge_h_index],)
            )[0],
        "deleted_charge_compute_detected":
            charge_rows["data"] != correct_rows["data"],
        "deleted_charge_compute_data_mismatch_bits":
            (charge_rows["data"] ^ correct_rows["data"]).bit_count(),
        "deleted_or_cascade_gate":
            F724.F723.fast_classical_word(
                (local[deleted_or_index],)
            )[0],
        "deleted_or_cascade_detected":
            or_rows["data"] != correct_rows["data"],
        "deleted_or_cascade_data_mismatch_bits":
            (or_rows["data"] ^ correct_rows["data"]).bit_count(),
        "deleted_uncompute_gate":
            F724.F723.fast_classical_word(
                (local[deleted_uncompute_index],)
            )[0],
        "deleted_uncompute_retained_auxiliary_weight":
            retained_auxiliary,
        "deleted_uncompute_detected": retained_auxiliary > 0,
    }


def physical_layout(bank_count: int) -> dict[str, object]:
    program, track = K.held_physical_program_and_track(bank_count)
    base = M.R12.full_wire_layout()
    data_sites = base["wire_sites"]
    a_sites = track[::2]
    b_sites = track[1::2]
    work_sites = tuple((x, y - 1, z) for x, y, z in a_sites)
    syndrome_sites = tuple((x, y - 2, z) for x, y, z in a_sites)
    mcx_scratch_sites = tuple(
        (x, y - 3 - slot, z)
        for x, y, z in a_sites
        for slot in range(MCX_SCRATCH_PER_STATION)
    )
    or_scratch_sites = tuple(
        (x, y - 3 - MCX_SCRATCH_PER_STATION - slot, z)
        for x, y, z in a_sites
        for slot in range(OR_INTERMEDIATE_PER_STATION)
    )
    ref_sites = tuple(
        (
            x,
            y - 3 - MCX_SCRATCH_PER_STATION
            - OR_INTERMEDIATE_PER_STATION,
            z,
        )
        for x, y, z in a_sites
    )
    charge_sites = tuple((x, y - 11, z) for x, y, z in a_sites)
    marked = F728.marked_station(len(program))
    marked_site = a_sites[marked]
    h_sites = (
        (marked_site[0], marked_site[1] - 12, marked_site[2]),
    )
    controller_sites = (
        a_sites
        + b_sites
        + work_sites
        + syndrome_sites
        + mcx_scratch_sites
        + or_scratch_sites
        + ref_sites
        + charge_sites
        + h_sites
    )
    wire_sites = data_sites + controller_sites
    assigned = set(base["assigned_sites"])
    word, layout, _station_segments, _q_stop = extended_controller_build(
        program, len(data_sites)
    )
    if len(wire_sites) != layout["full_width"]:
        raise AssertionError(
            ("physical/register width", len(wire_sites), layout["full_width"])
        )
    return {
        "program": program,
        "track": track,
        "word": word,
        "register_layout": layout,
        "wire_sites": wire_sites,
        "controller_sites": controller_sites,
        "assigned": assigned,
        "placement_collisions": (
            len(controller_sites)
            - len(set(controller_sites))
            + len(assigned & set(controller_sites))
        ),
    }


def physical_certificate(bank_count: int) -> dict[str, object]:
    physical = physical_layout(bank_count)
    program = physical["program"]
    track = physical["track"]
    word = physical["word"]
    wire_sites = physical["wire_sites"]
    forward, inverse = F724.streaming_route_pair(word, wire_sites)
    frames = K.C712.C709.F.base.proper_cubic_frames()
    rail_failures = sum(
        sum(abs(a - b) for a, b in zip(left, right)) != 1
        for left, right in zip(track, track[1:] + track[:1])
    )
    controller_sites = physical["controller_sites"]
    coordinate_failures = 0
    for frame in frames:
        inverse_frame = frame.T
        for site in controller_sites:
            moved = tuple(int(value) for value in frame @ np.asarray(site))
            restored = tuple(
                int(value)
                for value in inverse_frame @ np.asarray(moved)
            )
            coordinate_failures += restored != site
    translation_failures = 0
    for shift in ((3, -2, 1), (-5, 4, 2)):
        for site in controller_sites:
            moved = tuple(
                site[axis] + shift[axis] for axis in range(3)
            )
            restored = tuple(
                moved[axis] - shift[axis] for axis in range(3)
            )
            translation_failures += restored != site
    product_failures = 0
    for left in frames:
        for right in frames:
            product = left @ right
            product_failures += not any(
                np.array_equal(product, frame) for frame in frames
            )
    stations = len(program)
    return {
        "banks": bank_count,
        "stations": stations,
        "nonidentity_stations": sum(
            bool(K.mapped_macro(row)) for row in program
        ),
        "controller_semantic_gates": len(word),
        "controller_word_sha256": K.gate_digest(word),
        "controller_M2": len(controller_sites),
        "reference_M2": stations,
        "charge_scratch_M2": stations,
        "h_M2": 1,
        "or_cascade_scratch_M2":
            OR_INTERMEDIATE_PER_STATION * stations,
        "total_declared_M2": len(
            physical["assigned"] | set(controller_sites)
        ),
        "placement_collisions": physical["placement_collisions"],
        "rail_cycle_NN_failures": rail_failures,
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "coordinate_failures": coordinate_failures,
        "frame_product_failures": product_failures,
        "translation_failures": translation_failures,
        "forward": forward,
        "inverse": inverse,
    }


def physical_layer_certificate() -> dict[str, object]:
    rows = {
        banks: physical_certificate(banks) for banks in (2, 5, 12)
    }
    direct_keys = (
        "placement_collisions",
        "rail_cycle_NN_failures",
        "coordinate_failures",
        "frame_product_failures",
        "translation_failures",
    )
    route_keys = (
        "non_NN_failures",
        "operand_order_failures",
        "route_return_failures",
    )
    failures = sum(
        row[key] for row in rows.values() for key in direct_keys
    )
    failures += sum(
        row[direction][key]
        for row in rows.values()
        for direction in ("forward", "inverse")
        for key in route_keys
    )
    failures += sum(
        row["proper_cubic_frames"] != 24
        or row["ordered_frame_products"] != 576
        for row in rows.values()
    )
    return {"banks": rows, "failure_census": failures}


def compiled_extended_orbit_certificate() -> dict[str, object]:
    program = R719.PROGRAM
    word, layout, _station_segments, _q_stop = extended_controller_build(
        program, DATA_WIDTH
    )
    digest = K.gate_digest(word)
    refs, h = lawful_reference_rails(len(program))
    if _PADDED_LITERAL_SHARED.get("word_sha256") == digest:
        source_bases = _PADDED_LITERAL_SHARED["compiled_source_bases"]
        source_full = _PADDED_LITERAL_SHARED["compiled_sources"]
        observed_full = _PADDED_LITERAL_SHARED["compiled_observed"]
        shared = True
    else:
        banks, links = B.chain_genesis(F724.BANKS)
        initial_data = F724.F723.tuple_to_int(
            M.pack_state(banks, links, matter=1)
        )
        matter = R719.C713.apply_sparse_word(
            {initial_data: 1.0 + 0.0j}, R719.MATTER_WORD
        )
        source_bases = tuple(sorted(matter))
        source_full = tuple(
            controller_full_input(
                value, layout, a=(0,), refs=refs, h=h
            )
            for value in source_bases
        )
        observed_full = F724.F723.apply_literal_bitplanes(
            source_full, word, layout["full_width"], len(program)
        )
        shared = False
    restored_full = F724.F723.apply_literal_bitplanes(
        observed_full,
        tuple(reversed(word)),
        layout["full_width"],
        len(program),
    )
    equality_failures = 0
    inverse_failures = 0
    register_failures = 0
    rows = []
    for basis, source, observed_value, restored in zip(
        source_bases, source_full, observed_full, restored_full
    ):
        host = charge_host_orbit(
            basis, program, refs=refs, h=h
        )
        observed = controller_rows(observed_value, layout)
        equality_failures += observed["data"] != host["data"]
        inverse_failures += restored != source
        row_register_failures = (
            observed["A"] != host["A"]
            or observed["B"] != host["B"]
            or observed["work"] != host["work"]
            or observed["refs"] != refs
            or observed["h"] != h
            or any(
                bit
                for key in (
                    "syndrome",
                    "scratch",
                    "or_scratch",
                    "charge",
                )
                for bit in observed[key]
            )
        )
        register_failures += row_register_failures
        rows.append(
            {
                "source_matter_mode":
                    (int(basis) & 4095).bit_length() - 1,
                "compiled_equals_host":
                    observed["data"] == host["data"],
                "A0_return":
                    observed["A"]
                    == (1,) + (0,) * (len(program) - 1),
                "all_supplied_and_scratch_registers_return":
                    not row_register_failures,
                "inverse_exact": restored == source,
            }
        )
    return {
        "Cycle713_origin0_fixture_states": len(source_bases),
        "forward_shared_with_charge_census": shared,
        "semantic_gates_per_H": len(word),
        "H_applications_per_orbit": len(program),
        "forward_semantic_gate_applications_tested":
            len(source_bases) * len(word) * len(program),
        "inverse_semantic_gate_applications_tested":
            len(source_bases) * len(word) * len(program),
        "compiled_host_equality_failures": equality_failures,
        "compiled_inverse_failures": inverse_failures,
        "controller_register_return_failures": register_failures,
        "rows": rows,
        "controller_H_word_sha256": digest,
    }


def inherited_anchors_certificate() -> dict[str, object]:
    inherited = F724.inherited_anchors_certificate()
    return {
        "Cycle713_runner_expected_sha256":
            inherited["Cycle713_runner_expected_sha256"],
        "Cycle713_runner_observed_sha256":
            inherited["Cycle713_runner_observed_sha256"],
        "Cycle713_pin_match": inherited["Cycle713_pin_match"],
        "matter_residual_failures":
            inherited["matter_residual_failures"],
        "mass_residual": inherited["mass_residual"],
        "contact_residuals": inherited["contact_residuals"],
        "matter_falsifier_active":
            inherited["matter_falsifier_active"],
    }


def render_with_exact_size(
    report: dict[str, object],
) -> tuple[str, int]:
    report["stdout_characters"] = 0
    for _attempt in range(20):
        final_json = json.dumps(
            report, sort_keys=True, separators=(",", ":"), default=str
        )
        text = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
        size = len(text)
        if report["stdout_characters"] == size:
            return text, size
        report["stdout_characters"] = size
    raise AssertionError("stdout character fixed point")


def main() -> int:
    started = perf_counter()

    recovered_input_closure = declared_input_closure(DIRECT_INPUT_PATHS)
    check(
        "A0_declared_mutable_input_closure_exact",
        recovered_input_closure == AUDIT_INPUT_PATHS,
    )

    anchor = cycle724_regression_anchor()
    structure = circuit_structure_certificate()
    check(
        "A_Cycle724_regression_anchor",
        anchor["count_match"] and anchor["lawful_held_2_pass"],
    )

    q_time_rows = tuple(
        lawful_q_time_charge_certificate(program)
        for program in (
            K.interleaved_program(2),
            K.interleaved_program(5),
            R719.PROGRAM,
        )
    )
    check(
        "B0_lawful_trajectory_every_Q_time_charge_row_zero",
        all(
            row["q_time_active_charge_failures"] == 0
            and row["q_time_active_rows_checked"] == row["stations"]
            and row["every_station_checked_once"]
            for row in q_time_rows
        ),
    )

    census = charge_violation_census_certificate()
    lawful = lawful_behavior_certificate()
    check(
        "B_lawful_unchanged_charge_extended_wrap",
        lawful["failure_census"] == 0
        and structure["count_match"]
        and structure["charge_coverage_failures"] == 0
        and structure["exact_uncompute_failures"] == 0
        and structure["R_literal_suffix_match"]
        and structure["R_static_ref_h_touch_failures"] == 0
        and structure["ref_h_target_failures"] == 0
        and structure["K_R_semantic_failures"] == 0,
    )
    check(
        "C_exhaustive_charge_violation_refusal_census",
        census["nonidentity_stations"] == 91
        and census["census_size"]
        == 2 * census["nonidentity_stations"] + 1
        and census["literal_fixture_cases_compiled"]
        == census["census_size"]
        and census["literal_prediction_mismatches"] == 0
        and census["host_prediction_mismatches"] == 0
        and census["refusal_event_mismatches"] == 0
        and census["target_station_refusal_mismatches"] == 0
        and census["rail_and_reference_return_failures"] == 0
        and census["syndrome_scratch_return_failures"] == 0
        and census["visible_violation_failures"] == 0
        and census["predicted_refusals"] == census["observed_refusals"],
    )

    projection_guard = projection_and_local_guard_certificate()
    check(
        "D_existential_reference_projection_and_local_guard_split",
        projection_guard[
            "existential_reference_projection_iff_parity_equals_h"
        ]
        and projection_guard["exactly_two_reference_extensions"]
        and projection_guard["fixed_reference_is_not_whole_sector"]
        and projection_guard[
            "all_ring11_active_macros_have_local_row_guard"
        ]
        and projection_guard["global_parity_acceptance_not_constructed"]
        and projection_guard["global_guard_counterexample_pass"]
        and projection_guard["projected_exact_separation_failures"] == 0
        and projection_guard["twist_telescope_failures"] == 0,
    )
    check(
        "D0_static_multitoken_row_witness_bounded",
        projection_guard["static_row_witness_pass"],
    )

    deletions = deletion_controls_certificate()
    check(
        "E_deletion_controls",
        deletions["correct_charge_violation_refused"]
        and deletions["correct_auxiliary_return"]
        and deletions["deleted_or_cascade_detected"]
        and deletions["deleted_or_cascade_data_mismatch_bits"] > 0
        and deletions["deleted_uncompute_detected"]
        and deletions[
            "deleted_uncompute_retained_auxiliary_weight"
        ] > 0
        and deletions["deleted_charge_compute_detected"]
        and deletions["deleted_charge_compute_data_mismatch_bits"] > 0,
    )

    physical = physical_layer_certificate()
    check("F_physical_layer", physical["failure_census"] == 0)

    compiled = compiled_extended_orbit_certificate()
    check(
        "G_compiled_extended_orbit_six_Cycle713_fixture_states",
        compiled["Cycle713_origin0_fixture_states"] == 6
        and compiled["forward_shared_with_charge_census"]
        and compiled["H_applications_per_orbit"] == len(R719.PROGRAM)
        and compiled["compiled_host_equality_failures"] == 0
        and compiled["compiled_inverse_failures"] == 0
        and compiled["controller_register_return_failures"] == 0
        and all(
            row["compiled_equals_host"]
            and row["A0_return"]
            and row["all_supplied_and_scratch_registers_return"]
            and row["inverse_exact"]
            for row in compiled["rows"]
        ),
    )

    inherited = inherited_anchors_certificate()
    check(
        "H_inherited_Cycle713_source_pin_and_residuals",
        inherited["Cycle713_pin_match"]
        and inherited["matter_residual_failures"] == 0
        and inherited["matter_falsifier_active"],
    )

    local_charge_row_guard = (
        structure["charge_coverage_failures"] == 0
        and structure["exact_uncompute_failures"] == 0
        and projection_guard[
            "all_ring11_active_macros_have_local_row_guard"
        ]
        and CHECKS["C_exhaustive_charge_violation_refusal_census"]
    )
    boundary = {
        "local_charge_row_guard_at_every_active_macro":
            local_charge_row_guard,
        "existential_reference_projection_theorem":
            projection_guard[
                "existential_reference_projection_iff_parity_equals_h"
            ],
        "fixed_reference_chain_covers_whole_matching_sector": False,
        "global_parity_acceptance_constructed": False,
        "static_matched_parity_multitoken_row_witness": True,
        "global_one_token_existence_uniqueness_derived": False,
        "references_h_and_cleanliness_are_declared_supplies": True,
        "genesis_untouched": True,
        "algebra_scope": (
            "for every finite n>=1 and A,B,h, there exists r making all "
            "declared rows zero iff rail parity equals h; two r extensions "
            "exist when matched, while one fixed r covers only 2^n rails"
        ),
        "circuit_scope": (
            "on the declared fixtures, an active station's dirty charge row "
            "refuses that station's macro and all added scratch is uncomputed"
        ),
        "open_boundary": (
            "no global acceptance bit, autonomous reference preparation, "
            "physical meaning for h, recurrent invariance, or one-token "
            "existence/uniqueness is derived"
        ),
    }
    check(
        "OPEN_BOUNDARY_global_one_token_condition_remains_supplied",
        boundary["local_charge_row_guard_at_every_active_macro"]
        and boundary["existential_reference_projection_theorem"]
        and not boundary[
            "fixed_reference_chain_covers_whole_matching_sector"
        ]
        and not boundary["global_parity_acceptance_constructed"]
        and not boundary[
            "global_one_token_existence_uniqueness_derived"
        ]
        and boundary[
            "references_h_and_cleanliness_are_declared_supplies"
        ],
    )

    elapsed = perf_counter() - started
    padded_physical = physical["banks"][12]
    report: dict[str, object] = {
        "declared_mutable_input_paths": len(AUDIT_INPUT_PATHS),
        "declared_input_closure_exact":
            recovered_input_closure == AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "local_charge_row_guard_at_every_active_macro":
            boundary["local_charge_row_guard_at_every_active_macro"],
        "existential_reference_projection_theorem":
            boundary["existential_reference_projection_theorem"],
        "global_parity_acceptance_constructed": False,
        "static_matched_parity_multitoken_row_witness": True,
        "global_one_token_existence_uniqueness_derived": False,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not passed for passed in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
        "Cycle724_regression_anchor": anchor,
        "circuit_structure": structure,
        "lawful_Q_time_charge_rows": q_time_rows,
        "lawful_charge_extended_wrap": lawful,
        "charge_violation_census": census,
        "projection_and_local_guard": projection_guard,
        "deletion_controls": deletions,
        "physical": physical,
        "compiled_extended_orbit": compiled,
        "inherited_anchors": inherited,
        "word_size_comparison": {
            "Cycle724_semantic_gates": EXPECTED_CYCLE724_PADDED_GATES,
            "Cycle730_semantic_gates": structure["semantic_gates"],
            "added_semantic_gates":
                structure["semantic_gates"]
                - EXPECTED_CYCLE724_PADDED_GATES,
            "Cycle730_to_Cycle724_ratio":
                structure["semantic_gates"]
                / EXPECTED_CYCLE724_PADDED_GATES,
        },
        "physical_12_bank_summary": {
            "semantic_gates":
                padded_physical["controller_semantic_gates"],
            "forward_physical_primitives":
                padded_physical["forward"]["physical_primitives"],
            "forward_routed_NN_gates":
                padded_physical["forward"]["routed_NN_gates"],
            "forward_route_sha256":
                padded_physical["forward"]["route_blueprint_sha256"],
            "inverse_physical_primitives":
                padded_physical["inverse"]["physical_primitives"],
            "inverse_routed_NN_gates":
                padded_physical["inverse"]["routed_NN_gates"],
            "inverse_route_sha256":
                padded_physical["inverse"]["route_blueprint_sha256"],
            "controller_M2": padded_physical["controller_M2"],
            "reference_M2": padded_physical["reference_M2"],
            "charge_scratch_M2":
                padded_physical["charge_scratch_M2"],
            "h_M2": padded_physical["h_M2"],
            "total_declared_M2":
                padded_physical["total_declared_M2"],
        },
        "supplied_inventory": (
            "One source controller token; zero B/work/syndrome/MCX/OR/"
            "charge scratch; a clean static reference chain and h; oriented "
            "program ring and clean data genesis."
        ),
        "claim_boundary": boundary,
        "terminal": (
            "CYCLE730_LOCAL_CHARGE_ROW_GUARD_PASS"
            if all(CHECKS.values())
            else "CYCLE730_LOCAL_CHARGE_ROW_GUARD_HONEST_FAIL"
        ),
    }
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    preliminary = (
        "\n".join(OUTPUT_LINES)
        + "\n"
        + json.dumps(
            report, sort_keys=True, separators=(",", ":"), default=str
        )
        + "\n"
    )
    check(
        "OUTPUT_stdout_under_20000_characters",
        len(preliminary) < STDOUT_LIMIT_CHARACTERS,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not passed for passed in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE730_LOCAL_CHARGE_ROW_GUARD_PASS"
        if report["pass"]
        else "CYCLE730_LOCAL_CHARGE_ROW_GUARD_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    text, exact_size = render_with_exact_size(report)
    if exact_size >= STDOUT_LIMIT_CHARACTERS:
        raise AssertionError(("stdout bound", exact_size))
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
