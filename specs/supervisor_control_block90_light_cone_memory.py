#!/usr/bin/env python3
"""Supervisor control for block 90 (disjoint machinery: floating-point quadrature, lattice sums, and an independent light-cone formation simulator;
evidence, not proof).

W1: the infinite-volume constants: I_0 = int d^3k/(2 pi)^3 1/E(k) = int_0^inf e^{-6t} I_0(2t)^3 dt against W/6 with W the cubic lattice's return
    integral in closed form (Gamma functions), I_2 = int 1/(E + 2) = int_0^inf e^{-8t} I_0(2t)^3 dt; beta_0 = (3/2)(I_0 + I_2).
W2: the finite-size thresholds beta_L = (3/2)(G_L + H_L) on tori of side 4 to 64 (the approach to beta_0).
W3: an independent light-cone formation simulator (not the probes' formation_levelplane.py): unit vectors on an L^3 plane; each level every
    record re-forms from the seven records of the previous level at x + {0, +-e_j} with density proportional to exp(beta s'.h) on the sphere
    (exact sampling of the cosine by inversion); start aligned; |m| averaged over the second half of T levels; L = 24, 32; beta across 0.55-0.65.
"""
import math
import sys

import numpy as np
from scipy import integrate, special


def w1():
    print("W1: infinite-volume constants")
    f0 = lambda t: special.ive(0, 2 * t) ** 3
    f2 = lambda t: special.ive(0, 2 * t) ** 3 * math.exp(-2 * t)
    I0 = integrate.quad(f0, 0, np.inf, limit=400, epsabs=1e-14, epsrel=1e-13)[0]
    I2 = integrate.quad(f2, 0, np.inf, limit=400, epsabs=1e-14, epsrel=1e-13)[0]
    W = math.sqrt(6) / (32 * math.pi ** 3) * math.gamma(1 / 24) * math.gamma(5 / 24) * math.gamma(7 / 24) * math.gamma(11 / 24)
    print(f"  I_0 = {I0:.12f}; W/6 = {W / 6:.12f} (W = {W:.10f}); I_2 = {I2:.12f}; beta_0 = (3/2)(I_0 + I_2) = {1.5 * (I0 + I2):.10f}")
    return 1.5 * (I0 + I2)


def w2():
    print("W2: finite-size thresholds beta_L = (3/2)(G_L + H_L)")
    for L in (4, 6, 8, 12, 16, 24, 32, 48, 64):
        k = 2 * np.pi * np.arange(L) / L
        c = np.cos(k)
        E = 6 - 2 * (c[:, None, None] + c[None, :, None] + c[None, None, :])
        N = L ** 3
        G = np.sum(1 / E[E > 1e-12]) / N
        H = np.sum(1 / (E + 2)) / N
        print(f"  L={L}: beta_L = {1.5 * (G + H):.6f}")


def sample_sphere_exp(h, beta, rng):
    """Sample s with density proportional to exp(beta s.h) on the unit sphere, for an array of h (n x 3)."""
    n = h.shape[0]
    kap = beta * np.linalg.norm(h, axis=1)
    u = rng.random(n)
    with np.errstate(divide="ignore", invalid="ignore"):
        w = np.where(kap > 1e-12, 1 + np.log(u + (1 - u) * np.exp(-2 * kap)) / np.maximum(kap, 1e-300), 2 * u - 1)
    w = np.clip(w, -1, 1)
    hn = np.where(kap[:, None] > 1e-12, h / np.maximum(np.linalg.norm(h, axis=1), 1e-300)[:, None], np.array([0.0, 0.0, 1.0]))
    a = np.where(np.abs(hn[:, 0:1]) < 0.9, np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]))
    e1 = np.cross(hn, a)
    e1 /= np.linalg.norm(e1, axis=1)[:, None]
    e2 = np.cross(hn, e1)
    phi = 2 * np.pi * rng.random(n)
    r = np.sqrt(np.maximum(0, 1 - w * w))
    return w[:, None] * hn + (r * np.cos(phi))[:, None] * e1 + (r * np.sin(phi))[:, None] * e2


def light_cone_run(L, beta, T, seed):
    rng = np.random.default_rng(seed)
    s = np.zeros((L, L, L, 3))
    s[..., 2] = 1.0
    ms = []
    for t in range(T):
        h = s.copy()
        for ax in range(3):
            h += np.roll(s, 1, axis=ax) + np.roll(s, -1, axis=ax)
        s = sample_sphere_exp(h.reshape(-1, 3), beta, rng).reshape(L, L, L, 3)
        if t >= T // 2:
            ms.append(np.linalg.norm(s.mean(axis=(0, 1, 2))))
    return float(np.mean(ms))


def w3():
    print("W3: independent light-cone formation simulator, plateau |m| (aligned start, second half of T levels)")
    for L, T in ((24, 1600), (32, 1600)):
        row = []
        for beta in (0.55, 0.58, 0.60, 0.62, 0.65):
            row.append(f"beta={beta}: {light_cone_run(L, beta, T, seed=L + int(beta * 100)):.4f}")
        print(f"  L={L}, T={T}: " + "; ".join(row), flush=True)


def main():
    w1()
    w2()
    w3()


if __name__ == "__main__":
    sys.exit(main())
