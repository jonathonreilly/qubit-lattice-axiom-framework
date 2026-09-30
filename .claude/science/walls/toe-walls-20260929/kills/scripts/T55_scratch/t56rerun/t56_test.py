#!/usr/bin/env python3
"""T56 test suite: kernel check, Sommerfeld argument, freeze-out solve, fixed-channel table.
Author: Claude Sonnet 5.5. Same-family check, not independent referee.
"""
import numpy as np, math, json, sys
import mpmath as mp
from scipy.integrate import quad, solve_ivp
from scipy.special import kve
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

out = {}
def P(*a):
    print(*a); sys.stdout.flush()

# ---------------------------------------------------------------- constants
MPL   = 1.2209e19
GSTAR = 106.75
V_EW  = 246.28
M16V  = 16*V_EW                 # 3940.48 GeV (lane quotes 3940.53 with v=246.2831)
M16V  = 3940.53
ALPHA_LM = 0.09067
ALPHA_LO, ALPHA_HI = 0.090667836017286, 0.092264992618360
OMB_H2 = 0.02237                 # Planck 2018 (external comparator)
OMC_H2 = 0.1200
R_OBS  = OMC_H2/OMB_H2
R_BASE = 31/9

# ---------------------------------------------------------------- Sommerfeld
def S_form(eta, k):
    """k=1: pi form (lane); k=2: 2 pi form. eta = alpha/v_rel (negative = repulsive)."""
    z = k*np.pi*eta
    z = np.asarray(z, dtype=float)
    return np.where(np.abs(z) < 1e-9, 1.0, z/(-np.expm1(-z)))

def thermal_S(alpha_eff, x, k):
    """<S> over v_rel with weight v^2 exp(-x v^2/4); S argument k*pi*alpha/v."""
    a = x/4.0
    f = lambda t: float(S_form(alpha_eff*math.sqrt(a/t), k))*math.sqrt(t)*math.exp(-t)
    val = quad(f, 0, 1, limit=200)[0] + quad(f, 1, 60, limit=200)[0]
    return val*2/math.sqrt(math.pi)

# ---------------------------------------------------------------- T1: kernel reproduction (mpmath, lane's own definition)
mp.mp.dps = 30
def lane_stable_S(alpha_eff, v):
    z = mp.mpf(alpha_eff)/mp.mpf(v)
    if abs(z) < mp.mpf('1e-40'): return mp.mpf(1)
    return (mp.pi*z)/(1-mp.e**(-mp.pi*z))
def lane_avg(alpha_eff, x, attractive, k=1):
    sign = 1 if attractive else -1
    a = mp.mpf(x)/4
    kk = mp.mpf(k)
    num = lambda v: lane_stable_S(sign*kk*alpha_eff, v)*v*v*mp.e**(-a*v*v)
    den = lambda v: v*v*mp.e**(-a*v*v)
    return float(mp.quad(num,[0,1,mp.inf])/mp.quad(den,[0,1,mp.inf]))
def lane_R(alpha_s, k=1):
    s1 = lane_avg(4/3*alpha_s, 25, True, k)
    s8 = lane_avg(alpha_s/6, 25, False, k)
    return R_BASE*(8*s1+s8)/9

P("== T1 reproduction gate (lane's kernel, mpmath) ==")
r_lo = lane_R(ALPHA_LO); r_hi = lane_R(ALPHA_HI)
P(f" my R(alpha_lo)={r_lo:.6f}  lane 5.442020 ; my R(alpha_hi)={r_hi:.6f}  lane 5.482856")
t1_ok = abs(r_lo/5.442020-1) < 3e-4 and abs(r_hi/5.482856-1) < 3e-4
P(" T1 PASS" if t1_ok else " T1 FAIL")
out['T1'] = dict(R_lo=r_lo, R_hi=r_hi, pass_=bool(t1_ok))

