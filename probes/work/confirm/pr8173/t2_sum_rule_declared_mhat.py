#!/usr/bin/env python3
"""J:confirm:J-attack-f-PR8173 -- independent test of the finder's normalization HIT on block 29 (PR #8173).

Finder's HIT: (i) T2 'beta h N <(m^1)^2> = <m^3>' fails by sqrt(N) under the declared Fourier transform
s^(k) = N^{-1/2} sum_x e^{-ik.x} s_x, read at k = 0; (ii) the runner's D1 prints N^{-1} sum_k |f^(k)|^2 = sum_x f_x^2,
true only for the unnormalized transform.

The note's Definitions declare BOTH objects: s^(k) = N^{-1/2} sum_x e^{-ik.x} s_x AND, separately,
'm^ = N^{-1} sum_x s_x' (the magnetization). This script tests T2 with the declared m^ by other machinery:
  A. two sphere spins (N = 2, one bond of strength beta, field h along e3): exact reduction to a 3D integral over
     (u1, u2, relative angle), Gauss-Legendre x trapezoid quadrature;
  B. a heat-bath Monte Carlo of the sphere static law on the 4^3 torus (N = 64) in a field;
  C. Parseval on rings with rational data under the declared unitary transform (T3) and under the runner's
     unnormalized f_hat (D1).
"""
from __future__ import annotations

import math
from fractions import Fraction as Fr

import numpy as np
import sympy as sp


# ------------------------------------------------------------------------------------------------ A
def two_site(beta, h, nu=160, nphi=256):
    x, w = np.polynomial.legendre.leggauss(nu)
    phi = 2 * np.pi * np.arange(nphi) / nphi
    u1, u2, ph = np.meshgrid(x, x, phi, indexing="ij")
    W = (w[:, None, None] * w[None, :, None]) * np.ones_like(ph)
    r1, r2 = np.sqrt(1 - u1 ** 2), np.sqrt(1 - u2 ** 2)
    dot = u1 * u2 + r1 * r2 * np.cos(ph)
    dens = np.exp(beta * dot + beta * h * (u1 + u2)) * W
    Z = dens.sum()
    m3 = ((u1 + u2) / 2 * dens).sum() / Z
    # (m^1)^2 averaged over the common azimuth: (1/4)[(r1^2 + r2^2)/2 + r1 r2 cos(phi)]
    m1sq = (((r1 ** 2 + r2 ** 2) / 2 + r1 * r2 * np.cos(ph)) / 4 * dens).sum() / Z
    N = 2
    return m3, m1sq, beta * h * N * m1sq


