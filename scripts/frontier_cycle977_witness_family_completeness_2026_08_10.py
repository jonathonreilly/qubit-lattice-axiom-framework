#!/usr/bin/env python3
"""Cycle 977: exhaustive one-step witness-family completeness census.

The declared family is every distinct word of length zero or one whose gate
support lies in the target-centred seven-site nearest-neighbour star.  The
landed basis-state semantic substrate exposes X, CNOT, and TOF constructors.
Thus the family is

    1 identity + 7 X + 7*6 ordered CNOT + 7*C(6,2) TOF = 155 words.

TOF controls are an unordered pair because exchanging them gives the same
landed Gate and Boolean action.  No adjacency restriction is imposed inside
the seven-site support cap.  Every word is evaluated on both target bits and
all 2^6 neighbour conditions with the landed Cycle-719 apply_semantic method.

Certificate truth gates construction, exhaustive reconciliation, partition
bookkeeping, and controls only.  It does not require any particular witness
count, class count, or covariance verdict, so null, enlarged, and
non-covariant findings are reported without changing certificate integrity.
"""
from __future__ import annotations

import argparse
import ast
from collections import defaultdict
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from math import comb
from pathlib import Path
import subprocess
import sys
from time import monotonic

AUDIT_TIMEOUT_SEC = 300
HOUSE_STDOUT_LIMIT_BYTES = 6_000
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
EXECUTABLE_SUBSTRATE = AUDIT_INPUT_PATHS[1]
BLOCKLIST_CITED_PRIMARIES = (AUDIT_INPUT_PATHS[0],)
PROVENANCE = {
    "cycle972_runner": (
        "3826925e019c0e1966a9b85110a397db2c61d33f",
        "scripts/frontier_cycle972_covariant_dependence_law_2026_08_09.py",
        "ab497ae52f74bc8e8c6cc6eb5888bfaf9f119f15",
        "ast",
    ),
    "cycle972_note": (
        "3826925e019c0e1966a9b85110a397db2c61d33f",
        "docs/COVARIANT_DEPENDENCE_LAW_CYCLE972_BOUNDED_THEOREM_NOTE_2026-08-09.md",
        "e328562ec0ff3b80acef65c490bb5903cc3e8438",
        "text",
    ),
    "cycle975_runner": (
        "cfe4f1316aa961e19463c50de0d6d89b0dbdb63c",
        "scripts/frontier_cycle975_input_distribution_dependence_law_2026_08_10.py",
        "663029bfe1e937fd95278427cd417f98ea1ca0c6",
        "ast",
    ),
    "cycle975_note": (
        "cfe4f1316aa961e19463c50de0d6d89b0dbdb63c",
        "docs/INPUT_DISTRIBUTION_DEPENDENCE_LAW_CYCLE975_BOUNDED_THEOREM_NOTE_2026-08-10.md",
        "5ccef8dd95178460fa39642a7376d9919b386dcf",
        "text",
    ),
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as CORE

A = CORE.A
CENTER = (0, 0, 0)
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
DIRECTION_NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
DIR_TO_NAME = dict(zip(DIRECTIONS, DIRECTION_NAMES))
DIR_TO_WIRE = {direction: index + 1 for index, direction in enumerate(DIRECTIONS)}
WIRE_TO_OFFSET = (CENTER, *DIRECTIONS)
SITE_COUNT = len(WIRE_TO_OFFSET)
NEIGHBOUR_CONDITIONS = tuple(product((0, 1), repeat=len(DIRECTIONS)))
OTHER_CONTEXTS = tuple(product((0, 1), repeat=len(DIRECTIONS) - 1))
TRANSLATION_GENERATORS = DIRECTIONS
GATE_ALPHABET = ("X", "CNOT", "TOF")
FAMILY_DESCRIPTION = (
    "every distinct length-zero/one word over landed basis-state X, CNOT, "
    "and TOF with all operands inside the target-centred radius-one "
    "seven-site star; no within-star adjacency restriction"
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


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


def determinant(matrix: tuple[tuple[int, int, int], ...]) -> int:
    return dot(matrix[0], cross(matrix[1], matrix[2]))


def mat_vec(matrix: tuple[tuple[int, int, int], ...], vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(dot(row, vector) for row in matrix)


def proper_cubic_rotations() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    matrices = set()
    for axis_order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = tuple(
                tuple(signs[row] * int(column == axis_order[row]) for column in range(3))
                for row in range(3)
            )
            if determinant(rows) == 1:
                matrices.add(rows)
    return tuple(sorted(matrices))


ROTATIONS = proper_cubic_rotations()


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


def declared_family() -> tuple[dict, ...]:
    descriptors = [("I",)]
    descriptors.extend(("X", target) for target in range(SITE_COUNT))
    descriptors.extend(("CNOT", control, target) for control, target in permutations(range(SITE_COUNT), 2))
    for target in range(SITE_COUNT):
        other_sites = tuple(site for site in range(SITE_COUNT) if site != target)
        descriptors.extend(("TOF", controls[0], controls[1], target) for controls in combinations(other_sites, 2))
    return tuple({"name": word_name(descriptor), "descriptor": descriptor} for descriptor in descriptors)


def legacy_family() -> tuple[tuple, ...]:
    descriptors = [("I",)]
    descriptors.extend(("X", target) for target in range(SITE_COUNT))
    descriptors.extend(("CNOT", 0, neighbour) for neighbour in range(1, SITE_COUNT))
    descriptors.extend(("CNOT", neighbour, 0) for neighbour in range(1, SITE_COUNT))
    return tuple(descriptors)


def core_word(descriptor: tuple) -> tuple:
    if descriptor[0] == "I":
        return ()
    if descriptor[0] == "X":
        return (A.x(descriptor[1]),)
    if descriptor[0] == "CNOT":
        return (A.cn(descriptor[1], descriptor[2]),)
    return (A.tof(descriptor[1], descriptor[2], descriptor[3]),)


def basis_state(local_input: int, condition: tuple[int, ...]) -> tuple[int, ...]:
    return (local_input, *condition)


def output_state(descriptor: tuple, local_input: int, condition: tuple[int, ...]) -> tuple[int, ...]:
    return A.apply_semantic(basis_state(local_input, condition), core_word(descriptor))


def output_bit(descriptor: tuple, local_input: int, condition: tuple[int, ...]) -> int:
    return output_state(descriptor, local_input, condition)[0]


def with_edge_bit(index: int, other: tuple[int, ...], bit: int) -> tuple[int, ...]:
    values = []
    source = iter(other)
    for position in range(len(DIRECTIONS)):
        values.append(bit if position == index else next(source))
    return tuple(values)


def law_signature(descriptor: tuple) -> tuple[int, ...]:
    values = []
    for mask in range(1 << SITE_COUNT):
        bits = tuple((mask >> index) & 1 for index in range(SITE_COUNT))
        values.append(output_bit(descriptor, bits[0], bits[1:]))
    return tuple(values)


def anf_formula(signature: tuple[int, ...]) -> str:
    coefficients = list(signature)
    for bit in range(SITE_COUNT):
        for mask in range(1 << SITE_COUNT):
            if mask & (1 << bit):
                coefficients[mask] ^= coefficients[mask ^ (1 << bit)]
    variables = ("x", *(f"n_{name}" for name in DIRECTION_NAMES))
    terms = []
    for mask, coefficient in enumerate(coefficients):
        if not coefficient:
            continue
        factors = [variables[index] for index in range(SITE_COUNT) if mask & (1 << index)]
        terms.append(" AND ".join(factors) if factors else "1")
    return " XOR ".join(terms) if terms else "0"


def rotate_wire(wire: int, rotation: tuple[tuple[int, int, int], ...]) -> int:
    if wire == 0:
        return 0
    return DIR_TO_WIRE[mat_vec(rotation, WIRE_TO_OFFSET[wire])]


def rotate_descriptor(descriptor: tuple, rotation: tuple[tuple[int, int, int], ...]) -> tuple:
    if descriptor[0] == "I":
        return descriptor
    if descriptor[0] == "X":
        return ("X", rotate_wire(descriptor[1], rotation))
    if descriptor[0] == "CNOT":
        return ("CNOT", rotate_wire(descriptor[1], rotation), rotate_wire(descriptor[2], rotation))
    controls = sorted((rotate_wire(descriptor[1], rotation), rotate_wire(descriptor[2], rotation)))
    return ("TOF", controls[0], controls[1], rotate_wire(descriptor[3], rotation))


def rotate_state(state: tuple[int, ...], rotation: tuple[tuple[int, int, int], ...]) -> tuple[int, ...]:
    transported = [0] * SITE_COUNT
    for wire, bit in enumerate(state):
        transported[rotate_wire(wire, rotation)] = bit
    return tuple(transported)


def local_coordinate(wire: int, target: tuple[int, int, int]) -> tuple[int, int, int]:
    return add(target, WIRE_TO_OFFSET[wire])


def global_descriptor(descriptor: tuple, target: tuple[int, int, int]) -> tuple:
    if descriptor[0] == "I":
        return descriptor
    coordinates = tuple(local_coordinate(wire, target) for wire in descriptor[1:])
    return (descriptor[0], *coordinates)


def translate_descriptor(descriptor: tuple, translation: tuple[int, int, int]) -> tuple:
    if descriptor[0] == "I":
        return descriptor
    return (descriptor[0], *(add(site, translation) for site in descriptor[1:]))


def coordinate_state(target: tuple[int, int, int], local_input: int, condition: tuple[int, ...]) -> dict:
    return {
        local_coordinate(wire, target): bit
        for wire, bit in enumerate((local_input, *condition))
    }


def apply_coordinate_semantic(state: dict, descriptor: tuple) -> dict:
    after = dict(state)
    if descriptor[0] == "X":
        after[descriptor[1]] ^= 1
    elif descriptor[0] == "CNOT" and after[descriptor[1]]:
        after[descriptor[2]] ^= 1
    elif descriptor[0] == "TOF" and after[descriptor[1]] and after[descriptor[2]]:
        after[descriptor[3]] ^= 1
    return after


def translate_state(state: dict, translation: tuple[int, int, int]) -> dict:
    return {add(site, translation): bit for site, bit in state.items()}


def witness_census() -> dict:
    rows = []
    changed_atoms = []
    witness_descriptors = []
    signatures = {}
    for word in declared_family():
        descriptor = word["descriptor"]
        word_dependent = False
        word_changed = 0
        word_directions = set()
        for local_input in (0, 1):
            dependent_directions = []
            changed_pairs = 0
            for direction_index, direction_name in enumerate(DIRECTION_NAMES):
                direction_changed = False
                for other in OTHER_CONTEXTS:
                    condition_0 = with_edge_bit(direction_index, other, 0)
                    condition_1 = with_edge_bit(direction_index, other, 1)
                    if output_bit(descriptor, local_input, condition_0) != output_bit(descriptor, local_input, condition_1):
                        direction_changed = True
                        changed_pairs += 1
                        changed_atoms.append((word["name"], local_input, direction_name, other))
                if direction_changed:
                    dependent_directions.append(direction_name)
                    word_directions.add(direction_name)
            dependent = bool(dependent_directions)
            word_dependent |= dependent
            word_changed += changed_pairs
            rows.append({
                "word_name": word["name"],
                "fixed_target_input": local_input,
                "dependent_neighbour_bits": dependent_directions,
                "changed_edge_pairs": changed_pairs,
                "edge_pair_comparisons": len(DIRECTIONS) * len(OTHER_CONTEXTS),
                "dependent": dependent,
            })
        if word_dependent:
            witness_descriptors.append(descriptor)
            signature = law_signature(descriptor)
            signatures[descriptor] = signature
    witnesses = []
    for descriptor in witness_descriptors:
        witnesses.append({
            "word_name": word_name(descriptor),
            "dependent_neighbour_bits": sorted({row["dependent_neighbour_bits"][index]
                for row in rows if row["word_name"] == word_name(descriptor)
                for index in range(len(row["dependent_neighbour_bits"]))}),
            "induced_target_law_anf": anf_formula(signatures[descriptor]),
            "law_signature_sha256": digest(signatures[descriptor]),
            "changed_edge_pairs": sum(row["changed_edge_pairs"] for row in rows if row["word_name"] == word_name(descriptor)),
        })
    return {
        "conditioned_configurations": len(declared_family()) * 2 * len(NEIGHBOUR_CONDITIONS),
        "word_input_rows": len(rows),
        "dependent_word_input_rows": sum(row["dependent"] for row in rows),
        "edge_pair_comparisons": len(rows) * len(DIRECTIONS) * len(OTHER_CONTEXTS),
        "changed_edge_pairs": len(changed_atoms),
        "witness_word_count": len(witnesses),
        "witness_words": witnesses,
        "witness_descriptors": witness_descriptors,
        "rows": rows,
        "changed_atoms_digest": digest(changed_atoms),
        "witness_signature_digest": digest([(word_name(d), signatures[d]) for d in witness_descriptors]),
    }


def covariance_and_classes(census: dict) -> dict:
    family = declared_family()
    descriptors = {word["descriptor"] for word in family}
    names = {word["descriptor"]: word["name"] for word in family}
    witness_descriptors = tuple(census["witness_descriptors"])
    witness_set = set(witness_descriptors)

    closure_failures = []
    rotation_failures = []
    rotation_checks = 0
    for rotation in ROTATIONS:
        for word in family:
            descriptor = word["descriptor"]
            transported = rotate_descriptor(descriptor, rotation)
            if transported not in descriptors:
                closure_failures.append((word["name"], transported))
                continue
            for local_input in (0, 1):
                for condition in NEIGHBOUR_CONDITIONS:
                    rotation_checks += 1
                    before = basis_state(local_input, condition)
                    left = rotate_state(A.apply_semantic(before, core_word(descriptor)), rotation)
                    right = A.apply_semantic(rotate_state(before, rotation), core_word(transported))
                    if left != right:
                        rotation_failures.append((word["name"], names[transported], local_input, condition, left, right))

    bridge_failures = []
    bridge_checks = 0
    for word in family:
        descriptor = word["descriptor"]
        global_word = global_descriptor(descriptor, CENTER)
        for local_input in (0, 1):
            for condition in NEIGHBOUR_CONDITIONS:
                bridge_checks += 1
                core_after = output_state(descriptor, local_input, condition)
                coordinate_after = apply_coordinate_semantic(
                    coordinate_state(CENTER, local_input, condition), global_word
                )
                reencoded = tuple(coordinate_after[local_coordinate(wire, CENTER)] for wire in range(SITE_COUNT))
                if core_after != reencoded:
                    bridge_failures.append((word["name"], local_input, condition, core_after, reencoded))

    translation_failures = []
    translation_checks = 0
    for translation in TRANSLATION_GENERATORS:
        for word in family:
            descriptor = word["descriptor"]
            global_word = global_descriptor(descriptor, CENTER)
            transported_word = translate_descriptor(global_word, translation)
            if transported_word != global_descriptor(descriptor, translation):
                translation_failures.append((word["name"], translation, "word_transport"))
            for local_input in (0, 1):
                for condition in NEIGHBOUR_CONDITIONS:
                    translation_checks += 1
                    before = coordinate_state(CENTER, local_input, condition)
                    left = translate_state(apply_coordinate_semantic(before, global_word), translation)
                    right = apply_coordinate_semantic(translate_state(before, translation), transported_word)
                    if left != right:
                        translation_failures.append((word["name"], translation, local_input, condition))

    canonical_law_keys = {}
    for descriptor in witness_descriptors:
        orbit_signatures = tuple(sorted(law_signature(rotate_descriptor(descriptor, rotation)) for rotation in ROTATIONS))
        canonical_law_keys[descriptor] = orbit_signatures[0]
    grouped = defaultdict(list)
    for descriptor, key in canonical_law_keys.items():
        grouped[key].append(descriptor)

    failure_names = {
        failure[0]
        for failure in closure_failures + rotation_failures + bridge_failures + translation_failures
    }
    classes = []
    covered = []
    for class_index, members in enumerate(sorted(grouped.values(), key=lambda group: min(word_name(item) for item in group)), start=1):
        members = sorted(members, key=word_name)
        covered.extend(members)
        representative = members[0]
        member_names = [word_name(item) for item in members]
        rotation_orbit = {rotate_descriptor(representative, rotation) for rotation in ROTATIONS}
        stabilizer = sum(rotate_descriptor(representative, rotation) == representative for rotation in ROTATIONS)
        class_failure_names = sorted(set(member_names) & failure_names)
        classes.append({
            "class_id": f"L{class_index}",
            "representative_word": word_name(representative),
            "representative_induced_target_law_anf": anf_formula(law_signature(representative)),
            "member_count": len(members),
            "member_words": member_names,
            "local_rotation_orbit_size": len(rotation_orbit & witness_set),
            "proper_rotation_stabilizer_size": stabilizer,
            "rotation_semantic_comparisons": len(members) * len(ROTATIONS) * 2 * len(NEIGHBOUR_CONDITIONS),
            "translation_semantic_comparisons": len(members) * len(TRANSLATION_GENERATORS) * 2 * len(NEIGHBOUR_CONDITIONS),
            "failure_words": class_failure_names,
            "covariant": not class_failure_names,
        })

    return {
        "realized_group": "Z^3 semidirect product O+_cubic",
        "proper_rotation_count": len(ROTATIONS),
        "rotation_group_closed": all(
            tuple(tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3)) for i in range(3)) in set(ROTATIONS)
            for left in ROTATIONS for right in ROTATIONS
        ),
        "rotation_family_closure_failures": closure_failures,
        "rotation_semantic_comparisons": rotation_checks,
        "rotation_semantic_failures": rotation_failures,
        "landed_coordinate_bridge_comparisons": bridge_checks,
        "landed_coordinate_bridge_failures": bridge_failures,
        "translation_semantic_comparisons": translation_checks,
        "translation_semantic_failures": translation_failures,
        "induced_law_class_count": len(classes),
        "induced_law_classes": classes,
        "class_partition_descriptors": covered,
        "non_covariant_witnesses": sorted(set(names[d] for d in witness_descriptors) & failure_names),
        "family_covariant": not (closure_failures or rotation_failures or bridge_failures or translation_failures),
    }


def undercount_audit(census: dict) -> dict:
    legacy = set(legacy_family())
    enlarged = {word["descriptor"] for word in declared_family()}
    witnesses = set(census["witness_descriptors"])
    added = enlarged - legacy
    added_by_kind = {kind: sum(descriptor[0] == kind for descriptor in added) for kind in GATE_ALPHABET}
    added_witnesses_by_kind = {kind: sum(descriptor[0] == kind for descriptor in added & witnesses) for kind in GATE_ALPHABET}
    return {
        "legacy_family_size": len(legacy),
        "legacy_is_subset": legacy <= enlarged,
        "legacy_witness_count_in_enlarged_semantics": len(legacy & witnesses),
        "enlarged_family_size": len(enlarged),
        "added_word_count": len(added),
        "added_words_by_gate_kind": added_by_kind,
        "added_witness_count": len(added & witnesses),
        "added_witnesses_by_gate_kind": added_witnesses_by_kind,
        "added_witness_words": sorted(word_name(descriptor) for descriptor in added & witnesses),
        "exact_reason": (
            "the 20-word family was exhaustive only after imposing a two-site arity restriction and centre-edge CNOT restriction; "
            "the enlarged family adds every TOF and every off-centre CNOT supported in the star.  Any added witnesses are measured "
            "separately by gate kind, so the census does not assume which exclusion mattered"
        ),
    }


def provenance_controls() -> dict:
    observations = {}
    for label, (commit, path, expected_blob, mode) in PROVENANCE.items():
        spec = f"{commit}:{path}"
        observed_blob = subprocess.check_output(("git", "rev-parse", spec), cwd=ROOT, text=True).strip()
        body = subprocess.check_output(("git", "show", spec), cwd=ROOT)
        row = {
            "commit": commit,
            "path": path,
            "expected_blob": expected_blob,
            "observed_blob": observed_blob,
            "read_mode": "AST only; never executed" if mode == "ast" else "text only",
        }
        if mode == "ast":
            tree = ast.parse(body.decode(), filename=spec)
            functions = {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}
            row["declares_family"] = "declared_family" in functions
            row["declares_census"] = bool({"state_resolved_census", "symbolic_marginal_census"} & functions)
        else:
            text = body.decode()
            row["bounded_scope_present"] = "bounded" in text.lower()
            row["witness_context_present"] = "witness" in text.lower() or "dependence" in text.lower()
        observations[label] = row
    return observations


def input_controls() -> dict:
    pins = {}
    all_exist = True
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        all_exist &= path.is_file() and path.resolve().is_relative_to(ROOT.resolve())
        pins[relative] = sha256(path.read_bytes()).hexdigest() if path.is_file() else None
    axiom = (ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    probes = (A.x(0), A.cn(0, 1), A.tof(0, 1, 2))
    provenance = provenance_controls()
    return {
        "literal_source_read_count": len(AUDIT_INPUT_PATHS) + len(PROVENANCE),
        "literal_audit_input_paths": list(AUDIT_INPUT_PATHS),
        "sha256": pins,
        "primary_source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "all_inputs_exist_worktree_relative": all_exist,
        "blocklist_cited_primaries": list(BLOCKLIST_CITED_PRIMARIES),
        "blocklist_text_only": all(not path.endswith(".py") for path in BLOCKLIST_CITED_PRIMARIES),
        "executable_substrate": EXECUTABLE_SUBSTRATE,
        "substrate_gate_probe": [(gate.kind, list(gate.wires)) for gate in probes],
        "substrate_gate_alphabet_matches": tuple(gate.kind for gate in probes) == GATE_ALPHABET,
        "axiom_covariance_needle_matches": "covariant under lattice\ntranslations and proper cubic rotations" in axiom,
        "axiom_distribution_needle_matches": "probability distribution over the possibilities is\ndetermined by, and varies with, the nearest-neighbor conditions" in axiom,
        "text_ast_provenance": provenance,
        "provenance_pins_match": all(row["expected_blob"] == row["observed_blob"] for row in provenance.values()),
        "provenance_never_executed": all("never executed" in row["read_mode"] or row["read_mode"] == "text only" for row in provenance.values()),
    }


def run_science() -> dict:
    census = witness_census()
    covariance = covariance_and_classes(census)
    undercount = undercount_audit(census)
    census = {key: value for key, value in census.items() if key != "witness_descriptors"}
    covariance = {key: value for key, value in covariance.items() if key != "class_partition_descriptors"}
    return {"census": census, "class_structure": covariance, "undercount": undercount}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt-path", default="outputs/witness_family_completeness_cycle977_receipt_2026_08_10.json")
    parser.add_argument("--cache-path", default="logs/runner-cache/frontier_cycle977_witness_family_completeness_2026_08_10.txt")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    started = monotonic()
    raw_census = witness_census()
    raw_covariance = covariance_and_classes(raw_census)
    undercount = undercount_audit(raw_census)
    first = {
        "census": {key: value for key, value in raw_census.items() if key != "witness_descriptors"},
        "class_structure": {key: value for key, value in raw_covariance.items() if key != "class_partition_descriptors"},
        "undercount": undercount,
    }
    second = run_science()
    deterministic = digest(first) == digest(second)
    controls = input_controls()
    census = first["census"]
    covariance = first["class_structure"]
    family = declared_family()

    expected_family_size = 1 + SITE_COUNT + SITE_COUNT * (SITE_COUNT - 1) + SITE_COUNT * comb(SITE_COUNT - 1, 2)
    kind_counts = {
        "identity": sum(row["descriptor"][0] == "I" for row in family),
        "X": sum(row["descriptor"][0] == "X" for row in family),
        "CNOT": sum(row["descriptor"][0] == "CNOT" for row in family),
        "TOF": sum(row["descriptor"][0] == "TOF" for row in family),
    }
    a_ok = (
        len(family) == expected_family_size
        and len({row["descriptor"] for row in family}) == len(family)
        and len({row["name"] for row in family}) == len(family)
        and kind_counts["identity"] + kind_counts["X"] + kind_counts["CNOT"] + kind_counts["TOF"] == len(family)
        and all(len(set(row["descriptor"][1:])) == len(row["descriptor"][1:]) for row in family if row["descriptor"][0] != "I")
    )
    a_finding = (
        f"word_length_cap=1; spatial_support=target-centred_radius-one_7-site_star; support_size_cap=3; "
        f"gate_alphabet={list(GATE_ALPHABET)}; family_words={len(family)}="
        f"{kind_counts['identity']}I+{kind_counts['X']}X+{kind_counts['CNOT']}CNOT+{kind_counts['TOF']}TOF"
    )

    witness_names = [row["word_name"] for row in census["witness_words"]]
    b_ok = (
        census["conditioned_configurations"] == len(family) * 2 * len(NEIGHBOUR_CONDITIONS)
        and census["word_input_rows"] == len(family) * 2
        and census["dependent_word_input_rows"] == sum(row["dependent"] for row in census["rows"])
        and census["edge_pair_comparisons"] == len(census["rows"]) * len(DIRECTIONS) * len(OTHER_CONTEXTS)
        and census["changed_edge_pairs"] == sum(row["changed_edge_pairs"] for row in census["rows"])
        and census["witness_word_count"] == len(census["witness_words"]) == len(set(witness_names))
        and 0 <= census["changed_edge_pairs"] <= census["edge_pair_comparisons"]
        and 0 <= census["witness_word_count"] <= len(family)
    )
    b_finding = (
        f"witness_words={census['witness_word_count']}/{len(family)}; dependent_word_input_rows="
        f"{census['dependent_word_input_rows']}/{census['word_input_rows']}; changed_edge_pairs="
        f"{census['changed_edge_pairs']}/{census['edge_pair_comparisons']}; conditioned_configurations="
        f"{census['conditioned_configurations']}; witnesses={witness_names}"
    )

    classes = covariance["induced_law_classes"]
    class_members = [name for row in classes for name in row["member_words"]]
    covariance_failure_count = (
        len(covariance["rotation_family_closure_failures"])
        + len(covariance["rotation_semantic_failures"])
        + len(covariance["landed_coordinate_bridge_failures"])
        + len(covariance["translation_semantic_failures"])
    )
    c_ok = (
        covariance["proper_rotation_count"] == len(set(ROTATIONS))
        and all(determinant(rotation) == 1 for rotation in ROTATIONS)
        and covariance["rotation_group_closed"]
        and covariance["rotation_semantic_comparisons"] == len(ROTATIONS) * len(family) * 2 * len(NEIGHBOUR_CONDITIONS)
        and covariance["landed_coordinate_bridge_comparisons"] == len(family) * 2 * len(NEIGHBOUR_CONDITIONS)
        and covariance["translation_semantic_comparisons"] == len(TRANSLATION_GENERATORS) * len(family) * 2 * len(NEIGHBOUR_CONDITIONS)
        and covariance["induced_law_class_count"] == len(classes)
        and sorted(class_members) == sorted(witness_names)
        and len(class_members) == len(set(class_members))
        and covariance["family_covariant"] == (covariance_failure_count == 0)
        and sorted(covariance["non_covariant_witnesses"]) == sorted({name for row in classes for name in row["failure_words"]})
        and all(row["covariant"] == (not row["failure_words"]) for row in classes)
    )
    c_finding = (
        f"induced_law_classes={len(classes)}; representatives="
        f"{[(row['representative_word'], row['representative_induced_target_law_anf'], row['member_count']) for row in classes]}; "
        f"rotation_checks={covariance['rotation_semantic_comparisons']}; translation_checks="
        f"{covariance['translation_semantic_comparisons']}; bridge_checks={covariance['landed_coordinate_bridge_comparisons']}; "
        f"covariance_verdict={'COVARIANT' if covariance['family_covariant'] else 'NON_COVARIANT'}; "
        f"non_covariant_witnesses={covariance['non_covariant_witnesses']}"
    )

    elapsed = monotonic() - started
    provenance = controls["text_ast_provenance"]
    output_upper_bound = sum(map(len, (a_finding, b_finding, c_finding))) + 3_000
    d_ok = (
        undercount["legacy_is_subset"]
        and undercount["legacy_family_size"] + undercount["added_word_count"] == undercount["enlarged_family_size"]
        and undercount["legacy_witness_count_in_enlarged_semantics"] + undercount["added_witness_count"] == census["witness_word_count"]
        and sum(undercount["added_words_by_gate_kind"].values()) == undercount["added_word_count"]
        and sum(undercount["added_witnesses_by_gate_kind"].values()) == undercount["added_witness_count"]
        and controls["literal_source_read_count"] <= 6
        and controls["all_inputs_exist_worktree_relative"]
        and controls["blocklist_text_only"]
        and controls["substrate_gate_alphabet_matches"]
        and controls["axiom_covariance_needle_matches"]
        and controls["axiom_distribution_needle_matches"]
        and controls["provenance_pins_match"]
        and controls["provenance_never_executed"]
        and all(row.get("declares_family", True) and row.get("declares_census", True) for row in provenance.values())
        and all(row.get("bounded_scope_present", True) and row.get("witness_context_present", True) for row in provenance.values())
        and deterministic
        and all(controls["sha256"].values())
        and elapsed < AUDIT_TIMEOUT_SEC < 1400
        and output_upper_bound < HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
    )
    d_finding = (
        f"legacy={undercount['legacy_witness_count_in_enlarged_semantics']}/{undercount['legacy_family_size']}; "
        f"added={undercount['added_witness_count']}/{undercount['added_word_count']}; added_words_by_kind="
        f"{undercount['added_words_by_gate_kind']}; added_witnesses_by_kind={undercount['added_witnesses_by_gate_kind']}; "
        f"source_reads={controls['literal_source_read_count']}<=6; sha_pins={compact(controls['sha256'])}; "
        f"provenance_pins_match={controls['provenance_pins_match']}; determinism_replay={deterministic}; "
        f"runtime_s={elapsed:.6f}<timeout_s={AUDIT_TIMEOUT_SEC}; stdout_upper_bound={output_upper_bound}<"
        f"{HOUSE_STDOUT_LIMIT_BYTES}<{STDOUT_LIMIT_BYTES}"
    )

    certificates = (
        ("A_ENLARGED_FAMILY", a_ok, a_finding),
        ("B_WITNESS_CENSUS", b_ok, b_finding),
        ("C_CLASS_STRUCTURE", c_ok, c_finding),
        ("D_CONTROLS", d_ok, d_finding),
    )
    all_pass = all(ok for _, ok, _ in certificates)
    checker_payload = {
        "family_size": len(family),
        "family_kind_counts": kind_counts,
        "family_descriptor_digest": digest([row["descriptor"] for row in family]),
        "conditioned_configurations": census["conditioned_configurations"],
        "witness_count": census["witness_word_count"],
        "witness_names": witness_names,
        "dependent_word_input_rows": census["dependent_word_input_rows"],
        "word_input_rows": census["word_input_rows"],
        "changed_edge_pairs": census["changed_edge_pairs"],
        "edge_pair_comparisons": census["edge_pair_comparisons"],
        "witness_signature_digest": census["witness_signature_digest"],
        "class_count": len(classes),
        "classes": [{
            "representative": row["representative_word"],
            "law": row["representative_induced_target_law_anf"],
            "member_count": row["member_count"],
            "members": row["member_words"],
            "covariant": row["covariant"],
        } for row in classes],
        "rotation_checks": covariance["rotation_semantic_comparisons"],
        "rotation_failure_count": len(covariance["rotation_semantic_failures"]),
        "translation_checks": covariance["translation_semantic_comparisons"],
        "translation_failure_count": len(covariance["translation_semantic_failures"]),
        "bridge_checks": covariance["landed_coordinate_bridge_comparisons"],
        "bridge_failure_count": len(covariance["landed_coordinate_bridge_failures"]),
        "family_covariant": covariance["family_covariant"],
        "non_covariant_witnesses": covariance["non_covariant_witnesses"],
        "legacy_witness_count": undercount["legacy_witness_count_in_enlarged_semantics"],
        "added_witness_count": undercount["added_witness_count"],
        "added_witnesses_by_kind": undercount["added_witnesses_by_gate_kind"],
        "science_digest": digest(first),
    }
    lines = ["=" * 78, "CYCLE 977 -- WITNESS-FAMILY COMPLETENESS", "=" * 78]
    lines.extend(f"{'PASS' if ok else 'FAIL'} {name} :: {finding}" for name, ok, finding in certificates)
    lines.append("CHECKER_PAYLOAD: " + compact(checker_payload))
    if not all_pass:
        verdict = "ENLARGED_CENSUS_INCOMPLETE"
    elif covariance["non_covariant_witnesses"]:
        verdict = "NON_COVARIANT_ENLARGED_WITNESS_FOUND"
    elif undercount["added_witness_count"]:
        verdict = "LEGACY_FAMILY_UNDERCOUNTED_WITNESSES"
    else:
        verdict = "LEGACY_WITNESS_COUNT_COMPLETE_AT_ENLARGED_SCOPE"
    lines.append("VERDICT: " + verdict)
    lines.append(f"TOTAL: PASS={sum(ok for _, ok, _ in certificates)} FAIL={sum(not ok for _, ok, _ in certificates)}")
    stdout = "\n".join(lines) + "\n"
    if len(stdout.encode()) >= HOUSE_STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1

    receipt_path = ROOT / args.receipt_path
    if not receipt_path.resolve().is_relative_to(ROOT.resolve()):
        sys.stderr.write("output path escapes repository\n")
        return 1
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "cycle": 977,
        "artifact": "witness_family_completeness",
        "claim_type": "bounded_theorem",
        "actual_current_surface_status": "bounded-support",
        "trace_class": "direct_blocker_closure",
        "reachability_to_target": "closes",
        "conditional_surface_status": "exact on the declared radius-one, word-length-at-most-one landed basis-state gate family",
        "hypothetical_axiom_status": None,
        "admitted_observation_status": None,
        "proposal_allowed": False,
        "proposal_allowed_reason": "finite basis-state and one-step support cap; not the full continuous M_2(C) distribution law",
        "audit_required_before_effective_retained": True,
        "bare_retained_allowed": False,
        "family_horizon": {
            "word_length_cap": 1,
            "spatial_horizon": "target-centred radius-one seven-site star",
            "support_size_cap": 3,
            "within_star_adjacency_restriction": False,
            "target_input_menu": [0, 1],
            "neighbour_condition_horizon": "all 2^6 basis-bit conditions",
            "gate_alphabet": list(GATE_ALPHABET),
            "family_description": FAMILY_DESCRIPTION,
            "family_size": len(family),
            "excluded": ["words of length >=2", "support outside the seven-site star", "continuous M_2(C) distributions"],
        },
        "findings": first,
        "controls": controls,
        "primary_source_sha256": controls["primary_source_sha256"],
        "determinism_replay": deterministic,
        "science_digest": digest(first),
        "runtime_sec": elapsed,
        "stdout_bytes": len(stdout.encode()),
        "certificates": {name: {"pass": ok, "finding": finding} for name, ok, finding in certificates},
        "all_certificates_pass": all_pass,
        "checker_payload": checker_payload,
    }
    receipt_path.write_text(json.dumps(report, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    cache_path = ROOT / args.cache_path
    if not cache_path.resolve().is_relative_to(ROOT.resolve()):
        sys.stderr.write("cache path escapes repository\n")
        return 1
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(stdout, encoding="utf-8")
    sys.stdout.write(stdout)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
