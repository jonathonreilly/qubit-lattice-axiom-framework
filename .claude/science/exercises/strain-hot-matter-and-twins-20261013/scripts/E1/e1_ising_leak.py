#!/usr/bin/env python3
"""E1 (A)(a3): leak of covariance against r/a AT criticality, on the Onsager mass shell.
G(r) = int d^2q/(2pi)^2 e^{iq.r} / D(q),  D = cosh2Kx cosh2Ky - sinh2Kx cos qx - sinh2Ky cos qy,
on the critical curve sinh2Kx sinh2Ky = 1 (stretched by u: sinh2Kx = e^u, sinh2Ky = e^-u).
Continuum (metric) form: G(r) - G(0) = -(1/pi) ln|r'| + C0 + O(1/r^2), |r'|^2 = 2 (x^2/sx + y^2/sy).
We print delta(r) = G(r) - G(0) + (1/pi) ln|r'| along x, y and the diagonal; covariance means a
common limit C0 in every direction, and the leak is delta_dir(r) - C0 ~ c_dir / r^2.
q_y (or q_x) is done in closed form; the remaining 1D integral by a 2e6-point midpoint rule.
"""
import numpy as np

def run(u, ns, N=2000000):
    sx, sy = np.exp(u), np.exp(-u)
    C = np.sqrt(1 + sx**2) * np.sqrt(1 + sy**2)
    q = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    out = {}
    for lab, s1, s2 in (("x", sx, sy), ("y", sy, sx)):
        a = C - s1 * np.cos(q); w = 1.0 / np.sqrt(a * a - s2 * s2)
        out[lab] = [np.mean((np.cos(n * q) - 1.0) * w) for n in ns]
        if lab == "x":
            rho = (a - np.sqrt(a * a - s2 * s2)) / s2
            out["d"] = [np.mean((np.cos(n * q) * rho**n - 1.0) * w) for n in ns]
    res = []
    for i, n in enumerate(ns):
        rx = np.sqrt(2 * n * n / sx); ry = np.sqrt(2 * n * n / sy); rd = np.sqrt(2 * n * n * (1 / sx + 1 / sy))
        res.append((n, out["x"][i] + np.log(rx) / np.pi, out["y"][i] + np.log(ry) / np.pi, out["d"][i] + np.log(rd) / np.pi))
    return res

if __name__ == "__main__":
    ns = [2, 4, 8, 16, 32, 64, 128]
    for u in (0.0, 0.3, 0.8):
        print(f"u = {u}  (sinh2Kx = {np.exp(u):.4f}, sinh2Ky = {np.exp(-u):.4f}; metric ratio xi_x/xi_y = {np.exp(u):.4f})")
        res = run(u, ns)
        C0 = res[-1][1]
        print("   n    delta_x          delta_y          delta_diag       n^2(dx-dy)   n^2(dx-dd)")
        for (n, dx, dy, dd) in res:
            print(f"  {n:4d}  {dx:.10f}  {dy:.10f}  {dd:.10f}   {n*n*(dx-dy):+.6f}    {n*n*(dx-dd):+.6f}")
