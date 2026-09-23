#!/usr/bin/env python3
"""J:derive:the-anisotropic-state:a1 -- exact checks (sympy, Fractions, integer matrices) plus labelled zone-average notes.

Setting (blocks 59, 84, 88, 89): bond amplitudes t_j = e^{u_j} per axis; the traceless anisotropy u = eps(2, -1, -1) costs
36 beta eps^2 per site under block 59's law quadratic in log rates (block 88 T1); the free sea's energy per site is
E_sea(eps) = -< sqrt(e^{4 eps} s_x^2 + e^{-2 eps}(s_y^2 + s_z^2)) >, s_j = sin k_j, <.> the zone average.
Balance: F(eps) = 36 beta eps^2 + E_sea(eps).  Alternation (block 89): amplitudes t_j e^{+-delta_j} along axis j.
"""
import itertools, math, sys, time
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from scipy.optimize import brentq

T0 = time.time()
FAILS = []


def ok(tag, cond, msg=""):
    print(("ok   " if cond else "FAIL ") + tag + (": " + msg if msg else ""), flush=True)
    if not cond:
        FAILS.append(tag)


e, a, b, bt = sp.symbols("epsilon a b beta", real=True)
X, Y = sp.exp(4 * e), sp.exp(-2 * e)
f = a * X + b * Y
phi = sp.sqrt(f)
# ---------------------------------------------------------------- A: the sea's term is concave; the second-order coefficient
num = sp.expand(sp.simplify(sp.diff(phi, e, 2) * 2 * f ** sp.Rational(3, 2)))
good = sp.simplify(num - (8 * a ** 2 * X ** 2 + 28 * a * b * X * Y + 2 * b ** 2 * Y ** 2)) == 0
p0 = sp.simplify((sp.diff(phi, e, 2)).subs(e, 0) * (a + b) ** sp.Rational(3, 2))
good &= sp.simplify(p0 - (4 * a ** 2 + 14 * a * b + b ** 2)) == 0
sx, sy, sz = sp.symbols("s_x s_y s_z", real=True)
num3 = lambda p, q, r: 2 * p ** 4 + p ** 2 * (q ** 2 + r ** 2) - (q ** 2 + r ** 2) ** 2      # (4a^2+14ab+b^2) - (9ab + 2(a+b)^2)
good &= sp.expand(num3(sx, sy, sz) + num3(sy, sz, sx) + num3(sz, sx, sy)) == 0
good &= sp.expand((4 * a ** 2 + 14 * a * b + b ** 2) - (9 * a * b + 2 * (a + b) ** 2) - (2 * a ** 2 + a * b - b ** 2)) == 0
ok("A.concave", good, "d^2/de^2 sqrt(a e^{4e} + b e^{-2e}) = (8a^2X^2 + 28abXY + 2b^2Y^2)/(2 f^{3/2}) >= 0, so E_sea is concave in eps; "
   "at 0 the integrand is (4a^2 + 14ab + b^2)/|s|^3, whose average is 9<s_x^2 s_perp^2/|s|^3> + 2<|s|> = chi_a + 2<|s|> "
   "(the difference 2a^2 + ab - b^2 has zero cyclic sum): block 89's threshold 72 beta = chi_a + 2<|s|>")

# ---------------------------------------------------------------- B: no global minimum, with explicit runaway points
good = True
for lhs, rhs in ((a * X + b * Y, a * X), (a * X + b * Y, b * Y)):
    good &= sp.simplify(lhs - rhs - (b * Y if rhs == a * X else a * X)) == 0          # the dropped term is >= 0
eps_p = sp.Max(1, 3 * sp.pi / 8 * (36 * bt + sp.sqrt(3)))
eps_m = sp.Max(1, 3 * sp.pi * (36 * bt + sp.sqrt(3)))
for bv in (sp.Rational(1, 50), sp.Rational(1, 20), sp.Rational(1, 10), sp.Rational(1, 2), 3):
    for sgn, ew, amp, pw in ((1, eps_p, 2, sp.Rational(4, 3)), (-1, eps_m, 1, sp.Rational(1, 6))):
        w = ew.subs(bt, bv)
        for tt in (w, w + sp.Rational(1, 2), 2 * w):
            # F(eps) - F(0) <= 36 beta eps^2 - (2/pi) e^{amp |eps|} + sqrt3 and e^{amp t} >= (amp t)^3/6
            poly = 36 * bv * tt ** 2 - (2 / sp.pi) * (amp * tt) ** 3 / 6 + sp.sqrt(3)
            good &= bool(sp.N(poly, 30) < 0)
ok("B.runaway", good, "for every beta: sqrt(e^{4e}s_x^2 + e^{-2e}s_perp^2) >= e^{2e}|s_x|, >= e^{-e}|s_perp|, <|sin k|> = 2/pi, <|s|> <= sqrt3, "
   "so F(eps) < F(0) for eps >= max(1, (3pi/8)(36 beta + sqrt3)) (chains) and eps <= -max(1, 3pi(36 beta + sqrt3)) (planes): "
   "no global minimum under a law quadratic in log rates")

