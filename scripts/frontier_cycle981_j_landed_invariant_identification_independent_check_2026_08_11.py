#!/usr/bin/env python3
"""Independent refutation checker for the Cycle-981 J identification census.

The checker imports and executes neither the primary nor the pinned Cycle-980
substrate.  It parses the primary as inert text/AST, independently rebuilds the
21-word value table with signed-axis counts, validates the primary receipt and
cache, checks the note boundary, and applies active corruptions from REFUTE_SPEC.
"""

from __future__ import annotations

import ast
import copy
import json
import sys
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
CYCLE = 981
AUDIT_TIMEOUT_SEC = 300
HOUSE_STDOUT_LIMIT_BYTES = 6_000
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle981_j_landed_invariant_identification_2026_08_11.py",
    "outputs/j_landed_invariant_identification_cycle981_receipt_2026_08_11.json",
    "logs/runner-cache/frontier_cycle981_j_landed_invariant_identification_2026_08_11.txt",
    "docs/J_LANDED_INVARIANT_IDENTIFICATION_CYCLE981_BOUNDED_THEOREM_NOTE_2026-08-11.md",
)
EXPECTED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]: "4b0b371bdf48ff512da4485385d5f52d9a40b7365414f8456b39271f00c4e524",
    AUDIT_INPUT_PATHS[3]: "7161d4baccac6ea74759b3daa325d06e63d641a46e3d88712b6fc3bc4d3d4a40",
}
EXPECTED_MAIN_PIN = "ea0968c71ad46c39c6dacb39f88a18780363b71f"
EXPECTED_CYCLE980_PIN = "c186c8ba7f44f2245cf38e59fc429ce90a6e0d7d"
EXPECTED_CANDIDATE_IDS = (
    "cycle980_control_arity",
    "cycle980_off_diagonal_control_gram_sum",
    "cycle719_controller_b_rail_occupation_sum",
    "cycle719_two_rail_token_total",
    "oh_star_shell_leverage",
    "cycle732_cell_adjacency_cost",
    "cycle732_cover_certificate_parity",
    "cycle733_column_subset_cost_parity_law",
    "cycle735_piece_borne_gf2_charge",
)
EXPECTED_PRIMARY_FUNCTIONS = (
    "pinned_source_controls",
    "declared_witnesses",
    "witness_values",
    "candidate_inventory",
    "compare_candidates",
    "science_measurement",
    "identification_bookkeeping",
    "verdict_bookkeeping",
)
CHECKER_PATH = (
    "scripts/frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.py"
)
RECEIPT_PATH = (
    "outputs/j_landed_invariant_identification_cycle981_independent_check_receipt_2026_08_11.json"
)

REFUTE_SPEC = (
    {"id": "SOURCE_PIN_CHANGED", "target": "A", "mutation": "replace the pinned main snapshot"},
    {"id": "CANDIDATE_REMOVED", "target": "A", "mutation": "remove one extracted candidate"},
    {"id": "LANDED_FLAG_FLIPPED", "target": "A", "mutation": "mark a main candidate non-landed"},
    {"id": "FIRST_WITNESS_CORRUPTED", "target": "B", "mutation": "replace the first arity disagreement"},
    {"id": "NOT_COMPARABLE_PROMOTED", "target": "B", "mutation": "promote a domain mismatch to coincidence"},
    {"id": "ABSENT_SURFACE_FLIPPED", "target": "A", "mutation": "claim an absent Cycle-736 path is present"},
    {"id": "EXACT_J_HIT_INJECTED", "target": "A", "mutation": "inject a false landed exact-formula hit"},
    {"id": "VERDICT_FLIPPED", "target": "C", "mutation": "replace landed-new by coincidence"},
    {"id": "CACHE_OUTCOME_CORRUPTED", "target": "R3", "mutation": "replace the cache outcome counts"},
)

