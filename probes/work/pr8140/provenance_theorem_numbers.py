#!/usr/bin/env python3
"""J:provenance:PR8140 — theorem numbers vs runner-cache."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/physics-loop/clock-static-charge-20260915"
CACHES = [
    "logs/runner-cache/finite_clock_exact_coupled_electric_magnetic_defect_representation_2026_09_15.txt",
    "logs/runner-cache/finite_clock_ginibre_free_state_and_static_charge_bound_2026_09_15.txt",
    "logs/runner-cache/carrier_preserving_closed_integer_charge_gas_convexification_2026_09_15.txt",
]
NUMBERS = [
    ("17/24", "P_e and <a,Q^{-1}a>"),
    ("51/8", "phase exp[2 pi i 51/8]"),
    ("7/24", "||P_perp k||^2 = 9*(7/24)"),
]


def git_show(path: str) -> str:
    try:
        return subprocess.check_output(
            ["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, text=True, stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError:
        return ""


def find_line(blob: str, token: str) -> str | None:
    import re
    pat = re.compile(r"(?<![0-9])" + re.escape(token) + r"(?![0-9])")
    for line in blob.splitlines():
        if "sha256" in line.lower():
            continue
        if pat.search(line):
            return line.strip()
    return None


def main() -> None:
    blobs = [git_show(c) for c in CACHES]
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
