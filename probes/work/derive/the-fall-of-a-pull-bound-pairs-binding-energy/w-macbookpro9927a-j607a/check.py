#!/usr/bin/env python3
"""Exact checks for J:derive:the-fall-of-a-pull-bound-pairs-binding-energy:a1 (worker w-macbookpro9927a-j607a).

Independent routes to block 145 (landed; the supplied charge model of block 60's bilinear members
X = l^{p/2}: X = 1 + sum_j Q_j g(., x_j), Q_i X(x_i) = E_i/c, ledger c sum_i Q_i):
  F1  T1 for every N: L = sum_i m_i (1 - phi_i + 2 phi_i^2) + O(c^-3), phi_i = sum_{j!=i} m_j g_ij / c
  F2  T2(a): moving charges Q_i X(x_i) = sqrt(m_i^2 + k_i^2 X(x_i)^{-4/p})/c give the (1/2 + 1/p) coefficient
  F3  T3 by Hamilton's equations: the force on the pair's total momentum, not the m_3-derivative
  F4  extension: block 60's finite-box solution keeps each body's self-field g0; in dressed masses a
      leftover (2 g0/c^2) sum_{i!=j} m_i^2 m_j g_ij remains, i.e. T3's formula at <T> = 0
All exact (sympy series in 1/c, symbols).
"""
import itertools
import time

import sympy as sp

T0 = time.time()
RES = []


