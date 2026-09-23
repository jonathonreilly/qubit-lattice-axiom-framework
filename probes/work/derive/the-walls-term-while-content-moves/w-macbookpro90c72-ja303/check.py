#!/usr/bin/env python3
"""J:derive:the-walls-term-while-content-moves:a1 - checks for ATTEMPT.md (same directory).

Block 60's walled box: interior I of a cubic box of Z^3, wall sites W (the interior's outer neighbours) held at
w = l = 1; rates w = phi^2 = e^u, lengths l = chi^2 = e^lam, N = w chi; the curvature member in bond form
F = -8K sum_{bonds with an interior end} (N_y - N_x)(chi_y - chi_x); content <H> of weight one; the lengths' kinetic
term K_lam = sum_I c_k l^s lamdot^2 / w; L = K_lam - <H> - F; walls' term Wt = sum_{x in W} d(<H> + F)/du_x.
E1-E3 exact (sympy rationals / Gaussian rationals / Fractions); S1 high precision (mpmath, 80 digits, error stated);
B1-B2 floating point, evidence only.
"""
import sys
from fractions import Fraction as Fr
from itertools import product
import random

import mpmath as mp
import numpy as np
import sympy as sp

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def add(a, d):
    return (a[0] + d[0], a[1] + d[1], a[2] + d[2])


def box(n):
    """interior 1..n per axis; walls = outer neighbours of the interior; bonds with an interior end."""
    I = [p for p in product(range(1, n + 1), repeat=3)]
    Iset = set(I)
    W = sorted({add(p, d) for p in I for d in DIRS} - Iset)
    B = sorted({tuple(sorted((p, add(p, d)))) for p in I for d in DIRS})
    nb = {p: [] for p in I + W}
    for a, b in B:
        nb[a].append(b)
        nb[b].append(a)
    return I, W, B, nb


def lap(f, nb, sites):
    return {x: sum(f[y] - f[x] for y in nb[x]) for x in sites}


# ---------------------------------------------------------------- E1: identities on the 2^3 box (exact, off shell)
I2, W2, B2, NB2 = box(2)
S2 = I2 + W2
K = sp.Rational(1, 2)
CK, SPOW = -6 * K, 3
rng = random.Random(20260923)
phi = {x: sp.Symbol("p_%d%d%d" % x, positive=True) for x in S2}
chi = {x: sp.Symbol("c_%d%d%d" % x, positive=True) for x in S2}
ld = {x: sp.Symbol("l_%d%d%d" % x) for x in I2}
Nf = {x: phi[x] ** 2 * chi[x] for x in S2}
F = -8 * K * sum((Nf[b] - Nf[a]) * (chi[b] - chi[a]) for a, b in B2)
Klam = sum(CK * chi[x] ** (2 * SPOW) * ld[x] ** 2 / phi[x] ** 2 for x in I2)
rho = {x: sp.Rational(rng.randint(1, 9), rng.randint(1, 5)) for x in I2}
Hrest = sum(phi[x] ** 2 * rho[x] for x in I2)
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def hblock(x, y):
    """block 54's walk H = sum_j sigma_j S_j, S_j = (T_j - T_j^dag)/(2i), (T_j psi)(x) = psi(x - e_j)."""
    for j in range(3):
        e = tuple(int(k == j) for k in range(3))
        if y == tuple(a - b for a, b in zip(x, e)):
            return SIG[j] / (2 * sp.I)
        if y == add(x, e):
            return -SIG[j] / (2 * sp.I)
    return None


psi = {x: sp.Matrix([sp.Rational(rng.randint(-4, 4), 3) + sp.I * sp.Rational(rng.randint(-4, 4), 5) for _ in range(2)])
       for x in I2}
cxy = {}
for x in I2:
    for y in I2:
        h = hblock(x, y)
        if h is not None:
            cxy[(x, y)] = sp.expand((psi[x].H * h * psi[y])[0])
Hwalk = sum(phi[x] * phi[y] / (chi[x] * chi[y]) * c for (x, y), c in cxy.items())
point = {}
for x in S2:
    point[phi[x]] = 1 if x in W2 else sp.Rational(rng.randint(5, 15), 10)
    point[chi[x]] = 1 if x in W2 else sp.Rational(rng.randint(8, 20), 10)
