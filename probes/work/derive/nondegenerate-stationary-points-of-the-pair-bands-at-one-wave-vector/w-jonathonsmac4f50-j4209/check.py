#!/usr/bin/env python3
"""check.py for J:derive:nondegenerate-stationary-points-of-the-pair-bands-at-one-wave-vector:a2 (worker w-jonathonsmac4f50-j4209, claude-opus-5-5).

Certify assumption (A') of block 143 (PR #9229) on Z^2 at one total wave vector K0 with rational half-angle tangents:
the band functions E(q) = s1 eps(K0/2 + q) + s2 eps(K0/2 - q), eps(k) = (sin^2 k1 + sin^2 k2)^(1/2), have only nondegenerate stationary points
away from the cone points.  Stationary points: grad eps(k1) = sigma grad eps(k2), k2 = K0 - k1, sigma = s1 s2 (the pairs (s1,s2) and (-s1,-s2) give E and -E).

Method (exact rational arithmetic throughout; no floating point enters any certified statement):
  * the torus in k1 is covered by four chart boxes in half-angle tangents: per coordinate t = tan(k/2) on [-1, 1] (k in [-pi/2, pi/2]) or
    u = cot(k/2) on [-1, 1] (k in [pi/2, 3pi/2]); sin and cos are rational in t (u); sin K0, cos K0 are rational;
  * interval arithmetic on Fractions with outward rounding to 2^-96, and forward-mode derivatives (interval Jacobian of G = grad eps(k1) - sigma grad eps(k2)
    with respect to the chart coordinates);
  * each root: a Krawczyk test on a small box (unique zero) and the interval Jacobian determinant excluding 0 there (nondegenerate: the chart map k(t) is a
    diffeomorphism with dk/dt > 0, so det Hess_q E = det(dG/dt) / (product of dk/dt) up to sign);
  * elsewhere: exclusion by subdivision - a box is cleared when a component of G excludes 0, or near a cone point by a division-free magnitude test
    (|grad eps(k)|^2 = 1 - sum sin^4/sum sin^2 >= 1 - max sin^2, and <= 1 - eps^2/2 in two dimensions).
Floating point is used only to find the approximate roots that seed the Krawczyk boxes.
"""
import math, sys, time
from fractions import Fraction as Fr
import numpy as np

PASS, FAIL = [], []
t_start = time.time()
def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(("PASS " if ok else "FAIL ") + name + ((": " + detail) if detail else "") + "  [%.0f s]" % (time.time() - t_start), flush=True)

SH = 96
SC = 1 << SH
def rdn(x): return Fr(math.floor(x * SC), SC)
def rup(x): return Fr(math.ceil(x * SC), SC)
class I:
    __slots__ = ("lo", "hi")
    def __init__(self, lo, hi=None):
        if hi is None: hi = lo
        self.lo, self.hi = lo, hi
    @staticmethod
    def of(x):
        return x if isinstance(x, I) else I(Fr(x), Fr(x))
    def __add__(a, b): b = I.of(b); return I(rdn(a.lo + b.lo), rup(a.hi + b.hi))
    __radd__ = __add__
    def __neg__(a): return I(-a.hi, -a.lo)
    def __sub__(a, b): return a + (-I.of(b))
    def __rsub__(a, b): return I.of(b) + (-a)
    def __mul__(a, b):
        b = I.of(b); ps = (a.lo * b.lo, a.lo * b.hi, a.hi * b.lo, a.hi * b.hi)
        return I(rdn(min(ps)), rup(max(ps)))
    __rmul__ = __mul__
    def sq(a):
        if a.lo >= 0: return I(rdn(a.lo * a.lo), rup(a.hi * a.hi))
        if a.hi <= 0: return I(rdn(a.hi * a.hi), rup(a.lo * a.lo))
        return I(Fr(0), rup(max(a.lo * a.lo, a.hi * a.hi)))
    def inv(a):
        if a.lo <= 0 <= a.hi: raise ZeroDivisionError
        return I(rdn(1 / a.hi), rup(1 / a.lo))
    def __truediv__(a, b): return a * I.of(b).inv()
    def __rtruediv__(a, b): return I.of(b) * a.inv()
    def contains0(a): return a.lo <= 0 <= a.hi
    def mid(a): return (a.lo + a.hi) / 2
    def width(a): return a.hi - a.lo
