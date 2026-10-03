#!/usr/bin/env python3
"""A18: post-Newtonian bookkeeping for the candidate package P1-P4 (supplied toy, nothing adopted).

Eikonal Hamiltonian of a species with one-site rest energy (pace N) and two-site motion (pace w):
    H(x,p) = A(r) * sqrt(m^2 + p^2 / B(r)^2)
  AND/product rule: A = N, B = 1/N   (metric -N^2 dt^2 + N^-2 dx^2)
  OR/mean rule    : A = N, B = 1     (metric -N^2 dt^2 + dx^2)
  GR comparator (isotropic Schwarzschild): A = (1-U/2)/(1+U/2), B = (1+U/2)^2
Lapse forms: exp N = e^{-U};  lin N = 1 - U  (A6/A8 event-rate lapse).  U = M/r, M = 1.

(a) light deflection to 2nd order: fit alpha(M/b) and compare with alpha1 = 2 a1, alpha2 = pi (a2 + a1^2/2)
(b) perihelion advance per orbit / (6 pi M/p) -> (2 + 2 gamma - beta)/3
(c) circular-orbit periastron K(x), x = (M Omega)^(2/3), series to 2PN (sympy)
(d) photon sphere / shadow impact parameter; (e) Einstein tensor of the exp-AND metric (sympy)
"""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(58)
import mpmath as mp
import numpy as np
import sympy as sp

import sys
PARTS = sys.argv[1] if len(sys.argv) > 1 else "abcde"
mp.mp.dps = 30
PI = mp.pi

MODELS = {
    # name: (A(U), B(U))
    "GR-iso":  (lambda U: (1 - U / 2) / (1 + U / 2), lambda U: (1 + U / 2) ** 2),
    "exp-AND": (lambda U: mp.e ** (-U),              lambda U: mp.e ** (U)),
    "lin-AND": (lambda U: 1 - U,                     lambda U: 1 / (1 - U)),
    "exp-OR":  (lambda U: mp.e ** (-U),              lambda U: mp.mpf(1)),
    "lin-OR":  (lambda U: 1 - U,                     lambda U: mp.mpf(1)),
}
# predictions: index n = B/A = 1 + a1 U + a2 U^2
PRED_LIGHT = {"GR-iso": (4, 15 * PI / 4), "exp-AND": (4, 4 * PI), "lin-AND": (4, 5 * PI),
              "exp-OR": (2, PI), "lin-OR": (2, 3 * PI / 2)}
PRED_PERI = {"GR-iso": 1, "exp-AND": 1, "lin-AND": mp.mpf(7) / 6, "exp-OR": mp.mpf(1) / 3, "lin-OR": mp.mpf(1) / 2}


def deflection(name, r0):
    A, B = MODELS[name]
    n = lambda r: B(1 / r) / A(1 / r)
    n0 = n(r0)
    f = lambda chi: n0 * mp.cos(chi) / mp.sqrt(n(r0 / mp.sin(chi)) ** 2 - (n0 * mp.sin(chi)) ** 2)
    alpha = 2 * mp.quad(f, [0, PI / 4, PI / 2], method="gauss-legendre") - PI
    return alpha, n0 * r0          # deflection, impact parameter b


def perihelion(name, p, e):
    A, B = MODELS[name]
    u1, u2 = (1 + e) / p, (1 - e) / p
    # P(u) = B^2 (E^2/A^2 - 1) - L^2 u^2 = 0 at u1, u2 : linear in (E^2, L^2)
    M = mp.matrix([[B(u1) ** 2 / A(u1) ** 2, -u1 ** 2], [B(u2) ** 2 / A(u2) ** 2, -u2 ** 2]])
    rhs = mp.matrix([B(u1) ** 2, B(u2) ** 2])
    E2, L2 = mp.lu_solve(M, rhs)
    L = mp.sqrt(L2)
    mid, half = (u1 + u2) / 2, (u1 - u2) / 2
    P = lambda u: B(u) ** 2 * (E2 / A(u) ** 2 - 1) - L2 * u ** 2
    g = lambda chi: L * half * mp.sin(chi) / mp.sqrt(P(mid - half * mp.cos(chi)))
    return 2 * mp.quad(g, [0, PI / 2, PI], method="gauss-legendre") - 2 * PI


def part_a():
    print("(a) light deflection alpha = A1 (M/b) + A2 (M/b)^2 + ...  [fit on M/r0 = 1e-3 .. 8e-3]")
    for name in MODELS:
        xs, al = [], []
        for s in (1, 2, 3, 4, 6, 8):
            a, b = deflection(name, mp.mpf(1000) / s)
            xs.append(1 / b); al.append(a)
        # least squares in mp for alpha = sum_k c_k x^k, k = 1..5
        X = mp.matrix([[x ** k for k in range(1, 6)] for x in xs])
        c = mp.lu_solve(X.T * X, X.T * mp.matrix(al))
        p1, p2 = PRED_LIGHT[name]
        print("  %-8s A1 = %.8f (pred %s)   A2/pi = %.6f (pred %.6f)" %
              (name, float(c[0]), p1, float(c[1] / PI), float(p2 / PI)))


def part_b():
    print("(b) perihelion advance per orbit / (6 pi M/p), e = 0.2; extrapolated to M/p -> 0")
    for name in MODELS:
        xs, rs = [], []
        for q in (1e-4, 2e-4, 4e-4):
            p = mp.mpf(1) / mp.mpf(q)
            d = perihelion(name, p, mp.mpf("0.2"))
            xs.append(q); rs.append(d / (6 * PI / p))
        slope = (rs[1] - rs[0]) / (xs[1] - xs[0])
        r0 = rs[0] - slope * xs[0]
        print("  %-8s ratio at M/p=1e-4: %.6f   extrapolated: %.6f   pred (2+2g-b)/3 = %.6f" %
              (name, float(rs[0]), float(r0), float(PRED_PERI[name])))