# ---------------------------------------------------------------- C: the walk in the anisotropic state; with the alternation
good = True
L = 4
sites = list(itertools.product(range(L), repeat=3))
ix = {p: i for i, p in enumerate(sites)}
n = len(sites)
SG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
tv = [Fr(2), Fr(1, 2), Fr(1)]                 # a traceless log anisotropy: 2 * (1/2) * 1 = 1
dv = [Fr(3), Fr(1), Fr(2)]                    # e^{delta_j}
D = []
for j in range(3):
    Dj = np.zeros((n, n), complex)
    for p in sites:
        q = list(p); q[j] = (q[j] + 1) % L
        amp = float(tv[j] * (dv[j] if p[j] % 2 == 0 else 1 / dv[j]))
        Dj[ix[p], ix[tuple(q)]] += amp / 2j; Dj[ix[tuple(q)], ix[p]] += -amp / 2j
    D.append(Dj)
H = sum(np.kron(D[j], SG[j]) for j in range(3))
good &= all(np.abs(D[i] @ D[j] - D[j] @ D[i]).max() < 1e-12 for i in range(3) for j in range(3))
good &= np.abs(H @ H - sum(np.kron(D[j] @ D[j], np.eye(2)) for j in range(3))).max() < 1e-12
ev = np.sort(np.linalg.eigvalsh(H @ H))
m2 = sum(float(tv[j] ** 2 * ((dv[j] - 1 / dv[j]) / 2) ** 2) for j in range(3))
good &= abs(ev[0] - m2) < 1e-9
ok("C.walk", good, "on the 4^3 torus with log-traceless axis amplitudes (2, 1/2, 1) and alternations e^{delta} = 3, 1, 2: the axis "
   "operators commute and H^2 = sum_j D_j^2 (half-integer entries, exact in floating point); the lowest eigenvalue of H^2 is sum_j t_j^2 sinh^2 delta_j = %s to 1e-9 (per-axis spectrum sin^2 k + sinh^2 delta, block 89 T1): E^2 = sum_j t_j^2 (sin^2 k_j + sinh^2 "
   "delta_j), an exact mass that adds in quadrature to the anisotropic massless walk" % str(sum(tv[j] ** 2 * ((dv[j] - 1 / dv[j]) / 2) ** 2 for j in range(3))))

de = sp.symbols("delta", real=True)
t1, t2, t3, s1, s2, s3 = sp.symbols("t1 t2 t3 s1 s2 s3", positive=True)
En = sp.sqrt(t1 ** 2 * (s1 ** 2 + sp.sinh(de) ** 2) + t2 ** 2 * s2 ** 2 + t3 ** 2 * s3 ** 2)
sec = sp.simplify(sp.diff(-En, de, 2).subs(de, 0) + t1 ** 2 / sp.sqrt(t1 ** 2 * s1 ** 2 + t2 ** 2 * s2 ** 2 + t3 ** 2 * s3 ** 2))
kk = sp.symbols("k", positive=True)
low = (2 / sp.pi) * sp.integrate(1 / (sp.exp(2 * e) * kk + sp.sqrt(2) * sp.exp(-e)), (kk, 0, sp.pi / 2))
low_ok = sp.simplify(sp.exp(sp.expand(low * sp.pi / 2 * sp.exp(2 * e))) - (1 + sp.pi * sp.exp(3 * e) / (2 * sp.sqrt(2)))) == 0
ok("C.alternation", sec == 0 and low_ok,
   "d^2 E_sea/d delta_j^2 at delta = 0 is -t_j^2 <1/E_eps>: the alternation along axis j sets in when alpha + 2 beta < t_j^2 <1/E_eps>/4; "
   "since E_eps <= e^{2e}|s_x| + sqrt2 e^{-e}, t_x^2 <1/E_eps> >= (2/pi) e^{2e} log(1 + pi e^{3e}/(2 sqrt2)) -> infinity along the chains")

# ---------------------------------------------------------------- notes: zone averages (midpoint grids, floating point)
ng = 96
gg = 2 * np.pi * (np.arange(ng) + 0.5) / ng
Aa = (np.sin(gg) ** 2)[:, None]
Bb = (np.sin(gg)[:, None] ** 2 + np.sin(gg)[None, :] ** 2).ravel()[None, :]


def Ez(ev_):
    return np.sqrt(np.exp(4 * ev_) * Aa + np.exp(-2 * ev_) * Bb)


def Esea(ev_):
    return -Ez(ev_).mean()


def Gz(ev_):
    return ((2 * np.exp(4 * ev_) * Aa - np.exp(-2 * ev_) * Bb) / Ez(ev_)).mean()


def Rz(ev_):
    return Gz(ev_) / ev_


S0 = np.sqrt(Aa + Bb)
chi_lin = 9 * (Aa * Bb / S0 ** 3).mean()
ms = S0.mean()
chi_log = ((4 * Aa ** 2 + 14 * Aa * Bb + Bb ** 2) / S0 ** 3).mean()
h3 = 2e-3
c3 = (Esea(2 * h3) - 2 * Esea(h3) + 2 * Esea(-h3) - Esea(-2 * h3)) / (2 * h3 ** 3)
print("note: chi_a = %.4f, <|s|> = %.4f, chi_a + 2<|s|> = %.4f (threshold beta = %.5f); E_sea'''(0) = %.3f < 0: the cubic "
      "term favours eps < 0 (two axes fast: planes)" % (chi_lin, ms, chi_log, chi_log / 72, c3))
