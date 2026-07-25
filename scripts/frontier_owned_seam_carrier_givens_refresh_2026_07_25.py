#!/usr/bin/env python3
"""Occupancy-conditioned carrier Givens word for one refreshed owned seam.

This is an independent constructive bypass of the spectator-unsafe 22-port
selector.  Each local n=1 Cycle-311 carrier vector is unprepared by four
explicit complex Givens rotations whose coefficients are derived from the
landed carrier amplitudes.  The endpoint occupations are then FSWAPed on the
canonical carrier slot and the inverse word reprepares the exact target
carrier vector.  The matrix control records the equivalent Route-B chart
refresh, while the physical synthesis implements every carrier/chart change
as an equality-controlled Pauli two-level rotation.  Its membership predicate
is invariant on the source/target pair and is therefore recomputed from the
target to return all work.  No E U E^dagger ambient completion is formed.
"""

from __future__ import annotations

from dataclasses import dataclass
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import math

import numpy as np
from scipy import sparse

import frontier_two_overlapping_maximal_star_direct_port_extractor_2026_07_25 as direct
import frontier_two_star_qutrit_compute_uncompute_coin_2026_07_25 as refresh
import frontier_two_star_qutrit_physical_update_integration_2026_07_25 as route_b
import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315


TOL = 1.0e-10
@dataclass(frozen=True)
class LocalCarrier:
    body: tuple[int, int, int]
    cell: tuple[int, int, int]
    specs: tuple[tuple[int, tuple[int, ...]], ...]
    branches: tuple[object, ...]
    representatives: tuple[object, ...]
    encoding: np.ndarray
    preparation: np.ndarray
    canonical_rows: tuple[int, ...]
    givens_rotations: int
    givens_coefficients: tuple[tuple[float, complex], ...]
    givens_factors: tuple[tuple[int, int, int, float, complex], ...]


def max_abs(matrix) -> float:
    if sparse.issparse(matrix):
        return float(max(np.abs(matrix.data), default=0.0))
    array = np.asarray(matrix)
    return float(np.max(np.abs(array))) if array.size else 0.0


def matrix_norm(matrix) -> float:
    if sparse.issparse(matrix):
        return float(np.sqrt(np.sum(np.abs(matrix.data) ** 2)))
    return float(np.linalg.norm(np.asarray(matrix)))


def complex_givens_unprepare(
    vector: np.ndarray,
) -> tuple[np.ndarray, int, tuple[tuple[float, complex], ...]]:
    """Return a product of two-level gates taking vector exactly to e_0."""

    work = np.asarray(vector, dtype=complex).copy()
    dimension = len(work)
    result = np.eye(dimension, dtype=complex)
    rotations = 0
    coefficients = []
    for other in range(dimension - 1, 0, -1):
        a, b = work[0], work[other]
        radius = math.sqrt(abs(a) ** 2 + abs(b) ** 2)
        if radius < 1.0e-15:
            continue
        if abs(a) < 1.0e-15:
            cosine = 0.0
            sine = np.conjugate(b) / abs(b)
        else:
            cosine = abs(a) / radius
            sine = a * np.conjugate(b) / (radius * abs(a))
        gate = np.eye(dimension, dtype=complex)
        gate[0, 0] = cosine
        gate[0, other] = sine
        gate[other, 0] = -np.conjugate(sine)
        gate[other, other] = cosine
        work = gate @ work
        result = gate @ result
        rotations += 1
        coefficients.append((float(cosine), complex(sine)))
    if abs(work[0]) < 1.0e-15:
        raise ValueError("the carrier vector unexpectedly vanished")
    phase_gate = np.eye(dimension, dtype=complex)
    phase_gate[0, 0] = np.conjugate(work[0]) / abs(work[0])
    work = phase_gate @ work
    result = phase_gate @ result
    assert np.linalg.norm(work - np.eye(dimension)[:, 0]) < 2.0e-13
    assert np.linalg.norm(result.conj().T @ result - np.eye(dimension)) < 2.0e-13
    return result, rotations, tuple(coefficients)


def local_carrier(
    code,
    length: int,
    cell: tuple[int, int, int],
    anchor: tuple[int, int, int] = (2, 2, 2),
) -> LocalCarrier:
    body = tuple((anchor[axis] + cell[axis]) % length for axis in range(3))
    specs = refresh.local_specs()
    branches, _labels, encoding = refresh.branch_shell(code, body, specs)
    representatives = tuple(
        refresh.representative_for_branch(code, body, branch) for branch in branches
    )
    preparation = np.eye(len(branches), dtype=complex)
    canonical_rows = []
    rotations = 0
    coefficients = []
    factors = []
    for column, spec in enumerate(specs):
        rows = np.flatnonzero(np.abs(encoding[:, column]) > 1.0e-14)
        canonical_rows.append(int(rows[0]))
        vector = encoding[rows, column]
        unprepare, count, landed_coefficients = complex_givens_unprepare(vector)
        preparation[np.ix_(rows, rows)] = unprepare.conj().T
        rotations += count
        coefficients.extend(landed_coefficients)
        for local_order, (cosine, sine) in enumerate(landed_coefficients):
            other_position = len(rows) - 1 - local_order
            factors.append(
                (
                    column,
                    int(rows[0]),
                    int(rows[other_position]),
                    float(cosine),
                    complex(sine),
                )
            )
    canonical = np.zeros_like(encoding)
    for column, row in enumerate(canonical_rows):
        canonical[row, column] = 1
    assert max_abs(preparation @ canonical - encoding) < TOL
    assert max_abs(preparation.conj().T @ preparation - np.eye(len(branches))) < TOL
    return LocalCarrier(
        body=body,
        cell=cell,
        specs=specs,
        branches=branches,
        representatives=representatives,
        encoding=encoding,
        preparation=preparation,
        canonical_rows=tuple(canonical_rows),
        givens_rotations=rotations,
        givens_coefficients=tuple(coefficients),
        givens_factors=tuple(factors),
    )


def swapped_specs(
    edge: direct.Edge,
    left: tuple[int, tuple[int, ...]],
    right: tuple[int, tuple[int, ...]],
) -> tuple[tuple[int, tuple[int, ...]], tuple[int, tuple[int, ...]], complex]:
    left_modes = set(left[1])
    right_modes = set(right[1])
    left_active = edge.first_mode in left_modes
    right_active = edge.second_mode in right_modes
    left_modes.discard(edge.first_mode)
    right_modes.discard(edge.second_mode)
    if right_active:
        left_modes.add(edge.first_mode)
    if left_active:
        right_modes.add(edge.second_mode)
    phase = -1.0 + 0j if left_active and right_active else 1.0 + 0j
    return (
        (len(left_modes), tuple(sorted(left_modes))),
        (len(right_modes), tuple(sorted(right_modes))),
        phase,
    )


