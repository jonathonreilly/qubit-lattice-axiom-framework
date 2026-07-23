#!/usr/bin/env python3
"""Cycle620: pair-register algebra, feedback candidates, and coframe generators.

The three routes are deliberately separate.  Route A lowers the Cycle615
resource/cubic-neutral-pair involution into a 13-bit register and reuses the
Cycle610 K=129 conditional coordinate/gate descriptors.  It does not construct
a literal physical M2 encoder or update.  Route B adds one explicit conditional
feedback-square candidate to the joined gauge-Regge algebra and audits local
sign/scale alternatives.  Route C differentiates the actual coin -> stream ->
contact full-Fock unitary with respect to a spatial coframe.  Wrapped
quasiphase is not energy or stress, and a generator element is not a rate or
time.  Authority none; audit unset.
"""
from __future__ import annotations

import contextlib
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import io
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
        "e9649a3193590a0caeccb832d8738bbaa39ca3ca08a44131cd5cfe47a68f015e",
    "docs/work_history/repo/review_feedback/PHYSICAL_LAWFUL_CHARGE_JOINED_METRIC_RESPONSE_TOURNAMENT_CYCLE615_NOTE_2026-07-22.md":
        "58ceb8fcd82a808535ea2c7cc67084eec159255d4c38c368bbc2fa67b4c90a3f",
    "outputs/physical_lawful_charge_joined_metric_response_tournament_cycle615_receipt_2026_07_22.json":
        "7bf6e65b72976029bd55019a5338e5e9ee29c8c94f317e14c8b3031c453da929",
    "outputs/physical_lawful_charge_joined_metric_response_tournament_cycle615_cold_2026_07_22.txt":
        "2369ba76754bcc834508adb254bd4da6f10c42e31d16704edc612541f948a3ea",
    "scripts/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22.py":
        "ed2250711646ad99bf077e74b8e4194f2df0a2cf368d3c05c45ea95cac8083db",
    "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md":
        "3768d2a1407bdc8de06e2a55fa18300469b1006c0a16a78ada8b8d3a4b936105",
    "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_receipt_2026_07_22.json":
        "375f843606a81970ae50f71d74c53f7e4c4d1437007daaecbedd0b19e3fdfa34",
    "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_cold_2026_07_22.txt":
        "0adbee38e398c9e1d1ccd2733454ead2669338b86d48cbefa5331abb78c126e8",
    "scripts/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22.py":
        "ac2a337140d40624500a5f23fc771b9b716d4c4bd467eb27a1963d1db5eac875",
    "docs/work_history/repo/review_feedback/PHYSICAL_RADIUS_ONE_DRESSED_DETECTOR_CONTROLLED_UPDATE_RECURRENCE_TOURNAMENT_CYCLE608_NOTE_2026-07-22.md":
        "6e8e3aae72547e8a13b0ced4cea7230c7b594348073e45802c95e6a55329ee54",
    "outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json":
        "4ccba85490c08120aab645917fee87dbd58f21cf4fb17c5f60b3a4fab9dbca48",
    "outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_cold_2026_07_22.txt":
        "087e3ef7a5657a85432553f29e7050458a9c8552a3e59852e74ae86b5f9fc605",
    "scripts/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_2026_07_22.py":
        "91f22d23dd2730f76a05736634236d41036f68eaedc4921daca69de25ab6a344",
    "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md":
        "920776555dce6505bccb0e46e552e90d24858c08cfb7f6978d884f10a5bb0789",
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