def part_c():
    print("(c) circular orbits: periastron ratio K = Omega_phi/Omega_r as series in x = (M Omega)^(2/3)")
    U, L2, xx = sp.symbols("U L2 x", positive=True)
    def K_series(Afun, Bfun, order=4):
        r = 1 / U
        A, B = Afun(U), Bfun(U)
        rr = sp.symbols("rr", positive=True)
        Ar, Br = Afun(1 / rr), Bfun(1 / rr)
        S2 = 1 + L2 / (rr ** 2 * Br ** 2)
        V2 = Ar ** 2 * S2                              # V^2 = H^2 at p_r = 0
        L2sol = sp.solve(sp.Eq(sp.diff(V2, rr), 0), L2)[0]
        V = sp.sqrt(V2)
        Vpp = sp.diff(V, rr, 2)
        Hpp = Ar / (Br ** 2 * sp.sqrt(S2))             # d^2H/dp_r^2 at p_r = 0
        Om = Ar * sp.sqrt(L2) / (rr ** 2 * Br ** 2 * sp.sqrt(S2))   # dH/dL
        K2 = (Om ** 2 / (Vpp * Hpp)).subs(L2, L2sol)
        Omc = Om.subs(L2, L2sol)
        K2U = sp.series(sp.simplify(K2.subs(rr, 1 / U)), U, 0, order).removeO()
        xU = sp.series(sp.simplify((Omc ** 2).subs(rr, 1 / U)) ** sp.Rational(1, 3), U, 0, order).removeO()
        # invert x(U)
        Us = sp.symbols("Us")
        a = [sp.Symbol("a%d" % i) for i in range(1, order)]
        Uin = sum(a[i] * xx ** (i + 1) for i in range(order - 1))
        eqs = sp.Poly(sp.series(xU.subs(U, Uin) - xx, xx, 0, order).removeO(), xx).all_coeffs()[::-1]
        sol = sp.solve(eqs[1:order], a, dict=True)[0]
        KUx = sp.series(sp.sqrt(K2U).subs(U, Uin.subs(sol)), xx, 0, order).removeO()
        return sp.expand(KUx)
    for name, Af, Bf in (("GR-iso", lambda u: (1 - u / 2) / (1 + u / 2), lambda u: (1 + u / 2) ** 2),
                         ("exp-AND", lambda u: sp.exp(-u), lambda u: sp.exp(u)),
                         ("lin-AND", lambda u: 1 - u, lambda u: 1 / (1 - u))):
        print("  %-8s K(x) = %s" % (name, K_series(Af, Bf)))


def part_d():
    print("(d) photon sphere and shadow (critical impact parameter b_c = min_r n(r) r), M = 1")
    for name in ("GR-iso", "exp-AND", "lin-AND"):
        A, B = MODELS[name]
        h = lambda r: B(1 / r) / A(1 / r) * r
        rmin = mp.findroot(lambda r: mp.diff(h, r), 2.2 if name != "GR-iso" else 1.9)
        print("  %-8s photon sphere at isotropic r = %.6f (U = %.6f, N = A = %.6f); b_c = %.6f" %
              (name, float(rmin), float(1 / rmin), float(A(1 / rmin)), float(h(rmin))))
    print("  3*sqrt(3) = %.6f ; 2e = %.6f" % (3 * np.sqrt(3), 2 * np.e))


def part_e():
    print("(e) Einstein tensor of ds^2 = -e^{-2U} dt^2 + e^{2U}(dr^2 + r^2 dOmega^2), U = M/r")
    t, r, th, ph, Mm = sp.symbols("t r theta phi M", positive=True)
    Uf = Mm / r
    g = sp.diag(-sp.exp(-2 * Uf), sp.exp(2 * Uf), sp.exp(2 * Uf) * r ** 2, sp.exp(2 * Uf) * r ** 2 * sp.sin(th) ** 2)
    co = (t, r, th, ph)
    gi = g.inv()
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], co[c]) + sp.diff(g[d, c], co[b]) - sp.diff(g[b, c], co[d])) for d in range(4)) / 2
             for c in range(4)] for b in range(4)] for a in range(4)]
    def Ric(b, c):
        return sp.simplify(sum(sp.diff(Gam[a][b][c], co[a]) - sp.diff(Gam[a][b][a], co[c]) +
                               sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(4))
                               for a in range(4)))
    R = sp.Matrix(4, 4, lambda b, c: Ric(b, c))
    Rs = sp.simplify(sum(gi[a, b] * R[a, b] for a in range(4) for b in range(4)))
    G = sp.simplify(R - g * Rs / 2)
    Gmix = sp.simplify(gi * G)
    gradU2 = sp.simplify(sp.exp(-2 * Uf) * sp.diff(Uf, r) ** 2)   # g^rr (dU/dr)^2
    print("  G^t_t = %s ;  G^r_r = %s ;  G^th_th = %s" % (sp.simplify(Gmix[0, 0] / gradU2),
          sp.simplify(Gmix[1, 1] / gradU2), sp.simplify(Gmix[2, 2] / gradU2)), "  (in units of g^rr (dU/dr)^2)")


for _p in PARTS:
    globals()["part_" + _p]()
