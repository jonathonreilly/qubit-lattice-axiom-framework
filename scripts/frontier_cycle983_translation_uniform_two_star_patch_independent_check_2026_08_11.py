#!/usr/bin/env python3
"""Independent refutation checker for the Cycle-983 two-star patch packet.

The checker imports and executes neither the primary nor Cycle-719.  It binds
the primary source, receipt, and canonical cache; reconstructs the geometry,
two 23-program laws, witnesses, cubic classes, separator, routing arithmetic,
and overlap table independently; rejects declared corruptions; and proves that
coherent obstructed and not-hostable receipts remain bookkeeping-clean.
"""

from __future__ import annotations

import ast
import copy
import json
import sys
from hashlib import sha1, sha256
from itertools import combinations, permutations, product
from pathlib import Path
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
CYCLE = 983
AUDIT_TIMEOUT_SEC = 300
HOUSE_STDOUT_LIMIT_BYTES = 6_000
STDOUT_LIMIT_BYTES = 150_000
BASE_ORIGIN_MAIN_COMMIT = "ea0968c71ad46c39c6dacb39f88a18780363b71f"

PRIMARY_PATH = (
    "scripts/frontier_cycle983_translation_uniform_two_star_patch_2026_08_11.py"
)
PRIMARY_RECEIPT_PATH = (
    "outputs/translation_uniform_two_star_patch_cycle983_receipt_2026_08_11.json"
)
PRIMARY_CACHE_PATH = (
    "logs/runner-cache/frontier_cycle983_translation_uniform_two_star_patch_2026_08_11.txt"
)
CHECKER_PATH = (
    "scripts/frontier_cycle983_translation_uniform_two_star_patch_independent_check_2026_08_11.py"
)
RECEIPT_PATH = (
    "outputs/translation_uniform_two_star_patch_cycle983_independent_check_receipt_2026_08_11.json"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle983_translation_uniform_two_star_patch_2026_08_11.py",
    "outputs/translation_uniform_two_star_patch_cycle983_receipt_2026_08_11.json",
    "logs/runner-cache/frontier_cycle983_translation_uniform_two_star_patch_2026_08_11.txt",
)
BYTE_PINNED_INPUT_PATHS = (
    "scripts/frontier_cycle983_translation_uniform_two_star_patch_2026_08_11.py",
    "outputs/translation_uniform_two_star_patch_cycle983_receipt_2026_08_11.json",
)
EXPECTED_INPUT_SHA256 = {
    PRIMARY_PATH: "c4ff78125b1d82954acbcd7fd5e409abe61815bb64c75c1b2ca6a7aa24d6b51d",
    PRIMARY_RECEIPT_PATH: "cbd2f7857cdd03f580aef30126294e32c8d4f57e4fb0282f6ef73936f2d75754",
}
EXPECTED_INPUT_BLOBS = {
    PRIMARY_PATH: "c96f54135c6e0a94d4614aab556e2fb8841570f1",
    PRIMARY_RECEIPT_PATH: "459971c0e8b7d67ccac41f789a373c0ddeb9c4e0",
}
FORBIDDEN_IMPORT_FRAGMENTS = (
    "frontier_cycle719_two_rail_recurrent_controller_core",
    "frontier_cycle983_translation_uniform_two_star_patch_2026_08_11",
    "cycle970", "cycle972", "cycle977", "cycle979", "cycle980", "cycle982",
)

ZERO = (0, 0, 0)
EX = (1, 0, 0)
CENTRES = (ZERO, EX)
CENTRE_NAMES = ("A", "B")
STEPS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
STEP_NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
RELATIVE_SITES = (ZERO, *STEPS)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def plus(left: tuple, right: tuple) -> tuple:
    return tuple(a + b for a, b in zip(left, right))


def taxicab(left: tuple, right: tuple) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def scalar(left: tuple, right: tuple) -> int:
    return sum(a * b for a, b in zip(left, right))


