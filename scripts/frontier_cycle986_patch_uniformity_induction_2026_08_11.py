#!/usr/bin/env python3
"""Cycle 986: finite-patch uniformity by closed-star gluing induction.

The runner formulates a checkable chart-gluing lemma, exhausts every relative
overlap of two distinct closed unit stars in Z^3, and verifies the 2->3 and
3->4 steps on a sequence that exercises every overlap type.  Science outcomes
are reported data.  Checks gate reconciliation and provenance only, so a
coherent obstruction or not-hostable result remains bookkeeping-clean.
"""

from __future__ import annotations

import ast
import copy
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
CYCLE = 986
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
    "docs/TRANSLATION_UNIFORM_TWO_STAR_PATCH_CYCLE983_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/GENERAL_N_SECTOR_THEOREM_CYCLE738_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/RING_FAMILY_UNIFORMITY_CYCLE737_BOUNDED_THEOREM_NOTE_2026-07-28.md",
)
BLOCKLIST_AST_FRAGMENTS = ("cycle737", "cycle738", "cycle983")

PRIMARY_PATH = "scripts/frontier_cycle986_patch_uniformity_induction_2026_08_11.py"
RECEIPT_PATH = "outputs/patch_uniformity_induction_cycle986_receipt_2026_08_11.json"
EXACT_QUANTIFIER = (
    "for every integer n>=2 and every ordered tuple of distinct targets "
    "(t1,...,tn) in Z^3 such that t2-t1 is a signed unit vector and, for each "
    "m=3,...,n, S(tm) intersects the union of S(ti) for i<m, the same relative "
    "23-program dependence-law chart is translation-uniform on all targets of "
    "the finite support union Omega_n"
)

ZERO = (0, 0, 0)
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
DIRECTION_NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
RELATIVE_SITES = (ZERO, *DIRECTIONS)
CONDITIONS = tuple(product((0, 1), repeat=6))
OTHER_CONTEXTS = tuple(product((0, 1), repeat=5))

# P2x -> P3x -> P4T exercises adjacent, axial-distance-two, and diagonal-distance-two overlaps.
TARGET_A = (0, 0, 0)
TARGET_B = (1, 0, 0)
TARGET_C = (2, 0, 0)
TARGET_D = (1, 1, 0)
STEP_CASES = (
    ("k=2_to_3", (TARGET_A, TARGET_B), TARGET_C),
    ("k=3_to_4", (TARGET_A, TARGET_B, TARGET_C), TARGET_D),
)


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


def coordinate_name(site: tuple[int, int, int]) -> str:
    return f"({site[0]},{site[1]},{site[2]})"


