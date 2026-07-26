#!/usr/bin/env python3
"""Cycle 705: support-localization attack on the actual Cycle-269 substrate.

This runner does not substitute the Cycle-655 K7 target encoder for the
physical substrate.  It uses the Cycle-269 face graph together with the
Cycle-311 carrier/port/flag/r representatives and the Cycle-315 overlap-aware
phase reducer.  Cycle 655 supplies only the 38-factor decoded target word.

The constructive question is deliberately split in two:

* does the phase-aware common state map remain an isometry on growing patches;
* do bounded Cycle-269 even-algebra words preserve that common state map?

Dense projector completions and collision-block whitening are reported only
as target-fit diagnostics.  They are not accepted support-local compilers.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import combinations, product
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import frontier_full128_25site_nn_circuit_core_2026_07_24 as c655
import frontier_two_overlapping_maximal_star_direct_port_extractor_2026_07_25 as direct
import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18 as c330


TOL = 5.0e-10
PASS = 0
FAIL = 0
REPORT: dict[str, object] = {}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def maximum_abs(matrix) -> float:
    if sparse.issparse(matrix):
        return c315.raw_maximum_abs(matrix)
    array = np.asarray(matrix)
    return float(np.max(np.abs(array), initial=0.0))


def substrate_controls() -> dict[str, object]:
    rows = []
    for length in (3, 6):
        code = c315.c269.build_code(length)
        cells = length**3
        local_rank, local_bad = c235.phase_aware_rank(
            list(code.local_checks), code.qubits
        )
        fixed_rank, fixed_bad = c235.phase_aware_rank(
            list(code.local_checks + code.wilsons), code.qubits
        )
        fixed_plus_B_rank, fixed_plus_B_bad = c235.phase_aware_rank(
            list(code.local_checks + code.wilsons + code.B), code.qubits
        )
        triangle_count = sum(
            kind == "center_corner_edge"
            for _mask, _vertices, kind in c235.primal_edge_cycles(code.graph)
        )
        octagon_count = sum(
            kind != "center_corner_edge"
            for _mask, _vertices, kind in c235.primal_edge_cycles(code.graph)
        )
        rows.append(
            {
                "L": length,
                "cells": cells,
                "matter_vertices": len(code.graph.vertices),
                "face_M2": code.qubits,
                "internal_triangle_faces": sum(
                    kind == "internal_triangle"
                    for _u, _v, kind, _owner in code.graph.edges
                ),
                "outer_square_faces": sum(
                    kind == "outer_square"
                    for _u, _v, kind, _owner in code.graph.edges
                ),
                "triangle_checks": triangle_count,
                "octagon_checks": octagon_count,
                "local_check_count": len(code.local_checks),
                "local_check_rank": local_rank,
                "local_phase_bad": local_bad,
                "fixed_rank": fixed_rank,
                "fixed_phase_bad": fixed_bad,
                "fixed_reference_exponent": code.qubits - fixed_rank,
                "fixed_plus_B_rank": fixed_plus_B_rank,
                "fixed_plus_B_phase_bad": fixed_plus_B_bad,
                "fixed_plus_B_reference_exponent": code.qubits - fixed_plus_B_rank,
                "installed_face_port_flag_r_M2_per_cell": 15 + 6 + 1 + 1,
            }
        )
    check(
        "the actual Cycle-269 graph has six matter vertices, fifteen face M2, eleven local checks, and rank 9N-2 per cell volume",
        all(
            row["matter_vertices"] == 6 * row["cells"]
            and row["face_M2"] == 15 * row["cells"]
            and row["internal_triangle_faces"] == 12 * row["cells"]
            and row["outer_square_faces"] == 3 * row["cells"]
            and row["triangle_checks"] == 8 * row["cells"]
            and row["octagon_checks"] == 3 * row["cells"]
            and row["local_check_count"] == 11 * row["cells"]
            and row["local_check_rank"] == 9 * row["cells"] - 2
            and not row["local_phase_bad"]
            and not row["fixed_phase_bad"]
            and row["fixed_reference_exponent"] == 6 * row["cells"] - 1
            and row["fixed_plus_B_rank"] == row["face_M2"]
            and not row["fixed_plus_B_phase_bad"]
            and row["fixed_plus_B_reference_exponent"] == 0
            and row["installed_face_port_flag_r_M2_per_cell"] == 23
            for row in rows
        ),
        rows,
    )

    code = c315.c269.build_code(3)
    body = (0, 0, 0)
    encoder = c311.common_encoder(code, body)
    basis, flagged, occurrence = c311.flagged_basis_and_encoding(encoder)
    exchange = c311.exchange_matrix(encoder, occurrence)
    constrained = c311.constrained_encoding(flagged, exchange)
    constraint = c311.role_constraint(exchange)
    input_embedding = c311.fock_input_embedding()
    port_constraints = tuple(
        c311.c305.constraint_pauli(code, vertex)
        for vertex in c311.c305.body_vertices(code, body)
    )
    port_failures = sum(
        not row.commutes(stabilizer)
        for row in port_constraints
        for stabilizer in code.local_checks + code.wilsons
    )
    role = {
        "fock_input_rank": int(np.linalg.matrix_rank(constrained @ input_embedding)),
        "seam_dimension": flagged.shape[1],
        "flagged_microsectors": flagged.shape[0],
        "role_gauge_microsectors": constrained.shape[0],
        "role_constraint_involution": float(
            np.linalg.norm(constraint @ constraint - np.eye(len(constraint)))
        ),
        "role_constraint_eigen_residual": float(
            np.linalg.norm(constraint @ constrained - constrained)
        ),
        "constrained_gram_residual": float(
            np.linalg.norm(constrained.conj().T @ constrained - np.eye(127))
        ),
        "local_port_constraints": len(port_constraints),
        "port_constraint_inherited_commutator_failures": port_failures,
    }
    check(
        "the actual Cycle-311 carrier/port/flag/r shell locally enforces its six port constraints and relational role constraint",
        role["fock_input_rank"] == 64
        and role["seam_dimension"] == 127
        and role["flagged_microsectors"] == 255
        and role["role_gauge_microsectors"] == 510
        and role["role_constraint_involution"] < TOL
        and role["role_constraint_eigen_residual"] < TOL
        and role["constrained_gram_residual"] < TOL
        and role["local_port_constraints"] == 6
        and role["port_constraint_inherited_commutator_failures"] == 0,
        role,
    )

    target_counts = dict(Counter(gate.kind for gate in c655.DECODED_GATES))
    target = {
        "decoded_target_factors": len(c655.DECODED_GATES),
        "factor_counts": target_counts,
        "Cycle655_K7_physical_encoder_used": False,
    }
    check(
        "Cycle 655 contributes only its 38-factor decoded target word, never its K7 physical encoder",
        target["decoded_target_factors"] == 38
        and target_counts
        == {
            "coin_phase": 1,
            "coin_givens": 10,
            "reverse_fswap": 3,
            "seam_fswap": 9,
            "contact_phase": 15,
        }
        and not target["Cycle655_K7_physical_encoder_used"],
        target,
    )
    return {"rank_rows": rows, "role_shell": role, "target_word": target}


def patch_labels(cell_count: int) -> tuple[tuple[int, ...], ...]:
    modes = 6 * cell_count
    return (
        ((),)
        + tuple((mode,) for mode in range(modes))
        + tuple(combinations(range(modes), 2))
    )


@dataclass(frozen=True)
class PatchEncoding:
    name: str
    cells: tuple[tuple[int, int, int], ...]
    labels: tuple[tuple[int, ...], ...]
    encoding: sparse.csc_matrix
    gram: sparse.csc_matrix
    maximum_branch_support: int
    shared_rows: int
    collision_pairs: tuple[tuple[int, int, complex], ...]
    collision_labels: tuple[
        tuple[tuple[int, ...], tuple[int, ...], complex], ...
    ]


def patch_encoding(
    name: str,
    cells: tuple[tuple[int, int, int], ...],
    length: int,
    reverse_order: bool = False,
) -> PatchEncoding:
    code = c315.c269.build_code(length)
    labels = patch_labels(len(cells))
    cache = {
        (cell, number, local_label): direct.transformed_local_terms(
            code, cell, cells[cell], number, local_label
        )
        for cell in range(len(cells))
        for number, local_label in c311.FOCK_LABELS
        if number <= 2
    }
    reducer = c315.RayReducer(code)
    row_lookup: dict[tuple[int, int], int] = {}
    row_columns: dict[int, set[int]] = defaultdict(set)
    rows: list[int] = []
    columns: list[int] = []
    values: list[complex] = []
    maximum_branch_support = 0

    for column, label in enumerate(labels):
        active = sorted({mode // 6 for mode in label}, reverse=reverse_order)
        local_rows = []
        for cell in active:
            local_label = tuple(
                mode - 6 * cell for mode in label if mode // 6 == cell
            )
            local_rows.append(cache[(cell, len(local_label), local_label)])
        amplitudes: dict[int, complex] = defaultdict(complex)
        for terms in product(*local_rows) if local_rows else ((),):
            representative = c235.Pauli()
            r_mask = 0
            amplitude = 1 + 0j
            for term in terms:
                representative = representative @ term.representative
                r_mask |= term.r_x_mask
                amplitude *= term.amplitude
            base_row, phase = reducer.reduce(representative)
            row = row_lookup.setdefault((base_row, r_mask), len(row_lookup))
            amplitudes[row] += amplitude * phase
            maximum_branch_support = max(
                maximum_branch_support,
                (representative.x | representative.z).bit_count()
                + r_mask.bit_count(),
            )
        for row, amplitude in amplitudes.items():
            if abs(amplitude) > 2.0e-13:
                rows.append(row)
                columns.append(column)
                values.append(amplitude)
                row_columns[row].add(column)

    encoding = sparse.coo_matrix(
        (values, (rows, columns)),
        shape=(len(row_lookup), len(labels)),
        dtype=complex,
    ).tocsc()
    gram = encoding.conj().T @ encoding
    difference = (gram - sparse.eye(len(labels), format="csc")).tocoo()
    collisions = tuple(
        (int(left), int(right), complex(value))
        for left, right, value in zip(difference.row, difference.col, difference.data)
        if left < right and abs(value) > 1.0e-8
    )
    return PatchEncoding(
        name,
        cells,
        labels,
        encoding,
        gram,
        maximum_branch_support,
        sum(len(columns) > 1 for columns in row_columns.values()),
        collisions,
        tuple((labels[left], labels[right], value) for left, right, value in collisions),
    )


def cell_pair(mode_pair: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(mode // 6 for mode in mode_pair)


def patch_encoding_controls() -> dict[str, object]:
    l_cells = ((2, 2, 2), (3, 2, 2), (3, 3, 2))
    square_cells = ((2, 2, 2), (3, 2, 2), (2, 3, 2), (3, 3, 2))
    held_cells = tuple((1 + x, 1 + y, 1) for y in range(3) for x in range(3))
    fixtures = (
        patch_encoding("L-triomino", l_cells, 5),
        patch_encoding("2x2", square_cells, 5),
        patch_encoding("held-3x3", held_cells, 6),
    )
    rows = []
    for fixture in fixtures:
        difference = fixture.gram - sparse.eye(len(fixture.labels), format="csc")
        row = {
            "shape": fixture.name,
            "cells": len(fixture.cells),
            "logical_dimension_total_n_le_2": len(fixture.labels),
            "physical_rows": fixture.encoding.shape[0],
            "encoding_nonzeros": fixture.encoding.nnz,
            "gram_raw_maximum": maximum_abs(difference),
            "gram_frobenius": float(sparse.linalg.norm(difference)),
            "shared_physical_rows": fixture.shared_rows,
            "collision_pairs": len(fixture.collision_pairs),
            "maximum_branch_support_M2": fixture.maximum_branch_support,
        }
        rows.append(row)

    check(
        "the raw phase-aware common E is an isometry on the acyclic L triomino and first fails on the closed 2x2 plaquette",
        rows[0]["gram_raw_maximum"] < TOL
        and rows[0]["collision_pairs"] == 0
        and rows[1]["gram_raw_maximum"] > 1.0e-4
        and rows[1]["collision_pairs"] == 6,
        rows[:2],
    )
    held = fixtures[-1]
    held_row = rows[-1]
    collision_cell_pairs = tuple(
        (cell_pair(left), cell_pair(right), value)
        for left, right, value in held.collision_labels
    )
    collision_magnitudes = sorted(
        {round(abs(value), 14) for _left, _right, value in held.collision_pairs}
    )
    collision_signs = dict(
        Counter(1 if value.real > 0 else -1 for _left, _right, value in held.collision_pairs)
    )
    collision_cells = Counter(
        tuple(sorted(set(cell_pair(left) + cell_pair(right))))
        for left, right, _value in held.collision_labels
    )
    check(
        "the held 3x3 raw E repeats exactly six pairing overlaps on each of four elementary plaquettes",
        held_row["gram_raw_maximum"] > 1.0e-4
        and held_row["collision_pairs"] == 24
        and held_row["shared_physical_rows"] == 24
        and collision_magnitudes == [0.0025]
        and sorted(collision_cells.values()) == [6] * 4,
        {
            **held_row,
            "collision_magnitudes": collision_magnitudes,
            "collision_signs": collision_signs,
            "plaquette_collision_multiplicities": dict(collision_cells),
        },
    )

    repaired, repaired_gram, whitening = direct.whiten_encoding(
        held.encoding, held.gram
    )
    repaired_residual = maximum_abs(
        repaired_gram - sparse.eye(len(held.labels), format="csc")
    )
    check(
        "a 24-block target-fit whitener repairs the held Gram matrix but is classified diagnostic-only",
        repaired_residual < TOL
        and whitening["collision_components"] == 24
        and whitening["collision_component_sizes"] == (2,) * 24
        and whitening["collided_logical_columns"] == 48,
        {**whitening, "repaired_gram_raw_maximum": repaired_residual},
    )

    held_reverse = patch_encoding("held-3x3-reverse-order", held_cells, 6, True)
    reverse_difference = held_reverse.gram - sparse.eye(
        len(held_reverse.labels), format="csc"
    )
    reverse_pairs = {
        (left, right, round(abs(value), 14))
        for left, right, value in held_reverse.collision_pairs
    }
    forward_pairs = {
        (left, right, round(abs(value), 14))
        for left, right, value in held.collision_pairs
    }
    ordering = {
        "forward_collision_pairs": len(forward_pairs),
        "reverse_collision_pairs": len(reverse_pairs),
        "pair_set_equal": forward_pairs == reverse_pairs,
        "reverse_gram_raw_maximum": maximum_abs(reverse_difference),
    }
    check(
        "reversing the supplied cell multiplication order does not remove the held plaquette collision",
        ordering["forward_collision_pairs"] == 24
        and ordering["reverse_collision_pairs"] == 24
        and ordering["pair_set_equal"],
        ordering,
    )

    deletion = fixtures[1].encoding.copy().tolil()
    deleted_column = next(
        column
        for column in range(deletion.shape[1])
        if len(deletion[:, column].nonzero()[0]) > 1
    )
    deleted_row = int(deletion[:, deleted_column].nonzero()[0][0])
    deleted_value = complex(deletion[deleted_row, deleted_column])
    deletion[deleted_row, deleted_column] = 0
    deletion = deletion.tocsc()
    deletion_residual = maximum_abs(
        deletion.conj().T @ deletion
        - sparse.eye(deletion.shape[1], format="csc")
    )
    check(
        "deleting one nonzero carrier coefficient is detected by the train-patch Gram control",
        abs(deleted_value) > 0 and deletion_residual > 1.0e-4,
        {
            "deleted_column": deleted_column,
            "deleted_row": deleted_row,
            "deleted_amplitude": deleted_value,
            "Gram_raw_maximum": deletion_residual,
        },
    )
    return {
        "shape_rows": rows,
        "held_collision_labels": [
            {"left": left, "right": right, "overlap": value}
            for left, right, value in held.collision_labels
        ],
        "held_collision_cell_pairs": collision_cell_pairs,
        "whitening_diagnostic": {**whitening, "residual": repaired_residual},
        "ordering_control": ordering,
        "coefficient_deletion_residual": deletion_residual,
    }


class PhysicalRayBasis:
    """Canonical physical rays by auxiliary word and reference syndrome."""

    def __init__(self, code):
        self.code = code
        self.face_mask = (1 << code.qubits) - 1
        self.stabilizers = code.local_checks + code.wilsons + code.B
        self.reducer = c315.c305.StabilizerReducer(code)
        self.reference: dict[tuple[int, int, int], c235.Pauli] = {}
        self.row: dict[tuple[int, int, int], int] = {}

    def reduce(self, representative: c235.Pauli) -> tuple[int, complex]:
        face = c235.Pauli(
            representative.phase,
            representative.x & self.face_mask,
            representative.z & self.face_mask,
        )
        auxiliary_x = representative.x >> self.code.qubits
        auxiliary_z = representative.z >> self.code.qubits
        syndrome = sum(
            (not face.commutes(row)) << index
            for index, row in enumerate(self.stabilizers)
        )
        key = (auxiliary_x, auxiliary_z, syndrome)
        if key not in self.reference:
            self.reference[key] = face
            self.row[key] = len(self.row)
            return self.row[key], 1 + 0j
        phase = self.reducer.relative_phase(face, self.reference[key])
        if phase is None:
            raise ValueError("equal reference syndromes must name one physical ray")
        return self.row[key], c311.c308.phase_scalar(phase)


def linear_columns(
    code,
    body,
    term_builder,
    operators: tuple[tuple[complex, c235.Pauli], ...] | None = None,
):
    basis = PhysicalRayBasis(code)
    input_columns: list[dict[int, complex]] = []
    output_columns: list[dict[int, complex]] = []
    labels = tuple(c311.FOCK_LABELS)
    for number, label in labels:
        input_amplitudes: dict[int, complex] = defaultdict(complex)
        output_amplitudes: dict[int, complex] = defaultdict(complex)
        for term in term_builder(code, body, number, label):
            row, phase = basis.reduce(term.representative)
            input_amplitudes[row] += term.amplitude * phase
            if operators is None:
                output_amplitudes[row] += term.amplitude * phase
            else:
                for coefficient, operator in operators:
                    target = operator @ term.representative
                    target_row, target_phase = basis.reduce(target)
                    output_amplitudes[target_row] += (
                        coefficient * term.amplitude * target_phase
                    )
        input_columns.append(dict(input_amplitudes))
        output_columns.append(dict(output_amplitudes))
    rows = len(basis.row)

    def matrix(columns):
        data = []
        row_indices = []
        column_indices = []
        for column, amplitudes in enumerate(columns):
            for row, amplitude in amplitudes.items():
                if abs(amplitude) > 2.0e-13:
                    row_indices.append(row)
                    column_indices.append(column)
                    data.append(amplitude)
        return sparse.coo_matrix(
            (data, (row_indices, column_indices)),
            shape=(rows, len(columns)),
            dtype=complex,
        ).tocsc()

    return labels, matrix(input_columns), matrix(output_columns)


def logical_fswap(labels, left: int, right: int) -> sparse.csc_matrix:
    lookup = {label: index for index, label in enumerate(labels)}
    rows = []
    phases = []
    for number, label in labels:
        occupied = list(label)
        both = left in occupied and right in occupied
        mapped = [
            right if mode == left else left if mode == right else mode
            for mode in occupied
        ]
        rows.append(lookup[(number, tuple(sorted(mapped)))])
        phases.append(-1 if both else 1)
    return sparse.coo_matrix(
        (phases, (rows, np.arange(len(labels)))),
        shape=(len(labels), len(labels)),
        dtype=complex,
    ).tocsc()


def outer_seam_n2_attack(code, operators):
    labels = c315.joint_labels(2)
    basis = PhysicalRayBasis(code)
    input_columns = []
    output_columns = []
    cache = {}
    for left_number, left_label, right_number, right_label in labels:
        left_terms = cache.setdefault(
            ("left", left_number, left_label),
            c315.gauge_input_terms(code, c315.LEFT, left_number, left_label),
        )
        right_terms = cache.setdefault(
            ("right", right_number, right_label),
            c315.gauge_input_terms(code, c315.RIGHT, right_number, right_label),
        )
        source_amplitudes: dict[int, complex] = defaultdict(complex)
        target_amplitudes: dict[int, complex] = defaultdict(complex)
        for left_term, right_term in product(left_terms, right_terms):
            representative = left_term.representative @ right_term.representative
            amplitude = left_term.amplitude * right_term.amplitude
            row, phase = basis.reduce(representative)
            source_amplitudes[row] += amplitude * phase
            for coefficient, operator in operators:
                target_row, target_phase = basis.reduce(operator @ representative)
                target_amplitudes[target_row] += coefficient * amplitude * target_phase
        input_columns.append(dict(source_amplitudes))
        output_columns.append(dict(target_amplitudes))

    def matrix(columns):
        rows = []
        cols = []
        data = []
        for column, amplitudes in enumerate(columns):
            for row, amplitude in amplitudes.items():
                if abs(amplitude) > 2.0e-13:
                    rows.append(row)
                    cols.append(column)
                    data.append(amplitude)
        return sparse.coo_matrix(
            (data, (rows, cols)),
            shape=(len(basis.row), len(labels)),
            dtype=complex,
        ).tocsc()

    encoding = matrix(input_columns)
    output = matrix(output_columns)
    lookup = {label: index for index, label in enumerate(labels)}
    target_rows = []
    phases = []
    for left_number, left_label, right_number, right_label in labels:
        occupied = tuple(left_label) + tuple(6 + mode for mode in right_label)
        mapped = tuple(
            7 if mode == 0 else 0 if mode == 7 else mode for mode in occupied
        )
        sign = c311.c308.permutation_sign(mapped)
        ordered = tuple(sorted(mapped))
        next_left = tuple(mode for mode in ordered if mode < 6)
        next_right = tuple(mode - 6 for mode in ordered if mode >= 6)
        target_rows.append(
            lookup[(len(next_left), next_left, len(next_right), next_right)]
        )
        phases.append(sign)
    target = sparse.coo_matrix(
        (phases, (target_rows, np.arange(len(labels)))),
        shape=(len(labels), len(labels)),
        dtype=complex,
    ).tocsc()
    overlap = encoding.conj().T @ output
    leakage = []
    for column in range(len(labels)):
        out = output[:, column].toarray().ravel()
        projected = overlap[:, column].toarray().ravel()
        leakage.append(
            max(0.0, float(np.vdot(out, out).real - np.vdot(projected, projected).real))
        )
    return {
        "logical_dimension_total_n_le_2": len(labels),
        "physical_rows": encoding.shape[0],
        "encoding_gram_raw_maximum": maximum_abs(
            encoding.conj().T @ encoding
            - sparse.eye(len(labels), format="csc")
        ),
        "intertwiner_frobenius": float(sparse.linalg.norm(output - encoding @ target)),
        "leaky_columns": sum(value > 1.0e-10 for value in leakage),
        "maximum_leakage_probability": max(leakage),
    }


def local_operator_attack() -> dict[str, object]:
    code = c315.c269.build_code(3)
    body = (0, 0, 0)
    vertices = c311.c305.body_vertices(code, body)
    # Modes 1 and 2 are adjacent both in the decoded register and on one
    # internal triangular face.  This avoids disguising a Jordan-Wigner
    # ordering string as a two-wire target convention.
    logical_left, logical_right = 1, 2
    left, right = vertices[logical_left], vertices[logical_right]
    edge = code.graph.edge_between(left, right)
    port_x = (1 << (code.qubits + left)) | (1 << (code.qubits + right))
    ahat = c235.Pauli(x=port_x) @ code.A[edge]
    bare_fswap = (
        (0.5 + 0j, code.B[left]),
        (0.5 + 0j, code.B[right]),
        (0.0 + 0.5j, code.B[left] @ ahat),
        (0.0 - 0.5j, code.B[right] @ ahat),
    )
    port_constraints = tuple(
        c311.c305.constraint_pauli(code, vertex)
        for vertex in range(len(code.graph.vertices))
    )
    commutator_failures = sum(
        not operator.commutes(constraint)
        for _coefficient, operator in bare_fswap
        for constraint in port_constraints
    )

    all_edge_maximum = 0
    all_edge_commutator_failures = 0
    maximum_by_kind: dict[str, int] = defaultdict(int)
    for edge_index, (u, v, kind, _owner) in enumerate(code.graph.edges):
        edge_ahat = c235.Pauli(
            x=(1 << (code.qubits + u)) | (1 << (code.qubits + v))
        ) @ code.A[edge_index]
        edge_terms = (
            code.B[u],
            code.B[v],
            code.B[u] @ edge_ahat,
            code.B[v] @ edge_ahat,
        )
        edge_maximum = max((term.x | term.z).bit_count() for term in edge_terms)
        all_edge_maximum = max(all_edge_maximum, edge_maximum)
        maximum_by_kind[kind] = max(maximum_by_kind[kind], edge_maximum)
        all_edge_commutator_failures += sum(
            not term.commutes(constraint)
            for term in edge_terms
            for constraint in port_constraints
        )
    check(
        "every internal and outer-edge Ahat/B FSWAP summand has bounded support and preserves all local port constraints",
        all_edge_maximum <= 11 and all_edge_commutator_failures == 0,
        {
            "tested_physical_edges": len(code.graph.edges),
            "maximum_summand_support_M2": all_edge_maximum,
            "maximum_by_face_kind": dict(maximum_by_kind),
            "port_constraint_commutator_failures": all_edge_commutator_failures,
        },
    )

    rows = {}
    matrices = {}
    for name, builder in (
        ("raw_carrier", c315.raw_input_terms),
        ("constrained_role_gauge", c315.gauge_input_terms),
    ):
        labels, encoding, physical_output = linear_columns(
            code, body, builder, bare_fswap
        )
        target = logical_fswap(labels, logical_left, logical_right)
        overlap = encoding.conj().T @ physical_output
        target_residual = float(
            sparse.linalg.norm(physical_output - encoding @ target)
        )
        per_sector = {}
        for number in range(7):
            indices = [
                index for index, (n, _label) in enumerate(labels) if n == number
            ]
            leakages = []
            for index in indices:
                output_norm = float(
                    np.vdot(
                        physical_output[:, index].toarray().ravel(),
                        physical_output[:, index].toarray().ravel(),
                    ).real
                )
                projected_norm = float(
                    np.vdot(
                        overlap[:, index].toarray().ravel(),
                        overlap[:, index].toarray().ravel(),
                    ).real
                )
                leakages.append(max(0.0, output_norm - projected_norm))
            per_sector[number] = {
                "columns": len(indices),
                "leaky_columns": sum(value > 1.0e-10 for value in leakages),
                "maximum_leakage_probability": max(leakages),
                "target_intertwiner_frobenius": float(
                    sparse.linalg.norm(
                        physical_output[:, indices] - encoding @ target[:, indices]
                    )
                ),
            }
        row = {
            "physical_rows": encoding.shape[0],
            "encoding_nonzeros": encoding.nnz,
            "encoding_gram_raw_maximum": maximum_abs(
                encoding.conj().T @ encoding
                - sparse.eye(encoding.shape[1], format="csc")
            ),
            "physical_output_norm_residual": maximum_abs(
                physical_output.conj().T @ physical_output
                - sparse.eye(physical_output.shape[1], format="csc")
            ),
            "target_intertwiner_frobenius": target_residual,
            "sectors": per_sector,
        }
        rows[name] = row
        matrices[name] = (encoding, target)

    raw = rows["raw_carrier"]
    constrained = rows["constrained_role_gauge"]
    check(
        "the bounded Ahat/B candidate commutes with every inherited port constraint and preserves, but does not correctly update, the raw even-number direct sectors",
        commutator_failures == 0
        and all(
            raw["sectors"][number]["leaky_columns"] == 0
            for number in (0, 2, 4, 6)
        )
        and raw["sectors"][2]["target_intertwiner_frobenius"] > 1.0
        and raw["sectors"][4]["target_intertwiner_frobenius"] > 1.0,
        {
            "port_constraint_commutator_failures": commutator_failures,
            "even_sector_rows": {
                number: raw["sectors"][number] for number in (0, 2, 4, 6)
            },
        },
    )
    check(
        "the same bounded word fails the actual odd carrier representatives and the constrained role-gauge common E",
        sum(
            raw["sectors"][number]["leaky_columns"]
            for number in (1, 3, 5)
        )
        > 0
        and sum(
            constrained["sectors"][number]["leaky_columns"]
            for number in range(7)
        )
        == 56
        and constrained["target_intertwiner_frobenius"] > 1.0,
        rows,
    )

    phase_scan = {}
    for phase_name, phase_factor in (
        ("+1", 1 + 0j),
        ("-1", -1 + 0j),
        ("+i", 1j),
        ("-i", -1j),
    ):
        phase_word = (
            (0.5 + 0j, code.B[left]),
            (0.5 + 0j, code.B[right]),
            (0.5j * phase_factor, code.B[left] @ ahat),
            (-0.5j * phase_factor, code.B[right] @ ahat),
        )
        phase_labels, phase_encoding, phase_output = linear_columns(
            code, body, c315.gauge_input_terms, phase_word
        )
        phase_target = logical_fswap(
            phase_labels, logical_left, logical_right
        )
        phase_overlap = phase_encoding.conj().T @ phase_output
        phase_leakages = []
        for column in range(len(phase_labels)):
            output_column = phase_output[:, column].toarray().ravel()
            projected_column = phase_overlap[:, column].toarray().ravel()
            phase_leakages.append(
                max(
                    0.0,
                    float(
                        np.vdot(output_column, output_column).real
                        - np.vdot(projected_column, projected_column).real
                    ),
                )
            )
        phase_scan[phase_name] = {
            "target_intertwiner_frobenius": float(
                sparse.linalg.norm(
                    phase_output - phase_encoding @ phase_target
                )
            ),
            "leaky_columns": sum(value > 1.0e-10 for value in phase_leakages),
            "maximum_leakage_probability": max(phase_leakages),
        }
    check(
        "all four phase/orientation conventions for Ahat fail the constrained carrier-role target",
        min(row["target_intertwiner_frobenius"] for row in phase_scan.values()) > 1.0
        and min(row["leaky_columns"] for row in phase_scan.values()) > 0,
        phase_scan,
    )

    outer_left = c311.c305.body_vertices(code, c315.LEFT)[0]
    outer_right = c311.c305.body_vertices(code, c315.RIGHT)[1]
    outer_edge = code.graph.edge_between(outer_left, outer_right)
    outer_ahat = c235.Pauli(
        x=(1 << (code.qubits + outer_left))
        | (1 << (code.qubits + outer_right))
    ) @ code.A[outer_edge]
    outer_fswap = (
        (0.5 + 0j, code.B[outer_left]),
        (0.5 + 0j, code.B[outer_right]),
        (0.0 + 0.5j, code.B[outer_left] @ outer_ahat),
        (0.0 - 0.5j, code.B[outer_right] @ outer_ahat),
    )
    outer_seam = outer_seam_n2_attack(code, outer_fswap)
    check(
        "the bare bounded outer-edge FSWAP also fails the actual two-cell role-gauge seam code at total n<=2",
        outer_seam["encoding_gram_raw_maximum"] < TOL
        and outer_seam["leaky_columns"] > 0
        and outer_seam["intertwiner_frobenius"] > 1.0,
        outer_seam,
    )

    encoder = c311.common_encoder(code, body)
    contact_basis, flagged, occurrence = c311.flagged_basis_and_encoding(encoder)
    exchange = c311.exchange_matrix(encoder, occurrence)
    constrained_encoding = c311.constrained_encoding(flagged, exchange)
    old_contact = c311.flagged_contact(encoder, contact_basis, c311.COUPLING)
    physical_contact = c311.gauge_lift(old_contact, exchange)
    logical_contact = c311.logical_contact(c311.COUPLING)
    contact_residual = maximum_abs(
        physical_contact @ constrained_encoding
        - constrained_encoding @ logical_contact
    )
    contact_phase_failures = 0
    for column in encoder.columns:
        expected = np.exp(
            1j * math.comb(column.number, 2) * c311.COUPLING
        ) if column.stream_slice == 0 else 1 + 0j
        contact_phase_failures += any(
            abs(c311.contact_phase(code, branch, c311.COUPLING) - expected) > TOL
            for branch in column.branches
        )
    check(
        "the local Cycle-230 contact is exactly reproduced on every actual carrier branch and through the role-gauge lift",
        contact_residual < TOL and contact_phase_failures == 0,
        {
            "contact_intertwiner_raw_maximum": contact_residual,
            "carrier_branch_phase_failures": contact_phase_failures,
            "coupling": c311.COUPLING,
        },
    )

    encoding, target = matrices["constrained_role_gauge"]
    fit_gram = encoding.conj().T @ encoding
    target_fit = {
        "logical_dimension": encoding.shape[1],
        "physical_ray_rows": encoding.shape[0],
        "encoding_gram_raw_maximum": maximum_abs(
            fit_gram - sparse.eye(encoding.shape[1], format="csc")
        ),
        "logical_target_unitarity_raw_maximum": maximum_abs(
            target.conj().T @ target
            - sparse.eye(target.shape[0], format="csc")
        ),
        "projector_completion_intertwiner": 0.0,
        "classification": "dense target-fit diagnostic only",
    }
    check(
        "E F E-dagger plus the complement is exact only as a dense target-fit diagnostic",
        target_fit["encoding_gram_raw_maximum"] < TOL
        and target_fit["logical_target_unitarity_raw_maximum"] < TOL
        and target_fit["classification"] == "dense target-fit diagnostic only",
        target_fit,
    )

    deleted_fswap = bare_fswap[:-1]
    _labels, deletion_input, deletion_output = linear_columns(
        code, body, c315.raw_input_terms, deleted_fswap
    )
    deletion_norm = maximum_abs(
        deletion_output.conj().T @ deletion_output
        - sparse.eye(deletion_input.shape[1], format="csc")
    )
    check(
        "deleting one B-Ahat summand breaks the physical factor norm control",
        deletion_norm > 1.0e-3,
        deletion_norm,
    )
    return {
        "modes": (logical_left, logical_right),
        "internal_edge": edge,
        "Ahat_support_M2": (ahat.x | ahat.z).bit_count(),
        "maximum_FSWAP_summand_support_M2": max(
            (operator.x | operator.z).bit_count()
            for _coefficient, operator in bare_fswap
        ),
        "all_edge_maximum_FSWAP_summand_support_M2": all_edge_maximum,
        "all_edge_maximum_by_face_kind": dict(maximum_by_kind),
        "all_edge_port_constraint_commutator_failures": all_edge_commutator_failures,
        "port_constraint_commutator_failures": commutator_failures,
        "route_rows": rows,
        "Ahat_phase_orientation_scan": phase_scan,
        "outer_seam_total_n_le_2": outer_seam,
        "local_contact": {
            "intertwiner_raw_maximum": contact_residual,
            "carrier_branch_phase_failures": contact_phase_failures,
        },
        "target_fit_diagnostic": target_fit,
        "summand_deletion_norm_residual": deletion_norm,
    }


def full_fock_and_covariance_controls() -> dict[str, object]:
    code = c315.c269.build_code(3)
    labels = c315.joint_labels(12)
    two_cell = c315.joint_encoding(code, labels, c315.RayReducer(code), False)
    two_cell_gram = maximum_abs(
        two_cell.conj().T @ two_cell
        - sparse.eye(len(labels), format="csc")
    )
    sector_dimensions = dict(Counter(left + right for left, _ll, right, _rl in labels))
    expected_dimensions = {number: math.comb(12, number) for number in range(13)}
    check(
        "the actual carrier/role graph supports the complete two-cell 2^12 Fock space, not only n<=2",
        len(labels) == 4096
        and two_cell_gram < TOL
        and sector_dimensions == expected_dimensions,
        {
            "dimension": len(labels),
            "encoding_shape": two_cell.shape,
            "encoding_nonzeros": two_cell.nnz,
            "Gram_raw_maximum": two_cell_gram,
            "sector_dimensions": sector_dimensions,
        },
    )

    encoder = c311.common_encoder(code, (0, 0, 0))
    basis, flagged, occurrence = c311.flagged_basis_and_encoding(encoder)
    exchange = c311.exchange_matrix(encoder, occurrence)
    constrained = c311.constrained_encoding(flagged, exchange)
    reducer = c315.c305.StabilizerReducer(code)
    frames = c235.proper_cubic_frames()
    reps = [c311.logical_frame_representation(frame) for frame in frames]
    frame_lookup = {tuple(frame.flatten()): index for index, frame in enumerate(frames)}
    group_failures = 0
    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            target = frame_lookup[tuple((left @ right).flatten())]
            group_failures += (
                maximum_abs(reps[left_index] @ reps[right_index] - reps[target])
                > TOL
            )
    frame_failures = 0
    maximum_flagged_residual = 0.0
    maximum_constrained_residual = 0.0
    for frame, logical in zip(frames, reps):
        physical, failures = c311.flagged_frame_representation(
            encoder, basis, occurrence, frame, reducer
        )
        mapping, phases, mapping_failures = c311.signed_mapping(physical)
        maximum_flagged_residual = max(
            maximum_flagged_residual,
            maximum_abs(c311.apply_signed_mapping(mapping, phases, flagged) - flagged @ logical),
        )
        new_mapping = np.concatenate((mapping, mapping + len(basis)))
        new_phases = np.concatenate((phases, phases))
        maximum_constrained_residual = max(
            maximum_constrained_residual,
            maximum_abs(
                c311.apply_signed_mapping(new_mapping, new_phases, constrained)
                - constrained @ logical
            ),
        )
        frame_failures += failures + mapping_failures

    translation_failures = 0
    translation_tests = 0
    for displacement in product(range(3), repeat=3):
        vertex_map, edge_map = c315.c269.graph_translation_maps(code.graph, displacement)
        toggles, pairs, flips = c315.c269.repair_data(code.graph, vertex_map, edge_map)
        target_encoder = c311.common_encoder(code, displacement)
        target_basis, _target_encoding, target_occurrence = c311.flagged_basis_and_encoding(
            target_encoder
        )
        for branch in basis:
            target_index = target_occurrence[
                (
                    branch.number,
                    branch.label,
                    branch.stream_slice,
                    branch.carrier_direction,
                )
            ]
            target_branch = target_basis[target_index]
            transformed = c311.local.transform_pauli(
                code, branch.face_pauli, edge_map, toggles, pairs, flips
            )
            translation_failures += (
                reducer.relative_phase(transformed, target_branch.face_pauli) != 0
            )
            translation_failures += (
                c311.ports.permute_bits(branch.tags, vertex_map) != target_branch.tags
            )
            translation_tests += 1
    covariance = {
        "proper_frames": len(frames),
        "group_compositions": len(frames) ** 2,
        "group_failures": group_failures,
        "frame_branch_failures": frame_failures,
        "maximum_flagged_E_residual": maximum_flagged_residual,
        "maximum_constrained_E_residual": maximum_constrained_residual,
        "translations": 27,
        "translation_branch_tests": translation_tests,
        "translation_failures": translation_failures,
    }
    check(
        "the supplied one-cell common E is phase-aware under all 24 frames, all 576 products, and all L=3 translations",
        covariance["proper_frames"] == 24
        and covariance["group_compositions"] == 576
        and covariance["group_failures"] == 0
        and covariance["frame_branch_failures"] == 0
        and covariance["maximum_flagged_E_residual"] < TOL
        and covariance["maximum_constrained_E_residual"] < TOL
        and covariance["translations"] == 27
        and covariance["translation_failures"] == 0,
        covariance,
    )

    species = c311.c219.common_species(-0.3)
    scalar_eigenvalue = np.trace(c311.c219.c210.P_SCALAR @ species.coin)
    uniform = np.ones(6) / math.sqrt(6)
    mass = {
        "beta": -0.3,
        "Cycle219_rest_mass": c311.c219.rest_mass(species),
        "uniform_coin_eigen_residual": float(
            np.linalg.norm(species.coin @ uniform - scalar_eigenvalue * uniform)
        ),
        "rest_phase": float(np.angle(scalar_eigenvalue)),
        "mass_from_scalar_phase": float(
            np.angle(scalar_eigenvalue) / c311.c219.C_SQUARED
        ),
        "contact_coupling": c311.COUPLING,
        "one_particle_contact_phase": complex(
            np.exp(1j * math.comb(1, 2) * c311.COUPLING)
        ),
        "two_particle_colocated_contact_phase": complex(
            np.exp(1j * c311.COUPLING)
        ),
    }
    check(
        "the one-particle mass fixture is unchanged and the Cycle-230 contact first becomes nontrivial at n=2",
        mass["uniform_coin_eigen_residual"] < TOL
        and abs(mass["mass_from_scalar_phase"] - mass["Cycle219_rest_mass"]) < TOL
        and abs(mass["one_particle_contact_phase"] - 1) < TOL
        and abs(mass["two_particle_colocated_contact_phase"] - 1) > 1.0e-3,
        mass,
    )
    return {
        "two_cell_full_fock": {
            "dimension": len(labels),
            "encoding_shape": two_cell.shape,
            "encoding_nonzeros": two_cell.nnz,
            "Gram_raw_maximum": two_cell_gram,
            "sector_dimensions": sector_dimensions,
        },
        "covariance": covariance,
        "mass_contact": mass,
    }


def supplied_structure_inventory() -> dict[str, object]:
    inventory = {
        "physical_substrate": [
            "Cycle-269 periodic proper-cubic square-pyramid dual graph",
            "six matter vertices and fifteen face M2 per coarse cell",
            "eight triangle plus three octagon local checks per coarse cell",
            "three fixed Wilson signs for the reference-ray reducer",
        ],
        "auxiliary_structure": [
            "six collision-safe port M2 per cell with B_v Z_port(v)=+1",
            "one stream-role flag f per cell",
            "one gauge companion r per cell",
            "Cycle-311 C_role=K_exchange X_r=+1 shell constraint",
            "carrier superpositions over unoccupied directions in odd sectors",
        ],
        "compiler_structure": [
            "a fixed cell multiplication order and its explicit reverse audit",
            "the Cycle-219 beta=-0.3 coin fixture",
            "the Cycle-230 coupling g and contact convention",
            "the Cycle-655 38-factor decoded target word only",
            "periodic hosts L=5 for train patches and L=6 for held 3x3",
        ],
        "not_supplied": [
            "no global Jordan-Wigner parity string",
            "no nonlocal parity service",
            "no Cycle-655 K7 physical encoder",
            "no host-side branch selection",
            "no physical-time interpretation of factor order",
        ],
    }
    check(
        "the runner inventories every supplied carrier, gauge, reference, ordering, target, and host choice",
        all(inventory.values()),
        inventory,
    )
    return inventory


def unlawful_domain_controls() -> dict[str, object]:
    code = c315.c269.build_code(3)
    body = (0, 0, 0)
    encoder = c311.common_encoder(code, body)
    _basis, flagged, occurrence = c311.flagged_basis_and_encoding(encoder)
    exchange = c311.exchange_matrix(encoder, occurrence)
    constrained = c311.constrained_encoding(flagged, exchange)
    port_constraints = tuple(
        c311.c305.constraint_pauli(code, vertex)
        for vertex in c311.c305.body_vertices(code, body)
    )
    extended_qubits = code.qubits + len(code.graph.vertices)
    port_rank = c315.c269.rank(list(port_constraints), extended_qubits)
    port_deletion_ranks = tuple(
        c315.c269.rank(
            list(port_constraints[:index] + port_constraints[index + 1 :]),
            extended_qubits,
        )
        for index in range(len(port_constraints))
    )
    constrained_rank = int(np.linalg.matrix_rank(constrained, tol=1.0e-10))
    unconstrained_role_shell_rank = 2 * int(
        np.linalg.matrix_rank(flagged, tol=1.0e-10)
    )
    rejected_calls = 0
    for action in (
        lambda: c311.common_branches(code, body, 7, (), 0),
        lambda: c311.common_branches(code, body, 1, (0,), 2),
        lambda: c315.joint_labels(-1),
        lambda: c315.joint_labels(13),
        lambda: c315.c269.build_code(2),
    ):
        try:
            action()
        except ValueError:
            rejected_calls += 1
    details = {
        "six_local_port_constraint_rank": port_rank,
        "single_port_constraint_deletion_ranks": port_deletion_ranks,
        "role_constrained_shell_rank": constrained_rank,
        "role_shell_rank_without_C_role": unconstrained_role_shell_rank,
        "invalid_domain_calls": 5,
        "invalid_domain_rejections": rejected_calls,
    }
    check(
        "unlawful number/slice/host inputs are rejected and deleting either local constraint family enlarges the admitted shell",
        port_rank == 6
        and port_deletion_ranks == (5,) * 6
        and constrained_rank == 127
        and unconstrained_role_shell_rank == 254
        and rejected_calls == 5,
        details,
    )
    return details


def main() -> int:
    print("CYCLE 705 ACTUAL CYCLE-269 CARRIER/ROLE SUPPORT-LOCALIZATION ATTACK")
    REPORT["substrate"] = substrate_controls()
    REPORT["patch_common_E"] = patch_encoding_controls()
    REPORT["bounded_even_word"] = local_operator_attack()
    REPORT["full_fock_covariance_mass_contact"] = full_fock_and_covariance_controls()
    REPORT["supplied_structure"] = supplied_structure_inventory()
    REPORT["unlawful_domain"] = unlawful_domain_controls()
    REPORT["status"] = {
        "strongest_constructive_result": (
            "actual phase-aware carrier/role E is exact on the L-shaped tree at total n<=2; "
            "the actual graph also has exact full one-cell and two-cell Fock capacity"
        ),
        "scoped_failure": (
            "raw common E collides on the first closed 2x2 plaquette and held 3x3, "
            "while the bare bounded Ahat/B FSWAP "
            "does not preserve the actual carrier/role code"
        ),
        "broad_negative": "blocked",
        "axiom_pressure": False,
        "authority": "none",
        "audit": "unset",
    }
    REPORT["checks"] = {"pass": PASS, "fail": FAIL}
    print("\nCYCLE705_REPORT_JSON")
    print(
        json.dumps(
            REPORT,
            indent=2,
            sort_keys=True,
            default=lambda value: (
                {"real": value.real, "imag": value.imag}
                if isinstance(value, complex)
                else list(value)
                if isinstance(value, tuple)
                else int(value)
                if isinstance(value, np.integer)
                else float(value)
                if isinstance(value, np.floating)
                else str(value)
            ),
        )
    )
    print(f"SUMMARY pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
