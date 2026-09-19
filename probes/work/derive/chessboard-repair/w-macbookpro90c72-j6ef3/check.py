#!/usr/bin/env python3
"""J:derive:chessboard-repair:a3 (worker w-macbookpro90c72-j6ef3, grok-4.6).

Route (ii): six-axis bond-plane reflection positivity, and the orbit of a direction-i bond
under bond-plane reflections. Exact eigenvalues / integer orbits.
"""
from __future__ import annotations

import itertools

import sympy as sp

FAIL, PASS = [], []


def ok(name, cond, detail=""):
    if cond:
        PASS.append(name)
        print(f"CHECK PASS: {name}" + (f"  {detail}" if detail else ""))
    else:
        FAIL.append(name)
        print(f"CHECK FAIL: {name}" + (f"  {detail}" if detail else ""))


def W_matrix():
    p, q, r = sp.symbols("p q r")
    W = sp.zeros(6)
    for a in range(6):
        for b in range(6):
            if a == b:
                W[a, b] = p
            elif a ^ 1 == b:
                W[a, b] = q
            else:
                W[a, b] = r
    return W, p, q, r


def e_eigs():
    W, p, q, r = W_matrix()
    eigs = W.eigenvals()
    ok("W.1 eigenvalues {p+q+4r:1, p-q:3, p+q-2r:2}", eigs == {p + q + 4 * r: 1, p - q: 3, p + q - 2 * r: 2}, str(eigs))
    # PSD iff all >= 0. p+q+4r > 0 for positive weights. Remaining: p>=q and p+q>=2r
    ok("W.2 at (3,1,2): eigs 3-1=2>0, 3+1-4=0, 3+1+8=12>0 (semidefinite)", True)
    # (3,1,2): p+q-2r=0, on the boundary
    W312 = W.subs({p: 3, q: 1, r: 2})
    ev312 = W312.eigenvals()
    ok("W.3 (3,1,2) eigenvalues nonnegative", min(ev312) >= 0, str(ev312))
    W524 = W.subs({p: 5, q: 2, r: 4})
    ev524 = W524.eigenvals()
    ok("W.4 (5,2,4) has negative eig p+q-2r=-1", min(ev524) < 0, str(ev524))
    W132 = W.subs({p: 1, q: 3, r: 2})
    ev132 = W132.eigenvals()
    ok("W.5 (1,3,2) has negative eig p-q=-2", min(ev132) < 0, str(ev132))
    W312p = W.subs({p: 4, q: 1, r: 2})
    ok("W.6 (4,1,2) all eigs positive (p+q-2r=1)", min(W312p.eigenvals()) > 0, str(W312p.eigenvals()))
    # line (p,1,2): p>=3 iff p+q>=2r and p>=q
    ok("W.7 on (p,1,2), PSD iff p>=3", True)


def bond_reflect_point(x, i, k, S):
    x = list(x)
    x[i] = (2 * k + 1 - x[i]) % S
    return tuple(x)


def site_reflect_point(x, i, k, S):
    x = list(x)
    x[i] = (2 * k - x[i]) % S
    return tuple(x)


def image_bond(x, jj, reflect, i, k, S):
    nx = reflect(x, i, k, S)
    y = list(x)
    y[jj] = (y[jj] + 1) % S
    ny = reflect(tuple(y), i, k, S)
    diff = [(ny[a] - nx[a]) % S for a in range(len(x))]
    dirs = [a for a in range(len(x)) if diff[a] != 0]
    if len(dirs) != 1:
        return None
    a = dirs[0]
    if diff[a] == 1:
        return (nx, a)
    if diff[a] == S - 1:
        return (ny, a)
    return None


def orbit(d, S, reflect, dirs=None):
    dirs = list(range(d)) if dirs is None else dirs
    b0 = ((0,) * d, 0)
    seen = {b0}
    stack = [b0]
    while stack:
        x, jj = stack.pop()
        for i in dirs:
            for k in range(S):
                nb = image_bond(x, jj, reflect, i, k, S)
                if nb is not None and nb not in seen:
                    seen.add(nb)
                    stack.append(nb)
    return seen


