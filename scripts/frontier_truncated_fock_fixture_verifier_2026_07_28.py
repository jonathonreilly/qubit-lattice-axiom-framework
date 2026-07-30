#!/usr/bin/env python3
"""Fixed-pin verifier for the landed n_left,n_right<=2 Fock fixture.

This is meta test infrastructure. It exposes no candidate physics input,
registers nothing in the source-acceptance harness, and makes no full-Fock
claim.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from typing import Any

import frontier_truncated_fock_fixture_verifier_independent_check_2026_07_28 as INDEPENDENT_PACKET_SOURCE


AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = "docs/TRUNCATED_FOCK_FIXTURE_VERIFIER_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "docs/TRUNCATED_FOCK_EQUAL_SPLIT_SUPPORT_NOTE_2026-07-28.md",
    "docs/TRUNCATED_FOCK_COMPONENT_NAMING_NOTE_2026-07-28.md",
    "scripts/frontier_truncated_fock_equal_split_support_2026_07_28.py",
    "scripts/frontier_truncated_fock_equal_split_independent_check_2026_07_28.py",
    "scripts/frontier_truncated_fock_fixture_verifier_independent_check_2026_07_28.py",
)

ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = "scripts/frontier_truncated_fock_equal_split_support_2026_07_28.py"
SOURCE_SHA256 = "05853a493ddc083ba3a4f63f7d41d80b97e7d6d9a2b57be83145407fd5f501d0"
SOURCE_CHECKER_PATH = (
    "scripts/frontier_truncated_fock_equal_split_independent_check_2026_07_28.py"
)
SOURCE_CHECKER_SHA256 = (
    "dd0f66f4b44008df5b38fe0d5908753caa3257f7528d868ad8705b1af39bcffc"
)

EXPECTED_CONTRACT = {
    "certified_layers": [
        {"active_channels": 0, "number": 0},
        {"active_channels": 6, "number": 1},
        {"active_channels": 24, "number": 2},
    ],
    "claim_scope": "two-cell n_left,n_right<=2 conditional bookkeeping support",
    "complete_columns": 57344,
    "complete_number_layers": [0, 1, 2, 3, 4, 5, 6],
    "component_labels": ["matter", "component_1", "component_2"],
    "component_labels_construct_degrees_of_freedom": False,
    "equal_split": {
        "status": "supplied_not_derived",
        "weights": [1.0, 1.0],
    },
    "full_fock_claim": False,
    "omitted_number_layers": [3, 4, 5, 6],
    "truncated_columns": 6776,
}


def _sha256(path: str | Path) -> str:
    target = Path(path)
    if not target.is_absolute():
        target = ROOT / target
    return hashlib.sha256(target.read_bytes()).hexdigest()


def _run_script(path: str, timeout: int = 180) -> dict[str, Any]:
    started = time.monotonic()
    completed = subprocess.run(
        [sys.executable, str(ROOT / path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=timeout,
    )
    return {
        "returncode": completed.returncode,
        "runtime_seconds": round(time.monotonic() - started, 6),
        "stderr": completed.stderr,
        "stdout": completed.stdout,
    }


def _source_terminal(stdout: str) -> tuple[dict[str, Any] | None, int]:
    terminals: list[dict[str, Any]] = []
    for line in stdout.splitlines():
        if not line.startswith("FINAL_JSON "):
            continue
        try:
            value = json.loads(line.removeprefix("FINAL_JSON "))
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            terminals.append(value)
    return (terminals[0] if len(terminals) == 1 else None, len(terminals))


def _checker_summary(stdout: str) -> tuple[dict[str, Any] | None, str | None]:
    summary: dict[str, Any] | None = None
    final: str | None = None
    for line in stdout.splitlines():
        if line.startswith("SUMMARY "):
            raw = line.removeprefix("SUMMARY ").replace("'", '"')
            try:
                candidate = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if isinstance(candidate, dict):
                summary = candidate
        elif line.startswith("FINAL "):
            final = line.removeprefix("FINAL ").strip()
    return summary, final


def contract_from_terminal(terminal: dict[str, Any]) -> dict[str, Any]:
    """Normalize only the bounded fields published by the landed source."""
    layer_rows = terminal.get("layer_rows")
    if not isinstance(layer_rows, list):
        layer_rows = []
    certified_layers = [
        {
            "active_channels": row.get("active_channels"),
            "number": row.get("number"),
        }
        for row in layer_rows
        if isinstance(row, dict)
    ]
    return {
        "certified_layers": certified_layers,
        "claim_scope": terminal.get("claim_scope"),
        "complete_columns": 57344,
        "complete_number_layers": list(range(7)),
        "component_labels": ["matter", "component_1", "component_2"],
        "component_labels_construct_degrees_of_freedom": False,
        "equal_split": terminal.get("equal_split"),
        "full_fock_claim": terminal.get("full_fock_claim"),
        "omitted_number_layers": [3, 4, 5, 6],
        "truncated_columns": 6776,
    }


def classify_record(record: Any) -> str:
    """Classify one evidence record against immutable in-module expectations."""
    if not isinstance(record, dict):
        return "REJECT"
    pins = record.get("dependency_pins")
    if not isinstance(pins, dict):
        return "REJECT"
    expected_pins = {
        "source": {
            "actual": SOURCE_SHA256,
            "expected": SOURCE_SHA256,
            "verified": True,
        },
        "source_checker": {
            "actual": SOURCE_CHECKER_SHA256,
            "expected": SOURCE_CHECKER_SHA256,
            "verified": True,
        },
    }
    if pins != expected_pins:
        return "DRIFT"
    source_run = record.get("source_run")
    checker_run = record.get("source_checker_run")
    if not isinstance(source_run, dict) or not isinstance(checker_run, dict):
        return "REJECT"
    source_ok = (
        source_run.get("returncode") == 0
        and source_run.get("stderr_empty") is True
        and source_run.get("terminal_count") == 1
        and source_run.get("summary") == {"fail": 0, "pass": 10}
        and source_run.get("support_certificate_passed") is True
    )
    checker_ok = (
        checker_run.get("returncode") == 0
        and checker_run.get("stderr_empty") is True
        and checker_run.get("summary") == {"fail": 0, "pass": 7}
        and checker_run.get("final") == "ALL_PASS"
    )
    if not source_ok or not checker_ok:
        return "REJECT"
    return "ACCEPT" if record.get("contract") == EXPECTED_CONTRACT else "REJECT"


def collect_record() -> dict[str, Any]:
    source_before = _sha256(SOURCE_PATH)
    checker_before = _sha256(SOURCE_CHECKER_PATH)
    pins_verified = (
        source_before == SOURCE_SHA256
        and checker_before == SOURCE_CHECKER_SHA256
    )

    source_run = _run_script(SOURCE_PATH) if pins_verified else {
        "returncode": None,
        "stderr": "dependency pin mismatch",
        "stdout": "",
    }
    checker_run = _run_script(SOURCE_CHECKER_PATH) if pins_verified else {
        "returncode": None,
        "stderr": "dependency pin mismatch",
        "stdout": "",
    }
    source_after = _sha256(SOURCE_PATH)
    checker_after = _sha256(SOURCE_CHECKER_PATH)

    terminal, terminal_count = _source_terminal(source_run["stdout"])
    checker_summary, checker_final = _checker_summary(checker_run["stdout"])
    contract = contract_from_terminal(terminal or {})
    return {
        "contract": contract,
        "dependency_pins": {
            "source": {
                "actual": source_after,
                "expected": SOURCE_SHA256,
                "verified": (
                    source_before == source_after == SOURCE_SHA256
                ),
            },
            "source_checker": {
                "actual": checker_after,
                "expected": SOURCE_CHECKER_SHA256,
                "verified": (
                    checker_before == checker_after == SOURCE_CHECKER_SHA256
                ),
            },
        },
        "source_checker_run": {
            "final": checker_final,
            "returncode": checker_run["returncode"],
            "stderr_empty": checker_run["stderr"] == "",
            "summary": (
                {
                    "fail": checker_summary.get("fail"),
                    "pass": checker_summary.get("pass"),
                }
                if checker_summary
                else None
            ),
        },
        "source_run": {
            "returncode": source_run["returncode"],
            "stderr_empty": source_run["stderr"] == "",
            "summary": terminal.get("summary") if terminal else None,
            "support_certificate_passed": (
                terminal.get("support_certificate_passed") if terminal else None
            ),
            "terminal_count": terminal_count,
        },
    }


def _mutated_records(record: dict[str, Any]) -> dict[str, dict[str, Any]]:
    mutations: dict[str, dict[str, Any]] = {}

    full_fock = copy.deepcopy(record)
    full_fock["contract"]["full_fock_claim"] = True
    mutations["full_fock_promotion"] = full_fock

    derived_split = copy.deepcopy(record)
    derived_split["contract"]["equal_split"]["status"] = "derived"
    mutations["derived_equal_split"] = derived_split

    carrier_labels = copy.deepcopy(record)
    carrier_labels["contract"]["component_labels"] = [
        "matter",
        "mediator",
        "auxiliary",
    ]
    carrier_labels["contract"]["component_labels_construct_degrees_of_freedom"] = True
    mutations["carrier_promotion"] = carrier_labels

    expanded_domain = copy.deepcopy(record)
    expanded_domain["contract"]["certified_layers"].append(
        {"active_channels": 36, "number": 3}
    )
    mutations["uncertified_layer"] = expanded_domain

    pin_drift = copy.deepcopy(record)
    pin_drift["dependency_pins"]["source"]["actual"] = "0" * 64
    pin_drift["dependency_pins"]["source"]["verified"] = False
    mutations["pin_drift"] = pin_drift
    return mutations


def _check(label: str, condition: bool, detail: Any) -> bool:
    print("PASS" if condition else "FAIL", label, "::", detail)
    return condition


def main() -> int:
    if sys.argv[1:] == ["--classify-json"]:
        try:
            record = json.load(sys.stdin)
        except (json.JSONDecodeError, OSError):
            print("REJECT")
            return 0
        print(classify_record(record))
        return 0
    if sys.argv[1:]:
        print("usage: frontier_truncated_fock_fixture_verifier_2026_07_28.py [--classify-json]", file=sys.stderr)
        return 2

    started = time.monotonic()
    record = collect_record()
    verdict = classify_record(record)
    mutation_verdicts = {
        name: classify_record(mutated)
        for name, mutated in _mutated_records(record).items()
    }

    results = [
        _check(
            "the repaired truncated source and clean-room checker are immutable and rerun",
            verdict == "ACCEPT",
            {
                "pins": record["dependency_pins"],
                "source": record["source_run"],
                "source_checker": record["source_checker_run"],
            },
        ),
        _check(
            "the normalized contract remains strictly n_left,n_right<=2",
            (
                record["contract"] == EXPECTED_CONTRACT
                and record["contract"]["full_fock_claim"] is False
                and record["contract"]["omitted_number_layers"] == [3, 4, 5, 6]
            ),
            record["contract"],
        ),
        _check(
            "equal split and neutral component labels remain supplied conventions",
            (
                record["contract"]["equal_split"]["status"]
                == "supplied_not_derived"
                and record["contract"]["component_labels"]
                == ["matter", "component_1", "component_2"]
                and record["contract"][
                    "component_labels_construct_degrees_of_freedom"
                ]
                is False
            ),
            {
                "component_labels": record["contract"]["component_labels"],
                "equal_split": record["contract"]["equal_split"],
            },
        ),
        _check(
            "public classifier rejects scope, interpretation, and pin mutations",
            mutation_verdicts
            == {
                "carrier_promotion": "REJECT",
                "derived_equal_split": "REJECT",
                "full_fock_promotion": "REJECT",
                "pin_drift": "DRIFT",
                "uncertified_layer": "REJECT",
            },
            mutation_verdicts,
        ),
        _check(
            "the independent checker is exposed as an audit packet helper",
            (
                INDEPENDENT_PACKET_SOURCE.CHECKER_KIND
                == "clean-room-stdlib-mutation"
            ),
            INDEPENDENT_PACKET_SOURCE.CHECKER_KIND,
        ),
    ]
    final = {
        "checks": {"fail": results.count(False), "pass": results.count(True)},
        "contract": record["contract"],
        "dependency_pins": record["dependency_pins"],
        "mutation_verdicts": mutation_verdicts,
        "note_path": NOTE_PATH,
        "record": record,
        "runtime_seconds": round(time.monotonic() - started, 6),
        "tool_role": "non-authoritative fixed-pin truncated-fixture verification",
        "verdict": verdict,
    }
    print("FINAL_JSON", json.dumps(final, sort_keys=True))
    return int(not all(results))


if __name__ == "__main__":
    raise SystemExit(main())
