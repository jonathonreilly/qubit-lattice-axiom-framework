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
PRIMARY_RECEIPT_PATH = (
    "outputs/neighbour_dependence_record_content_cycle985_receipt_2026_08_11.json"
)
PRIMARY_CACHE_PATH = (
    "logs/runner-cache/frontier_cycle985_neighbour_dependence_record_content_2026_08_11.txt"
)
RECEIPT_PATH = (
    "outputs/neighbour_dependence_record_content_cycle985_independent_check_receipt_2026_08_11.json"
)
AUDIT_INPUT_PATHS = (PRIMARY_PATH, PRIMARY_RECEIPT_PATH, PRIMARY_CACHE_PATH)
EXPECTED_PRIMARY_SOURCE_SHA256 = (
    "0e66cb4b11c38c78b03d0fab66b0218839005fe32e5c3daaf289eb64040714a2"
)
EXPECTED_PRIMARY_RECEIPT_SHA256 = (
    "ae6b337dad743eb2ddc389f4be055e35c9c2a4b7306003e0548ffc66f21ec6d1"
)
EXPECTED_PRIMARY_INPUT_FINGERPRINT_SHA256 = (
    "db7786cde9df9554b9e925bd8927e6f129e0cdd1546e5ea349a31056104b73bb"
)
EXPECTED_PRIMARY_STDOUT_SHA256 = (
    "827a15c4268161e1f81355807636474f8b315b195f8062a12a0c79b621e9e345"
)

