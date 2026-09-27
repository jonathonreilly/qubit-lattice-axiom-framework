#!/usr/bin/env python3
"""Composite-site network, flux-free comparator: exact touchings of the middle bands, two below kappa_c and six above.

Supplied u = +1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, couplings
J_x = J_y = 1, J_z = J, odd term kappa, four-site Bloch matrix H(f) = i M(f) over the fractional zone. A computer-assisted
certificate:
(A) exact rational algebra (sympy, polynomial-ring determinants), for every kappa and J: D = det H, its three momentum derivatives and
    the constant and linear characteristic-polynomial coefficients vanish on three families of points, the line f = (x, 1 - x, 0)
    with 4k^2 c^2 - 2c + J^2 - 4k^2 - 2 = 0 (c = cos 2 pi x), the plane f1 + f2 = 1 with cos 2 pi x = 1 - J/(4k^2),
    cos 2 pi f3 = (J + 2)/(4k^2) - (4 + J - J^2)/J, and the plane f1 + f2 = 2 f3 with f = (f3 + g, f3 - g, f3),
    cos 2 pi f3 = (J + 2 - s)/2, cos 2 pi g = -J - cos 2 pi f3, s = sqrt(5J^2 + 8J + J(J + 2)/k^2);
(B) rigorous clearing: interval enclosures of H at exact dyadic cube centres (mpmath interval phases, outward-rounded IEEE float
    arithmetic) and interval LDL^T inertia show that outside small boxes every cube has exactly two negative and two positive levels,
    none within lip h of zero (the landed Lipschitz bound and Weyl's inequality carry this to the whole cube);
(C) each box contains exactly one family node, where the outer levels are nonzero (interval evaluation), and the Hessian of D is
    positive definite on the whole box (centred interval forms with bisection, interval Cholesky), so D > 0 there except at the node;
    Hessian - m I positive definite gives a middle gap >= sqrt(2m)/||H||_bound |f - f*| on the box (conical touching);
(D) at each node the chirality sign det V, V the Pauli coefficients of P dH P with P = (H^2 - tr(H) H + q)/q the kernel projector,
    is certified from det V = Im Tr(P d1H P d2H P d3H)/2 in interval arithmetic; the chiralities sum to zero.
Checks: (1) enclosure sanity; (2)-(4) the three exact families; (5)-(17) certificates at J = 1, kappa = 1/10, 3/10, 7/20, 9/20, 12/25,
3/5, 4/5, 1; J = 1/2, kappa = 1/5, 2/5; J = 3/2, kappa = 2/5, 7/10, 1. Couplings between the samples are not certified here.
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

AUDIT_TIMEOUT_SEC = 2400

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



# ------------------------------------------------------------------------------------------------ exact algebra, J_x = J_y = 1, J_z = J
z1, z2, w, kk, JJ, mu, yv, sv = sp.symbols("z1 z2 w k J mu y s")
S = 2
_T1 = terms((1.0, 1.0, 1.0), 0.3)
_T2 = terms((1.0, 1.0, 1.5), 0.3)
KIND = ["xy" if abs(t1 - 2.0) < 1e-12 and abs(t2 - 2.0) < 1e-12 else ("z" if abs(t1 - 2.0) < 1e-12 else "odd") for (_, _, _, t1), (_, _, _, t2) in zip(_T1, _T2)]
TERMS = [(a, b, n, kd) for (a, b, n, _), kd in zip(_T1, KIND)]
assert max(abs(int(x)) for tm in TERMS for x in tm[2]) <= S


def amp(kd, kap, J):
    return {"xy": 2, "z": 2 * J, "odd": 2 * kap}[kd]


def shifted(kap, J, withmu=False):
    """(z1 z2 w)^S M with exact amplitudes 2, 2J and 2 kappa (optionally + mu on the diagonal)."""
    Ms = [[sp.Integer(0)] * 4 for _ in range(4)]
    for (a, b, n, kd) in TERMS:
        tt = amp(kd, kap, J)
        e = [int(x) for x in n]
        Ms[a][b] += tt * z1 ** (S + e[0]) * z2 ** (S + e[1]) * w ** (S + e[2])
        Ms[b][a] -= tt * z1 ** (S - e[0]) * z2 ** (S - e[1]) * w ** (S - e[2])
    if withmu:
        for i in range(4):
            Ms[i][i] += mu * (z1 * z2 * w) ** S
    return Ms


def det_of(Ms, gens):
    R = sp.QQ[gens]
    return R.to_sympy(DomainMatrix([[R.from_sympy(sp.expand(x)) for x in r] for r in Ms], (4, 4), R).det())


# ---------------------------------------------------------------- 1. enclosure sanity (J = 1, kappa = 3/10)
a_, b_, n_, t_, lip_ = build(terms((1.0, 1.0, 1.0), 0.3))
rng = np.random.default_rng(0)
pts = np.floor(rng.random((400, 3)) * 2 ** 20) / 2 ** 20
A_ = H_intervals(pts, a_, b_, n_, t_)
mp.dps = 40
miss = 0
for s_ in range(20):
    f = [mpf(float(x)) for x in pts[s_]]
    M = [[mpc(0)] * 4 for _ in range(4)]
    for (a, b, n, kd) in TERMS:
        tt = mpf(amp(kd, sp.Rational(3, 10), 1).p) / amp(kd, sp.Rational(3, 10), 1).q if kd == "odd" else mpf(2)
        th = 2 * mp.pi * sum(f[j] * int(n[j]) for j in range(3))
        M[a][b] += tt * mp.expj(th); M[b][a] -= tt * mp.expj(-th)
    for (i, j), e in A_.items():
        hij = mpc(0, 1) * M[i][j]
        miss += not (e.re.lo[s_] <= hij.real <= e.re.hi[s_] and (i == j or e.im.lo[s_] <= hij.imag <= e.im.hi[s_]))
Hf = np.zeros((len(pts), 4, 4), dtype=complex)
ph = np.exp(2j * np.pi * pts @ n_.T)
for j, (a, b, n, kd) in enumerate(TERMS):
    tt = 0.6 if kd == "odd" else 2.0
    Hf[:, a, b] += 1j * tt * ph[:, j]; Hf[:, b, a] -= 1j * tt * np.conj(ph[:, j])
ev = np.linalg.eigvalsh(Hf)
agree = []
for m_ in (-1.0, 0.0, 0.37, 2.5):
    ng, ok = inertia_neg(A_, m_)
    agree.append(bool(ok.all()) and np.mean(ng == (ev < m_).sum(axis=1)))
check("interval Bloch matrices contain 40-digit entries at 20 dyadic points; interval inertia matches floating eigenvalue counts "
      "at 400 points and four shifts (J = 1, kappa = 3/10)", miss == 0 and min(agree) == 1.0, f"outside {miss}; agreement {min(agree):.3f}")

# ---------------------------------------------------------------- 2.-4. exact node families for every kappa and J
Dg = sp.expand(det_of(shifted(kk, JJ), [kk, JJ, z1, z2, w]) / (z1 * z2 * w) ** (4 * S))
CPg = sp.expand(det_of(shifted(kk, JJ, True), [kk, JJ, z1, z2, w, mu]) / (z1 * z2 * w) ** (4 * S))
DOM = sp.QQ.frac_field(kk, JJ)
TARGETS = [Dg] + [v * sp.diff(Dg, v) for v in (z1, z2, w)] + [CPg.coeff(mu, 0), CPg.coeff(mu, 1)]
PL = sp.Poly(kk ** 2 * z1 ** 4 - z1 ** 3 + (JJ ** 2 - 2 * kk ** 2 - 2) * z1 ** 2 - z1 + kk ** 2, z1, domain=DOM)
r_line = [sp.simplify(sp.rem(sp.Poly(sp.expand(sp.expand(e.subs({z2: 1 / z1, w: 1})) * z1 ** 10), z1, domain=DOM), PL).as_expr()) for e in TARGETS]
cst = sp.symbols("c")
landed = sp.simplify((sp.expand(Dg.subs({z2: 1 / z1, w: 1})) - 16 * (JJ ** 2 + 4 * cst ** 2 * kk ** 2 - 2 * cst - 4 * kk ** 2 - 2) ** 2).subs(cst, (z1 + 1 / z1) / 2))
lam = sp.symbols("lam")
Mr = sp.zeros(4, 4)
for (a, b, n, kd) in TERMS:
    phs = sp.I ** int(n[0]) * (-sp.I) ** int(n[1]) * (-1) ** int(n[2])      # e^{2 pi i f.n} at (1/4, 3/4, 1/2)
    Mr[a, b] += amp(kd, kk, 1) * phs; Mr[b, a] -= amp(kd, kk, 1) * sp.conjugate(phs)
rat = sp.expand((sp.I * Mr - lam * sp.eye(4)).det() - (lam ** 2 - 48 * (sp.Rational(1, 2) - kk) ** 2) * (lam ** 2 - 48 * (sp.Rational(1, 2) + kk) ** 2))
check("line family, every kappa and J: at the roots of k^2 z^4 - z^3 + (J^2 - 2k^2 - 2) z^2 - z + k^2 on f = (x, 1 - x, 0) the determinant, "
      "its three momentum derivatives and the constant and linear characteristic coefficients vanish; D on the line is the landed "
      "16[J^2 + 4c^2k^2 - 2c - 4k^2 - 2]^2 and at J = 1 the (1/4, 3/4, 1/2) polynomial is the landed one",
      all(x == 0 for x in r_line) and landed == 0 and rat == 0, f"remainders {r_line}; rational-point difference {rat}")
C1, C3 = 1 - JJ / (4 * kk ** 2), (JJ + 2) / (4 * kk ** 2) - (4 + JJ - JJ ** 2) / JJ
G2 = [sp.expand((z1 ** 2 - 2 * C1 * z1 + 1) * 4 * kk ** 2 * JJ), sp.expand((w ** 2 - 2 * C3 * w + 1) * 4 * kk ** 2 * JJ)]
r_p1 = [sp.simplify(sp.reduced(sp.expand(sp.expand(e.subs(z2, 1 / z1)) * z1 ** 10 * w ** 10), G2, z1, w, domain=DOM)[1]) for e in TARGETS]
check("first plane family, every kappa and J: on f1 + f2 = 1 at cos 2 pi x = 1 - J/(4k^2), cos 2 pi f3 = (J + 2)/(4k^2) - (4 + J - J^2)/J "
      "the same six quantities vanish", all(x == 0 for x in r_p1), f"remainders {r_p1}")
Cf = (JJ + 2 - sv) / 2
G3 = [sp.expand(w ** 2 - 2 * Cf * w + 1), sp.expand(yv ** 2 - 2 * (-JJ - Cf) * yv + 1), sp.expand((sv ** 2 - 5 * JJ ** 2 - 8 * JJ) * kk ** 2 - JJ * (JJ + 2))]
r_p2 = [sp.simplify(sp.reduced(sp.expand(sp.expand(e.subs({z1: w * yv, z2: w / yv}, simultaneous=True)) * w ** 12 * yv ** 12), G3, w, yv, sv,
                               order="lex", domain=DOM)[1]) for e in TARGETS]
check("second plane family, every kappa and J: at f = (f3 + g, f3 - g, f3) with cos 2 pi f3 = (J + 2 - s)/2, cos 2 pi g = -J - cos 2 pi f3, "
      "s = sqrt(5J^2 + 8J + J(J + 2)/k^2), the same six quantities vanish", all(x == 0 for x in r_p2), f"remainders {r_p2}; {time.time() - T0:.0f} s")


# ---------------------------------------------------------------- 5.-17. certificates
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




def outer_nonzero(kap, J, node):
    """Interval value (real, imaginary) of the quadratic characteristic coefficient (the product of the outer levels up to sign)."""
    poly = sp.Poly(sp.expand(CPg.coeff(mu, 2).subs({kk: kap, JJ: J}) * (z1 * z2 * w) ** 8), z1, z2, w)
    re_, im_ = iv.mpf(0), iv.mpf(0)
    for (p1, p2, p3), cf in poly.terms():
        ang = 2 * iv.pi * ((p1 - 8) * node[0] + (p2 - 8) * node[1] + (p3 - 8) * node[2])
        cf = sp.Rational(cf); c_ = iv.mpf(cf.p) / iv.mpf(cf.q)
        re_ += c_ * iv.cos(ang); im_ += c_ * iv.sin(ang)
    return re_, im_


def ivq(r):
    r = sp.Rational(r)
    return iv.mpf(r.p) / iv.mpf(r.q)


def chirality(kap, J, f):
    """sign det V at the node enclosure f: det V = Im Tr(P d1H P d2H P d3H)/2, P = (H^2 - tr(H) H + q)/q (interval arithmetic)."""
    Zm = lambda: [[iv.mpc(0) for _ in range(4)] for _ in range(4)]
    M, dM = Zm(), [Zm(), Zm(), Zm()]
    for (a, b, n, kd) in TERMS:
        tt = ivq(amp(kd, kap, J))
        th = 2 * iv.pi * sum(int(n[j]) * f[j] for j in range(3))
        e = iv.mpc(iv.cos(th), iv.sin(th)); ec = iv.mpc(iv.cos(th), -iv.sin(th))
        M[a][b] += tt * e; M[b][a] -= tt * ec
        for j in range(3):
            c = 2 * iv.pi * int(n[j])
            dM[j][a][b] += tt * e * iv.mpc(0, 1) * c; dM[j][b][a] -= tt * ec * iv.mpc(0, -1) * c
    I_ = iv.mpc(0, 1)
    H = [[I_ * M[r][c] for c in range(4)] for r in range(4)]
    dH = [[[I_ * dM[j][r][c] for c in range(4)] for r in range(4)] for j in range(3)]
    mm = lambda A, B: [[sum((A[r][k] * B[k][c] for k in range(4)), iv.mpc(0)) for c in range(4)] for r in range(4)]
    tr = sum((H[i][i] for i in range(4)), iv.mpc(0))
    q = sum((H[i][i] * H[j][j] - H[i][j] * H[j][i] for i in range(4) for j in range(i + 1, 4)), iv.mpc(0))
    H2 = mm(H, H)
    P = [[(H2[r][c] - tr * H[r][c] + (q if r == c else iv.mpc(0))) / q for c in range(4)] for r in range(4)]
    T = mm(mm(mm(P, dH[0]), mm(P, dH[1])), mm(P, dH[2]))
    dv = sum((T[i][i] for i in range(4)), iv.mpc(0)).imag / 2
    return 1 if dv.a > 0 else (-1 if dv.b < 0 else 0)


def certificate(J, kap, levels=13):
    t0 = time.time()
    J, kap = sp.Rational(J), sp.Rational(kap)
    Cs, h, lip, log, negs = clear((1.0, 1.0, float(J)), float(kap), levels=levels, verbose=False)
    D = sp.expand(Dg.subs({kk: kap, JJ: J}))
    tl = [((m[0] - 8, m[1] - 8, m[2] - 8), sp.Rational(c)) for m, c in sp.Poly(sp.expand(D * (z1 * z2 * w) ** 8), z1, z2, w).terms()]
    mp.dps = 40; iv.dps = 30
    k2 = kap ** 2
    Ki, Ji = ivq(k2), ivq(J)
    root = lambda e_iv, e_sp: enclose_acos(e_iv, mp.acos(sp.N(e_sp, 50)) / (2 * mp.pi))
    cl = (1 - sp.sqrt(1 + 8 * k2 + 16 * k2 ** 2 - 4 * k2 * J ** 2)) / (4 * k2)
    xl = root((1 - iv.sqrt(1 + 8 * Ki + 16 * Ki ** 2 - 4 * Ki * Ji ** 2)) / (4 * Ki), cl)
    nodes = [(xl, 1 - xl, iv.mpf(0)), (1 - xl, xl, iv.mpf(0))]
    kc2, kh2 = J * (J + 2) / (4 * (4 + 2 * J - J ** 2)), J / (4 * (2 - J))
    if kc2 < k2 < kh2:
        c1, c3 = 1 - J / (4 * k2), (J + 2) / (4 * k2) - (4 + J - J ** 2) / J
        xo, fo = root(ivq(c1), c1), root(ivq(c3), c3)
        nodes += [(xo, 1 - xo, fo), (xo, 1 - xo, 1 - fo), (1 - xo, xo, fo), (1 - xo, xo, 1 - fo)]
    elif k2 > kh2:
        sq_sp = sp.sqrt(5 * J ** 2 + 8 * J + J * (J + 2) / k2)
        sq_iv = iv.sqrt(5 * Ji ** 2 + 8 * Ji + Ji * (Ji + 2) / Ki)
        F = root((Ji + 2 - sq_iv) / 2, (J + 2 - sq_sp) / 2)
        G = root(-Ji - (Ji + 2 - sq_iv) / 2, -J - (J + 2 - sq_sp) / 2)
        nodes += [(sf * F + sg * G, sf * F - sg * G, sf * F) for sf in (1, -1) for sg in (1, -1)]
    outer = all((lambda r: not (r[0].a <= 0 <= r[0].b and r[1].a <= 0 <= r[1].b))(outer_nonzero(kap, J, nd)) for nd in nodes)
    chir = [chirality(kap, J, list(nd)) for nd in nodes]
    groups = clusters(Cs, h)
    ok = negs == {2} and len(groups) == len(nodes) and outer and 0 not in chir and sum(chir) == 0
    hit, pivs, cone = [], [], []
    NH = float(sum((2 if a == b else 1) * abs(float(amp(kd, kap, J))) for (a, b, n, kd) in TERMS)) + 1e-9
    for gi in groups:
        X = Cs[gi].copy(); X = X - np.round(X - X[0])
        lo, hi = X.min(axis=0) - h, X.max(axis=0) + h
        mid = (lo + hi) / 2
        inside = [i for i, nd in enumerate(nodes)
                  if all(nd[j].a - round(float(nd[j].a) - mid[j]) >= lo[j] and nd[j].b - round(float(nd[j].a) - mid[j]) <= hi[j] for j in range(3))]
        pd, st = pd_box(tl, lo, hi)
        ok &= pd and len(inside) == 1
        hit += inside; pivs.append(st["minpiv"])
        m = st["minpiv"] / 4 if pd else 0.0             # Hess - m I positive definite: D >= (m/2)|d|^2, gap >= sqrt(2m)|d|/||H||
        while pd and m > 1e-9 and not pd_box(tl, lo, hi, shift=m)[0]:
            m /= 4
        cone.append(0.99 * float(mp.sqrt(2 * mpf(m)) / mpf(NH)) if pd else 0.0)
    ok &= sorted(hit) == list(range(len(nodes))) and min(cone) > 0
    check(f"J = {J}, kappa = {kap}: exactly the {len(nodes)} family nodes; double, conical, chiral", ok,
          f"{log[-1][3]} cubes/{len(groups)} groups, counts {sorted(negs)}, outer {outer}, pivot >= {min(pivs):.3g}, gap >= {min(cone):.2g}|d|, "
          f"chirality {''.join('+' if c > 0 else '-' for c in chir)}; {time.time() - t0:.0f} s")


for Jk in ((1, "1/10"), (1, "3/10"), (1, "7/20"), (1, "9/20"), (1, "12/25"), (1, "3/5"), (1, "4/5"), (1, 1),
           ("1/2", "1/5"), ("1/2", "2/5"), ("3/2", "2/5"), ("3/2", "7/10"), ("3/2", 1)):
    certificate(*Jk)

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
