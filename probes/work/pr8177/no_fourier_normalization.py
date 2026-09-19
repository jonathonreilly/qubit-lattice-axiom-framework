#!/usr/bin/env python3
"""J:attack-f:PR8177 — NORMALIZATION.

Pattern: factors of L, N, 2 pi, 1/2 and conjugation conventions in Fourier
sums, structure factors and sum rules, recomputed at small size.

This note is the rooted-value / tight-sibling / one-processed-child count
(combinatorial trees and a generating-function recursion). Scan the note for
Fourier objects; if none, the pattern has no purchase.

Do not re-find the known T2 Z_B predecessor-value HIT.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = (
    "origin/physics-loop/admissibility-induced-law-block33-rooted-inequality-"
    "tight-sibling-lemma-one-processed-child-count-20260917"
)
NOTE = (
    "docs/ADMISSIBILITY_RULE_SIX_AXIS_FORMATION_THRESHOLD_THE_ROOTED_INEQUALITY_"
    "REDUCES_THE_UNIT_BUDGET_TO_THE_TIGHT_SIBLING_LEMMA_AND_THE_ONE_PROCESSED_"
    "CHILD_COUNT_BOUNDED_THEOREM_NOTE_2026-09-17.md"
)

NEEDLES = (
    r"\bFourier\b",
    r"\bParseval\b",
    r"\bstructure factor",
    r"2\s*\\\\pi",
    r"2\s*π",
    r"\b2\s*pi\b",
    r"e\^\{ik",
    r"\bconjugation\b",
    r"\bcomplex conjugate\b",
    r"\bZ_N\b",
    r"\btorus\b",
    r"1/N\b",
    r"1/L\b",
    r"\b2\\\\pi / L",
    r"k \\\\in",
)


def git_show(path: str) -> str:
    r = subprocess.run(
        ["git", "show", f"{BRANCH}:{path}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        # fetch once if the ref is missing in this worktree
        subprocess.run(
            ["git", "fetch", "origin", BRANCH.split("origin/", 1)[-1]],
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
    note = git_show(NOTE)
    hits = []
    for pat in NEEDLES:
        ms = list(re.finditer(pat, note, flags=re.I))
        print(f"needle {pat!r}: {len(ms)}")
        for m in ms[:3]:
            i = m.start()
            ctx = note[max(0, i - 40) : i + 40].replace("\n", " ")
            print(f"  ...{ctx}...")
            hits.append(f"{pat} -> {ctx.strip()[:80]}")
    if hits:
        print("HIT: Fourier/normalization tokens present: " + hits[0])
        print(
            "SUMMARY: NORMALIZATION (PR #8177): note carries Fourier-like tokens; "
            + "; ".join(hits[:3])
        )
        return 0
    print(
        "SUMMARY: NORMALIZATION (PR #8177): no Fourier sums, structure factors, "
        "2 pi, 1/L, 1/N, torus, or conjugation conventions in the rooted-inequality "
        "/ tight-sibling note; pattern has no purchase"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
