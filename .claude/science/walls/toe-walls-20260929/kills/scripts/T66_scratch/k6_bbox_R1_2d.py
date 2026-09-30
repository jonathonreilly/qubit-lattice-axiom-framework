"""Kill check: the attack's 2D R=1 'window' has ONE xy face (faces indexed i,j < R) for V2/T3, while G2/xi1/chi use a bounding-box rule
(spread <= R lattice units in each direction, incl. faces at half-integers). Redo R=1 (and optionally R=2) with the bounding-box rule for V2/T3
too, and test the ADM-matched 2D system exactly (mod two primes)."""
import sys, itertools, time
import numpy as np
from fractions import Fraction as F
import solve2d, solve2d_sym as S
from engine2 import canon
from solve import rref_mod, PRIMES

R = int(sys.argv[1]) if len(sys.argv) > 1 else 1

def positions(R):
    """all doubled positions in [0, 2R+1]^2 : sites (even,even) for comps XX,YY,ZZ ; faces (odd,odd) for XY"""
    out = []
    for px in range(0, 2 * R + 2):
        for py in range(0, 2 * R + 2):
            if px % 2 == 0 and py % 2 == 0:
                for c in (solve2d.XX, solve2d.YY, solve2d.ZZ):
                    out.append((c, (px, py)))
            elif px % 2 == 1 and py % 2 == 1:
                out.append((solve2d.XY, (px, py)))
    return out

def lapse_positions(R):
    return [(px, py) for px in range(0, 2 * R + 1, 2) for py in range(0, 2 * R + 1, 2)]

def bbox(points):
    xs = [p[0] for p in points]; ys = [p[1] for p in points]
    return max(xs) - min(xs), max(ys) - min(ys)

def enum_bbox(R, kind):
    pos = positions(R); lps = lapse_positions(R)
    res = set()
    if kind == 'V2':
        for (a, b) in itertools.combinations_with_replacement(pos, 2):
            for lp in lps:
                w = bbox([a[1], b[1], lp])
                if w[0] <= 2 * R and w[1] <= 2 * R:
                    res.add(canon(tuple(sorted([('N', 0, lp), ('h', a[0], a[1]), ('h', b[0], b[1])]))))
    else:
        for (a, b) in itertools.combinations_with_replacement(pos, 2):
            for hh in pos:
                for lp in lps:
                    w = bbox([a[1], b[1], hh[1], lp])
                    if w[0] <= 2 * R and w[1] <= 2 * R:
                        res.add(canon(tuple(sorted([('N', 0, lp), ('P', a[0], a[1]), ('P', b[0], b[1]), ('h', hh[0], hh[1])]))))
    return sorted(res)

old_V2 = solve2d.enum_V2(R); old_T3 = solve2d.enum_T3(R)
new_V2 = enum_bbox(R, 'V2'); new_T3 = enum_bbox(R, 'T3')
print(f"R={R}: V2 monomials old {len(old_V2)} new(bbox) {len(new_V2)} ; T3 old {len(old_T3)} new(bbox) {len(new_T3)}", flush=True)
print("old subset of new:", set(old_V2) <= set(new_V2), set(old_T3) <= set(new_T3), flush=True)
S.enum_V2 = lambda R_: new_V2
S.enum_T3 = lambda R_: new_T3

def exact(match):
    cols = S.build_sym(R, verbose=False)
    rows, entries, b, nr0 = S.assemble(cols, match, R)
    nr, nc = len(rows), len(cols)
    out = []
    for p in PRIMES[:2]:
        M = np.zeros((nr, nc + 1), dtype=np.int64)
        for i, j, c in entries:
            M[i, j] = (M[i, j] + (c.numerator % p) * pow(c.denominator % p, -1, p)) % p
        for i, c in b.items():
            M[i, nc] = (c.numerator % p) * pow(c.denominator % p, -1, p) % p
        rk, cons, piv, Mred = rref_mod(M, p, nc)
        out.append((p, rk, cons))
    return nr, nc, out

t0 = time.time()
print("identity-only:", exact(()), round(time.time() - t0, 1), flush=True)
print("ADM-matched  :", exact(('V2', 'T3', 'G2', 'xi1', 'chi')), round(time.time() - t0, 1), flush=True)
