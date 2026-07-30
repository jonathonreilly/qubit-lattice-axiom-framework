#!/usr/bin/env python3
"""Clean-room and mutation checker for the truncated-fixture verifier.

The verifier and landed scientific scripts are never imported. The bounded
combinatorics is reconstructed with the standard library, and the verifier's
public classifier is exercised through subprocess JSON records.
"""

from __future__ import annotations

import ast
import copy
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from typing import Any


AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = "docs/TRUNCATED_FOCK_FIXTURE_VERIFIER_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "docs/TRUNCATED_FOCK_EQUAL_SPLIT_SUPPORT_NOTE_2026-07-28.md",
    "docs/TRUNCATED_FOCK_COMPONENT_NAMING_NOTE_2026-07-28.md",
    "scripts/frontier_truncated_fock_equal_split_support_2026_07_28.py",
    "scripts/frontier_truncated_fock_equal_split_independent_check_2026_07_28.py",
    "scripts/frontier_truncated_fock_fixture_verifier_2026_07_28.py",
)
CHECKER_KIND = "clean-room-stdlib-mutation"

ROOT = Path(__file__).resolve().parents[1]
VERIFIER_PATH = ROOT / "scripts/frontier_truncated_fock_fixture_verifier_2026_07_28.py"
SOURCE_PATH = ROOT / "scripts/frontier_truncated_fock_equal_split_support_2026_07_28.py"
SOURCE_SHA256 = "05853a493ddc083ba3a4f63f7d41d80b97e7d6d9a2b57be83145407fd5f501d0"
SOURCE_CHECKER_PATH = ROOT / "scripts/frontier_truncated_fock_equal_split_independent_check_2026_07_28.py"
SOURCE_CHECKER_SHA256 = "dd0f66f4b44008df5b38fe0d5908753caa3257f7528d868ad8705b1af39bcffc"

MODE_COUNT = 6
Q_DIMENSION = 7
OPPOSITE = (1, 0, 3, 2, 5, 4)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: Any = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_script(path: Path, args: tuple[str, ...] = (), stdin: str = "") -> dict[str, Any]:
    environment = dict(os.environ)
    scripts_path = str(ROOT / "scripts")
    inherited_pythonpath = environment.get("PYTHONPATH", "")
    environment["PYTHONPATH"] = (
        scripts_path
        if not inherited_pythonpath
        else scripts_path + os.pathsep + inherited_pythonpath
    )
    completed = subprocess.run(
        [sys.executable, str(path), *args],
        cwd=ROOT,
        env=environment,
        input=stdin,
        text=True,
        capture_output=True,
        check=False,
        timeout=180,
    )
    return {
        "returncode": completed.returncode,
        "stderr": completed.stderr,
        "stdout": completed.stdout,
    }


def literal_assignments(tree: ast.Module) -> dict[str, Any]:
    values: dict[str, Any] = {}
    for node in tree.body:
        name: str | None = None
        expression: ast.expr | None = None
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            if isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
                expression = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            name = node.target.id
            expression = node.value
        if name is None or expression is None:
            continue
        try:
            values[name] = ast.literal_eval(expression)
        except (TypeError, ValueError):
            pass
    return values


def inspect_verifier() -> dict[str, Any]:
    source = VERIFIER_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(VERIFIER_PATH))
    values = literal_assignments(tree)
    classifier = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "classify_record"
    ]
    classifier_args = (
        tuple(arg.arg for arg in classifier[0].args.args)
        if len(classifier) == 1
        else ()
    )
    forbidden_terms = (
        "frontier_full_fock_unit_weight_source_2026_07_28",
        "FullFockAcceptance",
        "ACCEPTANCE_SURFACE_REGISTRY",
        "C_source firewall",
        "source-lane ceiling",
    )
    return {
        "classifier_args": classifier_args,
        "expected_contract": values.get("EXPECTED_CONTRACT"),
        "forbidden_terms": [
            term for term in forbidden_terms if term in source
        ],
        "source_checker_path": values.get("SOURCE_CHECKER_PATH"),
        "source_checker_sha256": values.get("SOURCE_CHECKER_SHA256"),
        "source_path": values.get("SOURCE_PATH"),
        "source_sha256": values.get("SOURCE_SHA256"),
    }


