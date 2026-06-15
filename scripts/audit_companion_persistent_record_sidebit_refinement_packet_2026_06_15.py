#!/usr/bin/env python3
"""Audit companion for the persistent-record side-bit/refinement rows.

The default `persistent_record_matched_compare.py` cache does not exercise the
side-bit and side+packet+entry method surfaces quoted by the two source notes.
This companion runs the exact bounded CLI surfaces and checks the frozen table
values and non-promotion boundaries.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Packet-visible helper references for build_citation_graph.py.
    import persistent_record_matched_compare as _persistent_record_matched_compare


AUDIT_TIMEOUT_SEC = 300
ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts" / "persistent_record_matched_compare.py"
SIDEBIT_NOTE = ROOT / "docs" / "PERSISTENT_RECORD_SIDEBIT_NOTE.md"
REFINEMENT_NOTE = ROOT / "docs" / "PERSISTENT_RECORD_REFINEMENT_NOTE.md"

PASS = 0
FAIL = 0

SIDEBIT_COLUMNS = ["node", "pr_trace", "pr_g1", "pr_side_trace", "pr_side_g1"]
SIDEBIT_EXPECTED = {
    8: [0.7971, 0.8317, 0.8672, 0.8323, 0.8644],
    12: [0.5128, 0.5349, 0.6099, 0.5284, 0.5698],
    18: [0.7121, 0.7511, 0.7314, 0.7699, 0.7287],
}

REFINEMENT_COLUMNS = [
    "node",
    "pr_side_packet_trace",
    "pr_side_packet_g1",
    "pr_side_packet_g1.5",
    "pr_side_packet_g2",
    "pr_side_packet_entry_trace",
    "pr_side_packet_entry_g1",
    "pr_side_packet_entry_g1.5",
    "pr_side_packet_entry_g2",
]
REFINEMENT_EXPECTED = {
    8: [0.7971, 0.8323, 0.8643, 0.8445, 0.8368, 0.8323, 0.8645, 0.8445, 0.8368],
    12: [0.5128, 0.5284, 0.5634, 0.5484, 0.5403, 0.5284, 0.5627, 0.5483, 0.5404],
    18: [0.7121, 0.7630, 0.7217, 0.7387, 0.7490, 0.7630, 0.7213, 0.7386, 0.7490],
}


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def section(title: str) -> None:
    print()
    print("=" * 92)
    print(title)
    print("=" * 92)


def run_compare(label: str, args: list[str], timeout: int) -> str:
    section(f"Run matched comparison: {label}")
    cmd = [sys.executable, str(RUNNER), *args]
    print("$ " + " ".join(cmd))
    env = {**os.environ, "PYTHONPATH": str(ROOT / "scripts")}
    proc = subprocess.run(
        cmd,
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
    )
    print(proc.stdout)
    if proc.stderr.strip():
        print("STDERR:")
        print(proc.stderr)
    check(f"{label} exits 0", proc.returncode == 0, f"returncode={proc.returncode}")
    return proc.stdout


def parse_rows(stdout: str, expected_columns: list[str]) -> dict[int, list[float]]:
    rows: dict[int, list[float]] = {}
    expected_width = 1 + len(expected_columns)
    for line in stdout.splitlines():
        parts = line.split()
        if not parts or not parts[0].isdigit() or len(parts) != expected_width:
            continue
        rows[int(parts[0])] = [float(x) for x in parts[1:]]
    return rows


def check_table(label: str, rows: dict[int, list[float]], expected: dict[int, list[float]], columns: list[str], tol: float) -> None:
    section(f"Check table: {label}")
    check(f"{label} has expected N rows", set(rows) == set(expected), str(sorted(rows)))
    for n, expected_values in expected.items():
        observed = rows.get(n)
        check(f"{label} N={n} column count", observed is not None and len(observed) == len(columns))
        if observed is None:
            continue
        for col, obs, exp in zip(columns, observed, expected_values):
            check(
                f"{label} N={n} {col}",
                abs(obs - exp) <= tol,
                f"observed={obs:.4f} expected={exp:.4f} tol={tol}",
            )


def check_sidebit_conclusions(rows: dict[int, list[float]]) -> None:
    section("Side-bit bounded conclusions")
    idx = {name: i for i, name in enumerate(SIDEBIT_COLUMNS)}
    for n in (12, 18):
        row = rows[n]
        check(f"N={n} side-bit soft improves persistent soft", row[idx["pr_side_g1"]] < row[idx["pr_g1"]])
        check(f"N={n} side-bit soft remains behind node-label", row[idx["pr_side_g1"]] > row[idx["node"]])
    check("N=18 trace does not uniformly improve", rows[18][idx["pr_side_trace"]] > rows[18][idx["pr_trace"]])


def check_refinement_conclusions(rows: dict[int, list[float]]) -> None:
    section("Refinement bounded conclusions")
    idx = {name: i for i, name in enumerate(REFINEMENT_COLUMNS)}
    row18 = rows[18]
    check("N=18 side+packet+entry g1 beats side+packet g1 slightly", row18[idx["pr_side_packet_entry_g1"]] < row18[idx["pr_side_packet_g1"]])
    check("N=18 side+packet+entry g1 remains behind node-label", row18[idx["pr_side_packet_entry_g1"]] > row18[idx["node"]])
    check("N=18 gamma 1.5 worsens against gamma 1.0", row18[idx["pr_side_packet_entry_g1.5"]] > row18[idx["pr_side_packet_entry_g1"]])
    check("N=18 gamma 2.0 worsens against gamma 1.0", row18[idx["pr_side_packet_entry_g2"]] > row18[idx["pr_side_packet_entry_g1"]])


def check_note_boundaries() -> None:
    section("Source-note boundaries")
    for note, markers in [
        (
            SIDEBIT_NOTE,
            [
                "**Claim type:** bounded_theorem",
                "node-label on raw purity",
                "Independent audit still owns any status movement",
                "scripts/audit_companion_persistent_record_sidebit_refinement_packet_2026_06_15.py",
            ],
        ),
        (
            REFINEMENT_NOTE,
            [
                "**Claim type:** bounded_theorem",
                "it still does **not** beat the node-label baseline",
                "scripts/audit_companion_persistent_record_sidebit_refinement_packet_2026_06_15.py",
            ],
        ),
    ]:
        text = note.read_text(encoding="utf-8")
        flat = " ".join(text.split())
        check(f"{note.name} exists", note.exists(), note.relative_to(ROOT).as_posix())
        for marker in markers:
            check(f"{note.name} marker: {marker[:58]}", marker in text or marker in flat)
        for forbidden in [
            "does beat the node-label baseline",
            "beats node-label outright",
            "new raw decoherence winner",
            "asymptotic closure",
        ]:
            check(f"{note.name} forbidden absent: {forbidden}", forbidden not in text)


def main() -> int:
    print("PERSISTENT RECORD SIDEBIT / REFINEMENT AUDIT PACKET")
    check_note_boundaries()
    side_stdout = run_compare(
        "sidebit",
        [
            "--seeds", "2",
            "--gamma", "1.0",
            "--methods", "node,pr_trace,pr_soft,pr_side_trace,pr_side_soft",
        ],
        timeout=120,
    )
    side_rows = parse_rows(side_stdout, SIDEBIT_COLUMNS)
    check_table("sidebit", side_rows, SIDEBIT_EXPECTED, SIDEBIT_COLUMNS, tol=0.0025)
    check_sidebit_conclusions(side_rows)

    refinement_stdout = run_compare(
        "side_packet_entry_refinement",
        [
            "--seeds", "2",
            "--gamma", "1.0,1.5,2.0",
            "--methods", "node,pr_side_packet_trace,pr_side_packet_soft,pr_side_packet_entry_trace,pr_side_packet_entry_soft",
        ],
        timeout=240,
    )
    refinement_rows = parse_rows(refinement_stdout, REFINEMENT_COLUMNS)
    check_table("refinement", refinement_rows, REFINEMENT_EXPECTED, REFINEMENT_COLUMNS, tol=0.0005)
    check_refinement_conclusions(refinement_rows)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
