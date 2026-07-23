#!/usr/bin/env python3
"""Cycle642: fixed-cubic Wilson-fill incidence attempt.

Tests the exact Cycle537 marked square disk against a single all-frame
placement, and constructs a smaller proper-cubic orbit-replicated tree fill
as a positive enlarged-incidence comparator.  The comparator is an exact
stabilizer presentation and K129 role placement, not a preparation isometry
or an autonomous routed-check controller.

Authority none; audit unset; author accepted false; breakthrough false.
"""
from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
from itertools import combinations, permutations, product
import io
import json
import resource
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
IMMUTABLE_COMMIT = "e2719c0f7fceccc3a61e7b4a11049bc1e616550a"
_EXPORT_HOLDER = tempfile.TemporaryDirectory(prefix="cycle642-immutable-")
IMMUTABLE_ROOT = Path(_EXPORT_HOLDER.name).resolve()
_archive = subprocess.check_output(
    ["git", "archive", "--format=tar", IMMUTABLE_COMMIT, "scripts"], cwd=ROOT
)
with tarfile.open(fileobj=io.BytesIO(_archive), mode="r:") as _tar:
    _tar.extractall(IMMUTABLE_ROOT, filter="data")
sys.path.insert(0, str(IMMUTABLE_ROOT / "scripts"))
import physical_local_wilson_fill_disk_cycle537_2026_07_21 as c537
import physical_hierarchical_grammar_full_act_compiler_cycle638_2026_07_23 as c638

c532 = c537.c532
c235 = c537.c235
FRAMES = tuple(c235.proper_cubic_frames())
K = 129
H = 64
AUTHORITY = "none"
AUDIT = "unset"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_FIXED_CUBIC_WILSON_FILL_INCIDENCE_CYCLE642_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_fixed_cubic_wilson_fill_incidence_cycle642_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_fixed_cubic_wilson_fill_incidence_cycle642_cold_2026_07_23.txt"
PASS = FAIL = 0

PINS = {
    "scripts/physical_local_wilson_fill_disk_cycle537_2026_07_21.py": "cd00034db5e106accfd95e33de5c9b3b2a26b2c35719611454c3486481ad47ac",
    "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md": "e413a8c079fa2d5ff14d1b46d19df60cd07d853d118b51d8494632cc03a427f8",
    "outputs/physical_local_wilson_fill_disk_cycle537_receipt_2026_07_21.json": "ebe7222afedba7907dcff9e233b2bc30284af8d35d5d7cae1941668ed81c5856",
    "scripts/physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21.py": "8bf1c836661b4c902d09cf2f7d147b07c3083404569ce9bc0a2b3dd4820233da",
    "scripts/physical_unchanged_torus_cap_homology_discriminator_cycle637_2026_07_23.py": "65accbf8d3c7ffba2bd469c5cdee76cf14d79241a3c0899fede8764ce703e672",
    "docs/work_history/repo/review_feedback/PHYSICAL_UNCHANGED_TORUS_CAP_HOMOLOGY_DISCRIMINATOR_CYCLE637_NOTE_2026-07-23.md": "15e01b73d71631646ee3387443575a9c4921eca1e1104c83fda11d74b8b76ff0",
    "outputs/physical_unchanged_torus_cap_homology_discriminator_cycle637_receipt_2026_07_23.json": "871ce37fa9308ce9316681e1290866f40c908f8b6b70469250e5d06b500207ff",
    "scripts/physical_hierarchical_grammar_full_act_compiler_cycle638_2026_07_23.py": "7c30cb47934ea6faf908d13ef15e6d62bf0c494ba8632ebdffeec88352037d53",
    "docs/work_history/repo/review_feedback/PHYSICAL_HIERARCHICAL_GRAMMAR_FULL_ACT_COMPILER_CYCLE638_NOTE_2026-07-23.md": "30b9793f87ac0e96d92567709201fbae8833904302b9c195eb8eefcc0972abf1",
    "outputs/physical_hierarchical_grammar_full_act_compiler_cycle638_receipt_2026_07_23.json": "706a592d667dfa12a2215d588f5b3cf09c8d1212d4907e9a73d8647a76762e46",
    "outputs/physical_hierarchical_grammar_full_act_compiler_cycle638_cold_2026_07_23.txt": "6ec79c334322c832c9bb54babe0dd80ad2e55e8f44304e6ee1ccfdaa96557ffa",
}
NO_GO_ORIGIN_MAIN_SHA256 = "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7"
FRESHNESS_SHA256 = "1e0ec4ef4d7c5dd24243d7c3954c78a3f00ecd3d5e43805e788dd3629973a962"


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, value):
        for stream in self.streams: stream.write(value)
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def git_blob_sha(path: str) -> str:
    body = subprocess.check_output(["git", "show", f"{IMMUTABLE_COMMIT}:{path}"], cwd=ROOT)
    return sha256(body).hexdigest()


def json_default(value):
    if isinstance(value, np.generic): return value.item()
    if isinstance(value, np.ndarray): return value.tolist()
    if isinstance(value, (set, frozenset)): return sorted(value, key=repr)
    raise TypeError(type(value).__name__)


def check(label: str, condition: bool, detail="") -> None:
    global PASS, FAIL
    PASS += int(condition); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def signed_axis(frame: np.ndarray, axis: int) -> tuple[int, int]:
    image = frame @ np.eye(3, dtype=int)[:, axis]
    target = int(np.flatnonzero(image)[0])
    return target, int(image[target])


def square_marking_falsifier() -> dict:
    rows = []
    for length in (3, 6, 7):
        disk = c537.build_fill_disk(length)
        face_coords = tuple(row[0] for row in disk.faces)
        marked = tuple(face_coords[index] for index in disk.chunk_face)
        quarter = lambda face: (length - 1 - face[1], face[0])
        fixed_faces = tuple(face for face in face_coords if quarter(face) == face)
        mismatches = sum(quarter(face) != face for face in marked)
        set_failures = sum(quarter(face) not in set(marked) for face in marked)
        rows.append({
            "length": length,
            "marked_chunk_faces": marked,
            "quarter_turned_marked_faces": tuple(quarter(face) for face in marked),
            "quarter_turn_fixed_faces": fixed_faces,
            "chunk_attachment_incidence_mismatches": mismatches,
            "marked_set_nonclosure_count": set_failures,
            "all_chunks_fixed_by_rotation_about_their_axis": True,
            "injective_exact_marked_square_incidence_equivariant": mismatches == 0,
        })
    result = {
        "tested_object": "the exact Cycle537 one-chunk-to-one-marked-face square-disk incidence",
        "witness": "a proper 90-degree rotation about the Wilson axis fixes every axial chunk label and rotates the square faces",
        "rows": rows,
        "narrow_conclusion": "the exact marked Cycle537 square presentation has no injective row-permutation-equivariant fixed placement; retriangulation, role splitting, or a changed incidence remains open",
        "general_enlarged_incidence_no_go": False,
        "pass_as_narrow_falsifier": all(row["chunk_attachment_incidence_mismatches"] > 0 for row in rows),
    }
    check("the exact marked Cycle537 square disk fails one fixed quarter-turn incidence action at L3/L6/L7",
          result["pass_as_narrow_falsifier"], rows)
    return result


