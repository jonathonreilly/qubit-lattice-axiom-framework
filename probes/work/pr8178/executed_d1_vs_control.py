#!/usr/bin/env python3
"""J:attack:PR8178 — pattern (c) EXECUTED NUMBERS: claim_scope D1 ratios vs torus_msd.

claim_scope names D_1/(sigma^2/L^2) = 1.34, 1.14, 1.06, 1.02 at beta=6,12,24,48
(L=16) and 1.42, 1.18 at L=32 for beta=6,12, plus linear-model 0.97-1.01.
Parsed from supervisor_control_block34_torus_msd.out.txt with Decimal.
"""
from __future__ import annotations

import re
import subprocess
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HEAD = "e6ffae5b460b9ec0fd0d99c99f9784232bd225bd"
MSD = (
    ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/"
    "supervisor_control_block34_torus_msd.out.txt"
)
STATED = {
    (6, 16): Decimal("1.34"),
    (12, 16): Decimal("1.14"),
    (24, 16): Decimal("1.06"),
    (48, 16): Decimal("1.02"),
    (6, 32): Decimal("1.42"),
    (12, 32): Decimal("1.18"),
}


def git_show(path: str) -> str:
    r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return r.stdout


def main() -> None:
    text = git_show(MSD)
    lag25 = {}
    lin = []
    beta = L = None
    for line in text.splitlines():
        m = re.match(r"beta=([0-9.]+) L=(\d+)", line)
        if m:
            beta, L = int(Decimal(m.group(1))), int(m.group(2))
            continue
        m = re.search(
            r"lag +(\d+): nonlinear MSD .*ratio to sigma\^2/L\^2: ([0-9.]+) .*linear model MSD .* \(ratio ([0-9.]+)",
            line,
        )
        if m and beta is not None:
            lag, nl, li = int(m.group(1)), Decimal(m.group(2)), Decimal(m.group(3))
            lin.append((li, beta, L, lag))
            if lag == 25:
                lag25[(beta, L)] = nl
    hits = []
    for key, stated in STATED.items():
        got = lag25.get(key)
        print(f"D1 lag25 {key}: stated {stated} control {got}")
        if got is None or abs(got - stated) >= Decimal("0.005"):
            hits.append(f"{key} stated {stated} vs lag-25 {got}")
    lo, hi = min(lin), max(lin)
    print(f"linear ratios {lo[0]}..{hi[0]} stated 0.97-1.01")
    if lo[0] < Decimal("0.97") or hi[0] > Decimal("1.01"):
        hits.append(f"linear {lo[0]}..{hi[0]} vs 0.97-1.01")
    if hits:
        print("HIT: " + "; ".join(hits))
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS - " + "; ".join(hits))
    else:
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS - lag-25 D1 and linear ratios match; does not fire")


if __name__ == "__main__":
    main()
