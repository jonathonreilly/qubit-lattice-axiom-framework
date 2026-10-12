#!/usr/bin/env python3
"""C3: Wetterich-type position-blind action on fixed Z^d. Constant composite vielbein E.

Classical part (EXACT lemma, no numerics): a scalar density L with L(E M^-1) = L(E)/det M
for constant E (position blindness under linear relabelling) gives L(E) = det(E) L(1),
so every position-blind counterterm is a function of det E only; at fixed det E it is
constant and cannot cancel a TT curvature.

One-loop part (this check): mean-field fermion operator det(E) gamma^m e_m^mu Delta_mu,
e = E^{-1}, Delta_mu the symmetric label difference (symbol i sin k_mu).
 (a) 3D Hamiltonian Dirac sea:   E_sea(A) = -< |A^{-1} s(k)| >_BZ        (per 2-component)
 (b) 4D Euclidean log det:       V(A)     = -< log |A^{-1} s(k)|^2 >_BZ  (per 2-component)
 with A = exp(eps X/2), det A = 1, X traceless symmetric in the spatial block.
Covariance (position blindness surviving the loop) would give d^2/deps^2 = 0.
Control: same integrand over a window that follows the strain (|A^{-1}k| < kc, s -> k): 0.
"""
import numpy as np
from scipy.linalg import expm

XE3 = np.diag([1.0, -1.0, 0.0]) / np.sqrt(2)
XT3 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], float) / np.sqrt(2)


def kgrid(L, d):
    # midpoint grid avoids k=0 and the doubler corners exactly (log singularities integrable)
    k = -np.pi + (np.arange(L) + 0.5) * 2 * np.pi / L
    return np.stack(np.meshgrid(*([k] * d), indexing="ij"), -1)


def f3(A, K):
    s = np.sin(K) @ np.linalg.inv(A).T
    return -np.sqrt((s * s).sum(-1)).mean()


def f4(A, K):
    s = np.sin(K) @ np.linalg.inv(A).T
    return -np.log((s * s).sum(-1)).mean()


def hess(f, X, K, h=0.02):
    e = [f(expm(t * h * X / 2), K) for t in (-2, -1, 0, 1, 2)]
    return (-e[0] + 16 * e[1] - 30 * e[2] + 16 * e[3] - e[4]) / (12 * h * h)


def embed4(X3):
    X = np.zeros((4, 4))
    X[1:, 1:] = X3
    return X


if __name__ == "__main__":
    for L in (48, 96, 160):
        K = kgrid(L, 3)
        print(f"3D Dirac sea  L={L}: H_E={hess(f3, XE3, K):+.5e}  H_T={hess(f3, XT3, K):+.5e}")
    for L in (24, 40, 56):
        K = kgrid(L, 4)
        print(f"4D log det    L={L}: H_E={hess(f4, embed4(XE3), K):+.5e}  H_T={hess(f4, embed4(XT3), K):+.5e}")
    # control: strain-following window, linear symbol, Monte Carlo-free exact radial check
    rng = np.random.default_rng(1)
    q = rng.normal(size=(400000, 3))
    q = q / np.linalg.norm(q, axis=1, keepdims=True) * rng.uniform(0, 1, (400000, 1)) ** (1 / 3)
    for X in (XE3, XT3):
        vals = []
        for t in (-1, 0, 1):
            A = expm(t * 0.05 * X / 2)
            k = q @ A.T  # window = image of the proper ball: |A^{-1}k| < 1
            vals.append(-np.linalg.norm(k @ np.linalg.inv(A).T, axis=1).mean())
        print(f"control (strain-following window) second difference: {(vals[0]-2*vals[1]+vals[2])/0.05**2:+.2e}")
