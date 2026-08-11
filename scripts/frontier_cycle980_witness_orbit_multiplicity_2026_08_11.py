#!/usr/bin/env python3
"""Cycle 980: exact witness-orbit and landed-alphabet multiplicity census.

The primary calculation derives the neighbour-dependent members of the full
length-zero/one seven-site family from the immutable Cycle-719 basis-state
substrate.  It then computes the effective proper-cubic action on those
witness descriptors, rather than assuming that the reported 6/12/3 classes
are orbits.  Integrity checks certify construction and reconciliation only:
failure of closure, orbit separation, or a three-class outcome is reportable
without making the runner fail.
"""

from __future__ import annotations

import ast
import io
import importlib.util
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
CYCLE = 980
AUDIT_TIMEOUT_SEC = 1400
HOUSE_STDOUT_LIMIT_BYTES = 6_000
STDOUT_LIMIT_BYTES = 150_000
BASE_ORIGIN_MAIN_COMMIT = "e8cb78a911d91f48abac9783c68305b0e7aabdf7"
PINNED_CYCLE719_COMMIT = "39c74017b870c27c804e3992f2a11e90336476b2"
PINNED_CYCLE719_CORE = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
)
PINNED_CYCLE719_CORE_SHA256 = (
    "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4"
)
PINNED_CYCLE719_CORE_BLOB = "c123b8d681c3d76fce08ef13d7673622deac64ad"

AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
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
    "outputs/witness_family_completeness_cycle977_receipt_2026_08_10.json",
    "outputs/class_coexistence_born_requirement_cycle979_receipt_2026_08_10.json",
)
BLOCKLIST_AST_MODULES = (
    "frontier_cycle977_witness_family_completeness_2026_08_10",
    "frontier_cycle977_witness_family_independent_check_2026_08_10",
    "frontier_cycle979_class_coexistence_born_requirement_2026_08_10",
    "frontier_cycle979_class_coexistence_independent_check_2026_08_10",
)

