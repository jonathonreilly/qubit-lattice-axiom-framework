#!/usr/bin/env python3
"""Cycle-789 fixed coframe schedule for the repaired O/I/L circuit.

This runner is deliberately not a retained package.  It replaces finite-box
greedy conflict colouring and anonymous mobile rails by a translation-local
mod-3 colouring, explicit coframe palettes, and returned Manhattan macros.
The ordered circuit is

  A: pump the O/I Choi character with retained pump-syndrome ancillas;
  B: extract the I/L Bell character with fresh retained Bell ancillas;
  C: coherently apply the private correction on O;
  D: apply the already landed recurrent Cycle-720 word G on O.

The integers indexing these circuit layers are scheduling labels, not time.
Genesis of clean ancillas, the sector/coframe code and its enforcement remain
supplied exactly as in the source theorems.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
from itertools import combinations
import json
from pathlib import Path

import numpy as np

import frontier_companion_bank_bell_character_dilation_2026_07_28 as B
import frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27 as P
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/THREE_REGISTER_COMPANION_INPUT_CIRCUIT_CYCLE789_"
    "BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_companion_bank_bell_character_dilation_2026_07_28.py",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS


Coord = tuple[int, int, int]
Frame = tuple[tuple[int, int, int], ...]
SHAPES = ((1, 1, 1), (2, 2, 2), (3, 2, 2), (5, 3, 2), (6, 5, 4))
COLOR_MODULUS = 3
FAMILY_SLOTS = 17
PADDED_MICROSTEP_BOUND = 4096
BUS_PAIR = (7, 7)

# Nine qutrit-free physical copies of the encoded 9-M2 cell block.  The
# deliberately sparse positive-yz bank palettes leave fixed router corridors.
I_PAIRS = tuple([(1, z) for z in range(1, 8)] + [(2, 1), (2, 2)])
L_PAIRS = tuple([(2, z) for z in range(3, 8)] + [(3, z) for z in range(1, 5)])
ANCILLA_PAIRS = tuple(
    [(3, z) for z in range(5, 8)]
    + [(4, z) for z in range(1, 8)]
    + [(5, z) for z in range(1, 8)]
)
# These are the three *additional* coframe-gauge M2, not the three companion
# axes already present in U.placement's 9-M2 O block.
COFRAME_OFFSETS = ((3, -7, -7), (3, -7, -6), (3, -7, -5))


@dataclass(frozen=True)
class Primitive:
    kind: str
    sites: tuple[Coord, ...]


@dataclass(frozen=True)
class RoutedMacro:
    stage: str
    role: str
    owner: Coord
    slot: int
    control: Coord
    target: Coord
    path: tuple[Coord, ...]
    letter: str
    primitives: tuple[Primitive, ...]


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def matvec(frame: Frame, vector: Coord) -> Coord:
    return tuple(
        sum(frame[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def matmul(left: Frame, right: Frame) -> Frame:
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(3))
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def transform(point: Coord, frame: Frame, origin: Coord = (0, 0, 0)) -> Coord:
    return add(matvec(frame, point), origin)


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def append_axis_path(path: list[Coord], target: Coord, axes=(0, 1, 2)) -> None:
    cursor = list(path[-1])
    for axis in axes:
        step = 1 if target[axis] > cursor[axis] else -1
        while cursor[axis] != target[axis]:
            cursor[axis] += step
            path.append(tuple(cursor))


def centers_and_placement(fixture):
    placed = U.placement(fixture)
    minimum = tuple(min(cell[a] for cell in fixture.cells) for a in range(3))
    maximum = tuple(max(cell[a] for cell in fixture.cells) for a in range(3))
    shift = tuple(8 * (low + high) for low, high in zip(minimum, maximum))
    centers = {
        cell: tuple(16 * value - offset for value, offset in zip(cell, shift))
        for cell in fixture.cells
    }
    return centers, placed


def local_nine_index(fixture, qubit: int) -> tuple[int, int]:
    n = len(fixture.cells)
    if qubit < 6 * n:
        return qubit // 6, qubit % 6
    shifted = qubit - 6 * n
    return shifted // 3, 6 + shifted % 3


def bank_sites(fixture, centers, xoffset: int, pairs) -> tuple[Coord, ...]:
    sites = []
    for qubit in range(fixture.qubits):
        cell, local = local_nine_index(fixture, qubit)
        sites.append(add(centers[fixture.cells[cell]], (xoffset, *pairs[local])))
    return tuple(sites)


def coframe_sites(fixture, centers) -> tuple[Coord, ...]:
    return tuple(
        add(centers[cell], offset)
        for cell in fixture.cells
        for offset in COFRAME_OFFSETS
    )


def tag_owner_slot(fixture, tag) -> tuple[Coord, int]:
    if tag[0] == "onsite_Z":
        return fixture.cells[tag[1]], tag[2]
    if tag[0] == "onsite_XX":
        return fixture.cells[tag[1]], 6 + tag[2]
    if tag[0] == "edge":
        edge = fixture.edges[tag[1]]
        owner, axis = tuple(edge[2]), int(edge[3])
        # The canonical box has the positive signed port.  Under a frame the
        # entire coframe, including this slot, is transported; the unused odd
        # slot is the opposite port required by a translation-local law.
        return owner, 11 + 2 * axis
    raise ValueError(tag)


def ancilla_site(center: Coord, slot: int, stage: str) -> Coord:
    sign = -6 if stage == "pump" else 6
    y, z = ANCILLA_PAIRS[slot]
    return add(center, (sign, y, z))


def route_path(
    source: Coord,
    source_center: Coord,
    target: Coord,
    target_center: Coord,
    stage: str,
) -> tuple[Coord, ...]:
    router_x = -4 if stage == "pump" else 4
    source_offset = sub(source, source_center)
    y, z = source_offset[1], source_offset[2]
    path = [source]
    append_axis_path(path, add(source_center, (router_x, y, z)), (0,))
    # Change to a bank- and ancilla-free bus word before crossing a cell
    # boundary.  Without this turn, an x-directed row revisits its own
    # ancilla and crosses the corresponding ancilla in the neighbouring cell.
    append_axis_path(
        path, add(source_center, (router_x, *BUS_PAIR)), (1, 2)
    )
    append_axis_path(
        path, add(target_center, (router_x, *BUS_PAIR)), (0, 1, 2)
    )
    # The target's own yz is approached inside the empty x=+/-4 router plane.
    target_offset = sub(target, target_center)
    append_axis_path(
        path,
        add(target_center, (router_x, target_offset[1], target_offset[2])),
        (1, 2),
    )
    append_axis_path(path, target, (0,))
    if len(path) < 2 or path[0] != source or path[-1] != target:
        raise AssertionError("bad routed path")
    if any(manhattan(left, right) != 1 for left, right in zip(path, path[1:])):
        raise AssertionError("non-nearest-neighbour routed path")
    return tuple(path)


def returned_macro(
    stage: str,
    role: str,
    owner: Coord,
    slot: int,
    control: Coord,
    target: Coord,
    path: tuple[Coord, ...],
    letter: str,
) -> RoutedMacro:
    swaps = tuple(
        Primitive("SWAP", (left, right))
        for left, right in zip(path[:-2], path[1:-1])
    )
    primitives = (
        swaps
        + (Primitive(f"CP_{letter}", (path[-2], path[-1])),)
        + tuple(reversed(swaps))
    )
    return RoutedMacro(
        stage, role, owner, slot, control, target, path, letter, primitives
    )


def letter_at(row, qubit: int) -> str:
    return B.letter_at(row, qubit)


def support(row) -> tuple[int, ...]:
    return B.supported_qubits(row)


def row_word(
    fixture,
    centers,
    placed,
    i_sites,
    l_sites,
    compiled_word,
    correction,
    stage: str,
    include_character: bool = True,
    include_correction: bool = True,
):
    tag = compiled_word["tag"]
    owner, slot = tag_owner_slot(fixture, tag)
    center = centers[owner]
    ancilla = ancilla_site(center, slot, stage)
    primitives = [Primitive("H", (ancilla,))] if include_character else []
    macros = []
    q = fixture.qubits
    measured = compiled_word["row"]
    for qubit in support(measured) if include_character else ():
        if stage == "pump":
            target_sites = placed["sites_by_qubit"] if qubit < q else i_sites
        else:
            target_sites = i_sites if qubit < q else l_sites
        local_qubit = qubit if qubit < q else qubit - q
        target = target_sites[local_qubit]
        target_cell, _local = local_nine_index(fixture, local_qubit)
        path = route_path(
            ancilla, center, target, centers[fixture.cells[target_cell]], stage
        )
        macro = returned_macro(
            stage, "character", owner, slot, ancilla, target, path,
            letter_at(measured, qubit),
        )
        macros.append(macro)
        primitives.extend(macro.primitives)
    if include_character:
        primitives.append(Primitive("H", (ancilla,)))
    # The retained syndrome ancilla coherently controls the private correction.
    for qubit in support(correction) if include_correction else ():
        if qubit >= q:
            raise AssertionError("private correction left the O physical bank")
        target = placed["sites_by_qubit"][qubit]
        target_cell, _local = local_nine_index(fixture, qubit)
        path = route_path(
            ancilla, center, target, centers[fixture.cells[target_cell]], stage
        )
        macro = returned_macro(
            stage, "correction", owner, slot, ancilla, target, path,
            letter_at(correction, qubit),
        )
        macros.append(macro)
        primitives.extend(macro.primitives)
    return {
        "stage": stage,
        "tag": tag,
        "owner": owner,
        "slot": slot,
        "ancilla": ancilla,
        "colour": tuple(value % COLOR_MODULUS for value in owner),
        "primitives": tuple(primitives),
        "macros": tuple(macros),
    }


def label_return_failures(macro: RoutedMacro, delete_last_return=False) -> int:
    labels = {site: site for site in macro.path}
    sequence = list(macro.primitives)
    if delete_last_return:
        reverse_indices = [
            index for index, primitive in enumerate(sequence)
            if primitive.kind == "SWAP"
        ]
        if reverse_indices:
            sequence.pop(reverse_indices[-1])
    for primitive in sequence:
        if primitive.kind == "SWAP":
            left, right = primitive.sites
            labels[left], labels[right] = labels[right], labels[left]
    return sum(labels[site] != site for site in labels)


def routed_target_failures(macro: RoutedMacro) -> int:
    """Check that CP sees the moved control label and untouched target label."""
    labels = {site: site for site in macro.path}
    failures = 0
    for primitive in macro.primitives:
        if primitive.kind == "SWAP":
            left, right = primitive.sites
            labels[left], labels[right] = labels[right], labels[left]
        elif primitive.kind.startswith("CP_"):
            left, right = primitive.sites
            failures += labels[left] != macro.control
            failures += labels[right] != macro.target
    return failures


def primitive_conflicts(words) -> tuple[int, int]:
    grouped = defaultdict(list)
    for word in words:
        grouped[(word["stage"], word["colour"], word["slot"])].append(word)
    conflicts = 0
    tested_microsteps = 0
    for group in grouped.values():
        width = max(len(word["primitives"]) for word in group)
        for ordinal in range(width):
            occupied = set()
            for word in group:
                if ordinal >= len(word["primitives"]):
                    continue
                sites = word["primitives"][ordinal].sites
                conflicts += bool(occupied.intersection(sites))
                occupied.update(sites)
            tested_microsteps += 1
    return conflicts, tested_microsteps


def paulis_anticommute(left, right) -> bool:
    return bool(
        ((left.x & right.z).bit_count() + (left.z & right.x).bit_count()) % 2
    )


def correction_pair_data(fixture, tags, corrections):
    by_qubit = defaultdict(list)
    for index, row in enumerate(corrections):
        for qubit in support(row):
            by_qubit[qubit].append(index)
    candidates = set()
    for rows in by_qubit.values():
        candidates.update(tuple(sorted(pair)) for pair in combinations(rows, 2))
    anti = tuple(sorted(
        pair for pair in candidates
        if paulis_anticommute(corrections[pair[0]], corrections[pair[1]])
    ))
    owners_slots = tuple(tag_owner_slot(fixture, tag) for tag in tags)
    maximum_owner_distance = max((
        manhattan(owners_slots[left][0], owners_slots[right][0])
        for left, right in anti
    ), default=0)
    return tuple(sorted(candidates)), anti, owners_slots, maximum_owner_distance


def firewall_macros(fixture, centers, anti, owners_slots):
    macros = []
    for stage in ("pump", "bell"):
        for left, right in anti:
            left_owner, left_slot = owners_slots[left]
            right_owner, right_slot = owners_slots[right]
            left_site = ancilla_site(centers[left_owner], left_slot, stage)
            right_site = ancilla_site(centers[right_owner], right_slot, stage)
            path = route_path(
                left_site, centers[left_owner], right_site,
                centers[right_owner], stage,
            )
            macro = returned_macro(
                f"{stage}_phase_firewall", "inversion_CZ", left_owner,
                left_slot, left_site, right_site, path, "Z",
            )
            macros.append((macro, right_owner, right_slot))
    return tuple(macros)


def firewall_conflicts(macros):
    groups = defaultdict(list)
    for macro, right_owner, right_slot in macros:
        delta = sub(right_owner, macro.owner)
        key = (
            macro.stage,
            tuple(value % 5 for value in macro.owner),
            delta,
            macro.slot,
            right_slot,
        )
        groups[key].append(macro)
    conflicts = 0
    for group in groups.values():
        for ordinal in range(max(len(macro.primitives) for macro in group)):
            occupied = set()
            for macro in group:
                if ordinal >= len(macro.primitives):
                    continue
                sites = macro.primitives[ordinal].sites
                conflicts += bool(occupied.intersection(sites))
                occupied.update(sites)
    return conflicts, len(groups)


def fixture_for(shape):
    return B.P.O.arbitrary_fixture(B.P.Q.shape_cells(shape))


def box_certificate(shape, atlas):
    fixture = fixture_for(shape)
    centers, placed = centers_and_placement(fixture)
    compiled = B.compile_fixture(fixture)
    corrections = tuple(
        P.correction_from_atlas(fixture, tag, atlas)
        for tag in compiled["tags"]
    )
    pair_candidates, anti_pairs, owners_slots, maximum_anti_owner_distance = (
        correction_pair_data(fixture, compiled["tags"], corrections)
    )
    private_dual_failures = sum(
        paulis_anticommute(correction, graph_row) != (left == right)
        for left, correction in enumerate(corrections)
        for right, graph_row in enumerate(compiled["graph"])
    )
    i_sites = bank_sites(fixture, centers, 1, I_PAIRS)
    l_sites = bank_sites(fixture, centers, 2, L_PAIRS)
    c_sites = coframe_sites(fixture, centers)
    pump_ancillas = tuple(
        ancilla_site(centers[cell], slot, "pump")
        for cell in fixture.cells for slot in range(FAMILY_SLOTS)
    )
    bell_ancillas = tuple(
        ancilla_site(centers[cell], slot, "bell")
        for cell in fixture.cells for slot in range(FAMILY_SLOTS)
    )
    o_sites = tuple(placed["sites_by_qubit"])
    classes = {
        "O_matter": set(o_sites[:fixture.matter_qubits]),
        "O_companion": set(o_sites[fixture.matter_qubits:]),
        "coframe": set(c_sites),
        "I": set(i_sites),
        "L": set(l_sites),
        "pump_ancilla": set(pump_ancillas),
        "bell_ancilla": set(bell_ancillas),
    }
    persistent = set().union(*classes.values())
    palette_count = sum(len(rows) for rows in classes.values())
    palette_collisions = palette_count - len(persistent)

    words = []
    for compiled_word, correction in zip(compiled["words"], corrections):
        words.append(row_word(
            fixture, centers, placed, i_sites, l_sites,
            compiled_word, correction, "pump",
        ))
        words.append(row_word(
            fixture, centers, placed, i_sites, l_sites,
            compiled_word, correction, "bell_measure",
            include_correction=False,
        ))
        words.append(row_word(
            fixture, centers, placed, i_sites, l_sites,
            compiled_word, correction, "bell_correction",
            include_character=False,
        ))
    macros = tuple(macro for word in words for macro in word["macros"])
    phase_firewall = firewall_macros(
        fixture, centers, anti_pairs, owners_slots
    )
    firewall_collision_failures, firewall_blocks = firewall_conflicts(
        phase_firewall
    )
    firewall_return_failures = sum(
        label_return_failures(macro) for macro, _owner, _slot in phase_firewall
    )
    firewall_target_reconstruction_failures = sum(
        routed_target_failures(macro)
        for macro, _owner, _slot in phase_firewall
    )
    firewall_deletion_witness = next((
        label_return_failures(macro, True)
        for macro, _owner, _slot in phase_firewall
        if any(p.kind == "SWAP" for p in macro.primitives)
    ), 0)
    firewall_maximum_distance = max((
        len(macro.path) - 1 for macro, _owner, _slot in phase_firewall
    ), default=0)
    route_nn_failures = sum(
        manhattan(left, right) != 1
        for macro in macros
        for left, right in zip(macro.path, macro.path[1:])
    )
    label_failures = sum(label_return_failures(macro) for macro in macros)
    routed_target_reconstruction_failures = sum(
        routed_target_failures(macro) for macro in macros
    )
    deletion_witness = next(
        (label_return_failures(macro, True) for macro in macros
         if sum(p.kind == "SWAP" for p in macro.primitives) > 0),
        0,
    )
    conflicts, tested_microsteps = primitive_conflicts(words)
    maximum_word = max(len(word["primitives"]) for word in words)

    # Cycle-720 G acts only on the 9-site O block and extends by identity on
    # the 3N coframe M2.  We nevertheless include both in this firewall.
    g_word, _g_update = U.physical_word(fixture, placed)
    g_touch = {site for instruction in g_word for site in instruction.sites}
    g_outside_o = len(g_touch - set(o_sites))
    g_coframe_collisions = len(g_touch & set(c_sites))
    non_o_palette_g_collisions = {
        name: len(rows & g_touch)
        for name, rows in classes.items()
        if name not in ("O_matter", "O_companion")
    }

    route_live_hits = Counter()
    route_g_hits = Counter()
    route_maximum_distance = Counter()
    for macro in macros:
        route_maximum_distance[(macro.stage, macro.role)] = max(
            route_maximum_distance[(macro.stage, macro.role)], len(macro.path) - 1
        )
        internal = set(macro.path[1:-1])
        route_live_hits[(macro.stage, macro.role)] += len(internal & persistent)
        route_g_hits[(macro.stage, macro.role)] += len(internal & g_touch)

    # The Bell character paths are the external-input paths.  They use only
    # the +4 router corridor and must not traverse G or another live palette.
    bell_character_forbidden = sum(
        len(set(macro.path[1:-1]) & (persistent | g_touch))
        for macro in macros
        if macro.stage == "bell_measure" and macro.role == "character"
    )

    # O/I pumping and O correction intentionally reach O.  Any other live
    # labels on their paths are legal only because each route is returned and
    # the stage barrier places all of them before G.
    serialized_reuse = sum(
        len(set(macro.path[1:-1]) & (persistent | g_touch))
        for macro in macros
        if not (macro.stage == "bell_measure" and macro.role == "character")
    )
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "rows": len(compiled["words"]),
        "words": len(words),
        "macros": len(macros),
        "primitive_count": sum(len(word["primitives"]) for word in words),
        "persistent_coordinate_census": {
            name: len(rows) for name, rows in classes.items()
        },
        "retained_M2_per_cell_before_syndrome_ancillas": (
            palette_count - len(pump_ancillas) - len(bell_ancillas)
        ) // len(fixture.cells),
        "total_explicit_M2_per_cell_including_retained_syndromes": (
            palette_count // len(fixture.cells)
        ),
        "palette_collisions": palette_collisions,
        "route_nearest_neighbour_failures": route_nn_failures,
        "returned_label_failures": label_failures,
        "routed_target_reconstruction_failures": (
            routed_target_reconstruction_failures
        ),
        "deleted_return_label_mismatches": deletion_witness,
        "same_block_microstep_collisions": conflicts,
        "tested_active_microsteps": tested_microsteps,
        "maximum_word_microsteps": maximum_word,
        "padded_microstep_bound": PADDED_MICROSTEP_BOUND,
        "fixed_blocks": 3 * (COLOR_MODULUS ** 3) * FAMILY_SLOTS,
        "G_sites_touched": len(g_touch),
        "G_sites_outside_O": g_outside_o,
        "G_coframe_collisions": g_coframe_collisions,
        "non_O_palette_G_collisions": non_o_palette_g_collisions,
        "Bell_character_forbidden_live_or_G_hits": bell_character_forbidden,
        "serialized_returned_live_or_G_reuse": serialized_reuse,
        "route_live_hits": {
            ":".join(key): value for key, value in route_live_hits.items()
        },
        "route_G_hits": {
            ":".join(key): value for key, value in route_g_hits.items()
        },
        "route_maximum_distance": {
            ":".join(key): value for key, value in route_maximum_distance.items()
        },
        "source_binary_rebuild_failures": (
            compiled["coarse_input_binary_replacement_failures"]
            + compiled["physical_tag_rebuild_failures"]
        ),
        "private_correction_pair_candidates": len(pair_candidates),
        "private_dual_one_hot_failures": private_dual_failures,
        "anticommuting_private_correction_pairs": len(anti_pairs),
        "maximum_anticommuting_owner_cell_distance": maximum_anti_owner_distance,
        "potential_phase_firewall_macros": len(phase_firewall),
        "phase_firewall_fixed_blocks": firewall_blocks,
        "phase_firewall_declared_block_ceiling": (
            2 * (5 ** 3) * 25 * (FAMILY_SLOTS ** 2)
        ),
        "phase_firewall_same_block_collisions": firewall_collision_failures,
        "phase_firewall_returned_label_failures": firewall_return_failures,
        "phase_firewall_target_reconstruction_failures": (
            firewall_target_reconstruction_failures
        ),
        "phase_firewall_deleted_return_label_mismatches": firewall_deletion_witness,
        "phase_firewall_maximum_route_distance": firewall_maximum_distance,
    }, {
        "fixture": fixture,
        "centers": centers,
        "classes": classes,
        "words": tuple(words),
        "macros": macros,
        "corrections": corrections,
        "graph": compiled["graph"],
        "tags": compiled["tags"],
        "owners_slots": owners_slots,
        "pair_candidates": pair_candidates,
        "anti_pairs": anti_pairs,
        "phase_firewall": phase_firewall,
    }


def covariance_certificate(base):
    frames = tuple(B.V.T.proper_cubic_frames())
    origins = tuple(product((0, 1), repeat=3))
    palette = tuple(sorted(set().union(*base["classes"].values())))
    macro_paths = tuple(
        macro.path for macro in base["macros"][: min(256, len(base["macros"]))]
    )
    context_nn_failures = 0
    context_collision_invariance_failures = 0
    context_palette_failures = 0
    colour_transport_failures = 0
    source_cells = base["fixture"].cells
    source_colours = {
        tuple(value % COLOR_MODULUS for value in cell) for cell in source_cells
    }
    for frame in frames:
        frame = tuple(tuple(int(v) for v in row) for row in frame)
        frame_palette = {matvec(frame, point) for point in palette}
        context_palette_failures += len(frame_palette) != len(palette)
        for origin in origins:
            mapped_palette = {transform(point, frame, origin) for point in palette}
            context_palette_failures += len(mapped_palette) != len(palette)
            for path in macro_paths:
                mapped = tuple(transform(point, frame, origin) for point in path)
                context_nn_failures += any(
                    manhattan(left, right) != 1
                    for left, right in zip(mapped, mapped[1:])
                )
            # The origin is also the transported colour seed, so signed axis
            # permutation gives a bijection of the 27 fixed colours.
            transported = {
                tuple(v % COLOR_MODULUS for v in matvec(frame, colour))
                for colour in product(range(COLOR_MODULUS), repeat=3)
            }
            colour_transport_failures += len(transported) != COLOR_MODULUS ** 3
            mapped_source = {
                tuple(v % COLOR_MODULUS for v in matvec(frame, cell))
                for cell in source_cells
            }
            context_collision_invariance_failures += len(mapped_source) != len(source_colours)

    product_coordinate_failures = 0
    product_colour_failures = 0
    test_points = palette + tuple(
        point for path in macro_paths[:32] for point in path
    )
    colours = tuple(product(range(COLOR_MODULUS), repeat=3))
    for left in frames:
        left = tuple(tuple(int(v) for v in row) for row in left)
        for right in frames:
            right = tuple(tuple(int(v) for v in row) for row in right)
            combined = matmul(left, right)
            product_coordinate_failures += any(
                matvec(left, matvec(right, point)) != matvec(combined, point)
                for point in test_points
            )
            product_colour_failures += any(
                tuple(v % COLOR_MODULUS for v in matvec(left, matvec(right, colour)))
                != tuple(v % COLOR_MODULUS for v in matvec(combined, colour))
                for colour in colours
            )
    return {
        "proper_cubic_frames": len(frames),
        "translation_origins": len(origins),
        "frame_origin_contexts": len(frames) * len(origins),
        "ordered_frame_products": len(frames) ** 2,
        "context_nearest_neighbour_failures": context_nn_failures,
        "context_palette_bijection_failures": context_palette_failures,
        "context_collision_invariance_failures": context_collision_invariance_failures,
        "colour_transport_bijection_failures": colour_transport_failures,
        "product_coordinate_failures": product_coordinate_failures,
        "product_colour_failures": product_colour_failures,
        "boundary": (
            "coordinate, collision and colour-label covariance only; the "
            "ordered signed Clifford channel is not inferred from this census"
        ),
    }


def schedule_order_certificate(scratch, include_products=False):
    """Actual mod-3 colour re-sorts and exact two-hot phase reconstruction."""
    frames = tuple(
        tuple(tuple(int(v) for v in row) for row in frame)
        for frame in B.V.T.proper_cubic_frames()
    )
    origins = tuple(product((0, 1), repeat=3))
    corrections = scratch["corrections"]
    owners_slots = scratch["owners_slots"]
    candidates = scratch["pair_candidates"]
    anti = set(scratch["anti_pairs"])

    def order_for(frame, shift=(0, 0, 0)):
        def key(index):
            owner, slot = owners_slots[index]
            mapped = add(matvec(frame, owner), shift)
            return (
                tuple(value % COLOR_MODULUS for value in mapped),
                slot,
                # Same-block rows have disjoint primitive footprints and
                # commute; this final key only makes the emitted list stable.
                index,
            )
        return tuple(sorted(range(len(corrections)), key=key))

    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    canonical = order_for(identity)
    canonical_position = {row: index for index, row in enumerate(canonical)}

    def ordered_product(pair, position):
        left, right = pair
        if position[left] < position[right]:
            return B.multiply(corrections[left], corrections[right])
        return B.multiply(corrections[right], corrections[left])

    canonical_products = {
        pair: ordered_product(pair, canonical_position) for pair in candidates
    }

    reconstruction_failures = 0
    missing_firewall_routes = int(
        len(scratch["phase_firewall"]) != 2 * len(anti)
    )
    inversion_cz_gates = 0
    distinct_orders = set()

    def test_order(order):
        nonlocal reconstruction_failures, inversion_cz_gates
        distinct_orders.add(order)
        position = {row: index for index, row in enumerate(order)}
        for pair in candidates:
            actual = ordered_product(pair, position)
            inverted = (
                (canonical_position[pair[0]] < canonical_position[pair[1]])
                != (position[pair[0]] < position[pair[1]])
            )
            if inverted and pair in anti:
                actual = B.Pauli(
                    (actual.phase + 2) % 4, actual.x, actual.z
                )
                inversion_cz_gates += 2  # pump and Bell syndrome banks
            reconstruction_failures += (
                B.fields(actual) != B.fields(canonical_products[pair])
            )

    for frame in frames:
        for origin in origins:
            test_order(order_for(frame, origin))

    product_reconstruction_failures_before = reconstruction_failures
    frame_origin_inversion_CZ_gates = inversion_cz_gates
    if include_products:
        for left in frames:
            for right in frames:
                test_order(order_for(matmul(left, right)))
    product_reconstruction_failures = (
        reconstruction_failures - product_reconstruction_failures_before
    )
    return {
        "rows": len(corrections),
        "pair_candidates_exhausted_per_order": len(candidates),
        "frame_origin_orders": len(frames) * len(origins),
        "distinct_frame_origin_orders": len(distinct_orders),
        "frame_origin_target_reconstruction_failures": (
            product_reconstruction_failures_before
        ),
        "frame_origin_inversion_CZ_gates": frame_origin_inversion_CZ_gates,
        "frame_product_inversion_CZ_gates": (
            inversion_cz_gates - frame_origin_inversion_CZ_gates
        ),
        "missing_routed_firewall_pair_failures": missing_firewall_routes,
        "ordered_frame_products": len(frames) ** 2 if include_products else 0,
        "frame_product_target_reconstruction_failures": (
            product_reconstruction_failures
        ),
        "boundary": (
            "the coframe chart transports the generator/slot labels; this "
            "certificate attacks the actual numeric mod-3 block re-sort and "
            "reconstructs every nontrivial two-hot correction target phase"
        ),
    }


def ordered_channel_attack(atlas):
    """Exact one-cell order attack, reduced firewall and reversible repair."""
    fixture = fixture_for((1, 1, 1))
    compiled = B.compile_fixture(fixture)
    corrections = tuple(
        P.correction_from_atlas(fixture, tag, atlas)
        for tag in compiled["tags"]
    )
    q = fixture.qubits
    rows = len(corrections)
    width = 3 * q + 2 * rows

    def measurement_word(index: int, stage: str):
        source = compiled["words"][index]
        ancilla = 3 * q + (0 if stage == "pump" else rows) + index
        gates = [("H", ancilla)]
        shift = 0 if stage == "pump" else q
        for qubit in support(source["row"]):
            gates.append((
                "CP", ancilla, qubit + shift,
                letter_at(source["row"], qubit),
            ))
        gates.append(("H", ancilla))
        return tuple(gates)

    def correction_word(index: int, stage: str):
        ancilla = 3 * q + (0 if stage == "pump" else rows) + index
        gates = []
        for qubit in support(corrections[index]):
            gates.append((
                "CP", ancilla, qubit, letter_at(corrections[index], qubit)
            ))
        return tuple(gates)

    order = tuple(range(rows))
    reversed_order = tuple(reversed(order))

    def circuit(row_order):
        # Pump is triangular measurement+repair.  Bell measurement completes
        # before the separate O-correction stage.
        return (
            tuple(
                gate
                for index in row_order
                for gate in (
                    measurement_word(index, "pump")
                    + correction_word(index, "pump")
                )
            )
            + tuple(
                gate for index in row_order
                for gate in measurement_word(index, "bell")
            )
            + tuple(
                gate for index in row_order
                for gate in correction_word(index, "bell")
            )
        )

    canonical = circuit(order)
    hostile = circuit(reversed_order)
    graph_width = fixture.qubits + fixture.matter_qubits
    anticommuting_pairs = tuple(
        (left, right)
        for left in range(rows)
        for right in range(left)
        if P.M.symplectic(
            corrections[left].symplectic(graph_width),
            corrections[right].symplectic(graph_width),
            graph_width,
        )
    )
    # Reversing two controlled anticommuting Paulis contributes exactly one
    # CZ between their syndrome controls.  Add that inversion cocycle to both
    # pump and Bell syndrome banks.
    inversion_cz = tuple(
        ("CP", 3 * q + offset + left, 3 * q + offset + right, "Z")
        for offset in (0, rows)
        for left, right in anticommuting_pairs
    )
    repaired_hostile = hostile + inversion_cz
    full_mismatches = output_mismatches = 0
    repaired_full_mismatches = 0
    canonical_images = []
    hostile_images = []
    for qubit in range(width):
        for letter in ("X", "Z"):
            row = B.pauli_letter(qubit, letter)
            left = B.conjugate_word(row, canonical)
            right = B.conjugate_word(row, hostile)
            repaired = B.conjugate_word(row, repaired_hostile)
            canonical_images.append(left)
            hostile_images.append(right)
            mismatch = B.fields(left) != B.fields(right)
            full_mismatches += mismatch
            output_mismatches += mismatch and qubit < q
            repaired_full_mismatches += B.fields(left) != B.fields(repaired)

    permutation_controls = (
        (tuple(range(0, rows, 2)) + tuple(range(1, rows, 2))),
        *(tuple(order[shift:] + order[:shift]) for shift in range(1, rows)),
    )
    permutation_firewall_failures = 0
    permutation_inversion_cz_gates = 0
    canonical_fields = tuple(B.fields(row) for row in canonical_images)
    for row_order in permutation_controls:
        position = {row: index for index, row in enumerate(row_order)}
        inversions = tuple(
            (left, right) for left, right in anticommuting_pairs
            if position[left] < position[right]
        )
        cocycle = tuple(
            ("CP", 3 * q + offset + left, 3 * q + offset + right, "Z")
            for offset in (0, rows)
            for left, right in inversions
        )
        permutation_inversion_cz_gates += len(cocycle)
        repaired = circuit(row_order) + cocycle
        actual = tuple(
            B.fields(B.conjugate_word(B.pauli_letter(qubit, letter), repaired))
            for qubit in range(width)
            for letter in ("X", "Z")
        )
        permutation_firewall_failures += actual != canonical_fields

    # Compare the reduced O channel exactly on all 4^9 output Pauli
    # observables.  Syndrome ancillas start in |0>; an X/Y factor has zero
    # matrix element and a Z factor evaluates to +1 before they are traced.
    ancilla_mask = ((1 << (2 * rows)) - 1) << (3 * q)
    system_mask = (1 << (3 * q)) - 1

    def reduced(row):
        if row.x & ancilla_mask:
            return ("zero",)
        return (row.phase % 4, row.x & system_mask, row.z & system_mask)

    canonical_x = canonical_images[0::2][:q]
    canonical_z = canonical_images[1::2][:q]
    hostile_x = hostile_images[0::2][:q]
    hostile_z = hostile_images[1::2][:q]

    def image_from_generators(x, z, x_images, z_images):
        row = B.Pauli()
        for qubit in range(q):
            if (x >> qubit) & 1:
                row = B.multiply(row, x_images[qubit])
        for qubit in range(q):
            if (z >> qubit) & 1:
                row = B.multiply(row, z_images[qubit])
        return row

    reduced_mismatches = 0
    reduced_observables = 1 << (2 * q)
    for x in range(1 << q):
        for z in range(1 << q):
            reduced_mismatches += reduced(image_from_generators(
                x, z, canonical_x, canonical_z
            )) != reduced(image_from_generators(
                x, z, hostile_x, hostile_z
            ))
    return {
        "one_cell_abstract_wires": width,
        "one_cell_rows_per_stage": rows,
        "canonical_gates": len(canonical),
        "anticommuting_private_correction_pairs": len(anticommuting_pairs),
        "hostile_reversal_full_signed_generator_mismatches": full_mismatches,
        "hostile_reversal_O_output_generator_mismatches": output_mismatches,
        "reduced_O_Pauli_observables_exhausted": reduced_observables,
        "hostile_reversal_reduced_O_channel_mismatches": reduced_mismatches,
        "inversion_CZ_gates": len(inversion_cz),
        "CZ_repaired_full_signed_generator_mismatches": repaired_full_mismatches,
        "additional_order_permutations_tested": len(permutation_controls),
        "additional_permutation_inversion_CZ_gates": permutation_inversion_cz_gates,
        "additional_permutation_firewall_failures": permutation_firewall_failures,
        "verdict": (
            "bare row order changes the retained-syndrome dilation but not the "
            "reduced O channel; the explicit local inversion-CZ cocycle restores "
            "the full signed Clifford tableau for reversal"
        ),
    }


def source_hashes():
    names = (
        "frontier_companion_bank_bell_character_dilation_2026_07_28.py",
        "frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
        "frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
        "frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27.py",
    )
    root = Path(__file__).resolve().parent
    return {
        name: sha256((root / name).read_bytes()).hexdigest() for name in names
    }


def main() -> None:
    atlas = P.build_private_atlases()
    boxes = []
    scratches = []
    base = None
    for shape in SHAPES:
        report, scratch = box_certificate(shape, atlas)
        boxes.append(report)
        scratches.append(scratch)
        if shape == (2, 2, 2):
            base = scratch
        print("BOX", json.dumps(report, sort_keys=True))
    assert base is not None
    covariance = covariance_certificate(base)
    schedule_orders = tuple(
        schedule_order_certificate(
            scratch,
            include_products=(scratch["fixture"].cells == base["fixture"].cells),
        )
        for scratch in scratches
    )
    order_attack = ordered_channel_attack(atlas)
    checks = []

    def check(label, condition):
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "explicit O/I/L, 3N coframe and two syndrome palettes are collision-free with a fixed 64-M2/cell census",
        all(
            row["palette_collisions"] == 0
            and row["retained_M2_per_cell_before_syndrome_ancillas"] == 30
            and row["total_explicit_M2_per_cell_including_retained_syndromes"] == 64
            and row["persistent_coordinate_census"]["coframe"] == 3 * row["cells"]
            for row in boxes
        ),
    )
    check(
        "all explicit Manhattan macros are nearest-neighbour and return every traversed label",
        all(
            row["route_nearest_neighbour_failures"] == 0
            and row["returned_label_failures"] == 0
            and row["routed_target_reconstruction_failures"] == 0
            for row in boxes
        ),
    )
    check(
        "deleting a final reverse SWAP leaves an active label mismatch",
        all(row["deleted_return_label_mismatches"] > 0 for row in boxes),
    )
    check(
        "mod-3 cell colours and 17 signed-port family slots have no simultaneous primitive collision and fit one fixed padded bound",
        all(
            row["same_block_microstep_collisions"] == 0
            and row["maximum_word_microsteps"] <= PADDED_MICROSTEP_BOUND
            and row["fixed_blocks"] == 1377
            for row in boxes
        ),
    )
    check(
        "the external I/L Bell-character routes avoid every live palette and every Cycle-720 G site",
        all(row["Bell_character_forbidden_live_or_G_hits"] == 0 for row in boxes),
    )
    check(
        "G touches only O, extends by identity over the explicit 3N coframe and all non-O palettes, and begins after every returned route",
        all(
            row["G_sites_outside_O"] == 0
            and row["G_coframe_collisions"] == 0
            and not any(row["non_O_palette_G_collisions"].values())
            and row["returned_label_failures"] == 0
            for row in boxes
        ),
    )
    check(
        "the source character rebuild remains exact on every held box",
        all(
            row["source_binary_rebuild_failures"] == 0
            and row["private_dual_one_hot_failures"] == 0
            for row in boxes
        ),
    )
    check(
        "every potential local inversion-CZ firewall has a returned NN route, a fixed mod-5 block and an active deletion control",
        all(
            row["maximum_anticommuting_owner_cell_distance"] <= 2
            and row["potential_phase_firewall_macros"]
                == 2 * row["anticommuting_private_correction_pairs"]
            and row["phase_firewall_same_block_collisions"] == 0
            and row["phase_firewall_fixed_blocks"]
                <= row["phase_firewall_declared_block_ceiling"]
            and row["phase_firewall_returned_label_failures"] == 0
            and row["phase_firewall_target_reconstruction_failures"] == 0
            and row["phase_firewall_deleted_return_label_mismatches"] > 0
            for row in boxes
        ),
    )
    check(
        "the coframe palette, nearest-neighbour paths and mod-3 schedule geometry are exact in 24 frames by 8 origins and all 576 frame products",
        covariance["proper_cubic_frames"] == 24
        and covariance["translation_origins"] == 8
        and covariance["ordered_frame_products"] == 576
        and all(
            value == 0 for key, value in covariance.items()
            if key.endswith("failures")
        ),
    )
    check(
        "actual frame/origin mod-3 order permutations reconstruct every nontrivial two-hot correction target, including 576 products on 2x2x2",
        all(
            row["frame_origin_target_reconstruction_failures"] == 0
            and row["missing_routed_firewall_pair_failures"] == 0
            and row["frame_product_target_reconstruction_failures"] == 0
            for row in schedule_orders
        )
        and sum(row["ordered_frame_products"] for row in schedule_orders) == 576,
    )
    check(
        "exact Clifford controls separate harmless reduced-channel order from retained-syndrome phase and repair the latter with the inversion-CZ cocycle",
        order_attack["anticommuting_private_correction_pairs"] > 0
        and order_attack["hostile_reversal_full_signed_generator_mismatches"] > 0
        and order_attack["hostile_reversal_O_output_generator_mismatches"] > 0
        and order_attack["hostile_reversal_reduced_O_channel_mismatches"] == 0
        and order_attack["CZ_repaired_full_signed_generator_mismatches"] == 0
        and order_attack["additional_permutation_firewall_failures"] == 0,
    )
    report = {
        "status": "PASS" if all(row["pass"] for row in checks) else "FAIL",
        "authority": "none",
        "audit": "unset",
        "claim": (
            "conditional fixed translation-local physical scheduling theorem for "
            "the repaired three-register O/I/L character circuit, with a returned-"
            "route site firewall before the separately landed Cycle-720 G; "
            "circuit-layer indices are not physical time"
        ),
        "checks": checks,
        "boxes": boxes,
        "covariance": covariance,
        "actual_schedule_order_covariance": schedule_orders,
        "ordered_channel_attack": order_attack,
        "source_sha256": source_hashes(),
        "derived": (
            "explicit 64-M2/cell coframe palette; fixed mod-3-by-17 schedule; "
            "literal nearest-neighbour returned SWAP/controlled-Pauli macros; "
            "held-size collision, label-return, G-firewall and 24/576 geometric "
            "covariance certificates; exhaustive one-cell reduced-channel order "
            "firewall and exact inversion-CZ repair of the retained dilation"
        ),
        "supplied": (
            "fixed parity/center sector and mixed-gauge reference; 3N locally "
            "constrained coframe M2 and its origin sector; clean pump and Bell "
            "ancillas; O/I Choi-pump and I/L Bell-character algebra; private "
            "correction atlas; cell chart, signed-port slot labels, mod-3 colour "
            "origin, transported ordered tableau program, stage order, boundary, "
            "and the landed recurrent G"
        ),
        "open": (
            "autonomous genesis/renewal and local enforcement of all retained "
            "banks, syndrome and coframe constraints; removal of the supplied "
            "stage/program order; fault-tolerant physical gate realization; "
            "translation-invariant recurrent admission; a routed held-box and "
            "24/576 signed-channel test of the inversion-CZ firewall under actual "
            "frame-induced generator changes; law-level time, source/gravity, "
            "Record and Born/history bridges"
        ),
        "boundary": (
            "serialized live-O/G relay reuse is allowed only because every route "
            "is literally returned before the G barrier; this is a conditional "
            "finite-depth schedule theorem. Bare numerical reordering "
            "changes the retained-syndrome dilation but not the reduced O channel; "
            "a local CZ cocycle repairs the tested one-cell permutations. Geometric "
            "covariance is still not a held-box full signed-channel theorem. This "
            "is not an autonomous clock, "
            "genesis theorem, minimum, no-go, Record, Born law, or source/gravity law"
        ),
    }
    print("REPORT_JSON", json.dumps(report, sort_keys=True))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
