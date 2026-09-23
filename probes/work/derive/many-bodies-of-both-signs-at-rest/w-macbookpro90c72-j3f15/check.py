#!/usr/bin/env python3
"""J:derive:many-bodies-of-both-signs-at-rest:a1 -- worker w-macbookpro90c72-j3f15.

Block 60's curvature member, bodies at rest (block 60 T4, block 71 T3): chi = 1 + sum Q_i g(., x_i),
Q_i chi(x_i) = mu_i (mu = m/(8K), either sign), N = 1 - sum P_i g(., x_i) solving (-Delta + Q/chi) N = 0,
walls held at chi = N = 1, rates w = N/chi; positive static rates iff L = -Delta + Q/chi is positive
definite (block 71 T3(d)).

  B  exact rational: the 5^3 box with held walls (walls at 0 and 6), Green columns by exact banded
     elimination; the certificate of a negative body beyond its single-body bound; all roots
  S  exact symbolic: the positive-definiteness criterion, the fold identity, the bounds (a), (b), (e)
  C  the zero-ledger pair (c)
  D  content that moves (d): the two field equations from block 60's bond form, and the closed lattice
  X  executed on Z^3 (floating point): extended and joint bounds, balls
See ATTEMPT.md.
"""
import itertools
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import ive

NF = 0
NP = 0


def rep(tag, ok, msg):
    global NF, NP
    NF += (not ok)
    NP += bool(ok)
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


NBR = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
n = 5
SITES = list(itertools.product(range(1, n + 1), repeat=3))
IDX = {s: i for i, s in enumerate(SITES)}


def band_solve(diag_extra, rhs_cols):
    """exact solve of (-Delta_D + diag(diag_extra)) X = rhs on the n^3 interior; returns (X, pivots)."""
    N = len(SITES)
    A = [dict() for _ in range(N)]
    for i, s in enumerate(SITES):
        A[i][i] = Fr(6) + diag_extra.get(i, Fr(0))
        for d in NBR:
            t = (s[0] + d[0], s[1] + d[1], s[2] + d[2])
            if t in IDX:
                A[i][IDX[t]] = Fr(-1)
    B = [list(r) for r in rhs_cols]
    piv = []
    for p in range(N):
        pv = A[p][p]
        piv.append(pv)
        for r in range(p + 1, min(N, p + n * n + 1)):
            if p in A[r]:
                f = A[r][p] / pv
                del A[r][p]
                for c, v in A[p].items():
                    if c > p:
                        A[r][c] = A[r].get(c, Fr(0)) - f * v
                for j in range(len(B[r])):
                    B[r][j] -= f * B[p][j]
    X = [[Fr(0)] * len(B[0]) for _ in range(N)]
    for p in range(N - 1, -1, -1):
        for j in range(len(B[0])):
            X[p][j] = (B[p][j] - sum(v * X[c][j] for c, v in A[p].items() if c > p)) / A[p][p]
    return X, piv


def green(targets):
    rhs = [[Fr(1) if IDX[t] == i else Fr(0) for t in targets] for i in range(len(SITES))]
    X, _ = band_solve({}, rhs)
    return [[X[i][j] for i in range(len(SITES))] for j in range(len(targets))]


def lap_ok(col, src):
    val = lambda t: col[IDX[t]] if t in IDX else Fr(0)
    return all(6 * val(s) - sum(val((s[0] + d[0], s[1] + d[1], s[2] + d[2])) for d in NBR) == (1 if s == src else 0)
               for s in SITES)


def two_body(A, B, QA, QB):
    gA, gB = green([A, B])
    a, c, b = gA[IDX[A]], gA[IDX[B]], gB[IDX[B]]
    chi = [1 + QA * gA[i] + QB * gB[i] for i in range(len(SITES))]
    cA, cB = chi[IDX[A]], chi[IDX[B]]
    vA, vB = QA / cA, QB / cB
    M = sp.Matrix([[1 + vA * a, vA * c], [vB * c, 1 + vB * b]])
    P = M.LUsolve(sp.Matrix([vA, vB]))
    PA, PB = Fr(str(sp.Rational(P[0]))), Fr(str(sp.Rational(P[1])))
    Nf = [1 - PA * gA[i] - PB * gB[i] for i in range(len(SITES))]
    return dict(gA=gA, gB=gB, a=a, b=b, c=c, chi=chi, cA=cA, cB=cB, vA=vA, vB=vB, PA=PA, PB=PB, N=Nf,
                muA=QA * cA, muB=QB * cB)


