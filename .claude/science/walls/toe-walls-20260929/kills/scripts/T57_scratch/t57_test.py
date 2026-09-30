#!/usr/bin/env python3
"""T57 test: can any mechanism class make Omega_DM/Omega_b = R_base x S a consequence (not an input)?
Pre-registration: PREREG.md (same folder).  numpy/scipy only.  Inputs are the lane's own numbers.
"""
import math, itertools
from fractions import Fraction as F
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import kve
from scipy.optimize import brentq

# ---------------- lane inputs ----------------
v = 246.282818290129
m_DM = 16 * v                        # 3940.5 GeV (bypass note)
aLM = 0.090667836017286
xF = 25.0
K = 1.07e9                           # GeV^-1 (Kolb-Turner)
gstar_DM = 106.75
MPl = 1.2209e19
S_c = 1.59
Rb = F(31, 9)
R_pred = float(Rb) * S_c
mp = 0.938272
eta_obs = 6.12e-10
Oc, Ob = 0.1200, 0.02237
R_obs = Oc / Ob
sig_R = R_obs * math.sqrt((0.0012 / 0.12) ** 2 + (0.00015 / 0.02237) ** 2)
print("R_base = %s = %.4f ; R_pred(S=1.59) = %.4f ; R_obs = %.3f +/- %.3f" % (Rb, float(Rb), R_pred, R_obs, sig_R))

# ---------------- Boltzmann solver (symmetric s-wave relic) ----------------
def lnYeq(x, g, gs):
    # Y_eq = 45/(4 pi^4) (g/g*) x^2 K2(x); use kve for range
    return math.log(45 / (4 * math.pi ** 4) * g / gs) + 2 * math.log(x) + math.log(kve(2, x)) - x

def relic_Omega_h2(m, sigv, gs, g=4, x0=1.0, x1=None):
    """dY/dx = -(lam/x^2)(Y^2 - Yeq^2), lam = sqrt(pi/45) sqrt(g*) MPl m sigv. Returns Omega h^2, Y_inf, Y(x0)."""
    lam = math.sqrt(math.pi / 45) * math.sqrt(gs) * MPl * m * sigv
    x1 = x1 or max(2000.0, 60 * xF)
    def rhs(x, w):
        # w = ln Y
        Y = math.exp(w[0]); Ye2 = math.exp(2 * lnYeq(x, g, gs) - w[0])
        return [-(lam / x ** 2) * (Y - Ye2)]
    w0 = [lnYeq(x0, g, gs)]
    sol = solve_ivp(rhs, (x0, x1), w0, method="Radau", rtol=1e-8, atol=1e-10)
    Yinf = math.exp(sol.y[0, -1])
    return 2.742e8 * m * Yinf, Yinf, math.exp(w0[0])

def analytic_Omega_h2(m, sigv, gs, xf=xF):
    return K * xf / (math.sqrt(gs) * MPl * sigv)

print("\n== C1  R-free headline: DM relic density from the lane's formula alone")
sv_DM = math.pi * aLM ** 2 / m_DM ** 2
o_an = analytic_Omega_h2(m_DM, sv_DM, gstar_DM)
o_bz, Yinf_DM, Y0_DM = relic_Omega_h2(m_DM, sv_DM, gstar_DM)
print(" sigma v = pi a^2/m^2 = %.4e GeV^-2 ; Omega h^2 (lane formula, x_F=25) = %.4f ; full Boltzmann = %.4f" % (sv_DM, o_an, o_bz))
band = [analytic_Omega_h2(m_DM, sv_DM, gstar_DM, xf) for xf in (22, 28)]
print(" x_F band 22-28 -> Omega h^2 in [%.4f, %.4f]  (Planck 0.1200 %s the band)" % (min(band), max(band), "inside" if min(band) <= 0.12 <= max(band) else "outside"))
m_tgt_free = m_DM * math.sqrt(0.1200 / o_an)
print(" R-free target mass (Omega h^2 = 0.1200 directly, x_F=25): %.0f GeV ; 16 v is %+.1f%% from it" % (m_tgt_free, 100 * (m_DM / m_tgt_free - 1)))
Ob_from_R = o_an / R_pred
print(" bypass table row: Omega_b h^2 := Omega_DM h^2 / R = %.4f (table 0.0233); its 'R = Omega_DM/Omega_b' = %.4f = the INPUT R_pred -> not an independent output" % (Ob_from_R, o_an / Ob_from_R))

