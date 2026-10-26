#!/usr/bin/env python3
"""Exact Koide/Brannen pair (r=1/2, delta=2/9): independent comparison, covariance,
statistical reading, and mass-scheme map (pole vs MS-bar).

Machinery (disjoint from scripts/koide_exact_pair_pole_mass_precision_check_2026_09_30.py):
  sympy symbolic algebra; mpmath INTERVAL arithmetic (rigorous enclosures);
  closed-form generalized-least-squares in a log basis (e, mu/e, tau);
  scipy least_squares cross-check in MeV space with the full covariance.
It derives neither r=1/2 nor delta=2/9.  Inputs are external comparator data.

Check classes: [P] proved by exact/interval arithmetic, [C] numerical check,
[D] external datum, [T] transcription of a published formula (verified by a
reproduction test).  Deterministic; runtime a few seconds.
"""
import math
import sys

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.optimize import least_squares

mp.mp.dps = 50
PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("PASS " + name + (" | " + detail if detail else ""))
    else:
        FAIL += 1
        print("FAIL " + name + (" | " + detail if detail else ""))


HIT_LINES = []

# ---------------------------------------------------------------------------
# A. symbolic algebra [P]
# ---------------------------------------------------------------------------
th = sp.symbols("theta", real=True)
roots = []
for k in range(3):
    ck = sp.cos(2 * sp.pi * k / 3)
    sk = sp.sin(2 * sp.pi * k / 3)
    roots.append(1 + sp.sqrt(2) * (sp.cos(th) * ck - sp.sin(th) * sk))
S1 = sp.expand(sum(roots))
S2 = sp.expand(sum(v ** 2 for v in roots))
S2 = sp.simplify(S2.subs(sp.sin(th) ** 2, 1 - sp.cos(th) ** 2))
S2 = sp.simplify(sp.expand(S2).subs(sp.sin(th) ** 2, 1 - sp.cos(th) ** 2))
check("A1 [P] sum of the three roots is exactly 3 for every theta (sympy)", sp.simplify(S1 - 3) == 0)
check("A2 [P] sum of squared roots is exactly 6 for every theta (sympy); hence Q=6/9=2/3 phase-blind",
      sp.simplify(S2 - 6) == 0, "S2=" + str(S2))
rr = sp.symbols("r", positive=True)
Sg = 0
for k in range(3):
    ck = sp.cos(2 * sp.pi * k / 3)
    sk = sp.sin(2 * sp.pi * k / 3)
    Sg += (1 + 2 * sp.sqrt(rr) * (sp.cos(th) * ck - sp.sin(th) * sk)) ** 2
Sg = sp.simplify(sp.expand(Sg).subs(sp.sin(th) ** 2, 1 - sp.cos(th) ** 2))
Qg = sp.simplify(Sg / 9)
check("A3 [P] general family: Q=(1+2r)/3 (sympy), so r=1/2 <=> Q=2/3", sp.simplify(Qg - (1 + 2 * rr) / 3) == 0, str(Qg))

# ---------------------------------------------------------------------------
# B. interval enclosure of the exact-pair predictions [P]
# ---------------------------------------------------------------------------
iv = mp.iv
iv.dps = 40
K_TAU, K_E, K_MU = 0, 1, 2


def ivroot(k, d, r2=None):
    s = iv.sqrt(iv.mpf(2)) if r2 is None else 2 * iv.sqrt(r2)
    return 1 + s * iv.cos(d + 2 * iv.pi * k / 3)


d0 = iv.mpf(2) / 9
vE, vM, vT = ivroot(K_E, d0), ivroot(K_MU, d0), ivroot(K_TAU, d0)
check("B1 [P] at delta=2/9 all three roots are strictly positive (interval)", vE.a > 0 and vM.a > 0 and vT.a > 0,
      "vE=%s vM=%s vT=%s" % (mp.nstr(vE.mid, 8), mp.nstr(vM.mid, 8), mp.nstr(vT.mid, 8)))
