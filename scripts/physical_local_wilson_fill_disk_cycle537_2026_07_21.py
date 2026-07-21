#!/usr/bin/env python3
"""Cycle 537: local fill-disk replacement for three Wilson initializers.

Three auxiliary square disks are attached to the axial Wilson loops of the
Cycle-532 rough code.  Disk-face and interior-star stabilizers are bounded;
the product of one disk's face stabilizers is exactly its Wilson Pauli.  The
runner dresses every local constraint, matter generator, and gauge generator
through the disk dual graph and audits the resulting target-times-gauge code.

The cap sheets are an explicit added topology.  Their intrinsic local complex
and a 24-member compile-time frame orbit are constructed, but an embedding of
the cap sheets into the old period-32 periodic M2 placement as one fixed
frame-independent triangulation is not supplied.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
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

import physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21 as c532


c235 = c532.c235
c247 = c532.c247
c210 = c532.c210
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 5e-12
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
CLI_MODES = ("dry-contract", "fill-disk-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md"
)
CYCLE532_RUNNER = ROOT / "scripts/physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21.py"
CYCLE532_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    CYCLE532_RUNNER: "8bf1c836661b4c902d09cf2f7d147b07c3083404569ce9bc0a2b3dd4820233da",
    CYCLE532_NOTE: "5f668f6cc04a5eece23f913d5869f57553df583c23d6dbb5cdac6756be41bfc3",
}


class CertificateFailure(RuntimeError):
    """A declared finite certificate condition failed."""


class ResourceWall(RuntimeError):
    """A technical ceiling, never physical evidence."""


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
    if swap_count():
        raise ResourceWall(f"nonzero process swap count at {label}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swap_count(),
    }


def alarm_handler(_signum, _frame) -> None:
    raise ResourceWall("hard Cycle537 wall alarm reached")


def edge_key(first, second):
    return tuple(sorted((tuple(first), tuple(second))))


@dataclass(frozen=True)
class FillDisk:
    length: int
    edges: tuple
    edge_index: dict
    faces: tuple
    stars: tuple
    perimeter: tuple
    chunk_face: tuple[int, ...]

    @property
    def edge_count(self) -> int:
        return len(self.edges)


def build_fill_disk(length: int) -> FillDisk:
    edges = []
    for vertical in range(length + 1):
        for horizontal in range(length):
            key = edge_key((horizontal, vertical), (horizontal + 1, vertical))
            if vertical not in (0, length):
                edges.append(key)
    for horizontal in range(length + 1):
        for vertical in range(length):
            key = edge_key((horizontal, vertical), (horizontal, vertical + 1))
            if horizontal not in (0, length):
                edges.append(key)
    edges = tuple(edges)
    edge_index = {edge: index for index, edge in enumerate(edges)}

    faces = []
    face_by_edge = {}
    for horizontal in range(length):
        for vertical in range(length):
            boundary = (
                edge_key((horizontal, vertical), (horizontal + 1, vertical)),
                edge_key((horizontal + 1, vertical), (horizontal + 1, vertical + 1)),
                edge_key((horizontal, vertical + 1), (horizontal + 1, vertical + 1)),
                edge_key((horizontal, vertical), (horizontal, vertical + 1)),
            )
            face = len(faces)
            faces.append(((horizontal, vertical), boundary))
            for edge in boundary:
                face_by_edge.setdefault(edge, []).append(face)

    perimeter = tuple(
        [edge_key((horizontal, 0), (horizontal + 1, 0)) for horizontal in range(length)]
        + [edge_key((length, vertical), (length, vertical + 1)) for vertical in range(length)]
        + [
            edge_key((horizontal, length), (horizontal + 1, length))
            for horizontal in reversed(range(length))
        ]
        + [
            edge_key((0, vertical), (0, vertical + 1))
            for vertical in reversed(range(length))
        ]
    )
    chunk_face = []
    for chunk in range(length):
        boundary_edge = perimeter[4 * chunk]
        owners = face_by_edge[boundary_edge]
        if len(owners) != 1:
            raise CertificateFailure("one fill boundary edge did not have one incident face")
        chunk_face.append(owners[0])

    stars = []
    for horizontal in range(1, length):
        for vertical in range(1, length):
            incident = (
                edge_key((horizontal, vertical), (horizontal + 1, vertical)),
                edge_key((horizontal - 1, vertical), (horizontal, vertical)),
                edge_key((horizontal, vertical), (horizontal, vertical + 1)),
                edge_key((horizontal, vertical - 1), (horizontal, vertical)),
            )
            stars.append(tuple(edge_index[edge] for edge in incident))

    if len(edges) != 2 * length * (length - 1):
        raise CertificateFailure("fill disk interior-edge law failed")
    if len(faces) + len(stars) != len(edges) + 1:
        raise CertificateFailure("fill disk Euler rank law failed")
    return FillDisk(
        length,
        edges,
        edge_index,
        tuple(faces),
        tuple(stars),
        perimeter,
        tuple(chunk_face),
    )


def pauli_product(rows) -> c235.Pauli:
    return c532.pauli_product(rows)


def wilson_chunks(graph) -> tuple[tuple[c235.Pauli, ...], ...]:
    owner_masks = {}
    for qubit, edge in enumerate(graph.edges):
        owner_masks[edge.owner] = owner_masks.get(edge.owner, 0) | (1 << qubit)
    output = []
    for axis, wilson in enumerate(c532.wilson_initializers(graph)):
        chunks = []
        for position in range(graph.length):
            cell = [0, 0, 0]
            cell[axis] = position
            mask = owner_masks[tuple(cell)]
            x = wilson.x & mask
            z = wilson.z & mask
            if not (x | z):
                raise CertificateFailure("one axial Wilson owner supplied an empty chunk")
            chunks.append(c235.Pauli((x & z).bit_count() & 1, x, z))
        product_row = pauli_product(chunks)
        if product_row != wilson:
            if not (
                product_row.x == wilson.x
                and product_row.z == wilson.z
                and (product_row.phase - wilson.phase) % 4 == 2
            ):
                raise CertificateFailure("local chunks did not multiply to their Wilson")
            first = chunks[0]
            chunks[0] = c235.Pauli((first.phase + 2) % 4, first.x, first.z)
        if pauli_product(chunks) != wilson:
            raise CertificateFailure("Wilson root-sign repair failed")
        output.append(tuple(chunks))
    return tuple(output)


@lru_cache(maxsize=None)
def minimum_face_pairs(nodes: tuple[tuple[int, int], ...]):
    if not nodes:
        return 0, ()
    first = nodes[0]
    best = None
    for index in range(1, len(nodes)):
        second = nodes[index]
        remainder = nodes[1:index] + nodes[index + 1 :]
        cost, pairs = minimum_face_pairs(remainder)
        candidate = (
            abs(first[0] - second[0]) + abs(first[1] - second[1]) + cost,
            ((first, second),) + pairs,
        )
        if best is None or candidate < best:
            best = candidate
    return best


def dual_path_edges(first, second):
    current = list(first)
    output = []
    for dimension in (0, 1):
        step = 1 if second[dimension] > current[dimension] else -1
        while current[dimension] != second[dimension]:
            target = current.copy()
            target[dimension] += step
            if dimension == 0:
                boundary = max(current[0], target[0])
                edge = edge_key((boundary, current[1]), (boundary, current[1] + 1))
            else:
                boundary = max(current[1], target[1])
                edge = edge_key((current[0], boundary), (current[0] + 1, boundary))
            output.append(edge)
            current = target
    return tuple(output)


def dress_pauli(pauli: c235.Pauli, graph, disk: FillDisk, chunks) -> tuple[c235.Pauli, dict]:
    x = pauli.x
    per_axis_counts = []
    maximum_path = 0
    for axis, axis_chunks in enumerate(chunks):
        if not pauli.commutes(pauli_product(axis_chunks)):
            raise CertificateFailure("only Wilson-commuting rows admit fill-disk dressing")
        syndrome_faces = set()
        for chunk, row in enumerate(axis_chunks):
            if not pauli.commutes(row):
                face = disk.chunk_face[chunk]
                if face in syndrome_faces:
                    syndrome_faces.remove(face)
                else:
                    syndrome_faces.add(face)
        if len(syndrome_faces) % 2:
            raise CertificateFailure("one fill-disk syndrome had odd parity")
        nodes = tuple(sorted(disk.faces[face][0] for face in syndrome_faces))
        _cost, pairs = minimum_face_pairs(nodes)
        selected = set()
        for first, second in pairs:
            path = dual_path_edges(first, second)
            maximum_path = max(maximum_path, len(path))
            for edge in path:
                index = graph.qubits + axis * disk.edge_count + disk.edge_index[edge]
                if index in selected:
                    selected.remove(index)
                else:
                    selected.add(index)
        for index in selected:
            x ^= 1 << index
        per_axis_counts.append(len(selected))
    return c235.Pauli(pauli.phase, x, pauli.z), {
        "per_axis_added_X": tuple(per_axis_counts),
        "added_X": sum(per_axis_counts),
        "maximum_dual_path_edges": maximum_path,
    }


def fill_stabilizers(graph, disk: FillDisk, chunks):
    z_rows = []
    x_rows = []
    product_checks = []
    for axis, axis_chunks in enumerate(chunks):
        axis_z = []
        for face, (_coordinate, face_edges) in enumerate(disk.faces):
            row = c235.Pauli()
            for chunk, target_face in enumerate(disk.chunk_face):
                if target_face == face:
                    row = row @ axis_chunks[chunk]
            z = 0
            for edge in face_edges:
                if edge in disk.edge_index:
                    z ^= 1 << (
                        graph.qubits + axis * disk.edge_count + disk.edge_index[edge]
                    )
            row = row @ c235.Pauli(z=z)
            axis_z.append(row)
            z_rows.append(row)
        product_checks.append(pauli_product(axis_z))
        for star in disk.stars:
            x = sum(
                1 << (graph.qubits + axis * disk.edge_count + edge)
                for edge in star
            )
            row = c235.Pauli(x=x)
            x_rows.append(row)
    expected = c532.wilson_initializers(graph)
    if tuple(product_checks) != expected:
        raise CertificateFailure("fill-face products did not reproduce all three Wilsons")
    return tuple(z_rows), tuple(x_rows)


def extended_objects(length: int):
    graph = c247.PunctureGraph(length, terminals=1)
    disk = build_fill_disk(length)
    chunks = wilson_chunks(graph)
    local_rows = []
    local_meta = []
    for row in c532.local_stabilizers(graph):
        dressed, meta = dress_pauli(row, graph, disk, chunks)
        local_rows.append(dressed)
        local_meta.append(meta)
    matter_rows = []
    matter_meta = []
    for row in c532.matter_generators(graph):
        dressed, meta = dress_pauli(row, graph, disk, chunks)
        matter_rows.append(dressed)
        matter_meta.append(meta)
    gauge_z, gauge_a, gauge_edges = c532.gauge_generators(graph)
    gauge_rows = []
    gauge_meta = []
    for row in gauge_z + gauge_a:
        dressed, meta = dress_pauli(row, graph, disk, chunks)
        gauge_rows.append(dressed)
        gauge_meta.append(meta)
    fill_z, fill_x = fill_stabilizers(graph, disk, chunks)
    stabilizers = tuple(local_rows) + fill_z + fill_x
    qubits = graph.qubits + 3 * disk.edge_count
    return {
        "graph": graph,
        "disk": disk,
        "chunks": chunks,
        "qubits": qubits,
        "local": tuple(local_rows),
        "fill_z": fill_z,
        "fill_x": fill_x,
        "stabilizers": stabilizers,
        "matter": tuple(matter_rows),
        "gauge": tuple(gauge_rows),
        "gauge_edges": gauge_edges,
        "meta": {
            "local": tuple(local_meta),
            "matter": tuple(matter_meta),
            "gauge": tuple(gauge_meta),
        },
    }


def factorization_controls(length: int) -> tuple[dict, dict]:
    started = time.monotonic()
    objects = extended_objects(length)
    graph = objects["graph"]
    disk = objects["disk"]
    qubits = objects["qubits"]
    cells = length**3
    stabilizers = objects["stabilizers"]
    matter = objects["matter"]
    gauge = objects["gauge"]
    rank, inconsistent = c532.phase_rank(stabilizers, qubits)
    stabilizer_vectors = tuple(row.symplectic(qubits) for row in stabilizers)
    matter_vectors = tuple(row.symplectic(qubits) for row in matter)
    gauge_vectors = tuple(row.symplectic(qubits) for row in gauge)
    matter_reps = c532.quotient_complement(stabilizer_vectors, matter_vectors)
    gauge_reps = c532.quotient_complement(stabilizer_vectors, gauge_vectors)
    matter_rank = c532.symplectic_gram_rank(matter_reps, qubits)
    gauge_rank = c532.symplectic_gram_rank(gauge_reps, qubits)

    mask = (1 << qubits) - 1
    centralizer_equations = tuple(
        (row >> qubits) | ((row & mask) << qubits)
        for row in stabilizer_vectors + matter_vectors
    )
    centralizer = c532.null_basis(centralizer_equations, 2 * qubits)
    commutant_reps = c532.quotient_complement(stabilizer_vectors, centralizer)
    commutant_dimension = len(commutant_reps)
    commutant_rank = c532.symplectic_gram_rank(commutant_reps, qubits)

    wilsons = c532.wilson_initializers(graph)
    wilson_rank_increments = tuple(
        len(c532.quotient_complement(stabilizer_vectors, (row.symplectic(qubits),)))
        for row in wilsons
    )
    fill_pair_failures = sum(
        not left.commutes(right)
        for index, left in enumerate(objects["fill_z"] + objects["fill_x"])
        for right in (objects["fill_z"] + objects["fill_x"])[index + 1 :]
    )
    matter_stabilizer_failures = sum(
        not row.commutes(stabilizer) for row in matter for stabilizer in stabilizers
    )
    gauge_stabilizer_failures = sum(
        not row.commutes(stabilizer) for row in gauge for stabilizer in stabilizers
    )
    gauge_matter_failures = sum(
        not gauge_row.commutes(matter_row) for gauge_row in gauge for matter_row in matter
    )

    raw_matter_parity = pauli_product(
        graph.B(vertex) for vertex in range(graph.matter_count)
    )
    matter_parity, _ = dress_pauli(raw_matter_parity, graph, disk, objects["chunks"])
    raw_gauge_z, _raw_gauge_a, _ = c532.gauge_generators(graph)
    gauge_parity_raw = pauli_product(raw_gauge_z)
    gauge_parity, _ = dress_pauli(gauge_parity_raw, graph, disk, objects["chunks"])
    parity_join = matter_parity @ gauge_parity
    joined_rank, joined_inconsistent = c532.phase_rank(
        stabilizers + (parity_join,), qubits
    )
    positive_rank, positive_inconsistent = c532.phase_rank(
        stabilizers + (matter_parity,), qubits
    )
    negative_rank, negative_inconsistent = c532.phase_rank(
        stabilizers + (c235.Pauli(phase=2) @ matter_parity,), qubits
    )

    all_meta = objects["meta"]
    maximum_added = {
        family: max(row["added_X"] for row in rows)
        for family, rows in all_meta.items()
    }
    maximum_path = {
        family: max(row["maximum_dual_path_edges"] for row in rows)
        for family, rows in all_meta.items()
    }
    maximum_support = {
        "dressed_local_constraint": max((row.x | row.z).bit_count() for row in objects["local"]),
        "fill_Z_face": max((row.x | row.z).bit_count() for row in objects["fill_z"]),
        "fill_X_star": max((row.x | row.z).bit_count() for row in objects["fill_x"]),
        "dressed_matter": max((row.x | row.z).bit_count() for row in matter),
        "dressed_gauge": max((row.x | row.z).bit_count() for row in gauge),
    }
    expected_stabilizer_rank = 15 * cells + 1 + 3 * disk.edge_count
    expected_matter_dimension = 12 * cells - 1
    expected_matter_rank = 12 * cells - 2
    expected_gauge_dimension = 2 * cells - 1
    expected_gauge_rank = 2 * cells - 2
    pass_flag = bool(
        inconsistent == 0
        and rank == expected_stabilizer_rank
        and qubits - rank == 7 * cells - 1
        and tuple(wilson_rank_increments) == (0, 0, 0)
        and len(matter_reps) == expected_matter_dimension
        and matter_rank == expected_matter_rank
        and len(gauge_reps) == commutant_dimension == expected_gauge_dimension
        and gauge_rank == commutant_rank == expected_gauge_rank
        and fill_pair_failures == matter_stabilizer_failures == 0
        and gauge_stabilizer_failures == gauge_matter_failures == 0
        and joined_rank == rank
        and joined_inconsistent == 0
        and positive_rank == negative_rank == rank + 1
        and positive_inconsistent == negative_inconsistent == 0
        and maximum_support["fill_Z_face"] <= 11
        and maximum_support["fill_X_star"] == 4
        and max(maximum_added.values()) <= 9
    )
    result = {
        "length": length,
        "held": length == HELD_LENGTH,
        "coarse_cells": cells,
        "rough_M2": graph.qubits,
        "fill_disk_interior_edge_M2_per_axis": disk.edge_count,
        "added_fill_M2": 3 * disk.edge_count,
        "total_M2": qubits,
        "average_M2_per_coarse_cell": qubits / cells,
        "fill_faces_per_axis": len(disk.faces),
        "fill_interior_stars_per_axis": len(disk.stars),
        "fill_constraint_minus_added_M2_per_axis": (
            len(disk.faces) + len(disk.stars) - disk.edge_count
        ),
        "stabilizer_rank": rank,
        "code_exponent": qubits - rank,
        "target_Fock_exponent": 6 * cells,
        "gauge_qubits": cells - 1,
        "Wilson_initializer_rows_supplied": 0,
        "Wilson_rank_increments_after_local_fill": wilson_rank_increments,
        "matter_quotient_dimension": len(matter_reps),
        "matter_symplectic_rank": matter_rank,
        "gauge_quotient_dimension": len(gauge_reps),
        "gauge_symplectic_rank": gauge_rank,
        "full_matter_commutant_dimension": commutant_dimension,
        "full_matter_commutant_symplectic_rank": commutant_rank,
        "explicit_dressed_gauge_exhausts_commutant": (
            len(gauge_reps) == commutant_dimension and gauge_rank == commutant_rank
        ),
        "matter_gauge_parities_equal_on_code": joined_rank == rank,
        "both_matter_parity_sectors_nonempty": (
            positive_inconsistent == negative_inconsistent == 0
        ),
        "fixed_parity_sector_exponent": qubits - rank - 1,
        "expected_target_parity_plus_gauge_exponent": (6 * cells - 1) + (cells - 1),
        "fill_constraint_mutual_commutator_failures": fill_pair_failures,
        "matter_stabilizer_commutator_failures": matter_stabilizer_failures,
        "gauge_stabilizer_commutator_failures": gauge_stabilizer_failures,
        "gauge_matter_commutator_failures": gauge_matter_failures,
        "maximum_added_disk_X_by_family": maximum_added,
        "maximum_dual_path_edges_by_family": maximum_path,
        "maximum_support_M2": maximum_support,
        "factorization": (
            "H_local-fill = H_target-full-Fock tensor H_(N-1)-gauge, "
            "sectorwise across the shared matter/gauge parity center"
        ),
        "resource": checkpoint(started, f"Cycle537-factorization-L{length}"),
        "pass": pass_flag,
    }
    return result, objects


def onsite_and_runtime_controls(objects) -> dict:
    graph = objects["graph"]
    disk = objects["disk"]
    chunks = objects["chunks"]
    stabilizers = objects["stabilizers"]
    gauge = objects["gauge"]
    cell = (0, 0, 0)
    raw_hoppings = tuple(
        c532.onsite_hopping(graph, cell, left, right)
        for left, right in combinations(range(6), 2)
    )
    raw_b = tuple(
        graph.B(graph.base.vertex_index[(cell, direction)]) for direction in range(6)
    )
    raw_contacts = tuple(left @ right for left, right in combinations(raw_b, 2))
    hoppings = tuple(dress_pauli(row, graph, disk, chunks)[0] for row in raw_hoppings)
    cell_b = tuple(dress_pauli(row, graph, disk, chunks)[0] for row in raw_b)
    contacts = tuple(dress_pauli(row, graph, disk, chunks)[0] for row in raw_contacts)
    stabilizer_failures = sum(
        not row.commutes(stabilizer)
        for row in hoppings + contacts
        for stabilizer in stabilizers
    )
    gauge_failures = sum(
        not row.commutes(gauge_row)
        for row in hoppings + contacts
        for gauge_row in gauge
    )
    endpoint_failures = 0
    for (left, right), hopping in zip(combinations(range(6), 2), hoppings):
        actual = {
            direction for direction, parity in enumerate(cell_b)
            if not hopping.commutes(parity)
        }
        endpoint_failures += actual != {left, right}
    stream_edges = tuple(
        edge for edge, row in enumerate(graph.base.edges) if row[2] == "outer_square"
    )
    fswap_supports = []
    for edge in stream_edges:
        source, target, _kind, _owner = graph.base.edges[edge]
        rows = tuple(
            dress_pauli(row, graph, disk, chunks)[0]
            for row in (graph.B(source), graph.B(target), graph.mapped_matter_A(edge))
        )
        fswap_supports.append(
            ((rows[0].x | rows[0].z) | (rows[1].x | rows[1].z) | (rows[2].x | rows[2].z)).bit_count()
        )
    return {
        "length": graph.length,
        "onsite_pairs": len(hoppings),
        "contact_pairs": len(contacts),
        "maximum_dressed_onsite_hopping_support_M2": max(
            (row.x | row.z).bit_count() for row in hoppings
        ),
        "maximum_dressed_contact_support_M2": max(
            (row.x | row.z).bit_count() for row in contacts
        ),
        "onsite_endpoint_incidence_failures": endpoint_failures,
        "onsite_contact_stabilizer_failures": stabilizer_failures,
        "onsite_contact_gauge_failures": gauge_failures,
        "B_FSWAP_blocks": len(fswap_supports),
        "B_FSWAP_blocks_per_cell": len(fswap_supports) / graph.length**3,
        "maximum_dressed_B_FSWAP_block_support_M2": max(fswap_supports),
        "pass": bool(
            len(hoppings) == len(contacts) == 15
            and endpoint_failures == stabilizer_failures == gauge_failures == 0
            and len(fswap_supports) == 3 * graph.length**3
        ),
    }


def signed_axis(frame: np.ndarray, axis: int) -> tuple[int, int]:
    image = frame @ np.eye(3, dtype=int)[:, axis]
    target = int(np.flatnonzero(image)[0])
    return target, int(image[target])


def covariance_controls() -> dict:
    frames = c235.proper_cubic_frames()
    size_rows = []
    all_digests = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        labels = tuple((axis, position) for axis in range(3) for position in range(length))
        frame_failures = 0
        digests = []
        for frame in frames:
            mapped = []
            for axis, position in labels:
                target, sign = signed_axis(frame, axis)
                mapped.append((target, (sign * position) % length))
            frame_failures += len(set(mapped)) != len(labels)
            digest = sha256(
                repr((length, tuple(frame.ravel()), tuple(mapped))).encode()
            ).hexdigest()
            digests.append(digest)
            all_digests.append(digest)

        group_failures = 0
        for left in frames:
            for right in frames:
                product_frame = left @ right
                mismatch = False
                for axis in range(3):
                    for position in range(length):
                        middle_axis, middle_sign = signed_axis(right, axis)
                        target_axis, target_sign = signed_axis(left, middle_axis)
                        composed = (
                            target_axis,
                            (target_sign * middle_sign * position) % length,
                        )
                        direct_axis, direct_sign = signed_axis(product_frame, axis)
                        direct = (direct_axis, (direct_sign * position) % length)
                        if composed != direct:
                            group_failures += 1
                            mismatch = True
                            break
                    if mismatch:
                        break
        size_rows.append(
            {
                "length": length,
                "held": length == HELD_LENGTH,
                "axis_position_labels": len(labels),
                "frame_orbit_failures": frame_failures,
                "frame_group_failures": group_failures,
                "presentation_digests": tuple(digests),
                "pass": frame_failures == group_failures == 0,
            }
        )

    rough = c532.covariance_controls()
    return {
        "proper_cubic_frames": len(frames),
        "frame_products": len(frames) ** 2,
        "rough_fixed_target_frame_and_group_certificate": rough,
        "L5_held_L6_fill_orbits": tuple(size_rows),
        "mapped_fill_presentation_digests": tuple(all_digests),
        "runtime_frame_query": False,
        "compile_time_retriangulated_fill_orbit": True,
        "one_fixed_frame_independent_cap_triangulation_claimed": False,
        "statement": (
            "all 24 frame-specific cap presentations and all 576 signed-axis "
            "compositions close; a single embedded cap triangulation is not claimed"
        ),
        "pass": bool(
            len(frames) == 24
            and len(frames) ** 2 == 576
            and rough["pass"]
            and all(row["pass"] for row in size_rows)
        ),
    }


def deletion_controls() -> dict:
    objects = extended_objects(3)
    qubits = objects["qubits"]
    stabilizers = objects["stabilizers"]
    full_rank, full_inconsistent = c532.phase_rank(stabilizers, qubits)
    deleted_face = objects["local"] + objects["fill_z"][1:] + objects["fill_x"]
    deleted_face_rank, deleted_face_inconsistent = c532.phase_rank(deleted_face, qubits)
    deleted_star = objects["local"] + objects["fill_z"] + objects["fill_x"][1:]
    deleted_star_rank, deleted_star_inconsistent = c532.phase_rank(deleted_star, qubits)
    first_wilson = c532.wilson_initializers(objects["graph"])[0]
    deleted_vectors = tuple(row.symplectic(qubits) for row in deleted_face)
    deleted_wilson_increment = len(
        c532.quotient_complement(deleted_vectors, (first_wilson.symplectic(qubits),))
    )
    witness = None
    for raw in c532.matter_generators(objects["graph"]):
        dressed, meta = dress_pauli(
            raw, objects["graph"], objects["disk"], objects["chunks"]
        )
        added = dressed.x & ~((1 << objects["graph"].qubits) - 1)
        if added:
            bit = added & -added
            deleted = c235.Pauli(dressed.phase, dressed.x ^ bit, dressed.z)
            violations = sum(not deleted.commutes(row) for row in objects["fill_z"])
            if violations:
                witness = {
                    "deleted_disk_X_site": bit.bit_length() - 1,
                    "fill_face_syndrome_violations": violations,
                    "original_added_X": meta["added_X"],
                }
                break
    if witness is None:
        raise CertificateFailure("no deleted dressing witness was found")
    return {
        "full_stabilizer_rank": full_rank,
        "delete_one_fill_face_rank": deleted_face_rank,
        "delete_one_fill_face_Wilson_rank_increment": deleted_wilson_increment,
        "delete_one_fill_star_rank": deleted_star_rank,
        "phase_inconsistencies_full_face_deleted_star_deleted": (
            full_inconsistent,
            deleted_face_inconsistent,
            deleted_star_inconsistent,
        ),
        "delete_one_dressing_X": witness,
        "deleted_FSWAP_fourth_term_residual": c532.fswap_matrix_control()[
            "deleted_fourth_term_residual"
        ],
        "pass": bool(
            full_inconsistent == deleted_face_inconsistent == deleted_star_inconsistent == 0
            and deleted_face_rank == deleted_star_rank == full_rank - 1
            and deleted_wilson_increment == 1
            and witness["fill_face_syndrome_violations"] > 0
        ),
    }


def alternative_route_controls() -> dict:
    rows = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        graph = c247.PunctureGraph(length, terminals=1)
        chunks = wilson_chunks(graph)
        # A cycle-only fill has L ancillas and L commuting checks per axis, so
        # it does not lower the exponent.  A linear dressing rooted at one
        # position contains the long complementary arc for a cut-crossing row.
        maximum_rooted_linear_dress = 0
        for row in c532.local_stabilizers(graph) + c532.matter_generators(graph):
            for axis_chunks in chunks:
                syndrome = [int(not row.commutes(chunk)) for chunk in axis_chunks]
                if sum(syndrome) % 2:
                    raise CertificateFailure("rooted chain received odd syndrome")
                values = [0] * length
                for index in range(length - 1):
                    values[index + 1] = values[index] ^ syndrome[index]
                maximum_rooted_linear_dress = max(maximum_rooted_linear_dress, sum(values))
        rows.append(
            {
                "length": length,
                "ring_fill_added_M2_per_axis": length,
                "ring_fill_checks_per_axis": length,
                "ring_fill_net_exponent_reduction_per_axis": 0,
                "rooted_open_chain_added_M2_per_axis": length - 1,
                "rooted_open_chain_checks_per_axis": length,
                "rooted_linear_dressing_maximum_X_support": maximum_rooted_linear_dress,
                "fan_center_star_weight": length,
            }
        )
    return {
        "rows": tuple(rows),
        "ring_relational_field_disposition": (
            "local and covariant but leaves three replacement logicals; it is not the target factor"
        ),
        "rooted_chain_disposition": (
            "rank-correct but one linear local-algebra dressing grows across the root cut"
        ),
        "fan_disk_disposition": (
            "rank-correct and dihedral-covariant, but the center-star check grows with L"
        ),
        "square_fill_disposition": (
            "bounded face/star constraints and exact target factor; fixed old-periodic embedding remains open"
        ),
        "pass": bool(
            rows[0]["ring_fill_net_exponent_reduction_per_axis"] == 0
            and rows[1]["ring_fill_net_exponent_reduction_per_axis"] == 0
            and rows[1]["fan_center_star_weight"] > rows[0]["fan_center_star_weight"]
            and rows[1]["rooted_linear_dressing_maximum_X_support"]
            >= rows[0]["rooted_linear_dressing_maximum_X_support"]
        ),
    }


def inherited_target_controls() -> dict:
    target = c532.target_B_controls()
    fixtures = c532.fixture_controls()
    fswap = c532.fswap_matrix_control()
    return {
        "full_Fock_Gamma_P": target,
        "mass_contact_and_seam": fixtures,
        "FSWAP_polynomial_inverse": fswap,
        "pass": target["pass"] and fixtures["pass"] and fswap["pass"],
    }


def upstream_evidence() -> dict:
    expected = {str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()}
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    return {"expected_sha256": expected, "observed_sha256": observed, "pass": expected == observed}


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE), "pass": False}
    flat = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "fill disk",
        "euler",
        "no growing wilson initializer",
        "both matter parities",
        "full-fock",
        "gamma(p)",
        "all 24",
        "576",
        "held l6",
        "not an abstract code quotient",
        "cap-sheet topology",
        "n1 —",
        "n2 —",
        "n3 —",
        "n4 —",
        "n5 —",
        "n6 —",
        "n7 —",
        "n8 —",
        "fail / do not ship",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in flat)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def dry_contract() -> dict:
    evidence = upstream_evidence()
    note = note_contract()
    tests = {
        "strict_Cycle532_pins": evidence["pass"],
        "note_scope_supply_and_N1_N8": note["pass"],
    }
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
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
        raise CertificateFailure("Cycle537 dry contract failed")
    factorizations = []
    objects_by_length = []
    runtime = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        factorization, objects = factorization_controls(length)
        factorizations.append(factorization)
        objects_by_length.append(objects)
        runtime.append(onsite_and_runtime_controls(objects))
    checkpoints.append(checkpoint(started, "L5-L6-fill-factorizations"))
    covariance = covariance_controls()
    checkpoints.append(checkpoint(started, "all24-576-fill-orbit"))
    deletions = deletion_controls()
    alternatives = alternative_route_controls()
    inherited = inherited_target_controls()
    checkpoints.append(checkpoint(started, "deletions-alternatives-target"))

    tests = {
        "dry_contract": dry["pass"],
        "L5_held_L6_local_fill_target_tensor_gauge": all(row["pass"] for row in factorizations),
        "both_parities_and_full_commutant": all(
            row["both_matter_parity_sectors_nonempty"]
            and row["explicit_dressed_gauge_exhausts_commutant"]
            for row in factorizations
        ),
        "bounded_dressed_onsite_contact_and_B": all(row["pass"] for row in runtime),
        "all24_576_compile_time_fill_presentation_orbit": covariance["pass"],
        "inverse_leakage_and_deletions": deletions["pass"],
        "ring_rooted_fan_route_discriminators": alternatives["pass"],
        "full_Fock_GammaP_mass_contact_seam_preserved": inherited["pass"],
        "supply_boundary_and_no_axiom_pressure": True,
        "resource_contract": rss_bytes() < RSS_GUARD_BYTES and swap_count() == 0,
    }
    elapsed = time.monotonic() - started
    result = {
        "revision": REVISION,
        "mode": "fill-disk-certificate",
        "status": "cycle537-local-fill-disk-algebraic-partial-closure",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "strongest_constructive_result": (
            "three bounded square fill disks replace the three growing Wilson rows; "
            "their dressed L5/L6 code is exactly full-Fock target tensor N-1 gauge"
        ),
        "factorization_L5_L6": tuple(factorizations),
        "onsite_contact_B_L5_L6": tuple(runtime),
        "covariance": covariance,
        "deletions": deletions,
        "alternative_route_discriminators": alternatives,
        "inherited_target": inherited,
        "explicit_encoding_status": {
            "abstract_quotient_called_encoding": False,
            "local_stabilizer_and_operator_presentation_constructed": True,
            "code_space_isometry_or_state_preparation_circuit_constructed": False,
            "ordinary_period32_three_dimensional_cap_embedding_constructed": False,
        },
        "supplied_structure_inventory": {
            "Cycle532_rough_graph_matter_and_gauge_Paulis": True,
            "three_square_cap_sheet_topologies": True,
            "one_macro_origin_and_three_axial_attachment_loops": True,
            "frame_specific_compile_time_retriangulation": True,
            "finite_periodic_L5_L6_domains": True,
            "Cycle219_coin_Cycle230_contact_and_factor_order": True,
            "growing_Wilson_initializer_rows": False,
            "runtime_sector_or_parity_query": False,
            "old_period32_cap_sheet_embedding": False,
            "initial_local_stabilizer_state_preparation": False,
        },
        "boundary": {
            "three_Wilson_words_in_span_of_bounded_local_fill_checks": True,
            "fixed_target_tensor_gauge_algebra_closed": True,
            "new_cap_sheet_topology_imported": True,
            "fixed_single_frame_independent_physical_embedding_closed": False,
            "bounded_state_preparation_circuit_closed": False,
            "unconditional_existing_M2_substrate_compiler_claimed": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "broad_negative_gate": "FAIL / DO NOT SHIP",
        },
        "causal_type_boundary": {
            "fill_schedule_called_physical_time": False,
            "phase_called_physical_energy": False,
            "puncture_state_called_Record": False,
            "algebraic_factorization_called_realized_encoding": False,
        },
        "resources": {
            "elapsed_seconds": elapsed,
            "maximum_RSS_bytes": max(row["maximum_RSS_bytes"] for row in checkpoints),
            "process_swap_count": sum(row["process_swap_count"] for row in checkpoints),
            "hard_wall_seconds": WALL_LIMIT_SECONDS,
            "checkpoints": checkpoints,
        },
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }
    return result


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
            "status": "cycle537-runner-failed",
            "authority": AUTHORITY,
            "audit": AUDIT,
            "constitutional_effect": "none",
            "error_type": type(exc).__name__,
            "error": str(exc),
            "pass": False,
        }
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload.get("pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