AXES = (("+x", 0, 1), ("-x", 0, -1), ("+y", 1, 1), ("-y", 1, -1), ("+z", 2, 1), ("-z", 2, -1))
WITNESS_SCHEMA = "target-centred-radius-one-gate-word"


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


def ast_assignment_node(tree: ast.Module, name: str) -> ast.AST:
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            return node.value
    raise KeyError(name)


def independent_words() -> tuple[dict, ...]:
    rows = []
    for name, axis, sign in AXES:
        rows.append({"name": f"CNOT({name}->C)", "kind": "CNOT", "controls": ((axis, sign),)})
    for left, right in combinations(AXES, 2):
        rows.append({
            "name": f"TOF({left[0]},{right[0]}->C)",
            "kind": "TOF",
            "controls": ((left[1], left[2]), (right[1], right[2])),
        })
    return tuple(rows)


def independent_values(row: dict) -> dict[str, int]:
    signed_counts = [0, 0, 0]
    for axis, sign in row["controls"]:
        signed_counts[axis] += sign
    j_value = sum(value * value for value in signed_counts)
    gram_sum = 0
    for left, right in combinations(row["controls"], 2):
        gram_sum += left[1] * right[1] if left[0] == right[0] else 0
    return {
        "J": j_value,
        "control_arity": len(row["controls"]),
        "off_diagonal_control_gram_sum": gram_sum,
    }


def independent_orbit_table() -> list[dict]:
    grouped = {}
    for row in independent_words():
        values = independent_values(row)
        key = (row["kind"], values["J"])
        grouped.setdefault(key, {"count": 0, "values": values})["count"] += 1
    labels = {
        ("CNOT", 1): "CNOT",
        ("TOF", 2): "TOF_PERPENDICULAR_CONTROLS",
        ("TOF", 0): "TOF_OPPOSITE_CONTROLS",
    }
    return [
        {"class": labels[key], "member_count": grouped[key]["count"], **grouped[key]["values"]}
        for key in sorted(grouped, key=lambda item: (item[0], -item[1]))
    ]


def independent_tests(primary_candidates: list[dict]) -> list[dict]:
    values = [(row["name"], independent_values(row)) for row in independent_words()]
    same_domain_keys = {
        "cycle980_control_arity": "control_arity",
        "cycle980_off_diagonal_control_gram_sum": "off_diagonal_control_gram_sum",
    }
    tests = []
    for candidate in primary_candidates:
        row = {
            "candidate_id": candidate["candidate_id"],
            "landed_at_pinned_main": candidate["landed_at_pinned_main"],
            "candidate_domain_schema": candidate["domain_schema"],
            "J_domain_schema": WITNESS_SCHEMA,
            "normalization": candidate["normalization"],
        }
        key = same_domain_keys.get(candidate["candidate_id"])
        if candidate["domain_schema"] != WITNESS_SCHEMA:
            row.update({
                "outcome": "NOT_COMPARABLE",
                "reason": (
                    f"domain/type mismatch: {candidate['domain_schema']} -> "
                    f"{candidate['codomain']}, not {WITNESS_SCHEMA} -> integer"
                ),
                "shared_input_count": 0,
            })
        else:
            table = [
                {"word": name, "J": item["J"], "candidate": item[key]}
                for name, item in values
            ]
            mismatches = [item for item in table if item["J"] != item["candidate"]]
            row.update({
                "outcome": "DISAGREES" if mismatches else "COINCIDES",
                "shared_input_count": len(table),
                "agreement_count": len(table) - len(mismatches),
                "first_witness": mismatches[0] if mismatches else None,
                "exact_agreement_table": table if not mismatches else None,
            })
        tests.append(row)
    return tests


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


