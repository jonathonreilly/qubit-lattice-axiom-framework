#!/usr/bin/env python3
"""check.py for J:derive:an-exact-enclosure-of-beta-for-forward-streaming:a1 (worker w-macbookpro9927a-j956c, claude-opus-5-5).

Certified enclosures of beta = <|s_1 s_2| W_12> for block 118's staircase and axes-and-faces rules, in exact rational
arithmetic: interval Darboux sums with rationals (outward rounding to the grid 2^-64, lower ends down, upper ends up),
rational square-root bounds by integer square roots, and pi between 333/106 and 355/113.

Families
  Q  pinned sources (block 118 on its branch; the axes-and-faces maximal merge as defined in attempt #9127; the task)
  W  both rules at exact rational points of the sphere: weights >= 0, total 1, mean s, forward and sign-compatible, and
     sum_{m<n} |s_m s_n| W_mn equal to the sector integrands used below
  G  the reduction to one sector in gnomonic coordinates (symbolic): Jacobian 1/rho^3, the integrands, the identity
     H = 1 - q/(1+rho), q <= x + y, and beta = (4/pi) * I
  E  certified enclosures: two controls with known values (sector area pi/12; <|s_1|^3> sector integral pi/16), then
     beta_staircase > 1/16 > beta_af, and the isotropic mixing weight lambda*
"""
import hashlib
import json
import os
import subprocess
import sys
import time
from fractions import Fraction as F
from math import isqrt

import sympy as sp

T0 = time.time()
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *([os.pardir] * 5)))
FAILS = []


def rep(fam, ok, msg):
    if not ok:
        FAILS.append(fam)
    print(f"[{fam}] {'PASS' if ok else 'FAIL'} {msg}")
    sys.stdout.flush()


# ------------------------------------------------------------------ Q
B118 = ("3eaf52ff8e11f79cc3ff315391fece2bdcea4518",
        "docs/ADMISSIBILITY_RULE_FORWARD_STREAMING_ON_THE_26_NEIGHBOURS_ISOTROPY_OF_THE_SECOND_ORDER_TERM_IS_ONE_NUMBER_AND"
        "_CONSTANT_RATE_RULES_CAPTURE_ISOTROPICALLY_BOUNDED_THEOREM_NOTE_2026-09-24.md",
        "ac3ccbb01488076b1f11b05b9e12d12f6fc457b4da6d8027037c9c2ca79c65bb",
        ["`M_kl(s) = Σ_d a(s, d) d_k d_l` and `T_ijkl = ⟨s_i s_j M_kl(s)⟩` over the uniform sphere.",
         "`W₁₂` is the rate of steps that move both coordinates 1 and 2.",
         "It is isotropic iff `β = 1/16`.",
         "Put weight `(1 − t)[(a − b)u_i + (b − c)(u_i + u_j) + c(u_i + u_j + u_k)] + t[a u_i + b u_j + c u_k]`, with `t = (1 − a)/(b + c)`.",
         "Merge weight from pairs of axes into face diagonals, as far as the budgets allow, and scale the merge so the total is 1.",
         "Quadrature gives `β_stair = 0.064898…` and `β_af = 0.056128…`."],
        "physics-loop/admissibility-induced-law-block118-forward-streaming-on-the-26-neighbours-isotropy-is-one-number-20260924")
A9127 = ("818f59167fe906d91f4e173e331b63f70bb1d824",
         "probes/work/derive/isotropic-streaming-clause/w-macbookpro9927a-jfad7/ATTEMPT.md",
         "3056ef9385ababb18ad0fc7a3da458cb69aedaf6a723777a79d9619af46f9817",
         ["- `(b, c, 0)` if `a ≥ b + c`, with `Σz* = b + c`;",
          "otherwise `((a+b−c)/2, (a−b+c)/2, (−a+b+c)/2)`, with `Σz* = (a+b+c)/2` and every budget tight.",
          "Scale by `θ = (a + b + c − 1)/Σz*`."], None)
TASKQ = ("44cbb7bf6398b9742a0aa5d7ff8e4611ee838817", "J:derive:an-exact-enclosure-of-beta-for-forward-streaming:a1",
         ["(a) prove beta_staircase > 1/16 exactly - a certified enclosure in exact rational arithmetic",
          "and likewise beta_af < 1/16", "HIT: (a) or (b) with an exact certificate."])


