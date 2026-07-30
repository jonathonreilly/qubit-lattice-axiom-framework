#!/usr/bin/env python3
"""Fast source-identity and deterministic-slice certificate for the Poisson row.

The complete numerical runner contains a large ``N=52`` sparse eigenvalue
solve that can be pathologically slow on some SciPy/ARPACK builds.  A completed
14/14 output was committed together with the current full runner.  This
certificate proves that the numerical code used by that output is still the
code in the tree, pins the repo-local helper module and checks the helper
function used through ``F`` by AST identity, then reruns the small ``N=12``
slice against the completed output.

This is a compute/provenance certificate.  It does not mint or predict an audit
verdict and it does not claim that the full sweep was rerun in this process.
"""
from __future__ import annotations

import ast
import hashlib
import re
import subprocess
import sys
from pathlib import Path

import physical_poisson_self_consistent_well_depth_finite_volume_2026_07_27 as full


REPO_ROOT = Path(__file__).resolve().parent.parent
FULL_RUNNER = "scripts/physical_poisson_self_consistent_well_depth_finite_volume_2026_07_27.py"
HELPER = "scripts/frontier_self_consistent_field_equation.py"
COMPLETED_LOG = "logs/runner-cache/physical_poisson_self_consistent_well_depth_finite_volume_2026_07_27.txt"
PAIRED_COMMIT = "870573b35c1c5fa3c0a5a822984aa951e3c6477e"
FULL_RUNNER_BLOB = "5ac4ed61155e093c554cb464f096d59d0954c86c"
COMPLETED_LOG_BLOB = "fa5b859ea4366fc1c72a613ef33b38d337ae520e"
HELPER_BLOB = "761ea4b41cbe1eee28dc9561eb947e87bfb4bad8"

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "scripts/physical_poisson_self_consistent_well_depth_finite_volume_2026_07_27.py",
    "scripts/frontier_self_consistent_field_equation.py",
    "logs/runner-cache/physical_poisson_self_consistent_well_depth_finite_volume_2026_07_27.txt",
)


def git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(REPO_ROOT), *args],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def sha256(path: str) -> str:
    return hashlib.sha256((REPO_ROOT / path).read_bytes()).hexdigest()


def function_ast(source: str, name: str) -> str:
    matches = [
        node
        for node in ast.walk(ast.parse(source))
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == name
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one {name} definition, found {len(matches)}")
    return ast.dump(matches[0], include_attributes=False)


def imported_full_symbols(source: str) -> set[str]:
    return {
        node.attr
        for node in ast.walk(ast.parse(source))
        if isinstance(node, ast.Attribute)
        and isinstance(node.value, ast.Name)
        and node.value.id == "F"
    }


def checked(label: str, condition: bool, detail: str) -> bool:
    print(f"[{'PASS' if condition else 'FAIL'}] {label}: {detail}")
    return condition


def summarize(checks: list[bool]) -> int:
    passed = sum(checks)
    failed = len(checks) - passed
    status = "PASS" if failed == 0 else "FAIL"
    print(
        f"{status} (C): source-identity-pinned completed sweep plus "
        "current deterministic slice"
    )
    print(f"SUMMARY: CERTIFICATE PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


def main() -> int:
    print("=" * 78)
    print("POISSON FINITE-VOLUME COMPLETED-LOG AND DETERMINISTIC-SLICE CERTIFICATE")
    print("=" * 78)

    checks: list[bool] = []

    def record(label: str, condition: bool, detail: str) -> None:
        checks.append(checked(label, condition, detail))

    runner_commit = git("log", "-1", "--format=%H", "--", FULL_RUNNER)
    log_commit = git("log", "-1", "--format=%H", "--", COMPLETED_LOG)
    runner_blob = git("hash-object", str(REPO_ROOT / FULL_RUNNER))
    log_blob = git("hash-object", str(REPO_ROOT / COMPLETED_LOG))
    helper_blob = git("hash-object", str(REPO_ROOT / HELPER))
    record(
        "A1 paired artifact",
        runner_commit == log_commit == PAIRED_COMMIT,
        f"runner and completed log were last changed together at {runner_commit[:12]}",
    )
    artifacts_exact = (
        runner_blob == FULL_RUNNER_BLOB
        and log_blob == COMPLETED_LOG_BLOB
        and helper_blob == HELPER_BLOB
    )
    record(
        "A2 exact artifacts",
        artifacts_exact,
        f"runner blob {runner_blob[:12]}, completed-log blob {log_blob[:12]}, "
        f"helper blob {helper_blob[:12]}",
    )

    runner_source = (REPO_ROOT / FULL_RUNNER).read_text(encoding="utf-8")
    helper_source = (REPO_ROOT / HELPER).read_text(encoding="utf-8")
    paired_helper_source = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "show", f"{PAIRED_COMMIT}:{HELPER}"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    used_symbols = imported_full_symbols(runner_source)
    helper_same = function_ast(helper_source, "build_laplacian_sparse") == function_ast(
        paired_helper_source, "build_laplacian_sparse"
    )
    record(
        "B1 imported surface",
        used_symbols == {"build_laplacian_sparse"},
        f"full runner imports only F.{', F.'.join(sorted(used_symbols))}",
    )
    record(
        "B2 imported numerical identity",
        helper_same,
        "build_laplacian_sparse AST matches the paired completed-log commit",
    )

    completed = (REPO_ROOT / COMPLETED_LOG).read_text(encoding="utf-8")
    summary_ok = "SUMMARY: SELF-CONSISTENT WELL DEPTH PASS=14 FAIL=0" in completed
    record(
        "C1 completed full sweep",
        summary_ok,
        "paired log records the full scored sweep with PASS=14 FAIL=0",
    )
    if artifacts_exact and summary_ok:
        print("----- BEGIN BLOB-VERIFIED COMPLETED FULL-SWEEP OUTPUT -----")
        print(completed.rstrip())
        print("----- END BLOB-VERIFIED COMPLETED FULL-SWEEP OUTPUT -----")
    else:
        print("completed full-sweep output omitted because its identity check failed")

    match = re.search(
        r"g=\s*20\.0\s+N=\s*12\s+rms=\s*([0-9.]+)\s+"
        r"depth=\s*([0-9.]+)\s+iters=\s*(\d+)",
        completed,
    )
    if match is None:
        record("C2 historical slice", False, "N=12 row missing from completed log")
    else:
        expected_rms = float(match.group(1))
        expected_depth = float(match.group(2))
        expected_iters = int(match.group(3))
        slice_result = full.self_consistent(12, "poisson", 20.0)
        slice_ok = (
            slice_result["conv"]
            and abs(slice_result["rms"] - expected_rms) <= 1e-4
            and abs(slice_result["depth"] - expected_depth) <= 1e-4
            and slice_result["it"] == expected_iters
        )
        record(
            "C2 deterministic current slice",
            slice_ok,
            "current N=12 result "
            f"rms={slice_result['rms']:.4f}, depth={slice_result['depth']:.4f}, "
            f"iters={slice_result['it']} versus paired completed log",
        )

    print(f"full_runner_sha256={sha256(FULL_RUNNER)}")
    print(f"helper_sha256={sha256(HELPER)}")
    print(f"completed_log_sha256={sha256(COMPLETED_LOG)}")
    return summarize(checks)


if __name__ == "__main__":
    sys.exit(main())
