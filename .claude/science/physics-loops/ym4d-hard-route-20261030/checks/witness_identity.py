#!/usr/bin/env python3
"""Exact rectangle identity for Gaussian potentials with lattice-symmetric covariance.

Covariance on T^4, colour-isotropic, in Fourier space,
  c_mn(k) = delta_mn / khat^2 + a z_m conj(z_n) (w_m(k) + w_n(k)) / khat^4,
with z_m = exp(i k_m) - 1, khat^2 = sum |z_m|^2, and w_m(k) real, even in each k_mu, covariant
under permutations of the axes. On conserved J this adds a lattice gradient, so d c d^T = P is
unchanged and the law of gauge-invariant functions does change. This c is invariant under
lattice translations and reflections, and a, w are arbitrary otherwise (it is allowed to be wild).

Claim (parts/witness.md, Lemma 3.2): with E_k = c J_(l(y_k)), e = c J_3,
  sum_k K_comp^(k) / P_k = -24 Flux - 12 sum_k A_(l_3)(E_k, E_(k+1)) / P_k,
  and E_k is uniform, P_k / 4, in increments on the plaquette l(y_(k+1)).

PRE-REGISTERED CRITERIA (written before the first run).
 I1 IDENTITY: both sides agree to relative 1e-9 for each (a, b) tried, with the gradient part
    large enough that K_comp^(k) moves by more than 1e-3 relative to Feynman gauge.
 I2 UNIFORM: E_k on l(y_(k+1)) is uniform to 1e-9 relative to P_k / 4.
 I3 PSD: report the minimum over k of the smallest eigenvalue of khat^2 c(k), to say whether the
    example is a genuine covariance.
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_stokes import lasso_steps, steps_between  # noqa: E402
from witness_tree_coeff import K_comp, Lat, check_rss, curl, current, field_E, lievy, path_links, plaq  # noqa: E402


class Cov:
    def __init__(self, lat, a, b):
        self.lat = lat
        T = lat.T
        k = 2 * np.pi * np.fft.fftfreq(T)
        K = np.meshgrid(k, k, k, k, indexing="ij", sparse=True)
        self.z = [np.exp(1j * K[m]) - 1 for m in range(4)]
        self.khat2 = sum(np.abs(zm) ** 2 for zm in self.z)
        self.G = lat.inv
        G2 = self.G * self.G
        env = np.ones_like(self.khat2)
        for m in range(4):
            env = env * (1 + b * np.cos(3 * K[m]))
        self.w = [(np.abs(self.z[m]) ** 2) * env for m in range(4)]
        self.G2 = G2
        self.a = a

    def apply(self, J):
        Jh = [np.fft.fftn(J[m]) for m in range(4)]
        out = []
        for m in range(4):
            acc = self.G * Jh[m]
            for n in range(4):
                acc = acc + self.a * self.z[m] * np.conj(self.z[n]) * (self.w[m] + self.w[n]) * self.G2 * Jh[n]
            out.append(np.fft.ifftn(acc).real)
        return np.stack(out)

    def min_eig(self, nsample=4000, seed=3):
        rng = np.random.default_rng(seed)
        T = self.lat.T
        worst = np.inf
        for _ in range(nsample):
            i = tuple(rng.integers(0, T, size=4))
            if i == (0, 0, 0, 0):
                continue
            z = np.array([self.z[m][i if self.z[m].shape == (T, T, T, T) else tuple(i[j] if self.z[m].shape[j] > 1 else 0 for j in range(4))] for m in range(4)])
            w = np.array([self.w[m][i] for m in range(4)])
            kh2 = float(np.sum(np.abs(z) ** 2))
            C = np.eye(4, dtype=complex) / kh2 + self.a * np.outer(z, np.conj(z)) * (w[:, None] + w[None, :]) / kh2**2
            worst = min(worst, float(np.linalg.eigvalsh(kh2 * C).min()))
        return worst


def run(lat, cov, D, R):
    c = (D - 1) // 2
    far = (R, 0, c, c)
    corners = [(0, 0, 0, 0), (0, 0, D, 0), (0, 0, D, D), (0, 0, 0, D)]
    l3 = plaq(3, 4)
    L3base = path_links(lat, far, l3)
    e = cov.apply(current(lat, L3base))
    Es = {y: cov.apply(current(lat, path_links(lat, y, plaq(1, 2)))) for y in corners}
    lhs, far_term, unif = 0.0, 0.0, 0.0
    kvals = []
    for k, y in enumerate(corners):
        z = corners[(k + 1) % 4]
        L1 = path_links(lat, y, plaq(1, 2))
        L2 = path_links(lat, y, lasso_steps(steps_between(y, z), plaq(1, 2)))
        L3 = path_links(lat, y, lasso_steps(steps_between(y, far), l3))
        E1, E2 = Es[y], Es[z]
        kc = K_comp(lat, L1, L2, L3, E1, E2, e)
        Pk = float(np.sum(current(lat, L2) * E1))
        lhs += kc / Pk
        far_term += lievy(L3base, E1, E2) / Pk
        kvals.append(kc)
        incs = [eps * E1[(mu,) + site] for site, mu, eps in path_links(lat, z, plaq(1, 2))]
        unif = max(unif, max(abs(v - Pk / 4) for v in incs) / abs(Pk / 4))
    P3 = curl(lat, e, 2, 3)
    flux = float(np.sum(P3[0, 0, 0:D, 0:D]))
    rhs = -24 * flux - 12 * far_term
    return lhs, rhs, flux, far_term, unif, kvals


def main():
    T = 24
    lat = Lat(4, T)
    base = None
    for (a, b) in ((0.0, 0.0), (0.5, 0.0), (-0.5, 0.0), (2.0, 0.0), (0.5, 0.7), (-1.5, 0.9)):
        cov = Cov(lat, a, b)
        for (D, R) in ((3, 6), (3, 8), (5, 8)):
            lhs, rhs, flux, far, unif, kvals = run(lat, cov, D, R)
            if a == 0.0 and (D, R) == (3, 8):
                base = kvals[0]
            rel = abs(lhs - rhs) / max(abs(rhs), 1e-30)
            print(f"a={a} b={b} D={D} R={R}: lhs={lhs:.6e} rhs={rhs:.6e} rel={rel:.1e} -24Flux={-24*flux:.6e} far={far:.3e} unif={unif:.1e} K0={kvals[0]:.4e}", flush=True)
        print(f"   min eig of khat^2 c(k) over samples: {cov.min_eig(1500):.3f} rss={check_rss():.2f}GB", flush=True)


if __name__ == "__main__":
    main()
