#!/usr/bin/env python3
"""Literal fixed-M2 reachable-state executor for the two-star candidate.

Unlike the preceding contracted executor, this runner stores every carrier
rail, matcher scratch, flag, bypass, token, edge-role, chart, and transit M2 as
an actual bit.  It executes the token-controlled matcher/Toffoli word, controlled
Fredkin bypass, lifted two-rail Givens on all 00/01/10/11 words, chart CNOTs,
routed SWAP-CZ-SWAP macros, seam edge-work compute/use/uncompute, endpoint
FSWAP, seven rail bundle SWAPs, and onsite contact gates literally.

Only the reachable n<=2 two-star code columns are enumerated; the surrounding
2^335 decoded-interface Hilbert is defined by the same square local gates but
is not materialized.  The target-derived 224-CZ finite order list remains a
supplied two-star object and does not satisfy the recurrent/no-preferred-order
contract.  No recurrent, full-covariance, no-go, or axiom-pressure claim is
made.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from hashlib import sha256
from itertools import product
import json
import math
import resource
import time

import numpy as np
from scipy import sparse

import frontier_two_star_fixed_register_local_executor_2026_07_25 as base


START = time.perf_counter()
TOL = 6.0e-10
DROP = 2.0e-13
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


@dataclass(frozen=True)
class LiteralBasis:
    data: int                 # 6 * 12 decoded data M2s
    role_rails: int           # 7 * 12 actual one-hot rail M2s
    charts: int               # 2 * 24 chart M2s
    tokens: int               # 1 clean program token per cell
    matcher_scratch: int      # 5 * 12 M2s
    matcher_flags: int        # 1 * 12 M2s
    bypass: int               # 2 * 12 M2s
    edge_work: int            # 1 * 11 M2s
    transit: int              # 1 * 12 M2s


State = dict[LiteralBasis, complex]


def add(output: State, key: LiteralBasis, amplitude: complex) -> None:
    if abs(amplitude) <= DROP:
        return
    output[key] = output.get(key, 0.0 + 0.0j) + amplitude
    if abs(output[key]) <= DROP:
        del output[key]


def bit(value: int, index: int) -> int:
    return (value >> index) & 1


def set_bit(value: int, index: int, supplied: int) -> int:
    return value ^ ((bit(value, index) ^ supplied) << index)


def role_index(cell: int, rail: int) -> int:
    return 7 * cell + rail


def scratch_index(cell: int, slot: int) -> int:
    return 5 * cell + slot


def bypass_index(cell: int, slot: int) -> int:
    return 2 * cell + slot


def role_mask(roles: tuple[int, ...]) -> int:
    return sum(1 << role_index(cell, rail) for cell, rail in enumerate(roles))


def chart_mask(data: int, role_rails: int) -> int:
    value = 0
    for block, (_star, _direction, _endpoint, cell_coord, mode) in enumerate(base.FEATURES):
        cell = base.CELL_INDEX[cell_coord]
        value |= bit(data, 6 * cell + mode) << (2 * block)
        value |= bit(role_rails, role_index(cell, mode)) << (2 * block + 1)
    return value


def encoded_column(label: tuple[int, ...], length: int, transit: int = 0) -> State:
    data = sum(1 << mode for mode in label)
    output: State = {}
    for roles, amplitude in base.role_choices(label, length):
        rails = role_mask(roles)
        key = LiteralBasis(
            data=data,
            role_rails=rails,
            charts=chart_mask(data, rails),
            tokens=(1 << len(base.CELLS)) - 1,
            matcher_scratch=0,
            matcher_flags=0,
            bypass=0,
            edge_work=0,
            transit=transit,
        )
        add(output, key, amplitude)
    return output


def map_keys(state: State, operation) -> State:
    output: State = {}
    for key, amplitude in state.items():
        target, phase = operation(key)
        add(output, target, phase * amplitude)
    return output


def x_data(state: State, mode: int) -> State:
    return map_keys(state, lambda key: (replace(key, data=key.data ^ (1 << mode)), 1))


def toffoli_token_data_to_scratch(
    state: State, cell: int, data_mode: int, scratch: int
) -> State:
    return map_keys(state, lambda key: (
        replace(
            key,
            matcher_scratch=key.matcher_scratch
            ^ (
                (bit(key.tokens, cell) & bit(key.data, data_mode))
                << scratch
            ),
        ), 1
    ))


def toffoli_scratch_data_to_scratch(
    state: State, left_scratch: int, data_mode: int, target_scratch: int
) -> State:
    return map_keys(state, lambda key: (
        replace(
            key,
            matcher_scratch=key.matcher_scratch ^ (
                (bit(key.matcher_scratch, left_scratch) & bit(key.data, data_mode))
                << target_scratch
            ),
        ), 1
    ))


def toffoli_scratch_data_to_flag(
    state: State, left_scratch: int, data_mode: int, cell: int
) -> State:
    return map_keys(state, lambda key: (
        replace(
            key,
            matcher_flags=key.matcher_flags ^ (
                (bit(key.matcher_scratch, left_scratch) & bit(key.data, data_mode))
                << cell
            ),
        ), 1
    ))


def fredkin_role_bypass(
    state: State, cell: int, role_rail: int, bypass_slot: int
) -> State:
    r_index = role_index(cell, role_rail)
    b_index = bypass_index(cell, bypass_slot)

    def operation(key: LiteralBasis) -> tuple[LiteralBasis, int]:
        if not bit(key.matcher_flags, cell):
            return key, 1
        left, right = bit(key.role_rails, r_index), bit(key.bypass, b_index)
        roles = set_bit(key.role_rails, r_index, right)
        bypass = set_bit(key.bypass, b_index, left)
        return replace(key, role_rails=roles, bypass=bypass), 1

    return map_keys(state, operation)


def two_bypass_matrix(state: State, cell: int, matrix: np.ndarray) -> State:
    first, second = bypass_index(cell, 0), bypass_index(cell, 1)
    output: State = {}
    for key, amplitude in state.items():
        source = bit(key.bypass, first) | (bit(key.bypass, second) << 1)
        for target in range(4):
            coefficient = matrix[target, source]
            if abs(coefficient) <= DROP:
                continue
            bypass = set_bit(key.bypass, first, target & 1)
            bypass = set_bit(bypass, second, (target >> 1) & 1)
            add(output, replace(key, bypass=bypass), coefficient * amplitude)
    return output


def controlled_role_factor(
    state: State, cell: int, carrier: int, two_level: np.ndarray
) -> State:
    state = fredkin_role_bypass(state, cell, base.refresh.SENTINEL, 0)
    state = fredkin_role_bypass(state, cell, carrier, 1)
    state = two_bypass_matrix(state, cell, base.refresh.two_M2_matrix(two_level))
    state = fredkin_role_bypass(state, cell, carrier, 1)
    state = fredkin_role_bypass(state, cell, base.refresh.SENTINEL, 0)
    return state


def matcher_compute(state: State, cell: int, occupied: int) -> State:
    for mode in range(6):
        if mode != occupied:
            state = x_data(state, 6 * cell + mode)
    state = toffoli_token_data_to_scratch(
        state, cell, 6 * cell, scratch_index(cell, 0)
    )
    for mode in range(1, 5):
        state = toffoli_scratch_data_to_scratch(
            state,
            scratch_index(cell, mode - 1),
            6 * cell + mode,
            scratch_index(cell, mode),
        )
    state = toffoli_scratch_data_to_flag(
        state, scratch_index(cell, 4), 6 * cell + 5, cell
    )
    return state


def matcher_uncompute(state: State, cell: int, occupied: int) -> State:
    state = toffoli_scratch_data_to_flag(
        state, scratch_index(cell, 4), 6 * cell + 5, cell
    )
    for mode in reversed(range(1, 5)):
        state = toffoli_scratch_data_to_scratch(
            state,
            scratch_index(cell, mode - 1),
            6 * cell + mode,
            scratch_index(cell, mode),
        )
    state = toffoli_token_data_to_scratch(
        state, cell, 6 * cell, scratch_index(cell, 0)
    )
    for mode in reversed(range(6)):
        if mode != occupied:
            state = x_data(state, 6 * cell + mode)
    return state


def role_refresh(state: State, inverse: bool) -> State:
    for cell in range(len(base.CELLS)):
        for occupied in range(6):
            state = matcher_compute(state, cell, occupied)
            word = base.refresh.ROLE_PREPARATIONS[occupied]
            factors = tuple(
                (carrier, matrix.conj().T)
                for carrier, matrix in reversed(word)
            ) if inverse else word
            for carrier, matrix in factors:
                state = controlled_role_factor(state, cell, carrier, matrix)
            state = matcher_uncompute(state, cell, occupied)
    return state


def chart_word(state: State) -> State:
    def operation(key: LiteralBasis) -> tuple[LiteralBasis, int]:
        charts = key.charts
        for block, (_star, _direction, _endpoint, cell_coord, mode) in enumerate(base.FEATURES):
            cell = base.CELL_INDEX[cell_coord]
            charts ^= bit(key.data, 6 * cell + mode) << (2 * block)
            charts ^= bit(key.role_rails, role_index(cell, mode)) << (2 * block + 1)
        return replace(key, charts=charts), 1
    return map_keys(state, operation)


def apply_data_gate(state: State, cell: int, wires: tuple[int, ...], matrix: np.ndarray) -> State:
    output: State = {}
    global_wires = tuple(6 * cell + wire for wire in wires)
    for key, amplitude in state.items():
        source = sum(bit(key.data, wire) << index for index, wire in enumerate(global_wires))
        for target in range(1 << len(global_wires)):
            coefficient = matrix[target, source]
            if abs(coefficient) <= DROP:
                continue
            data = key.data
            for index, wire in enumerate(global_wires):
                data = set_bit(data, wire, (target >> index) & 1)
            add(output, replace(key, data=data), coefficient * amplitude)
    return output


def coin_word(state: State) -> State:
    for cell in range(len(base.CELLS)):
        for gate in base.COIN_GATES:
            state = apply_data_gate(state, cell, gate.wires, gate.matrix)
    return state


def swap_data_transit(state: State, mode: int, center: int) -> State:
    def operation(key: LiteralBasis) -> tuple[LiteralBasis, int]:
        left, right = bit(key.data, mode), bit(key.transit, center)
        return replace(
            key,
            data=set_bit(key.data, mode, right),
            transit=set_bit(key.transit, center, left),
        ), 1
    return map_keys(state, operation)


def cz_data_pair(state: State, left: int, right: int) -> State:
    return map_keys(state, lambda key: (
        key, -1 if bit(key.data, left) and bit(key.data, right) else 1
    ))


def cz_transit_data(state: State, center: int, mode: int) -> State:
    return map_keys(state, lambda key: (
        key, -1 if bit(key.transit, center) and bit(key.data, mode) else 1
    ))


def transition_word(state: State) -> State:
    for term in base.routed.ROUTED_TERMS:
        left, right = term.pair
        if term.distance <= 1:
            state = cz_data_pair(state, left, right)
        else:
            if term.midpoint is None:
                raise AssertionError(term)
            center = base.CELL_INDEX[term.midpoint]
            state = swap_data_transit(state, left, center)
            state = cz_transit_data(state, center, right)
            state = swap_data_transit(state, left, center)
    return state


def cnot_data_edge(state: State, mode: int, edge: int) -> State:
    return map_keys(state, lambda key: (
        replace(key, edge_work=key.edge_work ^ (bit(key.data, mode) << edge)), 1
    ))


def cz_data_edge(state: State, mode: int, edge: int) -> State:
    return map_keys(state, lambda key: (
        key, -1 if bit(key.data, mode) and bit(key.edge_work, edge) else 1
    ))


def swap_data(state: State, left: int, right: int) -> State:
    return map_keys(state, lambda key: (
        replace(
            key,
            data=set_bit(set_bit(key.data, left, bit(key.data, right)), right, bit(key.data, left)),
        ), 1
    ))


def swap_role_rail(state: State, left_cell: int, right_cell: int, rail: int) -> State:
    left, right = role_index(left_cell, rail), role_index(right_cell, rail)
    return map_keys(state, lambda key: (
        replace(
            key,
            role_rails=set_bit(
                set_bit(key.role_rails, left, bit(key.role_rails, right)),
                right, bit(key.role_rails, left),
            ),
        ), 1
    ))


def seam_word(state: State, edge: int) -> State:
    left, right, intermediate = base.SPECS[edge]
    for mode in intermediate:
        state = cnot_data_edge(state, mode, edge)
    state = cz_data_edge(state, left, edge)
    state = cz_data_edge(state, right, edge)
    for mode in reversed(intermediate):
        state = cnot_data_edge(state, mode, edge)
    state = cz_data_pair(state, left, right)
    state = swap_data(state, left, right)
    for rail in range(7):
        state = swap_role_rail(state, left // 6, right // 6, rail)
    return state


def contact_word(state: State) -> State:
    contact = np.diag((1, 1, 1, np.exp(1j * base.route_c.c230.COUPLING))).astype(complex)
    for cell in range(len(base.CELLS)):
        for left, right in base.combinations(range(6), 2):
            state = apply_data_gate(state, cell, (left, right), contact)
    return state


def execute(source: State, include_coin: bool) -> tuple[State, dict[str, int]]:
    state = chart_word(source)
    state = role_refresh(state, inverse=True)
    chart_failures = sum(key.charts != 0 for key in state)
    role_failures = sum(
        any(bit(key.role_rails, role_index(cell, rail)) != int(rail == base.refresh.SENTINEL)
            for cell in range(len(base.CELLS)) for rail in range(7))
        for key in state
    )
    if include_coin:
        state = coin_word(state)
    state = transition_word(state)
    for edge in range(len(base.EDGES)):
        state = seam_word(state, edge)
    state = contact_word(state)
    work_failures = sum(
        key.matcher_scratch != 0 or key.matcher_flags != 0
        or key.bypass != 0 or key.edge_work != 0
        for key in state
    )
    token_failures = sum(key.tokens != (1 << len(base.CELLS)) - 1 for key in state)
    state = role_refresh(state, inverse=False)
    state = chart_word(state)
    return state, {
        "chart_erase_failures": chart_failures,
        "carrier_sentinel_failures": role_failures,
        "work_return_failures": work_failures,
        "token_return_failures": token_failures,
    }


def difference(left: State, right: State) -> tuple[float, float]:
    values = [left.get(key, 0.0) - right.get(key, 0.0) for key in set(left) | set(right)]
    return max((abs(value) for value in values), default=0.0), math.sqrt(
        sum(abs(value) ** 2 for value in values)
    )


def expected(logical: sparse.csc_matrix, column: int, length: int, transit: int) -> State:
    output: State = {}
    supplied = logical.getcol(column)
    for target, coefficient in zip(supplied.indices, supplied.data):
        for key, amplitude in encoded_column(base.FOCK_BASIS[int(target)], length, transit).items():
            add(output, key, coefficient * amplitude)
    return output


def intertwiner(length: int, include_coin: bool, columns: tuple[int, ...]) -> dict[str, object]:
    logical = base.route_c.patch_contact(base.CELLS) @ base.route_c.patch_stream(base.CELLS, base.EDGES)
    if include_coin:
        logical = logical @ base.route_c.patch_coin(base.CELLS)
    mismatch = chart = carrier = work = token = 0
    raw_max = norm_max = norm_defect = 0.0
    rays = 0
    for column in columns:
        source = encoded_column(base.FOCK_BASIS[column], length)
        observed, stages = execute(source, include_coin)
        target = expected(logical, column, length, 0)
        raw, norm = difference(observed, target)
        mismatch += raw > TOL
        raw_max = max(raw_max, raw)
        norm_max = max(norm_max, norm)
        norm_defect = max(norm_defect, abs(sum(abs(value) ** 2 for value in observed.values()) - 1))
        chart += stages["chart_erase_failures"]
        carrier += stages["carrier_sentinel_failures"]
        work += stages["work_return_failures"]
        token += stages["token_return_failures"]
        rays += len(observed)
    return {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "coin_executed": include_coin,
        "columns": len(columns),
        "output_rays": rays,
        "mismatch_columns": mismatch,
        "maximum_intertwiner_raw": raw_max,
        "maximum_column_residual": norm_max,
        "maximum_norm_defect": norm_defect,
        "chart_erase_failures": chart,
        "carrier_sentinel_failures": carrier,
        "work_return_failures": work,
        "token_return_failures": token,
    }


def local_literal_controls() -> dict[str, object]:
    matcher_failures = matcher_return = token_block_failures = token_return = bypass_return = 0
    two_rail_unitarity = vacuum_change = double_change = 0.0
    for occupied in range(6):
        for supplied in range(64):
            # One cell embedded in the fixed 12-cell register layout.
            key = LiteralBasis(
                data=supplied,
                role_rails=1 << role_index(0, base.refresh.SENTINEL),
                charts=0,
                tokens=(1 << len(base.CELLS)) - 1,
                matcher_scratch=0,
                matcher_flags=0,
                bypass=0,
                edge_work=0,
                transit=0,
            )
            state = matcher_compute({key: 1.0 + 0.0j}, 0, occupied)
            fired = next(iter(state)).matcher_flags & 1
            matcher_failures += fired != int(supplied == (1 << occupied))
            state = matcher_uncompute(state, 0, occupied)
            landed = next(iter(state))
            matcher_return += landed.data != supplied or landed.matcher_scratch != 0 or landed.matcher_flags != 0

            token_zero_key = replace(key, tokens=key.tokens ^ 1)
            token_zero_state = matcher_compute(
                {token_zero_key: 1.0 + 0.0j}, 0, occupied
            )
            token_zero_landed = next(iter(token_zero_state))
            token_block_failures += bool(token_zero_landed.matcher_flags & 1)
            token_zero_state = matcher_uncompute(
                token_zero_state, 0, occupied
            )
            token_zero_returned = next(iter(token_zero_state))
            token_return += (
                token_zero_returned != token_zero_key
                or token_zero_returned.tokens != token_zero_key.tokens
            )
        for carrier, matrix in base.refresh.ROLE_PREPARATIONS[occupied]:
            lifted = base.refresh.two_M2_matrix(matrix)
            two_rail_unitarity = max(two_rail_unitarity, float(np.linalg.norm(
                lifted.conj().T @ lifted - np.eye(4)
            )))
            vacuum_change = max(vacuum_change, float(np.linalg.norm(lifted[:, 0] - np.eye(4)[:, 0])))
            double_change = max(double_change, float(np.linalg.norm(lifted[:, 3] - np.eye(4)[:, 3])))

    # Dirty-bypass mutation is returned as a non-code witness, not silently erased.
    dirty = LiteralBasis(
        data=1,
        role_rails=1 << role_index(0, base.refresh.SENTINEL),
        charts=0,
        tokens=(1 << len(base.CELLS)) - 1,
        matcher_scratch=0,
        matcher_flags=1,
        bypass=1,
        edge_work=0,
        transit=0,
    )
    dirty_state = controlled_role_factor(
        {dirty: 1.0 + 0.0j}, 0, 1, base.refresh.ROLE_PREPARATIONS[0][0][1]
    )
    bypass_return += all(key.bypass == 0 for key in dirty_state)
    return {
        "matcher_cases": 384,
        "matcher_failures": matcher_failures,
        "matcher_return_failures": matcher_return,
        "token_zero_block_cases": 384,
        "token_zero_block_failures": token_block_failures,
        "token_zero_return_failures": token_return,
        "maximum_two_rail_unitarity_residual": two_rail_unitarity,
        "off_code_vacuum_change": vacuum_change,
        "off_code_double_change": double_change,
        "dirty_bypass_incorrectly_cleaned": bypass_return,
        "literal_decoded_interface_M2": 335,
        "logical_label_registers": 0,
        "variable_packet_blocks": 0,
    }


def main() -> None:
    local = local_literal_controls()
    check(
        "literal matcher, flag, bypass and two-rail gates close on their actual M2 bits",
        local["matcher_cases"] == 384
        and local["matcher_failures"] == 0
        and local["matcher_return_failures"] == 0
        and local["token_zero_block_cases"] == 384
        and local["token_zero_block_failures"] == 0
        and local["token_zero_return_failures"] == 0
        and local["maximum_two_rail_unitarity_residual"] < TOL
        and local["off_code_vacuum_change"] < TOL
        and local["off_code_double_change"] < TOL
        and local["dirty_bypass_incorrectly_cleaned"] == 0
        and local["literal_decoded_interface_M2"] == 335
        and local["logical_label_registers"] == 0
        and local["variable_packet_blocks"] == 0,
        local,
    )

    # Full n<=2 stream/contact at train size; held L6 uses an independently
    # recomputed carrier table on a deterministic sector-spanning set.
    full_columns = tuple(range(len(base.FOCK_BASIS)))
    held_columns = (
        0,
        *range(1, 1 + base.MODE_COUNT),
        *(base.FOCK_INDEX[(left, right)]
          for left, right in ((0, 1), (0, 6), (1, 31), (17, 44), (70, 71))),
    )
    stream_rows = (
        intertwiner(5, False, full_columns),
        intertwiner(6, False, tuple(held_columns)),
    )
    check(
        "the literal fixed-M2 word closes the complete L5 stream/contact basis and held L6 sectors",
        stream_rows[0]["columns"] == 2629
        and stream_rows[1]["columns"] == 78
        and all(
            row["mismatch_columns"] == 0
            and row["maximum_intertwiner_raw"] < TOL
            and row["maximum_column_residual"] < TOL
            and row["maximum_norm_defect"] < TOL
            and row["chart_erase_failures"] == 0
            and row["carrier_sentinel_failures"] == 0
            and row["work_return_failures"] == 0
            and row["token_return_failures"] == 0
            for row in stream_rows
        ),
        stream_rows,
    )

    # Coin is executed literally on a sector-spanning sample only in this
    # successor; the contracted predecessor retains the complete 2629-column
    # same-E coin sweep.
    coin_columns = tuple(held_columns)
    coin_rows = (
        intertwiner(5, True, coin_columns),
        intertwiner(6, True, coin_columns),
    )
    check(
        "the literal onsite coin factors compose on the same M2 word on held sector-spanning columns",
        all(
            row["columns"] == 78
            and row["mismatch_columns"] == 0
            and row["maximum_intertwiner_raw"] < TOL
            and row["maximum_column_residual"] < TOL
            and row["maximum_norm_defect"] < TOL
            and row["work_return_failures"] == 0
            and row["token_return_failures"] == 0
            for row in coin_rows
        ),
        coin_rows,
    )

    certificate = {
        "local_controls": local,
        "stream_contact": stream_rows,
        "coin_sample": coin_rows,
        "predecessor_full_sweep_certificate": "1b532df9f513d7de20af684353e7e8e1527339831a1be275ff6210901f504752",
    }
    digest = sha256(json.dumps(
        certificate, sort_keys=True, separators=(",", ":"), default=str
    ).encode()).hexdigest()
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "literal-fixed-M2-two-star-decoded-interface-closure",
        "terminal": "LITERAL_M2_TWO_STAR_STREAM_CLOSED_RECURRENT_GAUGE_OPEN",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "equation": "E_literal G_stream/contact,n<=2 = G_literal-M2 E_literal",
        "local_controls": local,
        "stream_contact": stream_rows,
        "coin_sample": coin_rows,
        "supplied": (
            "fixed tensor-product decoded data/rail/chart/token/work/transit M2 registers",
            "Cycle656 clean matcher/Fredkin-bypass grammar and Cycle655 onsite coin factors",
            "the finite global order and target-derived 224-CZ two-star transition list",
        ),
        "derived": (
            "literal storage of all 335 decoded-interface M2s and execution of every nonidentity operand on reachable states",
            "complete 2629-column L5 stream/contact closure and held L6 sector controls",
            "literal same-word coin closure on 78 sector-spanning columns at L5/L6",
        ),
        "open": (
            "complete literal coin sweep (available only in contracted predecessor)",
            "Cycle655 landed physical decode/encode execution with these literal auxiliary M2s",
            "target-independent recurrent local even-CAR gauge law on L-shaped/2x2 overlaps",
            "actual transformed-E/rebuilt-word 24/576 covariance",
        ),
        "claim_ceiling": (
            "Positive literal fixed-M2 decoded-interface compiler for the bounded two-star stream/contact fixture. "
            "The global-order transition remains supplied and nonrecurrent; the coin literal sweep is sampled, "
            "and the physical Cycle655 binding and full covariance remain open."
        ),
        "resources": {
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024),
            "certificate_sha256": digest,
        },
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True, default=str))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
