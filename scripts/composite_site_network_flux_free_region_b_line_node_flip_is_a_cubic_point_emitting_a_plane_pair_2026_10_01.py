#!/usr/bin/env python3
"""Composite-site network, supplied u = +1 quadratic Majorana comparator H = iM (landed hopping rules rebuilt below), Jx = Jy = 1, Jz = J, odd term kappa.
Region (b), Jz = J > Jx + Jy = 2: the line node f = (x, 1-x, 0) with cos 2 pi x = c_F = (J-2)(J+1)/(J+2) flips its charge +1 -> -1 at kappa_f^2 = u_f = J(J+2)/(4A),
A = 4 + 2J - J^2 (otri: larger root of R2; c1 flips for J < J0, c2 for J > J0, J0 = 2.38298 root of N = J^3 - 4J - 4; no flip for J >= 1 + sqrt5).  Nothing here is an axiom
of the framework: statements about a supplied model.  Coordinates xi = 2 pi (f - f0), u = xi1 - xi2, v = xi1 + xi2, t = xi3, eps = kappa - kappa_f, chi = sign T,
T = Im Tr(P d1H P d2H P d3H) (P kernel projector); Berry flux of the lowest two bands around a node = -chi.

EXACT (X1-X15; identities in the function field L = Q(J)(omega, Y), omega^2 = -A, Y^2 = J(J+2)A, kappa_f = Y/(2A), e^{2 pi i x} = (J+omega)^2/(2(J+2)), i.e. for every J at once;
 signs on (2, J0) and (J0, 1+sqrt5) by exact factorisation and Sturm counts; sympy/rational arithmetic, no floating point):
 X1-X3 flip node, its identification with the otri flip coupling and with the line root that flips, kernel projector.
 X4-X8 the exact Schur complement S = s0 + d.sigma at the double-zero kernel: d has no t-linear and no t^3 term, d_tt = -u2 d_u, with u' = u - u2 t^2
   d = x_u u' + x_v v + x_beta t^3 + (weighted order >= 4): mutually orthogonal, det[x_u, x_v, x_beta] > 0: a cubic (3,3,1) point of local degree +1; det H weight-6 part = 16J^2 |d0|^2;
   unfolding d = ... + x_beta (t^3 - mu eps t), mu = (J+2)/kappa_f^3 > 0: three nodes for eps > 0 (line chi -1, two off-line chi +1), one for eps < 0.
 X9-X11 the off-line pair is the plane-(ii) family (det H = 0 identically), positions to first order from the unfolding and exact series at J = 13/6, 5/2.
 X12-X15 the J0 event: weights (u:1, v:2, t:1, eps:2, delta = J - J0:1): F1 = c_uu u^2 + c_tt t^2 + a_d delta u + c_eps eps, F2 = b v, F3 = c_ut u t; local degree 0; four nodes born.
FLOAT (F1-F7; double precision, one 50-digit mpmath block; never certified): independent float Schur code, Fukui fluxes, grid searches of zeros, T(kappa), the J0 event, anisotropic couplings.
CAVEATS: (i) weighted-Taylor statements: the remainder beyond the stated weighted order has no explicit radius, and the Pauli-vector degree = Chern number link is the landed two-level
reduction; float fluxes support it; (ii) 'exactly three nodes near the flip' rests on the weighted degree argument and float grid searches, not on interval arithmetic;
(iii) the anisotropic statements are 50-digit/double numerics at five couplings; the vanishing of the quadratic term along the kernel direction is observed, not proved.
Prints [PASS]/[FAIL] lines and TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import sys
import time
from math import comb

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize
from sympy import QQ, ZZ
from sympy.polys.fields import field
from sympy.polys.matrices import DomainMatrix

AUDIT_TIMEOUT_SEC = 120

RESULTS = []
T0 = time.time()
VERBOSE = bool(os.environ.get("RBIRTH_VERBOSE"))
OUTCHARS = [0]


def emit(txt):
    OUTCHARS[0] += len(txt) + 1
    print(txt, flush=True)


def check(label, ok, note="", detail=""):
    """note: short result line, always printed; detail: printed on FAIL or with RBIRTH_VERBOSE=1."""
    RESULTS.append(bool(ok))
    emit(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {note}" if note else ""))
    if detail and (VERBOSE or not ok):
        emit("        " + detail)


def _hook(tp, val, tb):
    """backstop: a crash is reported as a FAIL line and the TOTAL line, never silently."""
    emit(f"[FAIL] runner exception {tp.__name__}: {str(val)[:160]}")
    RESULTS.append(False)
    emit(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")


sys.excepthook = _hook


def allok(conds):
    bad = [i for i, c_ in enumerate(conds) if not c_]
    return (not bad), (f" FAILED sub-conditions {bad}" if bad else "")


# ------------------------------------------------------------------------------------------------ network (landed rules, rebuilt)
AX = {"x": 0, "y": 1, "z": 2}


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
            q = list(p); q[a] += s_; q = tuple(q)
            if is_site(q):
                out.append(q)
    return out


REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]


def reduce_cell(p):
    """p = rep + n1 a1 + n2 a2 + n3 a3 (a1 = (2,0,0), a2 = (0,2,0), a3 = (1,1,2)); returns (rep index, n)."""
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    return REPS.index((x - 2 * n1, y - 2 * n2, z)), (n1, n2, n3)


def terms(J, kappa):
    """Real hopping terms (a, b, n, t): M(f)[a, b] += t e^{2 pi i f.n}, M(f)[b, a] -= t e^{-2 pi i f.n}, gauge u = +1 (H = i M)."""
    out = []
    for p in REPS:
        a, n0 = reduce_cell(p)
        assert n0 == (0, 0, 0) and is_site(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce_cell(q)
                out.append((a, b, n, 2.0 * J[AX[flavour(p, q)]]))
        if kappa:
            nb = {flavour(p, q): q for q in neighbours(p)}
            assert len(nb) == 3
            for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
                r1, n1 = reduce_cell(nb[l]); r2, n2 = reduce_cell(nb[m])
                out.append((r1, r2, tuple(int(v) for v in np.subtract(n2, n1)), 2.0 * kappa))
    return out


# amplitude tags: Jx, Jy, Jz, kappa = 1, 3, 7, 0.3 gives 2, 6, 14, 0.6
_KIND = {2.0: "x", 6.0: "y", 14.0: "z", 0.6: "odd"}
TERMS = [(int(a), int(b), tuple(int(v) for v in n), _KIND[round(float(t), 9)]) for (a, b, n, t) in terms((1.0, 3.0, 7.0), 0.3)]
assert len(TERMS) == 18


class Bloch:
    """Double-precision Bloch matrix H(f) = i M(f) for couplings J = (Jx, Jy, Jz) and odd term kappa."""

    def __init__(self, J, kappa):
        amp = {"x": 2 * J[0], "y": 2 * J[1], "z": 2 * J[2], "odd": 2 * kappa}
        self.a = np.array([t[0] for t in TERMS]); self.b = np.array([t[1] for t in TERMS])
        self.n = np.array([t[2] for t in TERMS], float); self.t = np.array([amp[t[3]] for t in TERMS])

    def H(self, F):
        F = np.atleast_2d(F)
        ph = np.exp(2j * np.pi * F @ self.n.T)
        Mk = np.zeros((len(F), 4, 4), complex)
        for j in range(len(self.t)):
            Mk[:, self.a[j], self.b[j]] += self.t[j] * ph[:, j]
            Mk[:, self.b[j], self.a[j]] -= self.t[j] * np.conj(ph[:, j])
        return 1j * Mk

    def levels(self, F, vecs=False):
        return np.linalg.eigh(self.H(F)) if vecs else np.linalg.eigvalsh(self.H(F))

    def detH(self, f):
        return float(np.linalg.det(self.H(np.asarray(f, float))[0]).real)

    def dH(self, f):
        """H and the three first derivatives dH/df_j at one point f (analytic)."""
        ph = np.exp(2j * np.pi * (self.n @ np.asarray(f, float)))
        M = np.zeros((4, 4), complex); dM = [np.zeros((4, 4), complex) for _ in range(3)]
        for j in range(len(self.t)):
            a, b = self.a[j], self.b[j]
            M[a, b] += self.t[j] * ph[j]; M[b, a] -= self.t[j] * np.conj(ph[j])
            for l in range(3):
                dM[l][a, b] += self.t[j] * ph[j] * 2j * np.pi * self.n[j, l]
                dM[l][b, a] -= self.t[j] * np.conj(ph[j]) * (-2j * np.pi * self.n[j, l])
        return 1j * M, [1j * d for d in dM]


def chi_T(B, f, tol=1e-6):
    """sign of T = Im Tr(P d1H P d2H P d3H), P the projector on the two levels nearest zero (the node chirality chi; Berry flux of the lowest two bands = -chi)."""
    try:
        H, dH = B.dH(f)
        ev, V = np.linalg.eigh(H)
    except (np.linalg.LinAlgError, ValueError):
        return 0, float("nan")
    if not (abs(ev[1]) < tol and abs(ev[2]) < tol):
        return 0, float("nan")                                   # not a node: reported as chi = 0 (the calling check fails)
    Pk = V[:, 1:3] @ V[:, 1:3].conj().T
    T = np.trace(Pk @ dH[0] @ Pk @ dH[1] @ Pk @ dH[2]).imag
    return int(np.sign(T)), T


def _link(A_, B_):
    return np.linalg.det(np.einsum('...ia,...ib->...ab', A_.conj(), B_))


def _plaquettes(V):
    links = (_link(V[:-1, :-1], V[1:, :-1]), _link(V[1:, :-1], V[1:, 1:]), _link(V[1:, 1:], V[:-1, 1:]), _link(V[:-1, 1:], V[:-1, :-1]))
    assert all(np.isfinite(z).all() and np.min(np.abs(z)) > 1e-12 for z in links), "singular occupied-band overlap"
    return np.angle(links[0] * links[1] * links[2] * links[3])


def sphere_chern(B, c, s, m=64, nocc=2):
    """Berry flux/2pi of the lowest nocc bands on the sphere |f - c| = s (outward), Fukui link method on a latitude-longitude grid;
    returns (flux, smallest middle gap met, largest plaquette phase)."""
    th = np.linspace(0, np.pi, m + 1)
    ph = np.linspace(0, 2 * np.pi, 2 * m + 1)
    Pp = np.stack([np.sin(th)[:, None] * np.cos(ph)[None, :], np.sin(th)[:, None] * np.sin(ph)[None, :],
                   np.cos(th)[:, None] * np.ones_like(ph)[None, :]], axis=-1) * s + np.asarray(c, float)
    try:
        ev, Vv = B.levels(Pp.reshape(-1, 3), vecs=True)
        Vv = Vv[:, :, :nocc].reshape(m + 1, 2 * m + 1, 4, nocc).copy()
        Vv[0, :] = Vv[0, 0]; Vv[-1, :] = Vv[-1, 0]; Vv[:, -1] = Vv[:, 0]
        pq = _plaquettes(Vv)
    except (AssertionError, np.linalg.LinAlgError, ValueError):
        return float("nan"), 0.0, 99.0                           # singular overlap: reported as an unresolved sphere (the calling check fails)
    return pq.sum() / (2 * np.pi), float((ev[:, 2] - ev[:, 1]).min()), float(np.abs(pq).max())


# ------------------------------------------------------------------------------------------------ exact field L = Q(J)(omega, Y)
# A = 4 + 2J - J^2 > 0 on (0, 1+sqrt5);  omega^2 = -A (omega = i W, W = sqrt(A) > 0);  Y^2 = J(J+2)A (Y = R W, R = sqrt(J(J+2)) > 0).
K0, Jf = field("J", QQ)
Af = 4 + 2 * Jf - Jf ** 2
Y2 = Jf * (Jf + 2) * Af
P2 = -Af                                                    # omega^2


class El:
    """a0 + a1 omega + a2 Y + a3 omega Y, a_i in K0 = Q(J); complex conjugation omega -> -omega (Y real)."""
    __slots__ = ("c",)

    def __init__(self, c0=0, c1=0, c2=0, c3=0):
        self.c = tuple(x if hasattr(x, "field") else K0(x) for x in (c0, c1, c2, c3))

    def __add__(s, o):
        o = o if isinstance(o, El) else El(o); return El(*(a + b for a, b in zip(s.c, o.c)))

    def __neg__(s):
        return El(*(-a for a in s.c))

    def __sub__(s, o):
        o = o if isinstance(o, El) else El(o); return El(*(a - b for a, b in zip(s.c, o.c)))

    def __mul__(s, o):
        if not isinstance(o, El):
            return El(*(a * o for a in s.c))
        a0, a1, a2, a3 = s.c; b0, b1, b2, b3 = o.c
        return El(a0 * b0 + a1 * b1 * P2 + a2 * b2 * Y2 + a3 * b3 * P2 * Y2,
                  a0 * b1 + a1 * b0 + (a2 * b3 + a3 * b2) * Y2,
                  a0 * b2 + a2 * b0 + (a1 * b3 + a3 * b1) * P2,
                  a0 * b3 + a3 * b0 + a1 * b2 + a2 * b1)

    def conj(s):
        return El(s.c[0], -s.c[1], s.c[2], -s.c[3])

    def is_zero(s):
        return all(a == 0 for a in s.c)

    def inv(s):
        a = (s.c[0], s.c[2]); b = (s.c[1], s.c[3])

        def m(x, y):
            return (x[0] * y[0] + x[1] * y[1] * Y2, x[0] * y[1] + x[1] * y[0])
        aa = m(a, a); bb = m(b, b)
        n = (aa[0] + Af * bb[0], aa[1] + Af * bb[1])
        dn = n[0] ** 2 - n[1] ** 2 * Y2
        ni = (n[0] / dn, -n[1] / dn)
        ra = m(a, ni); rb = m(b, ni)
        return El(ra[0], -rb[0], ra[1], -rb[1])

    def __pow__(s, e):
        if e < 0:
            return s.inv() ** (-e)
        r = El(1)
        for _ in range(e):
            r = r * s
        return r

    def __eq__(s, o):
        return (s - o).is_zero()


ZERO, ONE = El(0), El(1)
OMEGA, YY = El(0, 1, 0, 0), El(0, 0, 1, 0)
KIND = {"x": "xy", "y": "xy", "z": "z", "odd": "odd"}
XTERMS = [(a, b, n, KIND[k]) for (a, b, n, k) in TERMS]     # Jx = Jy = 1: both flavours carry amplitude 2
eta = El(Jf, 1, 0, 0)                                      # J + omega
z0 = eta * eta * (1 / (2 * (Jf + 2)))                      # e^{2 pi i x} at the flip node
z0i = eta.conj() * eta.conj() * (1 / (2 * (Jf + 2)))
KAPPA = El(0, 0, 1 / (2 * Af), 0)                          # kappa_f = Y/(2A)
amp = {"xy": El(2), "z": El(2 * Jf), "odd": KAPPA * 2}
ZP = {e: (z0 ** e if e >= 0 else z0i ** (-e)) for e in range(-12, 13)}
FACT = [1, 1, 2, 6, 24, 120, 720]


def mat0():
    return [[ZERO] * 4 for _ in range(4)]


def mmul(A_, B_):
    return [[sum((A_[r][k] * B_[k][c] for k in range(1, 4)), A_[r][0] * B_[0][c]) for c in range(4)] for r in range(4)]


def madd(A_, B_):
    return [[A_[r][c] + B_[r][c] for c in range(4)] for r in range(4)]


def msub(A_, B_):
    return [[A_[r][c] - B_[r][c] for c in range(4)] for r in range(4)]


def mscale(A_, s):
    return [[A_[r][c] * s for c in range(4)] for r in range(4)]


def mtr(A_):
    return A_[0][0] + A_[1][1] + A_[2][2] + A_[3][3]


def mzero(A_):
    return all(A_[r][c].is_zero() for r in range(4) for c in range(4))


def mconj_t(A_):
    return [[A_[c][r].conj() for c in range(4)] for r in range(4)]


def mident():
    return [[ONE if r == c else ZERO for c in range(4)] for r in range(4)]


def coeff_tensor(maxdeg, odd_only=False):
    """Taylor coefficients of M(zeta) at the node (z_j = z0_j e^{zeta_j}, node z = (z0, 1/z0, 1)); zeta1 = (zv + zu)/2, zeta2 = (zv - zu)/2, zeta3 = zt;
    {(a, b, c): 4x4 matrix} = coefficient of zu^a zv^b zt^c.  odd_only: d/d kappa of the odd terms (amplitude 2)."""
    out = {}
    for a in range(maxdeg + 1):
        for b in range(maxdeg + 1 - a):
            for c in range(maxdeg + 1 - a - b):
                Mx = mat0(); sgn = (-1) ** (a + b + c)
                for (r, s_, n, kind) in XTERMS:
                    if odd_only and kind != "odd":
                        continue
                    sc = (sp.Rational(n[0] - n[1], 2), sp.Rational(n[0] + n[1], 2), sp.Integer(n[2]))
                    f = sc[0] ** a * sc[1] ** b * sc[2] ** c / (FACT[a] * FACT[b] * FACT[c])
                    if f == 0:
                        continue
                    f = QQ.convert(f)
                    am = El(2) if odd_only else amp[kind]
                    Mx[r][s_] = Mx[r][s_] + am * ZP[n[0] - n[1]] * f
                    Mx[s_][r] = Mx[s_][r] - am * ZP[-(n[0] - n[1])] * (f * sgn)
                out[(a, b, c)] = Mx
    return out


def ratio(Mx, Nx):
    """g with Mx = g Nx (matrices over L), and whether the whole matrix identity holds."""
    for r in range(4):
        for c in range(4):
            if not Nx[r][c].is_zero():
                g = Mx[r][c] * Nx[r][c].inv()
                return g, mzero(msub(Mx, mscale(Nx, g)))
    return None, mzero(Mx)


Jx = sp.Symbol("J")
Wsym, Rsym = sp.symbols("W R", positive=True)
Nj = Jx ** 3 - 4 * Jx - 4                                   # N(J): zero at J0 = 2.38298 (root of J^3 - 4J - 4)
Aj = 4 + 2 * Jx - Jx ** 2                                   # A(J) > 0 on (-1.236, 3.236)
J0f = brentq(lambda x: x ** 3 - 4 * x - 4, 2.0, 3.0, xtol=1e-15)                    # J0 = 2.38298
PHI_S = 1 + sp.sqrt(5)                                      # phi * s with s = Jx + Jy = 2: upper end of region (b) flip range


def sgn_tab(expr):
    """(sign on (2, J0), sign on (J0, 1+sqrt5)) of a rational function of J; exact factorisation, Sturm counts for unknown factors; None if undecided."""
    num, den = sp.fraction(sp.cancel(sp.together(expr)))
    s_lo = s_hi = 1
    for part in (num, den):
        c0, fl = sp.factor_list(part, Jx)
        s_lo *= int(sp.sign(c0)); s_hi *= int(sp.sign(c0))
        for f_, mult in fl:
            if f_ in (Jx, Jx + 1, Jx + 2, Jx - 2):
                continue                                    # positive on (2, 1+sqrt5)
            if f_ == Nj:
                s_lo *= (-1) ** mult
                continue
            if f_ == Jx ** 2 - 2 * Jx - 4:                  # its real roots are 1 +- sqrt5: negative on (2, 1+sqrt5)
                s_lo *= (-1) ** mult; s_hi *= (-1) ** mult
                continue
            if sp.Poly(f_, Jx).count_roots(2, sp.Rational(33, 10)) != 0:
                return None
            sg = int(sp.sign(f_.subs(Jx, sp.Rational(5, 2)))) ** mult
            s_lo *= sg; s_hi *= sg
    return (s_lo, s_hi)


def sq(x):
    return sp.simplify(x)


def at1(e):
    return sp.nsimplify(e.as_expr().subs(Jx, 1)) if hasattr(e, "as_expr") else e


# ================================================================================================ EXACT 1: the flipping line node at Jx = Jy = 1, Jz = J
# line f = (x, 1-x, 0), c = cos 2 pi x, u = kappa^2; s = 2, P = 1, S = 2 - J^2:
#   q = 4u c^2 - 2P c - (4u+S),  F_c = P(s+J)c^2 + s(s^2+J s-2P)c + (1+J)^2 (s-J),  Fb = P c^2 + S c + P   (otri notation)
cs, us = sp.symbols("c u")
Sx = 2 - Jx ** 2
qL = 4 * us * cs ** 2 - 2 * cs - (4 * us + Sx)
FcL = (2 + Jx) * cs ** 2 + 4 * (1 + Jx) * cs + (1 + Jx) ** 2 * (2 - Jx)
FbL = cs ** 2 + Sx * cs + 1
uF = Jx * (Jx + 2) / (4 * Aj)
cF = (Jx - 2) * (Jx + 1) / (Jx + 2)
R2L = Jx ** 3 * (16 * Aj * us ** 2 + 8 * (2 - Jx ** 2) * us - Jx * (Jx + 2))          # iso form of the otri factor R2
resq = sp.factor(sp.resultant(qL, FcL, cs))
resb = sp.factor(sp.resultant(FcL, FbL, cs))
uminus = sp.cancel(-Jx * (Jx + 2) / (16 * Aj) / uF)                   # product of the roots C2/A2 divided by u_f
ok1, bad1 = allok([sp.simplify(qL.subs({cs: cF, us: uF})) == 0, sp.simplify(FcL.subs(cs, cF)) == 0,
                   sp.simplify(FcL - (Jx + 2) * (cs - cF) * (cs + Jx + 1)) == 0,
                   sp.simplify(-(2 * cF + Sx) / (4 * (1 - cF ** 2)) - uF) == 0,
                   sp.simplify(resq + (Jx + 2) * R2L) == 0, sp.simplify(R2L.subs(us, uF)) == 0, sp.simplify(uminus + sp.Rational(1, 4)) == 0,
                   sp.simplify(1 - cF - Aj / (Jx + 2)) == 0, sp.simplify(1 + cF - Jx ** 2 / (Jx + 2)) == 0])
ok1b = (sp.simplify(sp.diff(qL, cs).subs({cs: cF, us: uF}) - 2 * Nj / Aj) == 0 and sp.simplify(sp.diff(qL, us).subs({cs: cF}) + 4 * (1 - cF ** 2)) == 0)
sg_cF = sgn_tab(cF); sg_1c = sgn_tab(1 - cF); sg_uf = sgn_tab(uF)
check("X1 flip node u_f = J(J+2)/(4A), c_F = (J-2)(J+1)/(J+2)",
      ok1 and sg_cF == (1, 1) and sg_1c == (1, 1) and sg_uf == (1, 1) and ok1b, "q = F_c = 0; Res_c(q,F_c) = -(J+2) R2; u_f larger root; 0 < c_F < 1 on (2,1+sqrt5)" + bad1,
      f"Res_c(q,F_c) = {resq}; sign tables {sg_cF} {sg_1c} {sg_uf}; 1-c_F = A/(J+2), 1+c_F = J^2/(J+2), F_c = (J+2)(c-c_F)(c+J+1), other root of R2 = -1/4; dq/dc = 2N/A, dq/du = -4(1-c_F^2) at the node")
# which line root flips: Fb(c_F) = -J^2 N/(J+2)^2 (N = J^3-4J-4): c_F < c_b (c1 branch) iff N < 0; Res_c(F_c, Fb) = -J^4 (J+2) N (otri: -Jz^2 P (Jz+s) G, G = Jz^2 N)
ok2, bad2 = allok([sp.simplify(FbL.subs(cs, cF) + Jx ** 2 * Nj / (Jx + 2) ** 2) == 0, sp.simplify(resb + Jx ** 4 * (Jx + 2) * Nj) == 0,
                   sp.Poly(Nj, Jx).count_roots(2, 3) == 1, sp.Poly(Nj, Jx).is_irreducible, Nj.subs(Jx, 2) < 0, Nj.subs(Jx, PHI_S).simplify() > 0])
check("X2 flipping root: Fb(c_F) = -J^2 N/(J+2)^2",
      ok2, "c1 flips for 2<J<J0, c2 for J0<J<1+sqrt5; J0 = 2.38298 root of N = J^3-4J-4" + bad2,
      f"Res_c(F_c,Fb) = -J^4(J+2)N; N irreducible, one root in (2,3); N(2) = -4 < 0 < N(1+sqrt5) = {sp.simplify(Nj.subs(Jx, PHI_S))}")

# ================================================================================================ EXACT 2: node, kernel projector, Schur series (all J)
T = coeff_tensor(3)
M0 = T[(0, 0, 0)]
c16 = El(16 * Jf ** 2)
kc2 = KAPPA * KAPPA
c1 = (z0 + z0i) * QQ(1, 2)
u_ = kc2.c[0]
ok_node = (kc2 == El(Jf * (Jf + 2) / (4 * (4 + 2 * Jf - Jf ** 2))) and (z0 * z0i == ONE) and (z0i == z0.conj())
           and c1 == El((Jf - 2) * (Jf + 1) / (Jf + 2))
           and (kc2 * c1 * c1 * 4 - c1 * 2 + El(Jf ** 2 - 2) - kc2 * 4).is_zero()                                       # line equation q = 0
           and (1 - Jf / (4 * u_)) == (Jf - 2) * (Jf + 1) / (Jf + 2) and ((Jf + 2) / (4 * u_) - (4 + Jf - Jf ** 2) / Jf) == 1   # plane-(ii) cosines meet the line node, f3 = 0
           and (Jf * (Jf + 2) - 4 * u_ * (4 + 2 * Jf - Jf ** 2)) == 0)
M2 = mmul(M0, M0); M3 = mmul(M2, M0)
p1, p2, p3, p4 = mtr(M0), mtr(M2), mtr(M3), mtr(mmul(M2, M2))
E1 = p1; E2 = (E1 * p1 - p2) * QQ(1, 2); E3 = (E2 * p1 - E1 * p2 + p3) * QQ(1, 3); E4 = (E3 * p1 - E2 * p2 + E1 * p3 - p4) * QQ(1, 4)
I4 = mident()
P = mscale(madd(M2, mscale(I4, c16)), El(1 / (16 * Jf ** 2)))
G = mscale(M0, El(-1 / (16 * Jf ** 2)))
ok_spec = E1.is_zero() and E3.is_zero() and E4.is_zero() and E2 == c16 and mzero(madd(M0, mconj_t(M0)))
ok_proj = (mzero(mmul(M0, P)) and mzero(msub(mmul(P, P), P)) and mzero(msub(P, mconj_t(P))) and mtr(P) == El(2)
           and mzero(msub(mmul(G, M0), msub(I4, P))) and mzero(mmul(G, P)))
check("X3 node data and kernel projector (identities in J)",
      ok_node and ok_spec and ok_proj, "kappa_f = Y/(2A), levels 0,0,+-4J; J=13/6: kappa_f^2 = 325/524, J=5/2: 45/44",
      f"e^(2 pi i x) = (J+omega)^2/(2(J+2)), omega^2 = -A, Y^2 = J(J+2)A; P = (M0^2+16J^2)/(16J^2), G = -M0/(16J^2); J=1 test: kappa = sqrt15/10, z0 = (-2+i sqrt5)/3, levels 0,0,+-{sp.sqrt(at1(E2.c[0]))}")

MAXD = 3


def pm_mul(Aa, Bb, maxdeg=MAXD):
    out = {}
    for ka, ma in Aa.items():
        for kb, mb in Bb.items():
            k = (ka[0] + kb[0], ka[1] + kb[1], ka[2] + kb[2])
            if sum(k) > maxdeg:
                continue
            pr = mmul(ma, mb)
            out[k] = madd(out[k], pr) if k in out else pr
    return out


def pm_add(Aa, Bb, sB=1):
    out = dict(Aa)
    for k, m in Bb.items():
        mm = m if sB == 1 else mscale(m, El(-1))
        out[k] = madd(out[k], mm) if k in out else mm
    return out


Vp = {k: m for k, m in T.items() if sum(k) >= 1}
GP = {(0, 0, 0): G}; PP = {(0, 0, 0): P}
sand = lambda X: pm_mul(pm_mul(PP, X), PP)
VGV = pm_mul(pm_mul(Vp, GP), Vp); VGVGV = pm_mul(pm_mul(pm_mul(pm_mul(Vp, GP), Vp), GP), Vp)
S = pm_add(pm_add(sand(Vp), sand(VGV), -1), sand(VGVGV), 1)
S = {k: m for k, m in S.items() if not mzero(m)}
get = lambda k: S.get(k, mat0())
Su, Sv, St, Stt, Sut, Sttt = get((1, 0, 0)), get((0, 1, 0)), get((0, 0, 1)), get((0, 0, 2)), get((1, 0, 1)), get((0, 0, 3))
Suu = get((2, 0, 0))

# unfolding jets (weights u:2, v:3, t:1, eps:2 for the cubic form; eps-jet needed at weight <= 3)
WT = (2, 3, 1, 2); MAXW = 3
TK = coeff_tensor(3, odd_only=True)
wt = lambda k: sum(w * e for w, e in zip(WT, k))
V4 = {}
for k, m in T.items():
    if sum(k) >= 1 and wt(k + (0,)) <= MAXW:
        V4[k + (0,)] = m
for k, m in TK.items():
    if wt(k + (1,)) <= MAXW:
        V4[k + (1,)] = m


def pm4_mul(Aa, Bb):
    out = {}
    for ka, ma in Aa.items():
        for kb, mb in Bb.items():
            k = tuple(x + y for x, y in zip(ka, kb))
            if wt(k) > MAXW:
                continue
            pr = mmul(ma, mb)
            out[k] = madd(out[k], pr) if k in out else pr
    return out


Z4 = (0, 0, 0, 0)
G4 = {Z4: G}; P4 = {Z4: P}
s4 = lambda X: pm4_mul(pm4_mul(P4, X), P4)
VGV4 = pm4_mul(pm4_mul(V4, G4), V4); VGVGV4 = pm4_mul(pm4_mul(pm4_mul(pm4_mul(V4, G4), V4), G4), V4)
S4 = dict(s4(V4))
for k, m in s4(VGV4).items():
    S4[k] = madd(S4[k], mscale(m, El(-1))) if k in S4 else mscale(m, El(-1))
for k, m in s4(VGVGV4).items():
    S4[k] = madd(S4[k], m) if k in S4 else m
S4 = {k: m for k, m in S4.items() if not mzero(m)}
Se, Set = S4[(0, 0, 0, 1)], S4[(0, 0, 1, 1)]

# ---- sign tables on (2, J0) and (J0, 1+sqrt5)
Aj_ = Aj
fx = {"a2": Nj ** 2 / ((Jx + 2) ** 2 * Aj_), "b2": 2 * Jx ** 3 * (Jx + 1) ** 2 / ((Jx + 2) ** 2 * Aj_),
      "g2": Jx ** 4 * (Jx + 2) / (8 * Nj ** 2), "mu/Y": 8 * Aj_ / (Jx ** 2 * (Jx + 2)),
      "det/WY": Jx ** 3 * (Jx + 1) / (2 * (Jx + 2) ** 2 * Aj_ ** 2), "u2/W": (Jx + 2) / (2 * Nj)}
SG = {k: sgn_tab(v_) for k, v_ in fx.items()}
sg2 = {k_: int(sp.sign(v_.subs(Jx, 2))) for k_, v_ in fx.items()}                # exact signs at the boundary J = 2 (Jz = Jx + Jy)
ok_J2 = all(sg2[k_] == 1 for k_ in ('a2', 'b2', 'g2', 'det/WY', 'mu/Y')) and sg2['u2/W'] == -1



def cf_vals(Jv):
    A = 4 + 2 * Jv - Jv ** 2; W = np.sqrt(A); N = Jv ** 3 - 4 * Jv - 4; Y = np.sqrt(Jv * (Jv + 2) * A)
    return (f"J={Jv:.4f}: kappa_f={Y / (2 * A):.6f} x_F={np.arccos((Jv - 2) * (Jv + 1) / (Jv + 2)) / (2 * np.pi):.6f} a={abs(N) / ((Jv + 2) * W):.6f} b={Jv * (Jv + 1) * np.sqrt(2 * Jv) / ((Jv + 2) * W):.6f} "
            f"g={Jv ** 2 * np.sqrt(Jv + 2) / (2 * np.sqrt(2) * abs(N)):.6f} u2={W * (Jv + 2) / (2 * N):+.6f} mu={8 * Y * A / (Jv ** 2 * (Jv + 2)):.6f} N={N:+.5f}")


CF_TXT = "; ".join(cf_vals(Jv_) for Jv_ in (13 / 6, 5 / 2, 2.2, 3.0))

# ---- X4: vanishing structure
ok_van = (mzero(St) and mzero(Sttt) and all(mtr(X).is_zero() for X in (Su, Sv, Stt, Sut, Suu, Se)))
g, okg = ratio(Stt, Su)
check("X4 Schur jets: no t-linear, no t^3, no identity part",
      ok_van and okg and g == El(0, (Jf + 2) / (2 * (Jf ** 3 - 4 * Jf - 4)), 0, 0) and SG['u2/W'] == (-1, 1), f"d_tt = -u2 d_u, u2 = W(J+2)/(2N): sign {SG['u2/W']} on (2,J0),(J0,1+sqrt5)",
      f"identities in J (no sign input); {len(S)} nonzero monomials u^a v^b t^c; identity part vanishes for u, v, uu, ut, tt, eps")

# ---- X5: Gram data
Sb = madd(Sttt, mscale(Sut, -g))
tr2 = lambda A_, B_: mtr(mmul(A_, B_))
tr3 = lambda A_, B_, C_: mtr(mmul(mmul(A_, B_), C_))
a2 = (Jf ** 3 - 4 * Jf - 4) ** 2 / ((Jf + 2) ** 2 * Af)
b2 = 2 * Jf ** 3 * (Jf + 1) ** 2 / ((Jf + 2) ** 2 * Af)
g2 = Jf ** 4 * (Jf + 2) / (8 * (Jf ** 3 - 4 * Jf - 4) ** 2)
ok_herm = all(mzero(msub(X, mconj_t(X))) and mtr(X).is_zero() for X in (Su, Sv, Sb))
ok_gram = (tr2(Su, Su) * QQ(1, 2) == El(a2) and tr2(Sv, Sv) * QQ(1, 2) == El(b2) and tr2(Sb, Sb) * QQ(1, 2) == El(g2)
           and tr2(Su, Sv).is_zero() and tr2(Su, Sb).is_zero() and tr2(Sv, Sb).is_zero())
T3 = tr3(Su, Sv, Sb)
ok_det = (T3 == El(0, Jf ** 3 * (Jf + 1) / ((Jf + 2) ** 2 * Af ** 2), 0, 0) * YY
          and a2 * b2 * g2 == Jf ** 7 * (Jf + 1) ** 2 / (4 * (Jf + 2) ** 3 * Af ** 2))
check("X5 x_u, x_v, x_beta orthogonal; a^2, b^2, g^2, det exact",
      ok_herm and ok_gram and ok_det, f"signs on (2,J0),(J0,1+sqrt5): a2 {SG['a2']} b2 {SG['b2']} g2 {SG['g2']} det {SG['det/WY']}",
      "a^2 = N^2/((J+2)^2 A), b^2 = 2J^3(J+1)^2/((J+2)^2 A), g^2 = J^4(J+2)/(8N^2), det[x_u,x_v,x_beta] = W Y J^3(J+1)/(2(J+2)^2 A^2)")

# ---- X6: D = det H, weights (3,3,1)
RD, Jr, kap, z1, z2, z3 = sp.ring("Jr,kap,z1,z2,z3", ZZ)
dom = RD.to_domain()
S0 = 2
tag = {"xy": RD(2), "z": 2 * Jr, "odd": 2 * kap}
Ms = [[RD(0)] * 4 for _ in range(4)]
for (a, b, n, kind) in XTERMS:
    Ms[a][b] += tag[kind] * z1 ** (S0 + n[0]) * z2 ** (S0 + n[1]) * z3 ** (S0 + n[2])
    Ms[b][a] -= tag[kind] * z1 ** (S0 - n[0]) * z2 ** (S0 - n[1]) * z3 ** (S0 - n[2])
Dp = DomainMatrix([[dom.convert(x) for x in row] for row in Ms], (4, 4), dom).det()           # det H z^(4 S0); det H = det M since i^4 = 1
KP = [ONE, KAPPA, KAPPA * KAPPA, KAPPA * KAPPA * KAPPA, KAPPA * KAPPA * KAPPA * KAPPA]
group = {}
for mon, co in Dp.terms():
    jp, kp, a1, a2_, a3 = mon
    e = (a1 - 4 * S0, a2_ - 4 * S0, a3 - 4 * S0)
    group[e] = group.get(e, ZERO) + KP[kp] * (Jf ** jp) * int(co)
Te = {e: c_ * ZP[e[0] - e[1]] for e, c_ in group.items()}
Dco = {}
for a in range(7):
    for b in range(7 - a):
        for c in range(7 - a - b):
            acc = ZERO
            for e, t_ in Te.items():
                f = sp.Rational(e[0] - e[1], 2) ** a * sp.Rational(e[0] + e[1], 2) ** b * sp.Integer(e[2]) ** c / (FACT[a] * FACT[b] * FACT[c])
                if f != 0:
                    acc = acc + t_ * QQ.convert(f)
            Dco[(a, b, c)] = acc


def Dreal(k):
    return Dco[k] * ((-1) ** (sum(k) // 2))


def Dodd(k):
    assert Dco[k].c[0] == 0 and Dco[k].c[2] == 0
    return El(Dco[k].c[1], 0, Dco[k].c[3], 0) * ((-1) ** ((sum(k) + 1) // 2))


ok_D0 = Dco[(0, 0, 0)].is_zero() and all(Dco[k].is_zero() for k in ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
hess_ok = (Dreal((2, 0, 0)) == El(16 * Jf ** 2 * a2) and Dreal((0, 2, 0)) == El(16 * Jf ** 2 * b2)
           and all(Dreal(k).is_zero() for k in ((0, 0, 2), (1, 1, 0), (1, 0, 1), (0, 1, 1))))
s2f = (Jf + 2) / (2 * (Jf ** 3 - 4 * Jf - 4))
lowD = [k for k, v_ in Dco.items() if not v_.is_zero() and 2 * k[0] + 3 * k[1] + k[2] < 4]
ok_lin = (not lowD and Dodd((1, 0, 2)) == El(-2 * s2f * 16 * Jf ** 2 * a2) and Dreal((0, 0, 4)) == El(s2f ** 2 * Af * 16 * Jf ** 2 * a2))
gs = -g
Wd = {}
for (a, b, c), co in Dco.items():
    if co.is_zero():
        continue
    for m in range(a + 1):
        w_ = 3 * m + 3 * b + c + 2 * (a - m)
        if w_ > 6:
            continue
        key = (m, b, c + 2 * (a - m))
        Wd[key] = Wd.get(key, ZERO) + co * (gs ** (a - m)) * comb(a, m)
byw = {}
for (i, j, k), co in Wd.items():
    if not co.is_zero():
        byw.setdefault(3 * i + 3 * j + k, {})[(i, j, k)] = co
pred6 = {(2, 0, 0): tr2(Su, Su) * (-8 * Jf ** 2), (0, 2, 0): tr2(Sv, Sv) * (-8 * Jf ** 2), (0, 0, 6): tr2(Sb, Sb) * (-8 * Jf ** 2)}
w6 = byw.get(6, {})
ok_w6 = (all(w_ not in byw for w_ in range(6)) and all(k in pred6 for k in w6) and all((w6.get(k, ZERO) - v_).is_zero() for k, v_ in pred6.items()))
check("X6 det H weights (3,3,1): order 6 = 16J^2 |d0|^2",
      ok_D0 and ok_lin and hess_ok and ok_w6, "orders 0-5 vanish, Hessian rank 2 (kernel t); independent of the Schur route",
      "c = 16 J^2; exact Laurent determinant (175 monomials); weights (2,3,1): leading c a^2 (u-u2 t^2)^2; D > 0 on a punctured weighted neighbourhood")

# ---- X7: local degree +1 on both sub-intervals
orient = sp.Matrix([[1, -1], [1, 1]]).det()
okdeg = all(SG[k] == (1, 1) for k in ("a2", "b2", "g2", "det/WY")) and ok_det and ok_gram and orient == 2
check("X7 cubic (3,3,1) point at the flip, local degree +1",
      okdeg and ok_J2, "2<J<J0, J0<J<1+sqrt5 and J=2: d = x_u u' + x_v v + x_beta t^3 + higher, u' = u - u2 t^2",
      f"Jacobian of (u',v,t) -> d0 = 3 a b g t^2 >= 0 in the right-handed frame (x_u/a, x_v/b, x_beta/g), a g > 0; sign T > 0; (u,v)->(xi1,xi2) Jacobian 2; signs at J=2: {sg2}; closed forms: {CF_TXT}")

# ---- X8: unfolding in kappa
rho, okr = ratio(Se, Su)
epst = madd(Set, mscale(Sut, -rho))
mu, okm = ratio(epst, Sb)
mu_exp = El(8 * Af / (Jf ** 2 * (Jf + 2))) * YY
rho_exp = El(0, 4 * Jf / ((Jf + 2) * (Jf ** 3 - 4 * Jf - 4)), 0, 0) * YY
mus = sp.Symbol("mu", positive=True); tt = sp.Symbol("t", real=True)
charges = {}
for esg in (1, -1):
    nodes = [r for r in sp.solve(tt ** 3 - mus * esg * tt, tt) if r.is_real]
    charges[esg] = sorted(int(SG["det/WY"][0] * sp.sign((3 * tt ** 2 - mus * esg).subs(tt, r))) for r in nodes)
ok_unf = (set(S4.keys()) == {(0, 0, 2, 0), (1, 0, 0, 0), (0, 0, 0, 1), (0, 1, 0, 0), (0, 0, 1, 1), (1, 0, 1, 0)}
          and okr and rho == rho_exp and mtr(Se).is_zero() and okm and mu == mu_exp and mtr(epst).is_zero() and sgn_tab(fx["mu/Y"]) == (1, 1)
          and charges[1] == [-1, 1, 1] and charges[-1] == [1])
check("X8 unfolding d = ... + x_beta (t^3 - mu eps t), mu = (J+2)/kappa_f^3 > 0",
      ok_unf, "eps>0: three nodes chi (-,+,+) (line, emitted pair at t = +-sqrt(mu eps)); eps<0: one node chi +",
      f"mu = 8YA/(J^2(J+2)); charges eps>0 {charges[1]}, eps<0 {charges[-1]}; mu/Y sign {sgn_tab(fx['mu/Y'])}; total chi +1 on both sides")


# ================================================================================================ EXACT 3: plane-(ii) family, first order, exact series
# ---- X9: det H vanishes identically on the plane-(ii) family f = (x, 1-x, f3): cos 2 pi x = 1 - J/(4u), cos 2 pi f3 = (J+2)/(4u) - (4+J-J^2)/J (u = kappa^2)
KF, Jk, kk = field("J,k", QQ)
grp = {}
for mon, co in Dp.terms():
    jp, kp, a1_, a2_, a3_ = mon
    key = (a1_ - a2_, a3_ - 4 * S0)                                   # z2 = 1/z1 on the family: z1^(e1-e2) z3^e3
    grp[key] = grp.get(key, KF(0)) + int(co) * Jk ** jp * kk ** kp
uk = kk * kk
c1f = 1 - Jk / (4 * uk)
c3f = (Jk + 2) / (4 * uk) - (4 + Jk - Jk * Jk) / Jk


def powtab(cc, Nmax):
    """z^n = a_n z + b_n modulo z^2 - 2 cc z + 1, n in [-Nmax, Nmax]."""
    tab = {0: (KF(0), KF(1)), 1: (KF(1), KF(0)), -1: (KF(-1), 2 * cc)}
    for n in range(2, Nmax + 1):
        a, b = tab[n - 1]; tab[n] = (2 * cc * a + b, -a)
        a, b = tab[-(n - 1)]; tab[-n] = (-b, a + 2 * cc * b)
    return tab


t1_ = powtab(c1f, max(abs(k[0]) for k in grp)); t3_ = powtab(c3f, max(abs(k[1]) for k in grp))
acc = {(1, 1): KF(0), (1, 0): KF(0), (0, 1): KF(0), (0, 0): KF(0)}
for (e1, e3), Pq in grp.items():
    ia, ib = t1_[e1]; ja, jb = t3_[e3]
    acc[(1, 1)] += Pq * ia * ja; acc[(1, 0)] += Pq * ia * jb; acc[(0, 1)] += Pq * ib * ja; acc[(0, 0)] += Pq * ib * jb
ok_fam = all(v_ == 0 for v_ in acc.values()) and all(grp.get(k, KF(0)) == grp.get((-k[0], -k[1]), KF(0)) for k in grp)
c3_ge = sp.simplify((Jx + 2) / (4 * us) - (4 + Jx - Jx ** 2) / Jx - 1)
check("X9 det H = 0 identically on the plane-(ii) family",
      ok_fam and sgn_tab((4 - Jx ** 2) / Jx) == (-1, -1), "all (J, kappa); real for every kappa >= kappa_f when 2<J<1+sqrt5",
      f"reduction of the Laurent determinant modulo z1^2 - 2c1 z1 + 1, z3^2 - 2c3 z3 + 1: all four coefficients vanish ({len(grp)} (e1,e3) classes); reality: cos 2 pi x = 1 - J/(4u) rises from c_F in (0,1), cos 2 pi f3 falls from 1 at u_f to -(4+J-J^2)/J >= -1 (J > 2)")

# ---- X10: first-order consistency with the landed closed forms (identities in J)
mu_f = El(Jf + 2) * (KAPPA * KAPPA * KAPPA).inv()
W_sin = El(0, Jf / (Jf + 2), 0, 0)                                  # i sin 2 pi x = omega J/(J+2)
dd = (4 + 4 * Jf - Jf ** 3) / (4 + 2 * Jf - Jf ** 2)
d_c_ok = El(dd * dd) == (El(1) + kc2 * 8 + kc2 * kc2 * 16 - kc2 * (4 * Jf ** 2))
dprime = (KAPPA * 16 + KAPPA * KAPPA * KAPPA * 64 - KAPPA * (8 * Jf ** 2)) * QQ(1, 2) * (1 / dd)
num = (-(dprime) * (kc2 * 4)) - (El(1) - El(dd)) * (KAPPA * 8)
dcos_line_landed = num * (1 / (16 * kc2.c[0] ** 2))
dcos_line_pred = W_sin * (-rho) * QQ(1, 2)
dcos_plane_pred = W_sin * (-rho + gs * (-mu)) * QQ(1, 2)
dcos_plane_landed = El(Jf) * (KAPPA * KAPPA * KAPPA * 2).inv()
ok_first = (mu_f == mu_exp and d_c_ok and (dcos_line_landed - dcos_line_pred).is_zero() and (dcos_plane_landed - dcos_plane_pred).is_zero())
check("X10 first-order shifts from the unfolding = d/dkappa of the closed forms",
      ok_first, "(2 pi f3)^2 = mu eps; cos 2 pi x (line, plane) agree; identities in J",
      "plane nodes sit on u = u2 t^2 - rho eps, v = 0, line node at u = -rho eps; dcos(plane)/dk = J/(2 k^3)")

# ---- X11: exact series of the three nodes at J = 13/6 and 5/2
ee = sp.Symbol("e", positive=True)
SERIES = {}
ok_ser = True
ser_note = []
for Jv in (sp.Rational(13, 6), sp.Rational(5, 2)):
    Av = 4 + 2 * Jv - Jv ** 2; ufv = Jv * (Jv + 2) / (4 * Av); k0 = sp.sqrt(ufv); Wv = sp.sqrt(Av); Nv = Jv ** 3 - 4 * Jv - 4
    kap_e = k0 + ee; ue = kap_e ** 2
    cF_v = (Jv - 2) * (Jv + 1) / (Jv + 2)
    c3e = (Jv + 2) / (4 * ue) - (4 + Jv - Jv ** 2) / Jv
    yv = sp.series(1 - c3e, ee, 0, 4).removeO()
    th2 = sp.series(2 * yv + yv ** 2 / 3 + 4 * yv ** 3 / 45, ee, 0, 4).removeO()                        # acos(1-y)^2 through y^3
    mu_c = [sp.simplify(th2.coeff(ee, k_)) for k_ in (1, 2, 3)]
    cpe = sp.series(1 - Jv / (4 * ue), ee, 0, 3).removeO()
    dcp = sp.expand(cpe - cF_v)
    sinF = Jv * Wv / (Jv + 2); cosF = cF_v
    d1, d2 = dcp.coeff(ee, 1), dcp.coeff(ee, 2)
    lam_e = [sp.simplify(-d1 / sinF), sp.simplify(-d2 / sinF - cosF * d1 ** 2 / (2 * sinF ** 3))]              # coefficients of e, e^2 in acos(cp) = 2 pi x_e - 2 pi x_F
    root_l = sp.solve(4 * ue * cs ** 2 - 2 * cs - (4 * ue + 2 - Jv ** 2), cs)
    cl = min(root_l, key=lambda r_: abs(float(r_.subs(ee, 0)) - float(cF_v)))
    dcl = sp.series(cl, ee, 0, 3).removeO() - cF_v
    l1, l2 = sp.simplify(dcl.coeff(ee, 1)), sp.simplify(dcl.coeff(ee, 2))
    lam_l = [sp.simplify(-l1 / sinF), sp.simplify(-l2 / sinF - cosF * l1 ** 2 / (2 * sinF ** 3))]
    muX = (Jv + 2) / k0 ** 3
    lam_e_cf = sp.simplify(-(Jv + 2) / (2 * k0 ** 3 * Wv)); lam_l_cf = sp.simplify(-4 * k0 * Av * Jv * Wv / ((Jv + 2) * Nv))      # closed forms of d(2 pi x)/dkappa: -(J+2)/(2 k^3 W), -4 k A J W/((J+2) N)
    okj = (sp.simplify(mu_c[0] - muX) == 0 and sp.simplify(lam_e[0] - lam_e_cf) == 0 and sp.simplify(lam_l[0] - lam_l_cf) == 0)
    okj = okj and sp.simplify(2 * (lam_e[0] - lam_l[0]) - Wv * (Jv + 2) / (2 * Nv) * muX) == 0         # u_e - u_line = u2 mu eps at leading order (u = 2 * (2 pi dx))
    # numeric residual of the series against the exact closed forms at two small eps (the residual must scale like e^3)
    mp.mp.dps = 40
    resid = []
    for eps_ in (mp.mpf("1e-4"), mp.mpf("2e-4")):
        kk_ = mp.sqrt(mp.mpf(ufv.p) / ufv.q) + eps_
        uu_ = kk_ ** 2; Jm = mp.mpf(Jv.p) / Jv.q
        c3m = (Jm + 2) / (4 * uu_) - (4 + Jm - Jm ** 2) / Jm
        ex = mp.acos(c3m) ** 2
        ap = sum(mp.mpf(sp.N(mc_, 40)) * eps_ ** (i_ + 1) for i_, mc_ in enumerate(mu_c))
        resid.append(abs(ex - ap))
    okj = okj and 12 < resid[1] / resid[0] < 20                      # series complete through e^3: the residual is O(e^4), ratio 16
    ok_ser = ok_ser and okj
    SERIES[str(Jv)] = dict(k0=k0, mu=mu_c, lam_e=lam_e, lam_l=lam_l, xF=sp.acos(cF_v) / (2 * sp.pi))
    ser_note.append(f"J={Jv}: kappa_f={float(k0):.6f} mu={float(mu_c[0]):.5f} mu2={float(mu_c[1]):.4f} lam_e={float(lam_e[0] / (2 * sp.pi)):.5f} lam_l={float(lam_l[0] / (2 * sp.pi)):.5f}")
check("X11 exact series of the three nodes at J = 13/6, 5/2",
      ok_ser, "; ".join(ser_note), "(2 pi f3)^2 = mu e + mu2 e^2 + ...; 2 pi x_e, 2 pi x_line = 2 pi x_F + lam e + lam2 e^2; u_e - u_line = u2 mu e; exact radical forms in the verbose log")
SER_LOG = {k_: {kk2: [str(sp.simplify(x_)) for x_ in vv] if isinstance(vv, list) else str(sp.simplify(vv)) for kk2, vv in dd_.items()} for k_, dd_ in SERIES.items()}

if VERBOSE:
    emit("        exact series data (kappa_f, [mu, mu2, mu3] of (2 pi f3)^2, [lam, lam2] of 2 pi x_e and 2 pi x_line, x_F): " + str(SER_LOG))


# ================================================================================================ EXACT 4: the J0 event (N = J^3 - 4J - 4 = 0), local form at weights (u:1, v:2, t:1, eps:2, delta = J - J0:1)
def real_val(tr, dsum):
    """x.y = tr(H_x H_y)/2 = -i^dsum tr(Sigma_x Sigma_y)/2 with H_m = i^(|m|+1) Sigma_m (real); tr in L -> sympy expression in J, W, R (W^2 = A, R^2 = J(J+2), Y = R W)."""
    c0, c1_, c2_, c3_ = [sp.factor(x.as_expr()) for x in tr.c]
    Y_ = Rsym * Wsym
    if dsum % 2 == 0:
        assert c1_ == 0 and c3_ == 0
        return sp.factor(-((-1) ** (dsum // 2)) * (c0 + c2_ * Y_) / 2)
    assert c0 == 0 and c2_ == 0
    return sp.factor(-((-1) ** ((dsum + 1) // 2)) * Wsym * (c1_ + c3_ * Y_) / 2)


gram = lambda X, dX, Z, dZ: real_val(tr2(X, Z), dX + dZ)
Stt_, Se_, Suu_ = Stt, Se, Suu
g_uu, g_u_uu, g_uu_uu = gram(Su, 1, Su, 1), gram(Su, 1, Suu, 2), gram(Suu, 2, Suu, 2)
g_u_tt, g_tt_tt, g_u_e, g_e_e = gram(Su, 1, Stt, 2), gram(Stt, 2, Stt, 2), gram(Su, 1, Se, 0), gram(Se, 0, Se, 0)
g_ut_ut, g_ut_u, g_ut_v, g_ut_ttt = gram(Sut, 2, Sut, 2), gram(Sut, 2, Su, 1), gram(Sut, 2, Sv, 1), gram(Sut, 2, Sttt, 3)
g_v_uu, g_v_e = gram(Sv, 1, Suu, 2), gram(Sv, 1, Se, 0)
Gb = sp.groebner([Nj, Wsym ** 2 - Aj, Rsym ** 2 - Jx * (Jx + 2)], Wsym, Rsym, Jx, order="lex")


def zero_mod_N(expr):
    """True if the rational expression (in J, W, R) vanishes at J = J0 (root of N), W^2 = A, R^2 = J(J+2); the expression is cancelled first so a pole at J0 is not hidden."""
    e = sp.cancel(sp.together(expr))
    nu, de = sp.fraction(e)
    rn = sp.reduced(sp.expand(nu), list(Gb.exprs), Wsym, Rsym, Jx, order="lex")[1]
    rd = sp.reduced(sp.expand(de), list(Gb.exprs), Wsym, Rsym, Jx, order="lex")[1]
    return rd != 0 and rn == 0


def zero_id(expr):
    return sp.simplify(sp.cancel(sp.together(expr)).subs({Wsym: sp.sqrt(Aj), Rsym: sp.sqrt(Jx * (Jx + 2))})) == 0


a_s = -Nj / ((Jx + 2) * Wsym)                                       # signed amplitude: x_u = a e1
Yq = Rsym * Wsym
c_tt_e = sp.cancel(g_u_tt / a_s)
c_eps_e = sp.cancel(g_u_e / a_s)
c_uu_e = sp.cancel(g_u_uu / a_s)
ok_cs = (zero_id(g_uu_uu * g_uu - g_u_uu ** 2) and zero_id(g_e_e * g_uu - g_u_e ** 2) and zero_id(g_tt_tt - sp.Rational(1, 4))
         and g_ut_u == 0 and g_ut_v == 0 and g_ut_ttt == 0 and g_v_uu == 0 and g_v_e == 0)
wlist = sorted(k for k in S if k[0] * 1 + k[1] * 2 + k[2] * 1 <= 2)
ok_w2 = (wlist == [(0, 0, 2), (0, 1, 0), (1, 0, 0), (1, 0, 1), (2, 0, 0)] and (0, 0, 1) not in S)
check("X12 J0: weight-2 Schur jets at weights (u:1,v:2,t:1,eps:2,N:1)",
      ok_cs and ok_w2, "x_uu, x_tt, x_eps parallel to x_u; x_ut orthogonal to x_u, x_v, x_ttt; |x_tt| = 1/2",
      f"Cauchy-Schwarz equalities exact in J; weight<=2 monomials {wlist}; |x_ut|^2 = {g_ut_ut}")
Jv0 = sp.Symbol("J0s")
ok_c = (zero_id(c_tt_e - sp.Rational(1, 2)) and zero_id(c_eps_e + 4 * Jx * Yq / (Jx + 2) ** 2) and zero_mod_N(c_uu_e - Jx ** 2 / (4 * (Jx + 2)))
        and zero_id(g_ut_ut - Jx ** 4 / (2 * (Jx + 2) * Aj)))
# consistency with the exact line equation: q(c_F + dc; kappa_f + eps) = (2N/A) dc + 4 u_f dc^2 - 8 kappa_f s^2 eps, dc = -(s/2) u:  F1 = q/J at weight 2
s_F = Jx * Wsym / (Jx + 2); kf_ = Yq / (2 * Aj); uf_ = Jx * (Jx + 2) / (4 * Aj); Np = 3 * Jx ** 2 - 4
a_delta = -Np / ((Jx + 2) * Wsym)
ok_q = (zero_mod_N(c_uu_e - uf_ * s_F ** 2 / Jx) and zero_id(c_eps_e + 8 * kf_ * s_F ** 2 / Jx) and zero_id(a_delta + s_F * Np / (Aj * Jx)))
sg_u2 = SG["u2/W"]; sg_a = (-sg_u2[0], -sg_u2[1])                    # sign(a) = -sign(N) = -sign(u2)
sg_cut = (sg_u2[0] * sg_a[0], sg_u2[1] * sg_a[1])                      # c_ut = u2 |x_ut|^2 / g, sign(g) = sign(a)
check("X13 J0 form F1 = c_uu u^2 + c_tt t^2 + a_d delta u + c_eps eps, F2 = b v, F3 = c_ut u t",
      ok_c and ok_q and sg_cut == (-1, -1) and sg_u2 == (-1, 1), "c_uu = J^2/(4(J+2)) (mod N), c_tt = 1/2, c_eps = -4JY/(J+2)^2, c_ut < 0; F1 = q/J",
      f"(c_uu, a_d, c_eps) = (u_f s^2, -s N'/A, -8 kappa_f s^2)/J (Pauli route = line-root route, mod N); a_d = -N'/((J+2)W); sign(c_ut) on (2,J0),(J0,1+sqrt5) = {sg_cut}")
# ---- degree and charges of the weight-2 form at J0 (numerical values of the exact closed forms at J0 = 2.38298, signs and winding)
Aj0 = 4 + 2 * J0f - J0f ** 2; Y0 = float(np.sqrt(J0f * (J0f + 2) * Aj0)); W0 = float(np.sqrt(Aj0))
cuu_n = J0f ** 2 / (4 * (J0f + 2)); ctt_n = 0.5; ceps_n = -4 * J0f * Y0 / (J0f + 2) ** 2
cut_n = -J0f ** 2 / (np.sqrt(2 * (J0f + 2)) * W0); b_n = J0f * (J0f + 1) * np.sqrt(2 * J0f) / ((J0f + 2) * W0); ad_n = -(3 * J0f ** 2 - 4) / ((J0f + 2) * W0)
ph_ = np.linspace(0, 2 * np.pi, 20001)
wind = float(np.sum(np.diff(np.unwrap(np.arctan2(cut_n * np.cos(ph_) * np.sin(ph_), cuu_n * np.cos(ph_) ** 2 + ctt_n * np.sin(ph_) ** 2)))) / (2 * np.pi))
line_chi = int(np.sign(cuu_n) * np.sign(cut_n))                      # Jacobian sign b c_ut (2 c_uu u^2) at t = 0: sign(c_uu c_ut)
emit_chi = int(-np.sign(ctt_n) * np.sign(cut_n))                     # at u = 0: -2 c_tt c_ut t^2 b
check("X14 J0: local degree 0; eps>0: 4 nodes, chi (-1,-1,+1,+1)",
      abs(wind) < 1e-9 and line_chi == -1 and emit_chi == 1 and ceps_n < 0 and cuu_n > 0 and ctt_n > 0 and cut_n < 0,
      f"c_uu={cuu_n:.4f} c_tt=0.5 c_eps={ceps_n:.4f} c_ut={cut_n:.4f} b={b_n:.4f} a_d={ad_n:.4f}; winding {wind:.3f}",
      "line pair u = +-sqrt(-c_eps eps/c_uu), t = 0; off-line pair t = +-sqrt(-c_eps eps/c_tt), u = 0; Jacobian 2 b c_ut (c_uu u^2 - c_tt t^2): charge 0 for eps < eps_*(delta) and eps > 0")


# ---- X15: determinant route at J0: det H at weights (u:1, v:2, t:1) = c |d2|^2 with c = 16 J^2
def coefD(k):
    v_ = Dco[k]
    if sum(k) % 2 == 0:
        assert v_.c[1] == 0 and v_.c[3] == 0
        return ((-1) ** (sum(k) // 2)) * (v_.c[0].as_expr() + v_.c[2].as_expr() * Rsym * Wsym)
    assert v_.c[0] == 0 and v_.c[2] == 0
    d_ = Dodd(k)
    return Wsym * (d_.c[0].as_expr() + d_.c[2].as_expr() * Rsym * Wsym)


c16e = 16 * Jx ** 2
cuu_e = Jx ** 2 / (4 * (Jx + 2)); ctt_e = sp.Rational(1, 2); cut2_e = Jx ** 4 / (2 * (Jx + 2) * Aj); b2_e = 2 * Jx ** 3 * (Jx + 1) ** 2 / ((Jx + 2) ** 2 * Aj)
pred4 = {(4, 0, 0): c16e * cuu_e ** 2, (0, 0, 4): c16e * ctt_e ** 2, (2, 0, 2): c16e * (2 * cuu_e * ctt_e + cut2_e), (0, 2, 0): c16e * b2_e}
keys4 = [k for k in Dco if k[0] + 2 * k[1] + k[2] <= 4]
bad4 = [k for k in keys4 if not zero_mod_N(coefD(k) - pred4.get(k, 0))]
ctrl4 = zero_mod_N(coefD((4, 0, 0)) - sp.Rational(11, 10) * pred4[(4, 0, 0)])
check("X15 J0: det H at weights (u:1,v:2,t:1) = 16J^2[(c_uu u^2+c_tt t^2)^2 + c_ut^2 u^2t^2 + b^2 v^2]",
      not bad4 and not ctrl4, f"all {len(keys4)} monomials of weight <= 4 match mod N (determinant route; a wrong coefficient is rejected)",
      "weight <= 3 coefficients vanish mod N; weight 4 contains just u^4, u^2t^2, t^4, v^2 (c_uu^2, 2c_uu c_tt + c_ut^2, c_tt^2, b^2 times 16J^2)")


# ================================================================================================ FLOAT 1: independent Schur code, spheres, node search (iso, 13/6 and 5/2)
def flip_data(J3):
    """(c_F, u_f) of the flipping line node for couplings J3 = (Jx, Jy, Jz) in region (b), Jz < phi s (otri formulas; F_c root in (0,1), u = u(c))."""
    Jx_, Jy_, Jz_ = J3
    s_ = Jx_ + Jy_; P_ = Jx_ * Jy_; S_ = Jx_ ** 2 + Jy_ ** 2 - Jz_ ** 2
    a2_ = P_ * (s_ + Jz_); a1_ = s_ * (s_ * s_ + Jz_ * s_ - 2 * P_); a0_ = (Jx_ + Jz_) * (Jy_ + Jz_) * (s_ - Jz_)
    cs_ = [r.real for r in np.roots([a2_, a1_, a0_]) if abs(r.imag) < 1e-12 and 0 < r.real < 1]
    assert len(cs_) == 1
    return cs_[0], -(2 * P_ * cs_[0] + S_) / (4 * (1 - cs_[0] ** 2))


def line_roots(J3, u):
    """roots c in (-1,1) of q = 4u c^2 - 2P c - (4u + S), ascending."""
    Jx_, Jy_, Jz_ = J3
    P_ = Jx_ * Jy_; S_ = Jx_ ** 2 + Jy_ ** 2 - Jz_ ** 2
    r_ = np.roots([4 * u, -2 * P_, -(4 * u + S_)])
    return np.sort([x.real for x in r_ if abs(x.imag) < 1e-12 and abs(x.real) < 1])


def pick(rts, c0):
    """the root nearest to c0 (nan if there is none)."""
    return rts[np.argmin(np.abs(rts - c0))] if len(rts) else float("nan")


def fam2(J, u):
    """plane-(ii) node (x, f3) of the iso family (cos 2 pi x = 1 - J/(4u), cos 2 pi f3 = (J+2)/(4u) - (4+J-J^2)/J), or (nan, nan) when it is not real."""
    cx = 1 - J / (4 * u); c3 = (J + 2) / (4 * u) - (4 + J - J * J) / J
    if abs(cx) > 1 or abs(c3) > 1:
        return float("nan"), float("nan")
    return np.arccos(cx) / (2 * np.pi), np.arccos(c3) / (2 * np.pi)


def effective_tensors(J3, kappa, f0):
    """Schur-complement tensors S1[j], S2[j,k], S3[j,k,l] (2x2, kernel basis by eigh) in xi = 2 pi (f - f0); returns also the node spectrum."""
    Tt = terms(J3, kappa)
    H0 = np.zeros((4, 4), complex); D1 = np.zeros((3, 4, 4), complex); D2 = np.zeros((3, 3, 4, 4), complex); D3 = np.zeros((3, 3, 3, 4, 4), complex)
    for (a, b, n, t) in Tt:
        n = np.array(n, float); th = 2 * np.pi * np.dot(f0, n)
        for (r, c, sg, m_, e) in ((a, b, 1, n, np.exp(1j * th)), (b, a, -1, -n, np.exp(-1j * th))):
            base = 1j * sg * t * e
            H0[r, c] += base
            for j in range(3):
                D1[j][r, c] += base * 1j * m_[j]
                for k in range(3):
                    D2[j, k][r, c] += base * (1j * m_[j]) * (1j * m_[k])
                    for l in range(3):
                        D3[j, k, l][r, c] += base * (1j * m_[j]) * (1j * m_[k]) * (1j * m_[l])
    ev, Vv = np.linalg.eigh(H0)
    Wk = Vv[:, 1:3]; Qv = Vv[:, [0, 3]]
    Gf = Qv @ np.diag(1 / ev[[0, 3]]) @ Qv.conj().T
    red = lambda A_: Wk.conj().T @ A_ @ Wk
    S1 = np.array([red(D1[j]) for j in range(3)])
    S2 = np.zeros((3, 3, 2, 2), complex); S3 = np.zeros((3, 3, 3, 2, 2), complex)
    for j in range(3):
        for k in range(3):
            S2[j, k] = 0.5 * red(D2[j, k]) - red(D1[j] @ Gf @ D1[k])
            for l in range(3):
                S3[j, k, l] = (red(D3[j, k, l]) / 6.0 - 0.5 * red(D1[j] @ Gf @ D2[k, l]) - 0.5 * red(D2[k, l] @ Gf @ D1[j])
                               + red(D1[j] @ Gf @ D1[k] @ Gf @ D1[l]))
    return S1, S2, S3, ev


def pauli(M):
    """Hermitian 2x2 M = s0 + dx sigma_x + dy sigma_y + dz sigma_z -> (s0, dx, dy, dz)."""
    return np.array([(M[0, 0] + M[1, 1]).real / 2, M[0, 1].real, M[1, 0].imag, (M[0, 0] - M[1, 1]).real / 2])


MON = [(i, j, k) for i in range(4) for j in range(4 - i) for k in range(4 - i - j)]


def float_jets(J3, kappa, f0):
    """Pauli vectors of the monomials u^i v^j t^k (i+j+k <= 3), u = xi1 - xi2, v = xi1 + xi2, t = xi3, from a polynomial fit of the Schur complement."""
    S1, S2, S3, ev = effective_tensors(J3, kappa, f0)

    def Sxi(xi):
        out = np.zeros((2, 2), complex)
        for j in range(3):
            out += S1[j] * xi[j]
            for k in range(3):
                out += S2[j, k] * xi[j] * xi[k]
                for l in range(3):
                    out += S3[j, k, l] * xi[j] * xi[k] * xi[l]
        return out
    pts = np.random.default_rng(7).uniform(-0.6, 0.6, size=(60, 3))
    Am = np.array([[u ** i * v ** j * t ** k for (i, j, k) in MON] for (u, v, t) in pts])
    vals = np.array([Sxi(np.array([(u + v) / 2, (v - u) / 2, t])).reshape(4) for (u, v, t) in pts])
    coef = np.linalg.lstsq(Am, vals, rcond=None)[0]
    jt = {m: coef[n].reshape(2, 2) for n, m in enumerate(MON)}
    return {m: pauli(jt[m]) for m in MON if sum(m) >= 1}, ev


def iso_exact_float(J):
    A = 4 + 2 * J - J * J; W = np.sqrt(A); Yv = np.sqrt(J * (J + 2) * A); N = J ** 3 - 4 * J - 4
    return dict(a=abs(N) / ((J + 2) * W), b=J * (J + 1) * np.sqrt(2 * J) / ((J + 2) * W), u2=W * (J + 2) / (2 * N),
                g=J ** 2 * np.sqrt(J + 2) / (2 * np.sqrt(2) * abs(N)), det=W * Yv * J ** 3 * (J + 1) / (2 * (J + 2) ** 2 * A ** 2))


reldev = 0.0; vanmax = 0.0; spec_ok = True; sgn_u2 = []
for Jv in (13 / 6, 2.2, 5 / 2, 3.0):
    cF_, uf_ = flip_data((1.0, 1.0, Jv)); xF_ = np.arccos(cF_) / (2 * np.pi)
    X, ev = float_jets((1.0, 1.0, Jv), np.sqrt(uf_), np.array([xF_, 1 - xF_, 0.0]))
    spec_ok = spec_ok and abs(ev[1]) < 1e-12 and abs(ev[2]) < 1e-12 and abs(abs(ev[3]) - 4 * Jv) < 1e-12
    xu, xv, xt, xtt, xut, xttt = X[(1, 0, 0)][1:], X[(0, 1, 0)][1:], X[(0, 0, 1)][1:], X[(0, 0, 2)][1:], X[(1, 0, 1)][1:], X[(0, 0, 3)][1:]
    a, b = np.linalg.norm(xu[:]), np.linalg.norm(xv)
    u2 = -(xtt @ xu) / a ** 2
    beta = xttt + u2 * xut
    s0 = max(abs(X[m][0]) for m in X if 2 * m[0] + 3 * m[1] + m[2] <= 3)
    van = max(np.linalg.norm(xt), np.linalg.norm(xtt + u2 * xu), s0, abs(xu @ xv), abs(beta @ xu), abs(beta @ xv))
    ex = iso_exact_float(Jv)
    fl = dict(a=a, b=b, u2=u2, g=np.linalg.norm(beta), det=np.linalg.det(np.array([xu, xv, beta])))
    reldev = max(reldev, max(abs(fl[k_] - ex[k_]) / abs(ex[k_]) for k_ in ex)); vanmax = max(vanmax, van)
    sgn_u2.append(int(np.sign(u2)))
check("F1 FLOAT float Schur code vs exact closed forms, J = 13/6, 2.2, 5/2, 3.0",
      reldev < 1e-9 and vanmax < 1e-11 and spec_ok and sgn_u2 == [-1, -1, 1, 1], f"rel dev {reldev:.1e}; vanishing parts <= {vanmax:.1e}; sign(u2) {sgn_u2}",
      "eigh kernel basis + polynomial fit of the cubic jets; x_t = 0, d_tt = -u2 d_u, orthogonality; J0 = 2.38298")


def node_zero(B, f, tol=1e-9):
    """refine a zero of det H by BFGS (det H >= 0, quadratic basin at an isolated node); returns (f, residual middle level)."""
    r = minimize(lambda x: B.detH(x), np.asarray(f, float), method="BFGS", options=dict(gtol=1e-16, maxiter=200))
    return r.x, float(np.abs(B.levels(r.x)[0][1:3]).max())


def grid_nodes(B, center, hw, m=31, dmax=5e-2):
    """independent node search: local minima of det H on an m^3 grid of half-width hw around center, refined by BFGS; clustered list of zeros (|levels| < 1e-6)."""
    ax = np.linspace(-hw, hw, m)
    g = np.stack(np.meshgrid(ax, ax, ax, indexing="ij"), -1).reshape(-1, 3) + np.asarray(center, float)
    Dg = np.concatenate([np.linalg.det(B.H(g[i_:i_ + 20000])).real for i_ in range(0, len(g), 20000)]).reshape(m, m, m)
    from scipy.ndimage import minimum_filter
    mn = (Dg == minimum_filter(Dg, size=3, mode="nearest")) & (Dg < dmax)
    out = []
    for idx in np.argwhere(mn):
        f0_ = np.array([ax[i] for i in idx]) + np.asarray(center, float)
        f1_, res = node_zero(B, f0_)
        if res < 1e-6 and np.max(np.abs(f1_ - np.asarray(center, float))) < 1.2 * hw and not any(np.linalg.norm(f1_ - o) < 1e-5 for o in out):
            out.append(f1_)
    return out


rel = 4e-3
rows = []; ok_f2 = True; ok_nodes = True; ok_T = True; tdev = 0.0
for Jv in (13 / 6, 5 / 2):
    cF_, uf_ = flip_data((1.0, 1.0, Jv)); kf_ = np.sqrt(uf_); xF_ = np.arccos(cF_) / (2 * np.pi); f0_ = np.array([xF_, 1 - xF_, 0.0])
    mir = lambda f_: np.array([1 - f_[0], 1 - f_[1], -f_[2]])                    # inversion f -> -f (mod 1): the mirror node, opposite charge
    # before: one node
    Bb = Bloch((1.0, 1.0, Jv), kf_ * (1 - rel))
    rts = line_roots((1.0, 1.0, Jv), (kf_ * (1 - rel)) ** 2)
    cl = pick(rts, cF_); xl = np.arccos(cl) / (2 * np.pi); fl = np.array([xl, 1 - xl, 0.0])
    chi_b = chi_T(Bb, fl)[0]
    flb, gpb, phb = sphere_chern(Bb, fl, 0.012)
    flbm = sphere_chern(Bb, mir(fl), 0.012)
    gnb = grid_nodes(Bb, f0_, 0.03)
    # after: line node + two plane nodes
    Ba = Bloch((1.0, 1.0, Jv), kf_ * (1 + rel))
    rts = line_roots((1.0, 1.0, Jv), (kf_ * (1 + rel)) ** 2)
    cl2 = pick(rts, cF_); xl2 = np.arccos(cl2) / (2 * np.pi); fl2 = np.array([xl2, 1 - xl2, 0.0])
    xe, f3e = fam2(Jv, (kf_ * (1 + rel)) ** 2); fe = [np.array([xe, 1 - xe, s_ * f3e]) for s_ in (1, -1)]
    chis = [chi_T(Ba, f_)[0] for f_ in [fl2] + fe]
    fls = [sphere_chern(Ba, f_, 0.008) for f_ in [fl2] + fe]
    flms = [sphere_chern(Ba, mir(f_), 0.008) for f_ in [fl2] + fe]
    flall = sphere_chern(Ba, f0_, 0.05)
    gna = grid_nodes(Ba, f0_, 0.03)
    match = all(min(np.linalg.norm(g_ - f_) for g_ in gna) < 1e-6 for f_ in [fl2] + fe) if len(gna) == 3 else False
    ok_f2 = ok_f2 and chi_b == 1 and abs(flb + 1) < 1e-6 and chis == [-1, 1, 1] and abs(fls[0][0] - 1) < 1e-6 and all(abs(x_[0] + 1) < 1e-6 for x_ in fls[1:]) \
        and abs(flall[0] + 1) < 1e-6 and min(gpb, flall[1], min(x_[1] for x_ in fls)) > 0 and max(phb, flall[2], max(x_[2] for x_ in fls)) < 1.0 \
        and abs(flbm[0] - 1) < 1e-6 and abs(flms[0][0] + 1) < 1e-6 and all(abs(x_[0] - 1) < 1e-6 for x_ in flms[1:])
    # a third kappa just above the flip: still three zeros, positions = closed forms
    r3 = 1e-3; u3 = (kf_ * (1 + r3)) ** 2; B3 = Bloch((1.0, 1.0, Jv), kf_ * (1 + r3))
    c3r = pick(line_roots((1.0, 1.0, Jv), u3), cF_); x3 = np.arccos(c3r) / (2 * np.pi)
    xe3, f33 = fam2(Jv, u3)
    ex3 = [np.array([x3, 1 - x3, 0.0]), np.array([xe3, 1 - xe3, f33]), np.array([xe3, 1 - xe3, -f33])]
    gn3 = grid_nodes(B3, f0_, 0.03, m=61)
    ok_nodes = ok_nodes and len(gnb) == 1 and len(gna) == 3 and match and len(gn3) == 3 and all(min(np.linalg.norm(g_ - f_) for g_ in gn3) < 1e-6 for f_ in ex3)
    # T(kappa) along the line node: closed form -32 pi^3 kappa q'(c) F_c(c) sin(2 pi x)/J^3 and its sign flip
    sT = []
    for r_ in (-4e-3, -1e-3, 1e-3, 4e-3):
        k_ = kf_ * (1 + r_); u_ = k_ ** 2; Bt = Bloch((1.0, 1.0, Jv), k_)
        c_ = pick(line_roots((1.0, 1.0, Jv), u_), cF_); x_ = np.arccos(c_) / (2 * np.pi)
        sg_, Tn = chi_T(Bt, np.array([x_, 1 - x_, 0.0]))
        Tcf = -32 * np.pi ** 3 * k_ * (8 * u_ * c_ - 2) * ((2 + Jv) * c_ ** 2 + 4 * (1 + Jv) * c_ + (1 + Jv) ** 2 * (2 - Jv)) * np.sin(2 * np.pi * x_) / Jv ** 3
        tdev = max(tdev, abs(Tn - Tcf) / abs(Tcf)); sT.append(sg_)
    ok_T = ok_T and sT == [1, 1, -1, -1]
    rows.append(f"J={Jv:.4f}: before chi={chi_b} flux {flb:+.4f}; after chi {chis} flux {fls[0][0]:+.4f},{fls[1][0]:+.4f},{fls[2][0]:+.4f}, enclosing {flall[0]:+.4f}; mirror before {flbm[0]:+.3f}, after {flms[0][0]:+.3f},{flms[1][0]:+.3f},{flms[2][0]:+.3f}; grid zeros {len(gnb)} -> {len(gna)} (rel 4e-3), {len(gn3)} (rel 1e-3); emitted f3 = +-{f3e:.4f}")
check("F2 FLOAT fluxes and chi around the flipping node, kappa = kappa_f (1 -+ 0.004)",
      ok_f2, "J=13/6, 5/2: before chi +1, flux -1; after chi (-1,+1,+1), flux (+1,-1,-1), enclosing sphere -1; mirror nodes opposite",
      " | ".join(rows))
check("F3 FLOAT independent grid search of zeros of det H, and T(kappa) vs closed form",
      ok_nodes and ok_T, f"1 zero below, 3 above (box 0.03), positions = closed forms (1e-6); T sign (+,+,-,-) at rel (-4,-1,1,4)e-3, max rel dev of T {tdev:.1e}",
      "T = -32 pi^3 kappa q'(c) F_c(c) sin(2 pi x)/J^3 (otri) vs Im Tr(P d1H P d2H P d3H) at the line node")


# ================================================================================================ FLOAT 2: the J0 event (iso, J = J0 = root of J^3 - 4J - 4)
cF0, uf0 = flip_data((1.0, 1.0, J0f)); kf0 = np.sqrt(uf0); x0 = np.arccos(cF0) / (2 * np.pi); f00 = np.array([x0, 1 - x0, 0.0])
Y0n = float(np.sqrt(J0f * (J0f + 2) * (4 + 2 * J0f - J0f ** 2)))
rows = []; ok_j0 = True
for rel_ in (4e-3, 1e-4):
    eps_ = kf0 * rel_
    B0 = Bloch((1.0, 1.0, J0f), kf0 * (1 + rel_)); u_ = (kf0 * (1 + rel_)) ** 2
    rts = line_roots((1.0, 1.0, J0f), u_)
    xl = np.arccos(rts) / (2 * np.pi)
    xe, f3e = fam2(J0f, u_)
    nodes = [np.array([x_, 1 - x_, 0.0]) for x_ in xl] + [np.array([xe, 1 - xe, s_ * f3e]) for s_ in (1, -1)]
    u_ex = sorted(4 * np.pi * (xl - x0)); t_ex = 2 * np.pi * f3e
    u_pr = 4 * np.sqrt(Y0n * eps_ / (J0f * (J0f + 2))); t_pr = 2 / (J0f + 2) * np.sqrt(2 * J0f * Y0n * eps_)
    r_u = [abs(u_ex[0]) / u_pr, u_ex[1] / u_pr]; r_t = t_ex / t_pr
    rows.append(f"rel {rel_:g}: u/u_pred {r_u[0]:.3f},{r_u[1]:.3f} t/t_pred {r_t:.3f}")
    if rel_ == 4e-3:
        chis = [chi_T(B0, f_)[0] for f_ in nodes]
        fls = [sphere_chern(B0, f_, 0.008) for f_ in nodes]
        flall = sphere_chern(B0, f00, 0.05)
        Bm = Bloch((1.0, 1.0, J0f), kf0 * (1 - rel_))
        flm = sphere_chern(Bm, f00, 0.05)
        zb = grid_nodes(Bm, f00, 0.04); za = grid_nodes(B0, f00, 0.04)
        ok_j0 = ok_j0 and sorted(chis) == [-1, -1, 1, 1] and chis[0] == chis[1] == -1 and all(abs(fls[i][0] - 1) < 1e-6 for i in (0, 1)) \
            and all(abs(fls[i][0] + 1) < 1e-6 for i in (2, 3)) and abs(flall[0]) < 1e-6 and abs(flm[0]) < 1e-6 and len(zb) == 0 and len(za) == 4 \
            and min(x_[1] for x_ in fls + [flall, flm]) > 0 and max(x_[2] for x_ in fls + [flall, flm]) < 1.0
        rows.append(f"chi {chis} flux {[round(float(x_[0]), 3) for x_ in fls]}, sphere {flall[0]:+.3f} (eps>0) {flm[0]:+.3f} (eps<0), grid zeros {len(zb)} -> {len(za)}")
    else:
        ok_j0 = ok_j0 and abs(r_u[0] - 1) < 0.05 and abs(r_u[1] - 1) < 0.05 and abs(r_t - 1) < 0.05
check("F4 FLOAT J0: 0 zeros below, 4 above; chi (-1,-1,+1,+1); sphere flux 0 both sides",
      ok_j0, rows[0].replace("rel 0.004: ", "") + f"; at rel 1e-4 u/u_pred {r_u[0]:.3f},{r_u[1]:.3f} t/t_pred {r_t:.3f}",
      "; ".join(rows) + "; u = 4 pi (x - x_F), t = 2 pi f3; u_pred = 4 sqrt(Y eps/(J(J+2))), t_pred = 2 sqrt(2JY eps)/(J+2)")

# ---- birth-curve coefficient: (kappa_* - kappa_f)/delta^2 -> -a_d^2/(4 c_uu |c_eps|) as delta = J - J0 -> 0 (mp, independent of the Schur route: u_* = (J^2-2+J sqrt(J^2-4))/8, u_f = J(J+2)/(4A))
mp.mp.dps = 50
J0m = mp.findroot(lambda x: x ** 3 - 4 * x - 4, mp.mpf("2.383"))
A0m = 4 + 2 * J0m - J0m ** 2; W0m = mp.sqrt(A0m); Y0m = mp.sqrt(J0m * (J0m + 2) * A0m)
a_d = -(3 * J0m ** 2 - 4) / ((J0m + 2) * W0m); c_uu0 = J0m ** 2 / (4 * (J0m + 2)); c_eps0 = -4 * J0m * Y0m / (J0m + 2) ** 2
Lpred = -a_d ** 2 / (4 * c_uu0 * abs(c_eps0))


def dk(J):
    A = 4 + 2 * J - J ** 2
    return mp.sqrt((J ** 2 - 2 + J * mp.sqrt(J ** 2 - 4)) / 8) - mp.sqrt(J * (J + 2) / (4 * A))


rr = {}
for dl in (mp.mpf("1e-3"), mp.mpf("1e-4"), mp.mpf("1e-5")):
    rr[dl] = (dk(J0m + dl) / dl ** 2, dk(J0m - dl) / dl ** 2)
avg = [(x_[0] + x_[1]) / 2 for x_ in rr.values()]
ok_bc = all(abs(a_ - Lpred) < 1e-5 * abs(Lpred) for a_ in avg[1:]) and abs(avg[0] - Lpred) < 5e-3 * abs(Lpred) and Lpred < 0 \
    and all(x_[0] < 0 and x_[1] < 0 for x_ in rr.values())
check("F5 FLOAT mp50: (kappa_*-kappa_f)/delta^2 vs -a_d^2/(4 c_uu |c_eps|)",
      ok_bc, f"predicted {mp.nstr(Lpred, 10)}; delta=1e-3,1e-4,1e-5 averages {[mp.nstr(a_, 9) for a_ in avg]}",
      f"u_* = (J^2-2+J sqrt(J^2-4))/8, u_f = J(J+2)/(4A) (closed forms, independent of the Schur route); one-sided values {[ (mp.nstr(x_[0], 8), mp.nstr(x_[1], 8)) for x_ in rr.values()]}")

# ================================================================================================ FLOAT 3: anisotropic couplings (50-digit mpmath Schur data; double-precision nodes and fluxes)
mp.mp.dps = 50


def mpm(n=4):
    return mp.matrix(n, n)


def hp_tensors(J3, kappa, f0):
    amp_ = {"x": 2 * J3[0], "y": 2 * J3[1], "z": 2 * J3[2], "odd": 2 * kappa}
    H0 = mpm(); D1 = [mpm() for _ in range(3)]; D2 = [[mpm() for _ in range(3)] for _ in range(3)]
    D3 = [[[mpm() for _ in range(3)] for _ in range(3)] for _ in range(3)]
    for (a, b, n, kind) in TERMS:
        t = amp_[kind]
        th = 2 * (f0[0] * n[0] + f0[1] * n[1] + f0[2] * n[2])
        for (r, c, sg, m_, e) in ((a, b, 1, n, mp.expjpi(th)), (b, a, -1, tuple(-x_ for x_ in n), mp.expjpi(-th))):
            base = mp.mpc(0, 1) * sg * t * e
            H0[r, c] += base
            for j in range(3):
                D1[j][r, c] += base * mp.mpc(0, m_[j])
                for k in range(3):
                    D2[j][k][r, c] += base * mp.mpc(0, m_[j]) * mp.mpc(0, m_[k])
                    for l in range(3):
                        D3[j][k][l][r, c] += base * mp.mpc(0, m_[j]) * mp.mpc(0, m_[k]) * mp.mpc(0, m_[l])
    return H0, D1, D2, D3


def mtrace(M):
    return sum(M[i, i] for i in range(M.rows))


def hp_local(J3, kappa, f0):
    """Local structure at a node with a two-dimensional kernel (50 digits): Gram matrix of the three first-order operators (rank 2 <=> T = 0), kernel direction k,
    component of Q(k,k) outside the range (c2), and the local degree sign(Im tr(A B Y)), (e_a, e_b, k) right-handed, Y = cubic part along k after eliminating the range part of Q."""
    H0, D1, D2, D3 = hp_tensors(J3, kappa, f0)
    c16 = 16 * mp.mpf(J3[2]) ** 2
    P = mp.eye(4) - H0 * H0 / c16
    G = H0 / c16
    spec_res = max(abs(x_) for x_ in (H0 * P))
    sand = lambda X: P * X * P
    O = [sand(D1[j]) for j in range(3)]
    S2 = [[sand(D2[j][k]) / 2 - sand(D1[j] * G * D1[k]) for k in range(3)] for j in range(3)]
    S2s = [[(S2[j][k] + S2[k][j]) / 2 for k in range(3)] for j in range(3)]

    def S3f(j, k, l):
        return sand(D3[j][k][l]) / 6 - sand(D1[j] * G * D2[k][l]) / 2 - sand(D2[k][l] * G * D1[j]) / 2 + sand(D1[j] * G * D1[k] * G * D1[l])
    ip = lambda X, Y: (mtrace(X * Y)).real / 2
    gram_ = mp.matrix(3, 3)
    for j in range(3):
        for k in range(3):
            gram_[j, k] = ip(O[j], O[k])
    E, Q = mp.eigsy(gram_)
    kv = [Q[i, 0] for i in range(3)]; ea = [Q[i, 1] for i in range(3)]; eb = [Q[i, 2] for i in range(3)]
    if mp.det(mp.matrix([[ea[i], eb[i], kv[i]] for i in range(3)])) < 0:
        eb = [-x_ for x_ in eb]
    lin = lambda v: sum((O[j] * v[j] for j in range(3)), mpm())
    A_ = lin(ea); B_ = lin(eb)
    quad = lambda v, w: sum((S2s[j][l] * (v[j] * w[l]) for j in range(3) for l in range(3)), mpm())
    Qkk = quad(kv, kv)
    G2 = mp.matrix([[ip(A_, A_), ip(A_, B_)], [ip(B_, A_), ip(B_, B_)]])
    cf = mp.lu_solve(G2, mp.matrix([ip(A_, Qkk), ip(B_, Qkk)]))
    Xp = Qkk - A_ * cf[0] - B_ * cf[1]
    c2 = mp.sqrt(max(ip(Xp, Xp), 0))
    w = [-(cf[0] * ea[i] + cf[1] * eb[i]) for i in range(3)]
    Ck = sum((S3f(j, l, m) * (kv[j] * kv[l] * kv[m]) for j in range(3) for l in range(3) for m in range(3)), mpm())
    Yv = Ck + 2 * quad(kv, w)
    t3 = (mtrace(A_ * B_ * Yv)).imag / 2
    return dict(E=E, k=kv, spec=spec_res, c2=c2, s0=(mtrace(Qkk) / 2).real, t3=t3, deg=int(mp.sign(t3)))


def flip_hp(J3):
    Jx_, Jy_, Jz_ = [mp.mpf(x_) for x_ in J3]
    s_ = Jx_ + Jy_; P_ = Jx_ * Jy_; S_ = Jx_ ** 2 + Jy_ ** 2 - Jz_ ** 2
    a2_ = P_ * (s_ + Jz_); a1_ = s_ * (s_ * s_ + Jz_ * s_ - 2 * P_); a0_ = (Jx_ + Jz_) * (Jy_ + Jz_) * (s_ - Jz_)
    cF = (-a1_ + mp.sqrt(a1_ ** 2 - 4 * a2_ * a0_)) / (2 * a2_)
    return cF, -(2 * P_ * cF + S_) / (4 * (1 - cF ** 2))


COUPL = ((1, 1, mp.mpf(13) / 6), (1, mp.mpf(1) / 2, 2), (1, mp.mpf(1) / 2, mp.mpf(8) / 5), (mp.mpf(13) / 10, mp.mpf(2) / 5, mp.mpf(9) / 5), (1, mp.mpf(4) / 5, mp.mpf(11) / 5))
hp_rows = []; ok_hp = True; max_small = mp.mpf(0)
for J3 in COUPL:
    cF_h, uF_h = flip_hp(J3); x_h = mp.acos(cF_h) / (2 * mp.pi)
    r_ = hp_local(J3, mp.sqrt(uF_h), (x_h, 1 - x_h, mp.mpf(0)))
    small = max(abs(r_["E"][0]), r_["c2"], abs(r_["s0"]), r_["spec"])
    max_small = max(max_small, small)
    ok_hp = ok_hp and small < mp.mpf("1e-40") and r_["E"][1] > mp.mpf("1e-3") and r_["deg"] == 1
    hp_rows.append(f"({float(J3[0]):g},{float(J3[1]):g},{float(J3[2]):.3f}) k=({float(r_['k'][0]):+.3f},{float(r_['k'][1]):+.3f},{float(r_['k'][2]):+.3f}) deg {r_['deg']:+d}")
# control: a non-flip node (kappa = 1.05 kappa_f, coupling (1,1/2,2)) must NOT show a rank-2 first-order part
J3 = (1, mp.mpf(1) / 2, 2); cF_h, uF_h = flip_hp(J3); kc_ = mp.sqrt(uF_h) * mp.mpf("1.05"); uc_ = kc_ ** 2
P_ = mp.mpf(1) / 2; S_ = 1 + mp.mpf(1) / 4 - 4
rts_c = [(2 * P_ + s_ * mp.sqrt(4 * P_ ** 2 + 16 * uc_ * (4 * uc_ + S_))) / (8 * uc_) for s_ in (1, -1)]
ctrl = []
for cc_ in rts_c:
    x_c = mp.acos(cc_) / (2 * mp.pi)
    ctrl.append(float(hp_local(J3, kc_, (x_c, 1 - x_c, mp.mpf(0)))["E"][0]))
check("F6 FLOAT mp50 anisotropic flip nodes: rank-2 linear part, c2 = 0, local degree +1",
      ok_hp and min(ctrl) > 1e-3 and max_small < mp.mpf("1e-40"),
      f"5 couplings, max residual {mp.nstr(max_small, 3)}; {hp_rows[1]}; control (non-flip node) eigenvalues {[round(x_, 3) for x_ in ctrl]}",
      "; ".join(hp_rows) + "; residual = max |smallest Gram eigenvalue of the three first-order operators, c2 = component of Q(k,k) outside their span, s0(Q(k,k)), H0 P|")

# ---- double-precision nodes and fluxes at two anisotropic couplings (kappa = kappa_f (1 -+ 0.016))
rows = []; ok_an = True
for J3 in ((1.0, 0.5, 2.0), (1.0, 0.5, 1.6)):
    cF_, uf_ = flip_data(J3); kf_ = np.sqrt(uf_); xF_ = np.arccos(cF_) / (2 * np.pi); f0_ = np.array([xF_, 1 - xF_, 0.0])
    Xj, _ = float_jets(J3, kf_, f0_)
    Lm = np.array([Xj[(1, 0, 0)][1:] + Xj[(0, 1, 0)][1:], -Xj[(1, 0, 0)][1:] + Xj[(0, 1, 0)][1:], Xj[(0, 0, 1)][1:]]).T
    _, svs, Vt_ = np.linalg.svd(Lm); kdir = Vt_[-1] * np.sign(Vt_[-1][2])
    res_b = []; res_a = []
    for rel_, store in ((-1.6e-2, res_b), (1.6e-2, res_a)):
        B_ = Bloch(J3, kf_ * (1 + rel_))
        nd = grid_nodes(B_, f0_, 0.06, m=41)
        for f_ in nd:
            store.append((f_, chi_T(B_, f_)[0], sphere_chern(B_, f_, 0.01)))
        store.append(sphere_chern(B_, f0_, 0.07))
    nb = res_b[:-1]; na = res_a[:-1]
    line_ = [r_ for r_ in na if abs(r_[0][2]) < 1e-6]
    ok_j = (len(nb) == 1 and nb[0][1] == 1 and abs(nb[0][2][0] + 1) < 1e-6 and abs(res_b[-1][0] + 1) < 1e-6 and len(na) == 3 and len(line_) == 1
            and line_[0][1] == -1 and abs(line_[0][2][0] - 1) < 1e-6 and abs(res_a[-1][0] + 1) < 1e-6 and svs[2] < 1e-12 and svs[1] > 1e-2)
    angs = []; upart = []
    if ok_j:
        uh = np.array([1, -1, 0]) / np.sqrt(2)
        for r_ in na:
            if abs(r_[0][2]) > 1e-6:
                off = r_[0] - line_[0][0]; offp = off - (off @ uh) * uh
                angs.append(float(np.degrees(np.arccos(min(1.0, abs(offp @ kdir) / np.linalg.norm(offp)))))); upart.append(float(off @ uh))
                ok_j = ok_j and r_[1] == 1 and abs(r_[2][0] + 1) < 1e-6
        ok_j = ok_j and len(angs) == 2 and max(angs) < 2.0 and abs(upart[0] - upart[1]) < 1e-4
    ok_an = ok_an and ok_j
    rows.append(f"({J3[0]:g},{J3[1]:g},{J3[2]:g}): nodes {len(nb)}->{len(na)}, chi before {[r_[1] for r_ in nb]} after {[r_[1] for r_ in na]}, k=({kdir[0]:+.3f},{kdir[1]:+.3f},{kdir[2]:+.3f}), angle(emitted, +-k) {max(angs) if angs else float('nan'):.2f} deg")
check("F7 FLOAT anisotropic (1,1/2,2), (1,1/2,8/5): 1 node -> 3 nodes",
      ok_an, " | ".join(r_.split(", k=")[0] for r_ in rows) + f"; emitted along +-k within {(max(angs) if angs else float('nan')):.2f} deg",
      " | ".join(rows) + "; offsets from the line node minus their component along (1,-1,0) lie along +-k; the two line-direction components agree")

# ---- persistence of the emitted pair at finite eps (iso, J = 13/6, 5/2, 3.0; kappa up to 6 kappa_f)
ok_p = True; npts = 0
for Jv in (13 / 6, 5 / 2, 3.0):
    cF_, uf_ = flip_data((1.0, 1.0, Jv)); kf_ = np.sqrt(uf_)
    for rel_ in (0.01, 0.05, 0.2, 0.5, 1.0, 2.0, 5.0):
        k_ = kf_ * (1 + rel_); u_ = k_ ** 2; B_ = Bloch((1.0, 1.0, Jv), k_)
        xe_, f3e_ = fam2(Jv, u_)
        ch_e = [chi_T(B_, np.array([xe_, 1 - xe_, s_ * f3e_]))[0] for s_ in (1, -1)]
        rts_ = line_roots((1.0, 1.0, Jv), u_)
        ch_l = [chi_T(B_, np.array([np.arccos(c_) / (2 * np.pi), 1 - np.arccos(c_) / (2 * np.pi), 0.0]))[0] for c_ in rts_]
        ok_p = ok_p and ch_e == [1, 1] and ch_l == [-1, -1] and len(rts_) == 2
        npts += 1
check("F8 FLOAT emitted pair persists: chi (+1,+1), both line nodes chi -1, up to kappa = 6 kappa_f",
      ok_p, f"{npts} points, J = 13/6, 5/2, 3.0, kappa/kappa_f - 1 = 0.01 ... 5: net chi 0 on the cluster after the flip",
      "T = Im Tr(P d1H P d2H P d3H) at the exact plane-(ii) nodes (x_e, 1-x_e, +-f3) and at the two line roots; middle levels < 1e-6 at every point")


# ================================================================================================ output size and total
size_now = OUTCHARS[0]
check("S stdout size", VERBOSE or size_now + 200 < 5000, f"{size_now} characters before this line and the TOTAL line (limit 5000; not enforced with RBIRTH_VERBOSE=1)")
emit(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
