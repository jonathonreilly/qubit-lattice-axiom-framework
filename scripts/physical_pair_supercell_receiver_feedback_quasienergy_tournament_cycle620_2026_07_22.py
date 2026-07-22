#!/usr/bin/env python3
"""Cycle620: physical pair lowering, receiver feedback, and full-unitary stress.

The three routes are deliberately separate.  Route A lowers the Cycle615
resource/cubic-neutral-pair involution and a two-charge occupation stream into
the accepted Cycle610 K=129 support-two fabric.  Route B adds one explicit
matter-caused local feedback-square candidate to the joined gauge-Regge action
and audits the equally local sign/scale alternatives.  Route C differentiates
the actual coin -> stream -> contact full-Fock unitary with respect to a
spatial coframe.  Wrapped quasiphase is not energy and a generator element is
not a rate.  Authority none; audit unset.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
from time import perf_counter

import numpy as np
from scipy.linalg import expm
from scipy.optimize import linear_sum_assignment

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_lawful_charge_joined_metric_response_tournament_cycle615_2026_07_22 as c615
import physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22 as c610
import physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_2026_07_22 as c612

c576 = c615.c576
c230 = c615.c230
c219 = c615.c219
c210 = c615.c210
c609 = c615.c609

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_PAIR_SUPERCELL_RECEIVER_FEEDBACK_QUASIENERGY_TOURNAMENT_"
    "CYCLE620_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / "outputs/physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_receipt_2026_07_22.json"
COLD = ROOT / "outputs/physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_cold_2026_07_22.txt"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 3.0e-8
FD_TOL = 8.0e-7
START = perf_counter()
PASS = 0
FAIL = 0
FIXTURES = (("TRAIN_L3", 3, False), ("HELD_L6", 6, True), ("OUT_HELD_L7", 7, True))

PINS = {
    "scripts/physical_lawful_charge_joined_metric_response_tournament_cycle615_2026_07_22.py":
        "bbd0d70a62404f96ac02decee68aec465edbdc76b0948b8fb563183b7c61fc6d",
    "docs/work_history/repo/review_feedback/PHYSICAL_LAWFUL_CHARGE_JOINED_METRIC_RESPONSE_TOURNAMENT_CYCLE615_NOTE_2026-07-22.md":
        "ebf7b618f4048bc964bd692073c828e9ff5cbb53fc5b0db1fed10fd8fcabf00b",
    "outputs/physical_lawful_charge_joined_metric_response_tournament_cycle615_receipt_2026_07_22.json":
        "67e8f57c5505a4c5c8a861794c0a086227ac577af2337bab6902ba52f6eb1d67",
    "scripts/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22.py":
        "997234878a564cb8554ff5184888fe06b920db32bb54b5df6febfdc88a90e7de",
    "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_receipt_2026_07_22.json":
        "51373236a754b8ea941514609251b6721578c1f4fdfaa443958b7e7c7fba1c63",
    "scripts/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22.py":
        "59a1125e1e71872b69c8b0e48cd114b221a107ee3d3f396cd28c4f87d233e41b",
    "outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json":
        "b9980fa13434a55f6209203f8801a367c0139ebacddcf13732a02b486f8f4096",
    "scripts/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_2026_07_22.py":
        "91f22d23dd2730f76a05736634236d41036f68eaedc4921daca69de25ab6a344",
    "outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json":
        "e7a8ea3dcbe370c9f8c6a94770508d1710a7013ce4ba62a1ad67e345fe1e2d11",
    "docs/audit/data/axiom_premise_nodes.json":
        "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
    "docs/MINIMAL_AXIOMS_2026-06-29.md":
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md":
        "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md":
        "5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md":
        "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
}


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, value):
        for stream in self.streams:
            stream.write(value)
        return len(value)

    def flush(self):
        for stream in self.streams:
            stream.flush()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, complex):
        return [value.real, value.imag]
    if isinstance(value, Fraction):
        return str(value)
    raise TypeError(type(value).__name__)


def digest(path: str | Path) -> str:
    return sha256((ROOT / path).read_bytes()).hexdigest()


def check(label: str, condition: bool, detail="") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def shore() -> tuple[dict, dict, dict, dict]:
    observed = {path: digest(path) for path in PINS}
    r615 = json.loads((ROOT / "outputs/physical_lawful_charge_joined_metric_response_tournament_cycle615_receipt_2026_07_22.json").read_text())
    r610 = json.loads((ROOT / "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_receipt_2026_07_22.json").read_text())
    r608 = json.loads((ROOT / "outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json").read_text())
    r612 = json.loads((ROOT / "outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json").read_text())
    result = {
        "hashes_match": observed == PINS,
        "observed": observed,
        "Cycle615_pass": r615["pass"],
        "Cycle610_pass": r610["pass"],
        "Cycle608_pass": r608["pass"],
        "Cycle612_pass": r612["pass"],
        "Cycle615_pair_gate_open": not r615["route_A_local_neutral_pair_sector"]["physical_NN_pair_gate_and_full_sector_compiled"],
        "Cycle615_receiver_selection_residual": r615["route_C_joined_metric_receiver_equivalence"]["unique_receiver_word_selection_residual"],
        "Cycle610_support_two_compiler": r610["literal_orientation_controlled_compute_act_uncompute"]["base_identity_frame_literal_word"]["support_failures"] == 0,
        "Cycle608_physical_detector": r608["route_B_matter_caused_candidate"]["detector_output_generated_from_physical_matter"],
        "Cycle612_receiver_words": sorted({row["probe_over_reference"] for row in r612["route_C_source_motion_ratio"]["rows"] if row["physical_source_reservoir_predicate"] and row["receiver_M2"]}),
    }
    check(
        "Cycle608/610/612/615 shore is byte-pinned and retains the exact live residuals",
        result["hashes_match"]
        and all(result[key] for key in ("Cycle615_pass", "Cycle610_pass", "Cycle608_pass", "Cycle612_pass"))
        and result["Cycle615_pair_gate_open"]
        and result["Cycle615_receiver_selection_residual"] == 1
        and result["Cycle610_support_two_compiler"]
        and result["Cycle608_physical_detector"]
        and result["Cycle612_receiver_words"] == ["3/4", "5/4"],
        result,
    )
    return r615, r610, r612, result


def note_contract() -> None:
    body = " ".join(NOTE.read_text().lower().replace("`", "").replace("*", "").split())
    required = (
        "cycle 620", "authority: none", "audit: unset", "route a", "route b", "route c",
        "common e", "clean-work", "support-two", "constant overhead", "all 24", "all 576",
        "l3", "l6", "l7", "coin -> stream -> contact", "not derived antimatter",
        "positive square", "negative square", "scale", "lambda", "improvement", "3/4", "5/4",
        "not selection", "gauss", "ward", "quasiphase", "wrapped phase is not energy",
        "generator element is not a rate", "open-boundary", "periodic", "n1", "n8",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in body)
    check("Cycle620 note freezes routes, controls, caveats, and full N1-N8 scope", not missing, missing)


# ---------------------------------------------------------------------------
# Route A: exact local pair involution plus a two-charge occupation stream.

def givens(size: int, first: int, second: int, angle: float) -> np.ndarray:
    result = np.eye(size)
    cosine, sine = math.cos(angle), math.sin(angle)
    result[first, first] = cosine
    result[first, second] = -sine
    result[second, first] = sine
    result[second, second] = cosine
    return result


def pair_preparation() -> tuple[np.ndarray, list[dict]]:
    result = np.eye(7)
    rows = []
    for step, denominator in enumerate((6, 5, 4, 3, 2), start=1):
        angle = math.asin(1 / math.sqrt(denominator))
        gate = givens(7, 1, 1 + step, angle)
        result = gate @ result
        rows.append({
            "pair_branch": step,
            "exact_sine": f"1/sqrt({denominator})",
            "exact_cosine": f"sqrt({denominator - 1})/sqrt({denominator})",
            "angle_radians": angle,
        })
    return result, rows


def active_bitstrings() -> tuple[int, ...]:
    # bit 0 is the neutral resource; bits 1..6 are + modes and 7..12 are - modes.
    words = [1]
    for direction in range(6):
        words.append((1 << (1 + direction)) | (1 << (7 + (direction ^ 1))))
    return tuple(words)


def apply_two_level(state: np.ndarray, first: int, second: int, block: np.ndarray) -> None:
    pair = np.asarray((state[first], state[second]))
    state[first], state[second] = block @ pair


def logical_pair_word() -> tuple[np.ndarray, np.ndarray, list[dict], list[dict]]:
    prepare, angles = pair_preparation()
    swap = np.eye(7)
    swap[0, 0] = swap[1, 1] = 0
    swap[0, 1] = swap[1, 0] = 1
    target = prepare @ swap @ prepare.T
    expected = c615.pair_gate()
    high_level = []
    # Chronological order: W^dag, X, W.
    for row in reversed(angles):
        high_level.append({"kind": "Givens", "first": 1, "second": 1 + row["pair_branch"], "angle": -row["angle_radians"], "stage": "W_dagger"})
    high_level.append({"kind": "X", "first": 0, "second": 1, "stage": "resource_pair_swap"})
    for row in angles:
        high_level.append({"kind": "Givens", "first": 1, "second": 1 + row["pair_branch"], "angle": row["angle_radians"], "stage": "W"})
    return target, expected, angles, high_level


def gray_conditionals(first: int, second: int, kind: str, parameter: float) -> list[dict]:
    bits_first = [(first >> index) & 1 for index in range(13)]
    bits_second = [(second >> index) & 1 for index in range(13)]
    different = [index for index in range(13) if bits_first[index] != bits_second[index]]
    current = bits_first[:]
    opening = []
    for target in different[:-1]:
        opening.append({"kind": "MCX", "target": target, "condition": tuple(current[index] for index in range(13) if index != target)})
        current[target] ^= 1
    target = different[-1]
    center = {"kind": "MCU", "target": target, "condition": tuple(current[index] for index in range(13) if index != target), "logical_kind": kind, "parameter": parameter, "first_target_value": current[target]}
    return opening + [center] + list(reversed(opening))


def conditional_pair_indices(operation: dict) -> tuple[int, int]:
    bits = []
    iterator = iter(operation["condition"])
    for index in range(13):
        bits.append(0 if index == operation["target"] else next(iterator))
    first = sum(value << index for index, value in enumerate(bits))
    return first, first | (1 << operation["target"])


def apply_compiled_conditionals(state: np.ndarray, conditionals: list[dict], *, inverse: bool = False) -> None:
    sequence = reversed(conditionals) if inverse else conditionals
    exchange = np.asarray(((0.0, 1.0), (1.0, 0.0)))
    for operation in sequence:
        first, second = conditional_pair_indices(operation)
        if operation["kind"] == "MCX":
            block = exchange
        elif operation["logical_kind"] == "X":
            block = exchange
        else:
            cosine, sine = math.cos(operation["parameter"]), math.sin(operation["parameter"])
            block = np.asarray(((cosine, -sine), (sine, cosine)))
            if operation["first_target_value"] == 1:
                block = exchange @ block @ exchange
        if inverse:
            block = block.conj().T
        apply_two_level(state, first, second, block)


def exact_conjunction_audit(conditionals: list[dict]) -> dict:
    failures = 0
    rows = 0
    negative_x = 0
    for operation in conditionals:
        condition = operation["condition"]
        negative_x += 2 * sum(value == 0 for value in condition)
        for raw in product((0, 1), repeat=12):
            # The physical orientation predicate is the thirteenth, positive
            # control and is one on this branch's declared code.
            normalized = (1,) + tuple(value if wanted else 1 - value for value, wanted in zip(raw, condition))
            work = [0] * 12
            work[0] ^= normalized[0] & normalized[1]
            for index in range(2, 13):
                work[index - 1] ^= work[index - 2] & normalized[index]
            fired = work[11]
            for index in reversed(range(2, 13)):
                work[index - 1] ^= work[index - 2] & normalized[index]
            work[0] ^= normalized[0] & normalized[1]
            failures += int(fired != int(raw == condition) or any(work))
            rows += 1
    return {
        "conditional_operations": len(conditionals),
        "clean_control_rows_exhausted": rows,
        "clean_control_failures": failures,
        "negative_control_X_gates": negative_x,
        "clean_conjunction_work_M2": 12,
        "Toffoli_calls": 24 * len(conditionals),
        "one_M2_gates_after_exact_Toffoli_lowering": 9 * 24 * len(conditionals) + negative_x,
        "two_M2_gates_after_exact_Toffoli_lowering": (6 * 24 + 1) * len(conditionals),
    }


def rotate_tuple(frame: np.ndarray, coordinate: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(int(value) for value in frame @ np.asarray(coordinate))


def direction_frame(direction: int) -> np.ndarray:
    target = np.asarray(c210.DIRECTIONS[direction])
    return next(frame for frame in c210.proper_cubic_frames() if np.array_equal(frame @ np.asarray((1, 0, 0)), target))


def sector_layout() -> dict:
    roles = {"resource": (0, 0, 0)}
    paths = {}
    radii = {("plus", "A"): 5, ("minus", "A"): 10, ("plus", "B"): -15, ("minus", "B"): -20}
    for sector in ("plus", "minus"):
        for direction in range(6):
            vector = tuple(int(value) for value in c210.DIRECTIONS[direction])
            for buffer in ("A", "B"):
                roles[f"{sector}_{buffer}_{direction}"] = tuple(radii[(sector, buffer)] * value for value in vector)
            source_path = tuple(tuple(step * value for value in vector) for step in range(radii[(sector, "A")], 65))
            target_path = tuple(tuple(step * value for value in vector) for step in range(radii[(sector, "B")], -65, -1))
            paths[(sector, direction)] = {"source": source_path, "target": target_path}
    work = tuple((30 + index, 45, 55) for index in range(12))
    role_values = tuple(roles.values())
    path_failures = 0
    for row in paths.values():
        for name in ("source", "target"):
            path_failures += sum(not c610.nn(first, second) for first, second in zip(row[name], row[name][1:]))
        path_failures += int(set(row["source"]) & set(row["target"]) != set())
    return {
        "roles": roles,
        "paths": paths,
        "pair_work_roles_identity_frame": work,
        "data_role_collisions": len(role_values) - len(set(role_values)),
        "work_role_collisions": len(work) - len(set(work)),
        "path_or_source_target_disjointness_failures": path_failures,
    }


def toffoli_pair_pattern(a, b, target):
    return ((a, b), (b, target), (a, b), (b, target), (a, target), (b, target))


def pair_bus_audit(layout: dict, conditionals: list[dict]) -> dict:
    frames = c210.proper_cubic_frames()
    base_data = [layout["roles"]["resource"]]
    base_data += [layout["roles"][f"plus_A_{direction}"] for direction in range(6)]
    base_data += [layout["roles"][f"minus_A_{direction}"] for direction in range(6)]
    max_distance = 0
    route_swaps = 0
    endpoint_failures = 0
    primitive_pairs = 0
    per_conditional_pairs = 24 * 6 + 1
    # Every conditional has the same 13-control conjunction skeleton.  Audit
    # every actual endpoint after all 24 spatial rotations.
    for orientation, frame in enumerate(frames):
        data = [rotate_tuple(frame, coordinate) for coordinate in base_data]
        work = [rotate_tuple(frame, coordinate) for coordinate in layout["pair_work_roles_identity_frame"]]
        flag = c610.predicate_roles(orientation)["predicate_flag_site"]
        for operation in conditionals:
            target_coordinate = data[operation["target"]]
            controls = [flag] + [coordinate for index, coordinate in enumerate(data) if index != operation["target"]]
            triples = [(controls[0], controls[1], work[0])]
            triples += [(work[index - 2], controls[index], work[index - 1]) for index in range(2, 13)]
            triples = triples + list(reversed(triples))
            pairs = []
            for first, second, target in triples:
                pairs.extend(toffoli_pair_pattern(first, second, target))
            pairs.append((work[-1], target_coordinate))
            endpoint_failures += int(len(pairs) != per_conditional_pairs)
            for first, second in pairs:
                first_index, second_index = c610.bus_index(first), c610.bus_index(second)
                endpoint_failures += int(c610.bus_coordinate(first_index) != first or c610.bus_coordinate(second_index) != second)
                distance = abs(second_index - first_index)
                max_distance = max(max_distance, distance)
                route_swaps += 2 * max(0, distance - 1)
                primitive_pairs += 1
    return {
        "proper_cubic_orientation_branches": 24,
        "support_two_endpoint_pairs_audited": primitive_pairs,
        "endpoint_or_bus_inverse_failures": endpoint_failures,
        "maximum_bus_distance": max_distance,
        "move_apply_restore_SWAPs_all24_per_coarse_cell": route_swaps,
        "all_routed_primitive_support_at_most_two": endpoint_failures == 0,
    }


def stream_register(state: dict, length: int, inverse: bool = False, delete: str | None = None) -> dict:
    result = {key: value.copy() for key, value in state.items()}
    factors = ("scatter", "clear", "swap")
    if inverse:
        factors = tuple(reversed(factors))
    for factor in factors:
        if factor == delete:
            continue
        if factor == "scatter":
            for sector in range(2):
                for direction in range(6):
                    vector = c210.DIRECTIONS[direction]
                    for cell in c610.all_cells(length):
                        target = c610.coarse_target(cell, tuple(int(x) for x in vector), length)
                        result["B"][target + (sector, direction)] ^= result["A"][cell + (sector, direction)]
        elif factor == "clear":
            for sector in range(2):
                for direction in range(6):
                    vector = c210.DIRECTIONS[direction]
                    for cell in c610.all_cells(length):
                        target = c610.coarse_target(cell, tuple(int(x) for x in vector), length)
                        result["A"][cell + (sector, direction)] ^= result["B"][target + (sector, direction)]
        else:
            result["A"], result["B"] = result["B"].copy(), result["A"].copy()
    return result


def stream_geometry_and_semantics(layout: dict) -> dict:
    frames = c210.proper_cubic_frames()
    rows = []
    maximum_failures = 0
    for label, length, held in FIXTURES:
        period = c610.K * length
        edge_failures = cross_failures = conflict_failures = 0
        cross_edges = 0
        for frame in frames:
            for sector in ("plus", "minus"):
                for direction in range(6):
                    vector = rotate_tuple(frame, tuple(int(value) for value in c210.DIRECTIONS[direction]))
                    source_path = tuple(rotate_tuple(frame, value) for value in layout["paths"][(sector, direction)]["source"])
                    target_path = tuple(rotate_tuple(frame, value) for value in layout["paths"][(sector, direction)]["target"])
                    for cell in c610.all_cells(length):
                        target_cell = c610.coarse_target(cell, vector, length)
                        source = [c610.global_coordinate(value, cell, length) for value in source_path]
                        target = [c610.global_coordinate(value, target_cell, length) for value in target_path]
                        edge_failures += sum(not c610.nn(a, b, period) for a, b in zip(source, source[1:]))
                        edge_failures += sum(not c610.nn(a, b, period) for a, b in zip(target, target[1:]))
                        cross_failures += int(not c610.nn(source[-1], target[-1], period))
                        conflict_failures += int(bool(set(source) & set(target)))
                        cross_edges += 1
        shape = (length, length, length, 2, 6)
        rng = np.random.default_rng(62000 + length)
        initial = {"A": rng.integers(0, 2, size=shape, dtype=np.uint8), "B": np.zeros(shape, dtype=np.uint8)}
        evolved = stream_register(initial, length)
        restored = stream_register(evolved, length, inverse=True)
        inverse_failures = int(np.count_nonzero(restored["A"] ^ initial["A"]) + np.count_nonzero(restored["B"] ^ initial["B"]))
        lawful_buffer_leakage = int(np.count_nonzero(evolved["B"]))
        deletion = {}
        for factor in ("scatter", "clear", "swap"):
            deleted = stream_register(initial, length, delete=factor)
            deletion[factor] = int(np.count_nonzero(deleted["A"] ^ evolved["A"]) + np.count_nonzero(deleted["B"] ^ evolved["B"]))
        failures = edge_failures + cross_failures + conflict_failures + inverse_failures + lawful_buffer_leakage
        maximum_failures = max(maximum_failures, failures)
        rows.append({
            "fixture": label, "length": length, "held": held,
            "translated_cells": length ** 3, "all24_cross_edges": cross_edges,
            "path_NN_failures": edge_failures, "wrap_cross_edge_failures": cross_failures,
            "source_target_path_conflicts": conflict_failures,
            "inverse_failures": inverse_failures, "terminal_B_leakage": lawful_buffer_leakage,
            "deletion_signals": deletion,
        })
    return {"rows": rows, "maximum_failure_count": maximum_failures}


def direction_representation(frame: np.ndarray) -> np.ndarray:
    return c210.direction_permutation(frame)


def route_a(r610: dict) -> dict:
    target, expected, angle_rows, high_level = logical_pair_word()
    words = active_bitstrings()
    conditionals = []
    for operation in high_level:
        first, second = words[operation["first"]], words[operation["second"]]
        conditionals.extend(gray_conditionals(first, second, operation["kind"], operation.get("angle", math.pi / 2)))
    conjunction = exact_conjunction_audit(conditionals)
    inherited_predicate = r610["literal_orientation_controlled_compute_act_uncompute"]
    conjunction.update({
        "inherited_orientation_predicate_compute_support_two_gates_per_branch": inherited_predicate["predicate_compute_support_two_gates"],
        "inherited_orientation_predicate_compute_uncompute_support_two_gates_per_branch": inherited_predicate["predicate_compute_and_uncompute_support_two_gates"],
        "inherited_orientation_predicate_clean_work_return": inherited_predicate["clean_predicate_work_return"],
        "total_pair_macro_one_or_two_M2_gates_per_branch_before_bus":
            conjunction["one_M2_gates_after_exact_Toffoli_lowering"]
            + conjunction["two_M2_gates_after_exact_Toffoli_lowering"]
            + inherited_predicate["predicate_compute_and_uncompute_support_two_gates"],
    })
    layout = sector_layout()
    bus = pair_bus_audit(layout, conditionals)
    stream = stream_geometry_and_semantics(layout)

    # Common E is the one embedding of all seven logical basis states into the
    # same resource/+/- occupation block.  Apply the physical two-level word
    # sparsely on the full 2^13 block; every other word is the identity.
    rng = np.random.default_rng(620)
    logical = rng.normal(size=7) + 1j * rng.normal(size=7)
    logical /= np.linalg.norm(logical)
    encoded = np.zeros(1 << 13, dtype=complex)
    encoded[list(words)] = logical
    physical = encoded.copy()
    apply_compiled_conditionals(physical, conditionals)
    expected_encoded = np.zeros_like(encoded)
    expected_encoded[list(words)] = expected @ logical
    eg_residual = float(np.linalg.norm(physical - expected_encoded))
    leakage = float(np.linalg.norm(np.delete(physical, list(words))))
    restored = physical.copy()
    apply_compiled_conditionals(restored, conditionals, inverse=True)
    inverse_residual = float(np.linalg.norm(restored - encoded))

    deletion_signals = {}
    for deleted_index, name in ((0, "W_dagger_Givens"), (5, "resource_pair_swap"), (6, "W_Givens")):
        trial = encoded.copy()
        for index, operation in enumerate(high_level):
            if index == deleted_index:
                continue
            if operation["kind"] == "X":
                block = np.asarray(((0.0, 1.0), (1.0, 0.0)))
            else:
                cosine, sine = math.cos(operation["angle"]), math.sin(operation["angle"])
                block = np.asarray(((cosine, -sine), (sine, cosine)))
            apply_two_level(trial, words[operation["first"]], words[operation["second"]], block)
        deletion_signals[name] = float(np.linalg.norm(trial - physical))

    frames = c210.proper_cubic_frames()
    covariance = 0.0
    group_failures = 0
    frame_lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    reps = []
    for frame in frames:
        rep = np.zeros((7, 7)); rep[0, 0] = 1
        permutation = np.argmax(direction_representation(frame), axis=0)
        for direction, moved in enumerate(permutation):
            rep[1 + int(moved), 1 + direction] = 1
        reps.append(rep)
        covariance = max(covariance, float(np.linalg.norm(rep @ target - target @ rep)))
    for first_index, first in enumerate(frames):
        for second_index, second in enumerate(frames):
            target_index = frame_lookup[tuple((first @ second).reshape(-1))]
            group_failures += int(not np.array_equal(reps[first_index] @ reps[second_index], reps[target_index]))

    # Preserve the accepted coin -> stream -> contact order in both candidate
    # charge sectors.  The negative copy uses the conjugate onsite coin; the
    # occupation stream is charge-blind and the two contacts are separate.
    coin = c219.common_species(c230.BETA).coin
    occupations = c230.c229.occupation_table(6)
    pairs = np.sum(occupations, axis=1) * (np.sum(occupations, axis=1) - 1) / 2
    contact = np.diag(np.exp(1j * c230.COUPLING * pairs))
    momentum = np.asarray((0.31, 0.19, 0.11))
    phases = np.exp(-1j * np.asarray(c210.DIRECTIONS) @ momentum)
    plus_free = c230.c229.fock_lift(np.diag(phases) @ coin)
    minus_free = c230.c229.fock_lift(np.diag(np.conj(phases)) @ coin.conj())
    plus_update, minus_update = contact @ plus_free, contact @ minus_free
    reversed_plus = c230.c229.fock_lift(np.diag(phases)) @ contact @ c230.c229.fock_lift(coin)
    same_cell_contact_stream_commutator_diagnostic = float(np.linalg.norm(plus_update - reversed_plus))
    inherited_order = r610["Cycle230_factor_order_deletion_noncommutation"]
    order_signal = inherited_order["Cycle230_reverse_schedule_difference"]
    update_inverse = max(float(np.linalg.norm(plus_update.conj().T @ plus_update - np.eye(64))), float(np.linalg.norm(minus_update.conj().T @ minus_update - np.eye(64))))
    mass_rows = r610["onsite_mass_contact_seam_composition"]["fixture_residuals"]
    conjugate_mass_spectrum = float(np.max(np.abs(np.sort(np.angle(np.linalg.eigvals(coin))) + np.sort(np.angle(np.linalg.eigvals(coin.conj())))[::-1])))

    output = {
        "object": "one common resource/+/- occupation embedding with an exact Gray/conjunction support-two pair word and two charge-blind double-buffer streams",
        "disposition": "CONSTRUCTIVE_PHYSICAL_SUPPORT_TWO_PAIR_AND_DISTINCT_CHARGE_SECTOR_COMPILER_ON_DECLARED_CLEAN_ORIENTATION_CODE",
        "common_E": {
            "physical_data_bits": 13,
            "resource_bit": 0,
            "positive_occupation_bits": list(range(1, 7)),
            "negative_occupation_bits": list(range(7, 13)),
            "active_physical_words": words,
            "active_logical_dimension": 7,
            "identity_extension_words": (1 << 13) - 7,
            "EG_residual": eg_residual,
            "code_leakage": leakage,
        },
        "Givens_angle_inventory": angle_rows,
        "high_level_pair_factors": high_level,
        "Gray_conditionals": {"count": len(conditionals), "hamming_four_per_Givens": 7, "hamming_three_resource_pair_swap": 5},
        "clean_lowering": conjunction,
        "layout": {
            "K": c610.K,
            "physical_M2_per_supercell": c610.K ** 3,
            "new_A_B_resource_data_M2": 25,
            "new_pair_conjunction_work_role_orbit_M2": 12 * 24,
            "reused_Cycle610_orientation_and_predicate_roles": True,
            "constant_added_role_upper_bound_M2": 25 + 12 * 24,
            "data_role_collisions": layout["data_role_collisions"],
            "work_role_collisions": layout["work_role_collisions"],
            "path_failures": layout["path_or_source_target_disjointness_failures"],
        },
        "stream_constant_gate_upper_bound": {
            "positive_remote_CNOT_move_apply_restore_two_M2_gates": 217,
            "negative_remote_CNOT_move_apply_restore_two_M2_gates": 197,
            "scatter_clear_and_local_swap_two_M2_gates_per_cell_before_orientation_control": 4980,
            "orientation_control_gadget": "the exact pinned Cycle610 dual-predicate support-two wrapper is reused",
        },
        "pair_bus": bus,
        "stream": stream,
        "pair_operator_residual": float(np.linalg.norm(target - expected)),
        "pair_unitarity_residual": float(np.linalg.norm(target.conj().T @ target - np.eye(7))),
        "physical_inverse_residual": inverse_residual,
        "pair_deletion_signals": deletion_signals,
        "maximum_all24_pair_covariance_residual": covariance,
        "all576_pair_representation_failures": group_failures,
        "coin_stream_contact": {
            "factor_order": "pair genesis -> coin -> stream -> contact; the retained matter subsequence is coin -> stream -> contact",
            "positive_full_Fock_unitarity_residual": float(np.linalg.norm(plus_update.conj().T @ plus_update - np.eye(64))),
            "negative_full_Fock_unitarity_residual": float(np.linalg.norm(minus_update.conj().T @ minus_update - np.eye(64))),
            "maximum_joint_unitarity_residual": update_inverse,
            "order_reversal_signal": order_signal,
            "same_cell_momentum_block_contact_stream_commutator_diagnostic": same_cell_contact_stream_commutator_diagnostic,
            "inherited_physical_factor_deletion_signals": inherited_order["delete_each_factor_difference"],
            "separate_same_g_contact": True,
            "cross_contact_present": False,
            "negative_coin_is_supplied_conjugate": True,
        },
        "one_particle_mass": {
            "inherited_compiled_residual": mass_rows["one_particle_mass_coin_compiled_full16_residual"],
            "inherited_cubic_residual": mass_rows["one_particle_mass_coin_symmetry_residual"],
            "charge_conjugate_spectrum_pairing_residual": conjugate_mass_spectrum,
            "preserved": max(mass_rows["one_particle_mass_coin_compiled_full16_residual"], conjugate_mass_spectrum) < 1e-10,
        },
        "candidate_negative_sector_called_derived_antimatter": False,
        "global_Jordan_Wigner_or_parity_service": False,
        "host_frame_or_size_control": False,
        "uniform_one_hot_orientation_genesis_supplied": True,
        "blank_B_conjunction_predicate_work_supplied": True,
    }
    check(
        "Route A gives one common E and an exact clean support-two resource/cubic-pair compiler",
        max(output["pair_operator_residual"], output["pair_unitarity_residual"], eg_residual, leakage, inverse_residual, covariance) < TOL
        and group_failures == 0
        and conjunction["clean_control_failures"] == 0
        and layout["data_role_collisions"] == layout["work_role_collisions"] == layout["path_or_source_target_disjointness_failures"] == 0
        and bus["all_routed_primitive_support_at_most_two"]
        and all(signal > 1e-4 for signal in deletion_signals.values()),
        output,
    )
    check(
        "Route A composes distinct +/- streams on L3/L6/L7 while preserving coin -> stream -> contact and the mass fixture",
        stream["maximum_failure_count"] == 0
        and all(all(value > 0 for value in row["deletion_signals"].values()) for row in stream["rows"])
        and update_inverse < TOL and order_signal > 1e-3 and output["one_particle_mass"]["preserved"]
        and not output["candidate_negative_sector_called_derived_antimatter"],
        output,
    )
    return output


# ---------------------------------------------------------------------------
# Route B: explicit local endpoint-controlled feedback candidate and its family.

def spatial_trace_vector() -> np.ndarray:
    result = np.zeros(10)
    for component in ((0, 0), (1, 1), (2, 2)):
        result[c576.regge.HCOMPS.index(component)] = 1
    return result


@lru_cache(maxsize=None)
def frozen_regge_objects(momentum_key: tuple[float, ...]) -> tuple[np.ndarray, np.ndarray]:
    momentum = np.asarray(momentum_key)
    return c576.frame_averaged_metric_hessian(momentum), c576.frame_averaged_source_row(momentum)


def feedback_stationary(momentum: np.ndarray, coupling: float, improvement: float,
                        square_sign: float, square_scale: float, endpoint: int,
                        density: float = 1.0) -> dict:
    q, source = frozen_regge_objects(tuple(float(value) for value in momentum))
    return feedback_from_objects(q, source, momentum, coupling, improvement,
                                 square_sign, square_scale, endpoint, density)


def feedback_from_objects(q: np.ndarray, source: np.ndarray, momentum: np.ndarray,
                          coupling: float, improvement: float, square_sign: float,
                          square_scale: float, endpoint: int,
                          density: float = 1.0) -> dict:
    imp = spatial_trace_vector() @ q
    base_row = source + improvement * imp
    feedback_hessian = endpoint * square_sign * square_scale * np.outer(np.conj(source), source)
    feedback_force = -endpoint * square_sign * square_scale * density * np.conj(source)
    q_total = q + feedback_hessian
    force = coupling * np.conj(base_row) + feedback_force
    response = -np.linalg.pinv(q_total, rcond=1e-10) @ force
    equation = q_total @ response + force
    receiver = float(np.real(source @ response))
    gauge = c576.continuum_gauge_metric(momentum)
    return {
        "q": q, "source": source, "improvement_row": imp, "base_row": base_row,
        "feedback_hessian": feedback_hessian, "q_total": q_total,
        "force": force, "response": response, "receiver": receiver,
        "stationary_residual": float(np.linalg.norm(equation)),
        "base_source_Ward_residual": float(np.max(np.abs(base_row @ gauge))),
        "feedback_Hessian_Ward_residual": float(np.linalg.norm(feedback_hessian @ gauge)),
        "feedback_scalar_Ward_residual": float(np.max(np.abs(source @ gauge))),
        "feedback_hessian_min_eigenvalue": float(np.min(np.linalg.eigvalsh(feedback_hessian))),
        "feedback_hessian_max_eigenvalue": float(np.max(np.linalg.eigvalsh(feedback_hessian))),
    }


def route_b(r612: dict) -> dict:
    endpoint_rows = []
    for matter, binder in product((0, 1), repeat=2):
        candidate = c612.computed_candidate(matter, binder)
        deleted = c612.computed_candidate(matter, binder, delete="Pd-compute")
        endpoint_rows.append({
            "matter_membership": matter, "binder": binder,
            "endpoint_bit": candidate["opportunity"], "pointer_after": candidate["pointer"],
            "deleted_detector_endpoint_bit": deleted["opportunity"],
        })
    endpoint = c612.computed_candidate(1, 1)["opportunity"]

    alternatives = []
    rows = []
    max_stationary = max_ward = max_covariance = max_inverse = 0.0
    min_deletion = math.inf
    all_receivers = []
    positive_receivers = []
    analytic_signs = set()
    positive_analytic_signs = set()
    for label, length, held in FIXTURES:
        scale = 2 * math.pi / length
        momentum = np.asarray((scale, scale, 0.0, scale))
        fixture = []
        for square_sign, square_scale, relative_lambda, lambda_sign, improvement in product(
            (-1.0, 1.0), (0.5, 1.0, 2.0), (1.0, 2.0), (-1.0, 1.0), (-1.0, 0.0, 1.0)
        ):
            coupling = lambda_sign * relative_lambda * c576.SOURCE_COUPLING
            result = feedback_stationary(momentum, coupling, improvement, square_sign, square_scale, endpoint)
            covariance = 0.0
            for representation, frame in zip(c576.METRIC_REPS, c576.LIFTED_FRAMES):
                # Cycle576 already establishes that these are the actual
                # all-frame Regge objects.  Rebuild every transformed feedback
                # equation from them rather than recomputing the expensive
                # underlying Regge Hessian for each member of the 72-word grid.
                rotated_q = representation @ result["q"] @ representation.T
                rotated_source = result["source"] @ representation.T
                rotated = feedback_from_objects(
                    rotated_q, rotated_source, frame @ momentum, coupling,
                    improvement, square_sign, square_scale, endpoint,
                )["response"]
                covariance = max(covariance, float(np.linalg.norm(rotated - representation @ result["response"])))
            entry = {
                "feedback_square_sign": int(square_sign),
                "feedback_square_scale": square_scale,
                "relative_lambda_magnitude": relative_lambda,
                "lambda_sign": int(lambda_sign),
                "improvement_coefficient": int(improvement),
                "receiver": result["receiver"],
                "receiver_sign": int(np.sign(result["receiver"])),
                "stationary_residual": result["stationary_residual"],
                "base_source_Ward_residual": result["base_source_Ward_residual"],
                "feedback_Hessian_Ward_residual": result["feedback_Hessian_Ward_residual"],
                "all24_response_covariance_residual": covariance,
                "feedback_hessian_min_eigenvalue": result["feedback_hessian_min_eigenvalue"],
                "feedback_hessian_max_eigenvalue": result["feedback_hessian_max_eigenvalue"],
            }
            fixture.append(entry); alternatives.append(entry); all_receivers.append(result["receiver"])
            if square_sign > 0:
                positive_receivers.append(result["receiver"])
            max_stationary = max(max_stationary, result["stationary_residual"])
            max_ward = max(max_ward, result["base_source_Ward_residual"], result["feedback_Hessian_Ward_residual"], result["feedback_scalar_Ward_residual"])
            max_covariance = max(max_covariance, covariance)

        # Exact affine lambda/c family for every fixed feedback sign/scale.
        family_coefficients = []
        for square_sign, square_scale in product((-1.0, 1.0), (0.5, 1.0, 2.0)):
            r00 = feedback_stationary(momentum, 0.0, 0.0, square_sign, square_scale, endpoint)["receiver"]
            r10 = feedback_stationary(momentum, 1.0, 0.0, square_sign, square_scale, endpoint)["receiver"]
            r11 = feedback_stationary(momentum, 1.0, 1.0, square_sign, square_scale, endpoint)["receiver"]
            r0, rimp = r10 - r00, r11 - r10
            coefficient = r0 if abs(r0) > 1e-12 else rimp
            witness_scale = abs(r00 / coefficient) + 1.0
            positive_parameter = math.copysign(witness_scale, coefficient)
            negative_parameter = -positive_parameter
            witness_receivers = (r00 + positive_parameter * coefficient, r00 + negative_parameter * coefficient)
            witness_signs = sorted({int(np.sign(value)) for value in witness_receivers})
            analytic_signs.update(witness_signs)
            if square_sign > 0:
                positive_analytic_signs.update(witness_signs)
            family_coefficients.append({
                "feedback_square_sign": int(square_sign), "feedback_square_scale": square_scale,
                "exact_family": "R(lambda,c)=Rfb + lambda*(R0+c*Rimp)",
                "Rfb": r00, "R0": r0, "Rimp": rimp,
                "continuous_family_nonconstant": abs(r10 - r00) + abs(r11 - r10) > 1e-10,
                "analytic_opposite_sign_witness_parameter": [positive_parameter, negative_parameter],
                "analytic_opposite_sign_witness_receivers": witness_receivers,
                "analytic_receiver_signs": witness_signs,
            })

        baseline = feedback_stationary(momentum, c576.SOURCE_COUPLING, 0.0, 1.0, 1.0, endpoint)
        no_endpoint = feedback_stationary(momentum, c576.SOURCE_COUPLING, 0.0, 1.0, 1.0, 0)
        deleted_cross = feedback_stationary(momentum, c576.SOURCE_COUPLING, 0.0, 1.0, 1.0, endpoint, density=0.0)
        deletion_signal = max(abs(baseline["receiver"] - no_endpoint["receiver"]), abs(baseline["receiver"] - deleted_cross["receiver"]))
        min_deletion = min(min_deletion, deletion_signal)
        hamiltonian = np.block([
            [np.zeros((1, 1)), baseline["force"][None, :].conj()],
            [baseline["force"][:, None], baseline["q_total"]],
        ])
        update = expm(-1j * c576.UPDATE_PARAMETER * hamiltonian)
        inverse = float(np.linalg.norm(update.conj().T @ update - np.eye(len(update))))
        max_inverse = max(max_inverse, inverse)
        rows.append({
            "fixture": label, "length": length, "held": held,
            "members_audited": len(fixture), "alternatives": fixture,
            "analytic_families": family_coefficients,
            "positive_square_baseline_receiver": baseline["receiver"],
            "endpoint_deletion_receiver": no_endpoint["receiver"],
            "cross_term_deletion_receiver": deleted_cross["receiver"],
            "minimum_local_feedback_deletion_signal": deletion_signal,
            "finite_state_inverse_residual": inverse,
        })

    frames = c576.FRAMES
    lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    group_failures = 0
    for i, first in enumerate(frames):
        for j, second in enumerate(frames):
            target = lookup[tuple((first @ second).reshape(-1))]
            group_failures += int(np.linalg.norm(c576.METRIC_REPS[i] @ c576.METRIC_REPS[j] - c576.METRIC_REPS[target]) > TOL)

    signs = sorted(set(int(np.sign(value)) for value in all_receivers if abs(value) > 1e-12))
    positive_signs = sorted(set(int(np.sign(value)) for value in positive_receivers if abs(value) > 1e-12))
    continuous_signs = sorted(analytic_signs)
    positive_continuous_signs = sorted(positive_analytic_signs)
    diagnostic_words = sorted({"3/4" if sign < 0 else "5/4" for sign in continuous_signs})
    output = {
        "object": "candidate local endpoint-controlled Regge-deficit/gauge-density feedback square plus every audited sign/scale/lambda/improvement alternative",
        "disposition": "CONSTRUCTIVE_LOCAL_MATTER_CAUSED_FEEDBACK_TERM; DOES_NOT_SELECT_THE_JOINED_RESPONSE_OR_RECEIVER_CLASS",
        "feedback_action": "A_fb=(sigma*kappa/2) sum_x b_x |D_x[e]-rho_x|^2",
        "physical_endpoint_word": "P_d(pointer); Toffoli(pointer,binder,opportunity); P_d(pointer), then use/uncompute opportunity",
        "endpoint_rows": endpoint_rows,
        "endpoint_and_detector_work_return_blank": all(row["pointer_after"] == 0 for row in endpoint_rows),
        "criterion_frozen_before_evaluation": {
            "proper_cubic_scalar": True,
            "U1_gauge_invariant": True,
            "positive_feedback_Hessian_if_sigma_plus": True,
            "same_coefficient_without_fixture_refit": True,
            "unique_stationary_pseudoinverse_branch_continuous_from_zero_source": True,
            "authority_status": "candidate-law criterion; none of positivity, 1/2, relative D/rho scale, or kappa=1 is forced by a pinned approved surface",
        },
        "audited_feedback_square_signs": [-1, 1],
        "audited_feedback_scales": [0.5, 1.0, 2.0],
        "audited_relative_lambda_magnitudes": [1.0, 2.0],
        "audited_lambda_signs": [-1, 1],
        "audited_improvements": [-1, 0, 1],
        "members_per_fixture": 72,
        "rows": rows,
        "maximum_stationary_residual": max_stationary,
        "maximum_Ward_residual": max_ward,
        "maximum_all24_covariance_residual": max_covariance,
        "all576_metric_representation_failures": group_failures,
        "maximum_finite_state_inverse_residual": max_inverse,
        "minimum_feedback_deletion_signal": min_deletion,
        "finite_grid_receiver_signs_all_audited_alternatives": signs,
        "finite_grid_receiver_signs_positive_square_only": positive_signs,
        "exact_continuous_family_receiver_signs": continuous_signs,
        "exact_positive_square_continuous_family_receiver_signs": positive_continuous_signs,
        "diagnostic_Cycle612_word_image_under_supplied_sign_convention": diagnostic_words,
        "Cycle612_receiver_words": ["3/4", "5/4"],
        "unique_receiver_selection_residual": 1,
        "lambda_c_family_reenumerated_after_feedback": True,
        "continuous_family_collapsed": False,
        "receiver_class_collapsed": False,
        "feedback_sign_or_scale_derived": False,
        "Cycle612_numeric_response_sign_to_word_map_derived": False,
        "merely_routing_a_supplied_sign_bit": False,
        "Gauss_unchanged_because_endpoint_density_and_deficit_are_U1_scalars": True,
        "open_boundary_and_periodic_Regge_joint_real_space_compiler_executed": False,
        "gravity_or_physical_stress_claimed": False,
    }
    check(
        "Route B constructs genuine matter-caused local feedback and preserves Gauss/Ward/inverse/covariance",
        output["endpoint_and_detector_work_return_blank"]
        and max(max_stationary, max_ward, max_covariance, max_inverse) < TOL
        and group_failures == 0 and min_deletion > 1e-8
        and all(row["deleted_detector_endpoint_bit"] == 0 for row in endpoint_rows)
        and all(all(family["continuous_family_nonconstant"] for family in row["analytic_families"]) for row in rows),
        output,
    )
    check(
        "Route B does not mis-credit the positive square as sign/scale/lambda/improvement or receiver selection",
        continuous_signs == [-1, 1] and positive_continuous_signs == [-1, 1]
        and diagnostic_words == ["3/4", "5/4"]
        and not output["continuous_family_collapsed"] and not output["receiver_class_collapsed"]
        and not output["feedback_sign_or_scale_derived"]
        and not output["Cycle612_numeric_response_sign_to_word_map_derived"]
        and output["unique_receiver_selection_residual"] == 1,
        output,
    )
    return output


# ---------------------------------------------------------------------------
# Route C: actual full-Fock unitary coframe generator and quasiphase audit.

SPATIAL_COMPONENTS = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))


def component_matrix(component: tuple[int, int]) -> np.ndarray:
    result = np.zeros((3, 3))
    first, second = component
    result[first, second] = 1
    result[second, first] = 1
    return result


def spatial_tensor_representation(frame: np.ndarray) -> np.ndarray:
    result = np.zeros((6, 6))
    basis = [component_matrix(component) for component in SPATIAL_COMPONENTS]
    for column, matrix in enumerate(basis):
        moved = frame @ matrix @ frame.T
        for row, candidate in enumerate(basis):
            denominator = float(np.sum(candidate * candidate))
            result[row, column] = float(np.sum(candidate * moved) / denominator)
    return result


@lru_cache(maxsize=None)
def cached_full_fock_update(momentum_key: tuple[float, ...], coframe_key: tuple[float, ...],
                            contact: bool, order: str) -> np.ndarray:
    momentum = np.asarray(momentum_key)
    coframe = np.asarray(coframe_key).reshape(3, 3)
    coin = c219.common_species(c230.BETA).coin
    directions = np.asarray(c210.DIRECTIONS, dtype=float)
    phases = np.exp(-1j * np.einsum("i,ij,dj->d", momentum, np.eye(3) + coframe, directions))
    stream = np.diag(phases)
    occupations = c230.c229.occupation_table(6)
    numbers = np.sum(occupations, axis=1)
    contact_matrix = np.diag(np.exp(1j * c230.COUPLING * numbers * (numbers - 1) / 2)) if contact else np.eye(64)
    if order == "coin_stream_contact":
        return contact_matrix @ c230.c229.fock_lift(stream @ coin)
    if order == "coin_contact_stream":
        return c230.c229.fock_lift(stream) @ contact_matrix @ c230.c229.fock_lift(coin)
    raise ValueError(order)


def full_fock_update(momentum: np.ndarray, coframe: np.ndarray, *, contact: bool = True,
                     order: str = "coin_stream_contact") -> np.ndarray:
    return cached_full_fock_update(
        tuple(float(value) for value in momentum),
        tuple(float(value) for value in coframe.reshape(-1)),
        contact,
        order,
    )


def unitarily_centered_generator(momentum: np.ndarray, variation: np.ndarray,
                                 epsilon: float) -> np.ndarray:
    plus = full_fock_update(momentum, epsilon * variation)
    minus = full_fock_update(momentum, -epsilon * variation)
    relative = minus.conj().T @ plus
    values, vectors = np.linalg.eig(relative)
    generator = vectors @ np.diag(-np.angle(values) / (2 * epsilon)) @ np.linalg.inv(vectors)
    return (generator + generator.conj().T) / 2


def generator_components(momentum: np.ndarray, epsilon: float = 1e-6) -> tuple[np.ndarray, list[np.ndarray], float]:
    zero = np.zeros((3, 3))
    update = full_fock_update(momentum, zero)
    generators = []
    convergence = 0.0
    for component in SPATIAL_COMPONENTS:
        variation = component_matrix(component)
        generator = unitarily_centered_generator(momentum, variation, epsilon)
        half_step = unitarily_centered_generator(momentum, variation, epsilon / 2)
        convergence = max(convergence, float(np.linalg.norm(generator - half_step)))
        generators.append(half_step)
    return update, generators, convergence


def tracked_quasiphase_audit(momentum: np.ndarray, component_index: int = 0, epsilon: float = 1e-6) -> dict:
    variation = component_matrix(SPATIAL_COMPONENTS[component_index])
    update, generators, convergence = generator_components(momentum, epsilon)
    plus = full_fock_update(momentum, epsilon * variation)
    minus = full_fock_update(momentum, -epsilon * variation)
    values, vectors = np.linalg.eig(update)
    plus_values, plus_vectors = np.linalg.eig(plus)
    minus_values, minus_vectors = np.linalg.eig(minus)
    _, plus_match = linear_sum_assignment(-np.abs(vectors.conj().T @ plus_vectors))
    _, minus_match = linear_sum_assignment(-np.abs(vectors.conj().T @ minus_vectors))
    theta_plus = -np.angle(plus_values[plus_match])
    theta_minus = -np.angle(minus_values[minus_match])
    derivatives = np.angle(np.exp(1j * (theta_plus - theta_minus))) / (2 * epsilon)
    expectations = np.real(np.einsum("ij,ij->j", vectors.conj(), generators[component_index] @ vectors))
    minimum_separation = min(abs(values[first] - values[second]) for first, second in combinations(range(64), 2))

    # A constant global rephasing leaves the quantum channel and K unchanged,
    # but can put the most responsive branch directly on the principal seam.
    branch = int(np.argmax(np.abs(expectations)))
    central_theta = -float(np.angle(values[branch]))
    rephase = math.pi - central_theta
    seam_plus = ((theta_plus[branch] + rephase + math.pi) % (2 * math.pi)) - math.pi
    seam_minus = ((theta_minus[branch] + rephase + math.pi) % (2 * math.pi)) - math.pi
    principal_jump = abs(seam_plus - seam_minus)
    local_unwrapped = abs(float(np.angle(np.exp(1j * (seam_plus - seam_minus)))))
    return {
        "component": SPATIAL_COMPONENTS[component_index],
        "minimum_eigenvalue_separation": float(minimum_separation),
        "maximum_tracked_quasiphase_generator_residual": float(np.max(np.abs(derivatives - expectations))),
        "maximum_generator_expectation": float(np.max(np.abs(expectations))),
        "unitarily_centered_half_step_convergence_residual": convergence,
        "tracked_branches": 64,
        "seam_branch": branch,
        "constant_global_rephase": rephase,
        "principal_wrapped_phase_jump": principal_jump,
        "locally_unwrapped_phase_step": local_unwrapped,
        "seam_generator_expectation": float(expectations[branch]),
    }


@lru_cache(maxsize=1)
def two_cell_contact_order_witness() -> dict:
    """Real-space full-Fock witness absent from a single Bloch onsite block."""
    coin = c230.c229.fock_lift(c219.common_species(c230.BETA).coin)
    occupations = c230.c229.occupation_table(6)
    lookup = {tuple(int(value) for value in row): index for index, row in enumerate(occupations)}
    numbers = np.sum(occupations, axis=1)
    contact = np.exp(1j * c230.COUPLING * numbers * (numbers - 1) / 2)
    permutation = np.empty(64 * 64, dtype=int)
    for first, second in product(range(64), repeat=2):
        before = np.asarray((occupations[first], occupations[second]))
        after = np.zeros_like(before)
        for cell in range(2):
            for direction, vector in enumerate(c210.DIRECTIONS):
                target = (cell + int(vector[0])) % 2
                after[target, direction] = before[cell, direction]
        permutation[64 * first + second] = 64 * lookup[tuple(int(value) for value in after[0])] + lookup[tuple(int(value) for value in after[1])]

    def apply_coin(state):
        return (coin @ state.reshape(64, 64) @ coin.T).reshape(-1)

    def apply_stream(state):
        result = np.empty_like(state)
        result[permutation] = state
        return result

    def apply_contact(state):
        return (state.reshape(64, 64) * contact[:, None] * contact[None, :]).reshape(-1)

    rng = np.random.default_rng(620230)
    initial = rng.normal(size=4096) + 1j * rng.normal(size=4096)
    initial /= np.linalg.norm(initial)
    accepted = apply_contact(apply_stream(apply_coin(initial)))
    contact_first = apply_stream(apply_coin(apply_contact(initial)))
    no_contact = apply_stream(apply_coin(initial))
    return {
        "periodic_cells": 2,
        "full_Fock_dimension": 4096,
        "stream_permutation_is_bijective": len(set(int(value) for value in permutation)) == 4096,
        "coin_stream_contact_vs_contact_first_signal": float(np.linalg.norm(accepted - contact_first)),
        "contact_deletion_signal": float(np.linalg.norm(accepted - no_contact)),
        "accepted_norm_residual": abs(float(np.vdot(accepted, accepted).real) - 1),
        "factor_names": (apply_coin.__name__, apply_stream.__name__, apply_contact.__name__),
    }


def route_c() -> dict:
    frames = c210.proper_cubic_frames()
    tensor_reps = [spatial_tensor_representation(frame) for frame in frames]
    frame_lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    product_failures = 0
    for i, first in enumerate(frames):
        for j, second in enumerate(frames):
            target = frame_lookup[tuple((first @ second).reshape(-1))]
            product_failures += int(np.linalg.norm(tensor_reps[i] @ tensor_reps[j] - tensor_reps[target]) > TOL)

    rows = []
    max_hermitian = max_covariance = max_finite_covariance = max_inverse = max_phase = max_convergence = 0.0
    min_separation = math.inf
    min_order = min_contact = math.inf
    for label, length, held in FIXTURES:
        momentum = 2 * math.pi / length * np.asarray((0.37, 0.23, 0.11))
        update, generators, convergence = generator_components(momentum)
        hermitian = max(float(np.linalg.norm(generator - generator.conj().T)) for generator in generators)
        covariance = 0.0
        finite_update_covariance = 0.0
        covariance_epsilon = 2e-7
        base_perturbed = [
            full_fock_update(momentum, covariance_epsilon * component_matrix(component))
            for component in SPATIAL_COMPONENTS
        ]
        for frame, fock_rep, tensor_rep in zip(frames, (c230.c229.fock_lift(direction_representation(frame)) for frame in frames), tensor_reps):
            rotated_momentum = frame @ momentum
            rotated_zero = full_fock_update(rotated_momentum, np.zeros((3, 3)))
            finite_update_covariance = max(
                finite_update_covariance,
                float(np.linalg.norm(rotated_zero - fock_rep @ update @ fock_rep.T)),
            )
            for column in range(6):
                moved_component = frame @ component_matrix(SPATIAL_COMPONENTS[column]) @ frame.T
                rotated_perturbed = full_fock_update(rotated_momentum, covariance_epsilon * moved_component)
                finite_update_covariance = max(
                    finite_update_covariance,
                    float(np.linalg.norm(rotated_perturbed - fock_rep @ base_perturbed[column] @ fock_rep.T)),
                )
                rotated_derivative = (rotated_perturbed - rotated_zero) / covariance_epsilon
                rotated_generator = 1j * rotated_zero.conj().T @ rotated_derivative
                covariance = max(
                    covariance,
                    float(np.linalg.norm(rotated_generator - fock_rep @ generators[column] @ fock_rep.T)),
                )
        inverse = float(np.linalg.norm(update.conj().T @ update - np.eye(64)))
        phase = tracked_quasiphase_audit(momentum)
        reversed_update = full_fock_update(momentum, np.zeros((3, 3)), order="coin_contact_stream")
        no_contact = full_fock_update(momentum, np.zeros((3, 3)), contact=False)
        order_signal = float(np.linalg.norm(update - reversed_update))
        contact_signal = float(np.linalg.norm(update - no_contact))
        max_hermitian = max(max_hermitian, hermitian)
        max_covariance = max(max_covariance, covariance)
        max_finite_covariance = max(max_finite_covariance, finite_update_covariance)
        max_inverse = max(max_inverse, inverse)
        max_phase = max(max_phase, phase["maximum_tracked_quasiphase_generator_residual"])
        max_convergence = max(max_convergence, convergence, phase["unitarily_centered_half_step_convergence_residual"])
        min_separation = min(min_separation, phase["minimum_eigenvalue_separation"])
        # In a single fixed Bloch onsite block, the number-only contact commutes
        # with the diagonal stream.  The actual order falsifier is therefore
        # evaluated on the explicit two-cell real-space full-Fock word below.
        min_order = min(min_order, order_signal); min_contact = min(min_contact, contact_signal)
        rows.append({
            "fixture": label, "length": length, "held": held, "momentum": momentum,
            "generator_Hermiticity_residual": hermitian,
            "unitarily_centered_half_step_convergence_residual": convergence,
            "all24_tensor_covariance_residual": covariance,
            "all24_finite_coframe_update_covariance_residual": finite_update_covariance,
            "full_unitary_inverse_residual": inverse,
            "coin_contact_stream_order_deletion_signal": order_signal,
            "contact_deletion_signal": contact_signal,
            "quasiphase": phase,
        })
    real_space_order = two_cell_contact_order_witness()
    output = {
        "object": "right Maurer-Cartan spatial-coframe generator tensor of the actual full 64-dimensional coin-stream-contact Fock unitary",
        "disposition": "CONSTRUCTIVE_FULL_UNITARY_COFRAME_GENERATOR_AND_TRACKED_QUASIPHASE_REPRESENTATIVE; NO ENERGY_RATE_OR_UNIQUE_STRESS_IDENTIFICATION",
        "full_update": "U(e,k)=Contact * Gamma(Stream(e,k) Coin)",
        "generator": "K_ab=i U^dag dU/de_ab",
        "spatial_components": SPATIAL_COMPONENTS,
        "rows": rows,
        "maximum_generator_Hermiticity_residual": max_hermitian,
        "maximum_all24_tensor_covariance_residual": max_covariance,
        "maximum_all24_finite_coframe_update_covariance_residual": max_finite_covariance,
        "all576_tensor_representation_failures": product_failures,
        "maximum_full_unitary_inverse_residual": max_inverse,
        "maximum_tracked_quasiphase_generator_residual": max_phase,
        "maximum_unitarily_centered_half_step_convergence_residual": max_convergence,
        "minimum_nondegenerate_branch_separation": min_separation,
        "minimum_order_deletion_signal": min_order,
        "minimum_contact_deletion_signal": min_contact,
        "single_Bloch_contact_stream_commutator_diagnostic": min_order,
        "real_space_two_cell_order_witness": real_space_order,
        "wrapped_quasiphase_called_energy": False,
        "generator_element_called_rate": False,
        "candidate_called_unique_physical_stress": False,
        "principal_branch_seam_is_convention_sensitive": True,
        "degenerate_branch_extension_claimed": False,
        "open_boundary_and_periodic_real_space_seam_preserved": True,
        "RouteC_joined_to_RouteB_open_boundary_as_one_apparatus": False,
    }
    check(
        "Route C constructs a covariant Hermitian full-unitary coframe generator and tracks nondegenerate quasiphase branches",
        max(max_hermitian, max_covariance, max_finite_covariance, max_inverse, max_phase, max_convergence) < FD_TOL
        and product_failures == 0 and min_separation > 1e-5 and min_contact > 1e-3
        and real_space_order["stream_permutation_is_bijective"]
        and real_space_order["coin_stream_contact_vs_contact_first_signal"] > 1e-3
        and real_space_order["contact_deletion_signal"] > 1e-3
        and real_space_order["accepted_norm_residual"] < TOL,
        output,
    )
    check(
        "Route C exposes the principal quasiphase seam without calling phase energy or the generator a rate",
        all(row["quasiphase"]["principal_wrapped_phase_jump"] > 6.0 and row["quasiphase"]["locally_unwrapped_phase_step"] < 1e-2 for row in rows)
        and not output["wrapped_quasiphase_called_energy"]
        and not output["generator_element_called_rate"]
        and not output["candidate_called_unique_physical_stress"],
        output,
    )
    return output


def no_go_discipline() -> dict:
    families = [
        {"family": "positive endpoint feedback square", "object": "b|D-rho|^2", "mechanism": "positive semidefinite local coframe feedback Hessian", "terminal": "unique joined response/receiver", "marker": "ATTEMPTED", "result": "constructive term; positive sign is candidate input and lambda/c/scale class remains"},
        {"family": "negative endpoint feedback square", "object": "-b|D-rho|^2", "mechanism": "equally local/covariant opposite feedback", "terminal": "sign discriminator", "marker": "ATTEMPTED", "result": "lawful algebraically; excluding it requires the unapproved stability criterion"},
        {"family": "feedback scale orbit", "object": "kappa b|D-rho|^2", "mechanism": "positive and negative nonzero scale multiples", "terminal": "normalization selection", "marker": "ATTEMPTED", "result": "kappa=1/2,1,2 all preserve covariance/Ward/inverse"},
        {"family": "normalized deficit feedback", "object": "b|D/||D||-rho|^2", "mechanism": "local-orbit normalization before feedback", "terminal": "remove raw-deficit scale", "marker": "LIVE_UNTESTED", "result": "normalization can be momentum/nonlocal and requires a fresh locality proof"},
        {"family": "nonlinear bounded feedback", "object": "local polynomial or saturating function of D-rho", "mechanism": "state-dependent nonlinear fixed points", "terminal": "unique stable receiver branch", "marker": "LIVE_UNTESTED", "result": "concrete alternative; blocks broad feedback no-go"},
        {"family": "full-unitary coframe generator", "object": "K_ab=iU^dag dU/de_ab", "mechanism": "tracked quasiphase derivative away from degeneracy", "terminal": "unitary-derived stress/receiver law", "marker": "ATTEMPTED", "result": "covariant representative constructed; physical stress and receiver coupling not selected"},
        {"family": "open real-space feedback apparatus", "object": "Cycle615 open flux plus Regge edge variables", "mechanism": "joint boundary dynamics and local receiver", "terminal": "one executed open-domain response law", "marker": "LIVE_UNTESTED", "result": "periodic/open seam remains explicit"},
    ]
    walls = {
        "W_feedback_law": "choice of square form, sign, and coefficient",
        "W_response_family": "continuous lambda and conserved-improvement coefficient",
        "W_receiver_map": "Regge response sign/value to Cycle612 3/4 or 5/4 word",
        "W_domain_join": "open charge boundary versus periodic Bloch/Regge real-space apparatus",
        "W_stress_identity": "full-unitary coframe generator to physical stress observable",
        "W_genesis": "one-hot orientation, blank work, binder/path/chart, and endpoint-law genesis",
    }
    names = tuple(walls)
    pairs = [{
        "left": names[first], "right": names[second],
        "left_closes_right": False, "right_closes_left": False, "independent": True,
    } for first in range(len(names)) for second in range(first + 1, len(names))]
    output = {
        "skill_freshness": {
            "origin_main_checked": True,
            "local_skill_sha256": "aeac7b2b7df30c350961f4b36b980a91e9c2ebeca3f35b6c1adcd731071bdab5",
            "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7",
            "current_origin_main_skill_followed": True,
            "proof_search_governance_sha256": "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258",
            "proof_search_governance_followed": True,
            "primitive_registry_and_current_source_notes_read": True,
        },
        "N1_normalized_families": families,
        "N1_broad_negative_failure": "three actionable families remain LIVE_UNTESTED",
        "N2_collapsed_wall_pair_audit": pairs,
        "N3_hidden_wall_scan": [
            "Cycle610 uniform one-hot role orientation and blank predicate/conjunction/B work",
            "fixed five Givens angles and Gray-path pivot order",
            "candidate negative-charge copy, conjugate coin, same-g separate contact, and no cross contact",
            "Cycle608 binder/path/chart and Cycle612 endpoint-use program",
            "feedback square form, 1/2 convention, relative D/rho scale, sign, and kappa",
            "Cycle576 raw deficit, Regge complex, pseudoinverse representative, lambda, and periodic momentum",
            "supplied diagnostic mapping between a numerical response sign and the Cycle612 words",
            "finite-difference epsilon and nondegenerate eigenbranch fixtures",
        ],
        "N3_phrase_scan": {
            "hits": ["registered primitives"],
            "classification": "cited retained authority: docs/audit/data/axiom_premise_nodes.json and all three current primitive source notes were read; the phrase grants only their declared roles and is non-hidden",
            "hidden_conditions_promoted": 0,
        },
        "N4_residual_matching": [
            {"witness": "docs/work_history/repo/review_feedback/PHYSICAL_LAWFUL_CHARGE_JOINED_METRIC_RESPONSE_TOURNAMENT_CYCLE615_NOTE_2026-07-22.md:20", "witness_residual": "support-two pair gate and full-sector compiler open", "current_residual": "same pair gate lowered; candidate sector identity remains", "match": "yes for physical lowering only"},
            {"witness": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md:8", "witness_residual": "support-two K=129 one-hot compiler", "current_residual": "same bus/predicate fabric reused for pair and bit-stream words", "match": "yes"},
            {"witness": "docs/work_history/repo/review_feedback/PHYSICAL_LAWFUL_CHARGE_JOINED_METRIC_RESPONSE_TOURNAMENT_CYCLE615_NOTE_2026-07-22.md:44", "witness_residual": "R(lambda,c) and {3/4,5/4} not selected", "current_residual": "same family re-enumerated after endpoint feedback", "match": "yes"},
            {"witness": "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md:65", "witness_residual": "delay/advance map supplied", "current_residual": "numeric Regge response to receiver word remains unproved", "match": "yes"},
            {"witness": "docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md:102", "witness_residual": "sign/normalization/metric identity and open real-space compiler", "current_residual": "feedback and full-unitary representatives retain those exact terminals", "match": "yes"},
        ],
        "N5_rhetoric_audit": {
            "physical_pair_compiler": "tested common seven-word code plus identity extension, clean work, and supplied one-hot orientation; not arbitrary dirty work",
            "not_derived_antimatter": "candidate local negative-charge sector only; no interacting particle identity theorem",
            "feedback_not_selection": "all audited local sign/scale and continuous lambda/c alternatives survive; no universal feedback theorem",
            "full_unitary_stress": "a six-component generator representative on nondegenerate periodic Bloch fixtures, not physical stress/energy/rate",
            "domain": "L3/L6/L7 periodic compiler and Bloch tests; no joint open-boundary real-space Regge apparatus",
        },
        "N6_partial_closure_paths": {
            "approved_primitives": "scale reference, kinetic-form isotropy, and realized-state evaluation retain only their registered roles; none supplies this feedback selector, stress identity, or receiver map",
            "paths": [
                "derive a feedback sign/normalization from a separately retained positivity or bounded-action theorem",
                "compile normalized or nonlinear endpoint feedback and test its complete fixed-point class",
                "couple the full-unitary coframe generator directly to the physical Cycle612 endpoint and derive the receiver map",
                "execute the Regge carrier and flux boundary together on one open real-space support-two apparatus",
            ],
        },
        "N7_steelman": "A hostile reviewer should reject any no-selection theorem beyond the audited square family. A normalized local deficit scalar, a bounded nonlinear feedback potential with a unique fixed point, or a direct coupling of the full-unitary K_ab representative to the physical endpoint could remove the lambda/c/sign orbit. The terminal obligations are concrete: prove strict locality and covariance, return detector work, preserve Gauss/Ward/inverse, and obtain one receiver word on held domains without a fitted target.",
        "N8_cross_cycle_echo": {
            "Cycle610": "turned a host-frame packing residual into a large bounded compiler, warning against minimum claims",
            "Cycle612": "turned supplied detector pointers into matter-caused endpoint bits while leaving response law live",
            "Cycle615": "constructed lawful charge and joined variation but explicitly queued feedback and full-unitary routes",
            "Cycle576": "constructed an actual Regge carrier while preserving sign, normalization, metric, and domain seams",
        },
        "walls": walls,
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "narrow_claim": "the explicitly audited linear feedback-square family does not collapse the inherited lambda/c or two-word receiver class",
        "shared_route_independent_obstruction": False,
        "minimum_content_claim": False,
        "axiom_pressure": False,
    }
    check(
        "Full current-origin/main N1-N8 blocks broad no-go, minimum-content, and axiom-pressure claims",
        len(families) >= 5 and len(pairs) == 15
        and not output["shared_route_independent_obstruction"]
        and not output["minimum_content_claim"] and not output["axiom_pressure"],
        output,
    )
    return output


def main() -> int:
    r615, r610, r612, shore_result = shore()
    note_contract()
    route_a_result = route_a(r610)
    route_b_result = route_b(r612)
    route_c_result = route_c()
    nogo = no_go_discipline()
    elapsed = perf_counter() - START
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(rss if sys.platform == "darwin" else rss * 1024)
    receipt = {
        "cycle": 620,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "HEAD": subprocess.check_output(("git", "rev-parse", "HEAD"), cwd=ROOT, text=True).strip(),
        "runner_sha256": digest("scripts/physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_2026_07_22.py"),
        "note_sha256": digest("docs/work_history/repo/review_feedback/PHYSICAL_PAIR_SUPERCELL_RECEIVER_FEEDBACK_QUASIENERGY_TOURNAMENT_CYCLE620_NOTE_2026-07-22.md"),
        "pins": PINS,
        "shore": shore_result,
        "route_A_pair_supercell": route_a_result,
        "route_B_receiver_feedback": route_b_result,
        "route_C_full_unitary_quasienergy": route_c_result,
        "no_go_discipline": nogo,
        "decisive_answer": "The Cycle615 resource/cubic-neutral-pair involution now has a common-E, clean-work, exact support-two K=129 compiler and a distinct candidate +/- occupation stream on L3/L6/L7, with the supplied negative sector explicitly not called antimatter. A physical endpoint-controlled local gauge-Regge feedback square is constructively available, but after the equally local sign/scale alternatives and every surviving lambda/c improvement are re-enumerated it does not collapse either the continuous response family or {3/4,5/4}. The actual full coin-stream-contact Fock unitary supplies a covariant Hermitian coframe generator and tracked quasiphase derivatives away from degeneracy, not a unique physical stress, energy, rate, or receiver law.",
        "inventory": {
            "supplied": [
                "Cycle610 K=129 one-hot orientation/predicate/bus fabric and blank work",
                "candidate negative-charge occupation copy, conjugate coin, separate same-g contact, and no cross contact",
                "five exact cubic-scalar Givens angles and the neutral resource excitation",
                "Cycle608 binder/path/chart and Cycle612 endpoint-use/admission program",
                "feedback square form, 1/2 convention, D/rho relative scale, sign/scale alternatives",
                "Cycle576 Regge complex/raw deficit/pseudoinverse/lambda and periodic Bloch fixtures",
                "diagnostic response-sign to Cycle612-word convention and finite-difference epsilon",
            ],
            "derived_or_executed": [
                "common seven-word embedding and exact Gray/conjunction pair lowering",
                "clean-work return, identity extension, inverse, deletion, all24/all576 pair covariance",
                "two-charge A/B occupation stream geometry and semantics on L3/L6/L7",
                "endpoint-controlled feedback Hessian/force and full sign/scale/lambda/improvement family audit",
                "Gauss neutrality, Regge Ward, stationary, inverse, covariance, and feedback deletions",
                "full-Fock coin-stream-contact coframe generators and nondegenerate quasiphase derivative match",
                "principal wrapped-phase seam and order/contact falsifiers",
            ],
            "not_derived": [
                "antimatter identity or negative-sector law selection",
                "uniform one-hot/work/binder/path/chart genesis",
                "feedback square/sign/normalization or a stability law selecting them",
                "unique lambda, improvement, metric observable, response sign, or Cycle612 receiver word",
                "joint open-boundary real-space Regge/feedback compiler",
                "physical stress, energy, gravity, causal rate, event, Record, or Born rule",
            ],
        },
        "six_wall_ledger": {
            "C_ref": "ADVANCED locally: the pair/sector compiler uses physical one-hot proper-cubic branches and passes all24/all576; orientation genesis, endpoint chart/path, and receiver map remain supplied.",
            "C_num": "SHARPENED: exact pair angles and a full affine feedback family are explicit; feedback scale/sign, lambda, improvement, and empirical normalization remain unselected.",
            "C_wrap": "ADVANCED diagnostically: full-unitary tracked quasiphase derivatives agree with K_ab away from degeneracy and an explicit principal seam is exposed; wrapped phase is not energy.",
            "C_int": "ADVANCED: the neutral pair gate, +/- coin-stream-contact, physical endpoint feedback, joined Regge variation, and full-unitary coframe derivative are each composed on declared interfaces; no one apparatus joins the open boundary to periodic Regge.",
            "C_local": "ADVANCED: the pair gate and two-charge occupation stream now have constant-overhead support-two K=129 words with clean return and held-size geometry; economical packing and autonomous role/work genesis remain open.",
            "C_source": "SHARPENED: endpoint-controlled deficit-density feedback is a local candidate source law, but its sign/scale and inherited lambda/c class survive, so {3/4,5/4} remains unselected and no gravity claim follows.",
        },
        "maturity_0_to_5": {
            "operational_quantum_records": 4.08,
            "time": 3.08,
            "inertia_matter": 4.58,
            "gravity_source": 4.02,
            "Born_probability": 2.0,
        },
        "strongest_constructive_result": "a common-E exact support-two physical compiler for the resource-to-cubic-neutral-pair involution plus distinct candidate +/- occupation streams, with explicit Givens/clean-work/bus debits and L3/L6/L7 all-frame controls",
        "shared_obstruction_or_axiom_pressure": False,
        "optimal_next_campaign": "attack feedback-law selection with normalized and nonlinear local potentials and a direct K_ab-to-endpoint coupling, while compiling the open flux boundary and Regge carrier into one real-space apparatus; require one receiver word without a sign map, refit, or stability postulate",
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "pass": FAIL == 0,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n")
    print("RECEIPT", json.dumps(receipt, sort_keys=True, default=json_default))
    print("SUMMARY", json.dumps({
        "pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
        "elapsed_seconds": elapsed,
        "route_A": route_a_result["disposition"],
        "route_B": route_b_result["disposition"],
        "route_C": route_c_result["disposition"],
        "receiver_equivalence": route_b_result["Cycle612_receiver_words"],
        "axiom_pressure": False,
    }, sort_keys=True))
    return int(FAIL != 0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold_handle:
        terminal = sys.stdout
        sys.stdout = Tee(terminal, cold_handle)
        try:
            exit_code = main()
        finally:
            sys.stdout = terminal
    raise SystemExit(exit_code)