def clean_room_contract() -> tuple[dict[str, Any], dict[str, Any]]:
    mask_counts = tuple(math.comb(MODE_COUNT, number) for number in range(7))
    channel_counts: list[int] = []
    for number in range(7):
        count = 0
        for occupied in itertools.combinations(range(MODE_COUNT), number):
            mask = sum(1 << mode for mode in occupied)
            for direction in range(MODE_COUNT):
                if (
                    (mask >> direction) & 1
                    and not (mask >> OPPOSITE[direction]) & 1
                ):
                    count += 1
        channel_counts.append(count)
    truncated_masks = sum(mask_counts[:3])
    truncated_columns = 2 * Q_DIMENSION * truncated_masks**2
    complete_columns = 2 * Q_DIMENSION * sum(mask_counts) ** 2
    theta = 0.8 * 3.0 * math.tan(0.15)
    anchor_weight = math.sin(theta) ** 2
    alpha_totals = {
        str(alpha): alpha + (2.0 - alpha)
        for alpha in (0.0, 0.25, 1.0, 1.7, 2.0, 3.0)
    }
    contract = {
        "certified_layers": [
            {"active_channels": channel_counts[number], "number": number}
            for number in range(3)
        ],
        "claim_scope": "two-cell n_left,n_right<=2 conditional bookkeeping support",
        "complete_columns": complete_columns,
        "complete_number_layers": list(range(7)),
        "component_labels": ["matter", "component_1", "component_2"],
        "component_labels_construct_degrees_of_freedom": False,
        "equal_split": {
            "status": "supplied_not_derived",
            "weights": [1.0, 1.0],
        },
        "full_fock_claim": False,
        "omitted_number_layers": [3, 4, 5, 6],
        "truncated_columns": truncated_columns,
    }
    detail = {
        "alpha_totals": alpha_totals,
        "anchor_weight": anchor_weight,
        "channel_counts": tuple(channel_counts),
        "mask_counts": mask_counts,
    }
    return contract, detail


def parse_final_json(stdout: str) -> tuple[dict[str, Any] | None, int]:
    rows: list[dict[str, Any]] = []
    for line in stdout.splitlines():
        if not line.startswith("FINAL_JSON "):
            continue
        try:
            value = json.loads(line.removeprefix("FINAL_JSON "))
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            rows.append(value)
    return (rows[0] if len(rows) == 1 else None, len(rows))


def parse_source_checker(stdout: str) -> tuple[dict[str, int] | None, str | None]:
    summary: dict[str, int] | None = None
    final: str | None = None
    for line in stdout.splitlines():
        if line.startswith("SUMMARY "):
            try:
                value = ast.literal_eval(line.removeprefix("SUMMARY "))
            except (SyntaxError, ValueError):
                continue
            if isinstance(value, dict):
                summary = {
                    "fail": value.get("fail"),
                    "pass": value.get("pass"),
                }
        elif line.startswith("FINAL "):
            final = line.removeprefix("FINAL ").strip()
    return summary, final


def classify_with(path: Path, record: dict[str, Any]) -> str:
    run = run_script(
        path,
        args=("--classify-json",),
        stdin=json.dumps(record, sort_keys=True),
    )
    if run["returncode"] != 0 or run["stderr"]:
        return "EXECUTION_ERROR"
    lines = [line.strip() for line in run["stdout"].splitlines() if line.strip()]
    return lines[0] if len(lines) == 1 else "MALFORMED_OUTPUT"


def classifier_matrix(
    path: Path, record: dict[str, Any]
) -> dict[str, str]:
    records: dict[str, dict[str, Any]] = {"canonical": record}

    promoted = copy.deepcopy(record)
    promoted["contract"]["full_fock_claim"] = True
    records["full_fock_promotion"] = promoted

    derived = copy.deepcopy(record)
    derived["contract"]["equal_split"]["status"] = "derived"
    records["derived_equal_split"] = derived

    labels = copy.deepcopy(record)
    labels["contract"]["component_labels"] = [
        "matter",
        "mediator",
        "auxiliary",
    ]
    labels["contract"]["component_labels_construct_degrees_of_freedom"] = True
    records["carrier_promotion"] = labels

    expanded = copy.deepcopy(record)
    expanded["contract"]["certified_layers"].append(
        {"active_channels": 36, "number": 3}
    )
    records["uncertified_layer"] = expanded

    drift = copy.deepcopy(record)
    drift["dependency_pins"]["source"]["actual"] = "0" * 64
    drift["dependency_pins"]["source"]["verified"] = False
    records["pin_drift"] = drift

    return {
        name: classify_with(path, candidate)
        for name, candidate in records.items()
    }


class AlwaysAccept(ast.NodeTransformer):
    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        self.generic_visit(node)
        if node.name == "classify_record":
            node.body = [
                ast.Return(value=ast.Constant(value="ACCEPT"))
            ]
        return node


def always_accept_mutation_is_caught(record: dict[str, Any]) -> dict[str, Any]:
    source = VERIFIER_PATH.read_text(encoding="utf-8")
    tree = ast.fix_missing_locations(AlwaysAccept().visit(ast.parse(source)))
    with tempfile.TemporaryDirectory(
        prefix="truncated_fixture_verifier_mutation_"
    ) as directory:
        mutant = Path(directory) / VERIFIER_PATH.name
        mutant.write_text(ast.unparse(tree) + "\n", encoding="utf-8")
        matrix = classifier_matrix(mutant, record)
    expected_mutant = {
        "canonical": "ACCEPT",
        "carrier_promotion": "ACCEPT",
        "derived_equal_split": "ACCEPT",
        "full_fock_promotion": "ACCEPT",
        "pin_drift": "ACCEPT",
        "uncertified_layer": "ACCEPT",
    }
    return {
        "caught": matrix == expected_mutant,
        "expected_mutant_matrix": expected_mutant,
        "mutant_matrix": matrix,
    }


