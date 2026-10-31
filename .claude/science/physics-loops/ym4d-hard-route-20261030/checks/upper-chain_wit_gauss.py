#!/usr/bin/env python3
"""Criteria W1-W3: normalized plaquette covariance P_pq of the Wilson Gaussian theory.

P_pq(x) = T^-4 sum_k exp(i k.x) [d_m d*_r delta_ns - d_m d*_s delta_nr - d_n d*_r delta_ms + d_n d*_s delta_mr] / khat^2,
with d_m = exp(i k_m) - 1, for plaquettes in the planes (m,n) at 0 and (r,s) at x. Usage: upper-chain_wit_gauss.py T
"""
import os
import resource
import sys

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np


def kernel(T, m, n, r, s):
    k = 2 * np.pi * np.fft.fftfreq(T)
    K = np.meshgrid(k, k, k, k, indexing="ij")
    d = [np.exp(1j * c) - 1 for c in K]
    khat2 = sum(np.abs(c) ** 2 for c in d)
    khat2[0, 0, 0, 0] = 1.0
    out = np.zeros((T, T, T, T), dtype=complex)
    if n == s:
        out += d[m] * np.conj(d[r])
    if n == r:
        out -= d[m] * np.conj(d[s])
    if m == s:
        out -= d[n] * np.conj(d[r])
    if m == r:
        out += d[n] * np.conj(d[s])
    out /= khat2
    out[0, 0, 0, 0] = 0.0
    return np.fft.ifftn(out).real


def tensor(x, m, n, r, s):
    x = np.array(x, dtype=float)
    x2 = np.sum(x**2)
    dl = lambda a, b: 1.0 if a == b else 0.0
    br = dl(m, r) * dl(n, s) - dl(m, s) * dl(n, r)
    q = x[m] * x[r] * dl(n, s) - x[m] * x[s] * dl(n, r) - x[n] * x[r] * dl(m, s) + x[n] * x[s] * dl(m, r)
    return (br - 2 * q / x2) / (np.pi**2 * x2**2)


def main(T):
    P12 = kernel(T, 0, 1, 0, 1)
    P13 = kernel(T, 0, 1, 0, 2)
    print(f"P_pp(1,2) = {P12[0,0,0,0]:.6f}")
    # W3: P^2 = P on one plaquette, summing over all six planes
    tot = 0.0
    planes = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    for (r, s) in planes:
        tot += np.sum(kernel(T, 0, 1, r, s) ** 2)
    print(f"sum_q P_pq^2 = {tot:.6f}, P_pp = {P12[0,0,0,0]:.6f}, difference = {tot - P12[0,0,0,0]:.2e}")
    ok3 = abs(tot - P12[0, 0, 0, 0]) < 1e-6 and abs(P12[0, 0, 0, 0] - 0.5) < 1e-3
    ratios = {}
    for d in (3, 4, 5, 6):
        x = (d, d, 2 * d, 2 * d)
        val = P12[x]
        pred = tensor(x, 0, 1, 0, 1)
        ratios[d] = val / pred
        print(f"d={d} offset {x}: P = {val:.4e}, prediction {pred:.4e}, ratio {val/pred:.4f}")
    ok1 = all(r > 0 for r in ratios.values()) and abs(ratios[6] - 1) <= 0.25 and abs(ratios[6] - 1) < abs(ratios[3] - 1)
    x = (6, 6, 6, 6)
    par, ort = P12[x], P13[x]
    print(f"offset {x}: parallel {par:.4e}, (1,2),(1,3) {ort:.4e}, prediction {tensor(x,0,1,0,2):.4e}, parallel prediction {tensor(x,0,1,0,1):.4e}")
    ok2 = abs(par) <= 0.1 * abs(ort)
    print("RSS GB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9)
    print("RESULT", "W1", "PASS" if ok1 else "FAIL", "W2", "PASS" if ok2 else "FAIL", "W3", "PASS" if ok3 else "FAIL")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 48)
