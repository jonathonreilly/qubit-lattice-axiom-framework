#!/usr/bin/env python3
"""J:confirm:J-provenance:PR8173 — independent check of the 0.86-0.98 range HIT.

Finder (opus-max-1 / claude-opus-5) logged that claim_scope's executed range
'0.86-0.98 for n >= 2' disagrees with the kernel control output. This script
does not reuse the finder's regex ITEMS loop or float rounding. It:

  * pulls the claim_scope sentence and the note's markdown table from git
  * parses the kernel control file with Decimal on the printed 3-dp tokens
  * treats the first token of each 'n  beta E(k) S_perp(k):' line as n = 1
    and the rest as n >= 2 (k = 2 pi n / L along e_1)

HIT if the control's n >= 2 values leave the stated 0.86-0.98 interval.
"""
from __future__ import annotations

import re
import subprocess
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HEAD = "e5b3aa31686d88d8a2fe0aad5e938acac0e39404"
NOTE = (
    "docs/ADMISSIBILITY_RULE_TRANSVERSE_KERNEL_NORMALIZATION_IN_THE_ORDERED_SPHERE_STATIC_LAW_"
    "MEASURED_BETWEEN_THE_BOUNDS_WITH_THE_TRANSVERSE_SUM_RULE_AND_THE_SPIN_WAVE_REFERENCE_"
    "BOUNDED_THEOREM_NOTE_2026-09-16.md"
)
KER = (
    ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/"
    "supervisor_control_block29_kernel.out.txt"
)
STATED_LO = Decimal("0.86")
STATED_HI = Decimal("0.98")


def git_show(path: str) -> str:
    r = subprocess.run(
        ["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True
    )
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return r.stdout


def parse_kernel(text: str) -> list[tuple[int, Decimal, int, Decimal]]:
    """Return (L, beta, n, c) for each printed c = beta E(k) S_perp(k)."""
    rows: list[tuple[int, Decimal, int, Decimal]] = []
    L = None
    beta = None
    for line in text.splitlines():
        m = re.match(r"===== kernel_L(\d+) =====", line)
        if m:
            L = int(m.group(1))
            continue
        m = re.match(r"\s+beta=([0-9.]+):", line)
        if m:
            beta = Decimal(m.group(1))
            continue
        m = re.search(r"n  beta E\(k\) S_perp\(k\):\s*(.+)$", line)
        if m and L is not None and beta is not None:
            toks = [Decimal(t) for t in m.group(1).split()]
            for i, c in enumerate(toks, start=1):
                rows.append((L, beta, i, c))
    return rows


def parse_note_table(note: str) -> list[Decimal]:
    """Two-decimal tokens in the executed-grid markdown table, skipping n = 1."""
    rest: list[Decimal] = []
    for line in note.splitlines():
        if not re.match(r"\| `\d+` \| `", line):
            continue
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        vals = [Decimal(t) for t in cells[-1].split()]
        rest.extend(vals[1:])
    return rest


def main() -> None:
    note = git_show(NOTE)
    ker = git_show(KER)
    fm = note.split("\n---\n", 1)[0]
    m = re.search(r'lies at ([0-9.]+)-([0-9.]+) for the modes n >= 2', fm)
    if not m:
        print("SUMMARY: not reproduced - claim_scope range sentence not found")
        return
    scope_lo, scope_hi = Decimal(m.group(1)), Decimal(m.group(2))
    print(f"claim_scope range: {scope_lo}-{scope_hi} (stated {STATED_LO}-{STATED_HI})")

    rows = parse_kernel(ker)
    n2 = [(L, b, n, c) for L, b, n, c in rows if n >= 2]
    n1 = [(L, b, n, c) for L, b, n, c in rows if n == 1]
    grids = sorted({(L, b) for L, b, _, _ in rows})
    print(f"control rows: {len(rows)} values, {len(grids)} (L,beta) pairs, n>=2 count {len(n2)}")
    lo = min(n2, key=lambda t: t[3])
    hi = max(n2, key=lambda t: t[3])
    print(f"n>=2 min {lo[3]} at L={lo[0]} beta={lo[1]} n={lo[2]}")
    print(f"n>=2 max {hi[3]} at L={hi[0]} beta={hi[1]} n={hi[2]}")
    if n1:
        print(f"n=1 min {min(t[3] for t in n1)} max {max(t[3] for t in n1)}")

    table_n2 = parse_note_table(note)
    if table_n2:
        print(f"note table n>=2 min {min(table_n2)} max {max(table_n2)}")

    body = re.search(r"between `([0-9.]+)` and `([0-9.]+)` at every lattice", note)
    if body:
        print(f"note 'What the runs say (i)': {body.group(1)}-{body.group(2)}")

    outside = [t for t in n2 if t[3] < scope_lo or t[3] > scope_hi]
    print(f"n>=2 values outside claim_scope [{scope_lo},{scope_hi}]: {len(outside)}")
    for t in sorted(outside, key=lambda x: x[3], reverse=True)[:6]:
        print(f"  outside: L={t[0]} beta={t[1]} n={t[2]} c={t[3]}")

    if scope_lo == STATED_LO and scope_hi == STATED_HI and outside:
        print(
            f"HIT: confirmed - claim_scope states {scope_lo}-{scope_hi} for n>=2 but "
            f"kernel control has min {lo[3]} max {hi[3]} "
            f"(max at L={hi[0]} beta={hi[1]} n={hi[2]}); "
            f"{len(outside)} of {len(n2)} n>=2 values leave the interval"
        )
        print(
            "SUMMARY: confirmed range mismatch: executed c(beta,k) for n>=2 "
            f"spans {lo[3]}-{hi[3]} against claim_scope {scope_lo}-{scope_hi}"
        )
    elif not outside:
        print(
            "SUMMARY: not reproduced - every n>=2 control value lies in the "
            f"claim_scope interval {scope_lo}-{scope_hi}"
        )
    else:
        print("SUMMARY: not reproduced - claim_scope range tokens were not 0.86-0.98")


if __name__ == "__main__":
    main()