def star(center: tuple) -> tuple:
    return (center, *(plus(center, step) for step in STEPS))


STARS = tuple(star(center) for center in CENTRES)
SUPPORT = tuple(sorted(set(STARS[0]) | set(STARS[1])))


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


def boolean_output(descriptor: tuple, target: int, neighbours: tuple) -> int:
    if descriptor[0] == "I":
        return target
    if descriptor[0] == "X":
        return target ^ 1
    if descriptor[0] == "CNOT":
        return target ^ neighbours[descriptor[1] - 1]
    return target ^ (
        neighbours[descriptor[1] - 1] & neighbours[descriptor[2] - 1]
    )


def dependence_witness(descriptor: tuple) -> bool:
    for target in (0, 1):
        for neighbours in product((0, 1), repeat=6):
            for index in range(6):
                flipped = list(neighbours)
                flipped[index] ^= 1
                if boolean_output(descriptor, target, neighbours) != boolean_output(
                    descriptor, target, tuple(flipped)
                ):
                    return True
    return False


def determinant(matrix: tuple) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def rotation_actions() -> tuple:
    site_to_wire = {site: wire for wire, site in enumerate(RELATIVE_SITES)}
    actions = set()
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[row] * int(column == order[row]) for column in range(3))
                for row in range(3)
            )
            if determinant(matrix) != 1:
                continue
            rotated = tuple(
                tuple(scalar(row, site) for row in matrix) for site in RELATIVE_SITES
            )
            actions.add(tuple(site_to_wire[site] for site in rotated))
    return tuple(sorted(actions))


ACTIONS = rotation_actions()


def transform_descriptor(descriptor: tuple, action: tuple) -> tuple:
    if descriptor[0] in ("I", "X"):
        return descriptor
    wires = tuple(action[wire] for wire in descriptor[1:])
    if descriptor[0] == "TOF":
        return ("TOF", *sorted(wires[:2]), wires[2])
    return (descriptor[0], *wires)


def separator_j(descriptor: tuple) -> int:
    controls = (descriptor[1],) if descriptor[0] == "CNOT" else descriptor[1:3]
    total = tuple(
        sum(RELATIVE_SITES[wire][axis] for wire in controls) for axis in range(3)
    )
    return scalar(total, total)


def witness_class(descriptor: tuple) -> str:
    if descriptor[0] == "CNOT":
        return "CNOT"
    if separator_j(descriptor) == 0:
        return "TOF_OPPOSITE_CONTROLS"
    return "TOF_PERPENDICULAR_CONTROLS"


def independent_orbits(witnesses: tuple) -> list[dict]:
    all_witnesses = set(witnesses)
    remaining = set(witnesses)
    rows = []
    while remaining:
        seed = min(remaining, key=descriptor_name)
        ambient = {transform_descriptor(seed, action) for action in ACTIONS}
        members = ambient & all_witnesses
        rows.append({
            "class_label": witness_class(seed),
            "member_count": len(members),
            "effective_stabilizer_order": sum(
                transform_descriptor(seed, action) == seed for action in ACTIONS
            ),
            "J_values": sorted({separator_j(member) for member in members}),
            "members": sorted(descriptor_name(member) for member in members),
        })
        remaining -= members
    return sorted(rows, key=lambda row: row["class_label"])


def minimum_two_star_union() -> tuple[int, str]:
    rows = []
    base = set(star(ZERO))
    for offset in product(range(-2, 3), repeat=3):
        if offset == ZERO:
            continue
        overlap = len(base & set(star(offset)))
        if overlap:
            rows.append({
                "offset": list(offset),
                "L1": taxicab(ZERO, offset),
                "intersection_size": overlap,
                "union_size": 14 - overlap,
            })
    return min(row["union_size"] for row in rows), digest(rows)


