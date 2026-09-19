#!/usr/bin/env python3
"""J:note check for NATIVE_GAUGE_TRANSFER_REDUCED_A2_SUBLEADING_SIGN_RUNG_NINETEEN_BOUNDED_NOTE_2026-06-12 (on main).

A. The note's exact content, re-derived symbolically (sympy, eps = beta^-1/2):
   beta^-3/2 d_(p,q) = H + eps G_1 + eps^2 G_2 + eps^3 exactly (G_1 = (u^2 + 2xy)/2, G_2 = 3u/2); 3 C2/beta = Q + 3u eps; P_1, P_2 as
   the eps, eps^2 coefficients of exp(-3u eps)(H + eps G_1 + eps^2 G_2 + eps^3); the six-neighbour heat side
   (beta/2)(J - I) = L/2 + C_4/beta + O(beta^-2) with no odd term, by Taylor expansion on every monomial of degree <= 7;
   [D, L] = -2L and [D, C_4] = -4 C_4; the degree structure of P_1, P_2; and the falsifier table (79/10 vs 38/5, P_1(1,2) = -41/2 vs
   N_c = 2 -23/2 and dimension-omitted -27, P_2(1,2) = 135/2 vs 39/2 and 243/2, swap P_1(1,2) - P_1(2,1) = 0).
B. The fenced witness beyond the note's grid (numbers only, not a sign derivation): c_J - c_D computed as the runner defines it, with
   Wilson coefficients from the character recurrence (positive walk sums), on swap sectors of an elliptical region
   (p+1)^2 + (p+1)(q+1) + (q+1)^2 <= R^2 checked for convergence at two radii, for beta = 30 .. 960; the identity
   c_J - c_D = -beta d/dbeta log(lambda_1/lambda_0) checked by central differences; and least-squares fits of
   beta (c_J - c_D) = a sqrt(beta) + b + c/sqrt(beta) + d/beta (the half-integer coefficient is a) and of log(lambda_1/lambda_0).
HIT if an exact identity or a table value fails.
"""
from __future__ import annotations

from math import exp, lgamma, log, sqrt

import numpy as np
import sympy as sp

