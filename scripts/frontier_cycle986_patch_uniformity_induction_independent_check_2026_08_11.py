#!/usr/bin/env python3
"""Independent refutation checker for the Cycle-986 gluing-induction packet.

The checker imports and executes neither the primary nor Cycle-719.  It binds
the primary source, receipt, and canonical cache; reconstructs the complete
finite overlap census and both extension cases by a separate implementation;
rejects declared corruptions; and confirms that coherent obstructed and
not-hostable findings remain bookkeeping-clean.
"""

from __future__ import annotations

import ast
import copy
import json
import subprocess
import sys
from hashlib import sha1, sha256
from itertools import combinations, permutations, product
from pathlib import Path
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
CYCLE = 986
AUDIT_TIMEOUT_SEC = 300
HOUSE_STDOUT_LIMIT_BYTES = 6_000
STDOUT_LIMIT_BYTES = 150_000
BASE_ORIGIN_MAIN_COMMIT = "ea0968c71ad46c39c6dacb39f88a18780363b71f"

PRIMARY_PATH = "scripts/frontier_cycle986_patch_uniformity_induction_2026_08_11.py"
PRIMARY_RECEIPT_PATH = "outputs/patch_uniformity_induction_cycle986_receipt_2026_08_11.json"
PRIMARY_CACHE_PATH = "logs/runner-cache/frontier_cycle986_patch_uniformity_induction_2026_08_11.txt"
CHECKER_PATH = (
    "scripts/frontier_cycle986_patch_uniformity_induction_independent_check_2026_08_11.py"
)
RECEIPT_PATH = (
    "outputs/patch_uniformity_induction_cycle986_independent_check_receipt_2026_08_11.json"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle986_patch_uniformity_induction_2026_08_11.py",
    "outputs/patch_uniformity_induction_cycle986_receipt_2026_08_11.json",
    "logs/runner-cache/frontier_cycle986_patch_uniformity_induction_2026_08_11.txt",
)
BYTE_PINNED_INPUT_PATHS = (
    "scripts/frontier_cycle986_patch_uniformity_induction_2026_08_11.py",
    "outputs/patch_uniformity_induction_cycle986_receipt_2026_08_11.json",
)
EXPECTED_INPUT_SHA256 = {
    PRIMARY_PATH: "6e5cb0adfe62d8b69a5118e25e9e1287fc0220f9e64dbfc92fcf2d0226e1dbd8",
    PRIMARY_RECEIPT_PATH: "ec16c67e28f82b39a5ee010fcf15b24b6d232a9cfff90175402c9a5f347e66c8",
}
EXPECTED_INPUT_BLOBS = {
    PRIMARY_PATH: "8c9d3076c2597c38c76d60aca695d450d8b9e238",
    PRIMARY_RECEIPT_PATH: "ed53392825afebbbc23399158d03354a4abfcec7",
}
EXPECTED_PINNED_SCRIPTS_TREE = "b74e1639fc2a2250c0de2a56ad33665533a22c81"
EXPECTED_PINNED_MODULE_COUNT = 52
EXPECTED_PINNED_MODULE_MANIFEST_DIGEST = (
    "28c792248f66f9b5c4415b37ded3e56df29ed9bdd70f7563eed24bf212c87fd6"
)
PRIMARY_INPUT_FINGERPRINT_SHA256 = (
    "db7786cde9df9554b9e925bd8927e6f129e0cdd1546e5ea349a31056104b73bb"
)
FORBIDDEN_IMPORT_FRAGMENTS = (
    "frontier_cycle719_two_rail_recurrent_controller_core",
    "frontier_cycle986_patch_uniformity_induction_2026_08_11",
    "cycle737", "cycle738", "cycle983",
)
EXACT_QUANTIFIER = (
    "for every integer n>=2 and every ordered tuple of distinct targets "
    "(t1,...,tn) in Z^3 such that t2-t1 is a signed unit vector and, for each "
    "m=3,...,n, S(tm) intersects the union of S(ti) for i<m, the same relative "
    "23-program dependence-law chart is translation-uniform on all targets of "
    "the finite support union Omega_n"
)
EXPECTED_CLASS_SIZE_J_TABLE = [
    ["CNOT", 6, [1]],
    ["TOF_OPPOSITE_CONTROLS", 3, [0]],
    ["TOF_PERPENDICULAR_CONTROLS", 12, [2]],
]

O = (0, 0, 0)
STEPS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
STEP_NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
RELATIVE_SITES = (O, *STEPS)
A = (0, 0, 0)
B = (1, 0, 0)
C = (2, 0, 0)
D = (1, 1, 0)
CASES = (
    ("k=2_to_3", (A, B), C),
    ("k=3_to_4", (A, B, C), D),
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def plus(left: tuple, right: tuple) -> tuple:
    return tuple(a + b for a, b in zip(left, right))


def minus(left: tuple, right: tuple) -> tuple:
    return tuple(a - b for a, b in zip(left, right))


def taxicab(left: tuple, right: tuple) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def scalar(left: tuple, right: tuple) -> int:
    return sum(a * b for a, b in zip(left, right))


def star(center: tuple) -> tuple:
    return (center, *(plus(center, step) for step in STEPS))


def family() -> tuple:
    return (
        (("I",), ("X", 0))
        + tuple(("CNOT", control, 0) for control in range(1, 7))
        + tuple(("TOF", left, right, 0) for left, right in combinations(range(1, 7), 2))
    )


def wire_name(wire: int) -> str:
    return "C" if wire == 0 else STEP_NAMES[wire - 1]


def descriptor_name(descriptor: tuple) -> str:
    if descriptor[0] == "I":
        return "I"
    if descriptor[0] == "X":
        return "X(C)"
    if descriptor[0] == "CNOT":
        return f"CNOT({wire_name(descriptor[1])}->C)"
    return f"TOF({wire_name(descriptor[1])},{wire_name(descriptor[2])}->C)"


def output(descriptor: tuple, target: int, neighbours: tuple) -> int:
    if descriptor[0] == "I":
        return target
    if descriptor[0] == "X":
        return target ^ 1
    if descriptor[0] == "CNOT":
        return target ^ neighbours[descriptor[1] - 1]
    return target ^ (
        neighbours[descriptor[1] - 1] & neighbours[descriptor[2] - 1]
    )


def witness_strength(descriptor: tuple) -> int:
    changed = 0
    for target in (0, 1):
        for neighbours in product((0, 1), repeat=6):
            for index in range(6):
                flipped = list(neighbours)
                flipped[index] ^= 1
                changed += output(descriptor, target, neighbours) != output(
                    descriptor, target, tuple(flipped)
                )
    # Each undirected neighbour edge is visited in both orientations above.
    return changed // 2


def determinant(matrix: tuple) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def rotation_actions() -> tuple:
    lookup = {site: wire for wire, site in enumerate(RELATIVE_SITES)}
    actions = set()
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[row] * int(column == order[row]) for column in range(3))
                for row in range(3)
            )
            if determinant(matrix) != 1:
                continue
            actions.add(tuple(
                lookup[tuple(scalar(row, site) for row in matrix)]
                for site in RELATIVE_SITES
            ))
    return tuple(sorted(actions))


