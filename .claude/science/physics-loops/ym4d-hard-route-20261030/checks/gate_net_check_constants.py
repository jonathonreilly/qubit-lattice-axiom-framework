#!/usr/bin/env python3
"""Exact checks of the constants in Theorem 10.7 and Remark 3.3.

(1) 2D SU(2) on a torus with V plaquettes, exact in characters.
    Var(X_p) and Cov(X_p, X_q), X = beta s, as beta -> infinity. Naive Remark 3.3 with
    P the projector onto exact two-forms (P_pq = delta_pq - 1/V) predicts
    Var -> (3/2)(1-1/V)^2 and Cov -> (3/2)/V^2. Tests the (3/2) and the colour counting.
(2) Single plaquette law: <X> -> 3/2, Var X -> 3/2 (P_pp = 1). The chi^2_3 / 2 check.
(3) P_pq on Z^4, exact via the heat-kernel product of Bessel functions, against the
    Maxwell tensor at the offsets used in Theorem 10.7. P_pp = 1/2. Size of the main term.
"""
import numpy as np
from scipy import integrate, special

np.set_printoptions(precision=6, suppress=True, linewidth=120)


def su2_tables(beta, nj):
    th, w = np.polynomial.legendre.leggauss(3000)
    th = 0.5 * np.pi * (th + 1)
    w = 0.5 * np.pi * w
    meas = (2 / np.pi) * np.sin(th) ** 2 * w
    s = 1 - np.cos(th)
    base = np.exp(-beta * s)
    a = np.zeros(nj)
    a1 = np.zeros(nj)
    a2 = np.zeros(nj)
    for n in range(nj):
        chi = np.sin((n + 1) * th) / np.sin(th) / (n + 1)
        a[n] = np.sum(meas * base * chi)
        a1[n] = np.sum(meas * base * chi * s)
        a2[n] = np.sum(meas * base * chi * s * s)
    return a, a1, a2


def torus2d(beta, V, nj=400):
    a, a1, a2 = su2_tables(beta, nj)
    ok = a > 1e-250 * a[0]
    a = a[ok]
    a1 = a1[ok]
    a2 = a2[ok]
    w = (a / a[0]) ** V  # Z = sum_j a_j^V on genus one (no dimension factor)
    w = w / w.sum()
    e = a1 / a
    e2 = a2 / a
    mean = np.sum(w * e)
    var_same = np.sum(w * e2) - mean ** 2
    cov_diff = np.sum(w * e * e) - mean ** 2
    return beta * mean, beta ** 2 * var_same, beta ** 2 * cov_diff


def part1():
    print("(1) 2D SU(2) torus, exact. X = beta s.")
    print("    V    beta      <X>     Var(X)    Cov(X_p,X_q)*V^2  naive 3/2 ; moduli-corrected 1/2")
    for V in [4, 16]:
        for beta in [200.0, 2000.0]:
            m, v, c = torus2d(beta, V, nj=300)
            print("  %4d %8.0f  %8.5f  %8.5f  %10.5f" % (V, beta, m, v, c * V * V))


def part2():
    print("(2) single plaquette, chi^2_3/2 law")
    for beta in [10.0, 100.0, 1000.0]:
        a, a1, a2 = su2_tables(beta, 1)
        m = a1[0] / a[0]
        v = a2[0] / a[0] - m ** 2
        print("  beta %8.0f  <X> %.6f  Var X %.6f  (limits 3/2, 3/2)" % (beta, beta * m, beta * beta * v))


_T = np.exp(np.linspace(np.log(1e-4), np.log(1e7), 6001))
_DL = np.log(_T[1] / _T[0])
_IVE = {}


def _ive(n):
    if n not in _IVE:
        _IVE[n] = special.ive(n, 2 * _T)
    return _IVE[n]


def G4(x):
    """Lattice Green function on Z^4 by heat kernel: int_0^inf prod exp(-2t) I_{x_mu}(2t) dt.
    Log-grid trapezoid, plus the tail 1/(16 pi^2 T_max) and the head T_min."""
    x = np.abs(np.asarray(x, dtype=int))
    f = np.ones_like(_T)
    for n in x:
        f = f * _ive(int(n))
    val = np.sum(f * _T) * _DL - 0.5 * _DL * (f[0] * _T[0] + f[-1] * _T[-1])
    return val + 1.0 / (16 * np.pi ** 2 * _T[-1]) + (_T[0] if x.sum() == 0 else 0.0)


def Ppar(x):
    """P_{12,12}(x) on Z^4: -(Delta_1 + Delta_2) G (x), the parallel plaquette covariance
    divided by 4/beta, with symbol (|f_1|^2 + |f_2|^2)/|f|^2."""
    x = np.asarray(x, dtype=int)
    g0 = G4(x)
    e1 = np.array([1, 0, 0, 0])
    e2 = np.array([0, 1, 0, 0])
    return 4 * g0 - G4(x + e1) - G4(x - e1) - G4(x + e2) - G4(x - e2)


def maxwell_par(x):
    x = np.asarray(x, dtype=float)
    r2 = np.sum(x * x)
    return (1 - 2 * (x[0] ** 2 + x[1] ** 2) / r2) / (np.pi ** 2 * r2 ** 2)


def part3():
    print("(3) P_{12,12}(x) on Z^4")
    print("  P(0) = %.8f (exact 1/2)" % Ppar([0, 0, 0, 0]))
    print("      x                lattice P         Maxwell         ratio      (3/2)P^2")
    for d in [1, 2, 3, 4, 6, 8, 12]:
        x = [d, d, 2 * d, 2 * d]
        p = Ppar(x)
        m = maxwell_par(x)
        print("  %-20s %+.6e   %+.6e   %.4f   %.3e" % (x, p, m, p / m, 1.5 * p * p))
    for d in [2, 4, 8]:
        x = [d, d, d, d]
        print("  %-20s %+.6e   %+.6e   (vanishing pair)" % (x, Ppar(x), maxwell_par(x)))
    print("  coefficient check at (d,d,2d,2d): 0.6/(100 pi^2) = %.6e" % (0.6 / (100 * np.pi ** 2)))


if __name__ == "__main__":
    part1()
    part2()
    part3()
