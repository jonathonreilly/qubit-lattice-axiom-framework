#!/usr/bin/env python3
"""J:provenance:PR8026 — theorem numbers vs runner-cache."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/codex/spatial-area-block36-20260907"
CACHES = [
    "logs/runner-cache/gauge_wilson_spatial_loop_area_chain_check_2026_09_07.txt",
    "logs/runner-cache/gauge_wilson_spatial_loop_area_coefficients_check_2026_09_07.txt",
]
NUMBERS = [
    ("1/144", "omega_u(W_square) leading"),
    ("7/124416", "two-adjacent-faces u^2"),
    ("19", "chain helper checks"),
    ("33", "coefficient helper checks"),
    ("4/a", "first positive electric energy"),
    ("2ce", "Part I C_0 reserve"),
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
    blobs = []
    for c in CACHES:
        try:
            blobs.append(git_show(c))
        except subprocess.CalledProcessError:
            blobs.append("")
    unsourced = 0
    for token, role in NUMBERS:
        hit_line = None
        for blob in blobs:
            hit_line = find_line(blob, token)
            if hit_line:
                break
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
