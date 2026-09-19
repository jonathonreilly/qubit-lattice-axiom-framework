#!/usr/bin/env python3
"""Referee of J:derive:kernel-normalization-in-3plus1:a1 (author w-macbookpro90c72-jee37, grok-4.6); referee w-jonathonsmac4f50-j303f
(claude-opus-5). Independent code (sympy, exact rationals, a seeded Monte Carlo of the exact conditional variance); nothing from the
author's check.py. Disclosure: this referee's model family refereed attempt a2 of this problem (grok; referee_w-jonathonsmac4f50-jdd85),
where G_4 = 1913/1344 was derived two ways.

Backward 3+1 with n = 4 predecessors, phi = (1 + sum_j e^{-ik_j})/4, sigma^2 = A(n beta)/(n beta), A = coth - 1/k; G_V = V^-1 sum_{k != 0}
1/(1 - |phi|^2); on the linear covariance C(0) = sigma^2 G_V and C_v (the covariance of the predecessor average) = C(0) - sigma^2 (1 - 1/V).

K1  step 1: vMF(k, u) on S^2 has E[s.u] = A, E[(s.u)^2] = 1 - 2A/k, E[(s.e_perp)^2] = A/k (sympy integrals), so
    Var(s_x | S) = A/k + (1 - 3A/k - A^2) u_x^2; with A = 1 - 1/k the projector coefficient is 2/k^2 - 1/k
K2  G_4 = 1913/1344 and C(0) - C_v = sigma^2 (1 - 1/V) = 63/64 sigma^2 on L = 4 (exact)
K3  step 2 does not follow: <A(beta|S|)/(beta|S|)> / sigma^2 is written (1 + sigma^2 c)/A(n beta), c = 1 - 1/V; that is <1/kappa>/sigma^2 and
    drops -<1/kappa^2>. Without |S| fluctuations (c = 0, |S| = n) the ratio is exactly A(n beta)/(n beta)/sigma^2 = 1, but the formula gives
    1/A(n beta). The consistent expansion (sympy) is 1 + c/(n beta) + O(1/beta^2), so R_noise = 1 + (2c - G_V)/(n beta) + O(1/beta^2), not
    1 + (3 - G_V)/(n beta); at beta = 6, n = 4, V = infinity the |S| piece is 299/288, not 599/552
K4  a Monte Carlo of the exact conditional variance (Gaussian transverse fluctuations with C(0) = sigma^2 G, C_v = sigma^2 (G - 1), seed
    fixed) agrees with 1 + (2 - G)/(n beta) and not with 1 + (3 - G)/(n beta) at beta = 6, 12, 24 and G = 1.79, 1913/1344
K5  the sign conclusion survives the correction: G_4 = 1913/1344 < 2 exactly and G_L at L = 8..64 rises to about 1.79 < 2, so the corrected
    R_noise is still above 1
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


def main():
    k, t = sp.symbols("k t", positive=True)
    Z = sp.integrate(sp.exp(k * t), (t, -1, 1))
    Es = sp.integrate(t * sp.exp(k * t), (t, -1, 1)) / Z
    Es2 = sp.integrate(t ** 2 * sp.exp(k * t), (t, -1, 1)) / Z
    A = sp.coth(k) - 1 / k
    Eperp = (1 - Es2) / 2
    ok = (sp.simplify((Es - A).rewrite(sp.exp)) == 0 and sp.simplify((Es2 - (1 - 2 * A / k)).rewrite(sp.exp)) == 0
          and sp.simplify((Eperp - A / k).rewrite(sp.exp)) == 0)
    A0 = 1 - 1 / k
    proj = sp.simplify(1 - 3 * A0 / k - A0 ** 2 - (2 / k ** 2 - 1 / k))
    check("K1", ok and proj == 0, "E[s.u] = A, E[(s.u)^2] = 1 - 2A/k, E[(s.e_perp)^2] = A/k; projector coefficient with A = 1 - 1/k is 2/k^2 - 1/k")

    units = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    G4 = F(0)
    Cv = F(0)
    for m in itertools.product(range(4), repeat=3):
        if m == (0, 0, 0):
            continue
        re = F(1 + sum(units[j][0] for j in m), 4)
        im = F(sum(units[j][1] for j in m), 4)
        u = re * re + im * im
        G4 += 1 / (1 - u)
        Cv += u / (1 - u)
    G4 /= 64
    Cv /= 64
    check("K2", G4 == F(1913, 1344) and G4 - Cv == F(63, 64), f"G_4 = {G4}; C(0) - C_v = {G4 - Cv} sigma^2 (= 1 - 1/64)")

    b, c, n = sp.symbols("beta c n", positive=True)
    s2 = (1 - 1 / (n * b)) / (n * b)
    inv1 = (1 / (n * b)) * (1 + s2 * c)
    inv2 = (1 / (n * b)) ** 2 * (1 + 2 * s2 * c)
    ratio = sp.simplify((inv1 - inv2) / s2)
    lead = sp.limit((ratio - 1) * b, b, sp.oo)
    attempt = (1 + s2 * c) / (1 - 1 / (n * b))
    att_lead = sp.limit((attempt - 1) * b, b, sp.oo)
    at_c0 = sp.simplify(attempt.subs(c, 0))
    val = ratio.subs({n: 4, b: 6, c: 1})
    att_val = attempt.subs({n: 4, b: 6, c: 1})
    ok = (sp.simplify(lead - c / n) == 0 and sp.simplify(att_lead - (c + 1) / n) == 0 and sp.simplify(ratio.subs(c, 0)) == 1
          and at_c0 != 1 and sp.nsimplify(val) == sp.Rational(299, 288) and sp.nsimplify(att_val) == sp.Rational(599, 552))
    check("K3", ok, f"consistent |S| piece: 1 + {lead}/beta + O(1/beta^2) (equal to 1 at c = 0); the attempt's (1 + sigma^2 c)/A(n beta) = 1 + "
          f"{att_lead}/beta + ..., which is {at_c0} at c = 0; at beta = 6, n = 4, c = 1: {sp.nsimplify(val)} against the attempt's "
          f"{sp.nsimplify(att_val)}; so R_noise = 1 + (2c - G_V)/(n beta) + O(1/beta^2)")

    rng = np.random.default_rng(20260919)
    Af = lambda x: 1 / np.tanh(x) - 1 / x
    rows, ok = [], True
    for beta in (6.0, 12.0, 24.0):
        s2n = Af(4 * beta) / (4 * beta)
        for G in (1.79, 1913 / 1344):
            C0, Cvn = s2n * G, s2n * (G - 1)
            rho = (16 * Cvn - 4 * C0) / 12
            Sig = np.full((4, 4), rho)
            np.fill_diagonal(Sig, C0)
            Lc = np.linalg.cholesky(Sig)
            N = 1_000_000
            th = np.einsum("ij,sjc->sic", Lc, rng.standard_normal((N, 4, 2)))
            sz = np.sqrt(np.clip(1 - (th ** 2).sum(-1), 0, None))
            S = np.concatenate([th.sum(1), sz.sum(1)[:, None]], axis=1)
            Sn = np.linalg.norm(S, axis=1)
            kk = beta * Sn
            Ak = Af(kk)
            var = Ak / kk + (1 - 3 * Ak / kk - Ak ** 2) * (S[:, 0] / Sn) ** 2
            R = var.mean() / s2n
            corr, att = 1 + (2 - G) / (4 * beta), 1 + (3 - G) / (4 * beta)
            ok &= abs(R - corr) < abs(R - att) / 10 and abs(R - corr) < 0.3 / beta ** 2
            rows.append(f"beta {beta:g}, G {G:.4f}: MC {R:.5f}, corrected {corr:.5f}, attempt {att:.5f}")
    check("K4", ok, "; ".join(rows))

    Gs = []
    for L in (8, 16, 32, 64):
        g = np.meshgrid(*[2 * np.pi * np.arange(L) / L] * 3, indexing="ij")
        ph = (1 + sum(np.exp(-1j * gg) for gg in g)) / 4
        w = 1 - np.abs(ph) ** 2
        w.flat[0] = np.inf
        Gs.append((L, float((1 / w).sum() / L ** 3)))
    ok = G4 < 2 and all(v < 2 for _, v in Gs) and Gs[-1][1] - Gs[-2][1] < 0.03
    check("K5", ok, f"G_4 = {float(G4):.4f}; G_L = {[(L, round(v, 4)) for L, v in Gs]}: all below 2, so 1 + (2 - G)/(n beta) > 1 and the sign "
          "conclusion survives")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 2 - the vMF tensor, the projector coefficient, G_4 = 1913/1344 and C(0) - C_v = sigma^2 (1 - 1/V) hold, but "
          "step 2 writes <A/kappa>/sigma^2 = (1 + sigma^2 c)/A(n beta), which is <1/kappa>/sigma^2 without the -<1/kappa^2> term of the stated "
          "truncation A = 1 - 1/kappa (it gives 1/A(n beta), not 1, when |S| does not fluctuate); the consistent expansion gives R_noise = "
          "1 + (2(1 - 1/V) - G_V)/(n beta) + O(1/beta^2), confirmed by a Monte Carlo of the exact conditional variance, so the stated "
          "1 + (3 - G)/(n beta) and 599/552 are wrong; the sign conclusion (R_noise > 1 against the executed 0.9719) survives, since G < 2 "
          "(G_4 = 1913/1344, G_64 = 1.77)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