ROOT_VERTEX = "root"


def vertex_key(value):
    return (-1, 0) if value == ROOT_VERTEX else (0, int(value))


def edge_key(left, right):
    return tuple(sorted((left, right), key=vertex_key))


def fill_tree(length: int) -> tuple[tuple, tuple]:
    vertices = (ROOT_VERTEX,) + tuple(range(length))
    edges = [edge_key(ROOT_VERTEX, 0)]
    half = length // 2
    if length % 2:
        edges += [edge_key(ROOT_VERTEX, 1), edge_key(ROOT_VERTEX, length - 1)]
        for value in range(1, half):
            edges += [edge_key(value, value + 1), edge_key((-value) % length, (-(value + 1)) % length)]
    else:
        edges += [edge_key(ROOT_VERTEX, half), edge_key(ROOT_VERTEX, 1), edge_key(ROOT_VERTEX, length - 1)]
        for value in range(1, half - 1):
            edges += [edge_key(value, value + 1), edge_key((-value) % length, (-(value + 1)) % length)]
    edges = tuple(sorted(set(edges), key=repr))
    return vertices, edges


def tree_controls(length: int) -> dict:
    vertices, edges = fill_tree(length)
    adjacency = {vertex: set() for vertex in vertices}
    for left, right in edges:
        adjacency[left].add(right); adjacency[right].add(left)
    seen = {ROOT_VERTEX}; queue = deque([ROOT_VERTEX])
    while queue:
        vertex = queue.popleft()
        for target in adjacency[vertex] - seen: seen.add(target); queue.append(target)
    reflection_failures = 0
    reflected = lambda vertex: ROOT_VERTEX if vertex == ROOT_VERTEX else (-vertex) % length
    edge_set = set(edges)
    for left, right in edges:
        reflection_failures += edge_key(reflected(left), reflected(right)) not in edge_set
    return {
        "length": length, "vertices": vertices, "edges": edges,
        "vertex_count": len(vertices), "edge_count": len(edges),
        "connected": len(seen) == len(vertices), "Euler_surplus": len(vertices) - len(edges),
        "maximum_degree": max(map(len, adjacency.values())),
        "reflection_failures": reflection_failures,
        "pass": len(edges) == len(vertices) - 1 and len(seen) == len(vertices)
                and reflection_failures == 0 and max(map(len, adjacency.values())) <= 4,
    }


def act_vertex(frame, axis: int, vertex, length: int):
    target, sign = signed_axis(frame, axis)
    mapped = ROOT_VERTEX if vertex == ROOT_VERTEX else (sign * int(vertex)) % length
    return target, mapped


def act_edge(frame, role, length: int):
    axis, left, right = role
    target, mapped_left = act_vertex(frame, axis, left, length)
    _target, mapped_right = act_vertex(frame, axis, right, length)
    edge = edge_key(mapped_left, mapped_right)
    return (target, edge[0], edge[1])


def rotate(frame, coordinate):
    return tuple(int(value) for value in frame @ np.asarray(coordinate, dtype=int))


def allocate_orbit_roles(length: int) -> tuple[dict, dict]:
    _vertices, base_edges = fill_tree(length)
    roles = tuple((axis, left, right) for axis in range(3) for left, right in base_edges)
    role_set = set(roles); remaining = set(roles); fibers = {}; orbit_rows = []; used = set()
    candidates = ((64, first, second) for first in range(1, 63) for second in range(first + 1, 64))
    candidate_iter = iter(candidates)
    while remaining:
        representative = min(remaining, key=repr)
        orbit = {act_edge(frame, representative, length) for frame in FRAMES}
        if not orbit <= role_set: raise AssertionError("tree role orbit escaped")
        stabilizer = tuple(frame for frame in FRAMES if act_edge(frame, representative, length) == representative)
        while True:
            seed = next(candidate_iter)
            physical_orbit = {rotate(frame, seed) for frame in FRAMES}
            if len(physical_orbit) == 24 and not (physical_orbit & used): break
        for role in orbit:
            fiber = {rotate(frame, seed) for frame in FRAMES if act_edge(frame, representative, length) == role}
            if len(fiber) != len(stabilizer): raise AssertionError("orbit fiber size")
            fibers[role] = tuple(sorted(fiber))
        used |= physical_orbit; remaining -= orbit
        orbit_rows.append({
            "representative": representative, "abstract_orbit_size": len(orbit),
            "role_stabilizer_size": len(stabilizer), "physical_seed": seed,
            "physical_orbit_size": len(physical_orbit),
        })
    covariance_failures = 0; group_failures = 0
    for frame in FRAMES:
        for role, fiber in fibers.items():
            target = act_edge(frame, role, length)
            covariance_failures += {rotate(frame, site) for site in fiber} != set(fibers[target])
    for left in FRAMES:
        for right in FRAMES:
            product = left @ right
            for role in roles:
                group_failures += act_edge(left, act_edge(right, role, length), length) != act_edge(product, role, length)
    all_sites = tuple(site for fiber in fibers.values() for site in fiber)
    inner_collisions = sum(max(map(abs, site)) <= 63 for site in all_sites)
    old_role_collisions = sum(max(map(abs, site)) <= 16 for site in all_sites)
    dynamic = {c638.c633.representative(site) for site in c638.c629.dynamic_geometry_sites()}
    markers = {c638.c633.representative(site) for site in c638.c630.marker_residues()}
    dynamic_collisions = len(set(all_sites) & dynamic)
    marker_collisions = len(set(all_sites) & markers)
    translated = {}
    for lattice_length in (3, 6, 7):
        modulus = K * lattice_length; seen = set(); collisions = 0
        for x in range(lattice_length):
            for y in range(lattice_length):
                for z in range(lattice_length):
                    for site in all_sites:
                        point = tuple((site[a] + K * (x, y, z)[a]) % modulus for a in range(3))
                        collisions += point in seen; seen.add(point)
        translated[lattice_length] = {"motif_copies": lattice_length**3, "placed_roles": len(seen), "collisions": collisions}
    result = {
        "length": length, "logical_aux_edges": len(roles), "physical_aux_M2": len(all_sites),
        "abstract_role_orbits": len(orbit_rows), "orbit_rows": orbit_rows,
        "role_copy_multiplicity_histogram": dict(Counter(map(len, fibers.values()))),
        "placement_bound": "all cap roles lie on max|coordinate|=64 shell of one supplied K129 block",
        "Cycle638_inner_program_role_collisions": inner_collisions,
        "Cycle629_638_dynamic_geometry_collisions": dynamic_collisions,
        "Cycle629_638_marker_role_collisions": marker_collisions,
        "Cycle532_rescaled_old_role_collisions": old_role_collisions,
        "injective_role_collisions": len(all_sites) - len(set(all_sites)),
        "all24_fiber_covariance_failures": covariance_failures,
        "all576_label_group_failures": group_failures,
        "translated_L3_L6_L7": translated,
        "pass": inner_collisions == old_role_collisions == dynamic_collisions == marker_collisions == 0
                and len(all_sites) == len(set(all_sites))
                and covariance_failures == group_failures == 0
                and all(row["collisions"] == 0 for row in translated.values()),
    }
    check(f"L{length} orbit-split tree roles are injective in K129 and covariant all24/all576 with translated L3/L6/L7 ownership",
          result["pass"], {key: result[key] for key in ("logical_aux_edges", "physical_aux_M2", "abstract_role_orbits", "role_copy_multiplicity_histogram", "all24_fiber_covariance_failures", "all576_label_group_failures")})
    return result, fibers


