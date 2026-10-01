#!/usr/bin/env python3
"""Composite-site network, flux-free comparator, J >= 2: the touchings of the middle bands (line, plane (ii), no plane (iii)), exact conditions and a representative certificate.

Supplied u = +1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, couplings J_x = J_y = 1, J_z = J, odd term kappa
(K = kappa^2), four-site Bloch matrix H(f) = i M(f). Exact families of the landed note (2026-09-26) for J_x = J_y = 1:
 (i)   line   (x, 1-x, 0), (1-x, x, 0):   4K c^2 - 2c + J^2 - 4K - 2 = 0,  c = cos 2 pi x   (BOTH roots)
 (ii)  plane  f1 + f2 = 1:  cos 2 pi x = 1 - J/(4K),  cos 2 pi f3 = (J+2)/(4K) - (4+J-J^2)/J
 (iii) plane  f1 + f2 = 2 f3:  cos 2 pi f3 = (J + 2 -+ s)/2 (both signs of s), cos 2 pi g = -J - cos 2 pi f3, s^2 = 5J^2 + 8J + J(J+2)/K.
EXACT (sympy; polynomial identities, rational arithmetic; no floating point): for every J, kappa the six landed vanishing quantities (det H, its three gradient components,
the constant and linear characteristic coefficients) vanish on all three families; at every real family point (J != 0) zero is exactly a double level with outer levels
+-sqrt(tr H^2/2), |outer| >= 2|J| (+-4|J| on the line); the real region of each family for J >= 2: line roots in (-1,1) iff K >= K_+(J) = [(J^2-2) + J sqrt(J^2-4)]/8 (J > 2),
the point Gamma = (0,0,0) at J = 2 (semi-Dirac: Hessian of det H of rank 2, quartic along (1,-1,0)); plane (ii) iff 0 < J < 1 + sqrt 5 and K >= K_c^2 = J(J+2)/[4(4+2J-J^2)] with NO
upper limit (kappa_h^2 = J/[4(2-J)] is irrelevant for J >= 2); plane (iii) never; K_c^2 >= K_+ with equality only at the root J0 = 2.3829... of J^3 - 4J - 4 (the shared root is the
smaller line root c- for J < J0, the larger c+ for J > J0); for J < 0 the line family is that of |J|, no plane (ii), plane (iii) only the point Gamma at J = -2, and J -> -J is no symmetry.
The region formulas are also compared with independent exact Sturm-sequence/rational counts at 7680 rational couplings.
INTERVAL-CERTIFIED (the landed method and code, outward-rounded float arithmetic and mpmath interval functions, interval LDL^* inertia of H(c) -+ r with r rounded up from
lip*h, equal certified negative counts => no level in the cube; Hessian-of-det-H positive definiteness on the cluster boxes => conical; chirality sign det V from the kernel
projector in interval arithmetic) at a REPRESENTATIVE subset only: gapped (5/2, 99/100) just below kappa_+ = 1 and (4, 1); node-bearing (4, 2) (4 line nodes), (5/2, 3/2) (8 nodes)
and (2, 1) (7 nodes including Gamma, where only 'one cluster containing the exact double-zero point' is claimed). Nothing in the certificates is floating-point search.
FLOAT: none in this runner (the floating scans of the exploration are not reproduced here).
Scope: J >= 2, plus the exact J < 0 statements above. Not covered: couplings between the samples, other anisotropies, J = 0, the soft windows near K = K_+ and K = K_c^2,
equality with the spin model, any physical identification.
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import sympy as sp
from mpmath import iv, mp, mpc, mpf
from sympy.polys.matrices import DomainMatrix

AUDIT_TIMEOUT_SEC = 1200

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


# ------------------------------------------------------------------------------------------------ landed definitions (copied verbatim from the landed
# certificate runner, outward-rounded version): network, Bloch terms, interval arithmetic, clearing, exact determinants, Hessian/Cholesky, chirality
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

A_VEC = np.array([[2, 0, 0], [0, 2, 0], [1, 1, 2]])

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
        out[float(v)] = (float(rd(float(cc.a))), float(ru(float(cc.b))),
                         float(rd(float(ss.a))), float(ru(float(ss.b))))
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
    return a, b, n, t, float(ru(float(lip.b)))



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

Dg = sp.expand(det_of(shifted(kk, JJ), [kk, JJ, z1, z2, w]) / (z1 * z2 * w) ** (4 * S))

CPg = sp.expand(det_of(shifted(kk, JJ, True), [kk, JJ, z1, z2, w, mu]) / (z1 * z2 * w) ** (4 * S))



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


# ================================================================================================ exact checks (sympy)
DOM = sp.QQ.frac_field(kk, JJ)
TARGETS = [Dg] + [v * sp.diff(Dg, v) for v in (z1, z2, w)] + [CPg.coeff(mu, 0), CPg.coeff(mu, 1)]
J, K, c = sp.symbols("J K c", real=True)
m_ = sp.symbols("m", positive=True)
q = 4 * K * c ** 2 - 2 * c + J ** 2 - 4 * K - 2
Delta = 16 * K ** 2 - 4 * (J ** 2 - 2) * K + 1                       # quarter discriminant, c = (1 +- sqrt Delta)/(4K)
Kplus = ((J ** 2 - 2) + J * sp.sqrt(J ** 2 - 4)) / 8
Kminus = ((J ** 2 - 2) - J * sp.sqrt(J ** 2 - 4)) / 8
Kc2 = J * (J + 2) / (4 * (4 + 2 * J - J ** 2))
Kh2 = J / (4 * (2 - J))
c1s = 1 - J / (4 * K)
c3s = (J + 2) / (4 * K) - (4 + J - J ** 2) / J
sig = 5 * J ** 2 + 8 * J + J * (J + 2) / K                            # s^2
pt1 = {z1: 1, z2: 1, w: 1}                                           # Gamma


# ---- 1. the three families: landed vanishing as polynomial identities (every kappa, J)
PL = sp.Poly(kk ** 2 * z1 ** 4 - z1 ** 3 + (JJ ** 2 - 2 * kk ** 2 - 2) * z1 ** 2 - z1 + kk ** 2, z1, domain=DOM)
r_line = [sp.simplify(sp.rem(sp.Poly(sp.expand(sp.expand(e.subs({z2: 1 / z1, w: 1})) * z1 ** 10), z1, domain=DOM), PL).as_expr()) for e in TARGETS]
C1, C3 = 1 - JJ / (4 * kk ** 2), (JJ + 2) / (4 * kk ** 2) - (4 + JJ - JJ ** 2) / JJ
G2 = [sp.expand((z1 ** 2 - 2 * C1 * z1 + 1) * 4 * kk ** 2 * JJ), sp.expand((w ** 2 - 2 * C3 * w + 1) * 4 * kk ** 2 * JJ)]
r_p1 = [sp.simplify(sp.reduced(sp.expand(sp.expand(e.subs(z2, 1 / z1)) * z1 ** 10 * w ** 10), G2, z1, w, domain=DOM)[1]) for e in TARGETS]
Cf = (JJ + 2 - sv) / 2
G3 = [sp.expand(w ** 2 - 2 * Cf * w + 1), sp.expand(yv ** 2 - 2 * (-JJ - Cf) * yv + 1), sp.expand((sv ** 2 - 5 * JJ ** 2 - 8 * JJ) * kk ** 2 - JJ * (JJ + 2))]
r_p2 = [sp.simplify(sp.reduced(sp.expand(sp.expand(e.subs({z1: w * yv, z2: w / yv}, simultaneous=True)) * w ** 12 * yv ** 12), G3, w, yv, sv,
                               order="lex", domain=DOM)[1]) for e in TARGETS]
check("1 families: det H, its 3 gradient components, e3, e4 vanish on line, plane (ii), plane (iii) for every kappa, J",
      all(x == 0 for x in r_line + r_p1 + r_p2), "18 remainders = 0 modulo the family polynomials; in (iii) s is the formal root of s^2 = 5J^2 + 8J + J(J+2)/K (both signs)")

# ---- 2. line roots and K_+(J)
dK = sp.discriminant(sp.Poly(Delta, K))
chk = [sp.expand(q.subs(c, 1) - (J ** 2 - 4)), sp.expand(q.subs(c, -1) - J ** 2),
       sp.simplify(sp.expand(q.subs(c, (1 + sp.sqrt(Delta)) / (4 * K)))), sp.simplify(sp.expand(q.subs(c, (1 - sp.sqrt(Delta)) / (4 * K)))),
       sp.simplify(dK - 16 * J ** 2 * (J ** 2 - 4)), sp.simplify(sp.expand(Delta.subs(K, Kplus))), sp.simplify(sp.expand(Delta.subs(K, Kminus))),
       sp.simplify(Kplus * Kminus - sp.Rational(1, 16)), sp.simplify(Kplus.subs(J, 2) - sp.Rational(1, 4)),
       sp.simplify(sp.diff(Kplus, J) * 8 * sp.sqrt(J ** 2 - 4) - (2 * J * sp.sqrt(J ** 2 - 4) + (J ** 2 - 4) + J ** 2))]
check("2 line (i), J > 2: both roots in (-1,1) iff K >= K_+(J), none below (K_+(2) = 1/4, K_+(5/2) = 1, K_+(3) = (7+3 sqrt5)/8, K_+(4) = 7/4 + sqrt3)",
      all(x == 0 for x in chk),
      "q(1) = J^2-4, q(-1) = J^2; Delta = 16K^2-4(J^2-2)K+1, disc_K = 16J^2(J^2-4), K+- roots, K+ K- = 1/16, K_+ increasing; K >= K_+: vertex in (0,1), q(+-1) > 0; K <= K_- < 1/4: q decreasing on [-1,1], q(1) > 0")

# ---- 3. J = 2: the point Gamma and the other line root
D_G = sp.factor(Dg.subs(pt1))
c2root = sp.simplify((J ** 2 - 2 - 4 * K) / (4 * K)).subs(J, 2)      # product of the two roots at J = 2 (one root is 1)
chk = [sp.simplify(D_G - 16 * (JJ - 2) ** 2 * (JJ + 2) ** 2), sp.simplify(q.subs(J, 2) - (c - 1) * (4 * K * (c + 1) - 2)),
       sp.simplify(c2root - (sp.Rational(1, 2) / K - 1)), sp.simplify((sp.Rational(1, 2) / K - 1) - 1 - (1 - 4 * K) / (2 * K)), sp.simplify((sp.Rational(1, 2) / K - 1) + 1 - sp.Rational(1, 2) / K)]
check("3 J = 2: Gamma = (0,0,0) (c = 1) is a line node for every kappa; the other root 1/(2K) - 1 lies in (-1,1) iff K > 1/4; D(Gamma) = 16(J-2)^2(J+2)^2",
      all(x == 0 for x in chk), f"q(c; J=2) = (c-1)(4K(c+1)-2); c2 - 1 = (1-4K)/(2K), c2 + 1 = 1/(2K); D(Gamma) = {D_G}")

# ---- 4. plane (ii)
chk = [sp.simplify(J * (c3s - 1) - (J * (J + 2) / (4 * K) - (4 + 2 * J - J ** 2))), sp.simplify(J * (c3s + 1) - (J * (J + 2) / (4 * K) - (4 - J ** 2))),
       sp.simplify(c3s.subs(K, Kc2) - 1), sp.simplify(c3s.subs(K, Kh2) + 1), sp.simplify(Kc2 - J / 8 - J ** 3 / (8 * (4 + 2 * J - J ** 2))),
       sp.simplify(c1s.subs(J, -J) - (1 + J / (4 * K))), sp.simplify(J * (c3s + 1) - (J * (J + 2) / (4 * K) + (J ** 2 - 4))),
       sp.expand(4 + 2 * J - J ** 2).subs(J, 1 + sp.sqrt(5)).simplify()]
check("4 plane (ii) real iff 0 < J < 1 + sqrt5 and K >= K_c^2 = J(J+2)/[4(4+2J-J^2)], no upper limit for J >= 2 (c3 > -1 always); never for J >= 1 + sqrt5 or J < 0",
      all(x == 0 for x in chk),
      "J(c3-1) = J(J+2)/(4K)-(4+2J-J^2); K_c^2 - J/8 = J^3/[8(4+2J-J^2)] > 0 (c1 in [-1,1] implied); J(c3+1) = J(J+2)/(4K) + J^2 - 4 > 0 for J >= 2; c1 > 1 for J < 0")

# ---- 5. plane (iii)
quad_cw = 4 * c ** 2 - 4 * (J + 2) * c + (J + 2) ** 2 - sig
chk = [sp.simplify(quad_cw.subs(c, (J + 2 + sp.sqrt(sig)) / 2)), sp.simplify(quad_cw.subs(c, (J + 2 - sp.sqrt(sig)) / 2)),
       sp.simplify(3 * J - (J + 4) - 2 * (J - 2)), sp.simplify(sig.subs(J, 2) - (36 + 8 / K)),
       sp.simplify(sig - 9 * J ** 2 - (J * (J + 2) / K - 4 * J * (J - 2))), sp.simplify((J + 4) ** 2 - sig - (16 - 4 * J ** 2 - J * (J + 2) / K)),
       sp.simplify((16 - 4 * J ** 2 - J * (J + 2) / K).subs(K, Kh2))]
check("5 plane (iii) never real for J >= 2, either sign of s: |cw|,|cg| <= 1 needs max(J,3J) <= e s <= min(J+4, 3J+4); for J > 2, 3J > J+4",
      all(x == 0 for x in chk), "at J = 2 it needs s = 6 but s^2 = 36 + 8/K; for 0 < J < 2 it reduces to e = +1, K >= K_h^2 (landed range)")

# ---- 6. ordering K_c^2 >= K_+, birth of (ii), shared root
A_ = sp.simplify(8 * Kc2 - (J ** 2 - 2))
cstar = (J - 2) * (J + 1) / (J + 2)
numP = sp.Poly(J ** 4 - 2 * J ** 3 - 4 * J ** 2 + 8 * J + 8, J)
chk = [sp.simplify(A_ - (J ** 4 - 2 * J ** 3 - 4 * J ** 2 + 8 * J + 8) / (4 + 2 * J - J ** 2)),
       sp.simplify(A_ ** 2 - J ** 2 * (J ** 2 - 4) - 4 * (J ** 3 - 4 * J - 4) ** 2 / (J ** 2 - 2 * J - 4) ** 2),
       sp.simplify(c1s.subs(K, Kc2) - cstar), sp.simplify(q.subs({c: cstar, K: Kc2})), sp.simplify(cstar - 1 / (4 * Kc2) - (J ** 3 - 4 * J - 4) / (J * (J + 2)))]
J0 = sp.CRootOf(J ** 3 - 4 * J - 4, 0)
check("6 K_c^2 >= K_+ on [2, 1+sqrt5), equality only at J0 (root of J^3-4J-4); (ii) is born at K_c^2 from the line root c* = (J-2)(J+1)/(J+2), the smaller root c- for J < J0, the larger c+ for J > J0",
      all(x == 0 for x in chk) and numP.count_roots(2, sp.Rational(33, 10)) == 0 and sp.Poly(J ** 3 - 4 * J - 4, J).count_roots(2, sp.Rational(33, 10)) == 1,
      f"A^2 - J^2(J^2-4) = 4(J^3-4J-4)^2/(J^2-2J-4)^2; quartic J^4-2J^3-4J^2+8J+8 has no root in [2, 3.3] (Sturm); c* - 1/(4K_c^2) = (J^3-4J-4)/(J(J+2)); J0 = {sp.N(J0, 10)}")

# ---- 7. double level and outer levels
e2g = CPg.coeff(mu, 2)
r_e2 = sp.rem(sp.Poly(sp.expand(sp.expand((e2g - 16 * JJ ** 2).subs({z2: 1 / z1, w: 1})) * z1 ** 10), z1, domain=DOM), PL).as_expr()
trM = sp.expand(CPg.coeff(mu, 3))
M03 = sum(amp(kd, kk, JJ) * z1 ** int(n[0]) * z2 ** int(n[1]) * w ** int(n[2]) for (a, b, n, kd) in TERMS if (a, b) == (0, 3))
M30 = sum(amp(kd, kk, JJ) * z1 ** int(n[0]) * z2 ** int(n[1]) * w ** int(n[2]) for (a, b, n, kd) in TERMS if (a, b) == (3, 0))
check("7 every real family point (J != 0) has zero as an EXACT double level, outer levels +-sqrt(tr H^2/2), |outer| >= 2|J|; on the line exactly +-4|J|",
      trM == 0 and sp.simplify(M03 - 2 * JJ / w) == 0 and M30 == 0 and sp.simplify(r_e2) == 0,
      "tr M = 0 and M[0,3] = 2J/z3 only, so tr H^2 >= 8J^2 > 0, and e3 = e4 = 0 there; line: e2 - 16J^2 = 0 modulo the line polynomial")

# ---- 8. Gamma at J = 2: Hessian of det H of rank 2, quartic vanishing along the line
D2_ = Dg.subs(JJ, 2)
zsv = (z1, z2, w)
Nmat = sp.Matrix(3, 3, lambda i, j: sp.simplify((zsv[j] * sp.diff(zsv[i] * sp.diff(D2_, zsv[i]), zsv[j])).subs(pt1)))
Nexp = sp.Matrix([[-128 * (16 * kk ** 2 + 1), -128 * (16 * kk ** 2 + 1), 256], [-128 * (16 * kk ** 2 + 1), -128 * (16 * kk ** 2 + 1), 256], [256, 256, -512]])
grad_G = [sp.simplify((zsv[i] * sp.diff(D2_, zsv[i])).subs(pt1)) for i in range(3)]
cst = sp.symbols("cst")
on_line = sp.simplify((sp.expand(Dg.subs({z2: 1 / z1, w: 1})) - 16 * (JJ ** 2 + 4 * cst ** 2 * kk ** 2 - 2 * cst - 4 * kk ** 2 - 2) ** 2).subs(cst, (z1 + 1 / z1) / 2))
lam = sp.Symbol("lam")
rr = sp.sqrt(256 * kk ** 4 - 32 * kk ** 2 + 9)
check("8 Gamma at J = 2 is semi-Dirac: Hessian of det H in f has rank 2, null vector (1,-1,0); det H on the line = 16(c-1)^2(4K(c+1)-2)^2 ~ x^4 (x^8 at K = 1/4)",
      sp.simplify(Nmat - Nexp) == sp.zeros(3, 3) and sp.simplify(Nmat.det()) == 0 and Nmat.nullspace() == [sp.Matrix([-1, 1, 0])] and all(g == 0 for g in grad_G)
      and sp.expand((16 * kk ** 2 + 3) ** 2 - (256 * kk ** 4 - 32 * kk ** 2 + 9) - 128 * kk ** 2) == 0
      and sp.simplify(Nmat.charpoly(lam).as_expr() - lam * (lam + 128 * (16 * kk ** 2 + 3 + rr)) * (lam + 128 * (16 * kk ** 2 + 3 - rr))) == 0 and on_line == 0,
      "N = sum a m m^T = [[-128(16k^2+1), -128(16k^2+1), 256], [same], [256, 256, -512]], eigenvalues -128[16k^2+3 +- sqrt(256k^4-32k^2+9)] < 0, gradient 0, D|line = 16 q(c)^2")

# ---- 9. J < 0
Dodd = sp.expand((Dg - Dg.subs(JJ, -JJ)) / 2)
nosym = all(sp.expand(Dg.subs({JJ: -JJ, kk: sk * kk, z1: s1 * z1, z2: s2 * z2, w: s3 * w}, simultaneous=True) - Dg) != 0
            for s1, s2, s3, sk in itertools.product((1, -1), repeat=4))
sigm = sp.simplify(sig.subs(J, -m_))
chk = [sp.simplify(sigm + m_ * ((8 - 5 * m_) + (2 - m_) / K)), sp.simplify(m_ * (5 * m_ - 8) - (3 * m_ - 4) ** 2 + 4 * (m_ - 2) ** 2)]
check("9 J < 0: the line is that of |J| (q depends on J^2); no plane (ii) (c1 > 1); plane (iii) real only at J = -2 (the point Gamma); J -> -J is no symmetry of det H",
      all(x == 0 for x in chk) and nosym and Dodd != 0,
      "with m = -J: s^2 < m(5m-8) = (3m-4)^2 - 4(m-2)^2 < (3m-4)^2 blocks e = -1; e = +1 needs m <= 4/3 but s^2 >= 0 needs m > 8/5; all 16 sign changes of (k, z1, z2, w) fail; odd part of det H has "
      f"{len(sp.Add.make_args(Dodd))} terms, proportional to J k^2")


# ---- 10. exact rational cross-check (Sturm sequences / exact rational inequalities) of the closed-form regions
def fam_line(Jv, Kv):
    P = sp.Poly(4 * Kv * c ** 2 - 2 * c + Jv ** 2 - 4 * Kv - 2, c, domain=sp.QQ)
    n_all = P.sqf_part().count_roots(-1, 1)
    nb = int(P.eval(1) == 0) + int(P.eval(-1) == 0)
    return 2 * (n_all - nb) + nb


def pred_line(Jv, Kv):
    a = abs(Jv)
    if a < 2:
        return 1 if Jv == 0 else 2
    if a == 2:
        return 1 + (2 if Kv > Fr(1, 4) else 0)
    Dl = 16 * Kv ** 2 - 4 * (Jv ** 2 - 2) * Kv + 1
    if Dl < 0 or Kv <= Fr(1, 4):
        return 0
    return 2 if Dl == 0 else 4


def fam_ii(Jv, Kv):
    cc1 = 1 - Jv / (4 * Kv)
    cc3 = (Jv + 2) / (4 * Kv) - (4 + Jv - Jv ** 2) / Jv
    if abs(cc1) > 1 or abs(cc3) > 1:
        return 0
    return (1 if abs(cc1) == 1 else 2) * (1 if abs(cc3) == 1 else 2)


def pred_ii(Jv, Kv):
    if Jv <= 0 or 4 + 2 * Jv - Jv ** 2 <= 0:
        return 0
    if Kv < Jv * (Jv + 2) / (4 * (4 + 2 * Jv - Jv ** 2)):
        return 0
    if Jv < 2 and Kv > Jv / (4 * (2 - Jv)):
        return 0
    cc1 = 1 - Jv / (4 * Kv)
    cc3 = (Jv + 2) / (4 * Kv) - (4 + Jv - Jv ** 2) / Jv
    return (1 if abs(cc1) == 1 else 2) * (1 if abs(cc3) == 1 else 2)


def fam_iii(Jv, Kv):
    s2 = 5 * Jv ** 2 + 8 * Jv + Jv * (Jv + 2) / Kv
    lo, hi = max(Fr(-1), -Jv - 1), min(Fr(1), 1 - Jv)
    if lo > hi:
        return 0
    P = sp.Poly(4 * c ** 2 - 4 * (Jv + 2) * c + (Jv + 2) ** 2 - s2, c, domain=sp.QQ)
    sq = P.sqf_part()
    rlo, rhi = sp.Rational(lo.numerator, lo.denominator), sp.Rational(hi.numerator, hi.denominator)
    if sq.count_roots(rlo, rhi) == 0:
        return 0
    tot = 0
    for r in sq.real_roots():
        if rlo <= r <= rhi:
            cwv, cgv = r, -sp.Rational(Jv.numerator, Jv.denominator) - r
            tot += (1 if abs(cwv) == 1 else 2) * (1 if abs(cgv) == 1 else 2)
    return tot


def pred_iii(Jv, Kv):
    s2 = 5 * Jv ** 2 + 8 * Jv + Jv * (Jv + 2) / Kv
    if s2 < 0:
        return 0
    tot = 0
    for e in (1, -1):
        lo = max(Jv, 3 * Jv); hi = min(Jv + 4, 3 * Jv + 4)
        slo, shi = (max(lo, 0), hi) if e == 1 else (max(-hi, 0), -lo)
        if slo > shi or shi < 0 or not (slo ** 2 <= s2 <= shi ** 2) or (e == -1 and s2 == 0):
            continue
        hits = lambda val: ((e == 1) == (val >= 0) or val == 0) and s2 == val ** 2
        tot += (1 if (hits(Jv) or hits(Jv + 4)) else 2) * (1 if (hits(3 * Jv) or hits(3 * Jv + 4)) else 2)
    return tot


bad = {"line": 0, "ii": 0, "iii": 0}
npts = 0
for Jv in [Fr(n, 8) for n in range(-48, 49) if n != 0]:
    for Kv in [Fr(n, 20) ** 2 for n in range(1, 81)]:
        npts += 1
        bad["line"] += fam_line(sp.Rational(Jv.numerator, Jv.denominator), sp.Rational(Kv.numerator, Kv.denominator)) != pred_line(Jv, Kv)
        bad["ii"] += fam_ii(Jv, Kv) != pred_ii(Jv, Kv)
        bad["iii"] += fam_iii(Jv, Kv) != pred_iii(Jv, Kv)
check("10 closed-form real regions = independent exact counts (Sturm / rational inequalities) of distinct real family points at all rational couplings below",
      sum(bad.values()) == 0, f"{npts} couplings (J = n/8 in [-6,6] without 0, kappa = n/20 in (0,4]); mismatches line {bad['line']}, plane (ii) {bad['ii']}, plane (iii) {bad['iii']}")


# ================================================================================================ interval certificates at representative couplings
mp.dps = 40
iv.dps = 30


def expected_nodes(Jq, kap):
    """Real family points for J >= 2 (exact bookkeeping with sympy Rationals, interval enclosures of the node coordinates): both line roots, plane (ii)."""
    K_ = kap ** 2
    Ki, Ji = ivq(K_), ivq(Jq)
    nodes = []
    acos_x = lambda e_iv, e_sp: enclose_acos(e_iv, mp.acos(sp.N(e_sp, 50)) / (2 * mp.pi))
    Dl = 1 + 8 * K_ + 16 * K_ ** 2 - 4 * K_ * Jq ** 2
    if Dl > 0:
        for e in (-1, 1):
            c_sp = (1 + e * sp.sqrt(Dl)) / (4 * K_)
            if c_sp == 1:
                nodes.append(("Gamma", (iv.mpf(0), iv.mpf(0), iv.mpf(0))))
            elif -1 < c_sp < 1:
                c_iv = (1 + e * iv.sqrt(1 + 8 * Ki + 16 * Ki ** 2 - 4 * Ki * Ji ** 2)) / (4 * Ki)
                xl = acos_x(c_iv, c_sp)
                nodes += [("line", (xl, 1 - xl, iv.mpf(0))), ("line", (1 - xl, xl, iv.mpf(0)))]
    if 4 + 2 * Jq - Jq ** 2 > 0 and K_ > Jq * (Jq + 2) / (4 * (4 + 2 * Jq - Jq ** 2)):
        c1, c3 = 1 - Jq / (4 * K_), (Jq + 2) / (4 * K_) - (4 + Jq - Jq ** 2) / Jq
        xo, fo = acos_x(ivq(c1), c1), acos_x(ivq(c3), c3)
        nodes += [("ii", (xo, 1 - xo, fo)), ("ii", (xo, 1 - xo, 1 - fo)), ("ii", (1 - xo, xo, fo)), ("ii", (1 - xo, xo, 1 - fo))]
    return nodes


def certificate(Jq, kq, want_nodes, levels=13):
    """Clearing + node bookkeeping. Returns (ok, detail)."""
    t0 = time.time()
    Jq, kap = sp.Rational(Jq), sp.Rational(kq)
    K_ = kap ** 2
    nodes = expected_nodes(Jq, kap)
    Cs, h, lip, log, negs = clear((1.0, 1.0, float(Jq)), float(kap), levels=levels, verbose=False)
    if not nodes:
        Kp_ = ((Jq ** 2 - 2) + Jq * sp.sqrt(Jq ** 2 - 4)) / 8
        ok = want_nodes == 0 and len(Cs) == 0 and negs == {2} and K_ < Kp_
        return ok, (f"gapped: K = {K_} < K_+ = {sp.N(Kp_, 8)} (no family node); {len(log)} levels, {len(Cs)} cubes left, every cleared cube has 2 negative levels "
                    f"(counts {sorted(negs)}), lip {lip:.1f}; {time.time() - t0:.0f} s")
    D = sp.expand(Dg.subs({kk: kap, JJ: Jq}))
    tl = [((m[0] - 8, m[1] - 8, m[2] - 8), sp.Rational(cf)) for m, cf in sp.Poly(sp.expand(D * (z1 * z2 * w) ** 8), z1, z2, w).terms()]
    outer = all(not (r[0].a <= 0 <= r[0].b and r[1].a <= 0 <= r[1].b) for r in (outer_nonzero(kap, Jq, nd) for _, nd in nodes))
    chir = [chirality(kap, Jq, list(nd)) for _, nd in nodes]
    groups = clusters(Cs, h) if len(Cs) else []
    NH = float(sum((2 if a == b else 1) * abs(float(amp(kd, kap, Jq))) for (a, b, n, kd) in TERMS)) + 1e-9
    hit, pivs, cone = [], [], []
    ok_boxes = True
    for gi in groups:
        X = Cs[gi].copy(); X = X - np.round(X - X[0])
        lo, hi = X.min(axis=0) - h, X.max(axis=0) + h
        mid = (lo + hi) / 2
        inside = [i for i, (fam, nd) in enumerate(nodes)
                  if all(nd[j].a - round(float(nd[j].a) - mid[j]) >= lo[j] and nd[j].b - round(float(nd[j].a) - mid[j]) <= hi[j] for j in range(3))]
        hit += inside
        ok_boxes &= len(inside) == 1
        if len(inside) == 1 and nodes[inside[0]][0] == "Gamma":
            continue                                            # Hessian of det H singular at Gamma: no conical claim, only 'one cluster contains the exact double zero'
        pd, st = pd_box(tl, lo, hi)
        pivs.append(st["minpiv"] if pd else float("nan"))
        m = st["minpiv"] / 4 if pd else 0.0
        while pd and m > 1e-9 and not pd_box(tl, lo, hi, shift=m)[0]:
            m /= 4
        shift_ok = pd and pd_box(tl, lo, hi, shift=m)[0]
        cone.append(float(rd(float((iv.sqrt(2 * iv.mpf(m)) / iv.mpf(NH)).a))) if shift_ok else 0.0)
    string = "".join("+" if x > 0 else "-" if x < 0 else "0" for x in chir)
    ok = (len(nodes) == want_nodes and negs == {2} and len(groups) == len(nodes) and ok_boxes and sorted(hit) == list(range(len(nodes))) and outer
          and sum(chir) == 0 and all(x != 0 for (f_, _), x in zip(nodes, chir) if f_ != "Gamma") and (not cone or min(cone) > 0) and len(pivs) == len(cone)
          and all(p == p for p in pivs))
    gam = any(f_ == "Gamma" for f_, _ in nodes)
    return ok, (f"{len(nodes)} nodes ({sum(f_ == 'line' for f_, _ in nodes)} line, {sum(f_ == 'ii' for f_, _ in nodes)} plane (ii)" + (", Gamma" if gam else "")
                + f"); {len(log)} levels, {len(Cs)} cubes left in {len(groups)} clusters, 1 node each, counts {sorted(negs)}, outer levels != 0; chirality {string}, sum {sum(chir)}; "
                + (f"min Hessian pivot {min(pivs):.3g}, gap >= {min(cone):.2g}|f-f*| at every non-Gamma node; " if cone else "")
                + (f"Gamma: no conical claim; " if gam else "") + f"{time.time() - t0:.0f} s")


for (Jc, kc, wn, tag) in ((sp.Rational(5, 2), sp.Rational(99, 100), 0, "just below kappa_+ = 1"), (4, 1, 0, "gapped"),
                          (4, 2, 4, "4 line nodes, both roots"), (sp.Rational(5, 2), sp.Rational(3, 2), 8, "8 nodes"), (2, 1, 7, "Gamma + 2 line + 4 plane (ii)")):
    ok_c, det_c = certificate(Jc, kc, wn)
    check(f"cert (J, kappa) = ({Jc}, {kc}) {tag}", ok_c, det_c)

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
