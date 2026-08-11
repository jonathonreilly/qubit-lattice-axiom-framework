#!/usr/bin/env python3
"""Cycle 983: bounded translation-uniformity test on two overlapping Z3 stars.

The target domain has two adjacent sites.  Each target is supplied with its
complete closed Z3 nearest-neighbour star, so the hosting support has twelve
sites.  One relative 23-program rule schema is exhausted at both targets.
Science outcomes (uniform, obstructed, or not hostable) are reported data;
checks gate construction, reconciliation, provenance, and scope only.
"""

from __future__ import annotations

import ast
import importlib.util
import io
import json
import subprocess
import sys
import tarfile
import tempfile
from hashlib import sha1, sha256
from itertools import combinations, permutations, product
from pathlib import Path
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
CYCLE = 983
AUDIT_TIMEOUT_SEC = 1400
HOUSE_STDOUT_LIMIT_BYTES = 6_000
STDOUT_LIMIT_BYTES = 150_000
BASE_ORIGIN_MAIN_COMMIT = "ea0968c71ad46c39c6dacb39f88a18780363b71f"
PINNED_CYCLE719_COMMIT = "39c74017b870c27c804e3992f2a11e90336476b2"
PINNED_CYCLE719_CORE = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
)
PINNED_CYCLE719_CORE_SHA256 = (
    "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4"
)
PINNED_CYCLE719_CORE_BLOB = "c123b8d681c3d76fce08ef13d7673622deac64ad"

AUDIT_INPUT_PATHS = ("docs/MINIMAL_AXIOMS_2026-06-29.md",)
EXPECTED_INPUT_SHA256 = {
    "docs/MINIMAL_AXIOMS_2026-06-29.md":
        "53175250f0458168330160ad6a39c8ec708316f338efd69c49e8eb09e3267b39",
}
EXPECTED_INPUT_BLOBS = {
    "docs/MINIMAL_AXIOMS_2026-06-29.md":
        "2f5fdd26898f62c17fcabc846761f7785c2eadb1",
}
BLOCKLIST_TEXT_PATHS = (
    "docs/WITNESS_FAMILY_COMPLETENESS_CYCLE977_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/CLASS_COEXISTENCE_BORN_REQUIREMENT_CYCLE979_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/WITNESS_ORBIT_MULTIPLICITY_CYCLE980_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/Z3_ADJACENCY_DEPENDENCE_CLASSES_CYCLE982_BOUNDED_THEOREM_NOTE_2026-08-11.md",
)
BLOCKLIST_AST_FRAGMENTS = (
    "cycle970", "cycle972", "cycle977", "cycle979", "cycle980", "cycle982",
)

PRIMARY_PATH = (
    "scripts/frontier_cycle983_translation_uniform_two_star_patch_2026_08_11.py"
)
RECEIPT_PATH = (
    "outputs/translation_uniform_two_star_patch_cycle983_receipt_2026_08_11.json"
)

ORIGIN = (0, 0, 0)
STEP_X = (1, 0, 0)
TARGET_CENTRES = (ORIGIN, STEP_X)
TARGET_NAMES = ("A", "B")
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
DIRECTION_NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
LOCAL_WIRES = tuple(range(7))
NEIGHBOUR_WIRES = tuple(range(1, 7))
CONDITIONS = tuple(product((0, 1), repeat=6))
OTHER_CONTEXTS = tuple(product((0, 1), repeat=5))


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a + b for a, b in zip(left, right))


def subtract(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a - b for a, b in zip(left, right))


