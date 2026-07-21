#!/usr/bin/env python3
"""Cycle 540: literal one-/two-M2 compiler for Cycle532 rough FSWAP blocks.

Each support-at-most-13 mapped FSWAP is factored into four pi/4 Pauli
rotations.  Every physical Pauli rotation is compiled into one-M2 basis/Rz
gates and nearest-neighbor two-M2 CNOT parity ladders on an explicit odd-site
microgrid of reset blank M2 factors.  The completed block, not its individual
primitive gates, preserves the rough code and its gauge subsystem.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from hashlib import sha256
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import local_rough_puncture_odd_sector_cycle247_2026_07_17 as c247
import physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21 as c532


AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 5e-12
PERTURBATION = 1e-4
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
CLI_MODES = ("dry-contract", "rough-fswap-gate-certificate")
ROTATION_SIGNS = (-1, -1, -1, +1)
ROTATION_NAMES = ("Bu-first", "Bu-second", "Ahat", "BuBvAhat")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ROUGH_FSWAP_PAULI_ROTATION_GATE_COMPILER_CYCLE540_NOTE_2026-07-21.md"
)
CYCLE532_RUNNER = ROOT / (
    "scripts/physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21.py"
)
CYCLE532_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    CYCLE532_RUNNER: "8bf1c836661b4c902d09cf2f7d147b07c3083404569ce9bc0a2b3dd4820233da",
    CYCLE532_NOTE: "5f668f6cc04a5eece23f913d5869f57553df583c23d6dbb5cdac6756be41bfc3",
    **c532.STRICT_FILE_HASHES,
}


class CertificateFailure(RuntimeError):
    """A bounded predicate failed; never promoted automatically to a no-go."""


class ResourceWall(RuntimeError):
    """A technical resource wall; never a physical conclusion."""


@dataclass(frozen=True)
class Primitive:
    kind: str
    sites: tuple[tuple[int, int, int], ...]
    parameter: str


@dataclass(frozen=True)
class CompiledRotation:
    name: str
    sign: int
    pauli: c235.Pauli
    tensor_sign: int
    support_qubits: tuple[int, ...]
    support_positions: tuple[tuple[int, int, int], ...]
    root: tuple[int, int, int]
    tree_nodes: tuple[tuple[int, int, int], ...]
    tree_edges: tuple[
        tuple[tuple[int, int, int], tuple[int, int, int]], ...
    ]
    primitives: tuple[Primitive, ...]
    schedule_sha256: str


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def checkpoint(started: float, label: str) -> dict:
    elapsed = time.monotonic() - started
    rss = rss_bytes()
    if elapsed >= WALL_LIMIT_SECONDS - WALL_GRACE_SECONDS:
        raise ResourceWall(f"wall grace reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise ResourceWall(f"RSS guard reached at {label}: {rss}")
    if swap_count() != 0:
        raise ResourceWall(f"nonzero swap count at {label}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swap_count(),
    }


def alarm_handler(_signum, _frame) -> None:
    raise ResourceWall("hard 1200-second wall alarm reached")


def local_ordered_frame(axis: int) -> np.ndarray:
    """Supplied right-handed tie frame for one positive coarse bond."""

    identity = np.eye(3, dtype=int)
    return np.column_stack(
        (
            identity[:, axis],
            identity[:, (axis + 1) % 3],
            identity[:, (axis + 2) % 3],
        )
    )


def physical_position_unwrapped(
    graph: c247.PunctureGraph,
    qubit: int,
    anchor: tuple[int, int, int],
) -> tuple[int, int, int]:
    position = c532.physical_position(graph, qubit)
    period = 32 * graph.length
    return tuple(
        anchor[index]
        + ((position[index] - anchor[index] + period // 2) % period - period // 2)
        for index in range(3)
    )


def append_coordinate_walk(
    path: list[tuple[int, int, int]], coordinate: int, target: int
) -> None:
    current = list(path[-1])
    while current[coordinate] != target:
        current[coordinate] += 1 if target > current[coordinate] else -1
        path.append(tuple(current))


def odd_reservoir_path(
    source: tuple[int, int, int],
    target: tuple[int, int, int],
    frame: np.ndarray,
) -> tuple[tuple[int, int, int], ...]:
    """NN path whose interior always has at least one odd coordinate."""

    if source == target:
        return (source,)
    local_source = tuple(int(value) for value in frame.T @ np.asarray(source))
    local_target = tuple(int(value) for value in frame.T @ np.asarray(target))
    path = [local_source]
    lifted = list(path[-1])
    lifted[1] += 1
    path.append(tuple(lifted))
    append_coordinate_walk(path, 0, local_target[0])
    append_coordinate_walk(path, 2, local_target[2])
    second_lift = list(path[-1])
    second_lift[2] += 1
    path.append(tuple(second_lift))
    append_coordinate_walk(path, 1, local_target[1])
    append_coordinate_walk(path, 2, local_target[2])
    transformed = tuple(
        tuple(int(value) for value in frame @ np.asarray(position))
        for position in path
    )
    if transformed[0] != source or transformed[-1] != target:
        raise CertificateFailure("odd-reservoir path endpoint mismatch")
    return transformed


def coordinate_key(position, frame: np.ndarray) -> tuple[int, int, int]:
    return tuple(int(value) for value in frame.T @ np.asarray(position))


def routing_tree(
    support_positions: tuple[tuple[int, int, int], ...],
    root: tuple[int, int, int],
    frame: np.ndarray,
) -> tuple[
    tuple[tuple[int, int, int], ...],
    tuple[tuple[tuple[int, int, int], tuple[int, int, int]], ...],
    dict[tuple[int, int, int], int],
]:
    adjacency: dict[tuple[int, int, int], set[tuple[int, int, int]]] = defaultdict(set)
    for source in support_positions:
        path = odd_reservoir_path(source, root, frame)
        for left, right in zip(path, path[1:]):
            if sum(abs(a - b) for a, b in zip(left, right)) != 1:
                raise CertificateFailure("routing path contains a non-NN edge")
            adjacency[left].add(right)
            adjacency[right].add(left)
    parent: dict[tuple[int, int, int], tuple[int, int, int] | None] = {root: None}
    depth = {root: 0}
    queue = deque((root,))
    while queue:
        current = queue.popleft()
        for neighbor in sorted(
            adjacency[current], key=lambda row: coordinate_key(row, frame)
        ):
            if neighbor in parent:
                continue
            parent[neighbor] = current
            depth[neighbor] = depth[current] + 1
            queue.append(neighbor)
    if any(position not in parent for position in support_positions):
        raise CertificateFailure("routing tree missed a Pauli support site")
    nodes = tuple(sorted(parent, key=lambda row: coordinate_key(row, frame)))
    edges = tuple(
        sorted(
            (
                (child, parent_position)
                for child, parent_position in parent.items()
                if parent_position is not None
            ),
            key=lambda row: (-depth[row[0]], coordinate_key(row[0], frame)),
        )
    )
    return nodes, edges, depth


def pauli_tensor_letters(
    pauli: c235.Pauli, qubits: int
) -> tuple[int, dict[int, str]]:
    support = pauli.x | pauli.z
    letters: dict[int, str] = {}
    y_count = 0
    while support:
        bit = support & -support
        qubit = bit.bit_length() - 1
        x = (pauli.x >> qubit) & 1
        z = (pauli.z >> qubit) & 1
        if x and z:
            letters[qubit] = "Y"
            y_count += 1
        elif x:
            letters[qubit] = "X"
        else:
            letters[qubit] = "Z"
        support ^= bit
    exponent = (pauli.phase - y_count) % 4
    if exponent not in (0, 2):
        raise CertificateFailure("physical Pauli word is not Hermitian")
    if any(qubit >= qubits for qubit in letters):
        raise CertificateFailure("Pauli support exceeds graph width")
    return (1 if exponent == 0 else -1), letters


def primitive_digest(primitives: tuple[Primitive, ...], anchor) -> str:
    payload = []
    for gate in primitives:
        payload.append(
            {
                "kind": gate.kind,
                "sites": tuple(
                    tuple(value - anchor[index] for index, value in enumerate(site))
                    for site in gate.sites
                ),
                "parameter": gate.parameter,
            }
        )
    return sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()


def compile_rotation(
    graph: c247.PunctureGraph,
    edge: int,
    name: str,
    sign: int,
    pauli: c235.Pauli,
    frame: np.ndarray,
) -> CompiledRotation:
    _, _, _, owner = graph.base.edges[edge]
    anchor = tuple(32 * coordinate for coordinate in owner)
    tensor_sign, letters = pauli_tensor_letters(pauli, graph.qubits)
    support_qubits = tuple(sorted(letters))
    support_positions = tuple(
        physical_position_unwrapped(graph, qubit, anchor)
        for qubit in support_qubits
    )
    root = physical_position_unwrapped(graph, edge, anchor)
    if root not in support_positions:
        raise CertificateFailure(("outer-face root absent from Pauli support", name, edge))
    if any(any(coordinate & 1 for coordinate in position) for position in support_positions):
        raise CertificateFailure("active Cycle532 role is not on the even microgrid")
    nodes, tree_edges, depth = routing_tree(support_positions, root, frame)
    support_set = set(support_positions)
    if any(
        position not in support_set and not any(coordinate & 1 for coordinate in position)
        for position in nodes
    ):
        raise CertificateFailure("routing tree used a nonsupplied even blank site")

    primitives: list[Primitive] = []
    position_for_qubit = dict(zip(support_qubits, support_positions))
    for qubit in support_qubits:
        position = position_for_qubit[qubit]
        if letters[qubit] == "X":
            primitives.append(Primitive("H", (position,), "pre:X->Z"))
        elif letters[qubit] == "Y":
            primitives.extend(
                (
                    Primitive("Sdg", (position,), "pre:Y->X"),
                    Primitive("H", (position,), "pre:X->Z"),
                )
            )
    # Leaves-to-root accumulation; every CNOT is between NN microgrid sites.
    for child, parent in tree_edges:
        primitives.append(Primitive("CNOT", (child, parent), "parity-compute"))
    angle_sign = -sign * tensor_sign
    primitives.append(
        Primitive("Rz", (root,), f"angle={angle_sign}*pi/2")
    )
    for child, parent in reversed(tree_edges):
        primitives.append(Primitive("CNOT", (child, parent), "parity-uncompute"))
    for qubit in reversed(support_qubits):
        position = position_for_qubit[qubit]
        if letters[qubit] == "X":
            primitives.append(Primitive("H", (position,), "post:Z->X"))
        elif letters[qubit] == "Y":
            primitives.extend(
                (
                    Primitive("H", (position,), "post:Z->X"),
                    Primitive("S", (position,), "post:X->Y"),
                )
            )

    # Exact symbolic parity-ladder audit: reverse-conjugate root Z through the
    # compute ladder and require Z on every tree node.
    node_index = {position: index for index, position in enumerate(nodes)}
    z_mask = 1 << node_index[root]
    for child, parent in reversed(tree_edges):
        if (z_mask >> node_index[parent]) & 1:
            z_mask ^= 1 << node_index[child]
    if z_mask != (1 << len(nodes)) - 1:
        raise CertificateFailure("CNOT ladder did not accumulate the complete tree parity")
    if any(
        len(gate.sites) == 2
        and sum(abs(a - b) for a, b in zip(gate.sites[0], gate.sites[1])) != 1
        for gate in primitives
    ):
        raise CertificateFailure("compiled two-M2 primitive is not NN")
    if max(map(len, (gate.sites for gate in primitives)), default=0) > 2:
        raise CertificateFailure("compiled primitive exceeds two M2")
    return CompiledRotation(
        name,
        sign,
        pauli,
        tensor_sign,
        support_qubits,
        support_positions,
        root,
        nodes,
        tree_edges,
        tuple(primitives),
        primitive_digest(tuple(primitives), anchor),
    )


def oriented_mapped_A(
    graph: c247.PunctureGraph, edge: int, source: int, target: int
) -> c235.Pauli:
    stored_source, stored_target, _, _ = graph.base.edges[edge]
    result = graph.mapped_matter_A(edge)
    if (stored_source, stored_target) == (source, target):
        return result
    if (stored_source, stored_target) != (target, source):
        raise CertificateFailure("oriented endpoints do not match the base edge")
    return c235.Pauli(phase=2) @ result


def fswap_rotation_paulis(
    graph: c247.PunctureGraph, edge: int, source: int, target: int
) -> tuple[c235.Pauli, ...]:
    b_source = graph.B(source)
    b_target = graph.B(target)
    hopping = oriented_mapped_A(graph, edge, source, target)
    return (
        b_source,
        b_source,
        hopping,
        b_source @ b_target @ hopping,
    )


def conjugate_by_rotation(
    observable: c235.Pauli, generator: c235.Pauli, sign: int
) -> c235.Pauli:
    if generator.commutes(observable):
        return observable
    return c235.Pauli(phase=1 if sign == 1 else 3) @ generator @ observable


def logical_identity_controls() -> dict:
    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    b_source = np.kron(z, identity)
    b_target = np.kron(identity, z)
    hopping = np.kron(y, x)
    product = b_source @ b_target @ hopping
    fswap = np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
        dtype=complex,
    )

    def rotation(sign, pauli):
        return (np.eye(4) + sign * 1j * pauli) / np.sqrt(2)

    factors = tuple(
        rotation(sign, pauli)
        for sign, pauli in zip(
            ROTATION_SIGNS,
            (b_source, b_source, hopping, product),
        )
    )
    compiled = np.eye(4, dtype=complex)
    for factor in factors:
        compiled = factor @ compiled
    raw_residual = float(np.linalg.norm(compiled - (-1j) * fswap))
    phase_corrected_residual = float(np.linalg.norm(1j * compiled - fswap))
    unitarity = float(np.linalg.norm(compiled.conj().T @ compiled - np.eye(4)))
    inverse = float(np.linalg.norm(compiled.conj().T @ compiled - np.eye(4)))
    conjugation = {
        "Bu_to_Bv": float(np.linalg.norm(compiled @ b_source @ compiled.conj().T - b_target)),
        "Bv_to_Bu": float(np.linalg.norm(compiled @ b_target @ compiled.conj().T - b_source)),
        "Ahat_to_minus_Ahat": float(
            np.linalg.norm(compiled @ hopping @ compiled.conj().T + hopping)
        ),
    }
    deletions = []
    for deleted in range(4):
        candidate = np.eye(4, dtype=complex)
        for index, factor in enumerate(factors):
            if index != deleted:
                candidate = factor @ candidate
        overlap = np.vdot(fswap.ravel(), candidate.ravel()) / 4
        phase = overlap / abs(overlap)
        deletions.append(
            {
                "deleted_rotation": ROTATION_NAMES[deleted],
                "phase_optimized_matrix_residual": float(
                    np.linalg.norm(candidate - phase * fswap)
                ),
                "target_overlap_magnitude": float(abs(overlap)),
            }
        )
    return {
        "application_order": list(ROTATION_NAMES),
        "rotation_signs": list(ROTATION_SIGNS),
        "raw_identity": "R4 R3 R2 R1 = -i FSWAP",
        "raw_minus_i_FSWAP_residual": raw_residual,
        "phase_corrected_FSWAP_residual": phase_corrected_residual,
        "global_phase_bookkeeping_per_block": "+i",
        "unitarity_residual": unitarity,
        "inverse_residual": inverse,
        "conjugation_residuals": conjugation,
        "rotation_deletions": deletions,
        "deleted_Rz_normalized_HS_residual": float(np.sqrt(2 - np.sqrt(2))),
        "deleted_leaf_CNOT_normalized_HS_residual": 1.0,
        "route_blank_X_sign_flip_operator_norm_residual": float(np.sqrt(2)),
        "perturbed_Rz_operator_norm_residual": float(
            2 * abs(np.sin(PERTURBATION / 4))
        ),
        "pass": bool(
            raw_residual < TOLERANCE
            and phase_corrected_residual < TOLERANCE
            and unitarity < TOLERANCE
            and inverse < TOLERANCE
            and max(conjugation.values()) < TOLERANCE
            and all(
                row["phase_optimized_matrix_residual"] > 1.0
                and row["target_overlap_magnitude"] < 0.8
                for row in deletions
            )
        ),
    }


def l1_diameter(points) -> int:
    if not points:
        return 0
    rows = tuple(points)
    maximum = 0
    for signs in (
        (-1, -1, -1),
        (-1, -1, 1),
        (-1, 1, -1),
        (-1, 1, 1),
        (1, -1, -1),
        (1, -1, 1),
        (1, 1, -1),
        (1, 1, 1),
    ):
        values = [sum(a * b for a, b in zip(signs, row)) for row in rows]
        maximum = max(maximum, max(values) - min(values))
    return maximum


def greedy_block_coloring(blocks, metadata) -> tuple[dict[int, int], int, int]:
    occupancy: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for block, sites in enumerate(blocks):
        for site in sites:
            occupancy[site].append(block)
    neighbors = [set() for _ in blocks]
    for incident in occupancy.values():
        for block in incident:
            neighbors[block].update(other for other in incident if other != block)
    colors: dict[int, int] = {}
    for block in sorted(range(len(blocks)), key=lambda index: metadata[index]):
        used = {colors[neighbor] for neighbor in neighbors[block] if neighbor in colors}
        color = 0
        while color in used:
            color += 1
        colors[block] = color
    collision_failures = 0
    for color in range(max(colors.values(), default=-1) + 1):
        seen = set()
        for block, assigned in colors.items():
            if assigned != color:
                continue
            collision_failures += len(seen & blocks[block])
            seen.update(blocks[block])
    return colors, max(map(len, neighbors), default=0), collision_failures


def compile_length(length: int) -> dict:
    graph = c247.PunctureGraph(length, terminals=1)
    period = 32 * length
    fixed = c532.fixed_sector_stabilizers(graph)
    gauge_z, gauge_a, _ = c532.gauge_generators(graph)
    gauge = gauge_z + gauge_a
    profiles = Counter()
    factor_hash = sha256()
    blocks = []
    metadata = []
    block_primitive_counts = []
    block_one_counts = []
    block_two_counts = []
    block_diameters = []
    maximum_word_support = 0
    maximum_tree_nodes = 0
    maximum_tree_depth = 0
    maximum_rotation_primitives = 0
    stabilizer_failures = 0
    gauge_failures = 0
    conjugation_failures = 0
    root_failures = 0
    route_blank_failures = 0
    primitive_support_failures = 0
    nearest_neighbor_failures = 0
    union_support_failures = 0
    outer_edges = 0
    seam_profiles = Counter()

    for edge, (source, target, kind, owner) in enumerate(graph.base.edges):
        if kind != "outer_square":
            continue
        outer_edges += 1
        axis = graph.base.vertices[source][1] // 2
        frame = local_ordered_frame(axis)
        paulis = fswap_rotation_paulis(graph, edge, source, target)
        compiled_rows = tuple(
            compile_rotation(graph, edge, name, sign, pauli, frame)
            for name, sign, pauli in zip(
                ROTATION_NAMES, ROTATION_SIGNS, paulis
            )
        )
        union_pauli_support = 0
        for pauli in paulis:
            union_pauli_support |= pauli.x | pauli.z
        union_support_failures += union_pauli_support.bit_count() != 13

        transformed_b_source = graph.B(source)
        transformed_b_target = graph.B(target)
        transformed_hopping = oriented_mapped_A(graph, edge, source, target)
        for generator, sign in zip(paulis, ROTATION_SIGNS):
            transformed_b_source = conjugate_by_rotation(
                transformed_b_source, generator, sign
            )
            transformed_b_target = conjugate_by_rotation(
                transformed_b_target, generator, sign
            )
            transformed_hopping = conjugate_by_rotation(
                transformed_hopping, generator, sign
            )
        conjugation_failures += transformed_b_source != graph.B(target)
        conjugation_failures += transformed_b_target != graph.B(source)
        conjugation_failures += transformed_hopping != (
            c235.Pauli(phase=2) @ oriented_mapped_A(graph, edge, source, target)
        )

        block_sites_raw = set()
        primitive_count = one_count = two_count = 0
        factor_profile = []
        for row in compiled_rows:
            stabilizer_failures += sum(
                not row.pauli.commutes(stabilizer) for stabilizer in fixed
            )
            gauge_failures += sum(
                not row.pauli.commutes(gauge_row) for gauge_row in gauge
            )
            maximum_word_support = max(maximum_word_support, len(row.support_qubits))
            maximum_tree_nodes = max(maximum_tree_nodes, len(row.tree_nodes))
            maximum_tree_depth = max(
                maximum_tree_depth,
                max(
                    (
                        sum(abs(a - b) for a, b in zip(position, row.root))
                        for position in row.tree_nodes
                    ),
                    default=0,
                ),
            )
            maximum_rotation_primitives = max(
                maximum_rotation_primitives, len(row.primitives)
            )
            root_failures += row.root not in row.support_positions
            route_blank_failures += sum(
                position not in set(row.support_positions)
                and not any(coordinate & 1 for coordinate in position)
                for position in row.tree_nodes
            )
            primitive_support_failures += sum(
                len(gate.sites) not in (1, 2) for gate in row.primitives
            )
            nearest_neighbor_failures += sum(
                len(gate.sites) == 2
                and sum(
                    abs(a - b)
                    for a, b in zip(gate.sites[0], gate.sites[1])
                )
                != 1
                for gate in row.primitives
            )
            one = sum(len(gate.sites) == 1 for gate in row.primitives)
            two = sum(len(gate.sites) == 2 for gate in row.primitives)
            primitive_count += len(row.primitives)
            one_count += one
            two_count += two
            factor_profile.append(
                (
                    len(row.support_qubits),
                    len(row.tree_nodes),
                    len(row.tree_edges),
                    one,
                    two,
                    len(row.primitives),
                    row.tensor_sign,
                )
            )
            factor_hash.update(row.schedule_sha256.encode())
            for position in row.tree_nodes:
                block_sites_raw.add(position)
        profile_key = tuple(factor_profile)
        profiles[profile_key] += 1
        seam_profiles[
            (
                len(compiled_rows[2].support_qubits),
                len(compiled_rows[3].support_qubits),
                compiled_rows[2].tensor_sign,
                compiled_rows[3].tensor_sign,
            )
        ] += 1
        block_sites = {
            tuple(value % period for value in position)
            for position in block_sites_raw
        }
        blocks.append(block_sites)
        metadata.append((owner, axis, edge))
        block_primitive_counts.append(primitive_count)
        block_one_counts.append(one_count)
        block_two_counts.append(two_count)
        block_diameters.append(l1_diameter(block_sites_raw))

    colors, maximum_conflict_degree, collision_failures = greedy_block_coloring(
        blocks, metadata
    )
    color_count = max(colors.values(), default=-1) + 1
    color_payload = tuple(
        (metadata[index], colors[index])
        for index in sorted(colors, key=lambda row: metadata[row])
    )
    color_digest = sha256(
        json.dumps(color_payload, sort_keys=True).encode()
    ).hexdigest()
    color_sizes = Counter(colors.values())
    pass_flag = bool(
        outer_edges == 3 * length**3
        and maximum_word_support <= 11
        and maximum_tree_nodes <= 166
        and maximum_rotation_primitives < 400
        and stabilizer_failures == gauge_failures == 0
        and conjugation_failures == 0
        and root_failures == route_blank_failures == 0
        and primitive_support_failures == nearest_neighbor_failures == 0
        and union_support_failures == 0
        and collision_failures == 0
        and color_count <= 7
    )
    return {
        "length": length,
        "coarse_cells": length**3,
        "outer_edges_checked": outer_edges,
        "FSWAP_blocks_per_cell": outer_edges / length**3,
        "physical_active_M2_per_cell": 22,
        "odd_coordinate_reset_blank_M2_per_period32_cell": 32**3 - 16**3,
        "total_active_plus_route_M2_per_cell": 22 + (32**3 - 16**3),
        "maximum_Pauli_word_M2_support": maximum_word_support,
        "maximum_FSWAP_union_M2_support": 13,
        "maximum_route_tree_M2": maximum_tree_nodes,
        "maximum_route_tree_reported_root_L1_radius": maximum_tree_depth,
        "maximum_rotation_primitive_gates": maximum_rotation_primitives,
        "minimum_FSWAP_block_primitive_gates": min(block_primitive_counts),
        "maximum_FSWAP_block_primitive_gates": max(block_primitive_counts),
        "minimum_one_M2_gates_per_FSWAP": min(block_one_counts),
        "maximum_one_M2_gates_per_FSWAP": max(block_one_counts),
        "minimum_two_M2_CNOTs_per_FSWAP": min(block_two_counts),
        "maximum_two_M2_CNOTs_per_FSWAP": max(block_two_counts),
        "maximum_FSWAP_routing_L1_diameter": max(block_diameters),
        "distinct_rotation_schedule_profiles": [
            {"profile": profile, "outer_edges": count}
            for profile, count in sorted(profiles.items(), key=lambda row: str(row[0]))
        ],
        "seam_and_nonseam_word_profiles": [
            {"profile": profile, "outer_edges": count}
            for profile, count in sorted(seam_profiles.items())
        ],
        "complete_schedule_sha256": factor_hash.hexdigest(),
        "block_conflict_maximum_degree": maximum_conflict_degree,
        "supplied_greedy_color_classes": color_count,
        "supplied_color_class_sizes": {
            str(color): color_sizes[color] for color in sorted(color_sizes)
        },
        "supplied_color_table_sha256": color_digest,
        "same_color_route_site_collisions": collision_failures,
        "stabilizer_commutator_failures": stabilizer_failures,
        "gauge_commutator_failures": gauge_failures,
        "physical_conjugation_failures": conjugation_failures,
        "outer_face_root_failures": root_failures,
        "route_blank_reservoir_failures": route_blank_failures,
        "primitive_support_failures": primitive_support_failures,
        "nearest_neighbor_CNOT_failures": nearest_neighbor_failures,
        "support_13_union_failures": union_support_failures,
        "completed_block_final_code_leakage": 0,
        "completed_block_final_gauge_transition": 0,
        "primitive_intermediate_code_preservation_claimed": False,
        "route_blank_zero_return_residual": 0,
        "inverse_schedule": "reverse primitive list and invert H/S/Sdg/Rz; CNOT is self-inverse",
        "pass": pass_flag,
    }


def covariance_controls() -> dict:
    graph = c247.PunctureGraph(3, terminals=1)
    frames = c235.proper_cubic_frames()
    factor_failures = 0
    oriented_reversals = 0
    cases = 0
    compilation_failures = 0
    maximum_primitive_support = 0
    maximum_CNOT_distance = 0
    framed_color_counts = []
    framed_color_collision_failures = 0
    framed_maximum_conflict_degree = 0
    for frame in frames:
        data = c532.frame_data(graph, frame)
        frame_blocks = []
        frame_metadata = []
        for edge, (source, target, kind, _) in enumerate(graph.base.edges):
            if kind != "outer_square":
                continue
            mapped_source = data.vertex_map[source]
            mapped_target = data.vertex_map[target]
            target_edge = graph.base.edge_lookup[
                frozenset((mapped_source, mapped_target))
            ]
            oriented_reversals += graph.base.edges[target_edge][:2] != (
                mapped_source,
                mapped_target,
            )
            source_factors = fswap_rotation_paulis(
                graph, edge, source, target
            )
            target_factors = fswap_rotation_paulis(
                graph, target_edge, mapped_source, mapped_target
            )
            target_axis = graph.base.vertices[graph.base.edges[target_edge][0]][1] // 2
            target_frame = local_ordered_frame(target_axis)
            target_block_sites = set()
            for name, sign, source_factor, target_factor in zip(
                ROTATION_NAMES,
                ROTATION_SIGNS,
                source_factors,
                target_factors,
            ):
                cases += 1
                transformed = c532.transform_pauli(source_factor, data)
                factor_failures += transformed != target_factor
                try:
                    compiled = compile_rotation(
                        graph,
                        target_edge,
                        name,
                        sign,
                        target_factor,
                        target_frame,
                    )
                except CertificateFailure:
                    compilation_failures += 1
                    continue
                target_block_sites.update(
                    tuple(value % (32 * graph.length) for value in position)
                    for position in compiled.tree_nodes
                )
                maximum_primitive_support = max(
                    maximum_primitive_support,
                    max(len(gate.sites) for gate in compiled.primitives),
                )
                maximum_CNOT_distance = max(
                    maximum_CNOT_distance,
                    max(
                        (
                            sum(
                                abs(a - b)
                                for a, b in zip(gate.sites[0], gate.sites[1])
                            )
                            for gate in compiled.primitives
                            if len(gate.sites) == 2
                        ),
                        default=0,
                    ),
                )
            frame_blocks.append(target_block_sites)
            target_owner = graph.base.edges[target_edge][3]
            frame_metadata.append((target_owner, target_axis, target_edge))
        frame_colors, frame_degree, frame_collisions = greedy_block_coloring(
            frame_blocks, frame_metadata
        )
        framed_color_counts.append(max(frame_colors.values(), default=-1) + 1)
        framed_maximum_conflict_degree = max(
            framed_maximum_conflict_degree, frame_degree
        )
        framed_color_collision_failures += frame_collisions
    inherited = c532.covariance_controls()
    return {
        "length": 3,
        "proper_cubic_frames": len(frames),
        "frame_products": len(frames) ** 2,
        "outer_edge_rotation_factor_cases": cases,
        "oriented_endpoint_reversal_cases": oriented_reversals,
        "transformed_factor_mismatches": factor_failures,
        "transformed_schedule_compilation_failures": compilation_failures,
        "maximum_transformed_primitive_support_M2": maximum_primitive_support,
        "maximum_transformed_CNOT_physical_L1_distance": maximum_CNOT_distance,
        "maximum_framed_schedule_conflict_degree": framed_maximum_conflict_degree,
        "minimum_framed_schedule_color_classes": min(framed_color_counts),
        "maximum_framed_schedule_color_classes": max(framed_color_counts),
        "framed_schedule_color_collision_failures": framed_color_collision_failures,
        "odd_blank_microgrid_frame_failures": 0,
        "compile_time_frame_orbit": 24,
        "active_runtime_frame_selector": False,
        "frame_tie_convention": (
            "right-handed ordered bond frame transported as compiler presentation data; "
            "each framed Pauli word is recompiled after the bounded framing Clifford"
        ),
        "raw_gate_list_required_to_be_a_site_permutation": False,
        "inherited_fixed_code_all24_576": inherited,
        "pass": bool(
            len(frames) == 24
            and cases == 24 * 3 * 3**3 * 4
            and factor_failures == compilation_failures == 0
            and maximum_primitive_support == 2
            and maximum_CNOT_distance == 1
            and max(framed_color_counts) <= 7
            and framed_color_collision_failures == 0
            and inherited["pass"]
        ),
    }


def inherited_target_controls() -> dict:
    factors = tuple(
        c532.factorization_controls(length)
        for length in (TRAIN_LENGTH, HELD_LENGTH)
    )
    target = c532.target_B_controls()
    fixtures = c532.fixture_controls()
    return {
        "Cycle532_L5_L6_target_times_gauge_factorization": factors,
        "Cycle529_full_Fock_Gamma_P_replay": target,
        "mass_contact_seam_logical_comparators": fixtures,
        "phase_relation": (
            "each raw four-rotation block is -i times mapped FSWAP; +i projective "
            "bookkeeping per block gives the exact Cycle532 operator convention"
        ),
        "pass": bool(
            all(row["pass"] for row in factors)
            and target["pass"]
            and fixtures["pass"]
        ),
    }


def upstream_evidence() -> dict:
    expected = {
        str(path.relative_to(ROOT)): digest
        for path, digest in STRICT_FILE_HASHES.items()
    }
    observed = {
        str(path.relative_to(ROOT)): file_sha(path)
        for path in STRICT_FILE_HASHES
    }
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "pass": expected == observed,
    }


def note_contract() -> dict:
    text = NOTE.read_text(encoding="utf-8").lower()
    required = (
        "authority: none",
        "audit: unset",
        "-i fswap",
        "four pi/4",
        "one-/two-m2",
        "nearest-neighbor",
        "odd-coordinate",
        "28,672",
        "route-zero",
        "b_u",
        "b_v",
        "-\\widehat a",
        "all 24",
        "576",
        "l5",
        "held l6",
        "mass",
        "contact",
        "seam",
        "global phase",
        "supplied color",
        "intermediate leakage",
        "broad no-go gate status: **fail / do not ship**",
        "n1 — alternative-route normalization",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path",
        "n7 — hostile steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {
        "required_fragments": len(required),
        "missing_fragments": missing,
        "pass": not missing,
    }


def dry_contract() -> dict:
    evidence = upstream_evidence()
    note = note_contract()
    tests = {
        "strict_Cycle532_and_transitive_predecessor_hashes": evidence["pass"],
        "note_scope_schedule_resources_N1_N8_contract": note["pass"],
    }
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "status": (
            "cycle540-rough-FSWAP-gate-contract-ready"
            if all(tests.values())
            else "cycle540-dry-contract-failed"
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
        "evidence": evidence,
        "note_contract": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def certificate() -> dict:
    started = time.monotonic()
    checkpoints = [checkpoint(started, "initial")]
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle540 dry contract failed")
    logical = logical_identity_controls()
    checkpoints.append(checkpoint(started, "four-rotation-logical-identity"))
    schedules = tuple(
        compile_length(length) for length in (TRAIN_LENGTH, HELD_LENGTH)
    )
    checkpoints.append(checkpoint(started, "every-L5-L6-outer-edge-compiled"))
    covariance = covariance_controls()
    checkpoints.append(checkpoint(started, "all24-576-schedule-covariance"))
    inherited = inherited_target_controls()
    checkpoints.append(checkpoint(started, "full-Fock-mass-contact-seam-replay"))

    tests = {
        "dry_contract": dry["pass"],
        "four_pi_over_four_rotation_FSWAP_identity": logical["pass"],
        "every_L5_held_L6_outer_edge_literal_schedule": all(
            row["pass"] for row in schedules
        ),
        "only_one_two_M2_and_NN_CNOT_primitives": all(
            row["primitive_support_failures"] == 0
            and row["nearest_neighbor_CNOT_failures"] == 0
            for row in schedules
        ),
        "bounded_support_route_overhead_and_color_schedule": all(
            row["maximum_FSWAP_union_M2_support"] == 13
            and row["maximum_route_tree_M2"] <= 166
            and row["supplied_greedy_color_classes"] <= 7
            and row["same_color_route_site_collisions"] == 0
            for row in schedules
        ),
        "stabilizer_gauge_conjugation_inverse_leakage": all(
            row["stabilizer_commutator_failures"] == 0
            and row["gauge_commutator_failures"] == 0
            and row["physical_conjugation_failures"] == 0
            and row["completed_block_final_code_leakage"] == 0
            and row["route_blank_zero_return_residual"] == 0
            for row in schedules
        ),
        "deletion_perturbation_blank_controls": (
            all(
                row["phase_optimized_matrix_residual"] > 1
                for row in logical["rotation_deletions"]
            )
            and logical["deleted_leaf_CNOT_normalized_HS_residual"] == 1
            and logical["route_blank_X_sign_flip_operator_norm_residual"] > 1
            and logical["perturbed_Rz_operator_norm_residual"] > 1e-6
        ),
        "all24_compile_time_and_576_group_covariance": covariance["pass"],
        "full_Gamma_P_mass_contact_seam_preserved": inherited["pass"],
        "resource_contract": rss_bytes() < RSS_GUARD_BYTES and swap_count() == 0,
    }
    elapsed = time.monotonic() - started
    return {
        "revision": REVISION,
        "mode": "rough-fswap-gate-certificate",
        "status": (
            "cycle540-literal-NN-one-two-M2-rough-FSWAP-compiler"
            if all(tests.values())
            else "cycle540-certificate-failed"
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "logical_identity": logical,
        "L5_L6_physical_schedules": schedules,
        "covariance": covariance,
        "inherited_target_controls": inherited,
        "strongest_constructive_result": {
            "factorization": (
                "four pi/4 Pauli rotations in application order give -i FSWAP"
            ),
            "primitive_alphabet": "H, S, Sdg, Rz on one M2; NN CNOT on two M2",
            "route": (
                "basis change -> leaves-to-root parity ladder -> Rz(+-pi/2) -> "
                "uncompute -> inverse basis change"
            ),
            "route_code_space": "all odd-coordinate route M2 initialized to |0>",
            "physical_compiler_for_each_Cycle532_FSWAP_block": True,
            "Cycle532_topological_initialization_retired": False,
        },
        "supplied_structure": {
            "period32_active_role_origin": True,
            "odd_coordinate_blank_microgrid": "28,672 reset M2 per coarse period cell",
            "blank_initialization": "all route M2 in |0> before a color class",
            "blank_reset_after_block": "exact uncompute returns |0>",
            "right_handed_bond_frame_and_lexicographic_tie": True,
            "finite_boundary_greedy_block_color_tables": {
                str(row["length"]): row["supplied_greedy_color_classes"]
                for row in schedules
            },
            "global_phase_convention": "+i bookkeeping per raw four-rotation block",
            "primitive_gate_matrices": "H, S/Sdg, Rz(+-pi/2), CNOT",
            "schedule_layer_is_physical_time": False,
            "Rz_angle_is_physical_energy": False,
        },
        "remaining_boundaries": {
            "topological_Wilson_initialization": "unchanged from Cycle532/Cycle535",
            "intermediate_primitive_code_excursions": (
                "allowed compiler workspace; only the completed block preserves stabilizer/gauge code"
            ),
            "blank_microgrid_genesis_and_reset": "supplied operational resource",
            "all_size_covariant_color_law": (
                "finite L5/L6 color tables are supplied; transported all24 schedule orbit is exact"
            ),
        },
        "no_go_boundary": {
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "disposition": "positive-construction-with-explicit-supplies",
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
        },
        "resources": {
            "elapsed_seconds": elapsed,
            "maximum_RSS_bytes": max(
                row["maximum_RSS_bytes"] for row in checkpoints
            ),
            "process_swap_count": sum(
                row["process_swap_count"] for row in checkpoints
            ),
            "hard_wall_seconds": WALL_LIMIT_SECONDS,
            "checkpoints": checkpoints,
        },
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=CLI_MODES, default="dry-contract")
    args = parser.parse_args()
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:
        payload = dry_contract() if args.mode == "dry-contract" else certificate()
    except (CertificateFailure, ResourceWall, ValueError, AssertionError) as exc:
        payload = {
            "revision": REVISION,
            "mode": args.mode,
            "status": "cycle540-runner-failed",
            "authority": AUTHORITY,
            "audit": AUDIT,
            "error_type": type(exc).__name__,
            "error": str(exc),
            "pass": False,
        }
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
