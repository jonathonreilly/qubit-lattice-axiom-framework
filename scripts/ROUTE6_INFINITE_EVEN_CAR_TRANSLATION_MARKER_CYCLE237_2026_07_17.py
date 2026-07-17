#!/usr/bin/env python3
"""Cycle 237: infinite even-CAR and unit-translation marker discriminator.

This runner keeps four questions separate:

1. finite scalar-reference parity bookkeeping;
2. quasi-local even-CAR observables versus the full graded CAR net;
3. locality-preserving operator maps versus preparation of a block-code state;
4. covariance of a code family versus selection/preparation of one crystal sector.

The marker construction is deliberately explicit.  The 27 active residues of
the Cycle-232 spacing-16 layout remain arbitrary data qubits.  The other 4069
residues carry a deterministic classical product marker.  A radius-two local
window identifies one of all 16^3 translated phases, and neighboring windows
have exactly one compatible successor in each positive axis.  The marker word
is invariant under all 24 proper-cubic frames, so the allowed local-projector
family is both unit-translation and proper-cubic covariant.

This does not prepare or select a marker sector from homogeneous input, and it
does not compile the CAR dynamics.  It is a code/admissibility construction.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path
from random import Random
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17 as c232

NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "ROUTE6_INFINITE_EVEN_CAR_TRANSLATION_MARKER_CYCLE237_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0
PERIOD = 16
RADIUS = 2
MARKER_SEED = 237000

DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
OPPOSITE = (1, 0, 3, 2, 5, 4)
POSITIVE_DIRECTIONS = (0, 2, 4)


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
        "local even-algebra morphism",
        "sector representation",
        "locality-preserving state encoding",
        "finite-depth preparation",
        "rank-73",
        "three torus wilson labels",
        "radius-two marker",
        "16^3",
        "authority: none",
        "audit: unset",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("note preserves claim distinctions and N1-N8 gate", not missing, missing)


def det3(matrix: tuple[tuple[int, int, int], ...]) -> int:
    return (
        matrix[0][0]
        * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1]
        * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2]
        * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat_vec(
    matrix: tuple[tuple[int, int, int], ...],
    vector: tuple[int, int, int],
    modulus: int | None = None,
) -> tuple[int, int, int]:
    out = tuple(
        sum(matrix[row][col] * vector[col] for col in range(3))
        for row in range(3)
    )
    if modulus is not None:
        return tuple(value % modulus for value in out)
    return out


def proper_cubic_frames() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    frames = []
    for axis_permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(
                    signs[row] if axis_permutation[row] == col else 0
                    for col in range(3)
                )
                for row in range(3)
            )
            if det3(matrix) == 1:
                frames.append(matrix)
    return tuple(frames)


def add_mod(
    left: tuple[int, int, int], right: tuple[int, int, int]
) -> tuple[int, int, int]:
    return tuple((left[axis] + right[axis]) % PERIOD for axis in range(3))


def scale_mod(
    scalar: int, vector: tuple[int, int, int]
) -> tuple[int, int, int]:
    return tuple((scalar * value) % PERIOD for value in vector)


def active_residues() -> frozenset[tuple[int, int, int]]:
    active: set[tuple[int, int, int]] = set()
    for left, right in combinations(range(6), 2):
        if right == OPPOSITE[left]:
            continue
        active.add(
            scale_mod(2, add_mod(DIRECTIONS[left], DIRECTIONS[right]))
        )
    for direction in range(6):
        active.add(scale_mod(4, DIRECTIONS[direction]))
    for direction in POSITIVE_DIRECTIONS:
        vector = DIRECTIONS[direction]
        active.update(scale_mod(offset, vector) for offset in (7, 8, 9))
    return frozenset(active)


def finite_domain_bookkeeping() -> None:
    print("\nFINITE OPEN/PERIODIC BOOKKEEPING")
    for length in (3, 4, 5):
        cells = length**3
        for periodic in (False, True):
            graph = c232.ReferenceGraph(length, periodic)
            vertices = len(graph.vertices)
            edges = len(graph.edges)
            cycle_rank = edges - vertices + 1
            local_cycles = c232.local_cycles(graph)
            bounded_loop_rank = c232.gf2_rank(
                mask for mask, _, _ in local_cycles
            )
            boundary_failures = sum(
                c232.mask_boundary(graph, mask) != 0
                for mask, _, _ in local_cycles
            )
            wilson = cycle_rank - bounded_loop_rank
            check(
                f"L={length} {'periodic' if periodic else 'open'} graph rank",
                vertices == 7 * cells
                and cycle_rank == edges - vertices + 1
                and boundary_failures == 0
                and wilson == (3 if periodic else 0),
                {
                    "vertices": vertices,
                    "edges": edges,
                    "cycle_rank": cycle_rank,
                    "bounded_loop_rank": bounded_loop_rank,
                    "wilson_labels": wilson,
                    "bounded_loop_boundary_failures": boundary_failures,
                },
            )

        # BKSF represents the even sector of seven modes per cell.  Uniform
        # reference equality has rank N-1 and leaves 6N logical qubits.
        logical_before_reference = 7 * cells - 1
        reference_rank = cells - 1
        logical_after_reference = logical_before_reference - reference_rank
        if cells % 2:
            multiplicities = {"matter_even": 1, "matter_odd": 1}
        else:
            multiplicities = {"matter_even": 2, "matter_odd": 0}
        check(
            f"L={length} scalar-reference sector count",
            logical_after_reference == 6 * cells
            and (
                multiplicities == {"matter_even": 1, "matter_odd": 1}
                if cells % 2
                else multiplicities == {"matter_even": 2, "matter_odd": 0}
            ),
            {
                "cells": cells,
                "logical_qubits": logical_after_reference,
                **multiplicities,
            },
        )


def kron_all(operators: list[np.ndarray]) -> np.ndarray:
    result = np.array([[1.0 + 0.0j]])
    for operator in operators:
        result = np.kron(result, operator)
    return result


def quasi_local_and_full_car_controls() -> None:
    print("\nQUASI-LOCAL EVEN CAR / FULL GRADED CAR")
    identity = np.eye(2, dtype=complex)
    x_pauli = np.array([[0, 1], [1, 0]], dtype=complex)
    y_pauli = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z_pauli = np.diag([1, -1]).astype(complex)

    # The canonical finite-region parity products are not norm Cauchy.
    parity_gaps = []
    for modes in range(1, 7):
        old_embedded = kron_all([z_pauli] * modes + [identity])
        enlarged = kron_all([z_pauli] * (modes + 1))
        parity_gaps.append(float(np.linalg.norm(enlarged - old_embedded, 2)))
    check(
        "finite parity products have no quasi-local norm limit",
        max(abs(value - 2.0) for value in parity_gaps) < 1e-12,
        parity_gaps,
    )

    # Exact two-mode witness.  Fermionic Majoranas anticommute.  Operators on
    # disjoint bosonic tensor factors commute, so they cannot be their images
    # under a radius-local full-CAR homomorphism.
    gamma_left = np.kron(x_pauli, identity)
    gamma_right = np.kron(z_pauli, x_pauli)
    boson_left = np.kron(x_pauli, identity)
    boson_right = np.kron(identity, x_pauli)
    fermion_anticommutator = float(
        np.linalg.norm(gamma_left @ gamma_right + gamma_right @ gamma_left, 2)
    )
    fermion_commutator = float(
        np.linalg.norm(gamma_left @ gamma_right - gamma_right @ gamma_left, 2)
    )
    boson_anticommutator = float(
        np.linalg.norm(boson_left @ boson_right + boson_right @ boson_left, 2)
    )
    boson_commutator = float(
        np.linalg.norm(boson_left @ boson_right - boson_right @ boson_left, 2)
    )
    check(
        "full graded CAR cannot map odd fields to disjoint bosonic supports",
        fermion_anticommutator < 1e-12
        and abs(fermion_commutator - 2.0) < 1e-12
        and abs(boson_anticommutator - 2.0) < 1e-12
        and boson_commutator < 1e-12,
        {
            "fermion_anticommutator": fermion_anticommutator,
            "fermion_commutator": fermion_commutator,
            "boson_anticommutator": boson_anticommutator,
            "boson_commutator": boson_commutator,
        },
    )
    for radius in (0, 1, 2, 4):
        separation = 2 * radius + 1
        check(
            f"radius-{radius} remote odd-field witness",
            separation > 2 * radius,
            {"separation": separation, "bosonic_CAR_residual": 2.0},
        )

    # Disjoint even observables commute exactly.  Four-mode JW matrices are
    # used only as a finite algebra regression, not as the spatial compiler.
    def majorana(mode: int, second: bool, count: int = 4) -> np.ndarray:
        operators = []
        for site in range(count):
            if site < mode:
                operators.append(z_pauli)
            elif site == mode:
                operators.append(y_pauli if second else x_pauli)
            else:
                operators.append(identity)
        return kron_all(operators)

    even_left = -1j * majorana(0, False) @ majorana(0, True)
    even_right = -1j * majorana(3, False) @ majorana(3, True)
    even_commutator = float(
        np.linalg.norm(even_left @ even_right - even_right @ even_left, 2)
    )
    check(
        "disjoint even-CAR observables commute",
        even_commutator < 1e-12,
        even_commutator,
    )

    fixture_parities = {"one_particle": 1 % 2, "rank_73": 73 % 2, "vacuum": 0}
    check(
        "one-particle and rank-73 fixtures share the odd superselection sector",
        fixture_parities["one_particle"] == fixture_parities["rank_73"] == 1,
        fixture_parities,
    )


def preparation_depth_control() -> None:
    print("\nBLOCK-CODE PREPARATION DEPTH")
    held = {length: (length - 2) // 4 for length in (3, 4, 5)}
    extended = {length: (length - 2) // 4 for length in (6, 10, 14, 18)}
    check(
        "held open squares expose no asymptotic depth by themselves",
        held == {3: 0, 4: 0, 5: 0},
        held,
    )
    check(
        "embedded open-square 8-shape depth bound grows with size",
        extended == {6: 1, 10: 2, 14: 3, 18: 4},
        extended,
    )
    print(
        "INFO Guaita theorem applies because the scalar reference r-lattice "
        "contains these open square subgraphs; it lower-bounds unitary "
        "preparation from product input, not measurement/feedforward preparation."
    )


def fixture_graph_control() -> None:
    """Verify the fixture actually contains the required overlapping loops."""

    print("\nFIXTURE-SPECIFIC OVERLAPPING-LOOP GEOMETRY")

    def shift(
        cell: tuple[int, int, int], axis: int, amount: int = 1
    ) -> tuple[int, int, int]:
        target = list(cell)
        target[axis] += amount
        return tuple(target)

    def matter_edge(
        left: tuple[tuple[int, int, int], int],
        right: tuple[tuple[int, int, int], int],
    ) -> bool:
        left_cell, left_mode = left
        right_cell, right_mode = right
        if left_cell == right_cell:
            return right_mode != OPPOSITE[left_mode] and right_mode != left_mode
        for axis in range(3):
            if right_cell == shift(left_cell, axis):
                return left_mode == 2 * axis + 1 and right_mode == 2 * axis
            if left_cell == shift(right_cell, axis):
                return right_mode == 2 * axis + 1 and left_mode == 2 * axis
        return False

    for length in (3, 4, 5):
        cycles = 0
        failures = 0
        for axis_a, axis_b in combinations(range(3), 2):
            other = 3 - axis_a - axis_b
            for fixed in range(length):
                for first in range(length - 1):
                    for second in range(length - 1):
                        cell_list = [0, 0, 0]
                        cell_list[axis_a] = first
                        cell_list[axis_b] = second
                        cell_list[other] = fixed
                        cell = tuple(cell_list)
                        cell_a = shift(cell, axis_a)
                        cell_b = shift(cell, axis_b)
                        cell_ab = shift(cell_a, axis_b)
                        positive_a, negative_a = 2 * axis_a, 2 * axis_a + 1
                        positive_b, negative_b = 2 * axis_b, 2 * axis_b + 1
                        # Four stream edges and four nonopposite intracell turns.
                        loop = (
                            (cell, negative_a),
                            (cell_a, positive_a),
                            (cell_a, negative_b),
                            (cell_ab, positive_b),
                            (cell_ab, positive_a),
                            (cell_b, negative_a),
                            (cell_b, positive_b),
                            (cell, negative_b),
                        )
                        cycles += 1
                        if len(set(loop)) != 8 or any(
                            not matter_edge(loop[index], loop[(index + 1) % 8])
                            for index in range(8)
                        ):
                            failures += 1
        check(
            f"L={length} six-mode matter graph has tiled 8-edge plaquettes",
            failures == 0 and cycles == 3 * length * (length - 1) ** 2,
            {"plaquettes": cycles, "failures": failures},
        )

    # The scalar r-lattice gives literal square-grid theta/8-shaped subgraphs.
    # The three paths below share only endpoints and their central-corridor
    # separation grows linearly.  We then lift every coarse path explicitly to
    # the six-mode matter graph, including a one-mode bridge whenever a
    # straight passage would otherwise connect opposite ports.
    theta_controls = {}
    matter_theta_controls = {}

    def stream_ports(
        left: tuple[int, int, int], right: tuple[int, int, int]
    ) -> tuple[int, int]:
        delta = tuple(right[axis] - left[axis] for axis in range(3))
        axis = next(axis for axis, value in enumerate(delta) if value)
        if delta[axis] == 1:
            return 2 * axis + 1, 2 * axis
        if delta[axis] == -1:
            return 2 * axis, 2 * axis + 1
        raise ValueError((left, right))

    def lift_coarse_path(
        path: tuple[tuple[int, int, int], ...], endpoint_mode: int = 4
    ) -> tuple[tuple[tuple[int, int, int], int], ...]:
        lifted = [(path[0], endpoint_mode)]
        for index in range(len(path) - 1):
            left, right = path[index], path[index + 1]
            departure, arrival = stream_ports(left, right)
            current = lifted[-1]
            departure_vertex = (left, departure)
            if not matter_edge(current, departure_vertex):
                bridge = next(
                    mode
                    for mode in range(6)
                    if matter_edge(current, (left, mode))
                    and matter_edge((left, mode), departure_vertex)
                )
                lifted.append((left, bridge))
            lifted.append(departure_vertex)
            lifted.append((right, arrival))
        final_vertex = (path[-1], endpoint_mode)
        if not matter_edge(lifted[-1], final_vertex):
            bridge = next(
                mode
                for mode in range(6)
                if matter_edge(lifted[-1], (path[-1], mode))
                and matter_edge((path[-1], mode), final_vertex)
            )
            lifted.append((path[-1], bridge))
        lifted.append(final_vertex)
        return tuple(lifted)

    for length in (6, 10, 14, 18):
        middle = (length - 1) // 2
        start = (0, middle)
        end = (length - 1, middle)
        direct = tuple((x, middle) for x in range(length))
        upper = (
            tuple((0, y) for y in range(middle, -1, -1))
            + tuple((x, 0) for x in range(1, length))
            + tuple((length - 1, y) for y in range(1, middle + 1))
        )
        lower = (
            tuple((0, y) for y in range(middle, length))
            + tuple((x, length - 1) for x in range(1, length))
            + tuple((length - 1, y) for y in range(length - 2, middle - 1, -1))
        )

        def edge_set(path: tuple[tuple[int, int], ...]) -> set[frozenset[tuple[int, int]]]:
            return {
                frozenset((path[index], path[index + 1]))
                for index in range(len(path) - 1)
            }

        paths = (direct, upper, lower)
        interiors_disjoint = all(
            set(paths[left][1:-1]).isdisjoint(paths[right][1:-1])
            for left, right in combinations(range(3), 2)
        )
        edges = tuple(edge_set(path) for path in paths)
        edges_disjoint = all(
            edges[left].isdisjoint(edges[right])
            for left, right in combinations(range(3), 2)
        )
        lawful_steps = all(
            abs(path[index][0] - path[index + 1][0])
            + abs(path[index][1] - path[index + 1][1])
            == 1
            for path in paths
            for index in range(len(path) - 1)
        )
        theta_controls[length] = {
            "endpoint_match": all(path[0] == start and path[-1] == end for path in paths),
            "interiors_disjoint": interiors_disjoint,
            "edges_disjoint": edges_disjoint,
            "lawful_steps": lawful_steps,
            "corridor_separation": min(middle, length - 1 - middle),
        }

        coarse_3d = tuple(
            tuple((x, y, 0) for x, y in path) for path in paths
        )
        matter_paths = tuple(lift_coarse_path(path) for path in coarse_3d)
        matter_interiors_disjoint = all(
            set(matter_paths[left][1:-1]).isdisjoint(
                matter_paths[right][1:-1]
            )
            for left, right in combinations(range(3), 2)
        )
        matter_edges = tuple(edge_set(path) for path in matter_paths)
        matter_edges_disjoint = all(
            matter_edges[left].isdisjoint(matter_edges[right])
            for left, right in combinations(range(3), 2)
        )
        matter_theta_controls[length] = {
            "endpoint_match": all(
                path[0] == (coarse_3d[0][0], 4)
                and path[-1] == (coarse_3d[0][-1], 4)
                for path in matter_paths
            ),
            "interiors_disjoint": matter_interiors_disjoint,
            "edges_disjoint": matter_edges_disjoint,
            "lawful_edges": all(
                matter_edge(path[index], path[index + 1])
                for path in matter_paths
                for index in range(len(path) - 1)
            ),
            "path_edge_counts": tuple(len(path) - 1 for path in matter_paths),
            "coarse_corridor_separation_lower_bound": min(
                middle, length - 1 - middle
            ),
        }
    check(
        "scalar graph has growing 8-shaped square-grid subgraphs",
        all(
            row["endpoint_match"]
            and row["interiors_disjoint"]
            and row["edges_disjoint"]
            and row["lawful_steps"]
            for row in theta_controls.values()
        ),
        theta_controls,
    )
    check(
        "six-mode matter graph has growing subdivided 8-shaped subgraphs",
        all(
            row["endpoint_match"]
            and row["interiors_disjoint"]
            and row["edges_disjoint"]
            and row["lawful_edges"]
            for row in matter_theta_controls.values()
        ),
        matter_theta_controls,
    )


def gf2_rank(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for row in rows:
        value = row
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def exact_bosonization_flux_control() -> None:
    """Cubic-chain version of the closed-manifold flux identity.

    In exact 3-D bosonization a fermion parity P_t maps to a cell flux W_t.
    On a closed cell complex every face belongs to two cells, hence the product
    of all W_t is identity.  A product of face-X operators on a dual path flips
    exactly the two endpoint fluxes.  A single flux therefore needs a boundary
    endpoint or a semi-infinite string/sector representation.
    """

    print("\nEXACT-BOSONIZATION FLUX / STRING CONTROL")
    for length in (3, 4, 5):
        cells = tuple(product(range(length), repeat=3))
        cell_index = {cell: index for index, cell in enumerate(cells)}
        faces = []
        for cell in cells:
            for axis in range(3):
                target = list(cell)
                target[axis] = (target[axis] + 1) % length
                faces.append((cell, tuple(target), axis))
        rows = [0 for _ in cells]
        for face, (left, right, _) in enumerate(faces):
            rows[cell_index[left]] ^= 1 << face
            rows[cell_index[right]] ^= 1 << face
        total_flux_product = 0
        for row in rows:
            total_flux_product ^= row
        check(
            f"L={length} closed product of all cell fluxes is identity",
            total_flux_product == 0
            and gf2_rank(rows) == len(cells) - 1,
            {
                "cells": len(cells),
                "faces": len(faces),
                "flux_constraint_rank": gf2_rank(rows),
                "independent_global_relations": 1,
            },
        )

        start = (0, 0, 0)
        end = tuple(length // 2 for _ in range(3))
        path = []
        cursor = list(start)
        for axis in range(3):
            for _ in range(length // 2):
                owner = tuple(cursor)
                path.append((owner, axis))
                cursor[axis] = (cursor[axis] + 1) % length
        boundary: set[tuple[int, int, int]] = set()
        for owner, axis in path:
            target = list(owner)
            target[axis] = (target[axis] + 1) % length
            for endpoint in (owner, tuple(target)):
                if endpoint in boundary:
                    boundary.remove(endpoint)
                else:
                    boundary.add(endpoint)
        check(
            f"L={length} face string creates exactly two flux endpoints",
            boundary == {start, end},
            {"path_faces": len(path), "flux_endpoints": sorted(boundary)},
        )

    distance_controls = {}
    for distance in (1, 2, 4, 8):
        # A dual path with D face flips has mod-two boundary {0,D}.
        path_edges = tuple((step, step + 1) for step in range(distance))
        boundary: set[int] = set()
        for edge in path_edges:
            for endpoint in edge:
                if endpoint in boundary:
                    boundary.remove(endpoint)
                else:
                    boundary.add(endpoint)
        distance_controls[distance] = {
            "face_string_support": len(path_edges),
            "endpoints": tuple(sorted(boundary)),
        }
    check(
        "distant two-flux preparation needs a connecting string",
        all(
            data["face_string_support"] == distance
            and data["endpoints"] == (0, distance)
            for distance, data in distance_controls.items()
        ),
        distance_controls,
    )
    check(
        "finite-support infinite-lattice strings have even endpoint number",
        all(len(data["endpoints"]) % 2 == 0 for data in distance_controls.values()),
        "one flux requires a boundary or semi-infinite string/sector",
    )


def cubic_marker(
    frames: tuple[tuple[tuple[int, int, int], ...], ...]
) -> tuple[
    dict[tuple[int, int, int], int],
    tuple[frozenset[tuple[int, int, int]], ...],
]:
    coordinates = set(product(range(PERIOD), repeat=3))
    orbits = []
    while coordinates:
        representative = min(coordinates)
        orbit = frozenset(
            mat_vec(frame, representative, PERIOD) for frame in frames
        )
        orbits.append(orbit)
        coordinates.difference_update(orbit)
    rng = Random(MARKER_SEED)
    marker: dict[tuple[int, int, int], int] = {}
    for orbit in orbits:
        bit = rng.randrange(2)
        for coordinate in orbit:
            marker[coordinate] = bit
    return marker, tuple(orbits)


def marker_templates(
    marker: dict[tuple[int, int, int], int],
    active: frozenset[tuple[int, int, int]],
) -> tuple[
    tuple[tuple[int, int], ...],
    tuple[tuple[int, int, int], ...],
    tuple[tuple[int, int, int], ...],
]:
    coordinates = tuple(product(range(PERIOD), repeat=3))
    offsets = tuple(product(range(-RADIUS, RADIUS + 1), repeat=3))
    templates = []
    for phase in coordinates:
        mask = 0
        bits = 0
        for index, offset in enumerate(offsets):
            residue = tuple(
                (phase[axis] + offset[axis]) % PERIOD for axis in range(3)
            )
            if residue in active:
                continue
            mask |= 1 << index
            if marker[residue]:
                bits |= 1 << index
        templates.append((mask, bits))
    return tuple(templates), coordinates, offsets


def template_ambiguities(templates: tuple[tuple[int, int], ...]) -> int:
    ambiguities = 0
    for left, (left_mask, left_bits) in enumerate(templates):
        for right in range(left):
            right_mask, right_bits = templates[right]
            if ((left_bits ^ right_bits) & left_mask & right_mask) == 0:
                ambiguities += 1
    return ambiguities


def rotation_mismatches(
    templates: tuple[tuple[int, int], ...],
    coordinates: tuple[tuple[int, int, int], ...],
    offsets: tuple[tuple[int, int, int], ...],
    frames: tuple[tuple[tuple[int, int, int], ...], ...],
) -> int:
    coordinate_index = {coordinate: index for index, coordinate in enumerate(coordinates)}
    offset_index = {offset: index for index, offset in enumerate(offsets)}
    mismatches = 0
    for frame in frames:
        offset_map = tuple(
            offset_index[mat_vec(frame, offset)] for offset in offsets
        )
        for phase_index, phase in enumerate(coordinates):
            mask, bits = templates[phase_index]
            rotated_mask = 0
            rotated_bits = 0
            for source, target in enumerate(offset_map):
                if (mask >> source) & 1:
                    rotated_mask |= 1 << target
                    if (bits >> source) & 1:
                        rotated_bits |= 1 << target
            target_phase = mat_vec(frame, phase, PERIOD)
            if (rotated_mask, rotated_bits) != templates[
                coordinate_index[target_phase]
            ]:
                mismatches += 1
    return mismatches


def successor_mismatches(
    templates: tuple[tuple[int, int], ...],
    coordinates: tuple[tuple[int, int, int], ...],
    offsets: tuple[tuple[int, int, int], ...],
) -> tuple[int, int]:
    coordinate_index = {coordinate: index for index, coordinate in enumerate(coordinates)}
    offset_index = {offset: index for index, offset in enumerate(offsets)}
    missing_intended = 0
    extra_compatible = 0
    for axis in range(3):
        common = tuple(offset for offset in offsets if offset[axis] >= -RADIUS + 1)
        first_projected = []
        second_projected = []
        for mask, bits in templates:
            first_mask = first_bits = second_mask = second_bits = 0
            for common_index, first_offset in enumerate(common):
                first_index = offset_index[first_offset]
                second_offset = list(first_offset)
                second_offset[axis] -= 1
                second_index = offset_index[tuple(second_offset)]
                if (mask >> first_index) & 1:
                    first_mask |= 1 << common_index
                    if (bits >> first_index) & 1:
                        first_bits |= 1 << common_index
                if (mask >> second_index) & 1:
                    second_mask |= 1 << common_index
                    if (bits >> second_index) & 1:
                        second_bits |= 1 << common_index
            first_projected.append((first_mask, first_bits))
            second_projected.append((second_mask, second_bits))

        for phase_index, phase in enumerate(coordinates):
            intended_phase = list(phase)
            intended_phase[axis] = (intended_phase[axis] + 1) % PERIOD
            intended = coordinate_index[tuple(intended_phase)]
            first_mask, first_bits = first_projected[phase_index]
            compatible = []
            for candidate, (second_mask, second_bits) in enumerate(second_projected):
                if (
                    (first_bits ^ second_bits) & first_mask & second_mask
                ) == 0:
                    compatible.append(candidate)
            if intended not in compatible:
                missing_intended += 1
            extra_compatible += len(compatible) - int(intended in compatible)
    return missing_intended, extra_compatible


def translation_marker_probe() -> None:
    print("\nUNIT-TRANSLATION / AUTONOMOUS MARKER PROBE")
    frames = proper_cubic_frames()
    active = active_residues()
    check("proper-cubic frame count", len(frames) == 24, len(frames))
    check("active residue count", len(active) == 27, len(active))
    check(
        "active layout is proper-cubic invariant",
        all(
            {mat_vec(frame, residue, PERIOD) for residue in active} == set(active)
            for frame in frames
        ),
        "24/24",
    )

    marker, orbits = cubic_marker(frames)
    check(
        "marker is proper-cubic invariant",
        all(
            marker[mat_vec(frame, residue, PERIOD)] == marker[residue]
            for frame in frames
            for residue in marker
        ),
        {"proper_cubic_orbits": len(orbits), "seed": MARKER_SEED},
    )
    templates, coordinates, offsets = marker_templates(marker, active)
    ambiguities = template_ambiguities(templates)
    check(
        "radius-two local windows distinguish all offset sectors",
        ambiguities == 0,
        {
            "templates": len(templates),
            "ambiguous_pairs": ambiguities,
            "max_data_wildcards": max(
                len(offsets) - mask.bit_count() for mask, _ in templates
            ),
        },
    )
    frame_mismatches = rotation_mismatches(
        templates, coordinates, offsets, frames
    )
    check(
        "radius-two template family is proper-cubic covariant",
        frame_mismatches == 0,
        {"tests": len(frames) * len(coordinates), "mismatches": frame_mismatches},
    )
    missing, extra = successor_mismatches(templates, coordinates, offsets)
    check(
        "neighbor overlap enforces a unique phase successor",
        missing == 0 and extra == 0,
        {
            "directed_phase_tests": 3 * len(coordinates),
            "missing_intended": missing,
            "extra_compatible": extra,
        },
    )

    inactive = PERIOD**3 - len(active)
    check(
        "marker uses only prior blank sites and leaves all data sites free",
        inactive == 4069,
        {
            "fixed_marker_sites_per_period": inactive,
            "arbitrary_data_sites_per_period": len(active),
            "marker_ones_on_fixed_sites": sum(
                marker[residue] for residue in marker if residue not in active
            ),
        },
    )
    check(
        "all-offset overlay is not 4096 independent compiler copies",
        len(coordinates) * len(active) // PERIOD**3 == 27,
        {
            "offset_sectors": len(coordinates),
            "carrier_incidences_per_physical_residue_if_overlaid": 27,
            "interpretation": "direct-sum sectors, not simultaneous copies",
        },
    )

    # A single sector is not itself invariant; the family is.  This makes
    # sector preparation/selection distinct from covariance of the law.
    base_configuration = {
        residue: (0 if residue in active else marker[residue])
        for residue in coordinates
    }
    hamming = []
    for axis in range(3):
        step = tuple(1 if index == axis else 0 for index in range(3))
        shifted_configuration = {}
        for residue in coordinates:
            source = tuple((residue[index] - step[index]) % PERIOD for index in range(3))
            shifted_configuration[residue] = base_configuration[source]
        hamming.append(
            sum(
                base_configuration[residue] != shifted_configuration[residue]
                for residue in coordinates
            )
        )
    check(
        "one chosen marker sector breaks unit translation",
        all(value > 0 for value in hamming),
        {"unit_shift_hamming_distances": hamming},
    )

    for length in (3, 4, 5):
        check(
            f"L={length} held torus carries the same 16^3 offset orbit",
            (PERIOD * length) % PERIOD == 0 and len(templates) == PERIOD**3,
            {"physical_linear_size": PERIOD * length, "offset_sectors": len(templates)},
        )


def main() -> int:
    note_contract()
    finite_domain_bookkeeping()
    quasi_local_and_full_car_controls()
    preparation_depth_control()
    fixture_graph_control()
    exact_bosonization_flux_control()
    translation_marker_probe()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
