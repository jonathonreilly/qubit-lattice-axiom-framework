#!/usr/bin/env python3
"""Referee of J:derive:chessboard-repair:a3 (author w-macbookpro90c72-j6ef3, grok-4.6); referee w-jonathonsmac4f50-j8343
(claude-opus-5). Independent machinery (sympy; orbit closures by my own code). Disclosure: this referee's model family wrote
attempt a1 of the same problem (bond-plane RP plus a mixed chessboard); a3 is independent of it.

C1  step 1: the 6x6 bond weight W (p same, q antipodal, r orthogonal) has eigenvalues p + q + 4r (once), p - q (three times),
    p + q - 2r (twice); PSD iff p >= q and p + q >= 2r (sympy); the witnesses (3,1,2), (5,2,4), (1,3,2), (4,1,2)
C2  steps 2-3: orbit of the direction-0 bond {0, e_0} on (Z/S)^d, (d, S) in {(2,4), (2,6), (3,4), (3,6)}, under (a) all bond-plane
    reflections x_i -> 2k + 1 - x_i: N/2 bonds, exactly the direction-0 bonds with even longitudinal start; (b) all site-plane
    reflections x_i -> 2k - x_i: N/2^(d-1); (c) site-plane reflections in direction 0 with bond-plane reflections in the others: N
C3  step 4 / section (4): the missing ingredient the attempt names, site-plane RP, is block 17's T2 ('reflection positivity through
    site planes, any weights', PR #8151); with it the mixed group of C2(c) disseminates to all N direction-i bonds (as attempt a1
    of this problem uses); this check reads the statement from the note on its branch
"""
from __future__ import annotations

import itertools
import subprocess
import sys

import sympy as sp


def orbit(S, d, moves):
    start = ((0,) * d, 0)            # bond {x, x + e_0} identified by its start x and direction 0
    seen = {start}
    stack = [start]
    while stack:
        (x, i) = stack.pop()
        for (j, kind) in moves:
            for k in range(S):
                y = list(x)
                if kind == "site":
                    if j == i:
                        y[j] = (2 * k - x[j] - 1) % S
                    else:
                        y[j] = (2 * k - x[j]) % S
                else:                        # bond plane between k and k + 1
                    if j == i:
                        y[j] = (2 * k + 1 - x[j] - 1) % S
                    else:
                        y[j] = (2 * k + 1 - x[j]) % S
                b = (tuple(y), i)
                if b not in seen:
                    seen.add(b)
                    stack.append(b)
    return seen


def main():
    fails = 0

    def check(tag, ok, msg):
        nonlocal fails
        fails += (not ok)
        print(("PASS: " if ok else "FAIL: ") + tag + " " + msg)

    p, q, r = sp.symbols("p q r", positive=True)
    W = sp.Matrix(6, 6, lambda a, b: p if a == b else (q if b == (a ^ 1) else r))
    ev = W.eigenvals()
    want = {sp.expand(p + q + 4 * r): 1, sp.expand(p - q): 3, sp.expand(p + q - 2 * r): 2}
    got = {sp.expand(k): v for k, v in ev.items()}
    ok = got == want
    wit = {(3, 1, 2): 0, (5, 2, 4): -1, (1, 3, 2): None, (4, 1, 2): 1}
    rows = []
    for (a, b, c), _ in wit.items():
        evs = sorted(sp.Matrix(6, 6, lambda i, j: a if i == j else (b if j == (i ^ 1) else c)).eigenvals().keys())
        psd = all(e >= 0 for e in evs)
        ok = ok and psd == (a >= b and a + b >= 2 * c)
        rows.append(f"({a},{b},{c}): eigenvalues {evs}, PSD {psd}")
    check("C1", ok, "W has eigenvalues p + q + 4r (1), p - q (3), p + q - 2r (2); PSD exactly when p >= q and p + q >= 2r: " + "; ".join(rows))

    ok = True
    rows = []
    for d, S in ((2, 4), (2, 6), (3, 4), (3, 6)):
        N = S ** d
        bond_all = orbit(S, d, [(j, "bond") for j in range(d)])
        site_all = orbit(S, d, [(j, "site") for j in range(d)])
        mixed = orbit(S, d, [(0, "site")] + [(j, "bond") for j in range(1, d)])
        even = {(x, 0) for x in itertools.product(range(S), repeat=d) if x[0] % 2 == 0}
        ok = ok and bond_all == even and len(bond_all) == N // 2 and len(site_all) == N // 2 ** (d - 1) and len(mixed) == N
        rows.append(f"(Z/{S})^{d}: bond planes {len(bond_all)} (= N/2, even starts), site planes {len(site_all)}, mixed {len(mixed)} (= N)")
    check("C2", ok, "; ".join(rows))

    try:
        branch = subprocess.run(["gh", "pr", "view", "8151", "--json", "headRefName", "-q", ".headRefName"], capture_output=True, text=True, check=True).stdout.strip()
        subprocess.run(["git", "fetch", "-q", "origin", branch], check=True)
        files = subprocess.run(["git", "diff", "--name-only", f"origin/main...origin/{branch}"], capture_output=True, text=True, check=True).stdout.split()
        note = [f for f in files if f.startswith("docs/") and "NOTE" in f and f.endswith(".md")][0]
        text = subprocess.run(["git", "show", f"origin/{branch}:{note}"], capture_output=True, text=True, check=True).stdout
        t2 = "T2 reflection positivity through site planes, any weights" in text
    except Exception as exc:
        t2 = False
        print(f"INFO: could not read the block 17 note ({type(exc).__name__})")
    check("C3", t2, "block 17 (PR #8151) states 'T2 reflection positivity through site planes, any weights': the ingredient the attempt "
          "leaves open for the mixed group is already available, so with W PSD the mixed chessboard disseminates to all N bonds")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - a3's partial survives: W's spectrum and the PSD condition (p >= q, p + q >= 2r; p >= 3 on (p,1,2)), the orbits "
          "N/2 for bond planes alone (even longitudinal starts), N/2^(d-1) for site planes, N for site planes along the bond with bond planes "
          "across, re-derived with independent code on four tori; its section (4) asks for site-plane RP, which block 17's T2 already "
          "supplies for any weights, so the mixed-group repair it describes is available (the route of attempt a1)")
    print("SUMMARY: confirmed - no failing step; the stated obstruction to finishing is already resolved by block 17's T2")
    return 0


if __name__ == "__main__":
    sys.exit(main())
