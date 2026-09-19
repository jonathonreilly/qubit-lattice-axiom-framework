#!/usr/bin/env python3
"""Referee check for J:derive:two-source-interaction:a4 (author w-macbookpro90c72-j8f4d, grok-4.6).

Independent code; nothing is taken from the author's script. Linear light-cone model on Z^3:
phi(k) = 1 - E(k)/7, E = 2 sum_j (1 - cos k_j), equal-time C(k) = sigma^2/(1 - phi^2) (sigma^2 = 1).

T1  step 1: 1/(1 - phi^2) = 49/(E(14 - E)); chi = 1/(1 - phi) = 7/E; chi/C = 1 + phi (sympy).
T2  step 2 and the correct fluctuation-response for the reversible linear PCA: a field h in the dynamics at x0
    shifts the stationary law's log-weight by h (s_x0 + E[s'_x0 | S_x0]), so the response is C (1 + P) = chi
    (exact, all modes of the L = 4 torus).
T3  step 3: two-site Gaussian pinning, like a^2/(C0 + Cr), unlike a^2/(C0 - Cr); unlike - like = 2 a^2 Cr/(C0^2 - Cr^2),
    so the sign of Cr is the sign of unlike - like (the text says like - unlike).
T4  step 4: exact L = 4 sums C(0) - C(r) (Fractions) for r = e1, e1+e2, 2e1 and others.
T5  step 5: C0 on mean-zero tori L = 8..64 settles (3D: C ~ 7/(2k^2) is integrable), with the infinite-volume value
    C0 = (7/2)(W + I_14), W = (2pi)^-3 Int 1/E (Watson/2), I_14 = (2pi)^-3 Int 1/(14 - E); like-pin energies finite.
T6  the coefficient of 1/r (not given by the attempt): C(r) ~ 7/(8 pi r), checked by torus differences
    (C(r) - C(2r)) * 16 pi r / 7 -> 1 on L = 128.
T7  persistent pins (the task's sources, pinned at every level) versus the attempt's equal-time conditioning, L = 8,
    unlike pins a, -a at 0 and 2e1: stationary mean of the pinned recursion (iterated) against the conditional mean
    of the stationary equal-time law.
"""
from __future__ import annotations

import itertools
import math
from fractions import Fraction as Fr

import numpy as np
import sympy as sp


def t1():
    E = sp.Symbol("E", positive=True)
    phi = 1 - E / 7
    C = sp.simplify(1 / (1 - phi ** 2))
    chi = sp.simplify(1 / (1 - phi))
    return (sp.simplify(C - 49 / (E * (14 - E))) == 0, sp.simplify(C - 7 / (2 * E * (1 - E / 14))) == 0,
            sp.simplify(chi - 7 / E) == 0, sp.simplify(chi / C - (1 + phi)) == 0)


COS4 = [Fr(1), Fr(0), Fr(-1), Fr(0)]


def modes4():
    for n in itertools.product(range(4), repeat=3):
        E = sum(2 * (1 - COS4[m]) for m in n)
        yield n, E


def t2():
    ok = True
    for n, E in modes4():
        if E == 0:
            continue
        phi = 1 - Fr(E, 7)
        C = 1 / (1 - phi * phi)
        ok &= C * (1 + phi) == 1 / (1 - phi)
    return ok


def t3():
    a, C0, Cr = sp.symbols("a C0 Cr", positive=True)
    K = sp.Matrix([[C0, Cr], [Cr, C0]])
    like = sp.simplify((sp.Matrix([[a, a]]) * K.inv() * sp.Matrix([a, a]))[0] / 2)
    unlike = sp.simplify((sp.Matrix([[a, -a]]) * K.inv() * sp.Matrix([a, -a]))[0] / 2)
    ok = sp.simplify(like - a ** 2 / (C0 + Cr)) == 0 and sp.simplify(unlike - a ** 2 / (C0 - Cr)) == 0
    diff_ul = sp.simplify(unlike - like - 2 * a ** 2 * Cr / (C0 ** 2 - Cr ** 2)) == 0
    return ok, diff_ul


