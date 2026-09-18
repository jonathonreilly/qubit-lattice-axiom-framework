#!/usr/bin/env python3
"""J:provenance:PR8032 — theorem numbers vs PR branch runners, caches, and note."""
from __future__ import annotations

import re
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/codex/finite-pw-energy-block42-20260907"
RUNNER = "scripts/gauge_wilson_finite_pw_charged_energy_controls_2026_09_07.py"
RUNNER_R1 = "scripts/gauge_wilson_finite_pw_actual_r1_charged_energy_check_2026_09_07.py"
NOTE = "docs/GAUGE_WILSON_FINITE_PW_STATIC_SOURCE_ENERGY_UPPER_BOUND_BOUNDED_THEOREM_NOTE_2026-09-07.md"
CACHE = "logs/runner-cache/gauge_wilson_finite_pw_charged_energy_controls_2026_09_07.txt"
CACHE_R1 = "logs/runner-cache/gauge_wilson_finite_pw_actual_r1_charged_energy_check_2026_09_07.txt"

NUMBERS = [
    ("4d/a", "full-unitary trial cost and kinetic identity (3)"),
    ("40", "geometry/shell/compression helper checks"),
    ("22", "R1 Haar-contraction charged-energy checks"),
    ("8v", "per-link kinetic budget E_e <= 8v"),
    ("32v", "four-link face budget E_face <= 32v"),
    ("8/3", "Casimir sum_A T_A^2 = (8/3)I"),
    ("e_R", "R^2-floor(R^2/4)+3R over a"),
    ("8d/3", "row-operator square of D_eA W"),
    ("4d", "at most 4d touching faces"),
    ("theta_0", "8avd/h_R"),
    ("1/100", "fixture t"),
    ("1/18", "B-J-A magnetic entry"),
    ("1/54", "B-J-C magnetic entry; 36/1944"),
    ("16", "electric energies 0,16,16 of the character basis"),
    ("4.01", "R1 trial excess strictly between 4 and 4.01"),
    ("1/50", "rational enclosure sqrt(theta)"),
    ("3/100", "rational enclosures of sqrt(E_path) and sqrt(E_face/e_R)"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, text=True, stderr=subprocess.STDOUT
    )


def alts_for(token: str) -> list[str]:
    spelled = {
        "4d/a": ["4d/a", "exact-four", "cost4d/a"],
        "40": ["performs40", "TOTAL: 40"],
        "22": ["computes22", "All22 checks", "TOTAL: 22"],
        "8v": ["<=8v", "E_e<=8v", "<=8v."],
        "32v": ["<=32v", "E_face<=32v"],
        "8/3": ["(8/3)I", "8/3", "(8d/3)"],
        "e_R": ["e_R=[R^2", "e_R=", "e_R=4"],
        "8d/3": ["(8d/3)I", "8d/3"],
        "4d": ["at most4d", "4d distinct"],
        "theta_0": ["theta_0=8avd/h_R", "theta_0<1"],
        "1/100": ["t=1/100"],
        "1/18": ["1/18", "[0,1/18,1/54]"],
        "1/54": ["1/54", "giving1/54"],
        "16": ["energies0,16,16", "0,16,16"],
        "4.01": ["between4 and4.01", "less than4.01"],
        "1/50": ["<=1/50", "1/50"],
        "3/100": ["<=3/100", "3/100"],
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
    blobs = [
        ("cache", git_show(CACHE)),
        ("cache_r1", git_show(CACHE_R1)),
        ("runner", git_show(RUNNER)),
        ("runner_r1", git_show(RUNNER_R1)),
        ("note", git_show(NOTE)),
    ]
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

    if Fraction(36, 1944) != Fraction(1, 54):
        unsourced += 1
        hits.append("36/1944 != 1/54")
        print("IDENTITY | 36/1944 = 1/54 | MISMATCH")
    else:
        print("IDENTITY | 36/1944 = 1/54 | OK")
    g1 = 1 * 1 - (1 * 1) // 4 + 3 * 1
    print(f"IDENTITY | e_R numerator at R=1 is {g1} (note uses e_R=4 at a=1) | " + ("OK" if g1 == 4 else "MISMATCH"))
    if g1 != 4:
        unsourced += 1
        hits.append("e_R(R=1)!=4")

    print(f"SUMMARY: {len(NUMBERS)} theorem numbers, {unsourced} unsourced")
    if hits:
        print("HIT: " + "; ".join(hits))


if __name__ == "__main__":
    main()