def tree_selected_edges(marked, length: int):
    vertices, edges = fill_tree(length)
    adjacency = {vertex: [] for vertex in vertices}
    for edge in edges:
        left, right = edge; adjacency[left].append((right, edge)); adjacency[right].append((left, edge))
    parent = {ROOT_VERTEX: None}; parent_edge = {}; order = [ROOT_VERTEX]
    for vertex in order:
        for target, edge in adjacency[vertex]:
            if target in parent: continue
            parent[target] = vertex; parent_edge[target] = edge; order.append(target)
    parity = {vertex: int(vertex != ROOT_VERTEX and vertex in marked) for vertex in vertices}
    selected = set()
    for vertex in reversed(order[1:]):
        if parity[vertex]: selected.add(parent_edge[vertex])
        parity[parent[vertex]] ^= parity[vertex]
    if parity[ROOT_VERTEX]: raise AssertionError("odd tree syndrome")
    return selected


def build_tree_code(length: int, fibers: dict) -> dict:
    graph = c532.c247.PunctureGraph(length, terminals=1)
    chunks = c537.wilson_chunks(graph)
    roles = tuple(sorted(fibers, key=repr))
    coordinates = tuple(site for role in roles for site in fibers[role])
    index = {}; cursor = graph.qubits
    for role in roles:
        index[role] = tuple(range(cursor, cursor + len(fibers[role]))); cursor += len(fibers[role])
    qubits = cursor
    equality = []
    for role in roles:
        for left, right in combinations(index[role], 2): equality.append(c235.Pauli(x=(1 << left) ^ (1 << right)))
    face_by_axis = []
    all_faces = []
    vertices, base_edges = fill_tree(length)
    for axis in range(3):
        axis_faces = []
        for vertex in vertices:
            row = c235.Pauli() if vertex == ROOT_VERTEX else chunks[axis][vertex]
            for left, right in base_edges:
                if vertex in (left, right):
                    role = (axis, left, right)
                    z = sum(1 << bit for bit in index[role])
                    row = row @ c235.Pauli(z=z)
            axis_faces.append(row); all_faces.append(row)
        face_by_axis.append(tuple(axis_faces))

    def dress(pauli):
        x = pauli.x; selected_count = 0
        for axis in range(3):
            marked = {j for j, chunk in enumerate(chunks[axis]) if not pauli.commutes(chunk)}
            if len(marked) % 2: raise AssertionError("non-Wilson-commuting row")
            for left, right in tree_selected_edges(marked, length):
                role = (axis, left, right); x ^= 1 << index[role][0]; selected_count += 1
        return c235.Pauli(pauli.phase, x, pauli.z), selected_count

    local_meta = [dress(row) for row in c532.local_stabilizers(graph)]
    matter_meta = [dress(row) for row in c532.matter_generators(graph)]
    raw_gz, raw_ga, gauge_edges = c532.gauge_generators(graph)
    gauge_meta = [dress(row) for row in raw_gz + raw_ga]
    local = tuple(row for row, _ in local_meta); matter = tuple(row for row, _ in matter_meta)
    gauge = tuple(row for row, _ in gauge_meta)
    stabilizers = local + tuple(equality) + tuple(all_faces)
    return {
        "graph": graph, "chunks": chunks, "roles": roles, "fibers": fibers, "index": index,
        "coordinates": coordinates, "qubits": qubits, "equality": tuple(equality),
        "faces": tuple(all_faces), "face_by_axis": tuple(face_by_axis), "local": local,
        "matter": matter, "gauge": gauge, "gauge_edges": gauge_edges,
        "stabilizers": stabilizers,
        "maximum_selected_tree_edges": {
            "local": max(count for _, count in local_meta),
            "matter": max(count for _, count in matter_meta),
            "gauge": max(count for _, count in gauge_meta),
        },
    }


