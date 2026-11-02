#!/usr/bin/env python3
# checks/nb1_logdiv.py  (T55-E, session 25)
# Criteria: checks/nb1_criteria.md, written BEFORE this script.
# Plain python, integers + floats, no numpy/BLAS.  No numeric lock needed (DRIVE_BRIEF rule 6).
#
# Decides one arithmetic fact: is sum_{x in Z^4, 0<|x|<=R} |x|^{-s} log-divergent at s=4 (claim)
# and convergent at s=5 (designed-FAIL control)?

import math

D = 4
RS = [3, 6, 12, 24]
SS = [4, 5]
RMAX = max(RS)

TWO_PI2_LN2 = 2.0 * math.pi**2 * math.log(2.0)   # 13.6871...  (|S^3| = 2 pi^2)
PI2_OVER_2 = math.pi**2 / 2.0                    # 4.9348...

# enumerate once: squared norms of all x in [-RMAX,RMAX]^4 with 0 < |x| <= RMAX
# accumulate sums at each cutoff R in RS, for each exponent s
sums = {(s, R): 0.0 for s in SS for R in RS}
counts = {R: 0 for R in RS}

RMAX2 = RMAX * RMAX
sq = [i * i for i in range(-RMAX, RMAX + 1)]
cut2 = [(R, R * R) for R in RS]

for a in sq:
    if a > RMAX2:
        continue
    for b in sq:
        ab = a + b
        if ab > RMAX2:
            continue
        for c in sq:
            abc = ab + c
            if abc > RMAX2:
                continue
            for e in sq:
                n2 = abc + e
                if n2 == 0 or n2 > RMAX2:
                    continue
                n = math.sqrt(n2)
                for R, R2 in cut2:
                    if n2 <= R2:
                        counts[R] += 1
                        for s in SS:
                            sums[(s, R)] += n ** (-s)

print("=== nb1: lattice sums of |x|^-s over Z^4 ===")
print("reference constants: 2*pi^2*ln2 = %.6f ; pi^2/2 = %.6f" % (TWO_PI2_LN2, PI2_OVER_2))
print()

for s in SS:
    print("--- s = %d ---" % s)
    for R in RS:
        print("  S_%d(%2d) = %14.6f   (N = %8d)" % (s, R, sums[(s, R)], counts[R]))
    incs = []
    for i in range(len(RS) - 1):
        R = RS[i]
        inc = sums[(s, RS[i + 1])] - sums[(s, R)]
        incs.append(inc)
        print("  delta_%d(%2d->%2d) = %12.6f   (ratio to 2pi^2 ln2 = %8.4f)"
              % (s, R, RS[i + 1], inc, inc / TWO_PI2_LN2))
    # nb1-A criterion, applied to this s
    band_ok = all(abs(x - TWO_PI2_LN2) <= 0.20 * TWO_PI2_LN2 for x in incs[:2])
    nondecay_ok = all(incs[j + 1] >= 0.8 * incs[j] for j in range(min(1, len(incs) - 1)))
    verdict = "PASSES nb1-A criterion" if (band_ok and nondecay_ok) else "FAILS nb1-A criterion"
    print("  band_ok=%s  nondecay_ok=%s  ->  %s" % (band_ok, nondecay_ok, verdict))
    print()

# nb1-C
ratio = counts[RMAX] / float(RMAX ** 4)
print("--- nb1-C geometry sanity ---")
print("  N(%d)/%d^4 = %.6f   target pi^2/2 = %.6f   rel.dev = %.4f"
      % (RMAX, RMAX, ratio, PI2_OVER_2, abs(ratio - PI2_OVER_2) / PI2_OVER_2))
print("  nb1-C: %s" % ("PASS" if abs(ratio - PI2_OVER_2) <= 0.15 * PI2_OVER_2 else "FAIL"))
