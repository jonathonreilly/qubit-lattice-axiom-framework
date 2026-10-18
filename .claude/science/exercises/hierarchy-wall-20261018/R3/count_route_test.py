"""R3 count-route test (hierarchy wall, 2026-10-18).

Route 1: can a growing count N(t) (ticks, sites or records in a causal region)
set v/M_Pl?  Drift lemma: if v/M_Pl = F(N) with present elasticity
e = d ln F / d ln N, then d ln(v/M_Pl)/dt = e * d ln N/dt.  For a power law
fitted to today's value, e = ln(v/M_Pl)/ln N0.

Route 2: frozen patch capacity.  v/M_Pl = kappa * (a/R_L)^s with R_L the
asymptotic de Sitter radius.  Needed s*, and the IR scaling dimension the
order-parameter operator would need (unitarity check).

All observational numbers are comparator inputs, quoted conservatively.
"""
import math
import numpy as np
from scipy.integrate import quad

# ---------------- constants (comparator) ----------------
GeV_s = 6.582119569e-25          # hbar in GeV s
yr = 3.15576e7                   # s
M_Pl = 1.220890e19               # GeV, non-reduced; scale primitive a^-1 = M_Pl
M_Plr = 2.435e18                 # GeV, reduced (convention check only)
v = 246.22                       # GeV
m_h = 125.25
t_P = 1.0 / M_Pl * GeV_s         # s  (a = l_P, tick = a by kinetic isotropy)
H0_kms = 67.4
Mpc_km = 3.0856775814913673e19
H0 = H0_kms / Mpc_km             # s^-1
Om, Orad = 0.315, 9.15e-5
OL = 1.0 - Om - Orad

def H(a):  # s^-1
    return H0 * math.sqrt(Orad / a**4 + Om / a**3 + OL)

# ---- tabulated background on a log grid (trapezoid in ln a) ----
lna = np.linspace(math.log(1e-30), math.log(1.0), 400001)
A = np.exp(lna)
Hs = H0 * np.sqrt(Orad / A**4 + Om / A**3 + OL)
def cumtrap(y, x):
    out = np.zeros_like(y)
    out[1:] = np.cumsum(0.5 * (y[1:] + y[:-1]) * np.diff(x))
    return out
a_min = A[0]
t_arr = cumtrap(1.0 / Hs, lna) + 1.0 / (2 * H0 * math.sqrt(Orad)) * a_min**2        # radiation-era start t = a^2/(2 H0 sqrt(Or))
chi_arr = cumtrap(1.0 / (A * Hs), lna) + a_min / (H0 * math.sqrt(Orad))            # chi = a/(H0 sqrt(Or)) at start

def idx(a):
    return int(np.argmin(np.abs(lna - math.log(a))))

def t_of_a(a):
    return float(np.interp(math.log(a), lna, t_arr))

def chi_of_a(a):
    return float(np.interp(math.log(a), lna, chi_arr))

t0 = t_of_a(1.0)
chi0 = chi_of_a(1.0)

def V4_and_rate(a_obs):
    """Proper 4-volume of the causal past of an observer at a_obs (s^4) and d ln V4/dt_obs (1/s)."""
    i = idx(a_obs)
    chi_obs = chi_arr[i]
    w = (A[:i+1]**3) * (chi_obs - chi_arr[:i+1])
    dt_dlna = 1.0 / Hs[:i+1]
    V4 = float(np.trapezoid(w**1 * (chi_obs - chi_arr[:i+1])**2 * (4*math.pi/3) * dt_dlna, lna[:i+1]))
    I2 = float(np.trapezoid((A[:i+1]**3) * (chi_obs - chi_arr[:i+1])**2 * dt_dlna, lna[:i+1]))
    return V4, (4 * math.pi / A[i]) * I2 / V4

def counts(a):
    """returns {name: (N, dlnN/dt [1/s])}"""
    t = t_of_a(a); chi = chi_of_a(a); h = math.sqrt(Orad / a**4 + Om / a**3 + OL) * H0
    d_p = a * chi; R_H = 1.0 / h
    dH_da = H0 * 0.5 / math.sqrt(Orad / a**4 + Om / a**3 + OL) * (-4 * Orad / a**5 - 3 * Om / a**4)
    V4, rV4 = V4_and_rate(a)
    return {
        "N_age  (ticks t/t_P)": (t / t_P, 1.0 / t),
        "N_vol  (sites in particle horizon)": ((4 * math.pi / 3) * (d_p / t_P) ** 3, 3 * (h + 1.0 / d_p)),
        "N_area (Hubble-horizon area/4, Planck units)": (math.pi * (R_H / t_P) ** 2, -2 * a * dH_da),
        "N_V4   (events in causal past)": (V4 / t_P ** 4, rV4),
    }

