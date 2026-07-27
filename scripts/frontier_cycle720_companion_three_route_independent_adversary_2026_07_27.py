#!/usr/bin/env python3
"""Cycle-720 independent adversarial reconstruction of companion-code routes.

This independent checker intentionally does not import the three top-level route
runners under review.  It loads their lower-level construction modules from a
caller-supplied checkout and independently rebuilds:

* the shared-register overlapping-box recurrent update;
* finite-open coframe preparation and the parity-twirl channel; and
* the 11N+E Choi stabilizer basis, local private corrections, triangular
  tree/plaquette pump, and one-ancilla Kraus signs.

The checker also separates a prepared Choi resource from an encoder acting on
a live input.  It has authority none and audit unset.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md"
AUDIT_INPUT_PATHS = (
    "docs/RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle720_bounded_general_clifford_orbit_2026_07_27.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
    "scripts/frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27.py",
    "scripts/frontier_cycle720_companion_parity_rail_local_gauge_2026_07_27.py",
    "scripts/frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py",
    "scripts/frontier_cycle720_companion_three_route_independent_adversary_2026_07_27.py",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py",
    "scripts/frontier_cycle720_product_companion_full_word_holonomy_2026_07_27.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import argparse
import ast
from collections import Counter, defaultdict
from hashlib import sha256
import importlib
from itertools import combinations, permutations, product
import json
import math
from pathlib import Path
import re
import sys
from typing import Iterable

import numpy as np


TOP_LEVEL_BLOCKLIST = {
    "frontier_cycle720_companion_recurrent_overlap_update_2026_07_27",
    "frontier_cycle720_companion_local_genesis_broadcast_2026_07_27",
    "frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27",
    "frontier_cycle720_companion_fixed_sector_even_car_bell_2026_07_27",
}
TOL = 4.0e-10

M = U = F = O = R = Q = T = F128 = S25 = None
Pauli = object


def load_dependencies(source_root: Path) -> None:
    global M, U, F, O, R, Q, T, F128, S25, Pauli
    scripts = (source_root / "scripts").resolve()
    if not scripts.is_dir():
        raise SystemExit(f"missing Cycle-720 scripts directory: {scripts}")
    sys.path.insert(0, str(scripts))
    names = {
        "M": "frontier_cycle720_cell_majorana_companion_geometry_2026_07_27",
        "U": "frontier_cycle720_companion_subsystem_m2_update_2026_07_27",
        "F": "frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27",
        "O": "frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27",
        "R": "frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27",
        "Q": "frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27",
        "T": "frontier_cycle708_endpoint_cube_tableau_core_2026_07_26",
        "F128": "frontier_full128_cycle_encoder_2026_07_24",
        "S25": "frontier_full128_25site_nn_circuit_core_2026_07_24",
    }
    loaded = {key: importlib.import_module(name) for key, name in names.items()}
    M, U, F, O, R, Q, T, F128, S25 = (
        loaded[key] for key in ("M", "U", "F", "O", "R", "Q", "T", "F128", "S25")
    )
    Pauli = M.Pauli
    forbidden = sorted(TOP_LEVEL_BLOCKLIST & set(sys.modules))
    if forbidden:
        raise AssertionError(f"top-level runners imported transitively: {forbidden}")


def gf2_rank(rows: Iterable[int]) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def gf2_combination(target: int, generators: tuple[int, ...]) -> int | None:
    pivots: dict[int, tuple[int, int]] = {}
    for index, original in enumerate(generators):
        row = original
        combination = 1 << index
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                old, old_combination = pivots[pivot]
                row ^= old
                combination ^= old_combination
            else:
                pivots[pivot] = (row, combination)
                break
    row = target
    combination = 0
    while row:
        pivot = row.bit_length() - 1
        if pivot not in pivots:
            return None
        old, old_combination = pivots[pivot]
        row ^= old
        combination ^= old_combination
    return combination


def independent_rows(rows: tuple, qubits: int) -> tuple:
    pivots: dict[int, int] = {}
    output = []
    for candidate in rows:
        row = candidate.symplectic(qubits)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                output.append(candidate)
                break
    return tuple(output)


def pauli_product(rows: Iterable) -> object:
    output = Pauli()
    for row in rows:
        output = output @ row
    return output


def signed_span_failures(targets: tuple, basis: tuple, qubits: int) -> int:
    vectors = tuple(row.symplectic(qubits) for row in basis)
    failures = 0
    for target in targets:
        combination = gf2_combination(target.symplectic(qubits), vectors)
        if combination is None:
            failures += 1
            continue
        replay = pauli_product(
            basis[index]
            for index in range(len(basis))
            if (combination >> index) & 1
        )
        failures += replay != target
    return failures


def hermitian_sign(row) -> int:
    """Return +1/-1 for a Hermitian Pauli, raising otherwise."""
    y_parity = (row.x & row.z).bit_count() & 1
    if (row.phase - y_parity) & 1:
        raise AssertionError("non-Hermitian stabilizer row")
    return 1 if ((row.phase - y_parity) % 4) == 0 else -1


def symplectic(left, right, qubits: int) -> int:
    return (
        ((left.x & right.z).bit_count() + (left.z & right.x).bit_count()) & 1
    )


def arbitrary_fixture(cells: Iterable[tuple[int, int, int]]):
    cells = tuple(sorted(set(cells)))
    lookup = {cell: index for index, cell in enumerate(cells)}
    edges = []
    for cell in cells:
        for axis in range(3):
            target = list(cell)
            target[axis] += 1
            target = tuple(target)
            if target not in lookup:
                continue
            left, right = lookup[cell], lookup[target]
            edges.append((
                left, right, cell, axis,
                6 * left + 2 * axis + 1,
                6 * right + 2 * axis,
            ))
    return M.CompanionFixture(
        (0, 0, 0), cells, tuple(edges), 6 * len(cells), 9 * len(cells)
    )


def semantic_keys(fixture) -> set[tuple]:
    coin, _mass, _phase = F128.common_coin()
    coin_schedule, _residual = S25.compile_adjacent_qr(coin)
    output = set()
    for cell in fixture.cells:
        output.update(("coin", cell, factor) for factor in range(len(coin_schedule)))
        output.update(("reverse", cell, axis) for axis in range(3))
        output.update(
            ("contact", cell, left, right)
            for left, right in combinations(range(6), 2)
        )
    for _left, _right, owner, axis, *_rest in fixture.edges:
        output.update(("seam", owner, axis, factor) for factor in range(4))
    return output


def embed_view_pauli(source, target, row):
    """Coordinate-embed a view Pauli into the one global register set."""
    lookup = {cell: index for index, cell in enumerate(target.cells)}
    x = z = 0
    for source_cell, cell in enumerate(source.cells):
        target_cell = lookup[cell]
        for mode in range(6):
            old, new = 6 * source_cell + mode, 6 * target_cell + mode
            x |= ((row.x >> old) & 1) << new
            z |= ((row.z >> old) & 1) << new
        for axis in range(3):
            old = source.matter_qubits + 3 * source_cell + axis
            new = target.matter_qubits + 3 * target_cell + axis
            x |= ((row.x >> old) & 1) << new
            z |= ((row.z >> old) & 1) << new
    return Pauli(row.phase, x, z)


def decode_coordinate_failures(fixture, factor) -> dict[str, int]:
    logical_mask = (1 << factor.logical) - 1
    gauge_mask = ((1 << factor.gauge) - 1) << factor.logical
    failures = Counter()
    gauge_rows = (
        factor.physical_w[factor.logical:factor.logical + factor.gauge]
        + factor.physical_v[factor.logical:factor.logical + factor.gauge]
    )
    center_rows = factor.physical_w[
        factor.logical + factor.gauge:
        factor.logical + factor.gauge + factor.center
    ]
    for _family, physical, target in M.operator_rows(fixture):
        pc = T.decode(physical, factor.physical_w, factor.physical_v, fixture.qubits)
        tc = T.decode(target, factor.target_w, factor.target_v, fixture.matter_qubits)
        failures["logical"] += (
            (pc.v_mask & logical_mask) != (tc.v_mask & logical_mask)
            or (pc.w_mask & logical_mask) != (tc.w_mask & logical_mask)
        )
        failures["gauge"] += bool(pc.v_mask & gauge_mask)
        failures["gauge"] += bool(pc.w_mask & gauge_mask)
        physical_parity = (
            pc.w_mask >> (factor.logical + factor.gauge + factor.center - 1)
        ) & 1
        target_parity = (tc.w_mask >> factor.logical) & 1
        failures["parity"] += physical_parity != target_parity
        for odd in (0, 1):
            failures["sector_sign"] += (
                (pc.phase + 2 * odd * physical_parity) % 4
                != (tc.phase + 2 * odd * target_parity) % 4
            )
        failures["gauge_commutator"] += sum(
            symplectic(physical, gauge, fixture.qubits) for gauge in gauge_rows
        )
        failures["center_commutator"] += sum(
            symplectic(physical, center, fixture.qubits) for center in center_rows
        )
    return dict(failures)


def expansion_word(rows: tuple, order: tuple[int, ...]) -> dict[tuple[int, int], complex]:
    output = {(0, 0): 1.0 + 0.0j}
    for index in order:
        stabilizer = rows[index]
        updated: dict[tuple[int, int], complex] = {}
        for (x, z), coefficient in output.items():
            updated[(x, z)] = updated.get((x, z), 0.0j) + coefficient / math.sqrt(2)
            product_row = Pauli(0, x, z) @ stabilizer
            key = (product_row.x, product_row.z)
            updated[key] = updated.get(key, 0.0j) - 1j * (1j ** product_row.phase) * coefficient / math.sqrt(2)
        output = {key: value for key, value in updated.items() if abs(value) > 1e-13}
    return output


def expansion_distance(left: dict, right: dict) -> float:
    return float(math.sqrt(sum(
        abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2
        for key in set(left) | set(right)
    )))


def recurrent_certificate() -> dict[str, object]:
    left_cells = set(Q.shape_cells((2, 2, 2), (0, 0, 0)))
    right_cells = set(Q.shape_cells((2, 2, 2), (1, 0, 0)))
    union_cells = left_cells | right_cells
    left, right, union = map(arbitrary_fixture, (left_cells, right_cells, union_cells))
    shared = tuple(sorted(left_cells & right_cells))
    left_index = {cell: index for index, cell in enumerate(left.cells)}
    right_index = {cell: index for index, cell in enumerate(right.cells)}
    union_index = {cell: index for index, cell in enumerate(union.cells)}
    shared_embedding_failures = 0
    for cell in shared:
        for local in range(9):
            union_qubit = 6 * union_index[cell] + local if local < 6 else union.matter_qubits + 3 * union_index[cell] + local - 6
            left_qubit = 6 * left_index[cell] + local if local < 6 else left.matter_qubits + 3 * left_index[cell] + local - 6
            right_qubit = 6 * right_index[cell] + local if local < 6 else right.matter_qubits + 3 * right_index[cell] + local - 6
            for kind in ("X", "Z"):
                left_row = Pauli(
                    x=(1 << left_qubit) if kind == "X" else 0,
                    z=(1 << left_qubit) if kind == "Z" else 0,
                )
                right_row = Pauli(
                    x=(1 << right_qubit) if kind == "X" else 0,
                    z=(1 << right_qubit) if kind == "Z" else 0,
                )
                expected = Pauli(
                    x=(1 << union_qubit) if kind == "X" else 0,
                    z=(1 << union_qubit) if kind == "Z" else 0,
                )
                shared_embedding_failures += embed_view_pauli(left, union, left_row) != expected
                shared_embedding_failures += embed_view_pauli(right, union, right_row) != expected

    keys_left, keys_right, keys_union = map(semantic_keys, (left, right, union))
    cover = keys_left | keys_right
    factor = O.build_factorization(union)
    coordinate_failures = decode_coordinate_failures(union, factor)
    placed = U.placement(union)
    word, word_report = U.physical_word(union, placed)
    routed, route_report = U.c707.route_word(word)

    categories = []
    compressed_seam_factors = []
    prior_seam = None
    unitarity_residual = 0.0
    for instruction in word:
        kind = instruction.kind
        category = (
            "coin" if kind.startswith("coin_")
            else "reverse" if kind == "reverse_FSWAP"
            else "seam" if kind.startswith("seam_")
            else "contact" if kind == "onsite_contact"
            else "unknown"
        )
        categories.append(category)
        unitarity_residual = max(unitarity_residual, float(np.linalg.norm(
            instruction.matrix.conj().T @ instruction.matrix
            - np.eye(instruction.matrix.shape[0])
        )))
        if category == "seam":
            match = re.search(r"_f([0-3])_", kind)
            if not match:
                compressed_seam_factors.append(-1)
            else:
                factor_index = int(match.group(1))
                if factor_index != prior_seam:
                    compressed_seam_factors.append(factor_index)
                    prior_seam = factor_index
        else:
            prior_seam = None
    rank = {name: index for index, name in enumerate(("coin", "reverse", "seam", "contact"))}
    category_order_failures = sum(
        category == "unknown" or rank[category] < rank[previous]
        for previous, category in zip(categories, categories[1:])
    )
    seam_factor_pattern_failures = sum(
        tuple(compressed_seam_factors[index:index + 4]) != (0, 1, 2, 3)
        for index in range(0, len(compressed_seam_factors), 4)
    )

    minimal = arbitrary_fixture(Q.shape_cells((2, 1, 1)))
    seam_rows = minimal.physical_terms(0)
    frozen = expansion_word(seam_rows, (0, 1, 2, 3))
    reversed_groups = expansion_word(seam_rows, (1, 0, 3, 2))
    hostile = expansion_word(seam_rows, (0, 2, 1, 3))
    deleted = expansion_word(seam_rows, (1, 2, 3))
    cross_edge_commutators = 0
    within_edge_noncommuting = 0
    blocks = tuple(union.physical_terms(edge) for edge in range(len(union.edges)))
    for edge, rows in enumerate(blocks):
        within_edge_noncommuting += sum(
            symplectic(rows[left_index_], rows[right_index_], union.qubits)
            for left_index_ in range(4) for right_index_ in range(left_index_)
        )
        cross_edge_commutators += sum(
            symplectic(a, b, union.qubits)
            for earlier in blocks[:edge] for a in rows for b in earlier
        )

    return {
        "union_cells": len(union.cells),
        "shared_cells": len(shared),
        "union_registers": union.qubits,
        "shared_registers": 9 * len(shared),
        "shared_embedding_failures": shared_embedding_failures,
        "cover_missing_factors": len(keys_union - cover),
        "cover_excess_factors": len(cover - keys_union),
        "duplicated_view_factors": len(keys_left & keys_right),
        "coordinate_failures": coordinate_failures,
        "placement_collisions": placed["placement_collisions"],
        "word_category_order_failures": category_order_failures,
        "seam_factor_pattern_failures": seam_factor_pattern_failures,
        "word_unitarity_residual": unitarity_residual,
        "logical_update_factors": word_report["logical_update_factors"],
        "expected_logical_update_factors": 29 * len(union.cells) + 4 * len(union.edges),
        "runtime_parity_queries": word_report["runtime_parity_queries"],
        "sector_conditioned_gates": word_report["sector_conditioned_gates"],
        "route_return_failures": route_report["route_return_failures"],
        "route_non_NN_failures": route_report["non_NN_failures"],
        "routed_primitives": len(routed),
        "cross_edge_seam_commutators": cross_edge_commutators,
        "within_edge_noncommuting_pairs": within_edge_noncommuting,
        "orientation_reversal_residual": expansion_distance(frozen, reversed_groups),
        "hostile_interleave_residual": expansion_distance(frozen, hostile),
        "factor_deletion_residual": expansion_distance(frozen, deleted),
        "recurrence_proof_class": (
            "factorwise signed-coordinate equality plus one fixed ordered "
            "unitary word; recurrence is algebraic induction on the declared "
            "code, not a fresh state-space execution at every power"
        ),
    }


def tree_parent(cells, root, order):
    cell_set = set(cells)
    parent = {root: None}
    for cell in cells:
        if cell == root:
            continue
        for axis in order:
            if cell[axis] != root[axis]:
                candidate = list(cell)
                candidate[axis] += 1 if cell[axis] < root[axis] else -1
                candidate = tuple(candidate)
                if candidate not in cell_set:
                    raise AssertionError("parent left box")
                parent[cell] = candidate
                break
        else:
            raise AssertionError("missing parent")
    return parent


def edge_axis(left, right):
    axes = [axis for axis in range(3) if left[axis] != right[axis]]
    if len(axes) != 1 or abs(left[axes[0]] - right[axes[0]]) != 1:
        raise AssertionError("non-NN edge")
    return axes[0]


def contour(cells, root, order, coframe_seed, parity_seed, dirty_coframe=0, dirty_parity=0):
    parent = tree_parent(cells, root, order)
    axis_rank = {axis: index for index, axis in enumerate(order)}
    children = {cell: [] for cell in cells}
    for child, owner in parent.items():
        if owner is not None:
            children[owner].append(child)
    children = {
        cell: tuple(sorted(rows, key=lambda child: (axis_rank[edge_axis(cell, child)], child)))
        for cell, rows in children.items()
    }
    lookup = {cell: index for index, cell in enumerate(cells)}
    coframe = dirty_coframe | (coframe_seed << (3 * lookup[root]))
    parity = dirty_parity | (parity_seed << lookup[root])
    current, incoming = root, None
    control_visits = [root]
    transitions = []
    while True:
        ports = children[current]
        if incoming is None or incoming == parent[current]:
            outgoing = ports[0] if ports else parent[current]
        else:
            index = ports.index(incoming)
            outgoing = ports[index + 1] if index + 1 < len(ports) else parent[current]
        if outgoing is None:
            break
        if parent[outgoing] == current:
            child = outgoing
            for axis in range(3):
                control = 3 * lookup[current] + axis
                target = 3 * lookup[child] + axis
                coframe ^= ((coframe >> control) & 1) << target
            coframe ^= 1 << (3 * lookup[child] + edge_axis(current, child))
            parity ^= ((parity >> lookup[current]) & 1) << lookup[child]
            transitions.append((current, child, "down"))
            current, incoming = child, current
            control_visits.append(current)
        else:
            child, owner = current, outgoing
            parity ^= ((parity >> lookup[owner]) & 1) << lookup[child]
            transitions.append((child, owner, "up"))
            current, incoming = owner, child
    assignment = tuple((coframe >> (3 * index)) & 7 for index in range(len(cells)))
    return assignment, parity, tuple(control_visits), tuple(transitions)


def expected_coframe(cells, seed):
    return tuple(
        sum((((cell[axis] & 1) ^ ((seed >> axis) & 1)) << axis) for axis in range(3))
        for cell in cells
    )


def one_qubit_parity_twirl_dilation() -> dict[str, float]:
    h = np.asarray(((1, 1), (1, -1)), complex) / math.sqrt(2)
    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), complex)
    z = np.diag((1, -1)).astype(complex)
    p0 = np.diag((1, 0)).astype(complex)
    p1 = np.diag((0, 1)).astype(complex)
    controlled_z = np.kron(p0, identity) + np.kron(p1, z)
    # For the twirl the seed is traced after the controlled parity.  The
    # Bell reference only purifies the equal classical seed weights.
    unitary = controlled_z @ np.kron(h, identity)
    k0 = unitary[0:2, 0:2]
    k1 = unitary[2:4, 0:2]
    expected = identity / math.sqrt(2), z / math.sqrt(2)
    return {
        "K0_residual": float(np.linalg.norm(k0 - expected[0])),
        "K1_residual": float(np.linalg.norm(k1 - expected[1])),
        "completeness_residual": float(np.linalg.norm(
            k0.conj().T @ k0 + k1.conj().T @ k1 - identity
        )),
    }


def genesis_certificate() -> dict[str, object]:
    shapes = ((2, 2, 2), (3, 2, 2), (5, 3, 2))
    failures = Counter()
    distribution_digests = {}
    dirty_tests = dirty_collisions = 0
    parity_visits = []
    root_dependent_seed_label_mismatches = 0
    for shape in shapes:
        cells = tuple(Q.shape_cells(shape))
        expected_set = {expected_coframe(cells, seed) for seed in range(8)}
        bounds = tuple((min(cell[a] for cell in cells), max(cell[a] for cell in cells)) for a in range(3))
        digests = set()
        for root in product(*bounds):
            for order in permutations(range(3)):
                outputs = []
                for seed in range(8):
                    assignment, parity, visits, transitions = contour(cells, root, order, seed, 1)
                    outputs.append(assignment)
                    failures["coframe_constraint_or_support"] += assignment not in expected_set
                    root_dependent_seed_label_mismatches += (
                        assignment != expected_coframe(cells, seed)
                    )
                    failures["parity_return"] += parity != (1 << cells.index(root))
                    failures["contour_length"] += len(transitions) != 2 * (len(cells) - 1)
                    failures["visit_once"] += len(visits) != len(cells) or len(set(visits)) != len(cells)
                    parity_visits.extend(Counter(visits).values())
                digests.add(sha256(repr(tuple(sorted(outputs))).encode()).hexdigest())
        distribution_digests[str(shape)] = len(digests)
        canonical_root = tuple(low for low, _high in bounds)
        for index, cell in enumerate(cells):
            if cell == canonical_root:
                continue
            dirty_tests += 4
            clean, clean_parity, _visits, _transitions = contour(cells, canonical_root, (0, 1, 2), 0, 1)
            for axis in range(3):
                dirty, _parity, _v, _t = contour(
                    cells, canonical_root, (0, 1, 2), 0, 1,
                    dirty_coframe=1 << (3 * index + axis),
                )
                dirty_collisions += dirty == clean
            _assignment, dirty_p, _v, _t = contour(
                cells, canonical_root, (0, 1, 2), 0, 1,
                dirty_parity=1 << index,
            )
            dirty_collisions += dirty_p == clean_parity
    twirl = one_qubit_parity_twirl_dilation()
    return {
        "shapes": shapes,
        "failures": dict(failures),
        "distinct_distribution_digests": distribution_digests,
        "minimum_parity_control_visits": min(parity_visits),
        "maximum_parity_control_visits": max(parity_visits),
        "dirty_target_tests": dirty_tests,
        "dirty_targets_hidden": dirty_collisions,
        "root_dependent_seed_label_mismatches": (
            root_dependent_seed_label_mismatches
        ),
        "sector_label_boundary": (
            "the uniform eight-sector density is root/order independent, but "
            "the map from the three raw root seed bits to an absolute sector "
            "label is chart dependent; a retained typed sector input must "
            "carry or quotient that preparation chart"
        ),
        "dirty_target_rejection_mechanism_present": False,
        "dirty_target_boundary": (
            "dirty targets change the output and are not hidden, but the route "
            "only declares a clean-input domain; it does not dynamically reject "
            "or repair a dirty preparation register"
        ),
        "one_qubit_twirl_dilation": twirl,
        "parity_superselection_explanation_derived": False,
    }


def direct_graph_basis(fixture) -> tuple[tuple, tuple[tuple, ...]]:
    rows, tags = [], []
    for cell in range(len(fixture.cells)):
        for mode in range(6):
            row = Pauli(z=1 << (6 * cell + mode))
            rows.append(R.choi_pauli(row, row, fixture.qubits))
            tags.append(("onsite_Z", cell, mode))
        for mode in range(5):
            row = Pauli(x=(1 << (6 * cell + mode)) | (1 << (6 * cell + mode + 1)))
            rows.append(R.choi_pauli(row, row, fixture.qubits))
            tags.append(("onsite_XX", cell, mode))
    for edge in range(len(fixture.edges)):
        rows.append(R.choi_pauli(
            fixture.physical_terms(edge)[2], fixture.target_terms(edge)[2], fixture.qubits
        ))
        tags.append(("edge", edge))
    return tuple(rows), tuple(tags)


def repeated_star_basis(fixture) -> tuple:
    entries = []
    union_cells = set(fixture.cells)
    for center in fixture.cells:
        patch_cells = {center} | {
            R.add(center, direction) for direction in R.DIRECTIONS
            if R.add(center, direction) in union_cells
        }
        patch = arbitrary_fixture(patch_cells)
        factor = O.build_factorization(patch)
        entries.extend(R.channel_graph_entries(patch, factor, patch_cells, fixture, True))
    return independent_rows(tuple(row for row, _support in entries), fixture.qubits + fixture.matter_qubits)


def incident_mask(fixture, cell: int) -> int:
    mask = 0
    for left, right, _owner, axis, *_rest in fixture.edges:
        if cell == left:
            mask |= 1 << (2 * axis + 1)
        elif cell == right:
            mask |= 1 << (2 * axis)
    return mask


def onsite_allowed(fixture, cell: int) -> tuple[int, ...]:
    return tuple(
        list(range(6 * cell, 6 * cell + 6))
        + list(range(fixture.matter_qubits + 3 * cell, fixture.matter_qubits + 3 * cell + 3))
        + list(range(fixture.qubits + 6 * cell, fixture.qubits + 6 * cell + 6))
    )


def edge_allowed(fixture, edge: int) -> tuple[int, ...]:
    left, right, *_rest = fixture.edges[edge]
    return tuple(
        fixture.matter_qubits + 3 * cell + local
        for cell in (left, right) for local in range(3)
    )


def solve_binary(equations: list[tuple[int, int]]) -> tuple[int, int]:
    pivots: dict[int, tuple[int, int]] = {}
    contradictions = 0
    for mask, rhs in equations:
        while mask:
            pivot = mask.bit_length() - 1
            if pivot in pivots:
                old_mask, old_rhs = pivots[pivot]
                mask ^= old_mask
                rhs ^= old_rhs
            else:
                pivots[pivot] = (mask, rhs)
                break
        else:
            contradictions += rhs
    solution = 0
    for pivot in sorted(pivots):
        mask, rhs = pivots[pivot]
        other = mask & ~(1 << pivot)
        value = rhs ^ ((other & solution).bit_count() & 1)
        solution |= value << pivot
    return solution, contradictions


def solve_correction(rows: tuple, target: int, allowed: tuple[int, ...]):
    equations = []
    for index, stabilizer in enumerate(rows):
        mask = 0
        for variable, qubit in enumerate(allowed):
            mask |= ((stabilizer.z >> qubit) & 1) << (2 * variable)
            mask |= ((stabilizer.x >> qubit) & 1) << (2 * variable + 1)
        equations.append((mask, int(index == target)))
    solution, contradictions = solve_binary(equations)
    x = sum(((solution >> (2 * variable)) & 1) << qubit for variable, qubit in enumerate(allowed))
    z = sum(((solution >> (2 * variable + 1)) & 1) << qubit for variable, qubit in enumerate(allowed))
    return Pauli((x & z).bit_count() & 1, x, z), contradictions


def local_signature(row, allowed):
    return (
        sum(((row.x >> qubit) & 1) << index for index, qubit in enumerate(allowed)),
        sum(((row.z >> qubit) & 1) << index for index, qubit in enumerate(allowed)),
    )


def signature_pauli(signature, allowed):
    local_x, local_z = signature
    x = sum(((local_x >> index) & 1) << qubit for index, qubit in enumerate(allowed))
    z = sum(((local_z >> index) & 1) << qubit for index, qubit in enumerate(allowed))
    return Pauli((x & z).bit_count() & 1, x, z)


def correction_key(fixture, tag):
    if tag[0] == "edge":
        edge = tag[1]
        left, right, _owner, axis, *_rest = fixture.edges[edge]
        return ("edge", incident_mask(fixture, left), incident_mask(fixture, right), axis)
    return ("onsite", incident_mask(fixture, tag[1]), tag[0], tag[2])


def allowed_for_tag(fixture, tag):
    return edge_allowed(fixture, tag[1]) if tag[0] == "edge" else onsite_allowed(fixture, tag[1])


def correction_from_signature(signature, fixture, tag):
    return signature_pauli(signature, allowed_for_tag(fixture, tag))


def syndrome_failures(rows, target, correction, qubits):
    return sum(
        symplectic(correction, stabilizer, qubits) != int(index == target)
        for index, stabilizer in enumerate(rows)
    )


def build_independent_atlas() -> tuple[dict[tuple, tuple[int, int]], dict[str, int]]:
    atlas: dict[tuple, tuple[int, int]] = {}
    report = Counter()
    for shape in product(range(1, 5), repeat=3):
        fixture = arbitrary_fixture(Q.shape_cells(shape))
        rows, tags = direct_graph_basis(fixture)
        total = fixture.qubits + fixture.matter_qubits
        for target, tag in enumerate(tags):
            key = correction_key(fixture, tag)
            allowed = allowed_for_tag(fixture, tag)
            if key not in atlas:
                correction, contradictions = solve_correction(rows, target, allowed)
                report["solve_contradictions"] += contradictions
                atlas[key] = local_signature(correction, allowed)
            correction = correction_from_signature(atlas[key], fixture, tag)
            report["training_syndrome_failures"] += syndrome_failures(
                rows, target, correction, total
            )
            report["maximum_weight"] = max(
                report["maximum_weight"], (correction.x | correction.z).bit_count()
            )
    report["atlas_keys"] = len(atlas)
    report["onsite_keys"] = sum(key[0] == "onsite" for key in atlas)
    report["edge_keys"] = sum(key[0] == "edge" for key in atlas)
    return atlas, dict(report)


def coordinate_maps(fixture, root, order):
    signs = tuple(
        1 if root[axis] == min(cell[axis] for cell in fixture.cells) else -1
        for axis in range(3)
    )
    forward = {
        cell: tuple(signs[axis] * (cell[axis] - root[axis]) for axis in order)
        for cell in fixture.cells
    }
    return forward, {value: cell for cell, value in forward.items()}


def edge_lookup(fixture):
    return {
        frozenset((fixture.cells[left], fixture.cells[right])): edge
        for edge, (left, right, *_rest) in enumerate(fixture.edges)
    }


def tree_plaquette_schedule(fixture, root, order):
    forward, reverse = coordinate_maps(fixture, root, order)
    lookup = edge_lookup(fixture)
    lengths = tuple(max(value[index] for value in forward.values()) + 1 for index in range(3))

    def edge(left_u, right_u):
        return lookup[frozenset((reverse[tuple(left_u)], reverse[tuple(right_u)]))]

    def plaquette(base, axis_a, axis_b):
        a, b, ab = list(base), list(base), list(base)
        a[axis_a] += 1
        b[axis_b] += 1
        ab[axis_a] += 1
        ab[axis_b] += 1
        return (edge(base, a), edge(base, b), edge(a, ab), edge(b, ab))

    tree = []
    for cell in fixture.cells:
        u = forward[cell]
        if u[0] > 0:
            parent = list(u); parent[0] -= 1
        elif u[1] > 0:
            parent = list(u); parent[1] -= 1
        elif u[2] > 0:
            parent = list(u); parent[2] -= 1
        else:
            continue
        tree.append(edge(u, parent))
    prepared, fill = set(tree), []

    def add_new(new_edge, cycle):
        if new_edge in prepared or any(item not in prepared for item in cycle if item != new_edge):
            raise AssertionError("non-triangular plaquette")
        fill.append((new_edge, cycle))
        prepared.add(new_edge)

    for slow in range(lengths[2]):
        for middle in range(lengths[1] - 1):
            for fast in range(1, lengths[0]):
                base = (fast - 1, middle, slow)
                cycle = plaquette(base, 0, 1)
                add_new(edge((fast, middle, slow), (fast, middle + 1, slow)), cycle)
    for slow in range(lengths[2] - 1):
        for fast in range(1, lengths[0]):
            base = (fast - 1, 0, slow)
            cycle = plaquette(base, 0, 2)
            add_new(edge((fast, 0, slow), (fast, 0, slow + 1)), cycle)
    for slow in range(lengths[2] - 1):
        for middle in range(1, lengths[1]):
            for fast in range(lengths[0]):
                base = (fast, middle - 1, slow)
                cycle = plaquette(base, 1, 2)
                add_new(edge((fast, middle, slow), (fast, middle, slow + 1)), cycle)
    if prepared != set(range(len(fixture.edges))):
        raise AssertionError("schedule missed edges")
    return tuple(tree), tuple(fill)


def scheduled_basis(fixture):
    direct, tags = direct_graph_basis(fixture)
    onsite_count = 11 * len(fixture.cells)
    seam = direct[onsite_count:]
    tree, fill = tree_plaquette_schedule(fixture, min(fixture.cells), (2, 1, 0))
    rows = list(direct[:onsite_count]) + [seam[edge] for edge in tree]
    scheduled_tags = list(tags[:onsite_count]) + [("edge", edge) for edge in tree]
    for new_edge, cycle in fill:
        rows.append(pauli_product(seam[edge] for edge in cycle))
        scheduled_tags.append(("edge", new_edge))
    return tuple(rows), tuple(scheduled_tags), {"tree": len(tree), "fill": len(fill)}


def pump_kraus_sign_certificate() -> dict[str, float]:
    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), complex)
    z = np.diag((1, -1)).astype(complex)
    h = np.asarray(((1, 1), (1, -1)), complex) / math.sqrt(2)
    p0 = np.diag((1, 0)).astype(complex)
    p1 = np.diag((0, 1)).astype(complex)
    residuals = {}
    for sign in (1, -1):
        stabilizer = sign * z
        controlled_s = np.kron(p0, identity) + np.kron(p1, stabilizer)
        controlled_c = np.kron(p0, identity) + np.kron(p1, x)
        unitary = controlled_c @ np.kron(h, identity) @ controlled_s @ np.kron(h, identity)
        k0, k1 = unitary[0:2, 0:2], unitary[2:4, 0:2]
        p_plus = (identity + stabilizer) / 2
        p_minus = (identity - stabilizer) / 2
        residuals[f"sign_{sign}_Kplus"] = float(np.linalg.norm(k0 - p_plus))
        residuals[f"sign_{sign}_Kminus"] = float(np.linalg.norm(k1 - x @ p_minus))
        residuals[f"sign_{sign}_completeness"] = float(np.linalg.norm(
            k0.conj().T @ k0 + k1.conj().T @ k1 - identity
        ))
        residuals[f"sign_{sign}_prepared_plus"] = float(max(
            np.linalg.norm(stabilizer @ k0 - k0),
            np.linalg.norm(stabilizer @ k1 - k1),
        ))
    return residuals


def choi_certificate(source_root: Path) -> dict[str, object]:
    atlas, atlas_report = build_independent_atlas()
    training_shapes = set(product(range(1, 5), repeat=3))
    advertised = ((2, 2, 2), (3, 2, 2), (3, 3, 2), (5, 3, 2), (4, 4, 3))
    genuinely_held = tuple(shape for shape in advertised if shape not in training_shapes)
    atlas_overlap = tuple(shape for shape in advertised if shape in training_shapes)
    held_shapes = ((5, 3, 2), (5, 5, 3), (6, 5, 4))
    held = []
    for shape in held_shapes:
        fixture = arbitrary_fixture(Q.shape_cells(shape))
        rows, tags = direct_graph_basis(fixture)
        total = fixture.qubits + fixture.matter_qubits
        failures = 0
        unseen_keys = set()
        max_weight = 0
        for target, tag in enumerate(tags):
            key = correction_key(fixture, tag)
            if key not in atlas:
                failures += 1
                unseen_keys.add(key)
                continue
            correction = correction_from_signature(atlas[key], fixture, tag)
            failures += syndrome_failures(rows, target, correction, total)
            max_weight = max(max_weight, (correction.x | correction.z).bit_count())
        schedule, schedule_tags, schedule_counts = scheduled_basis(fixture)
        schedule_failures = 0
        for target, tag in enumerate(schedule_tags):
            correction = correction_from_signature(atlas[correction_key(fixture, tag)], fixture, tag)
            schedule_failures += sum(
                symplectic(correction, schedule[previous], total) != int(previous == target)
                for previous in range(target + 1)
            )
        held.append({
            "shape": shape,
            "cells": len(fixture.cells),
            "rows": len(rows),
            "atlas_or_syndrome_failures": failures,
            "unseen_local_atlas_keys": len(unseen_keys),
            "schedule_pump_failures": schedule_failures,
            "maximum_correction_weight": max_weight,
            "schedule_counts": schedule_counts,
            "all_row_deletions_rank_loss_failures": sum(
                gf2_rank(
                    row.symplectic(total)
                    for index, row in enumerate(schedule) if index != deleted
                ) != len(schedule) - 1
                for deleted in range(len(schedule))
            ),
        })

    span_shapes = ((2, 2, 2), (3, 2, 2))
    spans = []
    for shape in span_shapes:
        fixture = arbitrary_fixture(Q.shape_cells(shape))
        direct, _tags = direct_graph_basis(fixture)
        repeated = repeated_star_basis(fixture)
        total = fixture.qubits + fixture.matter_qubits
        scheduled, _scheduled_tags, _counts = scheduled_basis(fixture)
        spans.append({
            "shape": shape,
            "rank_formula": 11 * len(fixture.cells) + len(fixture.edges),
            "direct_rank": gf2_rank(row.symplectic(total) for row in direct),
            "repeated_rank": gf2_rank(row.symplectic(total) for row in repeated),
            "schedule_rank": gf2_rank(row.symplectic(total) for row in scheduled),
            "direct_from_repeated_signed_failures": signed_span_failures(direct, repeated, total),
            "repeated_from_direct_signed_failures": signed_span_failures(repeated, direct, total),
            "schedule_from_direct_signed_failures": signed_span_failures(scheduled, direct, total),
            "direct_from_schedule_signed_failures": signed_span_failures(direct, scheduled, total),
            "nonhermitian_rows": sum(
                1 for row in direct + scheduled if (row.phase - (row.x & row.z).bit_count()) & 1
            ),
            "negative_signed_stabilizers": sum(hermitian_sign(row) < 0 for row in scheduled),
        })

    top_source = (
        source_root / "scripts" / "frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py"
    ).read_text()
    tree = ast.parse(top_source)
    function_names = tuple(
        node.name for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    )
    live_input_functions = tuple(
        name for name in function_names
        if any(token in name.lower() for token in ("teleport", "inject", "live_input", "encode_input"))
    )
    return {
        "atlas": atlas_report,
        "advertised_box_shapes_also_in_atlas_training": atlas_overlap,
        "advertised_genuinely_held_shapes": genuinely_held,
        "extra_held_boxes": tuple(held),
        "held_size_interpretation": (
            "the 1..4 training family exhausts the 64 one-cell port masks and "
            "192 oriented endpoint-mask/axis keys; the larger boxes therefore "
            "test reuse at new global sizes, not discovery of new local masks"
        ),
        "span_reconstructions": tuple(spans),
        "pump_kraus_signs": pump_kraus_sign_certificate(),
        "top_level_runner_imported": bool(TOP_LEVEL_BLOCKLIST & set(sys.modules)),
        "live_input_interface_functions": live_input_functions,
        "resource_vs_live_input_boundary": (
            "the code prepares and certifies a mixed Choi stabilizer resource "
            "with retained Bell/syndrome purifiers; it defines no deterministic "
            "teleportation or injection map that consumes an arbitrary live "
            "logical input, so it is not yet the autonomous encoder E"
        ),
    }


def greedy_conflict_layers(supports: Iterable[frozenset]) -> int:
    layers: list[list[frozenset]] = []
    for support in supports:
        for occupied in layers:
            if all(not (support & other) for other in occupied):
                occupied.append(support)
                break
        else:
            layers.append([support])
    return len(layers)


def independent_even_car_live_input_certificate() -> dict[str, object]:
    """Rebuild the fixed-sector even-CAR character cancellation.

    This deliberately uses only the independently reconstructed Choi rows and
    private-dual atlas.  It does not import the submitted live-input runner.
    """
    atlas, atlas_report = build_independent_atlas()
    shapes = ((2, 2, 2), (5, 3, 2), (5, 5, 3), (6, 5, 4))
    rows = []
    for shape in shapes:
        fixture = arbitrary_fixture(Q.shape_cells(shape))
        graph, tags = direct_graph_basis(fixture)
        m = fixture.matter_qubits
        q = fixture.qubits
        total = q + m
        targets = []
        tag_supports = []
        corrections = []
        correction_supports = []
        for tag in tags:
            if tag[0] == "onsite_Z":
                target = Pauli(z=1 << (6 * tag[1] + tag[2]))
                support = frozenset(((tag[1], tag[2]),))
            elif tag[0] == "onsite_XX":
                left = 6 * tag[1] + tag[2]
                target = Pauli(x=(1 << left) | (1 << (left + 1)))
                support = frozenset(((tag[1], tag[2]), (tag[1], tag[2] + 1)))
            else:
                edge = fixture.edges[tag[1]]
                target = fixture.target_terms(tag[1])[2]
                support = frozenset(((edge[0], edge[4] % 6), (edge[1], edge[5] % 6)))
            targets.append(target)
            tag_supports.append(support)
            correction = correction_from_signature(
                atlas[correction_key(fixture, tag)], fixture, tag
            )
            corrections.append(correction)
            touched = set()
            for qubit in range(q):
                if not (((correction.x | correction.z) >> qubit) & 1):
                    continue
                touched.add(qubit // 6 if qubit < m else (qubit - m) // 3)
            correction_supports.append(frozenset(touched))

        doubled = tuple(Pauli(
            (target.x & target.z).bit_count() & 1,
            target.x | (target.x << m),
            target.z | (target.z << m),
        ) for target in targets)
        doubled_commutator_failures = 0
        if shape == shapes[0]:
            doubled_commutator_failures = sum(
                symplectic(left, right, 2 * m)
                for index, left in enumerate(doubled)
                for right in doubled[:index]
            )

        private_dual_failures = sum(
            syndrome_failures(graph, index, correction, total)
            for index, correction in enumerate(corrections)
        )
        target_rank = gf2_rank(target.symplectic(m) for target in targets)

        character_failures = relation_failures = 0
        target_relations = M.kernel_relations(tuple(
            target.symplectic(m) for target in targets
        ))
        if shape == shapes[0]:
            errors = tuple(Pauli(z=1 << mode) for mode in range(m)) + tuple(
                Pauli(x=1 | (1 << mode)) for mode in range(1, m)
            )
            for error in errors:
                syndrome = tuple(
                    symplectic(error, target, m) for target in targets
                )
                correction = pauli_product(
                    row for bit, row in zip(syndrome, corrections) if bit
                )
                replay = tuple(
                    symplectic(correction, stabilizer, total)
                    for stabilizer in graph
                )
                character_failures += replay != syndrome
                relation_failures += sum(
                    sum(
                        syndrome[index]
                        for index in range(len(syndrome))
                        if (relation >> index) & 1
                    ) & 1
                    for relation in target_relations
                )

        measurement_layers = greedy_conflict_layers(tag_supports)
        correction_layers = greedy_conflict_layers(tuple(
            frozenset(
                qubit for qubit in range(q)
                if ((correction.x | correction.z) >> qubit) & 1
            ) for correction in corrections
        ))
        deleted = len(corrections) // 2
        deletion_residual = symplectic(
            corrections[deleted], graph[deleted], total
        )
        rows.append({
            "shape": shape,
            "target_rank": target_rank,
            "expected_target_rank": 2 * m - 1,
            "fixed_sector_Bell_bits": target_rank - 1,
            "expected_fixed_sector_Bell_bits": 2 * (m - 1),
            "literal_doubled_commutator_failures": doubled_commutator_failures,
            "private_dual_failures": private_dual_failures,
            "maximum_correction_support_cells": max(map(len, correction_supports)),
            "measurement_conflict_layers": measurement_layers,
            "correction_conflict_layers": correction_layers,
            "basis_character_failures": character_failures,
            "basis_relation_failures": relation_failures,
            "deleted_private_dual_residual": deletion_residual,
        })
    return {
        "atlas": atlas_report,
        "boxes": tuple(rows),
        "top_level_live_input_runner_imported": (
            "frontier_cycle720_companion_fixed_sector_even_car_bell_2026_07_27"
            in sys.modules
        ),
        "physical_input_Bell_coupling_compiled": False,
        "boundary": (
            "independent fixed-sector CAR-character and physical-correction "
            "certificate; the input Bell measurements remain bounded CAR-"
            "local domain operations rather than a compiled M2 input circuit"
        ),
    }


def all_zero(mapping: dict[str, int]) -> bool:
    return all(value == 0 for value in mapping.values())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    source_root = args.source_root.resolve()
    load_dependencies(source_root)
    identity = sha256()
    for relative in AUDIT_INPUT_PATHS:
        if not relative.startswith("scripts/"):
            continue
        path = source_root / relative
        label = relative.encode()
        body = path.read_bytes()
        identity.update(len(label).to_bytes(8, "big"))
        identity.update(label)
        identity.update(len(body).to_bytes(8, "big"))
        identity.update(body)
    source_identity = identity.hexdigest()

    recurrent = recurrent_certificate()
    genesis = genesis_certificate()
    choi = choi_certificate(source_root)
    even_car = independent_even_car_live_input_certificate()
    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "shared-register overlap and factor ownership are exact without copied view registers",
        recurrent["union_cells"] == 12
        and recurrent["shared_cells"] == 4
        and recurrent["shared_registers"] == 36
        and recurrent["shared_embedding_failures"] == 0
        and recurrent["cover_missing_factors"] == 0
        and recurrent["cover_excess_factors"] == 0,
    )
    check(
        "recurrent G has exact signed coordinates, fixed macro/factor order, active schedule controls, and returned NN routing",
        all_zero(recurrent["coordinate_failures"])
        and recurrent["placement_collisions"] == 0
        and recurrent["word_category_order_failures"] == 0
        and recurrent["seam_factor_pattern_failures"] == 0
        and recurrent["logical_update_factors"] == recurrent["expected_logical_update_factors"]
        and recurrent["runtime_parity_queries"] == 0
        and recurrent["sector_conditioned_gates"] == 0
        and recurrent["route_return_failures"] == 0
        and recurrent["route_non_NN_failures"] == 0
        and recurrent["word_unitarity_residual"] < TOL
        and recurrent["cross_edge_seam_commutators"] == 0
        and recurrent["within_edge_noncommuting_pairs"] > 0
        and recurrent["orientation_reversal_residual"] < TOL
        and recurrent["hostile_interleave_residual"] > 1e-3
        and recurrent["factor_deletion_residual"] > 1e-3,
    )
    check(
        "coframe broadcast and parity twirl close on the declared clean finite-open domain",
        all_zero(genesis["failures"])
        and all(value == 1 for value in genesis["distinct_distribution_digests"].values())
        and genesis["minimum_parity_control_visits"] == 1
        and genesis["maximum_parity_control_visits"] == 1
        and genesis["dirty_targets_hidden"] == 0
        and max(genesis["one_qubit_twirl_dilation"].values()) < TOL,
    )
    check(
        "the independent atlas survives genuinely held larger boxes and every scheduled private correction",
        choi["atlas"].get("solve_contradictions", 0) == 0
        and choi["atlas"].get("training_syndrome_failures", 0) == 0
        and all(
            row["atlas_or_syndrome_failures"] == 0
            and row["schedule_pump_failures"] == 0
            and row["all_row_deletions_rank_loss_failures"] == 0
            for row in choi["extra_held_boxes"]
        ),
    )
    check(
        "11N+E direct, repeated-star, and tree-plaquette signed spans agree independently",
        all(
            row["direct_rank"] == row["rank_formula"]
            and row["repeated_rank"] == row["rank_formula"]
            and row["schedule_rank"] == row["rank_formula"]
            and row["direct_from_repeated_signed_failures"] == 0
            and row["repeated_from_direct_signed_failures"] == 0
            and row["schedule_from_direct_signed_failures"] == 0
            and row["direct_from_schedule_signed_failures"] == 0
            and row["nonhermitian_rows"] == 0
            for row in choi["span_reconstructions"]
        )
        and max(choi["pump_kraus_signs"].values()) < TOL,
    )
    check(
        "fixed-sector even-CAR Bell characters and bounded physical private-dual corrections close independently",
        not even_car["top_level_live_input_runner_imported"]
        and not even_car["physical_input_Bell_coupling_compiled"]
        and even_car["atlas"].get("solve_contradictions", 0) == 0
        and even_car["atlas"].get("training_syndrome_failures", 0) == 0
        and all(
            row["target_rank"] == row["expected_target_rank"]
            and row["fixed_sector_Bell_bits"]
            == row["expected_fixed_sector_Bell_bits"]
            and row["literal_doubled_commutator_failures"] == 0
            and row["private_dual_failures"] == 0
            and row["maximum_correction_support_cells"] <= 1
            and row["measurement_conflict_layers"] <= 4
            and row["correction_conflict_layers"] <= 11
            and row["basis_character_failures"] == 0
            and row["basis_relation_failures"] == 0
            and row["deleted_private_dual_residual"] == 1
            for row in even_car["boxes"]
        ),
    )
    check(
        "the checker did not import the four top-level construction runners and does not promote the Choi resource alone to a live-input encoder",
        not choi["top_level_runner_imported"]
        and not choi["live_input_interface_functions"],
    )

    report = {
        "status": "PASS" if all(row["pass"] for row in checks) else "FAIL",
        "authority": "none",
        "audit": "unset",
        "source_root": str(source_root),
        "declared_source_identity_sha256": source_identity,
        "top_level_blocklist": sorted(TOP_LEVEL_BLOCKLIST),
        "checks": checks,
        "recurrent_overlap_G": recurrent,
        "local_coframe_parity_genesis": genesis,
        "choi_11N_plus_E_pump": choi,
        "fixed_sector_even_car_live_input": even_car,
        "adversarial_disposition": {
            "positive": (
                "The four constructions survive independent GF(2), signed-"
                "Pauli, literal-order, routing, Kraus-sign, and held-size checks "
                "at their stated finite conditional boundaries."
            ),
            "wording_corrections": (
                "Only 5x3x2 among the five advertised Choi boxes is outside "
                "the 1..4 atlas-training family; 4x4x3 is training, not held. "
                "Larger boxes reuse an exhaustively trained local-mask atlas, "
                "so they test global-size reuse rather than new local masks. "
                "Dirty-target checks establish non-hiding, not autonomous "
                "rejection or repair. Raw coframe seed labels permute with the "
                "root chart even though the uniform density is invariant. The "
                "Choi pump alone prepares a resource; the separate even-"
                "CAR character map is a fixed-sector live-input E whose input "
                "Bell operations are not yet compiled to physical M2."
            ),
            "open": (
                "local enforcement/genesis of clean targets, root/router and "
                "epoch removal, collision-free joint controller placement, "
                "physical input-Bell compilation and joint epoch integration "
                "remain open"
            ),
            "no_shared_obstruction_or_axiom_pressure_claim": True,
        },
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    payload = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(payload + "\n")
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    print("COMPANION_THREE_ROUTE_INDEPENDENT_ADVERSARY_PASS" if report["status"] == "PASS" else "COMPANION_THREE_ROUTE_INDEPENDENT_ADVERSARY_FAIL")
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
