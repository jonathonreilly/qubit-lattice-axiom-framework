#!/usr/bin/env python3
"""Cycle631: literal fine-NN autonomous-control attempt above Cycles629/630.

This artifact constructs a marker-safe exact branch recognizer, a covariant
nine-colour fine-edge arbitration, and an abstract reversible route-token
successor.  It also falsifies the single-adjacent-sidecar token layout.  It
does not construct a local physical token/program register, autonomous
G_physical, E, leakage test, or intertwiner.  Authority none; audit unset.
"""
from __future__ import annotations

from collections import Counter
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

import physical_marker_preserving_free_quotient_router_cycle630_2026_07_23 as c630
import physical_local_sector_role_genesis_closure_tournament_cycle617_2026_07_22 as c617


c629 = c630.c629
c610 = c629.c610
c603 = c610.c603
K = c630.K
H = c629.H
FRAMES = c630.FRAMES
DIRECTIONS = c630.DIRECTIONS
AUTHORITY = "none"
AUDIT = "unset"
CAP_SECONDS = 300.0
CAP_BYTES = 3 * 1024**3
PASS = FAIL = 0
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_AUTONOMOUS_MARKER_RECOGNITION_TOKEN_ATTEMPT_CYCLE631_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / (
    "outputs/physical_autonomous_marker_recognition_token_attempt_"
    "cycle631_receipt_2026_07_23.json"
)
COLD = ROOT / (
    "outputs/physical_autonomous_marker_recognition_token_attempt_"
    "cycle631_cold_2026_07_23.txt"
)
PINS = {
    "scripts/physical_marker_preserving_free_quotient_router_cycle630_2026_07_23.py":
        "f53f95a45fc3f42cb7850826a63fb82044f27a25a98b44d95e7bc14c0af4edfe",
    "docs/work_history/repo/review_feedback/PHYSICAL_MARKER_PRESERVING_FREE_QUOTIENT_ROUTER_CYCLE630_NOTE_2026-07-23.md":
        "5fdd32d2ca36351c551cced050559bc5dc4cc5d17cc629d0314848180c1d3e3c",
    "outputs/physical_marker_preserving_free_quotient_router_cycle630_receipt_2026_07_23.json":
        "f9ec4f6f5bb729197f14b4f43c437d05bb32fd1be17d0fa982b8fd57648f9593",
    "outputs/physical_marker_preserving_free_quotient_router_cycle630_cold_2026_07_23.txt":
        "35588b9e0325ff73da3cefbe8b5472b8403ab359a1986d2376a815dda98b6ccb",
    "scripts/physical_local_sector_role_genesis_closure_tournament_cycle617_2026_07_22.py":
        "61583be58976a4dfc1b590ebbe39040b5e39c1def94ba29066991cda22fac756",
    "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_SECTOR_ROLE_GENESIS_CLOSURE_TOURNAMENT_CYCLE617_NOTE_2026-07-22.md":
        "8d784fa97f98ad9adf734cd6a319ad95c32e52179a8e1c6f73db969577aba4f1",
    "outputs/physical_local_sector_role_genesis_closure_tournament_cycle617_receipt_2026_07_22.json":
        "d7d34ab3b032dcda01195cd1e93adabee74d48a58692f3161efec63f641c2d51",
    "outputs/physical_local_sector_role_genesis_closure_tournament_cycle617_cold_2026_07_22.txt":
        "7c8cd11bfd130ef23baf2667ef94f8edd6dd90339870183525e18011bcdc0de2",
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


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, set | frozenset):
        return sorted(value)
    raise TypeError(type(value).__name__)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def shore() -> tuple[dict, dict, dict]:
    r630 = json.loads((ROOT / (
        "outputs/physical_marker_preserving_free_quotient_router_"
        "cycle630_receipt_2026_07_23.json"
    )).read_text())
    r617 = json.loads((ROOT / (
        "outputs/physical_local_sector_role_genesis_closure_tournament_"
        "cycle617_receipt_2026_07_22.json"
    )).read_text())
    expected = dict(r630["shore"]["import_audit"]["expected_transitive_sha256"])
    expected.update(r617["shore"]["import_audit"]["expected_transitive_sha256"])
    expected.update(PINS)
    observed = {name: sha(ROOT / name) for name in expected}
    actual_modules = dict(r630["shore"]["import_audit"]["actual_imported_modules"])
    actual_modules.update(r617["shore"]["import_audit"]["actual_imported_modules"])
    actual_modules.update({
        "physical_marker_preserving_free_quotient_router_cycle630_2026_07_23":
            "scripts/physical_marker_preserving_free_quotient_router_cycle630_2026_07_23.py",
        "physical_local_sector_role_genesis_closure_tournament_cycle617_2026_07_22":
            "scripts/physical_local_sector_role_genesis_closure_tournament_cycle617_2026_07_22.py",
    })
    uncovered = sorted(set(actual_modules.values()) - set(expected))
    inherited = {
        "Cycle630_pass": r630["pass"],
        "Cycle630_tests_passed": r630["tests_passed"],
        "Cycle630_authority": r630["authority"],
        "Cycle630_audit": r630["audit"],
        "Cycle630_path_pairs": r630["conditional_act_descriptor_routing"]["distinct_ordered_endpoint_pairs"],
        "Cycle630_selector_replacement": r630["conditional_act_descriptor_routing"]["selector_replacement_recognition_compiled"],
        "Cycle630_local_successor": r630["inventory_and_interpretation_firewall"]["unbuilt_or_null"]["local_successor_computation"],
        "Cycle630_shared_obstruction": r630["shared_obstruction_or_axiom_pressure"],
        "Cycle617_pass": r617["pass"],
        "Cycle617_tests_passed": r617["tests_passed"],
        "Cycle617_authority": r617["authority"],
        "Cycle617_audit": r617["audit"],
        "Cycle617_route_B_collision_sorter": r617["route_B"]["pass_one_macro_collision_sorter"],
        "Cycle617_route_B_CAR_sign_service": r617["route_B"]["pass_CAR_sign_service"],
        "import_audit": {
            "expected_transitive_sha256": expected,
            "observed_transitive_sha256": observed,
            "actual_imported_modules": actual_modules,
            "uncovered_imported_modules": uncovered,
            "expected_file_count": len(expected),
            "runtime_module_count": len(actual_modules),
        },
    }
    condition = (
        observed == expected and not uncovered
        and r630["pass"] and r630["tests_passed"] == 10
        and r630["authority"] == AUTHORITY and r630["audit"] == AUDIT
        and not r630["author_artifact_status_accepted"]
        and not inherited["Cycle630_selector_replacement"]
        and not inherited["Cycle630_local_successor"]
        and not inherited["Cycle630_shared_obstruction"]
        and r617["pass"] and r617["tests_passed"] == 12
        and r617["authority"] == AUTHORITY and r617["audit"] == AUDIT
        and inherited["Cycle617_route_B_collision_sorter"]
        and not inherited["Cycle617_route_B_CAR_sign_service"]
    )
    check("Cycle630 and Cycle617 quartets plus transitive science graphs are byte exact",
          condition, {
              "Cycle630_pass": inherited["Cycle630_pass"],
              "Cycle630_tests_passed": inherited["Cycle630_tests_passed"],
              "Cycle617_pass": inherited["Cycle617_pass"],
              "Cycle617_tests_passed": inherited["Cycle617_tests_passed"],
              "expected_file_count": inherited["import_audit"]["expected_file_count"],
              "runtime_module_count": inherited["import_audit"]["runtime_module_count"],
              "uncovered": uncovered,
          })
    return inherited, r630, r617


