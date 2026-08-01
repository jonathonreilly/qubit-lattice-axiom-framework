#!/usr/bin/env python3
"""Cycle 864 local dilated edge-service placement theorem probe.

This replaces a finite edge-index rack by the proper-cubic doubled-midpoint
address q=2*owner+axis.  The physical cell pitch is a supplied dilation of
320, so the controller anchor is the actual dilated edge midpoint 160*q.
All port corridors are finite templates selected by a supplied periodic
owner colour; no global edge enumeration is used.

The certified surface stops before recompiling the complete Cycle-822/823
intercell update/seam atlas at the new pitch.  Authority: none.  Audit: unset.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

import frontier_cycle822_routec_staggered_radius_one_parity_even_transport_2026_07_30 as R822
import frontier_cycle823_companion_full_seam_endpoint_instrument_2026_07_30 as I823
import frontier_cycle827_cycle719_parity_safe_typed_controller_atlas_2026_07_30 as C827
import frontier_cycle863_cycle823_cycle719_same_chart_history_port_2026_08_01 as C863


Coord = tuple[int, int, int]
AXIS_FRAMES = (
    ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
    ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
)
UNIT = tuple(tuple(int(index == axis) for index in range(3)) for axis in range(3))
DILATION_HALF_PITCH = 160
CELL_PITCH = 2 * DILATION_HALF_PITCH
COLOUR_MODULUS = 8
SUPPLIED_COLOUR_ORIGIN = (0, 0, 0)
SUPPLIED_PHYSICAL_ORIGIN = (0, 0, 0)
SHAPES = ((3, 2, 2), (5, 3, 2))
ROOT = Path(__file__).resolve().parents[1]
BASE_CACHE = ROOT / "outputs" / (
    "cycle864_dilated_midpoint_edge_service_base_cache_2026_08_01.json"
)
EXPECTED_BASE_CACHE_SHA256 = (
    "5966321976dceb304d78b53570912beaa458b1009994d413ccd270f9202e5e97"
)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def scale(value: int, row: Coord) -> Coord:
    return tuple(value * item for item in row)  # type: ignore[return-value]


def mv(frame, vector: Coord) -> Coord:
    return tuple(
        sum(frame[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def mm(left, right):
    return tuple(tuple(
        sum(left[row][inner] * right[inner][column] for inner in range(3))
        for column in range(3)
    ) for row in range(3))


def transpose(matrix):
    return tuple(tuple(matrix[column][row] for column in range(3)) for row in range(3))


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def waypoint_path(points: tuple[Coord, ...]) -> tuple[Coord, ...]:
    output = [points[0]]
    for source, target in zip(points, points[1:]):
        changed = [axis for axis in range(3) if source[axis] != target[axis]]
        if len(changed) != 1:
            raise AssertionError(("non-axial waypoint", source, target))
        axis = changed[0]
        step = 1 if target[axis] > source[axis] else -1
        cursor = list(source)
        while cursor[axis] != target[axis]:
            cursor[axis] += step
            output.append(tuple(cursor))
    return tuple(output)


def transport(site: Coord, old_anchor: Coord, frame, new_anchor: Coord) -> Coord:
    return add(new_anchor, mv(frame, sub(site, old_anchor)))


def transport_set(sites, old_anchor, frame, new_anchor):
    return frozenset(transport(site, old_anchor, frame, new_anchor) for site in sites)


def transport_path(path, old_anchor, frame, new_anchor):
    return tuple(transport(site, old_anchor, frame, new_anchor) for site in path)


def edge_colour(owner: Coord) -> int:
    relative = sub(owner, SUPPLIED_COLOUR_ORIGIN)
    return sum(relative) % COLOUR_MODULUS


def midpoint_code(owner: Coord, axis: int) -> Coord:
    return add(scale(2, owner), UNIT[axis])


def edge_anchor(owner: Coord, axis: int) -> Coord:
    return add(
        SUPPLIED_PHYSICAL_ORIGIN,
        scale(DILATION_HALF_PITCH, midpoint_code(owner, axis)),
    )


def cell_center(cell: Coord) -> Coord:
    return add(SUPPLIED_PHYSICAL_ORIGIN, scale(CELL_PITCH, cell))


def embed_local_template(cell: Coord, local_offset: Coord) -> Coord:
    """Uniform dilation E_D keeps every within-cell coordinate unchanged."""
    return add(cell_center(cell), local_offset)


def canonical_sources(owner: Coord, axis: int) -> tuple[Coord, Coord, Coord]:
    center = cell_center(owner)
    target = add(owner, UNIT[axis])
    return (
        sub(center, scale(4, UNIT[axis])),
        add(cell_center(target), scale(4, UNIT[axis])),
        add(center, I823.auxiliary_offset(axis, 2)),
    )


def canonical_access_paths(
    owner: Coord, axis: int, transported_sources, transported_pointer_target
):
    """Finite colour-selected paths, transported from one +x edge tube."""
    colour = edge_colour(owner)
    height = 32 + 8 * colour
    pitch = CELL_PITCH
    half = DILATION_HALF_PITCH
    reference_owner = cell_center(owner)
    # The reference paths end at the transported Cycle863 tail starts.
    left = waypoint_path((
        add(reference_owner, (-4, 0, 0)),
        add(reference_owner, (-4, height, 0)),
        add(reference_owner, (half - 4, height, 0)),
        add(reference_owner, (half - 4, 0, 0)),
    ))
    right = waypoint_path((
        add(reference_owner, (pitch + 4, 0, 0)),
        add(reference_owner, (pitch + 4, -height, 0)),
        add(reference_owner, (half + 40, -height, 0)),
        add(reference_owner, (half + 40, 0, 0)),
        add(reference_owner, (half + 20, 0, 0)),
    ))
    pointer = waypoint_path((
        add(reference_owner, (6, -6, -4)),
        add(reference_owner, (6, -24, -4)),
        add(reference_owner, (6, -24, height)),
        add(reference_owner, (half + 6, -24, height)),
        add(reference_owner, (half + 6, -24, -1)),
        add(reference_owner, (half + 6, -11, -1)),
    ))
    frame = AXIS_FRAMES[axis]
    reference_anchor = edge_anchor(owner, 0)
    anchor = edge_anchor(owner, axis)
    paths = tuple(
        transport_path(path, reference_anchor, frame, anchor)
        for path in (left, right, pointer)
    )
    # Axis-specific native Cycle823 pointer conventions differ by four sites
    # from the transported +x convention.  Attach the obstacle-free adapter.
    actual_pointer = canonical_sources(owner, axis)[2]
    if actual_pointer != paths[2][0]:
        source = actual_pointer
        target = paths[2][0]
        if axis == 1:
            adapter = waypoint_path((
                source,
                (target[0], source[1], source[2]),
                target,
            ))
        elif axis == 2:
            adapter = waypoint_path((
                source,
                (source[0], target[1], source[2]),
                target,
            ))
        else:
            raise AssertionError((axis, source, target))
        paths = paths[:2] + (adapter[:-1] + paths[2],)
    if tuple(path[0] for path in paths) != canonical_sources(owner, axis):
        raise AssertionError(("source binding", owner, axis))
    expected_targets = tuple(transported_sources[:2]) + (
        transported_pointer_target,
    )
    if tuple(path[-1] for path in paths) != expected_targets:
        raise AssertionError(("tail binding", owner, axis))
    return paths


def local_companion_offsets(private) -> tuple[Coord, ...]:
    """Extract the finite persistent cell palette without its 16-cell pitch."""
    context = R822.local_site_maps((3, 3, 3), private)
    centers = tuple(context["centers"].values())
    offsets = set()
    tie_failures = far_failures = 0
    for site in context["persistent"]:
        distances = tuple(manhattan(site, center) for center in centers)
        nearest = min(distances)
        tie_failures += distances.count(nearest) != 1
        far_failures += nearest >= 32
        offsets.add(sub(site, centers[distances.index(nearest)]))
    if tie_failures or far_failures:
        raise AssertionError(("local palette extraction", tie_failures, far_failures))
    return tuple(sorted(offsets))


def build_shape(shape, base, local_offsets, private):
    context = R822.local_site_maps(shape, private)
    fixture = context["fixture"]
    old_owner = base["old_owner"]
    geometry = base["geometry"]
    companion_persistent = {
        add(cell_center(cell), offset)
        for cell in fixture.cells for offset in local_offsets
    }
    endpoint_auxiliaries = set()
    for edge in fixture.edges:
        owner = tuple(edge[2])
        axis = int(edge[3])
        endpoint_auxiliaries.update(
            embed_local_template(owner, I823.auxiliary_offset(axis, register))
            for register in range(3)
        )
    endpoint_auxiliary_local_persistent_collisions = len(
        endpoint_auxiliaries & companion_persistent
    )
    endpoint_auxiliary_alias_failures = (
        3 * len(fixture.edges) - len(endpoint_auxiliaries)
    )
    companion_persistent.update(endpoint_auxiliaries)
    controllers = []
    edge_address_failures = source_dilation_binding_failures = 0
    full_source_template_binding_failures = 0
    unordered_keys = []
    for edge_index, edge in enumerate(fixture.edges):
        owner = tuple(edge[2])
        axis = int(edge[3])
        target_cell = add(owner, UNIT[axis])
        unordered_key = tuple(sorted((owner, target_cell)))
        unordered_keys.append(unordered_key)
        edge_address_failures += midpoint_code(owner, axis) != add(owner, target_cell)
        edge_address_failures += add(owner, target_cell) != add(target_cell, owner)
        expected_sources = (
            embed_local_template(owner, scale(-4, UNIT[axis])),
            embed_local_template(target_cell, scale(4, UNIT[axis])),
            embed_local_template(owner, I823.auxiliary_offset(axis, 2)),
        )
        source_dilation_binding_failures += canonical_sources(owner, axis) != expected_sources
        expected_auxiliaries = tuple(
            embed_local_template(owner, I823.auxiliary_offset(axis, register))
            for register in range(3)
        )
        full_source_template_binding_failures += expected_sources[2] != expected_auxiliaries[2]
        full_source_template_binding_failures += len(set(expected_auxiliaries)) != 3
        frame = AXIS_FRAMES[axis]
        anchor = edge_anchor(owner, axis)
        charged = transport_set(
            geometry["controller_charged"], old_owner, frame, anchor
        )
        neutral = transport_set(
            geometry["controller_neutral"], old_owner, frame, anchor
        )
        wires = transport_set(
            geometry["translated_wires"], old_owner, frame, anchor
        )
        tails = tuple(
            transport_path(path, old_owner, frame, anchor)
            for path in geometry["port_paths"]
        )
        access = canonical_access_paths(
            owner, axis, tuple(path[0] for path in tails), tails[2][-1]
        )
        paths = (
            access[0][:-1] + tails[0],
            access[1][:-1] + tails[1],
            access[2],
        )
        controllers.append({
            "edge_index": edge_index,
            "owner": owner,
            "axis": axis,
            "colour": edge_colour(owner),
            "midpoint_code": midpoint_code(owner, axis),
            "anchor": anchor,
            "sources": canonical_sources(owner, axis),
            "charged": charged,
            "neutral": neutral,
            "wires": wires,
            "paths": paths,
        })

    conflicts = Counter()
    conflict_sites = Counter()
    all_charged = set()
    all_neutral = set()
    all_wires = set()
    all_path_sites = set()
    path_rows = []
    own_cross_samples = []
    companion_hit_samples = []
    for index, row in enumerate(controllers):
        own_charged = set(row["charged"]) | set(row["paths"][0]) | set(row["paths"][1])
        own_neutral = set(row["neutral"]) | set(row["paths"][2])
        tests = {
            "charged_charged": own_charged & all_charged,
            "neutral_neutral": own_neutral & all_neutral,
            "charged_neutral": own_charged & all_neutral,
            "neutral_charged": own_neutral & all_charged,
            "persistent_wires": set(row["wires"]) & all_wires,
            "path_pair": set().union(*(set(path) for path in row["paths"])) & all_path_sites,
            "controller_companion": set(row["wires"]) & companion_persistent,
        }
        for label, sites in tests.items():
            conflicts[label] += bool(sites)
            conflict_sites[label] += len(sites)
        own_path_pair_sites = set().union(*(
            set(row["paths"][left]) & set(row["paths"][right])
            for left in range(3) for right in range(left)
        ))
        conflicts["own_path_pair"] += bool(own_path_pair_sites)
        conflict_sites["own_path_pair"] += len(own_path_pair_sites)
        conflicts["own_charged_neutral"] += bool(own_charged & own_neutral)
        conflict_sites["own_charged_neutral"] += len(own_charged & own_neutral)
        if own_charged & own_neutral and len(own_cross_samples) < 12:
            own_cross_samples.append((
                index, row["axis"], row["colour"],
                tuple(sorted(own_charged & own_neutral)),
            ))
        for port, path in enumerate(row["paths"]):
            internal = set(path[1:-1])
            persistent_hits = internal & companion_persistent
            conflicts["path_companion_persistent"] += bool(persistent_hits)
            conflict_sites["path_companion_persistent"] += len(persistent_hits)
            if persistent_hits and len(companion_hit_samples) < 18:
                companion_hit_samples.append((
                    index, row["axis"], row["colour"], port,
                    tuple(sorted(persistent_hits)),
                ))
            conflicts["path_repeat"] += len(path) != len(set(path))
            conflicts["path_non_nn"] += any(
                manhattan(a, b) != 1 for a, b in zip(path, path[1:])
            )
            structure = C827.route_structure(path)
            conflicts["path_route_structure"] += sum(structure[:3])
            conflicts["path_active_deletion_missing"] += (
                len(path) > 2 and not structure[3]
            )
            path_rows.append((index, port, len(path) - 1, path))
        all_charged.update(own_charged)
        all_neutral.update(own_neutral)
        all_wires.update(row["wires"])
        all_path_sites.update(*(set(path) for path in row["paths"]))

    midpoint_codes = tuple(row["midpoint_code"] for row in controllers)
    material_colours = {tuple(cell): edge_colour(tuple(cell)) for cell in fixture.cells}
    colour_local_gradient_failures = 0
    for edge in fixture.edges:
        owner = tuple(edge[2])
        axis = int(edge[3])
        target = add(owner, UNIT[axis])
        colour_local_gradient_failures += (
            material_colours[target]
            != (material_colours[owner] + 1) % COLOUR_MODULUS
        )
    flipped = dict(material_colours)
    flipped_cell = tuple(fixture.cells[len(fixture.cells) // 2])
    flipped[flipped_cell] = (flipped[flipped_cell] + 1) % COLOUR_MODULUS
    colour_flip_detected_edges = 0
    for edge in fixture.edges:
        owner = tuple(edge[2])
        axis = int(edge[3])
        target = add(owner, UNIT[axis])
        colour_flip_detected_edges += (
            flipped[target] != (flipped[owner] + 1) % COLOUR_MODULUS
        )
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "edges": len(fixture.edges),
        "shared_edge_alias_failures": (
            len(midpoint_codes) - len(set(midpoint_codes))
            + len(unordered_keys) - len(set(unordered_keys))
        ),
        "incident_label_edge_address_failures": edge_address_failures,
        "uniform_source_dilation_binding_failures": source_dilation_binding_failures,
        "uniform_full_source_template_binding_failures": (
            full_source_template_binding_failures
        ),
        "endpoint_auxiliary_coordinates": len(endpoint_auxiliaries),
        "endpoint_auxiliary_local_persistent_collisions": (
            endpoint_auxiliary_local_persistent_collisions
        ),
        "endpoint_auxiliary_alias_failures": endpoint_auxiliary_alias_failures,
        "colour_local_gradient_failures": colour_local_gradient_failures,
        "colour_single_cell_flip_detected_edges": colour_flip_detected_edges,
        "axis_counts": dict(sorted(Counter(row["axis"] for row in controllers).items())),
        "colour_counts": dict(sorted(Counter(row["colour"] for row in controllers).items())),
        "conflict_pairs": dict(sorted(conflicts.items())),
        "conflict_sites": dict(sorted(conflict_sites.items())),
        "combined_charged_neutral_overlap": len(all_charged & all_neutral),
        "own_cross_samples": tuple(own_cross_samples),
        "companion_hit_samples": tuple(companion_hit_samples),
        "controller_wire_coordinates": len(all_wires),
        "path_count": len(path_rows),
        "charged_FSWAP_routes": 2 * len(controllers),
        "neutral_SWAP_routes": len(controllers),
        "path_distance_minimum": min(row[2] for row in path_rows),
        "path_distance_maximum": max(row[2] for row in path_rows),
        "path_distance_sum": sum(row[2] for row in path_rows),
        "returned_exchange_factor_sum": sum(2 * row[2] - 1 for row in path_rows),
        "anchor_sha256": sha256(repr(tuple(
            (row["owner"], row["axis"], row["colour"], row["anchor"])
            for row in controllers
        )).encode()).hexdigest(),
        "path_sha256": sha256(repr(tuple(path_rows)).encode()).hexdigest(),
        "controllers": controllers,
    }


def covariance(base, reports):
    frames = base["frames"]
    sample_report = reports[-1]
    controllers = sample_report["controllers"]
    all_paths = tuple(path for row in controllers for path in row["paths"])
    all_anchors = tuple(row["anchor"] for row in controllers)
    nn_failures = bijection_failures = 0
    for frame in frames:
        mapped_anchors = tuple(mv(frame, anchor) for anchor in all_anchors)
        bijection_failures += len(mapped_anchors) != len(set(mapped_anchors))
        for path in all_paths:
            mapped = tuple(mv(frame, site) for site in path)
            nn_failures += any(
                manhattan(a, b) != 1 for a, b in zip(mapped, mapped[1:])
            )
    closure_failures = product_failures = 0
    samples = tuple(site for path in all_paths[:12] for site in path[:32])
    for left in frames:
        for right in frames:
            combined = mm(left, right)
            closure_failures += combined not in frames
            product_failures += any(
                mv(left, mv(right, site)) != mv(combined, site)
                for site in samples
            )

    midpoint_equivariance_failures = 0
    material_colour_frame_failures = axis_frame_action_failures = 0
    # Test canonical edge reorientation, including sign flips.  The doubled
    # midpoint is independent of which endpoint becomes the canonical owner.
    for frame in frames:
        for owner in product(range(-1, 2), repeat=3):
            owner = tuple(owner)
            for axis in range(3):
                q = midpoint_code(owner, axis)
                direction = mv(frame, UNIT[axis])
                transported_edge_frame = mm(frame, AXIS_FRAMES[axis])
                axis_frame_action_failures += (
                    mv(transported_edge_frame, UNIT[0]) != direction
                )
                # Colour is evaluated in the supplied material coframe.  The
                # coframe and origin co-transform, so signed lab axes do not
                # alter the retained material coordinate or colour.
                relative = sub(owner, SUPPLIED_COLOUR_ORIGIN)
                lab_relative = mv(frame, relative)
                recovered_material = mv(transpose(frame), lab_relative)
                material_colour_frame_failures += recovered_material != relative
                material_colour_frame_failures += (
                    sum(recovered_material) % COLOUR_MODULUS
                    != edge_colour(owner)
                )
                mapped_owner = mv(frame, owner)
                new_axis = next(i for i, value in enumerate(direction) if value)
                if direction[new_axis] < 0:
                    mapped_owner = sub(mapped_owner, UNIT[new_axis])
                midpoint_equivariance_failures += (
                    midpoint_code(mapped_owner, new_axis) != mv(frame, q)
                )

    translations = tuple(product((-2, 0, 3), repeat=3))
    translation_failures = translation_tests = 0
    translation_path_coordinate_failures = 0
    translation_path_coordinate_tests = 0
    for delta in translations:
        delta = tuple(delta)
        physical_delta = scale(CELL_PITCH, delta)
        for row in controllers:
            shifted_owner = add(row["owner"], delta)
            shifted_anchor = edge_anchor(shifted_owner, row["axis"])
            translation_failures += shifted_anchor != add(row["anchor"], physical_delta)
            translation_tests += 1
            # Translate the supplied colour origin with the fixture.  The
            # retained material colour then follows the edge without change.
            shifted_colour_origin = add(SUPPLIED_COLOUR_ORIGIN, delta)
            shifted_colour = sum(sub(shifted_owner, shifted_colour_origin)) % COLOUR_MODULUS
            translation_failures += shifted_colour != row["colour"]
            translation_tests += 1
        for path in all_paths:
            shifted = tuple(add(site, physical_delta) for site in path)
            translation_path_coordinate_failures += any(
                sub(shifted[index], path[index]) != physical_delta
                for index in range(len(path))
            )
            translation_path_coordinate_failures += any(
                manhattan(a, b) != 1 for a, b in zip(shifted, shifted[1:])
            )
            translation_path_coordinate_tests += len(path)
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "transported_path_nearest_neighbour_failures": nn_failures,
        "transported_anchor_bijection_failures": bijection_failures,
        "proper_cubic_closure_failures": closure_failures,
        "proper_cubic_product_failures": product_failures,
        "doubled_midpoint_equivariance_failures": midpoint_equivariance_failures,
        "material_colour_frame_failures": material_colour_frame_failures,
        "axis_frame_action_failures": axis_frame_action_failures,
        "translation_vectors": len(translations),
        "translation_tests": translation_tests,
        "translation_failures": translation_failures,
        "translation_path_coordinate_tests": translation_path_coordinate_tests,
        "translation_path_coordinate_failures": translation_path_coordinate_failures,
        "collision_invariance_identity": (
            "for every signed-permutation frame/translation T, injectivity gives "
            "T(A) intersect T(B)=T(A intersect B); base-box zero intersections "
            "therefore remain exactly zero"
        ),
    }


def local_template_bounds(base):
    geometry = base["geometry"]
    old_owner = base["old_owner"]
    maximum_distance = maximum_chebyshev_radius = maximum_support = 0
    maximum_three_route_one_pass = maximum_forward_port_factors = 0
    rows = []
    for colour in range(COLOUR_MODULUS):
        owner = (colour, 0, 0)
        for axis in range(3):
            frame = AXIS_FRAMES[axis]
            anchor = edge_anchor(owner, axis)
            tails = tuple(
                transport_path(path, old_owner, frame, anchor)
                for path in geometry["port_paths"]
            )
            access = canonical_access_paths(
                owner, axis, tuple(path[0] for path in tails), tails[2][-1]
            )
            paths = (
                access[0][:-1] + tails[0],
                access[1][:-1] + tails[1],
                access[2],
            )
            charged = set(transport_set(
                geometry["controller_charged"], old_owner, frame, anchor
            )) | set(paths[0]) | set(paths[1])
            neutral = set(transport_set(
                geometry["controller_neutral"], old_owner, frame, anchor
            )) | set(paths[2])
            distances = tuple(len(path) - 1 for path in paths)
            support = charged | neutral
            radius = max(
                max(abs(value) for value in sub(site, anchor)) for site in support
            )
            one_pass = sum(2 * distance - 1 for distance in distances)
            forward = (
                2 * (2 * distances[0] - 1)
                + 2 * (2 * distances[1] - 1)
                + (2 * distances[2] - 1)
            )
            maximum_distance = max(maximum_distance, *distances)
            maximum_chebyshev_radius = max(maximum_chebyshev_radius, radius)
            maximum_support = max(maximum_support, len(support))
            maximum_three_route_one_pass = max(maximum_three_route_one_pass, one_pass)
            maximum_forward_port_factors = max(maximum_forward_port_factors, forward)
            rows.append((colour, axis, distances, len(support), radius, one_pass, forward))
    return {
        "finite_template_variants": len(rows),
        "maximum_single_port_distance": maximum_distance,
        "maximum_single_returned_macro_factors": 2 * maximum_distance - 1,
        "maximum_three_route_one_pass_factors": maximum_three_route_one_pass,
        "maximum_forward_load_return_factors": maximum_forward_port_factors,
        "maximum_typed_support_coordinates_per_edge": maximum_support,
        "maximum_chebyshev_radius_about_edge_midpoint": maximum_chebyshev_radius,
        "size_independent": True,
        "rows_sha256": sha256(repr(tuple(rows)).encode()).hexdigest(),
    }


def sanitize(value):
    if isinstance(value, dict):
        return {
            str(key): sanitize(item)
            for key, item in value.items()
            if key != "controllers"
        }
    if isinstance(value, (tuple, list)):
        return [sanitize(item) for item in value]
    return value


def cached_base():
    frames = tuple(
        tuple(tuple(int(value) for value in row) for row in frame)
        for frame in R822.B.V.T.proper_cubic_frames()
    )
    if BASE_CACHE.exists():
        cache_sha256 = sha256(BASE_CACHE.read_bytes()).hexdigest()
        if cache_sha256 != EXPECTED_BASE_CACHE_SHA256:
            raise AssertionError(("base cache digest", cache_sha256))
        payload = json.loads(BASE_CACHE.read_text())
        geometry = {
            "controller_charged": frozenset(map(tuple, payload["controller_charged"])),
            "controller_neutral": frozenset(map(tuple, payload["controller_neutral"])),
            "translated_wires": tuple(map(tuple, payload["translated_wires"])),
            "port_paths": tuple(
                tuple(map(tuple, path)) for path in payload["port_paths"]
            ),
        }
        return {
            "geometry": geometry,
            "old_owner": tuple(payload["old_owner"]),
            "frames": frames,
            "cache": "reused",
            "cache_sha256": cache_sha256,
            "cache_digest_matches_reconstruction_pin": True,
        }
    geometry = C863.joint_geometry()
    old_owner = geometry["context"]["centers"][
        geometry["context"]["fixture"].edges[C863.EDGE_INDEX][2]
    ]
    payload = {
        "old_owner": old_owner,
        "controller_charged": tuple(sorted(geometry["controller_charged"])),
        "controller_neutral": tuple(sorted(geometry["controller_neutral"])),
        "translated_wires": geometry["translated_wires"],
        "port_paths": geometry["port_paths"],
    }
    BASE_CACHE.write_text(json.dumps(payload, sort_keys=True) + "\n")
    cache_sha256 = sha256(BASE_CACHE.read_bytes()).hexdigest()
    if cache_sha256 != EXPECTED_BASE_CACHE_SHA256:
        raise AssertionError(("generated base cache digest", cache_sha256))
    return {
        "geometry": geometry,
        "old_owner": old_owner,
        "frames": frames,
        "cache": "generated",
        "cache_sha256": cache_sha256,
        "cache_digest_matches_reconstruction_pin": True,
    }


def main():
    private = R822.B.P.build_private_atlases()
    base = cached_base()
    geometry = base["geometry"]
    local_offsets = local_companion_offsets(private)
    reports = tuple(
        build_shape(shape, base, local_offsets, private) for shape in SHAPES
    )
    covariant = covariance(base, reports)
    bounds = local_template_bounds(base)
    report = {
        "status": "cycle864-local-dilated-edge-midpoint-controller-port-placement-pass",
        "rule": {
            "doubled_midpoint": (
                "q=n_left+n_right=2*canonical_owner+positive_axis_unit; "
                "computed from the unordered incident-cell labels"
            ),
            "controller_anchor": "physical_origin+160*q",
            "cell_pitch": CELL_PITCH,
            "half_pitch": DILATION_HALF_PITCH,
            "uniform_source_embedding": "E_D(cell,local)=physical_origin+320*cell+local",
            "colour": (
                "material kappa=sum(owner-colour_origin) mod 8 in the supplied "
                "coframe; origin and coframe co-transform"
            ),
            "physical_origin_genesis": "SUPPLIED",
            "colour_origin_genesis": "SUPPLIED",
            "coframe_genesis": "SUPPLIED proper cubic frame",
            "blank_typed_corridor_genesis": "SUPPLIED",
            "global_edge_enumeration": False,
            "exact_symmetry_group": (
                "coarse translations 320*Z^3 semidirect proper-cubic 24-frame "
                "action on the supplied material coframe; no unit-lattice translation claim"
            ),
        },
        "base": {
            "old_owner": base["old_owner"],
            "controller_charged": len(geometry["controller_charged"]),
            "controller_neutral": len(geometry["controller_neutral"]),
            "controller_wires": len(geometry["translated_wires"]),
            "local_companion_offsets": len(local_offsets),
            "cache_mode": base["cache"],
            "cache_sha256": base["cache_sha256"],
            "cache_digest_matches_reconstruction_pin": base[
                "cache_digest_matches_reconstruction_pin"
            ],
            "source_sha256": {
                "Cycle822": sha256(Path(R822.__file__).read_bytes()).hexdigest(),
                "Cycle823": sha256(Path(I823.__file__).read_bytes()).hexdigest(),
                "Cycle827": sha256(Path(C827.__file__).read_bytes()).hexdigest(),
                "Cycle863": sha256(Path(C863.__file__).read_bytes()).hexdigest(),
            },
        },
        "shapes": reports,
        "covariance": covariant,
        "size_independent_local_bounds": bounds,
        "claim_boundary": {
            "certified_here": (
                "uniformly dilated actual per-cell persistent/source templates, "
                "one Cycle827 controller atlas per unordered actual edge, and "
                "typed FSWAP/SWAP controller-port corridors"
            ),
            "cycle823_full_typed_update_at_pitch_320": (
                "NOT recompiled; intercell Cycle822/823 seam/update corridors are "
                "outside this placement certificate"
            ),
            "mass_contact": (
                "not numerically rerun; preservation is only the conditional semantic "
                "conjugation corollary if the dilated Cycle823 update is separately compiled"
            ),
        },
        "route_a_owner_local_comparison": {
            "3x1x1": {
                "persistent_conflict_pairs": 1,
                "persistent_conflict_sites": 18,
                "cross_type_conflict_pairs": 1,
                "cross_type_conflict_sites": 26,
                "global_cross_type_coordinates": 26,
            },
            "3x2x2": {
                "persistent_conflict_pairs": 48,
                "persistent_conflict_sites": 54246,
                "cross_type_conflict_pairs": 66,
                "cross_type_conflict_sites": 2073,
                "global_cross_type_coordinates": 1439,
            },
            "5x3x2": {
                "persistent_conflict_pairs": 309,
                "persistent_conflict_sites": 269187,
                "cross_type_conflict_pairs": 433,
                "cross_type_conflict_sites": 12967,
                "global_cross_type_coordinates": 5499,
            },
            "comparison_only_global_rack_not_imported": (
                "Route A slot(i)=(256,256,256)+160*(i mod4, floor(i/4) mod4, floor(i/16))"
            ),
        },
    }
    sanitized = sanitize(report)
    conflict_total = sum(
        sum(shape["conflict_sites"].values()) for shape in sanitized["shapes"]
    )
    covariance_failures = sum(
        value for key, value in sanitized["covariance"].items()
        if key.endswith("failures")
    )
    covariance_coverage = (
        sanitized["covariance"]["proper_cubic_frames"] == 24
        and sanitized["covariance"]["ordered_frame_products"] == 576
        and sanitized["covariance"]["translation_vectors"] == 27
        and sanitized["covariance"]["translation_path_coordinate_tests"]
        == 1429515
    )
    local_rule_failures = sum(
        shape["shared_edge_alias_failures"]
        + shape["incident_label_edge_address_failures"]
        + shape["uniform_source_dilation_binding_failures"]
        + shape["uniform_full_source_template_binding_failures"]
        + shape["endpoint_auxiliary_local_persistent_collisions"]
        + shape["endpoint_auxiliary_alias_failures"]
        + shape["colour_local_gradient_failures"]
        + (shape["colour_single_cell_flip_detected_edges"] == 0)
        for shape in sanitized["shapes"]
    )
    sanitized["pass"] = (
        conflict_total == 0 and covariance_failures == 0
        and covariance_coverage and local_rule_failures == 0
    )
    serial = json.dumps(sanitized, sort_keys=True, separators=(",", ":"))
    sanitized["report_sha256"] = sha256(serial.encode()).hexdigest()
    print(json.dumps(sanitized, sort_keys=True, indent=2))
    print(
        "CYCLE864_LOCAL_DILATED_SERVICE_PASS"
        if sanitized["pass"] else "CYCLE864_LOCAL_DILATED_SERVICE_FAIL"
    )
    if not sanitized["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
