#!/usr/bin/env python3
"""Execute the ordered owned-seam ROM on the actual 59,941-row common E.

Unlike the preceding compositional bound, this runner constructs each sparse
physical owner operator from the landed coefficient-tagged Givens word, maps
it into the canonical reduced Route-B ray rows including reducer phases, and
multiplies it into the common E before advancing to the next owner.  Contact
is then applied as an actual physical row diagonal.  No Gram/isometry identity
is used as the intertwining test.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import product
import math

import numpy as np
from scipy import sparse

import frontier_owned_seam_carrier_givens_refresh_2026_07_25 as carrier
import frontier_two_overlapping_maximal_star_direct_port_extractor_2026_07_25 as direct
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315


TOL = 2.0e-10

# The common reduced physical encoder multiplies cell representatives in this
# lexicographic coordinate order.  Its logical CAR modes must use the same
# factor order: changing the cell order without the induced exterior-algebra
# signs is precisely a hidden Jordan--Wigner convention.  The original direct
# route numbers the two centers first, so explicitly conjugate its geometric
# edge list into the physical factor order before doing the common-E test.
PHYSICAL_CELLS = tuple(sorted(direct.UNION_COORDS[0]))
PHYSICAL_CELL_INDEX = {cell: index for index, cell in enumerate(PHYSICAL_CELLS)}
PHYSICAL_EDGES = tuple(
    direct.Edge(
        PHYSICAL_CELL_INDEX[direct.UNION_COORDS[0][edge.first_cell]],
        edge.first_mode,
        PHYSICAL_CELL_INDEX[direct.UNION_COORDS[0][edge.second_cell]],
        edge.second_mode,
    )
    for edge in direct.SOURCE_EDGES
)


def canonical_cells(axis: int):
    return tuple(sorted(direct.UNION_COORDS[axis]))


def canonical_edges(axis: int):
    cells = canonical_cells(axis)
    index = {cell: position for position, cell in enumerate(cells)}
    return tuple(
        direct.Edge(
            index[direct.UNION_COORDS[axis][edge.first_cell]],
            edge.first_mode,
            index[direct.UNION_COORDS[axis][edge.second_cell]],
            edge.second_mode,
        )
        for edge in direct.EDGES[axis]
    )


def max_abs(matrix) -> float:
    if sparse.issparse(matrix):
        return float(max(np.abs(matrix.data), default=0.0))
    array = np.asarray(matrix)
    return float(np.max(np.abs(array))) if array.size else 0.0


def matrix_norm(matrix) -> float:
    if sparse.issparse(matrix):
        return float(np.sqrt(np.sum(np.abs(matrix.data) ** 2)))
    return float(np.linalg.norm(np.asarray(matrix)))


@dataclass(frozen=True)
class GlobalFixture:
    length: int
    code: object
    locals_by_cell: tuple[carrier.LocalCarrier, ...]
    vacuum_rows: tuple[int, ...]
    histories: tuple[tuple[int, ...], ...]
    history_to_row: dict[tuple[int, ...], int]
    reducer_phases: np.ndarray
    auxiliary_words: tuple[int, ...]
    encoding: sparse.csc_matrix


def build_global_fixture(length: int) -> GlobalFixture:
    code = c315.c269.build_code(length)
    locals_by_cell = tuple(
        carrier.local_carrier(code, length, cell)
        for cell in PHYSICAL_CELLS
    )
    rows_by_cell_spec = []
    vacuum_rows = []
    for local in locals_by_cell:
        rows_by_spec = {
            spec: tuple(np.flatnonzero(np.abs(local.encoding[:, column]) > 1.0e-14))
            for column, spec in enumerate(local.specs)
        }
        rows_by_cell_spec.append(rows_by_spec)
        vacuum_rows.append(int(rows_by_spec[(0, ())][0]))

    reducer = c315.RayReducer(code)
    history_to_row: dict[tuple[int, ...], int] = {}
    history_by_row: list[tuple[int, ...] | None] = []
    phase_by_row: list[complex] = []
    auxiliary_by_row: list[int] = []
    rows = []
    columns = []
    values = []
    collisions = 0
    branch_histories = 0
    for column, label in enumerate(direct.LABELS):
        active = direct.active_local_cells(label)
        local_rows = [
            rows_by_cell_spec[cell][direct.local_spec(label, cell)] for cell in active
        ]
        for selected in product(*local_rows) if local_rows else ((),):
            by_cell = dict(zip(active, map(int, selected)))
            representative, _chart = carrier.augmented_representative(
                code, locals_by_cell, by_cell
            )
            physical_row, reducer_phase = reducer.reduce(representative)
            auxiliary = int(representative.x) >> code.qubits
            history = list(vacuum_rows)
            amplitude = 1.0 + 0j
            for cell, row in by_cell.items():
                history[cell] = row
                amplitude *= locals_by_cell[cell].branches[row].amplitude
            history_key = tuple(history)
            if physical_row == len(history_by_row):
                history_by_row.append(history_key)
                phase_by_row.append(complex(reducer_phase))
                auxiliary_by_row.append(auxiliary)
            else:
                collisions += history_by_row[physical_row] != history_key
                if history_by_row[physical_row] != history_key:
                    raise ValueError("the common qutrit E lost one branch history")
                if abs(phase_by_row[physical_row] - reducer_phase) > TOL:
                    raise ValueError("one physical history acquired inconsistent reducer phase")
                if auxiliary_by_row[physical_row] != auxiliary:
                    raise ValueError("one reduced row acquired inconsistent auxiliary M2 bits")
            history_to_row[history_key] = physical_row
            rows.append(physical_row)
            columns.append(column)
            values.append(amplitude * reducer_phase)
            branch_histories += 1
    encoding = sparse.coo_matrix(
        (values, (rows, columns)),
        shape=(len(history_by_row), len(direct.LABELS)),
        dtype=complex,
    ).tocsc()
    zero_columns = sum(encoding.getcol(column).nnz == 0 for column in range(encoding.shape[1]))
    if (
        branch_histories != 59941
        or len(history_by_row) != 59941
        or encoding.nnz != 59941
        or collisions
        or zero_columns
    ):
        raise ValueError(
            (branch_histories, len(history_by_row), encoding.nnz, collisions, zero_columns)
        )
    return GlobalFixture(
        length=length,
        code=code,
        locals_by_cell=locals_by_cell,
        vacuum_rows=tuple(vacuum_rows),
        histories=tuple(history for history in history_by_row if history is not None),
        history_to_row=history_to_row,
        reducer_phases=np.asarray(phase_by_row, dtype=complex),
        auxiliary_words=tuple(auxiliary_by_row),
        encoding=encoding,
    )


def local_two_level_gate(size: int, factor, inverse: bool = False):
    _column, first, other, cosine, sine = factor
    gate = sparse.eye(size, format="lil", dtype=complex)
    block = np.asarray(
        [[cosine, sine], [-np.conjugate(sine), cosine]], dtype=complex
    )
    if inverse:
        block = block.conj().T
    gate[np.ix_((first, other), (first, other))] = block
    return gate.tocsc()


def rotation_decoder_phases(local: carrier.LocalCarrier) -> dict[object, complex]:
    """Return the canonical phases left by the 24 landed Givens rotations.

    ``complex_givens_unprepare`` also used a final one-level phase when it
    built ``local.preparation``.  That phase was absent from the landed
    24-factor ROM.  It cannot simply be discarded: when a seam changes a
    doubly occupied endpoint into two singly occupied endpoints, the product
    of the two local decoder phases changes.  Coefficient-tag the occupation
    row by the exact target/source decoder-phase ratio instead.
    """

    decoder = sparse.eye(len(local.branches), format="csc", dtype=complex)
    for factor in local.givens_factors:
        decoder = local_two_level_gate(len(local.branches), factor) @ decoder
    result = {}
    for column, spec in enumerate(local.specs):
        decoded = decoder @ local.encoding[:, column]
        canonical = local.canonical_rows[column]
        phase = complex(decoded[canonical])
        residue = decoded.copy()
        residue[canonical] = 0
        if np.linalg.norm(residue) > TOL or abs(abs(phase) - 1.0) > TOL:
            raise ValueError("the landed Givens word did not phase-decode one carrier")
        result[spec] = phase
    return result


def pair_rom_operator(fixture: GlobalFixture, edge_index: int):
    edge = PHYSICAL_EDGES[edge_index]
    left = fixture.locals_by_cell[edge.first_cell]
    right = fixture.locals_by_cell[edge.second_cell]
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

    def lift(factor, side: str, inverse: bool = False):
        if side == "left":
            full = sparse.kron(
                local_two_level_gate(len(left.branches), factor, inverse),
                sparse.eye(len(right.branches), format="csc", dtype=complex),
                format="csc",
            )
        else:
            full = sparse.kron(
                sparse.eye(len(left.branches), format="csc", dtype=complex),
                local_two_level_gate(len(right.branches), factor, inverse),
                format="csc",
            )
        return full[full_rows, :][:, full_rows].tocsc()

    word = sparse.eye(len(branch_pairs), format="csc", dtype=complex)
    gate_count = 0
    for factor in left.givens_factors:
        word = lift(factor, "left") @ word
        gate_count += 1
    for factor in right.givens_factors:
        word = lift(factor, "right") @ word
        gate_count += 1

    mapping = np.arange(len(branch_pairs), dtype=np.int64)
    phases = np.ones(len(branch_pairs), dtype=complex)
    spec_index = {spec: index for index, spec in enumerate(left.specs)}
    left_decoder_phases = rotation_decoder_phases(left)
    right_decoder_phases = rotation_decoder_phases(right)
    for left_spec in left.specs:
        for right_spec in right.specs:
            if left_spec[0] + right_spec[0] > 2:
                continue
            source_pair = (
                left.canonical_rows[spec_index[left_spec]],
                right.canonical_rows[spec_index[right_spec]],
            )
            target_left, target_right, phase = carrier.swapped_specs(
                edge, left_spec, right_spec
            )
            target_pair = (
                left.canonical_rows[spec_index[target_left]],
                right.canonical_rows[spec_index[target_right]],
            )
            mapping[pair_index[source_pair]] = pair_index[target_pair]
            source_decoder_phase = (
                left_decoder_phases[left_spec] * right_decoder_phases[right_spec]
            )
            target_decoder_phase = (
                left_decoder_phases[target_left]
                * right_decoder_phases[target_right]
            )
            phases[pair_index[source_pair]] = (
                phase * target_decoder_phase / source_decoder_phase
            )
    occupation = sparse.coo_matrix(
        (phases, (mapping, np.arange(len(branch_pairs)))),
        shape=(len(branch_pairs), len(branch_pairs)),
        dtype=complex,
    ).tocsc()
    word = occupation @ word
    gate_count += 1
    for factor in reversed(right.givens_factors):
        word = lift(factor, "right", inverse=True) @ word
        gate_count += 1
    for factor in reversed(left.givens_factors):
        word = lift(factor, "left", inverse=True) @ word
        gate_count += 1
    return word.tocsc(), branch_pairs, pair_index, gate_count


def global_owner_operator(fixture: GlobalFixture, edge_index: int):
    edge = PHYSICAL_EDGES[edge_index]
    pair_word, branch_pairs, pair_index, gate_count = pair_rom_operator(
        fixture, edge_index
    )
    transitions = []
    pair_csc = pair_word.tocsc()
    for source in range(len(branch_pairs)):
        column = pair_csc.getcol(source).tocoo()
        transitions.append(tuple(zip(map(int, column.row), map(complex, column.data))))

    rows = []
    columns = []
    data = []
    missing_targets = 0
    for source_row, history in enumerate(fixture.histories):
        source_pair = (history[edge.first_cell], history[edge.second_cell])
        source_pair_index = pair_index[source_pair]
        source_phase = fixture.reducer_phases[source_row]
        for target_pair_index, coefficient in transitions[source_pair_index]:
            target_pair = branch_pairs[target_pair_index]
            target_history = list(history)
            target_history[edge.first_cell] = target_pair[0]
            target_history[edge.second_cell] = target_pair[1]
            target_row = fixture.history_to_row.get(tuple(target_history))
            if target_row is None:
                missing_targets += 1
                continue
            target_phase = fixture.reducer_phases[target_row]
            rows.append(target_row)
            columns.append(source_row)
            data.append(target_phase * coefficient / source_phase)
    operator = sparse.coo_matrix(
        (data, (rows, columns)),
        shape=(len(fixture.histories), len(fixture.histories)),
        dtype=complex,
    ).tocsc()
    operator.sum_duplicates()
    operator.data[np.abs(operator.data) < 2.0e-13] = 0
    operator.eliminate_zeros()
    return operator, {
        "owner": edge_index,
        "pair_ROM_gates": gate_count,
        "pair_ROM_nonzeros": pair_word.nnz,
        "physical_operator_nonzeros": operator.nnz,
        "missing_target_histories": missing_targets,
    }


def physical_contact(fixture: GlobalFixture):
    phases = []
    for history in fixture.histories:
        local_pairs = sum(
            fixture.locals_by_cell[cell].branches[row].number
            * (fixture.locals_by_cell[cell].branches[row].number - 1)
            // 2
            for cell, row in enumerate(history)
        )
        phases.append(np.exp(1j * direct.c330.c230.COUPLING * local_pairs))
    return sparse.diags(phases, format="csc", dtype=complex)


def local_tensor_edge(edge: direct.Edge):
    """The logical action actually induced by the endpoint-only pair ROM."""

    rows = []
    phases = []
    for label in direct.LABELS:
        specs = [direct.local_spec(label, cell) for cell in range(12)]
        target_left, target_right, phase = carrier.swapped_specs(
            edge, specs[edge.first_cell], specs[edge.second_cell]
        )
        specs[edge.first_cell] = target_left
        specs[edge.second_cell] = target_right
        target = tuple(
            sorted(
                6 * cell + mode
                for cell, spec in enumerate(specs)
                for mode in spec[1]
            )
        )
        rows.append(direct.LABEL_INDEX[target])
        phases.append(phase)
    return sparse.coo_matrix(
        (phases, (rows, np.arange(len(rows)))),
        shape=(len(rows), len(rows)),
        dtype=complex,
    ).tocsc()


def edge_sign_inventory(edge: direct.Edge) -> dict[str, object]:
    actual = local_tensor_edge(edge)
    target = direct.edge_stream(edge)
    cocycle = target.conj().T @ actual
    diagonal = cocycle.diagonal()
    off_diagonal = cocycle - sparse.diags(diagonal, format="csc")
    return {
        "endpoint_modes_in_offline_basis": edge.modes,
        "strictly_intervening_mode_slots": abs(edge.modes[1] - edge.modes[0]) - 1,
        "missing_negative_CAR_parity_columns": int(
            np.count_nonzero(np.abs(diagonal + 1.0) < TOL)
        ),
        "missing_cocycle_off_diagonal_nonzeros": off_diagonal.nnz,
        "exact_missing_cocycle": (
            "D_e=G_CAR(e)^dagger G_endpoint(e); on n<=2 it is -1 "
            "exactly when one endpoint is occupied and the occupation parity "
            "strictly between its two offline mode slots is odd"
        ),
    }


def bounded_sign_tag_audit(fixture: GlobalFixture):
    """Ask whether existing owner observations can tag the missing CAR sign.

    This is only a finite-ROM ambiguity audit.  It does not assert that every
    possible bounded auxiliary enlargement fails.
    """

    spec_by_row = []
    canonical_by_spec = []
    for local in fixture.locals_by_cell:
        row_specs = {}
        canonical = {}
        for column, spec in enumerate(local.specs):
            rows = tuple(
                map(
                    int,
                    np.flatnonzero(np.abs(local.encoding[:, column]) > 1.0e-14),
                )
            )
            canonical[spec] = rows[0]
            for row in rows:
                row_specs[row] = spec
        spec_by_row.append(row_specs)
        canonical_by_spec.append(canonical)

    edge_data = tuple(
        direct.physical_edge_data(
            fixture.code,
            tuple(local.body for local in fixture.locals_by_cell),
            edge,
        )
        for edge in PHYSICAL_EDGES
    )
    cell_blocks = tuple(
        tuple(
            sorted(
                {
                    block
                    for mode in range(6)
                    for block in carrier.route_b.BLOCKS_BY_CELL_MODE.get(
                        (cell, mode), ()
                    )
                }
            )
        )
        for cell in PHYSICAL_CELLS
    )
    rows = []
    for owner, edge in enumerate(PHYSICAL_EDGES):
        ports = tuple(sorted(edge_data[owner]["union"]))
        blocks = tuple(
            sorted(
                set(cell_blocks[edge.first_cell])
                | set(cell_blocks[edge.second_cell])
            )
        )
        sign_counts = defaultdict(Counter)
        examples = defaultdict(lambda: defaultdict(list))
        for label in direct.LABELS:
            history = list(fixture.vacuum_rows)
            for cell in direct.active_local_cells(label):
                history[cell] = canonical_by_spec[cell][
                    direct.local_spec(label, cell)
                ]
            by_cell = {
                cell: row
                for cell, row in enumerate(history)
                if fixture.locals_by_cell[cell].branches[row].number
            }
            source, source_chart = carrier.augmented_representative(
                fixture.code, fixture.locals_by_cell, by_cell
            )
            left_spec = spec_by_row[edge.first_cell][history[edge.first_cell]]
            right_spec = spec_by_row[edge.second_cell][history[edge.second_cell]]
            target_left, target_right, local_phase = carrier.swapped_specs(
                edge, left_spec, right_spec
            )
            target_history = list(history)
            target_history[edge.first_cell] = canonical_by_spec[edge.first_cell][
                target_left
            ]
            target_history[edge.second_cell] = canonical_by_spec[edge.second_cell][
                target_right
            ]
            target_by_cell = {
                cell: row
                for cell, row in enumerate(target_history)
                if fixture.locals_by_cell[cell].branches[row].number
            }
            target, target_chart = carrier.augmented_representative(
                fixture.code, fixture.locals_by_cell, target_by_cell
            )
            source_observation = carrier.bounded_observation(
                fixture.code, source, source_chart, ports, blocks
            )
            target_observation = carrier.bounded_observation(
                fixture.code, target, target_chart, ports, blocks
            )
            transition = target @ carrier.pauli_inverse(source)
            first, second = edge.modes
            mapping = list(range(72))
            mapping[first], mapping[second] = mapping[second], mapping[first]
            mapped = tuple(mapping[mode] for mode in label)
            car_phase = complex(carrier.c311.c308.permutation_sign(mapped))
            correction = int(round(float(np.real(car_phase / local_phase))))
            key = (
                source_observation,
                target_observation,
                int(transition.phase),
                int(transition.x),
                int(transition.z),
            )
            sign_counts[key][correction] += 1
            if len(examples[key][correction]) < 4:
                examples[key][correction].append(label)
        conflicts = [key for key, counts in sign_counts.items() if len(counts) > 1]
        rows.append(
            {
                "owner": owner,
                "bounded_sign_tag_rows": len(sign_counts),
                "sign_conflicted_rows": len(conflicts),
                "logical_columns_in_conflicted_rows": sum(
                    sum(sign_counts[key].values()) for key in conflicts
                ),
                "minimum_wrong_columns_for_any_single_tag_per_row": sum(
                    min(sign_counts[key].values()) for key in conflicts
                ),
                "conflict_sign_counts": tuple(
                    dict(sign_counts[key]) for key in conflicts
                ),
                "conflict_examples": tuple(
                    {
                        sign: tuple(examples[key][sign])
                        for sign in sorted(examples[key])
                    }
                    for key in conflicts
                ),
            }
        )
    return {
        "edge_rows": tuple(rows),
        "total_sign_conflicted_rows": sum(
            row["sign_conflicted_rows"] for row in rows
        ),
        "existing_bounded_owner_observation_repairs_all_CAR_signs": all(
            row["sign_conflicted_rows"] == 0 for row in rows
        ),
        "scope": (
            "the landed owner port-plus-q observation alphabet only; no claim "
            "against a different bounded gauge/auxiliary encoding"
        ),
    }


def canonical_frame_mode_map(source_axis: int, frame):
    target_axis, reverse, _cells, direction_map, direct_mode_map = direct.frame_action(
        source_axis, frame
    )
    source_direct = direct.UNION_COORDS[source_axis]
    target_direct = direct.UNION_COORDS[target_axis]
    source_canonical = canonical_cells(source_axis)
    target_canonical_index = {
        cell: index for index, cell in enumerate(canonical_cells(target_axis))
    }
    source_direct_index = {cell: index for index, cell in enumerate(source_direct)}
    mode_map = []
    for cell in source_canonical:
        source_index = source_direct_index[cell]
        for mode in range(6):
            mapped = direct_mode_map[6 * source_index + mode]
            target_cell = target_direct[mapped // 6]
            mode_map.append(6 * target_canonical_index[target_cell] + mapped % 6)
    return target_axis, reverse, direction_map, tuple(mode_map)


def actual_code_action_covariance():
    """Covariance of the code action induced by the executed endpoint ROM."""

    actual_streams = []
    target_streams = []
    for axis in range(3):
        actual = sparse.eye(len(direct.LABELS), format="csc", dtype=complex)
        target = sparse.eye(len(direct.LABELS), format="csc", dtype=complex)
        for edge in canonical_edges(axis):
            actual = local_tensor_edge(edge) @ actual
            target = direct.edge_stream(edge) @ target
        actual_streams.append(actual)
        target_streams.append(target)
    coin = direct.logical_coin()
    contact = direct.logical_contact()
    actual_updates = tuple(contact @ stream @ coin for stream in actual_streams)
    target_updates = tuple(contact @ stream @ coin for stream in target_streams)
    actual_residuals = []
    target_residuals = []
    representation_residuals = []
    for frame in direct.FRAMES:
        axis, _reverse, _direction_map, mode_map = canonical_frame_mode_map(0, frame)
        representation = direct.mode_permutation(mode_map)
        identity = sparse.eye(len(direct.LABELS), format="csc", dtype=complex)
        representation_residuals.append(
            c315.largest_singular(
                representation.conj().T @ representation - identity
            )
        )
        actual_residuals.append(
            c315.largest_singular(
                representation @ actual_updates[0]
                - actual_updates[axis] @ representation
            )
        )
        target_residuals.append(
            c315.largest_singular(
                representation @ target_updates[0]
                - target_updates[axis] @ representation
            )
        )

    group_failures = 0
    for left in direct.FRAMES:
        for right in direct.FRAMES:
            middle_axis, _reverse, _directions, right_map = canonical_frame_mode_map(
                0, right
            )
            target_axis, _reverse, _directions, left_map = canonical_frame_mode_map(
                middle_axis, left
            )
            product_axis, _reverse, _directions, product_map = canonical_frame_mode_map(
                0, direct.matmul(left, right)
            )
            composed = tuple(left_map[right_map[mode]] for mode in range(72))
            group_failures += target_axis != product_axis or composed != product_map
    return {
        "proper_cubic_frames": len(direct.FRAMES),
        "frame_products": len(direct.FRAMES) ** 2,
        "frame_representation_group_failures": group_failures,
        "maximum_representation_unitarity": max(representation_residuals),
        "target_CAR_update_maximum_covariance_residual": max(target_residuals),
        "executed_endpoint_ROM_maximum_covariance_residual": max(actual_residuals),
        "executed_endpoint_ROM_failed_frames": sum(
            residual > TOL for residual in actual_residuals
        ),
        "lexicographic_order_runtime_service_used": False,
        "lexicographic_order_role": (
            "offline sparse-row and mode-basis bookkeeping; its parity cocycle "
            "is not supplied to the physical ROM"
        ),
    }


def execute_composition(length: int):
    fixture = build_global_fixture(length)
    # The already executed bounded qutrit-refresh coin obeys C_p E=E C on
    # this same encoding.  Start from its exact output.  Inductively, every
    # following residual is therefore (U_s E-E G_s) C; right multiplication
    # by the unitary coin preserves Frobenius and operator norms.
    coin = direct.logical_coin()
    state = (fixture.encoding @ coin).tocsc()
    logical = coin.copy()
    actual_logical = coin.copy()
    target_seam = sparse.eye(len(direct.LABELS), format="csc", dtype=complex)
    actual_seam = sparse.eye(len(direct.LABELS), format="csc", dtype=complex)
    stage_rows = []
    rng = np.random.default_rng(659500 + length)
    for edge_index, edge in enumerate(PHYSICAL_EDGES):
        operator, details = global_owner_operator(fixture, edge_index)
        random = rng.normal(size=operator.shape[0]) + 1.0j * rng.normal(
            size=operator.shape[0]
        )
        random /= np.linalg.norm(random)
        inverse_residual = float(
            np.linalg.norm(operator.conj().T @ (operator @ random) - random)
        )
        state = (operator @ state).tocsc()
        state.data[np.abs(state.data) < 2.0e-12] = 0
        state.eliminate_zeros()
        logical = direct.edge_stream(edge) @ logical
        target_seam = direct.edge_stream(edge) @ target_seam
        local_action = local_tensor_edge(edge)
        actual_logical = local_action @ actual_logical
        actual_seam = local_action @ actual_seam
        target = fixture.encoding @ logical
        difference = state - target
        executed_action_difference = state - fixture.encoding @ actual_logical
        details.update(
            {
                "state_nonzeros": state.nnz,
                "stage_intertwiner_norm": matrix_norm(difference),
                "stage_intertwiner_raw": max_abs(difference),
                "executed_ROM_minus_E_local_tensor_action_norm": matrix_norm(
                    executed_action_difference
                ),
                "randomized_physical_inverse_residual": inverse_residual,
                "missing_sign": edge_sign_inventory(edge),
            }
        )
        stage_rows.append(details)

    contact = physical_contact(fixture)
    state = (contact @ state).tocsc()
    logical = direct.logical_contact() @ logical
    actual_logical = direct.logical_contact() @ actual_logical
    target = fixture.encoding @ logical
    difference = state - target
    actual_action_difference = state - fixture.encoding @ actual_logical
    projected = fixture.encoding @ (fixture.encoding.conj().T @ state)
    leakage = state - projected
    seam_cocycle = target_seam.conj().T @ actual_seam
    seam_cocycle_diagonal = seam_cocycle.diagonal()
    seam_cocycle_off_diagonal = seam_cocycle - sparse.diags(
        seam_cocycle_diagonal, format="csc"
    )
    one_indices = [direct.LABEL_INDEX[(mode,)] for mode in range(72)]
    actual_one_particle = actual_logical[np.ix_(one_indices, one_indices)]
    uniform = np.ones(72, dtype=complex) / math.sqrt(72)
    eigenvalue = np.vdot(uniform, actual_one_particle @ uniform)
    return {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "physical_rows": fixture.encoding.shape[0],
        "logical_columns": fixture.encoding.shape[1],
        "encoding_nonzeros": fixture.encoding.nnz,
        "stage_rows": stage_rows,
        "contact_physical_nonzeros": contact.nnz,
        "final_state_nonzeros": state.nnz,
        "physical_coin_composition": (
            "start from the independently executed exact equality C_p E=E C; "
            "then multiply every physical seam and contact on that common output"
        ),
        "coin_stage_intertwiner_imported_residual": 0.0,
        "U_physical_E_minus_E_G_target_norm": matrix_norm(difference),
        "U_physical_E_minus_E_G_target_raw": max_abs(difference),
        "U_physical_E_minus_E_G_target_opnorm": c315.largest_singular(difference),
        "physical_code_leakage_norm": matrix_norm(leakage),
        "physical_code_leakage_raw": max_abs(leakage),
        "physical_code_leakage_opnorm": c315.largest_singular(leakage),
        "executed_ROM_minus_E_local_tensor_update_norm": matrix_norm(
            actual_action_difference
        ),
        "final_missing_signed_permutation_negative_columns_before_coin": int(
            np.count_nonzero(np.abs(seam_cocycle_diagonal + 1.0) < TOL)
        ),
        "final_missing_signed_permutation_off_diagonal_nonzeros_before_coin": (
            seam_cocycle_off_diagonal.nnz
        ),
        "comparator_work_nonblank_norm": 0.0,
        "comparator_work_return_failures": 0,
        "target": "physical contact times eleven ordered owned seams",
        "one_particle_mass": float(np.angle(eigenvalue))
        / direct.c330.c219.C_SQUARED,
        "Cycle219_mass_fixture": direct.c330.c219.rest_mass(
            direct.c330.c219.common_species(-0.3)
        ),
        "one_particle_eigen_residual": float(
            np.linalg.norm(actual_one_particle @ uniform - eigenvalue * uniform)
        ),
        "Gram_or_isometry_used_as_intertwiner": False,
        "dense_EUE_completion_used": False,
    }


def main() -> None:
    rows = tuple(execute_composition(length) for length in (5, 6))
    sign_audits = tuple(
        bounded_sign_tag_audit(build_global_fixture(length)) for length in (5, 6)
    )
    covariance = actual_code_action_covariance()
    translations = tuple(
        carrier.translated_two_star_fixture_control(length) for length in (5, 6)
    )
    print("COMMON_E_ORDERED_PHYSICAL_ROM_COMPOSITION")
    for row in rows:
        print("composition", row)
    for length, audit in zip((5, 6), sign_audits):
        print("bounded_sign_tag_audit", length, audit)
    print("physical_code_action_covariance", covariance)
    for translation in translations:
        print("translation", translation)
    for row in rows:
        assert row["physical_rows"] == 59941
        assert row["logical_columns"] == 2629
        assert row["encoding_nonzeros"] == 59941
        assert len(row["stage_rows"]) == 11
        assert all(stage["pair_ROM_gates"] == 97 for stage in row["stage_rows"])
        assert all(stage["missing_target_histories"] == 0 for stage in row["stage_rows"])
        assert max(
            stage["executed_ROM_minus_E_local_tensor_action_norm"]
            for stage in row["stage_rows"]
        ) < TOL
        assert max(
            stage["randomized_physical_inverse_residual"]
            for stage in row["stage_rows"]
        ) < TOL
        assert row["U_physical_E_minus_E_G_target_norm"] > 30.0
        assert row["U_physical_E_minus_E_G_target_opnorm"] > 1.9
        assert row["physical_code_leakage_norm"] < TOL
        assert row["executed_ROM_minus_E_local_tensor_update_norm"] < TOL
        assert row[
            "final_missing_signed_permutation_negative_columns_before_coin"
        ] == 240
        assert row[
            "final_missing_signed_permutation_off_diagonal_nonzeros_before_coin"
        ] == 0
        assert row["comparator_work_nonblank_norm"] == 0
        assert row["comparator_work_return_failures"] == 0
        assert abs(row["one_particle_mass"] - row["Cycle219_mass_fixture"]) < TOL
        assert row["one_particle_eigen_residual"] < TOL
        assert not row["Gram_or_isometry_used_as_intertwiner"]
        assert not row["dense_EUE_completion_used"]
    for audit in sign_audits:
        assert audit["total_sign_conflicted_rows"] == 14
        assert not audit[
            "existing_bounded_owner_observation_repairs_all_CAR_signs"
        ]
        assert [
            row["minimum_wrong_columns_for_any_single_tag_per_row"]
            for row in audit["edge_rows"]
        ] == [40, 20, 10, 10, 0, 0, 20, 10, 10, 0, 0]
    assert covariance["proper_cubic_frames"] == 24
    assert covariance["frame_products"] == 576
    assert covariance["frame_representation_group_failures"] == 0
    assert covariance["target_CAR_update_maximum_covariance_residual"] < TOL
    assert covariance["executed_endpoint_ROM_maximum_covariance_residual"] > 1.9
    assert covariance["executed_endpoint_ROM_failed_frames"] > 0
    assert not covariance["lexicographic_order_runtime_service_used"]
    for translation in translations:
        assert translation["translations"] == translation["L"] ** 3
        assert translation["translated_owner_fixtures"] == 11 * translation["L"] ** 3
        assert translation["translation_chart_ambiguities"] == 0
        assert translation["translation_invalid_qutrit_words"] == 0
        assert translation["translation_duplicate_chart_failures"] == 0
        assert translation["translation_carrier_coefficient_mismatches"] == 0
        assert translation["all_torus_translations_tested"]
        assert not translation["recurrent_update_claimed"]
    print(
        "ROUTE_A_ACTUAL_COMMON_E_COMPOSITION_FALSIFIED_BY_UNSUPPLIED_CAR_PARITY_COCYCLE"
    )


if __name__ == "__main__":
    main()
