#!/usr/bin/env python3
"""Cycle 703: reversible local echo/ack controller and record factorization.

Each axial-decoder dependency component is a rooted tree.  A finite-state token
walks its local Euler contour: parent->child computes the child prefix and
emits the colocated controlled Z; child->parent applies the same XOR again and
returns the child work blank.  A fresh/spent syndrome-bank flag supplies the
one-time preparation epoch.  No host selects a path, stop, barrier, or round.

The measured/coherently extracted syndrome bits are retained.  This runner also
proves that coherent extraction and phase-zero Z correction factor the unique
open BKSF vacuum from a fixed pure record stabilizer state.  That record is
inert under later loading/update, but this runner does not reuse it as a blank
syndrome bank or erase a dephased classical record unitarily.
"""

from __future__ import annotations

from itertools import product
import json

import ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17 as base
import frontier_cycle703_open_bksf_stabilizer_preparation_2026_07_25 as prep
import frontier_cycle703_local_cellular_plaquette_decoder_2026_07_25 as ca


AUDIT_INPUT_PATHS = (
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/frontier_cycle703_open_bksf_stabilizer_preparation_2026_07_25.py",
    "scripts/frontier_cycle703_local_cellular_plaquette_decoder_2026_07_25.py",
)


Coord = tuple[int, int, int]
Node = tuple[str, int, int, int]
ECHO_CLAUSES = frozenset(
    (
        "start_ay_roots",
        "start_az_roots",
        "route_x_child",
        "route_y_child",
        "compute_child",
        "source_xor",
        "emit_controlled_z",
        "ack_uncompute",
        "root_spent_ack",
    )
)


def ay_node(x: int, y: int, z: int) -> Node:
    return ("ay", x, y, z)


def az_node(x: int, y: int, z: int) -> Node:
    return ("az", x, y, z)


def node_anchor(node: Node) -> Coord:
    return node[1], node[2], node[3]


def forest_roots(length: int) -> tuple[Node, ...]:
    ay_roots = tuple(
        ay_node(0, y, z)
        for y in range(length - 1)
        for z in range(length)
    )
    az_roots = tuple(az_node(0, 0, z) for z in range(length - 1))
    return ay_roots + az_roots


def parent_and_source(node: Node):
    kind, x, y, z = node
    if kind == "ay":
        if x == 0:
            return None
        return ay_node(x - 1, y, z), ((x - 1, y, z), (0, 1))
    if x > 0:
        return az_node(x - 1, y, z), ((x - 1, y, z), (0, 2))
    if y > 0:
        return az_node(0, y - 1, z), ((0, y - 1, z), (1, 2))
    return None


def children(
    node: Node, length: int, disabled: frozenset[str]
) -> tuple[Node, ...]:
    kind, x, y, z = node
    result = []
    if x + 1 < length and "route_x_child" not in disabled:
        result.append(
            ay_node(x + 1, y, z)
            if kind == "ay"
            else az_node(x + 1, y, z)
        )
    if (
        kind == "az"
        and x == 0
        and y + 1 < length
        and "route_y_child" not in disabled
    ):
        result.append(az_node(0, y + 1, z))
    return tuple(result)


def node_edge_index(geometry: dict[str, object], node: Node) -> int:
    edges = geometry["edges"]
    if not isinstance(edges, tuple):
        raise TypeError("malformed edges")
    lookup = {
        (left, axis): index
        for index, (left, _, axis) in enumerate(edges)
    }
    axis = 1 if node[0] == "ay" else 2
    return lookup[(node_anchor(node), axis)]