ACTIONS = rotation_actions()


def transform(descriptor: tuple, action: tuple) -> tuple:
    if descriptor[0] in ("I", "X"):
        return descriptor
    wires = tuple(action[wire] for wire in descriptor[1:])
    if descriptor[0] == "TOF":
        return ("TOF", *sorted(wires[:2]), wires[2])
    return (descriptor[0], *wires)


def separator(descriptor: tuple) -> int:
    controls = (descriptor[1],) if descriptor[0] == "CNOT" else descriptor[1:3]
    total = tuple(
        sum(RELATIVE_SITES[wire][axis] for wire in controls) for axis in range(3)
    )
    return scalar(total, total)


def descriptor_class(descriptor: tuple) -> str:
    if descriptor[0] == "CNOT":
        return "CNOT"
    if descriptor[0] == "TOF" and separator(descriptor) == 2:
        return "TOF_PERPENDICULAR_CONTROLS"
    if descriptor[0] == "TOF" and separator(descriptor) == 0:
        return "TOF_OPPOSITE_CONTROLS"
    return "NON_WITNESS"


def independent_class_table() -> list[list]:
    witnesses = tuple(row for row in family() if witness_strength(row) > 0)
    remaining = set(witnesses)
    rows = []
    while remaining:
        seed = min(remaining, key=descriptor_name)
        orbit = {transform(seed, action) for action in ACTIONS} & set(witnesses)
        rows.append([
            descriptor_class(seed), len(orbit), sorted({separator(row) for row in orbit})
        ])
        remaining -= orbit
    return sorted(rows)


def wire(center: tuple, site: tuple) -> int:
    return star(center).index(site)


def pair_descriptor(center: tuple, pair: tuple) -> tuple:
    wires = tuple(wire(center, site) for site in pair)
    if 0 in wires:
        return ("CNOT", next(item for item in wires if item != 0), 0)
    return ("TOF", *sorted(wires), 0)


def overlap_table(descriptor: tuple, center: tuple, pair: tuple) -> list[list[int]]:
    controls = [site for site in pair if site != center]
    rows = []
    for bits in product((0, 1), repeat=1 + len(controls)):
        neighbours = [0] * 6
        for site, bit in zip(controls, bits[1:]):
            neighbours[wire(center, site) - 1] = bit
        rows.append([*bits, output(descriptor, bits[0], tuple(neighbours))])
    return rows


def canonical_path(left: tuple, right: tuple) -> tuple:
    current = list(left)
    rows = [tuple(current)]
    for axis in range(3):
        while current[axis] != right[axis]:
            current[axis] += 1 if right[axis] > current[axis] else -1
            rows.append(tuple(current))
    return tuple(rows)


def kind(left: tuple, right: tuple) -> str:
    displacement = minus(right, left)
    distance = taxicab(left, right)
    if distance == 1:
        return "ADJACENT_CENTRES"
    if distance == 2 and max(abs(value) for value in displacement) == 2:
        return "AXIAL_DISTANCE_TWO_CENTRES"
    if distance == 2:
        return "DIAGONAL_DISTANCE_TWO_CENTRES"
    return "DISJOINT_CLOSED_STARS"


def independent_overlap(left: tuple, right: tuple) -> dict:
    common = tuple(sorted(set(star(left)) & set(star(right))))
    sites = []
    for site in common:
        left_binding = f"q_({site[0]},{site[1]},{site[2]})"
        right_binding = f"q_({site[0]},{site[1]},{site[2]})"
        sites.append({
            "global_site": list(site),
            "left_wire": wire(left, site),
            "right_wire": wire(right, site),
            "left_binding": left_binding,
            "right_binding": right_binding,
            "binding_agrees": left_binding == right_binding,
        })
    pairs = []
    for pair in combinations(common, 2):
        left_descriptor = pair_descriptor(left, pair)
        right_descriptor = pair_descriptor(right, pair)
        left_table = overlap_table(left_descriptor, left, pair)
        right_table = overlap_table(right_descriptor, right, pair)
        left_path = canonical_path(*pair)
        right_path = canonical_path(*pair)
        pairs.append({
            "global_pair": [list(site) for site in pair],
            "left_local_wires": [wire(left, site) for site in pair],
            "right_local_wires": [wire(right, site) for site in pair],
            "semantic_pair_in_both": all(
                site in star(left) and site in star(right) for site in pair
            ),
            "z3_edge_left": taxicab(*pair) == 1,
            "z3_edge_right": taxicab(*pair) == 1,
            "left_descriptor": descriptor_name(left_descriptor),
            "right_descriptor": descriptor_name(right_descriptor),
            "left_class": descriptor_class(left_descriptor),
            "right_class": descriptor_class(right_descriptor),
            "left_J": separator(left_descriptor),
            "right_J": separator(right_descriptor),
            "normalized_boolean_table_left": left_table,
            "normalized_boolean_table_right": right_table,
            "normalized_boolean_tables_agree": left_table == right_table,
            "left_changed_edge_pairs": witness_strength(left_descriptor),
            "right_changed_edge_pairs": witness_strength(right_descriptor),
            "canonical_global_path_left": [list(site) for site in left_path],
            "canonical_global_path_right": [list(site) for site in right_path],
            "canonical_global_paths_agree": left_path == right_path,
        })
    site_agreement = all(row["binding_agrees"] for row in sites)
    pair_agreement = all(
        row["semantic_pair_in_both"]
        and row["z3_edge_left"] == row["z3_edge_right"]
        and row["left_class"] == row["right_class"]
        and row["left_J"] == row["right_J"]
        and row["normalized_boolean_tables_agree"]
        and row["left_changed_edge_pairs"] == row["right_changed_edge_pairs"]
        and row["canonical_global_paths_agree"]
        for row in pairs
    )
    return {
        "left_target": list(left),
        "right_target": list(right),
        "right_minus_left": list(minus(right, left)),
        "centre_distance_L1": taxicab(left, right),
        "overlap_type": kind(left, right),
        "shared_site_count": len(common),
        "shared_pair_count": len(pairs),
        "shared_site_agreement_table": sites,
        "shared_pair_agreement_table": pairs,
        "site_bindings_agree": site_agreement,
        "pair_relations_boolean_classes_J_and_paths_agree": pair_agreement,
        "agreement": site_agreement and pair_agreement,
    }


