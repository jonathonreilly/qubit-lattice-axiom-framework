#!/usr/bin/env python3
"""Gate independent-core, toy checks. Criteria are registered in
gates/independent-core-16ca92dd7.md before the first run.

A one-dimensional chain. H_1 is strictly local, P a Chebyshev polynomial in H_1
approximating its inverse square root. This tests linear algebra that two
arguments of the attempt lean on. It cannot test the attempt's chart, and it
establishes no bound.

TAIL     d xi_c / d u_j at fixed b, for xi = P_Z^+ b.
CENTRE   Im s / (alpha q) for the centre s = 2^{1/2} P^+ (G_1 xi_1 + G_2 xi_2).
CONTOUR  one variable, a complex centre, modulus bound against shifted contour.
"""
import json
import os
import resource
import sys

import numpy as np

RSS_LIMIT_BYTES = 2 * 1024**3


def guard():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  # bytes on darwin
    if rss > RSS_LIMIT_BYTES:
        sys.exit(f"RSS guard: {rss} bytes, stopping")


def chain(n, m2, u):
    h = np.zeros((n, n), dtype=complex)
    for i in range(n):
        h[i, i] = 2.0 + m2 + u[i]
        if i + 1 < n:
            h[i, i + 1] = h[i + 1, i] = -1.0
    return h


def cheb_coeffs(f, a, b, deg):
    nodes = np.cos(np.pi * (np.arange(deg + 1) + 0.5) / (deg + 1))
    vals = f(0.5 * (b - a) * nodes + 0.5 * (b + a))
    c = np.zeros(deg + 1)
    for k in range(deg + 1):
        c[k] = (2.0 / (deg + 1)) * np.sum(
            vals * np.cos(k * np.arccos(nodes))
        )
    c[0] *= 0.5
    return c


def cheb_matrix(h, c, a, b):
    n = h.shape[0]
    x = (2.0 * h - (a + b) * np.eye(n)) / (b - a)
    t0, t1 = np.eye(n, dtype=complex), x.copy()
    out = c[0] * t0 + c[1] * t1
    for k in range(2, len(c)):
        t0, t1 = t1, 2.0 * x @ t1 - t0
        out = out + c[k] * t1
    return out


def right_inverse(p_z):
    return p_z.T @ np.linalg.inv(p_z @ p_z.T)


