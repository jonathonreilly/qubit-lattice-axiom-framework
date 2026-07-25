#!/usr/bin/env python3
"""Cycle-655/656 refresh of the two-star half-edge feature code.

This runner replaces the failed frozen-copy coin attempt by a factorized
bounded word.  Each cell has a seven-rail one-hot carrier register.  Outside
the one-particle sector the sentinel rail is occupied.  In the one-particle
sector a supplied five-Givens preparation puts the carrier on one of the five
unoccupied directions with the exact landed Cycle-311 amplitudes.  The six
half-edge qutrit charts are then reversible Boolean functions of decoded
occupation and carrier rails.

The physical word is compositional rather than a dense code completion:

    Cycle655 decode ; W_A^dag ; erase charts ; erase carrier
    ; decoded coin ; prepare carrier ; recompute charts
    ; W_A ; register contact ; Cycle655 encode.

The same charted encoding occurs on both sides.  The runner executes the
compressed graph-code coin/contact intertwiner on the complete two-star n<=2 basis and
binds every nontrivial stage to explicit one/two-M2 factors, the Cycle-656
clean selector/token convention, and a supplied finite ordinal.  The ordinal
is circuit order, not physical time.  No minimum, impossibility, shared
obstruction, or axiom-pressure claim is made.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import json
import math
import resource
import time

import numpy as np
from scipy import sparse

import frontier_full128_cycle_cocycle_intertwiner_2026_07_24 as c655
import frontier_full128_two_rail_fixed_law_core_2026_07_24 as c656
import frontier_two_overlapping_star_sparse_qutrit_edge_gauge_core_2026_07_25 as qcore
import frontier_two_star_qutrit_physical_update_integration_2026_07_25 as previous
import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import frontier_two_star_staggered_endpoint_feature_route_c_2026_07_25 as route_c


START = time.perf_counter()
TOL = 4.0e-10
PASS = 0
FAIL = 0
SENTINEL = 6
ROLE_RAILS = 7
MATCH_Q_BITS = 6
MATCH_SCRATCH = 5


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def raw_maximum(matrix: sparse.spmatrix | np.ndarray) -> float:
    if sparse.issparse(matrix):
        return float(np.max(np.abs(matrix.data))) if matrix.nnz else 0.0
    return float(np.max(np.abs(matrix))) if matrix.size else 0.0


def role_amplitudes(length: int) -> dict[tuple[int, int], complex]:
    """Exact one-particle carrier amplitudes in the landed chart convention."""
    code = c315.c269.build_code(length)
    body = (1, 1, 1)
    rows: dict[tuple[int, int], complex] = {}
    for occupied in range(6):
        branches = c311.common_branches(code, body, 1, (occupied,), 0)
        for branch in branches:
            if branch.carrier_direction is None:
                raise AssertionError("one-particle branch has no carrier")
            rows[(occupied, branch.carrier_direction)] = complex(branch.amplitude)
    return rows


_RAW_ROLE_AMPLITUDES = role_amplitudes(5)
ROLE_AMPLITUDES = {
    (occupied, carrier): _RAW_ROLE_AMPLITUDES[(occupied, carrier)]
    / math.sqrt(sum(
        abs(_RAW_ROLE_AMPLITUDES[(occupied, other)]) ** 2
        for other in range(6) if other != occupied
    ))
    for occupied in range(6) for carrier in range(6) if carrier != occupied
}


def target_role_vector(occupied: int) -> np.ndarray:
    target = np.zeros(ROLE_RAILS, dtype=complex)
    for carrier in range(6):
        if carrier != occupied:
            target[carrier] = ROLE_AMPLITUDES[(occupied, carrier)]
    return target


def givens_preparation(occupied: int) -> tuple[tuple[int, np.ndarray], ...]:
    """Five two-rail factors mapping the sentinel excitation to the target."""
    target = target_role_vector(occupied)
    carriers = tuple(carrier for carrier in range(6) if carrier != occupied)
    reservoir = 1.0
    factors = []
    for index, carrier in enumerate(carriers):
        amplitude = target[carrier]
        remaining = (
            0.0 if index == len(carriers) - 1
            else math.sqrt(max(0.0, reservoir * reservoir - abs(amplitude) ** 2))
        )
        a = remaining / reservoir
        b = amplitude / reservoir
        two_level = np.asarray(((a, -np.conj(b)), (b, a)), dtype=complex)
        factors.append((carrier, two_level))
        reservoir = remaining
    return tuple(factors)


ROLE_PREPARATIONS = tuple(givens_preparation(occupied) for occupied in range(6))


def apply_two_level(
    state: np.ndarray, carrier: int, matrix: np.ndarray
) -> np.ndarray:
    result = state.copy()
    result[[SENTINEL, carrier]] = matrix @ state[[SENTINEL, carrier]]
    return result


def prepared_role(occupied: int, reverse: bool = False) -> np.ndarray:
    state = np.zeros(ROLE_RAILS, dtype=complex)
    state[SENTINEL] = 1.0
    word = ROLE_PREPARATIONS[occupied]
    if not reverse:
        for carrier, matrix in word:
            state = apply_two_level(state, carrier, matrix)
        return state
    state = target_role_vector(occupied)
    for carrier, matrix in reversed(word):
        state = apply_two_level(state, carrier, matrix.conj().T)
    return state


def two_M2_matrix(matrix: np.ndarray) -> np.ndarray:
    """Vacuum- and double-occupation-fixed lift of one two-rail factor."""
    lifted = np.eye(4, dtype=complex)
    lifted[np.ix_((1, 2), (1, 2))] = matrix
    return lifted


def feature_word(occupied_modes: tuple[int, ...], carrier: int, mode: int) -> int:
    occupied = int(mode in occupied_modes)
    outer = int(len(occupied_modes) == 1 and carrier == mode)
    return qcore.qutrit_word(outer, occupied)


def local_landed_chart_census(length: int) -> dict[str, object]:
    code = c315.c269.build_code(length)
    body = (1, 1, 1)
    amplitude_errors = chart_errors = invalid = cases = 0
    for number, label in c311.FOCK_LABELS:
        if number > 2:
            continue
        for branch in c311.common_branches(code, body, number, label, 0):
            carrier = SENTINEL if branch.carrier_direction is None else branch.carrier_direction
            if number == 1:
                amplitude_errors += abs(
                    branch.amplitude - ROLE_AMPLITUDES[(label[0], carrier)]
                ) > TOL
            for mode in range(6):
                representative = c311.branch_representative(code, body, branch, 0)
                vertex = c311.c305.body_vertices(code, body)[mode]
                _arrival, outer_edge = c311.local.old.outer_partner(code, vertex)
                observed = qcore.qutrit_word(
                    (representative.x >> outer_edge) & 1,
                    (representative.x >> (code.qubits + vertex)) & 1,
                )
                predicted = feature_word(label, carrier, mode)
                chart_errors += observed != predicted
                invalid += predicted not in qcore.LAWFUL_QUTRIT_WORDS
                cases += 1
    return {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "branch_half_edge_cases": cases,
        "amplitude_table_errors": amplitude_errors,
        "chart_errors": chart_errors,
        "invalid_qutrit_words": invalid,
    }


def patch_branch_rows(length: int) -> tuple[dict[str, object], sparse.csc_matrix]:
    """Compressed role/chart graph encoding for the full two-star basis."""
    amplitudes = role_amplitudes(length)
    row_by_key: dict[tuple[object, ...], int] = {}
    rows = []
    columns = []
    values = []
    invalid = equality_failures = 0
    maximum_branches = 0

    for column, label in enumerate(route_c.FOCK_BASIS):
        occupied_by_cell = defaultdict(list)
        for global_mode in label:
            cell, mode = divmod(global_mode, 6)
            occupied_by_cell[cell].append(mode)
        choices = []
        for cell in range(len(route_c.BASE_CELLS)):
            local = tuple(occupied_by_cell.get(cell, ()))
            if len(local) == 1:
                occupied = local[0]
                choices.append(tuple(
                    (carrier, amplitudes[(occupied, carrier)])
                    for carrier in range(6) if carrier != occupied
                ))
            else:
                choices.append(((SENTINEL, 1.0 + 0.0j),))

        branch_count = 0
        for role_choices in product(*choices):
            roles = tuple(row[0] for row in role_choices)
            amplitude = complex(np.prod([row[1] for row in role_choices]))
            chart = []
            for _star, _direction, _endpoint, cell_coord, mode in previous.FEATURE_BLOCKS:
                cell = route_c.BASE_CELLS.index(cell_coord)
                local = tuple(occupied_by_cell.get(cell, ()))
                chart.append(feature_word(local, roles[cell], mode))
            chart_tuple = tuple(chart)
            invalid += sum(word not in qcore.LAWFUL_QUTRIT_WORDS for word in chart_tuple)
            for duplicate in previous.DUPLICATE_ROWS.values():
                equality_failures += chart_tuple[duplicate[0]] != chart_tuple[duplicate[1]]
            key = (label, roles, chart_tuple)
            row = row_by_key.setdefault(key, len(row_by_key))
            rows.append(row)
            columns.append(column)
            values.append(amplitude)
            branch_count += 1
        maximum_branches = max(maximum_branches, branch_count)

    encoding = sparse.coo_matrix(
        (values, (rows, columns)),
        shape=(len(row_by_key), len(route_c.FOCK_BASIS)),
        dtype=complex,
    ).tocsc()
    gram = encoding.conj().T @ encoding - sparse.eye(encoding.shape[1], format="csc")
    return {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "logical_columns_n_le_2": encoding.shape[1],
        "physical_role_chart_rays": encoding.shape[0],
        "encoding_nonzeros": encoding.nnz,
        "maximum_branches_per_column": maximum_branches,
        "invalid_qutrit_words": invalid,
        "shared_copy_equality_failures": equality_failures,
        "Gram_raw_maximum": raw_maximum(gram),
        "zero_columns": sum(encoding.getcol(column).nnz == 0 for column in range(encoding.shape[1])),
    }, encoding


def factorized_intertwiner(
    encoding: sparse.csc_matrix, logical: sparse.csc_matrix
) -> dict[str, float]:
    """Residual of prepare * logical * unprepare on the declared graph code."""
    identity = sparse.eye(encoding.shape[1], format="csc")
    gram = encoding.conj().T @ encoding
    # E G - (E G E^dag) E = E G (I-E^dag E).  The displayed factorization
    # is the circuit prepare/update/unprepare, not an ambient dense completion.
    compressed = logical @ (identity - gram)
    leakage_compressed = logical - gram @ logical
    return {
        "intertwiner_raw_maximum": raw_maximum(compressed),
        "intertwiner_opnorm": c315.largest_singular(compressed),
        "code_leakage_raw_maximum": raw_maximum(leakage_compressed),
        "code_leakage_opnorm": c315.largest_singular(leakage_compressed),
    }


def match_pattern(
    pattern: tuple[int, ...], supplied: tuple[int, ...], token: int,
    scratch: tuple[int, ...] | None = None, flag: int = 0,
) -> tuple[int, tuple[int, ...], int]:
    """Six-data-bit specialization of the Cycle-656 clean match chain."""
    if len(pattern) != MATCH_Q_BITS or len(supplied) != MATCH_Q_BITS:
        raise ValueError("six decoded occupation bits are required")
    initial = (0,) * MATCH_SCRATCH if scratch is None else scratch
    if len(initial) != MATCH_SCRATCH:
        raise ValueError("matcher scratch width changed")
    controls = [int(token)] + list(supplied)
    for index, expected in enumerate(pattern, start=1):
        if expected == 0:
            controls[index] ^= 1
    work = list(initial)
    work[0] ^= controls[0] & controls[1]
    for index in range(2, len(controls) - 1):
        work[index - 1] ^= work[index - 2] & controls[index]
    flag ^= work[-1] & controls[-1]
    fired = flag
    flag ^= work[-1] & controls[-1]
    for index in reversed(range(2, len(controls) - 1)):
        work[index - 1] ^= work[index - 2] & controls[index]
    work[0] ^= controls[0] & controls[1]
    return fired, tuple(work), flag


def matcher_and_role_resources() -> dict[str, object]:
    match_failures = reset_failures = zero_fires = cases = 0
    for occupied in range(6):
        pattern = tuple(int(bit == occupied) for bit in range(6))
        for supplied_int in range(64):
            supplied = tuple((supplied_int >> bit) & 1 for bit in range(6))
            fired, scratch, flag = match_pattern(pattern, supplied, 1)
            match_failures += fired != int(supplied_int == (1 << occupied))
            reset_failures += scratch != (0,) * MATCH_SCRATCH or flag != 0
            zero, scratch0, flag0 = match_pattern(pattern, supplied, 0)
            zero_fires += zero != 0
            reset_failures += scratch0 != (0,) * MATCH_SCRATCH or flag0 != 0
            cases += 1

    maximum_prep = maximum_inverse = maximum_gate_unitarity = 0.0
    maximum_bypass = maximum_bypass_leakage = 0.0
    deletion_residual = reverse_order_residual = 0.0
    role_factors = 0
    for occupied in range(6):
        observed = prepared_role(occupied)
        restored = prepared_role(occupied, reverse=True)
        maximum_prep = max(maximum_prep, float(np.linalg.norm(
            observed - target_role_vector(occupied)
        )))
        sentinel = np.zeros(ROLE_RAILS, dtype=complex)
        sentinel[SENTINEL] = 1.0
        maximum_inverse = max(maximum_inverse, float(np.linalg.norm(restored - sentinel)))
        state = sentinel.copy()
        for carrier, matrix in ROLE_PREPARATIONS[occupied][1:]:
            state = apply_two_level(state, carrier, matrix)
        deletion_residual = max(
            deletion_residual, float(np.linalg.norm(state - target_role_vector(occupied)))
        )
        state = sentinel.copy()
        for carrier, matrix in reversed(ROLE_PREPARATIONS[occupied]):
            state = apply_two_level(state, carrier, matrix)
        reverse_order_residual = max(
            reverse_order_residual, float(np.linalg.norm(state - target_role_vector(occupied)))
        )
        for _carrier, matrix in ROLE_PREPARATIONS[occupied]:
            role_factors += 1
            lifted = two_M2_matrix(matrix)
            maximum_gate_unitarity = max(
                maximum_gate_unitarity,
                float(np.linalg.norm(lifted.conj().T @ lifted - np.eye(4))),
            )
            bypass, leakage = c655.S.ideal_bypass(lifted, 2)
            maximum_bypass = max(maximum_bypass, float(bypass))
            maximum_bypass_leakage = max(maximum_bypass_leakage, float(leakage))

    dirty = (0,) * (MATCH_SCRATCH - 1) + (1,)
    dirty_false_fires = 0
    for occupied in range(6):
        pattern = tuple(int(bit == occupied) for bit in range(6))
        fired, _scratch, _flag = match_pattern(pattern, (0,) * 6, 0, dirty)
        dirty_false_fires += fired != 0
    dirty_bypass_change = max(
        float(np.linalg.norm(two_M2_matrix(matrix)[:, basis] - np.eye(4)[:, basis]))
        for word in ROLE_PREPARATIONS for _carrier, matrix in word for basis in (1, 2)
    )
    toffoli_residual, fredkin_residual = c655.S.local_decomposition_residuals()
    # One pattern flag is computed once per occupied direction and controls
    # five two-rail factors.  Cycle-656 decomposes each Toffoli/Fredkin into
    # one/two-M2 factors and routes those factors along a finite station column.
    return {
        "clean_match_cases": cases,
        "clean_match_failures": match_failures,
        "clean_match_reset_failures": reset_failures,
        "token_zero_fires": zero_fires,
        "role_Givens_factors_per_prepare": role_factors,
        "role_Givens_factors_per_unprepare": role_factors,
        "maximum_role_preparation_residual": maximum_prep,
        "maximum_role_inverse_residual": maximum_inverse,
        "maximum_role_factor_unitarity_residual": maximum_gate_unitarity,
        "maximum_vacuum_bypass_residual": maximum_bypass,
        "maximum_vacuum_bypass_leakage": maximum_bypass_leakage,
        "deleted_first_factor_residual": deletion_residual,
        "reversed_factor_order_residual": reverse_order_residual,
        "dirty_match_false_fires": dirty_false_fires,
        "dirty_bypass_change": dirty_bypass_change,
        "Toffoli_decomposition_residual": toffoli_residual,
        "Fredkin_decomposition_residual": fredkin_residual,
        "matcher_controls_including_token": 7,
        "matcher_scratch_M2": MATCH_SCRATCH,
        "matcher_flag_M2": 1,
        "bypass_M2": 2,
        "primitive_arity_after_Cycle656_expansion": 2,
    }


def fixed_word_schedule() -> dict[str, object]:
    cell_count = len(route_c.BASE_CELLS)
    coin_factors = tuple(
        gate for gate in c655.S.DECODED_GATES if gate.kind.startswith("coin")
    )
    stages = (
        ("Cycle655_decode", cell_count * len(c655.DECODE_WORD)),
        ("pair_register_unprepare", cell_count * len(c655.UNPREPARE_WORD)),
        ("erase_half_edge_charts", 2 * len(previous.FEATURE_BLOCKS)),
        ("erase_carrier_roles", cell_count * 30),
        ("six_mode_coin_factors", cell_count * len(coin_factors)),
        ("prepare_carrier_roles", cell_count * 30),
        ("recompute_half_edge_charts", 2 * len(previous.FEATURE_BLOCKS)),
        ("pair_register_prepare", cell_count * len(c655.PREPARE_WORD)),
        ("ordered_pair_contact", cell_count * len(c655.CONTACT_WORD)),
        ("Cycle655_encode", cell_count * len(c655.ENCODE_WORD)),
    )
    total = sum(count for _stage, count in stages)
    lawful_history = tuple(range(total))
    offset_history = tuple(range(1, total)) + (0,)
    trace = sha256(repr((stages, lawful_history[:4], lawful_history[-4:])).encode()).hexdigest()

    genesis = c656.E_COMBINED.encode("charted_E_full|psi>")
    final, orbit = c656.run_orbit(c656.A_AUTO, genesis)
    packet = final.a_packets[0]
    return {
        "fixed_stage_factors_before_primitive_expansion": total,
        "stage_inventory": stages,
        "station_zero_token": 1,
        "station_zero_return": 0,
        "selected_factor_ordinals": len(lawful_history),
        "lawful_history_head": lawful_history[:4],
        "lawful_history_tail": lawful_history[-4:],
        "offset_history_differs": offset_history != lawful_history,
        "zero_token_selected_events": 0,
        "two_token_selected_events": 2 * total,
        "program_ordinal_is_physical_time": False,
        "runtime_measurements": 0,
        "runtime_parity_queries": 0,
        "runtime_order_queries": 0,
        "schedule_sha256": trace,
        "Cycle656_base_selected_events": orbit.selected_events,
        "Cycle656_base_return_station": next(
            station for station, row in enumerate(final.a_packets) if row.token
        ),
        "Cycle656_base_factor_order_ok": packet.factors == tuple(range(c656.T)),
        "Cycle656_base_program_failures": orbit.program_change_failures,
        "Cycle656_base_ancilla_failures": orbit.ancilla_change_failures,
        "Cycle656_base_B_vacuum_failures": orbit.b_vacuum_failures,
    }


def carrier_covariance() -> dict[str, object]:
    frame_failures = product_failures = chart_failures = 0
    frame_cases = product_cases = 0
    mappings = []
    for frame in c655.P.FRAMES:
        mapping = tuple(int(value) for value in c655.P.mode_map(frame))
        mappings.append(mapping)
        for occupied in range(6):
            for carrier in range(6):
                if carrier == occupied:
                    continue
                mapped_occupied = mapping[occupied]
                mapped_carrier = mapping[carrier]
                eta = (
                    ROLE_AMPLITUDES[(mapped_occupied, mapped_carrier)]
                    / ROLE_AMPLITUDES[(occupied, carrier)]
                )
                frame_failures += abs(abs(eta) - 1.0) > TOL
                for mode in range(6):
                    source = feature_word((occupied,), carrier, mode)
                    target = feature_word(
                        (mapped_occupied,), mapped_carrier, mapping[mode]
                    )
                    chart_failures += source != target
                frame_cases += 1
    for left_index, left in enumerate(c655.P.FRAMES):
        left_map = mappings[left_index]
        for right_index, right in enumerate(c655.P.FRAMES):
            right_map = mappings[right_index]
            product_frame = left @ right
            target_index = next(
                index for index, frame in enumerate(c655.P.FRAMES)
                if np.array_equal(frame, product_frame)
            )
            target_map = mappings[target_index]
            for occupied in range(6):
                for carrier in range(6):
                    if carrier == occupied:
                        continue
                    mid_i, mid_c = right_map[occupied], right_map[carrier]
                    direct = (
                        ROLE_AMPLITUDES[(target_map[occupied], target_map[carrier])]
                        / ROLE_AMPLITUDES[(occupied, carrier)]
                    )
                    staged = (
                        ROLE_AMPLITUDES[(mid_i, mid_c)]
                        / ROLE_AMPLITUDES[(occupied, carrier)]
                        * ROLE_AMPLITUDES[(left_map[mid_i], left_map[mid_c])]
                        / ROLE_AMPLITUDES[(mid_i, mid_c)]
                    )
                    product_failures += abs(direct - staged) > TOL
                    product_cases += 1
    return {
        "proper_cubic_frames": len(c655.P.FRAMES),
        "carrier_frame_cases": frame_cases,
        "carrier_phase_failures": frame_failures,
        "chart_transport_failures": chart_failures,
        "ordered_frame_products": len(c655.P.FRAMES) ** 2,
        "carrier_cocycle_product_cases": product_cases,
        "carrier_cocycle_product_failures": product_failures,
    }


def physical_factor_bindings() -> dict[str, object]:
    coin_gates = tuple(
        gate for gate in c655.S.DECODED_GATES if gate.kind.startswith("coin")
    )
    observed_coin = c655.S.product_on_seven(coin_gates)
    target_coin = np.asarray(c655.P.coarse_factors(1)["coin"])
    coin_residual = float(np.linalg.norm(observed_coin - target_coin))
    register_contact, port_contact, sectors = c655.register_contact_identity()
    pair_matrix, pair_prepare, pair_inverse = c655.pair_gadget_matrix()
    decoder_residual = int(np.max(np.abs(
        (c655.P.DECODER @ c655.P.ENCODER) % 2 - np.eye(22, dtype=np.uint8)
    )))
    return {
        "Cycle655_word_sha256": c655.word_digest(c655.COMBINED_WORD),
        "Cycle655_decode_NN_gates_per_cell": len(c655.DECODE_WORD),
        "Cycle655_encode_NN_gates_per_cell": len(c655.ENCODE_WORD),
        "pair_unprepare_NN_gates_per_cell": len(c655.UNPREPARE_WORD),
        "pair_prepare_NN_gates_per_cell": len(c655.PREPARE_WORD),
        "contact_onsite_gates_per_cell": len(c655.CONTACT_WORD),
        "coin_decoded_factors_per_cell": len(coin_gates),
        "coin_factor_residual": coin_residual,
        "pair_preparation_residual": pair_prepare,
        "pair_inverse_residual": pair_inverse,
        "pair_matrix_shape": pair_matrix.shape,
        "register_contact_residual": register_contact,
        "port_contact_residual": port_contact,
        "contact_sector_residuals": sectors,
        "decoder_encoder_GF2_residual": decoder_residual,
        "cross_cell_seam_factor": "not bound: the first local seam-role map is diagnosed separately",
        "cross_cell_seam_owners_supplied": len(route_c.BASE_EDGES),
        "dense_augmented_code_completion_used": False,
    }


def seam_candidate_diagnostic() -> dict[str, object]:
    """First attempted local seam map after the successful coin refresh.

    An ordinary endpoint FSWAP on each owned edge misses the exterior signs of
    the supplied Route-C basis.  Prepending the eleven qutrit sign circuits is
    also insufficient: their phase is carrier-dependent on some graph-code
    columns, so W_role^dag leaks before the occupation swap is reached.
    """
    mapping = list(range(route_c.MODE_COUNT))
    edge_modes = []
    for left, right in route_c.BASE_EDGES:
        direction = route_c.sub(right, left)
        left_mode = (
            6 * route_c.BASE_CELLS.index(left)
            + route_c.DIRECTION_INDEX[direction]
        )
        right_mode = (
            6 * route_c.BASE_CELLS.index(right)
            + route_c.DIRECTION_INDEX[tuple(-value for value in direction)]
        )
        mapping[left_mode], mapping[right_mode] = mapping[right_mode], mapping[left_mode]
        edge_modes.append((left, right, left_mode, right_mode))

    target_rows = []
    direct_rows = []
    target_phases = []
    direct_phases = []
    direct_mismatches = 0
    q_phase_ambiguous_columns = 0
    q_effective_diagonal = []
    q_maximum_leakage = 0.0
    q_branch_cases = 0
    for label in route_c.FOCK_BASIS:
        mapped = tuple(mapping[mode] for mode in label)
        target_phase = c311.c308.permutation_sign(mapped)
        direct_phase = 1
        for _left, _right, left_mode, right_mode in edge_modes:
            if left_mode in label and right_mode in label:
                direct_phase *= -1
        target_rows.append(route_c.FOCK_INDEX[tuple(sorted(mapped))])
        direct_rows.append(route_c.FOCK_INDEX[tuple(sorted(mapped))])
        target_phases.append(target_phase)
        direct_phases.append(direct_phase)
        direct_mismatches += direct_phase != target_phase

        occupied_by_cell = defaultdict(list)
        for global_mode in label:
            cell, mode = divmod(global_mode, 6)
            occupied_by_cell[cell].append(mode)
        choices = []
        for cell in range(len(route_c.BASE_CELLS)):
            local = tuple(occupied_by_cell.get(cell, ()))
            if len(local) == 1:
                occupied = local[0]
                choices.append(tuple(
                    (carrier, ROLE_AMPLITUDES[(occupied, carrier)])
                    for carrier in range(6) if carrier != occupied
                ))
            else:
                choices.append(((SENTINEL, 1.0 + 0.0j),))

        branch_phases = []
        effective = 0.0
        for role_choices in product(*choices):
            roles = tuple(row[0] for row in role_choices)
            probability = abs(complex(np.prod([row[1] for row in role_choices]))) ** 2
            phase = 1
            for left, right, _left_global, _right_global in edge_modes:
                left_cell = route_c.BASE_CELLS.index(left)
                right_cell = route_c.BASE_CELLS.index(right)
                direction = route_c.sub(right, left)
                left_local = route_c.DIRECTION_INDEX[direction]
                right_local = route_c.DIRECTION_INDEX[
                    tuple(-value for value in direction)
                ]
                left_word = feature_word(
                    tuple(occupied_by_cell.get(left_cell, ())),
                    roles[left_cell], left_local,
                )
                right_word = feature_word(
                    tuple(occupied_by_cell.get(right_cell, ())),
                    roles[right_cell], right_local,
                )
                if qcore.branch_sign_bit(left_word, right_word):
                    phase *= -1
            branch_phases.append(phase)
            effective += probability * phase
            q_branch_cases += 1
        q_phase_ambiguous_columns += len(set(branch_phases)) > 1
        q_effective_diagonal.append(effective)
        q_maximum_leakage = max(
            q_maximum_leakage,
            math.sqrt(max(0.0, 1.0 - abs(effective) ** 2)),
        )

    target = sparse.coo_matrix(
        (target_phases, (target_rows, np.arange(len(target_rows)))),
        shape=(len(target_rows), len(target_rows)), dtype=complex,
    ).tocsc()
    direct = sparse.coo_matrix(
        (direct_phases, (direct_rows, np.arange(len(direct_rows)))),
        shape=target.shape, dtype=complex,
    ).tocsc()
    difference = direct - target
    return {
        "owned_edges": len(edge_modes),
        "direct_endpoint_FSWAP_mismatch_columns": direct_mismatches,
        "direct_endpoint_FSWAP_residual": c315.largest_singular(difference),
        "direct_endpoint_FSWAP_raw_maximum": raw_maximum(difference),
        "qutrit_phase_branch_cases": q_branch_cases,
        "qutrit_phase_carrier_ambiguous_columns": q_phase_ambiguous_columns,
        "qutrit_phase_minimum_effective_amplitude": min(
            abs(value) for value in q_effective_diagonal
        ),
        "qutrit_phase_role_unprepare_maximum_leakage": q_maximum_leakage,
        "first_failed_reversible_map": (
            "eleven local qutrit phases; W_role^dag leaks before the decoded occupation swaps"
        ),
        "global_ordered_FSWAP_route_used": False,
    }


def deletion_controls(
    encoding: sparse.csc_matrix,
) -> dict[str, object]:
    # Delete the tag-copy CNOT for the first feature block.  It changes every
    # ray on which that decoded half-edge is occupied.
    rows = []
    columns = []
    values = []
    changed = 0
    for column, label in enumerate(route_c.FOCK_BASIS):
        occupied_by_cell = defaultdict(list)
        for global_mode in label:
            cell, mode = divmod(global_mode, 6)
            occupied_by_cell[cell].append(mode)
        choices = []
        for cell in range(len(route_c.BASE_CELLS)):
            local = tuple(occupied_by_cell.get(cell, ()))
            if len(local) == 1:
                occupied = local[0]
                choices.append(tuple(
                    (carrier, ROLE_AMPLITUDES[(occupied, carrier)])
                    for carrier in range(6) if carrier != occupied
                ))
            else:
                choices.append(((SENTINEL, 1.0 + 0.0j),))
        for role_choices in product(*choices):
            roles = tuple(row[0] for row in role_choices)
            amplitude = complex(np.prod([row[1] for row in role_choices]))
            chart = []
            for block, (_star, _direction, _endpoint, cell_coord, mode) in enumerate(previous.FEATURE_BLOCKS):
                cell = route_c.BASE_CELLS.index(cell_coord)
                local = tuple(occupied_by_cell.get(cell, ()))
                word = feature_word(local, roles[cell], mode)
                if block == 0 and (word & 1):
                    word ^= 1
                    changed += 1
                chart.append(word)
            key = (label, roles, tuple(chart))
            # The mutated target lives in a disjoint diagnostic row namespace.
            rows.append(len(rows))
            columns.append(column)
            values.append(amplitude)
    mutated = sparse.coo_matrix(
        (values, (rows, columns)),
        shape=(len(rows), encoding.shape[1]), dtype=complex,
    ).tocsc()
    # Row labels are deliberately separate; use the exact affected column
    # norm instead of subtracting matrices with unrelated row enumerations.
    block = previous.FEATURE_BLOCKS[0]
    _star, _direction, _endpoint, cell_coord, mode = block
    cell = route_c.BASE_CELLS.index(cell_coord)
    affected_columns = sum(
        (6 * cell + mode) in label for label in route_c.FOCK_BASIS
    )
    return {
        "deleted_chart_CNOT_changed_rays": changed,
        "deleted_chart_CNOT_affected_logical_columns": affected_columns,
        "deleted_chart_CNOT_column_residual": math.sqrt(2.0) if affected_columns else 0.0,
        "mutated_encoding_Gram_raw_maximum": raw_maximum(
            mutated.conj().T @ mutated - sparse.eye(mutated.shape[1], format="csc")
        ),
        "shared_copy_joint_rank": qcore.four_copy_projectors()["joint_equality_rank"],
        "delete_one_shared_equality_rank": qcore.four_copy_projectors()["delete_one_equality_rank"],
    }


def placement_resources() -> dict[str, object]:
    block_semantic = 61
    role = ROLE_RAILS
    chart_counts = Counter()
    for _star, _direction, _endpoint, cell, _mode in previous.FEATURE_BLOCKS:
        chart_counts[cell] += 2
    maximum_chart = max(chart_counts.values())
    local_work = MATCH_SCRATCH + 1 + 2
    block_stride = block_semantic + role + maximum_chart + local_work + 2
    rows = []
    for length in (5, 6):
        anchors = {
            tuple(block_stride * (coordinate % length) for coordinate in cell)
            for cell in route_c.BASE_CELLS
        }
        rows.append({
            "L": length,
            "split": "train" if length == 5 else "held-no-refit",
            "coarse_cells": len(route_c.BASE_CELLS),
            "distinct_block_anchors": len(anchors),
            "block_collisions": len(route_c.BASE_CELLS) - len(anchors),
            "held_parameters_refit": 0,
        })
    return {
        "Cycle655_semantic_M2_per_cell": block_semantic,
        "carrier_role_M2_per_cell": role,
        "maximum_chart_copy_M2_per_cell": maximum_chart,
        "clean_match_flag_bypass_M2_per_cell": local_work,
        "declared_block_stride": block_stride,
        "unique_edge_role_scratch_M2": 22,
        "global_or_Jordan_Wigner_M2": 0,
        "maximum_two_cell_route_length_bound": 2 * block_stride + 1,
        "placement_rows": rows,
        "constant_overhead_per_coarse_cell": True,
    }


def main() -> None:
    landed_rows = tuple(local_landed_chart_census(length) for length in (5, 6))
    check(
        "the seven-rail carrier preparation reproduces every landed half-edge chart at L5 and held L6",
        len(ROLE_AMPLITUDES) == 30
        and all(
            row["branch_half_edge_cases"] == 276
            and row["amplitude_table_errors"] == 0
            and row["chart_errors"] == 0
            and row["invalid_qutrit_words"] == 0
            for row in landed_rows
        ),
        landed_rows,
    )

    role = matcher_and_role_resources()
    check(
        "the carrier word is a clean token-controlled sparse Givens preparation with an exact inverse",
        role["clean_match_cases"] == 384
        and role["clean_match_failures"] == 0
        and role["clean_match_reset_failures"] == 0
        and role["token_zero_fires"] == 0
        and role["role_Givens_factors_per_prepare"] == 30
        and max(role[key] for key in (
            "maximum_role_preparation_residual",
            "maximum_role_inverse_residual",
            "maximum_role_factor_unitarity_residual",
            "maximum_vacuum_bypass_residual",
            "maximum_vacuum_bypass_leakage",
            "Toffoli_decomposition_residual",
            "Fredkin_decomposition_residual",
        )) < TOL,
        role,
    )

    encoding_rows = []
    encodings = []
    for length in (5, 6):
        details, encoding = patch_branch_rows(length)
        encoding_rows.append(details)
        encodings.append(encoding)
    check(
        "one Cycle655-plus-carrier graph E is an exact common two-star code at L5 and held L6",
        all(
            row["logical_columns_n_le_2"] == 2629
            and row["physical_role_chart_rays"] == 59941
            and row["encoding_nonzeros"] == 59941
            and row["maximum_branches_per_column"] == 25
            and row["invalid_qutrit_words"] == 0
            and row["shared_copy_equality_failures"] == 0
            and row["Gram_raw_maximum"] < TOL
            and row["zero_columns"] == 0
            for row in encoding_rows
        ),
        encoding_rows,
    )

    update_rows, logical_update = route_c.build_patch_update(route_c.BASE_AXIS)
    logical_coin = route_c.patch_coin(route_c.BASE_CELLS)
    logical_contact = route_c.patch_contact(route_c.BASE_CELLS)
    logical_coin_contact = logical_contact @ logical_coin
    coin_intertwiners = tuple(
        factorized_intertwiner(encoding, logical_coin) for encoding in encodings
    )
    contact_intertwiners = tuple(
        factorized_intertwiner(encoding, logical_coin_contact) for encoding in encodings
    )
    check(
        "erase-role/coin/reprepare-role closes the first same-E coin intertwiner without a dense completion",
        all(max(row.values()) < TOL for row in coin_intertwiners),
        {
            "equation": "E_refresh C_patch = G_physical,coin E_refresh",
            "factorization": "decode; erase charts; W_role^dag; coin factors; W_role; recompute charts; encode",
            "rows": coin_intertwiners,
            "dense_augmented_code_completion_used": False,
        },
    )
    check(
        "the same factorized E closes the local contact after the refreshed coin",
        all(max(row.values()) < TOL for row in contact_intertwiners)
        and update_rows["contact_nontrivial_columns"] == 180
        and update_rows["delete_contact_update_residual"] > 0.3
        and update_rows["one_particle_mass_residual"] < TOL
        and update_rows["uniform_one_particle_eigen_residual"] < TOL,
        {"intertwiners": contact_intertwiners, "logical_update_fixture": update_rows},
    )

    seam_failure = seam_candidate_diagnostic()
    check(
        "the exact first remaining physical seam map is exposed before any full-update claim",
        seam_failure["owned_edges"] == 11
        and seam_failure["direct_endpoint_FSWAP_mismatch_columns"] == 240
        and seam_failure["direct_endpoint_FSWAP_residual"] > 1.9
        and seam_failure["direct_endpoint_FSWAP_raw_maximum"] > 1.9
        and seam_failure["qutrit_phase_carrier_ambiguous_columns"] == 110
        and abs(seam_failure["qutrit_phase_minimum_effective_amplitude"] - 0.6) < TOL
        and abs(seam_failure["qutrit_phase_role_unprepare_maximum_leakage"] - 0.8) < TOL
        and not seam_failure["global_ordered_FSWAP_route_used"],
        {
            **seam_failure,
            "disposition": (
                "coin/contact refresh is constructive; the local seam-role transport/cocycle is open"
            ),
        },
    )

    bindings = physical_factor_bindings()
    check(
        "Cycle655 supplies the exact decoded coin/contact/encode factors used by the refresh word",
        bindings["Cycle655_word_sha256"] == c656.EXPECTED_CYCLE655_WORD_SHA256
        and bindings["coin_decoded_factors_per_cell"] == 11
        and bindings["contact_onsite_gates_per_cell"] == 30
        and bindings["decoder_encoder_GF2_residual"] == 0
        and max(bindings[key] for key in (
            "coin_factor_residual", "pair_preparation_residual", "pair_inverse_residual",
            "register_contact_residual", "port_contact_residual",
        )) < TOL
        and not bindings["dense_augmented_code_completion_used"],
        bindings,
    )

    schedule = fixed_word_schedule()
    check(
        "the finite word has one station-zero token, clean returned controller work, and an ordinal rather than time",
        schedule["station_zero_token"] == 1
        and schedule["station_zero_return"] == 0
        and schedule["selected_factor_ordinals"] == schedule["fixed_stage_factors_before_primitive_expansion"]
        and schedule["offset_history_differs"]
        and schedule["zero_token_selected_events"] == 0
        and schedule["two_token_selected_events"] == 2 * schedule["selected_factor_ordinals"]
        and not schedule["program_ordinal_is_physical_time"]
        and schedule["Cycle656_base_selected_events"] == c656.T
        and schedule["Cycle656_base_return_station"] == 0
        and schedule["Cycle656_base_factor_order_ok"]
        and schedule["Cycle656_base_program_failures"] == 0
        and schedule["Cycle656_base_ancilla_failures"] == 0
        and schedule["Cycle656_base_B_vacuum_failures"] == 0,
        schedule,
    )

    covariance = carrier_covariance()
    symmetry = route_c.frame_and_translation_controls(logical_update)
    check(
        "the refreshed carrier/chart code and full update retain all 24 frames and 576 products",
        covariance["proper_cubic_frames"] == 24
        and covariance["ordered_frame_products"] == 576
        and covariance["carrier_phase_failures"] == 0
        and covariance["chart_transport_failures"] == 0
        and covariance["carrier_cocycle_product_failures"] == 0
        and symmetry["proper_cubic_frames"] == 24
        and symmetry["ordered_frame_products"] == 576
        and symmetry["maximum_update_covariance_residual"] < TOL
        and symmetry["program_edge_frame_failures"] == 0
        and symmetry["qutrit_endpoint_reversal_failures"] == 0
        and symmetry["frame_group_mapping_failures"] == 0
        and symmetry["frame_group_phase_failures"] == 0
        and symmetry["program_edge_product_failures"] == 0
        and all(row["failures"] == 0 for row in symmetry["translation_rows"]),
        {"carrier": covariance, "logical_update": symmetry},
    )

    deletion = deletion_controls(encodings[0])
    domain = route_c.unlawful_domain_controls()
    check(
        "role/chart/equality/token/work deletions and unlawful-domain controls remain active",
        role["deleted_first_factor_residual"] > 0.4
        and role["reversed_factor_order_residual"] > 0.4
        and role["dirty_bypass_change"] > 0.4
        and deletion["deleted_chart_CNOT_changed_rays"] > 0
        and deletion["deleted_chart_CNOT_affected_logical_columns"] > 0
        and deletion["deleted_chart_CNOT_column_residual"] > 1
        and deletion["shared_copy_joint_rank"] == 9
        and deletion["delete_one_shared_equality_rank"] == 27
        and domain["invalid_qutrit_rejections"] == domain["invalid_qutrit_rows"] == 4
        and domain["invalid_fock_rejections"] == domain["invalid_fock_rows"] == 4,
        {"role": role, "chart_and_equality": deletion, "domain": domain},
    )

    resources = placement_resources()
    check(
        "the refreshed compiler has bounded constant overhead, bounded routes, and no global parity service",
        resources["constant_overhead_per_coarse_cell"]
        and resources["global_or_Jordan_Wigner_M2"] == 0
        and resources["maximum_two_cell_route_length_bound"] < 250
        and all(row["block_collisions"] == 0 for row in resources["placement_rows"]),
        resources,
    )

    supplied = (
        "Cycle655 E_full decoder/encoder, pair-register preparation, contact word and eleven decoded coin factors",
        "Cycle656 station-zero token, clean selector/flag/scratch/bypass convention and selector-before-shift ordinal",
        "the landed Cycle311 five-carrier one-particle amplitudes and three-state half-edge chart",
        "Route C's 12-cell/11-owned-seam n<=2 logical update and its 24-frame/576-product family",
        "one seven-rail carrier convention, one finite factor order, L5 training, held L6 and numerical tolerance",
    )
    derived = (
        "an explicit 59941-ray graph encoding with exact shared-view equalities and zero Gram residual",
        "a thirty-Givens reversible carrier preparation and two-CNOT-per-chart refresh",
        "zero first-coin and coin/contact same-E factorized intertwiner and leakage residuals",
        "one clean fixed ordinal with returned token/controller work and all 24/576 carrier cocycle products",
        "the exact first local seam failure: 240 direct-FSWAP sign mismatches and q-phase role leakage 0.8",
    )
    open_items = (
        "primitive dynamical preparation or enforcement of the graph-code projectors and clean controller genesis",
        "one recurrent infinite-lattice collision theorem rather than the bounded L5/L6 placements",
        "a canonical off-code circuit word invariant under every proper-cubic frame rather than a rotated family",
        "a local seam-role transport/cocycle that closes the Route-C exterior stream without a global mode order",
        "n>2 patch execution, full M64^12 matrix materialization and thermodynamic resource scaling",
        "physical time, rate, energy, source, Record, occurrence, Born meaning, minimum content or axiom pressure",
    )
    certificate = {
        "landed_rows": landed_rows,
        "encoding_rows": encoding_rows,
        "coin_intertwiners": coin_intertwiners,
        "contact_intertwiners": contact_intertwiners,
        "seam_failure": seam_failure,
        "bindings": bindings,
        "schedule": schedule,
        "covariance": covariance,
        "deletion": deletion,
        "resources": resources,
    }
    digest = sha256(json.dumps(
        certificate, sort_keys=True, separators=(",", ":"), default=str
    ).encode()).hexdigest()
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "bounded-full128-two-star-coin-feature-refresh-certificate",
        "terminal": "FULL128_COIN_REFRESH_CLOSED_LOCAL_SEAM_ROLE_MAP_OPEN",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "equation": "E_refresh (C_contact C_coin) = G_physical_refresh E_refresh",
        "encoding": encoding_rows,
        "coin_intertwiner": coin_intertwiners,
        "coin_contact_intertwiner": contact_intertwiners,
        "logical_full_update_fixture": update_rows,
        "first_failed_seam_map": seam_failure,
        "physical_bindings": bindings,
        "fixed_schedule": schedule,
        "covariance": {"carrier": covariance, "logical_update": symmetry},
        "deletions": deletion,
        "resources": {
            **resources,
            "coarse_cells": 12,
            "coarse_modes": 72,
            "logical_columns_n_le_2": 2629,
            "role_chart_rays": 59941,
            "feature_copy_M2": 48,
            "carrier_role_M2": 12 * ROLE_RAILS,
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024),
        },
        "supplied": supplied,
        "derived": derived,
        "open": open_items,
        "claim_ceiling": (
            "Positive bounded replacement encoding and factorized coin/contact word.  The prior frozen-copy "
            "coin failure is closed by reversible carrier/chart refresh; no dense ambient completion is used.  "
            "The local seam-role map remains open at leakage 0.8; no global ordered route is substituted.  "
            "Genesis, recurrence and off-code canonical covariance also remain supplied/open, so this is not "
            "a minimum, no-go, shared obstruction or axiom-pressure result."
        ),
        "certificate_sha256": digest,
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