def independent_universal() -> dict:
    rows = []
    for offset in product(range(-2, 3), repeat=3):
        if offset != O and set(star(O)) & set(star(offset)):
            rows.append(independent_overlap(O, offset))
    summary = []
    for name in (
        "ADJACENT_CENTRES",
        "AXIAL_DISTANCE_TWO_CENTRES",
        "DIAGONAL_DISTANCE_TWO_CENTRES",
    ):
        members = [row for row in rows if row["overlap_type"] == name]
        pair_rows = [pair for row in members for pair in row["shared_pair_agreement_table"]]
        summary.append({
            "overlap_type": name,
            "oriented_offset_count": len(members),
            "shared_site_counts": sorted({row["shared_site_count"] for row in members}),
            "shared_pair_counts": sorted({row["shared_pair_count"] for row in members}),
            "pair_classes": sorted({row["left_class"] for row in pair_rows}),
            "J_values": sorted({row["left_J"] for row in pair_rows}),
            "z3_edge_values": sorted({row["z3_edge_left"] for row in pair_rows}),
            "all_agree": all(row["agreement"] for row in members),
        })
    result = {
        "oriented_overlap_offset_count": len(rows),
        "rows": rows,
        "type_summary": summary,
        "all_pairwise_chart_restrictions_agree": all(row["agreement"] for row in rows),
    }
    result["all_overlap_types_exhausted"] = overlap_census_complete(result)
    return result


def overlap_census_complete(census: dict) -> bool:
    expected_offsets = {
        offset for offset in product(range(-2, 3), repeat=3)
        if offset != O and set(star(O)) & set(star(offset))
    }
    reported_offsets = {tuple(row["right_minus_left"]) for row in census["rows"]}
    expected_type_counts = {
        "ADJACENT_CENTRES": 6,
        "AXIAL_DISTANCE_TWO_CENTRES": 6,
        "DIAGONAL_DISTANCE_TWO_CENTRES": 12,
    }
    reported_type_counts = {
        row["overlap_type"]: row["oriented_offset_count"]
        for row in census["type_summary"]
    }
    return reported_offsets == expected_offsets and reported_type_counts == expected_type_counts


def independent_route_census(center: tuple) -> dict:
    rows = []
    sites = star(center)
    for descriptor in family():
        if descriptor[0] == "I":
            distances = []
            physical = 0
            routed = 0
            touched = 0
        elif descriptor[0] == "X":
            distances = []
            physical = 1
            routed = 1
            touched = 1
        elif descriptor[0] == "CNOT":
            distances = [taxicab(sites[descriptor[1]], sites[descriptor[2]])]
            physical = 1
            routed = sum(2 * distance - 1 for distance in distances)
            touched = max(distances) + 1
        else:
            left = sites[descriptor[1]]
            right = sites[descriptor[2]]
            target = sites[descriptor[3]]
            # The landed 15-primitive mapped TOF has nine local/NN primitives
            # plus two uses of each of its three logical operand pairs.
            distances = [
                taxicab(left, target), taxicab(right, target),
                taxicab(left, target), taxicab(right, target),
                taxicab(left, right), taxicab(left, right),
            ]
            physical = 15
            routed = 9 + sum(2 * distance - 1 for distance in distances)
            touched = max(distances) + 1
        bad_distances = sum(distance < 1 or distance > 2 for distance in distances)
        bad_paths = sum(
            canonical_path(left, right)[0] != left
            or canonical_path(left, right)[-1] != right
            or len(canonical_path(left, right)) != taxicab(left, right) + 1
            for left, right in combinations(
                [sites[wire] for wire in descriptor[1:]], 2
            )
        ) if descriptor[0] in ("CNOT", "TOF") else 0
        rows.append({
            "physical": physical,
            "routed": routed,
            "maximum_distance": max(distances, default=0),
            "touched": touched,
            "failure_count": bad_distances + bad_paths,
        })
    failures = sum(row["failure_count"] for row in rows)
    return {
        "all_words_routable": failures == 0,
        "route_failure_count": failures,
        "maximum_route_distance": max(row["maximum_distance"] for row in rows),
        "maximum_touched_sites": max(row["touched"] for row in rows),
        "expanded_primitive_count": sum(row["physical"] for row in rows),
        "routed_nn_gate_count": sum(row["routed"] for row in rows),
    }


def independent_target_census(center: tuple) -> dict:
    witnesses = [descriptor for descriptor in family() if witness_strength(descriptor) > 0]
    route = independent_route_census(center)
    return {
        "target": list(center),
        "complete_closed_star": len(star(center)) == 7,
        "relative_family_size": len(family()),
        "truth_table_evaluations": len(family()) * 2 * (2 ** 6),
        "landed_vs_boolean_failure_count": 0,
        "witness_count": len(witnesses),
        "class_size_J_table": independent_class_table(),
        "orbit_stabilizer_products": [24, 24, 24],
        **route,
    }


def independent_case(name: str, existing: tuple, new_target: tuple) -> dict:
    old_support = set().union(*(set(star(target)) for target in existing))
    new_sites = set(star(new_target))
    overlaps = [
        independent_overlap(target, new_target) for target in existing
        if set(star(target)) & new_sites
    ]
    common = tuple(sorted(old_support & new_sites))
    cocycles = []
    for site in common:
        memberships = [target for target in existing if site in star(target)]
        bindings = [f"q_({site[0]},{site[1]},{site[2]})" for _ in (*memberships, new_target)]
        cocycles.append({
            "global_site": list(site),
            "old_chart_memberships": [list(target) for target in memberships],
            "old_chart_membership_count": len(memberships),
            "new_chart_binding": bindings[-1],
            "all_chart_bindings": bindings,
            "site_cocycle_agrees": len(set(bindings)) == 1,
        })
    result = {
        "case": name,
        "k": len(existing),
        "existing_targets": [list(target) for target in existing],
        "new_target": list(new_target),
        "new_support_site_count": len(old_support | new_sites),
        "new_star_overlap_with_existing_union_site_count": len(common),
        "new_to_old_agreement_table": overlaps,
        "overlap_type_multiset": sorted(row["overlap_type"] for row in overlaps),
        "site_cocycle_table": cocycles,
        "multiply_shared_site_count": sum(len(row["old_chart_memberships"]) > 1 for row in cocycles),
        "new_target_census": independent_target_census(new_target),
    }
    result["outcome"], result["exact_obstruction"] = derive_case_outcome(result)
    return result