# ------------------------------------------------------------------------------------------------ B
def vmf_sample(field, rng):
    """sample s on S^2 with density proportional to exp(field . s), field of shape (..., 3)."""
    kappa = np.linalg.norm(field, axis=-1)
    U = rng.random(kappa.shape)
    u = 1 + np.log(U + (1 - U) * np.exp(-2 * kappa)) / kappa  # cos angle to the field
    ang = 2 * np.pi * rng.random(kappa.shape)
    r = np.sqrt(np.clip(1 - u ** 2, 0, None))
    n = field / kappa[..., None]
    # orthonormal frame around n
    a = np.where(np.abs(n[..., 0:1]) < 0.9, np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
    e1 = np.cross(n, a)
    e1 /= np.linalg.norm(e1, axis=-1, keepdims=True)
    e2 = np.cross(n, e1)
    return u[..., None] * n + (r * np.cos(ang))[..., None] * e1 + (r * np.sin(ang))[..., None] * e2


def monte_carlo(L=4, beta=0.5, h=0.5, sweeps=24000, burn=2000, seed=8173):
    rng = np.random.default_rng(seed)
    s = np.zeros((L, L, L, 3))
    s[..., 2] = 1.0
    ii, jj, kk = np.indices((L, L, L))
    parity = (ii + jj + kk) % 2
    hvec = np.array([0, 0, h])
    acc3, acc11, n = 0.0, 0.0, 0
    series3, series11 = [], []
    for t in range(sweeps):
        for par in (0, 1):
            nb = sum(np.roll(s, sh, axis=ax) for ax in range(3) for sh in (1, -1))
            field = beta * (nb + hvec)
            new = vmf_sample(field, rng)
            mask = parity == par
            s[mask] = new[mask]
        if t >= burn:
            m = s.reshape(-1, 3).mean(axis=0)  # the declared m^ = N^{-1} sum_x s_x
            series3.append(m[2])
            series11.append(0.5 * (m[0] ** 2 + m[1] ** 2))  # <(m^1)^2> by symmetry of the 1,2 axes
    series3, series11 = np.array(series3), np.array(series11)
    N = L ** 3

    def mean_err(a, blocks=40):
        b = a[: len(a) // blocks * blocks].reshape(blocks, -1).mean(axis=1)
        return a.mean(), b.std(ddof=1) / math.sqrt(blocks)

    m3, e3 = mean_err(series3)
    m11, e11 = mean_err(series11)
    lhs = beta * h * N * m11
    return m3, e3, lhs, beta * h * N * e11, N


# ------------------------------------------------------------------------------------------------ C
def parseval():
    out = []
    for f in ([Fr(3, 7), Fr(-2, 7), Fr(5, 7), Fr(1, 7)], [Fr(1, 2), Fr(-1, 3), Fr(2, 5), Fr(0), Fr(-3, 4), Fr(1, 6)]):
        N = len(f)
        fs = [sp.Rational(fx.numerator, fx.denominator) for fx in f]
        s_unn = sp.Integer(0)
        for k in range(N):
            re = sum((fx * sp.cos(2 * sp.pi * k * x / N) for x, fx in enumerate(fs)), sp.Integer(0))
            im = sum((-fx * sp.sin(2 * sp.pi * k * x / N) for x, fx in enumerate(fs)), sp.Integer(0))
            s_unn += sp.expand(re ** 2 + im ** 2)
        s_unn = sp.nsimplify(sp.simplify(s_unn))
        sum_sq = sum(fx * fx for fx in f)
        mean_sq = sum_sq / N
        declared = s_unn / N  # sum_k |s^(k)|^2 with s^ = N^{-1/2} f^_unn
        out.append((N, sp.simplify(s_unn / N), sp.simplify(declared / N), sum_sq, mean_sq))
    return out


def main():
    print("A. two sphere spins, m^ = (s1 + s2)/2 as declared, exact reduction + quadrature")
    worstA = 0.0
    for beta, h in ((0.3, 0.7), (1.0, 0.5), (2.0, 0.2), (0.7, 2.0)):
        m3, m1sq, lhs = two_site(beta, h)
        worstA = max(worstA, abs(lhs - m3) / abs(m3))
        print(f"   beta={beta} h={h}: <m^3> = {m3:.12f}, beta h N <(m^1)^2> = {lhs:.12f}; with the finder's reading "
              f"m^ -> N^(1/2) m^: LHS/RHS = {lhs * 2 / (math.sqrt(2) * m3):.6f}")
    print("B. heat-bath Monte Carlo, sphere static law on the 4^3 torus (N = 64), beta = 0.5, h = 0.5, m^ = N^-1 sum s")
    m3, e3, lhs, elhs, N = monte_carlo()
    print(f"   <m^3> = {m3:.4f} +- {e3:.4f}; beta h N <(m^1)^2> = {lhs:.4f} +- {elhs:.4f}; ratio {lhs / m3:.4f}; "
          f"finder's reading predicts ratio sqrt(N) = {math.sqrt(N):.1f}")
    print("C. Parseval on rings with rational data")
    parse_ok = True
    for N, unn_over_N, declared_over_N, sum_sq, mean_sq in parseval():
        ok_d1 = unn_over_N == sp.Rational(sum_sq.numerator, sum_sq.denominator)
        ok_t3 = declared_over_N == sp.Rational(mean_sq.numerator, mean_sq.denominator)
        parse_ok &= ok_d1 and ok_t3
        print(f"   N={N}: runner's D1 (unnormalized f_hat): N^-1 sum|f_hat|^2 = {unn_over_N} = sum f^2 = {sum_sq}: {ok_d1}; "
              f"declared unitary s^ (T3): N^-1 sum|s^|^2 = {declared_over_N} = <f^2> = {mean_sq}: {ok_t3}")
    print("   (observation, not a HIT: T2's proof line writes '<N m^3> = beta h <N m^1 . N m^1>/N', whose left side should read <m^3>;"
          " the stated identity is the one A and B verify)")

    t2_holds = worstA < 1e-9 and abs(lhs / m3 - 1) < 5 * (elhs / m3 + e3 / m3) + 0.03
    if t2_holds and parse_ok:
        print(f"SUMMARY: not reproduced - the note declares m^ = N^-1 sum_x s_x (Definitions), separately from s^(k) = N^-1/2 sum e^-ikx s_x; "
              f"with the declared m^ T2 holds (two-site quadrature, max relative gap {worstA:.1e}; Monte Carlo on 4^3: ratio "
              f"{lhs / m3:.3f}, the finder's reading would give 8); the finder substituted N^-1/2 sum s for m^; D1 checks Parseval for "
              f"the runner's unnormalized f_hat (a true identity) and T3 holds under the declared unitary s^ on rings N = 4, 6")
    elif not t2_holds:
        print(f"HIT: confirmed - T2 fails even with the declared m^ (two-site gap {worstA:.2e}, Monte Carlo ratio {lhs / m3:.3f})")
        print("SUMMARY: confirmed")
    else:
        print("SUMMARY: not reproduced for T2; Parseval check inconclusive")


if __name__ == "__main__":
    main()
