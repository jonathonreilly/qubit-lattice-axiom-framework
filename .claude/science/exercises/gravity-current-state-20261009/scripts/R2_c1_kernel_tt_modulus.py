#!/usr/bin/env python3
"""C1: vacuum TT stiffness of a free massive scalar on fixed Z^3 versus the
shape of its metric coupling.

Metric g = exp(eps X), X traceless symmetric (det g = 1, volume preserving).
X_E = diag(1,-1,0)/sqrt2 (E_g), X_T = (e_xy+e_yx)/sqrt2 (T_2g).
Vacuum energy per site E(eps) = 1/2 <sqrt(m^2 + K(k; g))>_BZ (Hamiltonian, one real scalar).
TT stiffness = d^2E/deps^2 at eps=0 (5-point stencil).

Kernels:
  nn    : K = sum_i g^ii shat_i^2 + sum_{i!=j} g^ij sin k_i sin k_j   (minimal-coupling type)
  gauss : K = sum_n w(|A n|)(1-cos k.n), w = 2/((2pi)^{3/2} s^5) exp(-|An|^2/2s^2), A = g^{1/2}
          (isotropic function of the PROPER distance of the label displacement: cutoff moves with g)
  ratl  : K = S/(1+s^2 S), S = nn form   (saturating, Pauli-Villars-like; built from lattice ops)
Continuum covariance predicts 0 for every kernel; any nonzero value is a lattice (fixed-BZ) effect.
"""
import numpy as np
from scipy.linalg import expm

M = 0.2
XE = np.diag([1.0, -1.0, 0.0]) / np.sqrt(2)
XT = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], float) / np.sqrt(2)


def grids(L):
    k = 2 * np.pi * np.fft.fftfreq(L)
    n = np.fft.fftfreq(L, d=1.0 / L)
    K = np.stack(np.meshgrid(k, k, k, indexing="ij"), -1)
    N = np.stack(np.meshgrid(n, n, n, indexing="ij"), -1)
    return K, N


def nn_form(K, gi):
    sh = 2 * np.sin(K / 2)
    sn = np.sin(K)
    S = sum(gi[i, i] * sh[..., i] ** 2 for i in range(3))
    S = S + sum(gi[i, j] * sn[..., i] * sn[..., j] for i in range(3) for j in range(3) if i != j)
    return S


def energy(kind, g, s, L, K, N):
    gi = np.linalg.inv(g)
    if kind == "nn":
        Kk = nn_form(K, gi)
    elif kind == "ratl":
        S = nn_form(K, gi)
        Kk = S / (1 + s * s * S)
    elif kind == "gauss":
        r2 = np.einsum("...i,ij,...j->...", N, g, N)
        w = 2.0 / ((2 * np.pi) ** 1.5 * s ** 5) * np.exp(-r2 / (2 * s * s))
        w[0, 0, 0] = 0.0
        Kk = w.sum() - np.fft.fftn(w).real
    Kk = np.maximum(Kk, 0.0)
    return 0.5 * np.sqrt(M * M + Kk).mean()


def hess(kind, X, s, L, K, N, h=0.02):
    e = [energy(kind, expm(t * h * X), s, L, K, N) for t in (-2, -1, 0, 1, 2)]
    return (-e[0] + 16 * e[1] - 30 * e[2] + 16 * e[3] - e[4]) / (12 * h * h), e[2]


if __name__ == "__main__":
    for L in (64, 96):
        K, N = grids(L)
        print(f"L={L}")
        hE, E0 = hess("nn", XE, 0, L, K, N)
        hT, _ = hess("nn", XT, 0, L, K, N)
        print(f"  nn          E0={E0:.6f}  H_E={hE:+.3e}  H_T={hT:+.3e}")
        for s in (0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.5):
            hE, E0 = hess("gauss", XE, s, L, K, N)
            hT, _ = hess("gauss", XT, s, L, K, N)
            pred = np.exp(-np.pi ** 2 * s * s)
            print(f"  gauss s={s:4.2f} E0={E0:.6f}  H_E={hE:+.3e}  H_T={hT:+.3e}  exp(-pi^2 s^2)={pred:.1e}")
        for s in (1.0, 2.0, 4.0, 8.0):
            hE, E0 = hess("ratl", XE, s, L, K, N)
            hT, _ = hess("ratl", XT, s, L, K, N)
            print(f"  ratl  s={s:4.1f} E0={E0:.6f}  H_E={hE:+.3e}  H_T={hT:+.3e}")