# ------------------------------------------------------------------ B family
def B1():
    A, B = (3, 3, 3), (3, 3, 4)
    gA, gB = green([A, B])
    ok = lap_ok(gA, A) and lap_ok(gB, B)
    rep("B1 box", ok, f"5^3 interior, walls at 0 and 6: exact columns g(.,A), g(.,B) (A=(3,3,3), B=(3,3,4)); -Delta g = delta at all 125 "
        f"sites; G_AA = {gA[IDX[A]]}, G_AB = {gA[IDX[B]]}, G_BB = {float(gB[IDX[B]]):.6f}")


def B2():
    A, B = (3, 3, 3), (3, 3, 4)
    T = two_body(A, B, Fr(4), Fr(-2))
    single = -1 / (4 * T['b'])
    X, piv = band_solve({IDX[A]: T['vA'], IDX[B]: T['vB']}, [[Fr(0)] for _ in SITES])
    pd = all(p > 0 for p in piv)
    w = [T['N'][i] / T['chi'][i] for i in range(len(SITES))]
    # N solves (-Delta + Q/chi) N = 0 with N = 1 on the walls
    val = lambda t: T['N'][IDX[t]] if t in IDX else Fr(1)
    eqn = all(6 * val(s) - sum(val((s[0] + d[0], s[1] + d[1], s[2] + d[2])) for d in NBR)
              + (T['vA'] if s == A else T['vB'] if s == B else 0) * val(s) == 0 for s in SITES)
    ok = T['muB'] < single and min(T['chi']) > 0 and pd and eqn and min(T['N']) > 0 and min(w) > 0
    rep("B2 beyond the bound", ok,
        f"charges Q=(4,-2): mu_A = {float(T['muA']):.4f}, mu_B = {float(T['muB']):.4f} < single-body bound -1/(4G_BB) = {float(single):.4f}; "
        f"chi >= {float(min(T['chi'])):.4f} at all sites; L = -Delta + Q/chi positive definite (all 125 pivots > 0, exact); "
        f"N solves L N = 0 exactly, N >= {float(min(T['N'])):.4f}; rates in [{float(min(w)):.4f}, {float(max(w)):.4f}] (w_B = {float(w[IDX[B]]):.4f})")
    return T


def B3(T):
    a, b, c = sp.Rational(str(T['a'])), sp.Rational(str(T['b'])), sp.Rational(str(T['c']))
    muA, muB = sp.Rational(str(T['muA'])), sp.Rational(str(T['muB']))
    qa, qb = sp.symbols('qa qb')
    e1 = sp.expand(qa * (1 + a * qa + c * qb) - muA)
    e2 = sp.expand(qb * (1 + c * qa + b * qb) - muB)
    pol = sp.Poly(sp.resultant(e1, e2, qa), qb)
    nreal = pol.count_roots()
    D = a * b - c * c
    rows = []
    for r in pol.nroots(n=40):
        if abs(sp.im(r)) < 1e-25:
            rb = sp.re(r)
            ra = (muB / rb - 1 - b * rb) / c
            cA, cB = 1 + a * ra + c * rb, 1 + c * ra + b * rb
            det = (b / D + ra / cA) * (a / D + rb / cB) - (c / D)**2
            rows.append((float(ra), float(rb), bool(cA > 0) and bool(cB > 0), bool(det > 0) and bool(b / D + ra / cA > 0)))
    ok = pol.degree() == 4 and nreal == 2 and all(r[2] for r in rows) and sum(r[3] for r in rows) == 1
    rep("B3 roots", ok,
        f"at these (mu_A, mu_B) the lengths' equations have 4 roots, {nreal} real (Sturm count on the exact quartic), both with positive "
        f"lengths; exactly one has L positive definite: " + "; ".join(f"Q=({r[0]:.3f},{r[1]:.3f}) PD={r[3]}" for r in rows))


