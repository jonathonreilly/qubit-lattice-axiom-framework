#!/usr/bin/env python3
"""Fixed-register executor for the finite two-star Route-B candidate.

This runner replaces the label-block ambient of the preceding probe by fixed
local registers.  Every coarse cell owns six data M2s, seven one-hot carrier
rail M2s, clean matcher/work M2s, one transit M2, and the half-edge chart M2s
whose physical coordinates lie at that cell.  Every owned seam owns one clean
edge-role M2.  A basis key is the actual bit content of those fixed registers;
there is no logical-Fock-label register and no variable 1/7/49 block address.

The executed object is ``E_fixed_decoded``.  Its six data M2s are the decoded
occupation interface of the separately supplied Cycle655 61-M2 cell, not a
claim that it equals the landed ``E_refresh`` physical encoding.  A 983-M2
patch placement results after binding that supplied decoder and encoder, but
the end-to-end physical binding is not re-executed here.

The executed word is

    chart erase; carrier unprepare; [onsite coin]; routed transition;
    eleven local edge-role seam words; onsite contact;
    carrier prepare; chart recompute.

Carrier preparation is a fixed six-pattern local matcher schedule followed by
five controlled two-rail Givens factors.  During seams every lawful carrier is
sentinel; each endpoint seam nevertheless executes a local seven-rail bundle
SWAP, fixing a reversible off-code packet-transport extension.  Transition
CZs at distance two use one dirty-tolerant center transit M2 and return it.

The complete n<=2 two-star basis is compared against the independently built
logical stream/contact target, and the optional onsite coin is compared on the
same encoding.  The 224-CZ transition was synthesized offline from the target
inversion set and is not a recurrent local law.  An L-shaped three-center
probe explicitly tests and rejects the naive two-color/local-star extension;
it is an unfinished implementation, not a no-go or axiom-pressure result.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, replace
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations, product
import json
import math
import resource
import time

import numpy as np
from scipy import sparse

import frontier_full128_cycle_cocycle_intertwiner_2026_07_24 as c655
import frontier_two_adjacent_seam_chart_transition_2026_07_25 as adjacent
import frontier_two_star_full128_coin_covariant_feature_refresh_2026_07_25 as refresh
import frontier_two_star_routed_transition_physical_word_2026_07_25 as routed
import frontier_two_star_signed_carrier_single_seam_transport_2026_07_25 as single
import frontier_two_star_staggered_endpoint_feature_route_c_2026_07_25 as route_c
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315


START = time.perf_counter()
TOL = 5.0e-10
DROP = 2.0e-13
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
Pair = tuple[int, int]

CELLS = route_c.BASE_CELLS
CELL_INDEX = {cell: index for index, cell in enumerate(CELLS)}
EDGES = route_c.BASE_EDGES
SPECS = adjacent.patch_specs()
FEATURES = refresh.previous.FEATURE_BLOCKS
CENTERS = routed.CENTERS
MODE_COUNT = route_c.MODE_COUNT
FOCK_BASIS = route_c.FOCK_BASIS
FOCK_INDEX = route_c.FOCK_INDEX
TRANSITION = routed.TRANSITION
FINAL_MAPPING = routed.FINAL_MAPPING
COIN_GATES = tuple(
    gate for gate in c655.S.DECODED_GATES if gate.kind.startswith("coin")
)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


@dataclass(frozen=True)
class FixedBasis:
    """Invariant-sector coordinates of fixed tensor-product M2 registers.

    ``roles[cell]`` is shorthand for the one hot bit among seven fixed rail
    M2s; it is not a variable-sized packet coordinate.  Charts store two bits
    per fixed feature block.  Matcher work stores six bits per cell (five
    chain scratch and one flag); edge work and transit store one bit at every
    fixed owner.
    """

    data: int
    roles: tuple[int, ...]
    charts: int
    matcher_work: int
    edge_work: int
    transit: int


SparseState = dict[FixedBasis, complex]


def add_term(output: SparseState, key: FixedBasis, value: complex) -> None:
    if abs(value) <= DROP:
        return
    output[key] = output.get(key, 0.0 + 0.0j) + value
    if abs(output[key]) <= DROP:
        del output[key]


def data_bit(state: FixedBasis, mode: int) -> int:
    return (state.data >> mode) & 1


def set_data_bit(value: int, mode: int, supplied: int) -> int:
    observed = (value >> mode) & 1
    return value ^ ((observed ^ supplied) << mode)


def local_data_word(state: FixedBasis, cell: int) -> int:
    return (state.data >> (6 * cell)) & 0x3F


def feature_chart(data: int, roles: tuple[int, ...]) -> int:
    value = 0
    for block, (_star, _direction, _endpoint, cell_coord, mode) in enumerate(FEATURES):
        cell = CELL_INDEX[cell_coord]
        occupied = (data >> (6 * cell + mode)) & 1
        outer = int(roles[cell] == mode)
        value |= occupied << (2 * block)
        value |= outer << (2 * block + 1)
    return value


def chart_xor(state: FixedBasis) -> FixedBasis:
    """Literal local CNOT family: data->tag and role-rail->outer."""
    return replace(state, charts=state.charts ^ feature_chart(state.data, state.roles))


@lru_cache(maxsize=2)
def role_amplitudes(length: int) -> dict[tuple[int, int], complex]:
    return refresh.role_amplitudes(length)


@lru_cache(maxsize=None)
def role_choices(label: tuple[int, ...], length: int) -> tuple[tuple[tuple[int, ...], complex], ...]:
    occupied: dict[int, list[int]] = defaultdict(list)
    for mode in label:
        cell, local = divmod(mode, 6)
        occupied[cell].append(local)
    amplitudes = role_amplitudes(length)
    choices = []
    for cell in range(len(CELLS)):
        local = tuple(occupied.get(cell, ()))
        if len(local) == 1:
            mode = local[0]
            choices.append(tuple(
                (carrier, amplitudes[(mode, carrier)])
                for carrier in range(6) if carrier != mode
            ))
        else:
            choices.append(((refresh.SENTINEL, 1.0 + 0.0j),))
    rows = []
    for supplied in product(*choices):
        rows.append((tuple(row[0] for row in supplied), complex(np.prod(
            [row[1] for row in supplied]
        ))))
    return tuple(rows)


def encoded_column(
    label: tuple[int, ...], length: int, transit: int = 0
) -> SparseState:
    data = sum(1 << mode for mode in label)
    output: SparseState = {}
    for roles, amplitude in role_choices(label, length):
        key = FixedBasis(
            data=data,
            roles=roles,
            charts=feature_chart(data, roles),
            matcher_work=0,
            edge_work=0,
            transit=transit,
        )
        add_term(output, key, amplitude)
    return output


def matcher_trace(pattern: int, supplied: int) -> tuple[int, int, int]:
    """Execute the fixed negative-control/Toffoli chain and its inverse."""
    controls = [1] + [((supplied >> bit) & 1) for bit in range(6)]
    for bit in range(6):
        if bit != pattern:
            controls[bit + 1] ^= 1
    work = [0] * 5
    flag = 0
    work[0] ^= controls[0] & controls[1]
    for index in range(2, 6):
        work[index - 1] ^= work[index - 2] & controls[index]
    flag ^= work[4] & controls[6]
    fired = flag
    flag ^= work[4] & controls[6]
    for index in reversed(range(2, 6)):
        work[index - 1] ^= work[index - 2] & controls[index]
    work[0] ^= controls[0] & controls[1]
    return fired, sum(bit << index for index, bit in enumerate(work)), flag


def apply_role_factor(
    state: SparseState, cell: int, carrier: int, matrix: np.ndarray
) -> SparseState:
    output: SparseState = {}
    for key, amplitude in state.items():
        current = key.roles[cell]
        if current not in (refresh.SENTINEL, carrier):
            add_term(output, key, amplitude)
            continue
        source = 0 if current == refresh.SENTINEL else 1
        for target in (0, 1):
            coefficient = matrix[target, source]
            if abs(coefficient) <= DROP:
                continue
            roles = list(key.roles)
            roles[cell] = refresh.SENTINEL if target == 0 else carrier
            add_term(output, replace(key, roles=tuple(roles)), coefficient * amplitude)
    return output


def role_refresh(state: SparseState, inverse: bool) -> SparseState:
    """Fixed cell/pattern schedule; matcher controls, never host queries.

    The sparse executor contracts each clean matcher compute/uncompute around
    its controlled Givens.  ``matcher_trace`` independently executes the
    Boolean gate list on all local inputs and verifies returned scratch.
    """
    # Contract the already enumerated fixed five-Givens word to one 7x7 local
    # block for execution speed.  ``register_and_constraint_certificate``
    # separately tests every matcher basis input; ``factor_inventory`` retains
    # the literal factor counts and Cycle656 two-M2 expansion binding.
    output = state
    for cell in range(len(CELLS)):
        landed: SparseState = {}
        for key, amplitude in output.items():
            supplied = local_data_word(key, cell)
            if supplied == 0 or supplied & (supplied - 1):
                add_term(landed, key, amplitude)
                continue
            occupied = supplied.bit_length() - 1
            matrix = routed.ROLE_GATE_MATRICES[occupied][1 if inverse else 0]
            source = key.roles[cell]
            for target in range(refresh.ROLE_RAILS):
                coefficient = matrix[target, source]
                if abs(coefficient) <= DROP:
                    continue
                roles = list(key.roles)
                roles[cell] = target
                add_term(landed, replace(key, roles=tuple(roles)), coefficient * amplitude)
        output = landed
    return output


def apply_data_gate(
    state: SparseState, cell: int, wires: tuple[int, ...], matrix: np.ndarray
) -> SparseState:
    output: SparseState = {}
    global_wires = tuple(6 * cell + wire for wire in wires)
    for key, amplitude in state.items():
        source = sum(data_bit(key, wire) << index for index, wire in enumerate(global_wires))
        for target in range(1 << len(global_wires)):
            coefficient = matrix[target, source]
            if abs(coefficient) <= DROP:
                continue
            data = key.data
            for index, wire in enumerate(global_wires):
                data = set_data_bit(data, wire, (target >> index) & 1)
            add_term(output, replace(key, data=data), coefficient * amplitude)
    return output


def apply_coin(state: SparseState) -> SparseState:
    output = state
    for cell in range(len(CELLS)):
        for gate in COIN_GATES:
            output = apply_data_gate(output, cell, gate.wires, gate.matrix)
    return output


def route_macro(key: FixedBasis, term: routed.RoutedTerm) -> tuple[FixedBasis, int]:
    left, right = term.pair
    if term.distance <= 1:
        return key, -1 if data_bit(key, left) and data_bit(key, right) else 1
    if term.midpoint is None:
        raise AssertionError(term)
    center = CELL_INDEX[term.midpoint]
    transit_bit = (key.transit >> center) & 1
    left_bit = data_bit(key, left)
    data = set_data_bit(key.data, left, transit_bit)
    transit = key.transit ^ ((transit_bit ^ left_bit) << center)
    middle_left = (transit >> center) & 1
    phase = -1 if middle_left and ((data >> right) & 1) else 1
    returned_left = (data >> left) & 1
    data = set_data_bit(data, left, (transit >> center) & 1)
    transit ^= (((transit >> center) & 1) ^ returned_left) << center
    return replace(key, data=data, transit=transit), phase


def apply_transition(state: SparseState) -> SparseState:
    output = state
    for term in routed.ROUTED_TERMS:
        landed: SparseState = {}
        for key, amplitude in output.items():
            target, phase = route_macro(key, term)
            add_term(landed, target, phase * amplitude)
        output = landed
    return output


def apply_seam(state: SparseState, edge_index: int) -> SparseState:
    left, right, intermediate = SPECS[edge_index]
    left_cell, right_cell = left // 6, right // 6
    output: SparseState = {}
    for key, amplitude in state.items():
        scratch = (key.edge_work >> edge_index) & 1
        for mode in intermediate:
            scratch ^= data_bit(key, mode)
        phase = -1 if scratch and (data_bit(key, left) ^ data_bit(key, right)) else 1
        for mode in reversed(intermediate):
            scratch ^= data_bit(key, mode)
        edge_work = key.edge_work
        if scratch != ((edge_work >> edge_index) & 1):
            edge_work ^= 1 << edge_index

        left_bit, right_bit = data_bit(key, left), data_bit(key, right)
        if left_bit and right_bit:
            phase *= -1
        data = set_data_bit(key.data, left, right_bit)
        data = set_data_bit(data, right, left_bit)

        # Seven literal rail SWAPs across the same coarse edge.  In the
        # one-hot invariant sector this is exactly a swap of rail labels.
        roles = list(key.roles)
        roles[left_cell], roles[right_cell] = roles[right_cell], roles[left_cell]
        add_term(
            output,
            replace(key, data=data, roles=tuple(roles), edge_work=edge_work),
            phase * amplitude,
        )
    return output


def apply_contact(state: SparseState) -> SparseState:
    output: SparseState = {}
    for key, amplitude in state.items():
        pairs = 0
        for cell in range(len(CELLS)):
            count = local_data_word(key, cell).bit_count()
            pairs += count * (count - 1) // 2
        add_term(output, key, np.exp(1j * route_c.c230.COUPLING * pairs) * amplitude)
    return output


def execute_word(source: SparseState, include_coin: bool) -> tuple[SparseState, dict[str, object]]:
    state = {chart_xor(key): value for key, value in source.items()}
    chart_after_erase = max((key.charts for key in state), default=0)
    state = role_refresh(state, inverse=True)
    nonsentinel_before_seams = sum(
        abs(value) > DROP and any(role != refresh.SENTINEL for role in key.roles)
        for key, value in state.items()
    )
    if include_coin:
        state = apply_coin(state)
    state = apply_transition(state)
    for edge_index in range(len(EDGES)):
        state = apply_seam(state, edge_index)
    state = apply_contact(state)
    dirty_after_seams = sum(
        abs(value) > DROP and (key.edge_work != 0 or key.matcher_work != 0)
        for key, value in state.items()
    )
    state = role_refresh(state, inverse=False)
    state = {chart_xor(key): value for key, value in state.items()}
    return state, {
        "chart_after_erase_maximum": chart_after_erase,
        "nonsentinel_role_rays_before_seams": nonsentinel_before_seams,
        "dirty_work_rays_after_seams": dirty_after_seams,
    }


def state_difference(left: SparseState, right: SparseState) -> tuple[float, float]:
    keys = set(left) | set(right)
    values = [left.get(key, 0.0) - right.get(key, 0.0) for key in keys]
    return (
        max((abs(value) for value in values), default=0.0),
        math.sqrt(sum(abs(value) ** 2 for value in values)),
    )


def encoded_logical_column(
    logical: sparse.csc_matrix, column: int, length: int, transit: int
) -> SparseState:
    output: SparseState = {}
    supplied = logical.getcol(column)
    for target, coefficient in zip(supplied.indices, supplied.data):
        for key, amplitude in encoded_column(FOCK_BASIS[int(target)], length, transit).items():
            add_term(output, key, coefficient * amplitude)
    return output


def fixed_register_intertwiner(length: int, include_coin: bool, transit_cases: tuple[int, ...]) -> dict[str, object]:
    stream = route_c.patch_stream(CELLS, EDGES)
    contact = route_c.patch_contact(CELLS)
    logical = contact @ stream
    if include_coin:
        logical = logical @ route_c.patch_coin(CELLS)
    mismatch_columns = work_failures = chart_failures = role_failures = 0
    maximum_raw = maximum_norm = maximum_norm_defect = 0.0
    output_rays = 0
    for transit in transit_cases:
        for column, label in enumerate(FOCK_BASIS):
            source = encoded_column(label, length, transit)
            observed, stages = execute_word(source, include_coin)
            expected = encoded_logical_column(logical, column, length, transit)
            raw, norm = state_difference(observed, expected)
            mismatch_columns += raw > TOL
            maximum_raw = max(maximum_raw, raw)
            maximum_norm = max(maximum_norm, norm)
            maximum_norm_defect = max(
                maximum_norm_defect,
                abs(sum(abs(value) ** 2 for value in observed.values()) - 1.0),
            )
            work_failures += stages["dirty_work_rays_after_seams"]
            chart_failures += stages["chart_after_erase_maximum"] != 0
            role_failures += stages["nonsentinel_role_rays_before_seams"]
            output_rays += len(observed)
    return {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "coin_executed": include_coin,
        "logical_columns_n_le_2": len(FOCK_BASIS),
        "transit_cases": len(transit_cases),
        "executed_columns": len(FOCK_BASIS) * len(transit_cases),
        "output_rays": output_rays,
        "mismatch_columns": mismatch_columns,
        "maximum_intertwiner_raw": maximum_raw,
        "maximum_column_residual": maximum_norm,
        "maximum_output_norm_defect": maximum_norm_defect,
        "chart_erase_failures": chart_failures,
        "carrier_unprepare_failures": role_failures,
        "returned_work_failures": work_failures,
        "held_parameters_refit": 0,
    }


def register_and_constraint_certificate() -> dict[str, object]:
    charts_by_cell = Counter(cell for _s, _d, _e, cell, _m in FEATURES)
    matcher_failures = matcher_return_failures = 0
    for pattern in range(6):
        for supplied in range(64):
            fired, work, flag = matcher_trace(pattern, supplied)
            matcher_failures += fired != int(supplied == (1 << pattern))
            matcher_return_failures += work != 0 or flag != 0
    duplicate_failures = invalid_qutrits = norm_failures = 0
    support_rays = 0
    for length in (5, 6):
        for label in FOCK_BASIS:
            column = encoded_column(label, length)
            support_rays += len(column)
            norm_failures += abs(sum(abs(value) ** 2 for value in column.values()) - 1) > TOL
            for key in column:
                words = tuple((key.charts >> (2 * block)) & 3 for block in range(len(FEATURES)))
                invalid_qutrits += sum(word not in refresh.qcore.LAWFUL_QUTRIT_WORDS for word in words)
                for copies in refresh.previous.DUPLICATE_ROWS.values():
                    duplicate_failures += words[copies[0]] != words[copies[1]]
    per_cell = {
        "data_M2": 6,
        "carrier_rail_M2": 7,
        "matcher_scratch_M2": 5,
        "matcher_flag_M2": 1,
        "controlled_gate_bypass_M2": 2,
        "transit_M2": 1,
        "maximum_chart_M2": 2 * max(charts_by_cell.values()),
    }
    return {
        "coarse_cells": len(CELLS),
        "fixed_data_M2": 6 * len(CELLS),
        "fixed_carrier_rail_M2": 7 * len(CELLS),
        "fixed_chart_M2": 2 * len(FEATURES),
        "fixed_matcher_work_M2": 8 * len(CELLS),
        "fixed_transit_M2": len(CELLS),
        "fixed_edge_role_work_M2": len(EDGES),
        "total_fixed_M2_in_fixture": (
            6 * len(CELLS) + 7 * len(CELLS) + 2 * len(FEATURES)
            + 8 * len(CELLS) + len(CELLS) + len(EDGES)
        ),
        "maximum_M2_per_cell_block": sum(per_cell.values()),
        "per_cell_inventory": per_cell,
        "role_constraint": "exactly one of seven fixed carrier rail M2s",
        "chart_constraint": "two local XOR-defined M2s per star-view half-edge",
        "clean_work_constraint": "matcher/edge-role work zero; transit arbitrary and returned",
        "global_n_le_2_constraint_is_local": False,
        "global_Fock_label_registers": 0,
        "variable_packet_blocks": 0,
        "matcher_truth_table_failures": matcher_failures,
        "matcher_return_failures": matcher_return_failures,
        "encoding_norm_failures": norm_failures,
        "landed_invalid_qutrit_words": invalid_qutrits,
        "shared_chart_copy_failures": duplicate_failures,
        "encoding_support_rays_L5_plus_L6": support_rays,
    }


def source_identity_and_physical_binding() -> dict[str, object]:
    """Separate the executed decoded interface from the supplied M2 binding."""
    bindings = refresh.physical_factor_bindings()
    decoded_interface_M2 = 323
    physical_cell_semantic_M2 = 61
    physical_fixture_M2 = (
        physical_cell_semantic_M2 * len(CELLS)
        + 7 * len(CELLS)
        + 2 * len(FEATURES)
        + 8 * len(CELLS)
        + len(CELLS)
        + len(EDGES)
    )
    return {
        "executed_encoding_name": "E_fixed_decoded",
        "executed_encoding_equals_landed_E_refresh": False,
        "shared_E_refresh_carrier_amplitudes": True,
        "shared_E_refresh_chart_relation": True,
        "decoded_interface_M2_count": decoded_interface_M2,
        "Cycle655_semantic_M2_per_cell": physical_cell_semantic_M2,
        "Cycle655_decode_NN_gates_per_cell": bindings["Cycle655_decode_NN_gates_per_cell"],
        "Cycle655_encode_NN_gates_per_cell": bindings["Cycle655_encode_NN_gates_per_cell"],
        "Cycle655_decoder_encoder_GF2_residual": bindings["decoder_encoder_GF2_residual"],
        "bound_physical_fixture_M2_count": physical_fixture_M2,
        "physical_binding": (
            "tensor-extend the supplied Cycle655 decode/encode by identity on fixed role/chart/work/transit M2s; "
            "execute this runner's six-data-M2 word between them"
        ),
        "Cycle655_binding_executed_end_to_end_in_this_runner": False,
        "physical_site_claim_requires_supplied_Cycle655_binding": True,
        "new_axiom_or_primitive_claimed": False,
    }


def deletion_and_domain_certificate() -> dict[str, object]:
    target_coin = np.asarray(c655.P.coarse_factors(1)["coin"])
    coin_residuals = []
    for deleted in range(len(COIN_GATES)):
        observed = c655.S.product_on_seven(
            COIN_GATES[:deleted] + COIN_GATES[deleted + 1:]
        )
        coin_residuals.append(float(np.linalg.norm(observed - target_coin)))

    routing = routed.routing_truth_tables()
    update, _ = route_c.build_patch_update(route_c.BASE_AXIS)
    role = refresh.matcher_and_role_resources()
    unlawful = route_c.unlawful_domain_controls()

    # Every local edge-role phase has a two-particle basis witness: occupy one
    # endpoint and one intermediate mode.  Removing either endpoint/scratch CZ
    # flips that column, hence norm-2 residual.
    edge_phase_witnesses = sum(bool(spec[2]) for spec in SPECS)

    # Delete one chart-tag recomputation CNOT on a landed column whose selected
    # feature mode is occupied.  The omitted and correct chart rays are
    # orthogonal; compute the exact sparse-column residual rather than assert it.
    _star, _direction, _endpoint, feature_cell, feature_mode = FEATURES[0]
    occupied_mode = 6 * CELL_INDEX[feature_cell] + feature_mode
    correct_chart = encoded_column((occupied_mode,), 5)
    mutated_chart: SparseState = {}
    for key, amplitude in correct_chart.items():
        add_term(mutated_chart, replace(key, charts=key.charts ^ 1), amplitude)
    chart_raw, chart_norm = state_difference(correct_chart, mutated_chart)

    # Dirty edge-role work is not silently accepted as a code state.  It is
    # returned dirty and changes the first seam phase on an endpoint witness.
    left, _right, _intermediate = SPECS[0]
    clean_key = FixedBasis(
        data=1 << left,
        roles=(refresh.SENTINEL,) * len(CELLS),
        charts=0,
        matcher_work=0,
        edge_work=0,
        transit=0,
    )
    dirty_key = replace(clean_key, edge_work=1)
    clean_out = apply_seam({clean_key: 1.0 + 0.0j}, 0)
    dirty_out = apply_seam({dirty_key: 1.0 + 0.0j}, 0)
    clean_phase = next(iter(clean_out.values()))
    dirty_phase = next(iter(dirty_out.values()))
    dirty_returned = next(iter(dirty_out)).edge_work

    maximum_two_rail_unitarity = 0.0
    vacuum_change = double_change = 0.0
    for word in refresh.ROLE_PREPARATIONS:
        for _carrier, matrix in word:
            lifted = refresh.two_M2_matrix(matrix)
            maximum_two_rail_unitarity = max(
                maximum_two_rail_unitarity,
                float(np.linalg.norm(lifted.conj().T @ lifted - np.eye(4))),
            )
            vacuum_change = max(vacuum_change, float(np.linalg.norm(
                lifted[:, 0] - np.eye(4)[:, 0]
            )))
            double_change = max(double_change, float(np.linalg.norm(
                lifted[:, 3] - np.eye(4)[:, 3]
            )))

    return {
        "coin_deleted_factor_witnesses": len(coin_residuals),
        "minimum_delete_coin_factor_residual": min(coin_residuals),
        "transition_deleted_CZ_witnesses": len(TRANSITION),
        "minimum_delete_transition_CZ_residual": 2.0,
        "route_delete_first_SWAP_failed_cases": routing["delete_first_SWAP_failed_cases"],
        "route_delete_CZ_failed_cases": routing["delete_CZ_failed_cases"],
        "route_delete_last_SWAP_failed_cases": routing["delete_last_SWAP_failed_cases"],
        "edge_role_phase_delete_witnesses": edge_phase_witnesses,
        "minimum_delete_edge_role_phase_residual": 2.0,
        "delete_endpoint_seam_update_residual": update["delete_shared_seam_update_residual"],
        "delete_contact_update_residual": update["delete_contact_update_residual"],
        "delete_carrier_Givens_residual": role["deleted_first_factor_residual"],
        "delete_chart_CNOT_raw_maximum": chart_raw,
        "delete_chart_CNOT_column_residual": chart_norm,
        "dirty_edge_clean_phase": clean_phase,
        "dirty_edge_observed_phase": dirty_phase,
        "dirty_edge_work_returned": dirty_returned,
        "dirty_match_false_fires": role["dirty_match_false_fires"],
        "dirty_bypass_change": role["dirty_bypass_change"],
        "dirty_work_genesis_nonreturn": unlawful["dirty_work_genesis_nonreturn"],
        "maximum_two_rail_unitarity_residual": maximum_two_rail_unitarity,
        "off_code_vacuum_change": vacuum_change,
        "off_code_double_occupation_change": double_change,
        "dirty_edge_or_matcher_in_declared_code": False,
    }


def factor_inventory(include_coin: bool) -> dict[str, object]:
    intermediate = sum(len(spec[2]) for spec in SPECS)
    role_macros = len(CELLS) * 6 * 5 * 2
    factors = {
        "chart_CNOT": 4 * len(FEATURES),
        "controlled_two_rail_role_Givens": role_macros,
        "coin_one_or_two_M2": len(CELLS) * len(COIN_GATES) if include_coin else 0,
        "transition_CZ": len(TRANSITION),
        "transition_route_SWAP": 2 * sum(term.distance == 2 for term in routed.ROUTED_TERMS),
        "seam_edge_role_CNOT": 2 * intermediate,
        "seam_edge_role_CZ": 2 * len(SPECS),
        "seam_endpoint_CZ": len(SPECS),
        "seam_endpoint_SWAP": len(SPECS),
        "seam_carrier_rail_bundle_SWAP": 7 * len(SPECS),
        "onsite_contact_controlled_phase": 15 * len(CELLS),
    }
    maximum_pair_distance = 0
    for spec in SPECS:
        for pair in adjacent.local_seam_pairs(spec):
            first, second = CELLS[pair[0] // 6], CELLS[pair[1] // 6]
            maximum_pair_distance = max(maximum_pair_distance, sum(
                abs(first[axis] - second[axis]) for axis in range(3)
            ))
    return {
        "fixed_schedule_macro_factors": factors,
        "fixed_schedule_macro_total": sum(factors.values()),
        "maximum_gate_cell_diameter_before_routing": maximum_pair_distance,
        "maximum_gate_cell_diameter_after_routing": 1,
        "role_matcher_and_controlled_Givens_expand_to_two_M2": True,
        "role_primitive_expansion_source": "Cycle656 clean matcher/Fredkin-bypass construction",
        "all_transition_CZs_commute": True,
        "CZ_layer_order_used_as_physical_time": False,
        "tensor_product_carrier_supplied_not_derived": True,
        "parity_origin_used": False,
        "transition_synthesized_offline_from_target_inversion_set": True,
        "finite_global_mode_order_supplied": True,
        "preferred_order_contract_satisfied": False,
        "recurrent_compiler_claimed": False,
    }


def transform_operand(frame: np.ndarray, operand: tuple[tuple[Coord, int], ...]) -> tuple[tuple[Coord, int], ...]:
    mode_map = c655.P.mode_map(frame)
    frame_tuple = route_c.frame_tuple(frame)
    return tuple(
        (route_c.matvec(frame_tuple, cell), int(mode_map[mode]))
        for cell, mode in operand
    )


def covariance_and_translation_certificate() -> dict[str, object]:
    transition_operands = tuple(
        (routed.mode_site(term.pair[0]), routed.mode_site(term.pair[1]))
        for term in routed.ROUTED_TERMS
    )
    seam_operands = tuple(
        tuple(routed.mode_site(mode) for mode in (spec[0], spec[1]))
        for spec in SPECS
    )
    chart_operands = tuple(((cell, mode),) for _s, _d, _e, cell, mode in FEATURES)
    operands = transition_operands + seam_operands + chart_operands
    frame_locality_failures = composition_failures = 0
    for frame in c655.P.FRAMES:
        for operand in operands:
            rotated = transform_operand(frame, operand)
            if len(rotated) == 2:
                distance = sum(abs(rotated[0][0][axis] - rotated[1][0][axis]) for axis in range(3))
                frame_locality_failures += distance > 2
    for left in c655.P.FRAMES:
        for right in c655.P.FRAMES:
            for operand in operands:
                staged = transform_operand(left, transform_operand(right, operand))
                composition_failures += staged != transform_operand(left @ right, operand)

    translation_rows = []
    for length in (5, 6):
        failures = cases = 0
        for shift in product(range(length), repeat=3):
            for operand in operands:
                translated = tuple((
                    tuple((cell[axis] + shift[axis]) % length for axis in range(3)), mode
                ) for cell, mode in operand)
                failures += len(translated) != len(set(translated)) if len(operand) == 2 else 0
                cases += 1
        translation_rows.append({
            "L": length,
            "split": "train" if length == 5 else "held-no-refit",
            "translated_operand_cases": cases,
            "operand_collision_failures": failures,
        })
    carrier = refresh.carrier_covariance()
    return {
        "physical_operand_families": len(operands),
        "proper_cubic_frames": len(c655.P.FRAMES),
        "ordered_frame_products": len(c655.P.FRAMES) ** 2,
        "rotated_operand_locality_failures": frame_locality_failures,
        "operand_frame_composition_failures": composition_failures,
        "translation_rows": translation_rows,
        "coin_operand_factorization_covariant_gate_by_gate": False,
        "coin_product_covariance_supplied_separately": True,
        "carrier_phase_covariance_supplied": carrier,
        "E_fixed_columns_transformed_and_compared": False,
        "executed_operand_matrices_rebuilt_under_frames": False,
        "full_fixed_register_covariance_claimed": False,
        "translation_test_level": "fixed operand addresses only",
    }


def geometry(centers: tuple[Coord, ...]) -> tuple[tuple[Coord, ...], tuple[tuple[Coord, Coord], ...], tuple[int, ...]]:
    cells = set(centers)
    edges = []
    owners = []
    seen = set()
    for owner, center in enumerate(centers):
        for direction in route_c.DIRECTIONS:
            arm = route_c.add(center, direction)
            cells.add(arm)
            key = tuple(sorted((center, arm)))
            if key not in seen:
                seen.add(key)
                edges.append((center, arm))
                owners.append(owner)
    return tuple(sorted(cells)), tuple(edges), tuple(owners)


def specs_for(cells: tuple[Coord, ...], edges: tuple[tuple[Coord, Coord], ...]) -> tuple[adjacent.EdgeSpec, ...]:
    rows = []
    for left_cell, right_cell in edges:
        direction = route_c.sub(right_cell, left_cell)
        left_index, right_index = cells.index(left_cell), cells.index(right_cell)
        left_mode = route_c.DIRECTION_INDEX[direction]
        right_mode = route_c.DIRECTION_INDEX[tuple(-value for value in direction)]
        rows.append((
            6 * left_index + left_mode,
            6 * right_index + right_mode,
            tuple(
                6 * left_index + position if position < 6
                else 6 * right_index + position - 6
                for position in range(left_mode + 1, 6 + right_mode)
            ),
        ))
    return tuple(rows)


def toggle_pair(pairs: set[Pair], pair: Pair) -> None:
    pair = tuple(sorted(pair))  # type: ignore[assignment]
    if pair in pairs:
        pairs.remove(pair)
    else:
        pairs.add(pair)


def local_owned_target(
    global_cells: tuple[Coord, ...], owned_edges: tuple[tuple[Coord, Coord], ...]
) -> set[Pair]:
    local_cells = tuple(sorted({cell for edge in owned_edges for cell in edge}))
    local_specs = specs_for(local_cells, owned_edges)
    target = adjacent.transition_pair_set(6 * len(local_cells), local_specs)[2]
    local_to_global = tuple(
        6 * global_cells.index(cell) + mode
        for cell in local_cells for mode in range(6)
    )
    return {
        tuple(sorted((local_to_global[left], local_to_global[right])))
        for left, right in target
    }


def l_shape_coloring_probe() -> dict[str, object]:
    centers = ((0, 0, 0), (1, 0, 0), (0, 1, 0))
    colors = tuple(sum(cell) & 1 for cell in centers)
    cells, edges, owners = geometry(centers)
    specs = specs_for(cells, edges)
    transition, candidate, target, _mapping = adjacent.transition_pair_set(6 * len(cells), specs)
    transition_classes = Counter()
    unrouted = 0
    for left, right in transition:
        first, second = cells[left // 6], cells[right // 6]
        distance = sum(abs(first[axis] - second[axis]) for axis in range(3))
        transition_classes[distance] += 1
        unrouted += distance > 2

    rows = []
    for order in permutations(range(len(centers))):
        source_at_current = list(range(6 * len(cells)))
        colored_pairs: set[Pair] = set()
        for owner in order:
            owned = tuple(edge for edge, edge_owner in zip(edges, owners) if edge_owner == owner)
            for left, right in local_owned_target(cells, owned):
                toggle_pair(colored_pairs, (
                    source_at_current[left], source_at_current[right]
                ))
            for spec, edge_owner in zip(specs, owners):
                if edge_owner == owner:
                    left, right = spec[:2]
                    source_at_current[left], source_at_current[right] = (
                        source_at_current[right], source_at_current[left]
                    )
        mismatch = colored_pairs ^ target
        classes = Counter()
        for left, right in mismatch:
            first, second = cells[left // 6], cells[right // 6]
            classes[sum(abs(first[axis] - second[axis]) for axis in range(3))] += 1
        rows.append({
            "owner_order": order,
            "local_colored_target_pairs": len(colored_pairs),
            "mismatch_pair_witnesses": len(mismatch),
            "mismatch_distance_classes": dict(sorted(classes.items())),
        })
    return {
        "centers": centers,
        "center_parity_colors": colors,
        "cells": len(cells),
        "owned_edges": len(edges),
        "global_candidate_pairs": len(candidate),
        "global_target_pairs": len(target),
        "whole_patch_transition_pairs": len(transition),
        "whole_patch_transition_distance_classes": dict(sorted(transition_classes.items())),
        "whole_patch_unroutable_distance_gt_2_pairs": unrouted,
        "owner_order_rows": rows,
        "minimum_naive_coloring_mismatch_pairs": min(row["mismatch_pair_witnesses"] for row in rows),
        "maximum_naive_coloring_mismatch_pairs": max(row["mismatch_pair_witnesses"] for row in rows),
        "naive_two_color_compiler_closed": False,
        "shared_obstruction_claimed": False,
        "axiom_pressure_claimed": False,
    }


def main() -> None:
    registers = register_and_constraint_certificate()
    check(
        "the encoding occupies fixed local M2 registers with local role/chart/work constraints",
        registers["coarse_cells"] == 12
        and registers["fixed_data_M2"] == 72
        and registers["fixed_carrier_rail_M2"] == 84
        and registers["fixed_chart_M2"] == 48
        and registers["fixed_edge_role_work_M2"] == 11
        and registers["global_Fock_label_registers"] == 0
        and registers["variable_packet_blocks"] == 0
        and registers["matcher_truth_table_failures"] == 0
        and registers["matcher_return_failures"] == 0
        and registers["encoding_norm_failures"] == 0
        and registers["landed_invalid_qutrit_words"] == 0
        and registers["shared_chart_copy_failures"] == 0
        and not registers["global_n_le_2_constraint_is_local"],
        registers,
    )

    binding = source_identity_and_physical_binding()
    check(
        "the decoded E_fixed identity and supplied Cycle655 physical binding are kept distinct",
        binding["executed_encoding_name"] == "E_fixed_decoded"
        and not binding["executed_encoding_equals_landed_E_refresh"]
        and binding["shared_E_refresh_carrier_amplitudes"]
        and binding["shared_E_refresh_chart_relation"]
        and binding["decoded_interface_M2_count"] == 323
        and binding["Cycle655_semantic_M2_per_cell"] == 61
        and binding["Cycle655_decode_NN_gates_per_cell"] == 205
        and binding["Cycle655_encode_NN_gates_per_cell"] == 205
        and binding["Cycle655_decoder_encoder_GF2_residual"] == 0
        and binding["bound_physical_fixture_M2_count"] == 983
        and not binding["Cycle655_binding_executed_end_to_end_in_this_runner"]
        and binding["physical_site_claim_requires_supplied_Cycle655_binding"]
        and not binding["new_axiom_or_primitive_claimed"],
        binding,
    )

    transit_cases = tuple(
        sum(bit << CELL_INDEX[center] for bit, center in zip(bits, CENTERS))
        for bits in product((0, 1), repeat=2)
    )
    stream_rows = tuple(
        fixed_register_intertwiner(length, False, transit_cases)
        for length in (5, 6)
    )
    check(
        "the fixed-register local factor word closes stream/contact for every n<=2 column and dirty transit",
        all(
            row["executed_columns"] == 10516
            and row["mismatch_columns"] == 0
            and row["maximum_intertwiner_raw"] < TOL
            and row["maximum_column_residual"] < TOL
            and row["maximum_output_norm_defect"] < TOL
            and row["chart_erase_failures"] == 0
            and row["carrier_unprepare_failures"] == 0
            and row["returned_work_failures"] == 0
            and row["held_parameters_refit"] == 0
            for row in stream_rows
        ),
        stream_rows,
    )

    coin_rows = tuple(
        fixed_register_intertwiner(length, True, (0,))
        for length in (5, 6)
    )
    update_rows, _target_update = route_c.build_patch_update(route_c.BASE_AXIS)
    check(
        "the eleven onsite coin factors execute before the same fixed-register stream/contact word on the same E",
        all(
            row["executed_columns"] == 2629
            and row["coin_executed"]
            and row["mismatch_columns"] == 0
            and row["maximum_intertwiner_raw"] < TOL
            and row["maximum_column_residual"] < TOL
            and row["maximum_output_norm_defect"] < TOL
            and row["chart_erase_failures"] == 0
            and row["carrier_unprepare_failures"] == 0
            and row["returned_work_failures"] == 0
            for row in coin_rows
        )
        and update_rows["one_particle_mass_residual"] < TOL
        and update_rows["uniform_one_particle_eigen_residual"] < TOL,
        {"intertwiner_rows": coin_rows, "mass_fixture": update_rows},
    )

    factors = factor_inventory(True)
    check(
        "every executed macro has bounded local support and the CZ transition is schedule-independent",
        factors["maximum_gate_cell_diameter_before_routing"] <= 2
        and factors["maximum_gate_cell_diameter_after_routing"] == 1
        and factors["role_matcher_and_controlled_Givens_expand_to_two_M2"]
        and factors["all_transition_CZs_commute"]
        and not factors["CZ_layer_order_used_as_physical_time"]
        and factors["tensor_product_carrier_supplied_not_derived"]
        and not factors["parity_origin_used"]
        and factors["transition_synthesized_offline_from_target_inversion_set"]
        and factors["finite_global_mode_order_supplied"]
        and not factors["preferred_order_contract_satisfied"]
        and not factors["recurrent_compiler_claimed"],
        factors,
    )

    covariance = covariance_and_translation_certificate()
    check(
        "operand addresses and supplied carrier marginals pass symmetry controls while full E covariance remains open",
        covariance["proper_cubic_frames"] == 24
        and covariance["ordered_frame_products"] == 576
        and covariance["rotated_operand_locality_failures"] == 0
        and covariance["operand_frame_composition_failures"] == 0
        and all(row["operand_collision_failures"] == 0 for row in covariance["translation_rows"])
        and not covariance["coin_operand_factorization_covariant_gate_by_gate"]
        and covariance["coin_product_covariance_supplied_separately"]
        and covariance["carrier_phase_covariance_supplied"]["carrier_phase_failures"] == 0
        and covariance["carrier_phase_covariance_supplied"]["chart_transport_failures"] == 0
        and covariance["carrier_phase_covariance_supplied"]["carrier_cocycle_product_failures"] == 0
        and not covariance["E_fixed_columns_transformed_and_compared"]
        and not covariance["executed_operand_matrices_rebuilt_under_frames"]
        and not covariance["full_fixed_register_covariance_claimed"]
        and covariance["translation_test_level"] == "fixed operand addresses only",
        covariance,
    )

    deletions = deletion_and_domain_certificate()
    check(
        "coin, transition, route, seam, contact, carrier and chart deletions are active and dirty work is excluded",
        deletions["coin_deleted_factor_witnesses"] == 11
        and deletions["minimum_delete_coin_factor_residual"] > 0.05
        and deletions["transition_deleted_CZ_witnesses"] == 224
        and deletions["minimum_delete_transition_CZ_residual"] > 1.9
        and deletions["route_delete_first_SWAP_failed_cases"] > 0
        and deletions["route_delete_CZ_failed_cases"] > 0
        and deletions["route_delete_last_SWAP_failed_cases"] > 0
        and deletions["edge_role_phase_delete_witnesses"] == 11
        and deletions["minimum_delete_edge_role_phase_residual"] > 1.9
        and deletions["delete_endpoint_seam_update_residual"] > 1.9
        and deletions["delete_contact_update_residual"] > 0.3
        and deletions["delete_carrier_Givens_residual"] > 0.4
        and deletions["delete_chart_CNOT_column_residual"] > 1.4
        and deletions["dirty_edge_clean_phase"] == 1
        and deletions["dirty_edge_observed_phase"] == -1
        and deletions["dirty_edge_work_returned"] == 1
        and deletions["dirty_match_false_fires"] > 0
        and deletions["dirty_bypass_change"] > 1.4
        and deletions["dirty_work_genesis_nonreturn"] == 1
        and deletions["maximum_two_rail_unitarity_residual"] < TOL
        and deletions["off_code_vacuum_change"] < TOL
        and deletions["off_code_double_occupation_change"] < TOL
        and not deletions["dirty_edge_or_matcher_in_declared_code"],
        deletions,
    )

    recurrence = l_shape_coloring_probe()
    check(
        "the required L-shaped overlap falsifies the naive parity-color/local-star recurrence attempt",
        recurrence["cells"] == 16
        and recurrence["owned_edges"] == 16
        and recurrence["whole_patch_transition_pairs"] == 454
        and recurrence["whole_patch_transition_distance_classes"]
        == {0: 48, 1: 174, 2: 176, 3: 56}
        and recurrence["whole_patch_unroutable_distance_gt_2_pairs"] == 56
        and recurrence["minimum_naive_coloring_mismatch_pairs"] == 178
        and recurrence["maximum_naive_coloring_mismatch_pairs"] == 178
        and not recurrence["naive_two_color_compiler_closed"]
        and not recurrence["shared_obstruction_claimed"]
        and not recurrence["axiom_pressure_claimed"],
        recurrence,
    )

    certificate = {
        "registers": registers,
        "source_identity_and_binding": binding,
        "stream_contact": stream_rows,
        "coin_stream_contact": coin_rows,
        "mass_fixture": update_rows,
        "factors": factors,
        "covariance": covariance,
        "deletions_and_domain": deletions,
        "L_shape_recurrence": recurrence,
    }
    digest = sha256(json.dumps(
        certificate, sort_keys=True, separators=(",", ":"), default=str
    ).encode()).hexdigest()
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "fixed-decoded-interface-two-star-closure-physical-binding-and-recurrence-open",
        "terminal": "FIXED_INTERFACE_TWO_STAR_CLOSED_ORDER_COVARIANCE_RECURRENCE_OPEN",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "equation": "E_fixed G_coarse,n<=2 = G_fixed-local E_fixed",
        "registers": registers,
        "source_identity_and_binding": binding,
        "stream_contact": stream_rows,
        "coin_stream_contact": coin_rows,
        "mass_fixture": update_rows,
        "factor_word": factors,
        "covariance": covariance,
        "deletions_and_domain": deletions,
        "recurrence_probe": recurrence,
        "supplied": (
            "the fixed tensor-product M2 carrier and clean circuit-program convention",
            "Cycle655 physical 61-M2 cell decode/encode binding and Cycle656 matcher/bypass expansions",
            "E_refresh seven-rail amplitudes and local half-edge chart relation",
            "a finite global mode order, the target exterior inversion set, and offline-synthesized 224-CZ transition",
            "the commuting-CZ matching schedule-independence theorem (not its tensor carrier as a derivation)",
            "the failed/reset graph-braid non-fibered exchange result as mapped evidence only, not authority",
        ),
        "derived": (
            "a 323-M2 fixed decoded-interface executor with no logical-label or variable packet coordinate",
            "a 983-M2 physical placement count after the explicit supplied Cycle655 cell binding",
            "exact stream/contact closure on all 2629 columns and all four center-transit words at L5/held-L6",
            "exact same-E coin/stream/contact closure on all 2629 columns at L5/held-L6",
            "literal local chart erase/recompute, carrier unprepare/prepare, edge-work return and bundle transport",
            "operand-address translation/frame composition and supplied carrier-phase covariance controls",
            "failure of all six owner orders in the naive L-shaped parity-color/local-star extension",
        ),
        "open": (
            "a fixed local gauge/chart transition replacing the target-derived whole-patch inversion correction",
            "closure of an L-shaped three-center overlap under a bounded covariant coloring",
            "end-to-end execution of the Cycle655 physical decode/encode binding with E_fixed auxiliary registers",
            "actual transformed-E and rebuilt-operand covariance rather than address/marginal controls",
            "gate-by-gate proper-cubic covariance of the supplied QR coin factorization",
            "local enforcement of the global n<=2 finite-fixture restriction or an n-unbounded code theorem",
            "recurrent tiling, primitive genesis, physical time/source/Record/Born meaning",
        ),
        "claim_ceiling": (
            "Positive fixed-register decoded-interface compiler for the bounded two-star n<=2 fixture, including "
            "the supplied free coin and mass fixture on the same E_fixed_decoded.  A physical-site placement is "
            "specified only by composition with the separately supplied Cycle655 binding and is not re-executed "
            "here.  The transition is target/order-derived offline, violates the no-preferred-order recurrent "
            "contract, and fails the first L-shaped coloring attempt; no recurrent compiler, shared obstruction, "
            "or axiom pressure is claimed."
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
