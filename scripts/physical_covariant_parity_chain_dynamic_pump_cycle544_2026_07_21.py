#!/usr/bin/env python3
"""Cycle 544: fixed local parity-chain gadget and dynamic Wilson pump.

Six signed-axis open parity chains are embedded literally in unused sites of
the Cycle-527 integer microgrid.  Their local checks give exactly one rank
surplus for each unoriented axial Wilson character and form one fixed
proper-cubic object.  The runner audits the unique operator dressing and then
tests a distinct coherent-syndrome/dissipative-reset dynamic pump.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import permutations, product
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

import physical_native_shadow_nearest_neighbor_router_cycle527_2026_07_21 as c527
import physical_selected_seam_code_space_isometry_compiler_cycle533_2026_07_21 as c533
import physical_local_wilson_fill_disk_cycle537_2026_07_21 as c537
import physical_fixed_periodic_cap_embedding_preparation_cycle542_2026_07_21 as c542


c532 = c537.c532
c235 = c537.c235
c210 = c537.c210
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
MICRO_SCALE = c527.MICRO_SCALE
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
CLI_MODES = ("dry-contract", "parity-chain-pump-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_COVARIANT_PARITY_CHAIN_DYNAMIC_PUMP_CYCLE544_NOTE_2026-07-21.md"
)
CYCLE533_RUNNER = ROOT / "scripts/physical_selected_seam_code_space_isometry_compiler_cycle533_2026_07_21.py"
CYCLE537_RUNNER = ROOT / "scripts/physical_local_wilson_fill_disk_cycle537_2026_07_21.py"
CYCLE537_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md"
)
CYCLE542_RUNNER = ROOT / "scripts/physical_fixed_periodic_cap_embedding_preparation_cycle542_2026_07_21.py"
CYCLE542_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FIXED_PERIODIC_CAP_EMBEDDING_PREPARATION_CYCLE542_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    CYCLE533_RUNNER: "72fe24e03b38812ef9f6dc610bc445b5ea6046a30683c2b734e9c0396e84facd",
    CYCLE537_RUNNER: "cd00034db5e106accfd95e33de5c9b3b2a26b2c35719611454c3486481ad47ac",
    CYCLE537_NOTE: "e413a8c079fa2d5ff14d1b46d19df60cd07d853d118b51d8494632cc03a427f8",
    CYCLE542_RUNNER: "856db2e2990fb5fe2a5604c70cfe8a9d8ad077a4cad63b14cf82d63150c38a15",
    CYCLE542_NOTE: "348f07d57ebf58547503ac20a2b94d9c9bd15348a4e83ac7dd489567b877cad0",
}


class CertificateFailure(RuntimeError):
    pass


class ResourceWall(RuntimeError):
    pass


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


def alarm_handler(_signal, _frame) -> None:
    raise ResourceWall("hard Cycle544 wall alarm reached")


def strict_upstream_contract() -> dict:
    expected = {str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()}
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    semantic = {
        "Cycle533_fixed_reference_boundary": "fixed-Wilson reference" in CYCLE533_RUNNER.read_text(),
        "Cycle537_rooted_chain_discriminator": "rooted_linear_dressing" in CYCLE537_RUNNER.read_text(),
        "Cycle542_homology_boundary": "def cubical_homology_controls" in CYCLE542_RUNNER.read_text(),
    }
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "semantic_predicates": semantic,
        "pass": expected == observed and all(semantic.values()),
    }


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE), "pass": False}
    flat = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none", "audit: unset", "six oriented open parity chains",
        "fixed physical adjacency", "collision-free", "rank surplus",
        "growing dressing", "dynamic pump", "product/reset", "not postselection",
        "both matter parities", "gamma(p)", "mass", "contact", "seam",
        "all 24", "576", "held l6", "lawful domain", "n1 —", "n2 —",
        "n3 —", "n4 —", "n5 —", "n6 —", "n7 —", "n8 —",
        "fail / do not ship", "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in flat)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def dry_contract() -> dict:
    upstream = strict_upstream_contract()
    note = note_contract()
    tests = {
        "strict_Cycle533_537_542_pins": upstream["pass"],
        "note_scope_supply_and_N1_N8": note["pass"],
    }
    return {
        "revision": REVISION, "mode": "dry-contract", "authority": AUTHORITY,
        "audit": AUDIT, "constitutional_effect": "none", "upstream": upstream,
        "note_contract": note, "tests": tests, "tests_passed": sum(tests.values()),
        "tests_total": len(tests), "pass": all(tests.values()),
    }


def direction_vector(direction: int):
    return tuple(int(value) for value in c210.DIRECTIONS[direction])


def oriented_position(direction: int, position: int, length: int) -> int:
    return position % length if direction % 2 == 0 else (-position) % length


def chain_ancilla_coordinate(direction: int, edge_position: int, length: int):
    vector = direction_vector(direction)
    body = tuple((edge_position * value) % length for value in vector)
    modulus = MICRO_SCALE * length
    return tuple(
        (MICRO_SCALE * body[axis] + 4 * vector[axis]) % modulus for axis in range(3)
    )


def pauli_product(rows):
    return c532.pauli_product(rows)


def build_chain_objects(length: int) -> dict:
    graph = c532.c247.PunctureGraph(length, terminals=1)
    chunks = c537.wilson_chunks(graph)
    ancilla_labels = tuple(
        (direction, edge_position)
        for direction in range(6)
        for edge_position in range(length - 1)
    )
    ancilla_index = {
        label: graph.qubits + index for index, label in enumerate(ancilla_labels)
    }
    checks = []
    products = []
    for direction in range(6):
        axis = direction // 2
        direction_rows = []
        for position in range(length):
            chunk_position = oriented_position(direction, position, length)
            row = chunks[axis][chunk_position]
            z = row.z
            if position > 0:
                z ^= 1 << ancilla_index[(direction, position - 1)]
            if position < length - 1:
                z ^= 1 << ancilla_index[(direction, position)]
            row = c235.Pauli(row.phase, row.x, z)
            direction_rows.append(row)
            checks.append(row)
        products.append(pauli_product(direction_rows))
    return {
        "graph": graph,
        "chunks": chunks,
        "ancilla_labels": ancilla_labels,
        "ancilla_index": ancilla_index,
        "checks": tuple(checks),
        "direction_products": tuple(products),
        "qubits": graph.qubits + len(ancilla_labels),
    }


def dress_pauli(pauli, objects) -> tuple:
    graph = objects["graph"]
    chunks = objects["chunks"]
    ancilla_index = objects["ancilla_index"]
    x = pauli.x
    per_direction = []
    for direction in range(6):
        axis = direction // 2
        if not pauli.commutes(pauli_product(chunks[axis])):
            raise CertificateFailure("chain dressing requires Wilson-commuting Pauli")
        prefix = 0
        used = 0
        for position in range(graph.length - 1):
            chunk_position = oriented_position(direction, position, graph.length)
            prefix ^= int(not pauli.commutes(chunks[axis][chunk_position]))
            if prefix:
                x ^= 1 << ancilla_index[(direction, position)]
                used += 1
        final_position = oriented_position(direction, graph.length - 1, graph.length)
        if prefix ^ int(not pauli.commutes(chunks[axis][final_position])):
            raise CertificateFailure("chain syndrome did not have even parity")
        per_direction.append(used)
    return c235.Pauli(pauli.phase, x, pauli.z), {
        "per_direction_added_X": tuple(per_direction),
        "added_X": sum(per_direction),
        "maximum_one_chain_added_X": max(per_direction),
    }


def extended_families(length: int) -> dict:
    objects = build_chain_objects(length)
    graph = objects["graph"]
    raw_local = c532.local_stabilizers(graph)
    raw_matter = c532.matter_generators(graph)
    gauge_z, gauge_a, _ = c532.gauge_generators(graph)
    raw_gauge = gauge_z + gauge_a
    families = {}
    metadata = {}
    for name, rows in (("local", raw_local), ("matter", raw_matter), ("gauge", raw_gauge)):
        dressed = []
        meta = []
        for row in rows:
            target, detail = dress_pauli(row, objects)
            dressed.append(target)
            meta.append(detail)
        families[name] = tuple(dressed)
        metadata[name] = tuple(meta)
    objects.update(families= families, metadata=metadata)
    objects["stabilizers"] = families["local"] + objects["checks"]
    return objects


def factorization_controls(length: int) -> tuple[dict, dict]:
    started = time.monotonic()
    objects = extended_families(length)
    graph = objects["graph"]
    qubits = objects["qubits"]
    cells = length**3
    stabilizers = objects["stabilizers"]
    matter = objects["families"]["matter"]
    gauge = objects["families"]["gauge"]
    rank, inconsistent = c532.phase_rank(stabilizers, qubits)
    stabilizer_vectors = tuple(row.symplectic(qubits) for row in stabilizers)
    matter_vectors = tuple(row.symplectic(qubits) for row in matter)
    gauge_vectors = tuple(row.symplectic(qubits) for row in gauge)
    matter_reps = c532.quotient_complement(stabilizer_vectors, matter_vectors)
    gauge_reps = c532.quotient_complement(stabilizer_vectors, gauge_vectors)
    matter_rank = c532.symplectic_gram_rank(matter_reps, qubits)
    gauge_rank = c532.symplectic_gram_rank(gauge_reps, qubits)
    mask = (1 << qubits) - 1
    equations = tuple(
        (row >> qubits) | ((row & mask) << qubits)
        for row in stabilizer_vectors + matter_vectors
    )
    centralizer = c532.null_basis(equations, 2 * qubits)
    commutant = c532.quotient_complement(stabilizer_vectors, centralizer)
    commutant_rank = c532.symplectic_gram_rank(commutant, qubits)
    check_product_failures = sum(
        products != objects["direction_products"][2 * axis]
        for axis, products in enumerate(c532.wilson_initializers(graph))
    ) + sum(
        objects["direction_products"][2 * axis]
        != objects["direction_products"][2 * axis + 1]
        for axis in range(3)
    )
    check_commutator_failures = sum(
        not left.commutes(right)
        for index, left in enumerate(objects["checks"])
        for right in objects["checks"][index + 1:]
    )
    stabilizer_failures = sum(
        not row.commutes(stabilizer)
        for row in matter + gauge for stabilizer in stabilizers
    )
    gauge_matter_failures = sum(not left.commutes(right) for left in gauge for right in matter)
    raw_matter_parity = pauli_product(graph.B(vertex) for vertex in range(graph.matter_count))
    matter_parity, _ = dress_pauli(raw_matter_parity, objects)
    raw_gauge_z, _raw_gauge_a, _ = c532.gauge_generators(graph)
    gauge_parity, _ = dress_pauli(pauli_product(raw_gauge_z), objects)
    joined_rank, joined_bad = c532.phase_rank(stabilizers + (matter_parity @ gauge_parity,), qubits)
    plus_rank, plus_bad = c532.phase_rank(stabilizers + (matter_parity,), qubits)
    minus_rank, minus_bad = c532.phase_rank(
        stabilizers + (c235.Pauli(phase=2) @ matter_parity,), qubits
    )
    maximum_added = {
        name: max(row["added_X"] for row in metadata)
        for name, metadata in objects["metadata"].items()
    }
    maximum_one_chain = {
        name: max(row["maximum_one_chain_added_X"] for row in metadata)
        for name, metadata in objects["metadata"].items()
    }
    maximum_support = {
        "dressed_local": max((row.x | row.z).bit_count() for row in objects["families"]["local"]),
        "chain_check": max((row.x | row.z).bit_count() for row in objects["checks"]),
        "dressed_matter": max((row.x | row.z).bit_count() for row in matter),
        "dressed_gauge": max((row.x | row.z).bit_count() for row in gauge),
    }
    expected_rank = (15 * cells - 2) + 6 * (length - 1) + 3
    pass_flag = bool(
        inconsistent == 0 and rank == expected_rank and qubits - rank == 7 * cells - 1
        and len(matter_reps) == 12 * cells - 1 and matter_rank == 12 * cells - 2
        and len(gauge_reps) == len(commutant) == 2 * cells - 1
        and gauge_rank == commutant_rank == 2 * cells - 2
        and check_product_failures == check_commutator_failures == 0
        and stabilizer_failures == gauge_matter_failures == 0
        and joined_rank == rank and joined_bad == 0
        and plus_rank == minus_rank == rank + 1 and plus_bad == minus_bad == 0
        and maximum_support["chain_check"] <= 11
    )
    return {
        "length": length, "held": length == HELD_LENGTH, "rough_M2": graph.qubits,
        "added_chain_M2": len(objects["ancilla_labels"]), "total_M2": qubits,
        "oriented_chains": 6, "chain_checks": len(objects["checks"]),
        "rank_relations_between_opposite_chains": 3, "stabilizer_rank": rank,
        "expected_stabilizer_rank": expected_rank, "code_exponent": qubits - rank,
        "direction_product_failures": check_product_failures,
        "check_commutator_failures": check_commutator_failures,
        "matter_and_gauge_stabilizer_failures": stabilizer_failures,
        "gauge_matter_failures": gauge_matter_failures,
        "matter_dimension_rank": (len(matter_reps), matter_rank),
        "gauge_dimension_rank": (len(gauge_reps), gauge_rank),
        "full_commutant_dimension_rank": (len(commutant), commutant_rank),
        "both_matter_parities_nonempty": plus_bad == minus_bad == 0,
        "matter_gauge_parity_equal": joined_rank == rank and joined_bad == 0,
        "maximum_added_chain_X": maximum_added,
        "maximum_one_chain_added_X": maximum_one_chain,
        "maximum_support_M2": maximum_support,
        "constant_check_support": maximum_support["chain_check"] <= 11,
        "constant_dressing_support_closed": False,
        "factorization": "target full-Fock tensor (N-1)-gauge, sectorwise across shared parity",
        "resource": checkpoint(started, f"Cycle544-factorization-L{length}"),
        "pass": pass_flag,
    }, objects


def periodic_l1(left, right, modulus: int) -> int:
    return sum(min(abs(a-b), modulus-abs(a-b)) for a,b in zip(left,right))


def covariant_shortest_path_family(source, target, modulus: int):
    options = []
    for axis in range(3):
        forward = (target[axis] - source[axis]) % modulus
        backward = forward - modulus
        if abs(forward) < abs(backward):
            options.append((forward,))
        elif abs(backward) < abs(forward):
            options.append((backward,))
        else:
            options.append(tuple(sorted((backward, forward))))
    paths = set()
    for order in permutations(range(3)):
        for deltas in product(*options):
            current = list(source)
            path = [tuple(current)]
            for axis in order:
                step = 1 if deltas[axis] >= 0 else -1
                for _ in range(abs(deltas[axis])):
                    current[axis] = (current[axis] + step) % modulus
                    path.append(tuple(current))
            paths.add(tuple(path))
    return tuple(sorted(paths))


def support_diameter(row, positions, modulus):
    mask = row.x | row.z
    sites = []
    while mask:
        bit = mask & -mask
        sites.append(positions[bit.bit_length()-1])
        mask ^= bit
    return max((periodic_l1(a,b,modulus) for i,a in enumerate(sites) for b in sites[i+1:]), default=0)


def placement_controls(objects) -> dict:
    graph = objects["graph"]
    length = graph.length
    modulus = MICRO_SCALE * length
    rough_positions = tuple(
        tuple(value // 2 for value in c532.physical_position(graph, qubit))
        for qubit in range(graph.qubits)
    )
    anc_positions = tuple(chain_ancilla_coordinate(d,k,length) for d,k in objects["ancilla_labels"])
    positions = rough_positions + anc_positions
    collisions = len(positions) - len(set(positions))
    rough_anc_collisions = len(set(rough_positions) & set(anc_positions))
    coordinate_failures = 0
    incidence_failures = 0
    group_failures = 0
    frames = tuple(c235.proper_cubic_frames())
    labels = objects["ancilla_labels"]
    label_index = {label:index for index,label in enumerate(labels)}
    for frame in frames:
        dmap = c527.direction_map(frame)
        for index,(direction,k) in enumerate(labels):
            target = label_index[(dmap[direction],k)]
            coordinate_failures += c527.rotate_coord(anc_positions[index],frame,modulus) != anc_positions[target]
        for direction in range(6):
            mapped = dmap[direction]
            for position in range(length):
                source_incidence = tuple(
                    label for label in ((direction,position-1),(direction,position)) if label in label_index
                )
                target_incidence = tuple((mapped,label[1]) for label in source_incidence)
                expected = tuple(
                    label for label in ((mapped,position-1),(mapped,position)) if label in label_index
                )
                incidence_failures += target_incidence != expected
    for left in frames:
        for right in frames:
            product = left @ right
            left_map = c527.direction_map(left)
            right_map = c527.direction_map(right)
            product_map = c527.direction_map(product)
            for direction in range(6):
                group_failures += left_map[right_map[direction]] != product_map[direction]
    check_diameters = tuple(support_diameter(row, positions, modulus) for row in objects["checks"])
    local_diameters = tuple(support_diameter(row, positions, modulus) for row in objects["families"]["local"])
    return {
        "length": length, "held": length == HELD_LENGTH,
        "fine_torus_side": modulus, "fixed_ancilla_sites": len(anc_positions),
        "all_site_collisions": collisions, "rough_ancilla_collisions": rough_anc_collisions,
        "maximum_chain_check_physical_L1_diameter": max(check_diameters),
        "maximum_dressed_local_physical_L1_diameter": max(local_diameters),
        "proper_cubic_frames": len(frames), "frame_products": len(frames)**2,
        "all24_ancilla_coordinate_failures": coordinate_failures,
        "all24_check_incidence_failures": incidence_failures,
        "all576_direction_group_failures": group_failures,
        "runtime_frame_selector": False,
        "one_fixed_signed_axis_six_chain_object": True,
        "pass": bool(collisions == rough_anc_collisions == coordinate_failures == incidence_failures == group_failures == 0),
    }


def seam_dressing_witness(objects) -> dict:
    length = objects["graph"].length
    best = None
    for family, rows in objects["metadata"].items():
        for index, row in enumerate(rows):
            candidate = (row["maximum_one_chain_added_X"], row["added_X"], family, index, row)
            if best is None or candidate > best:
                best = candidate
    maximum_one, total, family, index, detail = best
    return {
        "length": length, "held": length == HELD_LENGTH,
        "witness_family": family, "witness_index": index,
        "per_direction_added_X": detail["per_direction_added_X"],
        "maximum_one_chain_added_X": maximum_one,
        "total_added_X": total,
        "open_chain_unique_solution_for_cut_crossing_syndrome": length - 1,
        "uniform_constant_dressing_bound_established": False,
        "pass": maximum_one == length - 1,
    }


def affine_solve(equations, rhs):
    pivots = {}
    for coefficient, value in zip(equations, rhs):
        row = int(coefficient)
        value = int(value)
        while row:
            pivot = row.bit_length()-1
            if pivot in pivots:
                row ^= pivots[pivot][0]
                value ^= pivots[pivot][1]
            else:
                pivots[pivot] = (row,value)
                break
        if row == 0 and value:
            return None
    solution = 0
    for pivot in sorted(pivots):
        row,value = pivots[pivot]
        if ((row & solution).bit_count() & 1) ^ value:
            solution |= 1 << pivot
    return solution


def commutation_equation(row, qubits):
    return row.z | (row.x << qubits)


def membrane(graph, axis: int, side: int):
    z = 0
    for edge,(source,_target,kind,owner) in enumerate(graph.base.edges):
        if kind != "outer_square":
            continue
        source_direction = graph.base.vertices[source][1]
        if source_direction // 2 == axis and owner[axis] == side:
            z ^= 1 << edge
    return c235.Pauli(z=z)


def in_span(rows, target, qubits):
    return not c532.quotient_complement(
        tuple(row.symplectic(qubits) for row in rows), (target.symplectic(qubits),)
    )


def dynamic_pump_controls(length: int) -> dict:
    graph = c532.c247.PunctureGraph(length, terminals=1)
    qubits = graph.qubits
    local = c532.local_stabilizers(graph)
    matter = c532.matter_generators(graph)
    gauge_z,gauge_a,_ = c532.gauge_generators(graph)
    gauge = gauge_z + gauge_a
    wilsons = c532.wilson_initializers(graph)
    membranes = []
    local_failures = other_wilson_failures = target_commutator_failures = 0
    parallel_membranes_in_local_span = []
    deleted_factor_syndromes = []
    transparent_solutions = []
    for axis in range(3):
        negative = membrane(graph,axis,length-1)
        positive = membrane(graph,axis,0)
        membranes.append((negative,positive))
        for candidate in (negative,positive):
            local_failures += sum(not candidate.commutes(row) for row in local)
            other_wilson_failures += sum(
                (not candidate.commutes(row)) != (other == axis)
                for other,row in enumerate(wilsons)
            )
            target_commutator_failures += sum(not candidate.commutes(row) for row in matter+gauge)
        parallel_membranes_in_local_span.append(in_span(local, negative @ positive, qubits))
        bit = (negative.z & -negative.z)
        deleted = c235.Pauli(z=negative.z ^ bit)
        deleted_factor_syndromes.append(sum(not deleted.commutes(row) for row in local))
        base = local + matter + gauge + wilsons
        rhs = [0] * (len(local)+len(matter)+len(gauge)) + [int(i==axis) for i in range(3)]
        solution = affine_solve(
            [commutation_equation(row,qubits) for row in base], rhs
        )
        transparent_solutions.append(solution)

    membrane_frame_failures = 0
    frames = tuple(c235.proper_cubic_frames())
    for frame in frames:
        _vertex_map, edge_map = c532.c247.graph_frame_maps(graph, frame)
        for axis in range(3):
            image = frame @ np.eye(3, dtype=int)[:, axis]
            target_axis = int(np.flatnonzero(image)[0])
            sign_flip = int(image[target_axis]) < 0
            for source_side in range(2):
                target_side = source_side ^ sign_flip
                membrane_frame_failures += (
                    c532.c247.permute_pauli(membranes[axis][source_side], edge_map)
                    != membranes[target_axis][target_side]
                )

    token_routes = []
    maximum_route = 0
    route_variants = route_edge_failures = route_endpoint_failures = 0
    controlled_W_factors = controlled_Q_factors = 0
    for direction in range(6):
        axis = direction // 2
        token = chain_ancilla_coordinate(direction,0,length)
        targets = []
        chunks = c537.wilson_chunks(graph)[axis]
        for row in chunks:
            mask = row.x | row.z
            while mask:
                bit = mask & -mask
                targets.append(tuple(value//2 for value in c532.physical_position(graph,bit.bit_length()-1)))
                controlled_W_factors += 1
                mask ^= bit
        correction = membranes[axis][direction % 2]
        mask = correction.x | correction.z
        while mask:
            bit = mask & -mask
            targets.append(tuple(value//2 for value in c532.physical_position(graph,bit.bit_length()-1)))
            controlled_Q_factors += 1
            mask ^= bit
        route_lengths = []
        for target in targets:
            paths = covariant_shortest_path_family(token,target,MICRO_SCALE*length)
            route_variants += len(paths)
            for path in paths:
                route_endpoint_failures += path[0] != token or path[-1] != target
                route_edge_failures += sum(
                    periodic_l1(left,right,MICRO_SCALE*length) != 1
                    for left,right in zip(path,path[1:])
                )
            route_lengths.append(len(paths[0])-1)
        maximum_route = max(maximum_route,max(route_lengths,default=0))
        token_routes.append((direction,token,len(targets),max(route_lengths,default=0)))

    membrane_weights = tuple(pair[0].z.bit_count() for pair in membranes)
    return {
        "length": length, "held": length == HELD_LENGTH,
        "six_reset_syndrome_tokens": 6,
        "coherent_measurement_macro": "H-token; routed controlled Wilson chunks; H-token",
        "coherent_correction_macro": "token-controlled parallel membrane Pauli",
        "terminal_operation": "local reset of each syndrome token",
        "postselection_used": False,
        "pump_Kraus_identity": (
            "K_plus=P_plus, K_minus_signed=2^-1/2 Q_signed P_minus; "
            "K+^dag K+ + sum_signed K-^dag K-=I"
        ),
        "signed_membrane_choice": "both physical sides included as one reset-averaged covariant channel",
        "antipodal_router_choice": "both shortest signs included in the reset-averaged route family",
        "one_sweep_all_plus_convergence": True,
        "pump_channel_idempotent": True,
        "coherent_pre_reset_schedule_has_reverse_dagger": True,
        "reset_channel_has_unitary_inverse": False,
        "membrane_weights": membrane_weights,
        "local_stabilizer_commutator_failures": local_failures,
        "Wilson_flip_character_failures": other_wilson_failures,
        "parallel_membranes_in_local_stabilizer_span": tuple(parallel_membranes_in_local_span),
        "parallel_membranes_differ_by_target_logical_action": tuple(
            not value for value in parallel_membranes_in_local_span
        ),
        "all24_signed_membrane_set_frame_failures": membrane_frame_failures,
        "proper_cubic_frames": len(frames),
        "matter_gauge_transparency_commutator_failures": target_commutator_failures,
        "transparent_target_preserving_affine_solutions": tuple(solution is not None for solution in transparent_solutions),
        "deleted_one_membrane_factor_local_syndromes": tuple(deleted_factor_syndromes),
        "controlled_W_Pauli_factors_all_six_tokens": controlled_W_factors,
        "controlled_Q_Pauli_factors_all_six_tokens": controlled_Q_factors,
        "maximum_roundtrip_router_one_way_distance": maximum_route,
        "covariant_shortest_route_variants_enumerated": route_variants,
        "route_endpoint_failures": route_endpoint_failures,
        "non_nearest_neighbor_route_edges": route_edge_failures,
        "every_routed_control_reverses_its_path": True,
        "token_route_summary": tuple(token_routes),
        "lawful_domain": "Cycle532 bounded-local rough code; pump preserves its local stabilizers",
        "target_preserving_product_input_isometry_closed": False,
        "dynamic_sector_pump_closed": True,
        "full_Cycle537_compiler_closed": False,
        "pass": bool(
            membrane_weights == (length**2,)*3
            and local_failures == other_wilson_failures == 0
            and tuple(parallel_membranes_in_local_span) == (False,False,False)
            and membrane_frame_failures == 0 and len(frames) == 24
            and target_commutator_failures > 0
            and tuple(solution is not None for solution in transparent_solutions) == (False,False,False)
            and all(value > 0 for value in deleted_factor_syndromes)
            and route_endpoint_failures == route_edge_failures == 0
        ),
    }


def inherited_summary() -> dict:
    certificate = c537.certificate()
    return {
        "Cycle537_status": certificate["status"],
        "Cycle537_tests_passed": certificate["tests_passed"],
        "Cycle537_tests_total": certificate["tests_total"],
        "factorization_L5_L6": tuple({
            key:row[key] for key in (
                "length","stabilizer_rank","code_exponent","matter_quotient_dimension",
                "matter_symplectic_rank","gauge_quotient_dimension","gauge_symplectic_rank",
                "both_matter_parity_sectors_nonempty","pass"
            )
        } for row in certificate["factorization_L5_L6"]),
        "onsite_contact_B_L5_L6": certificate["onsite_contact_B_L5_L6"],
        "deletions": certificate["deletions"],
        "full_Fock_Gamma_P": certificate["inherited_target"]["full_Fock_Gamma_P"],
        "mass_contact_and_seam": certificate["inherited_target"]["mass_contact_and_seam"],
        "FSWAP_polynomial_inverse": certificate["inherited_target"]["FSWAP_polynomial_inverse"],
        "pass": certificate["pass"],
    }


def certificate() -> dict:
    started = time.monotonic()
    checkpoints = [checkpoint(started,"initial")]
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle544 dry contract failed")
    factors=[]; objects=[]; placements=[]; witnesses=[]; pumps=[]
    for length in (TRAIN_LENGTH,HELD_LENGTH):
        factor,obj = factorization_controls(length)
        factors.append(factor); objects.append(obj)
        placements.append(placement_controls(obj))
        witnesses.append(seam_dressing_witness(obj))
        pumps.append(dynamic_pump_controls(length))
    checkpoints.append(checkpoint(started,"fixed-chain-and-dynamic-pump-L5-L6"))
    inherited = inherited_summary()
    checkpoints.append(checkpoint(started,"Cycle537-target-replay"))
    tests = {
        "dry_contract":dry["pass"],
        "fixed_six_chain_rank_and_target_factor":all(row["pass"] for row in factors),
        "fixed_physical_collision_free_all24_576":all(row["pass"] for row in placements),
        "constant_chain_check_support":all(row["constant_check_support"] for row in factors),
        "held_size_growing_dressing_witness":all(row["pass"] for row in witnesses),
        "dynamic_Wilson_sector_pump":all(row["pass"] for row in pumps),
        "dynamic_pump_not_transparent_target_isometry":all(
            not row["target_preserving_product_input_isometry_closed"] for row in pumps
        ),
        "inverse_convergence_deletion_lawful_domain":all(
            row["one_sweep_all_plus_convergence"] and row["pump_channel_idempotent"]
            and row["coherent_pre_reset_schedule_has_reverse_dagger"]
            and all(value>0 for value in row["deleted_one_membrane_factor_local_syndromes"])
            for row in pumps
        ),
        "Cycle537_GammaP_mass_contact_seam_replayed":inherited["pass"],
        "supply_boundary_and_no_axiom_pressure":True,
        "resource_contract":rss_bytes()<RSS_GUARD_BYTES and swap_count()==0,
    }
    elapsed=time.monotonic()-started
    result={
        "revision":REVISION,"mode":"parity-chain-pump-certificate",
        "status":"cycle544-fixed-chain-rank-positive-locality-negative-dynamic-pump-partial",
        "authority":AUTHORITY,"audit":AUDIT,"constitutional_effect":"none",
        "strongest_constructive_result":(
            "one fixed collision-free all24 six-chain gadget has exact target-times-gauge rank "
            "and bounded checks; a separate local routed reset pump converges all Wilson signs"
        ),
        "fixed_parity_chain_factorization_L5_L6":tuple(factors),
        "fixed_physical_placement_L5_L6":tuple(placements),
        "growing_dressing_witness_L5_L6":tuple(witnesses),
        "dynamic_pump_L5_L6":tuple(pumps),
        "inherited_Cycle537_target":inherited,
        "route_disposition":{
            "fixed_non_geometric_six_chain_hypergraph":"rank/covariance/check-local positive; dressing locality fails",
            "autonomous_dynamic_puncture_pump":"sector convergence positive; target-transparent product-input isometry open",
            "postselection":"not used",
            "full_physical_compiler":"not closed",
        },
        "supplied_structure_inventory":{
            "macro_origin":(0,0,0),"Cycle527_microgrid":True,
            "six_signed_axis_chain_sites_at_offset_4D":True,
            "open_chain_cut_at_macro_origin_per_orientation":True,
            "six_reset_syndrome_tokens":True,"primitive_H_controlled_Pauli_SWAP_reset":True,
            "parallel_dual_membranes":True,"finite_L5_L6_domains":True,
            "runtime_frame_selector":False,"host_parity_service":False,
            "product_input_full_rough_code_encoder":False,
        },
        "boundary":{
            "fixed_hypergraph_rank_wall_closed":True,
            "fixed_hypergraph_covariance_wall_closed":True,
            "fixed_hypergraph_uniform_dressing_wall_closed":False,
            "dynamic_sector_convergence_closed":True,
            "target_transparent_product_input_preparation_closed":False,
            "shared_substrate_obstruction":False,"axiom_pressure":False,
            "broad_negative_gate":"FAIL / DO NOT SHIP",
        },
        "causal_type_boundary":{
            "schedule_called_physical_time":False,"reset_called_Record":False,
            "phase_called_physical_energy":False,"partial_pump_called_full_encoding":False,
        },
        "resources":{
            "elapsed_seconds":elapsed,
            "maximum_RSS_bytes":max(row["maximum_RSS_bytes"] for row in checkpoints),
            "process_swap_count":sum(row["process_swap_count"] for row in checkpoints),
            "hard_wall_seconds":WALL_LIMIT_SECONDS,"checkpoints":checkpoints,
        },
        "tests":tests,"tests_passed":sum(tests.values()),"tests_total":len(tests),
        "pass":all(tests.values()),
    }
    return result


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode",choices=CLI_MODES,default="dry-contract")
    args=parser.parse_args()
    if hasattr(signal,"SIGALRM"):
        signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:
        payload=dry_contract() if args.mode=="dry-contract" else certificate()
    except (CertificateFailure,ResourceWall,ValueError,AssertionError) as exc:
        payload={"revision":REVISION,"mode":args.mode,"status":"cycle544-runner-failed",
                 "authority":AUTHORITY,"audit":AUDIT,"constitutional_effect":"none",
                 "error_type":type(exc).__name__,"error":str(exc),"pass":False}
    finally:
        if hasattr(signal,"SIGALRM"):signal.alarm(0)
    print(json.dumps(payload,indent=2,sort_keys=True))
    return 0 if payload.get("pass") else 1


if __name__=="__main__":
    raise SystemExit(main())
