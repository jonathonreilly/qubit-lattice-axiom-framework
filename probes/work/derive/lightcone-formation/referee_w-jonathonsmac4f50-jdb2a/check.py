#!/usr/bin/env python3
"""Referee of J:derive:lightcone-formation:a6 (author w-macbookpro90c72-j0029, grok-4.6); referee w-jonathonsmac4f50-jdb2a
(claude-opus-5). Independent machinery (exact integers, sympy, mpmath, numpy for one spectrum), none of the author's code.

K1  step 1 and 3: the 7-stencil pairing identity on random unit-vector configurations of (Z/3)^3 (exact integer vectors on
    the six-axis menu), and its failure for the backward stencil {0, -e_j} on a pair of unit-vector configurations
K2  step 4: the Bloch Laplacian of the doubled graph has eigenvalues E(k) and 14 - E(k) (sympy), and the Laplacian of the
    doubled graph over (Z/3)^3 has exactly the spectrum {E(k), 14 - E(k)} over the 27 momenta (numpy)
K3  step 5: 1/(1 - phi^2) = 49/(E(14 - E)) = 7/(2E(1 - E/14)); the prefactor 7/(2(1 - E/14)) is increasing on (0, 12] with
    range [7/2, 49/2], not [7/4, 7/2] as stated
K4  step 6: A'(0) = 1/3 = lim A/k, so the mean map has Jacobian (beta/3) I at S = 0; A'(k) < 1/3 and A(k)/k <= 1/3 hold for
    all k (as attempt 5 proves), yet the Wasserstein influence is not bounded by the mean map: at k = 3 the 1-Lipschitz
    f = -|s - n| has Cov(f, s.n) = 0.1136 > A'(3) = 0.1011; so 'under ||Cov|| <= 1/3 the PCA is unique for beta < 3/7' and
    'proving A' <= 1/3 would make beta < 3/7 a theorem' do not follow
K5  step 7: log(sinh k / k) = k^2/6 - k^4/180 + O(k^6)
"""
from __future__ import annotations

import itertools
import random
import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 30


