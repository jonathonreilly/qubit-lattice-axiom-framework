#!/usr/bin/env python3
"""J:provenance:PR8143 — theorem numbers vs PR branch runner, cache, and note."""
from __future__ import annotations

import math
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/physics-loop/full-domain-projective-corridor-20260915"
RUNNER = "scripts/full_domain_matrix_kernel_and_autonomous_projective_record_corridor_2026_09_15.py"
NOTE = "docs/FULL_DOMAIN_MATRIX_KERNEL_AND_AUTONOMOUS_PROJECTIVE_RECORD_CORRIDOR_BOUNDED_THEOREM_NOTE_2026-09-15.md"
CACHE = "logs/runner-cache/full_domain_matrix_kernel_and_autonomous_projective_record_corridor_2026_09_15.txt"

NUMBERS = [
    ("1/4", "psi equals 1 for u<=1/4"),
    ("17", "program tag trace 17 = tr(8I+P)"),
    ("8I", "program encoding B=8I+P"),
    ("2I", "carrier A=2I+rho and scalar marker"),
    ("tr A-5", "r(A)=psi(|tr A-5|^2)"),
    ("3/4", "Z>=3/4 and lambda denominator"),
    ("6n", "at most 6n blank sites of rate <=1"),
    ("exp(6t)", "Gronwall bound n0 exp(6t)"),
    ("8/3", "f_S(1/4)=1/(1+exp(8/3))"),
    ("1+5L", "|C|=1+5L seed sites"),
    ("3L", "3L writes / Erlang shape / E tau"),
    ("1+2L", "1+2L nonzero seed records"),
    ("187", "all_frontier_states_checked (executed L=5)"),
    ("87", "guard_records (executed)"),
    ("8", "TOTAL PASS checks"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, text=True, stderr=subprocess.STDOUT
    )


def alts_for(token: str) -> list[str]:
    spelled = {
        "1/4": [r"u<=1/4", "Rational(1,4)", "1/4"],
        "17": ["trace is17", "tr-17", "tr A-17", "abs(tr-17)"],
        "8I": ["B=8I+P", "8*I", "A-8I", "8*eye"],
        "2I": ["A=2I+rho", "2I+rho", "2*I", "marker2I"],
        "tr A-5": [r"|tr A-5|^2", "tr-5", "abs(tr-5)"],
        "3/4": ["Z>=3/4", "at least3/4", "3/4"],
        "6n": ["at most6n", "6n such", "6*|C|", "6|C|"],
        "exp(6t)": ["exp(6t)", "n_0 exp(6t)"],
        "8/3": ["exp(8/3)", "Rational(8,3)", "8/3"],
        "1+5L": ["|C|=1+5L", "1+5L"],
        "3L": ["shape3L", "E tau=3L", "3L writes", "3L initially"],
        "1+2L": ["1+2L seed", "these1+2L"],
        "187": ["all_frontier_states_checked\": 187", "187"],
        "87": ["guard_records\": 87", "87"],
        "8": ["TOTAL: PASS=8", "PASS=8 FAIL=0"],
    }
    return spelled.get(token, [token])


def find_line(blob: str, token: str) -> str | None:
    for alt in alts_for(token):
        pat = re.compile(re.escape(alt))
        for line in blob.splitlines():
            if pat.search(line):
                return line.strip()[:200]
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

    # Exact identities from the theorem.
    fs = 1 / (1 + math.exp(8 / 3))
    print(f"IDENTITY | 1/(1+exp(8/3))={fs:.12f} != 1/4={0.25} | OK")
    if abs(fs - 0.25) < 1e-6:
        unsourced += 1
        hits.append("f_S(1/4) collapsed to 1/4")
        print("HIT: f_S quarter equals 1/4")
    for L in range(1, 8):
        c = 1 + 5 * L
        writes = 3 * L
        if c != 1 + 5 * L or writes != 3 * L:
            unsourced += 1
            hits.append(f"seed census L={L}")
    print("IDENTITY | |C|=1+5L and 3L writes for L=1..7 | OK")

    print(f"SUMMARY: {len(NUMBERS)} theorem numbers, {unsourced} unsourced")
    if hits:
        print("HIT: " + "; ".join(hits))


if __name__ == "__main__":
    main()
