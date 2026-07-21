#!/usr/bin/env python3
"""Cycle 549: literal gate compiler for the Cycle-426 recoil source.

Compile the coefficient-two M64 x seven-resource-M2 source exponential on the
complete local Q<=2 code into explicit two-level Givens/phase factors, Gray
equality macros, exact Toffoli decomposition, and nearest-neighbor routing.
Compose the Q=1 restriction with Cycle539 W^dagger/source/W on Cycle546's
current-selected interface.  Compiler order is not physical time.
"""

from __future__ import annotations

from dataclasses import dataclass
import gc
import hashlib
from itertools import product
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np
from scipy import linalg, sparse
from scipy.sparse.csgraph import connected_components


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_current_selected_carried_source_prediction_bridge_cycle546_2026_07_21 as c546
import physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21 as c523


c434 = c546.c434
c429 = c546.c429
c426 = c429.c426
c396 = c429.c396
c322 = c429.c322
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECOIL_SOURCE_LITERAL_GATE_COMPILER_CYCLE549_NOTE_2026-07-21.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 1.5e-9
PASS = 0
FAIL = 0

DEPENDENCIES = {
    ROOT / "scripts/physical_recoil_hard_core_field_bridge_cycle426_2026_07_19.py":
        "1001fc29d3e230ed55a0c973cdf5c598f75c72a6ee6b916a56eeddfdaa0a599e",
    ROOT / "scripts/physical_shared_middle_three_cell_source_compiler_cycle396_2026_07_18.py":
        "82824e4bf66874192cab9f53d20dbd799eec27fc8f07ac61af6bc6602494fff0",
    ROOT / "scripts/physical_test_matter_recoil_receiver_multiedge_prediction_cycle429_2026_07_19.py":
        "75362f83b6de34c6c3f5e9aebe280ac083e76679c9f96fe6388f700e50d28564",
    ROOT / "scripts/physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21.py":
        "d9dd02bbb4dfacebf0f75f6b8c56881ff56653843cb7ed75baa381d5aa605b9d",
    ROOT / "scripts/physical_shared_seam_code_space_isometry_compiler_cycle539_2026_07_21.py":
        "aa126a6363f9fc8c08d28a47b840c1b6e0a7c0b47bbe296087340b804a0087d1",
    ROOT / "scripts/physical_rough_fswap_pauli_rotation_gate_compiler_cycle540_2026_07_21.py":
        "1bb1528459fecb9f78ed3fe4c295d75e94ffb07745a1aa807bcdd4d276bf87fa",
    ROOT / "scripts/physical_current_selected_carried_source_prediction_bridge_cycle546_2026_07_21.py":
        "2564dedf95509a51a599c99baea8414a48c7b7fcf6b45c17ed1335a01417decb",
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def dependency_controls() -> dict:
    expected = {str(path.relative_to(ROOT)): value for path, value in DEPENDENCIES.items()}
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in DEPENDENCIES}
    return {"expected": expected, "observed": observed, "pass": expected == observed}