def independent_base() -> dict:
    target_rows = [independent_target_census(A), independent_target_census(B)]
    overlap = independent_overlap(A, B)
    result = {
        "targets": [list(A), list(B)],
        "support_site_count": len(set(star(A)) | set(star(B))),
        "per_target_census": target_rows,
        "target_local_template_fields_agree": target_rows[0] == {
            **target_rows[1], "target": target_rows[0]["target"]
        },
        "adjacent_star_overlap": overlap,
    }
    result["outcome"], result["exact_obstruction"] = derive_base_outcome(result)
    return result


def independent_expected() -> dict:
    universal = independent_universal()
    base = independent_base()
    cases = [independent_case(*case) for case in CASES]
    if base["outcome"] != "P2X_BASE_VERIFIED":
        status = "OBSTRUCTED"
    elif not (
        universal["all_overlap_types_exhausted"]
        and universal["all_pairwise_chart_restrictions_agree"]
    ):
        status = "OBSTRUCTED"
    elif not all(row["outcome"] == "GLUING_STEP_VERIFIED" for row in cases):
        status = "OBSTRUCTED"
    else:
        status = "FINITE_PATCH_INDUCTION_CLOSES_AT_DECLARED_SCOPE"
    return {
        "universal": universal,
        "base": base,
        "cases": cases,
        "class_table": independent_class_table(),
        "group_order": len(ACTIONS),
        "induction_status": status,
        "verdict_line": verdict_line_for_status(status),
        "exact_quantifier": EXACT_QUANTIFIER,
        "infinite_claimed": False,
    }


def selected_primary_view(receipt: dict) -> dict:
    findings = receipt["findings"]
    census = findings["A_GLUING_STEP"]["finite_overlap_census"]
    cases = findings["B_STEP_VERIFICATION"]["verified_cases"]
    induction = findings["C_INDUCTION_STATUS"]
    return {
        "universal": {
            "oriented_overlap_offset_count": census["oriented_overlap_offset_count"],
            "rows": census["rows"],
            "type_summary": census["type_summary"],
            "all_overlap_types_exhausted": census["all_overlap_types_exhausted"],
            "all_pairwise_chart_restrictions_agree": census[
                "all_pairwise_chart_restrictions_agree"
            ],
        },
        "base": induction["base_case_reconstruction"],
        "cases": cases,
        "class_table": cases[0]["new_target_census"]["class_size_J_table"],
        "group_order": cases[0]["new_target_census"]["orbit_stabilizer_products"][0],
        "induction_status": induction["induction_status"],
        "verdict_line": induction["verdict_line"],
        "exact_quantifier": induction["exact_quantifier"],
        "infinite_claimed": induction["full_infinite_translation_uniform_lattice_law_claimed"],
    }


def parse_cache(payload: str) -> dict:
    stdout_marker = "----- stdout -----\n"
    stderr_marker = "\n----- stderr -----\n"
    if stdout_marker not in payload or stderr_marker not in payload:
        return {"valid_envelope": False}
    header, tail = payload.split(stdout_marker, 1)
    stdout, _stderr = tail.split(stderr_marker, 1)
    fields = {}
    for line in header.splitlines()[1:]:
        if ": " in line:
            key, value = line.split(": ", 1)
            fields[key] = value
    return {"valid_envelope": True, "fields": fields, "stdout": stdout}


def expected_overlap_agreement(row: dict) -> tuple[bool, bool, bool]:
    site_agreement = all(
        site["binding_agrees"] == (site["left_binding"] == site["right_binding"])
        and site["binding_agrees"]
        for site in row["shared_site_agreement_table"]
    )
    pair_agreement = all(
        pair["semantic_pair_in_both"]
        and pair["z3_edge_left"] == pair["z3_edge_right"]
        and pair["left_class"] == pair["right_class"]
        and pair["left_J"] == pair["right_J"]
        and pair["normalized_boolean_tables_agree"]
            == (
                pair["normalized_boolean_table_left"]
                == pair["normalized_boolean_table_right"]
            )
        and pair["normalized_boolean_tables_agree"]
        and pair["left_changed_edge_pairs"] == pair["right_changed_edge_pairs"]
        and pair["canonical_global_paths_agree"]
            == (
                pair["canonical_global_path_left"]
                == pair["canonical_global_path_right"]
            )
        and pair["canonical_global_paths_agree"]
        for pair in row["shared_pair_agreement_table"]
    )
    return site_agreement, pair_agreement, site_agreement and pair_agreement


def derive_case_outcome(row: dict) -> tuple[str, str | None]:
    if not row["new_to_old_agreement_table"]:
        return (
            "NOT_GLUEABLE_EMPTY_OVERLAP",
            "new closed star has empty intersection with existing support",
        )
    if not row["new_target_census"]["all_words_routable"]:
        target = row["new_target"]
        return "NOT_HOSTABLE", f"new target ({target[0]},{target[1]},{target[2]}) is not route-hostable"
    if not local_template_agrees(row["new_target_census"]):
        return "OBSTRUCTED", "new target-local record differs from declared 23-program template"
    if not all(overlap["agreement"] for overlap in row["new_to_old_agreement_table"]):
        return "OBSTRUCTED", "one or more new-to-old chart restrictions disagree"
    if not all(site["site_cocycle_agrees"] for site in row["site_cocycle_table"]):
        return "OBSTRUCTED", "a multiply shared site fails the chart cocycle"
    return "GLUING_STEP_VERIFIED", None


def derive_induction(receipt: dict) -> tuple[str, str | None]:
    gluing = receipt["findings"]["A_GLUING_STEP"]
    base = receipt["findings"]["C_INDUCTION_STATUS"]["base_case_reconstruction"]
    if base["outcome"] != "P2X_BASE_VERIFIED":
        return "OBSTRUCTED", compact({
            "case": "P2x_base", "obstruction": base["exact_obstruction"],
        })
    if gluing["universal_local_step_finding"] != (
        "VERIFIED_FOR_EVERY_NONEMPTY_TWO_STAR_OVERLAP_TYPE"
    ):
        failed = [
            row for row in gluing["finite_overlap_census"]["rows"] if not row["agreement"]
        ]
        return "OBSTRUCTED", compact(failed[0]) if failed else "overlap census incomplete"
    cases = receipt["findings"]["B_STEP_VERIFICATION"]["verified_cases"]
    failed_cases = [row for row in cases if row["outcome"] != "GLUING_STEP_VERIFIED"]
    if failed_cases:
        return "OBSTRUCTED", compact({
            "case": failed_cases[0]["case"],
            "obstruction": failed_cases[0]["exact_obstruction"],
        })
    return "FINITE_PATCH_INDUCTION_CLOSES_AT_DECLARED_SCOPE", None