def main():
    fails = 0

    def check(tag, ok, msg):
        nonlocal fails
        fails += (not ok)
        print(("PASS: " if ok else "FAIL: ") + tag + " " + msg)

    # K1
    L = 3
    MENU = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    N7 = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    NB = [(0, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
    sites = list(itertools.product(range(L), repeat=3))

    def pair(sp_, s, N):
        tot = 0
        for x in sites:
            S = [0, 0, 0]
            for z in N:
                y = tuple((x[i] + z[i]) % L for i in range(3))
                for c in range(3):
                    S[c] += s[y][c]
            tot += sum(sp_[x][c] * S[c] for c in range(3))
        return tot
    random.seed(7)
    ok7 = True
    for _ in range(200):
        s = {x: random.choice(MENU) for x in sites}
        s2 = {x: random.choice(MENU) for x in sites}
        ok7 = ok7 and pair(s2, s, N7) == pair(s, s2, N7)
    ez = (0, 0, 1)
    s = {x: ez for x in sites}
    s[(0, 0, 0)] = (1, 0, 0)
    s2 = {x: ez for x in sites}
    s2[(1, 0, 0)] = (1, 0, 0)
    lb, rb = pair(s2, s, NB), pair(s, s2, NB)
    okb = lb != rb
    check("K1", ok7 and okb, f"the 7-stencil pairing holds on 200 random six-axis configuration pairs of (Z/3)^3; the backward stencil "
          f"fails on unit-vector configurations (all +z except one +x site each): {lb} against {rb}")

    # K2
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    E = sum(2 * (1 - sp.cos(k)) for k in (k1, k2, k3))
    a = 1 + 2 * (sp.cos(k1) + sp.cos(k2) + sp.cos(k3))
    Lb = sp.Matrix([[7, -a], [-a, 7]])
    ev = list(Lb.eigenvals().keys())
    okb2 = any(sp.simplify(e - E) == 0 for e in ev) and any(sp.simplify(e - (14 - E)) == 0 for e in ev)
    try:
        import numpy as np
        n = len(sites)
        idx = {x: i for i, x in enumerate(sites)}
        Lap = np.zeros((2 * n, 2 * n))
        for x in sites:
            for z in N7:
                y = tuple((x[i] + z[i]) % L for i in range(3))
                Lap[idx[x], n + idx[y]] -= 1
                Lap[n + idx[y], idx[x]] -= 1
        for i in range(2 * n):
            Lap[i, i] = -Lap[i].sum()
        num = np.sort(np.linalg.eigvalsh(Lap))
        pred = []
        for kv in itertools.product(range(L), repeat=3):
            Ek = sum(2 * (1 - np.cos(2 * np.pi * c / L)) for c in kv)
            pred += [Ek, 14 - Ek]
        okn = np.allclose(num, np.sort(pred), atol=1e-9) and np.allclose(np.diag(Lap), 7)
    except Exception:
        okn = False
    check("K2", okb2 and okn, "the Bloch Laplacian [[7, -a], [-a, 7]], a = 1 + 2 sum cos k_j = 7 - E, has eigenvalues E and 14 - E; the "
          "doubled graph over (Z/3)^3 (degree 7) has exactly the spectrum {E(k), 14 - E(k)} over its 27 momenta")

    # K3
    Ev = sp.symbols("E", positive=True)
    phi = 1 - Ev / 7
    ok = sp.simplify(1 / (1 - phi ** 2) - 49 / (Ev * (14 - Ev))) == 0 and sp.simplify(49 / (Ev * (14 - Ev)) - 7 / (2 * Ev * (1 - Ev / 14))) == 0
    pref = 7 / (2 * (1 - Ev / 14))
    lo = sp.limit(pref, Ev, 0)
    hi = pref.subs(Ev, 12)
    inc = sp.simplify(sp.diff(pref, Ev)) 
    ok = ok and lo == sp.Rational(7, 2) and hi == sp.Rational(49, 2) and all(inc.subs(Ev, e) > 0 for e in (sp.Rational(1, 10), 6, 12))
    check("K3", ok, f"1/(1 - phi^2) = 49/(E(14 - E)) = 7/(2E(1 - E/14)); the prefactor 7/(2(1 - E/14)) increases from {lo} (E -> 0) to "
          f"{hi} (E = 12): its range on (0, 12] is [7/2, 49/2], not the stated [7/4, 7/2] (7/4 would need E = -14)")

    # K4
    kk = sp.symbols("k", positive=True)
    lim1 = sp.limit(1 / kk ** 2 - 1 / sp.sinh(kk) ** 2, kk, 0)
    lim2 = sp.limit((kk * sp.cosh(kk) - sp.sinh(kk)) / (kk ** 2 * sp.sinh(kk)), kk, 0)
    kap = mp.mpf(3)
    Z = mp.quad(lambda m: mp.e ** (kap * m), [-1, 1])

    def Ex(g):
        return mp.quad(lambda m: g(m) * mp.e ** (kap * m), [-1, 1]) / Z
    f = lambda m: -mp.sqrt(2 * (1 - m))
    cov = Ex(lambda m: f(m) * m) - Ex(f) * Ex(lambda m: m)
    Ap3 = 1 / kap ** 2 - 1 / mp.sinh(kap) ** 2
    grid_ok = all((1 / x ** 2 - 1 / mp.sinh(x) ** 2) < mp.mpf(1) / 3 and (mp.coth(x) - 1 / x) / x <= mp.mpf(1) / 3
                  for x in [mp.mpf(i) / 10 for i in range(1, 300)])
    ok = lim1 == sp.Rational(1, 3) and lim2 == sp.Rational(1, 3) and grid_ok and cov > Ap3 + mp.mpf("0.01")
    check("K4", ok, f"A'(0) = {lim1} = lim A(k)/k, so the mean map has Jacobian (beta/3) I at 0, and A' < 1/3, A/k <= 1/3 on (0, 30); but at "
          f"k = 3 the 1-Lipschitz f = -|s - n| has Cov(f, s.n) = {mp.nstr(cov, 6)} > A'(3) = {mp.nstr(Ap3, 6)}: the Wasserstein influence "
          "of a predecessor is not the mean map's Lipschitz constant, so the conditional uniqueness 'for beta < 3/7 under ||Cov|| <= 1/3' "
          "and the remark that proving A' <= 1/3 would close it do not follow (A' <= 1/3 is true, and the gap remains)")

    # K5
    ser = sp.series(sp.log(sp.sinh(kk) / kk), kk, 0, 7).removeO()
    ok = ser.coeff(kk, 2) == sp.Rational(1, 6) and ser.coeff(kk, 4) == sp.Rational(-1, 180) and ser.coeff(kk, 0) == 0
    check("K5", ok, f"log(sinh k/k) = {ser} (series to k^6), i.e. k^2/6 - k^4/180 + O(k^6)")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 5 - its stated range of the kernel prefactor, 7/(2(1 - E/14)) in [7/4, 7/2] on E in (0, 12], is wrong: "
          "the prefactor increases from 7/2 to 49/2; and step 6's conditional uniqueness (beta < 3/7 from ||Cov_vMF|| <= 1/3) does not "
          "follow, because the Wasserstein influence exceeds the mean map's Lipschitz constant (witness at k = 3), so proving A' <= 1/3 "
          "does not close it. What holds, re-verified: the 7-stencil pairing and its failure for the backward stencil, reversibility "
          "w.r.t. prod Z, the doubled-graph spectrum {E, 14 - E} (symbolically and on (Z/3)^3), the identity 1/(1 - phi^2) = "
          "49/(E(14 - E)), the linearised coefficient 7 beta/3, and log(sinh k/k) = k^2/6 - k^4/180 + O(k^6)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
