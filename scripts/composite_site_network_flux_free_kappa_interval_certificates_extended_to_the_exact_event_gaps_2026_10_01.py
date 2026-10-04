#!/usr/bin/env python3
"""Composite-site network, flux-free comparator: kappa-interval certificates extended toward the exact special couplings kappa_c and kappa_h.

Supplied u = +1 quadratic Majorana comparator (one copy, landed hopping-sign convention), couplings (Jx, Jy, Jz), odd term kappa, four-site Bloch
matrix H(f; kappa) = i M(f; kappa).  A certified kappa-cell [a, b] (couplings rational) means, for EVERY kappa in [a, b]: det H vanishes in the zone
exactly at the exact family nodes (J_x = J_y = 1: three landed families; J_x != J_y: the line family alone), each a double zero with outer levels of
opposite sign, conical with an explicit constant, with a constant chirality sign (the signs sum to zero), and H has two negative and two positive
levels everywhere else.  Cells are tiled along kappa; cells that contain kappa_c^2 = J(J+2)/[4(4+2J-J^2)] or kappa_h^2 = J/[4(2-J)] are refused.

Method (the earlier hierarchical kappa-interval certificate, with three changes and one extension):
 1. coarse clearing of boxes (f-cube) x [a, b] by interval LDL^T after the congruence with a float eigenbasis (Q^dagger Q is enclosed and checked
    diagonally dominant, so Sylvester's law applies); the uncleared cubes form one blob per node tube (tubes = interval evaluation of the exact
    cosine formulas); per blob and kappa sub-cell a frame moving with the node; one cluster; interval Hessian of det H positive definite on the sheared
    hull with the node tube inside; e2 < 0 and chirality sign from interval arithmetic on adaptive kappa sub-ranges; sub-cells tile the cell exactly.
 2. NEW (symmetry): det(M + mu) is invariant (exact sympy, kappa symbolic) under f -> -f and f1 <-> f2.  The frame stage is run for one node of each
    orbit; for every other node the statement is transported by the coordinate map g: every leaf box of the representative, mapped by g, is checked
    (interval arithmetic) to contain the node tube of the image node.  Spectra at f and g(f) coincide, so the negative-level counts, the strict
    convexity of D and the zero of D in the image hull are the images of the representative's.
 3. NEW (first-order f-Taylor): inside a cube the f-variation is no longer a Weyl radius lip * h on all levels; the family
    {H0 + sum_j delta_j W_j + s K + s^2 K2/2 + E : |delta_j| <= h, |s| <= rho, ||E|| <= r}, W_j = d_j H, is tested by interval LDL^T after the eigenbasis
    congruence, with r a rigorous bound (ray Taylor, ftaylor_remainder) on the delta-delta, delta-s and joint third-order remainder.
 4. EXTENSION (anisotropy): amplitudes (2 Jx, 2 Jy, 2 Jz, 2 kappa); for Jx != Jy just the line family exists below the flip coupling (regime check by an
    interval enclosure of kappa_c^2 = u_+ from the exact resultant closed form).

Tiers.  EXACT (sympy / Fractions / Q(sqrt(-5), sqrt(15)) arithmetic, no floating point): the node families, the symmetries, the special-coupling
identities, D and its derivatives at the merged points, kappa = 0.  INTERVAL-CERTIFIED with outward rounding (one-ulp outward steps on IEEE
operations, mpmath interval cos/sin with outward float conversion, exact Fractions for couplings and kappa endpoints): clearing, Hessian, tubes, e2,
chirality, cone constants, symmetry-image inclusions, remainder bounds.  FLOAT, no claim attached: the eigenbasis Q, the frame velocity v0, the choice
of sub-cell widths and levels (they affect efficiency alone), the sampled-remainder diagnostic and the coverage cells that are not re-run here.
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time
from fractions import Fraction

import numpy as np
import sympy as sp
from mpmath import iv, mp, mpc, mpf
from sympy.polys.matrices import DomainMatrix

AUDIT_TIMEOUT_SEC = 900

mp.dps = 40
iv.dps = 30

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


# ================================================================================================ library (kgap_lib.py)
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


def reduce(p):
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


_T1 = terms((1.0, 2.0, 3.0), 0.7)


KIND = [{2.0: "x", 4.0: "y", 6.0: "z"}.get(round(t1, 9), "odd") for (_, _, _, t1) in _T1]


TERMS = [(a, b, tuple(int(x) for x in n), kd) for (a, b, n, _), kd in zip(_T1, KIND)]


S = 2


NTERM = len(TERMS)


def clusters(C, h):
    """Connected groups of uncleared cubes (touching or diagonal neighbours, periodic zone)."""
    n = int(round(0.5 / h))
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
    """Real interval arrays [lo, hi]; every operation rounds outward by one ulp."""
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
    """Outward enclosures of cos and sin of 2 pi v for exactly representable floats v."""
    out = {}
    for v in values:
        x = iv.mpf(mpf(float(v)))
        a = 2 * iv.pi * x
        cc, ss = iv.cos(a), iv.sin(a)
        out[float(v)] = (float(rd(float(cc.a))), float(ru(float(cc.b))), float(rd(float(ss.a))), float(ru(float(ss.b))))
    return out


def inertia_neg(A, mu):
    """Number of negative pivots of A - mu I (interval LDL^T) and ok (False where a pivot interval contains zero)."""
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
            s = A[(k, i)].conj()
            for j in range(k):
                s = s - (L[(i, j)] * L[(k, j)].conj()).rmul(d[j])
            L[(i, k)] = C(s.re.div(safe), s.im.div(safe))
    return neg, ok


def qint(r):
    """Outward float interval of a rational (exact when the float is exact)."""
    r = Fraction(r)
    f = float(r)
    if Fraction(f) == r:
        return (f, f)
    return (float(np.nextafter(f, -np.inf)), float(np.nextafter(f, np.inf)))


def jt(J):
    """Couplings (Jx, Jy, Jz) as Fractions: a scalar J means (1, 1, J)."""
    if isinstance(J, (tuple, list)):
        return tuple(Fraction(x) for x in J)
    return (Fraction(1), Fraction(1), Fraction(J))


def amp_intervals(J, klo, khi):
    """Float intervals (lo, hi) of the hopping amplitudes: 2 Jx, 2 Jy, 2 Jz, [2 klo, 2 khi]."""
    Jx, Jy, Jz = jt(J)
    amp = {"x": Jx, "y": Jy, "z": Jz}
    out = []
    for (a, b, n, kd) in TERMS:
        if kd == "odd":
            out.append((qint(2 * Fraction(klo))[0], qint(2 * Fraction(khi))[1]))
        else:
            out.append(qint(2 * amp[kd]))
    return out


def lip_bounds(tflt):
    """Two rigorous bounds lip_A, lip_B with ||H(f) - H(f')|| <= lip * ||f - f'||_inf (H = iM, Hermitian).
    A: landed termwise bound, sum over terms of fac * t * 2 pi ||n||_1 (fac = 2 for diagonal terms).
    B: for a Hermitian matrix ||A||_2 <= max absolute row sum.  The entry (a,b) of sum_j d_j dM/df_j is bounded by the sum over the
       terms mapped to (a,b) or (b,a) of t 2 pi |d.n|; the maximum over |d_j| <= 1 of this convex function is attained at a sign vertex.
    Returns floats rounded up."""
    A = iv.mpf(0)
    for (a, b, n, kd), (tl, th) in zip(TERMS, tflt):
        fac = 2 if a == b else 1
        A += fac * iv.mpf(th) * 2 * iv.pi * sum(abs(x) for x in n)
    lipA = float(ru(float(A.b)))
    best = iv.mpf(0)
    for s in itertools.product((1, -1), repeat=3):
        E = [[iv.mpf(0)] * 4 for _ in range(4)]
        for (a, b, n, kd), (tl, th) in zip(TERMS, tflt):
            val = iv.mpf(th) * 2 * iv.pi * abs(sum(si * ni for si, ni in zip(s, n)))
            E[a][b] += val
            E[b][a] += val
        for a in range(4):
            row = sum(E[a], iv.mpf(0))
            if row.b > best.b:
                best = row
    lipB = float(ru(float(best.b)))
    return lipA, lipB


def H_intervals(Cs, tflt):
    """Upper-triangle complex-interval entries of H(c) = i M(c) for every centre c, amplitudes tflt (interval tuples)."""
    N = len(Cs)
    nn = np.array([x[2] for x in TERMS], dtype=np.int64)
    vals = np.mod(Cs @ nn.T.astype(float), 1.0)
    uniq = np.unique(vals)
    tab = phase_table(uniq)
    look = np.array([tab[float(v)] for v in uniq])
    idx = np.searchsorted(uniq, vals)
    cl, ch, sl, sh = look[idx, 0], look[idx, 1], look[idx, 2], look[idx, 3]
    zero = lambda: I(np.zeros(N))
    Mre = {(i, j): zero() for i in range(4) for j in range(4)}
    Mim = {(i, j): zero() for i in range(4) for j in range(4)}
    for j, (a, b, n, kd) in enumerate(TERMS):
        tt = I(np.full(N, tflt[j][0]), np.full(N, tflt[j][1]))
        cs = I(cl[:, j], ch[:, j]); sn = I(sl[:, j], sh[:, j])
        Mre[(a, b)] = Mre[(a, b)] + tt * cs
        Mim[(a, b)] = Mim[(a, b)] + tt * sn
        Mre[(b, a)] = Mre[(b, a)] - tt * cs
        Mim[(b, a)] = Mim[(b, a)] + tt * sn
    A = {}
    for i in range(4):
        for j in range(i, 4):
            A[(i, j)] = C(-Mim[(i, j)], Mre[(i, j)])
    return A


def ivr(q):
    q = Fraction(q)
    return iv.mpf(q.numerator) / iv.mpf(q.denominator)


def ivrange(lo, hi):
    a, b = ivr(lo), ivr(hi)
    return iv.mpf([a.a, b.b])


def acos_br(c, pad=mpf(10) ** -25):
    """Enclosure of x in (0, 1/2) with cos 2 pi x in the interval c (an iv.mpf inside (-1, 1)): x in [xl, xh] where
    cos 2 pi x is decreasing, so x(c.b) <= x <= x(c.a); both ends verified by interval cos."""
    if not (c.a > -1 and c.b < 1):
        raise ValueError("cosine interval not inside (-1, 1)")
    two_pi = 2 * mp.pi
    for _ in range(8):
        xl = mp.acos(c.b) / two_pi - pad
        xh = mp.acos(c.a) / two_pi + pad
        okl = iv.cos(2 * iv.pi * iv.mpf(xl)).a > c.b
        okh = iv.cos(2 * iv.pi * iv.mpf(xh)).b < c.a
        if okl and okh and xl > 0 and xh < mpf(1) / 2:
            return iv.mpf([xl, xh])
        pad *= 1000
    raise ValueError("acos enclosure failed")


def ivneg(x):
    return iv.mpf([-x.b, -x.a])


def uplus_enclosure(Jx, Jy, Jz):
    """Interval enclosure of the flip coupling kappa_c^2 = u_+ = (N0 + N1 sqrt(Delta_F))/Den for rational (Jx, Jy, Jz) (closed form of the exact
    resultant computation), evaluated with outward-rounded interval arithmetic."""
    s_, P = Jx + Jy, Jx * Jy
    N0 = (s_ * s_ - 2 * P - Jz * Jz) * (2 * Jz ** 3 * P - 4 * Jz * P * s_ * s_ + Jz * s_ ** 4 - 4 * P * s_ ** 3 + s_ ** 5)
    N1 = 2 * Jz * Jz * P - Jz * Jz * s_ * s_ - 4 * P * s_ * s_ + s_ ** 4
    Den = -8 * (s_ * s_ + Jz * s_ - Jz * Jz) * (Jz ** 3 - 4 * P * s_ + s_ ** 3)
    a2 = P * (s_ + Jz)
    a1 = s_ * (s_ * s_ + Jz * s_ - 2 * P)
    a0 = (P + Jz * s_ + Jz * Jz) * (s_ - Jz)
    DF = a1 * a1 - 4 * a2 * a0
    if not DF > 0:
        raise ValueError("Delta_F not positive")
    return (ivr(N0) + ivr(N1) * iv.sqrt(ivr(DF))) / ivr(Den)


def regime(J, klo, khi):
    """Exact regime of the cell.  Isotropic (Jx = Jy = 1, Jz = J): 'a' (kappa^2 < kappa_c^2: line nodes alone), 'b' (kappa_c^2 < k^2 < kappa_h^2),
    'c' (k^2 > kappa_h^2), None when the cell contains kappa_c or kappa_h (or is outside the formulas' range).
    Anisotropic (Jx != Jy or Jx != 1): just 'a' = line nodes below the flip coupling u_+ (|Jx - Jy| < Jz < Jx + Jy and |Jx^2 - Jy^2| < Jz^2, and
    khi^2 below an interval lower bound of u_+); None otherwise."""
    Jx, Jy, Jz = jt(J)
    klo, khi = Fraction(klo), Fraction(khi)
    if Jx == 1 and Jy == 1:
        J = Jz
        if not (0 < J < 2 and 0 < klo < khi):
            return None
        kc2 = J * (J + 2) / (4 * (4 + 2 * J - J * J))
        kh2 = J / (4 * (2 - J))
        if khi * khi < kc2:
            return "a"
        if klo * klo > kc2 and khi * khi < kh2:
            return "b"
        if klo * klo > kh2:
            return "c"
        return None
    if not (Jx > 0 and Jy > 0 and Jz > 0 and 0 < klo < khi):
        return None
    if not (abs(Jx - Jy) < Jz < Jx + Jy and abs(Jx * Jx - Jy * Jy) < Jz * Jz):
        return None
    up = uplus_enclosure(Jx, Jy, Jz)
    return "a" if ivr(khi * khi).b < up.a else None


def iv_hull(xs):
    """Interval hull of a list of mpmath intervals (exact endpoint comparison)."""
    from mpmath.libmp import mpf_gt, mpf_lt
    lo, hi = xs[0]._mpi_
    for x in xs[1:]:
        if mpf_lt(x._mpi_[0], lo):
            lo = x._mpi_[0]
        if mpf_gt(x._mpi_[1], hi):
            hi = x._mpi_[1]
    return iv.make_mpf((lo, hi))


def node_tubes(J, klo, khi, step=None):
    """Interval enclosures (lists of three iv.mpf coordinates, mod 1) of the exact family nodes for every kappa in [klo, khi].
    With `step`, the range is cut into equal pieces of width <= step and the hulls of the piece enclosures are returned (the closed formulas
    are evaluated with interval arithmetic, whose dependency inflation grows with the range width; the hull of narrow pieces is much tighter)."""
    klo_, khi_ = Fraction(klo), Fraction(khi)
    if step is not None and khi_ - klo_ > Fraction(step):
        n = -((klo_ - khi_) // Fraction(step))
        subs = [node_tubes(J, klo_ + (khi_ - klo_) * i / n, klo_ + (khi_ - klo_) * (i + 1) / n) for i in range(int(n))]
        return [(subs[0][t][0], [iv_hull([sb[t][1][j] for sb in subs]) for j in range(3)]) for t in range(len(subs[0]))]
    reg = regime(J, klo, khi)
    if reg is None:
        raise ValueError("cell contains kappa_c or kappa_h (or is outside 0 < J < 2)")
    K = ivrange(klo, khi)
    K2 = K ** 2
    K4 = K ** 4
    Jx_, Jy_, Jz_ = jt(J)
    Ji = ivr(Jz_)
    Pq, Sq = Jx_ * Jy_, Jx_ * Jx_ + Jy_ * Jy_ - Jz_ * Jz_         # q(c) = 4 u c^2 - 2 P c - (4 u + S), u = kappa^2
    nodes = []
    disc = ivr(Pq) ** 2 + 16 * K4 + 4 * K2 * ivr(Sq)
    if not disc.a > 0:
        raise ValueError("line discriminant not positive on the cell")
    cl = -(4 * K2 + ivr(Sq)) / (ivr(Pq) + iv.sqrt(disc))      # = (P - sqrt(disc))/(4 K^2), K^2 cancelled analytically
    xl = acos_br(cl)
    zero = iv.mpf(0)
    nodes += [("line", [xl, 1 - xl, zero]), ("line", [1 - xl, xl, zero])]
    if reg == "b":
        c1 = 1 - Ji / (4 * K2)
        c3 = (Ji + 2) / (4 * K2) - (4 + Ji - Ji * Ji) / Ji
        xo, fo = acos_br(c1), acos_br(c3)
        nodes += [("ii", [xo, 1 - xo, fo]), ("ii", [xo, 1 - xo, 1 - fo]), ("ii", [1 - xo, xo, fo]), ("ii", [1 - xo, xo, 1 - fo])]
    elif reg == "c":
        sq = iv.sqrt(5 * Ji * Ji + 8 * Ji + Ji * (Ji + 2) / K2)
        cF = (Ji + 2 - sq) / 2
        cG = -Ji - cF
        F, G = acos_br(cF), acos_br(cG)
        for sf in (1, -1):
            for sg in (1, -1):
                fa = F if sf == 1 else ivneg(F)
                ga = G if sg == 1 else ivneg(G)
                nodes.append(("iii", [fa + ga, fa - ga, fa]))
    return nodes


def tubes_disjoint(nodes):
    """Every pair of tube boxes is disjoint on the torus (some coordinate has disjoint intervals for every integer shift)."""
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            sep = False
            for k in range(3):
                A, B = nodes[i][1][k], nodes[j][1][k]
                if all((A.b < B.a + s) or (B.b + s < A.a) for s in range(-3, 4)):
                    sep = True
                    break
            if not sep:
                return False
    return True


_kk, _z1, _z2, _w, _mu = sp.symbols("k z1 z2 w mu")


def shifted(J, withmu=False):
    """(z1 z2 w)^S M with exact amplitudes 2, 2J and 2 k (k symbolic, J rational), optionally + mu on the diagonal."""
    Jr = [sp.Rational(x.numerator, x.denominator) for x in jt(J)]
    Ms = [[sp.Integer(0)] * 4 for _ in range(4)]
    for (a, b, n, kd) in TERMS:
        tt = {"x": 2 * Jr[0], "y": 2 * Jr[1], "z": 2 * Jr[2], "odd": 2 * _kk}[kd]
        Ms[a][b] += tt * _z1 ** (S + n[0]) * _z2 ** (S + n[1]) * _w ** (S + n[2])
        Ms[b][a] -= tt * _z1 ** (S - n[0]) * _z2 ** (S - n[1]) * _w ** (S - n[2])
    if withmu:
        for i in range(4):
            Ms[i][i] += _mu * (_z1 * _z2 * _w) ** S
    return Ms


def det_of(Ms, gens):
    R = sp.QQ[gens]
    return R.to_sympy(DomainMatrix([[R.from_sympy(sp.expand(x)) for x in r] for r in Ms], (4, 4), R).det())


def D_terms(J):
    """D = det H(f; kappa) = sum_m a_m(kappa) cos(2 pi m.f) (D is even), kept on a half lattice (m ~ -m merged).
    Returns dict m -> list of (q, Fraction coefficient of kappa^q) with the doubling of merged pairs included; m = 0 is dropped
    (it does not enter the Hessian)."""
    Dsh = sp.expand(det_of(shifted(J), [_kk, _z1, _z2, _w]))
    P = sp.Poly(Dsh, _z1, _z2, _w, _kk)
    full = {}
    for (p1, p2, p3, q), c in P.terms():
        m = (p1 - 4 * S, p2 - 4 * S, p3 - 4 * S)
        full.setdefault(m, {})
        full[m][q] = full[m].get(q, Fraction(0)) + Fraction(int(sp.Rational(c).p), int(sp.Rational(c).q))
    # evenness check: coefficient of m equals the coefficient of -m
    for m, d in full.items():
        dm = full.get(tuple(-x for x in m), {})
        keys = set(d) | set(dm)
        assert all(d.get(k, 0) == dm.get(k, 0) for k in keys), "D is not even"
    half = {}
    for m, d in full.items():
        if m == (0, 0, 0):
            continue
        mm = tuple(-x for x in m)
        if m < mm:                                          # keep one of each pair, coefficient doubled (cos is even)
            half[m] = sorted((q, 2 * c) for q, c in d.items() if c != 0)
    return half, full


def coeff_intervals(half, klo, khi):
    """Enclosures a_m(K), K = [klo, khi], by the mean-value form a(km) + a'(K) [-rho, rho] (km, rho exact rationals)."""
    klo, khi = Fraction(klo), Fraction(khi)
    km = (klo + khi) / 2
    rho = ivr((khi - klo) / 2)
    Ki = ivrange(klo, khi)
    sym = iv.mpf([-rho.b, rho.b])
    out = []
    for m, tl in half.items():
        a0 = sum((c * km ** q for q, c in tl), Fraction(0))
        da = iv.mpf(0)
        for q, c in tl:
            if q > 0:
                da += ivr(c) * q * Ki ** (q - 1)
        out.append((m, ivr(a0) + da * sym))
    return out


def _bloch_iv(Kiv, J, f):
    """Interval Bloch matrix H = iM and its f-derivatives at the f-box f (list of three iv.mpf), kappa in Kiv."""
    Jxi, Jyi, Jzi = [ivr(x) for x in jt(J)]
    Zm = lambda: [[iv.mpc(0) for _ in range(4)] for _ in range(4)]
    M, dM = Zm(), [Zm(), Zm(), Zm()]
    for (a, b, n, kd) in TERMS:
        tt = {"x": 2 * Jxi, "y": 2 * Jyi, "z": 2 * Jzi, "odd": 2 * Kiv}[kd]
        th = 2 * iv.pi * sum(n[j] * f[j] for j in range(3))
        e = iv.mpc(iv.cos(th), iv.sin(th)); ec = iv.mpc(iv.cos(th), -iv.sin(th))
        M[a][b] += tt * e; M[b][a] -= tt * ec
        for j in range(3):
            c = 2 * iv.pi * n[j]
            dM[j][a][b] += tt * e * iv.mpc(0, 1) * c; dM[j][b][a] -= tt * ec * iv.mpc(0, -1) * c
    I_ = iv.mpc(0, 1)
    H = [[I_ * M[r][c] for c in range(4)] for r in range(4)]
    dH = [[[I_ * dM[j][r][c] for c in range(4)] for r in range(4)] for j in range(3)]
    return H, dH


def outer_and_chirality(J, klo, khi, nodes):
    """For one kappa range and its node tubes: (True iff e2 = sum of principal 2x2 minors of H excludes zero on every tube (the outer
    levels are nonzero), list of chirality signs from Im Tr(P d1H P d2H P d3H)/2 in interval arithmetic, 0 if undecided)."""
    Kiv = ivrange(klo, khi)
    outer_ok, chir = True, []
    mm = lambda A, B: [[sum((A[r][k] * B[k][c] for k in range(4)), iv.mpc(0)) for c in range(4)] for r in range(4)]
    for kind, f in nodes:
        H, dH = _bloch_iv(Kiv, J, f)
        tr = sum((H[i][i] for i in range(4)), iv.mpc(0))
        q = sum((H[i][i] * H[j][j] - H[i][j] * H[j][i] for i in range(4) for j in range(i + 1, 4)), iv.mpc(0))
        # e2 is real (sum of principal 2x2 minors of a Hermitian matrix): require it strictly negative, i.e. the two outer levels have opposite signs
        nz = bool(q.real.b < 0) and (q.imag.a <= 0 <= q.imag.b)
        outer_ok &= bool(nz)
        if not nz:
            chir.append(0)
            continue
        H2 = mm(H, H)
        P = [[(H2[r][c] - tr * H[r][c] + (q if r == c else iv.mpc(0))) / q for c in range(4)] for r in range(4)]
        T = mm(mm(mm(P, dH[0]), mm(P, dH[1])), mm(P, dH[2]))
        dv = sum((T[i][i] for i in range(4)), iv.mpc(0)).imag / 2
        chir.append(1 if dv.a > 0 else (-1 if dv.b < 0 else 0))
    return outer_ok, chir


def second_deriv_bound(tflt_hi, v0):
    """B2 >= sup over s of ||phi''(s)||, phi(s) = H(c + s v0, kappa_m + s), for every centre c and every s with kappa_m + s <= khi
    (amplitudes tflt_hi taken at khi).  Per term the second derivative of t(kappa) e^{i theta} is (2 t' i w + t (i w)^2) e^{i theta} with
    w = 2 pi n.v0, t' = 2 for odd terms, 0 otherwise; the entry bound is the sum over the terms mapped to (a,b) or (b,a) and the norm of a
    Hermitian matrix is at most its maximal absolute row sum.  Returns a float rounded up."""
    E = [[iv.mpf(0)] * 4 for _ in range(4)]
    for (a, b, n, kd), (tl, th) in zip(TERMS, tflt_hi):
        nv = sum(n[j] * iv.mpf(float(v0[j])) for j in range(3))
        w = 2 * iv.pi * abs(nv)
        tp = 2 if kd == "odd" else 0
        val = 2 * tp * w + iv.mpf(th) * w * w
        E[a][b] += val
        E[b][a] += val
    best = iv.mpf(0)
    for a in range(4):
        row = sum(E[a], iv.mpf(0))
        if row.b > best.b:
            best = row
    return float(ru(float(best.b)))


def _term_amp(tflt_m, v0):
    """Float intervals (lo, hi) of A_re = t' and A_im = 2 pi t (n.v0) for every term (K amplitude A = A_re + i A_im)."""
    out = []
    for (a, b, n, kd), (tl, th) in zip(TERMS, tflt_m):
        nv = sum(n[j] * iv.mpf(float(v0[j])) for j in range(3))
        aim = 2 * iv.pi * iv.mpf([tl, th]) * nv
        out.append((2.0 if kd == "odd" else 0.0, float(rd(float(aim.a))), float(ru(float(aim.b)))))
    return out


def H_and_K(Cs, tflt_m, v0):
    """Upper-triangle complex-interval entries of H(c, kappa_m) = i M and of K(c) = d/ds H(c + s v0, kappa_m + s)|_{s=0} for every centre."""
    N = len(Cs)
    nn = np.array([x[2] for x in TERMS], dtype=np.int64)
    vals = np.mod(Cs @ nn.T.astype(float), 1.0)
    uniq = np.unique(vals)
    tab = phase_table(uniq)
    look = np.array([tab[float(v)] for v in uniq])
    idx = np.searchsorted(uniq, vals)
    cl, ch, sl, sh = look[idx, 0], look[idx, 1], look[idx, 2], look[idx, 3]
    zero = lambda: I(np.zeros(N))
    Mre = {(i, j): zero() for i in range(4) for j in range(4)}
    Mim = {(i, j): zero() for i in range(4) for j in range(4)}
    Kre = {(i, j): zero() for i in range(4) for j in range(4)}
    Kim = {(i, j): zero() for i in range(4) for j in range(4)}
    amps = _term_amp(tflt_m, v0)
    for j, (a, b, n, kd) in enumerate(TERMS):
        tt = I(np.full(N, tflt_m[j][0]), np.full(N, tflt_m[j][1]))
        cs = I(cl[:, j], ch[:, j]); sn = I(sl[:, j], sh[:, j])
        Mre[(a, b)] = Mre[(a, b)] + tt * cs
        Mim[(a, b)] = Mim[(a, b)] + tt * sn
        Mre[(b, a)] = Mre[(b, a)] - tt * cs
        Mim[(b, a)] = Mim[(b, a)] + tt * sn
        ar = I(np.full(N, amps[j][0]))
        ai = I(np.full(N, amps[j][1]), np.full(N, amps[j][2]))
        zre = ar * cs - ai * sn
        zim = ar * sn + ai * cs
        Kre[(a, b)] = Kre[(a, b)] + zre
        Kim[(a, b)] = Kim[(a, b)] + zim
        Kre[(b, a)] = Kre[(b, a)] - zre
        Kim[(b, a)] = Kim[(b, a)] + zim
    A, K = {}, {}
    for i in range(4):
        for j in range(i, 4):
            A[(i, j)] = C(-Mim[(i, j)], Mre[(i, j)])
            K[(i, j)] = C(-Kim[(i, j)], Kre[(i, j)])
    return A, K


def _cfull(A, a, b):
    return A[(a, b)] if a <= b else A[(b, a)].conj()


def _cpoint_mul(X, qr, qi):
    """Complex interval X times the exact complex number qr + i qi (float arrays)."""
    Qr, Qi = I(qr), I(qi)
    return C(X.re * Qr - X.im * Qi, X.re * Qi + X.im * Qr)


def _conjq_mul(qr, qi, Y):
    """conj(q) * Y for the exact complex q and complex interval Y."""
    Qr, Qi = I(qr), I(qi)
    return C(Qr * Y.re + Qi * Y.im, Qr * Y.im - Qi * Y.re)


def _cadd(a, b):
    return b if a is None else a + b


def congruence(Xfull, Qr, Qi):
    """Upper triangle of Q^dagger X Q for a Hermitian complex-interval matrix given by Xfull(a, b) and exact Q = Qr + i Qi, Q[..., a, k]."""
    N = Qr.shape[0]
    Y = {}
    for a in range(4):
        for k in range(4):
            acc = None
            for b in range(4):
                acc = _cadd(acc, _cpoint_mul(Xfull(a, b), Qr[:, b, k], Qi[:, b, k]))
            Y[(a, k)] = acc
    T = {}
    for j in range(4):
        for k in range(j, 4):
            acc = None
            for a in range(4):
                acc = _cadd(acc, _conjq_mul(Qr[:, a, j], Qi[:, a, j], Y[(a, k)]))
            T[(j, k)] = acc
    return T


def _abs_hi(x):
    return np.maximum(np.abs(x.lo), np.abs(x.hi))


def K_norm_bound(tflt_hi, v0):
    """Rigorous bound on ||K(f)|| (K = d/ds H(f + s v0, kappa + s)) for every f: per term |A| <= t' + 2 pi t_hi |n.v0|, maximal absolute row sum."""
    E = [[iv.mpf(0)] * 4 for _ in range(4)]
    for (a, b, n, kd), (tl, th) in zip(TERMS, tflt_hi):
        nv = sum(n[j] * iv.mpf(float(v0[j])) for j in range(3))
        val = (2 if kd == "odd" else 0) + iv.mpf(th) * 2 * iv.pi * abs(nv)
        E[a][b] += val
        E[b][a] += val
    best = iv.mpf(0)
    for a in range(4):
        row = sum(E[a], iv.mpf(0))
        if row.b > best.b:
            best = row
    return float(ru(float(best.b)))


def third_deriv_bound(tflt_hi, v0):
    """B3 >= sup ||phi'''(s)||, phi(s) = H(c + s v0, kappa_m + s): per term |3 t' (i w)^2 + t (i w)^3| <= 3 t' w^2 + t w^3 (t''' = t'' = 0),
    w = 2 pi n.v0; entry bound summed over the terms mapped to (a,b) or (b,a); Hermitian => norm <= maximal absolute row sum."""
    E = [[iv.mpf(0)] * 4 for _ in range(4)]
    for (a, b, n, kd), (tl, th) in zip(TERMS, tflt_hi):
        nv = sum(n[j] * iv.mpf(float(v0[j])) for j in range(3))
        w = 2 * iv.pi * abs(nv)
        tp = 2 if kd == "odd" else 0
        val = 3 * tp * w * w + iv.mpf(th) * w * w * w
        E[a][b] += val
        E[b][a] += val
    best = iv.mpf(0)
    for a in range(4):
        row = sum(E[a], iv.mpf(0))
        if row.b > best.b:
            best = row
    return float(ru(float(best.b)))


def _term_amp2(tflt_m, v0):
    """Second-derivative amplitude A2 = 2 t' i w - t w^2 per term: float intervals of (re_lo, re_hi, im) with w = 2 pi n.v0."""
    out = []
    for (a, b, n, kd), (tl, th) in zip(TERMS, tflt_m):
        nv = sum(n[j] * iv.mpf(float(v0[j])) for j in range(3))
        w = 2 * iv.pi * nv
        tt = iv.mpf([tl, th])
        re = -tt * w * w
        im = (4 * w) if kd == "odd" else iv.mpf(0)           # 2 t' w with t' = 2
        out.append((float(rd(float(re.a))), float(ru(float(re.b))), float(rd(float(im.a))), float(ru(float(im.b)))))
    return out


def H_K_K2(Cs, tflt_m, v0, want2=True):
    """Upper-triangle entries of H(c, kappa_m), K = phi'(0), K2 = phi''(0) for phi(s) = H(c + s v0, kappa_m + s)."""
    A, K = H_and_K(Cs, tflt_m, v0)
    if not want2:
        return A, K, None
    N = len(Cs)
    nn = np.array([x[2] for x in TERMS], dtype=np.int64)
    vals = np.mod(Cs @ nn.T.astype(float), 1.0)
    uniq = np.unique(vals)
    tab = phase_table(uniq)
    look = np.array([tab[float(v)] for v in uniq])
    idx = np.searchsorted(uniq, vals)
    cl, ch, sl, sh = look[idx, 0], look[idx, 1], look[idx, 2], look[idx, 3]
    zero = lambda: I(np.zeros(N))
    Kre = {(i, j): zero() for i in range(4) for j in range(4)}
    Kim = {(i, j): zero() for i in range(4) for j in range(4)}
    amps = _term_amp2(tflt_m, v0)
    for j, (a, b, n, kd) in enumerate(TERMS):
        cs = I(cl[:, j], ch[:, j]); sn = I(sl[:, j], sh[:, j])
        ar = I(np.full(N, amps[j][0]), np.full(N, amps[j][1]))
        ai = I(np.full(N, amps[j][2]), np.full(N, amps[j][3]))
        zre = ar * cs - ai * sn
        zim = ar * sn + ai * cs
        Kre[(a, b)] = Kre[(a, b)] + zre
        Kim[(a, b)] = Kim[(a, b)] + zim
        Kre[(b, a)] = Kre[(b, a)] - zre
        Kim[(b, a)] = Kim[(b, a)] + zim
    K2 = {}
    for i in range(4):
        for j in range(i, 4):
            K2[(i, j)] = C(-Kim[(i, j)], Kre[(i, j)])
    return A, K, K2


def precond_clear2(Cs, tflt_m, v0, r, rho_up, second):
    """As precond_clear, with the second-order term: family {H(c) + delta K + delta^2/2 K2 : |delta| <= rho}; r must include the third-order
    remainder rho^3 B3 / 6 (the caller's responsibility) when second is True."""
    N = len(Cs)
    A, K, K2 = H_K_K2(Cs, tflt_m, v0, second)
    Hf = np.zeros((N, 4, 4), dtype=complex)
    for i in range(4):
        for j in range(i, 4):
            z = 0.5 * (A[(i, j)].re.lo + A[(i, j)].re.hi) + 1j * 0.5 * (A[(i, j)].im.lo + A[(i, j)].im.hi)
            if i == j:
                Hf[:, i, i] = z.real
            else:
                Hf[:, i, j] = z; Hf[:, j, i] = np.conj(z)
    _, Q = np.linalg.eigh(Hf)
    Qr, Qi = np.ascontiguousarray(Q.real), np.ascontiguousarray(Q.imag)
    T0 = congruence(lambda a, b: _cfull(A, a, b), Qr, Qi)
    W = congruence(lambda a, b: _cfull(K, a, b), Qr, Qi)
    W2 = congruence(lambda a, b: _cfull(K2, a, b), Qr, Qi) if second else None
    one = {}
    for j in range(4):
        for k in range(j, 4):
            acc = None
            for a in range(4):
                acc = _cadd(acc, _conjq_mul(Qr[:, a, j], Qi[:, a, j], C(I(Qr[:, a, k]), I(Qi[:, a, k]))))
            one[(j, k)] = acc
    sok = np.ones(N, dtype=bool)
    for j in range(4):
        off = np.zeros(N)
        for k in range(4):
            if k != j:
                s = one[(min(j, k), max(j, k))]
                off = ru(ru(off + _abs_hi(s.re)) + _abs_hi(s.im))
        sok &= one[(j, j)].re.lo > ru(off)
    rr = I(np.array([-rho_up]), np.array([rho_up]))
    r2 = I(np.array([0.0]), np.array([float(ru(0.5 * rho_up * rho_up))]))
    res = []
    for mu in (r, -r):
        M = I(np.array([mu]))
        Tm = {}
        for j in range(4):
            for k in range(j, 4):
                re = T0[(j, k)].re - M * one[(j, k)].re + rr * W[(j, k)].re
                if second:
                    re = re + r2 * W2[(j, k)].re
                if j == k:
                    im = I(np.zeros(N))
                else:
                    im = T0[(j, k)].im - M * one[(j, k)].im + rr * W[(j, k)].im
                    if second:
                        im = im + r2 * W2[(j, k)].im
                Tm[(j, k)] = C(re, im)
        ng, ok = inertia_neg(Tm, 0.0)
        res.append((ng, ok))
    (ngp, okp), (ngm, okm) = res
    return ngp, ngm, okp & okm & sok


def H_W(Cs, tflt_m, jdir):
    """Upper-triangle complex-interval entries of W_j = d/df_j H(c, kappa_m) (H = iM), j = jdir, for every centre c."""
    N = len(Cs)
    nn = np.array([x[2] for x in TERMS], dtype=np.int64)
    vals = np.mod(Cs @ nn.T.astype(float), 1.0)
    uniq = np.unique(vals)
    tab = phase_table(uniq)
    look = np.array([tab[float(v)] for v in uniq])
    idx = np.searchsorted(uniq, vals)
    cl, ch, sl, sh = look[idx, 0], look[idx, 1], look[idx, 2], look[idx, 3]
    zero = lambda: I(np.zeros(N))
    Wre = {(i, j): zero() for i in range(4) for j in range(4)}
    Wim = {(i, j): zero() for i in range(4) for j in range(4)}
    for j, (a, b, n, kd) in enumerate(TERMS):
        if n[jdir] == 0:
            continue
        tl, th = tflt_m[j]
        aim = 2 * iv.pi * iv.mpf([tl, th]) * n[jdir]
        ai = I(np.full(N, float(rd(float(aim.a)))), np.full(N, float(ru(float(aim.b)))))
        cs = I(cl[:, j], ch[:, j]); sn = I(sl[:, j], sh[:, j])
        zre = I(np.zeros(N)) - ai * sn
        zim = ai * cs
        Wre[(a, b)] = Wre[(a, b)] + zre
        Wim[(a, b)] = Wim[(a, b)] + zim
        Wre[(b, a)] = Wre[(b, a)] - zre
        Wim[(b, a)] = Wim[(b, a)] + zim
    return {(i, j): C(-Wim[(i, j)], Wre[(i, j)]) for i in range(4) for j in range(i, 4)}


def ftaylor_remainder(tflt_hi, v0, h, rho_up):
    """Rigorous bound (float, rounded up) on the operator norm of the remainder Rem(delta, s) of
        Phi(delta, s) = H(c + delta + s v0, kappa_m + s) = H0 + sum_j delta_j W_j + s K + s^2 K2 / 2 + Rem,   |delta_j| <= h, |s| <= rho,
    where W_j = d_j H, K = d_s Phi, K2 = d_s^2 Phi at (0, 0).  Taylor along the ray r -> Phi(r delta, r s): Rem = C + R3 with the quadratic
    delta-delta and the delta-s cross terms C and the joint third-order remainder R3 (integral form, sup norm / 6).  Per term t e^{i theta}
    (t' = 2 for odd terms, t'' = 0), with wd = 2 pi h |n|_1, nv = |n . v0|, ws = 2 pi rho nv, wmax = wd + ws:
        |C| <= t wd^2 / 2 + rho wd (t' + t 2 pi nv),    |R3| <= (t wmax^3 + 3 t' rho wmax^2) / 6.
    Entry bound per term summed over the terms mapped to (a, b) or (b, a); norm of a Hermitian matrix <= maximal absolute row sum."""
    E = [[iv.mpf(0)] * 4 for _ in range(4)]
    hh, rr = iv.mpf(float(h)), iv.mpf(float(rho_up))
    for (a, b, n, kd), (tl, th) in zip(TERMS, tflt_hi):
        n1 = sum(abs(x) for x in n)
        nv = abs(sum(n[j] * iv.mpf(float(v0[j])) for j in range(3)))
        tp = 2 if kd == "odd" else 0
        t = iv.mpf(th)
        wd = 2 * iv.pi * hh * n1
        ws = 2 * iv.pi * rr * nv
        wmax = wd + ws
        val = t * wd * wd / 2 + rr * wd * (tp + t * 2 * iv.pi * nv) + (t * wmax ** 3 + 3 * tp * rr * wmax ** 2) / 6
        E[a][b] += val
        E[b][a] += val
    best = iv.mpf(0)
    for a in range(4):
        row = sum(E[a], iv.mpf(0))
        if row.b > best.b:
            best = row
    return float(ru(float(best.b)))


def precond_clear3(Cs, tflt_m, v0, r, rho_up, second, h_up):
    """As precond_clear2 with the first-order f-variation carried in the eigenbasis family:
        {H0 + sum_j delta_j W_j + s K + s^2 K2 / 2 + E : |delta_j| <= h, |s| <= rho, ||E|| <= r}
    where r bounds the remainder (ftaylor_remainder).  Interval LDL of Q^dagger(.)Q - mu Q^dagger Q at mu = +-r with the interval multipliers
    [-h, h] (the W_j), [-rho, rho] (K) and [0, rho^2/2] (K2)."""
    N = len(Cs)
    A, K, K2 = H_K_K2(Cs, tflt_m, v0, second)
    Wj = [H_W(Cs, tflt_m, j) for j in range(3)]
    Hf = np.zeros((N, 4, 4), dtype=complex)
    for i in range(4):
        for j in range(i, 4):
            z = 0.5 * (A[(i, j)].re.lo + A[(i, j)].re.hi) + 1j * 0.5 * (A[(i, j)].im.lo + A[(i, j)].im.hi)
            if i == j:
                Hf[:, i, i] = z.real
            else:
                Hf[:, i, j] = z; Hf[:, j, i] = np.conj(z)
    _, Q = np.linalg.eigh(Hf)
    Qr, Qi = np.ascontiguousarray(Q.real), np.ascontiguousarray(Q.imag)
    T0 = congruence(lambda a, b: _cfull(A, a, b), Qr, Qi)
    W = congruence(lambda a, b: _cfull(K, a, b), Qr, Qi)
    W2 = congruence(lambda a, b: _cfull(K2, a, b), Qr, Qi) if second else None
    WF = [congruence(lambda a, b, X=X: _cfull(X, a, b), Qr, Qi) for X in Wj]
    one = {}
    for j in range(4):
        for k in range(j, 4):
            acc = None
            for a in range(4):
                acc = _cadd(acc, _conjq_mul(Qr[:, a, j], Qi[:, a, j], C(I(Qr[:, a, k]), I(Qi[:, a, k]))))
            one[(j, k)] = acc
    sok = np.ones(N, dtype=bool)
    for j in range(4):
        off = np.zeros(N)
        for k in range(4):
            if k != j:
                s = one[(min(j, k), max(j, k))]
                off = ru(ru(off + _abs_hi(s.re)) + _abs_hi(s.im))
        sok &= one[(j, j)].re.lo > ru(off)
    rr = I(np.array([-rho_up]), np.array([rho_up]))
    rh = I(np.array([-h_up]), np.array([h_up]))
    r2 = I(np.array([0.0]), np.array([float(ru(0.5 * rho_up * rho_up))]))
    res = []
    for mu in (r, -r):
        M = I(np.array([mu]))
        Tm = {}
        for j in range(4):
            for k in range(j, 4):
                re = T0[(j, k)].re - M * one[(j, k)].re + rr * W[(j, k)].re
                for X in WF:
                    re = re + rh * X[(j, k)].re
                if second:
                    re = re + r2 * W2[(j, k)].re
                if j == k:
                    im = I(np.zeros(N))
                else:
                    im = T0[(j, k)].im - M * one[(j, k)].im + rr * W[(j, k)].im
                    for X in WF:
                        im = im + rh * X[(j, k)].im
                    if second:
                        im = im + r2 * W2[(j, k)].im
                Tm[(j, k)] = C(re, im)
        ng, ok = inertia_neg(Tm, 0.0)
        res.append((ng, ok))
    (ngp, okp), (ngm, okm) = res
    return ngp, ngm, okp & okm & sok


def char_poly_laurent(J):
    """det(M(f) + mu) as a Laurent polynomial in (z1, z2, w, mu) with kappa symbolic (exact sympy, rational couplings); the spectrum of H = iM
    is the root set of this polynomial in mu = i lambda."""
    return sp.expand(sp.expand(det_of(shifted(J, True), [_kk, _z1, _z2, _w, _mu])) / (_z1 * _z2 * _w) ** (4 * S))


SYM_SUBS = {"neg": {_z1: 1 / _z1, _z2: 1 / _z2, _w: 1 / _w}, "swap": {_z1: _z2, _z2: _z1}, "negswap": {_z1: 1 / _z2, _z2: 1 / _z1, _w: 1 / _w}}


def exact_symmetries(J):
    """Names of the coordinate maps g in {neg: f -> -f, swap: (f1, f2, f3) -> (f2, f1, f3), negswap} under which det(M(f) + mu) is identically
    invariant (exact sympy, kappa symbolic, rational couplings).  For such g the spectrum of H at g(f) equals the spectrum at f for every kappa."""
    CP = char_poly_laurent(J)
    return [nm for nm, sub in SYM_SUBS.items() if sp.expand(CP.subs(sub, simultaneous=True) - CP) == 0]


# ================================================================================================ vectorised Hessian test (kgap_fast.py)
def _isqrt(x):
    return I(rd(np.sqrt(x.lo)), ru(np.sqrt(x.hi)))


def _pi_consts():
    p2 = 4 * iv.pi ** 2
    p3 = 8 * iv.pi ** 3
    return (float(rd(float(p2.a))), float(ru(float(p2.b))), float(rd(float(p3.a))), float(ru(float(p3.b))))


PI2LO, PI2HI, PI3LO, PI3HI = _pi_consts()


class FastPD:
    def __init__(self, half):
        self.keys = list(half.keys())
        self.half = half
        self.M = np.array(self.keys, dtype=int)
        self.K = int(np.abs(self.M).max())
        self.cache = {}

    def coef_arrays(self, klo, khi):
        key = (klo, khi)
        if key not in self.cache:
            co = coeff_intervals(self.half, klo, khi)
            d = dict(co)
            lo = np.array([float(rd(float(d[m].a))) for m in self.keys])
            hi = np.array([float(ru(float(d[m].b))) for m in self.keys])
            self.cache[key] = (lo, hi)
        return self.cache[key]

    def hess(self, lo, hi, Alo, Ahi):
        """lo, hi: (N,3) float box corners; Alo, Ahi: (N,T) coefficient enclosures.  Returns the 3x3 upper-triangle dict of I arrays (N,)."""
        N = len(lo)
        c = 0.5 * (lo + hi)
        r = ru(np.maximum(ru(c - lo), ru(hi - c)))                    # half-width bound: [lo, hi] subset [c - r, c + r]
        # phasors z_j = e^{2 pi i c_j}
        vals = c  # Preserve exact binary centres; floating modulo can round.
        uniq = np.unique(vals)
        tab = phase_table(uniq)
        look = np.array([tab[float(v)] for v in uniq])
        idx = np.searchsorted(uniq, vals)                             # (N,3)
        Z = []
        for j in range(3):
            cl, ch, sl, sh = look[idx[:, j], 0], look[idx[:, j], 1], look[idx[:, j], 2], look[idx[:, j], 3]
            Z.append(C(I(cl, ch), I(sl, sh)))
        one = C(I(np.ones(N)), I(np.zeros(N)))
        P = []
        for j in range(3):
            pw = [one, Z[j]]
            for k in range(2, self.K + 1):
                pw.append(pw[-1] * Z[j])
            P.append(pw)
        H = {(i, j): None for i in range(3) for j in range(i, 3)}
        pi2 = I(np.array([PI2LO]), np.array([PI2HI]))
        for t, m in enumerate(self.keys):
            zt = None
            for j in range(3):
                if m[j] == 0:
                    continue
                zz = P[j][abs(m[j])] if m[j] > 0 else P[j][abs(m[j])].conj()
                zt = zz if zt is None else zt * zz
            cosv = zt.re
            sm = np.zeros(N)
            for j in range(3):
                if m[j] != 0:
                    sm = ru(sm + ru(abs(m[j]) * r[:, j]))
            v = ru(PI3HI * sm)
            inner = (I(np.zeros(1)) - pi2 * cosv) + I(-v, v)
            T = I(Alo[:, t], Ahi[:, t]) * inner
            for i in range(3):
                if m[i] == 0:
                    continue
                for j in range(i, 3):
                    if m[j] == 0:
                        continue
                    term = T * I(np.array([float(m[i] * m[j])]))
                    H[(i, j)] = term if H[(i, j)] is None else H[(i, j)] + term
        zero = I(np.zeros(N))
        for key in H:
            if H[key] is None:
                H[key] = zero
        return H

    @staticmethod
    def chol(H, shift=0.0):
        """Interval Cholesky of the symmetric interval matrix H - shift I; returns (ok (N,), minimal pivot lower bound (N,))."""
        sh = I(np.array([shift]))
        s0 = H[(0, 0)] - sh
        ok = s0.lo > 0
        mp_ = s0.lo.copy()
        s0s = I(np.where(ok, s0.lo, 1.0), np.where(ok, s0.hi, 1.0))
        L00 = _isqrt(s0s)
        L10 = H[(0, 1)].div(L00)
        L20 = H[(0, 2)].div(L00)
        s1 = H[(1, 1)] - sh - L10.sq()
        ok1 = s1.lo > 0
        ok &= ok1
        mp_ = np.minimum(mp_, s1.lo)
        s1s = I(np.where(ok1, s1.lo, 1.0), np.where(ok1, s1.hi, 1.0))
        L11 = _isqrt(s1s)
        L21 = (H[(1, 2)] - L20 * L10).div(L11)
        s2 = H[(2, 2)] - sh - L20.sq() - L21.sq()
        ok2 = s2.lo > 0
        ok &= ok2
        mp_ = np.minimum(mp_, s2.lo)
        return ok, mp_

    def pd_boxes(self, lo, hi, Alo, Ahi, shift=0.0, maxdepth=9, maxboxes=40000):
        """Every box (rows of lo, hi; own coefficient rows) is covered by sub-boxes (longest-side bisection up to maxdepth) on each of which the
        Cholesky test passes.  Returns (ok per original box, min pivot per original box)."""
        n0 = len(lo)
        owner = np.arange(n0)
        res_ok = np.ones(n0, dtype=bool)
        res_piv = np.full(n0, np.inf)
        lo, hi, Alo, Ahi = lo.copy(), hi.copy(), Alo.copy(), Ahi.copy()
        for depth in range(maxdepth + 1):
            if len(lo) == 0:
                break
            H = self.hess(lo, hi, Alo, Ahi)
            ok, piv = self.chol(H, shift)
            np.minimum.at(res_piv, owner[ok], piv[ok])
            bad = ~ok
            if depth == maxdepth:
                res_ok[np.unique(owner[bad])] = False
                break
            if not bad.any():
                break
            lo, hi, Alo, Ahi, owner = lo[bad], hi[bad], Alo[bad], Ahi[bad], owner[bad]
            # drop owners already known to fail (none at intermediate depth) ; split the longest side
            k = np.argmax(hi - lo, axis=1)
            mid = 0.5 * (lo[np.arange(len(lo)), k] + hi[np.arange(len(lo)), k])
            lo1, hi1 = lo.copy(), hi.copy()
            lo2, hi2 = lo.copy(), hi.copy()
            hi1[np.arange(len(lo)), k] = mid
            lo2[np.arange(len(lo)), k] = mid
            lo = np.concatenate([lo1, lo2]); hi = np.concatenate([hi1, hi2])
            Alo = np.concatenate([Alo, Alo]); Ahi = np.concatenate([Ahi, Ahi]); owner = np.concatenate([owner, owner])
            if len(lo) > maxboxes:
                res_ok[np.unique(owner)] = False
                break
        return res_ok, res_piv


# ================================================================================================ hierarchical certificate (kgap_hier.py)
FTAYLOR = True


def make_params(J, klo, khi, v0, second):
    km = (klo + khi) / 2
    rho = (khi - klo) / 2
    tflt_m = amp_intervals(J, km, km)
    tflt_hi = amp_intervals(J, khi, khi)
    tfull = amp_intervals(J, klo, khi)
    lipA, lipB = lip_bounds(tflt_hi)
    lip = min(lipA, lipB)
    rho_up = float(ru(float(rho)))
    BK = K_norm_bound(tflt_hi, v0)
    if second:
        B2 = second_deriv_bound(tflt_hi, v0)
        B3 = third_deriv_bound(tflt_hi, v0)
        # every product is rounded up; the final factor (1 + 1e-9) covers the remaining unrounded operations (powers, division by 6)
        rem3 = float(ru(ru(ru(ru(rho_up * rho_up) * rho_up) * B3) / 6 * (1 + 1e-9)))
        pre_extra = float(ru(ru(ru(rho_up * BK) + ru(ru(ru(0.5 * rho_up) * rho_up) * B2)) * (1 + 1e-9)))
    else:
        B2 = B3 = 0.0
        assert all(x == 0.0 for x in v0)
        rem3 = 0.0
        pre_extra = float(ru(ru(rho_up * BK) * (1 + 1e-9)))
    s = 0.0
    for (a, b, n, kd), (tl, th) in zip(TERMS, tfull):
        s += (2 if a == b else 1) * th
    NH = float(ru(s * (1 + 1e-12)))
    return dict(km=km, rho=rho, rho_up=rho_up, tflt_m=tflt_m, tflt_hi=tflt_hi, lip=lip, BK=BK, B2=B2, B3=B3, rem3=rem3, pre_extra=pre_extra, v0=tuple(v0),
                second=second, NH=NH, ftaylor=FTAYLOR)


def clear_level(Cs, h, p, chunk):
    """One clearing pass: plain interval LDL (radius r + first/second-order norm bounds) then the eigenbasis family for what is left."""
    r = float(ru(ru(p["lip"] * h) + p["rem3"]))
    rpre = float(ru(r + p["pre_extra"]))
    keep, negs, n2 = [], set(), 0
    r2 = float(ftaylor_remainder(p["tflt_hi"], p["v0"], h, p["rho_up"])) if p.get("ftaylor") else None
    for s in range(0, len(Cs), chunk):
        c = Cs[s:s + chunk]
        A = H_intervals(c, p["tflt_m"])
        ngp, okp = inertia_neg(A, rpre)
        ngm, okm = inertia_neg(A, -rpre)
        cleared = okp & okm & (ngp == ngm)
        negs |= set(np.unique(ngp[cleared]).tolist())
        rest = ~cleared
        if rest.any():
            cr = c[rest]
            n2 += len(cr)
            if r2 is not None:
                ngp2, ngm2, ok2 = precond_clear3(cr, p["tflt_m"], p["v0"], r2, p["rho_up"], p["second"], float(h))
            else:
                ngp2, ngm2, ok2 = precond_clear2(cr, p["tflt_m"], p["v0"], r, p["rho_up"], p["second"])
            cl2 = ok2 & (ngp2 == ngm2)
            negs |= set(np.unique(ngp2[cl2]).tolist())
            idx = np.nonzero(rest)[0]
            cleared[idx[cl2]] = True
        keep.append(c[~cleared])
    return (np.concatenate(keep) if keep else np.zeros((0, 3))), negs, r, n2


def refine(Cs, h):
    off = np.array(list(itertools.product((-0.5, 0.5), repeat=3))) * h
    return (Cs[:, None, :] + off[None, :, :]).reshape(-1, 3), h / 2


def groups_info(Cs, h):
    """Clusters of the uncleared cubes with their (unwrapped) bounding boxes and whether the box meets a cleared cube."""
    out = []
    for gi in clusters(Cs, h):
        X = Cs[gi].copy(); X = X - np.round(X - X[0])
        lo, hi = X.min(axis=0) - h, X.max(axis=0) + h
        mid = (lo + hi) / 2
        ncube = int(np.prod(np.round((hi - lo) / (2 * h))))
        Y = Cs - np.round(Cs - mid)
        nunc = int(np.sum(np.all((Y >= lo - 1e-15) & (Y <= hi + 1e-15), axis=1)))
        out.append({"gi": gi, "lo": lo, "hi": hi, "ncube": ncube, "nunc": nunc, "n": len(gi), "cleared_in_box": ncube > nunc})
    return out


def tube_in_box(nd, lo, hi):
    mid = [(lo[j] + hi[j]) / 2 for j in range(3)]
    return all(nd[j].a - round(float(nd[j].a) - mid[j]) >= lo[j] and nd[j].b - round(float(nd[j].a) - mid[j]) <= hi[j] for j in range(3))


def tube_in_box_touch(nd, lo, hi):
    """True iff the tube box intersects the box [lo, hi] on the torus (some integer shift gives an intersection in every coordinate)."""
    mid = [(lo[j] + hi[j]) / 2 for j in range(3)]
    for j in range(3):
        s = round(float(nd[j].a) - mid[j])
        if not (nd[j].b - s >= lo[j] and nd[j].a - s <= hi[j]):
            return False
    return True


def tube_velocity(J, a, b, idx):
    """Mean velocity of node tube idx between kappa = a and kappa = b (float; used solely to choose the frame)."""
    eps = Fraction(1, 10 ** 12)
    ta = node_tubes(J, a, a + eps)[idx][1]
    tb = node_tubes(J, b - eps, b)[idx][1]
    return tuple((float(tb[j].mid) - float(ta[j].mid)) / float(b - a) for j in range(3))


def out_round(x, direction):
    return float(np.nextafter(float(x), direction * np.inf))


def sheared_box(lo, hi, v0, da, db):
    flo, fhi = [], []
    for j in range(3):
        vj = Fraction(float(v0[j]))
        c1, c2 = da * vj, db * vj
        flo.append(out_round(Fraction(float(lo[j])) + min(c1, c2), -1))
        fhi.append(out_round(Fraction(float(hi[j])) + max(c1, c2), +1))
    return np.array(flo), np.array(fhi)


def pd_sheared(fpd, J, tube_idx, lo, hi, v0, a, b, km, fdepth, kdepth, leaves):
    """Hessian positive definite on the sheared hull of the cluster box [lo, hi] for kappa in [a, b] and the node tube of each kappa range inside
    its hull; kappa ranges that fail are bisected (all ranges of one depth are tested in one vectorised call).  Appends (flo, fhi, a, b, minpivot)
    of every successful leaf to `leaves`; returns True iff the whole range is covered by successful leaves."""
    ranges = [(a, b)]
    for kd in range(kdepth + 1):
        if not ranges:
            break
        boxes = [sheared_box(lo, hi, v0, x - km, y - km) for (x, y) in ranges]
        flo = np.array([bx[0] for bx in boxes]); fhi = np.array([bx[1] for bx in boxes])
        A = [fpd.coef_arrays(x, y) for (x, y) in ranges]
        Alo = np.array([t[0] for t in A]); Ahi = np.array([t[1] for t in A])
        ok, piv = fpd.pd_boxes(flo, fhi, Alo, Ahi, 0.0, fdepth)
        nxt = []
        for i, (x, y) in enumerate(ranges):
            good = bool(ok[i])
            if good:
                good = tube_in_box(node_tubes(J, x, y, step=Fraction(1, 1000))[tube_idx][1], flo[i], fhi[i])
            if good:
                leaves.append((flo[i], fhi[i], x, y, float(piv[i])))
            else:
                m = (x + y) / 2
                nxt += [(x, m), (m, y)]
        ranges = nxt
    return len(ranges) == 0


def coarse_stage(J, a, b, nodes, n0, maxlev, chunk, P, cap=400000, stop_factor=2.0):
    p = make_params(J, a, b, (0.0, 0.0, 0.0), False)
    rho = float(p["rho"])
    h = 0.5 / n0
    g = (np.arange(n0) + 0.5) / n0
    Cs = np.array(np.meshgrid(g, g, g, indexing="ij")).reshape(3, -1).T
    negs_all, log = set(), []
    for lev in range(maxlev):
        tl = time.time()
        Cs, negs, r, n2 = clear_level(Cs, h, p, chunk)
        negs_all |= negs
        log.append((lev, h, r, len(Cs)))
        P(f"   coarse level {lev}: h {h:.3e}, r {r:.3e}, uncleared {len(Cs)} (stage 2 saw {n2}), {time.time() - tl:.1f} s")
        if len(Cs) == 0:
            return None, negs_all, log, p
        if len(Cs) > cap:
            P("   coarse stage: too many cubes")
            return None, negs_all, log, p
        gi = groups_info(Cs, h) if len(Cs) <= cap else None
        inside = [[i for i, (k, nd) in enumerate(nodes) if tube_in_box(nd, G["lo"], G["hi"])] for G in gi]
        ok = len(gi) == len(nodes) and all(len(x) == 1 for x in inside) and sorted(x[0] for x in inside) == list(range(len(nodes)))
        if ok:
            # efficiency criterion (the frame stage re-checks everything rigorously): the padded blob box must not touch another node's tube
            for G, x in zip(gi, inside):
                mg = 4 * h
                for j, (kj, ndj) in enumerate(nodes):
                    if j != x[0] and tube_in_box_touch(ndj, G["lo"] - mg, G["hi"] + mg):
                        ok = False
        P(f"      {len(gi)} blobs, one tube each (and no other tube within the padded box): {ok}")
        if ok and r <= rho * stop_factor:
            blobs = [dict(G=G, tube=x[0], h=h, cubes=Cs[G["gi"]]) for G, x in zip(gi, inside)]
            return blobs, negs_all, log, p
        Cs, h = refine(Cs, h)
    return None, negs_all, log, p


def frame_stage(J, a, b, blob, nodes_cell, pdc, n_levels, chunk, P, fdepth=7, kdepth=8, cap=300000, pd_wmax=2e-3, capture=False, param_hook=None):
    """One blob, one kappa sub-cell [a, b]: cluster in the moving frame and the Hessian step."""
    t0 = time.time()
    tidx = blob["tube"]
    v0 = tube_velocity(J, a, b, tidx)
    p = make_params(J, a, b, v0, True)
    if param_hook is not None:
        p = param_hook(p)
    hc = blob["h"]
    G = blob["G"]
    pad = [p["rho_up"] * abs(v) + 2 * hc for v in v0]
    lo = G["lo"] - np.array(pad); hi = G["hi"] + np.array(pad)
    i0 = np.floor(lo / (2 * hc)).astype(int); i1 = np.ceil(hi / (2 * hc)).astype(int)
    ax = [(np.arange(i0[j], i1[j]) + 0.5) * (2 * hc) for j in range(3)]
    Cs = np.array(np.meshgrid(*ax, indexing="ij")).reshape(3, -1).T
    h = hc
    res = {"a": str(a), "b": str(b), "tube": tidx, "v0": list(v0), "pass": False,
           "tile": ([int(x) for x in i0], [int(x) for x in i1], float(hc))}          # region tiled by cubes: [i0 * 2 hc, i1 * 2 hc] per axis
    negs_all, log = set(), []
    wprev, nprev = None, 0
    for lev in range(n_levels):
        tl = time.time()
        Cs, negs, r, n2 = clear_level(Cs, h, p, chunk)
        negs_all |= negs
        log.append((lev, h, len(Cs)))
        P(f"      sub-cell [{float(a):.5f},{float(b):.5f}] tube {tidx} level {lev}: h {h:.2e}, r {r:.2e}, uncleared {len(Cs)}, {time.time() - tl:.1f} s")
        if len(Cs) == 0:
            res["why"] = "no uncleared cube (impossible: node is singular)"; return res
        if len(Cs) > cap:
            res["why"] = "too many cubes"; return res
        gi = groups_info(Cs, h)
        wnow = max(float((G_["hi"] - G_["lo"]).max()) for G_ in gi)
        if lev >= 2 and wprev is not None and wnow > 0.75 * wprev and len(Cs) > 1.5 * nprev:
            res["why"] = f"stalled (cluster width {wnow:.2e} not shrinking, {len(Cs)} cubes)"; res["negs"] = sorted(negs_all); return res
        wprev, nprev = wnow, len(Cs)
        if len(gi) == 1 and gi[0]["cleared_in_box"]:
            Gc = gi[0]
            leaves = []
            wmax = float((Gc["hi"] - Gc["lo"]).max())
            ok = False if wmax > pd_wmax else pd_sheared(pdc, J, tidx, Gc["lo"], Gc["hi"], v0, a, b, p["km"], fdepth, kdepth, leaves)
            P(f"         one cluster (max box width {wmax:.2e}): Hessian PD with tube inside on the sheared hull: "
              f"{ok if wmax <= pd_wmax else 'not tried (box too wide)'} ({len(leaves)} leaves)")
            if ok:
                res.update(dict(cluster_box_w=[float(x) for x in (Gc["hi"] - Gc["lo"])], nleaves=len(leaves), final_h=h, uncleared=int(len(Cs)),
                                negs=sorted(negs_all), levels=log, NH=p["NH"]))
                res["leaves"] = leaves
                if capture:
                    res["capture"] = dict(U=Cs.copy(), h=h, lo=lo, hi=hi, v0=v0, km=p["km"], rho=p["rho"], tile=(i0, i1, hc))
                res["pass"] = negs_all <= {2}
                res["sec"] = round(time.time() - t0, 1)
                return res
        Cs, h = refine(Cs, h)
    res["why"] = "levels used up"; res["negs"] = sorted(negs_all); res["levels"] = log; res["sec"] = round(time.time() - t0, 1)
    return res


def cone_constant(fpd, leaves, NH, fdepth, chunk=12):
    """Largest m (by quartering from min pivot / 4) with Hess - m I positive definite on every leaf (leaves tested in chunks, one vectorised call
    each); returns the conical gap constant sqrt(2m)/NH rounded down (0 if none found)."""
    flo = np.array([l[0] for l in leaves]); fhi = np.array([l[1] for l in leaves])
    A = [fpd.coef_arrays(l[2], l[3]) for l in leaves]
    Alo = np.array([t[0] for t in A]); Ahi = np.array([t[1] for t in A])
    m = min(l[4] for l in leaves) / 4
    while m > 1e-14:
        ok = True
        for s in range(0, len(leaves), chunk):
            o, _ = fpd.pd_boxes(flo[s:s + chunk], fhi[s:s + chunk], Alo[s:s + chunk], Ahi[s:s + chunk], m, fdepth)
            if not o.all():
                ok = False
                break
        if ok:
            return float(rd(float((iv.sqrt(2 * iv.mpf(m)) / iv.mpf(NH)).a)))
        m /= 4
    return 0.0


def node_checks_adaptive(J, a, b, depth=0, maxdepth=16):
    """outer levels nonzero and chirality constant on adaptive kappa sub-ranges (tubes recomputed per sub-range, narrow pieces hulled);
    returns (ok, chirality list, number of sub-ranges, depth).  An enclosure that cannot be formed (cosine interval touching +-1) counts as undecided."""
    try:
        nodes = node_tubes(J, a, b, step=Fraction(1, 2000))
        outer, chir = outer_and_chirality(J, a, b, nodes)
    except (ValueError, ZeroDivisionError):
        outer, chir = False, [0]
    if outer and 0 not in chir:
        return True, chir, 1, 1
    if depth >= maxdepth:
        return False, chir, 1, 1
    m = (a + b) / 2
    ok1, c1, n1, d1 = node_checks_adaptive(J, a, m, depth + 1, maxdepth)
    ok2, c2, n2, d2 = node_checks_adaptive(J, m, b, depth + 1, maxdepth)
    return ok1 and ok2 and c1 == c2, c1, n1 + n2, max(d1, d2) + 1


SYM_MAPS = ("neg", "swap", "negswap")


def jstr(J):
    return ",".join(str(x) for x in J) if isinstance(J, (tuple, list)) else str(J)


def sym_box(name, lo, hi):
    """Image of the f-box [lo, hi] (unwrapped floats) under the coordinate map f -> -f, (f1, f2, f3) -> (f2, f1, f3), or their composition."""
    lo = np.asarray(lo, dtype=float)
    hi = np.asarray(hi, dtype=float)
    if name == "neg":
        return -hi, -lo
    if name == "swap":
        return lo[[1, 0, 2]], hi[[1, 0, 2]]
    if name == "negswap":
        return -hi[[1, 0, 2]], -lo[[1, 0, 2]]
    raise ValueError(name)


def sym_tube(name, nd):
    """Image of a tube (three iv.mpf coordinates) under the same maps."""
    x = list(nd)
    if name in ("swap", "negswap"):
        x = [x[1], x[0], x[2]]
    if name in ("neg", "negswap"):
        x = [iv.mpf([-t.b, -t.a]) for t in x]
    return x


def tubes_touch(n1, n2):
    """Float test (used solely to choose which tube is the image of which): the tube boxes meet on the torus."""
    for j in range(3):
        s = round(float(n1[j].a) - float(n2[j].a))
        if not (float(n1[j].b) - s >= float(n2[j].a) and float(n1[j].a) - s <= float(n2[j].b)):
            return False
    return True


def _round_up(x):
    """Smallest float >= the exact rational x (exact when x is representable)."""
    f = float(x)
    return f if Fraction(f) >= x else float(np.nextafter(f, np.inf))


def _round_down(x):
    f = float(x)
    return f if Fraction(f) <= x else float(np.nextafter(f, -np.inf))


def image_blob_covered(rr, nm, cubes, hb):
    """Coverage of an image blob by the representative's frame-stage region.  The frame stage of the representative tiles the region
    [i0 2 hc, i1 2 hc] (per axis) and certifies every tiled point f' = g' + s v0, |s| <= rho, to be cleared (two negative levels) or inside the sheared
    hull.  A point f of a coarse-uncleared cube of the image blob is covered when g^-1(f) - s v0 lies in the tiled region for every |s| <= rho, i.e. when
    g^-1(f) lies in the tiled region shrunk by rho |v0_k| per axis.  The shrunk region is computed in exact rational arithmetic and rounded in the
    shrinking direction, mapped by g (negation and permutation are exact) and compared with the cubes (dyadic floats, exact comparisons) on the torus."""
    i0, i1, hc = rr["tile"]
    rho = (Fraction(rr["b"]) - Fraction(rr["a"])) / 2
    rho_up = Fraction(float(ru(float(rho))))
    shr = [Fraction(_round_up(rho_up * abs(Fraction(float(v))))) for v in rr["v0"]]
    two_hc = 2 * Fraction(float(hc))
    lo = np.array([_round_up(Fraction(i) * two_hc + sh) for i, sh in zip(i0, shr)])
    hi = np.array([_round_down(Fraction(i) * two_hc - sh) for i, sh in zip(i1, shr)])
    glo, ghi = sym_box(nm, lo, hi)
    mid = 0.5 * (glo + ghi)
    shift = np.round(cubes - mid)
    return bool(np.all((cubes - hb - shift >= glo) & (cubes + hb - shift <= ghi)))


def march_blob(J, a, b, bl, nodes, pdc, msub, frame_levels, chunk, P, fdepth, kdepth, frame_cap, split_max):
    """Adaptive marching along kappa of the frame stage for one blob: returns (list of (record, leaves), failed attempts) or (None, failed attempts)."""
    out, nfail = [], 0
    w0 = (b - a) / msub
    wmin = w0 / 2 ** split_max
    w = w0
    sa = a
    streak = 0
    while sa < b:
        wtry = min(w, b - sa)
        if b - sa - wtry < wtry / 3:                      # do not leave a tiny remainder
            wtry = b - sa
        sb = sa + wtry
        r = frame_stage(J, sa, sb, bl, nodes, pdc, frame_levels, chunk, P, fdepth, kdepth, cap=frame_cap)
        ok_sub = bool(r["pass"])
        cone = 0.0
        if ok_sub:
            cone = cone_constant(pdc, r["leaves"], r["NH"], fdepth)
            ok_sub = cone > 0
        if not ok_sub:
            nfail += 1
            P(f"      sub-cell [{float(sa):.5f},{float(sb):.5f}] tube {bl['tube']} failed ({r.get('why', 'cone')}); " +
              ("halving the width" if wtry / 2 >= wmin else "NO WIDTH LEFT"))
            if wtry / 2 < wmin:
                return None, nfail
            w = wtry / 2
            streak = 0
            continue
        rr = {k: v for k, v in r.items() if k != "leaves"}
        rr["cone"] = cone
        out.append((rr, r["leaves"]))
        sa = sb
        streak += 1
        w = wtry
        if streak >= 3:                                    # enlarge solely after three successes in a row
            w = min(wtry * Fraction(5, 4), w0 * 4)
            streak = 0
    return out, nfail


def certify_cell(J, a, b, msub, n0=16, coarse_levels=12, frame_levels=18, chunk=20000, verbose=True, fdepth=7, kdepth=8, stop_factor=1000.0,
                 split_max=5, frame_cap=80000, sym=True):
    t0 = time.time()
    P = (lambda *x: print(*x, flush=True)) if verbose else (lambda *x: None)
    J = jt(J) if isinstance(J, (tuple, list)) else Fraction(J)
    a, b = Fraction(a), Fraction(b)
    reg = regime(J, a, b)
    out = {"J": jstr(J), "a": str(a), "b": str(b), "regime": reg, "pass": False}
    if reg is None:
        out["why"] = "regime"; P("cell contains kappa_c or kappa_h"); return out
    nodes = node_tubes(J, a, b, step=Fraction(1, 500))
    assert tubes_disjoint(nodes)
    P(f"coarse cell J={J} kappa in [{a}, {b}] regime {reg}: {len(nodes)} tubes, max tube width {max(float(nd[j].delta) for _, nd in nodes for j in range(3)):.3e}")
    half, full = D_terms(J)
    pdc = FastPD(half)
    blobs, negs, log, p = coarse_stage(J, a, b, nodes, n0, coarse_levels, chunk, P, stop_factor=stop_factor)
    out["coarse_levels"] = [(l, h, r, n) for l, h, r, n in log]
    if blobs is None:
        out["why"] = "coarse stage failed"; out["sec"] = round(time.time() - t0, 1)
        return out
    out["blobs"] = len(blobs); out["nodes"] = len(nodes)
    tcoarse = time.time() - t0
    P(f"  coarse stage done: {len(blobs)} blobs, cube counts {[bl['G']['n'] for bl in blobs]}, negative counts {sorted(negs)}, {tcoarse:.1f} s")
    # symmetry orbits of the node tubes (float choice of representatives; the image statements are verified rigorously below)
    reps, image_of = [], {}
    allowed = set(exact_symmetries(J)) if sym else set()
    P(f"  exact symmetries of the characteristic polynomial: {sorted(allowed)}")
    for pos, bl in enumerate(blobs):
        found = None
        if sym:
            for rp in reps:
                for nm in [x for x in SYM_MAPS if x in allowed]:
                    if tubes_touch(sym_tube(nm, nodes[blobs[rp]["tube"]][1]), nodes[bl["tube"]][1]):
                        found = (rp, nm)
                        break
                if found:
                    break
        if found:
            image_of[pos] = found
        else:
            reps.append(pos)
    P(f"  symmetry: representatives (blob positions) {reps}, images {image_of}")
    subs, allneg, nfail = [], set(negs), 0
    done = {}                                                  # blob position -> list of (record, leaves)
    for pos in reps:
        res_b, nf = march_blob(J, a, b, blobs[pos], nodes, pdc, msub, frame_levels, chunk, P, fdepth, kdepth, frame_cap, split_max)
        nfail += nf
        if res_b is None:
            out["subcells"] = subs; out["why"] = "frame stage failed"; out["sec"] = round(time.time() - t0, 1)
            return out
        done[pos] = res_b
        for rr, lv in res_b:
            subs.append(rr)
            allneg |= set(rr.get("negs", []))
    tcache = {}
    verified = {}
    for pos, (rp, nm) in image_of.items():
        tj = blobs[pos]["tube"]
        new, ok_img = [], True
        for rr, leaves in done[rp]:
            if not image_blob_covered(rr, nm, blobs[pos]["cubes"], blobs[pos]["h"]):
                ok_img = False
                break
            for (flo, fhi, x, y, piv) in leaves:
                key = (x, y)
                if key not in tcache:
                    tcache[key] = node_tubes(J, x, y, step=Fraction(1, 1000))
                blo, bhi = sym_box(nm, flo, fhi)
                if not tube_in_box(tcache[key][tj][1], blo, bhi):
                    ok_img = False
                    break
            if not ok_img:
                break
            r2 = dict(rr); r2["tube"] = tj; r2["sym"] = [int(blobs[rp]["tube"]), nm]
            new.append(r2)
        if ok_img:
            verified[pos] = (rp, nm)
            subs += new
            P(f"  tube {tj}: certified as the image of tube {blobs[rp]['tube']} under {nm} (all {sum(len(l) for _, l in done[rp])} leaf boxes contain its tube)")
        else:
            P(f"  tube {tj}: image check failed, running its own frame stage")
            res_b, nf = march_blob(J, a, b, blobs[pos], nodes, pdc, msub, frame_levels, chunk, P, fdepth, kdepth, frame_cap, split_max)
            nfail += nf
            if res_b is None:
                out["subcells"] = subs; out["why"] = "frame stage failed"; out["sec"] = round(time.time() - t0, 1)
                return out
            for rr, lv in res_b:
                subs.append(rr)
                allneg |= set(rr.get("negs", []))
    P(f"  frame stage done ({len(subs)} sub-cell/tube pairs certified, {nfail} failed attempts split), {time.time() - t0:.0f} s")
    tn = time.time()
    ok, chir, nch, depth = node_checks_adaptive(J, a, b)
    P(f"  outer levels nonzero and chirality constant nonzero on {nch} adaptive kappa sub-ranges: {ok}; chirality {''.join('+' if c > 0 else '-' for c in chir)} "
      f"(sum {sum(chir)}); {time.time() - tn:.1f} s")
    out.update({"pass": bool(ok and allneg == {2} and sum(chir) == 0), "negs": sorted(allneg), "chir": chir, "subcells": subs,
                "min_cone": min(s["cone"] for s in subs), "sec": round(time.time() - t0, 1), "chir_ranges": nch,
                "sym_images": {str(blobs[k]["tube"]): [int(blobs[v[0]]["tube"]), v[1]] for k, v in verified.items()}})
    P(f"  CELL RESULT {'PASS' if out['pass'] else 'FAIL'}: kappa in [{a}, {b}], J = {J}; negative counts {sorted(allneg)}; min cone constant {out['min_cone']:.3g}; {out['sec']} s")
    return out

# ================================================================================================ drivers (hand-written)
KC2, KH2 = Fraction(3, 20), Fraction(1, 4)        # kappa_c^2 and kappa_h^2 at J = 1 (J(J+2)/(4(4+2J-J^2)), J/(4(2-J)))


def exact_line_family(J):
    """Exact (sympy), kappa symbolic, rational (Jx, Jy, Jz): det H, z_j dD/dz_j and the constant and linear characteristic coefficients vanish
    identically on the line family z2 = 1/z1, w = 1, with q(c) = 4 u c^2 - 2 P c - (4 u + S) = 0 (z1 + 1/z1 = 2c, u = kappa^2, P = Jx Jy,
    S = Jx^2 + Jy^2 - Jz^2).  A wrong S gives a nonzero remainder (negative control, wrongS = True)."""
    return _line_family_remainders(J, 0)


def _line_family_remainders(J, dS):
    Jx, Jy, Jz = [sp.Rational(x.numerator, x.denominator) for x in jt(J)]
    z1, z2, w, k, mu = _z1, _z2, _w, _kk, _mu
    S4 = 4 * S
    Dg = sp.expand(sp.expand(det_of(shifted(J), [k, z1, z2, w])) / (z1 * z2 * w) ** S4)
    CP = char_poly_laurent(J)
    DOM = sp.QQ.frac_field(k)
    TG = [Dg] + [v * sp.diff(Dg, v) for v in (z1, z2, w)] + [CP.coeff(mu, 0), CP.coeff(mu, 1)]
    P_ = Jx * Jy
    S_ = Jx ** 2 + Jy ** 2 - Jz ** 2 + dS
    PL = sp.Poly(k ** 2 * z1 ** 4 - P_ * z1 ** 3 - (2 * k ** 2 + S_) * z1 ** 2 - P_ * z1 + k ** 2, z1, domain=DOM)
    r1 = [sp.simplify(sp.rem(sp.Poly(sp.expand(sp.expand(e.subs({z2: 1 / z1, w: 1})) * z1 ** 12), z1, domain=DOM), PL).as_expr()) for e in TG]
    return all(x == 0 for x in r1)


def exact_families(Jq):
    """Exact (sympy) check, kappa symbolic and J rational (Jx = Jy = 1): D = det H, z_j dD/dz_j and the constant and linear characteristic
    coefficients vanish identically on the line family, the plane f1 + f2 = 1 family (ii) and the plane f1 + f2 = 2 f3 family (iii)."""
    Jr = sp.Rational(Jq.numerator, Jq.denominator)
    z1, z2, w, k, mu = _z1, _z2, _w, _kk, _mu
    y, s = sp.symbols("y s")
    S4 = 4 * S
    Dg = sp.expand(sp.expand(det_of(shifted(Jq), [k, z1, z2, w])) / (z1 * z2 * w) ** S4)
    CP = char_poly_laurent(Jq)
    DOM = sp.QQ.frac_field(k)
    TG = [Dg] + [v * sp.diff(Dg, v) for v in (z1, z2, w)] + [CP.coeff(mu, 0), CP.coeff(mu, 1)]
    PL = sp.Poly(k ** 2 * z1 ** 4 - z1 ** 3 + (Jr ** 2 - 2 * k ** 2 - 2) * z1 ** 2 - z1 + k ** 2, z1, domain=DOM)
    r1 = [sp.simplify(sp.rem(sp.Poly(sp.expand(sp.expand(e.subs({z2: 1 / z1, w: 1})) * z1 ** 10), z1, domain=DOM), PL).as_expr()) for e in TG]
    C1, C3 = 1 - Jr / (4 * k ** 2), (Jr + 2) / (4 * k ** 2) - (4 + Jr - Jr ** 2) / Jr
    G2 = [sp.expand((z1 ** 2 - 2 * C1 * z1 + 1) * 4 * k ** 2 * Jr), sp.expand((w ** 2 - 2 * C3 * w + 1) * 4 * k ** 2 * Jr)]
    r2 = [sp.simplify(sp.reduced(sp.expand(sp.expand(e.subs(z2, 1 / z1)) * z1 ** 10 * w ** 10), G2, z1, w, domain=DOM)[1]) for e in TG]
    Cf = (Jr + 2 - s) / 2
    G3 = [sp.expand(w ** 2 - 2 * Cf * w + 1), sp.expand(y ** 2 - 2 * (-Jr - Cf) * y + 1), sp.expand((s ** 2 - 5 * Jr ** 2 - 8 * Jr) * k ** 2 - Jr * (Jr + 2))]
    r3 = [sp.simplify(sp.reduced(sp.expand(sp.expand(e.subs({z1: w * y, z2: w / y}, simultaneous=True)) * w ** 12 * y ** 12), G3, w, y, s,
                                 order="lex", domain=DOM)[1]) for e in TG]
    return all(x == 0 for x in r1), all(x == 0 for x in r2), all(x == 0 for x in r3)


def float_eigs(f, kap, Jq):
    """Float Bloch eigenvalues (diagnostic)."""
    f = np.atleast_2d(f)
    kap = np.broadcast_to(np.asarray(kap, float), (len(f),))
    Jx, Jy, Jz = [float(x) for x in jt(Jq)]
    amp = {"x": 2.0 * Jx, "y": 2.0 * Jy, "z": 2.0 * Jz}
    nn = np.array([x[2] for x in TERMS], float)
    ph = np.exp(2j * np.pi * f @ nn.T)
    Hf = np.zeros((len(f), 4, 4), dtype=complex)
    for j, (a, b, n, kd) in enumerate(TERMS):
        tt = np.broadcast_to(2.0 * kap if kd == "odd" else amp[kd], (len(f),))
        Hf[:, a, b] += 1j * tt * ph[:, j]
        Hf[:, b, a] -= 1j * tt * np.conj(ph[:, j])
    return np.linalg.eigvalsh(Hf)


class QF:
    """Exact element of Q(g_1, ..., g_k) with g_i^2 = A[i] (basis: products of distinct generators, bitmask keys); used for the exact evaluation of
    D = det H and its derivatives at algebraic points."""
    A = []
    __slots__ = ("c",)

    def __init__(self, c=None):
        self.c = {k_: v for k_, v in (c or {}).items() if v != 0}

    @staticmethod
    def const(x):
        return QF({0: Fraction(x)})

    @staticmethod
    def gen(i):
        return QF({1 << i: Fraction(1)})

    def __add__(s_, o):
        o = o if isinstance(o, QF) else QF.const(o)
        d = dict(s_.c)
        for k_, v in o.c.items():
            d[k_] = d.get(k_, 0) + v
        return QF(d)

    __radd__ = __add__

    def __neg__(s_):
        return QF({k_: -v for k_, v in s_.c.items()})

    def __sub__(s_, o):
        return s_ + (-(o if isinstance(o, QF) else QF.const(o)))

    def __mul__(s_, o):
        o = o if isinstance(o, QF) else QF.const(o)
        d = {}
        for k1, v1 in s_.c.items():
            for k2, v2 in o.c.items():
                f = v1 * v2
                com, i = k1 & k2, 0
                while com:
                    if com & 1:
                        f *= QF.A[i]
                    com >>= 1
                    i += 1
                d[k1 ^ k2] = d.get(k1 ^ k2, 0) + f
        return QF(d)

    __rmul__ = __mul__

    def conj(s_, conjgens):
        return QF({k_: (-v if bin(k_ & conjgens).count("1") % 2 else v) for k_, v in s_.c.items()})

    def iszero(s_):
        return not s_.c


def qf_pow(z, zi, n):
    r = QF.const(1)
    base = z if n >= 0 else zi
    for _ in range(abs(n)):
        r = r * base
    return r


def exact_point_data(J, K, z, conjgens):
    """Exact D, its gradient (coefficient of i) and Hessian with respect to theta = 2 pi f at the unit-circle point z (z^-1 = conjugate) and
    odd coupling K, both in QF arithmetic: D = sum c_{m,q} K^q z^m, d_j -> i m_j, d_i d_j -> -m_i m_j."""
    zi = [t.conj(conjgens) for t in z]
    half, full = D_terms(J)
    qmax = max(q for d in full.values() for q in d)
    Kp = {0: QF.const(1)}
    for q in range(1, qmax + 1):
        Kp[q] = K * Kp[q - 1]
    D, G, H = QF(), [QF() for _ in range(3)], [[QF() for _ in range(3)] for _ in range(3)]
    for m, d in full.items():
        zm = QF.const(1)
        for j in range(3):
            zm = zm * qf_pow(z[j], zi[j], m[j])
        for q, c in d.items():
            if c == 0:
                continue
            term = zm * Kp[q] * QF.const(c)
            D = D + term
            for i in range(3):
                G[i] = G[i] + term * m[i]
                for j in range(3):
                    H[i][j] = H[i][j] + term * (-m[i] * m[j])
    return D, G, H


def sanity():
    """Interval Bloch entries contain 40-digit values; interval inertia equals float counts; the eigenbasis-congruence family test agrees with
    float eigenvalue counts at the corners of the family (first order frame and moving second-order frame)."""
    Jq, km = Fraction(1), Fraction(3, 10)
    tf = amp_intervals(Jq, km, km)
    rng = np.random.default_rng(0)
    pts = np.floor(rng.random((400, 3)) * 2 ** 20) / 2 ** 20
    A = H_intervals(pts, tf)
    miss = 0
    for s_ in range(20):
        f = [mpf(float(x)) for x in pts[s_]]
        M = [[mpc(0)] * 4 for _ in range(4)]
        for (a, b, n, kd) in TERMS:
            tt = mpf(2) if kd != "odd" else 2 * mpf(3) / 10
            th = 2 * mp.pi * sum(f[j] * n[j] for j in range(3))
            M[a][b] += tt * mp.expj(th)
            M[b][a] -= tt * mp.expj(-th)
        for (i, j), e in A.items():
            hij = mpc(0, 1) * M[i][j]
            miss += not (e.re.lo[s_] <= hij.real <= e.re.hi[s_] and (i == j or e.im.lo[s_] <= hij.imag <= e.im.hi[s_]))
    ev = float_eigs(pts, 0.3, Jq)
    agree = []
    for m_ in (-1.0, 0.0, 0.37, 2.5):
        ng, ok = inertia_neg(A, m_)
        agree.append(bool(ok.all()) and float(np.mean(ng == (ev < m_).sum(axis=1))))
    rho = Fraction(1, 1000)
    rho_up = float(ru(float(rho)))
    nok, bad = 0, 0
    for v0, second in (((0.0, 0.0, 0.0), False), ((0.1, -0.1, 0.05), True)):
        ng1, ng2, ok = precond_clear2(pts, tf, v0, 0.02, rho_up, second)
        good = ok & (ng1 == ng2)
        nok += int(good.sum())
        for dlt in (-float(rho), 0.0, float(rho)):
            evd = float_eigs(pts + dlt * np.array(v0)[None, :], 0.3 + dlt, Jq)
            bad += int(np.sum(good & ((evd < 0).sum(axis=1) != ng1)))
    return miss == 0 and min(agree) == 1.0 and nok > 400 and bad == 0, \
        f"interval entries outside the 40-digit values {miss}; plain inertia agreement {min(agree):.3f}; congruence family cleared at {nok}/800 point-frames, float inertia mismatches {bad}"


def tiling_ok(res):
    """Exact rational check: for every tube the certified kappa sub-cells tile [a, b] without gap or overlap."""
    a, b = Fraction(res["a"]), Fraction(res["b"])
    tubes = sorted(set(sc["tube"] for sc in res["subcells"]))
    ok = len(tubes) == res["nodes"]
    for t in tubes:
        ss = sorted((Fraction(sc["a"]), Fraction(sc["b"])) for sc in res["subcells"] if sc["tube"] == t)
        ok &= ss[0][0] == a and ss[-1][1] == b and all(ss[i][1] == ss[i + 1][0] for i in range(len(ss) - 1))
    return bool(ok)


def run_cell(J, a, b, msub, levels=18):
    t0 = time.time()
    res = certify_cell(J, a, b, msub, frame_levels=levels, verbose=False)
    return res, time.time() - t0


def certified_interval(label, J, a, b, msub, nodes_expected, regime_expected, levels, chir_expected, nsym_expected):
    res, sec = run_cell(J, a, b, msub, levels)
    if not res["pass"]:
        check(label, False, f"certificate failed: {res.get('why')}; {sec:.0f} s")
        return None
    chir = "".join("+" if c > 0 else "-" for c in res["chir"])
    nsym = len(res.get("sym_images", {}))
    ok = (res["regime"] == regime_expected and res["nodes"] == nodes_expected and res["blobs"] == res["nodes"] and tiling_ok(res)
          and res["negs"] == [2] and res["min_cone"] > 0 and sum(res["chir"]) == 0 and 0 not in res["chir"]
          and chir == chir_expected and nsym >= nsym_expected)
    check(label, ok,
          f"exactly the {res['nodes']} family nodes ({nsym} verified symmetry images); {len(res['subcells'])} sub-cell/node pairs tile the cell; "
          f"min cone {res['min_cone']:.3g}; chirality {chir}; {sec:.0f} s")
    return res


def check_exact_symmetries():
    """Exact (sympy, kappa symbolic): det(M + mu) is invariant under f -> -f, f1 <-> f2 and their composition at J = 1 and at (1, 4/5, 1); a
    wrong map (z1 <-> w) is not a symmetry (negative control)."""
    out = []
    for J in (Fraction(1), (Fraction(1), Fraction(4, 5), Fraction(1))):
        out.append(sorted(exact_symmetries(J)) == ["neg", "negswap", "swap"])
    CP = char_poly_laurent(Fraction(1))
    wrong = sp.expand(CP.subs({_z1: _w, _w: _z1}, simultaneous=True) - CP) != 0
    return all(out) and wrong, f"J = 1: {out[0]}, J = (1, 4/5, 1): {out[1]}, negative control z1 <-> w not invariant: {wrong}"


def check_special_couplings():
    """Exact statements at J = 1 for the two special couplings (all rational or in Q(sqrt(-5), sqrt(15)) / Q(i), no floating point)."""
    J = Fraction(1)
    # kappa_c^2 = 3/20: line cosine = plane (ii) cosine c1, c3 = 1, F2 = 0
    u = KC2
    disc = 1 + 8 * u + 16 * u * u - 4 * u * J * J
    d = Fraction(7, 5)
    cl = (1 - d) / (4 * u)
    c1 = 1 - J / (4 * u)
    c3 = (J + 2) / (4 * u) - (4 + J - J * J) / J
    F2 = J * (J + 2) - 4 * u * (4 + 2 * J - J * J)
    okc = disc == d * d and cl == c1 == Fraction(-2, 3) and c3 == 1 and F2 == 0 and J - 4 * (2 - J) * u > 0
    # kappa_h^2 = 1/4: c1 = J - 1 = 0, c3 = -1, plane (iii) s = 5, cos 2 pi f3 = -1, cos 2 pi g = 0, F1 = 0
    u = KH2
    s2 = 5 * J * J + 8 * J + J * (J + 2) / u
    cF = (J + 2 - 5) / 2
    okh = (1 - J / (4 * u) == J - 1 == 0 and (J + 2) / (4 * u) - (4 + J - J * J) / J == -1 and s2 == 25 and cF == -1 and -J - cF == 0
           and J - 4 * (2 - J) * u == 0 and J * (J + 2) - 4 * u * (4 + 2 * J - J * J) < 0)
    # exact D, gradient, Hessian (theta = 2 pi f) at the merged points
    QF.A = [Fraction(-1)]
    I_ = QF.gen(0)
    Dh, Gh, Hh = exact_point_data(J, QF.const(Fraction(1, 2)), [I_, -I_, QF.const(-1)], 1)
    hh = [[Hh[i][j].c for j in range(3)] for i in range(3)]
    exp_h = [[{0: Fraction(192)}, {0: Fraction(-192)}, {}], [{0: Fraction(-192)}, {0: Fraction(192)}, {}], [{}, {}, {}]]
    okH = Dh.iszero() and all(g.iszero() for g in Gh) and hh == exp_h
    QF.A = [Fraction(-5), Fraction(15)]
    s_, r_ = QF.gen(0), QF.gen(1)
    z1 = (s_ + QF.const(-2)) * Fraction(1, 3)
    z2 = (-s_ + QF.const(-2)) * Fraction(1, 3)
    Dc, Gc, Hc = exact_point_data(J, r_ * Fraction(1, 10), [z1, z2, QF.const(1)], 1)
    hc = [[Hc[i][j].c for j in range(3)] for i in range(3)]
    exp_c = [[{0: Fraction(608, 15)}, {0: Fraction(-1312, 45)}, {}], [{0: Fraction(-1312, 45)}, {0: Fraction(608, 15)}, {}], [{}, {}, {}]]
    okC = Dc.iszero() and all(g.iszero() for g in Gc) and hc == exp_c
    return okc, okh, okH, okC


def check_kappa_zero():
    """Exact: D(kappa = 0) = 16 |(1 + z1)(1 + z2) - w|^2 on the torus (nodal line), which vanishes at (1/3, 2/3, 0) = kappa -> 0 limit of the line nodes."""
    J = Fraction(1)
    Dg = sp.expand(sp.expand(det_of(shifted(J), [_kk, _z1, _z2, _w])) / (_z1 * _z2 * _w) ** (4 * S))
    D0 = sp.expand(Dg.subs(_kk, 0))
    F = (1 + _z1) * (1 + _z2) - _w
    Fp = _w * (1 + _z1) * (1 + _z2) - _z1 * _z2
    ident = sp.expand(D0 * _w * _z1 * _z2 - 16 * F * Fp) == 0
    zz = sp.Symbol("zz")
    vanish = sp.rem(sp.Poly(sp.expand(F.subs({_z1: zz, _z2: zz ** 2, _w: 1})), zz), sp.Poly(zz ** 2 + zz + 1, zz)).is_zero
    cl0 = -(Fraction(2) - J * J) / 2                  # line cosine at kappa = 0
    return ident and vanish and cl0 == Fraction(-1, 2), f"identity {ident}; F(w, w^2, 1) = 0: {vanish}; line cosine at kappa = 0: {cl0}"


def check_remainder_bound():
    """FLOAT diagnostic of a rigorous bound: the ray-Taylor remainder bound dominates the sampled remainder norms (three couplings)."""
    rng = np.random.default_rng(5)
    worst = 0.0
    for J, klo, khi, v0, h in ((Fraction(1), Fraction(2, 5), Fraction(41, 100), (0.1, -0.1, 0.05), 1e-2),
                               (Fraction(1), Fraction(3, 5), Fraction(31, 50), (-0.3, 0.2, 0.1), 3e-2),
                               ((Fraction(1), Fraction(4, 5), Fraction(1)), Fraction(1, 10), Fraction(11, 100), (0.0, 0.0, 0.0), 2e-2)):
        km = (klo + khi) / 2
        rho_up = float(ru(float((khi - klo) / 2)))
        tm, thi = amp_intervals(J, km, km), amp_intervals(J, khi, khi)
        Jx, Jy, Jz = [float(x) for x in jt(J)]
        amp = {"x": 2 * Jx, "y": 2 * Jy, "z": 2 * Jz}

        def bloch(f, kap):
            Hm = np.zeros((4, 4), complex)
            for (a, b, n, kd) in TERMS:
                tt = 2 * kap if kd == "odd" else amp[kd]
                ph = np.exp(2j * np.pi * np.dot(n, f))
                Hm[a, b] += 1j * tt * ph
                Hm[b, a] -= 1j * tt * np.conj(ph)
            return Hm

        def mid(X):
            out = np.zeros((4, 4), complex)
            for (i, j), e in X.items():
                z = 0.5 * (e.re.lo[0] + e.re.hi[0]) + 1j * 0.5 * (e.im.lo[0] + e.im.hi[0])
                if i == j:
                    out[i, i] = z.real
                else:
                    out[i, j] = z; out[j, i] = np.conj(z)
            return out
        rem = ftaylor_remainder(thi, v0, h, rho_up)
        for _ in range(3):
            c = rng.random((1, 3))
            A, Kx, K2x = H_K_K2(c, tm, v0, True)
            H0, Km, K2m = mid(A), mid(Kx), mid(K2x)
            Wm = [mid(H_W(c, tm, j)) for j in range(3)]
            for trial in range(150):
                d = rng.uniform(-h, h, 3); s = rng.uniform(-rho_up, rho_up)
                if trial < 8:
                    d = h * np.array([(-1) ** ((trial >> k) & 1) for k in range(3)]); s = rho_up * (-1) ** (trial & 1)
                Phi = bloch(c[0] + d + s * np.array(v0), float(km) + s)
                poly = H0 + sum(d[j] * Wm[j] for j in range(3)) + s * Km + 0.5 * s * s * K2m
                worst = max(worst, np.linalg.norm(Phi - poly, 2) / rem)
    return worst < 1.0, f"max (sampled remainder norm)/(bound) = {worst:.3f} over 3 couplings x 3 centres x 150 samples"


def check_aniso_flip():
    """Exact (sympy, one radical sqrt(5441)): at (Jx, Jy, Jz) = (1, 4/5, 1) the closed form u_+ = (N0 + N1 sqrt(Delta_F))/Den equals
    (-6134 + 354 sqrt(5441))/169175, c_F = (-a1 + sqrt(Delta_F))/(2 a2) is a root of F_c, and q(c_F; u_+) = 0 (the line root meets the root of F_c)."""
    Jx, Jy, Jz = sp.Rational(1), sp.Rational(4, 5), sp.Rational(1)
    s_, P = Jx + Jy, Jx * Jy
    S_ = s_ ** 2 - 2 * P - Jz ** 2
    N0 = (s_ ** 2 - 2 * P - Jz ** 2) * (2 * Jz ** 3 * P - 4 * Jz * P * s_ ** 2 + Jz * s_ ** 4 - 4 * P * s_ ** 3 + s_ ** 5)
    N1 = 2 * Jz ** 2 * P - Jz ** 2 * s_ ** 2 - 4 * P * s_ ** 2 + s_ ** 4
    Den = -8 * (s_ ** 2 + Jz * s_ - Jz ** 2) * (Jz ** 3 - 4 * P * s_ + s_ ** 3)
    a2, a1, a0 = P * (s_ + Jz), s_ * (s_ ** 2 + Jz * s_ - 2 * P), (P + Jz * s_ + Jz ** 2) * (s_ - Jz)
    DF = a1 ** 2 - 4 * a2 * a0
    u = (N0 + N1 * sp.sqrt(DF)) / Den
    c = (-a1 + sp.sqrt(DF)) / (2 * a2)
    ok1 = DF == sp.Rational(195876, 15625) and sp.simplify(u - (-6134 + 354 * sp.sqrt(5441)) / 169175) == 0
    ok2 = sp.simplify(a2 * c ** 2 + a1 * c + a0) == 0
    ok3 = sp.simplify(4 * u * c ** 2 - 2 * P * c - (4 * u + S_)) == 0
    return ok1 and ok2 and ok3, f"Delta_F = {DF}; u_+ closed form {ok1}; F_c(c_F) = 0 {ok2}; q(c_F; u_+) = 0 {ok3}"


def check_clear3_samples():
    """FLOAT diagnostic of the rigorous clearing test: cubes cleared by precond_clear3 (frame of a family-(ii) node, J = 1, kappa in [21/50, 211/500])
    have the float inertia of the cleared count (two negative levels, no zero level) at corner and random samples (delta, s) of the cube/frame family."""
    rng = np.random.default_rng(11)
    J, klo, khi = Fraction(1), Fraction(21, 50), Fraction(211, 500)
    nodes = node_tubes(J, klo, khi, step=Fraction(1, 500))
    v0 = tube_velocity(J, klo, khi, 2)
    p = make_params(J, klo, khi, v0, True)
    node = np.array([float(x.mid) for x in nodes[2][1]])
    rho, km = p["rho_up"], float(p["km"])
    bad, ncl, nsamp = 0, 0, 0
    for h in (3e-2, 1e-2, 1e-3):
        N = 1500
        dist = h * np.exp(rng.uniform(np.log(0.5), np.log(80), N))
        dirs = rng.normal(size=(N, 3))
        dirs /= np.linalg.norm(dirs, axis=1)[:, None]
        Cs = node[None, :] + dist[:, None] * dirs
        r2 = ftaylor_remainder(p["tflt_hi"], p["v0"], h, rho)
        ngp, ngm, ok = precond_clear3(Cs, p["tflt_m"], p["v0"], r2, rho, True, h)
        cl = np.nonzero(ok & (ngp == ngm))[0]
        ncl += len(cl)
        for i in sorted(cl, key=lambda q: dist[q])[:150]:                   # the cleared cubes closest to the node are the borderline ones
            for t in range(24):
                d = rng.uniform(-h, h, 3)
                s_ = rng.uniform(-rho, rho)
                if t < 8:
                    d = h * np.array([(-1) ** ((t >> k) & 1) for k in range(3)])
                    s_ = rho * (-1) ** (t & 1)
                ev = float_eigs(Cs[i] + d + s_ * np.array(v0), km + s_, J)[0]
                nsamp += 1
                if int((ev < 0).sum()) != int(ngp[i]) or np.abs(ev).min() < 1e-12:
                    bad += 1
    return bad == 0 and ncl > 500, f"{ncl} cubes cleared at h = 3e-2, 1e-2, 1e-3; {nsamp} samples, float inertia violations {bad}"


def check_wiring():
    """clear_level uses the remainder bound: at h = 1e-2 (J = 1, kappa in [21/50, 211/500], frame of a family-(ii) node) collect cubes on rays from the node that
    precond_clear3 clears with remainder 0 but not with the rigorous bound; clear_level must leave all of them uncleared."""
    rng = np.random.default_rng(3)
    J, klo, khi = Fraction(1), Fraction(21, 50), Fraction(211, 500)
    nodes = node_tubes(J, klo, khi, step=Fraction(1, 500))
    v0 = tube_velocity(J, klo, khi, 2)
    p = make_params(J, klo, khi, v0, True)
    node = np.array([float(x.mid) for x in nodes[2][1]])
    rho, h = p["rho_up"], 1e-2
    r2 = ftaylor_remainder(p["tflt_hi"], p["v0"], h, rho)
    dirs = rng.normal(size=(24, 3))
    dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    ds = h * np.exp(np.linspace(np.log(2.0), np.log(40), 70))
    B = []
    for d in dirs:
        Cs = node[None, :] + ds[:, None] * d[None, :]
        n0, m0, o0 = precond_clear3(Cs, p["tflt_m"], p["v0"], 0.0, rho, True, h)
        n2, m2, o2 = precond_clear3(Cs, p["tflt_m"], p["v0"], r2, rho, True, h)
        sel = (o0 & (n0 == m0)) & ~(o2 & (n2 == m2))
        B += [Cs[i] for i in np.nonzero(sel)[0]]
    B = np.array(B)
    unc, negs, rr, n2c = clear_level(B, h, p, 20000) if len(B) else (B, set(), 0.0, 0)
    return len(B) >= 5 and len(unc) == len(B), f"{len(B)} cubes cleared with remainder 0 but not with the bound; clear_level leaves {len(unc)} of them uncleared"


def check_controls():
    """Negative and positive controls of the Hessian and symmetry-image machinery (interval arithmetic)."""
    J = Fraction(1)
    half, full = D_terms(J)
    fpd = FastPD(half)
    # positive control: box of half-width 1e-4 around the line node at kappa in [1/5, 20001/100000]
    nd = node_tubes(J, Fraction(1, 5), Fraction(20001, 100000))[0][1]
    c = np.array([float(x.mid) for x in nd])
    klo, khi = Fraction(1, 5), Fraction(20001, 100000)
    Alo, Ahi = fpd.coef_arrays(klo, khi)
    okp, _ = fpd.pd_boxes((c - 1e-4)[None], (c + 1e-4)[None], Alo[None], Ahi[None], 0.0, 7)
    # negative control: box containing the kappa_c merged point (x, 1-x, 0), cos 2 pi x = -2/3, kappa in [0.3872, 0.3874] (Hessian rank 2 there)
    x = float(np.arccos(-2.0 / 3.0) / (2 * np.pi))
    c2 = np.array([x, 1.0 - x, 0.0])
    klo2, khi2 = Fraction(3872, 10000), Fraction(3874, 10000)
    Alo2, Ahi2 = fpd.coef_arrays(klo2, khi2)
    okn, _ = fpd.pd_boxes((c2 - 2e-4)[None], (c2 + 2e-4)[None], Alo2[None], Ahi2[None], 0.0, 7)
    # symmetry-image control: a box and the tube of the SAME node are not related by f -> -f (the node (x, 1-x, 0) is not at its own mirror image)
    lo, hi = (c - 1e-4), (c + 1e-4)
    blo, bhi = sym_box("neg", lo, hi)
    wrong_in = tube_in_box(nd, blo, bhi)
    right_in = tube_in_box(node_tubes(J, Fraction(1, 5), Fraction(20001, 100000))[1][1], blo, bhi)
    # tiling control: a result with a gap in the sub-cell tiling is rejected
    bad = {"a": "0", "b": "1", "nodes": 1, "subcells": [{"tube": 0, "a": "0", "b": "1/3"}, {"tube": 0, "a": "1/2", "b": "1"}]}
    good = {"a": "0", "b": "1", "nodes": 1, "subcells": [{"tube": 0, "a": "0", "b": "1/2"}, {"tube": 0, "a": "1/2", "b": "1"}]}
    okt = tiling_ok(good) and not tiling_ok(bad)
    return okp and (not okn) and (not wrong_in) and right_in and okt, \
        f"PD: regular node {bool(okp)}, kappa_c point {bool(okn)}; neg-image inclusion: own tube {wrong_in}, mirror tube {right_in}; tiling {okt}"


def merged(cells):
    out = []
    for a, b in sorted(cells):
        if out and out[-1][1] >= a:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out


def check_coverage(cells, kc2, kh2, lo, hi):
    """Exact rational bookkeeping of logged certified cells (J = 1): the union covers [lo, hi] except gaps; exactly one gap contains kappa_c (g0^2 < kappa_c^2 < g1^2)
    and exactly one contains kappa_h; every other gap is an untested hole that contains neither."""
    m = merged([(Fraction(a), Fraction(b)) for a, b in cells])
    gaps = [(m[i][1], m[i + 1][0]) for i in range(len(m) - 1)]
    contains = lambda g, k2: g[0] * g[0] < k2 < g[1] * g[1]
    gc = [g for g in gaps if contains(g, kc2)]
    gh = [g for g in gaps if contains(g, kh2)]
    ok = m[0][0] <= lo and m[-1][1] >= hi and len(gc) == 1 and len(gh) == 1 and gc[0] != gh[0]
    return ok, m, gaps


def main():
    t = time.time()
    ex = exact_families(Fraction(1))
    check("exact families, J = 1, kappa symbolic: det H, its 3 gradients, constant and linear char. coefficients vanish identically on line, (ii), (iii)",
          all(ex), f"{ex}; {time.time() - t:.0f} s")
    t = time.time()
    la = [exact_line_family(J) for J in ((Fraction(1), Fraction(4, 5), Fraction(1)), (Fraction(6, 5), Fraction(4, 5), Fraction(1)))]
    neg = _line_family_remainders((Fraction(1), Fraction(4, 5), Fraction(1)), Fraction(1, 10))
    check("exact line family for Jx != Jy: same identities on q(c) = 4uc^2 - 2Pc - (4u + S) = 0 at (1, 4/5, 1), (6/5, 4/5, 1)",
          all(la) and not neg, f"{la}; wrong S fails (control) {not neg}; {time.time() - t:.0f} s")
    t = time.time()
    ok, detail = check_exact_symmetries()
    check("exact char.-polynomial symmetries f -> -f, f1 <-> f2", ok, f"{detail}; {time.time() - t:.0f} s")
    t = time.time()
    okc, okh, okH, okC = check_special_couplings()
    check("exact: kappa_c^2 = 3/20 (line cos = c1 = -2/3, c3 = 1, F2 = 0); kappa_h^2 = 1/4 (c1 = 0, c3 = -1, s = 5, cos 2pi f3 = -1, cos 2pi g = 0, F1 = 0)",
          okc and okh, f"kappa_c {okc}; kappa_h {okh}")
    check("exact: D = grad D = 0 at merged points; Hess_theta D rank 1 (192[[1,-1],[-1,1]] on f1,f2) at (1/4,3/4,1/2), kappa_h; rank 2, kernel f3, "
          "[[608/15,-1312/45],[-1312/45,608/15]] on f1,f2 at (x,1-x,0), kappa_c", okH and okC, f"kappa_h point {okH}; kappa_c point {okC}; {time.time() - t:.0f} s")
    t = time.time()
    ok, detail = check_kappa_zero()
    check("exact kappa = 0: D = 16 |(1+z1)(1+z2) - w|^2 (nodal curve) through the kappa -> 0 line-node limit (1/3, 2/3, 0)", ok, f"{detail}; {time.time() - t:.0f} s")
    t = time.time()
    ok, detail = check_aniso_flip()
    check("exact flip coupling at (1, 4/5, 1): kappa_c^2 = (-6134 + 354 sqrt(5441))/169175, line root meets root of F_c", ok, f"{detail}; {time.time() - t:.0f} s")
    t = time.time()
    ok, detail = sanity()
    check("interval Bloch entries / congruence inertia test vs 40-digit and float values (J = 1, kappa = 3/10)", ok, f"{detail}; {time.time() - t:.0f} s")
    ok, detail = check_remainder_bound()
    check("f-Taylor remainder bound dominates sampled remainders (float diagnostic of a rigorous bound)", ok, detail)
    cells = CELLS + (CELLS_NEAR if os.environ.get("KGAP_NEAR_GAP") else [])
    for lab, J, a, b, msub, levels, nn, rg, ce, ns in cells:
        certified_interval(lab, J, Fraction(a), Fraction(b), msub, nn, rg, levels, ce, ns)
    ok, m, gaps = check_coverage(COVER, KC2, KH2, COVER_LO, COVER_HI)
    check("bookkeeping of logged cells (J = 1, exact rationals): one gap brackets kappa_c, one brackets kappa_h, others are holes",
          ok, f"{len(COVER)} cells; union " + ", ".join(f"[{float(a):.4g}, {float(b):.4g}]" for a, b in m) + "; gaps " + ", ".join(f"({float(a):.5g}, {float(b):.5g})" for a, b in gaps) +
          f"; kappa_c = {float(KC2) ** 0.5:.5f}, kappa_h = {float(KH2) ** 0.5:.5f}")
    ma = merged([(Fraction(a), Fraction(b)) for a, b in COVER_ANISO])
    up = uplus_enclosure(*JA)
    okA = len(ma) == 1 and ivr(ma[0][1] * ma[0][1]).b < up.a
    check("bookkeeping of logged cells at (1, 4/5, 1): one interval below the flip coupling u_+ (interval enclosure)", okA,
          f"union [{float(ma[0][0]):.4g}, {float(ma[0][1]):.4g}]; kappa_c^2 in [{float(up.a):.12g}, {float(up.b):.12g}], kappa_c = {float(up.mid) ** 0.5:.6f}")
    r1 = regime(Fraction(1), Fraction(49, 100), Fraction(51, 100))            # contains kappa_h = 1/2
    r2 = regime(Fraction(1), Fraction(19, 50), Fraction(2, 5))                # contains kappa_c = 0.3873
    r3 = regime(Fraction(1), Fraction(1, 2), Fraction(51, 100))               # touches kappa_h at an endpoint
    r4 = regime(Fraction(1), Fraction(11, 25), Fraction(12, 25))              # inside the family-(ii) window: accepted
    res = certify_cell(Fraction(1), Fraction(49, 100), Fraction(51, 100), 1, verbose=False)
    check("exclusion: cells containing/touching kappa_c or kappa_h are refused (regime check, certify_cell)",
          r1 is None and r2 is None and r3 is None and r4 == "b" and (not res["pass"]) and res.get("why") == "regime",
          f"[49/100, 51/100] {r1}, [19/50, 2/5] {r2}, [1/2, 51/100] {r3}, [11/25, 12/25] {r4}; certify_cell pass = {res['pass']}, why = {res.get('why')}")
    t = time.time()
    ok, detail = check_clear3_samples()
    check("clearing test (f-Taylor family) vs float inertia at sampled points of the cleared cubes (diagnostic)", ok, f"{detail}; {time.time() - t:.0f} s")
    t = time.time()
    ok, detail = check_wiring()
    check("clear_level applies the remainder bound (borderline cubes stay uncleared)", ok, f"{detail}; {time.time() - t:.0f} s")
    t = time.time()
    ok, detail = check_controls()
    check("controls: Hessian PD passes at a regular node, fails at the kappa_c point; wrong-map inclusion and tiling gap rejected", ok, f"{detail}; {time.time() - t:.0f} s")
    Jq, a, b = Fraction(1), Fraction(3, 5), Fraction(31, 50)
    nodes = node_tubes(Jq, a, b, step=Fraction(1, 500))
    pn = coarse_stage(Jq, a, b, nodes[:-1], 16, 6, 20000, lambda *x: None, stop_factor=1000.0)
    check("negative control: one family node removed from the tube list, the coarse stage gives no certificate", pn[0] is None,
          f"5 of 6 tubes: {'no blobs' if pn[0] is None else 'blobs'}")
    print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
    print(f"runtime {time.time() - T0:.0f} s", flush=True)



# ================================================================================================ data tables (logged runs)
# J = 1 certified cells (one cell = one run of certify_cell with this code; times from the logs, machine at load 4-8):
COVER = [
    ("1/125", "9/1000"), ("9/1000", "1/100"), ("1/100", "9/800"), ("9/800", "1/80"), ("1/80", "11/800"), ("11/800", "3/200"),
    ("3/200", "7/400"), ("7/400", "1/50"), ("1/50", "1/40"), ("1/40", "3/100"), ("3/100", "1/25"), ("1/25", "1/20"),
    ("1/20", "1/10"), ("1/10", "1/5"), ("1/5", "3/10"), ("3/10", "7/20"), ("7/20", "37/100"), ("37/100", "19/50"),
    ("19/50", "191/500"), ("191/500", "48/125"), ("48/125", "77/200"), ("2/5", "321/800"), ("321/800", "161/400"), ("161/400", "81/200"),
    ("81/200", "13/32"), ("13/32", "163/400"), ("163/400", "41/100"), ("41/100", "33/80"), ("33/80", "83/200"), ("83/200", "21/50"),
    ("21/50", "17/40"), ("17/40", "87/200"), ("87/200", "89/200"), ("89/200", "91/200"), ("91/200", "93/200"), ("93/200", "19/40"),
    ("19/40", "97/200"), ("97/200", "49/100"), ("49/100", "197/400"), ("197/400", "79/160"), ("79/160", "99/200"), ("99/200", "62/125"),
    ("101/200", "203/400"), ("203/400", "51/100"), ("51/100", "13/25"), ("13/25", "53/100"), ("53/100", "11/20"), ("11/20", "57/100"),
    ("57/100", "3/5"), ("3/5", "31/50"), ("31/50", "7/10"), ("7/10", "4/5"), ("4/5", "9/10"), ("9/10", "1"),
    ("1", "11/10"),
]
COVER_LO, COVER_HI = Fraction(1, 125), Fraction(11, 10)
# (1, 4/5, 1) certified cells (line nodes below the flip coupling):
COVER_ANISO = [
    ("3/100", "1/20"), ("1/20", "1/10"), ("1/10", "1/5"), ("1/5", "3/10"), ("3/10", "8/25"), ("8/25", "33/100"), ("33/100", "67/200"), ("67/200", "169/500"), ("169/500", "17/50"),
]
# Cells re-run by this runner (label, couplings, a, b, initial kappa sub-cells, frame levels, nodes expected, regime expected, chirality string, minimum number of verified symmetry images); kappa_c = 0.38730,
# kappa_h = 1/2 at J = 1; JA = (1, 4/5, 1) with flip coupling kappa_c = 0.34364.
JA = (Fraction(1), Fraction(4, 5), Fraction(1))
CELLS = [
    ("A: J = 1, kappa in [19/50, 191/500] (0.0073 below kappa_c)", Fraction(1), "19/50", "191/500", 1, 32, 2, "a", "+-", 1),
    ("B: J = 1, kappa in [87/200, 89/200] (family ii)", Fraction(1), "87/200", "89/200", 2, 24, 6, "b", "-+++--", 1),
    ("C: J = 1, kappa in [97/200, 49/100] (0.01 below kappa_h)", Fraction(1), "97/200", "49/100", 2, 24, 6, "b", "-+++--", 1),
    ("D: J = 1, kappa in [13/25, 53/100] (0.02 above kappa_h)", Fraction(1), "13/25", "53/100", 2, 28, 6, "c", "-+-+-+", 4),
    ("E: J = 1, kappa in [3/5, 31/50] (family iii)", Fraction(1), "3/5", "31/50", 2, 28, 6, "c", "-+-+-+", 4),
    ("F: J = 1, kappa in [1/25, 1/20] (small kappa)", Fraction(1), "1/25", "1/20", 1, 34, 2, "a", "+-", 1),
    ("G: J = (1, 4/5, 1), kappa in [3/10, 8/25]", JA, "3/10", "8/25", 2, 30, 2, "a", "+-", 1),
]
CELLS_NEAR = [
    ("near A: J = 1, kappa in [48/125, 77/200] (0.0023 below kappa_c)", Fraction(1), "48/125", "77/200", 1, 36, 2, "a", "+-", 1),
    ("near B: J = 1, kappa in [2/5, 321/800] (0.0127 above kappa_c)", Fraction(1), "2/5", "321/800", 2, 28, 6, "b", "-+++--", 4),
    ("near C: J = 1, kappa in [99/200, 62/125] (0.004 below kappa_h)", Fraction(1), "99/200", "62/125", 1, 32, 6, "b", "-+++--", 4),
    ("near D: J = 1, kappa in [101/200, 203/400] (0.005 above kappa_h)", Fraction(1), "101/200", "203/400", 2, 28, 6, "c", "-+-+-+", 4),
    ("near E: J = 1, kappa in [1/125, 9/1000]", Fraction(1), "1/125", "9/1000", 1, 42, 2, "a", "+-", 1),
    ("near F: J = (1, 4/5, 1), kappa in [169/500, 17/50] (0.0036 below the flip coupling)", JA, "169/500", "17/50", 1, 36, 2, "a", "+-", 1),
]


main()

# A failed scientific check must fail the bounded execution.
raise SystemExit(1 if len(RESULTS) - sum(RESULTS) else 0)
