#!/usr/bin/env python3
"""Composite-site network, flux-free comparator: interval certificate of the middle-band touchings for EVERY kappa in a rational interval.

Supplied u = +1 quadratic Majorana comparator of the landed notes (one copy, the landed hopping-sign convention), couplings J_x = J_y = 1, J_z = J,
odd term kappa, four-site Bloch matrix H(f; kappa) = i M(f; kappa) over the fractional zone.  The landed note certifies the middle-band touchings
at thirteen sample couplings.  Here kappa is a fourth interval variable: a certified kappa-interval [a, b] (J rational) means, for EVERY kappa in
[a, b], that det H vanishes in the zone exactly at the family nodes (the three landed exact families), each a double zero with outer levels of
opposite sign, conical with an explicit constant, with a constant chirality sign (the signs sum to zero), and that H has two negative and two
positive levels everywhere else.

Certificate stages (kint_hier.certify_cell):
 1. coarse clearing of boxes (f-cube) x [a, b].  H is exactly affine in kappa, so the family {H(c, kappa_m) + delta H1(c)}, |delta| <= rho, is tested
    through the congruence Q^dagger (.) Q (Q = float eigenvectors of H(c, kappa_m), only a basis: Q^dagger Q is enclosed and checked diagonally
    dominant, so Sylvester's law of inertia applies) with an interval LDL^T at -+ r, r = lip h the Weyl radius of the f-variation inside the cube
    (lip = the smaller of two rigorous Lipschitz bounds).  Cleared cubes: nonsingular with two negative levels for every kappa in [a, b].
 2. the uncleared cubes form one blob per node tube (tubes = interval evaluation of the exact cosine formulas of the families, hull over narrow
    kappa pieces).  Per blob and kappa sub-cell: a frame moving with the node, f' = g + (kappa - km) v0; the first and second kappa-derivatives
    of H along the path are carried exactly in the eigenbasis family, the third-order remainder and the f-variation by Weyl radii; the
    uncleared g-cubes must form ONE cluster.
 3. uniqueness: the sheared hull of the cluster is a convex f-box; the interval Hessian of D = det H (Fourier form, centred interval form with
    exact phasors, mean-value form of the kappa-dependent coefficients, interval Cholesky, bisection in f and kappa) is positive definite on it
    for every kappa of the leaf, so D(., kappa) is strictly convex there; the node tube lies inside; with D = grad D = 0 at the node (exact algebra)
    D > 0 on the punctured hull, which is connected and meets a cleared cube, hence two negative levels there.
 4. node checks on adaptive kappa sub-ranges: e2 (sum of principal 2x2 minors, = product of the outer levels at the node) < 0 in interval arithmetic;
    chirality sign from Im Tr(P d1H P d2H P d3H)/2 in interval arithmetic; conical constant sqrt(2m)/||H|| from Hess D - m I positive definite.
 5. the kappa sub-cells of every tube tile the cell (exact rational check).

Tiers.  EXACT (sympy, polynomial rings, kappa symbolic): the three node families (check 1: det H, its three momentum derivatives and the constant
and linear characteristic coefficients vanish identically on them).  INTERVAL-CERTIFIED with outward rounding (one-ulp outward steps on IEEE
operations, mpmath interval cos/sin with outward float conversion, exact Fractions for J and the kappa endpoints): clearing, Hessian, tubes, e2,
chirality, cone constants.  FLOAT, no claim attached: the eigenbasis Q, the frame velocity v0 and the choice of sub-cell widths and levels (they
affect only efficiency, never validity), and the random samplers of check 2.
Excluded: cells containing kappa_c^2 = J(J+2)/[4(4+2J-J^2)] or kappa_h^2 = J/[4(2-J)] (or touching them at an endpoint) are refused (check 7);
nothing is claimed between the certified intervals, for other anisotropies, or beyond the listed couplings.
Checks: (1) exact families, J = 1 and J = 1/2; (2) interval Bloch entries and congruence/inertia against high-precision and float values;
(3)-(6) certified intervals at J = 1: [1/10, 3/25] (2 nodes), [3/5, 31/50] (6 nodes, family iii), [21/50, 17/40] (6 nodes, family ii),
[1, 11/10] (6 nodes); (7) exclusion of cells containing kappa_h or kappa_c.
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

AUDIT_TIMEOUT_SEC = 1800

mp.dps = 40
iv.dps = 30

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


# ================================================================================================ library (kint_lib.py)
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


_T1 = terms((1.0, 1.0, 1.0), 0.3)


_T2 = terms((1.0, 1.0, 1.5), 0.3)


KIND = ["xy" if abs(t1 - 2.0) < 1e-12 and abs(t2 - 2.0) < 1e-12 else ("z" if abs(t1 - 2.0) < 1e-12 else "odd")
        for (_, _, _, t1), (_, _, _, t2) in zip(_T1, _T2)]


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


def amp_intervals(J, klo, khi):
    """Float intervals (lo, hi) of the hopping amplitudes: 2, 2J, [2 klo, 2 khi]."""
    out = []
    for (a, b, n, kd) in TERMS:
        if kd == "xy":
            out.append((2.0, 2.0))
        elif kd == "z":
            out.append(qint(2 * Fraction(J)))
        else:
            out.append((qint(2 * Fraction(klo))[0], qint(2 * Fraction(khi))[1]))
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


def regime(J, klo, khi):
    """Exact rational regime of the cell: 'a' (kappa^2 < kappa_c^2: line nodes only), 'b' (kappa_c^2 < k^2 < kappa_h^2), 'c' (k^2 > kappa_h^2),
    or None when the cell contains kappa_c or kappa_h (or is outside the formulas' range)."""
    J, klo, khi = Fraction(J), Fraction(klo), Fraction(khi)
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
    Ji = ivr(J)
    nodes = []
    disc = 1 + 8 * K2 + 16 * K4 - 4 * K2 * Ji * Ji
    if not disc.a > 0:
        raise ValueError("line discriminant not positive on the cell")
    cl = -(2 + 4 * K2 - Ji * Ji) / (1 + iv.sqrt(disc))        # = (1 - sqrt(disc))/(4 K^2), K^2 cancelled analytically
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
    J = sp.Rational(J.numerator, J.denominator) if isinstance(J, Fraction) else sp.Rational(J)
    Ms = [[sp.Integer(0)] * 4 for _ in range(4)]
    for (a, b, n, kd) in TERMS:
        tt = {"xy": sp.Integer(2), "z": 2 * J, "odd": 2 * _kk}[kd]
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
    Ji = ivr(J)
    Zm = lambda: [[iv.mpc(0) for _ in range(4)] for _ in range(4)]
    M, dM = Zm(), [Zm(), Zm(), Zm()]
    for (a, b, n, kd) in TERMS:
        tt = {"xy": iv.mpf(2), "z": 2 * Ji, "odd": 2 * Kiv}[kd]
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


# ================================================================================================ vectorised Hessian test (kint_fast.py)
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
        vals = np.mod(c, 1.0)
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


# ================================================================================================ hierarchical certificate (kint_hier.py)
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
    return dict(km=km, rho=rho, rho_up=rho_up, tflt_m=tflt_m, lip=lip, BK=BK, B2=B2, B3=B3, rem3=rem3, pre_extra=pre_extra, v0=tuple(v0),
                second=second, NH=NH)


def clear_level(Cs, h, p, chunk):
    """One clearing pass: plain interval LDL (radius r + first/second-order norm bounds) then the eigenbasis family for what is left."""
    r = float(ru(ru(p["lip"] * h) + p["rem3"]))
    rpre = float(ru(r + p["pre_extra"]))
    keep, negs, n2 = [], set(), 0
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
    """Mean velocity of node tube idx between kappa = a and kappa = b (float; only used to choose the frame)."""
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
    res = {"a": str(a), "b": str(b), "tube": tidx, "v0": list(v0), "pass": False}
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
    res["why"] = "levels exhausted"; res["negs"] = sorted(negs_all); res["levels"] = log; res["sec"] = round(time.time() - t0, 1)
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


def certify_cell(J, a, b, msub, n0=16, coarse_levels=12, frame_levels=18, chunk=20000, verbose=True, fdepth=7, kdepth=8, stop_factor=1000.0,
                 split_max=5, frame_cap=80000):
    t0 = time.time()
    P = (lambda *x: print(*x, flush=True)) if verbose else (lambda *x: None)
    J, a, b = Fraction(J), Fraction(a), Fraction(b)
    reg = regime(J, a, b)
    out = {"J": str(J), "a": str(a), "b": str(b), "regime": reg, "pass": False}
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
    subs = []
    allneg = set(negs)
    nfail = 0
    for bl in blobs:
        # adaptive marching along kappa: the sub-cell width is halved after a failed attempt and enlarged by 25% after a success
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
                    out["subcells"] = subs; out["why"] = "frame stage failed"; out["sec"] = round(time.time() - t0, 1)
                    return out
                w = wtry / 2
                streak = 0
                continue
            rr = {k: v for k, v in r.items() if k != "leaves"}
            rr["cone"] = cone
            subs.append(rr)
            allneg |= set(r.get("negs", []))
            sa = sb
            streak += 1
            w = wtry
            if streak >= 3:                                    # enlarge only after three successes in a row
                w = min(wtry * Fraction(5, 4), w0 * 4)
                streak = 0
    P(f"  frame stage done ({len(subs)} sub-cell/tube pairs certified, {nfail} failed attempts split), {time.time() - t0:.0f} s")
    tn = time.time()
    ok, chir, nch, depth = node_checks_adaptive(J, a, b)
    P(f"  outer levels nonzero and chirality constant nonzero on {nch} adaptive kappa sub-ranges: {ok}; chirality {''.join('+' if c > 0 else '-' for c in chir)} "
      f"(sum {sum(chir)}); {time.time() - tn:.1f} s")
    out.update({"pass": bool(ok and allneg == {2} and sum(chir) == 0), "negs": sorted(allneg), "chir": chir, "subcells": subs,
                "min_cone": min(s["cone"] for s in subs), "sec": round(time.time() - t0, 1), "chir_ranges": nch})
    P(f"  CELL RESULT {'PASS' if out['pass'] else 'FAIL'}: kappa in [{a}, {b}], J = {J}; negative counts {sorted(allneg)}; min cone constant {out['min_cone']:.3g}; {out['sec']} s")
    return out

# ================================================================================================ drivers (hand-written)
def exact_families(Jq):
    """Exact (sympy) check, kappa symbolic and J rational: D = det H, z_j dD/dz_j and the constant and linear characteristic coefficients vanish
    identically on the line family, the plane f1 + f2 = 1 family (ii) and the plane f1 + f2 = 2 f3 family (iii)."""
    Jr = sp.Rational(Jq.numerator, Jq.denominator)
    z1, z2, w, k, mu = _z1, _z2, _w, _kk, _mu
    y, s = sp.symbols("y s")
    S4 = 4 * S
    Dg = sp.expand(sp.expand(det_of(shifted(Jq), [k, z1, z2, w])) / (z1 * z2 * w) ** S4)
    CP = sp.expand(sp.expand(det_of(shifted(Jq, True), [k, z1, z2, w, mu])) / (z1 * z2 * w) ** S4)
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
    """Float Bloch eigenvalues (diagnostic only)."""
    f = np.atleast_2d(f)
    kap = np.broadcast_to(np.asarray(kap, float), (len(f),))
    nn = np.array([x[2] for x in TERMS], float)
    ph = np.exp(2j * np.pi * f @ nn.T)
    Hf = np.zeros((len(f), 4, 4), dtype=complex)
    for j, (a, b, n, kd) in enumerate(TERMS):
        tt = 2.0 if kd == "xy" else (2.0 * float(Jq) if kd == "z" else 2.0 * kap)
        tt = np.broadcast_to(tt, (len(f),))
        Hf[:, a, b] += 1j * tt * ph[:, j]
        Hf[:, b, a] -= 1j * tt * np.conj(ph[:, j])
    return np.linalg.eigvalsh(Hf)


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
    # congruence family test: cleared points must have the float inertia at delta = -rho, 0, +rho (moving frame: f' = c + delta v0)
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
        f"interval entries outside the 40-digit values {miss}; plain inertia agreement {min(agree):.3f} (400 points, 4 shifts); " \
        f"congruence family cleared at {nok}/800 point-frames, float inertia mismatches {bad}"


def tiling_ok(res):
    """Exact rational check: for every tube the certified kappa sub-cells tile [a, b] without gap or overlap."""
    a, b = Fraction(res["a"]), Fraction(res["b"])
    tubes = sorted(set(sc["tube"] for sc in res["subcells"]))
    ok = len(tubes) == res["nodes"]
    for t in tubes:
        ss = sorted((Fraction(sc["a"]), Fraction(sc["b"])) for sc in res["subcells"] if sc["tube"] == t)
        ok &= ss[0][0] == a and ss[-1][1] == b and all(ss[i][1] == ss[i + 1][0] for i in range(len(ss) - 1))
    return bool(ok)


def certified_interval(label, Jq, a, b, msub, nodes_expected, regime_expected):
    t0 = time.time()
    res = certify_cell(Jq, a, b, msub, verbose=False)
    sec = time.time() - t0
    if not res["pass"]:
        check(label, False, f"certificate failed: {res.get('why')}; {sec:.0f} s")
        return
    chir = "".join("+" if c > 0 else "-" for c in res["chir"])
    ok = (res["regime"] == regime_expected and res["nodes"] == nodes_expected and res["blobs"] == res["nodes"] and tiling_ok(res)
          and res["negs"] == [2] and res["min_cone"] > 0 and sum(res["chir"]) == 0 and 0 not in res["chir"])
    check(label, ok,
          f"every kappa in [{a}, {b}] (J = {Jq}): exactly the {res['nodes']} family nodes (clusters = tubes, one hull each, Hessian PD, double zero, "
          f"e2 < 0, count 2/2 elsewhere); sub-cell/node pairs {len(res['subcells'])} tile the cell exactly; min cone constant {res['min_cone']:.3g}; "
          f"chirality {chir} (sum 0); {sec:.0f} s")


def main():
    t = time.time()
    ex = [exact_families(Fraction(1)), exact_families(Fraction(1, 2))]
    check("exact families, kappa symbolic, J = 1 and J = 1/2: det H, its three momentum derivatives and the constant and linear characteristic "
          "coefficients vanish identically on the line, plane (ii) and plane (iii) families", all(all(e) for e in ex),
          f"line/(ii)/(iii) at J = 1: {ex[0]}; at J = 1/2: {ex[1]}; {time.time() - t:.0f} s")
    t = time.time()
    ok, detail = sanity()
    check("interval Bloch entries and the eigenbasis-congruence inertia test against 40-digit and float values (J = 1, kappa = 3/10)", ok, f"{detail}; {time.time() - t:.0f} s")
    certified_interval("certified interval 1: J = 1, kappa in [1/10, 3/25], two line nodes", Fraction(1), Fraction(1, 10), Fraction(3, 25), 1, 2, "a")
    certified_interval("certified interval 2: J = 1, kappa in [3/5, 31/50], six nodes (family iii)", Fraction(1), Fraction(3, 5), Fraction(31, 50), 4, 6, "c")
    certified_interval("certified interval 3: J = 1, kappa in [21/50, 17/40], six nodes (family ii)", Fraction(1), Fraction(21, 50), Fraction(17, 40), 4, 6, "b")
    certified_interval("certified interval 4: J = 1, kappa in [1, 11/10], six nodes (family iii)", Fraction(1), Fraction(1), Fraction(11, 10), 4, 6, "c")
    kc, kh = Fraction(3, 20), Fraction(1, 4)                                   # kappa_c^2, kappa_h^2 at J = 1
    r1 = regime(Fraction(1), Fraction(49, 100), Fraction(51, 100))            # contains kappa_h = 1/2
    r2 = regime(Fraction(1), Fraction(19, 50), Fraction(2, 5))                # contains kappa_c = 0.3873
    r3 = regime(Fraction(1), Fraction(1, 2), Fraction(51, 100))               # touches kappa_h at an endpoint
    r4 = regime(Fraction(1), Fraction(11, 25), Fraction(12, 25))              # inside the family-(ii) window: accepted
    res = certify_cell(Fraction(1), Fraction(49, 100), Fraction(51, 100), 1, verbose=False)
    check("exclusion: cells containing or touching kappa_c or kappa_h are refused by the regime check and by certify_cell",
          r1 is None and r2 is None and r3 is None and r4 == "b" and (not res["pass"]) and res.get("why") == "regime",
          f"J = 1 (kappa_c^2 = {kc}, kappa_h^2 = {kh}): [49/100, 51/100] -> {r1}, [19/50, 2/5] -> {r2}, [1/2, 51/100] -> {r3}, [11/25, 12/25] -> {r4}; "
          f"certify_cell on [49/100, 51/100]: pass = {res['pass']}, why = {res.get('why')}")
    print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
    print(f"runtime {time.time() - T0:.0f} s", flush=True)


main()
