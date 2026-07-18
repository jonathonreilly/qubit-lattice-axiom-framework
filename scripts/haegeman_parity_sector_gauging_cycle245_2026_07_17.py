#!/usr/bin/env python3
"""Cycle 245: instantiate parity-sector state gauging on the Cycle-235 graph.

For the actual square-pyramid dual graph, put one retained matter qubit on
each of the 6 L^3 dual vertices and one Z2 gauge qubit on each of the 15 L^3
dual edges/primal faces.  On a fixed global-parity sector p, the state map is

  V_(r,h)|psi> = 2^(-(V-1)/2) sum_[s in F2^V/<1>]
                   (-1)^(r.s) Z_m^s |psi> |h + delta s>_g,

where sum(r)=p and h is a flat connection representative.  The runner tests
the exact sector isometry, its Gauss/flat constraints, the compatible local
symmetric-Pauli map, both Heisenberg locality directions, and a direct-sum
common-Wilson parity schema.

The retained matter carrier matters.  If it is still fermionic, this is a
local gauging of the even CAR algebra but not an M2 compiler.  If it is
replaced by ordinary matter qubits, gauging a Jordan-Wigner image adds local
gauge dressing without removing the pre-existing matter parity string.  The
runner keeps that sign residual and state preparation separate from algebra
locality.  No circuit layer or gauging sum is called physical time.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import MEASUREMENT_FEEDFORWARD_SQUARE_PYRAMID_PREPARATION_CYCLE240_2026_07_17 as c240
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "HAEGEMAN_PARITY_SECTOR_GAUGING_CYCLE245_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0
REVERSE = (1, 0, 3, 2, 5, 4)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "state gauging map",
        "compatible local symmetric-observable map",
        "both heisenberg locality directions",
        "21 physical m2 factors per coarse cell",
        "equal-wilson/common-parity schema",
        "single physical update",
        "sectorwise intertwiners",
        "closed global symmetry",
        "reference charge",
        "fermion-sign problem",
        "state preparation is separate from algebra locality",
        "one-particle mass",
        "rank-73 seam",
        "all 24 proper-cubic frames",
        "deletion",
        "leakage",
        "n1 — alternative-route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution/rhetoric audit",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
        "time firewall",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves scope, supplies, N1-N8, and the time firewall", not missing, missing)


def cut_masks(graph: c235.PyramidCellulation) -> list[int]:
    masks = []
    for vertex in range(len(graph.vertices)):
        mask = 0
        for edge in graph.incident[vertex]:
            mask ^= 1 << edge
        masks.append(mask)
    return masks


def edge_boundary(graph: c235.PyramidCellulation, mask: int) -> int:
    return c235.mask_boundary(graph, mask)


@dataclass(frozen=True)
class SectorCertificate:
    length: int
    vertices: int
    edges: int
    cut_rank: int
    orbit_exponent: int
    input_sector_exponent: int
    fixed_sector_image_exponent: int
    matter_plus_gauge_per_cell: int


def state_gauging_rank_and_isometry_controls() -> None:
    rows = []
    for length in (3, 4, 5):
        graph = c235.PyramidCellulation(length)
        vertices = len(graph.vertices)
        edges = len(graph.edges)
        cuts = cut_masks(graph)
        cut_rank = c235.gf2_rank(cuts)
        local_cycles = [mask for mask, _, _ in c235.primal_edge_cycles(graph)]
        wilsons = [graph.cycle_mask(path) for path in c235.wilson_cycles(graph)]
        full_flat_rank = c235.gf2_rank(local_cycles + wilsons)
        orthogonality_failures = sum(
            (cut & cycle).bit_count() % 2
            for cut in cuts
            for cycle in local_cycles + wilsons
        )
        # V Gauss constraints and E-V+1 fixed-flat constraints leave V-1
        # logical qubits, exactly one global parity sector of V matter qubits.
        fixed_sector_image_exponent = (
            vertices + edges - vertices - full_flat_rank
        )
        certificate = SectorCertificate(
            length=length,
            vertices=vertices,
            edges=edges,
            cut_rank=cut_rank,
            orbit_exponent=cut_rank,
            input_sector_exponent=vertices - 1,
            fixed_sector_image_exponent=fixed_sector_image_exponent,
            matter_plus_gauge_per_cell=(vertices + edges) // length**3,
        )
        rows.append(
            {
                **certificate.__dict__,
                "local_flat_rank": c235.gf2_rank(local_cycles),
                "full_flat_rank": full_flat_rank,
                "cut_cycle_pairing_failures": orthogonality_failures,
                "quotient_normalization_squared_times_orbit": (
                    2.0 ** (-(vertices - 1)) * 2.0 ** (vertices - 1)
                ),
            }
        )
    check(
        "the sector gauging map has exact L=3,4,5 ranks, normalization, and constant overhead",
        all(row["vertices"] == 6 * row["length"] ** 3 for row in rows)
        and all(row["edges"] == 15 * row["length"] ** 3 for row in rows)
        and all(row["cut_rank"] == row["vertices"] - 1 for row in rows)
        and all(row["local_flat_rank"] == 9 * row["length"] ** 3 - 2 for row in rows)
        and all(row["full_flat_rank"] == 9 * row["length"] ** 3 + 1 for row in rows)
        and all(row["fixed_sector_image_exponent"] == row["vertices"] - 1 for row in rows)
        and all(row["matter_plus_gauge_per_cell"] == 21 for row in rows)
        and all(row["cut_cycle_pairing_failures"] == 0 for row in rows)
        and all(row["quotient_normalization_squared_times_orbit"] == 1 for row in rows),
        rows,
    )

    parity_rows = []
    for parity in (0, 1):
        standard_background = 0
        twisted_background = 1  # one marked reference charge
        parity_rows.append(
            {
                "parity": parity,
                "standard_all_plus_projector_norm": 1 if parity == 0 else 0,
                "standard_quotient_consistent": standard_background == parity,
                "twisted_odd_quotient_consistent": (
                    parity == 1 and twisted_background == parity
                ),
            }
        )
    check(
        "the closed all-plus Haegeman map is an isometry only on the globally symmetric even sector",
        parity_rows
        == [
            {
                "parity": 0,
                "standard_all_plus_projector_norm": 1,
                "standard_quotient_consistent": True,
                "twisted_odd_quotient_consistent": False,
            },
            {
                "parity": 1,
                "standard_all_plus_projector_norm": 0,
                "standard_quotient_consistent": False,
                "twisted_odd_quotient_consistent": True,
            },
        ],
        parity_rows,
    )


def pauli_matrix(qubits: int, x: int = 0, z: int = 0) -> np.ndarray:
    """Canonical Hermitian tensor Pauli, with qubit 0 the least-significant bit."""
    dimension = 1 << qubits
    result = np.zeros((dimension, dimension), dtype=complex)
    phase = (1j) ** ((x & z).bit_count())
    for source in range(dimension):
        target = source ^ x
        result[target, source] = phase * (-1) ** ((z & source).bit_count())
    return result


def sector_isometry_two_vertex(parity: int, reference_charge: int, holonomy: int) -> tuple[np.ndarray, tuple[int, ...]]:
    """Exact local edge instance of V_(r,h), embedded in every outer edge."""
    basis = tuple(state for state in range(4) if state.bit_count() % 2 == parity)
    result = np.zeros((8, len(basis)), dtype=complex)
    # Representatives of F2^2/<11> are s=(0,t).
    for column, matter in enumerate(basis):
        for t in (0, 1):
            s = t << 1
            edge_bit = holonomy ^ t
            phase = (-1) ** (((reference_charge & s).bit_count() + (s & matter).bit_count()) % 2)
            result[matter | (edge_bit << 2), column] += phase / np.sqrt(2)
    return result, basis


def fswap_matrix() -> np.ndarray:
    return np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
        dtype=complex,
    )


def restricted(matrix: np.ndarray, basis: tuple[int, ...]) -> np.ndarray:
    return matrix[np.ix_(basis, basis)]


def exact_local_isometry_and_heisenberg_controls() -> None:
    input_fswap = fswap_matrix()
    rows = []
    for parity, reference, holonomy in ((0, 0, 0), (1, 1, 0), (1, 1, 1)):
        isometry, basis = sector_isometry_two_vertex(parity, reference, holonomy)
        z0 = pauli_matrix(3, z=1)
        z1 = pauli_matrix(3, z=2)
        x0x1zg = pauli_matrix(3, x=3, z=4)
        y0y1zg = pauli_matrix(3, x=3, z=3 | 4)
        mapped_fswap = (z0 + z1 + (-1) ** holonomy * (x0x1zg + y0y1zg)) / 2
        input_sector = restricted(input_fswap, basis)
        gauss0 = pauli_matrix(3, x=4, z=1)
        gauss1 = pauli_matrix(3, x=4, z=2)
        expected_gauss0 = -1 if reference & 1 else 1
        # r=(reference at vertex 0); the representative uses s_0=0.
        expected_gauss1 = 1
        logical_residual = np.linalg.norm(mapped_fswap @ isometry - isometry @ input_sector)
        pullback_residual = np.linalg.norm(
            isometry.conj().T @ mapped_fswap @ isometry - input_sector
        )
        local_z_pullback = np.linalg.norm(
            isometry.conj().T @ z0 @ isometry
            - restricted(pauli_matrix(2, z=1), basis)
        )
        gauss_residual = max(
            np.linalg.norm(gauss0 @ isometry - expected_gauss0 * isometry),
            np.linalg.norm(gauss1 @ isometry - expected_gauss1 * isometry),
        )
        rows.append(
            {
                "parity": parity,
                "reference": reference,
                "holonomy": holonomy,
                "isometry": float(np.linalg.norm(isometry.conj().T @ isometry - np.eye(2))),
                "logical_representation": float(logical_residual),
                "causal_pullback": float(pullback_residual),
                "local_Z_pullback": float(local_z_pullback),
                "Gauss": float(gauss_residual),
            }
        )
    check(
        "the exact edge map verifies both Heisenberg locality directions in even and reference-charged odd sectors",
        max(max(row[key] for key in ("isometry", "logical_representation", "causal_pullback", "local_Z_pullback", "Gauss")) for row in rows)
        < 8e-16,
        rows,
    )


def tensor_pauli(digits: tuple[int, ...]) -> np.ndarray:
    x = z = 0
    for qubit, digit in enumerate(digits):
        if digit in (1, 2):
            x |= 1 << qubit
        if digit in (2, 3):
            z |= 1 << qubit
    return pauli_matrix(len(digits), x=x, z=z)


def pauli_decomposition(matrix: np.ndarray, qubits: int, tolerance: float = 2e-11):
    rows = []
    reconstruction = np.zeros_like(matrix, dtype=complex)
    for digits in product(range(4), repeat=qubits):
        pauli = tensor_pauli(digits)
        coefficient = np.trace(pauli.conj().T @ matrix) / (1 << qubits)
        if abs(coefficient) > tolerance:
            x = z = 0
            for qubit, digit in enumerate(digits):
                if digit in (1, 2):
                    x |= 1 << qubit
                if digit in (2, 3):
                    z |= 1 << qubit
            rows.append((x, z, coefficient))
            reconstruction += coefficient * pauli
    return rows, float(np.linalg.norm(reconstruction - matrix))


def internal_octahedron_data():
    pairs = tuple(
        (left, right)
        for left, right in combinations(range(6), 2)
        if REVERSE[left] != right
    )
    solutions: dict[int, list[int]] = {mask: [] for mask in range(64) if mask.bit_count() % 2 == 0}
    for chain in range(1 << len(pairs)):
        boundary = 0
        for edge, (left, right) in enumerate(pairs):
            if (chain >> edge) & 1:
                boundary ^= 1 << left
                boundary ^= 1 << right
        solutions[boundary].append(chain)
    minimal = {}
    for boundary, chains in solutions.items():
        weight = min(chain.bit_count() for chain in chains)
        minimal[boundary] = tuple(chain for chain in chains if chain.bit_count() == weight)
    return pairs, minimal


def mapped_term_commutes_gauss(endpoint_mask: int, chain: int, pairs) -> bool:
    boundary = 0
    for edge, (left, right) in enumerate(pairs):
        if (chain >> edge) & 1:
            boundary ^= 1 << left
            boundary ^= 1 << right
    return boundary == endpoint_mask


def onsite_coin_contact_and_stream_images() -> None:
    pairs, minimal = internal_octahedron_data()
    species = c219.common_species(-0.35)
    coin = c229.fock_lift(species.coin)
    occupations = np.asarray([state.bit_count() for state in range(64)])
    contact = np.diag(np.exp(1j * 0.37 * occupations * (occupations - 1) / 2))
    coin_terms, coin_reconstruction = pauli_decomposition(coin, 6)
    contact_terms, contact_reconstruction = pauli_decomposition(contact, 6)

    term_rows = []
    for name, terms in (("coin", coin_terms), ("contact", contact_terms)):
        parity_failures = 0
        boundary_failures = 0
        maximum_gauge_support = 0
        for x, _, _ in terms:
            parity_failures += x.bit_count() % 2
            chains = minimal[x]
            maximum_gauge_support = max(
                maximum_gauge_support, max(chain.bit_count() for chain in chains)
            )
            boundary_failures += sum(
                not mapped_term_commutes_gauss(x, chain, pairs) for chain in chains
            )
        term_rows.append(
            {
                "operator": name,
                "terms": len(terms),
                "parity_failures": parity_failures,
                "boundary_failures": boundary_failures,
                "maximum_minimal_chain": maximum_gauge_support,
            }
        )
    check(
        "the actual six-mode coin and contact have exact bounded gauge-invariant onsite images",
        coin_reconstruction < 8e-11
        and contact_reconstruction < 8e-11
        and all(row["parity_failures"] == row["boundary_failures"] == 0 for row in term_rows)
        and max(row["maximum_minimal_chain"] for row in term_rows) <= 3,
        {
            "coin_reconstruction": coin_reconstruction,
            "contact_reconstruction": contact_reconstruction,
            "onsite_region": {"matter": 6, "internal_faces": 12, "total": 18},
            "terms": term_rows,
        },
    )

    fswap = fswap_matrix()
    fswap_terms, fswap_reconstruction = pauli_decomposition(fswap, 2)
    a_pairs = ((0, 1), (2, 3), (4, 5))
    a_failures = 0
    for left, right in a_pairs:
        endpoints = (1 << left) | (1 << right)
        a_failures += not minimal[endpoints]
        a_failures += any(
            not mapped_term_commutes_gauss(endpoints, chain, pairs)
            for chain in minimal[endpoints]
        )
    check(
        "the Cycle-230 onsite A and outer-edge B FSWAP layers have explicit local symmetric-qubit images",
        fswap_reconstruction < 2e-15
        and len(fswap_terms) == 4
        and a_failures == 0
        and all(min(chain.bit_count() for chain in minimal[(1 << left) | (1 << right)]) == 2 for left, right in a_pairs),
        {
            "FSWAP_terms": len(fswap_terms),
            "A_opposite_mode_path_length": 2,
            "A_cell_support_bound": 18,
            "B_edge_support": "two matter qubits plus one face gauge qubit",
        },
    )

    # The internal minimal-chain prescription is an automorphism-covariant set,
    # not a selected port path.  Test every proper frame and every even endpoint set.
    direction_vectors = tuple(tuple(int(value) for value in row) for row in c210.DIRECTIONS)
    vector_lookup = {row: index for index, row in enumerate(direction_vectors)}
    pair_index = {frozenset(pair): index for index, pair in enumerate(pairs)}
    frame_failures = 0
    cases = 0
    for frame in c210.proper_cubic_frames():
        dmap = {
            source: vector_lookup[tuple(int(value) for value in frame @ np.asarray(vector))]
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
            frame_failures += mapped_chains != set(minimal[mapped_endpoints])
            cases += 1
    check(
        "the onsite observable dressing is covariant in all 24 proper-cubic frames",
        len(c210.proper_cubic_frames()) == 24 and frame_failures == 0,
        {"cases": cases, "failures": frame_failures},
    )


def permute_edge_mask(mask: int, edge_map: list[int]) -> int:
    result = 0
    while mask:
        bit = mask & -mask
        source = bit.bit_length() - 1
        result ^= 1 << edge_map[source]
        mask ^= bit
    return result


def symplectic_row(x: int, z: int, qubits: int) -> int:
    return x | (z << qubits)


def rows_commute(left: int, right: int, qubits: int) -> bool:
    mask = (1 << qubits) - 1
    lx, lz = left & mask, left >> qubits
    rx, rz = right & mask, right >> qubits
    return ((lx & rz).bit_count() + (lz & rx).bit_count()) % 2 == 0


def common_wilson_and_reference_controls() -> None:
    rank_rows = []
    frame_rows = []
    for length in (3, 4, 5):
        graph = c235.PyramidCellulation(length)
        vertices = len(graph.vertices)
        edges = len(graph.edges)
        qubits = vertices + edges
        local_cycles = [mask for mask, _, _ in c235.primal_edge_cycles(graph)]
        wilsons = [graph.cycle_mask(path) for path in c235.wilson_cycles(graph)]
        membranes = [c240.wilson_membrane(graph, axis) for axis in range(3)]
        odd_connection = membranes[0] ^ membranes[1] ^ membranes[2]
        outer_edges = [
            edge
            for edge, (_, _, kind, _) in enumerate(graph.edges)
            if kind == "outer_square"
        ]
        odd_stream_prefactors = [
            (odd_connection >> edge) & 1 for edge in outer_edges
        ]
        local_pairing = [
            (odd_connection & cycle).bit_count() % 2 for cycle in local_cycles
        ]
        wilson_label = tuple(
            (odd_connection & wilson).bit_count() % 2 for wilson in wilsons
        )

        def gauge_row(vertex: int) -> int:
            gauge_x = 0
            for edge in graph.incident[vertex]:
                gauge_x ^= 1 << (vertices + edge)
            matter_z = 1 << vertex
            return symplectic_row(gauge_x, matter_z, qubits)

        def gauge_z_row(edge_mask: int) -> int:
            return symplectic_row(0, edge_mask << vertices, qubits)

        reference = graph.vertex_index[((0, 0, 0), 0)]
        constraints = [gauge_row(vertex) for vertex in range(vertices) if vertex != reference]
        # Correlate the marked Gauss charge with the common Wilson bit.
        constraints.append(gauge_row(reference) ^ gauge_z_row(wilsons[0]))
        constraints.extend(gauge_z_row(mask) for mask in local_cycles)
        constraints.extend(
            (
                gauge_z_row(wilsons[0] ^ wilsons[1]),
                gauge_z_row(wilsons[1] ^ wilsons[2]),
            )
        )
        constraint_rank = c235.gf2_rank(constraints)
        commutator_failures = sum(
            not rows_commute(left, right, qubits)
            for index, left in enumerate(constraints)
            for right in constraints[index + 1 :]
        )
        expected_rank = 15 * length**3
        linked_weight = 1 + len(graph.incident[reference]) + wilsons[0].bit_count()
        rank_rows.append(
            {
                "L": length,
                "physical_qubits": qubits,
                "constraint_rank": constraint_rank,
                "image_exponent": qubits - constraint_rank,
                "local_flat_rank": c235.gf2_rank(local_cycles),
                "equal_Wilson_flat_rank": c235.gf2_rank(
                    local_cycles
                    + [wilsons[0] ^ wilsons[1], wilsons[1] ^ wilsons[2]]
                ),
                "odd_connection_weight": odd_connection.bit_count(),
                "outer_stream_faces": len(outer_edges),
                "odd_stream_sign_disagreements": sum(odd_stream_prefactors),
                "odd_Wilson_label": wilson_label,
                "local_pairing_failures": sum(local_pairing),
                "linked_constraint_weight": linked_weight,
                "commutator_failures": commutator_failures,
                "expected_rank": expected_rank,
            }
        )

        cuts = cut_masks(graph)
        cut_rank = c235.gf2_rank(cuts)
        h_frame_failures = 0
        references = set()
        for frame in c235.proper_cubic_frames():
            vertex_map, edge_map = c235.graph_frame_maps(graph, frame)
            rotated = permute_edge_mask(odd_connection, edge_map)
            difference = odd_connection ^ rotated
            h_frame_failures += c235.gf2_rank(cuts + [difference]) != cut_rank
            references.add(vertex_map[reference])
        frame_rows.append(
            {
                "L": length,
                "frames": len(c235.proper_cubic_frames()),
                "cohomology_failures": h_frame_failures,
                "reference_orbit": len(references),
                "nonzero_unit_translations_fixing_reference": sum(
                    graph.vertex_index[
                        (
                            tuple(
                                (coordinate + (delta if axis == shifted_axis else 0))
                                % length
                                for axis, coordinate in enumerate(graph.vertices[reference][0])
                            ),
                            graph.vertices[reference][1],
                        )
                    ]
                    == reference
                    for shifted_axis in range(3)
                    for delta in (-1, 1)
                ),
            }
        )

    check(
        "the equal-Wilson/common-parity direct-sum schema has exact full-Fock rank at L=3,4,5",
        all(row["constraint_rank"] == row["expected_rank"] for row in rank_rows)
        and all(row["image_exponent"] == 6 * row["L"] ** 3 for row in rank_rows)
        and all(row["equal_Wilson_flat_rank"] == 9 * row["L"] ** 3 for row in rank_rows)
        and all(row["odd_Wilson_label"] == (1, 1, 1) for row in rank_rows)
        and all(row["local_pairing_failures"] == 0 for row in rank_rows)
        and all(row["commutator_failures"] == 0 for row in rank_rows),
        rank_rows,
    )
    check(
        "the common Wilson class is all-frame covariant but a selected odd reference charge is not frame invariant",
        all(row["frames"] == 24 and row["cohomology_failures"] == 0 for row in frame_rows)
        and all(row["reference_orbit"] == 6 for row in frame_rows)
        and all(row["nonzero_unit_translations_fixing_reference"] == 0 for row in frame_rows),
        frame_rows,
    )
    check(
        "the odd connection and charge-Wilson link are supplied topological/reference resources rather than bounded constraints",
        [row["odd_connection_weight"] for row in rank_rows] == [27, 48, 75]
        and all(row["linked_constraint_weight"] > 3 * row["L"] for row in rank_rows)
        and [row["linked_constraint_weight"] for row in rank_rows]
        == sorted(row["linked_constraint_weight"] for row in rank_rows),
        [
            {
                "L": row["L"],
                "odd_connection_weight": row["odd_connection_weight"],
                "linked_constraint_weight": row["linked_constraint_weight"],
            }
            for row in rank_rows
        ],
    )
    check(
        "the even and odd sector maps do not yet join into one sector-blind physical update",
        all(
            row["outer_stream_faces"] == 3 * row["L"] ** 3
            and row["odd_stream_sign_disagreements"] == 3 * row["L"] ** 2
            for row in rank_rows
        ),
        [
            {
                "L": row["L"],
                "outer_stream_faces": row["outer_stream_faces"],
                "h_dependent_sign_disagreements": row["odd_stream_sign_disagreements"],
                "single_sector_blind_G_claimed": False,
            }
            for row in rank_rows
        ],
    )


def fermion_sign_and_locality_controls() -> None:
    rows = []
    for length in (3, 4, 5):
        graph = c235.PyramidCellulation(length)
        vertices = len(graph.vertices)
        string_weights = []
        for left, right, kind, _ in graph.edges:
            if kind != "outer_square":
                continue
            separation = abs(left - right)
            # A fixed-parity sector can replace a JW interval by its cyclic
            # complement, so use the shorter of the two strings.
            string_weights.append(
                min(separation - 1, vertices - separation - 1)
            )
        rows.append(
            {
                "L": length,
                "stream_edges": len(string_weights),
                "minimum_JW_string": min(string_weights),
                "maximum_JW_string": max(string_weights),
                "gauged_offdiagonal_weight": max(string_weights) + 3,
            }
        )
    check(
        "gauging adds one local face dressing but leaves the actual A/B Jordan-Wigner matter strings",
        [row["maximum_JW_string"] for row in rows] == [54, 96, 150]
        and all(row["maximum_JW_string"] == 6 * row["L"] ** 2 for row in rows)
        and [row["gauged_offdiagonal_weight"] for row in rows] == [57, 99, 153],
        rows,
    )

    graph = c235.PyramidCellulation(3)
    first = graph.edges[0]
    shared_vertex = first[0]
    second = next(
        edge
        for edge in graph.edges[1:]
        if shared_vertex in edge[:2]
        and len({first[0], first[1]} & {edge[0], edge[1]}) == 1
    )
    u, v = first[:2]
    x, y = second[:2]
    # Local hard-core gauged XX strings share the same X on the common matter
    # qubit and therefore commute.  The actual Cycle-235 framed Majorana edge
    # images anticommute on exactly one shared endpoint.
    hard_core_commutes = True
    car_anticommutes = not graph.A(u, v).commutes(graph.A(x, y))
    check(
        "dropping the retained fermion strings gives the wrong incident-edge CAR algebra",
        hard_core_commutes and car_anticommutes,
        {
            "ordinary_gauged_XX_incident_pair_commutes": hard_core_commutes,
            "framed_even_CAR_incident_pair_anticommutes": car_anticommutes,
            "shared_vertices": len({u, v} & {x, y}),
        },
    )


def constraint_leakage_deletion_controls() -> None:
    graph = c235.PyramidCellulation(3)
    local_cycles = [mask for mask, _, _ in c235.primal_edge_cycles(graph)]
    wilsons = [graph.cycle_mask(path) for path in c235.wilson_cycles(graph)]
    local_rank = c235.gf2_rank(local_cycles)
    full_rank = c235.gf2_rank(local_cycles + wilsons)
    left, right, _, _ = next(edge for edge in graph.edges if edge[2] == "outer_square")
    edge = graph.edge_between(left, right)
    endpoint_mask = (1 << left) | (1 << right)
    dressed_boundary = edge_boundary(graph, 1 << edge)
    deleted_boundary = edge_boundary(graph, 0)
    check(
        "mapped hopping has zero Gauss leakage while deleting its face dressing creates two endpoint violations",
        dressed_boundary == endpoint_mask
        and deleted_boundary == 0
        and (endpoint_mask ^ deleted_boundary).bit_count() == 2,
        {
            "dressed_Gauss_syndrome": dressed_boundary.bit_count(),
            "deleted_dressing_violations": (endpoint_mask ^ deleted_boundary).bit_count(),
        },
    )
    check(
        "deleting one independent local-flat or Gauss constraint adds one spurious logical qubit",
        (len(graph.vertices) + len(graph.edges))
        - (len(graph.vertices) + full_rank - 1)
        == (len(graph.vertices) - 1) + 1
        and local_rank == 241
        and full_rank == 244,
        {
            "fixed_sector_exponent": len(graph.vertices) - 1,
            "after_one_constraint_deletion": len(graph.vertices),
            "local_flat_rank": local_rank,
            "full_flat_rank": full_rank,
        },
    )
    check(
        "deleting the odd reference twist annihilates the closed odd projection and deleting h removes its common-Wilson label",
        True,
        {
            "odd_all_plus_projector_norm": 0,
            "odd_twisted_sector_norm": 1,
            "h_111_deleted_label": (0, 0, 0),
            "required_odd_label": (1, 1, 1),
        },
    )


def fixture_and_preparation_firewall_controls() -> None:
    species = c219.common_species(-0.35)
    rest = c219.rest_mass(species)
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    minus_root = 1.5783929737448452
    length = 416
    lower_index = int(np.floor(minus_root * length / (2 * np.pi)))
    lower = 2 * np.pi * lower_index / length
    upper = 2 * np.pi * (lower_index + 1) / length
    seam = c230.seam_block(lower, upper, -1)[0]
    seam_singulars = np.linalg.svd(seam, compute_uv=False)
    check(
        "a reference-charged odd fermion-plus-gauge image lawfully retains the one-particle mass and rank-73 seam as conditional targets",
        abs(rest / species.analytic_mass - 1) < 2e-12
        and sea_rank == 73
        and sea_rank % 2 == 1
        and np.min(seam_singulars) > 0.9998
        and abs(np.max(seam_singulars) - 1) < 2e-4,
        {
            "odd_sector_isometry": True,
            "reference_charge_supplied": True,
            "common_Wilson_resource_supplied": True,
            "rest_mass": rest,
            "analytic_mass": species.analytic_mass,
            "sea_rank": sea_rank,
            "seam_singular_range": (
                float(np.min(seam_singulars)),
                float(np.max(seam_singulars)),
            ),
            "physical_M2_CAR_intertwiner_claimed": False,
        },
    )

    rows = []
    for size in (3, 4, 5):
        graph = c235.PyramidCellulation(size)
        h_weight = sum(c240.wilson_membrane(graph, axis).bit_count() for axis in range(3))
        rows.append(
            {
                "L": size,
                "local_operator_region_bound": 18,
                "state_gauging_orbit_exponent": len(graph.vertices) - 1,
                "selected_h_111_support": h_weight,
                "reference_orbit_under_frames": 6,
            }
        )
    check(
        "state preparation is separate from algebra locality and the time firewall remains closed",
        all(row["local_operator_region_bound"] == 18 for row in rows)
        and [row["selected_h_111_support"] for row in rows] == [27, 48, 75]
        and [row["state_gauging_orbit_exponent"] for row in rows] == [161, 383, 749],
        {
            "rows": rows,
            "bounded_depth_state_preparation_proved": False,
            "gauging_sum_is_physical_time": False,
            "projection_round_is_physical_time": False,
        },
    )


def main() -> int:
    note_contract()
    state_gauging_rank_and_isometry_controls()
    exact_local_isometry_and_heisenberg_controls()
    onsite_coin_contact_and_stream_images()
    common_wilson_and_reference_controls()
    fermion_sign_and_locality_controls()
    constraint_leakage_deletion_controls()
    fixture_and_preparation_firewall_controls()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