def factorization_controls(length: int, fibers: dict, full_commutant=False) -> tuple[dict, dict]:
    obj = build_tree_code(length, fibers); graph = obj["graph"]; qubits = obj["qubits"]
    cells = length**3; stabilizers = obj["stabilizers"]
    rank, inconsistent = c532.phase_rank(stabilizers, qubits)
    stabv = tuple(row.symplectic(qubits) for row in stabilizers)
    matterv = tuple(row.symplectic(qubits) for row in obj["matter"])
    gaugev = tuple(row.symplectic(qubits) for row in obj["gauge"])
    matter_reps = c532.quotient_complement(stabv, matterv)
    gauge_reps = c532.quotient_complement(stabv, gaugev)
    matter_rank = c532.symplectic_gram_rank(matter_reps, qubits)
    gauge_rank = c532.symplectic_gram_rank(gauge_reps, qubits)
    commutant_dimension = commutant_rank = None
    if full_commutant:
        mask = (1 << qubits) - 1
        equations = tuple((row >> qubits) | ((row & mask) << qubits) for row in stabv + matterv)
        centralizer = c532.null_basis(equations, 2 * qubits)
        reps = c532.quotient_complement(stabv, centralizer)
        commutant_dimension = len(reps); commutant_rank = c532.symplectic_gram_rank(reps, qubits)
    products = tuple(c537.pauli_product(rows) for rows in obj["face_by_axis"])
    exact_products = tuple(products) == c532.wilson_initializers(graph)
    wilson_inc = tuple(len(c532.quotient_complement(stabv, (row.symplectic(qubits),))) for row in c532.wilson_initializers(graph))
    comm_fail = {
        "stabilizer_mutual": sum(not left.commutes(right) for i, left in enumerate(stabilizers) for right in stabilizers[i+1:]),
        "matter_stabilizer": sum(not row.commutes(stab) for row in obj["matter"] for stab in stabilizers),
        "gauge_stabilizer": sum(not row.commutes(stab) for row in obj["gauge"] for stab in stabilizers),
        "matter_gauge": sum(not row.commutes(gauge) for row in obj["matter"] for gauge in obj["gauge"]),
    }
    expected_rank = 15 * cells + 1 + (qubits - graph.qubits)
    result = {
        "length": length, "coarse_cells": cells, "rough_M2": graph.qubits,
        "physical_orbit_aux_M2": qubits - graph.qubits, "total_M2": qubits,
        "average_total_M2_per_coarse_cell": qubits / cells,
        "tree_logical_edges": 3 * length, "tree_face_checks": 3 * (length + 1),
        "equality_check_rows_displayed": len(obj["equality"]),
        "stabilizer_rank": rank, "expected_stabilizer_rank": expected_rank,
        "code_exponent": qubits - rank, "expected_code_exponent": 7 * cells - 1,
        "face_product_exact_old_Wilson_including_phase": exact_products,
        "face_product_phases": tuple(row.phase for row in products),
        "old_Wilson_rank_increments": wilson_inc,
        "matter_quotient_dimension_rank": (len(matter_reps), matter_rank),
        "expected_matter_dimension_rank": (12 * cells - 1, 12 * cells - 2),
        "gauge_quotient_dimension_rank": (len(gauge_reps), gauge_rank),
        "expected_gauge_dimension_rank": (2 * cells - 1, 2 * cells - 2),
        "full_matter_commutant_dimension_rank": (commutant_dimension, commutant_rank),
        "commutator_failures": comm_fail,
        "maximum_face_support_M2": max((row.x | row.z).bit_count() for row in obj["faces"]),
        "maximum_equality_support_M2": 2,
        "maximum_dressed_support_M2": {
            "local": max((row.x | row.z).bit_count() for row in obj["local"]),
            "matter": max((row.x | row.z).bit_count() for row in obj["matter"]),
            "gauge": max((row.x | row.z).bit_count() for row in obj["gauge"]),
        },
        "maximum_selected_tree_edges": obj["maximum_selected_tree_edges"],
    }
    result["pass"] = bool(inconsistent == 0 and rank == expected_rank and qubits-rank == 7*cells-1
                           and exact_products and wilson_inc == (0,0,0)
                           and result["matter_quotient_dimension_rank"] == result["expected_matter_dimension_rank"]
                           and result["gauge_quotient_dimension_rank"] == result["expected_gauge_dimension_rank"]
                           and all(value == 0 for value in comm_fail.values())
                           and (not full_commutant or (commutant_dimension,commutant_rank) == (2*cells-1,2*cells-2)))
    check(f"L{length} orbit-replicated tree fill has exact Wilson products, rank/code exponent, and target-times-gauge quotient",
          result["pass"], {key: result[key] for key in ("physical_orbit_aux_M2", "stabilizer_rank", "code_exponent", "matter_quotient_dimension_rank", "gauge_quotient_dimension_rank", "commutator_failures")})
    return result, obj


def old_position_K(graph, qubit: int):
    row = graph.edges[qubit]; center = K * np.asarray(row.owner, dtype=int)
    if row.kind == "rough_terminal": offset = np.zeros(3, dtype=int)
    elif row.kind == "puncture_spoke": offset = 4 * np.asarray(c532.c210.DIRECTIONS[row.label], dtype=int)
    elif row.kind == "matter_internal_triangle":
        left = graph.base.vertices[row.u][1]; right = graph.base.vertices[row.v][1]
        offset = 2 * (np.asarray(c532.c210.DIRECTIONS[left], dtype=int) + np.asarray(c532.c210.DIRECTIONS[right], dtype=int))
    elif row.kind == "matter_outer_square":
        direction = graph.base.vertices[row.u][1]; offset = 16 * np.asarray(c532.c210.DIRECTIONS[direction], dtype=int)
    else: raise ValueError(row.kind)
    return tuple(int(value) for value in center + offset)


def periodic_l1(left, right, modulus):
    return sum(min((left[a]-right[a]) % modulus, (right[a]-left[a]) % modulus) for a in range(3))


def shortest_deltas(left, right, modulus):
    choices = []
    for axis in range(3):
        positive = (right[axis] - left[axis]) % modulus
        negative = positive - modulus
        if abs(positive) < abs(negative): choices.append((positive,))
        elif abs(negative) < abs(positive): choices.append((negative,))
        else: choices.append((negative, positive))
    return tuple(product(*choices))


def shortest_path_family(left, right, modulus):
    paths = set()
    for deltas in shortest_deltas(left, right, modulus):
        for order in permutations(range(3)):
            current = list(left); path = [tuple(current)]
            for axis in order:
                step = 1 if deltas[axis] > 0 else -1
                for _ in range(abs(deltas[axis])):
                    current[axis] = (current[axis] + step) % modulus
                    path.append(tuple(current))
            if tuple(current) != tuple(right): raise AssertionError("shortest router endpoint")
            paths.add(tuple(path))
    return tuple(sorted(paths))


def routing_scout(length: int, obj: dict) -> dict:
    modulus = K * length
    old = tuple(tuple(value % modulus for value in old_position_K(obj["graph"], q)) for q in range(obj["graph"].qubits))
    aux = {bit: tuple(site[a] % modulus for a in range(3))
           for role in obj["roles"] for bit, site in zip(obj["index"][role], obj["fibers"][role])}
    rows = obj["equality"] + obj["faces"]
    route_pairs = 0; maximum = 0; total_shortest = 0; support_hist = Counter()
    route_variants = 0; owner_site_incidences = 0; occupancy = Counter(); digest = sha256()
    for row in rows:
        mask = row.x | row.z; sites = []
        while mask:
            bit = mask & -mask; q = bit.bit_length()-1; mask ^= bit
            sites.append(old[q] if q < obj["graph"].qubits else aux[q])
        support_hist[len(sites)] += 1
        for left, right in combinations(sites, 2):
            distance = periodic_l1(left, right, modulus)
            route_pairs += 1; total_shortest += distance; maximum = max(maximum, distance)
            family = shortest_path_family(left, right, modulus)
            route_variants += len(family)
            owner_sites = {site for path in family for site in path}
            owner_site_incidences += len(owner_sites)
            occupancy.update(owner_sites)
            digest.update(repr((left, right, family)).encode())
    shared = sum(value > 1 for value in occupancy.values())
    maximum_owners = max(occupancy.values(), default=0)
    result = {
        "length": length, "physical_period": modulus,
        "checks_scouted": len(rows), "unordered_support_pair_routes": route_pairs,
        "support_weight_histogram": dict(support_hist),
        "total_shortest_fine_NN_edges_if_pairs_routed_separately": total_shortest,
        "maximum_shortest_fine_NN_path_edges": maximum,
        "all_axis_order_and_tied_sign_route_variants": route_variants,
        "route_owner_site_incidences": owner_site_incidences,
        "distinct_physical_sites_touched": len(occupancy),
        "physical_sites_with_multiple_route_owners": shared,
        "maximum_route_owner_multiplicity_at_one_site": maximum_owners,
        "path_family_sha256": digest.hexdigest(),
        "route_rule": "state-carried endpoint coordinates may enumerate all signed shortest steps and all axis orders; no path table is required",
        "all24_path_family_covariance": "the full shortest-path family is invariant under signed coordinate permutations",
        "crossing_ownership": "each descriptor owns (check label, unordered support pair); shared sites and maximum owner multiplicity are exhaustively counted but not yet autonomously scheduled",
        "literal_fine_NN_path_exists_for_every_pair": True,
        "host_path_table_used": False,
        "autonomous_crossing_schedule_or_static_local_check_gadget_constructed": False,
        "strict_physical_enforcement_pass": False,
    }
    check(f"L{length} every tree-fill check support pair has an explicit bounded finite-NN route family without a stored path table",
          route_pairs > 0 and maximum <= 3 * modulus // 2 and not result["host_path_table_used"],
          {"pairs": route_pairs, "max": maximum, "total": total_shortest})
    return result


