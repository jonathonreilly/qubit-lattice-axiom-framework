#!/usr/bin/env python3
"""J:note check for NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12 (on main).

The note's central number: lambda_1/lambda_0 of the half-slice packet operator T_beta = exp((beta/2)J) D_beta exp((beta/2)J) tends
to 0.1938058 (error proxy below 2e-7), from true ratios at beta <= 200 plus a 1/beta Richardson fit; the exact-coefficient route
overflows at beta = 800 (the note's words). This script re-derives the true ratios with machinery disjoint from the runner (which uses
the Bessel-determinant Wilson evaluator, scipy expm_multiply and eigsh), and carries them beyond the note's range:
  - proof step, exact: d(p,q) = (p+1)(q+1)(p+q+2)/2 satisfies 6 d = sum over the six recurrence neighbours as a polynomial identity,
    and d vanishes on the lines p = -1, q = -1, so omitting negative labels is the same boundary condition (the spectral-edge claim);
  - the Wilson coefficients from the note's own definition c_(p,q)(beta) = sum_n m^(n)_(p,q) beta^n / (6^n n!), with m^(n) the walk
    counts of the recurrence: c_(p,q) = e^beta [e^{beta(J - I)} delta_(0,0)](p,q), evaluated as a Poisson(beta)-weighted sum of
    walk probabilities J^n delta (no overflow at any beta; weights in log space); the saddle claim r/d ~ exp(-3 C2/beta) is compared;
  - e^{(beta/2)(J - I)} applied by the same Poisson-weighted walk sums on the box p, q <= S (stencil with Dirichlet truncation);
  - the top two eigenvalues by subspace iteration with Rayleigh-Ritz (three vectors), two box sizes per beta for shell stability;
  - beta in {50, 100, 200} (the note's rows, compared) and beta in {300, 400, 600, 800} (beyond), then a least-squares fit in
    powers of 1/beta over all rows and over the new rows alone.
HIT if the true ratios at the note's betas differ from its table by more than 1e-6, or if the ratios beyond beta = 200 are inconsistent
with the claimed limit 0.1938058 +- 2e-7 (the fit over all rows moves the limit by more than 1e-5).
"""
from __future__ import annotations

from math import lgamma, log, sqrt, exp

import numpy as np
import sympy as sp

