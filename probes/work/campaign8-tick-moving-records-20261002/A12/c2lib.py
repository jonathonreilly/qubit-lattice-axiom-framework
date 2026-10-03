"""C2: soft excitations. Massless 1D Dirac step, R seed (flat quasi-energy measure).
Stopband S = (-pi, 0) (the filled sea). Target band I_E = [E/2, 3E/2] (soft excitations near quasi-energy E).
For a T-tap window f: eps = f^+ A_S f / f^+ f (vacuum rate), eta = f^+ A_I f / f^+ f
(= recording probability of the best-matched excitation with spectrum inside I_E).
Pareto optimum eps*(T, E) at eta >= 1/2 via the Lagrangian: smallest eigenvector of A_S - lam A_I
(joint numerical range of two Hermitian forms is convex, so this is exact), bisection on lam.
Test: does eps* collapse onto a function of E*T (uncertainty scaling), or scale like sqrt(E)*T?
Also: Dolph-Chebyshev window centred at E with main-lobe half-width E (closed form)."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
from scipy.linalg import eigh, toeplitz

PI = np.pi


def arc_toeplitz(T, a, b):
    """M[s,t] = (1/2pi) int_a^b e^{i theta (t-s)} d theta."""
    d = np.arange(T, dtype=float)
    col = np.empty(T, complex)
    col[0] = (b - a) / (2 * PI)
    dd = d[1:]
    col[1:] = (np.exp(-1j * b * dd) - np.exp(-1j * a * dd)) / (2 * PI * (-1j) * dd)   # entries M[s, 0], s - t = d
    return toeplitz(col, col.conj())


def pareto(T, E, eta0=0.5):
    AS = arc_toeplitz(T, -PI, 0.0)
    AI = arc_toeplitz(T, E / 2, 3 * E / 2)
    def point(lam):
        w, V = eigh(AS - lam * AI, subset_by_index=[0, 0])
        f = V[:, 0]
        return (f.conj() @ AS @ f).real, (f.conj() @ AI @ f).real
    lo, hi = 0.0, 1.0
    while point(hi)[1] < eta0:
        hi *= 4
        if hi > 1e12:
            return np.nan, np.nan
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if point(mid)[1] < eta0:
            lo = mid
        else:
            hi = mid
    return point(hi)


def cheb_at_E(T, E):
    """DC window centred at E, main-lobe half-width E: eps into S and eta in I_E (closed form W)."""
    n = T - 1
    x0 = 1 / np.cos(E / 2); kap = np.arccosh(x0)
    M = 64 * T + 4096
    th = -PI + 2 * PI * (np.arange(M) + 0.5) / M
    y = x0 * np.cos((th - E) / 2)
    big = np.abs(y) > 1
    lw = np.empty(M)
    a = np.arccosh(np.abs(y[big])); lw[big] = 2 * (n * a + np.log1p(np.exp(-2 * n * a)) - np.log(2))
    lw[~big] = 2 * np.log(np.abs(np.cos(n * np.arccos(y[~big]))) + 1e-300)
    tot = np.logaddexp.reduce(lw)
    eps = np.exp(np.logaddexp.reduce(lw[th < 0]) - tot)
    inI = (th >= E / 2) & (th <= 3 * E / 2)
    eta = np.exp(np.logaddexp.reduce(lw[inI]) - tot)
    return eps, eta, kap