def expected_route_counts() -> dict:
    # Per target: X gives 1 primitive/gate; six CNOTs give 6/6.
    # Each of 15 TOFs expands to 15 primitives.  Four control pairs are at
    # distance 1 and two at distance 2, so routed count is
    # 9 + 4*(2*1-1) + 2*(2*2-1) = 19 for every TOF.
    return {
        "all_words_routable": True,
        "maximum_route_distance": 2,
        "maximum_touched_sites": 3,
        "expanded_primitive_count": 1 + 6 + 15 * 15,
        "routed_nn_gate_count": 1 + 6 + 15 * 19,
        "non_nn_failure_count": 0,
        "operand_order_failure_count": 0,
        "route_return_failure_count": 0,
    }


def independent_expected() -> dict:
    descriptors = family()
    witnesses = tuple(row for row in descriptors if dependence_witness(row))
    orbits = independent_orbits(witnesses)
    witness_names = [descriptor_name(row) for row in witnesses]
    normalized_structure = {
        "relative_witnesses": witness_names,
        "class_assignments": [
            [descriptor_name(row), witness_class(row), separator_j(row)]
            for row in witnesses
        ],
        "orbits": [
            [
                row["class_label"], row["member_count"],
                row["effective_stabilizer_order"], row["J_values"],
            ]
            for row in orbits
        ],
    }
    minimum_union, offset_digest = minimum_two_star_union()
    shared = tuple(sorted(set(STARS[0]) & set(STARS[1])))
    target_rows = []
    route = expected_route_counts()
    for index, center in enumerate(CENTRES):
        target_rows.append({
            "target_name": CENTRE_NAMES[index],
            "target_site": list(center),
            "complete_six_neighbour_star_present": set(STARS[index]) <= set(SUPPORT),
            "relative_family_size": len(descriptors),
            "truth_table_evaluations": len(descriptors) * 2 * (2 ** 6),
            "landed_vs_independent_truth_failure_count": 0,
            "witness_count": len(witnesses),
            "witness_names": sorted(witness_names),
            "class_assignments": sorted(
                [descriptor_name(row), witness_class(row), separator_j(row)]
                for row in witnesses
            ),
            "orbits": [
                {
                    "class_label": row["class_label"],
                    "member_count": row["member_count"],
                    "effective_stabilizer_order": row["effective_stabilizer_order"],
                    "J_values": row["J_values"],
                    "members": row["members"],
                }
                for row in orbits
            ],
            "normalized_structure_digest": digest(normalized_structure),
            "route": route,
        })
    return {
        "construction": {
            "patch_name": "P2x_ADJACENT_TWO_CENTRE_CLOSED_STAR_PATCH",
            "target_sites": [list(site) for site in CENTRES],
            "target_site_count": len(CENTRES),
            "host_support_sites": [list(site) for site in SUPPORT],
            "host_support_site_count": len(SUPPORT),
            "center_separation_L1": taxicab(*CENTRES),
            "closed_star_intersection": [list(site) for site in shared],
            "closed_star_intersection_size": len(shared),
            "closed_star_union_size": len(SUPPORT),
            "relative_family_size_per_target": len(descriptors),
            "site_program_instance_count": len(descriptors) * len(CENTRES),
            "relative_family_digest": digest(descriptors),
            "minimum_union_size": minimum_union,
            "offset_census_digest": offset_digest,
        },
        "uniformity": {
            "target_rows": target_rows,
            "classification": "translation_uniform_on_every_target_site_of_P2x",
            "all_patch_target_sites_tested": True,
        },
        "overlap": {
            "shared_site_rows": [
                {
                    "global_site": [0, 0, 0],
                    "star_A_local_wire": 0,
                    "star_A_local_name": "C",
                    "star_B_local_wire": 2,
                    "star_B_local_name": "-x",
                    "same_global_site_binding": True,
                },
                {
                    "global_site": [1, 0, 0],
                    "star_A_local_wire": 1,
                    "star_A_local_name": "+x",
                    "star_B_local_wire": 0,
                    "star_B_local_name": "C",
                    "same_global_site_binding": True,
                },
            ],
            "shared_pair_rows": [{
                "global_pair": [[0, 0, 0], [1, 0, 0]],
                "star_A_local_wires_for_sorted_global_pair": [0, 1],
                "star_B_local_wires_for_sorted_global_pair": [2, 0],
                "semantic_pair_in_both_stars": True,
                "z3_nearest_neighbour_in_star_A": True,
                "z3_nearest_neighbour_in_star_B": True,
                "target_equations_are_distinct_instances_not_equal_outputs": True,
                "star_A_class": "CNOT",
                "star_B_class": "CNOT",
                "star_A_J": 1,
                "star_B_J": 1,
                "paths_agree_up_to_reversal": True,
            }],
            "classification": "exact_agreement_on_all_shared_sites_and_pairs",
        },
        "verdict": {
            "verdict": "TRANSLATION_UNIFORM_AT_PATCH_SCOPE",
            "named_patch": "P2x_ADJACENT_TWO_CENTRE_CLOSED_STAR_PATCH",
            "exact_obstruction": None,
            "target_patch_site_count": 2,
            "host_support_site_count": 12,
            "full_infinite_translation_uniform_lattice_law_claimed": False,
        },
        "group_order": len(ACTIONS),
    }


