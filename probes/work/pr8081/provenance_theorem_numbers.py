#!/usr/bin/env python3
"""J:provenance:PR8081 — theorem-statement numbers of the correlated Ward note.

Source each number in claim_scope + the T/L(E,F) theorem block to the runner
cache, runner source, or an exact derivation here. HIT if unsourced.
"""
from __future__ import annotations

import subprocess
from fractions import Fraction as F
from itertools import combinations

import sympy as sp

ROOT_CWD = None
HEAD = "ac5e0c248f9af28f86ee148e95c148a74e260524"
BRANCH = "codex/native-correlated-ward-20260910"
NOTE = "docs/NATIVE_CORRELATED_WARD_CERTIFICATES_NOTE_2026-09-10.md"
RUNNER = "scripts/native_correlated_ward_certificates_2026_09_10.py"
CACHE = "logs/runner-cache/native_correlated_ward_certificates_2026_09_10.txt"

HITS: list[str] = []


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True)


def show(path):
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        r = git("show", f"origin/{BRANCH}:{path}")
    return r.stdout if r.returncode == 0 else ""


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def k6_spectrum():
    verts = range(6)
    edges = list(combinations(verts, 2))
    N = sp.zeros(6, 15)
    for j, e in enumerate(edges):
        N[e[0], j] = 1
        N[e[1], j] = 1
    I6, J6 = sp.eye(6), sp.ones(6)
    nn = N * N.T
    ok_nn = nn == 4 * I6 + J6
    T = sp.ones(15) + sp.eye(15) - N.T * N
    ev = sorted(sp.Matrix(T).eigenvals().items(), key=lambda kv: -kv[0])
    # eigenvals dict value is multiplicity
    return ok_nn, ev, T


def main() -> int:
    note = show(NOTE)
    runner = show(RUNNER)
    cache = show(CACHE)
    print(f"note {len(note)} chars; runner {len(runner)} chars; cache {len(cache)} chars")
    ok_nn, ev, T = k6_spectrum()
    print(f"[DERIVED] NN*=4I+J6: {ok_nn}; T eigenvalues {ev}")
    if not ok_nn:
        hit("NN* != 4I+J6")
    want = {sp.Integer(6): 1, sp.Integer(-3): 5, sp.Integer(1): 9}
    got = {k: int(v) for k, v in ev}
    if got != {6: 1, -3: 5, 1: 9} and got != want:
        # sympy Integer keys
        got_i = {int(k): int(v) for k, v in ev}
        print(f"got {got_i}")
        if got_i != {6: 1, -3: 5, 1: 9}:
            hit(f"T spectrum {got_i} != 6,-3,1 with 1,5,9")
        else:
            print("[DERIVED] T spectrum 6,-3,1 multiplicities 1,5,9")
    else:
        print("[DERIVED] T spectrum 6,-3,1 multiplicities 1,5,9")

    blob = note + "\n" + runner + "\n" + cache
    items = [
        ("15 channels", "15 two-neighbor", blob),
        ("six labels", "six labels", blob),
        ("delta=1/4", "1/4", blob),
        ("W=8 alpha", "8alpha", blob.replace(" ", "")),
        ("2E boundary", "2E", blob.replace(" ", "")),
        ("4E boundary", "4E", blob.replace(" ", "")),
    ]
    sourced = 0
    for name, needle, blob in items:
        ok = needle in blob.replace(" ", "") or needle in blob
        print(f"[{'CACHE/RUNNER/NOTE' if ok else 'UNSOURCED'}] {name}")
        if ok:
            sourced += 1
        else:
            hit(f"unsourced {name}")

    # L branches derived
    E, Fv = sp.symbols("E F", positive=True)
    L1 = -3 * E**2 - 3 * E * Fv
    L2 = -6 * E**2 - 3 * Fv**2 / 4
    L3 = 6 * E**2 - 6 * E * Fv
    b12 = sp.simplify(L1.subs(Fv, 2 * E) - L2.subs(Fv, 2 * E))
    b23 = sp.simplify(L2.subs(Fv, 4 * E) - L3.subs(Fv, 4 * E))
    print(f"[DERIVED] L branches agree at F=2E: {b12==0}; F=4E: {b23==0}")
    if b12 != 0 or b23 != 0:
        hit("L branch mismatch at 2E or 4E")

    # delta=1/4 is a definition of the common gap
    print("[DEFINITION] delta=1/4 common channel gap")
    print("[DEFINITION] 15=C(6,2) two-neighbor channels")

    n_items = sourced + 3  # spectrum, NN*, L
    print(
        f"SUMMARY: {len(items)+3} theorem numbers: derived K6 NN*/spectrum/L-join; "
        f"sourced {sourced}/{len(items)} needles in runner/cache/note; "
        f"unsourced {len(HITS)}"
    )
    for h in HITS:
        print(h)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
