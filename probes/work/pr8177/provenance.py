#!/usr/bin/env python3
"""J:provenance:PR8177 — theorem/result-up-front numbers vs PR #8177 runner-cache."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = (
    "origin/physics-loop/admissibility-induced-law-block33-rooted-inequality-"
    "tight-sibling-lemma-one-processed-child-count-20260917"
)
CACHE = (
    "logs/runner-cache/admissibility_rule_six_axis_formation_threshold_"
    "rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_lemma_"
    "and_the_one_processed_child_count_2026_09_17.txt"
)

NUMBERS = [
    ("4165", "block 30 region restated"),
    ("453", "unit-budget region restated"),
    ("140", "tiny realizations"),
    ("357", "extension pairs"),
    ("121", "amplified sites"),
    ("15", "single-seed lemma cases"),
    ("78", "double-seed lemma cases"),
    ("788", "sites with (H)"),
    ("2921", "restricted c=2 (p,1,2)"),
    ("1464", "restricted c=2 (p,1,1)"),
    ("5841", "restricted c=2 (p,2,4)"),
    ("4380", "restricted c=2 (p,1,3)"),
    ("405", "restricted c=1 (p,1,2)"),
    ("208", "restricted c=1 (p,1,1)"),
    ("810", "restricted c=1 (p,2,4)"),
    ("605", "restricted c=1 (p,1,3)"),
    ("60", "tiny restriction cases / 2"),
    ("120", "tiny restriction cases"),
    ("125", "shape-survey realizations"),
    ("-61", "W3 restricted min c=2"),
    ("-62", "W3 unrestricted min c=2"),
    ("2887", "at-most-two-children count"),
    ("18", "checks"),
    ("7", "mutations"),
    ("10^4", "climb realizations"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, text=True, stderr=subprocess.STDOUT
    )


def alts_for(token: str) -> list[str]:
    out = [token]
    if token == "10^4":
        out += ["10^4", "10⁴", "about 10^4"]
    return list(dict.fromkeys(out))


def find_line(blob: str, token: str) -> str | None:
    import re
    for alt in alts_for(token):
        pat = re.compile(r"(?<![0-9A-Fa-f])" + re.escape(alt) + r"(?![0-9A-Fa-f])")
        for line in blob.splitlines():
            if "sha256" in line.lower():
                continue
            if pat.search(line):
                return line.strip()
    return None


def main() -> None:
    cache = git_show(CACHE)
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