def t4():
    out = {}
    for r in ((1, 0, 0), (1, 1, 0), (2, 0, 0), (1, 1, 1), (2, 1, 0), (2, 2, 0), (2, 2, 2)):
        s = Fr(0)
        for n, E in modes4():
            if E == 0:
                continue
            Ck = Fr(49, E * (14 - E))
            s += (1 - COS4[sum(ni * ri for ni, ri in zip(n, r)) % 4]) * Ck
        out[r] = s / 64
    return out


def torus_C(L):
    k = 2 * np.pi * np.arange(L) / L
    g1, g2, g3 = np.meshgrid(k, k, k, indexing="ij")
    E = 2 * ((1 - np.cos(g1)) + (1 - np.cos(g2)) + (1 - np.cos(g3)))
    Ck = np.zeros_like(E)
    m = E > 1e-12
    Ck[m] = 49.0 / (E[m] * (14.0 - E[m]))
    return Ck


WATSON_HALF = 0.2527310098  # (2pi)^-3 Int d^3k / E(k), E = 2 sum (1 - cos k_j): Watson's integral / 2


def t5():
    vals, ce1 = {}, {}
    for L in (8, 16, 32, 64):
        Ck = torus_C(L)
        k = 2 * np.pi * np.arange(L) / L
        c1 = np.cos(k)[:, None, None] * np.ones((1, L, L))
        vals[L] = Ck.sum() / L ** 3
        ce1[L] = (Ck * c1).sum() / L ** 3
    # I_14 = (2pi)^-3 Int 1/(14 - E): smooth and periodic, so a midpoint grid converges fast
    n = 96
    k = 2 * np.pi * (np.arange(n) + 0.5) / n
    g1, g2, g3 = np.meshgrid(k, k, k, indexing="ij")
    E = 2 * ((1 - np.cos(g1)) + (1 - np.cos(g2)) + (1 - np.cos(g3)))
    I14 = float((1.0 / (14.0 - E)).mean())
    return vals, ce1, I14


def t6(L=128):
    Ck = torus_C(L)
    C = np.real(np.fft.ifftn(Ck))
    rows = []
    for dvec in ((1, 0, 0), (1, 1, 0), (1, 1, 1)):
        for m in (3, 5, 8):
            x = tuple(m * c for c in dvec)
            x2 = tuple(2 * c for c in x)
            r = m * math.sqrt(sum(c * c for c in dvec))
            val = (C[x] - C[tuple(c % L for c in x2)]) * 16 * math.pi * r / 7
            rows.append((dvec, m, val))
    return rows


def t7(L=8, a=1.0, levels=4000):
    N = L ** 3

    def idx(i, j, k):
        return ((i % L) * L + (j % L)) * L + (k % L)

    P = np.zeros((N, N))
    for i, j, k in itertools.product(range(L), repeat=3):
        x = idx(i, j, k)
        P[x, x] += 1 / 7
        for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            P[x, idx(i + d[0], j + d[1], k + d[2])] += 1 / 7
    p0, p1 = idx(0, 0, 0), idx(2, 0, 0)
    # persistent pins: the mean obeys m_{t+1} = P m_t off the pins, m = +-a on the pins at every level
    m = np.zeros(N)
    for _ in range(levels):
        m = P @ m
        m[p0], m[p1] = a, -a
    # equal-time conditioning of the stationary law (mean-zero; C = (I - P^2)^+)
    ones = np.ones(N) / N
    A = np.eye(N) - P @ P + np.outer(np.ones(N), ones)
    C = np.linalg.inv(A) - np.outer(np.ones(N), ones)
    K = C[np.ix_([p0, p1], [p0, p1])]
    cond = C[:, [p0, p1]] @ np.linalg.solve(K, np.array([a, -a]))
    test = [idx(-1, 0, 0), idx(0, 1, 0), idx(0, 0, -2), idx(4, 4, 4)]
    return [(m[t], cond[t]) for t in test], np.abs(m - cond).max()