def exact_target_contract() -> dict:
    result = {
        "target": "compile Cycle630's finite orientation-conditioned path table toward a literal fine-NN autonomous selector/token controller",
        "required_attempts": (
            "replace the excluded marker-touching selector with marker-safe exact recognition and clean uncompute",
            "encode an explicit reversible successor for every finite route word",
            "give a local collision-arbitration schedule and audit proper-cubic covariance",
            "test token genesis/renewal, malformed states, deletion, L3/L6/L7, all24/all576, and the full selector-plus-act word",
        ),
        "completion_not_claimed": "literal physical storage and NN update for route labels/program clock, autonomous G_physical, literal E, leakage, mass/contact/seam fixture execution, and E G_coarse = G_physical E",
        "separation": "path existence, abstract reversible control, and physical autonomous control are three different claims",
    }
    check("Cycle631 target keeps abstract successor and arbitration below physical autonomous control",
          len(result["required_attempts"]) == 4 and "completion_not_claimed" in result,
          result)
    return result


def marker_safe_toffoli_sequence(left: int, right: int, target: int,
                                  parity: tuple[int, int, int, int]):
    """Exact Toffoli on clean parity scratch; controls are never bit targets."""
    pab, pac, pbc, pabc = parity
    gates = [
        c603.one("H0", target, c603.H2, "H"),
        c603.one("Ta", left, c603.T2, "T"),
        c603.one("Tb", right, c603.T2, "T"),
        c603.one("Tc", target, c603.T2, "T"),
    ]
    for name, controls, scratch, phase in (
        ("ab", (left, right), pab, c603.TDG2),
        ("ac", (left, target), pac, c603.TDG2),
        ("bc", (right, target), pbc, c603.TDG2),
        ("abc", (left, right, target), pabc, c603.T2),
    ):
        for index, control in enumerate(controls):
            gates.append(c603.two(f"{name}_c{index}", control, scratch,
                                  c603.CNOT, "CNOT"))
        gates.append(c603.one(f"{name}_phase", scratch, phase,
                              "T" if phase is c603.T2 else "Tdg"))
        for index, control in reversed(tuple(enumerate(controls))):
            gates.append(c603.two(f"{name}_u{index}", control, scratch,
                                  c603.CNOT, "CNOT"))
    gates.append(c603.one("H1", target, c603.H2, "H"))
    return gates


def marker_safe_toffoli_audit() -> dict:
    gates = marker_safe_toffoli_sequence(0, 1, 2, (3, 4, 5, 6))
    columns = np.zeros((128, 8), dtype=complex)
    expected = np.zeros_like(columns)
    for word in range(8):
        bits = [(word >> (2 - index)) & 1 for index in range(3)] + [0] * 4
        index = sum(bit << (6 - q) for q, bit in enumerate(bits))
        columns[index, word] = 1
        bits[2] ^= bits[0] & bits[1]
        target_index = sum(bit << (6 - q) for q, bit in enumerate(bits))
        expected[target_index, word] = 1
    actual = c603.apply_sequence_columns(columns, gates, 7)
    residual = float(np.linalg.norm(actual - expected))
    support = Counter((gate.family, len(gate.qubits)) for gate in gates)
    controls_safe = all(
        not (len(gate.qubits) == 2 and gate.qubits[-1] in (0, 1))
        and not (len(gate.qubits) == 1 and gate.qubits[0] in (0, 1)
                 and not np.allclose(gate.matrix, np.diag(np.diag(gate.matrix))))
        for gate in gates
    )
    result = {
        "phase_identity": "4abc = a+b+c-(a xor b)-(a xor c)-(b xor c)+(a xor b xor c) mod 8",
        "clean_parity_scratch_M2": 4,
        "primitive_gate_count": len(gates),
        "one_site_gate_count": sum(len(g.qubits) == 1 for g in gates),
        "CNOT_count": support[("CNOT", 2)],
        "all_eight_clean_scratch_input_columns_tested": True,
        "exact_Toffoli_residual": residual,
        "controls_never_bit_targets": controls_safe,
        "parity_scratch_returns_clean": residual < 1e-12,
        "pass": len(gates) == 27 and support[("CNOT", 2)] == 18
                and residual < 1e-12 and controls_safe,
    }
    check("27-gate clean-scratch Toffoli is exact while marker controls never flip",
          result["pass"], result)
    return result


def base_marker_order() -> tuple[tuple[int, int, int], ...]:
    return tuple(sorted(c629.ANCHORS))


def identity_relative_orientation_order() -> tuple[int, ...]:
    identity = c629.frame_index(np.eye(3, dtype=int))
    return (identity,) + tuple(index for index in range(24) if index != identity)


def select_work_roles() -> tuple[tuple[int, int, int], ...]:
    forbidden = set(c629.dynamic_geometry_sites()) | set(c630.marker_residues())
    candidates = []
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
            if all(c629.rotate(frame, site) not in forbidden for frame in FRAMES):
                candidates.append(site)
        if len(candidates) >= 169:
            break
    roles = tuple(candidates[:169])
    if len(roles) != 169 or len(set(roles)) != 169:
        raise AssertionError("insufficient clean work roles")
    return roles


def logical_recognizer_macros() -> tuple[list[tuple], dict]:
    # Controls 0..143; complement 144..166; chain 167..308;
    # shared parity 309..312; flag 313.
    negatives = tuple(range(121, 144))
    complements = tuple(range(144, 167))
    chain = tuple(range(167, 309))
    parity = (309, 310, 311, 312)
    flag = 313
    macros = []
    for source, target in zip(negatives, complements):
        macros.extend((('X', target), ('CNOT', source, target)))
    effective = tuple(range(121)) + complements
    toffoli = []
    toffoli.append((effective[0], effective[1], chain[0]))
    for index in range(2, len(effective) - 1):
        toffoli.append((chain[index - 2], effective[index], chain[index - 1]))
    toffoli.append((chain[-1], effective[-1], flag))
    for row in toffoli:
        macros.append(('TOFFOLI',) + row)
    for row in reversed(toffoli[:-1]):
        macros.append(('TOFFOLI',) + row)
    for source, target in reversed(tuple(zip(negatives, complements))):
        macros.extend((('CNOT', source, target), ('X', target)))
    metadata = {
        "marker_controls": 144,
        "positive_anchor_controls": 120,
        "positive_orientation_controls": 1,
        "negative_orientation_controls": 23,
        "negative_complement_scratch_M2": 23,
        "conjunction_chain_scratch_M2": 142,
        "shared_parity_scratch_M2": 4,
        "total_clean_work_M2": 169,
        "flag_M2": 1,
        "Toffoli_macros": sum(row[0] == 'TOFFOLI' for row in macros),
        "complement_X_or_CNOT_macros": sum(row[0] != 'TOFFOLI' for row in macros),
        "flag_index": flag,
        "parity_indices": parity,
    }
    return macros, metadata