def source_controls() -> dict:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    sha_rows = {path: sha256(payload).hexdigest() for path, payload in payloads.items()}
    primary_text = payloads[AUDIT_INPUT_PATHS[0]].decode()
    primary_tree = ast.parse(primary_text, filename=AUDIT_INPUT_PATHS[0])
    functions = {node.name for node in primary_tree.body if isinstance(node, ast.FunctionDef)}
    imports = {
        alias.name for node in ast.walk(primary_tree) if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module for node in ast.walk(primary_tree)
        if isinstance(node, ast.ImportFrom) and node.module
    }
    return {
        "literal_source_read_count": len(AUDIT_INPUT_PATHS),
        "literal_audit_input_paths": list(AUDIT_INPUT_PATHS),
        "all_inputs_relative_and_present": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "input_sha256": sha_rows,
        "sha_pins_match": all(
            sha_rows.get(path) == expected for path, expected in EXPECTED_INPUT_SHA256.items()
        ),
        "primary_text": primary_text,
        "primary_tree": primary_tree,
        "primary_receipt": json.loads(payloads[AUDIT_INPUT_PATHS[1]]),
        "primary_cache": payloads[AUDIT_INPUT_PATHS[2]].decode(),
        "note_text": payloads[AUDIT_INPUT_PATHS[3]].decode(),
        "primary_functions_present": all(name in functions for name in EXPECTED_PRIMARY_FUNCTIONS),
        "primary_main_pin": ast_literal_assignment(primary_tree, "PINNED_MAIN_COMMIT"),
        "primary_cycle980_pin": ast_literal_assignment(primary_tree, "PINNED_CYCLE980_COMMIT"),
        "primary_source_read_count": len(
            ast_assignment_node(primary_tree, "PINNED_SOURCE_READS").elts
        ),
        "primary_requested_absent_paths": ast_literal_assignment(primary_tree, "REQUESTED_BUT_UNLANDED_PATHS"),
        "primary_imports": sorted(imports),
        "primary_imported_or_executed": False,
    }


def validate_primary(receipt: dict) -> bool:
    findings = receipt.get("findings", {})
    candidates = findings.get("candidate_inventory", [])
    tests = findings.get("identification_tests", [])
    return bool(
        receipt.get("primary_source_sha256") == EXPECTED_INPUT_SHA256[AUDIT_INPUT_PATHS[0]]
        and receipt.get("science_digest") == digest(findings)
        and receipt.get("pass") is True and all(receipt.get("checks", {}).values())
        and findings.get("search_design", {}).get("snapshot") == EXPECTED_MAIN_PIN
        and findings.get("search_design", {}).get("body_read_count") == 6
        and findings.get("search_design", {}).get("exact_J_formula_hit_paths") == []
        and tuple(row.get("candidate_id") for row in candidates) == EXPECTED_CANDIDATE_IDS
        and len(tests) == len(EXPECTED_CANDIDATE_IDS)
        and tests == independent_tests(candidates)
        and findings.get("witness_count") == 21
        and findings.get("orbit_value_table") == independent_orbit_table()
        and not any(findings.get("requested_surface_presence_at_pin", {}).values())
        and findings.get("coincident_landed_candidates") == []
        and findings.get("verdict") == "LANDED_NEW_WITHIN_DECLARED_SEARCH"
        and findings.get("physics_identification_established") is False
    )


def validate_cache(cache: str, receipt: dict) -> bool:
    headers, body, stderr = parse_cache(cache)
    normalized = body.rstrip() + "\n"
    expected_outcomes = compact({"COINCIDES": 0, "DISAGREES": 2, "NOT_COMPARABLE": 7})
    return bool(
        headers.get("runner") == AUDIT_INPUT_PATHS[0]
        and headers.get("runner_sha256") == EXPECTED_INPUT_SHA256[AUDIT_INPUT_PATHS[0]]
        and headers.get("timeout_sec") == "300"
        and headers.get("exit_code") == "0" and headers.get("status") == "ok"
        and not stderr.strip()
        and receipt.get("stdout_sha256") == sha256(normalized.encode()).hexdigest()
        and "exact_J_hits=0" in body
        and f"outcomes={expected_outcomes}" in body
        and "LANDED_NEW_WITHIN_DECLARED_SEARCH" in body
        and body.rstrip().endswith("TOTAL: PASS=4 FAIL=0")
    )


