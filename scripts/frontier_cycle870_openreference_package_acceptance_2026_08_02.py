#!/usr/bin/env python3
"""Cold package acceptance harness for the Cycle-870 matter compiler.

The static imports are intentional: they make every load-bearing primary and
independent runner available to the repository's restricted audit packet.
The executable acceptance path reruns all six sources in dependency order,
checks their terminal markers, verifies their deterministic receipts, and
rejects any source or receipt drift.
"""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

import frontier_cycle870_openreference_physical_m2_placement_2026_08_02 as placement
import frontier_cycle870_openreference_native_recurrent_update_2026_08_02 as native
import frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02 as joined
import frontier_cycle870_openreference_recurrent_update_independent_check_2026_08_02 as independent_update
import frontier_cycle870_openreference_chronological_encoder_independent_check_2026_08_02 as independent_encoder
import frontier_cycle870_openreference_fixed_route_schedule_independent_check_2026_08_02 as independent_schedule


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
AUDIT_TIMEOUT_SEC = 1800
CHILD_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py",
    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py",
    "scripts/frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py",
    "scripts/frontier_cycle870_openreference_recurrent_update_independent_check_2026_08_02.py",
    "scripts/frontier_cycle870_openreference_chronological_encoder_independent_check_2026_08_02.py",
    "scripts/frontier_cycle870_openreference_fixed_route_schedule_independent_check_2026_08_02.py",
)
OUTPUT = (
    ROOT
    / "outputs"
    / "cycle870_openreference_package_acceptance_receipt_2026_08_02.json"
)

IMPORTED_HELPER_MODULES = (
    placement,
    native,
    joined,
    independent_update,
    independent_encoder,
    independent_schedule,
)

RUNNERS = (
    (
        "placement",
        "frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py",
        "cycle870_openreference_physical_m2_placement_receipt_2026_08_02.json",
        "OPENREFERENCE_PHYSICAL_PLACEMENT_PASS",
        "64b36432670f8a05179d0473e724afee1dfe6327cdd0233d3d788a6b8413c8a2",
        "ab2d980726e336221e49808b6edcfaaae802173ee2f00fe96d8d55a4f2c6899d",
    ),
    (
        "native_update",
        "frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py",
        "cycle870_openreference_native_recurrent_update_receipt_2026_08_02.json",
        "OPENREFERENCE_NATIVE_UPDATE_PASS",
        "687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237",
        "b1c812afbf25b84b99a5d171cf7925ffc86272e52c252c5f7ee68cb9f5a76807",
    ),
    (
        "joined_compiler",
        "frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py",
        "cycle870_openreference_joined_recurrent_compiler_receipt_2026_08_02.json",
        "OPENREFERENCE_JOINED_CUBE_PASS",
        "1b66c061dcb8e0082fd9e7264e78ccbd0f77440c0f517aa93696bde49f78c1bd",
        "d6be75419b1fab56853127d55730b63a23ef7d44205e66b7fa73c9f19aac8611",
    ),
    (
        "independent_update",
        "frontier_cycle870_openreference_recurrent_update_independent_check_2026_08_02.py",
        "cycle870_openreference_recurrent_update_independent_receipt_2026_08_02.json",
        "INDEPENDENT_OPENREFERENCE_RECONSTRUCTION_PASS",
        "49d76550de2d1d44adb2703be0ce7d3bc1ebfdc4914c8eee0413b29ad8dc8af9",
        "f3fa00ade5696bf3061a2bedc776a910ad801e6bef28a7558f1a3f07ab7a813f",
    ),
    (
        "independent_encoder",
        "frontier_cycle870_openreference_chronological_encoder_independent_check_2026_08_02.py",
        "cycle870_openreference_chronological_encoder_independent_receipt_2026_08_02.json",
        "INDEPENDENT_CHRONOLOGICAL_E_EXACTNESS_PASS_WITH_QUALIFICATIONS",
        "6ae587e6bd8769e0b6880199d7a95023649464f625211bcb0530c21634a7e3ab",
        "dfedebd2cc790cadd692bb323b2578b830dc800938e90b60aa2739216cde5308",
    ),
    (
        "independent_schedule",
        "frontier_cycle870_openreference_fixed_route_schedule_independent_check_2026_08_02.py",
        "cycle870_openreference_fixed_route_schedule_independent_receipt_2026_08_02.json",
        "INDEPENDENT_FIXED_MOD3_ROUTE_SCHEDULE_PASS",
        "7d2a074dda9bf89566895c7df99de32a675e0ba0706304f4db964d2f053cbdbd",
        "87d8a95f305c4adaa1feadc051df2d9ac89ee8adc93534f783922bc29cec1b8f",
    ),
)


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def receipt_semantic_failures(name: str, receipt: dict[str, object]) -> list[str]:
    if name in {"placement", "native_update", "joined_compiler"}:
        return [] if receipt.get("status") == "pass" and not receipt.get("failures") else [name]
    if name == "independent_update":
        return [] if receipt.get("independent_reconstruction_pass") and not receipt.get("validation_failures") else [name]
    if name == "independent_encoder":
        return (
            []
            if receipt.get("independent_chronological_E_exactness_pass")
            and not receipt.get("validation_failures")
            and receipt.get("verification_status")
            == "pass_with_deletion_and_domain_qualifications"
            and receipt.get("independent_per_occurrence_deletion_completeness_pass")
            is False
            else [name]
        )
    if name == "independent_schedule":
        return [] if receipt.get("independent_fixed_schedule_pass") and not receipt.get("validation_failures") else [name]
    return [f"unknown:{name}"]