def git_show(spec, branch=None):
    r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "--quiet", "origin", branch or spec.split(":")[0]], cwd=REPO, capture_output=True)
        r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def fam_Q():
    ok, msg = True, []
    for tag, (c, p, h, quotes, br) in (("block118", B118), ("attempt9127", A9127)):
        b = git_show(f"{c}:{p}", br)
        if b is None:
            rep("Q", False, f"{tag} unreadable")
            return
        good = hashlib.sha256(b).hexdigest() == h
        n = sum(q in b.decode() for q in quotes)
        ok &= good and n == len(quotes)
        msg.append(f"{tag}@{c[:8]} {'sha ok' if good else 'SHA MISMATCH'} {n}/{len(quotes)}")
    b = git_show(f"{TASKQ[0]}:probes/TASKS.json")
    what = next((t["what"] for t in json.loads(b.decode()) if t["id"] == TASKQ[1]), "") if b else ""
    n = sum(q in what for q in TASKQ[2])
    ok &= n == len(TASKQ[2])
    msg.append(f"task@{TASKQ[0][:8]} {n}/{len(TASKQ[2])}")
    rep("Q", ok, "; ".join(msg))


# ------------------------------------------------------------------ W: the two rules at rational points
def rules(s):
    """Return (staircase weights, axes-and-faces weights) as dicts target-tuple -> Fraction, for a rational unit s."""
    order = sorted(range(3), key=lambda m: -abs(s[m]))
    i, j, k = order
    a, b, c = abs(s[i]), abs(s[j]), abs(s[k])
    u = [tuple((1 if s[m] > 0 else -1) if q == m else 0 for q in range(3)) for m in range(3)]

    def add(*vs):
        return tuple(sum(v[q] for v in vs) for q in range(3))
    st = {}

    def put(w, d, x):
        if x != 0:
            w[d] = w.get(d, F(0)) + x
    t = (1 - a) / (b + c)
    put(st, u[i], (1 - t) * (a - b) + t * a)
    put(st, add(u[i], u[j]), (1 - t) * (b - c))
    put(st, add(u[i], u[j], u[k]), (1 - t) * c)
    put(st, u[j], t * b)
    put(st, u[k], t * c)
    if a >= b + c:
        z = {(i, j): b, (i, k): c, (j, k): F(0)}
        tot = b + c
    else:
        z = {(i, j): (a + b - c) / 2, (i, k): (a - b + c) / 2, (j, k): (-a + b + c) / 2}
        tot = (a + b + c) / 2
    th = (a + b + c - 1) / tot
    af = {}
    mag = {i: a, j: b, k: c}
    for m in range(3):
        put(af, u[m], mag[m] - th * sum(v for (p, q), v in z.items() if m in (p, q)))
    for (p, q), v in z.items():
        put(af, add(u[p], u[q]), th * v)
    return st, af, (a, b, c)


def fam_W():
    ok, npts = True, 0
    for p in range(-7, 8):
        for q in range(-7, 8):
            for den in (5, 7, 11):
                uu, vv = F(p, den), F(q, den)
                n2 = 1 + uu * uu + vv * vv
                s = (2 * uu / n2, 2 * vv / n2, (1 - uu * uu - vv * vv) / n2)
                if sum(1 for x in s if x == 0) >= 2:
                    continue
                npts += 1
                st, af, (a, b, c) = rules(s)
                sig = a + b + c
                for w in (st, af):
                    ok &= all(x >= 0 for x in w.values()) and sum(w.values()) == 1
                    ok &= all(sum(x * d[m] for d, x in w.items()) == s[m] for m in range(3))
                    ok &= all(sum(d[m] * s[m] for m in range(3)) > 0 for d in w)                       # forward
                    ok &= all(d[m] in (0, (1 if s[m] > 0 else -1)) for d in w for m in range(3))       # sign-compatible
                Wsum = lambda w: sum(abs(s[m] * s[n]) * sum(x for d, x in w.items() if d[m] != 0 and d[n] != 0)
                                     for m in range(3) for n in range(m + 1, 3))
                if b + c > 0:
                    ok &= Wsum(st) == (sig - 1) * (a * b * b + a * c * c + b * c * c) / (b + c)
                    if a >= b + c:
                        ok &= Wsum(af) == (sig - 1) * (a * b * b + a * c * c) / (b + c)
                    else:
                        ok &= Wsum(af) == (sig - 1) * (a * b * (a + b - c) + a * c * (a - b + c) + b * c * (-a + b + c)) / sig
    rep("W", ok, f"{npts} exact rational points of the sphere (inverse stereographic images): both rules have weights >= 0, "
                 "total 1, mean exactly s, every target forward and sign-compatible; sum_{m<n}|s_m s_n| W_mn equals "
                 "(sigma-1)(ab^2+ac^2+bc^2)/(b+c) for the staircase and, for axes-and-faces, (sigma-1)(ab^2+ac^2)/(b+c) if "
                 "a >= b+c, else (sigma-1)(ab(a+b-c)+ac(a-b+c)+bc(-a+b+c))/sigma (a >= b >= c sorted |s_m|, sigma = a+b+c)")