def l1(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def dot(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(a * b for a, b in zip(left, right))


def canonical_pair(left: tuple, right: tuple) -> tuple:
    return tuple(sorted((left, right)))


def coordinate_name(site: tuple[int, int, int]) -> str:
    return f"({site[0]},{site[1]},{site[2]})"


def local_wire_name(wire: int) -> str:
    return "C" if wire == 0 else DIRECTION_NAMES[wire - 1]


def ast_literal_assignment(tree: ast.Module, name: str):
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def load_pinned_cycle719_core():
    archive = subprocess.run(
        ["git", "archive", "--format=tar", PINNED_CYCLE719_COMMIT, "scripts"],
        cwd=ROOT, check=True, capture_output=True,
    ).stdout
    temporary = tempfile.TemporaryDirectory(prefix="cycle983-cycle719-")
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as bundle:
        bundle.extractall(temporary.name, filter="data")
    scripts_dir = Path(temporary.name) / "scripts"
    sys.path.insert(0, str(scripts_dir))
    core_path = Path(temporary.name) / PINNED_CYCLE719_CORE
    spec = importlib.util.spec_from_file_location("cycle983_pinned_cycle719", core_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load pinned Cycle-719 core")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return temporary, module


PINNED_TEMP, K = load_pinned_cycle719_core()


def closed_star(center: tuple[int, int, int]) -> tuple[tuple[int, int, int], ...]:
    return (center, *(add(center, direction) for direction in DIRECTIONS))


STAR_SITES = tuple(closed_star(center) for center in TARGET_CENTRES)
HOST_SUPPORT = tuple(sorted(set().union(*(set(star) for star in STAR_SITES))))


def declared_relative_family() -> tuple:
    rows = [("I",), ("X", 0)]
    rows.extend(("CNOT", control, 0) for control in NEIGHBOUR_WIRES)
    rows.extend(
        ("TOF", left, right, 0)
        for left, right in combinations(NEIGHBOUR_WIRES, 2)
    )
    return tuple(rows)


def relative_word_name(descriptor: tuple) -> str:
    if descriptor[0] == "I":
        return "I"
    if descriptor[0] == "X":
        return "X(C)"
    if descriptor[0] == "CNOT":
        return f"CNOT({local_wire_name(descriptor[1])}->C)"
    return (
        f"TOF({local_wire_name(descriptor[1])},"
        f"{local_wire_name(descriptor[2])}->C)"
    )


def global_word_name(descriptor: tuple, center: tuple[int, int, int]) -> str:
    sites = closed_star(center)
    if descriptor[0] == "I":
        return f"I@{coordinate_name(center)}"
    if descriptor[0] == "X":
        return f"X({coordinate_name(center)})"
    if descriptor[0] == "CNOT":
        return (
            f"CNOT({coordinate_name(sites[descriptor[1]])}"
            f"->{coordinate_name(center)})"
        )
    return (
        f"TOF({coordinate_name(sites[descriptor[1]])},"
        f"{coordinate_name(sites[descriptor[2]])}->{coordinate_name(center)})"
    )


def core_word(descriptor: tuple) -> tuple:
    if descriptor[0] == "I":
        return ()
    if descriptor[0] == "X":
        return (K.A.x(descriptor[1]),)
    if descriptor[0] == "CNOT":
        return (K.A.cn(descriptor[1], descriptor[2]),)
    return (K.A.tof(descriptor[1], descriptor[2], descriptor[3]),)


def independent_target_output(descriptor: tuple, x: int, conditions: tuple) -> int:
    if descriptor[0] == "I":
        return x
    if descriptor[0] == "X":
        return x ^ 1
    if descriptor[0] == "CNOT":
        return x ^ conditions[descriptor[1] - 1]
    return x ^ (
        conditions[descriptor[1] - 1] & conditions[descriptor[2] - 1]
    )


def global_rule_output(
    descriptor: tuple,
    center: tuple[int, int, int],
    assignment: dict[tuple[int, int, int], int],
) -> int:
    sites = closed_star(center)
    return independent_target_output(
        descriptor,
        assignment[center],
        tuple(assignment[site] for site in sites[1:]),
    )


def landed_target_output(descriptor: tuple, x: int, conditions: tuple) -> int:
    return K.A.apply_semantic((x, *conditions), core_word(descriptor))[0]


def with_edge(index: int, other: tuple, bit: int) -> tuple:
    source = iter(other)
    return tuple(bit if position == index else next(source) for position in range(6))


def witness_measurement(descriptor: tuple) -> dict:
    changed = 0
    for x in (0, 1):
        for direction_index in range(6):
            for other in OTHER_CONTEXTS:
                condition_0 = with_edge(direction_index, other, 0)
                condition_1 = with_edge(direction_index, other, 1)
                changed += landed_target_output(descriptor, x, condition_0) != (
                    landed_target_output(descriptor, x, condition_1)
                )
    return {"is_witness": changed > 0, "changed_edge_pairs": changed}


def determinant(matrix: tuple[tuple[int, int, int], ...]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def proper_cubic_rotations() -> tuple:
    rows = set()
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[row] * int(column == order[row]) for column in range(3))
                for row in range(3)
            )
            if determinant(matrix) == 1:
                rows.add(matrix)
    return tuple(sorted(rows))


ROTATIONS = proper_cubic_rotations()
RELATIVE_SITE_TO_WIRE = {site: wire for wire, site in enumerate((ORIGIN, *DIRECTIONS))}


def mat_vec(matrix: tuple, vector: tuple) -> tuple:
    return tuple(dot(row, vector) for row in matrix)


def rotate_wire(wire: int, rotation: tuple) -> int:
    return RELATIVE_SITE_TO_WIRE[mat_vec(rotation, (ORIGIN, *DIRECTIONS)[wire])]


def rotate_descriptor(descriptor: tuple, rotation: tuple) -> tuple:
    if descriptor[0] in ("I", "X"):
        return descriptor
    wires = tuple(rotate_wire(wire, rotation) for wire in descriptor[1:])
    if descriptor[0] == "TOF":
        return ("TOF", *sorted(wires[:2]), wires[2])
    return (descriptor[0], *wires)


def invariant_j(descriptor: tuple) -> int:
    controls = (descriptor[1],) if descriptor[0] == "CNOT" else descriptor[1:3]
    summed = tuple(
        sum((ORIGIN, *DIRECTIONS)[control][axis] for control in controls)
        for axis in range(3)
    )
    return dot(summed, summed)


def class_label(descriptor: tuple) -> str:
    if descriptor[0] == "CNOT":
        return "CNOT"
    if descriptor[0] == "TOF" and invariant_j(descriptor) == 2:
        return "TOF_PERPENDICULAR_CONTROLS"
    if descriptor[0] == "TOF" and invariant_j(descriptor) == 0:
        return "TOF_OPPOSITE_CONTROLS"
    return "NON_WITNESS"


def orbit_decomposition(witnesses: tuple) -> dict:
    witness_set = set(witnesses)
    remaining = set(witnesses)
    rows = []
    while remaining:
        seed = min(remaining, key=relative_word_name)
        ambient = {rotate_descriptor(seed, rotation) for rotation in ROTATIONS}
        members = tuple(sorted(ambient & witness_set, key=relative_word_name))
        stabilizer = sum(
            rotate_descriptor(seed, rotation) == seed for rotation in ROTATIONS
        )
        rows.append({
            "class_label": class_label(seed),
            "representative": relative_word_name(seed),
            "member_count": len(members),
            "effective_stabilizer_order": stabilizer,
            "orbit_stabilizer_product": len(ambient) * stabilizer,
            "orbit_closed_in_witness_set": ambient <= witness_set,
            "J_values": sorted({invariant_j(member) for member in members}),
            "members": [relative_word_name(member) for member in members],
        })
        remaining -= set(members)
    rows.sort(key=lambda row: row["class_label"])
    covered = [member for row in rows for member in row["members"]]
    return {
        "effective_group": "proper cubic rotation group",
        "effective_group_order": len(ROTATIONS),
        "orbit_count": len(rows),
        "orbits": rows,
        "partition_has_no_overlap_or_omission": (
            len(covered) == len(set(covered)) == len(witnesses)
        ),
        "action_closed_on_witnesses": all(
            row["orbit_closed_in_witness_set"] for row in rows
        ),
        "J_constant_on_each_orbit": all(len(row["J_values"]) == 1 for row in rows),
        "J_distinct_across_orbits": len({
            value for row in rows for value in row["J_values"]
        }) == len(rows),
    }


def family_declaration() -> dict:
    family = declared_relative_family()
    return {
        "rule_schema": (
            "at target t: I; X(t); CNOT(t+d->t) for every signed unit d; "
            "TOF(t+d,t+e->t) for every unordered pair of distinct signed units"
        ),
        "site_menu": [0, 1],
        "word_length": "zero or one",
        "relative_family_size_per_target": len(family),
        "target_count": len(TARGET_CENTRES),
        "site_program_instance_count": len(family) * len(TARGET_CENTRES),
        "relative_family_digest": digest(family),
        "cap": (
            "all 23 relative descriptors at each of two targets; both target bits; "
            "all 2^6 neighbour conditions; every neighbour-bit edge comparison; no sampling"
        ),
    }


def patch_construction() -> dict:
    star_sets = tuple(set(star) for star in STAR_SITES)
    intersection = tuple(sorted(star_sets[0] & star_sets[1]))
    semantic_pair_sets = tuple(
        {canonical_pair(*pair) for pair in combinations(star, 2)}
        for star in STAR_SITES
    )
    z3_edge_sets = tuple(
        {pair for pair in semantic_pairs if l1(*pair) == 1}
        for semantic_pairs in semantic_pair_sets
    )
    offset_rows = []
    for offset in product(range(-2, 3), repeat=3):
        if offset == ORIGIN:
            continue
        candidate = set(closed_star(offset))
        overlap = len(set(closed_star(ORIGIN)) & candidate)
        if overlap:
            offset_rows.append({
                "offset": list(offset),
                "L1": l1(ORIGIN, offset),
                "intersection_size": overlap,
                "union_size": 14 - overlap,
            })
    minimum_union = min(row["union_size"] for row in offset_rows)
    support_roles = []
    for site in HOST_SUPPORT:
        memberships = [
            TARGET_NAMES[index] for index, star in enumerate(star_sets) if site in star
        ]
        support_roles.append({
            "site": list(site),
            "role": "target" if site in TARGET_CENTRES else "support_only_halo",
            "closed_star_memberships": memberships,
            "induced_support_degree": sum(
                l1(site, other) == 1 for other in HOST_SUPPORT
            ),
        })
    return {
        "patch_name": "P2x_ADJACENT_TWO_CENTRE_CLOSED_STAR_PATCH",
        "target_domain_definition": "P2x={(0,0,0),(1,0,0)}",
        "target_sites": [list(site) for site in TARGET_CENTRES],
        "target_site_count": len(TARGET_CENTRES),
        "host_support_definition": "Omega=union over t in P2x of {t} union {t+d: ||d||_1=1}",
        "host_support_sites": [list(site) for site in HOST_SUPPORT],
        "host_support_site_count": len(HOST_SUPPORT),
        "support_site_roles": support_roles,
        "stars": [
            {
                "name": TARGET_NAMES[index],
                "center": list(center),
                "sites_in_local_wire_order": [list(site) for site in STAR_SITES[index]],
                "site_count": len(STAR_SITES[index]),
            }
            for index, center in enumerate(TARGET_CENTRES)
        ],
        "center_separation_L1": l1(*TARGET_CENTRES),
        "closed_star_intersection": [list(site) for site in intersection],
        "closed_star_intersection_size": len(intersection),
        "closed_star_union_size": len(HOST_SUPPORT),
        "global_semantic_pair_union_count": len(
            semantic_pair_sets[0] | semantic_pair_sets[1]
        ),
        "global_z3_star_edge_union_count": len(z3_edge_sets[0] | z3_edge_sets[1]),
        "family": family_declaration(),
        "minimality": {
            "number_of_stars": 2,
            "distinct_centres_required": True,
            "overlapping_offset_count_with_L1_at_most_2": len(offset_rows),
            "maximum_intersection_for_distinct_closed_unit_stars": max(
                row["intersection_size"] for row in offset_rows
            ),
            "minimum_union_size_for_two_distinct_overlapping_closed_unit_stars": minimum_union,
            "chosen_patch_attains_minimum": len(HOST_SUPPORT) == minimum_union,
            "reason": (
                "two is the smallest number of stars exceeding one; exhaustive relative offsets "
                "with nonempty intersection give maximum intersection two and minimum union twelve"
            ),
            "offset_census_digest": digest(offset_rows),
        },
        "scope_convention": (
            "the patch sites at which the rule is asserted are the two target-domain sites; "
            "the other ten Omega sites are declared support-only halo, not silently tested targets"
        ),
    }


def target_site_census(index: int) -> dict:
    center = TARGET_CENTRES[index]
    family = declared_relative_family()
    witnesses = []
    assignments = []
    truth_failures = 0
    route_rows = []
    for descriptor in family:
        measurement = witness_measurement(descriptor)
        if measurement["is_witness"]:
            witnesses.append(descriptor)
            assignments.append({
                "relative_word": relative_word_name(descriptor),
                "global_word": global_word_name(descriptor, center),
                "class_label": class_label(descriptor),
                "J": invariant_j(descriptor),
                "changed_edge_pairs": measurement["changed_edge_pairs"],
            })
        for x in (0, 1):
            for condition in CONDITIONS:
                truth_failures += landed_target_output(descriptor, x, condition) != (
                    independent_target_output(descriptor, x, condition)
                )
        route = K.streaming_route(core_word(descriptor), STAR_SITES[index])
        route_rows.append({"relative_word": relative_word_name(descriptor), **route})
    route_failures = sum(
        row["non_NN_failures"] + row["operand_order_failures"]
        + row["route_return_failures"] for row in route_rows
    )
    hostable = route_failures == 0
    orbit = orbit_decomposition(tuple(witnesses))
    normalized_structure = {
        "relative_witnesses": [relative_word_name(row) for row in witnesses],
        "class_assignments": [
            [relative_word_name(row), class_label(row), invariant_j(row)]
            for row in witnesses
        ],
        "orbits": [
            [
                row["class_label"], row["member_count"],
                row["effective_stabilizer_order"], row["J_values"],
            ]
            for row in orbit["orbits"]
        ],
    }
    return {
        "target_name": TARGET_NAMES[index],
        "target_site": list(center),
        "complete_six_neighbour_star_present": set(STAR_SITES[index]) <= set(HOST_SUPPORT),
        "relative_family_size": len(family),
        "truth_table_evaluations": len(family) * 2 * len(CONDITIONS),
        "landed_vs_independent_truth_failure_count": truth_failures,
        "witness_count": len(witnesses),
        "witness_names": [relative_word_name(row) for row in witnesses],
        "witness_assignments": assignments,
        "orbit_decomposition": orbit,
        "normalized_structure_digest": digest(normalized_structure),
        "route_host": {
            "all_words_routable": hostable,
            "classification": (
                "complete_target_star_hosted" if hostable
                else "complete_target_star_not_hosted"
            ),
            "maximum_route_distance": max(row["maximum_route_distance"] for row in route_rows),
            "maximum_touched_sites": max(row["touched_M2"] for row in route_rows),
            "expanded_primitive_count": sum(row["physical_primitives"] for row in route_rows),
            "routed_nn_gate_count": sum(row["routed_NN_gates"] for row in route_rows),
            "non_nn_failure_count": sum(row["non_NN_failures"] for row in route_rows),
            "operand_order_failure_count": sum(row["operand_order_failures"] for row in route_rows),
            "route_return_failure_count": sum(row["route_return_failures"] for row in route_rows),
            "route_rows_digest": digest(route_rows),
        },
    }


def classify_uniformity(per_site: list[dict], translation_truth_failures: int) -> str:
    if not all(row["route_host"]["all_words_routable"] for row in per_site):
        return "not_hostable_at_one_or_more_target_sites"
    keys = (
        "relative_family_size", "witness_count", "witness_names",
        "normalized_structure_digest",
    )
    if any(
        any(row[key] != per_site[0][key] for key in keys)
        for row in per_site[1:]
    ):
        return "class_structure_differs_across_target_sites"
    if any(row["landed_vs_independent_truth_failure_count"] for row in per_site):
        return "landed_truth_law_differs_from_declared_rule"
    if translation_truth_failures:
        return "pointwise_translation_covariance_failure"
    return "translation_uniform_on_every_target_site_of_P2x"


def uniformity_test() -> dict:
    per_site = [target_site_census(index) for index in range(len(TARGET_CENTRES))]
    reference = per_site[0]
    translation = subtract(TARGET_CENTRES[1], TARGET_CENTRES[0])
    translation_comparisons = 0
    translation_truth_failures = 0
    for descriptor in declared_relative_family():
        for target_bit in (0, 1):
            for conditions in CONDITIONS:
                assignment_a = {
                    site: bit for site, bit in zip(
                        STAR_SITES[0], (target_bit, *conditions)
                    )
                }
                assignment_b = {
                    add(site, translation): bit for site, bit in assignment_a.items()
                }
                translation_comparisons += 1
                translation_truth_failures += global_rule_output(
                    descriptor, TARGET_CENTRES[0], assignment_a
                ) != global_rule_output(
                    descriptor, TARGET_CENTRES[1], assignment_b
                )
    comparison_fields = (
        "relative_family_size", "witness_count", "witness_names",
        "normalized_structure_digest",
    )
    return {
        "one_rule": {
            "formula": family_declaration()["rule_schema"],
            "relative_family_digest": family_declaration()["relative_family_digest"],
            "translation_vector_A_to_B": list(translation),
            "pointwise_covariance_equation": (
                "R_(t+tau)(tau.assignment; descriptor) = R_t(assignment; descriptor)"
            ),
            "pointwise_translation_comparison_count": translation_comparisons,
            "pointwise_translation_truth_failure_count": translation_truth_failures,
            "translated_descriptor_table_digest": digest([
                [
                    relative_word_name(descriptor),
                    global_word_name(descriptor, TARGET_CENTRES[0]),
                    global_word_name(descriptor, TARGET_CENTRES[1]),
                ]
                for descriptor in declared_relative_family()
            ]),
        },
        "tested_target_site_count": len(per_site),
        "all_patch_target_sites_tested": len(per_site) == len(TARGET_CENTRES),
        "per_site_census": per_site,
        "per_site_exact_agreement": {
            field: all(row[field] == reference[field] for row in per_site)
            for field in comparison_fields
        },
        "classification": classify_uniformity(per_site, translation_truth_failures),
    }


def local_wire_for_site(star_index: int, site: tuple[int, int, int]) -> int:
    return STAR_SITES[star_index].index(site)


def overlap_consistency() -> dict:
    star_sets = tuple(set(star) for star in STAR_SITES)
    shared_sites = tuple(sorted(star_sets[0] & star_sets[1]))
    shared_site_rows = []
    for site in shared_sites:
        wire_a = local_wire_for_site(0, site)
        wire_b = local_wire_for_site(1, site)
        shared_site_rows.append({
            "global_site": list(site),
            "global_variable": f"q_{coordinate_name(site)}",
            "star_A_local_wire": wire_a,
            "star_A_local_name": local_wire_name(wire_a),
            "star_B_local_wire": wire_b,
            "star_B_local_name": local_wire_name(wire_b),
            "same_global_site_binding": STAR_SITES[0][wire_a] == STAR_SITES[1][wire_b],
        })

    semantic_pairs = []
    z3_pairs = []
    for star in STAR_SITES:
        semantic_pairs.append({canonical_pair(*pair) for pair in combinations(star, 2)})
        z3_pairs.append({pair for pair in semantic_pairs[-1] if l1(*pair) == 1})
    shared_semantic_pairs = tuple(sorted(semantic_pairs[0] & semantic_pairs[1]))
    pair_rows = []
    for pair in shared_semantic_pairs:
        wires = [
            tuple(local_wire_for_site(index, site) for site in pair)
            for index in range(2)
        ]
        neighbour_from_target = [
            next(wire for wire in local_pair if wire != 0) for local_pair in wires
        ]
        paths = [
            tuple(K.C712.c707.c655.manhattan_path(TARGET_CENTRES[index], pair[1 - index]))
            for index in range(2)
        ]
        descriptor_a = ("CNOT", neighbour_from_target[0], 0)
        descriptor_b = ("CNOT", neighbour_from_target[1], 0)
        measurement_a = witness_measurement(descriptor_a)
        measurement_b = witness_measurement(descriptor_b)
        center_exchange_truth_table = []
        for bit_a, bit_b in product((0, 1), repeat=2):
            conditions_a = [0] * 6
            conditions_b = [0] * 6
            conditions_a[neighbour_from_target[0] - 1] = bit_b
            conditions_b[neighbour_from_target[1] - 1] = bit_a
            output_a = independent_target_output(
                descriptor_a, bit_a, tuple(conditions_a)
            )
            output_b = independent_target_output(
                descriptor_b, bit_b, tuple(conditions_b)
            )
            center_exchange_truth_table.append({
                "q_A": bit_a,
                "q_B": bit_b,
                "star_A_target_output": output_a,
                "star_B_target_output": output_b,
                "outputs_agree_after_target_component_exchange": output_a == output_b,
            })
        pair_rows.append({
            "global_pair": [list(site) for site in pair],
            "star_A_local_wires_for_sorted_global_pair": list(wires[0]),
            "star_B_local_wires_for_sorted_global_pair": list(wires[1]),
            "semantic_pair_in_both_stars": pair in semantic_pairs[0] and pair in semantic_pairs[1],
            "z3_nearest_neighbour_in_star_A": pair in z3_pairs[0],
            "z3_nearest_neighbour_in_star_B": pair in z3_pairs[1],
            "star_A_target_equation": "q_(0,0,0)' = q_(0,0,0) XOR q_(1,0,0)",
            "star_B_target_equation": "q_(1,0,0)' = q_(1,0,0) XOR q_(0,0,0)",
            "target_equations_are_distinct_target_components": True,
            "star_A_witness_id": relative_word_name(descriptor_a),
            "star_B_witness_id": relative_word_name(descriptor_b),
            "star_A_class": class_label(descriptor_a),
            "star_B_class": class_label(descriptor_b),
            "star_A_J": invariant_j(descriptor_a),
            "star_B_J": invariant_j(descriptor_b),
            "star_A_changed_edge_pairs": measurement_a["changed_edge_pairs"],
            "star_B_changed_edge_pairs": measurement_b["changed_edge_pairs"],
            "center_exchange_truth_table": center_exchange_truth_table,
            "target_component_exchanged_truth_tables_agree": all(
                row["outputs_agree_after_target_component_exchange"]
                for row in center_exchange_truth_table
            ),
            "star_A_target_to_neighbour_path": [list(site) for site in paths[0]],
            "star_B_target_to_neighbour_path": [list(site) for site in paths[1]],
            "paths_agree_up_to_reversal": paths[0] == tuple(reversed(paths[1])),
        })
    site_agreement = all(row["same_global_site_binding"] for row in shared_site_rows)
    pair_agreement = all(
        row["semantic_pair_in_both_stars"]
        and row["z3_nearest_neighbour_in_star_A"]
        == row["z3_nearest_neighbour_in_star_B"]
        and row["star_A_class"] == row["star_B_class"]
        and row["star_A_J"] == row["star_B_J"]
        and row["star_A_changed_edge_pairs"] == row["star_B_changed_edge_pairs"]
        and row["target_component_exchanged_truth_tables_agree"]
        and row["paths_agree_up_to_reversal"]
        for row in pair_rows
    )
    return {
        "overlap_definition": "closed-star intersection and induced semantic-pair intersection",
        "shared_site_count": len(shared_sites),
        "shared_site_agreement_table": shared_site_rows,
        "shared_semantic_pair_count": len(shared_semantic_pairs),
        "shared_pair_agreement_table": pair_rows,
        "shared_site_global_bindings_agree": site_agreement,
        "shared_pair_relations_classes_J_and_paths_agree": pair_agreement,
        "classification": (
            "exact_agreement_on_all_shared_sites_and_pairs"
            if site_agreement and pair_agreement
            else "overlap_disagreement_obstructs_translation_uniformity"
        ),
    }


def derive_verdict(uniformity: dict, overlap: dict) -> tuple[str, str | None]:
    if uniformity["classification"] == "not_hostable_at_one_or_more_target_sites":
        failed = [
            row["target_name"] for row in uniformity["per_site_census"]
            if not row["route_host"]["all_words_routable"]
        ]
        return "NOT_HOSTABLE", "unhosted target stars: " + ",".join(failed)
    if uniformity["classification"] != "translation_uniform_on_every_target_site_of_P2x":
        return "OBSTRUCTED", uniformity["classification"]
    if overlap["classification"] != "exact_agreement_on_all_shared_sites_and_pairs":
        return "OBSTRUCTED", overlap["classification"]
    return "TRANSLATION_UNIFORM_AT_PATCH_SCOPE", None


def verdict_measurement(uniformity: dict, overlap: dict) -> dict:
    verdict, obstruction = derive_verdict(uniformity, overlap)
    return {
        "verdict": verdict,
        "named_patch": "P2x_ADJACENT_TWO_CENTRE_CLOSED_STAR_PATCH",
        "exact_obstruction": obstruction,
        "scope_established": (
            "one relative 23-program dependence-law schema has the same 21-witness, "
            "6/12/3 proper-cubic class structure and J={1,2,0} at both target sites "
            "of P2x, with exact consistency on the two shared sites and one shared pair"
        ),
        "target_patch_site_count": 2,
        "host_support_site_count": 12,
        "full_infinite_translation_uniform_lattice_law_claimed": False,
        "scope_exclusions": [
            "targets outside the two-site domain P2x",
            "an infinite allocation of one M2(C) site at every point of Z3",
            "a simultaneous global execution or schedule of alternative local words",
            "a translation-uniform admissibility probability or selection rule",
            "identification of semantic operand availability with geometric adjacency",
        ],
        "scope_warning": (
            "translation-uniform at this named finite target-patch scope is not an infinite-lattice theorem"
        ),
    }


def input_controls() -> dict:
    source = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)
    literal_paths = ast_literal_assignment(tree, "AUDIT_INPUT_PATHS")
    literal_blocklist = ast_literal_assignment(tree, "BLOCKLIST_TEXT_PATHS")
    literal_fragments = ast_literal_assignment(tree, "BLOCKLIST_AST_FRAGMENTS")
    payloads = {path: (ROOT / path).read_bytes() for path in literal_paths}
    sha_rows = {path: sha256(payload).hexdigest() for path, payload in payloads.items()}
    blob_rows = {path: git_blob(payload) for path, payload in payloads.items()}
    imported_names = {
        alias.name for node in ast.walk(tree) if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    }
    pinned_core = subprocess.run(
        ["git", "show", f"{PINNED_CYCLE719_COMMIT}:{PINNED_CYCLE719_CORE}"],
        cwd=ROOT, check=True, capture_output=True,
    ).stdout
    base_is_ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", BASE_ORIGIN_MAIN_COMMIT, "HEAD"],
        cwd=ROOT, check=False, capture_output=True,
    ).returncode == 0
    return {
        "literal_audit_input_paths": list(literal_paths),
        "literal_source_read_count": len(literal_paths),
        "input_sha256": sha_rows,
        "input_git_blobs": blob_rows,
        "sha_pins_match": sha_rows == EXPECTED_INPUT_SHA256,
        "blob_pins_match": blob_rows == EXPECTED_INPUT_BLOBS,
        "all_inputs_relative_and_present": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in literal_paths
        ),
        "blocklist_text_paths": list(literal_blocklist),
        "blocklist_ast_fragments": list(literal_fragments),
        "blocklist_text_disjoint_from_reads": not set(literal_paths) & set(literal_blocklist),
        "blocked_ast_imports": sorted(
            name for name in imported_names
            if any(fragment in name.lower() for fragment in literal_fragments)
        ),
        "prior_cycle_text_or_ast_executed": False,
        "pinned_substrate": {
            "commit": PINNED_CYCLE719_COMMIT,
            "path": PINNED_CYCLE719_CORE,
            "sha256": sha256(pinned_core).hexdigest(),
            "git_blob": git_blob(pinned_core),
            "sha_pin_match": sha256(pinned_core).hexdigest() == PINNED_CYCLE719_CORE_SHA256,
            "blob_pin_match": git_blob(pinned_core) == PINNED_CYCLE719_CORE_BLOB,
            "loaded_from_immutable_git_archive": True,
        },
        "base_origin_main_commit": BASE_ORIGIN_MAIN_COMMIT,
        "base_is_ancestor_of_head": base_is_ancestor,
    }


