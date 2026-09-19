#!/usr/bin/env python3
"""Probe: NATIVE_GAUGE_TRANSFER_REDUCED_A2_EIGENVALUE_RATIO_EPS_CANCELLATION_RUNG_TWENTY_BOUNDED_NOTE_2026-06-12.

Machinery disjoint from the runner (exact-Wilson Bessel/Weyl determinants on a
fixed box, fits over beta in {60,...,200}): Wilson ratios from the character
recurrence integrated as Poisson-weighted six-neighbour walk sums; the operator
T_beta = e^{(beta/2)J} diag(r) e^{(beta/2)J} on elliptical regions
(p+1)^2 + (p+1)(q+1) + (q+1)^2 <= R^2 in the swap-symmetric sector, converged
between two radii (single radius at beta = 960).

 E  exact identities (sympy): R H = (u^2+2xy)/2, R Q = 3u, R[H e^-Q] = P_1 e^-Q,
    R(Q H e^-Q) = (3uH + Q P_1) e^-Q, P_1(1,2) = -41/2, P_2(1,2) = 135/2 with
    P_2 = G_2 - 3u G_1 + (9/2) u^2 H, 3uH(1,2) = 27, A1 discriminant degree 1 vs
    A2 2H degree 3; <v|[C,T0]|v> on random symmetric T0 of sizes 10..400.
 W  exact-Wilson witness rows beyond the note's range: Lambda = log(l1/l0) at
    beta = 60, 90, 120, 150, 200, 300, 500, 960; the Hellmann identity
    c_J - c_D = -beta dLambda/dbeta by central differences (beta = 30, 120, 300);
    fits Lambda = L_inf + b beta^-1/2 + a_2/beta + a_3 beta^-3/2 (+ a_4/beta^2)
    on the note's five betas and on all eight; forced b = 0; Richardson of
    beta(c_J - c_D).  The note's falsifier rows: |b| < 0.02, a_2 in (1.55, 1.75).
 H  the heat piece a_2^heat = (1/4)(||L Phi_1||^2 - ||L Phi_0||^2) read from the
    lattice eigenvectors with L ~ beta (J - I), at every beta of W
    (the note: ~1.0 > 0 on its reduced grid).

Prints SUMMARY: lines; HIT: only when a stated fact of the note fails.
"""
import sys
import time
from math import exp, lgamma, log, sqrt

import numpy as np
import sympy as sp
from scipy import sparse

