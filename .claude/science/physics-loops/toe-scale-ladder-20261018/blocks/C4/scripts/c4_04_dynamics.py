#!/usr/bin/env python3
"""C4 step 4: dynamics of every O-covariant radius-1 one-qubit Clifford QCA.

Proved facts checked on instances (the proofs are in NOTE.md, Theorem 2):
  (i)   Cayley-Hamilton over F2: M^2 = tau M + 1 (det M = 1).  tau = 0 -> M^2 = 1; tau = 1 -> M^3 = 1.
        Signed periods of alpha (with phases) computed exactly by iterating the automorphism.
  (ii)  tr(M^n) = D_n(tau), the char-2 Dickson polynomial D_n = tau D_{n-1} + D_{n-2}, D_0 = 0, D_1 = tau.
  (iii) light cone: for nonconstant tau and every vertex v of Newt(tau), x^{n v} occurs in tr(M^n)
        (so alpha^n(X_0) or alpha^n(Z_0) acts nontrivially at n v), and supp alpha^n(P_0) lies in n*cell.
  (iv)  no glider / no recurrence: det(M^n - x^t) = x^{2t} + tr(M^n) x^t + 1 != 0 for all checked n, t.
Numerical (not proof): support sizes of alpha^n(X_0) for n <= NMAX and a box-counting exponent.
"""
import sys
import os
import itertools
import numpy as np
from scipy.signal import convolve
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
NMAX = int(os.environ.get('C4_NMAX', '32'))
OG = L.SUBGROUPS['O']
REP = {a: tuple(L.menu_hom(a)) for a in ('trivial', 'sign', 'axis', 'full')}
Hf = L.G([[-1, 0, 0], [0, 0, 1], [0, 1, 0]])
REP['sign-f'] = tuple(L.ID if L.perm_sign(L.O[R]) == 1 else Hf for R in range(24))
NAMES = ['trivial', 'sign', 'sign-f', 'axis', 'full']
I2 = [[L.ONE, L.ZERO], [L.ZERO, L.ONE]]


def mat_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(2) for j in range(2))


def mat_scale_add(tau, M):
    """tau*M + 1"""
    return [[L.padd(L.pmulL(tau, M[i][j]), I2[i][j]) for j in range(2)] for i in range(2)]


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


# dense grid arithmetic for powers
def to_grid(p, R):
    g = np.zeros((2 * R + 1,) * 3, np.int64)
    for e in p:
        g[e[0] + R, e[1] + R, e[2] + R] = 1
    return g


def newton_vertices(p):
    from scipy.spatial import ConvexHull
    pts = np.array(sorted(p), float)
    if len(pts) < 4:
        return [tuple(int(v) for v in x) for x in pts]
    hull = ConvexHull(pts)
    return [tuple(int(v) for v in pts[i]) for i in hull.vertices]


def dickson(tau, n):
    d0, d1 = L.ZERO, tau
    if n == 0:
        return d0
    for _ in range(n - 1):
        d0, d1 = d1, L.padd(L.pmulL(tau, d1), d0)
    return d1


# ---------------------------------------------------------------- collect O-covariant solutions
sols = {}
for nm in NAMES:
    h = REP[nm]
    B = L.covariance_space(h, h, OG)
    uns = L.enumerate_solutions_split(B)
    signed = []
    for s in uns:
        for sx in (1, -1):
            for sz in (1, -1):
                PX, PZ = L.pstr_from_vec(s[:D], sx), L.pstr_from_vec(s[D:], sz)
                if L.signed_covariant(PX, PZ, h, h, OG):
                    signed.append((s, PX, PZ))
    sols[nm] = (uns, signed)
    print(f'{nm}: {len(uns)} unsigned, {len(signed)} signed')

# ---------------------------------------------------------------- (i) Cayley-Hamilton and periods
for nm in NAMES:
    uns, signed = sols[nm]
    ok_ch = ok0 = ok1 = True
    for s in uns:
        M = L.matrix_of(s)
        tau = L.trace(M)
        M2 = L.mat_mul(M, M)
        ok_ch &= mat_eq(M2, mat_scale_add(tau, M))
        if tau == L.ZERO:
            ok0 &= mat_eq(M2, I2)
        if tau == L.ONE:
            ok1 &= mat_eq(L.mat_mul(M2, M), I2)
    check(f'{nm}: Cayley-Hamilton M^2 = tau M + 1 for all unsigned solutions', ok_ch)
    check(f'{nm}: tau = 0 => M^2 = 1 and tau = 1 => M^3 = 1', ok0 and ok1)
    per = {}
    for s, PX, PZ in signed:
        tau = L.trace(L.matrix_of(s))
        if tau in (L.ZERO, L.ONE):
            k = signed_period(PX, PZ)
            per.setdefault('tau=' + ('0' if tau == L.ZERO else '1'), {}).setdefault(k, 0)
            per['tau=' + ('0' if tau == L.ZERO else '1')][k] += 1
    print(f'  {nm}: signed periods of periodic-class QCAs (tau -> {{period: count}}): {per}')
    allp = all(k is not None and k <= 6 for d in per.values() for k in d)
    check(f'{nm}: every signed periodic-class QCA has exact period dividing 4 or 6 (alpha^4 or alpha^6 = id)',
          allp and all(k in (1, 2, 3, 4, 6) for d in per.values() for k in d))

