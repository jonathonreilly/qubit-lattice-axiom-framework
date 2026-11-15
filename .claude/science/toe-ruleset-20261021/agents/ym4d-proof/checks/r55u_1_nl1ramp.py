#!/usr/bin/env python3
"""r55u_1_nl1ramp.py -- REVIEW55_TUNIF check r55u_1 (criteria: checks/r55u_1_criteria.md, written first).
NLOC Lemma NL-1's spread-axial construction, implemented from its text, applied to explicit fields on (Z/R)^d.
Exact rationals only (fractions.Fraction). Independent code: imports nothing from the lane."""
from fractions import Fraction as Fr
from itertools import product
import sys

def sites(R, d):
    return list(product(range(R), repeat=d))

def shift(y, mu, R, s=1):
    z = list(y); z[mu] = (z[mu] + s) % R; return tuple(z)

def curl(B, R, d):
    out = {}
    for y in sites(R, d):
        for a in range(d):
            for b in range(a + 1, d):
                out[(a, b, y)] = B[a][y] + B[b][shift(y, a, R)] - B[a][shift(y, b, R)] - B[b][y]
    return out

def nl1(B0, R, d):
    """Return (B', lam) with B' = B0 - d lam, following NLOC Lemma NL-1 Steps 1-3 (rounds r = 0..d-1)."""
    B = [dict(B0[m]) for m in range(d)]
    lam_tot = {y: Fr(0) for y in sites(R, d)}
    for r in range(d):
        # transverse positions t = coordinates r+1..d-1 ; earlier coordinates fixed to 0 (sub-torus S_r)
        lamr = {}
        for t in product(range(R), repeat=d - r - 1):
            line = [B[r][tuple([0] * r + [i] + list(t))] for i in range(R)]
            w = sum(line, Fr(0))
            acc = Fr(0)
            for i in range(R):
                lamr[(i,) + t] = acc
                acc += line[i] - w / R
            assert acc == 0
        lam = {y: lamr[y[r:]] for y in sites(R, d)}       # independent of y_0..y_{r-1}
        for m in range(d):
            for y in sites(R, d):
                B[m][y] -= lam[shift(y, m, R)] - lam[y]
        for y in lam_tot:
            lam_tot[y] += lam[y]
    return B, lam_tot

def field(kind, R, d):
    B = [{y: Fr(0) for y in sites(R, d)} for _ in range(d)]
    for y in sites(R, d):
        sgn = 1 if y[1] % 2 == 0 else -1
        if kind == "test":
            B[0][y] = Fr(sgn) if y[0] < R // 2 else Fr(0)
        else:
            B[0][y] = Fr(sgn)
    return B

def run(kind, R, d):
    B0 = field(kind, R, d)
    Bp, lam = nl1(B0, R, d)
    c0, c1 = curl(B0, R, d), curl(Bp, R, d)
    bad_curl = sum(1 for k in c0 if c0[k] != c1[k])
    n = R ** d
    h0 = [sum(B0[m].values(), Fr(0)) / n for m in range(d)]
    h1 = [sum(Bp[m].values(), Fr(0)) / n for m in range(d)]
    bad_mean = sum(1 for m in range(d) if h0[m] != h1[m])
    S = max(abs(Bp[m][y] - h0[m]) for m in range(d) for y in sites(R, d))
    supB = max(abs(B0[m][y]) for m in range(d) for y in sites(R, d))
    supdB = max(abs(v) for v in c0.values())
    return S, supB, supdB, bad_curl, bad_mean

def main():
    okA, okB, fireC = True, True, True
    print("kind   d   R   S=max|B-dlam-h|   |B|inf  |dB|inf  S/(4dR|dB|)  bad_curl bad_mean")
    for d, Rs in ((2, (4, 8, 16, 32)), (3, (4, 8, 16))):
        for R in Rs:
            for kind in ("test", "ctrl"):
                S, supB, supdB, bc, bm = run(kind, R, d)
                ratio = S / (4 * d * R * supdB) if supdB else Fr(0)
                print(f"{kind:5s} {d:2d} {R:3d}   {str(S):>14s}   {str(supB):>5s}  {str(supdB):>6s}  {str(ratio):>10s}  {bc:6d} {bm:6d}")
                if bc or bm: okA = False
                if kind == "test" and not (S >= Fr(R, 4)): okB = False
                if kind == "ctrl" and not (S <= 1): fireC = False
                if ratio > 1: print("   r55u_1-D: Lemma NL-1 bound exceeded (would contradict NL-1)")
    print(f"r55u_1-A (implementation exact): {'PASS' if okA else 'FAIL'}")
    print(f"r55u_1-B (S(R) >= R/4 for TEST, all R): {'PASS' if okB else 'FAIL'}")
    print(f"r55u_1-C (designed-FAIL control: CTRL stays <= 1): {'FIRED as designed' if fireC else 'DID NOT FIRE'}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
