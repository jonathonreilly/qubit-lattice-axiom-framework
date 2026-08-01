#!/usr/bin/env python3
"""Cycle 863: one-edge same-chart Cycle823-to-Cycle719 history port.

This runner moves the actual Cycle823 endpoint occupations into a translated
Cycle719 controller with FSWAP, moves the neutral opportunity pointer with
SWAP, executes the complete normalized controller orbit, and returns the
endpoint occupations.  The construction is a fixed first-use finite port.  It
does not make the controller program, admission sector, atlas, or occurrence
autonomous, and its 130 circuit applications are not physical time.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import time

import numpy as np

import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as H719
import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M720
import frontier_cycle822_routec_staggered_radius_one_parity_even_transport_2026_07_30 as R822
import frontier_cycle823_companion_full_seam_endpoint_instrument_2026_07_30 as I823
import frontier_cycle826_companion_endpoint_cycle719_history_interface_2026_07_30 as I826
import frontier_cycle827_cycle719_parity_safe_typed_controller_atlas_2026_07_30 as C827


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    "docs/CYCLE823_CYCLE719_SAME_CHART_HISTORY_PORT_"
    "CYCLE863_BOUNDED_THEOREM_NOTE_2026-08-01.md"
)
RUNNER_PATH = (
    "scripts/frontier_cycle863_cycle823_cycle719_same_chart_history_"
    "port_2026_08_01.py"
)
RECEIPT_PATH = (
    "outputs/cycle823_cycle719_same_chart_history_port_"
    "cycle863_receipt_2026_08_01.json"
)
AUDIT_INPUT_PATHS = (
    NOTE_PATH,
    RUNNER_PATH,
    RECEIPT_PATH,
    "docs/COMPANION_FULL_SEAM_ENDPOINT_INSTRUMENT_"
    "CYCLE823_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "scripts/frontier_cycle823_companion_full_seam_endpoint_"
    "instrument_2026_07_30.py",
    "docs/COMPANION_ENDPOINT_CYCLE719_HISTORY_INTERFACE_"
    "CYCLE826_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "scripts/frontier_cycle826_companion_endpoint_cycle719_history_"
    "interface_2026_07_30.py",
    "docs/CYCLE719_PARITY_SAFE_TYPED_CONTROLLER_ATLAS_"
    "CYCLE827_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "scripts/frontier_cycle827_cycle719_parity_safe_typed_controller_"
    "atlas_2026_07_30.py",
    "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_"
    "CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "scripts/frontier_cycle719_recurrent_matter_history_"
    "controller_2026_07_26.py",
    "docs/RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_"
    "CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "docs/ROUTEC_STAGGERED_RADIUS_ONE_PARITY_EVEN_TRANSPORT_"
    "CYCLE822_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "scripts/frontier_cycle822_routec_staggered_radius_one_parity_even_"
    "transport_2026_07_30.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

SHAPE = (2, 1, 1)
EDGE_INDEX = 0
CONTROLLER_TRANSLATION = (6, -10, -2)
PORT_WAYPOINTS = (
    (
        (-12, 0, 0), (-7, 0, 0), (-7, -1, 0), (1, -1, 0),
        (1, -12, 0), (1, -12, -2), (0, -12, -2),
    ),
    (
        (12, 0, 0), (11, 0, 0), (11, -1, 0), (2, -1, 0),
        (2, -10, 0), (2, -10, 1), (-2, -10, 1),
        (-2, -10, 0), (-4, -10, 0),
    ),
    (
        (-2, -6, -4), (-2, -7, -4), (-2, -7, -3),
        (-2, -10, -3), (-2, -10, -1), (-2, -11, -1),
    ),
)
TOL = 3.0e-11
STAGE_MANIFEST = (
    "Cycle823 prefix/prewrite/seam/postwrite-clean",
    "two charged endpoint transfer macros",
    "one neutral pointer transfer macro",
    "normalized Cycle719 H repeated 130 circuit ordinals",
    "two charged endpoint return macros",
    "Cycle823 contact",
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def matvec(matrix, vector):
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )


def matmul(left, right):
    return tuple(tuple(
        sum(left[row][inner] * right[inner][column] for inner in range(3))
        for column in range(3)
    ) for row in range(3))


def waypoint_path(points):
    output = [points[0]]
    for source, target in zip(points, points[1:]):
        changed = tuple(
            axis for axis in range(3) if source[axis] != target[axis]
        )
        if len(changed) != 1:
            raise ValueError(("non-axial waypoint segment", source, target))
        axis = changed[0]
        step = 1 if target[axis] > source[axis] else -1
        current = list(source)
        while current[axis] != target[axis]:
            current[axis] += step
            output.append(tuple(current))
    return tuple(output)


def state_residual(left, right) -> float:
    keys = set(left) | set(right)
    return float(math.sqrt(sum(
        abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2
        for key in keys
    )))


def apply_two_site(state, matrix, first: int, second: int):
    output = defaultdict(complex)
    clear = ~((1 << first) | (1 << second))
    for basis, amplitude in state.items():
        local = ((basis >> first) & 1) | (((basis >> second) & 1) << 1)
        base = basis & clear
        for target in range(4):
            coefficient = matrix[target, local]
            if abs(coefficient) < 1.0e-15:
                continue
            word = (
                base
                | ((target & 1) << first)
                | (((target >> 1) & 1) << second)
            )
            output[word] += coefficient * amplitude
    return {
        basis: amplitude for basis, amplitude in output.items()
        if abs(amplitude) > 1.0e-13
    }


def route_sequence(path):
    edges = tuple(zip(path, path[1:]))
    return edges[:-1] + edges[-1:] + tuple(reversed(edges[:-1]))


def apply_route(state, path, matrix, site_bits, *, delete_ordinal=None):
    for ordinal, (left, right) in enumerate(route_sequence(path)):
        if ordinal == delete_ordinal:
            continue
        state = apply_two_site(
            state, matrix, site_bits[left], site_bits[right]
        )
    return state


def controller_genesis(*, tokens=(0,), rejected_field=None):
    banks, links = H719.B.chain_genesis(H719.BANKS)
    if rejected_field is not None:
        mutable = list(banks)
        selected = list(mutable[0])
        selected[rejected_field] = 0
        mutable[0] = tuple(selected)
        banks = tuple(mutable)
    data = H719.tuple_to_int(H719.M.pack_state(banks, links))
    for station in tokens:
        data |= 1 << (H719.CONTROLLER_A_BASE + station)
    return data


def joint_geometry():
    private = R822.B.P.build_private_atlases()
    context = I823.augment_context(R822.local_site_maps(SHAPE, private))
    context, base_routes, base_words, *_rest = R822.fixed_typed_compile(context)
    routes = list(base_routes)
    before, after = I823.instrument_words(context, routes)
    words = I823.combined_word_order(base_words, before, after)
    type_report, seam_charged, seam_neutral = R822.fixed_type_assignment(
        context, tuple(routes)
    )

    block = H719.physical_controller_block(H719.BANKS)
    normalized, swaps, equivalence_failures = C827.normalize_word(
        block["semantic"]
    )
    controller_atlas = C827.typed_atlas(normalized, block["wire_sites"])
    translated_wires = tuple(
        add(site, CONTROLLER_TRANSLATION) for site in block["wire_sites"]
    )
    controller_charged = frozenset(
        add(site, CONTROLLER_TRANSLATION)
        for site in controller_atlas["fixed_charged"]
    )
    controller_neutral = frozenset(
        add(site, CONTROLLER_TRANSLATION)
        for site in controller_atlas["fixed_neutral"]
    )
    controller_paths = {
        pair: tuple(add(site, CONTROLLER_TRANSLATION) for site in path)
        for pair, path in controller_atlas["paths"].items()
    }

    edge = context["fixture"].edges[EDGE_INDEX]
    sources = (
        context["o_sites"][edge[4]],
        context["o_sites"][edge[5]],
        context["endpoint_auxiliaries"][EDGE_INDEX][2],
    )
    targets = (
        translated_wires[H719.M.R3.X.LEFT_ENDPOINT],
        translated_wires[H719.M.R3.X.RIGHT_ENDPOINT],
        translated_wires[H719.R3_SOURCE_POINTER()],
    )
    persistent = set(context["persistent"]) | set(translated_wires)
    port_paths = [waypoint_path(points) for points in PORT_WAYPOINTS]
    if tuple(path[0] for path in port_paths) != sources:
        raise AssertionError(("port source binding", sources))
    if tuple(path[-1] for path in port_paths) != targets:
        raise AssertionError(("port target binding", targets))
    charged = (
        set(seam_charged) | set(controller_charged)
        | set(port_paths[0]) | set(port_paths[1])
    )
    pointer_path = port_paths[2]
    neutral = set(seam_neutral) | set(controller_neutral) | set(pointer_path)

    return {
        "context": context,
        "seam_routes": tuple(routes),
        "seam_words": words,
        "seam_type_report": type_report,
        "seam_charged": seam_charged,
        "seam_neutral": seam_neutral,
        "block": block,
        "normalized": normalized,
        "normalization_swaps": swaps,
        "normalization_equivalence_failures": equivalence_failures,
        "controller_atlas": controller_atlas,
        "controller_paths": controller_paths,
        "translated_wires": translated_wires,
        "controller_charged": controller_charged,
        "controller_neutral": controller_neutral,
        "sources": sources,
        "targets": targets,
        "port_paths": tuple(port_paths),
        "persistent": frozenset(persistent),
        "charged": frozenset(charged),
        "neutral": frozenset(neutral),
    }


def geometry_certificate(geometry):
    paths = geometry["port_paths"]
    seam_charged = geometry["seam_charged"]
    seam_neutral = geometry["seam_neutral"]
    controller_charged = geometry["controller_charged"]
    controller_neutral = geometry["controller_neutral"]
    persistent = geometry["persistent"]
    base_fixed = (
        set(seam_charged) | set(seam_neutral)
        | set(controller_charged) | set(controller_neutral)
    )
    path_pairs = tuple(
        len(set(paths[left]) & set(paths[right]))
        for left in range(3) for right in range(left + 1, 3)
    )
    internal_persistent_hits = tuple(
        len(set(path[1:-1]) & set(persistent)) for path in paths
    )
    type_forbidden_hits = (
        len(set(paths[0]) & (set(seam_neutral) | set(controller_neutral))),
        len(set(paths[1]) & (set(seam_neutral) | set(controller_neutral))),
        len(set(paths[2]) & geometry["charged"]),
    )
    new_sites = tuple(len(set(path) - base_fixed) for path in paths)
    distances = tuple(len(path) - 1 for path in paths)
    returned_gates = tuple(2 * distance - 1 for distance in distances)
    return {
        "shape": SHAPE,
        "edge_index": EDGE_INDEX,
        "controller_translation": CONTROLLER_TRANSLATION,
        "cycle823_endpoint_and_pointer_sites": geometry["sources"],
        "translated_controller_endpoint_and_pointer_sites": geometry["targets"],
        "port_route_distances": distances,
        "port_returned_macro_gates": returned_gates,
        "forward_port_gate_count": 2 * sum(returned_gates[:2]) + returned_gates[2],
        "path_pair_intersections": path_pairs,
        "internal_persistent_hits": internal_persistent_hits,
        "forbidden_cross_type_path_hits": type_forbidden_hits,
        "path_repeat_failures": tuple(
            len(path) - len(set(path)) for path in paths
        ),
        "nearest_neighbour_failures": tuple(sum(
            R822.S789.manhattan(left, right) != 1
            for left, right in zip(path, path[1:])
        ) for path in paths),
        "new_fixed_coordinates_per_path": new_sites,
        "cycle823_controller_persistent_collisions": len(
            set(geometry["context"]["persistent"])
            & set(geometry["translated_wires"])
        ),
        "separate_atlas_same_type_collisions": (
            len(set(seam_charged) & set(controller_charged)),
            len(set(seam_neutral) & set(controller_neutral)),
        ),
        "separate_atlas_cross_type_collisions": (
            len(set(seam_charged) & set(controller_neutral)),
            len(set(seam_neutral) & set(controller_charged)),
        ),
        "combined_charged_coordinates": len(geometry["charged"]),
        "combined_neutral_coordinates": len(geometry["neutral"]),
        "combined_charged_neutral_overlap": len(
            geometry["charged"] & geometry["neutral"]
        ),
        "port_path_sha256": sha256(repr(paths).encode()).hexdigest(),
    }


def schedule_certificate(geometry):
    port_charged_internal = set().union(*(
        set(path[1:-1]) for path in geometry["port_paths"][:2]
    ))
    port_neutral_internal = set(geometry["port_paths"][2][1:-1])
    existing_charged = (
        set(geometry["seam_charged"])
        | set(geometry["controller_charged"])
    )
    existing_neutral = (
        set(geometry["seam_neutral"])
        | set(geometry["controller_neutral"])
    )
    charged_reuse = port_charged_internal & existing_charged
    neutral_reuse = port_neutral_internal & existing_neutral
    base_stages = tuple(word.stage for word in geometry["seam_words"])
    endpoint_post_indices = tuple(
        index for index, stage in enumerate(base_stages)
        if stage == "endpoint_post_or_clean"
    )
    contact_indices = tuple(
        index for index, stage in enumerate(base_stages)
        if stage == "recurrent_contact"
    )
    # Endpoint routes in each transfer layer may be parallel because they are
    # disjoint.  Every other top-level resource use is serial.  Cycle823's own
    # fixed stage/colour/slot collision graph remains an inherited subcheck.
    controller_sites = set().union(*(
        set(path) for path in geometry["controller_paths"].values()
    ))
    contact_sites = {
        site for word in geometry["seam_words"]
        if word.stage == "recurrent_contact"
        for primitive in word.primitives for site in primitive.sites
    }
    seam_sites = {
        site for word in geometry["seam_words"]
        if word.stage != "recurrent_contact"
        for primitive in word.primitives for site in primitive.sites
    }
    scheduled_rows = (
        (0, "cycle823_through_postwrite", seam_sites),
        (1, "left_in", set(geometry["port_paths"][0])),
        (1, "right_in", set(geometry["port_paths"][1])),
        (2, "pointer_in", set(geometry["port_paths"][2])),
        (3, "controller", controller_sites),
        (4, "right_out", set(geometry["port_paths"][1])),
        (4, "left_out", set(geometry["port_paths"][0])),
        (5, "contact", contact_sites),
    )
    top_level_collision_edges = sum(
        bool(left_sites & right_sites)
        for index, (left_ordinal, _left_label, left_sites) in enumerate(
            scheduled_rows
        )
        for right_ordinal, _right_label, right_sites in scheduled_rows[index + 1:]
        if left_ordinal == right_ordinal
    )
    seam_collision_edges = R822.collision_graph(
        geometry["seam_words"]
    )["edges"]
    stage_aware_collision_edges = top_level_collision_edges + seam_collision_edges
    erased_stage_reuse = charged_reuse | neutral_reuse
    controller = geometry["controller_atlas"]
    return {
        "manifest": STAGE_MANIFEST,
        "manifest_sha256": sha256(repr(STAGE_MANIFEST).encode()).hexdigest(),
        "endpoint_post_words": len(endpoint_post_indices),
        "contact_words": len(contact_indices),
        "endpoint_post_precedes_contact": bool(
            endpoint_post_indices and contact_indices
            and max(endpoint_post_indices) < min(contact_indices)
        ),
        "distinct_serial_stage_ordinals": len(set(
            ordinal for ordinal, _label, _sites in scheduled_rows
        )),
        "top_level_scheduled_resource_rows": len(scheduled_rows),
        "cycle823_stage_colour_slot_collision_edges": seam_collision_edges,
        "stage_aware_collision_edges": stage_aware_collision_edges,
        "charged_same_type_corridor_reuse": len(charged_reuse),
        "neutral_same_type_corridor_reuse": len(neutral_reuse),
        "erased_stage_reuse_coordinates": len(erased_stage_reuse),
        "controller_route_return_failures": controller["route_return_failures"],
        "controller_charged_corridor_persistent_hits": controller[
            "charged_corridor_persistent_hits"
        ],
        "stage_labels_are_physical_time": False,
        "schedule_scope": (
            "supplied serial circuit order separating same-type workspace reuse; "
            "no counter or duration variable"
        ),
    }


def site_bit_map(geometry):
    site_bits = {
        site: wire for wire, site in enumerate(geometry["translated_wires"])
    }
    next_bit = H719.CONTROLLER_FULL_WIDTH
    for site in geometry["context"]["o_sites"]:
        if site not in site_bits:
            site_bits[site] = next_bit
            next_bit += 1
    for site in geometry["context"]["endpoint_auxiliaries"][EDGE_INDEX]:
        if site not in site_bits:
            site_bits[site] = next_bit
            next_bit += 1
    for path in geometry["port_paths"]:
        for site in path:
            if site not in site_bits:
                site_bits[site] = next_bit
                next_bit += 1
    return site_bits


def embed_instrument_state(
    geometry, site_bits, instrumented, width, *, controller=None
):
    base = controller_genesis() if controller is None else controller
    output = defaultdict(complex)
    o_sites = geometry["context"]["o_sites"]
    auxiliaries = geometry["context"]["endpoint_auxiliaries"][EDGE_INDEX]
    for basis, amplitude in instrumented.items():
        word = base
        for qubit in range(width):
            word |= ((basis >> qubit) & 1) << site_bits[o_sites[qubit]]
        for register, site in enumerate(auxiliaries):
            word |= ((basis >> (width + register)) & 1) << site_bits[site]
        output[word] += amplitude
    return dict(output)


def extract_matter(geometry, site_bits, basis, width):
    return sum(
        ((basis >> site_bits[geometry["context"]["o_sites"][qubit]]) & 1)
        << qubit
        for qubit in range(width)
    )


def decode_history(basis):
    data = H719.int_to_tuple(basis & H719.CONTROLLER_DATA_MASK)
    banks, links = H719.M.unpack_state(data, H719.BANKS)
    chain, _order = H719.B.decode_local_graph(banks, links)
    return tuple(cell.orientation for cell in chain.cells)


def controller_tables(inputs, normalized_fast):
    forward = {}
    inverse = {}
    for value in sorted(inputs):
        observed = H719.repeated_fast_word(value, normalized_fast)
        restored = H719.repeated_fast_word(
            observed, tuple(reversed(normalized_fast))
        )
        forward[value] = observed
        inverse[observed] = restored
    return forward, inverse


def apply_controller_table(state, table):
    output = defaultdict(complex)
    high_mask = ~((1 << H719.CONTROLLER_FULL_WIDTH) - 1)
    low_mask = (1 << H719.CONTROLLER_FULL_WIDTH) - 1
    for basis, amplitude in state.items():
        low = basis & low_mask
        output[(basis & high_mask) | table[low]] += amplitude
    return dict(output)


def port_in(state, geometry, site_bits):
    fswap = R822.primitive_matrix("FSWAP")
    swap = R822.primitive_matrix("SWAP")
    state = apply_route(state, geometry["port_paths"][0], fswap, site_bits)
    state = apply_route(state, geometry["port_paths"][1], fswap, site_bits)
    return apply_route(state, geometry["port_paths"][2], swap, site_bits)


def endpoint_return(state, geometry, site_bits):
    fswap = R822.primitive_matrix("FSWAP")
    state = apply_route(state, geometry["port_paths"][1], fswap, site_bits)
    return apply_route(state, geometry["port_paths"][0], fswap, site_bits)


def physical_intertwiner_certificate(geometry):
    context = geometry["context"]
    fixture = context["fixture"]
    edge = fixture.edges[EDGE_INDEX]
    left, right = edge[4], edge[5]
    site_bits = site_bit_map(geometry)
    normalized_fast = H719.fast_classical_word(geometry["normalized"])
    corridor_bits = tuple(
        site_bits[site] for path in geometry["port_paths"]
        for site in path[1:-1]
    )

    def corridor_cleanliness_failures(state):
        return sum(
            any((basis >> bit) & 1 for bit in corridor_bits)
            for basis in state
        )

    cases = []
    prepared = []
    controller_inputs = set()
    for family, rows, width in (
        ("physical", fixture.physical_terms(EDGE_INDEX), fixture.qubits),
        ("target", fixture.target_terms(EDGE_INDEX), fixture.matter_qubits),
    ):
        for source in I823.signature_representatives(rows, left, right):
            instrumented = I823.instrument_sparse(
                rows, source, left, right, width
            )
            embedded = embed_instrument_state(
                geometry, site_bits, instrumented, width
            )
            transferred = port_in(embedded, geometry, site_bits)
            controller_inputs.update(
                basis & ((1 << H719.CONTROLLER_FULL_WIDTH) - 1)
                for basis in transferred
            )
            prepared.append((family, rows, width, source, embedded, transferred))
    forward_table, inverse_table = controller_tables(
        controller_inputs, normalized_fast
    )

    maximum_residual = maximum_inverse_residual = 0.0
    cleanup_failures = token_failures = endpoint_failures = 0
    port_in_corridor_failures = port_out_corridor_failures = 0
    inverse_corridor_failures = 0
    physical_cases = target_cases = 0
    decoded_observed = []
    decoded_expected = []
    coherent_inputs = {0: defaultdict(complex), 1: defaultdict(complex)}
    coherent_expected = {0: defaultdict(complex), 1: defaultdict(complex)}
    for family, rows, width, source, embedded, transferred in prepared:
        port_in_corridor_failures += corridor_cleanliness_failures(transferred)
        controlled = apply_controller_table(transferred, forward_table)
        observed = endpoint_return(controlled, geometry, site_bits)
        port_out_corridor_failures += corridor_cleanliness_failures(observed)
        expected = defaultdict(complex)
        actual = defaultdict(complex)
        seam = I823.apply_full_seam(rows, source)
        for matter, amplitude in seam.items():
            post_left = (matter >> left) & 1
            post_right = (matter >> right) & 1
            history = I826.expected_orientation(
                post_left, post_right, post_left ^ post_right
            )
            expected[(matter, history)] += amplitude
        for basis, amplitude in observed.items():
            matter = extract_matter(geometry, site_bits, basis, width)
            history = decode_history(basis)
            actual[(matter, history)] += amplitude
            expected_matters = set(seam)
            endpoint_failures += (
                matter not in expected_matters
                or ((basis >> site_bits[geometry["sources"][0]]) & 1)
                != ((next(iter(expected_matters)) >> left) & 1)
                or ((basis >> site_bits[geometry["sources"][1]]) & 1)
                != ((next(iter(expected_matters)) >> right) & 1)
            )
            cleanup_sites = (
                *geometry["targets"],
                *geometry["context"]["endpoint_auxiliaries"][EDGE_INDEX],
            )
            cleanup_failures += any(
                (basis >> site_bits[site]) & 1 for site in cleanup_sites
            )
            rows_out = H719.controller_register_rows(basis)
            token_failures += not (
                rows_out["A"] == (1,) + (0,) * (H719.CONTROLLER_STATIONS - 1)
                and not any(rows_out["B"])
                and not any(rows_out["work"])
            )
        residual = state_residual(actual, expected)
        maximum_residual = max(maximum_residual, residual)

        moved_back = port_in(observed, geometry, site_bits)
        inverse_controlled = apply_controller_table(moved_back, inverse_table)
        pointer_back = apply_route(
            inverse_controlled, geometry["port_paths"][2],
            R822.primitive_matrix("SWAP"), site_bits,
        )
        restored = endpoint_return(pointer_back, geometry, site_bits)
        inverse_corridor_failures += corridor_cleanliness_failures(restored)
        inverse_residual = state_residual(restored, embedded)
        maximum_inverse_residual = max(
            maximum_inverse_residual, inverse_residual
        )
        cases.append({
            "family": family,
            "source_basis": source,
            "residual": residual,
            "inverse_residual": inverse_residual,
        })
        physical_cases += family == "physical"
        target_cases += family == "target"
        decoded_observed.append((family, source, tuple(sorted(actual))))
        decoded_expected.append((family, source, tuple(sorted(expected))))

        if family == "physical":
            parity = next(iter(seam)).bit_count() % 2
            phase = np.exp(1j * (0.37 + 0.29 * len(coherent_inputs[parity])))
            for basis, amplitude in embedded.items():
                coherent_inputs[parity][basis] += phase * amplitude
            for key, amplitude in expected.items():
                coherent_expected[parity][key] += phase * amplitude

    coherent_residuals = []
    coherent_inverse_residuals = []
    for parity in (0, 1):
        norm = math.sqrt(sum(abs(value) ** 2 for value in coherent_inputs[parity].values()))
        initial = {
            key: value / norm for key, value in coherent_inputs[parity].items()
        }
        expected = {
            key: value / norm for key, value in coherent_expected[parity].items()
        }
        transferred = port_in(initial, geometry, site_bits)
        controlled = apply_controller_table(transferred, forward_table)
        observed = endpoint_return(controlled, geometry, site_bits)
        decoded = defaultdict(complex)
        for basis, amplitude in observed.items():
            decoded[(
                extract_matter(geometry, site_bits, basis, fixture.qubits),
                decode_history(basis),
            )] += amplitude
        coherent_residuals.append(state_residual(decoded, expected))
        inverse_ports = port_in(observed, geometry, site_bits)
        inverse_controller = apply_controller_table(inverse_ports, inverse_table)
        inverse_pointer = apply_route(
            inverse_controller, geometry["port_paths"][2],
            R822.primitive_matrix("SWAP"), site_bits,
        )
        restored = endpoint_return(inverse_pointer, geometry, site_bits)
        coherent_inverse_residuals.append(state_residual(restored, initial))

    return {
        "site_bits": site_bits,
        "normalized_fast": normalized_fast,
        "forward_table": forward_table,
        "inverse_table": inverse_table,
        "physical_signature_cases": physical_cases,
        "target_signature_cases": target_cases,
        "distinct_controller_inputs_executed": len(controller_inputs),
        "maximum_intertwiner_residual": maximum_residual,
        "maximum_inverse_residual": maximum_inverse_residual,
        "coherent_fixed_parity_tests": len(coherent_residuals),
        "maximum_coherent_intertwiner_residual": max(coherent_residuals),
        "maximum_coherent_inverse_residual": max(coherent_inverse_residuals),
        "endpoint_restoration_failures": endpoint_failures,
        "pointer_endpoint_and_scratch_cleanup_failures": cleanup_failures,
        "controller_token_and_work_return_failures": token_failures,
        "port_in_corridor_cleanliness_failures": port_in_corridor_failures,
        "port_out_corridor_cleanliness_failures": port_out_corridor_failures,
        "inverse_corridor_cleanliness_failures": inverse_corridor_failures,
        "case_rows": tuple(cases),
        "decoded_observed_sha256": sha256(
            repr(tuple(decoded_observed)).encode()
        ).hexdigest(),
        "decoded_expected_sha256": sha256(
            repr(tuple(decoded_expected)).encode()
        ).hexdigest(),
    }


def port_algebra_and_controls(geometry, physical):
    site_bits = physical["site_bits"]
    fswap = R822.primitive_matrix("FSWAP")
    swap = R822.primitive_matrix("SWAP")
    path_matrices = (fswap, fswap, swap)
    path_residuals = []
    deletion_residuals = []
    return_deletion_residuals = []
    for path, matrix in zip(geometry["port_paths"], path_matrices):
        source = site_bits[path[0]]
        target = site_bits[path[-1]]
        for left in (0, 1):
            for right in (0, 1):
                initial = {((left << source) | (right << target)): 1.0 + 0.0j}
                observed = apply_route(initial, path, matrix, site_bits)
                expected = apply_two_site(initial, matrix, source, target)
                path_residuals.append(state_residual(observed, expected))
        witness = {(1 << source): 1.0 + 0.0j}
        ideal = apply_route(witness, path, matrix, site_bits)
        deleted = apply_route(
            witness, path, matrix, site_bits,
            delete_ordinal=len(path) - 2,
        )
        deletion_residuals.append(state_residual(ideal, deleted))

    for path in geometry["port_paths"][:2]:
        source = site_bits[path[0]]
        witness = {(1 << source): 1.0 + 0.0j}
        moved = apply_route(witness, path, fswap, site_bits)
        returned = apply_route(moved, path, fswap, site_bits)
        damaged = apply_route(
            moved, path, fswap, site_bits,
            delete_ordinal=len(path) - 2,
        )
        return_deletion_residuals.append(state_residual(returned, damaged))

    parity = np.diag((1, -1, -1, 1)).astype(complex)
    dirty_type_residual = float(np.linalg.norm((fswap - swap)[:, 3]))
    clean_type_residual = float(np.linalg.norm((fswap - swap)[:, (0, 1, 2)]))
    fswap_square = float(np.linalg.norm(fswap @ fswap - np.eye(4)))
    fswap_parity = float(np.linalg.norm(fswap @ parity - parity @ fswap))

    # Seven nonblank destination triples are outside the port code and are
    # actively distinguished before the controller is applied.
    dirty_destination_inputs_detected = 0
    clean_controller = controller_genesis()
    context = geometry["context"]
    fixture = context["fixture"]
    edge = fixture.edges[EDGE_INDEX]
    rows = fixture.physical_terms(EDGE_INDEX)
    source_basis = next(
        basis for basis in I823.signature_representatives(rows, edge[4], edge[5])
        if ((basis >> edge[4]) & 1) ^ ((basis >> edge[5]) & 1)
    )
    instrumented = I823.instrument_sparse(
        rows, source_basis, edge[4], edge[5], fixture.qubits
    )
    clean_initial = embed_instrument_state(
        geometry, site_bits, instrumented, fixture.qubits,
        controller=clean_controller,
    )
    clean_moved = port_in(clean_initial, geometry, site_bits)
    for dirty in range(1, 8):
        controller = clean_controller
        for index, wire in enumerate((
            H719.M.R3.X.LEFT_ENDPOINT,
            H719.M.R3.X.RIGHT_ENDPOINT,
            H719.R3_SOURCE_POINTER(),
        )):
            controller |= ((dirty >> index) & 1) << wire
        initial = embed_instrument_state(
            geometry, site_bits, instrumented, fixture.qubits,
            controller=controller,
        )
        dirty_destination_inputs_detected += (
            state_residual(port_in(initial, geometry, site_bits), clean_moved)
            > 1.0e-6
        )

    return {
        "maximum_blank_corridor_endpoint_exchange_residual": max(path_residuals),
        "route_deletions_detected": sum(value > 1.0e-6 for value in deletion_residuals),
        "minimum_route_deletion_residual": min(deletion_residuals),
        "endpoint_return_deletions_detected": sum(
            value > 1.0e-6 for value in return_deletion_residuals
        ),
        "minimum_endpoint_return_deletion_residual": min(return_deletion_residuals),
        "FSWAP_square_residual": fswap_square,
        "FSWAP_parity_commutator_residual": fswap_parity,
        "FSWAP_vs_SWAP_clean_subspace_residual": clean_type_residual,
        "FSWAP_vs_SWAP_dirty_11_residual": dirty_type_residual,
        "dirty_destination_triples_detected": dirty_destination_inputs_detected,
        "dirty_destination_triples_tested": 7,
    }


def controller_sector_controls(geometry, physical):
    site_bits = physical["site_bits"]
    fixture = geometry["context"]["fixture"]
    edge = fixture.edges[EDGE_INDEX]
    left, right = edge[4], edge[5]
    rows = fixture.physical_terms(EDGE_INDEX)
    source = next(
        basis for basis in I823.signature_representatives(rows, left, right)
        if ((basis >> left) & 1) ^ ((basis >> right) & 1)
    )
    instrumented = I823.instrument_sparse(
        rows, source, left, right, fixture.qubits
    )
    normalized_fast = physical["normalized_fast"]

    def run(controller, word=normalized_fast):
        initial = embed_instrument_state(
            geometry, site_bits, instrumented, fixture.qubits,
            controller=controller,
        )
        moved = port_in(initial, geometry, site_bits)
        controlled = {
            H719.repeated_fast_word(basis, word): amplitude
            for basis, amplitude in moved.items()
        }
        return endpoint_return(controlled, geometry, site_bits)

    lawful = run(controller_genesis())
    rejected = {}
    for field in (
        H719.B.A.BINDER, H719.B.A.ACTUAL,
        H719.B.A.ADMISS, H719.B.A.LAW,
    ):
        observed = run(controller_genesis(rejected_field=field))
        rejected[str(field)] = {
            "different_from_lawful": state_residual(observed, lawful) > 1.0e-6,
            "controller_pointer_pending": all(
                (basis >> H719.R3_SOURCE_POINTER()) & 1 for basis in observed
            ),
        }

    token_controls = {}
    for label, tokens in (("zero", ()), ("two", (0, 1))):
        observed = run(controller_genesis(tokens=tokens))
        token_controls[label] = state_residual(observed, lawful) > 1.0e-6

    program = list(H719.PROGRAM)
    finalizer = next(
        index for index, row in enumerate(program) if row[0] == "finalizer"
    )
    program[finalizer] = ("identity", 0, ())
    damaged_word = H719.fast_classical_word(C827.normalize_word(
        H719.K.controller_word(tuple(program), H719.CONTROLLER_DATA_WIDTH)
    )[0])
    damaged = run(controller_genesis(), damaged_word)
    return {
        "rejected_acceptance_fields": rejected,
        "rejected_acceptance_fields_detected": sum(
            row["different_from_lawful"] and row["controller_pointer_pending"]
            for row in rejected.values()
        ),
        "zero_token_detected": token_controls["zero"],
        "two_token_detected": token_controls["two"],
        "success_finalizer_deletion_detected": state_residual(damaged, lawful) > 1.0e-6,
        "success_finalizer_deletion_leaves_pointer_pending": all(
            (basis >> H719.R3_SOURCE_POINTER()) & 1 for basis in damaged
        ),
    }


def parity_certificate(geometry):
    seam = I823.combined_parity_certificate(
        geometry["seam_words"],
        geometry["seam_charged"], geometry["seam_neutral"],
    )
    original = geometry["block"]["semantic"]
    controller = C827.expanded_certificate(original, geometry["normalized"])
    port_violations = 0
    port_factors = 0
    for index, path in enumerate(geometry["port_paths"]):
        factor_sites = set(path)
        expected = geometry["charged"] if index < 2 else geometry["neutral"]
        port_violations += bool(factor_sites - set(expected))
        port_factors += len(route_sequence(path)) * (2 if index < 2 else 1)
    return {
        "cycle823_elementary_failures": seam[
            "elementary_global_P_ext_commutator_failures"
        ],
        "cycle823_prefix_failures": seam["prefix_commutant_certificate_failures"],
        "controller_expanded_factors": controller["expanded_factors"],
        "controller_elementary_failures": controller[
            "normalized_elementary_parity_violations"
        ],
        "controller_prefix_failures": controller[
            "normalized_noncommuting_prefixes"
        ],
        "controller_terminal_parity_return": controller[
            "normalized_terminal_parity_returns"
        ],
        "controller_route_exchange_prefix_parity_violations": geometry[
            "controller_atlas"
        ]["route_exchange_prefix_parity_violations"],
        "port_typed_exchange_factor_occurrences": port_factors,
        "port_type_violations": port_violations,
        "combined_prefix_argument": (
            "each elementary factor in the ordered Cycle823; port; H^130; "
            "return; contact word commutes with the same combined P_ext"
        ),
    }


def covariance_certificate(geometry):
    frames = tuple(
        tuple(tuple(int(value) for value in row) for row in frame)
        for frame in R822.B.V.T.proper_cubic_frames()
    )
    route_paths = (
        tuple(record.path for record in geometry["seam_routes"])
        + tuple(geometry["controller_paths"].values())
        + geometry["port_paths"]
    )
    edges = frozenset(
        tuple(sorted((left, right)))
        for path in route_paths for left, right in zip(path, path[1:])
    )
    nn_failures = type_failures = edge_bijection_failures = 0
    translation_failures = port_order_failures = 0
    charged = geometry["charged"]
    neutral = geometry["neutral"]
    for frame in frames:
        mapped_charged = {matvec(frame, site) for site in charged}
        mapped_neutral = {matvec(frame, site) for site in neutral}
        type_failures += (
            len(mapped_charged) != len(charged)
            or len(mapped_neutral) != len(neutral)
            or bool(mapped_charged & mapped_neutral)
        )
        mapped_edges = {
            tuple(sorted((matvec(frame, left), matvec(frame, right))))
            for left, right in edges
        }
        edge_bijection_failures += len(mapped_edges) != len(edges)
        nn_failures += sum(
            R822.S789.manhattan(left, right) != 1
            for left, right in mapped_edges
        )
        for path in geometry["port_paths"]:
            mapped = tuple(matvec(frame, site) for site in path)
            port_order_failures += any(
                R822.S789.manhattan(left, right) != 1
                for left, right in zip(mapped, mapped[1:])
            )
        for site in geometry["block"]["wire_sites"]:
            translation_failures += (
                matvec(frame, add(site, CONTROLLER_TRANSLATION))
                != add(matvec(frame, site), matvec(frame, CONTROLLER_TRANSLATION))
            )

    product_failures = product_closure_failures = 0
    product_sites = tuple(
        site for path in geometry["port_paths"] for site in path
    )
    for left in frames:
        for right in frames:
            combined = matmul(left, right)
            product_closure_failures += combined not in frames
            product_failures += any(
                matvec(left, matvec(right, site)) != matvec(combined, site)
                for site in product_sites
            )
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "unique_joint_route_edges": len(edges),
        "transported_nearest_neighbour_failures": nn_failures,
        "transported_type_partition_failures": type_failures,
        "transported_edge_bijection_failures": edge_bijection_failures,
        "transported_port_path_order_failures": port_order_failures,
        "controller_translation_affine_failures": translation_failures,
        "port_coordinate_product_failures": product_failures,
        "proper_cubic_product_closure_failures": product_closure_failures,
        "port_coordinate_product_sites_tested": len(product_sites),
        "covariance_scope": (
            "full per-frame transport of one supplied finite joint program plus "
            "576 product checks on all port coordinates; not intrinsic rerouting "
            "or execution in independently generated frames"
        ),
    }


def execution_scope_certificate(geometry, physical, parity, placement):
    semantic_gates = len(geometry["normalized"])
    inputs = physical["distinct_controller_inputs_executed"]
    controller = geometry["controller_atlas"]
    return {
        "normalized_semantic_gates_per_H": semantic_gates,
        "semantic_H_applications_per_input": H719.CONTROLLER_STATIONS,
        "semantic_gate_applications_per_input": (
            semantic_gates * H719.CONTROLLER_STATIONS
        ),
        "semantic_controller_inputs_executed": inputs,
        "semantic_gate_applications_total": (
            semantic_gates * H719.CONTROLLER_STATIONS * inputs
        ),
        "controller_elementary_factors_per_H_structural": parity[
            "controller_expanded_factors"
        ],
        "controller_routed_gates_per_H_structural": controller[
            "routed_total_gates"
        ],
        "controller_routed_gates_per_orbit_structural": controller[
            "full_130_H_orbit_routed_controller_gates"
        ],
        "literal_new_port_factors_executed_on_sparse_state": placement[
            "forward_port_gate_count"
        ],
        "semantic_controller_execution": True,
        "controller_elementary_dense_execution": False,
        "routed_controller_dense_execution": False,
        "new_port_literal_sparse_state_execution": True,
        "execution_boundary": (
            "the 235 new port factors are literal sparse-state execution; the "
            "normalized semantic H is executed 130 times on four inputs; the "
            "740226-factor and 1731014740-routed-gate controller surfaces remain "
            "the inherited structural compiler certificate"
        ),
    }


def paired_receipt_certificate(
    placement, schedule, physical, algebra, controls, parity, covariance,
    execution_scope, mass
):
    payload = json.loads((ROOT / RECEIPT_PATH).read_text())
    expected = {
        "artifact": Path(RUNNER_PATH).name,
        "audit": "unset",
        "authority": "none",
        "artifact_provenance_sha256": {
            "note": digest(ROOT / NOTE_PATH),
            "runner": digest(ROOT / RUNNER_PATH),
        },
        "checks_passed": 11,
        "checks_total": 11,
        "claim_scope": (
            "one-use one-edge clean-genesis same-chart physical-M2 endpoint and "
            "pointer port into one translated finite Cycle719 H^130 controller"
        ),
        "placement": {
            "controller_translation": list(placement["controller_translation"]),
            "port_route_distances": list(placement["port_route_distances"]),
            "port_returned_macro_gates": list(
                placement["port_returned_macro_gates"]
            ),
            "forward_port_gate_count": placement["forward_port_gate_count"],
            "combined_charged_coordinates": placement[
                "combined_charged_coordinates"
            ],
            "combined_neutral_coordinates": placement[
                "combined_neutral_coordinates"
            ],
            "combined_charged_neutral_overlap": placement[
                "combined_charged_neutral_overlap"
            ],
            "port_path_sha256": placement["port_path_sha256"],
        },
        "serial_schedule": {
            "manifest": list(schedule["manifest"]),
            "manifest_sha256": schedule["manifest_sha256"],
            "stage_aware_collision_edges": schedule[
                "stage_aware_collision_edges"
            ],
            "charged_same_type_corridor_reuse": schedule[
                "charged_same_type_corridor_reuse"
            ],
            "neutral_same_type_corridor_reuse": schedule[
                "neutral_same_type_corridor_reuse"
            ],
            "erased_stage_reuse_coordinates": schedule[
                "erased_stage_reuse_coordinates"
            ],
            "endpoint_post_precedes_contact": schedule[
                "endpoint_post_precedes_contact"
            ],
            "stage_labels_are_physical_time": schedule[
                "stage_labels_are_physical_time"
            ],
        },
        "intertwiner": {
            "physical_signature_cases": physical["physical_signature_cases"],
            "target_signature_cases": physical["target_signature_cases"],
            "coherent_fixed_parity_tests": physical[
                "coherent_fixed_parity_tests"
            ],
            "maximum_intertwiner_residual": physical[
                "maximum_intertwiner_residual"
            ],
            "maximum_inverse_residual": physical["maximum_inverse_residual"],
            "maximum_coherent_intertwiner_residual": physical[
                "maximum_coherent_intertwiner_residual"
            ],
            "maximum_coherent_inverse_residual": physical[
                "maximum_coherent_inverse_residual"
            ],
            "cleanup_failures": (
                physical["endpoint_restoration_failures"]
                + physical["pointer_endpoint_and_scratch_cleanup_failures"]
                + physical["controller_token_and_work_return_failures"]
                + physical["port_in_corridor_cleanliness_failures"]
                + physical["port_out_corridor_cleanliness_failures"]
                + physical["inverse_corridor_cleanliness_failures"]
            ),
            "decoded_observed_sha256": physical["decoded_observed_sha256"],
            "decoded_expected_sha256": physical["decoded_expected_sha256"],
        },
        "active_controls": {
            "route_deletions_detected": algebra["route_deletions_detected"],
            "endpoint_return_deletions_detected": algebra[
                "endpoint_return_deletions_detected"
            ],
            "minimum_route_deletion_residual": algebra[
                "minimum_route_deletion_residual"
            ],
            "dirty_destination_triples_detected": algebra[
                "dirty_destination_triples_detected"
            ],
            "FSWAP_vs_SWAP_dirty_11_residual": algebra[
                "FSWAP_vs_SWAP_dirty_11_residual"
            ],
            "rejected_acceptance_fields_detected": controls[
                "rejected_acceptance_fields_detected"
            ],
            "zero_token_detected": controls["zero_token_detected"],
            "two_token_detected": controls["two_token_detected"],
            "success_finalizer_deletion_detected": controls[
                "success_finalizer_deletion_detected"
            ],
        },
        "parity_and_covariance": {
            "controller_expanded_factors": parity[
                "controller_expanded_factors"
            ],
            "combined_elementary_or_prefix_failures": (
                parity["cycle823_elementary_failures"]
                + parity["cycle823_prefix_failures"]
                + parity["controller_elementary_failures"]
                + parity["controller_prefix_failures"]
                + parity[
                    "controller_route_exchange_prefix_parity_violations"
                ]
                + parity["port_type_violations"]
            ),
            "proper_cubic_frames": covariance["proper_cubic_frames"],
            "ordered_frame_products": covariance["ordered_frame_products"],
            "unique_joint_route_edges": covariance["unique_joint_route_edges"],
            "transport_or_product_failures": sum(
                covariance[label] for label in (
                    "transported_nearest_neighbour_failures",
                    "transported_type_partition_failures",
                    "transported_edge_bijection_failures",
                    "transported_port_path_order_failures",
                    "controller_translation_affine_failures",
                    "port_coordinate_product_failures",
                    "proper_cubic_product_closure_failures",
                )
            ),
            "port_coordinate_product_sites_tested": covariance[
                "port_coordinate_product_sites_tested"
            ],
        },
        "execution_scope": {
            key: execution_scope[key] for key in (
                "normalized_semantic_gates_per_H",
                "semantic_H_applications_per_input",
                "semantic_gate_applications_per_input",
                "semantic_controller_inputs_executed",
                "semantic_gate_applications_total",
                "controller_elementary_factors_per_H_structural",
                "controller_routed_gates_per_H_structural",
                "controller_routed_gates_per_orbit_structural",
                "literal_new_port_factors_executed_on_sparse_state",
                "semantic_controller_execution",
                "controller_elementary_dense_execution",
                "routed_controller_dense_execution",
                "new_port_literal_sparse_state_execution",
            )
        },
        "mass_contact": {
            "one_particle_mass": mass["one_particle_mass"],
            "one_particle_mass_residual": mass["one_particle_mass_residual"],
            "contact_vacuum_and_one_particle_residual": mass[
                "contact_vacuum_and_one_particle_residual"
            ],
            "contact_double_occupation_phase_residual": mass[
                "contact_double_occupation_phase_residual"
            ],
        },
        "open_boundary": [
            "multi-edge placement, selection, arbitration, and resource scaling",
            "intrinsic atlas generation, local type enforcement, and charged/neutral port-corridor genesis",
            "autonomous program, token, bank, admission, occurrence, capacity, and renewal",
            "physical time, inaccessible inverse, permanent Record, Born/history, source/gravity, and prediction bridges",
        ],
        "status": (
            "cycle863-cycle823-cycle719-same-chart-history-port-bounded-positive"
        ),
    }
    sections = {key: payload.get(key) == value for key, value in expected.items()}
    sections["no_unpinned_receipt_sections"] = set(payload) == set(expected)
    sections["all"] = all(sections.values())
    return sections


def main():
    started = time.time()
    declared = (
        len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
        and NOTE_PATH in AUDIT_INPUT_PATHS
        and RUNNER_PATH in AUDIT_INPUT_PATHS
        and RECEIPT_PATH in AUDIT_INPUT_PATHS
        and all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        )
    )
    geometry = joint_geometry()
    placement = geometry_certificate(geometry)
    schedule = schedule_certificate(geometry)
    physical = physical_intertwiner_certificate(geometry)
    algebra = port_algebra_and_controls(geometry, physical)
    controls = controller_sector_controls(geometry, physical)
    parity = parity_certificate(geometry)
    covariance = covariance_certificate(geometry)
    execution_scope = execution_scope_certificate(
        geometry, physical, parity, placement
    )
    mass = R822.one_particle_mass_fixture()
    paired_receipt = paired_receipt_certificate(
        placement, schedule, physical, algebra, controls, parity, covariance,
        execution_scope, mass
    )

    checks = {
        "declared_inputs_are_unique_existing_repo_relative_files": declared,
        "one_edge_joint_atlas_and_three_ports_are_collision_free": (
            placement["controller_translation"] == CONTROLLER_TRANSLATION
            and placement["port_route_distances"] == (28, 28, 8)
            and placement["path_pair_intersections"] == (0, 0, 0)
            and placement["internal_persistent_hits"] == (0, 0, 0)
            and placement["forbidden_cross_type_path_hits"] == (0, 0, 0)
            and placement["path_repeat_failures"] == (0, 0, 0)
            and placement["nearest_neighbour_failures"] == (0, 0, 0)
            and placement["cycle823_controller_persistent_collisions"] == 0
            and placement["separate_atlas_same_type_collisions"] == (0, 0)
            and placement["separate_atlas_cross_type_collisions"] == (0, 0)
            and placement["combined_charged_coordinates"] == 582
            and placement["combined_neutral_coordinates"] == 17915
            and placement["combined_charged_neutral_overlap"] == 0
            and placement["port_path_sha256"]
            == "a27767ae0a4a0cda45bcfca43582b270024b69d141ff730ce574ccf34567784c"
        ),
        "fixed_serial_schedule_separates_same_type_workspace_reuse": (
            schedule["manifest"] == STAGE_MANIFEST
            and schedule["endpoint_post_words"] > 0
            and schedule["contact_words"] > 0
            and schedule["endpoint_post_precedes_contact"]
            and schedule["distinct_serial_stage_ordinals"] == 6
            and schedule["top_level_scheduled_resource_rows"] == 8
            and schedule["stage_aware_collision_edges"] == 0
            and schedule["charged_same_type_corridor_reuse"] == 27
            and schedule["neutral_same_type_corridor_reuse"] == 3
            and schedule["erased_stage_reuse_coordinates"] == 30
            and schedule["controller_route_return_failures"] == 0
            and schedule["controller_charged_corridor_persistent_hits"] == 0
            and not schedule["stage_labels_are_physical_time"]
        ),
        "actual_state_transfer_controller_and_inverse_intertwine": (
            physical["physical_signature_cases"] == 8
            and physical["target_signature_cases"] == 8
            and physical["distinct_controller_inputs_executed"] == 4
            and physical["maximum_intertwiner_residual"] < TOL
            and physical["maximum_inverse_residual"] < TOL
            and physical["coherent_fixed_parity_tests"] == 2
            and physical["maximum_coherent_intertwiner_residual"] < TOL
            and physical["maximum_coherent_inverse_residual"] < TOL
            and physical["endpoint_restoration_failures"] == 0
            and physical["pointer_endpoint_and_scratch_cleanup_failures"] == 0
            and physical["controller_token_and_work_return_failures"] == 0
            and physical["port_in_corridor_cleanliness_failures"] == 0
            and physical["port_out_corridor_cleanliness_failures"] == 0
            and physical["inverse_corridor_cleanliness_failures"] == 0
            and physical["decoded_observed_sha256"]
            == physical["decoded_expected_sha256"]
        ),
        "port_route_algebra_and_deletions_are_active": (
            algebra["maximum_blank_corridor_endpoint_exchange_residual"] < TOL
            and algebra["route_deletions_detected"] == 3
            and algebra["endpoint_return_deletions_detected"] == 2
            and algebra["FSWAP_square_residual"] < TOL
            and algebra["FSWAP_parity_commutator_residual"] < TOL
            and algebra["FSWAP_vs_SWAP_clean_subspace_residual"] < TOL
            and algebra["FSWAP_vs_SWAP_dirty_11_residual"] > 1.0
            and algebra["dirty_destination_triples_detected"]
            == algebra["dirty_destination_triples_tested"] == 7
        ),
        "admission_token_and_finalizer_controls_are_active": (
            controls["rejected_acceptance_fields_detected"] == 4
            and controls["zero_token_detected"]
            and controls["two_token_detected"]
            and controls["success_finalizer_deletion_detected"]
            and controls["success_finalizer_deletion_leaves_pointer_pending"]
        ),
        "one_combined_parity_operator_closes_every_elementary_prefix": (
            parity["cycle823_elementary_failures"] == 0
            and parity["cycle823_prefix_failures"] == 0
            and parity["controller_expanded_factors"] == 740226
            and parity["controller_elementary_failures"] == 0
            and parity["controller_prefix_failures"] == 0
            and parity["controller_terminal_parity_return"]
            and parity[
                "controller_route_exchange_prefix_parity_violations"
            ] == 0
            and parity["port_type_violations"] == 0
        ),
        "proper_cubic_transport_and_port_product_checks_are_exact": (
            covariance["proper_cubic_frames"] == 24
            and covariance["ordered_frame_products"] == 576
            and covariance["transported_nearest_neighbour_failures"] == 0
            and covariance["transported_type_partition_failures"] == 0
            and covariance["transported_edge_bijection_failures"] == 0
            and covariance["transported_port_path_order_failures"] == 0
            and covariance["controller_translation_affine_failures"] == 0
            and covariance["port_coordinate_product_failures"] == 0
            and covariance["proper_cubic_product_closure_failures"] == 0
            and covariance["port_coordinate_product_sites_tested"] == 67
        ),
        "dense_and_structural_execution_surfaces_are_separated": (
            execution_scope["normalized_semantic_gates_per_H"] == 61562
            and execution_scope["semantic_H_applications_per_input"] == 130
            and execution_scope["semantic_gate_applications_per_input"]
            == 8003060
            and execution_scope["semantic_controller_inputs_executed"] == 4
            and execution_scope["semantic_gate_applications_total"] == 32012240
            and execution_scope[
                "controller_elementary_factors_per_H_structural"
            ] == 740226
            and execution_scope["controller_routed_gates_per_H_structural"]
            == 13315498
            and execution_scope[
                "controller_routed_gates_per_orbit_structural"
            ] == 1731014740
            and execution_scope[
                "literal_new_port_factors_executed_on_sparse_state"
            ] == 235
            and execution_scope["semantic_controller_execution"]
            and not execution_scope["controller_elementary_dense_execution"]
            and not execution_scope["routed_controller_dense_execution"]
            and execution_scope["new_port_literal_sparse_state_execution"]
        ),
        "mass_seam_and_contact_fixture_is_unchanged_before_contact": (
            mass["one_particle_coin_eigen_residual"] < 1.0e-12
            and mass["one_particle_mass_residual"] < 1.0e-12
            and mass["contact_vacuum_and_one_particle_residual"] < TOL
            and mass["contact_double_occupation_phase_residual"] < TOL
            and physical["endpoint_restoration_failures"] == 0
        ),
        "paired_receipt_is_current_and_all_values_are_pinned": paired_receipt[
            "all"
        ],
    }
    report = {
        "cycle": 863,
        "status": (
            "cycle863-cycle823-cycle719-same-chart-history-port-bounded-positive"
            if all(checks.values()) else "cycle863-failed"
        ),
        "authority": "none",
        "audit": "unset",
        "claim_scope": (
            "one-use one-edge clean-genesis same-chart physical-M2 endpoint and "
            "pointer port into one translated finite Cycle719 H^130 controller"
        ),
        "stage_manifest": STAGE_MANIFEST,
        "circuit_ordinals_are_physical_time": False,
        "normalization_control_swaps": geometry["normalization_swaps"],
        "normalization_equivalence_failures": geometry[
            "normalization_equivalence_failures"
        ],
        "placement": placement,
        "serial_schedule": schedule,
        "physical_intertwiner": {
            key: value for key, value in physical.items()
            if key not in ("site_bits", "normalized_fast", "forward_table", "inverse_table")
        },
        "port_algebra_and_controls": algebra,
        "controller_sector_controls": controls,
        "combined_parity": parity,
        "covariance": covariance,
        "execution_scope": execution_scope,
        "one_particle_mass_fixture": mass,
        "paired_receipt": paired_receipt,
        "checks": checks,
        "inventory": {
            "derived": (
                "three explicit disjoint same-chart typed port routes",
                "actual FSWAP/SWAP state transfer without endpoint-bit extraction",
                "exact 16-signature and two coherent fixed-parity intertwiners",
                "successful-sector pointer cleanup and exact reversible recreation",
                "one combined P_ext and passive 24-frame/576-product covariance",
            ),
            "supplied": (
                "fixed (2,1,1) single edge and controller translation",
                "offline joint route atlas, coframe, and blank charged and neutral port corridors",
                "clean Cycle823 instrument and complete Cycle719 first-use bank genesis",
                "unique station-zero token and fixed 130-station program occurrence",
                "successful BINDER/ACTUAL/ADMISS/LAW sector and fresh capacity",
            ),
            "open": (
                "two-, twenty-, and fifty-nine-edge placement and arbitration",
                "intrinsic local atlas generation, type enforcement, and charged/neutral port-corridor genesis",
                "autonomous program/token/bank/admission occurrence and renewal",
                "physical time, inaccessible inverse, permanent Record, Born/history law",
                "source/gravity response and a no-refit prediction bridge",
            ),
        },
        "source_sha256": {
            path: digest(ROOT / path) for path in AUDIT_INPUT_PATHS
        } if declared else {},
        "runtime_seconds": time.time() - started,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    for label, passed in checks.items():
        print(f"CHECK {label}: {'PASS' if passed else 'FAIL'}")
    if not all(checks.values()):
        raise SystemExit(1)
    print("CYCLE863_CYCLE823_CYCLE719_SAME_CHART_HISTORY_PORT_BOUNDED_PASS")


if __name__ == "__main__":
    main()
