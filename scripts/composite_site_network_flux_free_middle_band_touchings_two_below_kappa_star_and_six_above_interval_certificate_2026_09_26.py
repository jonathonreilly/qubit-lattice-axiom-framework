#!/usr/bin/env python3
"""Composite-site network, flux-free comparator: exact touchings of the middle bands, two below kappa* = sqrt(3/20) and six above.

Supplied u = +1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, isotropic J = 1,
four-site Bloch matrix H(f) = i M(f) over the fractional zone. A computer-assisted certificate:
(A) exact rational algebra (sympy, polynomial-ring determinants), for every kappa: D = det H, its three momentum derivatives and the
    constant and linear characteristic-polynomial coefficients vanish at the two line nodes f = (x, 1 - x, 0), cos 2 pi x =
    [1 - sqrt(1 + 4k^2 + 16k^4)]/(4k^2), and, for 3/20 < k^2 <= 1/4, at the four plane nodes f = (x, 1 - x, +-f3) and (1 - x, x, +-f3)
    with cos 2 pi x = 1 - 1/(4k^2), cos 2 pi f3 = 3/(4k^2) - 4, and, for k^2 >= 1/4, at the four points (f3 + g, f3 - g, f3) with
    cos 2 pi f3 = 3/2 - s/2, cos 2 pi g = -5/2 + s/2, s = sqrt(13 + 3/k^2), both signs of f3 and of g;
(B) rigorous clearing: interval enclosures of H at exact dyadic cube centres (mpmath interval phases, outward-rounded IEEE float
    arithmetic) and interval LDL^T inertia show that outside small boxes every cube has exactly two negative and two positive levels,
    none within lip h of zero (the landed Lipschitz bound and Weyl's inequality carry this to the whole cube);
(C) each box contains exactly one exact node, where the outer levels are nonzero (interval evaluation), and the Hessian of D is
    positive definite on the whole box (centred interval forms with bisection, interval Cholesky), so D > 0 there except at the node;
    Hessian - m I positive definite gives a middle gap >= sqrt(2m)/||H||_bound |f - f*| on the box (conical touching);
(D) at each node the chirality sign det V, V the Pauli coefficients of P dH P with P = (H^2 - tr(H) H + q)/q the kernel projector,
    is certified from det V = Im Tr(P d1H P d2H P d3H)/2 in interval arithmetic; the chiralities sum to zero.
Checks: (1) enclosure sanity; (2) exact line-node algebra; (3) exact plane-node algebra below 1/2; (4) exact node algebra above 1/2;
(5)-(12) certificates at kappa = 1/10, 3/10, 7/20 (two nodes), 9/20, 12/25 and 3/5, 4/5, 1 (six nodes). Couplings between the samples are not certified here.
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np
import sympy as sp
from mpmath import iv, mp, mpc, mpf
from sympy.polys.matrices import DomainMatrix

AUDIT_TIMEOUT_SEC = 1800

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" -- {detail}" if detail else ""), flush=True)


# ------------------------------------------------------------------------------------------------ network and Bloch terms
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


A_VEC = np.array([[2, 0, 0], [0, 2, 0], [1, 1, 2]])       # rows: primitive translations of the site and colour rules
REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]


def reduce(p):
    """p = rep + n1 a1 + n2 a2 + n3 a3 with rep in the 2x2x2 box; returns (rep index, n)."""
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)


def terms(J, kappa):
    """Real hopping terms (a, b, n, t): M(f)[a, b] += t e^{2 pi i f.n}, M(f)[b, a] -= t e^{-2 pi i f.n}, gauge u = +1."""
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


def clusters(C, h):
    """Connected groups of uncleared cubes (touching or diagonal neighbours, periodic zone), by breadth-first search on the
    integer cube indices of the finest level."""
    n = int(round(0.5 / h))                          # cubes have full width 2h
    ids = np.floor(C / (2 * h)).astype(np.int64) % n
    where = {tuple(x): i for i, x in enumerate(ids)}
    seen = np.zeros(len(C), dtype=bool)
    out = []
    offs = [d for d in itertools.product((-1, 0, 1), repeat=3) if d != (0, 0, 0)]
    for s0 in range(len(C)):
        if seen[s0]:
            continue
        seen[s0] = True
        grp = [s0]; q = [s0]
        while q:
            i = q.pop()
            x = ids[i]
            for d in offs:
                k = where.get(((x[0] + d[0]) % n, (x[1] + d[1]) % n, (x[2] + d[2]) % n))
                if k is not None and not seen[k]:
                    seen[k] = True; grp.append(k); q.append(k)
        out.append(np.array(grp))
    return out


# ------------------------------------------------------------------------------------------------ rigorous interval tools
DN, UP = -np.inf, np.inf


def rd(x):
    return np.nextafter(x, DN)


def ru(x):
    return np.nextafter(x, UP)


class I:
    """Real interval arrays [lo, hi]."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = np.asarray(lo, dtype=float)
        self.hi = self.lo.copy() if hi is None else np.asarray(hi, dtype=float)

    def __add__(self, o):
        o = o if isinstance(o, I) else I(o)
        return I(rd(self.lo + o.lo), ru(self.hi + o.hi))

    def __sub__(self, o):
        o = o if isinstance(o, I) else I(o)
        return I(rd(self.lo - o.hi), ru(self.hi - o.lo))

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __mul__(self, o):
        o = o if isinstance(o, I) else I(o)
        p = np.stack([self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi])
        return I(rd(p.min(axis=0)), ru(p.max(axis=0)))

    def sq(self):
        a, b = self.lo * self.lo, self.hi * self.hi
        lo = np.where((self.lo <= 0) & (self.hi >= 0), 0.0, rd(np.minimum(a, b)))
        return I(lo, ru(np.maximum(a, b)))

    def div(self, o):
        """self / o, o must exclude zero (checked by the caller)."""
        p = np.stack([self.lo / o.lo, self.lo / o.hi, self.hi / o.lo, self.hi / o.hi])
        return I(rd(p.min(axis=0)), ru(p.max(axis=0)))