def fsqrt_lo(x):
    """rational lower bound of sqrt(x), x >= 0"""
    if x <= 0: return Fr(0)
    return Fr(math.isqrt(math.floor(x * SC * SC)), SC)
def fsqrt_hi(x):
    if x <= 0: return Fr(0)
    r = math.isqrt(math.ceil(x * SC * SC))
    if r * r < x * SC * SC: r += 1
    return Fr(r, SC)
def isqrt_(a):
    if a.hi < 0: raise ValueError
    return I(fsqrt_lo(max(a.lo, Fr(0))), fsqrt_hi(a.hi))

class D:
    """interval with an interval gradient (forward mode) in NV variables"""
    __slots__ = ("v", "g")
    NV = 2
    def __init__(self, v, g=None):
        self.v = v; self.g = g if g is not None else [I(Fr(0)) for _ in range(D.NV)]
    @staticmethod
    def of(x): return x if isinstance(x, D) else D(I.of(x))
    def __add__(a, b): b = D.of(b); return D(a.v + b.v, [x + y for x, y in zip(a.g, b.g)])
    __radd__ = __add__
    def __neg__(a): return D(-a.v, [-x for x in a.g])
    def __sub__(a, b): return a + (-D.of(b))
    def __rsub__(a, b): return D.of(b) + (-a)
    def __mul__(a, b):
        b = D.of(b); return D(a.v * b.v, [a.v * y + b.v * x for x, y in zip(a.g, b.g)])
    __rmul__ = __mul__
    def sq(a): return D(a.v.sq(), [2 * a.v * x for x in a.g])
    def inv(a):
        iv = a.v.inv(); iv2 = iv.sq()
        return D(iv, [-(iv2 * x) for x in a.g])
    def __truediv__(a, b): return a * D.of(b).inv()
    def sqrt(a):
        s = isqrt_(a.v)
        if s.lo <= 0: raise ZeroDivisionError
        half_inv = (2 * s).inv()
        return D(s, [half_inv * x for x in a.g])

