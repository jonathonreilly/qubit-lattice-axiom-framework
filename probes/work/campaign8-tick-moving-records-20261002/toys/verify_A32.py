#!/usr/bin/env python3
"""Coordinator's independent check of A32 (own code).
(i)  D21: H(k) = sin k sx + m sz: clock rate R = d omega/dm = m/omega obeys R^2 = 1 - v^2/cos^2 k, v = d omega/dk;
(ii) D33: two-level Zeno toy at chance 1 per tick: record rate sin^2(J tau)/tau, max at tan(J tau) = 2 J tau (J tau* = 1.1656),
     max value 0.7246 J; chance c < 1: optimum near tau ~ c/(2J) (exact Markov chain over ticks);
(iii) D30: leak beyond the record cone after n ticks, sum_{|d|>n} J_d(n x)^2: exponential at x = 0.5 with rate 2 eta(0.5) = 0.902,
     power law 0.1688 n^(-1/3) at x = 1 (slow convergence), -> 1 - (2/pi) arcsin(1/x) at x = 1.1;
(iv) D20(b): momentum-independent positive weights F = a + b sz + d sx + e sy: moving/rest count ratio >= 1/2 (rest R = 1)."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
from scipy.special import jv
from scipy.optimize import brentq
# (i)
worst = 0.0
for m in (0.05, 0.3, 1.0):
    for k in np.linspace(0.05, 1.5, 30):
        om = np.sqrt(np.sin(k)**2 + m*m); h = 1e-6
        R = (np.sqrt(np.sin(k)**2 + (m+h)**2) - np.sqrt(np.sin(k)**2 + (m-h)**2))/(2*h)
        v = (np.sqrt(np.sin(k+h)**2 + m*m) - np.sqrt(np.sin(k-h)**2 + m*m))/(2*h)
        worst = max(worst, abs(R*R - (1 - v*v/np.cos(k)**2)))
print("(i) max |R^2 - (1 - v^2/cos^2 k)| = %.1e" % worst)
# (ii)
x0 = brentq(lambda x: np.tan(x) - 2*x, 0.5, 1.5)
print("(ii) J tau* = %.4f ; max rate = %.4f J" % (x0, np.sin(x0)**2/x0))
def rate(Jtau, c):
    # exact stationary record rate for u<->r two-level, H = J sx, each tick: evolve tau, then instrument weight c|r><r|
    # state after a no-record outcome stays pure; track as density matrix; recording resets to u (record formed -> new trial)
    # renewal: expected ticks to first record from u
    U = np.array([[np.cos(Jtau), -1j*np.sin(Jtau)], [-1j*np.sin(Jtau), np.cos(Jtau)]])
    K0 = np.diag([1.0, np.sqrt(1 - c)])           # basis (u, r): no-record Kraus
    rho = np.array([[1, 0], [0, 0]], complex); surv = 1.0; Et = 0.0; n = 0
    while surv > 1e-14 and n < 200000:
        n += 1
        rho = U @ rho @ U.conj().T
        p = c*rho[1, 1].real
        Et += n*p
        rho = K0 @ rho @ K0.conj().T
        surv = np.trace(rho).real
    return 1.0/(Et*Jtau)      # records per unit (J time)
for c in (1.0, 0.5, 0.1):
    grid = np.linspace(0.005, 1.6, 640)
    rates = [rate(g, c) for g in grid]
    i = int(np.argmax(rates))
    print("    c=%.1f: optimum J tau = %.3f (c/2 = %.3f), max rate %.4f J" % (c, grid[i], c/2, rates[i]))
# (iii)
def leak(n, x):
    d = np.arange(n+1, n + 60*int(max(10, n**0.5)) + 200)
    return 2*np.sum(jv(d, n*x)**2)
eta = np.log((1+np.sqrt(1-0.25))/0.5) - np.sqrt(1-0.25)
l1, l2 = leak(40, 0.5), leak(80, 0.5)
print("(iii) x=0.5: slope -ln(L80/L40)/40 = %.3f vs 2 eta = %.3f" % (-np.log(l2/l1)/40, 2*eta))
for n in (10, 100, 1000, 3000):
    print("     x=1, n=%d: leak*n^(1/3)/0.1688 = %.3f" % (n, leak(n, 1.0)*n**(1/3)/0.1688))
print("     x=1.1, n=2000: leak = %.4f vs 1-(2/pi)asin(1/1.1) = %.4f" % (leak(2000, 1.1), 1-2/np.pi*np.arcsin(1/1.1)))
# (iv)
rng = np.random.default_rng(5); worst_ratio = 1.0
for t in range(20000):
    b, d, e = rng.normal(size=3); a = np.sqrt(b*b+d*d+e*e)*(1 + abs(rng.normal())*rng.uniform(0, 1))
    m = 0.3
    rest = a + b                      # k = 0: upper-band sz expectation = m/omega = 1, sx expectation = 0
    for k in np.linspace(0.01, 1.55, 40):
        om = np.sqrt(np.sin(k)**2 + m*m)
        mov = a + (b*m + d*np.sin(k))/om
        if rest > 1e-9:
            worst_ratio = min(worst_ratio, mov/rest)
print("(iv) min over 20000 positive weights of (moving count)/(rest count) = %.4f (claim: >= 1/2 achievable only as limit)" % worst_ratio)