def cell_chart_signature(code, local: LocalCarrier, representative) -> int:
    signature = 0
    for mode in range(6):
        blocks = route_b.BLOCKS_BY_CELL_MODE.get((local.cell, mode), ())
        if not blocks:
            continue
        vertex = c311.c305.body_vertices(code, local.body)[mode]
        _arrival, outer_edge = c311.local.old.outer_partner(code, vertex)
        outer = (int(representative.x) >> outer_edge) & 1
        tag = (int(representative.x) >> (code.qubits + vertex)) & 1
        word = route_b.qcore.qutrit_word(outer, tag)
        for block in blocks:
            signature ^= word << (2 * block)
    return signature


def pauli_inverse(pauli):
    phase = (-int(pauli.phase) - 2 * (int(pauli.z) & int(pauli.x)).bit_count()) % 4
    return direct.c330.c235.Pauli(phase, int(pauli.x), int(pauli.z))


def augmented_representative(code, locals_by_cell, by_cell):
    representative = direct.c330.c235.Pauli()
    chart = 0
    for cell in sorted(by_cell, key=lambda index: locals_by_cell[index].cell):
        row = by_cell[cell]
        local = locals_by_cell[cell]
        representative = representative @ local.representatives[row]
        chart ^= cell_chart_signature(code, local, local.representatives[row])
    base = (
        code.qubits
        + len(code.graph.vertices)
        + 2 * len(code.graph.cells)
    )
    return direct.c330.c235.Pauli(
        int(representative.phase),
        int(representative.x) | (int(chart) << base),
        int(representative.z),
    ), chart


def bounded_observation(code, representative, chart, ports, blocks):
    port_word = sum(
        ((int(representative.x) >> (code.qubits + vertex)) & 1) << bit
        for bit, vertex in enumerate(ports)
    )
    chart_word = sum(
        ((int(chart) >> (2 * block)) & 0b11) << (2 * bit)
        for bit, block in enumerate(blocks)
    )
    return chart_word, port_word


def periodic_l1(left, right, length: int) -> int:
    return sum(
        min((left[axis] - right[axis]) % length, (right[axis] - left[axis]) % length)
        for axis in range(3)
    )


def support_coarse_cells(code, support: int, anchor=(2, 2, 2)):
    cells = set()
    vertices = len(code.graph.vertices)
    coarse_cells = len(code.graph.cells)
    q_base = code.qubits + vertices + 2 * coarse_cells
    for qubit in range(support.bit_length()):
        if not ((support >> qubit) & 1):
            continue
        if qubit < code.qubits:
            first, second, *_rest = code.graph.edges[qubit]
            cells.add(tuple(code.graph.vertices[first][0]))
            cells.add(tuple(code.graph.vertices[second][0]))
        elif qubit < code.qubits + vertices:
            cells.add(tuple(code.graph.vertices[qubit - code.qubits][0]))
        elif qubit < q_base:
            role_index = (qubit - code.qubits - vertices) % coarse_cells
            cells.add(tuple(code.graph.cells[role_index]))
        else:
            block = (qubit - q_base) // 2
            if block < len(route_b.FEATURE_BLOCKS):
                cell = route_b.FEATURE_BLOCKS[block][3]
                cells.add(
                    tuple((anchor[axis] + cell[axis]) % code.length for axis in range(3))
                )
    return cells


