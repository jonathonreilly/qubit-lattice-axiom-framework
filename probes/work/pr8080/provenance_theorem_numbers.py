#!/usr/bin/env python3
"""J:provenance:PR8080 — theorem-statement numbers vs note derivation / runner / check.py.

HIT for any theorem-statement number without a runner line, cache line, or
exact derivation in the note.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HEAD = "ac7bc8d614a67cec5a86d59253be17bf04b98f34"
BRANCH = "codex/native-stronger-ward-20260910"
NOTE = "docs/NATIVE_STRONGER_WARD_ESTIMATORS_NOTE_2026-09-10.md"
RUNNER = "scripts/native_stronger_ward_estimators_2026_09_10.py"
CHECKER = (
    ".claude/science/physics-loops/native-stronger-ward-20260910/"
    "source_draft/check.py"
)

# Theorem-statement / result-up-front numbers (not review-record RSS).
ITEMS = [
    ("h/4", "δ = h/4 in D_A ≥ δ"),
    ("2√2", "j = 2√2 h in J_A* J_A = j² I"),
    ("15", "fifteen two-link channels"),
    ("6", "adjacency T of norm 6 / posterior prefactor 6"),
    ("8", "8α = Re(<x,Tx>−<x,Tg v>)"),
    ("√15", "X = √15/δ and V = j√15/δ²"),
    ("12", "12 s0_P in a²"),
    ("3", "3 s0_O in a²"),
    ("90", "ninety ordered terms"),
    ("2", "tau+2δ in A=(tau+2δ)/(δ² tau³)"),
    ("3", "3 tau − 2λ in Q_tau"),
]


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def show(path: str) -> str:
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit(f"cannot read {path}: {r.stderr.strip()[:400]}")
    return r.stdout


def find(blob: str, token: str) -> str | None:
    spelled = {
        "h/4": ["δ=h/4", "delta=h/4", "h/4"],
        "2√2": ["j=2√2", "2√2h", "2*sqrt(2)", r"2\sqrt2"],
        "√15": ["√15/δ", "sqrt(15)", r"\sqrt{15}"],
        "15": ["fifteen two-link", "fifteen channels"],
        "90": ["ninety ordered", "90 ordered"],
        "12": ["12s0_P", "12 s0_P", "12*s0"],
        "6": ["norm6", "norm 6", "at most6", "≤6[", "<=6["],
        "8": ["8α", "8h²", "8h^2", "(8h"],
        "2": ["tau+2δ", "2δ", "+2delta"],
        "3": ["3s0_O", "3 s0_O", "3q_O", "3 tau"],
    }
    alts = spelled.get(token, [token])
    for alt in alts:
        for line in blob.splitlines():
            if "sha256" in line.lower():
                continue
            if alt in line:
                return line.strip()[:160]
    return None


def main() -> None:
    note = show(NOTE)
    runner = show(RUNNER)
    checker = show(CHECKER)
    blobs = [("NOTE", note), ("RUNNER", runner), ("CHECKER", checker)]
    unsourced = []
    for token, role in ITEMS:
        src = None
        for name, blob in blobs:
            hit = find(blob, token)
            if hit:
                src = f"{name}: {hit}"
                break
        if src:
            print(f"OK | {token} | {role} | {src}")
        else:
            print(f"UNSOURCED | {token} | {role}")
            unsourced.append(f"{token} ({role})")
    if unsourced:
        for u in unsourced:
            print("HIT:", u)
        print("SUMMARY: provenance FIRED; unsourced: " + "; ".join(unsourced))
        return
    print(
        f"SUMMARY: provenance OK — {len(ITEMS)} theorem-statement numbers "
        "sourced in the note derivation, runner, or check.py"
    )


if __name__ == "__main__":
    main()