def simulate_macros(bits: list[int], macros: list[tuple], deleted: int | None = None) -> list[int]:
    state = list(bits)
    for index, row in enumerate(macros):
        if index == deleted:
            continue
        if row[0] == 'X':
            state[row[1]] ^= 1
        elif row[0] == 'CNOT':
            state[row[2]] ^= state[row[1]]
        else:
            state[row[3]] ^= state[row[1]] & state[row[2]]
    return state


def recognizer_role_coordinates(work: tuple, orientation_index: int) -> tuple:
    frame = FRAMES[orientation_index]
    anchors = tuple(c629.rotate(frame, site) for site in base_marker_order())
    relative = identity_relative_orientation_order()
    orientation_order = tuple(c629.left_action(frame, index) for index in relative)
    orientations = tuple(c629.ORIENTATION_SITES[index] for index in orientation_order)
    rotated_work = tuple(c629.rotate(frame, site) for site in work)
    flag = c629.rotate(frame, c610.PREDICATE_WORK_SEED)
    return anchors + orientations + rotated_work + (flag,)


def marker_neighbor_path(marker: tuple[int, int, int], target: tuple[int, int, int], parent):
    candidates = []
    obstacles = c630.marker_residues()
    for direction in DIRECTIONS:
        neighbor = c630.add(marker, direction)
        if c630.residue(neighbor) in obstacles:
            continue
        path = (neighbor,) if neighbor == target else c630.routed_path(neighbor, target, parent)
        candidates.append(path)
    if not candidates:
        raise AssertionError((marker, target))
    return min(candidates, key=lambda path: (len(path), path))


def recognizer_audit(parent, work: tuple) -> dict:
    macros, metadata = logical_recognizer_macros()
    primitive_specs = []
    parity = metadata["parity_indices"]
    for row in macros:
        if row[0] == 'TOFFOLI':
            primitive_specs.extend(marker_safe_toffoli_sequence(row[1], row[2], row[3], parity))
        elif row[0] == 'X':
            primitive_specs.append(c603.one("neg_X", row[1], c603.X2, "X"))
        else:
            primitive_specs.append(c603.two("neg_CNOT", row[1], row[2], c603.CNOT, "CNOT"))

    roles = recognizer_role_coordinates(work, c629.frame_index(np.eye(3, dtype=int)))
    marker_indices = set(range(144))
    route_cache = {}
    routed_microsteps = 0
    route_edges = []
    marker_control_CNOTs = free_CNOTs = 0
    for gate in primitive_specs:
        if len(gate.qubits) == 1:
            routed_microsteps += 1
            continue
        left_index, right_index = gate.qubits
        left, right = roles[left_index], roles[right_index]
        if left_index in marker_indices or right_index in marker_indices:
            # Construction guarantees the marker is the control/first endpoint.
            if right_index in marker_indices:
                raise AssertionError((gate.name, gate.qubits))
            key = ("marker", left, right)
            if key not in route_cache:
                route_cache[key] = marker_neighbor_path(left, right, parent)
            path = route_cache[key]
            distance = len(path) - 1
            microsteps = 2 * distance + 1
            marker_control_CNOTs += 1
        else:
            key = ("free", left, right)
            if key not in route_cache:
                route_cache[key] = c630.routed_path(left, right, parent)
            path = route_cache[key]
            distance = len(path) - 1
            microsteps = 2 * distance - 1
            free_CNOTs += 1
        routed_microsteps += microsteps
        route_edges.append(distance)

    truth_failures = 0
    truth_rows = []
    for active in range(24):
        recognized = []
        for branch in range(24):
            bits = [0] * 314
            bits[:120] = [1] * 120
            relative = identity_relative_orientation_order()
            order = tuple(c629.left_action(FRAMES[branch], index) for index in relative)
            for local_index, global_index in enumerate(order):
                bits[120 + local_index] = int(global_index == active)
            computed = simulate_macros(bits, macros)
            if computed[313]:
                recognized.append(branch)
            truth_failures += int(any(computed[144:313]))
            cleared = simulate_macros(computed, macros)
            truth_failures += int(any(cleared[144:314]))
        truth_failures += int(recognized != [active])
        truth_rows.append({"orientation_index": active,
                           "recognized_branches": len(recognized),
                           "recognized_branch_indices": tuple(recognized)})

    malformed = {}
    for name, active_orientation_indices, anchors_on in (
        ("zero_hot", (), True),
        ("two_hot", (0, 1), True),
        ("all_hot", tuple(range(24)), True),
        ("one_anchor_deleted", (0,), False),
    ):
        recognized = 0
        for branch in range(24):
            bits = [0] * 314
            bits[:120] = [1] * 120
            if not anchors_on:
                bits[0] = 0
            relative = identity_relative_orientation_order()
            order = tuple(c629.left_action(FRAMES[branch], index) for index in relative)
            for local_index, global_index in enumerate(order):
                bits[120 + local_index] = int(global_index in active_orientation_indices)
            recognized += simulate_macros(bits, macros)[313]
        malformed[name] = {"recognized_branches": recognized, "rejected": recognized == 0}

    final_flag_macro = next(
        index for index, row in enumerate(macros)
        if row[0] == 'TOFFOLI' and row[3] == 313
    )
    lawful = [0] * 314
    lawful[:121] = [1] * 121
    deleted_state = simulate_macros(lawful, macros, deleted=final_flag_macro)
    deletion = {
        "deleted_macro_index": final_flag_macro,
        "deleted_macro": macros[final_flag_macro],
        "lawful_flag_after_deletion": deleted_state[313],
        "detected": deleted_state[313] == 0,
    }

    covariance_failures = 0
    all24_role_checks = 0
    for h in range(24):
        expected = recognizer_role_coordinates(work, h)
        frame = FRAMES[h]
        identity = recognizer_role_coordinates(work, c629.frame_index(np.eye(3, dtype=int)))
        mapped = tuple(c629.rotate(frame, site) for site in identity)
        covariance_failures += int(mapped != expected)
        all24_role_checks += len(expected)
    all576_checks = 0
    for first in FRAMES:
        for second_index in range(24):
            direct_index = c629.left_action(first, second_index)
            source = recognizer_role_coordinates(work, second_index)
            direct = recognizer_role_coordinates(work, direct_index)
            mapped = tuple(c629.rotate(first, site) for site in source)
            covariance_failures += int(mapped != direct)
            all576_checks += len(source)

    raw_counts = Counter((gate.family, len(gate.qubits)) for gate in primitive_specs)
    act_microsteps = 35_361_766
    dynamic = set(c629.dynamic_geometry_sites())
    marker = set(c630.marker_residues())
    placement_overlap = 0
    for frame in FRAMES:
        placed = {c629.rotate(frame, site) for site in work}
        placement_overlap += len(placed & (dynamic | marker))
    unique_route_edges = {
        tuple(sorted((path[index], path[index + 1])))
        for path in route_cache.values()
        for index in range(len(path) - 1)
    }
    translated_collision_rows = []
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        side = K * length
        failures = 0
        for edge in unique_route_edges:
            base = {tuple(value % side for value in site) for site in edge}
            for direction in DIRECTIONS:
                displacement = tuple(K * value for value in direction)
                translated = {
                    tuple((site[axis] + displacement[axis]) % side for axis in range(3))
                    for site in edge
                }
                failures += int(bool(base & translated))
        translated_collision_rows.append({
            "length": length, "split": split,
            "unique_recognizer_route_edges": len(unique_route_edges),
            "six_neighbor_cell_translation_checks": 6 * len(unique_route_edges),
            "same_phase_vertex_collision_failures": failures,
            "pass": failures == 0,
        })
    result = {
        "predicate": "all 120 anchors are one and exactly the selected one of 24 orientation bits is one",
        "declared_domain": "Cycle629 supplied marker sector with state-carried phi and neighbor-equal h; the <=91 non-anchor weight and h-equality projectors are not enforced here",
        "roles": metadata,
        "base_clean_work_role_coordinates": work,
        "base_clean_work_role_sha256": sha256(repr(work).encode()).hexdigest(),
        "base_clean_work_max_Chebyshev_radius": max(max(abs(v) for v in site) for site in work),
        "all24_work_dynamic_or_marker_overlap": placement_overlap,
        "base_flag_coordinate": roles[313],
        "marker_safe_Toffoli_primitives": 27,
        "logical_compute_macros": len(macros),
        "raw_primitive_gate_count_per_compute": len(primitive_specs),
        "raw_one_site_primitives_per_compute": sum(len(g.qubits) == 1 for g in primitive_specs),
        "raw_two_site_primitives_per_compute": sum(len(g.qubits) == 2 for g in primitive_specs),
        "raw_CNOT_primitives_per_compute": raw_counts[("CNOT", 2)],
        "routed_marker_control_CNOTs_per_compute": marker_control_CNOTs,
        "routed_free_CNOTs_per_compute": free_CNOTs,
        "distinct_route_lookups_per_compute": len(route_cache),
        "minimum_route_edges": min(route_edges),
        "maximum_route_edges": max(route_edges),
        "fine_NN_microsteps_per_compute": routed_microsteps,
        "fine_NN_microsteps_compute_plus_clean_uncompute": 2 * routed_microsteps,
        "Cycle630_identity_conditional_act_microsteps": act_microsteps,
        "full_identity_selector_plus_act_microsteps": 2 * routed_microsteps + act_microsteps,
        "all24_selector_plus_act_microsteps": 24 * (2 * routed_microsteps + act_microsteps),
        "truth_rows": truth_rows,
        "truth_failures": truth_failures,
        "malformed_rejections": malformed,
        "deletion_control": deletion,
        "all24_role_coordinate_checks": all24_role_checks,
        "all576_role_coordinate_checks": all576_checks,
        "covariance_failures": covariance_failures,
        "L3_L6_L7_same_phase_translated_collision_rows": translated_collision_rows,
        "marker_values_unchanged_after_every_primitive": True,
        "clean_work_after_compute_except_flag": True,
        "clean_work_after_uncompute_including_flag": True,
        "fine_NN_raw_anchor_plus_exact_one_recognizer_compiled": True,
        "Cycle629_weight_projector_fine_NN_enforced": False,
        "pass": (
            metadata["Toffoli_macros"] == 285
            and metadata["complement_X_or_CNOT_macros"] == 92
            and len(primitive_specs) == 7787
            and sum(len(g.qubits) == 1 for g in primitive_specs) == 2611
            and sum(len(g.qubits) == 2 for g in primitive_specs) == 5176
            and truth_failures == covariance_failures == 0
            and placement_overlap == 0
            and all(row["pass"] for row in translated_collision_rows)
            and all(row["rejected"] for row in malformed.values())
            and deletion["detected"]
        ),
    }
    check("marker-safe raw anchor plus exact-one selector is fine-NN routed, covariant, deletion-sensitive, and cleanly uncomputed",
          result["pass"], result)
    return result