for x in I2:
    point[ld[x]] = sp.Rational(rng.randint(-9, 9), 7)


def at(expr):
    return sp.expand(expr.subs(point))


def du(expr, x):  # d/du_x = (phi_x / 2) d/dphi_x
    return phi[x] / 2 * sp.diff(expr, phi[x])


def dlam(expr, x):  # d/dlam_x = (chi_x / 2) d/dchi_x
    return chi[x] / 2 * sp.diff(expr, chi[x])


wv = {x: point[phi[x]] ** 2 for x in S2}
cv = {x: point[chi[x]] for x in S2}
Nv = {x: wv[x] * cv[x] for x in S2}
Lc, LN = lap(cv, NB2, S2), lap(Nv, NB2, S2)
g1 = all(at(du(F, x)) == 8 * K * Nv[x] * Lc[x] for x in S2)
g2 = all(at(sp.diff(F, chi[x])) == 8 * K * (wv[x] * Lc[x] + LN[x]) for x in I2)
Aeff = {x: point[phi[x]] / point[chi[x]] for x in I2}
Hpsi = {x: sum((Aeff[x] * Aeff[y] * hblock(x, y) * psi[y] for y in I2 if hblock(x, y) is not None), sp.zeros(2, 1))
        for x in I2}
ev = {x: sp.re(sp.expand((psi[x].H * Hpsi[x])[0])) for x in I2}
g3 = all(at(du(Hwalk, x)) == ev[x] and at(dlam(Hwalk, x)) == -ev[x] for x in I2) and sum(ev.values()) == at(Hwalk)
g4 = sum(Lc.values()) == 0
walls_def = {nm: at(sum(du(Hc + F, x) for x in W2)) for nm, Hc in (("rest", Hrest), ("walker", Hwalk))}
walls_flux = 8 * K * sum(Lc[x] for x in W2)
g5 = all(v == walls_flux for v in walls_def.values())
gap = []
for Hc in (Hrest, Hwalk):
    L = Klam - Hc - F
    h = Klam + Hc + F  # energy function: K_lam is quadratic in the rates of change, the walker's term linear (adds 0)
    gap.append(at(h - walls_flux + sum(du(L, x) for x in I2)))
ok("E1", g1 and g2 and g3 and g4 and g5 and gap == [0, 0],
   "2^3 box, rational point, walls at 1, exact: dF/du_x = 8K N_x (Lap chi)_x at all 32 sites; dF/dchi_z = "
   "8K[w_z (Lap chi)_z + (Lap N)_z]; walker d<H>/du_z = e_z = Re psi^dag (A H A psi)_z = -d<H>/dlam_z, sum e = <H>; "
   "walls' term = 8K (flux of chi into the walls) for both contents; h - Wt = -sum_I dL/du_x for rest and walker content")

# ---------------------------------------------------------------- E2: the energy function's rate along any path (exact)
t = sp.Symbol("t")
cd = {x: sp.Symbol("d_%d%d%d" % x) for x in I2}
rt = {x: rho[x] + sp.Rational(rng.randint(-5, 5), 4) * t for x in I2}
Lt = (sum(CK * chi[x] ** (2 * SPOW) * (2 * cd[x] / chi[x]) ** 2 / phi[x] ** 2 for x in I2)
      - sum(phi[x] ** 2 * rt[x] for x in I2) - F)
path = {}
for x in I2:
    path[chi[x]] = 1 + sp.Rational(rng.randint(-3, 3), 10) * t + sp.Rational(rng.randint(-3, 3), 10) * t ** 2
    path[phi[x]] = 1 + sp.Rational(rng.randint(-3, 3), 10) * t + sp.Rational(rng.randint(-3, 3), 10) * t ** 2
for x in W2:
    path[chi[x]] = sp.Integer(1)
    path[phi[x]] = sp.Integer(1)
for x in I2:
    path[cd[x]] = sp.diff(path[chi[x]], t)
hfun = sum(cd[x] * sp.diff(Lt, cd[x]) for x in I2) - Lt
E2ok = True
for t0 in (sp.Rational(1, 3), sp.Rational(3, 4)):
    lhs = sp.diff(hfun.subs(path), t).subs(t, t0)
    rhs = 0
    for x in I2:
        pL = sp.diff(Lt, cd[x]).subs(path)
        Ex = sp.diff(pL, t) - sp.diff(Lt, chi[x]).subs(path)
        rhs += (path[cd[x]] * Ex - sp.diff(path[phi[x]], t) * sp.diff(Lt, phi[x]).subs(path)).subs(t, t0)
    rhs += -sp.diff(Lt, t).subs(path).subs(t, t0)
    E2ok &= sp.simplify(lhs - rhs) == 0
