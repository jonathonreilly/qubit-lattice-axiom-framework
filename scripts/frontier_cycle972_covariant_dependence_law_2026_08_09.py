#!/usr/bin/env python3
"""Cycle 972: covariant neighbour-dependence law in a bounded landed family.

The declared finite family at a target site ``a`` is every distinct word of
length zero or one on the seven-site nearest-neighbour star
``{a, a +/- e_x, a +/- e_y, a +/- e_z}`` made from the landed classical-basis
gate kinds identity, X, and oriented CNOT.  It has exactly

    1 identity + 7 X + 12 oriented centre-neighbour CNOT = 20 words.

For every word, both fixed target inputs, and all 2^6 neighbour conditions,
the runner applies the real Cycle-719 semantic substrate.  It then checks the
transported data under the 24 proper signed-permutation rotations and under
the six unit translation generators.  Translation checks use a coordinate
state dictionary and perform actual state mutation.

Certificate truth values gate enumeration, reconciliation, provenance, and
control integrity only.  They do not require a nonzero census, covariance, a
particular orbit count, or marginal independence.  A null or non-covariant
finding therefore passes when it is consistently measured and reported.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000
HOUSE_STDOUT_LIMIT_BYTES = 6_000
AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
BLOCKLIST_CITED_PRIMARIES = (AUDIT_INPUT_PATHS[0],)
EXECUTABLE_SUBSTRATE = AUDIT_INPUT_PATHS[1]
PROVENANCE_COMMIT = "6fd0de0a288d212a4a6ce3fdd4dc9019f30dbbad"
PROVENANCE_OBJECTS = {
    "runner": (
        "scripts/frontier_cycle970_inter_site_gate_2026_08_09.py",
        "4670bcb9d83cfc039f1336398c6a4aa4af014f7c",
    ),
    "note": (
        "docs/INTER_SITE_GATE_CYCLE970_BOUNDED_THEOREM_NOTE_2026-08-09.md",
        "f7b788d8076e7864bc5dbcbb33cb9e49554e494a",
    ),
}

import ast
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic

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
TRANSLATION_GENERATORS = DIRECTIONS
NEIGHBOUR_CONDITIONS = tuple(product((0, 1), repeat=len(DIRECTIONS)))
OTHER_CONTEXTS = tuple(product((0, 1), repeat=len(DIRECTIONS) - 1))

FAMILY_DESCRIPTION = (
    "all 20 distinct length-zero/one words on a target-centred seven-site "
    "nearest-neighbour star: identity; X on each of seven sites; and CNOT "
    "in both orientations on each of six centre-neighbour edges"
)
LAW_FORMULA = "for W_d=CNOT(a+d->a), target output y=x XOR n_d"


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a + b for a, b in zip(left, right))


def cross(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def dot(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(a * b for a, b in zip(left, right))


def mat_vec(matrix: tuple[tuple[int, int, int], ...], vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(dot(row, vector) for row in matrix)


def determinant(matrix: tuple[tuple[int, int, int], ...]) -> int:
    return dot(matrix[0], cross(matrix[1], matrix[2]))


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


def direction_name(direction: tuple[int, int, int]) -> str:
    return DIR_TO_NAME[direction]


def declared_family() -> tuple[dict, ...]:
    rows = [{"name": "I", "descriptor": ("I",)}]
    rows.append({"name": "X(C)", "descriptor": ("X", "C")})
    rows.extend(
        {"name": f"X({direction_name(d)})", "descriptor": ("X", d)}
        for d in DIRECTIONS
    )
    rows.extend(
        {
            "name": f"CNOT(C->{direction_name(d)})",
            "descriptor": ("CNOT", "C", d),
        }
        for d in DIRECTIONS
    )
    rows.extend(
        {
            "name": f"CNOT({direction_name(d)}->C)",
            "descriptor": ("CNOT", d, "C"),
        }
        for d in DIRECTIONS
    )
    return tuple(rows)


def site_wire(site: str | tuple[int, int, int]) -> int:
    return 0 if site == "C" else DIR_TO_WIRE[site]


def core_word(descriptor: tuple) -> tuple:
    if descriptor[0] == "I":
        return ()
    if descriptor[0] == "X":
        return (A.x(site_wire(descriptor[1])),)
    return (A.cn(site_wire(descriptor[1]), site_wire(descriptor[2])),)


def basis_state(local_input: int, condition: tuple[int, ...]) -> tuple[int, ...]:
    return (local_input, *condition)


def point_distribution(descriptor: tuple, local_input: int, condition: tuple[int, ...]) -> tuple[int, int]:
    before = basis_state(local_input, condition)
    after = A.apply_semantic(before, core_word(descriptor))
    outcome = after[0]
    return (int(outcome == 0), int(outcome == 1))


def with_edge_bit(direction_index: int, other: tuple[int, ...], bit: int) -> tuple[int, ...]:
    values = []
    other_iter = iter(other)
    for index in range(len(DIRECTIONS)):
        values.append(bit if index == direction_index else next(other_iter))
    return tuple(values)


def state_resolved_census() -> dict:
    rows = []
    all_changed_pairs = []
    witness_words = []
    all_xor_failures = []
    all_control_preservation_failures = []
    for word in declared_family():
        descriptor = word["descriptor"]
        word_dependencies = set()
        word_rows = []
        for local_input in (0, 1):
            dependencies = []
            changed_pair_count = 0
            for direction_index, direction in enumerate(DIRECTIONS):
                direction_changed = False
                for other in OTHER_CONTEXTS:
                    condition_0 = with_edge_bit(direction_index, other, 0)
                    condition_1 = with_edge_bit(direction_index, other, 1)
                    distribution_0 = point_distribution(descriptor, local_input, condition_0)
                    distribution_1 = point_distribution(descriptor, local_input, condition_1)
                    changed = distribution_0 != distribution_1
                    if changed:
                        direction_changed = True
                        changed_pair_count += 1
                        all_changed_pairs.append((
                            word["name"], local_input, direction_name(direction),
                            condition_0, condition_1, distribution_0, distribution_1,
                        ))
                if direction_changed:
                    dependencies.append(direction_name(direction))
                    word_dependencies.add(direction)
            word_rows.append({
                "word_name": word["name"],
                "local_input": local_input,
                "dependent_neighbour_bits": dependencies,
                "edge_pair_comparisons": len(DIRECTIONS) * len(OTHER_CONTEXTS),
                "changed_edge_pairs": changed_pair_count,
                "depends_on_neighbour_condition": bool(dependencies),
            })
            rows.append(word_rows[-1])
        if word_dependencies:
            incoming_direction = descriptor[1] if descriptor[:1] == ("CNOT",) and descriptor[2] == "C" else None
            law_comparisons = 0
            xor_failures = []
            control_preservation_failures = []
            for local_input in (0, 1):
                for condition in NEIGHBOUR_CONDITIONS:
                    law_comparisons += 1
                    before = basis_state(local_input, condition)
                    after = A.apply_semantic(before, core_word(descriptor))
                    control_wire = DIR_TO_WIRE[incoming_direction]
                    expected_target = local_input ^ condition[DIRECTIONS.index(incoming_direction)]
                    if after[0] != expected_target:
                        xor_failures.append((word["name"], local_input, condition, after[0], expected_target))
                    if after[control_wire] != before[control_wire]:
                        control_preservation_failures.append((
                            word["name"], local_input, condition,
                            before[control_wire], after[control_wire],
                        ))
            all_xor_failures.extend(xor_failures)
            all_control_preservation_failures.extend(control_preservation_failures)
            canonical_other = (0,) * (len(DIRECTIONS) - 1)
            direction_index = DIRECTIONS.index(incoming_direction) if incoming_direction is not None else 0
            pair_templates = []
            for local_input in (0, 1):
                condition_0 = with_edge_bit(direction_index, canonical_other, 0)
                condition_1 = with_edge_bit(direction_index, canonical_other, 1)
                before_0 = basis_state(local_input, condition_0)
                before_1 = basis_state(local_input, condition_1)
                after_0 = A.apply_semantic(before_0, core_word(descriptor))
                after_1 = A.apply_semantic(before_1, core_word(descriptor))
                pair_templates.append({
                    "fixed_target_input": local_input,
                    "other_five_neighbour_bits": "arbitrary",
                    "replicated_other_contexts": len(OTHER_CONTEXTS),
                    "distribution_n_d_0": list(point_distribution(descriptor, local_input, condition_0)),
                    "distribution_n_d_1": list(point_distribution(descriptor, local_input, condition_1)),
                    "target_neighbour_input_pair": [[local_input, 0], [local_input, 1]],
                    "target_neighbour_output_pair": [
                        [after_0[0], after_0[DIR_TO_WIRE[incoming_direction]]],
                        [after_1[0], after_1[DIR_TO_WIRE[incoming_direction]]],
                    ],
                    "target_state_mutates_between_branches": after_0[0] != after_1[0],
                })
            witness_words.append({
                "word_name": word["name"],
                "reads_neighbour_bit": direction_name(incoming_direction),
                "target_coordinate_moved": "a",
                "induced_target_map": "y=x XOR n_d",
                "separated_pairs": pair_templates,
                "changed_edge_pairs": sum(row["changed_edge_pairs"] for row in word_rows),
                "law_truth_table_comparisons": law_comparisons,
                "xor_law_failures": xor_failures,
                "control_preservation_failures": control_preservation_failures,
            })
    changed_rows = sum(row["depends_on_neighbour_condition"] for row in rows)
    changed_pairs = len(all_changed_pairs)
    return {
        "family": FAMILY_DESCRIPTION,
        "family_words": len(declared_family()),
        "neighbour_condition_count": len(NEIGHBOUR_CONDITIONS),
        "word_local_input_rows": len(rows),
        "dependent_word_local_input_rows": changed_rows,
        "conditioned_configurations": len(rows) * len(NEIGHBOUR_CONDITIONS),
        "conditioned_configurations_in_dependent_rows": changed_rows * len(NEIGHBOUR_CONDITIONS),
        "edge_pair_comparisons": len(rows) * len(DIRECTIONS) * len(OTHER_CONTEXTS),
        "changed_edge_pair_comparisons": changed_pairs,
        "witness_word_count": len(witness_words),
        "witness_words": witness_words,
        "law_truth_table_comparisons": sum(row["law_truth_table_comparisons"] for row in witness_words),
        "xor_law_failures": all_xor_failures,
        "control_preservation_failures": all_control_preservation_failures,
        "xor_law_holds": not all_xor_failures,
        "controls_preserved": not all_control_preservation_failures,
        "rows": rows,
        "changed_edge_pairs_digest": digest(all_changed_pairs),
    }


def uniform_target_input_census() -> dict:
    rows = []
    all_changed_pairs = []
    for word in declared_family():
        descriptor = word["descriptor"]
        distributions = {}
        for condition in NEIGHBOUR_CONDITIONS:
            distributions[condition] = tuple(
                sum(Fraction(point_distribution(descriptor, x, condition)[y], 2) for x in (0, 1))
                for y in (0, 1)
            )
        dependencies = []
        for direction_index, direction in enumerate(DIRECTIONS):
            direction_changed = False
            for other in OTHER_CONTEXTS:
                condition_0 = with_edge_bit(direction_index, other, 0)
                condition_1 = with_edge_bit(direction_index, other, 1)
                if distributions[condition_0] != distributions[condition_1]:
                    direction_changed = True
                    all_changed_pairs.append((
                        word["name"], direction_name(direction), condition_0,
                        condition_1, distributions[condition_0], distributions[condition_1],
                    ))
            if direction_changed:
                dependencies.append(direction_name(direction))
        rows.append({
            "word_name": word["name"],
            "dependent_neighbour_bits": dependencies,
            "breaks_marginal_independence": bool(dependencies),
            "distinct_marginals": sorted({tuple(str(v) for v in value) for value in distributions.values()}),
        })
    changed_rows = sum(row["breaks_marginal_independence"] for row in rows)
    return {
        "definition": "Dbar[W,a](y|n)=(D[W,a,0](y|n)+D[W,a,1](y|n))/2",
        "averaging_identity": "(1/2) sum_{x in {0,1}} 1{y=x XOR n_d}=1/2 for each y,n_d",
        "reason": "for fixed neighbour condition, every declared target map is a permutation of x",
        "word_rows": len(rows),
        "changed_word_rows": changed_rows,
        "conditioned_configurations": len(rows) * len(NEIGHBOUR_CONDITIONS),
        "edge_pair_comparisons": len(rows) * len(DIRECTIONS) * len(OTHER_CONTEXTS),
        "changed_edge_pair_comparisons": len(all_changed_pairs),
        "any_word_breaks_marginal_independence": bool(changed_rows),
        "scope": "the declared 20-word length-zero/one family only; longer landed words are outside the horizon",
        "rows": rows,
        "changed_edge_pairs_digest": digest(all_changed_pairs),
    }


def rotate_site(site: str | tuple[int, int, int], rotation: tuple[tuple[int, int, int], ...]):
    return site if site == "C" else mat_vec(rotation, site)


def rotate_descriptor(descriptor: tuple, rotation: tuple[tuple[int, int, int], ...]) -> tuple:
    if descriptor[0] == "I":
        return descriptor
    if descriptor[0] == "X":
        return ("X", rotate_site(descriptor[1], rotation))
    return (
        "CNOT", rotate_site(descriptor[1], rotation),
        rotate_site(descriptor[2], rotation),
    )


def rotate_condition(condition: tuple[int, ...], rotation: tuple[tuple[int, int, int], ...]) -> tuple[int, ...]:
    by_direction = {
        mat_vec(rotation, direction): condition[index]
        for index, direction in enumerate(DIRECTIONS)
    }
    return tuple(by_direction[direction] for direction in DIRECTIONS)


def local_site_coordinate(site: str | tuple[int, int, int], target: tuple[int, int, int]) -> tuple[int, int, int]:
    return target if site == "C" else add(target, site)


def global_descriptor(descriptor: tuple, target: tuple[int, int, int]) -> tuple:
    if descriptor[0] == "I":
        return ("I",)
    if descriptor[0] == "X":
        return ("X", local_site_coordinate(descriptor[1], target))
    return (
        "CNOT", local_site_coordinate(descriptor[1], target),
        local_site_coordinate(descriptor[2], target),
    )


def translate_descriptor(descriptor: tuple, translation: tuple[int, int, int]) -> tuple:
    if descriptor[0] == "I":
        return descriptor
    if descriptor[0] == "X":
        return ("X", add(descriptor[1], translation))
    return ("CNOT", add(descriptor[1], translation), add(descriptor[2], translation))


def coordinate_state(target: tuple[int, int, int], local_input: int, condition: tuple[int, ...]) -> dict:
    state = {target: local_input}
    state.update({add(target, direction): condition[index] for index, direction in enumerate(DIRECTIONS)})
    return state


def apply_coordinate_semantic(state: dict, descriptor: tuple) -> dict:
    after = dict(state)
    if descriptor[0] == "X":
        after[descriptor[1]] ^= 1
    elif descriptor[0] == "CNOT" and after[descriptor[1]]:
        after[descriptor[2]] ^= 1
    return after


def translate_state(state: dict, translation: tuple[int, int, int]) -> dict:
    return {add(site, translation): value for site, value in state.items()}


def orbit_under_rotations(atom: tuple, atom_kind: str) -> tuple:
    if atom_kind == "word":
        direction = atom[0]
        return tuple(sorted({mat_vec(rotation, direction) for rotation in ROTATIONS}))
    direction, local_input = atom
    return tuple(sorted({(mat_vec(rotation, direction), local_input) for rotation in ROTATIONS}))


def covariance_and_orbits(resolved: dict) -> dict:
    family = declared_family()
    descriptors = {row["descriptor"] for row in family}
    descriptor_names = {row["descriptor"]: row["name"] for row in family}
    rotation_failures = []
    family_closure_failures = []
    rotation_checks = 0
    for rotation in ROTATIONS:
        for word in family:
            transported = rotate_descriptor(word["descriptor"], rotation)
            if transported not in descriptors:
                family_closure_failures.append((word["name"], rotation, transported))
                continue
            for local_input in (0, 1):
                for condition in NEIGHBOUR_CONDITIONS:
                    rotation_checks += 1
                    left = point_distribution(word["descriptor"], local_input, condition)
                    right = point_distribution(transported, local_input, rotate_condition(condition, rotation))
                    if left != right:
                        rotation_failures.append((word["name"], descriptor_names[transported], local_input, condition, left, right))

    landed_coordinate_bridge_failures = []
    landed_coordinate_bridge_checks = 0
    for word in family:
        global_word = global_descriptor(word["descriptor"], CENTER)
        for local_input in (0, 1):
            for condition in NEIGHBOUR_CONDITIONS:
                landed_coordinate_bridge_checks += 1
                core_after = A.apply_semantic(
                    basis_state(local_input, condition), core_word(word["descriptor"])
                )
                coordinate_after = apply_coordinate_semantic(
                    coordinate_state(CENTER, local_input, condition), global_word
                )
                reencoded = tuple(
                    coordinate_after[CENTER] if wire == 0
                    else coordinate_after[add(CENTER, DIRECTIONS[wire - 1])]
                    for wire in range(1 + len(DIRECTIONS))
                )
                if core_after != reencoded:
                    landed_coordinate_bridge_failures.append((
                        word["name"], local_input, condition, core_after, reencoded,
                    ))

    translation_failures = []
    translation_checks = 0
    target = CENTER
    for translation in TRANSLATION_GENERATORS:
        for word in family:
            local_global = global_descriptor(word["descriptor"], target)
            transported_word = translate_descriptor(local_global, translation)
            if transported_word != global_descriptor(word["descriptor"], translation):
                translation_failures.append((word["name"], translation, "word_transport"))
            for local_input in (0, 1):
                for condition in NEIGHBOUR_CONDITIONS:
                    translation_checks += 1
                    before = coordinate_state(target, local_input, condition)
                    left = translate_state(apply_coordinate_semantic(before, local_global), translation)
                    right_before = translate_state(before, translation)
                    right = apply_coordinate_semantic(right_before, transported_word)
                    if left != right:
                        translation_failures.append((word["name"], translation, local_input, condition))

    witness_directions = tuple(
        DIRECTIONS[DIRECTION_NAMES.index(row["reads_neighbour_bit"])]
        for row in resolved["witness_words"]
    )
    word_atoms = set((direction,) for direction in witness_directions)
    word_orbits = []
    while word_atoms:
        representative = min(word_atoms)
        orbit = set((direction,) for direction in orbit_under_rotations(representative, "word")) & word_atoms
        word_orbits.append(tuple(sorted(orbit)))
        word_atoms -= orbit

    state_atoms = set((direction, local_input) for direction in witness_directions for local_input in (0, 1))
    state_orbits = []
    while state_atoms:
        representative = min(state_atoms)
        orbit = set(orbit_under_rotations(representative, "state")) & state_atoms
        state_orbits.append(tuple(sorted(orbit)))
        state_atoms -= orbit

    def orbit_record(orbit: tuple, state_resolved: bool) -> dict:
        representative = orbit[0]
        direction = representative[0] if state_resolved else representative[0]
        local_input = representative[1] if state_resolved else None
        stabilizer = sum(
            mat_vec(rotation, direction) == direction for rotation in ROTATIONS
        )
        result = {
            "representative_word": f"CNOT({direction_name(direction)}->C)",
            "local_rotation_orbit_size": len(orbit),
            "proper_rotation_stabilizer_size": stabilizer,
            "global_space_group_orbit_cardinality": "countably infinite",
            "global_orbit_parameterization": "a in Z^3 and d in {+/-e_x,+/-e_y,+/-e_z}",
        }
        if state_resolved:
            result["fixed_target_input"] = local_input
        return result

    non_covariant_words = sorted({
        failure[0] for failure in (
            rotation_failures + translation_failures + landed_coordinate_bridge_failures
        )
    })
    return {
        "realized_group": "Z^3 semidirect product with the 24 proper signed-permutation cubic rotations",
        "group_action": "(a,d,x) maps to (R a+t,R d,x); target bit x is not acted on",
        "proper_rotation_count": len(ROTATIONS),
        "rotation_group_closed": all(
            tuple(tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3)) for i in range(3)) in set(ROTATIONS)
            for left in ROTATIONS for right in ROTATIONS
        ),
        "rotation_family_closure_failures": family_closure_failures,
        "rotation_semantic_comparisons": rotation_checks,
        "rotation_semantic_failures": rotation_failures,
        "translation_generators": [list(value) for value in TRANSLATION_GENERATORS],
        "translation_semantic_comparisons": translation_checks,
        "translation_semantic_failures": translation_failures,
        "landed_coordinate_bridge_comparisons": landed_coordinate_bridge_checks,
        "landed_coordinate_bridge_failures": landed_coordinate_bridge_failures,
        "covariant": (
            not family_closure_failures and not rotation_failures
            and not landed_coordinate_bridge_failures and not translation_failures
        ),
        "non_covariant_witnesses": non_covariant_words,
        "word_law_class_count": len(word_orbits),
        "word_law_orbits": [orbit_record(orbit, False) for orbit in word_orbits],
        "state_resolved_class_count": len(state_orbits),
        "state_resolved_orbits": [orbit_record(orbit, True) for orbit in state_orbits],
        "class_interpretation": "one spatial word-law class; two state-resolved classes because proper lattice motions do not flip x=0 and x=1",
    }


def provenance_controls() -> dict:
    observations = {}
    for label, (path, expected_blob) in PROVENANCE_OBJECTS.items():
        spec = f"{PROVENANCE_COMMIT}:{path}"
        observed_blob = subprocess.check_output(("git", "rev-parse", spec), cwd=ROOT, text=True).strip()
        body = subprocess.check_output(("git", "show", spec), cwd=ROOT)
        if label == "runner":
            tree = ast.parse(body.decode("utf-8"), filename=spec)
            observations[label] = {
                "path": path,
                "expected_blob": expected_blob,
                "observed_blob": observed_blob,
                "read_mode": "AST only; never executed",
                "has_declared_family_function": any(isinstance(node, ast.FunctionDef) and node.name == "declared_family" for node in ast.walk(tree)),
                "has_state_resolved_census_function": any(isinstance(node, ast.FunctionDef) and node.name == "state_resolved_census" for node in ast.walk(tree)),
            }
        else:
            text = body.decode("utf-8")
            observations[label] = {
                "path": path,
                "expected_blob": expected_blob,
                "observed_blob": observed_blob,
                "read_mode": "text only",
                "declares_full_covariant_law_open": "full covariant M_2(C) law remains open" in text,
                "reports_four_of_twenty": "four of the 20" in text,
            }
    return observations


def input_controls() -> dict:
    pins = {}
    existing = True
    for rel in AUDIT_INPUT_PATHS:
        path = ROOT / rel
        inside = path.resolve().is_relative_to(ROOT.resolve())
        existing &= path.is_file() and inside
        pins[rel] = sha256(path.read_bytes()).hexdigest() if path.is_file() else None
    axiom_text = (ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    needle = (
        "For each site, the probability distribution over the possibilities is\n"
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    record_boundary_needles = (
        "Finite additivity, a named scalar collection functional `I`, and an assigned",
        "value `I(empty)=0` are not Record axiom content.",
        "A site with no record cannot be read.",
    )
    provenance = provenance_controls()
    return {
        "literal_audit_input_paths": list(AUDIT_INPUT_PATHS),
        "all_inputs_exist_worktree_relative": existing,
        "sha256": pins,
        "primary_source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "blocklist_cited_primaries": list(BLOCKLIST_CITED_PRIMARIES),
        "blocklist_text_only": all(not path.endswith(".py") for path in BLOCKLIST_CITED_PRIMARIES),
        "executable_substrate": EXECUTABLE_SUBSTRATE,
        "landed_axiom_needle_matches": needle in axiom_text,
        "current_record_boundary_matches": all(
            value in axiom_text for value in record_boundary_needles
        ),
        "cycle970_text_ast_provenance": provenance,
        "provenance_pins_match": all(row["expected_blob"] == row["observed_blob"] for row in provenance.values()),
    }


def run_science() -> dict:
    resolved = state_resolved_census()
    uniform = uniform_target_input_census()
    covariance = covariance_and_orbits(resolved)
    return {"resolved": resolved, "covariance": covariance, "uniform": uniform}


def main() -> int:
    started = monotonic()
    first = run_science()
    second = run_science()
    deterministic = digest(first) == digest(second)
    controls = input_controls()
    resolved = first["resolved"]
    covariance = first["covariance"]
    uniform = first["uniform"]

    expected_family_size = 1 + (1 + len(DIRECTIONS)) + 2 * len(DIRECTIONS)
    expected_resolved_rows = len(declared_family()) * 2
    expected_edge_pairs = expected_resolved_rows * len(DIRECTIONS) * len(OTHER_CONTEXTS)
    a_ok = (
        len(declared_family()) == expected_family_size
        and len({row["name"] for row in declared_family()}) == len(declared_family())
        and resolved["word_local_input_rows"] == expected_resolved_rows
        and resolved["edge_pair_comparisons"] == expected_edge_pairs
        and resolved["changed_edge_pair_comparisons"] == sum(row["changed_edge_pairs"] for row in resolved["rows"])
        and resolved["witness_word_count"] == len(resolved["witness_words"])
        and resolved["law_truth_table_comparisons"] == sum(
            row["law_truth_table_comparisons"] for row in resolved["witness_words"]
        )
        and resolved["xor_law_holds"] == (not resolved["xor_law_failures"])
        and resolved["controls_preserved"] == (not resolved["control_preservation_failures"])
        and 0 <= resolved["dependent_word_local_input_rows"] <= resolved["word_local_input_rows"]
        and 0 <= resolved["changed_edge_pair_comparisons"] <= resolved["edge_pair_comparisons"]
    )
    a_finding = (
        f"family_words={resolved['family_words']}=1_identity+7_X+12_oriented_CNOT; "
        f"neighbour_conditions={resolved['neighbour_condition_count']}; witness_words="
        f"{resolved['witness_word_count']}/{resolved['family_words']}; dependent_word_x_rows="
        f"{resolved['dependent_word_local_input_rows']}/{resolved['word_local_input_rows']}; "
        f"changed_edge_pairs={resolved['changed_edge_pair_comparisons']}/{resolved['edge_pair_comparisons']}; "
        f"witnesses={[row['word_name'] for row in resolved['witness_words']]}; "
        f"xor_truth_table_failures={len(resolved['xor_law_failures'])}/"
        f"{resolved['law_truth_table_comparisons']}; control_preservation_failures="
        f"{len(resolved['control_preservation_failures'])}/{resolved['law_truth_table_comparisons']}"
    )

    expected_rotation_checks = len(ROTATIONS) * len(declared_family()) * 2 * len(NEIGHBOUR_CONDITIONS)
    expected_translation_checks = len(TRANSLATION_GENERATORS) * len(declared_family()) * 2 * len(NEIGHBOUR_CONDITIONS)
    expected_bridge_checks = len(declared_family()) * 2 * len(NEIGHBOUR_CONDITIONS)
    b_ok = (
        len(ROTATIONS) == len(set(ROTATIONS))
        and all(determinant(rotation) == 1 for rotation in ROTATIONS)
        and covariance["rotation_group_closed"]
        and covariance["rotation_semantic_comparisons"] == expected_rotation_checks
        and covariance["translation_semantic_comparisons"] == expected_translation_checks
        and covariance["landed_coordinate_bridge_comparisons"] == expected_bridge_checks
        and covariance["covariant"] == (
            not covariance["rotation_family_closure_failures"]
            and not covariance["rotation_semantic_failures"]
            and not covariance["landed_coordinate_bridge_failures"]
            and not covariance["translation_semantic_failures"]
        )
    )
    b_finding = (
        f"group=Z3_semidirect_Oplus_cubic; rotations={covariance['proper_rotation_count']}; "
        f"rotation_checks={covariance['rotation_semantic_comparisons']}; landed_coordinate_bridge_failures="
        f"{len(covariance['landed_coordinate_bridge_failures'])}/"
        f"{covariance['landed_coordinate_bridge_comparisons']}; translation_generator_checks="
        f"{covariance['translation_semantic_comparisons']}; covariance_verdict="
        f"{'COVARIANT' if covariance['covariant'] else 'NON_COVARIANT'}; "
        f"non_covariant_witnesses={covariance['non_covariant_witnesses']}"
    )

    orbit_atoms = sum(row["local_rotation_orbit_size"] for row in covariance["state_resolved_orbits"])
    c_ok = (
        covariance["word_law_class_count"] == len(covariance["word_law_orbits"])
        and covariance["state_resolved_class_count"] == len(covariance["state_resolved_orbits"])
        and orbit_atoms == resolved["witness_word_count"] * 2
        and all(row["local_rotation_orbit_size"] > 0 for row in covariance["state_resolved_orbits"])
    )
    c_finding = (
        f"word_law_classes={covariance['word_law_class_count']}; state_resolved_classes="
        f"{covariance['state_resolved_class_count']}; state_representatives="
        f"{[(row['representative_word'], row['fixed_target_input']) for row in covariance['state_resolved_orbits']]}; "
        f"local_orbit_sizes={[row['local_rotation_orbit_size'] for row in covariance['state_resolved_orbits']]}; "
        f"stabilizers={[row['proper_rotation_stabilizer_size'] for row in covariance['state_resolved_orbits']]}"
    )

    d_ok = (
        uniform["word_rows"] == len(declared_family())
        and uniform["edge_pair_comparisons"] == len(declared_family()) * len(DIRECTIONS) * len(OTHER_CONTEXTS)
        and uniform["changed_word_rows"] == sum(row["breaks_marginal_independence"] for row in uniform["rows"])
        and uniform["any_word_breaks_marginal_independence"] == bool(uniform["changed_word_rows"])
        and 0 <= uniform["changed_edge_pair_comparisons"] <= uniform["edge_pair_comparisons"]
    )
    d_finding = (
        f"uniform_target_input_changed_words={uniform['changed_word_rows']}/{uniform['word_rows']}; "
        f"changed_edge_pairs={uniform['changed_edge_pair_comparisons']}/{uniform['edge_pair_comparisons']}; "
        f"identity={uniform['averaging_identity']}; any_break="
        f"{uniform['any_word_breaks_marginal_independence']}; scope=declared_length_zero/one_family"
    )

    elapsed = monotonic() - started
    provenance = controls["cycle970_text_ast_provenance"]
    output_upper_bound = sum(map(len, (a_finding, b_finding, c_finding, d_finding))) + 3_000
    e_ok = (
        controls["all_inputs_exist_worktree_relative"]
        and controls["blocklist_text_only"]
        and controls["landed_axiom_needle_matches"]
        and controls["current_record_boundary_matches"]
        and controls["provenance_pins_match"]
        and provenance["runner"]["has_declared_family_function"]
        and provenance["runner"]["has_state_resolved_census_function"]
        and provenance["note"]["declares_full_covariant_law_open"]
        and provenance["note"]["reports_four_of_twenty"]
        and deterministic
        and all(controls["sha256"].values())
        and elapsed < AUDIT_TIMEOUT_SEC
        and AUDIT_TIMEOUT_SEC < 1400
        and output_upper_bound < HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
    )
    e_finding = (
        f"sha_pins={compact(controls['sha256'])}; cycle970_provenance_commit={PROVENANCE_COMMIT}; "
        f"runner_read=AST_only; note_read=text_only; provenance_pins_match="
        f"{controls['provenance_pins_match']}; determinism_replay={deterministic}; "
        f"runtime_s={elapsed:.6f}<timeout_s={AUDIT_TIMEOUT_SEC}; stdout_upper_bound_bytes="
        f"{output_upper_bound}<{HOUSE_STDOUT_LIMIT_BYTES}<{STDOUT_LIMIT_BYTES}; timeout_s={AUDIT_TIMEOUT_SEC}<1400"
    )

    certificates = (
        ("A_FULL_WITNESS_CENSUS", a_ok, a_finding),
        ("B_COVARIANCE_MEASUREMENT", b_ok, b_finding),
        ("C_ORBIT_PARTITION", c_ok, c_finding),
        ("D_MARGINAL_MEASUREMENT", d_ok, d_finding),
        ("E_CONTROLS_AND_PROVENANCE", e_ok, e_finding),
    )
    all_pass = all(ok for _, ok, _ in certificates)
    report = {
        "cycle": 972,
        "claim_type": "bounded_theorem",
        "actual_current_surface_status": "bounded-support",
        "trace_class": "direct_blocker_closure",
        "reachability_to_target": "closes",
        "family_horizon": {
            "word_length_cap": 1,
            "spatial_horizon": "one target-centred radius-one nearest-neighbour star",
            "target_input_menu": [0, 1],
            "neighbour_condition_horizon": "all 2^6 basis-bit conditions",
            "gate_kinds": ["identity", "X", "CNOT"],
            "family_description": FAMILY_DESCRIPTION,
            "family_size": len(declared_family()),
            "excluded": [
                "TOF (excluded by the declared two-site gate-kind/arity condition)",
                "words of length >=2",
                "continuous M_2(C) distributions",
            ],
        },
        "law_formula": LAW_FORMULA,
        "findings": first,
        "controls": controls,
        "determinism_replay": deterministic,
        "science_digest": digest(first),
        "runtime_sec": elapsed,
        "certificates": {name: {"pass": ok, "finding": finding} for name, ok, finding in certificates},
        "all_certificates_pass": all_pass,
    }
    checker_payload = {
        "family_words": resolved["family_words"],
        "witness_word_count": resolved["witness_word_count"],
        "witness_word_names": [row["word_name"] for row in resolved["witness_words"]],
        "dependent_word_local_input_rows": resolved["dependent_word_local_input_rows"],
        "word_local_input_rows": resolved["word_local_input_rows"],
        "changed_edge_pair_comparisons": resolved["changed_edge_pair_comparisons"],
        "edge_pair_comparisons": resolved["edge_pair_comparisons"],
        "law_truth_table_comparisons": resolved["law_truth_table_comparisons"],
        "xor_law_failures": resolved["xor_law_failures"],
        "control_preservation_failures": resolved["control_preservation_failures"],
        "witness_structures_digest": digest(resolved["witness_words"]),
        "covariant": covariance["covariant"],
        "non_covariant_witnesses": covariance["non_covariant_witnesses"],
        "proper_rotation_count": covariance["proper_rotation_count"],
        "rotation_semantic_comparisons": covariance["rotation_semantic_comparisons"],
        "rotation_semantic_failure_count": len(covariance["rotation_semantic_failures"]),
        "landed_coordinate_bridge_comparisons": covariance["landed_coordinate_bridge_comparisons"],
        "landed_coordinate_bridge_failure_count": len(covariance["landed_coordinate_bridge_failures"]),
        "translation_semantic_comparisons": covariance["translation_semantic_comparisons"],
        "translation_semantic_failure_count": len(covariance["translation_semantic_failures"]),
        "word_law_class_count": covariance["word_law_class_count"],
        "state_resolved_class_count": covariance["state_resolved_class_count"],
        "state_orbit_sizes": [row["local_rotation_orbit_size"] for row in covariance["state_resolved_orbits"]],
        "state_stabilizer_sizes": [row["proper_rotation_stabilizer_size"] for row in covariance["state_resolved_orbits"]],
        "marginal_changed_words": uniform["changed_word_rows"],
        "marginal_word_rows": uniform["word_rows"],
        "marginal_changed_edge_pairs": uniform["changed_edge_pair_comparisons"],
        "marginal_edge_pairs": uniform["edge_pair_comparisons"],
        "science_digest": report["science_digest"],
    }
    lines = ["=" * 78, "CYCLE 972 -- COVARIANT NEIGHBOUR-DEPENDENCE LAW", "=" * 78]
    lines.extend(f"{'PASS' if ok else 'FAIL'} {name} :: {finding}" for name, ok, finding in certificates)
    lines.append("CHECKER_PAYLOAD: " + compact(checker_payload))
    if not all_pass:
        verdict = "COVARIANT_DEPENDENCE_MEASUREMENT_INCOMPLETE"
    elif covariance["covariant"]:
        verdict = "BOUNDED_COVARIANT_DEPENDENCE_LAW_CHARACTERIZED"
    else:
        verdict = "NON_COVARIANT_WITNESS_FOUND"
    lines.append("VERDICT: " + verdict)
    pass_count = sum(ok for _, ok, _ in certificates)
    lines.append(f"TOTAL: PASS={pass_count} FAIL={len(certificates) - pass_count}")
    text = "\n".join(lines) + "\n"
    report["stdout_bytes"] = len(text.encode())
    receipt_path = ROOT / "outputs" / "covariant_dependence_law_cycle972_receipt_2026_08_09.json"
    if len(text.encode()) >= HOUSE_STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    receipt_path.write_text(json.dumps(report, indent=1, sort_keys=True) + "\n")
    sys.stdout.write(text)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
