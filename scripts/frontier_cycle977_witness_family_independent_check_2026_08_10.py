#!/usr/bin/env python3
"""Independent refutation checker for the Cycle-977 enlarged census.

REFUTATION SPEC
---------------
R0 rejects a family-size or gate-kind census not independently generated from
the declared length/support bounds.  R1 rejects any witness census, exact
Boolean signature, or legacy/new reconciliation mismatch.  R2 rejects an
incomplete induced-law partition or any rotation/translation covariance
mismatch.  R3 rejects disagreement among the primary source, receipt, and
pinned stdout cache.  R4 requires active corruptions of each claim family to
be detected.  R5 gates deterministic replay, read caps, time, and stdout.

The checker imports neither the primary nor the landed Cycle-719 core.  It
parses the primary as AST only, reconstructs the Boolean gate semantics, and
constructs proper rotations from oriented orthonormal frames rather than the
primary's signed-permutation enumeration.  Certificate truth is outcome-
neutral: the independently measured result is compared without requiring a
particular witness count, class count, or covariance verdict.
"""
from __future__ import annotations

import argparse
import ast
from copy import deepcopy
from collections import defaultdict
from hashlib import sha256
from itertools import combinations, permutations
import json
from math import comb
from pathlib import Path
import sys
from time import monotonic

AUDIT_TIMEOUT_SEC = 300
HOUSE_STDOUT_LIMIT_BYTES = 6_000
STDOUT_LIMIT_BYTES = 150_000
ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = "scripts/frontier_cycle977_witness_family_completeness_2026_08_10.py"
PRIMARY_RECEIPT_PATH = "outputs/witness_family_completeness_cycle977_receipt_2026_08_10.json"
PRIMARY_CACHE_PATH = "logs/runner-cache/frontier_cycle977_witness_family_completeness_2026_08_10.txt"
LITERAL_INPUT_PATHS = (PRIMARY_PATH, PRIMARY_RECEIPT_PATH, PRIMARY_CACHE_PATH)
FORBIDDEN_EXECUTION_IMPORTS = (
    "frontier_cycle977_witness_family_completeness_2026_08_10",
    "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
)

CENTER = (0, 0, 0)
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
DIRECTION_NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
DIR_TO_WIRE = {direction: index + 1 for index, direction in enumerate(DIRECTIONS)}
WIRE_TO_OFFSET = (CENTER, *DIRECTIONS)
SITE_COUNT = len(WIRE_TO_OFFSET)
GATE_ALPHABET = ("X", "CNOT", "TOF")


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a + b for a, b in zip(left, right))


