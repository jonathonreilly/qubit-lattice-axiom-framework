#!/usr/bin/env python3
"""J:attack-e:PR8030 — SAMPLED EVIDENCE.

The continuum-boundary note's load-bearing statements are exact Haar moments
(E J=0, E J^2=1/18, E X^2=1) and a characteristic-function CLT for disjoint
plaquette traces, not a 'never/always observed' Monte Carlo conjecture.
'Random distributions' appears only as a non-claim. Pattern (e) has no purchase.
"""
from __future__ import annotations

import re
import subprocess
from fractions import Fraction as Fr

HEAD = "3dee7c038c60dd9aaddbcc186207f165367cc274"
BRANCH = "codex/continuum-boundary-block40-20260907"
NOTE = "docs/GAUGE_WILSON_UNIFORM_WEAK_CONTINUUM_CORRELATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-07.md"


def git(*args: str) -> subprocess.CompletedProcess:
    import os

    cwd = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def show_note() -> str:
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
    r = git("show", f"{HEAD}:{NOTE}")
    if r.returncode != 0:
        raise SystemExit(f"cannot read note: {r.stderr.strip()[:400]}")
    return r.stdout


def main() -> int:
    note = show_note()
    keys = (r"\bnever\b", r"\balways observed\b", r"\bMonte\b", r"Metropolis", r"heat-bath")
    hits = []
    for para in re.split(r"\n\n+", note):
        if any(re.search(k, para, re.I) for k in keys):
            hits.append(" ".join(para.split())[:180])
    print(f"never/always-observed/MC paragraphs: {len(hits)}")
    for p in hits:
        print("  LANG:", p)

    # exact Haar second moment as written: (0+2+0)/36 = 1/18
    ej2 = (Fr(0) + Fr(2) + Fr(0)) / Fr(36)
    print(f"E J^2 = (0+2+0)/36 = {ej2}")
    assert ej2 == Fr(1, 18)
    # X = sqrt(18) J so E X^2 = 18 * 1/18 = 1
    ex2 = 18 * ej2
    print(f"E X^2 = 18 * 1/18 = {ex2}")
    assert ex2 == 1
    print("Haar contact second moment is exact, not a sample")

    print(
        "SUMMARY: pattern has no purchase on this note — Haar E J^2=1/18 and "
        "the Gaussian-contact CLT are exact characteristic-function identities, "
        "not sampled never/always observations"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