STEPS = [(1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (-1, 0)]
HITS = []


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


# ------------------------------------------------------------------------------------------------ E
def run_E():
    print("=" * 78)
    print("E  exact identities and table values")
    x, y = sp.symbols("x y", positive=True)
    u = x + y
    H = x * y * u / 2
    Q = x ** 2 + x * y + y ** 2
    R = lambda f: sp.diff(f, x) + sp.diff(f, y)
    P1 = (u ** 2 + 2 * x * y) / 2 - 3 * u * H
    G1, G2 = (u ** 2 + 2 * x * y) / 2, 3 * u / 2
    P2 = G2 - 3 * u * G1 + sp.Rational(9, 2) * u ** 2 * H
    ok = {
        "R H": sp.expand(R(H) - (u ** 2 + 2 * x * y) / 2) == 0,
        "R Q": sp.expand(R(Q) - 3 * u) == 0,
        "R[H e^-Q] = P_1 e^-Q": sp.simplify(R(H * sp.exp(-Q)) - P1 * sp.exp(-Q)) == 0,
        "R(Q H e^-Q)": sp.simplify(R(Q * H * sp.exp(-Q)) - (3 * u * H + Q * P1) * sp.exp(-Q)) == 0,
    }
    vals = {"P_1(1,2)": P1.subs({x: 1, y: 2}), "P_2(1,2)": P2.subs({x: 1, y: 2}), "3uH(1,2)": (3 * u * H).subs({x: 1, y: 2}),
            "A1 degree": sp.Poly(x, x, y).total_degree(), "A2 2H degree": sp.Poly(sp.expand(2 * H), x, y).total_degree()}
    rng = np.random.default_rng(20)
    worst = 0.0
    for n in (10, 50, 100, 400):
        A = rng.standard_normal((n, n))
        T0 = A + A.T
        C = rng.standard_normal((n, n))
        w, V = np.linalg.eigh(T0)
        comm = C @ T0 - T0 @ C
        worst = max(worst, max(abs(V[:, i] @ comm @ V[:, i]) / np.linalg.norm(comm) for i in range(0, n, max(1, n // 10))))
    print(f"  identities {ok}; values {dict((k, str(v)) for k, v in vals.items())}; max |<v|[C,T0]|v>|/||[C,T0]|| {worst:.1e}")
    good = all(ok.values()) and vals["P_1(1,2)"] == sp.Rational(-41, 2) and vals["P_2(1,2)"] == sp.Rational(135, 2) \
        and vals["3uH(1,2)"] == 27 and vals["A1 degree"] == 1 and vals["A2 2H degree"] == 3 and worst < 1e-12
    if not good:
        hit("an exact identity or table value of the note fails")
    return ok, vals, worst


# ------------------------------------------------------------------------------------------------ lattice machinery
def stencil(a):
    out = np.zeros_like(a)
    n = a.shape[0]
    for dp, dq in STEPS:
        out[max(-dp, 0): n + min(-dp, 0), max(-dq, 0): n + min(-dq, 0)] += a[max(dp, 0): n + min(dp, 0), max(dq, 0): n + min(dq, 0)]
    return out / 6.0


def coefficients(beta, reach):
    B = int(reach) + int(10 * sqrt(beta)) + 60
    a = np.zeros((B + 1, B + 1))
    a[0, 0] = 1.0
    acc = np.zeros_like(a)
    for n in range(int(beta + 14 * sqrt(beta) + 40) + 1):
        acc += exp(-beta + n * log(beta) - lgamma(n + 1)) * a
        a = stencil(a)
    return acc / acc[0, 0]


def ellipse_sites(R):
    return [(p, q) for p in range(int(R) + 1) for q in range(int(R) + 1)
            if (p + 1) ** 2 + (p + 1) * (q + 1) + (q + 1) ** 2 <= R * R]


def sector(sites, rf):
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    rows, cols = [], []
    for (p, q), i in idx.items():
        for dp, dq in STEPS:
            k = (p + dp, q + dq)
            if k in idx:
                rows.append(idx[k])
                cols.append(i)
    J = sparse.csr_matrix((np.full(len(rows), 1 / 6), (rows, cols)), shape=(n, n))
    r = np.array([rf[p, q] for (p, q) in sites])
    Bn = rf.shape[0]
    cp = np.array([sum(rf[p + dp, q + dq] for dp, dq in STEPS if 0 <= p + dp < Bn and 0 <= q + dq < Bn) / 6.0 for (p, q) in sites])
    cp00 = (rf[1, 0] + rf[0, 1]) / 6.0
    rp = cp - r * cp00
    ur, uc, uv, m = [], [], [], 0
    for (p, q) in sites:
        if p < q and (q, p) in idx:
            ur += [idx[(p, q)], idx[(q, p)]]
            uc += [m, m]
            uv += [1 / sqrt(2), 1 / sqrt(2)]
            m += 1
        elif p == q:
            ur.append(idx[(p, p)])
            uc.append(m)
            uv.append(1.0)
            m += 1
    U = sparse.csr_matrix((uv, (ur, uc)), shape=(n, m))
    Js = (U.T @ J @ U).toarray()
    rs = (U.T @ sparse.diags(r) @ U).diagonal()
    rps = (U.T @ sparse.diags(rp) @ U).diagonal()
    return Js, rs, rps


def spectral(beta, R, rf, want_heat=False):
    Js, rs, rps = sector(ellipse_sites(R), rf)
    w, V = np.linalg.eigh(Js)
    E = (V * np.exp(beta / 2 * (w - w.max()))) @ V.T
    del V
    T = E @ (rs[:, None] * E)
    lam, W = np.linalg.eigh(T)
    del T
    o = np.argsort(lam)[::-1][:2]
    (l0, l1), (v0, v1) = (lam[o[0]], lam[o[1]]), (W[:, o[0]], W[:, o[1]])
    cJ = beta * (v0 @ Js @ v0 - v1 @ Js @ v1)
    Ev0, Ev1 = E @ v0, E @ v1
    cD = beta * ((Ev1 @ (rps * Ev1)) / l1 - (Ev0 @ (rps * Ev0)) / l0)
    heat = None
    if want_heat:
        g0 = Js @ v0 - v0
        g1 = Js @ v1 - v1
        heat = 0.25 * beta * beta * (g1 @ g1 - g0 @ g0)
    return log(l1 / l0), cJ, cD, heat, Js.shape[0]


def radii(beta):
    return 5.0 * sqrt(beta) + 8, 5.6 * sqrt(beta) + 10


def run_W():
    print("=" * 78)
    print("W  exact-Wilson witness rows (converged regions)")
    rows = {}
    for beta in (60, 90, 120, 150, 200, 300, 500, 960):
        Ra, Rb = radii(beta)
        rf = coefficients(beta, Rb + 5)
        La, cJa, cDa, heat, na = spectral(beta, Ra, rf, want_heat=True)
        if beta <= 500:
            Lb, cJb, cDb, _, nb = spectral(beta, Rb, rf)
        else:
            Lb, cJb, cDb, nb = La, cJa, cDa, na
        rows[beta] = (Lb, cJb - cDb, abs(La - Lb), nb, heat)
        print(f"  beta={beta:4d}: sector dim {nb:5d}: Lambda {Lb:.12f} (radius change {abs(La - Lb):.1e}), c_J - c_D {cJb - cDb:.10f}, "
              f"beta(c_J - c_D) {beta * (cJb - cDb):.8f}")
    # Hellmann identity by a five-point central difference (truncation O(d^4))
    hell = []
    for beta in (30, 120, 300):
        d = 0.5
        Rb = radii(beta + 2 * d)[1]
        vals = {}
        for bb in (beta - 2 * d, beta - d, beta, beta + d, beta + 2 * d):
            rf = coefficients(bb, Rb + 5)
            vals[bb] = spectral(bb, Rb, rf)
        dL = (8 * (vals[beta + d][0] - vals[beta - d][0]) - (vals[beta + 2 * d][0] - vals[beta - 2 * d][0])) / (12 * d)
        hell.append((beta, vals[beta][1] - vals[beta][2], -beta * dL))
    print("  Hellmann c_J - c_D vs -beta dLambda/dbeta: " + ", ".join(f"beta={b}: {m:.10f} vs {f:.10f}" for b, m, f in hell))
    # fits
    def fit(betas, cols):
        bt = np.array(betas, float)
        A = np.column_stack([bt ** (-k / 2) for k in cols])
        y = np.array([rows[b][0] for b in betas])
        coef = np.linalg.lstsq(A, y, rcond=None)[0]
        return dict(zip(cols, coef))
    note_b = [60, 90, 120, 150, 200]
    all_b = sorted(rows)
    f_note = fit(note_b, [0, 1, 2, 3])
    f_all = fit(all_b, [0, 1, 2, 3])
    f_all5 = fit(all_b, [0, 1, 2, 3, 4])
    f_b0 = fit(all_b, [0, 2, 3, 4])
    bm = [b * rows[b][1] for b in all_b]
    # Richardson on the last two points assuming 1/beta corrections: a_2 ~ (960 bm(960) - 500 bm(500))/(960 - 500)
    rich = (960 * bm[-1] - 500 * bm[-2]) / (960 - 500)
    print(f"  fit on the note's betas: b = {f_note[1]:+.3e}, a_2 = {f_note[2]:.5f}; on all eight: b = {f_all[1]:+.3e}, a_2 = "
          f"{f_all[2]:.5f}; with a beta^-2 term: b = {f_all5[1]:+.3e}, a_2 = {f_all5[2]:.5f}; forced b = 0: a_2 = {f_b0[2]:.5f}; "
          f"beta(c_J - c_D) Richardson (500, 960): {rich:.5f}")
    hell_dev = max(abs(m - f) for _, m, f in hell)
    ok = abs(f_note[1]) < 0.02 and 1.55 < f_note[2] < 1.75 and abs(f_all[1]) < 0.02 and 1.55 < f_all[2] < 1.75 and \
        1.55 < f_b0[2] < 1.75 and hell_dev < 1e-5
    if not ok:
        hit(f"exact-Wilson witness rows differ from the note's falsifier rows (b, a_2) or the Hellmann identity fails "
            f"(dev {hell_dev:.1e})")
    return rows, hell, f_note, f_all, f_all5, f_b0, rich


def run_H(rows):
    print("=" * 78)
    print("H  the heat piece a_2^heat from lattice eigenvectors, L ~ beta (J - I)")
    out = [(b, rows[b][4]) for b in sorted(rows)]
    for beta, heat in out:
        print(f"  beta={beta}: (beta^2/4)(||(J-I)v_1||^2 - ||(J-I)v_0||^2) = {heat:.6f}")
    return out


def main():
    t0 = time.time()
    ok, vals, worst = run_E()
    summary(f"E exact: R H, R Q, R[H e^-Q] = P_1 e^-Q, R(QH e^-Q) = (3uH + Q P_1) e^-Q hold; P_1(1,2) = {vals['P_1(1,2)']}, "
            f"P_2(1,2) = {vals['P_2(1,2)']}, 3uH(1,2) = {vals['3uH(1,2)']}, degrees A1 {vals['A1 degree']} vs A2 "
            f"{vals['A2 2H degree']}; <v|[C,T0]|v> relative {worst:.1e}")
    rows, hell, fn, fa, fa5, fb0, rich = run_W()
    summary(f"W converged exact-Wilson rows to beta = 960: beta(c_J - c_D) = "
            f"{', '.join(f'{b * rows[b][1]:.5f}' for b in sorted(rows))} at beta = {', '.join(str(b) for b in sorted(rows))}; "
            f"Hellmann identity to {max(abs(m - f) for _, m, f in hell):.1e}; fit (note's betas) b = {fn[1]:+.2e}, a_2 = {fn[2]:.4f}; "
            f"(all eight) b = {fa[1]:+.2e}, a_2 = {fa[2]:.4f}; (+beta^-2) b = {fa5[1]:+.2e}, a_2 = {fa5[2]:.4f}; forced b = 0 "
            f"a_2 = {fb0[2]:.4f}; Richardson {rich:.4f}")
    heat = run_H(rows)
    summary("H lattice heat piece (beta^2/4)(||(J-I)v1||^2 - ||(J-I)v0||^2) = " +
            ", ".join(f"{h:.4f} (beta={b})" for b, h in heat) + "; note's reduced a_2^heat ~ 1.0")
    print("=" * 78)
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