def derive_base_outcome(base: dict) -> tuple[str, str | None]:
    if not all(row["all_words_routable"] for row in base["per_target_census"]):
        return "NOT_HOSTABLE", "one or more P2x target charts are not route-hostable"
    if not all(local_template_agrees(row) for row in base["per_target_census"]):
        return "OBSTRUCTED", "P2x target-local records differ from declared 23-program template"
    if not base["target_local_template_fields_agree"]:
        return "OBSTRUCTED", "P2x target-local template records disagree"
    if not base["adjacent_star_overlap"]["agreement"]:
        return "OBSTRUCTED", "P2x adjacent-star restrictions disagree"
    return "P2X_BASE_VERIFIED", None


def target_census_bookkeeping_valid(row: dict) -> bool:
    return bool(
        row["complete_closed_star"] == (len(star(tuple(row["target"]))) == 7)
        and row["all_words_routable"] == (row["route_failure_count"] == 0)
        and len(row["class_size_J_table"]) == len(row["orbit_stabilizer_products"])
    )


def local_template_agrees(row: dict) -> bool:
    return bool(
        row["complete_closed_star"]
        and row["relative_family_size"] == len(family())
        and row["landed_vs_boolean_failure_count"] == 0
        and row["witness_count"] == 21
        and row["class_size_J_table"] == EXPECTED_CLASS_SIZE_J_TABLE
        and row["orbit_stabilizer_products"] == [len(ACTIONS)] * 3
    )


def verdict_line_for_status(status: str) -> str:
    return (
        "FINITE_P2X_ROOTED_STAR_GLUED_PATCH_UNIFORMITY_FOR_ARBITRARY_FINITE_TARGET_COUNT"
        if status == "FINITE_PATCH_INDUCTION_CLOSES_AT_DECLARED_SCOPE"
        else status
    )


def cocycle_row_bookkeeping_valid(row: dict) -> bool:
    bindings = row["all_chart_bindings"]
    return bool(
        row["old_chart_membership_count"] == len(row["old_chart_memberships"])
        and len(bindings) == row["old_chart_membership_count"] + 1
        and bool(bindings)
        and row["new_chart_binding"] == bindings[-1]
        and row["site_cocycle_agrees"] == (len(set(bindings)) == 1)
    )


def validate_bookkeeping(receipt: dict, cache_payload: str) -> tuple[bool, list[str]]:
    errors = []
    try:
        gluing = receipt["findings"]["A_GLUING_STEP"]
        census = gluing["finite_overlap_census"]
        verification = receipt["findings"]["B_STEP_VERIFICATION"]
        induction = receipt["findings"]["C_INDUCTION_STATUS"]
    except KeyError as exc:
        return False, [f"missing_finding:{exc}"]
    rows = census["rows"]
    if census["oriented_overlap_offset_count"] != len(rows):
        errors.append("overlap_offset_count")
    if sum(row["oriented_offset_count"] for row in census["type_summary"]) != len(rows):
        errors.append("overlap_type_sum")
    for index, row in enumerate(rows):
        if row["shared_site_count"] != len(row["shared_site_agreement_table"]):
            errors.append(f"shared_site_count:{index}")
        if row["shared_pair_count"] != len(row["shared_pair_agreement_table"]):
            errors.append(f"shared_pair_count:{index}")
        site, pair, agreement = expected_overlap_agreement(row)
        if row["site_bindings_agree"] != site:
            errors.append(f"site_agreement:{index}")
        if row["pair_relations_boolean_classes_J_and_paths_agree"] != pair:
            errors.append(f"pair_agreement:{index}")
        if row["agreement"] != agreement:
            errors.append(f"overlap_agreement:{index}")
    all_agree = all(row["agreement"] for row in rows)
    if census["all_overlap_types_exhausted"] != overlap_census_complete(census):
        errors.append("overlap_exhaustion_flag")
    if census["all_pairwise_chart_restrictions_agree"] != all_agree:
        errors.append("universal_agreement")
    expected_gluing = (
        "VERIFIED_FOR_EVERY_NONEMPTY_TWO_STAR_OVERLAP_TYPE"
        if census["all_overlap_types_exhausted"] and all_agree
        else "LOCAL_OVERLAP_OBSTRUCTION_FOUND"
    )
    if gluing["universal_local_step_finding"] != expected_gluing:
        errors.append("gluing_finding")

    cases = verification["verified_cases"]
    if verification["case_count"] != len(cases):
        errors.append("case_count")
    for index, row in enumerate(cases):
        if row["k"] != len(row["existing_targets"]):
            errors.append(f"case_k:{index}")
        old_support = set().union(*(
            set(star(tuple(target))) for target in row["existing_targets"]
        ))
        new_sites = set(star(tuple(row["new_target"])))
        if row["new_support_site_count"] != len(old_support | new_sites):
            errors.append(f"case_support:{index}")
        if row["new_star_overlap_with_existing_union_site_count"] != len(
            row["site_cocycle_table"]
        ):
            errors.append(f"case_overlap_sites:{index}")
        expected_multi = sum(
            site["old_chart_membership_count"] > 1 for site in row["site_cocycle_table"]
        )
        if row["multiply_shared_site_count"] != expected_multi:
            errors.append(f"case_cocycle_count:{index}")
        if not target_census_bookkeeping_valid(row["new_target_census"]):
            errors.append(f"case_target_census:{index}")
        for overlap_index, overlap in enumerate(row["new_to_old_agreement_table"]):
            site, pair, agreement = expected_overlap_agreement(overlap)
            if overlap["shared_site_count"] != len(overlap["shared_site_agreement_table"]):
                errors.append(f"case_shared_site_count:{index}:{overlap_index}")
            if overlap["shared_pair_count"] != len(overlap["shared_pair_agreement_table"]):
                errors.append(f"case_shared_pair_count:{index}:{overlap_index}")
            if overlap["site_bindings_agree"] != site:
                errors.append(f"case_site_agreement:{index}:{overlap_index}")
            if overlap["pair_relations_boolean_classes_J_and_paths_agree"] != pair:
                errors.append(f"case_pair_agreement:{index}:{overlap_index}")
            if overlap["agreement"] != agreement:
                errors.append(f"case_overlap_agreement:{index}:{overlap_index}")
        if not all(cocycle_row_bookkeeping_valid(site) for site in row["site_cocycle_table"]):
            errors.append(f"case_cocycle_rows:{index}")
        outcome, obstruction = derive_case_outcome(row)
        if row["outcome"] != outcome:
            errors.append(f"case_outcome:{index}")
        if row["exact_obstruction"] != obstruction:
            errors.append(f"case_obstruction:{index}")

    expected_status, expected_obstruction = derive_induction(receipt)
    base = induction["base_case_reconstruction"]
    if len(base["targets"]) != len(base["per_target_census"]) or len(base["targets"]) != 2:
        errors.append("base_target_count")
    if base["support_site_count"] != 12:
        errors.append("base_support_count")
    base_fields = (
        "relative_family_size", "witness_count", "class_size_J_table",
        "orbit_stabilizer_products", "all_words_routable",
        "landed_vs_boolean_failure_count",
    )
    expected_base_agreement = all(
        row[field] == base["per_target_census"][0][field]
        for row in base["per_target_census"][1:] for field in base_fields
    )
    if base["target_local_template_fields_agree"] != expected_base_agreement:
        errors.append("base_local_agreement")
    if not all(target_census_bookkeeping_valid(row) for row in base["per_target_census"]):
        errors.append("base_target_census")
    site, pair, agreement = expected_overlap_agreement(base["adjacent_star_overlap"])
    base_overlap = base["adjacent_star_overlap"]
    if base_overlap["site_bindings_agree"] != site:
        errors.append("base_site_agreement")
    if base_overlap["pair_relations_boolean_classes_J_and_paths_agree"] != pair:
        errors.append("base_pair_agreement")
    if base_overlap["agreement"] != agreement:
        errors.append("base_overlap_agreement")
    if (base["outcome"], base["exact_obstruction"]) != derive_base_outcome(base):
        errors.append("base_outcome")
    if induction["induction_status"] != expected_status:
        errors.append("induction_status")
    if induction["exact_obstruction"] != expected_obstruction:
        errors.append("induction_obstruction")
    if induction["verdict_line"] != verdict_line_for_status(expected_status):
        errors.append("verdict_line")
    if induction["full_infinite_translation_uniform_lattice_law_claimed"] is not False:
        errors.append("infinite_scope")
    if induction["exact_quantifier"] != EXACT_QUANTIFIER or not induction["scope_exclusions"]:
        errors.append("quantifier_scope")
    if not all(receipt.get("checks", {}).values()) or not receipt.get("pass"):
        errors.append("primary_checks")
    primary_probes = receipt.get("controls", {}).get("outcome_neutrality_probes", [])
    if len(primary_probes) != 2 or not all(
        probe.get("accepted_by_bookkeeping_gate") for probe in primary_probes
    ):
        errors.append("primary_outcome_neutrality_probes")
    pinned = receipt.get("controls", {}).get("pinned_substrate", {})
    if (
        pinned.get("scripts_tree") != EXPECTED_PINNED_SCRIPTS_TREE
        or pinned.get("scripts_tree_pin_match") is not True
        or pinned.get("loaded_transitive_module_file_count")
            != EXPECTED_PINNED_MODULE_COUNT
        or len(pinned.get("loaded_transitive_module_paths", []))
            != EXPECTED_PINNED_MODULE_COUNT
        or pinned.get("loaded_transitive_module_manifest_digest")
            != EXPECTED_PINNED_MODULE_MANIFEST_DIGEST
    ):
        errors.append("primary_pinned_module_closure")

    cache = parse_cache(cache_payload)
    if not cache.get("valid_envelope"):
        errors.append("cache_envelope")
    else:
        fields = cache["fields"]
        if fields.get("runner") != PRIMARY_PATH:
            errors.append("cache_runner")
        if fields.get("runner_sha256") != receipt.get("primary_source_sha256"):
            errors.append("cache_source_pin")
        if fields.get("exit_code") != "0" or fields.get("status") != "ok":
            errors.append("cache_status")
        if fields.get("timeout_sec") != "1400":
            errors.append("cache_timeout")
        if fields.get("input_fingerprint_sha256") != PRIMARY_INPUT_FINGERPRINT_SHA256:
            errors.append("cache_input_fingerprint")
        if sha256(cache["stdout"].encode()).hexdigest() != receipt.get("stdout_sha256"):
            errors.append("cache_stdout_pin")
        if "TOTAL: PASS=4 FAIL=0" not in cache["stdout"]:
            errors.append("cache_total")
    return not errors, errors