# ---------------------------------------------------------------- T2: Sommerfeld by radial Schroedinger equation
def S_numeric(eta, rmax=4000.0):
    """mu=1, k=1, alpha=eta => eta = mu*alpha/k = alpha/v_rel (v_rel = k/mu = 1)."""
    alpha = eta; k = 1.0
    def rhs(r, y):
        u, up = y
        return [up, -(k*k + 2*alpha/r)*u]
    r0 = 1e-6
    y0 = [r0 - alpha*r0**2, 1 - 2*alpha*r0]
    sol = solve_ivp(rhs, [r0, rmax], y0, method='DOP853', rtol=1e-11, atol=1e-13, dense_output=False)
    u, up = sol.y[0][-1], sol.y[1][-1]
    kr = math.sqrt(k*k + 2*alpha/rmax)
    A2 = (u*u + (up/kr)**2)*kr/k       # asymptotic amplitude^2 (WKB-corrected)
    return 1.0/(k*k*A2)
P("\n== T2 Sommerfeld factor from the radial Schroedinger equation (eta = alpha/v_rel) ==")
rows = []
t2_ok = True
for eta in [0.05, 0.1, 0.25, 0.5, 1.0, -0.1, -0.25]:
    sn = S_numeric(eta)
    s2 = float(S_form(eta, 2)); s1 = float(S_form(eta, 1))
    rows.append(dict(eta=eta, S_num=sn, S_2pi=s2, S_pi=s1))
    P(f" eta={eta:6.2f}  S_num={sn:9.5f}  S_2pi={s2:9.5f} ({sn/s2-1:+.2%})  S_pi={s1:9.5f} ({sn/s1-1:+.2%})")
    if abs(sn/s2-1) > 0.01: t2_ok = False
    if abs(eta) >= 0.25 and abs(sn/s1-1) < 0.05: t2_ok = False
P(" T2 PASS (H2: 2 pi form is right for v_rel)" if t2_ok else " T2 FAIL")
out['T2'] = dict(rows=rows, pass_=bool(t2_ok))

# ---------------------------------------------------------------- T3: corrected kernel
P("\n== T3 R(alpha) under the lane's kernel (pi form) vs corrected kernel (2 pi form) ==")
tab = []
for al in [0.03, 0.045, 0.048, 0.05, ALPHA_LM, ALPHA_HI]:
    rl = lane_R(al, 1); rt = lane_R(al, 2)
    tab.append(dict(alpha=al, R_lane=rl, S_lane=rl/R_BASE, R_true=rt, S_true=rt/R_BASE))
    P(f" alpha={al:.5f}  lane: R={rl:.4f} S={rl/R_BASE:.3f}   corrected: R={rt:.4f} S={rt/R_BASE:.3f}")
out['T3_table'] = tab
def pin(target, k):
    return brentq(lambda a: lane_R(a, k)-target, 0.01, 0.2, xtol=1e-6)
pins = {}
for name, tg in [('Planck R=5.364', R_OBS), ('5.375', 5.375), ('5.469', 5.469), ('5.48', 5.48)]:
    pins[name] = dict(alpha_lane=pin(tg,1), alpha_true=pin(tg,2))
    P(f" alpha giving {name}: lane kernel {pins[name]['alpha_lane']:.5f}   corrected kernel {pins[name]['alpha_true']:.5f}")
out['T3_pins'] = pins
sband_true = (lane_R(0.03,2)/R_BASE, lane_R(0.05,2)/R_BASE)
sband_lane = (lane_R(0.03,1)/R_BASE, lane_R(0.05,1)/R_BASE)
P(f" S band for alpha_GUT in [0.03,0.05]: corrected {sband_true[0]:.3f}..{sband_true[1]:.3f} ; lane kernel {sband_lane[0]:.3f}..{sband_lane[1]:.3f} ; notes claim 1.4..1.7")
P3a = abs(sband_true[0]-1.4) < 0.05 and abs(sband_true[1]-1.7) < 0.06 and abs(sband_lane[0]-1.4) > 0.15
rlm_true = lane_R(ALPHA_LM,2)
P(f" R_true(alpha_LM)={rlm_true:.3f} ({rlm_true/R_OBS-1:+.1%} vs 5.364); P3a={'PASS' if P3a else 'FAIL'}")
out['T3'] = dict(S_band_true=sband_true, S_band_lane=sband_lane, P3a=bool(P3a), R_true_alphaLM=rlm_true)

# ---------------------------------------------------------------- Boltzmann solver
def yeq(x, g):
    return 45/(4*math.pi**4)*g/GSTAR*x*x*kve(2, x)*math.exp(-x)