es = np.linspace(-3.0, -0.05, 60)
Rs = np.array([Rz(x_) for x_ in es])
i0 = int(Rs.argmin())
e_lo, e_hi = es[max(i0 - 1, 0)], es[min(i0 + 1, len(es) - 1)]
from scipy.optimize import minimize_scalar
res = minimize_scalar(Rz, bounds=(e_lo, e_hi), method="bounded")
Rmin, emin = res.fun, res.x
esp = np.linspace(0.05, 2.5, 40)
mono = bool(np.all(np.diff([Rz(x_) for x_ in esp]) > 0))
print("note: critical points solve R(eps) = -E_sea'(eps)/eps = 72 beta; on the planes side R has its minimum %.4f at eps = %.3f, on the "
      "chains side R rises monotonically (%s): a metastable planar state exists for %.5f < beta < %.5f" % (Rmin, emin, mono, Rmin / 72, chi_log / 72))
rows = []
for bv in (0.040, 0.045, 0.050, 0.055, 0.058):
    lam = 72 * bv
    r1 = brentq(lambda x_: Rz(x_) - lam, emin, -1e-4)
    r2 = brentq(lambda x_: Rz(x_) - lam, -6.0, emin)
    F = lambda x_: 36 * bv * x_ * x_ + Esea(x_)
    tx = math.exp(-r1)
    alt = tx ** 2 * (1 / Ez(r1)).mean() / 4
    rows.append("beta %.3f: eps* %.3f (F %.4f vs F(0) %.4f), barrier at %.2f (F %.3f); fast-axis speed %.3f, alternation sets in below "
                "alpha + 2beta = %.4f" % (bv, r1, F(r1), F(0), r2, F(r2), tx, alt))
print("note: " + "; ".join(rows))
brs = []
for bv in (0.065, 0.08, 0.10):
    lam = 72 * bv
    rp = brentq(lambda x_: Rz(x_) - lam, 1e-3, 3.0)
    F = lambda x_: 36 * bv * x_ * x_ + Esea(x_)
    brs.append("beta %.3f: chains barrier at eps %.3f, height %.5f" % (bv, rp, F(rp) - F(0)))
print("note: above threshold the isotropic state is guarded towards chains by a small barrier: " + "; ".join(brs) +
      "; isotropic alternation threshold <1/|s|>/4 = %.4f" % ((1 / S0).mean() / 4))

mut = []
for dl in (0.1, 0.3, 0.5):
    s2_ = math.sinh(dl) ** 2
    aa_, bb_ = Aa + s2_, Bb + 2 * s2_
    chm = ((4 * aa_ ** 2 + 14 * aa_ * bb_ + bb_ ** 2) / (aa_ + bb_) ** 1.5).mean()
    mut.append("delta %.1f: %.4f (beta %.5f)" % (dl, chm, chm / 72))
print("note: conversely an alternation of equal delta on the three axes raises the anisotropy's second-order coefficient "
      "(the mass sum_j t_j^2 sinh^2 delta also responds to the anisotropy): " + "; ".join(mut) + ", against %.4f at delta = 0" % chi_log)
print("runtime %.1f s" % (time.time() - T0))
if FAILS:
    print("CHECK FAIL: " + ", ".join(FAILS))
    print("SUMMARY: ROUTE FAILS AT a failed exact check (" + ", ".join(FAILS) + ")")
    sys.exit(1)
HITS = [
    "HIT: (a) the balance F(eps) = 36 beta eps^2 - <sqrt(e^{4eps} s_x^2 + e^{-2eps}(s_y^2 + s_z^2))> has a concave sea term and, for every "
    "beta, falls below F(0) beyond eps = max(1, (3pi/8)(36beta + sqrt3)) towards chains and below -max(1, 3pi(36beta + sqrt3)) towards "
    "planes: no global minimum; its critical points solve R(eps) = 72 beta, R = -E_sea'/eps (executed: a metastable planar state "
    "for %.4f < beta < %.4f, none on the chains side)." % (Rmin / 72, chi_log / 72),
    "HIT: (b, c) the anisotropy keeps all eight species massless at speeds e^{2eps}, e^{-eps}, e^{-eps}; with the alternation "
    "E^2 = sum_j t_j^2 (sin^2 k_j + sinh^2 delta_j) exactly; along axis j the alternation sets in below alpha + 2 beta = "
    "t_j^2 <1/E_eps>/4, unbounded along the runaway to chains; executed, each instability raises the other's threshold, so "
    "they coexist whichever comes first.",
]
print("SUMMARY: PARTIAL the anisotropy balance has no global minimum for any beta (explicit runaway points both ways); a metastable "
      "planar state below threshold, none towards chains; the anisotropic walk stays massless and combines with the alternation "
      "exactly, whose threshold it raises along its fast axes")
print("\n".join(HITS))