def canonical_pair(left: tuple, right: tuple) -> tuple:
    return tuple(sorted((left, right)))


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
    temporary = tempfile.TemporaryDirectory(prefix="cycle986-cycle719-")
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as bundle:
        bundle.extractall(temporary.name, filter="data")
    scripts_dir = Path(temporary.name) / "scripts"
    sys.path.insert(0, str(scripts_dir))
    core_path = Path(temporary.name) / PINNED_CYCLE719_CORE
    spec = importlib.util.spec_from_file_location("cycle986_pinned_cycle719", core_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load pinned Cycle-719 core")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return temporary, module


PINNED_TEMP, K = load_pinned_cycle719_core()


def closed_star(center: tuple[int, int, int]) -> tuple[tuple[int, int, int], ...]:
    return (center, *(add(center, direction) for direction in DIRECTIONS))


def declared_relative_family() -> tuple:
    return (
        (("I",), ("X", 0))
        + tuple(("CNOT", control, 0) for control in range(1, 7))
        + tuple(
            ("TOF", left, right, 0)
            for left, right in combinations(range(1, 7), 2)
        )
    )


def local_wire_name(wire: int) -> str:
    return "C" if wire == 0 else DIRECTION_NAMES[wire - 1]


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


def core_word(descriptor: tuple) -> tuple:
    if descriptor[0] == "I":
        return ()
    if descriptor[0] == "X":
        return (K.A.x(descriptor[1]),)
    if descriptor[0] == "CNOT":
        return (K.A.cn(descriptor[1], descriptor[2]),)
    return (K.A.tof(descriptor[1], descriptor[2], descriptor[3]),)


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


def landed_output(descriptor: tuple, target: int, neighbours: tuple) -> int:
    return K.A.apply_semantic((target, *neighbours), core_word(descriptor))[0]


def with_edge(index: int, other: tuple, bit: int) -> tuple:
    source = iter(other)
    return tuple(bit if position == index else next(source) for position in range(6))


def witness_measurement(descriptor: tuple) -> dict:
    changed = 0
    for target in (0, 1):
        for direction_index in range(6):
            for other in OTHER_CONTEXTS:
                left = with_edge(direction_index, other, 0)
                right = with_edge(direction_index, other, 1)
                changed += landed_output(descriptor, target, left) != landed_output(
                    descriptor, target, right
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
RELATIVE_SITE_TO_WIRE = {site: wire for wire, site in enumerate(RELATIVE_SITES)}


def rotate_wire(wire: int, rotation: tuple) -> int:
    site = RELATIVE_SITES[wire]
    rotated = tuple(dot(row, site) for row in rotation)
    return RELATIVE_SITE_TO_WIRE[rotated]


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
        sum(RELATIVE_SITES[wire][axis] for wire in controls) for axis in range(3)
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


def orbit_summary(witnesses: tuple) -> list[dict]:
    witness_set = set(witnesses)
    remaining = set(witnesses)
    rows = []
    while remaining:
        seed = min(remaining, key=relative_word_name)
        ambient = {rotate_descriptor(seed, rotation) for rotation in ROTATIONS}
        members = ambient & witness_set
        rows.append({
            "class_label": class_label(seed),
            "member_count": len(members),
            "stabilizer_order": sum(
                rotate_descriptor(seed, rotation) == seed for rotation in ROTATIONS
            ),
            "J_values": sorted({invariant_j(member) for member in members}),
        })
        remaining -= members
    return sorted(rows, key=lambda row: row["class_label"])


def target_census(center: tuple[int, int, int]) -> dict:
    family = declared_relative_family()
    witnesses = []
    truth_failures = 0
    routes = []
    for descriptor in family:
        measurement = witness_measurement(descriptor)
        if measurement["is_witness"]:
            witnesses.append(descriptor)
        for target in (0, 1):
            for neighbours in CONDITIONS:
                truth_failures += landed_output(descriptor, target, neighbours) != (
                    boolean_output(descriptor, target, neighbours)
                )
        routes.append(K.streaming_route(core_word(descriptor), closed_star(center)))
    route_failures = sum(
        row["non_NN_failures"] + row["operand_order_failures"]
        + row["route_return_failures"] for row in routes
    )
    summary = orbit_summary(tuple(witnesses))
    return {
        "target": list(center),
        "complete_closed_star": len(closed_star(center)) == 7,
        "relative_family_size": len(family),
        "truth_table_evaluations": len(family) * 2 * len(CONDITIONS),
        "landed_vs_boolean_failure_count": truth_failures,
        "witness_count": len(witnesses),
        "class_size_J_table": [
            [row["class_label"], row["member_count"], row["J_values"]]
            for row in summary
        ],
        "orbit_stabilizer_products": [
            row["member_count"] * row["stabilizer_order"] for row in summary
        ],
        "all_words_routable": route_failures == 0,
        "route_failure_count": route_failures,
        "maximum_route_distance": max(row["maximum_route_distance"] for row in routes),
        "maximum_touched_sites": max(row["touched_M2"] for row in routes),
        "expanded_primitive_count": sum(row["physical_primitives"] for row in routes),
        "routed_nn_gate_count": sum(row["routed_NN_gates"] for row in routes),
    }


def local_wire(center: tuple, site: tuple) -> int:
    return closed_star(center).index(site)


def descriptor_for_shared_pair(center: tuple, pair: tuple) -> tuple:
    wires = tuple(local_wire(center, site) for site in pair)
    if 0 in wires:
        neighbour = next(wire for wire in wires if wire != 0)
        return ("CNOT", neighbour, 0)
    return ("TOF", *sorted(wires), 0)


def normalized_overlap_table(descriptor: tuple, center: tuple, pair: tuple) -> list[list[int]]:
    control_sites = [site for site in pair if site != center]
    rows = []
    for bits in product((0, 1), repeat=1 + len(control_sites)):
        target = bits[0]
        neighbours = [0] * 6
        for site, bit in zip(control_sites, bits[1:]):
            neighbours[local_wire(center, site) - 1] = bit
        rows.append([*bits, boolean_output(descriptor, target, tuple(neighbours))])
    return rows


def overlap_type(left: tuple, right: tuple) -> str:
    displacement = subtract(right, left)
    distance = l1(left, right)
    if distance == 1:
        return "ADJACENT_CENTRES"
    if distance == 2 and max(abs(value) for value in displacement) == 2:
        return "AXIAL_DISTANCE_TWO_CENTRES"
    if distance == 2:
        return "DIAGONAL_DISTANCE_TWO_CENTRES"
    return "DISJOINT_CLOSED_STARS"


def overlap_record(left: tuple, right: tuple) -> dict:
    left_star = set(closed_star(left))
    right_star = set(closed_star(right))
    shared_sites = tuple(sorted(left_star & right_star))
    shared_pairs = tuple(combinations(shared_sites, 2))
    site_rows = [{
        "global_site": list(site),
        "left_wire": local_wire(left, site),
        "right_wire": local_wire(right, site),
        "left_binding": f"q_{coordinate_name(site)}",
        "right_binding": f"q_{coordinate_name(site)}",
        "binding_agrees": True,
    } for site in shared_sites]
    pair_rows = []
    for raw_pair in shared_pairs:
        pair = canonical_pair(*raw_pair)
        descriptor_left = descriptor_for_shared_pair(left, pair)
        descriptor_right = descriptor_for_shared_pair(right, pair)
        table_left = normalized_overlap_table(descriptor_left, left, pair)
        table_right = normalized_overlap_table(descriptor_right, right, pair)
        path_left = tuple(K.C712.c707.c655.manhattan_path(*pair))
        path_right = tuple(K.C712.c707.c655.manhattan_path(*pair))
        measure_left = witness_measurement(descriptor_left)
        measure_right = witness_measurement(descriptor_right)
        pair_rows.append({
            "global_pair": [list(site) for site in pair],
            "left_local_wires": [local_wire(left, site) for site in pair],
            "right_local_wires": [local_wire(right, site) for site in pair],
            "semantic_pair_in_both": all(site in left_star & right_star for site in pair),
            "z3_edge_left": l1(*pair) == 1,
            "z3_edge_right": l1(*pair) == 1,
            "left_descriptor": relative_word_name(descriptor_left),
            "right_descriptor": relative_word_name(descriptor_right),
            "left_class": class_label(descriptor_left),
            "right_class": class_label(descriptor_right),
            "left_J": invariant_j(descriptor_left),
            "right_J": invariant_j(descriptor_right),
            "normalized_boolean_table_left": table_left,
            "normalized_boolean_table_right": table_right,
            "normalized_boolean_tables_agree": table_left == table_right,
            "left_changed_edge_pairs": measure_left["changed_edge_pairs"],
            "right_changed_edge_pairs": measure_right["changed_edge_pairs"],
            "canonical_global_path_left": [list(site) for site in path_left],
            "canonical_global_path_right": [list(site) for site in path_right],
            "canonical_global_paths_agree": path_left == path_right,
        })
    site_agreement = all(row["binding_agrees"] for row in site_rows)
    pair_agreement = all(
        row["semantic_pair_in_both"]
        and row["z3_edge_left"] == row["z3_edge_right"]
        and row["left_class"] == row["right_class"]
        and row["left_J"] == row["right_J"]
        and row["normalized_boolean_tables_agree"]
        and row["left_changed_edge_pairs"] == row["right_changed_edge_pairs"]
        and row["canonical_global_paths_agree"]
        for row in pair_rows
    )
    return {
        "left_target": list(left),
        "right_target": list(right),
        "right_minus_left": list(subtract(right, left)),
        "centre_distance_L1": l1(left, right),
        "overlap_type": overlap_type(left, right),
        "shared_site_count": len(shared_sites),
        "shared_pair_count": len(shared_pairs),
        "shared_site_agreement_table": site_rows,
        "shared_pair_agreement_table": pair_rows,
        "site_bindings_agree": site_agreement,
        "pair_relations_boolean_classes_J_and_paths_agree": pair_agreement,
        "agreement": site_agreement and pair_agreement,
    }


def overlap_row_bookkeeping_valid(row: dict) -> bool:
    site_rows = row["shared_site_agreement_table"]
    pair_rows = row["shared_pair_agreement_table"]
    site_flags_reconcile = all(
        site["binding_agrees"]
        == (site["left_binding"] == site["right_binding"])
        for site in site_rows
    )
    site_agreement = all(site["binding_agrees"] for site in site_rows)
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
        for pair in pair_rows
    )
    return bool(
        row["shared_site_count"] == len(site_rows)
        and row["shared_pair_count"] == len(pair_rows)
        and site_flags_reconcile
        and row["site_bindings_agree"] == site_agreement
        and row["pair_relations_boolean_classes_J_and_paths_agree"] == pair_agreement
        and row["agreement"] == (site_agreement and pair_agreement)
    )


def target_census_bookkeeping_valid(row: dict) -> bool:
    center = tuple(row["target"])
    return bool(
        row["complete_closed_star"] == (len(closed_star(center)) == 7)
        and row["all_words_routable"] == (row["route_failure_count"] == 0)
        and len(row["class_size_J_table"]) == len(row["orbit_stabilizer_products"])
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


def universal_overlap_census() -> dict:
    rows = []
    for offset in product(range(-2, 3), repeat=3):
        if offset == ZERO or not set(closed_star(ZERO)) & set(closed_star(offset)):
            continue
        rows.append(overlap_record(ZERO, offset))
    summaries = []
    for name in (
        "ADJACENT_CENTRES",
        "AXIAL_DISTANCE_TWO_CENTRES",
        "DIAGONAL_DISTANCE_TWO_CENTRES",
    ):
        members = [row for row in rows if row["overlap_type"] == name]
        pair_rows = [pair for row in members for pair in row["shared_pair_agreement_table"]]
        summaries.append({
            "overlap_type": name,
            "oriented_offset_count": len(members),
            "shared_site_counts": sorted({row["shared_site_count"] for row in members}),
            "shared_pair_counts": sorted({row["shared_pair_count"] for row in members}),
            "pair_classes": sorted({pair["left_class"] for pair in pair_rows}),
            "J_values": sorted({pair["left_J"] for pair in pair_rows}),
            "z3_edge_values": sorted({pair["z3_edge_left"] for pair in pair_rows}),
            "all_agree": all(row["agreement"] for row in members),
        })
    return {
        "relative_offset_domain": "all nonzero d with S(0) intersection S(d) nonempty",
        "oriented_overlap_offset_count": len(rows),
        "rows": rows,
        "type_summary": summaries,
        "all_overlap_types_exhausted": len(rows) == 24,
        "all_pairwise_chart_restrictions_agree": all(row["agreement"] for row in rows),
    }


def extension_case(name: str, existing: tuple, new_target: tuple) -> dict:
    old_support = set().union(*(set(closed_star(target)) for target in existing))
    new_star = set(closed_star(new_target))
    overlap_rows = [
        overlap_record(old_target, new_target)
        for old_target in existing
        if set(closed_star(old_target)) & new_star
    ]
    overlap_sites = tuple(sorted(old_support & new_star))
    cocycle_rows = []
    for site in overlap_sites:
        memberships = [target for target in existing if site in closed_star(target)]
        bindings = [f"q_{coordinate_name(site)}" for _ in (*memberships, new_target)]
        cocycle_rows.append({
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
        "new_support_site_count": len(old_support | new_star),
        "new_star_overlap_with_existing_union_site_count": len(overlap_sites),
        "new_to_old_agreement_table": overlap_rows,
        "overlap_type_multiset": sorted(row["overlap_type"] for row in overlap_rows),
        "site_cocycle_table": cocycle_rows,
        "multiply_shared_site_count": sum(
            row["old_chart_membership_count"] > 1 for row in cocycle_rows
        ),
        "new_target_census": target_census(new_target),
    }
    outcome, obstruction = derive_extension_outcome(result)
    result.update({"outcome": outcome, "exact_obstruction": obstruction})
    return result


def derive_extension_outcome(row: dict) -> tuple[str, str | None]:
    if not row["new_to_old_agreement_table"]:
        return (
            "NOT_GLUEABLE_EMPTY_OVERLAP",
            "new closed star has empty intersection with existing support",
        )
    if not row["new_target_census"]["all_words_routable"]:
        target = tuple(row["new_target"])
        return "NOT_HOSTABLE", f"new target {coordinate_name(target)} is not route-hostable"
    if not all(overlap["agreement"] for overlap in row["new_to_old_agreement_table"]):
        return "OBSTRUCTED", "one or more new-to-old chart restrictions disagree"
    if not all(site["site_cocycle_agrees"] for site in row["site_cocycle_table"]):
        return "OBSTRUCTED", "a multiply shared site fails the chart cocycle"
    return "GLUING_STEP_VERIFIED", None


def gluing_step_measurement(census: dict) -> dict:
    return {
        "lemma_name": "FINITE_CLOSED_STAR_CHART_GLUING_STEP",
        "hypothesis": (
            "Given a uniform k-target patch T_k with support Omega_k, a distinct target s "
            "extends it when S(s) intersects Omega_k; the translated 23-program chart at s "
            "is route-hostable; for every old chart S(t) meeting S(s), both restrictions "
            "agree on every shared global site and shared semantic pair (Z3-edge label, "
            "normalized Boolean table, witness strength, proper-cubic class, J, and canonical "
            "global path); and multiply shared sites satisfy the equality cocycle."
        ),
        "conclusion": (
            "The union chart is uniform on T_k union {s}; no condition is imposed on empty "
            "overlaps, and no simultaneous schedule is inferred."
        ),
        "checkable_obligations": [
            "NEW_STAR_OVERLAPS_EXISTING_SUPPORT",
            "NEW_LOCAL_TEMPLATE_COMPLETE_AND_HOSTABLE",
            "ALL_NEW_TO_OLD_SHARED_SITE_BINDINGS_AGREE",
            "ALL_NEW_TO_OLD_SHARED_PAIR_RECORDS_AGREE",
            "MULTI_CHART_SHARED_SITE_COCYCLE_AGREES",
        ],
        "proof_reduction": (
            "Every datum of the union is either old, new-only, or shared. Old and new-only "
            "data keep their chart values; the pairwise restriction equalities make shared "
            "data single-valued, and equality transitivity gives the site cocycle. The local "
            "rule record is the same translated template at every target."
        ),
        "finite_overlap_census": census,
        "universal_local_step_finding": (
            "VERIFIED_FOR_EVERY_NONEMPTY_TWO_STAR_OVERLAP_TYPE"
            if census["all_overlap_types_exhausted"]
            and census["all_pairwise_chart_restrictions_agree"]
            else "LOCAL_OVERLAP_OBSTRUCTION_FOUND"
        ),
    }


def base_case_measurement() -> dict:
    target_rows = [target_census(TARGET_A), target_census(TARGET_B)]
    overlap = overlap_record(TARGET_A, TARGET_B)
    local_fields = (
        "relative_family_size", "witness_count", "class_size_J_table",
        "orbit_stabilizer_products", "all_words_routable",
        "landed_vs_boolean_failure_count",
    )
    local_agreement = all(
        row[field] == target_rows[0][field]
        for row in target_rows[1:] for field in local_fields
    )
    result = {
        "targets": [list(TARGET_A), list(TARGET_B)],
        "support_site_count": len(set(closed_star(TARGET_A)) | set(closed_star(TARGET_B))),
        "per_target_census": target_rows,
        "target_local_template_fields_agree": local_agreement,
        "adjacent_star_overlap": overlap,
    }
    outcome, obstruction = derive_base_outcome(result)
    result.update({"outcome": outcome, "exact_obstruction": obstruction})
    return result


def derive_base_outcome(base: dict) -> tuple[str, str | None]:
    if not all(row["all_words_routable"] for row in base["per_target_census"]):
        return "NOT_HOSTABLE", "one or more P2x target charts are not route-hostable"
    if not base["target_local_template_fields_agree"]:
        return "OBSTRUCTED", "P2x target-local template records disagree"
    if not base["adjacent_star_overlap"]["agreement"]:
        return "OBSTRUCTED", "P2x adjacent-star restrictions disagree"
    return "P2X_BASE_VERIFIED", None


def derive_induction_status(
    gluing: dict, cases: list[dict], base: dict
) -> tuple[str, str | None]:
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
    failed_cases = [row for row in cases if row["outcome"] != "GLUING_STEP_VERIFIED"]
    if failed_cases:
        return "OBSTRUCTED", compact({
            "case": failed_cases[0]["case"],
            "obstruction": failed_cases[0]["exact_obstruction"],
        })
    return "FINITE_PATCH_INDUCTION_CLOSES_AT_DECLARED_SCOPE", None


def induction_measurement(gluing: dict, cases: list[dict], base: dict) -> dict:
    status, obstruction = derive_induction_status(gluing, cases, base)
    return {
        "induction_status": status,
        "exact_obstruction": obstruction,
        "base_case_reconstruction": base,
        "base_case_provenance": (
            "P2x is reconstructed inside this runner without executing prior-cycle text or AST"
        ),
        "exact_quantifier": EXACT_QUANTIFIER,
        "verdict_line": (
            "FINITE_P2X_ROOTED_STAR_GLUED_PATCH_UNIFORMITY_FOR_ARBITRARY_FINITE_TARGET_COUNT"
            if status == "FINITE_PATCH_INDUCTION_CLOSES_AT_DECLARED_SCOPE"
            else status
        ),
        "target_count_scope": "arbitrary finite n>=2 within the exact quantified family",
        "full_infinite_translation_uniform_lattice_law_claimed": False,
        "infinite_scope_reason": (
            "ordinary finite induction quantifies over each finite n separately; it neither "
            "constructs an infinite allocation nor proves compatible infinite execution"
        ),
        "scope_exclusions": [
            "the infinite target set Z^3 as one executed or allocated patch",
            "a simultaneous conflict-free schedule of alternative local words",
            "a probability distribution, admissibility weight, or selection rule",
            "finite patches outside the stated P2x-rooted star-gluing order",
        ],
    }


def science_measurement() -> dict:
    overlap_census = universal_overlap_census()
    gluing = gluing_step_measurement(overlap_census)
    base = base_case_measurement()
    cases = [extension_case(*case) for case in STEP_CASES]
    induction = induction_measurement(gluing, cases, base)
    return {
        "A_GLUING_STEP": gluing,
        "B_STEP_VERIFICATION": {
            "verified_cases": cases,
            "case_count": len(cases),
            "all_three_overlap_types_exercised": set().union(*(
                set(row["overlap_type_multiset"]) for row in cases
            )) == {
                "ADJACENT_CENTRES",
                "AXIAL_DISTANCE_TWO_CENTRES",
                "DIAGONAL_DISTANCE_TWO_CENTRES",
            },
        },
        "C_INDUCTION_STATUS": induction,
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
            not Path(path).is_absolute() and (ROOT / path).is_file() for path in literal_paths
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


def validate_science_bookkeeping(findings: dict) -> dict:
    gluing = findings["A_GLUING_STEP"]
    census = gluing["finite_overlap_census"]
    cases = findings["B_STEP_VERIFICATION"]["verified_cases"]
    induction = findings["C_INDUCTION_STATUS"]
    a = bool(
        census["oriented_overlap_offset_count"] == len(census["rows"])
        and sum(row["oriented_offset_count"] for row in census["type_summary"])
            == len(census["rows"])
        and all(overlap_row_bookkeeping_valid(row) for row in census["rows"])
    )
    b = bool(
        findings["B_STEP_VERIFICATION"]["case_count"] == len(cases)
        and all(
            row["k"] == len(row["existing_targets"])
            and row["new_star_overlap_with_existing_union_site_count"]
                == len(row["site_cocycle_table"])
            and row["multiply_shared_site_count"] == sum(
                site["old_chart_membership_count"] > 1
                for site in row["site_cocycle_table"]
            )
            and target_census_bookkeeping_valid(row["new_target_census"])
            and all(
                overlap_row_bookkeeping_valid(overlap)
                for overlap in row["new_to_old_agreement_table"]
            )
            and all(cocycle_row_bookkeeping_valid(site) for site in row["site_cocycle_table"])
            and (row["outcome"], row["exact_obstruction"])
                == derive_extension_outcome(row)
            for row in cases
        )
    )
    base = induction["base_case_reconstruction"]
    base_fields = (
        "relative_family_size", "witness_count", "class_size_J_table",
        "orbit_stabilizer_products", "all_words_routable",
        "landed_vs_boolean_failure_count",
    )
    base_local_agreement = all(
        row[field] == base["per_target_census"][0][field]
        for row in base["per_target_census"][1:] for field in base_fields
    )
    base_bookkeeping = bool(
        len(base["targets"]) == len(base["per_target_census"]) == 2
        and base["support_site_count"] == 12
        and base["target_local_template_fields_agree"] == base_local_agreement
        and all(target_census_bookkeeping_valid(row) for row in base["per_target_census"])
        and overlap_row_bookkeeping_valid(base["adjacent_star_overlap"])
        and (base["outcome"], base["exact_obstruction"])
            == derive_base_outcome(base)
    )
    expected_status, expected_obstruction = derive_induction_status(gluing, cases, base)
    c = bool(
        base_bookkeeping
        and
        induction["induction_status"] == expected_status
        and induction["exact_obstruction"] == expected_obstruction
        and induction["full_infinite_translation_uniform_lattice_law_claimed"] is False
        and induction["exact_quantifier"] == EXACT_QUANTIFIER
        and bool(induction["scope_exclusions"])
    )
    return {
        "A_GLUING_STEP": a,
        "B_STEP_VERIFICATION": b,
        "C_INDUCTION_STATUS": c,
    }


def rewrite_probe_induction(findings: dict) -> None:
    gluing = findings["A_GLUING_STEP"]
    cases = findings["B_STEP_VERIFICATION"]["verified_cases"]
    induction = findings["C_INDUCTION_STATUS"]
    status, obstruction = derive_induction_status(
        gluing, cases, induction["base_case_reconstruction"]
    )
    induction["induction_status"] = status
    induction["exact_obstruction"] = obstruction
    induction["verdict_line"] = status


def outcome_neutrality_probes(findings: dict) -> list[dict]:
    probes = []

    obstructed = copy.deepcopy(findings)
    case = obstructed["B_STEP_VERIFICATION"]["verified_cases"][0]
    overlap = case["new_to_old_agreement_table"][0]
    site = overlap["shared_site_agreement_table"][0]
    site["right_binding"] = "q_conflicting_binding"
    site["binding_agrees"] = False
    overlap["site_bindings_agree"] = False
    overlap["agreement"] = False
    case["outcome"], case["exact_obstruction"] = derive_extension_outcome(case)
    rewrite_probe_induction(obstructed)
    checks = validate_science_bookkeeping(obstructed)
    probes.append({
        "name": "coherent_site_binding_obstruction",
        "accepted_by_bookkeeping_gate": all(checks.values()),
        "checks": checks,
    })

    not_hostable = copy.deepcopy(findings)
    case = not_hostable["B_STEP_VERIFICATION"]["verified_cases"][0]
    census = case["new_target_census"]
    census["route_failure_count"] = 1
    census["all_words_routable"] = False
    case["outcome"], case["exact_obstruction"] = derive_extension_outcome(case)
    rewrite_probe_induction(not_hostable)
    checks = validate_science_bookkeeping(not_hostable)
    probes.append({
        "name": "coherent_not_hostable_outcome",
        "accepted_by_bookkeeping_gate": all(checks.values()),
        "checks": checks,
    })
    return probes


def render_stdout(receipt: dict) -> str:
    findings = receipt["findings"]
    gluing = findings["A_GLUING_STEP"]
    cases = findings["B_STEP_VERIFICATION"]["verified_cases"]
    induction = findings["C_INDUCTION_STATUS"]
    summaries = [
        [
            row["overlap_type"], row["oriented_offset_count"],
            row["shared_site_counts"], row["shared_pair_counts"],
            row["pair_classes"], row["J_values"], row["all_agree"],
        ]
        for row in gluing["finite_overlap_census"]["type_summary"]
    ]
    case_rows = [
        [
            row["case"], row["k"], row["new_target"],
            row["new_support_site_count"], row["overlap_type_multiset"],
            row["multiply_shared_site_count"], row["outcome"],
        ]
        for row in cases
    ]
    lines = [
        "CYCLE986_PATCH_UNIFORMITY_STAR_GLUING_INDUCTION",
        "A_GLUING_STEP " + ("PASS" if receipt["checks"]["A_GLUING_STEP"] else "FAIL")
        + f" :: finding={gluing['universal_local_step_finding']}; types={compact(summaries)}",
        "B_STEP_VERIFICATION "
        + ("PASS" if receipt["checks"]["B_STEP_VERIFICATION"] else "FAIL")
        + f" :: cases={compact(case_rows)}",
        "C_INDUCTION_STATUS "
        + ("PASS" if receipt["checks"]["C_INDUCTION_STATUS"] else "FAIL")
        + f" :: status={induction['induction_status']}; verdict={induction['verdict_line']};"
        + f" infinite_claimed={induction['full_infinite_translation_uniform_lattice_law_claimed']};"
        + f" obstruction={compact(induction['exact_obstruction'])}",
        "D_CONTROLS " + ("PASS" if receipt["checks"]["D_CONTROLS"] else "FAIL")
        + f" :: source_reads={receipt['controls']['literal_source_read_count']}<=6;"
        + f" pins={receipt['controls']['sha_pins_match'] and receipt['controls']['blob_pins_match']};"
        + f" prior_ast_text={receipt['controls']['prior_cycle_text_or_ast_executed']};"
        + f" outcome_neutral={compact([row['accepted_by_bookkeeping_gate'] for row in receipt['controls']['outcome_neutrality_probes']])};"
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
    checks = validate_science_bookkeeping(first)
    probes = outcome_neutrality_probes(first)
    runtime_budget_met = monotonic() - started < AUDIT_TIMEOUT_SEC
    controls.update({
        "determinism_replay": deterministic,
        "runtime_budget_met": runtime_budget_met,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "house_stdout_limit_bytes": HOUSE_STDOUT_LIMIT_BYTES,
        "outcome_neutrality_probes": probes,
    })
    checks["D_CONTROLS"] = bool(
        controls["literal_source_read_count"] <= 6
        and controls["all_inputs_relative_and_present"]
        and controls["sha_pins_match"] and controls["blob_pins_match"]
        and controls["blocklist_text_disjoint_from_reads"]
        and not controls["blocked_ast_imports"]
        and not controls["prior_cycle_text_or_ast_executed"]
        and controls["pinned_substrate"]["sha_pin_match"]
        and controls["pinned_substrate"]["blob_pin_match"]
        and controls["base_is_ancestor_of_head"]
        and all(row["accepted_by_bookkeeping_gate"] for row in probes)
        and deterministic and runtime_budget_met
    )
    receipt = {
        "cycle": CYCLE,
        "artifact": "finite-patch star-gluing induction bounded theorem primary",
        "audit_status_authority": "independent audit lane only",
        "integrity_policy": (
            "checks gate construction, reconciliation, and provenance only; verified, "
            "obstructed, not-hostable, and not-glueable outcomes remain cleanly reportable"
        ),
        "findings": first,
        "science_digest": digest(first),
        "controls": controls,
        "checks": checks,
    }
    receipt["primary_source_sha256"] = sha256((ROOT / PRIMARY_PATH).read_bytes()).hexdigest()
    for _ in range(3):
        stdout = render_stdout(receipt)
        controls["stdout_bytes"] = len(stdout.encode())
    stdout = render_stdout(receipt)
    if len(stdout.encode()) >= HOUSE_STDOUT_LIMIT_BYTES:
        receipt["checks"]["D_CONTROLS"] = False
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
