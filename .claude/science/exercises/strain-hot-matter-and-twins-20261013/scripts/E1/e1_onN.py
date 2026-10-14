#!/usr/bin/env python3
"""E1 (B') comparator class: a coarse scale made by dimensional transmutation (no tuning).
2D lattice O(N) sigma model at N = infinity (exact saddle point), couplings J_x, J_y:
   1/g^2 = G(m^2) = int d^2q/(2pi)^2 1 / (m^2 + J_x e_x + J_y e_y),  e_j = 2(1 - cos q_j).
The gap m = 1/xi is exponentially small in 1/g^2 (asymptotic freedom): xi >> a with no tuned point.
Stretch at fixed g^2: linear J = (1+t, 1-t) and volume-preserving J = (e^t, e^-t).
Question: is delta m additive at the lattice scale (delta m / t^2 -> const, as Ising) or multiplicative
(delta ln m / t^2 -> const or ~ log xi)?  q_y integral in closed form, q_x by adaptive quadrature.
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

def G(m2, Jx, Jy):
    def f(q):
        A = m2 + Jx * 2 * (1 - np.cos(q))
        return 1.0 / np.sqrt(A * (A + 4 * Jy))
    m = np.sqrt(m2)
    pts = [p for p in (m, 3 * m, 10 * m, 30 * m, 100 * m, 1000 * m) if p < np.pi]
    val, err = quad(f, 0, np.pi, points=pts, limit=2000, epsabs=1e-15, epsrel=1e-13)
    return val / np.pi          # (1/2pi) * 2 * int_0^pi

def solve_m(ig2, Jx, Jy, m0):
    return np.exp(brentq(lambda lm: G(np.exp(2 * lm), Jx, Jy) - ig2, np.log(m0) - 3, np.log(m0) + 3, xtol=1e-15))

if __name__ == "__main__":
    print("2D O(N), N=inf: stretch response of the transmuted gap")
    print("  xi0        1/g^2      dln m/t^2 (lin,t=1e-2)  (lin,t=5e-3)   dln m/t^2 (vol-pres)   dm/t^2 (lin)     Ising-like dm/t^2 would be const")
    for xi0 in (10.0, 100.0, 1e3, 1e4, 1e5):
        m0 = 1 / xi0
        ig2 = G(m0 * m0, 1.0, 1.0)
        r = []
        for t in (1e-2, 5e-3):
            m = solve_m(ig2, 1 + t, 1 - t, m0)
            r.append(np.log(m / m0) / t**2)
        t = 1e-2
        mv = solve_m(ig2, np.exp(t), np.exp(-t), m0)
        ml = solve_m(ig2, 1 + t, 1 - t, m0)
        print(f"  {xi0:8.0e}  {ig2:.6f}   {r[0]:+.6f}             {r[1]:+.6f}       {np.log(mv/m0)/t**2:+.6f}             {(ml-m0)/t**2:+.4e}")
    print("  continuum expectation (lin): dln m/t^2 = pi/g^2 * (1/ (2pi))*... i.e. ~ (1/2) ln(xi) + const; vol-pres: const")
