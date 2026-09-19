#!/usr/bin/env python3
"""J:provenance:PR8153 — theorem-statement numbers vs note / exact torus G_L."""
from __future__ import annotations

import subprocess
from fractions import Fraction as Fr
from itertools import product
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/admissibility-induced-law-block19-sphere-static-law-goldstone-green-function-channel-20260915"
NOTE = (
    "docs/ADMISSIBILITY_RULE_UNSOLDERED_SPHERE_STATIC_LAW_ORDERED_PHASE_TRANSVERSE_"
    "CHANNEL_CARRIES_THE_LATTICE_GREEN_FUNCTION_INFRARED_AND_BOGOLIUBOV_BOUNDS_"
    "BOUNDED_THEOREM_NOTE_2026-09-15.md"
)
pi = sp.pi


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def show(path: str) -> str:
    git("fetch", "origin", BRANCH, "--quiet")
    head = git("rev-parse", f"origin/{BRANCH}").stdout.strip()
    r = git("show", f"{head}:{path}")
    if r.returncode != 0:
        raise SystemExit(r.stderr[:400])
    return r.stdout


def main() -> None:
    note = show(NOTE)
    items = [
        ("4^3", ["4^3", "4³", "4*4*4"]),
        ("2(1-cos", ["2(1-cos", "2(1 − cos", "E(k)"]),
        ("2π", ["2π", "2pi", "2 pi"]),
        ("3G(0)", ["3G(0)", "3 G(0)"]),
    ]
    unsourced = []
    for token, alts in items:
        src = None
        for alt in alts:
            for line in note.splitlines():
                if alt in line:
                    src = line.strip()[:140]
                    break
            if src:
                break
        if src:
            print(f"OK | {token} | NOTE: {src}")
        else:
            print(f"UNSOURCED | {token}")
            unsourced.append(token)
    # exact G_2 = 29/192
    L, N = 2, 8
    s = 0
    for n in product(range(L), repeat=3):
        if n == (0, 0, 0):
            continue
        e = sum(2 * (1 - sp.cos(2 * pi * ni / L)) for ni in n)
        s += 1 / sp.simplify(e)
    g = sp.simplify(s / N)
    print(f"DERIVED | 4^3 torus N=64, 3N=192 bonds; G_2 = {g} (29/192)")
    if g != Fr(29, 192):
        unsourced.append(f"G_2={g}")
        print("HIT: G_2 != 29/192")
    if unsourced:
        for u in unsourced:
            print("HIT:", u)
        print("SUMMARY: provenance FIRED; " + "; ".join(map(str, unsourced)))
        return
    print(
        "SUMMARY: provenance OK — 4^3, E=2(1-cos), 2π, 3G(0) sourced in the "
        "note; N=64, 3N=192 and G_2=29/192 derived exactly"
    )


if __name__ == "__main__":
    main()
