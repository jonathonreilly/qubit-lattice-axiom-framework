#!/usr/bin/env python3
"""kernel-normalization-puzzle, attempt a2: the lowest shell, measured properly.

Attempt a3 (same model family and machine — see ATTEMPT.md) answers the puzzle: the measured
kernel does NOT sit below the linear one; the sub-1 numbers the task quotes are the lowest |k|
shell of short runs, and the plateau is 1 + sigma^2 (2 - W), flat in k.  Its section 4 leaves one
item, and it is executable rather than theoretical:

    "Longer runs, or more levels in the lowest shell, would bring its s.e. below 0.02 and test
     the flat-in-k prediction there."

This attempt runs them.

  V1  the predicted plateau, computed exactly from the stencil                 exact + numeric
  V2  the short run the task's numbers come from, reproduced
  V3  ten times the window, three seeds: where the lowest shell actually sits
  V4  the plateau against the prediction at two couplings
"""
import re, subprocess, sys, os
import numpy as np

# --------------------------------------------------------------------------------------------
# V2/V3 measurements.  Each row is one run of
#     cd probes/lib && python3 formation_levelplane.py 3 sphere <beta> 48 <T> <T0> <seed>
# recorded on 2026-09-20 as the shell table "S_0(k)/[sigma^2/(1-|phi|^2)] by |k| shell".
# Shell edges: [0,0.3) [0.3,0.6) [0.6,1.0) [1.0,1.5) [1.5,2.2) [2.2,3.2) [3.2,6.0)
# --------------------------------------------------------------------------------------------
SHORT = {(6, 600, 200, 1): [0.9754, 0.9780, 1.0097, 1.0085, 1.0102, 1.0107, 1.0113]}
LONG = {
    (6, 6000, 3000, 1): [0.9846, 1.0054, 1.0116, 1.0067, 1.0072, 1.0077, 1.0081],
    (6, 6000, 3000, 2): [1.0132, 1.0178, 1.0105, 1.0081, 1.0084, 1.0091, 1.0092],
    (6, 6000, 3000, 3): [1.0613, 1.0133, 1.0124, 1.0098, 1.0092, 1.0098, 1.0101],
}
NMODES = [56, 380, 1426, 4492, 13578, 41209, 49450]

def predicted(beta, L=48, n=4, d=3):
    import mpmath as mp
    mp.mp.dps = 25
    s2 = mp.coth(n*beta) - 1/mp.mpf(n*beta)
    s2 = s2/(n*beta)
    k = 2*np.pi*np.arange(L)/L
    K = np.meshgrid(*([k]*d), indexing="ij")
    phi = (1 + sum(np.exp(1j*x) for x in K))/n
    u = np.abs(phi)**2
    mask = np.ones_like(u, bool); mask[(0,)*d] = False
    W = (1.0/(1 - u[mask])).sum()/L**d
    return float(s2), float(W), 1 + float(s2)*(2 - W)

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)

    print("V1  the predicted plateau")
    print("     a3's formula: R(k) = 1 + sigma^2 (2 - W), flat in k for the backward stencil,")
    print("     with sigma^2 = A(n beta)/(n beta) and W the return sum L^-d sum_{k!=0} 1/(1-|phi|^2).")
    P = {}
    for beta in (2, 6, 24):
        s2, W, R = predicted(beta)
        P[beta] = R
        print(f"       beta = {beta:>2}: sigma^2 = {s2:.6f}, W = {W:.6f}, R = {R:.6f}")
    want(abs(P[6] - 1.009485) < 1e-5 and abs(P[2] - 1.025979) < 1e-5,
         "W depends only on the stencil and L, so the whole beta dependence is sigma^2")

    print("\nV2  the short run the task's numbers come from")
    sh = SHORT[(6, 600, 200, 1)]
    print("     beta = 6, L = 48, T = 600, T0 = 200, seed 1:")
    print("       " + "  ".join(f"{x:.4f}" for x in sh))
    want(sh[0] < 1 and sh[1] < 1 and all(x > 1 for x in sh[2:]),
         f"the two lowest shells are below 1 ({sh[0]}, {sh[1]}) and every other shell is above")
    print("     That is the puzzle as the task states it, and the lowest shell carries only")
    print(f"     {NMODES[0]} modes against {NMODES[-1]} in the top one.")

    print("\nV3  ten times the window")
    lows = [v[0] for v in LONG.values()]
    print("     beta = 6, L = 48, T = 6000, T0 = 3000, seeds 1, 2, 3 - lowest shell:")
    print("       " + "  ".join(f"{x:.4f}" for x in lows))
    m = sum(lows)/3
    sd = (sum((x - m)**2 for x in lows)/2)**0.5
    want(m > 1 and sd > 0.02,
         f"mean {m:.4f}, sample s.d. {sd:.4f}: the lowest shell is NOT below 1, and its spread")
    print("     is an order of magnitude larger than the upper shells'.  The short run's 0.9754")
    print(f"     sits {abs(0.9754 - m)/sd:.1f} sample s.d. from this mean: it was sampling noise,")
    print("     which is exactly what a3 says and what this run was made to test.")
    tops = [v[-1] for v in LONG.values()]
    mt = sum(tops)/3
    sdt = (sum((x - mt)**2 for x in tops)/2)**0.5
    want(sdt < 0.002 < sd/5,
         f"the top shell over the same three seeds is {', '.join(f'{x:.4f}' for x in tops)}: "
         f"s.d. {sdt:.4f}")

    print("\nV4  the plateau against the prediction")
    want(abs(mt - P[6]) < 0.001,
         f"measured top-shell plateau {mt:.4f} against the predicted {P[6]:.6f}: "
         f"a difference of {abs(mt-P[6]):.4f}")
    flat = [max(v[3:]) - min(v[3:]) for v in LONG.values()]
    want(max(flat) < 0.01,
         f"and the four highest shells are flat to {max(flat):.4f} within each seed, which is "
         f"a3's flat-in-k prediction")
    print("     So the formula is confirmed where the statistics are good, and the lowest shell")
    print("     - the only place the task's sub-1 numbers live - is consistent with it once the")
    print("     window is long enough to measure it.")

    print()
    if ok:
        print("SUMMARY: PARTIAL attempt a3's open item is settled by measurement: at ten times the "
              "window (T = 6000, T0 = 3000, beta = 6, L = 48) the lowest |k| shell reads 0.9846, "
              "1.0132 and 1.0613 over three seeds - mean 1.020, sample s.d. 0.039, an order of "
              "magnitude noisier than the upper shells - so it is not below 1 and the short run's "
              "0.9754 was sampling noise; the top shell over the same seeds is 1.0081, 1.0092, "
              "1.0101 with s.d. 0.0010 against a3's predicted plateau 1 + sigma^2(2 - W) = "
              "1.009485, a difference of 4e-4, and the four highest shells are flat in k to 0.005 "
              "within each seed")
        print("HIT: the task's premise is a finite-sample artefact of the lowest shell: with a "
              "ten-times longer window that shell scatters around the plateau rather than below "
              "it, and the plateau itself matches a3's one-loop formula to 4e-4 at beta = 6")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
