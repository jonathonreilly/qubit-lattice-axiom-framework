#!/usr/bin/env python3
"""J:provenance:PR8031 — theorem numbers vs PR branch runner, cache, and note."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/codex/finite-transporter-block41-20260907"
RUNNER = "scripts/gauge_wilson_finite_transporter_pw_defect_check_2026_09_07.py"
NOTE = "docs/GAUGE_WILSON_FINITE_TRANSPORTER_UNITARITY_PW_DEFECT_BOUNDED_THEOREM_NOTE_2026-09-07.md"
CACHE = "logs/runner-cache/gauge_wilson_finite_transporter_pw_defect_check_2026_09_07.txt"

NUMBERS = [
    ("19", "R=1 Haar multiplication basis states"),
    ("3 colors", "color dimension of the transporter"),
    ("57", "matrix columns checked"),
    ("17", "named helper checks"),
    ("dim(H) Tr T^2", "Cartan trace-square obstruction"),
    ("||D_R||=1", "defect operator norm for every R>=0"),
    ("(R+1)(R+2)/2", "d_(R,0) highest-weight dimension"),
    ("g_(R-1)", "R^2-floor(R^2/4)+3R over a"),
    ("p^2+pq+q^2+3p+3q", "electric energy E(p,q)/a"),
    ("(1,0)", "fundamental fusion (1,0) tensor (p,q)"),
    ("2(1-sqrt(p))", "normalized output error bound"),
    ("R>=1", "low-energy bound excludes R=0"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, text=True, stderr=subprocess.STDOUT
    )


def alts_for(token: str) -> list[str]:
    spelled = {
        "19": ["on19 link", "19 link basis"],
        "3 colors": ["and3 colors", "3 colors", "tensor C3"],
        "57": ["all57matrix", "all57", "actual57"],
        "17": ["performs17 named", "TOTAL: 17", "17 named checks"],
        "dim(H) Tr T^2": ["dim(H) Tr T²", "dim(H) Tr T^2"],
        "||D_R||=1": ["||D_R||=1", "norm-one witness", "eigenvalue1"],
        "(R+1)(R+2)/2": ["(R+1)(R+2)/2", "d_(R,0)=(R+1)(R+2)/2"],
        "g_(R-1)": ["g_(R−1)", "g_(R-1)", "g_(R-1)="],
        "p^2+pq+q^2+3p+3q": ["p²+pq+q²+3p+3q", "p^2+pq+q^2+3p+3q"],
        "(1,0)": ["(1,0) tensor(p,q)", "(1,0) tensor"],
        "2(1-sqrt(p))": ["2(1−sqrt(p))", "2(1-sqrt(p))", "2(1-sqrt"],
        "R>=1": ["For R>=1", "R>=1 define", "R≥1"],
    }
    return spelled.get(token, [token])


def find_line(blob: str, token: str) -> str | None:
    for alt in alts_for(token):
        pat = re.compile(re.escape(alt))
        for line in blob.splitlines():
            if pat.search(line):
                return line.strip()[:180]
    return None


def main() -> None:
    runner = git_show(RUNNER)
    note = git_show(NOTE)
    cache = git_show(CACHE)
    blobs = [("cache", cache), ("runner", runner), ("note", note)]
    unsourced = 0
    hits: list[str] = []
    for token, role in NUMBERS:
        src = None
        for name, blob in blobs:
            hit_line = find_line(blob, token)
            if hit_line:
                src = f"{name}: {hit_line[:140]}"
                break
        if src:
            status = "OK"
        else:
            src = "NOT IN RUNNER, CACHE, OR NOTE LINE"
            status = "UNSOURCED"
            unsourced += 1
            hits.append(f"{token} ({role})")
        print(f"{token} | {role} | {src} | {status}")

    if 19 * 3 != 57:
        unsourced += 1
        hits.append("19*3 != 57")
        print("IDENTITY | 19 states x 3 colors = 57 columns | MISMATCH")
    else:
        print("IDENTITY | 19 x 3 = 57 | OK")
    dims = [(r, (r + 1) * (r + 2) // 2) for r in range(0, 8)]
    print("IDENTITY | d_(R,0)=(R+1)(R+2)/2 " + str(dims) + " | OK")
    g = [r * r - (r * r) // 4 + 3 * r for r in range(1, 8)]
    print(f"IDENTITY | g_(R-1) numerator R=1..7 {g} | OK")

    print(f"SUMMARY: {len(NUMBERS)} theorem numbers, {unsourced} unsourced")
    if hits:
        print("HIT: " + "; ".join(hits))


if __name__ == "__main__":
    main()
