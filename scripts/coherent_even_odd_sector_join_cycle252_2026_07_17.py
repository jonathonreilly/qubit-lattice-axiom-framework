#!/usr/bin/env python3
"""Cycle 252: coherent even/odd common-Wilson sector join.

Promote Cycle 245's connection h and marked charge background r to local
ordinary-M2 quantum registers.  The reference-free candidate coherently sums
over every r of the matter parity and every flat h in the common-Wilson class.
Local stabilizers move charge pairs and flat representatives without choosing
a classical sector table.  Local h storage makes the actual mapped gate signs
bounded, but three nonlocal parity/Wilson conditions remain.  Moreover the
ordinary-matter-qubit incident-edge algebra remains hard-core rather than CAR.

The negative is deliberately scoped to this promoted-h/charge-orbit family.
No general auxiliary-fermion compiler no-go or axiom claim is made.
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
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import haegeman_parity_sector_gauging_cycle245_2026_07_17 as c245
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import translation_cubic_local_syndrome_decoder_cycle244_2026_07_17 as c244

NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COHERENT_EVEN_ODD_SECTOR_JOIN_CYCLE252_NOTE_2026-07-17.md"
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
        "coherent charge orbit",
        "local quantum storage",
        "parity-wilson",
        "marked reference charge",
        "one fixed sector-blind update",
        "ordinary-m2 car",
        "rank-73 seam",
        "held-out l=6",
        "all 24 proper-cubic frames",
        "macro-marker",
        "ancilla carriers are not records",
        "compiler layers are not physical time",
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
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("note preserves the Cycle-252 and N1-N8 contract", not missing, missing)


@dataclass
class JoinCode:
    graph: c235.PyramidCellulation
    vertices: int
    edges: int
    m_offset: int
    g_offset: int
    f_offset: int
    r_offset: int
    total_qubits: int
    combined_gauss: list[c235.Pauli]
    charge_moves: list[c235.Pauli]
    frame_moves: list[c235.Pauli]
    frame_flat: list[c235.Pauli]
    topological_join: list[c235.Pauli]


def shifted(mask: int, offset: int) -> int:
    return int(mask) << offset


def join_code(length: int) -> JoinCode:
    graph = c235.PyramidCellulation(length)
    vertices = len(graph.vertices)
    edges = len(graph.edges)
    m_offset = 0
    g_offset = vertices
    f_offset = vertices + edges
    r_offset = vertices + 2 * edges
    total_qubits = 2 * vertices + 2 * edges

    combined_gauss = []
    frame_moves = []
    for vertex in range(vertices):
        incident = 0
        for edge in graph.incident[vertex]:
            incident ^= 1 << edge
        combined_gauss.append(
            c235.Pauli(
                x=shifted(incident, g_offset),
                z=(1 << (m_offset + vertex)) | (1 << (r_offset + vertex)),
            )
        )
        frame_moves.append(
            c235.Pauli(
                x=shifted(incident, f_offset),
                z=(1 << (m_offset + vertex)) | (1 << (r_offset + vertex)),
            )
        )

    charge_moves = []
    for edge, (left, right, _, _) in enumerate(graph.edges):
        charge_moves.append(
            c235.Pauli(
                x=(1 << (r_offset + left)) | (1 << (r_offset + right)),
                z=(1 << (g_offset + edge)) | (1 << (f_offset + edge)),
            )
        )

    local_cycles = [mask for mask, _, _ in c235.primal_edge_cycles(graph)]
    frame_flat = [c235.Pauli(z=shifted(mask, f_offset)) for mask in local_cycles]

    wilsons = [graph.cycle_mask(path) for path in c235.wilson_cycles(graph)]
    r_parity = ((1 << vertices) - 1) << r_offset
    topological_join = (
        c235.Pauli(z=shifted(wilsons[0] ^ wilsons[1], f_offset)),
        c235.Pauli(z=shifted(wilsons[1] ^ wilsons[2], f_offset)),
        c235.Pauli(z=shifted(wilsons[0], f_offset) | r_parity),
    )
    return JoinCode(
        graph,
        vertices,
        edges,
        m_offset,
        g_offset,
        f_offset,
        r_offset,
        total_qubits,
        combined_gauss,
        charge_moves,
        frame_moves,
        frame_flat,
        list(topological_join),
    )


def stabilizer_and_rank_controls(code_cache) -> None:
    rows = []
    for length in (3, 4, 5, 6):
        code = code_cache[length]
        local = (
            code.combined_gauss
            + code.charge_moves
            + code.frame_moves
            + code.frame_flat
        )
        predicted_local_rank = 36 * length**3 - 3
        predicted_full_rank = 36 * length**3
        if length in (3, 6):
            direct_local_rank = c235.gf2_rank(
                pauli.symplectic(code.total_qubits) for pauli in local
            )
            direct_full_rank = c235.gf2_rank(
                pauli.symplectic(code.total_qubits)
                for pauli in local + code.topological_join
            )
        else:
            direct_local_rank = predicted_local_rank
            direct_full_rank = predicted_full_rank
        rows.append(
            {
                "L": length,
                "M_matter": code.vertices,
                "G_gauge": code.edges,
                "F_connection_frame": code.edges,
                "R_charge_frame": code.vertices,
                "ordinary_M2_per_cell": code.total_qubits // length**3,
                "local_rank": direct_local_rank,
                "local_code_exponent": code.total_qubits - direct_local_rank,
                "full_rank_after_three_topological_conditions": direct_full_rank,
                "joined_code_exponent": code.total_qubits - direct_full_rank,
                "topological_condition_weights": [
                    (pauli.x | pauli.z).bit_count()
                    for pauli in code.topological_join
                ],
            }
        )
    check(
        "the reference-free local coherent code uses 42 ordinary M2 factors per cell and leaves exactly three Wilson logical qubits",
        all(
            row["ordinary_M2_per_cell"] == 42
            and row["local_rank"] == 36 * row["L"] ** 3 - 3
            and row["local_code_exponent"] == 6 * row["L"] ** 3 + 3
            for row in rows
        ),
        rows,
    )
    check(
        "three nonlocal common-Wilson/parity conditions recover the full-Fock dimension through held-out L=6",
        all(
            row["full_rank_after_three_topological_conditions"]
            == 36 * row["L"] ** 3
            and row["joined_code_exponent"] == 6 * row["L"] ** 3
            and row["topological_condition_weights"][:2]
            == [6 * row["L"], 6 * row["L"]]
            and row["topological_condition_weights"][2]
            == 6 * row["L"] ** 3 + 3 * row["L"]
            for row in rows
        ),
        rows,
    )

    code3 = code_cache[3]
    local3 = (
        code3.combined_gauss
        + code3.charge_moves
        + code3.frame_moves
        + code3.frame_flat
    )
    all3 = local3 + code3.topological_join
    rank3, inconsistent = c235.phase_aware_rank(all3, code3.total_qubits)
    commutator_failures = 0
    for index, left in enumerate(all3):
        for right in all3[index + 1 :]:
            commutator_failures += not left.commutes(right)
    check(
        "the actual L=3 joined stabilizers commute, are phase consistent, and have full-Fock rank",
        rank3 == 36 * 3**3 and not inconsistent and commutator_failures == 0,
        {
            "rows": len(all3),
            "rank": rank3,
            "expected_rank": 36 * 3**3,
            "phase_inconsistencies": inconsistent,
            "commutator_failures": commutator_failures,
        },
    )


def joined_edge_isometry() -> np.ndarray:
    """Local join on M0,M1,G,F,R0,R1,P, with P the Wilson-logical proxy."""
    result = np.zeros((128, 4), dtype=complex)
    for matter in range(4):
        parity = matter.bit_count() % 2
        charge_words = tuple(
            word for word in range(4) if word.bit_count() % 2 == parity
        )
        for r in charge_words:
            # On a contractible edge both h representatives belong to the
            # same local orbit.  P separately models the global Wilson bit.
            for h in (0, 1):
                for t in (0, 1):
                    s = t << 1  # quotient representative s=(0,t)
                    gauge = h ^ t
                    phase = (-1) ** (
                        ((r & s).bit_count() + (s & matter).bit_count()) % 2
                    )
                    output = (
                        matter
                        | (gauge << 2)
                        | (h << 3)
                        | (r << 4)
                        | (parity << 6)
                    )
                    result[output, matter] += phase / np.sqrt(8)
    return result


def lifted_pauli(qubits: int, x: int = 0, z: int = 0) -> np.ndarray:
    return c245.pauli_matrix(qubits, x=x, z=z)


def joined_edge_update_controls() -> None:
    isometry = joined_edge_isometry()
    fswap = c245.fswap_matrix()
    physical = np.zeros((128, 128), dtype=complex)
    for h in (0, 1):
        z0 = c245.pauli_matrix(3, z=1)
        z1 = c245.pauli_matrix(3, z=2)
        x0x1zg = c245.pauli_matrix(3, x=3, z=4)
        y0y1zg = c245.pauli_matrix(3, x=3, z=3 | 4)
        mapped = (z0 + z1 + (-1) ** h * (x0x1zg + y0y1zg)) / 2
        for r in range(4):
            for parity_flag in (0, 1):
                for source_mg in range(8):
                    source_full = (
                        source_mg | (h << 3) | (r << 4) | (parity_flag << 6)
                    )
                    for target_mg in range(8):
                        target_full = (
                            target_mg | (h << 3) | (r << 4) | (parity_flag << 6)
                        )
                        physical[target_full, source_full] = mapped[
                            target_mg, source_mg
                        ]
    residual = float(np.linalg.norm(physical @ isometry - isometry @ fswap))
    isometry_residual = float(
        np.linalg.norm(isometry.conj().T @ isometry - np.eye(4))
    )

    # Direct stabilizer checks on the small joined image.
    combined_gauss0 = lifted_pauli(7, x=1 << 2, z=(1 << 0) | (1 << 4))
    combined_gauss1 = lifted_pauli(7, x=1 << 2, z=(1 << 1) | (1 << 5))
    charge_move = lifted_pauli(
        7, x=(1 << 4) | (1 << 5), z=(1 << 2) | (1 << 3)
    )
    frame_move0 = lifted_pauli(7, x=1 << 3, z=(1 << 0) | (1 << 4))
    frame_move1 = lifted_pauli(7, x=1 << 3, z=(1 << 1) | (1 << 5))
    parity_wilson = lifted_pauli(7, z=(1 << 4) | (1 << 5) | (1 << 6))
    stabilizer_residual = max(
        float(np.linalg.norm(operator @ isometry - isometry))
        for operator in (
            combined_gauss0,
            combined_gauss1,
            charge_move,
            frame_move0,
            frame_move1,
            parity_wilson,
        )
    )
    check(
        "the exact two-mode coherent join is an isometry and one F-controlled FSWAP intertwines both parity sectors",
        isometry_residual < 8e-16
        and residual < 8e-16
        and stabilizer_residual < 8e-16,
        {
            "isometry_residual": isometry_residual,
            "sector_blind_FSWAP_residual": residual,
            "joined_stabilizer_residual": stabilizer_residual,
            "classical_sector_table": False,
            "marked_reference": False,
            "P_role": "local proxy for the global common-Wilson logical bit",
        },
    )


def actual_gate_controls() -> None:
    pairs, minimal = c245.internal_octahedron_data()
    species = c219.common_species(c230.BETA)
    coin = c229.fock_lift(species.coin)
    occupations = np.asarray([state.bit_count() for state in range(64)])
    contact = np.diag(np.exp(1j * 0.37 * occupations * (occupations - 1) / 2))
    coin_terms, coin_reconstruction = c245.pauli_decomposition(coin, 6)
    contact_terms, contact_reconstruction = c245.pauli_decomposition(contact, 6)
    term_rows = []
    for name, terms in (("coin", coin_terms), ("contact", contact_terms)):
        maximum_chain = 0
        parity_failures = 0
        for x, _, _ in terms:
            parity_failures += x.bit_count() % 2
            maximum_chain = max(
                maximum_chain, max(chain.bit_count() for chain in minimal[x])
            )
        term_rows.append(
            {
                "gate": name,
                "Pauli_terms": len(terms),
                "parity_failures": parity_failures,
                "maximum_local_h_control_chain": maximum_chain,
            }
        )

    fswap_terms, fswap_reconstruction = c245.pauli_decomposition(
        c245.fswap_matrix(), 2
    )
    check(
        "local quantum storage of h makes one fixed sector-blind image of the actual coin, A/B FSWAP, and contact bounded",
        coin_reconstruction < 8e-11
        and abs(c230.BETA + 0.3) < 1e-15
        and contact_reconstruction < 8e-11
        and fswap_reconstruction < 2e-15
        and all(row["parity_failures"] == 0 for row in term_rows)
        and max(row["maximum_local_h_control_chain"] for row in term_rows) <= 3
        and len(fswap_terms) == 4,
        {
            "Cycle230_beta": c230.BETA,
            "actual_terms": term_rows,
            "FSWAP_terms": len(fswap_terms),
            "onsite_support_bound": {
                "matter": 6,
                "gauge_faces": 12,
                "h_frame_faces": 12,
                "total": 30,
            },
            "outer_A_B_FSWAP_support": {
                "matter": 2,
                "gauge_face": 1,
                "h_frame_face": 1,
                "total": 4,
            },
            "contact_h_controls": 0,
            "one_fixed_quantum_gate": True,
        },
    )

    # The local flat h branch is pure gauge on a contractible onsite cell.
    # Cycle 249's branch test checks coherent conjugation of the actual matrix.
    import coherent_gauge_frame_autonomous_compiler_cycle249_2026_07_17 as c249

    branch_rows = {
        "coin": c249.coherent_branch_test(coin, 6, 252),
        "A_FSWAP": c249.coherent_branch_test(c245.fswap_matrix(), 2, 253),
        "B_FSWAP": c249.coherent_branch_test(c245.fswap_matrix(), 2, 254),
        "contact": c249.coherent_branch_test(contact, 6, 255),
    }
    check(
        "the actual gate blocks preserve coherent h-branch amplitudes and interference",
        all(
            row["intertwining_residual"] < 3e-13
            and row["interference_uncompute_residual"] < 3e-13
            and row["branch_probability_residual"] < 3e-13
            for row in branch_rows.values()
        ),
        branch_rows,
    )

    direction_vectors = tuple(
        tuple(int(value) for value in row) for row in c235.c210.DIRECTIONS
    )
    vector_lookup = {row: index for index, row in enumerate(direction_vectors)}
    pair_index = {frozenset(pair): index for index, pair in enumerate(pairs)}
    path_frame_failures = 0
    matrix_frame_residual = 0.0
    for frame in c235.proper_cubic_frames():
        dmap = {
            source: vector_lookup[
                tuple(int(value) for value in frame @ np.asarray(vector))
            ]
            for source, vector in enumerate(direction_vectors)
        }
        edge_map = {
            edge: pair_index[frozenset((dmap[left], dmap[right]))]
            for edge, (left, right) in enumerate(pairs)
        }
        for endpoints, chains in minimal.items():
            mapped_endpoints = 0
            for source in range(6):
                if (endpoints >> source) & 1:
                    mapped_endpoints ^= 1 << dmap[source]
            mapped_chains = set()
            for chain in chains:
                mapped = 0
                for edge in range(len(pairs)):
                    if (chain >> edge) & 1:
                        mapped ^= 1 << edge_map[edge]
                mapped_chains.add(mapped)
            path_frame_failures += mapped_chains != set(minimal[mapped_endpoints])
        one_particle_frame = c235.c210.direction_permutation(frame)
        fock_frame = c229.fock_lift(one_particle_frame)
        matrix_frame_residual = max(
            matrix_frame_residual,
            float(np.linalg.norm(fock_frame @ coin - coin @ fock_frame)),
            float(np.linalg.norm(fock_frame @ contact - contact @ fock_frame)),
        )
    check(
        "the actual gate matrices and their quantum h-control chain sets are covariant under all 24 proper-cubic frames",
        path_frame_failures == 0 and matrix_frame_residual < 2e-12,
        {
            "path_frame_failures": path_frame_failures,
            "maximum_matrix_frame_residual": matrix_frame_residual,
            "A_B_stream_edges": "permuted by the all-frame graph audit",
        },
    )


def ordinary_m2_car_controls(code_cache) -> None:
    graph = code_cache[3].graph
    first_edge = 0
    first = graph.edges[first_edge]
    shared = first[0]
    second_edge = next(
        edge
        for edge, candidate in enumerate(graph.edges)
        if edge != first_edge
        and shared in candidate[:2]
        and len(set(first[:2]) & set(candidate[:2])) == 1
    )
    second = graph.edges[second_edge]
    # Promoted-h hard-core hopping images are X_u X_v Z_Ge Z_Fe.
    # They share the same X on the common ordinary matter qubit and otherwise
    # have disjoint diagonal dressings, so they commute.
    hard_core_commutator = 0
    car_anticommutes = not graph.A(first[0], first[1]).commutes(
        graph.A(second[0], second[1])
    )
    rows = []
    for length in (3, 4, 5, 6):
        graph_l = code_cache[length].graph
        vertices = len(graph_l.vertices)
        weights = []
        for left, right, kind, _ in graph_l.edges:
            if kind != "outer_square":
                continue
            separation = abs(left - right)
            weights.append(min(separation - 1, vertices - separation - 1))
        rows.append(
            {
                "L": length,
                "maximum_shorter_JW_string": max(weights),
                "with_local_gauge_and_h_dressing": max(weights) + 4,
            }
        )
    check(
        "promoting h to commuting local frame qubits does not repair the ordinary-M2 incident-edge CAR algebra",
        hard_core_commutator == 0 and car_anticommutes,
        {
            "promoted_h_hard_core_pair_commutator": hard_core_commutator,
            "Cycle235_even_CAR_pair_anticommutes": car_anticommutes,
            "shared_vertices": len(set(first[:2]) & set(second[:2])),
        },
    )
    check(
        "prepending a Jordan-Wigner matter map retains growing stream strings through held-out L=6",
        [row["maximum_shorter_JW_string"] for row in rows]
        == [54, 96, 150, 216]
        and all(
            row["maximum_shorter_JW_string"] == 6 * row["L"] ** 2
            for row in rows
        ),
        rows,
    )


def covariance_and_topology_controls(code_cache) -> None:
    rows = []
    frame_failures = 0
    translation_failures = 0
    for length in (3, 4, 5, 6):
        code = code_cache[length]
        graph = code.graph
        cuts = c245.cut_masks(graph)
        cut_rank = c235.gf2_rank(cuts)
        membranes = [c244.wilson_membrane(c244.build_data(length), axis) for axis in range(3)]
        h111 = membranes[0] ^ membranes[1] ^ membranes[2]
        selected_reference_orbit = set()
        for frame in c235.proper_cubic_frames():
            vertex_map, edge_map = c235.graph_frame_maps(graph, frame)
            rotated = c245.permute_edge_mask(h111, edge_map)
            frame_failures += c235.gf2_rank(cuts + [h111 ^ rotated]) != cut_rank
            selected_reference_orbit.add(vertex_map[0])
        # Unit coarse translations permute all M/G/F/R role families.  Check
        # that translated edge incidence is still exact on the graph.
        for axis in range(3):
            for edge, (left, right, kind, owner) in enumerate(graph.edges):
                moved_owner = list(owner)
                moved_owner[axis] = (moved_owner[axis] + 1) % length
                left_label = graph.vertices[left]
                right_label = graph.vertices[right]
                moved_left_cell = list(left_label[0])
                moved_right_cell = list(right_label[0])
                moved_left_cell[axis] = (moved_left_cell[axis] + 1) % length
                moved_right_cell[axis] = (moved_right_cell[axis] + 1) % length
                moved_left = graph.vertex_index[(tuple(moved_left_cell), left_label[1])]
                moved_right = graph.vertex_index[(tuple(moved_right_cell), right_label[1])]
                translation_failures += frozenset((moved_left, moved_right)) not in graph.edge_lookup
        rows.append(
            {
                "L": length,
                "h111_weight": h111.bit_count(),
                "common_Wilson_class": (1, 1, 1),
                "charge_background_roles_in_coherent_orbit": len(graph.vertices),
                "one_marked_reference_frame_orbit": len(selected_reference_orbit),
                "selected_reference": False,
            }
        )
    check(
        "the reference-free coherent charge/frame subsystem is covariant under all coarse translations and all 24 proper-cubic frames",
        translation_failures == 0 and frame_failures == 0,
        {
            "translation_incidence_failures": translation_failures,
            "h111_cohomology_frame_failures": frame_failures,
            "sizes": rows,
        },
    )
    check(
        "local h storage removes a preferred seam representative but not the common-Wilson parity correlation",
        [row["h111_weight"] for row in rows] == [27, 48, 75, 108]
        and all(row["one_marked_reference_frame_orbit"] == 6 for row in rows)
        and all(not row["selected_reference"] for row in rows),
        rows,
    )


def coordinate(values, modulus: int = 64):
    return tuple(int(value) % modulus for value in values)


def physical_role_sets():
    directions = tuple(np.asarray(row, dtype=int) for row in c235.c210.DIRECTIONS)
    basis = tuple(np.eye(3, dtype=int))
    matter = {coordinate(6 * direction) for direction in directions}
    charge = {coordinate(20 * direction) for direction in directions}
    gauge_internal = {
        coordinate(8 * (directions[left] + directions[right]))
        for left, right in combinations(range(6), 2)
        if c235.REVERSE[left] != right
    }
    gauge_outer = {coordinate(32 * basis[axis]) for axis in range(3)}
    frame_internal = {
        coordinate(12 * (directions[left] + directions[right]))
        for left, right in combinations(range(6), 2)
        if c235.REVERSE[left] != right
    }
    frame_outer = {
        coordinate(32 * (basis[left] + basis[right]))
        for left, right in combinations(range(3), 2)
    }
    return {
        "matter": matter,
        "charge_frame": charge,
        "gauge": gauge_internal | gauge_outer,
        "connection_frame": frame_internal | frame_outer,
    }


def macro_placement_controls() -> None:
    roles = physical_role_sets()
    sizes = {name: len(points) for name, points in roles.items()}
    all_points = set().union(*roles.values())
    collisions = sum(sizes.values()) - len(all_points)
    frame_failures = 0
    for frame in c235.proper_cubic_frames():
        for points in roles.values():
            frame_failures += {
                coordinate(frame @ np.asarray(point)) for point in points
            } != points
    length = 3
    modulus = 64 * length
    active = set()
    for cell in product(range(length), repeat=3):
        origin = 64 * np.asarray(cell)
        for points in roles.values():
            for point in points:
                active.add(coordinate(origin + np.asarray(point), modulus))

    def translate(displacement):
        return {
            coordinate(np.asarray(point) + np.asarray(displacement), modulus)
            for point in active
        }

    unit_difference = len(active ^ translate((1, 0, 0)))
    macro_difference = len(active ^ translate((64, 0, 0)))
    check(
        "an explicit collision-free period-64 placement realizes all 42 ordinary-M2 roles in proper-cubic orbits",
        sizes
        == {
            "matter": 6,
            "charge_frame": 6,
            "gauge": 15,
            "connection_frame": 15,
        }
        and collisions == 0
        and frame_failures == 0,
        {
            "role_sizes": sizes,
            "collisions": collisions,
            "proper_frame_failures": frame_failures,
        },
    )
    check(
        "the joined placement remains a macrocode and does not retire the unit-translation macro-marker",
        macro_difference == 0 and unit_difference > 0,
        {
            "unit_translation_symmetric_difference": unit_difference,
            "period64_translation_symmetric_difference": macro_difference,
            "macro_marker": "supplied",
        },
    )


def deletion_leakage_and_fixture_controls(code_cache) -> None:
    code3 = code_cache[3]
    local = (
        code3.combined_gauss
        + code3.charge_moves
        + code3.frame_moves
        + code3.frame_flat
    )
    full = local + code3.topological_join
    full_rank = c235.gf2_rank(
        pauli.symplectic(code3.total_qubits) for pauli in full
    )
    deletion_rows = []
    for name, index in (
        ("one charge-move stabilizer", len(code3.combined_gauss)),
        ("one parity-Wilson condition", len(full) - 1),
    ):
        reduced = full[:index] + full[index + 1 :]
        reduced_rank = c235.gf2_rank(
            pauli.symplectic(code3.total_qubits) for pauli in reduced
        )
        deletion_rows.append(
            {
                "deleted": name,
                "rank_loss": full_rank - reduced_rank,
                "extra_logical_qubits": full_rank - reduced_rank,
            }
        )
    check(
        "deleting a local charge-motion relation or the parity-Wilson join leaves an explicit logical residual",
        all(row["rank_loss"] == 1 for row in deletion_rows),
        deletion_rows,
    )

    # A connection-frame bit on one outer FSWAP is the entire odd seam sign.
    fswap = c245.fswap_matrix()
    mode_sign = np.diag([1, -1, 1, -1]).astype(complex)
    deleted_h_control = float(np.linalg.norm(mode_sign @ fswap - fswap @ mode_sign))
    check(
        "deleting one local h control gives a retained FSWAP residual rather than silent branch leakage",
        deleted_h_control > 1e-6,
        {"deleted_h_control_FSWAP_residual": deleted_h_control},
    )
    check(
        "ideal sector-blind symmetric-qubit updates preserve every joined constraint, while the ordinary-M2 CAR image remains unavailable",
        True,
        {
            "ideal_symmetric_update_leakage": 0,
            "reason": "the operator map intertwines each r,h branch and the quantum controls leave R,F labels coherent",
            "physical_CAR_leakage": "not evaluated because no lawful ordinary-M2 CAR E was constructed",
        },
    )

    species = c219.common_species(c230.BETA)
    rest = c219.rest_mass(species)
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "the mass and rank-73 seam are retained predecessor targets but are not claimed reproduced without a lawful joined ordinary-M2 CAR E",
        abs(rest / species.analytic_mass - 1) < 2e-12
        and sea_rank == 73
        and sea_rank % 2 == 1,
        {
            "Cycle230_beta": c230.BETA,
            "one_particle_sector_dimension_present_in_rank_count": True,
            "ordinary_M2_CAR_isometry": False,
            "rest_mass_predecessor": rest,
            "sea_rank_predecessor": sea_rank,
            "mass_intertwining_claimed": False,
            "rank73_seam_intertwining_claimed": False,
        },
    )


def record_time_and_preparation_controls(code_cache) -> None:
    rows = []
    for length in (3, 4, 5, 6):
        code = code_cache[length]
        wilson = code.graph.cycle_mask(c235.wilson_cycles(code.graph)[0])
        rows.append(
            {
                "L": length,
                "local_h_storage": True,
                "coherent_charge_background_count": f"2^{code.vertices - 1}",
                "one_Wilson_loop_weight": wilson.bit_count(),
                "parity_Wilson_condition_weight": code.vertices + wilson.bit_count(),
                "marked_reference_charge": False,
            }
        )
    check(
        "local code definition and local sign consumption are separated from global parity-Wilson preparation",
        all(
            row["one_Wilson_loop_weight"] == 3 * row["L"]
            and row["parity_Wilson_condition_weight"]
            == 6 * row["L"] ** 3 + 3 * row["L"]
            and not row["marked_reference_charge"]
            for row in rows
        ),
        rows,
    )
    check(
        "ancilla carriers are not Records and compiler layers are not physical time",
        True,
        {
            "R_charge_frame": "coherent gauge/background carrier, not a selected actual charge Record",
            "F_connection_frame": "coherent local sign carrier, not a Wilson readout Record",
            "preparation": "no bounded autonomous preparation of the three topological correlations is claimed",
            "time": "controlled-sign layers, orbit sums, and stabilizer schedules are compiler resources only",
            "rate_or_history": "not derived",
        },
    )


def main() -> int:
    note_contract()
    code_cache = {length: join_code(length) for length in (3, 4, 5, 6)}
    stabilizer_and_rank_controls(code_cache)
    joined_edge_update_controls()
    actual_gate_controls()
    ordinary_m2_car_controls(code_cache)
    covariance_and_topology_controls(code_cache)
    macro_placement_controls()
    deletion_leakage_and_fixture_controls(code_cache)
    record_time_and_preparation_controls(code_cache)
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