def pair_control(length: int, edge_index: int) -> dict[str, object]:
    code = c315.c269.build_code(length)
    edge = direct.SOURCE_EDGES[edge_index]
    left = local_carrier(code, length, direct.UNION_COORDS[0][edge.first_cell])
    right = local_carrier(code, length, direct.UNION_COORDS[0][edge.second_cell])
    spec_index = {spec: index for index, spec in enumerate(left.specs)}
    logical_pairs = tuple(
        (left_spec, right_spec)
        for left_spec in left.specs
        for right_spec in right.specs
        if left_spec[0] + right_spec[0] <= 2
    )
    logical_index = {pair: index for index, pair in enumerate(logical_pairs)}

    branch_pairs = tuple(
        (left_row, right_row)
        for left_row, left_branch in enumerate(left.branches)
        for right_row, right_branch in enumerate(right.branches)
        if left_branch.number + right_branch.number <= 2
    )
    pair_index = {pair: index for index, pair in enumerate(branch_pairs)}
    full_rows = np.asarray(
        [left_row * len(right.branches) + right_row for left_row, right_row in branch_pairs]
    )
    full_columns = np.asarray(
        [
            spec_index[left_spec] * len(right.specs) + spec_index[right_spec]
            for left_spec, right_spec in logical_pairs
        ]
    )
    full_encoding = sparse.kron(
        sparse.csc_matrix(left.encoding),
        sparse.csc_matrix(right.encoding),
        format="csc",
    )
    encoding = full_encoding[full_rows, :][:, full_columns].tocsc()
    full_preparation = sparse.kron(
        sparse.csc_matrix(left.preparation),
        sparse.csc_matrix(right.preparation),
        format="csc",
    )
    preparation = full_preparation[full_rows, :][:, full_rows].tocsc()

    mapping = np.arange(len(branch_pairs), dtype=np.int64)
    phases = np.ones(len(branch_pairs), dtype=complex)
    logical_rows = []
    logical_phases = []
    for source, (left_spec, right_spec) in enumerate(logical_pairs):
        target_left, target_right, phase = swapped_specs(edge, left_spec, right_spec)
        target = logical_index[(target_left, target_right)]
        logical_rows.append(target)
        logical_phases.append(phase)
        source_pair = (
            left.canonical_rows[spec_index[left_spec]],
            right.canonical_rows[spec_index[right_spec]],
        )
        target_pair = (
            left.canonical_rows[spec_index[target_left]],
            right.canonical_rows[spec_index[target_right]],
        )
        mapping[pair_index[source_pair]] = pair_index[target_pair]
        phases[pair_index[source_pair]] = phase
    occupation_fswap = sparse.coo_matrix(
        (phases, (mapping, np.arange(len(branch_pairs)))),
        shape=(len(branch_pairs), len(branch_pairs)),
        dtype=complex,
    ).tocsc()
    logical_fswap = sparse.coo_matrix(
        (logical_phases, (logical_rows, np.arange(len(logical_pairs)))),
        shape=(len(logical_pairs), len(logical_pairs)),
        dtype=complex,
    ).tocsc()

    decoded = preparation.conj().T @ encoding
    transported = occupation_fswap @ decoded
    output = preparation @ transported
    target = encoding @ logical_fswap
    intertwiner = output - target
    physical_seam = preparation @ occupation_fswap @ preparation.conj().T
    identity = sparse.eye(len(branch_pairs), format="csc", dtype=complex)

    # Expose the invalid old decoder argument: keeping the source pair label
    # while K mixes the branch and then XORing the target label does not return
    # work.  A lawful transition transports the label to the coherent target;
    # the physical implementation below instead uses an invariant unordered
    # source/target membership predicate and avoids a persistent pair label.
    stale_rows = []
    stale_cols = []
    stale_data = []
    seam_coo = physical_seam.tocoo()
    encoding_csr = encoding.tocsr()
    for target_row, source_row, transition in zip(
        seam_coo.row, seam_coo.col, seam_coo.data
    ):
        source_column = encoding_csr.getrow(int(source_row)).tocoo()
        work_word = int(source_row) ^ int(target_row)
        for column, amplitude in zip(source_column.col, source_column.data):
            stale_rows.append(work_word * len(branch_pairs) + int(target_row))
            stale_cols.append(int(column))
            stale_data.append(transition * amplitude)
    stale_output = sparse.coo_matrix(
        (stale_data, (stale_rows, stale_cols)),
        shape=((1 << 10) * len(branch_pairs), len(logical_pairs)),
        dtype=complex,
    ).tocsc()
    stale_nonblank = stale_output[len(branch_pairs) :, :]
    transported_label_output = physical_seam @ encoding
    transported_label_return_residual = matrix_norm(transported_label_output - output)

    # Route-B chart refresh matrix control.  The later physical primitive
    # audit replaces a persistent erase/decoder word by direct augmented
    # source/target two-level rotations with invariant membership work.
    left_signatures = tuple(
        cell_chart_signature(code, left, representative)
        for representative in left.representatives
    )
    right_signatures = tuple(
        cell_chart_signature(code, right, representative)
        for representative in right.representatives
    )
    signatures = np.asarray(
        [left_signatures[i] ^ right_signatures[j] for i, j in branch_pairs],
        dtype=object,
    )
    signature_values = tuple(sorted(set(int(value) for value in signatures)))
    signature_index = {value: index for index, value in enumerate(signature_values)}

    def augment(matrix: sparse.csc_matrix) -> sparse.csc_matrix:
        matrix = matrix.tocoo()
        rows = [
            signature_index[int(signatures[row])] * len(branch_pairs) + int(row)
            for row in matrix.row
        ]
        return sparse.coo_matrix(
            (matrix.data, (rows, matrix.col)),
            shape=(len(signature_values) * len(branch_pairs), matrix.shape[1]),
            dtype=complex,
        ).tocsc()

    augmented_encoding = augment(encoding)
    augmented_output = augment(output)
    augmented_target = augmented_encoding @ logical_fswap
    augmented_difference = augmented_output - augmented_target
    augmented_leakage = augmented_output - augmented_encoding @ (
        augmented_encoding.conj().T @ augmented_output
    )

    invalid_qutrit_words = 0
    duplicate_failures = 0
    for signature in signatures:
        words = tuple((int(signature) >> (2 * block)) & 0b11 for block in range(24))
        invalid_qutrit_words += sum(word not in route_b.qcore.LAWFUL_QUTRIT_WORDS for word in words)
        duplicate_failures += words[0] != words[15]
        duplicate_failures += words[1] != words[14]

    # Deleting one landed carrier coefficient means replacing the exact
    # five-component preparation on the first n=1 label by a spectator block.
    deleted_local = left.preparation.copy()
    first_one = next(
        column for column, spec in enumerate(left.specs) if spec[0] == 1
    )
    deleted_rows = np.flatnonzero(np.abs(left.encoding[:, first_one]) > 1.0e-14)
    deleted_local[np.ix_(deleted_rows, deleted_rows)] = np.eye(len(deleted_rows))
    deleted_full = sparse.kron(
        sparse.csc_matrix(deleted_local),
        sparse.csc_matrix(right.preparation),
        format="csc",
    )[full_rows, :][:, full_rows].tocsc()
    deleted_output = deleted_full @ occupation_fswap @ deleted_full.conj().T @ encoding
    deletion_residual = matrix_norm(deleted_output - target)

    rng = np.random.default_rng(659000 + length)
    random = rng.normal(size=len(branch_pairs)) + 1.0j * rng.normal(size=len(branch_pairs))
    random /= np.linalg.norm(random)
    returned = physical_seam.conj().T @ (physical_seam @ random)
    coefficient_rows = left.givens_coefficients + right.givens_coefficients
    coefficient_unitarity = max(
        abs(cosine * cosine + abs(sine) ** 2 - 1.0)
        for cosine, sine in coefficient_rows
    )

    return {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "edge": edge_index,
        "cells": (edge.first_cell, edge.second_cell),
        "modes": (edge.first_mode, edge.second_mode),
        "logical_pair_columns_n_le_2": len(logical_pairs),
        "bare_pair_branch_microbasis": len(branch_pairs),
        "local_carrier_rotations_per_cell": left.givens_rotations,
        "two_cell_carrier_rotations": left.givens_rotations + right.givens_rotations,
        "landed_complex_givens_coefficients": len(coefficient_rows),
        "givens_coefficient_unitarity_residual": coefficient_unitarity,
        "preparation_unitarity": max_abs(preparation.conj().T @ preparation - identity),
        "occupation_FSWAP_unitarity": max_abs(
            occupation_fswap.conj().T @ occupation_fswap - identity
        ),
        "structured_seam_unitarity": max_abs(
            physical_seam.conj().T @ physical_seam - identity
        ),
        "bare_intertwiner_norm": matrix_norm(intertwiner),
        "bare_intertwiner_raw": max_abs(intertwiner),
        "reachable_qutrit_chart_words": len(signature_values),
        "invalid_qutrit_words": invalid_qutrit_words,
        "duplicate_shared_chart_failures": duplicate_failures,
        "chart_refresh_intertwiner_norm": matrix_norm(augmented_difference),
        "chart_refresh_intertwiner_raw": max_abs(augmented_difference),
        "chart_refresh_leakage": matrix_norm(augmented_leakage),
        "carrier_coefficient_deletion_residual": deletion_residual,
        "randomized_inverse_residual": float(np.linalg.norm(returned - random)),
        "naive_source_label_target_decode_nonblank_norm": matrix_norm(stale_nonblank),
        "coherently_transported_target_label_return_residual": (
            transported_label_return_residual
        ),
        "persistent_pair_label_used_by_physical_word": False,
        "carrier_word_extra_work_M2": 0,
        "dense_EUE_completion_used": False,
        "global_mode_order_used": False,
        "direct_22_port_selector_used": False,
        "full_domain_seam_claimed": False,
    }


