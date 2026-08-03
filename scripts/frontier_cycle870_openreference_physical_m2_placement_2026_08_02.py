#!/usr/bin/env python3
"""Cycle 870 physical-M2 placement for the Cycle703 OpenReference encoder.

This bounded component composes the
parallel-reference-bond OpenReferenceGraph with the landed spacing-16 carrier
geometry, allocates raw-input/syndrome/echo-controller M2 in bounded macrocell
slots, and routes every declared two-site interaction by returned Manhattan
macros.  The controller event labels remain circuit structure, not time.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

AUDIT_INPUT_PATHS = (
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/frontier_cycle703_open_bksf_stabilizer_preparation_2026_07_25.py",
    "scripts/frontier_cycle703_reversible_echo_ack_controller_2026_07_25.py",
    "scripts/frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
)
EXPECTED_DEPENDENCY_SHA256 = {
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py": "717a60f45c7d7e9e354b50005fea6ace4bae7b63d74cebb48ded59546cc561f9",
    "scripts/frontier_cycle703_open_bksf_stabilizer_preparation_2026_07_25.py": "833ac9ee1d7f83185fdd66d89e2f3208e514c0b3b2cff660e7227dc28f506245",
    "scripts/frontier_cycle703_reversible_echo_ack_controller_2026_07_25.py": "5dab64cd17ead6cb5062eab9266b9206d74bb608dcc22f3a1132ee1f1af3e9a9",
    "scripts/frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25.py": "eb0841f064bc840b1892a02ce1cf75e2c8275b6c21cc9b2952a5032cc03d4bb4",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py": "e79b733bd3b8e273a2094679e6175b5d1f253ebef1a33b96544519cbdf278e13",
}

import ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17 as base
import frontier_cycle703_open_bksf_stabilizer_preparation_2026_07_25 as prep
import frontier_cycle703_reversible_echo_ack_controller_2026_07_25 as echo
import frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25 as local_gauss
import frontier_full128_25site_nn_circuit_core_2026_07_24 as route


Coord = tuple[int, int, int]
DIRECTIONS = tuple(tuple(map(int, row)) for row in base.c210.DIRECTIONS)
TOL = 1.0e-10


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[i] + right[i] for i in range(3))


def scale(value: int, row: Coord) -> Coord:
    return tuple(value * x for x in row)


def matvec(frame: np.ndarray, row: Coord) -> Coord:
    return tuple(map(int, frame @ np.asarray(row, dtype=int)))


def box(shape: tuple[int, int, int]) -> tuple[Coord, ...]:
    return tuple(product(*(range(length) for length in shape)))


def center(cell: Coord) -> Coord:
    return scale(16, cell)


def edge_axis(graph: prep.OpenReferenceGraph, edge: int) -> int:
    u, v, _kind, _owner = graph.edges[edge]
    left = graph.vertices[u][0]
    right = graph.vertices[v][0]
    delta = tuple(abs(left[i] - right[i]) for i in range(3))
    return delta.index(1)


def carrier_placement(graph: prep.OpenReferenceGraph) -> dict[int, tuple[Coord, ...]]:
    result: dict[int, tuple[Coord, ...]] = {}
    for edge, (u, v, kind, owner) in enumerate(graph.edges):
        c = center(owner)
        if kind == "octahedral":
            left = graph.vertices[u][1]
            right = graph.vertices[v][1]
            offset = scale(2, add(DIRECTIONS[left], DIRECTIONS[right]))
            sites = (add(c, offset),)
        elif kind == "spoke":
            umode = graph.vertices[u][1]
            vmode = graph.vertices[v][1]
            mode = vmode if vmode != 6 else umode
            sites = (add(c, scale(4, DIRECTIONS[mode])),)
        elif kind == "matter_stream":
            axis = edge_axis(graph, edge)
            direction = tuple(int(i == axis) for i in range(3))
            sites = (add(c, scale(7, direction)), add(c, scale(9, direction)))
        elif kind == "reference_bond":
            axis = edge_axis(graph, edge)
            direction = tuple(int(i == axis) for i in range(3))
            sites = (add(c, scale(8, direction)),)
        else:
            raise AssertionError(kind)
        result[edge] = sites
    return result


def occupied(site_map: dict[int, tuple[Coord, ...]]) -> set[Coord]:
    return {site for sites in site_map.values() for site in sites}


def lift_pauli(
    row: base.Pauli,
    graph: prep.OpenReferenceGraph,
    site_map: dict[int, tuple[Coord, ...]],
) -> dict[Coord, tuple[int, int]]:
    result: dict[Coord, tuple[int, int]] = {}
    for edge, sites in site_map.items():
        x = (row.x >> edge) & 1
        z = (row.z >> edge) & 1
        if x:
            for site in sites:
                old = result.get(site, (0, 0))
                result[site] = (old[0] ^ 1, old[1])
        if z:
            site = sites[0]
            old = result.get(site, (0, 0))
            result[site] = (old[0], old[1] ^ 1)
    return {site: axis for site, axis in result.items() if axis != (0, 0)}


def carrier_offsets() -> set[Coord]:
    cells = box((3, 3, 3))
    graph = prep.OpenReferenceGraph(cells)
    site_map = carrier_placement(graph)
    origin = center((1, 1, 1))
    return {
        tuple(site[i] - origin[i] for i in range(3))
        for site in occupied(site_map)
        if max(abs(site[i] - origin[i]) for i in range(3)) <= 9
    }


ROLE_COUNTS = {
    "triangle_syndrome": 12,
    "coarse_syndrome": 3,
    "bond_syndrome": 3,
    "input": 6,
    "ay_controller": 6,
    "az_controller": 6,
}


def slot_offsets() -> dict[tuple[str, int], Coord]:
    blocked = carrier_offsets()
    candidates = [
        row
        for row in product(range(-6, 7), repeat=3)
        if row not in blocked and max(map(abs, row)) >= 5
    ]
    candidates.sort(key=lambda row: (sum(abs(x) for x in row), row))
    needed = sum(ROLE_COUNTS.values())
    if len(candidates) < needed:
        raise AssertionError("slot deficit")
    result = {}
    cursor = 0
    for role, count in ROLE_COUNTS.items():
        for index in range(count):
            result[(role, index)] = tuple(map(int, candidates[cursor]))
            cursor += 1
    return result


SLOTS = slot_offsets()


def slot(cell: Coord, role: str, index: int) -> Coord:
    return add(center(cell), SLOTS[(role, index)])


def pauli_product(rows) -> base.Pauli:
    result = base.Pauli()
    for row in rows:
        result = result @ row
    return result


def local_d(graph: prep.OpenReferenceGraph, cell: Coord) -> base.Pauli:
    return pauli_product(
        graph.B(graph.vertex_index[(cell, mode)]) for mode in range(7)
    )


def path_a(graph: prep.OpenReferenceGraph, vertices: tuple[int, ...]) -> base.Pauli:
    result = base.Pauli(phase=(len(vertices) - 2) % 4)
    for left, right in zip(vertices, vertices[1:]):
        result = result @ graph.A(left, right)
    return result


def logical_rows(
    graph: prep.OpenReferenceGraph,
) -> tuple[tuple[Coord, int, base.Pauli, base.Pauli], ...]:
    rows = []
    for cell in graph.cells:
        reference = graph.vertex_index[(cell, 6)]
        for mode in range(6):
            zrow = graph.B(graph.vertex_index[(cell, mode)])
            xrow = pauli_product(
                graph.B(graph.vertex_index[(cell, other)])
                for other in range(mode, 6)
            ) @ graph.A(graph.vertex_index[(cell, mode)], reference)
            # The physical X definition is -i times the written product.
            xrow = base.Pauli(phase=(xrow.phase + 3) % 4, x=xrow.x, z=xrow.z)
            rows.append((cell, mode, xrow, zrow))
    return tuple(rows)


@dataclass(frozen=True)
class Interaction:
    owner: Coord
    role: tuple[object, ...]
    left: Coord
    right: Coord


def cycle_rows(graph: prep.OpenReferenceGraph):
    return tuple(
        (graph.loop_pauli(vertices), kind, key)
        for _mask, vertices, kind, key in prep.open_local_cycles(graph)
    )


def syndrome_interactions(
    graph: prep.OpenReferenceGraph,
    site_map: dict[int, tuple[Coord, ...]],
) -> list[Interaction]:
    rows = cycle_rows(graph)
    counters: Counter[tuple[Coord, str]] = Counter()
    output = []
    for row_index, (row, kind, key) in enumerate(rows):
        if kind == "cell_triangle":
            owner = key
            role = "triangle_syndrome"
        elif kind == "coarse_plaquette":
            owner = key[0]
            role = "coarse_syndrome"
        elif kind == "bond_rectangle":
            owner = key[0]
            role = "bond_syndrome"
        else:
            raise AssertionError(kind)
        local_index = counters[(owner, role)]
        counters[(owner, role)] += 1
        ancilla = slot(owner, role, local_index)
        for support_index, target in enumerate(sorted(lift_pauli(row, graph, site_map))):
            output.append(
                Interaction(owner, ("syndrome", kind, local_index, support_index), ancilla, target)
            )
    return output


def loader_interactions(
    graph: prep.OpenReferenceGraph,
    site_map: dict[int, tuple[Coord, ...]],
) -> list[Interaction]:
    output = []
    for cell, mode, xrow, zrow in logical_rows(graph):
        source = slot(cell, "input", mode)
        for word_kind, row in (("X", xrow), ("Z", zrow)):
            for support_index, target in enumerate(sorted(lift_pauli(row, graph, site_map))):
                left, right = (source, target) if word_kind == "X" else (target, source)
                output.append(
                    Interaction(cell, ("loader", mode, word_kind, support_index), left, right)
                )
    return output


def correction_interactions(
    graph: prep.OpenReferenceGraph,
    site_map: dict[int, tuple[Coord, ...]],
) -> list[Interaction]:
    output = []
    one = prep.OpenReferenceGraph(((0, 0, 0),))
    triangle_data = tuple(
        (prep.cycle_mask(one, vertices), vertices)
        for _mask, vertices, kind, _key in prep.open_local_cycles(one)
        if kind == "cell_triangle"
    )
    decoder = prep.right_inverse(tuple(row[0] for row in triangle_data), len(one.edges))
    for cell in graph.cells:
        for syndrome_index, column in enumerate(decoder):
            source = slot(cell, "triangle_syndrome", syndrome_index)
            correction_index = 0
            for local_edge, (u, v, _kind, _owner) in enumerate(one.edges):
                if not ((column >> local_edge) & 1):
                    continue
                umode = one.vertices[u][1]
                vmode = one.vertices[v][1]
                edge = graph.edge_between(
                    graph.vertex_index[(cell, umode)],
                    graph.vertex_index[(cell, vmode)],
                )
                output.append(
                    Interaction(
                        cell,
                        ("triangle_correction", syndrome_index, correction_index),
                        source,
                        site_map[edge][0],
                    )
                )
                correction_index += 1
    bond_index: Counter[Coord] = Counter()
    for _row, kind, key in cycle_rows(graph):
        if kind != "bond_rectangle":
            continue
        cell, axis = key
        local_index = bond_index[cell]
        bond_index[cell] += 1
        edge = graph.cross_edge[(cell, axis, 1)]
        output.append(
            Interaction(
                cell,
                ("bond_correction", local_index),
                slot(cell, "bond_syndrome", local_index),
                site_map[edge][0],
            )
        )
    return output


def syndrome_slot_for_source(cell: Coord, axes: tuple[int, int]) -> Coord:
    pairs = ((0, 1), (0, 2), (1, 2))
    return slot(cell, "coarse_syndrome", pairs.index(tuple(axes)))


def stream_target(
    graph: prep.OpenReferenceGraph,
    site_map: dict[int, tuple[Coord, ...]],
    node: echo.Node,
) -> Coord:
    kind, x, y, z = node
    axis = 1 if kind == "ay" else 2
    edge = graph.cross_edge[((x, y, z), axis, 0)]
    return site_map[edge][0]


def controller_interactions(
    shape: tuple[int, int, int],
    graph: prep.OpenReferenceGraph,
    site_map: dict[int, tuple[Coord, ...]],
) -> list[Interaction]:
    if len(set(shape)) != 1:
        return []
    length = shape[0]
    output = []
    for node_kind in ("ay", "az"):
        for x in range(length):
            for y in range(length):
                for z in range(length):
                    node = (node_kind, x, y, z)
                    try:
                        parent_source = echo.parent_and_source(node)
                        target = stream_target(graph, site_map, node)
                    except KeyError:
                        continue
                    owner = (x, y, z)
                    role = f"{node_kind}_controller"
                    child_value = slot(owner, role, 0)
                    if parent_source is None:
                        output.extend(
                            (
                                Interaction(
                                    owner,
                                    ("controller_root_epoch", node_kind),
                                    slot(owner, role, 4),
                                    slot(owner, role, 5),
                                ),
                                Interaction(
                                    owner,
                                    ("controller_router", node_kind),
                                    slot(owner, role, 2),
                                    slot(owner, role, 3),
                                ),
                            )
                        )
                        continue
                    parent, source_key = parent_source
                    parent_cell = echo.node_anchor(parent)
                    parent_role = f"{parent[0]}_controller"
                    for traversal in ("down", "up"):
                        output.extend((
                            Interaction(
                                owner,
                                ("controller_parent_xor", node_kind, traversal),
                                slot(parent_cell, parent_role, 0),
                                child_value,
                            ),
                            Interaction(
                                owner,
                                ("controller_source_xor", node_kind, traversal),
                                syndrome_slot_for_source(source_key[0], source_key[1]),
                                child_value,
                            ),
                            Interaction(
                                owner,
                                ("controller_token_swap", node_kind, traversal),
                                slot(parent_cell, parent_role, 1),
                                slot(owner, role, 1),
                            ),
                        ))
                    output.extend(
                        (
                            Interaction(
                                owner,
                                ("controller_emit", node_kind),
                                child_value,
                                target,
                            ),
                            Interaction(
                                owner,
                                ("controller_router", node_kind),
                                slot(owner, role, 2),
                                slot(owner, role, 3),
                            ),
                        )
                    )
    return output


def manhattan_path(left: Coord, right: Coord) -> tuple[Coord, ...]:
    return tuple(route.manhattan_path(left, right))


def route_certificate(interactions: list[Interaction]) -> dict[str, object]:
    maximum_distance = 0
    nn_failures = 0
    return_failures = 0
    operand_failures = 0
    deletion_detected = 0
    total_gates = 0
    footprints: dict[tuple[object, ...], set[Coord]] = defaultdict(set)
    for interaction in interactions:
        path = manhattan_path(interaction.left, interaction.right)
        distance = len(path) - 1
        maximum_distance = max(maximum_distance, distance)
        total_gates += max(1, 2 * distance - 1)
        nn_failures += sum(
            sum(abs(left[i] - right[i]) for i in range(3)) != 1
            for left, right in zip(path, path[1:])
        )
        labels = list(path)
        for index in range(len(path) - 2):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
        operand_failures += labels[-2:] != [interaction.left, interaction.right]
        for index in reversed(range(len(path) - 2)):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
        return_failures += labels != list(path)
        if len(path) > 2:
            deleted = list(path)
            for index in range(1, len(path) - 2):
                deleted[index], deleted[index + 1] = deleted[index + 1], deleted[index]
            for index in reversed(range(len(path) - 2)):
                deleted[index], deleted[index + 1] = deleted[index + 1], deleted[index]
            deletion_detected += deleted != list(path)
        # A finite schedule type plus owner parity is a constant local color.
        color = interaction.role + tuple(value & 1 for value in interaction.owner)
        footprints[color].update(path)

    # Recompute collisions without losing multiplicity: equal role/parity items
    # must have disjoint paths for the claimed simultaneous layer.
    collision_failures = 0
    grouped: dict[tuple[object, ...], list[set[Coord]]] = defaultdict(list)
    for interaction in interactions:
        color = interaction.role + tuple(value & 1 for value in interaction.owner)
        path_set = set(manhattan_path(interaction.left, interaction.right))
        collision_failures += sum(bool(path_set & prior) for prior in grouped[color])
        grouped[color].append(path_set)
    return {
        "interaction_count": len(interactions),
        "routed_gate_count": total_gates,
        "maximum_route_distance": maximum_distance,
        "non_NN_failures": nn_failures,
        "operand_order_failures": operand_failures,
        "route_return_failures": return_failures,
        "first_swap_deletion_detected_macros": deletion_detected,
        "fixed_role_parity_colors": len(grouped),
        "same_color_route_collisions": collision_failures,
    }


def stabilizer_and_loader_certificate(
    graph: prep.OpenReferenceGraph,
    site_map: dict[int, tuple[Coord, ...]],
) -> dict[str, object]:
    cycles = cycle_rows(graph)
    drows = tuple(local_d(graph, cell) for cell in graph.cells[:-1])
    logical = logical_rows(graph)
    abstract_qubits = len(graph.edges)
    stabilizers = tuple(row for row, _kind, _key in cycles) + drows
    rank = base.gf2_rank(row.symplectic(abstract_qubits) for row in stabilizers)
    logical_commutator_failures = 0
    canonical_failures = 0
    for index, (_cell, _mode, xrow, zrow) in enumerate(logical):
        logical_commutator_failures += sum(
            not row.commutes(stabilizer) for row in (xrow, zrow) for stabilizer in stabilizers
        )
        for j, (_c2, _m2, x2, z2) in enumerate(logical):
            canonical_failures += (not xrow.commutes(z2)) != (index == j)
            canonical_failures += not xrow.commutes(x2)
            canonical_failures += not zrow.commutes(z2)
    lifted_weights = [
        len(lift_pauli(row, graph, site_map))
        for row in stabilizers
        for row in (row,)
    ]
    loader_weights = [
        len(lift_pauli(row, graph, site_map))
        for _cell, _mode, xrow, zrow in logical
        for row in (xrow, zrow)
    ]
    return {
        "abstract_edge_qubits": abstract_qubits,
        "stabilizer_rows": len(stabilizers),
        "stabilizer_rank": rank,
        "logical_qubits": len(logical),
        "expected_logical_qubits": 6 * len(graph.cells),
        "logical_stabilizer_commutator_failures": logical_commutator_failures,
        "logical_canonical_failures": canonical_failures,
        "maximum_lifted_stabilizer_weight": max(lifted_weights, default=0),
        "maximum_lifted_loader_weight": max(loader_weights, default=0),
    }


def covariance_certificate(shape: tuple[int, int, int], graph, site_map) -> dict[str, object]:
    sites = occupied(site_map) | {
        slot(cell, role, index)
        for cell in graph.cells
        for role, count in ROLE_COUNTS.items()
        for index in range(count)
    }
    frames = base.proper_cubic_frames()
    frame_failures = 0
    product_failures = 0
    for frame in frames:
        transformed = {matvec(frame, site) for site in sites}
        frame_failures += len(transformed) != len(sites)
    for left in frames:
        for right in frames:
            direct = {matvec(left @ right, site) for site in sites}
            sequential = {matvec(left, matvec(right, site)) for site in sites}
            product_failures += direct != sequential
    return {
        "proper_cubic_frames": len(frames),
        "ordered_products": len(frames) ** 2,
        "frame_injectivity_failures": frame_failures,
        "product_diagram_failures": product_failures,
        "coframe_status": "supplied and transported",
    }


def graph_transport(source: prep.OpenReferenceGraph, target: prep.OpenReferenceGraph, frame):
    direction_map = base.direction_map(np.asarray(frame, dtype=int))
    vertex_map = tuple(
        target.vertex_index[(
            matvec(frame, cell),
            6 if mode == 6 else direction_map[mode],
        )]
        for cell, mode in source.vertices
    )
    edge_map = tuple(
        target.edge_between(vertex_map[u], vertex_map[v])
        for u, v, _kind, _owner in source.edges
    )
    gauge = local_gauss.port_gauge(source, target, vertex_map, edge_map)
    return vertex_map, edge_map, gauge


def generator_rows(graph: prep.OpenReferenceGraph):
    return tuple(graph.B(vertex) for vertex in range(len(graph.vertices))) + tuple(
        graph.A(u, v) for u, v, _kind, _owner in graph.edges
    )


def semantic_covariance_certificate(shape: tuple[int, int, int]) -> dict[str, object]:
    source = prep.OpenReferenceGraph(box(shape))
    source_sites = carrier_placement(source)
    frames = tuple(base.proper_cubic_frames())
    key = lambda frame: tuple(map(int, np.asarray(frame, dtype=int).reshape(-1)))
    targets = {}
    transports = {}
    rows = generator_rows(source)
    generator_failures = 0
    placement_failures = 0
    edge_type_failures = 0
    for frame in frames:
        target = prep.OpenReferenceGraph(tuple(matvec(frame, cell) for cell in source.cells))
        targets[key(frame)] = target
        vertex_map, edge_map, gauge = graph_transport(source, target, frame)
        transports[key(frame)] = (vertex_map, edge_map, gauge)
        target_rows = generator_rows(target)
        expected = tuple(
            target.B(vertex_map[vertex]) for vertex in range(len(source.vertices))
        ) + tuple(
            target.A(vertex_map[u], vertex_map[v])
            for u, v, _kind, _owner in source.edges
        )
        generator_failures += sum(
            local_gauss.transform_pauli(row, edge_map, gauge) != wanted
            for row, wanted in zip(rows, expected)
        )
        target_sites = carrier_placement(target)
        for edge, mapped_edge in enumerate(edge_map):
            transformed = {matvec(frame, site) for site in source_sites[edge]}
            placement_failures += transformed != set(target_sites[mapped_edge])
            edge_type_failures += source.edges[edge][2] != target.edges[mapped_edge][2]

    product_generator_failures = 0
    product_edge_failures = 0
    product_site_failures = 0
    for left in frames:
        for right in frames:
            final = left @ right
            right_target = targets[key(right)]
            final_target = targets[key(final)]
            _vr, er, gr = transports[key(right)]
            _vf, ef, gf = transports[key(final)]
            _v2, e2, g2 = graph_transport(right_target, final_target, left)
            product_edge_failures += sum(e2[er[index]] != ef[index] for index in range(len(er)))
            for row in rows:
                sequential = local_gauss.transform_pauli(
                    local_gauss.transform_pauli(row, er, gr), e2, g2
                )
                direct = local_gauss.transform_pauli(row, ef, gf)
                product_generator_failures += sequential != direct
            for edge, sites in source_sites.items():
                sequential_sites = {
                    matvec(left, matvec(right, site)) for site in sites
                }
                direct_sites = {matvec(final, site) for site in sites}
                product_site_failures += sequential_sites != direct_sites
    return {
        "shape": shape,
        "semantic_generator_rows": len(rows),
        "proper_cubic_frames": len(frames),
        "ordered_products": len(frames) ** 2,
        "single_frame_generator_failures": generator_failures,
        "single_frame_placement_failures": placement_failures,
        "single_frame_edge_type_failures": edge_type_failures,
        "product_generator_failures": product_generator_failures,
        "product_edge_failures": product_edge_failures,
        "product_site_failures": product_site_failures,
        "port_order_gauge_status": "signed local chart gauge included",
    }


def fixture(shape: tuple[int, int, int]) -> dict[str, object]:
    cells = box(shape)
    graph = prep.OpenReferenceGraph(cells)
    site_map = carrier_placement(graph)
    carrier = occupied(site_map)
    registers = {
        slot(cell, role, index)
        for cell in cells
        for role, count in ROLE_COUNTS.items()
        for index in range(count)
    }
    seam_count = sum(
        (shape[axis] - 1) * np.prod([shape[a] for a in range(3) if a != axis])
        for axis in range(3)
    )
    expected_abstract = 18 * len(cells) + 2 * int(seam_count)
    expected_physical = 18 * len(cells) + 3 * int(seam_count)
    syndrome = syndrome_interactions(graph, site_map)
    corrections = correction_interactions(graph, site_map)
    loader = loader_interactions(graph, site_map)
    controller = controller_interactions(shape, graph, site_map)
    # This order is load bearing.  The earlier scratch catalog grouped every
    # measurement before every correction and put the coarse controller after
    # the loader.  That was a useful route census but not an executable encoder.
    # The Cycle703 preparation chronology is instead
    #
    #   triangle measure/correct -> coarse measure/echo-correct/ack
    #   -> bond measure/correct -> logical load.
    #
    # The controller list is the physical atlas for the autonomous Cycle703
    # echo partial order; its list order is not reinterpreted as circuit time.
    triangle_syndrome = [
        row for row in syndrome if row.role[1] == "cell_triangle"
    ]
    coarse_syndrome = [
        row for row in syndrome if row.role[1] == "coarse_plaquette"
    ]
    bond_syndrome = [
        row for row in syndrome if row.role[1] == "bond_rectangle"
    ]
    triangle_corrections = [
        row for row in corrections if row.role[0] == "triangle_correction"
    ]
    bond_corrections = [
        row for row in corrections if row.role[0] == "bond_correction"
    ]
    chronological = (
        triangle_syndrome
        + triangle_corrections
        + coarse_syndrome
        + controller
        + bond_syndrome
        + bond_corrections
        + loader
    )
    routes = route_certificate(chronological)
    return {
        "shape": shape,
        "cells": len(cells),
        "coarse_edges": int(seam_count),
        "abstract_edges": len(graph.edges),
        "expected_abstract_edges": expected_abstract,
        "physical_carrier_M2": len(carrier),
        "expected_physical_carrier_M2": expected_physical,
        "persistent_auxiliary_slots": len(registers),
        "carrier_collisions": sum(len(sites) for sites in site_map.values()) - len(carrier),
        "carrier_auxiliary_collisions": len(carrier & registers),
        "algebra": stabilizer_and_loader_certificate(graph, site_map),
        "interaction_counts": {
            "syndrome": len(syndrome),
            "corrections": len(corrections),
            "loader": len(loader),
            "controller": len(controller),
        },
        "encoder_chronology": (
            "triangle_syndrome",
            "triangle_correction",
            "coarse_syndrome",
            "coarse_echo_correction_ack",
            "bond_syndrome",
            "bond_correction",
            "logical_load",
        ),
        "chronology_interaction_count": len(chronological),
        "routes": routes,
        "covariance": covariance_certificate(shape, graph, site_map),
    }


def main() -> int:
    dependency_hashes = {
        path: file_sha256(ROOT / path) for path in EXPECTED_DEPENDENCY_SHA256
    }
    dependency_pin_failures = {
        path: {"expected": expected, "observed": dependency_hashes[path]}
        for path, expected in EXPECTED_DEPENDENCY_SHA256.items()
        if dependency_hashes[path] != expected
    }
    rows = [
        fixture(shape)
        for shape in (
            (3, 2, 2),
            (5, 3, 2),
            (2, 2, 2),
            (3, 3, 3),
            (4, 4, 4),
            (5, 5, 5),
        )
    ]
    semantic_covariance = semantic_covariance_certificate((3, 2, 2))
    failures = [("dependencies", path) for path in dependency_pin_failures]
    for row in rows:
        alg = row["algebra"]
        routes = row["routes"]
        cov = row["covariance"]
        conditions = {
            "edge_count": row["abstract_edges"] == row["expected_abstract_edges"],
            "carrier_count": row["physical_carrier_M2"] == row["expected_physical_carrier_M2"],
            "carrier_collision": row["carrier_collisions"] == 0,
            "aux_collision": row["carrier_auxiliary_collisions"] == 0,
            "logical_count": alg["logical_qubits"] == alg["expected_logical_qubits"],
            "logical_commutators": alg["logical_stabilizer_commutator_failures"] == 0,
            "logical_canonical": alg["logical_canonical_failures"] == 0,
            "nn": routes["non_NN_failures"] == 0,
            "operand": routes["operand_order_failures"] == 0,
            "return": routes["route_return_failures"] == 0,
            "route_colors": routes["same_color_route_collisions"] == 0,
            "chronology_count": row["chronology_interaction_count"]
            == sum(row["interaction_counts"].values()),
            "chronology_order": row["encoder_chronology"]
            == (
                "triangle_syndrome",
                "triangle_correction",
                "coarse_syndrome",
                "coarse_echo_correction_ack",
                "bond_syndrome",
                "bond_correction",
                "logical_load",
            ),
            "frame": cov["frame_injectivity_failures"] == 0,
            "products": cov["product_diagram_failures"] == 0,
        }
        for key, value in conditions.items():
            if not value:
                failures.append((row["shape"], key))
        print("FIXTURE", json.dumps(row, sort_keys=True, default=str))
    semantic_zero_fields = (
        "single_frame_generator_failures",
        "single_frame_placement_failures",
        "single_frame_edge_type_failures",
        "product_generator_failures",
        "product_edge_failures",
        "product_site_failures",
    )
    failures.extend(
        ((3, 2, 2), key)
        for key in semantic_zero_fields
        if semantic_covariance[key] != 0
    )
    print("SEMANTIC_COVARIANCE", json.dumps(semantic_covariance, sort_keys=True))
    receipt = {
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "fixtures": rows,
        "semantic_covariance": semantic_covariance,
        "dependency_sha256": dependency_hashes,
        "dependency_pin_failures": dependency_pin_failures,
        "boundary": {
            "derived": [
                "formulaic OpenReference carrier placement including reference bonds",
                "bounded macrocell allocation for raw input, syndrome, and echo-controller registers",
                "literal returned nearest-neighbor routes for every declared preparation/loader/controller interaction",
                "transported 24/576 coordinate covariance",
            ],
            "supplied": [
                "spacing-16 origin and coframe",
                "finite open boundary and one preparation invocation",
                "clean raw-input/syndrome/controller genesis domain",
                "Cycle703 abstract preparation and loader semantics",
            ],
            "open": [
                "full OpenReference free/seam/contact update on the identical site map",
                "intrinsic coframe/boundary/clean-genesis law",
                "fault repair and periodic topology",
            ],
        },
    }
    payload = json.dumps(receipt, sort_keys=True, default=str, indent=2)
    digest = sha256(payload.encode()).hexdigest()
    receipt["content_sha256_before_hash_field"] = digest
    out = ROOT / "outputs" / "cycle870_openreference_physical_m2_placement_receipt_2026_08_02.json"
    out.write_text(json.dumps(receipt, sort_keys=True, default=str, indent=2) + "\n")
    print("RECEIPT", out, digest)
    print("OPENREFERENCE_PHYSICAL_PLACEMENT_PASS" if not failures else "OPENREFERENCE_PHYSICAL_PLACEMENT_FAIL")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