def main() -> int:
    failures: list[str] = []
    rows: list[dict[str, object]] = []
    for name, source_name, receipt_name, marker, expected_source, expected_receipt in RUNNERS:
        source = HERE / source_name
        receipt_path = ROOT / "outputs" / receipt_name
        observed_source = file_hash(source)
        if observed_source != expected_source:
            failures.append(f"{name}:source pin")
            rows.append(
                {
                    "name": name,
                    "source": str(source.relative_to(ROOT)),
                    "source_sha256": observed_source,
                    "expected_source_sha256": expected_source,
                    "executed": False,
                }
            )
            continue
        try:
            completed = subprocess.run(
                (sys.executable, "-B", str(source.relative_to(ROOT))),
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
                timeout=CHILD_TIMEOUT_SEC,
            )
        except subprocess.TimeoutExpired:
            failures.append(f"{name}:timeout>{CHILD_TIMEOUT_SEC}s")
            rows.append(
                {
                    "name": name,
                    "source": str(source.relative_to(ROOT)),
                    "source_sha256": observed_source,
                    "expected_source_sha256": expected_source,
                    "executed": False,
                    "timeout_seconds": CHILD_TIMEOUT_SEC,
                }
            )
            continue
        marker_seen = marker in completed.stdout
        if completed.returncode != 0:
            failures.append(f"{name}:exit={completed.returncode}")
        if not marker_seen:
            failures.append(f"{name}:terminal marker")
        observed_receipt = file_hash(receipt_path) if receipt_path.is_file() else None
        if observed_receipt != expected_receipt:
            failures.append(f"{name}:receipt pin")
        semantic_failures = (
            receipt_semantic_failures(name, json.loads(receipt_path.read_text()))
            if receipt_path.is_file()
            else [name]
        )
        failures.extend(f"{item}:receipt semantics" for item in semantic_failures)
        rows.append(
            {
                "name": name,
                "source": str(source.relative_to(ROOT)),
                "source_sha256": observed_source,
                "expected_source_sha256": expected_source,
                "receipt": str(receipt_path.relative_to(ROOT)),
                "receipt_sha256": observed_receipt,
                "expected_receipt_sha256": expected_receipt,
                "returncode": completed.returncode,
                "terminal_marker": marker,
                "terminal_marker_seen": marker_seen,
                "semantic_failure_count": len(semantic_failures),
                "executed": completed.returncode == 0,
            }
        )

    artifact_path = Path(__file__).resolve()
    report: dict[str, object] = {
        "artifact": {
            "path": str(artifact_path.relative_to(ROOT)),
            "sha256": file_hash(artifact_path),
            "method": "cold dependency-ordered execution of every registered Cycle-870 runner",
        },
        "static_audit_helper_modules": tuple(
            module.__name__ for module in IMPORTED_HELPER_MODULES
        ),
        "runner_rows": rows,
        "validation_failures": failures,
        "package_acceptance_pass": not failures,
        "claim_boundary": (
            "This harness certifies package execution, pins, and receipt semantics. "
            "It adds no physical law and does not upgrade the bounded theorem scope."
        ),
    }
    canonical = json.dumps(report, sort_keys=True, default=str).encode()
    report["content_sha256_before_hash_field"] = sha256(canonical).hexdigest()
    OUTPUT.write_text(json.dumps(report, indent=2, sort_keys=True, default=str) + "\n")
    print("CYCLE870_PACKAGE_ACCEPTANCE_PASS" if not failures else "CYCLE870_PACKAGE_ACCEPTANCE_FAIL")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
