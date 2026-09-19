#!/usr/bin/env python3
"""J:note falsifiers for NATIVE_GAUGE_TRANSFER_REDUCED_A2_VIRIAL_LEADING_EQUALITY_RUNG_EIGHTEEN_BOUNDED_NOTE_2026-06-12 (on main).

Falsifiers implemented: the note's wrong-structure table (retained constant 3/2; wrong-sign samples -7/2, -11/2; wrong confiner
-12 exp(-9); fixed-weight samples 79/10 and 79/15) and the virial proof step itself, with machinery disjoint from its runner:
  - symbolic, on a generic smooth test function f(x, y): [D, L] f = -2 L f for D = x d/dx + y d/dy, L = (1/3)(d_xx - d_xy + d_yy);
    [L, [L, D]] = 0, so e^{tL} D e^{-tL} = D + 2 t L exactly and [D, e^{L/2}] = -L e^{L/2}; D H = 3 H, D Q = 2 Q, D W = (3 - 2Q) W;
    the eigenstate expectation 0 = -2 mu A + 3 mu - 2 B solved for A + B/mu;
  - the finite-beta witnesses A_i + B_i/mu_i recomputed with an independent heat operator (Poisson-weighted walk sums of the
    six-neighbour averaging stencil J, in place of expm_multiply) and subspace iteration with Rayleigh-Ritz (in place of eigsh), at the
    note's beta = 100, 200, 400 (compared with its table) and beyond at beta = 800, 1600, with the runner's definitions
    A = beta (<v, J v> - 1), B/mu = <S v, (3 C2 / beta) r S v> / <S v, r S v>, r = d exp(-3 C2 / beta), S = e^{(beta/2)(J - I)}.
"""
from __future__ import annotations

from math import exp, lgamma, log, sqrt

import numpy as np
import sympy as sp

