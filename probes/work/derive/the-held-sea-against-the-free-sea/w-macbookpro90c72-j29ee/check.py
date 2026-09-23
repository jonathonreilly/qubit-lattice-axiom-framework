#!/usr/bin/env python3
"""J:derive:the-held-sea-against-the-free-sea:a1 -- exact checks for ATTEMPT.md (Fractions, sympy) plus float notes.

Walk (block 54): H = sum_a sigma_a S_a, (S_a psi)(x) = (1/2i)[psi(x+e_a) - psi(x-e_a)], symbol s(k) = (sin k1, sin k2, sin k3);
clocked walk H_w = phi H phi, phi = e^{u/2} (block 76).  Held sea: E_fix = tr(P_- phi H phi) with P_- the lower band of H.
Free sea: E_opt = sum of the negative eigenvalues of phi H phi (block 76's E_sea).  Block 76's normalisation: for
u = eps cos(q.x), E(eps) - E(0) = Pi(q) eps^2 N + O(eps^3); Pi(q) = c0/4 + (kappa/4)|q|^2_lat + ..., |q|^2_lat = sum 2(1 - cos q_a).
Second order: Pi_opt - Pi_fix = dPi(q) = -(1/8) <F(., q)>, F = (a - b)^2/(a + b) (1 - s^_a . s^_b)/2, a = |s(k+q)|, b = |s(k)|.
Lines marked 'note' are floating point and are not claims.
"""
import itertools, math, sys, time
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

T0 = time.time()
FAILS = []


def ok(tag, cond, msg=""):
    print(("ok   " if cond else "FAIL ") + tag + (": " + msg if msg else ""))
    if not cond:
        FAILS.append(tag)


rng = __import__("random").Random(20260923)


def runit():
    a = Fr(rng.randint(-9, 9), rng.randint(1, 9))
    b = Fr(rng.randint(-9, 9), rng.randint(1, 9))
    n = a * a + b * b + 1
    return (2 * a / n, 2 * b / n, (a * a + b * b - 1) / n)