print("\n== A1  reading (I): baryons as a symmetric freeze-out relic, same formula (s-wave pi a^2/m^2, a = a_LM)")
sv_p = math.pi * aLM ** 2 / mp ** 2
o_p, Y_p, _ = relic_Omega_h2(mp, sv_p, 10.75, x1=3000)
print(" m_p: sigma v = %.4e GeV^-2 ; Omega_b,sym h^2 = %.3e ; Y_inf = %.3e (observed baryon Omega_b h^2 = 0.02237, n_b/s = 8.7e-11)" % (sv_p, o_p, Y_p))
R_sym = o_bz / o_p
print(" R_sym = Omega_DM(16v) / Omega_b,sym = %.3e   vs R_pred = %.3f  -> off by factor %.2e" % (R_sym, R_pred, R_sym / R_pred))
mpi = 0.13957
sv_qcd = 1.0 / mpi ** 2                # geometric hadronic annihilation, Kolb-Turner/Steigman type input (literature-type)
o_p2, Y_p2, _ = relic_Omega_h2(mp, sv_qcd, 10.75, x1=3000)
print(" with sigma v = 1/m_pi^2 = %.1f GeV^-2 (literature-type): Omega_b,sym h^2 = %.3e ; Y_inf = %.2e ; R_sym = %.2e" % (sv_qcd, o_p2, Y_p2, o_bz / o_p2))
# what visible mass would make the symmetric Lee-Weinberg ratio equal R_pred (lane's own formula)?
def f(m):
    o, _, _ = relic_Omega_h2(m, math.pi * aLM ** 2 / m ** 2, gstar_DM)
    return o_bz / o - R_pred
mvis = brentq(f, 100, 2 * m_DM)
print(" visible symmetric relic that would give R_pred (same s-wave formula, g*=106.75): m_vis = %.1f GeV = %.2f TeV = %.0f x m_p" % (mvis, mvis / 1e3, mvis / mp))
m0 = m_DM / 3
print(" April Hamming reading: m_dark = 3 m0 -> m0 = %.0f GeV ; visible states at %.0f and %.0f GeV (not baryons)" % (m0, m0, 2 * m0))

print("\n== B  reading (II): linked origin, R = (m_DM/m_p)(n_DM/n_b)")
need_ratio = R_pred * mp / m_DM
print(" IIa: at m_DM = 16 v the needed n_DM/n_b = %.3e  (~ 1/%.0f) ; nearest small-denominator rational (den<=100): %s" %
      (need_ratio, 1 / need_ratio, F(need_ratio).limit_denominator(100)))
for r in (F(1), F(1, 2), F(1, 3), F(3, 8), F(8, 79), F(28, 79), F(2), F(3)):
    print("     n_DM/n_b = %-6s -> m_DM = R m_p / ratio = %.2f GeV" % (r, R_pred * mp / float(r)))
# IIb: Boltzmann-suppressed asymmetry at decoupling, order-of-magnitude with g-ratio 1 and equal chemical potentials
def ratio_x(x, gr=1.0):
    return 12 * gr * (x / (2 * math.pi)) ** 1.5 * math.exp(-x)
for gr in (1 / 3, 1.0, 3.0):
    xs = brentq(lambda x: ratio_x(x, gr) - need_ratio, 3, 60)
    print(" IIb: g-ratio %.2f -> x = m/T_d = %.2f -> T_d = %.0f GeV (T_d/m = %.3f). T_d is a NEW dynamical number." % (gr, xs, m_DM / xs, 1 / xs))
# IIc: WIMPy conversion (suggested, order of magnitude)
Y_B = eta_obs / 7.04
dY = Y0_DM - Yinf_DM
print(" IIc: Y_B = eta/7.04 = %.2e ; DM number destroyed from x=1: dY = %.3e (per species) -> eps_needed ~ Y_B/dY = %.2e (a NEW CP number; = the eta problem, T58)" % (Y_B, dY, Y_B / dY))

