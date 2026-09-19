#!/usr/bin/env python3
"""Referee of J:derive:chessboard-repair:a2 (author w-macbookpro90c72-j1e77, grok-4.6); referee w-jonathonsmac4f50-j4a80
(claude-opus-5). Independent code (sympy for the spectrum; my own enumeration of reflections, cells and orbits); nothing from the
author's check.py. Disclosure: this referee's model family wrote attempt a1 of this problem (the mixed chessboard: site planes
along the bond, bond planes across it), which is the chessboard that S3c exhibits.

Bonds of direction i on the torus (Z/S)^d are named by their start x (the bond {x, x + e_i}); N = S^d of them.
Reflections: site plane x_j -> 2k - x_j; bond plane (between k and k + 1) x_j -> 2k + 1 - x_j. A direction-i bond with start s
along i goes to start 2k - 1 - s (site plane along i) or 2k - s (bond plane along i).

S1  step 1: W (p same, q antipodal, r orthogonal) has eigenvalues p + q + 4r (1), p - q (3), p + q - 2r (2); for p, q, r >= 0 it is
    PSD iff p >= q and p + q >= 2r (sympy, plus every integer triple in [0,6]^3)
S2  step 2: on (Z/4)^2, (Z/6)^2, (Z/4)^3, (Z/6)^3 each even 2-cell c + {0,1}^d holds 2^(d-1) direction-0 bonds, one per transverse
    parity class, all with even start; the tiling's union is the N/2 even-start bonds
S3a step 3's parity sentences, every reflection and every bond: site planes along i FLIP the longitudinal start parity, bond planes
    along i PRESERVE it; site planes across preserve transverse parity, bond planes across flip it. The attempt says site
    reflection 'does not move x_i mod 2' and bond-plane reflections 'would move longitudinal parity': both reversed
S3b the narrow no-go: the reflections mapping the even 2-cell tiling to itself are the bond planes; the orbit of a cell's
    direction-0 bonds under them is exactly the N/2 even-start bonds (holds)
S3c the chessboard the attempt says does not exist: site planes along i with bond planes across map the 2-cell to 2-windows at
    every corner along i and even corners across (overlapping along i on shared faces only: the site-plane block structure), and
    the orbit of a cell's direction-0 bonds, and of a single bond, is all N bonds
S3d its reflection positivity: site planes for any weights (block 17's T2, read from the note on PR #8151's branch), bond planes
    when W is PSD (S1; p >= 3 on (p,1,2))
"""
from __future__ import annotations

import itertools
import subprocess
import sys

import sympy as sp

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


def reflect_site(x, j, k, kind, S, i=0):
    """image of a site (bond=False) or of a direction-i bond start (bond=True) under the reflection of `kind` in direction j"""
    y = list(x)
    if kind == "site":
        y[j] = (2 * k - x[j]) % S
    else:
        y[j] = (2 * k + 1 - x[j]) % S
    return tuple(y)


def reflect_bond(x, j, k, kind, S, i=0):
    y = list(x)
    if kind == "site":
        y[j] = ((2 * k - x[j] - 1) if j == i else (2 * k - x[j])) % S
    else:
        y[j] = ((2 * k - x[j]) if j == i else (2 * k + 1 - x[j])) % S
    return tuple(y)


def cell(c, d, S):
    return frozenset(tuple((c[t] + u[t]) % S for t in range(d)) for u in itertools.product((0, 1), repeat=d))


def cell_bonds(c, d, S):
    return {tuple((c[t] + u[t]) % S for t in range(d)) for u in itertools.product((0, 1), repeat=d) if u[0] == 0}


def orbit_bonds(start_set, d, S, moves):
    seen = set(start_set)
    st = list(start_set)
    while st:
        x = st.pop()
        for j, kind in moves:
            for k in range(S):
                y = reflect_bond(x, j, k, kind, S)
                if y not in seen:
                    seen.add(y)
                    st.append(y)
    return seen


def orbit_cells(c0, d, S, moves):
    start = cell(c0, d, S)
    seen = {start}
    st = [start]
    while st:
        C = st.pop()
        for j, kind in moves:
            for k in range(S):
                D = frozenset(reflect_site(x, j, k, kind, S) for x in C)
                if D not in seen:
                    seen.add(D)
                    st.append(D)
    return seen


