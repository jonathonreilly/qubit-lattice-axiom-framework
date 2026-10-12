"""R3-1 check 3: per-realization Lorentz violation in a Gamma_L-invariant orbit sum (in the tube).

Realization = L7 itself (g = 1, u = 0). Shell N = -3 (timelike, tau = sqrt3), future sheet n0 >= 1.
For a future unit timelike u and kappa > 0 (p = i kappa u, inside the forward tube), the
retarded/advanced orbit sum   S(u, kappa) = sum_{x in shell, x0>0} exp(-kappa w),  w = -u.x = u0 x0 - u.x
is absolutely convergent and exactly Gamma_L-invariant in u.  If the shell's points were exactly
equidistributed on H^3 (continuum Lorentz-invariant kernel), S would equal
      S_LI(kappa) = nu * 4 pi K1(kappa tau)/(kappa tau),   nu = point density per unit hyperbolic volume,
independent of u.  The u-dependence of S/S_LI is the per-realization Lorentz violation of this
(non-polynomial) term.  Prediction (spectral expansion on Gamma\\H^3, tempered spectrum):
      rms_u (S/S_LI - 1)  ~ C * (kappa tau)^1   as kappa -> 0  (relative), i.e. absolute ~ 1/kappa.
"""
import numpy as np
from scipy.special import k1

N = -3
tau = np.sqrt(3.0)
n0max = 760
Mmax = 7 * n0max ** 2 + 10
R2 = int(np.sqrt(Mmax)) + 1
a = np.arange(-R2, R2 + 1, dtype=np.int32)
A, Bb = np.meshgrid(a, a, indexing="ij")
V = (A * A + Bb * Bb).ravel()
keep = V <= Mmax
V, A, Bb = V[keep], A.ravel()[keep], Bb.ravel()[keep]
order = np.argsort(V, kind="stable")
V, A, Bb = V[order], A[order].astype(np.int32), Bb[order].astype(np.int32)
print("two-square index built:", len(V), "pairs")

X0, X1, X2, X3 = [], [], [], []
for n0 in range(1, n0max + 1):
    m = 7 * n0 * n0 + N
    n1 = np.arange(-int(np.sqrt(m)), int(np.sqrt(m)) + 1)
    v = m - n1 * n1
    lo = np.searchsorted(V, v, "left"); hi = np.searchsorted(V, v, "right")
    c = hi - lo
    if c.sum() == 0: continue
    idx = np.concatenate([np.arange(l, h) for l, h in zip(lo[c > 0], hi[c > 0])])
    X0.append(np.full(len(idx), n0, dtype=np.int32))
    X1.append(np.repeat(n1[c > 0], c[c > 0]).astype(np.int32))
    X2.append(A[idx]); X3.append(Bb[idx])
X0 = np.sqrt(7.0) * np.concatenate(X0); X1 = np.concatenate(X1).astype(float)
X2 = np.concatenate(X2).astype(float); X3 = np.concatenate(X3).astype(float)
assert np.allclose(-X0**2 + X1**2 + X2**2 + X3**2, N)
npts = len(X0)
Xmax = np.sqrt(7.0) * n0max
print("future-sheet points with n0 <=", n0max, ":", npts, "; x0max =", round(Xmax, 1))

# density per unit hyperbolic volume, from counting in the e0 frame (|x|_E^2 = tau^2 cosh 2r)
TE = np.sqrt(X0**2 + X1**2 + X2**2 + X3**2)
Tcut = Xmax  # all points with |x|_E <= Xmax have x0 <= Xmax
Rcut = 0.5 * np.arccosh(Tcut**2 / tau**2)
vol = np.pi * (np.sinh(2 * Rcut) - 2 * Rcut)   # hyperbolic ball volume in H^3
nu = (TE <= Tcut).sum() / vol
print(f"nu (points per unit hyperbolic volume) = {nu:.6f}  [N(T)/T^2 method predicts 0.39318*tau^2/pi*... ]")

def S(u, kap):
    w = u[0] * X0 - (u[1] * X1 + u[2] * X2 + u[3] * X3)
    return np.exp(-kap * w).sum(), (kap * np.exp(-1.0) * Xmax)  # second: truncation exponent margin (rap<=1)

def boost(r, nhat):
    nhat = np.asarray(nhat, float); nhat /= np.linalg.norm(nhat)
    return np.array([np.cosh(r), *(np.sinh(r) * nhat)])

rng = np.random.default_rng(7)
us = [boost(rng.uniform(0, 1.0) ** (1/3) * 1.0, rng.normal(size=3)) for _ in range(32)]
kaps = [0.8, 0.4, 0.2, 0.1, 0.07, 0.05]
print("\nkappa | margin kappa*e^-1*x0max | mean_u S/S_LI | rms_u(S/S_LI - 1) | max-min")
rows = []
for kap in kaps:
    SLI = nu * 4 * np.pi * k1(kap * tau) / (kap * tau)
    vals = np.array([S(u, kap)[0] for u in us]) / SLI
    margin = kap * np.exp(-1.0) * Xmax
    rms = np.sqrt(np.mean((vals - 1.0) ** 2)); spread = vals.max() - vals.min()
    rows.append((kap, rms, spread, vals.std()))
    print(f"{kap:5.3f} | {margin:7.1f} | {vals.mean():.6f} | {rms:.3e} | {spread:.3e}  (std_u {vals.std():.3e})")
rows = np.array(rows)
sl = np.diff(np.log(rows[:, 3])) / np.diff(np.log(rows[:, 0]))
print("log-log slopes of std_u(S/S_LI) vs kappa:", np.round(sl, 3).tolist())
sl2 = np.diff(np.log(rows[:, 2])) / np.diff(np.log(rows[:, 0]))
print("log-log slopes of (max-min) vs kappa:", np.round(sl2, 3).tolist())

# exact Gamma_L invariance check: gamma = s_(0,1,0,0) s_(1,3,0,0) is the boost along x1 with cosh eta = 8
eta = np.arccosh(8.0)
u1 = boost(-eta / 2, [1, 0, 0]); u2 = boost(+eta / 2, [1, 0, 0])
for kap in [0.4, 0.2, 0.1]:
    s1, s2 = S(u1, kap)[0], S(u2, kap)[0]
    print(f"Gamma-invariance check kappa={kap}: S(u)={s1:.10e}, S(gamma u)={s2:.10e}, rel diff {abs(s1-s2)/s1:.2e}"
          f"  (truncation margin kappa*e^-{eta/2:.2f}*x0max = {kap*np.exp(-eta/2)*Xmax:.1f})")
# non-invariance control: a boost along x2 by the same rapidity is NOT in Gamma_L
u3 = boost(+eta / 2, [0, 1, 0]); u4 = boost(+eta / 2, [0.6, 0.8, 0])
for kap in [0.4, 0.2, 0.1]:
    s1, s3, s4 = S(u1, kap)[0], S(u3, kap)[0], S(u4, kap)[0]
    print(f"control kappa={kap}: S(x2-boost)/S(u) - 1 = {s3/s1-1:.3e}; S(oblique)/S(u) - 1 = {s4/s1-1:.3e}")
