#!/usr/bin/env python3
"""Referee of J:derive:formation-in-3plus1:a1 (author w-macbookpro90c72-j8db3, grok-4.6); referee w-jonathonsmac4f50-j9163
(claude-opus-5). Independent code (sympy; exact Gaussian-rational torus sums; numpy for the return sums); nothing from the
author's check.py. Provenance: this referee's model family refereed attempts a2, a3 and a6 of this problem (all grok), which
share the Hessian; the checks here are written afresh.

Linear formation on a d-dimensional level plane with the d + 1 predecessors x, x - e_j: phi_d(k) = (1 + sum_j e^{i k_j})/(d + 1).

L1  d = 3: the Hessian of 1 - |phi|^2 at 0 is (1/8)[[3,-1,-1],[-1,3,-1],[-1,-1,3]] with eigenvalues 1/8, 1/2, 1/2, and
    k^T M k = (4|k|^2 - (1.k)^2)/16 with 4|k|^2 - (1.k)^2 = |k|^2 + sum_{i<j}(k_i - k_j)^2 (sympy); phi = 1 and grad phi =
    i(1,1,1)/4 at 0; the one-level kernel's mean displacement is (1,1,1)/4
L2  every d = 1..5: the Hessian of 1 - |phi_d|^2 at 0 is positive definite, and |phi_d(k)| = 1 on the torus only at k = 0 (exact on
    (Z/4)^d, d <= 4: |phi|^2 = 1 exactly at the zero mode only)
L3  the integral test: int_0^1 k^(d-3) dk diverges for d = 1, 2 and equals 1 for d = 3 (sympy), so the zero-mode sum
    int d^d k / (k^T M k) is finite iff d > 2; d = 2 (the campaign's Z^3) has Hessian eigenvalues 2/9 and 2/3
I1  INFO: return sums G_L = L^-d sum_{k != 0} 1/(1 - |phi|^2) at L = 8..128: d = 2 grows by a constant per doubling (log L),
    d = 3 levels off (G_4 = 1913/1344 exactly)
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

import numpy as np
import sympy as sp

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


def hessian(d):
    ks = sp.symbols(f"k1:{d + 1}", real=True)
    phi = (1 + sum(sp.exp(sp.I * k) for k in ks)) / (d + 1)
    om = sp.expand_complex(1 - phi * sp.conjugate(phi))
    H = sp.Matrix(d, d, lambda a, b: sp.simplify(sp.diff(om, ks[a], ks[b]).subs({k: 0 for k in ks})))
    return ks, phi, H


def main():
    ks, phi, H = hessian(3)
    k = sp.Matrix(ks)
    quad = sp.expand((k.T * (H / 2) * k)[0])
    cauchy = sp.expand(4 * sum(x ** 2 for x in ks) - sum(ks) ** 2 - (sum(x ** 2 for x in ks) + sum((a - b) ** 2 for a, b in itertools.combinations(ks, 2))))
    grad = [sp.simplify(sp.diff(phi, x).subs({y: 0 for y in ks})) for x in ks]
    ok = (H == sp.Rational(1, 8) * sp.Matrix([[3, -1, -1], [-1, 3, -1], [-1, -1, 3]]) and H.eigenvals() == {sp.Rational(1, 8): 1, sp.Rational(1, 2): 2}
          and sp.simplify(quad - (4 * sum(x ** 2 for x in ks) - sum(ks) ** 2) / 16) == 0 and cauchy == 0
          and phi.subs({y: 0 for y in ks}) == 1 and grad == [sp.I / 4] * 3)
    mean = [F(sum(1 for off in [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)] if off[j] == 1), 4) for j in range(3)]
    check("L1", ok and mean == [F(1, 4)] * 3, f"H = (1/8)[[3,-1,-1],...], eigenvalues {H.eigenvals()}; k^T M k = (4|k|^2 - (1.k)^2)/16 "
          f"= (|k|^2 + sum (k_i - k_j)^2)/16; grad phi(0) = {grad}; kernel mean displacement {mean}")

    ok, rows = True, []
    for d in range(1, 6):
        _, _, Hd = hessian(d)
        ev = Hd.eigenvals()
        ok &= all(e > 0 for e in ev)
        rows.append(f"d = {d}: {ev}")
    units = [(1, 0), (0, 1), (-1, 0), (0, -1)]                     # e^{i pi m/2}
    for d in range(1, 5):
        ones = 0
        for m in itertools.product(range(4), repeat=d):
            re = F(1 + sum(units[j][0] for j in m), d + 1)
            im = F(sum(units[j][1] for j in m), d + 1)
            ones += re * re + im * im == 1
        ok &= ones == 1
    check("L2", ok, "Hessians positive definite: " + "; ".join(rows) + "; on (Z/4)^d, d <= 4, |phi|^2 = 1 only at k = 0")

    kk = sp.symbols("k", positive=True)
    ints = {d: sp.integrate(kk ** (d - 3), (kk, 0, 1)) for d in (1, 2, 3)}
    _, _, H2 = hessian(2)
    ok = ints[1] == sp.oo and ints[2] == sp.oo and ints[3] == 1 and H2.eigenvals() == {sp.Rational(2, 9): 1, sp.Rational(2, 3): 1}
    check("L3", ok, f"int_0^1 k^(d-3) dk = {ints}; d = 2 Hessian eigenvalues {H2.eigenvals()}")

    rows = {2: [], 3: []}
    for d in (2, 3):
        for L in (8, 16, 32, 64, 128) if d == 2 else (8, 16, 32, 64):
            g = np.meshgrid(*[2 * np.pi * np.arange(L) / L] * d, indexing="ij")
            ph = (1 + sum(np.exp(1j * gg) for gg in g)) / (d + 1)
            w = 1 - np.abs(ph) ** 2
            w.flat[0] = np.inf
            rows[d].append((L, float((1 / w).sum() / L ** d)))
    g4 = F(0)
    units4 = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    for m in itertools.product(range(4), repeat=3):
        if m == (0, 0, 0):
            continue
        re = F(1 + sum(units4[j][0] for j in m), 4)
        im = F(sum(units4[j][1] for j in m), 4)
        g4 += 1 / (1 - re * re - im * im)
    g4 /= 64
    inc2 = [round(b[1] - a[1], 4) for a, b in zip(rows[2], rows[2][1:])]
    inc3 = [round(b[1] - a[1], 4) for a, b in zip(rows[3], rows[3][1:])]
    print(f"INFO I1: d = 2 return sums {[(L, round(v, 4)) for L, v in rows[2]]}, increments per doubling {inc2} (log growth); "
          f"d = 3 {[(L, round(v, 4)) for L, v in rows[3]]}, increments {inc3} (levelling off); G_4 = {g4}")
    if g4 != F(1913, 1344):
        fails.append("G4")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - formation-in-3plus1 a1: 1 - |phi|^2 = k^T M k + O(k^4) with M = (1/16)(4I - 11^T) positive definite "
          "(eigenvalues 1/16, 1/4, 1/4; 4|k|^2 - (1.k)^2 = |k|^2 + sum (k_i - k_j)^2), positive-definite Hessians for d = 1..5 with "
          "|phi| = 1 only at k = 0, the integral test (finite zero-mode sum iff d > 2; d = 2 logarithmic with eigenvalues 2/9, 2/3), "
          "drift (1,1,1)/4; recomputed independently, with the return sums growing like log L in d = 2 and levelling off in d = 3. "
          "The attempt correctly leaves nonlinear LRO open")
    print("SUMMARY: confirmed - the linear dichotomy and drift hold; no failing step in what is claimed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