dLdt = sp.simplify(-sp.diff(Lt, t) - sum(phi[x] ** 2 * sp.diff(rt[x], t) for x in I2))
ok("E2", E2ok and dLdt == 0,
   "2^3 box, polynomial paths of chi, phi and a supplied rho(t), exact at t = 1/3, 3/4: dh/dt = sum_I chidot E_chi "
   "- sum_I phidot dL/dphi - dL/dt with -dL/dt = sum_x w_x drho_x/dt; on solutions dh/dt = sum w rhodot")

# ---------------------------------------------------------------- E3: second order in the source, 3^3 interior (exact)
I3, W3, B3, NB3 = box(3)
KF = Fr(1, 2)
CKF = -6 * KF
n3 = len(I3)
idx = {x: i for i, x in enumerate(I3)}


def inv_exact(M):
    n = len(M)
    A = [row[:] + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [v / pv for v in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    return [row[n:] for row in A]


mlap = [[Fr(0)] * n3 for _ in range(n3)]
for x in I3:
    mlap[idx[x]][idx[x]] = Fr(6)
    for y in NB3[x]:
        if y in idx:
            mlap[idx[x]][idx[y]] -= 1
G = inv_exact(mlap)  # g = (-Lap)^-1, zero walls


def P(*c):  # polynomial in t, coefficients low to high
    return [Fr(v) for v in c]


def padd(p, q):
    m = max(len(p), len(q))
    return [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(m)]


def pmul(p, q):
    r = [Fr(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r


def psc(p, c):
    return [c * v for v in p]


def pder(p):
    return [i * p[i] for i in range(1, len(p))] or [Fr(0)]


def pval(p, t0):
    return sum(c * t0 ** i for i, c in enumerate(p))


def pz(p):
    return all(v == 0 for v in p)


def gapply(vec):  # g applied to a vector of polynomials
    out = []
    for i in range(n3):
        acc = [Fr(0)]
        for j in range(n3):
            if G[i][j] and not pz(vec[j]):
                acc = padd(acc, psc(vec[j], G[i][j]))
        out.append(acc)
    return out


class Ser:
    """truncated series in the source strength eps, orders 0..2, coefficients polynomials in the label t."""

    def __init__(self, c):
        self.c = [c[k] if k < len(c) else [Fr(0)] for k in range(3)]

    def __add__(s, o):
        return Ser([padd(a, b) for a, b in zip(s.c, o.c)])

    def __mul__(s, o):
        return Ser([padd(padd(pmul(s.c[0], o.c[k]) if k >= 0 else [Fr(0)], pmul(s.c[1], o.c[k - 1]) if k >= 1 else [Fr(0)]),
                         pmul(s.c[2], o.c[k - 2]) if k >= 2 else [Fr(0)]) for k in range(3)])

    def sc(s, v):
        return Ser([psc(a, v) for a in s.c])

    def inv(s):  # 1/(1 + a1 eps + a2 eps^2)
        assert s.c[0] == [Fr(1)] or pz(padd(s.c[0], [Fr(-1)]))
        a1, a2 = s.c[1], s.c[2]
        return Ser([[Fr(1)], psc(a1, -1), padd(pmul(a1, a1), psc(a2, -1))])

    def pw(s, k):
        r = Ser([[Fr(1)]])
        for _ in range(k):
            r = r * s
        return r

    def dt(s):
        return Ser([pder(a) for a in s.c])


def second_order(rhohat):
    """perturbation theory of the walled box with supplied rest content rho = eps rhohat(t)."""
    chi1 = [psc(v, 1 / (8 * KF)) for v in gapply(rhohat)]  # order eps constraint: rhohat + 8K Lap chi1 = 0
    chi = {x: Ser([[Fr(1)], chi1[idx[x]]]) if x in idx else Ser([[Fr(1)]]) for x in I3 + W3}

    def lapS(f, x):
        acc = Ser([[Fr(0)]])
        for y in NB3[x]:
            acc = acc + f[y] + f[x].sc(-1)
        return acc
    # lengths' equation at order eps with w1 = 0; w1 then enters as 8K Lap w1
    Eo = []
    for x in I3:
        c_, cdot = chi[x], chi[x].dt()
        pl = (c_.pw(2 * SPOW - 2) * cdot).sc(8 * CKF)  # dL/dchidot at w = 1
        dF = (lapS(chi, x) + lapS(chi, x)).sc(8 * KF)  # dF/dchi = 8K[w Lap chi + Lap N], at w = 1 (w1 added below)
        e_ = pl.dt() + dF + (c_.pw(2 * SPOW - 3) * cdot * cdot).sc(-4 * CKF * (2 * SPOW - 2))
        Eo.append(e_.c[1])
    w1 = [psc(v, 1 / (8 * KF)) for v in gapply(Eo)]  # E1 + 8K Lap w1 = 0  =>  w1 = g E1 / (8K)
    wS = {x: Ser([[Fr(1)], w1[idx[x]]]) if x in idx else Ser([[Fr(1)]]) for x in I3 + W3}
    C1, C2 = [], []
    for x in I3:
        c_ = chi[x]
        lamdot = (c_.dt() * c_.inv()).sc(2)
        kin = (c_.pw(2 * SPOW) * lamdot * lamdot * wS[x].inv()).sc(CKF)
        cont = wS[x] * Ser([[Fr(0)], rhohat[idx[x]]])
        fld = (wS[x] * c_ * lapS(chi, x)).sc(8 * KF)
        tot = kin + cont + fld
        C1.append(tot.c[1])
        C2.append(tot.c[2])
    flux1 = [Fr(0)]
    for x in W3:  # order-eps flux of chi into the walls, 8K sum over wall bonds chi1_int
        for y in NB3[x]:
            flux1 = padd(flux1, psc(chi1[idx[y]], 8 * KF))
    tot1 = [Fr(0)]
    for v in rhohat:
        tot1 = padd(tot1, v)
    W2p = [Fr(0)]
    for v in C2:  # Wt at order eps^2 = -8K sum_I Lap chi2 = sum_I C2|_(chi2 = 0)
        W2p = padd(W2p, v)
    rate = [Fr(0)]
    for i in range(n3):
        rate = padd(rate, pmul(w1[i], pder(rhohat[i])))
    grho = gapply(rhohat)
    rgr = [Fr(0)]
    kin2 = [Fr(0)]
    for i in range(n3):
        rgr = padd(rgr, pmul(rhohat[i], grho[i]))
        ld1 = psc(pder(chi1[i]), 2)
        kin2 = padd(kin2, pmul(ld1, ld1))
    closed = padd(psc(rgr, -1 / (8 * KF)), psc(kin2, CKF))
    return C1, W2p, rate, closed, rgr, pz(padd(flux1, psc(tot1, -1)))


S = P(0, 0, 3, -2)  # smooth step 3t^2 - 2t^3: rest at both ends
cen, off = (2, 2, 2), (2, 2, 1)
rh1 = [[Fr(0)] for _ in range(n3)]
rh1[idx[cen]] = padd(P(1), psc(S, -1))
rh1[idx[off]] = S
A_, B0, B1 = (1, 2, 2), (3, 2, 2), (2, 2, 2)
rh2 = [[Fr(0)] for _ in range(n3)]
rh2[idx[A_]] = P(1)
rh2[idx[B0]] = padd(P(1), psc(S, -1))
rh2[idx[B1]] = S
res = []
for rh in (rh1, rh2):
    C1, W2p, rate, closed, rgr, gauss = second_order(rh)
    res.append((all(pz(v) for v in C1) and gauss, pz(padd(pder(W2p), psc(rate, -1))), pz(padd(W2p, psc(closed, -1))),
                pval(W2p, 1) - pval(W2p, 0), pval(W2p, Fr(1, 2)) - pval(closed, Fr(1, 2)), rgr))
gcc, goo = G[idx[cen]][idx[cen]], G[idx[off]][idx[off]]
d1, d2 = res[0][3], res[1][3]
ok("E3", all(r[0] and r[1] and r[2] for r in res) and d1 == -(goo - gcc) / (8 * KF) and d1 > 0 and d2 < 0,
   f"3^3 interior, K = 1/2, c_k = -6K, exact series in the source: Wt = sum rho - (1/8K) rho.g rho + c_k sum lamdot1^2 "
   f"(lam1 = g rho/4K) and dWt/dt = sum w1 rhodot at every t, for a body carried centre -> face-adjacent site "
   f"(g_cc = {gcc}, g_oo = {goo}: Wt rises by {d1} = (g_cc - g_oo)/8K) and for a body carried towards a fixed one "
   f"(Wt falls by {-d2}); first order in velocity -(1/4K) rhodot.g rho")

# ---------------------------------------------------------------- S1: strong field, static law, exact solution (T4)
mp.mp.dps = 80
Gm = mp.matrix(n3, n3)
for i in range(n3):
    for j in range(n3):
        Gm[i, j] = mp.mpf(G[i][j].numerator) / G[i][j].denominator
Km = mp.mpf(1) / 2
m_tot = 8 * Km * 20  # mu_total = m/(8K) = 20: chi at the body about 3


def strong(sv):
    xi, yi = idx[cen], idx[off]
    mu = [m_tot * (1 - sv) / (8 * Km), m_tot * sv / (8 * Km)]
    gxx, gxy, gyy = Gm[xi, xi], Gm[xi, yi], Gm[yi, yi]
    f = lambda q1, q2: [q1 * (1 + q1 * gxx + q2 * gxy) - mu[0], q2 * (1 + q1 * gxy + q2 * gyy) - mu[1]]
    q = mp.findroot(f, (mp.mpf(5), mp.mpf(3)))
    Q = [q[0], q[1]]
    chiI = [1 + Q[0] * Gm[i, xi] + Q[1] * Gm[i, yi] for i in range(n3)]
    cx, cy = chiI[xi], chiI[yi]
    M = mp.matrix([[cx + Q[0] * gxx, Q[0] * gxy], [Q[1] * gxy, cy + Q[1] * gyy]])
    Pv = mp.lu_solve(M, mp.matrix([Q[0], Q[1]]))
    NI = [1 - Pv[0] * Gm[i, xi] - Pv[1] * Gm[i, yi] for i in range(n3)]
    chiF = {x: (chiI[idx[x]] if x in idx else mp.mpf(1)) for x in I3 + W3}
    NF = {x: (NI[idx[x]] if x in idx else mp.mpf(1)) for x in I3 + W3}
    wF = {x: NF[x] / chiF[x] for x in chiF}
    rhoF = {x: mp.mpf(0) for x in I3}
    rhoF[cen], rhoF[off] = m_tot * (1 - sv), m_tot * sv
    Lc_, LN_ = lap(chiF, NB3, I3 + W3), lap(NF, NB3, I3 + W3)
    r1 = max(abs(wF[x] * rhoF[x] + 8 * Km * NF[x] * Lc_[x]) for x in I3)
    r2 = max(abs(wF[x] * Lc_[x] + LN_[x]) for x in I3)
    Fb = -8 * Km * sum((NF[b] - NF[a]) * (chiF[b] - chiF[a]) for a, b in B3)
    ledger = sum(wF[x] * rhoF[x] for x in I3) + Fb
    flux = 8 * Km * sum(Lc_[x] for x in W3)
    return flux, ledger, 8 * Km * (Q[0] + Q[1]), wF, max(r1, r2), chiF


s0, dl = mp.mpf(3) / 10, mp.mpf(10) ** -25
fl, led, qs, wF, resid, chiF = strong(s0)
dW = (strong(s0 + dl)[0] - strong(s0 - dl)[0]) / (2 * dl)
work = m_tot * (wF[off] - wF[cen])
ok("S1", resid < mp.mpf(10) ** -50 and abs(fl - led) < mp.mpf(10) ** -50 and abs(fl - qs) < mp.mpf(10) ** -50
   and abs(dW - work) < mp.mpf(10) ** -40,
   f"strong field (m/8K = 20, chi at the centre {mp.nstr(chiF[cen], 5)}), static law, a body shared between the centre "
   f"and a face-adjacent site at s = 3/10: residuals < 1e-50, flux of chi = <H> + F = 8K(Q1+Q2) = {mp.nstr(fl, 12)}; "
   f"dWt/ds = {mp.nstr(dW, 15)} = m(w_off - w_cen) (the work of the supply) to {mp.nstr(abs(dW - work), 2)}")

# ---------------------------------------------------------------- B1, B2: a walker with slaved fields (floating point)
Kw = 1 / 8
hdim = 2 * n3
Hm = np.zeros((hdim, hdim), complex)
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
for x in I3:
    for j in range(3):
        e = tuple(int(k == j) for k in range(3))
        y = tuple(a - b for a, b in zip(x, e))
        if y in idx:  # H_{x, x-e} = sigma/(2i), H_{x-e, x} = its adjoint
            Hm[2 * idx[x]:2 * idx[x] + 2, 2 * idx[y]:2 * idx[y] + 2] = sig[j] / 2j
            Hm[2 * idx[y]:2 * idx[y] + 2, 2 * idx[x]:2 * idx[x] + 2] = (sig[j] / 2j).conj().T
Gf = np.array([[float(v) for v in row] for row in G])
Mf = np.array([[float(v) for v in row] for row in mlap])
Lw = np.zeros((n3, len(W3)))
wid = {x: i for i, x in enumerate(W3)}
for x in I3:
    for y in NB3[x]:
        if y in wid:
            Lw[idx[x], wid[y]] = 1


def fields(psi_, w, c, tol=1e-15):
    for _ in range(500):
        A = np.repeat(np.sqrt(w) / c, 2)
        Hp = A * (Hm @ (A * psi_))
        e = np.real(np.conj(psi_) * Hp).reshape(n3, 2).sum(1)
        N = w * c
        c_new = 1 + Gf @ (e / (8 * Kw * N))
        N_new = 1 - Gf @ (3 * e / (8 * Kw * c_new))
        w_new = N_new / c_new
        d = max(np.abs(c_new - c).max(), np.abs(w_new - w).max())
        w, c = w_new, c_new
        if d < tol:
            break
    return w, c


def ledger_parts(psi_, w, c):
    A = np.repeat(np.sqrt(w) / c, 2)
    Heff = (A[:, None] * Hm) * A[None, :]
    Hexp = np.real(np.conj(psi_) @ (Heff @ psi_))
    lapc = -Mf @ c + Lw.sum(1)  # (Lap chi)_x at interior sites, walls at 1
    N = w * c
    flux = 8 * Kw * np.sum(Lw.T @ (c - 1))  # 8K sum over wall bonds (chi_int - 1)
    # F = 8K sum_all N (Lap chi): interior part plus walls (N = 1 there, Lap chi = flux share)
    Fv = 8 * Kw * (np.sum(N * lapc) + np.sum(Lw.T @ (c - 1)))
    return Hexp, Fv, flux, Heff


evals, evecs = np.linalg.eigh(Hm)
k2 = max(k for k in range(hdim) if evals[k] < evals[-1] - 1e-6)
psi0 = (evecs[:, -1] + evecs[:, k2]) / np.sqrt(2)


def rhs(p, w, c, mismatch):
    w, c = fields(p, w, c)
    A = np.repeat(np.sqrt(w), 2) if mismatch else np.repeat(np.sqrt(w) / c, 2)
    return -1j * (A * (Hm @ (A * p))), w, c


def rk4(ps, w, c, dt, mismatch):
    k1, w, c = rhs(ps, w, c, mismatch)
    k2, _, _ = rhs(ps + dt / 2 * k1, w, c, mismatch)
    k3, _, _ = rhs(ps + dt / 2 * k2, w, c, mismatch)
    k4, _, _ = rhs(ps + dt * k3, w, c, mismatch)
    return ps + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4), w, c


def flux_of(ps, w, c):
    w, c = fields(ps, w, c)
    return ledger_parts(ps, w, c), w, c


def run(mismatch, T=3.0, dt=0.01, probes=(0, 100, 200), h=1e-3):
    ps = psi0.copy()
    w, c = fields(ps, np.ones(n3), np.ones(n3))
    out, rates = [], []
    dens0 = np.abs(ps.reshape(n3, 2)) ** 2
    maxmove = 0.0
    for k in range(int(round(T / dt)) + 1):
        (Hexp, Fv, flux, Heff), w, c = flux_of(ps, w, c)
        out.append((k * dt, flux, Hexp + Fv))
        maxmove = max(maxmove, np.abs(np.abs(ps.reshape(n3, 2)) ** 2 - dens0).sum())
        if k in probes:  # finite-difference rate with two small steps vs i<psi|[G, H_eff]|psi> (G = generator used)
            Ag = np.repeat(np.sqrt(w), 2) if mismatch else np.repeat(np.sqrt(w) / c, 2)
            Gg = (Ag[:, None] * Hm) * Ag[None, :]
            pred = np.real(1j * np.vdot(ps, (Gg @ Heff - Heff @ Gg) @ ps))
            p1, w1_, c1_ = rk4(ps, w, c, h, mismatch)
            (_, _, f1, _), w1_, c1_ = flux_of(p1, w1_, c1_)
            p2, w2_, c2_ = rk4(p1, w1_, c1_, h, mismatch)
            (_, _, f2, _), _, _ = flux_of(p2, w2_, c2_)
            rates.append(((-3 * flux + 4 * f1 - f2) / (2 * h), pred))
        ps, w, c = rk4(ps, w, c, dt, mismatch)
    fl = np.array([o[1] for o in out])
    le = np.array([o[2] for o in out])
    return fl, le, maxmove, rates


fl, le, mv, rates1 = run(False)
drift1 = np.abs(fl - fl[0]).max()
ok("B1", drift1 < 1e-7 and np.abs(fl - le).max() < 1e-10 and mv > 0.1 and max(abs(r[1]) for r in rates1) == 0,
   f"FLOAT: walker on block 54's walk (3^3 interior, K = 1/8, top-two positive-energy superposition), fields slaved "
   f"(static law) at each RK4 stage: flux of chi = <H> + F to {np.abs(fl - le).max():.1e}, flux {fl[0]:.9f} constant to "
   f"{drift1:.1e} over t = 0..3 while the density moved by {mv:.2f} (l1)")
flm, lem, mvm, rates2 = run(True)
drift2 = np.abs(flm - flm[0]).max()
agree = max(abs(r[0] - r[1]) for r in rates2)
big = max(abs(r[1]) for r in rates2)
ok("B2", agree < 1e-3 * big and big > 1e4 * drift1 and drift2 > 1e4 * drift1 and np.abs(flm - lem).max() < 1e-10,
   f"FLOAT: same walker evolved by sqrt(w) H sqrt(w) while the ledger crosses bonds at sqrt(w w')/(chi chi'): flux = "
   f"<H> + F still, but it moves: rate at t = 0, 1, 2 " + ", ".join(f"{r[0]:.3e}" for r in rates2)
   + f" vs i<[G, H_eff]> " + ", ".join(f"{r[1]:.3e}" for r in rates2) + f" (worst gap {agree:.0e}); drift {drift2:.1e} "
   f"over t = 0..3, {drift2 / max(drift1, 1e-300):.0e} times B1's")

print("SUMMARY: " + ("PROVED " if not FAILS else "PARTIAL (failed checks: " + ", ".join(FAILS) + ") ")
      + "in block 60's walled box, for every weight-one ledger and every lengths' kinetic term of weight -1 in the rates, "
      "K_lam + <H> + F equals the walls' term on solutions and moves only with the content's explicit label dependence: "
      "(a) supplied content: dWt/dt = sum_x w_x drho_x/dt (the supply's work), at first order in velocity the change "
      "of the static ledger, -(1/4K) rhodot.g rho at weak field, not zero; (b) a walker with slaved fields keeps the "
      "flux of chi exactly; (c) this is block 55's kept ledger with held walls in place of mu, K_lam included")
if not FAILS:
    print("HIT: in block 60's walled box (walls held at w = l = 1), for every ledger of weight one and every lengths' "
          "kinetic term of weight -1 in the rates (c_k l^s lamdot^2/w among them), h = K_lam + <H> + F equals the walls' "
          "term sum_W d(<H> + F)/du (8K x the flux of chi into the walls for the curvature member) at every label time on "
          "solutions, and dh/dt is the content's explicit label derivative; supplied rest content: dWt/dt = sum_x w_x "
          "drho_x/dt exactly, Wt = sum rho - (1/8K)(rho.g rho + 3 rhodot.g^2 rhodot) + O(rho^3) for c_k = -6K; a walker "
          "evolved by the ledger's own generator with slaved fields keeps the flux exactly, one evolved by sqrt(w) H "
          "sqrt(w) moves it at i<[G, H_eff]>")