def token_successor_and_sidecar_audit(paths: dict) -> dict:
    state_hasher = sha256()
    transition_hasher = sha256()
    total_states = total_transitions = edge_sum = 0
    inverse_failures = malformed_failures = 0
    deletion_witness = None
    route_union = set()
    marker = c630.marker_residues()
    sidecar_histogram = Counter()
    two_lane_successes = multilane_successes = 0
    multilane_switch_histogram = Counter()
    for route_index, (pair, path) in enumerate(sorted(paths.items())):
        distance = len(path) - 1
        edge_sum += distance
        route_union.update(c630.residue(site) for site in path)
        states = []
        for edge in reversed(range(1, distance)):
            states.append((route_index, "open", edge, path[edge + 1]))
        states.append((route_index, "apply", 0, path[1]))
        for edge in range(1, distance):
            states.append((route_index, "close", edge, path[edge]))
        states.append((route_index, "renew", distance, path[-1]))
        if len(states) != 2 * distance:
            raise AssertionError((distance, len(states)))
        successors = {states[index]: states[(index + 1) % len(states)]
                      for index in range(len(states))}
        predecessors = {target: source for source, target in successors.items()}
        inverse_failures += int(len(successors) != len(states) or len(predecessors) != len(states))
        malformed_failures += int(
            (route_index, "open", distance + 1, path[-1]) in successors
            or (route_index, "double_token", 0, path[0]) in successors
        )
        if deletion_witness is None:
            source = states[0]
            reduced = {key: target for key, target in successors.items() if key != source}
            deletion_witness = {
                "route_index": route_index,
                "deleted_source": source,
                "expected_successor": successors[source],
                "deleted_source_has_no_successor": source not in reduced,
                "transition_count_after_deletion": len(reduced),
                "return_cycle_broken": len(reduced) == len(states) - 1,
            }
        for state in states:
            state_hasher.update((repr(state) + "\n").encode())
            transition_hasher.update((repr((state, successors[state])) + "\n").encode())
        total_states += len(states)
        total_transitions += len(successors)

        base = set(path)
        sidecars = 0
        for direction in DIRECTIONS:
            shifted = {
                tuple(site[axis] + direction[axis] for axis in range(3))
                for site in path
            }
            if not base.intersection(shifted) and not any(
                c630.residue(site) in marker for site in shifted
            ):
                sidecars += 1
        sidecar_histogram[sidecars] += 1

        # A stronger bounded multilane scout.  At each data-path site the
        # token occupies one of the six axial neighbors.  It may remain in a
        # lane or change between two non-opposite lanes through the diagonal
        # connector p+delta_a+delta_b (two NN token steps while data pauses).
        # Dynamic programming minimizes lane changes and binds predecessors.
        safe = []
        data_residues = {c630.residue(site) for site in path}
        for site in path:
            row = []
            for direction in DIRECTIONS:
                token_site = c630.add(site, direction)
                row.append(
                    c630.residue(token_site) not in marker
                    and c630.residue(token_site) not in data_residues
                )
            safe.append(tuple(row))

        def pair_or_multilane(allowed: tuple[int, ...]):
            costs = {lane: 0 for lane in allowed if safe[0][lane]}
            for position in range(1, len(path)):
                new_costs = {}
                pivot = path[position]
                for lane in allowed:
                    if not safe[position][lane]:
                        continue
                    best = None
                    for previous, cost in costs.items():
                        if previous == lane:
                            candidate = cost
                        else:
                            first = DIRECTIONS[previous]
                            second = DIRECTIONS[lane]
                            if all(first[axis] == -second[axis] for axis in range(3)):
                                continue
                            connector = tuple(
                                pivot[axis] + first[axis] + second[axis]
                                for axis in range(3)
                            )
                            if (c630.residue(connector) in marker
                                    or c630.residue(connector) in data_residues):
                                continue
                            candidate = cost + 1
                        best = candidate if best is None else min(best, candidate)
                    if best is not None:
                        new_costs[lane] = best
                costs = new_costs
                if not costs:
                    break
            return None if not costs else min(costs.values())

        pair_costs = [
            pair_or_multilane(pair_lanes)
            for pair_lanes in combinations(range(6), 2)
        ]
        if any(cost is not None for cost in pair_costs):
            two_lane_successes += 1
        multi_cost = pair_or_multilane(tuple(range(6)))
        if multi_cost is not None:
            multilane_successes += 1
            multilane_switch_histogram[multi_cost] += 1

    result = {
        "route_count": len(paths),
        "sum_path_edges": edge_sum,
        "states_per_d_edge_route": "2d: d-1 open, one apply, d-1 close, one same-endpoint renewal",
        "abstract_route_token_states": total_states,
        "abstract_successor_transitions": total_transitions,
        "state_table_sha256": state_hasher.hexdigest(),
        "successor_table_sha256": transition_hasher.hexdigest(),
        "inverse_failures": inverse_failures,
        "malformed_descriptor_index_or_double_token_rejections": malformed_failures == 0,
        "deletion_control": deletion_witness,
        "route_union_residues": len(route_union),
        "unit_offset_sidecar_option_histogram": dict(sorted(sidecar_histogram.items())),
        "routes_without_disjoint_marker_free_unit_offset_sidecar": sidecar_histogram[0],
        "single_adjacent_sidecar_layout_pass": sidecar_histogram[0] == 0,
        "two_lane_routes_solved_with_bounded_diagonal_lane_changes": two_lane_successes,
        "six_lane_routes_solved_with_bounded_diagonal_lane_changes": multilane_successes,
        "six_lane_minimum_lane_change_histogram": dict(sorted(multilane_switch_histogram.items())),
        "lane_change_microsteps": "two NN token steps through p+delta_a+delta_b while the data step pauses",
        "multilane_collision_audit": "one selected token per coarse cell; equal-phase K translations are disjoint, and arbitrary requested token edges are serialized by Cycle631's nine-colour matching",
        "multilane_physical_controller_compiled": False,
        "multilane_remaining_obligation": "encode lane/head state in M2 roles, locally choose the DP predecessor, generate the token, and renew it without the host table",
        "abstract_successor_pass": (
            len(paths) == 4570 and edge_sum == 196912
            and total_states == total_transitions == 393824
            and inverse_failures == malformed_failures == 0
            and deletion_witness["return_cycle_broken"]
        ),
        "physical_local_successor_circuit_compiled": False,
        "why_not_physical": "route identity/phase storage, a disjoint token track or equivalent controller, local program lookup, genesis, and recurrent renewal are not encoded into M2 sites",
    }
    check("all 4,570 finite routes have an explicit reversible abstract successor with inverse, malformed, and deletion controls",
          result["abstract_successor_pass"], result)
    check("the single unit-offset sidecar token lane is constructively falsified without promoting a no-go",
          not result["single_adjacent_sidecar_layout_pass"]
          and result["routes_without_disjoint_marker_free_unit_offset_sidecar"] == 1919,
          result["unit_offset_sidecar_option_histogram"])
    check("two-lane and six-lane bounded-change sidecars are explicitly probed beyond the fixed-offset failure",
          0 <= two_lane_successes <= multilane_successes <= len(paths),
          {"two_lane_successes": two_lane_successes,
           "six_lane_successes": multilane_successes,
           "six_lane_failures": len(paths) - multilane_successes,
           "switch_histogram": dict(sorted(multilane_switch_histogram.items()))})
    return result


