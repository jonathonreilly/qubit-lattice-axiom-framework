#!/usr/bin/env python3
"""Cycle-720 gauge-native local-D BKSF FSWAP Clifford factorization.

This support probe asks whether the four-term local-D FSWAP already landed as
operator-algebra evidence can be executed as a bounded physical Clifford word,
without comparing it to an exterior-order endpoint FSWAP.  It then tests a
fixed checkerboard seam schedule on held three-dimensional boxes.

The result is deliberately narrower than a full recurrent M64 compiler.  Coin
and contact are checked only as inherited bounded local-D factors; their
literal physical words are not composed here.  Code/coframe/program genesis
and parallel nearest-neighbour routing also remain supplied/open.
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
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py",
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

from collections import Counter
from hashlib import sha256
import json
import math
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25 as C703
import frontier_cycle709_local_seam_clifford_core_2026_07_26 as C709
import frontier_cycle709_local_seam_physical_core_2026_07_26 as P709


F = C709.F
G = C709.G
Pauli = F.base.Pauli
Coord = tuple[int, int, int]
TOL = 3.0e-10
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail=None) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def pauli_product(rows) -> Pauli:
    result = Pauli()
    for row in rows:
        result = result @ row
    return result


def path_A(graph, vertices: tuple[int, ...]) -> Pauli:
    result = Pauli(phase=(len(vertices) - 2) % 4)
    for left, right in zip(vertices, vertices[1:]):
        result = result @ graph.A(left, right)
    return result


def target_cell(cell: Coord, axis: int) -> Coord:
    return tuple(value + int(index == axis) for index, value in enumerate(cell))


def path_fswap_terms(equivalence, cell: Coord, axis: int) -> tuple[Pauli, ...]:
    """Diagnostic target-graph path substitution; not the retained common E."""
    graph = equivalence.patch_graph
    target = target_cell(cell, axis)
    source_mode = 2 * axis + 1
    target_mode = 2 * axis
    u = graph.vertex_index[(cell, source_mode)]
    v = graph.vertex_index[(target, target_mode)]
    ru = graph.vertex_index[(cell, 6)]
    rv = graph.vertex_index[(target, 6)]
    reference_path = path_A(graph, (ru, u, v, rv))
    core = graph.A(u, v) @ reference_path
    spectator = pauli_product(
        graph.B(graph.vertex_index[(target, mode)])
        for mode in range(6)
        if mode != target_mode
    )
    return (
        graph.B(u),
        graph.B(v),
        Pauli(phase=2) @ spectator @ core,
        spectator @ graph.B(u) @ graph.B(v) @ core,
    )


def source_fswap_terms(equivalence, cell: Coord, axis: int) -> tuple[Pauli, ...]:
    """Direct-reference local-D quartet on the gauge-native source graph."""
    graph = equivalence.open_graph
    target = target_cell(cell, axis)
    source_mode = 2 * axis + 1
    target_mode = 2 * axis
    u = graph.vertex_index[(cell, source_mode)]
    v = graph.vertex_index[(target, target_mode)]
    ru = graph.vertex_index[(cell, 6)]
    rv = graph.vertex_index[(target, 6)]
    core = graph.A(u, v) @ graph.A(ru, rv)
    spectator = pauli_product(
        graph.B(graph.vertex_index[(target, mode)])
        for mode in range(6)
        if mode != target_mode
    )
    return (
        graph.B(u),
        graph.B(v),
        Pauli(phase=2) @ spectator @ core,
        spectator @ graph.B(u) @ graph.B(v) @ core,
    )


def target_fswap_terms(equivalence, cell: Coord, axis: int) -> tuple[Pauli, ...]:
    """Signed graph-equivalence image on PatchGraph plus persistent seam rails."""
    return tuple(equivalence.forward(row) for row in source_fswap_terms(equivalence, cell, axis))


def expected_logical_terms(equivalence, cell: Coord, axis: int) -> tuple[Pauli, ...]:
    """Independent Jordan-Wigner terms for the same fermionic transposition."""
    # Cycle708's held-box tableau deliberately uses the supplied Hamiltonian
    # cell path as its logical order even though OpenReferenceGraph stores a
    # sorted geometric cell tuple.
    cells = equivalence.cells
    left = 6 * cells.index(cell) + 2 * axis + 1
    right = 6 * cells.index(target_cell(cell, axis)) + 2 * axis
    left, right = sorted((left, right))
    endpoints = (1 << left) | (1 << right)
    between = ((1 << right) - 1) ^ ((1 << (left + 1)) - 1)
    return (
        Pauli(z=1 << left),
        Pauli(z=1 << right),
        Pauli(phase=2, x=endpoints, z=between | endpoints),
        Pauli(x=endpoints, z=between),
    )


def decode_term(row: Pauli, equivalence) -> tuple[Pauli, int, int]:
    coordinates = F.decode(
        row, equivalence.target_w, equivalence.target_v, equivalence.qubits
    )
    logical_count = len(equivalence.source_logical_z)
    logical_mask = (1 << logical_count) - 1
    logical = Pauli(
        phase=coordinates.phase,
        x=coordinates.v_mask & logical_mask,
        z=coordinates.w_mask & logical_mask,
    )
    leakage = coordinates.v_mask >> logical_count
    stabilizer = coordinates.w_mask >> logical_count
    return logical, leakage, stabilizer


def decode_source_term(row: Pauli, equivalence) -> tuple[Pauli, int, int]:
    coordinates = F.decode(
        row, equivalence.source_w, equivalence.source_v, equivalence.qubits
    )
    logical_count = len(equivalence.source_logical_z)
    logical_mask = (1 << logical_count) - 1
    return (
        Pauli(
            phase=coordinates.phase,
            x=coordinates.v_mask & logical_mask,
            z=coordinates.w_mask & logical_mask,
        ),
        coordinates.v_mask >> logical_count,
        coordinates.w_mask >> logical_count,
    )


def encoded_extended_bits(matter: tuple[int, ...]) -> tuple[int, ...]:
    output = []
    for offset in range(0, len(matter), 6):
        cell = matter[offset : offset + 6]
        output.extend(cell)
        output.append(sum(cell) & 1)
    return tuple(output)


def strip_references(extended: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        extended[7 * cell + mode]
        for cell in range(len(extended) // 7)
        for mode in range(6)
    )


def apply_gamma(bits: tuple[int, ...], mode: int):
    output = list(bits)
    phase = -1.0 if sum(bits[:mode]) & 1 else 1.0
    output[mode] ^= 1
    return tuple(output), phase


def apply_A(bits: tuple[int, ...], source: int, target: int):
    if source > target:
        output, phase = apply_A(bits, target, source)
        return output, -phase
    output, right = apply_gamma(bits, target)
    output, left = apply_gamma(output, source)
    return output, -1j * left * right


def coarse_fswap_action(matter: tuple[int, ...], left: int, right: int):
    permutation = list(range(len(matter)))
    permutation[left], permutation[right] = right, left
    occupied = [index for index, value in enumerate(matter) if value]
    targets = [permutation[index] for index in occupied]
    inversions = sum(
        targets[a] > targets[b]
        for a in range(len(targets))
        for b in range(a + 1, len(targets))
    )
    output = [0] * len(matter)
    for target in targets:
        output[target] = 1
    return tuple(output), -1.0 if inversions & 1 else 1.0


def extended_fswap_action(
    extended: tuple[int, ...], left_cell: int, left_mode: int,
    right_cell: int, right_mode: int,
):
    left = 7 * left_cell + left_mode
    right = 7 * right_cell + right_mode
    if extended[left] == extended[right]:
        return extended, -1.0 if extended[left] else 1.0
    left_reference = 7 * left_cell + 6
    right_reference = 7 * right_cell + 6
    output, reference_phase = apply_A(extended, left_reference, right_reference)
    output, matter_phase = apply_A(output, left, right)
    spectator = sum(
        extended[7 * right_cell + mode]
        for mode in range(6)
        if mode != right_mode
    ) & 1
    phase = reference_phase * matter_phase * (-1.0 if spectator == 0 else 1.0)
    return output, phase


def extended_intertwiner(equivalence) -> dict[str, object]:
    modes = 6 * len(equivalence.cells)
    labels = ((),) + tuple((mode,) for mode in range(modes)) + tuple(
        (left, right) for left in range(modes) for right in range(left + 1, modes)
    )
    failures = reference_failures = deleted_reference_failures = 0
    seam_cases = 0
    cell_index = {cell: index for index, cell in enumerate(equivalence.cells)}
    for cell, axis, _matter, _reference in equivalence.open_graph.cross_edges:
        target = target_cell(cell, axis)
        left_cell = cell_index[cell]
        right_cell = cell_index[target]
        left_mode, right_mode = 2 * axis + 1, 2 * axis
        logical_left = 6 * left_cell + left_mode
        logical_right = 6 * right_cell + right_mode
        for label in labels:
            matter = tuple(int(index in label) for index in range(modes))
            extended = encoded_extended_bits(matter)
            expected_matter, expected_phase = coarse_fswap_action(
                matter, logical_left, logical_right
            )
            observed, observed_phase = extended_fswap_action(
                extended, left_cell, left_mode, right_cell, right_mode
            )
            failures += (
                strip_references(observed) != expected_matter
                or abs(observed_phase - expected_phase) > TOL
            )
            reference_failures += observed != encoded_extended_bits(expected_matter)
            seam_cases += 1

        witness = [0] * modes
        witness[logical_left] = 1
        extended = encoded_extended_bits(tuple(witness))
        bare, _phase = apply_A(
            extended,
            7 * left_cell + left_mode,
            7 * right_cell + right_mode,
        )
        deleted_reference_failures += sum(
            sum(bare[7 * index : 7 * index + 7]) & 1
            for index in (left_cell, right_cell)
        )
    return {
        "columns": len(labels),
        "seams": len(equivalence.open_graph.cross_edges),
        "seam_column_cases": seam_cases,
        "EG_failures": failures,
        "local_reference_constraint_failures": reference_failures,
        "deleted_reference_endpoint_D_violations": deleted_reference_failures,
        "scope": "vacuum plus all one/two-particle columns",
    }


def pauli_support(row: Pauli) -> frozenset[int]:
    mask = row.x | row.z
    return frozenset(index for index in range(mask.bit_length()) if (mask >> index) & 1)


def seam_support(terms: tuple[Pauli, ...]) -> frozenset[int]:
    return frozenset().union(*(pauli_support(row) for row in terms))


def schedule_colour(key: tuple[Coord, int], origin: Coord = (0, 0, 0)):
    """Six fixed classes: transported axis and body-checkerboard parity."""
    cell, axis = key
    parity = sum(value - origin[index] for index, value in enumerate(cell)) & 1
    return axis, parity


def seam_rows(equivalence):
    return tuple(
        ((cell, axis), target_fswap_terms(equivalence, cell, axis))
        for cell, axis, _matter, _reference in equivalence.patch_graph.cross_edges
    )


def transvection_word_action(rows, axes: tuple[Pauli, ...], deleted: int | None = None):
    output = tuple(rows)
    for index, axis in enumerate(axes):
        if index == deleted:
            continue
        output = tuple(
            Pauli(phase=3) @ axis @ row if C709.anticommutes(row, axis) else row
            for row in output
        )
    return output


def quadratic_rephase_system(equivalence) -> dict[str, int]:
    """Try one symmetric matter-only CZ rephase; this is only one route."""
    modes = len(equivalence.source_logical_z)

    def variable(left: int, right: int) -> int | None:
        if left == right:
            return None
        if left > right:
            left, right = right, left
        return left * modes - left * (left + 1) // 2 + right - left - 1

    pivots: dict[int, tuple[int, int]] = {}
    contradictions = equations = 0
    for cell, axis, _matter, _reference in equivalence.open_graph.cross_edges:
        current = [decode_source_term(row, equivalence)[0]
                   for row in source_fswap_terms(equivalence, cell, axis)]
        expected = expected_logical_terms(equivalence, cell, axis)
        endpoints = [index for index in range(modes) if (current[2].x >> index) & 1]
        if len(endpoints) != 2 or current[2].z ^ expected[2].z != current[3].z ^ expected[3].z:
            raise AssertionError("unexpected direct-seam coordinate pattern")
        difference = current[2].z ^ expected[2].z
        for row in range(modes):
            mask = 0
            for column in endpoints:
                item = variable(row, column)
                if item is not None:
                    mask ^= 1 << item
            rhs = (difference >> row) & 1
            equations += 1
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
    return {
        "matter_modes": modes,
        "symmetric_CZ_variables": modes * (modes - 1) // 2,
        "equations": equations,
        "coefficient_rank": len(pivots),
        "augmented_contradictions": contradictions,
    }


def fixture(shape: tuple[int, int, int]) -> dict[str, object]:
    cells = G.box_cells(shape)
    equivalence = G.build_equivalence(cells).equivalence
    rows = seam_rows(equivalence)
    coordinate_mismatches = leakage_failures = 0
    source_target_coordinate_failures = 0
    source_stabilizer_commutator_failures = 0
    target_stabilizer_commutator_failures = 0
    path_substitution_coordinate_mismatches = 0
    nonhermitian = 0
    supports = []
    weights = []
    deletion_action_failures = []
    for key, terms in rows:
        expected = expected_logical_terms(equivalence, *key)
        source_terms = source_fswap_terms(equivalence, *key)
        source_decoded = [decode_source_term(term, equivalence) for term in source_terms]
        path_terms = path_fswap_terms(equivalence, *key)
        for index, (term, target) in enumerate(zip(terms, expected)):
            logical, leakage, stabilizer = decode_term(term, equivalence)
            coordinate_mismatches += logical != target
            leakage_failures += bool(leakage)
            source_target_coordinate_failures += logical != source_decoded[index][0]
            source_target_coordinate_failures += leakage != source_decoded[index][1]
            nonhermitian += term.phase % 2 != (term.x & term.z).bit_count() % 2
            target_stabilizer_commutator_failures += sum(
                C709.anticommutes(term, row)
                for row in equivalence.target_w[len(equivalence.source_logical_z) :]
            )
            source_stabilizer_commutator_failures += sum(
                C709.anticommutes(source_terms[index], row)
                for row in equivalence.source_w[len(equivalence.source_logical_z) :]
            )
            path_logical, path_leakage, _path_stabilizer = decode_term(
                path_terms[index], equivalence
            )
            path_substitution_coordinate_mismatches += (
                path_logical != target or bool(path_leakage)
            )
            weights.append(len(pauli_support(term)))
        supports.append(seam_support(terms))

        logical_count = len(equivalence.source_logical_z)
        generators = C709.identity_images(logical_count)
        full_images = transvection_word_action(generators, expected)
        for deleted in range(4):
            images = transvection_word_action(generators, expected, deleted)
            deletion_action_failures.append(sum(a != b for a, b in zip(images, full_images)))

    same_colour_collisions = 0
    different_colour_overlaps = 0
    for right in range(len(rows)):
        for left in range(right):
            if not (supports[left] & supports[right]):
                continue
            if schedule_colour(rows[left][0]) == schedule_colour(rows[right][0]):
                same_colour_collisions += 1
            else:
                different_colour_overlaps += 1
    colour_counts = Counter(schedule_colour(key) for key, _terms in rows)
    return {
        "shape": shape,
        "cells": len(cells),
        "abstract_patch_plus_rail_qubits": equivalence.qubits,
        "seams": len(rows),
        "ordinary_JW_coordinate_mismatches": coordinate_mismatches,
        "source_target_signed_tableau_coordinate_failures": source_target_coordinate_failures,
        "logical_leakage_failures": leakage_failures,
        "source_stabilizer_commutator_failures": source_stabilizer_commutator_failures,
        "target_stabilizer_commutator_failures": target_stabilizer_commutator_failures,
        "path_substitution_ordinary_coordinate_mismatches": path_substitution_coordinate_mismatches,
        "nonhermitian_terms": nonhermitian,
        "maximum_term_weight": max(weights, default=0),
        "maximum_four_factor_union": max(map(len, supports), default=0),
        "schedule_colours_present": len(colour_counts),
        "maximum_seams_per_colour": max(colour_counts.values(), default=0),
        "same_colour_support_collisions": same_colour_collisions,
        "different_colour_support_overlaps": different_colour_overlaps,
        "minimum_single_rotation_deletion_logical_mismatches": min(
            deletion_action_failures, default=0
        ),
        "extended_Fock_intertwiner": extended_intertwiner(equivalence),
        "static_quadratic_rephase": quadratic_rephase_system(equivalence),
    }


def canonical_factorization() -> dict[str, object]:
    I = np.eye(2, dtype=complex)
    X = np.asarray(((0, 1), (1, 0)), dtype=complex)
    Y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    Z = np.diag((1, -1)).astype(complex)
    terms = (np.kron(Z, I), np.kron(I, Z), np.kron(Y, Y), np.kron(X, X))
    fswap = sum(terms) / 2
    product = np.eye(4, dtype=complex)
    for term in terms:
        product = (np.cos(math.pi / 4) * np.eye(4) - 1j * np.sin(math.pi / 4) * term) @ product
    phase = np.vdot(fswap, product) / 4
    aligned = phase / abs(phase)
    return {
        "unitarity_residual": float(np.linalg.norm(fswap.conj().T @ fswap - np.eye(4))),
        "involution_residual": float(np.linalg.norm(fswap @ fswap - np.eye(4))),
        "four_rotation_residual_up_to_phase": float(np.linalg.norm(product - aligned * fswap)),
        "global_phase": [float(aligned.real), float(aligned.imag)],
        "double_occupation_phase": [float(fswap[3, 3].real), float(fswap[3, 3].imag)],
        "ordinary_SWAP_residual": float(np.linalg.norm(
            fswap - np.asarray(((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)), complex)
        )),
    }


def physical_axis(axis: int) -> dict[str, object]:
    source = (0, 0, 0)
    target = tuple(int(index == axis) for index in range(3))
    cells = (source, target)
    equivalence = G.build_equivalence(cells).equivalence
    graph = P709.c707.PatchGraph(cells)
    site_map, gauges = P709.c707.placement(graph, include_edge_gauge=True)
    all_sites = tuple(sorted(P709.c707.occupied_sites(site_map, gauges)))
    abstract = target_fswap_terms(equivalence, source, axis)
    physical = tuple(
        P709.physical_lift(row, equivalence, graph, site_map, gauges)[0]
        for row in abstract
    )
    local, support, word = P709.compile_factor_rows(physical, (1, 1, 1, 1), all_sites)

    rng = np.random.default_rng(2700 + axis)
    state = rng.normal(size=1 << len(support)) + 1j * rng.normal(size=1 << len(support))
    state /= np.linalg.norm(state)
    direct = state
    for row in local:
        direct = P709.c707.direct_rotation(direct, row, math.pi / 2, len(support))
    compiled = P709.execute_word(state, word, support)
    compiled_residual = P709.phase_aligned_residual(compiled, direct)

    factor_deletion_residuals = []
    offsets = [0]
    for row in local:
        offsets.append(offsets[-1] + len(P709.compile_clifford_rotation(row, support, 1)))
    for deleted in range(4):
        damaged = word[: offsets[deleted]] + word[offsets[deleted + 1] :]
        factor_deletion_residuals.append(
            P709.phase_aligned_residual(P709.execute_word(state, damaged, support), direct)
        )
    routed, route_report = P709.c707.route_word(word)
    return {
        "axis": axis,
        "abstract_term_weights": tuple(len(pauli_support(row)) for row in abstract),
        "physical_term_weights": tuple(len(pauli_support(row)) for row in physical),
        "physical_factor_union_M2": len(support),
        "literal_placement_M2": len(all_sites),
        "placement_collisions": (
            sum(len(sites) for sites in site_map.values()) + len(gauges) - len(all_sites)
        ),
        "repetition_stabilizer_failures": sum(
            P709.repetition_failures(row, graph, site_map, all_sites) for row in physical
        ),
        "primitive_gates": len(word),
        "primitive_census": dict(Counter(item.kind for item in word)),
        "compiled_vs_direct_rotation_residual": compiled_residual,
        "minimum_factor_deletion_residual": min(factor_deletion_residuals),
        "routed_gates": len(routed),
        "maximum_route_distance": route_report["maximum_route_distance"],
        "non_NN_failures": route_report["non_NN_failures"],
        "operand_order_failures": route_report["operand_order_failures"],
        "route_return_failures": route_report["route_return_failures"],
        "delete_first_swap_detected_macros": route_report["delete_first_swap_detected_macros"],
        "routed_word_sha256": route_report["word_sha256"],
    }


def physical_two_star_box() -> dict[str, object]:
    shape = (2, 2, 2)
    cells = G.box_cells(shape)
    equivalence = G.build_equivalence(cells).equivalence
    graph = P709.c707.PatchGraph(cells)
    site_map, gauges = P709.c707.placement(graph, include_edge_gauge=True)
    all_sites = tuple(sorted(P709.c707.occupied_sites(site_map, gauges)))
    rows = sorted(seam_rows(equivalence), key=lambda row: schedule_colour(row[0]))
    word = []
    physical_supports = []
    repetition_failures = 0
    factor_weights = []
    rail_active_seams = 0
    patch = len(equivalence.patch_graph.edges)
    for key, terms in rows:
        rail_active_seams += any(((term.x | term.z) >> patch) != 0 for term in terms)
        physical = tuple(
            P709.physical_lift(term, equivalence, graph, site_map, gauges)[0]
            for term in terms
        )
        repetition_failures += sum(
            P709.repetition_failures(term, graph, site_map, all_sites)
            for term in physical
        )
        _local, support, factor_word = P709.compile_factor_rows(
            physical, (1, 1, 1, 1), all_sites
        )
        physical_supports.append((key, frozenset(support)))
        factor_weights.extend(len(pauli_support(term)) for term in physical)
        word.extend(factor_word)

    same_colour_collisions = sum(
        schedule_colour(left_key) == schedule_colour(right_key)
        and bool(left_support & right_support)
        for index, (right_key, right_support) in enumerate(physical_supports)
        for left_key, left_support in physical_supports[:index]
    )
    routed, route_report = P709.c707.route_word(tuple(word))
    return {
        "shape": shape,
        "cells": len(cells),
        "seams": len(rows),
        "literal_assigned_M2": len(all_sites),
        "placement_collisions": (
            sum(len(sites) for sites in site_map.values()) + len(gauges) - len(all_sites)
        ),
        "persistent_rail_active_seams": rail_active_seams,
        "maximum_physical_term_weight": max(factor_weights),
        "maximum_physical_seam_union": max(len(support) for _key, support in physical_supports),
        "same_colour_physical_support_collisions": same_colour_collisions,
        "repetition_stabilizer_failures": repetition_failures,
        "primitive_gates": len(word),
        "primitive_census": dict(Counter(item.kind for item in word)),
        "routed_gates": len(routed),
        "maximum_route_distance": route_report["maximum_route_distance"],
        "non_NN_failures": route_report["non_NN_failures"],
        "operand_order_failures": route_report["operand_order_failures"],
        "route_return_failures": route_report["route_return_failures"],
        "delete_first_swap_detected_macros": route_report["delete_first_swap_detected_macros"],
        "routed_word_sha256": route_report["word_sha256"],
    }


def matvec(frame, cell: Coord) -> Coord:
    return tuple(int(value) for value in frame @ np.asarray(cell, dtype=int))


def transform_key(key: tuple[Coord, int], frame) -> tuple[Coord, int]:
    cell, axis = key
    left = matvec(frame, cell)
    right = matvec(frame, target_cell(cell, axis))
    delta = tuple(r - l for l, r in zip(left, right))
    target_axis = next(index for index, value in enumerate(delta) if value)
    lower = tuple(min(l, r) for l, r in zip(left, right))
    return lower, target_axis


def colour_covariance() -> dict[str, object]:
    frames = C703.prior.proper_cubic_frames()
    keys = tuple(((x, y, z), axis) for x in range(2) for y in range(2) for z in range(2) for axis in range(3))
    frame_failures = 0
    for frame in frames:
        for key in keys:
            source_colour = schedule_colour(key)
            transformed = transform_key(key, frame)
            target_colour = schedule_colour(transformed)
            direction = tuple(int(value) for value in frame @ np.eye(3, dtype=int)[:, key[1]])
            target_axis = next(index for index, value in enumerate(direction) if value)
            predicted = (target_axis, source_colour[1] ^ int(direction[target_axis] < 0))
            frame_failures += target_colour != predicted
    product_failures = 0
    for right in frames:
        for left in frames:
            combined = left @ right
            for key in keys:
                product_failures += transform_key(transform_key(key, right), left) != transform_key(key, combined)
    return {
        "proper_cubic_frames": len(frames),
        "frame_colour_cases": len(frames) * len(keys),
        "frame_colour_failures": frame_failures,
        "ordered_frame_products": len(frames) ** 2,
        "product_key_cases": len(frames) ** 2 * len(keys),
        "product_key_failures": product_failures,
    }


def inherited_covariance() -> tuple[dict[str, object], ...]:
    rows = []
    for spec in C703.PATCHES[:2]:
        rows.append(C703.covariance_certificate(spec))
    return tuple(rows)


def local_free_contact_mass() -> dict[str, object]:
    factors = []
    for spec in C703.PATCHES[:2]:
        graph = C703.ExtendedGraph.patch(spec.centers)
        factors.append(C703.mapped_factor_certificate(spec, graph))
    return {
        "factor_rows": tuple(factors),
        "mass_contact": C703.mass_and_contact_certificate(),
    }


def report_digest(report: dict[str, object]) -> str:
    payload = json.dumps(report, sort_keys=True, separators=(",", ":"))
    return sha256(payload.encode()).hexdigest()


def main() -> None:
    factorization = canonical_factorization()
    fixtures = tuple(
        fixture(shape)
        for shape in ((2, 2, 2), (3, 2, 2), (4, 2, 2), (3, 3, 2), (3, 3, 3))
    )
    axes = tuple(physical_axis(axis) for axis in range(3))
    two_star = physical_two_star_box()
    colours = colour_covariance()
    covariance = inherited_covariance()
    local_factors = local_free_contact_mass()
    translations = C709.translation_certificate()

    check(
        "four pi/4 rotations are the exact canonical FSWAP up to global phase",
        factorization["four_rotation_residual_up_to_phase"] < TOL
        and factorization["unitarity_residual"] < TOL
        and factorization["involution_residual"] < TOL
        and factorization["double_occupation_phase"] == [-1.0, 0.0]
        and factorization["ordinary_SWAP_residual"] > 1.9,
        factorization,
    )
    check(
        "the signed graph map preserves the direct-seam code while the naive local-reference E is actively falsified",
        all(
            row["extended_Fock_intertwiner"]["EG_failures"] > 0
            and row["extended_Fock_intertwiner"]["local_reference_constraint_failures"] == 0
            and row["extended_Fock_intertwiner"]["deleted_reference_endpoint_D_violations"] > 0
            and row["static_quadratic_rephase"]["augmented_contradictions"] > 0
            and row["source_target_signed_tableau_coordinate_failures"] == 0
            and row["logical_leakage_failures"] == 0
            and row["source_stabilizer_commutator_failures"] == 0
            and row["target_stabilizer_commutator_failures"] == 0
            and row["nonhermitian_terms"] == 0
            and row["minimum_single_rotation_deletion_logical_mismatches"] > 0
            for row in fixtures
        ),
        fixtures,
    )
    check(
        "the body-checkerboard six-colour law makes every same-layer BKSF support disjoint",
        all(row["schedule_colours_present"] <= 6 and row["same_colour_support_collisions"] == 0 for row in fixtures),
        fixtures,
    )
    check(
        "all three axis quartets compile to literal repetition-compatible routed M2 words",
        all(
            row["physical_factor_union_M2"] == 18
            and tuple(row["physical_term_weights"]) == (6, 6, 13, 13)
            and row["placement_collisions"] == 0
            and row["repetition_stabilizer_failures"] == 0
            and row["compiled_vs_direct_rotation_residual"] < TOL
            and row["minimum_factor_deletion_residual"] > 0.1
            and row["non_NN_failures"] == 0
            and row["operand_order_failures"] == 0
            and row["route_return_failures"] == 0
            and row["delete_first_swap_detected_macros"] > 0
            for row in axes
        ),
        axes,
    )
    check(
        "the complete 2x2x2 two-star seam macro is a literal routed persistent-rail M2 word",
        two_star["cells"] == 8
        and two_star["seams"] == 12
        and two_star["persistent_rail_active_seams"] == 12
        and two_star["placement_collisions"] == 0
        and two_star["same_colour_physical_support_collisions"] == 0
        and two_star["repetition_stabilizer_failures"] == 0
        and two_star["non_NN_failures"] == 0
        and two_star["operand_order_failures"] == 0
        and two_star["route_return_failures"] == 0
        and two_star["delete_first_swap_detected_macros"] > 0,
        two_star,
    )
    check(
        "coin/contact logarithms and the Cycle219 mass fixture remain exact on the same local-D family",
        all(
            row["maximum_unitary_expansion_residual"] < TOL
            and row["maximum_log_expansion_residual"] < TOL
            and row["maximum_Hermitian_log_residual"] < TOL
            and row["maximum_imaginary_log_coefficient"] < TOL
            and row["non_Hermitian_physical_terms"] == 0
            and row["projector_commutator_failures"] == 0
            and row["returned_work_failures"] == 0
            for row in local_factors["factor_rows"]
        )
        and local_factors["mass_contact"]["one_particle_coin_eigen_residual"] < TOL
        and local_factors["mass_contact"]["one_particle_mass_residual"] < TOL
        and local_factors["mass_contact"]["contact_vacuum_and_one_particle_residual"] < TOL
        and local_factors["mass_contact"]["contact_double_occupation_phase_residual"] < TOL,
        local_factors,
    )
    check(
        "the six colours and transported direct local-D seam close 24 frames and 576 products",
        colours["frame_colour_failures"] == 0
        and colours["product_key_failures"] == 0
        and all(
            row["frames"] == 24
            and row["ordered_products"] == 576
            and row["corrected_dressed_stream_failures"] == 0
            and row["address_group_law_failures"] == 0
            and row["operator_group_law_failures"] == 0
            for row in covariance
        )
        and translations["parity_residue_translations"] == 8
        and translations["translated_semantic_failures"] == 0,
        {"colours": colours, "operators": covariance, "translations": translations},
    )

    report = {
        "status": "cycle720-gauge-native-direct-seam-positive-common-E-open",
        "pass": FAIL == 0,
        "authority": "none",
        "audit": "unset",
        "baseline": "origin/main@f7d78df6455d41cf50c143e41c81f204d3dec72e",
        "factorization": factorization,
        "fixtures": fixtures,
        "literal_axes": axes,
        "literal_two_star_seam_macro": two_star,
        "local_free_contact_mass": local_factors,
        "schedule_covariance": colours,
        "inherited_operator_covariance_reexecuted": covariance,
        "translations": translations,
        "derived": (
            "the exact local-D BKSF FSWAP is four bounded pi/4 Pauli rotations",
            "the signed OpenReference-to-PatchGraph-plus-rail tableau transports the direct-seam code without leakage",
            "a fixed axis plus body-checkerboard parity law gives six collision-free abstract support layers",
            "each persistent-rail two-cell axis word compiles on 18 physical M2 and routes with returned spectators",
            "the complete 2x2x2 seam macro uses all 12 persistent rails in six collision-free phases",
            "the naive amplitude-one local-reference E fails ordinary multi-cell CAR columns on every held box",
            "a symmetric matter-only quadratic CZ rephase is inconsistent on every held box",
        ),
        "supplied": (
            "one persistent direct-reference/seam-gauge sector, transported to the Cycle706 prepared rail sector",
            "the Cycle707 literal repetition placement and blank serial route workspace",
            "one transported proper-cubic coframe, checkerboard origin, and six program phases",
            "the Cycle219 coin and Cycle230 contact values and fixed factor order",
        ),
        "open": (
            "a coherent gauge-native state isometry E or fixed sector whose multi-cell columns intertwine the ordinary coarse-CAR convention",
            "literal single-M2-rotation compilation and one combined routed word for the non-Clifford coin/contact factors",
            "parallel nearest-neighbour routing rather than the supplied serial route-and-return microprogram",
            "autonomous genesis/enforcement of local-D, loop, rail, repetition, coframe, origin, and program registers",
            "periodic Wilson direct-sum and arbitrary irregular-domain recurrence",
            "composition with endpoint packet allocation, source/gravity, Record/Born, and prediction interfaces",
        ),
        "claim_ceiling": (
            "Positive gauge-native direct-seam algebra compiler, two-star routed seam macro, and collision-free scheduler.  "
            "The actual multi-cell common state encoding E remains open: the naive amplitude-one reference encoding and "
            "one symmetric quadratic rephase are falsified, while coherent gauge-sector and quotient encodings remain live.  "
            "Coin/contact are exact bounded local-D logarithm factors but are not yet in the same literal routed macro.  "
            "This is not a time law, a Record, a broad no-go, a minimum theorem, or axiom pressure."
        ),
        "no_go_discipline": {
            "gate": "FAIL_for_broad_no_go__positive_construction_only",
            "N1_alternative_routes": {
                "naive_amplitude_one_local_reference_E": tuple(
                    {
                        "shape": row["shape"],
                        "tested_columns": row["extended_Fock_intertwiner"]["seam_column_cases"],
                        "EG_failures": row["extended_Fock_intertwiner"]["EG_failures"],
                    }
                    for row in fixtures
                ),
                "symmetric_matter_only_quadratic_rephase": tuple(
                    {
                        "shape": row["shape"],
                        "rank": row["static_quadratic_rephase"]["coefficient_rank"],
                        "contradictions": row["static_quadratic_rephase"]["augmented_contradictions"],
                    }
                    for row in fixtures
                ),
                "direct_BKSF_algebra_plus_signed_graph_transport": "positive_operator_compiler__state_E_open",
                "ordinary_E_Gauss_boundary_flux": "exact_but_non_covariant_and_boundary_support_grows_in_prior_scratch",
                "coherent_gauge_sector_superposition": "untested",
                "symmetric_quotient_or_non_diagonal_E": "untested",
            },
            "N2_wall_independence": (
                "operator-algebra compilation is separated from state-isometry construction",
                "state-isometry construction is separated from gauge-sector genesis",
                "coin/contact physical routing is separated from the Clifford seam macro",
                "parallel recurrence is separated from the serial route-and-return controller",
            ),
            "N3_hidden_wall_scan": (
                "persistent direct-reference and rail sector supplied",
                "clean repetition and route workspace supplied",
                "proper-cubic coframe, checkerboard origin, and six program phases supplied",
                "coin/contact values and factor order supplied",
            ),
            "N4_residual_matching": (
                "operator claims require zero binary tableau mismatch and leakage",
                "physical Clifford claims require numerical residual below tolerance and active deletion witnesses",
                "state-E claims use explicit coarse-column phases and are reported as failures rather than inferred from equal algebra",
            ),
            "N5_domain": (
                "explicit state-E stress is vacuum plus all one/two-particle columns on five boxes from 2x2x2 through 3x3x3",
                "operator, schedule, frame, product, and translation claims use their separately reported finite domains",
                "no extrapolation to arbitrary size or particle number",
            ),
            "N6_partial_closure": (
                "four-rotation direct-seam factorization",
                "signed graph code transport",
                "literal routed 2x2x2 seam macro",
                "six-phase proper-cubic scheduler",
                "exact local-D coin/contact/mass factor evidence",
            ),
            "N7_steelman": (
                "a coherent uniform gauge-sector superposition may absorb the missing multi-cell CAR phase",
                "a quotient or non-diagonal local encoding may avoid the static quadratic-rephase contradiction",
            ),
            "N8_cross_cycle_echo": (
                "Cycle703 direct local-D factor and covariance certificates reexecuted",
                "Cycle705/706 signed graph equivalence used rather than inferred path substitution",
                "Cycle707/709 literal M2 placement, routing, and translation certificates reexecuted",
                "the prior edge-Gauss support route narrows but does not eliminate coherent-sector routes",
            ),
            "live_routes": (
                "complete gauge-native direct-factor composition",
                "parallel local router/controller",
                "plaquette/symmetric quotient E",
                "non-diagonal coherent gauge-sector E",
            ),
        },
    }
    report["report_sha256"] = report_digest(report)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    if FAIL:
        raise SystemExit(1)
    print("GAUGE_NATIVE_DIRECT_SEAM_PHYSICAL_PARTIAL_COMMON_E_OPEN")


if __name__ == "__main__":
    main()