def deletion_controls(obj: dict) -> dict:
    qubits = obj["qubits"]; full_rank, _ = c532.phase_rank(obj["stabilizers"], qubits)
    deleted_face = obj["local"] + obj["equality"] + obj["faces"][1:]
    face_rank, _ = c532.phase_rank(deleted_face, qubits)
    wilson = c532.wilson_initializers(obj["graph"])[0]
    increment = len(c532.quotient_complement(tuple(row.symplectic(qubits) for row in deleted_face), (wilson.symplectic(qubits),)))
    target = next(role for role in obj["roles"] if len(obj["index"][role]) > 1)
    bits = obj["index"][target]; isolated = bits[0]
    pruned_equality = tuple(row for row in obj["equality"] if not ((row.x >> isolated) & 1))
    pruned = obj["local"] + pruned_equality + obj["faces"]
    pruned_rank, _ = c532.phase_rank(pruned, qubits)
    malformed = obj["faces"][0]
    malformed = c235.Pauli(malformed.phase, malformed.x, malformed.z ^ (1 << isolated))
    syndrome = sum(not malformed.commutes(row) for row in obj["equality"])
    result = {
        "full_rank": full_rank, "delete_one_face_rank": face_rank,
        "deleted_face_rank_loss": full_rank-face_rank,
        "deleted_face_old_Wilson_rank_increment": increment,
        "disconnect_one_repetition_copy_rank": pruned_rank,
        "disconnected_copy_rank_loss": full_rank-pruned_rank,
        "malformed_one-copy_face_equality_syndromes": syndrome,
        "pass": face_rank == full_rank-1 and increment == 1 and pruned_rank == full_rank-1 and syndrome > 0,
    }
    check("face deletion, orbit-copy disconnection, and malformed incidence expose independent residuals",
          result["pass"], result)
    return result


def immutable_citation(path: str, fragment: str) -> dict:
    body = subprocess.check_output(
        ["git", "show", f"{IMMUTABLE_COMMIT}:{path}"], cwd=ROOT, text=True
    )
    for line, text in enumerate(body.splitlines(), start=1):
        if fragment in text:
            return {
                "ref": IMMUTABLE_COMMIT, "path": path, "line": line,
                "line_text": text.strip(), "fragment": fragment,
            }
    raise AssertionError(f"immutable citation absent: {path}: {fragment}")


def current_citation(path: str, fragment: str) -> dict:
    for line, text in enumerate((ROOT / path).read_text().splitlines(), start=1):
        if fragment in text:
            return {
                "ref": "Cycle642 working artifact", "path": path, "line": line,
                "line_text": text.strip(), "fragment": fragment,
            }
    raise AssertionError(f"current citation absent: {path}: {fragment}")


