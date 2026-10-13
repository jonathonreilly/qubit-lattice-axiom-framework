"""Illustration only (naive Wilson-Dirac, r=1, NN; NOT the D1 root edge).
Vacuum of a free 4-component Wilson-Dirac field: rho(l,m) = -2 <eps>/l^3 per site volume,
eps = sqrt(S/l^2 + (m + R/l)^2), S = sum sin^2 k, R = sum (1 - cos k); isotropic stretch l.
p = -dE/dV. Linear-in-m response at m = 0, l = 1: d rho/dm, d p/dm, dW/dm (W = rho + p)."""
import numpy as np
N = 96
k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
S = np.sin(kx)**2 + np.sin(ky)**2 + np.sin(kz)**2
R = (1 - np.cos(kx)) + (1 - np.cos(ky)) + (1 - np.cos(kz))
def g(l, m):
    return np.mean(np.sqrt(S / l**2 + (m + R / l)**2))
def rho(l, m):
    return -2 * g(l, m) / l**3
def p(l, m, h=1e-5):
    # E = rho * V, V = l^3 per site; p = -dE/dV
    E = lambda L: rho(L, m) * L**3
    return -(E(l + h) - E(l - h)) / (2 * h) / (3 * l**2)
h = 1e-6
drho = (rho(1, h) - rho(1, -h)) / (2 * h)
dp = (p(1, h) - p(1, -h)) / (2 * h)
print('naive Wilson r=1, N=%d: rho0 = %.6f, p0 = %.6f, p0/rho0 = %.6f' % (N, rho(1, 0), p(1, 0), p(1, 0) / rho(1, 0)))
print('d rho/dm = %.6f, d p/dm = %.3e, dW/dm = %.6f  (per 4-component field, lattice units)' % (drho, dp, drho + dp))
print('analytic: d rho/dm = -2<R/eps0> = %.6f' % (-2 * np.mean(R / np.sqrt(S + R**2))))
ma_top = 1.4145e-17
sum_ma = 3 * ma_top  # top only, 3 colours (illustrative)
cell = 8.8e122  # rho_Lambda per (1/l_P^4), as rR19-17 units
print('top-only |Delta W| ~ %.2e per cell ~ %.1e rho_Lambda (naive Wilson, illustrative)' % (abs(drho) * sum_ma, abs(drho) * sum_ma * cell))