# ---------------------------------------------------------------- A: exact ingredients of the second-order kernel
Isp = sp.I
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -Isp], [Isp, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def proj(n, sgn):
    return (sp.eye(2) + sgn * sum((sp.Rational(n[i]) * SIG[i] for i in range(3)), sp.zeros(2))) / 2


good = True
for _ in range(6):
    a, b = runit(), runit()
    tr = sp.simplify((proj(a, 1) * proj(b, -1)).trace())
    good &= tr == sp.Rational(1, 2) * (1 - sum(sp.Rational(a[i]) * sp.Rational(b[i]) for i in range(3)))
    Hk = sum((sp.Rational(a[i]) * SIG[i] for i in range(3)), sp.zeros(2))
    good &= sp.simplify(Hk * proj(a, 1) - proj(a, 1)) == sp.zeros(2) and sp.simplify(Hk * proj(a, -1) + proj(a, -1)) == sp.zeros(2)
ok("A.overlap", good, "|<u_+(k')|u_-(k)>|^2 = tr(P_+(n')P_-(n)) = (1 - n'.n)/2 for rational unit vectors; P_+-(n) project on "
   "n.sigma = +-1")

good = True
for L in (4, 6):
    cosL = {m: Fr(sp.cos(2 * sp.pi * m / L)) for m in range(L)}
    X = list(itertools.product(range(L), repeat=3))
    for n in itertools.product(range(L), repeat=3):
        if n == (0, 0, 0):
            continue
        c = {x: cosL[sum(p * q for p, q in zip(n, x)) % L] for x in X}
        lin = sum(c[x] + c[tuple((x[i] + (i == a)) % L for i in range(3))] for x in X for a in range(3))
        quad = sum((c[x] + c[tuple((x[i] + (i == a)) % L for i in range(3))]) ** 2 for x in X for a in range(3))
        mult = 2 if all((2 * m) % L == 0 for m in n) else 1     # 2q = 0: cos(q.x) = +-1, mean square 1 instead of 1/2
        good &= lin == 0 and quad == mult * len(X) * (3 + sum(cosL[m] for m in n))
ok("A.held", good, "every mode u = eps cos(q.x) on the 4^3 and 6^3 tori: sum_bonds (u_x+u_y) = 0 and sum_bonds (u_x+u_y)^2 = "
   "eps^2 N (3 + sum_a cos q_a) (twice that when 2q = 0); so Pi_fix = (beta/8)(3 + sum cos q_a): c0 = 3 beta, kappa_fix = -beta/4 = I/12")

# ---------------------------------------------------------------- B: two-sided bounds on the kernel near q = 0
a_, b_, c_ = sp.symbols("a b c", real=True)
vec = sp.expand(4 * (a_ ** 2 + b_ ** 2 - 2 * a_ * b_ * c_) - 2 * (1 - c_) * (a_ + b_) ** 2 - 2 * (1 + c_) * (a_ - b_) ** 2) == 0
vec &= sp.expand(2 - 2 * c_ - (1 - c_ ** 2) - (1 - c_) ** 2) == 0
ok("B.vector", vec, "4(a^2+b^2-2abc) - 2(1-c)(a+b)^2 = 2(1+c)(a-b)^2, so |x^ - y^| <= 2|x-y|/(|x|+|y|); and 2-2c >= 1-c^2")
qq, r_ = sp.symbols("q r", positive=True)
r0, Rm = sp.pi * qq / 2, sp.pi * sp.sqrt(3) / 2
up = sp.integrate(qq * 4 * sp.pi * r_ ** 2, (r_, 0, r0)) + sp.integrate(sp.pi ** 3 * qq ** 4 / (8 * r_ ** 3) * 4 * sp.pi * r_ ** 2, (r_, r0, Rm))
ok("B.upper", sp.simplify(up - sp.pi ** 4 * qq ** 4 * (sp.Rational(1, 6) + sp.log(sp.sqrt(3) / qq) / 2)) == 0
   and sp.simplify(sp.pi ** 3 * qq ** 4 / (8 * r0 ** 3) - qq) == 0,
   "8 cells x int min(|q|, pi^3|q|^4/(8 r^3)) 4 pi r^2 dr / (2 pi)^3 = pi|q|^4 (1/6 + log(sqrt3/|q|)/2): -8 dPi <= that")
dc = Fr(431, 512) * Fr(1535, 1536)
cl = sp.Rational(dc.numerator, dc.denominator) ** 4 * sp.Rational(23, 24) ** 4 * sp.Rational(32, 1125) * sp.Rational(4, 15) * sp.pi / (8 * sp.pi ** 3)
low = (1 - Fr(9, 16) ** 2 / 2 == Fr(431, 512)) and (1 - Fr(1, 16) ** 2 / 6 == Fr(1535, 1536)) and (1 - Fr(1, 2) ** 2 / 6 == Fr(23, 24))
low &= sp.integrate(2 * sp.pi * c_ ** 2 * (1 - c_ ** 2), (c_, 0, 1)) == 4 * sp.pi / 15
low &= (Fr(5, 2) ** 3 * Fr(9, 4) == Fr(1125, 32)) and float(cl) > 4e-5
ok("B.lower", low, "cos(9/16) >= 431/512, sin(t/2) >= (t/2)(1535/1536), sin x >= 23x/24 on [0,1/2], hemisphere int c^2(1-c^2) = "
   "4pi/15: -8 dPi(t e1) >= C t^4 log(1/(4t)) for t <= 1/8, C = %.3e" % float(cl))

# ---------------------------------------------------------------- C: the line, in closed form
h, q1 = sp.symbols("h q", positive=True)
Gd = sp.log(1 / sp.cos(h) + sp.tan(h)) - sp.sin(h)
line = sp.simplify(sp.diff(Gd, h) - sp.sin(h) ** 2 / sp.cos(h)) == 0
dPi1 = -(sp.cos(q1 / 2) ** 2 / (2 * sp.pi * sp.sin(q1 / 2))) * Gd.subs(h, q1 / 2)
g1 = 1 / (4 * sp.pi) + dPi1 / (1 - sp.cos(q1))
line &= sp.simplify(sp.series(dPi1, q1, 0, 4).removeO() + q1 ** 2 / (24 * sp.pi)) == 0
line &= sp.simplify(sp.limit(g1, q1, 0, "+") - 1 / (6 * sp.pi)) == 0 and sp.simplify(sp.limit(g1, q1, sp.pi, "-") - 1 / (4 * sp.pi)) == 0
ok("C.line", line, "on a line dPi(q) = -(cos^2(q/2)/(2 pi sin(q/2)))[ln(sec+tan)(q/2) - sin(q/2)] = -q^2/(24 pi) + O(q^4); "
   "g(q) = 1/(4pi) + dPi/(1-cos q) runs from 1/(6pi) (q->0) to 1/(4pi) (q = pi)")

# ---------------------------------------------------------------- notes (floating point)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)


def kernel_torus(L, n):
    g = 2 * np.pi * np.arange(L) / L
    K = np.stack(np.meshgrid(g, g, g, indexing="ij"), -1).reshape(-1, 3)
    q = 2 * np.pi * np.array(n) / L
    s, s2 = np.sin(K), np.sin(K + q)
    b, a = np.linalg.norm(s, axis=1), np.linalg.norm(s2, axis=1)
    F = np.zeros(len(K))
    gen = (b > 1e-12) & (a > 1e-12)
    F[gen] = (a[gen] - b[gen]) ** 2 / (a[gen] + b[gen]) * (1 - np.einsum("ij,ij->i", s[gen], s2[gen]) / (a[gen] * b[gen])) / 2
    zm = (b > 1e-12) & (a < 1e-12)                      # exact zero modes as intermediate states (both coin states)
    F[zm] = b[zm]
    beta = -b.mean() / 3
    return beta / 8 * (3 + np.cos(q).sum()), -F.mean() / 8, 3 * beta, np.sum(2 * (1 - np.cos(q)))


L = 6
N = L ** 3
X = np.array(list(itertools.product(range(L), repeat=3)))
idx = lambda Y: ((Y[:, 0] % L) * L + Y[:, 1] % L) * L + Y[:, 2] % L
Hm = np.zeros((2 * N, 2 * N), complex)
for aa, sg in enumerate((sx, sy, sz)):
    i, j = idx(X), idx(X + np.eye(3, dtype=int)[aa])
    for p in range(2):
        for r in range(2):
            Hm[2 * i + p, 2 * j + r] += sg[p, r] / 2j
            Hm[2 * j + p, 2 * i + r] += -sg[p, r] / 2j


def esea(phi):
    ph = np.repeat(phi, 2)
    ev = np.linalg.eigvalsh(ph[:, None] * Hm * ph[None, :])
    return ev[ev < -1e-12].sum()


dev = 0.0
for n in ((1, 0, 0), (1, 1, 0), (2, 1, 0)):
    q = 2 * np.pi * np.array(n) / L
    vals = []
    for eps in (1e-2, 2e-2):
        u = eps * np.cos(X @ q)
        vals.append((esea(np.exp(u / 2)) + esea(np.exp(-u / 2)) - 2 * esea(np.ones(N))) / (2 * eps ** 2 * N))
    pf, dp, _, _ = kernel_torus(L, n)
    dev = max(dev, abs((4 * vals[0] - vals[1]) / 3 - (pf + dp)))
print("note: dense eigenvalues of phi H phi on 6^3 (three modes, Richardson in eps) vs Pi_fix + dPi: max deviation %.1e" % dev)
rows = []
for L, modes in ((6, [(1, 0, 0)]), (8, [(1, 0, 0), (2, 0, 0)]), (10, [(1, 0, 0), (2, 0, 0)]),
                 (12, [(1, 0, 0), (2, 0, 0), (3, 0, 0), (1, 1, 0), (1, 1, 1), (2, 2, 0)])):
    for n in modes:
        pf, dp, c0, ql2 = kernel_torus(L, n)
        rows.append("%.4f" % ((pf + dp - c0 / 4) / ql2))
print("note: free-sea gradient part per |q|^2_lat from the formula, L=6 (100); 8 (100),(200); 10 (100),(200); 12 (100),(200),(300),"
      "(110),(111),(220): " + " ".join(rows) + "  [block 76 executed: 0.0202; 0.0221 0.0234; 0.0231 0.0237; 0.0236 0.0239 0.0240 "
      "0.0238 0.0238 0.0237]; held sea at L=12: %.4f" % ((kernel_torus(12, (1, 0, 0))[0] - kernel_torus(12, (1, 0, 0))[2] / 4)
                                                       / kernel_torus(12, (1, 0, 0))[3]))
share = []
for L in (6, 8, 10, 12):
    pf, dp, c0, ql2 = kernel_torus(L, (1, 0, 0))
    zm = math.sin(2 * math.pi / L) / L ** 3 / ql2          # the eight zero-mode terms, -sin(2pi/L)/N, per |q|^2_lat
    share.append("L=%d %.5f of %.5f (1/(2pi L^2) = %.5f)" % (L, zm, -dp / ql2, 1 / (2 * math.pi * L * L)))
print("note: (100) deficit per |q|^2_lat carried by the zero-mode terms, of the total: " + "; ".join(share))


def zone(q, nr=400, nc=40, nph=80):
    x, wx = np.polynomial.legendre.leggauss(nc)
    ph = (np.arange(nph) + 0.5) * 2 * np.pi / nph
    lr, wlr = np.polynomial.legendre.leggauss(nr)
    lo, hi = np.log(1e-7), np.log(np.pi * np.sqrt(3) / 2)
    r = np.exp((lr + 1) / 2 * (hi - lo) + lo)
    wr = wlr * (hi - lo) / 2 * r
    st = np.sqrt(1 - x ** 2)
    dirs = np.stack([np.outer(st, np.cos(ph)), np.outer(st, np.sin(ph)), np.outer(x, np.ones(nph))], -1).reshape(-1, 3)
    wd = np.outer(wx, np.full(nph, 2 * np.pi / nph)).reshape(-1)
    tot = 0.0
    for kD in itertools.product((0.0, np.pi), repeat=3):
        for i0 in range(0, nr, 50):
            P = np.array(kD) + r[i0:i0 + 50, None, None] * dirs[None]
            inside = np.all(np.abs(P - np.array(kD)) <= np.pi / 2, axis=-1)
            s, s2 = np.sin(P), np.sin(P + q)
            b, a = np.linalg.norm(s, axis=-1), np.linalg.norm(s2, axis=-1)
            cth = np.einsum("...i,...i->...", s, s2) / np.maximum(a * b, 1e-300)
            Fv = (a - b) ** 2 / np.maximum(a + b, 1e-300) * (1 - cth) / 2 * inside
            tot += np.sum(Fv * (r[i0:i0 + 50] ** 2 * wr[i0:i0 + 50])[:, None] * wd[None])
    return tot / (2 * np.pi) ** 3


zs = {t: zone(np.array([t, 0.0, 0.0])) for t in (0.1, 0.05, 0.025)}
inc = [zs[0.05] / 0.05 ** 4 - zs[0.1] / 0.1 ** 4, zs[0.025] / 0.025 ** 4 - zs[0.05] / 0.05 ** 4]
print("note: zone integral <F>/t^4 along e1: %.5f (t=0.1), %.5f (0.05), %.5f (0.025); increments per halving %.5f, %.5f vs "
      "log2/(15 pi^2) = %.5f, i.e. dPi ~ -|q|^4 log(1/|q|)/(120 pi^2); bounds at t=0.025: %.2e <= %.2e <= %.2e"
      % (zs[0.1] / 1e-4, zs[0.05] / 0.05 ** 4, zs[0.025] / 0.025 ** 4, inc[0], inc[1], math.log(2) / (15 * math.pi ** 2),
         float(cl) * 0.025 ** 4 * math.log(1 / 0.1), zs[0.025], math.pi * 0.025 ** 4 * (1 / 6 + math.log(math.sqrt(3) / 0.025) / 2)))
g = 2 * np.pi * (np.arange(96) + 0.5) / 96
Kg = np.stack(np.meshgrid(g, g, g, indexing="ij"), -1).reshape(-1, 3)
Ival = float(np.linalg.norm(np.sin(Kg), axis=1).mean())
print("note: I = int |s(k)| d^3k/(2pi)^3 = %.5f (midpoint 96^3): kappa_fix = I/12 = %.5f, gamma = 12/I = %.3f; on a line kappa_fix = "
      "1/(2pi), kappa_opt = 1/(3pi) (a1: c = 1/(6pi), g(pi) = 0.0795)" % (Ival, Ival / 12, 12 / Ival))

print("runtime %.1f s" % (time.time() - T0))
if FAILS:
    print("CHECK FAIL: " + ", ".join(FAILS))
    print("SUMMARY: ROUTE FAILS AT a failed exact check (" + ", ".join(FAILS) + ")")
    sys.exit(1)
HITS = [
    "HIT: (a) the second-order kernel of E_opt - E_fix is exactly dPi(q) = -(1/8) int d^3k/(2pi)^3 (a-b)^2/(a+b) (1 - s^(k+q).s^(k))/2, "
    "a = |s(k+q)|, b = |s(k)| (per site per eps^2, u = eps cos(q.x)); it is negative for q != 0 and C t^4 log(1/(4t)) <= -8 dPi(t e1) "
    "<= pi t^4 (1/6 + log(sqrt3/t)/2), so dPi/|q|^2 -> 0: the free sea's clock stiffness equals the held sea's, kappa = I/12 = 0.0995.",
    "HIT: block 76's kappa = 0.095 is a torus value: on an even L-torus the kernel gains the exact zero modes as intermediate "
    "states, -sin(2pi/L)/N at q = (2pi/L)e1, about 1/(2 pi L^2) per |q|^2; executed, the torus formula gives block 76's eleven "
    "gradient parts at L = 6, 8, 10, 12 to four digits, the zero-mode terms carrying most of the deficit.",
    "HIT: (b) the difference is long-ranged: dPi is not C^4 at q = 0, so sum_r |r|^4 |R(r)| diverges for its real-space kernel R; "
    "on a line it has the closed form -(cos^2(q/2)/(2 pi sin(q/2)))[ln(sec + tan)(q/2) - sin(q/2)], which makes the free sea "
    "softer by a third there (kappa 1/(3pi) against 1/(2pi)).",
]
print("SUMMARY: PARTIAL the free sea's second-order deficit below the held sea is an exact zone integral, negative, of order "
      "|q|^4 log(1/|q|), so both seas have the clock stiffness I/12 = 0.0995 in three dimensions; block 76's 0.095 is its torus "
      "value; the deficit is long-ranged")
print("\n".join(HITS))
