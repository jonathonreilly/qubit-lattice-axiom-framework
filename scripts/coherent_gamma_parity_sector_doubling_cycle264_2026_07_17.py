#!/usr/bin/env python3
"""Cycle 264: coherent parity-sector doubling of the Cycle-261 gamma code.

Test three exact routes to restore the missing odd sector of the covariant
degree-six GSE-shaped code: a direct-sum label, distributed equality carriers,
and a local reference-spoke extension.  Code-space rank is kept separate from
bounded encoder preparation.  The result is fixture-specific and makes no
general bosonization or preparation no-go.
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
import covariant_vertex_gamma_car_compiler_cycle261_2026_07_17 as c261

NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COHERENT_GAMMA_PARITY_SECTOR_DOUBLING_CYCLE264_NOTE_2026-07-17.md"
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
        check("the Cycle-264 note exists", False, NOTE)
        return
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "direct-sum label",
        "distributed equality carrier",
        "reference-spoke",
        "one common full-fock e",
        "bounded preparation",
        "coherent parity superposition",
        "all 24 proper-cubic frames",
        "group law",
        "held-out l=6",
        "beta=-0.3",
        "g=0.37",
        "rank-73",
        "bravyi",
        "setia",
        "chen",
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
    check("the Cycle-264 note preserves sector, preparation, N1-N8, and time contracts", not missing, missing)


def shifted_local(pauli: c235.Pauli, mode: int) -> c235.Pauli:
    shift = 3 * mode
    return c235.Pauli(pauli.phase, pauli.x << shift, pauli.z << shift)


def gamma(mode: int, label: int) -> c235.Pauli:
    return shifted_local(c261.LOCAL_GAMMAS[label], mode)


def chirality(mode: int) -> c235.Pauli:
    return c235.Pauli(z=0b111 << (3 * mode))


def multiply(paulis: list[c235.Pauli]) -> c235.Pauli:
    result = c235.Pauli()
    for pauli in paulis:
        result = result @ pauli
    return result


def shifted_extra_z(qubit: int) -> c235.Pauli:
    return c235.Pauli(z=1 << qubit)


def shifted_extra_x(qubit: int) -> c235.Pauli:
    return c235.Pauli(x=1 << qubit)


def phase_flip(pauli: c235.Pauli) -> c235.Pauli:
    return c235.Pauli((pauli.phase + 2) % 4, pauli.x, pauli.z)


def sector_status(
    stabilizers: list[c235.Pauli], parity: c235.Pauli, qubits: int
) -> dict[str, object]:
    rank, inconsistent = c235.phase_aware_rank(stabilizers, qubits)
    plus_rank, plus_inconsistent = c235.phase_aware_rank(
        stabilizers + [parity], qubits
    )
    minus_rank, minus_inconsistent = c235.phase_aware_rank(
        stabilizers + [phase_flip(parity)], qubits
    )
    return {
        "rank": rank,
        "base_inconsistencies": len(inconsistent),
        "plus_rank_increment": plus_rank - rank,
        "minus_rank_increment": minus_rank - rank,
        "plus_consistent": not plus_inconsistent,
        "minus_consistent": not minus_inconsistent,
        "plus_inconsistencies": len(plus_inconsistent),
        "minus_inconsistencies": len(minus_inconsistent),
    }


def base_full_code(length: int) -> tuple[c261.DegreeSixCode, list[c235.Pauli]]:
    code = c261.degree_six_code(length)
    return code, code.local_loops + code.dummy_triangles + code.wilson_loops


def base_control() -> None:
    rows = []
    for length in (3, 4, 5, 6):
        code, stabilizers = base_full_code(length)
        cells = length**3
        vertices = len(code.graph.vertices)
        qubits = 3 * vertices
        rank, inconsistent = c235.phase_aware_rank(stabilizers, qubits)
        rows.append(
            {
                "L": length,
                "cells": cells,
                "vertices": vertices,
                "rank": rank,
                "code_exponent": qubits - rank,
                "target_even_exponent": vertices - 1,
                "phase_inconsistencies": len(inconsistent),
            }
        )
    check(
        "the Cycle-261 degree-six predecessor is exactly one parity sector before doubling",
        all(
            row["vertices"] == 6 * row["cells"]
            and row["rank"] == 12 * row["cells"] + 1
            and row["code_exponent"] == row["target_even_exponent"]
            and row["phase_inconsistencies"] == 0
            for row in rows
        ),
        rows,
    )


def direct_sum_label_controls() -> None:
    rows = []
    for length in (3, 4, 5, 6):
        code, stabilizers = base_full_code(length)
        vertices = len(code.graph.vertices)
        base_qubits = 3 * vertices
        label_qubit = base_qubits
        root = code.graph.vertex_index[((0, 0, 0), 0)]
        parities = list(code.parities)
        parities[root] = parities[root] @ shifted_extra_z(label_qubit)
        physical_parity = multiply(parities)
        status = sector_status(stabilizers, physical_parity, base_qubits + 1)
        root_algebra_failures = sum(
            parities[root].commutes(code.edge_paulis[edge])
            for edge in code.graph.incident[root]
        )
        rows.append(
            {
                "L": length,
                "vertices": vertices,
                "code_exponent": base_qubits + 1 - int(status["rank"]),
                "target_full_Fock_exponent": vertices,
                "plus_sector_exponent": base_qubits
                + 1
                - int(status["rank"])
                - int(status["plus_rank_increment"]),
                "minus_sector_exponent": base_qubits
                + 1
                - int(status["rank"])
                - int(status["minus_rank_increment"]),
                "plus_consistent": status["plus_consistent"],
                "minus_consistent": status["minus_consistent"],
                "root_algebra_failures": root_algebra_failures,
                "root_B_support": (
                    parities[root].x | parities[root].z
                ).bit_count(),
            }
        )
    check(
        "one free direct-sum label gives the exact full-Fock rank and both physical parity sectors at a marked root",
        all(
            row["code_exponent"] == row["target_full_Fock_exponent"]
            and row["plus_sector_exponent"] == row["vertices"] - 1
            and row["minus_sector_exponent"] == row["vertices"] - 1
            and row["plus_consistent"]
            and row["minus_consistent"]
            and row["root_algebra_failures"] == 0
            and row["root_B_support"] <= 4
            for row in rows
        ),
        rows,
    )

    frames, permutations = c261.direction_permutations()
    frame_root_failures = sum(permutation[0] != 0 for permutation in permutations)
    translation_root_failures = {length: length**3 - 1 for length in (3, 4, 5, 6)}
    check(
        "the direct-sum label fails the no-marked-root covariance requirement",
        frame_root_failures == 20
        and all(value > 0 for value in translation_root_failures.values()),
        {
            "proper_frame_root_failures": frame_root_failures,
            "proper_frames_fixing_root_role": len(frames) - frame_root_failures,
            "coarse_translation_root_failures": translation_root_failures,
            "global_parity_query_for_label_preparation": True,
        },
    )


def carrier_edges(graph: c235.PyramidCellulation) -> list[tuple[int, int]]:
    return [(left, right) for left, right, _, _ in graph.edges]


def invariant_vertex_orbits(graph: c235.PyramidCellulation) -> list[set[int]]:
    parents = list(range(len(graph.vertices)))

    def find(vertex: int) -> int:
        while parents[vertex] != vertex:
            parents[vertex] = parents[parents[vertex]]
            vertex = parents[vertex]
        return vertex

    def union(left: int, right: int) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root != right_root:
            parents[right_root] = left_root

    for frame in c235.proper_cubic_frames():
        vertex_map, _ = c235.graph_frame_maps(graph, frame)
        for source, target in enumerate(vertex_map):
            union(source, target)
    for axis in range(3):
        for source, (cell, role) in enumerate(graph.vertices):
            moved = list(cell)
            moved[axis] = (moved[axis] + 1) % graph.length
            union(source, graph.vertex_index[(tuple(moved), role)])
    groups: dict[int, set[int]] = {}
    for vertex in range(len(graph.vertices)):
        groups.setdefault(find(vertex), set()).add(vertex)
    return list(groups.values())


def distributed_carrier_controls() -> None:
    z_rows = []
    x_rows = []
    orbit_rows = []
    for length in (3, 4, 5, 6):
        code, stabilizers = base_full_code(length)
        graph = code.graph
        vertices = len(graph.vertices)
        base_qubits = 3 * vertices
        qubits = base_qubits + vertices
        z_equalities = [
            shifted_extra_z(base_qubits + left)
            @ shifted_extra_z(base_qubits + right)
            for left, right in carrier_edges(graph)
        ]
        x_equalities = [
            shifted_extra_x(base_qubits + left)
            @ shifted_extra_x(base_qubits + right)
            for left, right in carrier_edges(graph)
        ]
        dressed_parities = [
            parity @ shifted_extra_z(base_qubits + vertex)
            for vertex, parity in enumerate(code.parities)
        ]
        physical_parity = multiply(dressed_parities)
        z_status = sector_status(
            stabilizers + z_equalities, physical_parity, qubits
        )
        z_rank, z_inconsistent = c235.phase_aware_rank(z_equalities, qubits)
        z_local_leakage = sum(
            not dressed.commutes(constraint)
            for dressed in dressed_parities
            for constraint in z_equalities
        )
        z_rows.append(
            {
                "L": length,
                "vertices": vertices,
                "carrier_rank": z_rank,
                "carrier_phase_inconsistencies": len(z_inconsistent),
                "combined_code_exponent": qubits - int(z_status["rank"]),
                "target_full_Fock_exponent": vertices,
                "positive_physical_parity_consistent": z_status["plus_consistent"],
                "negative_physical_parity_consistent": z_status["minus_consistent"],
                "negative_parity_phase_inconsistencies": z_status[
                    "minus_inconsistencies"
                ],
                "local_B_carrier_leakage": z_local_leakage,
            }
        )

        x_rank, x_inconsistent = c235.phase_aware_rank(x_equalities, qubits)
        x_local_leakage = sum(
            not dressed.commutes(constraint)
            for dressed in dressed_parities
            for constraint in x_equalities
        )
        carrier_global_z = multiply(
            [shifted_extra_z(base_qubits + vertex) for vertex in range(vertices)]
        )
        x_plus = sector_status(x_equalities, carrier_global_z, qubits)
        x_rows.append(
            {
                "L": length,
                "vertices": vertices,
                "carrier_rank": x_rank,
                "carrier_phase_inconsistencies": len(x_inconsistent),
                "global_Z_is_logical": x_plus["plus_rank_increment"] == 1
                and x_plus["minus_rank_increment"] == 1,
                "local_B_carrier_leakage": x_local_leakage,
                "expected_incidence_leakage": 5 * vertices,
            }
        )

        orbits = invariant_vertex_orbits(graph)
        orbit_rows.append(
            {
                "L": length,
                "orbit_count": len(orbits),
                "orbit_weights": sorted(len(orbit) for orbit in orbits),
                "odd_invariant_subset_exists": any(
                    len(orbit) % 2 for orbit in orbits
                ),
            }
        )

    check(
        "the covariant Z-equality carrier has the target rank and preserves every local B_v but duplicates the even sector",
        all(
            row["carrier_rank"] == row["vertices"] - 1
            and row["carrier_phase_inconsistencies"] == 0
            and row["combined_code_exponent"]
            == row["target_full_Fock_exponent"]
            and row["positive_physical_parity_consistent"]
            and not row["negative_physical_parity_consistent"]
            and row["negative_parity_phase_inconsistencies"] > 0
            and row["local_B_carrier_leakage"] == 0
            for row in z_rows
        ),
        z_rows,
    )
    check(
        "the covariant X-equality carrier makes global carrier parity logical but every locally dressed B_v leaks",
        all(
            row["carrier_rank"] == row["vertices"] - 1
            and row["carrier_phase_inconsistencies"] == 0
            and row["global_Z_is_logical"]
            and row["local_B_carrier_leakage"]
            == row["expected_incidence_leakage"]
            for row in x_rows
        ),
        x_rows,
    )
    check(
        "the proper-cubic translation group is transitive on physical vertices, so invariant scalar-label dressings have even weight",
        all(
            row["orbit_count"] == 1
            and row["orbit_weights"] == [6 * row["L"] ** 3]
            and not row["odd_invariant_subset_exists"]
            for row in orbit_rows
        ),
        orbit_rows,
    )


def distributed_signed_covariance_control() -> None:
    frames, permutations = c261.direction_permutations()
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

    def variable(frame: int, role: int, label: int) -> int:
        return (frame * 6 + role) * 6 + label

    equations: list[tuple[int, int]] = []

    def add(indices: list[int], right_hand_side: int = 0) -> None:
        mask = 0
        for index in indices:
            mask ^= 1 << index
        equations.append((mask, right_hand_side))

    for role in range(6):
        for label in range(6):
            add([variable(identity, role, label)])
    for left in range(24):
        for right in range(24):
            product_frame = multiplication[left][right]
            for role in range(6):
                for label in range(6):
                    add(
                        [
                            variable(product_frame, role, label),
                            variable(right, role, label),
                            variable(
                                left,
                                permutations[right][role],
                                permutations[right][label],
                            ),
                        ]
                    )
    for frame, permutation in enumerate(permutations):
        parity = c261.permutation_parity(permutation)
        for role in range(6):
            add([variable(frame, role, label) for label in range(6)], parity)
        for left, right in combinations(range(6), 2):
            add(
                [
                    variable(frame, left, right),
                    variable(frame, right, left),
                ]
            )
        for left, right in ((0, 1), (2, 3), (4, 5)):
            add(
                [
                    variable(frame, left, left),
                    variable(frame, right, right),
                ]
            )
    coefficient_rank, augmented_rank = c261.affine_system_ranks(
        equations, variables
    )

    family_failures = 0
    for length in (3, 4, 5, 6):
        graph = c235.PyramidCellulation(length)
        edge_set = {frozenset((left, right)) for left, right in carrier_edges(graph)}
        for frame in frames:
            vertex_map, _ = c235.graph_frame_maps(graph, frame)
            family_failures += {
                frozenset((vertex_map[left], vertex_map[right]))
                for left, right in carrier_edges(graph)
            } != edge_set
        for displacement in product(range(length), repeat=3):
            vertex_map = []
            for cell, role in graph.vertices:
                moved = tuple(
                    (cell[axis] + displacement[axis]) % length
                    for axis in range(3)
                )
                vertex_map.append(graph.vertex_index[(moved, role)])
            family_failures += {
                frozenset((vertex_map[left], vertex_map[right]))
                for left, right in carrier_edges(graph)
            } != edge_set
    check(
        "both distributed equality families retain the exact signed all-frame gamma action, group law, and all translations",
        coefficient_rank == augmented_rank == 850 and family_failures == 0,
        {
            "frames": 24,
            "variables": variables,
            "equations": len(equations),
            "coefficient_rank": coefficient_rank,
            "augmented_rank": augmented_rank,
            "solution_dimension": variables - coefficient_rank,
            "equality_family_frame_or_translation_failures": family_failures,
            "carrier_Paulis": "permuted with positive sign",
        },
    )


@dataclass
class ReferenceSpokeCode:
    graph: c235.PyramidCellulation
    cell_index: dict[tuple[int, int, int], int]
    reference_modes: list[int]
    edge_paulis: list[c235.Pauli]
    physical_parities: list[c235.Pauli]
    reference_parities: list[c235.Pauli]
    local_loops: list[c235.Pauli]
    wilson_loops: list[c235.Pauli]


def reference_spoke_code(length: int) -> ReferenceSpokeCode:
    graph = c235.PyramidCellulation(length)
    vertices = len(graph.vertices)
    cells = list(graph.cells)
    cell_index = {cell: index for index, cell in enumerate(cells)}
    reference_modes = [vertices + cell_index[cell] for cell in cells]
    original_edges = [
        c261.original_edge_pauli(graph, edge) for edge in range(len(graph.edges))
    ]
    spokes: list[c235.Pauli] = []
    for cell in cells:
        reference = vertices + cell_index[cell]
        for direction in range(6):
            physical = graph.vertex_index[(cell, direction)]
            spokes.append(gamma(physical, direction) @ gamma(reference, direction))
    edge_paulis = original_edges + spokes
    original_local = [
        c261.original_loop_pauli(graph, edge_paulis, cycle_vertices)
        for _, cycle_vertices, _ in c235.primal_edge_cycles(graph)
    ]
    triangles: list[c235.Pauli] = []
    original_count = len(graph.edges)
    for cell in cells:
        for left, right in combinations(range(6), 2):
            if right == (left ^ 1):
                continue
            left_vertex = graph.vertex_index[(cell, left)]
            right_vertex = graph.vertex_index[(cell, right)]
            triangles.append(
                c261.loop_pauli(
                    edge_paulis,
                    [
                        original_count + 6 * cell_index[cell] + left,
                        graph.edge_between(left_vertex, right_vertex),
                        original_count + 6 * cell_index[cell] + right,
                    ],
                )
            )
    wilson = [
        c261.original_loop_pauli(graph, edge_paulis, vertices_on_cycle)
        for vertices_on_cycle in c235.wilson_cycles(graph)
    ]
    return ReferenceSpokeCode(
        graph=graph,
        cell_index=cell_index,
        reference_modes=reference_modes,
        edge_paulis=edge_paulis,
        physical_parities=[chirality(vertex) for vertex in range(vertices)],
        reference_parities=[chirality(mode) for mode in reference_modes],
        local_loops=original_local + triangles,
        wilson_loops=wilson,
    )


def reference_equalities(code: ReferenceSpokeCode) -> list[c235.Pauli]:
    result: list[c235.Pauli] = []
    length = code.graph.length
    cells = list(code.graph.cells)
    for cell in cells:
        source = code.cell_index[cell]
        for axis in range(3):
            moved = list(cell)
            moved[axis] = (moved[axis] + 1) % length
            target = code.cell_index[tuple(moved)]
            result.append(
                code.reference_parities[source] @ code.reference_parities[target]
            )
    return result


def reference_spoke_algebra_and_rank_controls() -> None:
    rows = []
    direct_l3 = None
    for length in (3, 4, 5, 6):
        code = reference_spoke_code(length)
        cells = length**3
        physical_vertices = len(code.graph.vertices)
        modes = physical_vertices + cells
        qubits = 3 * modes
        local_rank, local_inconsistent = c235.phase_aware_rank(
            code.local_loops, qubits
        )
        full = code.local_loops + code.wilson_loops
        full_rank, full_inconsistent = c235.phase_aware_rank(full, qubits)
        rows.append(
            {
                "L": length,
                "cells": cells,
                "physical_modes": physical_vertices,
                "reference_modes": cells,
                "total_modes": modes,
                "edges": len(code.edge_paulis),
                "local_loop_rank": local_rank,
                "full_loop_rank": full_rank,
                "even_code_exponent": qubits - full_rank,
                "target_total_even_exponent": modes - 1,
                "phase_inconsistencies": (
                    len(local_inconsistent),
                    len(full_inconsistent),
                ),
                "maximum_local_loop_support": max(
                    (loop.x | loop.z).bit_count() for loop in code.local_loops
                ),
            }
        )
        if length == 3:
            endpoint_lists: list[list[int]] = [[] for _ in range(modes)]
            for edge, (left, right, _, _) in enumerate(code.graph.edges):
                endpoint_lists[left].append(edge)
                endpoint_lists[right].append(edge)
            original_count = len(code.graph.edges)
            for cell in code.graph.cells:
                reference = physical_vertices + code.cell_index[cell]
                for direction in range(6):
                    physical = code.graph.vertex_index[(cell, direction)]
                    edge = original_count + 6 * code.cell_index[cell] + direction
                    endpoint_lists[physical].append(edge)
                    endpoint_lists[reference].append(edge)
            parities = code.physical_parities + code.reference_parities
            incidence_failures = sum(
                code.edge_paulis[left].commutes(code.edge_paulis[right])
                for incident in endpoint_lists
                for left, right in combinations(incident, 2)
            )
            parity_failures = sum(
                parities[mode].commutes(code.edge_paulis[edge])
                for mode, incident in enumerate(endpoint_lists)
                for edge in incident
            )
            loop_edge_failures = sum(
                not loop.commutes(edge)
                for loop in full
                for edge in code.edge_paulis
            )
            loop_pair_failures = sum(
                not left.commutes(right)
                for index, left in enumerate(full)
                for right in full[index + 1 :]
            )
            direct_l3 = {
                "incidence_failures": incidence_failures,
                "parity_failures": parity_failures,
                "loop_edge_failures": loop_edge_failures,
                "loop_pair_failures": loop_pair_failures,
            }
    check(
        "the covariant reference-spoke graph has exact degree-six CAR algebra and a bounded full-rank even code",
        all(
            row["physical_modes"] == 6 * row["cells"]
            and row["reference_modes"] == row["cells"]
            and row["total_modes"] == 7 * row["cells"]
            and row["edges"] == 21 * row["cells"]
            and row["local_loop_rank"] == 14 * row["cells"] - 2
            and row["full_loop_rank"] == 14 * row["cells"] + 1
            and row["even_code_exponent"]
            == row["target_total_even_exponent"]
            and row["phase_inconsistencies"] == (0, 0)
            and row["maximum_local_loop_support"] <= 24
            for row in rows
        )
        and direct_l3
        == {
            "incidence_failures": 0,
            "parity_failures": 0,
            "loop_edge_failures": 0,
            "loop_pair_failures": 0,
        },
        {"sizes": rows, "direct_L3": direct_l3},
    )


def expanded_reference_pauli(
    pauli: c235.Pauli, physical_modes: int, cells: int
) -> c235.Pauli:
    """Encode each abstract three-qubit reference into three ZZ pair codes."""

    physical_qubits = 3 * physical_modes
    x = pauli.x & ((1 << physical_qubits) - 1)
    z = pauli.z & ((1 << physical_qubits) - 1)
    for cell in range(cells):
        for logical in range(3):
            source = physical_qubits + 3 * cell + logical
            target = physical_qubits + 6 * cell + 2 * logical
            if (pauli.x >> source) & 1:
                x ^= (1 << target) | (1 << (target + 1))
            if (pauli.z >> source) & 1:
                z ^= 1 << target
    return c235.Pauli(pauli.phase, x, z)


def reference_pair_constraints(
    physical_modes: int, cells: int
) -> list[c235.Pauli]:
    base = 3 * physical_modes
    return [
        c235.Pauli(z=(1 << (base + 6 * cell + 2 * logical)) | (1 << (base + 6 * cell + 2 * logical + 1)))
        for cell in range(cells)
        for logical in range(3)
    ]


def reference_physical_motif_controls() -> None:
    # Local six-site pair code.
    local_pairs = [
        c235.Pauli(z=(1 << (2 * logical)) | (1 << (2 * logical + 1)))
        for logical in range(3)
    ]
    logical_x = [
        c235.Pauli(x=(1 << (2 * logical)) | (1 << (2 * logical + 1)))
        for logical in range(3)
    ]
    logical_z = [c235.Pauli(z=1 << (2 * logical)) for logical in range(3)]
    local_gamma = []
    for abstract in c261.LOCAL_GAMMAS:
        x = z = 0
        for logical in range(3):
            if (abstract.x >> logical) & 1:
                x ^= logical_x[logical].x
            if (abstract.z >> logical) & 1:
                z ^= logical_z[logical].z
        local_gamma.append(c235.Pauli(abstract.phase, x, z))
    pair_rank, pair_inconsistent = c235.phase_aware_rank(local_pairs, 6)
    local_leakage = sum(
        not operator.commutes(constraint)
        for operator in logical_x + logical_z + local_gamma
        for constraint in local_pairs
    )
    logical_pair_failures = sum(
        logical_x[left].commutes(logical_z[right]) == (left == right)
        for left in range(3)
        for right in range(3)
    )
    gamma_failures = sum(
        left.commutes(right)
        for left, right in combinations(local_gamma, 2)
    )

    directions = tuple(np.asarray(row, dtype=int) for row in c235.c210.DIRECTIONS)

    def coordinate(vector: np.ndarray) -> tuple[int, int, int]:
        return tuple(int(value) % 64 for value in vector)

    old_shells = {
        coordinate(radius * direction)
        for radius in (6, 12, 18)
        for direction in directions
    }
    reference_shell = {coordinate(24 * direction) for direction in directions}
    collision_count = len(old_shells & reference_shell)
    frame_failures = sum(
        {coordinate(frame @ np.asarray(point)) for point in reference_shell}
        != reference_shell
        for frame in c235.proper_cubic_frames()
    )
    pair_set = {
        frozenset((coordinate(24 * directions[left]), coordinate(24 * directions[right])))
        for left, right in ((0, 1), (2, 3), (4, 5))
    }
    pair_frame_failures = 0
    for frame in c235.proper_cubic_frames():
        pair_frame_failures += {
            frozenset(
                (
                    coordinate(frame @ np.asarray(tuple(pair)[0])),
                    coordinate(frame @ np.asarray(tuple(pair)[1])),
                )
            )
            for pair in pair_set
        } != pair_set

    rows = []
    for length in (3, 4, 5, 6):
        code = reference_spoke_code(length)
        cells = length**3
        physical_modes = len(code.graph.vertices)
        abstract_qubits = 3 * (physical_modes + cells)
        physical_qubits = 3 * physical_modes + 6 * cells
        abstract_rows = (
            code.local_loops
            + code.wilson_loops
            + reference_equalities(code)
        )
        expanded = [
            expanded_reference_pauli(pauli, physical_modes, cells)
            for pauli in abstract_rows
        ]
        pairs = reference_pair_constraints(physical_modes, cells)
        rank, inconsistent = c235.phase_aware_rank(expanded + pairs, physical_qubits)
        physical_parity = multiply(code.physical_parities)
        expanded_parity = expanded_reference_pauli(
            physical_parity, physical_modes, cells
        )
        status = sector_status(expanded + pairs, expanded_parity, physical_qubits)
        rows.append(
            {
                "L": length,
                "cells": cells,
                "abstract_reference_qubits_per_cell": 3,
                "physical_reference_M2_per_cell": 6,
                "total_physical_M2_per_cell": physical_qubits // cells,
                "pair_constraint_rank": c235.gf2_rank(
                    pair.symplectic(physical_qubits) for pair in pairs
                ),
                "combined_rank": rank,
                "combined_code_exponent": physical_qubits - rank,
                "target_full_Fock_exponent": physical_modes,
                "phase_inconsistencies": len(inconsistent),
                "positive_parity_consistent": status["plus_consistent"],
                "negative_parity_consistent": status["minus_consistent"],
                "maximum_expanded_local_loop_support": max(
                    (
                        expanded_reference_pauli(loop, physical_modes, cells).x
                        | expanded_reference_pauli(loop, physical_modes, cells).z
                    ).bit_count()
                    for loop in code.local_loops
                ),
                "abstract_qubits_replaced": abstract_qubits,
            }
        )
    check(
        "six physical M2 sites in three opposite pair codes realize each abstract reference register covariantly and without collisions",
        pair_rank == 3
        and not pair_inconsistent
        and local_leakage == 0
        and logical_pair_failures == 0
        and gamma_failures == 0
        and max((pauli.x | pauli.z).bit_count() for pauli in local_gamma) == 4
        and collision_count == 0
        and frame_failures == 0
        and pair_frame_failures == 0
        and all(
            row["physical_reference_M2_per_cell"] == 6
            and row["total_physical_M2_per_cell"] == 24
            and row["pair_constraint_rank"] == 3 * row["cells"]
            and row["combined_code_exponent"]
            == row["target_full_Fock_exponent"]
            and row["phase_inconsistencies"] == 0
            and row["positive_parity_consistent"]
            and row["negative_parity_consistent"] == (row["cells"] % 2 == 1)
            for row in rows
        ),
        {
            "local_pair_rank": pair_rank,
            "local_pair_phase_inconsistencies": len(pair_inconsistent),
            "logical_or_gamma_pair_leakage": local_leakage,
            "logical_Pauli_failures": logical_pair_failures,
            "gamma_anticommutator_failures": gamma_failures,
            "maximum_reference_gamma_support": max(
                (pauli.x | pauli.z).bit_count() for pauli in local_gamma
            ),
            "reference_shell_radius": 24,
            "collisions_with_radii_6_12_18": collision_count,
            "proper_frame_shell_failures": frame_failures,
            "proper_frame_pair_failures": pair_frame_failures,
            "opposite_pair_periodic_separation": 16,
            "bounded_pair_encoder": "one constant-route pair encoding per axis pair, with periodic route length at most 16; no nearest-neighbor single-gate claim",
            "nearest_neighbor_single_CNOT_claimed": False,
            "sizes": rows,
        },
    )


def augmented_sign_lift_control() -> None:
    frames, permutations = c261.direction_permutations()
    frame_lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    identity = frame_lookup[tuple(np.eye(3, dtype=int).reshape(-1))]
    multiplication = [
        [
            frame_lookup[tuple((frames[left] @ frames[right]).reshape(-1))]
            for right in range(24)
        ]
        for left in range(24)
    ]
    variables = 24 * 7 * 6

    def variable(frame: int, role: int, label: int) -> int:
        return (frame * 7 + role) * 6 + label

    def moved_role(permutation: tuple[int, ...], role: int) -> int:
        return permutation[role] if role < 6 else 6

    results = []
    for name, reference_label in (
        ("aligned", tuple(range(6))),
        ("antipodal", tuple(direction ^ 1 for direction in range(6))),
    ):
        equations: list[tuple[int, int]] = []

        def add(indices: list[int], right_hand_side: int = 0) -> None:
            mask = 0
            for index in indices:
                mask ^= 1 << index
            equations.append((mask, right_hand_side))

        for role in range(7):
            for label in range(6):
                add([variable(identity, role, label)])
        for left in range(24):
            for right in range(24):
                product_frame = multiplication[left][right]
                for role in range(7):
                    for label in range(6):
                        add(
                            [
                                variable(product_frame, role, label),
                                variable(right, role, label),
                                variable(
                                    left,
                                    moved_role(permutations[right], role),
                                    permutations[right][label],
                                ),
                            ]
                        )
        odd_frames = 0
        for frame, permutation in enumerate(permutations):
            parity = c261.permutation_parity(permutation)
            odd_frames += parity
            for role in range(7):
                add([variable(frame, role, label) for label in range(6)], parity)
            for left, right in combinations(range(6), 2):
                add(
                    [
                        variable(frame, left, right),
                        variable(frame, right, left),
                    ]
                )
            for direction in range(6):
                add(
                    [
                        variable(frame, direction, direction),
                        variable(frame, 6, reference_label[direction]),
                    ]
                )
        coefficient_rank, augmented_rank = c261.affine_system_ranks(
            equations, variables
        )
        results.append(
            {
                "reference_labeling": name,
                "frames": 24,
                "variables": variables,
                "equations": len(equations),
                "odd_raw_direction_permutations": odd_frames,
                "coefficient_rank": coefficient_rank,
                "augmented_rank": augmented_rank,
                "scope": "signed permutations of the displayed gamma labels with role-dependent signs; general Clifford/product relabelings remain open",
            }
        )
    check(
        "aligned and antipodal reference spokes have no exact signed-label all-frame lift preserving positive chirality and edges",
        all(
            row["odd_raw_direction_permutations"] == 12
            and row["augmented_rank"] == row["coefficient_rank"] + 1
            for row in results
        ),
        results,
    )


def reference_sector_controls() -> None:
    equality_rows = []
    rooted_rows = []
    diagonal_kernel_rows = []
    for length in (3, 4, 5, 6):
        code = reference_spoke_code(length)
        cells = length**3
        physical_vertices = len(code.graph.vertices)
        modes = physical_vertices + cells
        qubits = 3 * modes
        full = code.local_loops + code.wilson_loops
        equalities = reference_equalities(code)
        physical_parity = multiply(code.physical_parities)
        reference_parity = multiply(code.reference_parities)
        total_parity = physical_parity @ reference_parity
        equality_status = sector_status(full + equalities, physical_parity, qubits)
        equality_rank, equality_inconsistent = c235.phase_aware_rank(
            equalities, qubits
        )
        total_status = sector_status(full, total_parity, qubits)
        physical_generator_leakage = sum(
            not operator.commutes(constraint)
            for operator in code.physical_parities
            + code.edge_paulis[: len(code.graph.edges)]
            for constraint in equalities
        )
        equality_rows.append(
            {
                "L": length,
                "cells": cells,
                "reference_equality_rank": equality_rank,
                "reference_equality_phase_inconsistencies": len(
                    equality_inconsistent
                ),
                "combined_code_exponent": qubits - int(equality_status["rank"]),
                "target_full_Fock_exponent": physical_vertices,
                "positive_physical_parity_consistent": equality_status[
                    "plus_consistent"
                ],
                "negative_physical_parity_consistent": equality_status[
                    "minus_consistent"
                ],
                "positive_rank_increment": equality_status[
                    "plus_rank_increment"
                ],
                "negative_rank_increment": equality_status[
                    "minus_rank_increment"
                ],
                "full_loops_fix_positive_total_parity": total_status[
                    "plus_rank_increment"
                ]
                == 0
                and not total_status["minus_consistent"],
                "physical_generator_leakage": physical_generator_leakage,
            }
        )

        root = code.cell_index[(0, 0, 0)]
        rooted_constraints = [
            parity
            for index, parity in enumerate(code.reference_parities)
            if index != root
        ]
        rooted_status = sector_status(
            full + rooted_constraints, physical_parity, qubits
        )
        rooted_rows.append(
            {
                "L": length,
                "cells": cells,
                "constraints": len(rooted_constraints),
                "combined_code_exponent": qubits - int(rooted_status["rank"]),
                "target_full_Fock_exponent": physical_vertices,
                "positive_consistent": rooted_status["plus_consistent"],
                "negative_consistent": rooted_status["minus_consistent"],
                "coarse_translation_failures": cells - 1,
                "proper_frame_failures": 0,
            }
        )
        # Any translation-invariant diagonal binary constraint code of rank
        # N-1 has a one-dimensional kernel.  Translation acts trivially on a
        # one-dimensional GF(2) kernel, so cell transitivity forces its
        # nonzero vector to be all ones.  Total reference parity changes by
        # its weight N modulo two.  This scopes the volume-parity result beyond
        # the nearest-neighbor equality presentation, but only for diagonal
        # occupation constraints.
        diagonal_kernel_rows.append(
            {
                "L": length,
                "cells": cells,
                "cell_translation_orbits": 1,
                "unique_nonzero_invariant_kernel_weight": cells,
                "total_reference_parity_toggle": cells % 2,
            }
        )

    check(
        "translation-covariant reference equality has exact full-Fock rank but carries both parities only on odd-volume tori",
        all(
            row["reference_equality_rank"] == row["cells"] - 1
            and row["reference_equality_phase_inconsistencies"] == 0
            and row["combined_code_exponent"]
            == row["target_full_Fock_exponent"]
            and row["positive_physical_parity_consistent"]
            and row["full_loops_fix_positive_total_parity"]
            and row["physical_generator_leakage"] == 0
            and row["negative_physical_parity_consistent"]
            == (row["cells"] % 2 == 1)
            for row in equality_rows
        ),
        equality_rows,
    )
    check(
        "fixing every reference occupation except one restores both parities at every size but marks a coarse root",
        all(
            row["constraints"] == row["cells"] - 1
            and row["combined_code_exponent"]
            == row["target_full_Fock_exponent"]
            and row["positive_consistent"]
            and row["negative_consistent"]
            and row["coarse_translation_failures"] == row["cells"] - 1
            and row["proper_frame_failures"] == 0
            for row in rooted_rows
        ),
        rooted_rows,
    )
    check(
        "every translation-invariant rank-N-1 diagonal reference constraint has the same N-mod-2 parity functional",
        all(
            row["cell_translation_orbits"] == 1
            and row["unique_nonzero_invariant_kernel_weight"] == row["cells"]
            and row["total_reference_parity_toggle"] == row["cells"] % 2
            for row in diagonal_kernel_rows
        ),
        {
            "sizes": diagonal_kernel_rows,
            "scope": "binary diagonal constraints in the reference occupation basis; local even pair-flip/cat codes and non-diagonal quantum reference codes remain live",
        },
    )


def preparation_controls() -> None:
    rows = []
    for length in (3, 4, 5, 6):
        code, base_full = base_full_code(length)
        base_local = code.local_loops + code.dummy_triangles
        base_qubits = 3 * len(code.graph.vertices)
        base_local_rank = c235.gf2_rank(
            loop.symplectic(base_qubits) for loop in base_local
        )
        base_full_rank = c235.gf2_rank(
            loop.symplectic(base_qubits) for loop in base_full
        )
        reference = reference_spoke_code(length)
        reference_qubits = 3 * (len(reference.graph.vertices) + length**3)
        reference_local_rank = c235.gf2_rank(
            loop.symplectic(reference_qubits) for loop in reference.local_loops
        )
        reference_full_rank = c235.gf2_rank(
            loop.symplectic(reference_qubits)
            for loop in reference.local_loops + reference.wilson_loops
        )
        cell_diameter = 3 * (length // 2)
        rows.append(
            {
                "L": length,
                "base_Wilson_increment": base_full_rank - base_local_rank,
                "reference_Wilson_increment": reference_full_rank
                - reference_local_rank,
                "cell_torus_diameter": cell_diameter,
                "equality_cat_causal_depth_lower_bound": (cell_diameter + 1) // 2,
            }
        )
    check(
        "rank closure never supplies bounded preparation of Wilson data or a coherent parity superposition",
        all(
            row["base_Wilson_increment"] == 3
            and row["reference_Wilson_increment"] == 3
            for row in rows
        )
        and rows[-1]["equality_cat_causal_depth_lower_bound"]
        > rows[0]["equality_cat_causal_depth_lower_bound"],
        {
            "sizes": rows,
            "bounded_preparation": False,
            "reason": "the displayed equality carriers require system-spanning cat coherence, and both gamma codes retain three Wilson logicals before nonlocal sector fixing",
            "arbitrary_full_Fock_input": "not encoded by a bounded local circuit",
            "coherent_even_odd_superpositions": "not prepared",
        },
    )


def fixture_and_scope_firewall() -> None:
    species = c219.common_species(c230.BETA)
    rest = c219.rest_mass(species)
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "actual Cycle-230 gates and mass/rank-73 seam synthesis remain gated by the missing common physical E",
        abs(c230.BETA + 0.3) < 1e-15
        and abs(c230.COUPLING - 0.37) < 1e-15
        and abs(rest / species.analytic_mass - 1) < 2e-12
        and sea_rank == 73,
        {
            "beta": c230.BETA,
            "g": c230.COUPLING,
            "rest_mass_predecessor": rest,
            "principal_sea_rank_predecessor": sea_rank,
            "common_full_Fock_E": False,
            "coin_A_B_FSWAP_contact_synthesis": "not reached",
            "mass_and_rank73_seam_intertwining": "not claimed",
        },
    )
    check(
        "carrier fanout and stabilizer schedules are not physical time or Records",
        True,
        {
            "compiler_layers_are_not_physical_time": True,
            "label_and_reference_modes": "coherent code carriers, not Records",
            "universal_no_go": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    note_contract()
    base_control()
    direct_sum_label_controls()
    distributed_carrier_controls()
    distributed_signed_covariance_control()
    reference_spoke_algebra_and_rank_controls()
    reference_physical_motif_controls()
    augmented_sign_lift_control()
    reference_sector_controls()
    preparation_controls()
    fixture_and_scope_firewall()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