check("B2 [P] ordering electron<muon<tau is rigorous (intervals disjoint)", vE.b < vM.a and vM.b < vT.a)
X = (vM / vE) ** 2
Y = (vT / vM) ** 2
check("B3 [P] x_pred=m_mu/m_e of the exact pair enclosed in [206.7703159, 206.7703160] (interval, 40 digits)",
      X.a > mp.mpf("206.7703159") and X.b < mp.mpf("206.7703160"),
      "x_pred=" + mp.nstr(X.mid, 14) + " width " + mp.nstr(X.delta, 3))
check("B4 [P] y_pred=m_tau/m_mu of the exact pair enclosed to width <1e-30 (interval)", Y.delta < mp.mpf("1e-30"),
      "y_pred=" + mp.nstr(Y.mid, 15))
X_PRED = mp.mpf(X.mid)
Y_PRED = mp.mpf(Y.mid)
W_PRED = X_PRED * Y_PRED  # m_tau/m_e


# monotonicity of x in delta on [0.20,0.24]: derivative of ln x
def dlnx_iv(dint):
    out = []
    for k in (K_MU, K_E):
        v = ivroot(k, dint)
        dv = -iv.sqrt(iv.mpf(2)) * iv.sin(dint + 2 * iv.pi * k / 3)
        out.append(dv / v)
    return 2 * (out[0] - out[1])


dint = iv.mpf([mp.mpf("0.20"), mp.mpf("0.24")])
dl = dlnx_iv(dint)
check("B5 [P] d ln x/d delta > 0 on all of [0.20,0.24] (interval); lower bound", dl.a > 0, mp.nstr(dl.a.mid, 6))
check("B6 [P] x(0.20)<206.768 and x(0.24)>206.77: with B5 the delta fitting any m_mu/m_e in that range is unique",
      ((ivroot(K_MU, iv.mpf("0.20")) / ivroot(K_E, iv.mpf("0.20"))) ** 2).b < mp.mpf("206.768")
      and ((ivroot(K_MU, iv.mpf("0.24")) / ivroot(K_E, iv.mpf("0.24"))) ** 2).a > mp.mpf("206.77"),
      "bracket")


def xr(d, r=mp.mpf(1) / 2):
    f = lambda k: 1 + 2 * mp.sqrt(r) * mp.cos(d + 2 * mp.pi * k / 3)
    return (f(K_MU) / f(K_E)) ** 2


def wr(d, r=mp.mpf(1) / 2):
    f = lambda k: 1 + 2 * mp.sqrt(r) * mp.cos(d + 2 * mp.pi * k / 3)
    return (f(K_TAU) / f(K_E)) ** 2


# ---------------------------------------------------------------------------
# C. inputs [D]
# ---------------------------------------------------------------------------
M = mp.mpf
SETS = {
    # CODATA 2022 (NIST web values retrieved this session): m_e c^2 = 0.51099895069(16) MeV,
    # m_mu/m_e = 206.7682827(46); tau mass: PDG current listing 1776.93 +- 0.09 MeV.
    "current": dict(me=(M("0.51099895069"), M("0.00000000016")), R=(M("206.7682827"), M("0.0000046")),
                    mt=(M("1776.93"), M("0.09"))),
    # Belle II 2023, PRD 108, 032006: 1777.09 +- 0.08 +- 0.11
    "tau=BelleII": dict(me=(M("0.51099895069"), M("0.00000000016")), R=(M("206.7682827"), M("0.0000046")),
                        mt=(M("1777.09"), mp.sqrt(M("0.08") ** 2 + M("0.11") ** 2))),
    # BESIII 2014: 1776.91 +- 0.12 (+0.10 -0.13): symmetrised conservatively
    "tau=BESIII": dict(me=(M("0.51099895069"), M("0.00000000016")), R=(M("206.7682827"), M("0.0000046")),
                       mt=(M("1776.91"), mp.sqrt(M("0.12") ** 2 + M("0.13") ** 2))),
}
# the electron value the repo labels 'PDG 2024' (0.51099895000(15)) is the CODATA-2018 value
ME_REPO = (M("0.51099895000"), M("0.00000000015"))
MMU_REPO = (M("105.6583755"), M("0.0000023"))
R_repo = MMU_REPO[0] / ME_REPO[0]
sR_repo = R_repo * mp.sqrt((ME_REPO[1] / ME_REPO[0]) ** 2 + (MMU_REPO[1] / MMU_REPO[0]) ** 2)
check("C0 [D] repo-labelled 'PDG2024' m_e differs from CODATA-2022 m_e by 6.9e-10 MeV (1.35e-9 relative)",
      abs(abs(SETS["current"]["me"][0] - ME_REPO[0]) - M("0.00000000069")) < M(10) ** -20)
