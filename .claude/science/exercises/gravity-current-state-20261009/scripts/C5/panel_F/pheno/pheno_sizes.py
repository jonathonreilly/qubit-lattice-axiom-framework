"""Panel F, pheno lens: order-of-magnitude checks. Pure arithmetic, no repo edits.
Inputs: repo numbers (cited in statement.md) + external numbers (WEB/RECALLED, labelled in statement.md)."""
import numpy as np

hbar_c = 1.97327e-7      # eV m
hbar = 6.582120e-16      # eV s
c = 2.99792458e8
lP = 1.616e-35           # m (repo's a; non-reduced Planck length)
EP = 1.22089e28          # eV = hbar c / lP (repo's E_P)
G = 6.674e-11
me, mN, mp = 0.51100e6, 9.389e8, 9.3827e8
yr = 3.156e7

print("== A. sizes: fermion vs grid (a = lP) ==")
print("hbar c / lP = %.4e eV (repo uses %.4e)" % (hbar_c / lP, EP))
for lab, m in (("electron", me), ("u quark ~2.2 MeV", 2.2e6), ("proton", mp), ("top 172.7 GeV", 1.727e11)):
    lam = hbar_c / m
    print("  %-18s reduced Compton %.3e m = %.2e sites;  m*a = %.2e (lattice units)" % (lab, lam, lam / lP, m / EP))
rp = 0.8409e-15
print("  proton charge radius 0.8409 fm = %.2e sites; sites inside ~ %.1e" % (rp / lP, 4 / 3 * np.pi * (rp / lP) ** 3))
print("  electron point-like to <~1e-18..1e-20 m: still >= %.0e sites" % (1e-20 / lP))

print("\n== B. why the grid gives mass: sizes on the root edge ==")
dm0 = 0.041858390        # delta m per e^2, t = 0 (F1 = R19-34)
Wpi = 0.3552035823       # D1(0.909103708, 0.555604226) W(pi) per axis (computed here from dirac.py)
for lab, g2 in (("electron, e^2 ~ 0.1", 0.1), ("quark, C_F g_s^2 ~ 0.4", 4 / 3 * 0.3)):
    x = g2 * dm0
    print("  additive shift %-24s = %.2e /a = %.2e eV = %.1e x m_e;  fraction of E_P %.1e" % (lab, x, x * EP, x * EP / me, x))
print("  doublers: corner masses n*W(pi) = %.3f, %.3f, %.3f /a = %.2e .. %.2e eV" % (Wpi, 2 * Wpi, 3 * Wpi, Wpi * EP, 3 * Wpi * EP))
print("  fine tuning of critical mass for electron: m_e a / (0.1*dm0) = %.1e" % ((me / EP) / (0.1 * dm0)))

print("\n== C. re-derive Earth |m_g| and the 1.6e8 ==")
HessT = 2.42401e-2       # SF units t, per e^2 (F1, refereed U=1 Psym branch)
ch = 4 * HessT           # H-cov units
wN = 13 * (4 / 3) * 0.3  # nucleon weight (r1934_sizes.py)
n = 3.3e30               # nucleons / m^3 at 5500 kg/m^3
mg2a2 = 16 * np.pi * n * lP ** 3 * wN * ch / 4
mg = np.sqrt(mg2a2) * EP
muR = mg ** 2 / 5500.0
print("  |m_g|(Earth) = %.3e eV ; mu_rho = %.3e eV^2 m^3/kg ; / 1.5e-29 = %.2e" % (mg, muR, muR / 1.5e-29))
print("  decay length hbar c/m_g = %.0f m vs chords 9.3e6..1.13e7 m -> exponent ~ %.1e" % (hbar_c / mg, 1.0e7 / (hbar_c / mg)))
for f in (20.0, 30.0, 100.0):
    w = 2 * np.pi * hbar * f
    print("  graviton energy at %5.0f Hz = %.2e eV ; m_g/omega = %.1e" % (f, w, mg / w))
# crude independent bound: m_g(core) < omega(20 Hz)
w20 = 2 * np.pi * hbar * 20.0
print("  crude 'no evanescence at 20 Hz in core (rho~1.1e4)': mu_rho < %.1e (F2 1D exact: 1.5e-29)" % (w20 ** 2 / 1.1e4))
muGR = 16 * np.pi * G * hbar ** 2   # 16 pi G rho / rho in eV^2 m^3/kg  (16 pi G rho has units 1/s^2)
print("  gravitational-strength reference 16piG (eV^2 m^3/kg) = %.2e ; SF channel / GR-strength = %.1e" % (muGR, muR / muGR))
print("  m_g^2 / (16 pi G rho) check = %.2e (expect (w c_h/4) E_P / m_N = %.2e)" % (muR / muGR, wN * ch / 4 * EP / mN))

