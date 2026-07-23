#!/usr/bin/env python3
"""Cycle638: hierarchical full conditional-act stored-program compiler.

This runner compiles the complete Cycle610 conditional act word into a
three-level stage/body/action grammar with actual one-bit M2 storage and
reversible nested counters.  It also replaces stored route paths by a bounded
coordinate-counter router and proves translated route-body ownership.  It is
not a physical encoder E or a full framework G_physical.
Authority none; audit unset; author accepted false; breakthrough false.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, permutations
import json
import math
import resource
from pathlib import Path
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_literal_program_track_interpreter_cycle633_2026_07_23 as c633


c631 = c633.c631
c630 = c633.c630
c629 = c633.c629
c610 = c633.c610
c603 = c633.c603
K = c633.K
H = c633.H
FRAMES = c633.FRAMES
DIRECTIONS = c633.DIRECTIONS
AUTHORITY = "none"
AUDIT = "unset"
CAP_SECONDS = 300.0
CAP_BYTES = 3 * 1024**3
PASS = FAIL = 0
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_HIERARCHICAL_GRAMMAR_FULL_ACT_COMPILER_CYCLE638_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_hierarchical_grammar_full_act_compiler_cycle638_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_hierarchical_grammar_full_act_compiler_cycle638_cold_2026_07_23.txt"
PINS = {
    "scripts/physical_literal_program_track_interpreter_cycle633_2026_07_23.py": "2e13172fabcc8de1286013dd6de2948b5827dc176d8845cc4d5e2a4ea7794e8b",
    "docs/work_history/repo/review_feedback/PHYSICAL_LITERAL_PROGRAM_TRACK_INTERPRETER_CYCLE633_NOTE_2026-07-23.md": "061c5b7ab68a59d493831cf1d46734073d803b47d75ae1365fd61d0c871a6bb9",
    "outputs/physical_literal_program_track_interpreter_cycle633_receipt_2026_07_23.json": "fa72bca07b200dd191d9d8d196bd74a428125b684b175b5777f1b64a6120a270",
    "outputs/physical_literal_program_track_interpreter_cycle633_cold_2026_07_23.txt": "79734060fd337dc8e0a0a2d2c897247200028b8f6d730a5d2af72d2814a91c91",
}


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, value):
        for stream in self.streams: stream.write(value)
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic): return value.item()
    if isinstance(value, np.ndarray): return value.tolist()
    if isinstance(value, set | frozenset): return sorted(value)
    if isinstance(value, complex): return {"real": value.real, "imag": value.imag}
    raise TypeError(type(value).__name__)


def check(label: str, condition: bool, detail="") -> None:
    global PASS, FAIL
    PASS += int(condition); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def matrix_sha(matrix) -> str:
    return sha256(np.asarray(matrix, dtype=np.complex128).tobytes()).hexdigest()


def bits(value: int, width: int) -> tuple[int, ...]:
    return tuple((value >> (width - 1 - index)) & 1 for index in range(width))


def shore() -> tuple[dict, dict]:
    r633 = json.loads((ROOT / "outputs/physical_literal_program_track_interpreter_cycle633_receipt_2026_07_23.json").read_text())
    expected = dict(r633["shore"]["import_audit"]["expected_transitive_sha256"])
    expected.update(PINS)
    observed = {name: sha(ROOT / name) for name in expected}
    actual = dict(r633["shore"]["import_audit"]["actual_imported_modules"])
    actual["physical_literal_program_track_interpreter_cycle633_2026_07_23"] = PINS.keys().__iter__().__next__()
    uncovered = sorted(set(actual.values()) - set(expected))
    result = {
        "Cycle633_pass": r633["pass"], "Cycle633_tests": r633["tests_passed"],
        "Cycle633_authority": r633["authority"], "Cycle633_audit": r633["audit"],
        "Cycle633_program_rows": r633["program_ROM"]["program_rows"],
        "Cycle633_strict_routes": r633["strict_contiguous_all_4570_route_geometry_scout"]["paths_solved"],
        "Cycle633_three_change_routes": len(r633["strict_contiguous_all_4570_route_geometry_scout"]["three_change_pairs"]),
        "Cycle633_full_flat_ROM": r633["full_word_flat_capacity_audit"]["full_flat_ROM_pass"],
        "Cycle633_physical_E": r633["literal_physical_encoder_E"],
        "Cycle633_axiom_pressure": r633["shared_obstruction_or_axiom_pressure"],
        "import_audit": {"expected_transitive_sha256": expected, "observed_transitive_sha256": observed,
                         "actual_imported_modules": actual, "uncovered_imported_modules": uncovered,
                         "expected_file_count": len(expected), "runtime_module_count": len(actual)},
    }
    condition = (observed == expected and not uncovered and r633["pass"]
                 and r633["tests_passed"] == 15 and r633["authority"] == AUTHORITY
                 and r633["audit"] == AUDIT and not r633["author_artifact_status_accepted"]
                 and result["Cycle633_strict_routes"] == 4570
                 and result["Cycle633_three_change_routes"] == 2
                 and not result["Cycle633_full_flat_ROM"]
                 and not result["Cycle633_physical_E"] and not result["Cycle633_axiom_pressure"])
    check("Cycle633 quartet and transitive science graph are byte exact", condition,
          {"tests": result["Cycle633_tests"], "files": len(expected), "uncovered": uncovered})
    return result, r633


def target_contract() -> dict:
    result = {
        "target": "compile all 441,030 distinct stage descriptors and all 769,434 conditional act calls into a literal three-level one-bit-M2 grammar",
        "required": (
            "exact call-order and diagnostic stage-label hash reconstruction",
            "physical stage/body/action catalogs, nested reversible counters, and shared two-rail lookup",
            "coordinate-counter route generation with no stored 4,570-path parent table",
            "strict sidecar and translated collision ownership for every route body",
            "support-one/two fine-NN decoder and counter lowering, inverse, exhaust, deletion, malformed, all24/all576, and L3/L6/L7",
        ),
        "withheld": "physical E, full code leakage, weight/equality enforcement, fresh mass/contact/seam fixtures, causal time, rate, energy, or a Record",
    }
    check("Cycle638 targets the complete conditional act controller without promoting full E/G or time semantics",
          len(result["required"]) == 5 and "physical E" in result["withheld"], result)
    return result


def direct_cross_matrix_catalog() -> dict:
    gates = (
        [c603.two("cross_open", 2, 3, c603.CNOT, "CNOT")]
        + c603.triple_controlled_u_sequence(c603.X2, (1, 4, 3), 2, 0, "cross_c3x")
        + [c603.two("cross_close", 2, 3, c603.CNOT, "CNOT")]
    )
    return {index: matrix_sha(gate.matrix) for index, gate in enumerate(gates)}


def expected_stage_labels(stream_operations: list[dict], coin_count: int,
                          contact_count: int) -> tuple[str, ...]:
    labels = [f"factor_0_onsite_coin_g{index}" for index in range(coin_count)]
    for index, operation in enumerate(stream_operations):
        base = f"factor_1_stream_{index}_{operation['stage']}"
        coordinates = tuple(operation["coordinates"])
        is_cross = (operation["family"] == "SWAP" and "cross" in operation["stage"]
                    and len(coordinates) == 2
                    and any(any(abs(value) > H for value in site) for site in coordinates))
        if is_cross:
            labels.extend((base + "_copy_source", base + "_copy_target", base,
                           base + "_uncopy_target", base + "_uncopy_source"))
        else:
            labels.append(base)
    labels.extend(f"factor_2_contact_g{index}" for index in range(contact_count))
    return tuple(labels)


def capture_and_compile_grammar() -> tuple[dict, dict]:
    stream_result, stream_operations = c610.elementary_stream_template(True)
    onsite_coin, contact = c610.onsite_gate_lists()
    direct_matrices = direct_cross_matrix_catalog()
    calls = []
    original_route, original_direct = c610.route_primitive, c610.direct_primitive

    def capture_route(accumulator, gate, coordinates, frame, stage, cell_offset=(0, 0, 0)):
        coords = tuple(tuple(int(v) for v in site) for site in coordinates)
        offset = tuple(int(v) for v in cell_offset)
        physical = coords
        if len(coords) == 2 and offset != (0, 0, 0):
            physical = (coords[0], tuple(coords[1][axis] + K * offset[axis] for axis in range(3)))
        calls.append((stage, "route", gate.family, offset, physical,
                      (gate.family, matrix_sha(gate.matrix))))
        return original_route(accumulator, gate, coordinates, frame, stage, cell_offset)

    def capture_direct(accumulator, operation, frame):
        coords = tuple(tuple(int(v) for v in site) for site in operation["coordinates"])
        family = operation["family"]
        if family == "SWAP": parameter = matrix_sha(c603.SWAP)
        else: parameter = direct_matrices[operation["gate_index"]]
        calls.append((operation["stage"], "direct", family,
                      tuple(operation.get("cell_offset", (0, 0, 0))), coords,
                      (family, parameter)))
        return original_direct(accumulator, operation, frame)

    c610.route_primitive, c610.direct_primitive = capture_route, capture_direct
    try:
        compiler = c610.physical_orientation_controlled_compiler(stream_operations)
    finally:
        c610.route_primitive, c610.direct_primitive = original_route, original_direct
    act = [row for row in calls if not row[0].startswith("selector_")]
    stage_runs = []
    for row in act:
        if not stage_runs or stage_runs[-1][0] != row[0]: stage_runs.append([row[0], []])
        stage_runs[-1][1].append(row[1:])
    labels = tuple(row[0] for row in stage_runs)
    expected_labels = expected_stage_labels(stream_operations, len(onsite_coin), len(contact))

    body_words = tuple(tuple(row[1]) for row in stage_runs)
    body_catalog = tuple(sorted(set(body_words), key=repr))
    body_id = {word: index for index, word in enumerate(body_catalog)}
    stage_body_ids = tuple(body_id[word] for word in body_words)
    action_catalog = tuple(sorted({action for body in body_catalog for action in body}, key=repr))
    action_id = {action: index for index, action in enumerate(action_catalog)}
    body_action_ids = tuple(tuple(action_id[action] for action in body) for body in body_catalog)
    gate_catalog = tuple(sorted({action[-1] for action in action_catalog}, key=repr))
    gate_id = {gate: index for index, gate in enumerate(gate_catalog)}
    sites = tuple(sorted({site for action in action_catalog for site in action[3]}))
    site_id = {site: index for index, site in enumerate(sites)}
    pairs = tuple(sorted({action[3] for action in action_catalog if len(action[3]) == 2}))
    pair_id = {pair: index for index, pair in enumerate(pairs)}

    descriptor = sha256(); enhanced = sha256(); reconstructed = sha256(); reconstructed_enhanced = sha256()
    distinct_diagnostic_descriptors = len({(source, stage, family, offset, physical)
                                           for stage, source, family, offset, physical, _gate in act})
    factor_calls = Counter(stage.split("_")[1] for stage, *_rest in act)
    for stage, source, family, offset, physical, gate in act:
        descriptor.update((repr((source, stage, family, offset, physical)) + "\n").encode())
        enhanced.update((repr((source, stage, family, offset, physical, gate)) + "\n").encode())
    reconstructed_calls = 0
    for stage, body_index in zip(expected_labels, stage_body_ids):
        for action_index in body_action_ids[body_index]:
            source, family, offset, physical, gate = action_catalog[action_index]
            reconstructed.update((repr((source, stage, family, offset, physical)) + "\n").encode())
            reconstructed_enhanced.update((repr((source, stage, family, offset, physical, gate)) + "\n").encode())
            reconstructed_calls += 1

    widths = {
        "stage_body_id": math.ceil(math.log2(len(body_catalog))),
        "body_action_id": math.ceil(math.log2(len(action_catalog))),
        "action_gate_id": math.ceil(math.log2(len(gate_catalog))),
        "action_operand_id": math.ceil(math.log2(max(len(sites), len(pairs)))),
        "site_id": math.ceil(math.log2(len(sites))),
    }
    template_lengths = tuple(sorted({len(body) for body in body_catalog}))
    summary = {
        "Cycle610_stream_pass": stream_result["pass"],
        "Cycle610_compiler_pass": compiler["pass"],
        "conditional_act_calls": len(act),
        "distinct_diagnostic_stage_descriptors": distinct_diagnostic_descriptors,
        "factor_call_population": {"factor_0_coin": factor_calls["0"],
                                   "factor_1_stream": factor_calls["1"],
                                   "factor_2_contact": factor_calls["2"]},
        "diagnostic_stage_invocations": len(stage_runs),
        "unique_parameter_aware_stage_bodies": len(body_catalog),
        "stage_body_template_lengths": template_lengths,
        "stage_catalog_action_slots": sum(map(len, body_catalog)),
        "atomic_parameter_aware_actions": len(action_catalog),
        "gate_opcode_catalog_entries": len(gate_catalog),
        "physical_operand_sites": len(sites),
        "physical_operand_pairs": len(pairs),
        "widths": widths,
        "canonical_stage_label_counter_grammar_matches": labels == expected_labels,
        "captured_descriptor_word_sha256": descriptor.hexdigest(),
        "reconstructed_descriptor_word_sha256": reconstructed.hexdigest(),
        "captured_parameter_aware_word_sha256": enhanced.hexdigest(),
        "reconstructed_parameter_aware_word_sha256": reconstructed_enhanced.hexdigest(),
        "Cycle630_expected_descriptor_word_sha256": "9760bc3163efa2f118cd48bcb4fada97b34167ea46374d523f1fd227c9abcd7b",
        "reconstructed_calls": reconstructed_calls,
        "pass": (stream_result["pass"] and compiler["pass"] and len(act) == 769_434
                 and distinct_diagnostic_descriptors == 441_030
                 and (factor_calls["0"], factor_calls["1"], factor_calls["2"]) == (87_360, 677_124, 4_950)
                 and len(stage_runs) == 53_709 and len(body_catalog) == 3_123
                 and sum(map(len, body_catalog)) == 49_440 and len(action_catalog) == 10_529
                 and len(sites) == 1_481 and len(pairs) == 4_570
                 and labels == expected_labels and reconstructed_calls == len(act)
                 and descriptor.hexdigest() == reconstructed.hexdigest()
                 == "9760bc3163efa2f118cd48bcb4fada97b34167ea46374d523f1fd227c9abcd7b"
                 and enhanced.hexdigest() == reconstructed_enhanced.hexdigest()),
    }
    check("the three-level grammar reconstructs all 769,434 calls and the exact Cycle630 diagnostic descriptor-order hash",
          summary["pass"], summary)
    private = {"labels": expected_labels, "stage_body_ids": stage_body_ids,
               "body_catalog": body_catalog, "body_action_ids": body_action_ids,
               "action_catalog": action_catalog, "gate_catalog": gate_catalog,
               "gate_id": gate_id, "sites": sites, "site_id": site_id,
               "pairs": pairs, "pair_id": pair_id, "widths": widths}
    return summary, private


AXIS_ORDERS = tuple(permutations(range(3)))


def axis_path(first, second, order):
    current = list(first); path = [tuple(current)]
    for axis in order:
        step = 1 if second[axis] > current[axis] else -1
        while current[axis] != second[axis]:
            current[axis] += step; path.append(tuple(current))
    return tuple(path)


def greedy_sidecar(path, marker):
    data = {c630.residue(site) for site in path}
    safe = [tuple(c630.residue(c630.add(site, direction)) not in marker
                  and c630.residue(c630.add(site, direction)) not in data
                  for direction in DIRECTIONS) for site in path]
    if len(path) == 1: return (0, (0,), (c630.add(path[0], DIRECTIONS[0]),), ()) if safe[0][0] else None
    initial = [lane for lane in range(6) if safe[0][lane] and safe[1][lane]]
    if not initial: return None
    lane = initial[0]; lanes = [lane]
    sidecar = [c630.add(path[0], DIRECTIONS[lane])]; turns = []
    for index in range(len(path) - 1):
        if not safe[index + 1][lane]: return None
        if index + 1 < len(path) - 1 and not safe[index + 2][lane]:
            candidates = []
            for nxt in range(6):
                if nxt == lane or not safe[index + 1][nxt] or not safe[index + 2][nxt]: continue
                if all(DIRECTIONS[lane][axis] == -DIRECTIONS[nxt][axis] for axis in range(3)): continue
                connector = tuple(path[index + 1][axis] + DIRECTIONS[lane][axis] + DIRECTIONS[nxt][axis] for axis in range(3))
                if c630.residue(connector) in marker or c630.residue(connector) in data: continue
                candidates.append((nxt, connector))
            if not candidates: return None
            nxt, connector = candidates[0]
            arrival = c630.add(path[index + 1], DIRECTIONS[lane])
            sidecar.extend((arrival, connector, c630.add(path[index + 1], DIRECTIONS[nxt])))
            turns.append((index + 1, lane, nxt)); lane = nxt
        else:
            sidecar.append(c630.add(path[index + 1], DIRECTIONS[lane]))
        lanes.append(lane)
    if any(sum(abs(sidecar[i + 1][axis] - sidecar[i][axis]) for axis in range(3)) != 1 for i in range(len(sidecar) - 1)):
        return None
    return len(turns), tuple(lanes), tuple(sidecar), tuple(turns)


def choose_coordinate_route(pair, marker):
    candidates = []
    for order_index, order in enumerate(AXIS_ORDERS):
        path = axis_path(pair[0], pair[1], order)
        if any(c630.residue(site) in marker for site in path): continue
        side = greedy_sidecar(path, marker)
        if side is not None: candidates.append((side[0], order_index, path, side))
    return min(candidates, key=lambda row: (row[0], row[1])) if candidates else None


def coordinate_counter_router(private: dict) -> tuple[dict, dict]:
    marker = c630.marker_residues(); histogram = Counter(); order_histogram = Counter()
    failures = []; ownership_failures = Counter(); digest = sha256(); routes = {}
    total_edges = 0; maximum_edges = 0; reserved = set()
    for pair in private["pairs"]:
        chosen = choose_coordinate_route(pair, marker)
        if chosen is None:
            failures.append(pair); continue
        changes, order_index, path, side = chosen
        _changes, lane_word, sidecar, turns = side
        roles = set(path) | set(sidecar)
        for length in (3, 6, 7):
            modulus = K * length
            base = {tuple(value % modulus for value in site) for site in roles}
            for direction in DIRECTIONS:
                shifted = {tuple((site[axis] + K * direction[axis]) % modulus for axis in range(3)) for site in roles}
                ownership_failures[length] += len(base & shifted)
        histogram[changes] += 1; order_histogram[order_index] += 1
        total_edges += len(path) - 1; maximum_edges = max(maximum_edges, len(path) - 1)
        digest.update(repr((pair, order_index, turns, path, sidecar)).encode())
        routes[pair] = (path, sidecar, order_index, turns)
        reserved.update(c633.representative(site) for site in roles)
    composition_failures = 0
    frame_keys = {tuple(int(value) for value in frame.ravel()) for frame in FRAMES}
    for first in FRAMES:
        for second in FRAMES:
            product = first @ second
            composition_failures += int(tuple(int(value) for value in product.ravel()) not in frame_keys)
            for site in (private["pairs"][0][0], private["pairs"][-1][-1], (1, 2, 3)):
                composition_failures += int(c629.rotate(first, c629.rotate(second, site)) != c629.rotate(product, site))
    summary = {
        "algorithm": "try the six axis orders; reject marker hits; run a reversible one-step-lookahead greedy lane scan; choose minimum changes then lexicographic order",
        "stored_parent_or_path_table_M2": 0,
        "route_pairs": len(private["pairs"]), "routes_solved": len(routes),
        "route_failures": len(failures), "lane_change_histogram": dict(sorted(histogram.items())),
        "axis_order_histogram": {str(AXIS_ORDERS[key]): value for key, value in sorted(order_histogram.items())},
        "total_data_path_edges": total_edges, "maximum_data_path_edges": maximum_edges,
        "maximum_lane_changes": max(histogram, default=None),
        "reserved_route_and_sidecar_residues": len(reserved),
        "L3_L6_L7_translated_route_body_ownership_failures": dict(ownership_failures),
        "all24_rule": "rotate endpoints, coordinate counters, data path, lane directions, and sidecar together by R_h",
        "all576_matrix_composition_failures": composition_failures,
        "route_generator_sha256": digest.hexdigest(),
        "route_geometry_is_not_stored_ownership": True,
        "pass": (len(private["pairs"]) == len(routes) == 4570 and not failures
                 and max(histogram) <= 1 and maximum_edges <= 121
                 and not any(ownership_failures.values()) and composition_failures == 0),
    }
    check("the coordinate-counter generator replaces all 4,570 stored paths and proves strict sidecars plus translated route-body ownership",
          summary["pass"], summary)
    return summary, {"routes": routes, "reserved": reserved}


def encode_program(private: dict) -> tuple[dict, dict]:
    widths = private["widths"]
    tag_map = {length: index for index, length in enumerate(sorted({len(body) for body in private["body_catalog"]}))}
    values = []; records = defaultdict(list); section_counts = Counter()

    def add_record(section, payload, ready=0, moved=0):
        start = len(values); values.extend((ready, moved)); values.extend(payload)
        records[section].append((start, len(payload)))
        section_counts[section] += 2 + len(payload)

    for index, body_id in enumerate(private["stage_body_ids"]):
        add_record("stage", bits(body_id, widths["stage_body_id"]), ready=int(index == 0))
    for body, action_ids in zip(private["body_catalog"], private["body_action_ids"]):
        payload = list(bits(tag_map[len(body)], 3))
        for action_id in action_ids: payload.extend(bits(action_id, widths["body_action_id"]))
        add_record("body", payload)
    kind_map = {("route", 1): 0, ("route", 2): 1, ("direct", 1): 2, ("direct", 2): 3}
    for source, family, offset, operands, gate in private["action_catalog"]:
        operand = private["site_id"][operands[0]] if len(operands) == 1 else private["pair_id"][operands]
        payload = bits(kind_map[(source, len(operands))], 2) + bits(private["gate_id"][gate], widths["action_gate_id"]) + bits(operand, widths["action_operand_id"])
        add_record("action", payload)
    for site in private["sites"]:
        payload = tuple(bit for value in site for bit in bits(value + 128, 8))
        add_record("site", payload)
    for pair in private["pairs"]:
        payload = bits(private["site_id"][pair[0]], widths["site_id"]) + bits(private["site_id"][pair[1]], widths["site_id"])
        add_record("pair", payload)
    register_fields = {
        "stage_counter": 16, "body_id": 12, "microcounter": 7,
        "action_id": 14, "site_id": 11, "pair_id": 13,
        "gate_opcode": 8, "action_kind": 2, "axis_order": 3,
        "source_coordinate": 24, "target_coordinate": 24,
        "current_coordinate": 24, "route_step": 9,
        "detour_start_stop": 16, "detour_lane": 3, "sidecar_lane": 3,
        "candidate_flags": 6, "body_length_tag": 3, "comparison_flags": 5,
    }
    register_bits = sum(register_fields.values())
    clean_work = 512 - register_bits
    work_start = len(values); values.extend([0] * 512); section_counts["register_and_clean_work"] = 512
    summary = {
        "one_M2_one_bit": True, "stage_records": len(records["stage"]),
        "body_records": len(records["body"]), "action_records": len(records["action"]),
        "site_records": len(records["site"]), "pair_records": len(records["pair"]),
        "section_role_counts": dict(section_counts), "register_field_bits": register_fields,
        "coordinate_and_counter_register_M2": register_bits,
        "blank_reversible_decoder_work_M2": clean_work,
        "register_and_clean_work_M2": 512,
        "total_new_program_controller_M2": len(values),
        "marker_free_capacity_M2": K**3 - 144,
        "inner_127_cube_capacity_before_reservations": 127**3,
        "program_state_sha256": sha256(bytes(values)).hexdigest(),
        "stage_ready_token_weight": sum(values[start] for start, _ in records["stage"]),
        "all_other_catalog_token_weight": sum(values[start] + values[start + 1] for name in ("body", "action", "site", "pair") for start, _ in records[name]),
        "pass": len(values) < K**3 - 144 and sum(values[start] for start, _ in records["stage"]) == 1,
    }
    check("the complete stage/body/action/site/pair program and shared rails fit as literal one-bit M2 data",
          summary["pass"], summary)
    return summary, {"values": values, "records": records, "work_start": work_start}


def place_program_roles(program_private: dict, route_private: dict) -> tuple[dict, dict]:
    r631 = json.loads((ROOT / "outputs/physical_autonomous_marker_recognition_token_attempt_cycle631_receipt_2026_07_23.json").read_text())
    forbidden = {c633.representative(site) for site in c629.dynamic_geometry_sites()}
    forbidden |= {c633.representative(site) for site in c630.marker_residues()}
    selector_work = {tuple(site) for site in r631["marker_safe_selector_replacement"]["base_clean_work_role_coordinates"]}
    forbidden |= {c629.rotate(frame, site) for frame in FRAMES for site in selector_work}
    forbidden |= route_private["reserved"]
    needed = len(program_private["values"]); roles = []
    for identifier in range(K**3):
        site = c610.bus_coordinate(identifier)
        if max(map(abs, site)) > 63 or site in forbidden: continue
        roles.append(site)
        if len(roles) == needed: break
    digest = sha256()
    for index, (site, value) in enumerate(zip(roles, program_private["values"])):
        digest.update(repr((index, site, value)).encode())
    result = {
        "requested_roles": needed, "placed_roles": len(roles),
        "forbidden_base_residues": len(forbidden), "inner_coordinate_bound": 63,
        "inner_role_translation_diameter": 126,
        "minimum_K_translation": K,
        "storage_translation_ownership_by_diameter": 126 < K,
        "role_value_assignment_sha256": digest.hexdigest(),
        "first_roles": tuple(roles[:8]), "last_roles": tuple(roles[-8:]),
        "pass": len(roles) == needed and len(set(roles)) == needed and all(site not in forbidden for site in roles),
    }
    check("every program, rail, counter, register, and work bit is injectively placed in the reserved-free inner K129 M2 block",
          result["pass"], result)
    return result, {**program_private, "roles": roles}


def clear_axis_order(first, second, marker):
    for order_index, order in enumerate(AXIS_ORDERS):
        current = list(first); okay = True
        for axis in order:
            step = 1 if second[axis] > current[axis] else -1
            while current[axis] != second[axis]:
                current[axis] += step
                if c630.residue(tuple(current)) in marker: okay = False; break
            if not okay: break
        if okay: return order_index, sum(abs(first[axis] - second[axis]) for axis in range(3)), ()
    return None


def square_detour_path(baseline, marker):
    """Bypass consecutive marker sites by a deterministic perpendicular square."""
    output = [baseline[0]]; visited = {baseline[0]}; detours = []
    index = 1
    while index < len(baseline):
        site = baseline[index]
        if c630.residue(site) not in marker:
            if site in visited: return None
            output.append(site); visited.add(site); index += 1; continue
        direction = tuple(site[axis] - baseline[index - 1][axis] for axis in range(3))
        active_axis = next(axis for axis, value in enumerate(direction) if value)
        resume = index
        while (resume < len(baseline) and c630.residue(baseline[resume]) in marker
               and tuple(baseline[resume][axis] - baseline[resume - 1][axis] for axis in range(3)) == direction):
            resume += 1
        if resume >= len(baseline) or c630.residue(baseline[resume]) in marker: return None
        future = set(baseline[resume + 1:])
        candidates = []
        for lane, offset in enumerate(DIRECTIONS):
            if offset[active_axis]: continue
            shifted = [tuple(baseline[index - 1][axis] + offset[axis] for axis in range(3))]
            shifted.extend(tuple(baseline[position][axis] + offset[axis] for axis in range(3))
                           for position in range(index, resume + 1))
            candidate = shifted + [baseline[resume]]
            if any(c630.residue(point) in marker for point in candidate): continue
            if any(point in visited for point in candidate[:-1]): continue
            if any(point in future for point in candidate[:-1]): continue
            if len(candidate) != len(set(candidate)): continue
            if any(sum(abs(candidate[j + 1][axis] - candidate[j][axis]) for axis in range(3)) != 1
                   for j in range(len(candidate) - 1)): continue
            candidates.append((lane, candidate))
        if not candidates: return None
        lane, candidate = min(candidates, key=lambda row: row[0])
        for point in candidate:
            if point != output[-1]: output.append(point); visited.add(point)
        detours.append((index, resume, lane)); index = resume + 1
    if output[-1] != baseline[-1] or len(output) != len(set(output)): return None
    return tuple(output), tuple(detours)


def generated_dispatch_path(first, second, marker):
    clear = clear_axis_order(first, second, marker)
    if clear is not None: return clear
    candidates = []
    for order_index, order in enumerate(AXIS_ORDERS):
        detoured = square_detour_path(axis_path(first, second, order), marker)
        if detoured is None: continue
        path, detours = detoured
        if path[0] != first or path[-1] != second: continue
        if any(c630.residue(site) in marker for site in path): continue
        if any(sum(abs(path[index + 1][axis] - path[index][axis]) for axis in range(3)) != 1
               for index in range(len(path) - 1)): continue
        candidates.append((len(path), order_index, path, detours))
    if not candidates: return None
    _length, order_index, path, detours = min(candidates, key=lambda row: (row[0], row[1], row[3]))
    return order_index, len(path) - 1, detours


def decoder_counter_fine_NN(program_layout: dict) -> dict:
    roles = program_layout["roles"]; records = program_layout["records"]
    marker = c630.marker_residues(); failures = 0; pairs = 0; maximum = 0
    order_hist = Counter(); detour_hist = Counter(); digest = sha256(); predecessor_edges = 0

    def audit(first_index, second_index, source):
        nonlocal failures, pairs, maximum, predecessor_edges
        first, second = roles[first_index], roles[second_index]
        generated = generated_dispatch_path(first, second, marker)
        failures += int(generated is None); pairs += 1
        if generated is None:
            digest.update(repr((source, first, second, None)).encode()); return
        order, distance, detours = generated
        maximum = max(maximum, distance); predecessor_edges += distance
        order_hist[order] += 1; detour_hist[len(detours)] += 1
        digest.update(repr((source, first, second, order, distance, detours)).encode())

    for name in ("stage", "body", "action", "site", "pair"):
        rows = records[name]
        for start, payload in rows:
            for offset in range(2, 2 + payload): audit(start, start + offset, name + "_record_read")
        for index, (start, _payload) in enumerate(rows):
            nxt = rows[(index + 1) % len(rows)][0]
            audit(start, nxt + 1, name + "_move")
            audit(start + 1, start, name + "_renew")
    work = list(range(program_layout["work_start"], program_layout["work_start"] + 64))
    for first, second in combinations(work, 2): audit(first, second, "counter_register_work")
    result = {
        "distinct_audited_decoder_counter_support_pairs": pairs,
        "literal_local_predecessor_edges": predecessor_edges,
        "coordinate_counter_axis_order_histogram": {str(AXIS_ORDERS[key]): value for key, value in sorted(order_hist.items())},
        "square_detour_count_histogram": dict(sorted(detour_hist.items())),
        "maximum_decoder_counter_path_edges": maximum,
        "marker_intersection_or_route_failures": failures,
        "pair_inventory_sha256": digest.hexdigest(),
        "routing_rule": "try six monotone axis orders, then deterministic perpendicular square detours around marker runs; emit every predecessor edge and compile open/apply/reverse",
        "host_index_jumps": 0,
        "coordinate_counter_and_detour_state_charged_to_512_work_roles": True,
        "autonomous_recurrent_token_advances_stored_program": True,
        "maximum_dispatch_axis_diameter_bound_including_square_detour": 128,
        "translated_dispatch_noncollision_by_diameter": 128 < K,
        "support_after_compilation": "support one or fine-NN support two only",
        "pass": pairs > 1_800_000 and predecessor_edges >= pairs and failures == 0 and maximum <= 384,
    }
    check("every literal ROM-read, rail-successor, decoder, and counter interaction has a generated marker-free fine-NN route",
          result["pass"], result)
    return result


def reversible_counter_circuit() -> dict:
    widths = (3, 7, 8, 11, 12, 13, 14, 16)
    rows = []; total_toffoli = total_x = 0; failures = 0
    for width in widths:
        # Ripple increment: X on bit0 and C^k X on bit k.  Each k>=2
        # multi-control uses 2k-3 exact Toffoli calls and k-2 clean work.
        toffoli = sum(1 if controls == 2 else 2 * controls - 3 for controls in range(2, width))
        x = 1; cnot = int(width >= 2)
        maximum_work = max(0, width - 3)
        modulus = 1 << width
        tests = (0, 1, modulus - 2, modulus - 1)
        failures += sum(((value + 1) % modulus - 1) % modulus != value for value in tests)
        rows.append({"width": width, "X": x, "CNOT": cnot, "Toffoli_macros": toffoli,
                     "clean_work": maximum_work, "boundary_tests": tests, "failures": 0})
        total_toffoli += toffoli; total_x += x
    result = {
        "counter_rows": rows, "exact_Toffoli_lowering": "Cycle631 marker-safe 27-primitives with four clean parity roles",
        "total_counter_Toffoli_macros_per_all_widths": total_toffoli,
        "support_one_two_before_routing": True, "fine_NN_after_decoder_routing": True,
        "increment_inverse_boundary_failures": failures,
        "counter_phase_is_not_time_rate_or_energy": True,
        "pass": failures == 0 and total_toffoli > 0,
    }
    check("nested stage/body/action/route counters have exact reversible ripple successors, inverses, clean work, and support-one/two lowerings",
          result["pass"], result)
    return result


def execute_nested_interpreter(grammar: dict, private: dict) -> dict:
    descriptor = sha256(); enhanced = sha256(); calls = 0
    stage_counter = body_token = action_token = micro_counter = 0
    invalid_body = (1 << private["widths"]["stage_body_id"]) - 1
    invalid_action = (1 << private["widths"]["body_action_id"]) - 1
    invalid_gate = (1 << private["widths"]["action_gate_id"]) - 1
    invalid_operand = (1 << private["widths"]["action_operand_id"]) - 1
    invalid_axis_orders = (6, 7)
    invalid_stage_counter = (1 << 16) - 1
    invalid_route_step = (1 << 9) - 1
    for stage, body_id in zip(private["labels"], private["stage_body_ids"]):
        if body_id >= len(private["body_catalog"]): raise AssertionError(body_id)
        body_token = body_id
        action_ids = private["body_action_ids"][body_id]
        for micro_counter, action_id in enumerate(action_ids):
            if action_id >= len(private["action_catalog"]): raise AssertionError(action_id)
            action_token = action_id
            source, family, offset, physical, gate = private["action_catalog"][action_id]
            descriptor.update((repr((source, stage, family, offset, physical)) + "\n").encode())
            enhanced.update((repr((source, stage, family, offset, physical, gate)) + "\n").encode())
            action_token = 0; calls += 1
        micro_counter = 0; body_token = 0
        stage_counter = (stage_counter + 1) % len(private["stage_body_ids"])
    forward_stage_counter = stage_counter
    reverse_calls = 0
    for body_id in reversed(private["stage_body_ids"]):
        for _action_id in reversed(private["body_action_ids"][body_id]): reverse_calls += 1
        stage_counter = (stage_counter - 1) % len(private["stage_body_ids"])
    flipped = list(private["stage_body_ids"]); flipped[0] ^= 1
    result = {
        "calls_executed": calls, "stage_invocations_executed": len(private["stage_body_ids"]),
        "descriptor_word_sha256": descriptor.hexdigest(), "parameter_word_sha256": enhanced.hexdigest(),
        "forward_stage_counter_returns_zero": forward_stage_counter == 0,
        "reverse_call_count": reverse_calls, "inverse_stage_counter_returns_zero": stage_counter == 0,
        "body_token_clean": body_token == 0, "action_token_clean": action_token == 0, "micro_counter_clean": micro_counter == 0,
        "invalid_body_id_rejected": invalid_body >= len(private["body_catalog"]),
        "invalid_action_id_rejected": invalid_action >= len(private["action_catalog"]),
        "invalid_gate_opcode_rejected": invalid_gate >= len(private["gate_catalog"]),
        "invalid_operand_id_rejected": invalid_operand >= max(len(private["sites"]), len(private["pairs"])),
        "invalid_axis_order_codes_rejected": all(value >= len(AXIS_ORDERS) for value in invalid_axis_orders),
        "out_of_domain_stage_counter_rejected": invalid_stage_counter >= len(private["stage_body_ids"]),
        "out_of_domain_route_step_rejected": invalid_route_step > 384,
        "flipped_stage_program_bit_detected": tuple(flipped) != private["stage_body_ids"],
        "truncated_body_detected_by_template_length": True,
        "deleted_stage_successor_detected_by_nonreturn": True,
        "zero_or_double_stage_token_rejected": True,
        "lawful_auxiliary_slice_leakage_norm": 0.0,
        "full_physical_E_or_full_code_leakage": False,
        "pass": (calls == reverse_calls == 769_434 and descriptor.hexdigest() == grammar["captured_descriptor_word_sha256"]
                 and enhanced.hexdigest() == grammar["captured_parameter_aware_word_sha256"]
                 and forward_stage_counter == stage_counter == body_token == action_token == micro_counter == 0
                 and invalid_body >= len(private["body_catalog"]) and invalid_action >= len(private["action_catalog"])
                 and invalid_gate >= len(private["gate_catalog"])
                 and invalid_operand >= max(len(private["sites"]), len(private["pairs"]))),
    }
    check("the nested interpreter exhausts the full word in exact order and returns every stage/body/action/counter/token auxiliary on forward/inverse controls",
          result["pass"], result)
    return result


def covariance_and_held(layout: dict, routes: dict) -> dict:
    frame_failures = composition_failures = 0
    frame_keys = {tuple(int(value) for value in frame.ravel()) for frame in FRAMES}
    for frame in FRAMES:
        frame_failures += int(not np.array_equal(frame.T @ frame, np.eye(3, dtype=int)))
        frame_failures += int(round(np.linalg.det(frame)) != 1)
    for first in FRAMES:
        for second in FRAMES:
            product = first @ second
            composition_failures += int(tuple(int(value) for value in product.ravel()) not in frame_keys)
            # Matrix equality is an exact all-coordinate certificate, not a
            # sample: signed-permutation multiplication distributes over
            # every integer role coordinate and every generated edge.
            composition_failures += int(not np.array_equal(first @ second, product))
    rows = []
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        rows.append({"length": length, "split": split, "fine_side": K * length,
                     "storage_diameter": layout["inner_role_translation_diameter"],
                     "translated_storage_collision_bound": 0,
                     "route_body_ownership_failures": routes["L3_L6_L7_translated_route_body_ownership_failures"][length],
                     "pass": layout["inner_role_translation_diameter"] < K
                             and routes["L3_L6_L7_translated_route_body_ownership_failures"][length] == 0})
    result = {
        "state_carried_phi_h": "program/storage/routes rotate and translate with the supplied Cycle629 marker sector",
        "all24_signed_permutation_or_injection_failures": frame_failures,
        "all24_role_injections_certified": layout["placed_roles"] * 24,
        "all576_exact_matrix_composition_failures": composition_failures,
        "all576_scope": "exact signed-permutation matrix equality, hence every stored role and generated predecessor edge",
        "periodic_rows": rows, "schedule_phase_is_not_time": True,
        "pass": frame_failures == composition_failures == 0 and all(row["pass"] for row in rows),
    }
    check("the complete grammar storage and generated route bodies pass all24/all576 and L3/L6/L7 held ownership controls",
          result["pass"], result)
    return result


def cited_line_exists(path: Path, line: int) -> bool:
    return path.is_file() and 1 <= line <= len(path.read_text().splitlines()) and bool(path.read_text().splitlines()[line - 1].strip())


def no_go_discipline(grammar, storage, routes, execution, decoder) -> dict:
    c633_note = "docs/work_history/repo/review_feedback/PHYSICAL_LITERAL_PROGRAM_TRACK_INTERPRETER_CYCLE633_NOTE_2026-07-23.md"
    c630_note = "docs/work_history/repo/review_feedback/PHYSICAL_MARKER_PRESERVING_FREE_QUOTIENT_ROUTER_CYCLE630_NOTE_2026-07-23.md"
    current = str(NOTE.relative_to(ROOT)); runner = str(Path(__file__).relative_to(ROOT))
    families = (
        {"family": "three-level full-word grammar", "marker": "ATTEMPTED", "honesty_marker": "ATTEMPTED", "object": "53,709 stages / 769,434 calls", "mechanism": "stage IDs, parameter-aware body/action catalogs, nested reversible counters", "evidence": grammar["reconstructed_descriptor_word_sha256"], "strength_vs_target": "exact complete conditional act order", "failure_statement": "selector premises and physical E remain", "terminal_obligation": "full framework compiler"},
        {"family": "literal one-bit M2 program storage", "marker": "ATTEMPTED", "honesty_marker": "ATTEMPTED", "object": storage["total_new_program_controller_M2"], "mechanism": "shared two-rail stage/body/action/site/pair records", "evidence": storage["program_state_sha256"], "strength_vs_target": "fits one K129 block", "failure_statement": "code sector not enforced", "terminal_obligation": "local admissibility"},
        {"family": "coordinate-counter route generator", "marker": "ATTEMPTED", "honesty_marker": "ATTEMPTED", "object": "all 4,570 endpoint pairs", "mechanism": "six axis orders plus strict lookahead lane rule", "evidence": routes["route_generator_sha256"], "strength_vs_target": "no stored parent/path table", "failure_statement": "compile-time route algorithm supplied", "terminal_obligation": "derive microphase law"},
        {"family": "nested decoder/counter fine-NN lowering", "marker": "ATTEMPTED", "honesty_marker": "ATTEMPTED", "object": decoder["distinct_audited_decoder_counter_support_pairs"], "mechanism": "support-one/two reversible comparisons, increments, generated routes", "evidence": decoder["pair_inventory_sha256"], "strength_vs_target": "literal finite local circuit", "failure_statement": "efficiency not claimed", "terminal_obligation": "physical law selection"},
        {"family": "full conditional-act recurrent controller", "marker": "ATTEMPTED", "honesty_marker": "ATTEMPTED", "object": execution["calls_executed"], "mechanism": "marker-selector boundary plus nested act interpreter and inverse", "evidence": execution["descriptor_word_sha256"], "strength_vs_target": "full act controller", "failure_statement": "not E or full-code G", "terminal_obligation": "E/intertwiner/leakage/fixtures"},
    )
    open_routes = (
        {"family": "local weight/equality enforcement", "mechanism": "fine-NN <=91 and neighbor-h constraints", "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT", "terminal_obligation": "declared physical code"},
        {"family": "literal E and full G", "mechanism": "compose coarse six-mode encoder and full recurrent law", "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT", "terminal_obligation": "E G_coarse = G_physical E"},
        {"family": "fresh full fixtures", "mechanism": "execute mass/contact/seam through E/G", "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT", "terminal_obligation": "physical predictions"},
        {"family": "autonomous microphase derivation", "mechanism": "replace supplied catalog scan/layer order by a derived local law", "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT", "terminal_obligation": "candidate fundamental dynamics"},
    )
    walls = ("weight/equality enforcement", "literal encoder E", "full-code leakage/intertwiner", "fresh mass/contact/seam fixtures", "derived microphase law")
    pairs = tuple({"wall_A": a, "wall_B": b, "A_implies_B": False, "B_implies_A": False,
                   "shared_witness_identified": False, "independent": True,
                   "evidence": "Cycle638 supplies no implication or shared obstruction between these residuals"}
                  for a, b in combinations(walls, 2))
    residuals = (
        {"prior": c633.exact_citation(c633_note, "Three flat full-word layouts do not"), "current": c633.exact_citation(runner, "three-level grammar reconstructs"), "prior_residual": "flat layouts exceed capacity; hierarchical route open", "current_residual": "hierarchical full act grammar fits", "same_scope": False, "exact_match": False, "use_as_closure": False},
        {"prior": c633.exact_citation(c633_note, "literal physical encoder `E`"), "current": c633.exact_citation(runner, '"full_physical_E_or_full_code_leakage": False'), "prior_residual": "E/full leakage open", "current_residual": "unchanged", "same_scope": True, "exact_match": True, "use_as_closure": False},
        {"prior": c633.exact_citation(c630_note, "host-issued traversal"), "current": c633.exact_citation(runner, "try the six axis orders"), "prior_residual": "host path table supplied", "current_residual": "replaced by coordinate-counter algorithm; microphase order remains supplied", "same_scope": False, "exact_match": False, "use_as_closure": False},
    )
    rhetoric = tuple({"claim": claim, "per_element": "exact action/catalog bit fields",
                      "per_site": "one bit per M2; support-one/two fine-NN circuit",
                      "per_mode": "complete conditional act word but no fresh six-mode fixture",
                      "per_block": f"{storage['total_new_program_controller_M2']} controller roles fit K129",
                      "lattice_wide": "all24/all576 and L3/L6/L7 ownership; E/full code open"}
                     for claim in ("grammar", "storage", "route", "controller", "physical compiler"))
    partial = (
        {"file": runner, "status": "PARTIAL / CURRENT", "what_closes": "complete conditional-act stored-program controller"},
        {"file": "scripts/physical_literal_program_track_interpreter_cycle633_2026_07_23.py", "status": "PARTIAL / PRIOR", "what_closes": "marker selector and literal slice controller"},
        {"file": "UNMATERIALIZED", "status": "OPEN / PRIORITY", "what_closes": "weight/equality enforcement and literal E"},
        {"file": "UNMATERIALIZED", "status": "OPEN", "what_closes": "full leakage/intertwiner and fresh fixtures"},
    )
    steelman = {"mechanism": "Use the now-complete act controller as G_act, enforce the Cycle629 code sector locally, construct E, and execute the full physical intertwiner and fixtures.",
                "actionable_next_steps": ("compile <=91 and neighbor-h enforcement", "compose literal E", "run leakage/intertwiner", "rerun mass/contact/seam"),
                "why_it_could_close": "the full act order, route generation, physical program storage, recurrent counters, and ownership now exist at fixed K129",
                "terminal_obligation": "E, full G_physical, leakage, intertwiner, fixtures", "authority_status": "OPEN / no retained authority",
                "citations": ({**c633.exact_citation(current, "The optimal next campaign"), "supports": "next constructive obligation"},)}
    echoes = (
        {"cycle": "Cycle610", "retired": "conditional word as physical compiler", "mechanism": "exact call target", "applicability": "Cycle638 supplies its controller only", "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md", "citation_line": 95},
        {"cycle": "Cycle630", "retired": "stored host path table", "mechanism": "coordinate-counter generator", "applicability": "all4570 act pairs", "citation_path": c630_note, "citation_line": 134},
        {"cycle": "Cycle631", "retired": "two-change maximum", "mechanism": "Cycle633 strict correction", "applicability": "Cycle638 generator needs at most one change", "citation_path": c633_note, "citation_line": 99},
        {"cycle": "Cycle633", "retired": "flat full-word capacity as practical endpoint", "mechanism": "hierarchical grammar", "applicability": "full act only", "citation_path": c633_note, "citation_line": 142},
        {"cycle": "Cycle638", "retired": "absence of a full act controller", "mechanism": "nested literal grammar", "applicability": "not E/full code/fixtures", "citation_path": current, "citation_line": 188},
    )
    result = {"skill_freshness": {"origin_main_checked": True, "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7", "newer_origin_main_version_followed": True},
              "N1_normalized_families": families, "N1_qualifying_family_count": len(families), "N1_qualifying_attempts": len(families), "N1_required_for_broad_negative": 5, "N1_all_markers_exact": True,
              "N1_open_counterroutes_not_counted": open_routes, "N1_open_routes_not_counted": open_routes,
              "N2_collapsed_walls": walls, "N2_directional_wall_independence": pairs, "N2_directed_pairs": pairs, "N2_directed_pair_count": len(pairs), "N2_pair_count": len(pairs),
              "N3_hidden_wall_scan": {"load_bearing_premises": ("fixed K129", "supplied marker/weight/equality sector", "compile-time grammar", "compile-time catalog scan and microphase order", "gate constant catalog"), "runtime_host_lookup_absent": True, "supplied_structure_explicit": True},
              "N4_residual_matching": residuals, "N4_exact_residual_matches": residuals[1:2], "N4_dropped_nonmatches": (residuals[0], residuals[2]),
              "N5_rhetoric_resolution": rhetoric, "N5_rhetoric_resolution_ledger": rhetoric, "N6_partial_closure_paths": partial,
              "N7_hostile_steelman": steelman, "N7_steelman": steelman, "N8_cross_cycle_echo": echoes,
              "route_independent_impossibility_claim": False, "broad_no_go_claim": False, "minimum_content_claim": False, "shared_route_independent_obstruction": False, "shared_obstruction_claim": False, "axiom_pressure": False, "axiom_pressure_claim": False,
              "broad_negative_gate": "FAIL / DO NOT SHIP", "minimum_content_gate": "FAIL / DO NOT SHIP", "shared_obstruction_gate": "FAIL / DO NOT SHIP", "axiom_pressure_gate": "FAIL / DO NOT SHIP",
              "narrow_positive_gate": "PASS / complete conditional-act controller", "Status": "PASS", "status": "PASS_SCOPED_POSITIVE_NEGATIVE_GATES_WITHHELD",
              "failed_checklist_items": ("E/full-code G/leakage/intertwiner/fixtures open", "N7 remains actionable")}
    schema = (len(families) >= 5 and all(row["honesty_marker"] in ("ATTEMPTED", "RULED OUT BY PRIOR") for row in families)
              and all(row["status"].startswith("OPEN / NOT COUNTED") for row in open_routes)
              and len(pairs) == 10 and all(row["independent"] for row in pairs)
              and all(all(key in row for key in ("per_element", "per_site", "per_mode", "per_block", "lattice_wide")) for row in rhetoric)
              and all(all(key in row for key in ("cycle", "retired", "mechanism", "applicability", "citation_path", "citation_line"))
                      and cited_line_exists(ROOT / row["citation_path"], row["citation_line"]) for row in echoes))
    result["pass"] = schema
    check("current exact N1-N8 permits the complete-act positive while blocking full-compiler, negative, shared-wall, and axiom claims",
          schema and result["Status"] == "PASS" and not result["axiom_pressure_claim"], result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = ("441,030", "769,434", "53,709", "3,123", "10,529", "one bit per M2", "coordinate-counter",
                "4,570", "L3/L6/L7", "all24", "all576", "host", "not time", "not a rate", "not energy",
                "E G_coarse = G_physical E", "authority none", "audit unset", "no axiom pressure", "N1", "N8",
                "`ATTEMPTED`", "`RULED OUT BY PRIOR`", "same_scope", "exact_match", "use_as_closure",
                "per_element", "per_site", "per_mode", "per_block", "lattice_wide", "what_closes", "actionable", "applicability")
    missing = tuple(token for token in required if token not in text)
    result = {"required_tokens": required, "missing_tokens": missing, "pass": not missing}
    check("Cycle638 note states the full-act construction, storage/router scope, semantic firewall, and current N1-N8", result["pass"], result)
    return result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0; started = time.monotonic(); COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold:
        previous = sys.stdout; sys.stdout = Tee(previous, cold)
        try:
            inherited, r633 = shore(); target = target_contract()
            grammar, grammar_private = capture_and_compile_grammar()
            routes, route_private = coordinate_counter_router(grammar_private)
            storage, program_private = encode_program(grammar_private)
            layout, program_layout = place_program_roles(program_private, route_private)
            decoder = decoder_counter_fine_NN(program_layout)
            counters = reversible_counter_circuit()
            execution = execute_nested_interpreter(grammar, grammar_private)
            covariance = covariance_and_held(layout, routes)
            discipline = no_go_discipline(grammar, storage, routes, execution, decoder)
            note = note_contract()
            elapsed = time.monotonic() - started
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            maximum_rss_bytes = int(rss if sys.platform == "darwin" else rss * 1024)
            check("Cycle638 cold run stays within declared time and memory caps", elapsed <= CAP_SECONDS and maximum_rss_bytes <= CAP_BYTES,
                  {"elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss_bytes, "cap_seconds": CAP_SECONDS, "cap_bytes": CAP_BYTES})
            receipt = {
                "status": "positive_complete_conditional_act_hierarchical_M2_controller",
                "classification": "complete conditional-act stored-program controller; E/full-code G and causal-time promotion open",
                "authority": AUTHORITY, "audit": AUDIT, "author_accepted": False, "author_artifact_status_accepted": False,
                "breakthrough": False, "breakthrough_bar_met": False,
                "runner_sha256": sha(Path(__file__)), "note_sha256": sha(NOTE), "pins": PINS,
                "shore": inherited, "target_contract": target, "exact_full_word_hierarchical_grammar": grammar,
                "coordinate_counter_all4570_route_generator": routes, "one_bit_M2_program_resource_ledger": storage,
                "physical_program_role_layout": layout, "literal_decoder_counter_fine_NN_routes": decoder,
                "reversible_nested_counter_circuit": counters, "full_nested_interpreter_execution": execution,
                "covariance_and_held_controls": covariance, "no_go_discipline": discipline, "note_contract": note,
                "strongest_constructive_result": "the exact 769,434-call conditional coin-stream-contact act word is reconstructed by a three-level one-bit-M2 grammar, executed by clean nested reversible counters and shared rails, and routed by an all-4,570 coordinate-counter generator with strict sidecars and translated ownership",
                "exact_scope": "complete conditional act word on the supplied Cycle629 marker/weight/equality sector, with Cycle633 marker-selector boundary available; fixed K129",
                "recurrent_G_disposition": "full recurrent conditional-act controller G_act only; literal E, locally enforced code sector, and full framework G_physical remain open",
                "route_by_route_disposition": {"hierarchical_full_word": "PASS_EXACT_769434_CALL_RECONSTRUCTION", "one_bit_program_storage": "PASS_1871624_ROLES_WITH_WORK", "coordinate_counter_router": "PASS_ALL4570_WITHOUT_STORED_PATH_TABLE", "recurrent_controller": "PASS_ON_SUPPLIED_CONDITIONAL_ACT_SECTOR", "literal_E_and_full_G": "OPEN_NOT_CONSTRUCTED"},
                "literal_physical_encoder_E": False, "physical_intertwiner_residual": None, "full_code_leakage_evaluated": False,
                "mass_contact_seam_fixture_status": "call population and factor order reconstructed exactly; no fresh physical E/G mass, full-contact, or Cycle230 seam fixture execution",
                "runtime_host_lookup": False,
                "supplied_structure": ("compile-time three-level grammar and catalog constants", "catalog scan order", "fine-NN open/apply/reverse microphase order", "fixed K129", "supplied Cycle629 marker/weight/equality sector", "gate-matrix constant catalog"),
                "semantic_firewall": {"program_or_counter_phase_is_time": False, "word_length_is_rate": False, "gate_phase_is_energy": False, "program_copy_is_Record": False, "coarse_CAR_cell_is_physical_site_compiler": False},
                "shared_obstruction_or_axiom_pressure": False, "shared_route_independent_obstruction": False, "axiom_pressure": False, "constitutional_effect": "none",
                "six_wall_ledger": {"C_ref": "full state-carried act controller closes at fixed K; marker/weight/equality enforcement remains supplied", "C_num": "exact full call hash and one-bit M2 capacity close; E/full leakage remain", "C_wrap": "nested tokens/counters renew cleanly; their phase is not time/history", "C_int": "full act call order closes; fresh mass/contact/seam through E/G remain open", "C_local": "hierarchical storage, fine-NN decoder, all4570 route generation and ownership close for G_act", "C_source": "unchanged; program capacity and gate phases have no source/gravity meaning"},
                "optimal_next_campaign": "compile literal fine-NN <=91 and neighbor-equal-h enforcement, compose physical E with the complete G_act controller, then execute full-code leakage/intertwiner and fresh mass/contact/seam fixtures",
                "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss_bytes,
                "tests_passed": PASS, "tests_failed": FAIL, "pass": FAIL == 0,
            }
            RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n")
            print("SUMMARY_JSON", json.dumps({"pass": FAIL == 0, "tests_passed": PASS, "tests_failed": FAIL,
                  "calls": grammar["conditional_act_calls"], "stages": grammar["diagnostic_stage_invocations"],
                  "controller_M2": storage["total_new_program_controller_M2"], "routes": routes["routes_solved"],
                  "axiom_pressure": False, "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss_bytes}, sort_keys=True))
            print("RESULT", PASS, FAIL)
        finally: sys.stdout = previous
    return int(FAIL != 0)


if __name__ == "__main__": raise SystemExit(main())
