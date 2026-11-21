#!/usr/bin/env python3
"""Exact lemmas on the cross-ratio, Text 20 of parts/upper-chain.md.

Criteria, written before the run.
C1 Lemma 20.1: Z positive on X x Y, positive kernels from X-bar to X and from Y-bar to Y.
   sup |log CR| of the averaged kernel <= sup |log CR| of Z, up to 1e-9 relative. 2000 trials.
C2 Lemma 20.2: K1, K2 positive with sup |log CR| = e1, e2 <= 1/4, rho any positive measure on the
   middle pair (x, y), not a product. Then |log CR(K1 rho K2)| <= 4 artanh(sinh e1 sinh e2 exp(e1 + e2)),
   and this is <= 7 e1 e2. 2000 trials.
C3 Positive additive term: 0 <= Zx <= tau Z0 gives log CR(Z0 + Zx) <= log CR(Z0) + 2 log(1 + tau). 2000 trials.
C4 Finding F20.1, a failure that must be exhibited: Z(a, b) = sum z_i(a) z'_k(b) exp(m_ik), positive for all
   (a, b), with |m_ik| <= mu, has |log CR| >= 100 mu when signed activities nearly cancel.
   PASS means the failure is exhibited. It refutes the sentence, not any theorem.
"""
import math
import resource

import numpy as np

RSS_LIMIT_GB = 2.0


def rss_guard():
    # macOS reports ru_maxrss in bytes
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9 > RSS_LIMIT_GB:
        raise SystemExit("RSS above limit")


def sup_log_cr(Z):
    L = np.log(Z)
    # L[a,b] + L[a',b'] - L[a,b'] - L[a',b], over all quadruples
    D = L[:, None, :, None] + L[None, :, None, :] - L[:, None, None, :] - L[None, :, :, None]
    return float(np.max(np.abs(D)))


def near_product(rng, n, m, eps):
    u, v = np.exp(rng.normal(size=n)), np.exp(rng.normal(size=m))
    return np.outer(u, v) * np.exp(eps * rng.uniform(-1, 1, size=(n, m)))


def c1(rng):
    worst = 0.0
    for _ in range(2000):
        n, m = rng.integers(2, 7, size=2)
        Z = np.exp(rng.normal(scale=rng.uniform(0.1, 3), size=(n, m)))
        P = rng.exponential(size=(rng.integers(2, 6), n))
        Q = rng.exponential(size=(rng.integers(2, 6), m))
        worst = max(worst, sup_log_cr(P @ Z @ Q.T) / sup_log_cr(Z))
    print(f"C1: max ratio averaged/original = {worst:.6f} (claim <= 1)")
    return worst <= 1 + 1e-9


def c2(rng):
    worst_exact = worst_prod = 0.0
    for _ in range(2000):
        n, m, r, s = rng.integers(2, 7, size=4)
        K1 = near_product(rng, n, r, rng.uniform(0.005, 0.1))
        K2 = near_product(rng, s, m, rng.uniform(0.005, 0.1))
        e1, e2 = sup_log_cr(K1), sup_log_cr(K2)
        if max(e1, e2) > 0.25:
            continue
        rho = np.exp(rng.normal(scale=rng.uniform(0, 6), size=(r, s)))
        Z = K1 @ rho @ K2
        got = sup_log_cr(Z)
        bound = 4 * math.atanh(math.sinh(e1) * math.sinh(e2) * math.exp(e1 + e2))
        worst_exact = max(worst_exact, got / bound)
        worst_prod = max(worst_prod, got / (e1 * e2))
    print(f"C2: max got/bound = {worst_exact:.4f} (claim <= 1); max got/(e1 e2) = {worst_prod:.4f} (claim <= 7)")
    return worst_exact <= 1 + 1e-9 and worst_prod <= 7


def c3(rng):
    worst = -math.inf
    for _ in range(2000):
        n, m = rng.integers(2, 7, size=2)
        Z0 = np.exp(rng.normal(size=(n, m)))
        tau = rng.uniform(0, 1)
        Zx = tau * Z0 * rng.uniform(0, 1, size=(n, m))
        worst = max(worst, sup_log_cr(Z0 + Zx) - sup_log_cr(Z0) - 2 * math.log(1 + tau))
    print(f"C3: max excess = {worst:.3e} (claim <= 0)")
    return worst <= 1e-12


def c4():
    mu = 1e-3
    delta = 2e-2
    # activities at (a, a') and at (b, b'): one state where the signed sum nearly cancels
    za = np.array([[1.0, -1.0 + delta], [1.0, 0.0]])
    zb = za.copy()
    m = np.zeros((2, 2))
    Z = np.zeros((2, 2))
    for ia in range(2):
        for ib in range(2):
            for i in range(2):
                for k in range(2):
                    m_ik = mu if (ia, ib, i, k) == (0, 0, 0, 0) else 0.0
                    Z[ia, ib] += za[ia, i] * zb[ib, k] * math.exp(m_ik)
    assert np.all(Z > 0)
    cr = abs(math.log(Z[0, 0] * Z[1, 1] / (Z[0, 1] * Z[1, 0])))
    print(f"C4: mu = {mu:.1e}, signed sum U = {delta:.1e}, all Z positive, |log CR| = {cr:.3f}, ratio to mu = {cr / mu:.0f}")
    return cr >= 100 * mu


def main():
    rng = np.random.default_rng(20261031)
    ok = {"C1": c1(rng), "C2": c2(rng), "C3": c3(rng), "C4": c4()}
    rss_guard()
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")


if __name__ == "__main__":
    main()
