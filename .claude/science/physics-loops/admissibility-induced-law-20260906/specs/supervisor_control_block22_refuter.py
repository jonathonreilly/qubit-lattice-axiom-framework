"""Refuting pass, block 22 (supervisor seat, disjoint machinery from the runner's checks):
(R1) the multinomial sums T_n = sum_{a+b+c=n} (n!/(a!b!c!))^2 by direct enumeration of (a, b, c) for n <= 300, against the Vandermonde form;
(R2) the true tail by a fit: P_{2n} ~ c n^{-3/2}; c from n = 800..1000; the tail estimate 2c/sqrt(N) added to S_N lands near the classical
     value 1.5163860591... (used here as a reference only, never in the certificate);
(R3) the tail bound P_{2n} <= (36/11)^{3/2}/(4 pi^{3/2} n^{3/2}) + 2 e^{-4n/(3 pi^2)} against the exact P_{2n} (as floats) for n = 1..1000;
     the ratio bound/P_{2n} at n = 1000 (the slack of the elementary bound);
(R4) the symbol's lower bound 1 - phi(k) >= g(k) on a 41^3 grid of the cube;
(R5) the exponential majorant: (197/225)^(N+1) >= e^{-2(N+1)/15} >= e^{-4(N+1)/(3 pi^2)} at N = 1000 (log scale), and 225/14 = 2/(1 - 197/225)."""
import math
from fractions import Fraction as F
from math import comb, factorial, lgamma

import numpy as np


def T_direct(n):
    return sum((factorial(n) // (factorial(a) * factorial(b) * factorial(n - a - b))) ** 2 for a in range(n + 1) for b in range(n - a + 1))


def T_vand(n):
    return sum(comb(n, a) ** 2 * comb(2 * (n - a), n - a) for a in range(n + 1))


ok1 = all(T_direct(n) == T_vand(n) for n in range(0, 301))
print(f"R1 direct multinomial enumeration equals the Vandermonde form for n <= 300: {ok1}; T_300 has {len(str(T_vand(300)))} digits")


def logP(n):
    # log P_{2n} = log C(2n,n) + log T_n - 2n log 6
    return (lgamma(2 * n + 1) - 2 * lgamma(n + 1)) + math.log(T_vand(n)) - 2 * n * math.log(6)


P = {n: math.exp(logP(n)) for n in range(1, 1001)}
S = 1.0 + sum(P.values())
cs = [P[n] * n ** 1.5 for n in range(800, 1001)]
c = float(np.mean(cs))
tail_est = 2 * c / math.sqrt(1000)
print(f"R2 fit P_2n ~ c n^-3/2 with c = {c:.5f} (spread {max(cs)-min(cs):.1e}); S_1000 = {S:.7f}; S_1000 + 2c/sqrt(1000) = {S + tail_est:.7f} vs the classical value 1.5163861 (reference only)")
ok3 = True
ratio = None
for n in range(1, 1001):
    bound = (36 / 11) ** 1.5 / (4 * math.pi ** 1.5 * n ** 1.5) + 2 * math.exp(-4 * n / (3 * math.pi ** 2))
    ok3 = ok3 and P[n] <= bound
    if n == 1000:
        ratio = bound / P[n]
print(f"R3 the tail bound dominates the exact P_2n for n = 1..1000: {ok3}; slack at n = 1000: bound/P = {ratio:.3f}")
grid = np.linspace(-math.pi, math.pi, 41)
ok4 = True
for k1 in grid:
    for k2 in grid:
        for k3 in grid:
            phi = (math.cos(k1) + math.cos(k2) + math.cos(k3)) / 3
            g = (11 / 72) * (k1 * k1 + k2 * k2 + k3 * k3) if max(abs(k1), abs(k2), abs(k3)) <= 1 else 2 / (3 * math.pi ** 2)
            ok4 = ok4 and 1 - phi >= g - 1e-12
print(f"R4 1 - phi(k) >= g(k) on the 41^3 grid of the cube: {ok4}")
N = 1000
print(f"R5 log((197/225)^(N+1)) = {(N+1)*math.log(197/225):.2f} >= -2(N+1)/15 = {-2*(N+1)/15:.2f} >= -4(N+1)/(3 pi^2) = {-4*(N+1)/(3*math.pi**2):.2f}: {(N+1)*math.log(197/225) >= -2*(N+1)/15 >= -4*(N+1)/(3*math.pi**2)}; 2/(1 - 197/225) = {2/(1-197/225):.6f} = 225/14 = {225/14:.6f}")
