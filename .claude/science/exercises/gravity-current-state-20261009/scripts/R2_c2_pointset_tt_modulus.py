#!/usr/bin/env python3
"""C2: vacuum TT stiffness of a free massive scalar on a QUENCHED site set, with
adjacency/weights derived from the metric (Gaussian kernel in proper distance).

Site sets at unit density in a periodic box of side Lb (label coordinates):
  Z3      : cubic crystal
  poisson : uniform random points (law invariant under SL(3))
  rsa     : random sequential adsorption, exclusion diameter d (isotropic, correlated: a glass)
H = m^2 + Lap_g,  Lap_g = D - W,  W_ij = C exp(-|A(x_i-x_j)|^2/2s^2), A = g^{1/2}, det g = 1.
E = (1/2N) sum sqrt(eig H).  TT stiffness = d^2E/deps^2 for g = exp(eps X).
Lemma (EXACT for the ensemble mean): if the law of the site set is SL(3)-invariant, E[E(g)]
depends on g only through det g, so the mean stiffness is 0 (up to box-shape finite size).
"""
import sys
import numpy as np
from scipy.linalg import expm, eigvalsh

M = 0.2
S = 0.5
XE = np.diag([1.0, -1.0, 0.0]) / np.sqrt(2)
XT = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], float) / np.sqrt(2)


def sites(kind, Lb, rng, d=0.83):
    N = Lb ** 3
    if kind == "Z3":
        a = np.arange(Lb, dtype=float)
        return np.stack(np.meshgrid(a, a, a, indexing="ij"), -1).reshape(-1, 3)
    if kind == "poisson":
        return rng.uniform(0, Lb, size=(N, 3))
    if kind == "rsa":
        pts = []
        while len(pts) < N:
            p = rng.uniform(0, Lb, 3)
            if pts:
                dd = np.array(pts) - p
                dd -= Lb * np.round(dd / Lb)
                if (dd * dd).sum(1).min() < d * d:
                    continue
            pts.append(p)
        return np.array(pts)


def energy(X, Lb, g):
    D = X[:, None, :] - X[None, :, :]
    D -= Lb * np.round(D / Lb)
    r2 = np.einsum("abi,ij,abj->ab", D, g, D)
    C = 2.0 / ((2 * np.pi) ** 1.5 * S ** 5)
    W = C * np.exp(-r2 / (2 * S * S))
    np.fill_diagonal(W, 0.0)
    H = np.diag(W.sum(1) + M * M) - W
    ev = eigvalsh(H)
    return 0.5 * np.sqrt(np.maximum(ev, 0)).mean()


def hess(X, Lb, Xdir, h=0.02):
    e = [energy(X, Lb, expm(t * h * Xdir)) for t in (-2, -1, 0, 1, 2)]
    return (-e[0] + 16 * e[1] - 30 * e[2] + 16 * e[3] - e[4]) / (12 * h * h)


if __name__ == "__main__":
    Lb = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    ns = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    rng = np.random.default_rng(20261009 + Lb)
    for kind in ("Z3", "poisson", "rsa"):
        hs = []
        for s in range(1 if kind == "Z3" else ns):
            X = sites(kind, Lb, rng)
            hs.append((hess(X, Lb, XE), hess(X, Lb, XT)))
        hs = np.array(hs)
        mE, mT = hs.mean(0)
        if len(hs) > 1:
            eE, eT = hs.std(0, ddof=1) / np.sqrt(len(hs))
        else:
            eE = eT = 0.0
        print(f"Lb={Lb} N={Lb**3} {kind:8s} n={len(hs):2d}  H_E={mE:+.4e} +- {eE:.1e}   H_T={mT:+.4e} +- {eT:.1e}", flush=True)
