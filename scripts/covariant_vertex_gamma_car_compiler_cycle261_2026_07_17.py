#!/usr/bin/env python3
"""Cycle 261: proper-cubic covariant vertex-gamma CAR compiler.

Put six local Clifford Majoranas on three qubits at every degree-five vertex
of the square-pyramid dual graph.  Five labels serve the physical incident
edges and the missing label serves occupation parity.  Audit the exact local
CAR algebra, elementary loop code, ranks, parity sectors, Clifford frame group
law, and the strongest covariant sixth-dummy-edge completion.

The result is fixture-specific.  No general local-fermionization no-go or
axiom claim is made.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230

NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COVARIANT_VERTEX_GAMMA_CAR_COMPILER_CYCLE261_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-261 note exists", False, NOTE)
        return
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "six local clifford majoranas",
        "three m2 roles",
        "degree-five",
        "occupation parity",
        "dummy perfect matching",
        "elementary loop",
        "both parity sectors",
        "all 24 proper-cubic frames",
        "group law",
        "held-out l=6",
        "bounded preparation",
        "beta=-0.3",
        "g=0.37",
        "mass seam",
        "bravyi",
        "setia",
        "n1 — alternative routes",
        "n2 — condition independence",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution audit",
        "n6 — partial-closure scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "compiler layers are not physical time",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the Cycle-261 note preserves gamma, parity, N1-N8, and time contracts", not missing, missing)


def local_gamma(label: int) -> c235.Pauli:
    """Jordan-Wigner Clifford gamma on three local qubits."""
    qubit = label // 2
    x = 1 << qubit
    z = (1 << qubit) - 1
    phase = 0
    if label % 2:
        z |= 1 << qubit
        phase = 1
    return c235.Pauli(phase=phase, x=x, z=z)


LOCAL_GAMMAS = tuple(local_gamma(label) for label in range(6))


def shifted_gamma(vertex: int, label: int) -> c235.Pauli:
    gamma = LOCAL_GAMMAS[label]
    shift = 3 * vertex
    return c235.Pauli(gamma.phase, gamma.x << shift, gamma.z << shift)


def missing_gamma_parity(graph: c235.PyramidCellulation, vertex: int) -> c235.Pauli:
    return shifted_gamma(vertex, graph.vertices[vertex][1])


def chirality_parity(vertex: int) -> c235.Pauli:
    return c235.Pauli(z=0b111 << (3 * vertex))


def original_edge_pauli(graph: c235.PyramidCellulation, edge: int) -> c235.Pauli:
    left, right = graph.edges[edge][:2]
    left_label = graph.vertices[right][1]
    right_label = graph.vertices[left][1]
    return shifted_gamma(left, left_label) @ shifted_gamma(right, right_label)


def dummy_edges(graph: c235.PyramidCellulation) -> list[tuple[int, int, tuple[int, int, int]]]:
    result = []
    for cell in graph.cells:
        for direction in (0, 2, 4):
            result.append(
                (
                    graph.vertex_index[(cell, direction)],
                    graph.vertex_index[(cell, direction + 1)],
                    cell,
                )
            )
    return result


def dummy_edge_pauli(
    graph: c235.PyramidCellulation,
    dummies: list[tuple[int, int, tuple[int, int, int]]],
    dummy: int,
) -> c235.Pauli:
    left, right = dummies[dummy][:2]
    return shifted_gamma(left, graph.vertices[left][1]) @ shifted_gamma(
        right, graph.vertices[right][1]
    )


def loop_pauli(
    edge_paulis: list[c235.Pauli], edge_path: list[int]
) -> c235.Pauli:
    result = c235.Pauli(phase=len(edge_path) % 4)
    for edge in edge_path:
        result = result @ edge_paulis[edge]
    return result


def original_loop_pauli(
    graph: c235.PyramidCellulation,
    edge_paulis: list[c235.Pauli],
    vertices: list[int],
) -> c235.Pauli:
    edges = [
        graph.edge_between(vertex, vertices[(index + 1) % len(vertices)])
        for index, vertex in enumerate(vertices)
    ]
    return loop_pauli(edge_paulis, edges)


def total_parity(parities: list[c235.Pauli]) -> c235.Pauli:
    result = c235.Pauli()
    for parity in parities:
        result = result @ parity
    return result


def permutation_parity(permutation: tuple[int, ...]) -> int:
    return sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    ) % 2


def direction_permutations() -> tuple[list[np.ndarray], list[tuple[int, ...]]]:
    frames = c235.proper_cubic_frames()
    directions = tuple(tuple(int(value) for value in row) for row in c235.c210.DIRECTIONS)
    lookup = {direction: index for index, direction in enumerate(directions)}
    permutations = []
    for frame in frames:
        permutations.append(
            tuple(
                lookup[tuple(int(value) for value in frame @ np.asarray(direction))]
                for direction in directions
            )
        )
    return frames, permutations


def local_symplectic_vector(pauli: c235.Pauli) -> int:
    return pauli.x | (pauli.z << 3)


def symplectic_bit(left: int, right: int) -> int:
    left_x = left & 0b111
    left_z = left >> 3
    right_x = right & 0b111
    right_z = right >> 3
    return ((left_x & right_z).bit_count() + (left_z & right_x).bit_count()) % 2


LOCAL_GAMMA_VECTORS = tuple(local_symplectic_vector(gamma) for gamma in LOCAL_GAMMAS)
def gamma_coordinate_table() -> dict[int, int]:
    """Return the GF(2) coordinates of the six local gamma generators."""

    table: dict[int, int] = {}
    for coefficient in range(64):
        vector = 0
        for label in range(6):
            if (coefficient >> label) & 1:
                vector ^= LOCAL_GAMMA_VECTORS[label]
        table[vector] = coefficient
    return table


GAMMA_COORDINATES = gamma_coordinate_table()


def clifford_vector_map(vector: int, permutation: tuple[int, ...]) -> int:
    coefficient = GAMMA_COORDINATES[vector]
    result = 0
    for label in range(6):
        if (coefficient >> label) & 1:
            result ^= LOCAL_GAMMA_VECTORS[permutation[label]]
    return result


def gf2_rank(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for source in rows:
        row = int(source)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def affine_system_ranks(
    rows: list[tuple[int, int]], variables: int
) -> tuple[int, int]:
    coefficient_rank = gf2_rank([mask for mask, _ in rows])
    augmented_rank = gf2_rank(
        [mask | (right_hand_side << variables) for mask, right_hand_side in rows]
    )
    return coefficient_rank, augmented_rank


def gamma_and_clifford_controls() -> None:
    gamma_rank = gf2_rank(list(LOCAL_GAMMA_VECTORS))
    anticommutator_failures = sum(
        symplectic_bit(LOCAL_GAMMA_VECTORS[left], LOCAL_GAMMA_VECTORS[right]) != 1
        for left, right in combinations(range(6), 2)
    )
    nonhermitian = sum(
        (gamma.phase - (gamma.x & gamma.z).bit_count()) % 2 != 0
        for gamma in LOCAL_GAMMAS
    )
    check(
        "six local Clifford Majoranas on three M2 roles are Hermitian, independent, and pairwise anticommuting",
        gamma_rank == 6 and anticommutator_failures == 0 and nonhermitian == 0,
        {
            "gamma_rank": gamma_rank,
            "pair_anticommutator_failures": anticommutator_failures,
            "nonhermitian": nonhermitian,
            "maximum_gamma_support": max((gamma.x | gamma.z).bit_count() for gamma in LOCAL_GAMMAS),
        },
    )

    frames, permutations = direction_permutations()
    frame_lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    symplectic_failures = 0
    gamma_map_failures = 0
    for permutation in permutations:
        for label in range(6):
            gamma_map_failures += (
                clifford_vector_map(LOCAL_GAMMA_VECTORS[label], permutation)
                != LOCAL_GAMMA_VECTORS[permutation[label]]
            )
        for left in range(64):
            for right in range(64):
                symplectic_failures += (
                    symplectic_bit(
                        clifford_vector_map(left, permutation),
                        clifford_vector_map(right, permutation),
                    )
                    != symplectic_bit(left, right)
                )
    group_failures = 0
    for left_index, left_frame in enumerate(frames):
        for right_index, right_frame in enumerate(frames):
            product_index = frame_lookup[
                tuple((left_frame @ right_frame).reshape(-1))
            ]
            for vector in range(64):
                group_failures += (
                    clifford_vector_map(
                        clifford_vector_map(vector, permutations[right_index]),
                        permutations[left_index],
                    )
                    != clifford_vector_map(vector, permutations[product_index])
                )
    missing_gamma_failures = sum(
        clifford_vector_map(LOCAL_GAMMA_VECTORS[direction], permutation)
        != LOCAL_GAMMA_VECTORS[permutation[direction]]
        for permutation in permutations
        for direction in range(6)
    )
    check(
        "the 24 proper-cubic frames define exact symplectic direction-label actions with the full group law",
        symplectic_failures == 0
        and gamma_map_failures == 0
        and group_failures == 0
        and missing_gamma_failures == 0,
        {
            "frames": 24,
            "symplectic_failures": symplectic_failures,
            "gamma_map_failures": gamma_map_failures,
            "group_law_failures": group_failures,
            "missing_gamma_parity_failures": missing_gamma_failures,
            "phase_status": "this vector-level check alone does not resolve Pauli signs or prove positive occupation-parity covariance",
        },
    )


def degree_five_sign_lift_control() -> None:
    """Audit a phase-resolved signed-Pauli lift for the degree-five algebra."""

    frames, permutations = direction_permutations()
    frame_lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    identity = frame_lookup[tuple(np.eye(3, dtype=int).reshape(-1))]
    multiplication = [
        [
            frame_lookup[tuple((frames[left] @ frames[right]).reshape(-1))]
            for right in range(24)
        ]
        for left in range(24)
    ]
    variables = 24 * 6 * 6

    def variable(frame: int, direction: int, label: int) -> int:
        return (frame * 6 + direction) * 6 + label

    rows: list[tuple[int, int]] = []

    def add(indices: list[int], right_hand_side: int = 0) -> None:
        mask = 0
        for index in indices:
            mask ^= 1 << index
        rows.append((mask, right_hand_side))

    # Identity and exact groupoid composition of signed gamma relabelings.
    for direction in range(6):
        for label in range(6):
            add([variable(identity, direction, label)])
    for left in range(24):
        for right in range(24):
            product_frame = multiplication[left][right]
            for direction in range(6):
                for label in range(6):
                    add(
                        [
                            variable(product_frame, direction, label),
                            variable(right, direction, label),
                            variable(
                                left,
                                permutations[right][direction],
                                permutations[right][label],
                            ),
                        ]
                    )
    # The missing gamma B_d must map positively to B_{g d}.
    for frame in range(24):
        for direction in range(6):
            add([variable(frame, direction, direction)])
    # Every unordered direction pair occurs as an original edge role-pair.
    # Its two endpoint signs must cancel so A_{d r} maps positively.
    for frame in range(24):
        for left, right in combinations(range(6), 2):
            add(
                [
                    variable(frame, left, right),
                    variable(frame, right, left),
                ]
            )
    coefficient_rank, augmented_rank = affine_system_ranks(rows, variables)
    check(
        "the degree-five algebra admits a group-law signed-Pauli lift with positive B_v and A_e transformation",
        coefficient_rank == augmented_rank,
        {
            "variables": variables,
            "equations": len(rows),
            "coefficient_rank": coefficient_rank,
            "augmented_rank": augmented_rank,
            "solution_dimension": variables - coefficient_rank,
            "unitary_status": "each signed Pauli automorphism has a local Clifford implementer; scalar phases of those implementers remain projective and do not affect conjugation",
        },
    )


def chirality_sign_lift_control() -> None:
    """Audit a signed lift preserving chirality and every edge generator."""
    frames, permutations = direction_permutations()
    frame_lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    identity = frame_lookup[tuple(np.eye(3, dtype=int).reshape(-1))]
    multiplication = [
        [
            frame_lookup[tuple((frames[left] @ frames[right]).reshape(-1))]
            for right in range(24)
        ]
        for left in range(24)
    ]
    # t[g,d,a] is the sign on gamma_a at source vertex role d.  The system
    # allows vertex-role-dependent signs, imposes the exact groupoid law, and
    # requires product signs to cancel the parity of the six-label permutation
    # so chirality maps with positive sign.
    variables = 24 * 6 * 6

    def variable(frame: int, direction: int, label: int) -> int:
        return (frame * 6 + direction) * 6 + label

    rows: list[tuple[int, int]] = []

    def add(indices: list[int], right_hand_side: int = 0) -> None:
        mask = 0
        for index in indices:
            mask ^= 1 << index
        rows.append((mask, right_hand_side))

    for direction in range(6):
        for label in range(6):
            add([variable(identity, direction, label)])
    for left in range(24):
        for right in range(24):
            product_frame = multiplication[left][right]
            for direction in range(6):
                for label in range(6):
                    add(
                        [
                            variable(product_frame, direction, label),
                            variable(right, direction, label),
                            variable(
                                left,
                                permutations[right][direction],
                                permutations[right][label],
                            ),
                        ]
                    )
    odd_frames = 0
    for frame, permutation in enumerate(permutations):
        parity = permutation_parity(permutation)
        odd_frames += parity
        for direction in range(6):
            add(
                [variable(frame, direction, label) for label in range(6)],
                parity,
            )
        # Original edges realize all unordered pairs of direction roles.
        for left, right in combinations(range(6), 2):
            add(
                [
                    variable(frame, left, right),
                    variable(frame, right, left),
                ]
            )
        # Dummy edges pair opposite roles and use each endpoint's missing
        # gamma.  Their endpoint signs must also cancel.
        for left, right in ((0, 1), (2, 3), (4, 5)):
            add(
                [
                    variable(frame, left, left),
                    variable(frame, right, right),
                ]
            )
    coefficient_rank, augmented_rank = affine_system_ranks(rows, variables)
    check(
        "the degree-six direction action admits a group-law signed-Pauli lift with positive chirality and edge transformation",
        odd_frames > 0 and coefficient_rank == augmented_rank,
        {
            "variables": variables,
            "equations": len(rows),
            "odd_direction_permutations": odd_frames,
            "coefficient_rank": coefficient_rank,
            "augmented_rank": augmented_rank,
            "solution_dimension": variables - coefficient_rank,
            "scope": "signed permutations of the six displayed local gammas, with signs allowed to depend on frame and vertex role; all original and dummy edge signs constrained",
            "unitary_status": "each signed Pauli automorphism has a local Clifford implementer; scalar phases of those implementers remain projective and do not affect conjugation",
        },
    )


@dataclass
class DegreeFiveCode:
    graph: c235.PyramidCellulation
    edge_paulis: list[c235.Pauli]
    parities: list[c235.Pauli]
    local_loops: list[c235.Pauli]
    wilson_loops: list[c235.Pauli]


def degree_five_code(length: int) -> DegreeFiveCode:
    graph = c235.PyramidCellulation(length)
    edges = [original_edge_pauli(graph, edge) for edge in range(len(graph.edges))]
    parities = [missing_gamma_parity(graph, vertex) for vertex in range(len(graph.vertices))]
    local_loops = [
        original_loop_pauli(graph, edges, vertices)
        for _, vertices, _ in c235.primal_edge_cycles(graph)
    ]
    wilson_loops = [
        original_loop_pauli(graph, edges, vertices)
        for vertices in c235.wilson_cycles(graph)
    ]
    return DegreeFiveCode(graph, edges, parities, local_loops, wilson_loops)


@dataclass
class DegreeSixCode:
    graph: c235.PyramidCellulation
    dummies: list[tuple[int, int, tuple[int, int, int]]]
    edge_paulis: list[c235.Pauli]
    parities: list[c235.Pauli]
    local_loops: list[c235.Pauli]
    dummy_triangles: list[c235.Pauli]
    wilson_loops: list[c235.Pauli]


def degree_six_code(length: int) -> DegreeSixCode:
    graph = c235.PyramidCellulation(length)
    dummies = dummy_edges(graph)
    original_edges = [
        original_edge_pauli(graph, edge) for edge in range(len(graph.edges))
    ]
    dummy_paulis = [
        dummy_edge_pauli(graph, dummies, dummy) for dummy in range(len(dummies))
    ]
    edges = original_edges + dummy_paulis
    local_loops = [
        original_loop_pauli(graph, edges, vertices)
        for _, vertices, _ in c235.primal_edge_cycles(graph)
    ]
    dummy_triangles = []
    original_count = len(graph.edges)
    for dummy, (left, right, cell) in enumerate(dummies):
        left_role = graph.vertices[left][1]
        right_role = graph.vertices[right][1]
        for middle_role in range(6):
            if middle_role in (left_role, right_role):
                continue
            middle = graph.vertex_index[(cell, middle_role)]
            dummy_triangles.append(
                loop_pauli(
                    edges,
                    [
                        graph.edge_between(left, middle),
                        graph.edge_between(middle, right),
                        original_count + dummy,
                    ],
                )
            )
    wilson_loops = [
        original_loop_pauli(graph, edges, vertices)
        for vertices in c235.wilson_cycles(graph)
    ]
    parities = [chirality_parity(vertex) for vertex in range(len(graph.vertices))]
    return DegreeSixCode(
        graph,
        dummies,
        edges,
        parities,
        local_loops,
        dummy_triangles,
        wilson_loops,
    )


def direct_algebra_controls() -> None:
    degree_five = degree_five_code(3)
    graph = degree_five.graph
    incident_failures = 0
    parity_failures = 0
    disjoint_failures = 0
    for vertex in range(len(graph.vertices)):
        for left, right in combinations(graph.incident[vertex], 2):
            incident_failures += degree_five.edge_paulis[left].commutes(
                degree_five.edge_paulis[right]
            )
        for edge in graph.incident[vertex]:
            parity_failures += degree_five.parities[vertex].commutes(
                degree_five.edge_paulis[edge]
            )
    for left, right in combinations(range(len(graph.edges)), 2):
        endpoints_left = set(graph.edges[left][:2])
        endpoints_right = set(graph.edges[right][:2])
        if endpoints_left.isdisjoint(endpoints_right):
            disjoint_failures += not degree_five.edge_paulis[left].commutes(
                degree_five.edge_paulis[right]
            )
    check(
        "the degree-five missing-gamma construction has the exact B_v/A_e incidence algebra",
        incident_failures == 0
        and parity_failures == 0
        and disjoint_failures == 0,
        {
            "incident_edge_pair_failures": incident_failures,
            "parity_incidence_failures": parity_failures,
            "disjoint_edge_failures": disjoint_failures,
            "vertices": len(graph.vertices),
            "edges": len(graph.edges),
            "maximum_B_support": max((parity.x | parity.z).bit_count() for parity in degree_five.parities),
            "maximum_A_support": max((edge.x | edge.z).bit_count() for edge in degree_five.edge_paulis),
        },
    )

    full_loops = degree_five.local_loops + degree_five.wilson_loops
    loop_commutator_failures = sum(
        not left.commutes(right)
        for index, left in enumerate(full_loops)
        for right in full_loops[index + 1 :]
    )
    loop_update_failures = sum(
        not loop.commutes(edge)
        for loop in full_loops
        for edge in degree_five.edge_paulis
    )
    nonhermitian = sum(
        (loop.phase - (loop.x & loop.z).bit_count()) % 2 != 0
        for loop in full_loops
    )
    check(
        "the actual L=3 elementary and Wilson loop Paulis commute with the complete degree-five generator algebra",
        loop_commutator_failures == 0
        and loop_update_failures == 0
        and nonhermitian == 0,
        {
            "loop_commutator_failures": loop_commutator_failures,
            "loop_update_failures": loop_update_failures,
            "nonhermitian_loops": nonhermitian,
            "local_loops": len(degree_five.local_loops),
            "Wilson_loops": len(degree_five.wilson_loops),
        },
    )


def degree_five_rank_and_sector_controls() -> None:
    rows = []
    for length in (3, 4, 5, 6):
        code = degree_five_code(length)
        graph = code.graph
        cells = length**3
        qubits = 3 * len(graph.vertices)
        local_rank, local_inconsistent = c235.phase_aware_rank(
            code.local_loops, qubits
        )
        full_loops = code.local_loops + code.wilson_loops
        full_rank, full_inconsistent = c235.phase_aware_rank(full_loops, qubits)
        parity = total_parity(code.parities)
        plus_rank, plus_inconsistent = c235.phase_aware_rank(
            full_loops + [parity], qubits
        )
        minus_parity = c235.Pauli((parity.phase + 2) % 4, parity.x, parity.z)
        minus_rank, minus_inconsistent = c235.phase_aware_rank(
            full_loops + [minus_parity], qubits
        )
        rows.append(
            {
                "L": length,
                "cells": cells,
                "vertices": len(graph.vertices),
                "physical_M2_per_cell": qubits // cells,
                "local_loop_rank": local_rank,
                "full_loop_rank": full_rank,
                "code_exponent": qubits - full_rank,
                "target_full_Fock_exponent": len(graph.vertices),
                "excess_exponent": qubits - full_rank - len(graph.vertices),
                "total_parity_increment": plus_rank - full_rank,
                "plus_sector_exponent": qubits - plus_rank,
                "minus_sector_exponent": qubits - minus_rank,
                "phase_inconsistencies": (
                    len(local_inconsistent),
                    len(full_inconsistent),
                    len(plus_inconsistent),
                    len(minus_inconsistent),
                ),
                "maximum_elementary_loop_support": max(
                    (loop.x | loop.z).bit_count() for loop in code.local_loops
                ),
                "maximum_Wilson_support": max(
                    (loop.x | loop.z).bit_count() for loop in code.wilson_loops
                ),
                "total_parity_support": (parity.x | parity.z).bit_count(),
            }
        )
    check(
        "degree-five elementary loops are bounded and both parity sectors are nonempty, but the code has an exact V/2-1 auxiliary excess",
        all(
            row["physical_M2_per_cell"] == 18
            and row["local_loop_rank"] == 9 * row["cells"] - 2
            and row["full_loop_rank"] == 9 * row["cells"] + 1
            and row["code_exponent"] == 9 * row["cells"] - 1
            and row["target_full_Fock_exponent"] == 6 * row["cells"]
            and row["excess_exponent"] == 3 * row["cells"] - 1
            and row["total_parity_increment"] == 1
            and row["plus_sector_exponent"] == 9 * row["cells"] - 2
            and row["minus_sector_exponent"] == 9 * row["cells"] - 2
            and row["phase_inconsistencies"] == (0, 0, 0, 0)
            for row in rows
        ),
        rows,
    )


def dummy_matching_covariance_controls() -> None:
    frame_failures = 0
    translation_failures = 0
    rows = []
    for length in (3, 4, 5, 6):
        graph = c235.PyramidCellulation(length)
        dummies = dummy_edges(graph)
        dummy_set = {frozenset(edge[:2]) for edge in dummies}
        for frame in c235.proper_cubic_frames():
            vertex_map, _ = c235.graph_frame_maps(graph, frame)
            frame_failures += {
                frozenset((vertex_map[left], vertex_map[right]))
                for left, right, _ in dummies
            } != dummy_set
        for displacement in product(range(length), repeat=3):
            vertex_map = []
            for cell, role in graph.vertices:
                moved = tuple(
                    (cell[axis] + displacement[axis]) % length
                    for axis in range(3)
                )
                vertex_map.append(graph.vertex_index[(moved, role)])
            translation_failures += {
                frozenset((vertex_map[left], vertex_map[right]))
                for left, right, _ in dummies
            } != dummy_set
        rows.append(
            {
                "L": length,
                "dummy_edges": len(dummies),
                "expected_perfect_matching": len(graph.vertices) // 2,
                "maximum_dummy_edge_support": max(
                    (
                        dummy_edge_pauli(graph, dummies, dummy).x
                        | dummy_edge_pauli(graph, dummies, dummy).z
                    ).bit_count()
                    for dummy in range(len(dummies))
                ),
            }
        )
    check(
        "opposite-role onsite pairs form a genuine proper-cubic and coarse-translation-covariant sixth-edge perfect matching",
        frame_failures == 0
        and translation_failures == 0
        and all(
            row["dummy_edges"] == row["expected_perfect_matching"]
            for row in rows
        ),
        {
            "frame_failures": frame_failures,
            "translation_failures": translation_failures,
            "sizes": rows,
            "marked_pair": False,
        },
    )


def degree_six_rank_and_sector_controls() -> None:
    rows = []
    direct_l3 = None
    for length in (3, 4, 5, 6):
        code = degree_six_code(length)
        graph = code.graph
        cells = length**3
        qubits = 3 * len(graph.vertices)
        local_loops = code.local_loops + code.dummy_triangles
        full_loops = local_loops + code.wilson_loops
        local_rank, local_inconsistent = c235.phase_aware_rank(local_loops, qubits)
        full_rank, full_inconsistent = c235.phase_aware_rank(full_loops, qubits)
        parity = total_parity(code.parities)
        plus_rank, plus_inconsistent = c235.phase_aware_rank(
            full_loops + [parity], qubits
        )
        minus = c235.Pauli((parity.phase + 2) % 4, parity.x, parity.z)
        minus_rank, minus_inconsistent = c235.phase_aware_rank(
            full_loops + [minus], qubits
        )
        rows.append(
            {
                "L": length,
                "cells": cells,
                "vertices": len(graph.vertices),
                "dummy_edges": len(code.dummies),
                "local_augmented_rank": local_rank,
                "full_augmented_rank": full_rank,
                "code_exponent": qubits - full_rank,
                "target_even_sector_exponent": len(graph.vertices) - 1,
                "total_parity_increment": plus_rank - full_rank,
                "plus_sector_consistent": not plus_inconsistent,
                "minus_sector_consistent": not minus_inconsistent,
                "minus_sector_inconsistencies": len(minus_inconsistent),
                "phase_inconsistencies": (
                    len(local_inconsistent),
                    len(full_inconsistent),
                ),
                "maximum_elementary_loop_support": max(
                    (loop.x | loop.z).bit_count() for loop in local_loops
                ),
                "maximum_Wilson_support": max(
                    (loop.x | loop.z).bit_count() for loop in code.wilson_loops
                ),
                "total_parity_support": (parity.x | parity.z).bit_count(),
            }
        )
        if length == 3:
            loop_commutators = sum(
                not left.commutes(right)
                for index, left in enumerate(full_loops)
                for right in full_loops[index + 1 :]
            )
            loop_update_failures = sum(
                not loop.commutes(edge)
                for loop in full_loops
                for edge in code.edge_paulis
            )
            nonhermitian = sum(
                (loop.phase - (loop.x & loop.z).bit_count()) % 2 != 0
                for loop in full_loops
            )
            direct_l3 = {
                "loop_commutator_failures": loop_commutators,
                "loop_update_failures": loop_update_failures,
                "nonhermitian_loops": nonhermitian,
            }
    check(
        "the covariant degree-six dummy completion has the exact GSE even-sector rank but fixes total parity and deletes the odd sector",
        all(
            row["dummy_edges"] == 3 * row["cells"]
            and row["local_augmented_rank"] == 12 * row["cells"] - 2
            and row["full_augmented_rank"] == 12 * row["cells"] + 1
            and row["code_exponent"] == 6 * row["cells"] - 1
            and row["target_even_sector_exponent"] == 6 * row["cells"] - 1
            and row["total_parity_increment"] == 0
            and row["plus_sector_consistent"]
            and not row["minus_sector_consistent"]
            and row["minus_sector_inconsistencies"] > 0
            and row["phase_inconsistencies"] == (0, 0)
            for row in rows
        )
        and direct_l3 == {
            "loop_commutator_failures": 0,
            "loop_update_failures": 0,
            "nonhermitian_loops": 0,
        },
        {"sizes": rows, "direct_L3": direct_l3},
    )


def macro_placement_controls() -> None:
    directions = tuple(np.asarray(row, dtype=int) for row in c235.c210.DIRECTIONS)

    def coordinate(vector, modulus=64):
        return tuple(int(value) % modulus for value in vector)

    shells = {
        shell: {coordinate(radius * direction) for direction in directions}
        for shell, radius in enumerate((6, 12, 18))
    }
    all_points = set().union(*shells.values())
    collisions = sum(len(points) for points in shells.values()) - len(all_points)
    frame_failures = 0
    for frame in c235.proper_cubic_frames():
        for points in shells.values():
            frame_failures += {
                coordinate(frame @ np.asarray(point)) for point in points
            } != points
    length = 3
    modulus = 64 * length
    active = {
        tuple((64 * cell[axis] + point[axis]) % modulus for axis in range(3))
        for cell in product(range(length), repeat=3)
        for points in shells.values()
        for point in points
    }

    def moved(displacement):
        return {
            tuple((point[axis] + displacement[axis]) % modulus for axis in range(3))
            for point in active
        }

    check(
        "three proper-cubic radial M2 shells give 18 collision-free physical roles per coarse cell with constant routing overhead",
        collisions == 0
        and frame_failures == 0
        and len(all_points) == 18
        and active == moved((64, 0, 0))
        and active != moved((1, 0, 0)),
        {
            "roles_per_cell": len(all_points),
            "shell_sizes": {shell: len(points) for shell, points in shells.items()},
            "collisions": collisions,
            "proper_frame_failures": frame_failures,
            "period64_translation_difference": len(active ^ moved((64, 0, 0))),
            "unit_translation_difference": len(active ^ moved((1, 0, 0))),
            "macro_marker": "supplied",
        },
    )


def preparation_and_fixture_firewall() -> None:
    code5 = degree_five_code(3)
    code6 = degree_six_code(3)
    qubits = 3 * len(code5.graph.vertices)
    rank5_local = c235.gf2_rank(
        loop.symplectic(qubits) for loop in code5.local_loops
    )
    rank5_full = c235.gf2_rank(
        loop.symplectic(qubits)
        for loop in code5.local_loops + code5.wilson_loops
    )
    local6 = code6.local_loops + code6.dummy_triangles
    rank6_local = c235.gf2_rank(loop.symplectic(qubits) for loop in local6)
    rank6_full = c235.gf2_rank(
        loop.symplectic(qubits) for loop in local6 + code6.wilson_loops
    )
    check(
        "bounded elementary checks leave three Wilson logicals in both candidates, so bounded preparation and sector selection are not constructed",
        rank5_full - rank5_local == 3 and rank6_full - rank6_local == 3,
        {
            "degree5_Wilson_increment": rank5_full - rank5_local,
            "degree6_Wilson_increment": rank6_full - rank6_local,
            "bounded_preparation": False,
            "degree5_sector_selection": "both sectors exist; selecting one uses extensive total parity",
            "degree6_sector_selection": "even parity is fixed by the stabilizer group; odd parity is absent",
            "autonomous_preparation": "not constructed",
        },
    )

    species = c219.common_species(c230.BETA)
    rest = c219.rest_mass(species)
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "the fixed Cycle-230 gates and mass/contact/seam fixtures remain separate because neither candidate supplies one common full-Fock E",
        abs(c230.BETA + 0.3) < 1e-15
        and abs(c230.COUPLING - 0.37) < 1e-15
        and abs(rest / species.analytic_mass - 1) < 2e-12
        and sea_rank == 73,
        {
            "beta": c230.BETA,
            "g": c230.COUPLING,
            "rest_mass_predecessor": rest,
            "principal_sea_rank_predecessor": sea_rank,
            "degree5_common_full_Fock_E": False,
            "degree6_common_full_Fock_E": False,
            "coin_A_B_FSWAP_contact_synthesis": "not reached",
            "mass_seam_intertwining": "not claimed",
        },
    )


def time_and_scope_firewall() -> None:
    check(
        "the Clifford schedules and stabilizer preparation resources are not physical time or Records",
        True,
        {
            "compiler_layers_are_not_physical_time": True,
            "gamma_roles": "coherent local Clifford carriers, not Records",
            "dummy_edges": "code-design relations, not realized histories",
            "universal_no_go": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    note_contract()
    gamma_and_clifford_controls()
    degree_five_sign_lift_control()
    direct_algebra_controls()
    degree_five_rank_and_sector_controls()
    dummy_matching_covariance_controls()
    chirality_sign_lift_control()
    degree_six_rank_and_sector_controls()
    macro_placement_controls()
    preparation_and_fixture_firewall()
    time_and_scope_firewall()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
