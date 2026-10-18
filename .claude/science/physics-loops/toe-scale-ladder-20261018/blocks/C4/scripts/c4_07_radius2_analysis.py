#!/usr/bin/env python3
"""C4 step 7: analysis of the radius-2 O-covariant solutions under the soldered actions (axis, full),
found by c4_06 (4 unsigned / 4 signed each, 3 non-on-site).  Re-enumerates (exhaustive, same
enumerator as c4_06) and reports for each solution: signed images, support, trace, M^2, signed
period, closure under composition, and the dynamical class (Theorem 2)."""
import os
import sys
import time
os.environ['C4_RADIUS'] = '2'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c4lib as L

P = F = 0


def check(name, ok):
    global P, F
    if ok:
        P += 1
        print('PASS', name, flush=True)
    else:
        F += 1
        print('FAIL', name, flush=True)


D = L.D
OG = L.SUBGROUPS['O']
I2 = [[L.ONE, L.ZERO], [L.ZERO, L.ONE]]


def mat_key(M):
    return tuple(tuple(sorted(M[i][j])) for i in range(2) for j in range(2))


def apply_alpha(im, Pstr):
    out = (Pstr[0], {})
    for s, a in Pstr[1].items():
        out = L.pmul(out, L.translate(im[a], s))
    return out


def signed_period(PX, PZ, kmax=12):
    im = L.images(PX, PZ)
    X0, Z0 = (0, {(0, 0, 0): 1}), (0, {(0, 0, 0): 3})
    a, b = X0, Z0
    for k in range(1, kmax + 1):
        a, b = apply_alpha(im, a), apply_alpha(im, b)
        if L.peq(a, X0) and L.peq(b, Z0):
            return k
    return None


def shape_summary(Pstr):
    from collections import Counter
    c = Counter()
    for s, a in Pstr[1].items():
        c[(tuple(sorted(map(abs, s))), 'IXYZ'[a])] += 1
    return dict(sorted(c.items()))


for nm in os.environ.get('C4_ACTIONS', 'full,axis').split(','):
    h = tuple(L.menu_hom(nm))
    B = L.covariance_space(h, h, OG)
    t0 = time.time()
    uns = L.enumerate_solutions_split(B)
    print(f'== {nm}: {len(uns)} unsigned solutions ({time.time() - t0:.0f}s)')
    sols = []
    for s in uns:
        for sx in (1, -1):
            for sz in (1, -1):
                PX, PZ = L.pstr_from_vec(s[:D], sx), L.pstr_from_vec(s[D:], sz)
                if L.signed_covariant(PX, PZ, h, h, OG):
                    sols.append((s, PX, PZ))
    Ms = []
    for k, (s, PX, PZ) in enumerate(sols):
        M = L.matrix_of(s)
        Ms.append(M)
        tau = L.trace(M)
        M2 = L.mat_mul(M, M)
        per = signed_period(PX, PZ)
        rad = max([max(map(abs, e)) for e in list(PX[1]) + list(PZ[1])] + [0])
        print(f'  [{k}] sign(X,Z)=({1 if PX[0] == 0 else -1},{1 if PZ[0] == 0 else -1}) '
              f'tau={L.poly_str(tau)}  M^2=1: {mat_key(M2) == mat_key(I2)}  signed period={per}  '
              f'image radius={rad}  |supp X|={len(PX[1])} |supp Z|={len(PZ[1])}')
        print(f'      alpha(X_0) by (|site| shape, label): {shape_summary(PX)}')
        print(f'      alpha(Z_0) by (|site| shape, label): {shape_summary(PZ)}')
        if k > 0 and len(PX[1]) <= 40:
            print(f'      alpha(X_0) = sign {PX[0]} * {sorted(PX[1].items())}')
            print(f'      alpha(Z_0) = sign {PZ[0]} * {sorted(PZ[1].items())}')
    keys = {mat_key(M) for M in Ms}
    closed = all(mat_key(L.mat_mul(A, B_)) in keys for A in Ms for B_ in Ms)
    check(f'r2/{nm}: the unsigned solutions are closed under composition (a group of order {len(Ms)})', closed)
    check(f'r2/{nm}: every solution has constant trace (periodic class, Theorem 2)',
          all(L.trace(M) in (L.ZERO, L.ONE) for M in Ms))
    check(f'r2/{nm}: every solution satisfies M^2 = 1 (involution mod phases)',
          all(mat_key(L.mat_mul(M, M)) == mat_key(I2) for M in Ms))
print(f'TOTAL: PASS={P} FAIL={F}')
