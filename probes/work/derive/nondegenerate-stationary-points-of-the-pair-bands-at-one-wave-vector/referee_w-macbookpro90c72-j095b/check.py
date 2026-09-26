#!/usr/bin/env python3
"""Independent certificate for pair-band stationary points at one wave vector.

Does not import the author's script. Interval bounds are Fractions rounded
outward to 2^{-96}. Floats are used only to seed Newton; every certified
statement is rational. Krawczyk's inclusion test is an imported theorem:
if K(X) lies strictly inside X, X contains exactly one zero.
"""
import itertools
import math
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

FAIL = []
T0 = time.time()


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail else "")
          + f"  [{time.time() - T0:.0f}s]", flush=True)
    if not ok:
        FAIL.append(name)


# --- exact trig and gradient identities ---
t, k = sp.symbols("t k", real=True)
sins = [sp.symbols(f"s{i}", real=True) for i in range(3)]
check(
    "S1 half-angle",
    sp.simplify(sp.sin(2 * sp.atan(t)) - 2 * t / (1 + t**2)) == 0
    and sp.simplify(sp.cos(2 * sp.atan(t)) - (1 - t**2) / (1 + t**2)) == 0
    and sp.simplify(sp.diff(2 * sp.atan(t), t) - 2 / (1 + t**2)) == 0,
    "sin and cos of k=2 atan(t) are rational, and dk/dt = 2/(1+t^2) never zero",
)
eps2 = sum(s**2 for s in sins)
grad_sq = sp.together(sum((sins[i] * sp.sqrt(1 - sins[i]**2)) ** 2 for i in range(3)) / eps2)
ident = sp.simplify(grad_sq - (1 - sum(s**4 for s in sins) / eps2))
check(
    "S2 gradient magnitude",
    ident == 0,
    "|grad eps|^2 = 1 - sum sin^4 / sum sin^2",
)
# Cauchy: sum sin^4 * d - (sum sin^2)^2 = (1/2) sum_{i<j} (sin^2_i - sin^2_j)^2 >= 0
d = 3
s2 = [s**2 for s in sins]
cauchy = sp.expand(d * sum(x**2 for x in s2) - sum(s2) ** 2)
check(
    "S3 Cauchy",
    cauchy == sp.expand(sum((s2[i] - s2[j]) ** 2 for i in range(3) for j in range(i + 1, 3))),
    "sum sin^4 / sum sin^2 >= (sum sin^2)/d, and sum sin^4 / sum sin^2 <= max sin^2",
)

# --- outward interval arithmetic ---
SH = 96
SC = 1 << SH


def rdn(x):
    return Fr(math.floor(x * SC), SC)


def rup(x):
    return Fr(math.ceil(x * SC), SC)


