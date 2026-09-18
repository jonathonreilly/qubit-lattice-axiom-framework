#!/usr/bin/env python3
"""J:attack:PR8180 - block 35, attack pattern (c) EXECUTED NUMBERS.

Claim_scope: on 256x256 at beta=6,12,24 the equal-level structure factor is
the linearized kernel times a normalization 0.83-0.89, 0.90-0.94, 0.94-0.97
(rising with |k| and with beta). This script parses the kernel_sim control
with Decimal (shell 'mean ratio' lines and D(r) ratios) and does not reuse
the provenance ITEMS loop.

HIT if a stated range misses the control shells, or the shells do not rise
with |k|.
"""
from __future__ import annotations

import re
import subprocess
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HEAD = "7c844adf7555a3558729be69179646f6a83a1539"
NOTE = (
    "docs/ADMISSIBILITY_RULE_GRAVITY_NODE_KERNEL_UNDER_THE_FORMATION_READING_A_HEAT_KERNEL_IN_LEVEL_TIME_"
    "TIMES_A_PLANE_GREEN_FUNCTION_NOT_THE_COMPARATORS_THREE_DIMENSIONAL_GREEN_FUNCTION_BOUNDED_THEOREM_NOTE_2026-09-18.md"
)
CTRL = (
    ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/"
    "supervisor_control_block35_kernel_sim.out.txt"
)


def git_show(path: str) -> str:
    r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return r.stdout


def parse_shells(text: str) -> dict[int, list[tuple[str, Decimal, int]]]:
    out: dict[int, list[tuple[str, Decimal, int]]] = {}
    beta = None
    for line in text.splitlines():
        m = re.match(r"beta=([0-9.]+)\b", line)
        if m:
            beta = int(Decimal(m.group(1)))
            out.setdefault(beta, [])
            continue
        m = re.search(r"\|k\| in (\[[0-9.,]+\)): mean ratio ([0-9.]+) \(n=(\d+)\)", line)
        if m and beta is not None:
            out[beta].append((m.group(1), Decimal(m.group(2)), int(m.group(3))))
    return out


def main() -> None:
    note = git_show(NOTE)
    ctrl = git_show(CTRL)
    fm = note.split("\n---\n", 1)[0]
    m = re.search(
        r"times a normalization ([0-9.]+)-([0-9.]+), ([0-9.]+)-([0-9.]+), ([0-9.]+)-([0-9.]+) \(rising with \|k\|",
        fm,
    )
    if not m:
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; claim_scope normalization sentence not found")
        return
    stated = {
        6: (Decimal(m.group(1)), Decimal(m.group(2))),
        12: (Decimal(m.group(3)), Decimal(m.group(4))),
        24: (Decimal(m.group(5)), Decimal(m.group(6))),
    }
    print(f"claim_scope ranges: {stated}")
    shells = parse_shells(ctrl)
    hits: list[str] = []
    prev_hi: Decimal | None = None
    for beta in (6, 12, 24):
        vals = shells.get(beta, [])
        if not vals:
            hits.append(f"beta={beta}: no shells in control")
            continue
        ratios = [v for _, v, _ in vals]
        lo, hi = min(ratios), max(ratios)
        pair = stated[beta]
        mono = all(ratios[i] <= ratios[i + 1] for i in range(len(ratios) - 1))
        in_range = pair[0] <= lo and hi <= pair[1]
        print(f"beta={beta}: shells {[(s, str(v)) for s, v, _ in vals]}")
        print(f"  min {lo} max {hi}; stated {pair[0]}-{pair[1]}; in_range={in_range}; monotone={mono}")
        if not in_range:
            hits.append(f"beta={beta} control {lo}..{hi} vs stated {pair[0]}-{pair[1]}")
        if not mono:
            dips = [
                f"{vals[i][0]}={vals[i][1]} > {vals[i+1][0]}={vals[i+1][1]}"
                for i in range(len(ratios) - 1)
                if ratios[i] > ratios[i + 1]
            ]
            hits.append(f"beta={beta} shell ratios not increasing in |k| ({'; '.join(dips)})")
        if prev_hi is not None and hi <= prev_hi:
            hits.append(f"beta={beta} max {hi} did not rise vs previous max {prev_hi}")
        prev_hi = hi

    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; " + "; ".join(hits))
    else:
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; every stated shell range contains the control means and they rise with |k| and beta")


if __name__ == "__main__":
    main()
