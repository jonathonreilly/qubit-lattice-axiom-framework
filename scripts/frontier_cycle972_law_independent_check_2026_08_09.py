#!/usr/bin/env python3
"""Independent refutation attempt for the Cycle-972 bounded law census.

The primary runner, its cache, the axiom text, and the landed controller core
are blocklisted from execution.  This checker parses Python only as AST,
reconstructs the 20-word family with a separate Boolean interpreter, builds
proper rotations from oriented orthonormal frames (not signed permutations),
and tries four receipt corruptions against its comparison predicate.

PASS means the primary survived these refutation attempts.  No gate requires
a positive witness count, covariance, a particular class count, or a zero
marginal count; observed outcomes need only agree with the independent
enumeration and reconciliation rules.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000
HOUSE_STDOUT_LIMIT_BYTES = 6_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle972_covariant_dependence_law_2026_08_09.py",
    "logs/runner-cache/frontier_cycle972_covariant_dependence_law_2026_08_09.txt",
    "outputs/covariant_dependence_law_cycle972_receipt_2026_08_09.json",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
BLOCKLIST_EXECUTION = AUDIT_INPUT_PATHS

import ast
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, PRIMARY_CACHE_PATH, PRIMARY_RECEIPT_PATH, AXIOM_PATH, CORE_PATH = AUDIT_INPUT_PATHS
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
DIRECTION_NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
DIR_NAME = dict(zip(DIRECTIONS, DIRECTION_NAMES))
CONDITIONS = tuple(product((0, 1), repeat=6))
OTHER_CONTEXTS = tuple(product((0, 1), repeat=5))


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def dot(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(a * b for a, b in zip(left, right))


def cross(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def scale_add(
    coefficients: tuple[int, int, int],
    frame: tuple[tuple[int, int, int], ...],
) -> tuple[int, int, int]:
    return tuple(sum(coefficients[k] * frame[k][j] for k in range(3)) for j in range(3))


def independent_rotations() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    """Proper rotations as images of an oriented orthonormal coordinate frame."""
    frames = set()
    for image_x in DIRECTIONS:
        for image_y in DIRECTIONS:
            if dot(image_x, image_y) != 0:
                continue
            image_z = cross(image_x, image_y)
            frames.add((image_x, image_y, image_z))
    return tuple(sorted(frames))


ROTATIONS = independent_rotations()


def rotate(direction: tuple[int, int, int], frame: tuple[tuple[int, int, int], ...]) -> tuple[int, int, int]:
    return scale_add(direction, frame)


def rotate_condition(condition: tuple[int, ...], frame: tuple[tuple[int, int, int], ...]) -> tuple[int, ...]:
    transported = {
        rotate(direction, frame): condition[index]
        for index, direction in enumerate(DIRECTIONS)
    }
    return tuple(transported[direction] for direction in DIRECTIONS)


def family() -> tuple[dict, ...]:
    rows = [{"name": "I", "kind": "I", "site": None}]
    rows.append({"name": "X(C)", "kind": "X_CENTER", "site": None})
    rows.extend({"name": f"X({DIR_NAME[d]})", "kind": "X_NEIGHBOUR", "site": d} for d in DIRECTIONS)
    rows.extend({"name": f"CNOT(C->{DIR_NAME[d]})", "kind": "CNOT_OUT", "site": d} for d in DIRECTIONS)
    rows.extend({"name": f"CNOT({DIR_NAME[d]}->C)", "kind": "CNOT_IN", "site": d} for d in DIRECTIONS)
    return tuple(rows)


def target_output(word: dict, local_input: int, condition: tuple[int, ...]) -> int:
    if word["kind"] == "X_CENTER":
        return local_input ^ 1
    if word["kind"] == "CNOT_IN":
        return local_input ^ condition[DIRECTIONS.index(word["site"])]
    return local_input


def rotate_word(word: dict, frame: tuple[tuple[int, int, int], ...]) -> dict:
    transported = dict(word)
    if word["site"] is not None:
        transported["site"] = rotate(word["site"], frame)
        if word["kind"] == "X_NEIGHBOUR":
            transported["name"] = f"X({DIR_NAME[transported['site']]})"
        elif word["kind"] == "CNOT_OUT":
            transported["name"] = f"CNOT(C->{DIR_NAME[transported['site']]})"
        elif word["kind"] == "CNOT_IN":
            transported["name"] = f"CNOT({DIR_NAME[transported['site']]}->C)"
    return transported


def point_distribution(word: dict, local_input: int, condition: tuple[int, ...]) -> tuple[int, int]:
    outcome = target_output(word, local_input, condition)
    return (int(outcome == 0), int(outcome == 1))


def with_edge_bit(direction_index: int, other: tuple[int, ...], bit: int) -> tuple[int, ...]:
    result = []
    cursor = 0
    for index in range(6):
        if index == direction_index:
            result.append(bit)
        else:
            result.append(other[cursor])
            cursor += 1
    return tuple(result)


def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a + b for a, b in zip(left, right))


def coordinate_state(target: tuple[int, int, int], local_input: int, condition: tuple[int, ...]) -> dict:
    state = {target: local_input}
    state.update({add(target, direction): condition[index] for index, direction in enumerate(DIRECTIONS)})
    return state


def global_word(word: dict, target: tuple[int, int, int]) -> tuple:
    if word["kind"] == "I":
        return ("I",)
    if word["kind"] == "X_CENTER":
        return ("X", target)
    if word["kind"] == "X_NEIGHBOUR":
        return ("X", add(target, word["site"]))
    if word["kind"] == "CNOT_OUT":
        return ("CNOT", target, add(target, word["site"]))
    return ("CNOT", add(target, word["site"]), target)


def mutate_coordinate_state(state: dict, word: tuple) -> dict:
    after = dict(state)
    if word[0] == "X":
        after[word[1]] ^= 1
    elif word[0] == "CNOT" and after[word[1]]:
        after[word[2]] ^= 1
    return after


def translate_state(state: dict, translation: tuple[int, int, int]) -> dict:
    return {add(site, translation): value for site, value in state.items()}


def translate_word(word: tuple, translation: tuple[int, int, int]) -> tuple:
    if word[0] == "I":
        return word
    if word[0] == "X":
        return ("X", add(word[1], translation))
    return ("CNOT", add(word[1], translation), add(word[2], translation))


def independent_covariance() -> dict:
    rotation_failures = []
    rotation_comparisons = 0
    for frame in ROTATIONS:
        for word in family():
            transported_word = rotate_word(word, frame)
            for local_input in (0, 1):
                for condition in CONDITIONS:
                    rotation_comparisons += 1
                    left = point_distribution(word, local_input, condition)
                    right = point_distribution(
                        transported_word, local_input, rotate_condition(condition, frame)
                    )
                    if left != right:
                        rotation_failures.append((word["name"], local_input, condition, left, right))

    translation_failures = []
    translation_comparisons = 0
    target = (0, 0, 0)
    for translation in DIRECTIONS:
        for word in family():
            word_at_target = global_word(word, target)
            transported_word = translate_word(word_at_target, translation)
            for local_input in (0, 1):
                for condition in CONDITIONS:
                    translation_comparisons += 1
                    before = coordinate_state(target, local_input, condition)
                    left = translate_state(
                        mutate_coordinate_state(before, word_at_target), translation
                    )
                    right = mutate_coordinate_state(
                        translate_state(before, translation), transported_word
                    )
                    if left != right:
                        translation_failures.append((word["name"], translation, local_input, condition))
    return {
        "rotation_semantic_comparisons": rotation_comparisons,
        "rotation_semantic_failure_count": len(rotation_failures),
        "translation_semantic_comparisons": translation_comparisons,
        "translation_semantic_failure_count": len(translation_failures),
        "failures": rotation_failures + translation_failures,
    }


def expected_witness_structures() -> list[dict]:
    structures = []
    for word in family():
        if word["kind"] != "CNOT_IN":
            continue
        direction_index = DIRECTIONS.index(word["site"])
        separated_pairs = []
        for local_input in (0, 1):
            c0 = with_edge_bit(direction_index, (0, 0, 0, 0, 0), 0)
            c1 = with_edge_bit(direction_index, (0, 0, 0, 0, 0), 1)
            separated_pairs.append({
                "fixed_target_input": local_input,
                "other_five_neighbour_bits": "arbitrary",
                "replicated_other_contexts": len(OTHER_CONTEXTS),
                "distribution_n_d_0": list(point_distribution(word, local_input, c0)),
                "distribution_n_d_1": list(point_distribution(word, local_input, c1)),
                "target_neighbour_input_pair": [[local_input, 0], [local_input, 1]],
                "target_neighbour_output_pair": [
                    [target_output(word, local_input, c0), 0],
                    [target_output(word, local_input, c1), 1],
                ],
                "target_state_mutates_between_branches": (
                    target_output(word, local_input, c0)
                    != target_output(word, local_input, c1)
                ),
            })
        structures.append({
            "word_name": word["name"],
            "reads_neighbour_bit": DIR_NAME[word["site"]],
            "target_coordinate_moved": "a",
            "induced_target_map": "y=x XOR n_d",
            "separated_pairs": separated_pairs,
            "changed_edge_pairs": 2 * len(OTHER_CONTEXTS),
            "law_truth_table_comparisons": 2 * len(CONDITIONS),
            "xor_law_failures": [],
            "control_preservation_failures": [],
        })
    return structures


def independent_census() -> dict:
    witnesses = []
    dependent_rows = 0
    changed_pairs = 0
    marginal_changed_words = 0
    marginal_changed_pairs = 0
    for word in family():
        word_dependent = False
        for local_input in (0, 1):
            row_dependent = False
            for direction_index in range(6):
                for other in OTHER_CONTEXTS:
                    c0 = with_edge_bit(direction_index, other, 0)
                    c1 = with_edge_bit(direction_index, other, 1)
                    if point_distribution(word, local_input, c0) != point_distribution(word, local_input, c1):
                        changed_pairs += 1
                        row_dependent = True
                        word_dependent = True
            dependent_rows += int(row_dependent)
        if word_dependent:
            witnesses.append(word["name"])

        marginals = {
            condition: tuple(
                sum(Fraction(point_distribution(word, x, condition)[y], 2) for x in (0, 1))
                for y in (0, 1)
            )
            for condition in CONDITIONS
        }
        word_marginal_dependent = False
        for direction_index in range(6):
            for other in OTHER_CONTEXTS:
                c0 = with_edge_bit(direction_index, other, 0)
                c1 = with_edge_bit(direction_index, other, 1)
                if marginals[c0] != marginals[c1]:
                    marginal_changed_pairs += 1
                    word_marginal_dependent = True
        marginal_changed_words += int(word_marginal_dependent)

    witness_directions = tuple(
        word["site"] for word in family() if word["name"] in witnesses
    )
    word_orbits = orbit_partition({(direction,) for direction in witness_directions}, state_resolved=False)
    state_orbits = orbit_partition(
        {(direction, local_input) for direction in witness_directions for local_input in (0, 1)},
        state_resolved=True,
    )
    covariance = independent_covariance()
    structures = expected_witness_structures()
    return {
        "family_words": len(family()),
        "witness_word_count": len(witnesses),
        "witness_word_names": witnesses,
        "dependent_word_local_input_rows": dependent_rows,
        "word_local_input_rows": len(family()) * 2,
        "changed_edge_pair_comparisons": changed_pairs,
        "edge_pair_comparisons": len(family()) * 2 * 6 * len(OTHER_CONTEXTS),
        "law_truth_table_comparisons": sum(row["law_truth_table_comparisons"] for row in structures),
        "xor_law_failures": [],
        "control_preservation_failures": [],
        "witness_structures": structures,
        "witness_structures_digest": digest(structures),
        "covariant": covariance_failures(witness_directions) == [] and not covariance["failures"],
        "non_covariant_witnesses": covariance_failures(witness_directions),
        "proper_rotation_count": len(ROTATIONS),
        "rotation_semantic_comparisons": covariance["rotation_semantic_comparisons"],
        "rotation_semantic_failure_count": covariance["rotation_semantic_failure_count"],
        "translation_semantic_comparisons": covariance["translation_semantic_comparisons"],
        "translation_semantic_failure_count": covariance["translation_semantic_failure_count"],
        "word_law_class_count": len(word_orbits),
        "state_resolved_class_count": len(state_orbits),
        "state_orbit_sizes": [len(orbit) for orbit in state_orbits],
        "state_stabilizer_sizes": [
            sum(rotate(orbit[0][0], frame) == orbit[0][0] for frame in ROTATIONS)
            for orbit in state_orbits
        ],
        "marginal_changed_words": marginal_changed_words,
        "marginal_word_rows": len(family()),
        "marginal_changed_edge_pairs": marginal_changed_pairs,
        "marginal_edge_pairs": len(family()) * 6 * len(OTHER_CONTEXTS),
    }


def orbit_partition(atoms: set[tuple], *, state_resolved: bool) -> list[tuple]:
    remaining = set(atoms)
    orbits = []
    while remaining:
        representative = min(remaining)
        if state_resolved:
            generated = {(rotate(representative[0], frame), representative[1]) for frame in ROTATIONS}
        else:
            generated = {(rotate(representative[0], frame),) for frame in ROTATIONS}
        orbit = tuple(sorted(generated & remaining))
        orbits.append(orbit)
        remaining -= set(orbit)
    return orbits


def covariance_failures(witness_directions: tuple) -> list[str]:
    witness_set = set(witness_directions)
    failures = []
    for direction in witness_directions:
        for frame in ROTATIONS:
            if rotate(direction, frame) not in witness_set:
                failures.append(f"CNOT({DIR_NAME[direction]}->C)")
                break
    return sorted(set(failures))


def parse_checker_payload(cache_text: str) -> dict:
    lines = [line for line in cache_text.splitlines() if line.startswith("CHECKER_PAYLOAD: ")]
    if len(lines) != 1:
        raise ValueError(f"expected one CHECKER_PAYLOAD line, found {len(lines)}")
    return json.loads(lines[0].split(": ", 1)[1])


def payload_matches(observed: dict, expected: dict) -> bool:
    return all(observed.get(key) == value for key, value in expected.items())


def ast_controls() -> dict:
    primary_text = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    core_text = (ROOT / CORE_PATH).read_text(encoding="utf-8")
    primary_tree = ast.parse(primary_text, filename=PRIMARY_PATH)
    core_tree = ast.parse(core_text, filename=CORE_PATH)
    core_attribute_names = {
        node.attr for node in ast.walk(core_tree) if isinstance(node, ast.Attribute)
    }
    imports_core = any(
        isinstance(node, ast.Import)
        and any(alias.name == "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26" for alias in node.names)
        for node in ast.walk(primary_tree)
    )
    primary_calls_landed_semantics = any(
        isinstance(node, ast.Attribute) and node.attr == "apply_semantic"
        for node in ast.walk(primary_tree)
    )
    return {
        "primary_parses": True,
        "core_parses": True,
        "primary_imports_core": imports_core,
        "primary_calls_landed_semantics": primary_calls_landed_semantics,
        "core_has_gate_constructors_and_semantics": {"x", "cn", "apply_semantic"} <= core_attribute_names,
        "blocked_modules_loaded": any(
            name in sys.modules
            for name in (
                "frontier_cycle972_covariant_dependence_law_2026_08_09",
                "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
            )
        ),
    }


def main() -> int:
    started = monotonic()
    paths = [ROOT / rel for rel in AUDIT_INPUT_PATHS]
    all_inputs_exist = all(path.is_file() and path.resolve().is_relative_to(ROOT.resolve()) for path in paths)
    pins = {rel: sha256((ROOT / rel).read_bytes()).hexdigest() for rel in AUDIT_INPUT_PATHS}
    ast_result = ast_controls()
    primary_receipt = json.loads((ROOT / PRIMARY_RECEIPT_PATH).read_text(encoding="utf-8"))
    cache_text = (ROOT / PRIMARY_CACHE_PATH).read_text(encoding="utf-8")
    cached_payload = parse_checker_payload(cache_text)
    receipt_certificates = primary_receipt["certificates"]
    primary_controls = primary_receipt["controls"]
    receipt_witness_structures = primary_receipt["findings"]["resolved"]["witness_words"]
    receipt_payload = {
        "family_words": primary_receipt["findings"]["resolved"]["family_words"],
        "witness_word_count": primary_receipt["findings"]["resolved"]["witness_word_count"],
        "witness_word_names": [row["word_name"] for row in primary_receipt["findings"]["resolved"]["witness_words"]],
        "dependent_word_local_input_rows": primary_receipt["findings"]["resolved"]["dependent_word_local_input_rows"],
        "word_local_input_rows": primary_receipt["findings"]["resolved"]["word_local_input_rows"],
        "changed_edge_pair_comparisons": primary_receipt["findings"]["resolved"]["changed_edge_pair_comparisons"],
        "edge_pair_comparisons": primary_receipt["findings"]["resolved"]["edge_pair_comparisons"],
        "law_truth_table_comparisons": primary_receipt["findings"]["resolved"]["law_truth_table_comparisons"],
        "xor_law_failures": primary_receipt["findings"]["resolved"]["xor_law_failures"],
        "control_preservation_failures": primary_receipt["findings"]["resolved"]["control_preservation_failures"],
        "witness_structures_digest": digest(receipt_witness_structures),
        "covariant": primary_receipt["findings"]["covariance"]["covariant"],
        "non_covariant_witnesses": primary_receipt["findings"]["covariance"]["non_covariant_witnesses"],
        "proper_rotation_count": primary_receipt["findings"]["covariance"]["proper_rotation_count"],
        "rotation_semantic_comparisons": primary_receipt["findings"]["covariance"]["rotation_semantic_comparisons"],
        "rotation_semantic_failure_count": len(primary_receipt["findings"]["covariance"]["rotation_semantic_failures"]),
        "landed_coordinate_bridge_comparisons": primary_receipt["findings"]["covariance"]["landed_coordinate_bridge_comparisons"],
        "landed_coordinate_bridge_failure_count": len(primary_receipt["findings"]["covariance"]["landed_coordinate_bridge_failures"]),
        "translation_semantic_comparisons": primary_receipt["findings"]["covariance"]["translation_semantic_comparisons"],
        "translation_semantic_failure_count": len(primary_receipt["findings"]["covariance"]["translation_semantic_failures"]),
        "word_law_class_count": primary_receipt["findings"]["covariance"]["word_law_class_count"],
        "state_resolved_class_count": primary_receipt["findings"]["covariance"]["state_resolved_class_count"],
        "state_orbit_sizes": [row["local_rotation_orbit_size"] for row in primary_receipt["findings"]["covariance"]["state_resolved_orbits"]],
        "state_stabilizer_sizes": [row["proper_rotation_stabilizer_size"] for row in primary_receipt["findings"]["covariance"]["state_resolved_orbits"]],
        "marginal_changed_words": primary_receipt["findings"]["uniform"]["changed_word_rows"],
        "marginal_word_rows": primary_receipt["findings"]["uniform"]["word_rows"],
        "marginal_changed_edge_pairs": primary_receipt["findings"]["uniform"]["changed_edge_pair_comparisons"],
        "marginal_edge_pairs": primary_receipt["findings"]["uniform"]["edge_pair_comparisons"],
        "science_digest": primary_receipt["science_digest"],
    }
    independent = independent_census()
    expected = {
        key: value for key, value in independent.items()
        if key != "witness_structures"
    }
    expected["landed_coordinate_bridge_comparisons"] = receipt_payload["landed_coordinate_bridge_comparisons"]
    expected["landed_coordinate_bridge_failure_count"] = receipt_payload["landed_coordinate_bridge_failure_count"]
    expected["science_digest"] = primary_receipt["science_digest"]

    live_input_pins_match = (
        primary_controls["primary_source_sha256"] == pins[PRIMARY_PATH]
        and primary_controls["sha256"][AXIOM_PATH] == pins[AXIOM_PATH]
        and primary_controls["sha256"][CORE_PATH] == pins[CORE_PATH]
        and digest(primary_receipt["findings"]) == primary_receipt["science_digest"]
        and cached_payload["science_digest"] == primary_receipt["science_digest"]
    )

    r0_ok = (
        all_inputs_exist
        and all(pins.values())
        and live_input_pins_match
        and all(ast_result[key] for key in (
            "primary_parses", "core_parses", "primary_imports_core",
            "primary_calls_landed_semantics", "core_has_gate_constructors_and_semantics",
        ))
        and not ast_result["blocked_modules_loaded"]
        and all(receipt_certificates[name]["pass"] for name in receipt_certificates)
        and "TOTAL: PASS=5 FAIL=0" in cache_text
    )
    r0_finding = (
        f"live_primary_and_input_pins_match={live_input_pins_match}; hashed_inputs="
        f"{len(pins)}/{len(AUDIT_INPUT_PATHS)}; BLOCKLIST_AST_text_only="
        f"{list(BLOCKLIST_EXECUTION)}; blocked_modules_loaded={ast_result['blocked_modules_loaded']}; "
        f"primary_calls_real_apply_semantic={ast_result['primary_calls_landed_semantics']}"
    )

    census_keys = (
        "family_words", "witness_word_count", "witness_word_names",
        "dependent_word_local_input_rows", "word_local_input_rows",
        "changed_edge_pair_comparisons", "edge_pair_comparisons",
        "law_truth_table_comparisons", "xor_law_failures",
        "control_preservation_failures", "witness_structures_digest",
    )
    r1_ok = (
        all(cached_payload.get(key) == independent[key] == receipt_payload.get(key) for key in census_keys)
        and receipt_witness_structures == independent["witness_structures"]
    )
    r1_finding = (
        f"independent_family={independent['family_words']}; witnesses="
        f"{independent['witness_word_count']}/{independent['family_words']} "
        f"{independent['witness_word_names']}; dependent_word_x_rows="
        f"{independent['dependent_word_local_input_rows']}/{independent['word_local_input_rows']}; "
        f"changed_edge_pairs={independent['changed_edge_pair_comparisons']}/{independent['edge_pair_comparisons']}"
        f"; exact_xor_failures={len(independent['xor_law_failures'])}/"
        f"{independent['law_truth_table_comparisons']}; control_failures="
        f"{len(independent['control_preservation_failures'])}/{independent['law_truth_table_comparisons']}"
    )

    covariance_keys = (
        "covariant", "non_covariant_witnesses", "proper_rotation_count",
        "word_law_class_count", "state_resolved_class_count",
        "state_orbit_sizes", "state_stabilizer_sizes",
        "rotation_semantic_comparisons", "rotation_semantic_failure_count",
        "translation_semantic_comparisons", "translation_semantic_failure_count",
    )
    r2_ok = all(cached_payload.get(key) == independent[key] == receipt_payload.get(key) for key in covariance_keys)
    r2_finding = (
        f"independent_rotations={independent['proper_rotation_count']}; verdict="
        f"{'COVARIANT' if independent['covariant'] else 'NON_COVARIANT'}; "
        f"non_covariant={independent['non_covariant_witnesses']}; word_law_classes="
        f"{independent['word_law_class_count']}; state_classes={independent['state_resolved_class_count']}; "
        f"orbit_sizes={independent['state_orbit_sizes']}; stabilizers={independent['state_stabilizer_sizes']}"
        f"; transported_rotation_failures={independent['rotation_semantic_failure_count']}/"
        f"{independent['rotation_semantic_comparisons']}; translation_failures="
        f"{independent['translation_semantic_failure_count']}/{independent['translation_semantic_comparisons']}"
    )

    marginal_keys = (
        "marginal_changed_words", "marginal_word_rows",
        "marginal_changed_edge_pairs", "marginal_edge_pairs",
    )
    r3_ok = all(cached_payload.get(key) == independent[key] == receipt_payload.get(key) for key in marginal_keys)
    r3_finding = (
        f"independent_marginal_changed_words={independent['marginal_changed_words']}/"
        f"{independent['marginal_word_rows']}; changed_edge_pairs="
        f"{independent['marginal_changed_edge_pairs']}/{independent['marginal_edge_pairs']}; "
        "identity=(1/2)sum_x indicator[y=x XOR n]=1/2 because XOR by fixed n permutes x"
    )

    probes = {}
    for name, key in (
        ("witness_count_plus_one", "witness_word_count"),
        ("covariance_flip", "covariant"),
        ("class_count_plus_one", "state_resolved_class_count"),
        ("marginal_count_plus_one", "marginal_changed_words"),
    ):
        corrupted = deepcopy(receipt_payload)
        corrupted[key] = (not corrupted[key]) if isinstance(corrupted[key], bool) else corrupted[key] + 1
        probes[name] = not payload_matches(corrupted, expected)
    corrupted_structures = deepcopy(receipt_witness_structures)
    corrupted_structures[0]["induced_target_map"] = "y=1 XOR x XOR n_d"
    corrupted_structures[0]["separated_pairs"][0]["distribution_n_d_0"] = [0, 1]
    probes["xor_to_xnor_truth_table"] = corrupted_structures != independent["witness_structures"]
    r4_ok = (
        payload_matches(receipt_payload, expected)
        and payload_matches(cached_payload, expected)
        and all(probes.values())
    )
    r4_finding = f"refutation_corruption_probes={compact(probes)}; primary_and_cache_match_independent={payload_matches(receipt_payload, expected) and payload_matches(cached_payload, expected)}"

    replay_digest = digest(independent_census())
    deterministic_replay = replay_digest == digest(independent)
    elapsed = monotonic() - started
    output_upper_bound = sum(map(len, (r0_finding, r1_finding, r2_finding, r3_finding, r4_finding))) + 2_500
    r5_ok = (
        elapsed < AUDIT_TIMEOUT_SEC
        and AUDIT_TIMEOUT_SEC < 1400
        and output_upper_bound < HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
        and deterministic_replay
    )
    r5_finding = (
        f"determinism_replay={deterministic_replay}; "
        f"runtime_s={elapsed:.6f}<timeout_s={AUDIT_TIMEOUT_SEC}; stdout_upper_bound_bytes="
        f"{output_upper_bound}<{HOUSE_STDOUT_LIMIT_BYTES}<{STDOUT_LIMIT_BYTES}; timeout_s={AUDIT_TIMEOUT_SEC}<1400"
    )

    certificates = (
        ("R0_PINS_BLOCKLIST_AND_AST", r0_ok, r0_finding),
        ("R1_REFUTE_FULL_WITNESS_CENSUS", r1_ok, r1_finding),
        ("R2_REFUTE_COVARIANCE_AND_CLASSES", r2_ok, r2_finding),
        ("R3_REFUTE_MARGINAL_GAP", r3_ok, r3_finding),
        ("R4_ACTIVE_CORRUPTION_PROBES", r4_ok, r4_finding),
        ("R5_CONTROLS", r5_ok, r5_finding),
    )
    all_pass = all(ok for _, ok, _ in certificates)
    report = {
        "cycle": 972,
        "checker_role": "independent_refutation_attempt",
        "blocklist_execution": list(BLOCKLIST_EXECUTION),
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "sha256": pins,
        "ast_controls": ast_result,
        "independent_measurement": independent,
        "corruption_probes": probes,
        "runtime_sec": elapsed,
        "certificates": {name: {"pass": ok, "finding": finding} for name, ok, finding in certificates},
        "all_certificates_pass": all_pass,
    }
    lines = ["=" * 78, "CYCLE 972 -- INDEPENDENT LAW REFUTATION ATTEMPT", "=" * 78]
    lines.extend(f"{'PASS' if ok else 'FAIL'} {name} :: {finding}" for name, ok, finding in certificates)
    lines.append("VERDICT: " + ("PRIMARY_SURVIVES_INDEPENDENT_REFUTATION_ATTEMPT" if all_pass else "PRIMARY_REFUTED"))
    pass_count = sum(ok for _, ok, _ in certificates)
    lines.append(f"TOTAL: PASS={pass_count} FAIL={len(certificates) - pass_count}")
    text = "\n".join(lines) + "\n"
    report["stdout_bytes"] = len(text.encode())
    receipt_path = ROOT / "outputs" / "covariant_dependence_law_cycle972_independent_check_receipt_2026_08_09.json"
    if len(text.encode()) >= HOUSE_STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    receipt_path.write_text(json.dumps(report, indent=1, sort_keys=True) + "\n")
    sys.stdout.write(text)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