check("C1 [D] ratio from the repo-labelled pair vs CODATA-2022 ratio differ by <0.1 sigma_R",
      abs(R_repo - SETS["current"]["R"][0]) < M("0.1") * SETS["current"]["R"][1],
      "R_repo=" + mp.nstr(R_repo, 12) + " (sigma %s)" % mp.nstr(sR_repo, 3))


def analysis(S):
    me, sme = S["me"]
    R, sR = S["R"]
    mt, smt = S["mt"]
    s_e, s_R, s_t = sme / me, sR / R, smt / mt
    # log-basis data: (ln m_e, ln R, ln m_tau) independent => diagonal covariance
    ln_x_obs = mp.log(R)
    ln_w_obs = mp.log(mt / me)
    s_w = mp.sqrt(s_e ** 2 + s_t ** 2)
    zx = (mp.log(X_PRED) - ln_x_obs) / s_R
    zw = (mp.log(W_PRED) - ln_w_obs) / s_w
    chi2 = zx ** 2 + zw ** 2  # scale profiled out in closed form
    return dict(zx=zx, zw=zw, chi2=chi2, s_R=s_R, s_w=s_w, ln_x_obs=ln_x_obs, ln_w_obs=ln_w_obs, s_e=s_e, s_t=s_t)


RES = {k: analysis(v) for k, v in SETS.items()}
for k, a in RES.items():
    print("   [%s] z_x=%s  z_w=%s  chi2(2 dof, scale profiled)=%s" %
          (k, mp.nstr(a["zx"], 6), mp.nstr(a["zw"], 4), mp.nstr(a["chi2"], 5)))

# scipy cross-check in MeV space with the full covariance (m_mu = R m_e is correlated with m_e)
S = SETS["current"]
me0, mm0, mt0 = float(S["me"][0]), float(S["me"][0] * S["R"][0]), float(S["mt"][0])
# independent basis p=(m_e,R,m_tau) -> masses (m_e, R m_e, m_tau): Jacobian
J = np.array([[1, 0, 0], [float(S["R"][0]), me0, 0], [0, 0, 1]])
Cp = np.diag([float(S["me"][1]) ** 2, float(S["R"][1]) ** 2, float(S["mt"][1]) ** 2])
Cm = J @ Cp @ J.T
Lc = np.linalg.cholesky(np.linalg.inv(Cm))
f_pred = np.array([float(((1 + 2 ** 0.5 * math.cos(2 / 9 + 2 * math.pi * k / 3)) ** 2)) for k in (K_E, K_MU, K_TAU)])
d_obs = np.array([me0, mm0, mt0])
res = least_squares(lambda s: Lc.T @ (d_obs - s[0] * f_pred), x0=[me0 / f_pred[0]], xtol=1e-15, ftol=1e-15, gtol=1e-15)
chi2_np = float(np.sum(res.fun ** 2))
check("C2 [C] scipy MeV-space correlated-covariance chi2 agrees with closed-form log-basis chi2 to 1% (linearisation)",
      abs(chi2_np / float(RES["current"]["chi2"]) - 1) < 0.01,
      "scipy=%.5g closed=%s" % (chi2_np, mp.nstr(RES["current"]["chi2"], 6)))
# explicit: ln x = ln R ; ln w = ln m_tau - ln m_e ; independent => corr(ln x, ln w)=0 ; corr(ln x, ln y)=-s_R/s_y
s_y = mp.sqrt(RES["current"]["s_R"] ** 2 + RES["current"]["s_w"] ** 2)
corr_xy = -RES["current"]["s_R"] ** 2 / (RES["current"]["s_R"] * s_y)
check("C3 [C] corr(ln m_mu/m_e, ln m_tau/m_mu) is below 1e-3 in magnitude (shared m_mu)", abs(corr_xy) < M("1e-3"),
      mp.nstr(corr_xy, 3))
