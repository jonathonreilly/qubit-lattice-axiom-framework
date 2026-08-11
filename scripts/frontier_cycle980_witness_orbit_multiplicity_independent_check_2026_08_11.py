#!/usr/bin/env python3
"""Independent refutation checker for the Cycle-980 orbit multiplicities.

The checker never imports or executes the primary or Cycle-719 substrate.  It
parses the primary as text/AST, reconstructs the finite Boolean family and an
independently represented signed-permutation action, validates the pinned
receipt/cache, and applies active corruptions from the declared refute spec.
"""

from __future__ import annotations

import ast
import copy
import json
import sys
from hashlib import sha256
from itertools import combinations, permutations, product
from pathlib import Path
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
CYCLE = 980
AUDIT_TIMEOUT_SEC = 300
HOUSE_STDOUT_LIMIT_BYTES = 6_000
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle980_witness_orbit_multiplicity_2026_08_11.py",
    "outputs/witness_orbit_multiplicity_cycle980_receipt_2026_08_11.json",
    "logs/runner-cache/frontier_cycle980_witness_orbit_multiplicity_2026_08_11.txt",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
EXPECTED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "a6508e92cdd0b9885c08b2a8757fe9cfaf6eedc4f2ac349d6c7713a9aa2f0305",
    AUDIT_INPUT_PATHS[3]:
        "53175250f0458168330160ad6a39c8ec708316f338efd69c49e8eb09e3267b39",
}
EXPECTED_PRIMARY_BLOCKLIST_TEXT_PATHS = (
    "docs/WITNESS_FAMILY_COMPLETENESS_CYCLE977_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/CLASS_COEXISTENCE_BORN_REQUIREMENT_CYCLE979_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "outputs/witness_family_completeness_cycle977_receipt_2026_08_10.json",
    "outputs/class_coexistence_born_requirement_cycle979_receipt_2026_08_10.json",
)
EXPECTED_PRIMARY_BLOCKLIST_AST_MODULES = (
    "frontier_cycle977_witness_family_completeness_2026_08_10",
    "frontier_cycle977_witness_family_independent_check_2026_08_10",
    "frontier_cycle979_class_coexistence_born_requirement_2026_08_10",
    "frontier_cycle979_class_coexistence_independent_check_2026_08_10",
)
PRIMARY_EXPECTED_FUNCTIONS = (
    "load_pinned_cycle719_core",
    "declared_family",
    "is_witness",
    "proper_cubic_rotations",
    "orbit_decomposition",
    "witness_invariant",
    "alphabet_lattice",
)
EXPECTED_PINNED_CYCLE719_COMMIT = "39c74017b870c27c804e3992f2a11e90336476b2"
EXPECTED_PINNED_CYCLE719_CORE_SHA256 = (
    "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4"
)

