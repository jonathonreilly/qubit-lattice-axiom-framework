#!/usr/bin/env python3
"""Attempt review-20261004-cubic-unfolding (J:derive:review-20261004-cubic-unfolding:a1): exhaustive node census near the
J > 2 line-node flip (fixed J in (2,J0) u (J0,1+sqrt5)) and at / near the exceptional root J0 of N = J^3 - 4J - 4.

Self-contained (numpy not needed; sympy + mpmath only).  Supplied comparator: H(f) = i M(f), four-site Bloch matrix of the landed
network, Jx = Jy = 1, Jz = J, odd term kappa (rebuilt below from the network rules; nothing is imported from the repository).

What this script does (labels as in ATTEMPT.md):
  E1-E5  EXACT (sympy, symbolic in J and kappa): odd characteristic-polynomial coefficients vanish identically; line identity;
         rank(M) <= 2 on the line family and on plane family (ii), including COMPLEX points (adjugate vanishes mod the ideal);
         flip-node algebra c(kappa_f) = 1, q' = 2N/A, disc = 4N^2/A^2, u_f >= u_*.
  N1-N4  CHECKED (mpmath, 40-60 digits, not interval-certified): the landed jets at three J values (rank-2 Jacobian, order-3 reduced
         function, g and u2 formulas), the slaving |s0| <= |d|, the zero-count (argument principle) of the reduced function in a disc,
         exact family points as zeros of the Schur vector including the complex ones, the exceptional-point jets and the
         resultant of the two reduced quadratic forms, and the 0 / 2 / 4 pattern of real family points near (J0, kappa_f(J0)).
The proof that these ingredients give an exhaustive census is in ATTEMPT.md (conservation of multiplicity); this script does not
prove the census by itself and does not certify any radius.
"""
import sys
import time
import random

import mpmath as mp
import sympy as sp

T0 = time.time()
RES = []


def emit(s):
    print(s, flush=True)


def check(label, ok, note=""):
    RES.append(bool(ok))
    emit(("PASS " if ok else "FAIL ") + label + ((" :: " + note) if note else ""))


# ------------------------------------------------------------------------------------------------ network (supplied comparator)
def is_site(p):
    i, j, z = p
    m = z % 4
    if m == 0:
        return j % 2 == 0
    if m == 1:
        return i % 2 == 1
    if m == 2:
        return j % 2 == 1
    return i % 2 == 0


def flavour(p, q):
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0:
        return "z"
    lo = p if sum(d) > 0 else q
    m = p[2] % 4
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"


def neighbours(p):
    out = []
    for a in range(3):
        for s_ in (-1, 1):
            q = list(p)
            q[a] += s_
            q = tuple(q)
            if is_site(q):
                out.append(q)
    return out


REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]


def reduce_cell(p):
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    return REPS.index((x - 2 * n1, y - 2 * n2, z)), (n1, n2, n3)


