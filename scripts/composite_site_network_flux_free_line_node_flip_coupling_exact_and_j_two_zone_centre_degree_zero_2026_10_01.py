#!/usr/bin/env python3
"""Composite-site network, supplied u = +1 quadratic Majorana comparator: (A) the exact flip coupling of the line touching for general couplings,
(B) the zone centre Gamma at J_x = J_y = 1, J_z = 2 (exact local structure and local degree).

Setting. One copy of the landed composite-site (hyperhoneycomb-in-doubled-cubic) network with the landed hopping-sign convention and gauge u = +1; couplings J_x, J_y, J_z,
odd term kappa; four-site Bloch matrix H(f) = i M(f), M[a,b] += t e^{2 pi i f.n}, M[b,a] -= t e^{-2 pi i f.n} (t = 2 J_flavour or 2 kappa); the terms are rebuilt below from the
network rules. Nothing here is an axiom of the framework: this is a supplied model, and the statements are about it.

(A) General J_x, J_y, J_z, kappa > 0. Notation s = J_x + J_y, P = J_x J_y, S = J_x^2 + J_y^2 - J_z^2, u = kappa^2, c = cos 2 pi x on the line f = (x, 1-x, 0).
 Inputs (stated, not re-derived beyond the first): the line polynomial q(c) = 4u c^2 - 2P c - (4u + S) with det H = 16 q(c)^2 on the line (A0 verifies this symbolically from the
 network terms), so a middle-band touching on the line is a root of q; the charge of the x < 1/2 node is sign F_c(c_-), c_- the smaller root of q, with
 F_c(c) = a2 c^2 + a1 c + a0 = P(s+J_z) c^2 + s(s^2 + J_z s - 2P) c + (J_x+J_z)(J_y+J_z)(s-J_z) (the sign of the kernel-projector triple product Im Tr(P d1H P d2H P d3H) =
 -32 pi^3 kappa q'(c) F_c(c) sin(2 pi x)/J_z^3 at a root; (A5) reproduces this numerically from the network terms at 32 points).
 EXACT (sympy, polynomial identities over Q[s,P,J_z,u]): the resultant Res_c(q, F_c) = -(s+J_z) R2(u), R2 irreducible quadratic in u; its discriminant 16 N1^2 Delta_F with Delta_F =
 disc_c(F_c); the closed form u_(+-) = (N0 +- N1 sqrt(Delta_F))/Den are exact roots of R2 (and Vieta holds); c_F^(+-) = (-a1 +- sqrt(Delta_F))/(2 a2) are shared roots of q and F_c at u_(+-);
 in the triangle regime |J_x-J_y| < J_z < J_x+J_y the sign facts that select the branch (u(c) = -(2Pc+S)/(4(1-c^2)) is a strictly decreasing bijection of (-1,1) onto R, so the line root
 c_-(kappa) is unique and decreases from c0 = -S/(2P) to -1; F_c(-1) < 0 < F_c(1); F_c(c0) = (s+J_z)(J_z^4 - (J_x^2-J_y^2)^2)/(4P); u_- < 0; the denominators of the closed form are
 positive) give: the charge of the x < 1/2 line node flips exactly once, from +1 to -1, at kappa_c^2 = u_+, iff J_z < J_x + J_y and |J_x^2 - J_y^2| < J_z^2; otherwise (triangle
 regime) it is -1 for every kappa. Isotropic limit kappa_c^2 = J(J+2)/(4(4+2J-J^2)); three exact algebraic-number samples. NOT analysed: J_z >= J_x + J_y.
 FLOAT (A5, not certified): the sign of the numerical triple product at kappa_c(1 +- 1e-3) at six couplings and at two no-flip couplings.

(B) J_x = J_y = 1, J_z = 2, any kappa > 0: Gamma = (0,0,0). Coordinates theta = 2 pi f = x(1,-1,0) + y(1,1,0) + z(0,0,1). EXACT (sympy, symbolic kappa): H(0) has spectrum
 {0,0,+-8} for every kappa; the E = 0 Schur complement on the kernel (Brillouin-Wigner series with G0 = H(0)/64), carried to weight 4 with weights x:1, (y,z):2, gives the Pauli vector
 d = (2(y-z), (1-4kappa^2) x^2/2, -8 kappa y) (no identity part, no weight 1 or 3 terms) and the weight-4 part of det H equals 64 |d|^2; kappa = 1/2 (x^2 term absent): weights x:1,
 (y,z):4, d = (2(y-z), x^4/8, -4y), det H = 64 |d|^2 at weight 8; the Jacobian of the leading map is odd in x (32 a kappa x, resp. 4 x^3) with two preimages of opposite sign, so the
 local degree of d/|d| is 0 for every kappa > 0; the pair of line nodes born at Gamma for kappa > 1/2 are the zeros of d_y = x^2 (a + c4 x^2). The reading of the degree as the Chern
 number of the lowest two bands is the landed two-level reduction (not re-proved); the remainders are higher weight (no explicit radius). FLOAT (B3 pair positions, B4): Fukui
 fluxes (lowest two bands) through off-centre weighted ellipsoids that enclose Gamma and are not symmetric under f -> -f, at kappa = 0.5 and 1, plus positive controls at line nodes;
 an off-centre round sphere at kappa = 1/2 is under-resolved (plaquette phase near pi, flux +1 at m <= 240 but 0 at m = 320) and is excluded.
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import random
import time

import mpmath as mp
import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 300

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


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


# ================================================================================================ (A) exact: resultant, roots, branch
s, P, Jz, u, c, r = sp.symbols("s P Jz u c r")
Jx, Jy, kk, zz = sp.symbols("Jx Jy kk zz")
S = s ** 2 - 2 * P - Jz ** 2
q = 4 * u * c ** 2 - 2 * P * c - (4 * u + S)
a2 = P * (s + Jz); a1 = s * (s ** 2 + Jz * s - 2 * P); a0 = (P + Jz * s + Jz ** 2) * (s - Jz)
Fc = a2 * c ** 2 + a1 * c + a0
sub_xy = {s: Jx + Jy, P: Jx * Jy}

# A0: q is the line polynomial: det H = det(iM) = det M = 16 q(c)^2 on f = (x, 1-x, 0) (z1 = zz, z2 = 1/zz, z3 = 1), c = (zz + 1/zz)/2, symbolic in all couplings
AMPS = {"x": 2 * Jx, "y": 2 * Jy, "z": 2 * Jz, "odd": 2 * kk}
Mz = sp.zeros(4, 4)
for (a_, b_, n_, kind_) in TERMS:
    mon = zz ** (n_[0] - n_[1])
    Mz[a_, b_] += AMPS[kind_] * mon; Mz[b_, a_] -= AMPS[kind_] / mon
detM = sp.expand(Mz.det(method="berkowitz"))
cz = (zz + 1 / zz) / 2
q_line = 4 * kk ** 2 * cz ** 2 - 2 * Jx * Jy * cz + Jz ** 2 - Jx ** 2 - Jy ** 2 - 4 * kk ** 2
Fc_xy = Jx * Jy * (Jx + Jy + Jz) * c ** 2 + (Jx + Jy) * (Jx ** 2 + Jy ** 2 + Jz * (Jx + Jy)) * c + (Jx + Jz) * (Jy + Jz) * (Jx + Jy - Jz)
q_xy = 4 * u * c ** 2 - 2 * Jx * Jy * c + Jz ** 2 - Jx ** 2 - Jy ** 2 - 4 * u
ok0, bad0 = allok([sp.expand(detM - 16 * q_line ** 2) == 0, sp.expand(Fc.subs(sub_xy) - Fc_xy) == 0, sp.expand(q.subs(sub_xy) - q_xy) == 0])
check("A0 on the line (x,1-x,0): det H = 16 q(c)^2 symbolic in Jx,Jy,Jz,kappa from the network terms; q and F_c in (s,P,Jz) equal their (Jx,Jy,Jz) forms", ok0,
      "q = 4u c^2 - 2P c - (4u + S)" + bad0)

# A1: resultant and R2
res = sp.expand(sp.resultant(sp.Poly(Fc, c), sp.Poly(q, c)))
fl = sp.factor_list(res)
big = [f_ for f_, m_ in fl[1] if sp.degree(f_, u) == 2]
A2c = 16 * (s ** 2 + Jz * s - Jz ** 2) * (Jz ** 3 - 4 * P * s + s ** 3)
N0 = (s ** 2 - 2 * P - Jz ** 2) * (2 * Jz ** 3 * P - 4 * Jz * P * s ** 2 + Jz * s ** 4 - 4 * P * s ** 3 + s ** 5)
B2c = 4 * N0
C2c = P ** 2 * (s + Jz) * (s ** 4 - 4 * P * s ** 2 - Jz ** 4)
R2 = A2c * u ** 2 + B2c * u + C2c
ok1, bad1 = allok([len(fl[1]) == 2 and len(big) == 1 and sp.expand(sp.Mul(*[f_ ** m_ for f_, m_ in fl[1] if f_ not in big]) - (s + Jz)) == 0,
                   fl[0] == -1, sp.expand(res + (s + Jz) * R2) == 0, sp.Poly(big[0], u).degree() == 2])
check("A1 Res_c(q,F_c) = -(s+Jz) R2(u), R2 = A2 u^2 + B2 u + C2 irreducible over Q[s,P,Jz,u] (factor_list has exactly two factors)", ok1,
      "A2 = 16(s^2+Jz s-Jz^2)(Jz^3-4Ps+s^3), B2 = 4(s^2-2P-Jz^2)(2Jz^3P-4JzPs^2+Jz s^4-4Ps^3+s^5), C2 = P^2(s+Jz)(s^4-4Ps^2-Jz^4)" + bad1)

# A2: discriminants, roots, Vieta
Delta = sp.expand(a1 ** 2 - 4 * a2 * a0)
Delta_cf = (4 * Jz ** 4 * P + 4 * Jz ** 3 * P * s + 4 * Jz ** 2 * P ** 2 - 4 * Jz ** 2 * P * s ** 2 + Jz ** 2 * s ** 4 - 8 * Jz * P * s ** 3 + 2 * Jz * s ** 5 - 4 * P * s ** 4 + s ** 6)
N1 = 2 * Jz ** 2 * P - Jz ** 2 * s ** 2 - 4 * P * s ** 2 + s ** 4
Den = -8 * (s ** 2 + Jz * s - Jz ** 2) * (Jz ** 3 - 4 * P * s + s ** 3)
br0 = sp.expand(A2c * (N0 ** 2 + N1 ** 2 * Delta_cf) + B2c * N0 * Den + C2c * Den ** 2)     # rational part of Den^2 R2(u_(+-))
br1 = sp.expand(2 * A2c * N0 * N1 + B2c * N1 * Den)                                          # coefficient of r
ok2, bad2 = allok([sp.expand(Delta - Delta_cf) == 0, sp.expand(sp.discriminant(R2, u) - 16 * N1 ** 2 * Delta_cf) == 0, br0 == 0, br1 == 0,
                   sp.simplify(2 * N0 / Den + B2c / A2c) == 0, sp.simplify((N0 ** 2 - N1 ** 2 * Delta_cf) / Den ** 2 - C2c / A2c) == 0])
check("A2 disc_u(R2) = 16 N1^2 Delta_F; u_(+-) = (N0 +- N1 sqrt(Delta_F))/Den are exact roots of R2 (rational and sqrt parts of Den^2 R2 vanish), Vieta; closed form of the task = u_+", ok2,
      "Delta_F = disc_c(F_c); N1 = 2Jz^2P-Jz^2s^2-4Ps^2+s^4; Den = -8(s^2+Jz s-Jz^2)(Jz^3-4Ps+s^3)" + bad2)


# A3: shared roots
def reduce_r(expr):
    p_ = sp.Poly(sp.expand(expr), r)
    ev = sp.Integer(0); od = sp.Integer(0)
    for (m_,), co in p_.terms():
        t_ = co * Delta_cf ** (m_ // 2)
        if m_ % 2: od += t_
        else: ev += t_
    return sp.expand(ev), sp.expand(od)


conds3 = []
for sg in (1, -1):
    y_ = -a1 + sg * r                                            # c_F = y_/(2 a2)
    conds3.append(reduce_r(y_ ** 2 + 2 * a1 * y_ + 4 * a2 * a0) == (0, 0))
    conds3.append(reduce_r(4 * (N0 + sg * N1 * r) * y_ ** 2 - 4 * P * a2 * y_ * Den - 4 * a2 ** 2 * (4 * (N0 + sg * N1 * r) + S * Den)) == (0, 0))
ok3, bad3 = allok(conds3)
check("A3 c_F^(+-) = (-a1 +- sqrt(Delta_F))/(2 a2) are roots of F_c and q(c_F^(+-); u_(+-)) = 0 exactly (shared root): u_(+-) = u(c_F^(+-)), u(c) = -(2Pc+S)/(4(1-c^2))", ok3, "reduction mod r^2 - Delta_F" + bad3)

# A4: branch selection, flip criterion, isotropic limit, exact samples
t1 = s ** 2 - Jz ** 2; t2 = Jz ** 2 - s ** 2 + 4 * P                 # t1 = (Jx+Jy)^2 - Jz^2, t2 = Jz^2 - (Jx-Jy)^2: triangle regime <=> t1, t2 > 0
Fb = P * c ** 2 + S * c + P
ucf = lambda cc: -(2 * P * cc + S) / (4 * (1 - cc ** 2))
c0 = -S / (2 * P)
conds4 = [sp.expand(Fb.subs(c, -1) - t2) == 0 and sp.expand(Fb.subs(c, 1) - t1) == 0 and sp.expand(S ** 2 - 4 * P ** 2 + t1 * t2) == 0,      # F_b > 0 everywhere: u decreasing
          sp.simplify(sp.diff(ucf(c), c) + Fb / (2 * (1 - c ** 2) ** 2)) == 0,
          sp.simplify(ucf(c0)) == 0 and sp.expand(sp.cancel(1 - c0 ** 2) - t1 * t2 / (4 * P ** 2)) == 0,
          sp.expand(-(2 * P * (-1) + S) - t2) == 0 and sp.expand(-(2 * P + S) + t1) == 0 and sp.expand(q.subs(c, 1) + t1) == 0 and sp.expand(q.subs(c, -1) - t2) == 0,
          sp.expand(Fc.subs(c, 1) - (s + Jz) * (s ** 2 + Jz * s - Jz ** 2)) == 0 and sp.expand(Fc.subs(c, -1) + s * (s ** 2 - 4 * P) + Jz ** 3) == 0,
          sp.expand(4 * a2 * Fc.subs(c, -1) - ((a1 - 2 * a2) ** 2 - Delta_cf)) == 0,
          sp.simplify(Fc.subs(c, c0) - (s + Jz) * (Jz ** 4 - s ** 2 * (s ** 2 - 4 * P)) / (4 * P)) == 0,
          sp.expand(((Jx ** 2 - Jy ** 2) ** 2 - (s ** 2 * (s ** 2 - 4 * P)).subs(sub_xy))) == 0,                                  # (Jx^2-Jy^2)^2 = s^2 (s^2-4P)
          sp.expand(-(2 * P * c + S) - t2 + 2 * P * (c + 1)) == 0,
          sp.expand((s ** 2 + Jz * s - Jz ** 2) - (t1 + Jz * s)) == 0 and sp.expand((Jz ** 3 - 4 * P * s + s ** 3) - (Jz ** 3 + s * (s ** 2 - 4 * P))) == 0]
# iso limit
J = sp.symbols("J", positive=True)
iso = {s: 2, P: 1, Jz: J}
rr_iso = 2 * J * (J + 1)
u_iso = sp.simplify(((N0 + N1 * r) / Den).subs(iso).subs(r, rr_iso))
conds4.append(sp.expand(Delta_cf.subs(iso) - 4 * J ** 2 * (J + 1) ** 2) == 0 and sp.simplify(u_iso - J * (J + 2) / (4 * (4 + 2 * J - J ** 2))) == 0
              and sp.simplify(((N0 - N1 * r) / Den).subs(iso).subs(r, rr_iso) + sp.Rational(1, 4)) == 0
              and sp.simplify(((-a1 + r) / (2 * a2)).subs(iso).subs(r, rr_iso) - (J - 2) * (J + 1) / (J + 2)) == 0)
# exact samples
samples = ((sp.Integer(1), sp.Rational(4, 5), sp.Integer(1)), (sp.Rational(6, 5), sp.Rational(4, 5), sp.Integer(1)), (sp.Integer(2), sp.Integer(1), sp.Rational(5, 2)))
sdet = []
ok_samp = True
for (jx, jy, jz) in samples:
    vals = {s: jx + jy, P: jx * jy, Jz: jz}
    rr = sp.sqrt(Delta_cf.subs(vals))
    up = sp.radsimp(((N0 + N1 * rr) / Den).subs(vals)); um = sp.radsimp(((N0 - N1 * rr) / Den).subs(vals))
    cF = sp.radsimp(((-a1 + r) / (2 * a2)).subs(vals).subs(r, rr))
    ok_samp &= (sp.simplify(sp.radsimp(q.subs(vals).subs({u: up, c: cF}))) == 0 and sp.simplify(sp.radsimp(Fc.subs(vals).subs(c, cF))) == 0
                and sp.N(up) > 0 and sp.N(um) < 0 and -1 < sp.N(cF) < 1)
    sdet.append(f"({jx},{jy},{jz}): kc2 = {sp.N(up, 12)}")
conds4.append(ok_samp)
# grid check of the flip criterion on random rational triangle-regime couplings (consequence of the identities; mp 40 digits)
mp.mp.dps = 40
rng = random.Random(7)
n_flip = n_noflip = n_bad = 0
for _ in range(400):
    jx, jy = (mp.mpf(rng.randint(5, 40)) / 10 for _ in range(2))
    lo, hi = abs(jx - jy), jx + jy
    jz = lo + (hi - lo) * mp.mpf(rng.randint(1, 99)) / 100
    ss, pp = jx + jy, jx * jy
    D_ = 4 * jz ** 4 * pp + 4 * jz ** 3 * pp * ss + 4 * jz ** 2 * pp ** 2 - 4 * jz ** 2 * pp * ss ** 2 + jz ** 2 * ss ** 4 - 8 * jz * pp * ss ** 3 + 2 * jz * ss ** 5 - 4 * pp * ss ** 4 + ss ** 6
    n0 = (ss ** 2 - 2 * pp - jz ** 2) * (2 * jz ** 3 * pp - 4 * jz * pp * ss ** 2 + jz * ss ** 4 - 4 * pp * ss ** 3 + ss ** 5)
    n1 = 2 * jz ** 2 * pp - jz ** 2 * ss ** 2 - 4 * pp * ss ** 2 + ss ** 4
    dn = -8 * (ss ** 2 + jz * ss - jz ** 2) * (jz ** 3 - 4 * pp * ss + ss ** 3)
    upv, umv = (n0 + n1 * mp.sqrt(D_)) / dn, (n0 - n1 * mp.sqrt(D_)) / dn
    crit = abs(jx ** 2 - jy ** 2) < jz ** 2
    if abs(abs(jx ** 2 - jy ** 2) - jz ** 2) < mp.mpf("1e-6"):
        continue
    n_flip += int(crit); n_noflip += int(not crit)
    n_bad += int((upv > 0) != crit or umv >= 0 or D_ <= 0)
conds4.append(n_bad == 0 and n_flip > 50 and n_noflip > 50)
ok4, bad4 = allok(conds4)
check("A4 branch facts (u(c) strictly decreasing bijection, F_c(-1) < 0 < F_c(1), F_c(c0), u_- < 0, Den > 0): flip iff Jz < Jx+Jy and |Jx^2-Jy^2| < Jz^2; iso kc^2 = J(J+2)/(4(4+2J-J^2)); exact samples", ok4,
      f"iso u_- = -1/4; {'; '.join(sdet)}; grid of 400 couplings: criterion vs sign u_+ and u_- < 0, bad = {n_bad} (flip {n_flip}, no flip {n_noflip})" + bad4)

# A5 (float): sign of the numerical kernel-projector triple product at the line node, straddling kappa_c
def T_node(Jv, kappa):
    Jx0, Jy0, Jz0 = Jv; P0 = Jx0 * Jy0; S0 = Jx0 ** 2 + Jy0 ** 2 - Jz0 ** 2; u0 = kappa ** 2
    cm = (P0 - np.sqrt(P0 ** 2 + 4 * u0 * (4 * u0 + S0))) / (4 * u0)
    x0 = np.arccos(cm) / (2 * np.pi)
    f0 = np.array([x0, 1 - x0, 0.0])
    B = Bloch(Jv, kappa)
    H0, dH = B.dH(f0)
    w, V = np.linalg.eigh(H0)
    Pp = V[:, 1:3] @ V[:, 1:3].conj().T
    T = np.imag(np.trace(Pp @ dH[0] @ Pp @ dH[1] @ Pp @ dH[2]))
    A2_ = Jx0 * Jy0 * (Jx0 + Jy0 + Jz0); A1_ = (Jx0 + Jy0) * (Jx0 ** 2 + Jy0 ** 2 + Jz0 * (Jx0 + Jy0)); A0_ = (Jx0 + Jz0) * (Jy0 + Jz0) * (Jx0 + Jy0 - Jz0)
    Fc0 = A2_ * cm ** 2 + A1_ * cm + A0_
    Tf = -32 * np.pi ** 3 * kappa * (8 * u0 * cm - 2 * P0) * Fc0 * np.sin(2 * np.pi * x0) / Jz0 ** 3
    return T, Tf, Fc0, float(np.max(np.abs(w[1:3])))


def kc2_closed(Jv):
    jx, jy, jz = (mp.mpf(str(v)) for v in Jv); ss, pp = jx + jy, jx * jy
    D_ = 4 * jz ** 4 * pp + 4 * jz ** 3 * pp * ss + 4 * jz ** 2 * pp ** 2 - 4 * jz ** 2 * pp * ss ** 2 + jz ** 2 * ss ** 4 - 8 * jz * pp * ss ** 3 + 2 * jz * ss ** 5 - 4 * pp * ss ** 4 + ss ** 6
    n0 = (ss ** 2 - 2 * pp - jz ** 2) * (2 * jz ** 3 * pp - 4 * jz * pp * ss ** 2 + jz * ss ** 4 - 4 * pp * ss ** 3 + ss ** 5)
    n1 = 2 * jz ** 2 * pp - jz ** 2 * ss ** 2 - 4 * pp * ss ** 2 + ss ** 4
    return (n0 + n1 * mp.sqrt(D_)) / (-8 * (ss ** 2 + jz * ss - jz ** 2) * (jz ** 3 - 4 * pp * ss + ss ** 3))


flip_J = [(1.0, 0.8, 1.0), (1.2, 0.8, 1.0), (0.9, 1.1, 1.3), (2.0, 1.0, 2.5), (1.0, 1.0, 1.0), (1.0, 1.0, 1.9)]
conds5 = []; kcs = []; maxrel = 0.0; npts = 0
for Jv in flip_J:
    kc = float(mp.sqrt(kc2_closed(Jv))); kcs.append(f"{kc:.5f}")
    sg = []
    for rel in (-0.2, -1e-3, 1e-3, 0.2):
        T, Tf, Fc0, mid = T_node(Jv, kc * (1 + rel)); npts += 1
        sg.append(np.sign(T)); maxrel = max(maxrel, abs(T - Tf) / abs(Tf)); conds5.append(mid < 1e-9 and np.sign(Fc0) == np.sign(T))
    conds5.append(sg == [1, 1, -1, -1])
for Jv in ((3.0, 2.0, 1.5), (2.0, 1.0, 1.5)):
    conds5.append(float(kc2_closed(Jv)) < 0)
    for kap in (0.05, 0.3, 1.0, 3.0):
        T, Tf, Fc0, mid = T_node(Jv, kap); npts += 1
        maxrel = max(maxrel, abs(T - Tf) / abs(Tf)); conds5.append(np.sign(T) == -1 and np.sign(Fc0) == -1)
conds5.append(maxrel < 1e-6)
ok5, bad5 = allok(conds5)
check("A5 FLOAT: Bloch kernel-projector triple product at the x<1/2 line node: sign +1 -> -1 across kappa_c(1 +- 1e-3) at six couplings; -1 for all kappa at two no-flip couplings", ok5,
      f"kappa_c = {', '.join(kcs)}; {npts} points, max |T - T_formula|/|T_formula| = {maxrel:.1e}" + bad5)

# ================================================================================================ (B) Gamma at J = 2
eps = sp.Symbol("eps", positive=True)
x, y, z = sp.symbols("x y z", real=True)
k = sp.Symbol("k", positive=True)
lam = sp.Symbol("lam")
E_, A_, B_ = (1, -1, 0), (1, 1, 0), (0, 0, 1)
w1 = sp.Matrix([1, 0, -1, 0]) / sp.sqrt(2); w2 = sp.Matrix([0, 1, 0, -1]) / sp.sqrt(2)
Wm = sp.Matrix.hstack(w1, w2)


def trunc(e, n):
    e = sp.expand(e)
    if e == 0:
        return sp.Integer(0)
    p_ = sp.Poly(e, eps)
    return sum(co * eps ** m_ for (m_,), co in p_.terms() if m_ <= n)


def expser(phi, n):
    out = sp.Integer(1); term = sp.Integer(1)
    for m_ in range(1, n + 1):
        term = trunc(term * sp.I * phi / m_, n); out += term
    return trunc(out, n)


def weighted_H(kv, wy, N):
    """H(theta) with theta = eps x (1,-1,0) + eps^wy [y (1,1,0) + z (0,0,1)], entries Taylor-truncated at eps^N (J = (1,1,2), odd amplitude 2 kv)."""
    amp = {"x": 2, "y": 2, "z": 4, "odd": 2 * kv}
    M = sp.zeros(4, 4); M0 = sp.zeros(4, 4)
    for (a_, b_, n_, kind_) in TERMS:
        t = amp[kind_]
        M0[a_, b_] += t; M0[b_, a_] -= t
        phi = eps * x * sum(n_[j] * E_[j] for j in range(3)) + eps ** wy * (y * sum(n_[j] * A_[j] for j in range(3)) + z * sum(n_[j] * B_[j] for j in range(3)))
        M[a_, b_] += t * expser(phi, N); M[b_, a_] -= t * expser(-phi, N)
    return M0, (sp.I * M).applyfunc(lambda e: trunc(e, N))


def schur_pauli(H, Nd):
    """E = 0 Schur complement on ker H(0) (Brillouin-Wigner series with G0 = H(0)/64) to eps^Nd; Pauli vector in the real kernel basis w1, w2."""
    H0 = H.subs(eps, 0); Pk = sp.eye(4) - H0 * H0 / 64; G0 = H0 / 64
    V = (H - H0).applyfunc(lambda e: trunc(e, Nd))
    mm = lambda A, B: (A * B).applyfunc(lambda e: trunc(e, Nd))
    acc = mm(mm(Pk, V), Pk); cur = mm(Pk, V); sg = -1
    for m_ in range(2, Nd + 1):
        cur = mm(cur, G0 * V); acc = acc + sg * mm(cur, Pk); sg = -sg
    h2 = (Wm.T * acc * Wm).applyfunc(sp.expand)
    herm = sp.simplify(h2[0, 1] - sp.conjugate(h2[1, 0])) == 0 and sp.simplify(sp.im(h2[0, 0])) == 0 and sp.simplify(sp.im(h2[1, 1])) == 0
    d0 = sp.expand((h2[0, 0] + h2[1, 1]) / 2); dz_ = sp.expand((h2[0, 0] - h2[1, 1]) / 2)
    dx_ = sp.expand((h2[0, 1] + h2[1, 0]) / 2); dy_ = sp.expand(sp.I * (h2[0, 1] - h2[1, 0]) / 2)      # h12 = d_x - i d_y
    return herm, d0, dx_, dy_, dz_, Pk


def det_trunc(H, N):
    mm = lambda A, B: (A * B).applyfunc(lambda e: trunc(e, N))
    H2 = mm(H, H); H3 = mm(H2, H); H4 = mm(H3, H)
    p1, p2, p3, p4 = (trunc(sp.expand(A.trace()), N) for A in (H, H2, H3, H4))
    return trunc(sp.expand((p1 ** 4 - 6 * p1 ** 2 * p2 + 3 * p2 ** 2 + 8 * p1 * p3 - 6 * p4) / 24), N)


def cw(e, m_):
    return sp.expand(sp.Poly(sp.expand(e), eps).coeff_monomial(eps ** m_)) if e != 0 else sp.Integer(0)


# B1: generic kappa, weights (1,2,2), to weight 4
M0g, Hg = weighted_H(k, 2, 4)
H0g = sp.I * M0g
lamS = sp.Symbol("lamS")
herm, d0, dx, dy, dz, Pk = schur_pauli(Hg, 4)
a_coef = (1 - 4 * k ** 2) / 2
dlead = (2 * (y - z), a_coef * x ** 2, -8 * k * y)
Dser = det_trunc(Hg, 4)
Dp = sp.Poly(Dser, eps)
D4 = sp.expand(Dp.coeff_monomial(eps ** 4))
low_ok = all(sp.expand(Dp.coeff_monomial(eps ** m_)) == 0 for m_ in range(5) if m_ != 4)
Kk = k ** 2; rt = sp.sqrt(256 * Kk ** 2 - 32 * Kk + 9)
th1, th2, th3 = sp.symbols("th1 th2 th3", real=True)
Hess = sp.hessian(64 * (4 * (y - z) ** 2 + 64 * k ** 2 * y ** 2).subs({y: (th1 + th2) / 2, z: th3}), (th1, th2, th3))
cpC = sp.expand(lamS * (lamS - 128 * (16 * Kk + 3 + rt)) * (lamS - 128 * (16 * Kk + 3 - rt)))
conds_b1 = [M0g == 4 * sp.Matrix([[0, 1, 0, 1], [-1, 0, -1, 0], [0, 1, 0, 1], [-1, 0, -1, 0]]),
            sp.expand(H0g.charpoly(lam).as_expr() - lam ** 2 * (lam ** 2 - 64)) == 0,
            sp.simplify(H0g * H0g - 64 * (sp.eye(4) - Pk)) == sp.zeros(4, 4) and Pk.trace() == 2,
            herm and d0 == 0, all(cw(e, m_) == 0 for e in (dx, dy, dz) for m_ in (1, 3)),
            sp.expand(cw(dx, 2) - dlead[0]) == 0 and sp.expand(cw(dy, 2) - dlead[1]) == 0 and sp.expand(cw(dz, 2) - dlead[2]) == 0,
            sp.expand(sp.Poly(cw(dy, 4), x, y, z).coeff_monomial(x ** 4) - (20 * k ** 2 + 1) / 48) == 0
            and sp.Poly(cw(dx, 4), x, y, z).coeff_monomial(x ** 4) == 0 and sp.Poly(cw(dz, 4), x, y, z).coeff_monomial(x ** 4) == 0,
            low_ok and sp.expand(D4 - 64 * sum(e ** 2 for e in dlead)) == 0,
            sp.simplify(sp.expand(Hess.charpoly(lamS).as_expr()) - cpC) == 0 and sp.simplify(Hess * sp.Matrix([1, -1, 0])) == sp.zeros(3, 1)]
okb1, badb1 = allok(conds_b1)
check("B1 Gamma, J = 2: spectrum {0,0,+-8} for every kappa; weighted (x:1, y,z:2) Schur-complement Pauli vector to weight 4 and weight-4 part of det H = 64|d|^2", okb1,
      "d = (2(y-z), (1-4k^2)x^2/2, -8k y), d0 = 0, d_y4 x^4 coeff (20k^2+1)/48; det H = 16[(1-4K)^2 x^4 + 256K y^2 + 16(y-z)^2]; Hessian eigenvalues 128[16K+3 +- sqrt(256K^2-32K+9)], null (1,-1,0)" + badb1)

# B2: kappa = 1/2, weights (1,4,4), det H to eps^8
M0h, Hh = weighted_H(sp.Rational(1, 2), 4, 8)
herm2, d0h, dxh, dyh, dzh, _ = schur_pauli(Hh, 4)
D8 = det_trunc(Hh, 8)
D8p = sp.Poly(D8, eps)
dl2 = (2 * (y - z), x ** 4 / 8, -4 * y)
conds_b2 = [herm2 and d0h == 0, all(cw(e, m_) == 0 for e in (dxh, dyh, dzh) for m_ in (0, 1, 2, 3)),
            sp.expand(cw(dxh, 4) - dl2[0]) == 0 and sp.expand(cw(dyh, 4) - dl2[1]) == 0 and sp.expand(cw(dzh, 4) - dl2[2]) == 0,
            all(sp.expand(D8p.coeff_monomial(eps ** m_)) == 0 for m_ in range(8)) and sp.expand(D8p.coeff_monomial(eps ** 8) - 64 * sum(e ** 2 for e in dl2)) == 0]
okb2, badb2 = allok(conds_b2)
check("B2 kappa = 1/2 (x^2 term absent): weights x:1, y,z:4, d = (2(y-z), x^4/8, -4y) with no weight 1-3 terms; det H = 64|d|^2 at eps^8 (quartic soft direction)", okb2,
      f"det H eps^8 part = {sp.factor(D8p.coeff_monomial(eps ** 8))}" + badb2)

# B3: local degree 0, symmetry, T(Gamma) = 0, pair born at Gamma
a_s, k_s, pr, rp = sp.symbols("a_s k_s pr rp", positive=True)
Jac = sp.Matrix([[0, 2, -2], [2 * a_s * x, 0, 0], [0, -8 * k_s, 0]])
JacK = sp.Matrix([[0, 2, -2], [x ** 3 / 2, 0, 0], [0, -4, 0]])
sw = {x: -x, y: -y, z: -z}
Lm = sp.Matrix([[sp.diff(e, v) for v in (x, y, z)] for e in dlead])
dH0 = [sp.zeros(4, 4) for _ in range(3)]
for (a_, b_, n_, kind_) in TERMS:
    t = {"x": 2, "y": 2, "z": 4, "odd": 2 * k}[kind_]
    for j in range(3):
        dH0[j][a_, b_] += sp.I * (sp.I * t * n_[j]); dH0[j][b_, a_] += sp.I * (-1) * t * (-sp.I * n_[j])
Tg = sp.simplify(sp.im(sp.simplify((Pk * dH0[0] * Pk * dH0[1] * Pk * dH0[2]).trace())))
xsol_pos = sp.solve(x ** 4 / 8 - rp, x); xsol_neg = sp.solve(x ** 4 / 8 + rp, x)
c4 = (20 * k ** 2 + 1) / 48
pair_ok = (sp.simplify(a_coef.subs(k, sp.Rational(1, 2))) == 0 and all(sp.expand(a_coef.subs(k, kv)).is_negative for kv in (sp.Rational(11, 20), sp.Rational(51, 100)))
           and all(sp.expand(a_coef.subs(k, kv)).is_positive for kv in (sp.Rational(2, 5), sp.Rational(1, 4))) and c4.subs(k, sp.Rational(1, 2)) == sp.Rational(1, 8))
pair_ratios = []
for kv in (0.55, 0.51, 0.505):
    K_ = kv ** 2; x0 = np.sqrt(-((1 - 4 * K_) / 2) / ((20 * K_ + 1) / 48)); ex = np.arccos(1 / (2 * K_) - 1)
    pair_ratios.append(x0 / ex)
conds_b3 = [sp.factor(Jac.det()) == 32 * a_s * k_s * x, sp.expand(JacK.det() - 4 * x ** 3) == 0,
            len([s_ for s_ in sp.solve([2 * (y - z) - pr, a_s * x ** 2 - rp, -8 * k_s * y], [y, z, x], dict=True)]) == 2,
            sum(1 for s_ in xsol_pos if s_.is_real is True) == 2 and sum(1 for s_ in xsol_neg if s_.is_real is True) == 0,
            Lm.subs({x: 0}).rank() == 2 and Lm.subs({x: 0}).det() == 0,
            all(sp.expand(dd.subs(sw, simultaneous=True) - sgn * dd) == 0 for dd, sgn in ((dx, -1), (dy, 1), (dz, -1))),
            Tg == 0, pair_ok, all(0.97 < pr_ < 1.0 for pr_ in pair_ratios)]
okb3, badb3 = allok(conds_b3)
check("B3 local degree of d/|d| at Gamma = 0 for every kappa > 0: leading-map Jacobian 32 a kappa x (4 x^3 at kappa = 1/2) is odd in x, two preimages of opposite sign; rank L = 2, T(Gamma) = 0, d(-theta) = (-d_x,d_y,-d_z)", okb3,
      "pair born at Gamma for kappa > 1/2 = zeros of d_y = x^2 (a + c4 x^2), c4 = (20K+1)/48 > 0, a < 0 iff K > 1/4; float x0_eff/x0_exact at kappa = 0.55, 0.51, 0.505: "
      + ", ".join(f"{v_:.4f}" for v_ in pair_ratios) + badb3)


# B4 (float): Fukui fluxes of the lowest two bands
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


conds_b4 = []; fl_zero = []; pm_max = 0.0; gap_min = 1.0
for kappa, p_, eta, svals in ((0.5, 4, 1 / 32., (0.3, 0.2)), (1.0, 2, 0.2, (0.3, 0.15))):
    B = Bloch((1., 1., 2.), kappa)
    for s_ in svals:
        c_w = (0.3 * s_, 0.5 * eta * s_ ** p_, -0.4 * eta * s_ ** p_)
        inside = (c_w[0] / s_) ** 2 + (c_w[1] / (eta * s_ ** p_)) ** 2 + (c_w[2] / (eta * s_ ** p_)) ** 2
        for m_ in (48, 96):
            fl_, gap, pm = flux(B, weighted_off(s_, eta, p_, c_w), m_)
            conds_b4.append(inside < 1 and abs(fl_) < 1e-9 and pm < 1.0 and gap > 0)
            fl_zero.append(fl_); pm_max = max(pm_max, pm); gap_min = min(gap_min, gap)
B1c = Bloch((1., 1., 2.), 1.0)
xn = np.arccos(-0.5) / (2 * np.pi)                                    # kappa = 1: other line root c = 1/(2K) - 1 = -1/2
ctrl = []
for cen_ in ((xn, 1 - xn, 0.0), (1 - xn, xn, 0.0)):
    fl_, gap, pm = flux(B1c, round_sphere(cen_, 0.03, axis=(0., 0., 1.)), 64)
    ctrl.append(fl_); conds_b4.append(pm < 1.0)
conds_b4.append(abs(ctrl[0] - 1) < 1e-9 and abs(ctrl[1] + 1) < 1e-9)
kap = 0.55; Bp = Bloch((1., 1., 2.), kap)
xp = np.arccos(1 / (2 * kap ** 2) - 1) / (2 * np.pi); dist = np.sqrt(2) * xp
pair = []
for cen_, rho in (((0, 0, 0), 0.3 * dist), ((xp, -xp, 0), 0.3 * dist), ((-xp, xp, 0), 0.3 * dist), ((0, 0, 0), 1.6 * dist)):
    fl_, gap, pm = flux(Bp, round_sphere(cen_, rho), 96)
    pair.append(fl_); conds_b4.append(pm < 1.0)
conds_b4.append(abs(pair[0]) < 1e-9 and abs(pair[1] + 1) < 1e-9 and abs(pair[2] - 1) < 1e-9 and abs(pair[3]) < 1e-9)
okb4, badb4 = allok(conds_b4)
check("B4 FLOAT: Fukui flux of the lowest two bands through off-centre weighted ellipsoids enclosing Gamma (kappa = 0.5 and 1, m = 48, 96) is 0; controls: line nodes +-1; pair at kappa = 0.55", okb4,
      f"{len(fl_zero)} ellipsoids: max |flux| = {max(abs(v_) for v_ in fl_zero):.1e}, max |plaquette phase| = {pm_max:.2f}, min middle gap = {gap_min:.1e}; kappa = 1 nodes (1/3,2/3,0), (2/3,1/3,0): "
      f"{ctrl[0]:+.3f}, {ctrl[1]:+.3f}; kappa = 0.55 Gamma alone, +x' node, -x' node, all three: {pair[0]:+.3f}, {pair[1]:+.3f}, {pair[2]:+.3f}, {pair[3]:+.3f}" + badb4)

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}   ({time.time() - T0:.0f} s)")
