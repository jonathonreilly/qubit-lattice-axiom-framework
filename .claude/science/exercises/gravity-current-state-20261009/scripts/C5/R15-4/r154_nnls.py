"""R15-4 escape test: a NONLINEAR constrained-fit reader (outside class R+), to see whether the linear no-go is escaped on (c).

Reader C: on the past window s in [0, Sig] (Sig = 2 e-folds, 81 samples), fit rho_tot(u - s) = C + sum_j c_j e^{x_j s}
with C free (constants annihilated exactly: the weighted fit is invariant under rho_tot -> rho_tot + const), c_j >= 0,
x_j on a fixed grid in [-3, -0.05] U [0.05, 6] that contains 3 and 4, relative weights 1/rho_tot(u-s), ridge mu |c|^2.
Output rho_hat = sum_j c_j >= 0 always (real; no clamp). Phantom nodes (x<0) are read with POSITIVE density.
Tests: (i) radiation+dust exactness; (ii) S1 exact step alpha=0.5 (positivity, error); (iii) DESI DR2 CPL + matter (DESY5,
Pantheon+): rho_hat/rho_nc - 1 and the DE-part error (rho_hat - rho_m - rho_DE)/rho_DE at z = 0, 0.5, 1, 2;
(iv) continuity probe: w = -1 + eps constant DE plus matter, eps -> 0 (Lemma N0 predicts the DE is lost).
Subtraction rule: rho_nc = all non-constant content (CPL has no constant part); nothing else subtracted.
"""
import numpy as np
from scipy.optimize import nnls

Sig, ns = 2.0, 81
s = np.linspace(0, Sig, ns)
xg = np.concatenate([np.linspace(-3, -0.05, 30), np.linspace(0.05, 6, 60), [3.0, 4.0]])
B = np.exp(np.outer(s, xg))


def reader(dat, mu=1e-10):
    w = 1 / np.abs(dat)
    sw = np.sqrt(w)
    Pw = np.eye(ns) - np.outer(np.ones(ns), w) / w.sum()      # weighted centering removes the free constant exactly
    A = sw[:, None] * (Pw @ B); d = sw * (Pw @ dat)
    sc = np.max(np.abs(d))
    A2 = np.vstack([A / sc, np.sqrt(mu) * np.eye(len(xg))]); d2 = np.concatenate([d / sc, np.zeros(len(xg))])
    c, _ = nnls(A2, d2, maxiter=5000)
    return c.sum()


Om = 0.31
print('# (i) radiation + dust (R0 e^{-4u} + M0 e^{-3u}), plus a vacuum constant 1e6:')
for u in (-2.0, 0.0, 2.0):
    dat = 30 * np.exp(-4 * (u - s)) + 0.5 * np.exp(-3 * (u - s))
    rnc = dat[0]
    print(f'   u={u}: rho_hat/rho_nc - 1 = {reader(dat + 1e6)/rnc - 1:+.2e} (with vacuum 1e6), {reader(dat)/rnc - 1:+.2e} (no vacuum)')
print('# (ii) S1 exact step alpha = 0.5 at u=0 (R0=30, M0=0.5), reader at tau = u - u_T:')
for tau in (0.05, 0.2, 0.5, 1.0, 1.9, 2.5):
    uu = tau - s
    rr = np.where(uu > 0, 45.0, 30.0) * np.exp(-4 * uu) + 0.5 * np.exp(-3 * uu)
    rv = np.where(uu > 0, -15.0, 0.0)
    dat = rr + rv + 100.0
    rnc = 45 * np.exp(-4 * tau) + 0.5 * np.exp(-3 * tau)
    print(f'   tau={tau}: eps = {reader(dat)/rnc - 1:+.3e}')
print('# (iii) DESI DR2 CPL + matter')
for lab, (w0, wa) in (('DESY5', (-0.752, -0.86)), ('Pantheon+', (-0.838, -0.62)), ('Union3', (-0.667, -1.09))):
    out = []
    for z in (0.0, 0.5, 1.0, 2.0):
        u = -np.log1p(z); a = np.exp(u - s)
        rde = (1 - Om) * a ** (-3 * (1 + w0 + wa)) * np.exp(-3 * wa * (1 - a))
        rm = Om * a ** -3
        rh = reader(rm + rde + 3.0)
        out.append(f'z={z}: tot {rh/(rm[0]+rde[0]) - 1:+.3f}, DE-part {(rh - rm[0] - rde[0])/rde[0]:+.3f}')
    print(f'   {lab}: ' + '; '.join(out))
print('# (iv) continuity at w = -1 (Lemma N0): matter + constant-w DE, z = 0')
for eps in (0.3, 0.1, 0.03, 0.01, 0.003):
    a = np.exp(-s); rde = (1 - Om) * a ** (-3 * eps); rm = Om * a ** -3
    rh = reader(rm + rde)
    print(f'   1+w = {eps}: DE read fraction = {(rh - rm[0]) / rde[0]:+.3f}')
