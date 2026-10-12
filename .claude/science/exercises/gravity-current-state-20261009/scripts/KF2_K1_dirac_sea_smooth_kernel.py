#!/usr/bin/env python3
"""K1 (kill agent, route F2): does the zone-face image suppression exp(-pi^2 s^2) of the
vacuum TT stiffness survive for a filled Dirac sea, not only for a massive scalar?

Fixed Z^3, metric g = exp(eps X), X traceless (det g = 1), A = g^{1/2}.
Smooth Dirac kernel in PROPER distance (odd, so it must vanish at all 8 TRIMs):
    d_a(k) = c * sum_n f(|A n|) (A n)_a sin(k.n),  f = exp(-r^2/2s^2),
    c = 1/((2 pi s^2)^{3/2} s^2)  so that d ~ p = A^{-T} k at small k (covariant).
Optional smooth Wilson mass (even kernel, breaks chiral symmetry):
    mW(k) = m0 + (r s/2) * Kg(k),  Kg = sum_n w(|An|)(1 - cos k.n)  (C1's gauss kernel, ~k^2, saturates 2/s^2)
Sea energy per site per 2-component:  E(g) = -< sqrt(|d|^2 + mW^2) >_BZ.
TT stiffness H = d^2E/deps^2 (5-point, h = 0.02), directions E_g and T_2g as in R2_c1.

Massless case: the conical point at k = 0 makes the BZ sum converge slowly. We subtract
phi(p) = |p| exp(-b |p|^2) (b = 4, negligible at the zone face), whose R^3 integral is
exactly shear invariant (det A = 1), and keep only < |d| - phi >_grid (error ~ h^6).

Also reports the flat-band fraction: share of BZ modes with omega < 0.05 * max(omega).
"""
import sys
import numpy as np
from scipy.linalg import expm

XE = np.diag([1.0, -1.0, 0.0]) / np.sqrt(2)
XT = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], float) / np.sqrt(2)


def grids(L):
    k = 2 * np.pi * np.fft.fftfreq(L)
    n = np.fft.fftfreq(L, d=1.0 / L)
    K = np.stack(np.meshgrid(k, k, k, indexing="ij"), -1)
    N = np.stack(np.meshgrid(n, n, n, indexing="ij"), -1)
    return K, N


def spectrum(g, s, K, N, m0, rW):
    w_, V = np.linalg.eigh(g)
    A = V @ np.diag(np.sqrt(w_)) @ V.T
    AN = np.einsum("ij,...j->...i", A, N)
    r2 = (AN ** 2).sum(-1)
    f = np.exp(-r2 / (2 * s * s))
    c = 1.0 / ((2 * np.pi * s * s) ** 1.5 * s * s)
    d2 = 0.0
    for a in range(3):
        Fa = c * f * AN[..., a]
        da = -np.fft.fftn(Fa).imag
        d2 = d2 + da * da
    m = np.full(d2.shape, m0)
    if rW > 0:
        w = 2.0 / ((2 * np.pi) ** 1.5 * s ** 5) * np.exp(-r2 / (2 * s * s))
        w[0, 0, 0] = 0.0
        Kg = w.sum() - np.fft.fftn(w).real
        m = m + 0.5 * rW * s * Kg
    return d2, m, A


def energy(g, s, K, N, m0, rW, subtract):
    d2, m, A = spectrum(g, s, K, N, m0, rW)
    om = np.sqrt(d2 + m * m)
    if subtract:
        Ainv_T = np.linalg.inv(A).T
        P = np.einsum("ij,...j->...i", Ainv_T, K)
        p2 = (P ** 2).sum(-1)
        phi = np.sqrt(p2) * np.exp(-4.0 * p2)
        return -(om - phi).mean()
    return -om.mean()


def hess(X, s, K, N, m0, rW, subtract, h=0.02):
    e = [energy(expm(t * h * X), s, K, N, m0, rW, subtract) for t in (-2, -1, 0, 1, 2)]
    return (-e[0] + 16 * e[1] - 30 * e[2] + 16 * e[3] - e[4]) / (12 * h * h)


if __name__ == "__main__":
    Ls = [int(x) for x in sys.argv[1:]] or [64]
    cases = [("massive m0=0.2, no Wilson", 0.2, 0.0, False),
             ("massless, no Wilson (subtracted)", 0.0, 0.0, True),
             ("massless + smooth Wilson r=1 (subtracted)", 0.0, 1.0, True)]
    svals = (0.75, 1.0, 1.25, 1.5, 1.75, 2.0)
    for L in Ls:
        K, N = grids(L)
        print(f"L={L}")
        for name, m0, rW, sub in cases:
            print(f"  case: {name}")
            for s in svals:
                hE = hess(XE, s, K, N, m0, rW, sub)
                hT = hess(XT, s, K, N, m0, rW, sub)
                d2, m, _ = spectrum(np.eye(3), s, K, N, m0, rW)
                om = np.sqrt(d2 + m * m)
                flat = (om < 0.05 * om.max()).mean()
                print(f"    s={s:4.2f} H_E={hE:+.3e} H_T={hT:+.3e}  e^-pi2s2={np.exp(-np.pi**2*s*s):.1e}"
                      f"  e^-pi2s2/2={np.exp(-np.pi**2*s*s/2):.1e}  flat(<5% max)={flat:.3f}")
            sys.stdout.flush()