print("\n== D. matter side of the same term: rest-mass shift in a strain t (t = GW strain amplitude) ==")
d2e = 0.1 * HessT * EP   # eV per t^2 (second derivative)
d2N = wN * HessT * EP
print("  dm_e = %.2e eV * t^2 ; dm_N = %.2e eV * t^2 ; per-mass: e %.2e, N %.2e" % (d2e / 2, d2N / 2, d2e / 2 / me, d2N / 2 / mN))
print("  strain at which dm_e = m_e: t = %.2e (Earth surface potential 7e-10, Sun at 1 AU 9.9e-9)" % np.sqrt(me / (d2e / 2)))
# nanohertz GW background (NANOGrav 15 yr: A = 2.4e-15 at 1/yr, h_c ~ f^-2/3), WEB
A, fyr = 2.4e-15, 1 / yr
for f0 in (1 / (16 * yr), 1 / (30 * yr)):
    fs = np.logspace(np.log10(f0), np.log10(1e-7), 4000)
    hc2 = (A * (fs / fyr) ** (-2 / 3)) ** 2
    t2 = np.trapezoid(hc2 / fs, fs)
    # drift over a ~5 yr window: use modes with f < 1/(5 yr) for tdot (slow), times t_rms
    sel = fs < 1 / (5 * yr)
    tdot2 = np.trapezoid(((2 * np.pi * fs) ** 2 * hc2 / fs)[sel], fs[sel])
    rate_t2 = 2 * np.sqrt(t2) * np.sqrt(tdot2) * yr   # d(t^2)/dt per yr, rms
    rate_e = d2e / 2 * rate_t2 / me
    rate_N = d2N / 2 * rate_t2 / mN
    dlnmu = abs(rate_N - rate_e)
    print("  f_min = %.1e Hz: t_rms = %.1e ; d(t^2)/dt ~ %.1e /yr ; d ln(m_e)/dt ~ %.1e /yr ; d ln(mp/me)/dt ~ %.1e /yr ; / 3.6e-17 = %.0e"
          % (f0, np.sqrt(t2), rate_t2, rate_e, dlnmu, dlnmu / 3.6e-17))
    # EP: composition-dependent part of -grad(dm)/m ; grad t ~ (2 pi f/c) t
    k_eff = 2 * np.pi * f0 / c
    a_univ = d2N * t2 * k_eff / mN * c ** 2     # m/s^2 (dm'' t grad t / m)
    print("     universal strain acceleration ~ %.1e m/s^2 ; composition part (2e-3) ~ %.1e m/s^2 vs Eot-Wash space-fixed 8.8e-15 -> %.0e"
          % (a_univ, 2e-3 * a_univ, 2e-3 * a_univ / 8.8e-15))
print("  LIGO-band GW (t ~ 1e-21): dm_e/m_e = %.1e (invisible)" % (d2e / 2 * 1e-42 / me))

print("\n== E. multiplicative residual (not covered by P-R19-34a), per nucleon ==")
zpp = 0.0717             # |z''| per e^2, H-cov (R19-34, Wilson root, m-linear) -- not computed under SF
sum_mqq = 0.28e9         # eV: sum_q m_q <N|qbar q|N> ~ sigma_piN + sigma_s + 3 heavy (RECALLED, ~0.3 m_N)
mu_mult_per_N = sum_mqq / EP * (4 / 3 * 0.3) * zpp / 4
mu_add_per_N = wN * ch / 4
ratio = mu_mult_per_N / mu_add_per_N
mu_mult = muR * ratio
print("  mult/add = %.1e ; mu_rho(mult) = %.1e eV^2 m^3/kg ; Earth row 1.5e-29 -> passes by %.0e ; F2 toy pulsar 2e-43 -> x%.0f ; vs 16piG: %.1e"
      % (ratio, mu_mult, 1.5e-29 / mu_mult, mu_mult / 2e-43, mu_mult / muGR))

print("\n== F. scalar (Higgs) mass^2 channel, matter side (ESTIMATE) ==")
d2Sig = 0.53             # |d2_h Sigma(P=0)| per e^2 in a^-2, lattice scalar QED, H-cov (R19-31 table)
g2 = 0.4                 # SU(2)-ish coupling at the lattice scale (RECALLED, estimate)
mH = 125.1e9
for lab, conv in (("h units", 1.0), ("t units (/4)", 0.25)):
    dmH2 = 0.5 * d2Sig * g2 * conv * EP ** 2   # eV^2 per strain^2
    dv = 0.5 * dmH2 / mH ** 2
    print("  %-14s delta m_H^2 = %.1e eV^2 * s^2 ; delta v / v ~ %.1e * s^2 ; at s^2 = 1e-28 (GWB): %.0e ; at 1e-42 (LIGO): %.0e"
          % (lab, dmH2, dv, dv * 1e-28, dv * 1e-42))

print("\n== G. tolerances the rule must meet (fraction of F1's Hessian left over) ==")
print("  GW170817 Earth crossing (graviton side): %.0e" % (1 / 1.616e8))
print("  vacuum knock-on: vacuum m_g < ~1.9e-23 eV -> m_g^2 a^2 < %.0e (absorbed only if (Sigma) holds to that level)" % ((1.9e-23 / EP) ** 2))
