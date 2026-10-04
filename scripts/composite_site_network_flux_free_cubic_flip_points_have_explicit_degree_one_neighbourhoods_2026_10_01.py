#!/usr/bin/env python3
"""Cubic points of the supplied composite-network comparator: rigorous local statements with explicit weighted neighbourhoods.

Supplied model, not an axiom of the framework.  H(f) = i M(f), four-site Bloch matrix (landed network rules rebuilt below), J_x = J_y = 1, J_z = J,
odd term kappa, theta = 2 pi f = (x0 + x)(1,-1,0) + y (1,1,0) + z (0,0,1).  Two cases, each at the node of the line family (x0, -x0, 0), both signs of x0:
  (i)  J = 1,   kappa^2 = 3/20  (triangle-regime cubic point, kappa_c),    e^{i x0} = (-2 + i sqrt5)/3
  (ii) J = 5/2, kappa^2 = 45/44 (flipping node of region (b), kappa_f),    e^{i x0} = (7 + 5 i sqrt11)/18.
Exact arithmetic is done in the multiquadratic field K = Q(i, sqrt p, sqrt q) ((p,q) = (3,5) resp. (5,11)); the node, kappa and e^{i x0} lie in K, so the expansion point is
EXACT (no rational approximation of the node).  Square roots used for magnitudes are enclosed by rationals rounded outward; every proof inequality is a python-Fraction comparison.
FLOAT blocks are consistency diagnostics and carry the tag FLOAT.

Method (gamrem style).  At the node H0 = H(theta0) has spectrum {0,0,+-4J}; P = 1 - H0^2/(16J^2) is the exact kernel projector.  Basis T = [W U] (W = two columns of P, U = two columns of 1-P,
exact in K), blocks of T^+ H T, C = U-block, detC = det C, Num = detC * S with S = A - B C^-1 B^+ the E = 0 Schur complement (Laurent polynomials in e^{ix},e^{iy},e^{iz} over K),
Pauli components (Nx, Ny, Nz, N0), D = N/detC.  Exact Taylor coefficients to total degree 12 + Lagrange remainder |e^{i phi} - T_n(phi)| <= |phi|^{n+1}/(n+1)!.
Coordinates (x', y, z) with x' = x + m z^2 (exact shear, m in K); weights x':3, y:3, z:1; quasi-norm N^6 = x'^2 + y^2 + z^6, ball B_rho = {N <= rho}.
Num = N_lead + G, N_lead = n_x x' + n_y y + n_b z^3 (exact vectors), wt(G) >= 4, wt(N0) >= 5, wt(detC - detC0) >= 2.  Conditions on B_rho:
  (A) K_Delta rho^2 < |detC0|; (B) K_G rho < s (|N_lead| >= s N^3, s^2 = min Gram diagonal, vectors exactly orthogonal); (C) K_0 rho^2 + K_G rho < s.
Consequences: Num vanishes at the node and nowhere else in the ball, deg(D/|D|) = deg(D_lead/|D_lead|) = sign det[n_x,n_y,n_b]/sign(detC0)^3 on every sphere N = r <= rho, det H > 0 and signature (2,2) off the node.
Unfolding kappa = kappa_node + eps (checks U1-U5, UF1-UF2): Num is an exact cubic in eps (interpolated from 4 builds, checked on a 5th).  With X = x + m z^2 + lam eps, Y = y the weight<=3 part (weights X:3, Y:3,
z:1, eps:2) is n_x X + n_y Y + n_b (z^3 - mu eps z), mu = (J+2)/kappa^3.  Writing f = L^-1 Num = (X + g1, Y + g2, phi + g3), phi = z^3 - mu eps z, wt(g_i) >= 4: on Q = {|z| <= zeta, X^2+Y^2 <= zeta^6} the first two
equations are solved by a contraction (X*, Y*)(z, eps); the reduced function h = phi + g3(X*, Y*, z, eps) satisfies |h - phi| <= E m^4, |h' - phi'| <= E' m^3 (m^6 = z^6 + |eps|^3) and its roots are counted by monotone
pieces and sign changes (one root for eps < 0, three for eps > 0, indices from sign h').  All inequalities are rational comparisons; FLOAT blocks cross-check zeros and degrees with numpy.
Prints TOTAL: PASS=N FAIL=M.   CUBREM_VERBOSE=1 prints extra detail lines.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import time
from fractions import Fraction as Fr
from math import comb, factorial, isqrt

import numpy as np

AUDIT_TIMEOUT_SEC = 180
VERBOSE = os.environ.get("CUBREM_VERBOSE") == "1"
RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def vprint(*a):
    if VERBOSE:
        print("   ", *a, flush=True)


# ------------------------------------------------------------------------------------------------ the field K = Q(i, sqrt p, sqrt q)
def make_field(p, q):
    """element = 8 Fractions, basis index bits: 1 -> i, 2 -> sqrt p, 4 -> sqrt q (so index 6 = sqrt(pq), 5 = i sqrt q ...)"""
    g = (-1, p, q)
    FT = [[1] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            f = 1
            for b in range(3):
                if (i >> b) & 1 and (j >> b) & 1:
                    f *= g[b]
            FT[i][j] = f
    zero8 = tuple(Fr(0) for _ in range(8))

    class MQ:
        __slots__ = ("c",)
        P, Q = p, q

        def __init__(self, c):
            self.c = c

        @staticmethod
        def of(x):
            return x if isinstance(x, MQ) else MQ((Fr(x),) + zero8[1:])

        @staticmethod
        def basis(idx, val=1):
            c = [Fr(0)] * 8
            c[idx] = Fr(val)
            return MQ(tuple(c))

        def __add__(s, o):
            o = MQ.of(o)
            return MQ(tuple(a + b for a, b in zip(s.c, o.c)))
        __radd__ = __add__

        def __neg__(s):
            return MQ(tuple(-a for a in s.c))

        def __sub__(s, o):
            o = MQ.of(o)
            return MQ(tuple(a - b for a, b in zip(s.c, o.c)))

        def __rsub__(s, o):
            return MQ.of(o) - s

        def __mul__(s, o):
            if not isinstance(o, MQ):
                o = Fr(o)
                return MQ(tuple(a * o for a in s.c))
            r = [Fr(0)] * 8
            oc = o.c
            nzo = [j for j in range(8) if oc[j] != 0]
            for i in range(8):
                ai = s.c[i]
                if ai != 0:
                    for j in nzo:
                        r[i ^ j] += FT[i][j] * ai * oc[j]
            return MQ(tuple(r))
        __rmul__ = __mul__

        def cconj(s):
            return MQ(tuple(-a if (i & 1) else a for i, a in enumerate(s.c)))

        def sig(s, b):
            return MQ(tuple(-a if ((i >> b) & 1) else a for i, a in enumerate(s.c)))

        def is_zero(s):
            return all(a == 0 for a in s.c)

        def inv(s):
            y = s
            phi = MQ.of(1)
            for b in range(3):
                f = y.sig(b)
                phi = phi * f
                y = y * f
            assert all(y.c[i] == 0 for i in range(1, 8)) and y.c[0] != 0, "zero divisor"
            return phi * (1 / y.c[0])

        def __truediv__(s, o):
            return s * o.inv() if isinstance(o, MQ) else s * (1 / Fr(o))

        def __pow__(s, e):
            if e < 0:
                return s.inv() ** (-e)
            r, b_ = MQ.of(1), s
            while e:
                if e & 1:
                    r = r * b_
                b_ = b_ * b_
                e >>= 1
            return r

        def __eq__(s, o):
            return (s - MQ.of(o)).is_zero()

        def __hash__(s):
            return hash(s.c)

        def im_is_zero(s):
            return all(s.c[i] == 0 for i in range(8) if i & 1)

        def mulI(s):
            r = [Fr(0)] * 8
            for i, a in enumerate(s.c):
                if a != 0:
                    if i & 1:
                        r[i ^ 1] += -a
                    else:
                        r[i | 1] += a
            return MQ(tuple(r))

        def __repr__(s):
            names = ["1", "i", "rp", "i*rp", "rq", "i*rq", "rp*rq", "i*rp*rq"]
            return "+".join(f"({a})*{names[i]}" for i, a in enumerate(s.c) if a != 0) or "0"

    MQ.ZERO = MQ.of(0)
    MQ.ONE = MQ.of(1)
    MQ.I = MQ.basis(1)
    return MQ


# ------------------------------------------------------------------------------------------------ network terms (landed rules, rebuilt)
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


def reduce(p):
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)


def terms_tagged():
    out = []
    for p in REPS:
        a, n0 = reduce(p)
        assert n0 == (0, 0, 0) and is_site(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce(q)
                out.append((a, b, n, flavour(p, q)))
        nb = {flavour(p, q): q for q in neighbours(p)}
        assert len(nb) == 3
        for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
            r1, n1 = reduce(nb[l])
            r2, n2 = reduce(nb[m])
            out.append((r1, r2, tuple(int(v) for v in np.subtract(n2, n1)), "odd"))
    return out


TERMS = terms_tagged()
assert len(TERMS) == 18


# ------------------------------------------------------------------------------------------------ Laurent polynomials over K: {(a,b,c): K}
def lp_add(a, b):
    r = dict(a)
    for k, v in b.items():
        if k in r:
            w = r[k] + v
            if w.is_zero():
                del r[k]
            else:
                r[k] = w
        else:
            r[k] = v
    return r


def lp_neg(a):
    return {k: -v for k, v in a.items()}


def lp_sub(a, b):
    return lp_add(a, lp_neg(b))


def lp_scale(a, s):
    r = {}
    for k, v in a.items():
        w = v * s
        if not w.is_zero():
            r[k] = w
    return r


def lp_mul(a, b):
    r = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            key = (k1[0] + k2[0], k1[1] + k2[1], k1[2] + k2[2])
            w = v1 * v2
            r[key] = r[key] + w if key in r else w
    return {k: v for k, v in r.items() if not v.is_zero()}


def build_H(F, J, kappa, z0):
    """H(node + xi) as an LP matrix in e^{i xi}; the term of H(theta) with phase e^{i n.theta} gets the node factor z0^(n0-n1) (shift in the x variable)"""
    z0i = z0.cconj()
    zp = {e: (z0 ** e if e >= 0 else z0i ** (-e)) for e in range(-12, 13)}
    AMP = {"x": F.of(2), "y": F.of(2), "z": F.of(2) * F.of(J), "odd": kappa * 2}
    Hm = [[{} for _ in range(4)] for _ in range(4)]
    for (a, b, n, kind) in TERMS:
        t = AMP[kind]
        fr = (n[0] - n[1], n[0] + n[1], n[2])
        Hm[a][b] = lp_add(Hm[a][b], {fr: F.I * t * zp[fr[0]]})
        Hm[b][a] = lp_add(Hm[b][a], {(-fr[0], -fr[1], -fr[2]): -(F.I * t * zp[-fr[0]])})
    return Hm


def mat_of(Hm, F):
    out = [[F.ZERO] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            s = F.ZERO
            for v in Hm[i][j].values():
                s = s + v
            out[i][j] = s
    return out


def mmul(A, B, F):
    n, m, k = len(A), len(B[0]), len(B)
    out = [[F.ZERO] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            s = F.ZERO
            for l in range(k):
                s = s + A[i][l] * B[l][j]
            out[i][j] = s
    return out


def mzero(A):
    return all(x.is_zero() for r in A for x in r)


def perm_sign(p):
    s_ = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]:
                s_ = -s_
    return s_


def det4(M, F):
    s = F.ZERO
    for p_ in itertools.permutations(range(4)):
        t = F.of(perm_sign(p_))
        for i in range(4):
            t = t * M[i][p_[i]]
        s = s + t
    return s


def basis_T(F, J, Hm):
    """exact kernel projector P = 1 - H0^2/(16J^2) and the first column choice with det T != 0, T = [P e_a, P e_b, (1-P) e_c, (1-P) e_d]"""
    H0 = mat_of(Hm, F)
    H2 = mmul(H0, H0, F)
    P = [[(F.ONE if i == j else F.ZERO) - H2[i][j] * (1 / (16 * J * J)) for j in range(4)] for i in range(4)]
    Q = [[(F.ONE if i == j else F.ZERO) - P[i][j] for j in range(4)] for i in range(4)]
    for wc in itertools.combinations(range(4), 2):
        for uc in itertools.combinations(range(4), 2):
            T = [[P[r][wc[0]], P[r][wc[1]], Q[r][uc[0]], Q[r][uc[1]]] for r in range(4)]
            dT = det4(T, F)
            if not dT.is_zero():
                return T, dT, P, H0, H2, (wc, uc)
    raise AssertionError("no admissible basis")


def lp_block(Hm, T, rows, cols):
    """(T^+ H T)[rows x cols] as an LP matrix"""
    out = [[{} for _ in cols] for _ in rows]
    for ri, a in enumerate(rows):
        for ci, b in enumerate(cols):
            acc = {}
            for p in range(4):
                for q in range(4):
                    if not Hm[p][q]:
                        continue
                    co = T[p][a].cconj() * T[q][b]
                    if not co.is_zero():
                        acc = lp_add(acc, lp_scale(Hm[p][q], co))
            out[ri][ci] = acc
    return out


def build_num(F, Hm, T):
    A = lp_block(Hm, T, (0, 1), (0, 1))
    B = lp_block(Hm, T, (0, 1), (2, 3))
    Bd = lp_block(Hm, T, (2, 3), (0, 1))
    C = lp_block(Hm, T, (2, 3), (2, 3))
    detC = lp_sub(lp_mul(C[0][0], C[1][1]), lp_mul(C[0][1], C[1][0]))
    adj = [[C[1][1], lp_neg(C[0][1])], [lp_neg(C[1][0]), C[0][0]]]

    def mm(X, Y):
        return [[lp_add(lp_mul(X[i][0], Y[0][j]), lp_mul(X[i][1], Y[1][j])) for j in range(2)] for i in range(2)]

    BaB = mm(mm(B, adj), Bd)
    Nm = [[lp_sub(lp_mul(detC, A[i][j]), BaB[i][j]) for j in range(2)] for i in range(2)]
    half = F.of(Fr(1, 2))
    hI = F.I * half

    def comb_(pairs):
        out = {}
        for l, c in pairs:
            out = lp_add(out, lp_scale(l, c))
        return out

    Nx = comb_([(Nm[0][1], half), (Nm[1][0], half)])
    Ny = comb_([(Nm[0][1], hI), (Nm[1][0], -hI)])
    Nz = comb_([(Nm[0][0], half), (Nm[1][1], -half)])
    N0 = comb_([(Nm[0][0], half), (Nm[1][1], half)])
    detH = {}
    for p_ in itertools.permutations(range(4)):
        term = {(0, 0, 0): F.of(perm_sign(p_))}
        for i in range(4):
            term = lp_mul(term, Hm[i][p_[i]])
            if not term:
                break
        detH = lp_add(detH, term)
    dN = lp_sub(lp_mul(Nm[0][0], Nm[1][1]), lp_mul(Nm[0][1], Nm[1][0]))
    return dict(Nx=Nx, Ny=Ny, Nz=Nz, N0=N0, detC=detC, detH=detH, dN=dN)


NT = 12


def taylor(lp, F, n=NT):
    """exact Taylor coefficients (total degree <= n) at 0 of the real-analytic function sum_nu c_nu e^{i nu.(x,y,z)}; coefficients must be real"""
    items = [(k, v.c) for k, v in lp.items()]
    out = {}
    for p in range(n + 1):
        for q in range(n + 1 - p):
            for r in range(n + 1 - p - q):
                S = [Fr(0)] * 8
                for (a, b, c), comp in items:
                    w = (a ** p) * (b ** q) * (c ** r)
                    if w:
                        for k in range(8):
                            if comp[k] != 0:
                                S[k] += comp[k] * w
                if all(x == 0 for x in S):
                    continue
                e = F(tuple(S))
                for _ in range((p + q + r) % 4):
                    e = e.mulI()
                e = e * Fr(1, factorial(p) * factorial(q) * factorial(r))
                assert e.im_is_zero(), "non-real Taylor coefficient"
                out[(p, q, r)] = e
    return out


# ------------------------------------------------------------------------------------------------ the two cases (closed forms of the landed birth / flip reports)
#   A = 4 + 2J - J^2, omega = i sqrt(A), Y = sqrt(J(J+2)A);  kappa = Y/(2A),  e^{i x0} = (J + omega)^2/(2(J+2));  generators: sqrt A = (idx 4) * a, Y = (idx 6) * y
CASES = {"i": dict(J=Fr(1), p=3, q=5, sqA=(4, Fr(1)), Y=(6, Fr(1)), k2=Fr(3, 20)),
         "ii": dict(J=Fr(5, 2), p=5, q=11, sqA=(4, Fr(1, 2)), Y=(6, Fr(3, 4)), k2=Fr(45, 44))}

# ------------------------------------------------------------------------------------------------ rational enclosures of square roots (outward rounding)
DIG = 40


def sqrt_enc(n):
    n = Fr(n)
    S = 10 ** DIG
    lo = isqrt(n.numerator * S * S // n.denominator)
    return Fr(lo, S), Fr(lo + 1, S)


def up_sqrt(fr):
    fr = Fr(fr)
    S = 10 ** DIG
    return Fr(isqrt(fr.numerator * S * S // fr.denominator) + 1, S)


def lo_sqrt(fr):
    fr = Fr(fr)
    return Fr(0) if fr <= 0 else sqrt_enc(fr)[0]


def ru(x, d=30):
    """round a nonnegative rational UP to d decimal digits"""
    x = Fr(x)
    S = 10 ** d
    return Fr(-((-x.numerator * S) // x.denominator), S)


KEYS = ("algebra", "line", "kernel", "laurent_identity", "shear_parallel", "const_linear", "weights", "orthogonal", "det_route", "landed_forms")


class Node:
    """one expansion node: exact data, Taylor structure, shear, bounds"""

    def __init__(self, which, sgn):
        cd = CASES[which]
        self.which, self.sgn = which, sgn
        self.name = f"{which}{'+' if sgn > 0 else '-'}"
        J = cd["J"]
        self.J = J
        F = make_field(cd["p"], cd["q"])
        self.F = F
        self.A = 4 + 2 * J - J * J
        self.sqA = F.basis(*cd["sqA"])
        self.Yv = F.basis(*cd["Y"])
        self.omega = F.I * self.sqA
        self.kappa = self.Yv * (1 / (2 * self.A))
        z0 = (F.of(J) + self.omega) ** 2 * (1 / (2 * (J + 2)))
        self.z0 = z0 if sgn > 0 else z0.cconj()
        rp, rq = sqrt_enc(F.P), sqrt_enc(F.Q)
        self.rp_iv, self.rq_iv = rp, rq
        self.rpq_iv = (rp[0] * rq[0], rp[1] * rq[1])

    # interval helpers
    def real_iv(self, c0, c2, c4, c6):
        lo = hi = Fr(0)
        for co, iv in ((c0, (Fr(1), Fr(1))), (c2, self.rp_iv), (c4, self.rq_iv), (c6, self.rpq_iv)):
            a, b = co * iv[0], co * iv[1]
            lo += min(a, b)
            hi += max(a, b)
        return lo, hi

    def re_iv(self, c):
        assert c.im_is_zero()
        return self.real_iv(c.c[0], c.c[2], c.c[4], c.c[6])

    def abs_ub(self, c):
        a = self.real_iv(c.c[0], c.c[2], c.c[4], c.c[6])
        b = self.real_iv(c.c[1], c.c[3], c.c[5], c.c[7])
        ma, mb = max(abs(a[0]), abs(a[1])), max(abs(b[0]), abs(b[1]))
        if mb == 0:
            return ru(ma)
        if ma == 0:
            return ru(mb)
        return ru(up_sqrt(ma * ma + mb * mb))

    def to_complex(self, c):
        rp, rq = float(self.rp_iv[0]), float(self.rq_iv[0])
        bv = [1, 1j, rp, 1j * rp, rq, 1j * rq, rp * rq, 1j * rp * rq]
        return sum(float(a) * b for a, b in zip(c.c, bv))

    def to_real(self, c):
        return self.to_complex(c).real

    def exact(self):
        try:
            r = self._exact()
            self.failed = None
            return r
        except (AssertionError, KeyError, IndexError, ZeroDivisionError) as e_:      # a violated identity / weight assumption is a failed check, not a crash
            self.failed = repr(e_)
            return {k: False for k in KEYS}

    def _exact(self):
        F, J = self.F, self.J
        self.checks = {}
        z0, kap, A = self.z0, self.kappa, self.A
        c = (z0 + z0.cconj()) * Fr(1, 2)
        k2 = kap * kap
        chk = {}
        chk["algebra"] = (self.sqA * self.sqA == F.of(A)) and (self.Yv * self.Yv == F.of(J * (J + 2) * A)) and (k2 == F.of(CASES[self.which]["k2"])) \
            and (z0 * z0.cconj() == F.ONE) and (k2 == F.of(J * (J + 2) / (4 * A)))
        cF = Fr(J - 2) * (J + 1) / (J + 2)
        chk["line"] = (c == F.of(cF)) and ((k2 * 4 * c * c - c * 2 + (J * J - 2) - k2 * 4).is_zero()) \
            and ((c * c * (J + 2) + c * (4 * (J + 1)) + (J + 1) ** 2 * (2 - J)).is_zero())
        self.Hm = build_H(F, J, kap, z0)
        self.T, self.dT, self.P, H0, H2, self.cols = basis_T(F, J, self.Hm)
        X = [[H2[i][j] - (F.of(16 * J * J) if i == j else F.ZERO) for j in range(4)] for i in range(4)]
        PP = mmul(self.P, self.P, F)
        tr = sum((self.P[i][i] for i in range(4)), F.ZERO)
        chk["kernel"] = mzero([[H0[i][j] - H0[j][i].cconj() for j in range(4)] for i in range(4)]) and mzero(mmul(H2, X, F)) \
            and mzero([[PP[i][j] - self.P[i][j] for j in range(4)] for i in range(4)]) and mzero(mmul(H0, self.P, F)) and tr == F.of(2) and sum((H0[i][i] for i in range(4)), F.ZERO).is_zero()
        self.chk = chk
        self.NL = build_num(F, self.Hm, self.T)
        self.kT = self.dT * self.dT.cconj()
        lhs, rhs = self.NL["dN"], lp_scale(lp_mul(self.NL["detC"], self.NL["detH"]), self.kT)
        chk["laurent_identity"] = not lp_sub(lhs, rhs)
        self.TC = {nm: taylor(self.NL[nm], F) for nm in ("Nx", "Ny", "Nz", "N0", "detC", "detH")}
        Z = F.ZERO
        TC = self.TC

        def vec(key):
            return [TC[nm].get(key, Z) for nm in ("Nx", "Ny", "Nz")]
        vx, vz2 = vec((1, 0, 0)), vec((0, 0, 2))
        idx = [i for i in range(3) if not vx[i].is_zero()][0]
        self.mp = vz2[idx] / vx[idx]                                  # x' = x + m z^2
        chk["shear_parallel"] = all((vz2[i] - vx[i] * self.mp).is_zero() for i in range(3))
        chk["const_linear"] = all((0, 0, 0) not in TC[nm] and (0, 0, 1) not in TC[nm] for nm in ("Nx", "Ny", "Nz", "N0")) and not TC["N0"].get((1, 0, 0)) \
            and not TC["N0"].get((0, 1, 0))
        self.SH = {nm: self.subst(TC[nm]) for nm in ("Nx", "Ny", "Nz", "N0", "detC", "detH")}
        SH = self.SH
        wl = lambda nm: min([wt(k) for k in SH[nm]], default=99)
        chk["weights"] = all(wl(nm) >= 3 for nm in ("Nx", "Ny", "Nz")) and wl("N0") >= 5 \
            and all(wt(k) in (3, 3, 3) and k in ((1, 0, 0), (0, 1, 0), (0, 0, 3)) for nm in ("Nx", "Ny", "Nz") for k in SH[nm] if wt(k) <= 3) \
            and all(wt(k) >= 2 for k in SH["detC"] if k != (0, 0, 0))
        self.lead = {k: [SH[nm].get(k, Z) for nm in ("Nx", "Ny", "Nz")] for k in ((1, 0, 0), (0, 1, 0), (0, 0, 3))}
        nxv, nyv, nbv = self.lead[(1, 0, 0)], self.lead[(0, 1, 0)], self.lead[(0, 0, 3)]
        dot = lambda u, v: sum((a * b for a, b in zip(u, v)), Z)
        self.gram = [[dot(a, b) for b in (nxv, nyv, nbv)] for a in (nxv, nyv, nbv)]
        chk["orthogonal"] = all(self.gram[i][j].is_zero() for i in range(3) for j in range(3) if i != j)
        M3 = [[nxv[i], nyv[i], nbv[i]] for i in range(3)]
        self.det3 = (M3[0][0] * (M3[1][1] * M3[2][2] - M3[1][2] * M3[2][1]) - M3[0][1] * (M3[1][0] * M3[2][2] - M3[1][2] * M3[2][0])
                     + M3[0][2] * (M3[1][0] * M3[2][1] - M3[1][1] * M3[2][0]))
        self.detC0 = TC["detC"][(0, 0, 0)]
        # det route: weights 0..5 of det H vanish, weight-6 part = |N_lead|^2/(kT |detC0|) (the three monomials x'^2, y^2, z^6)
        w6 = {k: v for k, v in SH["detH"].items() if wt(k) <= 6}
        want = {(2, 0, 0): self.gram[0][0], (0, 2, 0): self.gram[1][1], (0, 0, 6): self.gram[2][2]}
        fac = (self.kT * (-self.detC0)).inv()
        chk["det_route"] = all(wt(k) == 6 for k in w6) and set(w6) == set(want) and all((w6[k] - want[k] * fac).is_zero() for k in want)
        # closed forms of the landed birth / flip reports (a^2, b^2, g^2, u2 = W(J+2)/(2N), N = J^3 - 4J - 4)
        Nn = J ** 3 - 4 * J - 4
        Aq = self.A
        a2 = Nn ** 2 / ((J + 2) ** 2 * Aq)
        b2 = 2 * J ** 3 * (J + 1) ** 2 / ((J + 2) ** 2 * Aq)
        g2 = J ** 4 * (J + 2) / (8 * Nn ** 2)
        s = self.kT * (-self.detC0)
        chk["landed_forms"] = (self.gram[0][0] == s * 64 * J * J * a2) and (self.gram[1][1] == s * 64 * J * J * b2) and (self.gram[2][2] == s * 16 * J * J * g2) \
            and (self.mp == self.sqA * Fr(-(J + 2)) / (4 * Nn) * self.sgn)
        return chk

    def subst(self, tc):
        """substitute x = x' - m z^2 into a Taylor polynomial {(p,q,r): c} -> {(i,q,l): c} in (x', y, z)"""
        out = {}
        for (p, q, r), c in tc.items():
            for k in range(p + 1):
                co = c * Fr(comb(p, k)) * ((-self.mp) ** k)
                key = (p - k, q, r + 2 * k)
                out[key] = out[key] + co if key in out else co
        return {k: v for k, v in out.items() if not v.is_zero()}

    # ---------------------------------------------------------------------------------------- bounds
    def prep(self):
        self.mub = ru(max(abs(x) for x in self.re_iv(self.mp)), 12)
        LEAD = {(1, 0, 0), (0, 1, 0), (0, 0, 3)}
        self.polyc, self.lpc = {}, {}
        for nm in ("Nx", "Ny", "Nz", "N0", "detC"):
            items = []
            for k, c in self.SH[nm].items():
                if (nm in ("Nx", "Ny", "Nz") and k in LEAD) or (nm == "detC" and k == (0, 0, 0)):
                    continue
                items.append((wt(k), self.abs_ub(c)))
            self.polyc[nm] = items
            self.lpc[nm] = [(abs(a), abs(b), abs(c_), self.abs_ub(co)) for (a, b, c_), co in self.NL[nm].items()]
        lam = min((self.re_iv(self.gram[i][i])[0] for i in range(3)))
        self.sN = lo_sqrt(lam)
        self.dC0 = -self.re_iv(self.detC0)[1]                      # |detC0| lower bound
        assert self.dC0 > 0

    def K(self, nm, Lw, rho):
        tot = Fr(0)
        for w, ub in self.polyc[nm]:
            assert w >= Lw, (nm, w)
            tot += ub * rho ** (w - Lw)
        rem = Fr(0)
        for a, b, c, ub in self.lpc[nm]:
            base = c + a * self.mub * rho + (a + b) * rho * rho
            rem += ub * base ** (NT + 1)
        rem = rem * rho ** (NT + 1 - Lw) / factorial(NT + 1)
        return tot + rem, tot, rem

    def conds(self, rho):
        Ks = {nm: self.K(nm, Lw, rho) for nm, Lw in (("Nx", 4), ("Ny", 4), ("Nz", 4), ("N0", 5), ("detC", 2))}
        KGn = ru(up_sqrt(sum(Ks[n][0] ** 2 for n in ("Nx", "Ny", "Nz"))))
        A_ = Ks["detC"][0] * rho ** 2 < self.dC0
        B_ = KGn * rho < self.sN
        C_ = Ks["N0"][0] * rho ** 2 + KGn * rho < self.sN
        return A_, B_, C_, Ks, KGn


def wt(key):
    return 3 * key[0] + 3 * key[1] + key[2]


# ================================================================================================ exact checks over the four nodes (+x0, -x0 for cases i, ii)
RHO = {"i": Fr(29, 500), "ii": Fr(69, 1000)}
NODES = [Node(w, s) for w in ("i", "ii") for s in (1, -1)]
CK = {}
for nd in NODES:
    CK[nd.name] = nd.exact()
    if nd.failed is None:
        try:
            nd.prep()
        except (AssertionError, KeyError, IndexError, ZeroDivisionError) as e_:
            nd.failed = "prep: " + repr(e_)
ALLOK = all(nd.failed is None for nd in NODES)
allk = lambda key: all(CK[nd.name][key] for nd in NODES)
if not ALLOK:
    vprint("node failures:", {nd.name: nd.failed for nd in NODES if nd.failed})
check("1: exact node data in K (kappa, e^{i x0}, line + flip equations), H0 Hermitian, H0^2 (H0^2-16J^2) = 0, P = 1 - H0^2/(16J^2) rank-2 kernel projector",
      allk("algebra") and allk("line") and allk("kernel"), "nodes " + " ".join(nd.name for nd in NODES) + "; kappa^2 = 3/20 (i), 45/44 (ii)")
check("2: exact: det T != 0, Laurent identity det Num = |det T|^2 detC detH, detC0 < 0",
      ALLOK and allk("laurent_identity") and all(nd.re_iv(nd.detC0)[1] < 0 for nd in NODES),
      ("detC0 = " + ", ".join(f"{nd.name}: {nd.detC0.c[0]}" for nd in NODES if nd.sgn > 0)) if ALLOK else "exact part failed")
check("3: exact Taylor (deg 12): Num(0)=0, no z-linear term, z^2 coeff = -m (x coeff); with x' = x + m z^2 weights <3 vanish, wt-3 = {x',y,z^3}, wt N0 >= 5, wt(detC-detC0) >= 2",
      ALLOK and allk("shear_parallel") and allk("const_linear") and allk("weights"),
      ("m = " + ", ".join(f"{nd.name}: {nd.mp}" for nd in NODES if nd.sgn > 0)) if ALLOK else "exact part failed")
check("3b: exact det route (4x4 Laurent det H): weights 0-5 vanish, weight 6 = (|n_x|^2 x'^2 + |n_y|^2 y^2 + |n_b|^2 z^6)/(|det T|^2 |detC0|)",
      ALLOK and allk("det_route"))
degs = {}
if ALLOK:
    for nd in NODES:
        sg3 = 1 if nd.re_iv(nd.det3)[0] > 0 else (-1 if nd.re_iv(nd.det3)[1] < 0 else 0)
        sc0 = 1 if nd.re_iv(nd.detC0)[0] > 0 else -1
        degs[nd.name] = sg3 * sc0 ** 3
check("4: exact: n_x,n_y,n_b orthogonal; Gram = landed closed forms (a^2,b^2,g^2), m = -W(J+2)/(4N); deg(D_lead/|D_lead|) = sign det[n]/sign(detC0)^3",
      ALLOK and allk("orthogonal") and allk("landed_forms") and all(degs[nd.name] == nd.sgn for nd in NODES),
      ("degrees " + " ".join(f"{k}:{v:+d}" for k, v in degs.items()) + "; Gram diag (i+) " + ", ".join(str(NODES[0].gram[i][i].c[0]) for i in range(3))
       + "; (ii+) " + ", ".join(str(NODES[2].gram[i][i].c[0]) for i in range(3))) if ALLOK else "exact part failed")
res5 = {}
okA = okB = okC = False
if ALLOK:
    for nd in NODES:
        rho = RHO[nd.which]
        try:
            res5[nd.name] = nd.conds(rho)
        except (AssertionError, KeyError, IndexError, ZeroDivisionError) as e_:
            res5[nd.name] = (False, False, False, None, Fr(0))
            vprint(nd.name, "conds failed:", e_)
            continue
        A_, B_, C_, Ks, KGn = res5[nd.name]
        vprint(nd.name, "rho", rho, "s_N >=", float(nd.sN), "|detC0| =", float(nd.dC0), "K_Gx,y,z =", [float(Ks[n][0]) for n in ("Nx", "Ny", "Nz")], "K_G =", float(KGn),
               "K_N0 =", float(Ks["N0"][0]), "K_Delta =", float(Ks["detC"][0]), "remainder shares", [float(Ks[n][2]) for n in ("Nx", "N0", "detC")])
    okA = all(res5[nd.name][0] for nd in NODES)
    okB = all(res5[nd.name][1] for nd in NODES)
    okC = all(res5[nd.name][2] for nd in NODES)
check("5: exact inequalities on B_rho (rho_i = 29/500, rho_ii = 69/1000): (A) K_D rho^2 < |detC0|, (B) K_G rho < s, (C) K_0 rho^2 + K_G rho < s",
      okA and okB and okC,
      "; ".join(f"{nd.name}: s>={float(nd.sN):.4f} K_G={float(res5[nd.name][4]):.3f} K_0={float(res5[nd.name][3]['N0'][0]):.3f} K_D={float(res5[nd.name][3]['detC'][0]):.3f}"
                for nd in NODES if nd.sgn > 0 and res5.get(nd.name) and res5[nd.name][3]) if ALLOK else "exact part failed")
if ALLOK:
    for nd in NODES:
        if nd.sgn > 0:
            vprint(nd.name, "m =", nd.mp, "| n_x =", nd.lead[(1, 0, 0)], "| n_y =", nd.lead[(0, 1, 0)], "| n_b =", nd.lead[(0, 0, 3)], "| det[n] =", nd.det3, "| detC0 =", nd.detC0, "| |det T|^2 =", nd.kT)
            vprint(nd.name, "Gram diagonal:", [str(nd.gram[i][i]) for i in range(3)], "| s_N >= %.6f, s_D = s_N/|detC0| >= %.6f" % (float(nd.sN), float(nd.sN / nd.dC0)),
                   "| ball extents: |z| <= %.4g, |y| <= %.3g, |x| <= %.3g" % (float(RHO[nd.which]), float(RHO[nd.which] ** 3), float(RHO[nd.which] ** 3 + nd.mub * RHO[nd.which] ** 2)))
RHO_BIG = {"i": Fr(3, 50), "ii": Fr(7, 100)}
ctrl = ALLOK
if ALLOK:
    for nd in NODES:
        try:
            a_, b_, c_, _, _ = nd.conds(RHO_BIG[nd.which])
            ctrl = ctrl and not (a_ and b_ and c_)
        except (AssertionError, KeyError, IndexError, ZeroDivisionError):
            ctrl = False
check("5c: control (non-vacuity): the same inequalities (A),(B),(C) fail at rho = 3/50 (i) and 7/100 (ii)", ctrl)
FLOK = ALLOK and all(res5.get(nd.name) and res5[nd.name][3] is not None for nd in NODES)          # the FLOAT blocks need the exact constants
cons = ALLOK and okA and okB and okC and allk("weights") and allk("orthogonal") and allk("det_route")
check("6: consequence: |N_lead + tG| >= (s - K_G rho) N^3 > 0 (t in [0,1]): Num = 0 at the node and nowhere else, degree +1 at +x0 / -1 at -x0 on every sphere N = r <= rho, det H > 0, signature (2,2) off node",
      cons and all(degs.get(nd.name) == nd.sgn for nd in NODES), "ball N^6 = x'^2 + y^2 + z^6 <= rho^6")


# ================================================================================================ FLOAT diagnostics
def Hnum(xyz, kappa, J, x0):
    x_, y_, z_ = x0 + xyz[:, 0], xyz[:, 1], xyz[:, 2]
    th = np.stack([x_ + y_, -x_ + y_, z_], 1)
    amp = {"x": 2.0, "y": 2.0, "z": 2.0 * J, "odd": 2.0 * kappa}
    M = np.zeros((len(xyz), 4, 4), complex)
    for (a, b, n, kind) in TERMS:
        ph = np.exp(1j * (th @ np.array(n, float)))
        M[:, a, b] += amp[kind] * ph
        M[:, b, a] -= amp[kind] * np.conj(ph)
    return 1j * M


def schur_pauli(H, Wn, Un):
    """E = 0 Schur complement S = A - B C^-1 B^+ for the basis [Wn Un]; returns Pauli vector D, d0, detC, det H"""
    Wd, Ud = np.conj(Wn.T), np.conj(Un.T)
    A = np.einsum("ai,mij,jb->mab", Wd, H, Wn)
    B = np.einsum("ai,mij,jb->mab", Wd, H, Un)
    C = np.einsum("ai,mij,jb->mab", Ud, H, Un)
    S = A - B @ np.linalg.inv(C) @ np.conj(np.transpose(B, (0, 2, 1)))
    d0 = ((S[:, 0, 0] + S[:, 1, 1]) / 2).real
    dz = ((S[:, 0, 0] - S[:, 1, 1]) / 2).real
    dx = ((S[:, 0, 1] + S[:, 1, 0]) / 2).real
    dy = (1j * (S[:, 0, 1] - S[:, 1, 0]) / 2).real
    return np.stack([dx, dy, dz], 1), d0, np.linalg.det(C).real, np.linalg.det(H).real


def lp_eval(lp, nd, xyz):
    keys = np.array(list(lp.keys()), float)
    co = np.array([nd.to_complex(v) for v in lp.values()], complex)
    return (np.exp(1j * (xyz @ keys.T)) @ co).real


def quasi_sphere(rho, mf, m_th, m_ph):
    """points (x, y, z) offsets on N = rho in the (x', y, z) coordinates, x = x' - m z^2 (mf = float m)"""
    th = np.linspace(0, np.pi, m_th + 1)[:, None] * np.ones((1, m_ph + 1))
    ph = np.ones((m_th + 1, 1)) * np.linspace(0, 2 * np.pi, m_ph + 1)[None, :]
    p_, q_, s2 = np.cos(th), np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph)
    z = rho * np.sign(p_) * np.abs(p_) ** (1.0 / 3.0)
    xp, y = rho ** 3 * q_, rho ** 3 * s2
    return np.stack([xp - mf * z ** 2, y, z], -1)


def solid_degree(Fv, m_th, m_ph):
    U = Fv / np.linalg.norm(Fv, axis=-1, keepdims=True)
    a, b, c, d = U[:-1, :-1], U[1:, :-1], U[1:, 1:], U[:-1, 1:]

    def om(p, q, r):
        num = np.einsum("...i,...i", p, np.cross(q, r))
        den = 1 + np.einsum("...i,...i", p, q) + np.einsum("...i,...i", q, r) + np.einsum("...i,...i", r, p)
        return 2 * np.arctan2(num, den)

    tot = om(a, b, c).sum() + om(a, c, d).sum()
    edge = max(np.arccos(np.clip(np.einsum("...i,...i", a, b), -1, 1)).max(), np.arccos(np.clip(np.einsum("...i,...i", a, d), -1, 1)).max())
    return tot / (4 * np.pi), edge


rng = np.random.default_rng(11)
F1dev, F2rat, F2lem, F2N0, F2D, F2mid = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
F3 = {}
F4 = {}
if FLOK:
    try:
        for nd in NODES:
            J = float(nd.J)
            kap = float(nd.to_real(nd.kappa))
            z0c = nd.to_complex(nd.z0)
            x0 = float(np.arctan2(z0c.imag, z0c.real))
            Tn = np.array([[nd.to_complex(nd.T[r][c]) for c in range(4)] for r in range(4)])
            Wn, Un = Tn[:, :2], Tn[:, 2:]
            mf = float(nd.to_real(nd.mp))
            # F1: Laurent objects (K coefficients converted to float) vs direct numpy Schur complement in the same basis
            pts = rng.uniform(-0.3, 0.3, (150, 3))
            Dn, d0n, dCn, dHn = schur_pauli(Hnum(pts, kap, J, x0), Wn, Un)
            dev = max(np.max(np.abs(lp_eval(nd.NL["detC"], nd, pts) - dCn)), np.max(np.abs(lp_eval(nd.NL["detH"], nd, pts) - dHn * float(nd.to_real(nd.kT)) * 0 - dHn)) * 0
                      + np.max(np.abs(lp_eval(nd.NL["detH"], nd, pts) - dHn)),
                      *[np.max(np.abs(lp_eval(nd.NL[nm], nd, pts) - dCn * Dn[:, i])) for i, nm in enumerate(("Nx", "Ny", "Nz"))], np.max(np.abs(lp_eval(nd.NL["N0"], nd, pts) - dCn * d0n)))
            F1dev = max(F1dev, dev)
            # F2: bounds hold at random points of the ball; Taylor remainder bound at large arguments
            rho = RHO[nd.which]
            A_, B_, C_, Ks, KGn = res5[nd.name]
            rf = float(rho)
            ur = rng.uniform(-1, 1, (400, 3))
            ur = ur / np.maximum(1, np.linalg.norm(ur, axis=1, keepdims=True))
            sc = rng.uniform(0.3, 1.0, (400, 1))
            zz = rf * sc[:, 0] * ur[:, 2]
            xp, yy = (rf * sc[:, 0]) ** 3 * ur[:, 0], (rf * sc[:, 0]) ** 3 * ur[:, 1]
            # N^6 = x'^2 + y^2 + z^6 <= (sc rho)^6 * (|u|^2) by construction (|u| <= 1, z^6 = (rho sc)^6 u_z^6 <= .)
            NN = (xp ** 2 + yy ** 2 + zz ** 6) ** (1 / 6)
            pts = np.stack([xp - mf * zz ** 2, yy, zz], 1)
            nxv = [nd.to_real(c) for c in nd.lead[(1, 0, 0)]]
            nyv = [nd.to_real(c) for c in nd.lead[(0, 1, 0)]]
            nbv = [nd.to_real(c) for c in nd.lead[(0, 0, 3)]]
            for i, nm in enumerate(("Nx", "Ny", "Nz")):
                G = lp_eval(nd.NL[nm], nd, pts) - (nxv[i] * xp + nyv[i] * yy + nbv[i] * zz ** 3)
                F2rat = max(F2rat, float(np.max(np.abs(G) / (NN ** 4 * float(Ks[nm][0])))))
            F2N0 = max(F2N0, float(np.max(np.abs(lp_eval(nd.NL["N0"], nd, pts)) / (NN ** 5 * float(Ks["N0"][0])))))
            F2D = max(F2D, float(np.max(np.abs(lp_eval(nd.NL["detC"], nd, pts) - float(nd.to_real(nd.detC0))) / (NN ** 2 * float(Ks["detC"][0])))))
            big = rng.uniform(-0.9, 0.9, (300, 3))
            for nm in ("Nx", "Ny", "Nz", "N0", "detC", "detH"):
                lp = nd.NL[nm]
                Fv = lp_eval(lp, nd, big)
                Tv = np.zeros(len(big))
                for (p, q, r), v in nd.TC[nm].items():
                    Tv += nd.to_real(v) * big[:, 0] ** p * big[:, 1] ** q * big[:, 2] ** r
                keys = np.array(list(lp.keys()), float)
                cm = np.array([float(nd.abs_ub(v)) for v in lp.values()])
                bound = (cm[None, :] * np.abs(big @ keys.T) ** (NT + 1)).sum(1) / factorial(NT + 1)
                F2lem = max(F2lem, float(np.max(np.abs(Fv - Tv) / (bound + 1e-9))))
                mid = rng.uniform(-0.1, 0.1, (200, 3))
                Tm = np.zeros(len(mid))
                for (p, q, r), v in nd.TC[nm].items():
                    Tm += nd.to_real(v) * mid[:, 0] ** p * mid[:, 1] ** q * mid[:, 2] ** r
                F2mid = max(F2mid, float(np.max(np.abs(lp_eval(lp, nd, mid) - Tm))))
            # F3: solid-angle degrees (T basis and unitary kernel basis) on quasi-spheres N = rho and rho/2
            H0n = Hnum(np.zeros((1, 3)), kap, J, x0)[0]
            ev, V = np.linalg.eigh(H0n)
            Wu, Uu = V[:, [1, 2]], V[:, [0, 3]]
            out = []
            for rr in (rf, rf / 2):
                sph = quasi_sphere(rr, mf, 120, 240)
                Hs = Hnum(sph.reshape(-1, 3), kap, J, x0)
                dgT, edT = solid_degree(schur_pauli(Hs, Wn, Un)[0].reshape(sph.shape), 120, 240)
                dgU, edU = solid_degree(schur_pauli(Hs, Wu, Uu)[0].reshape(sph.shape), 120, 240)
                out.append((dgT, dgU, max(edT, edU)))
            F3[nd.name] = (out, float(np.max(np.abs(ev[[1, 2]]))), float(ev[0]), float(ev[3]))
            # F4: sign of Im Tr(P d1H P d2H P d3H) on the axis x' = y = 0 of the ball, z = +-(0.005 ... rho)
            sg = []
            for zv in np.concatenate([np.linspace(0.005, rf, 20), -np.linspace(0.005, rf, 20)]):
                pt = np.array([-mf * zv ** 2, 0.0, zv])
                th = np.array([x0 + pt[0] + pt[1], -(x0 + pt[0]) + pt[1], pt[2]])
                M = np.zeros((4, 4), complex)
                dM = [np.zeros((4, 4), complex) for _ in range(3)]
                amp = {"x": 2.0, "y": 2.0, "z": 2.0 * J, "odd": 2.0 * kap}
                for (a, b, n, kind) in TERMS:
                    ph = np.exp(1j * np.dot(n, th))
                    M[a, b] += amp[kind] * ph
                    M[b, a] -= amp[kind] * np.conj(ph)
                    for l_ in range(3):
                        dM[l_][a, b] += amp[kind] * ph * 1j * n[l_]
                        dM[l_][b, a] -= amp[kind] * np.conj(ph) * (-1j * n[l_])
                evh, Vh = np.linalg.eigh(1j * M)
                Pm = Vh[:, 1:3] @ Vh[:, 1:3].conj().T
                d1, d2, d3 = [1j * d_ for d_ in dM]
                sg.append(np.trace(Pm @ d1 @ Pm @ d2 @ Pm @ d3).imag)
            F4[nd.name] = sg
    except Exception as e_:                                        # a failed diagnostic is a failed check, not a crash
        FLOK = False
        vprint('float block failed:', repr(e_))

check("F1 FLOAT: Laurent objects vs direct numpy Schur complement (same basis), 4 nodes x 150 points", FLOK and F1dev < 1e-9,
      f"max deviation {F1dev:.1e}")
check("F2 FLOAT: |G_i| <= K_i N^4, |N0| <= K_0 N^5, |detC-detC0| <= K_D N^2 at 400 ball points/node; Taylor remainder bound at 300 large-argument points; |F - T12| < 1e-9 at 200 points |xi| <= 0.1",
      FLOK and F2rat < 1 and F2N0 < 1 and F2D < 1 and F2lem < 1 and F2mid < 1e-9, f"max ratios G {F2rat:.2e}, N0 {F2N0:.2e}, detC {F2D:.2e}, remainder {F2lem:.2e}; |F - T12| <= {F2mid:.1e} at |xi| <= 0.1")
okd = FLOK
for nd in (NODES if FLOK else []):
    out, kz, em, ep = F3[nd.name]
    okd = okd and all(abs(dgT - nd.sgn) < 1e-6 and abs(dgU - nd.sgn) < 1e-6 and ed < 1.2 for dgT, dgU, ed in out) and kz < 1e-9
check("F3 FLOAT: solid-angle degree of D/|D| on N = rho, rho/2 (T basis and unitary kernel basis): +1 at +x0, -1 at -x0",
      okd, ("degrees " + " ".join(f"{n}:{F3[n][0][0][0]:+.4f}/{F3[n][0][0][1]:+.4f}" for n in F3)) if FLOK else "exact part failed")
okT = FLOK and all((np.all(np.array(F4[nd.name]) * nd.sgn > 0)) for nd in NODES)
check("F4 FLOAT: sign of Im Tr(P d1H P d2H P d3H) on the axis x' = y = 0, z = +-0.005..+-rho: > 0 at +x0, < 0 at -x0", okT,
      ("min |T| " + " ".join(f"{n}:{np.min(np.abs(F4[n])):.1e}" for n in F4)) if FLOK else "exact part failed")


# ================================================================================================ unfolding in kappa = kappa_node + eps: exact normal form and zero count by reduction
NTU = 8                                  # Taylor degree in (x, y, z) for the unfolded expansion (Lagrange remainder of order 9)
WU = (3, 3, 1, 2)                        # weights of (X, Y, z, eps)


def wt4(k):
    return 3 * k[0] + 3 * k[1] + k[2] + 2 * k[3]


def pmul4(A, B, F):
    r = {}
    for k1, v1 in A.items():
        for k2, v2 in B.items():
            key = (k1[0] + k2[0], k1[1] + k2[1], k1[2] + k2[2], k1[3] + k2[3])
            w = v1 * v2
            r[key] = r[key] + w if key in r else w
    return r


class Unfold:
    """E = 0 Schur complement of the node basis T at kappa = kappa_node + eps (M linear in kappa => Num is a cubic polynomial in eps)"""

    def __init__(self, nd):
        self.nd = nd

    def build(self):
        nd = self.nd
        F, J = nd.F, nd.J
        NUMk = []
        for k in range(4):
            NUMk.append(build_num(F, build_H(F, J, nd.kappa + F.of(k), nd.z0), nd.T))
        Vm = [[Fr(k) ** j for j in range(4)] for k in range(4)]
        n = 4
        A = [row[:] + [Fr(1) if i == j else Fr(0) for j in range(n)] for i, row in enumerate(Vm)]
        for c in range(n):
            piv = [r for r in range(c, n) if A[r][c] != 0][0]
            A[c], A[piv] = A[piv], A[c]
            pv = A[c][c]
            A[c] = [x / pv for x in A[c]]
            for r in range(n):
                if r != c and A[r][c] != 0:
                    f = A[r][c]
                    A[r] = [a - f * b for a, b in zip(A[r], A[c])]
        Vi = [row[n:] for row in A]
        self.NUMj = {}
        for nm in ("Nx", "Ny", "Nz", "N0"):
            for j in range(4):
                acc = {}
                for k in range(4):
                    if Vi[j][k] != 0:
                        acc = lp_add(acc, lp_scale(NUMk[k][nm], F.of(Vi[j][k])))
                self.NUMj[(nm, j)] = acc
        # interpolation sanity: eps = 0 reproduces the node Num, and the cubic reproduces the eps = 3 build
        ok0 = all(not lp_sub(self.NUMj[(nm, 0)], nd.NL[nm]) for nm in ("Nx", "Ny", "Nz", "N0"))
        ok3 = True
        NUM4 = build_num(F, build_H(F, J, nd.kappa + F.of(4), nd.z0), nd.T)           # independent fifth build: the cubic reproduces it
        for nm in ("Nx", "Ny", "Nz", "N0"):
            acc = {}
            for j in range(4):
                acc = lp_add(acc, lp_scale(self.NUMj[(nm, j)], F.of(4 ** j)))
            ok3 = ok3 and not lp_sub(acc, NUM4[nm])
        self.interp_ok = ok0 and ok3
        self.POL = {}
        for nm in ("Nx", "Ny", "Nz", "N0"):
            P = {}
            for j in range(4):
                for (p, q, r), c in taylor(self.NUMj[(nm, j)], F, NTU).items():
                    P[(p, q, r, j)] = c
            self.POL[nm] = P

    def subst(self, P, lam, a1, b1):
        nd = self.nd
        F = nd.F
        xs = {(1, 0, 0, 0): F.ONE, (0, 0, 2, 0): -nd.mp, (0, 0, 0, 1): -lam, (0, 0, 1, 1): -a1}
        ys = {(0, 1, 0, 0): F.ONE, (0, 0, 1, 1): -b1}
        xp, yp = [{(0, 0, 0, 0): F.ONE}], [{(0, 0, 0, 0): F.ONE}]
        for _ in range(NTU):
            xp.append(pmul4(xp[-1], xs, F))
            yp.append(pmul4(yp[-1], ys, F))
        out = {}
        for (p, q, r, j), c in P.items():
            for key, v in pmul4(xp[p], yp[q], F).items():
                key2 = (key[0], key[1], key[2] + r, key[3] + j)
                w = c * v
                out[key2] = out[key2] + w if key2 in out else w
        return {k: v for k, v in out.items() if not v.is_zero()}

    def normal_form(self):
        nd = self.nd
        F = nd.F
        Z = F.ZERO
        self.fail = None
        try:
            nxv, nyv, nbv = nd.lead[(1, 0, 0)], nd.lead[(0, 1, 0)], nd.lead[(0, 0, 3)]
            gx, gy, gb = nd.gram[0][0], nd.gram[1][1], nd.gram[2][2]
            dot = lambda u, v: sum((a * b for a, b in zip(u, v)), Z)
            e_eps = [self.POL[nm].get((0, 0, 0, 1), Z) for nm in ("Nx", "Ny", "Nz")]
            idx = [i for i in range(3) if not nxv[i].is_zero()][0]
            self.lam = e_eps[idx] / nxv[idx]
            par = all((e_eps[i] - nxv[i] * self.lam).is_zero() for i in range(3))
            P1 = {nm: self.subst(self.POL[nm], self.lam, Z, Z) for nm in ("Nx", "Ny", "Nz")}
            w1 = [P1[nm].get((0, 0, 1, 1), Z) for nm in ("Nx", "Ny", "Nz")]
            self.a1, self.b1, ga = dot(w1, nxv) / gx, dot(w1, nyv) / gy, dot(w1, nbv) / gb
            dec = all((w1[i] - nxv[i] * self.a1 - nyv[i] * self.b1 - nbv[i] * ga).is_zero() for i in range(3))
            self.mu = -ga
            self.PT = {nm: self.subst(self.POL[nm], self.lam, self.a1, self.b1) for nm in ("Nx", "Ny", "Nz", "N0")}
            # G = PT - lead, lead = n_x X + n_y Y + n_b (z^3 - mu eps z)
            self.G = {}
            ok_w = True
            for ci, nm in enumerate(("Nx", "Ny", "Nz")):
                G = dict(self.PT[nm])
                for key, v in (((1, 0, 0, 0), nxv[ci]), ((0, 1, 0, 0), nyv[ci]), ((0, 0, 3, 0), nbv[ci]), ((0, 0, 1, 1), -self.mu * nbv[ci])):
                    w_ = G.get(key, Z) - v
                    if w_.is_zero():
                        G.pop(key, None)
                    else:
                        G[key] = w_
                ok_w = ok_w and all(wt4(k) >= 4 for k in G)
                self.G[nm] = G
            ok_w = ok_w and all(wt4(k) >= 4 for k in self.PT["N0"])
            kap = nd.kappa
            mu_ok = (self.mu == (kap ** 3).inv() * (nd.J + 2)) and (self.mu == nd.Yv * nd.A * 8 / (nd.J * nd.J * (nd.J + 2)))
            self.chk = dict(interp=self.interp_ok, parallel=par, decomp=dec, weights=ok_w, mu=mu_ok, mupos=nd.re_iv(self.mu)[0] > 0)
        except (AssertionError, KeyError, IndexError, ZeroDivisionError) as e_:
            self.fail = repr(e_)
            self.chk = dict(interp=False, parallel=False, decomp=False, weights=False, mu=False, mupos=False)
        return self.chk

    # ---------------------------------------------------------------------------------------- bounds for the reduction
    def prep_bounds(self):
        nd = self.nd
        F = nd.F
        Z = F.ZERO
        comps = ("Nx", "Ny", "Nz")
        nvec = [nd.lead[(1, 0, 0)], nd.lead[(0, 1, 0)], nd.lead[(0, 0, 3)]]
        gram = [nd.gram[0][0], nd.gram[1][1], nd.gram[2][2]]
        ginv = [g_.inv() for g_ in gram]
        self.nlow = [lo_sqrt(nd.re_iv(g_)[0]) for g_ in gram]               # lower bounds of |n_x|, |n_y|, |n_b|
        self.gpoly = []                                                      # g_i = n_i . G / |n_i|^2
        for i in range(3):
            acc = {}
            for ci, nm in enumerate(comps):
                f = nvec[i][ci] * ginv[i]
                if f.is_zero():
                    continue
                for key, v in self.G[nm].items():
                    w_ = v * f
                    acc[key] = acc[key] + w_ if key in acc else w_
            self.gpoly.append([(key, wt4(key), nd.abs_ub(v)) for key, v in acc.items() if not v.is_zero()])
        # remainder data per component
        self.mub_ = ru(max(abs(x) for x in nd.re_iv(nd.mp)), 12)
        self.lamub = ru(max(abs(x) for x in nd.re_iv(self.lam)), 12)
        self.a1ub = ru(max(abs(x) for x in nd.re_iv(self.a1)), 12)
        self.b1ub = ru(max(abs(x) for x in nd.re_iv(self.b1)), 12)
        self.rem = {nm: [(j, abs(a), abs(b), abs(c), nd.abs_ub(co)) for j in range(4) for (a, b, c), co in self.NUMj[(nm, j)].items()] for nm in comps}
        self.muiv = nd.re_iv(self.mu)

    def consts(self, rho):
        n = NTU
        out = {}
        rem = {}
        for nm, lst in self.rem.items():
            sv = sX = sY = sz = Fr(0)
            for j, a, b, c, u in lst:
                B = c + a * ((self.mub_ + self.lamub) * rho + (1 + self.a1ub) * rho * rho) + b * (1 + self.b1ub) * rho * rho
                D = c + a * (2 * self.mub_ * rho + self.a1ub * rho * rho) + b * self.b1ub * rho * rho
                sv += u * B ** (n + 1) / factorial(n + 1) * rho ** (2 * j + n - 3)
                sX += u * a * B ** n / factorial(n) * rho ** (2 * j + n - 1)
                sY += u * b * B ** n / factorial(n) * rho ** (2 * j + n - 1)
                sz += u * D * B ** n / factorial(n) * rho ** (2 * j + n - 3)
            rem[nm] = (sv, sX, sY, sz)
        for i in range(3):
            pv = pX = pY = pz = Fr(0)
            for key, w, ub in self.gpoly[i]:
                assert w >= 4
                f = ub * rho ** (w - 4)
                pv += f
                pX += key[0] * f
                pY += key[1] * f
                pz += key[2] * f
            r4 = [up_sqrt(sum(rem[nm][t] ** 2 for nm in rem)) / self.nlow[i] for t in range(4)]
            out[i] = tuple(ru(x + y) for x, y in zip((pv, pX, pY, pz), r4))
        return out          # out[i] = (K_val, K_X, K_Y, K_z) for g_i, valid for M <= rho: |g| <= K_val M^4, |d_X g| <= K_X M, |d_Y g| <= K_Y M, |d_z g| <= K_z M^3

    def reduction(self, zeta):
        """constants of the reduction on Q = {|z| <= zeta, X^2 + Y^2 <= zeta^6}, M <= rho = 6 zeta/5"""
        rho = Fr(6, 5) * zeta
        c = self.consts(rho)
        K12 = ru(up_sqrt(c[0][0] ** 2 + c[1][0] ** 2))
        q1 = ru(up_sqrt(c[0][1] ** 2 + c[0][2] ** 2 + c[1][1] ** 2 + c[1][2] ** 2) * rho)
        K12z = ru(up_sqrt(c[0][3] ** 2 + c[1][3] ** 2))
        K3XY = ru(up_sqrt(c[2][1] ** 2 + c[2][2] ** 2))
        u = K12 ** 2 * rho ** 2
        ok = q1 <= Fr(1, 2) and K12 * rho ** 4 <= zeta ** 3 and u < Fr(1, 2)
        cM = ru(1 / (1 - u)) if u < 1 else Fr(10 ** 9)
        E = ru(c[2][0] * cM ** 4)
        Ep = ru((c[2][3] + K3XY * K12z * rho / (1 - q1) if q1 < 1 else Fr(10 ** 9)) * cM ** 3)
        return dict(rho=rho, ok=ok, q1=q1, K12=K12, E=E, Ep=Ep, cM=cM, c=c, K12z=K12z)

    def complement_gap(self, zeta, sig0):
        """Exact sufficient bound keeping C invertible with its node inertia on the full shifted Q-box."""
        nd = self.nd
        eps = sig0 * sig0
        X = zeta ** 3 + self.mub_ * zeta ** 2 + self.lamub * eps + self.a1ub * eps * zeta
        Y = zeta ** 3 + self.b1ub * eps * zeta
        amps = {'x': Fr(2), 'y': Fr(2), 'z': 2 * nd.J, 'odd': 2 * nd.abs_ub(nd.kappa)}
        # Hermitian term-by-term entry bounds; max row sum bounds operator norm.
        entry = [[Fr(0) for _ in range(4)] for _ in range(4)]
        for a, b, n, kind in TERMS:
            phi = abs(n[0]-n[1])*X + abs(n[0]+n[1])*Y + abs(n[2])*zeta
            delta = amps[kind] * phi + (2*eps if kind == 'odd' else 0)
            entry[a][b] += delta
            entry[b][a] += delta
        Hdelta = max(sum(r) for r in entry)
        Ufro2 = sum(nd.abs_ub(nd.T[i][j]) ** 2 for i in range(4) for j in (2,3))
        C = lp_block(nd.Hm, nd.T, (2,3), (2,3))
        Cnorm = sum(nd.abs_ub(sum(C[i][j].values(), nd.F.ZERO)) for i in range(2) for j in range(2))
        # min |lambda(C0)| >= |det C0| / ||C0||op >= dC0/Cnorm.
        margin = nd.dC0 / Cnorm - Ufro2 * Hdelta
        return margin > 0, margin

    def count(self, zeta, sig0, R=None):
        """exact inequalities for exactly one (eps < 0) / three (eps > 0) roots of h on |z| <= zeta, for 0 < |eps| <= sig0^2"""
        R = R or self.reduction(zeta)
        E, Ep = R["E"], R["Ep"]
        mu_lo, mu_hi = self.muiv
        zt = Fr(4, 5) * zeta                                           # z_top: all roots have |z| < z_top
        tau = (sig0 / zt) ** 6
        gap_ok, gap_margin = self.complement_gap(zeta, sig0)
        res = {"red": R["ok"] and sig0 <= zeta / 2 and gap_ok, "complement_gap": gap_ok, "complement_margin": gap_margin}
        # the points (X*, Y*, z) of the roots lie in Omega = {X^2 + Y^2 + z^6 <= zeta^6}
        res["inside"] = (R["K12"] * R["cM"] ** 4 * zt ** 4 * (1 + tau) ** 4) ** 2 + zt ** 6 <= zeta ** 6 if R["ok"] else False
        # eps < 0
        res["neg_deriv"] = Ep * zeta <= Fr(3, 2) and Ep * sig0 <= mu_lo / 2
        res["neg_sign"] = E * zt * (1 + tau) < 1
        # eps > 0: t_b < sqrt(mu/3) < t_a  (rationals), t_a^2 < mu
        cb_lo, cb_hi = sqrt_enc(mu_lo / 3)[0], sqrt_enc(mu_hi / 3)[1]
        t_b = Fr(int(Fr(4, 5) * cb_lo * 1000), 1000)
        t_a = Fr(-((-int(Fr(6, 5) * cb_hi * 1000 * 1000)) // 1000), 1000)
        res["t_ok"] = 3 * t_b * t_b < mu_lo and 3 * t_a * t_a > mu_hi and t_a * t_a < mu_lo and 0 < t_b < t_a
        res["P1"] = Ep * sig0 * (t_b ** 3 + 1) < mu_lo - 3 * t_b * t_b
        res["P2"] = (3 - mu_hi / (t_a * t_a)) > 0 and Ep * (1 + 1 / t_a ** 3) * zeta < (3 - mu_hi / (t_a * t_a))
        res["P3"] = E * sig0 * (1 + t_a * t_a) ** 2 < t_b * (mu_lo - t_a * t_a)
        res["P4"] = zt * zt > mu_hi * sig0 * sig0 and E * zt ** 4 * (1 + tau) < zt * (zt * zt - mu_hi * sig0 * sig0)
        return res, R, (t_a, t_b)


# ---- driver for the unfolding (exact)
ZETA = {"i": Fr(1, 20), "ii": Fr(1, 500)}
SIG0 = {"i": Fr(1, 250), "ii": Fr(1, 1500)}
UF = {}
if ALLOK:
    for nd in NODES:
        U = Unfold(nd)
        try:
            U.build()
            U.normal_form()
            if U.fail is None:
                U.prep_bounds()
                U.cres, U.R, U.ta = U.count(ZETA[nd.which], SIG0[nd.which])
        except (AssertionError, KeyError, IndexError, ZeroDivisionError) as e_:
            U.fail = repr(e_)
        UF[nd.name] = U
UOK = ALLOK and all(UF[nd.name].fail is None for nd in NODES)
check("U1: exact unfolding kappa = kappa_node + eps (cubic in eps, 5th build re-check): x' -> X = x + m z^2 + lam eps + a1 eps z, Y = y + b1 eps z: weight<=3 part = n_x X + n_y Y + n_b (z^3 - mu eps z), mu = (J+2)/kappa^3 = 8YA/(J^2(J+2)) > 0; rest weight >= 4",
      UOK and all(all(UF[nd.name].chk.values()) for nd in NODES),
      ("mu = " + ", ".join(f"{nd.name}: {UF[nd.name].mu}" for nd in NODES if nd.sgn > 0) + "; lam = " + ", ".join(f"{nd.name}: {UF[nd.name].lam}" for nd in NODES if nd.sgn > 0)) if UOK else "failed")
if UOK:
    for nd in NODES:
        U = UF[nd.name]
        vprint(nd.name, "zeta", ZETA[nd.which], "sigma0", SIG0[nd.which], "eps0", float(SIG0[nd.which] ** 2), "q1", float(U.R["q1"]), "K12", float(U.R["K12"]), "E", float(U.R["E"]), "E'", float(U.R["Ep"]),
               "cM", float(U.R["cM"]), "t_a,t_b", [float(x) for x in U.ta], "conds", U.cres)
check("U2: exact: on Q = {|z| <= zeta, X^2+Y^2 <= zeta^6}, |eps| <= eps0: C stays invertible with node inertia; (X,Y) slaved to z by contraction (q1 <= 1/2), |e| <= E m^4, |e'| <= E' m^3, m^6 = z^6+|eps|^3",
      UOK and all(UF[nd.name].R["ok"] and UF[nd.name].cres["red"] and UF[nd.name].cres["inside"] for nd in NODES),
      ("zeta, eps0: i 1/20, 1/62500; ii 1/500, 1/2250000; E, E' (i) %.2f %.2f, (ii) %.2f %.2f" % (float(UF["i+"].R["E"]), float(UF["i+"].R["Ep"]), float(UF["ii+"].R["E"]), float(UF["ii+"].R["Ep"]))) if UOK else "failed")
negok = UOK and all(UF[nd.name].cres["neg_deriv"] and UF[nd.name].cres["neg_sign"] for nd in NODES)
posok = UOK and all(all(UF[nd.name].cres[k] for k in ("t_ok", "P1", "P2", "P3", "P4")) for nd in NODES)
check("U3: exact: h(z) = z^3 - mu eps z + e(z) has exactly ONE root in |z| <= zeta for -eps0 <= eps < 0 and exactly THREE for 0 < eps <= eps0 (monotone pieces + sign changes): 1 resp. 3 zeros of the Pauli map in the shifted ball",
      negok and posok, "t_b, t_a (i) %.3f %.3f, (ii) %.3f %.3f" % (float(UF["i+"].ta[1]), float(UF["i+"].ta[0]), float(UF["ii+"].ta[1]), float(UF["ii+"].ta[0])) if UOK else "failed")
def _idxD(nd, hsign):
    return -(1 if nd.re_iv(nd.det3)[0] > 0 else -1) * hsign


idx_ok = UOK and negok and posok and all([_idxD(nd, -1), _idxD(nd, 1), _idxD(nd, 1)] == [-nd.sgn, nd.sgn, nd.sgn] and [_idxD(nd, 1)] == [nd.sgn] for nd in NODES)
check("U4: exact: D-index = -sign det L * sign h': (line, emitted pair) = (-1,+1,+1) for eps > 0, (+1) for eps < 0 at +x0, reversed at -x0; sum = ball degree",
      idx_ok,
      "sign det L: " + " ".join(f"{nd.name}:{'-' if nd.re_iv(nd.det3)[1] < 0 else '+'}" for nd in NODES))

ctrl_u = UOK
if UOK:
    SIG_BIG = {"i": Fr(1, 100), "ii": Fr(1, 1000)}
    for nd in NODES:
        U = UF[nd.name]
        r_big, _, _ = U.count(ZETA[nd.which], SIG_BIG[nd.which], U.R)
        ctrl_u = ctrl_u and not all(r_big[k] for k in ("t_ok", "P1", "P2", "P3", "P4", "neg_deriv", "neg_sign", "inside", "red"))
check("U5: control (non-vacuity): the exact conditions of U2/U3 fail at sigma0 = 1/100 (i), 1/1000 (ii), i.e. eps0 = 1e-4, 1e-6", ctrl_u)


# ---- FLOAT diagnostics for the unfolding: zeros of the Pauli map at eps = +-(inside the proven range), local degrees
def uf_float():
    from scipy.optimize import root
    rows = []
    for nd in NODES:
        U = UF[nd.name]
        J = float(nd.J)
        kap = float(nd.to_real(nd.kappa))
        z0c = nd.to_complex(nd.z0)
        x0 = float(np.arctan2(z0c.imag, z0c.real))
        Tn = np.array([[nd.to_complex(nd.T[r][c]) for c in range(4)] for r in range(4)])
        Wn, Un = Tn[:, :2], Tn[:, 2:]
        mf = float(nd.to_real(nd.mp))
        lam = float(nd.to_real(U.lam))
        mu = float(nd.to_real(U.mu))
        e0 = float(SIG0[nd.which] ** 2)
        zeta = float(ZETA[nd.which])
        for eps in (0.6 * e0, -0.6 * e0):
            sg_, s3 = abs(eps) ** 0.5, abs(eps) ** 1.5

            def pts_of(Xs, Ys, zs):
                return np.stack([Xs - mf * zs ** 2 - lam * eps, Ys, zs], -1)

            def Dmap(Xs, Ys, zs):
                P = pts_of(np.atleast_1d(Xs), np.atleast_1d(Ys), np.atleast_1d(zs))
                return schur_pauli(Hnum(P, kap + eps, J, x0), Wn, Un)[0]

            starts = [0.0] + ([np.sqrt(mu * eps), -np.sqrt(mu * eps)] if eps > 0 else [])
            sols = []
            for tz in starts:
                fun = lambda u: Dmap(u[0] * s3, u[1] * s3, u[2] * sg_)[0] / s3
                r_ = root(fun, [0.0, 0.0, tz / sg_], method="hybr", tol=1e-13)
                sols.append(np.array(r_.x) * np.array([s3, s3, sg_]))
            dist = min([np.linalg.norm((sols[a] - sols[b]) / np.array([s3, s3, sg_])) for a in range(len(sols)) for b in range(a)] + [9.9])
            ok_res = max(np.linalg.norm(Dmap(*s_)[0]) for s_ in sols) / s3 < 1e-6
            degl = []
            for s_ in sols:
                th = np.linspace(0, np.pi, 61)[:, None] * np.ones((1, 121))
                ph = np.ones((61, 1)) * np.linspace(0, 2 * np.pi, 121)[None, :]
                rr = 0.3 * min(1.0, np.sqrt(mu) / 2 if eps > 0 else 1.0)
                Xs = s_[0] + rr * s3 * np.sin(th) * np.cos(ph)
                Ys = s_[1] + rr * s3 * np.sin(th) * np.sin(ph)
                zs = s_[2] + rr * sg_ * np.cos(th)
                Dn = Dmap(Xs.ravel(), Ys.ravel(), zs.ravel()).reshape(61, 121, 3)
                degl.append(solid_degree(Dn, 60, 120)[0])
            # boundary sphere N = zeta in the (X, Y, z) coordinates
            th = np.linspace(0, np.pi, 81)[:, None] * np.ones((1, 161))
            ph = np.ones((81, 1)) * np.linspace(0, 2 * np.pi, 161)[None, :]
            p_, q_, s2 = np.cos(th), np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph)
            zb = zeta * np.sign(p_) * np.abs(p_) ** (1 / 3)
            Db = Dmap((zeta ** 3 * q_).ravel(), (zeta ** 3 * s2).ravel(), zb.ravel()).reshape(81, 161, 3)
            degb = solid_degree(Db, 80, 160)[0]
            # exact closed forms of the landed families at kappa = kappa_node + eps (float evaluation): line node (z = 0) and plane-(ii) pair (y = 0)
            k2 = (kap + eps) ** 2
            cc = J * J - 4 * k2 - 2
            cF = (J - 2) * (J + 1) / (J + 2)
            roots = [(1 + sg_r * np.sqrt(1 - 4 * k2 * cc)) / (4 * k2) for sg_r in (1, -1)]
            cl = min(roots, key=lambda r_: abs(r_ - cF))
            xl = np.arccos(cl)
            xe = np.arccos(1 - J / (4 * k2))
            ze = np.arccos((J + 2) / (4 * k2) - (4 + J - J * J) / J) if eps > 0 else 0.0     # the pair is real for eps >= 0
            # Newton solutions in (x, y, z) offsets
            offs = [(s_[0] - mf * s_[2] ** 2 - lam * eps, s_[1], s_[2]) for s_ in sols]
            ex = [(xl - x0, 0.0, 0.0)] + ([(xe - x0, 0.0, ze), (xe - x0, 0.0, -ze)] if eps > 0 else [])
            if eps > 0:
                order = [0, 1, 2]
                offs = [offs[0]] + sorted(offs[1:], key=lambda t: -t[2])
            dev_ex = max(abs(a - b) / (sg_ if k_ == 2 else 1.0) for o_, e_ in zip(offs, ex) for k_, (a, b) in enumerate(zip(o_, e_)))
            rows.append((nd.name, eps, len(sols), dist, ok_res, degl, degb, [float(s_[2] / sg_) for s_ in sols], dev_ex))
    return rows


try:
    UFROWS = uf_float() if UOK else []
except Exception as e_:                                                  # a failed diagnostic is a failed check, not a crash
    UFROWS = []
    vprint("uf_float failed:", repr(e_))
okuf = bool(UFROWS)
for (nm, eps, ns, dist, okr, degl, degb, tz, dev_ex) in UFROWS:
    sgn = 1 if nm.endswith("+") else -1
    exp = ([-1, 1, 1] if eps > 0 else [1])
    exp = [e_ * sgn for e_ in exp]
    # order of solutions: line node first, then +sqrt(mu eps), -sqrt(mu eps)
    okuf = okuf and ns == (3 if eps > 0 else 1) and okr and dist > 3 * 0.3 and all(abs(a - b) < 1e-3 for a, b in zip(degl, exp)) and abs(degb - sgn) < 1e-3
check("UF1 FLOAT: direct Schur at kappa_node + eps, eps = +-0.6 eps0, 4 nodes: Newton gives 3 (eps > 0) / 1 (eps < 0) simple separated zeros, local degrees as U4, boundary-sphere degree = node sign",
      okuf and UOK, "z/sqrt(eps) (i+): " + (", ".join(f"{t:+.3f}" for t in UFROWS[0][7]) if UFROWS else "n/a") + "; degrees " + (", ".join(f"{d:+.3f}" for d in UFROWS[0][5]) if UFROWS else "n/a"))
sgn_plus = [r_ for r_ in UFROWS if r_[0].endswith("+")]
check("UF2 FLOAT: +x0 Newton zeros = landed exact families (line root c; emitted pair cos x = 1 - J/(4k^2), cos z = (J+2)/(4k^2) - (4+J-J^2)/J, y = 0)", UOK and bool(sgn_plus) and max(r_[8] for r_ in sgn_plus) < 1e-6,
      "max deviation " + (f"{max(r_[8] for r_ in sgn_plus):.1e}" if sgn_plus else "n/a"))

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}   ({time.time() - T0:.0f} s)")

# A failed scientific check must fail the bounded execution.
raise SystemExit(1 if len(RESULTS) - sum(RESULTS) else 0)