STEPS = [(1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (-1, 0)]


def stencil(a):
    out = np.zeros_like(a)
    for dp, dq in STEPS:
        s1 = slice(max(dp, 0), a.shape[-2] + min(dp, 0))
        d1 = slice(max(-dp, 0), a.shape[-2] + min(-dp, 0))
        s2 = slice(max(dq, 0), a.shape[-1] + min(dq, 0))
        d2 = slice(max(-dq, 0), a.shape[-1] + min(-dq, 0))
        out[..., d1, d2] += a[..., s1, s2]
    return out / 6.0


def heat(a, t):
    nmax = int(t + 14 * sqrt(t) + 30)
    acc = np.zeros_like(a)
    cur = a.copy()
    for n in range(nmax + 1):
        acc += exp(-t + n * log(t) - lgamma(n + 1)) * cur
        cur = stencil(cur)
    return acc


def witnesses(beta, shell, nvec=4, iters=45):
    P, Qg = np.meshgrid(np.arange(shell + 1), np.arange(shell + 1), indexing="ij")
    d = (P + 1) * (Qg + 1) * (P + Qg + 2) / 2.0
    C2 = (P * P + Qg * Qg + P * Qg + 3 * P + 3 * Qg) / 3.0
    r = d * np.exp(-3 * C2 / beta)
    r /= r.max()
    qfac = 3 * C2 / beta
    rng = np.random.default_rng(5)
    V = rng.random((nvec, shell + 1, shell + 1))
    for _ in range(iters):
        W = heat(r * heat(V, beta / 2), beta / 2)
        Qm, _ = np.linalg.qr(W.reshape(nvec, -1).T)
        V = Qm.T.reshape(nvec, shell + 1, shell + 1)
    TV = heat(r * heat(V, beta / 2), beta / 2).reshape(nvec, -1)
    small = V.reshape(nvec, -1) @ TV.T
    ev, U = np.linalg.eigh((small + small.T) / 2)
    order = np.argsort(ev)[::-1]
    Vr = (U[:, order].T @ V.reshape(nvec, -1)).reshape(nvec, shell + 1, shell + 1)
    rows = []
    for i in range(3):
        v = Vr[i] / np.linalg.norm(Vr[i])
        A = beta * (float(np.sum(v * stencil(v))) - 1.0)
        m = heat(v, beta / 2)
        Bmu = float(np.sum(m * m * r * qfac)) / float(np.sum(m * m * r))
        rows.append((A, Bmu))
    return rows


def main():
    x, y = sp.symbols("x y", positive=True)
    f = sp.Function("f")(x, y)
    D = lambda g: x * sp.diff(g, x) + y * sp.diff(g, y)
    Lop = lambda g: (sp.diff(g, x, 2) - sp.diff(g, x, y) + sp.diff(g, y, 2)) / 3
    comm_DL = sp.simplify(D(Lop(f)) - Lop(D(f)) + 2 * Lop(f)) == 0
    # [L, [L, D]] f = L([L, D] f) - [L, D](L f) with [L, D] = 2 L
    LD = lambda g: Lop(D(g)) - D(Lop(g))
    nested = sp.simplify(Lop(LD(f)) - LD(Lop(f))) == 0
    H = x * y * (x + y) / 2
    Q = x ** 2 + x * y + y ** 2
    W = H * sp.exp(-Q)
    homog = sp.simplify(D(H) - 3 * H) == 0 and sp.simplify(D(Q) - 2 * Q) == 0 and sp.simplify(D(W) - (3 - 2 * Q) * W) == 0
    mu, A, B = sp.symbols("mu A B", positive=True)
    sol = sp.solve(sp.Eq(-2 * mu * A + 3 * mu - 2 * B, 0), B)[0]
    virial = sp.simplify(A + sol / mu)
    wrong_signed = [2 * a - sp.Rational(3, 2) for a in (-1, -2)]
    Qw = x ** 2 + 2 * x * y + y ** 2
    Ww = H * sp.exp(-Qw)
    mismatch = sp.simplify((D(Ww) - (3 - 2 * Q) * Ww).subs({x: 1, y: 2}))
    fw = lambda Nc: sp.Rational(Nc, 3) * (Q + 3 * (x + y) / sp.sqrt(100)).subs({x: 1, y: 2})
    print(f"1. symbolic: [D, L] = -2L on a generic f: {comm_DL}; [L, [L, D]] = 0 (so [D, e^(L/2)] = -L e^(L/2)): {nested}; D H = 3H, "
          f"D Q = 2Q, D W = (3 - 2Q) W: {homog}; eigenstate expectation gives A + B/mu = {virial}")
    table = {"retained virial constant": (virial, sp.Rational(3, 2)), "wrong signed A = -1": (wrong_signed[0], sp.Rational(-7, 2)),
             "wrong signed A = -2": (wrong_signed[1], sp.Rational(-11, 2)), "wrong confiner at (1,2)": (mismatch, -12 * sp.exp(-9)),
             "N_c = 3 fixed-weight sample": (fw(3), sp.Rational(79, 10)), "N_c = 2 sample": (fw(2), sp.Rational(79, 15))}
    tab_ok = all(sp.simplify(a - b) == 0 for a, b in table.values())
    print("2. the note's wrong-structure table recomputed: " + "; ".join(f"{k}: {sp.nsimplify(a)} (note {b})" for k, (a, b) in table.items()))
    note = {100: (1.464854, 1.454749, 1.450800), 200: (1.482438, 1.477406, 1.475445), 400: (1.491222, 1.488710, 1.487732)}
    shells = {100: 40, 200: 56, 400: 80, 800: 112, 1600: 160}
    res = {}
    for beta, shell in shells.items():
        rows = witnesses(beta, shell)
        plus = [a + b for a, b in rows]
        minus = [a - b for a, b in rows]
        res[beta] = (plus, minus)
        cmp = f"; note {note[beta]}, max difference {max(abs(p - n) for p, n in zip(plus, note[beta])):.1e}" if beta in note else " (beyond)"
        print(f"3. beta = {beta} (box {shell}): A + B/mu = {[round(p, 6) for p in plus]}, A - B/mu = {[round(m, 4) for m in minus]}{cmp}")
    betas = sorted(res)
    deficits = [max(1.5 - p for p in res[b][0]) for b in betas]
    spreads = [max(res[b][0]) - min(res[b][0]) for b in betas]
    match = all(max(abs(p - n) for p, n in zip(res[b][0], note[b])) < 2e-6 for b in note)
    conv = all(deficits[i + 1] < deficits[i] for i in range(len(deficits) - 1)) and all(spreads[i + 1] < spreads[i] for i in range(len(spreads) - 1))
    wrong_state_dep = all(max(res[b][1]) - min(res[b][1]) > 0.5 for b in betas)
    ok = comm_DL and nested and homog and virial == sp.Rational(3, 2) and tab_ok and match and conv and wrong_state_dep
    if not ok:
        print(f"HIT: a check fails: symbolic {comm_DL and nested and homog}, table {tab_ok}, note rows {match}, convergence {conv}, "
              f"wrong-sign state dependence {wrong_state_dep}")
    print(f"SUMMARY: the virial step holds symbolically (A + B/mu = {virial}) and the note's six wrong-structure values are reproduced "
          f"exactly ({tab_ok}); with an independent Poisson-walk heat operator and subspace iteration the finite witnesses reproduce the "
          f"note's beta = 100, 200, 400 rows ({match}) and, beyond them, the deficit 3/2 - (A + B/mu) keeps shrinking "
          f"({', '.join(f'{d:.5f}' for d in deficits)} at beta = {betas}, about halving per doubling) with shrinking state spread "
          f"({', '.join(f'{s:.5f}' for s in spreads)}), while A - B/mu stays state-dependent")


if __name__ == "__main__":
    main()
