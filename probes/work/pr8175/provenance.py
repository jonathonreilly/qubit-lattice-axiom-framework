#!/usr/bin/env python3
"""J:provenance:PR8175 — theorem numbers vs PR #8175 runner-cache."""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = (
    "origin/physics-loop/admissibility-induced-law-block31-sharper-bad-pair-budget-"
    "false-witnesses-two-level-period-20260916"
)
CACHE = (
    "logs/runner-cache/admissibility_rule_six_axis_formation_threshold_"
    "the_sharper_bad_pair_budget_is_false_for_the_extended_explanation_tree_"
    "explicit_witnesses_and_the_two_level_period_2026_09_16.txt"
)
NUMBERS = [
    ("4165", "block 30 region restated"),
    ("8/5", "W1 ratio"),
    ("5/3", "W2/W3 ratio"),
    ("16", "W1 E"),
    ("10", "W1 |A|"),
    ("20", "W2 E / checks"),
    ("12", "W2 |A|"),
    ("23", "W3 E"),
    ("2", "period ratio / |S| W3"),
    ("453", "stake (p,1,2)"),
    ("232", "stake (p,1,1)"),
    ("905", "stake (p,2,4)"),
    ("677", "stake (p,1,3)"),
    ("4/729", "false-budget ceiling"),
    ("367", "crossing lo"),
    ("368", "crossing hi"),
    ("256/531441", "block 30 ceiling restated"),
    ("300", "random cones in runner"),
    ("40000", "control cones"),
    ("9", "mutations"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, text=True, stderr=subprocess.STDOUT
    )


def find_line(blob: str, token: str) -> str | None:
    pat = re.compile(r"(?<![0-9A-Fa-f])" + re.escape(token) + r"(?![0-9A-Fa-f])")
    for line in blob.splitlines():
        if "sha256" in line.lower():
            continue
        if pat.search(line):
            return line.strip()
    return None


def main() -> None:
    try:
        cache = git_show(CACHE)
    except subprocess.CalledProcessError:
        # cache basename may differ; find it
        listing = subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", BRANCH], cwd=ROOT, text=True
        )
        cands = [l for l in listing.splitlines() if l.startswith("logs/runner-cache/") and "sharper" in l]
        if not cands:
            print("SUMMARY: 0 numbers, 1 unsourced")
            print("HIT: unsourced numbers")
            print("HIT: runner-cache path not found on PR branch")
            return
        cache = git_show(cands[0])
        print(f"cache path used: {cands[0]}")
    unsourced = 0
    for token, role in NUMBERS:
        hit_line = find_line(cache, token)
        if hit_line:
            src = f"cache: {hit_line[:140]}"
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