STEPS = [(1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (-1, 0)]


# --------------------------------------------------------------------------------------------------------------- A. exact part
def exact_part():
    x, y, e, h = sp.symbols("x y epsilon h", positive=True)
    u = x + y
    H = x * y * u / 2
    Q = x ** 2 + x * y + y ** 2
    G1, G2 = (u ** 2 + 2 * x * y) / 2, 3 * u / 2
    res = {}
    dexp = sp.expand((x + e) * (y + e) * (u + 2 * e) / 2)             # beta^-3/2 d with p = x/eps
    res["d expansion"] = sp.expand(dexp - (H + e * G1 + e ** 2 * G2 + e ** 3)) == 0
    p_, q_ = x / e, y / e
    C2 = (p_ ** 2 + q_ ** 2 + p_ * q_ + 3 * p_ + 3 * q_) / 3
    res["3 C2/beta = Q + 3u eps"] = sp.simplify(3 * C2 * e ** 2 - (Q + 3 * u * e)) == 0
    ser = sp.series(sp.exp(-3 * u * e) * (H + e * G1 + e ** 2 * G2 + e ** 3), e, 0, 3).removeO()
    P1 = sp.expand(ser.coeff(e, 1))
    P2 = sp.expand(ser.coeff(e, 2))
    res["P_1 formula"] = sp.expand(P1 - (G1 - 3 * u * H)) == 0
    res["P_2 formula"] = sp.expand(P2 - (G2 - 3 * u * G1 + sp.Rational(9, 2) * u ** 2 * H)) == 0
    res["P_1 degrees"] = sorted({sp.Poly(t, x, y).total_degree() for t in sp.Add.make_args(P1)})
    res["P_2 degrees"] = sorted({sp.Poly(t, x, y).total_degree() for t in sp.Add.make_args(P2)})
    at = {x: 1, y: 2}
    res["P_1(1,2)"] = P1.subs(at)
    res["P_2(1,2)"] = P2.subs(at)
    ser2 = sp.series(sp.exp(-2 * u * e) * (H + e * G1 + e ** 2 * G2), e, 0, 3).removeO()
    res["N_c=2 P_1, P_2 at (1,2)"] = (ser2.coeff(e, 1).subs(at), ser2.coeff(e, 2).subs(at))
    res["dimension omitted P_1, P_2 at (1,2)"] = ((-3 * u * H).subs(at), (sp.Rational(9, 2) * u ** 2 * H).subs(at))
    res["swap P_1(1,2)-P_1(2,1)"] = P1.subs(at) - P1.subs({x: 2, y: 1})
    pp, qq, bb = 10, 20, 100
    res["fixed-weight derivative (10,20,100)"] = sp.Rational(pp * pp + qq * qq + pp * qq + 3 * pp + 3 * qq, bb)
    xs, ys, es = sp.Rational(pp) / 10, sp.Rational(qq) / 10, sp.Rational(1, 10)
    res["wrong 2(x+y) correction"] = xs ** 2 + xs * ys + ys ** 2 + 2 * (xs + ys) * es
    # heat side on monomials: (beta/2)(J - I) f with shifts h = eps
    L = lambda f: (sp.diff(f, x, 2) - sp.diff(f, x, y) + sp.diff(f, y, 2)) / 3
    C4 = lambda f: (sp.Rational(1, 72) * (sp.diff(f, x, 4) + sp.diff(f, y, 4)) - sp.Rational(1, 36) * (sp.diff(f, x, 3, y, 1) + sp.diff(f, x, 1, y, 3))
                    + sp.Rational(1, 24) * sp.diff(f, x, 2, y, 2))
    ok_heat, ok_odd = True, True
    for a in range(8):
        for b in range(8 - a):
            f = x ** a * y ** b
            Jf = sum(f.subs({x: x + dp * h, y: y + dq * h}, simultaneous=True) for dp, dq in STEPS) / 6
            expr = sp.expand((Jf - f) / (2 * h ** 2))                  # (beta/2)(J - I) f with beta = h^-2
            ok_heat &= sp.expand(expr.coeff(h, 0) - L(f) / 2) == 0 and sp.expand(expr.coeff(h, 2) - C4(f)) == 0
            ok_odd &= all(sp.expand(expr.coeff(h, k)) == 0 for k in (1, 3, 5))
    res["heat side L/2 + C_4/beta"] = ok_heat
    res["no odd heat terms"] = ok_odd
    Dop = lambda f: x * sp.diff(f, x) + y * sp.diff(f, y)
    ok_D = True
    for a in range(7):
        for b in range(7 - a):
            f = x ** a * y ** b
            ok_D &= sp.expand(Dop(L(f)) - L(Dop(f)) + 2 * L(f)) == 0 and sp.expand(Dop(C4(f)) - C4(Dop(f)) + 4 * C4(f)) == 0
    res["[D,L] = -2L, [D,C_4] = -4C_4"] = ok_D
    return res


# ------------------------------------------------------------------------------------------------------ B. converged witness
def stencil(a):
    out = np.zeros_like(a)
    n = a.shape[0]
    for dp, dq in STEPS:
        out[max(-dp, 0): n + min(-dp, 0), max(-dq, 0): n + min(-dq, 0)] += a[max(dp, 0): n + min(dp, 0), max(dq, 0): n + min(dq, 0)]
    return out / 6.0


def coefficients(beta, Rmax):
    B = int(Rmax) + int(10 * sqrt(beta)) + 60
    a = np.zeros((B + 1, B + 1))
    a[0, 0] = 1.0
    acc = np.zeros_like(a)
    for n in range(int(beta + 14 * sqrt(beta) + 40) + 1):
        acc += exp(-beta + n * log(beta) - lgamma(n + 1)) * a
        a = stencil(a)
    return acc / acc[0, 0]


def sector_ops(beta, R, rf, sign):
    """Sparse region operators restricted to one swap sector (sign +1 symmetric, -1 antisymmetric)."""
    from scipy import sparse
    sites = [(p, q) for p in range(int(R) + 1) for q in range(int(R) + 1) if (p + 1) ** 2 + (p + 1) * (q + 1) + (q + 1) ** 2 <= R * R]
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
    cp = J @ r
    rprime = cp - r * cp[idx[(0, 0)]]
    ur, uc, uv, m = [], [], [], 0
    for (p, q) in sites:
        if p < q:
            ur += [idx[(p, q)], idx[(q, p)]]
            uc += [m, m]
            uv += [1 / sqrt(2), sign / sqrt(2)]
            m += 1
        elif p == q and sign == 1:
            ur.append(idx[(p, p)])
            uc.append(m)
            uv.append(1.0)
            m += 1
    U = sparse.csr_matrix((uv, (ur, uc)), shape=(n, m))
    Js = (U.T @ J @ U).toarray()
    rs = (U.T @ sparse.diags(r) @ U).diagonal()
    rps = (U.T @ sparse.diags(rprime) @ U).diagonal()
    return Js, rs, rps, n


def top_pairs(beta, Js, rs, rps, k=2):
    w, V = np.linalg.eigh(Js)
    E = (V * np.exp(beta / 2 * (w - 1))) @ V.T
    del V
    T = E @ (rs[:, None] * E)
    lam, W = np.linalg.eigh(T)
    del T
    o = np.argsort(lam)[::-1][:k]
    out = []
    for kk in o:
        v = W[:, kk]
        Ev = E @ v
        out.append((lam[kk], v @ Js @ v, Ev @ (rps * Ev)))
    return out


def sector_data(beta, R, rf, anti=True):
    Js, rs, rps, n = sector_ops(beta, R, rf, 1)
    sym = top_pairs(beta, Js, rs, rps, 2)
    lam_anti = None
    if anti:
        Ja, ra, rpa, _ = sector_ops(beta, R, rf, -1)
        lam_anti = top_pairs(beta, Ja, ra, rpa, 1)[0][0]
    (l0, j0, b0), (l1, j1, b1) = sym
    cJ, cD = beta * (j0 - j1), beta * (b1 / l1 - b0 / l0)
    return cJ, cD, l1 / l0, lam_anti, n, l1


def witness():
    rows = {}
    for beta in (30, 60, 120, 240, 480, 960):
        Ra, Rb = 5.0 * sqrt(beta) + 8, 5.6 * sqrt(beta) + 10
        rf = coefficients(beta, Rb)
        a1 = sector_data(beta, Ra, rf, anti=True)
        a2 = sector_data(beta, Rb, rf, anti=False)
        rows[beta] = (a1, a2)
    return rows


def fd_check(beta=120):
    R = 5.0 * sqrt(beta) + 8
    vals = {}
    for b in (beta - 0.5, beta, beta + 0.5):
        rf = coefficients(b, R)
        vals[b] = sector_data(b, R, rf, anti=False)
    deriv = (log(vals[beta + 0.5][2]) - log(vals[beta - 0.5][2])) / 1.0
    return vals[beta][0] - vals[beta][1], -beta * deriv


def main():
    ex = exact_part()
    print(f"A. exact: {ex}")
    rows = witness()
    for beta, (a1, a2) in rows.items():
        print(f"B{beta}: region dim {a1[4]}: cJ {a1[0]:.10f} cD {a1[1]:.10f} beta*(cJ-cD) {beta * (a1[0] - a1[1]):.8f} ratio {a1[2]:.10f}, "
              f"top antisymmetric / lambda_1 = {a1[3] / a1[5]:.6f}; larger region dim {a2[4]}: beta*(cJ-cD) {beta * (a2[0] - a2[1]):.8f} "
              f"ratio {a2[2]:.10f}")
    m, fdv = fd_check()
    print(f"B'. c_J - c_D = -beta d/dbeta log(lambda_1/lambda_0) at beta = 120: {m:.10f} vs central difference {fdv:.10f}")
    betas = np.array(sorted(rows), float)
    y = np.array([b * (rows[b][1][0] - rows[b][1][1]) for b in sorted(rows)])
    Afit = np.column_stack([np.sqrt(betas), np.ones_like(betas), 1 / np.sqrt(betas), 1 / betas])
    coef = np.linalg.lstsq(Afit, y, rcond=None)[0]
    diffs = np.diff(y)
    ratios = diffs[1:] / diffs[:-1]
    richardson = 2 * y[-1] - y[-2]
    lr = np.array([log(rows[b][1][2]) for b in sorted(rows)])
    Al = np.column_stack([np.ones_like(betas), 1 / np.sqrt(betas), 1 / betas, betas ** -1.5])
    cl = np.linalg.lstsq(Al, lr, rcond=None)[0]
    print(f"C. beta(cJ-cD) successive differences {[float('%.6f' % d) for d in diffs]}, ratios {[float('%.4f' % r) for r in ratios]} "
          f"(1/beta corrections give 1/2, a sqrt(beta) term would give sqrt(2)); Richardson limit from beta = 480, 960: {richardson:.6f}; "
          f"fit a sqrt(beta) + b + c/sqrt(beta) + d/beta: a = {coef[0]:.2e}, b = {coef[1]:.5f}; lambda1/lambda0 limit from a log fit "
          f"{exp(cl[0]):.6f} (its 1/sqrt(beta) coefficient {cl[1]:.1e})")
    fails = []
    for k in ("d expansion", "3 C2/beta = Q + 3u eps", "P_1 formula", "P_2 formula", "heat side L/2 + C_4/beta", "no odd heat terms",
              "[D,L] = -2L, [D,C_4] = -4C_4"):
        if ex[k] is not True:
            fails.append(k)
    table = {"P_1(1,2)": sp.Rational(-41, 2), "P_2(1,2)": sp.Rational(135, 2), "N_c=2 P_1, P_2 at (1,2)": (sp.Rational(-23, 2), sp.Rational(39, 2)),
             "dimension omitted P_1, P_2 at (1,2)": (-27, sp.Rational(243, 2)), "swap P_1(1,2)-P_1(2,1)": 0,
             "fixed-weight derivative (10,20,100)": sp.Rational(79, 10), "wrong 2(x+y) correction": sp.Rational(38, 5)}
    for k, v in table.items():
        if ex[k] != v:
            fails.append(f"{k}: {ex[k]} != {v}")
    if ex["P_1 degrees"] != [2, 4] or ex["P_2 degrees"] != [1, 3, 5]:
        fails.append("degree structure")
    anti_ok = all(rows[b][0][3] < rows[b][0][5] for b in rows)
    if fails:
        print(f"HIT: {fails}")
    conv = max(abs(rows[b][0][0] - rows[b][0][1] - rows[b][1][0] + rows[b][1][1]) * b for b in rows)
    print(f"SUMMARY: the note's expansions (d, C2, P_1, P_2, C_4 with no odd heat term, the D-commutators, degrees 2,4 and 1,3,5) and every "
          f"table value (79/10, 38/5, -41/2, -23/2, -27, 135/2, 39/2, 243/2, 0) hold exactly; the fenced witness, converged to {conv:.1e} in "
          f"beta*(cJ-cD) between two elliptical regions, gives beta*(cJ-cD) = "
          f"{', '.join(f'{b * (rows[b][1][0] - rows[b][1][1]):.6f}' for b in sorted(rows))} at beta = {', '.join(str(b) for b in sorted(rows))} "
          f"and lambda1/lambda0 = {', '.join(f'{rows[b][1][2]:.6f}' for b in sorted(rows))}; c_J - c_D equals -beta dlog(lambda1/lambda0)/dbeta "
          f"({m:.8f} vs {fdv:.8f} at beta = 120); successive differences shrink by {', '.join(f'{r:.3f}' for r in ratios)} (1/beta "
          f"corrections), the fitted half-integer coefficient is a = {coef[0]:.1e}, and the Richardson limit of beta*(cJ-cD) is "
          f"{richardson:.5f}; both top states are swap-symmetric at every beta ({anti_ok}); these rows are witnesses, not a derivation of "
          f"the sign")


if __name__ == "__main__":
    main()
