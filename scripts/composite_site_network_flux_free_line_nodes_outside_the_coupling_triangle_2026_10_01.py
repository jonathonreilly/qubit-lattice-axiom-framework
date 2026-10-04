#!/usr/bin/env python3
"""Composite-site network, supplied u = +1 quadratic Majorana comparator: the line touchings f = (x, 1-x, 0) OUTSIDE the triangle regime |Jx-Jy| < Jz < Jx+Jy,
all couplings Jx, Jy, Jz > 0 and odd term kappa > 0.  Nothing here is an axiom of the framework: this is a supplied model, and the statements are about it.

Setting.  Four-site Bloch matrix H(f) = i M(f) of the landed composite-site (hyperhoneycomb-in-doubled-cubic) network with the landed hopping-sign convention and gauge u = +1
(terms rebuilt below from the network rules).  Notation: s = Jx + Jy, P = Jx Jy, S = Jx^2 + Jy^2 - Jz^2, u = kappa^2, c = cos 2 pi x, t1 = s^2 - Jz^2, t2 = Jz^2 - (Jx-Jy)^2
(t1 + t2 = 4P, so t1 and t2 are never both <= 0), q(c) = 4u c^2 - 2P c - (4u + S), F_c(c) = P(s+Jz) c^2 + s(s^2+Jz s-2P) c + (Jx+Jz)(Jy+Jz)(s-Jz).
Region (a): Jz <= |Jx-Jy| (t2 <= 0).  Region (b): Jz >= Jx+Jy (t1 <= 0).  chi := sign T, T = Im Tr(P d1H P d2H P d3H) (P = kernel projector); the Fukui Chern number of the
lowest two bands around a node is -chi in this convention (float controls below).  The x > 1/2 partner (1-x, x, 0) of a node has the opposite charge.

EXACT statements (sympy, polynomial identities over Q[Jx,Jy,Jz,kappa] or Q[s,P,Jz,u], sign arguments written in the labels and in REPORT.txt):
 L  all couplings: the spectrum of H(f) is {+-l1, +-l2} at every f (no mu^3, mu^1 term), so det H = l1^2 l2^2 >= 0 and the middle bands touch iff det H = 0; on the line
    det H = 16 q(c)^2 and e2 = l1^2 + l2^2 = 16 Jz^2 at a root of q (simple or double): the kernel is exactly 2-dim and the other levels are +-4 Jz; T = -32 pi^3 kappa q'(c) F_c(c) sin(2 pi x)/Jz^3;
    independently det Hess_theta(det H) = 2^17 kappa^2 q'^2 F_c^2 (1-c^2) mod q.  Since det H >= 0 vanishes at a node, Hess det H is positive semidefinite there; hence at a simple
    root with F_c != 0 it is positive definite: an isolated, untilted touching (levels +-l2 with l2^2 = det H/e2 (1 + O(det H))), with charge chi = sign T = -sign(q') sign(F_c) (x < 1/2).
 A  region (a): q = -4u(1-c^2) - 2P(1+c) + t2 < 0 on (-1,1) for every u >= 0: NO line node at any kappa.  Boundary Jz = |Jx-Jy|: q = -2(1+c)(2u(1-c)+P), sole root c = -1, the TRIM
    M = (1/2,1/2,0), at every kappa; there (weights x:1, y,z:2, both orders Jx > Jy, Jx < Jy) the Schur-complement Pauli vector has a = -(P+4u)/(Jx-Jy) != 0 for all u >= 0, det H(4th order) = 16 Jz^2 |d|^2,
    Jacobian odd in x: isolated zero, local degree 0, never a birth point.
 B  region (b), Jz > s: q = -4(1-c^2)(u - u(c)), u(c) = -(2Pc+S)/(4(1-c^2)); Fb = Pc^2 + Sc + P has one root c_b in (0,1); u(c) falls on (-1,c_b), rises on (c_b,1), -> +inf at both ends.  Hence
    q has a root in (-1,1) iff u >= u_* = (-S + sqrt(S^2-4P^2))/8 = u(c_b); u = u_*: one DOUBLE root c_b = P/(4u_*) (q = 4u_*(c-c_b)^2, det H ~ (x-x_b)^4 on the line); u > u_*: two SIMPLE roots
    c1 < c_b < c2 (each a double zero of det H), c1 falling to -1, c2 rising to 1 as u grows; det H vanishes nowhere else on the line (q is quadratic).  Charges (x < 1/2): chi(c1) = +sign F_c(c1), chi(c2) = -sign F_c(c2).
    F_c is convex, F_c(-1) < 0, F_c(0) < 0: it has one zero c_F in (0,1) iff Jz < phi s (phi = golden ratio), none (F_c < 0 on (-1,1)) for Jz >= phi s.  Res_c(F_c, Fb) = -Jz^2 P (Jz+s) G(s,P,Jz)
    = P^2 F_c(c_b) F_c(1/c_b), G strictly increasing in Jz >= s with G(s) < 0 < G(phi s): a unique J0(Jx,Jy) in (s, phi s) (iso: Jz^3 - 4Jz - 4 = 0, J0 = 2.3830).  Consequences:
      Jz >= phi s     : born pair (chi) = (-1,+1), no flip, for all kappa > kappa_*;
      J0 < Jz < phi s : born (-1,+1); the c2 node flips +1 -> -1 at u_f; both -1 afterwards;
      Jz = J0         : u_f = u_* and the pair is born as (-1,-1) (line charge -2 at the merger);
      s < Jz < J0     : born (+1,-1); the c1 node flips +1 -> -1 at u_f; both -1 afterwards.
    u_f = u(c_F^+) = u_+ = (N0 + N1 sqrt(Delta_F))/Den, the larger root of R2 = A2 u^2 + B2 u + C2 (Res_c(q,F_c) = -(s+Jz) R2, R2 irreducible); the other root u_- = u(c_F^-) < 0.
    At u_* (G != 0) the merger is a pair creation: charges sign F_c(c_b) and -sign F_c(c_b), line charge sum 0.  Exact samples Jx = Jy = 1: Jz = 13/6, 5/2, 29/10, 10/3.
 C  boundary Jz = s: q = (c-1)(4u(c+1) - 2P): c = 1 (the TRIM Gamma) at every kappa, second root c_2 = P/(2u) - 1 in (-1,1) iff u > P/4 (double at c = 1 iff u = P/4: pair born at Gamma);
    F_c = 2 s c (Pc + s^2 - P): charge +1 for P/4 < u < P/2 and -1 for u > P/2, flip at kappa^2 = P/2 = u_+(Jz = s).  At Gamma the Schur Pauli vector is d = (2Jy y - s z, (P-4u) x^2/s, -8 kappa y)
    (u != P/4) and d = (2Jy y - s z, P x^4/(4s), -8 kappa y) with weights x:1, y,z:4 (u = P/4); det H at the leading order = 16 Jz^2 |d|^2; the Jacobian is odd in x: isolated zero, local degree 0.
FLOAT diagnostics (double precision, consistency checks, never certified): Bloch-matrix kernel-projector triple product vs the closed form; sign patterns across J0 and across u_f; region (a) positivity of det H on the line;
  Fukui fluxes around the merger, around Gamma and M (resolved: max plaquette phase < 1).
CAVEATS: (i) the TRIM statements are weighted Taylor (Schur-complement) statements with unquantified remainder radius, and the reading of the degree of the Pauli vector as the Chern number is the landed
  two-level reduction (not re-proved); (ii) the 3D local structure of the merger away from a TRIM is not computed exactly: its degree 0 rests on the exact charges of the two merging nodes and on float fluxes;
  (iii) at u_f and at Jz = J0 the line node has T = 0 and its charge changes by 2: off-line nodes would carry compensating charge if a common zero-free enclosing surface persists (not certified here); (iv) off-line nodes are not analysed in any region.
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import random
import time
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.optimize import brentq
from sympy import ZZ
from sympy.polys.rings import ring

AUDIT_TIMEOUT_SEC = 120

RESULTS = []
T0 = time.time()
VERBOSE = bool(os.environ.get("OTRI_VERBOSE"))


def check(label, ok, detail="", note=""):
    """detail: printed on FAIL or with OTRI_VERBOSE=1; note: short result line, always printed."""
    RESULTS.append(bool(ok))
    show = detail if (VERBOSE or not ok) else ""
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {note}" if note else "") + (f"\n        {show}" if show else ""), flush=True)


def allok(conds):
    bad = [i for i, c_ in enumerate(conds) if not c_]
    return (not bad), (f" FAILED sub-conditions {bad}" if bad else "")


# ------------------------------------------------------------------------------------------------ network terms (landed rules, rebuilt)
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


def reduce(p):
    """p = rep + n1 a1 + n2 a2 + n3 a3 (a1 = (2,0,0), a2 = (0,2,0), a3 = (1,1,2)); returns (rep index, n)."""
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)


def terms(J, kappa):
    out = []
    for p in REPS:
        a, n0 = reduce(p)
        assert n0 == (0, 0, 0) and is_site(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce(q)
                out.append((a, b, n, 2.0 * J[AX[flavour(p, q)]]))
        if kappa:
            nb = {flavour(p, q): q for q in neighbours(p)}
            assert len(nb) == 3
            for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
                r1, n1 = reduce(nb[l]); r2, n2 = reduce(nb[m])
                out.append((r1, r2, tuple(np.subtract(n2, n1)), 2.0 * kappa))
    return out


_KIND = {2.0: "x", 6.0: "y", 14.0: "z", 0.6: "odd"}      # amplitudes tagged by running terms() at J = (1,3,7), kappa = 0.3
TERMS = [(int(a), int(b), tuple(int(v) for v in n), _KIND[round(float(t), 9)]) for (a, b, n, t) in terms((1.0, 3.0, 7.0), 0.3)]
assert len(TERMS) == 18


class Bloch:
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

    def levels(self, F, vecs=False):
        return np.linalg.eigh(self.H(F)) if vecs else np.linalg.eigvalsh(self.H(F))




Jx, Jy, Jz, kk = sp.symbols("Jx Jy Jz kk")
w1, w2, w3 = sp.symbols("w1 w2 w3")


def M_sym(z1=w1, z2=w2, z3=w3, J=(Jx, Jy, Jz), kappa=kk):
    """Anti-hermitian Laurent matrix M (sympy 4x4) in z_j (H = i M)."""
    amp = {"x": 2 * J[0], "y": 2 * J[1], "z": 2 * J[2], "odd": 2 * kappa}
    M = sp.zeros(4, 4)
    for (a_, b_, n_, kind_) in TERMS:
        mon = z1 ** n_[0] * z2 ** n_[1] * z3 ** n_[2]
        M[a_, b_] += amp[kind_] * mon
        M[b_, a_] -= amp[kind_] / mon
    return M


# ================================================================================================ notation (exact part)
# s = Jx + Jy, P = Jx Jy, S = Jx^2 + Jy^2 - Jz^2 = s^2 - 2P - Jz^2, u = kappa^2, c = cos 2 pi x on the line f = (x, 1-x, 0)
# t1 = s^2 - Jz^2 = S + 2P,  t2 = Jz^2 - (Jx - Jy)^2 = 2P - S,  t1 + t2 = 4P.
# Region (a): t2 <= 0 (Jz <= |Jx-Jy|).  Region (b): t1 <= 0 (Jz >= Jx+Jy).  Triangle regime: t1 > 0 and t2 > 0.  (t1 and t2 cannot both be <= 0.)
s, P, u, c, r = sp.symbols("s P u c r")
c = sp.Symbol("c")
S_ = s ** 2 - 2 * P - Jz ** 2
t1 = s ** 2 - Jz ** 2
t2 = Jz ** 2 - s ** 2 + 4 * P
q = 4 * u * c ** 2 - 2 * P * c - (4 * u + S_)
Fb = P * c ** 2 + S_ * c + P                                     # du/dc = -Fb/(2(1-c^2)^2) for u(c) = -(2Pc+S)/(4(1-c^2))
a2 = P * (s + Jz); a1 = s * (s ** 2 + Jz * s - 2 * P); a0 = (P + Jz * s + Jz ** 2) * (s - Jz)
Fc = a2 * c ** 2 + a1 * c + a0
ucf = lambda cc: -(2 * P * cc + S_) / (4 * (1 - cc ** 2))
sub_xy = {s: Jx + Jy, P: Jx * Jy}


# ================================================================================================ (L) exact identities on the line, general couplings
def zero_mod_q_xy(f):
    qx = q.subs(sub_xy).subs(u, kk ** 2)
    return sp.expand(sp.prem(sp.Poly(sp.expand(f), c), sp.Poly(sp.expand(qx), c)).as_expr()) == 0


q_xy = sp.expand(q.subs(sub_xy).subs(u, kk ** 2))
Fc_xy = sp.expand(Fc.subs(sub_xy))
mu_, z_ = sp.symbols("mu z_")
Mg = M_sym()
cpg = {e: sp.expand(co) for (e,), co in sp.Poly(sp.expand((mu_ * sp.eye(4) - Mg).det(method="berkowitz")), mu_).terms()}
Ml = M_sym(z_, 1 / z_, sp.Integer(1))
cpl = {e: sp.expand(co) for (e,), co in sp.Poly(sp.expand((mu_ * sp.eye(4) - Ml).det(method="berkowitz")), mu_).terms()}
cz_ = (z_ + 1 / z_) / 2
e2_line = 8 * (Jx ** 2 + Jy ** 2 + Jz ** 2 + 2 * Jx * Jy * c + 4 * kk ** 2 * (1 - c ** 2))
ok, bad = allok([sp.simplify(Mg.trace()) == 0, cpg.get(3, 0) == 0, cpg.get(1, 0) == 0, sp.expand(cpl[0] - 16 * q_xy.subs(c, cz_) ** 2) == 0,
                 sp.expand(cpl[2] - e2_line.subs(c, cz_)) == 0, zero_mod_q_xy(e2_line - 16 * Jz ** 2)])
check("L1 charpoly(M) has no mu^3, mu^1 term (levels +-l1, +-l2, det H >= 0); on the line det H = 16 q(c)^2, e2 = 16 Jz^2 mod q", ok,
      "q = 4u c^2 - 2P c - (4u+S)" + bad)

# ring arithmetic in Z[Jx,Jy,Jz,kk,c][z]/(z^2 - 2 c z + 1): element (a, b) = a + b z
R_, rJx, rJy, rJz, rk, rc = ring("Jx,Jy,Jz,kk,c", ZZ)
ZERO = (R_.zero, R_.zero); ONE = (R_.one, R_.zero); Zg = (R_.zero, R_.one); Zinv = (2 * rc, -R_.one)
add = lambda a, b: (a[0] + b[0], a[1] + b[1])
sub = lambda a, b: (a[0] - b[0], a[1] - b[1])
scal = lambda a, s_: (a[0] * s_, a[1] * s_)


def mul(a, b):
    bd = a[1] * b[1]
    return (a[0] * b[0] - bd, a[0] * b[1] + a[1] * b[0] + 2 * rc * bd)


ZP = {0: ONE}
for e_ in range(1, 4):
    ZP[e_] = mul(ZP[e_ - 1], Zg); ZP[-e_] = mul(ZP[-e_ + 1], Zinv)
AMPR = {"x": 2 * rJx, "y": 2 * rJy, "z": 2 * rJz, "odd": 2 * rk}
mz = lambda: [[ZERO for _ in range(4)] for _ in range(4)]


def mm_(A, B):
    out = mz()
    for r_ in range(4):
        for q_ in range(4):
            sm = ZERO
            for m_ in range(4):
                if A[r_][m_] != ZERO and B[m_][q_] != ZERO:
                    sm = add(sm, mul(A[r_][m_], B[m_][q_]))
            out[r_][q_] = sm
    return out


trc = lambda A: add(add(A[0][0], A[1][1]), add(A[2][2], A[3][3]))
Mr = mz(); Nr = [mz() for _ in range(3)]
for (a_, b_, n_, kind_) in TERMS:
    t_ = AMPR[kind_]; e_ = n_[0] - n_[1]
    Mr[a_][b_] = add(Mr[a_][b_], scal(ZP[e_], t_)); Mr[b_][a_] = sub(Mr[b_][a_], scal(ZP[-e_], t_))
    for j in range(3):
        if n_[j]:
            Nr[j][a_][b_] = add(Nr[j][a_][b_], scal(ZP[e_], t_ * n_[j])); Nr[j][b_][a_] = add(Nr[j][b_][a_], scal(ZP[-e_], t_ * n_[j]))
M2r = mm_(Mr, Mr)
E2x2 = sub(mul(trc(Mr), trc(Mr)), trc(M2r))                       # 2 e2(M) (tr M = 0)
Pt2 = [[add(scal(M2r[i_][j_], 2), E2x2) if i_ == j_ else scal(M2r[i_][j_], 2) for j_ in range(4)] for i_ in range(4)]     # 2 Pt, Pt = M^2 + e2 I
MP = mm_(Mr, Pt2); PP = mm_(Pt2, Pt2); trP = trc(Pt2)
zq = lambda el: zero_mod_q_xy(el[0].as_expr()) and zero_mod_q_xy(el[1].as_expr())
ok_mp = all(zq(MP[i_][j_]) for i_ in range(4) for j_ in range(4))
ok_pp = all(zq(sub(PP[i_][j_], mul(E2x2, Pt2[i_][j_]))) for i_ in range(4) for j_ in range(4))


def det3(A):
    g = lambda i_, j_: A[i_][j_]
    t_1 = mul(g(0, 0), sub(mul(g(1, 1), g(2, 2)), mul(g(1, 2), g(2, 1))))
    t_2 = mul(g(0, 1), sub(mul(g(1, 0), g(2, 2)), mul(g(1, 2), g(2, 0))))
    t_3 = mul(g(0, 2), sub(mul(g(1, 0), g(2, 1)), mul(g(1, 1), g(2, 0))))
    return add(sub(t_1, t_2), t_3)


ok_adj = all(zq(det3([[Mr[r_][q_] for q_ in range(4) if q_ != j_] for r_ in range(4) if r_ != i_])) for i_ in range(4) for j_ in range(4))
ok, bad = allok([zero_mod_q_xy(E2x2[0].as_expr() - 32 * Jz ** 2), E2x2[1] == R_.zero, ok_mp, ok_pp,
                 zero_mod_q_xy((trP[0] - 2 * E2x2[0]).as_expr()) and zero_mod_q_xy((trP[1] - 2 * E2x2[1]).as_expr()), ok_adj])
check("L2 mod q, simple and double roots: M Pt = 0, Pt^2 = e2 Pt, tr Pt = 2 e2, rank M = 2: kernel 2-dim, levels 0,0,+-4Jz", ok, "Pt = M^2 + e2 I, e2 = 16 Jz^2" + bad)
X_ = [mm_(Pt2, Nr[j]) for j in range(3)]
Y_ = mm_(X_[0], X_[1])
Rr = ZERO
for i_ in range(4):
    for j_ in range(4):
        if Y_[i_][j_] != ZERO and X_[2][j_][i_] != ZERO:
            Rr = add(Rr, mul(Y_[i_][j_], X_[2][j_][i_]))
A_r = Rr[0].as_expr(); B_r = Rr[1].as_expr()                      # 8 R = A + B z, R = Tr(Pt N1 Pt N2 Pt N3), N_j = z_j dM/dz_j
delta_ = Jx * Jy - 4 * kk ** 2 * c
th_ = sp.Symbol("sinth")
a_coeff = -2 ** 15 * Jz ** 3 * kk * delta_ * Fc_xy
T_expr = -(2 * sp.pi) ** 3 * a_coeff * th_ / (16 * Jz ** 2) ** 3
T_claim = -32 * sp.pi ** 3 * kk * sp.diff(q_xy, c) * Fc_xy * th_ / Jz ** 3
ok, bad = allok([zero_mod_q_xy(A_r + c * B_r), zero_mod_q_xy(B_r + 2 ** 18 * Jz ** 3 * kk * delta_ * Fc_xy), sp.simplify(T_expr - T_claim) == 0, sp.expand(sp.diff(q_xy, c) + 2 * delta_) == 0])
check("L3 T = Im Tr(P d1H P d2H P d3H) = -32 pi^3 kappa q'(c) F_c(c) sin(2 pi x)/Jz^3 (exact trace mod q)", ok,
      "F_c = P(s+Jz)c^2 + s(s^2+Jz s-2P)c + (Jx+Jz)(Jy+Jz)(s-Jz)" + bad)
Dfull = sp.expand(Mg.det(method="berkowitz"))
wsy = (w1, w2, w3)
dth = lambda e, w: sp.expand(sp.I * w * sp.diff(e, w))
Hs = sp.Matrix(3, 3, lambda i_, j_: dth(dth(Dfull, wsy[i_]), wsy[j_]))
Hz = Hs.subs({w1: z_, w2: 1 / z_, w3: sp.Integer(1)}).applyfunc(sp.expand)
dHz = sp.expand(Hz.det(method="berkowitz"))
pz = sp.Poly(sp.expand(dHz * z_ ** 20), z_)
coef = {m_[0] - 20: co for m_, co in pz.terms()}
sym_ok = all(sp.expand(coef.get(n_, 0) - coef.get(-n_, 0)) == 0 for n_ in range(1, 21))
polyc = sp.expand(coef.get(0, 0) + sum(2 * coef.get(n_, 0) * sp.chebyshevt(n_, c) for n_ in range(1, 21)))
target = 2 ** 17 * kk ** 2 * sp.diff(q_xy, c) ** 2 * Fc_xy ** 2 * (1 - c ** 2)
check("L4 det Hess_theta(det H) = 2^17 kappa^2 q'^2 F_c^2 (1-c^2) mod q: with D >= 0, Hess D > 0 at simple roots with F_c != 0",
      sym_ok and zero_mod_q_xy(polyc - target))


# ================================================================================================ (A) region (a): Jz <= |Jx - Jy|
# q = -4u(1-c^2) - 2P(1+c) + t2 with t2 <= 0: every term is <= 0 and the first two are < 0 on (-1,1) for u >= 0, so q < 0 there: no line root.
ok_id = (sp.expand(q - (-4 * u * (1 - c ** 2) - 2 * P * (1 + c) + t2)) == 0 and sp.expand(q.subs(c, 1) + t1) == 0 and sp.expand(q.subs(c, -1) - t2) == 0
         and sp.expand(t1 + t2 - 4 * P) == 0 and sp.expand(t2.subs(sub_xy) - (Jz ** 2 - (Jx - Jy) ** 2)) == 0)
rng = random.Random(11)
n_grid = n_bad = 0
for _ in range(300):
    jx, jy = Fr(rng.randint(1, 60), 10), Fr(rng.randint(1, 60), 10)
    lo = abs(jx - jy)
    if lo == 0:
        continue
    jz = lo * Fr(rng.randint(1, 100), 100)
    uu = Fr(rng.randint(0, 300), 100)
    Pv = jx * jy; Sv = jx * jx + jy * jy - jz * jz
    for k_ in range(-49, 50):
        cv = Fr(k_, 50)
        n_grid += 1; n_bad += int(4 * uu * cv * cv - 2 * Pv * cv - (4 * uu + Sv) >= 0)
check("A1 region (a), Jz <= |Jx-Jy|: q = -4u(1-c^2) - 2P(1+c) + t2 < 0 on (-1,1): no line node at any kappa", ok_id and n_bad == 0,
      "q(1) = -t1 < 0, q(-1) = t2 <= 0: every term of the identity is <= 0", note=f"exact rational grid {n_grid} pts, none with q >= 0")
dd_ = sp.Symbol("dd")
qb = sp.expand(q.subs(Jz, sp.sqrt(s ** 2 - 4 * P)))
ok_bd = (sp.expand(qb + 2 * (1 + c) * (2 * u * (1 - c) + P)) == 0 and sp.expand(sp.diff(q, c).subs({c: -1}) + 8 * u + 2 * P) == 0
         and sp.expand((2 * u * (1 - c) + P).subs(c, 1) - P) == 0 and sp.expand((2 * u * (1 - c) + P).subs(c, -1) - (4 * u + P)) == 0)
check("A2 boundary Jz = |Jx-Jy|: q = -2(1+c)(2u(1-c)+P): sole root c = -1 (TRIM M) at every kappa; det H ~ (x-1/2)^4", ok_bd,
      "q'(-1) = -(8u+2P) != 0 (simple in c), 1+c = 2cos^2(pi x) (double in x)")

# ================================================================================================ (B) region (b): Jz > Jx + Jy
Dd = sp.expand(S_ ** 2 - 4 * P ** 2)
ok, bad = allok([sp.expand(Fb.subs(c, -1) - t2) == 0, sp.expand(Fb.subs(c, 1) - t1) == 0, sp.expand(Fb.subs(c, 0) - P) == 0, sp.expand(Fb - c ** 2 * Fb.subs(c, 1 / c)) == 0,
                 sp.expand(Dd + t1 * t2) == 0, sp.simplify(q + 4 * (1 - c ** 2) * (u - ucf(c))) == 0, sp.simplify(sp.diff(ucf(c), c) + Fb / (2 * (1 - c ** 2) ** 2)) == 0,
                 sp.expand(-(-2 * P + S_) - t2) == 0, sp.expand(-(2 * P + S_) + t1) == 0])
check("B1 region (b), Jz > s: q = -4(1-c^2)(u - u(c)); Fb palindromic, Fb(-1) = t2 > 0, Fb(0) = P, Fb(1) = t1 < 0: u(c) U-shaped, min at c_b in (0,1)", ok,
      "so Fb has one root c_b in (0,1): u falls on (-1,c_b), rises on (c_b,1); u_* = u(c_b) is its minimum" + bad)
cb = (-S_ - r) / (2 * P); cb2 = (-S_ + r) / (2 * P); ustar = (-S_ + r) / 8


def red(expr):
    num = sp.numer(sp.together(expr))
    return sp.rem(sp.Poly(sp.expand(num), r), sp.Poly(r ** 2 - Dd, r)).as_expr()


ok, bad = allok([red(Fb.subs(c, cb)) == 0, red(Fb.subs(c, cb2)) == 0, red(cb * cb2 - 1) == 0, red(q.subs({c: cb, u: ustar})) == 0,
                 red(sp.diff(q, c).subs({c: cb, u: ustar})) == 0, red(4 * ustar * cb - P) == 0, red(16 * ustar ** 2 + 4 * S_ * ustar + P ** 2) == 0,
                 sp.expand(sp.discriminant(q, c) - 4 * (16 * u ** 2 + 4 * S_ * u + P ** 2)) == 0, red(ustar * (-S_ - r) / 8 - P ** 2 / 16) == 0])
check("B2 u_* = (-S + sqrt(S^2-4P^2))/8 = u(c_b), q = 4u_*(c-c_b)^2 (double root); two simple roots c1 < c_b < c2 for u > u_*, none below", ok,
      "r^2 = S^2-4P^2 = -t1 t2; other disc root u_-' = (-S-r)/8 has vertex P/(4u) = 1/c_b > 1" + bad)
phi = (1 + sp.sqrt(5)) / 2; phib = (1 - sp.sqrt(5)) / 2
ok, bad = allok([sp.expand(Fc.subs(c, 1) - (s + Jz) * (s ** 2 + Jz * s - Jz ** 2)) == 0, sp.expand(Fc.subs(c, -1) + s * (s ** 2 - 4 * P) + Jz ** 3) == 0,
                 sp.expand(sp.expand(s ** 2 + Jz * s - Jz ** 2) + sp.expand((Jz - phi * s) * (Jz - phib * s))) == 0,
                 sp.expand((a0 - (Jx + Jz) * (Jy + Jz) * (Jx + Jy - Jz).subs(sub_xy)).subs(sub_xy)) == 0, sp.expand(Fc.subs(c, 0) - a0) == 0])
check("B3 F_c convex, F_c(-1) < 0, F_c(0) < 0: one zero c_F in (0,1) iff Jz < phi s (phi = golden ratio); F_c < 0 on (-1,1) for Jz >= phi s", ok,
      "unique root c_F in (0,1) iff Jz < phi s (phi = 1.618..), none (F_c < 0 on (-1,1)) for Jz >= phi s" + bad)
G = Jz ** 5 + (4 * P - 2 * s ** 2) * Jz ** 3 - 2 * P * s * Jz ** 2 + (4 * P ** 2 - 5 * P * s ** 2 + s ** 4) * Jz + P * s ** 3 - 4 * P ** 2 * s
Res = sp.resultant(sp.Poly(Fc, c), sp.Poly(Fb, c))
e1b = -S_ / P
prodF = a2 ** 2 + a2 * a1 * e1b + a2 * a0 * (e1b ** 2 - 2) + a1 ** 2 + a1 * a0 * e1b + a0 ** 2           # F_c(c_b) F_c(1/c_b) via r1 r2 = 1, r1 + r2 = -S/P
zt, pp = sp.symbols("zeta p", positive=True)
g = G.subs({s: 1, P: pp, Jz: zt})
ok, bad = allok([sp.expand(Res + Jz ** 2 * P * (Jz + s) * G) == 0, sp.simplify(P ** 2 * prodF - Res) == 0,
                 sp.expand(G.subs({s: 2 * s, P: 4 * P, Jz: 2 * Jz}, simultaneous=True) - 32 * G) == 0,
                 sp.expand(g.subs(zt, 1) + 2 * pp) == 0, sp.expand(sp.diff(g, zt).subs(zt, 1) - (3 * pp + 4 * pp ** 2)) == 0,
                 sp.expand(sp.diff(g, zt, 2) - (20 * zt ** 3 + (24 * pp - 12) * zt - 4 * pp)) == 0,
                 sp.simplify(g.subs(zt, phi) - ((2 * phi + 1) + (phi + 3) * pp + 4 * (phi - 1) * pp ** 2)) == 0,
                 sp.expand(G.subs({s: 2, P: 1}) - Jz ** 2 * (Jz ** 3 - 4 * Jz - 4)) == 0])
check("B4 Res(F_c,Fb) = -Jz^2 P (Jz+s) G = P^2 F_c(c_b) F_c(1/c_b); G increasing: unique J0 in (s, phi s); F_c(c_b) > 0 iff Jz < J0", ok,
      "p = P/s^2 in (0,1/4]; F_c(c_b) > 0 iff G < 0 iff Jz < J0 (F_c(1/c_b) > 0); iso G = Jz^2 (Jz^3 - 4Jz - 4), J0 = 2.3830" + bad)


# ================================================================================================ (B') the flip coupling (zero of F_c on a line root), general couplings
res = sp.expand(sp.resultant(sp.Poly(Fc, c), sp.Poly(q, c)))
fl = sp.factor_list(res)
big = [f_ for f_, m_ in fl[1] if sp.degree(f_, u) == 2]
A2c = 16 * (s ** 2 + Jz * s - Jz ** 2) * (Jz ** 3 - 4 * P * s + s ** 3)
N0 = S_ * (2 * Jz ** 3 * P - 4 * Jz * P * s ** 2 + Jz * s ** 4 - 4 * P * s ** 3 + s ** 5)
B2c = 4 * N0
C2c = P ** 2 * (s + Jz) * (s ** 4 - 4 * P * s ** 2 - Jz ** 4)
R2 = A2c * u ** 2 + B2c * u + C2c
Delta_cf = (4 * Jz ** 4 * P + 4 * Jz ** 3 * P * s + 4 * Jz ** 2 * P ** 2 - 4 * Jz ** 2 * P * s ** 2 + Jz ** 2 * s ** 4 - 8 * Jz * P * s ** 3 + 2 * Jz * s ** 5 - 4 * P * s ** 4 + s ** 6)
N1 = 2 * Jz ** 2 * P - Jz ** 2 * s ** 2 - 4 * P * s ** 2 + s ** 4
Den = -8 * (s ** 2 + Jz * s - Jz ** 2) * (Jz ** 3 - 4 * P * s + s ** 3)


def reduce_r(expr):
    p_ = sp.Poly(sp.expand(expr), r)
    ev = sp.Integer(0); od = sp.Integer(0)
    for (m_,), co in p_.terms():
        t_ = co * Delta_cf ** (m_ // 2)
        if m_ % 2:
            od += t_
        else:
            ev += t_
    return sp.expand(ev), sp.expand(od)


conds = [len(fl[1]) == 2 and len(big) == 1 and fl[0] == -1 and sp.expand(sp.Mul(*[f_ ** m_ for f_, m_ in fl[1] if f_ not in big]) - (s + Jz)) == 0, sp.expand(res + (s + Jz) * R2) == 0,
         sp.expand(a1 ** 2 - 4 * a2 * a0 - Delta_cf) == 0, sp.expand(sp.discriminant(R2, u) - 16 * N1 ** 2 * Delta_cf) == 0,
         sp.expand(4 * a2 * Fc.subs(c, -1) - ((a1 - 2 * a2) ** 2 - Delta_cf)) == 0]
for sg in (1, -1):
    y_ = -a1 + sg * r                                     # c_F = y_/(2 a2), q(c_F; u_(+-)) = 0 with u_(+-) = (N0 +- N1 r)/Den
    conds.append(reduce_r(y_ ** 2 + 2 * a1 * y_ + 4 * a2 * a0) == (0, 0))
    conds.append(reduce_r(4 * (N0 + sg * N1 * r) * y_ ** 2 - 4 * P * a2 * y_ * Den - 4 * a2 ** 2 * (4 * (N0 + sg * N1 * r) + S_ * Den)) == (0, 0))
conds.append(sp.expand(-(2 * P * c + S_) - (t2 - 2 * P * (c + 1))) == 0)
ok, bad = allok(conds)
check("B5 Res(q,F_c) = -(s+Jz) R2; u_(+-) = (N0 +- N1 sqrt(Delta_F))/Den = u(c_F^(+-)); u_- < 0; flip at u_f = u_+", ok,
      "Delta_F = a1^2 - 4 a2 a0; Region (b), Jz < phi s: c_F^+ in (0,1), c_F^- < -1 (F_c(-1) < 0), u_+ = u(c_F^+) >= u_* (equality at Jz = J0), u_- < 0 since -(2Pc+S) = t2 - 2P(c+1) > 0 and 1-c^2 < 0 for c < -1" + bad)

# ================================================================================================ (C1) boundary Jz = Jx + Jy: line structure
qs = q.subs(Jz, s)
Dels = sp.expand(Delta_cf.subs(Jz, s) - 4 * s ** 2 * (s ** 2 - P) ** 2)
a1s = a1.subs(Jz, s)
up_s = sp.simplify(((N0 + N1 * a1) / Den).subs(Jz, s))
um_s = sp.simplify(((N0 - N1 * a1) / Den).subs(Jz, s))
c2n = P / (2 * u) - 1
ok, bad = allok([sp.expand(qs - (c - 1) * (4 * u * (c + 1) - 2 * P)) == 0, sp.expand(Fc.subs(Jz, s) - 2 * s * c * (P * c + s ** 2 - P)) == 0, Dels == 0,
                 sp.expand(a1s - 2 * s * (s ** 2 - P)) == 0, sp.simplify(up_s - P / 2) == 0, sp.expand(R2.subs({Jz: s, u: P / 2})) == 0,
                 sp.simplify(qs.subs(c, c2n)) == 0, sp.simplify(sp.diff(qs, c).subs(c, c2n) - (2 * P - 8 * u)) == 0, sp.simplify(um_s - P ** 2 / (2 * (2 * P - s ** 2))) == 0])
check("C1 boundary Jz = s: q = (c-1)(4u(c+1)-2P): c = 1 (Gamma) always; c_2 = P/(2u)-1 in (-1,1) iff u > P/4; F_c = 2sc(Pc+s^2-P): flip at u = P/2", ok,
      "F_c = 2 s c (P c + s^2 - P): sign F_c(c_2) = sign c_2; charge +1 for P/4 < u < P/2, -1 for u > P/2: flip at kappa^2 = P/2 = u_+(Jz = s), exact" + bad)
print(f"        (boundary u_- = {um_s})") if VERBOSE else None

# ================================================================================================ exact samples
def Fc_f(jx, jy, jz, cv):
    sv = jx + jy; Pv = jx * jy
    return Pv * (sv + jz) * cv * cv + sv * (sv * sv + jz * sv - 2 * Pv) * cv + (Pv + jz * sv + jz * jz) * (sv - jz)


def q_f(jx, jy, jz, uv, cv):
    return 4 * uv * cv * cv - 2 * jx * jy * cv - (4 * uv + jx * jx + jy * jy - jz * jz)


def G_f(jx, jy, jz):
    sv = jx + jy; Pv = jx * jy
    return jz ** 5 + (4 * Pv - 2 * sv ** 2) * jz ** 3 - 2 * Pv * sv * jz ** 2 + (4 * Pv ** 2 - 5 * Pv * sv ** 2 + sv ** 4) * jz + Pv * sv ** 3 - 4 * Pv ** 2 * sv


def fr_sqrt(x):
    n_, d_ = x.numerator, x.denominator
    a_, b_ = int(round(n_ ** 0.5)), int(round(d_ ** 0.5))
    assert a_ * a_ == n_ and b_ * b_ == d_
    return Fr(a_, b_)


conds = []; rows_s = []
for jz in (Fr(13, 6), Fr(5, 2), Fr(29, 10), Fr(10, 3)):
    jx = jy = Fr(1); Sv = 2 - jz * jz; rv = jz * fr_sqrt(jz * jz - 4)
    us = (-Sv + rv) / 8; cbv = (-Sv - rv) / 2
    Fcb = Fc_f(jx, jy, jz, cbv); Gv = G_f(jx, jy, jz); den_f = 4 + 2 * jz - jz * jz
    conds += [q_f(jx, jy, jz, us, cbv) == 0, 8 * us * cbv - 2 == 0, 0 < cbv < 1, (Fcb > 0) == (Gv < 0), Fcb != 0]
    if den_f > 0:                                             # Jz < phi s: flip exists
        cF = (jz - 2) * (jz + 1) / (jz + 2); uf = jz * (jz + 2) / (4 * den_f)
        conds += [Fc_f(jx, jy, jz, cF) == 0, q_f(jx, jy, jz, uf, cF) == 0, uf > us, (cF < cbv) == (Fcb > 0), 0 < cF < 1]
        rows_s.append(f"{jz}: {us} {'(+,-)' if Fcb > 0 else '(-,+)'} {uf}")
    else:
        conds += [all(Fc_f(jx, jy, jz, Fr(k_, 100)) < 0 for k_ in range(-100, 101)), Fcb < 0]
        rows_s.append(f"{jz}: {us} (-,+) none")
ok, bad = allok(conds)
check("B6 exact rational samples Jx = Jy = 1, Jz = 13/6, 5/2, 29/10, 10/3: double root, born sign, flip (c_F, u_f); no flip above phi s", ok, bad, note="u_*, born, u_f: " + "; ".join(rows_s))


# B7: exact rational grid, region (b): Sturm root count of q on [-1,1] vs the threshold u > u_*; sign F_c(c_b) = -sign G (Jz < phi s), F_c(c_b) < 0 < G (Jz >= phi s)
def sign_surd(A_, B_, D_):
    """exact sign of A_ + B_ sqrt(D_) for Fractions, D_ > 0"""
    if A_ >= 0 and B_ >= 0:
        return 0 if (A_ == 0 and B_ == 0) else 1
    if A_ <= 0 and B_ <= 0:
        return -1
    return 1 if (A_ > 0) == (A_ * A_ > B_ * B_ * D_) else -1


rngb = random.Random(23)
n_roots = n_sign = n_badb = 0; n_flipside = [0, 0]
for _ in range(400):
    jx, jy = Fr(rngb.randint(1, 80), 10), Fr(rngb.randint(1, 80), 10)
    sv = jx + jy; Pv = jx * jy
    jz = sv * (1 + Fr(rngb.randint(1, 80), 100))
    Sv = jx * jx + jy * jy - jz * jz; Dv = Sv * Sv - 4 * Pv * Pv
    a2v = Pv * (sv + jz); a1v = sv * (sv * sv + jz * sv - 2 * Pv); a0v = (Pv + jz * sv + jz * jz) * (sv - jz)
    al, be = -Sv / (2 * Pv), Fr(-1) / (2 * Pv)                              # c_b = al + be sqrt(Dv)
    Fcb_sign = sign_surd(a2v * (al * al + be * be * Dv) + a1v * al + a0v, 2 * a2v * al * be + a1v * be, Dv)
    Gv = G_f(jx, jy, jz); below_phi = (sv * sv + jz * sv - jz * jz) > 0
    n_sign += 1; n_badb += int(Fcb_sign != (-(1 if Gv > 0 else -1) if below_phi else -1) or (not below_phi and Gv <= 0))
    n_flipside[int(Fcb_sign > 0)] += int(below_phi)
    ustar_f = float((-Sv + Fr(Dv).__float__() ** 0.5) / 8)
    for mult in (0.6, 0.97, 1.03, 1.8):
        uv = Fr(round(ustar_f * mult * 10 ** 6), 10 ** 6)
        pred = 2 if (8 * uv + Sv > 0 and 16 * uv * uv + 4 * Sv * uv + Pv * Pv > 0) else 0
        cnt = sp.Poly(4 * sp.Rational(uv.numerator, uv.denominator) * c ** 2 - 2 * sp.Rational(Pv.numerator, Pv.denominator) * c - sp.Rational((4 * uv + Sv).numerator, (4 * uv + Sv).denominator), c, domain="QQ").count_roots(-1, 1)
        n_roots += 1; n_badb += int(cnt != pred or pred != (2 if mult > 1 else 0))
check("B7 exact rational grid, region (b): Sturm root count of q on [-1,1] is 0 below u_*, 2 above; sign F_c(c_b) = -sign G (Jz < phi s), < 0 (Jz >= phi s)", n_badb == 0,
      "", note=f"{n_roots} root counts, {n_sign} couplings (F_c(c_b) > 0 in {n_flipside[1]}, < 0 in {n_flipside[0]} below phi s), bad {n_badb}")


# ================================================================================================ (C2-C4) the TRIM zeros on the boundaries: Gamma (Jz = s), M = (1/2,1/2,0) (Jz = |Jx-Jy|)
# Weighted Schur complement (Brillouin-Wigner series, G0 = H(0)/(16 Jz^2) on the complement of the kernel), theta = 2 pi f - TRIM = tx (1,-1,0) + ty (1,1,0) + tz (0,0,1)
# with weights tx: 1, (ty,tz): wy.  Pauli vector d in a real orthonormal kernel basis.
eps = sp.Symbol("eps", positive=True)
tx, ty, tz = sp.symbols("tx ty tz", real=True)
jx_, jy_ = sp.symbols("jx_ jy_", positive=True)
kp = sp.Symbol("kp", positive=True)
E_, A_, B_ = (1, -1, 0), (1, 1, 0), (0, 0, 1)


def trunc(e, n):
    e = sp.expand(e)
    if e == 0:
        return sp.Integer(0)
    return sum(co * eps ** m_ for (m_,), co in sp.Poly(e, eps).terms() if m_ <= n)


def expser(phi_, n):
    out = sp.Integer(1); term = sp.Integer(1)
    for m_ in range(1, n + 1):
        term = trunc(term * sp.I * phi_ / m_, n); out += term
    return trunc(out, n)


def weighted_H(Jv, kv, base, wy, N):
    amp = {"x": 2 * Jv[0], "y": 2 * Jv[1], "z": 2 * Jv[2], "odd": 2 * kv}
    M_ = sp.zeros(4, 4); M0_ = sp.zeros(4, 4)
    for (a_, b_, n_, kind_) in TERMS:
        t_ = amp[kind_] * (sp.Integer(-1) ** (base[0] * n_[0] + base[1] * n_[1]))
        M0_[a_, b_] += t_; M0_[b_, a_] -= t_
        ph_ = eps * tx * sum(n_[j] * E_[j] for j in range(3)) + eps ** wy * (ty * sum(n_[j] * A_[j] for j in range(3)) + tz * sum(n_[j] * B_[j] for j in range(3)))
        M_[a_, b_] += t_ * expser(ph_, N); M_[b_, a_] -= t_ * expser(-ph_, N)
    return M0_, (sp.I * M_).applyfunc(lambda e: trunc(e, N))


def schur(H, Wm, E2, Nd):
    H0 = H.subs(eps, 0); Pk = sp.eye(4) - H0 * H0 / E2; G0 = H0 / E2
    V = (H - H0).applyfunc(lambda e: trunc(e, Nd))
    mm2 = lambda A, B: (A * B).applyfunc(lambda e: trunc(e, Nd))
    acc = mm2(mm2(Pk, V), Pk); cur = mm2(Pk, V); sg = -1
    for m_ in range(2, Nd + 1):
        cur = mm2(cur, G0 * V); acc = acc + sg * mm2(cur, Pk); sg = -sg
    h2 = (Wm.T * acc * Wm).applyfunc(sp.expand)
    herm = sp.simplify(h2[0, 1] - sp.conjugate(h2[1, 0])) == 0 and sp.simplify(sp.im(h2[0, 0])) == 0 and sp.simplify(sp.im(h2[1, 1])) == 0
    d0 = sp.expand((h2[0, 0] + h2[1, 1]) / 2); dz_ = sp.expand((h2[0, 0] - h2[1, 1]) / 2)
    dx_ = sp.expand((h2[0, 1] + h2[1, 0]) / 2); dy_ = sp.expand(sp.I * (h2[0, 1] - h2[1, 0]) / 2)
    return herm, d0, dx_, dy_, dz_, Pk, H0


def cw(e, m_):
    return sp.expand(sp.Poly(sp.expand(e), eps).coeff_monomial(eps ** m_)) if e != 0 else sp.Integer(0)


def det_trunc(H, N):
    mm2 = lambda A, B: (A * B).applyfunc(lambda e: trunc(e, N))
    H2 = mm2(H, H); H3 = mm2(H2, H); H4 = mm2(H3, H)
    p1, p2, p3, p4 = (trunc(sp.expand(A.trace()), N) for A in (H, H2, H3, H4))
    return trunc(sp.expand((p1 ** 4 - 6 * p1 ** 2 * p2 + 3 * p2 ** 2 + 8 * p1 * p3 - 6 * p4) / 24), N)


def trim_case(Jv, kv, base, Wm, Jzv, wy, Nd, expected, wlead):
    """Returns (conditions, d_leading). Conditions: kernel/projector structure, d0 = 0, no terms below weight wlead, leading d = expected, det H weight 2*wlead part = 16 Jz^2 |d|^2, nothing below."""
    M0_, H = weighted_H(Jv, kv, base, wy, 2 * wlead)
    E2 = sp.expand(16 * Jzv ** 2)
    herm, d0, dx_, dy_, dz_, Pk, H0 = schur(H, Wm, E2, wlead)
    dl = tuple(cw(e, wlead) for e in (dx_, dy_, dz_))
    Dp = sp.Poly(det_trunc(H, 2 * wlead), eps)
    conds = [sp.expand((H0 * H0 - E2 * (sp.eye(4) - Pk))[i_, j_]) == 0 for i_ in range(4) for j_ in range(4)]
    conds = [all(conds), (H0 * Wm).applyfunc(sp.expand) == sp.zeros(4, 2), sp.simplify(Pk * Pk - Pk) == sp.zeros(4, 4) and sp.simplify(Pk.trace()) == 2, herm, d0 == 0,
             all(cw(e, m_) == 0 for e in (dx_, dy_, dz_) for m_ in range(1, wlead)), all(sp.simplify(dl[i_] - expected[i_]) == 0 for i_ in range(3)),
             all(sp.expand(Dp.coeff_monomial(eps ** m_)) == 0 for m_ in range(2 * wlead)),
             sp.simplify(sp.together(sp.expand(Dp.coeff_monomial(eps ** (2 * wlead))) - E2 * sum(e ** 2 for e in dl))) == 0]
    return conds, dl


jac = lambda d: sp.factor(sp.Matrix([[sp.diff(e, v) for v in (tx, ty, tz)] for e in d]).det())
kern_G = sp.Matrix.hstack(sp.Matrix([1, 0, -1, 0]) / sp.sqrt(2), sp.Matrix([0, 1, 0, -1]) / sp.sqrt(2))
kern_M2 = sp.Matrix.hstack(sp.Matrix([1, 0, 1, 0]) / sp.sqrt(2), sp.Matrix([0, 1, 0, 1]) / sp.sqrt(2))
sg_ = jx_ + jy_
aG = (jx_ * jy_ - 4 * kp ** 2) / sg_
dG = (2 * jy_ * ty - sg_ * tz, aG * tx ** 2, -8 * kp * ty)
cG, dlG = trim_case((jx_, jy_, sg_), kp, (0, 0), kern_G, sg_, 2, 2, dG, 2)
jG = jac(dG)
ok, bad = allok(cG + [sp.simplify(jG - 16 * sg_ * aG * kp * tx) == 0])
check("C2 Gamma (Jz = s): d = (2Jy y - s z, a x^2, -8k y), a = (P-4u)/s; det H(4th) = 16 Jz^2 |d|^2; Jacobian 16 s a k x: local degree 0", ok,
      "a != 0 (u != P/4): isolated zero; two preimages of opposite Jacobian sign: local degree 0" + bad)
cM, dlM = trim_case((jx_, jy_, jx_ - jy_), kp, (1, 1), kern_G, jx_ - jy_, 2, 2,
                    (-2 * jy_ * ty - (jx_ - jy_) * tz, -(jx_ * jy_ + 4 * kp ** 2) * tx ** 2 / (jx_ - jy_), 4 * kp * (2 * ty - tz)), 2)
aM = -(jx_ * jy_ + 4 * kp ** 2) / (jx_ - jy_)
cM2, dlM2 = trim_case((jx_, jy_, jy_ - jx_), kp, (1, 1), kern_M2, jy_ - jx_, 2, 2,
                      (-2 * jy_ * ty - (jx_ - jy_) * tz, -(jx_ * jy_ + 4 * kp ** 2) * tx ** 2 / (jx_ - jy_), 4 * kp * tz), 2)
jM = jac(dlM); jM2 = jac(dlM2)
ok, bad = allok(cM + cM2 + [sp.simplify(jM + 16 * aM * kp * jx_ * tx) == 0, sp.simplify(jM2 - 16 * aM * kp * jy_ * tx) == 0])
check("C3 M (Jz = |Jx-Jy|, both orders): a = -(P+4u)/(Jx-Jy) != 0; det H(4th) = 16 Jz^2 |d|^2; Jacobian odd in x: degree 0, no birth", ok,
      "isolated zero at every kappa > 0 (never a birth point), local degree 0" + bad)
aa_ = sp.Symbol("aa_", positive=True)
jxh, jyh = aa_, 4 * kp ** 2 / aa_                                   # u = kappa^2 = P/4
sh_ = jxh + jyh
dH4 = (2 * jyh * ty - sh_ * tz, (4 * kp ** 2 / (4 * sh_)) * tx ** 4, -8 * kp * ty)
cH, dlH = trim_case((jxh, jyh, sh_), kp, (0, 0), kern_G, sh_, 4, 8, dH4, 4)
jH = jac(dH4)
ok, bad = allok(cH + [sp.simplify(jH - 32 * sh_ * (4 * kp ** 2 / (4 * sh_)) * kp * tx ** 3) == 0])
check("C4 Gamma at u = P/4: d = (2Jy y - s z, (P/4s) x^4, -8k y), weights 1,4,4; det H(8th) = 16 Jz^2 |d|^2; Jacobian 8 P k x^3: degree 0", ok,
      "isolated zero, local degree 0" + bad)


# ================================================================================================ FLOAT consistency checks (double precision; not certified)
PHI_F = (1 + 5 ** 0.5) / 2


def T_node(J, kappa, cv, sgn=1):
    """Im Tr(P d1H P d2H P d3H), P = projector on the two middle eigenvectors, at the line node with cosine cv (x < 1/2 for sgn = +1); also max |middle level|."""
    x0 = np.arccos(cv) / (2 * np.pi)
    f0 = np.array([x0, 1 - x0, 0.0]) if sgn > 0 else np.array([1 - x0, x0, 0.0])
    B = Bloch(J, kappa); H0, dH = B.dH(f0)
    w, V = np.linalg.eigh(H0)
    Pp = V[:, 1:3] @ V[:, 1:3].conj().T
    return float(np.imag(np.trace(Pp @ dH[0] @ Pp @ dH[1] @ Pp @ dH[2]))), float(np.abs(w[1:3]).max())


def Fc_fl(J, cv):
    jx, jy, jz = J; sv = jx + jy; Pv = jx * jy
    return Pv * (sv + jz) * cv * cv + sv * (sv * sv + jz * sv - 2 * Pv) * cv + (Pv + jz * sv + jz * jz) * (sv - jz)


def roots_fl(J, uv):
    jx, jy, jz = J; Pv = jx * jy; Sv = jx ** 2 + jy ** 2 - jz ** 2
    rr = np.roots([4 * uv, -2 * Pv, -(4 * uv + Sv)])
    return sorted(cc.real for cc in rr if abs(cc.imag) < 1e-13 and -1 < cc.real < 1)


def G_fl(jx, jy, jz):
    sv = jx + jy; Pv = jx * jy
    return jz ** 5 + (4 * Pv - 2 * sv ** 2) * jz ** 3 - 2 * Pv * sv * jz ** 2 + (4 * Pv ** 2 - 5 * Pv * sv ** 2 + sv ** 4) * jz + Pv * sv ** 3 - 4 * Pv ** 2 * sv


def J0_fl(jx, jy):
    sv = jx + jy
    return brentq(lambda zz_: G_fl(jx, jy, zz_), sv, PHI_F * sv, xtol=1e-14)


def stars(J):
    jx, jy, jz = J; Pv = jx * jy; Sv = jx ** 2 + jy ** 2 - jz ** 2
    us = (-Sv + np.sqrt(Sv * Sv - 4 * Pv * Pv)) / 8
    sv = jx + jy; a2f = Pv * (sv + jz); a1f = sv * (sv * sv + jz * sv - 2 * Pv); a0f = (Pv + jz * sv + jz * jz) * (sv - jz)
    uf = cF = None
    if jz < PHI_F * sv:
        cF = (-a1f + np.sqrt(a1f * a1f - 4 * a2f * a0f)) / (2 * a2f)
        uf = -(2 * Pv * cF + Sv) / (4 * (1 - cF ** 2))
    return us, uf, cF


rngf = np.random.default_rng(5)
n_chk = n_bad = n_skip = 0; max_rel = 0.0; n_pat = n_patbad = 0
for _ in range(80):
    jx, jy = np.exp(rngf.uniform(np.log(0.1), np.log(4.0), 2)); sv = jx + jy
    J = (jx, jy, sv * rngf.uniform(1.01, 1.9)); Pv = jx * jy
    us, uf, cF = stars(J); j0 = J0_fl(jx, jy)
    for fac in (0.9, 1.01, 1.3, 2.5, 9.0):
        uu = us * fac; rts = roots_fl(J, uu)
        n_chk += 1; n_bad += int(len(rts) != (0 if fac < 1 else 2))
        sgs = []
        for cv in rts:
            T, mid = T_node(J, np.sqrt(uu), cv)
            qp = 8 * uu * cv - 2 * Pv
            Tf = -32 * np.pi ** 3 * np.sqrt(uu) * qp * Fc_fl(J, cv) * np.sin(np.arccos(cv)) / J[2] ** 3
            n_chk += 1; n_bad += int(mid > 1e-8)
            if abs(Tf) > 1e-8:
                max_rel = max(max_rel, abs(T - Tf) / abs(Tf)); n_bad += int(np.sign(T) != np.sign(Tf))
            else:
                n_skip += 1
            sgs.append(int(np.sign(T)))
        if fac == 9.0 and uf is not None and uu > uf:                    # after the flip both -1
            n_pat += 1; n_patbad += int(sgs != [-1, -1])
        if fac == 9.0 and uf is None:                                     # no flip for Jz >= phi s
            n_pat += 1; n_patbad += int(sgs != [-1, 1])
    ub = us * 1.01 if uf is None else us + 0.3 * (uf - us)           # just above the birth, below the flip: born pattern (+,-) iff Jz < J0, else (-,+)
    if uf is None or (uf - us) / us > 1e-5:
        sgb = [int(np.sign(T_node(J, np.sqrt(ub), cv)[0])) for cv in roots_fl(J, ub)]
        n_pat += 1; n_patbad += int(sgb != ([1, -1] if J[2] < j0 else [-1, 1]))
check("F1 FLOAT region (b): root counts, T = -32 pi^3 kappa q' F_c sin/Jz^3, born and post-flip signs, 80 random couplings", n_bad == 0 and n_patbad == 0 and max_rel < 1e-6,
      "levels: middle |E| < 1e-8 at every root; T sign from the closed form", note=f"{n_chk} root/level and {n_pat} pattern checks, bad {n_bad + n_patbad}, max rel dev {max_rel:.0e}")

conds = []; rows = []
for (jx, jy) in ((1.0, 1.0), (1.0, 0.5), (1.3, 0.4)):
    sv = jx + jy; j0 = J0_fl(jx, jy); rows.append(f"J0({jx},{jy}) = {j0:.5f}")
    for jz, expect in ((j0 * 0.98, [1, -1]), (j0 * 1.02, [-1, 1]), (j0, [-1, -1])):
        J = (jx, jy, jz); us, uf, cF = stars(J); uu = us * 1.01 if jz == j0 else us + 0.5 * (uf - us)
        sgs = [int(np.sign(T_node(J, np.sqrt(uu), cv)[0])) for cv in roots_fl(J, uu)]
        conds.append(sgs == expect)
for J in ((1, 1, 2.1), (1, 1, 2.5), (1, 0.5, 1.7), (1.3, 0.4, 2.2), (1, 1, 2.9)):
    us, uf, cF = stars(J); j0 = J0_fl(J[0], J[1])
    born = [1, -1] if J[2] < j0 else [-1, 1]
    below = [int(np.sign(T_node(J, np.sqrt(uf * (1 - 1e-3)), cv)[0])) for cv in roots_fl(J, uf * (1 - 1e-3))]
    above = [int(np.sign(T_node(J, np.sqrt(uf * (1 + 1e-3)), cv)[0])) for cv in roots_fl(J, uf * (1 + 1e-3))]
    conds.append(below == born and above == [-1, -1] and uf > us)
for J in ((1, 1, 3.5), (1, 0.5, 2.6), (1.3, 0.4, 2.9)):
    us, uf, cF = stars(J); assert uf is None
    conds.append(all([int(np.sign(T_node(J, np.sqrt(us * f_), cv)[0])) for cv in roots_fl(J, us * f_)] == [-1, 1] for f_ in (1.01, 3, 30, 300)))
mp.mp.dps = 40
j0m = mp.findroot(lambda x_: x_ ** 3 - 4 * x_ - 4, 2.38)
Sm = 2 - j0m ** 2; us_m = (-Sm + mp.sqrt(Sm ** 2 - 4)) / 8
cFm = (j0m - 2) * (j0m + 1) / (j0m + 2); uf_m = -(2 * cFm + Sm) / (4 * (1 - cFm ** 2))
conds.append(abs(uf_m - us_m) < mp.mpf("1e-30") and abs(cFm - 1 / (4 * us_m)) < mp.mpf("1e-30"))
ok, bad = allok(conds)
check("F2 FLOAT: born (+,-) below J0, (-,+) above, (-,-) at J0; flip at u_f; no flip above phi s; mp: u_f = u_* at iso J0", ok,
      bad, note="; ".join(rows) + f"; iso J0 = {mp.nstr(j0m, 8)}, |u_f - u_*| < 1e-30")

# region (a): float det H on the line vs 16 q^2, and q < 0 on a grid
rnga = np.random.default_rng(9)
worst_q = -1e9; worst_rel = 0.0; mindet = 1e9; npts = 0
for _ in range(100):
    jx, jy = rnga.uniform(0.3, 3.0, 2)
    if abs(jx - jy) < 0.05:
        continue
    jz = abs(jx - jy) * rnga.uniform(0.02, 1.0)
    for kap in (0.05, 0.5, 2.0, 10.0):
        xs_ = np.linspace(0.0005, 0.9995, 400)
        Hs_ = Bloch((jx, jy, jz), kap).H(np.stack([xs_, 1 - xs_, 0 * xs_], axis=1))
        det_ = np.real(np.linalg.det(Hs_)); cv = np.cos(2 * np.pi * xs_)
        qv = 4 * kap ** 2 * cv ** 2 - 2 * jx * jy * cv - (4 * kap ** 2 + jx ** 2 + jy ** 2 - jz ** 2)
        worst_q = max(worst_q, float(qv.max())); worst_rel = max(worst_rel, float(np.max(np.abs(det_ - 16 * qv ** 2) / (16 * qv ** 2 + 1e-300))))
        mindet = min(mindet, float(det_.min()) / (jx + jy + jz + kap) ** 8); npts += 400
check("F3 FLOAT region (a): Bloch det H = 16 q^2 > 0 on the line grid", worst_q < 0 and worst_rel < 1e-8 and mindet > 0,
      "", note=f"{npts} pts, max q = {worst_q:.0e}, max rel dev {worst_rel:.0e}")


# ---- Fukui link-method Chern number of the lowest two bands through a closed surface (float; resolved when max plaquette phase < 1)
def _link(A1, B1_):
    return np.linalg.det(np.einsum('...ia,...ib->...ab', A1.conj(), B1_))


def _plaquettes(V):
    links = (_link(V[:-1, :-1], V[1:, :-1]), _link(V[1:, :-1], V[1:, 1:]), _link(V[1:, 1:], V[:-1, 1:]), _link(V[:-1, 1:], V[:-1, :-1]))
    assert all(np.isfinite(zl).all() and np.min(np.abs(zl)) > 1e-12 for zl in links), "singular occupied-band overlap"
    return np.angle(links[0] * links[1] * links[2] * links[3])


def flux(B, surf, m=64, nocc=2):
    """Chern number of the lowest nocc bands through the closed surface surf(unit-sphere points); polar axis = first coordinate, polar grid clustered at the poles."""
    uu = np.linspace(0, 1, m + 1)
    t = np.pi * (1 - np.cos(np.pi * uu)) / 2
    ph = np.linspace(0, 2 * np.pi, 2 * m + 1)
    Xh = np.stack([np.cos(t)[:, None] * np.ones_like(ph)[None, :], np.sin(t)[:, None] * np.cos(ph)[None, :], np.sin(t)[:, None] * np.sin(ph)[None, :]], axis=-1)
    Pts = surf(Xh.reshape(-1, 3)).reshape(m + 1, 2 * m + 1, 3)
    ev, V = B.levels(Pts.reshape(-1, 3), vecs=True)
    V = V[:, :, :nocc].reshape(m + 1, 2 * m + 1, 4, nocc).copy()
    V[0, :] = V[0, 0]; V[-1, :] = V[-1, 0]; V[:, -1] = V[:, 0]
    pl = _plaquettes(V)
    return pl.sum() / (2 * np.pi), float((ev[:, 2] - ev[:, 1]).min()), float(np.abs(pl).max())


ehat = np.array([1., -1., 0.]); ahat = np.array([1., 1., 0.]); bhat = np.array([0., 0., 1.])


def weighted_off(s_, eta, p_, c_w):
    cx_, cy_, cz_ = c_w
    return lambda Xh: ((cx_ + s_ * Xh[:, :1]) * ehat + (cy_ + eta * s_ ** p_ * Xh[:, 1:2]) * ahat + (cz_ + eta * s_ ** p_ * Xh[:, 2:3]) * bhat) / (2 * np.pi)


def round_sphere(cen, rho, axis=(1., -1., 0.)):
    ax = np.array(axis); ax = ax / np.linalg.norm(ax)
    tt = np.array([1., 0, 0]) if abs(ax[0]) < 0.9 else np.array([0, 1., 0])
    e1 = np.cross(ax, tt); e1 /= np.linalg.norm(e1); e2 = np.cross(ax, e1)
    cen = np.array(cen, float)
    return lambda Xh: cen + rho * (Xh[:, :1] * ax + Xh[:, 1:2] * e1 + Xh[:, 2:3] * e2)


def round_sphere(cen, rho, axis=(1., -1., 0.)):
    ax = np.array(axis); ax = ax / np.linalg.norm(ax)
    tt = np.array([1., 0, 0]) if abs(ax[0]) < 0.9 else np.array([0, 1., 0])
    e1 = np.cross(ax, tt); e1 /= np.linalg.norm(e1); e2 = np.cross(ax, e1)
    cen = np.array(cen, float)
    return lambda Xh: cen + rho * (Xh[:, :1] * ax + Xh[:, 1:2] * e1 + Xh[:, 2:3] * e2)


ehat = np.array([1., -1., 0.]); ahat = np.array([1., 1., 0.]); bhat = np.array([0., 0., 1.])


def wsurf(center_f, s_, eta, p_, off):
    """Weighted ellipsoid theta = (cx + s X) (1,-1,0) + (cy + eta s^p Y) (1,1,0) + (cz + eta s^p Z) (0,0,1), f = center + theta/(2 pi)."""
    cx_, cy_, cz_ = off
    return lambda Xh: np.asarray(center_f)[None, :] + ((cx_ + s_ * Xh[:, :1]) * ehat + (cy_ + eta * s_ ** p_ * Xh[:, 1:2]) * ahat + (cz_ + eta * s_ ** p_ * Xh[:, 2:3]) * bhat) / (2 * np.pi)


def line_nodes(J, uv):
    jx, jy, jz = J; Pv = jx * jy; Sv = jx ** 2 + jy ** 2 - jz ** 2
    rr = np.roots([4 * uv, -2 * Pv, -(4 * uv + Sv)])
    cs = sorted(cc.real for cc in rr if abs(cc.imag) < 1e-9 and -1 < cc.real < 1)
    return cs, [np.arccos(cc) / (2 * np.pi) for cc in cs]


# F4: the merger of the two line nodes (charge sum 0): flux = -chi (chi = sign T) for each node, 0 through the merger point and through a sphere around both
conds = []; out_ = []; pm_all = 0.0
for J, facs in (((1.0, 1.0, 10 / 3), (0.95, 1.0, 1.2)), ((1.0, 1.0, 13 / 6), (0.97, 1.0, 1.03))):
    us, uf, cF = stars(J); Pv = J[0] * J[1]
    for fac in facs:
        uu = us * fac; B = Bloch(J, np.sqrt(uu)); cs, xs = line_nodes(J, uu)
        if fac <= 1.0:
            xb = np.arccos(Pv / (4 * us)) / (2 * np.pi)
            for rho in (0.02, 0.04):
                fl_, gap, pm = flux(B, round_sphere((xb, 1 - xb, 0.0), rho), 96)
                conds.append(abs(fl_) < 1e-9 and pm < 1.0 and gap > 0); pm_all = max(pm_all, pm)
            pass
        else:
            dist = abs(xs[0] - xs[1]) * np.sqrt(2); mid = ((xs[0] + xs[1]) / 2, 1 - (xs[0] + xs[1]) / 2, 0.0)
            chis = [np.sign(T_node(J, np.sqrt(uu), cv)[0]) for cv in cs]
            f1 = flux(B, round_sphere((xs[0], 1 - xs[0], 0.0), 0.25 * dist), 96); f2 = flux(B, round_sphere((xs[1], 1 - xs[1], 0.0), 0.25 * dist), 96)
            f3 = flux(B, round_sphere(mid, 0.75 * dist), 96)
            conds += [abs(f1[0] + chis[0]) < 1e-9, abs(f2[0] + chis[1]) < 1e-9, abs(f3[0]) < 1e-9, chis[0] == -chis[1], max(f1[2], f2[2], f3[2]) < 1.0]
            pm_all = max(pm_all, f1[2], f2[2], f3[2])
            out_.append(f"Jz={J[2]:.2f}: chi {int(chis[0]):+d},{int(chis[1]):+d}, flux {f1[0]:+.0f},{f2[0]:+.0f}, both {abs(f3[0]):.0f}")
ok, bad = allok(conds)
check("F4 FLOAT merger: Fukui flux 0 at u <= u_*, -chi per node above, 0 around both nodes", ok,
      bad, note="; ".join(out_) + f"; max plaq. phase {pm_all:.2f}")

# F5: Gamma (Jz = s) near the birth coupling and M (Jz = |Jx-Jy|): resolved fluxes
Jg = (1.0, 0.5, 1.5); kg = 0.3742; Bg = Bloch(Jg, kg); ug = kg ** 2
c2g = 0.5 / (2 * ug) - 1; x2g = np.arccos(c2g) / (2 * np.pi)
conds = []; res_ = []; pm_all = 0.0
for (s_, eta, offx, expect) in ((0.4, 0.3, 0.0, 0), (0.5, 0.3, 0.0, 0), (1.0, 0.3, 0.0, 0), (0.9, 0.3, 0.3, -1), (0.9, 0.15, 0.3, -1)):
    off = (offx * s_, 0.5 * eta * s_ ** 2 * 0.3, -0.4 * eta * s_ ** 2 * 0.3)
    for m_ in (96, 160):
        fl_, gap, pm = flux(Bg, wsurf((0, 0, 0), s_, eta, 2, off), m_)
        conds.append(abs(fl_ - expect) < 1e-9 and pm < 1.0 and gap > 0); pm_all = max(pm_all, pm)
na = flux(Bg, round_sphere((x2g, -x2g, 0.0), 0.02), 96); nb = flux(Bg, round_sphere((-x2g, x2g, 0.0), 0.02), 96)
chi_a = np.sign(T_node(Jg, kg, c2g)[0])
conds += [abs(na[0] + 1) < 1e-9, abs(nb[0] - 1) < 1e-9, chi_a == 1]
res_.append(f"Gamma (u just above P/4): alone 0, with both nodes 0, with one node {na[0]:+.0f} = node alone")
for (J, kap) in (((1.5, 0.5, 1.0), 0.7), ((1.5, 0.5, 1.0), 0.2), ((0.5, 1.5, 1.0), 0.7), ((0.5, 1.5, 1.0), 0.2)):
    Bm = Bloch(J, kap)
    for (s_, eta) in ((0.5, 0.3), (0.3, 0.3), (0.8, 0.2)):
        off = (0.3 * s_, 0.5 * eta * s_ ** 2, -0.4 * eta * s_ ** 2)
        for m_ in (48, 96):
            fl_, gap, pm = flux(Bm, wsurf((0.5, 0.5, 0.0), s_, eta, 2, off), m_)
            conds.append(abs(fl_) < 1e-9 and pm < 1.0 and gap > 0); pm_all = max(pm_all, pm)
res_.append("M: 0 at 4 couplings")
ok, bad = allok(conds)
check("F5 FLOAT TRIM: Fukui flux 0 around Gamma (Jz = s) and M (Jz = |Jx-Jy|); Gamma + one born node = that node", ok,
      bad, note="; ".join(res_) + f"; max plaq. phase {pm_all:.2f}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}   ({time.time() - T0:.0f} s)")

if __name__ == "__main__":
    raise SystemExit(0 if all(RESULTS) else 1)