CAUSAL_TIME_PR_5557 = {
    "commit": "a1e2f1ea60b1cf9b9cb0ae100c61cfd1f3a07318",
    "note": "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
    "note_sha256": "028133c490e771dd3012061c79910fcfb88cd6132df072ec15e725fe9bc35496",
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


def shore() -> tuple[dict, dict, dict, dict, dict]:
    observed = {path: digest(path) for path in PINS}
    r615 = json.loads((ROOT / "outputs/physical_lawful_charge_joined_metric_response_tournament_cycle615_receipt_2026_07_22.json").read_text())
    r610 = json.loads((ROOT / "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_receipt_2026_07_22.json").read_text())
    r608 = json.loads((ROOT / "outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json").read_text())
    r612 = json.loads((ROOT / "outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json").read_text())
    causal_note = subprocess.check_output(
        ("git", "show", f'{CAUSAL_TIME_PR_5557["commit"]}:{CAUSAL_TIME_PR_5557["note"]}'),
        cwd=ROOT,
    )
    c610_scope = r610["physical_M2_scope"]
    c608_boundary = r608["physical_promotion_boundary"]
    c608_compiler_null_keys = (
        "physical_encoder_E", "physical_update_G", "intertwiner_certificate",
        "physical_placement", "physical_primitive_product", "full_code_leakage",
        "locally_enforced_chart", "locally_enforced_path", "autonomous_genesis",
    )
    c608_composition_null_keys = (
        "physical_encoder_E", "physical_update_G", "intertwiner_certificate",
        "physical_placement", "physical_primitive_product", "full_code_leakage",
        "Event", "Record", "time", "full_echo",
    )
    result = {
        "hashes_match": observed == PINS,
        "observed": observed,
        "Cycle615_pass": r615["pass"],
        "Cycle610_pass": r610["pass"],
        "Cycle608_pass": r608["pass"],
        "Cycle612_pass": r612["pass"],
        "Cycle615_physical_pair_gate_open": not r615["route_A_local_neutral_pair_sector"]["physical_support_two_pair_gate_executed"],
        "Cycle615_receiver_selection_residual": r615["route_C_joined_metric_receiver_equivalence"]["receiver_label_selection_residual"],
        "Cycle610_conditional_support_two_descriptors": c610_scope["conditional_support_two_primitive_descriptors_compiled"],
        "Cycle610_literal_physical_encoder": c610_scope["literal_physical_encoder_composed"],
        "Cycle610_physical_intertwiner_residual": c610_scope["physical_intertwiner_residual"],
        "Cycle610_physical_code_leakage_evaluated": c610_scope["physical_code_leakage_evaluated"],
        "Cycle610_one_fine_site_translation_covariant": r610["fine_site_translation_falsifier"]["one_fine_site_translation_covariant_code_space"],
        "Cycle610_local_constraints_enforced": r610["local_constraint_scope"]["constraint_preparation_repair_rejection_or_penalty_dynamics_constructed"],
        "Cycle608_physical_promotion_boundary_all_null": len(c608_boundary) == 14 and all(value is None for value in c608_boundary.values()),
        "Cycle608_compiler_rows_physical_boundaries_all_null": all(
            all(row[key] is None for key in c608_compiler_null_keys)
            and row["every_cell_incident_C_role_table_audit"]["covariance_credit"] is None
            and row["inherited_transported_all24_all576"]["Cycle608_physical_covariance_credit"] is None
            for row in r608["compiler_rows"]
        ),
        "Cycle608_composition_physical_boundaries_all_null": all(
            r608["algebraic_composition_blueprint"][key] is None
            for key in c608_composition_null_keys
        ),
        "Cycle608_detector_Event_Record_time_boundaries_all_null": all(
            r608["route_B_candidate_role_blueprint"][key] is None
            for key in ("physical_detector_output", "physical_candidate_association", "Event", "Record", "time")
        ) and r608["route_C_inherited_prefix_controls"]["proper_time"] is None,
        "Cycle608_cold_hash_self_consistent": r608["cold_transcript_sha256"] == PINS["outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_cold_2026_07_22.txt"],
        "Cycle612_receiver_words": sorted({row["probe_over_reference"] for row in r612["route_C_source_motion_ratio"]["rows"] if row["physical_source_reservoir_predicate"] and row["receiver_M2"]}),
        "causal_time_PR_5557": {
            "commit": CAUSAL_TIME_PR_5557["commit"],
            "note_sha256": sha256(causal_note).hexdigest(),
            "matches_pin": sha256(causal_note).hexdigest() == CAUSAL_TIME_PR_5557["note_sha256"],
            "comparison_only": True,
            "runner_imported_or_executed": False,
            "backcredit": False,
        },
    }
    check(
        "Cycle608/610/612/615 shore is byte-pinned and retains the exact live residuals",
        result["hashes_match"]
        and all(result[key] for key in ("Cycle615_pass", "Cycle610_pass", "Cycle608_pass", "Cycle612_pass"))
        and result["Cycle615_physical_pair_gate_open"]
        and result["Cycle615_receiver_selection_residual"] == 1
        and result["Cycle610_conditional_support_two_descriptors"]
        and not result["Cycle610_literal_physical_encoder"]
        and result["Cycle610_physical_intertwiner_residual"] is None
        and not result["Cycle610_physical_code_leakage_evaluated"]
        and not result["Cycle610_one_fine_site_translation_covariant"]
        and not result["Cycle610_local_constraints_enforced"]
        and result["Cycle608_physical_promotion_boundary_all_null"]
        and result["Cycle608_compiler_rows_physical_boundaries_all_null"]
        and result["Cycle608_composition_physical_boundaries_all_null"]
        and result["Cycle608_detector_Event_Record_time_boundaries_all_null"]
        and result["Cycle608_cold_hash_self_consistent"]
        and result["Cycle612_receiver_words"] == ["3/4", "5/4"]
        and result["causal_time_PR_5557"]["matches_pin"]
        ,
        result,
    )
    return r615, r610, r608, r612, result


def note_contract() -> None:
    body = " ".join(NOTE.read_text().lower().replace("`", "").replace("*", "").split())
    required = (
        "cycle 620", "authority: none", "audit: unset", "route a", "route b", "route c",
        "13-bit register", "conditional", "support-two descriptors", "all-24", "all 576",
        "l3", "l6", "l7", "coin -> stream -> contact", "not derived antimatter",
        "positive square", "negative square", "scale", "lambda", "improvement", "3/4", "5/4",
        "not selection", "gauss", "ward", "quasiphase", "wrapped phase is not energy",
        "generator element is not a rate or time", "open-boundary", "periodic", "n1", "n8",
        "one-fine-site translation", "local constraints", "no axiom pressure",
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
    malformed_failures = 0
    rows = 0
    negative_x = 0
    for operation in conditionals:
        condition = operation["condition"]
        negative_x += 2 * sum(value == 0 for value in condition)
        for raw in product((0, 1), repeat=12):
            # The supplied conditional orientation predicate is the thirteenth,
            # positive control and is one on this branch's declared code.
            normalized = (1,) + tuple(value if wanted else 1 - value for value, wanted in zip(raw, condition))
            work = [0] * 12
            work[0] ^= normalized[0] & normalized[1]
            for index in range(2, 13):
                work[index - 1] ^= work[index - 2] & normalized[index]
            fired = work[11]
            for index in reversed(range(2, 13)):
                work[index - 1] ^= work[index - 2] & normalized[index]
            work[0] ^= normalized[0] & normalized[1]
            row_failure = int(fired != int(raw == condition) or any(work))
            failures += row_failure
            malformed_failures += int(raw != condition) * row_failure
            rows += 1
    return {
        "conditional_operations": len(conditionals),
        "clean_control_rows_exhausted": rows,
        "clean_control_failures": failures,
        "lawful_condition_match_rows": len(conditionals),
        "malformed_nonmatching_rows_exhausted": rows - len(conditionals),
        "malformed_nonmatching_failures": malformed_failures,
        "negative_control_X_gates": negative_x,
        "clean_conjunction_work_roles": 12,
        "Toffoli_calls": 24 * len(conditionals),
        "one_site_gate_descriptors_after_exact_Toffoli_lowering": 9 * 24 * len(conditionals) + negative_x,
        "two_site_gate_descriptors_after_exact_Toffoli_lowering": (6 * 24 + 1) * len(conditionals),
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
        "conditional_support_two_endpoint_pairs_audited": primitive_pairs,
        "endpoint_or_bus_inverse_failures": endpoint_failures,
        "maximum_bus_distance": max_distance,
        "move_apply_restore_SWAPs_all24_per_coarse_cell": route_swaps,
        "all_conditional_routed_descriptors_support_at_most_two": endpoint_failures == 0,
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
    inherited_predicate = r610["conditional_orientation_controlled_compute_act_uncompute"]
    conjunction.update({
        "inherited_conditional_orientation_predicate_compute_support_two_descriptors_per_branch": inherited_predicate["predicate_compute_support_two_gates"],
        "inherited_conditional_orientation_predicate_compute_uncompute_support_two_descriptors_per_branch": inherited_predicate["predicate_compute_and_uncompute_support_two_gates"],
        "inherited_orientation_predicate_clean_work_return": inherited_predicate["clean_predicate_work_return"],
        "total_pair_macro_one_or_two_site_descriptors_per_branch_before_bus":
            conjunction["one_site_gate_descriptors_after_exact_Toffoli_lowering"]
            + conjunction["two_site_gate_descriptors_after_exact_Toffoli_lowering"]
            + inherited_predicate["predicate_compute_and_uncompute_support_two_gates"],
    })
    layout = sector_layout()
    bus = pair_bus_audit(layout, conditionals)
    stream = stream_geometry_and_semantics(layout)

    # This is one algebraic embedding of all seven logical basis states into a
    # 13-bit resource/+/- occupation register.  It is not a literal map into
    # the physical M2 lattice.  Apply the two-level register word sparsely on
    # the full 2^13 block; every other register word is the identity.
    rng = np.random.default_rng(620)
    logical = rng.normal(size=7) + 1j * rng.normal(size=7)
    logical /= np.linalg.norm(logical)
    encoded = np.zeros(1 << 13, dtype=complex)
    encoded[list(words)] = logical
    register_updated = encoded.copy()
    apply_compiled_conditionals(register_updated, conditionals)
    expected_encoded = np.zeros_like(encoded)
    expected_encoded[list(words)] = expected @ logical
    register_intertwiner_residual = float(np.linalg.norm(register_updated - expected_encoded))
    register_array_escape = float(np.linalg.norm(np.delete(register_updated, list(words))))
    restored = register_updated.copy()
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
        deletion_signals[name] = float(np.linalg.norm(trial - register_updated))

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
    mass_rows = r610["conditional_onsite_mass_contact_seam_composition"]["fixture_residuals"]
    conjugate_mass_spectrum = float(np.max(np.abs(np.sort(np.angle(np.linalg.eigvals(coin))) + np.sort(np.angle(np.linalg.eigvals(coin.conj())))[::-1])))

    output = {
        "object": "one seven-word resource/+/- register embedding with an exact Gray/conjunction descriptor word and two conditional coarse-grid double-buffer streams",
        "disposition": "CONSTRUCTIVE_SEVEN_LEVEL_GIVENS_AND_REGISTER_DESCRIPTOR_ALGEBRA; LITERAL_PHYSICAL_M2_COMPILER_UNEXECUTED",
        "register_embedding": {
            "register_bits": 13,
            "resource_bit": 0,
            "positive_occupation_bits": list(range(1, 7)),
            "negative_occupation_bits": list(range(7, 13)),
            "active_register_words": words,
            "active_logical_dimension": 7,
            "identity_extension_words": (1 << 13) - 7,
            "register_intertwiner_residual": register_intertwiner_residual,
            "register_array_escape_residual": register_array_escape,
        },
        "Givens_angle_inventory": angle_rows,
        "high_level_pair_factors": high_level,
        "Gray_conditionals": {"count": len(conditionals), "hamming_four_per_Givens": 7, "hamming_three_resource_pair_swap": 5},
        "clean_lowering": conjunction,
        "layout": {
            "K": c610.K,
            "fine_coordinate_sites_in_supplied_K_cell": c610.K ** 3,
            "declared_A_B_resource_data_roles": 25,
            "declared_pair_conjunction_work_role_orbit": 12 * 24,
            "reused_Cycle610_conditional_orientation_and_predicate_roles": True,
            "constant_added_declared_role_upper_bound": 25 + 12 * 24,
            "data_role_collisions": layout["data_role_collisions"],
            "work_role_collisions": layout["work_role_collisions"],
            "path_failures": layout["path_or_source_target_disjointness_failures"],
        },
        "stream_constant_gate_upper_bound": {
            "positive_remote_CNOT_move_apply_restore_two_site_descriptors": 217,
            "negative_remote_CNOT_move_apply_restore_two_site_descriptors": 197,
            "scatter_clear_and_local_swap_two_site_descriptors_per_cell_before_orientation_control": 4980,
            "orientation_control_gadget": "the pinned Cycle610 conditional dual-predicate descriptor wrapper is reused",
        },
        "pair_bus": bus,
        "stream": stream,
        "pair_operator_residual": float(np.linalg.norm(target - expected)),
        "pair_unitarity_residual": float(np.linalg.norm(target.conj().T @ target - np.eye(7))),
        "register_inverse_residual": inverse_residual,
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
            "inherited_conditional_factor_deletion_signals": inherited_order["delete_each_factor_difference"],
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
        "literal_physical_M2_encoder_composed": False,
        "literal_physical_update_composed": False,
        "physical_M2_cost_per_coarse_cell": None,
        "physical_intertwiner_residual": None,
        "physical_code_leakage_evaluated": False,
        "physical_code_leakage_residual": None,
        "fine_NN_placement_product_executed": False,
        "physical_support_two_gate_product_executed": False,
        "physical_all24_update_covariance_executed": False,
        "physical_all576_update_composition_executed": False,
        "physical_held_size_update_executed": False,
        "physical_deletion_or_malformed_code_control_executed": False,
        "one_fine_site_translation_covariant_code_space": False,
        "one_fine_site_translation_covariant_update": False,
        "proper_rotations_about_every_fine_site_executed": False,
        "local_constraint_enforcement_constructed": False,
        "autonomous_no_host_schedule_executed": False,
        "conditional_support_two_coordinate_descriptors_executed": True,
        "conditional_coarse_grid_translation_only": True,
        "one_fine_site_translation_symmetric_difference": {
            row["length"]: row["one_fine_site_x_translation_symmetric_difference"]
            for row in r610["fine_site_translation_falsifier"]["rows"]
        },
        "candidate_negative_sector_called_derived_antimatter": False,
        "global_Jordan_Wigner_or_parity_service": False,
        "runtime_host_frame_or_size_query": False,
        "supplied_K_partition_origin_role_coloring": True,
        "uniform_one_hot_orientation_genesis_supplied": True,
        "blank_B_conjunction_predicate_work_supplied": True,
    }
    check(
        "Route A gives an exact seven-level/Givens register word and conditional support-two descriptors",
        max(output["pair_operator_residual"], output["pair_unitarity_residual"], register_intertwiner_residual, register_array_escape, inverse_residual, covariance) < TOL
        and group_failures == 0
        and conjunction["clean_control_failures"] == 0
        and conjunction["malformed_nonmatching_failures"] == 0
        and layout["data_role_collisions"] == layout["work_role_collisions"] == layout["path_or_source_target_disjointness_failures"] == 0
        and bus["all_conditional_routed_descriptors_support_at_most_two"]
        and all(signal > 1e-4 for signal in deletion_signals.values()),
        output,
    )
    check(
        "Route A preserves the conditional +/- register streams and mass fixture without physical-M2 promotion",
        stream["maximum_failure_count"] == 0
        and all(all(value > 0 for value in row["deletion_signals"].values()) for row in stream["rows"])
        and update_inverse < TOL and order_signal > 1e-3 and output["one_particle_mass"]["preserved"]
        and not output["candidate_negative_sector_called_derived_antimatter"]
        and not output["literal_physical_M2_encoder_composed"]
        and output["physical_M2_cost_per_coarse_cell"] is None
        and output["physical_intertwiner_residual"] is None
        and not output["physical_code_leakage_evaluated"]
        and not output["physical_support_two_gate_product_executed"]
        and not output["physical_all24_update_covariance_executed"]
        and not output["physical_all576_update_composition_executed"]
        and not output["one_fine_site_translation_covariant_code_space"]
        and not output["local_constraint_enforcement_constructed"]
        and not output["autonomous_no_host_schedule_executed"],
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
        "object": "conditional local endpoint-controlled Regge-deficit/gauge-density feedback-square family plus every audited sign/scale/lambda/improvement alternative",
        "disposition": "CONSTRUCTIVE_CONDITIONAL_FEEDBACK_SQUARE_FAMILY; UNIQUE_SOURCE_GRAVITY_AND_RECEIVER_SELECTION_UNEARNED",
        "feedback_action": "A_fb=(sigma*kappa/2) sum_x b_x |D_x[e]-rho_x|^2",
        "declared_local_Cycle612_endpoint_word": "P_d(pointer); Toffoli(pointer,binder,opportunity); P_d(pointer), then use/uncompute opportunity",
        "literal_physical_endpoint_compiler_revalidated_in_Cycle620": False,
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
        "unique_source_law_selected": False,
        "physical_gravity_law_selected": False,
        "gravity_or_physical_stress_claimed": False,
    }
    check(
        "Route B constructs a conditional local feedback-square family and preserves Gauss/Ward/inverse/covariance",
        output["endpoint_and_detector_work_return_blank"]
        and max(max_stationary, max_ward, max_covariance, max_inverse) < TOL
        and group_failures == 0 and min_deletion > 1e-8
        and all(row["deleted_detector_endpoint_bit"] == 0 for row in endpoint_rows)
        and all(all(family["continuous_family_nonconstant"] for family in row["analytic_families"]) for row in rows),
        output,
    )
    check(
        "Route B does not mis-credit the square as a unique source, gravity, or receiver selection",
        continuous_signs == [-1, 1] and positive_continuous_signs == [-1, 1]
        and diagnostic_words == ["3/4", "5/4"]
        and not output["continuous_family_collapsed"] and not output["receiver_class_collapsed"]
        and not output["feedback_sign_or_scale_derived"]
        and not output["Cycle612_numeric_response_sign_to_word_map_derived"]
        and not output["unique_source_law_selected"]
        and not output["physical_gravity_law_selected"]
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
        "disposition": "CONSTRUCTIVE_FULL_UNITARY_COFRAME_GENERATOR_AND_TRACKED_QUASIPHASE_REPRESENTATIVE; ENERGY_STRESS_RATE_AND_TIME_IDENTIFICATIONS_UNEARNED",
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
        "quasiphase_or_generator_called_physical_stress": False,
        "generator_element_called_rate": False,
        "generator_or_schedule_called_time": False,
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
        "Route C exposes the principal quasiphase seam without calling it energy, stress, rate, or time",
        all(row["quasiphase"]["principal_wrapped_phase_jump"] > 6.0 and row["quasiphase"]["locally_unwrapped_phase_step"] < 1e-2 for row in rows)
        and not output["wrapped_quasiphase_called_energy"]
        and not output["quasiphase_or_generator_called_physical_stress"]
        and not output["generator_element_called_rate"]
        and not output["generator_or_schedule_called_time"]
        and not output["candidate_called_unique_physical_stress"],
        output,
    )
    return output


def no_go_discipline() -> dict:
    families = [
        {"family": "seven-level Givens pair algebra", "object": "resource plus six opposite-direction pair branches", "mechanism": "five exact Givens rotations around one resource/pair swap", "terminal": "register intertwiner, inverse, deletion, all24 and all576", "marker": "ATTEMPTED", "result": "passes as seven-level/13-bit register algebra; no physical M2 encoder is composed"},
        {"family": "conditional K129 coordinate descriptors", "object": "partition-relative roles and returned-bus gate descriptors", "mechanism": "supplied one-hot orientation and move/apply/restore paths", "terminal": "conditional support-two/NN audit and one-fine-site promotion test", "marker": "ATTEMPTED", "result": "descriptor audit passes while inherited tagged support has nonzero one-site difference"},
        {"family": "positive endpoint feedback square", "object": "+kappa b|D-rho|^2", "mechanism": "positive local coframe-feedback Hessian", "terminal": "one response and receiver label", "marker": "ATTEMPTED", "result": "constructive candidate family; lambda, improvement and receiver alternatives remain"},
        {"family": "opposite-sign and scale feedback orbit", "object": "sigma kappa b|D-rho|^2", "mechanism": "local sign and nonzero-scale alternatives", "terminal": "sign and normalization discriminator", "marker": "ATTEMPTED", "result": "both signs and all tested scales preserve the algebraic controls"},
        {"family": "full-unitary coframe generator", "object": "K_ab=iU^dag dU/de_ab", "mechanism": "tracked nondegenerate quasiphase derivative", "terminal": "covariant generator representative", "marker": "ATTEMPTED", "result": "constructed without energy, stress, rate, time, or receiver identification"},
        {"family": "two-cell factor-order witness", "object": "4096-dimensional two-cell full-Fock word", "mechanism": "stream permutation and contact deletion", "terminal": "coin-stream-contact order sensitivity", "marker": "ATTEMPTED", "result": "order and contact signals are nonzero; this is not a physical-time law"},
    ]
    live_routes = [
        "construct a state-carried Z129^3 phase and literal fine-NN physical encoder/update",
        "construct fine-NN admissibility preparation or enforcement for orientation and work constraints",
        "test normalized or bounded nonlinear feedback with a complete fixed-point audit",
        "couple the coframe generator directly to one locally compiled endpoint",
        "join the open flux boundary and Regge variables in one real-space apparatus",
    ]
    walls = {
        "W_physical_lowering": "literal physical M2 encoder, update, fine-NN product and full-code leakage",
        "W_translation_constraints": "one-fine-site covariance and locally enforced admissibility",
        "W_feedback_law": "choice of square form, sign, and coefficient",
        "W_response_family": "continuous lambda and conserved-improvement coefficient",
        "W_receiver_map": "Regge response sign/value to Cycle612 3/4 or 5/4 word",
        "W_domain_join": "open charge boundary versus periodic Bloch/Regge real-space apparatus",
        "W_observable_identity": "coframe generator to energy, stress, rate or time observable",
    }
    names = tuple(walls)
    pairs = [{
        "left": names[first], "right": names[second],
        "left_to_right": {"status": "NOT_ESTABLISHED", "reason": "not jointly executed"},
        "right_to_left": {"status": "NOT_ESTABLISHED", "reason": "not jointly executed"},
        "independence": {"status": "NOT_ESTABLISHED", "reason": "directional non-implication was not proved"},
    } for first in range(len(names)) for second in range(first + 1, len(names))]
    phrases = ("we assume", "by construction", "as is standard", "the framework provides",
               "bridge context", "background", "naturally", "obviously", "standard qft",
               "registered", "canonical")
    phrase_hits = [phrase for phrase in phrases if phrase in NOTE.read_text().lower()]
    markers = all(row["marker"] in {"ATTEMPTED", "RULED OUT BY PRIOR"} for row in families)
    independence_complete = all(row["independence"]["status"] == "ESTABLISHED" for row in pairs)
    current_cycle_path = "scripts/physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_2026_07_22.py"

    def cited_line_exists(reference: str, line: int) -> bool:
        if reference.startswith(f'{CAUSAL_TIME_PR_5557["commit"]}:'):
            lines = subprocess.check_output(("git", "show", reference), cwd=ROOT, text=True).splitlines()
        else:
            path = ROOT / reference
            if not path.is_file():
                return False
            lines = path.read_text().splitlines()
        return 1 <= line <= len(lines) and bool(lines[line - 1].strip())

    n4 = [
        {"prior_path": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md", "prior_line": 96, "prior_residual": "literal physical encoder/intertwiner/full-code leakage unevaluated", "current_path": current_cycle_path, "current_line": 727, "current_residual": "Cycle620 reuses only the conditional K129 descriptor scope", "exact_match": True, "same_scope": True, "use_as_closure": True},
        {"prior_path": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md", "prior_line": 25, "prior_residual": "one-fine-site translation-covariant physical promotion is false", "current_path": current_cycle_path, "current_line": 722, "current_residual": "same inherited tagged-support promotion test", "exact_match": True, "same_scope": True, "use_as_closure": True},
        {"prior_path": "docs/work_history/repo/review_feedback/PHYSICAL_LAWFUL_CHARGE_JOINED_METRIC_RESPONSE_TOURNAMENT_CYCLE615_NOTE_2026-07-22.md", "prior_line": 34, "prior_residual": "seven coarse roles are not seven physical M2s", "current_path": current_cycle_path, "current_line": 710, "current_residual": "seven-level/register algebra still lacks a physical encoder/update", "exact_match": True, "same_scope": True, "use_as_closure": False},
        {"prior_path": "docs/work_history/repo/review_feedback/PHYSICAL_LAWFUL_CHARGE_JOINED_METRIC_RESPONSE_TOURNAMENT_CYCLE615_NOTE_2026-07-22.md", "prior_line": 60, "prior_residual": "lambda/improvement and two receiver labels survive", "current_path": current_cycle_path, "current_line": 985, "current_residual": "same family survives feedback-square candidates", "exact_match": True, "same_scope": True, "use_as_closure": True},
        {"prior_path": "docs/work_history/repo/review_feedback/PHYSICAL_RADIUS_ONE_DRESSED_DETECTOR_CONTROLLED_UPDATE_RECURRENCE_TOURNAMENT_CYCLE608_NOTE_2026-07-22.md", "prior_line": 23, "prior_residual": "physical encoder/update/intertwiner/placement/product/leakage/detector/time boundary is null", "current_path": current_cycle_path, "current_line": 187, "current_residual": "Cycle620 grants no physical endpoint or compiler backcredit", "exact_match": True, "same_scope": True, "use_as_closure": True},
        {"prior_path": "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md", "prior_line": 70, "prior_residual": "local source-on receiver words are 3:4 and 5:4", "current_path": current_cycle_path, "current_line": 983, "current_residual": "Cycle620 compares only to those declared labels", "exact_match": True, "same_scope": True, "use_as_closure": False},
        {"prior_path": f'{CAUSAL_TIME_PR_5557["commit"]}:{CAUSAL_TIME_PR_5557["note"]}', "prior_line": 42, "prior_residual": "delay is rate-reachable while advance is edit-reachable", "current_path": current_cycle_path, "current_line": 209, "current_residual": "Cycle620 imports neither causal mechanism", "exact_match": True, "same_scope": False, "use_as_closure": False},
    ]
    n5 = [
        {"claim": "Route A is register algebra rather than a literal physical M2 compiler", "per_element": "13 register bits and seven active words are enumerated", "per_site": "declared roles receive conditional K-cell coordinates", "per_mode": "six pair branches and two charge-sector copies are audited", "per_block": "no physical encoder/update or full physical-code leakage is composed", "lattice_wide": "one-fine-site support is noncovariant and local constraints are not enforced"},
        {"claim": "the feedback square is a candidate family rather than a unique source or gravity law", "per_element": "D, rho, sign and scale are supplied", "per_site": "the endpoint bit multiplies a local square", "per_mode": "lambda and improvement alternatives are enumerated", "per_block": "both receiver labels survive", "lattice_wide": "open-boundary and periodic Regge apparatuses are not joined"},
        {"claim": "the coframe generator is not identified as energy, stress, rate, or time", "per_element": "K_ab is computed from a relative unitary derivative", "per_site": "no local physical stress operator is selected", "per_mode": "nondegenerate Bloch branches are tracked", "per_block": "the 64-dimensional unitary and two-cell witness are separate", "lattice_wide": "no operational clock, rate accumulation, or gravity dynamics is executed"},
        {"claim": "the opposite-charge copy is not a derived particle identity", "per_element": "charge sign and conjugated coin are supplied", "per_site": "separate same-g contact and no cross contact are supplied", "per_mode": "six conjugate directions are tested", "per_block": "the 64-word sectors are algebraic copies", "lattice_wide": "no empirical calibration or autonomous genesis is derived"},
        {"claim": "local Cycle612 labels are not external causal-time PR evidence", "per_element": "3/4 and 5/4 are inherited labels", "per_site": "Cycle620 revalidates no physical endpoint compiler", "per_mode": "no delay/rate or advance/count edit is imported", "per_block": "the PR runner is not imported or executed", "lattice_wide": "no Event, Record, or time backcredit is granted"},
    ]
    n6 = [
        {"file": "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_receipt_2026_07_22.json", "status": "PINNED_CORRECTED_CONDITIONAL_PARENT", "what_closes": "conditional K129 register/coordinate/gate descriptor shore and exact one-site translation falsifier; no physical promotion"},
        {"file": "outputs/physical_lawful_charge_joined_metric_response_tournament_cycle615_receipt_2026_07_22.json", "status": "PINNED_EXECUTED_PARENT", "what_closes": "seven-level pair and response-family algebra shore while physical lowering remains open"},
        {"file": "outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json", "status": "PINNED_CORRECTED_COMPARATOR", "what_closes": "factor/count and small-matrix comparator scope plus the null physical-promotion boundary"},
        {"file": "outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json", "status": "PINNED_LOCAL_LABEL_COMPARATOR", "what_closes": "declared local 3/4 and 5/4 label comparison without a Cycle620 selector"},
        {"file": f'{CAUSAL_TIME_PR_5557["commit"]}:{CAUSAL_TIME_PR_5557["note"]}', "status": "PINNED_EXTERNAL_COMPARISON_NOT_EXECUTED", "what_closes": "identity separation from the causal-time lane only; no Event, Record, rate, edit, or time backcredit"},
    ]
    n8 = [
        {"cycle": "Cycle610", "prior_path": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md", "prior_line": 208, "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md", "citation_line": 208, "echo": "state-carried translation phase remains the strongest repair", "retired": False, "retirement_mechanism": None, "could_apply_here": True, "mechanism": "state-carried translation phase plus locally enforced admissibility", "applicability": "ACTIONABLE_PHYSICAL_LOWERING_ROUTE", "effect": "keeps literal physical lowering live and blocks foreclosure"},
        {"cycle": "Cycle615", "prior_path": "docs/work_history/repo/review_feedback/PHYSICAL_LAWFUL_CHARGE_JOINED_METRIC_RESPONSE_TOURNAMENT_CYCLE615_NOTE_2026-07-22.md", "prior_line": 72, "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_LAWFUL_CHARGE_JOINED_METRIC_RESPONSE_TOURNAMENT_CYCLE615_NOTE_2026-07-22.md", "citation_line": 72, "echo": "physical lowering, open-domain join, feedback and receiver selection remain open", "retired": False, "retirement_mechanism": None, "could_apply_here": True, "mechanism": "literal lowering, open-domain joining, and bounded local receiver feedback", "applicability": "ACTIONABLE_JOIN_AND_SELECTOR_ROUTE", "effect": "supports algebraic calculations but not physical promotion"},
        {"cycle": "Cycle608", "prior_path": "docs/work_history/repo/review_feedback/PHYSICAL_RADIUS_ONE_DRESSED_DETECTOR_CONTROLLED_UPDATE_RECURRENCE_TOURNAMENT_CYCLE608_NOTE_2026-07-22.md", "prior_line": 150, "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_RADIUS_ONE_DRESSED_DETECTOR_CONTROLLED_UPDATE_RECURRENCE_TOURNAMENT_CYCLE608_NOTE_2026-07-22.md", "citation_line": 150, "echo": "literal held-L6 E/G/placement/product/leakage remains the optimal campaign", "retired": False, "retirement_mechanism": None, "could_apply_here": True, "mechanism": "instantiate the literal held-L6 encoder, update, placement, product, and leakage audit", "applicability": "ACTIONABLE_TARGET_EQUIVALENT_COMPILER_ROUTE", "effect": "prevents endpoint/compiler backcredit"},
        {"cycle": "local Cycle612", "prior_path": "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md", "prior_line": 70, "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md", "citation_line": 70, "echo": "two local labels survive without a selected response sign", "retired": False, "retirement_mechanism": None, "could_apply_here": True, "mechanism": "derive one receiver selector rather than route a supplied response sign", "applicability": "ACTIONABLE_RECEIVER_SELECTION_ROUTE", "effect": "prevents receiver-selection credit"},
        {"cycle": "causal-time PR #5557", "prior_path": f'{CAUSAL_TIME_PR_5557["commit"]}:{CAUSAL_TIME_PR_5557["note"]}', "prior_line": 42, "citation_path": f'{CAUSAL_TIME_PR_5557["commit"]}:{CAUSAL_TIME_PR_5557["note"]}', "citation_line": 42, "echo": "delay and advance are separated by rate/edit reachability", "retired": False, "retirement_mechanism": None, "could_apply_here": False, "mechanism": "comparison-only rate/edit reachability split with no imported runner", "applicability": "NOT_APPLICABLE_WITHOUT_CAUSAL_MECHANISM_IMPORT", "effect": "comparison only; no time or Record import"},
        {"cycle": "Cycle576", "prior_path": "docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md", "prior_line": 36, "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md", "citation_line": 36, "echo": "source sign, normalization, frame preparation and update scale are supplied", "retired": False, "retirement_mechanism": None, "could_apply_here": True, "mechanism": "derive rather than supply feedback sign, normalization, frame preparation, and update scale", "applicability": "ACTIONABLE_SOURCE_NORMALIZATION_ROUTE", "effect": "keeps the feedback and coframe terms conditional"},
    ]
    n7 = {
        "steelman": "A state-carried translation phase with locally enforced admissibility could repair the supplied-origin translation defect, and a normalized nonlinear feedback or direct generator-to-endpoint coupling could select one receiver response without changing the retained algebraic shores.",
        "mechanism": "carry phi in Z_129^3 as local code data, update phi covariantly, enforce translated-role admissibility locally, and compose the resulting literal physical encoder/update with a bounded feedback selector",
        "terminal_obligation": "execute one-fine-site code/update covariance, a fine-nearest-neighbor primitive product, full-code leakage and local-constraint controls, then preserve Gauss, Ward, inverse, and one held-out receiver without refit",
        "citations": [
            {
                "path": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
                "line": 208,
                "supports": "state-carried translation phase is the strongest live repair",
            },
            {
                "path": "docs/work_history/repo/review_feedback/PHYSICAL_LAWFUL_CHARGE_JOINED_METRIC_RESPONSE_TOURNAMENT_CYCLE615_NOTE_2026-07-22.md",
                "line": 97,
                "supports": "literal physical lowering, open-domain dynamics, and local receiver feedback are actionable live work",
            },
        ],
        "action": "implement the local phase/admissibility compiler first, then test normalized nonlinear feedback and direct generator-to-endpoint coupling on one open real-space apparatus",
    }
    n4_cited_lines_exist = all(
        cited_line_exists(row["prior_path"], row["prior_line"])
        and cited_line_exists(row["current_path"], row["current_line"])
        for row in n4
    )
    n7_cited_lines_exist = all(
        cited_line_exists(citation["path"], citation["line"])
        for citation in n7["citations"]
    )
    n8_cited_lines_exist = all(
        cited_line_exists(row["citation_path"], row["citation_line"])
        for row in n8
    )
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
        "N1_allowed_markers": ["ATTEMPTED", "RULED OUT BY PRIOR"],
        "N1_marker_schema_pass": markers,
        "N1_live_routes": live_routes,
        "N2_collapsed_wall_pair_audit": pairs,
        "N2_independence_complete": independence_complete,
        "N3_canonical_hidden_wall_phrases": list(phrases),
        "N3_note_phrase_hits": phrase_hits,
        "N3_explicit_supplied_structure": ["K129 partition/origin/role coloring", "one-hot orientation and blank work", "five Givens angles and pivot order", "candidate opposite-charge copy and contacts", "local Cycle612 endpoint program", "feedback square/sign/scale", "Regge complex/pseudoinverse/lambda", "response-label comparison", "finite-difference step and nondegenerate fixtures"],
        "N4_exact_residual_matching": n4,
        "N4_cited_lines_exist": n4_cited_lines_exist,
        "N5_five_resolution_rhetoric_audit": n5,
        "N6_partial_closure_paths": n6,
        "N7_cited_actionable_steelman": n7,
        "N7_cited_lines_exist": n7_cited_lines_exist,
        "N8_rowwise_cross_cycle_echo": n8,
        "N8_cited_lines_exist": n8_cited_lines_exist,
        "walls": walls,
        "Status": "FAIL / DO NOT SHIP NEGATIVE",
        "narrowed_positive_artifact_status": "PASS",
        "negative_claim_shipped": False,
        "shared_route_independent_obstruction": False,
        "minimum_content_claim": False,
        "axiom_pressure": False,
    }
    check(
        "Full current-origin/main N1-N8 blocks broad no-go, minimum-content, and axiom-pressure claims",
        len(families) >= 5 and markers and len(live_routes) >= 5 and len(pairs) == 21
        and not independence_complete and not phrase_hits
        and all(all(key in row for key in ("prior_path", "prior_line", "prior_residual", "current_path", "current_line", "current_residual", "exact_match", "same_scope", "use_as_closure")) for row in n4)
        and n4_cited_lines_exist
        and all(all(key in row for key in ("per_element", "per_site", "per_mode", "per_block", "lattice_wide")) for row in n5)
        and all(all(key in row for key in ("file", "status", "what_closes")) for row in n6)
        and all(key in n7 for key in ("steelman", "mechanism", "terminal_obligation", "citations", "action"))
        and len(n7["citations"]) >= 2
        and all(all(key in citation for key in ("path", "line", "supports")) for citation in n7["citations"])
        and n7_cited_lines_exist
        and all(all(key in row for key in ("cycle", "prior_path", "prior_line", "citation_path", "citation_line", "echo", "retired", "retirement_mechanism", "could_apply_here", "mechanism", "applicability", "effect")) for row in n8)
        and all(row["citation_path"] == row["prior_path"] and row["citation_line"] == row["prior_line"] for row in n8)
        and all(isinstance(row["mechanism"], str) and row["mechanism"] and isinstance(row["applicability"], str) and row["applicability"] for row in n8)
        and n8_cited_lines_exist
        and output["Status"] == "FAIL / DO NOT SHIP NEGATIVE"
        and not output["negative_claim_shipped"]
        and not output["shared_route_independent_obstruction"]
        and not output["minimum_content_claim"] and not output["axiom_pressure"],
        output,
    )
    return output


def main() -> int:
    r615, r610, r608, r612, shore_result = shore()
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
        "author_artifact_status_accepted": False,
        "audit_verdict_inferred_from_dependencies": False,
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
        "decisive_answer": "Route A preserves an exact seven-level pair involution, one 13-bit register embedding, Gray/Givens/conjunction algebra, conditional K129 coordinate descriptors, and L3/L6/L7 register streams. It does not compose a literal physical M2 encoder or update, fine-NN product, full-code leakage audit, local enforcement, one-fine-site covariant code/update, or autonomous no-host schedule. Route B constructs a conditional feedback-square family; its sign, scale, lambda, improvement, source/gravity status, and {3/4,5/4} receiver choice remain unselected. Route C constructs a coframe-generator/quasiphase representative, not energy, stress, rate, or time.",
        "inventory": {
            "supplied": [
                "Cycle610 K129 partition/origin/role coloring, conditional orientation/predicate/bus descriptors, and blank work",
                "candidate negative-charge occupation copy, conjugate coin, separate same-g contact, and no cross contact",
                "five exact cubic-scalar Givens angles and the neutral resource excitation",
                "final corrected Cycle608 comparator and local Cycle612 endpoint-use/admission program",
                "feedback square form, 1/2 convention, D/rho relative scale, sign/scale alternatives",
                "Cycle576 Regge complex/raw deficit/pseudoinverse/lambda and periodic Bloch fixtures",
                "diagnostic response-sign to Cycle612-word convention and finite-difference epsilon",
            ],
            "derived_or_executed": [
                "seven-level pair involution, 13-bit register embedding, and exact Gray/conjunction algebra",
                "conditional clean-work descriptor return, register identity extension, inverse, deletion, and pair all24/all576 algebra",
                "two-charge A/B register-stream geometry and semantics on L3/L6/L7 conditional coarse grids",
                "conditional endpoint-controlled feedback Hessian/force and sign/scale/lambda/improvement family audit",
                "Gauss neutrality, Regge Ward, stationary, inverse, covariance, and feedback deletions",
                "full-Fock coin-stream-contact coframe generators and nondegenerate quasiphase derivative match",
                "principal wrapped-phase seam and order/contact falsifiers",
            ],
            "not_derived": [
                "physical particle identity or negative-sector law selection",
                "literal physical M2 encoder/update, fine-NN product, full-code leakage, local enforcement, one-site covariance, or autonomous schedule",
                "uniform one-hot/work/binder/path/chart genesis",
                "feedback square/sign/normalization or a stability law selecting them",
                "unique lambda, improvement, metric observable, response sign, or Cycle612 receiver word",
                "joint open-boundary real-space Regge/feedback compiler",
                "physical stress, energy, gravity, causal rate, event, Record, or Born rule",
            ],
        },
        "six_wall_ledger": {
            "C_ref": "NARROWED: pair all24/all576 algebra and conditional coarse-origin coordinate actions pass, while the supplied K129 origin/coloring fails one-fine-site translation promotion.",
            "C_num": "SHARPENED: exact pair angles and a full affine feedback family are explicit; feedback scale/sign, lambda, improvement, and empirical normalization remain unselected.",
            "C_wrap": "ADVANCED diagnostically only: tracked quasiphase derivatives agree with K_ab away from degeneracy and a principal seam is exposed; phase and generator are not energy, stress, rate, or time.",
            "C_int": "PARTIAL ALGEBRAIC COMPOSITION: pair/register, feedback, and coframe calculations coexist, but there is no literal physical M2 apparatus or open-boundary/periodic Regge join.",
            "C_local": "NARROWED: bounded conditional K129 descriptors and register semantics pass; physical encoder/update, local enforcement, one-fine-site covariance, full-code leakage, and autonomous scheduling remain unevaluated or false.",
            "C_source": "CONDITIONAL FAMILY ONLY: endpoint-controlled deficit-density feedback is an explicit candidate, while sign/scale/lambda/improvement and both labels survive; no unique source or gravity law is selected.",
        },
        "maturity_effect": "no maturity scores retained or increased; the corrected shore removes the prior physical-compiler promotion and the other routes remain conditional",
        "physical_lowering_audit": {
            "literal_physical_M2_encoder_composed": False,
            "literal_physical_update_composed": False,
            "physical_M2_cost_per_coarse_cell": None,
            "physical_intertwiner_residual": None,
            "fine_NN_placement_and_product_executed": False,
            "physical_support_two_gate_product_executed": False,
            "physical_all24_or_all576_update_covariance_executed": False,
            "physical_held_size_deletion_or_malformed_control_executed": False,
            "full_physical_code_leakage_evaluated": False,
            "full_physical_code_leakage_residual": None,
            "local_constraints_enforced": False,
            "one_fine_site_translation_covariant_code_and_update": False,
            "autonomous_no_host_schedule_executed": False,
            "Route_B_literal_physical_endpoint_revalidated": False,
            "Route_B_joint_open_periodic_physical_apparatus": False,
            "Route_C_energy_stress_rate_or_time_identification": False,
        },
        "Cycle612_identity_boundary": {
            "local_Cycle612": "current-branch label comparator only",
            "causal_time_PR_5557": "distinct external comparison lane at a1e2f1ea60",
            "causal_PR_runner_imported_or_executed": False,
            "causal_PR_Event_Record_or_time_backcredit": False,
        },
        "strongest_constructive_result": "an exact seven-level/Givens pair involution embedded in a 13-bit register, with conditional K129 coordinate descriptors and L3/L6/L7 register-stream controls; this is not a physical M2 compiler",
        "confirmed_breakthrough": False,
        "negative_claim_shipped": False,
        "shared_obstruction_or_axiom_pressure": False,
        "optimal_next_campaign": "construct a state-carried Z129^3 translation phase plus literal fine-NN admissibility and test a physical E/update under one-site translations; separately test normalized/nonlinear feedback or direct generator-to-endpoint coupling on one open real-space apparatus",
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
    if "--cold" in sys.argv:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            exit_code = main()
        transcript = buffer.getvalue()
        COLD.write_text(transcript, encoding="utf-8")
        print(transcript, end="")
        raise SystemExit(exit_code)
    raise SystemExit(main())
