#!/usr/bin/env python3
"""C4: reflection positivity (RP) of a free field whose 4D-isotropic kernel is smooth in time.

At spatial momentum 0 the 4D kernel reduces to a 1D kernel in Euclidean time:
  gauss: K(q0) = sum_n W(n)(1-cos q0 n), W(n) ~ exp(-n^2/2s^2)  (normalised to K ~ q0^2)
  ratl : K(q0) = S/(1+s^2 S), S = 2(1-cos q0)
  nn   : K(q0) = S
G(t) = (1/2pi) int dq0 cos(q0 t)/(m^2+K).  Lattice RP (Osterwalder-Schrader, reflection
through a site) requires the Hankel matrix [G(i+j)]_{i,j=0..T} to be positive semidefinite.
PASS (RP) iff min eigenvalue >= -tol.
"""
import numpy as np

M = 0.3


def G_of_t(kind, s, T, Nq=1 << 16):
    q = 2 * np.pi * np.arange(Nq) / Nq
    if kind == "gauss":
        n = np.arange(1, int(12 * s) + 2)
        W = np.exp(-n ** 2 / (2 * s * s))
        W = W / (W * n ** 2).sum()  # so that K ~ q0^2 at small q0
        K = (W[None, :] * (1 - np.cos(np.outer(q, n)))).sum(1)
    else:
        S = 2 * (1 - np.cos(q))
        K = S / (1 + s * s * S) if kind == "ratl" else S
    g = np.fft.ifft(1.0 / (M * M + K)).real
    return g[: 2 * T + 1]


if __name__ == "__main__":
    T = 10
    for kind, svals in (("nn", [0]), ("ratl", [1, 2, 4]), ("gauss", [0.5, 1, 2, 3])):
        for s in svals:
            g = G_of_t(kind, s, T)
            H = np.array([[g[i + j] for j in range(T + 1)] for i in range(T + 1)])
            ev = np.linalg.eigvalsh(H)
            ratio = ev.min() / ev.max()
            verdict = "RP ok" if ratio > -1e-12 else "RP VIOLATED"
            print(f"{kind:5s} s={s:<4} min/max Hankel eig = {ratio:+.3e}  {verdict}")