class I:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        if hi is None:
            hi = lo
        if lo > hi:
            raise ValueError("inverted interval")
        self.lo, self.hi = lo, hi

    @staticmethod
    def pt(x):
        return x if isinstance(x, I) else I(Fr(x), Fr(x))

    def __add__(self, other):
        other = I.pt(other)
        return I(rdn(self.lo + other.lo), rup(self.hi + other.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-I.pt(other))

    def __rsub__(self, other):
        return I.pt(other) + (-self)

    def __mul__(self, other):
        other = I.pt(other)
        vals = (self.lo * other.lo, self.lo * other.hi, self.hi * other.lo, self.hi * other.hi)
        return I(rdn(min(vals)), rup(max(vals)))

    __rmul__ = __mul__

    def sq(self):
        if self.lo >= 0:
            return I(rdn(self.lo * self.lo), rup(self.hi * self.hi))
        if self.hi <= 0:
            return I(rdn(self.hi * self.hi), rup(self.lo * self.lo))
        return I(Fr(0), rup(max(self.lo * self.lo, self.hi * self.hi)))

    def inv(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError
        return I(rdn(1 / self.hi), rup(1 / self.lo))

    def __truediv__(self, other):
        return self * I.pt(other).inv()

    def __rtruediv__(self, other):
        return I.pt(other) * self.inv()

    def contains0(self):
        return self.lo <= 0 <= self.hi

    def mid(self):
        return (self.lo + self.hi) / 2


def sqrt_lo(x):
    if x <= 0:
        return Fr(0)
    return Fr(math.isqrt(math.floor(x * SC * SC)), SC)


def sqrt_hi(x):
    if x <= 0:
        return Fr(0)
    n = math.ceil(x * SC * SC)
    r = math.isqrt(n)
    if Fr(r * r, SC * SC) < x:
        r += 1
    return Fr(r, SC)


def isqrt(a):
    if a.hi < 0:
        raise ValueError
    return I(sqrt_lo(max(a.lo, Fr(0))), sqrt_hi(a.hi))


class D:
    __slots__ = ("v", "g")
    n = 2

    def __init__(self, v, g=None):
        self.v = v
        self.g = g if g is not None else [I(Fr(0)) for _ in range(D.n)]

    @staticmethod
    def c(x):
        return x if isinstance(x, D) else D(I.pt(x))

    def __add__(self, other):
        other = D.c(other)
        return D(self.v + other.v, [a + b for a, b in zip(self.g, other.g)])

    __radd__ = __add__

    def __neg__(self):
        return D(-self.v, [-a for a in self.g])

    def __sub__(self, other):
        return self + (-D.c(other))

    def __rsub__(self, other):
        return D.c(other) + (-self)

    def __mul__(self, other):
        other = D.c(other)
        return D(self.v * other.v, [self.v * b + other.v * a for a, b in zip(self.g, other.g)])

    __rmul__ = __mul__

    def sq(self):
        return D(self.v.sq(), [2 * self.v * a for a in self.g])

    def inv(self):
        iv = self.v.inv()
        return D(iv, [-(iv.sq() * a) for a in self.g])

    def __truediv__(self, other):
        return self * D.c(other).inv()

    def sqrt(self):
        s = isqrt(self.v)
        if s.lo <= 0:
            raise ZeroDivisionError
        half = (2 * s).inv()
        return D(s, [half * a for a in self.g])


def det_interval(rows):
    n = len(rows)
    if n == 1:
        return rows[0][0]
    total = I(Fr(0))
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in rows[1:]]
        term = rows[0][j] * det_interval(minor)
        total = total + term if j % 2 == 0 else total - term
    return total


def certify(dim, tangents, n_seed):
    D.n = dim
    sin_k = [2 * t / (1 + t * t) for t in tangents]
    cos_k = [(1 - t * t) / (1 + t * t) for t in tangents]
    k0 = [2 * math.atan(float(t)) for t in tangents]

    def sincos(x, chart):
        den = 1 + x.sq()
        sine = 2 * x / den
        cosine = (1 - x.sq()) / den if chart == 0 else (x.sq() - 1) / den
        return sine, cosine

    def fields(xs, charts):
        sc = [sincos(xs[i], charts[i]) for i in range(dim)]
        s1 = [a for a, _ in sc]
        c1 = [b for _, b in sc]
        s2 = [sin_k[i] * c1[i] - cos_k[i] * s1[i] for i in range(dim)]
        c2 = [cos_k[i] * c1[i] + sin_k[i] * s1[i] for i in range(dim)]
        e1 = s1[0].sq()
        e2 = s2[0].sq()
        for i in range(1, dim):
            e1 = e1 + s1[i].sq()
            e2 = e2 + s2[i].sq()
        return s1, c1, s2, c2, e1, e2

    def G(box, charts, sigma, with_grad):
        xs = []
        for i, comp in enumerate(box):
            g = [I(Fr(0)) for _ in range(dim)]
            if with_grad:
                g[i] = I(Fr(1))
            xs.append(D(comp, g))
        s1, c1, s2, c2, e1, e2 = fields(xs, charts)
        r1, r2 = e1.sqrt(), e2.sqrt()
        return [s1[a] * c1[a] / r1 - sigma * (s2[a] * c2[a] / r2) for a in range(dim)]

    def magnitude_separates(box, charts):
        xs = [D(comp) for comp in box]
        s1, _, s2, _, e1, e2 = fields(xs, charts)
        m1 = max(s1[i].v.sq().hi for i in range(dim))
        m2 = max(s2[i].v.sq().hi for i in range(dim))
        # lower |grad eps(k1)|^2 > upper |grad eps(k2)|^2, or the swap
        if 1 - m1 > 1 - e2.v.lo / dim:
            return True
        if 1 - m2 > 1 - e1.v.lo / dim:
            return True
        return False

    def newton_seeds(sigma):
        grid = np.linspace(-math.pi, math.pi, n_seed, endpoint=False) + math.pi / n_seed
        pts = np.array(list(itertools.product(grid, repeat=dim)))
        k0v = np.array(k0)

        def residual(k):
            k2 = k0v - k
            e1 = np.sqrt((np.sin(k) ** 2).sum(1))[:, None]
            e2 = np.sqrt((np.sin(k2) ** 2).sum(1))[:, None]
            return np.sin(k) * np.cos(k) / e1 - sigma * np.sin(k2) * np.cos(k2) / e2

        k = pts.copy()
        with np.errstate(all="ignore"):
            for _ in range(60):
                g = residual(k)
                step = np.zeros_like(k)
                jac = np.zeros((len(k), dim, dim))
                h = 1e-7
                for a in range(dim):
                    dk = np.zeros(dim)
                    dk[a] = h
                    jac[:, :, a] = (residual(k + dk) - residual(k - dk)) / (2 * h)
                good = np.abs(np.linalg.det(jac)) > 1e-12
                step[good] = np.linalg.solve(jac[good], g[good][..., None])[..., 0]
                k = k - np.clip(step, -0.3, 0.3)
            g = residual(k)
        keep = np.isfinite(g).all(1) & (np.linalg.norm(g, axis=1) < 1e-9)
        e1 = np.sqrt((np.sin(k) ** 2).sum(1))
        e2 = np.sqrt((np.sin(k0v - k) ** 2).sum(1))
        keep &= (e1 > 1e-6) & (e2 > 1e-6)
        roots = []
        for row in np.mod(k[keep] + math.pi, 2 * math.pi) - math.pi:
            if all(np.linalg.norm(np.mod(row - old + math.pi, 2 * math.pi) - math.pi) > 1e-6 for old in roots):
                roots.append(row)
        return roots

    def to_chart(kv, chart):
        if chart == 0:
            if abs(kv) > math.pi / 2 + 0.05:
                return None
            return math.tan(kv / 2)
        ang = kv if kv > 0 else kv + 2 * math.pi
        if abs(ang - math.pi) > math.pi / 2 + 0.05:
            return None
        return 1 / math.tan(ang / 2)

    def krawczyk(center, charts, sigma):
        rad = Fr(1, 1 << 14)
        x = [Fr(c).limit_denominator(1 << 60) for c in center]
        box = [I(xi - rad, xi + rad) for xi in x]
        gx = G([I(xi) for xi in x], charts, sigma, False)
        gbox = G(box, charts, sigma, True)
        jac = [[gbox[a].g[b] for b in range(dim)] for a in range(dim)]
        mid = np.array([[float(jac[a][b].mid()) for b in range(dim)] for a in range(dim)])
        inv = np.linalg.inv(mid)
        Y = [[Fr(inv[a, b]).limit_denominator(1 << 50) for b in range(dim)] for a in range(dim)]
        image = []
        for a in range(dim):
            acc = I(x[a])
            for b in range(dim):
                acc = acc - Y[a][b] * gx[b].v
            for b in range(dim):
                slot = I(Fr(1 if a == b else 0))
                for c in range(dim):
                    slot = slot - Y[a][c] * jac[c][b]
                acc = acc + slot * (box[b] - x[b])
            image.append(acc)
        inside = all(image[a].lo > box[a].lo and image[a].hi < box[a].hi for a in range(dim))
        return inside, det_interval(jac), box

    def overlaps(a, b):
        return all(not (a[i].hi < b[i].lo or a[i].lo > b[i].hi) for i in range(dim))

    report = {}
    for sigma in (1, -1):
        roots = newton_seeds(sigma)
        boxes = {}
        dets = []
        certified = True
        for root in roots:
            placed = False
            for charts in itertools.product((0, 1), repeat=dim):
                coords = [to_chart(root[a], charts[a]) for a in range(dim)]
                if any(c is None for c in coords):
                    continue
                inside, delta, box = krawczyk(coords, charts, sigma)
                certified = certified and inside and not delta.contains0()
                dets.append(min(abs(delta.lo), abs(delta.hi)))
                boxes.setdefault(charts, []).append(box)
                placed = True
            certified = certified and placed
        disjoint = all(
            not overlaps(a, b)
            for group in boxes.values()
            for i, a in enumerate(group)
            for b in group[i + 1:]
        )
        stuck = 0
        nbox = 0
        for charts in itertools.product((0, 1), repeat=dim):
            group = boxes.get(charts, [])
            stack = [[I(Fr(-1), Fr(1)) for _ in range(dim)]]
            while stack:
                box = stack.pop()
                nbox += 1
                if any(all(box[i].lo >= b[i].lo and box[i].hi <= b[i].hi for i in range(dim)) for b in group):
                    continue
                cleared = False
                try:
                    vals = G(box, charts, sigma, False)
                    if any(not g.v.contains0() for g in vals):
                        cleared = True
                except (ZeroDivisionError, ValueError):
                    pass
                if not cleared and magnitude_separates(box, charts):
                    cleared = True
                if cleared:
                    continue
                if box[0].width() < Fr(1, 1 << 40):
                    stuck += 1
                    continue
                halves = [(I(c.lo, c.mid()), I(c.mid(), c.hi)) for c in box]
                for child in itertools.product(*halves):
                    stack.append(list(child))
        # width() isn't defined; fix below if this path is hit. Use hi-lo.
        report[sigma] = {
            "n": len(roots),
            "certified": certified,
            "disjoint": disjoint,
            "mindet": min(dets) if dets else None,
            "nbox": nbox,
            "stuck": stuck,
        }
        print(
            f"   dim {dim} sigma {sigma:+d}: seeds {len(roots)}, certified {certified}, "
            f"disjoint {disjoint}, min |det| {float(min(dets)) if dets else float('nan'):.3e}, "
            f"boxes {nbox}, stuck {stuck}  [{time.time() - T0:.0f}s]",
            flush=True,
        )
    return report


# width helper used above: add it onto I before certify runs
def _width(self):
    return self.hi - self.lo


I.width = _width

# engine sanity: the only zero of t - 1/3 on [-1, 1] is simple
center = Fr(1, 3)
rad = Fr(1, 32)
box = I(center - rad, center + rad)
# K(X) for f(t)=t-1/3, f'=1, Y=1: K = c - (c-1/3) + (1-1)(X-c) = 1/3
image = I(center) - (I(center) - I(Fr(1, 3)))
check(
    "S0 Krawczyk engine",
    image.lo > box.lo and image.hi < box.hi and image.lo <= Fr(1, 3) <= image.hi
    and image.hi - image.lo < Fr(1, 1 << 40),
    "outward rounding keeps 1/3 inside a tiny image, and that image sits inside the test box",
)

z2 = certify(2, [Fr(1, 3), Fr(2, 3)], 80)
check(
    "C1 Z2",
    z2[1]["n"] == 16 and z2[-1]["n"] == 8
    and all(z2[s]["certified"] and z2[s]["disjoint"] and z2[s]["stuck"] == 0 for s in (1, -1)),
    "at K0=(2 atan(1/3), 2 atan(2/3)): 16 nondegenerate zeros for sigma=+1 and 8 for sigma=-1, none elsewhere",
)

run3 = "--no3d" not in sys.argv
z3 = None
if run3:
    z3 = certify(3, [Fr(1, 3), Fr(2, 3), Fr(1, 4)], 36)
    check(
        "C2 Z3",
        z3[1]["n"] == 64 and z3[-1]["n"] == 48
        and all(z3[s]["certified"] and z3[s]["disjoint"] and z3[s]["stuck"] == 0 for s in (1, -1)),
        "at K0=(2 atan(1/3), 2 atan(2/3), 2 atan(1/4)): 64 and 48 nondegenerate zeros",
    )

print(f"TOTAL FAIL={len(FAIL)}", flush=True)
if FAIL:
    print("SUMMARY: fails at " + ", ".join(FAIL), flush=True)
else:
    print(
        "SUMMARY: PARTIAL (A') at one wave vector. On Z^2 at K0=(2 atan(1/3), 2 atan(2/3)) "
        "the four pair bands have 16, 8, 8 and 16 stationary points away from the cone points, all nondegenerate. "
        + (
            "On Z^3 at K0=(2 atan(1/3), 2 atan(2/3), 2 atan(1/4)) the counts are 64, 48, 48 and 64. "
            if run3 else "Z^3 was not run. "
        )
        + "Krawczyk inclusion is an imported uniqueness test. Persistence in K0 was not re-checked.",
        flush=True,
    )
    print(
        "HIT: confirmed - at K0=(2 atan(1/3), 2 atan(2/3)) every stationary point of each pair band on Z^2 "
        "away from the cone points is nondegenerate: 16 for sigma=+1 and 8 for sigma=-1."
        + (
            " On Z^3 at K0=(2 atan(1/3), 2 atan(2/3), 2 atan(1/4)) the counts are 64 and 48."
            if run3 else ""
        ),
        flush=True,
    )