# ------------------------------------------------------------------ S family (symbolic)
def S1():
    a, b, c, QA, QB = sp.symbols('a b c Q_A Q_B', real=True)
    cA, cB = 1 + a * QA + c * QB, 1 + c * QA + b * QB
    J = sp.Matrix([[cA + QA * a, QA * c], [QB * c, cB + QB * b]])        # d(mu)/dQ
    G2 = sp.Matrix([[a, c], [c, b]])
    V = sp.diag(QA / cA, QB / cB)
    fold = sp.simplify(J.det() - cA * cB * (sp.eye(2) + V * G2).det()) == 0
    pdid = sp.simplify((G2.inv() + V).det() - (sp.eye(2) + G2 * V).det() / G2.det()) == 0
    vA, vB = sp.symbols('v_A v_B', real=True)
    D = a * b - c * c
    det2 = (b / D + vA) * (a / D + vB) - c**2 / D**2
    thr = -(1 + a * vA) / (b + D * vA)
    crit = sp.simplify(det2.subs(vB, thr)) == 0
    ext = sp.simplify(thr + 1 / b - (-(c**2 * vA) / (b * (b + D * vA)))) == 0
    rep("S1 criterion", fold and pdid and crit and ext,
        "det(d mu/dQ) = chi_A chi_B det(1 + V G): the fold of the lengths' map is where L loses definiteness; with v = Q/chi, "
        "L > 0 iff b/D + v_A > 0 and v_B > -(1 + a v_A)/(b + D v_A) (D = ab - c^2); that threshold is -1/b - c^2 v_A/(b(b + D v_A)): "
        "below B's single value -1/b whenever v_A > 0 -- a positive neighbour extends the bound")


def S2():
    q, g, Q1, Q2, a, c = sp.symbols('q g Q_1 Q_2 a c', real=True)
    par = sp.simplify(q * (1 + g * q) + 1 / (4 * g) - g * (q + 1 / (2 * g))**2) == 0
    # two negative bodies: chi_A < 1 + a Q_A when c Q_B < 0, and Q_A < 0, so mu_A = Q_A chi_A > Q_A(1 + a Q_A) >= -1/(4a)
    gd = sp.symbols('g_d', positive=True)
    g0 = sp.symbols('g_0', positive=True)
    Qs = -1 / (2 * (g0 + gd))
    joint = sp.simplify(Qs * (1 + (g0 + gd) * Qs) + 1 / (4 * (g0 + gd))) == 0
    foldsym = sp.simplify(1 + 2 * Qs * (g0 + gd)) == 0
    # (e): sum mu = 1.Q + Q.GQ >= q + q^2/Cap >= -Cap/4 (Cauchy-Schwarz in the G inner product)
    cap = sp.symbols('C', positive=True)
    lo = sp.simplify(q + q**2 / cap + cap / 4 - (q + cap / 2)**2 / cap) == 0
    rep("S2 bounds", par and joint and foldsym and lo,
        "q(1+gq) = g(q + 1/(2g))^2 - 1/(4g): for two negative bodies each mu_i = Q_i chi_i > Q_i(1 + G_ii Q_i) >= -1/(4G_ii), so the joint "
        "region lies strictly inside the single ones; a symmetric negative pair folds at mu = -1/(4(g0 + g_d)); on any set S of body "
        "sites, sum mu_i = 1.Q + Q.GQ >= q + q^2/Cap(S) >= -Cap(S)/4 (q = 1.Q)")