CHECKER_PATH = (
    "scripts/frontier_cycle980_witness_orbit_multiplicity_independent_check_2026_08_11.py"
)
RECEIPT_PATH = (
    "outputs/witness_orbit_multiplicity_cycle980_independent_check_receipt_2026_08_11.json"
)
LANDED_GATE_MENU = ("X", "CNOT", "TOF")
CENTER = (0, 0, 0)
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
DIRECTION_NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
WIRE_TO_OFFSET = (CENTER, *DIRECTIONS)
OFFSET_TO_WIRE = {offset: wire for wire, offset in enumerate(WIRE_TO_OFFSET)}
SITE_COUNT = len(WIRE_TO_OFFSET)
OTHER_CONTEXTS = tuple(product((0, 1), repeat=5))
REFUTE_SPEC = (
    {"id": "ORBIT_MEMBER_REMOVED", "target": "A", "mutation": "decrement first orbit member count"},
    {"id": "STABILIZER_CORRUPTED", "target": "A", "mutation": "replace first stabilizer order by three"},
    {"id": "WITNESS_DROPPED", "target": "A", "mutation": "drop one derived witness name"},
    {"id": "INVARIANT_VALUE_CORRUPTED", "target": "B", "mutation": "replace CNOT J=1 by J=2"},
    {"id": "INVARIANT_DISTINCT_FLIPPED", "target": "B", "mutation": "flip the separator outcome"},
    {"id": "TOF_ALPHABET_CLASS_COUNT_CORRUPTED", "target": "C", "mutation": "replace TOF-only two orbits by three"},
    {"id": "TRANSLATION_KERNEL_FLIPPED", "target": "A", "mutation": "claim translations are not the recentered kernel"},
    {"id": "CACHE_ORBIT_HEADLINE_CORRUPTED", "target": "R3", "mutation": "replace the 6/12/3 cache headline"},
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def ast_literal_assignment(tree: ast.Module, name: str):
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def site_name(wire: int) -> str:
    return "C" if wire == 0 else DIRECTION_NAMES[wire - 1]


def word_name(descriptor: tuple) -> str:
    if descriptor[0] == "I":
        return "I"
    if descriptor[0] == "X":
        return f"X({site_name(descriptor[1])})"
    if descriptor[0] == "CNOT":
        return f"CNOT({site_name(descriptor[1])}->{site_name(descriptor[2])})"
    return (
        f"TOF({site_name(descriptor[1])},{site_name(descriptor[2])}"
        f"->{site_name(descriptor[3])})"
    )


def independent_family(alphabet: tuple[str, ...]) -> tuple:
    rows = [("I",)]
    if "X" in alphabet:
        rows.extend(("X", target) for target in range(SITE_COUNT))
    if "CNOT" in alphabet:
        rows.extend(
            ("CNOT", control, target)
            for control in range(SITE_COUNT)
            for target in range(SITE_COUNT)
            if control != target
        )
    if "TOF" in alphabet:
        for target in range(SITE_COUNT):
            available = tuple(wire for wire in range(SITE_COUNT) if wire != target)
            for first_index, first in enumerate(available):
                for second in available[first_index + 1:]:
                    rows.append(("TOF", first, second, target))
    return tuple(rows)


def boolean_target(descriptor: tuple, x: int, condition: tuple) -> int:
    state = [x, *condition]
    if descriptor[0] == "X":
        state[descriptor[1]] = 1 - state[descriptor[1]]
    elif descriptor[0] == "CNOT":
        state[descriptor[2]] ^= state[descriptor[1]]
    elif descriptor[0] == "TOF":
        state[descriptor[3]] ^= state[descriptor[1]] * state[descriptor[2]]
    return state[0]


def changed_pairs(descriptor: tuple) -> int:
    total = 0
    for x in (0, 1):
        for edge in range(6):
            remaining = tuple(index for index in range(6) if index != edge)
            for other in OTHER_CONTEXTS:
                low = [0] * 6
                high = [0] * 6
                high[edge] = 1
                for value, index in zip(other, remaining):
                    low[index] = value
                    high[index] = value
                total += boolean_target(descriptor, x, tuple(low)) != boolean_target(
                    descriptor, x, tuple(high)
                )
    return total


def permutation_sign(order: tuple[int, int, int]) -> int:
    inversions = sum(
        order[left] > order[right]
        for left in range(3) for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def independent_rotations() -> tuple:
    return tuple(
        (order, signs)
        for order in permutations(range(3))
        for signs in product((-1, 1), repeat=3)
        if permutation_sign(order) * signs[0] * signs[1] * signs[2] == 1
    )


ROTATIONS = independent_rotations()


def rotate_offset(offset: tuple, rotation: tuple) -> tuple:
    order, signs = rotation
    return tuple(signs[index] * offset[order[index]] for index in range(3))


def rotation_action(rotation: tuple) -> tuple:
    return tuple(rotate_offset(direction, rotation) for direction in DIRECTIONS)


def independent_group_certificate() -> dict:
    actions = {rotation_action(rotation) for rotation in ROTATIONS}
    identity = DIRECTIONS
    composition_closed = True
    all_have_inverse = True
    for left in ROTATIONS:
        for right in ROTATIONS:
            composed = tuple(
                rotate_offset(rotate_offset(direction, right), left)
                for direction in DIRECTIONS
            )
            composition_closed &= composed in actions
        all_have_inverse &= any(
            tuple(
                rotate_offset(rotate_offset(direction, right), left)
                for direction in DIRECTIONS
            ) == identity
            for right in ROTATIONS
        )
    determinants = tuple(
        permutation_sign(order) * signs[0] * signs[1] * signs[2]
        for order, signs in ROTATIONS
    )
    return {
        "generated_order": len(actions),
        "all_signed_permutation_determinants_plus_one": all(
            value == 1 for value in determinants
        ),
        "identity_present": identity in actions,
        "composition_closed": composition_closed,
        "all_have_inverse": all_have_inverse,
    }


def rotate_descriptor(descriptor: tuple, rotation: tuple) -> tuple:
    if descriptor[0] == "I":
        return descriptor
    wires = tuple(
        OFFSET_TO_WIRE[rotate_offset(WIRE_TO_OFFSET[wire], rotation)]
        for wire in descriptor[1:]
    )
    if descriptor[0] == "TOF":
        return (descriptor[0], *sorted(wires[:2]), wires[2])
    return (descriptor[0], *wires)


def dot(left: tuple, right: tuple) -> int:
    return sum(a * b for a, b in zip(left, right))


def independent_invariant(descriptor: tuple) -> dict:
    controls = (descriptor[1],) if descriptor[0] == "CNOT" else descriptor[1:3]
    offsets = tuple(WIRE_TO_OFFSET[wire] for wire in controls)
    summed = tuple(sum(row[axis] for row in offsets) for axis in range(3))
    gram = tuple(
        dot(offsets[left], offsets[right])
        for left in range(len(offsets)) for right in range(left + 1, len(offsets))
    )
    return {
        "control_arity": len(controls),
        "control_sum_norm_squared": dot(summed, summed),
        "off_diagonal_control_gram": list(sorted(gram)),
    }


def independent_label(members: tuple) -> str:
    kinds = {row[0] for row in members}
    values = {independent_invariant(row)["control_sum_norm_squared"] for row in members}
    if kinds == {"CNOT"}:
        return "CNOT"
    if kinds == {"TOF"} and values == {2}:
        return "TOF_PERPENDICULAR_CONTROLS"
    if kinds == {"TOF"} and values == {0}:
        return "TOF_OPPOSITE_CONTROLS"
    return "UNCLASSIFIED_" + digest([sorted(kinds), sorted(values)])[:12]


def independent_orbits(witnesses: tuple) -> dict:
    witness_set = set(witnesses)
    ambient_orbits = {}
    for descriptor in witnesses:
        ambient = frozenset(rotate_descriptor(descriptor, rotation) for rotation in ROTATIONS)
        ambient_orbits.setdefault(ambient, descriptor)
    rows = []
    covered = []
    for ambient, seed in sorted(ambient_orbits.items(), key=lambda item: word_name(min(item[0]))):
        members = tuple(sorted(ambient & witness_set, key=word_name))
        invariants = {
            compact(independent_invariant(descriptor)) for descriptor in members
        }
        stabilizer = sum(
            rotate_descriptor(seed, rotation) == seed for rotation in ROTATIONS
        )
        rows.append({
            "class_label": independent_label(members),
            "representative": word_name(min(members, key=word_name)),
            "member_count": len(members),
            "members": [word_name(row) for row in members],
            "ambient_orbit_size": len(ambient),
            "effective_stabilizer_order": stabilizer,
            "orbit_stabilizer_product": len(ambient) * stabilizer,
            "orbit_is_closed_in_witness_set": ambient <= witness_set,
            "invariant_values": [json.loads(value) for value in sorted(invariants)],
        })
        covered.extend(members)
    value_to_orbits = {}
    for index, row in enumerate(rows):
        for value in row["invariant_values"]:
            value_to_orbits.setdefault(compact(value), []).append(index)
    return {
        "ambient_group": "Z^3 semidirect O+_cubic",
        "finite_witness_data": "target-recentred relative descriptors",
        "translation_action_after_recentring": "trivial kernel Z^3",
        "effective_group": "O+_cubic",
        "effective_group_order": len(ROTATIONS),
        "action_closed_on_witnesses": all(row["orbit_is_closed_in_witness_set"] for row in rows),
        "orbit_count": len(rows),
        "orbits": rows,
        "partition_has_no_overlap_or_omission": (
            len(covered) == len(set(covered)) == len(witnesses)
            and set(covered) == witness_set
        ),
        "invariant_constant_on_each_orbit": all(len(row["invariant_values"]) == 1 for row in rows),
        "invariant_distinct_across_orbits": all(len(indices) == 1 for indices in value_to_orbits.values()),
        "class_count_sum": sum(row["member_count"] for row in rows),
    }


def independent_translation_kernel(witnesses: tuple) -> dict:
    failures = []
    checks = 0
    for translation in DIRECTIONS:
        for descriptor in witnesses:
            checks += 1
            shifted = tuple(
                tuple(translation[axis] + WIRE_TO_OFFSET[wire][axis] for axis in range(3))
                for wire in descriptor[1:]
            )
            recentered = tuple(
                tuple(site[axis] - translation[axis] for axis in range(3))
                for site in shifted
            )
            expected = tuple(WIRE_TO_OFFSET[wire] for wire in descriptor[1:])
            if recentered != expected:
                failures.append((word_name(descriptor), translation))
    return {
        "generator_checks": checks,
        "failure_count": len(failures),
        "translations_are_kernel_after_recentring": not failures,
    }


def independent_family_measurement(alphabet: tuple[str, ...]) -> dict:
    family = independent_family(alphabet)
    per_word_changed = tuple(changed_pairs(row) for row in family)
    witnesses = tuple(row for row, changed in zip(family, per_word_changed) if changed)
    orbits = independent_orbits(witnesses)
    return {
        "alphabet": list(alphabet),
        "family_size": len(family),
        "family_descriptor_digest": digest(family),
        "witness_count": len(witnesses),
        "witness_descriptors": [list(row) for row in witnesses],
        "witness_names": [word_name(row) for row in witnesses],
        "witness_digest": digest(witnesses),
        "changed_edge_pairs": sum(per_word_changed),
        "orbit_count": orbits["orbit_count"],
        "orbit_member_counts": [row["member_count"] for row in orbits["orbits"]],
        "orbit_labels": [row["class_label"] for row in orbits["orbits"]],
    }


def independent_measurement() -> dict:
    full = independent_family_measurement(LANDED_GATE_MENU)
    witnesses = tuple(tuple(row) for row in full["witness_descriptors"])
    orbit = independent_orbits(witnesses)
    subsets = [
        independent_family_measurement(subset)
        for size in range(4) for subset in combinations(LANDED_GATE_MENU, size)
    ]
    return {
        "declared_family": {
            "support": "target-centred radius-one seven-site star",
            "word_length": "zero or one",
            "landed_gate_menu": ["I", *LANDED_GATE_MENU],
            "operand_rule": "distinct wires; TOF controls unordered; no within-star adjacency restriction",
            "cap": "all descriptors in this finite family; no sampling",
        },
        "full_family": full,
        "effective_group_validation": independent_group_certificate(),
        "translation_kernel": independent_translation_kernel(witnesses),
        "orbit_decomposition": orbit,
        "invariant_definition": {
            "name": "J",
            "formula": "J(w)=||sum of centre-relative control displacement vectors||^2",
            "domain": "derived neighbour-dependence witnesses",
        },
        "alphabet_subset_census": subsets,
    }


def independently_comparable_primary_findings(findings: dict) -> dict:
    comparable = copy.deepcopy(findings)
    family_rows = [comparable["full_family"], *comparable["alphabet_subset_census"]]
    for row in family_rows:
        row.pop("landed_boolean_comparisons", None)
        row.pop("landed_boolean_failure_count", None)
    return comparable


def parse_cache(text: str) -> tuple[dict, str, str]:
    if not text.startswith("===== runner cache v1 =====\n"):
        return {}, "", ""
    header_text, remainder = text.split("----- stdout -----\n", 1)
    body, stderr = remainder.split("----- stderr -----\n", 1)
    headers = {}
    for line in header_text.splitlines()[1:]:
        if ": " in line:
            key, value = line.split(": ", 1)
            headers[key] = value
    return headers, body, stderr


def cache_fingerprint(primary_tree: ast.Module) -> str:
    primary_inputs = ast_literal_assignment(primary_tree, "AUDIT_INPUT_PATHS")
    hasher = sha256()
    hasher.update(b"runner-cache-input-fingerprint-v1\0")
    for relative in primary_inputs:
        relative_bytes = relative.encode()
        payload = (ROOT / relative).read_bytes()
        hasher.update(len(relative_bytes).to_bytes(8, "big"))
        hasher.update(relative_bytes)
        hasher.update(len(payload).to_bytes(8, "big"))
        hasher.update(payload)
    return hasher.hexdigest()


def source_controls() -> dict:
    own_tree = ast.parse((ROOT / CHECKER_PATH).read_text(encoding="utf-8"))
    literal_paths = ast_literal_assignment(own_tree, "AUDIT_INPUT_PATHS")
    payloads = {relative: (ROOT / relative).read_bytes() for relative in literal_paths}
    sha_rows = {relative: sha256(payload).hexdigest() for relative, payload in payloads.items()}
    primary_source = payloads[AUDIT_INPUT_PATHS[0]].decode()
    primary_tree = ast.parse(primary_source, filename=AUDIT_INPUT_PATHS[0])
    primary_functions = {
        node.name for node in primary_tree.body if isinstance(node, ast.FunctionDef)
    }
    primary_imports = {
        alias.name
        for node in ast.walk(primary_tree) if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module
        for node in ast.walk(primary_tree)
        if isinstance(node, ast.ImportFrom) and node.module
    }
    return {
        "literal_source_read_count": len(literal_paths),
        "literal_audit_input_paths": list(literal_paths),
        "all_inputs_relative_and_present": all(
            not Path(relative).is_absolute() and (ROOT / relative).is_file()
            for relative in literal_paths
        ),
        "input_sha256": sha_rows,
        "sha_pins_match": all(
            sha_rows.get(relative) == expected
            for relative, expected in EXPECTED_INPUT_SHA256.items()
        ),
        "primary_receipt_sha256": sha_rows[AUDIT_INPUT_PATHS[1]],
        "primary_cache_sha256": sha_rows[AUDIT_INPUT_PATHS[2]],
        "primary_source": primary_source,
        "primary_tree": primary_tree,
        "primary_receipt": json.loads(payloads[AUDIT_INPUT_PATHS[1]]),
        "primary_cache": payloads[AUDIT_INPUT_PATHS[2]].decode(),
        "primary_expected_functions_present": all(
            name in primary_functions for name in PRIMARY_EXPECTED_FUNCTIONS
        ),
        "primary_audit_input_paths": list(ast_literal_assignment(primary_tree, "AUDIT_INPUT_PATHS")),
        "primary_blocklist_text_paths": list(ast_literal_assignment(primary_tree, "BLOCKLIST_TEXT_PATHS")),
        "primary_blocklist_ast_modules": list(ast_literal_assignment(primary_tree, "BLOCKLIST_AST_MODULES")),
        "primary_pinned_commit": ast_literal_assignment(primary_tree, "PINNED_CYCLE719_COMMIT"),
        "primary_pinned_core_sha256": ast_literal_assignment(primary_tree, "PINNED_CYCLE719_CORE_SHA256"),
        "blocked_primary_imports": sorted(
            name for name in primary_imports
            if any(name.endswith(blocked) for blocked in EXPECTED_PRIMARY_BLOCKLIST_AST_MODULES)
        ),
        "primary_imported_or_executed": False,
    }


def validate_cache(controls: dict, expected: dict) -> bool:
    headers, body, stderr = parse_cache(controls["primary_cache"])
    receipt = controls["primary_receipt"]
    normalized_stdout = body.rstrip() + "\n"
    orbit = expected["orbit_decomposition"]
    expected_orbits = compact([
        [row["class_label"], row["member_count"], row["effective_stabilizer_order"]]
        for row in orbit["orbits"]
    ])
    expected_invariants = compact([
        [row["class_label"], row["invariant_values"]] for row in orbit["orbits"]
    ])
    expected_alphabets = compact({
        "+".join(row["alphabet"]) or "I_ONLY": row["orbit_count"]
        for row in expected["alphabet_subset_census"]
    })
    try:
        elapsed_nonnegative = float(headers.get("elapsed_sec", "-1")) >= 0
    except ValueError:
        elapsed_nonnegative = False
    return bool(
        headers.get("runner") == AUDIT_INPUT_PATHS[0]
        and headers.get("runner_sha256") == EXPECTED_INPUT_SHA256[AUDIT_INPUT_PATHS[0]]
        and headers.get("input_fingerprint_sha256") == cache_fingerprint(controls["primary_tree"])
        and headers.get("timeout_sec") == "1400"
        and headers.get("exit_code") == "0" and headers.get("status") == "ok"
        and elapsed_nonnegative and not stderr.strip()
        and receipt["primary_source_sha256"] == headers.get("runner_sha256")
        and receipt["stdout_sha256"] == sha256(normalized_stdout.encode()).hexdigest()
        and f"action_closed={orbit['action_closed_on_witnesses']}" in body
        and f"orbits={expected_orbits}" in body
        and f"sum={orbit['class_count_sum']}" in body
        and f"values={expected_invariants}" in body
        and f"constant={orbit['invariant_constant_on_each_orbit']}" in body
        and f"distinct={orbit['invariant_distinct_across_orbits']}" in body
        and f"alphabet_to_classes={expected_alphabets}" in body
        and body.rstrip().endswith("TOTAL: PASS=4 FAIL=0")
    )


def validate_primary(receipt: dict, expected: dict) -> bool:
    return bool(
        independently_comparable_primary_findings(receipt.get("findings", {})) == expected
        and receipt.get("science_digest") == digest(receipt.get("findings", {}))
        and receipt.get("pass") is True
        and all(receipt.get("checks", {}).values())
        and receipt.get("primary_source_sha256") == EXPECTED_INPUT_SHA256[AUDIT_INPUT_PATHS[0]]
    )


def corruption_probes(receipt: dict, cache: str, expected: dict, controls: dict) -> dict:
    results = {}
    original_receipt_valid = validate_primary(receipt, expected)

    def receipt_rejected(mutated: dict) -> bool:
        return bool(
            original_receipt_valid and mutated != receipt
            and not validate_primary(mutated, expected)
        )

    mutated = copy.deepcopy(receipt)
    mutated["findings"]["orbit_decomposition"]["orbits"][0]["member_count"] -= 1
    results["ORBIT_MEMBER_REMOVED"] = receipt_rejected(mutated)
    mutated = copy.deepcopy(receipt)
    mutated["findings"]["orbit_decomposition"]["orbits"][0]["effective_stabilizer_order"] = 3
    results["STABILIZER_CORRUPTED"] = receipt_rejected(mutated)
    mutated = copy.deepcopy(receipt)
    mutated["findings"]["full_family"]["witness_names"].pop()
    results["WITNESS_DROPPED"] = receipt_rejected(mutated)
    mutated = copy.deepcopy(receipt)
    mutated["findings"]["orbit_decomposition"]["orbits"][0]["invariant_values"][0]["control_sum_norm_squared"] = 2
    results["INVARIANT_VALUE_CORRUPTED"] = receipt_rejected(mutated)
    mutated = copy.deepcopy(receipt)
    mutated["findings"]["orbit_decomposition"]["invariant_distinct_across_orbits"] = False
    results["INVARIANT_DISTINCT_FLIPPED"] = receipt_rejected(mutated)
    mutated = copy.deepcopy(receipt)
    tof_row = next(
        row for row in mutated["findings"]["alphabet_subset_census"]
        if row["alphabet"] == ["TOF"]
    )
    tof_row["orbit_count"] = 3
    results["TOF_ALPHABET_CLASS_COUNT_CORRUPTED"] = receipt_rejected(mutated)
    mutated = copy.deepcopy(receipt)
    mutated["findings"]["translation_kernel"]["translations_are_kernel_after_recentring"] = False
    results["TRANSLATION_KERNEL_FLIPPED"] = receipt_rejected(mutated)
    orbit_rows = expected["orbit_decomposition"]["orbits"]
    original_orbits = compact([
        [row["class_label"], row["member_count"], row["effective_stabilizer_order"]]
        for row in orbit_rows
    ])
    corrupted_rows = [
        [row["class_label"], row["member_count"], row["effective_stabilizer_order"]]
        for row in orbit_rows
    ]
    corrupted_rows[0][1] += 1
    mutated_cache = cache.replace(
        f"orbits={original_orbits}", f"orbits={compact(corrupted_rows)}", 1
    )
    mutated_controls = dict(controls)
    mutated_controls["primary_cache"] = mutated_cache
    results["CACHE_ORBIT_HEADLINE_CORRUPTED"] = bool(
        validate_cache(controls, expected)
        and mutated_cache != cache
        and not validate_cache(mutated_controls, expected)
    )
    return {
        "refute_spec": list(REFUTE_SPEC),
        "results": results,
        "all_rejected": set(results) == {row["id"] for row in REFUTE_SPEC}
        and all(results.values()),
    }


def render_stdout(receipt: dict) -> str:
    checks = receipt["checks"]
    independent = receipt["independent_measurement"]
    orbit = independent["orbit_decomposition"]
    probes = receipt["active_corruption_probes"]
    rows = [
        "CYCLE980_WITNESS_ORBIT_MULTIPLICITY_INDEPENDENT_CHECK",
        "R0_PRIMARY_AST_TEXT_AND_PINS " + ("PASS" if checks["R0_PRIMARY_AST_TEXT_AND_PINS"] else "FAIL")
        + f" :: source_reads={receipt['controls']['literal_source_read_count']}<=6;"
        + f" sha_pins={receipt['controls']['sha_pins_match']}; primary_executed=false",
        "R1_INDEPENDENT_ORBIT_CENSUS " + ("PASS" if checks["R1_INDEPENDENT_ORBIT_CENSUS"] else "FAIL")
        + " :: orbit_size_stabilizer=" + compact([
            [row["member_count"], row["effective_stabilizer_order"]]
            for row in orbit["orbits"]
        ]) + f"; witnesses={independent['full_family']['witness_count']}",
        "R2_INVARIANT_AND_ALPHABET " + ("PASS" if checks["R2_INVARIANT_AND_ALPHABET"] else "FAIL")
        + f" :: J_constant={orbit['invariant_constant_on_each_orbit']};"
        + f" J_distinct={orbit['invariant_distinct_across_orbits']};"
        + " alphabet_classes=" + compact({
            "+".join(row["alphabet"]) or "I_ONLY": row["orbit_count"]
            for row in independent["alphabet_subset_census"]
        }),
        "R3_RECEIPT_CACHE_BINDING " + ("PASS" if checks["R3_RECEIPT_CACHE_BINDING"] else "FAIL")
        + f" :: primary_source_receipt_cache_bound={checks['R3_RECEIPT_CACHE_BINDING']}",
        "R4_ACTIVE_CORRUPTION_PROBES " + ("PASS" if checks["R4_ACTIVE_CORRUPTION_PROBES"] else "FAIL")
        + f" :: rejected={sum(probes['results'].values())}/{len(probes['results'])}",
        "R5_CONTROLS " + ("PASS" if checks["R5_CONTROLS"] else "FAIL")
        + f" :: determinism={receipt['controls']['determinism_replay']};"
        + f" runtime_s={receipt['controls']['runtime_seconds']:.3f}<300;"
        + f" stdout_bytes={receipt['controls']['stdout_bytes']}<6000<150000",
    ]
    rows.append(f"TOTAL: PASS={sum(checks.values())} FAIL={sum(not value for value in checks.values())}")
    return "\n".join(rows) + "\n"


def run() -> tuple[dict, str]:
    started = monotonic()
    controls = source_controls()
    first = independent_measurement()
    second = independent_measurement()
    deterministic = first == second
    primary_receipt = controls["primary_receipt"]
    r0 = bool(
        controls["literal_source_read_count"] <= 6
        and controls["all_inputs_relative_and_present"] and controls["sha_pins_match"]
        and controls["primary_expected_functions_present"]
        and len(controls["primary_audit_input_paths"]) <= 6
        and tuple(controls["primary_blocklist_text_paths"]) == EXPECTED_PRIMARY_BLOCKLIST_TEXT_PATHS
        and tuple(controls["primary_blocklist_ast_modules"]) == EXPECTED_PRIMARY_BLOCKLIST_AST_MODULES
        and not controls["blocked_primary_imports"]
        and controls["primary_pinned_commit"] == EXPECTED_PINNED_CYCLE719_COMMIT
        and controls["primary_pinned_core_sha256"] == EXPECTED_PINNED_CYCLE719_CORE_SHA256
        and controls["primary_imported_or_executed"] is False
    )
    r1 = validate_primary(primary_receipt, first)
    orbit = first["orbit_decomposition"]
    comparable_primary = independently_comparable_primary_findings(
        primary_receipt["findings"]
    )
    r2 = bool(
        comparable_primary["invariant_definition"] == first["invariant_definition"]
        and comparable_primary["alphabet_subset_census"] == first["alphabet_subset_census"]
        and orbit["class_count_sum"] == first["full_family"]["witness_count"]
    )
    r3 = validate_cache(controls, first)
    probes = corruption_probes(primary_receipt, controls["primary_cache"], first, controls)
    r4 = probes["all_rejected"]
    controls = {
        key: value for key, value in controls.items()
        if key not in {"primary_source", "primary_tree", "primary_receipt", "primary_cache"}
    }
    controls.update({
        "determinism_replay": deterministic,
        "runtime_seconds": monotonic() - started,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "house_stdout_limit_bytes": HOUSE_STDOUT_LIMIT_BYTES,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    })
    receipt = {
        "cycle": CYCLE,
        "checker": "independent refutation checker",
        "primary_imported_or_executed": False,
        "independent_measurement": first,
        "active_corruption_probes": probes,
        "controls": controls,
        "checks": {
            "R0_PRIMARY_AST_TEXT_AND_PINS": r0,
            "R1_INDEPENDENT_ORBIT_CENSUS": r1,
            "R2_INVARIANT_AND_ALPHABET": r2,
            "R3_RECEIPT_CACHE_BINDING": r3,
            "R4_ACTIVE_CORRUPTION_PROBES": r4,
            "R5_CONTROLS": False,
        },
    }
    for _ in range(3):
        stdout = render_stdout(receipt)
        controls["stdout_bytes"] = len(stdout.encode())
    stdout = render_stdout(receipt)
    r5 = bool(
        deterministic and controls["runtime_seconds"] < AUDIT_TIMEOUT_SEC
        and len(stdout.encode()) < HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
    )
    receipt["checks"]["R5_CONTROLS"] = r5
    controls["stdout_bytes"] = len(stdout.encode())
    stdout = render_stdout(receipt)
    receipt["pass"] = all(receipt["checks"].values())
    source_sha = sha256((ROOT / CHECKER_PATH).read_bytes()).hexdigest()
    receipt["checker_source_sha256"] = source_sha
    receipt["stdout_sha256"] = sha256(stdout.encode()).hexdigest()
    return receipt, stdout


def main() -> int:
    if sys.argv[1:]:
        raise SystemExit(f"usage: {Path(__file__).name}")
    receipt, stdout = run()
    receipt_path = ROOT / RECEIPT_PATH
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sys.stdout.write(stdout)
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
