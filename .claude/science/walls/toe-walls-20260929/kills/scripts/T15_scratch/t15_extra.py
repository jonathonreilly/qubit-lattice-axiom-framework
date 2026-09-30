#!/usr/bin/env python3
"""T15 extra tests E (static gauge background), F (time-first convention), G (discriminating power)."""
import itertools, json, math, os
import numpy as np
from t15_test import lnZ_KS, ln_absdet

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(11)


def spatial_ops_U(N, d, U):
    sites = list(itertools.product(range(N), repeat=d))
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    A = np.zeros((n, n), dtype=complex)
    P = np.zeros((n, n))
    for s in sites:
        i = idx[s]
        P[i, i] = (-1) ** sum(s)
        for mu in range(d):
            eta = (-1) ** sum(s[:mu])
            sp = list(s); sp[mu] = (sp[mu] + 1) % N
            sm = list(s); sm[mu] = (sm[mu] - 1) % N
            u_fwd = U[(s, mu)]
            u_bwd = np.conj(U[(tuple(sm), mu)])
            A[i, idx[tuple(sp)]] += 0.5 * eta * u_fwd
            A[i, idx[tuple(sm)]] -= 0.5 * eta * u_bwd
    return A, P, sites, idx


def rand_links(N, d, strength):
    sites = list(itertools.product(range(N), repeat=d))
    return {(s, mu): np.exp(1j * strength * rng.uniform(-math.pi, math.pi)) for s in sites for mu in range(d)}


def time_shift(L):
    S = np.zeros((L, L))
    for t in range(L):
        S[t, (t + 1) % L] += 1.0 if t + 1 < L else -1.0
        S[t, (t - 1) % L] -= 1.0 if t - 1 >= 0 else -1.0
    return S


def testE(d, N, m, L, strength):
    U = rand_links(N, d, strength)
    A, P, sites, idx = spatial_ops_U(N, d, U)
    n = len(sites)
    D = m * np.eye(n * L, dtype=complex) + np.kron(A, np.eye(L)) + 0.5 * np.kron(P, time_shift(L))
    B = P @ (A + m * np.eye(n))
    assert np.allclose(B, B.conj().T)
    mu = np.linalg.eigvalsh(B)
    sym = float(np.max(np.abs(np.sort(mu) + np.sort(mu)[::-1])))
    e = np.sign(mu) * np.arcsinh(np.abs(mu))
    lhs = ln_absdet(D)
    sq = -n * L * math.log(2.0) + 2.0 * lnZ_KS(e, L)
    return dict(d=d, N=N, m=m, L=L, strength=strength, spec_symmetry_defect=sym, err_doubled=abs(lhs - sq))


def testF(d, N, m, L):
    """time-first convention: eta_t = 1 ; eta_i = (-1)^{t + sum_{j<i} x_j}. Compare |det| to time-last."""
    sites = list(itertools.product(range(N), repeat=d))
    idx = {(s, t): t * len(sites) + i for i, s in enumerate(sites) for t in range(L)}
    n = len(sites)
    D = m * np.eye(n * L, dtype=complex)
    for s in sites:
        for t in range(L):
            i = idx[(s, t)]
            # time hop, eta_t = 1, antiperiodic
            tp, sgn_p = (t + 1) % L, (1 if t + 1 < L else -1)
            tm, sgn_m = (t - 1) % L, (1 if t - 1 >= 0 else -1)
            D[i, idx[(s, tp)]] += 0.5 * sgn_p
            D[i, idx[(s, tm)]] -= 0.5 * sgn_m
            for mu in range(d):
                eta = (-1) ** (t + sum(s[:mu]))
                sp = list(s); sp[mu] = (sp[mu] + 1) % N
                sm = list(s); sm[mu] = (sm[mu] - 1) % N
                D[i, idx[(tuple(sp), t)]] += 0.5 * eta
                D[i, idx[(tuple(sm), t)]] -= 0.5 * eta
    from t15_test import euclid_D
    D2, _, _ = euclid_D(N, d, L, m)
    return dict(d=d, N=N, m=m, L=L, diff_lndet=abs(ln_absdet(D) - ln_absdet(D2)))


def testG(d, N, m, L, strength_t):
    """time-dependent random temporal phases; compare with the free doubled identity"""
    from t15_test import spatial_ops
    A, P, sites = spatial_ops(N, d)
    n = len(sites)
    D = m * np.eye(n * L, dtype=complex) + np.kron(A, np.eye(L))
    # temporal hop with link phases U_t(x,t)
    for i in range(n):
        for t in range(L):
            u = np.exp(1j * strength_t * rng.uniform(-math.pi, math.pi))
            tp = (t + 1) % L
            sg = 1.0 if t + 1 < L else -1.0
            row = t * 0 + i * L + t
            D[i * L + t, i * L + tp] += 0.5 * P[i, i] * sg * u
            D[i * L + tp, i * L + t] -= 0.5 * P[i, i] * sg * np.conj(u)
    B = P @ (A + m * np.eye(n))
    mu = np.linalg.eigvalsh(B)
    e = np.sign(mu) * np.arcsinh(np.abs(mu))
    lhs = ln_absdet(D)
    sq = -n * L * math.log(2.0) + 2.0 * lnZ_KS(e, L)
    return dict(d=d, N=N, m=m, L=L, strength_t=strength_t, err_vs_free_doubled=abs(lhs - sq))


if __name__ == "__main__":
    out = {"E": [], "F": [], "G": []}
    for (d, N, m, L, st) in [(1, 6, 0.4, 4, 1.0), (2, 4, 0.5, 4, 1.0), (2, 4, 0.5, 6, 1.0), (3, 4, 0.3, 4, 1.0), (3, 4, 0.3, 6, 0.5)]:
        r = testE(d, N, m, L, st); out["E"].append(r); print("E", r)
    for (d, N, m, L) in [(1, 4, 0.5, 4), (2, 4, 0.5, 4), (2, 4, 0.3, 6), (3, 4, 0.3, 4)]:
        r = testF(d, N, m, L); out["F"].append(r); print("F", r)
    for (d, N, m, L, st) in [(1, 6, 0.4, 4, 0.5), (2, 4, 0.5, 4, 0.5), (3, 4, 0.3, 4, 0.5)]:
        r = testG(d, N, m, L, st); out["G"].append(r); print("G", r)
    json.dump(out, open(os.path.join(HERE, "results_extra.json"), "w"), indent=1)