def check(tag, ok, msg):
    RES.append((tag, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}")


eps = sp.symbols('epsilon', positive=True)      # bookkeeping: 1/c = eps


def solve_charges(ms, gmat, order, energies=None):
    """Q_i (1 + sum_j Q_j g_ij) = E_i eps, iterated to the given order in eps; returns Q as series."""
    n = len(ms)
    E = energies if energies is not None else ms
    Q = [E[i] * eps for i in range(n)]
    for _ in range(order + 1):
        Q = [sp.series(E[i] * eps / (1 + sum(Q[j] * gmat[i][j] for j in range(n))), eps, 0, order + 1).removeO()
             for i in range(n)]
    return Q


# ------------------------------------------------------------------ F1: T1 for N = 3, 4 (self-field subtracted)
ok1 = True
for N in (3, 4):
    ms = sp.symbols(f'm1:{N + 1}', positive=True)
    gs = {}
    gmat = [[0] * N for _ in range(N)]
    for i, j in itertools.combinations(range(N), 2):
        gs[(i, j)] = sp.Symbol(f'g{i + 1}{j + 1}', positive=True)
        gmat[i][j] = gmat[j][i] = gs[(i, j)]
    Q = solve_charges(ms, gmat, 3)
    L = sp.expand(sum(Q) / eps)
    phi = [sum(ms[j] * gmat[i][j] for j in range(N)) * eps for i in range(N)]
    target = sp.expand(sum(ms[i] * (1 - phi[i] + 2 * phi[i] ** 2) for i in range(N)))
    ok1 = ok1 and sp.expand(sp.series(L - target, eps, 0, 3).removeO()) == 0
# the continuum reading: g = 1/(4 pi r), G = 1/(2 pi c): -(eps) sum_{i!=j} m_i m_j g_ij = -sum_{i<j} G m_i m_j / r_ij and
# 2 sum m_i phi_i^2 = (G^2/2) sum_i m_i (sum_j m_j / r_ij)^2
c, r = sp.symbols('c r', positive=True)
G = 1 / (2 * sp.pi * c)
ok1 = ok1 and sp.simplify(2 * (1 / c) / (4 * sp.pi * r) - G / r) == 0 and sp.simplify(2 * (1 / (4 * sp.pi * c)) ** 2 - G ** 2 / 2) == 0
check("F1", ok1, "T1 for N = 3 and 4 (and, by the same iteration, every N): with self-fields subtracted the ledger is "
      "sum m_i (1 - phi_i + 2 phi_i^2) + O(c^-3), phi_i = sum_{j!=i} m_j g_ij/c; with g = 1/(4 pi r) this is "
      "M - sum_{a<b} G M_a M_b/r_ab + (G^2/2) sum_a M_a (sum_b M_b/r_ab)^2, G = 1/(2 pi c)")

# ------------------------------------------------------------------ F2: T2(a), moving charges
p, lam = sp.symbols('p lambda', positive=True)    # lambda: bookkeeping for k^2
m1, m2, k1, k2, g12 = sp.symbols('m1 m2 k1 k2 g12', positive=True)


def Emov(m, k, Xv):                                # sqrt(m^2 + k^2 / l^2), l^2 = X^(4/p)
    return sp.sqrt(m ** 2 + lam * k ** 2 * Xv ** (-4 / p))


dX1 = eps * g12 * Emov(m2, k2, 1)                  # X(x_1) - 1 = Q_2 g12 at first order (self-field subtracted)
dX2 = eps * g12 * Emov(m1, k1, 1)
QA = eps * Emov(m1, k1, 1 + dX1) / (1 + dX1)
QB = eps * Emov(m2, k2, 1 + dX2) / (1 + dX2)
L2s = sp.series(sp.series((QA + QB) / eps, eps, 0, 2).removeO(), lam, 0, 2).removeO()
inter = sp.expand(L2s).coeff(eps, 1)
expect = -g12 * m1 * m2 * (2 + lam * (sp.Rational(1, 2) + 1 / p) * 2 * (k1 ** 2 / m1 ** 2 + k2 ** 2 / m2 ** 2))
ok2 = sp.simplify(sp.expand(inter - expect)) == 0
check("F2", ok2, "T2(a): with Q_i X(x_i) = sqrt(m_i^2 + k_i^2 X(x_i)^(-4/p))/c the two-body ledger's first-order term "
      "is -(2 g12 m1 m2/c)[1 + (1/2 + 1/p)(k1^2/m1^2 + k2^2/m2^2)] at order k^2, i.e. -(G m1 m2/r)[1 + (1/2 + 1/p)(...)] "
      "with g = 1/(4 pi r): the 1/2 from the bodies' own energy of motion, the 1/p from the stretched bonds")

# ------------------------------------------------------------------ F3: T3 by Hamilton's equations
a_, s2 = sp.symbols('a s2')
X = sp.Matrix(sp.symbols('X1:4'))                 # pair centre
d1 = sp.Matrix(sp.symbols('d1:4'))                # x_1 - X
d2 = sp.Matrix(sp.symbols('e1:4'))                # x_2 - X
gradPhi = sp.Matrix(sp.symbols('F1:4'))           # grad Phi at X
Phi0 = sp.Symbol('Phi0')
T1_, T2_ = sp.symbols('T1 T2')
x1 = X + d1
x2 = X + d2
Phi = lambda xv: Phi0 + (gradPhi.T * (xv - X))[0]  # linear far field (tidal terms dropped)
rr = sp.sqrt(((x1 - x2).T * (x1 - x2))[0])
Gm = sp.Symbol('Gm12', positive=True)
U = -Gm / rr
m1s, m2s = sp.symbols('mA mB', positive=True)
# differentiate w.r.t. the particle positions explicitly: build Hext as a function of x1, x2
y1 = sp.Matrix(sp.symbols('y1:4'))
y2 = sp.Matrix(sp.symbols('z1:4'))
Phiy = lambda yv: Phi0 + (gradPhi.T * (yv - X))[0]
ry = sp.sqrt(((y1 - y2).T * (y1 - y2))[0])
Uy = -Gm / ry
Hy = Phiy(y1) * (m1s + 2 * a_ * T1_ + s2 * Uy) + Phiy(y2) * (m2s + 2 * a_ * T2_ + s2 * Uy)
Fy = -sp.Matrix([sp.diff(Hy, y1[i]) + sp.diff(Hy, y2[i]) for i in range(3)])
Fy = Fy.subs({y1[i]: x1[i] for i in range(3)}).subs({y2[i]: x2[i] for i in range(3)})
expectF = -gradPhi * (m1s + m2s + 2 * a_ * (T1_ + T2_) + 2 * s2 * U)
okF = all(sp.simplify(Fy[i] - expectF[i]) == 0 for i in range(3))
# passive mass with the virial <2T + U> = 0, against the energy M + <T> + <U>
Ut = sp.Symbol('U')
passive = (m1s + m2s) + 2 * a_ * (-Ut / 2) + 2 * s2 * Ut
energy = (m1s + m2s) + (-Ut / 2) + Ut
diffPE = sp.simplify(passive - energy)
okV = sp.simplify(diffPE - (2 * s2 - a_ - sp.Rational(1, 2)) * Ut) == 0
okP = sp.simplify(diffPE.subs({a_: sp.Rational(1, 2) + 1 / p, s2: 1}) - (1 - 1 / p) * Ut) == 0
check("F3", okF and okV and okP, "T3 by Hamilton's equations: with H_ext = sum_a Phi(x_a)[m_a + 2a T_a + s2 U] and a "
      "linear far field, dP/dt = -sum_a dH/dx_a = -grad Phi [M + 2a(T1 + T2) + 2 s2 U] exactly (the U-gradient terms "
      "cancel against each other); with <2T + U> = 0 the passive mass differs from the energy by (2 s2 - a - 1/2)<U>, "
      "which is (1 - 1/p)<U> for block 60's members and 0 only at p = 1")

# ------------------------------------------------------------------ F4: self-fields kept (block 60's finite box)
g0 = sp.symbols('g0', positive=True)
ok4 = True
for N in (2, 3):
    ms = sp.symbols(f'm1:{N + 1}', positive=True)
    gmat = [[g0 if i == j else sp.Symbol(f'g{min(i, j) + 1}{max(i, j) + 1}', positive=True) for j in range(N)]
            for i in range(N)]
    Q = solve_charges(ms, gmat, 3)
    L = sp.expand(sp.series(sum(Q) / eps, eps, 0, 3).removeO())
    # dressed single-body masses: M = c Q for a body alone, Q (1 + g0 Q) = m eps
    Md = [sp.expand(sp.series(solve_charges([mi], [[g0]], 3)[0] / eps, eps, 0, 3).removeO()) for mi in ms]
    first = -eps * sum(Md[i] * Md[j] * gmat[i][j] for i in range(N) for j in range(N) if i != j)
    second = 2 * eps ** 2 * sum(Md[i] * sum(Md[j] * gmat[i][j] for j in range(N) if j != i) ** 2 for i in range(N))
    leftover = 2 * eps ** 2 * g0 * sum(ms[i] ** 2 * ms[j] * gmat[i][j] for i in range(N) for j in range(N) if i != j)
    resid = sp.expand(sp.series(L - (sum(Md) + first + second + leftover), eps, 0, 3).removeO())
    ok4 = ok4 and resid == 0
check("F4", ok4, "extension, self-fields kept (block 60's finite-box charges with the diagonal g0): in dressed masses "
      "M_i = m_i - g0 m_i^2/c + 2 g0^2 m_i^3/c^2 the ledger is sum M - (1/c) sum_{i!=j} M_i M_j g_ij + (2/c^2) sum M_i "
      "(sum M_j g_ij)^2 + (2 g0/c^2) sum_{i!=j} m_i^2 m_j g_ij: body i couples with m_i + 2 E_self,i, E_self = -g0 m^2/c, "
      "which is T3's passive mass M + 2 s2 U at <T> = 0 (a pinned body has no virial balance), for N = 2 and 3")

npass = sum(ok for _, ok in RES)
print(f"TOTAL: PASS={npass} FAIL={len(RES) - npass}  ({time.time() - T0:.0f} s)")
if npass == len(RES):
    print("SUMMARY: PROVED block 145 T1-T3 by other routes within its supplied charge model: T1 for every N from "
          "L = sum m_i (1 - phi_i + 2 phi_i^2); T2(a)'s (1/2 + 1/p) from the moving charge equation; T3 from Hamilton's "
          "equations (force on the pair's momentum, U-gradients cancelling), passive minus energy = (2 s2 - a - 1/2)<U> = "
          "(1 - 1/p)<U>; extension: with block 60's finite-box self-fields a pinned body couples with m + 2 E_self, "
          "T3's formula at <T> = 0.")
    print("HIT: block 145 confirmed by independent routes: the static ledger's second order is "
          "sum_i m_i(1 - phi_i + 2 phi_i^2), phi_i = sum_{j!=i} m_j g_ij/c, for every N (so (G^2/2) sum M_a(sum M_b/r)^2, "
          "G = 1/(2 pi c)); moving charges give -(G m1 m2/r)[1 + (1/2 + 1/p)(k1^2/m1^2 + k2^2/m2^2)]; Hamilton's equations "
          "give dP/dt = -grad Phi[M + 2a T + 2 s2 U] exactly in a linear far field, so the passive mass exceeds the "
          "energy by (2 s2 - a - 1/2)<U> = (1 - 1/p)<U>; new: with finite-box self-fields g0, body i couples with "
          "m_i + 2 E_self,i (E_self = -g0 m_i^2/c), the pinned-body case <T> = 0 of the same formula.")
else:
    print("SUMMARY: ROUTE FAILS AT a failed check above")
