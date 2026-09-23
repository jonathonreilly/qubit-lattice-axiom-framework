#!/usr/bin/env python3
"""Supervisor control for block 92 (floating point; evidence, not proof).

W1: light-cone formation on PLANES (five predecessors: x and x +- e_j, j = 1, 2; block 19's rule on the sphere, exact sampling by inversion):
    aligned start, plateau |m| over the second half of T levels, sides 16 to 128, beta = 1, 2, 4. The theorem says the plateau tends to 0 as
    the side grows, at every beta; the bound itself is qualitative (it bites only when H_(L/2 - 1) exceeds 6 pi^2 beta + 1/2).
W2: the zero-field floors in 3+1, ((1 - beta_0/beta)/3)^2, against block 91's measured response R^(k)E(k).
W3: where the plane bound starts to bite: the side L at which H_(L/2 - 1) = 6 pi^2 beta + 1/2.
"""
import math
import sys

import numpy as np


def sample_sphere_exp(V, U, ph):
    kap = np.linalg.norm(V, axis=1)
    kap = np.where(kap < 1e-12, 1e-12, kap)
    uu = V / kap[:, None]
    w = np.clip(1.0 + np.log(U + (1.0 - U) * np.exp(-2.0 * kap)) / kap, -1.0, 1.0)
    a = np.where((np.abs(uu[:, 0]) < 0.9)[:, None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
    b1 = a - (a * uu).sum(1)[:, None] * uu
    b1 /= np.linalg.norm(b1, axis=1)[:, None]
    b2 = np.cross(uu, b1)
    r = np.sqrt(np.clip(1 - w * w, 0, 1))
    return w[:, None] * uu + r[:, None] * (np.cos(ph)[:, None] * b1 + np.sin(ph)[:, None] * b2)


def plane_run(L, beta, T, seed):
    rng = np.random.default_rng(seed)
    N = L * L
    s = np.zeros((L, L, 3))
    s[..., 2] = 1.0
    ms = []
    for t in range(T):
        S = s.copy()
        for ax in range(2):
            S += np.roll(s, 1, axis=ax) + np.roll(s, -1, axis=ax)
        s = sample_sphere_exp(beta * S.reshape(-1, 3), rng.random(N), 2 * np.pi * rng.random(N)).reshape(L, L, 3)
        if t >= T // 2:
            ms.append(np.linalg.norm(s.mean(axis=(0, 1))))
    return float(np.mean(ms))


def main():
    print("W1: light-cone formation on planes, plateau |m| (aligned start, second half of T = 2000 levels)")
    for beta in (1.0, 2.0, 4.0):
        row = []
        for L in (16, 32, 64, 128):
            row.append(f"L={L}: {plane_run(L, beta, 2000, seed=L + int(10 * beta)):.4f}")
        print(f"  beta={beta}: " + "; ".join(row), flush=True)
    beta0 = 0.5904937470
    print("W2: zero-field floors ((1 - beta_0/beta)/3)^2 in 3+1 against block 91's measured R^(k)E(k) (0.94, 0.96, 0.98 at beta = 1, 2, 3)")
    for beta in (1.0, 2.0, 3.0, 6.0, 1e9):
        print(f"  beta={beta:g}: floor {((1 - beta0 / beta) / 3) ** 2:.5f}")
    print("W3: the plane bound M^4 <= (6 pi^2 beta + 1/2)/H_(L/2 - 1) bites (right side < 1) only when H_(L/2 - 1) > 6 pi^2 beta + 1/2:")
    for beta in (0.1, 1.0, 2.0):
        target = 6 * math.pi ** 2 * beta + 0.5
        # H_n ~ ln n + 0.5772: n ~ exp(target - 0.5772)
        print(f"  beta={beta}: needs H > {target:.2f}, i.e. L/2 of order exp({target - 0.5772:.1f}) = {math.exp(target - 0.5772):.3g}")


if __name__ == "__main__":
    sys.exit(main())
