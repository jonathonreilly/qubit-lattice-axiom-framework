"""R18-2 extras: (e1) lattice-independent lower bound on Lambda_tilde from the EFT-valid field range;
(e2) the singlet benchmark's two-field RG-improved potential on a grid (global-minimum check);
(e3) vector-like 5-plet boundary: largest M_F that stabilizes, per n5, at M_t central and +2 sigma_exp.
Inputs RECALLED (PREREG.md)."""
import numpy as np
from scipy.optimize import brentq
from smrge import run, lam_eff, MP

RHO_L = 2.5e-47
Mt0, Mh0, as0 = 172.57, 125.20, 0.1180

print("e1. Variational bound: the 1PI effective potential is the minimum energy density at fixed <h>, so e0 <= V_eff(h)")
print("    for every h where V_eff is valid. Restricting to h a <= 1e-3 (lattice corrections O((h a)^2) <= 1e-6 relative):")
T, Y = run(Mt0, Mh0, as0, mu_max=MP * 1.01, npts=3000)
le, _ = lam_eff(T, Y)
h = np.exp(T)
for hcut_a in [1e-3, 1e-5, 1e-7]:
    m = (h >= 1e3) & (h <= hcut_a * MP)
    V = le[m] * h[m]**4 / 4
    j = np.argmin(V)
    print("    h <= %.0e/a = %.2e GeV: min V_eff = %+.3e GeV^4 at h = %.2e -> Lambda_tilde >= %.2e rho_Lambda" % (
        hcut_a, hcut_a * MP, V[j], h[m][j], max(-V[j], 0) / RHO_L))
for Mt in [171.5, 172.0]:
    T2, Y2 = run(Mt, Mh0, as0, mu_max=MP * 1.01, npts=3000)
    le2, _ = lam_eff(T2, Y2)
    h2 = np.exp(T2)
    m = (h2 >= 1e3) & (h2 <= 1e-3 * MP)
    V = le2[m] * h2[m]**4 / 4
    print("    (M_t = %.1f: same bound with h a <= 1e-3 gives Lambda_tilde >= %.2e rho_Lambda)" % (Mt, max(-V.min(), 0) / RHO_L))

print()
print("e2. Singlet benchmark m_S = 1e7 GeV, lS = 0.2, lHS = +0.25: RG-improved two-field quartic potential")
mS, lS0, lHS0 = 1e7, 0.2, 0.25
w = mS / np.sqrt(2 * lS0)
T, Y = run(Mt0, Mh0, as0, mu_max=MP * 1.01, singlet=dict(mS=mS, lS=lS0, lHS=lHS0), npts=2000)
v = 246.22
worst = np.inf
hs = np.logspace(2, np.log10(MP), 140)
ss = np.concatenate([[0.0], np.logspace(2, np.log10(MP), 140)])
for hh in hs:
    for s in ss:
        mu = max(hh, s, mS)
        t = np.log(mu)
        lH, lHS, lS = (np.interp(t, T, Y[k]) for k in (4, 5, 6))
        X = hh**2 / 2 - v**2 / 2
        Yv = s**2 - w**2
        V = lH * X**2 + lS / 4 * Yv**2 + lHS / 2 * X * Yv
        scale = (hh**2 + s**2 + w**2)**2
        worst = min(worst, V / scale)
print("    w = %.3e GeV; min over grid (h, s up to M_P) of V/(h^2+s^2+w^2)^2 = %+.3e  (>= 0 means (v, w) is the global minimum, V(v,w) = 0)" % (w, worst))
print("    tree-level positive-definiteness at m_S: 4 lH lS - lHS^2 = %.4f (> 0)" % (
    4 * np.interp(np.log(mS) + 1e-6, T, Y[4]) * lS0 - lHS0**2))
print("    note: tree-level Higgs-singlet mixing ~ lHS v/(2 lS w) = %.1e (negligible for M_h matching)" % (lHS0 * v / (2 * lS0 * w)))

print()
print("e3. Vector-like Dirac 5-plets (no Yukawa): largest M_F with min lambda_eff > 0 up to M_P and g_i(M_P) < 3")


def minle(MF, n5, Mt):
    T, Y = run(Mt, Mh0, as0, mu_max=MP * 1.01, n5=n5, MF=MF, npts=700)
    h = np.exp(T)
    le, _ = lam_eff(T, Y)
    m = (h >= 1e3) & (h <= MP)
    pert = np.abs(Y[:3, m]).max() < 3.0
    return le[m].min(), pert


for Mt in [Mt0, Mt0 + 2 * 0.29]:
    for n5 in [1, 2, 3, 4, 6, 8]:
        f = lambda lg: minle(10**lg, n5, Mt)[0]
        lo, hi = 3.0, 12.0
        if f(lo) <= 0:
            print("    M_t = %.2f, n5 = %d: not stable even at M_F = 1 TeV (min lambda_eff = %+.4f)" % (Mt, n5, f(lo)))
            continue
        if f(hi) > 0:
            mf = hi
        else:
            mf = brentq(f, lo, hi, xtol=1e-3)
        pert = minle(1e3, n5, Mt)[1]
        print("    M_t = %.2f, n5 = %d (db_i = %.2f): stable for M_F <= %.2e GeV ; perturbative to M_P at M_F = 1 TeV: %s" % (
            Mt, n5, 2 * n5 / 3, 10**mf, pert))