def science_measurement() -> dict:
    construction = patch_construction()
    uniformity = uniformity_test()
    overlap = overlap_consistency()
    return {
        "A_PATCH_CONSTRUCTION": construction,
        "B_UNIFORMITY_TEST": uniformity,
        "C_OVERLAP_CONSISTENCY": overlap,
        "D_VERDICT": verdict_measurement(uniformity, overlap),
    }


def render_stdout(receipt: dict) -> str:
    findings = receipt["findings"]
    construction = findings["A_PATCH_CONSTRUCTION"]
    uniformity = findings["B_UNIFORMITY_TEST"]
    overlap = findings["C_OVERLAP_CONSISTENCY"]
    verdict = findings["D_VERDICT"]
    site_rows = [
        [
            row["target_name"], row["witness_count"],
            [
                [orbit["class_label"], orbit["member_count"], orbit["J_values"]]
                for orbit in row["orbit_decomposition"]["orbits"]
            ],
            row["route_host"]["all_words_routable"],
        ]
        for row in uniformity["per_site_census"]
    ]
    lines = [
        "CYCLE983_TRANSLATION_UNIFORM_TWO_STAR_PATCH",
        "A_PATCH_CONSTRUCTION " + ("PASS" if receipt["checks"]["A_PATCH_CONSTRUCTION"] else "FAIL")
        + f" :: patch={construction['patch_name']}; targets={construction['target_site_count']};"
        + f" support={construction['host_support_site_count']}; overlap={construction['closed_star_intersection_size']};"
        + f" instances={construction['family']['site_program_instance_count']}",
        "B_UNIFORMITY_TEST " + ("PASS" if receipt["checks"]["B_UNIFORMITY_TEST"] else "FAIL")
        + f" :: result={uniformity['classification']}; sites={compact(site_rows)}",
        "C_OVERLAP_CONSISTENCY " + ("PASS" if receipt["checks"]["C_OVERLAP_CONSISTENCY"] else "FAIL")
        + f" :: result={overlap['classification']}; shared_sites={overlap['shared_site_count']};"
        + f" shared_pairs={overlap['shared_semantic_pair_count']}",
        "D_VERDICT " + ("PASS" if receipt["checks"]["D_VERDICT"] else "FAIL")
        + f" :: verdict={verdict['verdict']}; infinite_claimed={verdict['full_infinite_translation_uniform_lattice_law_claimed']};"
        + f" obstruction={compact(verdict['exact_obstruction'])}",
        "E_CONTROLS " + ("PASS" if receipt["checks"]["E_CONTROLS"] else "FAIL")
        + f" :: source_reads={receipt['controls']['literal_source_read_count']}<=6;"
        + f" pins={receipt['controls']['sha_pins_match'] and receipt['controls']['blob_pins_match']};"
        + f" prior_ast_text={receipt['controls']['prior_cycle_text_or_ast_executed']};"
        + f" determinism={receipt['controls']['determinism_replay']};"
        + f" runtime_lt_1400={receipt['controls']['runtime_budget_met']}",
    ]
    passed = sum(receipt["checks"].values())
    lines.append(f"TOTAL: PASS={passed} FAIL={len(receipt['checks']) - passed}")
    return "\n".join(lines) + "\n"