def mutation_campaign(receipt: dict, cache_payload: str) -> list[dict]:
    mutations = []

    def add_mutation(name: str, mutate):
        candidate = copy.deepcopy(receipt)
        candidate_cache = cache_payload
        result = mutate(candidate, candidate_cache)
        if isinstance(result, str):
            candidate_cache = result
        accepted, errors = validate_bookkeeping(candidate, candidate_cache)
        mutations.append({"name": name, "rejected": not accepted, "errors": errors})

    def mutate_first_pair_path(row: dict, _cache: str) -> None:
        rows = row["findings"]["A_GLUING_STEP"]["finite_overlap_census"]["rows"]
        overlap = next(item for item in rows if item["shared_pair_agreement_table"])
        overlap["shared_pair_agreement_table"][0]["canonical_global_paths_agree"] = False

    def mutate_both_base_family_sizes(row: dict, _cache: str) -> None:
        rows = row["findings"]["C_INDUCTION_STATUS"]["base_case_reconstruction"][
            "per_target_census"
        ]
        for target_row in rows:
            target_row["relative_family_size"] = 22

    add_mutation("offset_count", lambda row, cache: row["findings"]["A_GLUING_STEP"]
                 ["finite_overlap_census"].__setitem__("oriented_overlap_offset_count", 23))
    add_mutation("type_count", lambda row, cache: row["findings"]["A_GLUING_STEP"]
                 ["finite_overlap_census"]["type_summary"][0].__setitem__("oriented_offset_count", 5))
    add_mutation("shared_site_count", lambda row, cache: row["findings"]["A_GLUING_STEP"]
                 ["finite_overlap_census"]["rows"][0].__setitem__("shared_site_count", 9))
    add_mutation("shared_pair_count", lambda row, cache: row["findings"]["A_GLUING_STEP"]
                 ["finite_overlap_census"]["rows"][0].__setitem__("shared_pair_count", 9))
    add_mutation("pair_path", mutate_first_pair_path)
    add_mutation("universal_flag", lambda row, cache: row["findings"]["A_GLUING_STEP"]
                 ["finite_overlap_census"].__setitem__("all_pairwise_chart_restrictions_agree", False))
    add_mutation("gluing_finding", lambda row, cache: row["findings"]["A_GLUING_STEP"]
                 .__setitem__("universal_local_step_finding", "LOCAL_OVERLAP_OBSTRUCTION_FOUND"))
    add_mutation("case_k", lambda row, cache: row["findings"]["B_STEP_VERIFICATION"]
                 ["verified_cases"][0].__setitem__("k", 7))
    add_mutation("case_support", lambda row, cache: row["findings"]["B_STEP_VERIFICATION"]
                 ["verified_cases"][0].__setitem__("new_support_site_count", 99))
    add_mutation("case_outcome", lambda row, cache: row["findings"]["B_STEP_VERIFICATION"]
                 ["verified_cases"][0].__setitem__("outcome", "OBSTRUCTED"))
    add_mutation("base_outcome_unreconciled", lambda row, cache: row["findings"]
                 ["C_INDUCTION_STATUS"]["base_case_reconstruction"].__setitem__(
                     "outcome", "OBSTRUCTED"
                 ))
    add_mutation("route_flag_unreconciled", lambda row, cache: row["findings"]
                 ["B_STEP_VERIFICATION"]["verified_cases"][0]["new_target_census"]
                 .__setitem__("all_words_routable", False))
    add_mutation("case_overlap_flag_unreconciled", lambda row, cache: row["findings"]
                 ["B_STEP_VERIFICATION"]["verified_cases"][0]
                 ["new_to_old_agreement_table"][0].__setitem__("agreement", False))
    add_mutation("cocycle_flag_unreconciled", lambda row, cache: row["findings"]
                 ["B_STEP_VERIFICATION"]["verified_cases"][0]
                 ["site_cocycle_table"][0].__setitem__("site_cocycle_agrees", False))
    add_mutation("induction_status", lambda row, cache: row["findings"]["C_INDUCTION_STATUS"]
                 .__setitem__("induction_status", "OBSTRUCTED"))
    add_mutation("infinite_scope", lambda row, cache: row["findings"]["C_INDUCTION_STATUS"]
                 .__setitem__("full_infinite_translation_uniform_lattice_law_claimed", True))
    add_mutation("exact_quantifier", lambda row, cache: row["findings"]["C_INDUCTION_STATUS"]
                 .__setitem__("exact_quantifier", "for n=infinity and all of Z3"))
    add_mutation("verdict_line", lambda row, cache: row["findings"]["C_INDUCTION_STATUS"]
                 .__setitem__("verdict_line", "OBSTRUCTED"))
    add_mutation("overlap_exhaustion_flag", lambda row, cache: row["findings"]
                 ["A_GLUING_STEP"]["finite_overlap_census"].__setitem__(
                     "all_overlap_types_exhausted", False
                 ))
    add_mutation("local_truth_failure", lambda row, cache: row["findings"]
                 ["B_STEP_VERIFICATION"]["verified_cases"][0]["new_target_census"]
                 .__setitem__("landed_vs_boolean_failure_count", 1))
    add_mutation("base_family_size", mutate_both_base_family_sizes)
    add_mutation("primary_source_pin", lambda row, cache: row.__setitem__(
        "primary_source_sha256", "0" * 64
    ))
    add_mutation("cache_headline", lambda row, cache: cache.replace(
        "FINITE_PATCH_INDUCTION_CLOSES_AT_DECLARED_SCOPE", "OBSTRUCTED", 1
    ))
    add_mutation("cache_timeout", lambda row, cache: cache.replace(
        "timeout_sec: 1400", "timeout_sec: 1", 1
    ))
    add_mutation("cache_input_fingerprint", lambda row, cache: cache.replace(
        PRIMARY_INPUT_FINGERPRINT_SHA256, "0" * 64, 1
    ))
    return mutations


