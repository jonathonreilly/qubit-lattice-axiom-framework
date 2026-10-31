#!/usr/bin/env python3
"""Lemma 1 of library/curl-poincare-exterior.md, on a lattice box.

Pre-registered criteria.
PASS requires, for d = 3, 4 and N up to the limits below, for random H, for H a
gradient plus a small random field, and for H a smooth wave:
 (a) the identity H_i - d_i omega = avg_y sum_{j>i} S [curl_ji] holds at every
     bond with sup error below 1e-10;
 (b) ||H - d omega||_2 <= sqrt(2 (d-1)) l ||curl H||_2, with l = (N-1) eta.
FAIL on any violation. Self-limits RSS to 2 GB.
"""
import math
import resource
import sys

import numpy as np

resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, resource.RLIM_INFINITY)) if sys.platform != "darwin" else None


def rss_ok():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 2 * 1024**3


def d_axis(f, axis, eta):
    return np.diff(f, axis=axis) / eta


def prefix(f, axis, eta):
    """s -> eta sum_{t<s} f(t) along axis, with length one greater on that axis."""
    c = np.cumsum(f, axis=axis) * eta
    shape = list(c.shape)
    shape[axis] = 1
    return np.concatenate([np.zeros(shape), c], axis=axis)


def path_term(P, j, d):
    """avg_{y>j} P(x_{<j}, x_j, y_{>j}) - avg_{y>=j} P, with kept axes."""
    axes = tuple(range(j + 1, d))
    T = P.mean(axis=axes, keepdims=True) if axes else P
    return T - T.mean(axis=j, keepdims=True)


def omega_of(H, d, eta):
    w = 0.0
    for j in range(d):
        w = w + path_term(prefix(H[j], j, eta), j, d)
    return w


def curl(H, j, i, eta):
    """curl_ji := d_j H_i - d_i H_j."""
    return d_axis(H[i], j, eta) - d_axis(H[j], i, eta)


def rhs(H, i, d, eta, N):
    shape = [N] * d
    shape[i] = N - 1
    out = np.zeros(shape)
    for j in range(i + 1, d):
        out = out + path_term(prefix(curl(H, j, i, eta), j, eta), j, d)
    return out


def norm2(f, d, eta):
    return float((f**2).sum() * eta**d)


def run_field(H, d, N, eta):
    w = omega_of(H, d, eta)
    err = 0.0
    rem2 = 0.0
    for i in range(d):
        lhs = H[i] - d_axis(w, i, eta)
        err = max(err, float(np.abs(lhs - rhs(H, i, d, eta, N)).max()))
        rem2 += norm2(lhs, d, eta)
    curl2 = 0.0
    for i in range(d):
        for j in range(i + 1, d):
            curl2 += norm2(curl(H, j, i, eta), d, eta)
    l = (N - 1) * eta
    bound = math.sqrt(2 * (d - 1)) * l * math.sqrt(curl2)
    return err, math.sqrt(rem2), bound


def fields(d, N, eta, rng):
    shapes = []
    for i in range(d):
        s = [N] * d
        s[i] = N - 1
        shapes.append(s)
    yield "random", [rng.standard_normal(s) for s in shapes]
    g = rng.standard_normal([N] * d)
    yield "grad+small", [d_axis(g, i, eta) + 1e-3 * rng.standard_normal(shapes[i]) for i in range(d)]
    coords = np.meshgrid(*[np.arange(N) * eta] * d, indexing="ij")
    wave = np.sin(2.0 * coords[0] + 1.0) * np.cos(3.0 * coords[-1])
    H = []
    for i in range(d):
        idx = [slice(None)] * d
        idx[i] = slice(0, N - 1)
        H.append(wave[tuple(idx)] * (i + 1))
    yield "wave", H


def main():
    rng = np.random.default_rng(20261030)
    ok = True
    for d, Ns in ((3, (3, 5, 9, 17)), (4, (3, 5, 9))):
        for N in Ns:
            eta = 1.0 / (N - 1)
            for name, H in fields(d, N, eta, rng):
                err, rem, bound = run_field(H, d, N, eta)
                good = err < 1e-10 and rem <= bound
                ok = ok and good
                print(f"d={d} N={N:3d} {name:10s} err={err:.2e} rem={rem:.4e} bound={bound:.4e} ratio={rem/bound:.3f} {'ok' if good else 'VIOLATION'}")
    if not rss_ok():
        print("RSS over 2 GB")
        ok = False
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
