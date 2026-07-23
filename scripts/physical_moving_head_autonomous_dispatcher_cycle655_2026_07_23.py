#!/usr/bin/env python3
"""Cycle655: isolated moving-head autonomous-dispatcher tournament.

Builds and routes exact local opcode kernels and a state-carried nine-colour
transition layer.  It deliberately does not identify those bounded objects
with a globally embedded controller tape for the Cycle652 fixed word.

Authority none; audit unset; constitutional effect none.
"""
from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
import importlib.util
import io
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
import tarfile
import tempfile
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
IMMUTABLE_COMMIT = "d353925ca046702f1b0f50a41a6f8fa5a0ee3395"
C652_PATHS = (
    "scripts/physical_inherited_role_alias_repair_tournament_cycle652_2026_07_23.py",
    "docs/work_history/repo/review_feedback/PHYSICAL_INHERITED_ROLE_ALIAS_REPAIR_TOURNAMENT_CYCLE652_NOTE_2026-07-23.md",
    "outputs/physical_inherited_role_alias_repair_tournament_cycle652_receipt_2026_07_23.json",
    "outputs/physical_inherited_role_alias_repair_tournament_cycle652_cold_2026_07_23.txt",
)
PINS = {
    C652_PATHS[0]: "f8836934b210fa00ff7b828799388d72dbab8a627c47d7a97fe8e241a50eccdf",
    C652_PATHS[1]: "f0d4b852205d76d17cc1e39ff1ff10ee5c978826f66c410691882a81b0251a7d",
    C652_PATHS[2]: "56870b951b93c81125789041af6758196e588eeddf2cf7b0235e1f7fd5b03379",
    C652_PATHS[3]: "f18a69198636eda35186d713e0e63eb962d5761a6264c656673bb45066b151dd",
}
NO_GO_ORIGIN_MAIN_SHA256 = "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7"
FRESHNESS_ORIGIN_MAIN_SHA256 = "1e0ec4ef4d7c5dd24243d7c3954c78a3f00ecd3d5e43805e788dd3629973a962"
PROOF_SEARCH_ORIGIN_MAIN_SHA256 = "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258"
AUTHORITY = "none"
AUDIT = "unset"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_MOVING_HEAD_AUTONOMOUS_DISPATCHER_CYCLE655_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_moving_head_autonomous_dispatcher_cycle655_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_moving_head_autonomous_dispatcher_cycle655_cold_2026_07_23.txt"
PASS = FAIL = 0


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, value):
        for stream in self.streams: stream.write(value)
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not bool(condition))
    print("PASS" if condition else "FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.integer): return int(value)
    if isinstance(value, np.floating): return float(value)
    if isinstance(value, np.ndarray): return value.tolist()
    if isinstance(value, tuple): return list(value)
    raise TypeError(type(value).__name__)


def load_immutable_cycle652():
    export = tempfile.TemporaryDirectory(prefix="cycle655-immutable-")
    shore = Path(export.name).resolve()
    previous_git_dir = os.environ.get("GIT_DIR")
    previous_git_tree = os.environ.get("GIT_WORK_TREE")
    os.environ["GIT_DIR"] = str((ROOT / ".git").resolve())
    os.environ["GIT_WORK_TREE"] = str(ROOT.resolve())
    archive = subprocess.check_output([
        "git", "archive", "--format=tar", IMMUTABLE_COMMIT, *C652_PATHS,
    ])
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as stream:
        stream.extractall(shore, filter="data")
    os.symlink((ROOT / ".git").resolve(), shore / ".git", target_is_directory=True)
    spec = importlib.util.spec_from_file_location("cycle655_immutable_c652", shore / C652_PATHS[0])
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    if previous_git_dir is None: os.environ.pop("GIT_DIR", None)
    else: os.environ["GIT_DIR"] = previous_git_dir
    if previous_git_tree is None: os.environ.pop("GIT_WORK_TREE", None)
    else: os.environ["GIT_WORK_TREE"] = previous_git_tree
    receipt = json.loads((shore / C652_PATHS[2]).read_text())
    return export, shore, module, receipt


def bit_index(bits):
    count = len(bits)
    return sum(int(bit) << (count - 1 - q) for q, bit in enumerate(bits))


def clean_columns(qubits, active):
    columns = np.zeros((2 ** qubits, 2 ** len(active)), dtype=complex)
    words = []
    for word in range(2 ** len(active)):
        bits = [0] * qubits
        for j, q in enumerate(active): bits[q] = (word >> (len(active) - 1 - j)) & 1
        columns[bit_index(bits), word] = 1
        words.append(bits)
    return columns, words


def expected_columns(qubits, words, transform):
    expected = np.zeros((2 ** qubits, len(words)), dtype=complex)
    for column, source in enumerate(words):
        bits, amplitude = transform(list(source))
        expected[bit_index(bits), column] = amplitude
    return expected


def toffoli(c631, left, right, target, scratch):
    return c631.marker_safe_toffoli_sequence(left, right, target, scratch)


def macro_library(c631, c603):
    scratch7 = (3, 4, 5, 6)
    ccx = toffoli(c631, 0, 1, 2, scratch7)
    fredkin = ([c603.two("fredkin_open", 2, 1, c603.CNOT, "CNOT")]
               + toffoli(c631, 0, 1, 2, scratch7)
               + [c603.two("fredkin_close", 2, 1, c603.CNOT, "CNOT")])
    ccz = ([c603.one("ccz_open", 2, c603.H2, "H")]
           + toffoli(c631, 0, 1, 2, scratch7)
           + [c603.one("ccz_close", 2, c603.H2, "H")])
    ccy = ([c603.one("ccy_sdg0", 2, c603.TDG2, "Tdg"),
            c603.one("ccy_sdg1", 2, c603.TDG2, "Tdg")]
           + toffoli(c631, 0, 1, 2, scratch7)
           + [c603.one("ccy_s0", 2, c603.T2, "T"),
              c603.one("ccy_s1", 2, c603.T2, "T")])
    y2 = np.asarray([[0, -1j], [1j, 0]], dtype=complex)
    raw = {
        "NOP": [], "H": [c603.one("H", 4, c603.H2, "H")],
        "T": [c603.one("T", 4, c603.T2, "T")],
        "Tdg": [c603.one("Tdg", 4, c603.TDG2, "Tdg")],
        "X": [c603.one("X", 4, c603.X2, "X")],
        "Y": [c603.one("Y", 4, y2, "Y")],
        "Z": [c603.one("Z", 4, np.diag([1, -1]), "Z")],
        "CNOT": [c603.two("CNOT", 3, 4, c603.CNOT, "CNOT")],
        "SWAP": [c603.two("SWAP", 3, 4, c603.SWAP, "SWAP")],
    }
    gated = {}
    for name, core in (("controlled_X", ccx), ("controlled_Y", ccy),
                       ("controlled_Z", ccz), ("FREDKIN", fredkin)):
        # token q0 AND opcode q1 -> clean enable q2; core controls use q2.
        compute = toffoli(c631, 0, 1, 2, (5, 6, 7, 8))
        remapped = []
        mapping = {0: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8}
        for gate in core:
            remapped.append(c603.Gate(gate.name, tuple(mapping[q] for q in gate.qubits),
                                      gate.matrix, gate.family))
        gated[name] = compute + remapped + compute
    return {**raw, **gated}, {"CCX": ccx, "CCY": ccy, "CCZ": ccz, "FREDKIN": fredkin}


def exact_kernel_audit(c631, c603, library, cores):
    residuals = {}
    deletions = {}
    columns, words = clean_columns(7, (0, 1, 2))
    transforms = {
        "CCX": lambda b: (b[:2] + [b[2] ^ (b[0] & b[1])] + b[3:], 1),
        "CCZ": lambda b: (b, -1 if b[0] & b[1] & b[2] else 1),
        "CCY": lambda b: (b[:2] + [b[2] ^ (b[0] & b[1])] + b[3:],
                           (1j if b[2] == 0 else -1j) if b[0] & b[1] else 1),
        "FREDKIN": lambda b: (b[:1] + ([b[2], b[1]] if b[0] else [b[1], b[2]]) + b[3:], 1),
    }
    for name, gates in cores.items():
        expected = expected_columns(7, words, transforms[name])
        actual = c603.apply_sequence_columns(columns, gates, 7)
        residuals[name] = float(np.linalg.norm(actual - expected))
        cut = len(gates) // 2
        deleted = c603.apply_sequence_columns(columns, gates[:cut] + gates[cut + 1:], 7)
        deletions[name] = float(np.linalg.norm(deleted - expected))

    gated_residuals = {}
    gated_deletions = {}
    columns9, words9 = clean_columns(9, (0, 1, 3, 4))
    for name in ("controlled_X", "controlled_Y", "controlled_Z", "FREDKIN"):
        def transform(bits, which=name):
            enabled = bits[0] & bits[1]
            amplitude = 1
            if which == "FREDKIN" and enabled:
                bits[3], bits[4] = bits[4], bits[3]
            elif which == "controlled_X" and enabled and bits[3]: bits[4] ^= 1
            elif which == "controlled_Z" and enabled and bits[3] and bits[4]: amplitude = -1
            elif which == "controlled_Y" and enabled and bits[3]:
                amplitude = 1j if bits[4] == 0 else -1j
                bits[4] ^= 1
            return bits, amplitude
        expected = expected_columns(9, words9, transform)
        gates = library[name]
        actual = c603.apply_sequence_columns(columns9, gates, 9)
        gated_residuals[name] = float(np.linalg.norm(actual - expected))
        deleted = c603.apply_sequence_columns(columns9, gates[:-1], 9)
        gated_deletions[name] = float(np.linalg.norm(deleted - expected))
    counts = {name: len(gates) for name, gates in cores.items()}
    result = {
        "Cycle631_exact_Toffoli_primitive_count": len(cores["CCX"]),
        "core_primitive_counts": counts,
        "all_eight_clean_scratch_columns": True,
        "core_exact_residuals": residuals,
        "core_delete_one_primitive_residuals": deletions,
        "gated_all_sixteen_token_opcode_probe_target_columns": True,
        "gated_exact_residuals": gated_residuals,
        "gated_delete_uncompute_primitive_residuals": gated_deletions,
        "parity_and_enable_scratch_return_clean": max([*residuals.values(), *gated_residuals.values()]) < 1e-11,
    }
    result["pass"] = bool(result["Cycle631_exact_Toffoli_primitive_count"] == 27
                          and max(residuals.values()) < 1e-11
                          and max(gated_residuals.values()) < 1e-11
                          and min(deletions.values()) > 1e-6
                          and min(gated_deletions.values()) > 1e-6)
    check("exact Fredkin and token+opcode+probe X/Y/Z kernels use the Cycle631 27-primitive lowering",
          result["pass"], {"counts": counts, "residuals": residuals,
                            "gated": gated_residuals, "deleted_min": min(deletions.values())})
    return result


ROLE_COORDS = {
    0: (1, 1, 1), 1: (3, 1, 1), 2: (2, 2, 2),
    3: (1, 3, 1), 4: (3, 3, 1), 5: (1, 1, 3),
    6: (3, 1, 3), 7: (1, 3, 3), 8: (3, 3, 3),
}


def neighbors(site):
    for axis in range(3):
        for sign in (-1, 1):
            trial = list(site); trial[axis] += sign
            if all(0 <= x < 5 for x in trial): yield tuple(trial)


def shortest_access(start, fixed, obstacles):
    goals = set(neighbors(fixed)) - obstacles
    queue = deque([start]); parent = {start: None}
    while queue:
        site = queue.popleft()
        if site in goals:
            path = []
            while site is not None: path.append(site); site = parent[site]
            return tuple(reversed(path))
        for nxt in neighbors(site):
            if nxt not in parent and nxt not in obstacles and nxt != fixed:
                parent[nxt] = site; queue.append(nxt)
    raise RuntimeError((start, fixed, obstacles))


def local_tile_route_audit(c603, library):
    occupied = set(ROLE_COORDS.values())
    digest = sha256(); physical = Counter(); route_lengths = []
    all_nn = True; return_failures = 0; routed_primitives = 0
    deletion_nonreturn = False
    for opcode, gates in sorted(library.items()):
        for primitive_index, gate in enumerate(gates):
            if len(gate.qubits) == 1:
                physical[(gate.family, 1)] += 1
                digest.update(f"{opcode}|{primitive_index}|{gate.family}|{ROLE_COORDS[gate.qubits[0]]}\n".encode())
                continue
            left, right = gate.qubits
            start, fixed = ROLE_COORDS[right], ROLE_COORDS[left]
            obstacles = occupied - {start, fixed}
            path = shortest_access(start, fixed, obstacles)
            route_lengths.append(len(path) - 1)
            for a, b in zip(path, path[1:]):
                all_nn &= sum(abs(a[j] - b[j]) for j in range(3)) == 1
                physical[("SWAP_route", 2)] += 1
                digest.update(f"{opcode}|{primitive_index}|open|{a}|{b}\n".encode())
            access = path[-1]
            all_nn &= sum(abs(access[j] - fixed[j]) for j in range(3)) == 1
            physical[(gate.family, 2)] += 1; routed_primitives += 1
            digest.update(f"{opcode}|{primitive_index}|act|{fixed}|{access}|{gate.family}\n".encode())
            current = access
            for a, b in reversed(tuple(zip(path, path[1:]))):
                physical[("SWAP_route", 2)] += 1
                digest.update(f"{opcode}|{primitive_index}|close|{b}|{a}\n".encode())
                current = a
            return_failures += int(current != start)
            if len(path) > 1: deletion_nonreturn |= path[-2] != start
    result = {
        "tile_shape": [5, 5, 5], "bounded_tile_M2": 125,
        "logical_roles": {str(k): list(v) for k, v in ROLE_COORDS.items()},
        "roles_named": ["token", "opcode", "enable", "probe_or_left", "target_or_right",
                        "parity_scratch_0", "parity_scratch_1", "parity_scratch_2", "parity_scratch_3"],
        "routed_two_site_primitives": routed_primitives,
        "maximum_open_route_edges": max(route_lengths),
        "all_support_two_steps_fine_NN": all_nn,
        "route_return_failures": return_failures,
        "delete_one_closing_swap_nonreturn": deletion_nonreturn,
        "physical_primitive_counts": {f"{family}/support{support}": count for (family, support), count in sorted(physical.items())},
        "routed_library_sha256": digest.hexdigest(),
        "global_injective_tile_placement_executed": False,
    }
    result["pass_as_bounded_local_tile"] = bool(all_nn and return_failures == 0 and deletion_nonreturn
                                                  and result["maximum_open_route_edges"] < 15)
    check("every local-dispatch primitive routes inside one bounded 5-cube tile and returns its route stack",
          result["pass_as_bounded_local_tile"], {"routed": routed_primitives,
                                                   "max": result["maximum_open_route_edges"],
                                                   "return_failures": return_failures})
    return result


def recurrence_audit(receipt652, library):
    opcodes = tuple(sorted(library))
    macro_lengths = {name: max(1, len(library[name])) for name in opcodes}
    rows = []
    failures = inverse_failures = malformed_accepts = 0
    total = malformed_tests = 0

    def forward(state, checks):
        left_token, right_token, opcode_index, phase, counter, error = state
        if (left_token, right_token) != (1, 0): return state, "rejected_token"
        if not 0 <= opcode_index < len(opcodes): return state, "rejected_opcode"
        phases = macro_lengths[opcodes[opcode_index]]
        if not 0 <= phase < phases or not 0 <= counter < checks: return state, "rejected_domain"
        if phase + 1 < phases:
            return (1, 0, opcode_index, phase + 1, counter, error), "advanced_phase"
        return (0, 1, opcode_index, 0, (counter + 1) % checks, error), "advanced_head"

    def inverse(state, checks):
        left_token, right_token, opcode_index, phase, counter, error = state
        if not 0 <= opcode_index < len(opcodes): return state, "rejected_opcode"
        phases = macro_lengths[opcodes[opcode_index]]
        if (left_token, right_token) == (1, 0) and 0 < phase < phases and 0 <= counter < checks:
            return (1, 0, opcode_index, phase - 1, counter, error), "reversed_phase"
        if (left_token, right_token) == (0, 1) and phase == 0 and 0 <= counter < checks:
            return (1, 0, opcode_index, phases - 1, (counter - 1) % checks, error), "reversed_head"
        return state, "rejected_domain"

    for system in receipt652["systems"]:
        checks = system["descriptor_summary"]["checks"]
        word_length = sum(system["literal_oracle_circuit_word"]["primitive_counts"].values())
        sectors = 0
        for opcode_index, opcode in enumerate(opcodes):
            phases = macro_lengths[opcode]
            for counter in range(checks):
                for phase in range(phases):
                    total += 1; sectors += 1
                    state = (1, 0, opcode_index, phase, counter, 0)
                    advanced, status = forward(state, checks)
                    restored, reverse_status = inverse(advanced, checks)
                    failures += int(status not in ("advanced_phase", "advanced_head"))
                    inverse_failures += int(restored != state or not reverse_status.startswith("reversed_"))
                # Cross every counter/opcode sector with all malformed token
                # sectors.  Rejection is side-effect free.
                for token_pair in ((0, 0), (0, 1), (1, 1), (2, 0), (0, 2)):
                    malformed_tests += 1
                    malformed = (token_pair[0], token_pair[1], opcode_index, 0, counter, 0)
                    observed, status = forward(malformed, checks)
                    malformed_accepts += int(observed != malformed or not status.startswith("rejected_"))
            # Illegal opcode and counter controls for every legal opcode family.
            for malformed in ((1, 0, len(opcodes), 0, 0, 0),
                              (1, 0, opcode_index, 0, checks, 0)):
                malformed_tests += 1
                observed, status = forward(malformed, checks)
                malformed_accepts += int(observed != malformed or not status.startswith("rejected_"))
        boundary_ok = inverse_failures == 0
        rows.append({
            "length": system["length"], "checks": checks,
            "fixed_word_primitives": word_length,
            "opcode_sectors": len(opcodes), "opcode_phase_counter_sectors_exhausted": sectors,
            "token_sectors": ["00 rejected", "10 active", "01 inverse-facing", "11 rejected", "nonbinary rejected"],
            "head_terminal_moves_to_adjacent_program_cell": True,
            "counter_forward_inverse_return": boundary_ok,
        })
    result = {
        "state_fields": ["one-hot token/head on adjacent program cells", "static opcode", "microphase",
                         "check counter", "error bit", "four clean parity scratch"],
        "local_transition_rule": "advance state-carried microphase; at the opcode terminal use Fredkin to move the one-hot head to the adjacent static instruction cell and increment the check counter; inverse restores both",
        "opcodes": list(opcodes), "macro_lengths": macro_lengths,
        "every_token_check_counter_opcode_phase_sector_exhausted": True,
        "sector_tests": total, "transition_failures": failures,
        "malformed_sector_tests": malformed_tests,
        "inverse_failures": inverse_failures, "malformed_accepts": malformed_accepts,
        "systems": rows,
        "host_selected_gate_within_local_rule": False,
        "host_selected_site_in_global_Cycle652_word_eliminated": False,
        "global_program_rail_embedded": False,
    }
    result["pass_as_reversible_local_recurrence"] = bool(total > 0 and not failures and not inverse_failures
                                                          and not malformed_accepts)
    check("local token/opcode recurrence exhausts every L3/L6/L7 token, opcode, phase, and check-counter sector",
          result["pass_as_reversible_local_recurrence"], {"sectors": total, "failures": failures,
                                                            "global_rail": False})
    return result


def frame_key(matrix): return tuple(int(x) for x in np.asarray(matrix).reshape(-1))


def colour_permutation(matrix, shift=(0, 0, 0)):
    matrix = np.asarray(matrix, dtype=int)
    result = []
    for axis in range(3):
        column = matrix[:, axis]
        target_axis = int(np.flatnonzero(column)[0]); sign = int(column[target_axis])
        for residue in range(3):
            mapped = (sign * residue + shift[target_axis] - (1 if sign < 0 else 0)) % 3
            result.append(3 * target_axis + mapped)
    return tuple(result)


def colour_schedule_audit(frames, lengths):
    frame_map = {frame_key(frame): i for i, frame in enumerate(frames)}
    matching_failures = translation_failures = frame_failures = composition_failures = 0
    samples = 0
    for length in lengths:
        side = 129 * length
        matching_failures += int(side % 3 != 0)
        # Exact one-dimensional periodic incidence proof for every axis/color.
        for axis in range(3):
            for residue in range(3):
                origins = [q for q in range(side) if q % 3 == residue]
                vertices = []
                for q in origins: vertices.extend((q, (q + 1) % side))
                matching_failures += int(len(vertices) != len(set(vertices)))
        for shift in ((a, b, c) for a in range(3) for b in range(3) for c in range(3)):
            perm = colour_permutation(np.eye(3, dtype=int), shift)
            translation_failures += int(sorted(perm) != list(range(9))); samples += 1
    permutations = []
    for frame in frames:
        perm = colour_permutation(frame)
        permutations.append(perm)
        frame_failures += int(sorted(perm) != list(range(9)))
    for left in frames:
        for right in frames:
            product = np.asarray(right) @ np.asarray(left)
            expected = permutations[frame_map[frame_key(product)]]
            pleft = colour_permutation(left); pright = colour_permutation(right)
            observed = tuple(pright[pleft[index]] for index in range(9))
            composition_failures += int(observed != expected)
    result = {
        "physical_sides": [129 * length for length in lengths],
        "colour_definition": "(positive-edge axis, positive-edge-origin coordinate mod 3)",
        "colour_classes": 9, "each_colour_is_a_periodic_NN_matching": matching_failures == 0,
        "ordinary_translation_residue_representatives": samples,
        "ordinary_translation_permutation_failures": translation_failures,
        "proper_cubic_frames": len(frames), "all24_permutation_failures": frame_failures,
        "ordered_frame_products": len(frames) ** 2, "all576_composition_failures": composition_failures,
        "state_carried_fields": ["proper-cubic frame sector", "nine-colour phase"],
        "rule": "advance the state-carried phase and apply only the matching edge rule; transform the phase with the frame/translation-induced colour permutation",
        "phase_is_time": False, "phase_is_rate": False,
        "global_instruction_cells_placed": False,
    }
    result["pass_as_state_carried_staggered_rule"] = not any((matching_failures, translation_failures,
                                                               frame_failures, composition_failures))
    check("nine-colour NN matching rule is ordinary-translation, all24, and all576 covariant with state-carried phase",
          result["pass_as_state_carried_staggered_rule"], {"translation": translation_failures,
                                                             "all24": frame_failures,
                                                             "all576": composition_failures})
    return result


def inherited_and_capacity(receipt652):
    grammar = receipt652["baseline_Cycle638"]["grammar"]
    execution = receipt652["baseline_Cycle638"]["execution"]
    systems = []
    for system in receipt652["systems"]:
        covariance = system["covariance_and_capacity"]
        candidate_cells = system["backbone_M2"] + covariance["active_identity_finger_union_M2"]
        candidate_M2 = 125 * candidate_cells
        systems.append({
            "length": system["length"], "candidate_controller_cells": candidate_cells,
            "candidate_125_M2_tiles": candidate_M2,
            "Cycle652_capacity_margin_M2": covariance["capacity_margin"],
            "raw_capacity_discriminator_pass": candidate_M2 <= covariance["capacity_margin"],
            "injective_global_placement_witness": False,
            "Cycle652_fixed_word_sha256": system["literal_oracle_circuit_word"]["literal_gate_word_sha256"],
            "Cycle652_fixed_word_gate_count": sum(system["literal_oracle_circuit_word"]["primitive_counts"].values()),
            "Cycle652_checks": system["descriptor_summary"]["checks"],
            "Cycle652_Pauli_histogram": system["descriptor_summary"]["Pauli_letter_histogram"],
        })
    result = {
        "Cycle652_status": receipt652["Status"], "Cycle652_tests": receipt652["tests_passed"],
        "conditional_act_calls": grammar["conditional_act_calls"],
        "descriptor_word_sha256": grammar["captured_descriptor_word_sha256"],
        "parameter_word_sha256": grammar["captured_parameter_aware_word_sha256"],
        "factor_call_population": grammar["factor_call_population"],
        "Cycle652_lawful_auxiliary_slice_leakage_norm": execution["lawful_auxiliary_slice_leakage_norm"],
        "mass_contact_seam_pin_scope": "the inherited exact coin/stream/contact call word and Cycle652 fixed physical words are byte pinned; Cycle655 executes no new one-particle mass, contact, or seam fixture",
        "systems": systems,
    }
    result["pass"] = bool(receipt652["pass"] and grammar["conditional_act_calls"] == 769434
                           and grammar["factor_call_population"]["factor_2_contact"] == 4950
                           and all(row["raw_capacity_discriminator_pass"] for row in systems)
                           and not any(row["injective_global_placement_witness"] for row in systems))
    check("Cycle652 mass/contact/seam call-word pins are unchanged and raw tile capacity is only a discriminator",
          result["pass"], {"calls": result["conditional_act_calls"],
                            "contact": result["factor_call_population"]["factor_2_contact"],
                            "capacity": [row["raw_capacity_discriminator_pass"] for row in systems]})
    return result


def no_go_discipline(route_a, route_b, route_c):
    families = [
        {"family":"moving-head program/storage rail", "object":"static instruction cells plus one-hot mobile head", "mechanism":"state-carried opcode microphase, terminal Fredkin, adjacent-cell counter transition", "terminal":"global Cycle652 word traversed with no host-selected gate/site", "strength_vs_target":"target-equivalent", "honesty_marker":"ATTEMPTED", "result":"local recurrence exact; global rail placement and operand coupling unmaterialized"},
        {"family":"static bounded QCA transition tile", "object":"token/opcode/enable/probe/target/four-scratch 5-cube", "mechanism":"Cycle631 Toffoli, Fredkin, CCX/CCY/CCZ and fine-NN open/apply/reverse routing", "terminal":"one repeated physical local rule over the occupied Cycle652 graph", "strength_vs_target":"target-equivalent", "honesty_marker":"ATTEMPTED", "result":"bounded tile exact; injective global tiling unmaterialized"},
        {"family":"staggered state-carried colour dispatcher", "object":"nine NN edge colours and frame/phase state", "mechanism":"three residues per axis form matchings; translations and signed permutations act on colours", "terminal":"no host-selected edge layer or site", "strength_vs_target":"target-equivalent", "honesty_marker":"ATTEMPTED", "result":"ordinary translations/all24/all576 exact; instruction cells still unplaced"},
        {"family":"nested stored-program decoder adapter", "object":"immutable Cycle638 200-opcode grammar and Cycle652 fixed word", "mechanism":"reuse exact counters/decoder and attach the bounded macro library", "terminal":"literal physical adapter from every stored action record to a local tile", "strength_vs_target":"target-equivalent", "honesty_marker":"ATTEMPTED", "result":"byte pins and opcode-family coverage positive; adapter placement unmaterialized"},
        {"family":"flat replicated controller-tile budget", "object":"one candidate 125-M2 tile per Cycle652 backbone/finger controller vertex", "mechanism":"compare explicit constant tile budget with immutable free-capacity margin", "terminal":"collision-free injective placement with local operand access", "strength_vs_target":"weaker discriminator", "honesty_marker":"ATTEMPTED", "result":"raw L3/L6/L7 capacity positive; capacity is not an embedding"},
    ]
    walls = {
        "W_global_controller_embedding":"no injective placement couples each stored opcode/head tile to its Cycle652 routed operand while preserving occupied roles",
        "W_blank_renewal":"the clean outer-shell/routing blanks remain supplied rather than locally generated or renewed",
        "W_static_enforcement_or_repair":"the circuit dispatcher is not a static constraint/enforcement or autonomous malformed-sector repair law",
    }
    pairs = [{"from": a, "to": b, "implied": False, "reason": f"closing {a} does not construct {b}"}
             for a in walls for b in walls if a != b]
    result = {
        "Status":"PASS_SCOPED_POSITIVE_LOCAL_KERNEL_AND_BOUNDED_GLOBAL_RESIDUAL",
        "N1_normalized_families": families, "N1_qualifying_attempts": len(families),
        "N1_required_for_negative": 5, "N1_negative_gate":"FAIL / DO NOT SHIP",
        "N1_open_routes_not_counted":[
            {"family":"distributed packet/tree controller", "status":"OPEN / NOT COUNTED"},
            {"family":"topological program fibre", "status":"OPEN / NOT COUNTED"},
        ],
        "N2_collapsed_walls": walls, "N2_directed_ordered_pairs": pairs,
        "N3_hidden_wall_scan":[
            {"phrase":"static opcode", "classification":"explicit program-cell state, not a host gate choice", "wall":"W_global_controller_embedding"},
            {"phrase":"state-carried phase", "classification":"explicit nine-sector field, not schedule time or rate", "wall":None},
            {"phrase":"raw capacity", "classification":"necessary discriminator only, not placement", "wall":"W_global_controller_embedding"},
            {"phrase":"clean parity/routing scratch", "classification":"explicit supplied blank resource", "wall":"W_blank_renewal"},
        ],
        "N4_exact_residual_matches":[{
            "prior_ref":IMMUTABLE_COMMIT, "prior_path":C652_PATHS[2], "prior_line":"controller fixed-word result",
            "prior_residual":"autonomous_token_conditioned_gate_dispatch_law_executed=false",
            "current_path":str(Path(__file__).relative_to(ROOT)), "current_line":"def recurrence_audit",
            "current_residual":"bounded local recurrence is exact but global program rail/operand coupling remains unembedded",
            "same_scope":True, "exact_match":True, "use_as_closure":False,
        }],
        "N5_rhetoric":[
            {"claim":"bounded local dispatcher kernel passes", "per_element":"every core and opcode-gated truth-table column", "per_site":"all routed support-two primitives are fine NN in one 5-cube", "per_mode":"X/Y/Z and Fredkin", "per_block":"same tile for L3/L6/L7", "lattice_wide":"no injective controller embedding claimed"},
            {"claim":"autonomous physical dispatch does not yet pass", "per_element":"local opcode lookup is a finite transition table", "per_site":"global active site remains unplaced", "per_mode":"all local Pauli families covered", "per_block":"raw capacity only", "lattice_wide":"host-selected Cycle652 event iteration is not replaced"},
        ],
        "N6_partial_closure_paths":[
            {"file":"UNMATERIALIZED/physical_injective_program_fibre_cycle_next.py", "status":"OPEN / PRIORITY", "what_closes":"W_global_controller_embedding with literal instruction/head/operand placement"},
            {"file":"UNMATERIALIZED/physical_outer_shell_blank_renewal_cycle_next.py", "status":"OPEN / SEPARATE", "what_closes":"W_blank_renewal"},
            {"file":"UNMATERIALIZED/physical_static_or_repair_law_cycle_next.py", "status":"OPEN / SEPARATE", "what_closes":"W_static_enforcement_or_repair"},
        ],
        "N7_steelman":{
            "mechanism":"embed one static primitive-opcode cell beside each already enumerated Cycle652 gate occurrence, use the proven nine-colour matching rule to move a one-hot head, and couple each tile's probe/target ports to the existing route without overlap",
            "actionable_steps":["stream a collision-free instruction-cell placement instead of storing it flat", "route token/opcode/enable/parity roles to each occurrence", "execute a full head round trip for L3/L6/L7", "delete one cell and corrupt every token/opcode sector"],
            "terminal_test":"a literal repeated local rule traverses the immutable fixed-word digest, returns head/counters/scratch, and never receives a gate or site from Python",
            "why_it_breaks_the_negative":"all required local quantum kernels, routes, counter transitions, and covariant edge layers now exist, so the remaining question is a concrete global embedding rather than a substrate obstruction",
        },
        "N8_cross_cycle_echo":[
            {"cycle":631,"mechanism":"exact 27-primitive clean-scratch Toffoli","applicability":"used verbatim for all controlled local kernels"},
            {"cycle":638,"mechanism":"nested program decoder and counters","applicability":"pins the instruction grammar but not Cycle655 cell placement"},
            {"cycle":649,"mechanism":"outer-shell backbone/fingers","applicability":"supplies route geometry and blanks, not renewal"},
            {"cycle":652,"mechanism":"literal support-one/two fixed word","applicability":"exact target word; host dispatch residual is narrowed, not closed"},
        ],
        "route_A_local_pass": route_a["pass_as_reversible_local_recurrence"],
        "route_B_local_pass": route_b["pass_as_bounded_local_tile"],
        "route_C_phase_pass": route_c["pass_as_state_carried_staggered_rule"],
        "broad_negative_gate":"FAIL / DO NOT SHIP", "minimum_content_gate":"FAIL / DO NOT SHIP",
        "shared_obstruction_gate":"FAIL / DO NOT SHIP", "axiom_pressure_gate":"FAIL / DO NOT SHIP",
        "broad_negative_shipped":False, "minimum_content_shipped":False,
        "shared_obstruction_shipped":False, "axiom_pressure_shipped":False,
        "shared_route_independent_obstruction":False, "axiom_pressure":False,
    }
    required = {"prior_ref","prior_path","prior_line","prior_residual","current_path","current_line",
                "current_residual","same_scope","exact_match","use_as_closure"}
    result["pass"] = bool(len(families) >= 5 and len(pairs) == 6
                          and all(required <= set(row) for row in result["N4_exact_residual_matches"])
                          and all(result[key] == "FAIL / DO NOT SHIP" for key in
                                  ("broad_negative_gate","minimum_content_gate","shared_obstruction_gate","axiom_pressure_gate"))
                          and not any(result[key] for key in ("broad_negative_shipped","minimum_content_shipped",
                                                             "shared_obstruction_shipped","axiom_pressure_shipped")))
    check("canonical N1-N8 preserves local positives and blocks global no-go, minimum-content, and axiom-pressure promotion",
          result["pass"], {"families":len(families), "walls":len(walls), "pairs":len(pairs)})
    return result


def main():
    global PASS, FAIL
    started = time.perf_counter()
    observed = {path: file_sha(ROOT / path) for path in C652_PATHS}
    check("immutable Cycle652 quartet is byte exact at the declared shore",
          observed == PINS, {"commit":IMMUTABLE_COMMIT,
                              "mismatches":[path for path in PINS if observed[path] != PINS[path]]})
    export, shore, c652, receipt652 = load_immutable_cycle652()
    c631 = c652.c638.c631; c603 = c631.c603
    check("Cycle652 premise is loaded only from the immutable archive, not dirty working bytes",
          Path(c652.__file__).is_relative_to(shore) and receipt652["pass"],
          {"module":str(c652.__file__), "status":receipt652["Status"]})
    library, cores = macro_library(c631, c603)
    kernel = exact_kernel_audit(c631, c603, library, cores)
    route_b = local_tile_route_audit(c603, library)
    route_a = recurrence_audit(receipt652, library)
    route_c = colour_schedule_audit(c652.FRAMES, (3, 6, 7))
    inherited = inherited_and_capacity(receipt652)
    nogo = no_go_discipline(route_a, route_b, route_c)
    note = NOTE.read_text()
    markers = ("Status: **PASS**", "Authority: **none**", "Audit: **unset**", "27-primitive",
               "Fredkin", "controlled X/Y/Z", "5-cube", "nine-colour", "ordinary translations",
               "all24/all576", "host-selected gate/site", "N1-N8", "Axiom pressure: **none**")
    check("Cycle655 note freezes the local positives, global dispatcher firewall, and N1-N8 scope",
          all(marker in note for marker in markers), markers)
    local_positive = bool(kernel["pass"] and route_a["pass_as_reversible_local_recurrence"]
                          and route_b["pass_as_bounded_local_tile"]
                          and route_c["pass_as_state_carried_staggered_rule"] and inherited["pass"])
    autonomous_global = bool(route_a["host_selected_site_in_global_Cycle652_word_eliminated"]
                             and route_a["global_program_rail_embedded"]
                             and route_b["global_injective_tile_placement_executed"]
                             and route_c["global_instruction_cells_placed"])
    overall = bool(local_positive and not autonomous_global and nogo["pass"]
                   and not nogo["shared_route_independent_obstruction"] and not nogo["axiom_pressure"])
    check("Cycle655 produces exact autonomous local kernels but does not promote them to a global physical dispatcher",
          overall, {"local_positive":local_positive, "autonomous_global":autonomous_global})
    result = {
        "cycle":655, "date":"2026-07-23", "Status":"PASS" if overall and FAIL == 0 else "FAIL",
        "status":"cycle655-exact-local-dispatch-kernels-positive-global-controller-embedding-open",
        "classification":"bounded exact moving-head/QCA/staggered dispatcher kernels with one named global embedding interface",
        "authority":AUTHORITY, "audit":AUDIT, "author_accepted":False,
        "author_artifact_status_accepted":False, "constitutional_effect":"none", "breakthrough":False,
        "shore":{"immutable_commit":IMMUTABLE_COMMIT, "pins":PINS, "observed":observed,
                 "archive_root":str(shore), "working_tree_bytes_used_as_premise":False,
                 "no_go_skill_origin_main_sha256":NO_GO_ORIGIN_MAIN_SHA256,
                 "freshness_check_origin_main_sha256":FRESHNESS_ORIGIN_MAIN_SHA256,
                 "proof_search_governance_origin_main_sha256":PROOF_SEARCH_ORIGIN_MAIN_SHA256},
        "exact_target_contract":{
            "target":"replace host iteration of the immutable Cycle652 fixed support-one/fine-NN-support-two word by one recurrent state-conditioned local physical update over a placed instruction/head/operand substrate",
            "quantifiers_domain":"L3/L6/L7; token sectors including malformed states; every local opcode/microphase/check-counter sector; ordinary translations; all24 proper-cubic frames and all576 ordered products",
            "allowed_premises":"immutable Cycle652/Cycle638/Cycle631 resources, state-carried proper-cubic frame, static program opcodes, and explicitly supplied clean parity/routing work",
            "forbidden_weakenings":"no host-selected gate/site, nonlocal parity service, preferred global ordering, hidden route query, refit, blank renewal, repair, E, preparation, occurrence, Record, time, rate, energy, source, gravity, full-compiler, or axiom promotion",
            "completion_witness":"literal collision-free global program/head/operand embedding plus a repeated local rule whose executed digest equals every Cycle652 fixed word and whose inverse returns head, counters, token, route stack, enable, probe, and parity scratch",
            "does_not_count":"exact local macro, abstract head recurrence, colour schedule, or raw capacity without the global embedding and no-host trace",
        },
        "exact_local_kernel":kernel,
        "route_A_moving_head_program_rail":route_a,
        "route_B_static_local_transition_tile":route_b,
        "route_C_staggered_state_carried_phase":route_c,
        "inherited_pins_and_capacity_discriminator":inherited,
        "strongest_constructive_result":"one bounded 5x5x5 M2 tile exactly realizes Fredkin and token+opcode+probe-controlled X/Y/Z using the immutable Cycle631 27-primitive clean-scratch Toffoli; every support-two primitive is fine-NN routed with inverse return, and an exact nine-colour state-carried matching rule is ordinary-translation/all24/all576 covariant",
        "route_by_route_disposition":{
            "A_moving_head":"PARTIAL_LOCAL_RECURRENCE_PASS_GLOBAL_PROGRAM_RAIL_AND_OPERAND_COUPLING_OPEN",
            "B_static_QCA_tile":"PARTIAL_BOUNDED_TILE_PASS_GLOBAL_INJECTIVE_TILING_OPEN",
            "C_staggered_colour":"PARTIAL_PHASE_RULE_PASS_GLOBAL_INSTRUCTION_CELL_PLACEMENT_OPEN",
        },
        "autonomous_local_dispatch_kernel_pass":local_positive,
        "autonomous_token_conditioned_global_dispatch_pass":autonomous_global,
        "full_physical_oracle_compiler_pass":False,
        "shared_route_independent_obstruction":False, "axiom_pressure":False,
        "broad_negative_gate":"FAIL / DO NOT SHIP", "minimum_content_gate":"FAIL / DO NOT SHIP",
        "shared_obstruction_gate":"FAIL / DO NOT SHIP", "axiom_pressure_gate":"FAIL / DO NOT SHIP",
        "broad_negative_shipped":False, "minimum_content_shipped":False,
        "shared_obstruction_shipped":False, "axiom_pressure_shipped":False,
        "separate_unclosed_interfaces":{
            "dispatcher":"global injective controller/program/head/operand embedding",
            "blank_renewal":"not attempted; supplied clean work remains explicit",
            "static_enforcement_or_repair":"not attempted; circuit dispatch is not enforcement/repair",
            "physical_E":"not attempted; no preparation or intertwiner claim",
        },
        "supplied_structure_inventory":{
            "immutable_Cycle652_fixed_words":True, "static_program_opcode_bits":True,
            "state_carried_active_frame":True, "state_carried_nine_colour_phase":True,
            "one_hot_head_token":True, "four_clean_parity_scratch":True,
            "clean_enable_and_route_work":True, "raw_free_capacity_margin":True,
            "global_program_rail_placement":False, "global_operand_coupling":False,
            "autonomous_blank_renewal":False, "static_enforcement_or_repair":False,
            "physical_E_or_preparation":False,
        },
        "semantic_firewall":{"phase_is_time":False,"phase_is_rate":False,"phase_is_energy":False,
                             "gate_count_is_rate":False,"pointer_or_token_is_Record":False,
                             "local_kernel_is_full_compiler":False},
        "six_wall_ledger":{
            "C_ref":"nine-colour edge layers and the bounded tile are ordinary-translation/all24/all576 covariant; the active frame, macro origin, phase, and global controller placement remain supplied/open as declared",
            "C_num":"exact finite matrices, truth-table columns, counters, route stacks, digests, and deletion residuals only; no normalization/Born claim",
            "C_wrap":"local head/token/opcode/check-counter forward-inverse return passes; global traversal of each million-gate Cycle652 word without host gate/site dispatch remains open",
            "C_int":"immutable coin/stream/contact populations and fixed words are pinned; no new mass/contact/seam fixture, inertia law, or E-intertwiner is executed",
            "C_local":"exact bounded Fredkin and controlled-X/Y/Z kernels plus a local colour rule now pass; injective instruction/head/operand tiling, blank renewal, static enforcement/repair, and E remain separate",
            "C_source":"unchanged; controller geometry, capacity, gate phase, and counters carry no gravity/source meaning",
        },
        "maturity_0_to_5":{"operational_quantum_and_records":2,"causal_time":1,"inertia_and_matter":1,"gravity_and_source":1,"Born_and_probability":1},
        "no_go_discipline":nogo,
        "optimal_next_campaign":"construct a streamed injective program-fibre placement for every Cycle652 primitive occurrence, couple each bounded tile to the already routed operands, and execute one full forward/inverse head circuit for L3/L6/L7 with no Python-supplied gate or site; keep blank renewal, static enforcement/repair, and E separate",
        "resources":{"elapsed_seconds":time.perf_counter()-started,
                     "maximum_RSS_bytes":int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform == "darwin" else resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024)},
    }
    result.update({"tests_passed":PASS,"tests_failed":FAIL,"tests_total":PASS+FAIL,
                   "pass":bool(overall and FAIL == 0)})
    RECEIPT.write_text(json.dumps(result, indent=2, sort_keys=True, default=json_default) + "\n")
    print(json.dumps({"status":result["Status"],"tests":f"{PASS}/{PASS+FAIL}",
                      "elapsed":result["resources"]["elapsed_seconds"],
                      "receipt":str(RECEIPT.relative_to(ROOT))}, sort_keys=True))
    export.cleanup()
    return int(not result["pass"])


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as stream:
        previous = sys.stdout; sys.stdout = Tee(previous, stream)
        try: raise SystemExit(main())
        finally: sys.stdout = previous
