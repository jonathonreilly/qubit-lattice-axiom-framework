"""Reflection positivity (OS) test for Gaussian fields on the D4 cone, at fixed spatial Bloch momentum.

Field x_tau(b) on vertex types; quadratic form Q(k) per Bloch momentum (Q(k)[i,j] couples x_i(b) with x_j(b + d)
through phase e^{ik.d}). On a time torus of Nt cells, the covariance between (bt1, tau1) and (bt2, tau2) at
spatial momentum ks is G = (1/Nt) sum_kt [Q(ks,kt)^-1]_{tau1 tau2} e^{i kt (bt1 - bt2)} (sign fixed by a check).
OS positivity for the reflection Theta: t -> 2 t0 - t: the matrix R[a, b] = <x_a  conj(x_{Theta b})> over
vertices a, b with t >= t0 (one half of the torus) must be positive semidefinite.
"""
import numpy as np

def covariance_blocks(Qfun, ks, Nt):
    kts = 2 * np.pi * np.arange(Nt) / Nt
    inv = [np.linalg.inv(Qfun(np.array([*ks, kt]))) for kt in kts]
    def G(dbt):   # dbt = bt1 - bt2 (integer)
        return sum(Ki * np.exp(1j * kt * dbt) for Ki, kt in zip(inv, kts)) / Nt
    return G

def rp_matrix(Qfun, offs_t, ks, Nt, t0, conj_fix=False):
    """offs_t[tau]: t-offset of vertex type tau (0 or 1/2); reflection t -> 2 t0 - t maps type tau to itself."""
    G = covariance_blocks(Qfun, ks, Nt)
    half = []
    for bt in range(-1, Nt // 2 + 1):
        for tau, ot in enumerate(offs_t):
            t = bt + ot
            if t0 - 1e-9 <= t <= t0 + Nt / 2 + 1e-9: half.append((bt, tau, t))
    n = len(half); R = np.zeros((n, n), complex)
    for a, (bt1, ta, t1) in enumerate(half):
        for b, (bt2, tb, t2) in enumerate(half):
            tr = 2 * t0 - t2; btr = int(round(tr - offs_t[tb]))   # reflected cell index of vertex b
            R[a, b] = G(bt1 - btr)[ta, tb]
    return R, half