def S3():
    # symmetric placement in the box: two negative bodies equidistant from the centre
    A, B = (3, 3, 2), (3, 3, 4)
    gA, gB = green([A, B])
    a, c, b = gA[IDX[A]], gA[IDX[B]], gB[IDX[B]]
    Qs = Fr(-1) / (2 * (a + c))
    mus = Qs * (1 + (a + c) * Qs)
    inside = mus * Fr(99, 100)
    qin = (-1 + sp.sqrt(1 + 4 * (sp.Rational(str(a + c))) * sp.Rational(str(inside)))) / (2 * sp.Rational(str(a + c)))
    cin = 1 + (sp.Rational(str(a + c))) * qin
    v = qin / cin
    D = sp.Rational(str(a * b - c * c))
    det = (sp.Rational(str(b)) / D + v) ** 2 - (sp.Rational(str(c)) / D)**2
    ok = a == b and mus > -1 / (4 * a) and sp.N(det, 50) > 0 and (1 + 4 * (a + c) * (mus * Fr(101, 100))) < 0
    rep("S3 negative pair (box)", ok,
        f"A=(3,3,2), B=(3,3,4), G_AA = G_BB = {float(a):.5f}: symmetric fold mu* = -1/(4(G_AA+G_AB)) = {float(mus):.5f} against the single "
        f"{float(-1/(4*a)):.5f}; at 0.99 mu* the symmetric solution has L > 0, at 1.01 mu* it has no real symmetric solution")


# ------------------------------------------------------------------ C family
def C1():
    A, B = (3, 3, 3), (3, 3, 4)
    T = two_body(A, B, Fr(1), Fr(-1))
    X, piv = band_solve({IDX[A]: T['vA'], IDX[B]: T['vB']}, [[Fr(0)] for _ in SITES])
    ok = all(p > 0 for p in piv) and min(T['chi']) > 0 and min(T['N']) > 0 and T['PA'] + T['PB'] < 0
    rep("C1 zero ledger", ok,
        f"Q_A = -Q_B = 1 (ledger 8K(Q_A+Q_B) = 0): mu = ({float(T['muA']):.4f}, {float(T['muB']):.4f}); L > 0, all rates positive; far "
        f"fields: lengths 2(Q_A+Q_B) = 0 (a dipole only), rates P_A+P_B = {float(T['PA']+T['PB']):.5f} < 0: clocks run fast far away")


# ------------------------------------------------------------------ D family
def D1():
    K = sp.symbols('K', positive=True)
    Ls = 4
    Nv = sp.symbols('N0:%d' % Ls, positive=True)
    Cv = sp.symbols('c0:%d' % Ls, positive=True)          # chi
    rh = sp.symbols('r0:%d' % Ls, real=True)              # on-site energy per tick <m_x>
    th = sp.symbols('t0:%d' % Ls, real=True)              # hop energy per tick <h_b>, bond (x, x+1) on a ring
    lap = lambda f, z: f[(z + 1) % Ls] + f[(z - 1) % Ls] - 2 * f[z]
    F = 8 * K * sum(Nv[z] * lap(Cv, z) for z in range(Ls))
    cb = [sp.sqrt(Nv[z] * Nv[(z + 1) % Ls]) / (Cv[z] * Cv[(z + 1) % Ls])**sp.Rational(3, 2) for z in range(Ls)]
    E = sum(cb[z] * th[z] for z in range(Ls)) + sum(Nv[z] / Cv[z] * rh[z] for z in range(Ls))
    ok = True
    for z in range(Ls):
        tau = (cb[z] * th[z] + cb[(z - 1) % Ls] * th[(z - 1) % Ls]) / 2
        e = Nv[z] / Cv[z] * rh[z] + tau
        ok &= sp.simplify(sp.diff(F + E, Nv[z]) - (8 * K * lap(Cv, z) + e / Nv[z])) == 0
        ok &= sp.simplify(sp.diff(F + E, Cv[z]) - (8 * K * lap(Nv, z) - (e + 2 * tau) / Cv[z])) == 0
    f = [Fr(3), Fr(5, 2), Fr(7), Fr(1, 3)]
    ident = sum(Fr(lap(f, z)) / f[z] for z in range(Ls)) == sum((f[z] - f[(z + 1) % Ls])**2 / (f[z] * f[(z + 1) % Ls]) for z in range(Ls))
    rep("D1 moving content", ok and ident,
        "from F = 8K sum N (Delta chi) and <H> = sum_b sqrt(N_x N_y)/(chi_x chi_y)^(3/2) <h_b> + sum N/chi <m> (block 60: bonds crossed at "
        "sqrt(w_x w_y)/(chi_x chi_y), N = w chi): stationarity gives (Delta chi)_z = -e_z/(8K N_z), (Delta N)_z = (e_z + 2 tau_z)/(8K chi_z), "
        "tau_z = half the hop energy on z's bonds (symbolic, ring of 4); block 75 T1 checked")