# ================================================================ dimension-generic certificate
import itertools
def run_dim(d, TK, n_seed):
    D.NV = d
    SK = [2 * t / (1 + t * t) for t in TK]; CK = [(1 - t * t) / (1 + t * t) for t in TK]
    K0f = [2 * math.atan(float(t)) for t in TK]
    def zeros(): return [I(Fr(0)) for _ in range(d)]
    def sincos(x, chart):
        den = 1 + x.sq(); s_ = 2 * x / den
        c_ = (1 - x.sq()) / den if chart == 0 else (x.sq() - 1) / den
        return s_, c_
    def G_eval(X, charts, grad):
        xs = []
        for i in range(d):
            g = zeros()
            if grad: g[i] = I(Fr(1))
            xs.append(D(X[i], g))
        sc = [sincos(xs[i], charts[i]) for i in range(d)]
        s1 = [a for a, b in sc]; c1 = [b for a, b in sc]
        s2 = [SK[i] * c1[i] - CK[i] * s1[i] for i in range(d)]
        c2 = [CK[i] * c1[i] + SK[i] * s1[i] for i in range(d)]
        e1sq = s1[0].sq()
        for i in range(1, d): e1sq = e1sq + s1[i].sq()
        e2sq = s2[0].sq()
        for i in range(1, d): e2sq = e2sq + s2[i].sq()
        return s1, c1, s2, c2, e1sq, e2sq
    def G_of(X, charts, sigma, grad=False):
        s1, c1, s2, c2, e1sq, e2sq = G_eval(X, charts, grad)
        e1 = e1sq.sqrt(); e2 = e2sq.sqrt()
        return [s1[a] * c1[a] / e1 - sigma * (s2[a] * c2[a] / e2) for a in range(d)]
    def magnitude_clear(X, charts):
        s1, c1, s2, c2, e1sq, e2sq = G_eval(X, charts, False)
        m1 = max(s1[i].v.sq().hi for i in range(d)); m2 = max(s2[i].v.sq().hi for i in range(d))
        # |grad eps|^2 = 1 - sum s^4/sum s^2 lies in [1 - max s^2, 1 - (sum s^2)/d]
        if 1 - m1 > 1 - e2sq.v.lo / d: return True
        if 1 - m2 > 1 - e1sq.v.lo / d: return True
        return False
    # numerical seeds (vectorized Newton in floating point)
    def seeds(sigma):
        g1 = np.linspace(-math.pi, math.pi, n_seed, endpoint=False) + math.pi / n_seed
        K = np.array(list(itertools.product(g1, repeat=d)))
        K0v = np.array(K0f)
        def G(k):
            k2 = K0v - k
            e1 = np.sqrt((np.sin(k) ** 2).sum(1))[:, None]; e2 = np.sqrt((np.sin(k2) ** 2).sum(1))[:, None]
            return np.sin(k) * np.cos(k) / e1 - sigma * np.sin(k2) * np.cos(k2) / e2
        k = K.copy()
        with np.errstate(all="ignore"):
            for it in range(60):
                g = G(k); h = 1e-7
                J = np.zeros((len(k), d, d))
                for a in range(d):
                    dk = np.zeros(d); dk[a] = h
                    J[:, :, a] = (G(k + dk) - G(k - dk)) / (2 * h)
                ok = np.abs(np.linalg.det(J)) > 1e-12
                step = np.zeros_like(k)
                step[ok] = np.linalg.solve(J[ok], g[ok][..., None])[..., 0]
                step = np.clip(step, -0.3, 0.3)
                k = k - step
            g = G(k)
        good = np.isfinite(g).all(1) & (np.linalg.norm(g, axis=1) < 1e-10)
        e1 = np.sqrt((np.sin(k) ** 2).sum(1)); e2 = np.sqrt((np.sin(K0v - k) ** 2).sum(1))
        good &= (e1 > 1e-6) & (e2 > 1e-6)
        roots = []
        for kk in np.mod(k[good] + math.pi, 2 * math.pi) - math.pi:
            if all(np.linalg.norm(np.mod(kk - r + math.pi, 2 * math.pi) - math.pi) > 1e-7 for r in roots): roots.append(kk)
        return roots
    def krawczyk(center, charts, sigma, rad):
        x = [Fr(c).limit_denominator(1 << 60) for c in center]
        X = [I(xi - rad, xi + rad) for xi in x]
        Gx = G_of([I(xi) for xi in x], charts, sigma, False)
        GX = G_of(X, charts, sigma, True)
        Jm = [[GX[a].g[b] for b in range(d)] for a in range(d)]
        Jc = np.array([[float(Jm[a][b].mid()) for b in range(d)] for a in range(d)])
        Yf = np.linalg.inv(Jc)
        Y = [[Fr(Yf[a, b]).limit_denominator(1 << 50) for b in range(d)] for a in range(d)]
        K = []
        for a in range(d):
            acc = I(x[a])
            for b in range(d): acc = acc - Y[a][b] * Gx[b].v
            for b in range(d):
                M = I.of(1 if a == b else 0)
                for c in range(d): M = M - Y[a][c] * Jm[c][b]
                acc = acc + M * (X[b] - x[b])
            K.append(acc)
        inside = all(K[a].lo > X[a].lo and K[a].hi < X[a].hi for a in range(d))
        # determinant of the interval Jacobian (cofactor expansion, interval arithmetic)
        def det(Mx):
            if len(Mx) == 1: return Mx[0][0]
            tot = I(Fr(0))
            for j in range(len(Mx)):
                minor = [row[:j] + row[j + 1:] for row in Mx[1:]]
                term = Mx[0][j] * det(minor)
                tot = tot + term if j % 2 == 0 else tot - term
            return tot
        return inside, det(Jm), X
    def chart_coord(kv, cc):
        if cc == 0:
            return math.tan(kv / 2) if abs(kv) <= math.pi / 2 + 0.3 else None
        k = kv if kv > 0 else kv + 2 * math.pi
        return 1 / math.tan(k / 2) if abs(k - math.pi) <= math.pi / 2 + 0.3 else None
    out = {}
    for sigma in (1, -1):
        rs = seeds(sigma); boxes = {}; dets = []; okK = True
        for r in rs:
            placed = False
            for charts in itertools.product((0, 1), repeat=d):
                coords = [chart_coord(r[a], charts[a]) for a in range(d)]
                if any(c is None for c in coords): continue
                ins, dt, X = krawczyk(coords, charts, sigma, Fr(1, 1 << 14))
                okK = okK and ins and not dt.contains0()
                dets.append(min(abs(dt.lo), abs(dt.hi))); boxes.setdefault(charts, []).append(X); placed = True
            okK = okK and placed
        disjoint = all(not all(not (A[i].hi < B[i].lo or A[i].lo > B[i].hi) for i in range(d))
                       for bl in boxes.values() for ia, A in enumerate(bl) for B in bl[ia + 1:])
        # exclusion
        def covered(X, bl):
            return any(all(X[i].lo >= B[i].lo and X[i].hi <= B[i].hi for i in range(d)) for B in bl)
        nbox = 0; stuck = 0
        for charts in itertools.product((0, 1), repeat=d):
            bl = boxes.get(charts, [])
            stack = [[I(Fr(-1), Fr(1)) for _ in range(d)]]
            while stack:
                X = stack.pop(); nbox += 1
                if covered(X, bl): continue
                cleared = False
                try:
                    G = G_of(X, charts, sigma, False)
                    if any(not g.v.contains0() for g in G): cleared = True
                except (ZeroDivisionError, ValueError):
                    pass
                if not cleared and magnitude_clear(X, charts): cleared = True
                if cleared: continue
                if X[0].width() < Fr(1, 1 << 40): stuck += 1; continue
                halves = [(I(Xi.lo, Xi.mid()), I(Xi.mid(), Xi.hi)) for Xi in X]
                for combo in itertools.product(*halves): stack.append(list(combo))
        out[sigma] = dict(n=len(rs), okK=okK, disjoint=disjoint, mindet=min(dets) if dets else None, nbox=nbox, stuck=stuck)
        print("   Z^%d, sigma = %+d: %d stationary points (numerical seeds); Krawczyk boxes certified: %s, pairwise disjoint per chart: %s; smallest |det| lower bound "
              "%.3e; exclusion boxes %d, uncleared %d  [%.0f s]" % (d, sigma, len(rs), okK, disjoint, float(min(dets)) if dets else float("nan"), nbox, stuck,
                                                                     time.time() - t_start), flush=True)
    return out

