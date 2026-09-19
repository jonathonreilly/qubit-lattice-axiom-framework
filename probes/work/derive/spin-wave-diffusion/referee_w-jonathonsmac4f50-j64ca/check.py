#!/usr/bin/env python3
"""Referee of J:derive:spin-wave-diffusion:a1 (author w-macbookpro90c72-j2b02, grok-4.6); referee w-jonathonsmac4f50-j64ca
(claude-opus-5). Provenance: the attempt proves the L = 1 law that this referee family's a2 report (referee_w-jonathonsmac4f50-j1ab5,
check V5) recorded as 1/A(3 beta) up to e^{-6 beta}; the checks below are written afresh (sympy, mpmath quadrature).

U1  step 1: for vMF(k u) on S^2, E|s - u|^2 = 2 - 2A(k) (quadrature) and A(k) = 1 - 1/k + 2/(e^{2k} - 1) (identity)
U2  step 2: k(1 - A(k)) = 1 - 2k/(e^{2k} - 1), so at L = 1 (k = 3 beta, sigma^2 = A/k, one-step D_1 = 1 - A) the ratio is
    [1 - 6 beta/(e^{6 beta} - 1)]/A(3 beta); its 1/beta expansion is 1 + 1/(3 beta) + 1/(9 beta^2) + O(beta^-3) up to e^{-6 beta} terms
    (checked against the exact value at beta = 6, 12, 24, 48 to the next order), not identically 1
U3  step 3-4: G_4 = 189/128, G_1 = 0 (empty sum); (n_x/eps)^2 -> 1/m^2 for n = M/|M|, M = (eps, 0, m)
U4  (INFO) the script's estimator at lag l on L = 1 is (1 - A^l)/l, not 1 - A: the attempt's D_1 is the one-step rate
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction

import mpmath as mp
import sympy as sp

mp.mp.dps = 30


def main():
    fails = 0

    def check(tag, ok, msg):
        nonlocal fails
        fails += (not ok)
        print(("PASS: " if ok else "FAIL: ") + tag + " " + msg)

    k = sp.symbols("k", positive=True)
    E2 = sp.exp(2 * k)
    Aexpr = (E2 + 1) / (E2 - 1) - 1 / k                      # coth k written with exponentials
    ok_id = sp.simplify(Aexpr - (1 - 1 / k + 2 / (E2 - 1))) == 0
    ok = ok_id
    for kv in (mp.mpf("0.7"), mp.mpf(3), mp.mpf(10)):
        Am = mp.coth(kv) - 1 / kv
        # E|s - u|^2 = E[2 - 2 s.u], s.u = mu with density k e^{k mu}/(2 sinh k) on [-1, 1]
        val = mp.quad(lambda mu: (2 - 2 * mu) * kv * mp.e ** (kv * mu) / (2 * mp.sinh(kv)), [-1, 1])
        ok = ok and abs(val - (2 - 2 * Am)) < mp.mpf(10) ** -25
    check("U1", ok, "E|s - u|^2 = 2 - 2A(k) by quadrature at k = 0.7, 3, 10, and A(k) = 1 - 1/k + 2/(e^{2k} - 1) identically")

    ok = sp.simplify(k * (1 - Aexpr) - (1 - 2 * k / (E2 - 1))) == 0
    rows = []
    resids = []
    for beta in (6, 12, 24, 48):
        kv = mp.mpf(3 * beta)
        Am = mp.coth(kv) - 1 / kv
        ratio = (1 - 6 * mp.mpf(beta) / (mp.e ** (6 * beta) - 1)) / Am
        direct = (1 - Am) / (Am / kv)
        approx = 1 + mp.mpf(1) / (3 * beta) + mp.mpf(1) / (9 * beta ** 2)
        resid = (ratio - approx) * beta ** 3
        ok = ok and abs(ratio - direct) < mp.mpf(10) ** -25
        resids.append(resid)
        rows.append(f"beta = {beta}: {mp.nstr(ratio, 12)} (beta^3 x remainder = {mp.nstr(resid, 6)})")
    ok = ok and all(abs(resids[i + 1] - mp.mpf(1) / 27) < abs(resids[i] - mp.mpf(1) / 27) for i in range(3)) and abs(resids[-1] - mp.mpf(1) / 27) < mp.mpf("0.0005")
    check("U2", ok, "k(1 - A(k)) = 1 - 2k/(e^{2k} - 1); the L = 1 one-step ratio (1 - A)/sigma^2 equals [1 - 6 beta/(e^{6 beta} - 1)]/A(3 beta): "
          + "; ".join(rows) + " - so it is 1 + 1/(3 beta) + 1/(9 beta^2) + 1/(27 beta^3) + ..., not identically 1")

    cosr = {0: 1, 1: 0, 2: -1, 3: 0}
    G4 = sum(1 / (Fraction(6 - 2 * cosr[a] - 2 * cosr[b] - 2 * cosr[(a - b) % 4], 9)) for a in range(4) for b in range(4) if (a, b) != (0, 0)) / 16
    eps, m = sp.symbols("epsilon m", positive=True)
    jac = sp.limit((eps / sp.sqrt(m ** 2 + eps ** 2) / eps) ** 2, eps, 0)
    ok = G4 == Fraction(189, 128) and jac == 1 / m ** 2
    check("U3", ok, f"G_4 = {G4}, G_1 = 0 (no nonzero mode on L = 1), and (n_x/eps)^2 -> {jac}")

    Am = mp.coth(18) - mp.mpf(1) / 18
    one = 1 - Am
    lag25 = (1 - Am ** 25) / 25
    print(f"INFO: U4 on L = 1 at beta = 6 the script's estimator at lag l is (1 - A^l)/l: {mp.nstr(one, 6)} at l = 1 and {mp.nstr(lag25, 6)} "
          "at l = 25 (the script's smallest lag): the attempt's D_1 = 1 - A(3 beta) is the one-step rate, the natural reading of a "
          "diffusion constant, not the script's lag-25 number on L = 1")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - a1's exact L = 1 law survives: the one-step direction rate is 1 - A(3 beta), so D_1 L^2/sigma^2 = "
          "[1 - 6 beta/(e^{6 beta} - 1)]/A(3 beta) = 1 + 1/(3 beta) + 1/(9 beta^2) + O(beta^-3), not identically 1, which contradicts a2's "
          "1/(1 - sigma^2 G_L)^2 (= 1 at L = 1) as a finite-L identity; the chordal moment, the exponential form of A, G_4 = 189/128 and "
          "the Jacobian limit re-verified; D_1 here is the one-step rate (the script's lag-25 estimator saturates on L = 1)")
    print("SUMMARY: confirmed - no failing step; provenance disclosed (the L = 1 observation first appears in this referee family's "
          "a2 report); the general-L combination is left open, as the attempt says")
    return 0


if __name__ == "__main__":
    sys.exit(main())