def tail_test():
    """Complex step: u_j -> u_j + i h, exact to rounding for an analytic map."""
    deg, m2, nz = 4, 1.0, 90
    n = nz + 2 * deg
    lo, hi = m2 - 0.05, m2 + 4.1
    coeff = cheb_coeffs(lambda x: x ** (-0.5), lo, hi, deg)
    z = np.arange(deg, deg + nz)
    rng = np.random.default_rng(20261031)
    b = rng.normal(size=nz)
    c_site = z[nz // 2]  # middle of Z, in chain indices
    c_row = c_site  # xi has one entry per chain site
    step = 1e-30

    def xi_of(u):
        p = cheb_matrix(chain(n, m2, u), coeff, lo, hi)
        return (right_inverse(p[z, :]) @ b)[c_row]

    base = xi_of(np.zeros(n, dtype=complex))
    rows = []
    for j in range(deg, n - deg):
        u = np.zeros(n, dtype=complex)
        u[j] = 1j * step
        rows.append((abs(j - c_site), abs(xi_of(u).imag) / step))
        guard()
    far = [v for d, v in rows if d > 5 * deg]
    worst = max(far)
    verdict = "FAIL-TAIL-LOCAL" if worst > 1e-13 else "PASS-TAIL-LOCAL"
    by_dist = {}
    for d, v in rows:
        by_dist[d] = max(by_dist.get(d, 0.0), v)
    print(f"TAIL range D = {deg}, |xi_c| = {abs(base):.3e}")
    for d in (0, deg, 2 * deg, 3 * deg, 5 * deg + 1, 8 * deg, 10 * deg):
        if d in by_dist:
            print(f"  distance {d:3d}  max |d xi_c / d u_j| = {by_dist[d]:.3e}")
    print(f"  worst beyond 5 D: {worst:.3e}  {verdict}")
    return {"verdict": verdict, "worst_far": worst,
            "profile": {str(k): by_dist[k] for k in sorted(by_dist)}}


def matrix_fun(a, f):
    w, v = np.linalg.eig(a)
    return (v * f(w)) @ np.linalg.inv(v)


def centre_test():
    deg, m2, n = 6, 0.04, 80  # m2 plays the role of m^2 = L^{-2}
    a_mass = 1.0  # A has a gap, as (COER-G) gives
    lo, hi = a_mass + m2 - 0.05, a_mass + m2 + 4.1
    coeff = cheb_coeffs(lambda x: x ** (-0.5), lo, hi, deg)
    rows = []
    for alpha in (1e-3, 1e-2):
        for q in (1.0, 10.0, 100.0):
            u = 1j * alpha * np.ones(n)
            a = chain(n, a_mass, u)  # A(W), W complex
            c1half = matrix_fun(a + m2 * np.eye(n), lambda w: w ** (-0.5))
            ainvhalf = matrix_fun(a, lambda w: w ** (-0.5))
            p = cheb_matrix(a + m2 * np.eye(n), coeff, lo, hi)
            c1half_inv = np.linalg.inv(c1half)
            delta = c1half_inv @ (p @ p.T) @ c1half_inv - np.eye(n)
            root = matrix_fun(np.eye(n) - delta, lambda w: w ** 0.5)
            g1 = 2 ** (-0.5) * c1half @ root
            g2 = np.sqrt(m2) * ainvhalf @ c1half
            pplus = right_inverse(p)
            spike = np.zeros(n)
            spike[n // 2] = q
            s = 2 ** 0.5 * pplus @ (g1 @ np.zeros(n) + g2 @ spike)
            ratio = np.linalg.norm(s.imag) / (alpha * q)
            rows.append({"alpha": alpha, "q": q, "ratio": ratio,
                         "delta": float(np.linalg.norm(delta, 2))})
            print(f"CENTRE alpha {alpha:.0e} q {q:6.1f}  "
                  f"|Im s| / (alpha q) = {ratio:.4f}  ||Delta|| = {rows[-1]['delta']:.3e}")
            guard()
    ratios = [r["ratio"] for r in rows]
    constant = max(ratios) <= 2 * min(ratios) and min(ratios) > 1e-3
    verdict = "FAIL-CENTRE-SMALL" if constant else "PASS-CENTRE-SMALL"
    print(f"  {verdict}")
    return {"verdict": verdict, "rows": rows}


def contour_test():
    p = 12.0
    x, w = np.polynomial.legendre.leggauss(4000)
    x, w = p * x, p * w
    rho = lambda z: np.exp(-z * z / 2) / np.sqrt(2 * np.pi)
    h = lambda z: np.exp(0.01j * z - 0.002 * z * z)
    rows = []
    ok = True
    for y in (0.0, 1.0, 2.0, 3.0, 4.0):
        exact = abs(np.sum(w * rho(x - 1j * y) * h(x)))
        modulus = np.exp(y * y / 2)
        main = np.sum(w * rho(x) * np.abs(h(x + 1j * y)))
        walls = 2 * y * np.exp(-(p * p - y * y) / 2) / np.sqrt(2 * np.pi) * np.exp(0.002 * y * y)
        shifted = main + walls
        rows.append({"y": y, "exact": exact, "modulus_bound": modulus, "shifted_bound": shifted})
        print(f"CONTOUR y {y:.1f}  |I| = {exact:.6f}  modulus bound {modulus:.3e}  shifted {shifted:.6f}")
        ok = ok and exact <= 1.05 and exact <= shifted * (1 + 1e-9)
    last = rows[-1]
    ok = ok and last["modulus_bound"] >= 1e3 * last["shifted_bound"]
    verdict = "PASS-CONTOUR" if ok else "FAIL-CONTOUR"
    print(f"  {verdict}")
    return {"verdict": verdict, "rows": rows}


def main():
    print("blas threads", os.environ.get("VECLIB_MAXIMUM_THREADS"), os.environ.get("OPENBLAS_NUM_THREADS"))
    out = {"tail": tail_test(), "centre": centre_test(), "contour": contour_test()}
    out["max_rss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "toy_tail_centre_results.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", path, "rss", out["max_rss_bytes"])


if __name__ == "__main__":
    main()
