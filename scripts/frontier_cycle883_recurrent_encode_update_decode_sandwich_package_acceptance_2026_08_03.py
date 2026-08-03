#!/usr/bin/env python3
"""Cold package acceptance for the bounded Cycle-883 sandwich theorem."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

import frontier_cycle883_recurrent_encode_update_decode_sandwich_core_2026_08_03 as core
import frontier_cycle883_recurrent_encode_update_decode_sandwich_2026_08_03 as primary
import frontier_cycle883_recurrent_encode_update_decode_sandwich_independent_check_2026_08_03 as independent


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "outputs/cycle883_recurrent_encode_update_decode_sandwich_package_acceptance_receipt_2026_08_03.json"
AUDIT_TIMEOUT_SEC = 1800
CHILD_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle883_recurrent_encode_update_decode_sandwich_core_2026_08_03.py",
    "scripts/frontier_cycle883_recurrent_encode_update_decode_sandwich_2026_08_03.py",
    "scripts/frontier_cycle883_recurrent_encode_update_decode_sandwich_independent_check_2026_08_03.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
IMPORTED_HELPER_MODULES = (core, primary, independent)
RUNNERS = (
    (
        "primary",
        "scripts/frontier_cycle883_recurrent_encode_update_decode_sandwich_2026_08_03.py",
        "outputs/cycle883_recurrent_encode_update_decode_sandwich_primary_receipt_2026_08_03.json",
        "053b0886a5de2b204bc004b0bd30b47e47fd0049ba80f11a8d9b7b4b24e04aa0",
        "d4643ba7f109595ac21199ad4985ec5dbe8ce6263ed8274a9b8c4a40d87e3791",
    ),
    (
        "independent",
        "scripts/frontier_cycle883_recurrent_encode_update_decode_sandwich_independent_check_2026_08_03.py",
        "outputs/cycle883_recurrent_encode_update_decode_sandwich_independent_receipt_2026_08_03.json",
        "89b23e73d815c4c1c4c9ebc5a16b260331e153bd6267fed1289aa5b4ecaae5ba",
        "b78d209e50fb7b60c5072e140f5debfae4a629de8776fa20b07b5db400c7cbc3",
    ),
)


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> int:
    failures = []
    rows = []
    for name, source_name, receipt_name, expected_source, expected_receipt in RUNNERS:
        source = ROOT / source_name
        receipt = ROOT / receipt_name
        observed_source = file_hash(source)
        executed = False
        returncode = None
        stdout_matches_receipt = False
        if observed_source != expected_source:
            failures.append(name + ":source-pin")
        else:
            try:
                completed = subprocess.run(
                    (sys.executable, "-B", source_name),
                    cwd=ROOT,
                    capture_output=True,
                    text=True,
                    timeout=CHILD_TIMEOUT_SEC,
                    check=False,
                )
                returncode = completed.returncode
                executed = True
                if returncode:
                    failures.append(name + ":exit=" + str(returncode))
                stdout_matches_receipt = (
                    receipt.is_file() and completed.stdout == receipt.read_text()
                )
                if not stdout_matches_receipt:
                    failures.append(name + ":stdout-receipt")
            except subprocess.TimeoutExpired:
                failures.append(name + ":timeout")
        observed_receipt = file_hash(receipt) if receipt.is_file() else None
        if observed_receipt != expected_receipt:
            failures.append(name + ":receipt-pin")
        semantic_pass = False
        if receipt.is_file():
            payload = json.loads(receipt.read_text())
            semantic_pass = payload.get("status") == "pass" and not payload.get(
                "failures"
            )
        if not semantic_pass:
            failures.append(name + ":receipt-semantics")
        rows.append(
            {
                "name": name,
                "source": source_name,
                "source_sha256": observed_source,
                "expected_source_sha256": expected_source,
                "receipt": receipt_name,
                "receipt_sha256": observed_receipt,
                "expected_receipt_sha256": expected_receipt,
                "executed": executed,
                "returncode": returncode,
                "stdout_matches_receipt": stdout_matches_receipt,
                "semantic_pass": semantic_pass,
            }
        )
    report = {
        "status": "pass" if not failures else "fail",
        "claim_type": "package_acceptance",
        "static_audit_helper_modules": tuple(
            module.__name__ for module in IMPORTED_HELPER_MODULES
        ),
        "runner_rows": rows,
        "failures": failures,
        "boundary": (
            "cold execution, source/receipt pins, stdout equality, and receipt semantics only; no audit verdict or wider physics claim"
        ),
        "this_source_sha256": file_hash(Path(__file__)),
    }
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    OUT.write_text(payload)
    print(payload, end="")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
