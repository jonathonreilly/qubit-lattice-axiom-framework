"""Lane A8 helpers: exact Z^3 lattice Green function (same method as lane G's g1) and lump geometry.

G solves -Delta G = delta on Z^3 with Delta f(x) = sum_{y~x} (f(y) - f(x)).
G(x) = int_0^inf prod_i ive(x_i, 2t) dt  (validated in g1 against Watson/6 to 6e-13).
"""
import os
for _k in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[_k] = "1"
import numpy as np
from scipy.special import ive
from scipy.integrate import quad

PREF = (4 * np.pi) ** -1.5
_cache = {}


def G(x):
    a, b, c = sorted(abs(int(v)) for v in x)
    key = (a, b, c)
    if key in _cache:
        return _cache[key]
    r2 = a * a + b * b + c * c
    T = max(4000.0, 60.0 * r2)
    f = lambda t: ive(a, 2 * t) * ive(b, 2 * t) * ive(c, 2 * t)
    edges = [0.0] + list(np.geomspace(0.25, T, 24))
    val = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        v, _ = quad(f, lo, hi, limit=200, epsabs=1e-15, epsrel=1e-12)
        val += v
    s = (4 * a * a - 1) + (4 * b * b - 1) + (4 * c * c - 1)
    tail = PREF * (2 * T ** -0.5 - (s / 16.0) * (2.0 / 3.0) * T ** -1.5)
    _cache[key] = val + tail
    return _cache[key]


def Gmat(B):
    P = np.array(B)
    n = len(P)
    M = np.empty((n, n))
    for i in range(n):
        dif = P - P[i]
        for j in range(i, n):
            M[i, j] = M[j, i] = G(dif[j])
    return M


def cube(s):
    r = range(s)
    return [(i, j, k) for i in r for j in r for k in r]


def ball(R):
    m = int(np.ceil(R))
    return [(i, j, k) for i in range(-m, m + 1) for j in range(-m, m + 1) for k in range(-m, m + 1)
            if i * i + j * j + k * k <= R * R + 1e-9]


def sub_ball(R, d):
    """records on the spacing-d sublattice inside a ball of radius R (filling n = 1/d^3)."""
    m = int(np.ceil(R / d))
    out = []
    for i in range(-m, m + 1):
        for j in range(-m, m + 1):
            for k in range(-m, m + 1):
                if (d * i) ** 2 + (d * j) ** 2 + (d * k) ** 2 <= R * R + 1e-9:
                    out.append((d * i, d * j, d * k))
    return out