LAM0 = math.sqrt(math.pi/45)*math.sqrt(GSTAR)*MPL    # dY/dx = -(LAM0*m*<sv>/x^2)(Y^2-Yeq^2) ; LAM0 = 0.2642*sqrt(g*)*Mpl approx
LAM0 = 0.26418*math.sqrt(GSTAR)*MPL
def omega_h2(m, sv_of_x, g, dirac, x0=4.0, x1=3000.0):
    """sv_of_x: callable x -> <sigma v> in GeV^-2 (per QQbar pair for Dirac; effective for self-conj).
    Returns Omega h^2 (both species included for Dirac)."""
    def rhs(x, y):
        Y = y[0]
        return [-(LAM0*m*sv_of_x(x)/x**2)*(Y*Y - yeq(x,g)**2)]
    y0 = [yeq(x0, g)]
    sol = solve_ivp(rhs, [x0, x1], y0, method='Radau', rtol=1e-9, atol=1e-30)
    Yinf = sol.y[0][-1]
    return 2.742e8*m*Yinf*(2.0 if dirac else 1.0), sol

# ---- lane's analytic formula for comparison
def omega_lane(m, alpha, xF=25.0, K=1.07e9):
    return K*xF*m*m/(math.sqrt(GSTAR)*MPL*math.pi*alpha**2)
P("\n== T4 freeze-out solve ==")
w_lane = omega_lane(M16V, ALPHA_LM)
sv = lambda x: math.pi*ALPHA_LM**2/M16V**2
w_num,_ = omega_h2(M16V, sv, g=2, dirac=False)
P(f" lane analytic Omega h^2 (x_F=25) = {w_lane:.4f} ; numeric solve (kappa=1, alpha_LM, self-conj, S=1) = {w_num:.4f} ({w_num/w_lane-1:+.1%})")
P4a = abs(w_num/w_lane-1) < 0.15
# degeneracy at fixed m/alpha
c = M16V/ALPHA_LM
degs = []
for mult in [8, 16, 32]:
    m = mult*V_EW; al = m/c
    svm = (lambda mm, aa: (lambda x: math.pi*aa**2/mm**2))(m, al)
    w,_ = omega_h2(m, svm, g=2, dirac=False)
    degs.append((mult, al, w))
    P(f"  m={mult:2d} v alpha={al:.4f}  Omega h^2={w:.4f}")
spread = (max(d[2] for d in degs)-min(d[2] for d in degs))/np.mean([d[2] for d in degs])
P(f" spread at fixed m/alpha = {spread:.2%}  (P4b {'PASS' if spread<0.05 else 'FAIL'})")
out['T4'] = dict(w_lane=w_lane, w_num=w_num, P4a=bool(P4a), degeneracy=degs, spread=spread)

# ---------------------------------------------------------------- running couplings
MZ = 91.1876; MT = 172.5
def run_inv(inv0, b, mu, mu0=MZ):
    return inv0 - b/(2*math.pi)*math.log(mu/mu0)      # d alpha^-1/d ln mu = -b/(2pi)
def alpha3(mu, a_mz=0.1180):
    inv = 1/a_mz
    if mu <= MT: return 1/run_inv(inv, -23/3, mu)
    inv_t = run_inv(inv, -23/3, MT)
    return 1/run_inv(inv_t, -7.0, mu, MT)
def alpha2(mu): return 1/run_inv(1/0.0338, -19/6, mu)
def alphaY(mu): return 1/run_inv(1/0.01017, 41/6, mu)
def alpha3_framework(mu):
    # framework claim alpha_s(v) = alpha_LM/u0 = 0.1033 at mu=v, run 1-loop nf=6 above m_t
    a_v = 0.1033
    inv_v = 1/a_v
    return 1/run_inv(inv_v, -7.0, mu, V_EW)
P("\n== running couplings at mu = m = 3.94 TeV ==")
for nm, f in [('alpha_s (SM MZ=0.1180)', alpha3), ('alpha_s (framework alpha_s(v)=0.1033)', alpha3_framework), ('alpha_2', alpha2), ('alpha_Y', alphaY)]:
    P(f" {nm}: mu=m/2 {f(M16V/2):.5f}  mu=m {f(M16V):.5f}  mu=2m {f(2*M16V):.5f}")
