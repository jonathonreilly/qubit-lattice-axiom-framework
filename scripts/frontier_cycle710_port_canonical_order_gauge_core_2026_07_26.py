#!/usr/bin/env python3
"""Cycle710 port-canonical local Clifford compiler core.

A fixed Cycle709 reference compiler is moved into a graph presentation whose
edge orientation and incident prefixes are functions only of bounded port
descriptors.  Two graph-representation intertwiners implement

    C_b = Q_patch(a->b) C_a N_a Q_open(a->b)^-1 N_b^-1.

Each Q=D P.  P only relabels the emitted word by physical edge addresses. D is
an executable commuting Clifford product: one CZ for each inversion of two
edges incident on a common graph vertex, and one Z for each residual oriented
edge sign.  No target tuple is sorted or ranked by the emitted construction.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from contextlib import contextmanager
from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys

import numpy as np


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

import frontier_cycle709_local_seam_clifford_core_2026_07_26 as C


G = C.G
F = C.F
P = C.Pauli
LEGACY_GRAPH = G.c706.ReferencePatchGraph
Coord = tuple[int, int, int]
I3 = np.eye(3, dtype=int)
PASS = 0
FAIL = 0


class PortCanonicalGraph(LEGACY_GRAPH):
    """BKSF presentation ordered and oriented by radius-one port data.

    The names ``legacy`` and ``port`` refer to representations, not to an
    imported vertex-number order.  The keys below reconstruct the landed
    presentation from edge kind, the two endpoint mode labels, and a signed
    lattice direction.  They therefore survive arbitrary enumeration of the
    same bounded graph.
    """

    KIND_ORDER = {
        "octahedral": 0,
        "spoke": 1,
        "matter_stream": 2,
        "reference_bond": 2,
    }
    DIRECTION_ORDER = {
        (-1, 0, 0): 0,
        (0, -1, 0): 1,
        (0, 0, -1): 2,
        (1, 0, 0): 3,
        (0, 1, 0): 4,
        (0, 0, 1): 5,
        (0, 0, 0): 0,
    }

    def __init__(self, cells, reference_bonds):
        super().__init__(cells, reference_bonds)
        for vertex, row in enumerate(self.incident):
            row.sort(key=lambda edge: self.port_key(vertex, edge))

    def port_key(self, vertex, edge):
        u, v, kind, _owner = self.edges[edge]
        other = v if u == vertex else u
        _cell, mode = self.vertices[vertex]
        other_cell, other_mode = self.vertices[other]
        cell = self.vertices[vertex][0]
        delta = tuple(b - a for a, b in zip(cell, other_cell))
        if kind == "octahedral":
            return self.KIND_ORDER[kind], min(mode, other_mode), max(mode, other_mode)
        if kind == "spoke":
            return self.KIND_ORDER[kind], min(mode, other_mode)
        return self.KIND_ORDER[kind], self.DIRECTION_ORDER[delta]

    def canonical_first(self, edge):
        u, v, kind, _owner = self.edges[edge]
        if kind not in ("matter_stream", "reference_bond"):
            return min((u, v), key=lambda vertex: self.vertices[vertex][1])
        u_cell = self.vertices[u][0]
        v_cell = self.vertices[v][0]
        delta = tuple(b - a for a, b in zip(u_cell, v_cell))
        if sum(abs(value) for value in delta) != 1:
            raise AssertionError("cross-cell edge is not nearest-neighbor")
        return u if 1 in delta else v

    def A(self, source, target):
        edge = self.edge_between(source, target)
        z = 0
        for vertex in (source, target):
            for incident in self.incident[vertex]:
                if incident == edge:
                    break
                z ^= 1 << incident
        phase = 0 if source == self.canonical_first(edge) else 2
        return G.c706.base.Pauli(phase, 1 << edge, z)


@contextmanager
def graph_presentation(graph_class):
    previous = G.c706.ReferencePatchGraph
    G.c706.ReferencePatchGraph = graph_class
    try:
        yield
    finally:
        G.c706.ReferencePatchGraph = previous


def build_equivalence_as(cells, graph_class):
    with graph_presentation(graph_class):
        return G.build_equivalence(tuple(cells)).equivalence


def legacy_source_compiler(cells):
    with graph_presentation(LEGACY_GRAPH):
        equivalence = G.build_equivalence(tuple(cells)).equivalence
        images = C.coloured_composition(tuple(cells)).cleaned
    return equivalence, images


def port_equivalence(cells):
    return build_equivalence_as(tuple(cells), PortCanonicalGraph)


def check(label, condition, detail):
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def mismatch(left, right):
    return {
        "exact": sum(a != b for a, b in zip(left, right)),
        "symplectic": sum((a.x, a.z) != (b.x, b.z) for a, b in zip(left, right)),
        "phase_only": sum(
            (a.x, a.z) == (b.x, b.z) and a.phase != b.phase
            for a, b in zip(left, right)
        ),
    }


def edge_key(graph, edge):
    return G.c706.edge_key(graph, edge)


def pauli_permute(row, mapping):
    x = z = 0
    for source, target in enumerate(mapping):
        x |= ((row.x >> source) & 1) << target
        z |= ((row.z >> source) & 1) << target
    return P(row.phase, x, z)


def apply_patch_gauge(row, patch, toggles, pairs, flips):
    mask = (1 << patch) - 1
    transformed = F.base.apply_gauge(
        F.base.Pauli(row.phase, row.x & mask, row.z & mask),
        toggles, pairs, flips,
    )
    return P(
        transformed.phase,
        transformed.x | (row.x & ~mask),
        transformed.z | (row.z & ~mask),
    )


@dataclass(frozen=True)
class GraphGauge:
    source: object
    target: object
    cell_map: dict
    mode_map: dict
    vertex_map: tuple[int, ...]
    edge_map: tuple[int, ...]
    toggles: tuple[int, ...]
    pairs: tuple[tuple[int, int], ...]
    flips: int
    graph_A_failures: int
    pair_vertices: tuple[int, ...]


def graph_gauge(source, target, cell_map, mode_map) -> GraphGauge:
    vertex_map = tuple(
        target.vertex_index[(cell_map[cell], 6 if mode == 6 else mode_map[mode])]
        for cell, mode in source.vertices
    )
    edge_map = tuple(
        target.edge_between(vertex_map[u], vertex_map[v])
        for u, v, _kind, _owner in source.edges
    )
    toggles = [0] * len(target.edges)
    pairs = []
    pair_vertices = []
    for source_vertex, target_vertex in enumerate(vertex_map):
        pulled = [edge_map[edge] for edge in source.incident[source_vertex]]
        positions = {
            edge: index for index, edge in enumerate(target.incident[target_vertex])
        }
        for index, left in enumerate(pulled):
            for right in pulled[index + 1:]:
                if positions[left] > positions[right]:
                    toggles[left] ^= 1 << right
                    toggles[right] ^= 1 << left
                    pairs.append((left, right))
                    pair_vertices.append(target_vertex)
    flips = failures = 0
    for source_edge, (u, v, _kind, _owner) in enumerate(source.edges):
        moved = pauli_permute(source.A(u, v), edge_map)
        ordered = apply_patch_gauge(
            moved, len(target.edges), toggles, pairs, 0
        )
        expected = target.A(vertex_map[u], vertex_map[v])
        if (ordered.x, ordered.z) != (expected.x, expected.z):
            failures += 1
        elif (ordered.phase - expected.phase) % 4 == 2:
            flips ^= 1 << edge_map[source_edge]
        elif ordered.phase != expected.phase:
            failures += 1
    for source_edge, (u, v, _kind, _owner) in enumerate(source.edges):
        moved = pauli_permute(source.A(u, v), edge_map)
        observed = apply_patch_gauge(
            moved, len(target.edges), toggles, pairs, flips
        )
        failures += observed != target.A(vertex_map[u], vertex_map[v])
    return GraphGauge(
        source, target, dict(cell_map), dict(mode_map), vertex_map, edge_map,
        tuple(toggles), tuple(pairs), flips, failures, tuple(pair_vertices),
    )


def frame_maps(cells, frame):
    cell_map = {
        cell: tuple(int(value) for value in frame @ np.asarray(cell))
        for cell in cells
    }
    return cell_map, G.c706.direction_map(frame)


def identity_maps(cells):
    return {cell: cell for cell in cells}, {mode: mode for mode in range(6)}


def gauge_tableau(data: GraphGauge):
    q = len(data.source.edges)
    output = []
    for kind in range(2):
        for source in range(q):
            row = P(
                x=(1 << source) if kind == 0 else 0,
                z=(1 << source) if kind == 1 else 0,
            )
            moved = pauli_permute(row, data.edge_map)
            output.append(apply_patch_gauge(
                moved, q, data.toggles, data.pairs, data.flips
            ))
    return tuple(output)


def patch_augmented_tableau(source_eq, target_eq, data: GraphGauge):
    source_patch = len(source_eq.patch_graph.edges)
    target_patch = len(target_eq.patch_graph.edges)
    rail_lookup = {
        label: index for index, label in enumerate(target_eq.rail_labels)
    }
    mapping = list(data.edge_map)
    for label in source_eq.rail_labels:
        moved = frozenset((data.cell_map[cell], mode) for cell, mode in label)
        mapping.append(target_patch + rail_lookup[moved])
    output = []
    for kind in range(2):
        for source in range(source_eq.qubits):
            row = P(
                x=(1 << source) if kind == 0 else 0,
                z=(1 << source) if kind == 1 else 0,
            )
            moved = pauli_permute(row, mapping)
            output.append(apply_patch_gauge(
                moved, target_patch, data.toggles, data.pairs, data.flips
            ))
    return tuple(output), tuple(mapping)


def bare_tableau(mapping):
    q = len(mapping)
    return tuple(
        [P(x=1 << mapping[index]) for index in range(q)]
        + [P(z=1 << mapping[index]) for index in range(q)]
    )


def natural_inverse(eq, row):
    inverse = {target: source for source, target in eq.natural_edge_map.items()}
    x = z = 0
    for target, source in inverse.items():
        x |= ((row.x >> target) & 1) << source
        z |= ((row.z >> target) & 1) << source
    return P(row.phase, x, z)


def semantic_rows(eq):
    rows = {
        "logical_Z": tuple(zip(eq.source_logical_z, eq.target_logical_z)),
        "logical_X": tuple(zip(eq.source_logical_x, eq.target_logical_x)),
        "local_D_all": tuple(
            (
                G.c706.local_d(eq.open_graph, cell),
                G.c706.local_d(eq.patch_graph, cell),
            )
            for cell in eq.open_graph.cells
        ),
        "bond_to_rail": tuple(zip(eq.source_bond_loops, eq.target_rails)),
    }
    loops = defaultdict(list)
    for descriptor in G.c706.local_cycles(eq.open_graph):
        if descriptor.kind == "bond_rectangle":
            continue
        source = eq.open_graph.loop_pauli(descriptor.vertices)
        target_vertices = tuple(
            eq.patch_graph.vertex_index[eq.open_graph.vertices[vertex]]
            for vertex in descriptor.vertices
        )
        loops[descriptor.kind].append(
            (source, eq.patch_graph.loop_pauli(target_vertices))
        )
    rows.update({kind: tuple(pairs) for kind, pairs in loops.items()})
    return rows


def semantic_failures(images, eq):
    return {
        name: mismatch(
            tuple(
                C.apply_images(images, C.natural(eq, source), eq.qubits)
                for source, _target in pairs
            ),
            tuple(P(row.phase, row.x, row.z) for _source, row in pairs),
        )
        for name, pairs in semantic_rows(eq).items()
    }


@dataclass(frozen=True)
class CompilerTransport:
    source_eq: object
    target_eq: object
    images: tuple[P, ...]
    bare_images: tuple[P, ...]
    open_gauge: GraphGauge
    patch_gauge: GraphGauge
    open_forward: tuple[P, ...]
    open_inverse: tuple[P, ...]
    patch_forward: tuple[P, ...]
    pre: tuple[P, ...]
    patch_mapping: tuple[int, ...]


def compiler_transport(reference_cells, target_cells, frame, base_images=None):
    reference_cells = tuple(reference_cells)
    target_cells = tuple(target_cells)
    source_eq = G.build_equivalence(reference_cells).equivalence
    target_eq = G.build_equivalence(target_cells).equivalence
    if base_images is None:
        base_images = C.coloured_composition(reference_cells).cleaned
    cell_map, mode_map = frame_maps(reference_cells, frame)
    if set(cell_map.values()) != set(target_cells):
        raise ValueError("target cells must be the transported reference cell set")
    open_data = graph_gauge(
        source_eq.open_graph, target_eq.open_graph, cell_map, mode_map
    )
    patch_data = graph_gauge(
        source_eq.patch_graph, target_eq.patch_graph, cell_map, mode_map
    )
    open_forward = gauge_tableau(open_data)
    inverse_cell = {value: key for key, value in cell_map.items()}
    inverse_mode = {value: key for key, value in mode_map.items()}
    open_reverse_data = graph_gauge(
        target_eq.open_graph, source_eq.open_graph, inverse_cell, inverse_mode
    )
    open_inverse = gauge_tableau(open_reverse_data)
    patch_forward, patch_mapping = patch_augmented_tableau(
        source_eq, target_eq, patch_data
    )
    q = source_eq.qubits
    pre = []
    bare_pre = []
    open_bare_inverse = {target: source for source, target in enumerate(open_data.edge_map)}
    for kind in range(2):
        for target_qubit in range(q):
            open_target = natural_inverse(
                target_eq,
                P(
                    x=(1 << target_qubit) if kind == 0 else 0,
                    z=(1 << target_qubit) if kind == 1 else 0,
                ),
            )
            open_source = C.apply_images(open_inverse, open_target, q)
            pre.append(C.natural(source_eq, open_source))
            x = z = 0
            for target_open in range(q):
                source_open = open_bare_inverse[target_open]
                x |= ((open_target.x >> target_open) & 1) << source_open
                z |= ((open_target.z >> target_open) & 1) << source_open
            bare_pre.append(C.natural(source_eq, P(open_target.phase, x, z)))
    images = C.compose(
        patch_forward, C.compose(base_images, tuple(pre), q), q
    )
    bare_patch = bare_tableau(patch_mapping)
    bare_images = C.compose(
        bare_patch, C.compose(base_images, tuple(bare_pre), q), q
    )
    return CompilerTransport(
        source_eq, target_eq, images, bare_images, open_data, patch_data,
        open_forward, open_inverse, patch_forward, tuple(pre), patch_mapping,
    )


def mixed_compiler_transport(source_eq, target_eq, frame, base_images):
    """Move a legacy reference word into a port-canonical target chart."""
    cell_map, mode_map = frame_maps(source_eq.open_graph.cells, frame)
    if set(cell_map.values()) != set(target_eq.open_graph.cells):
        raise ValueError("target cells must be the transported reference cell set")
    open_data = graph_gauge(
        source_eq.open_graph, target_eq.open_graph, cell_map, mode_map
    )
    patch_data = graph_gauge(
        source_eq.patch_graph, target_eq.patch_graph, cell_map, mode_map
    )
    open_forward = gauge_tableau(open_data)
    inverse_cell = {value: key for key, value in cell_map.items()}
    inverse_mode = {value: key for key, value in mode_map.items()}
    open_inverse = gauge_tableau(graph_gauge(
        target_eq.open_graph, source_eq.open_graph, inverse_cell, inverse_mode
    ))
    patch_forward, patch_mapping = patch_augmented_tableau(
        source_eq, target_eq, patch_data
    )
    q = source_eq.qubits
    pre = []
    for kind in range(2):
        for target_qubit in range(q):
            open_target = natural_inverse(
                target_eq,
                P(
                    x=(1 << target_qubit) if kind == 0 else 0,
                    z=(1 << target_qubit) if kind == 1 else 0,
                ),
            )
            open_source = C.apply_images(open_inverse, open_target, q)
            pre.append(C.natural(source_eq, open_source))
    images = C.compose(
        patch_forward, C.compose(base_images, tuple(pre), q), q
    )
    return CompilerTransport(
        source_eq, target_eq, images, images, open_data, patch_data,
        open_forward, open_inverse, patch_forward, tuple(pre), patch_mapping,
    )


def completion_residual(transport):
    expected = C.target_images(transport.target_eq)
    residual = mismatch(transport.images, expected)
    rank = len(C.gf2_basis(
        (left.x ^ right.x) | (
            (left.z ^ right.z) << transport.target_eq.qubits
        )
        for left, right in zip(transport.images, expected)
    ))
    return residual, rank


def gauge_terms(data: GraphGauge):
    z_terms = tuple(
        edge_key(data.target, edge)
        for edge in range(len(data.target.edges))
        if (data.flips >> edge) & 1
    )
    cz_terms = tuple(
        tuple(sorted((edge_key(data.target, left), edge_key(data.target, right)), key=repr))
        for left, right in data.pairs
    )
    return z_terms, cz_terms


def cell_diameter_for_edges(graph, edges):
    cells = set()
    for edge in edges:
        u, v, _kind, _owner = graph.edges[edge]
        cells.add(graph.vertices[u][0])
        cells.add(graph.vertices[v][0])
    return max((
        sum(abs(a - b) for a, b in zip(left, right))
        for left in cells for right in cells
    ), default=0)


def gauge_locality(data: GraphGauge):
    per_vertex = Counter(data.pair_vertices)
    pair_locality_failures = sum(
        cell_diameter_for_edges(data.target, pair) > 2
        for pair in data.pairs
    )
    pair_shared_vertex_failures = 0
    for (left, right), vertex in zip(data.pairs, data.pair_vertices):
        pair_shared_vertex_failures += not (
            left in data.target.incident[vertex]
            and right in data.target.incident[vertex]
        )
    return {
        "edges": len(data.target.edges),
        "CZ_terms": len(data.pairs),
        "Z_terms": data.flips.bit_count(),
        "maximum_CZ_terms_at_one_vertex": max(per_vertex.values(), default=0),
        "maximum_graph_degree": max(map(len, data.target.incident), default=0),
        "pair_shared_vertex_failures": pair_shared_vertex_failures,
        "pair_cell_diameter_gt_two": pair_locality_failures,
        "graph_A_failures": data.graph_A_failures,
    }


def altered_graph_A_failures(data, deleted_pair=None, deleted_flip=None):
    pairs = tuple(
        pair for index, pair in enumerate(data.pairs) if index != deleted_pair
    )
    toggles = [0] * len(data.target.edges)
    for left, right in pairs:
        toggles[left] ^= 1 << right
        toggles[right] ^= 1 << left
    flips = data.flips
    if deleted_flip is not None:
        flips ^= 1 << deleted_flip
    failures = 0
    for source_edge, (u, v, _kind, _owner) in enumerate(data.source.edges):
        moved = pauli_permute(data.source.A(u, v), data.edge_map)
        observed = apply_patch_gauge(
            moved, len(data.target.edges), toggles, pairs, flips
        )
        failures += observed != data.target.A(
            data.vertex_map[u], data.vertex_map[v]
        )
    return failures


def deletion_certificate(data):
    pair_failures = tuple(
        altered_graph_A_failures(data, deleted_pair=index)
        for index in range(len(data.pairs))
    )
    flip_indices = tuple(
        edge for edge in range(len(data.target.edges))
        if (data.flips >> edge) & 1
    )
    flip_failures = tuple(
        altered_graph_A_failures(data, deleted_flip=edge)
        for edge in flip_indices
    )
    return {
        "CZ_deletions": len(pair_failures),
        "minimum_CZ_delete_graph_A_failures": min(pair_failures, default=0),
        "Z_deletions": len(flip_failures),
        "minimum_Z_delete_graph_A_failures": min(flip_failures, default=0),
    }


def representation_inverse_failures(transport):
    q = transport.source_eq.qubits
    identity = C.identity_images(q)
    open_failures = mismatch(
        C.compose(transport.open_inverse, transport.open_forward, q), identity
    )["exact"]
    inverse_cell = {
        value: key for key, value in transport.patch_gauge.cell_map.items()
    }
    inverse_mode = {
        value: key for key, value in transport.patch_gauge.mode_map.items()
    }
    reverse_data = graph_gauge(
        transport.target_eq.patch_graph,
        transport.source_eq.patch_graph,
        inverse_cell,
        inverse_mode,
    )
    reverse_patch, _mapping = patch_augmented_tableau(
        transport.target_eq, transport.source_eq, reverse_data
    )
    patch_failures = mismatch(
        C.compose(reverse_patch, transport.patch_forward, q), identity
    )["exact"]
    return open_failures + patch_failures


def shuffled_box_campaign():
    shapes = ((2, 2, 2), (3, 2, 2), (4, 2, 2), (3, 3, 2), (3, 3, 3))
    rng = np.random.default_rng(2710)
    reports = []
    selected_deletion = None
    for shape in shapes:
        reference = G.box_cells(shape)
        base = C.coloured_composition(reference).cleaned
        for sample in range(4):
            target = list(reference)
            rng.shuffle(target)
            target = tuple(target)
            transport = compiler_transport(reference, target, I3, base)
            semantics = semantic_failures(transport.images, transport.target_eq)
            bare = semantic_failures(transport.bare_images, transport.target_eq)
            ambient, residual_rank = completion_residual(transport)
            open_local = gauge_locality(transport.open_gauge)
            patch_local = gauge_locality(transport.patch_gauge)
            row = {
                "shape": shape,
                "sample": sample,
                "cells": len(reference),
                "qubits": transport.target_eq.qubits,
                "seams": len(transport.target_eq.rail_labels),
                "semantic_failures": semantics,
                "bare_without_order_gauge_failures": bare,
                "ambient_mismatches": ambient,
                "ambient_residual_rank": residual_rank,
                "open_gauge": open_local,
                "patch_gauge": patch_local,
                "representation_inverse_failures": representation_inverse_failures(transport),
                "parameters_refit": 0,
            }
            reports.append(row)
            if selected_deletion is None and patch_local["Z_terms"]:
                selected_deletion = deletion_certificate(transport.patch_gauge)
    return tuple(reports), selected_deletion


def transform_eq(reference_cells, frame):
    target = tuple(
        tuple(int(value) for value in frame @ np.asarray(cell))
        for cell in reference_cells
    )
    return target


def frame_campaign():
    reference = G.box_cells((2, 2, 2))
    base = C.coloured_composition(reference).cleaned
    frames = G.c706.proper_cubic_frames()
    transports = {}
    semantic_total = ambient_rows = 0
    locality = []
    for index, frame in enumerate(frames):
        target = transform_eq(reference, frame)
        transport = compiler_transport(reference, target, frame, base)
        transports[index] = transport
        semantic_total += sum(
            field
            for row in semantic_failures(transport.images, transport.target_eq).values()
            for field in row.values()
        )
        ambient_rows += completion_residual(transport)[0]["exact"]
        locality.extend((
            gauge_locality(transport.open_gauge),
            gauge_locality(transport.patch_gauge),
        ))
    frame_lookup = {
        tuple(int(value) for value in frame.flat): index
        for index, frame in enumerate(frames)
    }
    open_product_failures = patch_product_failures = 0
    inverse_failures = 0
    q = G.build_equivalence(reference).equivalence.qubits
    identity = C.identity_images(q)
    for index, transport in transports.items():
        inverse_failures += mismatch(
            C.compose(transport.open_inverse, transport.open_forward, q), identity
        )["exact"]
        reverse_patch_data = graph_gauge(
            transport.target_eq.patch_graph,
            transport.source_eq.patch_graph,
            {value: key for key, value in transport.patch_gauge.cell_map.items()},
            {value: key for key, value in transport.patch_gauge.mode_map.items()},
        )
        reverse_patch, _mapping = patch_augmented_tableau(
            transport.target_eq, transport.source_eq, reverse_patch_data
        )
        inverse_failures += mismatch(
            C.compose(reverse_patch, transport.patch_forward, q), identity
        )["exact"]
    for left in frames:
        for right in frames:
            right_index = frame_lookup[tuple(int(value) for value in right.flat)]
            product_frame = left @ right
            product_index = frame_lookup[
                tuple(int(value) for value in product_frame.flat)
            ]
            mid = transports[right_index].target_eq
            final = transports[product_index].target_eq
            cell_map, mode_map = frame_maps(mid.open_graph.cells, left)
            open_middle = gauge_tableau(graph_gauge(
                mid.open_graph, final.open_graph, cell_map, mode_map
            ))
            patch_middle_data = graph_gauge(
                mid.patch_graph, final.patch_graph, cell_map, mode_map
            )
            patch_middle, _mapping = patch_augmented_tableau(
                mid, final, patch_middle_data
            )
            open_product_failures += mismatch(
                C.compose(open_middle, transports[right_index].open_forward, q),
                transports[product_index].open_forward,
            )["exact"]
            patch_product_failures += mismatch(
                C.compose(patch_middle, transports[right_index].patch_forward, q),
                transports[product_index].patch_forward,
            )["exact"]
    most_pairs = max(
        (transport.patch_gauge for transport in transports.values()),
        key=lambda data: len(data.pairs),
    )
    return {
        "proper_cubic_frames": len(frames),
        "semantic_failure_sum": semantic_total,
        "ambient_mismatch_rows": ambient_rows,
        "ordered_frame_products": len(frames) ** 2,
        "open_product_failures": open_product_failures,
        "patch_product_failures": patch_product_failures,
        "inverse_failures": inverse_failures,
        "maximum_CZ_terms": max(row["CZ_terms"] for row in locality),
        "maximum_Z_terms": max(row["Z_terms"] for row in locality),
        "maximum_CZ_terms_per_vertex": max(
            row["maximum_CZ_terms_at_one_vertex"] for row in locality
        ),
        "locality_failures": sum(
            row["graph_A_failures"]
            + row["pair_shared_vertex_failures"]
            + row["pair_cell_diameter_gt_two"]
            for row in locality
        ),
        "active_deletions": deletion_certificate(most_pairs),
    }


def term_key_set(data):
    z, cz = gauge_terms(data)
    return {("Z", key) for key in z} | {("CZ", pair) for pair in cz}


def shared_port_campaign():
    global_reference = G.box_cells((3, 2, 2))
    rng = np.random.default_rng(3710)
    global_target = list(global_reference)
    rng.shuffle(global_target)
    global_target = tuple(global_target)
    left_set = set(G.box_cells((2, 2, 2)))
    right_set = {(x + 1, y, z) for x, y, z in G.box_cells((2, 2, 2))}
    rows = []
    open_term_count = 0
    rail_sets = []
    for cell_set in (left_set, right_set):
        reference = tuple(cell for cell in global_reference if cell in cell_set)
        target = tuple(cell for cell in global_target if cell in cell_set)
        source_graph = G.c706.ReferencePatchGraph(reference, False)
        target_graph = G.c706.ReferencePatchGraph(target, False)
        cell_map, mode_map = identity_maps(reference)
        data = graph_gauge(source_graph, target_graph, cell_map, mode_map)
        rows.append((data, term_key_set(data)))
        source_open = G.c706.ReferencePatchGraph(reference, True)
        target_open = G.c706.ReferencePatchGraph(target, True)
        open_data = graph_gauge(source_open, target_open, cell_map, mode_map)
        open_term_count += len(open_data.pairs) + open_data.flips.bit_count()
        rail_sets.append({
            frozenset((source_open.vertices[u], source_open.vertices[v]))
            for u, v, kind, _owner in source_open.edges
            if kind == "reference_bond"
        })
    left_data, left_terms = rows[0]
    right_data, right_terms = rows[1]
    left_edges = {edge_key(left_data.target, edge) for edge in range(len(left_data.target.edges))}
    right_edges = {edge_key(right_data.target, edge) for edge in range(len(right_data.target.edges))}
    shared = left_edges & right_edges
    def restrict(terms):
        output = set()
        for kind, item in terms:
            edges = (item,) if kind == "Z" else item
            if all(edge in shared for edge in edges):
                output.add((kind, item))
        return output
    return {
        "shared_patch_edge_addresses": len(shared),
        "shared_rail_addresses": len(rail_sets[0] & rail_sets[1]),
        "shared_augmented_addresses": len(shared) + len(rail_sets[0] & rail_sets[1]),
        "open_pre_gauge_terms_for_pure_order_shuffle": open_term_count,
        "left_terms": len(left_terms),
        "right_terms": len(right_terms),
        "shared_port_term_failures": len(restrict(left_terms) ^ restrict(right_terms)),
        "left_graph_A_failures": left_data.graph_A_failures,
        "right_graph_A_failures": right_data.graph_A_failures,
    }


def pauli_rank(rows, qubits):
    return F.base.gf2_rank(row.symplectic(qubits) for row in rows)


def anticommutator_bit(left, right):
    return (
        (left.x & right.z).bit_count()
        + (left.z & right.x).bit_count()
    ) & 1


def signed_stabilizer_status(row, equivalence):
    logical_count = len(equivalence.target_logical_z)
    coordinates = G.c706.decode(
        row, equivalence.target_w, equivalence.target_v, equivalence.qubits
    )
    if coordinates.v_mask or coordinates.w_mask & ((1 << logical_count) - 1):
        return "outside"
    return {0: "positive", 2: "negative"}.get(
        coordinates.phase, "nonhermitian"
    )


def code_span_certificate(images, equivalence):
    qubits = equivalence.qubits
    logical_count = len(equivalence.target_logical_z)
    actual_stabilizers = list(equivalence.target_w[logical_count:])
    logical_rows = []
    stabilizer_rows = []
    for name, pairs in semantic_rows(equivalence).items():
        targets = [target for _source, target in pairs]
        if name in ("logical_X", "logical_Z"):
            logical_rows.extend(targets)
        else:
            stabilizer_rows.extend(targets)
    expected = C.target_images(equivalence)
    residuals = [left @ right for left, right in zip(images, expected)]
    mismatches = [
        residual for residual, left, right in zip(residuals, images, expected)
        if left != right
    ]
    status = Counter(
        signed_stabilizer_status(row, equivalence) for row in mismatches
    )
    actual_rank = pauli_rank(actual_stabilizers, qubits)
    return {
        "qubits": qubits,
        "logical_qubits": logical_count,
        "actual_stabilizer_rank": actual_rank,
        "declared_stabilizer_rank": pauli_rank(stabilizer_rows, qubits),
        "union_stabilizer_rank": pauli_rank(
            stabilizer_rows + actual_stabilizers, qubits
        ),
        "declared_semantic_rank": pauli_rank(
            stabilizer_rows + logical_rows, qubits
        ),
        "full_centralizer_dimension": 2 * qubits - actual_rank,
        "semantic_stabilizer_commutator_failures": sum(
            anticommutator_bit(row, stabilizer)
            for row in stabilizer_rows + logical_rows
            for stabilizer in actual_stabilizers
        ),
        "declared_stabilizer_signed_status": dict(Counter(
            signed_stabilizer_status(row, equivalence)
            for row in stabilizer_rows
        )),
        "ambient_mismatch_rows": len(mismatches),
        "ambient_mismatch_residual_rank": pauli_rank(mismatches, qubits),
        "ambient_mismatch_signed_stabilizer_status": dict(status),
        "ambient_mismatch_outside_or_nonhermitian": (
            status["outside"] + status["nonhermitian"]
        ),
    }


def terms_digest(*gauges):
    payload = tuple(
        sorted((repr(item) for gauge in gauges for item in term_key_set(gauge)))
    )
    return sha256(repr(payload).encode()).hexdigest()


def port_shuffled_campaign():
    shapes = ((2, 2, 2), (3, 2, 2), (4, 2, 2), (3, 3, 2), (3, 3, 3))
    rng = np.random.default_rng(5710)
    reports = []
    for shape in shapes:
        reference = G.box_cells(shape)
        source_eq, base = legacy_source_compiler(reference)
        for sample in range(4):
            target = list(reference)
            rng.shuffle(target)
            target_eq = port_equivalence(tuple(target))
            transport = mixed_compiler_transport(
                source_eq, target_eq, I3, base
            )
            reports.append({
                "shape": shape,
                "sample": sample,
                "cells": len(reference),
                "qubits": target_eq.qubits,
                "seams": len(target_eq.rail_labels),
                "semantic_failures": semantic_failures(
                    transport.images, target_eq
                ),
                "open_gauge": gauge_locality(transport.open_gauge),
                "patch_gauge": gauge_locality(transport.patch_gauge),
                "term_set_sha256": terms_digest(
                    transport.open_gauge, transport.patch_gauge
                ),
                "code_span": code_span_certificate(
                    transport.images, target_eq
                ),
                "parameters_refit": 0,
            })
    return tuple(reports)


def port_frame_campaign():
    reference = G.box_cells((2, 2, 2))
    source_eq, base = legacy_source_compiler(reference)
    frames = G.c706.proper_cubic_frames()
    transports = {}
    semantic_total = inverse_failures = locality_failures = 0
    q = source_eq.qubits
    identity = C.identity_images(q)
    for index, frame in enumerate(frames):
        target_eq = port_equivalence(transform_eq(reference, frame))
        transport = mixed_compiler_transport(
            source_eq, target_eq, frame, base
        )
        transports[index] = transport
        semantic_total += sum(
            field
            for family in semantic_failures(transport.images, target_eq).values()
            for field in family.values()
        )
        locality_failures += sum(
            row["graph_A_failures"]
            + row["pair_shared_vertex_failures"]
            + row["pair_cell_diameter_gt_two"]
            for row in (
                gauge_locality(transport.open_gauge),
                gauge_locality(transport.patch_gauge),
            )
        )
        inverse_failures += mismatch(
            C.compose(transport.open_inverse, transport.open_forward, q),
            identity,
        )["exact"]
        inverse_patch_data = graph_gauge(
            target_eq.patch_graph,
            source_eq.patch_graph,
            {value: key for key, value in transport.patch_gauge.cell_map.items()},
            {value: key for key, value in transport.patch_gauge.mode_map.items()},
        )
        inverse_patch, _mapping = patch_augmented_tableau(
            target_eq, source_eq, inverse_patch_data
        )
        inverse_failures += mismatch(
            C.compose(inverse_patch, transport.patch_forward, q), identity
        )["exact"]
    lookup = {
        tuple(int(value) for value in frame.flat): index
        for index, frame in enumerate(frames)
    }
    open_products = patch_products = 0
    for left in frames:
        for right in frames:
            right_index = lookup[tuple(int(value) for value in right.flat)]
            product_index = lookup[tuple(int(value) for value in (left @ right).flat)]
            mid = transports[right_index].target_eq
            final = transports[product_index].target_eq
            cell_map, mode_map = frame_maps(mid.open_graph.cells, left)
            open_middle = gauge_tableau(graph_gauge(
                mid.open_graph, final.open_graph, cell_map, mode_map
            ))
            patch_middle, _mapping = patch_augmented_tableau(
                mid, final, graph_gauge(
                    mid.patch_graph, final.patch_graph, cell_map, mode_map
                )
            )
            open_products += mismatch(
                C.compose(open_middle, transports[right_index].open_forward, q),
                transports[product_index].open_forward,
            )["exact"]
            patch_products += mismatch(
                C.compose(patch_middle, transports[right_index].patch_forward, q),
                transports[product_index].patch_forward,
            )["exact"]
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "semantic_failure_sum": semantic_total,
        "open_product_failures": open_products,
        "patch_product_failures": patch_products,
        "inverse_failures": inverse_failures,
        "locality_failures": locality_failures,
        "maximum_open_CZ_terms": max(
            len(row.open_gauge.pairs) for row in transports.values()
        ),
        "maximum_patch_CZ_terms": max(
            len(row.patch_gauge.pairs) for row in transports.values()
        ),
        "maximum_open_Z_terms": max(
            row.open_gauge.flips.bit_count() for row in transports.values()
        ),
        "maximum_patch_Z_terms": max(
            row.patch_gauge.flips.bit_count() for row in transports.values()
        ),
    }


def port_independent_overlap_campaign():
    left = G.box_cells((2, 2, 2))
    right = tuple((x + 1, y, z) for x, y, z in G.box_cells((2, 2, 2)))
    rng = np.random.default_rng(6710)
    rows = []
    address_sets = []
    for cells in (left, right):
        target = list(cells)
        rng.shuffle(target)
        target_eq = port_equivalence(tuple(target))
        reference_eq = port_equivalence(cells)
        cm, mm = identity_maps(cells)
        open_data = graph_gauge(
            reference_eq.open_graph, target_eq.open_graph, cm, mm
        )
        patch_data = graph_gauge(
            reference_eq.patch_graph, target_eq.patch_graph, cm, mm
        )
        addresses = {C.address(target_eq, q) for q in range(target_eq.qubits)}
        address_sets.append(addresses)
        rows.append({
            "open_CZ": len(open_data.pairs),
            "open_Z": open_data.flips.bit_count(),
            "patch_CZ": len(patch_data.pairs),
            "patch_Z": patch_data.flips.bit_count(),
            "graph_A_failures": (
                open_data.graph_A_failures + patch_data.graph_A_failures
            ),
        })
    shared = address_sets[0] & address_sets[1]
    shared_rails = sum(address[0] == "rail" for address in shared)
    return {
        "independently_shuffled_cube_views": 2,
        "shared_augmented_addresses": len(shared),
        "shared_patch_edge_addresses": len(shared) - shared_rails,
        "shared_rail_addresses": shared_rails,
        "independent_order_transition_terms": sum(
            row["open_CZ"] + row["open_Z"]
            + row["patch_CZ"] + row["patch_Z"]
            for row in rows
        ),
        "graph_A_failures": sum(row["graph_A_failures"] for row in rows),
        "rows": tuple(rows),
    }


def half_edge_feature(graph, vertex, edge):
    u, v, kind, _owner = graph.edges[edge]
    other = v if u == vertex else u
    cell, mode = graph.vertices[vertex]
    other_cell, other_mode = graph.vertices[other]
    delta = tuple(b - a for a, b in zip(cell, other_cell))
    return kind, mode, other_mode, delta, int(vertex == v)


def oriented_edge_feature(graph, edge):
    u, v, kind, _owner = graph.edges[edge]
    cell, mode = graph.vertices[u]
    other_cell, other_mode = graph.vertices[v]
    delta = tuple(b - a for a, b in zip(cell, other_cell))
    return kind, mode, other_mode, delta


def feature_factoring_campaign():
    shapes = ((2, 2, 2), (3, 2, 2), (4, 2, 2), (3, 3, 2), (3, 3, 3))
    frames = G.c706.proper_cubic_frames()
    reports = {}
    for name, reference_bonds in (("open", True), ("patch", False)):
        z_outcomes = defaultdict(set)
        pair_outcomes = defaultdict(set)
        legacy_pair_outcomes = defaultdict(set)
        legacy_phase_outcomes = defaultdict(set)
        for shape in shapes:
            reference = G.box_cells(shape)
            legacy = LEGACY_GRAPH(reference, reference_bonds)
            for edge, (u, v, _kind, _owner) in enumerate(legacy.edges):
                legacy_phase_outcomes[oriented_edge_feature(legacy, edge)].add(
                    int(u > v)
                )
            for vertex, incident in enumerate(legacy.incident):
                for index, left in enumerate(incident):
                    for right in incident[index + 1:]:
                        features = tuple(sorted((
                            half_edge_feature(legacy, vertex, left),
                            half_edge_feature(legacy, vertex, right),
                        ), key=repr))
                        legacy_pair_outcomes[features].add(int(
                            half_edge_feature(legacy, vertex, left)
                            != features[0]
                        ))
            for frame_index, frame in enumerate(frames):
                target = transform_eq(reference, frame)
                target_graph = PortCanonicalGraph(target, reference_bonds)
                cell_map, mode_map = frame_maps(legacy.cells, frame)
                data = graph_gauge(
                    legacy, target_graph, cell_map, mode_map
                )
                active_pairs = {frozenset(pair) for pair in data.pairs}
                for edge in range(len(target_graph.edges)):
                    key = frame_index, oriented_edge_feature(target_graph, edge)
                    z_outcomes[key].add((data.flips >> edge) & 1)
                for vertex, incident in enumerate(target_graph.incident):
                    for index, left in enumerate(incident):
                        for right in incident[index + 1:]:
                            features = tuple(sorted((
                                half_edge_feature(target_graph, vertex, left),
                                half_edge_feature(target_graph, vertex, right),
                            ), key=repr))
                            key = (
                                frame_index,
                                target_graph.vertices[vertex][1],
                                features,
                            )
                            pair_outcomes[key].add(int(
                                frozenset((left, right)) in active_pairs
                            ))
        reports[name] = {
            "Z_features": len(z_outcomes),
            "Z_feature_collisions": sum(
                len(values) > 1 for values in z_outcomes.values()
            ),
            "pair_features": len(pair_outcomes),
            "pair_feature_collisions": sum(
                len(values) > 1 for values in pair_outcomes.values()
            ),
            "legacy_local_pair_features": len(legacy_pair_outcomes),
            "legacy_local_pair_order_collisions": sum(
                len(values) > 1 for values in legacy_pair_outcomes.values()
            ),
            "legacy_local_phase_features": len(legacy_phase_outcomes),
            "legacy_local_phase_collisions": sum(
                len(values) > 1 for values in legacy_phase_outcomes.values()
            ),
        }
    return reports


def legacy_local_match_campaign():
    """Show that local ports reproduce the landed presentation on five sizes."""
    shapes = ((2, 2, 2), (3, 2, 2), (4, 2, 2), (3, 3, 2), (3, 3, 3))
    incident_failures = oriented_A_failures = 0
    for shape in shapes:
        cells = G.box_cells(shape)
        for reference_bonds in (True, False):
            legacy = LEGACY_GRAPH(cells, reference_bonds)
            port = PortCanonicalGraph(cells, reference_bonds)
            incident_failures += sum(
                legacy.incident[vertex] != port.incident[vertex]
                for vertex in range(len(legacy.vertices))
            )
            for u, v, _kind, _owner in legacy.edges:
                oriented_A_failures += legacy.A(u, v) != port.A(u, v)
                oriented_A_failures += legacy.A(v, u) != port.A(v, u)
    return {
        "fixtures": 2 * len(shapes),
        "incident_order_failures": incident_failures,
        "oriented_A_failures": oriented_A_failures,
    }


def physical_edge_addresses(data):
    return {
        edge_key(data.target, edge) for edge in range(len(data.target.edges))
    }


def restrict_term_keys(terms, allowed_edges):
    answer = set()
    for kind, item in terms:
        edges = (item,) if kind == "Z" else item
        if all(edge in allowed_edges for edge in edges):
            answer.add((kind, item))
    return answer


def mixed_for_physical_frame(source_cells, frame):
    source_cells = tuple(sorted(source_cells))
    source_eq, base = legacy_source_compiler(source_cells)
    target = transform_eq(source_cells, frame)
    target_eq = port_equivalence(target)
    return mixed_compiler_transport(source_eq, target_eq, frame, base)


def common_coframe_restriction_campaign():
    """Restrict one common chart from 3x2x2 to its two maximal cubes."""
    global_cells = G.box_cells((3, 2, 2))
    subsets = (
        {cell for cell in global_cells if cell[0] <= 1},
        {cell for cell in global_cells if cell[0] >= 1},
    )
    checks = failures = maximum_difference = 0
    for frame in G.c706.proper_cubic_frames():
        global_transport = mixed_for_physical_frame(global_cells, frame)
        for subset in subsets:
            local_transport = mixed_for_physical_frame(subset, frame)
            for global_data, local_data in (
                (global_transport.open_gauge, local_transport.open_gauge),
                (global_transport.patch_gauge, local_transport.patch_gauge),
            ):
                allowed = physical_edge_addresses(local_data)
                difference = len(
                    restrict_term_keys(term_key_set(global_data), allowed)
                    ^ term_key_set(local_data)
                )
                checks += 1
                failures += difference != 0
                maximum_difference = max(maximum_difference, difference)
    return {
        "proper_cubic_frames": 24,
        "subcubes": 2,
        "graph_types": 2,
        "checks": checks,
        "failure_checks": failures,
        "maximum_difference": maximum_difference,
    }


def physical_chart_transport(physical_cells, frame):
    source = tuple(sorted(
        tuple(int(value) for value in frame.T @ np.asarray(cell))
        for cell in physical_cells
    ))
    return mixed_for_physical_frame(source, frame)


def shared_term_restriction(left_data, right_data):
    shared = physical_edge_addresses(left_data) & physical_edge_addresses(right_data)
    left = restrict_term_keys(term_key_set(left_data), shared)
    right = restrict_term_keys(term_key_set(right_data), shared)
    return {
        "shared_edges": len(shared),
        "left_terms": len(left),
        "right_terms": len(right),
        "term_difference": len(left ^ right),
    }


def independent_coframe_falsifier():
    """Retain the exact boundary: independent charts do not glue by equality."""
    identity = np.eye(3, dtype=int)
    rotated = np.diag((-1, -1, 1))
    cube = set(G.box_cells((2, 2, 2)))
    identity_cube = physical_chart_transport(cube, identity)
    rotated_cube = physical_chart_transport(cube, rotated)
    left = physical_chart_transport(cube, identity)
    right = physical_chart_transport(
        {(x + 1, y, z) for x, y, z in cube}, rotated
    )
    same_cube = {
        "open_term_difference": len(
            term_key_set(identity_cube.open_gauge)
            ^ term_key_set(rotated_cube.open_gauge)
        ),
        "patch_term_difference": len(
            term_key_set(identity_cube.patch_gauge)
            ^ term_key_set(rotated_cube.patch_gauge)
        ),
    }
    semantic_failure_sum = sum(
        value
        for transport in (identity_cube, rotated_cube, left, right)
        for family in semantic_failures(transport.images, transport.target_eq).values()
        for value in family.values()
    )
    return {
        "relative_frame": rotated.tolist(),
        "semantic_failure_sum": semantic_failure_sum,
        "same_physical_cube": same_cube,
        "overlap_open": shared_term_restriction(
            left.open_gauge, right.open_gauge
        ),
        "overlap_patch": shared_term_restriction(
            left.patch_gauge, right.patch_gauge
        ),
    }


def supplied_inventory():
    return {
        "supplied": (
            "one finite reference cell/path enumeration used only as the landed Cycle709 word template",
            "a common proper-cubic coframe on the declared overlapping-star domain",
            "local edge-kind, endpoint-mode, signed-port, and graph-incidence labels",
            "Cycle709 four-factor, six-colour, and cleanup word in the reference chart",
            "the Cycle706 signed A/B operator convention and OpenReference source sector",
        ),
        "derived": (
            "the landed presentation's incident prefixes from radius-one local ports",
            "canonical A orientation from lower endpoint mode or directed positive-axis port",
            "enumeration-independent bare edge-address relabeling P",
            "bounded vertex-local incident-inversion CZ and edge-local orientation Z terms",
            "pre gauge N_a Q_open^-1 N_b^-1 and post gauge Q_patch",
            "exact inverse, all 576 proper-cubic products, and common-chart overlap restriction",
            "full signed-code centralizer coverage on all twenty shuffled fixtures",
        ),
        "open": (
            "local preparation and dynamical enforcement of the source/repetition sector",
            "an autonomous coframe-transition/controller genesis law",
            "independently chosen overlapping coframes do not yet glue by equality",
            "a collision-free literal NN schedule for nonidentity coframe gauges",
            "periodic Wilson-sector character and recurrence",
            "the off-code ambient completion gauge is not eliminated or made canonical",
        ),
    }


def json_ready(value):
    if isinstance(value, dict):
        return {
            key if isinstance(key, (str, int, float, bool)) else repr(key): json_ready(item)
            for key, item in value.items()
        }
    if isinstance(value, (tuple, list)):
        return [json_ready(item) for item in value]
    return value


def main():
    legacy = legacy_local_match_campaign()
    check(
        "radius-one port rules exactly reproduce the landed presentation on five sizes",
        legacy["fixtures"] == 10
        and legacy["incident_order_failures"] == 0
        and legacy["oriented_A_failures"] == 0,
        legacy,
    )
    shuffled = port_shuffled_campaign()
    semantic_sum = sum(
        field for row in shuffled
        for family in row["semantic_failures"].values()
        for field in family.values()
    )
    locality_failures = sum(
        gauge["graph_A_failures"]
        + gauge["pair_shared_vertex_failures"]
        + gauge["pair_cell_diameter_gt_two"]
        for row in shuffled
        for gauge in (row["open_gauge"], row["patch_gauge"])
    )
    span_failures = sum(
        row["code_span"]["declared_stabilizer_rank"]
        != row["code_span"]["actual_stabilizer_rank"]
        or row["code_span"]["union_stabilizer_rank"]
        != row["code_span"]["actual_stabilizer_rank"]
        or row["code_span"]["declared_semantic_rank"]
        != row["code_span"]["full_centralizer_dimension"]
        or row["code_span"]["semantic_stabilizer_commutator_failures"]
        or row["code_span"]["ambient_mismatch_outside_or_nonhermitian"]
        for row in shuffled
    )
    check(
        "twenty shuffled paths close with zero order-gauge terms and full signed-code centralizer coverage",
        len(shuffled) == 20 and semantic_sum == 0 and locality_failures == 0
        and span_failures == 0
        and all(
            row["open_gauge"]["Z_terms"] + row["open_gauge"]["CZ_terms"]
            + row["patch_gauge"]["Z_terms"] + row["patch_gauge"]["CZ_terms"] == 0
            for row in shuffled
        ),
        {
            "fixtures": len(shuffled),
            "semantic_failure_sum": semantic_sum,
            "locality_failures": locality_failures,
            "centralizer_span_failures": span_failures,
            "rank_table": tuple(
                (
                    row["shape"],
                    row["code_span"]["actual_stabilizer_rank"],
                    row["code_span"]["full_centralizer_dimension"],
                )
                for row in shuffled[::4]
            ),
        },
    )
    frames = port_frame_campaign()
    check(
        "the local-port representation closes 24 frames and all 576 frame products",
        frames["proper_cubic_frames"] == 24 and frames["semantic_failure_sum"] == 0
        and frames["ordered_frame_products"] == 576
        and frames["open_product_failures"] == 0
        and frames["patch_product_failures"] == 0
        and frames["inverse_failures"] == 0
        and frames["locality_failures"] == 0,
        frames,
    )
    shared = port_independent_overlap_campaign()
    check(
        "independently enumerated overlapping cubes need no transition terms",
        shared["independent_order_transition_terms"] == 0
        and shared["shared_augmented_addresses"] == 80
        and shared["shared_rail_addresses"] == 4
        and shared["graph_A_failures"] == 0,
        shared,
    )
    restrictions = common_coframe_restriction_campaign()
    check(
        "a common coframe restricts exactly from 3x2x2 to both overlapping cubes",
        restrictions["checks"] == 96
        and restrictions["failure_checks"] == 0
        and restrictions["maximum_difference"] == 0,
        restrictions,
    )
    features = feature_factoring_campaign()
    check(
        "every local gauge choice factors through local ports plus the finite proper-cubic frame",
        all(
            row["Z_feature_collisions"] == 0
            and row["pair_feature_collisions"] == 0
            and row["legacy_local_pair_order_collisions"] == 0
            and row["legacy_local_phase_collisions"] == 0
            for row in features.values()
        ),
        features,
    )
    coframe_falsifier = independent_coframe_falsifier()
    check(
        "the independent-coframe gluing gap remains active rather than silently supplied",
        coframe_falsifier["semantic_failure_sum"] == 0
        and coframe_falsifier["same_physical_cube"] == {
            "open_term_difference": 108,
            "patch_term_difference": 88,
        }
        and coframe_falsifier["overlap_open"]["term_difference"] == 46
        and coframe_falsifier["overlap_patch"]["term_difference"] == 42,
        coframe_falsifier,
    )
    inventory = supplied_inventory()
    summary = {
        "authority": "none",
        "audit": "unset",
        "claim_scope": (
            "bounded port-canonical signed-code compiler conditional on one common coframe; "
            "independent-chart gluing, genesis, and literal recurrence remain open"
        ),
        "pass": PASS,
        "fail": FAIL,
        "formula": "C_b = Q_patch(a->b) C_a N_a Q_open(a->b)^-1 N_b^-1",
        "Q_factorization": "Q = (product Z_orientation)(product CZ_incident_inversions) P_address",
        "legacy_local_match": legacy,
        "shuffled": {
            "fixtures": len(shuffled),
            "semantic_failure_sum": semantic_sum,
            "locality_failures": locality_failures,
            "centralizer_span_failures": span_failures,
            "transition_term_sum": sum(
                row["open_gauge"]["Z_terms"] + row["open_gauge"]["CZ_terms"]
                + row["patch_gauge"]["Z_terms"] + row["patch_gauge"]["CZ_terms"]
                for row in shuffled
            ),
            "rank_table": tuple(
                (
                    row["shape"],
                    row["code_span"]["actual_stabilizer_rank"],
                    row["code_span"]["full_centralizer_dimension"],
                )
                for row in shuffled[::4]
            ),
        },
        "frames": frames,
        "shared_ports": shared,
        "common_coframe_restrictions": restrictions,
        "local_feature_factoring": features,
        "independent_coframe_falsifier": coframe_falsifier,
        "inventory": inventory,
        "terminal": "CYCLE710_PORT_CANONICAL_COMMON_COFRAME_COMPILER_PASS",
    }
    print("SUMMARY_JSON", json.dumps(json_ready(summary), sort_keys=True))
    if FAIL:
        return 1
    print("CYCLE710_PORT_CANONICAL_COMMON_COFRAME_COMPILER_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
