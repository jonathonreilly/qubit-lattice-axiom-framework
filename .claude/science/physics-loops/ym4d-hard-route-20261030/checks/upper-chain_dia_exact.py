#!/usr/bin/env python3
"""Exact test of E[s_p|xi] >= E[s_p|cold] with two free links sharing a plaquette (criteria D1, D2)."""
import os, sys
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np
from scipy.special import ive


def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0], axis=-1)


def qconj(a):
    c = -a.copy(); c[..., 0] = a[..., 0]; return c


def s3_grid(n):
    """Gauss quadrature for the Haar measure on S^3: (2/pi) sin^2(t) dt, sin(p) dp dphi /(4 pi)."""
    x, w = np.polynomial.legendre.leggauss(n)
    t = (x + 1) * np.pi / 2; wt = w * np.pi / 2 * (2 / np.pi) * np.sin(t) ** 2
    cp, wp = np.polynomial.legendre.leggauss(n); wp = wp / 2
    ph = 2 * np.pi * (np.arange(2 * n) + 0.5) / (2 * n); wph = np.full(2 * n, 1 / (2 * n))
    T, C, P = np.meshgrid(t, cp, ph, indexing="ij")
    W = np.einsum("i,j,k->ijk", wt, wp, wph)
    S = np.sqrt(1 - C**2)
    u = np.stack([np.cos(T), np.sin(T)*S*np.cos(P), np.sin(T)*S*np.sin(P), np.sin(T)*C], axis=-1)
    return u.reshape(-1, 4), W.ravel()


def expectations(beta, a1, a2, X, Y, grid):
    """Return E[(1/2)Tr U_p] for the 5 + 5 + 1 plaquettes. Weights exp(beta * sum)."""
    u2, wg = grid
    # q term: (1/2)Tr(U1 X U2^-1 Y) = u1 . b(u2), with b = conj(X U2^-1 Y) as a 4-vector
    b = qconj(qmul(qmul(X[None, :], qconj(u2)), Y[None, :]))
    A1 = a1.sum(axis=0)[None, :] + b
    r1 = np.linalg.norm(A1, axis=1)
    kappa = beta * r1
    # phi(kappa) = 2 I1(kappa)/kappa, with exponential scaling
    log_phi = np.log(2 * ive(1, kappa) / kappa) + kappa
    log_w = beta * (u2 @ a2.sum(axis=0)) + log_phi
    log_w -= log_w.max()
    w = wg * np.exp(log_w)
    w /= w.sum()
    Aratio = ive(2, kappa) / ive(1, kappa)
    Eu1 = (Aratio / r1)[:, None] * A1  # E[u1 | u2]
    out = [np.sum(w * (Eu1 @ a1[i])) for i in range(5)]
    out += [np.sum(w * (u2 @ a2[i])) for i in range(5)]
    out += [np.sum(w * np.sum(Eu1 * b, axis=1))]
    return np.array(out)


def rand_q(rng, n, amax=None):
    if amax is None:
        q = rng.standard_normal((n, 4)); return q / np.linalg.norm(q, axis=1, keepdims=True)
    d = rng.standard_normal((n, 3)); d /= np.linalg.norm(d, axis=1, keepdims=True)
    th = amax * rng.random(n)
    return np.concatenate([np.cos(th)[:, None], np.sin(th)[:, None] * d], axis=1)


def main():
    rng = np.random.default_rng(20261030)
    one = np.array([1.0, 0, 0, 0])
    a0 = np.tile(one, (5, 1))
    ncoarse, nfine = 28, 40
    g1, g2 = s3_grid(ncoarse), s3_grid(nfine)
    print("grid points", g1[0].shape[0], g2[0].shape[0], flush=True)
    for beta in (0.5, 1, 2, 4, 8, 16):
        # beta = 16 is sharp on the grid at cold; report the grid change at the worst point
        cold = expectations(beta, a0, a0, one, one, g2)
        worst = (1e9, None, None)
        for t in range(2000):
            amax = None if t % 2 == 0 else 0.3
            a1, a2 = rand_q(rng, 5, amax), rand_q(rng, 5, amax)
            X, Y = rand_q(rng, 1, amax)[0], rand_q(rng, 1, amax)[0]
            e = expectations(beta, a1, a2, X, Y, g1)
            d = (cold - e)  # E[s_p|xi] - E[s_p|cold] = E[trace|cold] - E[trace|xi]
            i = int(np.argmin(d))
            if d[i] < worst[0]:
                worst = (d[i], i, (a1, a2, X, Y))
        a1, a2, X, Y = worst[2]
        fine = (cold - expectations(beta, a1, a2, X, Y, g2))[worst[1]]
        print(f"beta={beta}: cold total s={11-cold.sum():.6f} min diff (coarse)={worst[0]:.3e} at p={worst[1]}, refined={fine:.3e}", flush=True)
    # D2: one free link, analytic check with q removed is checked by the first formula at beta small
    k = 6 * 1.0
    print("analytic one-link A(6)=", ive(2, k) / ive(1, k))


if __name__ == "__main__":
    main()
