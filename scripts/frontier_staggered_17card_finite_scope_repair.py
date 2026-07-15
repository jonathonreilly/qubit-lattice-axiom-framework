#!/usr/bin/env python3
"""Finite-scope wrapper for the canonical staggered 17-card runner."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "STAGGERED_FERMION_CARD_2026-04-11.md"
CANONICAL_RUNNER = ROOT / "scripts" / "frontier_staggered_17card.py"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if ok else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def check_note_boundary() -> None:
    section("Source-note boundary")
    text = NOTE_PATH.read_text()
    normalized = " ".join(text.split())
    required = [
        "bounded-support finite runner certificate",
        "That fixed finite runner certificate is the entire repaired theorem.",
        "This repair withdraws those physical and framework-realization claims from the binding theorem.",
        "The bridge from this finite runner certificate to a physical staggered-gravity theorem remains a separate open science problem.",
    ]
    for needle in required:
        check(f"note contains required boundary: {needle!r}", needle in normalized)

    forbidden = [
        "screened-Poisson bridge is derived",
        "physical gravity is derived",
        "attraction is derived",
        "universal graph-family theorem is derived",
        "framework-native staggered-Dirac realization is derived",
    ]
    for needle in forbidden:
        check(f"note avoids overclaim phrase: {needle!r}", needle not in normalized)


def run_canonical_runner() -> str:
    section("Canonical runner execution")
    env = dict(os.environ)
    env["PYTHONPATH"] = str(ROOT / "scripts") + os.pathsep + env.get("PYTHONPATH", "")
    result = subprocess.run(
        [sys.executable, str(CANONICAL_RUNNER)],
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=900,
        check=False,
    )
    check("canonical runner exits cleanly", result.returncode == 0, f"returncode={result.returncode}")
    if result.stderr.strip():
        print("  canonical stderr:")
        print(result.stderr.strip())
    return result.stdout


def parse_score_blocks(output: str) -> dict[str, int]:
    labels: dict[str, int] = {}
    current = None
    for line in output.splitlines():
        if line.startswith("1D CARD:"):
            current = "1d_n61"
        elif line.startswith("3D CARD (n=9):"):
            current = "3d_n9"
        elif line.startswith("3D CARD (n=11):"):
            current = "3d_n11"
        elif line.startswith("3D CARD (n=13):"):
            current = "3d_n13"
        m = re.search(r"SCORE:\s+(\d+)/17", line)
        if current and m:
            labels[current] = int(m.group(1))
    return labels


def check_finite_scores(output: str) -> None:
    section("Finite card score checks")
    scores = parse_score_blocks(output)
    expected = {
        "1d_n61": 17,
        "3d_n9": 17,
        "3d_n11": 17,
        "3d_n13": 17,
    }
    check("all four finite card blocks were parsed", set(scores) == set(expected), str(scores))
    for label, want in expected.items():
        got = scores.get(label)
        check(f"{label} score is {want}/17", got == want, f"got={got}")
    check("3D n=11 family-coverage gate is stated", "C17 tested 4/6 families" in output)
    check("3D n=13 family-coverage gate is stated", output.count("C17 tested 4/6 families") >= 2)
    print("  parsed_scores =", scores)


def check_scope_negative_controls(output: str) -> None:
    section("Scope negative controls")
    canonical_source = CANONICAL_RUNNER.read_text() if CANONICAL_RUNNER.is_file() else ""
    load_bearing_markers = (
        "def staggered_H(",
        "def staggered_H_3d(",
        "def evolve_cn(",
        "def run_card(",
        "for n3 in [9, 11, 13]",
    )
    check(
        "canonical source exposes the load-bearing finite-card implementation",
        all(marker in canonical_source for marker in load_bearing_markers),
    )
    check("wrapper does not claim screened-Poisson derivation", "screened-Poisson bridge is derived" not in NOTE_PATH.read_text())
    check("canonical output is treated as finite runner output", "SCORE:" in output)


def main() -> int:
    print("Staggered canonical 17-card finite-scope repair")
    check_note_boundary()
    output = run_canonical_runner()
    check_finite_scores(output)
    check_scope_negative_controls(output)
    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