print("\n== C2  look-elsewhere on the base (252 alternatives from the same Casimir data)")
C3, C2, d3, d2 = F(4, 3), F(3, 4), 8, 3
T3, T2 = F(1, 2), F(1, 2)
styles = {
    "C*dA (lane)": (C3 * d3, C2 * d2),
    "T*dA (=C*dR)": (T3 * d3, T2 * d2),
    "dA": (F(d3), F(d2)),
    "C": (C3, C2),
    "C^2": (C3 ** 2, C2 ** 2),
    "C^2*dA": (C3 ** 2 * d3, C2 ** 2 * d2),
}
prefs = [F(1), F(3, 5), F(5, 3), F(1, 2), F(2), F(3), F(1, 3)]
lo, hi = (R_obs - 2 * sig_R) / 1.7, (R_obs + 2 * sig_R) / 1.4
lo2, hi2 = (R_obs - 2 * sig_R) / S_c, (R_obs + 2 * sig_R) / S_c
tot = hit = hit2 = 0
hits = []
for sname, (w3, w2) in styles.items():
    W = {"3": w3, "2": w2, "3+2": w3 + w2}
    for num, den in itertools.permutations(W, 2):
        for p in prefs:
            r = p * W[num] / W[den]
            tot += 1
            if lo <= r <= hi:
                hit += 1; hits.append((sname, num, den, str(p), float(r)))
            if lo2 <= r <= hi2:
                hit2 += 1
print(" family size = %d ; window on R_alt (S free in [1.4,1.7]) = [%.3f, %.3f] ; landing: %d (%.1f%%)" % (tot, lo, hi, hit, 100 * hit / tot))
print(" window with S fixed at 1.59 = [%.3f, %.3f] ; landing: %d (%.1f%%)" % (lo2, hi2, hit2, 100 * hit2 / tot))
print(" lane's pick 31/9 = %.4f is %s the S-free window" % (float(Rb), "inside" if lo <= float(Rb) <= hi else "outside"))
print(" sample of alternatives that also land:", hits[:8])

prefsB = [F(1), F(3, 5), F(5, 3), F(1, 2), F(2), F(3), F(1, 3), F(3, 4), F(4, 3), F(2, 3), F(3, 2), F(4), F(1, 4), F(5, 2), F(2, 5), F(5), F(1, 5)]
totB = hitB = 0
for sname, (w3, w2) in styles.items():
    W = {"3": w3, "2": w2, "3+2": w3 + w2, "3-2": abs(w3 - w2)}
    for num, den in itertools.permutations(W, 2):
        for p in prefsB:
            r = p * W[num] / W[den]
            totB += 1
            if lo <= r <= hi: hitB += 1
print(" variant B (4 combos, 17 prefactors): family size = %d ; landing in S-free window: %d (%.1f%%)" % (totB, hitB, 100 * hitB / totB))
print(" naive log-uniform expectation for a base in [1,10]: window width = %.1f%% of a decade" % (100 * math.log10(hi / lo)))
print(" lane cascade note: alpha_GUT in [0.03,0.05] gives R in [4.8,5.3] and 'pins alpha_GUT ~ 0.048' to the observed R (S is tuned there)")

print("\n== C3  R_base = (3/5) f_vis/f_dark as the dark state's charges vary (f = C3*8 + C2*3)")
fvis = C3 * 8 + C2 * 3
for name, (c3, c2) in {"colour singlet, SU(2) doublet (lane Step 8)": (F(0), C2),
                       "colour triplet, SU(2) doublet (G1 embedding, |000>,|111>)": (C3, C2),
                       "colour triplet, SU(2) singlet": (C3, F(0)),
                       "true gauge singlet (lane Step 3)": (F(0), F(0))}.items():
    fd = c3 * 8 + c2 * 3
    print("  %-62s f_dark = %-6s R_base = %s" % (name, fd, "undefined (sigma_gauge = 0)" if fd == 0 else F(3, 5) * fvis / fd))

print("\n== summary of registered readings")
print(" (I)   FAIL by factor ~%.0e using the lane's own formula (and ~%.0e with hadronic sigma)" % (R_sym / R_pred, o_bz / o_p2 / R_pred))
print(" (IIa) needs n_DM/n_b=%.2e at 16 v (not a small rational) or m_DM ~ 5 GeV at ratio 1 -> FAIL at the lane's mass" % need_ratio)
print(" (IIb/IIc) need a new number (T_d ~ m/10; eps ~ %.0e) -> not a consequence of R_base x S" % (Y_B / dY))