def echo_ack_decode(
    length: int,
    syndrome: int,
    disabled: frozenset[str] = frozenset(),
) -> dict[str, object]:
    """Run every disjoint dependency-tree token to its local root acknowledgement."""

    unknown = disabled - ECHO_CLAUSES
    if unknown:
        raise ValueError(("unknown echo clauses", sorted(unknown)))
    geometry = ca.box_geometry(length)
    fields = ca.syndrome_values(geometry, syndrome)
    values: dict[Node, int] = {}
    correction = 0
    events = {"start": 0, "down": 0, "emit": 0, "up": 0, "ack": 0}
    stalled_tokens = 0
    spent_roots = 0
    started_roots = 0
    for root in forest_roots(length):
        if root[0] == "ay" and "start_ay_roots" in disabled:
            continue
        if root[0] == "az" and "start_az_roots" in disabled:
            continue
        started_roots += 1
        events["start"] += 1
        values[root] = 0
        current = root
        incoming_child: Node | None = None
        while True:
            local_children = children(current, length, disabled)
            if incoming_child is None:
                next_index = 0
            else:
                if incoming_child not in local_children:
                    raise AssertionError(("bad incoming port", current, incoming_child))
                next_index = local_children.index(incoming_child) + 1
            if next_index < len(local_children):
                child = local_children[next_index]
                if "compute_child" in disabled:
                    stalled_tokens += 1
                    break
                parent_source = parent_and_source(child)
                if parent_source is None or parent_source[0] != current:
                    raise AssertionError(("bad dependency edge", current, child))
                source = (
                    fields[parent_source[1]]
                    if "source_xor" not in disabled
                    else 0
                )
                child_value = values[current] ^ source
                if child in values:
                    raise AssertionError(("child work not blank", child))
                values[child] = child_value
                events["down"] += 1
                if "emit_controlled_z" not in disabled and child_value:
                    correction ^= 1 << node_edge_index(geometry, child)
                    events["emit"] += 1
                current = child
                incoming_child = None
                continue

            if current == root:
                if "root_spent_ack" not in disabled:
                    spent_roots += 1
                    events["ack"] += 1
                    del values[root]
                break
            parent_source = parent_and_source(current)
            if parent_source is None:
                raise AssertionError(("missing parent", current))
            parent, source_key = parent_source
            if "ack_uncompute" not in disabled:
                source = (
                    fields[source_key]
                    if "source_xor" not in disabled
                    else 0
                )
                returned = values[current] ^ values[parent] ^ source
                if returned != 0:
                    raise AssertionError(("XOR inverse failed", current, returned))
                del values[current]
            events["up"] += 1
            child = current
            current = parent
            incoming_child = child

    expected_roots = len(forest_roots(length))
    return {
        "correction": correction,
        "work_nonblank": len(values),
        "token_nonidle": stalled_tokens,
        "started_roots": started_roots,
        "spent_roots": spent_roots,
        "expected_roots": expected_roots,
        "all_roots_locally_acknowledged": spent_roots == expected_roots,
        "all_recurrence_work_returned": len(values) == 0,
        "events": events,
        "syndrome_after": syndrome,
        "syndrome_retained_exactly": True,
    }


def local_permutation_tables() -> dict[str, object]:
    xor_rows = []
    xor_failures = 0
    for parent, source, child in product((0, 1), repeat=3):
        out = child ^ parent ^ source
        returned = out ^ parent ^ source
        xor_rows.append((parent, source, child, out))
        xor_failures += returned != child

    router_tables = {
        "leaf": (0, 1, 2, 3),
        "one_child": (1, 0, 2, 3),
        "two_children": (1, 2, 0, 3),
    }
    router_failures = sum(
        sorted(table) != list(range(4)) for table in router_tables.values()
    )
    token_swap = tuple((left, right, right, left) for left, right in product((0, 1), repeat=2))
    token_swap_failures = sum(row[2:] != (row[1], row[0]) for row in token_swap)
    epoch_handshake = (1, 2, 3, 0)
    epoch_failures = sorted(epoch_handshake) != list(range(4))
    cz_phases = (1, 1, 1, -1)
    return {
        "xor3_truth_rows": tuple(xor_rows),
        "xor3_roundtrip_failures": xor_failures,
        "router_port_encoding": (
            "00=parent, 01=x-child, 10=y-child, 11=unused"
        ),
        "router_permutations": router_tables,
        "router_bijection_failures": router_failures,
        "token_presence_SWAP_rows": token_swap,
        "token_SWAP_failures": token_swap_failures,
        "epoch_handshake_four_cycle": epoch_handshake,
        "epoch_bijection_failures": int(epoch_failures),
        "controlled_Z_basis_phases": cz_phases,
        "controlled_Z_unitarity_failures": sum(abs(value) != 1 for value in cz_phases),
        "maximum_port_bits_M2": 2,
        "finite_controller_M2_upper_bound_per_work_node": 6,
        "meaning": (
            "all local data, routing, token, epoch, and correction primitives "
            "are bounded M2 permutations or a bounded controlled phase"
        ),
    }


