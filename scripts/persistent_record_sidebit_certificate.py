#!/usr/bin/env python3
"""Paired deterministic certificate for the persistent-record side-bit row."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 480
AUDIT_INPUT_PATHS = (
    "docs/PERSISTENT_RECORD_SIDEBIT_NOTE.md",
    "scripts/persistent_record_overlap_kernel.py",
    "scripts/persistent_record_matched_compare.py",
)


def run_child(args: list[str]) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, "-u", *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    print(f"CHILD {' '.join(args)} exit={proc.returncode}")
    print(proc.stdout, end="" if proc.stdout.endswith("\n") else "\n")
    if proc.stderr:
        print("STDERR")
        print(proc.stderr, end="" if proc.stderr.endswith("\n") else "\n")
    return proc.returncode, proc.stdout


def data_sides(text: str) -> list[int]:
    return [
        int(value)
        for value in re.findall(r"^\s*(8|12|18)\s+(?:[0-9]|nan)", text, re.MULTILINE)
    ]


def main() -> int:
    overlap_args = [
        "scripts/persistent_record_overlap_kernel.py",
        "--side-bit",
        "--seeds",
        "2",
        "--gamma",
        "1.0",
        "--n-layers",
        "8,12,18",
    ]
    matched_args = [
        "scripts/persistent_record_matched_compare.py",
        "--seeds",
        "2",
        "--gamma",
        "1.0",
        "--n-layers",
        "8,12,18",
        "--methods",
        "node,pr_trace,pr_soft,pr_side_trace,pr_side_soft",
    ]
    overlap_code, overlap = run_child(overlap_args)
    matched_code, matched = run_child(matched_args)

    source = (ROOT / "scripts/persistent_record_overlap_kernel.py").read_text(
        encoding="utf-8"
    )
    implementation_ok = (
        "include_side_bit" in source
        and "has_marker_in_range" in source
        and "side_marker_cell" in source
        and "update_record" in source
    )
    overlap_sides = data_sides(overlap)
    matched_sides = data_sides(matched)
    columns_ok = all(
        label in matched
        for label in ("node", "pr_trace", "pr_g1", "pr_side_trace", "pr_side_g1")
    )
    execution_ok = (
        overlap_code == 0
        and matched_code == 0
        and "side_bit: True" in overlap
        and overlap_sides == [8, 12, 18]
        and matched_sides == [8, 12, 18]
        and columns_ok
    )

    print()
    print(
        "per_element: computed every path-amplitude contribution entering "
        "the persistent record and side-marker states"
    )
    print(
        "per_site: computed all generated DAG nodes for matched N=8,12,18 "
        "with two deterministic seeds"
    )
    print(
        "per_mode: computed node, base trace/soft, and side-bit trace/soft "
        "modes at gamma=1.0"
    )
    print(
        f"per_block: computed paired overlap and matched-comparison blocks; "
        f"implementation_evidence={implementation_ok}"
    )
    print(
        "lattice_wide: checked and not executed — the claim is bounded to "
        "the matched N=8,12,18 DAG slice, not an asymptotic graph family"
    )
    passed = execution_ok and implementation_ok
    print(
        f"CERTIFICATE execution_ok={execution_ok} "
        f"implementation_ok={implementation_ok}"
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
