#!/usr/bin/env python3
"""J:provenance:PR8149 — theorem numbers vs runner-cache.

Not the known 216-env U2/U4 HIT.
"""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = (
    "origin/physics-loop/admissibility-induced-law-block15-formation-unit-"
    "clause-witness-20260915"
)
CACHE = (
    "logs/runner-cache/"
    "admissibility_rule_formation_unit_clause_witness_sequential_equals_"
    "joint_iff_criterion_2026_09_15.txt"
)
NUMBERS = [
    ("1/72", "star TV k=2"),
    ("5/144", "star TV k=3"),
    ("505/10368", "star TV k=4"),
    ("575/10368", "star TV k=5"),
    ("103375/1492992", "star TV k=6"),
    ("455/31176", "plaquette path-order TV"),
    ("37/1299", "plaquette diagonal-first TV"),
    ("18", "checks"),
    ("12", "mutations"),
    ("(3, 1, 2)", "executed triple"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, text=True, stderr=subprocess.STDOUT
    )


def find_line(blob: str, token: str) -> str | None:
    for line in blob.splitlines():
        if "sha256" in line.lower():
            continue
        if token in line:
            return line.strip()
    return None


def main() -> None:
    cache = git_show(CACHE)
    unsourced = 0
    for token, role in NUMBERS:
        hit_line = find_line(cache, token)
        if hit_line:
            src = f"cache: {hit_line[:120]}"
            status = "OK"
        else:
            # ASCII/unicode fraction variants
            alt = token.replace(" ", "")
            hit_line = find_line(cache, alt)
            if hit_line:
                src = f"cache: {hit_line[:120]}"
                status = "OK"
            else:
                src = "NOT IN CACHE"
                status = "UNSOURCED"
                unsourced += 1
        print(f"{token} | {role} | {src} | {status}")
    n = len(NUMBERS)
    print(f"SUMMARY: {n} numbers, {unsourced} unsourced")
    if unsourced:
        print("HIT: unsourced numbers")


if __name__ == "__main__":
    main()