ln_hier = math.log(M_Pl / v)
print("=== constants ===")
print(f"t0 = {t0/yr/1e9:.4f} Gyr ; ln(M_Pl/v) = {ln_hier:.4f} ; v/M_Pl = {v/M_Pl:.4e}")

# comparator bounds (conservative)
eps_clock = 1.0e-16      # |d ln mu/dt| per yr  (Yb+/Cs clocks give (-8 +- 36)e-18; take 1e-16)
eps_LLR = 1.5e-13        # |d ln G/dt| per yr in atomic units (LLR, conservative)
# sensitivity of observables to d ln v with Planck-scale couplings held fixed:
# Lambda_QCD^(3) ∝ Lambda_6^(7/9) (m_t m_b m_c)^(2/27)  ->  d ln Lambda_QCD / d ln v = 2/9
sens_mu = 2.0 / 9.0 - 1.0          # d ln(m_p/m_e)/d ln v
sens_G = 2.0 * (2.0 / 9.0)         # d ln(G m_p^2)/d ln v   (atomic-units G-dot proxy)

a_list = {"today": 1.0, "recombination z=1090": 1 / 1091.0}
# BBN epoch: n/p freeze-out near T ~ 1 MeV, t ~ 1 s
def a_at_t(t_target):
    lo, hi = 1e-16, 1.0
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if t_of_a(mid) < t_target:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)
a_bbn = a_at_t(1.0)
a_list["BBN t=1 s"] = a_bbn

c0 = counts(1.0)
c_rec = counts(1 / 1091.0)
c_bbn = counts(a_bbn)
print("\n=== Route 1: running counts, power law fitted to today ===")
hdr = f"{'count':46s} {'log10 N0':>9s} {'dlnN/dt [1/yr]':>15s} {'e=ln(v/M)/lnN0':>15s} {'dln v/dt [1/yr]':>16s} {'clock excess':>13s} {'LLR excess':>11s} {'v_rec/v0':>10s} {'v_BBN/v0':>10s} {'e_max(clock)':>13s}"
print(hdr)
rows = []
for k in c0:
    N0 = c0[k][0]
    dlnN_dt = c0[k][1] * yr
    e = -ln_hier / math.log(N0)                      # d ln(v/M)/d ln N
    drift = e * dlnN_dt
    clock_excess = abs(sens_mu * drift) / eps_clock
    llr_excess = abs(sens_G * drift) / eps_LLR
    v_rec = math.exp(e * (math.log(c_rec[k][0]) - math.log(N0)))
    v_bbn = math.exp(e * (math.log(c_bbn[k][0]) - math.log(N0)))
    e_max = eps_clock / abs(sens_mu) / dlnN_dt
    rows.append((k, N0, dlnN_dt, e, drift, clock_excess, llr_excess, v_rec, v_bbn, e_max))
    print(f"{k:46s} {math.log10(N0):9.2f} {dlnN_dt:15.3e} {e:15.4f} {drift:16.3e} {clock_excess:13.2e} {llr_excess:11.2e} {v_rec:10.3e} {v_bbn:10.3e} {e_max:13.2e}")

print("\nComparator bounds used: |dln mu/dt| < 1e-16/yr (clocks), |dln G/dt| < 1.5e-13/yr (LLR),")
print("|dv/v| < 0.1 at BBN and < 0.03 at recombination (conservative).")

# exponent-independence identity for pure power-law growth N ∝ t^k with N(t_P) = 1:
ident = ln_hier / (t0 / yr * math.log(t0 / t_P))
print(f"\nIdentity check (N ∝ t^k, N(t_P)=1, any k, any p): |dln v/dt| = ln(M/v)/(t0 ln(t0/t_P)) = {ident:.3e} /yr")

# share of the log-hierarchy a count could carry today if its elasticity were held at e_max over its whole growth
print("\nMax share of ln(M_Pl/v) a count may carry with present elasticity <= e_max (if e were constant):")
for r in rows:
    share = r[9] * math.log(r[1]) / ln_hier
    print(f"  {r[0]:46s} share <= {share:.2e}")