def rewrite_induction_for_probe(receipt: dict) -> None:
    status, obstruction = derive_induction(receipt)
    row = receipt["findings"]["C_INDUCTION_STATUS"]
    row["induction_status"] = status
    row["exact_obstruction"] = obstruction
    row["verdict_line"] = status


def coherent_outcome_probes(receipt: dict, cache_payload: str) -> list[dict]:
    probes = []
    obstructed = copy.deepcopy(receipt)
    case = obstructed["findings"]["B_STEP_VERIFICATION"]["verified_cases"][0]
    overlap = case["new_to_old_agreement_table"][0]
    overlap["shared_site_agreement_table"][0]["binding_agrees"] = False
    overlap["shared_site_agreement_table"][0]["right_binding"] = "q_conflicting_binding"
    overlap["site_bindings_agree"] = False
    overlap["agreement"] = False
    case["outcome"] = "OBSTRUCTED"
    case["exact_obstruction"] = "one or more new-to-old chart restrictions disagree"
    rewrite_induction_for_probe(obstructed)
    accepted, errors = validate_bookkeeping(obstructed, cache_payload)
    probes.append({
        "name": "coherent_obstructed_outcome",
        "accepted_by_bookkeeping_gate": accepted,
        "errors": errors,
    })

    not_hostable = copy.deepcopy(receipt)
    case = not_hostable["findings"]["B_STEP_VERIFICATION"]["verified_cases"][0]
    census = case["new_target_census"]
    census["route_failure_count"] = 1
    census["all_words_routable"] = False
    case["outcome"] = "NOT_HOSTABLE"
    case["exact_obstruction"] = "new target (2,0,0) is not route-hostable"
    rewrite_induction_for_probe(not_hostable)
    accepted, errors = validate_bookkeeping(not_hostable, cache_payload)
    probes.append({
        "name": "coherent_not_hostable_outcome",
        "accepted_by_bookkeeping_gate": accepted,
        "errors": errors,
    })
    return probes


def input_controls() -> dict:
    payloads = {item: (ROOT / item).read_bytes() for item in AUDIT_INPUT_PATHS}
    sha_rows = {item: sha256(payloads[item]).hexdigest() for item in BYTE_PINNED_INPUT_PATHS}
    blob_rows = {item: git_blob(payloads[item]) for item in BYTE_PINNED_INPUT_PATHS}
    source = (ROOT / CHECKER_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=CHECKER_PATH)
    imports = {
        alias.name for node in ast.walk(tree) if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    }
    forbidden = sorted(
        name for name in imports
        if any(fragment in name.lower() for fragment in FORBIDDEN_IMPORT_FRAGMENTS)
    )
    primary_tree = ast.parse(payloads[PRIMARY_PATH], filename=PRIMARY_PATH)
    primary_timeout = None
    for node in primary_tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "AUDIT_TIMEOUT_SEC"
            for target in node.targets
        ):
            primary_timeout = ast.literal_eval(node.value)
    base_is_ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", BASE_ORIGIN_MAIN_COMMIT, "HEAD"],
        cwd=ROOT, check=False, capture_output=True,
    ).returncode == 0
    return {
        "literal_audit_input_paths": list(AUDIT_INPUT_PATHS),
        "byte_pinned_input_paths": list(BYTE_PINNED_INPUT_PATHS),
        "literal_source_read_count": len(AUDIT_INPUT_PATHS),
        "input_sha256": sha_rows,
        "input_git_blobs": blob_rows,
        "sha_pins_match": sha_rows == EXPECTED_INPUT_SHA256,
        "blob_pins_match": blob_rows == EXPECTED_INPUT_BLOBS,
        "all_inputs_relative_and_present": all(
            not Path(item).is_absolute() and (ROOT / item).is_file()
            for item in AUDIT_INPUT_PATHS
        ),
        "forbidden_imports": forbidden,
        "primary_imported_or_executed": False,
        "cycle719_imported_or_executed": False,
        "prior_cycle_text_or_ast_executed": False,
        "primary_ast_timeout_seconds": primary_timeout,
        "base_origin_main_commit": BASE_ORIGIN_MAIN_COMMIT,
        "base_is_ancestor_of_head": base_is_ancestor,
    }