# ------------------------------------------------------------------ G: reduction to the gnomonic triangle
def fam_G():
    ok = True
    x, y = sp.symbols("x y", positive=True)
    rho = sp.sqrt(1 + x ** 2 + y ** 2)
    S = sp.Matrix([1, x, y]) / rho
    cr = S.diff(x).cross(S.diff(y))
    ok &= sp.simplify(cr.dot(cr) - 1 / (1 + x ** 2 + y ** 2) ** 3) == 0     # |dS/dx x dS/dy|^2 = rho^-6
    J = rho ** -3
    a, b, c = 1 / rho, x / rho, y / rho
    sig = a + b + c
    g_st = sp.simplify((sig - 1) * (a * b ** 2 + a * c ** 2 + b * c ** 2) / (b + c) * J)
    H = 1 - ((x ** 2 + y ** 2) / (x + y)) / (1 + rho)
    ok &= sp.simplify(g_st - H * (x ** 2 + y ** 2 + x * y ** 2) / (1 + x ** 2 + y ** 2) ** 3) == 0
    ok &= sp.simplify((1 + x + y - rho) / (x + y) - H) == 0
    g_af1 = sp.simplify((sig - 1) * (a * b ** 2 + a * c ** 2) / (b + c) * J)
    ok &= sp.simplify(g_af1 - H * (x ** 2 + y ** 2) / (1 + x ** 2 + y ** 2) ** 3) == 0
    g_af2 = sp.simplify((sig - 1) * (a * b * (a + b - c) + a * c * (a - b + c) + b * c * (-a + b + c)) / sig * J)
    N2 = x + y + x ** 2 + y ** 2 - 3 * x * y + x ** 2 * y + x * y ** 2
    ok &= sp.simplify(g_af2 - (1 - rho / (1 + x + y)) * N2 / (1 + x ** 2 + y ** 2) ** 3) == 0
    ok &= sp.expand((x + y) ** 2 - (x ** 2 + y ** 2) - 2 * x * y) == 0          # q <= x + y since 2xy >= 0
    ok &= sp.simplify(((a ** 3 + b ** 3 + c ** 3) * J) - (1 + x ** 3 + y ** 3) / (1 + x ** 2 + y ** 2) ** 3) == 0
    rep("G", ok, "sector {s1 >= s2 >= s3 >= 0} = {s = (1,x,y)/rho : 0 <= y <= x <= 1}, dS = dx dy/rho^3 (symbolic); "
                 "beta = (1/3)<sum_{m<n}|s_m s_n|W_mn> = (1/3)(12/pi) * sector integral = (4/pi) I (cubic covariance, "
                 "48 sectors of area pi/12); integrands g_st = H (x^2+y^2+xy^2)/(1+x^2+y^2)^3, g_af = H (x^2+y^2)/(1+x^2+y^2)^3 "
                 "for x+y <= 1 and (1 - rho/(1+x+y)) N2/(1+x^2+y^2)^3 for x+y >= 1, H = 1 - q/(1+rho), q = (x^2+y^2)/(x+y) "
                 "<= x+y (so H is bounded at the axis corner); the kink of axes-and-faces is the line x + y = 1")