def D2():
    S_chi, S_N, K = sp.symbols('S_chi S_N K')
    # walker without rest energy: e = tau pointwise, so sum e/(chi N) = -8K S_chi and sum 3e/(chi N) = 8K S_N
    sol = sp.solve([sp.Eq(3 * (-8 * K * S_chi), 8 * K * S_N)], [S_N], dict=True)
    only_zero = sol and sp.simplify(sol[0][S_N] + 3 * S_chi) == 0
    m = sp.Integer(1)
    Ep, Em = 2 * m, -m
    tau = lambda E: E - m**2 / E
    ex = (Ep + 3 * Em < 0) and (tau(Ep) + 3 * tau(Em) > 0)
    x = sp.symbols('x', positive=True)
    mono = sp.simplify(sp.diff(x - m**2 / x, x)) == 1 + m**2 / x**2
    rep("D2 closed lattice", only_zero and ex and mono,
        "block 54's walker has no on-site term, so e = tau: the identities give S_N + 3 S_chi = 0 with both >= 0, so chi and N are uniform "
        "and e = 0 at every site: no rest with walk content of either sign; with rest energy the identities only require "
        "sum e/(chi N) < 0 < sum tau/(chi N) (e.g. one amplitude at E = 2m with three at rest at -m, weak field); one of each sign never "
        "(tau = E - m^2/E is increasing in |E|)")


# ------------------------------------------------------------------ X family (executed, Z^3)
CACHE = {}


def Gz(d):
    k = tuple(sorted(abs(v) for v in d))
    if k not in CACHE:
        a, bb, c = k
        f = lambda t: ive(a, 2 * t) * ive(bb, 2 * t) * ive(c, 2 * t)
        r2 = a * a + bb * bb + c * c
        pts = sorted(set([0, 0.5, 2, max(4, r2 / 6), max(10, r2 / 2), 60, 400, 4000]))
        CACHE[k] = sum(quad(f, lo, hi, limit=400, epsabs=1e-15, epsrel=1e-13)[0] for lo, hi in zip(pts[:-1], pts[1:])) \
            + quad(f, 4000, np.inf, limit=200)[0]
    return CACHE[k]


def continuation(Gm, mu_vec_of, pos_fix=None):
    n_ = Gm.shape[0]
    Ginv = np.linalg.inv(Gm)
    Q = np.zeros(n_) if pos_fix is None else pos_fix.copy()
    t, step = 0.0, 0.05
    while step > 1e-10:
        mu = mu_vec_of(t + step)
        Qn = Q.copy()
        for _ in range(60):
            chi = 1 + Gm @ Qn
            Jm = np.diag(chi) + np.diag(Qn) @ Gm
            dQ = np.linalg.solve(Jm, -(Qn * chi - mu))
            Qn = Qn + dQ
            if np.abs(dQ).max() < 1e-13:
                break
        chi = 1 + Gm @ Qn
        ok = np.abs(Qn * chi - mu).max() < 1e-11 and chi.min() > 0 and np.abs(Qn - Q).max() < 1 \
            and np.linalg.eigvalsh(Ginv + np.diag(Qn / chi)).min() > 0
        if ok:
            t += step
            Q = Qn
        else:
            step /= 2
    return t


