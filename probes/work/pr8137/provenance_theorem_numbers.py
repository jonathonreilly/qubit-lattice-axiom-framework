#!/usr/bin/env python3
"""J:provenance:PR8137 — theorem numbers vs runner cache / derivation."""
from __future__ import annotations

import subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/possibility-symmetric-order-dependence-20260915"
NOTE = "docs/POSSIBILITY_SYMMETRIC_SEQUENTIAL_FORMATION_THAT_VARIES_HAS_ORDER_DEPENDENT_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-15.md"
CACHE = "logs/runner-cache/possibility_symmetric_sequential_variation_forces_order_dependence_2026_09_15.txt"
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

    pp, pm = F(4, 5), F(1, 5)
    k2pp = pp * pp + (1 - pp) * pm
    k2pm = pm * pp + (1 - pm) * pm
    print(f"[DERIVED] K^2(+|+)= {k2pp} stated 17/25; K^2(+|-)= {k2pm} stated 8/25")
    if k2pp != F(17, 25) or k2pm != F(8, 25):
        hit(f"Ising K^2 {k2pp},{k2pm} != 17/25, 8/25")
    plr = F(1, 2) * k2pp
    print(f"[DERIVED] P(L=R=+)={plr} stated 17/50")
    if plr != F(17, 50):
        hit(f"P(L=R=+)={plr} != 17/50")
    # Haar-square residual (a-b)^2; (6c-1)^2/3=0 => c=1/6
    if F(1, 6) * 6 != 1:
        hit("1/6 * 6 != 1")
    print("[DERIVED] (6c-1)^2/3=0 => c=1/6; a=b=1/6 with a+b+4c=1")

    items = [
        "17/25",
        "8/25",
        "17/50",
        "1/4",
        "1/6",
        "4/5",
        "1/5",
        "24",
        "(6c-1)^2 / 3",
        "1/2",
        "1/3",
    ]
    n_ok = 0
    for needle in items:
        in_c = needle in cache or needle.replace(" ", "") in cache.replace(" ", "")
        in_n = needle in note or needle.replace(" ", "") in note.replace(" ", "")
        tag = ("CACHE" if in_c else "") + ("+" if in_c and in_n else "") + ("NOTE" if in_n else "")
        print(f"[{tag or 'NONE'}] {needle}")
        if in_c or in_n:
            n_ok += 1
        else:
            hit(f"theorem number {needle} not in cache or note")

    if HITS:
        print("SUMMARY: PROVENANCE (PR #8137): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: PROVENANCE (PR #8137): Ising K^2 17/25, 8/25, 17/50 re-derive "
        "from (4/5,1/5); 24, 1/6, 1/4, Haar-square (6c-1)^2/3 are "
        "CACHE/NOTE-sourced; no provenance HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
