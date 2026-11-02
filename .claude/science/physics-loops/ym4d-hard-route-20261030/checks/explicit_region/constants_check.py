#!/usr/bin/env python3
"""Numerical sanity check of the elementary constants in Lemma TYP and Lemma RARE.

Guides only: both lemmas are proved by hand in library/explicit-region-two-step.md.

Registered pass criteria, written before the run:
  P1  E[1 - u] >= 1/(8 k) for k on a log grid in [1, 1e5], density sqrt(1-u^2) exp(k u).
  P2  P(phi > T) >= (T^3/12) exp(-2 k T^2) for k in [1, 6x], T in (0, 1/2], density sin^2(phi) exp(k cos phi).
  P3  P(phi > T) >= (T^3/12) exp(-12 x T^2) for k in (0, 1), x >= 1.
  P4  0.13/(0.13 + 0.334) >= 1/4, and the printed constants of (2.1).
Any failure is printed and the exit code is 1.
"""
import math, resource, sys
import numpy as np

resource.setrlimit(resource.RLIMIT_AS, (2 * 2**30, 2 * 2**30)) if sys.platform != "darwin" else None

def rss_guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 2 * 2**30:
        sys.exit("RSS above 2 GB, stopping")

N = 400001
fails = 0

# Grid in phi on [0, pi]; u = cos(phi), so du = sin(phi) dphi and sqrt(1-u^2) du = sin^2(phi) dphi.
phi = np.linspace(0.0, math.pi, N)
d = phi[1] - phi[0]
sin2 = np.sin(phi) ** 2
cosp = np.cos(phi)

worst1 = math.inf
for k in np.logspace(0, 5, 61):
    # work in exp(k(cos - 1)) to avoid overflow; refine near phi = 0 by the fine grid
    w = sin2 * np.exp(k * (cosp - 1.0))
    mean = np.trapezoid(w * (1.0 - cosp), dx=d) / np.trapezoid(w, dx=d)
    ratio = mean * 8.0 * k
    worst1 = min(worst1, ratio)
    if ratio < 1.0:
        print("P1 FAIL", k, ratio); fails += 1
print(f"P1 worst of 8 k E[1-u] = {worst1:.4f} (need >= 1; large-k limit is 8 * 3/(2) * ... )")
rss_guard()

worst2 = math.inf
for x in [1.0, 3.0, 10.0, 30.0, 100.0, 1000.0]:
    for k in np.logspace(0, math.log10(6 * x), 25):
        w = sin2 * np.exp(k * (cosp - 1.0))
        c = np.cumsum(w) * d
        total = c[-1]
        for T in [0.5, 0.3, 0.1, 0.03, 0.01]:
            i = int(T / d)
            tail = (total - c[i]) / total
            floor = T**3 / 12.0 * math.exp(-2.0 * k * T * T)
            if tail > 0 and floor > 0:
                r = tail / floor
                worst2 = min(worst2, r)
                if r < 1.0:
                    print("P2 FAIL", x, k, T, tail, floor); fails += 1
print(f"P2 worst ratio tail / floor = {worst2:.4f} (need >= 1)")
rss_guard()

worst3 = math.inf
for k in [1e-3, 0.1, 0.5, 0.999]:
    w = sin2 * np.exp(k * cosp)
    c = np.cumsum(w) * d
    for T in [0.5, 0.3, 0.1]:
        i = int(T / d)
        tail = (c[-1] - c[i]) / c[-1]
        r = tail / (T**3 / 12.0 * math.exp(-12.0 * T * T))
        worst3 = min(worst3, r)
        if r < 1.0:
            print("P3 FAIL", k, T); fails += 1
print(f"P3 worst ratio = {worst3:.4f} (need >= 1)")

a = 0.13 / (0.13 + 0.334)
print(f"P4 0.13/(0.13+0.334) = {a:.4f}; 1/(2 sqrt2 e) = {1/(2*math.sqrt(2)*math.e):.4f}; 16 pi^-2.5 (2/pi^2)^1.5 = {16*math.pi**-2.5*(2/math.pi**2)**1.5:.5f} vs 1/12 = {1/12:.5f}")
if a < 0.25 or 1 / (2 * math.sqrt(2) * math.e) < 0.13 or 16 * math.pi**-2.5 * (2 / math.pi**2) ** 1.5 < 1 / 12:
    print("P4 FAIL"); fails += 1

# (2.1): sample K_0 and n q on the flow, in logs, with the actual slope.
for L, xK, T in [(3, 50.0, 0.5), (5, 100.0, 0.1), (61, 400.0, 0.02)]:
    B = 0.372 * math.log(L)
    assert 12 * B * T * T <= 2 * math.log(L)
    K0 = (6 * xK * T * T + math.log(192 / T**3)) / math.log(L)
    print(f"L={L} x_K={xK} T={T}: K_0 = {K0:.1f}; log(nq) at 2 K_0 = {2*2*K0*math.log(L)/2 - 12*xK*T*T + math.log(T**3/192):.1f}")

print("RESULT", "PASS" if fails == 0 else f"FAIL ({fails})")
sys.exit(0 if fails == 0 else 1)
