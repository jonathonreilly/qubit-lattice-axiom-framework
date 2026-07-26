#!/usr/bin/env python3
"""Fail-closed acceptance wrapper for the three independent Cycle-705 routes."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import frontier_cycle705_direct_reference_edge_support_localization_2026_07_25  # noqa: F401
    import frontier_cycle705_geometry_local_seam_gauge_tableau_2026_07_25  # noqa: F401
    import frontier_cycle705_cycle269_carrier_role_support_localization_2026_07_26  # noqa: F401


ROOT = Path(__file__).resolve().parents[1]

ROUTES = (
    {
        "name": "direct_reference_edge",
        "path": "scripts/frontier_cycle705_direct_reference_edge_support_localization_2026_07_25.py",
        "sha256": "fe16008972dd77bfcea789ba530dc744bf6a8bf4777a06744032e372cdbce32e",
        "terminal": "DIRECT_REFERENCE_EDGE_COMMON_E_EXACT_PATH_SUPPORT_ADVANTAGE_RETAINED",
        "summary": "SUMMARY_JSON ",
        "passes": 9,
    },
    {
        "name": "geometry_local_seam_gauge",
        "path": "scripts/frontier_cycle705_geometry_local_seam_gauge_tableau_2026_07_25.py",
        "sha256": "bc61e5f93e47f18117064243d9d9a6b34bbe6bfdc07bda27c953b78880ef6d00",
        "terminal": "CYCLE705_FACE_GAUGE_COMMON_E_FREEZE_EXACT_HELD_SEAM_COSETS_5_55_132_ROUTE_OPEN",
        "summary": "SUMMARY_JSON ",
        "passes": 7,
    },
    {
        "name": "cycle269_carrier_role",
        "path": "scripts/frontier_cycle705_cycle269_carrier_role_support_localization_2026_07_26.py",
        "sha256": "92191de04731fee6a9fb5ecdeea2d32b38d688825e464dbc5ce3d6b7d6ee1a28",
        "terminal": None,
        "summary": None,
        "passes": 21,
    },
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_summary(stdout: str, prefix: str) -> dict[str, object]:
    rows = [line[len(prefix) :] for line in stdout.splitlines() if line.startswith(prefix)]
    if len(rows) != 1:
        raise AssertionError(f"expected one {prefix!r} row, found {len(rows)}")
    payload = json.loads(rows[0])
    if not isinstance(payload, dict):
        raise AssertionError("summary payload is not an object")
    return payload


def main() -> None:
    observed: list[dict[str, object]] = []
    failures: list[str] = []

    for route in ROUTES:
        path = ROOT / str(route["path"])
        digest = sha256(path)
        if digest != route["sha256"]:
            failures.append(f"{route['name']}: source hash {digest} != {route['sha256']}")
            continue

        proc = subprocess.run(
            [sys.executable, str(path)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        row: dict[str, object] = {
            "name": route["name"],
            "source_sha256": digest,
            "returncode": proc.returncode,
            "stderr_bytes": len(proc.stderr.encode()),
        }
        if proc.returncode != 0:
            failures.append(f"{route['name']}: return code {proc.returncode}")
        if proc.stderr:
            failures.append(f"{route['name']}: nonempty stderr")

        if route["summary"]:
            summary = extract_summary(proc.stdout, str(route["summary"]))
            row["terminal"] = summary.get("terminal")
            row["tests_passed"] = summary.get("tests_passed")
            row["tests_failed"] = summary.get("tests_failed")
            if summary.get("terminal") != route["terminal"]:
                failures.append(f"{route['name']}: terminal mismatch")
            if summary.get("tests_passed") != route["passes"]:
                failures.append(f"{route['name']}: pass-count mismatch")
            if summary.get("tests_failed") != 0:
                failures.append(f"{route['name']}: child reports failures")
        else:
            terminal = "SUMMARY pass=21 fail=0"
            count = proc.stdout.count(terminal)
            row["terminal"] = terminal
            row["terminal_count"] = count
            if count != 1:
                failures.append(f"{route['name']}: expected one exact summary, found {count}")

        observed.append(row)

    checks = {
        "all_three_sources_pinned": len(observed) == 3,
        "all_children_exit_zero": len(observed) == 3 and all(x["returncode"] == 0 for x in observed),
        "all_children_stderr_empty": len(observed) == 3 and all(x["stderr_bytes"] == 0 for x in observed),
        "expected_total_checks": sum(int(x.get("tests_passed", 21 if x["name"] == "cycle269_carrier_role" else 0)) for x in observed) == 37,
    }
    failures.extend(name for name, passed in checks.items() if not passed)

    payload = {
        "cycle": 705,
        "routes": observed,
        "checks": checks,
        "failures": failures,
        "route_independent_obstruction": False,
        "axiom_pressure": False,
        "audit": "unset",
        "authority": "none",
        "terminal": "CYCLE705_ENDPOINT_LOCALIZATION_THREE_ROUTE_ACCEPTANCE_CLOSED",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    if failures:
        raise SystemExit(1)
    print(payload["terminal"])


if __name__ == "__main__":
    main()