r2 = run_dim(2, [Fr(1, 3), Fr(2, 3)], 120)
ok2 = all(r2[s]["okK"] and r2[s]["disjoint"] and r2[s]["stuck"] == 0 for s in (1, -1))
check("C1 Z^2 at K0 = (2 atan(1/3), 2 atan(2/3)): every zero of grad eps(k1) - sigma grad eps(k2) away from the cone points lies in exactly one certified "
      "Krawczyk box (one zero each, interval Jacobian determinant excluding 0); sigma = +1 (bands (+,+), (-,-)): %d, sigma = -1 (bands (+,-), (-,+)): %d "
      "nondegenerate stationary points" % (r2[1]["n"], r2[-1]["n"]), ok2)
DO3 = "--no3d" not in sys.argv
if DO3:
    r3 = run_dim(3, [Fr(1, 3), Fr(2, 3), Fr(1, 4)], 36)
    ok3 = all(r3[s]["okK"] and r3[s]["disjoint"] and r3[s]["stuck"] == 0 for s in (1, -1))
    check("C2 Z^3 at K0 = (2 atan(1/3), 2 atan(2/3), 2 atan(1/4)): the same certificate: sigma = +1: %d, sigma = -1: %d nondegenerate stationary points"
          % (r3[1]["n"], r3[-1]["n"]), ok3)
counts = {s: r2[s]["n"] for s in (1, -1)}
print("")
print("TOTAL: PASS=%d FAIL=%d (%.0f s)" % (len(PASS), len(FAIL), time.time() - t_start))
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    extra = ("; on Z^3 at K0 = (2 atan(1/3), 2 atan(2/3), 2 atan(1/4)): %d, %d, %d and %d" % (r3[1]["n"], r3[-1]["n"], r3[-1]["n"], r3[1]["n"])) if DO3 else ""
    print("HIT: assumption (A') of block 143 certified: in exact rational interval arithmetic (Krawczyk boxes and exclusion boxes, cone neighbourhoods cleared "
          "by a magnitude test), the four pair bands at K0 = (2 atan(1/3), 2 atan(2/3)) on Z^2 have %d, %d, %d and %d stationary points away from the cone points, "
          "all nondegenerate%s" % (counts[1], counts[-1], counts[-1], counts[1], extra))
    print("SUMMARY: PROVED (A') at one K0 on Z^2%s, by an exact rational interval certificate" % (" and at one K0 on Z^3" if DO3 else " (Z^3 not run)"))
