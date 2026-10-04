#!/usr/bin/env python3
"""Composite-site network, supplied u = +1 comparator, GENERAL couplings: the exact line of middle-band touchings f = (x, 1-x, 0).

Supplied u = +1 quadratic Majorana comparator of the landed notes (landed hopping-sign convention), four-site Bloch matrix H(f) = i M(f) over the fractional
zone, general couplings J_x, J_y, J_z and odd term kappa (network terms of kcert7_runner.py, amplitudes tagged x, y, z, odd).  Notation: P = JxJy,
S = Jx^2+Jy^2-Jz^2, u = kappa^2, c = cos 2 pi x, q(c) = 4u c^2 - 2P c - (4u+S), d^2 = P^2 + 4u(4u+S), c_(-+) = (P -+ d)/(4u),
F_c(c) = JxJy(Jx+Jy+Jz) c^2 + (Jx+Jy)(Jx^2+Jy^2+Jz(Jx+Jy)) c + (Jx+Jz)(Jy+Jz)(Jx+Jy-Jz).
EXACT (sympy, symbolic couplings; pseudo-remainder "mod q" is over Q(Jx,Jy,Jz,kappa)[c], all couplings and kappa > 0): checks 1-5, 7 (identities), 10;
EXACT rational (python Fractions, exact tower arithmetic over Q) : check 8 and the exact flip test of check 7;  HIGH PRECISION (mpmath, 50-100 digits, exact decimal
couplings) comparison with the double-precision certified nodes of the anisotropic certificate (open PR 9419) (inlined constants from result_A..E.json): checks 6 and 9.
REPORTED, not asserted (printed as [REPORTED]): the closed form of kappa_c (sympy-rationalised, numerically verified only) and the PSLQ-identified quintic of
the off-plane nodes (identification, not a proof).
Checks: (1) spectrum {+-l1, +-l2} for every f and all couplings, symmetries I and S; (2) det H = 16 q(c)^2 on the line; (3) double zero at the roots (levels
0, 0, +-4Jz, all 3x3 minors vanish); (4) q(+-1) and d^2 identities and the regime table (Sturm count at 600 random rational couplings); (5) exact charge
T = -32 pi^3 kappa q'(c) F_c(c) sin(2 pi x)/Jz^3 = +-64 pi^3 kappa d F_c sin/Jz^3 at c_(-+); (6) isotropic reduction to the landed formula; (7) sign analysis and flip
criterion |Jx^2 - Jy^2| < Jz^2; (8) independent exact-rational grid of 2400 couplings; (9) 50-digit reproduction of the certified line nodes A-E with signs;
(10) the shear R: f3 -> f1+f2-f3 is a spectral symmetry iff Jx = Jy.
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import random
import time
from fractions import Fraction as Fr

import mpmath as mp
import sympy as sp
from sympy import ZZ
from sympy.polys.rings import ring

AUDIT_TIMEOUT_SEC = 600

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label} :: {detail}", flush=True)


def reported(label, detail):
    print(f"[REPORTED] {label} :: {detail}", flush=True)


# ------------------------------------------------------------------------------------------------ network (copied from kcert7_runner.py)
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


def reduce_site(p):
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)


def tagged_terms():
    """(a, b, n, kind): M(f)[a,b] += t e^{2 pi i f.n}, M(f)[b,a] -= t e^{-2 pi i f.n}; kind in x, y, z (hopping J_x, J_y, J_z) or odd (kappa)."""
    out = []
    for p in REPS:
        a, n0 = reduce_site(p)
        assert n0 == (0, 0, 0) and is_site(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce_site(q)
                out.append((a, b, n, flavour(p, q)))
        nb = {flavour(p, q): q for q in neighbours(p)}
        assert len(nb) == 3
        for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
            r1, n1 = reduce_site(nb[l]); r2, n2 = reduce_site(nb[m])
            out.append((r1, r2, tuple(n2[i] - n1[i] for i in range(3)), "odd"))
    return out


TERMS = tagged_terms()
Jx, Jy, Jz, k, c, mu = sp.symbols("Jx Jy Jz k c mu")
z, w1, w2, w3 = sp.symbols("z w1 w2 w3")
AMP = {"x": 2 * Jx, "y": 2 * Jy, "z": 2 * Jz, "odd": 2 * k}


def M_general(a1, a2, a3):
    M = sp.zeros(4, 4)
    for (a, b, n, kind) in TERMS:
        t = AMP[kind]
        mon = a1 ** n[0] * a2 ** n[1] * a3 ** n[2]
        M[a, b] += t * mon
        M[b, a] -= t / mon
    return M.applyfunc(sp.expand)


def charpoly(M):
    cp = sp.Poly(sp.expand((mu * sp.eye(4) - M).det(method="berkowitz")), mu)
    d = {e: sp.expand(co) for (e,), co in cp.terms()}
    return [d.get(e, sp.Integer(0)) for e in (4, 3, 2, 1, 0)]


u = k ** 2; P = Jx * Jy; S = Jx ** 2 + Jy ** 2 - Jz ** 2
qc = 4 * u * c ** 2 - 2 * P * c - (4 * u + S)
d2s = P ** 2 + 4 * u * (4 * u + S)
Fc = Jx * Jy * (Jx + Jy + Jz) * c ** 2 + (Jx + Jy) * (Jx ** 2 + Jy ** 2 + Jz * (Jx + Jy)) * c + (Jx + Jz) * (Jy + Jz) * (Jx + Jy - Jz)


def zero_mod_q(f):
    return sp.expand(sp.prem(sp.Poly(sp.expand(f), c), sp.Poly(qc, c)).as_expr()) == 0


# ------------------------------------------------------------------------------------------------ exact helpers (Fractions)
def exact_sign(p, q, D):
    """sign(p + q sqrt(D)) for rationals p, q and D >= 0, exact."""
    p, q, D = Fr(p), Fr(q), Fr(D)
    if D == 0 or q == 0:
        return (p > 0) - (p < 0)
    if p >= 0 and q >= 0:
        return 1 if (p > 0 or q > 0) else 0
    if p <= 0 and q <= 0:
        return -1
    lhs, rhs = p * p, q * q * D
    if lhs == rhs:
        return 0
    return (1 if p > 0 else -1) if lhs > rhs else (1 if q > 0 else -1)


def Fc_coeffs(jx, jy, jz):
    return jx * jy * (jx + jy + jz), (jx + jy) * (jx * jx + jy * jy + jz * (jx + jy)), (jx + jz) * (jy + jz) * (jx + jy - jz)


def Fc_over_d(jx, jy, jz, kap, sgn):
    """F_c(c) = f0 + f1 d at c = (P + sgn d)/(4u) (sgn = -1: c_-, +1: c_+); returns (f0, f1, d2)."""
    u_ = Fr(kap) ** 2; P_ = Fr(jx) * Fr(jy); S_ = Fr(jx) ** 2 + Fr(jy) ** 2 - Fr(jz) ** 2
    d2 = P_ * P_ + 4 * u_ * (4 * u_ + S_)
    A2, A1, A0 = Fc_coeffs(Fr(jx), Fr(jy), Fr(jz))
    cc0 = P_ / (4 * u_); cc1 = Fr(sgn) / (4 * u_)
    c2_0 = cc0 * cc0 + cc1 * cc1 * d2; c2_1 = 2 * cc0 * cc1
    return A2 * c2_0 + A1 * cc0 + A0, A2 * c2_1 + A1 * cc1, d2


# ================================================================================================ symbolic core
Mg = M_general(w1, w2, w3)
cg = charpoly(Mg)
a2g, a0g = cg[2], cg[4]
inv = lambda e: sp.expand(e.subs({w1: 1 / w1, w2: 1 / w2, w3: 1 / w3}, simultaneous=True))
swp = lambda e: sp.expand(e.subs({w1: w2, w2: w1}, simultaneous=True))
ok1 = sp.simplify(Mg.trace()) == 0 and cg[1] == 0 and cg[3] == 0
ok1s = sp.expand(inv(a0g) - a0g) == 0 and sp.expand(inv(a2g) - a2g) == 0 and sp.expand(swp(a0g) - a0g) == 0 and sp.expand(swp(a2g) - a2g) == 0
check("1 even spectrum", ok1 and ok1s, "tr M = 0, mu^3 and mu^1 coefficients of det(mu-M) vanish identically in (z1,z2,z3,Jx,Jy,Jz,kappa): spec H = {+-l1,+-l2}, det H = l1^2 l2^2 >= 0, "
      "middle touching <=> det H = 0; det M and the mu^2 coeff invariant under f->-f and f1<->f2")

Ml = M_general(z, 1 / z, sp.Integer(1))
cl = charpoly(Ml)
cz = (z + 1 / z) / 2
ok2a = sp.expand(cl[4] - 16 * qc.subs(c, cz) ** 2) == 0 and cl[1] == 0 and cl[3] == 0
e2_line = 8 * (Jx ** 2 + Jy ** 2 + Jz ** 2 + 2 * P * c + 4 * u * (1 - c ** 2))
ok2b = sp.expand(cl[2] - e2_line.subs(c, cz)) == 0 and zero_mod_q(e2_line - 16 * Jz ** 2)
iso_line = sp.expand(qc.subs({Jx: 1, Jy: 1}) - (4 * k ** 2 * c ** 2 - 2 * c + Jz ** 2 - 4 * k ** 2 - 2)) == 0
check("2 line determinant", ok2a and ok2b and iso_line, "on (z,1/z,1): det H = 16 q(c)^2, q = 4k^2c^2 - 2JxJy c + Jz^2-Jx^2-Jy^2-4k^2; mu^2 coeff = 8[Jx^2+Jy^2+Jz^2+2Pc+4k^2(1-c^2)] = 16 Jz^2 "
      "at q = 0 (levels 0,0,+-4Jz); Jx=Jy=1 gives the landed 4k^2c^2-2c+J^2-4k^2-2")

# ------------------------------------------------------------------------------------------------ ring Z[Jx,Jy,Jz,k,c][z]/(z^2 - 2cz + 1)
R_, rJx, rJy, rJz, rk, rc = ring("Jx,Jy,Jz,k,c", ZZ)
ZERO = (R_.zero, R_.zero); ONE = (R_.one, R_.zero); Zg = (R_.zero, R_.one); Zinv = (2 * rc, -R_.one)
add = lambda a, b: (a[0] + b[0], a[1] + b[1])
sub = lambda a, b: (a[0] - b[0], a[1] - b[1])
scal = lambda a, s: (a[0] * s, a[1] * s)


def mul(a, b):
    bd = a[1] * b[1]
    return (a[0] * b[0] - bd, a[0] * b[1] + a[1] * b[0] + 2 * rc * bd)


ZP = {0: ONE}
for _e in range(1, 4):
    ZP[_e] = mul(ZP[_e - 1], Zg); ZP[-_e] = mul(ZP[-_e + 1], Zinv)
RAMP = {"x": 2 * rJx, "y": 2 * rJy, "z": 2 * rJz, "odd": 2 * rk}
mz = lambda: [[ZERO for _ in range(4)] for _ in range(4)]


def mm(A, B):
    out = mz()
    for r in range(4):
        for q_ in range(4):
            s = ZERO
            for m_ in range(4):
                if A[r][m_] != ZERO and B[m_][q_] != ZERO:
                    s = add(s, mul(A[r][m_], B[m_][q_]))
            out[r][q_] = s
    return out


tr = lambda A: add(add(A[0][0], A[1][1]), add(A[2][2], A[3][3]))
Mr = mz(); Nr = [mz() for _ in range(3)]
for (a, b, n, kind) in TERMS:
    t = RAMP[kind]; e = n[0] - n[1]                      # z1 = z, z2 = 1/z, z3 = 1
    Mr[a][b] = add(Mr[a][b], scal(ZP[e], t)); Mr[b][a] = sub(Mr[b][a], scal(ZP[-e], t))
    for j in range(3):
        if n[j]:
            Nr[j][a][b] = add(Nr[j][a][b], scal(ZP[e], t * n[j])); Nr[j][b][a] = add(Nr[j][b][a], scal(ZP[-e], t * n[j]))
M2 = mm(Mr, Mr)
E2x2 = sub(mul(tr(Mr), tr(Mr)), tr(M2))                  # = 2 e2(M) (tr M = 0)
Pt2 = [[add(scal(M2[r][q_], 2), E2x2) if r == q_ else scal(M2[r][q_], 2) for q_ in range(4)] for r in range(4)]   # 2 Pt = 2 M^2 + 2 e2 I
z_ = lambda el: zero_mod_q(el[0].as_expr()) and zero_mod_q(el[1].as_expr())
MP = mm(Mr, Pt2); PP = mm(Pt2, Pt2)
ok3 = tr(Mr) == ZERO and zero_mod_q(E2x2[0].as_expr() - 32 * Jz ** 2) and E2x2[1] == R_.zero
ok3 &= all(z_(MP[r][q_]) for r in range(4) for q_ in range(4))
ok3 &= all(z_(sub(PP[r][q_], mul(E2x2, Pt2[r][q_]))) for r in range(4) for q_ in range(4))
trP = tr(Pt2)
ok3 &= z_(sub(trP, scal(E2x2, 2)))


def det3(A):
    r = lambda i, j: A[i][j]
    t1 = mul(r(0, 0), sub(mul(r(1, 1), r(2, 2)), mul(r(1, 2), r(2, 1))))
    t2 = mul(r(0, 1), sub(mul(r(1, 0), r(2, 2)), mul(r(1, 2), r(2, 0))))
    t3 = mul(r(0, 2), sub(mul(r(1, 0), r(2, 1)), mul(r(1, 1), r(2, 0))))
    return add(sub(t1, t2), t3)


ok_min = True
for i in range(4):
    for j in range(4):
        rows = [r for r in range(4) if r != i]; cols = [q_ for q_ in range(4) if q_ != j]
        ok_min &= z_(det3([[Mr[r][q_] for q_ in cols] for r in rows]))
check("3 double zero", ok3 and ok_min, "at q(c) = 0: e2(M) = 16 Jz^2, M Pt = 0, Pt^2 = e2 Pt, tr Pt = 2 e2 (Pt/e2 = rank-2 kernel projector), all sixteen 3x3 minors of M vanish "
      "(rank 2, adj = 0, grad det H = 0): a genuine double zero level, outer levels +-4Jz")

# ------------------------------------------------------------------------------------------------ 4 regime table
ok4 = sp.expand(qc.subs(c, 1) - (Jz ** 2 - (Jx + Jy) ** 2)) == 0 and sp.expand(qc.subs(c, -1) - (Jz ** 2 - (Jx - Jy) ** 2)) == 0
ok4 &= sp.expand(qc - ((4 * u * c - P) ** 2 - d2s) / (4 * u)) == 0
ok4 &= sp.expand(d2s - (4 * u + P) ** 2 - 4 * u * ((Jx - Jy) ** 2 - Jz ** 2)) == 0
ok4 &= sp.expand(d2s - (4 * u - P) ** 2 - 4 * u * ((Jx + Jy) ** 2 - Jz ** 2)) == 0
rng = random.Random(4)
vals = [Fr(i, 10) for i in range(2, 41)]
cq = sp.Symbol("cq")
cnt = {"tri": 0, "big": 0, "small": 0}; bad4 = 0; nsamp = 0
while nsamp < 600:
    jx, jy, jz, kk = rng.choice(vals), rng.choice(vals), rng.choice(vals), Fr(rng.randint(1, 100), 20)
    if jz in (jx + jy, abs(jx - jy)):
        continue
    P_ = jx * jy; u_ = kk * kk; S_ = jx * jx + jy * jy - jz * jz; d2 = P_ * P_ + 4 * u_ * (4 * u_ + S_)
    if d2 == 0 or 4 * u_ == P_:
        continue
    nsamp += 1
    if abs(jx - jy) < jz < jx + jy:
        reg = "tri"; want = 1
    elif jz > jx + jy:
        reg = "big"; want = 2 if (d2 > 0 and 4 * u_ > P_) else 0
    else:
        reg = "small"; want = 0
    cnt[reg] += 1
    qp = sp.Poly(sp.Rational(4 * u_.numerator, u_.denominator) * cq ** 2 - sp.Rational(2 * P_.numerator, P_.denominator) * cq
                 - sp.Rational((4 * u_ + S_).numerator, (4 * u_ + S_).denominator), cq)
    got = qp.count_roots(-1, 1)                              # simple roots only (d2 != 0), none at +-1 (Jz not on the triangle boundary)
    bad4 += (got != want)
check("4 regime table", ok4 and bad4 == 0, f"q(1) = Jz^2-(Jx+Jy)^2, q(-1) = Jz^2-(Jx-Jy)^2, d^2-(4u+-P)^2 = 4u[(Jx+-Jy)^2-Jz^2] exact; Sturm root count of q in (-1,1) at 600 random rational couplings "
      f"{cnt} vs table (triangle: exactly one root c_- for every kappa; Jz>Jx+Jy: two iff 4k^2>JxJy and d^2>0; Jz<|Jx-Jy|: none): {bad4} mismatches")

# ------------------------------------------------------------------------------------------------ 5 exact charge
X = [mm(Pt2, Nr[j]) for j in range(3)]
Yy = mm(X[0], X[1])
Rr = ZERO
for r in range(4):
    for q_ in range(4):
        if Yy[r][q_] != ZERO and X[2][q_][r] != ZERO:
            Rr = add(Rr, mul(Yy[r][q_], X[2][q_][r]))
A_ = Rr[0].as_expr(); B_ = Rr[1].as_expr()                 # 8 R = A + B z
delta = P - 4 * u * c
sinth = sp.Symbol("sinth")
a_coeff = -2 ** 15 * Jz ** 3 * k * delta * Fc
T_expr = -(2 * sp.pi) ** 3 * a_coeff * sinth / (16 * Jz ** 2) ** 3
T_claim = -32 * sp.pi ** 3 * k * sp.diff(qc, c) * Fc * sinth / Jz ** 3
dd = sp.Symbol("dd", positive=True)
cm = (P - dd) / (4 * u); cp_ = (P + dd) / (4 * u)
qprime_ok = sp.simplify(sp.diff(qc, c).subs(c, cm) + 2 * dd) == 0 and sp.simplify(sp.diff(qc, c).subs(c, cp_) - 2 * dd) == 0
ok5 = zero_mod_q(A_ + c * B_) and zero_mod_q(B_ + 2 ** 18 * Jz ** 3 * k * delta * Fc) and sp.simplify(T_expr - T_claim) == 0 and qprime_ok
check("5 exact charge", ok5, "Tr(Pt N1 Pt N2 Pt N3) = a(z-c), a = -2^15 Jz^3 k (P-4uc) F_c(c) mod q; T = Im Tr(P d1H P d2H P d3H) = -32 pi^3 k q'(c) F_c(c) sin(2 pi x)/Jz^3 "
      "= +64 pi^3 k d F_c(c_-) sin/Jz^3 (q' = -2d) and -64 pi^3 k d F_c(c_+) sin/Jz^3 (q' = +2d); partner node (1-x,x,0) opposite")

# ------------------------------------------------------------------------------------------------ 6 isotropic reduction (landed chiral_exact.py formula)
mp.mp.dps = 50


def T_ours(J, kap):
    jx = jy = mp.mpf(1); jz = mp.mpf(J); kk = mp.mpf(kap)
    P_ = jx * jy; S_ = jx**2 + jy**2 - jz**2; u_ = kk * kk
    d = mp.sqrt(P_**2 + 4 * u_ * (4 * u_ + S_)); cc = (P_ - d) / (4 * u_)
    Fcv = jx*jy*(jx+jy+jz)*cc*cc + (jx+jy)*(jx**2+jx*jz+jy**2+jy*jz)*cc + (jx+jz)*(jy+jz)*(jx+jy-jz)
    return 64 * mp.pi**3 * kk * d * Fcv * mp.sqrt(1 - cc * cc) / jz**3, Fcv


def T_landed(J, kap):
    J = mp.mpf(J); kk = mp.mpf(kap); u_ = kk * kk
    d = mp.sqrt(1 + 8*u_ + 16*u_*u_ - 4*u_*J*J); cc = (1 - d) / (4 * u_)
    U = 8*J*u_ + J + 8*u_ + 2
    V = 8*J**3*u_**2 + 2*J**3*u_ + 4*J**2*u_ + (-32)*J*u_**2 - 12*J*u_ - J - 32*u_**2 - 16*u_ - 2
    F2 = J*(J+2) - 4*u_*(4 + 2*J - J*J)
    return 32 * mp.pi**3 * kk * d * (J+2) * (4*u_+1) * F2 * mp.sqrt(1 - cc*cc) / (d*U - V), F2


isoF = sp.expand(Fc.subs({Jx: 1, Jy: 1}) - (Jz + 1 + c) * ((Jz + 2) * c + 2 + Jz - Jz ** 2)) == 0
isoroot = sp.simplify(((Jz + 2) * c + 2 + Jz - Jz ** 2).subs(c, (Jz - 2) * (Jz + 1) / (Jz + 2))) == 0
worst = mp.mpf(0); sgn_ok = True
for J, kap in [(1, "0.3"), (1, "0.45"), (1, "0.8"), ("0.5", "0.2"), ("0.5", "0.5"), ("1.5", "0.4"), ("1.5", "0.9"), ("1.9", "0.3"), ("0.2", "0.1")]:
    a, Fcv = T_ours(J, kap); b, F2 = T_landed(J, kap)
    worst = max(worst, abs(a - b) / abs(b)); sgn_ok &= (mp.sign(Fcv) == mp.sign(F2))
check("6 isotropic reduction", isoF and isoroot and worst < mp.mpf(10) ** -35 and sgn_ok, f"F_c(Jx=Jy=1) = (J+1+c)((J+2)c+2+J-J^2), root c = (J-2)(J+1)/(J+2); T(general) = T(landed 32 pi^3 k d (J+2)(4k^2+1)F2 sin/(dU-V)) "
      f"at 9 couplings, max rel diff {mp.nstr(worst, 3)} (50 digits), sign F_c = sign F2")

# ------------------------------------------------------------------------------------------------ 7 sign analysis
cF = sp.Poly(Fc, c).all_coeffs()
c0 = -S / (2 * P)
Fb = S * c + P * (1 + c ** 2)
ucf = lambda cc: -(2 * P * cc + S) / (4 * (1 - cc ** 2))
ok7 = sp.expand(cF[0] - Jx * Jy * (Jx + Jy + Jz)) == 0
ok7 &= sp.expand(Fc.subs(c, -1) + (Jx + Jy) * (Jx - Jy) ** 2 + Jz ** 3) == 0
ok7 &= sp.expand(Fc.subs(c, 1) - (Jx + Jy + Jz) * ((Jx + Jy) ** 2 + Jz * (Jx + Jy) - Jz ** 2)) == 0
ok7 &= sp.simplify(Fc.subs(c, c0) - (Jx + Jy + Jz) * (Jy ** 2 + Jz ** 2 - Jx ** 2) * (Jx ** 2 + Jz ** 2 - Jy ** 2) / (4 * Jx * Jy)) == 0
ok7 &= sp.expand((Jy ** 2 + Jz ** 2 - Jx ** 2) + (Jx ** 2 + Jz ** 2 - Jy ** 2) - 2 * Jz ** 2) == 0
ok7 &= zero_mod_q(Fb - (1 - c ** 2) * (P - 4 * u * c)) and zero_mod_q(S + 2 * P * c + 4 * u * (1 - c ** 2))
ok7 &= sp.simplify(sp.diff(ucf(c), c) + Fb / (2 * (1 - c ** 2) ** 2)) == 0 and sp.simplify(ucf(c) * 4 * (c ** 2 - 1) - (2 * P * c + S)) == 0
# exact-rational flip test: chirality of the x < 1/2 node = sign F_c(c_-) = exact_sign(f0 + f1 d)
rng7 = random.Random(7)
Ks = [Fr(1, 1000)] + [Fr(i, 20) for i in range(1, 81)] + [Fr(1000)]
nflip = nstay = bad7 = ntot = 0
while ntot < 300:
    jx, jy, jz = rng7.choice(vals), rng7.choice(vals), rng7.choice(vals)
    if not (abs(jx - jy) < jz < jx + jy) or abs(jx * jx - jy * jy) == jz * jz:
        continue
    ntot += 1
    sg = [exact_sign(*Fc_over_d(jx, jy, jz, kk, -1)) for kk in Ks]
    changes = sum(1 for i in range(len(sg) - 1) if sg[i] != sg[i + 1])
    flips = abs(jx * jx - jy * jy) < jz * jz
    if flips:
        nflip += 1; bad7 += not (sg[0] == 1 and sg[-1] == -1 and changes == 1)
    else:
        nstay += 1; bad7 += not (all(s == -1 for s in sg))
check("7 sign analysis", ok7 and bad7 == 0, f"F_c lead coeff > 0, F_c(-1) = -(Jx+Jy)(Jx-Jy)^2-Jz^3 < 0, F_c(1) = (Jx+Jy+Jz)((Jx+Jy)^2+Jz(Jx+Jy)-Jz^2), F_c(c0) = (Jx+Jy+Jz)(Jy^2+Jz^2-Jx^2)(Jx^2+Jz^2-Jy^2)/(4JxJy), "
      f"du/dc = -F_b/(2(1-c^2)^2) < 0 at c_- (c_- falls from c0 to -1); exact rational test at 300 triangle couplings x 83 kappa: charge +1 -> -1 exactly once iff |Jx^2-Jy^2| < Jz^2 "
      f"({nflip} flip, {nstay} always -1): {bad7} mismatches")

# ------------------------------------------------------------------------------------------------ 8 independent exact-rational tower grid


class Tower:
    """Tower F < E1 < E2 ...; a level-k element is x0 + x1 g_k, g^2 = r1 g + r0 (kind 'circle': g^2 = p g - 1, conj g -> 1/g; 'real': g^2 = r0)."""

    def __init__(self, F_zero, F_one, F_from_int):
        self.F0, self.F1, self.fi = F_zero, F_one, F_from_int
        self.levels = []

    def add_level(self, kind, p=None, r0=None):
        base = self.levels[-1] if self.levels else None
        tw = self
        R1, R0 = (p, -1) if kind == "circle" else (0, r0)

        class E:
            __slots__ = ("x0", "x1")
            BASE = base
            RR1, RR0 = R1, R0

            def __init__(s, x0, x1):
                s.x0, s.x1 = x0, x1

            @classmethod
            def lift(cls, x):
                if type(x) is cls:
                    return x
                if cls.BASE is None:
                    if isinstance(x, int):
                        x = tw.fi(x)
                    return cls(x, tw.F0)
                return cls(cls.BASE.lift(x), cls.BASE.zero())

            @classmethod
            def zero(cls):
                return cls(cls.BASE.zero() if cls.BASE else tw.F0, cls.BASE.zero() if cls.BASE else tw.F0)

            @classmethod
            def one(cls):
                return cls(cls.BASE.one() if cls.BASE else tw.F1, cls.BASE.zero() if cls.BASE else tw.F0)

            @classmethod
            def gen(cls):
                return cls(cls.BASE.zero() if cls.BASE else tw.F0, cls.BASE.one() if cls.BASE else tw.F1)

            def __add__(s, o):
                o = type(s).lift(o)
                return type(s)(s.x0 + o.x0, s.x1 + o.x1)

            __radd__ = __add__

            def __neg__(s):
                return type(s)(-s.x0, -s.x1)

            def __sub__(s, o):
                o = type(s).lift(o)
                return type(s)(s.x0 - o.x0, s.x1 - o.x1)

            def __rsub__(s, o):
                return type(s).lift(o) - s

            def __mul__(s, o):
                cls = type(s)
                if type(o) is not cls:
                    return cls(s.x0 * o, s.x1 * o)
                a0, a1, b0, b1 = s.x0, s.x1, o.x0, o.x1
                c11 = a1 * b1
                return cls(a0 * b0 + c11 * cls.RR0, a0 * b1 + a1 * b0 + c11 * cls.RR1)

            __rmul__ = __mul__

            def coords(s):
                out = []
                for part in (s.x0, s.x1):
                    out += part.coords() if hasattr(part, "x0") else [part]
                return out

        self.levels.append(E)
        return E


def _powers(g, gi, one):
    out = {}
    for e in range(-2, 3):
        r = one
        for _ in range(abs(e)):
            r = r * (g if e > 0 else gi)
        out[e] = r
    return out


def tower_node(jx, jy, jz, kap, which):
    """Exact check at the root c = (P + which d)/(4u) (which = -1: c_-, +1: c_+); None if |c| >= 1 or d^2 <= 0."""
    jx, jy, jz, kap = map(Fr, (jx, jy, jz, kap))
    u_ = kap * kap; P_ = jx * jy; S_ = jx * jx + jy * jy - jz * jz
    d2 = P_ * P_ + 4 * u_ * (4 * u_ + S_)
    if d2 <= 0:
        return None
    sgn = which
    if not (exact_sign(P_ - 4 * u_, sgn, d2) < 0 and exact_sign(P_ + 4 * u_, sgn, d2) > 0):
        return None
    T1 = Tower(Fr(0), Fr(1), Fr)
    Ed = T1.add_level("real", r0=d2)
    cL = (Ed.lift(P_) + Ed.gen() * sgn) * (1 / (4 * u_))
    Ez = T1.add_level("circle", p=cL * 2)
    zg = Ez.gen(); one = Ez.one(); zi = Ez.lift(cL * 2) - zg
    pw = {"1": _powers(zg, zi, one), "2": _powers(zi, zg, one), "3": _powers(one, one, one)}
    amp = {"x": 2 * jx, "y": 2 * jy, "z": 2 * jz, "odd": 2 * kap}
    zero_el = Ez.zero()
    M = [[zero_el for _ in range(4)] for _ in range(4)]
    N = [[[zero_el for _ in range(4)] for _ in range(4)] for _ in range(3)]
    for (a, b, n, kind) in TERMS:
        t = amp[kind]
        mon = pw["1"][n[0]] * pw["2"][n[1]] * pw["3"][n[2]]
        mon_inv = pw["1"][-n[0]] * pw["2"][-n[1]] * pw["3"][-n[2]]
        M[a][b] = M[a][b] + mon * t
        M[b][a] = M[b][a] - mon_inv * t
        for j in range(3):
            if n[j]:
                N[j][a][b] = N[j][a][b] + mon * (t * n[j])
                N[j][b][a] = N[j][b][a] + mon_inv * (t * n[j])
    mmul = lambda A, B: [[sum((A[r][kk] * B[kk][q_] for kk in range(1, 4)), A[r][0] * B[0][q_]) for q_ in range(4)] for r in range(4)]
    e1 = M[0][0] + M[1][1] + M[2][2] + M[3][3]
    M2_ = mmul(M, M)
    e2 = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    for i in range(4):
        for j in range(i + 1, 4):
            if (i, j) != (0, 1):
                e2 = e2 + (M[i][i] * M[j][j] - M[i][j] * M[j][i])
    Pt = [[M2_[r][q_] - e1 * M[r][q_] + (e2 if r == q_ else 0 * e2) for q_ in range(4)] for r in range(4)]
    X_ = [mmul(Pt, N[j]) for j in range(3)]
    Y_ = mmul(X_[0], X_[1])
    Rt = sum((Y_[r][kk] * X_[2][kk][r] for r in range(4) for kk in range(4)), 0 * e2)
    MPt = mmul(M, Pt); PPt = mmul(Pt, Pt)
    trPt = Pt[0][0] + Pt[1][1] + Pt[2][2] + Pt[3][3]
    ok_a = (all(cc == 0 for cc in e1.coords())
            and all(all(cc == 0 for cc in MPt[r][q_].coords()) for r in range(4) for q_ in range(4))
            and all(all(cc == 0 for cc in (PPt[r][q_] - e2 * Pt[r][q_]).coords()) for r in range(4) for q_ in range(4))
            and all(cc == 0 for cc in (trPt - e2 * 2).coords()))
    e2c = e2.coords()
    ok_b = e2c[0] == 16 * jz * jz and all(cc == 0 for cc in e2c[1:])
    co = Rt.coords()                                        # basis 1, d, z, d z
    a0_, a1_ = co[2], co[3]
    ac0 = (a0_ * P_ + sgn * a1_ * d2) / (4 * u_); ac1 = (a0_ * sgn + a1_ * P_) / (4 * u_)
    ok_const = co[0] == -ac0 and co[1] == -ac1              # R = a (z - c)
    f0, f1, _d2 = Fc_over_d(jx, jy, jz, kap, sgn)
    pre = 2 ** 15 * jz ** 3 * kap * sgn                     # a = -2^15 Jz^3 k (P - 4uc) F_c(c), P - 4uc = -sgn d
    ok_cf = a0_ == pre * f1 * d2 and a1_ == pre * f0
    chir = -exact_sign(a0_, a1_, d2)                        # sign T for sin 2 pi x > 0
    chir_formula = -sgn * exact_sign(f0, f1, d2)
    return ok_a and ok_b and ok_const and ok_cf and chir == chir_formula


rng8 = random.Random(20261001)
vals8 = [Fr(i, 10) for i in range(2, 41)]
kaps8 = [Fr(i, 20) for i in range(1, 81)]
n8 = bad8 = 0; reg8 = {"tri": 0, "big": 0, "small": 0}; nodes8 = 0
t8 = time.time()
while n8 < 2400:
    jx, jy, jz, kk = rng8.choice(vals8), rng8.choice(vals8), rng8.choice(vals8), rng8.choice(kaps8)
    if jz in (jx + jy, abs(jx - jy)):
        continue
    n8 += 1
    reg8["tri" if abs(jx - jy) < jz < jx + jy else ("big" if jz > jx + jy else "small")] += 1
    for wch in (-1, 1):
        res = tower_node(jx, jy, jz, kk, wch)
        if res is None:
            continue
        nodes8 += 1
        bad8 += (not res)
check("8 exact rational grid", bad8 == 0, f"independent exact tower arithmetic over Q, 2400 random rational couplings {reg8}, {nodes8} nodes (both roots): tr M = 0, kernel projector, e2 = 16Jz^2, "
      f"R = a(z-c), a = -2^15 Jz^3 k (P-4uc) F_c(c) coordinate by coordinate, chirality = -sgn sign F_c: {bad8} mismatches [{time.time() - t8:.0f} s]")

# ------------------------------------------------------------------------------------------------ 9 certified nodes A-E at 50 digits
# (J, kappa, f1 of the f1 < 1/2 line node, det V, Fukui C): inlined from the anisotropic certificate (open PR 9419) ('node', 'detV', 'chern_certified'); landed chirality = -C
CERT = [("A", ("1", "0.8", "1"), "0.45", 0.36800378419582996, -124.24499539687461, 1),
        ("B", ("1.2", "0.8", "1"), "0.3", 0.36613976359938505, -53.24708535269137, 1),
        ("C", ("1", "0.8", "1"), "0.8", 0.4112126412273503, -950.2528063915374, 1),
        ("D", ("1.2", "0.8", "1"), "0.2", 0.3552965519929693, 5.5940218692809935, -1),
        ("E", ("0.9", "1.1", "1.3"), "0.4", 0.3207616146589665, 67.30909511735412, -1)]


def mpq(s):
    f = Fr(s)
    return mp.mpf(f.numerator) / f.denominator


def H_dH_mp(jx, jy, jz, kk, f):
    amp = {"x": 2 * jx, "y": 2 * jy, "z": 2 * jz, "odd": 2 * kk}
    M = mp.zeros(4, 4); dM = [mp.zeros(4, 4) for _ in range(3)]
    for (a, b, n, kind) in TERMS:
        t = amp[kind]
        th = 2 * mp.pi * sum(n[j] * f[j] for j in range(3))
        e = mp.expj(th); ec = mp.conj(e)
        M[a, b] += t * e; M[b, a] -= t * ec
        for j in range(3):
            w = 2j * mp.pi * n[j] * t
            dM[j][a, b] += w * e; dM[j][b, a] += w * ec
    return 1j * M, [1j * x for x in dM]


mp.mp.dps = 50
mx_dx = mx_q = mx_lev = mx_cf = mx_log = mp.mpf(0); sign_ok = True; partner_ok = True
for name, J, kap, f1, dv_log, C_log in CERT:
    jx, jy, jz = [mpq(s) for s in J]; kk = mpq(kap)
    P_ = jx * jy; S_ = jx**2 + jy**2 - jz**2; u_ = kk * kk
    d = mp.sqrt(P_**2 + 4 * u_ * (4 * u_ + S_)); cc = (P_ - d) / (4 * u_); xx = mp.acos(cc) / (2 * mp.pi)
    qv = 4 * u_ * cc**2 - 2 * P_ * cc - (4 * u_ + S_)
    Fcv = jx*jy*(jx+jy+jz)*cc**2 + (jx+jy)*(jx**2+jy**2+jz*(jx+jy))*cc + (jx+jz)*(jy+jz)*(jx+jy-jz)
    mx_dx = max(mx_dx, abs(xx - mp.mpf(f1))); mx_q = max(mx_q, abs(qv))
    dets = []
    for node, sgn in (((xx, 1 - xx, mp.mpf(0)), 1), ((1 - xx, xx, mp.mpf(0)), -1)):
        Hm, dH = H_dH_mp(jx, jy, jz, kk, node)
        E, Q = mp.eigh(Hm)
        ev = sorted(mp.re(e) for e in E)
        mx_lev = max(mx_lev, abs(ev[0] + 4 * jz), abs(ev[1]), abs(ev[2]), abs(ev[3] - 4 * jz))
        Pk = mp.zeros(4, 4)
        for i in range(4):
            if abs(mp.re(E[i])) < mp.mpf(10) ** -30:
                col = Q[:, i]
                Pk += col * col.H
        Tm = Pk * dH[0] * Pk * dH[1] * Pk * dH[2]
        T = mp.im(sum(Tm[i, i] for i in range(4)))
        Tcf = 64 * mp.pi**3 * kk * d * Fcv * mp.sin(2 * mp.pi * xx) / jz**3 * sgn
        mx_cf = max(mx_cf, abs(T - Tcf) / abs(T))
        dets.append(T / 2)
    mx_log = max(mx_log, abs(dets[0] - mp.mpf(dv_log)) / abs(dv_log))
    sign_ok &= (int(mp.sign(Fcv)) == -C_log) and (int(mp.sign(dets[0])) == -C_log)
    partner_ok &= (dets[0] * dets[1] < 0)
check("9 certified nodes A-E", mx_dx < 1e-15 and mx_q < mp.mpf(10) ** -45 and mx_lev < mp.mpf(10) ** -45 and mx_cf < mp.mpf(10) ** -45 and mx_log < 1e-11 and sign_ok and partner_ok,
      f"closed-form line nodes vs double-precision certified nodes of the anisotropic certificate (open PR 9419) (A (1,.8,1;.45), B (1.2,.8,1;.3), C (1,.8,1;.8), D (1.2,.8,1;.2), E (.9,1.1,1.3;.4)): max|x-f1| {mp.nstr(mx_dx, 2)}; "
      f"max|q| {mp.nstr(mx_q, 2)}; levels (-4Jz,0,0,4Jz) err {mp.nstr(mx_lev, 2)}; det V closed form vs 50-digit kernel projector rel {mp.nstr(mx_cf, 2)}, vs log det V rel {mp.nstr(mx_log, 2)}; "
      f"chirality sign F_c = sign det V = -C (A,B,C: -1; D,E: +1); partner (1-x,x,0) opposite")

# ------------------------------------------------------------------------------------------------ 10 shear R
Rm = {w3: w1 * w2 / w3}
dif0 = sp.expand(sp.together(a0g.subs(Rm, simultaneous=True) - a0g))
dif2 = sp.expand(sp.together(a2g.subs(Rm, simultaneous=True) - a2g))
n0 = sp.numer(sp.together(dif0))
fac = sp.factor_list(n0)[1]
has = lambda expr: any(sp.expand(f_ - expr) == 0 or sp.expand(f_ + expr) == 0 for f_, m_ in fac)
ok10 = has(Jx - Jy) and has(w1 * w2 - 1) and has(w1 * w2 - w3 ** 2) and sp.expand(n0.subs(Jy, Jx)) == 0 and n0 != 0 and dif2 == 0
check("10 shear symmetry", ok10, f"det M(Rf) - det M(f) = (Jx-Jy)(z1z2-1)(z1z2-z3^2)(...) [{len(fac)} factors], zero iff Jx = Jy; the mu^2 coeff is R-invariant for all couplings: "
      "R: f -> (f1,f2,f1+f2-f3) is a spectral symmetry iff Jx = Jy (interpretation only, not asserted: f1+f2 = 2f3 and f1+f2 = 1 are fixed planes of R and SIR in the Jx = Jy group)")

# ================================================================================================ REPORTED (not asserted)
mp.mp.dps = 40


def kc_closed(jx, jy, jz):
    jx, jy, jz = map(mp.mpf, (jx, jy, jz)); s = jx + jy; P_ = jx * jy
    D = 4*jz**4*P_ + 4*jz**3*P_*s + 4*jz**2*P_**2 - 4*jz**2*P_*s**2 + jz**2*s**4 - 8*jz*P_*s**3 + 2*jz*s**5 - 4*P_*s**4 + s**6
    num = (s**2 - 2*P_ - jz**2) * (2*jz**3*P_ - 4*jz*P_*s**2 + jz*s**4 - 4*P_*s**3 + s**5) + (2*jz**2*P_ - jz**2*s**2 - 4*P_*s**2 + s**4) * mp.sqrt(D)
    return num / (-8 * (s**2 + jz*s - jz**2) * (jz**3 - 4*P_*s + s**3))


def kc_direct(jx, jy, jz):
    jx, jy, jz = map(mp.mpf, (jx, jy, jz)); P_ = jx * jy; S_ = jx**2 + jy**2 - jz**2
    a2_, a1_, a0_ = jx*jy*(jx+jy+jz), (jx+jy)*(jx**2+jy**2+jz*(jx+jy)), (jx+jz)*(jy+jz)*(jx+jy-jz)
    cf = (-a1_ + mp.sqrt(a1_**2 - 4*a2_*a0_)) / (2*a2_)
    return -(2*P_*cf + S_) / (4*(1 - cf**2))


jl = [("1", "0.8", "1"), ("1.2", "0.8", "1"), ("0.9", "1.1", "1.3"), ("1", "1", "1"), ("1", "1", "1.9"), ("2", "1", "2.5")]
mxd = max(abs(kc_closed(*[mpq(s) for s in j]) - kc_direct(*[mpq(s) for s in j])) for j in jl)
kcs = [mp.sqrt(kc_closed(*[mpq(s) for s in j])) for j in jl[:4]]
reported("kappa_c closed form", f"kappa_c^2 = [(s^2-2P-Jz^2)(2Jz^3P-4JzPs^2+Jzs^4-4Ps^3+s^5) + (2Jz^2P-Jz^2s^2-4Ps^2+s^4) sqrt(Delta_F)]/(-8(s^2+Jzs-Jz^2)(Jz^3-4Ps+s^3)), s=Jx+Jy, P=JxJy; "
         f"sympy-rationalised, numerically verified only (6 couplings, max diff vs direct u(c_F) {mp.nstr(mxd, 2)}): kappa_c = {mp.nstr(kcs[0], 12)} (1,.8,1), {mp.nstr(kcs[1], 12)} (1.2,.8,1), "
         f"{mp.nstr(kcs[2], 12)} (.9,1.1,1.3), {mp.nstr(kcs[3], 12)} (1,1,1, = sqrt(.15))")

# PSLQ quintic of the off-plane node, case B = (6/5, 4/5, 1), kappa = 3/10: Newton at 100 digits on grad det H = 0 from the double-precision node, then the identified polynomials
mp.mp.dps = 100
Gs = a0g.subs({Jx: sp.Rational(6, 5), Jy: sp.Rational(4, 5), Jz: 1, k: sp.Rational(3, 10)})
Dop = lambda F, w: sp.I * w * sp.diff(F, w)
ws = (w1, w2, w3)
grad = [Dop(Gs, w) for w in ws]
hess = [[Dop(grad[i], ws[j]) for j in range(3)] for i in range(3)]
fgr = sp.lambdify(ws, grad, modules="mpmath"); fhs = sp.lambdify(ws, hess, modules="mpmath"); fG = sp.lambdify(ws, Gs, modules="mpmath")
th = [2 * mp.pi * mp.mpf(v) for v in ("0.2550569293", "0.5899470504", "0.0426385692")]
for _ in range(9):
    wv = [mp.expj(t_) for t_ in th]
    g_ = mp.matrix([mp.re(v) for v in fgr(*wv)]); hv = fhs(*wv)
    H_ = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            H_[i, j] = mp.re(hv[i][j])
    dx = mp.lu_solve(H_, -g_)
    th = [th[i] + dx[i] for i in range(3)]
wv = [mp.expj(t_) for t_ in th]
g_ = mp.matrix([mp.re(v) for v in fgr(*wv)])
cs = [mp.cos(t_) for t_ in th]
quint = [864, 816, -166396, 837889, 205720, -829767]
rel1 = [(17489565975255, [26747013724932, -14260388057896, 2346373866944, 185878944384, -21181786848], cs[0] + cs[1]),
        (577155677183415, [-769343194123413, 843597637422044, -52872244231616, -12053297478876, 382658742432], cs[0] * cs[1])]
res_q = abs(mp.polyval(quint, cs[2]))
res_r = [abs(lead * v + sum(a_ * cs[2] ** j for j, a_ in enumerate(coef))) for lead, coef, v in rel1]
reported("off-plane quintic (PSLQ identification, NOT a proof)", f"B = (6/5,4/5,1), kappa 3/10: node f = ({mp.nstr(th[0] / (2 * mp.pi), 12)}, {mp.nstr(th[1] / (2 * mp.pi), 12)}, {mp.nstr(th[2] / (2 * mp.pi), 12)}), "
         f"|grad det H| {mp.nstr(mp.norm(g_), 2)}; cos 2 pi f3 = {mp.nstr(cs[2], 15)} root of 864c^5+816c^4-166396c^3+837889c^2+205720c-829767 (residual {mp.nstr(res_q, 2)} at 100 digits); "
         f"c1+c2 and c1c2 are rational polynomials of degree 4 in c3 (relation residuals {mp.nstr(res_r[0], 2)}, {mp.nstr(res_r[1], 2)}); same pattern (quintic for c3) found at 3 other couplings, see the identification logs")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}   ({time.time() - T0:.0f} s)")

# A failed decisive check must fail the bounded execution.
if __name__ == "__main__":
    raise SystemExit(int(not all(RESULTS)))