def main() -> int:
    started = time.monotonic()
    inspection = inspect_verifier()
    clean_contract, math_detail = clean_room_contract()
    check(
        "the verifier has fixed current-main dependencies and no caller oracle",
        (
            inspection["source_path"]
            == "scripts/frontier_truncated_fock_equal_split_support_2026_07_28.py"
            and inspection["source_sha256"] == SOURCE_SHA256
            and inspection["source_checker_path"]
            == "scripts/frontier_truncated_fock_equal_split_independent_check_2026_07_28.py"
            and inspection["source_checker_sha256"] == SOURCE_CHECKER_SHA256
            and inspection["classifier_args"] == ("record",)
            and not inspection["forbidden_terms"]
            and inspection["expected_contract"] == clean_contract
        ),
        inspection,
    )

    check(
        "clean-room enumeration distinguishes the bounded slice from full Fock space",
        (
            math_detail["mask_counts"] == (1, 6, 15, 20, 15, 6, 1)
            and math_detail["channel_counts"] == (0, 6, 24, 36, 24, 6, 0)
            and clean_contract["truncated_columns"] == 6776
            and clean_contract["complete_columns"] == 57344
            and all(value == 2.0 for value in math_detail["alpha_totals"].values())
            and abs(
                math_detail["anchor_weight"] - 0.12589921612871377
            )
            < 3e-10
        ),
        math_detail,
    )

    source_run = run_script(SOURCE_PATH)
    source_terminal, source_terminal_count = parse_final_json(
        source_run["stdout"]
    )
    source_checker_run = run_script(SOURCE_CHECKER_PATH)
    source_checker_summary, source_checker_final = parse_source_checker(
        source_checker_run["stdout"]
    )
    check(
        "the repaired bounded source and its checker rerun directly",
        (
            sha256(SOURCE_PATH) == SOURCE_SHA256
            and sha256(SOURCE_CHECKER_PATH) == SOURCE_CHECKER_SHA256
            and source_run["returncode"] == 0
            and source_run["stderr"] == ""
            and source_terminal_count == 1
            and source_terminal is not None
            and source_terminal.get("summary") == {"fail": 0, "pass": 10}
            and source_terminal.get("full_fock_claim") is False
            and source_checker_run["returncode"] == 0
            and source_checker_run["stderr"] == ""
            and source_checker_summary == {"fail": 0, "pass": 7}
            and source_checker_final == "ALL_PASS"
        ),
        {
            "source_summary": (
                source_terminal.get("summary") if source_terminal else None
            ),
            "source_checker_final": source_checker_final,
            "source_checker_summary": source_checker_summary,
        },
    )

    verifier_run = run_script(VERIFIER_PATH)
    verifier_final, verifier_final_count = parse_final_json(
        verifier_run["stdout"]
    )
    record = (
        verifier_final.get("record")
        if isinstance(verifier_final, dict)
        else None
    )
    check(
        "the live verifier emits one accepted bounded record",
        (
            verifier_run["returncode"] == 0
            and verifier_run["stderr"] == ""
            and verifier_final_count == 1
            and isinstance(verifier_final, dict)
            and verifier_final.get("checks") == {"fail": 0, "pass": 5}
            and verifier_final.get("verdict") == "ACCEPT"
            and isinstance(record, dict)
            and record.get("contract") == clean_contract
        ),
        {
            "final_count": verifier_final_count,
            "returncode": verifier_run["returncode"],
            "verdict": (
                verifier_final.get("verdict")
                if isinstance(verifier_final, dict)
                else None
            ),
        },
    )

    matrix = classifier_matrix(VERIFIER_PATH, record or {})
    expected_matrix = {
        "canonical": "ACCEPT",
        "carrier_promotion": "REJECT",
        "derived_equal_split": "REJECT",
        "full_fock_promotion": "REJECT",
        "pin_drift": "DRIFT",
        "uncertified_layer": "REJECT",
    }
    check(
        "the public classifier rejects every scope and interpretation mutation",
        matrix == expected_matrix,
        matrix,
    )

    mutation = always_accept_mutation_is_caught(record or {})
    check(
        "the checker executes and distinguishes an always-accept classifier mutation",
        mutation["caught"] is True,
        mutation,
    )

    runtime = time.monotonic() - started
    print(
        "SUMMARY",
        {"pass": PASS, "fail": FAIL, "runtime_seconds": round(runtime, 6)},
    )
    print("FINAL", "ALL_PASS" if FAIL == 0 else "HONEST_FAIL")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