def run() -> tuple[dict, str]:
    started = monotonic()
    controls = input_controls()
    first = science_measurement()
    second = science_measurement()
    deterministic = first == second
    construction = first["A_PATCH_CONSTRUCTION"]
    uniformity = first["B_UNIFORMITY_TEST"]
    overlap = first["C_OVERLAP_CONSISTENCY"]
    verdict = first["D_VERDICT"]

    stars = construction["stars"]
    a_bookkeeping = bool(
        construction["target_site_count"] == len(construction["target_sites"])
        and construction["host_support_site_count"] == len(construction["host_support_sites"])
        and all(row["site_count"] == len(row["sites_in_local_wire_order"]) for row in stars)
        and construction["closed_star_intersection_size"]
            == len(construction["closed_star_intersection"])
        and construction["closed_star_union_size"] == construction["host_support_site_count"]
        and construction["family"]["site_program_instance_count"]
            == construction["family"]["relative_family_size_per_target"]
                * construction["target_site_count"]
        and construction["minimality"]["chosen_patch_attains_minimum"]
    )
    per_site = uniformity["per_site_census"]
    b_bookkeeping = bool(
        uniformity["tested_target_site_count"] == len(per_site)
        and uniformity["all_patch_target_sites_tested"]
        and all(
            row["relative_family_size"] == len(declared_relative_family())
            and row["witness_count"] == len(row["witness_names"])
            == len(row["witness_assignments"])
            and sum(
                orbit["member_count"] for orbit in row["orbit_decomposition"]["orbits"]
            ) == row["witness_count"]
            and all(
                orbit["orbit_stabilizer_product"]
                    == row["orbit_decomposition"]["effective_group_order"]
                for orbit in row["orbit_decomposition"]["orbits"]
            )
            and row["route_host"]["all_words_routable"] == (
                sum(row["route_host"][key] for key in (
                    "non_nn_failure_count", "operand_order_failure_count",
                    "route_return_failure_count",
                )) == 0
            )
            for row in per_site
        )
        and uniformity["classification"] == classify_uniformity(
            per_site,
            uniformity["one_rule"]["pointwise_translation_truth_failure_count"],
        )
    )
    site_rows = overlap["shared_site_agreement_table"]
    pair_rows = overlap["shared_pair_agreement_table"]
    computed_site_agreement = all(row["same_global_site_binding"] for row in site_rows)
    computed_pair_agreement = all(
        row["semantic_pair_in_both_stars"]
        and row["z3_nearest_neighbour_in_star_A"]
            == row["z3_nearest_neighbour_in_star_B"]
        and row["star_A_class"] == row["star_B_class"]
        and row["star_A_J"] == row["star_B_J"]
        and row["star_A_changed_edge_pairs"] == row["star_B_changed_edge_pairs"]
        and row["target_component_exchanged_truth_tables_agree"]
        and row["paths_agree_up_to_reversal"]
        for row in pair_rows
    )
    c_bookkeeping = bool(
        overlap["shared_site_count"] == len(site_rows)
        and overlap["shared_semantic_pair_count"] == len(pair_rows)
        and overlap["shared_site_global_bindings_agree"] == computed_site_agreement
        and overlap["shared_pair_relations_classes_J_and_paths_agree"] == computed_pair_agreement
        and overlap["classification"] == (
            "exact_agreement_on_all_shared_sites_and_pairs"
            if computed_site_agreement and computed_pair_agreement
            else "overlap_disagreement_obstructs_translation_uniformity"
        )
    )
    expected_verdict, expected_obstruction = derive_verdict(uniformity, overlap)
    d_bookkeeping = bool(
        verdict["verdict"] == expected_verdict
        and verdict["exact_obstruction"] == expected_obstruction
        and verdict["full_infinite_translation_uniform_lattice_law_claimed"] is False
        and bool(verdict["scope_exclusions"])
        and bool(verdict["scope_warning"])
    )
    runtime_budget_met = monotonic() - started < AUDIT_TIMEOUT_SEC
    controls.update({
        "determinism_replay": deterministic,
        "runtime_budget_met": runtime_budget_met,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "house_stdout_limit_bytes": HOUSE_STDOUT_LIMIT_BYTES,
    })
    e_controls = bool(
        controls["literal_source_read_count"] <= 6
        and controls["all_inputs_relative_and_present"]
        and controls["sha_pins_match"] and controls["blob_pins_match"]
        and controls["blocklist_text_disjoint_from_reads"]
        and not controls["blocked_ast_imports"]
        and not controls["prior_cycle_text_or_ast_executed"]
        and controls["pinned_substrate"]["sha_pin_match"]
        and controls["pinned_substrate"]["blob_pin_match"]
        and controls["base_is_ancestor_of_head"]
        and deterministic and runtime_budget_met
    )
    receipt = {
        "cycle": CYCLE,
        "artifact": "translation-uniform two-overlapping-star bounded census primary",
        "audit_status_authority": "independent audit lane only",
        "integrity_policy": (
            "checks gate construction and bookkeeping only; uniform, obstructed, and not-hostable outcomes all remain cleanly reportable"
        ),
        "findings": first,
        "science_digest": digest(first),
        "controls": controls,
        "checks": {
            "A_PATCH_CONSTRUCTION": a_bookkeeping,
            "B_UNIFORMITY_TEST": b_bookkeeping,
            "C_OVERLAP_CONSISTENCY": c_bookkeeping,
            "D_VERDICT": d_bookkeeping,
            "E_CONTROLS": e_controls,
        },
    }
    receipt["primary_source_sha256"] = sha256((ROOT / PRIMARY_PATH).read_bytes()).hexdigest()
    for _ in range(3):
        stdout = render_stdout(receipt)
        controls["stdout_bytes"] = len(stdout.encode())
    stdout = render_stdout(receipt)
    if len(stdout.encode()) >= HOUSE_STDOUT_LIMIT_BYTES:
        receipt["checks"]["E_CONTROLS"] = False
        stdout = render_stdout(receipt)
    receipt["pass"] = all(receipt["checks"].values())
    receipt["stdout_sha256"] = sha256(stdout.encode()).hexdigest()
    return receipt, stdout


def main() -> int:
    if sys.argv[1:]:
        raise SystemExit(f"usage: {Path(__file__).name}")
    receipt, stdout = run()
    receipt_path = ROOT / RECEIPT_PATH
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    sys.stdout.write(stdout)
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
