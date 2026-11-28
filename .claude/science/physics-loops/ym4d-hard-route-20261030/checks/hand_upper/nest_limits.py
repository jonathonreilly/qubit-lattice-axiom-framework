#!/usr/bin/env python3
"""Float test of the limit values quoted in library/upper-chain-by-hand.md, 3.7. A remark only; Theorem N does not use them.

The mode of Theorem N, closed forms, numpy doubles. En by the exact formulas of 3.5, checked exactly in nest_mode_exact.py. Norm by direct sum, with the weight of checks/upper-chain_nest.py.
Criteria, written before the run.
L1. k = 1: at the largest L, Q L within 3 percent of 12 sqrt 3 at X = 2 and of 16 sqrt 3 at X = 4.
L2. k = 2, r = 1: at the largest L, Q L^2 within 10 percent of 48 sqrt 3 at X = 2 and of 64 sqrt 3 at X = 4.

Record of the first run. It printed L1, L2 PASS, and it is void, for two faults of mine. (1) It had no RSS guard and reached 2.76 GB at L = 401, n = 3, above the 2 GB rule of FINISH.md.
(2) The norm gave the edge bond m = 0 the fine weight, where checks/upper-chain_nest.py gives it the coarse one, and it left out the exterior; this showed as Q L = 20.3 at L = 25, below the printed
minimum 20.5, which a trial field cannot be. Fixed: guard below, largest L at n = 3 lowered to 201 for memory only, norm corrected.
L0, added with the fix: at (L, n, k, r, t, X) = (9, 2, 1, 1, 1, 2), (5, 3, 2, 1, 1, 2), (7, 3, 2, 1, 1, 2), Q agrees with nest_mode_exact.out, 2.47863, 2.68430, 1.46745, to 1e-4.
"""
import math
import resource

import numpy as np


RSS_LIMIT_GB = 2.0


def rss_guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9 > RSS_LIMIT_GB:
        raise SystemExit("RSS above limit")


def h(s):
    return (s * s - 1) / (6 * s)


def kap(s):
    return (4 * s * s + 2) / (s * s - 1)


def quotient(L, n, k, r, t, X):
    M = L**n
    if (t + 2) * M * 8 * 6 / 1e9 > 0.8 * RSS_LIMIT_GB:
        raise SystemExit("planned arrays too large")
    s = [L ** (n - k + j) for j in range(k + 1)]
    lo = [0] * k
    hi = [0] * k
    hi[k - 1] = t * M
    for j in range(k - 1, 0, -1):
        lo[j - 1], hi[j - 1] = lo[j] + r * s[j], hi[j] - r * s[j]
    T = (hi[0] - lo[0]) // s[0]
    rho = (kap(s[0]) - math.sqrt(kap(s[0]) ** 2 - 4)) / 2
    i = np.arange(T + 1)
    sign = lambda e: np.where(e % 2 == 0, 1.0, -1.0)
    fi = (sign(i) * rho ** i.astype(float) + sign(T - i) * rho ** (T - i).astype(float)) / (1 + (-rho) ** T)
    tau = (s[0] + 1) / 2 + h(s[0]) * (fi[1] - 1)
    A = 1.0
    pos, val = list(lo[0] + i * s[0]), list(fi)
    for j in range(1, k):
        sg = s[j]
        F = [A, A * (1 - (tau + (sg - 1) / 2) / h(sg))]
        for q in range(1, r):
            F.append(-kap(sg) * F[q] - F[q - 1])
        pos = [lo[j - 1] - q * sg for q in range(r, 0, -1)] + pos + [hi[j - 1] + q * sg for q in range(1, r + 1)]
        val = F[:0:-1] + val + F[1:]
        A = F[r]
        tau = (sg + 1) / 2 + h(sg) * (F[r - 1] / F[r] - 1)
    a = -6 * A * (tau + (M - 1) / 2) / (M * (M * M - 1))
    b = 30 * A * (tau * M + (M - 1) * (M - 2) / 6) / (M * (M * M - 1) * (M * M - 4))
    E = 12 * A * A * (tau + (M - 1) / 2) ** 2 / (M * (M * M - 1)) + 180 * A * A * (tau * M + (M - 1) * (M - 2) / 6) ** 2 / (M * (M * M - 1) * (M * M - 4))
    En = 4 * a * a * M * (M * M - 1) / 3 if X == t + 1 else 2 * E
    m = np.arange(hi[k - 1] + 1, dtype=np.int64)
    f = np.interp(m.astype(float), np.array(pos, dtype=float), np.array(val, dtype=float))
    site = m - 1
    w = np.full(m.shape, float(M))
    for j in range(k - 1, -1, -1):
        w[(site >= lo[j]) & (site < hi[j])] = float(s[j])
    norm = float(np.sum(f * f / w / w))
    # exterior, at the coarse weight; the bond at the far edge m = hi was counted above with the layer's weight, as in that code
    u = np.arange(1, M, dtype=float)
    g = A * (1 - u / M) + a * u * (M - u) + b * u * (M - u) * (2 * u - M)
    if X == t + 1:
        norm += float(np.sum((g + g[::-1]) ** 2)) / M**2
    else:
        norm += 2 * float(np.sum(g * g)) / M**2
    del m, w, site, f, g, u
    rss_guard()
    return En / norm


ok0 = True
for cfg, val in (((9, 2, 1, 1, 1, 2), 2.47863), ((5, 3, 2, 1, 1, 2), 2.68430), ((7, 3, 2, 1, 1, 2), 1.46745)):
    q = quotient(*cfg)
    print(f"L0 {cfg}: Q = {q:.5f}, exact run {val}")
    ok0 = ok0 and abs(q - val) <= 1e-4
print("L0", "PASS" if ok0 else "FAIL")
print("k = 1, t = 1, n = 2:")
res1 = {}
for L in (9, 25, 41, 101, 201, 401, 801):
    res1[L] = (quotient(L, 2, 1, 1, 1, 2) * L, quotient(L, 2, 1, 1, 1, 4) * L)
    print(f"  L = {L}: Q L = {res1[L][0]:.3f} (X = 2), {res1[L][1]:.3f} (X = 4)")
print("k = 2, r = 1, t = 1, n = 3:")
res2 = {}
for L in (9, 25, 41, 101, 201):
    res2[L] = (quotient(L, 3, 2, 1, 1, 2) * L**2, quotient(L, 3, 2, 1, 1, 4) * L**2)
    print(f"  L = {L}: Q L^2 = {res2[L][0]:.3f} (X = 2), {res2[L][1]:.3f} (X = 4)")
r3 = math.sqrt(3)
a = res1[801]
b = res2[201]
print(f"targets {12 * r3:.3f}, {16 * r3:.3f}, {48 * r3:.3f}, {64 * r3:.3f}")
print("L1", "PASS" if abs(a[0] / (12 * r3) - 1) <= 0.03 and abs(a[1] / (16 * r3) - 1) <= 0.03 else "FAIL")
print("L2", "PASS" if abs(b[0] / (48 * r3) - 1) <= 0.10 and abs(b[1] / (64 * r3) - 1) <= 0.10 else "FAIL")
print(f"max RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9:.3f} GB")
