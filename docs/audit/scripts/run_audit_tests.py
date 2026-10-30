#!/usr/bin/env python3
"""Run every audit test file, one process per file, and report by file.

CI runs this so a new failure cannot go unnoticed. Files in KNOWN_BROKEN were
already failing when this runner was added. They still run and are reported,
but do not fail the run; remove an entry once its file passes.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent / "tests"

KNOWN_BROKEN = {
    "test_audit_pipeline.py": (
        "8 cases: fixtures predate science_fingerprint_v2, so the legacy epoch "
        "reason fires first; two more pin live notes or ledger keys"
    ),
    "test_citation_graph_build_serialization.py": (
        "5 cases: reads the landing loop from review-loop/SKILL.md; "
        "it moved to references/LANDING.md"
    ),
    "test_cycle873_authority_packet_repair.py": "1 case: body exceeds the target limit it pins",
    "test_cycle970_inter_site_packet.py": "1 case: the packet checker now exits 1",
    "test_fingerprint_v1_stamping.py": (
        "28 cases: the fixture cannot build a science_fingerprint_v2 snapshot"
    ),
    "test_review_loop_backlog_inventory.py": "1 case: scan_error stays None on a symlink error",
    "test_runner_pin_gate.py": "1 case: the note read fails before the runner-pin check",
}


def run_file(path: Path) -> tuple[bool, str]:
    proc = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(TESTS_DIR), "-p", path.name],
        capture_output=True,
        text=True,
    )
    return proc.returncode == 0, proc.stdout + proc.stderr


def main() -> int:
    unexpected: list[str] = []
    for path in sorted(TESTS_DIR.glob("test_*.py")):
        passed, output = run_file(path)
        if passed:
            label = "PASS, remove from KNOWN_BROKEN" if path.name in KNOWN_BROKEN else "PASS"
        elif path.name in KNOWN_BROKEN:
            label = f"KNOWN BROKEN ({KNOWN_BROKEN[path.name]})"
        else:
            label = "FAIL"
            unexpected.append(path.name)
            print(output)
        print(f"{path.name}: {label}", flush=True)
    stale = sorted(set(KNOWN_BROKEN) - {p.name for p in TESTS_DIR.glob("test_*.py")})
    if stale:
        print(f"KNOWN_BROKEN names missing files: {', '.join(stale)}")
    print(f"unexpected failures: {len(unexpected)}")
    return 1 if unexpected or stale else 0


if __name__ == "__main__":
    raise SystemExit(main())