def main():
    # S1
    p, q, r = sp.symbols("p q r")
    W = sp.Matrix(6, 6, lambda a, b: p if a == b else (q if b == (a ^ 1) else r))
    got = {sp.expand(k): v for k, v in W.eigenvals().items()}
    want = {sp.expand(p + q + 4 * r): 1, sp.expand(p - q): 3, sp.expand(p + q - 2 * r): 2}
    grid_ok = True
    for a, b, c in itertools.product(range(7), repeat=3):
        M = sp.Matrix(6, 6, lambda s, t: a if s == t else (b if t == (s ^ 1) else c))
        psd = all(e >= 0 for e in M.eigenvals())
        grid_ok &= psd == (a >= b and a + b >= 2 * c)
    check("S1", got == want and grid_ok, "eigenvalues " + ", ".join(f"{k} (x{v})" for k, v in got.items())
          + "; PSD iff p >= q and p + q >= 2r on all 343 integer triples in [0,6]^3 (on (p,1,2): p >= 3)")

    tori = ((2, 4), (2, 6), (3, 4), (3, 6))
    # S2
    ok, rows = True, []
    for d, S in tori:
        N = S ** d
        corners = [c for c in itertools.product(range(0, S, 2), repeat=d)]
        union = set()
        for c in corners:
            B = cell_bonds(c, d, S)
            classes = {tuple(x[t] % 2 for t in range(1, d)) for x in B}
            ok &= len(B) == 2 ** (d - 1) and len(classes) == 2 ** (d - 1) and all(x[0] % 2 == 0 for x in B)
            union |= B
        even = {x for x in itertools.product(range(S), repeat=d) if x[0] % 2 == 0}
        ok &= union == even and len(union) == N // 2
        rows.append(f"(Z/{S})^{d}: {len(corners)} cells, union {len(union)} = N/2")
    check("S2", ok, "each even 2-cell holds one direction-0 bond per transverse parity class, all even starts; " + "; ".join(rows))

    # S3a
    ok = True
    for d, S in tori:
        for x in itertools.product(range(S), repeat=d):
            for k in range(S):
                ok &= reflect_bond(x, 0, k, "site", S)[0] % 2 != x[0] % 2
                ok &= reflect_bond(x, 0, k, "bond", S)[0] % 2 == x[0] % 2
                for j in range(1, d):
                    ok &= reflect_bond(x, j, k, "site", S)[j] % 2 == x[j] % 2
                    ok &= reflect_bond(x, j, k, "bond", S)[j] % 2 != x[j] % 2
    check("S3a", ok, "on all four tori, for every bond and plane: a site plane along the bond flips the longitudinal start parity "
          "(s -> 2k - 1 - s), a bond plane along it preserves it (s -> 2k - s); across the bond, site planes preserve and bond "
          "planes flip the transverse parity. Step 3 states the longitudinal cases the other way round")

    # S3b and S3c
    okb, okc, rows = True, True, []
    for d, S in tori:
        N = S ** d
        c0 = (0,) * d
        B0 = cell_bonds(c0, d, S)
        all_bond = [(j, "bond") for j in range(d)]
        tiling = {cell(c, d, S) for c in itertools.product(range(0, S, 2), repeat=d)}
        cells_b = orbit_cells(c0, d, S, all_bond)
        orb_b = orbit_bonds(B0, d, S, all_bond)
        even = {x for x in itertools.product(range(S), repeat=d) if x[0] % 2 == 0}
        okb &= cells_b == tiling and orb_b == even
        mixed = [(0, "site")] + [(j, "bond") for j in range(1, d)]
        cells_m = orbit_cells(c0, d, S, mixed)
        want = {cell(c, d, S) for c in itertools.product(range(S), *[range(0, S, 2)] * (d - 1))}
        faces_ok = True
        for C, D in itertools.combinations(cells_m, 2):
            I = C & D
            if I:
                xs = {x[0] for x in I}
                faces_ok &= len(xs) == 1 and len(I) == 2 ** (d - 1)
        orb_m = orbit_bonds(B0, d, S, mixed)
        orb_1 = orbit_bonds({c0}, d, S, mixed)
        okc &= cells_m == want and faces_ok and len(orb_m) == N and len(orb_1) == N
        rows.append(f"(Z/{S})^{d}: tiling group {len(cells_b)} cells / {len(orb_b)} bonds; mixed group {len(cells_m)} windows / "
                    f"{len(orb_m)} bonds (single bond {len(orb_1)}), N = {N}")
    check("S3b", okb, "the bond planes map the even 2-cell tiling to itself and carry a cell's direction-0 bonds onto exactly the "
          "N/2 even-start bonds (the attempt's narrow no-go holds)")
    check("S3c", okc, "site planes along the bond with bond planes across carry the 2-cell onto the 2-windows at every corner along "
          "the bond and even corners across, meeting only in shared faces x_0 = const, and a cell's direction-0 bonds (or one bond) "
          "onto all N: " + "; ".join(rows))

    # S3d
    try:
        branch = subprocess.run(["gh", "pr", "view", "8151", "--json", "headRefName", "-q", ".headRefName"], capture_output=True,
                                text=True, check=True).stdout.strip()
        subprocess.run(["git", "fetch", "-q", "origin", branch], check=True)
        files = subprocess.run(["git", "diff", "--name-only", f"origin/main...origin/{branch}"], capture_output=True, text=True,
                               check=True).stdout.split()
        note = [f for f in files if f.startswith("docs/") and "NOTE" in f and f.endswith(".md")][0]
        text = subprocess.run(["git", "show", f"origin/{branch}:{note}"], capture_output=True, text=True, check=True).stdout
        t2 = "T2 reflection positivity through site planes, any weights" in text
    except Exception as exc:
        t2 = False
        print(f"INFO: could not read the block 17 note ({type(exc).__name__})")
    check("S3d", t2, "block 17 (PR #8151) states 'T2 reflection positivity through site planes, any weights'; with the bond planes "
          "reflection positive when W is PSD (S1), the S3c group is a single chessboard on overlapping 2-windows for p >= 3 on (p,1,2)")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 3 - the counting holds (W's spectrum and PSD condition; an even 2-cell holds one direction-i bond per "
          "transverse parity class, all even starts, the tiling's union is N/2; the tiling's own bond-plane group reaches only those N/2), "
          "but step 3's parity claims are reversed: a site plane along the bond flips the longitudinal start parity and a bond plane "
          "along it preserves it (S3a, every bond and plane on four tori), and the overlapping 2-windows the statement calls 'not a "
          "chessboard product' are the blocks of the mixed group (site planes along i, bond planes across), whose orbit is all N bonds "
          "(S3c) and which is reflection positive for W PSD by block 17's T2 (S3d); the no-go holds only for the single tiling's "
          "bond-plane group")
    return 0


if __name__ == "__main__":
    sys.exit(main())
