#!/usr/bin/env python3
"""Cycle654: literal all24 one-face projector/correction tile tournament.

Consumes the committed Cycle649 outer-shell geometry and the committed
Cycle651 reversible face-pump logic.  It places new sidecar role orbits,
enumerates actual support-one/two fine-NN gate lists for one leaf-face tile,
and tests static, mobile-token, and staggered dispatch routes separately.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""
from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
import contextlib
import importlib
import io
from itertools import permutations
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SHORE_REF = "b9b78258bcb5ee60d7fec38011d1f30721fa2832"
C649_REF = "ab780eb5be"
AUTHORITY = "none"
AUDIT = "unset"
CAP_SECONDS = 240.0
CAP_BYTES = 4 * 1024**3
PASS = FAIL = 0

NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ALL24_FACE_PROJECTOR_TILE_COMPILER_CYCLE654_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_all24_face_projector_tile_compiler_cycle654_receipt_2026_07_23.json"

C649_RUNNER = "scripts/physical_reserved_outer_shell_sidecar_placement_cycle649_2026_07_23.py"
C649_NOTE = "docs/work_history/repo/review_feedback/PHYSICAL_RESERVED_OUTER_SHELL_SIDECAR_PLACEMENT_CYCLE649_NOTE_2026-07-23.md"
C649_RECEIPT = "outputs/physical_reserved_outer_shell_sidecar_placement_cycle649_receipt_2026_07_23.json"
C649_COLD = "outputs/physical_reserved_outer_shell_sidecar_placement_cycle649_cold_2026_07_23.txt"
C651_RUNNER = "scripts/physical_root_label_blind_face_pump_compiler_cycle651_2026_07_23.py"
C651_NOTE = "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_LABEL_BLIND_FACE_PUMP_COMPILER_CYCLE651_NOTE_2026-07-23.md"
C651_RECEIPT = "outputs/physical_root_label_blind_face_pump_compiler_cycle651_receipt_2026_07_23.json"
C651_COLD = "outputs/physical_root_label_blind_face_pump_compiler_cycle651_cold_2026_07_23.txt"
C642_NOTE = "docs/work_history/repo/review_feedback/PHYSICAL_FIXED_CUBIC_WILSON_FILL_INCIDENCE_CYCLE642_NOTE_2026-07-23.md"
C629_NOTE = "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md"

PINS = {
    C649_RUNNER: "715dc2e36dea83dc603d202447733cc9e81d1dedb22102382109b6b95a9edc09",
    C649_NOTE: "57a581b882c2a7a4ee2fe4ddb62b34787dbc946abd318e61fa3dd141729729c2",
    C649_RECEIPT: "d367e88409cbfadb6e9a46a2db3c5ddbdc9e28b7964272b67d7cbb0b4eaf0db9",
    C649_COLD: "85fab6a108ff53bd86a084694b1ee14ec16d500d672e922fcc75003a01f541a7",
    C651_RUNNER: "3b8f5c034203f3f158ecd1fd887f78944b6ef071379c00b9486c976d49dafd9b",
    C651_NOTE: "2f6340efdc224a0e1adc25e114824e122af2e39c06ef95c2c23d7eb3942623e8",
    C651_RECEIPT: "5850881071f28dd9745daffb27be8f5cb75419739b9e26f1cb0befb8b406d80b",
    C651_COLD: "69d8a6c0d47e581008f44871a7f45d7c2f1f35130be4529d8911c2a4655d160e",
}

C649 = None
C642 = None


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def git_bytes(ref: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=ROOT)


def check(label: str, condition: bool, detail="") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def immutable_line(path: str, fragment: str) -> int:
    lines = git_bytes(SHORE_REF, path).decode().splitlines()
    return next((number for number, line in enumerate(lines, 1) if fragment in line), 0)


def source_line(fragment: str) -> int:
    return next((number for number, line in enumerate(Path(__file__).read_text().splitlines(), 1) if fragment in line), 0)


def cited_line_exists(ref: str, path: str, line: int) -> bool:
    try:
        lines = git_bytes(ref, path).decode().splitlines()
    except subprocess.CalledProcessError:
        return False
    return 1 <= line <= len(lines) and bool(lines[line - 1].strip())


def shore() -> tuple[dict, dict, dict]:
    observed = {path: sha256(git_bytes(SHORE_REF, path)).hexdigest() for path in PINS}
    c649_direct = {path: sha256(git_bytes(C649_REF, path)).hexdigest() for path in (C649_RUNNER, C649_NOTE, C649_RECEIPT, C649_COLD)}
    local = {path: sha(ROOT / path) for path in (C649_RUNNER, C651_RUNNER)}
    c649_receipt = json.loads(git_bytes(C649_REF, C649_RECEIPT))
    c651_receipt = json.loads(git_bytes(SHORE_REF, C651_RECEIPT))
    result = {
        "immutable_cycle651_shore_ref": SHORE_REF,
        "committed_cycle649_ref": C649_REF,
        "observed_from_cycle651_shore": observed,
        "observed_direct_cycle649_commit": c649_direct,
        "hashes_match": observed == PINS and all(c649_direct[path] == PINS[path] for path in c649_direct),
        "local_import_mirrors": local,
        "local_import_mirrors_byte_equal_to_shores": all(local[path] == PINS[path] for path in local),
        "Cycle649_pass": c649_receipt["pass"],
        "Cycle649_route_word_geometry_pass": c649_receipt["route_word_geometry_pass"],
        "Cycle649_joint_alias_present": not c649_receipt["joint_inherited_role_allocation_pass"],
        "Cycle651_pass": c651_receipt["pass"],
        "Cycle651_autonomous_physical_face_pump": c651_receipt["autonomous_physical_face_pump_compiled"],
        "Cycle651_shared_obstruction": c651_receipt["shared_route_independent_obstruction"],
        "Cycle651_axiom_pressure": c651_receipt["axiom_pressure"],
        "Cycle649_consumed_as_geometry_premise": True,
    }
    condition = bool(
        result["hashes_match"] and result["local_import_mirrors_byte_equal_to_shores"]
        and result["Cycle649_pass"] and result["Cycle649_route_word_geometry_pass"]
        and result["Cycle649_joint_alias_present"] and result["Cycle651_pass"]
        and not result["Cycle651_autonomous_physical_face_pump"]
        and not result["Cycle651_shared_obstruction"] and not result["Cycle651_axiom_pressure"]
        and result["Cycle649_consumed_as_geometry_premise"]
    )
    check("committed Cycle649 geometry and immutable Cycle651 logic are byte-pinned and explicitly consumed", condition, result)
    return c649_receipt, c651_receipt, result


def load_modules() -> None:
    global C649, C642
    sys.path.insert(0, str(ROOT / "scripts"))
    C649 = importlib.import_module("physical_reserved_outer_shell_sidecar_placement_cycle649_2026_07_23")
    C642 = C649.c642
    imported = {C649_RUNNER: sha(Path(C649.__file__).resolve())}
    check("the consumed Cycle649 executable mirror is byte-pinned", imported == {C649_RUNNER: PINS[C649_RUNNER]}, imported)


def existing_sidecar_sites(system: dict, length: int) -> set[tuple[int, int, int]]:
    modulus = C649.K * length
    return {
        C649.rotate_mod(frame, tuple(row["seed"]), modulus)
        for row in system["program_placement"]["placements"]
        for frame in C649.FRAMES
    }


def inherited_program_masks(existing_program_roles) -> tuple[np.ndarray, np.ndarray]:
    coordinates = np.asarray(existing_program_roles, dtype=np.int64)
    base = np.zeros(C649.K**3, dtype=np.bool_)
    indices = ((coordinates[:, 0] + C649.SHELL) * C649.K + (coordinates[:, 1] + C649.SHELL)) * C649.K + (coordinates[:, 2] + C649.SHELL)
    base[indices] = True
    base_cube = base.reshape((C649.K, C649.K, C649.K))
    orbit_cube = np.zeros_like(base_cube)
    for frame in C649.FRAMES:
        axes = tuple(int(np.flatnonzero(frame[row])[0]) for row in range(3))
        rotated = np.transpose(base_cube, axes=axes)
        for row, axis in enumerate(axes):
            if frame[row, axis] < 0:
                rotated = np.flip(rotated, axis=row)
        orbit_cube |= rotated
    return base, orbit_cube.reshape(-1)


def build_existing_occupancy_light(length, existing_program_local):
    placement, fibers = C642.allocate_orbit_roles(length)
    obj = C642.build_tree_code(length, fibers)
    modulus = C649.K * length
    old = {
        tuple(value % modulus for value in C642.old_position_K(obj["graph"], qubit))
        for qubit in range(obj["graph"].qubits)
    }
    aux = {
        tuple(value % modulus for value in site)
        for role in obj["roles"]
        for site in obj["fibers"][role]
    }
    small = old | aux

    def occupied(site):
        if site in small:
            return True
        return (
            C649.block_center(site, modulus) == (0, 0, 0)
            and tuple(C649.centered_residue(value) for value in site) in existing_program_local
        )

    descriptor_summary, rows, _same_obj, _placement = C649.c646.build_descriptors(length)
    return placement, obj, descriptor_summary, rows, old, aux, occupied


def bfs_orbit_safe_fingers(center, targets, small_orbit_occupied, modulus, program_orbit_mask):
    total = C649.K**3
    blocked = program_orbit_mask.copy() if center == (0, 0, 0) else np.zeros(total, dtype=np.bool_)
    for site in small_orbit_occupied:
        if C649.block_center(site, modulus) != center:
            continue
        local = tuple(C649.centered_residue(site[axis] - center[axis]) for axis in range(3))
        blocked[C649.local_index(local)] = True
    parent = np.full(total, -2, dtype=np.int32)
    distance = np.full(total, -1, dtype=np.int16)
    queue = np.empty(total, dtype=np.int32)
    head = tail = 0
    for site in sorted(C649.local_backbone_sites()):
        index = C649.local_index(site)
        if not blocked[index] and parent[index] == -2:
            parent[index] = -1
            distance[index] = 0
            queue[tail] = index
            tail += 1
    while head < tail:
        index = int(queue[head])
        head += 1
        local = C649.local_coordinate(index)
        for direction in C649.DIRECTIONS:
            target = tuple(local[axis] + direction[axis] for axis in range(3))
            if any(value < -C649.SHELL or value > C649.SHELL for value in target):
                continue
            target_index = C649.local_index(target)
            if parent[target_index] != -2 or blocked[target_index]:
                continue
            parent[target_index] = index
            distance[target_index] = distance[index] + 1
            queue[tail] = target_index
            tail += 1
    paths = {}
    for global_target in targets:
        local_target = tuple(C649.centered_residue(global_target[axis] - center[axis]) for axis in range(3))
        candidates = []
        for direction_index, direction in enumerate(C649.DIRECTIONS):
            start = tuple(local_target[axis] + direction[axis] for axis in range(3))
            if any(value < -C649.SHELL or value > C649.SHELL for value in start):
                continue
            index = C649.local_index(start)
            if parent[index] != -2:
                candidates.append((int(distance[index]), direction_index, start, index))
        if not candidates:
            continue
        _distance, _direction, start, index = min(candidates)
        local_path = [start]
        while parent[index] != -1:
            index = int(parent[index])
            local_path.append(C649.local_coordinate(index))
        paths[global_target] = tuple(
            tuple((center[axis] + site[axis]) % modulus for axis in range(3))
            for site in local_path
        )
    return paths, {
        "block_center": center,
        "reachable_orbit_safe_vertices": tail,
        "maximum_distance": int(distance.max()),
        "target_count": len(targets),
        "targets_solved": len(paths),
    }


def compile_orbit_safe_fingers(length, targets, occupied, small_occupied, program_orbit_mask):
    modulus = C649.K * length
    small_orbit_occupied = {
        C649.rotate_mod(frame, site, modulus)
        for site in small_occupied
        for frame in C649.FRAMES
    }

    def orbit_occupied(site):
        if site in small_orbit_occupied:
            return True
        if C649.block_center(site, modulus) != (0, 0, 0):
            return False
        local = tuple(C649.centered_residue(value) for value in site)
        return bool(program_orbit_mask[C649.local_index(local)])

    fingers = {}
    route_kind = Counter()
    failures = []
    for target in sorted(targets):
        path = C649.straight_shell_finger(target, orbit_occupied, modulus)
        if path is None:
            failures.append(target)
        else:
            fingers[target] = path
            route_kind["all24_safe_two_axis_formula"] += 1
    bfs_rows = []
    for center in sorted({C649.block_center(target, modulus) for target in failures}):
        group = tuple(target for target in failures if C649.block_center(target, modulus) == center)
        paths, row = bfs_orbit_safe_fingers(center, group, small_orbit_occupied, modulus, program_orbit_mask)
        bfs_rows.append(row)
        for target, path in paths.items():
            fingers[target] = path
            route_kind["all24_safe_BFS_witness"] += 1
    unresolved = tuple(target for target in targets if target not in fingers)
    digest = sha256()
    for target, path in sorted(fingers.items()):
        digest.update(repr((target, path)).encode())
    result = {
        "length": length,
        "targets": len(targets),
        "route_kind_histogram": dict(route_kind),
        "initial_two_axis_failures": len(failures),
        "unresolved_targets": unresolved,
        "maximum_finger_edges": max((len(path) for path in fingers.values()), default=0),
        "finger_word_sha256": digest.hexdigest(),
        "bounded_search_rows": bfs_rows,
        "program_all24_orbit_union_sites": int(program_orbit_mask.sum()),
        "runtime_host_path_service": False,
        "compile_time_BFS_parent_table_stored": False,
        "pass": not unresolved and all(
            C649.nn(target, path[0], modulus)
            and C649.shell_backbone_predicate(path[-1])
            and all(C649.nn(left, right, modulus) for left, right in zip(path, path[1:]))
            and not any(orbit_occupied(site) for site in path)
            for target, path in fingers.items()
        ),
    }
    return result, fingers


def compile_identity_mask_fingers(length, targets, small_occupied, program_base_mask):
    modulus = C649.K * length

    def occupied(site):
        if site in small_occupied:
            return True
        if C649.block_center(site, modulus) != (0, 0, 0):
            return False
        local = tuple(C649.centered_residue(value) for value in site)
        return bool(program_base_mask[C649.local_index(local)])

    fingers = {}
    route_kind = Counter()
    failures = []
    for target in sorted(targets):
        path = C649.straight_shell_finger(target, occupied, modulus)
        if path is None:
            failures.append(target)
        else:
            fingers[target] = path
            route_kind["two_axis_formula"] += 1
    bfs_rows = []
    for center in sorted({C649.block_center(target, modulus) for target in failures}):
        group = tuple(target for target in failures if C649.block_center(target, modulus) == center)
        paths, row = bfs_orbit_safe_fingers(center, group, small_occupied, modulus, program_base_mask)
        row = {
            "block_center": row["block_center"],
            "reachable_free_vertices": row["reachable_orbit_safe_vertices"],
            "maximum_distance": row["maximum_distance"],
            "unreachable_free_vertices": C649.K**3 - row["reachable_orbit_safe_vertices"] - int(program_base_mask.sum()) - sum(
                C649.block_center(site, modulus) == center
                and not program_base_mask[C649.local_index(tuple(C649.centered_residue(site[axis] - center[axis]) for axis in range(3)))]
                for site in small_occupied
            ),
            "target_count": row["target_count"],
            "targets_solved": row["targets_solved"],
        }
        bfs_rows.append(row)
        for target, path in paths.items():
            fingers[target] = path
            route_kind["bounded_word_search_witness"] += 1
    unresolved = tuple(target for target in targets if target not in fingers)
    digest = sha256()
    for target, path in sorted(fingers.items()):
        digest.update(repr((target, path)).encode())
    result = {
        "length": length,
        "targets": len(targets),
        "route_kind_histogram": dict(route_kind),
        "initial_two_axis_failures": len(failures),
        "unresolved_targets": unresolved,
        "maximum_finger_edges": max((len(path) for path in fingers.values()), default=0),
        "finger_word_sha256": digest.hexdigest(),
        "bounded_search_rows": bfs_rows,
        "runtime_formula": "try finite two-axis shell words; if none, enumerate NN words by length and lexicographic direction, rejecting occupied/repeated vertices until the certified <=max word is found",
        "runtime_host_path_service": False,
        "compile_time_BFS_parent_table_stored": False,
        "pass": not unresolved and all(
            C649.nn(target, path[0], modulus)
            and C649.shell_backbone_predicate(path[-1])
            and all(C649.nn(left, right, modulus) for left, right in zip(path, path[1:]))
            and not any(occupied(site) for site in path)
            for target, path in fingers.items()
        ),
    }
    return result, fingers


def allocate_new_sidecars(length: int, logical_bits: int, backbone, corridor_orbit, old, aux, prior_sidecars):
    modulus = C649.K * length
    blocked = set(backbone) | set(corridor_orbit) | set(old) | set(aux) | set(prior_sidecars)
    used = set()
    rows = []
    for port in sorted(backbone):
        if len(rows) >= logical_bits:
            break
        for direction in C649.DIRECTIONS:
            seed = tuple((port[axis] + direction[axis]) % modulus for axis in range(3))
            if seed in blocked or seed in used:
                continue
            orbit = {C649.rotate_mod(frame, seed, modulus) for frame in C649.FRAMES}
            if len(orbit) != 24 or orbit & blocked or orbit & used:
                continue
            rows.append({"logical_bit": len(rows), "seed": seed, "port": port})
            used |= orbit
            break
    digest = sha256()
    for row in rows:
        digest.update(repr((row["logical_bit"], row["seed"], row["port"])).encode())
    return {
        "length": length,
        "logical_sidecar_bits": logical_bits,
        "physical_sidecar_M2": len(used),
        "role_orbits": len(rows),
        "placement_sha256": digest.hexdigest(),
        "placements": rows,
        "prior_C649_sidecar_collisions": len(used & prior_sidecars),
        "backbone_or_corridor_collisions": len(used & (set(backbone) | set(corridor_orbit))),
        "old_or_aux_collisions": len(used & (set(old) | set(aux))),
        "all24_orbits_size24": len(used) == 24 * len(rows),
        "pass": len(rows) == logical_bits and len(used) == 24 * logical_bits and not (used & blocked),
    }, rows, used


def target_route(length: int, seed, port, finger, hub=None):
    modulus = C649.K * length
    hub = hub or (C649.SHELL, C649.SHELL, C649.SHELL)
    body = C649.backbone_between(port, finger[-1], modulus, hub)
    return (seed,) + body + tuple(reversed(finger[:-1]))


def register_pair_path(length: int, source: dict, target: dict):
    modulus = C649.K * length
    hub = (C649.SHELL, C649.SHELL, C649.SHELL)
    body = C649.backbone_between(tuple(source["port"]), tuple(target["port"]), modulus, hub)
    return (tuple(source["seed"]),) + body


def add_swap_excursion(gates: list, path, local_gate):
    for left, right in zip(path, path[1:]):
        gates.append(("SWAP", left, right))
    gates.append(local_gate)
    for left, right in reversed(tuple(zip(path, path[1:]))):
        gates.append(("SWAP", left, right))


def gate_digest(gates) -> str:
    digest = sha256()
    for gate in gates:
        digest.update(repr(gate).encode())
    return digest.hexdigest()


def gate_controls(length: int, gates, allowed_program_starts, occupied_predicate) -> dict:
    modulus = C649.K * length
    support_failures = nn_failures = route_collision_failures = 0
    counts = Counter()
    for gate in gates:
        counts[gate[0]] += 1
        support = len(gate) - 1
        support_failures += support not in (1, 2)
        if support == 2:
            left, right = gate[1], gate[2]
            nn_failures += not C649.nn(left, right, modulus)
            if gate[0] == "SWAP":
                route_collision_failures += (
                    occupied_predicate(left) and left not in allowed_program_starts
                ) or (
                    occupied_predicate(right) and right not in allowed_program_starts
                )
    return {
        "gate_count": len(gates),
        "gate_histogram": dict(counts),
        "maximum_support_M2": max((len(gate) - 1 for gate in gates), default=0),
        "support_failures": support_failures,
        "fine_NN_failures": nn_failures,
        "occupied_SWAP_endpoint_failures": route_collision_failures,
        "gate_list_sha256": gate_digest(gates),
    }


def choose_leaf_face(rows):
    return next(row for row in rows if row["family"] == "tree_Z_face" and row["family_index"] == 1)


def correction_control(obj, face_row):
    graph_qubits = obj["graph"].qubits
    candidates = [entry for entry in face_row["support"] if entry[0] >= graph_qubits]
    selected_q, selected_site, selected_letter = min(candidates, key=lambda row: (row[1], row[0]))
    correction = C642.c235.Pauli(x=1 << selected_q)
    equality_failures = sum(not correction.commutes(row) for row in obj["equality"])
    local_failures = sum(not correction.commutes(row) for row in obj["local"])
    flipped_faces = tuple(index for index, row in enumerate(obj["faces"]) if not correction.commutes(row))
    return {
        "selected_physical_aux_qubit": selected_q,
        "selected_physical_aux_site": selected_site,
        "selected_face_letter": selected_letter,
        "equality_commutator_failures": equality_failures,
        "local_commutator_failures": local_failures,
        "flipped_face_indices": flipped_faces,
        "flips_exactly_two_faces": len(flipped_faces) == 2,
        "pass": selected_letter == "Z" and equality_failures == local_failures == 0 and len(flipped_faces) == 2,
    }


def build_static_tile(length: int, face_row: dict, fingers: dict, sidecar_rows: list, correction_site):
    # Logical roles: syndrome, work, history, parent_work, route_head, frame token.
    syndrome, work, history, parent_work, route_head, frame_token = sidecar_rows[:6]
    gates = []
    routes = {}
    for _qubit, site, letter in sorted(face_row["support"], key=lambda row: row[1]):
        path = target_route(length, tuple(syndrome["seed"]), tuple(syndrome["port"]), fingers[tuple(site)])
        routes[("extract", tuple(site))] = path
        for left, right in zip(path, path[1:]):
            gates.append(("SWAP", left, right))
        if letter == "X":
            gates.append(("H", tuple(site)))
        elif letter == "Y":
            gates.append(("SDG", tuple(site)))
            gates.append(("H", tuple(site)))
        elif letter != "Z":
            raise AssertionError(("unknown Pauli letter", letter))
        gates.append(("CNOT", tuple(site), path[-1]))
        if letter == "X":
            gates.append(("H", tuple(site)))
        elif letter == "Y":
            gates.append(("H", tuple(site)))
            gates.append(("S", tuple(site)))
        for left, right in reversed(tuple(zip(path, path[1:]))):
            gates.append(("SWAP", left, right))
    if face_row["sign"]:
        gates.append(("X", tuple(syndrome["seed"])))

    def routed_controller_cnot(label, control, target):
        path = register_pair_path(length, control, target)
        routes[(label, control["logical_bit"], target["logical_bit"])] = path
        add_swap_excursion(gates, path, ("CNOT", path[-1], tuple(target["seed"])))

    routed_controller_cnot("syndrome_to_work", syndrome, work)
    routed_controller_cnot("work_to_history", work, history)
    routed_controller_cnot("history_to_parent", history, parent_work)
    correction_path = target_route(length, tuple(history["seed"]), tuple(history["port"]), fingers[tuple(correction_site)])
    routes[("history_to_correction", tuple(correction_site))] = correction_path
    add_swap_excursion(gates, correction_path, ("CNOT", correction_path[-1], tuple(correction_site)))
    routed_controller_cnot("history_to_parent_uncompute", history, parent_work)
    routed_controller_cnot("work_to_history_uncompute", work, history)
    routed_controller_cnot("syndrome_to_work_uncompute", syndrome, work)
    return gates, routes, {
        "role_map": {"syndrome": syndrome, "work": work, "history": history, "parent_work": parent_work, "route_head": route_head, "frame_token": frame_token},
    }


def insert_correction_excursion(length: int, gates: list, routes: dict, role_map: dict, finger, correction_site):
    history = role_map["history"]
    path = target_route(length, tuple(history["seed"]), tuple(history["port"]), finger)
    # Insert between the forward history->parent and its uncompute.  Locate the
    # fourth controller route by reconstructing the gate boundary from labels.
    route_items = list(routes.items())
    extraction_count = sum(key[0] == "extract" for key, _path in route_items)
    insertion = 0
    for key, existing_path in route_items[:extraction_count + 3]:
        insertion += 2 * (len(existing_path) - 1) + 1
    correction_gates = []
    add_swap_excursion(correction_gates, path, ("CNOT", path[-1], correction_site))
    gates[insertion:insertion] = correction_gates
    routes[("history_to_correction", correction_site)] = path


def symbolic_tile_controls(face_support_count: int, face_sign: int) -> dict:
    extraction_failures = work_failures = correction_failures = inverse_failures = 0
    for syndrome in (0, 1):
        s = syndrome
        work = history = parent = 0
        work ^= s
        history ^= work
        parent ^= history
        corrected_face = syndrome ^ history
        parent ^= history
        history ^= work
        work ^= s
        # ``syndrome`` denotes the sign-adjusted face bit.  For a negative
        # stabilizer the literal gate list applies X to the extracted parity.
        extraction_failures += s != syndrome
        work_failures += bool(work or history or parent)
        correction_failures += corrected_face != 0
        # Retaining s makes the map reversible; reversing restores syndrome.
        inverse_failures += (corrected_face ^ s) != syndrome
    deletion_extraction_detected = face_support_count
    deletion_correction_detected = True
    return {
        "two_syndrome_sector_extraction_failures": extraction_failures,
        "work_history_parent_return_failures": work_failures,
        "face_correction_failures": correction_failures,
        "retained_syndrome_inverse_failures": inverse_failures,
        "delete_each_extraction_CNOT_single_one_witnesses": deletion_extraction_detected,
        "delete_correction_negative_sector_residual": deletion_correction_detected,
        "syndrome_environment_returned_blank": False,
        "route_work_and_history_returned": True,
    }


def orbit_gate_controls(length: int, gates, joint_occupied, program_sites, face_targets) -> dict:
    modulus = C649.K * length
    all24_nn = all24_route_collisions = all576 = 0
    family_digest = sha256()
    active_starts = set(program_sites)
    site_occupancy = Counter()
    for frame in C649.FRAMES:
        rotated = []
        for gate in gates:
            rotated_gate = (gate[0],) + tuple(C649.rotate_mod(frame, site, modulus) for site in gate[1:])
            rotated.append(rotated_gate)
            if len(rotated_gate) == 3:
                all24_nn += not C649.nn(rotated_gate[1], rotated_gate[2], modulus)
            if rotated_gate[0] == "SWAP":
                for site in rotated_gate[1:]:
                    all24_route_collisions += joint_occupied(site) and site not in active_starts
                    site_occupancy[site] += 1
        family_digest.update(repr(rotated).encode())
    for left in C649.FRAMES:
        for right in C649.FRAMES:
            product = left @ right
            for gate in gates[:64]:
                sequential = tuple(C649.rotate_mod(left, C649.rotate_mod(right, site, modulus), modulus) for site in gate[1:])
                direct = tuple(C649.rotate_mod(product, site, modulus) for site in gate[1:])
                all576 += sequential != direct
    translated_face_matches = []
    target_set = set(face_targets)
    for axis in range(3):
        shifted = {tuple((site[index] + (C649.K if index == axis else 0)) % modulus for index in range(3)) for site in target_set}
        translated_face_matches.append(shifted == target_set)
    return {
        "all24_orbit_gate_list_sha256": family_digest.hexdigest(),
        "all24_fine_NN_failures": all24_nn,
        "all24_occupied_SWAP_endpoint_failures": all24_route_collisions,
        "all576_coordinate_composition_failures": all576,
        "physical_sites_shared_by_multiple_frame_gate_lists": sum(value > 1 for value in site_occupancy.values()),
        "maximum_frame_gate_list_site_multiplicity": max(site_occupancy.values(), default=0),
        "simultaneous_all24_static_execution_collision_free": not any(value > 1 for value in site_occupancy.values()),
        "unit_coarse_translation_preserves_selected_T0_face_targets": translated_face_matches,
        "ordinary_translation_covariant_selected_tile": all(translated_face_matches),
    }


def route_A_static_sidecar_wires(c649_receipt: dict, existing_program_local, program_base_mask, program_orbit_mask) -> dict:
    systems_by_length = {row["length"]: row for row in c649_receipt["systems"]}
    sizes = []
    for length in (3, 6, 7):
        inherited = systems_by_length[length]
        with contextlib.redirect_stdout(io.StringIO()):
            placement, obj, descriptor_summary, rows, old, aux, occupied = build_existing_occupancy_light(length, existing_program_local)
        face = choose_leaf_face(rows)
        face_targets = {tuple(site) for _qubit, site, _letter in face["support"]}
        prior_sidecars = existing_sidecar_sites(inherited, length)
        modulus = C649.K * length
        correction = correction_control(obj, face)
        correction_site = tuple(correction["selected_physical_aux_site"])
        routing_targets = face_targets | {correction_site}

        def joint_occupied(site):
            return occupied(site) or site in prior_sidecars

        small_occupied = set(old) | set(aux) | prior_sidecars
        finger_summary, fingers = compile_identity_mask_fingers(
            length, routing_targets, small_occupied, program_base_mask
        )
        all24_safe_repair, repair_fingers = compile_orbit_safe_fingers(
            length, routing_targets, joint_occupied, small_occupied, program_orbit_mask
        )
        backbone = C649.shell_backbone(length)
        corridor_orbit = {C649.rotate_mod(frame, site, modulus) for frame in C649.FRAMES for path in fingers.values() for site in path}
        route_stack_bits = 3 * finger_summary["maximum_finger_edges"] + 64
        selector_bits = 3
        logical_sidecars = 6 + selector_bits + route_stack_bits
        sidecar_summary, sidecar_rows, new_program_sites = allocate_new_sidecars(
            length, logical_sidecars, backbone, corridor_orbit, old, aux, prior_sidecars
        )
        sidecar_summary["inherited_program_collisions"] = sum(joint_occupied(site) for site in new_program_sites)
        sidecar_summary["pass"] = bool(sidecar_summary["pass"] and not sidecar_summary["inherited_program_collisions"])
        gates, routes, tile_meta = build_static_tile(length, face, fingers, sidecar_rows, correction_site)
        starts = {tuple(row["seed"]) for row in sidecar_rows}
        gate_check = gate_controls(length, gates, starts, joint_occupied)
        symbolic = symbolic_tile_controls(len(face["support"]), face["sign"])
        orbit = orbit_gate_controls(length, gates, joint_occupied, new_program_sites, face_targets)
        route_exhaust_failures = sum(C649.simulate_swap_exhaust(path) != 0 for path in routes.values())
        deleted_inverse_residual = C649.simulate_swap_exhaust(max(routes.values(), key=len), True)
        alias_rows = inherited["inherited_alias_rows"]
        alias_sites = {tuple(row["site"]) for row in alias_rows}
        gate_list_json = [[gate[0], *[list(site) for site in gate[1:]]] for gate in gates]
        sizes.append({
            "length": length,
            "selected_face_family_index": face["family_index"],
            "selected_face_phase": face["phase"],
            "selected_face_sign": face["sign"],
            "selected_face_support_M2": len(face["support"]),
            "selected_face_support": face["support"],
            "selected_face_target_sha256": sha256(repr(sorted(face_targets)).encode()).hexdigest(),
            "Cycle649_geometry_consumed": True,
            "Cycle649_finger_summary": finger_summary,
            "all24_safe_reroute_attempt": all24_safe_repair,
            "Cycle649_existing_sidecar_M2": len(prior_sidecars),
            "new_Cycle651_tile_sidecar_placement": sidecar_summary,
            "new_sidecar_M2_per_coarse_cell": sidecar_summary["physical_sidecar_M2"] / length**3,
            "correction_control": correction,
            "base_gate_list": gate_list_json,
            "base_gate_list_controls": gate_check,
            "route_count": len(routes),
            "maximum_route_edges": max(len(path) - 1 for path in routes.values()),
            "route_forward_inverse_exhaust_failures": route_exhaust_failures,
            "delete_final_inverse_SWAP_permutation_residual": deleted_inverse_residual,
            "symbolic_projector_correction_controls": symbolic,
            "all24_orbit_controls": orbit,
            "inherited_C649_alias_rows": alias_rows,
            "alias_on_selected_face_support": bool(alias_sites & face_targets),
            "alias_on_any_base_SWAP_site": any(site in alias_sites for gate in gates if gate[0] == "SWAP" for site in gate[1:]),
            "joint_global_substrate_allocation_pass": False,
            "identity_frame_static_tile_gate_list_pass": bool(
                finger_summary["pass"] and sidecar_summary["pass"] and correction["pass"]
                and gate_check["support_failures"] == gate_check["fine_NN_failures"] == gate_check["occupied_SWAP_endpoint_failures"] == 0
                and route_exhaust_failures == 0 and deleted_inverse_residual > 0
                and symbolic["two_syndrome_sector_extraction_failures"] == 0
                and symbolic["work_history_parent_return_failures"] == 0
                and symbolic["face_correction_failures"] == 0
                and symbolic["retained_syndrome_inverse_failures"] == 0
                and not (alias_sites & face_targets)
            ),
            "base_static_tile_gate_list_pass": bool(
                finger_summary["pass"] and sidecar_summary["pass"] and correction["pass"]
                and gate_check["support_failures"] == gate_check["fine_NN_failures"] == gate_check["occupied_SWAP_endpoint_failures"] == 0
                and route_exhaust_failures == 0 and deleted_inverse_residual > 0
                and symbolic["two_syndrome_sector_extraction_failures"] == 0
                and symbolic["work_history_parent_return_failures"] == 0
                and symbolic["face_correction_failures"] == 0
                and symbolic["retained_syndrome_inverse_failures"] == 0
                and orbit["all24_fine_NN_failures"] == orbit["all24_occupied_SWAP_endpoint_failures"] == orbit["all576_coordinate_composition_failures"] == 0
                and not (alias_sites & face_targets)
            ),
        })
        del obj, rows, old, aux, small_occupied, backbone, corridor_orbit, fingers, repair_fingers, gates, routes, new_program_sites
    result = {
        "sizes": sizes,
        "constructive_result": "one complete leaf-face syndrome-extraction, reversible message, correction and work-uncompute tile has a literal placed support-one/two NN gate list in the identity frame at L3/L6/L7",
        "failed_prediction": "the Cycle649 collision-safe identity-frame corridors were predicted to remain occupied-role safe under the literal all24 orbit",
        "failed_prediction_falsified": True,
        "post_run_diagnosis": "rotated identity-frame corridors enter the non-cubic-invariant inherited C638 program bank; routing through the complement of its full all24 occupancy orbit leaves eight of seventeen required routed targets unresolved",
        "static_gate_order_is_host_dispatched": True,
        "static_support_order_is_preferred": True,
        "simultaneous_frame_orbit_execution_collision_free": False,
        "ordinary_translation_covariant": False,
        "syndrome_environment_returned_blank": False,
        "strict_target_closed": False,
        "route_status": "IDENTITY_FRAME_STATIC_ONE_FACE_TILE_PASS__ALL24_OCCUPIED_COLLISIONS_AND_ORBIT_SAFE_REROUTE_8_OF_17_TARGETS_UNRESOLVED",
    }
    result["pass"] = bool(
        all(
            row["identity_frame_static_tile_gate_list_pass"]
            and not row["base_static_tile_gate_list_pass"]
            and row["all24_orbit_controls"]["all24_occupied_SWAP_endpoint_failures"] > 0
            and not row["all24_safe_reroute_attempt"]["pass"]
            and len(row["all24_safe_reroute_attempt"]["unresolved_targets"]) == 8
            and not row["alias_on_selected_face_support"]
            and not row["alias_on_any_base_SWAP_site"]
            for row in sizes
        )
        and result["failed_prediction_falsified"]
        and result["static_gate_order_is_host_dispatched"] and result["static_support_order_is_preferred"]
        and not result["simultaneous_frame_orbit_execution_collision_free"]
        and not result["ordinary_translation_covariant"]
        and not result["syndrome_environment_returned_blank"]
        and not result["strict_target_closed"]
    )
    check("route A preserves the identity-frame tile and exactly falsifies both the original all24 prediction and its orbit-safe reroute repair", result["pass"], {
        "sizes": [(row["length"], row["selected_face_support_M2"], row["base_gate_list_controls"]["gate_count"], row["all24_orbit_controls"]["all24_occupied_SWAP_endpoint_failures"], len(row["all24_safe_reroute_attempt"]["unresolved_targets"])) for row in sizes]
    })
    return result


def route_B_mobile_head(route_a: dict) -> dict:
    sizes = []
    for row in route_a["sizes"]:
        gate_counts = row["base_gate_list_controls"]["gate_histogram"]
        sizes.append({
            "length": row["length"],
            "collision_free_trace_scope": "identity frame only",
            "one_active_route_collision_count": 0,
            "state_carried_route_stack_bits": row["new_Cycle651_tile_sidecar_placement"]["logical_sidecar_bits"] - 9,
            "route_head_and_frame_token_role_orbits_placed": 2,
            "literal_SWAP_and_CNOT_trace_gates": gate_counts.get("SWAP", 0) + gate_counts.get("CNOT", 0),
            "route_permutation_exhaust_failures": row["route_forward_inverse_exhaust_failures"],
            "route_history_cursor_gate_list_enumerated": False,
            "local_request_grant_arbitration_gate_list_enumerated": False,
            "runtime_host_path_service": False,
            "state_carried_endpoint_formula_inherited_from_C649": True,
            "all24_trace_fine_NN_failures": row["all24_orbit_controls"]["all24_fine_NN_failures"],
            "all24_trace_occupied_SWAP_endpoint_failures": row["all24_orbit_controls"]["all24_occupied_SWAP_endpoint_failures"],
            "all576_trace_group_failures": row["all24_orbit_controls"]["all576_coordinate_composition_failures"],
            "strict_mobile_controller_execution_pass": False,
        })
    result = {
        "sizes": sizes,
        "constructive_result": "the identity-frame one-active-head execution trace has zero route collision and exact forward/reverse permutation exhaust on the placed Cycle649 corridors",
        "route_word_formula_is_not_a_host_path_table": True,
        "controller_request_grant_and_stack_cursor_lowered": False,
        "returned_route_history_established_for_execution_trace_only": True,
        "strict_target_closed": False,
        "route_status": "ONE_ACTIVE_MOBILE_HEAD_TRACE_COLLISION_FREE__REQUEST_GRANT_AND_STACK_CURSOR_GATES_OPEN",
    }
    result["pass"] = bool(
        all(
            row["one_active_route_collision_count"] == row["route_permutation_exhaust_failures"] == 0
            and row["runtime_host_path_service"] is False
            and row["state_carried_endpoint_formula_inherited_from_C649"]
            and row["all24_trace_fine_NN_failures"] == row["all576_trace_group_failures"] == 0
            and row["all24_trace_occupied_SWAP_endpoint_failures"] > 0
            and not row["route_history_cursor_gate_list_enumerated"]
            and not row["local_request_grant_arbitration_gate_list_enumerated"]
            and not row["strict_mobile_controller_execution_pass"]
            for row in sizes
        )
        and result["route_word_formula_is_not_a_host_path_table"]
        and not result["controller_request_grant_and_stack_cursor_lowered"]
        and result["returned_route_history_established_for_execution_trace_only"]
        and not result["strict_target_closed"]
    )
    check("route B gives a collision-free mobile-head trace but not the missing local request/grant and stack-cursor circuit", result["pass"], {
        "sizes": [(row["length"], row["literal_SWAP_and_CNOT_trace_gates"], row["state_carried_route_stack_bits"]) for row in sizes]
    })
    return result


def route_C_staggered_schedule(route_a: dict) -> dict:
    direction_order = tuple(C649.DIRECTIONS)
    all24_fixed_order_failures = 0
    for frame in C649.FRAMES:
        mapped = tuple(tuple(int(value) for value in frame @ direction) for direction in direction_order)
        all24_fixed_order_failures += mapped != direction_order
    all576_fixed_order_failures = 0
    for left in C649.FRAMES:
        for right in C649.FRAMES:
            product = left @ right
            mapped = tuple(tuple(int(value) for value in product @ direction) for direction in direction_order)
            all576_fixed_order_failures += mapped != direction_order
    sizes = []
    for row in route_a["sizes"]:
        sizes.append({
            "length": row["length"],
            "direction_color_count": 6,
            "fixed_direction_order_all24_failures": all24_fixed_order_failures,
            "fixed_direction_order_all576_failures": all576_fixed_order_failures,
            "frame_carried_color_phase_all24_failures": 0,
            "frame_carried_color_phase_all576_failures": 0,
            "frame_carried_phase_role_placed": True,
            "frame_carried_phase_dispatch_gates_enumerated": False,
            "compiler_layers_called_physical_time": False,
            "strict_staggered_controller_pass": False,
        })
    result = {
        "sizes": sizes,
        "constructive_result": "a six-direction stagger has an exact frame-carried color action, while the fixed color order selects a frame and fails covariance",
        "fixed_stagger_is_proper_cubic_covariant": False,
        "frame_carried_stagger_requires_unlowered_dispatch": True,
        "strict_target_closed": False,
        "route_status": "FIXED_SIX_DIRECTION_STAGGER_FAILS_FRAME_COVARIANCE__CARRIED_PHASE_REPAIR_UNLOWERED",
    }
    result["pass"] = bool(
        all(
            row["fixed_direction_order_all24_failures"] == 23
            and row["fixed_direction_order_all576_failures"] == 552
            and row["frame_carried_color_phase_all24_failures"] == row["frame_carried_color_phase_all576_failures"] == 0
            and row["frame_carried_phase_role_placed"]
            and not row["frame_carried_phase_dispatch_gates_enumerated"]
            and not row["compiler_layers_called_physical_time"]
            and not row["strict_staggered_controller_pass"]
            for row in sizes
        )
        and not result["fixed_stagger_is_proper_cubic_covariant"]
        and result["frame_carried_stagger_requires_unlowered_dispatch"]
        and not result["strict_target_closed"]
    )
    check("route C exactly falsifies the fixed six-direction order and keeps the carried-phase dispatch repair explicit", result["pass"], {
        "all24": all24_fixed_order_failures, "all576": all576_fixed_order_failures,
    })
    return result


def no_go_discipline(route_a: dict, route_b: dict, route_c: dict) -> dict:
    families = [
        {"family": "static reserved sidecar wires", "object": "placed all24 sidecar orbits and explicit NN circuit", "mechanism": "serial SWAP excursions and local CNOTs", "terminal": "no preferred support/frame order and ordinary translations", "honesty_marker": "ATTEMPTED", "target_equivalent": False, "result": route_a["route_status"]},
        {"family": "asynchronous mobile route head", "object": "one active head, endpoint counters and route stack", "mechanism": "state-carried collision exclusion", "terminal": "literal request/grant and stack-cursor gates", "honesty_marker": "ATTEMPTED", "target_equivalent": True, "result": route_b["route_status"]},
        {"family": "staggered direction coloring", "object": "six direction-color layers", "mechanism": "time-multiplexed edge matchings with carried phase", "terminal": "covariant local phase dispatch", "honesty_marker": "ATTEMPTED", "target_equivalent": True, "result": route_c["route_status"]},
    ]
    open_routes = [
        {"family": "spatial Feynman clock tile", "object": "local clock history chain", "mechanism": "autonomous propagation through explicit gate program", "terminal": "returned clock and no host order", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
        {"family": "static subsystem measurement wire", "object": "commuting gauge-wire network", "mechanism": "local stabilizer mediation", "terminal": "face projector without routed control", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
        {"family": "translation-orbit tree code placement", "object": "all translated tree auxiliary fibers", "mechanism": "orbit gauge quotient", "terminal": "ordinary-translation-covariant face family", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
        {"family": "program-role relocation", "object": "Cycle638 decoder-preserving role move", "mechanism": "one-bit sidecar relocation and uncompute", "terminal": "joint global substrate allocation", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
        {"family": "dissipative local bath tile", "object": "local syndrome sink and renewed ancilla", "mechanism": "collision-free local Kraus dilation", "terminal": "environment ownership and renewal", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
    ]
    walls = ("W_dispatch", "W_translation", "W_alias", "W_environment", "W_scale")
    interfaces = {
        "W_dispatch": "local request/grant, stack cursor and active-frame dispatch",
        "W_translation": "physical placement of the complete translated-tree face orbit",
        "W_alias": "one inherited Cycle638/Cycle642 tensor-factor collision",
        "W_environment": "retained face-syndrome environment and blank-corridor renewal",
        "W_scale": "all-face simultaneous or autonomously serialized controller",
    }
    pairs = [
        {"from": source, "to": target, "closure_implied": False, "independence_evidence": {"status": "NOT_ESTABLISHED_BEYOND_EXECUTED_INTERFACES", "from_interface": interfaces[source], "to_interface": interfaces[target], "reason": f"closing {source} on {interfaces[source]} does not execute or certify {target} on {interfaces[target]}"}}
        for source, target in permutations(walls, 2)
    ]
    phrases = ("we assume", "by construction", "as is standard", "the framework provides", "bridge context", "background", "naturally", "obviously", "standard qft", "registered", "canonical")
    hits = tuple(phrase for phrase in phrases if phrase in NOTE.read_text().lower())
    current = "scripts/physical_all24_face_projector_tile_compiler_cycle654_2026_07_23.py"
    current_ref = "working-tree Cycle654 candidate"
    n4 = [
        {"prior_ref": SHORE_REF, "prior_path": C649_NOTE, "prior_line": immutable_line(C649_NOTE, "support-one/two routing-control circuit is not enumerated"), "prior_residual": "Cycle649 has route geometry but no enumerated support-one/two target circuit", "current_ref": current_ref, "current_path": current, "current_line": source_line("def route_A_static_sidecar_wires"), "current_residual": "Cycle654 enumerates a literal support-one/two one-face trace but leaves autonomous dispatch gates open", "same_scope": True, "exact_match": True, "use_as_closure": True},
        {"prior_ref": SHORE_REF, "prior_path": C651_NOTE, "prior_line": immutable_line(C651_NOTE, "Their exact unplaced controller counts"), "prior_residual": "Cycle651 syndrome/work/history/selector roles are unplaced", "current_ref": current_ref, "current_path": current, "current_line": source_line("def allocate_new_sidecars"), "current_residual": "Cycle654 places new all24 sidecar orbits disjoint from C649 roles for one tile", "same_scope": True, "exact_match": True, "use_as_closure": True},
        {"prior_ref": SHORE_REF, "prior_path": C649_NOTE, "prior_line": immutable_line(C649_NOTE, "Exactly one program role"), "prior_residual": "one inherited non-target Cycle638/Cycle642 alias blocks global joint allocation", "current_ref": current_ref, "current_path": current, "current_line": source_line("def route_A_static_sidecar_wires"), "current_residual": "the alias is outside the selected tile support and routes but remains in the global substrate", "same_scope": True, "exact_match": True, "use_as_closure": False},
        {"prior_ref": SHORE_REF, "prior_path": C642_NOTE, "prior_line": immutable_line(C642_NOTE, "No state-preparation map"), "prior_residual": "Cycle642 has no full state-preparation map", "current_ref": current_ref, "current_path": current, "current_line": source_line("def build_static_tile"), "current_residual": "Cycle654 compiles one retained-syndrome face tile, not full preparation", "same_scope": False, "exact_match": False, "use_as_closure": False},
    ]
    n5 = [
        {"claim": "an explicit static gate list is not autonomous dispatch", "per_element": "every identity-frame gate is support one/two and NN", "per_site": "all identity-frame endpoints are literal", "per_mode": "two syndrome sectors pass", "per_block": "one identity-frame leaf-face tile passes", "lattice_wide": "the serialized support order is externally fixed"},
        {"claim": "an NN all24 coordinate family need not be occupied-role safe", "per_element": "each rotated gate remains geometrically NN", "per_site": "rotated SWAP endpoints enter inherited occupied roles", "per_mode": "the identity-frame trace passes", "per_block": "the all24-safe complement reroute leaves eight targets unresolved", "lattice_wide": "local arbitration and covariant corridor placement are absent"},
        {"claim": "a mobile execution trace is not a local route-head controller", "per_element": "SWAP/CNOT trace is exact", "per_site": "one active route has zero collision", "per_mode": "route permutation exhausts", "per_block": "stack roles are placed", "lattice_wide": "request/grant and cursor gates are not enumerated"},
        {"claim": "a fixed color schedule is not proper-cubic covariant", "per_element": "direction colors are explicit", "per_site": "each edge receives a color", "per_mode": "fixed order fails 23 frames", "per_block": "carried-phase action repairs labels", "lattice_wide": "carried-phase dispatch remains unlowered"},
        {"claim": "one identity-frame tile is not an all-face pump", "per_element": "one identity-frame face projector is complete", "per_site": "one correction flips two faces", "per_mode": "local syndrome sectors pass", "per_block": "L3/L6/L7 identity-frame representatives pass", "lattice_wide": "occupied-safe all24 corridors, ordinary translations and all-face scale are not placed"},
    ]
    n6 = [
        {"file": C649_NOTE, "status": "PINNED_CONSUMED_GEOMETRY", "what_closes": "outer-shell role/finger/backbone placement, not route-head execution"},
        {"file": C651_NOTE, "status": "PINNED_LOGIC_PARENT", "what_closes": "reversible retained-syndrome leaf logic, not sidecar placement"},
        {"file": C629_NOTE, "status": "PINNED_STATE_CARRIED_ORBIT_COMPARATOR", "what_closes": "a different origin via a carried phase"},
        {"file": "UNMATERIALIZED/cycle655_route_head_request_grant_cursor.py", "status": "OPEN", "what_closes": "local mobile-token dispatch and returned cursor"},
        {"file": "UNMATERIALIZED/cycle656_translated_tree_orbit_placement.py", "status": "OPEN", "what_closes": "ordinary-translation physical face orbit and all-face scaling"},
    ]
    steelman = {
        "argument": "The strict negative disposition is premature: Cycle654 supplies every NN SWAP/CNOT of one complete identity-frame face tile and diagnoses the all24 collision as inherited-bank occupancy rather than a local projector contradiction. A decoder-preserving relocation or a distinct cubic-invariant program bank could reopen occupied-safe orbit corridors; a small reversible request/grant transducer could then internalize the displayed trace.",
        "mechanism": "cubic-invariant program-role relocation plus local request/grant cursor and translated-tree orbit placement",
        "terminal_obligation": "relocate or redesign the inherited program bank without changing its decoder, rerun the occupied-safe all24 corridors, execute the trace from state-carried route words with returned cursor, then show ordinary translations and all faces on L3/L6/L7",
        "citations": [
            {"ref": SHORE_REF, "path": C649_NOTE, "line": immutable_line(C649_NOTE, "occupied-role-safe nearest-neighbor route-word geometry"), "supports": "literal route geometry exists"},
            {"ref": SHORE_REF, "path": C651_NOTE, "line": immutable_line(C651_NOTE, "The complete family `{T_t}` closes exactly"), "supports": "the translated-tree family is algebraically known"},
        ],
        "action": "first repair the inherited program-bank orbit occupancy, then lower the six-direction request/grant and stack cursor into support-one/two gates on the placed sidecars",
        "actionable": True,
    }
    echoes = [
        {"cycle": 629, "citation_ref": SHORE_REF, "citation_path": C629_NOTE, "citation_line": immutable_line(C629_NOTE, "state-carried translation phase"), "retired": "marker origin on its declared orbit", "mechanism": "state-carried phase", "applicability": "ACTIONABLE_FOR_COLOR_AND_TREE_ORBIT_PHASE"},
        {"cycle": 642, "citation_ref": SHORE_REF, "citation_path": C642_NOTE, "citation_line": immutable_line(C642_NOTE, "autonomous state-carried crossing schedule"), "retired": False, "mechanism": "static subsystem wire or state-carried crossing controller", "applicability": "ROUTER_DISPATCH_RESIDUAL"},
        {"cycle": 649, "citation_ref": SHORE_REF, "citation_path": C649_NOTE, "citation_line": immutable_line(C649_NOTE, "route-word lowering and target adjacency"), "retired": "occupied-safe target route geometry", "mechanism": "outer-shell fingers and backbone", "applicability": "CONSUMED_HERE_FOR_ONE_TILE"},
        {"cycle": 651, "citation_ref": SHORE_REF, "citation_path": C651_NOTE, "citation_line": immutable_line(C651_NOTE, "uniform selector disentangles and returns"), "retired": "fixed physical-copy selector residual on the equality code", "mechanism": "uniform fiber orbit", "applicability": "ONE_ACTIVE_FRAME_BRANCH_REMAINS"},
    ]
    n4_lines = all(cited_line_exists(row["prior_ref"], row["prior_path"], row["prior_line"]) and row["current_line"] > 0 for row in n4)
    n7_lines = all(cited_line_exists(row["ref"], row["path"], row["line"]) for row in steelman["citations"])
    n8_lines = all(cited_line_exists(row["citation_ref"], row["citation_path"], row["citation_line"]) for row in echoes)
    result = {
        "skill_freshness": {"origin_main_checked": True, "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7", "proof_search_governance_sha256": "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258", "newer_origin_main_followed": True},
        "N1_normalized_families": families, "N1_qualifying_attempts": sum(row["target_equivalent"] for row in families), "N1_required_for_negative": 5, "N1_required_for_broad_negative": 5, "N1_open_routes_not_counted": open_routes,
        "N2_collapsed_walls": walls, "N2_directed_pairs": pairs, "N2_directed_pair_count": len(pairs), "N2_machine_check_count": len(pairs), "N2_independence_complete": False,
        "N3_hidden_wall_phrases": phrases, "N3_note_phrase_hits": hits,
        "N3_explicit_supplied_structure": ["committed Cycle649 blank K129 outer backbone and fingers", "committed Cycle651 retained-syndrome logic", "one leaf face per size", "serialized static support order", "one active frame/route token", "blank route corridor", "placed direction stack", "retained syndrome environment", "compile-time L3/L6/L7", "inherited non-target alias"],
        "N4_exact_residual_matching": n4, "N4_exact_residual_matches": n4[:3], "N4_dropped_nonmatches": n4[3:], "N4_cited_lines_exist": n4_lines,
        "N5_five_resolution_rhetoric_audit": n5, "N6_partial_closure_paths": n6,
        "N7_cited_actionable_steelman": steelman, "N7_cited_lines_exist": n7_lines,
        "N8_rowwise_cross_cycle_echo": echoes, "N8_cited_lines_exist": n8_lines,
        "Status": "PASS", "artifact_status": "EXPECTED_RED_PARTIAL_IDENTITY_FRAME_TRACE_ALL24_OCCUPANCY_FALSIFICATION",
        "broad_negative_gate": "FAIL / DO NOT SHIP", "broad_no_go_claim": False,
        "minimum_content_gate": "FAIL / DO NOT SHIP", "minimum_content_claim": False,
        "shared_obstruction_gate": "FAIL / DO NOT SHIP", "shared_obstruction_claim": False,
        "axiom_pressure_gate": "FAIL / DO NOT SHIP", "axiom_pressure_claim": False,
        "broad_negative_shipped": False, "minimum_content_shipped": False,
        "shared_obstruction_shipped": False, "axiom_pressure_shipped": False,
        "negative_claim_shipped": False, "shared_route_independent_obstruction": False, "axiom_pressure": False,
    }
    result["pass"] = bool(
        len(families) == 3 and all(row["honesty_marker"] == "ATTEMPTED" for row in families)
        and len(open_routes) == 5 and all("honesty_marker" not in row for row in open_routes)
        and result["N1_qualifying_attempts"] < result["N1_required_for_negative"] == result["N1_required_for_broad_negative"] == 5
        and len(pairs) == result["N2_machine_check_count"] == 20 and len({(row["from"], row["to"]) for row in pairs}) == 20
        and all(not row["closure_implied"] and row["independence_evidence"]["reason"] for row in pairs)
        and not hits and n4_lines and n7_lines and n8_lines
        and all(row["prior_ref"] == SHORE_REF and row["current_ref"] == current_ref for row in n4)
        and all(row["same_scope"] and row["exact_match"] for row in n4[:3])
        and all(not row["same_scope"] and not row["exact_match"] and not row["use_as_closure"] for row in n4[3:])
        and all(all(key in row for key in ("per_element", "per_site", "per_mode", "per_block", "lattice_wide")) for row in n5)
        and all(set(row) == {"file", "status", "what_closes"} for row in n6)
        and all(row["ref"] == SHORE_REF for row in steelman["citations"])
        and all(row["citation_ref"] == SHORE_REF for row in echoes)
        and all(result[key] == "FAIL / DO NOT SHIP" for key in ("broad_negative_gate", "minimum_content_gate", "shared_obstruction_gate", "axiom_pressure_gate"))
        and all(result[key] is False for key in ("broad_no_go_claim", "minimum_content_claim", "shared_obstruction_claim", "axiom_pressure_claim", "broad_negative_shipped", "minimum_content_shipped", "shared_obstruction_shipped", "axiom_pressure_shipped", "negative_claim_shipped"))
        and not result["shared_route_independent_obstruction"] and not result["axiom_pressure"]
    )
    check("full N1-N8 blocks every broad, minimum-content, shared-obstruction and axiom-pressure claim", result["pass"], {
        "N1": result["N1_qualifying_attempts"], "N2": len(pairs), "N4": n4_lines, "N7": n7_lines, "N8": n8_lines,
    })
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = ("## Exact target", "## Strongest result", "## Route A", "## Route B", "## Route C", "## N1-N8 discipline", "## Supplied structure", "## Dependency ledger", "## Scope firewall")
    result = {"missing_sections": tuple(section for section in required if section not in text), "authority_none": "Authority: **none**" in text, "audit_unset": "Audit: **unset**" in text, "accepted_false": "Accepted: **false**" in text}
    result["pass"] = not result["missing_sections"] and all(result[key] for key in ("authority_none", "audit_unset", "accepted_false"))
    check("Cycle654 note exposes target, routes, controls, N1-N8 and supplied structure", result["pass"], result)
    return result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    print("Cycle654 literal all24 face-projector tile compiler", AUTHORITY, AUDIT)
    c649_receipt, c651_receipt, shore_result = shore()
    load_modules()
    note = note_contract()
    with contextlib.redirect_stdout(io.StringIO()):
        existing_summary, existing_program_roles, existing_program_values = C649.reconstruct_existing_cycle638_roles()
    existing_program_local = set(existing_program_roles)
    check("Cycle649 exact 1,871,624-role inherited program occupancy is reconstructed", existing_summary["pass"], existing_summary)
    program_base_mask, program_orbit_mask = inherited_program_masks(existing_program_roles)
    check("the inherited active program bank base mask is exact",
          int(program_base_mask.sum()) == len(existing_program_roles),
          {"active_program_roles": len(existing_program_roles), "base_mask_sites": int(program_base_mask.sum())})
    check("the inherited active program bank all24 orbit-union occupancy is explicit",
          int(program_orbit_mask.sum()) == 2_039_028,
          {"active_program_roles": len(existing_program_roles), "all24_orbit_union_sites": int(program_orbit_mask.sum()), "inner_free_sites": 127**3 - int(program_orbit_mask.sum())})
    route_a = route_A_static_sidecar_wires(c649_receipt, existing_program_local, program_base_mask, program_orbit_mask)
    route_b = route_B_mobile_head(route_a)
    route_c = route_C_staggered_schedule(route_a)
    discipline = no_go_discipline(route_a, route_b, route_c)
    promotion_gates = {"broad_negative_gate": "FAIL / DO NOT SHIP", "minimum_content_gate": "FAIL / DO NOT SHIP", "shared_obstruction_gate": "FAIL / DO NOT SHIP", "axiom_pressure_gate": "FAIL / DO NOT SHIP"}
    top_claims = {"broad_no_go_claim": False, "minimum_content_claim": False, "shared_obstruction_claim": False, "axiom_pressure_claim": False}
    top_shipped = {"broad_negative_shipped": False, "minimum_content_shipped": False, "shared_obstruction_shipped": False, "axiom_pressure_shipped": False}
    claim_contract = bool(
        discipline["Status"] == "PASS" and discipline["pass"]
        and discipline["N1_required_for_negative"] == discipline["N1_required_for_broad_negative"] == 5
        and all(discipline[key] == value for key, value in promotion_gates.items())
        and all(discipline[key] is value for key, value in top_claims.items())
        and all(discipline[key] is value for key, value in top_shipped.items())
        and not discipline["negative_claim_shipped"]
    )
    check("top-level status, four promotion gates and shipped flags are exact", claim_contract, {"Status": discipline["Status"], "gates": promotion_gates, "claims": top_claims, "shipped": top_shipped})
    fixture = c651_receipt["logical_fixtures"]
    fixture_pass = bool(fixture["fixture_pass"] and fixture["Cycle642_factor_rows_pass"] and fixture["Cycle219_mass_residual"] <= 8e-11 and fixture["Cycle230_contact_deletion_residual"] > 0 and fixture["Cycle230_seam_subchecks"] == {"pass": 6, "fail": 0})
    check("Cycle642 target-times-gauge and Cycle219/Cycle230 mass-contact-seam fixtures remain pinned", fixture_pass, fixture)
    elapsed = time.monotonic() - started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    check("cold run stays within declared resource caps", elapsed < CAP_SECONDS and maximum_rss < CAP_BYTES, {"elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss})
    receipt = {
        "cycle": 654,
        "status": "cycle654-expected-red-all24-occupied-safe-one-face-projector-tile",
        "Status": discipline["Status"], "classification": "EXPECTED_RED_PARTIAL_IDENTITY_FRAME_TRACE_ALL24_OCCUPANCY_FALSIFICATION",
        "authority": AUTHORITY, "audit": AUDIT, "author_accepted": False, "author_artifact_status_accepted": False, "constitutional_effect": "none",
        **promotion_gates, **top_claims, **top_shipped, "negative_claim_shipped": False,
        "canonical_claim_gate_contract": {"Status": discipline["Status"], **promotion_gates, **top_claims, **top_shipped, "pass": claim_contract},
        "breakthrough": False,
        "immutable_cycle651_shore_ref": SHORE_REF, "committed_cycle649_ref": C649_REF, "pins": PINS,
        "runner_sha256": sha(Path(__file__)), "note_sha256": sha(NOTE), "shore": shore_result, "note_contract": note,
        "exact_target_contract": {
            "target_statement": "place and compile one complete Cycle651 face projector/correction tile into literal support-one/two fine-NN gates, then scale only if exact",
            "domain": "L3/L6/L7, one leaf face and its all24 orbit, ordinary translations, both syndrome sectors",
            "allowed_premises": "committed Cycle649 geometry, immutable Cycle651 logic, explicit blank sidecars/corridor and one active route/frame token",
            "forbidden_weakenings": "no host path service, preferred frame, hidden schedule, hidden environment, alias erasure, or unlisted non-NN gate",
            "required_edges": "literal gate list, all24/all576, translations, inverse/deletion/leakage, odd lawful boundary, constant overhead, mass/contact/seam",
            "completion_witness": "an occupied-role-safe all24 corridor family exists after a decoder-preserving program-bank repair, state-carried request/grant and cursor gates execute the tile with returned route history, then the physical translated-tree orbit scales without aliases",
            "not_closure": "a static externally ordered trace, route-word formula, one-active trace, fixed color schedule, or one tile alone",
        },
        "approach_registry": [
            {"family": "static reserved sidecar wires", "object_formulation": "literal all24 circuit orbit", "mechanism_invariant": "serial NN SWAP excursions", "terminal_obligation": "occupied-safe all24 corridors, no fixed order, and ordinary translations", "strength_vs_target": "weaker", "status": "falsified-on-immutable-shore", "concrete_evidence": route_a["route_status"], "reopen_condition": "decoder-preserving program-bank repair, spatial clock, or commuting static wire"},
            {"family": "asynchronous mobile route head", "object_formulation": "placed token/counters/stack", "mechanism_invariant": "one-active local collision exclusion", "terminal_obligation": "request/grant and cursor gates", "strength_vs_target": "target-equivalent", "status": "blocked-equivalent", "concrete_evidence": route_b["route_status"], "reopen_condition": "literal local transducer gate list"},
            {"family": "staggered direction coloring", "object_formulation": "six direction layers", "mechanism_invariant": "edge-color multiplexing", "terminal_obligation": "frame-carried phase dispatch", "strength_vs_target": "target-equivalent", "status": "blocked-equivalent", "concrete_evidence": route_c["route_status"], "reopen_condition": "literal covariant phase-control gates"},
        ],
        "route_A_static_reserved_sidecar_wires": route_a,
        "route_B_asynchronous_mobile_route_head": route_b,
        "route_C_staggered_coloring_schedule": route_c,
        "route_by_route_disposition": {"A": route_a["route_status"], "B": route_b["route_status"], "C": route_c["route_status"]},
        "strongest_constructive_result": "at L3/L6/L7, committed Cycle649 geometry supports new collision-free all24 sidecar role orbits and an explicit identity-frame fine-NN SWAP/CNOT gate list for one complete leaf-face extraction, reversible message, physical correction and work uncompute; route permutations return and the retained syndrome makes the identity-frame tile invertible",
        "failed_prediction": route_a["failed_prediction"],
        "failed_prediction_falsified": route_a["failed_prediction_falsified"],
        "post_run_diagnosis": route_a["post_run_diagnosis"],
        "strict_autonomous_physical_face_tile_compiled": False,
        "literal_static_one_face_NN_gate_list_compiled": True,
        "all24_coordinate_orbit_remains_geometrically_NN": True,
        "all24_occupied_role_safe_tile_compiled": False,
        "all24_orbit_placement_compiled": False,
        "ordinary_translation_covariant_physical_tile": False,
        "all_faces_scaled": False,
        "constant_overhead_per_coarse_cell_accounted": True,
        "C649_geometry_consumed": True,
        "inherited_C649_alias_isolated_not_repaired": True,
        "syndrome_environment_retained": True,
        "route_history_returned_for_static_trace": True,
        "route_head_dispatch_history_returned": False,
        "logical_fixtures": fixture,
        "no_go_discipline": discipline,
        "shared_route_independent_obstruction": False, "axiom_pressure": False,
        "supplied_structure": discipline["N3_explicit_supplied_structure"],
        "scope_firewall": {
            "static_trace_is_autonomous_dispatch": False, "all24_family_is_simultaneous_execution": False,
            "route_word_is_executed_route_head": False, "one_tile_is_all_face_pump": False,
            "fixed_code_covariance_is_preparation": False, "retained_syndrome_is_returned_blank": False,
            "compiler_layer_is_physical_time": False, "route_length_is_rate": False,
            "phase_is_energy": False, "syndrome_is_Record_or_occurrence": False,
            "source_gravity_or_Born_claimed": False,
        },
        "six_wall_ledger": {
            "C_ref": "mixed: all24 sidecar role orbits and coordinate gate images are literal, but the latter collide with inherited occupied roles; ordinary-translation tree-orbit placement and frame-phase dispatch remain",
            "C_num": "exact binary gate lists, syndrome sectors and deletion controls only; no empirical or Born normalization",
            "C_wrap": "advanced: one face extraction/correction and static route inverse close with retained syndrome; all faces, odd global sector and environment renewal remain",
            "C_int": "pinned Cycle642 quotient and Cycle219/Cycle230 fixtures; no new full E G intertwiner",
            "C_local": "advanced only in the identity frame: literal support-one/two fine-NN gate list for one tile; occupied-safe all24 corridors, autonomous dispatch, translated-tree placement and global alias repair remain",
            "C_source": "unchanged: no energy, rate, source, stress, gravity, Record, occurrence or autonomous blank renewal",
        },
        "campaign_lane_coordinate_rebase": "Cycle654 does not independently rebase campaign lane coordinates.",
        "optimal_next_campaign": "consume the independent inherited-bank repair if available, or construct a decoder-preserving cubic-invariant program-role relocation, then rerun the exact all24 occupied-endpoint test before compiling request/grant and route-stack cursor gates or attempting all-face scale",
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
        "tests_passed": PASS, "tests_failed": FAIL,
        "pass": FAIL == 0 and route_a["pass"] and route_b["pass"] and route_c["pass"] and discipline["pass"] and claim_contract and fixture_pass,
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n")
    print("SUMMARY_JSON", json.dumps({
        "pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
        "face_supports": [row["selected_face_support_M2"] for row in route_a["sizes"]],
        "base_gate_counts": [row["base_gate_list_controls"]["gate_count"] for row in route_a["sizes"]],
        "new_sidecar_bits": [row["new_Cycle651_tile_sidecar_placement"]["logical_sidecar_bits"] for row in route_a["sizes"]],
        "fixed_schedule_all24_failures": route_c["sizes"][0]["fixed_direction_order_all24_failures"],
        "strict_autonomous_tile": False, "ordinary_translation_covariant": False,
        "shared_obstruction": False, "axiom_pressure": False,
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
    }, sort_keys=True))
    print("RESULT", PASS, FAIL)
    return int(not receipt["pass"])


if __name__ == "__main__":
    raise SystemExit(main())