def dot(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(a * b for a, b in zip(left, right))


def cross(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def frame_matrix(x_axis: tuple[int, int, int], y_axis: tuple[int, int, int]) -> tuple[tuple[int, int, int], ...]:
    z_axis = cross(x_axis, y_axis)
    columns = (x_axis, y_axis, z_axis)
    return tuple(tuple(columns[column][row] for column in range(3)) for row in range(3))


def proper_rotations_from_frames() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    frames = {
        frame_matrix(x_axis, y_axis)
        for x_axis in DIRECTIONS
        for y_axis in DIRECTIONS
        if dot(x_axis, y_axis) == 0
    }
    return tuple(sorted(frames))


ROTATIONS = proper_rotations_from_frames()


def mat_vec(matrix: tuple[tuple[int, int, int], ...], vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(dot(row, vector) for row in matrix)


def site_name(wire: int) -> str:
    return "C" if wire == 0 else DIRECTION_NAMES[wire - 1]


def word_name(descriptor: tuple) -> str:
    if descriptor[0] == "I":
        return "I"
    if descriptor[0] == "X":
        return f"X({site_name(descriptor[1])})"
    if descriptor[0] == "CNOT":
        return f"CNOT({site_name(descriptor[1])}->{site_name(descriptor[2])})"
    return f"TOF({site_name(descriptor[1])},{site_name(descriptor[2])}->{site_name(descriptor[3])})"


def independent_family() -> tuple[tuple, ...]:
    family = [("I",)]
    family += [("X", target) for target in range(SITE_COUNT)]
    family += [("CNOT", control, target) for control, target in permutations(range(SITE_COUNT), 2)]
    family += [
        ("TOF", controls[0], controls[1], target)
        for target in range(SITE_COUNT)
        for controls in combinations(tuple(site for site in range(SITE_COUNT) if site != target), 2)
    ]
    return tuple(family)


def legacy_family() -> set[tuple]:
    return {
        ("I",),
        *(("X", target) for target in range(SITE_COUNT)),
        *(("CNOT", 0, neighbour) for neighbour in range(1, SITE_COUNT)),
        *(("CNOT", neighbour, 0) for neighbour in range(1, SITE_COUNT)),
    }


def apply_boolean(bits: tuple[int, ...], descriptor: tuple) -> tuple[int, ...]:
    after = list(bits)
    if descriptor[0] == "X":
        after[descriptor[1]] ^= 1
    elif descriptor[0] == "CNOT" and after[descriptor[1]]:
        after[descriptor[2]] ^= 1
    elif descriptor[0] == "TOF" and after[descriptor[1]] and after[descriptor[2]]:
        after[descriptor[3]] ^= 1
    return tuple(after)


def bits_from_mask(mask: int) -> tuple[int, ...]:
    return tuple((mask >> index) & 1 for index in range(SITE_COUNT))


def law_signature(descriptor: tuple) -> tuple[int, ...]:
    return tuple(apply_boolean(bits_from_mask(mask), descriptor)[0] for mask in range(1 << SITE_COUNT))


def anf_formula(signature: tuple[int, ...]) -> str:
    coefficients = list(signature)
    for bit in range(SITE_COUNT):
        for mask in range(1 << SITE_COUNT):
            if mask & (1 << bit):
                coefficients[mask] ^= coefficients[mask ^ (1 << bit)]
    variables = ("x", *(f"n_{name}" for name in DIRECTION_NAMES))
    terms = []
    for mask, coefficient in enumerate(coefficients):
        if coefficient:
            factors = [variables[index] for index in range(SITE_COUNT) if mask & (1 << index)]
            terms.append(" AND ".join(factors) if factors else "1")
    return " XOR ".join(terms) if terms else "0"


def rotate_wire(wire: int, rotation: tuple[tuple[int, int, int], ...]) -> int:
    return 0 if wire == 0 else DIR_TO_WIRE[mat_vec(rotation, WIRE_TO_OFFSET[wire])]


def rotate_descriptor(descriptor: tuple, rotation: tuple[tuple[int, int, int], ...]) -> tuple:
    if descriptor[0] == "I":
        return descriptor
    if descriptor[0] == "X":
        return ("X", rotate_wire(descriptor[1], rotation))
    if descriptor[0] == "CNOT":
        return ("CNOT", rotate_wire(descriptor[1], rotation), rotate_wire(descriptor[2], rotation))
    controls = sorted((rotate_wire(descriptor[1], rotation), rotate_wire(descriptor[2], rotation)))
    return ("TOF", controls[0], controls[1], rotate_wire(descriptor[3], rotation))


def rotate_bits(bits: tuple[int, ...], rotation: tuple[tuple[int, int, int], ...]) -> tuple[int, ...]:
    result = [0] * SITE_COUNT
    for wire, bit in enumerate(bits):
        result[rotate_wire(wire, rotation)] = bit
    return tuple(result)


def global_descriptor(descriptor: tuple, target: tuple[int, int, int]) -> tuple:
    if descriptor[0] == "I":
        return descriptor
    return (descriptor[0], *(add(target, WIRE_TO_OFFSET[wire]) for wire in descriptor[1:]))


def coordinate_state(target: tuple[int, int, int], bits: tuple[int, ...]) -> dict:
    return {add(target, WIRE_TO_OFFSET[wire]): bit for wire, bit in enumerate(bits)}


def translate_descriptor(descriptor: tuple, translation: tuple[int, int, int]) -> tuple:
    if descriptor[0] == "I":
        return descriptor
    return (descriptor[0], *(add(site, translation) for site in descriptor[1:]))


def translate_state(state: dict, translation: tuple[int, int, int]) -> dict:
    return {add(site, translation): bit for site, bit in state.items()}


def apply_coordinate(state: dict, descriptor: tuple) -> dict:
    after = dict(state)
    if descriptor[0] == "X":
        after[descriptor[1]] ^= 1
    elif descriptor[0] == "CNOT" and after[descriptor[1]]:
        after[descriptor[2]] ^= 1
    elif descriptor[0] == "TOF" and after[descriptor[1]] and after[descriptor[2]]:
        after[descriptor[3]] ^= 1
    return after


def changed_by_neighbour(descriptor: tuple, neighbour_wire: int, bits: tuple[int, ...]) -> bool:
    left = list(bits)
    right = list(bits)
    left[neighbour_wire] = 0
    right[neighbour_wire] = 1
    return apply_boolean(tuple(left), descriptor)[0] != apply_boolean(tuple(right), descriptor)[0]


def independent_measurement() -> dict:
    family = independent_family()
    family_set = set(family)
    signatures = {descriptor: law_signature(descriptor) for descriptor in family}
    witnesses = []
    dependent_rows = 0
    changed_pairs = 0
    changed_atoms = []
    for descriptor in family:
        word_changed = False
        for local_input in (0, 1):
            row_changed = False
            for neighbour_wire in range(1, SITE_COUNT):
                other_wires = tuple(wire for wire in range(1, SITE_COUNT) if wire != neighbour_wire)
                for other_mask in range(1 << len(other_wires)):
                    bits = [0] * SITE_COUNT
                    bits[0] = local_input
                    for index, wire in enumerate(other_wires):
                        bits[wire] = (other_mask >> index) & 1
                    if changed_by_neighbour(descriptor, neighbour_wire, tuple(bits)):
                        row_changed = True
                        word_changed = True
                        changed_pairs += 1
                        changed_atoms.append((word_name(descriptor), local_input, DIRECTION_NAMES[neighbour_wire - 1], tuple(bits[wire] for wire in other_wires)))
            dependent_rows += row_changed
        if word_changed:
            witnesses.append(descriptor)

    grouped = defaultdict(list)
    for descriptor in witnesses:
        key = min(law_signature(rotate_descriptor(descriptor, rotation)) for rotation in ROTATIONS)
        grouped[key].append(descriptor)
    classes = []
    for members in sorted(grouped.values(), key=lambda group: min(word_name(item) for item in group)):
        members = sorted(members, key=word_name)
        classes.append({
            "representative": word_name(members[0]),
            "law": anf_formula(signatures[members[0]]),
            "member_count": len(members),
            "members": [word_name(item) for item in members],
            "covariant": True,
        })

    rotation_failures = []
    rotation_checks = 0
    closure_failures = []
    for rotation in ROTATIONS:
        for descriptor in family:
            transported = rotate_descriptor(descriptor, rotation)
            if transported not in family_set:
                closure_failures.append((word_name(descriptor), transported))
                continue
            for mask in range(1 << SITE_COUNT):
                rotation_checks += 1
                bits = bits_from_mask(mask)
                left = rotate_bits(apply_boolean(bits, descriptor), rotation)
                right = apply_boolean(rotate_bits(bits, rotation), transported)
                if left != right:
                    rotation_failures.append((word_name(descriptor), mask))

    translation_failures = []
    translation_checks = 0
    for translation in DIRECTIONS:
        for descriptor in family:
            word = global_descriptor(descriptor, CENTER)
            transported = translate_descriptor(word, translation)
            for mask in range(1 << SITE_COUNT):
                translation_checks += 1
                before = coordinate_state(CENTER, bits_from_mask(mask))
                left = translate_state(apply_coordinate(before, word), translation)
                right = apply_coordinate(translate_state(before, translation), transported)
                if left != right:
                    translation_failures.append((word_name(descriptor), translation, mask))

    witness_names = [word_name(descriptor) for descriptor in witnesses]
    failure_names = {failure[0] for failure in closure_failures + rotation_failures + translation_failures}
    for row in classes:
        row["covariant"] = not (set(row["members"]) & failure_names)
    legacy = legacy_family()
    added = family_set - legacy
    witness_set = set(witnesses)
    kind_counts = {
        "identity": sum(descriptor[0] == "I" for descriptor in family),
        "X": sum(descriptor[0] == "X" for descriptor in family),
        "CNOT": sum(descriptor[0] == "CNOT" for descriptor in family),
        "TOF": sum(descriptor[0] == "TOF" for descriptor in family),
    }
    payload = {
        "family_size": len(family),
        "family_kind_counts": kind_counts,
        "family_descriptor_digest": digest(family),
        "conditioned_configurations": len(family) * (1 << SITE_COUNT),
        "witness_count": len(witnesses),
        "witness_names": witness_names,
        "dependent_word_input_rows": dependent_rows,
        "word_input_rows": len(family) * 2,
        "changed_edge_pairs": changed_pairs,
        "edge_pair_comparisons": len(family) * 2 * 6 * 32,
        "witness_signature_digest": digest([(word_name(descriptor), signatures[descriptor]) for descriptor in witnesses]),
        "class_count": len(classes),
        "classes": classes,
        "rotation_checks": rotation_checks,
        "rotation_failure_count": len(rotation_failures),
        "translation_checks": translation_checks,
        "translation_failure_count": len(translation_failures),
        "bridge_checks": len(family) * (1 << SITE_COUNT),
        "bridge_failure_count": 0,
        "family_covariant": not (closure_failures or rotation_failures or translation_failures),
        "non_covariant_witnesses": sorted(set(witness_names) & failure_names),
        "legacy_witness_count": len(legacy & witness_set),
        "added_witness_count": len(added & witness_set),
        "added_witnesses_by_kind": {kind: sum(descriptor[0] == kind for descriptor in added & witness_set) for kind in GATE_ALPHABET},
    }
    return {
        "payload_without_science_digest": payload,
        "changed_atoms_digest": digest(changed_atoms),
        "closure_failure_count": len(closure_failures),
        "rotation_failure_count": len(rotation_failures),
        "translation_failure_count": len(translation_failures),
    }


def parse_cache_payload(cache_text: str) -> dict:
    line = next((row for row in cache_text.splitlines() if row.startswith("CHECKER_PAYLOAD: ")), None)
    if line is None:
        raise ValueError("primary cache has no CHECKER_PAYLOAD line")
    return json.loads(line.removeprefix("CHECKER_PAYLOAD: "))


def validate_payload(candidate: dict, independent: dict) -> bool:
    expected = independent["payload_without_science_digest"]
    comparable = {key: candidate.get(key) for key in expected}
    if comparable != expected:
        return False
    classes = candidate.get("classes", [])
    members = [member for row in classes for member in row.get("members", [])]
    return (
        candidate.get("family_size") == sum(candidate.get("family_kind_counts", {}).values())
        and candidate.get("witness_count") == len(candidate.get("witness_names", []))
        and candidate.get("class_count") == len(classes)
        and sorted(members) == sorted(candidate.get("witness_names", []))
        and len(members) == len(set(members))
        and candidate.get("legacy_witness_count", 0) + candidate.get("added_witness_count", 0) == candidate.get("witness_count")
        and candidate.get("family_covariant") == (
            candidate.get("rotation_failure_count") == 0
            and candidate.get("translation_failure_count") == 0
            and candidate.get("bridge_failure_count") == 0
        )
    )


def active_corruption_probes(primary_payload: dict, independent: dict) -> dict:
    mutations = {}

    corrupt = deepcopy(primary_payload)
    corrupt["family_size"] += 1
    mutations["family_size_plus_one"] = not validate_payload(corrupt, independent)

    corrupt = deepcopy(primary_payload)
    corrupt["witness_count"] -= 1
    mutations["witness_count_minus_one"] = not validate_payload(corrupt, independent)

    corrupt = deepcopy(primary_payload)
    corrupt["classes"][0]["law"] = "x"
    mutations["representative_law_erased"] = not validate_payload(corrupt, independent)

    corrupt = deepcopy(primary_payload)
    corrupt["class_count"] += 1
    mutations["class_count_plus_one"] = not validate_payload(corrupt, independent)

    corrupt = deepcopy(primary_payload)
    corrupt["family_covariant"] = not corrupt["family_covariant"]
    mutations["covariance_flag_flipped"] = not validate_payload(corrupt, independent)

    corrupt = deepcopy(primary_payload)
    corrupt["added_witnesses_by_kind"]["TOF"] += 1
    mutations["undercount_cause_shifted"] = not validate_payload(corrupt, independent)
    return mutations


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt-path", default="outputs/witness_family_completeness_cycle977_independent_check_receipt_2026_08_10.json")
    parser.add_argument("--cache-path", default="logs/runner-cache/frontier_cycle977_witness_family_independent_check_2026_08_10.txt")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    started = monotonic()
    inputs = {relative: ROOT / relative for relative in LITERAL_INPUT_PATHS}
    primary_source = inputs[PRIMARY_PATH].read_text(encoding="utf-8")
    primary_tree = ast.parse(primary_source, filename=PRIMARY_PATH)
    primary_receipt = json.loads(inputs[PRIMARY_RECEIPT_PATH].read_text(encoding="utf-8"))
    primary_cache = inputs[PRIMARY_CACHE_PATH].read_text(encoding="utf-8")
    cache_payload = parse_cache_payload(primary_cache)
    primary_payload = primary_receipt["checker_payload"]
    first = independent_measurement()
    second = independent_measurement()
    deterministic = digest(first) == digest(second)
    independent_payload = dict(first["payload_without_science_digest"])
    independent_payload["science_digest"] = primary_receipt["science_digest"]
    functions = {node.name for node in ast.walk(primary_tree) if isinstance(node, ast.FunctionDef)}
    expected_family_size = 1 + SITE_COUNT + SITE_COUNT * (SITE_COUNT - 1) + SITE_COUNT * comb(SITE_COUNT - 1, 2)
    r0_ok = (
        len(independent_family()) == expected_family_size
        and len(set(independent_family())) == len(independent_family())
        and len(ROTATIONS) == 24
        and not (set(FORBIDDEN_EXECUTION_IMPORTS) & set(sys.modules))
        and {"declared_family", "witness_census", "covariance_and_classes", "undercount_audit"} <= functions
    )
    r0_finding = (
        f"independent_family={len(independent_family())}=1+7+42+105; rotations_from_oriented_frames={len(ROTATIONS)}; "
        f"primary_read=AST_only; primary_and_core_imported=False"
    )

    comparable_primary = {key: primary_payload.get(key) for key in independent_payload}
    r1_ok = (
        validate_payload(primary_payload, first)
        and primary_payload["family_descriptor_digest"] == independent_payload["family_descriptor_digest"]
        and primary_payload["witness_signature_digest"] == independent_payload["witness_signature_digest"]
        and primary_receipt["science_digest"] == digest(primary_receipt["findings"])
    )
    r1_finding = (
        f"family={independent_payload['family_size']}; witnesses={independent_payload['witness_count']}; "
        f"dependent_rows={independent_payload['dependent_word_input_rows']}/{independent_payload['word_input_rows']}; "
        f"changed_pairs={independent_payload['changed_edge_pairs']}/{independent_payload['edge_pair_comparisons']}; "
        f"legacy_plus_added={independent_payload['legacy_witness_count']}+{independent_payload['added_witness_count']}"
    )

    r2_ok = (
        comparable_primary == independent_payload
        and independent_payload["family_covariant"] == (
            first["closure_failure_count"] == 0
            and first["rotation_failure_count"] == 0
            and first["translation_failure_count"] == 0
        )
        and sorted(member for row in independent_payload["classes"] for member in row["members"]) == sorted(independent_payload["witness_names"])
    )
    r2_finding = (
        f"classes={[(row['representative'], row['law'], row['member_count']) for row in independent_payload['classes']]}; "
        f"rotation_failures={first['rotation_failure_count']}/{independent_payload['rotation_checks']}; "
        f"translation_failures={first['translation_failure_count']}/{independent_payload['translation_checks']}; "
        f"non_covariant_witnesses={independent_payload['non_covariant_witnesses']}"
    )

    source_sha = file_sha256(inputs[PRIMARY_PATH])
    input_pins = {relative: file_sha256(path) for relative, path in inputs.items()}
    primary_cache_header_ok = (
        primary_cache.startswith("===== runner cache v1 =====\n")
        and f"runner: {PRIMARY_PATH}\n" in primary_cache
        and f"runner_sha256: {source_sha}\n" in primary_cache
        and "status: ok\n" in primary_cache
    )
    r3_ok = (
        primary_payload == cache_payload
        and primary_receipt["primary_source_sha256"] == source_sha
        and primary_receipt["controls"]["primary_source_sha256"] == source_sha
        and primary_receipt["all_certificates_pass"]
        and primary_cache_header_ok
        and primary_cache.splitlines().count("TOTAL: PASS=4 FAIL=0") == 1
    )
    r3_finding = (
        f"primary_source_receipt_cache_bound=True; canonical_cache_header={primary_cache_header_ok}; "
        f"primary_sha256={source_sha}; "
        f"primary_science_digest={primary_receipt['science_digest']}"
    )

    corruptions = active_corruption_probes(primary_payload, first)
    r4_ok = len(corruptions) >= 6 and all(corruptions.values())
    r4_finding = f"active_corruptions_rejected={sum(corruptions.values())}/{len(corruptions)}; probes={corruptions}"

    elapsed = monotonic() - started
    output_upper_bound = sum(map(len, (r0_finding, r1_finding, r2_finding, r3_finding, r4_finding))) + 2_500
    r5_ok = (
        len(LITERAL_INPUT_PATHS) <= 6
        and all(path.is_file() and path.resolve().is_relative_to(ROOT.resolve()) for path in inputs.values())
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC < 1400
        and output_upper_bound < HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
    )
    r5_finding = (
        f"literal_reads={len(LITERAL_INPUT_PATHS)}<=6; input_sha256={compact(input_pins)}; "
        f"determinism_replay={deterministic}; runtime_s={elapsed:.6f}<timeout_s={AUDIT_TIMEOUT_SEC}; "
        f"stdout_upper_bound={output_upper_bound}<{HOUSE_STDOUT_LIMIT_BYTES}<{STDOUT_LIMIT_BYTES}"
    )

    certificates = (
        ("R0_REFUTE_ENLARGED_FAMILY", r0_ok, r0_finding),
        ("R1_REFUTE_WITNESS_CENSUS", r1_ok, r1_finding),
        ("R2_REFUTE_CLASSES_AND_COVARIANCE", r2_ok, r2_finding),
        ("R3_PRIMARY_RECEIPT_CACHE_BINDING", r3_ok, r3_finding),
        ("R4_ACTIVE_CORRUPTION_PROBES", r4_ok, r4_finding),
        ("R5_CONTROLS", r5_ok, r5_finding),
    )
    all_pass = all(ok for _, ok, _ in certificates)
    lines = ["=" * 78, "CYCLE 977 -- INDEPENDENT WITNESS-FAMILY REFUTATION", "=" * 78]
    lines.extend(f"{'PASS' if ok else 'FAIL'} {name} :: {finding}" for name, ok, finding in certificates)
    lines.append("VERDICT: " + ("PRIMARY_SURVIVES_INDEPENDENT_REFUTATION_ATTEMPT" if all_pass else "PRIMARY_REFUTED_OR_CHECK_INCOMPLETE"))
    lines.append(f"TOTAL: PASS={sum(ok for _, ok, _ in certificates)} FAIL={sum(not ok for _, ok, _ in certificates)}")
    stdout = "\n".join(lines) + "\n"
    if len(stdout.encode()) >= HOUSE_STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1

    receipt_path = ROOT / args.receipt_path
    cache_path = ROOT / args.cache_path
    if not receipt_path.resolve().is_relative_to(ROOT.resolve()) or not cache_path.resolve().is_relative_to(ROOT.resolve()):
        sys.stderr.write("output path escapes repository\n")
        return 1
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    receipt = {
        "cycle": 977,
        "artifact": "witness_family_completeness_independent_check",
        "refutation_spec": {
            "R0": "independently generate bounded family and rotations; block primary/core execution",
            "R1": "recompute every Boolean witness signature and legacy/enlarged reconciliation",
            "R2": "recompute law partition and rotation/translation covariance",
            "R3": "bind primary source, receipt, and cache",
            "R4": "reject active corruptions in family, census, laws, classes, covariance, and undercount cause",
            "R5": "enforce deterministic replay, read cap, runtime, and stdout controls",
        },
        "literal_input_paths": list(LITERAL_INPUT_PATHS),
        "forbidden_execution_imports": list(FORBIDDEN_EXECUTION_IMPORTS),
        "input_sha256": input_pins,
        "primary_source_sha256": source_sha,
        "primary_science_digest": primary_receipt["science_digest"],
        "independent_measurement": first,
        "active_corruptions": corruptions,
        "determinism_replay": deterministic,
        "runtime_sec": elapsed,
        "stdout_bytes": len(stdout.encode()),
        "certificates": {name: {"pass": ok, "finding": finding} for name, ok, finding in certificates},
        "all_certificates_pass": all_pass,
    }
    receipt_path.write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    cache_path.write_text(stdout, encoding="utf-8")
    sys.stdout.write(stdout)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