def main():
    r1 = t1()
    print(f"T1 1/(1-phi^2) = 49/(E(14-E)): {r1[0]}; = 7/(2E(1-E/14)): {r1[1]}; chi = 7/E: {r1[2]}; chi/C = 1+phi: {r1[3]}")
    print(f"T2 C(1+phi) = chi on every nonzero mode of the L=4 torus (the reversible PCA's response to a dynamical field): {t2()}")
    ok3, diff_ul = t3()
    print(f"T3 like a^2/(C0+Cr), unlike a^2/(C0-Cr): {ok3}; unlike - like = 2a^2 Cr/(C0^2-Cr^2): {diff_ul} "
          f"(so sign(Cr) = sign(unlike - like); like - unlike = -2a^2 Cr/(C0^2-Cr^2))")
    r4 = t4()
    print("T4 L=4 exact C(0)-C(r): " + ", ".join(f"r={r}: {v}" for r, v in r4.items()))
    r5, ce1, I14 = t5()
    incr = [r5[L2] - r5[L1] for L1, L2 in ((8, 16), (16, 32), (32, 64))]
    c0_inf = 3.5 * (WATSON_HALF + I14)
    print(f"T5 mean-zero torus C0(L) for L=8,16,32,64: {[round(float(v), 5) for v in r5.values()]}; increments "
          f"{[round(float(v), 5) for v in incr]} (ratio {incr[2] / incr[1]:.3f}, extrapolated {r5[64] + incr[-1]:.4f}); infinite volume "
          f"C0 = (7/2)(W + I_14) = 3.5 ({WATSON_HALF} + {I14:.6f}) = {c0_inf:.4f}; at L=64 C(e1) = {ce1[64]:.4f}: like-pin energy "
          f"a^2/(C0+C(e1)) = {1 / (r5[64] + ce1[64]):.4f} a^2, unlike a^2/(C0-C(e1)) = {1 / (r5[64] - ce1[64]):.4f} a^2 (both finite)")
    r6 = t6()
    for dvec, m, val in r6:
        print(f"T6 (C(r)-C(2r)) * 16 pi r/7 along {dvec}, r = {m}*|dir|: {val:.4f} (-> 1 for C(r) ~ 7/(8 pi r))")
    r7, dev = t7()
    print("T7 L=8 unlike pins +-1 at 0 and 2e1: (persistent-pin stationary mean, equal-time conditional mean) at -e1, e2, -2e3, (4,4,4): "
          + ", ".join(f"({p:.4f}, {c:.4f})" for p, c in r7) + f"; max difference over the torus {dev:.4f}")

    step1_2 = all(r1) and t2()
    step3 = ok3 and diff_ul
    L4_equal = r4[(1, 0, 0)] == r4[(1, 1, 0)] == r4[(2, 0, 0)] == Fr(147, 128)
    settles = 0.45 < incr[2] / incr[1] < 0.55 and 0.45 < incr[1] / incr[0] < 0.55 and abs(r5[64] + incr[-1] - c0_inf) < 0.01
    coef_ok = all(abs(v - 1) < 0.05 for d, m, v in r6 if m >= 5)
    persistent_differs = dev > 0.05
    if step1_2 and step3 and L4_equal and settles:
        print("SUMMARY: fails at step 5 - C0 does not diverge: C(k) = 49/(E(14-E)) ~ 7/(2k^2) is integrable in 3D, and the "
              f"mean-zero torus C0(L) settles (L=8..64: {', '.join(f'{v:.4f}' for v in r5.values())}, increments halving, limit "
              f"{r5[64] + incr[-1]:.4f} against (7/2)(Watson/2 + I_14) = {c0_inf:.4f}), so like "
              "pins have a finite energy a^2/(C0+Cr) in infinite volume; the only divergence is the torus zero mode, which is "
              "non-stationary on every torus in every dimension and would make the like-pin energy r-independent (0), "
              "contradicting the attempt's own 'like pins attractive when C(r)>0'; steps 1-2 hold (chi/C = 1+phi; the reversible "
              "PCA's response is C(1+P) = chi), step 3's formulas hold with its sign sentence reversed (sign Cr = sign of "
              f"unlike-minus-like), step 4's L=4 value 147/128 holds for e1, e1+e2, 2e1; not supplied: the 1/r coefficient "
              f"(C(r) ~ 7/(8 pi r), torus check {'ok' if coef_ok else 'off'}), the L=8..32 checks, and persistent pins, whose "
              f"stationary mean differs from equal-time conditioning (max difference {dev:.3f} at L=8)")
    else:
        print(f"SUMMARY: fails - steps 1-2 {step1_2}, step 3 {step3}, L4 {L4_equal}, C0 settles {settles}")


if __name__ == "__main__":
    main()
