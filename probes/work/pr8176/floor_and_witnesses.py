#!/usr/bin/env python3
"""J:attack:PR8176 — pattern (c) EXECUTED NUMBERS: 4/729 floor and W1–W3 ratios.

T4: max_t t(4/27-t)=4/729. T3: W1 c*=3/4, W2 4/11, W3 E-3(|S|-1)=-12.
HIT if the max identity fails or cache values disagree.
"""
from fractions import Fraction
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = (
    "origin/physics-loop/admissibility-induced-law-block32-minimal-marked-tree-"
    "family-constant-at-least-one-tree-route-floor-20260917"
)
CACHE = (
    "logs/runner-cache/admissibility_rule_six_axis_formation_threshold_minimal_marked_tree_"
    "family_constant_at_least_one_exact_certificates_and_the_tree_route_floor_2026_09_17.txt"
)


def git_show(path: str) -> str:
    r = subprocess.run(["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr.strip()[:400])
    return r.stdout


def main() -> None:
    hits = []
    t = Fraction(2, 27)
    mx = t * (Fraction(4, 27) - t)
    print(f"max t(4/27-t) at t=2/27 is {mx} stated 4/729 {mx==Fraction(4,729)}")
    if mx != Fraction(4, 729):
        hits.append(f"max={mx} != 4/729")
    a = Fraction(745, 135434)
    b = Fraction(747, 136171)
    c = Fraction(4, 729)
    print(f"p=367 d3={a} > 4/729 {a>c}; p=368 d3={b} < 4/729 {b<c}")
    if not (a > c > b):
        hits.append("367/368 do not straddle 4/729 as 367>floor>368")
    cache = git_show(CACHE)
    for needle in ["exactly 3/4", "ratio 4/11", "E - 3(|S|-1) = -12"]:
        ok = needle in cache or needle.replace("(", "\\(") in cache
        print(f"cache has {needle!r}: {needle in cache}")
        if needle not in cache:
            hits.append(f"missing {needle}")
    if hits:
        print("HIT: " + "; ".join(hits))
        print("SUMMARY: attack pattern (c) EXECUTED NUMBERS - " + "; ".join(hits))
    else:
        print(
            "SUMMARY: attack pattern (c) EXECUTED NUMBERS - 4/729 identity, 367/368 "
            "straddle, W1 3/4 W2 4/11 W3 -12 in cache; does not fire"
        )


if __name__ == "__main__":
    main()
