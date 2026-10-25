#!/usr/bin/env python3
"""check.py for J:derive:review-20261016-composite-clock-strain:a1

Scope: the composite / clock coefficient-transfer bridge of C5 E1 and C5 F6
(strain-hot-matter-twins-20261013 @ 6afb069...).  numpy, scipy, sympy, mpmath
and the standard library only.  Inputs quoted from the F6/E1 reports are
ASSUMED inputs (named below); every derived number is recomputed here.

One line per check starting PASS or FAIL.  INFO lines carry numbers.
"""
import hashlib
import os
import sys
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
n_pass = 0
n_fail = 0


def chk(ok, msg):
    global n_pass, n_fail
    if ok:
        n_pass += 1
        print("PASS " + msg)
    else:
        n_fail += 1
        print("FAIL " + msg)


def info(msg):
    print("INFO " + msg)


def close(a, b, rel):
    a, b = float(a), float(b)
    return abs(a - b) <= rel * max(abs(a), abs(b))


# ---------------------------------------------------------------------------
# 0. Source hashes (frozen commit 6afb0695..., copies in ./src)
# ---------------------------------------------------------------------------
SRC = {
    "C5_E1_referee_verdict.md": "932ace7b637106cb89d67babf6fc1cc15b2aed89bed5875eddf7505c01b9deaa",
    "C5_E1_report.md": "5349a78832efa473d419237e96ffcfce9bc3676e37e16ecef4997da2ac24a845",
    "C5_F6_referee_verdict.md": "fdc753260d52e78ffa0ac8a20b8bc139ec9a3a095527f7e6146d350126fc4f33",
    "C5_F6_report.md": "94ae8da373b52a0f1e3baee70f5c21d3f0523da1279e07df4ffde894c0fe4647",
    "panel_F/DOSSIER.md": "d3ea58e84b66231a4e52ab6ac30c5922ff34005b69b16b929ac72a5d9628dcdf",
    "panel_F/SYNTHESIS.md": "4b8318b1faf7439c2998a86d071fd0df464bc5d228743fcb7b66bd173d0f5b01",
    "panel_F/condmat_statement.md": "6c7b993c6739d79868b486b155af666932a667ceea15839e2c6471e1d55cb3f7",
    "panel_F/gr_statement.md": "0dd567186d84efdc0235857179f3fc9020cc2453ff362c0bc80b410abeff291f",
    "panel_F/lattice_statement.md": "25c3c68970da46fd2dc311403e82607c43e405122872f475a434176ec5f2fb29",
    "panel_F/pheno_statement.md": "18577dbb707a34e30413877f4e5e31673a368044e9734cb5f9f71019580dde7e",
    "panel_F/skeptic_statement.md": "22f248ea7785b95ac281d63a2b45bc72396c77cb0d06b862549492ffd495bcca",
}
for rel, want in SRC.items():
    p = os.path.join(HERE, "src", rel)
    try:
        got = hashlib.sha256(open(p, "rb").read()).hexdigest()
    except OSError:
        got = "missing"
    chk(got == want, "S0 sha256 of source object %s" % rel)

# ---------------------------------------------------------------------------
# 1. Quoted inputs (ASSUMED, from C5_F6_report.md and the referee verdicts)
# ---------------------------------------------------------------------------
# Hessian pieces (F6 report 3.2-3.5) and Planck-scale coupling set
H_g, H_Y, H_lam = Fr("2.43452e-3"), Fr("6.62484e-3"), Fr("-2.67482e-3")
g2, gp2, yt, lam, Nc = Fr("0.26"), Fr("0.21"), Fr("0.38"), Fr("-0.013"), 3
cH = (Fr(3, 4) * g2 + Fr(1, 4) * gp2) * H_g + Nc * yt**2 * H_Y + 6 * lam * H_lam
chk(close(cH, 3.681e-3, 2e-3), "S1 c_H assembled from the three loop Hessians = 3.681e-3 (got %.5e)" % float(cH))