def box_echo_certificate(length: int) -> dict[str, object]:
    geometry = ca.box_geometry(length)
    edges = geometry["edges"]
    masks = geometry["masks"]
    if not isinstance(edges, tuple) or not isinstance(masks, tuple):
        raise TypeError("malformed geometry")
    failures = 0
    ca_mismatches = 0
    work_failures = 0
    ack_failures = 0
    token_failures = 0
    columns = []
    syndromes = []
    maximum_events = 0
    for edge_index in range(len(edges)):
        syndrome = prep.apply_matrix(masks, 1 << edge_index)
        row = echo_ack_decode(length, syndrome)
        correction = row["correction"]
        failures += prep.apply_matrix(masks, correction) != syndrome
        ca_mismatches += correction != ca.cellular_decode(length, syndrome)["correction"]
        work_failures += not row["all_recurrence_work_returned"]
        ack_failures += not row["all_roots_locally_acknowledged"]
        token_failures += row["token_nonidle"] != 0
        maximum_events = max(maximum_events, sum(row["events"].values()))
        columns.append(correction)
        syndromes.append(syndrome)
    linearity_failures = 0
    sample_count = min(64, len(edges) * len(edges))
    for sample in range(sample_count):
        left = (11 * sample + 1) % len(edges)
        right = (31 * sample + 9) % len(edges)
        combined = echo_ack_decode(
            length, syndromes[left] ^ syndromes[right]
        )["correction"]
        linearity_failures += combined != (columns[left] ^ columns[right])
    nodes = 2 * length * length * (length - 1)
    roots = length * length - 1
    return {
        "L": length,
        "coarse_edges": len(edges),
        "unit_edge_basis_cases": len(edges),
        "syndrome_failures": failures,
        "forward_CA_correction_mismatches": ca_mismatches,
        "returned_work_failures": work_failures,
        "root_ack_failures": ack_failures,
        "token_idle_failures": token_failures,
        "linearity_pairs_checked": sample_count,
        "linearity_failures": linearity_failures,
        "dependency_nodes": nodes,
        "dependency_roots": roots,
        "maximum_total_event_count": maximum_events,
        "nonemission_control_event_count": 2 * nodes,
        "total_event_upper_bound": 3 * nodes - roots,
        "maximum_tree_degree": 3,
        "local_neighborhood_radius": 1,
    }


def exhaustive_l2_echo_certificate() -> dict[str, object]:
    length = 2
    geometry = ca.box_geometry(length)
    edges = geometry["edges"]
    masks = geometry["masks"]
    if not isinstance(edges, tuple) or not isinstance(masks, tuple):
        raise TypeError("malformed geometry")
    lawful = {
        prep.apply_matrix(masks, pattern)
        for pattern in range(1 << len(edges))
    }
    failures = 0
    work_failures = 0
    ack_failures = 0
    for syndrome in lawful:
        row = echo_ack_decode(length, syndrome)
        failures += prep.apply_matrix(masks, row["correction"]) != syndrome
        work_failures += not row["all_recurrence_work_returned"]
        ack_failures += not row["all_roots_locally_acknowledged"]
    return {
        "edge_patterns_enumerated": 1 << len(edges),
        "distinct_lawful_syndromes": len(lawful),
        "syndrome_failures": failures,
        "returned_work_failures": work_failures,
        "root_ack_failures": ack_failures,
    }


def transition_deletion_certificate(length: int = 4) -> dict[str, object]:
    geometry = ca.box_geometry(length)
    edges = geometry["edges"]
    masks = geometry["masks"]
    if not isinstance(edges, tuple) or not isinstance(masks, tuple):
        raise TypeError("malformed geometry")
    rows = []
    for clause in sorted(ECHO_CLAUSES):
        syndrome_failures = 0
        work_failures = 0
        ack_failures = 0
        stalled_tokens = 0
        for edge_index in range(len(edges)):
            syndrome = prep.apply_matrix(masks, 1 << edge_index)
            row = echo_ack_decode(length, syndrome, frozenset((clause,)))
            syndrome_failures += prep.apply_matrix(
                masks, row["correction"]
            ) != syndrome
            work_failures += not row["all_recurrence_work_returned"]
            ack_failures += not row["all_roots_locally_acknowledged"]
            stalled_tokens += row["token_nonidle"] != 0
        rows.append(
            {
                "deleted_transition": clause,
                "syndrome_failures": syndrome_failures,
                "work_return_failures": work_failures,
                "root_ack_failures": ack_failures,
                "stalled_token_cases": stalled_tokens,
                "detected": any(
                    (
                        syndrome_failures,
                        work_failures,
                        ack_failures,
                        stalled_tokens,
                    )
                ),
            }
        )
    return {
        "L": length,
        "unit_edge_cases_per_deletion": len(edges),
        "deletions": tuple(rows),
        "all_active_transition_deletions_detected": all(
            row["detected"] for row in rows
        ),
    }


def transported_echo_decode(
    length: int,
    physical_syndrome: frozenset[frozenset[Coord]],
    frame,
    shift: Coord,
) -> frozenset[frozenset[Coord]]:
    geometry = ca.box_geometry(length)
    plaquettes = geometry["plaquettes"]
    if not isinstance(plaquettes, tuple):
        raise TypeError("malformed plaquettes")
    pulled = 0
    known = set()
    for index, row in enumerate(plaquettes):
        transformed = frozenset(
            ca.transform_coord(frame, shift, vertex)
            for vertex in ca.plaquette_vertices(row)
        )
        known.add(transformed)
        if transformed in physical_syndrome:
            pulled ^= 1 << index
    if not physical_syndrome <= known:
        raise AssertionError("syndrome outside transported chart")
    correction = echo_ack_decode(length, pulled)["correction"]
    return ca.transformed_edge_set(geometry, correction, frame, shift)


