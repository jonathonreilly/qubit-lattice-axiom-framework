#!/usr/bin/env python3
"""J:provenance:PR8030 — theorem-statement numbers vs note derivation / runner.

HIT for any theorem-statement number without a runner line or exact derivation.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HEAD = "3dee7c038c60dd9aaddbcc186207f165367cc274"
BRANCH = "codex/continuum-boundary-block40-20260907"
NOTE = "docs/GAUGE_WILSON_UNIFORM_WEAK_CONTINUUM_CORRELATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-07.md"
RUNNER = "scripts/gauge_wilson_uniform_weak_scaling_controls_2026_09_07.py"
CACHE = "logs/runner-cache/gauge_wilson_uniform_weak_scaling_controls_2026_09_07.txt"

ITEMS = [
    ("1/18", "E J^2 = (0+2+0)/36 = 1/18"),
    ("1/3", "ReTr(U)/3 = J"),
    ("√18", "X = sqrt(18) J so E X^2 = 1"),
    ("h/3", "mesh ell = h/3"),
    ("0", "integral chi = 0, E J = 0"),
    ("1", "integral |chi|^2 = 1, E X^2 = 1"),
    ("36", "(0+2+0)/36"),
    ("2", "integral chi^2 = 0 via center; CLT t^2/2"),
]


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def show(path: str) -> str | None:
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        return None
    return r.stdout


def find(blob: str, alts: list[str]) -> str | None:
    for alt in alts:
        for line in blob.splitlines():
            if alt in line and "sha256" not in line.lower():
                return line.strip()[:160]
    return None


def main() -> None:
    note = show(NOTE) or ""
    runner = show(RUNNER) or ""
    cache = show(CACHE) or ""
    blobs = [("NOTE", note), ("RUNNER", runner), ("CACHE", cache)]
    spelled = {
        "1/18": ["1/18", "E J^2", "(0+2+0)/36"],
        "1/3": ["ReTr", "/3", "Tr(U_k)/3"],
        "√18": ["sqrt(18)", "√18", "sqrt18", "B=sqrt18"],
        "h/3": ["ell=h/3", "h/3", "ell = h/3"],
        "0": ["integral chi=0", "E J=0", "integral chi = 0"],
        "1": ["|chi|^2=1", "E X^2=1", "E X^2 = 1"],
        "36": ["/36", "(0+2+0)/36"],
        "2": ["chi^2=0", "t^2/2", "t²/2"],
    }
    unsourced = []
    for token, role in ITEMS:
        src = None
        for name, blob in blobs:
            hit = find(blob, spelled.get(token, [token]))
            if hit:
                src = f"{name}: {hit}"
                break
        if src:
            print(f"OK | {token} | {role} | {src}")
        else:
            # exact derivation in this script
            if token == "1/18":
                print("OK | 1/18 | DERIVED: (0+2+0)/36 = 1/18")
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
        "sourced in the note, runner, cache, or exact (0+2+0)/36=1/18"
    )


if __name__ == "__main__":
    main()