MP, mH = 1.22089e19, 125.1            # GeV, scale_reference_primitive a^-1 = M_Pl; m_H
kH = float(cH) * MP**2 / (2 * mH**2)  # |d ln v / dQ_E| , elementary Higgs, linear response
chk(close(kH, 1.753e31, 3e-3), "S1 kappa_H = c_H M_P^2/(2 m_H^2) = 1.75e31 (got %.4e)" % kH)

# <Q_E> from the NANOGrav-like spectrum: h_c = A (f/yr^-1)^(-2/3), <h_ij h_ij> = 2 Int h_c^2 dln f,
# 1/5 of the power per traceless component, Q_E = (c1^2+c2^2)/2 with c_i orthonormal components.
Aamp, fmin = 2.4e-15, 1.0 / 16.0
int_hc2 = Aamp**2 * 0.75 * fmin ** (-4.0 / 3.0)       # f_max -> infinity
sig2 = 2 * int_hc2 / 5.0
chk(close(sig2, 7.0e-29, 0.01), "S1 <Q_E> = sigma^2 reconstructed from spectrum = 7.0e-29 (got %.4e)" % sig2)

slope_min = 7.670e-30      # /yr, referee's conservative rms slope of Q_E (T_obs 10 yr, f_min 1/16)
slope_max = 1.02e-28       # /yr, pheno 2 t tdot estimator, f_min 1/30
dlnv_lnmp_me = 0.70        # |d ln(m_p/m_e)/d ln v|, ESTIMATE (F6)
bound = 3.6e-17            # /yr clock bound on |d ln(m_p/m_e)/dt| (pre-registered, F6)
kclock_hi = bound / (dlnv_lnmp_me * slope_min)   # largest allowed kappa
kclock_lo = bound / (dlnv_lnmp_me * slope_max)
E_formal = kH / kclock_hi
chk(close(E_formal, 2.614e18, 3e-3), "S1 formal exceedance kH/kclock = 2.614e18 as in F6 referee (got %.4e)" % E_formal)
info("kappa_clock band: %.3e (conservative) .. %.3e (largest slope)" % (kclock_hi, kclock_lo))

# ---------------------------------------------------------------------------
# 2. The three composite margins are one chain A*s with different borrowed s
# ---------------------------------------------------------------------------
Lam = 1.0e4                                   # GeV, the E1 benchmark (10 TeV)
A_amp = Lam**2 / mH**2                        # amplification Lambda^2/m_H^2
s_ans = float(cH) / 2.0                       # dimensionless strain coefficient used by the ansatz
kappa_ans = s_ans * A_amp
M_ans = kclock_hi / kappa_ans
chk(close(M_ans, 5.6e11, 0.02), "S2 transfer-ansatz margin = 5.6e11 (got %.3e)" % M_ans)

cN = 0.25 * np.log(32.0) - 0.5                # closed-form constant of the O(N) toy, section 5 below
s_toy = 0.5 * np.log(MP / Lam) + cN           # d ln Lambda / dQ in the toy, linear law
M_toy_bare = kclock_hi / s_toy                # delta ln v = delta ln Lambda (no amplification)
M_toy_amp = kclock_hi / (s_toy * A_amp)       # amplified by Lambda^2/m_H^2
chk(close(M_toy_amp, 5.9e7, 0.02), "S2 log-response x Lambda^2/m_H^2 margin = 5.9e7 (got %.3e)" % M_toy_amp)
chk(close(M_toy_bare, 3.8e11, 0.03), "S2 bare multiplicative toy margin = 3.8e11 (got %.3e)" % M_toy_bare)
ratio = M_ans / M_toy_amp
chk(close(ratio, 2 * s_toy / float(cH), 1e-9), "S2 M_ans/M_toy_amp = 2 s_toy/c_H = %.3e (borrowed coefficients, same A)" % ratio)

