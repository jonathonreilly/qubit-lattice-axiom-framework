#!/usr/bin/env python3
"""J:provenance:PR8079 — theorem numbers vs PR branch runner (no runner-cache on the branch)."""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/codex/native-finite-moment-ward-20260910"
RUNNER = "scripts/native_finite_moment_ward_2026_09_10.py"
NOTE = "docs/NATIVE_FINITE_MOMENT_WARD_NOTE_2026-09-10.md"
NUMBERS = [
    ("15", "two-link defects"),
    ("90", "ordered disjoint pairs"),
    ("6", "||T|| / adjacency degree"),
    ("8", "8α / J*J=8h^2"),
    ("h/4", "δ"),
    ("2√2", "j"),
    ("31/128", "ellipse positivity"),
    ("1742", "Gauss nodes"),
    ("3484", "endpoint oracles"),
    ("67", "panels"),
    ("2^{-64}", "ε"),
    ("1904", "conservative radius prefactor"),
    ("4^{-52}", "radius power"),
    ("10^{-24}", "width target"),
    ("205", "saved events"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, text=True, stderr=subprocess.STDOUT
    )


def find_line(blob: str, token: str) -> str | None:
    alts = [token, token.replace("^{-", "^-").replace("}", ""), token.replace("√", "sqrt")]
    if token == "2√2":
        alts += ["2√2", "2*sqrt(2)", "2√2h", "2*√2"]
    if token == "2^{-64}":
        alts += ["2^{-64}", "2^-64", "ε=2^{-64}"]
    if token == "4^{-52}":
        alts += ["4^{-52}", "4^-52"]
    if token == "10^{-24}":
        alts += ["10^{-24}", "10^-24", "1/1000000000000000000000000"]
    for alt in alts:
        pat = re.compile(re.escape(alt))
        for line in blob.splitlines():
            if "sha256" in line.lower():
                continue
            if pat.search(line):
                return line.strip()
    return None


def main() -> None:
    runner = git_show(RUNNER)
    note = git_show(NOTE)
    unsourced = 0
    for token, role in NUMBERS:
        rl = find_line(runner, token)
        nl = find_line(note, token)
        if rl:
            src = f"runner: {rl[:120]}"
            status = "OK"
        elif nl:
            src = f"note: {nl[:120]}"
            status = "OK"
        else:
            src = "NOT IN RUNNER OR NOTE LINE"
            status = "UNSOURCED"
            unsourced += 1
        print(f"{token} | {role} | {src} | {status}")
    n = len(NUMBERS)
    print(f"SUMMARY: {n} numbers, {unsourced} unsourced; no logs/runner-cache on PR branch")
    if unsourced:
        print("HIT: unsourced numbers")


if __name__ == "__main__":
    main()