def validate_note(note: str) -> bool:
    required = (
        "Claim type: `bounded_theorem`",
        "actual_current_surface_status: bounded-support",
        "**`J` is landed-new**",
        "TOF(+x,-x->C)",
        "CNOT(+x->C)",
        "`NOT_COMPARABLE`",
        EXPECTED_MAIN_PIN,
        EXPECTED_CYCLE980_PIN,
        "identify two functions on this finite shared domain only",
        "Audit-status authority: independent audit lane only",
    )
    forbidden = ("audited_clean", "audit_status: retained", "bare_retained_allowed: true")
    return all(token in note for token in required) and not any(token in note for token in forbidden)


def corruption_probes(receipt: dict, cache: str) -> dict:
    results = {}
    original_valid = validate_primary(receipt)

    def rejected(mutated: dict) -> bool:
        return original_valid and mutated != receipt and not validate_primary(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["findings"]["search_design"]["snapshot"] = "0" * 40
    results["SOURCE_PIN_CHANGED"] = rejected(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["findings"]["candidate_inventory"].pop()
    results["CANDIDATE_REMOVED"] = rejected(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["findings"]["candidate_inventory"][2]["landed_at_pinned_main"] = False
    results["LANDED_FLAG_FLIPPED"] = rejected(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["findings"]["identification_tests"][0]["first_witness"]["J"] = 1
    results["FIRST_WITNESS_CORRUPTED"] = rejected(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["findings"]["identification_tests"][2]["outcome"] = "COINCIDES"
    results["NOT_COMPARABLE_PROMOTED"] = rejected(mutated)

    mutated = copy.deepcopy(receipt)
    first_path = next(iter(mutated["findings"]["requested_surface_presence_at_pin"]))
    mutated["findings"]["requested_surface_presence_at_pin"][first_path] = True
    results["ABSENT_SURFACE_FLIPPED"] = rejected(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["findings"]["search_design"]["exact_J_formula_hit_paths"] = ["docs/FALSE.md"]
    results["EXACT_J_HIT_INJECTED"] = rejected(mutated)

    mutated = copy.deepcopy(receipt)
    mutated["findings"]["verdict"] = "COINCIDES_WITH_LANDED_CANDIDATE"
    results["VERDICT_FLIPPED"] = rejected(mutated)

    original = 'outcomes={"COINCIDES":0,"DISAGREES":2,"NOT_COMPARABLE":7}'
    changed = 'outcomes={"COINCIDES":1,"DISAGREES":1,"NOT_COMPARABLE":7}'
    mutated_cache = cache.replace(original, changed, 1)
    results["CACHE_OUTCOME_CORRUPTED"] = bool(
        validate_cache(cache, receipt) and mutated_cache != cache
        and not validate_cache(mutated_cache, receipt)
    )
    return {
        "refute_spec": list(REFUTE_SPEC),
        "results": results,
        "all_rejected": set(results) == {row["id"] for row in REFUTE_SPEC}
        and all(results.values()),
    }


def render_stdout(receipt: dict) -> str:
    checks = receipt["checks"]
    probes = receipt["active_corruption_probes"]
    independent = receipt["independent_measurement"]
    rows = [
        "CYCLE981_J_LANDED_INVARIANT_IDENTIFICATION_INDEPENDENT_CHECK",
        "R0_PRIMARY_AST_TEXT_AND_PINS " + ("PASS" if checks["R0_PRIMARY_AST_TEXT_AND_PINS"] else "FAIL")
        + f" :: reads={receipt['controls']['literal_source_read_count']}<=6;"
        + f" sha_pins={receipt['controls']['sha_pins_match']}; primary_executed=false",
        "R1_INDEPENDENT_SHARED_INPUTS " + ("PASS" if checks["R1_INDEPENDENT_SHARED_INPUTS"] else "FAIL")
        + f" :: witnesses={independent['witness_count']}; orbit_table={compact(independent['orbit_value_table'])}",
        "R2_CANDIDATE_OUTCOMES " + ("PASS" if checks["R2_CANDIDATE_OUTCOMES"] else "FAIL")
        + f" :: outcomes={compact(independent['outcome_counts'])}; verdict={independent['verdict']}",
        "R3_RECEIPT_CACHE_NOTE_BINDING " + ("PASS" if checks["R3_RECEIPT_CACHE_NOTE_BINDING"] else "FAIL")
        + f" :: bound={checks['R3_RECEIPT_CACHE_NOTE_BINDING']}",
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
    primary_receipt = controls["primary_receipt"]
    primary_cache = controls["primary_cache"]
    candidates = primary_receipt["findings"]["candidate_inventory"]

    def independent_measurement() -> dict:
        tests = independent_tests(candidates)
        return {
            "witness_count": len(independent_words()),
            "orbit_value_table": independent_orbit_table(),
            "identification_tests": tests,
            "outcome_counts": {
                outcome: sum(row["outcome"] == outcome for row in tests)
                for outcome in ("COINCIDES", "DISAGREES", "NOT_COMPARABLE")
            },
            "verdict": "COINCIDES_WITH_LANDED_CANDIDATE" if any(
                row["landed_at_pinned_main"] and row["outcome"] == "COINCIDES"
                for row in tests
            ) else "LANDED_NEW_WITHIN_DECLARED_SEARCH",
        }

    first = independent_measurement()
    second = independent_measurement()
    deterministic = first == second
    r0 = bool(
        controls["literal_source_read_count"] <= 6
        and controls["all_inputs_relative_and_present"] and controls["sha_pins_match"]
        and controls["primary_functions_present"]
        and controls["primary_main_pin"] == EXPECTED_MAIN_PIN
        and controls["primary_cycle980_pin"] == EXPECTED_CYCLE980_PIN
        and controls["primary_source_read_count"] == 6
        and len(controls["primary_requested_absent_paths"]) == 6
        and controls["primary_imported_or_executed"] is False
    )
    r1 = bool(
        first["witness_count"] == 21
        and [row["member_count"] for row in first["orbit_value_table"]] == [6, 12, 3]
    )
    r2 = validate_primary(primary_receipt)
    r3 = bool(
        validate_cache(primary_cache, primary_receipt)
        and validate_note(controls["note_text"])
    )
    probes = corruption_probes(primary_receipt, primary_cache)
    r4 = probes["all_rejected"]
    controls = {
        key: value for key, value in controls.items()
        if key not in {"primary_text", "primary_tree", "primary_receipt", "primary_cache", "note_text"}
    }
    controls.update({
        "determinism_replay": deterministic,
        "runtime_seconds": monotonic() - started,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
        "house_stdout_limit_bytes": HOUSE_STDOUT_LIMIT_BYTES,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_bytes": 0,
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
            "R1_INDEPENDENT_SHARED_INPUTS": r1,
            "R2_CANDIDATE_OUTCOMES": r2,
            "R3_RECEIPT_CACHE_NOTE_BINDING": r3,
            "R4_ACTIVE_CORRUPTION_PROBES": r4,
            "R5_CONTROLS": False,
        },
    }
    for _ in range(3):
        stdout = render_stdout(receipt)
        controls["stdout_bytes"] = len(stdout.encode())
    stdout = render_stdout(receipt)
    receipt["checks"]["R5_CONTROLS"] = bool(
        deterministic and controls["runtime_seconds"] < AUDIT_TIMEOUT_SEC
        and len(stdout.encode()) < HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
    )
    controls["stdout_bytes"] = len(stdout.encode())
    stdout = render_stdout(receipt)
    receipt["pass"] = all(receipt["checks"].values())
    receipt["checker_source_sha256"] = sha256((ROOT / CHECKER_PATH).read_bytes()).hexdigest()
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