# the ansatz is F6's own (l_P/a)^2 scaling with 1/a -> Lambda:  M_ans * E_formal = (M_P/Lambda)^2
cHs, MPs, Ls, ms, kc = sp.symbols("c_H M_P Lambda m_H kappa_c", positive=True)
Msym = kc / (cHs * Ls**2 / (2 * ms**2))
Esym = (cHs * MPs**2 / (2 * ms**2)) / kc
chk(sp.simplify(Msym * Esym - (MPs / Ls) ** 2) == 0, "S2 symbolic identity M_ans * E_formal = (M_P/Lambda)^2")
chk(close(M_ans * E_formal, (MP / Lam) ** 2, 1e-9), "S2 numeric identity M_ans * E_formal = (M_P/Lambda)^2 = %.3e" % (MP / Lam) ** 2)

# exponent form: R(Lambda) = kH (Lambda/M_P)^p ; clock needs p >= p_min
pmin = np.log(E_formal) / np.log(MP / Lam)
chk(abs(pmin - 1.2218) < 5e-3, "S2 p_min(10 TeV) = ln(E)/ln(M_P/Lambda) = %.4f; ansatz is p=2" % pmin)
chk(close((MP / Lam) ** 2 / E_formal, M_ans, 1e-9), "S2 p=2 reproduces the ansatz margin exactly")
# upper bound on the strain coefficient s of a Lambda-sized mass^2 (A=Lambda^2/m_H^2)
s_max = kclock_hi / A_amp
info("clock needs s*A <= %.3e, i.e. s <= %.3e at Lambda=10 TeV; ansatz s=%.2e, toy s=%.1f, elementary-like s=c_H/2 (M_P/Lambda)^2=%.2e"
     % (kclock_hi, s_max, s_ans, s_toy, s_ans * (MP / Lam) ** 2))
chk(s_ans < s_max and s_toy < s_max and s_ans * (MP / Lam) ** 2 > s_max,
    "S2 both borrowed s values pass, an unsuppressed (M_P/Lambda)^2 coefficient fails: bound s<=%.2e is the open number" % s_max)

# ---------------------------------------------------------------------------
# 3. Nonlinear vev readout (tree-level potential, exact)
# ---------------------------------------------------------------------------
v, mu2, lamq, d = sp.symbols("v mu2 lambda d", positive=True)
V = -mu2 * v**2 / 2 + lamq * v**4 / 4 + d * v**2 / 2   # (1/2)(-mu^2+d) v^2 + (lambda/4) v^4  [H^dag H = v^2/2]
sol = sp.solve(sp.diff(V, v), v)
v2 = sp.simplify((mu2 - d) / lamq)
chk(any(sp.simplify(s_ - sp.sqrt(v2)) == 0 for s_ in sol) and sp.simplify(sp.diff(V, v, 2).subs(v, sp.sqrt(v2)) - 2 * (mu2 - d)) == 0,
    "S3 broken stationary point v^2 = (mu^2-d)/lambda, curvature 2(mu^2-d) > 0 iff d < mu^2")
# m_H^2 = 2 mu^2 at d=0, x = d/m_H^2  =>  v^2/v0^2 = 1 - 2x
x_ = sp.symbols("x")
chk(sp.simplify(((mu2 - x_ * 2 * mu2) / lamq) / (mu2 / lamq) - (1 - 2 * x_)) == 0, "S3 v^2/v0^2 = 1 - 2x with x = d/m_H^2")
Qc = 1.0 / (2 * kH)
info("Q_c = 1/(2 kappa_H) = %.4e  (EW vacuum exists iff Q_E < Q_c)" % Qc)
chk(abs(Qc - 2.852e-32) / 2.852e-32 < 5e-3, "S3 Q_c = 2.85e-32")
chk(sig2 / Qc > 2000, "S3 <Q_E>/Q_c = %.0f: the background mean is thousands of times past the vacuum edge" % (sig2 / Qc))
xrms = kH * sig2
chk(close(xrms, 1.23e3, 0.02), "S3 x at <Q_E> = %.3e (F6 quoted ~1.2e3): linear formula is outside its regime" % xrms)