# ---------------------------------------------------------------- (ii)-(iv) spreading class
spread = [(nm, s) for nm in ('trivial', 'sign') for s in sols[nm][0]
          if L.trace(L.matrix_of(s)) not in (L.ZERO, L.ONE)]
print(f'\nspreading-class unsigned solutions (trivial+sign): {len(spread)}')
check('spreading class exists only for the trivial and sign actions (none for sign-f, axis, full)',
      all(L.trace(L.matrix_of(s)) in (L.ZERO, L.ONE) for nm in ('sign-f', 'axis', 'full') for s in sols[nm][0]))

NSYM = 8
ok_dick = ok_vert = ok_cone = ok_glide = True
for nm, s in spread:
    M = L.matrix_of(s)
    tau = L.trace(M)
    verts = newton_vertices(tau)
    Mn = M
    for n in range(1, NSYM + 1):
        if n > 1:
            Mn = L.mat_mul(M, Mn)
        tn = L.trace(Mn)
        ok_dick &= (tn == dickson(tau, n))
        ok_vert &= all((n * v[0], n * v[1], n * v[2]) in tn for v in verts)
        ok_cone &= all(max(map(abs, e)) <= n for i in range(2) for j in range(2) for e in Mn[i][j])
        # glider / recurrence test: x^{2t} + tn x^t + 1 == 0 ?
        for t in itertools.product(range(-n - 1, n + 2), repeat=3):
            xt = frozenset({t})
            val = L.padd(frozenset({(2 * t[0], 2 * t[1], 2 * t[2])}), L.pmulL(tn, xt), L.ONE)
            if val == L.ZERO:
                ok_glide = False
check(f'tr(M^n) equals the char-2 Dickson polynomial D_n(tau), all {len(spread)} spreading solutions, n<={NSYM}', ok_dick)
check(f'x^(n v) occurs in tr(M^n) for every vertex v of Newt(tau), n<={NSYM}', ok_vert)
check(f'supp M^n lies in the n-cell (range n), n<={NSYM}', ok_cone)
check(f'det(M^n - x^t) != 0 for all |t|_inf <= n+1, n<={NSYM} (no glider, no recurrent operator)', ok_glide)

# ---------------------------------------------------------------- numerical support growth (evidence)
print(f'\nsupport growth of alpha^n(X_0), n <= {NMAX} (numerical evidence; exact F2 convolution)')


def grow(M, nmax, seed):
    R = nmax + 1
    K = [[to_grid(M[i][j], 1) for j in range(2)] for i in range(2)]
    z = np.zeros((2 * R + 1,) * 3, np.int64)
    vx, vz = (to_grid(L.ONE, R), z.copy()) if seed == 'X' else (z.copy(), to_grid(L.ONE, R))
    out = []
    for n in range(1, nmax + 1):
        nx = (convolve(vx, K[0][0], mode='same', method='direct') + convolve(vz, K[0][1], mode='same', method='direct')) % 2
        nz = (convolve(vx, K[1][0], mode='same', method='direct') + convolve(vz, K[1][1], mode='same', method='direct')) % 2
        vx, vz = nx.astype(np.int64), nz.astype(np.int64)
        supp = (vx | vz)
        idx = np.argwhere(supp)
        rad = int(np.max(np.abs(idx - R))) if len(idx) else 0
        out.append((n, int(supp.sum()), rad))
    return out


reps = {}
for nm, s in spread:
    M = L.matrix_of(s)
    key = (nm, tuple(sorted(set(tuple(sorted(map(abs, e))) for e in L.trace(M)))),
           tuple(sorted(set(tuple(sorted(map(abs, e))) for i in range(2) for j in range(2) for e in M[i][j]))))
    reps.setdefault(key, s)
print(f'  {len(reps)} representatives (action, orbit shapes in tau, orbit shapes in M)')
ok_lb = True
nsat = 0
for key, s in sorted(reps.items()):
    M = L.matrix_of(s)
    tau = L.trace(M)
    gX, gZ = grow(M, NMAX, 'X'), grow(M, NMAX, 'Z')
    vmax = max(max(map(abs, v)) for v in newton_vertices(tau))
    lb = all(max(a[2], b[2]) >= n * vmax for (n, _, _), a, b in zip(gX, gX, gZ))
    ub = all(max(a[2], b[2]) <= n for (n, _, _), a, b in zip(gX, gX, gZ))
    ok_lb &= lb and ub
    sat = all(max(a[2], b[2]) == n for (n, _, _), a, b in zip(gX, gX, gZ))
    nsat += sat
    sizes = [c for (_, c, _) in gX]
    ns = np.array([n for (n, _, _) in gX], float)
    cs = np.array(sizes, float)
    slope = np.polyfit(np.log(ns[ns >= 4]), np.log(np.maximum(cs[ns >= 4], 1)), 1)[0]
    print(f'  {key[0]:7s} tau-shapes {list(key[1])} M-shapes {list(key[2])}: |supp a^n(X0)| n=1,2,4,8,16,32: '
          f'{[sizes[n - 1] for n in (1, 2, 4, 8, 16, 32) if n <= NMAX]}; front radius = n for all n: {sat}; '
          f'log-log slope {slope:.2f}')
check(f'light cone: n*max_v|v|_inf <= max(radius a^n(X0), radius a^n(Z0)) <= n for all reps, n<={NMAX}', ok_lb)
print(f'  representatives whose front radius saturates n at every step: {nsat}/{len(reps)}')
print(f'TOTAL: PASS={P} FAIL={F}')