# ---------------- self-consistent freezing lemma ----------------
print("\n=== Frozen count set at the epoch fixed by v itself (radiation era) ===")
print("N(T*) = c (M_Pl/T*)^k, T* = c' v, v/M_Pl = N^-p  ->  (v/M_Pl)^(1-kp) = c^-p c'^(kp)")
for (k, p, c, cp_) in [(2, 0.2, 1.0, 1.0), (3, 0.2, 10.0, 0.1), (6, 0.1, 100.0, 0.3), (2, 0.49, 3.0, 1.0), (3, 0.33, 2.0, 1.0)]:
    if abs(1 - k * p) < 1e-12:
        print(f"  k={k} p={p}: degenerate (any v)")
        continue
    lnr = (-p * math.log(c) + k * p * math.log(cp_)) / (1 - k * p)
    print(f"  k={k} p={p:.2f} c={c} c'={cp_}: v/M_Pl = {math.exp(lnr):.3e}   (needs 1-kp ~ O(1)/38 for 1e-17)")

# ---------------- Route 2: frozen patch capacity ----------------
print("\n=== Route 2: asymptotic de Sitter capacity (time independent) ===")
H_L = H0 * math.sqrt(OL)                     # s^-1
H_L_GeV = H_L * GeV_s
R_over_a = M_Pl / H_L_GeV
N_L = math.pi * R_over_a ** 2                # S_dS = pi M_Pl^2 / H^2
N_sites_S3 = 2 * math.pi ** 2 * R_over_a ** 3
print(f"R_L/a = {R_over_a:.4e} (log10 {math.log10(R_over_a):.3f});  N_L = S_dS = {N_L:.3e};  sites on S^3_R: {N_sites_S3:.3e}")
for (lab, MP, vv) in [("M_Pl, v", M_Pl, v), ("M_Pl, m_h", M_Pl, m_h), ("reduced M_Pl, v", M_Plr, v), ("reduced M_Pl, m_h", M_Plr, m_h)]:
    Ra = MP / H_L_GeV
    s_star = math.log(MP / vv) / math.log(Ra)
    kappa = (vv / MP) / (1 / Ra) ** 0.25
    pN = math.log(MP / vv) / math.log(math.pi * Ra ** 2)
    print(f"  [{lab:18s}] s* = ln(M/v)/ln(R/a) = {s_star:.4f} ; p* vs S_dS = {pN:.4f} (1/8 = 0.125) ; kappa for s=1/4: {kappa:.3f}")
s_star = math.log(M_Pl / v) / math.log(R_over_a)
print("\nLocal finite-size mechanism: <O>_L ~ a^-dO (a/L)^Delta  =>  v ~ a^-1 (a/L)^(Delta/dO); need Delta = dO * s*")
for dO in [1, 2, 3, 4, 6]:
    Delta = dO * s_star
    ok4 = "allowed (4D, Delta>=1)" if Delta >= 1 else "VIOLATES 4D scalar unitarity bound Delta>=1"
    print(f"  dO={dO}: Delta needed = {Delta:.3f}  -> {ok4}")

# what the 1/4-law predicts for Lambda given v (comparator only)
rhoL_obs = 3 * H_L_GeV ** 2 * M_Pl ** 2 / (8 * math.pi)   # GeV^4
pred_HL = (v ** 4 / M_Pl ** 3)                              # kappa = 1, s = 1/4
print(f"\nkappa=1, s=1/4 would give H_L = v^4/M_Pl^3 = {pred_HL:.3e} GeV vs observed {H_L_GeV:.3e} GeV (ratio {pred_HL/H_L_GeV:.3e})")
print(f"rho_L^(1/4) observed = {rhoL_obs**0.25*1e12:.3f} meV ; v^2/M_Pl = {v**2/M_Pl*1e12:.3f} meV ; v^2/M_Pl_red = {v**2/M_Plr*1e12:.3f} meV")

# ---------------- species-bound bookkeeping ----------------
print("\n=== Species bound (Dvali form M_Pl^2 >= N Lambda^2) ===")
print(f"N needed for gravity cutoff at v: (M_Pl/v)^2 = {(M_Pl/v)**2:.3e};  (M_Pl_red/v)^2 = {(M_Plr/v)**2:.3e}")
print("Free nearest-neighbour rule, one 2-dim site per cell on Z^3 x Z_tau: zero-mode doublers <= 2^4 per band, <= 2 bands -> <= 32")
print(f"Enlarged cell needed to host N light species from one band each: >= {(M_Pl/v)**2/2:.2e} sites, linear size >= {((M_Pl/v)**2/2)**(1/3):.2e} a")