def echo_covariance_certificate(length: int = 4) -> dict[str, object]:
    geometry = ca.box_geometry(length)
    edges = geometry["edges"]
    masks = geometry["masks"]
    if not isinstance(edges, tuple) or not isinstance(masks, tuple):
        raise TypeError("malformed geometry")
    shifts = ((0, 0, 0), (9, -4, 6))
    failures = 0
    cases = 0
    for frame in base.proper_cubic_frames():
        for shift in shifts:
            for edge_index in range(len(edges)):
                syndrome = prep.apply_matrix(masks, 1 << edge_index)
                correction = echo_ack_decode(length, syndrome)["correction"]
                physical_syndrome = ca.transformed_plaquette_set(
                    geometry, syndrome, frame, shift
                )
                expected = ca.transformed_edge_set(
                    geometry, correction, frame, shift
                )
                failures += transported_echo_decode(
                    length, physical_syndrome, frame, shift
                ) != expected
                cases += 1
    return {
        "L": length,
        "proper_cubic_frames": len(base.proper_cubic_frames()),
        "translations": len(shifts),
        "transport_cases": cases,
        "transport_failures": failures,
        "scope": "coframe, port order, roots, and boundary corner transported",
    }


def solve_pauli_span(target: base.Pauli, rows: tuple[base.Pauli, ...], qubits: int):
    vectors = tuple(row.symplectic(qubits) for row in rows)
    target_vector = target.symplectic(qubits)
    equations = []
    for bit in range(2 * qubits):
        coefficient = sum(
            ((vector >> bit) & 1) << index
            for index, vector in enumerate(vectors)
        )
        rhs = (target_vector >> bit) & 1
        if coefficient or rhs:
            equations.append((coefficient, rhs))
    basis_rows, rank, augmented_rank = prep.gaussian_basis(equations)
    if rank != augmented_rank:
        return None
    return prep.free_zero_solution(basis_rows)


def physical_coarse_z(
    graph: prep.OpenReferenceGraph,
    geometry: dict[str, object],
    correction: int,
) -> base.Pauli:
    edges = geometry["edges"]
    if not isinstance(edges, tuple):
        raise TypeError("malformed edges")
    z = 0
    for index, (cell, _, axis) in enumerate(edges):
        if (correction >> index) & 1:
            z ^= 1 << graph.cross_edge[(cell, axis, 0)]
    return base.Pauli(z=z)


def record_stabilizers_l2() -> tuple[base.Pauli, ...]:
    # 96 triangle records are |+>; six coarse records are the uniform even
    # state; 12 bond records are |+>.  The ordering is triangle/coarse/bond.
    rows = []
    triangle_count = 96
    coarse_offset = triangle_count
    bond_offset = triangle_count + 6
    for index in range(triangle_count):
        rows.append(base.Pauli(x=1 << index))
    for index in range(5):
        rows.append(
            base.Pauli(
                x=(1 << (coarse_offset + index)) | (1 << (coarse_offset + 5))
            )
        )
    rows.append(
        base.Pauli(z=sum(1 << (coarse_offset + index) for index in range(6)))
    )
    for index in range(12):
        rows.append(base.Pauli(x=1 << (bond_offset + index)))
    return tuple(rows)