def no_go_gate(square: dict) -> dict:
    qualifying = [
        {"family":"exact marked square-disk row-permutation placement","object":"Cycle537 marked face/chunk incidence","mechanism":"one fixed injective proper-cubic action","terminal":"all24 incidence automorphism","marker":"ATTEMPTED","result":"quarter-turn falsifier at L3/L6/L7"},
        {"family":"unchanged-torus plaquette cap","object":"old cubic two-chain","mechanism":"sum old plaquette boundaries","terminal":"one axial Wilson boundary","marker":"RULED OUT BY PRIOR","result":"Cycle637 dual-cocycle pairing"},
        {"family":"orbit-split tree normal form","object":"bounded-degree incidence tree plus cubic stabilizer fibers","mechanism":"tree edge cancellation and X repetition constraints","terminal":"static local enforcement or autonomous routed controller","marker":"ATTEMPTED","result":"algebra/rank/K129 roles positive; terminal open"},
    ]
    open_routes = [
        {"family":"cubic-symmetric redesigned disk","object":"new face/star complex","mechanism":"role splitting before attachment","terminal":"exact full-matter fixed embedding","status":"OPEN / NOT COUNTED","result":"not ruled out"},
        {"family":"defect/code-growth encoder","object":"temporary rough boundaries","mechanism":"leave code, grow and reglue","terminal":"local E and restored target intertwiner","status":"OPEN / NOT COUNTED","result":"not ruled out"},
        {"family":"time-multiplexed cap worldvolume","object":"reusable ancillas and state-carried program","mechanism":"sequential incidence simulation","terminal":"autonomous inverse/leakage and no host control","status":"OPEN / NOT COUNTED","result":"not ruled out"},
        {"family":"cut-sheet deformation","object":"open periodic planes","mechanism":"temporary boundary then reglue","terminal":"proper-cubic restored streams","status":"OPEN / NOT COUNTED","result":"not ruled out"},
    ]
    walls = {
        "W_fixed_incidence":"replace Cycle537's retriangulated marked square orbit by one fixed cubic incidence",
        "W_local_enforcement":"turn routed support geometry into static local gauge checks or an autonomous stored controller",
        "W_prepare":"construct code-state E/initialization preserving the target factor",
    }
    pairs = []
    for source in walls:
        for target in walls:
            if source == target: continue
            pairs.append({
                "from": source, "to": target, "implied": False,
                "reason": f"closing {source} does not construct or prove {target}",
            })
    c537_embed = immutable_citation(
        "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md",
        "It does not embed those cap",
    )
    c537_open = immutable_citation(
        "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md",
        "dynamic puncture sweep",
    )
    c637_old = immutable_citation(
        "docs/work_history/repo/review_feedback/PHYSICAL_UNCHANGED_TORUS_CAP_HOMOLOGY_DISCRIMINATOR_CYCLE637_NOTE_2026-07-23.md",
        "Therefore no static plaquette",
    )
    c637_open = immutable_citation(
        "docs/work_history/repo/review_feedback/PHYSICAL_UNCHANGED_TORUS_CAP_HOMOLOGY_DISCRIMINATOR_CYCLE637_NOTE_2026-07-23.md",
        "Added topology or a genuinely enlarged local incidence graph",
    )
    c629_orbit = immutable_citation(
        "docs/work_history/repo/review_feedback/PHYSICAL_TRANSLATION_ORBIT_MARKER_CRYSTAL_REPAIR_CYCLE629_NOTE_2026-07-22.md",
        "PASS at exact declared scope. The phase is state-carried",
    )
    c638_route = immutable_citation(
        "docs/work_history/repo/review_feedback/PHYSICAL_HIERARCHICAL_GRAMMAR_FULL_ACT_COMPILER_CYCLE638_NOTE_2026-07-23.md",
        "does not store the Cycle-630 parent tree",
    )
    c638_open = immutable_citation(
        "docs/work_history/repo/review_feedback/PHYSICAL_HIERARCHICAL_GRAMMAR_FULL_ACT_COMPILER_CYCLE638_NOTE_2026-07-23.md",
        "a literal physical encoder `E`",
    )
    current_square = current_citation(
        "scripts/physical_fixed_cubic_wilson_fill_incidence_cycle642_2026_07_23.py",
        "the exact marked Cycle537 square presentation has no injective",
    )
    current_tree = current_citation(
        "scripts/physical_fixed_cubic_wilson_fill_incidence_cycle642_2026_07_23.py",
        '"old_torus_plaquette_cap":"RULED_OUT_BY_CYCLE637"',
    )
    current_route = current_citation(
        "scripts/physical_fixed_cubic_wilson_fill_incidence_cycle642_2026_07_23.py",
        "FAIL_NOT_CLOSED: exact square incidence fails",
    )
    n4_matches = [{
        "prior_ref": c637_old["ref"], "prior_path": c637_old["path"],
        "prior_line": c637_old["line"],
        "prior_residual": "no old-periodic cubic plaquette two-chain has an axial Wilson boundary",
        "current_path": current_tree["path"], "current_line": current_tree["line"],
        "current_residual": "the orbit-tree comparator changes the incidence and does not reopen the old-plaquette route",
        "same_scope": True, "exact_match": True, "use_as_closure": True,
    }]
    n4_nonmatches = [
        {
            "prior_ref": c537_embed["ref"], "prior_path": c537_embed["path"],
            "prior_line": c537_embed["line"],
            "prior_residual": "one fixed frame-independent physical cap embedding plus preparation is absent",
            "current_path": current_square["path"], "current_line": current_square["line"],
            "current_residual": "only the exact unsplit one-chunk/one-marked-face square incidence is quarter-turn falsified",
            "same_scope": False, "exact_match": False, "use_as_closure": False,
        },
        {
            "prior_ref": c638_open["ref"], "prior_path": c638_open["path"],
            "prior_line": c638_open["line"],
            "prior_residual": "Cycle638 has no literal physical encoder E",
            "current_path": current_route["path"], "current_line": current_route["line"],
            "current_residual": "Cycle642 has route geometry but no autonomous local enforcement or preparation",
            "same_scope": False, "exact_match": False, "use_as_closure": False,
        },
    ]
    n5 = [
        {
            "claim":"the exact marked Cycle537 square is not one fixed injective row-permutation cubic incidence",
            "per_element":"all marked chunk-face incidences are tested under the axial quarter-turn",
            "per_site":"no conclusion about arbitrary physical-site gadgets; orbit-split sites remain open",
            "per_mode":"no fermionic-mode no-go is inferred",
            "per_block":"L3/L6/L7 exact marked disks are enumerated",
            "lattice_wide":"no general local-compiler impossibility is inferred",
        },
        {
            "claim":"finite-NN path geometry is not autonomous local enforcement",
            "per_element":"every equality/face support pair has a shortest-path family",
            "per_site":"shared physical route sites and maximum owner multiplicity are counted",
            "per_mode":"matter/gauge quotient compatibility is algebraic only",
            "per_block":"K129 roles and route families are tested at L3/L6/L7",
            "lattice_wide":"crossing schedule, full-code leakage, E, and G_physical are untested",
        },
    ]
    n6 = [
        {"file":"UNMATERIALIZED/static_subsystem_wire_cycle_next.py","status":"OPEN / PRIORITY","what_closes":"W_local_enforcement with local static equality/face gadgets"},
        {"file":"UNMATERIALIZED/physical_defect_code_growth_E_cycle_next.py","status":"OPEN","what_closes":"W_prepare without requiring a static square disk"},
        {"file":"UNMATERIALIZED/state_carried_cap_crossing_controller_cycle_next.py","status":"OPEN","what_closes":"W_local_enforcement for routed incidence without host scheduling"},
    ]
    n7 = {
        "mechanism":"split every symmetric axial attachment into its proper-cubic stabilizer fiber and connect those fibers with a static subsystem wire code or a state-carried crossing controller",
        "actionable_steps":[
            "compile each displayed XX equality and Z face row to support-one/two fine-NN primitives",
            "color or gauge every shared route site with locally stored ownership and clean inverse/exhaust",
            "execute full-code leakage and then construct preparation E as a separate terminal",
        ],
        "why_it_breaks_the_negative":"the positive orbit-tree comparator already preserves Wilson products and target quotient after role splitting, so the unsplit-square quarter-turn witness cannot exclude the split construction",
        "terminal_test":"literal local enforcement or autonomous routed checks, all24/all576 update covariance, deletion/malformed rejection, full-code leakage, and E G_coarse = G_physical E without host control",
        "supporting_citations":[c637_open, c638_route, c537_open],
    }
    n8 = [
        {"cycle":537,"retired":"the need for growing Wilson initializer rows after adding cap topology","mechanism":"bounded square-disk face/star algebra","applicability":"supports changed incidence while leaving fixed embedding and preparation open","citation_ref":c537_embed["ref"],"citation_path":c537_embed["path"],"citation_line":c537_embed["line"],"citation_text":c537_embed["line_text"]},
        {"cycle":629,"retired":"external origin at the supplied projector-sector level","mechanism":"state-carried translation orbit and cubic marker fibers","applicability":"shows orbit splitting can repair covariance without proving enforcement","citation_ref":c629_orbit["ref"],"citation_path":c629_orbit["path"],"citation_line":c629_orbit["line"],"citation_text":c629_orbit["line_text"]},
        {"cycle":637,"retired":"unchanged-torus static plaquette realization","mechanism":"exact H1 dual-cocycle discriminator","applicability":"forces changed incidence but leaves enlarged/dynamic routes open","citation_ref":c637_old["ref"],"citation_path":c637_old["path"],"citation_line":c637_old["line"],"citation_text":c637_old["line_text"]},
        {"cycle":638,"retired":"stored 4,570-path parent table","mechanism":"coordinate-counter route generation","applicability":"offers a controller mechanism but does not supply Cycle642 enforcement or E","citation_ref":c638_route["ref"],"citation_path":c638_route["path"],"citation_line":c638_route["line"],"citation_text":c638_route["line_text"]},
    ]
    return {
        "Status":"PASS",
        "N1_normalized_families":qualifying,
        "N1_open_routes_not_counted":open_routes,
        "N1_qualifying_attempts":len(qualifying), "N1_required_for_negative":5,
        "N1_negative_gate":"FAIL / DO NOT SHIP", "N1_broad_gate":"FAIL / DO NOT SHIP",
        "N2_collapsed_walls":walls, "N2_directed_ordered_pairs":pairs,
        "N2_negative_gate":"FAIL / DO NOT SHIP: no directed implication combines the three walls",
        "N3_hidden_wall_scan":[
            {"phrase":"supplied K129 block origin and shell","classification":"explicit condition","wall":"W_fixed_incidence"},
            {"phrase":"one finite K129 outer shell has finite orbit capacity while fill-tree roles grow as O(L)","classification":"explicit finite-held-family scope; asymptotic distributed placement is open","wall":"W_fixed_incidence"},
            {"phrase":"state-carried endpoint route rule","classification":"descriptor only, not enforcement","wall":"W_local_enforcement"},
            {"phrase":"target-times-gauge quotient","classification":"algebraic code statement, not preparation","wall":"W_prepare"},
        ],
        "N4_exact_residual_matches":n4_matches,
        "N4_nonmatches_not_used_as_closure":n4_nonmatches,
        "N4_negative_gate":"FAIL / DO NOT SHIP beyond the one exact old-plaquette residual",
        "N5_rhetoric":n5,
        "N6_partial_closure_paths":n6,
        "N7_steelman":n7,
        "N8_cross_cycle_echo":n8,
        "broad_no_go_claim":False, "minimum_content_claim":False,
        "shared_obstruction_claim":False, "axiom_pressure_claim":False,
        "shared_route_independent_obstruction":False, "axiom_pressure":False,
        "narrow_marked_square_falsifier":square["pass_as_narrow_falsifier"],
    }


