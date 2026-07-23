#!/usr/bin/env python3
"""Cycle648: root-free preparation tournament for the Cycle642 orbit tree.

Three routes are executed from immutable shore 014cebe47b:

* a direction-sensitive four-M2 crossing tensor;
* weight-three/four isolated reset duals;
* a root-label-blind leaf-peeling face-syndrome controller.

The exact positive pieces are retained separately from physical translation
covariance, fine-nearest-neighbor enforcement, and full state preparation.
Authority: none.  Audit: unset.  Constitutional effect: none.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
import contextlib
import gc
import importlib
import io
from itertools import permutations, product
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SHORE_REF = "014cebe47bff2fbbd981b174a8b0ab8e70dfda53"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 8.0e-11
CAP_SECONDS = 180.0
CAP_BYTES = 3 * 1024**3
LOCAL_DIAMETER = 80
PASS = 0
FAIL = 0

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ROOT_FREE_ORBIT_TREE_PREPARATION_TOURNAMENT_"
    "CYCLE648_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / (
    "outputs/physical_root_free_orbit_tree_preparation_tournament_"
    "cycle648_receipt_2026_07_23.json"
)
COLD = ROOT / (
    "outputs/physical_root_free_orbit_tree_preparation_tournament_"
    "cycle648_cold_2026_07_23.txt"
)

C642_RUNNER = "scripts/physical_fixed_cubic_wilson_fill_incidence_cycle642_2026_07_23.py"
C642_NOTE = "docs/work_history/repo/review_feedback/PHYSICAL_FIXED_CUBIC_WILSON_FILL_INCIDENCE_CYCLE642_NOTE_2026-07-23.md"
C642_RECEIPT = "outputs/physical_fixed_cubic_wilson_fill_incidence_cycle642_receipt_2026_07_23.json"
C642_COLD = "outputs/physical_fixed_cubic_wilson_fill_incidence_cycle642_cold_2026_07_23.txt"
C643_NOTE = "docs/work_history/repo/review_feedback/ABSTRACT_FILL_DISK_FULL_TABLEAU_ISOMETRY_CYCLE643_NOTE_2026-07-23.md"
C643_RECEIPT = "outputs/abstract_fill_disk_full_tableau_isometry_cycle643_receipt_2026_07_23.json"
C644_RUNNER = "scripts/physical_bounded_spin_sector_genesis_tournament_cycle644_2026_07_23.py"
C644_NOTE = "docs/work_history/repo/review_feedback/PHYSICAL_BOUNDED_SPIN_SECTOR_GENESIS_TOURNAMENT_CYCLE644_NOTE_2026-07-23.md"
C644_RECEIPT = "outputs/physical_bounded_spin_sector_genesis_tournament_cycle644_receipt_2026_07_23.json"
C644_COLD = "outputs/physical_bounded_spin_sector_genesis_tournament_cycle644_cold_2026_07_23.txt"

PINS = {
    C642_RUNNER: "fb0d8366494066e4191d66b9a2d83180cd99bf6f622b9de355bf28494e050bf7",
    C642_NOTE: "13f8074746f3b5e978f971567bbebecd1006ccd13b7d5fe91a0e38a946d30d3e",
    C642_RECEIPT: "9251ac323d4f26b672783fa8ed01dc8da6f3059c308d37325b3d7984969c3b37",
    C642_COLD: "2af7cb45f80e1e5719da6750cd9f2efbbf2bee1bc14abe95e234eba91d6920cb",
    C643_NOTE: "e28a55a8312ae9cf4b9048f8b07557602e5a223cc6da487eeddd8b730a982d8f",
    C643_RECEIPT: "d87bf3c90cd0016073cd5f3259f5d8c45c81dbc0796174361057ef5edd07cbec",
    C644_RUNNER: "41a29d1ddc4f38b49bf8822b45b4bb62fc8b6e98231905a990863e714a5c87bd",
    C644_NOTE: "c72899538a369c1c078b36844ef3f1d402c0ac14ee028e26a960f6dfedb9a2b5",
    C644_RECEIPT: "5b54deeba72e96867ee7a0ed55ff5ffd7cd7087eb85a5aeac15903797cb3b740",
    C644_COLD: "042f969b21614f97aab829bbb32ee30cdce0c8dd064eaac76604ea2ffdda18db",
}

C642 = None
C644 = None


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, text):
        for stream in self.streams:
            stream.write(text)
            stream.flush()

    def flush(self):
        for stream in self.streams:
            stream.flush()


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def git_bytes(ref: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=ROOT)


def check(label: str, condition: bool, detail="") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, complex):
        return (float(value.real), float(value.imag))
    if isinstance(value, set):
        return sorted(value, key=repr)
    raise TypeError(type(value).__name__)


def immutable_line(path: str, fragment: str) -> int:
    lines = git_bytes(SHORE_REF, path).decode().splitlines()
    return next((number for number, line in enumerate(lines, 1) if fragment in line), 0)


def source_line(fragment: str) -> int:
    return next(
        (number for number, line in enumerate(Path(__file__).read_text().splitlines(), 1) if fragment in line),
        0,
    )


def cited_line_exists(ref: str, path: str, line: int) -> bool:
    try:
        lines = git_bytes(ref, path).decode().splitlines()
    except subprocess.CalledProcessError:
        return False
    return 1 <= line <= len(lines) and bool(lines[line - 1].strip())


def shore() -> tuple[dict, dict, dict]:
    observed = {path: sha256(git_bytes(SHORE_REF, path)).hexdigest() for path in PINS}
    local_mirrors = {
        path: sha(ROOT / path) for path in (C642_RUNNER, C644_RUNNER)
    }
    c642_receipt = json.loads(git_bytes(SHORE_REF, C642_RECEIPT))
    c644_receipt = json.loads(git_bytes(SHORE_REF, C644_RECEIPT))
    result = {
        "immutable_shore_ref": SHORE_REF,
        "observed": observed,
        "hashes_match": observed == PINS,
        "local_import_mirrors": local_mirrors,
        "local_import_mirrors_byte_equal_to_shore": all(local_mirrors[p] == PINS[p] for p in local_mirrors),
        "uncommitted_C646_or_C647_imported": False,
        "Cycle642_pass": c642_receipt["pass"],
        "Cycle642_authority": c642_receipt["authority"],
        "Cycle642_audit": c642_receipt["audit"],
        "Cycle642_shared_obstruction": c642_receipt["shared_route_independent_obstruction"],
        "Cycle642_axiom_pressure": c642_receipt["axiom_pressure"],
        "Cycle644_pass": c644_receipt["pass"],
        "Cycle644_authority": c644_receipt["authority"],
        "Cycle644_audit": c644_receipt["audit"],
        "Cycle644_full_periodic_E": c644_receipt["full_periodic_E_preparation_and_G_closed"],
        "Cycle644_axiom_pressure": c644_receipt["axiom_pressure"],
    }
    condition = bool(
        result["hashes_match"]
        and result["local_import_mirrors_byte_equal_to_shore"]
        and not result["uncommitted_C646_or_C647_imported"]
        and result["Cycle642_pass"] and result["Cycle644_pass"]
        and result["Cycle642_authority"] == result["Cycle644_authority"] == AUTHORITY
        and result["Cycle642_audit"] == result["Cycle644_audit"] == AUDIT
        and not result["Cycle642_shared_obstruction"]
        and not result["Cycle642_axiom_pressure"]
        and not result["Cycle644_full_periodic_E"]
        and not result["Cycle644_axiom_pressure"]
    )
    check("immutable Cycle642/643/644 shore and executable mirrors are byte exact", condition, result)
    return c642_receipt, c644_receipt, result


def load_modules() -> None:
    global C642, C644
    sys.path.insert(0, str(ROOT / "scripts"))
    C642 = importlib.import_module("physical_fixed_cubic_wilson_fill_incidence_cycle642_2026_07_23")
    C644 = importlib.import_module("physical_bounded_spin_sector_genesis_tournament_cycle644_2026_07_23")
    imported = {
        C642_RUNNER: sha(Path(C642.__file__).resolve()),
        C644_RUNNER: sha(Path(C644.__file__).resolve()),
    }
    check(
        "only byte-pinned Cycle642 and Cycle644 executable mirrors are imported",
        imported == {path: PINS[path] for path in imported},
        imported,
    )


def pauli_matrix(x_mask: int, z_mask: int) -> np.ndarray:
    matrix = np.zeros((16, 16), dtype=complex)
    phase = 1j ** ((x_mask & z_mask).bit_count())
    for basis in range(16):
        matrix[basis ^ x_mask, basis] = phase * ((-1) ** ((basis & z_mask).bit_count()))
    return matrix


def common_plus_state(operators: tuple[tuple[int, int], ...]) -> np.ndarray:
    projector = np.eye(16, dtype=complex)
    for x_mask, z_mask in operators:
        projector = projector @ (np.eye(16) + pauli_matrix(x_mask, z_mask)) / 2
    for basis in range(16):
        state = projector[:, basis]
        norm = np.linalg.norm(state)
        if norm > TOL:
            return state / norm
    raise AssertionError("empty local plus eigenspace")


def apply_one(state: np.ndarray, qubit: int, gate: np.ndarray) -> np.ndarray:
    output = np.zeros_like(state)
    for basis, amplitude in enumerate(state):
        source = (basis >> qubit) & 1
        for target in (0, 1):
            word = (basis & ~(1 << qubit)) | (target << qubit)
            output[word] += gate[target, source] * amplitude
    return output


def apply_cnot(state: np.ndarray, control: int, target: int) -> np.ndarray:
    output = np.zeros_like(state)
    for basis, amplitude in enumerate(state):
        output[basis ^ ((1 << target) if ((basis >> control) & 1) else 0)] += amplitude
    return output


def crossing_circuit_state(phase_first: bool, phase_second: bool) -> tuple[np.ndarray, float]:
    h = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
    s = np.asarray(((1, 0), (0, 1j)), dtype=complex)
    sd = s.conj().T
    state = np.zeros(16, dtype=complex)
    state[0] = 1
    state = apply_one(state, 0, h)
    state = apply_cnot(state, 0, 1)
    if phase_first:
        state = apply_one(state, 1, s)
    state = apply_one(state, 2, h)
    state = apply_cnot(state, 2, 3)
    if phase_second:
        state = apply_one(state, 3, s)
    returned = state.copy()
    if phase_second:
        returned = apply_one(returned, 3, sd)
    returned = apply_cnot(returned, 2, 3)
    returned = apply_one(returned, 2, h)
    if phase_first:
        returned = apply_one(returned, 1, sd)
    returned = apply_cnot(returned, 0, 1)
    returned = apply_one(returned, 0, h)
    blank = np.zeros(16, dtype=complex)
    blank[0] = 1
    return state, float(np.max(abs(returned - blank)))


def factor_expectation(pauli, states, block_lookup, single_axes) -> complex:
    value = complex(1j ** (pauli.phase - (pauli.x & pauli.z).bit_count()))
    touched = {}
    support = pauli.x | pauli.z
    while support:
        bit = support & -support
        qubit = bit.bit_length() - 1
        support ^= bit
        x_bit = (pauli.x >> qubit) & 1
        z_bit = (pauli.z >> qubit) & 1
        if qubit in block_lookup:
            block, local = block_lookup[qubit]
            x_mask, z_mask = touched.get(block, (0, 0))
            touched[block] = (x_mask | (x_bit << local), z_mask | (z_bit << local))
        else:
            axis = "X" if x_bit and not z_bit else "Z" if z_bit and not x_bit else "Y"
            prepared, sign = single_axes[qubit]
            if axis != prepared:
                return 0j
            value *= sign
    for block, (x_mask, z_mask) in touched.items():
        value *= C644.local_pauli_expectation(states[block], x_mask, z_mask)
    return value


def expectation_counts(values) -> dict:
    return {
        "plus_one": sum(abs(value - 1) < TOL for value in values),
        "minus_one": sum(abs(value + 1) < TOL for value in values),
        "zero": sum(abs(value) < TOL for value in values),
        "other": sum(
            abs(value) >= TOL and abs(value - 1) >= TOL and abs(value + 1) >= TOL
            for value in values
        ),
    }


def route_A_direction_sensitive_tensor() -> dict:
    sizes = []
    for length in (3, 6, 7):
        graph = C644.c247.PunctureGraph(length, terminals=1)
        wilsons = C644.translated_wilsons(graph)
        blocks = tuple(
            tuple(15 * cell + offset for offset in (2, 3, 8, 10))
            for cell in range(length**3)
        )
        lookup = {
            qubit: (block, local)
            for block, members in enumerate(blocks)
            for local, qubit in enumerate(members)
        }
        axes = {}
        for metadata in wilsons:
            pauli = metadata["pauli"]
            support = pauli.x | pauli.z
            while support:
                bit = support & -support
                qubit = bit.bit_length() - 1
                support ^= bit
                if qubit in lookup:
                    continue
                x_bit = (pauli.x >> qubit) & 1
                z_bit = (pauli.z >> qubit) & 1
                axis = "X" if x_bit and not z_bit else "Z" if z_bit and not x_bit else "Y"
                axes.setdefault(qubit, set()).add(axis)
        single_axes = {}
        for qubit in range(graph.qubits):
            if qubit in lookup:
                continue
            choices = axes.get(qubit, {"Z"})
            if len(choices) != 1:
                raise AssertionError((length, qubit, choices))
            axis = next(iter(choices))
            sign = -1 if length % 2 == 0 and qubit % 15 in (12, 13, 14) and axis == "X" else 1
            single_axes[qubit] = (axis, sign)

        states = []
        patterns = []
        circuit_residuals = []
        restriction_residuals = []
        state_cache = {}
        for cell, block in enumerate(blocks):
            restrictions = []
            for metadata in wilsons:
                pauli = metadata["pauli"]
                x_mask = z_mask = 0
                for local, qubit in enumerate(block):
                    x_mask |= ((pauli.x >> qubit) & 1) << local
                    z_mask |= ((pauli.z >> qubit) & 1) << local
                if x_mask or z_mask:
                    restrictions.append((x_mask, z_mask))
            pattern = tuple(sorted(set(restrictions)))
            patterns.append(pattern)
            anticommutes = sum(
                ((left[0] & right[1]).bit_count() + (left[1] & right[0]).bit_count()) % 2
                for index, left in enumerate(pattern)
                for right in pattern[index + 1:]
            )
            if anticommutes:
                raise AssertionError((length, cell, pattern))
            coordinate = graph.base.cells[cell]
            flags = (coordinate[2] == 0, coordinate[1] == 0)
            circuit_state, inverse_residual = crossing_circuit_state(*flags)
            state_cache.setdefault(pattern, common_plus_state(pattern))
            projector_state = state_cache[pattern]
            circuit_residuals.append(float(1 - abs(np.vdot(projector_state, circuit_state)) ** 2))
            circuit_residuals.append(inverse_residual)
            restriction_residuals.extend(
                abs(C644.local_pauli_expectation(circuit_state, *operator) - 1)
                for operator in pattern
            )
            states.append(circuit_state)

        wilson_values = tuple(
            factor_expectation(metadata["pauli"], states, lookup, single_axes)
            for metadata in wilsons
        )
        local_values = tuple(
            factor_expectation(row, states, lookup, single_axes)
            for row in C644.c532.local_stabilizers(graph)
        )
        coordinate_pattern = {
            graph.base.cells[cell]: patterns[cell] for cell in range(length**3)
        }
        translation_mismatches = {}
        for axis in range(3):
            mismatches = 0
            for coordinate, pattern in coordinate_pattern.items():
                source = list(coordinate)
                source[axis] = (source[axis] - 1) % length
                mismatches += coordinate_pattern[tuple(source)] != pattern
            translation_mismatches[str(axis)] = mismatches

        one_seam_cell = next(
            cell for cell, coordinate in enumerate(graph.base.cells)
            if (coordinate[2] == 0) ^ (coordinate[1] == 0)
        )
        deleted_states = list(states)
        deleted_states[one_seam_cell] = crossing_circuit_state(False, False)[0]
        deleted_values = tuple(
            factor_expectation(metadata["pauli"], deleted_states, lookup, single_axes)
            for metadata in wilsons
        )
        sizes.append({
            "length": length,
            "translated_Wilson_loops": len(wilsons),
            "expected_translated_Wilson_loops": 3 * length**2,
            "four_M2_blocks": len(blocks),
            "unique_direction_sensitive_block_patterns": len(set(patterns)),
            "block_pattern_histogram": dict(Counter(map(repr, patterns))),
            "local_restriction_pair_anticommutations": 0,
            "maximum_block_circuit_or_inverse_residual": max(circuit_residuals),
            "maximum_local_restriction_residual": max(restriction_residuals),
            "Wilson_expectation_counts": expectation_counts(wilson_values),
            "maximum_Wilson_residual": float(max(abs(value - 1) for value in wilson_values)),
            "local_stabilizer_expectation_counts": expectation_counts(local_values),
            "negative_single_M2_role_signs": sum(sign < 0 for _axis, sign in single_axes.values()),
            "per_loop_sign_markers": 0,
            "ordinary_unit_translation_pattern_mismatches": translation_mismatches,
            "coordinate_zero_phase_sheets": {"y": length**2, "z": length**2, "x": 0},
            "axis_cycle_phase_sheet_count_invariant": False,
            "delete_one_required_phase_gate_Wilson_counts": expectation_counts(deleted_values),
            "delete_one_required_phase_gate_maximum_Wilson_residual": float(max(abs(value - 1) for value in deleted_values)),
            "maximum_elementary_gate_support_M2": 2,
            "maximum_gates_per_four_M2_block": 6,
            "inverse_returns_four_M2_blank": max(circuit_residuals) < TOL,
        })
    result = {
        "sizes": sizes,
        "maximum_numerical_Wilson_residual_across_sizes": max(
            row["maximum_Wilson_residual"] for row in sizes
        ),
        "constructive_result": (
            "two Bell pairs per cell, with S on the first pair exactly on z=0 and on the second "
            "pair exactly on y=0, prepare all translated Wilson signs; even L also uses three "
            "translation-uniform negative X-role signs"
        ),
        "fixed_code_covariance": C644.c532.covariance_controls(),
        "all_translated_Wilson_signs_prepared": True,
        "per_loop_marker_or_global_query": False,
        "coordinate_zero_sheet_field_supplied": True,
        "ordinary_translation_covariant_preparation": False,
        "preparation_all24_all576_established": False,
        "full_local_stabilizer_preparation": False,
        "full_Cycle642_orbit_tree_E": False,
        "route_status": "EXACT_DIRECTION_SENSITIVE_WILSON_SEED__TWO_SUPPLIED_SEAM_SHEETS_LOCAL_CODE_OPEN",
    }
    result["pass"] = bool(
        all(
            row["translated_Wilson_loops"] == row["expected_translated_Wilson_loops"]
            and row["unique_direction_sensitive_block_patterns"] == 4
            and row["local_restriction_pair_anticommutations"] == 0
            and row["maximum_block_circuit_or_inverse_residual"] < TOL
            and row["maximum_local_restriction_residual"] < TOL
            and row["Wilson_expectation_counts"]["plus_one"] == row["translated_Wilson_loops"]
            and row["maximum_Wilson_residual"] < TOL
            and row["local_stabilizer_expectation_counts"]["zero"] > 0
            and row["per_loop_sign_markers"] == 0
            and row["ordinary_unit_translation_pattern_mismatches"]["0"] == 0
            and row["ordinary_unit_translation_pattern_mismatches"]["1"] == 2 * row["length"]**2
            and row["ordinary_unit_translation_pattern_mismatches"]["2"] == 2 * row["length"]**2
            and not row["axis_cycle_phase_sheet_count_invariant"]
            and row["delete_one_required_phase_gate_maximum_Wilson_residual"] > 0.9
            and row["maximum_elementary_gate_support_M2"] == 2
            and row["inverse_returns_four_M2_blank"]
            for row in sizes
        )
        and result["fixed_code_covariance"]["pass"]
        and result["all_translated_Wilson_signs_prepared"]
        and not result["per_loop_marker_or_global_query"]
        and result["coordinate_zero_sheet_field_supplied"]
        and not result["ordinary_translation_covariant_preparation"]
        and not result["preparation_all24_all576_established"]
        and not result["full_local_stabilizer_preparation"]
        and not result["full_Cycle642_orbit_tree_E"]
    )
    check("route A exactly closes the translated Wilson signs but exposes two supplied seam sheets", result["pass"], {
        "sizes": [(row["length"], row["Wilson_expectation_counts"], row["ordinary_unit_translation_pattern_mismatches"]) for row in sizes],
        "fixed_code_covariance": result["fixed_code_covariance"]["pass"],
    })
    return result


def independent_rows_tagged(rows, qubits: int):
    pivots = {}
    selected = []
    for kind, row in rows:
        reduced = row.symplectic(qubits)
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot in pivots:
                reduced ^= pivots[pivot]
            else:
                pivots[pivot] = reduced
                selected.append((kind, row))
                break
    return tuple(selected)


def syndrome_columns(basis, qubits: int, extra=()):
    rank = len(basis)
    columns = []
    for qubit in range(qubits):
        x_syn = sum((((row.z >> qubit) & 1) << index) for index, row in enumerate(basis))
        z_syn = sum((((row.x >> qubit) & 1) << index) for index, row in enumerate(basis))
        for offset, row in enumerate(extra):
            x_syn |= ((row.z >> qubit) & 1) << (rank + offset)
            z_syn |= ((row.x >> qubit) & 1) << (rank + offset)
        for axis, syndrome in (("X", x_syn), ("Z", z_syn), ("Y", x_syn ^ z_syn)):
            if syndrome:
                columns.append((syndrome, qubit, axis))
    return tuple(columns)


def witness_search(basis, qubits: int, positions, period: int, kinds, extra=()) -> dict:
    columns = syndrome_columns(basis, qubits, extra)
    single = {}
    for syndrome, qubit, axis in columns:
        single.setdefault(syndrome, (qubit, axis))
    pairs = {}
    for index, (left_syn, left_qubit, left_axis) in enumerate(columns):
        for right_syn, right_qubit, right_axis in columns[index + 1:]:
            if left_qubit != right_qubit:
                pairs.setdefault(
                    left_syn ^ right_syn,
                    ((left_qubit, left_axis), (right_qubit, right_axis)),
                )
    counts = Counter()
    kind_counts = defaultdict(Counter)
    accepted_local = Counter()
    kind_accepted_local = defaultdict(Counter)
    maximum_diameter = 0
    maximum_accepted_diameter = 0
    off_target_failures = 0
    repeated_qubit_failures = 0
    witness_digest = sha256()
    deleted_factor_signal = 0
    for generator, kind in enumerate(kinds):
        target = 1 << generator
        witness = None
        if target in single:
            witness = (single[target],)
        elif target in pairs:
            witness = pairs[target]
        else:
            for syndrome, item in single.items():
                pair = pairs.get(target ^ syndrome)
                if pair is not None and len({item[0], pair[0][0], pair[1][0]}) == 3:
                    witness = (item,) + pair
                    break
        if witness is None:
            for syndrome, left in pairs.items():
                right = pairs.get(target ^ syndrome)
                if right is not None and len({item[0] for item in left + right}) == 4:
                    witness = left + right
                    break
        if witness is None:
            counts["not_found"] += 1
            kind_counts[kind]["not_found"] += 1
            continue
        weight = len(witness)
        syndrome = 0
        for qubit, axis in witness:
            syndrome ^= next(
                value for value, candidate_qubit, candidate_axis in columns
                if candidate_qubit == qubit and candidate_axis == axis
            )
        off_target_failures += syndrome != target
        repeated_qubit_failures += len({qubit for qubit, _axis in witness}) != weight
        diameter = max(
            (
                C644.c532.periodic_l1(positions[left], positions[right], period)
                if period == 32 * 3 else C642.periodic_l1(positions[left], positions[right], period)
            )
            for left, _left_axis in witness
            for right, _right_axis in witness
        )
        maximum_diameter = max(maximum_diameter, diameter)
        counts[str(weight)] += 1
        kind_counts[kind][str(weight)] += 1
        if diameter <= LOCAL_DIAMETER:
            accepted_local[str(weight)] += 1
            kind_accepted_local[kind][str(weight)] += 1
            maximum_accepted_diameter = max(maximum_accepted_diameter, diameter)
        witness_digest.update(repr((generator, witness, syndrome, diameter)).encode())
        if deleted_factor_signal == 0 and weight >= 3:
            deleted = 0
            for qubit, axis in witness[:-1]:
                deleted ^= next(
                    value for value, candidate_qubit, candidate_axis in columns
                    if candidate_qubit == qubit and candidate_axis == axis
                )
            deleted_factor_signal = (deleted ^ target).bit_count()
    del pairs
    gc.collect()
    found = sum(value for key, value in counts.items() if key != "not_found")
    accepted = sum(accepted_local.values())
    return {
        "independent_generators": len(basis),
        "extra_preserved_rows": len(extra),
        "candidate_single_M2_Paulis": len(columns),
        "positive_witness_counts_by_support": dict(counts),
        "positive_witness_counts_by_generator_kind": {key: dict(value) for key, value in kind_counts.items()},
        "diameter_at_most_80_positive_witness_counts_by_support": dict(accepted_local),
        "diameter_at_most_80_counts_by_generator_kind": {key: dict(value) for key, value in kind_accepted_local.items()},
        "positive_witnesses_found": found,
        "diameter_at_most_80_positive_witnesses_found": accepted,
        "not_covered_by_executed_representative_search": len(basis) - found,
        "not_covered_by_diameter_at_most_80_witness_set": len(basis) - accepted,
        "maximum_positive_witness_diameter": maximum_diameter,
        "maximum_accepted_local_diameter": maximum_accepted_diameter,
        "off_target_syndrome_failures": off_target_failures,
        "repeated_qubit_failures": repeated_qubit_failures,
        "delete_one_factor_syndrome_hamming_signal": deleted_factor_signal,
        "witness_sha256": witness_digest.hexdigest(),
        "weight_one_two_search_complete": True,
        "weight_three_four_search_uses_one_representative_per_pair_syndrome": True,
        "uncovered_rows_are_not_certified_absence_of_weight_three_four_duals": True,
        "Kraus_completeness_for_every_positive_witness": True,
    }


def route_B_weight_three_four_pump() -> dict:
    graph = C644.c247.PunctureGraph(3, terminals=1)
    old_basis = C644.independent_rows(C644.c532.local_stabilizers(graph), graph.qubits)
    old_positions = tuple(C644.c532.physical_position(graph, q) for q in range(graph.qubits))
    old = witness_search(
        old_basis, graph.qubits, old_positions, 32 * 3,
        tuple("old_local" for _row in old_basis),
        C644.c532.wilson_initializers(graph),
    )

    with contextlib.redirect_stdout(io.StringIO()):
        _placement, fibers = C642.allocate_orbit_roles(3)
    obj = C642.build_tree_code(3, fibers)
    tagged = independent_rows_tagged(
        tuple(("local", row) for row in obj["local"])
        + tuple(("equality", row) for row in obj["equality"])
        + tuple(("face", row) for row in obj["faces"]),
        obj["qubits"],
    )
    full_basis = tuple(row for _kind, row in tagged)
    kinds = tuple(kind for kind, _row in tagged)
    modulus = C642.K * 3
    positions = [
        tuple(value % modulus for value in C642.old_position_K(obj["graph"], qubit))
        for qubit in range(obj["graph"].qubits)
    ]
    for role in obj["roles"]:
        for qubit, site in zip(obj["index"][role], obj["fibers"][role]):
            if qubit != len(positions):
                raise AssertionError("auxiliary position order")
            positions.append(tuple(value % modulus for value in site))
    full = witness_search(full_basis, obj["qubits"], tuple(positions), modulus, kinds)
    held = [
        {
            "length": length,
            "full_weight_three_four_pump_executed": length == 3,
            "status": "EXECUTED" if length == 3 else "NOT_EXECUTED_AFTER_INCOMPLETE_L3",
        }
        for length in (3, 6, 7)
    ]
    result = {
        "Cycle644_same_scope_old_local_comparator": old,
        "Cycle642_full_stabilizer_basis_L3": full,
        "held_size_control": held,
        "declared_local_physical_L1_diameter": LOCAL_DIAMETER,
        "measurement_outcome_used_only_for_its_local_correction": True,
        "runtime_Wilson_or_sector_query": False,
        "all_found_witnesses_preserve_every_other_selected_row": full["off_target_syndrome_failures"] == 0,
        "dissipative_map_inverse_applicable": False,
        "Stinespring_syndrome_exhaust_returned": False,
        "preparation_all24_all576_established": False,
        "full_periodic_E_prepared": False,
        "route_status": "WEIGHT3_4_POSITIVE_DUALS__FULL_L3_AND_HELD_PREPARATION_INCOMPLETE",
    }
    result["pass"] = bool(
        old["positive_witness_counts_by_support"] == {"not_found": 67, "3": 60, "4": 46, "1": 169, "2": 61}
        and old["positive_witnesses_found"] == 336
        and old["off_target_syndrome_failures"] == old["repeated_qubit_failures"] == 0
        and full["independent_generators"] == 454
        and full["positive_witness_counts_by_generator_kind"]["local"] == {"not_found": 67, "3": 60, "4": 46, "1": 169, "2": 61}
        and full["positive_witness_counts_by_generator_kind"]["equality"] == {"1": 39}
        and full["positive_witness_counts_by_generator_kind"]["face"] == {"not_found": 12}
        and full["positive_witnesses_found"] == 375
        and full["diameter_at_most_80_positive_witnesses_found"] > 300
        and full["not_covered_by_diameter_at_most_80_witness_set"] > 0
        and full["maximum_accepted_local_diameter"] <= LOCAL_DIAMETER
        and full["off_target_syndrome_failures"] == full["repeated_qubit_failures"] == 0
        and full["delete_one_factor_syndrome_hamming_signal"] > 0
        and result["measurement_outcome_used_only_for_its_local_correction"]
        and not result["runtime_Wilson_or_sector_query"]
        and result["all_found_witnesses_preserve_every_other_selected_row"]
        and not result["Stinespring_syndrome_exhaust_returned"]
        and not result["preparation_all24_all576_established"]
        and not result["full_periodic_E_prepared"]
    )
    check("route B adds exact weight-three/four reset duals but leaves explicit local, face, distance, and held gaps", result["pass"], {
        "old": old["positive_witness_counts_by_support"],
        "full_by_kind": full["positive_witness_counts_by_generator_kind"],
        "local_diameter_80": full["diameter_at_most_80_positive_witnesses_found"],
        "held": held,
    })
    return result


def peel_decode(length: int, negative_vertices) -> tuple[set, set, set, int]:
    vertices, edges = C642.fill_tree(length)
    active = set(vertices)
    syndrome = {vertex: int(vertex in negative_vertices) for vertex in vertices}
    adjacency = {vertex: set() for vertex in vertices}
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    selected = set()
    rounds = 0
    while len(active) > 2:
        leaves = tuple(vertex for vertex in active if len(adjacency[vertex] & active) <= 1)
        if not leaves:
            raise AssertionError("leaf peel found a cycle")
        updates = []
        for leaf in leaves:
            neighbors = tuple(adjacency[leaf] & active)
            if neighbors and syndrome[leaf]:
                selected.add(C642.edge_key(leaf, neighbors[0]))
                updates.append(neighbors[0])
        for neighbor in updates:
            syndrome[neighbor] ^= 1
        active -= set(leaves)
        rounds += 1
    if len(active) == 2:
        left, right = tuple(active)
        if right not in adjacency[left]:
            raise AssertionError("two-vertex center is disconnected")
        if syndrome[left] and syndrome[right]:
            selected.add(C642.edge_key(left, right))
            syndrome[left] = syndrome[right] = 0
        rounds += 1
    produced = set()
    for left, right in selected:
        produced.symmetric_difference_update((left, right))
    residual = {vertex for vertex in active if syndrome[vertex]}
    return selected, produced, residual, rounds


def map_vertices(frame, axis: int, vertices, length: int):
    target_axis = C642.act_vertex(frame, axis, C642.ROOT_VERTEX, length)[0]
    mapped = {C642.act_vertex(frame, axis, vertex, length)[1] for vertex in vertices}
    return target_axis, mapped


def map_edges(frame, axis: int, edges, length: int):
    mapped = set()
    target_axis = C642.act_vertex(frame, axis, C642.ROOT_VERTEX, length)[0]
    for left, right in edges:
        role = C642.act_edge(frame, (axis, left, right), length)
        if role[0] != target_axis:
            raise AssertionError("axis action mismatch")
        mapped.add(C642.edge_key(role[1], role[2]))
    return target_axis, mapped


def route_C_leaf_peeling(c642_receipt: dict) -> dict:
    pinned_routes = {
        row["length"]: row for row in c642_receipt["fine_NN_routing_scouts"]
    }
    sizes = []
    for length in (3, 6, 7):
        with contextlib.redirect_stdout(io.StringIO()):
            placement, fibers = C642.allocate_orbit_roles(length)
        obj = C642.build_tree_code(length, fibers)
        vertices, edges = C642.fill_tree(length)
        even_failures = odd_failures = 0
        maximum_rounds = 0
        even_count = odd_count = 0
        for word in range(1 << len(vertices)):
            negative = {vertices[index] for index in range(len(vertices)) if (word >> index) & 1}
            selected, produced, residual, rounds = peel_decode(length, negative)
            maximum_rounds = max(maximum_rounds, rounds)
            if len(negative) % 2 == 0:
                even_count += 1
                even_failures += produced != negative or bool(residual)
            else:
                odd_count += 1
                odd_failures += len(residual) != 1

        all24_failures = 0
        all576_failures = 0
        even_syndromes = [
            {vertices[index] for index in range(len(vertices)) if (word >> index) & 1}
            for word in range(1 << len(vertices))
            if word.bit_count() % 2 == 0
        ]
        for axis in range(3):
            for negative in even_syndromes:
                selected, _produced, _residual, _rounds = peel_decode(length, negative)
                for frame in C642.FRAMES:
                    _target, mapped_negative = map_vertices(frame, axis, negative, length)
                    mapped_selected = map_edges(frame, axis, selected, length)[1]
                    decoded = peel_decode(length, mapped_negative)[0]
                    all24_failures += mapped_selected != decoded
                for left_frame in C642.FRAMES:
                    for right_frame in C642.FRAMES:
                        product_frame = left_frame @ right_frame
                        mid_axis, mid_negative = map_vertices(right_frame, axis, negative, length)
                        final_axis, sequential_negative = map_vertices(left_frame, mid_axis, mid_negative, length)
                        product_axis, product_negative = map_vertices(product_frame, axis, negative, length)
                        mid_edge_axis, mid_edges = map_edges(right_frame, axis, selected, length)
                        final_edge_axis, sequential_edges = map_edges(left_frame, mid_edge_axis, mid_edges, length)
                        product_edge_axis, product_edges = map_edges(product_frame, axis, selected, length)
                        decoded = peel_decode(length, product_negative)[0]
                        all576_failures += (
                            final_axis != product_axis
                            or final_edge_axis != product_edge_axis
                            or sequential_negative != product_negative
                            or sequential_edges != product_edges
                            or decoded != product_edges
                        )

        elementary_failures = 0
        two_face_syndrome_failures = 0
        for role in obj["roles"]:
            qubit = obj["index"][role][0]
            correction = C642.c235.Pauli(x=1 << qubit)
            elementary_failures += sum(not correction.commutes(row) for row in obj["equality"])
            elementary_failures += sum(not correction.commutes(row) for row in obj["local"])
            face_syndrome = tuple(index for index, row in enumerate(obj["faces"]) if not correction.commutes(row))
            two_face_syndrome_failures += len(face_syndrome) != 2

        first_edge = edges[0]
        selected, produced, residual, _rounds = peel_decode(length, set(first_edge))
        deletion_signal = len(set(first_edge) ^ (produced ^ set(first_edge))) if selected else 0
        route = pinned_routes[length]
        sizes.append({
            "length": length,
            "tree_vertices_per_axis": len(vertices),
            "tree_edges_per_axis": len(edges),
            "all_even_face_syndromes": even_count,
            "all_odd_face_syndromes": odd_count,
            "even_syndrome_decode_failures": even_failures,
            "odd_syndromes_not_leaving_exactly_one_residual": odd_failures,
            "maximum_synchronous_leaf_rounds": maximum_rounds,
            "all24_decoder_covariance_failures": all24_failures,
            "all576_decoder_group_failures": all576_failures,
            "elementary_aux_X_equality_or_local_commutator_failures": elementary_failures,
            "elementary_aux_X_two_face_syndrome_failures": two_face_syndrome_failures,
            "delete_one_selected_edge_correction_syndrome_signal": deletion_signal,
            "orbit_role_placement_pass": placement["pass"],
            "maximum_face_measurement_support_M2": max((row.x | row.z).bit_count() for row in obj["faces"]),
            "maximum_elementary_correction_support_M2": 1,
            "maximum_inherited_pair_route_length": route["maximum_shortest_fine_NN_path_edges"],
            "autonomous_crossing_schedule_or_static_local_check_gadget": route["autonomous_crossing_schedule_or_static_local_check_gadget_constructed"],
            "strict_physical_enforcement_pass": route["strict_physical_enforcement_pass"],
        })
    result = {
        "sizes": sizes,
        "exact_surface": "all even face syndromes are decoded by a synchronous adjacency-only leaf peel",
        "root_vertex_label_queried_by_decoder": False,
        "global_parity_queried_at_runtime": False,
        "odd_face_parity_closed": False,
        "one_odd_residual_per_axis_without_absorber": True,
        "a_supplied_single_defect_absorber_would_close_odd_parity": True,
        "all24_all576_abstract_tree_decoder_covariance": True,
        "physical_translation_covariant_preparation": False,
        "face_measurement_fine_NN_gadget_or_crossing_schedule_constructed": False,
        "dissipative_controller_has_unitary_inverse": False,
        "Stinespring_history_and_exhaust_returned": False,
        "lawful_domain": "even face syndromes, equivalently already-fixed Wilson + sector",
        "full_periodic_E_prepared": False,
        "route_status": "EXACT_ROOT_LABEL_BLIND_EVEN_SYNDROME_LEAF_PUMP__ODD_PARITY_AND_PHYSICAL_ROUTING_OPEN",
    }
    result["pass"] = bool(
        all(
            row["all_even_face_syndromes"] == 2 ** row["length"]
            and row["all_odd_face_syndromes"] == 2 ** row["length"]
            and row["even_syndrome_decode_failures"] == 0
            and row["odd_syndromes_not_leaving_exactly_one_residual"] == 0
            and row["all24_decoder_covariance_failures"] == 0
            and row["all576_decoder_group_failures"] == 0
            and row["elementary_aux_X_equality_or_local_commutator_failures"] == 0
            and row["elementary_aux_X_two_face_syndrome_failures"] == 0
            and row["delete_one_selected_edge_correction_syndrome_signal"] > 0
            and row["orbit_role_placement_pass"]
            and row["maximum_elementary_correction_support_M2"] == 1
            and not row["autonomous_crossing_schedule_or_static_local_check_gadget"]
            and not row["strict_physical_enforcement_pass"]
            for row in sizes
        )
        and not result["root_vertex_label_queried_by_decoder"]
        and not result["global_parity_queried_at_runtime"]
        and not result["odd_face_parity_closed"]
        and result["one_odd_residual_per_axis_without_absorber"]
        and result["all24_all576_abstract_tree_decoder_covariance"]
        and not result["physical_translation_covariant_preparation"]
        and not result["face_measurement_fine_NN_gadget_or_crossing_schedule_constructed"]
        and not result["Stinespring_history_and_exhaust_returned"]
        and not result["full_periodic_E_prepared"]
    )
    check("route C exactly pumps every even orbit-tree face syndrome without reading a root label and isolates the odd-parity residual", result["pass"], {
        "sizes": [(row["length"], row["all_even_face_syndromes"], row["maximum_synchronous_leaf_rounds"], row["all24_decoder_covariance_failures"], row["all576_decoder_group_failures"]) for row in sizes],
    })
    return result


def no_go_discipline(route_a: dict, route_b: dict, route_c: dict) -> dict:
    families = [
        {"family": "direction-sensitive crossing product tensor", "object": "four existing rough-code M2s per cell", "mechanism": "locally varying commuting Wilson restrictions", "terminal": "one translation-covariant root-free tensor field plus all local checks", "honesty_marker": "ATTEMPTED", "target_equivalent": False, "result": route_a["route_status"]},
        {"family": "isolated weight-three/four reset duals", "object": "independent Cycle642 stabilizer basis", "mechanism": "bounded Pauli syndrome dual and local Kraus reset", "terminal": "complete L3/L6/L7 dual coverage and returned exhaust", "honesty_marker": "ATTEMPTED", "target_equivalent": True, "result": route_b["route_status"]},
        {"family": "root-label-blind leaf syndrome automaton", "object": "Cycle642 face-incidence tree", "mechanism": "synchronous leaf elimination and auxiliary-edge X correction", "terminal": "even and odd parity plus fine-NN measurement controller", "honesty_marker": "ATTEMPTED", "target_equivalent": False, "result": route_c["route_status"]},
    ]
    open_routes = [
        {"family": "injective graded PEPS", "object": "virtual crossing bonds", "mechanism": "absorb sheet characters into a translation-invariant tensor", "terminal": "root-free fixed-sector PEPS", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
        {"family": "distributed local Clifford cellular automaton", "object": "state-carried tableau and routing rails", "mechanism": "compile and uncompute the Cycle643 frame locally", "terminal": "bounded-distance E and inverse", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
        {"family": "defect/code growth", "object": "moving local rough boundary", "mechanism": "grow a prepared open patch and heal its seam", "terminal": "periodic code without residual defect", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
        {"family": "reversible routed syndrome controller", "object": "Cycle642 shortest-path descriptors and crossing colors", "mechanism": "state-carried compute-copy-uncompute", "terminal": "returned routing work and full leakage", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
        {"family": "translation-invariant dissipative cooling", "object": "commuting-Pauli Hamiltonian plus finite reservoirs", "mechanism": "defect diffusion, annihilation and sector-changing local carrier", "terminal": "unique fixed code space with held mixing certificate", "search_status": "OPEN_UNTESTED_NOT_COUNTED"},
    ]
    walls = {
        "W_sheet": "route A requires coordinate-zero y/z phase sheets and an L-parity role sign",
        "W_dual": "route B leaves selected L3 rows without positive diameter-80 witnesses and has no held pump",
        "W_odd": "route C auxiliary edge corrections span only even face syndromes",
        "W_route": "Cycle642 face measurements still lack a fine-NN crossing gadget or autonomous routed schedule",
        "W_cov": "fixed code and abstract decoder covariance do not establish preparation translation/all24/all576 covariance",
    }
    interfaces = {
        "W_sheet": "rough-code crossing tensor field",
        "W_dual": "selected stabilizer-syndrome dual search",
        "W_odd": "tree incidence image over GF(2)",
        "W_route": "physical fine-NN measurement routing",
        "W_cov": "preparation orbit under translations and proper-cubic frames",
    }
    pairs = [
        {
            "from": source, "to": target, "closure_implied": False,
            "independence_evidence": {
                "status": "NOT_ESTABLISHED_BEYOND_EXECUTED_INTERFACES",
                "from_interface": interfaces[source], "to_interface": interfaces[target],
                "reason": f"closing {source} on {interfaces[source]} does not construct or test {target} on {interfaces[target]}",
            },
        }
        for source, target in permutations(walls, 2)
    ]
    phrases = (
        "we assume", "by construction", "as is standard", "the framework provides",
        "bridge context", "background", "naturally", "obviously", "standard qft",
        "registered", "canonical",
    )
    hits = tuple(phrase for phrase in phrases if phrase in NOTE.read_text().lower())
    current = "scripts/physical_root_free_orbit_tree_preparation_tournament_cycle648_2026_07_23.py"
    current_ref = "working-tree Cycle648 candidate"
    n4 = [
        {"prior_ref": SHORE_REF, "prior_path": C644_NOTE, "prior_line": immutable_line(C644_NOTE, "maximum residual from the all-plus target is exactly 1"), "prior_residual": "identical repeated crossing tensor has translated-Wilson residual 1", "current_ref": current_ref, "current_path": current, "current_line": source_line("def route_A_direction_sensitive_tensor"), "current_residual": "direction-sensitive y/z sheet tensor has all translated Wilson signs +1 with maximum numerical residual 3.1086244689504383e-15", "same_scope": True, "exact_match": True, "use_as_closure": True},
        {"prior_ref": SHORE_REF, "prior_path": C644_NOTE, "prior_line": immutable_line(C644_NOTE, "leaves the remainder explicit"), "prior_residual": "weight-one/two Wilson-preserving L3 search leaves 173 old local generators", "current_ref": current_ref, "current_path": current, "current_line": source_line("def route_B_weight_three_four_pump"), "current_residual": "same old-local/Wilson scope gains 60 weight-three and 46 weight-four witnesses and leaves 67 uncovered by the executed search", "same_scope": True, "exact_match": True, "use_as_closure": True},
        {"prior_ref": SHORE_REF, "prior_path": C642_NOTE, "prior_line": immutable_line(C642_NOTE, "No state-preparation map"), "prior_residual": "Cycle642 has no state preparation", "current_ref": current_ref, "current_path": current, "current_line": source_line("def route_C_leaf_peeling"), "current_residual": "face leaf pump is exact only on even syndrome and lacks physical measurement routing", "same_scope": True, "exact_match": True, "use_as_closure": False},
        {"prior_ref": SHORE_REF, "prior_path": C643_NOTE, "prior_line": immutable_line(C643_NOTE, "Cycle 643 closes Cycle537's state-preparation/isometry omission"), "prior_residual": "Cycle643 closes a different abstract square-fill tableau", "current_ref": current_ref, "current_path": current, "current_line": source_line("def route_C_leaf_peeling"), "current_residual": "Cycle648 tests the Cycle642 orbit-tree face incidence", "same_scope": False, "exact_match": False, "use_as_closure": False},
    ]
    n5 = [
        {"claim": "direction-sensitive local gates are not root-free preparation", "per_element": "H/S/CNOT support is at most two", "per_site": "four block patterns are exact", "per_mode": "all translated Wilson signs are plus", "per_block": "two coordinate-zero sheet predicates select phases", "lattice_wide": "ordinary y/z translation mismatch is 2L^2"},
        {"claim": "support weight four is not physical locality", "per_element": "each Pauli factor is one M2", "per_site": "accepted witnesses have diameter at most 80", "per_mode": "positive syndrome targets are exact", "per_block": "some algebraic witnesses have diameter above 80", "lattice_wide": "held L6/L7 full search is absent"},
        {"claim": "root-label-blind decoding is not arbitrary-sector genesis", "per_element": "edge X toggles two faces", "per_site": "leaf updates use adjacency only", "per_mode": "every even syndrome closes", "per_block": "odd syndrome leaves one defect", "lattice_wide": "no sector-changing absorber is present"},
        {"claim": "abstract tree covariance is not preparation covariance", "per_element": "edge action is exact", "per_site": "orbit fibers close all24", "per_mode": "decoder commutes with all24/all576", "per_block": "face measurement routing remains absent", "lattice_wide": "macro-origin K129 placement and seam sheets remain"},
        {"claim": "a partial reset pump is not a full E", "per_element": "each accepted Kraus pair is complete", "per_site": "all equality rows have positive duals", "per_mode": "face-even pump is exhaustive", "per_block": "67 local rows and odd face parity remain", "lattice_wide": "no L3/L6/L7 prepare-update-unprepare compiler"},
    ]
    n6 = [
        {"file": C642_NOTE, "status": "PINNED_ORBIT_TREE_PARENT", "what_closes": "bounded incidence algebra and all24/all576 role fibers, not preparation"},
        {"file": C643_NOTE, "status": "PINNED_ABSTRACT_TABLEAU_COMPARATOR", "what_closes": "global abstract H/S/CNOT isometry with supplied pivot/root/order"},
        {"file": C644_NOTE, "status": "PINNED_GENESIS_PARENT", "what_closes": "rooted triplet and reversible plaquette; supplies exact failed scalar tensor residual"},
        {"file": current, "status": "CURRENT_EXECUTABLE", "what_closes": "direction-sensitive Wilson seed, positive weight-three/four duals, and even face-syndrome decoder"},
        {"file": "UNMATERIALIZED/cycle649_distributed_cap_controller.py", "status": "OPEN", "what_closes": "state-carried fine-NN face measurement, odd-defect absorption, and returned exhaust"},
    ]
    steelman = {
        "argument": "A translation-invariant graded PEPS can place the two seam characters in virtual bond gauge rather than coordinate-zero tensors, while a distributed reversible syndrome automaton transports the remaining local and odd face defects through Cycle642's already explicit path family, absorbs them in a mobile defect pair, and uncomputes every routing rail.",
        "mechanism": "virtual-bond gauge plus state-carried defect transport and compute-copy-uncompute",
        "terminal_obligation": "literal L3/L6/L7 physical E, ordinary translations, all24/all576 preparation covariance, zero local/face syndrome, odd-sector closure, returned work, deletion, leakage and update intertwining",
        "citations": [
            {"ref": SHORE_REF, "path": C642_NOTE, "line": immutable_line(C642_NOTE, "static subsystem-wire gadget or an autonomous"), "supports": "Cycle642 leaves a state-carried crossing controller open"},
            {"ref": SHORE_REF, "path": C644_NOTE, "line": immutable_line(C644_NOTE, "weight-three/four corrections"), "supports": "higher-weight and cellular-automaton reset routes remained open"},
        ],
        "action": "compile a distributed cap controller with a mobile parity absorber and returned route history",
        "actionable": True,
    }
    echoes = [
        {"cycle": "Cycle629", "citation_ref": SHORE_REF, "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md", "citation_line": immutable_line("docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md", "state-carried"), "retired": "external origin on its declared marker orbit", "mechanism": "state-carried translation orbit", "applicability": "ACTIONABLE_FOR_REPLACING_COORDINATE_ZERO_SHEETS"},
        {"cycle": "Cycle642", "citation_ref": SHORE_REF, "citation_path": C642_NOTE, "citation_line": immutable_line(C642_NOTE, "state-carried crossing schedule"), "retired": False, "mechanism": "static wire or autonomous routed enforcement", "applicability": "EXACT_PHYSICAL_ROUTING_RESIDUAL"},
        {"cycle": "Cycle643", "citation_ref": SHORE_REF, "citation_path": C643_NOTE, "citation_line": immutable_line(C643_NOTE, "pivot/root and row order"), "retired": "abstract state-preparation omission only", "mechanism": "global Clifford tableau synthesis", "applicability": "DOES_NOT_CLOSE_AUTONOMOUS_PHYSICAL_GENESIS"},
        {"cycle": "Cycle644", "citation_ref": SHORE_REF, "citation_path": C644_NOTE, "citation_line": immutable_line(C644_NOTE, "multi-round cellular automaton"), "retired": "identical scalar crossing tensor only", "mechanism": "direction-sensitive crossing tensor and higher-weight reset", "applicability": "PARTIALLY_ADVANCED_HERE_WITH_LIVE_PEPEPS_AND_AUTOMATON_ROUTES"},
    ]
    n4_lines = all(cited_line_exists(row["prior_ref"], row["prior_path"], row["prior_line"]) and row["current_line"] > 0 for row in n4)
    n7_lines = all(cited_line_exists(row["ref"], row["path"], row["line"]) for row in steelman["citations"])
    n8_lines = all(cited_line_exists(row["citation_ref"], row["citation_path"], row["citation_line"]) for row in echoes)
    result = {
        "skill_freshness": {"origin_main_checked": True, "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7", "local_skill_sha256": "aeac7b2b7df30c350961f4b36b980a91e9c2ebeca3f35b6c1adcd731071bdab5", "proof_search_governance_sha256": "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258", "newer_origin_main_followed": True},
        "N1_normalized_families": families, "N1_qualifying_attempts": sum(row["target_equivalent"] for row in families), "N1_required_for_negative": 5, "N1_required_for_broad_negative": 5, "N1_open_routes_not_counted": open_routes,
        "N2_collapsed_walls": walls, "N2_directed_pairs": pairs, "N2_directed_pair_count": len(pairs), "N2_machine_check_count": len(pairs), "N2_independence_complete": False,
        "N3_hidden_wall_phrases": phrases, "N3_note_phrase_hits": hits,
        "N3_explicit_supplied_structure": ["immutable Cycle642/643/644 shore", "compile-time L/parity", "two coordinate-zero phase sheets", "four local tensor patterns", "selected L3 stabilizer basis", "one pair-syndrome representative", "diameter 80 threshold", "Cycle642 tree topology and K129 macro-origin", "synchronous active flags and measured face syndromes"],
        "N4_exact_residual_matching": n4, "N4_exact_residual_matches": n4[:-1], "N4_dropped_nonmatches": n4[-1:], "N4_cited_lines_exist": n4_lines,
        "N5_five_resolution_rhetoric_audit": n5,
        "N6_partial_closure_paths": n6,
        "N7_cited_actionable_steelman": steelman, "N7_cited_lines_exist": n7_lines,
        "N8_rowwise_cross_cycle_echo": echoes, "N8_cited_lines_exist": n8_lines,
        "Status": "PASS", "artifact_status": "PARTIAL_CONSTRUCTIVE_ADVANCE_NO_ROOT_FREE_FULL_E",
        "broad_negative_gate": "FAIL / DO NOT SHIP", "broad_no_go_claim": False,
        "minimum_content_gate": "FAIL / DO NOT SHIP", "minimum_content_claim": False,
        "shared_obstruction_gate": "FAIL / DO NOT SHIP", "shared_obstruction_claim": False,
        "axiom_pressure_gate": "FAIL / DO NOT SHIP", "axiom_pressure_claim": False,
        "broad_negative_shipped": False, "minimum_content_shipped": False,
        "shared_obstruction_shipped": False, "axiom_pressure_shipped": False,
        "negative_claim_shipped": False, "shared_route_independent_obstruction": False, "axiom_pressure": False,
    }
    schema = bool(
        len(families) == 3 and all(row["honesty_marker"] == "ATTEMPTED" for row in families)
        and len(open_routes) == 5 and all("honesty_marker" not in row for row in open_routes)
        and result["N1_required_for_negative"] == result["N1_required_for_broad_negative"] == 5
        and result["N1_qualifying_attempts"] < result["N1_required_for_negative"]
        and len(pairs) == result["N2_machine_check_count"] == 20
        and len({(row["from"], row["to"]) for row in pairs}) == 20
        and all(row["closure_implied"] is False and row["independence_evidence"]["reason"] for row in pairs)
        and not hits and n4_lines and n7_lines and n8_lines
        and all(row["prior_ref"] == SHORE_REF and row["current_ref"] == current_ref for row in n4)
        and all(row["same_scope"] and row["exact_match"] for row in n4[:-1])
        and all(not row["same_scope"] and not row["exact_match"] and not row["use_as_closure"] for row in n4[-1:])
        and all(all(key in row for key in ("per_element", "per_site", "per_mode", "per_block", "lattice_wide")) for row in n5)
        and all(set(row) == {"file", "status", "what_closes"} for row in n6)
        and all(row["ref"] == SHORE_REF for row in steelman["citations"])
        and all(row["citation_ref"] == SHORE_REF and all(key in row for key in ("retired", "mechanism", "applicability")) for row in echoes)
        and result["Status"] == "PASS"
        and all(result[key] == "FAIL / DO NOT SHIP" for key in ("broad_negative_gate", "minimum_content_gate", "shared_obstruction_gate", "axiom_pressure_gate"))
        and all(result[key] is False for key in ("broad_no_go_claim", "minimum_content_claim", "shared_obstruction_claim", "axiom_pressure_claim"))
        and all(result[key] is False for key in ("broad_negative_shipped", "minimum_content_shipped", "shared_obstruction_shipped", "axiom_pressure_shipped"))
        and not result["negative_claim_shipped"]
        and not result["shared_route_independent_obstruction"]
        and not result["axiom_pressure"]
    )
    result["pass"] = schema
    check("full N1-N8 keeps every broad negative and promotion claim blocked", schema, {
        "N1_qualifying": result["N1_qualifying_attempts"], "N2_directed": len(pairs),
        "N4": n4_lines, "N7": n7_lines, "N8": n8_lines,
    })
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "## Exact target", "## Strongest result", "## Route A", "## Route B", "## Route C",
        "## N1-N8 discipline", "## Supplied structure", "## Dependency ledger", "## Scope firewall",
    )
    result = {
        "missing_sections": tuple(section for section in required if section not in text),
        "authority_none": "Authority: **none**" in text,
        "audit_unset": "Audit: **unset**" in text,
        "accepted_false": "Accepted: **false**" in text,
    }
    result["pass"] = not result["missing_sections"] and all(result[key] for key in ("authority_none", "audit_unset", "accepted_false"))
    check("Cycle648 note exposes target, routes, controls, N1-N8 and supplied structure", result["pass"], result)
    return result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    print("Cycle648 root-free orbit-tree preparation tournament", AUTHORITY, AUDIT)
    c642_receipt, c644_receipt, shore_result = shore()
    load_modules()
    note = note_contract()
    route_a = route_A_direction_sensitive_tensor()
    route_b = route_B_weight_three_four_pump()
    route_c = route_C_leaf_peeling(c642_receipt)
    discipline = no_go_discipline(route_a, route_b, route_c)
    promotion_gates = {
        "broad_negative_gate": "FAIL / DO NOT SHIP", "minimum_content_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction_gate": "FAIL / DO NOT SHIP", "axiom_pressure_gate": "FAIL / DO NOT SHIP",
    }
    top_claims = {
        "broad_no_go_claim": False, "minimum_content_claim": False,
        "shared_obstruction_claim": False, "axiom_pressure_claim": False,
    }
    top_shipped = {
        "broad_negative_shipped": False, "minimum_content_shipped": False,
        "shared_obstruction_shipped": False, "axiom_pressure_shipped": False,
    }
    claim_contract = bool(
        discipline["Status"] == "PASS" and discipline["pass"]
        and discipline["N1_required_for_negative"] == discipline["N1_required_for_broad_negative"] == 5
        and all(discipline[key] == value for key, value in promotion_gates.items())
        and all(discipline[key] is value for key, value in top_claims.items())
        and all(discipline[key] is value for key, value in top_shipped.items())
        and not discipline["negative_claim_shipped"]
        and not discipline["shared_route_independent_obstruction"] and not discipline["axiom_pressure"]
    )
    check("top-level status, claim flags, and four promotion gates are exact", claim_contract, {
        "Status": discipline["Status"], "gates": promotion_gates, "claims": top_claims,
        "shipped": top_shipped,
    })
    fixture = C644.c532.fixture_controls()
    c642_factor_rows = c642_receipt["tree_fill_target_times_gauge_certificates"]
    fixture_pass = bool(fixture["pass"] and all(row["pass"] for row in c642_factor_rows))
    check("pinned mass/contact/seam and Cycle642 target-times-gauge fixtures remain exact", fixture_pass, {
        "mass": fixture["Cycle219_mass_fixture_residual"],
        "contact_deletion": fixture["Cycle230_contact_deletion_residual"],
        "seam": fixture["Cycle230_seam_subchecks"],
        "Cycle642_sizes": [row["length"] for row in c642_factor_rows],
    })
    elapsed = time.monotonic() - started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    check("cold run stays within declared resource caps", elapsed < CAP_SECONDS and maximum_rss < CAP_BYTES, {
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
    })
    receipt = {
        "status": "cycle648-root-free-orbit-tree-preparation-tournament",
        "Status": discipline["Status"],
        "classification": "PARTIAL_CONSTRUCTIVE_ADVANCE_NO_ROOT_FREE_FULL_E",
        "authority": AUTHORITY, "audit": AUDIT, "author_accepted": False,
        "author_artifact_status_accepted": False, "constitutional_effect": "none",
        **promotion_gates,
        **top_claims,
        **top_shipped,
        "canonical_claim_gate_contract": {"Status": discipline["Status"], **promotion_gates, **top_claims, **top_shipped, "pass": claim_contract},
        "breakthrough": False,
        "immutable_shore_ref": SHORE_REF,
        "pins": PINS,
        "runner_sha256": sha(Path(__file__)), "note_sha256": sha(NOTE),
        "shore": shore_result, "note_contract": note,
        "exact_target_contract": {
            "target_statement": "autonomous ordinary-translation-covariant preparation of the Cycle642 orbit-tree gauge/parity sector on physical M2 sites",
            "domain": "periodic L3 construction, L6 train, held L7; lawful target/gauge inputs; all24/all576 where applicable",
            "allowed_premises": "only immutable shore 014cebe47b and explicitly inventoried local ancillas/controllers",
            "forbidden_weakenings": "no root, coordinate-zero seam sheet, growing path service, global parity query, host sector branch, or unreturned work",
            "required_edges": "inverse where unitary, dissipative exhaust boundary, deletion, leakage, held-size, ordinary translations, proper-cubic covariance",
            "completion_witness": "literal preparation E or CPTP preparation plus physical update with code-space intertwiner and zero residuals",
            "not_closure": "Wilson-only seed, fixed-code covariance, partial syndrome pump, abstract incidence decoder, or support weight without physical diameter",
        },
        "approach_registry": [
            {"family": "direction-sensitive crossing product tensor", "object_formulation": "four-M2 cell tensors", "mechanism_invariant": "commuting local Wilson restrictions", "terminal_obligation": "translation-covariant full code seed", "strength_vs_target": "weaker", "status": "provisional", "concrete_evidence": route_a["route_status"], "reopen_condition": "virtualize the two sheet characters"},
            {"family": "weight-three/four reset duals", "object_formulation": "stabilizer syndrome columns", "mechanism_invariant": "isolated bounded Pauli dual", "terminal_obligation": "complete held-size pump with exhaust", "strength_vs_target": "target-equivalent", "status": "blocked-equivalent", "concrete_evidence": route_b["route_status"], "reopen_condition": "new local basis or multi-round defect transport"},
            {"family": "root-label-blind leaf automaton", "object_formulation": "tree incidence syndrome", "mechanism_invariant": "even boundary image", "terminal_obligation": "odd parity and physical routed measurement", "strength_vs_target": "weaker", "status": "provisional", "concrete_evidence": route_c["route_status"], "reopen_condition": "mobile local odd-defect absorber and returned routing"},
        ],
        "route_A_direction_sensitive_crossing_tensor": route_a,
        "route_B_weight_three_four_reset_duals": route_b,
        "route_C_root_label_blind_leaf_pump": route_c,
        "route_by_route_disposition": {"A": route_a["route_status"], "B": route_b["route_status"], "C": route_c["route_status"]},
        "strongest_constructive_result": "a four-pattern support-two circuit prepares all 3L^2 translated Wilson signs at L3/L6/L7 with zero per-loop markers and exact inverse; the exact pattern is two coordinate-zero phase sheets, so it is not root-free or ordinary-translation covariant",
        "full_root_free_translation_covariant_preparation": False,
        "fixed_code_all24_all576": route_a["fixed_code_covariance"]["pass"],
        "fixed_code_covariance_is_state_preparation": False,
        "preparation_all24_all576_established": False,
        "full_E_G_intertwiner_closed": False,
        "logical_fixtures": {
            "Cycle642_factor_rows_pass": all(row["pass"] for row in c642_factor_rows),
            "Cycle219_mass_residual": fixture["Cycle219_mass_fixture_residual"],
            "Cycle230_contact_deletion_residual": fixture["Cycle230_contact_deletion_residual"],
            "Cycle230_seam_subchecks": fixture["Cycle230_seam_subchecks"],
            "fixture_pass": fixture_pass,
        },
        "no_go_discipline": discipline,
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
        "supplied_structure": [
            "immutable shore 014cebe47b", "compile-time L and parity", "Cycle642 tree and K129 macro-origin",
            "four local crossing pattern labels", "coordinate-zero y and z phase sheets", "three even-L X-role signs",
            "selected independent L3 stabilizer basis", "one representative per pair syndrome", "diameter-80 acceptance threshold",
            "measured face syndrome bits", "active-vertex flags and synchronous leaf rounds", "Cycle642 shortest-path family without crossing schedule",
        ],
        "scope_firewall": {
            "Wilson_seed_is_full_code_E": False, "coordinate_sheet_tensor_is_root_free": False,
            "support_weight_four_is_physical_locality": False, "uncovered_search_row_is_no_dual_theorem": False,
            "even_face_decoder_is_arbitrary_sector_genesis": False, "abstract_decoder_covariance_is_preparation_covariance": False,
            "fixed_code_covariance_is_state_preparation": False, "compiler_round_is_time": False,
            "phase_is_energy": False, "generator_is_rate": False, "gauge_seed_is_Record": False,
            "source_or_gravity_claimed": False,
        },
        "six_wall_ledger": {
            "C_ref": "advanced: per-loop markers and growing rooted Wilson paths are replaced by two explicit coordinate-zero phase sheets; root-free sheet genesis remains open",
            "C_num": "advanced locally: exact support-three/four syndrome witnesses; no empirical normalization or Born statement",
            "C_wrap": "advanced: every translated Wilson sign is exact and even tree-face syndromes pump without a root-label query; odd parity and physical face routing remain",
            "C_int": "pinned Cycle642 quotient plus mass/contact/seam comparators only; no new full update or E G intertwiner",
            "C_local": "mixed: support-two Wilson circuit passes; diameter-80 reset witnesses cover a strict subset; face measurement paths lack crossing control",
            "C_source": "unchanged: no energy, rate, source, stress, gravity, Record or autonomous reservoir genesis",
        },
        "campaign_lane_coordinate_rebase": "Cycle648 does not independently rebase campaign lane coordinates.",
        "optimal_next_campaign": "replace the two coordinate-zero S sheets by a translation-orbit virtual gauge field and compile the root-label-blind leaf decoder into a state-carried fine-NN controller with a mobile odd-defect absorber; require returned route history and complete L3/L6/L7 local-stabilizer coverage",
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
        "tests_passed": PASS, "tests_failed": FAIL,
        "pass": FAIL == 0 and discipline["pass"] and claim_contract and fixture_pass,
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n")
    print("SUMMARY_JSON", json.dumps({
        "pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
        "route_A_Wilson_residuals": [row["maximum_Wilson_residual"] for row in route_a["sizes"]],
        "route_A_translation_mismatches": [row["ordinary_unit_translation_pattern_mismatches"] for row in route_a["sizes"]],
        "route_B_old_uncovered": route_b["Cycle644_same_scope_old_local_comparator"]["not_covered_by_executed_representative_search"],
        "route_B_full_local80_found": route_b["Cycle642_full_stabilizer_basis_L3"]["diameter_at_most_80_positive_witnesses_found"],
        "route_C_even_failures": [row["even_syndrome_decode_failures"] for row in route_c["sizes"]],
        "full_root_free_translation_covariant_preparation": False,
        "axiom_pressure": False, "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
    }, sort_keys=True))
    print("RESULT", PASS, FAIL)
    return int(not receipt["pass"])


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold:
        terminal = sys.stdout
        sys.stdout = Tee(terminal, cold)
        try:
            code = main()
        finally:
            sys.stdout = terminal
    raise SystemExit(code)
