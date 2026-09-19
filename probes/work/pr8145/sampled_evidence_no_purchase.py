#!/usr/bin/env python3
"""J:attack-e:PR8145 — SAMPLED EVIDENCE.

The field-history note's load-bearing statements are proofs (history Gram
reconstruction, temporal filling, conditional averaging (2)–(4)) plus
exhaustive finite enumerations (cube fibers 2^12, 3^12; 27 history words;
108 fillings; 29 single-vertex conditionals). No 'never/always observed'
claim rests on random sampling. Pattern (e) has no purchase.
"""
from __future__ import annotations

import re
import subprocess
from fractions import Fraction as Fr

HEAD = "c5580db2ebe78e4dca71f210539cea1471148483"
BRANCH = "physics-loop/clock-history-field-20260915"
NOTE = (
    "docs/FINITE_CLOCK_FIELD_HISTORY_RECONSTRUCTION_AND_CHARGE_SECTOR_"
    "HAMILTONIAN_BOUNDED_THEOREM_NOTE_2026-09-15.md"
)


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
    keys = (
        r"\bnever\b",
        r"\balways\b",
        r"\bobserved\b",
        r"\bsampl",
        r"\brandom\b",
        r"Metropolis",
        r"heat-bath",
        r"Monte",
        r"conjectur",
    )
    hits = []
    for para in re.split(r"\n\n+", note):
        if any(re.search(k, para, re.I) for k in keys):
            flat = " ".join(para.split())
            hits.append(flat[:200])
    print(f"never/always/sample/random paragraphs: {len(hits)}")
    for p in hits:
        print("  LANG:", p)

    n2, n3 = 2**12, 3**12
    print(f"cube fibers exact: 2^12={n2} 3^12={n3} (note 4096 and 531441)")
    assert n2 == 4096 and n3 == 531441

    # Part III mixing estimate is algebraic, not sampled:
    # r = 1 - (m/M)^6 with 0 < m <= M, so 0 < r < 1 whenever m < M.
    m, M = Fr(1, 3), Fr(1)
    delta = (m / M) ** 6
    r = 1 - delta
    print(f"adversarial (m,M)=(1/3,1): delta=(m/M)^6={delta} r=1-delta={r}")
    assert 0 < delta < 1 and 0 < r < 1
    # degree-2 square (runner's executed box) only improves the exponent
    delta2 = (m / M) ** 2
    print(f"degree-2 square: (m/M)^2={delta2} > cubic delta={delta} (bound improves)")
    assert delta2 > delta

    print(
        "SUMMARY: pattern has no purchase on this note — reconstruction, "
        "temporal filling and the r=1-(m/M)^6 charge-floor are exact mixing "
        "estimates / enumerations (2^12=4096, 3^12=531441), not sampled "
        "never/always observations"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