def selected_primary_view(receipt: dict) -> dict:
    findings = receipt["findings"]
    construction = findings["A_PATCH_CONSTRUCTION"]
    uniformity = findings["B_UNIFORMITY_TEST"]
    overlap = findings["C_OVERLAP_CONSISTENCY"]
    verdict = findings["D_VERDICT"]
    target_rows = []
    for row in uniformity["per_site_census"]:
        target_rows.append({
            "target_name": row["target_name"],
            "target_site": row["target_site"],
            "complete_six_neighbour_star_present": row["complete_six_neighbour_star_present"],
            "relative_family_size": row["relative_family_size"],
            "truth_table_evaluations": row["truth_table_evaluations"],
            "landed_vs_independent_truth_failure_count": row[
                "landed_vs_independent_truth_failure_count"
            ],
            "witness_count": row["witness_count"],
            "witness_names": sorted(row["witness_names"]),
            "class_assignments": sorted(
                [item["relative_word"], item["class_label"], item["J"]]
                for item in row["witness_assignments"]
            ),
            "orbits": [
                {
                    "class_label": orbit["class_label"],
                    "member_count": orbit["member_count"],
                    "effective_stabilizer_order": orbit["effective_stabilizer_order"],
                    "J_values": orbit["J_values"],
                    "members": sorted(orbit["members"]),
                }
                for orbit in row["orbit_decomposition"]["orbits"]
            ],
            "normalized_structure_digest": row["normalized_structure_digest"],
            "route": {
                key: row["route_host"][key] for key in (
                    "all_words_routable", "maximum_route_distance",
                    "maximum_touched_sites", "expanded_primitive_count",
                    "routed_nn_gate_count", "non_nn_failure_count",
                    "operand_order_failure_count", "route_return_failure_count",
                )
            },
        })
    shared_site_rows = [
        {
            key: row[key] for key in (
                "global_site", "star_A_local_wire", "star_A_local_name",
                "star_B_local_wire", "star_B_local_name", "same_global_site_binding",
            )
        }
        for row in overlap["shared_site_agreement_table"]
    ]
    shared_pair_rows = [
        {
            key: row[key] for key in (
                "global_pair", "star_A_local_wires_for_sorted_global_pair",
                "star_B_local_wires_for_sorted_global_pair",
                "semantic_pair_in_both_stars", "z3_nearest_neighbour_in_star_A",
                "z3_nearest_neighbour_in_star_B",
                "target_equations_are_distinct_instances_not_equal_outputs",
                "star_A_class", "star_B_class", "star_A_J", "star_B_J",
                "paths_agree_up_to_reversal",
            )
        }
        for row in overlap["shared_pair_agreement_table"]
    ]
    return {
        "construction": {
            "patch_name": construction["patch_name"],
            "target_sites": construction["target_sites"],
            "target_site_count": construction["target_site_count"],
            "host_support_sites": construction["host_support_sites"],
            "host_support_site_count": construction["host_support_site_count"],
            "center_separation_L1": construction["center_separation_L1"],
            "closed_star_intersection": construction["closed_star_intersection"],
            "closed_star_intersection_size": construction["closed_star_intersection_size"],
            "closed_star_union_size": construction["closed_star_union_size"],
            "relative_family_size_per_target": construction["family"][
                "relative_family_size_per_target"
            ],
            "site_program_instance_count": construction["family"][
                "site_program_instance_count"
            ],
            "relative_family_digest": construction["family"]["relative_family_digest"],
            "minimum_union_size": construction["minimality"][
                "minimum_union_size_for_two_distinct_overlapping_closed_unit_stars"
            ],
            "offset_census_digest": construction["minimality"]["offset_census_digest"],
        },
        "uniformity": {
            "target_rows": target_rows,
            "classification": uniformity["classification"],
            "all_patch_target_sites_tested": uniformity["all_patch_target_sites_tested"],
        },
        "overlap": {
            "shared_site_rows": shared_site_rows,
            "shared_pair_rows": shared_pair_rows,
            "classification": overlap["classification"],
        },
        "verdict": {
            key: verdict[key] for key in (
                "verdict", "named_patch", "exact_obstruction",
                "target_patch_site_count", "host_support_site_count",
                "full_infinite_translation_uniform_lattice_law_claimed",
            )
        },
        "group_order": uniformity["per_site_census"][0]["orbit_decomposition"][
            "effective_group_order"
        ],
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


def classify_uniformity_from_receipt(rows: list[dict]) -> str:
    if not all(row["route_host"]["all_words_routable"] for row in rows):
        return "not_hostable_at_one_or_more_target_sites"
    keys = (
        "relative_family_size", "witness_count", "witness_names",
        "normalized_structure_digest",
    )
    if any(
        any(row[key] != rows[0][key] for key in keys) for row in rows[1:]
    ):
        return "class_structure_differs_across_target_sites"
    if any(row["landed_vs_independent_truth_failure_count"] for row in rows):
        return "landed_truth_law_differs_from_declared_rule"
    return "translation_uniform_on_every_target_site_of_P2x"


def derive_verdict_from_receipt(uniformity: dict, overlap: dict) -> tuple[str, str | None]:
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


def validate_bookkeeping(receipt: dict, cache_payload: str) -> tuple[bool, list[str]]:
    errors = []
    findings = receipt.get("findings", {})
    try:
        construction = findings["A_PATCH_CONSTRUCTION"]
        uniformity = findings["B_UNIFORMITY_TEST"]
        overlap = findings["C_OVERLAP_CONSISTENCY"]
        verdict = findings["D_VERDICT"]
    except KeyError as exc:
        return False, [f"missing_finding:{exc}"]
    if construction["target_site_count"] != len(construction["target_sites"]):
        errors.append("target_site_count")
    if construction["host_support_site_count"] != len(construction["host_support_sites"]):
        errors.append("support_site_count")
    if construction["closed_star_union_size"] != construction["host_support_site_count"]:
        errors.append("star_union_count")
    if construction["closed_star_intersection_size"] != len(
        construction["closed_star_intersection"]
    ):
        errors.append("star_intersection_count")
    family_row = construction["family"]
    if family_row["site_program_instance_count"] != (
        family_row["relative_family_size_per_target"] * construction["target_site_count"]
    ):
        errors.append("site_program_instances")
    if not construction["minimality"]["chosen_patch_attains_minimum"]:
        errors.append("minimality_flag")

    rows = uniformity["per_site_census"]
    if uniformity["tested_target_site_count"] != len(rows):
        errors.append("tested_target_site_count")
    if uniformity["all_patch_target_sites_tested"] != (
        len(rows) == construction["target_site_count"]
    ):
        errors.append("all_patch_sites_flag")
    for index, row in enumerate(rows):
        if row["witness_count"] != len(row["witness_names"]):
            errors.append(f"witness_names:{index}")
        if row["witness_count"] != len(row["witness_assignments"]):
            errors.append(f"witness_assignments:{index}")
        orbits = row["orbit_decomposition"]
        if sum(orbit["member_count"] for orbit in orbits["orbits"]) != row["witness_count"]:
            errors.append(f"orbit_sum:{index}")
        if any(
            orbit["orbit_stabilizer_product"] != orbits["effective_group_order"]
            for orbit in orbits["orbits"]
        ):
            errors.append(f"orbit_stabilizer:{index}")
        route = row["route_host"]
        route_failures = sum(route[key] for key in (
            "non_nn_failure_count", "operand_order_failure_count",
            "route_return_failure_count",
        ))
        if route["all_words_routable"] != (route_failures == 0):
            errors.append(f"route_host_flag:{index}")
        expected_route_class = (
            "complete_target_star_hosted" if route_failures == 0
            else "complete_target_star_not_hosted"
        )
        if route["classification"] != expected_route_class:
            errors.append(f"route_host_class:{index}")
    computed_uniformity = classify_uniformity_from_receipt(rows)
    if uniformity["classification"] != computed_uniformity:
        errors.append("uniformity_classification")
    for field, agreement in uniformity["per_site_exact_agreement"].items():
        actual = all(row[field] == rows[0][field] for row in rows)
        if agreement != actual:
            errors.append(f"per_site_agreement:{field}")

    site_rows = overlap["shared_site_agreement_table"]
    pair_rows = overlap["shared_pair_agreement_table"]
    if overlap["shared_site_count"] != len(site_rows):
        errors.append("shared_site_count")
    if overlap["shared_semantic_pair_count"] != len(pair_rows):
        errors.append("shared_pair_count")
    site_agreement = all(row["same_global_site_binding"] for row in site_rows)
    pair_agreement = all(
        row["semantic_pair_in_both_stars"]
        and row["z3_nearest_neighbour_in_star_A"]
            == row["z3_nearest_neighbour_in_star_B"]
        and row["star_A_class"] == row["star_B_class"]
        and row["star_A_J"] == row["star_B_J"]
        and row["paths_agree_up_to_reversal"]
        for row in pair_rows
    )
    if overlap["shared_site_global_bindings_agree"] != site_agreement:
        errors.append("shared_site_agreement")
    if overlap["shared_pair_relations_classes_J_and_paths_agree"] != pair_agreement:
        errors.append("shared_pair_agreement")
    expected_overlap = (
        "exact_agreement_on_all_shared_sites_and_pairs"
        if site_agreement and pair_agreement
        else "overlap_disagreement_obstructs_translation_uniformity"
    )
    if overlap["classification"] != expected_overlap:
        errors.append("overlap_classification")

    expected_verdict, expected_obstruction = derive_verdict_from_receipt(
        uniformity, overlap
    )
    if verdict["verdict"] != expected_verdict:
        errors.append("verdict")
    if verdict["exact_obstruction"] != expected_obstruction:
        errors.append("verdict_obstruction")
    if verdict["full_infinite_translation_uniform_lattice_law_claimed"] is not False:
        errors.append("infinite_scope")
    if not verdict["scope_exclusions"]:
        errors.append("scope_exclusions")
    if not all(receipt.get("checks", {}).values()) or not receipt.get("pass"):
        errors.append("primary_checks")

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
        if sha256(cache["stdout"].encode()).hexdigest() != receipt.get("stdout_sha256"):
            errors.append("cache_stdout_pin")
        if "TOTAL: PASS=5 FAIL=0" not in cache["stdout"]:
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

    add_mutation(
        "target_site_count",
        lambda row, cache: row["findings"]["A_PATCH_CONSTRUCTION"].__setitem__(
            "target_site_count", 3
        ),
    )
    add_mutation(
        "support_site_count",
        lambda row, cache: row["findings"]["A_PATCH_CONSTRUCTION"].__setitem__(
            "host_support_site_count", 11
        ),
    )
    add_mutation(
        "site_program_instances",
        lambda row, cache: row["findings"]["A_PATCH_CONSTRUCTION"]["family"].__setitem__(
            "site_program_instance_count", 45
        ),
    )
    add_mutation(
        "second_site_witness_count",
        lambda row, cache: row["findings"]["B_UNIFORMITY_TEST"]["per_site_census"][1].__setitem__(
            "witness_count", 20
        ),
    )
    add_mutation(
        "orbit_size",
        lambda row, cache: row["findings"]["B_UNIFORMITY_TEST"]["per_site_census"][0]
            ["orbit_decomposition"]["orbits"][0].__setitem__("member_count", 5),
    )
    add_mutation(
        "hostability",
        lambda row, cache: row["findings"]["B_UNIFORMITY_TEST"]["per_site_census"][1]
            ["route_host"].__setitem__("all_words_routable", False),
    )
    add_mutation(
        "uniformity_classification",
        lambda row, cache: row["findings"]["B_UNIFORMITY_TEST"].__setitem__(
            "classification", "class_structure_differs_across_target_sites"
        ),
    )
    add_mutation(
        "shared_site_count",
        lambda row, cache: row["findings"]["C_OVERLAP_CONSISTENCY"].__setitem__(
            "shared_site_count", 1
        ),
    )
    add_mutation(
        "overlap_path_agreement",
        lambda row, cache: row["findings"]["C_OVERLAP_CONSISTENCY"]
            ["shared_pair_agreement_table"][0].__setitem__("paths_agree_up_to_reversal", False),
    )
    add_mutation(
        "verdict",
        lambda row, cache: row["findings"]["D_VERDICT"].__setitem__("verdict", "OBSTRUCTED"),
    )
    add_mutation(
        "infinite_scope",
        lambda row, cache: row["findings"]["D_VERDICT"].__setitem__(
            "full_infinite_translation_uniform_lattice_law_claimed", True
        ),
    )
    add_mutation(
        "primary_source_pin",
        lambda row, cache: row.__setitem__("primary_source_sha256", "0" * 64),
    )
    add_mutation(
        "cache_headline",
        lambda row, cache: cache.replace("support=12", "support=11", 1),
    )
    return mutations


def coherent_outcome_probes(receipt: dict, cache_payload: str) -> list[dict]:
    probes = []

    obstructed = copy.deepcopy(receipt)
    uniformity = obstructed["findings"]["B_UNIFORMITY_TEST"]
    uniformity["per_site_census"][1]["normalized_structure_digest"] = "coherent-obstruction"
    uniformity["per_site_exact_agreement"]["normalized_structure_digest"] = False
    uniformity["classification"] = "class_structure_differs_across_target_sites"
    verdict = obstructed["findings"]["D_VERDICT"]
    verdict["verdict"] = "OBSTRUCTED"
    verdict["exact_obstruction"] = "class_structure_differs_across_target_sites"
    accepted, errors = validate_bookkeeping(obstructed, cache_payload)
    probes.append({
        "name": "coherent_obstructed_outcome",
        "accepted_by_bookkeeping_gate": accepted,
        "errors": errors,
    })

    not_hostable = copy.deepcopy(receipt)
    uniformity = not_hostable["findings"]["B_UNIFORMITY_TEST"]
    route = uniformity["per_site_census"][1]["route_host"]
    route["route_return_failure_count"] = 1
    route["all_words_routable"] = False
    route["classification"] = "complete_target_star_not_hosted"
    uniformity["classification"] = "not_hostable_at_one_or_more_target_sites"
    verdict = not_hostable["findings"]["D_VERDICT"]
    verdict["verdict"] = "NOT_HOSTABLE"
    verdict["exact_obstruction"] = "unhosted target stars: B"
    accepted, errors = validate_bookkeeping(not_hostable, cache_payload)
    probes.append({
        "name": "coherent_not_hostable_outcome",
        "accepted_by_bookkeeping_gate": accepted,
        "errors": errors,
    })
    return probes


def input_controls() -> dict:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    sha_rows = {
        path: sha256(payloads[path]).hexdigest() for path in BYTE_PINNED_INPUT_PATHS
    }
    blob_rows = {
        path: git_blob(payloads[path]) for path in BYTE_PINNED_INPUT_PATHS
    }
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
    return {
        "literal_audit_input_paths": list(AUDIT_INPUT_PATHS),
        "byte_pinned_input_paths": list(BYTE_PINNED_INPUT_PATHS),
        "literal_source_read_count": len(AUDIT_INPUT_PATHS),
        "input_sha256": sha_rows,
        "input_git_blobs": blob_rows,
        "sha_pins_match": sha_rows == EXPECTED_INPUT_SHA256,
        "blob_pins_match": blob_rows == EXPECTED_INPUT_BLOBS,
        "all_inputs_relative_and_present": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "forbidden_imports": forbidden,
        "primary_imported_or_executed": False,
        "cycle719_imported_or_executed": False,
        "prior_cycle_text_or_ast_executed": False,
        "primary_ast_timeout_seconds": primary_timeout,
    }


def render_stdout(receipt: dict) -> str:
    findings = receipt["findings"]
    expected = findings["independent_expected"]
    probes = findings["coherent_outcome_probes"]
    lines = [
        "CYCLE983_TRANSLATION_UNIFORM_TWO_STAR_PATCH_INDEPENDENT_CHECK",
        "A_INDEPENDENT_RECONSTRUCTION "
        + ("PASS" if receipt["checks"]["A_INDEPENDENT_RECONSTRUCTION"] else "FAIL")
        + f" :: targets={expected['construction']['target_site_count']};"
        + f" support={expected['construction']['host_support_site_count']};"
        + f" witnesses={[row['witness_count'] for row in expected['uniformity']['target_rows']]};"
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
    agreement_mismatches = [
        key for key in expected if primary_view.get(key) != expected[key]
    ]
    clean, clean_errors = validate_bookkeeping(primary_receipt, primary_cache)
    mutations = mutation_campaign(primary_receipt, primary_cache)
    probes = coherent_outcome_probes(primary_receipt, primary_cache)
    expected_bookkeeping = bool(
        expected["construction"]["target_site_count"]
            == len(expected["construction"]["target_sites"])
        and expected["construction"]["host_support_site_count"]
            == len(expected["construction"]["host_support_sites"])
        and expected["construction"]["minimum_union_size"]
            == expected["construction"]["host_support_site_count"]
        and len(ACTIONS) == 24
        and all(
            row["witness_count"] == len(row["witness_names"])
            and sum(orbit["member_count"] for orbit in row["orbits"])
                == row["witness_count"]
            and all(
                orbit["member_count"] * orbit["effective_stabilizer_order"] == 24
                for orbit in row["orbits"]
            )
            for row in expected["uniformity"]["target_rows"]
        )
    )
    findings = {
        "independent_expected": expected,
        "independent_reconstruction_bookkeeping": expected_bookkeeping,
        "primary_science_agreement": not agreement_mismatches,
        "primary_science_agreement_mismatches": agreement_mismatches,
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
        and deterministic and runtime_budget_met
    )
    receipt = {
        "cycle": CYCLE,
        "artifact": "translation-uniform two-star patch independent refutation checker",
        "audit_status_authority": "independent audit lane only",
        "integrity_policy": (
            "checks gate independent reconstruction, bookkeeping, artifact binding, mutation rejection, and outcome neutrality only; science agreement is reported data"
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