def build_terms():
    out = []
    for p in REPS:
        a, _ = reduce_cell(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce_cell(q)
                out.append((a, b, n, flavour(p, q)))
        nb = {flavour(p, q): q for q in neighbours(p)}
        for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
            r1, n1 = reduce_cell(nb[l])
            r2, n2 = reduce_cell(nb[m])
            out.append((r1, r2, tuple(n2[i] - n1[i] for i in range(3)), "odd"))
    return out


TERMS = build_terms()
assert len(TERMS) == 18


def Hmat(f, J, kap):
    """H(f) = i M(f); analytic in complex f (M[b,a] gets -t e^{-2 pi i f.n}, equal to the conjugate for real f)."""
    f = [mp.mpmathify(x) for x in f]
    amp = {"x": 2, "y": 2, "z": 2 * J, "odd": 2 * kap}
    M = mp.zeros(4, 4)
    for (a, b, n, k) in TERMS:
        ph = mp.expj(2 * mp.pi * sum(f[i] * n[i] for i in range(3)))
        M[a, b] += amp[k] * ph
        M[b, a] -= amp[k] / ph
    return 1j * M


# ------------------------------------------------------------------------------------------------ EXACT block (sympy)
z1, z3, Js, ks, cs, us = sp.symbols("z1 z3 J kappa c u")
Z2 = sp.Symbol("z2")


def Msym(a1, a2, a3):
    amp = {"x": 2, "y": 2, "z": 2 * Js, "odd": 2 * ks}
    M = sp.zeros(4, 4)
    for (a, b, n, k) in TERMS:
        ph = a1 ** n[0] * a2 ** n[1] * a3 ** n[2]
        M[a, b] += amp[k] * ph
        M[b, a] -= amp[k] / ph
    return M


def exact_block():
    Aj = 4 + 2 * Js - Js ** 2
    Nj = Js ** 3 - 4 * Js - 4
    # E1: odd characteristic coefficients of H = iM vanish identically in (z1,z2,z3,J,kappa)
    Mg = Msym(z1, Z2, z3)
    lam = sp.Symbol("lam")
    cp = sp.Poly(sp.expand((Mg - lam * sp.eye(4)).det(method="berkowitz")), lam)
    odd = [sp.simplify(cp.coeff_monomial(lam ** 3)), sp.simplify(cp.coeff_monomial(lam ** 1))]
    check("E1 charpoly of M has no lam^3 and no lam^1 term, identically in z1,z2,z3,J,kappa",
          odd[0] == 0 and odd[1] == 0, "so spec H(f) = {+-l1, +-l2}, det H = l1^2 l2^2 >= 0, and a touching of the middle pair is at E = 0")
    # E2: line identity
    Hl = Msym(z1, 1 / z1, 1)
    D = sp.expand(Hl.det(method="berkowitz"))
    uu = ks ** 2
    cc = (z1 + 1 / z1) / 2
    qline = Js ** 2 + 4 * cc ** 2 * uu - 2 * cc - 4 * uu - 2
    check("E2 line identity D(z,1/z,1) = 16 [J^2 + 4 c^2 u - 2c - 4u - 2]^2", sp.simplify(sp.expand(D - 16 * qline ** 2)) == 0)
    # E3: adjugate of M vanishes modulo the ideals of the line family and of plane family (ii): rank M <= 2 at all (complex) family points
    minpoly = sp.Poly(uu * z1 ** 4 - z1 ** 3 + (Js ** 2 - 2 * uu - 2) * z1 ** 2 - z1 + uu, z1)
    adj = Msym(z1, 1 / z1, 1).adjugate(method="berkowitz")
    badL = 0
    for e in adj:
        num = sp.numer(sp.together(sp.expand(e)))
        if sp.simplify(sp.rem(sp.Poly(sp.expand(num), z1), minpoly).as_expr()) != 0:
            badL += 1
    check("E3a adj(M) = 0 mod (u z^4 - z^3 + (J^2-2u-2) z^2 - z + u) on the line family z=(z,1/z,1): rank M <= 2 at every root, complex included",
          badL == 0, f"{16 - badL}/16 entries reduce to 0")
    a_ = 1 - Js / (4 * uu)
    b_ = (Js + 2) / (4 * uu) - (4 + Js - Js ** 2) / Js
    dom = sp.QQ.frac_field(Js, ks)
    G = sp.groebner([z1 ** 2 - 2 * a_ * z1 + 1, z3 ** 2 - 2 * b_ * z3 + 1], z1, z3, order="lex", domain=dom)
    adj2 = Msym(z1, 1 / z1, z3).adjugate(method="berkowitz")
    badP = 0
    for e in adj2:
        num = sp.numer(sp.together(sp.expand(e)))
        if sp.simplify(G.reduce(sp.expand(num))[1]) != 0:
            badP += 1
    check("E3b adj(M) = 0 mod the two cosine quadratics of plane family (ii): rank M <= 2 at every (complex) point of the family",
          badP == 0, f"{16 - badP}/16 entries reduce to 0; z1 root of z^2-2az+1 (a=1-J/(4u)), z3 root of z^2-2bz+1")
    # E4: flip algebra
    uF = Js * (Js + 2) / (4 * Aj)
    cF = (Js - 2) * (Js + 1) / (Js + 2)
    qc = 4 * us * cs ** 2 - 2 * cs - (4 * us + 2 - Js ** 2)
    ok = [sp.simplify((Js + 2) / (4 * uF) - (4 + Js - Js ** 2) / Js - 1) == 0,
          sp.simplify(1 - Js / (4 * uF) - cF) == 0,
          sp.simplify(qc.subs({cs: cF, us: uF})) == 0,
          sp.simplify(sp.diff(qc, cs).subs({cs: cF, us: uF}) - 2 * Nj / Aj) == 0,
          sp.simplify(sp.discriminant(qc, cs).subs(us, uF) - 4 * Nj ** 2 / Aj ** 2) == 0,
          sp.simplify(sp.diff((Js + 2) / (4 * us ** 1) - (4 + Js - Js ** 2) / Js, us).subs(us, uF)) != 0]
    check("E4 flip node: cos 2 pi f3 = 1 and cos 2 pi x = c_F at u_f; q(c_F;u_f)=0, dq/dc = 2N/A, disc_c q (u_f) = 4N^2/A^2",
          all(ok), "so the line root c_F is simple iff N != 0; plane-(ii) pair is born from it at kappa_f (f3 = 0 there)")
    # u_f >= u_* : disc(u_f) >= 0 and u_f above the vertex -S/8 of disc(u)=64u^2+16 S u+4 on (2, 1+sqrt5)
    Sx = 2 - Js ** 2
    num = sp.numer(sp.together(uF + Sx / 8))
    pp = sp.Poly(sp.expand(num), Js)
    # compare against the denominator sign: A > 0 on (2, 1+sqrt5)
    cnt = pp.count_roots(2, sp.Rational(3236, 1000))
    val = pp.eval(sp.Rational(5, 2))
    check("E5 u_f lies above the vertex -S/8 of disc_c(q)(u) on (2, 1+sqrt5) (numerator sign, Sturm count)",
          cnt == 0 and val > 0, f"numerator has {cnt} roots in (2,3.236), value at 5/2 = {val}; with disc(u_f)=4N^2/A^2 >= 0 this gives u_f >= u_* with equality iff N = 0")


# ------------------------------------------------------------------------------------------------ numerical block (mpmath)
def node(J):
    J = mp.mpf(J)
    A = 4 + 2 * J - J ** 2
    cF = (J - 2) * (J + 1) / (J + 2)
    x = mp.acos(cF) / (2 * mp.pi)
    kf = mp.sqrt(J * (J + 2) * A) / (2 * A)
    return x, kf


class Setup:
    """E = 0 Schur complement S = A - B C^{-1} B' on the (fixed) kernel frame K of H(f0, kappa_f); analytic in complex (u,v,t,J,kappa)."""

    def __init__(s, J):
        s.J = mp.mpf(J)
        s.x, s.kf = node(J)
        s.f0 = [s.x, 1 - s.x, mp.mpf(0)]
        H0 = Hmat(s.f0, s.J, s.kf)
        ev, V = mp.eigh(H0)
        s.ev = [mp.re(e) for e in ev]
        s.K = V[:, 1:3]
        s.Q = mp.matrix(4, 2)
        s.Q[:, 0] = V[:, 0]
        s.Q[:, 1] = V[:, 3]
        s.Kd, s.Qd = s.K.H, s.Q.H

    def dvec(s, u, v, t, kap, J=None):
        J = s.J if J is None else J
        xi = [(u + v) / 2, (v - u) / 2, t]
        f = [s.f0[i] + xi[i] / (2 * mp.pi) for i in range(3)]
        H = Hmat(f, J, kap)
        A = s.Kd * H * s.K
        B = s.Kd * H * s.Q
        Bp = s.Qd * H * s.K
        C = s.Qd * H * s.Q
        Sm = A - B * (C ** -1) * Bp
        s0 = (Sm[0, 0] + Sm[1, 1]) / 2
        d1 = (Sm[0, 1] + Sm[1, 0]) / 2
        d2 = 1j * (Sm[0, 1] - Sm[1, 0]) / 2
        d3 = (Sm[0, 0] - Sm[1, 1]) / 2
        return s0, [d1, d2, d3]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def nrm(a):
    return mp.sqrt(dot(a, a))


def jac_cols(st, kap, h=None, J=None):
    h = mp.mpf(10) ** (-(mp.mp.dps // 3)) if h is None else h
    cols = []
    for k in range(3):
        e = [mp.mpf(0)] * 3
        e[k] = h
        dp = st.dvec(*e, kap, J)[1]
        e[k] = -h
        dm = st.dvec(*e, kap, J)[1]
        cols.append([mp.re((dp[i] - dm[i]) / (2 * h)) for i in range(3)])
    return cols


class Red:
    """Reduced scalar function phi(t, kappa): solve the two components of d along span(x_u, x_v) for (U, V), return the normal component."""

    def __init__(s, J):
        s.st = Setup(J)
        c = jac_cols(s.st, s.st.kf)
        s.xu, s.xv = c[0], c[1]
        nu = cross(s.xu, s.xv)
        s.nu = [x / nrm(nu) for x in nu]
        s.w1 = [x / nrm(s.xu) for x in s.xu]
        r = [s.xv[i] - dot(s.xv, s.w1) * s.w1[i] for i in range(3)]
        s.w2 = [x / nrm(r) for x in r]
        Jm = mp.matrix([[dot(s.w1, s.xu), dot(s.w1, s.xv)], [dot(s.w2, s.xu), dot(s.w2, s.xv)]])
        s.Ji = Jm ** -1

    def phi(s, t, kap, guess=(0, 0)):
        U, V = mp.mpmathify(guess[0]), mp.mpmathify(guess[1])
        for _ in range(80):
            _, d = s.st.dvec(U, V, t, kap)
            r = mp.matrix([dot(s.w1, d), dot(s.w2, d)])
            if mp.mnorm(r, 1) < mp.mpf(10) ** (-24) * max(1, abs(t) ** 3):
                break
            dd = s.Ji * r
            U -= dd[0]
            V -= dd[1]
        s0, d = s.st.dvec(U, V, t, kap)
        return dot(s.nu, d), U, V, s0


def winding(R, kap, rho, n):
    tot = mp.mpf(0)
    guess = (0, 0)
    prev = None
    for k in range(n + 1):
        t = rho * mp.expj(2 * mp.pi * k / n)
        ph, U, V, _ = R.phi(t, kap, guess)
        guess = (U, V)
        a = mp.arg(ph)
        if prev is not None:
            da = a - prev
            while da > mp.pi:
                da -= 2 * mp.pi
            while da < -mp.pi:
                da += 2 * mp.pi
            tot += da
        prev = a
    return tot / (2 * mp.pi)


def line_node_uvt(st, J, kap):
    """line node of the family nearest to c_F: (u,v,t) coordinates relative to the frame point f0."""
    uu = kap ** 2
    S_ = 2 - J ** 2
    disc = 1 + 4 * uu * (4 * uu + S_)
    cF = (J - 2) * (J + 1) / (J + 2)
    cands = [(1 + sg * mp.sqrt(disc)) / (4 * uu) for sg in (1, -1)]
    c = min(cands, key=lambda z: abs(z - cF))
    x = mp.acos(c) / (2 * mp.pi)
    return 4 * mp.pi * (x - st.x), mp.mpf(0), mp.mpf(0)


def plane_nodes_uvt(st, J, kap):
    uu = kap ** 2
    cx = 1 - J / (4 * uu)
    cf = (J + 2) / (4 * uu) - (4 + J - J ** 2) / J
    x = mp.acos(cx) / (2 * mp.pi)
    f3 = mp.acos(cf) / (2 * mp.pi)           # imaginary when cf > 1 (acos returns the principal complex value)
    u = 4 * mp.pi * (x - st.x)
    return [(u, mp.mpf(0), 2 * mp.pi * f3), (u, mp.mpf(0), -2 * mp.pi * f3)], cf


def detjac(st, pt, kap, J=None):
    h = mp.mpf(10) ** (-(mp.mp.dps // 3))
    cols = []
    for k in range(3):
        e = list(pt)
        e[k] = e[k] + h
        dp = st.dvec(*e, kap, J)[1]
        e[k] = e[k] - 2 * h
        dm = st.dvec(*e, kap, J)[1]
        cols.append([(dp[i] - dm[i]) / (2 * h) for i in range(3)])
    return mp.det(mp.matrix(cols))


def maxabs(v):
    return max(abs(x) for x in v)


def numeric_generic_J(Jr, tag):
    J = mp.mpf(Jr)
    N = J ** 3 - 4 * J - 4
    R = Red(Jr)
    st = R.st
    A = 4 + 2 * J - J ** 2
    # N0: node data
    check(f"N0[{tag}] H(f0,kappa_f) has levels 0,0,+-4J", abs(st.ev[1]) < 1e-30 and abs(st.ev[2]) < 1e-30 and abs(st.ev[3] - 4 * J) < 1e-30 and abs(st.ev[0] + 4 * J) < 1e-30)
    # N1: jets
    s0, d0 = st.dvec(0, 0, 0, st.kf)
    gram = [dot(R.xu, R.xv), nrm(R.xu), nrm(R.xv)]
    t_col = jac_cols(st, st.kf)[2]
    check(f"N1a[{tag}] d(node)=0, s0(node)=0, d_t(node)=0, Jacobian rank 2 (x_u,x_v orthogonal)",
          maxabs(d0) < 1e-30 and abs(s0) < 1e-30 and maxabs(t_col) < 1e-20 and abs(gram[0]) < 1e-15 * gram[1] * gram[2] and gram[1] > 1e-3 and gram[2] > 1e-3,
          f"|x_u|={mp.nstr(gram[1], 6)} |x_v|={mp.nstr(gram[2], 6)} cos={mp.nstr(gram[0] / gram[1] / gram[2], 3)}")
    ts = [mp.mpf("0.01"), mp.mpf("0.005")]
    rr = []
    uu_ = []
    for t in ts:
        ph, U, V, s0t = R.phi(t, st.kf)
        rr.append(mp.re(ph) / t ** 3)
        uu_.append(mp.re(U) / t ** 2)
    g_est = 2 * rr[1] - rr[0]
    u2_est = 2 * uu_[1] - uu_[0]
    gF = mp.sqrt(J ** 4 * (J + 2) / 8) / abs(N)
    u2F = mp.sqrt(A) * (J + 2) / (2 * N)
    check(f"N1b[{tag}] reduced function phi(t,kappa_f) = g t^3 + O(t^4), g != 0 (order exactly 3)",
          abs(abs(g_est) - gF) < 2e-3 * gF and abs(g_est) > 1e-2,
          f"g_est={mp.nstr(g_est, 8)}  landed-formula sqrt(J^4(J+2)/8)/|N|={mp.nstr(gF, 8)};  U/t^2 -> {mp.nstr(u2_est, 6)} vs sqrt(A)(J+2)/(2N)={mp.nstr(u2F, 6)}")
    # N2: slaving |s0| <= |d| at random real points near the node, kappa near kappa_f
    random.seed(7)
    worst = mp.mpf(0)
    ok = True
    for _ in range(25):
        pt = [mp.mpf(random.uniform(-0.15, 0.15)) for _ in range(3)]
        kap = st.kf * (1 + mp.mpf(random.uniform(-0.05, 0.05)))
        s0, d = st.dvec(*pt, kap)
        dn = nrm([mp.re(x) for x in d])
        ok = ok and (abs(mp.re(s0)) <= dn * (1 + mp.mpf(10) ** -25))
        worst = max(worst, abs(mp.re(s0)) / dn)
    check(f"N2[{tag}] slaving |s0| <= |d| at 25 random real points (consequence of det H >= 0, det C < 0)", ok, f"max |s0|/|d| = {mp.nstr(worst, 4)}")
    # N3: zero counts and family points, one eps of each sign
    rho = mp.mpf("0.14")
    Ttarget = mp.mpf("0.045")
    for sign in (+1, -1):
        c_t = mp.cos(Ttarget) if sign > 0 else mp.cosh(Ttarget)
        kap = mp.sqrt((J + 2) / (4 * (c_t + (4 + J - J ** 2) / J)))
        eps_sign = mp.sign(kap - st.kf)
        w = winding(R, kap, rho, 48)
        check(f"N3a[{tag},eps{'+' if sign > 0 else '-'}] argument principle: phi(.,kappa) has exactly 3 zeros in |t|<{mp.nstr(rho, 3)} (kappa/kappa_f-1={mp.nstr(kap / st.kf - 1, 4)})",
              eps_sign == sign and abs(w - 3) < 1e-6, f"winding = {mp.nstr(w, 8)}")
        L = line_node_uvt(st, J, kap)
        P, cf = plane_nodes_uvt(st, J, kap)
        pts = [L] + P
        dd = [st.dvec(*p, kap) for p in pts]
        zero_ok = all(maxabs(x[1]) < 1e-25 and abs(x[0]) < 1e-25 for x in dd)
        distinct = abs(P[0][2] - P[1][2]) > 1e-3 and abs(P[0][2]) > 1e-3
        tre = [mp.re(p[2]) for p in pts]
        tim = [mp.im(p[2]) for p in pts]
        if sign > 0:
            shape_ok = maxabs([mp.im(x) for x in tre]) < 1e-30 and all(abs(x) < 1e-30 for x in tim)
        else:
            shape_ok = abs(tre[1]) < 1e-30 and abs(tre[2]) < 1e-30 and abs(abs(tim[1]) - Ttarget) < 1e-12
        check(f"N3b[{tag},eps{'+' if sign > 0 else '-'}] line node and plane-(ii) pair are zeros of d with s0 = 0 (pair {'real' if sign > 0 else 'purely imaginary t = +-i y, y=arccosh c'})",
              zero_ok and distinct and shape_ok, "max |d|,|s0| over the three points < 1e-25; the three points are pairwise distinct")
        # nondegeneracy and degree
        if sign > 0:
            dj = [mp.re(detjac(st, p, kap)) for p in pts]
            sg = [int(mp.sign(x)) for x in dj]
            check(f"N3c[{tag},eps+] simple zeros; sign of det d_(u,v,t) at (line, pair) = {sg}, sum = +1 (local degree +1 conserved)",
                  all(x != 0 for x in sg) and sum(sg) == 1)
        else:
            dj = mp.re(detjac(st, L, kap))
            check(f"N3c[{tag},eps-] the single real zero (line node) is simple and has det d_(u,v,t) sign +1", mp.sign(dj) == 1, f"det={mp.nstr(dj, 5)}")
    return


def numeric_J0():
    mp.mp.dps = 60
    J0 = mp.findroot(lambda x: x ** 3 - 4 * x - 4, 2.38)
    st = Setup(J0)
    kf = st.kf
    J = J0
    h = mp.mpf(10) ** -14

    def D(a, b, c, k):
        return [mp.re(x) for x in st.dvec(a, b, c, k)[1]]

    def first(k):
        e = [0, 0, 0, 0]
        e[k] = h
        p = D(e[0], e[1], e[2], kf + e[3])
        e[k] = -h
        m = D(e[0], e[1], e[2], kf + e[3])
        return [(p[i] - m[i]) / (2 * h) for i in range(3)]

    def second(a, b):
        def ev(sa, sb):
            e = [0, 0, 0, 0]
            e[a] += sa * h
            e[b] += sb * h
            return D(e[0], e[1], e[2], kf + e[3])
        pp, pm, mpp, mm = ev(1, 1), ev(1, -1), ev(-1, 1), ev(-1, -1)
        return [(pp[i] - pm[i] - mpp[i] + mm[i]) / (4 * h * h) for i in range(3)]

    du, dv, dt, dk = first(0), first(1), first(2), first(3)
    duu, dut, dtt = second(0, 0), second(0, 2), second(2, 2)
    dkk_u = second(0, 3)
    s0, d0 = st.dvec(0, 0, 0, kf)
    check("N4a[J0] H(f0,kappa_f(J0)) levels 0,0,+-4J0; d(node)=0 and s0(node)=0 at the exceptional root",
          abs(st.ev[1]) < 1e-40 and abs(st.ev[2]) < 1e-40 and abs(st.ev[3] - 4 * J0) < 1e-40 and maxabs(d0) < 1e-50 and abs(s0) < 1e-50,
          f"J0={mp.nstr(J0, 20)}")
    check("N4b[J0] Jacobian rank 1: d_u = d_t = 0 (to 1e-25), d_v != 0", maxabs(du) < 1e-25 and maxabs(dt) < 1e-25 and nrm(dv) > 1,
          f"|d_v|={mp.nstr(nrm(dv), 8)}")
    e2 = [x / nrm(dv) for x in dv]
    # orthonormal basis of e2-perp from d_tt (orthogonal to d_v up to rounding, projected anyway) and e2 x e1
    pr = lambda w: [w[i] - dot(w, e2) * e2[i] for i in range(3)]
    e1 = [x / nrm(pr(dtt)) for x in pr(dtt)]
    e3 = cross(e2, e1)

    def qform(a):
        return (dot(a, duu) / 2, dot(a, dut), dot(a, dtt) / 2)     # alpha u^2 + beta u t + gamma t^2

    Q1, Q3 = qform(e1), qform(e3)
    res = (Q1[0] * Q3[2] - Q3[0] * Q1[2]) ** 2 - (Q1[0] * Q3[1] - Q3[0] * Q1[1]) * (Q1[1] * Q3[2] - Q3[1] * Q1[2])
    scale = max(abs(x) for x in Q1 + Q3) ** 4
    check("N4c[J0] 2-jet of the v-eliminated reduced map: two binary quadratic forms with nonzero resultant (no common complex tangent) => multiplicity 2*2 = 4",
          abs(res) > mp.mpf(10) ** -3 * scale,
          f"Q1 = ({mp.nstr(Q1[0], 7)} u^2 + {mp.nstr(Q1[1], 3)} ut + {mp.nstr(Q1[2], 7)} t^2), Q3 = ({mp.nstr(Q3[0], 3)} u^2 + {mp.nstr(Q3[1], 7)} ut + {mp.nstr(Q3[2], 3)} t^2), Res/scale={mp.nstr(res / scale, 6)}")
    cuu, ctt, cut = Q1[0], Q1[2], Q3[1]
    ceps = dot(e1, dk)
    off = [abs(Q1[1]), abs(Q3[0]), abs(Q3[2]), abs(dot(e2, duu)), abs(dot(e2, dtt)), abs(dot(e2, dut)), abs(dot(e2, dk)), abs(dot(e3, dk))]
    c_uu_landed = J0 ** 2 / (4 * (J0 + 2))
    check("N4d[J0] landed normal form reproduced: F1 = c_uu u^2 + c_tt t^2 + c_eps eps, F2 = b v, F3 = c_ut u t with c_uu = J0^2/(4(J0+2)), c_tt = 1/2, c_uu,c_tt > 0, c_eps < 0 (frame normalised |d_tt| = 1)",
          max(off) < 1e-25 and abs(cuu / ctt - 2 * c_uu_landed) < 1e-20 and abs(ctt - mp.mpf(1) / 2) < 1e-20 and ceps < 0 and cuu > 0,
          f"c_uu={mp.nstr(cuu, 10)} (landed {mp.nstr(c_uu_landed, 10)}), c_tt={mp.nstr(ctt, 10)}, c_eps={mp.nstr(ceps, 8)}, b={mp.nstr(nrm(dv), 8)}, c_ut={mp.nstr(abs(cut), 8)}; off-pattern entries <= {mp.nstr(max(off), 3)}")
    # N4e: family points at J0: eps>0 four real zeros with det signs (-,-,+,+); eps<0 four nonreal zeros of d
    S_ = 2 - J0 ** 2
    for rel in (mp.mpf("1e-6"), mp.mpf("-1e-6")):
        kap = kf * (1 + rel)
        uu = kap ** 2
        disc = 1 + 4 * uu * (4 * uu + S_)
        pts = []
        for sg in (1, -1):
            c = (1 + sg * mp.sqrt(disc)) / (4 * uu)
            x = mp.acos(c) / (2 * mp.pi)
            pts.append((4 * mp.pi * (x - st.x), mp.mpf(0), mp.mpf(0)))
        P, cf = plane_nodes_uvt(st, J0, kap)
        pts += P
        dd = [st.dvec(*p, kap) for p in pts]
        zero_ok = all(maxabs(x[1]) < 1e-40 and abs(x[0]) < 1e-40 for x in dd)
        sep = min(max(abs(pts[i][0] - pts[k][0]), abs(pts[i][2] - pts[k][2])) for i in range(4) for k in range(i + 1, 4))
        real = all(abs(mp.im(p[0])) < 1e-40 and abs(mp.im(p[2])) < 1e-40 for p in pts)
        if rel > 0:
            sg4 = [int(mp.sign(mp.re(detjac(st, p, kap)))) for p in pts]
            check(f"N4e[J0,eps+] four distinct REAL zeros (2 line + 2 plane-(ii)) of d with s0=0; det signs {sg4} sum 0 (local degree 0)",
                  zero_ok and real and sep > 1e-4 and sum(sg4) == 0 and sg4.count(1) == 2, f"separation {mp.nstr(sep, 4)}")
        else:
            check("N4e[J0,eps-] four distinct zeros of d (2 line, 2 plane-(ii)), all NON-real (complex family points), s0=0",
                  zero_ok and (not real) and sep > 1e-4 and all(abs(mp.im(p[0])) + abs(mp.im(p[2])) > 1e-6 for p in pts), f"separation {mp.nstr(sep, 4)}")
    # N4f: real-inequality for eps<0: F1 = c_uu u^2 + c_tt t^2 + |c_eps||eps| >0 on random small real points with v from e2-eq (finite check)
    random.seed(3)
    okp = True
    kap = kf * (1 - mp.mpf("1e-6"))
    for _ in range(30):
        pt = [mp.mpf(random.uniform(-0.01, 0.01)), mp.mpf(random.uniform(-0.01, 0.01)), mp.mpf(random.uniform(-0.01, 0.01))]
        dpt = [mp.re(x) for x in st.dvec(*pt, kap)[1]]
        okp = okp and (dot(e1, dpt) > 0 or abs(dot(e2, dpt)) > 1e-6)
    check("N4f[J0,eps-] finite check: at 30 random real points near the node either e1.d > 0 or |e2.d| > 1e-6 (finite sample, no real zero seen; not part of the proof)", okp)
    mp.mp.dps = 40


def two_parameter_pattern():
    """real family points near (J0, kappa_f(J0)) for J = J0 +- 0.004: counts 0 / 2 / 4 across u_* < u_f, and the family points are zeros of d (frames from P0)."""
    mp.mp.dps = 50
    J0 = mp.findroot(lambda x: x ** 3 - 4 * x - 4, 2.38)
    st = Setup(J0)
    allok_ = True
    detail = []
    for dJ in (mp.mpf("0.004"), mp.mpf("-0.004")):
        J = J0 + dJ
        A = 4 + 2 * J - J ** 2
        S_ = 2 - J ** 2
        uF = J * (J + 2) / (4 * A)
        ustar = (-S_ + mp.sqrt(S_ ** 2 - 4)) / 8
        order_ok = uF > ustar
        counts = []
        for u in (ustar * (1 - mp.mpf("2e-5")), (ustar + uF) / 2, uF * (1 + mp.mpf("2e-5"))):
            kap = mp.sqrt(u)
            disc = 1 + 4 * u * (4 * u + S_)
            pts = []
            for sg in (1, -1):
                c = (1 + sg * mp.sqrt(disc)) / (4 * u)
                x = mp.acos(c) / (2 * mp.pi)
                pts.append((4 * mp.pi * (x - st.x), mp.mpf(0), mp.mpf(0)))
            cx = 1 - J / (4 * u)
            cf = (J + 2) / (4 * u) - (4 + J - J ** 2) / J
            x = mp.acos(cx) / (2 * mp.pi)
            f3 = mp.acos(cf) / (2 * mp.pi)
            pts += [(4 * mp.pi * (x - st.x), mp.mpf(0), 2 * mp.pi * f3), (4 * mp.pi * (x - st.x), mp.mpf(0), -2 * mp.pi * f3)]
            zero_ok = all(maxabs(st.dvec(*p, kap, J)[1]) < 1e-30 and abs(st.dvec(*p, kap, J)[0]) < 1e-30 for p in pts)
            nreal = sum(1 for p in pts if abs(mp.im(p[0])) < 1e-30 and abs(mp.im(p[2])) < 1e-30)
            counts.append(nreal)
            allok_ = allok_ and zero_ok
        detail.append((mp.nstr(dJ, 3), counts, order_ok))
        allok_ = allok_ and order_ok and counts == [0, 2, 4]
    check("N5 two-parameter pattern near (J0,kappa_f(J0)), J=J0+-0.004: u_f > u_*, and the four family points are zeros of d (complex ones included) with 0 / 2 / 4 real ones for u<u_*, u_*<u<u_f, u>u_f",
          allok_, str(detail))
    mp.mp.dps = 40


def main():
    mp.mp.dps = 40
    exact_block()
    for Jr, tag in ((mp.mpf(13) / 6, "J=13/6"), (mp.mpf(5) / 2, "J=5/2"), (mp.mpf(3), "J=3")):
        numeric_generic_J(Jr, tag)
    numeric_J0()
    two_parameter_pattern()
    npass = sum(RES)
    nfail = len(RES) - npass
    emit(f"TOTAL: PASS={npass} FAIL={nfail}")
    if nfail == 0:
        emit("HIT: scoped conditional result: for each fixed J in (2,J0) or (J0,1+sqrt5) the zero-energy double-level (middle-band touching) set near the flipping line node is exactly {line node} for kappa<=kappa_f and {line node, plane-(ii) pair} for kappa>kappa_f, and near (J0,kappa_f(J0)) it is exactly the real points among the four line/plane-(ii) family points (0, 2, 4), given the supplied jets and conservation of multiplicity (ATTEMPT.md steps 2-11); radii non-constructive")
    emit("SUMMARY: re-verifies the supplied jets at J=13/6, 5/2, 3 and J0, shows the scalar part is slaved (|s0|<=|d|) and every family point (complex ones too) is a zero of the Schur vector, so multiplicity counts 3 (generic J) and 4 (J0) are saturated by the exact families; the census itself is the argument in ATTEMPT.md, not a finite search; runtime %.0f s" % (time.time() - T0))
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
