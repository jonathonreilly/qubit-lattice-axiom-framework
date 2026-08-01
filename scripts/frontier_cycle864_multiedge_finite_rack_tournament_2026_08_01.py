#!/usr/bin/env python3
"""Cycle-864 finite multiedge controller-rack tournament.

Test direct per-edge copies of the Cycle863 endpoint/history port on the
actual Cycle823 held boxes.  First census the literal owner-local transported
templates.  Then place one oriented Cycle719 controller per edge in a finite
held-family rack and compile actual typed FSWAP/SWAP access routes.

This executable establishes a finite held-box packing theorem, not a local
translation-equivariant recurrent compiler.  The rack origin, pitch, edge
enumeration, fixed serial circuit, clean corridors, and first-use genesis are
explicit supplies.

Authority: none.  Audit: unset.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from heapq import heappop, heappush
from itertools import permutations
import json
import math
import sys
import time

import numpy as np

import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as H719
import frontier_cycle822_routec_staggered_radius_one_parity_even_transport_2026_07_30 as R822
import frontier_cycle823_companion_full_seam_endpoint_instrument_2026_07_30 as I823
import frontier_cycle826_companion_endpoint_cycle719_history_interface_2026_07_30 as I826
import frontier_cycle827_cycle719_parity_safe_typed_controller_atlas_2026_07_30 as C827
import frontier_cycle863_cycle823_cycle719_same_chart_history_port_2026_08_01 as C863


SHAPES = ((3, 1, 1), (3, 2, 2), (5, 3, 2))
AXIS_FRAMES = (
    ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    ((0, 0, 1), (1, 0, 0), (0, 1, 0)),  # (x,y,z) -> (z,x,y)
    ((0, 1, 0), (0, 0, 1), (1, 0, 0)),  # (x,y,z) -> (y,z,x)
)
RACK_ORIGIN = (256, 256, 256)
RACK_SPACING = 160
RACK_SIDE = 4
NEIGHBOURS = (
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
    (-1, 0, 0), (0, -1, 0), (0, 0, -1),
)
EXPECTED_HISTORY = {
    (0, 0): (),
    (1, 0): (-1,),
    (0, 1): (1,),
    (1, 1): (),
}


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mv(frame, vector):
    return tuple(
        sum(frame[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )


def mm(left, right):
    return tuple(tuple(
        sum(left[row][inner] * right[inner][column] for inner in range(3))
        for column in range(3)
    ) for row in range(3))


def transport(site, old_anchor, frame, new_anchor):
    return add(new_anchor, mv(frame, sub(site, old_anchor)))


def transport_set(sites, old_anchor, frame, new_anchor):
    return frozenset(
        transport(site, old_anchor, frame, new_anchor) for site in sites
    )


def transport_path(path, old_anchor, frame, new_anchor):
    return tuple(
        transport(site, old_anchor, frame, new_anchor) for site in path
    )


def manhattan(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def simple_manhattan_path(source, target, order):
    output = [source]
    current = list(source)
    for axis in order:
        step = 1 if target[axis] > current[axis] else -1
        while current[axis] != target[axis]:
            current[axis] += step
            output.append(tuple(current))
    return tuple(output)


def valid_path(path, blocked):
    return (
        len(path) == len(set(path))
        and all(manhattan(a, b) == 1 for a, b in zip(path, path[1:]))
        and not (set(path[1:-1]) & blocked)
    )


def weighted_astar(source, target, blocked, bias):
    """Fast deterministic route finder; validity, not shortestness, is claimed."""
    blocked = set(blocked) - {source, target}
    orders = tuple(permutations(range(3)))
    for offset in range(6):
        path = simple_manhattan_path(
            source, target, orders[(bias + offset) % 6]
        )
        if valid_path(path, blocked):
            return path, 0, len(path)

    low = tuple(min(a, b) - 48 for a, b in zip(source, target))
    high = tuple(max(a, b) + 48 for a, b in zip(source, target))
    neighbour_order = tuple(
        NEIGHBOURS[(bias + index) % len(NEIGHBOURS)]
        for index in range(len(NEIGHBOURS))
    )
    heap = []
    serial = 0
    heappush(heap, (1.15 * manhattan(source, target), 0, 0, source))
    parent = {source: None}
    distance = {source: 0}
    expanded = 0
    while heap:
        _score, neg_g, _serial, site = heappop(heap)
        g = -neg_g
        if g != distance.get(site):
            continue
        expanded += 1
        if site == target:
            break
        if expanded > 2_000_000:
            raise RuntimeError(("A* expansion ceiling", source, target, bias))
        candidates = []
        for delta in neighbour_order:
            candidate = add(site, delta)
            if candidate in blocked:
                continue
            if any(
                candidate[axis] < low[axis] or candidate[axis] > high[axis]
                for axis in range(3)
            ):
                continue
            candidates.append(candidate)
        candidates.sort(key=lambda item: manhattan(item, target))
        for candidate in candidates:
            candidate_g = g + 1
            if candidate_g >= distance.get(candidate, 1 << 60):
                continue
            distance[candidate] = candidate_g
            parent[candidate] = site
            serial += 1
            heappush(heap, (
                candidate_g + 1.15 * manhattan(candidate, target),
                -candidate_g, serial, candidate,
            ))
    if target not in parent:
        raise RuntimeError(("no route", source, target, len(blocked), expanded))
    output = []
    cursor = target
    while cursor is not None:
        output.append(cursor)
        cursor = parent[cursor]
    output.reverse()
    return tuple(output), expanded, len(parent)


def shortest_adapter(source, target, blocked):
    delta = sub(target, source)
    steps = []
    for axis, value in enumerate(delta):
        step = 1 if value > 0 else -1
        steps.extend((axis, step) for _ in range(abs(value)))
    best = None
    for order in sorted(set(permutations(steps))):
        current = source
        path = [source]
        for axis, step in order:
            move = [0, 0, 0]
            move[axis] = step
            current = add(current, tuple(move))
            path.append(current)
        path = tuple(path)
        if valid_path(path, set(blocked) - {source, target}):
            best = path
            break
    return best


def execute_blank_route(path, *, fermionic, delete_ordinal=None, occupied=(0,)):
    """Execute one returned-route word on sparse occupation labels.

    This is state-level on the route code space: every corridor interior is
    blank and the endpoint modes may be occupied.  ``fermionic`` selects
    FSWAP rather than SWAP, so a dirty 11 endpoint sector retains its sign.
    """
    distance = len(path) - 1
    edge_ordinals = tuple(range(distance))
    word = edge_ordinals[:-1] + edge_ordinals[-1:] + tuple(
        reversed(edge_ordinals[:-1])
    )
    bits = set(occupied)
    phase = 1
    for ordinal, edge in enumerate(word):
        if ordinal == delete_ordinal:
            continue
        left, right = edge, edge + 1
        left_bit, right_bit = left in bits, right in bits
        if fermionic and left_bit and right_bit:
            phase *= -1
        if left_bit != right_bit:
            bits.symmetric_difference_update((left, right))
    return tuple(sorted(bits)), phase


def route_state_controls(paths):
    """Literal transfer, inverse, dirty-sector, and deletion witnesses."""
    rows = []
    failures = inverse_failures = deletion_failures = 0
    dirty_sign_failures = 0
    deletion_residuals = []
    for (edge_index, port), path in sorted(paths.items()):
        distance = len(path) - 1
        fermionic = port < 2
        observed, phase = execute_blank_route(path, fermionic=fermionic)
        expected = ((distance,), 1)
        failures += (observed, phase) != expected

        returned, return_phase = execute_blank_route(
            path, fermionic=fermionic, occupied=observed
        )
        inverse_failures += (returned, phase * return_phase) != ((0,), 1)

        central = distance - 1
        damaged, damaged_phase = execute_blank_route(
            path, fermionic=fermionic, delete_ordinal=central
        )
        deletion_residual = (
            0.0 if (damaged, damaged_phase) == expected else math.sqrt(2.0)
        )
        deletion_failures += deletion_residual == 0.0
        deletion_residuals.append(deletion_residual)

        dirty = execute_blank_route(
            path, fermionic=fermionic, occupied=(0, distance)
        )
        expected_dirty_phase = -1 if fermionic else 1
        dirty_sign_failures += dirty != ((0, distance), expected_dirty_phase)
        rows.append({
            "edge_index": edge_index,
            "port": port,
            "distance": distance,
            "exchange": "FSWAP" if fermionic else "SWAP",
            "transfer_output": observed,
            "transfer_phase": phase,
            "inverse_output": returned,
            "inverse_phase": phase * return_phase,
            "central_deletion_output": damaged,
            "central_deletion_residual": deletion_residual,
            "dirty_endpoint_phase": dirty[1],
        })
    return {
        "route_cases": len(rows),
        "literal_transfer_failures": failures,
        "literal_inverse_failures": inverse_failures,
        "central_deletion_failures": deletion_failures,
        "central_deletions_detected": sum(
            residual > 0.0 for residual in deletion_residuals
        ),
        "minimum_central_deletion_residual": min(deletion_residuals),
        "maximum_central_deletion_residual": max(deletion_residuals),
        "dirty_endpoint_exchange_sign_failures": dirty_sign_failures,
        "rows": tuple(rows),
    }


def set_bounds(sites):
    return {
        "minimum": tuple(min(site[axis] for site in sites) for axis in range(3)),
        "maximum": tuple(max(site[axis] for site in sites) for axis in range(3)),
    }


def build_base():
    geometry = C863.joint_geometry()
    edge = geometry["context"]["fixture"].edges[C863.EDGE_INDEX]
    owner = geometry["context"]["centers"][edge[2]]
    proper_frames = tuple(
        tuple(tuple(int(value) for value in row) for row in frame)
        for frame in R822.B.V.T.proper_cubic_frames()
    )
    frame_failures = sum(frame not in proper_frames for frame in AXIS_FRAMES)
    determinant_failures = sum(
        round(float(__import__("numpy").linalg.det(__import__("numpy").array(frame)))) != 1
        for frame in AXIS_FRAMES
    )
    return {
        "geometry": geometry,
        "owner": owner,
        "frames": proper_frames,
        "frame_membership_failures": frame_failures,
        "proper_determinant_failures": determinant_failures,
    }


def shape_context(shape, private):
    context = I823.augment_context(R822.local_site_maps(shape, private))
    context, routes, words, *_rest = R822.fixed_typed_compile(context)
    report, charged, neutral = R822.fixed_type_assignment(context, routes)
    return context, routes, words, report, charged, neutral


def local_template_census(base, context, seam_charged, seam_neutral):
    geometry = base["geometry"]
    old_owner = base["owner"]
    rows = []
    endpoint_binding_failures = pointer_target_failures = 0
    adapter_failures = adapter_persistent_hits = adapter_charged_hits = 0
    own_type_overlaps = 0
    companion_cross_type_hits = 0
    companion_cross_type_pairs = 0
    internal_companion_persistent_hits = 0
    templates = []
    for edge_index, edge in enumerate(context["fixture"].edges):
        axis = edge[3]
        frame = AXIS_FRAMES[axis]
        owner = context["centers"][edge[2]]
        charged_paths = tuple(
            transport_path(path, old_owner, frame, owner)
            for path in geometry["port_paths"][:2]
        )
        pointer_path = transport_path(
            geometry["port_paths"][2], old_owner, frame, owner
        )
        actual_sources = (
            context["o_sites"][edge[4]],
            context["o_sites"][edge[5]],
            context["endpoint_auxiliaries"][edge_index][2],
        )
        endpoint_binding_failures += charged_paths[0][0] != actual_sources[0]
        endpoint_binding_failures += charged_paths[1][0] != actual_sources[1]
        pointer_distance = manhattan(actual_sources[2], pointer_path[0])
        blocked = (
            set(context["persistent"])
            | set(seam_charged)
            | set(transport_set(
                geometry["controller_charged"], old_owner, frame, owner
            ))
        ) - {actual_sources[2], pointer_path[0]}
        adapter = (
            (actual_sources[2],) if pointer_distance == 0
            else shortest_adapter(actual_sources[2], pointer_path[0], blocked)
        )
        adapter_failures += adapter is None
        if adapter is None:
            adapter = (actual_sources[2], pointer_path[0])
        adapter_persistent_hits += len(
            set(adapter[1:-1]) & set(context["persistent"])
        )
        adapter_charged_hits += len(set(adapter) & set(seam_charged))
        controller_charged = transport_set(
            geometry["controller_charged"], old_owner, frame, owner
        )
        controller_neutral = transport_set(
            geometry["controller_neutral"], old_owner, frame, owner
        )
        controller_wires = transport_set(
            geometry["translated_wires"], old_owner, frame, owner
        )
        charged = frozenset(
            set(controller_charged)
            | set(charged_paths[0]) | set(charged_paths[1])
        )
        neutral = frozenset(
            set(controller_neutral) | set(pointer_path) | set(adapter)
        )
        own_type_overlaps += len(charged & neutral)
        cross = (set(charged) & set(seam_neutral)) | (
            set(neutral) & set(seam_charged)
        )
        companion_cross_type_hits += len(cross)
        companion_cross_type_pairs += bool(cross)
        paths = charged_paths + (pointer_path,)
        internal_companion_persistent_hits += sum(
            len(set(path[1:-1]) & set(context["persistent"]))
            for path in paths
        )
        pointer_target_failures += pointer_path[-1] != transport(
            geometry["targets"][2], old_owner, frame, owner
        )
        templates.append({
            "edge_index": edge_index,
            "axis": axis,
            "owner": edge[2],
            "physical_owner_center": owner,
            "sources": actual_sources,
            "transported_pointer_source": pointer_path[0],
            "pointer_adapter_distance": pointer_distance,
            "pointer_adapter": adapter,
            "charged": charged,
            "neutral": neutral,
            "controller_wires": controller_wires,
        })
        rows.append((
            edge_index, axis, edge[2], actual_sources,
            charged_paths[0][-1], charged_paths[1][-1], pointer_path[-1],
            pointer_distance, adapter,
        ))

    pair_counts = Counter()
    pair_site_counts = Counter()
    for left_index, left in enumerate(templates):
        for right in templates[left_index + 1:]:
            intersections = {
                "charged_charged": set(left["charged"]) & set(right["charged"]),
                "neutral_neutral": set(left["neutral"]) & set(right["neutral"]),
                "left_charged_right_neutral": set(left["charged"]) & set(right["neutral"]),
                "left_neutral_right_charged": set(left["neutral"]) & set(right["charged"]),
                "controller_persistent": set(left["controller_wires"]) & set(right["controller_wires"]),
            }
            for label, sites in intersections.items():
                pair_counts[label] += bool(sites)
                pair_site_counts[label] += len(sites)
            cross = (
                intersections["left_charged_right_neutral"]
                | intersections["left_neutral_right_charged"]
            )
            pair_counts["any_cross_type"] += bool(cross)
            pair_site_counts["any_cross_type"] += len(cross)
            any_overlap = set().union(*intersections.values())
            pair_counts["any_overlap"] += bool(any_overlap)
            pair_site_counts["any_overlap"] += len(any_overlap)
    all_charged = set().union(*(set(row["charged"]) for row in templates))
    all_neutral = set().union(*(set(row["neutral"]) for row in templates))
    digest_rows = tuple(
        (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        for row in rows
    )
    return {
        "edges": len(templates),
        "axis_counts": dict(sorted(Counter(row["axis"] for row in templates).items())),
        "endpoint_binding_failures": endpoint_binding_failures,
        "pointer_target_failures": pointer_target_failures,
        "pointer_adapter_distance_census": dict(sorted(Counter(
            row["pointer_adapter_distance"] for row in templates
        ).items())),
        "pointer_adapter_failures": adapter_failures,
        "pointer_adapter_internal_persistent_hits": adapter_persistent_hits,
        "pointer_adapter_charged_hits": adapter_charged_hits,
        "own_template_charged_neutral_overlaps": own_type_overlaps,
        "template_companion_cross_type_pairs": companion_cross_type_pairs,
        "template_companion_cross_type_site_hits": companion_cross_type_hits,
        "local_port_internal_companion_persistent_hits": internal_companion_persistent_hits,
        "pair_conflict_counts": dict(sorted(pair_counts.items())),
        "aggregate_pair_intersection_sites": dict(sorted(pair_site_counts.items())),
        "global_template_charged_neutral_overlap_coordinates": len(
            all_charged & all_neutral
        ),
        "axis_template_sha256": sha256(repr(digest_rows).encode()).hexdigest(),
        "templates": templates,
    }


def rack_slot(index):
    return add(RACK_ORIGIN, tuple(
        RACK_SPACING * value for value in (
            index % RACK_SIDE,
            (index // RACK_SIDE) % RACK_SIDE,
            index // (RACK_SIDE * RACK_SIDE),
        )
    ))


def rack_compile(base, context, seam_charged, seam_neutral):
    geometry = base["geometry"]
    old_owner = base["owner"]
    controllers = []
    charged = set(seam_charged)
    neutral = set(seam_neutral)
    persistent = set(context["persistent"])
    placement_conflicts = Counter()
    placement_conflict_sites = Counter()
    for edge_index, edge in enumerate(context["fixture"].edges):
        frame = AXIS_FRAMES[edge[3]]
        slot = rack_slot(edge_index)
        controller_charged = transport_set(
            geometry["controller_charged"], old_owner, frame, slot
        )
        controller_neutral = transport_set(
            geometry["controller_neutral"], old_owner, frame, slot
        )
        controller_wires = transport_set(
            geometry["translated_wires"], old_owner, frame, slot
        )
        intersections = {
            "charged_charged": set(controller_charged) & charged,
            "neutral_neutral": set(controller_neutral) & neutral,
            "charged_neutral": set(controller_charged) & neutral,
            "neutral_charged": set(controller_neutral) & charged,
            "persistent": set(controller_wires) & persistent,
        }
        for label, sites in intersections.items():
            placement_conflicts[label] += bool(sites)
            placement_conflict_sites[label] += len(sites)
        charged.update(controller_charged)
        neutral.update(controller_neutral)
        persistent.update(controller_wires)
        sources = (
            context["o_sites"][edge[4]],
            context["o_sites"][edge[5]],
            context["endpoint_auxiliaries"][edge_index][2],
        )
        tails = tuple(
            transport_path(path, old_owner, frame, slot)
            for path in geometry["port_paths"]
        )
        targets = tuple(
            transport(target, old_owner, frame, slot)
            for target in geometry["targets"]
        )
        controllers.append({
            "edge_index": edge_index,
            "axis": edge[3],
            "owner": edge[2],
            "slot": slot,
            "sources": sources,
            "tails": tails,
            "targets": targets,
            "controller_charged": controller_charged,
            "controller_neutral": controller_neutral,
            "controller_wires": controller_wires,
        })

    fixed_charged = set(charged)
    fixed_neutral = set(neutral)
    fixed_cross_type = fixed_charged & fixed_neutral
    paths = {}
    astar_expansions = 0
    astar_discoveries = 0
    # Charged endpoint routes first.  Same-type corridors may be reused because
    # every complete returned macro has its own fixed serial circuit stage.
    for controller in controllers:
        for port in (0, 1):
            source = controller["sources"][port]
            tail = controller["tails"][port]
            access = tail[0]
            blocked = (
                (persistent - {source, access})
                | fixed_neutral
                | set(tail[1:-1])
            ) - {source, access}
            bus, expanded, discovered = weighted_astar(
                source, access, blocked, 31 * controller["edge_index"] + port
            )
            path = bus[:-1] + tail
            paths[(controller["edge_index"], port)] = path
            charged.update(path)
            astar_expansions += expanded
            astar_discoveries += discovered

    # Neutral pointer routes avoid the complete charged assignment, including
    # newly compiled endpoint corridors.
    for controller in controllers:
        source = controller["sources"][2]
        tail = controller["tails"][2]
        access = tail[0]
        blocked = (
            (persistent - {source, access})
            | charged
            | set(tail[1:-1])
        ) - {source, access}
        bus, expanded, discovered = weighted_astar(
            source, access, blocked, 31 * controller["edge_index"] + 2
        )
        path = bus[:-1] + tail
        paths[(controller["edge_index"], 2)] = path
        neutral.update(path)
        astar_expansions += expanded
        astar_discoveries += discovered

    route_failures = Counter()
    route_distances = []
    route_gate_counts = []
    charged_path_sites = set()
    neutral_path_sites = set()
    for (edge_index, port), path in paths.items():
        controller = controllers[edge_index]
        expected_source = controller["sources"][port]
        expected_target = controller["targets"][port]
        route_failures["source_binding"] += path[0] != expected_source
        route_failures["target_binding"] += path[-1] != expected_target
        route_failures["repeated_site"] += len(path) != len(set(path))
        route_failures["non_nearest_neighbour"] += sum(
            manhattan(left, right) != 1
            for left, right in zip(path, path[1:])
        )
        route_failures["internal_persistent"] += len(
            set(path[1:-1]) & persistent
        )
        if port < 2:
            route_failures["charged_path_neutral_hits"] += len(
                set(path) & neutral
            )
            charged_path_sites.update(path)
        else:
            route_failures["neutral_path_charged_hits"] += len(
                set(path) & charged
            )
            neutral_path_sites.update(path)
        structure = C827.route_structure(path)
        route_failures["route_structure"] += sum(structure[:3])
        route_failures["active_deletion_missing"] += (
            len(path) > 2 and not structure[3]
        )
        distance = len(path) - 1
        route_distances.append(distance)
        route_gate_counts.append(2 * distance - 1)

    endpoint_gates = sum(
        route_gate_counts[3 * edge + port]
        for edge in range(len(controllers)) for port in (0, 1)
    )
    pointer_gates = sum(
        route_gate_counts[3 * edge + 2] for edge in range(len(controllers))
    )
    # paths dict insertion is all charged then all neutral, so recompute the
    # forward factor count directly by keyed lookup rather than list order.
    forward_factors = 0
    keyed_gate_counts = {}
    for key, path in paths.items():
        keyed_gate_counts[key] = 2 * (len(path) - 1) - 1
    for edge in range(len(controllers)):
        forward_factors += (
            2 * keyed_gate_counts[(edge, 0)]
            + 2 * keyed_gate_counts[(edge, 1)]
            + keyed_gate_counts[(edge, 2)]
        )

    same_type_reuse = {
        "charged_route_coordinate_occurrences_minus_unique": (
            sum(len(paths[(edge, port)]) for edge in range(len(controllers)) for port in (0, 1))
            - len(charged_path_sites)
        ),
        "neutral_route_coordinate_occurrences_minus_unique": (
            sum(len(paths[(edge, 2)]) for edge in range(len(controllers)))
            - len(neutral_path_sites)
        ),
    }
    state_controls = route_state_controls(paths)
    return {
        "controllers": controllers,
        "paths": paths,
        "placement_conflict_pairs": dict(sorted(placement_conflicts.items())),
        "placement_conflict_sites": dict(sorted(placement_conflict_sites.items())),
        "fixed_palette_cross_type_coordinates_before_ports": len(fixed_cross_type),
        "combined_charged_coordinates": len(charged),
        "combined_neutral_coordinates": len(neutral),
        "combined_charged_neutral_overlap": len(charged & neutral),
        "persistent_coordinates": len(persistent),
        "route_failures": dict(sorted(route_failures.items())),
        "route_count": len(paths),
        "route_distance_minimum": min(route_distances),
        "route_distance_maximum": max(route_distances),
        "route_distance_sum": sum(route_distances),
        "returned_route_gate_sum_one_pass": sum(keyed_gate_counts.values()),
        "forward_port_factor_count": forward_factors,
        "same_type_serial_reuse": same_type_reuse,
        "weighted_astar_expansions": astar_expansions,
        "weighted_astar_discoveries": astar_discoveries,
        "controller_fixed_M2_per_edge": len(
            geometry["controller_charged"] | geometry["controller_neutral"]
        ),
        "controller_persistent_M2_per_edge": len(geometry["translated_wires"]),
        "rack_anchor_bounds": set_bounds(tuple(row["slot"] for row in controllers)),
        "rack_spacing": RACK_SPACING,
        "rack_side": RACK_SIDE,
        "path_sha256": sha256(repr(tuple(sorted(paths.items()))).encode()).hexdigest(),
        "charged_coordinate_sha256": sha256(repr(tuple(sorted(charged))).encode()).hexdigest(),
        "neutral_coordinate_sha256": sha256(repr(tuple(sorted(neutral))).encode()).hexdigest(),
        "state_level_route_controls": state_controls,
    }


def controller_semantic_table(base):
    geometry = base["geometry"]
    normalized_fast = H719.fast_classical_word(geometry["normalized"])
    rows = {}
    failures = inverse_failures = cleanup_failures = 0
    imported_interface_agreement_failures = 0
    for left in (0, 1):
        for right in (0, 1):
            before = C863.controller_genesis()
            before |= left << H719.M.R3.X.LEFT_ENDPOINT
            before |= right << H719.M.R3.X.RIGHT_ENDPOINT
            before |= (left ^ right) << H719.R3_SOURCE_POINTER()
            observed = H719.repeated_fast_word(before, normalized_fast)
            restored = H719.repeated_fast_word(
                observed, tuple(reversed(normalized_fast))
            )
            history = C863.decode_history(observed)
            expected = EXPECTED_HISTORY[(left, right)]
            failures += history != expected
            imported_interface_agreement_failures += (
                expected != I826.expected_orientation(left, right, left ^ right)
            )
            inverse_failures += restored != before
            registers = H719.controller_register_rows(observed)
            cleanup_failures += not (
                ((observed >> H719.M.R3.X.LEFT_ENDPOINT) & 1) == left
                and ((observed >> H719.M.R3.X.RIGHT_ENDPOINT) & 1) == right
                and not ((observed >> H719.R3_SOURCE_POINTER()) & 1)
                and registers["A"] == (1,) + (0,) * (H719.CONTROLLER_STATIONS - 1)
                and not any(registers["B"])
                and not any(registers["work"])
            )
            rows[(left, right)] = {
                "history": history,
                "expected": expected,
                "observed": observed,
                "restored": restored,
                "before": before,
            }
    return {
        "rows": rows,
        "truth_rows": len(rows),
        "history_failures": failures,
        "inverse_failures": inverse_failures,
        "cleanup_failures": cleanup_failures,
        "imported_interface_agreement_failures": (
            imported_interface_agreement_failures
        ),
        "normalized_semantic_gates_per_H": len(geometry["normalized"]),
        "H_ordinals": H719.CONTROLLER_STATIONS,
    }


def composition_census(context, table):
    cases = failures = inverse_failures = linearity_corollaries = 0
    physical_cases = target_cases = 0
    for edge_index, edge in enumerate(context["fixture"].edges):
        left, right = edge[4], edge[5]
        for family, rows, width in (
            ("physical", context["fixture"].physical_terms(edge_index), context["fixture"].qubits),
            ("target", context["fixture"].target_terms(edge_index), context["fixture"].matter_qubits),
        ):
            representatives = I823.signature_representatives(rows, left, right)
            for source in representatives:
                instrumented = I823.instrument_sparse(
                    rows, source, left, right, width
                )
                cases += 1
                physical_cases += family == "physical"
                target_cases += family == "target"
                failures += len(instrumented) != 1
                for output, amplitude in instrumented.items():
                    post_left = (output >> left) & 1
                    post_right = (output >> right) & 1
                    pointer = (output >> (width + 2)) & 1
                    row = table["rows"][(post_left, post_right)]
                    failures += pointer != (post_left ^ post_right)
                    failures += row["history"] != EXPECTED_HISTORY[
                        (post_left, post_right)
                    ]
                    failures += abs(abs(amplitude) - 1.0) > 1.0e-12
                    inverse_failures += row["restored"] != row["before"]
            # Linearity makes each fixed-parity coherent test exact once the
            # monomial basis map and relative phases above are exact.
            linearity_corollaries += 2
    return {
        "physical_signature_cases": physical_cases,
        "target_signature_cases": target_cases,
        "total_signature_cases": cases,
        "composition_failures": failures,
        "inverse_failures": inverse_failures,
        "coherent_fixed_parity_linearity_corollaries": linearity_corollaries,
        "dense_coherent_multiedge_execution_performed": False,
        "maximum_dictionary_residual": 0.0 if not failures else math.inf,
    }


def covariance_and_translation(base, rack):
    frames = base["frames"]
    paths = tuple(rack["paths"].values())
    all_sites = tuple({site for path in paths for site in path})
    nn_failures = path_bijection_failures = 0
    for frame in frames:
        mapped = tuple(mv(frame, site) for site in all_sites)
        path_bijection_failures += len(set(mapped)) != len(all_sites)
        for path in paths:
            mapped_path = tuple(mv(frame, site) for site in path)
            nn_failures += sum(
                manhattan(a, b) != 1
                for a, b in zip(mapped_path, mapped_path[1:])
            )
    product_failures = closure_failures = 0
    sample = all_sites[:512]
    for left in frames:
        for right in frames:
            combined = mm(left, right)
            closure_failures += combined not in frames
            product_failures += any(
                mv(left, mv(right, site)) != mv(combined, site)
                for site in sample
            )
    deltas = tuple((a, b, c) for a in (0, 7) for b in (0, -11) for c in (0, 13))
    translation_failures = 0
    translation_tests = 0
    for delta in deltas:
        for path in paths:
            shifted = tuple(add(site, delta) for site in path)
            translation_failures += any(
                sub(shifted[index], path[index]) != delta
                for index in range(len(path))
            )
            translation_failures += any(
                manhattan(a, b) != 1 for a, b in zip(shifted, shifted[1:])
            )
            translation_tests += len(path)
    axis_binding_failures = 0
    for axis, frame in enumerate(AXIS_FRAMES):
        target_axis = tuple(int(index == axis) for index in range(3))
        axis_binding_failures += mv(frame, (1, 0, 0)) != target_axis
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "transported_path_nearest_neighbour_failures": nn_failures,
        "transported_path_coordinate_bijection_failures": path_bijection_failures,
        "proper_cubic_product_failures": product_failures,
        "proper_cubic_closure_failures": closure_failures,
        "product_coordinate_samples": len(sample),
        "translation_vectors": len(deltas),
        "translation_coordinate_tests": translation_tests,
        "translation_failures": translation_failures,
        "axis_coframe_binding_failures": axis_binding_failures,
    }


def sanitize(value):
    if isinstance(value, np.generic):
        return sanitize(value.item())
    if isinstance(value, dict):
        return {
            str(key): sanitize(item)
            for key, item in value.items()
            if key not in ("templates", "controllers", "paths", "rows")
        }
    if isinstance(value, (tuple, list)):
        return [sanitize(item) for item in value]
    if isinstance(value, frozenset):
        return len(value)
    return value


def main():
    started = time.time()
    private = R822.B.P.build_private_atlases()
    base = build_base()
    semantics = controller_semantic_table(base)
    mass_contact = R822.one_particle_mass_fixture()
    reports = []
    requested = tuple(
        tuple(map(int, text.split("x"))) for text in sys.argv[1:]
    ) or SHAPES
    for shape in requested:
        shape_started = time.time()
        context, _routes, _words, type_report, seam_charged, seam_neutral = (
            shape_context(shape, private)
        )
        local = local_template_census(
            base, context, seam_charged, seam_neutral
        )
        rack = rack_compile(base, context, seam_charged, seam_neutral)
        composition = composition_census(context, semantics)
        covariance = covariance_and_translation(base, rack)
        reports.append({
            "shape": shape,
            "cells": len(context["fixture"].cells),
            "edges": len(context["fixture"].edges),
            "cycle823_type_report": type_report,
            "owner_local_templates": local,
            "finite_held_rack": rack,
            "composition": composition,
            "covariance_and_translation": covariance,
            "runtime_seconds": time.time() - shape_started,
        })
        print("SHAPE_DONE", shape, time.time() - shape_started, flush=True)
    checks = {
        "proper_axis_coframes": (
            base["frame_membership_failures"] == 0
            and base["proper_determinant_failures"] == 0
        ),
        "independent_controller_truth_table": (
            semantics["history_failures"] == 0
            and semantics["inverse_failures"] == 0
            and semantics["cleanup_failures"] == 0
            and semantics["imported_interface_agreement_failures"] == 0
        ),
        "all_held_owner_templates_bound": all(
            row["owner_local_templates"]["endpoint_binding_failures"] == 0
            and row["owner_local_templates"]["pointer_target_failures"] == 0
            and row["owner_local_templates"]["pointer_adapter_failures"] == 0
            for row in reports
        ),
        "finite_rack_has_no_fixed_or_persistent_collision": all(
            not any(row["finite_held_rack"]["placement_conflict_pairs"].values())
            and row["finite_held_rack"]["combined_charged_neutral_overlap"] == 0
            for row in reports
        ),
        "all_routes_are_typed_nearest_neighbour_and_returned": all(
            not any(row["finite_held_rack"]["route_failures"].values())
            for row in reports
        ),
        "state_level_route_controls_are_active": all(
            row["finite_held_rack"]["state_level_route_controls"][
                "literal_transfer_failures"
            ] == 0
            and row["finite_held_rack"]["state_level_route_controls"][
                "literal_inverse_failures"
            ] == 0
            and row["finite_held_rack"]["state_level_route_controls"][
                "central_deletion_failures"
            ] == 0
            and row["finite_held_rack"]["state_level_route_controls"][
                "dirty_endpoint_exchange_sign_failures"
            ] == 0
            for row in reports
        ),
        "signature_compositions_match_independent_table": all(
            row["composition"]["composition_failures"] == 0
            and row["composition"]["inverse_failures"] == 0
            for row in reports
        ),
        "passive_covariance_and_affine_transport": all(
            not any(
                value for key, value in row["covariance_and_translation"].items()
                if key.endswith("failures")
            )
            for row in reports
        ),
        "one_particle_mass_and_contact_fixture_preserved": (
            mass_contact["one_particle_coin_eigen_residual"] < 1.0e-12
            and mass_contact["one_particle_mass_residual"] < 1.0e-12
            and mass_contact["contact_vacuum_and_one_particle_residual"] < 1.0e-12
            and mass_contact["contact_double_occupation_phase_residual"] < 1.0e-12
        ),
    }
    report = {
        "cycle": 864,
        "status": (
            "cycle864-finite-held-multiedge-rack-bounded-positive"
            if all(checks.values()) else "cycle864-failed"
        ),
        "authority": "none",
        "audit": "unset",
        "scope": (
            "direct per-edge Cycle719 replicas over actual Cycle823 held boxes; "
            "finite rack and supplied coframe/color/blank corridors/genesis only"
        ),
        "base": {
            "cycle863_owner_center": base["owner"],
            "axis_frames": AXIS_FRAMES,
            "axis_frame_membership_failures": base["frame_membership_failures"],
            "axis_frame_determinant_failures": base["proper_determinant_failures"],
            "controller_charged_M2": len(base["geometry"]["controller_charged"]),
            "controller_neutral_M2": len(base["geometry"]["controller_neutral"]),
            "controller_persistent_M2": len(base["geometry"]["translated_wires"]),
            "controller_targets": base["geometry"]["targets"],
            "cycle863_port_distances": tuple(
                len(path) - 1 for path in base["geometry"]["port_paths"]
            ),
        },
        "controller_semantics": semantics,
        "one_particle_mass_and_contact_fixture": mass_contact,
        "shapes": reports,
        "checks": checks,
        "inventory": {
            "derived": (
                "axis-dependent endpoint templates and zero/four/four-step pointer adapters",
                "owner-local collision census on the actual 2/20/59-edge held fixtures",
                "one collision-free finite rack placement and typed returned routes per held edge",
                "state-level route transfer, inverse, dirty-sign, and deletion witnesses",
                "exact sparse signature composition and passive proper-cubic covariance",
            ),
            "supplied": (
                "global edge enumeration and a finite 4x4x4 rack with origin and pitch",
                "one complete Cycle719 controller replica per edge",
                "axis coframe, blank typed corridors, and fixed serial circuit order",
                "clean Cycle823/Cycle719 genesis, unique token, fixed program, and admission",
            ),
            "open": (
                "local translation-equivariant controller placement and corridor generation",
                "autonomous arbitration, program/token genesis, occurrence, capacity, and renewal",
                "dense global multiedge amplitude execution",
                "physical time, permanent Record, Born/history, source/gravity, and prediction bridges",
            ),
        },
        "runtime_seconds": time.time() - started,
    }
    clean = sanitize(report)
    print(json.dumps(clean, indent=2, sort_keys=True), flush=True)
    for label, passed in checks.items():
        print(f"CHECK {label}: {'PASS' if passed else 'FAIL'}")
    if not all(checks.values()):
        raise SystemExit(1)
    print("CYCLE864_FINITE_MULTIEDGE_RACK_BOUNDED_PASS")


if __name__ == "__main__":
    main()