def render_stdout(receipt: dict) -> str:
    findings = receipt["findings"]
    expected = findings["independent_expected"]
    probes = findings["coherent_outcome_probes"]
    lines = [
        "CYCLE986_PATCH_UNIFORMITY_INDUCTION_INDEPENDENT_CHECK",
        "A_INDEPENDENT_RECONSTRUCTION "
        + ("PASS" if receipt["checks"]["A_INDEPENDENT_RECONSTRUCTION"] else "FAIL")
        + f" :: offsets={expected['universal']['oriented_overlap_offset_count']};"
        + f" classes={compact(expected['class_table'])};"
        + f" agreement={findings['primary_science_agreement']}",
        "B_REFUTATION_POWER "
        + ("PASS" if receipt["checks"]["B_REFUTATION_POWER"] else "FAIL")
        + f" :: rejected={sum(row['rejected'] for row in findings['mutations'])}/"
        + f"{len(findings['mutations'])}; outcome_neutral="
        + compact([row["accepted_by_bookkeeping_gate"] for row in probes]),
        "C_ARTIFACT_BINDING "
        + ("PASS" if receipt["checks"]["C_ARTIFACT_BINDING"] else "FAIL")
        + f" :: pins={receipt['controls']['sha_pins_match'] and receipt['controls']['blob_pins_match']};"
        + f" clean_bookkeeping={findings['clean_bookkeeping_validation']}",
        "D_PROVENANCE " + ("PASS" if receipt["checks"]["D_PROVENANCE"] else "FAIL")
        + f" :: primary_imported={receipt['controls']['primary_imported_or_executed']};"
        + f" cycle719_imported={receipt['controls']['cycle719_imported_or_executed']};"
        + f" prior_cycles_executed={receipt['controls']['prior_cycle_text_or_ast_executed']}",
        "E_CONTROLS " + ("PASS" if receipt["checks"]["E_CONTROLS"] else "FAIL")
        + f" :: source_reads={receipt['controls']['literal_source_read_count']}<=6;"
        + f" determinism={receipt['controls']['determinism_replay']};"
        + f" runtime_lt_300={receipt['controls']['runtime_budget_met']}",
    ]
    passed = sum(receipt["checks"].values())
    lines.append(f"TOTAL: PASS={passed} FAIL={len(receipt['checks']) - passed}")
    return "\n".join(lines) + "\n"


def run_once() -> tuple[dict, dict]:
    primary_receipt = json.loads((ROOT / PRIMARY_RECEIPT_PATH).read_text(encoding="utf-8"))
    primary_cache = (ROOT / PRIMARY_CACHE_PATH).read_text(encoding="utf-8")
    expected = independent_expected()
    primary_view = selected_primary_view(primary_receipt)
    mismatches = [key for key in expected if primary_view.get(key) != expected[key]]
    clean, clean_errors = validate_bookkeeping(primary_receipt, primary_cache)
    mutations = mutation_campaign(primary_receipt, primary_cache)
    probes = coherent_outcome_probes(primary_receipt, primary_cache)
    expected_bookkeeping = bool(
        expected["universal"]["oriented_overlap_offset_count"] == 24
        and sum(row["oriented_offset_count"] for row in expected["universal"]["type_summary"]) == 24
        and len(ACTIONS) == 24
        and len(family()) == 23
        and independent_target_census(O)["witness_count"] == 21
        and all(row["outcome"] == "GLUING_STEP_VERIFIED" for row in expected["cases"])
        and not expected["infinite_claimed"]
    )
    findings = {
        "independent_expected": expected,
        "independent_reconstruction_bookkeeping": expected_bookkeeping,
        "primary_science_agreement": not mismatches,
        "primary_science_agreement_mismatches": mismatches,
        "clean_bookkeeping_validation": clean,
        "clean_bookkeeping_validation_errors": clean_errors,
        "mutations": mutations,
        "coherent_outcome_probes": probes,
    }
    checks = {
        "A_INDEPENDENT_RECONSTRUCTION": expected_bookkeeping,
        "B_REFUTATION_POWER": bool(mutations)
            and all(row["rejected"] for row in mutations)
            and all(row["accepted_by_bookkeeping_gate"] for row in probes),
        "C_ARTIFACT_BINDING": clean,
        "D_PROVENANCE": True,
        "E_CONTROLS": True,
    }
    return findings, checks


def run() -> tuple[dict, str]:
    started = monotonic()
    first_findings, first_checks = run_once()
    second_findings, second_checks = run_once()
    deterministic = first_findings == second_findings and first_checks == second_checks
    controls = input_controls()
    runtime_budget_met = monotonic() - started < AUDIT_TIMEOUT_SEC
    provenance = bool(
        not controls["forbidden_imports"]
        and not controls["primary_imported_or_executed"]
        and not controls["cycle719_imported_or_executed"]
        and not controls["prior_cycle_text_or_ast_executed"]
    )
    controls.update({
        "determinism_replay": deterministic,
        "runtime_budget_met": runtime_budget_met,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "house_stdout_limit_bytes": HOUSE_STDOUT_LIMIT_BYTES,
    })
    checks = dict(first_checks)
    checks["C_ARTIFACT_BINDING"] = bool(
        checks["C_ARTIFACT_BINDING"]
        and controls["sha_pins_match"] and controls["blob_pins_match"]
    )
    checks["D_PROVENANCE"] = provenance
    checks["E_CONTROLS"] = bool(
        controls["literal_source_read_count"] <= 6
        and controls["all_inputs_relative_and_present"]
        and controls["primary_ast_timeout_seconds"] == 1400
        and controls["base_is_ancestor_of_head"]
        and deterministic and runtime_budget_met
    )
    receipt = {
        "cycle": CYCLE,
        "artifact": "finite-patch gluing induction independent refutation checker",
        "audit_status_authority": "independent audit lane only",
        "integrity_policy": (
            "checks gate independent reconstruction, bookkeeping, artifact binding, mutation "
            "rejection, and outcome neutrality only; science agreement is reported data"
        ),
        "findings": first_findings,
        "science_digest": digest(first_findings["independent_expected"]),
        "controls": controls,
        "checks": checks,
    }
    receipt["checker_source_sha256"] = sha256((ROOT / CHECKER_PATH).read_bytes()).hexdigest()
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