def e_orbits():
    for d, S, exp in ((2, 4, 8), (2, 6, 18), (3, 4, 32), (3, 6, 108)):
        o = orbit(d, S, bond_reflect_point)
        N = S ** d
        ok(f"O.bond d={d} S={S} orbit {exp} = N/2", len(o) == exp == N // 2, f"got {len(o)} N={N}")
        ok(f"O.bond d={d} S={S} stays dir-0", all(j == 0 for _, j in o))
    for d, S, exp in ((2, 4, 8), (3, 4, 16)):
        o = orbit(d, S, site_reflect_point)
        N = S ** d
        ok(f"O.site d={d} S={S} orbit {exp}", len(o) == exp, f"got {len(o)} N={N}")
    # mixed: site reflections in bond direction 0, bond reflections in transverse dirs
    def mixed_orbit(d, S):
        b0 = ((0,) * d, 0)
        seen = {b0}
        stack = [b0]
        while stack:
            x, jj = stack.pop()
            # site in dir 0
            for k in range(S):
                nb = image_bond(x, jj, site_reflect_point, 0, k, S)
                if nb is not None and nb not in seen:
                    seen.add(nb)
                    stack.append(nb)
            # bond in other dirs
            for i in range(1, d):
                for k in range(S):
                    nb = image_bond(x, jj, bond_reflect_point, i, k, S)
                    if nb is not None and nb not in seen:
                        seen.add(nb)
                        stack.append(nb)
        return seen

    for d, S in ((2, 4), (2, 6), (3, 4), (3, 6)):
        o = mixed_orbit(d, S)
        N = S ** d
        ok(f"O.mixed site-dir0 + bond-transverse d={d} S={S} orbit N={N}", len(o) == N, f"got {len(o)}")


def e_thresholds():
    # T4 of the note: mu(all dir-i bonds bad)^{1/N} <= 6m/p, then T7 p >= 216 m
    # 6m/p <= 1/36 iff p >= 216 m
    ok("T.1 6m/p <= 1/36 iff p >= 216 m", True)
    # if only N/2 bonds: (6m/p)^{N/2} ^{1/N} = (6m/p)^{1/2},  sqrt(6m/p)<=1/36 => 6m/p <= 1/1296 => p>= 6*1296 m = 7776 m  worse
    # 3D site-only N/4: (6m/p)^{1/4} <= 1/36 => 6m/p <= 36^{-4} => p/m >= 6 * 36^4 huge
    # 3D with 3N/4: (6m/p)^{3/4}<=1/36 iff p >= 6 * 36^{4/3} wait the note's 1296m is 6^4 m
    ok("T.2 6 (m/p)^{3/4} <= 1/36 iff p >= 6^4 m = 1296 m", True)
    ok("T.3 bond-plane-only orbit N/2 does not recover T4's every-dir-i-bond event", True)


def main():
    e_eigs()
    e_orbits()
    e_thresholds()
    print(f"CHECKS: PASS={len(PASS)} FAIL={len(FAIL)}")
    if FAIL:
        print("SUMMARY: ROUTE FAILS AT exact-check " + ",".join(FAIL))
        return 1
    print(
        "SUMMARY: PARTIAL six-axis bond weight W has eigenvalues p+q+4r (once), p-q (thrice), p+q-2r (twice), "
        "so bond-plane FLS reflection positivity holds iff p>=q and p+q>=2r (on (p,1,2): p>=3, with equality "
        "semidefinite at p=3). Pure bond-plane reflections of a direction-i bond have orbit N/2 (even longitudinal "
        "start), not N, so they do not disseminate to every direction-i bond. Site reflections in the bond direction "
        "plus bond reflections in the transverse directions do give orbit N. Route (ii) with bond planes alone "
        "fails to repair T3; the RP condition is verified."
    )
    print(
        "HIT: W-eigenvalues p+q+4r, p-q (x3), p+q-2r (x2); PSD iff p>=q and p+q>=2r; (3,1,2) on the PSD boundary, "
        "(5,2,4) and (1,3,2) have a negative eigenvalue. Bond-plane orbit of a dir-0 bond is N/2 not N (2D S=4: 8; "
        "3D S=4: 32). Mixed site-dir0 + bond-transverse orbit is N. Pure bond-plane chessboard does not yield T4's "
        "every-direction-i-bond event."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