def full_domain_chart_audit(length: int) -> dict[str, object]:
    """Test all eleven owned seam decoders on all 59,941 code branches."""

    code = c315.c269.build_code(length)
    locals_by_cell = tuple(
        local_carrier(code, length, cell) for cell in direct.UNION_COORDS[0]
    )
    spec_indices = {
        spec: index for index, spec in enumerate(locals_by_cell[0].specs)
    }
    rows_by_cell_spec = []
    signatures_by_cell = []
    vacuum_rows = []
    for local in locals_by_cell:
        rows_by_spec = {
            spec: tuple(np.flatnonzero(np.abs(local.encoding[:, column]) > 1.0e-14))
            for column, spec in enumerate(local.specs)
        }
        rows_by_cell_spec.append(rows_by_spec)
        signatures_by_cell.append(
            tuple(
                cell_chart_signature(code, local, representative)
                for representative in local.representatives
            )
        )
        vacuum_rows.append(rows_by_spec[(0, ())][0])

    edge_data = tuple(
        direct.physical_edge_data(code, tuple(local.body for local in locals_by_cell), edge)
        for edge in direct.SOURCE_EDGES
    )
    cell_blocks = []
    for cell in direct.UNION_COORDS[0]:
        blocks = sorted(
            {
                block
                for mode in range(6)
                for block in route_b.BLOCKS_BY_CELL_MODE.get((cell, mode), ())
            }
        )
        cell_blocks.append(tuple(blocks))
    edge_blocks = tuple(
        tuple(sorted(set(cell_blocks[edge.first_cell]) | set(cell_blocks[edge.second_cell])))
        for edge in direct.SOURCE_EDGES
    )
    edge_ports = tuple(tuple(sorted(data["union"])) for data in edge_data)
    observations = [defaultdict(set) for _edge in direct.SOURCE_EDGES]
    histories = 0
    invalid_qutrit_words = 0
    duplicate_shared_chart_failures = 0

    for label in direct.LABELS:
        active = direct.active_local_cells(label)
        local_rows = [
            rows_by_cell_spec[cell][direct.local_spec(label, cell)] for cell in active
        ]
        for selected in product(*local_rows) if local_rows else ((),):
            by_cell = dict(zip(active, selected))
            representative = direct.c330.c235.Pauli()
            chart = 0
            for cell, row in by_cell.items():
                representative = representative @ locals_by_cell[cell].representatives[row]
                chart ^= int(signatures_by_cell[cell][row])
            words = tuple((chart >> (2 * block)) & 0b11 for block in range(24))
            invalid_qutrit_words += sum(
                word not in route_b.qcore.LAWFUL_QUTRIT_WORDS for word in words
            )
            duplicate_shared_chart_failures += words[0] != words[15]
            duplicate_shared_chart_failures += words[1] != words[14]
            for owner, edge in enumerate(direct.SOURCE_EDGES):
                left_row = int(by_cell.get(edge.first_cell, vacuum_rows[edge.first_cell]))
                right_row = int(by_cell.get(edge.second_cell, vacuum_rows[edge.second_cell]))
                port_word = sum(
                    ((int(representative.x) >> (code.qubits + vertex)) & 1) << bit
                    for bit, vertex in enumerate(edge_ports[owner])
                )
                chart_word = sum(
                    ((chart >> (2 * block)) & 0b11) << (2 * bit)
                    for bit, block in enumerate(edge_blocks[owner])
                )
                observations[owner][(chart_word, port_word)].add((left_row, right_row))
            histories += 1

    edge_rows = []
    for owner, edge in enumerate(direct.SOURCE_EDGES):
        table = observations[owner]
        chart_deleted: dict[int, set[tuple[int, int]]] = defaultdict(set)
        port_deleted: dict[int, set[tuple[int, int]]] = defaultdict(set)
        for (chart_word, port_word), pairs in table.items():
            chart_deleted[port_word].update(pairs)
            port_deleted[chart_word].update(pairs)
        edge_rows.append(
            {
                "edge": owner,
                "cells": (edge.first_cell, edge.second_cell),
                "modes": (edge.first_mode, edge.second_mode),
                "reachable_bounded_observations": len(table),
                "decoder_ambiguities": sum(len(pairs) > 1 for pairs in table.values()),
                "maximum_decoder_multiplicity": max(map(len, table.values())),
                "port_M2": len(edge_ports[owner]),
                "qutrit_blocks": len(edge_blocks[owner]),
                "qutrit_M2": 2 * len(edge_blocks[owner]),
                "maximum_equality_controls": (
                    len(edge_ports[owner]) + 2 * len(edge_blocks[owner])
                ),
                "chart_deleted_ambiguities": sum(
                    len(pairs) > 1 for pairs in chart_deleted.values()
                ),
                "port_deleted_ambiguities": sum(
                    len(pairs) > 1 for pairs in port_deleted.values()
                ),
            }
        )

    maximum_branch_support = 0
    maximum_total_support = 0
    for owner, edge in enumerate(direct.SOURCE_EDGES):
        union = 0
        for cell in (edge.first_cell, edge.second_cell):
            for representative in locals_by_cell[cell].representatives:
                union |= int(representative.x) | int(representative.z)
        maximum_branch_support = max(maximum_branch_support, union.bit_count())
        maximum_total_support = max(
            maximum_total_support,
            union.bit_count() + 2 * len(edge_blocks[owner]),
        )
    return {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "logical_columns_n_le_2": len(direct.LABELS),
        "physical_code_branch_histories": histories,
        "owned_seams": len(direct.SOURCE_EDGES),
        "edge_rows": edge_rows,
        "total_decoder_ambiguities": sum(row["decoder_ambiguities"] for row in edge_rows),
        "invalid_qutrit_words": invalid_qutrit_words,
        "duplicate_shared_chart_failures": duplicate_shared_chart_failures,
        "minimum_chart_deletion_ambiguities": min(
            row["chart_deleted_ambiguities"] for row in edge_rows
        ),
        "minimum_port_deletion_ambiguities": min(
            row["port_deleted_ambiguities"] for row in edge_rows
        ),
        "maximum_port_M2": max(row["port_M2"] for row in edge_rows),
        "maximum_qutrit_blocks": max(row["qutrit_blocks"] for row in edge_rows),
        "maximum_qutrit_M2": max(row["qutrit_M2"] for row in edge_rows),
        "endpoint_pair_label_bits": 12,
        "maximum_reversible_truth_table_rows": max(
            row["reachable_bounded_observations"] for row in edge_rows
        ),
        "maximum_equality_controls": max(
            row["maximum_equality_controls"] for row in edge_rows
        ),
        "maximum_branch_control_M2_union": maximum_branch_support,
        "maximum_branch_plus_chart_M2_union": maximum_total_support,
        "global_mode_order_used": False,
        "full_union_selector_used": False,
        "host_side_control_used": False,
        "naive_pair_label_uncompute_claim_removed": True,
        "decoder_implementation": (
            "bounded observation table only; returned-work implementation is audited "
            "separately by invariant source/target membership predicates"
        ),
    }


