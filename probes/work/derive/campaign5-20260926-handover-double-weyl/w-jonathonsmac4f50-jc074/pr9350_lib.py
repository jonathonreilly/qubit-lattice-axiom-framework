"""Vendored, unchanged, from PR #9350 head 33a59fa50271dedd41632bc5ca51b1ec44899ae3,
scripts/composite_site_network_flux_free_middle_band_touchings_two_below_kappa_star_and_six_above_interval_certificate_2026_09_26.py
(lines 25-359 and 423-528: definitions only; the module-level checks and the certificate loop are omitted). Author: the PR's worker."""
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


