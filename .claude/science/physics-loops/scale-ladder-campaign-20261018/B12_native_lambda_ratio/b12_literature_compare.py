#!/usr/bin/env python3
"""B12 (G): compare with Hasenfratz & Hasenfratz (1980) Wilson->MSbar one-loop shift (LITERATURE INPUT,
quoted from memory, standard form): ln(Lambda_W/Lambda_MS) = (1/(2b0)) [1/(8N) - 0.16995599 N].
Checks the literature form against the textbook ratios 28.81 (SU3), 19.82 (SU2), then composes with
this campaign's c(4) = (3-N^2)/(24N) to get Lambda_MS/Lambda_HK."""
import math
FAIL = []
for N, lit in ((2, 19.82), (3, 28.81)):
    b0 = 11 * N / (48 * math.pi ** 2)
    lnW = (1 / (8 * N) - 0.16995599 * N) / (2 * b0)
    ok = abs(math.exp(-lnW) - lit) < 0.01
    print(f"{'PASS' if ok else 'FAIL'}: SU({N}) Lambda_MS/Lambda_W = {math.exp(-lnW):.3f} (textbook {lit})")
    FAIL += [] if ok else [N]
    c = (3 - N * N) / (24 * N)
    lnHK = lnW - c / (2 * b0)
    print(f"      SU({N}) Lambda_MS/Lambda_HK = {math.exp(-lnHK):.4f};  ln(Lambda_HK/Lambda_MS)*2b0/N = {lnHK*2*b0/N:.8f}")
lead = 1 / 24 - 0.16995599
algebra = all(abs((1/(8*N) - (3-N*N)/(24*N)) - N/24) < 1e-15 for N in range(2, 50))
print(f"{'PASS' if algebra else 'FAIL'}: 1/(8N) - c(4) = 1/(8N) - (3-N^2)/(24N) = N/24 for N=2..49 (non-planar Wilson term cancels); slope = {lead:.8f}")
FAIL += [] if algebra else ['algebra']
for N in (2, 3, 4, 10):
    b0 = 11 * N / (48 * math.pi ** 2)
    print(f"      N={N}: Lambda_MS/Lambda_HK = {math.exp(-N*lead/(2*b0)):.4f} (N-independent)")
print("SUMMARY:", "ALL PASS" if not FAIL else f"FAIL {FAIL}")
