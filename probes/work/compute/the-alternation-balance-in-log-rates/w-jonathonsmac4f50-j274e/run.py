#!/usr/bin/env python3
"""Block 84's balance redone in log rates (block 89, landed #8678), run 1 of 2.

As landed: T2 gives the local coefficient 6 kappa - 3I/2 (I = <1/sqrt S>, S = sum sin^2 k_j), threshold kappa = I/4; T3 the anisotropy zero
beta = (chi_a + 2J)/72 (J = <sqrt S>, chi_a the linear-rate model's coefficient); T4: the supplied objective is unbounded below (witness
delta_w = 6 + 12 sqrt(3) kappa).  Here: the whole profile of
    three axes  F3(delta) = -<sqrt(S + 3 sinh^2 delta)> + 6 kappa delta^2,
    one axis    F1(delta) = -<sqrt(S + sinh^2 delta)>   + 2 kappa delta^2,
    anisotropy  G(eps)    = -<sqrt(e^{4 eps} s_x^2 + e^{-2 eps}(s_y^2 + s_z^2))> + 36 beta eps^2.
Zone averages by an EXACT one-dimensional representation (sqrt(x) = (1/(2 sqrt pi)) int (1 - e^{-tx}) t^{-3/2} dt and <e^{-t sin^2 k}> =
e^{-t/2} I_0(t/2)), evaluated by adaptive quadrature (double precision), and on midpoint grids L^3, L = 32 .. 256 (numpy), as the task asks.
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import i0e, i1e
import mpmath as mp

def out(s): print(s, flush=True)
SQPI = np.sqrt(np.pi)
g = lambda u: i0e(0.5 * u)                         # <exp(-u sin^2 k)>
def qint(f, scale=1.0):
    """int_0^inf f; break points at the unit scale and at the scale 1/m of a factor exp(-x^2 m^2) (scale = 1/m < 1 for large m)"""
    pts = sorted({0.0, *(c for c in (0.5, 2, 8, 40, 400)), *(c * scale for c in (0.05, 0.25, 1, 4, 16, 64) if scale < 1)})
    tot = 0.0
    for a, b in zip(pts, pts[1:] + [np.inf]):
        v, _ = quad(f, a, b, limit=400, epsabs=1e-15, epsrel=1e-13); tot += v
    return tot

# ------------------------------------------------------------------ zone constants
I = 2 / SQPI * qint(lambda x: g(x * x) ** 3)
J = 1 / SQPI * qint(lambda x: (1 - g(x * x) ** 3) / (x * x) if x > 1e-8 else 1.5)
mp.mp.dps = 30
gm = lambda u: mp.exp(-u / 2) * mp.besseli(0, u / 2)
Imp = 2 / mp.sqrt(mp.pi) * mp.quad(lambda x: gm(x * x) ** 3, [0, 1, 4, 16, 64, mp.inf])
Jmp = 1 / mp.sqrt(mp.pi) * mp.quad(lambda x: (1 - gm(x * x) ** 3) / (x * x), [0, 1, 4, 16, 64, mp.inf])
out("X zone constants by the exact one-dimensional representation: I = <1/sqrt S> = %s, J = <sqrt S> = %s (30 digits); double-precision quadrature "
    "agrees to %.1e, %.1e" % (mp.nstr(Imp, 20), mp.nstr(Jmp, 20), abs(I - float(Imp)), abs(J - float(Jmp))))
kc = I / 4
out("X local threshold (landed T2, both the three-axis and the one-axis law): kappa_c = I/4 = %.12f" % kc)

# ------------------------------------------------------------------ midpoint grids
def grid_u(L):
    k = -np.pi + 2 * np.pi * (np.arange(L) + 0.5) / L
    return np.sin(k) ** 2
GRIDS = (32, 64, 128, 256)
Sgrid = {}
for L in GRIDS:
    u = grid_u(L)
    Sgrid[L] = (u[:, None, None] + u[None, :, None] + u[None, None, :]).astype(np.float64)
rows = []
for L in GRIDS:
    S = Sgrid[L]; IL = (1 / np.sqrt(S)).mean(); JL = np.sqrt(S).mean()
    rows.append((L, IL, JL))
out("N midpoint grids: " + "; ".join("L = %d: I %.8f (%+.1e), J %.10f (%+.1e), kappa_c %.8f" % (L, a, a - I, b, b - J, a / 4) for L, a, b in rows))
r = [(rows[i][1] - I) / (rows[i + 1][1] - I) for i in range(3)]
out("N the grids' error in I falls by %s per doubling (second order: 4)" % ", ".join("%.2f" % x for x in r))

# ------------------------------------------------------------------ the sea's gain and its derivative, exact representation
def W(m2):            # <sqrt(S + m2)>
    return 1 / SQPI * qint(lambda x: (1 - np.exp(-x * x * m2) * g(x * x) ** 3) / (x * x) if x > 1e-8 else m2 + 1.5, 1 / np.sqrt(1 + m2))
def Wp(m2):           # d<sqrt(S + m2)>/d m2 = <1/(2 sqrt(S + m2))>
    return 1 / SQPI * qint(lambda x: np.exp(-x * x * m2) * g(x * x) ** 3, 1 / np.sqrt(1 + m2))
# check at large gaps against the direct 48^3 midpoint average (a periodic analytic integrand when m2 > 0)
_u = np.sin(-np.pi + 2 * np.pi * (np.arange(48) + 0.5) / 48) ** 2; _S48 = _u[:, None, None] + _u[None, :, None] + _u[None, None, :]
_chk = max(abs(W(m2) - np.sqrt(_S48 + m2).mean()) / np.sqrt(1 + m2) for m2 in (1.0, 10.0, 1e3, 1e6, 1e10))
_chkp = max(abs(Wp(m2) - (0.5 / np.sqrt(_S48 + m2)).mean()) * np.sqrt(1 + m2) for m2 in (1.0, 10.0, 1e3, 1e6, 1e10))
out("N the one-dimensional representation at gaps m^2 = 1 .. 1e10 against the 48^3 midpoint average: relative differences below %.1e (value), %.1e (derivative)"
    % (_chk, _chkp))
def Wexcess(m2):      # <sqrt(S+m2)> - J - m2 I/2, without cancellation
    def f(x):
        y = x * x * m2
        return g(x * x) ** 3 * (-(np.expm1(-y) + y)) / (x * x) if x > 1e-8 else -0.5 * 0 
    return 1 / SQPI * qint(f)
# non-analytic quartic: W - J - m2 I/2 = -(m^4/(2 pi^2)) log(1/m) + O(m^4) (eight Weyl points, continuum); check the slope in log m
ms = [0.02, 0.04, 0.08, 0.16]
vals = [Wexcess(m * m) / m ** 4 for m in ms]
slopes = [(vals[i + 1] - vals[i]) / np.log(ms[i + 1] / ms[i]) for i in range(3)]
out("X beyond second order the sea's gain is not analytic: (<sqrt(S+m^2)> - J - m^2 I/2)/m^4 at m = %s: %s; slope in log m %s against "
    "1/(2 pi^2) = %.5f (eight nodes, each a cone): F3 - F3(0) = (6 kappa - 3I/2) delta^2 + (9/(2 pi^2)) delta^4 log(1/delta) + O(delta^4), "
    "a POSITIVE quartic-log term" % (ms, ", ".join("%.5f" % v for v in vals), ", ".join("%.5f" % s for s in slopes), 1 / (2 * np.pi ** 2)))

def profile(kind, kap):
    if kind == 3:
        m2 = lambda d: 3 * np.sinh(d) ** 2; dm2 = lambda d: 3 * np.sinh(2 * d); cc = 6.0
    else:
        m2 = lambda d: np.sinh(d) ** 2; dm2 = lambda d: np.sinh(2 * d); cc = 2.0
    F = lambda d: -W(m2(d)) + cc * kap * d * d
    Fp = lambda d: -dm2(d) * Wp(m2(d)) + 2 * cc * kap * d
    return F, Fp

def scan(F, dF, side, xmax, F0):
    """critical points of F on (0, side*xmax] (classified), and the outermost crossing of F(0) from above (None if F < F(0) all along)"""
    xs = side * np.concatenate([np.linspace(0.002, 0.3, 90), np.linspace(0.3, xmax, 500)[1:]])
    fp = np.array([dF(x) for x in xs])
    crit = []
    for i in range(len(xs) - 1):
        if fp[i] * fp[i + 1] < 0:
            x = brentq(dF, xs[i], xs[i + 1], xtol=1e-12)
            crit.append((x, F(x) - F0, "max" if fp[i] * side > 0 else "min"))
    fv = np.array([F(x) - F0 for x in xs])
    cross = None
    pos = np.where(fv > 0)[0]
    if len(pos):
        i = pos[-1]
        if i + 1 < len(xs):
            cross = brentq(lambda x: F(x) - F0, xs[i], xs[i + 1], xtol=1e-12)
    return crit, cross, fv[-1] < 0

def landscape(kind, kap):
    F, Fp = profile(kind, kap)
    dw = 6 + 12 * np.sqrt(3) * kap if kind == 3 else 6 + 36 * kap          # T4's witness (three axes); a bracket of the same kind for one axis
    crit, cross, below = scan(F, Fp, +1, dw, -J)
    return {"crit": crit, "cross": cross, "witness": dw, "below_at_end": below}

REL = (0.8, 0.9, 0.95, 0.99, 0.999, 1.0, 1.001, 1.01, 1.05, 1.1, 1.25, 1.5, 2.0, 3.0, 5.0, 10.0)
ALT, ANI = {}, {}
for kind, lab in ((3, "three axes, 6 kappa delta^2"), (1, "one axis, 2 kappa delta^2")):
    for rr in REL:
        kap = rr * kc
        res = landscape(kind, kap); ALT[(kind, rr)] = res
        crit = "; ".join("%s at delta = %.6f, F - F(0) = %+.8f" % (t, d, h) for d, h, t in res["crit"])
        cross = ("; runaway branch crosses F(0) at delta = %.6f (T4 witness %.3f)" % (res["cross"], res["witness"])) if res["cross"] is not None else "; F < F(0) for every delta > 0 on the scan"
        out("N %s: kappa = %.3f kappa_c = %.6f: %s%s" % (lab, rr, kap, crit if crit else "no critical point for delta > 0", cross))

# ------------------------------------------------------------------ anisotropy
def V(eps):
    a, b = np.exp(4 * eps), np.exp(-2 * eps)
    return 1 / SQPI * qint(lambda x: (1 - g(a * x * x) * g(b * x * x) ** 2) / (x * x) if x > 1e-8 else 0.5 * a + b, 1 / np.sqrt(max(a, b, 1.0)))
def d2(fun, h):
    return (fun(h) - 2 * fun(0.0) + fun(-h)) / h ** 2
gp = lambda u: 0.5 * (i1e(0.5 * u) - i0e(0.5 * u))          # d/du <exp(-u sin^2 k)>
def Vp(eps):          # d<sqrt A>/d eps, differentiated under the integral (no finite differences)
    a, b = np.exp(4 * eps), np.exp(-2 * eps)
    return 1 / SQPI * qint(lambda x: -(4 * a * gp(a * x * x) * g(b * x * x) ** 2 - 4 * b * g(a * x * x) * g(b * x * x) * gp(b * x * x)),
                           1 / np.sqrt(max(a, b, 1.0)))
def rich1(fun, h):      # derivative at 0 of fun by Richardson-extrapolated central differences
    c = lambda hh: (fun(hh) - fun(-hh)) / (2 * hh)
    return (4 * c(h / 2) - c(h)) / 3
V2 = rich1(Vp, 0.01)
bc = V2 / 72
# linear-rate model (1 + 2 eps, 1 - eps, 1 - eps): chi_a = its second derivative of <sqrt A>
def Vlin(eps):
    a, b = (1 + 2 * eps) ** 2, (1 - eps) ** 2
    return 1 / SQPI * qint(lambda x: (1 - g(a * x * x) * g(b * x * x) ** 2) / (x * x) if x > 1e-8 else 0.5 * a + b)
def Vlinp(eps):        # d<sqrt A_lin>/d eps under the integral, A_lin = (1 + 2 eps)^2 s_x^2 + (1 - eps)^2 (s_y^2 + s_z^2)
    a, b = (1 + 2 * eps) ** 2, (1 - eps) ** 2
    da, db = 4 * (1 + 2 * eps), -2 * (1 - eps)
    return 1 / SQPI * qint(lambda x: -(da * gp(a * x * x) * g(b * x * x) ** 2 + 2 * db * g(a * x * x) * g(b * x * x) * gp(b * x * x)))
chi_a = rich1(Vlinp, 0.01)
out("X anisotropy: d^2<sqrt A>/d eps^2 at 0 = %.10f; threshold beta_c = that/72 = %.10f; landed T3's (chi_a + 2J)/72 with chi_a = %.10f (the "
    "linear-rate model's second derivative) = %.10f (difference %.1e)" % (V2, bc, chi_a, (chi_a + 2 * J) / 72, bc - (chi_a + 2 * J) / 72))
for L in GRIDS:
    u = grid_u(L); vv = (u[:, None] + u[None, :])
    def VL(eps, u=u, vv=vv):
        return np.sqrt(np.exp(4 * eps) * u[:, None, None] + np.exp(-2 * eps) * vv[None, :, :]).mean()
    V2L = (4 * d2(VL, 0.01) - d2(VL, 0.02)) / 3
    out("N anisotropy on the midpoint grid L = %d: beta_c = %.10f (%+.1e)" % (L, V2L / 72, V2L / 72 - bc))
V3 = (V(0.02) - 2 * V(0.01) + 2 * V(-0.01) - V(-0.02)) / (2 * 0.01 ** 3)
out("X anisotropy: third derivative of <sqrt A> at 0 = %.6f: the landscape is not even in eps, so the barrier is lower on the side eps %s 0"
    % (V3, ">" if V3 > 0 else "<"))

_fd = (V(1e-3) - V(-1e-3)) / 2e-3
out("N anisotropy: the analytic derivative against a central difference at eps = 0 (%.2e, zero by symmetry) and at eps = 0.3: %.10f vs %.10f"
    % (Vp(0.0), Vp(0.3), (V(0.3 + 1e-4) - V(0.3 - 1e-4)) / 2e-4))
def aniso_landscape(bet):
    Gf = lambda e: -V(e) + 36 * bet * e * e
    dG = lambda e: -Vp(e) + 72 * bet * e
    return {side: scan(Gf, dG, side, 8.0, -J) for side in (+1, -1)}

for rr in REL:
    bet = rr * bc
    res = aniso_landscape(bet); ANI[rr] = res
    parts = []
    for side in (+1, -1):
        cr, cross, below = res[side]
        s1 = ", ".join("%s at eps = %+.6f, G - G(0) = %+.8f" % (t, e, v) for e, v, t in cr) if cr else "no critical point"
        parts.append("eps %s 0: %s%s" % (">" if side > 0 else "<", s1, "; runaway crosses G(0) at eps = %+.6f" % cross if cross is not None else "; G < G(0) all along"))
    out("N anisotropy, 36 beta eps^2: beta = %.3f beta_c = %.6f: %s" % (rr, bet, " | ".join(parts)))

# ------------------------------------------------------------------ grid cross-check of one barrier (three axes, 2 kappa_c; anisotropy 2 beta_c)
kap = 2 * kc
res = landscape(3, kap)
db = [c for c in res["crit"] if c[2] == "max"][-1]
S = Sgrid[256]
FL = lambda d: -np.sqrt(S + 3 * np.sinh(d) ** 2).mean() + 6 * kap * d * d
F0L = -np.sqrt(S).mean()
hL = 1e-5
dbL = brentq(lambda d: (FL(d + hL) - FL(d - hL)) / (2 * hL), db[0] * 0.8, db[0] * 1.2, xtol=1e-9)
xL = brentq(lambda d: FL(d) - F0L, dbL, res["cross"] * 1.2, xtol=1e-9)
out("N three axes, kappa = 2 kappa_c, midpoint grid 256^3 against the exact representation: barrier at %.6f (exact %.6f), height %+.8f (exact %+.8f), "
    "crossing at %.6f (exact %.6f)" % (dbL, db[0], FL(dbL) - F0L, db[1], xL, res["cross"]))

out("")
def first(res, t):
    c = [x for x in res["crit"] if x[2] == t]
    return c
def bar(kind, rr):
    c = first(ALT[(kind, rr)], "max")
    return ("%.3f (height %.2g)" % (c[-1][0], c[-1][1])) if c else "none"
def mins(kind, rr):
    c = [x for x in first(ALT[(kind, rr)], "min") if x[0] < 1.0]
    return ("%.3f" % c[0][0]) if c else "none"
def abar(rr, side):
    c = [x for x in ANI[rr][side][0] if x[2] == "max"]
    return ("%+.3f (height %.2g)" % (c[-1][0], c[-1][1])) if c else "none"
SUMMARY = ("log-rate balance: kappa_c = I/4 = %.8f for the three-axis (6 kappa delta^2) and the one-axis (2 kappa delta^2) law and beta_c = %.8f "
           "= (chi_a + 2J)/72 for the anisotropy, as landed (midpoint 256^3: %.8f, %.8f); beyond second order the sea adds +(m^4/(2 pi^2)) log(1/m) "
           "(eight conical nodes, m^2 the added gap), so for the alternation the threshold is not where the barrier vanishes: three axes, the small-delta minimum below "
           "kappa_c at 0.9/0.99/0.999 kappa_c is at delta = %s/%s/%s and the barrier at kappa_c is at delta = %s, at 2 and 10 kappa_c %s and %s; "
           "one axis, barrier at 1.001/1.01/2/10 kappa_c at %s/%s/%s/%s; the anisotropy is analytic with a cubic term (the side eps > 0 lower), "
           "its eps > 0 barrier shrinks to zero at beta_c: barrier (eps > 0 | eps < 0) at 1.01 beta_c %s | %s, at 2 beta_c %s | %s; the runaway branch crosses the uniform value at finite distance in every case (T4's unbounded objective): three axes at "
           "kappa_c, 2 kappa_c, 10 kappa_c at delta = %.3f, %.3f, %.3f"
           % (kc, bc, rows[-1][1] / 4, V2L / 72, mins(3, 0.9), mins(3, 0.99), mins(3, 0.999), bar(3, 1.0), bar(3, 2.0), bar(3, 10.0),
              bar(1, 1.001), bar(1, 1.01), bar(1, 2.0), bar(1, 10.0), abar(1.01, +1), abar(1.01, -1), abar(2.0, +1), abar(2.0, -1),
              ALT[(3, 1.0)]["cross"], ALT[(3, 2.0)]["cross"], ALT[(3, 10.0)]["cross"]))
out("SUMMARY: " + SUMMARY)