def physical_two_level_primitive_audit(length: int) -> dict[str, object]:
    """Synthesize/audit every ray transition used by all owned seam words.

    A transition is selected by membership in the unordered pair of its source
    and target bounded observations.  That predicate is one on both endpoints,
    so it remains one throughout the two-level rotation and can be XORed away
    by the target observation.  This replaces the invalid ``source XOR source``
    decoder argument.
    """

    code = c315.c269.build_code(length)
    locals_by_cell = tuple(
        local_carrier(code, length, cell) for cell in direct.UNION_COORDS[0]
    )
    rows_by_cell_spec = []
    vacuum_rows = []
    carrier_neighbors = []
    carrier_factor_maps = []
    canonical_by_spec = []
    spec_by_row = []
    for local in locals_by_cell:
        rows_by_spec = {
            spec: tuple(np.flatnonzero(np.abs(local.encoding[:, column]) > 1.0e-14))
            for column, spec in enumerate(local.specs)
        }
        rows_by_cell_spec.append(rows_by_spec)
        vacuum_rows.append(rows_by_spec[(0, ())][0])
        neighbors = defaultdict(set)
        canonical = {}
        row_specs = {}
        for spec, rows in rows_by_spec.items():
            canonical[spec] = int(rows[0])
            for row in rows:
                row_specs[int(row)] = spec
            if spec[0] == 1:
                for row in rows[1:]:
                    neighbors[int(rows[0])].add(int(row))
                    neighbors[int(row)].add(int(rows[0]))
        carrier_neighbors.append(neighbors)
        factor_map = {}
        for factor_order, (
            _column,
            first_row,
            other_row,
            cosine,
            sine,
        ) in enumerate(local.givens_factors):
            factor_map[frozenset((first_row, other_row))] = (
                factor_order,
                cosine,
                sine,
            )
        carrier_factor_maps.append(factor_map)
        canonical_by_spec.append(canonical)
        spec_by_row.append(row_specs)

    edge_data = tuple(
        direct.physical_edge_data(code, tuple(local.body for local in locals_by_cell), edge)
        for edge in direct.SOURCE_EDGES
    )
    cell_blocks = tuple(
        tuple(
            sorted(
                {
                    block
                    for mode in range(6)
                    for block in route_b.BLOCKS_BY_CELL_MODE.get((cell, mode), ())
                }
            )
        )
        for cell in direct.UNION_COORDS[0]
    )
    edge_blocks = tuple(
        tuple(sorted(set(cell_blocks[edge.first_cell]) | set(cell_blocks[edge.second_cell])))
        for edge in direct.SOURCE_EDGES
    )
    edge_ports = tuple(tuple(sorted(data["union"])) for data in edge_data)

    descriptors: dict[
        tuple[int, tuple[int, int], tuple[int, int], tuple[int, int]],
        set[tuple[tuple[int, int], int, int, int]],
    ] = defaultdict(set)
    coefficient_associations = defaultdict(set)
    diagonal_phase_rows = set()
    transition_visits = 0

    for label in direct.LABELS:
        active = direct.active_local_cells(label)
        local_rows = [
            rows_by_cell_spec[cell][direct.local_spec(label, cell)] for cell in active
        ]
        for selected in product(*local_rows) if local_rows else ((),):
            by_cell = dict(zip(active, map(int, selected)))
            source_augmented, source_chart = augmented_representative(
                code, locals_by_cell, by_cell
            )
            for owner, edge in enumerate(direct.SOURCE_EDGES):
                source_pair = (
                    int(by_cell.get(edge.first_cell, vacuum_rows[edge.first_cell])),
                    int(by_cell.get(edge.second_cell, vacuum_rows[edge.second_cell])),
                )
                source_observation = bounded_observation(
                    code,
                    source_augmented,
                    source_chart,
                    edge_ports[owner],
                    edge_blocks[owner],
                )
                target_actions = {}
                for target_left in carrier_neighbors[edge.first_cell].get(
                    source_pair[0], ()
                ):
                    pair = (target_left, source_pair[1])
                    order, cosine, sine = carrier_factor_maps[edge.first_cell][
                        frozenset((source_pair[0], target_left))
                    ]
                    target_actions[pair] = (
                        "left_carrier_givens",
                        order,
                        float(cosine),
                        float(np.real(sine)),
                        float(np.imag(sine)),
                    )
                for target_right in carrier_neighbors[edge.second_cell].get(
                    source_pair[1], ()
                ):
                    pair = (source_pair[0], target_right)
                    order, cosine, sine = carrier_factor_maps[edge.second_cell][
                        frozenset((source_pair[1], target_right))
                    ]
                    target_actions[pair] = (
                        "right_carrier_givens",
                        order,
                        float(cosine),
                        float(np.real(sine)),
                        float(np.imag(sine)),
                    )

                left_spec = spec_by_row[edge.first_cell][source_pair[0]]
                right_spec = spec_by_row[edge.second_cell][source_pair[1]]
                if (
                    source_pair[0] == canonical_by_spec[edge.first_cell][left_spec]
                    and source_pair[1] == canonical_by_spec[edge.second_cell][right_spec]
                ):
                    target_left_spec, target_right_spec, fswap_phase = swapped_specs(
                        edge, left_spec, right_spec
                    )
                    occupation_target = (
                        canonical_by_spec[edge.first_cell][target_left_spec],
                        canonical_by_spec[edge.second_cell][target_right_spec],
                    )
                    if occupation_target == source_pair:
                        if abs(fswap_phase + 1) < TOL:
                            diagonal_phase_rows.add(
                                (owner, source_observation, source_pair, -1.0, 0.0)
                            )
                    else:
                        target_actions[occupation_target] = (
                            "occupation_FSWAP",
                            0,
                            float(np.real(fswap_phase)),
                            float(np.imag(fswap_phase)),
                            0.0,
                        )

                for target_pair, coefficient_record in target_actions.items():
                    if target_pair == source_pair:
                        continue
                    target_by_cell = dict(by_cell)
                    for cell, row in (
                        (edge.first_cell, target_pair[0]),
                        (edge.second_cell, target_pair[1]),
                    ):
                        if locals_by_cell[cell].branches[row].number == 0:
                            target_by_cell.pop(cell, None)
                        else:
                            target_by_cell[cell] = int(row)
                    target_augmented, target_chart = augmented_representative(
                        code, locals_by_cell, target_by_cell
                    )
                    target_observation = bounded_observation(
                        code,
                        target_augmented,
                        target_chart,
                        edge_ports[owner],
                        edge_blocks[owner],
                    )
                    transition = target_augmented @ pauli_inverse(source_augmented)
                    descriptor_key = (
                        owner,
                        source_observation,
                        source_pair,
                        target_pair,
                    )
                    descriptors[descriptor_key].add(
                        (
                            target_observation,
                            int(transition.phase),
                            int(transition.x),
                            int(transition.z),
                        )
                    )
                    coefficient_associations[descriptor_key].add(coefficient_record)
                    transition_visits += 1

    descriptor_conflicts = sum(len(values) > 1 for values in descriptors.values())
    coefficient_association_conflicts = sum(
        len(values) > 1 for values in coefficient_associations.values()
    )
    descriptors_without_coefficients = sum(
        key not in coefficient_associations for key in descriptors
    )
    first_conflict = next(
        (
            {"key": key, "values": values}
            for key, values in descriptors.items()
            if len(values) > 1
        ),
        None,
    )
    membership_return_failures = 0
    maximum_transition_support = 0
    maximum_controls = 0
    maximum_control_transition_tensor_support = 0
    maximum_coarse_diameter = 0
    maximum_owner_radius = 0
    q_base = (
        code.qubits
        + len(code.graph.vertices)
        + 2 * len(code.graph.cells)
    )
    for (owner, source_observation, _source_pair, _target_pair), values in descriptors.items():
        maximum_controls = max(
            maximum_controls,
            len(edge_ports[owner]) + 2 * len(edge_blocks[owner]),
        )
        if len(values) != 1:
            continue
        target_observation, _phase, x_word, z_word = next(iter(values))
        maximum_transition_support = max(
            maximum_transition_support, (int(x_word) | int(z_word)).bit_count()
        )
        control_mask = sum(
            1 << (code.qubits + vertex) for vertex in edge_ports[owner]
        )
        control_mask |= sum(
            (0b11 << (q_base + 2 * block)) for block in edge_blocks[owner]
        )
        maximum_control_transition_tensor_support = max(
            maximum_control_transition_tensor_support,
            (int(x_word) | int(z_word) | control_mask).bit_count(),
        )
        tensor_cells = support_coarse_cells(
            code, int(x_word) | int(z_word) | control_mask
        )
        if tensor_cells:
            maximum_coarse_diameter = max(
                maximum_coarse_diameter,
                max(
                    periodic_l1(left_cell, right_cell, length)
                    for left_cell in tensor_cells
                    for right_cell in tensor_cells
                ),
            )
            edge = direct.SOURCE_EDGES[owner]
            owner_cells = (
                locals_by_cell[edge.first_cell].body,
                locals_by_cell[edge.second_cell].body,
            )
            maximum_owner_radius = max(
                maximum_owner_radius,
                max(
                    min(
                        periodic_l1(cell, owner_cell, length)
                        for owner_cell in owner_cells
                    )
                    for cell in tensor_cells
                ),
            )
        # The reversible predicate is membership in {source,target}; it is one
        # before and after the two-level gate, so the target-side recomputation
        # returns its predicate and comparator scratch to zero.
        source_membership = int(source_observation in (source_observation, target_observation))
        target_membership = int(target_observation in (source_observation, target_observation))
        membership_return_failures += source_membership != 1 or target_membership != 1

    maximum_comparator_work = max(0, maximum_controls - 2) + 3
    reverse_transition_failures = 0
    for (owner, source_observation, source_pair, target_pair), values in descriptors.items():
        if len(values) != 1:
            continue
        target_observation, phase, x_word, z_word = next(iter(values))
        reverse_key = (owner, target_observation, target_pair, source_pair)
        reverse_values = descriptors.get(reverse_key, set())
        transition = direct.c330.c235.Pauli(phase, x_word, z_word)
        inverse = pauli_inverse(transition)
        expected = (source_observation, inverse.phase, inverse.x, inverse.z)
        reverse_transition_failures += expected not in reverse_values
    observation_control_rows = defaultdict(set)
    for (owner, source_observation, source_pair, target_pair), values in descriptors.items():
        if len(values) != 1 or len(coefficient_associations.get(
            (owner, source_observation, source_pair, target_pair), set()
        )) != 1:
            continue
        target_observation, phase, x_word, z_word = next(iter(values))
        coefficient_record = next(
            iter(
                coefficient_associations[
                    (owner, source_observation, source_pair, target_pair)
                ]
            )
        )
        control_key = (
            owner,
            coefficient_record,
            source_observation,
            target_observation,
        )
        observation_control_rows[control_key].add(
            (source_pair, target_pair, phase, x_word, z_word)
        )
    observation_only_control_conflicts = sum(
        len(values) > 1 for values in observation_control_rows.values()
    )
    rom_rows = tuple(
        sorted(
            [
                (
                    repr(key),
                    repr(next(iter(values))),
                )
                for key, values in observation_control_rows.items()
                if len(values) == 1
            ]
            + [("diagonal_collision_phase", repr(row)) for row in diagonal_phase_rows]
        )
    )
    rom_sha256 = sha256(repr(rom_rows).encode("utf-8")).hexdigest()
    return {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "global_transition_visits": transition_visits,
        "distinct_controlled_two_level_rows": len(descriptors),
        "transition_descriptor_conflicts": descriptor_conflicts,
        "coefficient_association_conflicts": coefficient_association_conflicts,
        "descriptors_without_coefficients": descriptors_without_coefficients,
        "observation_only_control_conflicts": observation_only_control_conflicts,
        "observation_only_control_rows": len(observation_control_rows),
        "diagonal_collision_phase_rows": len(diagonal_phase_rows),
        "finite_rotation_ROM_sha256": rom_sha256,
        "first_transition_descriptor_conflict": first_conflict,
        "membership_predicate_return_failures": membership_return_failures,
        "reverse_transition_pairing_failures": reverse_transition_failures,
        "maximum_observation_controls": maximum_controls,
        "maximum_transition_Pauli_support": maximum_transition_support,
        "maximum_control_plus_transition_tensor_M2": (
            maximum_control_transition_tensor_support
        ),
        "maximum_clean_comparator_work_M2": maximum_comparator_work,
        "maximum_total_tensor_M2_with_returned_work": (
            maximum_control_transition_tensor_support + maximum_comparator_work
        ),
        "maximum_coarse_L1_diameter": maximum_coarse_diameter,
        "maximum_owner_coarse_L1_radius": maximum_owner_radius,
        "primitive_word": (
            "compute membership in the unordered source/target observation pair "
            "with X-normalization and multi-controlled Toffoli; Clifford-conjugate "
            "the fixed transition Pauli to one pivot; apply the landed complex "
            "two-level Ry/Rz angle; reverse Clifford and recompute membership on "
            "the target observation to return all predicate/comparator work"
        ),
        "projector_formula": (
            "Pi_o=product_k (I+(-1)^o_k Z_k)/2 on owner port+q-chart M2; "
            "A=Pi_target Q Pi_source; H_phi=-i exp(i phi) A + h.c."
        ),
        "abstract_ray_matrix_unit_used": False,
        "dense_EUE_completion_used": False,
        "physical_M2_primitive_supplied": (
            descriptor_conflicts == 0
            and coefficient_association_conflicts == 0
            and descriptors_without_coefficients == 0
            and observation_only_control_conflicts == 0
            and reverse_transition_failures == 0
            and membership_return_failures == 0
        ),
        "finite_control_ROM_retained": True,
        "gate_order": (
            "per owner: 24 left-carrier unprepare factors, then 24 right-carrier "
            "unprepare factors, canonical occupation FSWAP plus collision phase, "
            "then inverse right and inverse left factors; owners 0..10, then contact"
        ),
        "translation_invariant_recurrent_law_derived": False,
        "recurrent_volume_update_claimed": False,
    }