# stationary Gaussian background: Q = (c1^2+c2^2)/2, c_i ~ N(0,sigma^2)  => Q ~ Exp(mean sigma^2)
pvac = -np.expm1(-Qc / sig2)
info("P(EW vacuum present) = 1 - exp(-Q_c/sigma^2) = %.4e" % pvac)
chk(abs(pvac - 4.07e-4) < 1.5e-5, "S3 fraction of time with an EW vacuum = %.3e (premise: stationary Gaussian, ergodic)" % pvac)
rng = np.random.default_rng(20261016)
Ntot, chunk = 24_000_000, 2_000_000
hits, below = 0, np.zeros(3, dtype=np.int64)
qs = np.array([-np.log(0.9), -np.log(0.5), -np.log(0.1)])  # in units of sigma^2: CDF 0.1,0.5,0.9
for _ in range(Ntot // chunk):
    c = rng.standard_normal((2, chunk))
    Qs = 0.5 * (c[0] ** 2 + c[1] ** 2)          # units of sigma^2
    hits += int(np.count_nonzero(Qs < Qc / sig2))
    for i, q in enumerate(qs):
        below[i] += int(np.count_nonzero(Qs < q))
emp = hits / Ntot
chk(abs(emp - pvac) < 5 * np.sqrt(pvac * (1 - pvac) / Ntot), "S3 Monte Carlo (%d draws) vacuum fraction %.3e vs %.3e" % (Ntot, emp, pvac))
chk(all(abs(below[i] / Ntot - p_) < 5e-4 for i, p_ in enumerate([0.1, 0.5, 0.9])), "S3 Monte Carlo CDF of Q at 0.1/0.5/0.9 matches Exp(1)")

# dichotomy for kappa>0:  d ln v/dt = -kappa Qdot/(1-2 kappa Q)  so |rate| >= kappa|Qdot| whenever v exists
t_ = sp.symbols("t")
Qf = sp.Function("Q")(t_)
kk = sp.symbols("kappa", positive=True)
rate = sp.diff(sp.log(sp.sqrt(1 - 2 * kk * Qf)), t_)
chk(sp.simplify(rate + kk * sp.diff(Qf, t_) / (1 - 2 * kk * Qf)) == 0, "S3 d ln v/dt = -kappa Qdot/(1-2 kappa Q) (symbolic)")
ok = True
rs = np.random.default_rng(7)
for _ in range(2000):
    xq = Fr(int(rs.integers(1, 499)), 1000)       # x in (0, 1/2)
    ok &= (1 / (1 - 2 * xq)) > 1
chk(ok, "S3 for 0<x<1/2 the exact instantaneous rate exceeds the linear one by 1/(1-2x) > 1 (linear is a lower bound where v exists)")

# regime: linear formula within 10% iff x <= 0.05  (1/(1-2x) <= 1.1)
kreg = 0.05 / sig2
max_ex = kreg / kclock_hi
info("regime edge: kappa <= %.3e; formal exceedance meaningful only up to %.3e (F6 quotes %.3e)" % (kreg, max_ex, E_formal))
chk(E_formal > 1e3 * max_ex, "S3 F6 formal exceedance is %.0fx beyond the largest in-regime exceedance" % (E_formal / max_ex))
x_comp = kappa_ans * sig2
chk(x_comp < 1e-20 and (s_toy * A_amp * sig2) < 1e-20, "S3 composite candidates are deep in the linear regime (x = %.1e, %.1e)" % (x_comp, s_toy * A_amp * sig2))
# negative sign (c_H < 0, e.g. dressed branch): v^2/v0^2 = 1 + 2|x|, no vacuum loss but growth
chk(sp.simplify((mu2 + 2 * mu2 * x_) / mu2 - (1 + 2 * x_)) == 0, "S3 for c_H<0, v grows as sqrt(1+2|x|) (x=%.1e would give v/v0 ~ %.0f)" % (xrms, np.sqrt(1 + 2 * xrms)))
# Taylor parameter of Sigma_H(t) in the strain is t^2 ~ Q, not x
chk(sig2 < 1e-27 and xrms > 1, "S3 expansion parameter of Sigma_H(strain) is Q ~ %.0e (small); the large number is x = kappa Q" % sig2)

# ---------------------------------------------------------------------------
# 4/5. The O(N) N=infinity toy (E1 section 3 b-5): reconstruct and close the form
# ---------------------------------------------------------------------------
mp.mp.dps = 30


def Iint(m2, Jx, Jy):
    """int d^2q/(2pi)^2 1/(m2 + Jx(2-2cos qx) + Jy(2-2cos qy)); qx integral done exactly."""
    f = lambda q: 1 / mp.sqrt((m2 + 2 * Jx + Jy * (2 - 2 * mp.cos(q))) ** 2 - 4 * Jx**2)
    sm = mp.sqrt(m2)
    pts = sorted(set([mp.mpf(0)] + [p for p in (sm, 10 * sm, mp.mpf(1)) if p < mp.pi] + [mp.pi]))
    return mp.quad(f, pts) / mp.pi


# independent method: 2D periodic trapezoid (exponentially convergent), slabbed
def I2d(m2, Jx, Jy, N=1536):
    q = (np.arange(N) + 0.5) * 2 * np.pi / N
    ex = Jx * (2 - 2 * np.cos(q))
    tot = 0.0
    for i0 in range(0, N, 256):
        ey = Jy * (2 - 2 * np.cos(q[i0:i0 + 256]))
        tot += np.sum(1.0 / (m2 + ex[None, :] + ey[:, None]))
    return tot / N**2


for m in (0.1, 0.05):
    a = float(Iint(mp.mpf(m) ** 2, mp.mpf("1.2"), mp.mpf("0.8")))
    b = I2d(m**2, 1.2, 0.8)
    chk(abs(a - b) < 1e-10, "S5 gap-equation integral: mpmath 1D reduction vs numpy 2D grid at m=%g (%.12f vs %.12f)" % (m, a, b))

m = mp.mpf("1e-3")
chk(abs(Iint(m**2, 1, 1) - mp.log(32 / m**2) / (4 * mp.pi)) < mp.mpf("1e-5"), "S5 isotropic I(m) = (1/4pi) ln(32/m^2) to O(m^2 ln m)")

# closed form of the asymptote: I = (1/(4 pi sqrt(JxJy))) ln( 64 JxJy / ((Jx+Jy) m^2) )
worst = mp.mpf(0)
m2 = mp.mpf("1e-12")
for (Jx, Jy) in [("1.0", "1.0"), ("1.2", "0.8"), ("2.5", "0.4"), ("3.0", "1.0"), ("0.1", "7.0")]:
    Jx, Jy = mp.mpf(Jx), mp.mpf(Jy)
    form = mp.log(64 * Jx * Jy / ((Jx + Jy) * m2)) / (4 * mp.pi * mp.sqrt(Jx * Jy))
    worst = max(worst, abs(Iint(m2, Jx, Jy) - form))
chk(worst < mp.mpf("1e-9"), "S5 asymptote I = ln(64 JxJy/((Jx+Jy) m^2))/(4 pi sqrt(JxJy)), max error %s (CHECKED, not proved)" % mp.nstr(worst, 3))


def dlnm_t2(xi0, law, t):
    m0 = mp.mpf(1) / xi0
    target = Iint(m0**2, 1, 1)
    Jx, Jy = (1 + t, 1 - t) if law == "lin" else (mp.e**t, mp.e ** (-t))
    lm = mp.findroot(lambda z: Iint(mp.e ** (2 * z), Jx, Jy) - target, mp.log(m0))
    return (lm - mp.log(m0)) / t**2


E1tab = {10: 1.50, 100: 2.67, 1000: 3.82, 10000: 4.97, 100000: 6.12}
okt = True
for xi0, ref in E1tab.items():
    r1 = dlnm_t2(mp.mpf(xi0), "lin", mp.mpf("0.01"))
    r2 = dlnm_t2(mp.mpf(xi0), "lin", mp.mpf("0.005"))
    r0 = (4 * r2 - r1) / 3
    okt &= abs(float(r0) - ref) < 0.006
    info("toy linear law xi0=%g: d ln m/t^2 = %.5f (E1: %.2f), minus 0.5 ln xi0 = %.5f" % (xi0, float(r0), ref, float(r0 - mp.log(xi0) / 2)))
chk(okt, "S5 E1's linear-law table 1.50/2.67/3.82/4.97/6.12 reproduced from the N=infinity gap equation")
re = dlnm_t2(mp.mpf(1000), "exp", mp.mpf("0.005"))
chk(abs(float(re) + 0.25) < 1e-3, "S5 unimodular (exponential) law gives -1/4, no log (got %.5f)" % float(re))
r0big = (4 * dlnm_t2(mp.mpf(10) ** 5, "lin", mp.mpf("0.005")) - dlnm_t2(mp.mpf(10) ** 5, "lin", mp.mpf("0.01"))) / 3
chk(abs(float(r0big - mp.log(10) ** 1 * 5 / 2) - float(cN)) < 2e-4,
    "S5 closed constant: d ln m/t^2 -> (1/2) ln xi0 + (1/4)ln32 - 1/2 = +%.5f" % float(cN))

# symbolic derivation from the closed asymptote (linear law, large xi0)
tt, lxi = sp.symbols("t L", positive=True)    # L = ln xi0
Jx_, Jy_ = 1 + tt, 1 - tt
lnm = sp.Rational(1, 2) * sp.log(64 * Jx_ * Jy_ / (Jx_ + Jy_)) - 2 * sp.pi * sp.sqrt(Jx_ * Jy_) * (lxi + sp.log(32) / 2) / (2 * sp.pi)
lnm0 = lnm.subs(tt, 0)
coef = sp.simplify(sp.series(lnm - lnm0, tt, 0, 3).removeO().coeff(tt, 2))
chk(sp.simplify(coef - (lxi / 2 + sp.log(32) / 4 - sp.Rational(1, 2))) == 0, "S5 sympy: order-t^2 coefficient = L/2 + ln(32)/4 - 1/2 from the closed form")
# response-law dependence of the log: the L-dependence comes only from sqrt(JxJy) = 1 - t^2/2
Jx2, Jy2 = sp.exp(tt), sp.exp(-tt)
lnm_e = sp.Rational(1, 2) * sp.log(64 * Jx2 * Jy2 / (Jx2 + Jy2)) - sp.sqrt(Jx2 * Jy2) * (lxi + sp.log(32) / 2)
coef_e = sp.simplify(sp.series(lnm_e - lnm_e.subs(tt, 0), tt, 0, 3).removeO().coeff(tt, 2))
chk(sp.simplify(coef_e + sp.Rational(1, 4)) == 0, "S5 sympy: unimodular law gives exactly -1/4 at every L")

# ---------------------------------------------------------------------------
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
if n_fail == 0:
    print("HIT: composite-clock margins 5.6e11 and 5.9e7 are one chain (A=Lambda^2/m_H^2) times two borrowed strain coefficients, "
          "the ansatz equals F6's (l_P/a)^2 rule with 1/a->Lambda, and the exact tree-level vev map puts the formal 2.6e18 clock exceedance outside its regime (vacuum present ~4e-4 of the time)")
print("SUMMARY: Reduces the composite/clock transfer to two undetermined numbers (A, s) with a clock bound s*A<=6.7e12, "
      "reproduces the O(N) toy in closed form (d ln m/t^2 = L/2 + ln32/4 - 1/2, law-dependent), and replaces the linearized clock rate by an exact vev dichotomy; "
      "no composite-Higgs coefficient is derived.")
sys.exit(0 if n_fail == 0 else 1)