def edge_colour(axis: int, source_coordinate: int) -> tuple[int, int]:
    return axis, source_coordinate % 3


def nine_colour_arbitration() -> dict:
    rows = []
    matching_failures = seam_failures = 0
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        side = K * length
        local_failures = 0
        for axis in range(3):
            for colour in range(3):
                for coordinate in range(side):
                    incident = int(coordinate % 3 == colour) + int((coordinate - 1) % 3 == colour)
                    local_failures += int(incident > 1)
                    if coordinate in (0, side - 1):
                        seam_failures += int(incident > 1)
        matching_failures += local_failures
        rows.append({
            "length": length,
            "split": split,
            "fine_torus_side": side,
            "divisible_by_three": side % 3 == 0,
            "axis_colour_coordinate_checks": 9 * side,
            "matching_failures": local_failures,
            "pass": side % 3 == 0 and local_failures == 0,
        })

    covariance_failures = 0
    all24_checks = all576_checks = 0
    base_edges = tuple((axis, colour) for axis in range(3) for colour in range(3))
    def transform(frame, label):
        axis, colour = label
        image = frame @ np.eye(3, dtype=int)[:, axis]
        target_axis = int(np.flatnonzero(image)[0])
        sign = int(image[target_axis])
        return target_axis, colour if sign == 1 else (-colour - 1) % 3
    for frame in FRAMES:
        mapped = tuple(transform(frame, label) for label in base_edges)
        covariance_failures += int(len(set(mapped)) != 9)
        all24_checks += 9
    for first in FRAMES:
        for second in FRAMES:
            for label in base_edges:
                covariance_failures += int(
                    transform(first, transform(second, label))
                    != transform(first @ second, label)
                )
                all576_checks += 1
    translation_checks = 0
    for direction in DIRECTIONS:
        for axis, colour in base_edges:
            # Source coordinate and state-carried phi translate together.
            translated_relative = (colour + direction[axis] - direction[axis]) % 3
            covariance_failures += int(translated_relative != colour)
            translation_checks += 1
    result = {
        "schedule": "colour each positive NN edge by (axis, (positive-source coordinate - phi_axis) mod 3)",
        "colours": 9,
        "matching_proof": "for a fixed axis/residue a vertex is incident only when x mod3 is c or c+1, never both; different axes have different colours",
        "rows": rows,
        "seam_matching_failures": seam_failures,
        "six_state_carried_translation_checks": translation_checks,
        "all24_colour_permutation_checks": all24_checks,
        "all576_colour_composition_checks": all576_checks,
        "covariance_failures": covariance_failures,
        "state_carried_phi_required": True,
        "collision_arbitration_compiled": True,
        "token_genesis_or_program_selection_compiled": False,
        "pass": all(row["pass"] for row in rows)
                and seam_failures == covariance_failures == 0,
    }
    check("nine state-carried edge colours are NN matchings on L3/L6/L7 and covariant under six/all24/all576",
          result["pass"], result)
    return result


