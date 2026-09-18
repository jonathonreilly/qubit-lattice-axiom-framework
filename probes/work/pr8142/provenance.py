#!/usr/bin/env python3
"""J:provenance:PR8142 — theorem numbers vs PR branch runner, cache, and note."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/physics-loop/admissibility-induced-law-block11-three-body-exceptional-locus-20260915"
RUNNER = "scripts/admissibility_rule_three_body_term_exceptional_locus_exact_classification_2026_09_15.py"
NOTE = "docs/ADMISSIBILITY_RULE_THREE_BODY_TERM_EXCEPTIONAL_LOCUS_EXACT_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-15.md"
CACHE = "logs/runner-cache/admissibility_rule_three_body_term_exceptional_locus_exact_classification_2026_09_15.txt"

NUMBERS = [
    ("16", "distinct third-difference numerators"),
    ("20", "executed checks"),
    ("11", "mutations"),
    ("216", "Z_3 triples on six-menu"),
    ("6^6", "argument tuples for numerators"),
    ("2160/2197", "block 08 third difference at (3,1,2)"),
    ("(3,1,2)", "declared triple off the locus"),
    ("(5,2,4)", "declared triple off the locus"),
    ("t^3-3t^2-6t-1", "cubic for t* on p=q"),
    ("(4,5)", "isolating interval of t*"),
    ("x^3-3x^2-15x-19", "cubic for rho on p=r"),
    ("(6,7)", "isolating interval of rho and sigma_2"),
    ("x^6-6x^5-3x^4+4x^3-3x^2-6x+31", "sextic for (sigma_1, sigma_2)"),
    ("(1,2)", "isolating interval of sigma_1"),
    ("8/85", "leading coefficient of psi"),
    ("356/255", "constant term of psi"),
    ("10^{-30}", "refined isolating width"),
    ("V_1", "p^3+q^3+4r^3"),
    ("V_5", "3r^2(p+q)"),
    ("8(t-1)^3", "E_1 factor on p=q"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, text=True, stderr=subprocess.STDOUT
    )


def alts_for(token: str) -> list[str]:
    spelled = {
        "16": ["16 distinct", "all 16", "the 16"],
        "20": ["20 checks", "TOTAL: PASS=20", "PASS=20 FAIL=0"],
        "11": ["11 mutations"],
        "216": ["216 triples", "over the 216"],
        "6^6": ["6^6", "over the 6^6"],
        "2160/2197": ["2160/2197"],
        "(3,1,2)": ["(3,1,2)", "(3, 1, 2)"],
        "(5,2,4)": ["(5,2,4)", "(5, 2, 4)"],
        "t^3-3t^2-6t-1": ["t^3 - 3t^2 - 6t - 1", "t^3-3t^2-6t-1", "t³ − 3t² − 6t − 1"],
        "(4,5)": ["in (4, 5)", "in (4,5)", "root in (4,5)"],
        "x^3-3x^2-15x-19": ["x^3 - 3x^2 - 15x - 19", "q^3-3q^2-15q-19", "q³ − 3q² − 15q − 19"],
        "(6,7)": ["in (6, 7)", "in (6,7)", "root lies in (6,7)"],
        "x^6-6x^5-3x^4+4x^3-3x^2-6x+31": [
            "x^6 - 6x^5 - 3x^4 + 4x^3 - 3x^2 - 6x + 31",
            "x⁶ − 6x⁵ − 3x⁴ + 4x³ − 3x² − 6x + 31",
        ],
        "(1,2)": ["in (1, 2)", "in (1,2)", "roots, in (1,2)"],
        "8/85": ["8/85"],
        "356/255": ["356/255"],
        "10^{-30}": ["10^{-30}", "10^-30", "width `10^{−30}`"],
        "V_1": ["V_1 = p³ + q³ + 4r³", "V_1 = p^3+q^3+4r^3", "five pattern values V_1"],
        "V_5": ["V_5 = 3r²(p + q)", "V_5 = 3r^2(p+q)", "V_1..V_5"],
        "8(t-1)^3": ["8(t − 1)³", "8(t-1)^3", "-8(t-1)^3"],
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

    def cubic_t(t: int) -> int:
        return t**3 - 3 * t**2 - 6 * t - 1

    def cubic_rho(x: int) -> int:
        return x**3 - 3 * x**2 - 15 * x - 19

    def sextic(x: int) -> int:
        return x**6 - 6 * x**5 - 3 * x**4 + 4 * x**3 - 3 * x**2 - 6 * x + 31

    if not (cubic_t(4) < 0 < cubic_t(5)):
        unsourced += 1
        hits.append("t* not isolated in (4,5)")
        print("IDENTITY | t*^3-3t*^2-6t*-1 sign change (4,5) | MISMATCH")
    else:
        print(f"IDENTITY | cubic_t(4)={cubic_t(4)} cubic_t(5)={cubic_t(5)} | OK")
    if not (cubic_rho(6) < 0 < cubic_rho(7)):
        unsourced += 1
        hits.append("rho not isolated in (6,7)")
        print("IDENTITY | rho cubic sign change (6,7) | MISMATCH")
    else:
        print(f"IDENTITY | cubic_rho(6)={cubic_rho(6)} cubic_rho(7)={cubic_rho(7)} | OK")
    if not (sextic(1) > 0 and sextic(2) < 0 and sextic(6) < 0 and sextic(7) > 0):
        unsourced += 1
        hits.append("sextic sign pattern not (1,2) and (6,7)")
        print("IDENTITY | sextic isolating signs | MISMATCH")
    else:
        print(
            f"IDENTITY | sextic(1)={sextic(1)} sextic(2)={sextic(2)} "
            f"sextic(6)={sextic(6)} sextic(7)={sextic(7)} | OK"
        )

    print(f"SUMMARY: {len(NUMBERS)} theorem numbers, {unsourced} unsourced")
    if hits:
        print("HIT: " + "; ".join(hits))


if __name__ == "__main__":
    main()