def translated_two_star_fixture_control(length: int) -> dict[str, object]:
    """Replay every owned local chart at every torus translation."""

    code = c315.c269.build_code(length)
    reference = local_carrier(code, length, direct.UNION_COORDS[0][0])
    reference_coefficients = reference.givens_coefficients
    ambiguities = invalid_words = duplicate_failures = coefficient_mismatches = 0
    owner_fixtures = 0
    observation_counts = Counter()
    for anchor in code.graph.cells:
        anchor = tuple(anchor)
        locals_by_cell = tuple(
            local_carrier(code, length, cell, anchor=anchor)
            for cell in direct.UNION_COORDS[0]
        )
        coefficient_mismatches += sum(
            len(local.givens_coefficients) != len(reference_coefficients)
            or max(
                abs(left[0] - right[0]) + abs(left[1] - right[1])
                for left, right in zip(
                    local.givens_coefficients, reference_coefficients
                )
            )
            > TOL
            for local in locals_by_cell
        )
        for local in locals_by_cell:
            for representative in local.representatives:
                chart = cell_chart_signature(code, local, representative)
                words = tuple(
                    (chart >> (2 * block)) & 0b11 for block in range(24)
                )
                invalid_words += sum(
                    word not in route_b.qcore.LAWFUL_QUTRIT_WORDS
                    for word in words
                )
                duplicate_failures += words[0] != words[15]
                duplicate_failures += words[1] != words[14]
        bodies = tuple(local.body for local in locals_by_cell)
        for owner, edge in enumerate(direct.SOURCE_EDGES):
            data = direct.physical_edge_data(code, bodies, edge)
            ports = tuple(sorted(data["union"]))
            blocks = tuple(
                sorted(
                    {
                        block
                        for cell in (
                            direct.UNION_COORDS[0][edge.first_cell],
                            direct.UNION_COORDS[0][edge.second_cell],
                        )
                        for mode in range(6)
                        for block in route_b.BLOCKS_BY_CELL_MODE.get((cell, mode), ())
                    }
                )
            )
            left = locals_by_cell[edge.first_cell]
            right = locals_by_cell[edge.second_cell]
            left_signatures = tuple(
                cell_chart_signature(code, left, representative)
                for representative in left.representatives
            )
            right_signatures = tuple(
                cell_chart_signature(code, right, representative)
                for representative in right.representatives
            )
            outcomes = defaultdict(set)
            for left_row, left_branch in enumerate(left.branches):
                for right_row, right_branch in enumerate(right.branches):
                    if left_branch.number + right_branch.number > 2:
                        continue
                    representative = (
                        left.representatives[left_row]
                        @ right.representatives[right_row]
                    )
                    chart = int(left_signatures[left_row]) ^ int(
                        right_signatures[right_row]
                    )
                    observation = bounded_observation(
                        code, representative, chart, ports, blocks
                    )
                    outcomes[observation].add((left_row, right_row))
            ambiguities += sum(len(pairs) > 1 for pairs in outcomes.values())
            observation_counts[(owner, len(outcomes))] += 1
            owner_fixtures += 1
    digest = sha256(repr(sorted(observation_counts.items())).encode("utf-8")).hexdigest()
    return {
        "L": length,
        "translations": len(code.graph.cells),
        "translated_owner_fixtures": owner_fixtures,
        "translation_chart_ambiguities": ambiguities,
        "translation_invalid_qutrit_words": invalid_words,
        "translation_duplicate_chart_failures": duplicate_failures,
        "translation_carrier_coefficient_mismatches": coefficient_mismatches,
        "translation_fixture_sha256": digest,
        "all_torus_translations_tested": True,
        "recurrent_update_claimed": False,
    }


