#!/usr/bin/env python3
"""J:confirm:J-provenance:PR8180 — independent check of the beta=12 0.90-0.94 HIT.

Finder (opus-max-1 / claude-opus-5) logged that claim_scope's executed
normalization 0.90-0.94 at beta=12 disagrees with the kernel_sim control,
and that shell ratios do not rise with |k|. This script does not reuse the
finder's ITEMS loop or float rounding. It parses 'mean ratio' lines with
Decimal, grouped by the 'beta=' block headers.
"""
from __future__ import annotations

import re
import subprocess
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HEAD = "7c844adf7555a3558729be69179646f6a83a1539"
NOTE = (
    "docs/ADMISSIBILITY_RULE_GRAVITY_NODE_KERNEL_UNDER_THE_FORMATION_READING_A_HEAT_KERNEL_IN_LEVEL_TIME_"
    "TIMES_A_PLANE_GREEN_FUNCTION_NOT_THE_COMPARATORS_THREE_DIMENSIONAL_GREEN_FUNCTION_BOUNDED_THEOREM_NOTE_2026-09-18.md"
)
CTRL = (
    ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/"
    "supervisor_control_block35_kernel_sim.out.txt"
)
STATED = {6: (Decimal("0.83"), Decimal("0.89")), 12: (Decimal("0.90"), Decimal("0.94")), 24: (Decimal("0.94"), Decimal("0.97"))}


def git_show(path: str) -> str:
    r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return r.stdout


def parse_shells(text: str) -> dict[int, list[tuple[str, Decimal]]]:
    out: dict[int, list[tuple[str, Decimal]]] = {}
    beta = None
    for line in text.splitlines():
        m = re.match(r"beta=([0-9.]+)\b", line)
        if m:
            beta = int(Decimal(m.group(1)))
            out.setdefault(beta, [])
            continue
        m = re.search(r"\|k\| in (\[[0-9.,]+\)): mean ratio ([0-9.]+)", line)
        if m and beta is not None:
            out[beta].append((m.group(1), Decimal(m.group(2))))
    return out


def main() -> None:
    note = git_show(NOTE)
    ctrl = git_show(CTRL)
    fm = note.split("\n---\n", 1)[0]
    m = re.search(r"times a normalization ([0-9.]+)-([0-9.]+), ([0-9.]+)-([0-9.]+), ([0-9.]+)-([0-9.]+) \(rising with \|k\|", fm)
    if not m:
        print("SUMMARY: not reproduced - claim_scope normalization sentence not found")
        return
    stated = {
        6: (Decimal(m.group(1)), Decimal(m.group(2))),
        12: (Decimal(m.group(3)), Decimal(m.group(4))),
        24: (Decimal(m.group(5)), Decimal(m.group(6))),
    }
    print(f"claim_scope ranges: {stated}")
    shells = parse_shells(ctrl)
    hits: list[str] = []
    for beta, pair in stated.items():
        vals = shells.get(beta, [])
        if not vals:
            print(f"beta={beta}: no shells parsed")
            continue
        ratios = [v for _, v in vals]
        lo, hi = min(ratios), max(ratios)
        mono = all(ratios[i] <= ratios[i + 1] for i in range(len(ratios) - 1))
        in_range = pair[0] <= lo and hi <= pair[1]
        print(f"beta={beta}: shells {[(s, str(v)) for s, v in vals]}")
        print(f"  min {lo} max {hi}; stated {pair[0]}-{pair[1]}; in_range={in_range}; monotone={mono}")
        if not in_range:
            hits.append(f"beta={beta} control {lo}..{hi} vs stated {pair[0]}-{pair[1]}")
        if not mono:
            hits.append(f"beta={beta} shell ratios not increasing in |k|")

    if hits:
        print("HIT: confirmed - " + "; ".join(hits))
        print("SUMMARY: confirmed control mismatch: " + "; ".join(hits))
    else:
        print("SUMMARY: not reproduced - every stated shell range contains the control means and they rise with |k|")


if __name__ == "__main__":
    main()
