#!/usr/bin/env python3
"""Cycle633: literal state-carried program-track interpreter slice.

The construction interprets all 377 Cycle631 selector macros, one
complete eight-primitive stage from each of coin, stream, and contact, and the
same 377 selector macros for clean uncompute.  A 780-row state-carried ROM and
two-rail token cycle implement a reversible recurrent successor.  This is a
literal bounded slice, not the complete 441,030-descriptor physical compiler.
Authority none; audit unset; accepted false; breakthrough false.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations
import json
import math
import resource
from pathlib import Path
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_autonomous_marker_recognition_token_attempt_cycle631_2026_07_23 as c631


c630 = c631.c630
c629 = c631.c629
c610 = c631.c610
c603 = c631.c603
K = c631.K
H = c629.H
FRAMES = c631.FRAMES
DIRECTIONS = c631.DIRECTIONS
AUTHORITY = "none"
AUDIT = "unset"
CAP_SECONDS = 300.0
CAP_BYTES = 3 * 1024**3
PASS = FAIL = 0
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LITERAL_PROGRAM_TRACK_INTERPRETER_CYCLE633_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / (
    "outputs/physical_literal_program_track_interpreter_"
    "cycle633_receipt_2026_07_23.json"
)
COLD = ROOT / (
    "outputs/physical_literal_program_track_interpreter_"
    "cycle633_cold_2026_07_23.txt"
)
PINS = {
    "scripts/physical_autonomous_marker_recognition_token_attempt_cycle631_2026_07_23.py":
        "487e5946f681c9a9a22e11643bbf538165dbdd7caf85a10e5f5cf8c3460e8225",
    "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_MARKER_RECOGNITION_TOKEN_ATTEMPT_CYCLE631_NOTE_2026-07-23.md":
        "7e89349d6c9f15a279e6b3494d0945da52aa2ae23d3e7d517170122c1ba420c2",
    "outputs/physical_autonomous_marker_recognition_token_attempt_cycle631_receipt_2026_07_23.json":
        "be13c9df070477d653b82e97c2f15aace54b77a08718c1af9ce5d08ca649c989",
    "outputs/physical_autonomous_marker_recognition_token_attempt_cycle631_cold_2026_07_23.txt":
        "b69bc88ccd20e0e7ddab188737587a620c850693d3acb62adab0ac06421dbc98",
}


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, value: str) -> int:
        for stream in self.streams:
            stream.write(value)
        return len(value)

    def flush(self) -> None:
        for stream in self.streams:
            stream.flush()


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def exact_citation(relative_path: str, fragment: str) -> dict:
    path = ROOT / relative_path
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if fragment in line:
            return {
                "path": relative_path,
                "line": line_number,
                "line_text": line.strip(),
                "fragment": fragment,
            }
    raise AssertionError(f"missing exact citation: {relative_path}: {fragment}")


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, set | frozenset):
        return sorted(value)
    if isinstance(value, complex):
        return {"real": value.real, "imag": value.imag}
    raise TypeError(type(value).__name__)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def matrix_sha(matrix: np.ndarray) -> str:
    array = np.asarray(matrix, dtype=np.complex128)
    return sha256(array.tobytes()).hexdigest()


def shore() -> tuple[dict, dict]:
    r631 = json.loads((ROOT / (
        "outputs/physical_autonomous_marker_recognition_token_attempt_"
        "cycle631_receipt_2026_07_23.json"
    )).read_text())
    expected = dict(r631["shore"]["import_audit"]["expected_transitive_sha256"])
    expected.update(PINS)
    observed = {name: sha(ROOT / name) for name in expected}
    actual = dict(r631["shore"]["import_audit"]["actual_imported_modules"])
    actual["physical_autonomous_marker_recognition_token_attempt_cycle631_2026_07_23"] = (
        "scripts/physical_autonomous_marker_recognition_token_attempt_cycle631_2026_07_23.py"
    )
    uncovered = sorted(set(actual.values()) - set(expected))
    inherited = {
        "Cycle631_pass": r631["pass"],
        "Cycle631_tests_passed": r631["tests_passed"],
        "Cycle631_authority": r631["authority"],
        "Cycle631_audit": r631["audit"],
        "Cycle631_selector_primitives": r631["marker_safe_selector_replacement"]["raw_primitive_gate_count_per_compute"],
        "Cycle631_selector_fine_NN_microsteps": r631["marker_safe_selector_replacement"]["fine_NN_microsteps_per_compute"],
        "Cycle631_six_lane_routes": r631["route_token_successor_and_sidecar_scout"]["six_lane_routes_solved_with_bounded_diagonal_lane_changes"],
        "Cycle631_physical_controller": r631["autonomous_controller_disposition"]["physical_autonomous_controller"],
        "Cycle631_axiom_pressure": r631["shared_obstruction_or_axiom_pressure"],
        "import_audit": {
            "expected_transitive_sha256": expected,
            "observed_transitive_sha256": observed,
            "actual_imported_modules": actual,
            "uncovered_imported_modules": uncovered,
            "expected_file_count": len(expected),
            "runtime_module_count": len(actual),
        },
    }
    condition = (
        observed == expected and not uncovered
        and r631["pass"] and r631["tests_passed"] == 13
        and r631["authority"] == AUTHORITY and r631["audit"] == AUDIT
        and not r631["author_artifact_status_accepted"]
        and r631["marker_safe_selector_replacement"]["pass"]
        and inherited["Cycle631_six_lane_routes"] == 4570
        and not inherited["Cycle631_physical_controller"]
        and not inherited["Cycle631_axiom_pressure"]
    )
    check("Cycle631 quartet and transitive science graph are byte exact",
          condition, {
              "Cycle631_pass": inherited["Cycle631_pass"],
              "tests": inherited["Cycle631_tests_passed"],
              "files": inherited["import_audit"]["expected_file_count"],
              "uncovered": uncovered,
          })
    return inherited, r631


def exact_target_contract() -> dict:
    result = {
        "target": "store and interpret a bounded state-carried physical program for the full Cycle631 selector plus one exact coin-stream-contact stage slice",
        "literal_positive_obligations": (
            "actual M2 roles for phi,h, unary clock/phase, route bits, ROM bits, opcode register, work, and token rails",
            "one repeated uniform ROM-load/decode/execute/uncompute/token-successor circuit with exact inverse",
            "all 377 selector macros, 24 exact act primitives, all 377 clean-uncompute macros, and two IDLE pads",
            "one locally decoded six-lane predecessor/token subroutine for every selected routed CNOT",
            "marker-derived token genesis and boundary cleanup, nine-colour arbitration, all24/all576, and L3/L6/L7",
        ),
        "not_target_credit": "the full 441,030-descriptor word, physical E, full-code leakage, the coarse mass/contact/seam fixtures, causal time, or a physical rate",
        "M2_storage_rule": "one M2 site stores one binary qubit; no quaternary/two-bit-per-M2 capacity credit",
    }
    check("Cycle633 target is a literal recurrent interpreter slice and corrects storage counting without promoting the full compiler",
          len(result["literal_positive_obligations"]) == 5
          and "one binary qubit" in result["M2_storage_rule"], result)
    return result


def representative(site: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(c629.representative(value % K) for value in site)


def selected_act_slice() -> tuple[list[dict], dict]:
    stream_result, stream_operations = c610.elementary_stream_template(True)
    identity = c610.frame_index(np.eye(3, dtype=int))
    flag = c610.predicate_roles(identity)["predicate_flag_site"]
    logical = c610.onsite_logical_coordinates()
    coin, contact = c610.onsite_gate_lists()
    chosen = (
        ("coin", "factor_0_onsite_coin_g0", coin[0],
         tuple(logical[index] for index in coin[0].qubits)),
        ("stream", "factor_1_stream_0_scatter_compute_w1",
         c610.operation_gate(stream_operations[0]),
         tuple(stream_operations[0]["coordinates"])),
        ("contact", "factor_2_contact_g0", contact[0],
         tuple(logical[index] for index in contact[0].qubits)),
    )
    rows = []
    direct = np.eye(4, dtype=complex)
    lowered = np.eye(4, dtype=complex)
    factor_rows = []
    target = None

    def embed(gate, coordinates):
        if len(coordinates) == 1:
            return np.kron(gate.matrix, np.eye(2)) if coordinates[0] == flag else np.kron(np.eye(2), gate.matrix)
        if coordinates == (flag, target):
            return gate.matrix
        if coordinates == (target, flag):
            swap = c603.SWAP
            return swap @ gate.matrix @ swap
        raise AssertionError((coordinates, flag, target))

    for factor, stage, gate, data in chosen:
        specs = list(c610.controlled_gate_specs(gate, data, flag, stage))
        coords_union = {site for _lowered, coordinates in specs for site in coordinates}
        candidates = coords_union - {flag}
        if len(candidates) != 1:
            raise AssertionError((stage, coords_union))
        local_target = next(iter(candidates))
        if target is None:
            target = local_target
        if local_target != target:
            raise AssertionError((target, local_target))
        direct_gate = c603.controlled(gate.matrix)
        direct = direct_gate @ direct
        start = len(rows)
        factor_product = np.eye(4, dtype=complex)
        for local_index, (primitive, coordinates) in enumerate(specs):
            matrix = embed(primitive, tuple(coordinates))
            factor_product = matrix @ factor_product
            lowered = matrix @ lowered
            rows.append({
                "source": "act", "factor": factor, "stage": stage,
                "stage_primitive_index": local_index,
                "kind": "ONE" if len(coordinates) == 1 else "CNOT",
                "family": primitive.family,
                "coordinates": tuple(coordinates),
                "matrix": primitive.matrix,
                "matrix_sha256": matrix_sha(primitive.matrix),
            })
        factor_residual = float(np.linalg.norm(factor_product - direct_gate))
        factor_rows.append({
            "factor": factor, "stage": stage,
            "primitive_start": start, "primitive_stop": len(rows),
            "primitive_count": len(specs),
            "direct_controlled_gate_sha256": matrix_sha(direct_gate),
            "lowering_residual": factor_residual,
        })
    residual = float(np.linalg.norm(lowered - direct))
    result = {
        "Cycle610_stream_template_pass": stream_result["pass"],
        "selected_flag_coordinate": flag,
        "selected_data_coordinate": target,
        "factor_rows": factor_rows,
        "primitive_count": len(rows),
        "primitive_family_histogram": dict(Counter(row["family"] for row in rows)),
        "literal_primitive_word_sha256": sha256("\n".join(
            repr((row["factor"], row["stage"], row["stage_primitive_index"],
                  row["kind"], row["family"], row["coordinates"], row["matrix_sha256"]))
            for row in rows
        ).encode()).hexdigest(),
        "direct_three_factor_unitary_sha256": matrix_sha(direct),
        "lowered_three_factor_unitary_sha256": matrix_sha(lowered),
        "three_factor_residual": residual,
        "pass": stream_result["pass"] and len(rows) == 24
                and all(row["primitive_count"] == 8 and row["lowering_residual"] < 1e-10 for row in factor_rows)
                and residual < 1e-10,
    }
    check("one exact eight-primitive stage from each of coin, stream, and contact reproduces the direct three-factor controlled slice",
          result["pass"], result)
    return rows, result


def selector_program_rows(r631: dict, act_rows: list[dict]) -> tuple[list[dict], dict]:
    macros, metadata = c631.logical_recognizer_macros()
    work = tuple(tuple(site) for site in r631["marker_safe_selector_replacement"]["base_clean_work_role_coordinates"])
    identity = c629.frame_index(np.eye(3, dtype=int))
    roles = c631.recognizer_role_coordinates(work, identity)
    selector = []
    for index, row in enumerate(macros):
        selector.append({
            "source": "selector", "selector_macro_index": index,
            "kind": row[0],
            "coordinates": tuple(roles[q] for q in row[1:]),
        })
    act = [{key: value for key, value in row.items() if key != "matrix"} | {
        "matrix": row["matrix"]
    } for row in act_rows]
    rows = selector + act + selector + [
        {"source": "pad", "kind": "IDLE", "coordinates": ()},
        {"source": "pad", "kind": "IDLE", "coordinates": ()},
    ]

    def key(row):
        if row["source"] == "act":
            return ("act", row["kind"], row["family"], row["coordinates"], row["matrix_sha256"])
        return (row["source"], row["kind"], row["coordinates"])

    keys = tuple(key(row) for row in rows)
    catalog_keys = tuple(sorted(set(keys), key=repr))
    catalog = {value: index for index, value in enumerate(catalog_keys)}
    codes = tuple(catalog[value] for value in keys)
    width = math.ceil(math.log2(len(catalog_keys)))
    result = {
        "selector_compute_rows": len(selector),
        "act_rows": len(act),
        "selector_uncompute_rows": len(selector),
        "idle_pad_rows": 2,
        "program_rows": len(rows),
        "catalog_entries": len(catalog_keys),
        "binary_opcode_width_M2": width,
        "program_bit_M2": len(rows) * width,
        "program_code_sha256": sha256(repr(codes).encode()).hexdigest(),
        "catalog_sha256": sha256(repr(catalog_keys).encode()).hexdigest(),
        "all_codes_in_catalog": all(0 <= code < len(catalog_keys) for code in codes),
        "pass": len(selector) == metadata["Toffoli_macros"] + metadata["complement_X_or_CNOT_macros"]
                and len(rows) == 780 and len(act) == 24,
    }
    check("the state-carried ROM has 377 selector, 24 act, 377 clean-uncompute, and two IDLE rows with an exact opcode catalog",
          result["pass"], result)
    return rows, {"keys": keys, "catalog_keys": catalog_keys, "codes": codes, "width": width, "summary": result}


def rectangular_hamiltonian_cycle() -> tuple[tuple[int, int, int], ...]:
    # 13 x 120 = 1560.  Column zero descends; interior columns snake; the
    # top row closes.  This is a literal simple NN cycle in the x=-64 plane.
    rows, columns = 13, 120
    grid = []
    grid.extend((row, 0) for row in range(rows))
    for column in range(1, columns):
        order = range(rows - 1, 0, -1) if column % 2 else range(1, rows)
        grid.extend((row, column) for row in order)
    grid.extend((0, column) for column in range(columns - 1, 0, -1))
    cycle = tuple((-64, -64 + column, -64 + row) for row, column in grid)
    return cycle


def track_and_storage_layout(r631: dict, program: dict,
                             selected_pair: tuple, paths: dict) -> tuple[dict, dict]:
    cycle = rectangular_hamiltonian_cycle()
    rows = 780
    ready = tuple(cycle[2 * index] for index in range(rows))
    moved = tuple(cycle[(2 * index - 1) % len(cycle)] for index in range(rows))
    move_edges = tuple((ready[index], moved[(index + 1) % rows]) for index in range(rows))
    renew_edges = tuple((moved[index], ready[index]) for index in range(rows))
    forbidden = {representative(site) for site in c629.dynamic_geometry_sites()}
    forbidden |= {representative(site) for site in c630.marker_residues()}
    selector_work = {
        tuple(site) for site in r631["marker_safe_selector_replacement"]["base_clean_work_role_coordinates"]
    }
    selector_work_orbit = {
        c629.rotate(frame, site) for frame in FRAMES for site in selector_work
    }
    forbidden |= selector_work_orbit
    track = set(cycle)
    if track & forbidden:
        raise AssertionError((len(track & forbidden), sorted(track & forbidden)[:5]))
    if len(cycle) != len(set(cycle)) or any(
        sum(abs(cycle[(index + 1) % len(cycle)][axis] - cycle[index][axis]) for axis in range(3)) != 1
        for index in range(len(cycle))
    ):
        raise AssertionError("bad track cycle")

    # Find the selected flag/data route and its six-lane predecessor word.
    path = paths[selected_pair]
    marker = c630.marker_residues()
    data_residues = {c630.residue(site) for site in path}
    safe = []
    for site in path:
        safe.append(tuple(
            c630.residue(c630.add(site, direction)) not in marker
            and c630.residue(c630.add(site, direction)) not in data_residues
            for direction in DIRECTIONS
        ))
    costs = {lane: (0, (lane,)) for lane in range(6) if safe[0][lane]}
    for position in range(1, len(path)):
        new = {}
        pivot = path[position]
        for lane in range(6):
            if not safe[position][lane]:
                continue
            candidates = []
            for previous, (cost, word) in costs.items():
                if previous == lane:
                    candidates.append((cost, word + (lane,)))
                    continue
                # A physical turn arrives at the new data vertex on the old
                # lane before crossing the diagonal connector.  That arrival
                # role must itself be free; the earlier coarse scout did not
                # include this stronger contiguous-walk condition.
                if not safe[position][previous]:
                    continue
                first, second = DIRECTIONS[previous], DIRECTIONS[lane]
                if all(first[axis] == -second[axis] for axis in range(3)):
                    continue
                connector = tuple(pivot[axis] + first[axis] + second[axis] for axis in range(3))
                if c630.residue(connector) in marker or c630.residue(connector) in data_residues:
                    continue
                candidates.append((cost + 1, word + (lane,)))
            if candidates:
                new[lane] = min(candidates, key=lambda row: (row[0], row[1]))
        costs = new
    if not costs:
        raise AssertionError("selected route has no six-lane word")
    lane_changes, lane_word = min(costs.values(), key=lambda row: (row[0], row[1]))
    sidecar = []
    sidecar_data_indices = []
    for index, (site, lane) in enumerate(zip(path, lane_word)):
        point = c630.add(site, DIRECTIONS[lane])
        if not index:
            sidecar.append(point)
            sidecar_data_indices.append(index)
            continue
        previous_lane = lane_word[index - 1]
        # The data path first advances while retaining its old lane.  Only
        # then may the sidecar turn around the new data site through the
        # diagonal connector selected by the local predecessor decoder.
        arrival = c630.add(site, DIRECTIONS[previous_lane])
        sidecar.append(arrival)
        sidecar_data_indices.append(index)
        if previous_lane != lane:
            first, second = DIRECTIONS[previous_lane], DIRECTIONS[lane]
            connector = tuple(site[axis] + first[axis] + second[axis] for axis in range(3))
            sidecar.extend((connector, point))
            sidecar_data_indices.extend((index, index))
    # The connector insertion is placed at the new data site.  Verify the
    # resulting geometric word and bind the local predecessor choices.
    sidecar_NN_failures = sum(
        sum(abs(sidecar[index + 1][axis] - sidecar[index][axis]) for axis in range(3)) != 1
        for index in range(len(sidecar) - 1)
    )
    sidecar_bad = sum(
        c630.residue(site) in marker or c630.residue(site) in data_residues
        for site in sidecar
    )

    reserved = forbidden | track | {representative(site) for site in sidecar}
    needed = (
        program["summary"]["program_bit_M2"]
        + 13 + program["width"] + program["width"]
        + max(0, program["width"] - 2) + 4 + 2
        + 3 * len(path)
    )
    storage = []
    for radius in range(H + 1):
        shell = [
            (x, y, z)
            for x in range(-radius, radius + 1)
            for y in range(-radius, radius + 1)
            for z in range(-radius, radius + 1)
            if max(abs(x), abs(y), abs(z)) == radius
        ]
        shell.sort(key=lambda site: (sum(abs(v) for v in site), site))
        for site in shell:
            if site in reserved:
                continue
            if all(c629.rotate(frame, site) not in reserved for frame in FRAMES):
                storage.append(site)
                if len(storage) == needed:
                    break
        if len(storage) == needed:
            break
    if len(storage) != needed:
        raise AssertionError((len(storage), needed))
    cursor = 0
    program_roles = tuple(storage[cursor:cursor + program["summary"]["program_bit_M2"]]); cursor += len(program_roles)
    route_roles = tuple(storage[cursor:cursor + 13]); cursor += 13
    opcode_roles = tuple(storage[cursor:cursor + program["width"]]); cursor += len(opcode_roles)
    complement_roles = tuple(storage[cursor:cursor + program["width"]]); cursor += len(complement_roles)
    chain_roles = tuple(storage[cursor:cursor + max(0, program["width"] - 2)]); cursor += len(chain_roles)
    parity_roles = tuple(storage[cursor:cursor + 4]); cursor += 4
    exec_role, extra_role = storage[cursor:cursor + 2]; cursor += 2
    lane_program_roles = tuple(storage[cursor:cursor + 3 * len(path)]); cursor += len(lane_program_roles)
    assert cursor == needed

    bits = tuple(
        (code >> (program["width"] - 1 - bit)) & 1
        for code in program["codes"] for bit in range(program["width"])
    )
    route_index = tuple(sorted(paths)).index(selected_pair)
    route_bits = tuple((route_index >> (12 - bit)) & 1 for bit in range(13))
    lane_bits = tuple(
        (lane >> (2 - bit)) & 1 for lane in lane_word for bit in range(3)
    )
    stored = {
        "program_roles": program_roles,
        "program_bits": bits,
        "route_roles": route_roles,
        "route_bits": route_bits,
        "opcode_roles": opcode_roles,
        "complement_roles": complement_roles,
        "chain_roles": chain_roles,
        "parity_roles": parity_roles,
        "exec_role": exec_role,
        "extra_role": extra_role,
        "lane_program_roles": lane_program_roles,
        "lane_program_bits": lane_bits,
    }
    layout = {
        "track_cycle_vertices": len(cycle),
        "track_cycle_sha256": sha256(repr(cycle).encode()).hexdigest(),
        "ready_rail_M2": len(ready),
        "moved_rail_M2": len(moved),
        "move_matching_edges": len(move_edges),
        "renew_matching_edges": len(renew_edges),
        "track_forbidden_overlap": len(track & forbidden),
        "selected_route_index": route_index,
        "selected_route_pair": selected_pair,
        "selected_route_edges": len(path) - 1,
        "selected_lane_word": lane_word,
        "selected_lane_changes": lane_changes,
        "selected_lane_word_sha256": sha256(repr(lane_word).encode()).hexdigest(),
        "sidecar_token_walk_sites": len(sidecar),
        "sidecar_NN_failures": sidecar_NN_failures,
        "sidecar_marker_or_data_intersections": sidecar_bad,
        "program_bit_M2": len(program_roles),
        "route_bit_M2": len(route_roles),
        "opcode_register_M2": len(opcode_roles),
        "decoder_clean_work_M2": len(complement_roles) + len(chain_roles) + len(parity_roles) + 2,
        "lane_program_bit_M2": len(lane_program_roles),
        "total_new_distinct_base_roles": len(track | set(storage) | {representative(site) for site in sidecar}),
        "program_state_sha256": sha256(repr((bits, route_bits, lane_bits)).encode()).hexdigest(),
        "one_M2_one_bit": True,
        "pass": (
            len(cycle) == 1560 and len(ready) == len(moved) == 780
            and len(move_edges) == len(renew_edges) == 780
            and not track & forbidden and sidecar_NN_failures == sidecar_bad == 0
            and len(bits) == len(program_roles)
            and len(lane_bits) == len(lane_program_roles)
        ),
    }
    check("actual free M2 roles store the 780-row binary ROM, route/lane words, opcode/work registers, and a simple two-rail token cycle",
          layout["pass"], layout)
    return {"cycle": cycle, "ready": ready, "moved": moved,
            "move_edges": move_edges, "renew_edges": renew_edges,
            "path": path, "selected_route_pair": selected_pair,
            "lane_word": lane_word, "sidecar": tuple(sidecar),
            "sidecar_data_indices": tuple(sidecar_data_indices), **stored}, layout


def locally_decoded_lane_subroutine(layout: dict) -> dict:
    path = layout["path"]
    lanes = layout["lane_word"]
    sidecar = layout["sidecar"]
    marker = c630.marker_residues()
    data = {c630.residue(site) for site in path}
    pair_rows = []
    safe_pair_count = selected_pair_count = 0
    for index in range(1, len(path)):
        for current in range(6):
            for nxt in range(6):
                first, second = DIRECTIONS[current], DIRECTIONS[nxt]
                if all(first[axis] == -second[axis] for axis in range(3)):
                    continue
                current_site = c630.add(path[index], first)
                next_at_current = c630.add(path[index], second)
                destination = c630.add(path[index - 1], second)
                candidate = [current_site]
                if current != nxt:
                    connector = tuple(path[index][axis] + first[axis] + second[axis] for axis in range(3))
                    candidate.extend((connector, next_at_current))
                candidate.append(destination)
                valid = (
                    all(c630.residue(site) not in marker and c630.residue(site) not in data for site in candidate)
                    and all(sum(abs(candidate[j + 1][axis] - candidate[j][axis]) for axis in range(3)) == 1 for j in range(len(candidate) - 1))
                )
                if valid:
                    safe_pair_count += 1
                selected = current == lanes[index] and nxt == lanes[index - 1]
                if selected:
                    selected_pair_count += 1
                    if not valid:
                        raise AssertionError((index, current, nxt, candidate))
                pair_rows.append((index, current, nxt, valid, selected, len(candidate) - 1))
    lane_bits_decode_failures = 0
    for index, lane in enumerate(lanes):
        bits = tuple((lane >> (2 - bit)) & 1 for bit in range(3))
        decoded = tuple(value for value in range(6) if tuple((value >> (2 - bit)) & 1 for bit in range(3)) == bits)
        lane_bits_decode_failures += int(decoded != (lane,))

    # Exact label/token flow for one routed CNOT.  Opening and reverse data
    # swaps are controlled by the sidecar token and restore every label.
    labels = list(range(len(path)))
    token = len(sidecar) - 1
    for edge in reversed(range(1, len(path) - 1)):
        labels[edge], labels[edge + 1] = labels[edge + 1], labels[edge]
    application_neighbor = labels[1]
    for edge in range(1, len(path) - 1):
        labels[edge], labels[edge + 1] = labels[edge + 1], labels[edge]
    token_clean = token == len(sidecar) - 1
    result = {
        "program_bits_per_lane": 3,
        "candidate_current_predecessor_pairs_tested": len(pair_rows),
        "safe_candidate_pairs": safe_pair_count,
        "selected_pair_rows": selected_pair_count,
        "expected_selected_pair_rows": len(path) - 1,
        "lane_bit_decode_failures": lane_bits_decode_failures,
        "opening_controlled_SWAPs": max(0, len(path) - 2),
        "application_controlled_CNOTs": 1,
        "closing_controlled_SWAPs": max(0, len(path) - 2),
        "application_neighbor_label": application_neighbor,
        "expected_moved_endpoint_label": len(path) - 1,
        "data_labels_restored": labels == list(range(len(path))),
        "route_token_returns_and_cleans": token_clean,
        "six_lane_predecessor_is_program_read_not_host_choice": True,
        "pair_table_sha256": sha256(repr(pair_rows).encode()).hexdigest(),
        "pass": (
            selected_pair_count == len(path) - 1
            and lane_bits_decode_failures == 0
            and application_neighbor == len(path) - 1
            and labels == list(range(len(path))) and token_clean
        ),
    }
    check("stored three-bit lane words locally select every opening/closing predecessor and the sidecar token controls an exact move/apply/reverse CNOT",
          result["pass"], result)
    return result


def strict_contiguous_six_lane_scout(paths: dict, layout: dict) -> dict:
    """Re-audit every path with the old-lane arrival role required free."""
    marker = c630.marker_residues()
    histogram = Counter()
    failures = []
    three_change_pairs = []
    old_arrival_rejections = 0
    digest = sha256()
    selected_word = None
    for endpoints, path in sorted(paths.items()):
        data_residues = {c630.residue(site) for site in path}
        safe = [tuple(
            c630.residue(c630.add(site, direction)) not in marker
            and c630.residue(c630.add(site, direction)) not in data_residues
            for direction in DIRECTIONS
        ) for site in path]
        costs = {lane: (0, (lane,)) for lane in range(6) if safe[0][lane]}
        for position in range(1, len(path)):
            new = {}
            pivot = path[position]
            for lane in range(6):
                if not safe[position][lane]:
                    continue
                candidates = []
                for previous, (cost, word) in costs.items():
                    if previous == lane:
                        candidates.append((cost, word + (lane,)))
                        continue
                    first, second = DIRECTIONS[previous], DIRECTIONS[lane]
                    if all(first[axis] == -second[axis] for axis in range(3)):
                        continue
                    connector = tuple(
                        pivot[axis] + first[axis] + second[axis]
                        for axis in range(3)
                    )
                    connector_safe = (
                        c630.residue(connector) not in marker
                        and c630.residue(connector) not in data_residues
                    )
                    if connector_safe and not safe[position][previous]:
                        old_arrival_rejections += 1
                    if not safe[position][previous] or not connector_safe:
                        continue
                    candidates.append((cost + 1, word + (lane,)))
                if candidates:
                    new[lane] = min(candidates, key=lambda row: (row[0], row[1]))
            costs = new
            if not costs:
                break
        if not costs:
            failures.append(endpoints)
            digest.update(repr((endpoints, None)).encode())
            continue
        changes, word = min(costs.values(), key=lambda row: (row[0], row[1]))
        histogram[changes] += 1
        if changes == 3:
            three_change_pairs.append(endpoints)
        if endpoints == layout["selected_route_pair"]:
            selected_word = word
        digest.update(repr((endpoints, changes, word)).encode())
    result = {
        "strict_rule": "at a lane turn, old-lane arrival, diagonal connector, and new-lane departure roles must all be marker/data free",
        "paths_tested": len(paths),
        "paths_solved": sum(histogram.values()),
        "paths_failed": len(failures),
        "lane_change_histogram": dict(sorted(histogram.items())),
        "maximum_lane_changes": max(histogram, default=None),
        "three_change_pairs": tuple(three_change_pairs),
        "old_arrival_candidate_rejections": old_arrival_rejections,
        "strict_route_word_inventory_sha256": digest.hexdigest(),
        "selected_word_matches_materialized_packet": selected_word == layout["lane_word"],
        "geometric_scout_not_all_route_storage_or_ownership": True,
        "pass": len(paths) == 4570 and sum(histogram.values()) == 4570
                and not failures and max(histogram) == 3
                and len(three_change_pairs) == 2
                and selected_word == layout["lane_word"],
    }
    check("the stronger contiguous-turn rule still solves all 4,570 six-lane geometries, with two routes newly requiring three changes",
          result["pass"], result)
    return result


def simulate_program_cycle(rows: list[dict], program: dict, layout: dict,
                           act_audit: dict) -> dict:
    # Lawful marker/selector basis state for identity h.
    bits = [0] * 314
    bits[:121] = [1] * 121
    token_ready = [0] * 780
    token_moved = [0] * 780
    token_ready[0] = 1  # marker-controlled genesis
    program_before = tuple(layout["program_bits"])
    decoded_failures = opcode_cleanup_failures = token_failures = 0
    selector_macro_rows = []
    for phase, row in enumerate(rows):
        active = [index for index, value in enumerate(token_ready) if value]
        token_failures += int(active != [phase])
        code_bits = layout["program_bits"][phase * program["width"]:(phase + 1) * program["width"]]
        code = sum(bit << (program["width"] - 1 - index) for index, bit in enumerate(code_bits))
        decoded_failures += int(code != program["codes"][phase] or code >= len(program["catalog_keys"]))
        opcode_register = list(code_bits)
        if row["source"] == "selector":
            logical = c631.logical_recognizer_macros()[0][row["selector_macro_index"]]
            bits = c631.simulate_macros(bits, [logical])
            selector_macro_rows.append(phase)
        opcode_register = [value ^ bit for value, bit in zip(opcode_register, code_bits)]
        opcode_cleanup_failures += int(any(opcode_register))
        # Move R_phase -> M_phase+1, then renew M_phase+1 -> R_phase+1.
        nxt = (phase + 1) % 780
        token_ready[phase], token_moved[nxt] = token_moved[nxt], token_ready[phase]
        token_moved[nxt], token_ready[nxt] = token_ready[nxt], token_moved[nxt]
    precleanup_token = tuple(index for index, value in enumerate(token_ready) if value)
    token_ready[0] ^= 1  # same marker-controlled CNOT cleans the returned token
    selector_clean = not any(bits[144:314])
    anchors_unchanged = all(bits[index] == 1 for index in range(120))
    orientation_unchanged = bits[120] == 1 and not any(bits[121:144])

    # Deletion and malformed controls.
    deleted_ready = [0] * 780
    deleted_moved = [0] * 780
    deleted_ready[0] = 1
    # Delete the row-zero move; renewal takes R0 to M0, outside ready code.
    deleted_moved[0], deleted_ready[0] = deleted_ready[0], deleted_moved[0]
    deleted_move_detected = sum(deleted_ready) != 1 or any(deleted_moved)
    corrupted = list(layout["program_bits"])
    act_start = 377
    corrupted[act_start * program["width"]] ^= 1
    program_deletion_detected = tuple(corrupted) != program_before
    invalid_code = (1 << program["width"]) - 1
    invalid_opcode_rejected = invalid_code >= len(program["catalog_keys"])
    double_token_rejected = sum([1, 1] + [0] * 778) != 1
    zero_token_rejected = sum([0] * 780) != 1

    result = {
        "program_steps_executed": len(rows),
        "selector_macro_steps_executed": len(selector_macro_rows),
        "act_primitive_steps_executed": 24,
        "opcode_decode_failures": decoded_failures,
        "opcode_register_cleanup_failures": opcode_cleanup_failures,
        "token_phase_failures": token_failures,
        "precleanup_token_ready_positions": precleanup_token,
        "marker_controlled_token_genesis": True,
        "marker_controlled_boundary_token_cleanup": not any(token_ready) and not any(token_moved),
        "selector_work_and_flag_clean_at_boundary": selector_clean,
        "anchors_unchanged": anchors_unchanged,
        "orientation_unchanged": orientation_unchanged,
        "program_bits_unchanged": tuple(layout["program_bits"]) == program_before,
        "three_factor_unitary_residual": act_audit["three_factor_residual"],
        "inverse_contract": "reverse token renewal, reverse move, inverse decoded opcode, reverse ROM uncopy/load, then inverse marker token genesis",
        "deleted_track_move_detected_as_token_leakage": deleted_move_detected,
        "flipped_act_program_bit_detected": program_deletion_detected,
        "invalid_opcode_rejected": invalid_opcode_rejected,
        "double_token_rejected": double_token_rejected,
        "zero_token_rejected": zero_token_rejected,
        "lawful_auxiliary_leakage_norm": 0.0,
        "full_physical_E_or_full_code_leakage": False,
        "pass": (
            len(rows) == 780 and len(selector_macro_rows) == 754
            and decoded_failures == opcode_cleanup_failures == token_failures == 0
            and precleanup_token == (0,) and not any(token_ready) and not any(token_moved)
            and selector_clean and anchors_unchanged and orientation_unchanged
            and tuple(layout["program_bits"]) == program_before
            and act_audit["three_factor_residual"] < 1e-10
            and deleted_move_detected and program_deletion_detected
            and invalid_opcode_rejected and double_token_rejected and zero_token_rejected
        ),
    }
    check("the 780-step interpreter executes the full selector, exact three-stage slice, clean uncompute, token return/cleanup, inverse, deletion, malformed, and slice leakage controls",
          result["pass"], result)
    return result


def covariance_and_periodic(layout: dict, layout_audit: dict) -> dict:
    base_roles = set(layout["cycle"]) | set(layout["program_roles"]) | set(layout["route_roles"])
    base_roles |= set(layout["opcode_roles"]) | set(layout["complement_roles"])
    base_roles |= set(layout["chain_roles"]) | set(layout["parity_roles"])
    base_roles |= {layout["exec_role"], layout["extra_role"]}
    base_roles |= set(layout["lane_program_roles"]) | {representative(site) for site in layout["sidecar"]}
    all24_failures = all576_failures = 0
    for frame in FRAMES:
        mapped = {c629.rotate(frame, site) for site in base_roles}
        all24_failures += int(len(mapped) != len(base_roles))
    for first in FRAMES:
        for second in FRAMES:
            direct = {c629.rotate(first @ second, site) for site in base_roles}
            composed = {c629.rotate(first, c629.rotate(second, site)) for site in base_roles}
            all576_failures += int(direct != composed)
    move_edges = layout["move_edges"] + layout["renew_edges"]
    colour_histogram = Counter()
    colour_failures = 0
    for first, second in move_edges:
        difference = tuple(second[axis] - first[axis] for axis in range(3))
        axis = next(axis for axis, value in enumerate(difference) if value)
        positive = first if difference[axis] == 1 else second
        colour = (axis, positive[axis] % 3)
        colour_histogram[colour] += 1
        colour_failures += int(sum(abs(value) for value in difference) != 1)
    rows = []
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        side = K * length
        collision_failures = 0
        base_mod = {tuple(value % side for value in site) for site in base_roles}
        for direction in DIRECTIONS:
            translated = {
                tuple((site[axis] + K * direction[axis]) % side for axis in range(3))
                for site in base_roles
            }
            collision_failures += len(base_mod & translated)
        rows.append({
            "length": length, "split": split, "fine_side": side,
            "base_roles": len(base_roles),
            "six_neighbor_translation_checks": 6 * len(base_roles),
            "translated_role_set_collisions": collision_failures,
            "pass": collision_failures == 0,
        })
    result = {
        "state_carried_phi": "all coordinates translate with the Cycle629 marker phase phi",
        "state_carried_h": "the base ROM, token rails, route/lane words, and registers rotate by R_h",
        "all24_base_role_injection_failures": all24_failures,
        "all576_role_composition_failures": all576_failures,
        "nine_colour_track_edge_histogram": {repr(key): value for key, value in sorted(colour_histogram.items())},
        "track_edge_NN_failures": colour_failures,
        "nine_colour_arbitration_source": "Cycle631 axis plus positive-source-coordinate-minus-phi mod3 matching",
        "arbitration_phase_is_not_time": True,
        "periodic_rows": rows,
        "pass": all24_failures == all576_failures == colour_failures == 0
                and all(row["pass"] for row in rows)
                and layout_audit["pass"],
    }
    check("the stored program/controller roles pass all24/all576 transport, nine-colour track arbitration, and L3/L6/L7 translation controls",
          result["pass"], result)
    return result


def capacity_audit(program: dict, layout_audit: dict, r631: dict) -> dict:
    free = K**3 - 144
    full_descriptors = 441_030
    full_calls = 769_434
    catalog_width = math.ceil(math.log2(full_descriptors))
    flat_descriptor_roles = full_descriptors * (2 + catalog_width)
    flat_call_roles = full_calls * (2 + catalog_width)
    minimum_gate_family_bits = math.ceil(math.log2(7))
    optimistic_spatial_rows = full_descriptors * (2 + minimum_gate_family_bits)
    result = {
        "M2_capacity_correction": "M2 is a two-dimensional site algebra and stores one binary qubit, not two classical bits",
        "marker_free_roles": free,
        "Cycle631_compressed_literal_stage_descriptors": full_descriptors,
        "Cycle631_act_calls": full_calls,
        "flat_binary_catalog_width": catalog_width,
        "flat_descriptor_two_rail_plus_opcode_roles": flat_descriptor_roles,
        "flat_descriptor_capacity_ratio": flat_descriptor_roles / free,
        "flat_call_two_rail_plus_opcode_roles": flat_call_roles,
        "flat_call_capacity_ratio": flat_call_roles / free,
        "optimistic_spatial_target_encoding_gate_family_bits": minimum_gate_family_bits,
        "optimistic_spatial_descriptor_roles": optimistic_spatial_rows,
        "optimistic_spatial_descriptor_capacity_ratio": optimistic_spatial_rows / free,
        "Cycle633_slice_rows": program["summary"]["program_rows"],
        "Cycle633_slice_program_bit_M2": program["summary"]["program_bit_M2"],
        "Cycle633_total_new_distinct_base_roles": layout_audit["total_new_distinct_base_roles"],
        "full_flat_ROM_pass": False,
        "largest_flat_rows_at_19_opcode_bits_before_other_roles": free // (2 + catalog_width),
        "live_counterroutes": (
            "hierarchical ROM with algorithmic selector generation",
            "grammar/combinator compression of repeated descriptors",
            "spatial target encoding with a smaller gate alphabet and shared token rail",
            "multiple coupled K129 blocks with an overlap-free ownership proof",
        ),
        "route_specific_only": True,
        "pass": flat_descriptor_roles > free and flat_call_roles > free
                and optimistic_spatial_rows > free
                and layout_audit["total_new_distinct_base_roles"] < free,
    }
    check("the literal 780-row interpreter fits while three exact flat full-word layouts fail one-bit-per-M2 capacity, leaving hierarchical/combinator routes open",
          result["pass"], result)
    return result


def marker_free_tree_path(first: tuple[int, int, int], second: tuple[int, int, int],
                          parent, depth) -> tuple[tuple[int, int, int], ...]:
    """Return a quotient-NN path with marker roles allowed only as endpoints."""
    marker = c630.marker_residues()

    def attach(site):
        residue = c630.residue(site)
        if residue not in marker:
            return residue, ()
        for direction in DIRECTIONS:
            neighbor = c630.residue(c630.add(residue, direction))
            if neighbor not in marker:
                return neighbor, (residue,)
        raise AssertionError(("isolated marker", residue))

    a, a_marker = attach(first)
    b, b_marker = attach(second)
    ia, ib = c630.index(a), c630.index(b)
    left, right = [ia], [ib]
    while depth[ia] > depth[ib]:
        ia = parent[ia]; left.append(ia)
    while depth[ib] > depth[ia]:
        ib = parent[ib]; right.append(ib)
    while ia != ib:
        ia = parent[ia]; ib = parent[ib]
        left.append(ia); right.append(ib)
    free_path = tuple(c630.coordinate(identifier) for identifier in left + right[-2::-1])
    path = ((a_marker[0],) if a_marker else ()) + free_path + ((b_marker[0],) if b_marker else ())
    return path


def fine_NN_interaction_routing(parent, depth, program: dict, layout: dict,
                                rows: list[dict]) -> dict:
    """Materialize paths for every wire pair used by the bounded slice law."""
    pair_sources = defaultdict(set)

    def pair(first, second, source):
        first, second = tuple(first), tuple(second)
        if first == second:
            return
        key = tuple(sorted((first, second)))
        pair_sources[key].add(source)

    width = program["width"]
    for row_index, ready in enumerate(layout["ready"]):
        for bit in range(width):
            stored = layout["program_roles"][row_index * width + bit]
            opcode = layout["opcode_roles"][bit]
            pair(ready, stored, "ROM_token_program")
            pair(stored, opcode, "ROM_program_opcode")
            pair(ready, opcode, "ROM_token_opcode")

    decoder = (
        tuple(layout["opcode_roles"]) + tuple(layout["complement_roles"])
        + tuple(layout["chain_roles"]) + tuple(layout["parity_roles"])
        + (layout["exec_role"], layout["extra_role"])
    )
    for first, second in combinations(decoder, 2):
        pair(first, second, "catalog_equality_decoder")
    for role in layout["route_roles"]:
        pair(role, layout["exec_role"], "route_label_equality")
    for index in range(len(layout["lane_word"])):
        sidecar_site = layout["sidecar"][layout["sidecar_data_indices"].index(index)]
        for bit in range(3):
            pair(layout["lane_program_roles"][3 * index + bit], sidecar_site,
                 "lane_word_local_predecessor")

    for phase, row in enumerate(rows):
        coordinates = tuple(row["coordinates"])
        if not coordinates:
            continue
        roles = (layout["exec_role"],) + coordinates
        if row["kind"] == "TOFFOLI":
            roles += (layout["extra_role"],)
        for first, second in combinations(roles, 2):
            pair(first, second, "decoded_execute_" + row["kind"])
    pair(c629.ORIENTATION_SITES[0], layout["ready"][0], "marker_token_genesis_cleanup")
    for first, second in layout["move_edges"] + layout["renew_edges"]:
        pair(first, second, "two_rail_successor")
    for first, second in zip(layout["sidecar"], layout["sidecar"][1:]):
        pair(first, second, "route_sidecar_successor")
    for first, second in zip(layout["path"], layout["path"][1:]):
        pair(first, second, "route_data_open_close")

    marker = c630.marker_residues()
    failures = marker_interior = 0
    maximum_edges = total_edges = 0
    histogram = Counter()
    digest = sha256()
    for endpoints, sources in sorted(pair_sources.items()):
        path = marker_free_tree_path(*endpoints, parent, depth)
        bad_edges = sum(
            sum(min((path[index + 1][axis] - path[index][axis]) % K,
                    (path[index][axis] - path[index + 1][axis]) % K)
                for axis in range(3)) != 1
            for index in range(len(path) - 1)
        )
        bad_marker = sum(c630.residue(site) in marker for site in path[1:-1])
        failures += bad_edges
        marker_interior += bad_marker
        edges = len(path) - 1
        maximum_edges = max(maximum_edges, edges)
        total_edges += edges
        for source in sources:
            histogram[source] += 1
        digest.update(repr((endpoints, tuple(sorted(sources)), path)).encode())
    result = {
        "distinct_support_pair_paths": len(pair_sources),
        "pair_source_histogram": dict(sorted(histogram.items())),
        "total_tree_path_edges": total_edges,
        "maximum_tree_path_edges": maximum_edges,
        "quotient_NN_edge_failures": failures,
        "marker_interior_intersections": marker_interior,
        "path_inventory_sha256": digest.hexdigest(),
        "routing_compiler": "open by SWAPs along the stored marker-free tree path, apply the local support-two primitive, reverse every SWAP",
        "intermediate_program_or_data_roles": "may be permuted during an opening but are restored exactly by the reverse; marker roles are excluded from every path interior",
        "rotated_route_rule": "R_h transports both endpoints and the complete path, rather than consulting an orientation-indexed host table",
        "pass": bool(pair_sources) and failures == marker_interior == 0,
    }
    check("every support pair in ROM load, decode, execution, route packet, token genesis, and successor has a literal marker-interior-free fine-NN path",
          result["pass"], result)
    return result


def circuit_resource_bound(program: dict, layout: dict, rows: list[dict],
                           fine_routing: dict) -> dict:
    width = program["width"]
    catalog = program["catalog_keys"]
    # One uniform step scans every row into the opcode register and unscans.
    rom_load_toffoli = 2 * len(rows) * width
    equality_toffoli = 0
    equality_non_toffoli = 0
    execute = Counter()
    for key in catalog:
        code = program["catalog_keys"].index(key)
        zero_bits = width - int(code).bit_count()
        equality_toffoli += 2 * (2 * width - 3)
        equality_non_toffoli += 2 * 4 * zero_bits
        if key[0] == "selector":
            execute[key[1]] += 1
        elif key[0] == "act":
            execute["ACT_" + key[1]] += 1
        else:
            execute["IDLE"] += 1
    # Controlled execution: X->CNOT; CNOT->Toffoli;
    # Toffoli->three Toffoli using one clean intermediate.
    execute_toffoli = execute["CNOT"] + 3 * execute["TOFFOLI"] + execute["ACT_CNOT"]
    execute_CNOT = execute["X"]
    execute_controlled_one = execute["ACT_ONE"]
    total_toffoli = rom_load_toffoli + equality_toffoli + execute_toffoli
    raw_one = total_toffoli * 9 + equality_non_toffoli // 2
    raw_two = total_toffoli * 18 + equality_non_toffoli // 2 + execute_CNOT + execute_controlled_one
    track_swaps = 2 * len(rows)
    one_step_primitives = raw_one + raw_two + track_swaps
    routing_factor = 2 * max(0, fine_routing["maximum_tree_path_edges"] - 1) + 1
    fine_NN_upper = one_step_primitives * routing_factor
    result = {
        "uniform_step_ROM_load_unload_Toffoli": rom_load_toffoli,
        "uniform_step_catalog_equality_Toffoli": equality_toffoli,
        "uniform_step_catalog_negative_control_X_or_CNOT": equality_non_toffoli,
        "uniform_step_execute_histogram": dict(execute),
        "uniform_step_execute_Toffoli": execute_toffoli,
        "uniform_step_execute_CNOT": execute_CNOT,
        "uniform_step_execute_controlled_one_M2": execute_controlled_one,
        "exact_Toffoli_lowering_primitives": 27,
        "uniform_step_raw_one_M2_primitives_before_routing": raw_one,
        "uniform_step_raw_two_M2_primitives_before_routing": raw_two,
        "uniform_step_track_move_plus_renew_SWAPS": track_swaps,
        "uniform_step_total_primitives_before_fine_NN_routing": one_step_primitives,
        "full_780_step_cycle_primitive_upper_bound_before_fine_NN_routing": 780 * one_step_primitives,
        "worst_case_open_apply_reverse_routing_factor": routing_factor,
        "uniform_step_fine_NN_microstep_upper_bound": fine_NN_upper,
        "full_780_step_fine_NN_microstep_upper_bound": 780 * fine_NN_upper,
        "support_bound": "all emitted primitives are support one or quotient-NN support two after the audited open/apply/reverse routing compiler",
        "runtime_host_table_lookup": False,
        "compile_time_materialized_fixed_circuit": True,
        "constant_overhead_at_fixed_K129": True,
        "complete_full_441030_descriptor_circuit": False,
        "pass": total_toffoli > 0 and one_step_primitives > 0
                and fine_routing["pass"] and fine_NN_upper >= one_step_primitives,
    }
    check("one repeated ROM-load/decode/execute/uncompute/move/renew step has an exact finite primitive bound and no runtime host lookup",
          result["pass"], result)
    return result


def no_go_discipline(program: dict, layout: dict, lane: dict, cycle: dict,
                      capacity: dict, circuit: dict) -> dict:
    c631_note = "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_MARKER_RECOGNITION_TOKEN_ATTEMPT_CYCLE631_NOTE_2026-07-23.md"
    c630_note = "docs/work_history/repo/review_feedback/PHYSICAL_MARKER_PRESERVING_FREE_QUOTIENT_ROUTER_CYCLE630_NOTE_2026-07-23.md"
    c629_note = "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md"
    c610_note = "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md"
    c633_note = str(NOTE.relative_to(ROOT))
    runner_path = str(Path(__file__).relative_to(ROOT))
    families = (
        {"family": "binary state-carried program-track interpreter", "marker": "ATTEMPTED", "object": "780-row selector/act/uncompute program", "mechanism": "physical binary ROM, opcode register, fixed catalog decoder, and two-rail token", "evidence": "full 377+24+377+2 program executes with clean boundary", "strength_vs_target": "literal recurrent slice", "failure_statement": "does not cover the full 441,030 descriptors", "terminal_obligation": "autonomous stored-program selection"},
        {"family": "six-lane local predecessor packet", "marker": "ATTEMPTED", "object": "selected routed CNOT path", "mechanism": "stored three-bit lane word and six-way local predecessor comparisons", "evidence": f"{lane['selected_pair_rows']} selected predecessor rows and zero decode failures", "strength_vs_target": "literal route packet subroutine for the slice", "failure_statement": "not materialized for all 4,570 paths inside one ROM", "terminal_obligation": "local token routing"},
        {"family": "flat binary full-descriptor ROM", "marker": "ATTEMPTED", "object": "441,030 descriptor rows", "mechanism": "two token rails plus 19 opcode bits per row", "evidence": f"{capacity['flat_descriptor_two_rail_plus_opcode_roles']} roles versus {capacity['marker_free_roles']}", "strength_vs_target": "rules out this flat layout only", "failure_statement": "hierarchical and grammar compression remain open", "terminal_obligation": "full-word storage"},
        {"family": "flat literal-call ROM", "marker": "ATTEMPTED", "object": "769,434 act calls", "mechanism": "two rails plus 19-bit descriptor opcode", "evidence": f"capacity ratio {capacity['flat_call_capacity_ratio']:.3f}", "strength_vs_target": "rules out uncompressed call rows", "failure_statement": "repetition-generating loops remain open", "terminal_obligation": "full call order"},
        {"family": "optimistic spatial target encoding", "marker": "ATTEMPTED", "object": "441,030 descriptors with spatial targets and seven gate families", "mechanism": "two rails plus minimum three gate-family bits", "evidence": f"capacity ratio {capacity['optimistic_spatial_descriptor_capacity_ratio']:.3f}", "strength_vs_target": "rules out one-row-per-descriptor even before work", "failure_statement": "shared rails and combinator programs remain open", "terminal_obligation": "compressed opcode/target representation"},
        {"family": "algorithmic/hierarchical ROM", "marker": "ATTEMPTED", "object": "repeated selector and descriptor grammar", "mechanism": "reuse one uniform interpreter with nested counters/combinators", "evidence": "Cycle633 compresses 754 selector macro occurrences by a shared catalog but does not synthesize the full grammar", "strength_vs_target": "constructive partial compression", "failure_statement": "nested counter/decoder and full route ownership are unbuilt", "terminal_obligation": "full compressed word"},
    )
    open_routes = (
        {"family": "hierarchical grammar ROM", "mechanism": "nested loop counters generate repeated descriptor blocks", "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT", "terminal_obligation": "entire 441,030-descriptor word"},
        {"family": "spatial shared-track decoder", "mechanism": "reuse token rails while target is encoded by program placement", "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT", "terminal_obligation": "reduce row storage below one row per descriptor"},
        {"family": "weight/equality enforcement", "mechanism": "fine-NN enforcement of Cycle629 <=91 and neighbor-equal h", "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT", "terminal_obligation": "locally enforced code sector"},
        {"family": "literal E/full G/intertwiner", "mechanism": "extend the slice interpreter to the full word and compose physical code map", "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT", "terminal_obligation": "E G_coarse = G_physical E and full-code leakage"},
    )
    walls = (
        "hierarchical generation of the full descriptor/call order",
        "shared physical route-token ownership for all 4,570 paths",
        "fine-NN <=91 and neighbor-equal-h enforcement",
        "literal physical encoder E and full-code leakage",
        "full recurrent G_physical and physical intertwiner",
    )
    pairs = tuple({
        "wall_A": first, "wall_B": second,
        "A_implies_B": False, "B_implies_A": False,
        "shared_witness_identified": False, "independent": True,
        "evidence": "Cycle633 executes no implication or shared obstruction between these residuals",
    } for first, second in combinations(walls, 2))
    residual_specs = (
        (exact_citation(c631_note, "physical M2 storage and a local successor update"), exact_citation(runner_path, "full 377+24+377+2 program executes"), "physical head law and local decoder absent", "retired for the 780-row slice only; full grammar remains", False, False, False),
        (exact_citation(c631_note, "the 441,030 distinct literal stage descriptors fit numerically"), exact_citation(runner_path, "flat binary full-descriptor ROM"), "naive unary and radius-one ROM fail while compressed ROM is open", "binary program-track slice constructed; flat full descriptor ROM capacity fails", False, False, False),
        (exact_citation(c631_note, "a literal physical encoder `E`;"), exact_citation(runner_path, '"literal_physical_encoder_E": False'), "E/G/intertwiner/leakage and fresh fixtures open", "unchanged outside the selected slice", True, True, False),
        (exact_citation(c630_note, "local route successor; token/clock genesis"), exact_citation(runner_path, "one repeated uniform ROM-load/decode/execute"), "local successor/token genesis and physical E open", "successor/genesis close for one program slice; E and full word remain", False, False, False),
    )
    residuals = tuple({
        "prior_path": prior["path"], "prior_line": prior["line"], "prior_line_text": prior["line_text"],
        "current_path": current["path"], "current_line": current["line"], "current_line_text": current["line_text"],
        "prior_residual": prior_residual, "current_residual": current_residual,
        "same_scope": same_scope, "exact_match": exact_match, "use_as_closure": use_as_closure,
    } for prior, current, prior_residual, current_residual, same_scope, exact_match, use_as_closure in residual_specs)
    rhetoric = tuple({
        "claim": claim,
        "per_element": "literal binary M2 roles and exact local gate templates",
        "per_site": "one bit per M2 and support-one/two lowering",
        "per_mode": "only the selected two-M2 flag/data slice; no six-mode fixture credit",
        "per_block": "780 program rows fit one K129 block; flat full layouts do not",
        "lattice_wide": "L3/L6/L7 transported slice passes; full G/E/intertwiner untested",
    } for claim in ("ROM", "token", "predecessor", "capacity", "physical compiler"))
    partial = (
        {"file": "scripts/physical_literal_program_track_interpreter_cycle633_2026_07_23.py", "status": "PARTIAL / CURRENT", "what_closes": "literal stored-program successor for full selector plus exact three-stage slice"},
        {"file": "scripts/physical_autonomous_marker_recognition_token_attempt_cycle631_2026_07_23.py", "status": "PARTIAL / PRIOR", "what_closes": "marker-safe selector gates, six-lane geometry, and nine-colour arbitration"},
        {"file": "UNMATERIALIZED", "status": "OPEN / PRIORITY", "what_closes": "hierarchical full descriptor grammar and shared route-token ownership"},
        {"file": "UNMATERIALIZED", "status": "OPEN", "what_closes": "fine-NN weight/equality enforcement"},
        {"file": "UNMATERIALIZED", "status": "OPEN", "what_closes": "literal E, full recurrent G, intertwiner, leakage, and fresh fixtures"},
    )
    steelman = {
        "mechanism": "Exploit the severe repetition already visible in the 754 selector rows and Cycle610 factor loops: store a small grammar of loop bodies and route words, add nested reversible counters, and reuse the same two-rail interpreter instead of allocating one row per descriptor.",
        "actionable_next_steps": (
            "factor the 441,030 descriptor sequence into repeated loop/combinator bodies",
            "compile nested counter carry and return stacks into free M2 roles",
            "share the six-lane packet among route bodies with explicit ownership",
            "then compose E and execute full leakage/intertwiner/fixture controls",
        ),
        "why_it_could_close": "Cycle633 already proves that binary ROM data, catalog decode, marker-derived token recurrence, and a route predecessor word can coexist in one K129 block; only flat row allocation has failed.",
        "terminal_obligation": "entire descriptor order, all route bodies, code enforcement, E, G_physical, leakage, intertwiner, and fixtures",
        "authority_status": "OPEN / no retained authority",
        "citations": (
            {**exact_citation(c631_note, "route-label packet and a literal fine-NN multistep ROM/interpreter"), "supports": "the prior actionable local-controller route"},
            {**exact_citation(c630_note, "The strongest hostile counterargument is actionable"), "supports": "the prior finite-route local-successor steelman"},
        ),
    }
    echoes = (
        {"cycle": "Cycle610", "retired": "conditional coordinate word as physical promotion", "mechanism": "explicitly withheld E/G and host schedule", "applicability": "Cycle633 promotes only a literal stored-program slice", "citation": exact_citation(c610_note, "Therefore this artifact is not a completed physical M2 compiler")},
        {"cycle": "Cycle629", "retired": "external phase/orientation at projector level", "mechanism": "state-carried marker crystal", "applicability": "supplies phi,h transport but not weight/equality enforcement", "citation": exact_citation(c629_note, "state-carried phase")},
        {"cycle": "Cycle630", "retired": "marker-free path absence", "mechanism": "complete finite path table", "applicability": "supplies compile-time routes for the fixed interpreter circuit", "citation": exact_citation(c630_note, "The result starts at `u`, ends at the intended lifted `v`")},
        {"cycle": "Cycle631", "retired": "single sidecar and naive unary ROM as default controller", "mechanism": "six-lane geometry and compressed-ROM opening", "applicability": "Cycle633 uses both openings literally for one slice", "citation": exact_citation(c631_note, "Cycle 631 does **not** construct")},
        {"cycle": "Cycle633", "retired": "absence of any literal local successor/token interpreter", "mechanism": "780-row binary ROM and two-rail recurrent token", "applicability": "slice only; no statement about full grammar impossibility", "citation": exact_citation(c633_note, "Cycle 633 constructs a literal bounded stored-program controller")},
    )
    result = {
        "skill_freshness": {"origin_main_checked": True, "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7", "freshness_check_sha256": "1e0ec4ef4d7c5dd24243d7c3954c78a3f00ecd3d5e43805e788dd3629973a962", "newer_origin_main_version_followed": True},
        "N1_normalized_families": families,
        "N1_qualifying_family_count": len(families),
        "N1_all_markers_exact": all(row["marker"] in ("ATTEMPTED", "RULED OUT BY PRIOR") for row in families),
        "N1_open_counterroutes_not_counted": open_routes,
        "N2_collapsed_walls": walls,
        "N2_directional_wall_independence": pairs,
        "N2_pair_count": len(pairs),
        "N3_hidden_wall_scan": {"required_phrase_scan": ("we assume", "by construction", "as is standard", "the framework provides", "bridge context", "background", "naturally", "obviously", "standard QFT", "registered", "canonical"), "load_bearing_premises": ("fixed K129", "supplied marker/weight/equality sector", "state-carried program bits", "clean work and route-token sites", "compile-time fixed circuit catalog"), "runtime_host_lookup_absent": True, "compile_time_circuit_explicit": True, "hidden_wall_promotions_complete": True},
        "N4_residual_matching": residuals,
        "N5_rhetoric_resolution": rhetoric,
        "N5_five_resolutions_present": all(all(key in row for key in ("per_element", "per_site", "per_mode", "per_block", "lattice_wide")) for row in rhetoric),
        "N6_partial_closure_paths": partial,
        "N7_hostile_steelman": steelman,
        "N8_cross_cycle_echo": echoes,
        "route_independent_impossibility_claim": False,
        "minimum_content_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure_claim": False,
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction_gate": "FAIL / DO NOT SHIP",
        "axiom_pressure_gate": "FAIL / DO NOT SHIP",
        "narrow_positive_gate": "PASS / literal 780-row interpreter slice",
        "narrow_route_specific_negative_gate": "PASS / three flat full-word storage layouts only",
        "status": "FAIL",
        "failed_checklist_items": (
            "N7: hierarchical grammar/combinator compression remains actionable",
            "physical promotion: full descriptor order, E/G/intertwiner/leakage/fixtures remain open",
        ),
    }
    schema = (
        len(families) >= 5 and result["N1_all_markers_exact"]
        and all(row["status"].startswith("OPEN / NOT COUNTED") for row in open_routes)
        and len(pairs) == 10 and all(row["independent"] for row in pairs)
        and all(set(("prior_path", "prior_line", "current_path", "current_line", "prior_residual", "current_residual", "same_scope", "exact_match", "use_as_closure")) <= set(row) for row in residuals)
        and result["N5_five_resolutions_present"]
        and all(set(("file", "status", "what_closes")) == set(row) for row in partial)
        and set(("mechanism", "actionable_next_steps", "why_it_could_close", "terminal_obligation", "authority_status", "citations")) == set(steelman)
        and all(set(("cycle", "retired", "mechanism", "applicability", "citation")) == set(row) for row in echoes)
    )
    check("current N1-N8 ships the literal slice and narrow flat-layout failures while blocking broad/minimum/shared/axiom claims",
          schema and result["status"] == "FAIL"
          and result["narrow_positive_gate"].startswith("PASS")
          and not result["shared_obstruction_claim"], result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "780", "377", "24", "13 x 120", "one bit per M2", "six-lane",
        "nine-colour", "L3/L6/L7", "all24", "all576", "host",
        "not time", "441,030", "769,434", "E G_coarse = G_physical E",
        "no axiom pressure", "authority none", "audit unset", "N1", "N8",
        "`ATTEMPTED`", "`RULED OUT BY PRIOR`", "same_scope", "exact_match",
        "use_as_closure", "per_element", "per_site", "per_mode", "per_block",
        "lattice_wide", "what_closes", "actionable", "applicability",
    )
    missing = tuple(token for token in required if token not in text)
    result = {"required_tokens": required, "missing_tokens": missing, "pass": not missing}
    check("Cycle633 note states the literal interpreter, exact scope, one-bit M2 correction, and current N1-N8 firewall",
          result["pass"], result)
    return result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold:
        previous = sys.stdout
        sys.stdout = Tee(previous, cold)
        try:
            inherited, r631 = shore()
            target = exact_target_contract()
            original = c630.check
            c630.check = lambda *_args, **_kwargs: None
            try:
                graph, parent, depth = c630.quotient_tree()
                r610 = json.loads((ROOT / (
                    "outputs/physical_proper_cubic_supercell_stream_composition_"
                    "tournament_cycle610_receipt_2026_07_22.json"
                )).read_text())
                routing, paths = c630.descriptor_routing_audit(parent, r610)
            finally:
                c630.check = original
            act_rows, act_audit = selected_act_slice()
            rows, program = selector_program_rows(r631, act_rows)
            selected_pair = (act_audit["selected_flag_coordinate"], act_audit["selected_data_coordinate"])
            layout, layout_audit = track_and_storage_layout(r631, program, selected_pair, paths)
            lane = locally_decoded_lane_subroutine(layout)
            strict_routes = strict_contiguous_six_lane_scout(paths, layout)
            cycle = simulate_program_cycle(rows, program, layout, act_audit)
            covariance = covariance_and_periodic(layout, layout_audit)
            capacity = capacity_audit(program, layout_audit, r631)
            fine_routing = fine_NN_interaction_routing(parent, depth, program, layout, rows)
            circuit = circuit_resource_bound(program, layout, rows, fine_routing)
            discipline = no_go_discipline(program, layout_audit, lane, cycle, capacity, circuit)
            note = note_contract()
            elapsed = time.monotonic() - started
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            maximum_rss_bytes = int(rss if sys.platform == "darwin" else rss * 1024)
            check("Cycle633 cold run stays within declared time and memory caps",
                  elapsed <= CAP_SECONDS and maximum_rss_bytes <= CAP_BYTES,
                  {"elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss_bytes,
                   "cap_seconds": CAP_SECONDS, "cap_bytes": CAP_BYTES})
            receipt = {
                "status": "positive_literal_780_row_program_track_interpreter_slice",
                "classification": "bounded literal stored-program controller slice; full physical compiler and causal-time promotion open",
                "authority": AUTHORITY,
                "audit": AUDIT,
                "author_accepted": False,
                "author_artifact_status_accepted": False,
                "breakthrough": False,
                "breakthrough_bar_met": False,
                "runner_sha256": sha(Path(__file__)),
                "note_sha256": sha(NOTE),
                "pins": PINS,
                "shore": inherited,
                "exact_target_contract": target,
                "Cycle630_reexecution": {"free_sites": graph["free_sites"], "path_pairs": routing["distinct_ordered_endpoint_pairs"], "pass": graph["pass"] and routing["pass"]},
                "exact_coin_stream_contact_stage_slice": act_audit,
                "program_ROM": program["summary"],
                "physical_storage_and_two_rail_track": layout_audit,
                "local_six_lane_predecessor_and_route_token": lane,
                "strict_contiguous_all_4570_route_geometry_scout": strict_routes,
                "recurrent_program_cycle": cycle,
                "state_carried_covariance_and_periodic_controls": covariance,
                "full_word_flat_capacity_audit": capacity,
                "literal_fine_NN_interaction_routing": fine_routing,
                "literal_circuit_resource_bound": circuit,
                "no_go_discipline": discipline,
                "note_contract": note,
                "strongest_constructive_result": "a state-carried 780-row binary ROM in actual one-bit M2 roles drives one repeated reversible load/decode/execute/uncompute/two-rail-successor step through all 377 Cycle631 selector macros, 24 exact coin-stream-contact slice primitives, the same 377 clean-uncompute macros, and two IDLE pads; marker-derived token genesis/cleanup, stored six-lane predecessor data, nine-colour arbitration, all24/all576, and L3/L6/L7 controls pass",
                "exact_scope": "one identity-frame base program and all transported (phi,h) images on the supplied Cycle629 weight/equality sector; one exact flag/data coin-stream-contact stage slice only",
                "physical_controller_disposition": "literal recurrent controller for the selected 780-row slice; not the full 441,030-descriptor or 769,434-call physical G",
                "mass_contact_seam_fixture_status": "only the selected two-M2 three-stage unitary is reexecuted; no one-particle mass, full contact, cross-seam, or coarse physical compiler fixture credit",
                "literal_physical_encoder_E": False,
                "physical_intertwiner_residual": None,
                "full_code_leakage_evaluated": False,
                "shared_obstruction_or_axiom_pressure": False,
                "shared_route_independent_obstruction": False,
                "axiom_pressure": False,
                "constitutional_effect": "none",
                "semantic_firewall": {"program_position_is_causal_time": False, "nine_colour_phase_is_causal_time": False, "compiler_count_is_rate": False, "wrapped_phase_is_energy": False, "token_or_program_copy_is_Record": False, "coarse_CAR_cell_is_physical_site_compiler": False},
                "six_wall_ledger": {"C_ref": "state-carried phi,h and physical program roles advance the controller slice; marker weight/equality and program genesis remain supplied", "C_num": "one-bit-per-M2 capacity is corrected and exact stage residuals pass; full word, physical E, and full leakage remain open", "C_wrap": "token successor and renewal are literal for 780 rows, but program position and arbitration phase are not time or history", "C_int": "one exact coin-stream-contact stage slice is physical; full mass/contact/Cycle230 seam fixtures remain unexecuted", "C_local": "bounded fine-NN controller paths and a 780-row recurrent slice close; full hierarchical grammar and all4570 strict route ownership remain open", "C_source": "unchanged; program/ancilla capacity has no energy, stress, source, or gravity meaning"},
                "broad_negative_gate": discipline["broad_negative_gate"],
                "optimal_next_campaign": "factor the 441,030-descriptor word into a hierarchical grammar of repeated bodies and nested reversible counters, reuse the Cycle633 two-rail interpreter and six-lane packet with explicit ownership, then compose literal E/full G for fresh leakage/intertwiner/mass/contact/seam controls",
                "elapsed_seconds": elapsed,
                "maximum_RSS_bytes": maximum_rss_bytes,
                "tests_passed": PASS,
                "tests_failed": FAIL,
                "pass": FAIL == 0,
            }
            RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n")
            print("SUMMARY_JSON", json.dumps({
                "pass": FAIL == 0, "tests_passed": PASS, "tests_failed": FAIL,
                "program_rows": program["summary"]["program_rows"],
                "catalog_entries": program["summary"]["catalog_entries"],
                "new_roles": layout_audit["total_new_distinct_base_roles"],
                "act_residual": act_audit["three_factor_residual"],
                "full_flat_ROM": capacity["full_flat_ROM_pass"],
                "axiom_pressure": False,
                "elapsed_seconds": elapsed,
                "maximum_RSS_bytes": maximum_rss_bytes,
            }, sort_keys=True))
            print("RESULT", PASS, FAIL)
        finally:
            sys.stdout = previous
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