check("C4 [C] z_x > 400 for every tau-mass choice (the miss is a statement about m_mu/m_e alone)",
      all(a["zx"] > 400 for a in RES.values()), ", ".join(mp.nstr(a["zx"], 5) for a in RES.values()))
check("C5 [C] y-direction (m_tau/m_e) is consistent: |z_w|<1.5 for every tau-mass choice",
      all(abs(a["zw"]) < 1.5 for a in RES.values()), ", ".join(mp.nstr(a["zw"], 3) for a in RES.values()))
check("C6 [C] chi2 of the pair equals z_x^2 to within 0.1 percent for the current set",
      abs(RES["current"]["chi2"] / RES["current"]["zx"] ** 2 - 1) < M("1e-3"))
# best scale deviations
a2 = None
me, sme = S["me"]; R, sR = S["R"]; mt, smt = S["mt"]
u1 = mp.log(me) - mp.log(M(f_pred[0]))
ff = [mp.mpf(1)] * 3
fE = ((1 + mp.sqrt(2) * mp.cos(M(2) / 9 + 2 * mp.pi / 3)) ** 2)
fM = ((1 + mp.sqrt(2) * mp.cos(M(2) / 9 + 4 * mp.pi / 3)) ** 2)
fT = ((1 + mp.sqrt(2) * mp.cos(M(2) / 9)) ** 2)
wE, wT = 1 / (sme / me) ** 2, 1 / (smt / mt) ** 2
wR = 1 / (sR / R) ** 2
# profile ln a^2 over the three log data (e, mu=R e, tau): use mass-space independent logs (e, R, tau) -> A from e and tau
A = (wE * (mp.log(me) - mp.log(fE)) + wT * (mp.log(mt) - mp.log(fT))) / (wE + wT)
devs = [mp.exp(A) * fE / me - 1, mp.exp(A) * fM / (R * me) - 1, mp.exp(A) * fT / mt - 1]
print("   best-scale deviations (e, mu, tau):", ", ".join(mp.nstr(d, 3) for d in devs))
check("C7b [C] ...with the scale fitted, each mass is reproduced to better than 1e-4 relative",
      all(abs(d) < M("1e-4") for d in devs))

# ---------------------------------------------------------------------------
# D. geometry in the (r, delta) plane [C]
# ---------------------------------------------------------------------------
a0 = RES["current"]
R_obs = SETS["current"]["R"][0]
d_fit = mp.findroot(lambda d: xr(d) - R_obs, M(2) / 9)
check("D1 [P/C] delta fitting m_mu/m_e at r=1/2 is 2/9 - 1.75e-7 (and the exact bracket from B6 is unique)",
      M("-1.76e-7") < d_fit - M(2) / 9 < M("-1.74e-7"), mp.nstr(d_fit - M(2) / 9, 6))
dlnx = mp.diff(lambda d: mp.log(xr(d)), M(2) / 9)
sig_d = a0["s_R"] / dlnx
check("D2 [C] sigma_delta from m_mu/m_e is about 4e-10 and 2/9 lies about 430-450 sigma from the fit",
      M("3e-10") < sig_d < M("5e-10") and 400 < (M(2) / 9 - d_fit) / sig_d < 460,
      "sigma=%s, z=%s" % (mp.nstr(sig_d, 3), mp.nstr((M(2) / 9 - d_fit) / sig_d, 5)))


def delta_c(r):
    return mp.findroot(lambda d: xr(d, r) - R_obs, d_fit)


def zw_arc(r):
    return (mp.log(wr(delta_c(r), r)) - a0["ln_w_obs"]) / a0["s_w"]


r_star = mp.findroot(lambda r: xr(M(2) / 9, r) - R_obs, M(1) / 2)
check("D3 [C] at delta=2/9 the r fitting m_mu/m_e is r* (offset from 1/2 printed); z_w(r*) acceptable",
      abs(zw_arc(r_star)) < 1.5, "r*-1/2=%s, z_w(r*)=%s" % (mp.nstr(r_star - M(1) / 2, 5), mp.nstr(zw_arc(r_star), 3)))
