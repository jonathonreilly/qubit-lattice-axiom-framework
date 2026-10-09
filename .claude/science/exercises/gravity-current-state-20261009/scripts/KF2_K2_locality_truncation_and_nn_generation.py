#!/usr/bin/env python3
"""K2 (kill agent, route F2): locality cost of the smooth proper-distance kernel.

Same observable as R2_c1: free massive scalar (M = 0.2) on fixed Z^3, E = 1/2 <sqrt(M^2 + K)>,
TT stiffness = d^2E/deps^2 along E_g and T_2g, g = exp(eps X), det g = 1.

(a) TRUNCATION. The Gaussian kernel w(|An|) cut at proper radius |An| < R (cut moves with g),
    and cut at label radius |n| < R (fixed set). Prediction: stiffness ~ exp(-R^2/2s^2) until the
    untruncated exp(-pi^2 s^2) floor. So 1e-102 needs R >~ 21.7 s.

(b) GENERATED FROM A FINITE-RANGE RULE. Any kernel produced by iterating / integrating out a
    fixed finite-range operator S_g is a function F(S_g). Heat-flow form:
        K = (2/s^2) (1 - exp(-s^2 S_g / 2)),
    with S_g = the R2_c1 'nn' form (axis + face-diagonal stencil; the off-diagonal metric needs
    the face diagonals). Also a Symanzik-improved (range-2) S_g^imp whose k^4 axis artefact is removed.
    Prediction: power-law decay in s (the generator's O(k^4) label structure at k ~ 1/s).
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


def imp_form(K, gi):
    # range-2 improved: axis symbol (4/3)(2-2cos k) - (1/12)(2-2cos 2k) = k^2 + O(k^6);
    # mixed symbol (4/3) sin k - (1/6) sin 2k = k + O(k^5)
    ax = (4.0 / 3.0) * (2 - 2 * np.cos(K)) - (1.0 / 12.0) * (2 - 2 * np.cos(2 * K))
    dv = (4.0 / 3.0) * np.sin(K) - (1.0 / 6.0) * np.sin(2 * K)
    S = sum(gi[i, i] * ax[..., i] for i in range(3))
    S = S + sum(gi[i, j] * dv[..., i] * dv[..., j] for i in range(3) for j in range(3) if i != j)
    return S


def energy(kind, g, s, K, N, R=None):
    gi = np.linalg.inv(g)
    if kind in ("gauss", "gauss_cut_proper", "gauss_cut_label"):
        r2 = np.einsum("...i,ij,...j->...", N, g, N)
        w = 2.0 / ((2 * np.pi) ** 1.5 * s ** 5) * np.exp(-r2 / (2 * s * s))
        if kind == "gauss_cut_proper":
            w = np.where(r2 < R * R, w, 0.0)
        if kind == "gauss_cut_label":
            w = np.where((N ** 2).sum(-1) < R * R, w, 0.0)
        w[0, 0, 0] = 0.0
        Kk = w.sum() - np.fft.fftn(w).real
    elif kind == "heat_nn":
        Kk = (2.0 / s ** 2) * (1 - np.exp(-s * s * nn_form(K, gi) / 2))
    elif kind == "heat_imp":
        Kk = (2.0 / s ** 2) * (1 - np.exp(-s * s * imp_form(K, gi) / 2))
    Kk = np.maximum(Kk, 0.0)
    return 0.5 * np.sqrt(M * M + Kk).mean()


def hess(kind, X, s, K, N, R=None, h=0.02):
    e = [energy(kind, expm(t * h * X), s, K, N, R) for t in (-2, -1, 0, 1, 2)]
    return (-e[0] + 16 * e[1] - 30 * e[2] + 16 * e[3] - e[4]) / (12 * h * h)


if __name__ == "__main__":
    L = 64
    K, N = grids(L)
    print(f"L={L}, M={M}")
    print("(a) truncation, s = 1.5 (untruncated floor ~ 1e-10 at this L, see R2_c1.out)")
    s = 1.5
    for R in (3.0, 4.0, 5.0, 6.0, 7.0):
        for kind in ("gauss_cut_proper", "gauss_cut_label"):
            hE = hess(kind, XE, s, K, N, R * s)
            hT = hess(kind, XT, s, K, N, R * s)
            print(f"  {kind:17s} R={R:.0f}s  H_E={hE:+.3e} H_T={hT:+.3e}  exp(-R^2/2s^2)={np.exp(-R*R/2):.1e}")
    print("(b) generated from a finite-range rule: K = (2/s^2)(1 - exp(-s^2 S_g/2))")
    for kind in ("heat_nn", "heat_imp"):
        prev = None
        for s in (1.0, 2.0, 4.0, 8.0, 16.0):
            hE = hess(kind, XE, s, K, N)
            hT = hess(kind, XT, s, K, N)
            slope = "" if prev is None else f"  local slope dlog|H_E|/dlog s = {np.log(abs(hE)/abs(prev))/np.log(2):+.2f}"
            print(f"  {kind:8s} s={s:5.1f} H_E={hE:+.3e} H_T={hT:+.3e}{slope}")
            prev = hE
    print("  (L=96 spot check of heat_nn s=8, s=16)")
    K2, N2 = grids(96)
    for s in (8.0, 16.0):
        print(f"  heat_nn  s={s:5.1f} L=96 H_E={hess('heat_nn', XE, s, K2, N2):+.3e} H_T={hess('heat_nn', XT, s, K2, N2):+.3e}")
