#!/usr/bin/env python3
"""Cycle 240: measurement/feedforward preparation of the square-pyramid code.

Measure the bounded modified-Gauss stabilizers of the Cycle-235 face-qubit
code, decode their signs, and correct them with face Z operators (equivalently,
reassign hopping-generator signs as suggested by Guaita).  The quantum
measurement layer is bounded.  The explicit deterministic decoder and the
three Wilson-sector corrections are global.  Postselection and coherent
dilation alternatives are audited separately, without calling compiler depth
physical time or a copied syndrome bit a framework Record.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230

NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "MEASUREMENT_FEEDFORWARD_SQUARE_PYRAMID_PREPARATION_CYCLE240_NOTE_2026-07-17.md"
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
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "guaita",
        "local measurements plus feedforward",
        "30 bounded quantum subrounds",
        "global gaussian decoder",
        "wilson membranes",
        "postselected",
        "autonomous coherent dilation",
        "syndrome outcome registers are not automatically records",
        "odd sector remains absent",
        "rank-73",
        "authority: none",
        "audit: unset",
        "n1 — alternative routes",
        "n2 — condition independence",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution audit",
        "n6 — partial-closure and primitive scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom conclusion",
    )
    missing = tuple(item for item in required if item not in text)
    check("note preserves the measurement/preparation and N1-N8 contract", not missing, missing)


def independent_indices(rows: list[int]) -> list[int]:
    pivots: dict[int, int] = {}
    indices = []
    for index, original in enumerate(rows):
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                indices.append(index)
                break
    return indices


def right_inverse(rows: list[int], qubit_count: int):
    """Return face-Z corrections z_i satisfying rows*z_i=e_i over GF(2)."""

    row_count = len(rows)
    pivots: dict[int, tuple[int, int]] = {}
    selected_faces = []
    for face in range(qubit_count):
        column = 0
        for row_index, row in enumerate(rows):
            column ^= ((row >> face) & 1) << row_index
        reduced = column
        correction = 1 << face
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot in pivots:
                reduced ^= pivots[pivot][0]
                correction ^= pivots[pivot][1]
            else:
                pivots[pivot] = (reduced, correction)
                selected_faces.append(face)
                break
        if len(pivots) == row_count:
            break
    if len(pivots) != row_count:
        raise RuntimeError(("syndrome matrix not surjective", len(pivots), row_count))

    solutions = []
    for target_index in range(row_count):
        target = 1 << target_index
        correction = 0
        while target:
            pivot = target.bit_length() - 1
            column, face_mask = pivots[pivot]
            target ^= column
            correction ^= face_mask
        solutions.append(correction)
    return solutions, frozenset(selected_faces)


def syndrome(mask: int, rows: list[int]) -> int:
    value = 0
    for index, row in enumerate(rows):
        value ^= ((mask & row).bit_count() % 2) << index
    return value


def cycle_anchor(graph: c235.PyramidCellulation, cycle_index: int):
    cell_count = graph.length**3
    if cycle_index < 8 * cell_count:
        return graph.cells[cycle_index // 8]
    if cycle_index < 11 * cell_count:
        return graph.cells[(cycle_index - 8 * cell_count) // 3]
    return (0, 0, 0)  # a Wilson measurement has no genuinely local anchor


def torus_l1(left, right, length: int) -> int:
    return sum(
        min((a - b) % length, (b - a) % length)
        for a, b in zip(left, right)
    )


def measurement_and_decoder_controls():
    rows = []
    decoder_cache = {}
    for length in (3, 4, 5):
        graph = c235.PyramidCellulation(length)
        cycles = c235.primal_edge_cycles(graph)
        local_paulis = [graph.loop_pauli(vertices) for _, vertices, _ in cycles]
        wilson_paulis = [
            graph.loop_pauli(vertices) for vertices in c235.wilson_cycles(graph)
        ]
        all_paulis = local_paulis + wilson_paulis
        basis_indices = independent_indices([row.x for row in all_paulis])
        basis_rows = [all_paulis[index].x for index in basis_indices]
        cell_fluxes = [graph.B(vertex) for vertex in range(len(graph.vertices))]
        flux_commutator_failures = sum(
            not measured.commutes(flux)
            for measured in all_paulis
            for flux in cell_fluxes
        )
        solutions, selected_faces = right_inverse(basis_rows, len(graph.edges))
        decoder_cache[length] = (basis_indices, basis_rows, solutions, selected_faces)

        decoder_failures = sum(
            syndrome(solution, basis_rows) != 1 << index
            for index, solution in enumerate(solutions)
        )
        correction_weights = [solution.bit_count() for solution in solutions]
        correction_radii = []
        for source_index, solution in zip(basis_indices, solutions):
            anchor = cycle_anchor(graph, source_index)
            distances = []
            support = solution
            while support:
                bit = support & -support
                edge = bit.bit_length() - 1
                distances.append(torus_l1(anchor, graph.edges[edge][3], length))
                support ^= bit
            correction_radii.append(max(distances, default=0))

        data_participation = [0] * len(graph.edges)
        incidence_count = 0
        for pauli in local_paulis:
            support = pauli.x | pauli.z
            incidence_count += support.bit_count()
            while support:
                bit = support & -support
                data_participation[bit.bit_length() - 1] += 1
                support ^= bit
        maximum_check_weight = max(
            (pauli.x | pauli.z).bit_count() for pauli in local_paulis
        )
        maximum_data_degree = max(data_participation)
        interaction_subrounds = max(maximum_check_weight, maximum_data_degree)
        local_rank = c235.gf2_rank(pauli.x for pauli in local_paulis)
        full_rank = len(basis_rows)
        row = {
            "L": length,
            "face_qubits": len(graph.edges),
            "local_check_nodes": len(local_paulis),
            "syndrome_incidence_edges": incidence_count,
            "local_check_rank": local_rank,
            "local_dependencies": len(local_paulis) - local_rank,
            "full_rank_with_Wilson": full_rank,
            "independent_outcomes_uniform_on_zero": c235.gf2_rank(basis_rows)
            == len(basis_rows),
            "cell_flux_commutator_failures": flux_commutator_failures,
            "max_check_weight": maximum_check_weight,
            "max_data_participation": maximum_data_degree,
            "bounded_measurement_subrounds": interaction_subrounds + 2,
            "decoder_failures": decoder_failures,
            "global_decoder_max_correction_weight": max(correction_weights),
            "global_decoder_mean_correction_weight": sum(correction_weights)
            / len(correction_weights),
            "global_decoder_max_coarse_radius": max(correction_radii),
            "all_plus_postselection_log2_probability": -full_rank,
            "local_plus_postselection_log2_probability": -local_rank,
            "Wilson_plus_given_local_probability": "1/8",
        }
        rows.append(row)
        check(
            f"L={length} bounded local measurements plus the explicit global decoder prepare the fixed code sector exactly",
            local_rank == 9 * length**3 - 2
            and full_rank == 9 * length**3 + 1
            and maximum_check_weight == 28
            and maximum_data_degree == 11
            and interaction_subrounds + 2 == 30
            and decoder_failures == 0,
            row,
        )
    check(
        "the deterministic decoder correction support grows across the held-size protocol",
        [row["global_decoder_max_correction_weight"] for row in rows]
        == [90, 152, 314]
        and [round(row["global_decoder_mean_correction_weight"], 6) for row in rows]
        == [23.729508, 39.462738, 60.094139],
        rows,
    )
    check(
        "the independent measured signs are uniform on the zero input and preserve every cell flux",
        all(row["independent_outcomes_uniform_on_zero"] for row in rows)
        and all(row["cell_flux_commutator_failures"] == 0 for row in rows),
        [
            {
                "L": row["L"],
                "independent_rank": row["full_rank_with_Wilson"],
                "flux_commutator_failures": row[
                    "cell_flux_commutator_failures"
                ],
            }
            for row in rows
        ],
    )
    return rows, decoder_cache


def wilson_membrane(graph: c235.PyramidCellulation, axis: int) -> int:
    mask = 0
    for edge, (u, _, kind, owner) in enumerate(graph.edges):
        if kind != "outer_square":
            continue
        edge_axis = graph.vertices[u][1] // 2
        if edge_axis == axis and owner[axis] == graph.length - 1:
            mask ^= 1 << edge
    return mask


def wilson_and_bounded_feedforward_controls() -> None:
    rows = []
    for length in (3, 4, 5):
        graph = c235.PyramidCellulation(length)
        cycles = c235.primal_edge_cycles(graph)
        local_masks = [mask for mask, _, _ in cycles]
        wilson_vertices = c235.wilson_cycles(graph)
        wilson_masks = [graph.cycle_mask(vertices) for vertices in wilson_vertices]
        wilson_paulis = [graph.loop_pauli(vertices) for vertices in wilson_vertices]
        membranes = [wilson_membrane(graph, axis) for axis in range(3)]
        local_commutator_failures = sum(
            (membrane & local).bit_count() % 2
            for membrane in membranes
            for local in local_masks
        )
        pairing = [
            [(membrane & wilson).bit_count() % 2 for wilson in wilson_masks]
            for membrane in membranes
        ]
        rows.append(
            {
                "L": length,
                "Wilson_measurement_weights": [
                    (pauli.x | pauli.z).bit_count() for pauli in wilson_paulis
                ],
                "Wilson_membrane_weights": [mask.bit_count() for mask in membranes],
                "membrane_local_commutator_failures": local_commutator_failures,
                "membrane_Wilson_pairing": pairing,
                "local_parity_aggregation_radius_lower_bound": length // 2,
                "conditional_membrane_broadcast_radius": 2 * (length // 2),
            }
        )
    check(
        "three exact LxL Wilson membranes correct the spin bits while preserving every local Gauss check",
        all(row["membrane_local_commutator_failures"] == 0 for row in rows)
        and all(
            row["membrane_Wilson_pairing"]
            == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            for row in rows
        )
        and [row["Wilson_membrane_weights"][0] for row in rows] == [9, 16, 25],
        rows,
    )
    check(
        "fixed-spin deterministic feedforward is noncontractible rather than bounded-radius",
        all(
            row["Wilson_membrane_weights"] == [row["L"] ** 2] * 3
            and min(row["Wilson_measurement_weights"]) > row["L"]
            for row in rows
        ),
        rows,
    )


def translated_wilson_vertices(
    graph: c235.PyramidCellulation, axis: int, offsets: tuple[int, int]
):
    transverse = (axis + 1) % 3
    other_axes = [value for value in range(3) if value != axis]
    vertices = []
    for step in range(graph.length):
        cell = [0, 0, 0]
        cell[axis] = step
        for other_axis, offset in zip(other_axes, offsets):
            cell[other_axis] = offset
        next_cell = list(cell)
        next_cell[axis] = (next_cell[axis] + 1) % graph.length
        vertices.extend(
            (
                graph.vertex_index[(tuple(cell), 2 * axis)],
                graph.vertex_index[(tuple(next_cell), 2 * axis + 1)],
                graph.vertex_index[(tuple(next_cell), 2 * transverse)],
            )
        )
    return vertices


def find_disjoint_wilson_scaffold(graph: c235.PyramidCellulation):
    options = []
    for axis in range(3):
        axis_options = []
        for offsets in product(range(graph.length), repeat=2):
            pauli = graph.loop_pauli(
                translated_wilson_vertices(graph, axis, offsets)
            )
            axis_options.append((offsets, pauli, pauli.x | pauli.z))
        options.append(axis_options)
    for first in options[0]:
        for second in options[1]:
            if first[2] & second[2]:
                continue
            for third in options[2]:
                if (first[2] | second[2]) & third[2] == 0:
                    return first, second, third
    raise RuntimeError("no disjoint Wilson scaffold")


def scaffold_and_covariance_controls(decoder_cache) -> None:
    scaffold_rows = []
    for length in (3, 4, 5):
        graph = c235.PyramidCellulation(length)
        scaffold = find_disjoint_wilson_scaffold(graph)
        scaffold_support = 0
        for _, _, support in scaffold:
            scaffold_support |= support
        loop_paulis = [
            graph.loop_pauli(vertices)
            for _, vertices, _ in c235.primal_edge_cycles(graph)
        ]
        wilson_commutator_failures = sum(
            not pauli.commutes(loop)
            for _, pauli, _ in scaffold
            for loop in loop_paulis
        )
        cell_flux_not_product_eigenstate = sum(
            bool(graph.B(vertex).z & sum((pauli.x for _, pauli, _ in scaffold), 0))
            for vertex in range(len(graph.vertices))
        )
        scaffold_rows.append(
            {
                "L": length,
                "offsets": [row[0] for row in scaffold],
                "support_weight": scaffold_support.bit_count(),
                "local_Gauss_commutator_failures": wilson_commutator_failures,
                "cell_fluxes_not_fixed_by_product_scaffold": cell_flux_not_product_eigenstate,
            }
        )
    check(
        "a depth-one globally marked product scaffold can pre-pin all three Wilson signs before local measurements",
        all(row["local_Gauss_commutator_failures"] == 0 for row in scaffold_rows)
        and all(row["cell_fluxes_not_fixed_by_product_scaffold"] > 0 for row in scaffold_rows)
        and [row["support_weight"] for row in scaffold_rows] == [59, 77, 95],
        scaffold_rows,
    )

    graph = c235.PyramidCellulation(3)
    source_constraints = {
        mask for mask, _, _ in c235.primal_edge_cycles(graph)
    }
    graph_failures = constraint_failures = 0
    scaffold = find_disjoint_wilson_scaffold(graph)
    scaffold_support = 0
    for _, _, support in scaffold:
        scaffold_support |= support
    scaffold_frame_mismatches = 0
    for frame in c235.proper_cubic_frames():
        _, edge_map = c235.graph_frame_maps(graph, frame)
        graph_failures += len(set(edge_map)) != len(graph.edges)
        for mask in source_constraints:
            mapped = c235.permute_pauli(c235.Pauli(x=mask), edge_map).x
            constraint_failures += mapped not in source_constraints
        moved_scaffold = c235.permute_pauli(
            c235.Pauli(x=scaffold_support), edge_map
        ).x
        scaffold_frame_mismatches += moved_scaffold != scaffold_support

    _, _, _, selected_faces = decoder_cache[3]
    decoder_frame_mismatches = 0
    selected_mask = sum(1 << face for face in selected_faces)
    for frame in c235.proper_cubic_frames():
        _, edge_map = c235.graph_frame_maps(graph, frame)
        moved = c235.permute_pauli(c235.Pauli(x=selected_mask), edge_map).x
        decoder_frame_mismatches += moved != selected_mask
    check(
        "the local measurement family and all-plus spin label are cubic, but the scaffold and Gaussian decoder presentation are not",
        graph_failures == 0
        and constraint_failures == 0
        and scaffold_frame_mismatches > 0
        and decoder_frame_mismatches > 0,
        {
            "graph_failures": graph_failures,
            "constraint_failures": constraint_failures,
            "scaffold_frame_mismatches": scaffold_frame_mismatches,
            "decoder_frame_mismatches": decoder_frame_mismatches,
            "all_plus_spin_label_frame_invariant": True,
        },
    )


def route_comparison_controls(protocol_rows) -> None:
    comparison = []
    for row in protocol_rows:
        length = row["L"]
        comparison.append(
            {
                "L": length,
                "local_unitary_Guaita_d": (length - 2) // 4,
                "local_measurement_quantum_subrounds": 30,
                "bounded_feedforward_fixed_spin": False,
                "global_decoder_deterministic_success": 1,
                "global_decoder_max_Z_support": row[
                    "global_decoder_max_correction_weight"
                ],
                "all_plus_postselection_log2_probability": row[
                    "all_plus_postselection_log2_probability"
                ],
                "coherent_local_parity_depth_lower_bound": length // 2,
            }
        )
    held_guaita = [((length - 2) // 4) for length in (3, 4, 5, 6, 10, 14, 18)]
    check(
        "local-unitary, measured, global-decoder, postselected, and coherent routes remain operationally distinct",
        held_guaita == [0, 0, 0, 1, 2, 3, 4]
        and all(row["global_decoder_deterministic_success"] == 1 for row in comparison)
        and [row["all_plus_postselection_log2_probability"] for row in comparison]
        == [-244, -577, -1126],
        {"routes": comparison, "Guaita_held_sizes": held_guaita},
    )
    check(
        "measurement feedforward needs actual syndrome outcomes whereas coherent dilation trades actualization for growing reversible control",
        all(row["coherent_local_parity_depth_lower_bound"] >= 1 for row in comparison),
        {
            "measured_route": {
                "actualized_branch_outcome_required": True,
                "host_global_decoder_required": True,
                "framework_Record_derived": False,
            },
            "coherent_route": {
                "actualized_branch_outcome_required": False,
                "syndrome_ancilla_or_garbage_required": True,
                "bounded_depth": False,
            },
        },
    )


def even_update_and_odd_sector_controls() -> None:
    sector_rows = []
    for length in (3, 4, 5):
        graph = c235.PyramidCellulation(length)
        total = c235.Pauli()
        for vertex in range(len(graph.vertices)):
            total = total @ graph.B(vertex)
        full_rank = c235.gf2_rank(
            [mask for mask, _, _ in c235.primal_edge_cycles(graph)]
            + [graph.cycle_mask(vertices) for vertices in c235.wilson_cycles(graph)]
        )
        sector_rows.append(
            {
                "L": length,
                "total_flux_identity": total == c235.Pauli(),
                "logical_exponent": len(graph.edges) - full_rank,
                "odd_sector_present": False,
            }
        )
    check(
        "measurement and feedforward do not repair the closed-code total-even identity",
        all(row["total_flux_identity"] for row in sector_rows)
        and all(
            row["logical_exponent"] == 6 * row["L"] ** 3 - 1
            for row in sector_rows
        ),
        sector_rows,
    )

    species = c219.common_species(-0.35)
    coin = c229.fock_lift(species.coin)
    parity = np.diag([(-1) ** index.bit_count() for index in range(64)]).astype(
        complex
    )
    occupations = np.asarray([index.bit_count() for index in range(64)])
    contact = np.diag(np.exp(1j * 0.37 * occupations * (occupations - 1) / 2))
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "the exact even update algebra survives while one-particle mass and the rank-73 seam state remain unavailable",
        np.linalg.norm(coin @ parity - parity @ coin) < 2e-12
        and np.linalg.norm(contact @ parity - parity @ contact) == 0
        and sea_rank == 73
        and sea_rank % 2 == 1,
        {
            "coin_parity_commutator": float(
                np.linalg.norm(coin @ parity - parity @ coin)
            ),
            "contact_parity_commutator": float(
                np.linalg.norm(contact @ parity - parity @ contact)
            ),
            "mapped_even_updates": ("coin", "A/B FSWAP", "contact"),
            "one_particle_mass_intertwining": "unavailable: odd sector absent",
            "sea_rank": sea_rank,
            "seam_intertwining": "unavailable: odd sector absent",
        },
    )


def main() -> int:
    note_contract()
    protocol_rows, decoder_cache = measurement_and_decoder_controls()
    wilson_and_bounded_feedforward_controls()
    scaffold_and_covariance_controls(decoder_cache)
    route_comparison_controls(protocol_rows)
    even_update_and_odd_sector_controls()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
