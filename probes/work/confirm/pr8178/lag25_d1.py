#!/usr/bin/env python3
"""J:confirm:J-provenance:PR8178 — independent lag-25 D_1 and linear-ratio check.

Finder (claude-opus-5) compared claim_scope's 1.18 at (beta,L)=(12,32) to
the torus_msd control using float rounding. This script parses the control
with Decimal and does not reuse the finder's ITEMS loop.
"""
from __future__ import annotations

import re
import subprocess
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
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
LIN_LO, LIN_HI = Decimal("0.97"), Decimal("1.01")


def git_show(path: str) -> str:
    r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return r.stdout


def main() -> None:
    text = git_show(MSD)
    lag25: dict[tuple[int, int], Decimal] = {}
    lin: list[tuple[Decimal, int, int, int]] = []
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

    hits: list[str] = []
    for key, stated in STATED.items():
        got = lag25.get(key)
        print(f"D1 lag25 {key}: stated {stated} control {got}")
        if got is None:
            hits.append(f"missing lag-25 at {key}")
        elif got != stated and abs(got - stated) >= Decimal("0.005"):
            # more than a half-cent difference from the two-decimal claim
            hits.append(f"{key} stated {stated} vs lag-25 {got}")

    lo = min(lin)
    hi = max(lin)
    print(f"linear ratios min {lo[0]} (beta={lo[1]} L={lo[2]} lag={lo[3]}) max {hi[0]} (beta={hi[1]} L={hi[2]} lag={hi[3]})")
    print(f"stated linear range {LIN_LO}-{LIN_HI}")
    if lo[0] < LIN_LO or hi[0] > LIN_HI:
        hits.append(f"linear ratios {lo[0]}..{hi[0]} vs stated {LIN_LO}-{LIN_HI}")

    if hits:
        print("HIT: confirmed - " + "; ".join(hits))
        print("SUMMARY: confirmed executed-number mismatch: " + "; ".join(hits))
    else:
        print("SUMMARY: not reproduced - lag-25 D_1 and linear ratios match the claim_scope")


if __name__ == "__main__":
    main()
