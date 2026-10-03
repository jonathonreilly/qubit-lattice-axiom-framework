#!/usr/bin/env python3
"""A18 estimator: can a lapse set by the records in a finite neighbourhood be exp(u/u_inf - 1)?
(supplied toy arithmetic, nothing adopted)
Setting: the snapshot shows 0/1 wanderer occupations; site x sees k = number of occupied sites among m
neighbourhood sites; locally k ~ Binomial(m, u) (product measure, exact for exclusion in equilibrium,
local-equilibrium approximation near a clump). The per-beat factor is f(k). In the small-dose limit the
ripple sees the averaged pace F(u) = E_u f(k), a polynomial of degree <= m in u (Bernstein form).
Exterior field: u = u_inf (1 - h), h harmonic. Then N/N_inf = F(u)/F(u_inf), and
    beta = (1 + F F'' / F'^2) / 2   evaluated at u_inf      (U_Newton := -(ln N)' * ... to first order)
"""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(58)
import numpy as np
from math import comb
import mpmath as mp
mp.mp.dps = 40


def F_of_u(fk, m, u):
    return mp.fsum(comb(m, k) * mp.mpf(u) ** k * (1 - mp.mpf(u)) ** (m - k) * fk(k) for k in range(m + 1))


def beta_numeric(fk, m, uinf):
    """beta from the 2nd-order expansion of N(h) = F(u_inf (1-h)) / F(u_inf):
       N = 1 - a h + b h^2  ->  U_N = a h,  N^2 = 1 - 2 U_N + 2 beta U_N^2"""
    F = lambda h: F_of_u(fk, m, uinf * (1 - h)) / F_of_u(fk, m, uinf)
    a = -mp.diff(F, 0)
    b = mp.diff(F, 0, 2) / 2
    # N^2 = 1 - 2 a h + (a^2 + 2 b) h^2 ; in U_N = a h : 2 beta = (a^2 + 2 b)/a^2
    return (a ** 2 + 2 * b) / (2 * a ** 2)


print("(1) exponential response to the count, f = r^k: averaged pace (1 + u (r-1))^m  ->  beta = 1 - 1/(2m)")
for m in (6, 7, 26, 124, 5000):
    for r in (1.5, 35.5):
        b = beta_numeric(lambda k, r=r: mp.mpf(r) ** k, m, mp.mpf("0.04"))
        print("   m=%5d r=%5.1f: beta = %.10f   1 - 1/(2m) = %.10f" % (m, r, float(b), 1 - 1 / (2 * m)))

print("(2) P4 literal: f = exp(k/(m u_inf) - 1); bias E f / F(u_inf) and relative noise Var f / (E f)^2 at u = u_inf")
for m in (6, 124, 10**4, 10**6):
    for uinf in (0.04, 1e-5):
        c = 1 / (m * uinf)
        r = mp.e ** c
        Ef = mp.e ** -1 * (1 + uinf * (r - 1)) ** m
        Ef2 = mp.e ** -2 * (1 + uinf * (r ** 2 - 1)) ** m
        relvar = Ef2 / Ef ** 2 - 1
        print("   m=%8d u_inf=%.0e (m u_inf=%9.3g): mean pace %.4g (target 1)  relative variance %.4g  beta %.6f"
              % (m, uinf, m * uinf, float(Ef), float(relvar), 1 - 1 / (2 * m)))

print("(3) power-law averaged pace F = u^p: beta = (2p-1)/(2p)  [p=1 is the A6/A8 event-rate lapse]")
for p in (1, 2, 4):
    F = lambda h, p=p: (1 - h) ** p
    a = -mp.diff(F, 0); bb = mp.diff(F, 0, 2) / 2
    print("   p=%d: exact u^p gives beta = %.6f ; (2p-1)/(2p) = %.6f" % (p, float((a ** 2 + 2 * bb) / (2 * a ** 2)), (2 * p - 1) / (2 * p)))

print("(4) a degree-2 rule tuned to beta = 1 at one background: f(k) = u0^2 + k(k-1)/(m(m-1))  ->  F = u0^2 + u^2")
m, u0 = 6, mp.mpf("0.04")
for s in ("0.8", "0.9", "1.0", "1.1", "1.25"):
    uinf = u0 * mp.mpf(s)
    b = beta_numeric(lambda k: u0 ** 2 + mp.mpf(k * (k - 1)) / (m * (m - 1)), m, uinf)
    print("   actual far density = %s x tuned value: beta = %.6f" % (s, float(b)))

print("(5) dephasing from snapshot noise (i.i.d. per beat; mu = rest energy per beat in lattice units)")
print("   visibility after T beats = |E exp(i mu (f_A - f_B))|^T = |phi(mu)|^(2T)  ->  T_coh ~ 1/(mu^2 Var f) beats")
hbar, c, tP, amu = 1.054571817e-34, 2.99792458e8, 5.391247e-44, 1.66053907e-27
for name, M in (("electron", 9.1093837e-31), ("neutron", 1.67492750e-27), ("Rb-87", 86.909 * amu)):
    rate2 = (M * c ** 2 / hbar) ** 2 * tP          # 1/s for unit relative variance, Planck beat
    print("   %-8s: T_coh = (1/relvar) x %.3g s  ->  1 s of coherence needs relvar <= %.2g" % (name, 1 / rate2, 1 / rate2))