def X1():
    g0 = Gz((0, 0, 0))
    rows = []
    for d in (1, 2, 4):
        c = Gz((d, 0, 0))
        Gm = np.array([[g0, c], [c, g0]])
        for muA in (0.5, 2.0, 8.0):
            QA0 = (-1 + np.sqrt(1 + 4 * g0 * muA)) / (2 * g0)
            Q0 = np.array([QA0, 0.0])
            # start at (mu_A, 0): solve with B absent, then push mu_B down
            t = continuation(Gm, lambda t_: np.array([muA, -t_]), Q0)
            rows.append((d, muA, -t))
    neg = [-1 / (4 * (g0 + Gz((d, 0, 0)))) for d in (1, 2, 4)]
    ok = all(r[2] < -1 / (4 * g0) for r in rows) and all(v > -1 / (4 * g0) for v in neg)
    rep("X1 Z^3 bounds (executed)", ok,
        f"single -1/(4g0) = {-1/(4*g0):.4f}; mu_B reached with L > 0 (continuation, a lower estimate of the reach) next to mu_A = 0.5, 2, 8: "
        + "; ".join(f"d={d}: " + ", ".join(f"{r[2]:.3f}" for r in rows if r[0] == d) for d in (1, 2, 4))
        + "; two equal negative bodies at d = 1, 2, 4: " + ", ".join(f"{v:.3f}" for v in neg))


def X2():
    out = []
    for R2 in (0, 1, 2, 4, 6, 9):
        R = int(np.ceil(np.sqrt(R2)))
        S = [p for p in itertools.product(range(-R, R + 1), repeat=3) if p[0]**2 + p[1]**2 + p[2]**2 <= R2]
        Gm = np.array([[Gz((p[0] - q[0], p[1] - q[1], p[2] - q[2])) for q in S] for p in S])
        cap = np.linalg.solve(Gm, np.ones(len(S))).sum()
        t = continuation(Gm, lambda t_: -t_ * np.ones(len(S)) / len(S))
        out.append((R2, len(S), cap, -t))
    ok = all(r[3] >= -r[2] / 4 - 1e-9 for r in out) and all(0.85 < r[3] / (-r[2] / 4) <= 1 + 1e-9 for r in out) \
        and abs(out[0][3] + 1 / (4 * Gz((0, 0, 0)))) < 1e-8
    rep("X2 spread body (executed)", ok,
        "negative body spread evenly over balls |x|^2 <= R^2: (N, Cap, total mu reached with L > 0) = "
        + "; ".join(f"({r[1]}, {r[2]:.2f}, {r[3]:.3f})" for r in out) + ": always >= -Cap/4 (S2), at 0.88-1.00 of it: the bound "
        "grows with the capacity (linear size), not with N")


def main():
    B1()
    T = B2()
    B3(T)
    S1(); S2(); S3()
    C1()
    D1(); D2()
    X1(); X2()
    print(f"TOTAL: PASS={NP} FAIL={NF}")
    if NF == 0:
        print("SUMMARY: PROVED the HIT case and (a)-(c) exactly, (d) for block 54's walker, (e) as a bound: a positive neighbour extends a "
              "negative body's bound (L > 0 iff v_B > -(1 + a v_A)/(b + D v_A), below -1/b for v_A > 0), two negative bodies tighten "
              "each other's (each mu_i > -1/(4G_ii); symmetric pair -1/(4(g0+g_d))), a zero-ledger pair is static with no length monopole "
              "and a rate monopole P_A+P_B < 0, moving walk content cannot hold a closed lattice at rest (e = tau forces S_N + 3S_chi = 0), "
              "and any set of body sites carries sum mu >= -Cap(S)/4")
        print("HIT: in block 60's curvature member on the 5^3 box with held walls, a negative body at (3,3,4) with mu_B = -1.5929 (beyond "
              "its single-body bound -1/(4G_BB) = -1.1045) next to a positive body with mu_A = 7.1650 at (3,3,3) is at rest with every rate "
              "positive (exact rational charges Q = (4, -2): L positive definite, all 125 pivots > 0, N >= 0.8724): a positive neighbour "
              "extends a negative body's bound")
    else:
        print(f"SUMMARY: ROUTE FAILS AT {NF} check(s) above")


if __name__ == "__main__":
    main()