# ------------------------------------------------------------------ E: certified enclosures
class Iv:
    __slots__ = ("lo", "hi")
    SH = 64

    def __init__(self, lo, hi=None):
        lo = F(lo)
        hi = F(lo if hi is None else hi)
        assert lo <= hi
        self.lo = F((lo.numerator << Iv.SH) // lo.denominator, 1 << Iv.SH)
        self.hi = F(-((-hi.numerator << Iv.SH) // hi.denominator), 1 << Iv.SH)

    def __add__(s, o):
        o = o if isinstance(o, Iv) else Iv(o)
        return Iv(s.lo + o.lo, s.hi + o.hi)
    __radd__ = __add__

    def __sub__(s, o):
        o = o if isinstance(o, Iv) else Iv(o)
        return Iv(s.lo - o.hi, s.hi - o.lo)

    def __rsub__(s, o):
        return Iv(o) - s

    def __mul__(s, o):
        o = o if isinstance(o, Iv) else Iv(o)
        p = (s.lo * o.lo, s.lo * o.hi, s.hi * o.lo, s.hi * o.hi)
        return Iv(min(p), max(p))
    __rmul__ = __mul__

    def __truediv__(s, o):
        o = o if isinstance(o, Iv) else Iv(o)
        assert o.lo > 0
        return s * Iv(1 / o.hi, 1 / o.lo)


DSQ = 10 ** 9


def sqrt_lo(v):
    return F(isqrt(v.numerator * DSQ * DSQ // v.denominator), DSQ)


def sqrt_hi(v):
    n = -(-v.numerator * DSQ * DSQ // v.denominator)
    r = isqrt(n)
    return F(r + (1 if r * r < n else 0), DSQ)


def cell(x0, x1, y0, y1, which):
    X, Y = Iv(x0, x1), Iv(y0, y1)
    r2lo, r2hi = 1 + x0 * x0 + y0 * y0, 1 + x1 * x1 + y1 * y1
    rho = Iv(sqrt_lo(r2lo), sqrt_hi(r2hi))
    inv6 = Iv(1 / r2hi ** 3, 1 / r2lo ** 3)
    if which == "area":
        return Iv(1 / rho.hi ** 3, 1 / rho.lo ** 3)
    if which == "cube":
        return Iv(1 + x0 ** 3 + y0 ** 3, 1 + x1 ** 3 + y1 ** 3) * inv6
    q_lo = (x0 * x0 + y0 * y0) / (x1 + y1)
    q_hi = x1 + y1 if x0 + y0 == 0 else min(x1 + y1, (x1 * x1 + y1 * y1) / (x0 + y0))
    H = Iv(1 - q_hi / (1 + rho.lo), 1 - q_lo / (1 + rho.hi))
    if which == "stair":
        return H * Iv(x0 * x0 + y0 * y0 + x0 * y0 * y0, x1 * x1 + y1 * y1 + x1 * y1 * y1) * inv6
    parts = []
    if x0 + y0 <= 1:
        parts.append(H * Iv(x0 * x0 + y0 * y0, x1 * x1 + y1 * y1) * inv6)
    if x1 + y1 >= 1:
        N2 = X + Y + X * X + Y * Y - 3 * X * Y + X * X * Y + X * Y * Y
        parts.append((1 - rho / (1 + X + Y)) * N2 * inv6)
    return Iv(min(p.lo for p in parts), max(p.hi for p in parts))


def integrate(which, N):
    h = F(1, N)
    lo, hi = F(0), F(0)
    for i in range(N):
        for j in range(i + 1):
            bnd = cell(i * h, (i + 1) * h, j * h, (j + 1) * h, which)
            area = h * h if j < i else h * h / 2
            lo += bnd.lo * area
            hi += bnd.hi * area
        lo = F((lo.numerator << 64) // lo.denominator, 1 << 64)
        hi = F(-((-hi.numerator << 64) // hi.denominator), 1 << 64)
    return lo, hi


def fam_E():
    ok = True
    PI_LO, PI_HI = F(333, 106), F(355, 113)

    def atan_bounds(z, n=12):   # alternating series: partial sums bracket arctan z for 0 < z <= 1
        sums = [sum(F((-1) ** k) * z ** (2 * k + 1) / (2 * k + 1) for k in range(m + 1)) for m in (n, n + 1)]
        return min(sums), max(sums)
    l5, u5 = atan_bounds(F(1, 5))
    l239, u239 = atan_bounds(F(1, 239))
    pi_lo, pi_hi = 16 * l5 - 4 * u239, 16 * u5 - 4 * l239          # Machin: pi = 16 atan(1/5) - 4 atan(1/239)
    ok &= PI_LO < pi_lo <= pi_hi < PI_HI
    alo, ahi = integrate("area", 128)
    clo, chi = integrate("cube", 128)
    ok &= alo <= PI_HI / 12 and PI_LO / 12 <= ahi and clo <= PI_HI / 16 and PI_LO / 16 <= chi
    N = 1000
    slo, shi = integrate("stair", N)
    flo, fhi = integrate("af", N)
    bs = (4 * slo / PI_HI, 4 * shi / PI_LO)
    ba = (4 * flo / PI_HI, 4 * fhi / PI_LO)
    q = F(1, 16)
    ok &= bs[0] > q and ba[1] < q
    ok &= slo > F(355, 7232) and fhi < F(333, 6784)            # the same comparisons without dividing by pi
    lam = ((bs[0] - q) / (bs[1] - ba[0]), (bs[1] - q) / (bs[0] - ba[1]))
    ok &= 0 < lam[0] <= lam[1] < 1
    ok &= bs[0] < F(6489844, 10 ** 8) < bs[1] and ba[0] < F(5612879, 10 ** 8) < ba[1]
    rep("E", ok, f"333/106 < pi < 355/113 certified by Machin's formula with alternating-series brackets; controls: sector area enclosed in [{float(alo):.5f}, {float(ahi):.5f}] (pi/12 = 0.26180), <a^3+b^3+c^3> "
                 f"sector integral in [{float(clo):.5f}, {float(chi):.5f}] (pi/16 = 0.19635); N = {N} (Darboux sums over "
                 f"{N * (N + 1) // 2} cells): I_stair in [{float(slo):.7f}, {float(shi):.7f}] > 355/7232 > pi/64, so beta_stair in "
                 f"[{float(bs[0]):.6f}, {float(bs[1]):.6f}] > 1/16; I_af in [{float(flo):.7f}, {float(fhi):.7f}] < 333/6784 < "
                 f"pi/64, so beta_af in [{float(ba[0]):.6f}, {float(ba[1]):.6f}] < 1/16; the isotropic mixture "
                 f"(1-lambda) staircase + lambda axes-and-faces exists, is unique, and has lambda* in [{float(lam[0]):.4f}, "
                 f"{float(lam[1]):.4f}]; attempt #9127's float values 0.06489844 and 0.05612879 lie inside")
    return bs, ba, lam


if __name__ == "__main__":
    fam_Q()
    fam_W()
    fam_G()
    bs, ba, lam = fam_E()
    print(f"runtime {time.time() - T0:.0f}s; failed families: {sorted(set(FAILS)) or 'none'}")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT check families {sorted(set(FAILS))}")
        sys.exit(1)
    print(f"SUMMARY: PROVED (a) with a certified enclosure in exact rational arithmetic: beta_staircase in "
          f"[{float(bs[0]):.6f}, {float(bs[1]):.6f}] > 1/16 and beta_axes-and-faces in [{float(ba[0]):.6f}, {float(ba[1]):.6f}] "
          f"< 1/16 (rational interval Darboux sums over the gnomonic sector, pi between 333/106 and 355/113); hence the "
          f"forward, sign-compatible, constant-rate mixture with isotropic fourth-rank streaming moment exists, with lambda* in "
          f"[{float(lam[0]):.4f}, {float(lam[1]):.4f}].")
    print(f"HIT: (a) exact certificate: beta_staircase > 1/16 > beta_axes-and-faces, with certified enclosures beta_staircase in "
          f"[{float(bs[0]):.6f}, {float(bs[1]):.6f}] and beta_axes-and-faces in [{float(ba[0]):.6f}, {float(ba[1]):.6f}] "
          f"(beta = (4/pi) times an integral over 0 <= y <= x <= 1 of an explicit function of x, y and sqrt(1+x^2+y^2), "
          f"bounded cell by cell in rational interval arithmetic); so block 118's isotropic mixture exists and is unique, "
          f"lambda* in [{float(lam[0]):.4f}, {float(lam[1]):.4f}].")