PRIMARY_PATH = "scripts/frontier_cycle980_witness_orbit_multiplicity_2026_08_11.py"
RECEIPT_PATH = "outputs/witness_orbit_multiplicity_cycle980_receipt_2026_08_11.json"
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
CONDITIONS = tuple(product((0, 1), repeat=6))
OTHER_CONTEXTS = tuple(product((0, 1), repeat=5))


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def ast_literal_assignment(tree: ast.Module, name: str):
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def load_pinned_cycle719_core():
    archive = subprocess.run(
        ["git", "archive", "--format=tar", PINNED_CYCLE719_COMMIT, "scripts"],
        cwd=ROOT, check=True, capture_output=True,
    ).stdout
    temporary = tempfile.TemporaryDirectory(prefix="cycle980-cycle719-")
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as bundle:
        bundle.extractall(temporary.name, filter="data")
    scripts_dir = Path(temporary.name) / "scripts"
    sys.path.insert(0, str(scripts_dir))
    core_path = Path(temporary.name) / PINNED_CYCLE719_CORE
    spec = importlib.util.spec_from_file_location("cycle980_pinned_cycle719", core_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load pinned Cycle-719 core")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return temporary, module


PINNED_TEMP, K = load_pinned_cycle719_core()


def site_name(wire: int) -> str:
    return "C" if wire == 0 else DIRECTION_NAMES[wire - 1]


def word_name(descriptor: tuple) -> str:
    kind = descriptor[0]
    if kind == "I":
        return "I"
    if kind == "X":
        return f"X({site_name(descriptor[1])})"
    if kind == "CNOT":
        return f"CNOT({site_name(descriptor[1])}->{site_name(descriptor[2])})"
    return (
        f"TOF({site_name(descriptor[1])},{site_name(descriptor[2])}"
        f"->{site_name(descriptor[3])})"
    )


def declared_family(alphabet: tuple[str, ...] = LANDED_GATE_MENU) -> tuple:
    allowed = set(alphabet)
    rows = [("I",)]
    if "X" in allowed:
        rows.extend(("X", target) for target in range(SITE_COUNT))
    if "CNOT" in allowed:
        rows.extend(
            ("CNOT", control, target)
            for control, target in permutations(range(SITE_COUNT), 2)
        )
    if "TOF" in allowed:
        for target in range(SITE_COUNT):
            available = tuple(site for site in range(SITE_COUNT) if site != target)
            rows.extend(
                ("TOF", controls[0], controls[1], target)
                for controls in combinations(available, 2)
            )
    return tuple(rows)


def core_word(descriptor: tuple) -> tuple:
    kind = descriptor[0]
    if kind == "I":
        return ()
    if kind == "X":
        return (K.A.x(descriptor[1]),)
    if kind == "CNOT":
        return (K.A.cn(descriptor[1], descriptor[2]),)
    return (K.A.tof(descriptor[1], descriptor[2], descriptor[3]),)


def landed_target_output(descriptor: tuple, x: int, condition: tuple) -> int:
    return K.A.apply_semantic((x, *condition), core_word(descriptor))[0]


def independent_target_output(descriptor: tuple, x: int, condition: tuple) -> int:
    state = [x, *condition]
    kind = descriptor[0]
    if kind == "X":
        state[descriptor[1]] ^= 1
    elif kind == "CNOT" and state[descriptor[1]]:
        state[descriptor[2]] ^= 1
    elif kind == "TOF" and state[descriptor[1]] and state[descriptor[2]]:
        state[descriptor[3]] ^= 1
    return state[0]


def with_edge(index: int, other: tuple, bit: int) -> tuple:
    values = []
    source = iter(other)
    for position in range(6):
        values.append(bit if position == index else next(source))
    return tuple(values)


def is_witness(descriptor: tuple) -> tuple[bool, int]:
    changed = 0
    for x in (0, 1):
        for direction_index in range(6):
            for other in OTHER_CONTEXTS:
                condition_0 = with_edge(direction_index, other, 0)
                condition_1 = with_edge(direction_index, other, 1)
                changed += landed_target_output(descriptor, x, condition_0) != (
                    landed_target_output(descriptor, x, condition_1)
                )
    return changed > 0, changed


def dot(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(a * b for a, b in zip(left, right))


def determinant(matrix: tuple[tuple[int, int, int], ...]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat_vec(matrix: tuple, vector: tuple) -> tuple:
    return tuple(dot(row, vector) for row in matrix)


def mat_mul(left: tuple, right: tuple) -> tuple:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
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


def rotate_wire(wire: int, rotation: tuple) -> int:
    return OFFSET_TO_WIRE[mat_vec(rotation, WIRE_TO_OFFSET[wire])]


def rotate_descriptor(descriptor: tuple, rotation: tuple) -> tuple:
    kind = descriptor[0]
    if kind == "I":
        return descriptor
    wires = tuple(rotate_wire(wire, rotation) for wire in descriptor[1:])
    if kind == "TOF":
        return (kind, *sorted(wires[:2]), wires[2])
    return (kind, *wires)


def controls_of_witness(descriptor: tuple) -> tuple[int, ...]:
    if descriptor[0] == "CNOT":
        return (descriptor[1],)
    if descriptor[0] == "TOF":
        return descriptor[1:3]
    raise ValueError(descriptor)


def witness_invariant(descriptor: tuple) -> dict:
    controls = controls_of_witness(descriptor)
    offsets = tuple(WIRE_TO_OFFSET[wire] for wire in controls)
    vector_sum = tuple(sum(offset[axis] for offset in offsets) for axis in range(3))
    norm_squared = dot(vector_sum, vector_sum)
    gram = tuple(
        dot(offsets[left], offsets[right])
        for left in range(len(offsets))
        for right in range(left + 1, len(offsets))
    )
    return {
        "control_arity": len(controls),
        "control_sum_norm_squared": norm_squared,
        "off_diagonal_control_gram": list(sorted(gram)),
    }


def orbit_label(members: tuple) -> str:
    kinds = {row[0] for row in members}
    invariants = {witness_invariant(row)["control_sum_norm_squared"] for row in members}
    if kinds == {"CNOT"}:
        return "CNOT"
    if kinds == {"TOF"} and invariants == {2}:
        return "TOF_PERPENDICULAR_CONTROLS"
    if kinds == {"TOF"} and invariants == {0}:
        return "TOF_OPPOSITE_CONTROLS"
    return "UNCLASSIFIED_" + digest([sorted(kinds), sorted(invariants)])[:12]


def orbit_decomposition(witnesses: tuple) -> dict:
    witness_set = set(witnesses)
    ambient_orbits = {}
    for descriptor in witnesses:
        ambient = frozenset(rotate_descriptor(descriptor, rotation) for rotation in ROTATIONS)
        ambient_orbits.setdefault(ambient, descriptor)
    rows = []
    covered = []
    for ambient, seed in sorted(ambient_orbits.items(), key=lambda item: word_name(min(item[0]))):
        members = tuple(sorted(ambient & witness_set, key=word_name))
        stabilizer = sum(
            rotate_descriptor(seed, rotation) == seed for rotation in ROTATIONS
        )
        invariant_values = {
            compact(witness_invariant(descriptor)) for descriptor in members
        }
        rows.append({
            "class_label": orbit_label(members),
            "representative": word_name(min(members, key=word_name)),
            "member_count": len(members),
            "members": [word_name(row) for row in members],
            "ambient_orbit_size": len(ambient),
            "effective_stabilizer_order": stabilizer,
            "orbit_stabilizer_product": len(ambient) * stabilizer,
            "orbit_is_closed_in_witness_set": ambient <= witness_set,
            "invariant_values": [json.loads(value) for value in sorted(invariant_values)],
        })
        covered.extend(members)
    invariant_to_orbits = {}
    for index, row in enumerate(rows):
        for value in row["invariant_values"]:
            invariant_to_orbits.setdefault(compact(value), []).append(index)
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
        "invariant_constant_on_each_orbit": all(
            len(row["invariant_values"]) == 1 for row in rows
        ),
        "invariant_distinct_across_orbits": all(
            len(indices) == 1 for indices in invariant_to_orbits.values()
        ),
        "class_count_sum": sum(row["member_count"] for row in rows),
    }


def translation_kernel_certificate(witnesses: tuple) -> dict:
    failures = []
    checks = 0
    for translation in DIRECTIONS:
        new_center = translation
        for descriptor in witnesses:
            checks += 1
            shifted_offsets = tuple(
                tuple(new_center[axis] + WIRE_TO_OFFSET[wire][axis] for axis in range(3))
                for wire in descriptor[1:]
            )
            recentered = tuple(
                tuple(site[axis] - new_center[axis] for axis in range(3))
                for site in shifted_offsets
            )
            if recentered != tuple(WIRE_TO_OFFSET[wire] for wire in descriptor[1:]):
                failures.append((word_name(descriptor), translation))
    return {
        "generator_checks": checks,
        "failure_count": len(failures),
        "translations_are_kernel_after_recentring": not failures,
    }


def family_measurement(alphabet: tuple[str, ...]) -> dict:
    family = declared_family(alphabet)
    witnesses = []
    changed_pairs = 0
    landed_boolean_failures = 0
    for descriptor in family:
        witness, changed = is_witness(descriptor)
        changed_pairs += changed
        if witness:
            witnesses.append(descriptor)
        for x in (0, 1):
            for condition in CONDITIONS:
                landed_boolean_failures += landed_target_output(descriptor, x, condition) != (
                    independent_target_output(descriptor, x, condition)
                )
    orbit_data = orbit_decomposition(tuple(witnesses))
    return {
        "alphabet": list(alphabet),
        "family_size": len(family),
        "family_descriptor_digest": digest(family),
        "witness_count": len(witnesses),
        "witness_descriptors": [list(row) for row in witnesses],
        "witness_names": [word_name(row) for row in witnesses],
        "witness_digest": digest(witnesses),
        "changed_edge_pairs": changed_pairs,
        "landed_boolean_comparisons": len(family) * 2 * len(CONDITIONS),
        "landed_boolean_failure_count": landed_boolean_failures,
        "orbit_count": orbit_data["orbit_count"],
        "orbit_member_counts": [row["member_count"] for row in orbit_data["orbits"]],
        "orbit_labels": [row["class_label"] for row in orbit_data["orbits"]],
    }


def alphabet_lattice() -> list[dict]:
    rows = []
    for size in range(len(LANDED_GATE_MENU) + 1):
        for subset in combinations(LANDED_GATE_MENU, size):
            rows.append(family_measurement(subset))
    return rows


def group_certificate() -> dict:
    rotation_set = set(ROTATIONS)
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    return {
        "generated_order": len(ROTATIONS),
        "all_signed_permutation_determinants_plus_one": all(
            determinant(rotation) == 1 for rotation in ROTATIONS
        ),
        "identity_present": identity in rotation_set,
        "composition_closed": all(
            mat_mul(left, right) in rotation_set
            for left in ROTATIONS for right in ROTATIONS
        ),
        "all_have_inverse": all(
            any(mat_mul(left, right) == identity for right in ROTATIONS)
            for left in ROTATIONS
        ),
    }


def science_measurement() -> dict:
    full = family_measurement(LANDED_GATE_MENU)
    witnesses = tuple(tuple(row) for row in full["witness_descriptors"])
    return {
        "declared_family": {
            "support": "target-centred radius-one seven-site star",
            "word_length": "zero or one",
            "landed_gate_menu": ["I", *LANDED_GATE_MENU],
            "operand_rule": "distinct wires; TOF controls unordered; no within-star adjacency restriction",
            "cap": "all descriptors in this finite family; no sampling",
        },
        "full_family": full,
        "effective_group_validation": group_certificate(),
        "translation_kernel": translation_kernel_certificate(witnesses),
        "orbit_decomposition": orbit_decomposition(witnesses),
        "invariant_definition": {
            "name": "J",
            "formula": "J(w)=||sum of centre-relative control displacement vectors||^2",
            "domain": "derived neighbour-dependence witnesses",
        },
        "alphabet_subset_census": alphabet_lattice(),
    }


def input_controls() -> dict:
    source_text = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    own_tree = ast.parse(source_text, filename=PRIMARY_PATH)
    literal_paths = ast_literal_assignment(own_tree, "AUDIT_INPUT_PATHS")
    literal_text_blocklist = ast_literal_assignment(own_tree, "BLOCKLIST_TEXT_PATHS")
    literal_ast_blocklist = ast_literal_assignment(own_tree, "BLOCKLIST_AST_MODULES")
    payloads = {relative: (ROOT / relative).read_bytes() for relative in literal_paths}
    sha_rows = {relative: sha256(payload).hexdigest() for relative, payload in payloads.items()}
    blob_rows = {relative: git_blob(payload) for relative, payload in payloads.items()}
    pinned_core = subprocess.run(
        ["git", "show", f"{PINNED_CYCLE719_COMMIT}:{PINNED_CYCLE719_CORE}"],
        cwd=ROOT, check=True, capture_output=True,
    ).stdout
    imported_names = {
        alias.name
        for node in ast.walk(own_tree) if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module
        for node in ast.walk(own_tree)
        if isinstance(node, ast.ImportFrom) and node.module
    }
    blocked_imports = sorted(
        name for name in imported_names
        if any(name.endswith(blocked) for blocked in literal_ast_blocklist)
    )
    blocked_loaded = sorted(
        name for name in sys.modules
        if any(name.endswith(blocked) for blocked in literal_ast_blocklist)
    )
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
            not Path(relative).is_absolute() and (ROOT / relative).is_file()
            for relative in literal_paths
        ),
        "blocklist_text_paths": list(literal_text_blocklist),
        "blocklist_ast_modules": list(literal_ast_blocklist),
        "blocklist_text_disjoint_from_reads": not (
            set(literal_paths) & set(literal_text_blocklist)
        ),
        "blocked_ast_imports": blocked_imports,
        "blocked_ast_modules_loaded": blocked_loaded,
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


def render_stdout(receipt: dict) -> str:
    findings = receipt["findings"]
    orbit = findings["orbit_decomposition"]
    rows = [
        "CYCLE980_WITNESS_ORBIT_MULTIPLICITY",
        "A_ORBIT_DECOMPOSITION " + ("PASS" if receipt["checks"]["A_ORBIT_DECOMPOSITION"] else "FAIL")
        + f" :: effective_group={orbit['effective_group']}({orbit['effective_group_order']});"
        + f" action_closed={orbit['action_closed_on_witnesses']};"
        + " orbits=" + compact([
            [row["class_label"], row["member_count"], row["effective_stabilizer_order"]]
            for row in orbit["orbits"]
        ]) + f"; sum={orbit['class_count_sum']}",
        "B_INVARIANT_SEPARATOR " + ("PASS" if receipt["checks"]["B_INVARIANT_SEPARATOR"] else "FAIL")
        + " :: J=norm2(sum_controls); values=" + compact([
            [row["class_label"], row["invariant_values"]] for row in orbit["orbits"]
        ]) + f"; constant={orbit['invariant_constant_on_each_orbit']};"
        + f" distinct={orbit['invariant_distinct_across_orbits']}",
        "C_NECESSITY " + ("PASS" if receipt["checks"]["C_NECESSITY"] else "FAIL")
        + " :: alphabet_to_classes=" + compact({
            "+".join(row["alphabet"]) or "I_ONLY": row["orbit_count"]
            for row in findings["alphabet_subset_census"]
        }),
        "D_CONTROLS " + ("PASS" if receipt["checks"]["D_CONTROLS"] else "FAIL")
        + f" :: source_reads={receipt['controls']['literal_source_read_count']}<=6;"
        + f" sha_pins={receipt['controls']['sha_pins_match']};"
        + f" blocklist_text_ast={receipt['controls']['blocklist_text_disjoint_from_reads'] and not receipt['controls']['blocked_ast_imports']};"
        + f" determinism={receipt['controls']['determinism_replay']};"
        + f" runtime_s={receipt['controls']['runtime_seconds']:.3f}<1400",
    ]
    passed = sum(receipt["checks"].values())
    rows.append(f"TOTAL: PASS={passed} FAIL={len(receipt['checks']) - passed}")
    return "\n".join(rows) + "\n"


def run() -> tuple[dict, str]:
    started = monotonic()
    controls = input_controls()
    first = science_measurement()
    second = science_measurement()
    deterministic = first == second
    group = first["effective_group_validation"]
    orbit = first["orbit_decomposition"]
    full = first["full_family"]
    subsets = first["alphabet_subset_census"]

    a_bookkeeping = bool(
        group["all_signed_permutation_determinants_plus_one"]
        and group["identity_present"] and group["composition_closed"]
        and group["all_have_inverse"]
        and orbit["partition_has_no_overlap_or_omission"]
        and orbit["class_count_sum"] == full["witness_count"]
        and all(
            row["orbit_stabilizer_product"] == group["generated_order"]
            for row in orbit["orbits"]
        )
    )
    b_bookkeeping = bool(
        all(row["invariant_values"] for row in orbit["orbits"])
        and all(
            {compact(value) for value in row["invariant_values"]} == {
                compact(witness_invariant(tuple(descriptor)))
                for descriptor in full["witness_descriptors"]
                if word_name(tuple(descriptor)) in row["members"]
            }
            for row in orbit["orbits"]
        )
    )
    expected_subsets = {
        subset
        for size in range(len(LANDED_GATE_MENU) + 1)
        for subset in combinations(LANDED_GATE_MENU, size)
    }
    c_bookkeeping = bool(
        {tuple(row["alphabet"]) for row in subsets} == expected_subsets
        and all(
            row["family_size"] == len(declared_family(tuple(row["alphabet"])))
            and row["witness_count"] == len(row["witness_descriptors"])
            and row["orbit_count"] == len(row["orbit_member_counts"])
            and row["witness_count"] == sum(row["orbit_member_counts"])
            and row["landed_boolean_failure_count"] == 0
            for row in subsets
        )
    )
    controls.update({
        "determinism_replay": deterministic,
        "runtime_seconds": monotonic() - started,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "house_stdout_limit_bytes": HOUSE_STDOUT_LIMIT_BYTES,
    })
    d_controls = bool(
        controls["literal_source_read_count"] <= 6
        and controls["all_inputs_relative_and_present"]
        and controls["sha_pins_match"] and controls["blob_pins_match"]
        and controls["blocklist_text_disjoint_from_reads"]
        and not controls["blocked_ast_imports"]
        and not controls["blocked_ast_modules_loaded"]
        and controls["pinned_substrate"]["sha_pin_match"]
        and controls["pinned_substrate"]["blob_pin_match"]
        and controls["base_is_ancestor_of_head"]
        and deterministic and controls["runtime_seconds"] < AUDIT_TIMEOUT_SEC
    )
    receipt = {
        "cycle": CYCLE,
        "artifact": "witness orbit multiplicity bounded theorem primary",
        "audit_status_authority": "independent audit lane only",
        "integrity_policy": (
            "checks gate construction and bookkeeping only; null, non-closed, or non-three-orbit outcomes remain clean reportable findings"
        ),
        "findings": first,
        "science_digest": digest(first),
        "controls": controls,
        "checks": {
            "A_ORBIT_DECOMPOSITION": a_bookkeeping,
            "B_INVARIANT_SEPARATOR": b_bookkeeping,
            "C_NECESSITY": c_bookkeeping,
            "D_CONTROLS": d_controls,
        },
    }
    source_sha = sha256((ROOT / PRIMARY_PATH).read_bytes()).hexdigest()
    receipt["primary_source_sha256"] = source_sha
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
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sys.stdout.write(stdout)
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