out['couplings'] = dict(a3_m=alpha3(M16V), a3fw_m=alpha3_framework(M16V), a2_m=alpha2(M16V), aY_m=alphaY(M16V),
                        a3_half=alpha3(M16V/2), a3_2m=alpha3(2*M16V))

# ---------------------------------------------------------------- Sommerfeld tables in x
XG = np.geomspace(3.0, 3000.0, 60)
def make_S_interp(alpha_eff, k=2):
    vals = np.array([thermal_S(alpha_eff, x, k) for x in XG])
    cs = CubicSpline(np.log(XG), np.log(vals))
    return lambda x: math.exp(float(cs(math.log(min(max(x, XG[0]), XG[-1])))))

NF = 6
def c1_sv(m, a3, with_ew=False, a2=None, sommerfeld=True, k=2):
    """Colour-triplet Dirac Q, colour-averaged sigma v(x) [GeV^-2]."""
    if sommerfeld:
        S1 = make_S_interp(4/3*a3, k); S8 = make_S_interp(-a3/6, k)
    else:
        S1 = S8 = (lambda x: 1.0)
    base = math.pi*a3**2/m**2
    ew = 0.0
    if with_ew:
        # SU(2) doublet vector-like Q: gauge-boson pairs 3/32, 12 left doublets x (3/16)/2, Higgs doublet 3/64;
        # colour dilution 1/N_c
        coef = 3/32 + 12*(3/16)/2 + 3/64
        ew = math.pi*a2**2/m**2*coef/3.0
    return lambda x: base*((2/27)*S1(x) + (5/27 + 2*NF/9)*S8(x)) + ew

def m_relic(builder, g, dirac, target=OMC_H2, lo=800.0, hi=20000.0):
    f = lambda lm: omega_h2(math.exp(lm), builder(math.exp(lm)), g, dirac)[0] - target
    return math.exp(brentq(f, math.log(lo), math.log(hi), xtol=1e-3))

P("\n== T5 fixed-channel table, m = 16 v ==")
rows = []
def record(name, w, extra=''):
    R = w/OMB_H2
    rows.append(dict(channel=name, omega_h2=w, ratio_to_planck=w/OMC_H2, R=R))
    P(f" {name:62s} Omega h^2={w:8.4f}  (x{w/OMC_H2:5.2f} Planck)  R={R:6.2f} {extra}")
# lane reference (numeric)
record("lane formula, kappa=1, alpha_LM, self-conj, S=1", w_num)
# C3 dark U(1): Dirac psi psibar -> gamma_D gamma_D
sv_c3 = lambda x: math.pi*ALPHA_LM**2/M16V**2
w,_ = omega_h2(M16V, sv_c3, g=2, dirac=True); record("C3a dark U(1) Dirac->2 gamma_D, alpha_LM, S=1", w)
S_c3 = make_S_interp(ALPHA_LM, 2)
sv_c3s = lambda x: math.pi*ALPHA_LM**2/M16V**2*S_c3(x)
w,_ = omega_h2(M16V, sv_c3s, g=2, dirac=True); record("C3b dark U(1) Dirac, alpha_LM, Coulomb S (2pi form)", w)
S_c3l = make_S_interp(ALPHA_LM, 1)
sv_c3l = lambda x: math.pi*ALPHA_LM**2/M16V**2*S_c3l(x)
w,_ = omega_h2(M16V, sv_c3l, g=2, dirac=True); record("C3c dark U(1) Dirac, alpha_LM, Coulomb S (lane pi form)", w)
w,_ = omega_h2(M16V, sv_c3s, g=2, dirac=False); record("C3d dark U(1) self-conj counting, alpha_LM, Coulomb S (2pi)", w)
# C1/C2 colour triplet Dirac, SM running
for mu_lab, mu in [('mu=m', M16V), ('mu=m/2', M16V/2), ('mu=2m', 2*M16V)]:
    a3 = alpha3(mu)
    svc1 = c1_sv(M16V, a3)
    w,_ = omega_h2(M16V, svc1, g=6, dirac=True); record(f"C1 colour-3 Dirac SU(3) only, alpha_s({mu_lab})={a3:.4f}, Sommerfeld", w)
