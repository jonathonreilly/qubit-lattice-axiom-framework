#!/usr/bin/env python3
"""Composite-site network, flux-free comparator: at the birth coupling the merged line/plane touching is a cubic (3, 3, 1) touching of local degree +1 for every J in (0, 2).

Supplied u = +1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, couplings J_x = J_y = 1, J_z = J in (0, 2),
odd term kappa, four-site Bloch matrix H(f) = i M(f).  At the birth coupling kappa_c^2 = J(J+2)/[4(4 + 2J - J^2)] the line node f0 = (x, 1 - x, 0),
cos 2 pi x = (J-2)(J+1)/(J+2), merges with the two plane-(ii) nodes (f3 = 0 there).  Coordinates: xi = 2 pi (f - f0), u = xi1 - xi2, v = xi1 + xi2, t = xi3.

EXACT (checks 1-10, no floating point): identities in the function field L = Q(J)(omega, Y), omega^2 = -A, Y^2 = J(J+2)A, A = 4 + 2J - J^2, with
kappa_c = Y/(2A) and e^{2 pi i x} = (J + omega)^2/(2(J+2)) (omega = iW, W = sqrt(A); Y = sqrt(J(J+2)A) > 0), i.e. for every J at once; signs on (0, 2) by exact
factorisation and Sturm root counts; the genus of the curve carrying the data by exact polynomial algebra.  The kernel projector P of H(f0) (rank two), H^-1 = H/c
on its complement and the Schur complement S = PVP - PVGVP + PVGVGVP (V = H(f) - H(f0), G the inverse of H(f0) on the complement) give the effective two-level
Hamiltonian S = s0 + d.sigma; Pauli vectors and their Gram data are traces over P, so no kernel-basis normalisation enters.
Results: det(H - lambda) = lambda^2 (lambda^2 - 16 J^2); d has no t-linear and no t^3 term, d_tt = -u2 d_u, so with u' = u - u2 t^2:
d = x_u u' + x_v v + x_beta t^3 + (weighted order >= 4), mutually orthogonal, det[x_u, x_v, x_beta] > 0: weights (3, 3, 1), local degree +1; D = det H has a rank-two
Hessian and its weight-6 part is c |d0|^2, c = 16 J^2; the first-order unfolding in kappa is d = ... + x_beta (t^3 - mu eps t).
FLOAT (check 11, not certified): an independent floating-point Schur-complement code (eigh kernel basis, polynomial fit of the cubic jets) compared with the exact
closed forms, and Berry fluxes of the lowest two bands on small spheres (the landed Fukui-link `sphere_chern`) around the merged point and its mirror.
CAVEAT: the effective Hamiltonian is the Schur complement at E = 0 (static) on the kernel at f0; the true two-band problem differs by an energy-dependent metric
1 + O(xi^2), which is argued (not computed) to change d only at weight >= 5; the link degree -> Berry flux sign (flux = -degree) is checked only in floating point.
Scope: J_x = J_y = 1, kappa = kappa_c (plus the first-order unfolding), kappa_c > 0; no statement at other couplings, anisotropies, spin-model equivalence or physical identification.
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import time
from math import comb

import numpy as np
import sympy as sp
from sympy import QQ, ZZ
from sympy.polys.fields import field
from sympy.polys.matrices import DomainMatrix

AUDIT_TIMEOUT_SEC = 300

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


# ------------------------------------------------------------------------------------------------ network (landed `terms`)
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
        for s in (-1, 1):
            q = list(p); q[a] += s; q = tuple(q)
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
    """Real hopping terms (a, b, n, t): M(f)[a, b] += t e^{2 pi i f.n}, M(f)[b, a] -= t e^{-2 pi i f.n}, gauge u = +1."""
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
                out.append((r1, r2, tuple(np.subtract(n2, n1)), 2.0 * kappa))
    return out


# ------------------------------------------------------------------------------------------------ exact field L = Q(J)(omega, Y)
K0, Jf = field("J", QQ)
Af = 4 + 2 * Jf - Jf ** 2
Y2 = Jf * (Jf + 2) * Af
P2 = -Af                                                    # omega^2


class El:
    """a0 + a1 omega + a2 Y + a3 omega Y, a_i in K0 = Q(J); conjugation omega -> -omega (Y real)."""
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
_T = terms((1.0, 1.0, 7.0), 0.3)                           # amplitude tags 2 (J_x, J_y), 14 (J_z), 0.6 (kappa)
KIND = {2.0: "xy", 14.0: "z", 0.6: "odd"}
TERMS = [(int(a), int(b), tuple(int(x) for x in n), KIND[round(float(t), 9)]) for (a, b, n, t) in _T]
assert len(TERMS) == 18
eta = El(Jf, 1, 0, 0)                                      # J + omega
z0 = eta * eta * (1 / (2 * (Jf + 2)))                      # e^{2 pi i x}
z0i = eta.conj() * eta.conj() * (1 / (2 * (Jf + 2)))
KAPPA = El(0, 0, 1 / (2 * Af), 0)                          # kappa_c = Y/(2A)
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
                for (r, s_, n, kind) in TERMS:
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


def e2_of(M):
    s = ZERO
    for i in range(4):
        for j in range(i + 1, 4):
            s = s + (M[i][i] * M[j][j] - M[i][j] * M[j][i])
    return s


def ratio(Mx, Nx):
    """g with Mx = g Nx (matrices over L), and whether the whole matrix identity holds."""
    for r in range(4):
        for c in range(4):
            if not Nx[r][c].is_zero():
                g = Mx[r][c] * Nx[r][c].inv()
                return g, mzero(msub(Mx, mscale(Nx, g)))
    return None, mzero(Mx)


Jx = sp.Symbol("J")


def at1(e):
    """K0 element or L element -> sympy value at J = 1 (L element: dict-free string via components)."""
    return sp.nsimplify(e.as_expr().subs(Jx, 1)) if hasattr(e, "as_expr") else e


def sign_on_interval(expr):
    """+1/-1 if the rational function expr(J) has that sign on all of (0, 2): every irreducible factor of numerator and denominator has no root in [0, 2]
    (exact Sturm count; the factor J is positive on (0, 2)) and its sign is read at J = 1.  None if undecided."""
    num, den = sp.fraction(sp.cancel(sp.together(expr)))
    sgn = 1
    for part in (num, den):
        c0, fl = sp.factor_list(part, Jx)
        sgn *= int(sp.sign(c0))
        for f_, mult in fl:
            if f_ == Jx:
                continue
            if sp.Poly(f_, Jx).count_roots(0, 2) != 0:
                return None
            sgn *= int(sp.sign(f_.subs(Jx, 1))) ** mult
    return sgn


def sq(x):
    return sp.simplify(x)


# ================================================================================================ exact computation
T = coeff_tensor(3)
M0 = T[(0, 0, 0)]
c16 = El(16 * Jf ** 2)
kc2 = KAPPA * KAPPA

# ---- check 1: node and kernel projector
c1 = (z0 + z0i) * QQ(1, 2)
u_ = kc2.c[0]
ok_node = (kc2 == El(Jf * (Jf + 2) / (4 * (4 + 2 * Jf - Jf ** 2))) and (z0 * z0i == ONE) and (z0i == z0.conj())
           and c1 == El((Jf - 2) * (Jf + 1) / (Jf + 2))
           and (kc2 * c1 * c1 * 4 - c1 * 2 + El(Jf ** 2 - 2) - kc2 * 4).is_zero()                                       # line-(i) equation
           and (1 - Jf / (4 * u_)) == (Jf - 2) * (Jf + 1) / (Jf + 2) and ((Jf + 2) / (4 * u_) - (4 + Jf - Jf ** 2) / Jf) == 1   # plane-(ii): same cosine, f3 = 0
           and (Jf * (Jf + 2) - 4 * u_ * (4 + 2 * Jf - Jf ** 2)) == 0)                                                   # F2 = 0
M2 = mmul(M0, M0); M3 = mmul(M2, M0)
p1, p2, p3, p4 = mtr(M0), mtr(M2), mtr(M3), mtr(mmul(M2, M2))
E1 = p1; E2 = (E1 * p1 - p2) * QQ(1, 2); E3 = (E2 * p1 - E1 * p2 + p3) * QQ(1, 3); E4 = (E3 * p1 - E2 * p2 + E1 * p3 - p4) * QQ(1, 4)
I4 = mident()
P = mscale(madd(M2, mscale(I4, c16)), El(1 / (16 * Jf ** 2)))
G = mscale(M0, El(-1 / (16 * Jf ** 2)))
ok_spec = E1.is_zero() and E3.is_zero() and E4.is_zero() and E2 == c16 and mzero(madd(M0, mconj_t(M0)))
ok_proj = (mzero(mmul(M0, P)) and mzero(msub(mmul(P, P), P)) and mzero(msub(P, mconj_t(P))) and mtr(P) == El(2)
           and mzero(msub(mmul(G, M0), msub(I4, P))) and mzero(mmul(G, P)))
check("1 node + kernel projector (birth conditions, spectrum, P, G)", ok_node and ok_spec and ok_proj,
      f"kappa_c = Y/(2A), z0 = (J+omega)^2/(2(J+2)) on |z| = 1, F2 = 0, f3 = 0; det(H - lambda) = lambda^2 (lambda^2 - 16J^2); P rank-2 projector, G = -M0/c; "
      f"J=1: kappa_c = sqrt15/10, z0 = (-2 + i sqrt5)/3, levels 0, 0, +-{sp.sqrt(at1(E2.c[0]))}")

# ---- Schur series (zeta = i xi; S_H = i Sigma), total degree 3
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

# ---- check 2: vanishing of the t-linear and t^3 matrices, identity part through weight 3
ok_van = mzero(St) and mzero(Sttt) and all(mtr(X).is_zero() for X in (Su, Sv, Stt, Sut))
check("2 Schur complement (degree <= 3): t-linear and t^3 matrices vanish; no identity part through weight 3", ok_van,
      f"{len(S)} nonzero monomials u^a v^b t^c, none equal to t or t^3; tr Sigma_u = tr Sigma_v = tr Sigma_tt = tr Sigma_ut = 0 (weights u:2, v:3, t:1)")

# ---- exact sign facts on 0 < J < 2
Aj = 4 + 2 * Jx - Jx ** 2
s2 = (Jx + 2) / (2 * (Jx ** 3 - 4 * Jx - 4))
fx = {"a2": (Jx ** 3 - 4 * Jx - 4) ** 2 / ((Jx + 2) ** 2 * Aj), "b2": 2 * Jx ** 3 * (Jx + 1) ** 2 / ((Jx + 2) ** 2 * Aj),
      "g2": Jx ** 4 * (Jx + 2) / (8 * (Jx ** 3 - 4 * Jx - 4) ** 2), "mu/Y": 8 * Aj / (Jx ** 2 * (Jx + 2)),
      "det/WY": Jx ** 3 * (Jx + 1) / (2 * (Jx + 2) ** 2 * Aj ** 2), "u2/W": s2}
SG = {k: sign_on_interval(v_) for k, v_ in fx.items()}

# ---- check 3: d_tt = -u2 d_u with u2 < 0
g, okg = ratio(Stt, Su)
check("3 d_tt = -u2 d_u exactly (no v part), u2 < 0 on (0, 2); u' = u - u2 t^2 removes the t^2 term", okg and g == El(0, (Jf + 2) / (2 * (Jf ** 3 - 4 * Jf - 4)), 0, 0) and SG["u2/W"] == -1,
      f"Sigma_tt = g Sigma_u, g = omega (J+2)/(2(J^3-4J-4)), u2 = W (J+2)/(2(J^3-4J-4)); J=1: u2 = {sq(sp.sqrt(5) * s2.subs(Jx, 1))} ({float(sp.sqrt(5) * s2.subs(Jx, 1)):.6f})")

# ---- check 4: orthogonality, norms, determinant
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
detJ1 = sq(sp.sqrt(5) * sp.sqrt(15) * fx["det/WY"].subs(Jx, 1))
check("4 x_u, x_v, x_beta mutually orthogonal, norms a^2, b^2, g^2, det[x_u, x_v, x_beta] > 0", ok_herm and ok_gram and ok_det,
      f"a^2 = (J^3-4J-4)^2/((J+2)^2 A), b^2 = 2J^3(J+1)^2/((J+2)^2 A), g^2 = J^4(J+2)/(8(J^3-4J-4)^2), det = W Y J^3(J+1)/(2(J+2)^2 A^2); "
      f"J=1: a^2 = {at1(a2)}, b^2 = {at1(b2)}, g^2 = {at1(g2)}, det = {detJ1} ({float(detJ1):.6f})")

# ---- check 5: D = det H
RD, Jr, kap, z1, z2, z3 = sp.ring("Jr,kap,z1,z2,z3", ZZ)
dom = RD.to_domain()
S0 = 2
tag = {"xy": RD(2), "z": 2 * Jr, "odd": 2 * kap}
Ms = [[RD(0)] * 4 for _ in range(4)]
for (a, b, n, kind) in TERMS:
    Ms[a][b] += tag[kind] * z1 ** (S0 + n[0]) * z2 ** (S0 + n[1]) * z3 ** (S0 + n[2])
    Ms[b][a] -= tag[kind] * z1 ** (S0 - n[0]) * z2 ** (S0 - n[1]) * z3 ** (S0 - n[2])
Dp = DomainMatrix([[dom.convert(x) for x in row] for row in Ms], (4, 4), dom).det()           # D z^(4 S0); det H = det M since i^4 = 1
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


def Dreal(k):                       # coefficient of xi^m, |m| even: i^|m| Dzeta_m
    return Dco[k] * ((-1) ** (sum(k) // 2))


def Dodd(k):                        # |m| odd: Dzeta_m = omega q, i^|m| omega q = W (-1)^((|m|+1)/2) q ; returns (-1)^.. q (an element of K0 + K0 Y)
    assert Dco[k].c[0] == 0 and Dco[k].c[2] == 0
    return El(Dco[k].c[1], 0, Dco[k].c[3], 0) * ((-1) ** ((sum(k) + 1) // 2))


ok_D0 = Dco[(0, 0, 0)].is_zero() and all(Dco[k].is_zero() for k in ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
hess_ok = (Dreal((2, 0, 0)) == El(16 * Jf ** 2 * a2) and Dreal((0, 2, 0)) == El(16 * Jf ** 2 * b2)
           and all(Dreal(k).is_zero() for k in ((0, 0, 2), (1, 1, 0), (1, 0, 1), (0, 1, 1))))
s2f = (Jf + 2) / (2 * (Jf ** 3 - 4 * Jf - 4))
lowD = [k for k, v_ in Dco.items() if not v_.is_zero() and 2 * k[0] + 3 * k[1] + k[2] < 4]
ok_lin = (not lowD and Dodd((1, 0, 2)) == El(-2 * s2f * 16 * Jf ** 2 * a2) and Dreal((0, 0, 4)) == El(s2f ** 2 * Af * 16 * Jf ** 2 * a2))
gs = -g                                                         # zeta_u = zeta_u' + gs zeta_t^2
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
check("5 D = det H: Hessian rank two; weights (3,3,1): weights 0-5 vanish, weight 6 = c |d0|^2 (independent of the Schur route)", ok_D0 and hess_ok and ok_lin and ok_w6,
      f"D = c a^2 u^2 + c b^2 v^2 + ..., c = 16J^2, kernel t; weights (2,3,1): leading c a^2 (u - u2 t^2)^2 (degenerate); weight 6 = c (a^2 u'^2 + b^2 v^2 + g^2 t^6); "
      f"J=1: c a^2 = {at1(16 * Jf ** 2 * a2)}, c b^2 = {at1(16 * Jf ** 2 * b2)}, c g^2 = {at1(16 * Jf ** 2 * g2)}")

# ---- check 6: degree +1
orient = sp.Matrix([[1, -1], [1, 1]]).det()                         # d(u, v)/d(xi1, xi2)
a1f, b1f, g1f = (float(sp.sqrt(at1(x_))) for x_ in (a2, b2, g2))
check("6 local degree of d/|d| at the merged point is +1 for every J in (0, 2)", SG["det/WY"] == 1 and SG["a2"] == 1 and SG["b2"] == 1 and SG["g2"] == 1 and orient == 2 and ok_det and ok_gram,
      f"orthonormal frame (x_u/a, x_v/b, x_beta/g) of orientation +1: d0 = (a u', b v, g t^3), Jacobian 3abg t^2 >= 0, (u,v) -> (xi1,xi2) Jacobian {orient}; "
      f"sign T > 0, flux -1; J=1: d0 = ({a1f:.6f} u', {b1f:.6f} v, {g1f:.6f} t^3)")

# ---- check 7: unfolding in kappa
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
rho, okr = ratio(Se, Su)
epst = madd(Set, mscale(Sut, -rho))
mu, okm = ratio(epst, Sb)
mu_exp = El(8 * Af / (Jf ** 2 * (Jf + 2))) * YY
rho_exp = El(0, 4 * Jf / ((Jf + 2) * (Jf ** 3 - 4 * Jf - 4)), 0, 0) * YY
mus = sp.Symbol("mu", positive=True); tt = sp.Symbol("t", real=True)
charges = {}
for esg in (1, -1):
    nodes = [r for r in sp.solve(tt ** 3 - mus * esg * tt, tt) if r.is_real]
    charges[esg] = sorted(int(SG["det/WY"] * sp.sign((3 * tt ** 2 - mus * esg).subs(tt, r))) for r in nodes)
ok_unf = (set(S4.keys()) == {(0, 0, 2, 0), (1, 0, 0, 0), (0, 0, 0, 1), (0, 1, 0, 0), (0, 0, 1, 1), (1, 0, 1, 0)}
          and okr and rho == rho_exp and mtr(Se).is_zero() and okm and mu == mu_exp and mtr(epst).is_zero() and SG["mu/Y"] == 1
          and charges[1] == [-1, 1, 1] and charges[-1] == [1])
check("7 unfolding kappa = kappa_c + eps: d = x_u u'' + x_v v + x_beta (t^3 - mu eps t), mu > 0; charges (-,+,+) above, (+) below", ok_unf,
      f"weight <= 3 monomials {{t^2, u, eps, v, eps t, u t}}; Sigma_eps = rho Sigma_u; eps*t matrix = mu beta, mu = 8YA/(J^2(J+2)); "
      f"J=1: mu = {sq(sp.sqrt(15) * fx['mu/Y'].subs(Jx, 1))}; charges eps>0 {charges[1]}, eps<0 {charges[-1]}")

# ---- check 8: first-order consistency with the landed family formulas
mu_f = El(Jf + 2) * (KAPPA * KAPPA * KAPPA).inv()
W_sin = El(0, Jf / (Jf + 2), 0, 0)                                  # i sin 2 pi x = omega J/(J+2)
dd = (4 + 4 * Jf - Jf ** 3) / (4 + 2 * Jf - Jf ** 2)                # landed d at kappa_c
d_c_ok = El(dd * dd) == (El(1) + kc2 * 8 + kc2 * kc2 * 16 - kc2 * (4 * Jf ** 2))
dprime = (KAPPA * 16 + KAPPA * KAPPA * KAPPA * 64 - KAPPA * (8 * Jf ** 2)) * QQ(1, 2) * (1 / dd)
num = (-(dprime) * (kc2 * 4)) - (El(1) - El(dd)) * (KAPPA * 8)
dcos_line_landed = num * (1 / (16 * kc2.c[0] ** 2))
dcos_line_pred = W_sin * (-rho) * QQ(1, 2)                         # zeta_u = -rho eps at t = 0; d cos = -(sin/2) du
dcos_plane_pred = W_sin * (-rho + gs * (-mu)) * QQ(1, 2)           # zeta_t^2 = -mu eps on the plane nodes
dcos_plane_landed = El(Jf) * (KAPPA * KAPPA * KAPPA * 2).inv()
check("8 first-order consistency with the landed node families (plane f3, line x, plane x)",
      mu_f == mu_exp and d_c_ok and (dcos_line_landed - dcos_line_pred).is_zero() and (dcos_plane_landed - dcos_plane_pred).is_zero(),
      f"(2 pi f3)^2 = mu eps [d(1-cos 2 pi f3)/dk = (J+2)/(2 k^3) = mu/2]; d cos(line)/dk from (1-d)/(4k^2) and d cos(plane)/dk = J/(2k^3) equal the unfolding values; "
      f"J=1: {sq(sp.sqrt(15) * dcos_line_landed.c[2].as_expr().subs(Jx, 1))}, {sq(sp.sqrt(15) * dcos_plane_landed.c[2].as_expr().subs(Jx, 1))}")

# ---- check 9: exact sign facts
ok_sg = (SG == {"a2": 1, "b2": 1, "g2": 1, "mu/Y": 1, "det/WY": 1, "u2/W": -1}
         and sp.Poly(Aj, Jx).count_roots(0, 2) == 0 and sp.Poly(Jx ** 3 - 4 * Jx - 4, Jx).count_roots(0, 2) == 0 and sp.Poly(Jx + 1, Jx).count_roots(0, 2) == 0
         and Aj.subs(Jx, 1) > 0 and (Jx ** 3 - 4 * Jx - 4).subs(Jx, 1) < 0)
check("9 exact signs on 0 < J < 2 (factorisation + Sturm counts)", ok_sg,
      f"A > 0, J^3-4J-4 < 0 (no root in [0, 2]); a^2, b^2, g^2, mu/Y, det/(WY) > 0, u2/W < 0: {SG}; kappa_c = Y/(2A) > 0 (Y -> -Y flips only det)")

# ---- check 10: genus
Jg, Zg, om, rh, lam, mug = sp.symbols("Jg Zg omega rho lam mu")
Ah = 4 * Zg ** 2 + 2 * Jg * Zg - Jg ** 2
Q1 = om ** 2 + Ah; Q2 = rh ** 2 + Jg ** 2 + 2 * Jg * Zg
vars_ = (Jg, Zg, om, rh)
pencil = sp.factor((lam * sp.hessian(Q1, vars_) / 2 + mug * sp.hessian(Q2, vars_) / 2).det())
tq = sp.symbols("tq")
fcub = sp.Poly(pencil.subs({lam: tq, mug: 1}), tq)
roots = sp.roots(fcub, multiple=True)
Jac = sp.Matrix([[sp.diff(q, v) for v in vars_] for q in (Q1, Q2)])
gens = [Q1, Q2] + [Jac[:, [i, j]].det() for i in range(4) for j in range(i + 1, 4)]
unit = []
for sub in ({Zg: 1}, {Zg: 0, Jg: 1}, {Zg: 0, Jg: 0, om: 1}, {Zg: 0, Jg: 0, om: 0, rh: 1}):
    gg = [sp.expand(g_.subs(sub)) for g_ in gens]
    free = [v for v in vars_ if v not in sub]
    unit.append(list(sp.groebner(gg, *free, order="grevlex").exprs) == [1] if free else any(g_ != 0 for g_ in gg))
kap_rel = sp.simplify((rh / (2 * om)) ** 2).subs({rh ** 2: -Jg * (Jg + 2), om ** 2: -(4 + 2 * Jg - Jg ** 2)})
kap_ok = sp.simplify(kap_rel - Jg * (Jg + 2) / (4 * (4 + 2 * Jg - Jg ** 2))) == 0
check("10 no rational one-parameter parametrisation: data lie on a smooth intersection of two quadrics (genus 1)",
      len(roots) == 3 and len(set(roots)) == 3 and fcub.degree() == 3 and all(unit) and kap_ok,
      f"omega^2 + A = 0 = rho^2 + J(J+2) in P^3 (rho = iR, Y = -rho omega, kappa_c = rho/(2 omega)); det(lam Q1 + mu Q2) = {pencil}; Jacobian-minor ideal = (1) in 4 charts")

# ================================================================================================ float diagnostics
class Bloch:
    def __init__(self, J, kappa):
        self.T = terms(J, kappa)
        self.a = np.array([x[0] for x in self.T]); self.b = np.array([x[1] for x in self.T])
        self.n = np.array([x[2] for x in self.T], dtype=float); self.t = np.array([x[3] for x in self.T])

    def H(self, F):
        F = np.atleast_2d(F)
        ph = np.exp(2j * np.pi * F @ self.n.T)
        Mk = np.zeros((len(F), 4, 4), dtype=complex)
        for j in range(len(self.T)):
            Mk[:, self.a[j], self.b[j]] += self.t[j] * ph[:, j]
            Mk[:, self.b[j], self.a[j]] -= self.t[j] * np.conj(ph[:, j])
        return 1j * Mk

    def levels(self, F, vecs=False):
        return np.linalg.eigh(self.H(F)) if vecs else np.linalg.eigvalsh(self.H(F))


def _link(A_, B_):
    return np.linalg.det(np.einsum('...ia,...ib->...ab', A_.conj(), B_))


def _plaquettes(V):
    links = (_link(V[:-1, :-1], V[1:, :-1]), _link(V[1:, :-1], V[1:, 1:]), _link(V[1:, 1:], V[:-1, 1:]), _link(V[:-1, 1:], V[:-1, :-1]))
    assert all(np.isfinite(z).all() and np.min(np.abs(z)) > 1e-12 for z in links), "singular occupied-band overlap"
    return np.angle(links[0] * links[1] * links[2] * links[3])


def sphere_chern(B, c, s, m=64, nocc=2):
    """Berry flux/2pi of the lowest nocc bands on the sphere |f - c| = s (outward), Fukui link method on a latitude-longitude grid; also the smallest middle gap met."""
    th = np.linspace(0, np.pi, m + 1)
    ph = np.linspace(0, 2 * np.pi, 2 * m + 1)
    Pp = np.stack([np.sin(th)[:, None] * np.cos(ph)[None, :], np.sin(th)[:, None] * np.sin(ph)[None, :],
                   np.cos(th)[:, None] * np.ones_like(ph)[None, :]], axis=-1) * s + c
    ev, Vv = B.levels(Pp.reshape(-1, 3), vecs=True)
    Vv = Vv[:, :, :nocc].reshape(m + 1, 2 * m + 1, 4, nocc).copy()
    Vv[0, :] = Vv[0, 0]; Vv[-1, :] = Vv[-1, 0]; Vv[:, -1] = Vv[:, 0]
    return _plaquettes(Vv).sum() / (2 * np.pi), float((ev[:, 2] - ev[:, 1]).min())


def float_effective(J, kappa, f0):
    """Independent float Schur complement: kernel basis by eigh, analytic derivatives of H, tensors S1, S2, S3 of 2x2 matrices (xi_j = 2 pi delta_j)."""
    Tt = terms((1.0, 1.0, J), kappa)
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
    return S1, S2, S3


def pauli(M):
    """Hermitian 2x2 M = s0 + dx sigma_x + dy sigma_y + dz sigma_z -> (s0, dx, dy, dz)."""
    return np.array([(M[0, 0] + M[1, 1]).real / 2, M[0, 1].real, M[1, 0].imag, (M[0, 0] - M[1, 1]).real / 2])


MON = [(i, j, k) for i in range(4) for j in range(4 - i) for k in range(4 - i - j)]


def float_jets(J):
    kc = np.sqrt(J * (J + 2) / (4 * (4 + 2 * J - J * J))); x = np.arccos((J - 2) * (J + 1) / (J + 2)) / (2 * np.pi)
    S1, S2, S3 = float_effective(J, kc, np.array([x, 1 - x, 0.0]))

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
    xv = {m: pauli(jt[m])[1:] for m in MON if sum(m) >= 1}
    s0 = max(abs(pauli(jt[m])[0]) for m in MON if sum(m) >= 1 and 2 * m[0] + 3 * m[1] + m[2] <= 3)
    xu, xvv, xt, xtt, xut, xttt = xv[(1, 0, 0)], xv[(0, 1, 0)], xv[(0, 0, 1)], xv[(0, 0, 2)], xv[(1, 0, 1)], xv[(0, 0, 3)]
    a, b = np.linalg.norm(xu), np.linalg.norm(xvv)
    u2 = -(xtt @ xu) / a ** 2
    beta = xttt + u2 * xut
    van = max(np.linalg.norm(xt), np.linalg.norm(xttt), np.linalg.norm(xtt + u2 * xu), s0, abs(xu @ xvv), abs(beta @ xu), abs(beta @ xvv))
    return dict(a=a, b=b, u2=u2, g=np.linalg.norm(beta), det=np.linalg.det(np.array([xu, xvv, beta])), van=van)


def exact_float(J):
    A = 4 + 2 * J - J * J; W = np.sqrt(A); Yv = np.sqrt(J * (J + 2) * A)
    return dict(a=(4 + 4 * J - J ** 3) / ((J + 2) * W), b=J * (J + 1) * np.sqrt(2 * J) / ((J + 2) * W), u2=W * (J + 2) / (2 * (J ** 3 - 4 * J - 4)),
                g=J ** 2 * np.sqrt(J + 2) / (2 * np.sqrt(2) * (4 + 4 * J - J ** 3)), det=W * Yv * J ** 3 * (J + 1) / (2 * (J + 2) ** 2 * A ** 2))


reldev = 0.0; vanmax = 0.0; fluxes = []; mirror = []; gaps = []
for Jv in (0.4, 1.0, 1.6):
    fj = float_jets(Jv); ej = exact_float(Jv)
    reldev = max(reldev, max(abs(fj[k] - ej[k]) / abs(ej[k]) for k in ("a", "b", "u2", "g", "det")))
    vanmax = max(vanmax, fj["van"])
    kc = np.sqrt(Jv * (Jv + 2) / (4 * (4 + 2 * Jv - Jv * Jv))); x = np.arccos((Jv - 2) * (Jv + 1) / (Jv + 2)) / (2 * np.pi)
    Bq = Bloch((1.0, 1.0, Jv), kc)
    for r in (0.004, 0.008):
        fl, gp = sphere_chern(Bq, np.array([x, 1 - x, 0.0]), r)
        fluxes.append(fl); gaps.append(gp)
    flm, gpm = sphere_chern(Bq, np.array([1 - x, x, 0.0]), 0.004)
    mirror.append(flm); gaps.append(gpm)
ok_float = (reldev < 1e-9 and vanmax < 1e-11 and all(abs(f_ + 1) < 1e-6 for f_ in fluxes) and all(abs(f_ - 1) < 1e-6 for f_ in mirror) and min(gaps) > 0)
check("11 FLOAT (not certified): independent float Schur code vs exact forms; sphere Berry fluxes -1 (merged), +1 (mirror)", ok_float,
      f"J = 0.4, 1.0, 1.6: max rel dev of a, b, u2, g, det {reldev:.1e}, max vanishing part {vanmax:.1e}; fluxes r = 0.004, 0.008: "
      f"{[round(float(f_), 6) for f_ in fluxes]}, mirror {[round(float(f_), 6) for f_ in mirror]}; min grid gap {min(gaps):.1e}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
