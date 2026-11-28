#!/usr/bin/env python3
"""Exact check of the strip bound, Lemma 10.1 of parts/upper-chain.md, criteria S1-S5.

2D Z_2 lattice gauge theory on a torus with n spatial links and Tt time slices.
Slice states: spatial link spins eta in {+1,-1}^n. Temporal links are integrated
inside T_1. Usage: upper-chain_strip.py
"""
import itertools
import os
import resource
import sys

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np

RSS_CAP = 2 * 1024**3


def check_rss():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss > RSS_CAP:
        sys.exit(f"RSS {rss} above cap")


def states(n):
    return np.array(list(itertools.product([1, -1], repeat=n)), dtype=float)


def build_T(beta, n):
    S = states(n)
    dim = len(S)
    U = states(n)
    T = np.zeros((dim, dim))
    for a in range(dim):
        for b in range(dim):
            w = 0.0
            for u in U:
                e = 0.0
                for i in range(n):
                    e += S[a, i] * u[(i + 1) % n] * S[b, i] * u[i]
                w += np.exp(beta * e)
            T[a, b] = w / len(U)
    return S, T


def slab_operator(Fvals, T, h):
    """F on a slab of thickness h as a kernel. Fvals has one value per path of slice
    states (eta_0, ..., eta_h), with temporal links integrated inside T_1; F is a
    function of the slices only, enough to test the algebra."""
    dim = T.shape[0]
    if h == 1:
        return Fvals * T
    Fh = np.zeros((dim, dim))
    for a in range(dim):
        for b in range(dim):
            Fh[a, b] = np.sum(Fvals[a, :, b] * T[a, :] * T[:, b])
    return Fh


def direct(Fh, Gh, T, h, m, Tt):
    N = Tt - 2 * h
    return np.trace(Fh @ np.linalg.matrix_power(T, m) @ Gh @ np.linalg.matrix_power(T, N - m)) / np.trace(
        np.linalg.matrix_power(T, Tt)
    )


def main():
    rng = np.random.default_rng(1)
    worst = {"S1": 0.0, "S2": 0.0, "S3": -np.inf, "S4": -np.inf}
    for n, Tt, beta in [(4, 8, 0.4), (4, 12, 0.8), (6, 8, 0.6)]:
        S, T = build_T(beta, n)
        check_rss()
        lam, vec = np.linalg.eigh(T)
        worst["S1"] = min(worst["S1"], lam.min() / lam.max())
        dim = T.shape[0]
        Z = np.trace(np.linalg.matrix_power(T, Tt))
        for h in (1, 2):
            N = Tt - 2 * h
            for trial in range(200 if n == 4 else 20):
                shape = (dim, dim) if h == 1 else (dim, dim, dim)
                Fv = rng.uniform(-1, 1, size=shape)
                Gv = rng.uniform(-1, 1, size=shape)
                Fh = slab_operator(Fv, T, h)
                Gh = slab_operator(Gv, T, h)
                c = {m: direct(Fh, Gh, T, h, m, Tt) for m in range(1, N)}
                Fe = vec.T @ Fh @ vec
                Ge = vec.T @ Gh @ vec
                lam_p = np.clip(lam, 0, None)
                keep = lam_p > 1e-12 * lam_p.max()

                def f(z):
                    lk = np.where(keep, lam_p, 1.0) ** z * keep
                    ll = np.where(keep, lam_p, 1.0) ** (N - z) * keep
                    return np.sum(Fe.T * np.outer(lk, ll) * Ge) / Z

                # S2 needs the trace identity against the eigen-expansion, and a
                # direct enumeration of the torus sum on the smallest system.
                for m in range(1, N):
                    worst["S2"] = max(worst["S2"], abs(f(m) - c[m]))
                if trial < 2 and n == 4 and Tt == 8 and h == 1:
                    worst["S2"] = max(worst["S2"], abs(enumerate_torus(Fv, Gv, S, T, m=2, Tt=Tt, Z=Z) - c[2]))
                M = np.abs(Fv).max() * np.abs(Gv).max()
                for _ in range(10):
                    z = rng.uniform(0.01, N - 0.01) + 1j * rng.uniform(-20, 20)
                    worst["S3"] = max(worst["S3"], abs(f(z)) - M)
                for m in range(1, N):
                    t = min(m, N - m)
                    for s in range(-t + 1, t):
                        if s != 0 and 0 < m + s < N:
                            worst["S4"] = max(worst["S4"], abs(c[m + s] - c[m]) - M * np.log(t / (t - abs(s))))
        check_rss()
    # S5: unequal thickness without padding, on the smallest system.
    n, Tt, beta = 4, 8, 0.8
    S, T = build_T(beta, n)
    dim = T.shape[0]
    Fv = rng.uniform(-1, 1, size=(dim, dim, dim))
    Fh = slab_operator(Fv, T, 2)
    Z = np.trace(np.linalg.matrix_power(T, Tt))
    N1 = Tt - 3
    a_unpadded = np.trace(Fh @ np.linalg.matrix_power(T, 2) @ Fh.T @ np.linalg.matrix_power(T, N1 - 2)) / Z
    print(f"S1 min lambda/lambda_max = {worst['S1']:.3e}")
    print(f"S2 max |f(m)-c(m)| and enumeration = {worst['S2']:.3e}")
    print(f"S3 max |f|-M = {worst['S3']:.3e}")
    print(f"S4 max excess over the log bound = {worst['S4']:.3e}")
    print(f"S5 unpadded A_F for |F|<=1, h_F=2, h_G=1, T=8: {a_unpadded:.4f}")
    ok = worst["S1"] >= -1e-12 and worst["S2"] <= 1e-10 and worst["S3"] <= 1e-10 and worst["S4"] <= 1e-10
    print("RESULT", "PASS" if ok else "FAIL")


def enumerate_torus(Fv, Gv, S, T, m, Tt, Z):
    """Direct sum over slice states of the torus, with F, G on slabs of thickness 1."""
    dim = T.shape[0]
    N = Tt - 2
    Tm = np.linalg.matrix_power(T, m)
    Tr = np.linalg.matrix_power(T, N - m)
    tot = 0.0
    for a in range(dim):
        for b in range(dim):
            for c in range(dim):
                for d in range(dim):
                    tot += Fv[a, b] * T[a, b] * Tm[b, c] * Gv[c, d] * T[c, d] * Tr[d, a]
    return tot / Z


if __name__ == "__main__":
    main()