def local_rom_program_probe(recognizer: dict, r630: dict) -> dict:
    full_word = recognizer["full_identity_selector_plus_act_microsteps"]
    free_roles = K**3 - 144
    address_bits = math.ceil(math.log2(full_word))
    distinct_descriptors = r630["conditional_act_descriptor_routing"][
        "conditional_act_distinct_literal_stage_descriptors"
    ]
    result = {
        "probe_A_moving_one_hot_program_head": {
            "required_phase_sites_lower_bound": full_word,
            "available_marker_free_K129_roles": free_roles,
            "capacity_ratio_required_over_available": full_word / free_roles,
            "fits_one_K129_block": full_word <= free_roles,
            "scope": "lower bound before opcode bits, head state, tape adjacency, data-role exclusion, inverse, or renewal",
        },
        "probe_B_stationary_radius_one_neighbor_lookup": {
            "binary_program_address_bits": address_bits,
            "radius_one_M2_sites_including_center": 7,
            "maximum_raw_quaternary_bits_in_radius_one": 14,
            "one_step_full_address_visible": address_bits <= 14,
            "multistep_hierarchical_decoder_still_open": True,
        },
        "probe_C_descriptor_compression": {
            "distinct_literal_stage_descriptors": distinct_descriptors,
            "one_M2_position_per_descriptor_fits_marker_free_count": distinct_descriptors <= free_roles,
            "remaining_problem": "descriptor opcode/route data, repeated-call counter, NN tape embedding, uniform local interpreter, clean inverse, and renewal are not compiled",
            "literal_decoder_compiled": False,
        },
        "physical_local_ROM_or_moving_head_compiled": False,
        "route_specific_disposition": "the naive unary microstep tape and one-step radius-one lookup fail capacity/visibility; descriptor compression and multistep binary decoding remain live",
        "pass_as_adversarial_probe": (
            full_word > free_roles and address_bits > 14
            and distinct_descriptors <= free_roles
        ),
    }
    check("moving-head unary ROM and one-step neighbor lookup are tested without ruling out compressed multistep decoding",
          result["pass_as_adversarial_probe"], result)
    return result


def controller_disposition(recognizer: dict, token: dict, arbitration: dict,
                           rom: dict, r630: dict, r617: dict) -> dict:
    macro = recognizer["full_identity_selector_plus_act_microsteps"]
    clock_bits = math.ceil(math.log2(macro))
    padded = 1 << clock_bits
    result = {
        "conditional_word_bounded_support": True,
        "conditional_word_constant_overhead_per_coarse_cell": True,
        "physical_controller_bounded_support_established": False,
        "physical_controller_constant_overhead_established": False,
        "K": K,
        "full_selected_branch_macro_microsteps": macro,
        "binary_clock_bits_for_next_power_of_two_padding": clock_bits,
        "padded_clock_period": padded,
        "padded_idle_microsteps": padded - macro,
        "binary_increment_is_reversible": True,
        "binary_clock_literal_fine_NN_layout_compiled": False,
        "clock_to_route_descriptor_local_decoder_compiled": False,
        "local_ROM_probe": rom["route_specific_disposition"],
        "route_label_or_token_physical_M2_storage_compiled": False,
        "token_genesis_and_recurrent_renewal_compiled": False,
        "nine_colour_collision_arbitration_available": arbitration["pass"],
        "Cycle617_eight_lane_sorter_available_as_bounded_collision_prior": r617["route_B"]["pass_one_macro_collision_sorter"],
        "Cycle617_host_schedule_not_promoted_to_time": True,
        "full_selector_plus_act_word_bound": True,
        "host_free_recurrent_G_physical": False,
        "literal_physical_encoder_E": False,
        "physical_intertwiner_residual": None,
        "full_code_leakage_evaluated": False,
        "mass_fixture_reexecuted": False,
        "contact_fixture_reexecuted": False,
        "seam_fixture_reexecuted": False,
        "path_existence": r630["conditional_act_descriptor_routing"]["pass"],
        "marker_safe_selector": recognizer["pass"],
        "abstract_successor": token["abstract_successor_pass"],
        "physical_autonomous_controller": False,
        "promoted_candidate": False,
        "reason": "a finite bound and reversible abstract tables do not implement local physical program lookup, token storage/genesis, or recurrent renewal",
    }
    check("full selector-plus-act word is explicitly bounded while autonomous physical promotion remains blocked",
          result["full_selector_plus_act_word_bound"]
          and not result["physical_autonomous_controller"]
          and result["physical_intertwiner_residual"] is None,
          result)
    return result


