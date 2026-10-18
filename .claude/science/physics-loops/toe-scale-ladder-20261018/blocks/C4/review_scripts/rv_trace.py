"""Instance checks of Theorem 2 (a)-(c) on the reviewer's own radius-1 solutions:
det M = 1, tau O-invariant, number with nonconstant tau, Cayley-Hamilton M^2 = tau M + 1, Dickson
tr(M^n) = D_n(tau), and the vertex claim x^{n v} in tr(M^n) for every vertex v of Newt(tau), n <= 5."""
import itertools
import numpy as np
from rv_common import O
from rv_classify import classify
from rv_linear import decode

def pmul(A, B):
    out = set()
    for a in A:
        for b in B:
            out ^= {(a[0]+b[0], a[1]+b[1], a[2]+b[2])}
    return frozenset(out)
def padd(A, B): return frozenset(set(A) ^ set(B))
def poly(Pd, want): return frozenset(r for r, a in Pd.items() if (a in 'XY' if want == 'x' else a in 'ZY'))
def mat(PX, PZ): return [[poly(PX,'x'), poly(PZ,'x')], [poly(PX,'z'), poly(PZ,'z')]]
def mmul(A, B): return [[padd(pmul(A[i][0], B[0][j]), pmul(A[i][1], B[1][j])) for j in range(2)] for i in range(2)]
ONE = frozenset({(0,0,0)}); Z0 = frozenset()
I2 = [[ONE, Z0], [Z0, ONE]]

def vertices(P):
    pts = np.array(sorted(P))
    vs = []
    # a point is a vertex iff it is not a convex combination of the other points (LP feasibility)
    from scipy.optimize import linprog
    for i, p in enumerate(pts):
        others = np.delete(pts, i, axis=0)
        if len(others) == 0:
            vs.append(tuple(p)); continue
        res = linprog(np.zeros(len(others)), A_eq=np.vstack([others.T, np.ones(len(others))]),
                      b_eq=np.append(p, 1), bounds=[(0, None)] * len(others), method='highs')
        if not res.success:
            vs.append(tuple(int(c) for c in p))
    return vs

PASS = FAIL = 0
def check(name, ok):
    global PASS, FAIL
    print(('PASS ' if ok else 'FAIL ') + name, flush=True); PASS += bool(ok); FAIL += (not ok)

for action in ('trivial', 'sign', 'signf'):
    sites, vecs, d = classify(1, action)
    Ms = [mat(*decode(v, sites)) for v in vecs]
    det_ok = all(padd(pmul(M[0][0], M[1][1]), pmul(M[0][1], M[1][0])) == ONE for M in Ms)
    taus = [padd(M[0][0], M[1][1]) for M in Ms]
    inv_ok = all(frozenset(tuple(int(c) for c in R @ np.array(e)) for e in t) == t for t in taus for R in O)
    noncon = [k for k, t in enumerate(taus) if not (t <= {(0,0,0)})]
    ch_ok = dick_ok = vert_ok = True
    for k in noncon:
        M, t = Ms[k], taus[k]
        tM = [[pmul(t, M[i][j]) for j in range(2)] for i in range(2)]
        ch_ok &= mmul(M, M) == [[padd(tM[i][j], I2[i][j]) for j in range(2)] for i in range(2)]
        D = [Z0, t]; P = I2
        vs = vertices(t)
        for n in range(1, 6):
            P = mmul(P, M)
            if n >= 2: D.append(padd(pmul(t, D[-1]), D[-2]))
            tr = padd(P[0][0], P[1][1])
            dick_ok &= tr == D[n]
            vert_ok &= all((n*v[0], n*v[1], n*v[2]) in tr for v in vs)
    print(f'{action}: {len(Ms)} unsigned, nonconstant tau: {len(noncon)}')
    check(f'{action}: det M = 1 for all', det_ok)
    check(f'{action}: tau O-invariant for all', inv_ok)
    check(f'{action}: Cayley-Hamilton, Dickson tr(M^n)=D_n(tau), vertex monomials x^(n v) present, n<=5', ch_ok and dick_ok and vert_ok)
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