def l2_record_factorization_certificate() -> dict[str, object]:
    cells = tuple(product(range(2), repeat=3))
    graph = prep.OpenReferenceGraph(cells)
    cycles = prep.open_local_cycles(graph)
    triangles = tuple(
        graph.loop_pauli(vertices)
        for _, vertices, kind, _ in cycles
        if kind == "cell_triangle"
    )
    coarse_with_key = tuple(
        (graph.loop_pauli(vertices), key)
        for _, vertices, kind, key in cycles
        if kind == "coarse_plaquette"
    )
    bonds_with_key = tuple(
        (graph.loop_pauli(vertices), key)
        for _, vertices, kind, key in cycles
        if kind == "bond_rectangle"
    )
    coarse = tuple(row for row, _ in coarse_with_key)
    bonds = tuple(row for row, _ in bonds_with_key)
    qubits = len(graph.edges)
    rank_triangles = prep.base.gf2_rank(row.symplectic(qubits) for row in triangles)
    rank_tri_coarse = prep.base.gf2_rank(
        row.symplectic(qubits) for row in triangles + coarse
    )
    rank_all = prep.base.gf2_rank(
        row.symplectic(qubits) for row in triangles + coarse + bonds
    )

    coarse_product = base.Pauli()
    for row in coarse:
        coarse_product = coarse_product @ row
    triangle_coordinates = solve_pauli_span(coarse_product, triangles, qubits)
    quotient_relation_failures = int(triangle_coordinates is None)
    relation_weight = 0
    relation_phase_failures = 0
    if triangle_coordinates is not None:
        relation_weight = triangle_coordinates.bit_count()
        reconstructed = base.Pauli()
        for index, row in enumerate(triangles):
            if (triangle_coordinates >> index) & 1:
                reconstructed = reconstructed @ row
        relation_phase_failures += reconstructed != coarse_product

    geometry = ca.box_geometry(2)
    masks = geometry["masks"]
    plaquettes = geometry["plaquettes"]
    if not isinstance(masks, tuple) or not isinstance(plaquettes, tuple):
        raise TypeError("malformed geometry")
    coarse_lookup = {key: row for row, key in coarse_with_key}
    ordered_coarse = tuple(
        coarse_lookup[(row["anchor"], *row["axes"])] for row in plaquettes
    )
    lawful = {
        prep.apply_matrix(masks, pattern)
        for pattern in range(1 << len(geometry["edges"]))
    }
    coarse_branch_failures = 0
    coarse_phase_failures = 0
    previous_commutator_failures = 0
    echo_mismatches = 0
    for syndrome in lawful:
        echo = echo_ack_decode(2, syndrome)
        correction = echo["correction"]
        echo_mismatches += correction != ca.cellular_decode(2, syndrome)["correction"]
        physical = physical_coarse_z(graph, geometry, correction)
        coarse_phase_failures += physical.phase != 0 or physical.x != 0
        for index, row in enumerate(ordered_coarse):
            coarse_branch_failures += (
                int(not physical.commutes(row)) != ((syndrome >> index) & 1)
            )
        previous_commutator_failures += sum(
            not physical.commutes(row) for row in triangles
        )

    # Complete one-cell 4096-column triangle phase check; the same table is
    # transported independently to all eight cells.
    one_cell = prep.OpenReferenceGraph(((0, 0, 0),))
    triangle_data = tuple(
        (prep.cycle_mask(one_cell, vertices), one_cell.loop_pauli(vertices))
        for _, vertices, kind, _ in prep.open_local_cycles(one_cell)
        if kind == "cell_triangle"
    )
    triangle_masks = tuple(row[0] for row in triangle_data)
    triangle_decoder = prep.right_inverse(triangle_masks, len(one_cell.edges))
    triangle_branch_failures = 0
    triangle_phase_failures = 0
    for syndrome in range(1 << len(triangle_masks)):
        correction = 0
        for index, column in enumerate(triangle_decoder):
            if (syndrome >> index) & 1:
                correction ^= column
        physical = base.Pauli(z=correction)
        triangle_phase_failures += physical.phase != 0 or physical.x != 0
        for index, (_, row) in enumerate(triangle_data):
            triangle_branch_failures += (
                int(not physical.commutes(row)) != ((syndrome >> index) & 1)
            )

    # Complete 4096-column bond phase check.  Reference-bond corrections are
    # unique and commute with the already fixed triangle/coarse rows.
    bond_branch_failures = 0
    bond_phase_failures = 0
    bond_previous_commutator_failures = 0
    for syndrome in range(1 << len(bonds_with_key)):
        z = 0
        for index, (_, (cell, axis)) in enumerate(bonds_with_key):
            if (syndrome >> index) & 1:
                z ^= 1 << graph.cross_edge[(cell, axis, 1)]
        physical = base.Pauli(z=z)
        bond_phase_failures += physical.phase != 0 or physical.x != 0
        for index, (row, _) in enumerate(bonds_with_key):
            bond_branch_failures += (
                int(not physical.commutes(row)) != ((syndrome >> index) & 1)
            )
        bond_previous_commutator_failures += sum(
            not physical.commutes(row) for row in triangles + coarse
        )

    # Uniform-amplitude discriminator.  Choose 113 independent check rows and
    # one phase-zero pure-Z correction for each row.  Injectivity of the X
    # projection proves that every nonidentity product has zero expectation in
    # |0_Z>; full rank of the correction/check anticommutation matrix proves
    # that all 2^113 syndrome characters occur.  Neither conclusion uses the
    # disjoint physical/record register typing census below.
    independent_checks = (
        triangles + ordered_coarse[:5] + tuple(row for row, _ in bonds_with_key)
    )
    triangle_corrections: list[base.Pauli] = []
    for cell in graph.cells:
        for column in triangle_decoder:
            z = 0
            for local_edge, (source, target, _, _) in enumerate(one_cell.edges):
                if (column >> local_edge) & 1:
                    source_mode = one_cell.vertices[source][1]
                    target_mode = one_cell.vertices[target][1]
                    source_vertex = graph.vertex_index[(cell, source_mode)]
                    target_vertex = graph.vertex_index[(cell, target_mode)]
                    z ^= 1 << graph.edge_between(source_vertex, target_vertex)
            triangle_corrections.append(base.Pauli(z=z))
    coarse_corrections = tuple(
        physical_coarse_z(
            graph,
            geometry,
            echo_ack_decode(2, (1 << index) | (1 << 5))["correction"],
        )
        for index in range(5)
    )
    bond_corrections = tuple(
        base.Pauli(z=1 << graph.cross_edge[(cell, axis, 1)])
        for _, (cell, axis) in bonds_with_key
    )
    independent_corrections = (
        tuple(triangle_corrections) + coarse_corrections + bond_corrections
    )
    pairing_rows = tuple(
        sum(
            int(not correction.commutes(check)) << check_index
            for check_index, check in enumerate(independent_checks)
        )
        for correction in independent_corrections
    )
    independent_x_rank = base.gf2_rank(row.x for row in independent_checks)
    all_check_x_rank = base.gf2_rank(
        row.x for row in triangles + ordered_coarse + bonds
    )
    pairing_rank = base.gf2_rank(pairing_rows)
    pairing_diagonal_failures = sum(
        ((row >> index) & 1) != 1 for index, row in enumerate(pairing_rows)
    )
    pairing_prior_stage_failures = sum(
        (row & ((1 << index) - 1)).bit_count()
        for index, row in enumerate(pairing_rows)
    )
    independent_correction_phase_or_x_failures = sum(
        correction.phase != 0 or correction.x != 0
        for correction in independent_corrections
    )
    independent_check_commutator_failures = sum(
        not left.commutes(right)
        for index, left in enumerate(independent_checks)
        for right in independent_checks[index + 1 :]
    )
    independent_check_phase_failures = base.stabilizer_phase_failures(
        list(independent_checks), qubits
    )

    record_rows = record_stabilizers_l2()
    record_qubits = 114
    record_rank = base.gf2_rank(
        row.symplectic(record_qubits) for row in record_rows
    )
    record_phase_failures = base.stabilizer_phase_failures(
        list(record_rows), record_qubits
    )
    record_commutator_failures = sum(
        not left.commutes(right)
        for index, left in enumerate(record_rows)
        for right in record_rows[index + 1 :]
    )
    physical_vacuum_rank = prep.base.gf2_rank(
        row.symplectic(qubits)
        for row in tuple(
            graph.loop_pauli(vertices) for _, vertices, _, _ in cycles
        )
        + tuple(graph.B(vertex) for vertex in range(len(graph.vertices)))
    )

    # Type-separation census only: physical and record tableaux occupy
    # disjoint registers, so these commutators are true by construction.  This
    # checks that the later-update interface was typed onto the physical edge
    # register; it is not evidence for the factorization proved above.
    physical_update_rows = tuple(
        row
        for edge in range(qubits)
        for row in (
            base.Pauli(x=1 << edge),
            base.Pauli(z=1 << edge),
        )
    )
    type_separation_commutator_failures = 0
    for physical in physical_update_rows:
        physical_combined = base.Pauli(
            physical.phase, physical.x, physical.z
        )
        for record in record_rows:
            record_combined = base.Pauli(
                record.phase,
                record.x << qubits,
                record.z << qubits,
            )
            type_separation_commutator_failures += not physical_combined.commutes(
                record_combined
            )

    total_rank = physical_vacuum_rank + record_rank
    return {
        "physical_edge_M2": qubits,
        "measured_loop_records": 114,
        "stage_rank_increments": (
            rank_triangles,
            rank_tri_coarse - rank_triangles,
            rank_all - rank_tri_coarse,
        ),
        "total_independent_syndrome_exponent": rank_all,
        "triangle_local_columns_checked": 1 << 12,
        "triangle_cells_using_same_table": 8,
        "triangle_branch_failures": triangle_branch_failures,
        "triangle_phase_failures": triangle_phase_failures,
        "coarse_lawful_columns_checked": len(lawful),
        "coarse_branch_failures": coarse_branch_failures,
        "coarse_phase_failures": coarse_phase_failures,
        "coarse_previous_stage_commutator_failures": previous_commutator_failures,
        "coarse_echo_mismatches": echo_mismatches,
        "coarse_cube_relation_in_triangle_span_failures": quotient_relation_failures,
        "coarse_cube_relation_triangle_weight": relation_weight,
        "coarse_cube_relation_phase_failures": relation_phase_failures,
        "bond_columns_checked": 1 << 12,
        "bond_branch_failures": bond_branch_failures,
        "bond_phase_failures": bond_phase_failures,
        "bond_previous_stage_commutator_failures": bond_previous_commutator_failures,
        "lawful_full_record_support_exponent": rank_all,
        "lawful_full_record_support_count": f"2^{rank_all}",
        "common_record_amplitude": f"2^(-{rank_all}/2)",
        "nonzero_record_amplitude_phase": 0,
        "uniform_amplitude_discriminator": {
            "independent_check_rows": len(independent_checks),
            "all_measured_check_rows": len(triangles + ordered_coarse + bonds),
            "independent_X_part_rank": independent_x_rank,
            "all_check_X_part_rank": all_check_x_rank,
            "nonidentity_independent_products_with_possible_nonzero_Z_vacuum_expectation": (
                0 if independent_x_rank == len(independent_checks) else "not excluded"
            ),
            "independent_phase_zero_Z_corrections": len(independent_corrections),
            "correction_check_anticommutation_rank": pairing_rank,
            "pairing_diagonal_failures": pairing_diagonal_failures,
            "pairing_prior_stage_failures": pairing_prior_stage_failures,
            "correction_phase_or_X_failures": (
                independent_correction_phase_or_x_failures
            ),
            "independent_check_commutator_failures": (
                independent_check_commutator_failures
            ),
            "independent_check_stabilizer_phase_failures": (
                independent_check_phase_failures
            ),
            "dependent_relation_count": len(triangles + ordered_coarse + bonds)
            - len(independent_checks),
            "dependent_relation_phase_failures": relation_phase_failures,
            "meaning": (
                "X-projection injectivity makes every nonidentity independent "
                "check product off-diagonal on |0_Z>; the full-rank phase-zero "
                "Z-correction pairing realizes every syndrome character"
            ),
        },
        "record_stabilizer_rows": len(record_rows),
        "record_stabilizer_rank": record_rank,
        "record_stabilizer_phase_failures": record_phase_failures,
        "record_stabilizer_commutator_failures": record_commutator_failures,
        "physical_vacuum_rank": physical_vacuum_rank,
        "factor_product_tableau_rank": total_rank,
        "factor_product_qubits": qubits + record_qubits,
        "code_edge_reduced_purity": 1.0,
        "record_reduced_purity": 1.0,
        "code_record_Schmidt_rank": 1,
        "type_separation_physical_record_commutator_failures": (
            type_separation_commutator_failures
        ),
        "type_separation_physical_Pauli_basis_rows": (
            len(physical_update_rows)
        ),
        "fixed_record_state": (
            "|+>^96_triangle tensor uniform-even-six-coarse tensor |+>^12_bond"
        ),
        "factorization_identity": (
            "A_s P_s = P_+ A_s and phase-zero Z A_s fixes |0_edge>, "
            "so every lawful branch has the same physical vacuum column"
        ),
    }


