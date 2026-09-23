#!/usr/bin/env python3
"""Supervisor control for block 94 (floating point; evidence, not proof).

W1: reading (i) (Z^3 read as spacetime, level order): the linear field of a source at rest (its worldline along (1,1,1), present every third
    level) in the level plane, Phi(y) = sum_n P_{3n}(y + (n, n)), P_m the m-step law of the level walk with steps 0, e1, e2 (1/3 each).
    The difference Phi(0) - Phi(y) against log|y|: a two-dimensional potential (slope sqrt(3)/pi in the walk's own metric), and the
    reflection-odd part Phi(y) - Phi(-y) along the three step directions and along the mirror lines.
W2: reading (ii)/(iii) geometry: the three-dimensional lattice Green function difference G(0) - G(r) against 1/r (the same test in 3D).
"""
import math
import sys

import numpy as np
from scipy.special import gammaln


def P(m, b, c):
    a = m - b - c
    if b < 0 or c < 0 or a < 0:
        return 0.0
    return math.exp(gammaln(m + 1) - gammaln(a + 1) - gammaln(b + 1) - gammaln(c + 1) - m * math.log(3))


def phi_diff(y, nmax):
    """Phi(0) - Phi(y) summed over the worldline to n = nmax."""
    return sum(P(3 * n, n, n) - P(3 * n, y[0] + n, y[1] + n) for n in range(1, nmax + 1))


def odd(y, nmax):
    return sum(P(3 * n, y[0] + n, y[1] + n) - P(3 * n, -y[0] + n, -y[1] + n) for n in range(1, nmax + 1))


def main():
    nmax = 6000
    print("W1: reading (i), resting source in the level plane (sums to n = %d)" % nmax)
    print("  along the mirror line (k, -k): Phi(0) - Phi(y), and its slope against log k (expected sqrt(3)/pi = %.4f)" % (math.sqrt(3) / math.pi))
    prev = None
    for k in (1, 2, 4, 8, 16):
        d = phi_diff((k, -k), nmax)
        line = f"    k={k:2d}: {d:.5f}"
        if prev is not None:
            line += f"   slope per log step {(d - prev[1]) / math.log(k / prev[0]):.4f}"
        print(line)
        prev = (k, d)
    print("  reflection-odd part Phi(y) - Phi(-y):")
    for y in ((1, 1), (2, 2), (4, 4), (1, 0), (2, -1), (4, -2)):
        print(f"    y={y}: {odd(y, nmax):+.5f}")
    print("W2: 3D lattice Green function (inverse lattice Laplacian) difference G(0) - G(r e1) against 1/r, by quadrature of the resolvent")
    from scipy import integrate, special
    def G(r):
        f = lambda t: special.ive(r, 2 * t) * special.ive(0, 2 * t) ** 2
        return integrate.quad(f, 0, np.inf, limit=400, epsabs=1e-13)[0]
    G0 = G(0)
    for r in (1, 2, 4, 8, 16):
        g = G(r)
        print(f"    r={r:2d}: G(r) = {g:.6f}, r G(r) = {r * g:.5f} (1/(4 pi) = {1 / (4 * math.pi):.5f})")


if __name__ == "__main__":
    sys.exit(main())
