#!/usr/bin/env python3
"""Occupancy-conditioned carrier Givens word for one refreshed owned seam.

This is an independent constructive bypass of the spectator-unsafe 22-port
selector.  Each local n=1 Cycle-311 carrier vector is unprepared by four
explicit complex Givens rotations whose coefficients are derived from the
landed carrier amplitudes.  The endpoint occupations are then FSWAPed on the
canonical carrier slot and the inverse word reprepares the exact target
carrier vector.  Route-B qutrit charts are treated by erase/recompute around
that bounded word.  No E U E^dagger ambient completion is formed.
"""

from __future__ import annotations

from dataclasses import dataclass
from collections import Counter, defaultdict
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


def max_abs(matrix) -> float:
    if sparse.issparse(matrix):
        return float(max(np.abs(matrix.data), default=0.0))
    array = np.asarray(matrix)
    return float(np.max(np.abs(array))) if array.size else 0.0


def matrix_norm(matrix) -> float:
    if sparse.issparse(matrix):
        return float(np.sqrt(np.sum(np.abs(matrix.data) ** 2)))
    return float(np.linalg.norm(np.asarray(matrix)))


def complex_givens_unprepare(vector: np.ndarray) -> tuple[np.ndarray, int]:
    """Return a product of two-level gates taking vector exactly to e_0."""

    work = np.asarray(vector, dtype=complex).copy()
    dimension = len(work)
    result = np.eye(dimension, dtype=complex)
    rotations = 0
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
    if abs(work[0]) < 1.0e-15:
        raise ValueError("the carrier vector unexpectedly vanished")
    phase_gate = np.eye(dimension, dtype=complex)
    phase_gate[0, 0] = np.conjugate(work[0]) / abs(work[0])
    work = phase_gate @ work
    result = phase_gate @ result
    assert np.linalg.norm(work - np.eye(dimension)[:, 0]) < 2.0e-13
    assert np.linalg.norm(result.conj().T @ result - np.eye(dimension)) < 2.0e-13
    return result, rotations


def local_carrier(code, length: int, cell: tuple[int, int, int]) -> LocalCarrier:
    body = tuple((2 + value) % length for value in cell)
    specs = refresh.local_specs()
    branches, _labels, encoding = refresh.branch_shell(code, body, specs)
    representatives = tuple(
        refresh.representative_for_branch(code, body, branch) for branch in branches
    )
    preparation = np.eye(len(branches), dtype=complex)
    canonical_rows = []
    rotations = 0
    for column, spec in enumerate(specs):
        rows = np.flatnonzero(np.abs(encoding[:, column]) > 1.0e-14)
        canonical_rows.append(int(rows[0]))
        vector = encoding[rows, column]
        unprepare, count = complex_givens_unprepare(vector)
        preparation[np.ix_(rows, rows)] = unprepare.conj().T
        rotations += count
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

    # Route-B chart refresh: the first XOR erases these exact words, the
    # structured seam acts only on the bare carrier shell, and the second XOR
    # writes the target-branch words.  Store only the reachable chart sectors;
    # no augmented completion is materialized.
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
    compute_uncompute_failures = 0
    for owner, edge in enumerate(direct.SOURCE_EDGES):
        table = observations[owner]
        chart_deleted: dict[int, set[tuple[int, int]]] = defaultdict(set)
        port_deleted: dict[int, set[tuple[int, int]]] = defaultdict(set)
        for (chart_word, port_word), pairs in table.items():
            chart_deleted[port_word].update(pairs)
            port_deleted[chart_word].update(pairs)
            if len(pairs) == 1:
                left_row, right_row = next(iter(pairs))
                decoded = left_row * 46 + right_row
                compute_uncompute_failures += (0 ^ decoded ^ decoded) != 0
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
                "decoder_work_M2": 12,
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
        "decoder_compute_uncompute_failures": compute_uncompute_failures,
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
        "decoder_work_M2": 12,
        "maximum_reversible_truth_table_rows": max(
            row["reachable_bounded_observations"] for row in edge_rows
        ),
        "maximum_equality_controls": max(
            row["maximum_equality_controls"] for row in edge_rows
        ),
        "maximum_branch_control_M2_union": maximum_branch_support,
        "maximum_branch_plus_chart_M2_union": maximum_total_support,
        "maximum_total_M2_with_decoder_work": maximum_total_support + 12,
        "global_mode_order_used": False,
        "full_union_selector_used": False,
        "host_side_control_used": False,
        "decoder_implementation": (
            "fixed equality-controlled XOR into a 12-M2 endpoint-pair word; "
            "use the word to select the finite Givens sequence; repeat XOR to return blank"
        ),
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
        "eleven_seam_intertwiner_norm_bound": 11 * maximum_local_intertwiner,
        "eleven_seam_leakage_norm_bound": 11 * maximum_local_leakage,
        "composition_argument": (
            "each owned seam maps the same common code to itself; the all-column "
            "bounded-chart decoder audit therefore applies inductively after every seam"
        ),
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
    composed = composed_update_controls(
        max(row["chart_refresh_intertwiner_norm"] for row in rows),
        max(row["chart_refresh_leakage"] for row in rows),
    )
    print("OWNED_SEAM_OCCUPANCY_CONDITIONED_CARRIER_GIVENS")
    for row in rows:
        print("pair", row)
    for audit in audits:
        print("domain", audit)
    print("composed", composed)
    for row in rows:
        assert row["logical_pair_columns_n_le_2"] == 79
        assert row["bare_pair_branch_microbasis"] == 991
        assert row["local_carrier_rotations_per_cell"] == 24
        assert row["two_cell_carrier_rotations"] == 48
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
        assert not row["dense_EUE_completion_used"]
        assert not row["global_mode_order_used"]
        assert not row["full_domain_seam_claimed"]
    for audit in audits:
        assert audit["logical_columns_n_le_2"] == 2629
        assert audit["physical_code_branch_histories"] == 59941
        assert audit["owned_seams"] == 11
        assert audit["total_decoder_ambiguities"] == 0
        assert audit["decoder_compute_uncompute_failures"] == 0
        assert audit["invalid_qutrit_words"] == 0
        assert audit["duplicate_shared_chart_failures"] == 0
        assert all(row["decoder_ambiguities"] == 0 for row in audit["edge_rows"])
        assert audit["minimum_chart_deletion_ambiguities"] > 0
        assert audit["maximum_port_M2"] <= 22
        assert audit["maximum_qutrit_blocks"] <= 14
        assert audit["decoder_work_M2"] == 12
        assert audit["maximum_equality_controls"] <= 50
        assert not audit["global_mode_order_used"]
        assert not audit["full_union_selector_used"]
        assert not audit["host_side_control_used"]
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
    print("ELEVEN_OWNED_CARRIER_GIVENS_SEAMS_AND_CONTACT_CLOSED_ON_COMMON_DOMAIN")


if __name__ == "__main__":
    main()
