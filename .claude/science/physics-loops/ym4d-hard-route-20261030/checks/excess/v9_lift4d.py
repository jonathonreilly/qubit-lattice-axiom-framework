#!/usr/bin/env python3
"""T9 of CRITERIA.md: abelian tensor lift in d = 4 on a small torus, kernels periodised from the line."""
import itertools
import sys

import numpy as np

sys.path.insert(0, ".")
from v8_lift1d import build


def kernels(L, Np):
    n, Nc, T0, R0 = build(L)
    dz = np.roll(T0, -1, axis=0) - T0
    eta = np.zeros((n, Nc))
    for j in range(Nc):
        for s in range(1, Nc // 2):
            eta[:, j] += dz[:, (j + s) % Nc]
        for xx in range(n):
            dist = ((xx - L * j - L / 2 + n / 2) % n) - n / 2
            if abs(dist) > 6.5 * L:
                eta[xx, j] = 0
    # periodise row j = 0 kernels onto torus of Np parents
    m = L * Np
    z = np.zeros((m, Np))
    e = np.zeros((m, Np))
    for j in range(Np):
        for x in range(n):
            xc = ((x + n // 2) % n) - n // 2  # signed
            z[(xc + L * j) % m, j] += T0[x, 0]
            e[(xc + L * j) % m, j] += eta[x, 0]
    return m, z, e


def apply(field, mats):
    out = field
    for ax, M in enumerate(mats):
        out = np.moveaxis(np.tensordot(M, out, axes=(1, ax)), 0, ax)
    return out


def grad_energy(th):
    tot = 0.0
    for t in th.values():
        for ax in range(4):
            tot += ((np.roll(t, -1, axis=ax) - t) ** 2).sum()
    return tot


def main():
    for L in (LS if 'LS' in globals() else (3, 5, 7)):
        Np = 4
        m, z, e = kernels(L, Np)
        rng = np.random.default_rng(L)
        worstC1 = worstC2 = 0.0
        for trial in range(TR if 'TR' in globals() else 6):
            if trial % 2 == 0:
                A = rng.normal(size=(Np,) * 4 + (4,))
            else:
                g = np.meshgrid(*[np.arange(Np)] * 4, indexing="ij")
                A = np.zeros((Np,) * 4 + (4,))
                for mode in range(4):
                    k = rng.integers(-1, 2, 4)
                    ph = rng.uniform(0, 6.28)
                    c = rng.normal(size=4)
                    w = np.cos(sum(2 * np.pi * k[a] * g[a] / Np for a in range(4)) + ph)
                    A += w[..., None] * c
            th1 = {}
            for mu, nu in itertools.combinations(range(4), 2):
                th1[(mu, nu)] = A[..., mu] + np.roll(A[..., nu], -1, mu) - np.roll(A[..., mu], -1, nu) - A[..., nu]
            th0 = {}
            for p, t in th1.items():
                mats = [e if a in p else z for a in range(4)]
                th0[p] = apply(t, mats)
            E1 = sum((t**2).sum() for t in th1.values())
            E0 = sum((t**2).sum() for t in th0.values())
            I1 = grad_energy(th1)
            I0 = grad_energy(th0)
            exc = E0 - E1
            worstC1 = max(worstC1, exc / I1)
            worstC2 = max(worstC2, I0 / I1 * L**2)
            # closedness on the fine lattice
            mu, nu, rho = 0, 1, 2
            a, b, c = th0[(0, 1)], th0[(1, 2)], th0[(0, 2)]
            db = (np.roll(a, -1, 2) - a) + (np.roll(b, -1, 0) - b) - (np.roll(c, -1, 1) - c)
            print(f"L {L} trial {trial}: E0 {E0:.4f} E1 {E1:.4f} exc/I1 {exc/I1:.4f} I0/I1*L^2 {I0/I1*L**2:.3f} closed {abs(db).max():.1e}", flush=True)
        # constant flux
        t = np.ones((Np,) * 4)
        lifted = apply(t, [e if a in (0, 1) else z for a in range(4)])
        print(f"L {L}: const flux lift range {lifted.min()*L**2:.12f} {lifted.max()*L**2:.12f}; C1 {worstC1:.3f} C2 {worstC2:.3f}", flush=True)


if __name__ == "__main__":
    main()
