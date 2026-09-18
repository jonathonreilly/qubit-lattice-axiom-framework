#!/usr/bin/env python3
"""J:provenance:PR8174 — theorem/result-up-front numbers vs PR #8174 runner-cache."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = (
    "origin/physics-loop/admissibility-induced-law-block30-six-axis-threshold-"
    "two-level-domination-amplified-nodes-20260916"
)
CACHE = (
    "logs/runner-cache/admissibility_rule_six_axis_formation_threshold_"
    "two_level_domination_seeds_and_amplified_nodes_2026_09_16.txt"
)

NUMBERS = [
    ("285718", "block 25 region restated"),
    ("10.5", "block 28 located strength lo"),
    ("11", "block 28 located strength hi"),
    ("4165", "T4 region (p,1,2)"),
    ("2085", "T4 region (p,1,1)"),
    ("8330", "T4 region (p,2,4)"),
    ("6247", "T4 region (p,1,3)"),
    ("4150", "T5 ceiling below"),
    ("4/27", "domain edge"),
    ("256/531441", "T5 ε2 ceiling"),
    ("8/81", "argmax t of t^2(4/27-t)"),
    ("3/2", "argmax v of (v-1)/v^3"),
    ("99/1000", "t at (4165,1,2)"),
    ("49/500", "t at (2085,1,1)"),
    ("10^{-7}", "ε1 R-bar bound"),
    ("4290", "construction configs"),
    ("932", "depth-2 cones"),
    ("2321", "depth-3 <=4 noise"),
    ("2/3", "max executed (E-3(|S|-1))/|A|"),
    ("20", "checks"),
    ("11", "mutations / located strength"),
    ("69", "factor below block 25"),
    ("380", "remaining factor to p≈11"),
    ("8311/17230811", "d3(4150,1,2)"),
    ("8341/17355566", "d3(4165,1,2)"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, text=True, stderr=subprocess.STDOUT
    )


def alts_for(token: str) -> list[str]:
    out = [token, token.replace("^{", "^").replace("}", "")]
    if token == "10^{-7}":
        out += ["10^-7", "10^{-7}"]
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