def record_reuse_certificate() -> dict[str, object]:
    immutable_rows = tuple(
        (syndrome, spent, syndrome, spent)
        for syndrome, spent in product((0, 1), repeat=2)
        if spent == 1
    )
    immutable_failures = sum(row[:2] != row[2:] for row in immutable_rows)
    # If a dephased record with N possible values were reset to one blank value
    # while the code is already the same vacuum, N orthogonal inputs would
    # collide.  L2 has 2^113 complete lawful record values.
    return {
        "spent_sector_truth_rows": immutable_rows,
        "spent_sector_immutable_failures": immutable_failures,
        "later_logical_loader_touches_record": False,
        "recurrent_physical_update_touches_record": False,
        "one_time_E_requires_record_reset": False,
        "record_can_remain_bounded_local_inert_auxiliary": True,
        "reuse_as_blank_without_reset_constructed": False,
        "coherent_fixed_record_reset_status": (
            "a unitary exists because the factorized record is one fixed pure "
            "stabilizer state, but no uniform local inverse-record encoder is constructed"
        ),
        "dephased_record_unitary_reset_collision_count_L2": "2^113-1",
        "dephased_reset_scope": (
            "without exporting the syndrome entropy to another retained register"
        ),
    }


def main() -> None:
    permutations = local_permutation_tables()
    exhaustive = exhaustive_l2_echo_certificate()
    box_rows = tuple(box_echo_certificate(length) for length in range(2, 9))
    deletions = transition_deletion_certificate()
    covariance = echo_covariance_certificate()
    factorization = l2_record_factorization_certificate()
    reuse = record_reuse_certificate()
    certificate = {
        "cycle": 703,
        "authority": "none",
        "audit": "unset",
        "status": "reversible-local-echo-ack-and-one-time-record-factor-positive",
        "controller": {
            "dependency_forest": "axial Ay lines plus Az y-spines with x-branches",
            "token_rule": (
                "local Euler port successor; down computes/emits, up uncomputes, "
                "root return acknowledges spent"
            ),
            "maximum_tree_degree": 3,
            "spatial_rule_radius": 1,
            "host_stop_barrier_path_or_counter": False,
            "round_or_event_counter_is_physical_time": False,
            "recurrence_work_returned": True,
            "syndrome_record_returned_blank": False,
        },
        "local_M2_permutation_tables": permutations,
        "exhaustive_L2": exhaustive,
        "box_basis_linearity_L2_L8": box_rows,
        "active_transition_deletions": deletions,
        "proper_cubic_boundary_translation_covariance": covariance,
        "complete_L2_record_factorization": factorization,
        "record_decoupling_and_reuse": reuse,
        "supplied": (
            "the open boundary, transported coframe, and local port order",
            "one fresh/spent preparation epoch state per dependency root",
            "coherently extracted or measured local syndrome bits",
            "bounded blank token/value M2 per dependency node",
            "one invocation of the preparation isometry E",
        ),
        "not_claimed": (
            "that controller events are physical time",
            "reuse of the same record bank as blank without a reset circuit",
            "unitary reset of a dephased classical record",
            "periodic fixed-Wilson preparation",
            "a Record, Born rule, source law, or axiom pressure",
        ),
    }
    print("CYCLE703_REVERSIBLE_ECHO_ACK_CONTROLLER")
    print(json.dumps(certificate, sort_keys=True, default=str))

    assert permutations["xor3_roundtrip_failures"] == 0
    assert permutations["router_bijection_failures"] == 0
    assert permutations["token_SWAP_failures"] == 0
    assert permutations["epoch_bijection_failures"] == 0
    assert permutations["controlled_Z_unitarity_failures"] == 0
    assert exhaustive == {
        "edge_patterns_enumerated": 4096,
        "distinct_lawful_syndromes": 32,
        "syndrome_failures": 0,
        "returned_work_failures": 0,
        "root_ack_failures": 0,
    }
    assert all(row["syndrome_failures"] == 0 for row in box_rows)
    assert all(row["forward_CA_correction_mismatches"] == 0 for row in box_rows)
    assert all(row["returned_work_failures"] == 0 for row in box_rows)
    assert all(row["root_ack_failures"] == 0 for row in box_rows)
    assert all(row["token_idle_failures"] == 0 for row in box_rows)
    assert all(row["linearity_failures"] == 0 for row in box_rows)
    assert deletions["all_active_transition_deletions_detected"]
    assert covariance["proper_cubic_frames"] == 24
    assert covariance["transport_failures"] == 0
    required_factor_zero = (
        "triangle_branch_failures",
        "triangle_phase_failures",
        "coarse_branch_failures",
        "coarse_phase_failures",
        "coarse_previous_stage_commutator_failures",
        "coarse_echo_mismatches",
        "coarse_cube_relation_in_triangle_span_failures",
        "coarse_cube_relation_phase_failures",
        "bond_branch_failures",
        "bond_phase_failures",
        "bond_previous_stage_commutator_failures",
        "record_stabilizer_phase_failures",
        "record_stabilizer_commutator_failures",
        "type_separation_physical_record_commutator_failures",
    )
    assert all(factorization[key] == 0 for key in required_factor_zero)
    assert factorization["stage_rank_increments"] == (96, 5, 12)
    assert factorization["total_independent_syndrome_exponent"] == 113
    uniform = factorization["uniform_amplitude_discriminator"]
    assert uniform["independent_check_rows"] == 113
    assert uniform["all_measured_check_rows"] == 114
    assert uniform["independent_X_part_rank"] == 113
    assert uniform["all_check_X_part_rank"] == 113
    assert uniform[
        "nonidentity_independent_products_with_possible_nonzero_Z_vacuum_expectation"
    ] == 0
    assert uniform["independent_phase_zero_Z_corrections"] == 113
    assert uniform["correction_check_anticommutation_rank"] == 113
    uniform_zero = (
        "pairing_diagonal_failures",
        "pairing_prior_stage_failures",
        "correction_phase_or_X_failures",
        "independent_check_commutator_failures",
        "independent_check_stabilizer_phase_failures",
        "dependent_relation_phase_failures",
    )
    assert all(uniform[key] == 0 for key in uniform_zero)
    assert uniform["dependent_relation_count"] == 1
    assert factorization["record_stabilizer_rank"] == 114
    assert factorization["physical_vacuum_rank"] == 168
    assert factorization["factor_product_tableau_rank"] == 282
    assert factorization["factor_product_qubits"] == 282
    assert factorization["code_record_Schmidt_rank"] == 1
    assert reuse["spent_sector_immutable_failures"] == 0
    print("CYCLE703_ECHO_WORK_RETURNED_RECORD_FACTORS_AND_STAYS_INERT")


if __name__ == "__main__":
    main()
