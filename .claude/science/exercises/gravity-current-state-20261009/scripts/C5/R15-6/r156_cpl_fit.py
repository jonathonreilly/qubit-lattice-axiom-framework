"""R15-6 step 4b: a family-matched reader on the DESI-like history (dust + CPL DE + any constant vacuum).
FM reader: at each u, solve the 4 derivative equations d_j rho_tot/du^j (j = 1..4) for (Om, A, w0, wa) of the family
rho_nc = Om e^{-3u} + A e^{-3(1+w0+wa)u} exp(-3 wa (1 - e^u)), continuation from the previous solution
(first point: start 10% off the truth).  Uses only derivatives -> annihilates constants; causal (local in u).
Then R = rho_nc(fitted), g/H^2 = V'/R.  Also a mismatch test: true history = dust + radiation + CPL, reader without radiation.
"""
import numpy as np, sympy as sp
from scipy.optimize import least_squares
u = sp.symbols('u'); P = sp.symbols('Om A w0 wa')
fam = P[0]*sp.exp(-3*u) + P[1]*sp.exp(-3*(1+P[2]+P[3])*u)*sp.exp(-3*P[3]*(1-sp.exp(u)))
famd = [sp.lambdify((u,)+P, sp.diff(fam, u, j), 'numpy') for j in range(5)]
def truth(Orad):
    rho = 0.3*sp.exp(-3*u) + Orad*sp.exp(-4*u) + 0.7*sp.exp(-3*(1-0.75-0.86)*u)*sp.exp(-3*(-0.86)*(1-sp.exp(u)))
    return [sp.lambdify(u, sp.diff(rho, u, j), 'numpy') for j in range(5)]
def run(Orad, label):
    tr = truth(Orad)
    us = np.linspace(np.log(0.1), 0.0, 1501)
    p = np.array([0.33, 0.77, -0.80, -0.80]); Rs = []; res = []
    for x in us:
        dt = np.array([tr[j](x) for j in range(1, 5)])
        fun = lambda q: (np.array([famd[j](x, *q) for j in range(1, 5)]) - dt)/np.abs(dt)
        s = least_squares(fun, p, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=2000)
        p = s.x; Rs.append(famd[0](x, *p)); res.append(np.max(np.abs(s.fun)))
    Rs = np.array(Rs); rnc = tr[0](us)
    V = rnc - Rs; gH2 = np.gradient(V, us)/Rs; eps = Rs/rnc - 1
    print(f"[{label}] final params (Om, A, w0, wa) = {np.round(p, 6)}; max fit residual = {max(res):.1e}")
    for aa in (1.0, 0.5, 0.25, 0.1):
        i = np.argmin(np.abs(us - np.log(aa)))
        print(f"   a={aa}: eps = {eps[i]:+.3e}, g/H^2 = {gH2[i]:+.3e}")
    print(f"   over 0.1<a<1: g/H^2 in [{gH2.min():+.3e}, {gH2.max():+.3e}], max|eps| = {np.max(np.abs(eps)):.3e}")
run(0.0, "FM on its own family (dust + CPL)")
run(9e-5, "FM with unmodelled radiation Omega_r = 9e-5")