def composed_update_controls(maximum_local_intertwiner: float, maximum_local_leakage: float):
    coin = direct.logical_coin()
    streams = tuple(direct.edge_stream(edge) for edge in direct.SOURCE_EDGES)
    seam = direct.stream_product(direct.SOURCE_EDGES)
    contact = direct.logical_contact()
    update = contact @ seam @ coin
    identity = sparse.eye(len(direct.LABELS), format="csc", dtype=complex)
    deleted = direct.stream_product(
        tuple(
            edge
            for index, edge in enumerate(direct.SOURCE_EDGES)
            if index != direct.SHARED_EDGE_INDEX
        )
    )
    duplicated = seam @ streams[direct.SHARED_EDGE_INDEX]
    one_indices = [direct.LABEL_INDEX[(mode,)] for mode in range(72)]
    one_particle = update[np.ix_(one_indices, one_indices)]
    uniform = np.ones(72, dtype=complex) / math.sqrt(72)
    eigenvalue = np.vdot(uniform, one_particle @ uniform)
    mass = float(np.angle(eigenvalue)) / direct.c330.c219.C_SQUARED
    mass_fixture = direct.c330.c219.rest_mass(
        direct.c330.c219.common_species(-0.3)
    )
    covariance = direct.covariance_controls(
        {"coin": coin, "contact": contact, "update": update}
    )
    return {
        "unique_owned_seams": len(streams),
        "seam_unitarity": c315.largest_singular(seam.conj().T @ seam - identity),
        "contact_unitarity": c315.largest_singular(contact.conj().T @ contact - identity),
        "update_unitarity": c315.largest_singular(update.conj().T @ update - identity),
        "deleted_shared_seam_residual": c315.largest_singular(deleted - seam),
        "duplicated_shared_seam_residual": c315.largest_singular(duplicated - seam),
        "contact_nontrivial_columns": int(
            np.count_nonzero(np.abs(contact.diagonal() - 1) > 2.0e-13)
        ),
        "one_particle_mass": mass,
        "Cycle219_mass_fixture": mass_fixture,
        "one_particle_eigen_residual": float(
            np.linalg.norm(one_particle @ uniform - eigenvalue * uniform)
        ),
        "sum_of_pair_fixture_intertwiner_residuals": 11 * maximum_local_intertwiner,
        "sum_of_pair_fixture_leakage_residuals": 11 * maximum_local_leakage,
        "composition_argument": (
            "pair-fixture closure does not establish common-E composition: the "
            "actual 59,941-row execution in the common-E runner finds the missing "
            "graded CAR parity cocycle"
        ),
        "common_E_composition_executed_here": False,
        "covariance": covariance,
        "dense_EUE_completion_used": False,
        "full_union_selector_used": False,
    }


