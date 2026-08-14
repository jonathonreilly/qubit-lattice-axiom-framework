#!/usr/bin/env python3
"""Independent refutation attempt for the Cycle-985 record-content theorem.

This checker never imports or executes the primary.  It parses the primary as
text/AST, reconstructs the three gate permutations and the binary readout dual
space independently, binds the primary receipt/cache, and runs active
corruption probes.  Its verdict concerns survival of this refutation attempt,
not audit status.
"""

from __future__ import annotations

import ast
import json
import sys
from copy import deepcopy
from hashlib import sha1, sha256
from itertools import product
from pathlib import Path
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
CYCLE = 985
AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 6_000
PRIMARY_PATH = (
    "scripts/frontier_cycle985_neighbour_dependence_record_content_2026_08_11.py"
)
NOTE_PATH = (
    "docs/NEIGHBOUR_DEPENDENCE_RECORD_CONTENT_CYCLE985_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
PRIMARY_RECEIPT_PATH = (
    "outputs/neighbour_dependence_record_content_cycle985_receipt_2026_08_11.json"
)
PRIMARY_CACHE_PATH = (
    "logs/runner-cache/frontier_cycle985_neighbour_dependence_record_content_2026_08_11.txt"
)
RECEIPT_PATH = (
    "outputs/neighbour_dependence_record_content_cycle985_independent_check_receipt_2026_08_11.json"
)
AUDIT_INPUT_PATHS = (
    "docs/NEIGHBOUR_DEPENDENCE_RECORD_CONTENT_CYCLE985_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "scripts/frontier_cycle985_neighbour_dependence_record_content_2026_08_11.py",
    "outputs/neighbour_dependence_record_content_cycle985_receipt_2026_08_11.json",
    "logs/runner-cache/frontier_cycle985_neighbour_dependence_record_content_2026_08_11.txt",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
BASE_ORIGIN_MAIN_COMMIT = "0dfd13c0a383e2ddde5660669bcff662be0e96d2"
EXPECTED_NOTE_SHA256 = "6e9d4c6656ebb89feef3121c14483980fde008040624df36d1813a1e8c4aa6e0"
EXPECTED_PRIMARY_SOURCE_SHA256 = (
    "d168e92247f45e325b28b5c6a0d99759fb4cf528ed65b2bf6109a8cf7a87232d"
)
EXPECTED_PRIMARY_RECEIPT_SHA256 = (
    "73e043bfb040b63bb77331cc5d72418555932f717666831bb821d365ca93d0c6"
)
EXPECTED_PRIMARY_INPUT_FINGERPRINT_SHA256 = (
    "0508bab90e8d90e7f18431b9290c97639b302bb3816dd774ce2ca11266eb0c7e"
)
EXPECTED_PRIMARY_STDOUT_SHA256 = (
    "a75514e70b263d92a97b49b49ca504df8e28538dd927a7aa868e0a30868adc4c"
)

CLASS_SPECS = (
    ("incoming CNOT", "CNOT", ((1, 0, 0),)),
    ("perpendicular-control TOF", "TOF", ((1, 0, 0), (0, 1, 0))),
    ("opposite-control TOF", "TOF", ((1, 0, 0), (-1, 0, 0))),
)
UNIT_VECTORS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)


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


def apply_gate_permutation(kind: str, state: tuple[int, ...]) -> tuple[int, ...]:
    """Apply the gate as a permutation of a small Boolean state space."""
    target_and_controls = list(state)
    active = target_and_controls[1] == 1
    if kind == "TOF":
        active = active and target_and_controls[2] == 1
    if active:
        target_and_controls[0] = 1 - target_and_controls[0]
    return tuple(target_and_controls)


def j_from_vectors(vectors: tuple[tuple[int, int, int], ...]) -> int:
    total = tuple(sum(vector[axis] for vector in vectors) for axis in range(3))
    return sum(value * value for value in total)


def dot(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(a * b for a, b in zip(left, right))


def cross(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def oriented_frame_rotations() -> tuple:
    frames = []
    for image_x in UNIT_VECTORS:
        for image_y in UNIT_VECTORS:
            if dot(image_x, image_y) == 0:
                frames.append((image_x, image_y, cross(image_x, image_y)))
    return tuple(frames)


ROTATION_FRAMES = oriented_frame_rotations()


def rotate_by_frame(frame: tuple, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(
        sum(vector[axis] * frame[axis][component] for axis in range(3))
        for component in range(3)
    )


def independent_orbit_certificate(vectors: tuple[tuple[int, int, int], ...]) -> dict:
    unordered = len(vectors) == 2
    canonical = tuple(sorted(vectors)) if unordered else vectors
    images = {
        tuple(sorted(rotate_by_frame(frame, vector) for vector in vectors))
        if unordered else tuple(rotate_by_frame(frame, vector) for vector in vectors)
        for frame in ROTATION_FRAMES
    }
    stabilizer = sum(
        (
            tuple(sorted(rotate_by_frame(frame, vector) for vector in vectors))
            if unordered else tuple(rotate_by_frame(frame, vector) for vector in vectors)
        ) == canonical
        for frame in ROTATION_FRAMES
    )
    return {
        "group_order": len(ROTATION_FRAMES),
        "orbit_size": len(images),
        "stabilizer": stabilizer,
        "orbit_stabilizer_product": len(images) * stabilizer,
    }


def independent_class_rows() -> list[dict]:
    classes = []
    for label, kind, vectors in CLASS_SPECS:
        table = []
        edges = []
        controls = tuple(product((0, 1), repeat=len(vectors)))
        for bits in controls:
            contents = tuple(
                apply_gate_permutation(kind, (target, *bits))[0]
                for target in (0, 1)
            )
            table.append({
                "bits": bits,
                "contents": contents,
                "point_masses": tuple(
                    (int(content == 0), int(content == 1)) for content in contents
                ),
            })
        for target in (0, 1):
            for left_index, left in enumerate(controls):
                for right in controls[left_index + 1:]:
                    if sum(a != b for a, b in zip(left, right)) != 1:
                        continue
                    before = apply_gate_permutation(kind, (target, *left))[0]
                    after = apply_gate_permutation(kind, (target, *right))[0]
                    edges.append((target, left, right, before, after, before != after))
        orbit = independent_orbit_certificate(vectors)
        classes.append({
            "class": label,
            "kind": kind,
            "J": j_from_vectors(vectors),
            **orbit,
            "table": table,
            "edges": edges,
            "separated": [edge[:5] for edge in edges if edge[5]],
        })
    return classes


def primary_class_rows(receipt: dict) -> list[dict]:
    rows = []
    for row in receipt["findings"]["A_LOCKED_CONTENT_CENSUS"]["classes"]:
        control_names = tuple(row["controls"])
        table = []
        for item in row["table"]:
            bits = tuple(item["control_configuration"][name] for name in control_names)
            table.append({
                "bits": bits,
                "contents": tuple(
                    item["locked_content_by_target_input"][str(target)]
                    for target in (0, 1)
                ),
                "point_masses": tuple(
                    (
                        item["point_mass_distribution_by_target_input"][str(target)]["P_0"],
                        item["point_mass_distribution_by_target_input"][str(target)]["P_1"],
                    )
                    for target in (0, 1)
                ),
            })
        edges = []
        for item in row["one_neighbour_bit_edges"]:
            left = tuple(item["configuration_before"][name] for name in control_names)
            right = tuple(item["configuration_after"][name] for name in control_names)
            edges.append((
                item["target_input"], left, right,
                item["content_before"], item["content_after"],
                item["changes_locked_content"],
            ))
        rows.append({
            "class": row["class"],
            "kind": "CNOT" if len(control_names) == 1 else "TOF",
            "J": row["J"],
            "orbit_size": row["orbit_size"],
            "stabilizer": row["stabilizer"],
            "group_order": row["group_order"],
            "orbit_stabilizer_product": row["orbit_stabilizer_product"],
            "table": table,
            "edges": edges,
            "separated": [edge[:5] for edge in edges if edge[5]],
        })
    return rows


def independent_readout_result(classes: list[dict]) -> dict:
    pairs = [
        (row.get("class", "synthetic equal-content fixture"), *pair)
        for row in classes for pair in row["separated"]
    ]
    deltas = [after - before for _, _, _, _, before, after in pairs]
    visible_count = sum(delta != 0 for delta in deltas)
    if pairs and visible_count == len(pairs):
        outcome = "DECLARED_SEPARATOR_EXISTS"
    elif pairs and visible_count == 0:
        outcome = "DECLARED_READOUT_FAMILY_AGREES_ON_ALL_COMPARED_PAIRS"
    elif pairs:
        outcome = "PARTIAL_VISIBILITY_IN_DECLARED_READOUT_FAMILY"
    else:
        outcome = "EMPTY_COMPARISON_DOMAIN"
    return {
        "family": "R^{\u007b0,1\u007d}, extended by finite sums",
        "basis": ((1, 0), (0, 1)),
        "pair_count": len(pairs),
        "visible_pair_count": visible_count,
        "I_one_deltas": deltas,
        "pair_signatures": [
            (class_label, target, before, after)
            for class_label, target, _, _, before, after in pairs
        ],
        "outcome": outcome,
        "basis_agreement_iff_contents_equal": all(
            (before == after) == all(weights[before] == weights[after] for weights in ((1, 0), (0, 1)))
            for _, _, _, _, before, after in pairs
        ),
    }


def parse_cache(cache_text: str) -> dict:
    stdout_marker = "----- stdout -----\n"
    stderr_marker = "\n----- stderr -----"
    if stdout_marker not in cache_text or stderr_marker not in cache_text:
        raise ValueError("unrecognized cache envelope")
    header, tail = cache_text.split(stdout_marker, 1)
    stdout, _ = tail.split(stderr_marker, 1)
    fields = {}
    for line in header.splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            fields[key] = value
    return {"fields": fields, "stdout": stdout}


def current_record_boundary(axiom_text: str) -> dict:
    try:
        record = axiom_text.split("### Record / Fixed Reality", 1)[1].split(
            "## Qualification", 1
        )[0]
    except IndexError:
        return {"pass": False}
    normalized = " ".join(record.split())
    required = (
        "Records form.",
        "When present, a record locks exactly one admissible local possibility.",
        "A site never carries more than one record; records are permanent.",
        "Only records are readable.",
        "A readout value is determined by record content alone.",
        "A site with no record cannot be read.",
    )
    forbidden = ("finite additivity", "I(empty)", "scalar functional")
    return {
        "required_sentences_present": all(item in normalized for item in required),
        "retired_collection_structure_absent": all(
            item.lower() not in normalized.lower() for item in forbidden
        ),
        "pass": all(item in normalized for item in required) and all(
            item.lower() not in normalized.lower() for item in forbidden
        ),
    }


def note_contract(note: bytes) -> dict:
    text = note.decode()
    normalized = " ".join(text.split())
    required = (
        "# Conditional locked-content separation in declared binary point-mass laws",
        "Those collection properties are extra declared structure, not Record axiom content.",
        "supplies no scalar/additive collection readout",
        "explicit non-axiom construction",
        "assembly into the framework's one fixed, simultaneous, translation-uniform",
        "negative_assertion_classes: []",
    )
    forbidden = (
        "The axiom licenses `I_one`",
        "content-only additive scalar readout | used directly",
        "Record-admissible additive content-only readout",
    )
    return {
        "sha256": sha256(note).hexdigest(),
        "sha_pin_match": sha256(note).hexdigest() == EXPECTED_NOTE_SHA256,
        "required_boundary_present": all(item in normalized for item in required),
        "forbidden_authority_absent": all(item not in text for item in forbidden),
    }


def primary_ast_and_pins(payloads: dict[str, bytes]) -> dict:
    source = payloads[PRIMARY_PATH]
    tree = ast.parse(source, filename=PRIMARY_PATH)
    literal_inputs = ast_literal_assignment(tree, "AUDIT_INPUT_PATHS")
    literal_base = ast_literal_assignment(tree, "BASE_ORIGIN_MAIN_COMMIT")
    literal_sha = ast_literal_assignment(tree, "EXPECTED_INPUT_SHA256")
    literal_blobs = ast_literal_assignment(tree, "EXPECTED_INPUT_BLOBS")
    axiom = payloads[AXIOM_PATH]
    note = note_contract(payloads[NOTE_PATH])
    return {
        "source_sha256": sha256(source).hexdigest(),
        "source_git_blob": git_blob(source),
        "source_pin_match": sha256(source).hexdigest() == EXPECTED_PRIMARY_SOURCE_SHA256,
        "primary_reads_only_axiom": literal_inputs == (
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
        "review_base_matches": literal_base == BASE_ORIGIN_MAIN_COMMIT,
        "current_axiom_sha_pin_matches": literal_sha == {
            AXIOM_PATH: sha256(axiom).hexdigest()
        },
        "current_axiom_blob_pin_matches": literal_blobs == {
            AXIOM_PATH: git_blob(axiom)
        },
        "current_record_boundary": current_record_boundary(axiom.decode()),
        "note_contract": note,
        "primary_has_main_guard": any(
            isinstance(node, ast.If)
            and isinstance(node.test, ast.Compare)
            for node in tree.body
        ),
    }


def compare_receipt(receipt: dict, independent: list[dict]) -> bool:
    census = receipt["findings"]["A_LOCKED_CONTENT_CENSUS"]
    return bool(
        primary_class_rows(receipt) == independent
        and census["proper_cubic_group_order"] == len(ROTATION_FRAMES)
        and census["M2C_possibility_embedding"] == {
            "P_0": [[1, 0], [0, 0]],
            "P_1": [[0, 0], [0, 1]],
        }
        and census["point_mass_normalization_failures"] == 0
        and census["locked_content_support_failures"] == 0
    )


def readout_agrees(receipt: dict, independent: dict) -> bool:
    visibility = receipt["findings"]["B_READOUT_VISIBILITY"]
    separator = visibility["exact_separator"]
    receipt_pair_signatures = [
        (
            pair["class"], pair["target_input"],
            pair["content_before"], pair["content_after"],
        )
        for pair in visibility["analysis"]["pairs"]
    ]
    common = bool(
        visibility["analysis"]["outcome"] == independent["outcome"]
        and visibility["analysis"]["pair_count"] == independent["pair_count"]
        and visibility["analysis"]["visible_pair_count"]
        == independent["visible_pair_count"]
        and len(visibility["analysis"]["pairs"])
        == visibility["analysis"]["pair_count"]
        and receipt_pair_signatures == independent["pair_signatures"]
        and independent["basis_agreement_iff_contents_equal"]
        and "explicit non-axiom structure" in visibility["selection_boundary"]
        and "Record supplies no" in visibility["selection_boundary"]
        and "Record axiom permits" not in visibility["selection_boundary"]
    )
    if not common:
        return False
    if independent["outcome"] == "DECLARED_SEPARATOR_EXISTS":
        return bool(
            separator
            and separator["name"] == "I_one"
            and separator["separates_every_declared_pair"]
            and [row["delta"] for row in separator["values_on_separated_pairs"]]
            == independent["I_one_deltas"]
        )
    if independent["outcome"] == "DECLARED_READOUT_FAMILY_AGREES_ON_ALL_COMPARED_PAIRS":
        proof = visibility["analysis"]["nonseparation_proof"]
        return bool(
            separator is None
            and proof
            and proof["all_basis_functionals_equal_on_all_compared_pairs"] is True
        )
    return separator is None


def agreement_outcome_control(receipt: dict) -> bool:
    equal_pair_classes = [{
        "class": "synthetic equal-content fixture",
        "separated": [(0, (0,), (1,), 0, 0)],
    }]
    result = independent_readout_result(equal_pair_classes)
    synthetic = deepcopy(receipt)
    synthetic["findings"]["B_READOUT_VISIBILITY"]["analysis"] = {
        "outcome": "DECLARED_READOUT_FAMILY_AGREES_ON_ALL_COMPARED_PAIRS",
        "pair_count": 1,
        "visible_pair_count": 0,
        "pairs": [{
            "class": "synthetic equal-content fixture",
            "target_input": 0,
            "configuration_before": {"n": 0},
            "configuration_after": {"n": 1},
            "content_before": 0,
            "content_after": 0,
            "basis_readout_values": [
                {"readout": "I_zero", "before": 1, "after": 1, "delta": 0},
                {"readout": "I_one", "before": 0, "after": 0, "delta": 0},
            ],
        }],
        "nonseparation_proof": {
            "basis_dimension": 2,
            "all_basis_functionals_equal_on_all_compared_pairs": True,
            "span_argument": "synthetic checker fixture",
        },
    }
    synthetic["findings"]["B_READOUT_VISIBILITY"]["exact_separator"] = None
    broken = deepcopy(synthetic)
    broken["findings"]["B_READOUT_VISIBILITY"]["analysis"]["pairs"] = []
    return readout_agrees(synthetic, result) and not readout_agrees(broken, result)


def scope_agrees(receipt: dict) -> bool:
    scope = receipt["findings"]["C_SCOPE"]
    return bool(
        scope["binary_M2C_embedding_declared_not_unique"] is True
        and scope["point_mass_distribution_constructed_at_finite_cap"] is True
        and scope["target_input_fixed_per_conditioned_law"] is True
        and scope["full_mosaic_claimed"] is False
        and scope["formation_site_probability_or_rate_claimed"] is False
        and scope["selected_physical_readout_claimed"] is False
        and scope["born_weight_selection_claimed"] is False
        and scope["continuous_M2_probability_law_claimed"] is False
        and scope["infinite_simultaneous_translation_uniform_law_claimed"] is False
        and scope["generic_axiom_only_consequence_claimed"] is False
        and scope["record_collection_structure_claimed_as_axiom"] is False
    )


def record_boundary_agrees(receipt: dict, axiom: bytes) -> bool:
    observed = receipt["controls"]["current_record_boundary"]
    independent = current_record_boundary(axiom.decode())
    return bool(
        observed["pass"]
        and observed["required_sentences_present"]
        and observed["retired_collection_structure_absent"]
        and observed["declared_separator_is_extra_non_axiom_structure"]
        and independent["pass"]
    )


def active_corruption_probes(
    receipt: dict, independent: list[dict], cache: dict, payloads: dict[str, bytes]
) -> dict:
    probes = {}

    mutant = deepcopy(receipt)
    mutant["findings"]["A_LOCKED_CONTENT_CENSUS"]["classes"][0]["table"][0][
        "locked_content_by_target_input"
    ]["0"] = 1
    probes["locked_content_row"] = not compare_receipt(mutant, independent)

    mutant = deepcopy(receipt)
    mutant["findings"]["A_LOCKED_CONTENT_CENSUS"]["classes"][1]["J"] = 0
    probes["class_separator_J"] = not compare_receipt(mutant, independent)

    mutant = deepcopy(receipt)
    mutant["findings"]["B_READOUT_VISIBILITY"]["analysis"]["outcome"] = (
        "DECLARED_READOUT_FAMILY_AGREES_ON_ALL_COMPARED_PAIRS"
    )
    probes["visibility_outcome"] = not readout_agrees(
        mutant, independent_readout_result(independent)
    )

    mutant = deepcopy(receipt)
    mutant["findings"]["C_SCOPE"]["full_mosaic_claimed"] = True
    probes["mosaic_scope"] = scope_agrees(receipt) and not scope_agrees(mutant)

    mutant = deepcopy(receipt)
    mutant["findings"]["C_SCOPE"]["record_collection_structure_claimed_as_axiom"] = True
    probes["record_collection_authority"] = scope_agrees(receipt) and not scope_agrees(mutant)

    mutant = deepcopy(receipt)
    mutant["controls"]["current_record_boundary"]["retired_collection_structure_absent"] = False
    mutant["controls"]["current_record_boundary"]["pass"] = False
    probes["current_record_boundary"] = (
        record_boundary_agrees(receipt, payloads[AXIOM_PATH])
        and not record_boundary_agrees(mutant, payloads[AXIOM_PATH])
    )

    source_mutant = dict(payloads)
    source_mutant[PRIMARY_PATH] += b"\n"
    probes["source_pin"] = not primary_ast_and_pins(source_mutant)["source_pin_match"]

    note_mutant = dict(payloads)
    note_mutant[NOTE_PATH] += b"\n"
    probes["note_pin"] = not primary_ast_and_pins(note_mutant)["note_contract"]["sha_pin_match"]

    corrupted_stdout = cache["stdout"].replace(
        "DECLARED_SEPARATOR_EXISTS", "DECLARED_READOUT_FAMILY_AGREES"
    )
    probes["cached_headline"] = (
        sha256(corrupted_stdout.encode()).hexdigest() != EXPECTED_PRIMARY_STDOUT_SHA256
    )
    return probes


def render_stdout(receipt: dict) -> str:
    checks = receipt["checks"]
    lines = [
        "CYCLE985_NEIGHBOUR_DEPENDENCE_RECORD_CONTENT_INDEPENDENT_CHECK",
        "R0_PRIMARY_AST_AND_PINS " + ("PASS" if checks["R0_PRIMARY_AST_AND_PINS"] else "FAIL"),
        "R1_INDEPENDENT_CONTENT_CENSUS " + ("PASS" if checks["R1_INDEPENDENT_CONTENT_CENSUS"] else "FAIL")
        + f" :: classes={receipt['independent']['class_summary']}",
        "R2_INDEPENDENT_READOUT_DUAL " + ("PASS" if checks["R2_INDEPENDENT_READOUT_DUAL"] else "FAIL")
        + f" :: outcome={receipt['independent']['readout']['outcome']};"
        + f" pairs={receipt['independent']['readout']['pair_count']}",
        "R3_RECEIPT_CACHE_BINDING " + ("PASS" if checks["R3_RECEIPT_CACHE_BINDING"] else "FAIL"),
        "R4_ACTIVE_CORRUPTION_PROBES " + ("PASS" if checks["R4_ACTIVE_CORRUPTION_PROBES"] else "FAIL")
        + f" :: rejected={sum(receipt['corruption_probes'].values())}/{len(receipt['corruption_probes'])}",
        "R5_CONTROLS " + ("PASS" if checks["R5_CONTROLS"] else "FAIL")
        + f" :: source_reads={receipt['controls']['literal_source_read_count']}<=6;"
        + f" primary_executed={receipt['controls']['primary_imported_or_executed']};"
        + f" agreement_gate={receipt['controls']['synthetic_agreement_outcome_accepted']}",
        "VERDICT: " + (
            "PRIMARY_SURVIVES_INDEPENDENT_REFUTATION_ATTEMPT"
            if all(checks.values()) else "PRIMARY_DOES_NOT_SURVIVE_INDEPENDENT_REFUTATION_ATTEMPT"
        ),
    ]
    passed = sum(checks.values())
    lines.append(f"TOTAL: PASS={passed} FAIL={len(checks) - passed}")
    return "\n".join(lines) + "\n"


def run() -> tuple[dict, str]:
    started = monotonic()
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    primary_receipt = json.loads(payloads[PRIMARY_RECEIPT_PATH])
    cache = parse_cache(payloads[PRIMARY_CACHE_PATH].decode())
    ast_pins = primary_ast_and_pins(payloads)
    independent = independent_class_rows()
    readout = independent_readout_result(independent)
    probes = active_corruption_probes(primary_receipt, independent, cache, payloads)

    cache_fields = cache["fields"]
    cache_binding = bool(
        cache_fields.get("runner") == PRIMARY_PATH
        and cache_fields.get("runner_sha256") == EXPECTED_PRIMARY_SOURCE_SHA256
        and cache_fields.get("input_fingerprint_sha256")
        == EXPECTED_PRIMARY_INPUT_FINGERPRINT_SHA256
        and cache_fields.get("timeout_sec") == "300"
        and cache_fields.get("exit_code") == "0"
        and cache_fields.get("status") == "ok"
        and sha256(cache["stdout"].encode()).hexdigest() == EXPECTED_PRIMARY_STDOUT_SHA256
        and primary_receipt["stdout_sha256"] == EXPECTED_PRIMARY_STDOUT_SHA256
        and sha256(payloads[PRIMARY_RECEIPT_PATH]).hexdigest()
        == EXPECTED_PRIMARY_RECEIPT_SHA256
        and primary_receipt["primary_source_sha256"] == EXPECTED_PRIMARY_SOURCE_SHA256
    )
    runtime_budget_met = monotonic() - started < AUDIT_TIMEOUT_SEC
    controls = {
        "literal_audit_input_paths": list(AUDIT_INPUT_PATHS),
        "literal_source_read_count": len(AUDIT_INPUT_PATHS),
        "input_sha256": {
            path: sha256(payload).hexdigest() for path, payload in payloads.items()
        },
        "input_git_blobs": {
            path: git_blob(payload) for path, payload in payloads.items()
        },
        "primary_imported_or_executed": False,
        "synthetic_agreement_outcome_accepted": agreement_outcome_control(
            primary_receipt
        ),
        "runtime_budget_met": runtime_budget_met,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    }
    checks = {
        "R0_PRIMARY_AST_AND_PINS": bool(
            ast_pins["source_pin_match"]
            and ast_pins["primary_reads_only_axiom"]
            and ast_pins["primary_has_main_guard"]
            and ast_pins["review_base_matches"]
            and ast_pins["current_axiom_sha_pin_matches"]
            and ast_pins["current_axiom_blob_pin_matches"]
            and ast_pins["current_record_boundary"]["pass"]
            and ast_pins["note_contract"]["sha_pin_match"]
            and ast_pins["note_contract"]["required_boundary_present"]
            and ast_pins["note_contract"]["forbidden_authority_absent"]
        ),
        "R1_INDEPENDENT_CONTENT_CENSUS": bool(
            compare_receipt(primary_receipt, independent)
            and all(
                row["orbit_stabilizer_product"] == row["group_order"]
                and len(row["edges"])
                == (len(row["table"]).bit_length() - 1) * len(row["table"])
                for row in independent
            )
        ),
        "R2_INDEPENDENT_READOUT_DUAL": bool(
            readout_agrees(primary_receipt, readout)
            and record_boundary_agrees(primary_receipt, payloads[AXIOM_PATH])
        ),
        "R3_RECEIPT_CACHE_BINDING": cache_binding,
        "R4_ACTIVE_CORRUPTION_PROBES": all(probes.values()),
        "R5_CONTROLS": bool(
            len(AUDIT_INPUT_PATHS) <= 6
            and not controls["primary_imported_or_executed"]
            and controls["synthetic_agreement_outcome_accepted"]
            and runtime_budget_met
        ),
    }
    receipt = {
        "cycle": CYCLE,
        "artifact": "Cycle 985 independent record-content refutation attempt",
        "audit_status_authority": "independent audit lane only",
        "independent": {
            "class_summary": [
                [row["class"], row["orbit_size"], row["stabilizer"], row["J"], len(row["table"])]
                for row in independent
            ],
            "readout": readout,
            "reconstruction_digest": digest(independent),
        },
        "primary_ast_and_pins": ast_pins,
        "cache_semantic_fields": cache_fields,
        "corruption_probes": probes,
        "controls": controls,
        "checks": checks,
    }
    stdout = render_stdout(receipt)
    controls["stdout_bytes"] = len(stdout.encode())
    if controls["stdout_bytes"] >= STDOUT_LIMIT_BYTES:
        receipt["checks"]["R5_CONTROLS"] = False
        stdout = render_stdout(receipt)
        controls["stdout_bytes"] = len(stdout.encode())
    receipt["pass"] = all(receipt["checks"].values())
    receipt["checker_source_sha256"] = sha256(
        (ROOT / Path(__file__).relative_to(ROOT)).read_bytes()
    ).hexdigest()
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