def bisect(f, lo, hi, n=80):
    flo = f(lo)
    for _ in range(n):
        mid = (lo + hi) / 2
        fm = f(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


r_lo = bisect(lambda r: zw_arc(r) + 2, M(1) / 2 - M("5e-5"), M(1) / 2)
r_hi = bisect(lambda r: zw_arc(r) - 2, M(1) / 2, M(1) / 2 + M("5e-5"))
print("   2-sigma window of r along the m_mu/m_e arc (from m_tau): [%s, %s]" % (mp.nstr(r_lo, 9), mp.nstr(r_hi, 9)))
check("D4 [C] the m_mu/m_e arc passes through the 2-sigma tau window at both r=1/2 and delta=2/9 ...",
      r_lo < M(1) / 2 < r_hi and r_lo < r_star < r_hi)
check("D5 [C] ... but the two crossings are different points: separation in delta at r=1/2 is 1.75e-7 (transverse), "
      "i.e. the pair needs r and delta from different points of the arc",
      abs((d_fit - M(2) / 9) + M("1.75e-7")) < M("1e-9") and abs(r_star - M(1) / 2) > M("1e-7"))

# statistical floor
miss = mp.log(X_PRED) - a0["ln_x_obs"]
sig_th2 = miss / 2
sig_th_need = mp.sqrt(sig_th2 ** 2 - a0["s_R"] ** 2)
apipi = (1 / M("137.035999177") / mp.pi) ** 2
print("   ln(x_pred/x_obs)=%s ; theory floor sigma_th on ln(m_mu/m_e) for z_eff<=2: %s ; (alpha/pi)^2=%s" %
      (mp.nstr(miss, 5), mp.nstr(sig_th_need, 4), mp.nstr(apipi, 4)))
check("D6 [C] the miss is 9.8e-6 relative, a floor of about 4.9e-6 would make 2 sigma; ratio floor/(alpha/pi)^2 printed (~0.9)",
      M("9.7e-6") < miss < M("9.9e-6") and M("0.5") < sig_th_need / apipi < M("1.5"),
      "floor/(alpha/pi)^2=%s" % mp.nstr(sig_th_need / apipi, 4))

# ---------------------------------------------------------------------------
# E. mass-scheme map
# ---------------------------------------------------------------------------
# E1: one-loop fixed-alpha common-mu MSbar conversion: mu-independence of shifts [P]
a_, mu_, m1, m2 = sp.symbols("a mu m1 m2", positive=True)
eps = lambda m: -a_ * (1 + sp.Rational(3, 2) * sp.log(mu_ / m))
diff_eps = sp.simplify(eps(m1) - eps(m2))
check("E1 [P] one-loop fixed-alpha conversion: eps_1-eps_2 = (3a/2) ln(m1/m2), independent of mu (sympy)",
      sp.simplify(sp.diff(diff_eps, mu_)) == 0 and sp.simplify(diff_eps - sp.Rational(3, 2) * a_ * sp.log(m1 / m2)) == 0,
      str(sp.simplify(diff_eps)))
pole = [SETS["current"]["me"][0], SETS["current"]["me"][0] * R_obs, SETS["current"]["mt"][0]]
tot = sum(pole)
sq = sum(mp.sqrt(m) for m in pole)
wts = [m / tot - mp.sqrt(m) / sq for m in pole]
check("E2 [P] first-order weights of d ln Q sum to zero (scale invariance), so the common eps cancels",
      abs(sum(wts)) < mp.mpf(10) ** -40)
alpha = 1 / M("137.035999177")
dlnQ1 = sum(w * M(3) / 2 * alpha / mp.pi * mp.log(m) for w, m in zip(wts, pole))
Q_pole = tot / sq ** 2
dQ1 = dlnQ1 * Q_pole
print("   first-order common-mu MSbar shift of Q: dQ=%s ; of ln(m_mu/m_e): %s" %
      (mp.nstr(dQ1, 5), mp.nstr(M(3) / 2 * alpha / mp.pi * mp.log(pole[1] / pole[0]), 5)))
check("E3 [C] first-order shift of Q is mu-independent, about 1.1e-3 to 1.3e-3, >100x |Q_pole-2/3|",
      M("1.0e-3") < dQ1 < M("1.4e-3") and dQ1 > 100 * abs(Q_pole - M(2) / 3),
      "Q_pole-2/3=%s" % mp.nstr(Q_pole - M(2) / 3, 4))
# explicit nonlinear check vs linear for several mu (window up to 5 GeV, where a*ln < 0.05)
nl = []
for mu in (M("1777"), M("3000"), M("5000")):
    conv = [m * (1 - alpha / mp.pi * (1 + M(3) / 2 * mp.log(mu / m))) for m in pole]
    nl.append((sum(conv) / sum(mp.sqrt(m) for m in conv) ** 2 - Q_pole))
check("E4 [C] exponentiated conversion at mu=1.8,3,5 GeV stays within 5 percent of the mu-independent first-order dQ",
      all(abs(x / dQ1 - 1) < M("0.05") for x in nl), ", ".join(mp.nstr(x, 4) for x in nl))

# E5: the QED two-loop relation M/m(m) reconstructed from Melnikov-van Ritbergen (hep-ph/9912391) Eq.(10) [T]
z3, pi, l2 = mp.zeta(3), mp.pi, mp.log(2)
d1 = M(7) / 128 - M(3) / 4 * z3 + pi ** 2 / 2 * l2 - 5 * pi ** 2 / 16
d2 = -M(1111) / 384 + M(3) / 8 * z3 - pi ** 2 / 4 * l2 + pi ** 2 / 12
d3 = M(71) / 96 + pi ** 2 / 12
d4 = M(143) / 96 - pi ** 2 / 6


def two_loop_coeff(CF, CA, TR, NL, NH):
    # m(M)/M = 1 - CF a + CF a^2 [CF d1 + CA d2 + TR NL d3 + TR NH d4];
    # M/m(m) = 1 + CF a + a^2 c2 with c2 = -CF*D - CF^2/2  (uses gamma_m0=3CF/4 and ln(M/m)=CF a)
    D = CF * d1 + CA * d2 + TR * NL * d3 + TR * NH * d4
    return -CF * D - CF ** 2 / 2


c_qcd0 = two_loop_coeff(M(4) / 3, 3, M(1) / 2, 0, 1)
c_qcd5 = two_loop_coeff(M(4) / 3, 3, M(1) / 2, 5, 1)
check("E5 [T] reconstruction reproduces the published QCD numbers 13.4434 (N_L=0) and 13.4434-5*1.0414=8.2364 (N_L=5)",
      abs(c_qcd0 - M("13.4434")) < M("5e-4") and abs(c_qcd5 - (M("13.4434") - 5 * M("1.0414"))) < M("5e-3"),
      "%s, %s" % (mp.nstr(c_qcd0, 7), mp.nstr(c_qcd5, 7)))
c0 = two_loop_coeff(M(1), 0, M(1), 0, 1)
cl = two_loop_coeff(M(1), 0, M(1), 1, 1) - c0
check("E6 [T] QED (C_F=T_R=1, C_A=0): N_L-independent coefficient c0 and per-light-lepton slope = -(71/96+pi^2/12)",
      abs(cl + d3) < M(10) ** -40, "c0=%s, slope=%s" % (mp.nstr(c0, 8), mp.nstr(cl, 10)))

# E7: own-scale scheme m_i(m_i): alpha^{(n)}(m_i) from one-loop running of the electron/muon loops
me_, mm_, mt_ = pole
pole_mt = SETS["current"]["mt"][0]
a_e = alpha / mp.pi
a_mu = alpha / mp.pi * (1 + alpha / (3 * mp.pi) * mp.log(mm_ ** 2 / me_ ** 2))
a_tau = alpha / mp.pi * (1 + alpha / (3 * mp.pi) * (mp.log(mt_ ** 2 / me_ ** 2) + mp.log(mt_ ** 2 / mm_ ** 2)))
Re = 1 + a_e + c0 * a_e ** 2
Rm = 1 + a_mu + (c0 + cl) * a_mu ** 2
Rt = 1 + a_tau + (c0 + 2 * cl) * a_tau ** 2
dx_own = mp.log(Re / Rm)      # ln(x_own/x_pole)
dw_own = mp.log(Re / Rt)      # ln(w_own/w_pole), w=m_tau/m_e
print("   own-scale MSbar: ln(x_own/x_pole)=%s (running-coupling piece %s, N_L piece %s) ; ln(w_own/w_pole)=%s" %
      (mp.nstr(dx_own, 5), mp.nstr(-(a_mu - a_e), 4), mp.nstr(-cl * a_e ** 2, 4), mp.nstr(dw_own, 4)))
check("E7 [C] the O(alpha) own-scale conversion is flavour-universal (cancels in ratios) so ln(x_own/x_pole) is O(alpha^2)",
      abs(dx_own) < M("5e-5") and abs(dx_own) > 0)
check("E8 [C] sign: the two O(alpha^2) pieces have opposite sign; net ln(x_own/x_pole) is negative (-1.0e-5 .. -1.2e-5)",
      M("-1.2e-5") < dx_own < M("-1.0e-5"), mp.nstr(dx_own, 5))
# compare the own-scale data with the exact pair
x_obs_own = mp.exp(a0["ln_x_obs"] + dx_own)
w_obs_own = mp.exp(a0["ln_w_obs"] + dw_own)
zx_own = (mp.log(X_PRED) - mp.log(x_obs_own)) / a0["s_R"]
zw_own = (mp.log(W_PRED) - mp.log(w_obs_own)) / a0["s_w"]
# theory-truncation allowance for the scheme map: O(a^3) flavour-dependent terms from Eq.(13) of the source
# (QCD colour factors, used only as a size estimate) plus unmodelled pieces
a3 = a_e ** 3
trunc = abs(M("-26.655")) * a3 + M("5e-7") + M("5e-8")  # a^3 N_L term; hadronic VP (order-of-magnitude assumption); massive-light-loop (assumption)
print("   exact pair vs own-scale-converted data: z_x=%s, z_w=%s ; truncation allowance on ln x: %s (%s sigma_R)" %
      (mp.nstr(zx_own, 5), mp.nstr(zw_own, 3), mp.nstr(trunc, 3), mp.nstr(trunc / a0["s_R"], 3)))
resid = mp.log(X_PRED) - mp.log(x_obs_own)
check("E9 [C] in the own-scale scheme the exact pair's miss of m_mu/m_e is about 2.1e-5 and exceeds 20x the truncation allowance",
      M("1.9e-5") < resid < M("2.3e-5") and resid > 20 * trunc, "miss=%s, allowance=%s" % (mp.nstr(resid, 4), mp.nstr(trunc, 3)))
check("E9b [C] robustness: even with every neglected piece inflated tenfold (allowance 10x), the own-scale miss exceeds it by >2x",
      resid > 2 * 10 * trunc, "miss/(10*allowance)=%s" % mp.nstr(resid / (10 * trunc), 3))
check("E10 [C] tau-direction in the own-scale scheme stays consistent (|z_w|<2)", abs(zw_own) < 2, mp.nstr(zw_own, 3))
# What scheme shift would be needed
need = mp.log(X_PRED) - a0["ln_x_obs"]
print("   required scheme shift of ln(m_mu/m_e) pole->scheme for the exact pair: %s ; pole-scheme is off by it; own-scale is off by %s" %
      (mp.nstr(need, 5), mp.nstr(resid, 5)))
check("E11 [C] required shift is positive (+9.8e-6) while both computed O(alpha^2) own-scale pieces net negative",
      need > 0 and dx_own < 0)

print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
print("SUMMARY: With exact interval/symbolic algebra and a covariance-complete log-basis fit, the exact Koide pair (1/2,2/9) misses "
      "pole-mass m_mu/m_e by 9.8e-6 (z=442 with the CODATA ratio error, about 450 with quadrature errors; all tau-mass choices), the miss is a scheme-sized O((alpha/pi)^2) quantity, "
      "and a reconstructed O(alpha^2) own-scale MSbar map moves m_mu/m_e the wrong way (miss grows to about 2e-5), "
      "so neither pole nor own-scale MSbar masses rescue the exact pair, and a fixed-order common-mu MSbar map moves Q by 1.15e-3 (500x the pole offset).")
sys.exit(1 if FAIL else 0)
