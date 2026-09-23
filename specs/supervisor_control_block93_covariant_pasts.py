#!/usr/bin/env python3
"""Supervisor control for block 93 (floating point; evidence, not proof).

W1: infinite-volume thresholds beta_0(w_0, w_1) = (3/(2 w_1))(I(0) + I(2 w_0/w_1)), I(a) = int d^3k/(2 pi)^3 1/(E(k) + a), by quadrature;
    the six neighbours alone: 3 I(0)/w_1; the record below alone: never.
W2: the six-neighbour past decouples a level's even and odd sites; all seven couple them. Start a level with even sites along z and odd sites
    along x; run the formation law (block 19's rule on the sphere, exact sampling) and follow the cosine between the even-site mean and the
    odd-site mean of the current level; 16^3, beta = 1.5 (w_0 = 0 and w_0 = 1, w_1 = 1), 400 levels.
"""
import math
import sys

import numpy as np
from scipy import integrate, special


def I(a):
    f = lambda t: special.ive(0, 2 * t) ** 3 * math.exp(-a * t)
    return integrate.quad(f, 0, np.inf, limit=400, epsabs=1e-14, epsrel=1e-13)[0]


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


def run(L, beta, w0, w1, T, seed):
    rng = np.random.default_rng(seed)
    N = L ** 3
    idx = np.indices((L, L, L)).sum(0) % 2
    s = np.zeros((L, L, L, 3))
    s[idx == 0, 2] = 1.0
    s[idx == 1, 0] = 1.0
    out = []
    for t in range(T):
        S = w0 * s
        for ax in range(3):
            S = S + w1 * (np.roll(s, 1, axis=ax) + np.roll(s, -1, axis=ax))
        s = sample_sphere_exp(beta * S.reshape(-1, 3), rng.random(N), 2 * np.pi * rng.random(N)).reshape(L, L, L, 3)
        if t + 1 in (1, 2, 5, 10, 25, 50, 100, 200, 400):
            me = s[idx == 0].mean(0)
            mo = s[idx == 1].mean(0)
            out.append(f"t={t + 1}: |m_even|={np.linalg.norm(me):.3f} |m_odd|={np.linalg.norm(mo):.3f} cos={me @ mo / (np.linalg.norm(me) * np.linalg.norm(mo)):+.3f}")
    return out


def main():
    print("W1: infinite-volume thresholds")
    I0 = I(0.0)
    for w0, w1 in ((1, 1), (1, 2), (2, 1)):
        print(f"  (w_0, w_1) = ({w0}, {w1}): beta_0 = {1.5 / w1 * (I0 + I(2 * w0 / w1)):.6f}")
    print(f"  six neighbours alone (w_0 = 0, w_1 = 1): 3 I(0) = {3 * I0:.6f}; record below alone: no memory")
    print("W2: even and odd sites of a level, started orthogonal (even along z, odd along x), 16^3, beta = 1.5")
    for w0 in (0, 1):
        print(f"  w_0 = {w0}, w_1 = 1:")
        for line in run(16, 1.5, w0, 1, 400, seed=93 + w0):
            print("    " + line, flush=True)


if __name__ == "__main__":
    sys.exit(main())