class C:
    """Complex interval arrays as rectangles re + i im."""
    __slots__ = ("re", "im")

    def __init__(self, re, im):
        self.re, self.im = re, im

    def __add__(self, o):
        return C(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return C(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return C(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def rmul(self, r):
        return C(self.re * r, self.im * r)

    def conj(self):
        return C(self.re, -self.im)

    def abs2(self):
        return self.re.sq() + self.im.sq()


def phase_table(values):
    """Rigorous enclosures of cos and sin of 2 pi v for exactly representable floats v (converted exactly to mpf)."""
    out = {}
    for v in values:
        x = iv.mpf(mpf(float(v)))
        a = 2 * iv.pi * x
        cc, ss = iv.cos(a), iv.sin(a)
        out[float(v)] = (float(cc.a), float(cc.b), float(ss.a), float(ss.b))
    return out


def inertia_neg(A, mu):
    """A: dict (i, j) -> C for i <= j (Hermitian, diagonal imaginary parts zero). Returns (number of negative pivots of A - mu I,
    ok) where ok is False wherever a pivot interval contains zero (inertia not certified there)."""
    n = 4
    N = A[(0, 0)].re.lo.shape
    d = [None] * n
    L = {}
    ok = np.ones(N, dtype=bool)
    neg = np.zeros(N, dtype=np.int64)
    for k in range(n):
        dk = A[(k, k)].re - mu
        for j in range(k):
            dk = dk - L[(k, j)].abs2() * d[j]
        d[k] = dk
        pos, ng = dk.lo > 0, dk.hi < 0
        ok &= pos | ng
        neg += ng
        safe = I(np.where(pos | ng, dk.lo, 1.0), np.where(pos | ng, dk.hi, 1.0))
        for i in range(k + 1, n):
            s = A[(k, i)].conj()                       # A[i, k] = conj(A[k, i])
            for j in range(k):
                s = s - (L[(i, j)] * L[(k, j)].conj()).rmul(d[j])
            L[(i, k)] = C(s.re.div(safe), s.im.div(safe))
    return neg, ok


def t_interval(t):
    """Hopping amplitudes: 2J = 2 exactly; 2 kappa enclosed one ulp either side of its float, which contains the exact rational."""
    return (t, t) if t == 2.0 else (float(np.nextafter(t, -np.inf)), float(np.nextafter(t, np.inf)))


def build(terms):
    a = np.array([x[0] for x in terms]); b = np.array([x[1] for x in terms])
    n = np.array([x[2] for x in terms], dtype=np.int64)
    t = [t_interval(float(x[3])) for x in terms]
    lip = iv.mpf(0)
    for j in range(len(terms)):
        fac = 2 if a[j] == b[j] else 1
        lip += fac * iv.mpf(t[j][1]) * 2 * iv.pi * int(np.abs(n[j]).sum())
    return a, b, n, t, float(lip.b)


def H_intervals(Cs, a, b, n, t):
    """Upper-triangle complex-interval entries of H(c) = i M(c) for every centre c (rows of Cs)."""
    N = len(Cs)
    vals = np.mod(Cs @ n.T.astype(float), 1.0)              # exact for dyadic centres and small integer n
    uniq = np.unique(vals)
    tab = phase_table(uniq)
    look = np.array([tab[float(v)] for v in uniq])
    idx = np.searchsorted(uniq, vals)
    cl, ch, sl, sh = look[idx, 0], look[idx, 1], look[idx, 2], look[idx, 3]
    zero = lambda: I(np.zeros(N))
    Mre = {(i, j): zero() for i in range(4) for j in range(4)}
    Mim = {(i, j): zero() for i in range(4) for j in range(4)}
    for j in range(len(a)):
        tt = I(np.full(N, t[j][0]), np.full(N, t[j][1]))
        cs = I(cl[:, j], ch[:, j]); sn = I(sl[:, j], sh[:, j])
        Mre[(a[j], b[j])] = Mre[(a[j], b[j])] + tt * cs            # + t e^{i th}
        Mim[(a[j], b[j])] = Mim[(a[j], b[j])] + tt * sn
        Mre[(b[j], a[j])] = Mre[(b[j], a[j])] - tt * cs            # - t e^{-i th}
        Mim[(b[j], a[j])] = Mim[(b[j], a[j])] + tt * sn
    A = {}
    for i in range(4):
        for j in range(i, 4):
            A[(i, j)] = C(-Mim[(i, j)], Mre[(i, j)])             # H = i M
    return A


def clear(J, kappa, n0=32, levels=12, chunk=100000, verbose=True):
    tms = terms(J, kappa)
    a, b, n, t, lip = build(tms)
    h = 0.5 / n0
    g = (np.arange(n0) + 0.5) / n0
    Cs = np.array(list(itertools.product(g, g, g)))
    log, t0 = [], time.time()
    negs = set()
    for lev in range(levels):
        r = float(ru(lip * h))
        keep = []
        for s in range(0, len(Cs), chunk):
            c = Cs[s:s + chunk]
            A = H_intervals(c, a, b, n, t)
            ngp, okp = inertia_neg(A, r)
            ngm, okm = inertia_neg(A, -r)
            cleared = okp & okm & (ngp == ngm)
            negs |= set(np.unique(ngp[cleared]).tolist())
            keep.append(c[~cleared])
        Cs = np.concatenate(keep)
        log.append((lev, h, r, len(Cs)))
        if verbose:
            print(f"   level {lev}: half-width {h:.3e}, r {r:.3e}, uncleared {len(Cs)}, {time.time() - t0:.0f} s", flush=True)
        if lev == levels - 1 or len(Cs) == 0:
            break
        off = np.array(list(itertools.product((-0.5, 0.5), repeat=3))) * h
        Cs = (Cs[:, None, :] + off[None, :, :]).reshape(-1, 3)
        h /= 2
    return Cs, h, lip, log, negs


# ------------------------------------------------------------------------------------------------ exact algebra
z1, z2, w, kk, mu = sp.symbols("z1 z2 w k mu")
S = 2
TERMS = terms((1.0, 1.0, 1.0), 0.3)                      # kappa enters only as the odd-term amplitude 2 kappa
assert max(abs(int(x)) for tm in TERMS for x in tm[2]) <= S


def shifted(kap, line=False, withmu=False):
    """(z1 z2 w)^S M, or z1^{2S} M on the line z2 = 1/z1, w = 1, with exact amplitudes 2 J = 2 and 2 kappa."""
    Ms = [[sp.Integer(0)] * 4 for _ in range(4)]
    for (a, b, n, t) in TERMS:
        tt = sp.Integer(2) if abs(t - 2.0) < 1e-12 else 2 * kap
        e = [int(x) for x in n]
        if line:
            d = e[0] - e[1]
            Ms[a][b] += tt * z1 ** (2 * S + d); Ms[b][a] -= tt * z1 ** (2 * S - d)
        else:
            Ms[a][b] += tt * z1 ** (S + e[0]) * z2 ** (S + e[1]) * w ** (S + e[2])
            Ms[b][a] -= tt * z1 ** (S - e[0]) * z2 ** (S - e[1]) * w ** (S - e[2])
    if withmu:
        for i in range(4):
            Ms[i][i] += mu * z1 ** (2 * S)
    return Ms


def det_of(Ms, gens):
    R = sp.QQ[gens]
    return R.to_sympy(DomainMatrix([[R.from_sympy(sp.expand(x)) for x in r] for r in Ms], (4, 4), R).det())


def Pk(kap, dom):
    return sp.Poly(kap ** 2 * z1 ** 4 - z1 ** 3 - (1 + 2 * kap ** 2) * z1 ** 2 - z1 + kap ** 2, z1, domain=dom)


def D_of(kap):
    """det H = det M (dimension four) as a Laurent polynomial in z1, z2, w (and k when kappa is the symbol)."""
    gens = [kk, z1, z2, w] if isinstance(kap, sp.Symbol) else [z1, z2, w]
    return sp.expand(det_of(shifted(kap), gens) / (z1 * z2 * w) ** (4 * S))


# ---------------------------------------------------------------- 1. enclosure sanity
a_, b_, n_, t_, lip_ = build(TERMS)
rng = np.random.default_rng(0)
pts = np.floor(rng.random((400, 3)) * 2 ** 20) / 2 ** 20
A_ = H_intervals(pts, a_, b_, n_, t_)
mp.dps = 40
miss = 0
for s in range(20):
    f = [mpf(float(x)) for x in pts[s]]
    M = [[mpc(0)] * 4 for _ in range(4)]
    for (a, b, n, t) in TERMS:
        tt = mpf(2) if abs(t - 2) < 1e-12 else mpf(3) / 5
        th = 2 * mp.pi * sum(f[j] * int(n[j]) for j in range(3))
        M[a][b] += tt * mp.expj(th); M[b][a] -= tt * mp.expj(-th)
    for (i, j), e in A_.items():
        hij = mpc(0, 1) * M[i][j]
        miss += not (e.re.lo[s] <= hij.real <= e.re.hi[s] and (i == j or e.im.lo[s] <= hij.imag <= e.im.hi[s]))
Hf = np.zeros((len(pts), 4, 4), dtype=complex)
ph = np.exp(2j * np.pi * pts @ n_.T)
for j, (a, b, n, t) in enumerate(TERMS):
    Hf[:, a, b] += 1j * t * ph[:, j]; Hf[:, b, a] -= 1j * t * np.conj(ph[:, j])
ev = np.linalg.eigvalsh(Hf)
agree, cert = [], []
for m_ in (-1.0, 0.0, 0.37, 2.5):
    ng, ok = inertia_neg(A_, m_)
    cert.append(ok.mean()); agree.append(np.mean(ng[ok] == (ev[ok] < m_).sum(axis=1)))
check("interval Bloch matrices at kappa = 3/10 contain the 40-digit entries at 20 dyadic points, and interval inertia counts agree "
      "with floating eigenvalue counts at 400 points and four shifts", miss == 0 and min(agree) == 1.0 and min(cert) == 1.0,
      f"entries outside the enclosures {miss}; certified fraction {min(cert):.3f}; agreement {min(agree):.3f}; "
      f"max entry width {max(float(np.max(e.re.hi - e.re.lo)) for e in A_.values()):.1e}")

# ---------------------------------------------------------------- 2. exact line algebra for every kappa
Dk = D_of(kk)
Fk = sp.QQ.frac_field(kk)
Pgen = Pk(kk, Fk)
line = {z2: 1 / z1, w: 1}


def red(expr, shift=8):
    return sp.simplify(sp.rem(sp.Poly(sp.expand(sp.expand(expr.subs(line)) * z1 ** shift), z1, domain=Fk), Pgen).as_expr())


r_D = red(Dk)
r_g = [red(v * sp.diff(Dk, v)) for v in (z1, z2, w)]
cp = sp.expand(det_of(shifted(kk, True, True), [kk, z1, mu]) / z1 ** (8 * S))
r_c0 = sp.simplify(sp.rem(sp.Poly(sp.expand(cp.coeff(mu, 0) * z1 ** 8), z1, domain=Fk), Pgen).as_expr())
r_c1 = sp.simplify(sp.rem(sp.Poly(sp.expand(cp.coeff(mu, 1) * z1 ** 8), z1, domain=Fk), Pgen).as_expr())
cst = sp.symbols("c")
landed = sp.simplify(sp.expand(Dk.subs(line)) - 16 * (1 + 4 * cst ** 2 * kk ** 2 - 2 * cst - 4 * kk ** 2 - 2) ** 2).subs(cst, (z1 + 1 / z1) / 2)
# the landed rational-point polynomial at f = (1/4, 3/4, 1/2): det(H - lam) = (lam^2 - 48(1/2 - k)^2)(lam^2 - 48(1/2 + k)^2)
lam = sp.symbols("lam")
Mr = sp.Matrix(4, 4, lambda i, j: 0)
for (a, b, n, t) in TERMS:
    tt = sp.Integer(2) if abs(t - 2.0) < 1e-12 else 2 * kk
    ph = sp.I ** int(n[0]) * (-sp.I) ** int(n[1]) * (-1) ** int(n[2])      # e^{2 pi i f.n} at (1/4, 3/4, 1/2)
    Mr[a, b] += tt * ph; Mr[b, a] -= tt * sp.conjugate(ph)
rat = sp.expand((sp.I * Mr - lam * sp.eye(4)).det() - (lam ** 2 - 48 * (sp.Rational(1, 2) - kk) ** 2) * (lam ** 2 - 48 * (sp.Rational(1, 2) + kk) ** 2))
check("exact line algebra for every kappa (J = 1): at the roots of P_k the determinant, its three momentum derivatives and the "
      "constant and linear characteristic-polynomial coefficients vanish; on the line D equals the landed 16[1 + 4c^2k^2 - 2c - 4k^2 - 2]^2, "
      "and at (1/4, 3/4, 1/2) the characteristic polynomial is the landed (lam^2 - 48(1/2 - k)^2)(lam^2 - 48(1/2 + k)^2)",
      all(x == 0 for x in [r_D, r_c0, r_c1] + r_g) and sp.simplify(landed) == 0 and rat == 0,
      f"remainders D {r_D}, gradient {r_g}, lambda^0 {r_c0}, lambda^1 {r_c1}; rational-point difference {rat}; {time.time() - T0:.0f} s")



# ---------------------------------------------------------------- 3. exact off-line nodes for every kappa
u_ = 1 / (4 * kk ** 2)
C1, C3 = 1 - u_, 3 * u_ - 4
G2 = [sp.expand((z1 ** 2 - 2 * C1 * z1 + 1) * 4 * kk ** 2), sp.expand((w ** 2 - 2 * C3 * w + 1) * 4 * kk ** 2)]


def red2(expr, shift=8):
    e = sp.expand(sp.expand(expr.subs(z2, 1 / z1)) * z1 ** shift * w ** shift)
    return sp.simplify(sp.reduced(e, G2, z1, w, domain=Fk)[1])


def plane_charpoly():
    """det(M + mu I) on the plane z2 = 1/z1, as a Laurent polynomial in z1, w, mu and k."""
    Ms = [[sp.Integer(0)] * 4 for _ in range(4)]
    for (a, b, n, t) in TERMS:
        tt = sp.Integer(2) if abs(t - 2.0) < 1e-12 else 2 * kk
        e = [int(x) for x in n]
        d = e[0] - e[1]
        Ms[a][b] += tt * z1 ** (2 * S + d) * w ** (S + e[2]); Ms[b][a] -= tt * z1 ** (2 * S - d) * w ** (S - e[2])
    for i in range(4):
        Ms[i][i] += mu * z1 ** (2 * S) * w ** S
    return sp.expand(det_of(Ms, [kk, z1, w, mu]) / (z1 ** (8 * S) * w ** (4 * S)))


CPP = plane_charpoly()
o_D = red2(Dk)
o_g = [red2(v * sp.diff(Dk, v)) for v in (z1, z2, w)]
o_c = [sp.simplify(sp.reduced(sp.expand(CPP.coeff(mu, j) * z1 ** 8 * w ** 8), G2, z1, w, domain=Fk)[1]) for j in (0, 1)]
check("exact off-line nodes for every kappa (J = 1): on the plane f1 + f2 = 1 at cos 2 pi x = 1 - 1/(4k^2), cos 2 pi f3 = 3/(4k^2) - 4 "
      "(real for 3/20 < k^2 <= 1/4) the determinant, its three momentum derivatives and the constant and linear characteristic-"
      "polynomial coefficients vanish", all(x == 0 for x in [o_D] + o_g + o_c),
      f"remainders modulo the two quadratics: D {o_D}, gradient {o_g}, lambda^0 {o_c[0]}, lambda^1 {o_c[1]}; {time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 4. exact nodes above kappa = 1/2 for every kappa
yv, sv = sp.symbols("y s")
G3 = [sp.expand(w ** 2 - 2 * (sp.Rational(3, 2) - sv / 2) * w + 1), sp.expand(yv ** 2 - 2 * (-sp.Rational(5, 2) + sv / 2) * yv + 1),
      sp.expand((sv ** 2 - 13) * kk ** 2 - 3)]


def red3(expr, sh=10):
    e = sp.expand(sp.expand(expr.subs({z1: w * yv, z2: w / yv}, simultaneous=True)) * w ** sh * yv ** sh)
    return sp.simplify(sp.reduced(e, G3, w, yv, sv, order="lex", domain=Fk)[1])


def full_charpoly():
    """det(M + mu I) at general momentum as a Laurent polynomial in z1, z2, w, mu and k."""
    Ms = shifted(kk)
    for i in range(4):
        Ms[i][i] += mu * (z1 * z2 * w) ** S
    return sp.expand(det_of(Ms, [kk, z1, z2, w, mu]) / (z1 * z2 * w) ** (4 * S))


CPF = full_charpoly()
a_D = red3(Dk)
a_g = [red3(v * sp.diff(Dk, v)) for v in (z1, z2, w)]
a_c = [red3(CPF.coeff(mu, j)) for j in (0, 1)]
check("exact nodes above kappa = 1/2 for every kappa (J = 1): at f = (f3 + g, f3 - g, f3) with cos 2 pi f3 = 3/2 - s/2, cos 2 pi g = "
      "-5/2 + s/2, s = sqrt(13 + 3/k^2) (real for k^2 >= 1/4) the determinant, its three momentum derivatives and the constant and "
      "linear characteristic-polynomial coefficients vanish", all(x == 0 for x in [a_D] + a_g + a_c),
      f"remainders modulo the two quadratics and s^2 = 13 + 3/k^2: D {a_D}, gradient {a_g}, lambda^0 {a_c[0]}, lambda^1 {a_c[1]}; "
      f"{time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 5.-12. certificates

def hess_centred(tl, lo, hi):
    c = [(mpf(float(lo[j])) + mpf(float(hi[j]))) / 2 for j in range(3)]
    r = [(mpf(float(hi[j])) - mpf(float(lo[j]))) / 2 for j in range(3)]
    fc = [iv.mpf(x) for x in c]
    fb = [iv.mpf([mpf(float(lo[j])), mpf(float(hi[j]))]) for j in range(3)]
    rad = [iv.mpf([-r[j], r[j]]) for j in range(3)]
    Hm = [[iv.mpf(0)] * 3 for _ in range(3)]
    for m, a in tl:
        aa = iv.mpf(a.p) / iv.mpf(a.q)
        ch = iv.cos(2 * iv.pi * (m[0] * fc[0] + m[1] * fc[1] + m[2] * fc[2]))
        sb = iv.sin(2 * iv.pi * (m[0] * fb[0] + m[1] * fb[1] + m[2] * fb[2]))
        lin = m[0] * rad[0] + m[1] * rad[1] + m[2] * rad[2]
        for i in range(3):
            for j in range(i, 3):
                # d_i d_j D = -4 pi^2 sum a m_i m_j cos; its variation is 8 pi^3 sum a m_i m_j (m . delta) sin over the box
                Hm[i][j] += aa * m[i] * m[j] * (-4 * iv.pi ** 2 * ch + 8 * iv.pi ** 3 * lin * sb)
    for i in range(3):
        for j in range(i):
            Hm[i][j] = Hm[j][i]
    return Hm


def chol_pd(Hm, shift=0):
    Lm = [[iv.mpf(0)] * 3 for _ in range(3)]; piv = []
    for k in range(3):
        s = Hm[k][k] - shift - sum(Lm[k][j] ** 2 for j in range(k)); piv.append(s)
        if not s.a > 0:
            return False, piv
        Lm[k][k] = iv.sqrt(s)
        for i in range(k + 1, 3):
            Lm[i][k] = (Hm[i][k] - sum(Lm[i][j] * Lm[k][j] for j in range(k))) / Lm[k][k]
    return True, piv


def pd_box(tl, lo, hi, depth=0, maxdepth=9, stats=None, shift=0):
    """Hessian - shift I positive definite on the whole box, by centred forms and bisection of the longest side."""
    stats = stats if stats is not None else {"boxes": 0, "minpiv": float("inf")}
    ok, piv = chol_pd(hess_centred(tl, lo, hi), shift)
    stats["boxes"] += 1
    if ok:
        stats["minpiv"] = min(stats["minpiv"], min(float(p.a) for p in piv))
        return True, stats
    if depth >= maxdepth:
        return False, stats
    k = max(range(3), key=lambda j: hi[j] - lo[j])
    mid = (lo[k] + hi[k]) / 2
    hi1 = list(hi); hi1[k] = mid
    lo2 = list(lo); lo2[k] = mid
    a, _ = pd_box(tl, lo, hi1, depth + 1, maxdepth, stats, shift)
    if not a:
        return False, stats
    return pd_box(tl, lo2, hi, depth + 1, maxdepth, stats, shift)


def enclose_acos(c, fl):
    """x with cos 2 pi x = c in (0, 1/2), enclosed by a certified sign change of cos 2 pi x - c around the float value fl."""
    xl, xh = mpf(fl) - mpf(10) ** -12, mpf(fl) + mpf(10) ** -12
    g = lambda x: iv.cos(2 * iv.pi * iv.mpf(x)) - c
    gl, gh = g(xl), g(xh)
    assert gl.a > 0 and gh.b < 0                          # cos 2 pi x is decreasing on (0, 1/2)
    return iv.mpf([xl, xh])


def outer_nonzero(kap, node):
    """Interval value (real, imaginary) of the quadratic characteristic coefficient, the product of the outer levels up to sign,
    at the node enclosure (f1, f2, f3)."""
    poly = sp.Poly(sp.expand(CPF.coeff(mu, 2).subs(kk, kap) * (z1 * z2 * w) ** 8), z1, z2, w)
    re_, im_ = iv.mpf(0), iv.mpf(0)
    for (p1, p2, p3), cf in poly.terms():
        ang = 2 * iv.pi * ((p1 - 8) * node[0] + (p2 - 8) * node[1] + (p3 - 8) * node[2])
        cf = sp.Rational(cf); c_ = iv.mpf(cf.p) / iv.mpf(cf.q)
        re_ += c_ * iv.cos(ang); im_ += c_ * iv.sin(ang)
    return re_, im_


def Hd_iv(terms, kap, f):
    """Interval H(f) and dH/df_j (fractional momentum) at interval momentum f, as 4x4 lists of iv.mpc."""
    Z = lambda: [[iv.mpc(0) for _ in range(4)] for _ in range(4)]
    M, dM = Z(), [Z(), Z(), Z()]
    for (a, b, n, t) in terms:
        tt = iv.mpf(2) if abs(t - 2) < 1e-12 else 2 * iv.mpf(kap[0]) / kap[1]
        th = 2 * iv.pi * sum(int(n[j]) * f[j] for j in range(3))
        e = iv.mpc(iv.cos(th), iv.sin(th)); ec = iv.mpc(iv.cos(th), -iv.sin(th))
        M[a][b] += tt * e; M[b][a] -= tt * ec
        for j in range(3):
            c = 2 * iv.pi * int(n[j])
            dM[j][a][b] += tt * e * iv.mpc(0, 1) * c; dM[j][b][a] -= tt * ec * iv.mpc(0, -1) * c
    I = iv.mpc(0, 1)
    H = [[I * M[r][c] for c in range(4)] for r in range(4)]
    dH = [[[I * dM[j][r][c] for c in range(4)] for r in range(4)] for j in range(3)]
    return H, dH


def mm(A, B):
    return [[sum((A[r][k] * B[k][c] for k in range(4)), iv.mpc(0)) for c in range(4)] for r in range(4)]


def chirality(terms, kap, f):
    H, dH = Hd_iv(terms, kap, f)
    tr = sum((H[i][i] for i in range(4)), iv.mpc(0))
    q = sum((H[i][i] * H[j][j] - H[i][j] * H[j][i] for i in range(4) for j in range(i + 1, 4)), iv.mpc(0))
    H2 = mm(H, H)
    P = [[(H2[r][c] - tr * H[r][c] + (q if r == c else iv.mpc(0))) / q for c in range(4)] for r in range(4)]
    T = mm(mm(mm(P, dH[0]), mm(P, dH[1])), mm(P, dH[2]))
    t = sum((T[i][i] for i in range(4)), iv.mpc(0))
    return t.imag / 2, q.real



def certificate(p, q, levels=13):
    t0 = time.time()
    kap = sp.Rational(p, q)
    Cs, h, lip, log, negs = clear((1.0, 1.0, 1.0), float(kap), levels=levels, verbose=False)
    D = D_of(kap)
    tl = [((m[0] - 8, m[1] - 8, m[2] - 8), sp.Rational(c)) for m, c in sp.Poly(sp.expand(D * (z1 * z2 * w) ** 8), z1, z2, w).terms()]
    mp.dps = 40; iv.dps = 30
    k2 = sp.Rational(p, q) ** 2
    cl = (1 - sp.sqrt(1 + 4 * k2 + 16 * k2 ** 2)) / (4 * k2)
    cl_iv = (1 - iv.sqrt(1 + 4 * iv.mpf(k2.p) / k2.q + 16 * (iv.mpf(k2.p) / k2.q) ** 2)) / (4 * iv.mpf(k2.p) / k2.q)
    xl = enclose_acos(cl_iv, mp.acos(sp.N(cl, 50)) / (2 * mp.pi))
    nodes = [((xl, 1 - xl, iv.mpf(0)), True), ((1 - xl, xl, iv.mpf(0)), True)]
    if sp.Rational(3, 20) < k2 < sp.Rational(1, 4):
        c1, c3 = 1 - 1 / (4 * k2), 3 / (4 * k2) - 4
        xo = enclose_acos(iv.mpf(c1.p) / c1.q, mp.acos(mpf(c1.p) / c1.q) / (2 * mp.pi))
        fo = enclose_acos(iv.mpf(c3.p) / c3.q, mp.acos(mpf(c3.p) / c3.q) / (2 * mp.pi))
        nodes += [((xo, 1 - xo, fo), False), ((xo, 1 - xo, 1 - fo), False), ((1 - xo, xo, fo), False), ((1 - xo, xo, 1 - fo), False)]
    elif k2 > sp.Rational(1, 4):
        sq = iv.sqrt(13 + 3 * iv.mpf(k2.q) / k2.p)
        sqf = mp.sqrt(13 + 3 * mpf(k2.q) / k2.p)
        F = enclose_acos(iv.mpf(3) / 2 - sq / 2, mp.acos(mpf(3) / 2 - sqf / 2) / (2 * mp.pi))
        Gg = enclose_acos(-iv.mpf(5) / 2 + sq / 2, mp.acos(-mpf(5) / 2 + sqf / 2) / (2 * mp.pi))
        nodes += [((sf * F + sg * Gg, sf * F - sg * Gg, sf * F), False) for sf in (1, -1) for sg in (1, -1)]
    # the outer levels are nonzero at every node, so zero is exactly a double level there
    outer = all((lambda r: not (r[0].a <= 0 <= r[0].b and r[1].a <= 0 <= r[1].b))(outer_nonzero(kap, nd[0])) for nd in nodes)
    chir = []
    for nd, _ in nodes:
        dv, _q = chirality(TERMS, (p, q), list(nd))
        chir.append(1 if dv.a > 0 else (-1 if dv.b < 0 else 0))
    groups = clusters(Cs, h)
    ok = negs == {2} and len(groups) == len(nodes) and outer and 0 not in chir and sum(chir) == 0
    hit, pivs, nsub, cone = [], [], 0, []
    NH = float(sum((2 if a == b else 1) * abs(float(2 * kap if abs(t - 2.0) > 1e-12 else 2)) for (a, b, n, t) in TERMS)) + 1e-9
    for gi in groups:
        X = Cs[gi].copy(); X = X - np.round(X - X[0])
        lo, hi = X.min(axis=0) - h, X.max(axis=0) + h
        mid = (lo + hi) / 2
        inside = [i for i, (nd, _) in enumerate(nodes)
                  if all(nd[j].a - round(float(nd[j].a) - mid[j]) >= lo[j] and nd[j].b - round(float(nd[j].a) - mid[j]) <= hi[j] for j in range(3))]
        pd, st = pd_box(tl, lo, hi)
        ok &= pd and len(inside) == 1
        hit += inside; pivs.append(st["minpiv"]); nsub += st["boxes"]
        # conical gap: Hess - m I positive definite gives D >= (m/2)|d|^2; |l1 l4| <= ||H||^2; AM-GM on l2 <= 0 <= l3
        m = st["minpiv"] / 4 if pd else 0.0
        while pd and m > 1e-6 and not pd_box(tl, lo, hi, shift=m)[0]:
            m /= 4
        cone.append(0.99 * float(mp.sqrt(2 * mpf(m)) / mpf(NH)) if pd else 0.0)      # 1% below the certified constant
    ok &= sorted(hit) == list(range(len(nodes))) and min(cone) > 0
    check(f"kappa = {kap}: det H vanishes exactly at the {len(nodes)} exact nodes and nowhere else, zero is a double level there, each "
          "touching is conical with certified chirality, and elsewhere there are two negative and two positive levels", ok,
          f"{log[-1][3]} uncleared cubes (half-width {h:.1e}) in {len(groups)} groups; counts {sorted(negs)}; one node per box "
          f"{sorted(hit) == list(range(len(nodes)))}; outer levels nonzero {outer}; Hessian PD ({nsub} boxes, pivot >= {min(pivs):.3g}); "
          f"conical: gap >= {min(cone):.3g}|d| in every box; chiralities sign det V {chir}; {time.time() - t0:.0f} s")


for pq in ((1, 10), (3, 10), (7, 20), (9, 20), (12, 25), (3, 5), (4, 5), (1, 1)):
    certificate(*pq)

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