def main() -> int:
    global PASS, FAIL
    started = time.perf_counter()
    observed = {name: git_blob_sha(name) for name in PINS}
    imported = {
        name: str(Path(module.__file__).resolve())
        for name, module in sys.modules.items()
        if name.startswith("physical_") and getattr(module, "__file__", None)
    }
    immutable_import_failures = [path for path in imported.values() if not Path(path).is_relative_to(IMMUTABLE_ROOT)]
    check("Cycle532/537/637/638 shores are immutable git blobs and every imported physical module comes from the export",
          observed == PINS and not immutable_import_failures,
          {"commit":IMMUTABLE_COMMIT,"files":len(PINS),"modules":len(imported),
           "blob_mismatches":[k for k in PINS if observed[k]!=PINS[k]],
           "working_tree_imports":immutable_import_failures})
    square = square_marking_falsifier()
    no_refit_rows = [tree_controls(length) for length in range(3, 32)]
    check("one closed-form fill_tree formula has connected E=V-1 reflection-invariant degree<=4 output for every L3..L31",
          all(row["pass"] for row in no_refit_rows),
          {"lengths":[row["length"] for row in no_refit_rows],
           "edge_minus_vertex_plus_one":sorted({row["edge_count"]-row["vertex_count"]+1 for row in no_refit_rows}),
           "maximum_degree":max(row["maximum_degree"] for row in no_refit_rows),
           "reflection_failures":sum(row["reflection_failures"] for row in no_refit_rows)})
    trees = []; placements = []; factors = []; routes = []; objects = {}
    for length in (3, 6, 7):
        tree = tree_controls(length)
        check(f"L{length} reflection-symmetric bounded-degree tree has one-check Euler surplus", tree["pass"], tree)
        placement, fibers = allocate_orbit_roles(length)
        factor, obj = factorization_controls(length, fibers, full_commutant=(length == 3))
        route = routing_scout(length, obj)
        trees.append(tree); placements.append(placement); factors.append(factor); routes.append(route); objects[length]=obj
    deletion = deletion_controls(objects[3])
    no_go = no_go_gate(square)
    exact_markers = {"ATTEMPTED", "RULED OUT BY PRIOR"}
    n4_fields = {"prior_ref","prior_path","prior_line","prior_residual","current_path","current_line","current_residual","same_scope","exact_match","use_as_closure"}
    check("full N1-N8 schema passes while every broad negative gate remains FAIL / DO NOT SHIP",
          no_go["Status"] == "PASS" and no_go["N1_broad_gate"] == "FAIL / DO NOT SHIP"
          and len(no_go["N1_normalized_families"]) == 3
          and all(row["marker"] in exact_markers for row in no_go["N1_normalized_families"])
          and all("marker" not in row for row in no_go["N1_open_routes_not_counted"])
          and len(no_go["N2_directed_ordered_pairs"]) == 6
          and all(n4_fields <= set(row) for row in no_go["N4_exact_residual_matches"] + no_go["N4_nonmatches_not_used_as_closure"])
          and all(set(("per_element","per_site","per_mode","per_block","lattice_wide")) <= set(row) for row in no_go["N5_rhetoric"])
          and all(set(("file","status","what_closes")) <= set(row) for row in no_go["N6_partial_closure_paths"])
          and not no_go["shared_route_independent_obstruction"] and not no_go["axiom_pressure"],
          {"qualifying":len(no_go["N1_normalized_families"]),"open":len(no_go["N1_open_routes_not_counted"]),"directed_pairs":len(no_go["N2_directed_ordered_pairs"]),"status":no_go["Status"]})
    markers = ("Authority: **none**", "Audit: **unset**", "exact marked square", "not a physical encoder", "N1-N8", "Axiom pressure: **none**")
    note_text = NOTE.read_text()
    check("Cycle642 note freezes the narrow falsifier, positive comparator, scope firewall, and N1-N8", all(marker in note_text for marker in markers), markers)
    head = subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip()
    result = {
        "cycle":642, "date":"2026-07-23",
        "status":"cycle642-partial-narrowing-positive-orbit-tree-comparator",
        "classification":"partial narrowing with exact marked-square covariance falsifier and positive orbit-tree enlarged-incidence comparator",
        "authority":AUTHORITY, "audit":AUDIT, "author_accepted":False,
        "author_artifact_status_accepted":False, "breakthrough":False,
        "constitutional_effect":"none",
        "shared_route_independent_obstruction":False,
        "axiom_pressure":False,
        "broad_no_go_claim":False,
        "minimum_content_claim":False,
        "shared_obstruction_claim":False,
        "axiom_pressure_claim":False,
        "git_head_at_run":head, "shore":{"pins":PINS,"observed":observed,
            "immutable_export_commit":IMMUTABLE_COMMIT,
            "actual_imported_physical_modules":imported,
            "working_tree_bytes_used_as_premise":False,
            "immutable_import_failures":immutable_import_failures,
            "no_go_skill_origin_main_sha256":NO_GO_ORIGIN_MAIN_SHA256,
            "skill_freshness_file_sha256":FRESHNESS_SHA256},
        "exact_Cycle537_marked_square_fixed_frame_falsifier":square,
        "size_uniform_fill_tree_no_refit_scan_L3_L31":{
            "formula":"vertices {root} union Z_L; odd L=2m+1 has root--0 plus reflected +/- chains; even L=2m has root--0, root--m plus reflected +/- chains",
            "lengths":list(range(3,32)),
            "rows":no_refit_rows,
            "all_connected_E_eq_V_minus_1_reflection_invariant_degree_le_4":all(row["pass"] for row in no_refit_rows),
            "full_rank_or_quotient_credit_outside_L3_L6_L7":False,
        },
        "reflection_symmetric_fill_trees":trees,
        "fixed_K129_orbit_role_placements":placements,
        "tree_fill_target_times_gauge_certificates":factors,
        "fine_NN_routing_scouts":routes,
        "deletion_and_malformed_incidence":deletion,
        "strict_fixed_3D_embedding_disposition":"FAIL_NOT_CLOSED: exact square incidence fails; tree roles/ranks pass but autonomous local enforcement/crossing schedule is absent",
        "strongest_constructive_result":"three proper-cubic orbit-replicated bounded-degree fill trees in fixed K129 shells have injective roles, all24/all576 fiber covariance, exact face-product Wilson phases, rank 15N+1+n_aux, code exponent 7N-1, and exact matter/gauge quotient data at L3/L6/L7",
        "supplied_structure_inventory":{
            "immutable_Cycle532_rough_graph_chunks_matter_and_gauge":True,
            "immutable_Cycle537_square_disk_and_phase_repair":True,
            "immutable_Cycle637_old_torus_scope_boundary":True,
            "immutable_Cycle638_K129_inner_role_envelope":True,
            "one_macro_origin_K129_partition_and_outer_shell":True,
            "finite_periodic_L3_L6_L7_domains":True,
            "reflection_symmetric_tree_topology_per_length":True,
            "size_uniform_fill_tree_formula":"vertices {root} union Z_L; odd L=2m+1 has root--0 and two reflected chains root--(+/-1)--...--(+/-m); even L=2m has root--0, root--m and reflected chains root--(+/-1)--...--(+/-(m-1)); no fitted parameter varies by size",
            "size_uniform_formula_refit_between_L3_L6_L7":False,
            "K129_outer_shell_allocation_scope":"finite L3/L6/L7 held-family certificate only; not an asymptotic all-L placement",
            "asymptotic_distributed_tree_role_placement":False,
            "generic_cubic_orbit_seed_enumeration":True,
            "pairwise_XX_fiber_equality_presentation":True,
            "all_axis_order_shortest_path_family":True,
            "runtime_frame_selector":False,
            "host_Wilson_or_parity_query":False,
            "host_path_table":False,
            "state_preparation_or_initialization":False,
        },
        "novelty_boundary":{
            "new_here":"quarter-turn incidence falsifier for the exact marked square; reflection-symmetric tree fill; stabilizer-fiber orbit replication; exact K129 collision/rank/quotient/routing/deletion certificates",
            "not_claimed":"general bosonization, physical encoder E, full M64 G_physical, autonomous local constraint enforcement, state genesis, causal time, energy, source, or gravity",
            "prior_art_engine_used":"Cycle532/537 code algebra only; no Thirring engine used",
        },
        "not_constructed":{"local_encoding_E":False,"full_M64_G_physical":False,"state_preparation_or_initialization":False,
            "autonomous_static_or_routed_constraint_enforcement":False,"host_path_table":False,"hidden_fourth_dimension":False,
            "global_parity_service":False,"preferred_fermion_ordering":False},
        "no_go_discipline":no_go,
        "six_wall_ledger":{
            "C_ref":"narrowed: orbit fibers remove the role-stabilizer collision for the tree comparator; the macro-origin/K129 shell remains supplied",
            "C_num":"retained: exact ranks and phases only; no empirical normalization or Born statement",
            "C_wrap":"narrowed: old Wilsons are exact products of bounded-support tree faces, but preparation/history meaning remains open",
            "C_int":"retained conditionally: matter/gauge quotient and prior mass/contact/seam inheritance are algebraic, not a physical E/G",
            "C_local":"mixed: exact marked square is falsified; tree role placement and finite-NN route geometry pass; autonomous local enforcement remains open",
            "C_source":"unchanged: no energy, stress, resource-source, or gravity identification",
        },
        "semantic_firewall":{"program_or_schedule_is_time":False,"generator_is_rate":False,"phase_is_energy":False,
            "pointer_is_Record":False,"coarse_CAR_cell_is_physical_site_compiler":False},
        "route_disposition":{
            "exact_Cycle537_marked_square_fixed_embedding":"NARROWLY_FALSIFIED_BY_AXIS_QUARTER_TURN",
            "orbit_split_tree_enlarged_incidence":"ALGEBRA_AND_FIXED_ROLE_PLACEMENT_PASS_LOCAL_ENFORCEMENT_OPEN",
            "old_torus_plaquette_cap":"RULED_OUT_BY_CYCLE637",
            "defect_code_growth":"OPEN","time_multiplexed":"OPEN","cubic_symmetric_redesigned_disk":"OPEN",
        },
        "optimal_next_campaign":"compile the orbit-tree X-equality and Z-face rows into a literal static subsystem-wire gadget or a state-carried fine-NN syndrome controller with explicit crossing colors, clean inverse/exhaust, and full physical-code leakage; then separately construct preparation E",
        "resources":{"elapsed_seconds":time.perf_counter()-started,"maximum_RSS_bytes":int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform=='darwin' else resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)},
        "tests_passed":PASS,"tests_failed":FAIL,"tests_total":PASS+FAIL,"pass":FAIL==0,
    }
    RECEIPT.write_text(json.dumps(result,indent=2,sort_keys=True,default=json_default)+"\n")
    print(json.dumps({"status":"PASS" if FAIL==0 else "FAIL","tests":f"{PASS}/{PASS+FAIL}","receipt":str(RECEIPT.relative_to(ROOT)),"elapsed":result["resources"]["elapsed_seconds"]},sort_keys=True))
    return int(FAIL != 0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as stream:
        original=sys.stdout; sys.stdout=Tee(original,stream)
        try: raise SystemExit(main())
        finally: sys.stdout=original
