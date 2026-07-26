#!/usr/bin/env python3
"""Cycle711 chart-erasure and fixed-program acceptance probe.

This fail-closed runner asks whether the 24 common-coframe Cycle710 family
can be represented by one immutable physical Cycle709 word once all coframe
dependence is moved into passive input/output chart identifications.  It also
keeps passive storage-chart changes separate from independently active local
coframes, and audits whether the surviving six-colour schedule is order-free.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import inspect
from itertools import combinations, permutations
import json
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle710_port_canonical_order_gauge_core_2026_07_26 as K
import frontier_cycle710_port_canonical_physical_core_2026_07_26 as PHYS
import frontier_cycle709_local_seam_physical_core_2026_07_26 as P709
import frontier_cycle709_local_seam_clifford_core_2026_07_26 as C709
import frontier_cycle709_local_seam_clifford_2026_07_26 as C709_RUNNER

c707 = PHYS.c707
P = K.P
PASS = 0
FAIL = 0
AUDIT_TIMEOUT_SEC = 360
NOTE_PATH = (
    "docs/CHART_ERASED_FIXED_PROGRAM_PHYSICAL_M2_COMPILER_"
    "CYCLE711_BOUNDED_THEOREM_NOTE_2026-07-26.md"
)
AUDIT_INPUT_PATHS = (
    "docs/CHART_ERASED_FIXED_PROGRAM_PHYSICAL_M2_COMPILER_"
    "CYCLE711_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "scripts/frontier_cycle711_chart_erased_fixed_program_2026_07_26.py",
    "docs/PORT_CANONICAL_COMMON_COFRAME_PHYSICAL_M2_COMPILER_"
    "CYCLE710_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_"
    "CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_"
    "EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md",
    "docs/LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_"
    "CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_CYCLE704_FSWAP_ENDPOINT_CUBE_BRIDGE_"
    "CYCLE708_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "scripts/frontier_cycle710_port_canonical_common_coframe_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle710_port_canonical_order_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle710_port_canonical_physical_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS


def check(label: str, condition: bool, detail):
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail, flush=True)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail, flush=True)


def json_ready(value):
    if isinstance(value, dict):
        return {str(key): json_ready(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [json_ready(item) for item in value]
    if isinstance(value, set):
        return [json_ready(item) for item in sorted(value, key=repr)]
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    return value


def tableau_digest(rows) -> str:
    payload = "\n".join(
        f"{row.phase}:{row.x:x}:{row.z:x}" for row in rows
    ).encode()
    return sha256(payload).hexdigest()


def instruction_signature(instruction):
    return (
        instruction.kind,
        tuple(tuple(int(value) for value in site) for site in instruction.sites),
        c707.c655.matrix_digest(instruction.matrix),
    )


def word_digest(word) -> str:
    payload = json.dumps(
        tuple(instruction_signature(instruction) for instruction in word),
        separators=(",", ":"),
    ).encode()
    return sha256(payload).hexdigest()


def inverse_tableau(images, qubits: int):
    """Exact inverse signed-Clifford tableau by GF(2) column elimination."""
    pivots = {}
    dimension = 2 * qubits
    for generator, image in enumerate(images):
        vector = image.symplectic(qubits)
        selector = 1 << generator
        while vector:
            pivot = vector.bit_length() - 1
            if pivot in pivots:
                prior_vector, prior_selector = pivots[pivot]
                vector ^= prior_vector
                selector ^= prior_selector
            else:
                pivots[pivot] = (vector, selector)
                break
    if len(pivots) != dimension:
        raise AssertionError(("singular tableau", len(pivots), dimension))
    output = []
    mask = (1 << qubits) - 1
    for target in range(dimension):
        vector = 1 << target
        selector = 0
        while vector:
            pivot = vector.bit_length() - 1
            prior_vector, prior_selector = pivots[pivot]
            vector ^= prior_vector
            selector ^= prior_selector
        candidate = P(0, selector & mask, selector >> qubits)
        observed = C709.apply_images(images, candidate, qubits)
        expected = P(
            x=(1 << target) if target < qubits else 0,
            z=(1 << (target - qubits)) if target >= qubits else 0,
        )
        if (observed.x, observed.z) != (expected.x, expected.z):
            raise AssertionError(("inverse binary residual", target))
        candidate = P((-observed.phase) % 4, candidate.x, candidate.z)
        if C709.apply_images(images, candidate, qubits) != expected:
            raise AssertionError(("inverse phase residual", target))
        output.append(candidate)
    return tuple(output)


def inverse_instruction(instruction):
    digest = c707.c655.matrix_digest(instruction.matrix)
    lookup = {
        c707.c655.matrix_digest(c707.c655.H): c707.c655.H,
        c707.c655.matrix_digest(c707.S_GATE): c707.SDG_GATE,
        c707.c655.matrix_digest(c707.SDG_GATE): c707.S_GATE,
        c707.c655.matrix_digest(c707.c655.CNOT): c707.c655.CNOT,
    }
    if digest not in lookup:
        raise AssertionError(("unsupported inverse gate", instruction.kind, digest))
    return c707.Instruction(
        "passive_inverse_" + instruction.kind,
        instruction.sites,
        lookup[digest],
    )


def inverse_word(word):
    return tuple(inverse_instruction(instruction) for instruction in reversed(word))


def pull_pauli_to_source(row, source_to_target, all_sites):
    index = {site: position for position, site in enumerate(all_sites)}
    x = z = 0
    for source, target in source_to_target.items():
        source_bit = 1 << index[source]
        target_bit = 1 << index[target]
        if row.x & target_bit:
            x |= source_bit
        if row.z & target_bit:
            z |= source_bit
    return c707.Pauli(row.phase, x, z)


def pull_rows_to_source(rows, source_to_target, all_sites):
    return tuple(
        pull_pauli_to_source(row, source_to_target, all_sites) for row in rows
    )


def code_mismatch(left, right, carriers, all_sites):
    exact = 0
    code = 0
    for observed, expected in zip(left, right):
        exact += observed != expected
        code += not PHYS.is_positive_repetition_stabilizer(
            observed @ expected, carriers, all_sites
        )
    return {"exact": exact, "code": code}


def frame_artifact(
    frame_index,
    frame,
    source_eq,
    base_images,
    primary,
    source_carriers,
    source_basis,
    base_observed,
    primary_sites,
):
    target_cells = K.transform_eq(source_eq.open_graph.cells, frame)
    target_eq = K.port_equivalence(target_cells)
    transport = K.mixed_compiler_transport(
        source_eq, target_eq, frame, base_images
    )
    graph, site_map, gauges, occupied, collisions = PHYS.physical_bundle(
        target_cells
    )
    target_carriers = PHYS.augmented_carriers(
        target_eq, graph, site_map, gauges
    )
    pulled_carriers = PHYS.pullback_carriers(target_carriers, frame)
    pulled_occupied = {PHYS.pullback(site, frame) for site in occupied}
    site_relabel = PHYS.physical_site_relabel(
        source_carriers, pulled_carriers, transport.patch_mapping
    )
    if set(site_relabel) != set(primary_sites):
        raise AssertionError("source physical relabel is not total")
    if set(site_relabel.values()) != set(primary_sites):
        raise AssertionError("target physical relabel is not bijective")

    relabelled_base = PHYS.relabel_word(primary["word"], site_relabel)
    inverse_relabel = {target: source for source, target in site_relabel.items()}
    recovered_base_word = PHYS.relabel_word(relabelled_base, inverse_relabel)
    terms = PHYS.mapped_gauge_terms(transport)
    pre_word = PHYS.compile_gauge_stage("pre", terms, pulled_carriers)
    post_word = PHYS.compile_gauge_stage("post", terms, pulled_carriers)
    full_word = pre_word + relabelled_base + post_word

    input_rows = PHYS.encoded_basis(
        target_eq.qubits, pulled_carriers, primary_sites
    )
    site_index = {site: index for index, site in enumerate(primary_sites)}
    observed_full = PHYS.conjugate_rows(input_rows, full_word, site_index)
    expected_full = tuple(
        PHYS.lift_pauli(row, pulled_carriers, primary_sites)
        for row in transport.images
    )
    full_mismatch = code_mismatch(
        observed_full, expected_full, pulled_carriers, primary_sites
    )

    # Address relabeling alone is the strict control.  If this differs from the
    # target action, the D_pre/D_post signed-code Clifford is genuinely
    # load-bearing in the currently emitted W_R, even though it can be moved
    # into the definition of passive input/output code charts below.
    address_only_observed = PHYS.conjugate_rows(
        input_rows, relabelled_base, site_index
    )
    address_only_mismatch = code_mismatch(
        address_only_observed, expected_full, pulled_carriers, primary_sites
    )

    patch_inverse = inverse_tableau(transport.patch_forward, source_eq.qubits)
    pre_inverse = inverse_tableau(transport.pre, source_eq.qubits)
    erased_abstract = C709.compose(
        patch_inverse,
        C709.compose(transport.images, pre_inverse, source_eq.qubits),
        source_eq.qubits,
    )
    abstract_mismatch = C709.mismatch_counts(erased_abstract, base_images)

    stabilizers = PHYS.repetition_stabilizers(
        pulled_carriers, primary_sites
    )
    stabilizer_images = PHYS.conjugate_rows(
        stabilizers, full_word, site_index
    )
    leakage = sum(
        observed != expected
        for observed, expected in zip(stabilizer_images, stabilizers)
    )
    routed, route_report = c707.route_word(full_word)
    return {
        "frame_index": frame_index,
        "frame_key": tuple(int(value) for value in frame.flat),
        "is_identity": bool(np.array_equal(frame, K.I3)),
        "abstract_chart_erased_digest": tableau_digest(erased_abstract),
        "abstract_chart_erased_mismatch": abstract_mismatch,
        "full_physical_intertwiner_mismatch": full_mismatch,
        "address_only_without_chart_Clifford_mismatch": address_only_mismatch,
        "recovered_base_primitive_digest": word_digest(recovered_base_word),
        "recovered_base_instruction_failures": sum(
            instruction_signature(left) != instruction_signature(right)
            for left, right in zip(recovered_base_word, primary["word"])
        ) + abs(len(recovered_base_word) - len(primary["word"])),
        "pre_gates_moved_to_passive_chart": len(pre_word),
        "post_gates_moved_to_passive_chart": len(post_word),
        "full_primitive_gates_before_erasure": len(full_word),
        "physical_M2": len(occupied),
        "placement_failures": collisions + len(
            pulled_occupied ^ set(primary_sites)
        ),
        "leakage_stabilizer_failures": leakage,
        "route_failures": sum(
            route_report[key]
            for key in (
                "non_NN_failures",
                "operand_order_failures",
                "route_return_failures",
            )
        ),
        "routed_gates_before_erasure": len(routed),
        "routed_digest_before_erasure": route_report["word_sha256"],
        "minimum_detected_first_SWAP_deletions": route_report[
            "delete_first_swap_detected_macros"
        ],
    }, transport


def schedule_audit(primary):
    cells = primary["cells"]
    eq = primary["equivalence"]
    identity = C709.identity_images(eq.qubits)
    layers = {colour: identity for colour in C709.ALL_COLOURS}
    counts = Counter()
    for cell, axis, _matter, _reference in eq.open_graph.cross_edges:
        colour = C709.seam_colour((cell, axis))
        counts[colour] += 1
        layers[colour] = C709.compose(
            C709.seam_images(eq, cell, axis), layers[colour], eq.qubits
        )
    active = tuple(colour for colour in C709.ALL_COLOURS if counts[colour])
    pair_rows = []
    for left, right in combinations(active, 2):
        lr = C709.compose(layers[left], layers[right], eq.qubits)
        rl = C709.compose(layers[right], layers[left], eq.qubits)
        mismatch = C709.mismatch_counts(lr, rl)
        pair_rows.append({
            "left": left,
            "right": right,
            "mismatch": mismatch,
        })
    cleanup = C709.cleanup_images(eq, primary["composition"].cleanup)
    permutation_rows = []
    reference = primary["composition"].cleaned
    for order in permutations(active):
        coloured = identity
        for colour in order:
            coloured = C709.compose(layers[colour], coloured, eq.qubits)
        cleaned = C709.compose(cleanup, coloured, eq.qubits)
        permutation_rows.append({
            "order": order,
            "mismatch": C709.mismatch_counts(cleaned, reference),
        })
    return {
        "all_layers": C709.ALL_COLOURS,
        "active_layers": active,
        "seams_per_layer": dict(counts),
        "same_layer_physical_support_collisions": primary[
            "same_colour_support_collisions"
        ],
        "active_layer_pairs": len(pair_rows),
        "noncommuting_layer_pairs": sum(
            row["mismatch"]["exact"] > 0 for row in pair_rows
        ),
        "maximum_pair_exact_mismatch": max(
            (row["mismatch"]["exact"] for row in pair_rows), default=0
        ),
        "pair_rows": pair_rows,
        "active_layer_permutations": len(permutation_rows),
        "permutations_equal_to_reference": sum(
            row["mismatch"]["exact"] == 0 for row in permutation_rows
        ),
        "maximum_permutation_exact_mismatch": max(
            (row["mismatch"]["exact"] for row in permutation_rows), default=0
        ),
        "permutation_rows": permutation_rows,
    }


def held_storage_summary():
    rows = K.port_shuffled_campaign()
    shapes = sorted({tuple(row["shape"]) for row in rows})
    semantic = sum(
        value
        for row in rows
        for family in row["semantic_failures"].values()
        for value in family.values()
    )
    transition_terms = sum(
        row["open_gauge"]["Z_terms"]
        + row["open_gauge"]["CZ_terms"]
        + row["patch_gauge"]["Z_terms"]
        + row["patch_gauge"]["CZ_terms"]
        for row in rows
    )
    return {
        "shapes": shapes,
        "rows": len(rows),
        "semantic_failure_sum": semantic,
        "storage_transition_terms": transition_terms,
        "maximum_qubits": max(row["qubits"] for row in rows),
        "parameters_refit_sum": sum(row["parameters_refit"] for row in rows),
    }


def origin_and_frame_free_program_audit():
    """Audit the fixed local generator without transporting an origin/frame."""
    shapes = ((2, 2, 2), (3, 2, 2), (4, 2, 2), (3, 3, 3))
    origins = tuple(np.ndindex((2, 2, 2)))
    origin_rows = []
    fixed_origin_translation_rows = []
    for shape in shapes:
        cells = C709.G.box_cells(shape)
        for origin in origins:
            candidate = C709.coloured_composition(cells, origin)
            origin_rows.append(
                C709.mismatch_counts(candidate.cleaned, candidate.target)["exact"]
            )
            shifted = tuple(
                tuple(value + delta for value, delta in zip(cell, origin))
                for cell in cells
            )
            fixed = C709.coloured_composition(shifted, (0, 0, 0))
            fixed_origin_translation_rows.append(
                C709.mismatch_counts(fixed.cleaned, fixed.target)["exact"]
            )

    primary = C709.G.box_cells((3, 2, 2))
    rotated_rows = []
    for frame in C709.G.c706.proper_cubic_frames():
        rotated = {
            tuple(int(value) for value in frame @ np.asarray(cell))
            for cell in primary
        }
        minimum = tuple(min(cell[axis] for cell in rotated) for axis in range(3))
        maximum = tuple(max(cell[axis] for cell in rotated) for axis in range(3))
        shape = tuple(maximum[axis] - minimum[axis] + 1 for axis in range(3))
        # The same frame-argument-free generator is evaluated on the normalized
        # rectangular physical set; no frame is passed to the law constructor.
        candidate = C709.coloured_composition(C709.G.box_cells(shape), (0, 0, 0))
        rotated_rows.append({
            "shape": shape,
            "exact_mismatch": C709.mismatch_counts(
                candidate.cleaned, candidate.target
            )["exact"],
        })
    return {
        "shapes": shapes,
        "colour_origins_per_shape": len(origins),
        "colour_origin_exact_failure_sum": sum(origin_rows),
        "fixed_origin_translation_residues_per_shape": len(origins),
        "fixed_origin_translation_exact_failure_sum": sum(
            fixed_origin_translation_rows
        ),
        "proper_cubic_normalized_boxes": len(rotated_rows),
        "proper_cubic_frame_argument_count": 0,
        "proper_cubic_exact_failure_sum": sum(
            row["exact_mismatch"] for row in rotated_rows
        ),
        "rotated_rows": tuple(rotated_rows),
        "colour_function_signature": str(inspect.signature(C709.seam_colour)),
        "cleanup_function_signature": str(inspect.signature(C709.cleanup_predicate)),
    }


def main():
    check(
        "the transitive source closure is repo-local and complete",
        len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and all(not path.startswith(("/", "../")) for path in AUDIT_INPUT_PATHS),
        {"declared_inputs": len(AUDIT_INPUT_PATHS)},
    )
    print("PHASE immutable W-star", flush=True)
    cells = K.G.box_cells((3, 2, 2))
    source_eq, base_images = K.legacy_source_compiler(cells)
    primary = P709.primary_word()
    source_carriers = PHYS.augmented_carriers(
        source_eq, primary["graph"], primary["site_map"], primary["gauges"]
    )
    primary_sites = tuple(primary["all_sites"])
    source_basis = PHYS.encoded_basis(
        source_eq.qubits, source_carriers, primary_sites
    )
    site_index = {site: index for index, site in enumerate(primary_sites)}
    base_observed = PHYS.conjugate_rows(
        source_basis, primary["word"], site_index
    )
    immutable_routed, immutable_route = c707.route_word(primary["word"])
    immutable = {
        "constructor_signature": str(inspect.signature(P709.primary_word)),
        "primitive_gate_count": len(primary["word"]),
        "primitive_digest": word_digest(primary["word"]),
        "routed_gate_count": len(immutable_routed),
        "routed_digest": immutable_route["word_sha256"],
        "maximum_route_distance": immutable_route["maximum_route_distance"],
        "route_failures": sum(
            immutable_route[key]
            for key in (
                "non_NN_failures",
                "operand_order_failures",
                "route_return_failures",
            )
        ),
        "runtime_frame_fields": sum(
            any(token in instruction.kind.lower() for token in (
                "frame", "coframe", "dispatch", "tag", "gauge"
            ))
            for instruction in immutable_routed
        ),
        "primary_M2": len(primary_sites),
        "input_tableau_digest": tableau_digest(source_basis),
        "output_tableau_digest": tableau_digest(base_observed),
    }
    check(
        "one immutable routed W-star is emitted with no runtime frame/tag/gauge opcode",
        immutable["constructor_signature"] == "()"
        and immutable["runtime_frame_fields"] == 0
        and immutable["route_failures"] == 0,
        immutable,
    )

    print("PHASE 24 physical chart erasures", flush=True)
    frames = K.G.c706.proper_cubic_frames()
    frame_rows = []
    transports = []
    for index, frame in enumerate(frames):
        print("FRAME", index, tuple(int(value) for value in frame.flat), flush=True)
        row, transport = frame_artifact(
            index,
            frame,
            source_eq,
            base_images,
            primary,
            source_carriers,
            source_basis,
            base_observed,
            primary_sites,
        )
        frame_rows.append(row)
        transports.append(transport)

    chart_failure_sum = sum(
        row[family][kind]
        for row in frame_rows
        for family in (
            "abstract_chart_erased_mismatch",
            "full_physical_intertwiner_mismatch",
        )
        for kind in (
            ("exact", "code")
            if "physical" in family
            else ("exact", "symplectic", "phase_only")
        )
        if kind in row[family]
    )
    unique_abstract = {
        row["abstract_chart_erased_digest"] for row in frame_rows
    }
    recovered_primitive = {
        row["recovered_base_primitive_digest"] for row in frame_rows
    }
    check(
        "all 24 verified physical actions chart-erase to one W-star exactly",
        chart_failure_sum == 0
        and unique_abstract == {tableau_digest(base_images)}
        and recovered_primitive == {immutable["primitive_digest"]}
        and sum(row["recovered_base_instruction_failures"] for row in frame_rows) == 0,
        {
            "failure_sum": chart_failure_sum,
            "abstract_digests": unique_abstract,
            "primitive_digests": recovered_primitive,
        },
    )
    address_only_nonidentity = tuple(
        row["address_only_without_chart_Clifford_mismatch"]
        for row in frame_rows if not row["is_identity"]
    )
    check(
        "address relabeling alone is separated from the executed signed-code chart Clifford",
        all(row["exact"] > 0 for row in address_only_nonidentity)
        and all(row["code"] > 0 for row in address_only_nonidentity),
        {
            "nonidentity_frames": len(address_only_nonidentity),
            "minimum_exact_mismatch": min(
                row["exact"] for row in address_only_nonidentity
            ),
            "maximum_exact_mismatch": max(
                row["exact"] for row in address_only_nonidentity
            ),
            "minimum_code_mismatch": min(
                row["code"] for row in address_only_nonidentity
            ),
            "maximum_code_mismatch": max(
                row["code"] for row in address_only_nonidentity
            ),
        },
    )
    check(
        "the original 24 pre/base/post words remain exact, local, leakage-free, and deletion-active",
        sum(row["placement_failures"] for row in frame_rows) == 0
        and sum(row["leakage_stabilizer_failures"] for row in frame_rows) == 0
        and sum(row["route_failures"] for row in frame_rows) == 0
        and min(row["minimum_detected_first_SWAP_deletions"] for row in frame_rows) > 0,
        {
            "placement_failures": sum(row["placement_failures"] for row in frame_rows),
            "leakage_failures": sum(row["leakage_stabilizer_failures"] for row in frame_rows),
            "route_failures": sum(row["route_failures"] for row in frame_rows),
            "minimum_SWAP_deletions": min(
                row["minimum_detected_first_SWAP_deletions"] for row in frame_rows
            ),
        },
    )

    print("PHASE overlap, held sizes, and 24/576", flush=True)
    storage_overlap = K.port_independent_overlap_campaign()
    active_coframe_boundary = K.independent_coframe_falsifier()
    held = held_storage_summary()
    frame_products = K.port_frame_campaign()
    common_restrictions = K.common_coframe_restriction_campaign()
    origin_frame_free = origin_and_frame_free_program_audit()
    check(
        "two fixed physical overlapping cubes accept independent passive storage charts with no transition",
        storage_overlap["independently_shuffled_cube_views"] == 2
        and storage_overlap["shared_augmented_addresses"] > 0
        and storage_overlap["independent_order_transition_terms"] == 0
        and storage_overlap["graph_A_failures"] == 0,
        storage_overlap,
    )
    check(
        "held storage charts close without refit and abstract proper-cubic 24/576 remains exact",
        held["semantic_failure_sum"] == 0
        and held["storage_transition_terms"] == 0
        and held["parameters_refit_sum"] == 0
        and frame_products["semantic_failure_sum"] == 0
        and frame_products["open_product_failures"] == 0
        and frame_products["patch_product_failures"] == 0
        and frame_products["inverse_failures"] == 0
        and frame_products["locality_failures"] == 0
        and common_restrictions["failure_checks"] == 0,
        {
            "held": held,
            "frame_products": frame_products,
            "common_restrictions": common_restrictions,
        },
    )
    check(
        "the same frame-argument-free generator closes all tested colour origins, translations, and normalized frames",
        origin_frame_free["colour_origin_exact_failure_sum"] == 0
        and origin_frame_free["fixed_origin_translation_exact_failure_sum"] == 0
        and origin_frame_free["proper_cubic_exact_failure_sum"] == 0
        and origin_frame_free["proper_cubic_frame_argument_count"] == 0,
        origin_frame_free,
    )

    print("PHASE schedule", flush=True)
    schedule = schedule_audit(primary)
    schedule_accepts = (
        schedule["same_layer_physical_support_collisions"] == 0
        and schedule["noncommuting_layer_pairs"] == 0
        and schedule["permutations_equal_to_reference"]
        == schedule["active_layer_permutations"]
    )
    check(
        "same-colour layers are locally disjoint",
        schedule["same_layer_physical_support_collisions"] == 0,
        {
            "active_layers": schedule["active_layers"],
            "collisions": schedule["same_layer_physical_support_collisions"],
        },
    )
    # This is an acceptance result, not a process failure: a noncommuting
    # residual is retained explicitly in the terminal disposition below.
    print(
        "ACCEPTANCE",
        "invariant_or_commuting_schedule",
        schedule_accepts,
        {
            "noncommuting_pairs": schedule["noncommuting_layer_pairs"],
            "active_pairs": schedule["active_layer_pairs"],
            "equal_permutations": schedule["permutations_equal_to_reference"],
            "all_permutations": schedule["active_layer_permutations"],
            "maximum_permutation_exact_mismatch": schedule[
                "maximum_permutation_exact_mismatch"
            ],
        },
        flush=True,
    )

    mass_contact = C709_RUNNER.mass_contact_regression_certificate()
    base_deletions = C709.deletion_certificate()
    active_open = max(
        (transport.open_gauge for transport in transports),
        key=lambda data: len(data.pairs) + data.flips.bit_count(),
    )
    active_patch = max(
        (transport.patch_gauge for transport in transports),
        key=lambda data: len(data.pairs) + data.flips.bit_count(),
    )
    gauge_deletions = {
        "open": K.deletion_certificate(active_open),
        "patch": K.deletion_certificate(active_patch),
    }
    primitive_deletions = PHYS.matrix_deletion_controls()
    scientific_controls = (
        mass_contact["one_particle_mass_residual"] < 3e-12
        and mass_contact["contact_vacuum_and_one_particle_residual"] < 3e-12
        and mass_contact["contact_double_occupation_phase_residual"] < 3e-12
        and min(base_deletions["delete_active_colour_failures"]) > 0
        and min(base_deletions["delete_cleanup_edge_failures"]) > 0
        and min(base_deletions["wrong_rotation_sign_failures"]) > 0
        and gauge_deletions["open"]["minimum_CZ_delete_graph_A_failures"] > 0
        and gauge_deletions["patch"]["minimum_CZ_delete_graph_A_failures"] > 0
        and primitive_deletions["minimum_delete_one_Z_S_residual"] > 0
        and primitive_deletions["minimum_delete_one_CZ_primitive_residual"] > 0
    )
    check(
        "mass/contact/seam/gauge/physical deletion controls remain active",
        scientific_controls,
        {
            "mass_contact": mass_contact,
            "base_deletions": base_deletions,
            "gauge_deletions": gauge_deletions,
            "primitive_deletions": primitive_deletions,
        },
    )

    moved = {
        "maximum_pre_gates": max(
            row["pre_gates_moved_to_passive_chart"] for row in frame_rows
        ),
        "maximum_post_gates": max(
            row["post_gates_moved_to_passive_chart"] for row in frame_rows
        ),
        "frames_with_executed_chart_Clifford_before_erasure": sum(
            row["pre_gates_moved_to_passive_chart"]
            + row["post_gates_moved_to_passive_chart"] > 0
            for row in frame_rows
        ),
        "minimum_full_gates_before_erasure": min(
            row["full_primitive_gates_before_erasure"] for row in frame_rows
        ),
        "maximum_full_gates_before_erasure": max(
            row["full_primitive_gates_before_erasure"] for row in frame_rows
        ),
    }
    status = (
        "CYCLE711_CHART_ERASED_FIXED_PROGRAM_BOUNDED_PASS"
        if FAIL == 0
        else "CYCLE711_CHART_ERASED_FIXED_PROGRAM_FAIL"
    )
    source_hashes = {
        "runner": sha256(Path(__file__).read_bytes()).hexdigest(),
        "Cycle710_physical_core": sha256(
            (ROOT / "scripts/frontier_cycle710_port_canonical_physical_core_2026_07_26.py").read_bytes()
        ).hexdigest(),
        "Cycle710_package_core": sha256(
            (ROOT / "scripts/frontier_cycle710_port_canonical_order_gauge_core_2026_07_26.py").read_bytes()
        ).hexdigest(),
        "Cycle709_physical_core": sha256(
            (ROOT / "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py").read_bytes()
        ).hexdigest(),
    }
    report = {
        "status": status,
        "checks": {"pass": PASS, "fail": FAIL},
        "source_hashes": source_hashes,
        "immutable_program": immutable,
        "frame_rows": frame_rows,
        "passive_chart_gates_removed_from_execution": moved,
        "storage_overlap": storage_overlap,
        "held_storage": held,
        "abstract_24_576": frame_products,
        "common_coframe_restrictions": common_restrictions,
        "origin_and_frame_free_program": origin_frame_free,
        "schedule": schedule,
        "mass_contact": mass_contact,
        "deletions": {
            "base": base_deletions,
            "gauge": gauge_deletions,
            "physical_primitive": primitive_deletions,
        },
        "independent_active_coframe_boundary": active_coframe_boundary,
        "inventory": {
            "supplied": (
                "one finite legacy Cycle709 reference word and its fixed chart/colour origin",
                "Cycle707 placement/repetition/rail sectors and source-sector preparation",
                "the radius-one legacy-local port key and local A orientation",
                "the declared input/output code-space chart identifications",
                "the fixed serial Manhattan route-and-return implementation",
                "Cycle219 coin and Cycle230 contact data",
            ),
            "derived_here": (
                "one frame-argument-free immutable W-star primitive and routed digest",
                "exact abstract and full-physical chart-erasure equality for all 24 common frames",
                "zero-transition descent for independent passive storage charts on a fixed overlap",
                "the exact noncommuting six-colour schedule residual",
            ),
            "not_derived": (
                "an order-free/invariant autonomous schedule; W-star retains one fixed noncommuting law-program order",
                "translation-invariant recurrent application or controller genesis",
                "an interface for independently active neighboring coframes",
                "physical preparation of code/source/work sectors",
                "off-code canonical completion, physical time, Record, probability, source, or gravity meaning",
            ),
        },
        "boundary": (
            "Common-frame dependence is exactly removable into passive input/output chart identifications "
            "on the declared code space, and passive storage charts glue without transition data.  The "
            "original W_R family nevertheless executes a nontrivial signed-code Clifford in every "
            "nonidentity frame; address relabeling alone does not remove it.  Reclassifying that Clifford "
            "as a passive code-chart identification is therefore the load-bearing chart convention.  The "
            "surviving immutable W-star uses one noncommuting fixed six-colour order.  The same frame-free "
            "bounded generator closes every tested origin/translation/frame, so this is a supplied "
            "law-program order wall rather than a coframe register, but an order-free schedule has not "
            "been derived.  Independently active neighboring "
            "coframes are a different unclosed interface.  No impossibility or axiom-pressure claim is made."
        ),
    }
    payload = json.dumps(json_ready(report), sort_keys=True, separators=(",", ":"))
    print(json.dumps(json_ready(report), indent=2, sort_keys=True))
    print("REPORT_SHA256", sha256(payload.encode()).hexdigest())
    print("RUNNER_SHA256", source_hashes["runner"])
    print(status)
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