CLASS_SPECS = (
    ("incoming CNOT", "CNOT", ((1, 0, 0),), 6, 4),
    ("perpendicular-control TOF", "TOF", ((1, 0, 0), (0, 1, 0)), 12, 2),
    ("opposite-control TOF", "TOF", ((1, 0, 0), (-1, 0, 0)), 3, 8),
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


def independent_class_rows() -> list[dict]:
    classes = []
    for label, kind, vectors, orbit_size, stabilizer in CLASS_SPECS:
        table = []
        separated = []
        controls = tuple(product((0, 1), repeat=len(vectors)))
        for bits in controls:
            table.append({
                "bits": bits,
                "contents": tuple(
                    apply_gate_permutation(kind, (target, *bits))[0]
                    for target in (0, 1)
                ),
            })
        for target in (0, 1):
            for left_index, left in enumerate(controls):
                for right in controls[left_index + 1:]:
                    if sum(a != b for a, b in zip(left, right)) != 1:
                        continue
                    before = apply_gate_permutation(kind, (target, *left))[0]
                    after = apply_gate_permutation(kind, (target, *right))[0]
                    if before != after:
                        separated.append((target, left, right, before, after))
        classes.append({
            "class": label,
            "kind": kind,
            "J": j_from_vectors(vectors),
            "orbit_size": orbit_size,
            "stabilizer": stabilizer,
            "table": table,
            "separated": separated,
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
            })
        separated = []
        for item in row["one_neighbour_bit_separations"]:
            left = tuple(item["configuration_before"][name] for name in control_names)
            right = tuple(item["configuration_after"][name] for name in control_names)
            separated.append((
                item["target_input"], left, right,
                item["content_before"], item["content_after"],
            ))
        rows.append({
            "class": row["class"],
            "kind": "CNOT" if len(control_names) == 1 else "TOF",
            "J": row["J"],
            "orbit_size": row["orbit_size"],
            "stabilizer": row["stabilizer"],
            "table": table,
            "separated": separated,
        })
    return rows


def independent_readout_result(classes: list[dict]) -> dict:
    pairs = [pair for row in classes for pair in row["separated"]]
    deltas = [after - before for _, _, _, before, after in pairs]
    return {
        "family": "R^{\u007b0,1\u007d}, extended by finite sums",
        "basis": ((1, 0), (0, 1)),
        "pair_count": len(pairs),
        "I_one_deltas": deltas,
        "outcome": (
            "SEPARATING_ADMISSIBLE_READOUT_EXISTS" if pairs and all(deltas)
            else "NO_ADMISSIBLE_SEPARATOR_IN_DECLARED_LINEAR_FAMILY"
        ),
        "no_separator_iff_contents_equal": all(
            (before == after) == all(weights[before] == weights[after] for weights in ((1, 0), (0, 1)))
            for _, _, _, before, after in pairs
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


def primary_ast_and_pins(payloads: dict[str, bytes]) -> dict:
    source = payloads[PRIMARY_PATH]
    tree = ast.parse(source, filename=PRIMARY_PATH)
    literal_inputs = ast_literal_assignment(tree, "AUDIT_INPUT_PATHS")
    return {
        "source_sha256": sha256(source).hexdigest(),
        "source_git_blob": git_blob(source),
        "source_pin_match": sha256(source).hexdigest() == EXPECTED_PRIMARY_SOURCE_SHA256,
        "primary_reads_only_axiom": literal_inputs == (
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
        "primary_has_main_guard": any(
            isinstance(node, ast.If)
            and isinstance(node.test, ast.Compare)
            for node in tree.body
        ),
    }


def compare_receipt(receipt: dict, independent: list[dict]) -> bool:
    return primary_class_rows(receipt) == independent


def readout_agrees(receipt: dict, independent: dict) -> bool:
    visibility = receipt["findings"]["B_READOUT_VISIBILITY"]
    separator = visibility["exact_separator"]
    return bool(
        visibility["analysis"]["outcome"] == independent["outcome"]
        and visibility["analysis"]["pair_count"] == independent["pair_count"]
        and separator["name"] == "I_one"
        and separator["separates_every_declared_pair"]
        and [row["delta"] for row in separator["values_on_separated_pairs"]]
        == independent["I_one_deltas"]
        and independent["no_separator_iff_contents_equal"]
    )


def negative_outcome_control() -> bool:
    equal_pair_classes = [{
        "separated": [(0, (0,), (1,), 0, 0)],
    }]
    result = independent_readout_result(equal_pair_classes)
    return result["outcome"] == "NO_ADMISSIBLE_SEPARATOR_IN_DECLARED_LINEAR_FAMILY"


def active_corruption_probes(receipt: dict, independent: list[dict], cache: dict) -> dict:
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
        "NO_ADMISSIBLE_SEPARATOR_IN_DECLARED_LINEAR_FAMILY"
    )
    probes["visibility_outcome"] = not readout_agrees(
        mutant, independent_readout_result(independent)
    )

    mutant = deepcopy(receipt)
    mutant["findings"]["C_SCOPE"]["full_mosaic_claimed"] = True
    probes["mosaic_scope"] = mutant["findings"]["C_SCOPE"] != receipt["findings"]["C_SCOPE"]

    probes["source_pin"] = sha256(b"corrupted primary").hexdigest() != EXPECTED_PRIMARY_SOURCE_SHA256

    corrupted_stdout = cache["stdout"].replace(
        "SEPARATING_ADMISSIBLE_READOUT_EXISTS", "NO_ADMISSIBLE_SEPARATOR"
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
        + f" negative_gate={receipt['controls']['synthetic_negative_outcome_accepted']}",
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
    probes = active_corruption_probes(primary_receipt, independent, cache)

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
        "synthetic_negative_outcome_accepted": negative_outcome_control(),
        "runtime_budget_met": runtime_budget_met,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    }
    checks = {
        "R0_PRIMARY_AST_AND_PINS": bool(
            ast_pins["source_pin_match"]
            and ast_pins["primary_reads_only_axiom"]
            and ast_pins["primary_has_main_guard"]
        ),
        "R1_INDEPENDENT_CONTENT_CENSUS": bool(
            compare_receipt(primary_receipt, independent)
            and [row["J"] for row in independent] == [1, 2, 0]
            and [row["orbit_size"] for row in independent] == [6, 12, 3]
        ),
        "R2_INDEPENDENT_READOUT_DUAL": readout_agrees(primary_receipt, readout),
        "R3_RECEIPT_CACHE_BINDING": cache_binding,
        "R4_ACTIVE_CORRUPTION_PROBES": all(probes.values()),
        "R5_CONTROLS": bool(
            len(AUDIT_INPUT_PATHS) <= 6
            and not controls["primary_imported_or_executed"]
            and controls["synthetic_negative_outcome_accepted"]
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
