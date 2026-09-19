#!/usr/bin/env python3
"""J:provenance:PR8025 — theorem numbers vs runner cache."""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/codex/local-observable-block35-20260907"
CACHE = "logs/runner-cache/gauge_wilson_local_observable_finite_region_pw_2026_09_07.txt"

ITEMS = [
    ("29", "named checks"),
    ("4", "plaquettes per link / crossing at r=0"),
    ("3", "N<=3|X|(2r+1)^3 prefactor"),
    ("81", "cap at r=1"),
    ("13", "|B_1| links"),
    ("32", "32 v in Theta_d(32 v |t|) / retained_faces r=2"),
    ("16", "16v subsequent face weight"),
]


def git_show(path: str) -> str:
    r = subprocess.run(
        ["git", "show", f"{BRANCH}:{path}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        subprocess.run(
            ["git", "fetch", "origin", "codex/local-observable-block35-20260907"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        r = subprocess.run(
            ["git", "show", f"{BRANCH}:{path}"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
    if r.returncode != 0:
        raise SystemExit((r.stderr or r.stdout)[:400])
    return r.stdout


def main() -> int:
    cache = git_show(CACHE)
    uncovered = []
    for token, role in ITEMS:
        ok = token in cache
        print(f"{token:8} {'CACHE' if ok else 'MISSING'}  {role}")
        if not ok:
            uncovered.append(f"{token} ({role})")
    if uncovered:
        print("HIT: unsourced " + "; ".join(uncovered))
        print("SUMMARY: provenance (PR #8025): UNCOVERED " + "; ".join(uncovered))
        return 0
    print(
        f"SUMMARY: provenance (PR #8025): all {len(ITEMS)} listed theorem "
        "tokens appear in the runner cache (29 checks, 4 plaquettes/link, "
        "3|X|(2r+1)^3, 32v); no UNCOVERED"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