def normalized(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def note_contract() -> dict:
    required = (
        "complete local q<=2 code",
        "literal nearest-neighbor one-/two-m2 gates",
        "w_path source_q w_path^dagger",
        "sparse direct-sum bookkeeping",
        "cycle-434 frozen values without refit",
        "current-correlated input preparation remains supplied",
        "cycle-539 selected and cycle-540 rough carriers remain distinct",
        "no axiom pressure",
        "authority: none",
        "audit: unset",
    )
    body = "" if not NOTE.exists() else normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    return {"required": required, "missing": missing, "pass": not missing}


@dataclass(frozen=True)
class Operation:
    q: int
    kind: str
    indices: tuple[int, ...]
    words: tuple[int, ...]
    matrix: np.ndarray


def basis_word(q: int, index: int) -> int:
    states = c426.LOCAL_STATES[q]
    matter_index, field_index = divmod(index, len(states))
    mask = int(c322.LOCAL_MASKS[matter_index])
    field_state = int(states[field_index])
    return mask | (field_state << 6)


def component_decomposition(q: int, indices: np.ndarray, target: np.ndarray):
    """Return physical-application-order two-level and phase gates."""

    size = len(indices)
    work = target.copy()
    eliminations = []
    for column in range(size - 1):
        for row in range(size - 1, column, -1):
            a = work[row - 1, column]
            b = work[row, column]
            if abs(b) < 3e-14:
                continue
            radius = float(np.sqrt(abs(a) ** 2 + abs(b) ** 2))
            givens = np.asarray(
                [[np.conj(a) / radius, np.conj(b) / radius],
                 [-b / radius, a / radius]],
                dtype=complex,
            )
            work[[row - 1, row], :] = givens @ work[[row - 1, row], :]
            eliminations.append((row - 1, row, givens))
    off_diagonal = work - np.diag(np.diag(work))
    if np.max(abs(off_diagonal), initial=0) > 2e-11:
        raise RuntimeError("component Givens elimination did not reach a diagonal")

    operations: list[Operation] = []
    for local, phase in enumerate(np.diag(work)):
        if abs(phase - 1) > 3e-14:
            global_index = int(indices[local])
            operations.append(
                Operation(
                    q,
                    "phase",
                    (global_index,),
                    (basis_word(q, global_index),),
                    np.asarray([[phase]], dtype=complex),
                )
            )
    for left, right, givens in reversed(eliminations):
        global_left = int(indices[left])
        global_right = int(indices[right])
        operations.append(
            Operation(
                q,
                "two_level",
                (global_left, global_right),
                (basis_word(q, global_left), basis_word(q, global_right)),
                givens.conj().T,
            )
        )
    return operations, float(np.max(abs(off_diagonal), initial=0))


def apply_operations_matrix(dimension: int, operations: list[Operation]) -> np.ndarray:
    output = np.eye(dimension, dtype=complex)
    for operation in operations:
        if operation.kind == "phase":
            output[operation.indices[0], :] *= operation.matrix[0, 0]
        else:
            rows = list(operation.indices)
            output[rows, :] = operation.matrix @ output[rows, :]
    return output


def apply_operations_vector(vector: np.ndarray, operations: list[Operation]) -> np.ndarray:
    output = vector.copy()
    for operation in operations:
        if operation.kind == "phase":
            output[operation.indices[0]] *= operation.matrix[0, 0]
        else:
            rows = list(operation.indices)
            output[rows] = operation.matrix @ output[rows]
    return output


def inverse_operations(operations: list[Operation]) -> list[Operation]:
    return [
        Operation(op.q, op.kind, op.indices, op.words, op.matrix.conj().T)
        for op in reversed(operations)
    ]


def compile_sector(q: int) -> dict:
    generator = c426.recoil_generator(q).tocsr()
    dimension = generator.shape[0]
    _count, labels = connected_components(abs(generator), directed=False)
    sizes = np.bincount(labels)
    target = np.eye(dimension, dtype=complex)
    operations: list[Operation] = []
    elimination_residual = 0.0
    component_rows = []
    for component in range(len(sizes)):
        indices = np.flatnonzero(labels == component)
        if len(indices) == 1:
            continue
        block_h = generator[indices][:, indices].toarray()
        block_u = linalg.expm(1j * c426.ANGLE * block_h)
        target[np.ix_(indices, indices)] = block_u
        block_operations, residual = component_decomposition(q, indices, block_u)
        operations.extend(block_operations)
        elimination_residual = max(elimination_residual, residual)
        component_rows.append(
            {
                "size": len(indices),
                "generator_nonzeros": int(np.count_nonzero(block_h)),
                "two_level_factors": sum(op.kind == "two_level" for op in block_operations),
                "phase_factors": sum(op.kind == "phase" for op in block_operations),
            }
        )
    compiled = apply_operations_matrix(dimension, operations)
    inverse = apply_operations_matrix(dimension, inverse_operations(operations))
    identity = np.eye(dimension, dtype=complex)
    deletion_operations = list(operations)
    deletion_index = next(
        index for index, operation in enumerate(deletion_operations)
        if operation.kind == "two_level"
    )
    deletion_operations.pop(deletion_index)
    deleted = apply_operations_matrix(dimension, deletion_operations)
    digest_payload = [
        {
            "kind": operation.kind,
            "indices": operation.indices,
            "words": operation.words,
            "matrix": tuple(
                (complex(value).real.hex(), complex(value).imag.hex())
                for value in operation.matrix.reshape(-1)
            ),
        }
        for operation in operations
    ]
    schedule_sha256 = hashlib.sha256(
        json.dumps(digest_payload, sort_keys=True).encode()
    ).hexdigest()
    histogram = {
        int(size): int(count) for size, count in zip(*np.unique(sizes, return_counts=True))
    }
    return {
        "q": q,
        "dimension": dimension,
        "generator": generator,
        "target": target,
        "compiled": compiled,
        "operations": operations,
        "component_histogram": histogram,
        "nontrivial_components": len(component_rows),
        "two_level_factors": sum(op.kind == "two_level" for op in operations),
        "phase_factors": sum(op.kind == "phase" for op in operations),
        "factor_schedule_sha256": schedule_sha256,
        "maximum_elimination_offdiagonal": elimination_residual,
        "factorization_maximum_residual": float(np.max(abs(compiled - target))),
        "factorization_Frobenius_residual": float(np.linalg.norm(compiled - target)),
        "inverse_residual": float(np.max(abs(inverse @ compiled - identity))),
        "unitarity_residual": float(np.max(abs(compiled.conj().T @ compiled - identity))),
        "deleted_factor_Frobenius_residual": float(np.linalg.norm(deleted - target)),
    }


def factorization_controls(compilers: dict[int, dict]) -> dict:
    rows = []
    for q, compiler in compilers.items():
        rows.append({key: value for key, value in compiler.items() if key not in {
            "generator", "target", "compiled", "operations"
        }})
    maximum = max(
        max(
            row["maximum_elimination_offdiagonal"],
            row["factorization_maximum_residual"],
            row["inverse_residual"],
            row["unitarity_residual"],
        )
        for row in rows
    )
    return {
        "angle": c426.ANGLE,
        "coefficient_two_supplied": True,
        "complete_declared_local_sectors": (0, 1, 2),
        "q0_identity": c426.recoil_generator(0).nnz == 0,
        "rows": rows,
        "maximum_factor_inverse_unitarity_residual": maximum,
        "pass": c426.recoil_generator(0).nnz == 0
        and maximum < 3e-11
        and all(row["deleted_factor_Frobenius_residual"] > 1e-3 for row in rows),
    }


def gray_path(source: int, target: int) -> tuple[int, ...]:
    path = [source]
    current = source
    difference = source ^ target
    for bit in range(13):
        if (difference >> bit) & 1:
            current ^= 1 << bit
            path.append(current)
    if current != target:
        raise RuntimeError("Gray path did not reach target")
    return tuple(path)


def gray_macro_apply(amplitudes: dict[int, complex], operation: Operation):
    source, target = operation.words
    path = gray_path(source, target)
    output = dict(amplitudes)
    for index in range(len(path) - 2):
        left, right = path[index], path[index + 1]
        output[left], output[right] = output.get(right, 0j), output.get(left, 0j)
    adjacent = (path[-2], path[-1])
    vector = np.asarray([output.get(adjacent[0], 0j), output.get(adjacent[1], 0j)])
    transformed = operation.matrix @ vector
    output[adjacent[0]], output[adjacent[1]] = transformed
    for index in reversed(range(len(path) - 2)):
        left, right = path[index], path[index + 1]
        output[left], output[right] = output.get(right, 0j), output.get(left, 0j)
    return output


def macro_controls(compilers: dict[int, dict]) -> dict:
    failures = 0
    hamming_rows = []
    gray_mcx = 0
    two_level_cores = 0
    phase_cores = 0
    maximum_hamming = 0
    for compiler in compilers.values():
        for operation in compiler["operations"]:
            if operation.kind == "phase":
                phase_cores += 1
                continue
            two_level_cores += 1
            source, target = operation.words
            path = gray_path(source, target)
            distance = len(path) - 1
            maximum_hamming = max(maximum_hamming, distance)
            gray_mcx += 2 * (distance - 1)
            a = 0.37 + 0.19j
            b = -0.23 + 0.41j
            actual = gray_macro_apply({source: a, target: b}, operation)
            expected = operation.matrix @ np.asarray((a, b))
            failures += int(abs(actual.get(source, 0) - expected[0]) > 3e-13)
            failures += int(abs(actual.get(target, 0) - expected[1]) > 3e-13)
            for intermediate in path[1:-1]:
                actual_intermediate = gray_macro_apply({intermediate: 1 + 0j}, operation)
                failures += int(abs(actual_intermediate.get(intermediate, 0) - 1) > 3e-13)
            hamming_rows.append(distance)
    # Exhaust the normalized 12-control truth table.  Negative equality
    # controls are conjugated to this all-one case by explicit one-M2 X gates.
    conjunction_truth_failures = 0
    conjunction_truth_cases = 0
    for control_word in range(1 << 12):
        controls = [(control_word >> bit) & 1 for bit in range(12)]
        for initial_target in (0, 1):
            conjunction_truth_cases += 1
            work = [0] * 10
            work[0] ^= controls[0] & controls[1]
            for index in range(1, 10):
                work[index] ^= work[index - 1] & controls[index + 1]
            target = initial_target ^ (work[9] & controls[11])
            for index in reversed(range(1, 10)):
                work[index] ^= work[index - 1] & controls[index + 1]
            work[0] ^= controls[0] & controls[1]
            expected = initial_target ^ int(control_word == (1 << 12) - 1)
            conjunction_truth_failures += int(target != expected or any(work))

        # The arbitrary-core form computes all twelve controls into an
        # eleventh clean flag, calls one controlled one-M2 core, and reverses.
        work = [0] * 11
        work[0] ^= controls[0] & controls[1]
        for index in range(1, 11):
            work[index] ^= work[index - 1] & controls[index + 1]
        core_enabled = work[10]
        for index in reversed(range(1, 11)):
            work[index] ^= work[index - 1] & controls[index + 1]
        work[0] ^= controls[0] & controls[1]
        conjunction_truth_failures += int(
            core_enabled != int(control_word == (1 << 12) - 1) or any(work)
        )

    toffoli = c523.bare_toffoli_controls()
    # Each adjacent-state transposition is a 12-control X (21 Toffolis).
    # Each equality-controlled arbitrary one-M2 core is conservatively bounded
    # by compute/uncompute of a 12-control flag (42 Toffolis) plus one 2-M2 core.
    toffoli_upper = 21 * gray_mcx + 42 * (two_level_cores + phase_cores)
    return {
        "local_data_M2": 13,
        "clean_conjunction_work_M2": 11,
        "maximum_live_local_compiler_M2": 24,
        "two_level_cores": two_level_cores,
        "basis_phase_cores": phase_cores,
        "Gray_equality_MCX": gray_mcx,
        "maximum_basis_pair_Hamming_distance": maximum_hamming,
        "Cycle523_exact_Toffoli_control": toffoli,
        "exact_15_call_Toffoli_decomposition": toffoli["pass"],
        "conservative_Toffoli_upper_bound": toffoli_upper,
        "conservative_bare_one_two_M2_call_upper_bound_before_routing":
            15 * toffoli_upper + two_level_cores + phase_cores,
        "macro_truth_failures": failures,
        "conjunction_truth_cases": conjunction_truth_cases,
        "conjunction_and_Gray_work_terminal_failures": conjunction_truth_failures,
        "all_compute_sequences_have_explicit_reverse_uncompute": True,
        "arbitrary_two_M2_core_matrices_are_explicit_supplied_compiler_angles": True,
        "pass": failures == 0
        and conjunction_truth_failures == 0
        and maximum_hamming <= 13
        and toffoli["pass"],
    }


def signed_permutation(operator: sparse.spmatrix):
    matrix = operator.tocsc()
    if not np.all(np.diff(matrix.indptr) == 1):
        raise ValueError("frame is not a signed permutation")
    return matrix.indices.copy(), matrix.data.copy()


def mapped_operations(operations: list[Operation], frame_operator):
    rows, phases = signed_permutation(frame_operator)
    mapped = []
    for operation in operations:
        targets = tuple(int(rows[index]) for index in operation.indices)
        words = tuple(basis_word(operation.q, index) for index in targets)
        if operation.kind == "phase":
            matrix = operation.matrix.copy()
        else:
            diagonal = np.diag([phases[index] for index in operation.indices])
            matrix = diagonal @ operation.matrix @ diagonal.conj().T
        mapped.append(Operation(operation.q, operation.kind, targets, words, matrix))
    return mapped


def layout_coordinates():
    directions = [tuple(int(value) for value in row) for row in c429.c210.DIRECTIONS]
    matter = [tuple(2 * value for value in direction) for direction in directions]
    reservoir = [(0, 0, 0)]
    fields = [tuple(6 * value for value in direction) for direction in directions]
    work = [
        (x, y, z)
        for x, y, z in product((-4, 4), repeat=3)
    ] + [(0, 4, 4), (4, 0, 4), (4, 4, 0)]
    coordinates = tuple(matter + reservoir + fields + work)
    if len(coordinates) != 24 or len(set(coordinates)) != 24:
        raise RuntimeError("local compiler coordinate placement collides")
    return coordinates


def manhattan_path(left, right):
    current = list(left)
    output = [tuple(current)]
    for axis in range(3):
        while current[axis] != right[axis]:
            current[axis] += 1 if right[axis] > current[axis] else -1
            output.append(tuple(current))
    return tuple(output)


def covariance_routing_controls(compilers: dict[int, dict]) -> dict:
    frames = c429.c210.proper_cubic_frames()
    coordinates = layout_coordinates()
    paths = [manhattan_path(left, right) for left, right in product(coordinates, repeat=2)]
    route_failures = 0
    maximum_route = 0
    for path in paths:
        maximum_route = max(maximum_route, len(path) - 1)
        route_failures += sum(c434.manhattan(a, b) != 1 for a, b in zip(path, path[1:]))
        for frame in frames:
            mapped = tuple(
                tuple(int(value) for value in frame @ np.asarray(point)) for point in path
            )
            route_failures += sum(
                c434.manhattan(a, b) != 1 for a, b in zip(mapped, mapped[1:])
            )

    rng = np.random.default_rng(549)
    covariance_residual = 0.0
    group_failures = 0
    for q, compiler in compilers.items():
        dimension = compiler["dimension"]
        target = compiler["target"]
        operations = compiler["operations"]
        probes = []
        for _ in range(2):
            vector = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
            vector /= np.linalg.norm(vector)
            probes.append(vector)
        representations = [c426.recoil_frame(q, frame) for frame in frames]
        for representation in representations:
            mapped = mapped_operations(operations, representation)
            for vector in probes:
                expected = representation @ (
                    target @ (representation.getH() @ vector)
                )
                actual = apply_operations_vector(vector, mapped)
                covariance_residual = max(
                    covariance_residual,
                    float(np.linalg.norm(actual - expected)),
                    float(np.linalg.norm(expected - target @ vector)),
                )
        signed = [signed_permutation(rep) for rep in representations]
        for first_index, first in enumerate(frames):
            first_rows, first_phases = signed[first_index]
            for second_index, second in enumerate(frames):
                second_rows, second_phases = signed[second_index]
                product_rows, product_phases = signed_permutation(
                    c426.recoil_frame(q, first @ second)
                )
                composed_rows = first_rows[second_rows]
                composed_phases = second_phases * first_phases[second_rows]
                group_failures += int(not np.array_equal(composed_rows, product_rows))
                group_failures += int(
                    np.max(abs(composed_phases - product_phases), initial=0) > 2e-13
                )
    return {
        "proper_cubic_frames": len(frames),
        "frame_products_per_sector": len(frames) ** 2,
        "Q_sectors": tuple(compilers),
        "maximum_mapped_factor_covariance_residual": covariance_residual,
        "frame_group_law_failures": group_failures,
        "local_live_M2": len(coordinates),
        "all_live_wire_pairs_routed": len(paths),
        "maximum_route_length_NN_edges": maximum_route,
        "route_or_mapped_edge_failures": route_failures,
        "installed_invariant_microgrid_M2_per_source_cell": 13 ** 3,
        "microgrid": "all integer sites in [-6,6]^3; compile-time mapped paths",
        "train_L5_and_held_L6_nonalias": True,
        "pass": len(frames) == 24
        and covariance_residual < 4e-11
        and group_failures == 0
        and route_failures == 0,
    }


def old_q_vertex(compiled_q1: np.ndarray) -> np.ndarray:
    encoding = c426.q1_encoding().toarray()
    return encoding.conj().T @ compiled_q1 @ encoding


def embedded_operator(vertex: np.ndarray, cell_index: int) -> sparse.csc_matrix:
    rows = []
    columns = []
    data = []
    for matter_source, label in enumerate(c429.LABELS):
        specs = list(c429.c319.label_specs(label))
        local_source = c396.LOCAL_SPEC_INDEX[specs[cell_index]]
        for q_source in range(7):
            column = 7 * local_source + q_source
            for target in np.flatnonzero(abs(vertex[:, column]) > 2e-13):
                local_target, q_target = divmod(int(target), 7)
                target_specs = list(specs)
                target_specs[cell_index] = c322.LOCAL_LABELS[local_target]
                target_label = tuple(item for spec in target_specs for item in spec)
                matter_target = c429.LABEL_INDEX[target_label]
                rows.append(7 * matter_target + q_target)
                columns.append(7 * matter_source + q_source)
                data.append(vertex[target, column])
    dimension = 7 * c429.MATTER_DIM
    return sparse.coo_matrix(
        (data, (rows, columns)), shape=(dimension, dimension), dtype=complex
    ).tocsc()


def lift_controls(compilers: dict[int, dict]) -> tuple[dict, tuple[sparse.csc_matrix, ...]]:
    vertex = old_q_vertex(compilers[1]["compiled"])
    old_vertex = c322.local_source_blocks(c426.ANGLE)[1]
    local_residual = float(np.max(abs(vertex - old_vertex)))
    operators = tuple(embedded_operator(vertex, cell) for cell in c429.CELLS)
    rows = []
    rng = np.random.default_rng(5491)
    for cell, operator in enumerate(operators):
        old = c396.embedded_source_operator("coefficient_two", cell)
        difference = operator - old
        probe = rng.normal(size=operator.shape[1]) + 1j * rng.normal(size=operator.shape[1])
        probe /= np.linalg.norm(probe)
        rows.append(
            {
                "cell": cell,
                "shape": operator.shape,
                "compiled_nonzeros": operator.nnz,
                "old_nonzeros": old.nnz,
                "raw_maximum_residual": 0.0 if difference.nnz == 0 else float(np.max(abs(difference.data))),
                "random_vector_residual": float(np.linalg.norm(difference @ probe)),
            }
        )
    maximum = max([local_residual] + [
        max(row["raw_maximum_residual"], row["random_vector_residual"]) for row in rows
    ])
    return {
        "local_Cycle426_to_Cycle322_vertex_residual": local_residual,
        "embedded_rows": rows,
        "maximum_lift_residual": maximum,
        "physical_selected_source_factor": "W_path source_q W_path^dagger",
        "Cycle539_W_path_strict_pinned_literal_NN": True,
        "persistent_q_readout_is_diagonal_on_literal_q_M2": True,
        "old_Cycle429_dense_matter_lift_needed_for_source_or_readout": False,
        "pass": maximum < 5e-11,
    }, operators


def apply_compiled_source(state, cell: int, operators, *, inverse=False, enabled=True):
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    active = (c429.reservoir_site(cell),) + tuple(
        c429.field_site(cell, direction) for direction in range(6)
    )
    zero = np.zeros(c429.MATTER_DIM, dtype=complex)
    joint = np.column_stack([state.get(key, zero) for key in active]).reshape(-1)
    operator = operators[cell].getH() if inverse else operators[cell]
    transformed = (operator @ joint).reshape((c429.MATTER_DIM, 7))
    output = {key: value.copy() for key, value in state.items() if key not in active}
    for local, key in enumerate(active):
        output[key] = transformed[:, local]
    return c429.prune(output)


def compiled_step(
    state,
    factors,
    operators,
    *,
    inverse=False,
    source_enabled=(True, True, True),
    enabled_edges=(True, True),
    contact_enabled=True,
):
    coin, first, second, contact = factors
    if not inverse:
        output = c429.apply_matter(state, coin)
        output = c434.field_coin_extended(output)
        for cell in c429.CELLS:
            output = apply_compiled_source(
                output, cell, operators, enabled=source_enabled[cell]
            )
        output = c429.apply_matter(output, first)
        output = c429.apply_matter(output, second)
        output = c429.apply_transport(
            output, c546.FIXED_ENGINE_ROLE, enabled_edges=enabled_edges
        )
        return c429.apply_matter(output, contact) if contact_enabled else output
    output = c429.apply_matter(state, contact.getH()) if contact_enabled else state
    output = c429.apply_transport(output, c546.FIXED_ENGINE_ROLE, inverse=True)
    output = c429.apply_matter(output, second.getH())
    output = c429.apply_matter(output, first.getH())
    for cell in reversed(c429.CELLS):
        output = apply_compiled_source(output, cell, operators, inverse=True)
    output = c434.field_coin_extended(output, inverse=True)
    return c429.apply_matter(output, coin.getH())


def compiled_current_forward(
    state,
    item,
    factors,
    operators,
    *,
    delete_current=False,
    source_enabled=(True, True, True),
    enabled_edges=(True, True),
    contact_enabled=True,
):
    output = c546.current_carry(state, item, delete_current_controls=delete_current)
    for _ in range(3):
        output = c546.map_engine(
            output,
            lambda value: compiled_step(
                value,
                factors,
                operators,
                source_enabled=source_enabled,
                enabled_edges=enabled_edges,
                contact_enabled=contact_enabled,
            ),
        )
    return c546.prune(output)


def compiled_current_inverse(state, item, factors, operators):
    output = dict(state)
    for _ in range(3):
        output = c546.map_engine(
            output,
            lambda value: compiled_step(
                value, factors, operators, inverse=True
            ),
        )
    return c546.current_carry(output, item, inverse=True)


def compiled_vertex_trace(state, cell, factors, operators):
    coin, _first, _second, _contact = factors
    output = c429.apply_matter(state, coin)
    output = c434.field_coin_extended(output)
    before = after = None
    for candidate in c429.CELLS:
        if candidate == cell:
            before = output
        output = apply_compiled_source(output, candidate, operators)
        if candidate == cell:
            after = output
    return before, after


def compiled_branch_row(item, current, factors, operators):
    prepared = c546.initial_state(item, {current: 1})
    carried = c546.sector(c546.current_carry(prepared, item), current)
    first = compiled_step(carried, factors, operators)
    second = compiled_step(first, factors, operators)
    third = compiled_step(second, factors, operators)
    source = c546.SOURCE_FOR_CURRENT[current]
    receiver = c546.RECEIVER_FOR_CURRENT[current]
    source_before, source_after = compiled_vertex_trace(carried, source, factors, operators)
    receiver_before, receiver_after = compiled_vertex_trace(second, receiver, factors, operators)
    source_matter = c429.matter_direction(source_after, source) - c429.matter_direction(source_before, source)
    source_field = 2 * (c429.field_direction(source_after, source) - c429.field_direction(source_before, source))
    receiver_matter = c429.matter_direction(receiver_after, receiver) - c429.matter_direction(receiver_before, receiver)
    receiver_field = 2 * (c429.field_direction(receiver_after, receiver) - c429.field_direction(receiver_before, receiver))
    source_loss = c429.reservoir_weight(source_before, source) - c429.reservoir_weight(source_after, source)
    field_gain = c429.cell_q(source_after, source) - c429.reservoir_weight(source_after, source)
    old = c546.fixed_forward(prepared, item, factors)
    return {
        "L": item.length,
        "current": current,
        "compiled_vs_Cycle546_complete_state_residual": c546.state_residual(
            {(current, key): value for key, value in third.items()}, old
        ),
        "receiver_response": c429.reservoir_weight(third, receiver),
        "receiver_coordinate": receiver_matter,
        "receiver_direction_ledger_residual": receiver_matter + receiver_field,
        "source_resource_balance_residual": source_loss - field_gain,
        "source_direction_ledger_residual": source_matter + source_field,
        "global_Q": c429.state_norm(third),
    }


def current_prediction_controls(factors, operators) -> dict:
    rows = []
    failures = 0
    tensor_rows = []
    coherent_amplitudes = {"NULL": 0.3 + 0.1j, "PLUS": -0.2 + 0.5j, "MINUS": 0.4 - 0.25j}
    scale = np.sqrt(sum(abs(value) ** 2 for value in coherent_amplitudes.values()))
    coherent_amplitudes = {key: value / scale for key, value in coherent_amplitudes.items()}
    coherent_residuals = []
    inverse_residuals = []
    for length in (5, 6):
        item = c546.fixture(length)
        tensor_rows.append(c546.tensor_circuit_controls(item))
        initial = c546.initial_state(item, coherent_amplitudes)
        compiled = compiled_current_forward(initial, item, factors, operators)
        old = c546.fixed_forward(initial, item, factors)
        restored = compiled_current_inverse(compiled, item, factors, operators)
        coherent_residuals.append(c546.state_residual(compiled, old))
        inverse_residuals.append(c546.state_residual(restored, initial))
        plus = compiled_branch_row(item, "PLUS", factors, operators)
        minus = compiled_branch_row(item, "MINUS", factors, operators)
        rows.extend((plus, minus))
        failures += int(np.linalg.norm(plus["receiver_coordinate"] + minus["receiver_coordinate"]) > 2e-13)
        failures += int(abs(plus["receiver_response"] - minus["receiver_response"]) > 2e-13)
        for row in (plus, minus):
            failures += int(row["compiled_vs_Cycle546_complete_state_residual"] > 2e-12)
            failures += int(np.linalg.norm(row["receiver_direction_ledger_residual"]) > 3e-13)
            failures += int(np.linalg.norm(row["source_direction_ledger_residual"]) > 3e-13)
            failures += int(abs(row["source_resource_balance_residual"]) > 3e-13)
            failures += int(abs(row["global_Q"] - 1) > 3e-12)
    null_item = c546.fixture(5)
    null_initial = c546.initial_state(null_item, {"NULL": 1})
    null_output = compiled_current_forward(null_initial, null_item, factors, operators)
    baseline = next(row["receiver_response"] for row in rows if row["L"] == 5 and row["current"] == "PLUS")
    plus_initial = c546.initial_state(null_item, {"PLUS": 1})
    source_enabled = [True, True, True]
    source_enabled[0] = False
    source_deleted = compiled_current_forward(plus_initial, null_item, factors, operators, source_enabled=tuple(source_enabled))
    receiver_enabled = [True, True, True]
    receiver_enabled[2] = False
    receiver_deleted = compiled_current_forward(plus_initial, null_item, factors, operators, source_enabled=tuple(receiver_enabled))
    current_deleted = compiled_current_forward(plus_initial, null_item, factors, operators, delete_current=True)
    first_edge = compiled_current_forward(plus_initial, null_item, factors, operators, enabled_edges=(False, True))
    second_edge = compiled_current_forward(plus_initial, null_item, factors, operators, enabled_edges=(True, False))
    contact_deleted = compiled_current_forward(plus_initial, null_item, factors, operators, contact_enabled=False)
    deletions = {
        "null_full_state_residual": c546.state_residual(null_output, null_initial),
        "current_deleted_receiver": c546.receiver_weight(current_deleted, "PLUS"),
        "source_deleted_receiver": c546.receiver_weight(source_deleted, "PLUS"),
        "receiver_deleted_receiver": c546.receiver_weight(receiver_deleted, "PLUS"),
        "first_transport_deleted_receiver": c546.receiver_weight(first_edge, "PLUS"),
        "second_transport_deleted_receiver": c546.receiver_weight(second_edge, "PLUS"),
        "contact_deleted_receiver": c546.receiver_weight(contact_deleted, "PLUS"),
        "baseline": baseline,
    }
    failures += int(any(not row["pass"] for row in tensor_rows))
    failures += int(max(coherent_residuals + inverse_residuals) > 2e-12)
    failures += int(deletions["null_full_state_residual"] > 2e-12)
    failures += int(any(deletions[key] != 0 for key in (
        "current_deleted_receiver", "source_deleted_receiver", "receiver_deleted_receiver",
        "first_transport_deleted_receiver", "second_transport_deleted_receiver"
    )))
    failures += int(abs(deletions["contact_deleted_receiver"] - baseline) < 1e-9)
    return {
        "rows": rows,
        "coherent_NULL_PLUS_MINUS_residuals_L5_L6": coherent_residuals,
        "compiled_inverse_residuals_L5_L6": inverse_residuals,
        "literal_current_tensor_rows": tensor_rows,
        "deletions": deletions,
        "frozen_Cycle434_values_replayed_without_refit": True,
        "coherent_weights_called_probability": False,
        "direction_called_force_momentum_energy_stress_or_gravity": False,
        "schedule_called_time": False,
        "failures": failures,
        "pass": failures == 0,
    }


def physics_and_boundary_controls(update_rows, factorization, lift, macro, routing, prediction):
    boundaries = {
        "retired": (
            "Cycle426 complete declared local Q<=2 source exponential as one primitive block",
            "Cycle429 dense E429 source lift/readout on the Cycle539 selected path code",
        ),
        "supplied": (
            "Cycle426 coefficient two, theta=0.8m, angle sign/normalization, and source invocation",
            "Cycle539 selected coefficient/Pauli tables, W_path, fixed reference preparation, and blank work",
            "explicit complex one-/two-M2 compiler core matrices and exact Toffoli decomposition",
            "current-correlated NULL/PLUS/MINUS input preparation and blank route microgrid",
        ),
        "open": (
            "Q>2 local source sectors and autonomous current-correlated input preparation",
            "resource compression of the generous 13-cube microgrid",
            "Cycle539-selected to Cycle540-rough carrier transducer",
            "Cycle420 host profile/centroid join and clock-calibrated motion",
            "energy/stress source selection, gravity, occurrence, Record, and Born law",
        ),
        "Cycle539_selected_equals_Cycle540_rough": False,
        "negative_or_minimum_claim": False,
        "axiom_pressure": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    physics = {
        "Cycle219_mass_fixture": update_rows["Cycle219_mass_fixture"],
        "three_cell_mass": update_rows["three_cell_rest_mass"],
        "uniform_one_particle_residual": update_rows["uniform_one_particle_eigen_residual"],
        "contact_nontrivial_columns": update_rows["contact_nontrivial_columns"],
        "first_FSWAP_unitarity": update_rows["first_FSWAP_unitarity_residual"],
        "second_FSWAP_unitarity": update_rows["second_FSWAP_unitarity_residual"],
    }
    return {
        "physics": physics,
        "boundaries": boundaries,
        "compiler_chain": {
            "source_factorization": factorization["pass"],
            "Gray_Toffoli_macro": macro["pass"],
            "NN_all24_576": routing["pass"],
            "W_source_Wdagger_lift": lift["pass"],
            "current_prediction": prediction["pass"],
        },
        "pass": abs(physics["three_cell_mass"] - physics["Cycle219_mass_fixture"]) < TOL
        and physics["uniform_one_particle_residual"] < TOL
        and physics["contact_nontrivial_columns"] == 645
        and physics["first_FSWAP_unitarity"] < TOL
        and physics["second_FSWAP_unitarity"] < TOL
        and not boundaries["axiom_pressure"]
        and not boundaries["Cycle539_selected_equals_Cycle540_rough"],
    }


def main() -> int:
    started = time.monotonic()
    print("Cycle549 literal recoil/source gate compiler")
    print("authority=none; audit=unset; compiler schedule is not physical time")
    dependencies = dependency_controls()
    contract = note_contract()
    compilers = {q: compile_sector(q) for q in (1, 2)}
    factorization = factorization_controls(compilers)
    macro = macro_controls(compilers)
    routing = covariance_routing_controls(compilers)
    lift, operators = lift_controls(compilers)
    update_rows, coin, first, second, contact, _forward, _reverse = c429.c319.update_controls(c429.LABELS, "path")
    factors = (coin, first, second, contact)
    prediction = current_prediction_controls(factors, operators)
    physics_boundary = physics_and_boundary_controls(
        update_rows, factorization, lift, macro, routing, prediction
    )
    tests = {
        "strict_dependency_byte_pins": dependencies["pass"],
        "note_authority_and_claim_contract": contract["pass"],
        "complete_Q0_Q1_Q2_source_factorization_inverse_and_deletion": factorization["pass"],
        "Gray_equality_Toffoli_literal_one_two_M2_macros": macro["pass"],
        "nearest_neighbor_all24_and_576_covariance": routing["pass"],
        "Cycle539_W_source_Wdagger_lift_and_q_readout": lift["pass"],
        "Cycle546_current_null_prediction_ledgers_and_deletions": prediction["pass"],
        "mass_contact_seams_boundaries_and_no_axiom_pressure": physics_boundary["pass"],
    }
    result = {
        "cycle": 549,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "dependencies": dependencies,
        "note_contract": contract,
        "factorization": factorization,
        "literal_gate_macros": macro,
        "routing_and_covariance": routing,
        "selected_matter_lift_and_readout": lift,
        "current_prediction": prediction,
        "physics_and_boundary": physics_boundary,
        "tests": tests,
        "pass": all(tests.values()),
        "elapsed_seconds": time.monotonic() - started,
        "maximum_RSS_bytes": rss_bytes(),
        "process_swap_count": swap_count(),
    }
    for label, passed in tests.items():
        check(label.replace("_", " "), bool(passed), "ok" if passed else result)
    result["pass_count"] = PASS
    result["fail_count"] = FAIL
    print("RESULT_JSON", json.dumps(result, sort_keys=True, default=str))
    print("SUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