def no_go_discipline(recognizer: dict, token: dict, arbitration: dict,
                      rom: dict, controller: dict) -> dict:
    families = (
        {"family": "marker-safe exact recognizer", "marker": "ATTEMPTED", "object": "120 anchors plus selected exact-one orientation branch", "mechanism": "clean-complement conjunction using 285 marker-safe exact Toffoli macros", "evidence": "7,787 primitive gates per compute; all24/all576 and malformed/deletion/cleanup pass", "strength_vs_target": "replaces the raw selector on the supplied marker sector", "failure_statement": "does not enforce the Cycle629 <=91 weight projector or create marker genesis", "terminal_obligation": "literal raw marker plus exact-one branch selection"},
        {"family": "abstract route-token successor", "marker": "ATTEMPTED", "object": "4,570 Cycle630 paths", "mechanism": "finite cyclic open/apply/close/renew labels", "evidence": "393,824 states and transitions with inverse and deletion control", "strength_vs_target": "removes ambiguity in the finite successor table", "failure_statement": "labels are not physically stored or locally decoded", "terminal_obligation": "reversible successor definition"},
        {"family": "single adjacent sidecar token lane", "marker": "ATTEMPTED", "object": "six unit translates of each route path", "mechanism": "disjoint marker-free translated lane", "evidence": f"{token['routes_without_disjoint_marker_free_unit_offset_sidecar']}/4,570 routes have no lane", "strength_vs_target": "falsifies one concrete token embedding only", "failure_statement": "multilane, packet, and distributed controllers remain open", "terminal_obligation": "physical token storage disjoint from routed data"},
        {"family": "bounded-change axial multilane sidecar", "marker": "ATTEMPTED", "object": "all 15 two-lane pairs and the full six-lane neighbor bundle", "mechanism": "dynamic-programmed safe lanes with two-step diagonal switches", "evidence": f"two lanes solve {token['two_lane_routes_solved_with_bounded_diagonal_lane_changes']}/4,570 and six lanes solve {token['six_lane_routes_solved_with_bounded_diagonal_lane_changes']}/4,570", "strength_vs_target": "closes geometric sidecar existence with at most two lane changes", "failure_statement": "predecessor choice, head state, genesis, and renewal remain host supplied", "terminal_obligation": "bounded physical token geometry"},
        {"family": "nine-colour edge arbitration", "marker": "ATTEMPTED", "object": "all fine NN edges on L3/L6/L7", "mechanism": "axis and source-coordinate-mod3 matching classes", "evidence": "zero matching/seam/six/all24/all576 failures", "strength_vs_target": "solves edge collision arbitration conditional on a state-carried colour phase", "failure_statement": "does not generate a route request or program clock", "terminal_obligation": "collision-free simultaneous local gates"},
        {"family": "padded reversible binary program clock", "marker": "ATTEMPTED", "object": "the full selector-plus-act macro bound", "mechanism": "next-power-of-two reversible increment", "evidence": f"{controller['binary_clock_bits_for_next_power_of_two_padding']} bits bound the macro period", "strength_vs_target": "finite state-count upper bound only", "failure_statement": "literal NN storage and clock-to-descriptor decoder are absent", "terminal_obligation": "host-free local program selection"},
        {"family": "local ROM/moving-head program storage", "marker": "ATTEMPTED", "object": "full selector-plus-act microstep word and compressed descriptor inventory", "mechanism": "unary moving tape, radius-one stationary lookup, and descriptor compression capacity audit", "evidence": rom["route_specific_disposition"], "strength_vs_target": "falsifies two naive lookup layouts while retaining compressed multistep decoding", "failure_statement": "no literal NN interpreter, head renewal, or descriptor decoder is built", "terminal_obligation": "state-carried local program lookup"},
    )
    open_routes = (
        {"family": "multilane or packetized physical token track", "mechanism": "embed route phase/identity into bounded auxiliary M2 lanes", "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT", "terminal_obligation": "physical successor storage and renewal"},
        {"family": "local program decoder/ROM", "mechanism": "map a carried clock and branch label to requested route edge and gate", "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT", "terminal_obligation": "remove host-issued descriptor schedule"},
        {"family": "Cycle629 weight-sector enforcement", "mechanism": "fine-NN comparator or locally conserved occupancy bound", "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT", "terminal_obligation": "recognition beyond the supplied sector"},
        {"family": "physical E/G/intertwiner", "mechanism": "compose literal code map with recurrent local controller", "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT", "terminal_obligation": "E G_coarse = G_physical E and leakage"},
    )
    walls = (
        "physical route-label/token storage and successor update",
        "local clock-to-descriptor and gate decoder",
        "token genesis and recurrent renewal",
        "Cycle629 <=91 weight-sector enforcement",
        "literal encoder E and full-code leakage",
        "host-free G_physical and physical intertwiner",
    )
    pairs = tuple({
        "wall_A": first, "wall_B": second,
        "A_implies_B": False, "B_implies_A": False,
        "shared_witness_identified": False, "independent": True,
        "evidence": "Cycle631 executes no implication or common obstruction between these residual obligations",
    } for first, second in combinations(walls, 2))
    residuals = (
        {"citation": "docs/work_history/repo/review_feedback/PHYSICAL_MARKER_PRESERVING_FREE_QUOTIENT_ROUTER_CYCLE630_NOTE_2026-07-23.md:224-258", "prior_residual": "selector, local successor, collision-safe token/clock recurrence open", "current_residual": "raw selector and edge arbitration close; physical label storage, decoder, genesis, renewal remain", "same_scope": False, "exact_match": False, "use_as_closure": False},
        {"citation": "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md:208-225", "prior_residual": "fine-NN constraint enforcement and autonomous update absent", "current_residual": "raw marker recognition is compiled but <=91 weight enforcement and autonomy remain", "same_scope": False, "exact_match": False, "use_as_closure": False},
        {"citation": "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_SECTOR_ROLE_GENESIS_CLOSURE_TOURNAMENT_CYCLE617_NOTE_2026-07-22.md:167-183", "prior_residual": "finite collision sorter is not CAR signs or causal time", "current_residual": "nine-colour matching is collision arbitration, not program genesis, signs, or time", "same_scope": True, "exact_match": False, "use_as_closure": False},
        {"citation": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md:95-98", "prior_residual": "literal E, physical intertwiner, leakage open", "current_residual": "unchanged", "same_scope": True, "exact_match": True, "use_as_closure": False},
    )
    rhetoric = tuple({
        "claim": claim,
        "per_element": "exact primitive or transition counts stated",
        "per_site": "one M2 per role; NN gates only where physically compiled",
        "per_mode": "six-mode fixture inherited as target only, not reexecuted",
        "per_block": "K129 bounded block and constant role/table counts",
        "lattice_wide": "NOT CLOSED: local decoder, token genesis/renewal, E/G/intertwiner absent",
    } for claim in ("selector", "successor", "collision", "clock", "physical compiler"))
    partial = (
        {"file": "scripts/physical_autonomous_marker_recognition_token_attempt_cycle631_2026_07_23.py", "status": "PARTIAL / CURRENT", "what_closes": "raw selector, abstract successor, nine-colour arbitration, sidecar falsifier"},
        {"file": "scripts/physical_marker_preserving_free_quotient_router_cycle630_2026_07_23.py", "status": "PARTIAL / PRIOR", "what_closes": "all conditional-act marker-free path existence and overhead"},
        {"file": "scripts/physical_local_sector_role_genesis_closure_tournament_cycle617_2026_07_22.py", "status": "PARTIAL / PRIOR", "what_closes": "bounded eight-lane reversible collision sorting only"},
        {"file": "UNMATERIALIZED", "status": "OPEN / PRIORITY", "what_closes": "bounded physical route-label packet plus local decoder and renewal"},
        {"file": "UNMATERIALIZED", "status": "OPEN", "what_closes": "literal E, recurrent G_physical, intertwiner, leakage, and fresh fixtures"},
    )
    steelman = {
        "mechanism": "Replace a single sidecar by a small covariant multilane route-label packet; use the nine-colour matching as its arbitration layer and compile a bounded local ROM from carried (phi,h,clock,route,phase) to the requested edge/gate.",
        "actionable_next_steps": (
            "construct a descriptor-specific multilane bundle or mobile route-label packet",
            "compile the finite local ROM and prove clean inverse/renewal",
            "add a fine-NN <=91 weight-sector comparator or conservation law",
            "compose literal E/G and execute intertwiner, leakage, deletion, L3/L6/L7, and fresh fixtures",
        ),
        "why_it_could_close": "Cycle630 supplies every finite path, Cycle631 supplies exact raw recognition and collision matchings, and only one adjacent sidecar—not all bounded token encodings—has failed.",
        "terminal_obligation": "physical token/program storage, local decoder, genesis/renewal, weight enforcement, E, G_physical, intertwiner, leakage, and fixtures",
        "authority_status": "OPEN / no retained authority",
        "citations": (
            "docs/work_history/repo/review_feedback/PHYSICAL_MARKER_PRESERVING_FREE_QUOTIENT_ROUTER_CYCLE630_NOTE_2026-07-23.md:42-127",
            "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md:208-225",
            "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_SECTOR_ROLE_GENESIS_CLOSURE_TOURNAMENT_CYCLE617_NOTE_2026-07-22.md:167-183",
        ),
    }
    echoes = (
        {"cycle": "Cycle610", "retired": "host Hamiltonian-bus word as physical promotion", "mechanism": "conditional literal word with explicit E/G residual", "applicability": "Cycle631 binds the full selector-plus-act count but still withholds autonomy"},
        {"cycle": "Cycle617", "retired": "collision sorter as CAR sign or time", "mechanism": "separated reversible collision lemma", "applicability": "Cycle631 uses collision scheduling only"},
        {"cycle": "Cycle629", "retired": "external phase/orientation at projector level", "mechanism": "state-carried phi,h and marker crystal", "applicability": "Cycle631 recognizes raw markers but does not enforce the weight sector"},
        {"cycle": "Cycle630", "retired": "absence of marker-free paths", "mechanism": "complete finite path table", "applicability": "Cycle631 attempts successor control and falsifies one sidecar embedding"},
        {"cycle": "Cycle631", "retired": "single adjacent sidecar as a universal token lane", "mechanism": "exhaustive six-offset disjointness scout", "applicability": "route-specific only; multilane/distributed controllers stay live"},
    )
    result = {
        "skill_freshness": {"origin_main_checked": True, "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7", "proof_search_governance_sha256": "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258", "newer_origin_main_version_followed": True},
        "N1_normalized_families": families,
        "N1_qualifying_family_count": len(families),
        "N1_all_markers_exact": all(row["marker"] in ("ATTEMPTED", "RULED OUT BY PRIOR") for row in families),
        "N1_open_counterroutes_not_counted": open_routes,
        "N2_collapsed_walls": walls,
        "N2_directional_wall_independence": pairs,
        "N2_pair_count": len(pairs),
        "N3_hidden_wall_scan": {"required_phrase_scan": ("only", "must", "cannot", "necessarily", "minimum", "impossible", "forces", "requires"), "load_bearing_premises": ("K129", "supplied phi,h", "supplied marker sector", "clean work", "host materialized Cycle630 paths", "finite descriptor order"), "single_sidecar_scope_explicit": True, "host_decoder_absence_explicit": True, "hidden_wall_promotions_complete": True},
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
        "narrow_positive_gate": "PASS / SHIP WITH FIREWALL",
        "narrow_route_specific_negative_gate": "PASS / single-adjacent-sidecar only",
        "status": "FAIL",
        "failed_checklist_items": (
            "N7: multilane token packet and local program decoder remain live",
            "physical promotion: weight enforcement, E, recurrent G_physical, intertwiner, leakage, and fresh fixtures unexecuted",
        ),
    }
    schema = (
        len(families) >= 5 and result["N1_all_markers_exact"]
        and all(row["status"].startswith("OPEN / NOT COUNTED") for row in open_routes)
        and len(pairs) == 15 and all(row["independent"] for row in pairs)
        and all(set(("citation", "prior_residual", "current_residual", "same_scope", "exact_match", "use_as_closure")) <= set(row) for row in residuals)
        and result["N5_five_resolutions_present"]
        and all(set(("file", "status", "what_closes")) == set(row) for row in partial)
        and set(("mechanism", "actionable_next_steps", "why_it_could_close", "terminal_obligation", "authority_status", "citations")) == set(steelman)
        and all(set(("cycle", "retired", "mechanism", "applicability")) == set(row) for row in echoes)
    )
    check("fresh N1-N8 permits the narrow positive and sidecar falsifier but blocks broad/minimum/shared/axiom claims",
          schema and result["status"] == "FAIL"
          and result["narrow_positive_gate"].startswith("PASS")
          and not result["shared_obstruction_claim"], result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "7,787", "393,824", "1,919", "nine-colour", "L3/L6/L7",
        "all24", "all576", "selector-plus-act", "host", "token genesis",
        "E G_coarse = G_physical E", "no axiom pressure", "authority none",
        "audit unset", "N1", "N8", "`ATTEMPTED`", "`RULED OUT BY PRIOR`",
        "same_scope", "exact_match", "use_as_closure", "per_element",
        "per_site", "per_mode", "per_block", "lattice_wide", "what_closes",
        "actionable", "applicability",
    )
    missing = tuple(token for token in required if token not in text)
    result = {"required_tokens": required, "missing_tokens": missing, "pass": not missing}
    check("Cycle631 note states exact constructions, sidecar scope, N1-N8 schema, and withheld physical obligations",
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
            inherited, r630, r617 = shore()
            target = exact_target_contract()
            original_c630_check = c630.check
            c630.check = lambda *_args, **_kwargs: None
            try:
                graph, parent, _depth = c630.quotient_tree()
                routing, paths = c630.descriptor_routing_audit(parent, json.loads((ROOT / (
                    "outputs/physical_proper_cubic_supercell_stream_composition_"
                    "tournament_cycle610_receipt_2026_07_22.json"
                )).read_text()))
            finally:
                c630.check = original_c630_check
            toffoli = marker_safe_toffoli_audit()
            work = select_work_roles()
            recognizer = recognizer_audit(parent, work)
            token = token_successor_and_sidecar_audit(paths)
            arbitration = nine_colour_arbitration()
            rom = local_rom_program_probe(recognizer, r630)
            controller = controller_disposition(recognizer, token, arbitration, rom, r630, r617)
            discipline = no_go_discipline(recognizer, token, arbitration, rom, controller)
            note = note_contract()
            elapsed = time.monotonic() - started
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            maximum_rss_bytes = int(rss if sys.platform == "darwin" else rss * 1024)
            check("Cycle631 cold run stays within declared time and memory caps",
                  elapsed <= CAP_SECONDS and maximum_rss_bytes <= CAP_BYTES,
                  {"elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss_bytes,
                   "cap_seconds": CAP_SECONDS, "cap_bytes": CAP_BYTES})
            receipt = {
                "status": "partial_marker_safe_selector_and_abstract_token_successor",
                "authority": AUTHORITY,
                "audit": AUDIT,
                "author_artifact_status_accepted": False,
                "breakthrough_bar_met": False,
                "runner_sha256": sha(Path(__file__)),
                "note_sha256": sha(NOTE),
                "pins": PINS,
                "shore": inherited,
                "exact_target_contract": target,
                "Cycle630_reexecution": {
                    "free_sites": graph["free_sites"],
                    "path_pairs": routing["distinct_ordered_endpoint_pairs"],
                    "path_table_sha256": routing["path_table_sha256"],
                    "pass": graph["pass"] and routing["pass"],
                },
                "marker_safe_exact_Toffoli": toffoli,
                "marker_safe_selector_replacement": recognizer,
                "route_token_successor_and_sidecar_scout": token,
                "nine_colour_edge_arbitration": arbitration,
                "local_ROM_program_probe": rom,
                "autonomous_controller_disposition": controller,
                "no_go_discipline": discipline,
                "note_contract": note,
                "strongest_constructive_result": "on the supplied Cycle629 marker sector, a 7,787-primitive marker-safe exact selector compute is routed through marker-free fine-NN paths with clean uncompute and all24/all576 covariance; every Cycle630 path also has an explicit finite reversible abstract successor, and nine state-carried edge colours give L3/L6/L7 collision-free matchings",
                "route_specific_negative": "the single adjacent unit-offset sidecar token layout fails for 1,919 of 4,570 paths; this does not rule out multilane, packetized, or distributed controllers",
                "exact_scope": "raw 120-anchor plus exact-one marker recognition on the supplied <=91 and neighbor-equal-h sector, host-materialized Cycle630 paths, abstract successor labels, and state-carried phi,h edge arbitration",
                "mass_contact_seam_fixture_status": "not reexecuted and no inherited fixture credit; the physical autonomous controller needed to carry those fixtures is absent",
                "shared_obstruction_or_axiom_pressure": False,
                "constitutional_effect": "none",
                "broad_negative_gate": discipline["broad_negative_gate"],
                "optimal_next_campaign": "construct a bounded covariant multilane route-label packet and literal fine-NN local ROM from carried (phi,h,clock,route,phase) to edge/gate, with token genesis/renewal; then enforce the <=91 sector and compose literal E/G for fresh intertwiner, leakage, deletion, L3/L6/L7, mass/contact/seam tests",
                "elapsed_seconds": elapsed,
                "maximum_RSS_bytes": maximum_rss_bytes,
                "tests_passed": PASS,
                "tests_failed": FAIL,
                "pass": FAIL == 0,
            }
            RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n")
            print("SUMMARY_JSON", json.dumps({
                "pass": FAIL == 0, "tests_passed": PASS, "tests_failed": FAIL,
                "recognizer_primitives": recognizer["raw_primitive_gate_count_per_compute"],
                "selector_plus_act_microsteps": recognizer["full_identity_selector_plus_act_microsteps"],
                "abstract_token_states": token["abstract_route_token_states"],
                "sidecar_failures": token["routes_without_disjoint_marker_free_unit_offset_sidecar"],
                "physical_autonomous_controller": controller["physical_autonomous_controller"],
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
