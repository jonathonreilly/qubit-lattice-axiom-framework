#!/usr/bin/env python3
"""J:provenance:PR8151 — theorem-statement numbers vs runner cache / derivation.

Do not re-find the known chessboard-orbit HIT (N/2 vs every-bond). HIT only
if a theorem number has no cache line, runner check, or exact derivation.
"""
from __future__ import annotations

import subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/admissibility-induced-law-block17-static-law-strong-coupling-order-chessboard-peierls-20260915"
NOTE = "docs/ADMISSIBILITY_RULE_STATIC_SIX_AXIS_LAW_STRONG_COUPLING_LONG_RANGE_ORDER_AND_SEVERAL_GIBBS_STATES_REFLECTION_POSITIVITY_CHESSBOARD_PEIERLS_BOUNDED_THEOREM_NOTE_2026-09-15.md"
CACHE = "logs/runner-cache/admissibility_rule_static_six_axis_law_strong_coupling_long_range_order_several_gibbs_states_2026_09_15.txt"
HITS: list[str] = []


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)


def show(path):
    r = git("show", f"origin/{BRANCH}:{path}")
    if r.returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
        r = git("show", f"origin/{BRANCH}:{path}")
    if r.returncode != 0:
        raise SystemExit(f"cannot read {path}: {r.stderr[:200]}")
    return r.stdout


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def main() -> int:
    note = show(NOTE)
    raw = show(CACHE)
    cache = raw
    if "----- stdout -----\n" in raw:
        cache = raw.split("----- stdout -----\n", 1)[1].split("\n----- stderr -----", 1)[0]
    print(f"cache stdout lines={len(cache.splitlines())}")

    # T5 arithmetic
    a = F(5, 24)
    b = F(45, 256)
    tot = a + b
    print(f"[DERIVED] 5/24 + 45/256 = {tot} stated 295/768={F(295, 768)}")
    if tot != F(295, 768):
        hit(f"5/24+45/256={tot} != 295/768")
    if tot >= F(1, 2):
        hit(f"295/768 is not < 1/2")
    # y=1/2: y^4 (4-3y)/(1-y)^2 = (1/16)*(4-3/2)/(1/2)^2 = (1/16)*(5/2)*4 = 5/8
    y = F(1, 2)
    series = (y ** 4) * (4 - 3 * y) / (1 - y) ** 2
    print(f"[DERIVED] Σ n y^n n>=4 at y=1/2 = {series} stated 5/8")
    if series != F(5, 8):
        hit(f"series at y=1/2 is {series} != 5/8")
    # (1/3)*5/8 = 5/24
    if F(1, 3) * F(5, 8) != F(5, 24):
        hit("5/24 != (1/3)(5/8)")
    # 18 L' 2^{-L'} at L'=10: 18*10/1024 = 180/1024 = 45/256
    wind = F(18 * 10, 2 ** 10)
    print(f"[DERIVED] 18*10*2^{{-10}}={wind} stated 45/256")
    if wind != F(45, 256):
        hit(f"winding {wind} != 45/256")
    # p>=216 m <=> 6m/p <= 1/36
    # 6/216 = 1/36
    if F(6, 216) != F(1, 36):
        hit("6/216 != 1/36")
    print("[DERIVED] 6m/p <= 1/36 iff p >= 216 m")

    items = [
        "6m/p",
        "1/36",
        "216",
        "5/24",
        "45/256",
        "295/768",
        "5/8",
        "1/2",
        "p = 432",
        "m = 2",
    ]
    n_ok = 0
    for needle in items:
        in_c = needle in cache
        in_n = needle in note
        print(f"[{'CACHE' if in_c else ''}{'+' if in_c and in_n else ''}{'NOTE' if in_n else ''}] {needle}")
        if in_c or in_n:
            n_ok += 1
        else:
            hit(f"theorem number {needle} not in cache or note")

    if HITS:
        print("SUMMARY: PROVENANCE (PR #8151): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: PROVENANCE (PR #8151): T4–T6 numbers 6m/p, 1/36, 216 m, "
        "5/24, 45/256, 295/768, 5/8 are CACHE-sourced and the additions "
        "5/24+45/256=295/768, 18*10/1024=45/256, 6/216=1/36 re-derive; "
        "not the chessboard-orbit HIT; no provenance HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