STEPS = [(1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (-1, 0)]


def stencil(a):
    """(J a)[p, q] = (1/6) sum_{delta in STEPS} a[(p, q) + delta], zero outside the box; works on (..., S+1, S+1) arrays."""
    out = np.zeros_like(a)
    for dp, dq in STEPS:
        src_p = slice(max(dp, 0), a.shape[-2] + min(dp, 0))
        dst_p = slice(max(-dp, 0), a.shape[-2] + min(-dp, 0))
        src_q = slice(max(dq, 0), a.shape[-1] + min(dq, 0))
        dst_q = slice(max(-dq, 0), a.shape[-1] + min(-dq, 0))
        out[..., dst_p, dst_q] += a[..., src_p, src_q]
    return out / 6.0


def poisson_exp(a, t):
    """e^{t (J - I)} a = sum_n e^{-t} t^n / n! J^n a (Poisson weights in log space)."""
    nmax = int(t + 14 * sqrt(t) + 30)
    acc = np.zeros_like(a)
    cur = a.copy()
    for n in range(nmax + 1):
        w = exp(-t + n * log(t) - lgamma(n + 1)) if t > 0 else (1.0 if n == 0 else 0.0)
        acc += w * cur
        cur = stencil(cur)
    return acc


def diagonal_r(beta, S):
    B = S + int(10 * sqrt(beta)) + 60
    delta = np.zeros((B + 1, B + 1))
    delta[0, 0] = 1.0
    u = poisson_exp(delta, beta)
    return (u / u[0, 0])[: S + 1, : S + 1], u


def top_ratio(beta, S, iters=80, seed=1):
    r, _ = diagonal_r(beta, S)
    rng = np.random.default_rng(seed)
    V = rng.random((3, S + 1, S + 1))
    for _ in range(iters):
        W = poisson_exp(r * poisson_exp(V, beta / 2), beta / 2)
        M = W.reshape(3, -1).T
        Qm, _ = np.linalg.qr(M)
        V = Qm.T.reshape(3, S + 1, S + 1)
    W = poisson_exp(r * poisson_exp(V, beta / 2), beta / 2).reshape(3, -1)
    Vm = V.reshape(3, -1)
    small = Vm @ W.T
    ev = np.sort(np.linalg.eigvalsh((small + small.T) / 2))[::-1]
    return ev[1] / ev[0]


def fit_limit(betas, vals, powers):
    A = np.array([[1.0] + [b ** (-k) for k in powers] for b in betas])
    coef, *_ = np.linalg.lstsq(A, np.array(vals), rcond=None)
    return coef[0]


def main():
    p, q = sp.symbols("p q")
    d = lambda P, Q: (P + 1) * (Q + 1) * (P + Q + 2) / 2
    harmonic = sp.expand(sum(d(p + a, q + b) for a, b in STEPS) - 6 * d(p, q)) == 0
    walls = sp.expand(d(-1, q)) == 0 and sp.expand(d(p, -1)) == 0
    print(f"1. spectral-edge function: sum over the six neighbours of d minus 6 d = 0 as a polynomial identity: {harmonic}; d = 0 on "
          f"p = -1 and q = -1: {walls}")
    # saddle check of the diagonal
    sad = []
    for beta in (200, 800):
        r, _ = diagonal_r(beta, 40)
        for (P, Q) in ((3, 1), (6, 4), (10, 7)):
            dv = (P + 1) * (Q + 1) * (P + Q + 2) / 2
            C2 = (P * P + Q * Q + P * Q + 3 * P + 3 * Q) / 3
            sad.append((beta, (P, Q), beta * log(r[P, Q] / dv), -3 * C2))
    print("2. Wilson diagonal from Poisson-weighted walk counts: beta*log(r/d) vs -3 C2: "
          + "; ".join(f"beta={b} {pq}: {x:.3f} vs {y:.3f}" for b, pq, x, y in sad))
    note = {50: 0.200348567762, 60: 0.199245299606, 80: 0.197873420919, 100: 0.197054136330, 140: 0.196121339772, 200: 0.195424212513}
    shells = {50: (30, 36), 100: (50, 60), 200: (70, 80), 300: (84, 96), 400: (96, 112), 600: (120, 140), 800: (140, 164)}
    rows = {}
    for beta, (s1, s2) in shells.items():
        a, b = top_ratio(beta, s1), top_ratio(beta, s2)
        rows[beta] = (b, abs(a - b))
        cmp = f"; note {note[beta]:.12f}, difference {b - note[beta]:.2e}" if beta in note else ""
        print(f"3. beta = {beta}: lambda_1/lambda_0 = {b:.12f} (box {s2}; box {s1} differs by {abs(a - b):.1e}){cmp}")
    mism = [beta for beta in rows if beta in note and abs(rows[beta][0] - note[beta]) > 1e-6]
    bet = sorted(rows)
    vals = [rows[b][0] for b in bet]
    fits = {pw: fit_limit(bet, vals, pw) for pw in ((1, 2), (1, 2, 3), (1, 2, 3, 4))}
    new = [b for b in bet if b > 200]
    fit_new = fit_limit(new, [rows[b][0] for b in new], (1, 2))
    pred = {b: 0.1938058 + (rows[200][0] - 0.1938058) * 200 / b for b in new}
    print(f"4. fits of lambda_1/lambda_0 in powers of 1/beta over beta = {bet}: " + ", ".join(f"powers {k}: {v:.8f}" for k, v in fits.items())
          + f"; over beta = {new} alone (1/beta, 1/beta^2): {fit_new:.8f}; the note's limit 0.1938058; first-order predictions from the note's "
          f"limit and its beta = 200 row: " + ", ".join(f"beta={b}: {v:.7f} vs computed {rows[b][0]:.7f}" for b, v in pred.items()))
    drift = max(abs(v - 0.1938058) for v in fits.values())
    if mism or drift > 1e-5:
        print(f"HIT: true ratios disagree with the note's table at beta {mism} or the extended fit moves the limit by {drift:.2e}")
    print(f"SUMMARY: with walk-count Wilson coefficients and Poisson-walk exponentials (disjoint from the runner) the true ratios at "
          f"beta = 50, 100, 200 reproduce the note's table (max difference "
          f"{max(abs(rows[b][0] - note[b]) for b in rows if b in note):.1e}); beyond it, beta = 300, 400, 600, 800 give "
          + ", ".join(f"{rows[b][0]:.9f}" for b in new) + f" (box spread <= {max(v[1] for v in rows.values()):.0e}); fits over all rows give "
          f"limits {', '.join(f'{v:.7f}' for v in fits.values())} against the note's 0.1938058 (max drift {drift:.1e}); the spectral-edge "
          f"identity holds exactly ({harmonic and walls})")


if __name__ == "__main__":
    main()
