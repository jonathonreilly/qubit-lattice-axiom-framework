"""A33 helper (factored from a9_inspect.py): commutant of the generators on a box, and an exact
impurity certificate (two anticommuting Paulis on the box, each commuting with every Z^3 generator)."""
import itertools
from p2a_core import role_of, shape_at
from p2lib import Elim, BITS2L, pcomm
from p2_tests import box


def commutant(S, sh, B):
    pos = {y: k for k, y in enumerate(B)}
    rad = S.rinf
    xs = {tuple(a + d for a, d in zip(y, dd)) for y in B for dd in itertools.product(range(-rad, rad + 1), repeat=3)}
    E = Elim()
    for x in xs:
        role, axis = role_of(x)
        _, p = shape_at(sh[role], role, axis, x)
        row = 0
        for z, l in p.items():
            if z in pos:
                kk = pos[z]
                bx, bz = {1: (1, 0), 2: (1, 1), 3: (0, 1)}[l]
                if bz:
                    row |= 1 << (2 * kk)
                if bx:
                    row |= 1 << (2 * kk + 1)
        if row:
            E.add(row)
    n = 2 * len(B)
    R = {h: v for h, (v, _) in E.rows.items()}
    hs = sorted(R, reverse=True)
    for h in hs:
        for h2 in hs:
            if h2 != h and (R[h2] >> h) & 1:
                R[h2] ^= R[h]
    pats = []
    for f in range(n):
        if f in R:
            continue
        v = 1 << f
        for h, row in R.items():
            if (row >> f) & 1:
                v |= 1 << h
        p = {}
        for kk, y in enumerate(B):
            a_, b_ = (v >> (2 * kk)) & 1, (v >> (2 * kk + 1)) & 1
            if a_ or b_:
                p[y] = BITS2L[(a_, b_)]
        pats.append(p)
    return pats


def certificate(S, sh, side, corner=(2, 2, 2)):
    pats = commutant(S, sh, box(corner, side))
    for i in range(len(pats)):
        for j in range(i + 1, len(pats)):
            if pcomm(pats[i], pats[j]):
                return len(pats), (pats[i], pats[j])
    return len(pats), None
