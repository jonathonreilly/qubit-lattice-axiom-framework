#!/usr/bin/env python3
"""J:attack-f:PR8150 — NORMALIZATION.

Pattern: L, N, 2 pi, 1/2, conjugation in Fourier sums / structure factors.
This note is flip-monotonicity of sequential vs static laws on windows of
Z^3. Scan the note; if no Fourier objects, the pattern has no purchase.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = (
    "origin/physics-loop/admissibility-induced-law-block16-static-law-not-a-"
    "mixture-of-formation-laws-20260915"
)
NOTE = (
    "docs/ADMISSIBILITY_RULE_STATIC_LAW_IS_NOT_A_MIXTURE_OF_FORMATION_LAWS_"
    "ON_ANY_WINDOW_WITH_A_CYCLE_FLIP_MONOTONICITY_BOUNDED_THEOREM_NOTE_2026-09-15.md"
)
NEEDLES = (
    r"\bFourier\b",
    r"\bParseval\b",
    r"\bstructure factor",
    r"2\s*π",
    r"\b2\s*pi\b",
    r"e\^\{ik",
    r"\bconjugation\b",
    r"\bcomplex conjugate\b",
    r"\btorus\b",
    r"1/N\b",
    r"1/L\b",
)


def git_show(path: str) -> str:
    r = subprocess.run(
        ["git", "show", f"{BRANCH}:{path}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
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
            "SUMMARY: NORMALIZATION (PR #8150): note carries Fourier-like tokens; "
            + "; ".join(hits[:3])
        )
        return 0
    print(
        "SUMMARY: NORMALIZATION (PR #8150): no Fourier sums, structure factors, "
        "2 pi, 1/L, 1/N, torus, or conjugation conventions in the static-vs-mixture "
        "flip-monotonicity note; pattern has no purchase"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