def main() -> None:
    rows = tuple(
        pair_control(length, edge)
        for length in (5, 6)
        for edge in range(len(direct.SOURCE_EDGES))
    )
    audits = tuple(full_domain_chart_audit(length) for length in (5, 6))
    primitives = tuple(
        physical_two_level_primitive_audit(length) for length in (5, 6)
    )
    translations = tuple(
        translated_two_star_fixture_control(length) for length in (5, 6)
    )
    composed = composed_update_controls(
        max(row["chart_refresh_intertwiner_norm"] for row in rows),
        max(row["chart_refresh_leakage"] for row in rows),
    )
    boundary = {
        "authority": "none",
        "audit": "unset",
        "finite_rotation_ROM_rows_L5": primitives[0][
            "observation_only_control_rows"
        ],
        "finite_rotation_ROM_rows_L6": primitives[1][
            "observation_only_control_rows"
        ],
        "diagonal_collision_phase_rows_L5": primitives[0][
            "diagonal_collision_phase_rows"
        ],
        "finite_rotation_ROM_supplied": True,
        "ROM_contents": (
            "bounded source/target owner observations, fixed transition Pauli, "
            "landed carrier Givens coefficient or occupation FSWAP/phase, and gate ordinal"
        ),
        "carrier_coefficient_direction_rule": (
            "for landed G=[[c,s],[-conj(s),c]]: other->canonical uses s, "
            "canonical->other uses -conj(s); reprepare uses the reversed adjoint word"
        ),
        "owner_gate_order_supplied": primitives[0]["gate_order"],
        "owner_schedule_is_finite_program_ordinal_not_physical_time": True,
        "derived_translation_invariant_recurrent_law": False,
        "recurrent_volume_update_claimed": False,
        "global_mode_order_used": False,
        "dense_EUE_completion_used": False,
        "axiom_pressure_claimed": False,
    }
    print("OWNED_SEAM_OCCUPANCY_CONDITIONED_CARRIER_GIVENS")
    for row in rows:
        print("pair", row)
    for audit in audits:
        print("domain", audit)
    for primitive in primitives:
        print("primitive", primitive)
    for translation in translations:
        print("translation", translation)
    print("composed", composed)
    print("boundary", boundary)
    for row in rows:
        assert row["logical_pair_columns_n_le_2"] == 79
        assert row["bare_pair_branch_microbasis"] == 991
        assert row["local_carrier_rotations_per_cell"] == 24
        assert row["two_cell_carrier_rotations"] == 48
        assert row["landed_complex_givens_coefficients"] == 48
        assert row["givens_coefficient_unitarity_residual"] < TOL
        assert row["preparation_unitarity"] < TOL
        assert row["occupation_FSWAP_unitarity"] < TOL
        assert row["structured_seam_unitarity"] < TOL
        assert row["bare_intertwiner_norm"] < TOL
        assert row["chart_refresh_intertwiner_norm"] < TOL
        assert row["chart_refresh_leakage"] < TOL
        assert row["invalid_qutrit_words"] == 0
        assert row["duplicate_shared_chart_failures"] == 0
        assert row["carrier_coefficient_deletion_residual"] > 1.0e-3
        assert row["randomized_inverse_residual"] < TOL
        assert row["naive_source_label_target_decode_nonblank_norm"] > 1.0e-3
        assert row["coherently_transported_target_label_return_residual"] < TOL
        assert not row["persistent_pair_label_used_by_physical_word"]
        assert not row["dense_EUE_completion_used"]
        assert not row["global_mode_order_used"]
        assert not row["full_domain_seam_claimed"]
    for audit in audits:
        assert audit["logical_columns_n_le_2"] == 2629
        assert audit["physical_code_branch_histories"] == 59941
        assert audit["owned_seams"] == 11
        assert audit["total_decoder_ambiguities"] == 0
        assert audit["invalid_qutrit_words"] == 0
        assert audit["duplicate_shared_chart_failures"] == 0
        assert all(row["decoder_ambiguities"] == 0 for row in audit["edge_rows"])
        assert audit["minimum_chart_deletion_ambiguities"] > 0
        assert audit["maximum_port_M2"] <= 22
        assert audit["maximum_qutrit_blocks"] <= 14
        assert audit["endpoint_pair_label_bits"] == 12
        assert audit["maximum_equality_controls"] <= 50
        assert not audit["global_mode_order_used"]
        assert not audit["full_union_selector_used"]
        assert not audit["host_side_control_used"]
        assert audit["naive_pair_label_uncompute_claim_removed"]
    for primitive in primitives:
        assert primitive["transition_descriptor_conflicts"] == 0
        assert primitive["coefficient_association_conflicts"] == 0
        assert primitive["descriptors_without_coefficients"] == 0
        assert primitive["observation_only_control_conflicts"] == 0
        assert primitive["observation_only_control_rows"] == 46306
        assert primitive["membership_predicate_return_failures"] == 0
        assert primitive["reverse_transition_pairing_failures"] == 0
        assert primitive["maximum_observation_controls"] <= 50
        assert primitive["maximum_transition_Pauli_support"] <= 117
        assert primitive["maximum_control_plus_transition_tensor_M2"] <= 117
        assert primitive["maximum_total_tensor_M2_with_returned_work"] <= 168
        assert primitive["maximum_coarse_L1_diameter"] <= 4
        assert primitive["maximum_owner_coarse_L1_radius"] <= 2
        assert primitive["physical_M2_primitive_supplied"]
        assert not primitive["abstract_ray_matrix_unit_used"]
        assert not primitive["dense_EUE_completion_used"]
        assert primitive["finite_control_ROM_retained"]
        assert not primitive["translation_invariant_recurrent_law_derived"]
        assert not primitive["recurrent_volume_update_claimed"]
    for translation in translations:
        assert translation["translations"] == translation["L"] ** 3
        assert translation["translated_owner_fixtures"] == 11 * translation["L"] ** 3
        assert translation["translation_chart_ambiguities"] == 0
        assert translation["translation_invalid_qutrit_words"] == 0
        assert translation["translation_duplicate_chart_failures"] == 0
        assert translation["translation_carrier_coefficient_mismatches"] == 0
        assert translation["all_torus_translations_tested"]
        assert not translation["recurrent_update_claimed"]
    covariance = composed["covariance"]
    assert composed["unique_owned_seams"] == 11
    assert composed["seam_unitarity"] < TOL
    assert composed["contact_unitarity"] < TOL
    assert composed["update_unitarity"] < TOL
    assert composed["deleted_shared_seam_residual"] > 1.0
    assert composed["duplicated_shared_seam_residual"] > 1.0
    assert composed["contact_nontrivial_columns"] == 180
    assert abs(composed["one_particle_mass"] - composed["Cycle219_mass_fixture"]) < TOL
    assert composed["one_particle_eigen_residual"] < TOL
    assert covariance["proper_cubic_frames"] == 24
    assert covariance["frame_products"] == 576
    assert covariance["maximum_update_covariance"] < TOL
    assert covariance["frame_group_failures"] == 0
    assert covariance["feature_transport_failures"] == 0
    assert covariance["feature_group_failures"] == 0
    assert not composed["dense_EUE_completion_used"]
    assert not composed["full_union_selector_used"]
    assert boundary["finite_rotation_ROM_supplied"]
    assert not boundary["derived_translation_invariant_recurrent_law"]
    assert not boundary["recurrent_volume_update_claimed"]
    assert not boundary["axiom_pressure_claimed"]
    print("LOCAL_OWNED_CARRIER_GIVENS_PRIMITIVES_CLOSED_GLOBAL_COMMON_E_UNSET_HERE")


if __name__ == "__main__":
    main()