a3m = alpha3(M16V); a2m = alpha2(M16V)
svc2 = c1_sv(M16V, a3m, with_ew=True, a2=a2m)
w_c2,_ = omega_h2(M16V, svc2, g=6, dirac=True); record("C2 C1 + SU(2)-doublet EW piece (mu=m)", w_c2)
w,_ = omega_h2(M16V, c1_sv(M16V, a3m, sommerfeld=False), g=6, dirac=True); record("C1 without Sommerfeld (mu=m)", w)
w,_ = omega_h2(M16V, c1_sv(M16V, a3m), g=6, dirac=False); record("C1 with self-conjugate counting (mu=m)", w)
a3fw = alpha3_framework(M16V)
w,_ = omega_h2(M16V, c1_sv(M16V, a3fw), g=6, dirac=True); record(f"C1 with framework alpha_s(v)=0.1033 run, alpha_s(m)={a3fw:.4f}", w)
w,_ = omega_h2(M16V, c1_sv(M16V, ALPHA_LM), g=6, dirac=True); record("C1 with alpha_s := alpha_LM fixed (what the lane would write)", w)
# C4 hypercharge only (Y=1/3, colour triplet): BB and ff-bar via B, colour-diluted 1/3
Y = 1/3
aY = alphaY(M16V)
coef_y = Y**4 + 5*Y**2      # gamma gamma analog + fermion pairs (3 gen, massless, Weyl sum: 5 Y^2 with Sum Y_f^2=10/3 per gen)
sv_c4 = math.pi*aY**2/M16V**2*coef_y/3.0
w,_ = omega_h2(M16V, lambda x: sv_c4, g=6, dirac=True); record("C4 U(1)_Y only, Y=1/3 (no colour force)", w)
out['T5_rows'] = rows

# required mass and required alpha
P("\n== thermal mass for Omega h^2 = 0.120 (coupling evaluated at mu = m) and needed alpha_X ==")
mr_c1 = m_relic(lambda m: c1_sv(m, alpha3(m)), 6, True)
mr_c2 = m_relic(lambda m: c1_sv(m, alpha3(m), with_ew=True, a2=alpha2(m)), 6, True)
mr_c1s = m_relic(lambda m: c1_sv(m, alpha3(m)), 6, False)
P(f" C1 Dirac : m = {mr_c1:.0f} GeV = {mr_c1/V_EW:.2f} v")
P(f" C2 Dirac : m = {mr_c2:.0f} GeV = {mr_c2/V_EW:.2f} v")
P(f" C1 self-conj counting: m = {mr_c1s:.0f} GeV = {mr_c1s/V_EW:.2f} v")
def alpha_need(dirac, S_on, k=2):
    def f(al):
        if S_on:
            Sx = make_S_interp(al, k); svx = lambda x: math.pi*al**2/M16V**2*Sx(x)
        else:
            svx = lambda x: math.pi*al**2/M16V**2
        return omega_h2(M16V, svx, 2, dirac)[0]-OMC_H2
    return brentq(f, 0.03, 0.4, xtol=1e-5)
an = {}
an['selfconj_S1'] = alpha_need(False, False)
an['dirac_S1'] = alpha_need(True, False)
an['dirac_S2pi'] = alpha_need(True, True, 2)
an['dirac_Spi'] = alpha_need(True, True, 1)
an['selfconj_S2pi'] = alpha_need(False, True, 2)
for k_,v_ in an.items(): P(f" alpha_X needed for Omega h^2=0.120 at 16 v ({k_}): {v_:.4f}  (alpha_LM=0.0907)")
out['T5_masses'] = dict(C1=mr_c1, C2=mr_c2, C1_selfconj=mr_c1s)
out['T5_alpha_needed'] = an

# R6 spread
vals = [r['omega_h2'] for r in rows if r['channel'].startswith(('C1','C2','C3','lane')) and 'framework' not in r['channel'] and 'without' not in r['channel']]
P(f"\n R6: Omega h^2 over the ambiguity set: min {min(vals):.4f} max {max(vals):.4f} ratio {max(vals)/min(vals):.2f}")
out['R6'] = dict(min=min(vals), max=max(vals), ratio=max(vals)/min(vals))
json.dump(out, open('t56_test.json','w'), indent=1, default=float)
P("done")
