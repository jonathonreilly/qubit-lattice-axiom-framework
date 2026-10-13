#!/usr/bin/env python3
"""R19-6 [V]: the same functional A'[h] = -<[sqrt(-g) G^{mu nu}]^(2)[h,h]>/8 pi on the graviton vacuum, with the same code
(r196_lib.py) that gives set A's a = 2 noise source (r196_setA.py).  Independent of R19-3's runners.

One on-shell mode k_mu = (-1, 0, 0, 1) (theta = z - t), h = A cos(theta) + B sin(theta), stationary Gaussian ensemble
<A A> = <B B> = Cov, <A B> = 0.  Per-mode coefficient c defined by t^{mu nu} = c * (TT value).  Covariances (lower):
  TT : (P_ac P_bd + P_ad P_bc - P_ab P_cd)/2,  P = diag(0,1,1,0)
  FdD: (eta_ac eta_bd + eta_ad eta_bc - eta_ab eta_cd)/2  (Feynman-de Donder, same normalization; R19-3 / its referee)
Weights w = 0, 1, 2 of the contravariant density (-g)^{w/2} G^{mu nu}, and the lower-index G_mu nu (R19-3's (B)).
Expected (R19-3, refereed): (B) 4, LL = w=2 form 2, A' = w=1 form 1 in FdD; all 1 in TT.
Subtraction: none.
"""
import sympy as sp, time, sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r196_lib import C, S, eps, eta, N, make_D, avg, einstein_lower, einstein_upper_density, order

t0 = time.time()
D = make_D(sp.Integer(1), sp.Integer(1))
pairs = [(m, n) for m in range(4) for n in range(m, 4)]
asym = {p: sp.Symbol('a%d%d' % p) for p in pairs}
A = sp.zeros(4, 4)
for (m, n), s in asym.items():
    A[m, n] = A[n, m] = s
h = A * C
G, gi = einstein_lower(h, D)
forms = {}
for wv in (0, 1, 2):
    Y = einstein_upper_density(G, gi, h, wv)
    forms['w=%d upper' % wv] = Y.applyfunc(lambda e: -avg(order(e, 2)) / (8 * sp.pi))
forms['G_mu nu lower (B)'] = G.applyfunc(lambda e: -avg(order(e, 2)) / (8 * sp.pi))
print("[V0] O(s^2) forms built [%.1fs]" % (time.time() - t0))

P = sp.diag(0, 1, 1, 0)


def cov(M):
    return lambda a_, b_, c_, d_: (M[a_, c_] * M[b_, d_] + M[a_, d_] * M[b_, c_] - M[a_, b_] * M[c_, d_]) / 2


covs = {'TT': cov(P), 'FdD': cov(eta)}


def contract(expr, cv):
    e = sp.expand(expr)
    if e == 0:
        return sp.Integer(0)
    poly = sp.Poly(e, *[asym[p] for p in pairs])
    out = 0
    for mon, cf in poly.terms():
        idx = [i for i, m in enumerate(mon) for _ in range(m)]
        (p1, p2) = (pairs[idx[0]], pairs[idx[1]])
        out += cf * cv(p1[0], p1[1], p2[0], p2[1])
    return sp.simplify(out)


kk = sp.Matrix([1, 0, 0, 1])     # k^mu (upper) for k_mu = (-1,0,0,1)
ref = None
for lab, M in forms.items():
    for cl, cv in covs.items():
        T = M.applyfunc(lambda e: contract(e, cv))
        if lab.startswith('G_mu'):
            T = eta * T * eta        # raise for comparison with k^mu k^nu
        if ref is None and cl == 'TT':
            ref = T[0, 0]
        c = sp.simplify(T[0, 0] / ref)
        pure = all(sp.simplify(T[m, n] - c * ref * kk[m] * kk[n]) == 0 for m in range(4) for n in range(4))
        print("     %-18s %-4s: c = %-4s [t^{mu nu} = c * k^mu k^nu * const: %s]" % (lab, cl, c, pure))
print("\n[V1] reading: the weight-1 functional A' gives the TT zero point (c = 1) on the FdD vacuum as on TT; the w-family")
print("     is linear in w (c = 1 + (w-1) * Delta) because the weight enters only through (w/2)<tr h G^(1)[h]>.")
print("total time %.1fs" % (time.time() - t0))
