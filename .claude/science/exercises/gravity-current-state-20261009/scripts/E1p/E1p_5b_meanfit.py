"""Fit the exact finite-density 4D mean to a continuum form with a renormalized mass and amplitude:
Kbar(tau) ~ -Z (M/(4 pi tau)) J1(M tau) over m tau in [2, mtmax]; report M/m - 1, Z, residual/envelope;
and check for exponential growth of |Kbar|/envelope."""
import numpy as np
from scipy.special import j1
from scipy.optimize import least_squares
for ml in [0.05, 0.1, 0.2, 0.4, 0.7]:
    d = np.load(f"../out/mean4d_ml{ml}.npz"); t = d["taus"]; K = d["K"]; m = float(d["m"])
    sel = m * t > 2
    env = (m / (4 * np.pi * t[sel])) * np.sqrt(2 / (np.pi * m * t[sel]))
    def res(p):
        Z, M = p
        return (K[sel] + Z * (M / (4 * np.pi * t[sel])) * j1(M * t[sel])) / env
    fit = least_squares(res, [1.0, m])
    Z, M = fit.x
    r = res(fit.x)
    # growth: max |K|/env in successive windows of m tau
    mt = m * t[sel]; ratio = np.abs(K[sel]) / env
    wins = [(2, 5), (5, 8), (8, 11), (11, 14), (14, 17), (17, 20)]
    g = [f"{ratio[(mt>=a)&(mt<b)].max():.3f}" if np.any((mt>=a)&(mt<b)) else "-" for a, b in wins]
    print(f"m*ell={ml}: fitted M/m-1 = {M/m-1:+.4f}, Z = {Z:.4f}, max|resid|/env = {np.abs(r).max():.4f};  max|Kbar|/env per m tau window {wins}: {g}")
