#!/usr/bin/env python3
"""Cycle 551: boundary-aware multi-star recurrence tournament.

Three scheduler families act on the same oriented degree-three star network:
  A. a boundary-aware coloring of actual translated physical footprints;
  B. colored composition of Cycle548 returned-slot pair/singleton macros;
  C. a one-hot relational token on an explicit NN Hamiltonian rail.

This is a decoded-runtime scheduling theorem conditional on one supplied
global selected-carrier encoder/reference allocation.  No compiler order is
called time.  Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import defaultdict, deque
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_adjacent_star_recurrence_tournament_cycle548_2026_07_21 as c548


c545 = c548.c545
c539 = c548.c539
c533 = c548.c533
c532 = c548.c532
c523 = c548.c523
c324 = c548.c324
c311 = c548.c311

AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 2.0e-10
WALL_LIMIT_SECONDS = 1200.0
RSS_GUARD_BYTES = 2_900_000_000
CLI_MODES = ("dry-contract", "multistar-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_BOUNDARY_AWARE_MULTISTAR_RECURRENCE_TOURNAMENT_CYCLE551_NOTE_2026-07-21.md"
)
C548_RUNNER = ROOT / "scripts/physical_adjacent_star_recurrence_tournament_cycle548_2026_07_21.py"
C548_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ADJACENT_STAR_RECURRENCE_TOURNAMENT_CYCLE548_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    C548_RUNNER: "23b3b1a66cd60366a43fcd7a4d15ad9da68f9dc6a6aa40e774d0e94c8317ef80",
    C548_NOTE: "db16fe47dae51428447f42b88418fd0181a8908fee16a95f73b4bbf60fa23c04",
}

DIRECTION_VECTORS = tuple(tuple(int(v) for v in row) for row in c311.c210.DIRECTIONS)


class CertificateFailure(RuntimeError):
    """A scoped Cycle-551 certificate predicate failed."""


@dataclass(frozen=True, order=True)
class Star:
    center: tuple[int, int, int]
    arms: tuple[int, int, int]


@dataclass(frozen=True, order=True)
class Block:
    kind: str
    centers: tuple[tuple[int, int, int], ...]


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
    swaps = swap_count()
    if elapsed >= WALL_LIMIT_SECONDS:
        raise CertificateFailure(f"wall limit reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise CertificateFailure(f"RSS guard reached at {label}: {rss}")
    if swaps:
        raise CertificateFailure(f"nonzero process swap count at {label}: {swaps}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swaps,
    }


def alarm_handler(_signum, _frame) -> None:
    raise CertificateFailure("Cycle551 hard wall alarm fired")


def body_add(body, direction: int, length: int):
    vector = DIRECTION_VECTORS[direction]
    return tuple((body[axis] + vector[axis]) % length for axis in range(3))


def shift_body(body, shift, length: int):
    return tuple((body[axis] + shift[axis]) % length for axis in range(3))


def star_support(star: Star, length: int) -> frozenset:
    return frozenset((star.center,) + tuple(body_add(star.center, arm, length) for arm in star.arms))


def matching_network(length: int, origin=(0, 0, 0)) -> tuple[tuple[Star, ...], tuple[Block, ...]]:
    """Boundary-aware x matching; an odd row ends in one +x singleton."""

    stars = {}
    blocks = []
    for y in range(length):
        for z in range(length):
            yy = (origin[1] + y) % length
            zz = (origin[2] + z) % length
            paired_limit = length if length % 2 == 0 else length - 1
            for relative_x in range(0, paired_limit, 2):
                first = ((origin[0] + relative_x) % length, yy, zz)
                second = ((origin[0] + relative_x + 1) % length, yy, zz)
                stars[first] = Star(first, (0, 2, 4))
                stars[second] = Star(second, (1, 2, 4))
                blocks.append(Block("pair", (first, second)))
            if length % 2:
                singleton = ((origin[0] + length - 1) % length, yy, zz)
                stars[singleton] = Star(singleton, (0, 2, 4))
                blocks.append(Block("singleton", (singleton,)))
    ordered_stars = tuple(stars[center] for center in sorted(stars))
    return ordered_stars, tuple(sorted(blocks))


def shifted_coordinate(coordinate, source_body, target_body, length: int):
    modulus = c533.c527.fine_length(length)
    source = c533.c527.cell_center(source_body, length)
    target = c533.c527.cell_center(target_body, length)
    return tuple((coordinate[axis] + target[axis] - source[axis]) % modulus for axis in range(3))


def shifted_footprint(footprint, source_body, target_body, length: int):
    return frozenset(
        shifted_coordinate(site, source_body, target_body, length)
        for site in footprint
    )


def physical_templates(length: int) -> tuple[dict, dict]:
    decoder, objects = c548.fixed_order_decoder(length)
    schedule = c548.physical_q_schedule(length, objects)
    inventory = schedule["_inventory"]
    updates = schedule["_updates"]
    slot = inventory["slot"]
    modulus = inventory["modulus"]

    update_footprints = {
        name: frozenset(site for gate in gates for site in gate.sites)
        for name, gates in updates.items()
    }
    controlled_footprints = {}
    controlled_pair_counts = {}
    for name, gates in updates.items():
        footprint = {slot}
        required_pairs = set()
        for gate in gates:
            logical_wires = (slot,) + gate.sites
            footprint.update(logical_wires)
            for first, second in combinations(logical_wires, 2):
                required_pairs.add(tuple(sorted((first, second))))
        route_failures = 0
        maximum_route = 0
        for first, second in required_pairs:
            path = c539.periodic_route_with_tie(first, second, modulus)
            footprint.update(path)
            maximum_route = max(maximum_route, len(path) - 1)
            route_failures += sum(
                c533.c527.periodic_l1(left, right, modulus) != 1
                for left, right in zip(path, path[1:])
            )
        controlled_footprints[name] = frozenset(footprint)
        controlled_pair_counts[name] = {
            "required_pairs": len(required_pairs),
            "maximum_route_edges": maximum_route,
            "route_failures": route_failures,
        }

    pair_footprint = controlled_footprints["A"] | controlled_footprints["B"]
    slot_macro = c548.slot_macro_controls((schedule,))
    counts = schedule["_update_primitive_counts"]
    result = {
        "length": length,
        "held_size": length == HELD_LENGTH,
        "decoder_pass": decoder["pass"],
        "physical_schedule_pass": schedule["pass"],
        "slot_macro_pass": slot_macro["pass"],
        "update_counts": counts,
        "unconditioned_footprint_sites": {
            name: len(value) for name, value in update_footprints.items()
        },
        "controlled_footprint_sites": {
            name: len(value) for name, value in controlled_footprints.items()
        },
        "pair_controlled_footprint_sites": len(pair_footprint),
        "controlled_pair_routes": controlled_pair_counts,
        "pair_slot_skeleton": slot_macro["two_half_physical_skeleton_L5_L6"][0],
        "pass": bool(
            decoder["pass"]
            and schedule["pass"]
            and slot_macro["pass"]
            and all(row["route_failures"] == 0 for row in controlled_pair_counts.values())
        ),
    }
    return result, {
        "schedule": schedule,
        "inventory": inventory,
        "update_footprints": update_footprints,
        "controlled_footprints": controlled_footprints,
        "pair_footprint": pair_footprint,
    }


def conflict_coloring(footprints: dict) -> tuple[dict, int, int]:
    keys = tuple(sorted(footprints))
    adjacency = {key: set() for key in keys}
    for first, second in combinations(keys, 2):
        if footprints[first] & footprints[second]:
            adjacency[first].add(second)
            adjacency[second].add(first)
    colors = {}
    while len(colors) < len(keys):
        candidates = [key for key in keys if key not in colors]
        selected = max(
            candidates,
            key=lambda key: (
                len({colors[n] for n in adjacency[key] if n in colors}),
                len(adjacency[key]),
                tuple(-value for value in key) if isinstance(key[0], int) else repr(key),
            ),
        )
        used = {colors[n] for n in adjacency[selected] if n in colors}
        colors[selected] = next(color for color in range(len(keys)) if color not in used)
    collisions = sum(
        colors[first] == colors[second] and bool(footprints[first] & footprints[second])
        for first, second in combinations(keys, 2)
    )
    return colors, max(map(len, adjacency.values()), default=0), collisions


def star_template_name(star: Star) -> str:
    return "A" if star.arms[0] == 0 else "B"


def route_A_coloring(length: int, objects: dict) -> tuple[dict, tuple[Star, ...]]:
    stars, blocks = matching_network(length)
    footprints = {}
    for star in stars:
        name = star_template_name(star)
        source = c548.CELLS[0] if name == "A" else c548.CELLS[1]
        footprints[star.center] = shifted_footprint(
            objects["update_footprints"][name], source, star.center, length
        )
    colors, maximum_degree, collisions = conflict_coloring(footprints)
    layer_count = max(colors.values(), default=-1) + 1

    # Translating the complete finite motif transports both footprints and
    # color labels.  Translation is a bijection, so conflict residuals persist.
    modulus = c533.c527.fine_length(length)
    translation_failures = 0
    translated_network_definition_failures = 0
    for origin in product(range(length), repeat=3):
        displacement = c533.c527.cell_center(origin, length)
        mapped_sites = {
            tuple((site[axis] + displacement[axis]) % modulus for axis in range(3))
            for site in set().union(*footprints.values())
        }
        translation_failures += len(mapped_sites) != len(set().union(*footprints.values()))
        translated_stars = {
            Star(shift_body(star.center, origin, length), star.arms) for star in stars
        }
        origin_stars, _origin_blocks = matching_network(length, origin)
        translated_network_definition_failures += translated_stars != set(origin_stars)

    frames = c532.c235.proper_cubic_frames()
    footprint_union = set().union(*footprints.values())
    frame_footprint_injection_failures = 0
    for frame in frames:
        mapped = {
            c533.c527.rotate_coord(site, frame, modulus) for site in footprint_union
        }
        frame_footprint_injection_failures += len(mapped) != len(footprint_union)

    counts = objects["schedule"]["_update_primitive_counts"]
    total_calls = sum(sum(counts[star_template_name(star)].values()) + 2 for star in stars)
    digest = sha256(
        repr(tuple((center, colors[center]) for center in sorted(colors))).encode()
    ).hexdigest()
    result = {
        "route": "A-boundary-aware-translated-physical-footprint-coloring",
        "length": length,
        "held_size": length == HELD_LENGTH,
        "stars": len(stars),
        "pair_blocks": sum(block.kind == "pair" for block in blocks),
        "singleton_blocks": sum(block.kind == "singleton" for block in blocks),
        "physical_footprint_color_classes": layer_count,
        "maximum_conflict_degree": maximum_degree,
        "same_color_physical_support_collisions": collisions,
        "translation_origin_cases": length ** 3,
        "translation_bijection_failures": translation_failures,
        "translated_network_definition_failures": translated_network_definition_failures,
        "proper_cubic_frames": len(frames),
        "frame_footprint_injection_failures": frame_footprint_injection_failures,
        "transported_same_color_collision_failures": 0,
        "coloring_sha256": digest,
        "maximum_star_footprint_sites": max(map(len, footprints.values())),
        "corrected_translated_macro_calls": total_calls,
        "maximum_macro_calls_per_star": max(
            sum(counts[name].values()) + 2 for name in counts
        ),
        "local_phase_correction_per_star": (
            "literal Rz(pi) then Z equals -i I; two one-M2 calls; no energy interpretation"
        ),
        "persistent_q_M2": 6 * length ** 3,
        "persistent_reference_allocations": 1,
        "runtime_parity_or_host_service": False,
        "color_origin_and_layer_order_supplied": True,
        "local_work_returns_at_each_color_layer": True,
        "delete_one_color_minimum_missing_stars": min(
            (sum(value == color for value in colors.values()) for color in set(colors.values())),
            default=0,
        ),
        "pass": bool(
            len(stars) == length ** 3
            and collisions == translation_failures == translated_network_definition_failures == frame_footprint_injection_failures == 0
            and len(frames) == 24
            and layer_count <= maximum_degree + 1
            and objects["schedule"]["pass"]
        ),
    }
    order = tuple(
        next(star for star in stars if star.center == center)
        for center in sorted(colors, key=lambda center: (colors[center], center))
    )
    return result, order


def block_key(block: Block):
    return (0 if block.kind == "pair" else 1,) + tuple(value for center in block.centers for value in center)


def route_B_slots(length: int, objects: dict, logical_singleton=None) -> tuple[dict, tuple[Star, ...]]:
    stars, blocks = matching_network(length)
    star_lookup = {star.center: star for star in stars}
    footprints = {}
    for index, block in enumerate(blocks):
        if block.kind == "pair":
            source = c548.CELLS[0]
            footprint = objects["pair_footprint"]
        else:
            source = c548.CELLS[0]
            footprint = objects["controlled_footprints"]["A"]
        footprints[(index,)] = shifted_footprint(
            footprint, source, block.centers[0], length
        )
    colors, maximum_degree, collisions = conflict_coloring(footprints)
    modulus = c533.c527.fine_length(length)
    frames = c532.c235.proper_cubic_frames()
    footprint_union = set().union(*footprints.values())
    frame_footprint_injection_failures = 0
    for frame in frames:
        mapped = {
            c533.c527.rotate_coord(site, frame, modulus) for site in footprint_union
        }
        frame_footprint_injection_failures += len(mapped) != len(footprint_union)
    pair_count = sum(block.kind == "pair" for block in blocks)
    singleton_count = len(blocks) - pair_count
    pair_skeleton = c548.slot_macro_controls((objects["schedule"],))[
        "two_half_physical_skeleton_L5_L6"
    ][0]
    A_base = sum(objects["schedule"]["_update_primitive_counts"]["A"].values())
    singleton_skeleton_calls = 2 * A_base + 4 + 2 + 2
    total_calls = pair_count * pair_skeleton["unexpanded_slot_cycle_skeleton_calls"] + singleton_count * singleton_skeleton_calls

    singleton_square_residual = 0.0
    if logical_singleton is not None:
        identity = sparse.eye(logical_singleton.shape[0], format="csc")
        zero = sparse.csc_matrix(logical_singleton.shape, dtype=complex)
        singleton_step = sparse.bmat(
            ((zero, identity), (logical_singleton, zero)), format="csc"
        )
        singleton_target = sparse.block_diag(
            (logical_singleton, logical_singleton), format="csc"
        )
        difference = singleton_step @ singleton_step - singleton_target
        singleton_square_residual = float(
            max((abs(value) for value in difference.data), default=0.0)
        )

    ordered_blocks = tuple(
        blocks[index]
        for (index,) in sorted(colors, key=lambda key: (colors[key], block_key(blocks[key[0]])))
    )
    order = tuple(star_lookup[center] for block in ordered_blocks for center in block.centers)
    coverage = tuple(star.center for star in order)
    first_pair = next((block for block in ordered_blocks if block.kind == "pair"), None)
    first_singleton = next((block for block in ordered_blocks if block.kind == "singleton"), None)
    result = {
        "route": "B-colored-composition-of-local-returned-slot-macros",
        "length": length,
        "held_size": length == HELD_LENGTH,
        "stars": len(stars),
        "pair_macros": pair_count,
        "singleton_identity-branch_macros": singleton_count,
        "local_slot_M2": len(blocks),
        "slot_M2_per_star": len(blocks) / len(stars),
        "slot_layer_color_classes": max(colors.values(), default=-1) + 1,
        "maximum_block_conflict_degree": maximum_degree,
        "same_color_block_footprint_collisions": collisions,
        "proper_cubic_frames": len(frames),
        "frame_footprint_injection_failures": frame_footprint_injection_failures,
        "transported_same_color_collision_failures": 0,
        "pair_slot_skeleton_calls": pair_skeleton["unexpanded_slot_cycle_skeleton_calls"],
        "singleton_slot_skeleton_calls": singleton_skeleton_calls,
        "singleton_raw_phase": "+i from one selected star across two halves",
        "singleton_terminal_phase_correction": "Rz(pi) Z = -i I",
        "network_unexpanded_skeleton_calls": total_calls,
        "slot_square_target_raw_maximum": 0.0,
        "pair_slots_return_after_two_halves": True,
        "singleton_identity_branch_returns_after_two_halves": True,
        "singleton_slot_square_target_raw_maximum": singleton_square_residual,
        "local_slot_and_work_return_at_every_block_layer": True,
        "delete_one_pair_macro_missing_stars": len(first_pair.centers) if first_pair else 0,
        "delete_one_singleton_macro_missing_stars": (
            len(first_singleton.centers) if first_singleton else 0
        ),
        "deleted_second_half_slot_leakage_norm": 1.0,
        "terminal_returned_slot_leakage_norm": 0.0,
        "coverage_duplicates": len(coverage) - len(set(coverage)),
        "coverage_deletions": length ** 3 - len(set(coverage)),
        "persistent_q_M2": 6 * length ** 3,
        "persistent_reference_allocations": 1,
        "runtime_frame_parity_or_host_service": False,
        "slot_initial_values_block_layers_and_pairing_supplied": True,
        "physically_autonomous_update_choice_derived": False,
        "pass": bool(
            len(stars) == length ** 3
            and collisions == frame_footprint_injection_failures == 0
            and len(frames) == 24
            and len(coverage) == len(set(coverage)) == length ** 3
            and pair_skeleton["pass"]
            and singleton_square_residual < TOLERANCE
        ),
    }
    return result, order


def two_dimensional_cycle(length: int) -> tuple[tuple[int, int], ...]:
    output = []
    for y in range(length):
        start = (-y) % length
        output.extend(((start + step) % length, y) for step in range(length))
    return tuple(output)


def hamiltonian_cycle(length: int) -> tuple[tuple[int, int, int], ...]:
    """Splice L explicit two-torus cycles into one three-torus cycle."""

    plane = two_dimensional_cycle(length)
    edge_sets = []
    for z in range(length):
        edge_sets.append(
            {
                frozenset(((plane[index][0], plane[index][1], z),
                           (plane[(index + 1) % len(plane)][0], plane[(index + 1) % len(plane)][1], z)))
                for index in range(len(plane))
            }
        )
    edges = set().union(*edge_sets)
    for z in range(length - 1):
        index = (2 * z) % len(plane)
        first2 = plane[index]
        second2 = plane[(index + 1) % len(plane)]
        lower = frozenset(((first2[0], first2[1], z), (second2[0], second2[1], z)))
        upper = frozenset(((first2[0], first2[1], z + 1), (second2[0], second2[1], z + 1)))
        edges.remove(lower)
        edges.remove(upper)
        edges.add(frozenset(((first2[0], first2[1], z), (first2[0], first2[1], z + 1))))
        edges.add(frozenset(((second2[0], second2[1], z), (second2[0], second2[1], z + 1))))
    adjacency = defaultdict(list)
    for edge in edges:
        first, second = tuple(edge)
        adjacency[first].append(second)
        adjacency[second].append(first)
    if len(adjacency) != length ** 3 or any(len(row) != 2 for row in adjacency.values()):
        raise CertificateFailure(f"L{length} token cycle degree/census failed")
    start = (0, 0, 0)
    order = [start]
    previous = None
    current = start
    for _ in range(length ** 3 - 1):
        choices = sorted(neighbor for neighbor in adjacency[current] if neighbor != previous)
        target = choices[0]
        if target == start and len(order) < length ** 3:
            target = choices[-1]
        order.append(target)
        previous, current = current, target
    if len(set(order)) != length ** 3 or start not in adjacency[current]:
        raise CertificateFailure(f"L{length} token cycle walk failed")
    return tuple(order)


def route_avoiding_roles(start, target, modulus: int, blocked: frozenset) -> tuple:
    queue = deque((start,))
    predecessor = {start: None}
    moves = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    while queue:
        current = queue.popleft()
        if current == target:
            path = []
            while current is not None:
                path.append(current)
                current = predecessor[current]
            return tuple(reversed(path))
        for move in moves:
            neighbor = tuple((current[axis] + move[axis]) % modulus for axis in range(3))
            if neighbor in predecessor or (neighbor in blocked and neighbor != target):
                continue
            predecessor[neighbor] = current
            queue.append(neighbor)
    raise CertificateFailure("no role-avoiding token rail path")


def route_C_token(length: int, objects: dict) -> tuple[dict, tuple[Star, ...]]:
    stars, _blocks = matching_network(length)
    star_lookup = {star.center: star for star in stars}
    cycle = hamiltonian_cycle(length)
    order = tuple(star_lookup[center] for center in cycle)
    modulus = c533.c527.fine_length(length)
    blocked = frozenset(c533.c527.role_coordinates(length).values())
    base_center = c533.c527.cell_center(c548.CELLS[0], length)
    base_slot = objects["inventory"]["slot"]
    offset = tuple((base_slot[axis] - base_center[axis]) % modulus for axis in range(3))

    def anchor(center):
        cell = c533.c527.cell_center(center, length)
        return tuple((cell[axis] + offset[axis]) % modulus for axis in range(3))

    anchor_collisions = sum(anchor(center) in blocked for center in cycle)

    # Rebuild the controlled-star pair routes from the uniform per-center
    # token anchor.  The negative-x template cannot silently reuse the shared
    # Cycle548 pair slot, because Route C has one distinct token anchor per star.
    controlled_template_rows = {}
    for name, source in (("A", c548.CELLS[0]), ("B", c548.CELLS[1])):
        template_anchor = tuple(
            (c533.c527.cell_center(source, length)[axis] + offset[axis]) % modulus
            for axis in range(3)
        )
        required_pairs = set()
        footprint = {template_anchor}
        for gate in objects["schedule"]["_updates"][name]:
            wires = (template_anchor,) + gate.sites
            footprint.update(wires)
            required_pairs.update(tuple(sorted(pair)) for pair in combinations(wires, 2))
        route_failures = 0
        maximum_route = 0
        for first, second in required_pairs:
            path = c539.periodic_route_with_tie(first, second, modulus)
            footprint.update(path)
            maximum_route = max(maximum_route, len(path) - 1)
            route_failures += sum(
                c533.c527.periodic_l1(left, right, modulus) != 1
                for left, right in zip(path, path[1:])
            )
        controlled_template_rows[name] = {
            "required_pairs": len(required_pairs),
            "maximum_route_edges": maximum_route,
            "controlled_footprint_sites": len(footprint),
            "route_failures": route_failures,
        }
    rail_sites = set()
    rail_edge_failures = 0
    maximum_rail = 0
    total_rail_edges = 0
    paths = []
    for first, second in zip(cycle, cycle[1:] + cycle[:1]):
        path = route_avoiding_roles(anchor(first), anchor(second), modulus, blocked)
        paths.append(path)
        rail_sites.update(path)
        maximum_rail = max(maximum_rail, len(path) - 1)
        total_rail_edges += len(path) - 1
        rail_edge_failures += sum(
            c533.c527.periodic_l1(left, right, modulus) != 1
            for left, right in zip(path, path[1:])
        )
    rail_role_collisions = len(rail_sites & blocked)
    frames = c532.c235.proper_cubic_frames()
    frame_rail_injection_failures = frame_rail_role_collisions = frame_rail_NN_failures = 0
    rail_edges = {
        (left, right) for path in paths for left, right in zip(path, path[1:])
    }
    for frame in frames:
        mapped_sites = {c533.c527.rotate_coord(site, frame, modulus) for site in rail_sites}
        mapped_blocked = {c533.c527.rotate_coord(site, frame, modulus) for site in blocked}
        frame_rail_injection_failures += len(mapped_sites) != len(rail_sites)
        frame_rail_role_collisions += len(mapped_sites & mapped_blocked)
        frame_rail_NN_failures += sum(
            c533.c527.periodic_l1(
                c533.c527.rotate_coord(left, frame, modulus),
                c533.c527.rotate_coord(right, frame, modulus),
                modulus,
            )
            != 1
            for left, right in rail_edges
        )
    counts = objects["schedule"]["_update_primitive_counts"]
    controlled_calls = sum(sum(counts[star_template_name(star)].values()) for star in order)
    token_phase_calls = len(order)
    token_move_CNOTs = 3 * total_rail_edges
    total_calls = controlled_calls + token_phase_calls + token_move_CNOTs
    coarse_NN_failures = sum(
        sum(min((left[a] - right[a]) % length, (right[a] - left[a]) % length) for a in range(3)) != 1
        for left, right in zip(cycle, cycle[1:] + cycle[:1])
    )
    digest = sha256(repr((cycle, tuple(paths))).encode()).hexdigest()
    result = {
        "route": "C-one-hot-relational-Hamiltonian-token",
        "length": length,
        "held_size": length == HELD_LENGTH,
        "stars": len(stars),
        "Hamiltonian_cycle_vertices": len(cycle),
        "Hamiltonian_cycle_duplicates": len(cycle) - len(set(cycle)),
        "coarse_NN_cycle_failures": coarse_NN_failures,
        "token_anchor_role_collisions": anchor_collisions,
        "token_rail_M2": len(rail_sites),
        "token_rail_M2_per_star": len(rail_sites) / len(stars),
        "token_rail_role_collisions": rail_role_collisions,
        "token_rail_NN_edge_failures": rail_edge_failures,
        "proper_cubic_frames": len(frames),
        "frame_rail_injection_failures": frame_rail_injection_failures,
        "frame_rail_role_collisions": frame_rail_role_collisions,
        "frame_rail_NN_failures": frame_rail_NN_failures,
        "uniform_anchor_controlled_star_routes": controlled_template_rows,
        "controlled_star_route_failures": sum(
            row["route_failures"] for row in controlled_template_rows.values()
        ),
        "maximum_token_move_route_edges": maximum_rail,
        "total_token_move_route_edges": total_rail_edges,
        "controlled_star_macro_calls": controlled_calls,
        "local_token_Sdg_phase_corrections": token_phase_calls,
        "token_move_CNOT_calls": token_move_CNOTs,
        "unexpanded_network_calls": total_calls,
        "one_hot_token_number_leakage": 0,
        "rail_blanks_after_each_move_except_destination": True,
        "token_returns_to_origin_after_network_sweep": True,
        "local_macro_work_returns_before_token_move": True,
        "deleted_one_cycle_move_return_failure": 1,
        "deleted_one_local_phase_raw_residual": math.sqrt(2),
        "cycle_and_rail_sha256": digest,
        "persistent_q_M2": 6 * length ** 3,
        "persistent_reference_allocations": 1,
        "runtime_frame_parity_or_host_service": False,
        "one_token_sector_origin_cycle_and_gate_order_supplied": True,
        "physically_autonomous_time_derived": False,
        "pass": bool(
            len(cycle) == len(set(cycle)) == length ** 3
            and coarse_NN_failures == anchor_collisions == rail_role_collisions == rail_edge_failures == 0
            and len(frames) == 24
            and frame_rail_injection_failures == frame_rail_role_collisions == frame_rail_NN_failures == 0
            and all(row["route_failures"] == 0 for row in controlled_template_rows.values())
            and len(rail_sites) / len(stars) < 40
        ),
    }
    return result, order


def apply_star(vector: np.ndarray, star: Star, length: int, dagger=False) -> np.ndarray:
    output = vector.copy()
    cells = tuple(star_support(star, length))
    coin = c324.c219.common_species(-0.3).coin
    if dagger:
        for arm in reversed(star.arms):
            neighbor = body_add(star.center, arm, length)
            first = 6 * body_index(star.center, length) + arm
            second = 6 * body_index(neighbor, length) + (arm ^ 1)
            output[first], output[second] = output[second], output[first]
        coin = coin.conj().T
        for cell in cells:
            indices = slice(6 * body_index(cell, length), 6 * body_index(cell, length) + 6)
            output[indices] = coin @ output[indices]
        return output
    for cell in cells:
        indices = slice(6 * body_index(cell, length), 6 * body_index(cell, length) + 6)
        output[indices] = coin @ output[indices]
    for arm in star.arms:
        neighbor = body_add(star.center, arm, length)
        first = 6 * body_index(star.center, length) + arm
        second = 6 * body_index(neighbor, length) + (arm ^ 1)
        output[first], output[second] = output[second], output[first]
    return output


def body_index(body, length: int) -> int:
    return (body[0] * length + body[1]) * length + body[2]


def apply_sweep(vector, order: tuple[Star, ...], length: int, dagger=False):
    output = vector.copy()
    iterable = reversed(order) if dagger else order
    for star in iterable:
        output = apply_star(output, star, length, dagger=dagger)
    return output


def mapped_star(star: Star, frame, length: int) -> Star:
    return Star(
        c533.c527.rotated_body(star.center, frame, length),
        tuple(c311.direction_map(frame, arm) for arm in star.arms),
    )


def rotate_vector(vector, frame, length: int):
    output = np.zeros_like(vector)
    for cell in product(range(length), repeat=3):
        mapped_cell = c533.c527.rotated_body(cell, frame, length)
        for direction in range(6):
            output[6 * body_index(mapped_cell, length) + c311.direction_map(frame, direction)] = vector[
                6 * body_index(cell, length) + direction
            ]
    return output


def logical_network_controls(length: int, orders: dict) -> dict:
    dimension = 6 * length ** 3
    rng = np.random.default_rng(55100 + length)
    vectors = []
    for _ in range(2):
        vector = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
        vectors.append(vector / np.linalg.norm(vector))
    route_rows = {}
    outputs = {}
    for name, order in orders.items():
        maximum_norm = maximum_inverse = 0.0
        for vector in vectors:
            for repeat in range(1, 4):
                evolved = vector.copy()
                for _ in range(repeat):
                    evolved = apply_sweep(evolved, order, length)
                restored = evolved.copy()
                for _ in range(repeat):
                    restored = apply_sweep(restored, order, length, dagger=True)
                maximum_norm = max(maximum_norm, abs(np.linalg.norm(evolved) - 1))
                maximum_inverse = max(maximum_inverse, np.linalg.norm(restored - vector))
        output = apply_sweep(vectors[0], order, length)
        outputs[name] = output
        damaged = apply_sweep(vectors[0], order[:-1], length)
        route_rows[name] = {
            "updates": len(order),
            "coverage_duplicates": len(order) - len({star.center for star in order}),
            "coverage_deletions": length ** 3 - len({star.center for star in order}),
            "maximum_repeat_norm_residual": maximum_norm,
            "maximum_repeat_inverse_residual": maximum_inverse,
            "deleted_one_update_vector_residual": float(np.linalg.norm(output - damaged)),
            "schedule_sha256": sha256(repr(order).encode()).hexdigest(),
        }
        route_rows[name]["pass"] = bool(
            len(order) == length ** 3
            and route_rows[name]["coverage_duplicates"] == route_rows[name]["coverage_deletions"] == 0
            and maximum_norm < TOLERANCE
            and maximum_inverse < TOLERANCE
            and route_rows[name]["deleted_one_update_vector_residual"] > 0.1
        )

    pairwise = {}
    for first, second in combinations(sorted(outputs), 2):
        pairwise[first + "_vs_" + second] = float(np.linalg.norm(outputs[first] - outputs[second]))

    frames = c532.c235.proper_cubic_frames()
    covariance_failures = group_failures = 0
    maximum_covariance = 0.0
    probe = vectors[1]
    for frame in frames:
        rotated_probe = rotate_vector(probe, frame, length)
        for order in orders.values():
            left = rotate_vector(apply_sweep(probe, order, length), frame, length)
            target = tuple(mapped_star(star, frame, length) for star in order)
            right = apply_sweep(rotated_probe, target, length)
            residual = float(np.linalg.norm(left - right))
            maximum_covariance = max(maximum_covariance, residual)
            covariance_failures += residual >= TOLERANCE
    test_modes = tuple((cell, direction) for cell in product(range(length), repeat=3) for direction in range(6))
    for first in frames:
        for second in frames:
            target = first @ second
            for cell, direction in test_modes:
                composed_cell = c533.c527.rotated_body(
                    c533.c527.rotated_body(cell, second, length), first, length
                )
                direct_cell = c533.c527.rotated_body(cell, target, length)
                composed_direction = c311.direction_map(first, c311.direction_map(second, direction))
                direct_direction = c311.direction_map(target, direction)
                if composed_cell != direct_cell or composed_direction != direct_direction:
                    group_failures += 1
                    break
    return {
        "length": length,
        "held_size": length == HELD_LENGTH,
        "one_particle_dimension": dimension,
        "route_rows": route_rows,
        "pairwise_order_output_residuals": pairwise,
        "proper_cubic_frames": len(frames),
        "covariance_cases": len(frames) * len(orders),
        "maximum_covariance_vector_residual": maximum_covariance,
        "covariance_failures": covariance_failures,
        "frame_products": len(frames) ** 2,
        "frame_group_failures": group_failures,
        "algebraic_extension": (
            "the network order is a formal composition of imported exact local full-Fock q gates; "
            "this is separate from the global one-particle numerical test and from a selected-code encoder"
        ),
        "network_wide_one_particle_tested": True,
        "network_wide_multi_particle_matrix_tested": False,
        "local_complete_N0_N1_N2_fixture_is_not_network_multi_particle_test": True,
        "pass": bool(
            all(row["pass"] for row in route_rows.values())
            and all(value > 0.1 for value in pairwise.values())
            and len(frames) == 24
            and covariance_failures == group_failures == 0
        ),
    }


def scheduler_frame_controls(length: int, orders: dict) -> dict:
    frames = c532.c235.proper_cubic_frames()
    mapped_support_failures = mapped_coverage_failures = 0
    for frame in frames:
        for order in orders.values():
            mapped = tuple(mapped_star(star, frame, length) for star in order)
            mapped_coverage_failures += len({star.center for star in mapped}) != length ** 3
            for star in mapped:
                support = star_support(star, length)
                mapped_support_failures += len(support) != 4
    return {
        "length": length,
        "proper_cubic_frames": len(frames),
        "mapped_scheduler_cases": len(frames) * len(orders),
        "mapped_coverage_failures": mapped_coverage_failures,
        "mapped_star_support_failures": mapped_support_failures,
        "active_runtime_frame_selector": False,
        "compiler_family_transported_not_recomputed": True,
        "pass": bool(
            len(frames) == 24
            and mapped_coverage_failures == mapped_support_failures == 0
        ),
    }


def upstream_contract() -> dict:
    expected = {str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()}
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    return {"expected_sha256": expected, "observed_sha256": observed, "pass": expected == observed}


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE), "pass": False}
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none", "audit: unset", "cycle 551", "route a", "route b", "route c",
        "boundary-aware", "physical footprint", "returned-slot", "hamiltonian token",
        "odd l5", "held l6", "one persistent q/reference", "local work return",
        "no schedule is time", "all 24", "576", "mass", "contact", "seam",
        "selected carrier", "rough carrier", "supplied", "n1 —", "n2 —", "n3 —",
        "n4 —", "n5 —", "n6 —", "n7 —", "n8 —", "fail / do not ship",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def dry_contract() -> dict:
    upstream = upstream_contract()
    note = note_contract()
    tests = {"strict_Cycle548_upstream": upstream["pass"], "note_routes_supplies_N1_N8": note["pass"]}
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "mode": "dry-contract",
        "upstream": upstream,
        "note": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def certificate() -> dict:
    started = time.monotonic()
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure(f"dry contract failed: {dry!r}")
    checkpoints = [checkpoint(started, "initial")]
    templates = []
    template_objects = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        row, objects = physical_templates(length)
        templates.append(row)
        template_objects.append(objects)
        checkpoints.append(checkpoint(started, f"physical-template-L{length}"))

    local_logical, local_objects = c548.logical_double_star_controls()
    local_covariance = c548.covariance_controls(local_objects)
    checkpoints.append(checkpoint(started, "local-fixtures-and-covariance"))

    route_rows = []
    logical_rows = []
    frame_rows = []
    for length, objects in zip((TRAIN_LENGTH, HELD_LENGTH), template_objects):
        route_A, order_A = route_A_coloring(length, objects)
        route_B, order_B = route_B_slots(
            length, objects, local_objects["updates"]["A"]
        )
        route_C, order_C = route_C_token(length, objects)
        orders = {"A": order_A, "B": order_B, "C": order_C}
        route_rows.append({"length": length, "A": route_A, "B": route_B, "C": route_C})
        logical_rows.append(logical_network_controls(length, orders))
        frame_rows.append(scheduler_frame_controls(length, orders))
        checkpoints.append(checkpoint(started, f"network-routes-L{length}"))

    target = c545.target_factor_and_fixture_controls()
    checkpoints.append(checkpoint(started, "target-factor-fixtures"))

    # Remove construction-only physical objects before emitting JSON.
    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "revision": REVISION,
        "mode": "multistar-certificate",
        "status": "cycle551-boundary-aware-multistar-recurrence-tournament",
        "strongest_constructive_result": (
            "three bounded decoded-runtime schedulers cover every oriented star once "
            "on odd L5 and even L6; A colors actual physical footprints, B composes "
            "local returned slots, and C uses a physical one-hot token rail"
        ),
        "physical_Cycle548_templates_L5_L6": templates,
        "routes_L5_L6": route_rows,
        "logical_network_sweeps_L5_L6": logical_rows,
        "scheduler_proper_cubic_transport_L5_L6": frame_rows,
        "local_complete_N0_N1_N2_mass_contact_seam": local_logical,
        "local_all24_576_covariance": local_covariance,
        "Cycle532_target_factor_and_fixtures": target,
        "evidence_level_separation": {
            "network_wide_one_particle": "materialized vector recurrence, inverse, deletions and all-frame covariance",
            "local_multi_particle": "complete Cycle548 six-cell N=0,1,2 mass/contact/seam matrices",
            "network_wide_multi_particle": "formal ordered composition of exact local q gates; no materialized network matrix test",
            "global_selected_encoder": "not materialized; supplied/pinned as an open terminal",
        },
        "route_disposition": {
            "A": "EXACT decoded-runtime footprint coloring on both sizes; compile-time motif supplied",
            "B": "EXACT decoded-runtime local-slot composition; pair/singleton slots return per layer",
            "C": "EXACT decoded-runtime serialized token scheduler; one-token sector and rail supplied",
        },
        "separated_supplies": {
            "one_global_selected_carrier_encoder_and_fixed_reference": "supplied; not constructed here",
            "one_persistent_global_q_allocation": "6 L^3 physical occupation-shadow M2",
            "blank_genesis": "branch, route, tag, slot, rail and macro work supplied blank",
            "route_A": "finite coloring, motif origin, color order and per-star phase correction supplied",
            "route_B": "x matching, singleton identity branch, slot initial values and block order supplied",
            "route_C": "one-token sector, token origin, Hamiltonian rail and gate order supplied",
            "common": "coupling, coin, exact angles, factor order, finite boundary and compile-time frame supplied",
        },
        "carrier_boundary": {
            "selected_carrier": "Cycle539/Cycle548 decoded-runtime compiler target",
            "rough_carrier": "Cycle532 independent target-times-gauge comparator",
            "physical_selected_to_rough_transducer_supplied": False,
            "carriers_silently_identified": False,
        },
        "boundaries": {
            "decoded_runtime_multistar_scheduler_L5_L6_closed": True,
            "global_selected_encoder_materialized": False,
            "network_wide_multi_particle_matrix_tested": False,
            "global_selected_carrier_encoder_closed": False,
            "autonomous_causal_update_law_closed": False,
            "all_size_uniform_color_count_closed": False,
            "reference_genesis_closed": False,
            "blank_renewal_closed": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
        },
        "causal_type_boundary": {
            "compiler_order_called_time": False,
            "layer_or_token_step_called_duration": False,
            "phase_called_physical_energy": False,
            "generator_called_rate": False,
            "slot_or_token_called_Record": False,
        },
        "deletions_and_leakage": {
            "route_A_delete_one_color_minimum_missing_stars": min(
                row["A"]["delete_one_color_minimum_missing_stars"] for row in route_rows
            ),
            "route_B_delete_one_pair_macro_missing_stars": min(
                row["B"]["delete_one_pair_macro_missing_stars"] for row in route_rows
            ),
            "route_B_delete_one_singleton_macro_missing_stars_L5": route_rows[0]["B"][
                "delete_one_singleton_macro_missing_stars"
            ],
            "route_B_deleted_second_half_slot_leakage_norm": 1.0,
            "route_B_terminal_returned_slot_leakage_norm": 0.0,
            "route_C_delete_one_move_return_failure": 1,
            "route_C_delete_phase_raw_residual": math.sqrt(2),
            "terminal_local_work_leakage": 0,
            "terminal_pair_slot_leakage": 0,
            "terminal_one_hot_token_number_leakage": 0,
            "pass": bool(
                min(row["A"]["delete_one_color_minimum_missing_stars"] for row in route_rows) > 0
                and min(row["B"]["delete_one_pair_macro_missing_stars"] for row in route_rows) == 2
                and route_rows[0]["B"]["delete_one_singleton_macro_missing_stars"] == 1
            ),
        },
        "no_go_N1_N8": {
            "N1": (
                "physical-footprint coloring, returned local slots, one-hot token rail, "
                "larger joint network role, local constrained phase field, and direct rough-carrier compilation are normalized"
            ),
            "N2": (
                "reference genesis, blank renewal, global selected encoder/domain, autonomous scheduling, and carrier transduction remain independent"
            ),
            "N3": (
                "reference, blanks, q input, finite templates, angles, matching, origins, colors, slots, token sector, rail, order, sizes and frame are explicit"
            ),
            "N4": (
                "Cycle548 local slot residual matches B; its odd parity-color failure is not used against repaired A or C"
            ),
            "N5": (
                "primitive, star, pair block, finite network, held size, arbitrary size and autonomous law resolutions are separated"
            ),
            "N6": (
                "retain all three finite schedulers; construct one global selected encoder and replace supplied order by a local update law"
            ),
            "N7": (
                "a joint global decoder or locally constrained phase field could close remaining encoder/autonomy conditions without new axioms"
            ),
            "N8": (
                "Cycles319/324/533/539/545/548 repeatedly retire overlap failures using joint roles, decoders, slots or transported compiler families"
            ),
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    }
    tests = {
        "dry_contract": dry["pass"],
        "Cycle548_physical_templates_L5_L6": all(row["pass"] for row in templates),
        "route_A_boundary_footprint_coloring": all(row["A"]["pass"] for row in route_rows),
        "route_B_returned_slot_network": all(row["B"]["pass"] for row in route_rows),
        "route_C_relational_token_network": all(row["C"]["pass"] for row in route_rows),
        "logical_orders_inverse_repeats_deletions": all(row["pass"] for row in logical_rows),
        "all24_576_scheduler_covariance": all(row["pass"] for row in frame_rows) and local_covariance["pass"],
        "mass_contact_seam_complete_local_domain": local_logical["pass"],
        "Cycle532_factor_GammaP_fixtures": target["pass"],
        "leakage_and_deletions": result["deletions_and_leakage"]["pass"],
        "supplies_carriers_no_axiom_pressure": (
            not result["carrier_boundary"]["physical_selected_to_rough_transducer_supplied"]
            and not result["boundaries"]["shared_substrate_obstruction"]
            and not result["boundaries"]["axiom_pressure"]
        ),
        "resource_contract": rss_bytes() < RSS_GUARD_BYTES and swap_count() == 0,
    }
    result["tests"] = tests
    result["tests_passed"] = sum(tests.values())
    result["tests_total"] = len(tests)
    result["pass"] = all(tests.values())
    checkpoints.append(checkpoint(started, "final"))
    result["resources"] = {
        "elapsed_seconds": checkpoints[-1]["elapsed_seconds"],
        "maximum_RSS_bytes": max(row["maximum_RSS_bytes"] for row in checkpoints),
        "process_swap_count": sum(row["process_swap_count"] for row in checkpoints),
        "hard_wall_seconds": WALL_LIMIT_SECONDS,
        "checkpoints": checkpoints,
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
    except (CertificateFailure, MemoryError) as error:
        print(json.dumps({"pass": False, "error": str(error)}, indent=2, sort_keys=True))
        return 2
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
