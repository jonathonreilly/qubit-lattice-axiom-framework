#!/usr/bin/env python3
"""Probe: NATIVE_GAUGE_TRANSFER_REDUCED_A2_SPECTRAL_DOMINATION_RUNG_ELEVEN_BOUNDED_NOTE_2026-06-12.

Machinery disjoint from the runner (Bessel-determinant Wilson coefficients with
a truncated mode sum, dense eigh on the box [0, shell]^2): the Wilson
coefficients come from the note's own character recurrence c' = (1/6) sum_nb c,
integrated exactly as Poisson-weighted six-neighbour walk sums
c(beta) = e^{beta J} delta_(0,0) on a box far larger than the operator region.

 T  the table: T_beta = E diag(r) E, E = exp((beta/2) J_region), on the note's
    own regions (box [0, shell]^2, shell = 16, 21, 28, 37, 45 at beta = 15, 30,
    60, 120, 180): c_J = -beta Delta_J, c_D = beta Delta_D reproduced against
    the printed six-digit rows.
 C  converged rows: the same quantities on elliptical regions
    (p+1)^2 + (p+1)(q+1) + (q+1)^2 <= R^2 in the swap-symmetric sector (both top
    states are swap-symmetric), at two radii R = 5 sqrt(beta) + 8 and
    5.6 sqrt(beta) + 10, for beta = 15, 30, 60, 120, 180 and beyond (240, 480):
    positivity of the margin, monotone shrinking, c_D/c_J rising, and
    beta (c_J - c_D) staying O(1), checked on the converged numbers.
 F  the two falsifiers of the note: (a) J normalization: replacing the /6
    average by /3 or /12 in the operator and in Delta_J changes the
    comparison; (b) the exact character-recurrence r' against a central
    difference of r(beta) (walk sums at beta +- 1/4); two wrong r' forms:
    omitting the -r c'_(0,0)/c_(0,0) term (exactly invisible: r' -> r' + alpha r
    shifts b_i/lambda_i by alpha for both states, so Delta_D is unchanged), and
    keeping only the three fundamental-weight neighbours in c' (visible).

Prints SUMMARY: lines; HIT: only when a stated fact of the note fails.
"""
import sys
import time
from math import exp, lgamma, log, sqrt

import numpy as np
from scipy import sparse

STEPS = [(1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (-1, 0)]
HITS = []


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


def stencil(a):
    out = np.zeros_like(a)
    n = a.shape[0]
    for dp, dq in STEPS:
        out[max(-dp, 0): n + min(-dp, 0), max(-dq, 0): n + min(-dq, 0)] += a[max(dp, 0): n + min(dp, 0), max(dq, 0): n + min(dq, 0)]
    return out / 6.0


def coefficients(beta, reach):
    """r_(p,q)(beta) = c_(p,q)/c_(0,0) with c = e^{beta J} delta_00, as Poisson-weighted walk sums."""
    B = int(reach) + int(10 * sqrt(beta)) + 60
    a = np.zeros((B + 1, B + 1))
    a[0, 0] = 1.0
    acc = np.zeros_like(a)
    for n in range(int(beta + 14 * sqrt(beta) + 40) + 1):
        acc += exp(-beta + n * log(beta) - lgamma(n + 1)) * a
        a = stencil(a)
    return acc / acc[0, 0]


def region_ops(sites, rf, kappa=1.0 / 6.0, rprime_mode="exact"):
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    rows, cols = [], []
    for (p, q), i in idx.items():
        for dp, dq in STEPS:
            k = (p + dp, q + dq)
            if k in idx:
                rows.append(idx[k])
                cols.append(i)
    J = sparse.csr_matrix((np.full(len(rows), kappa), (rows, cols)), shape=(n, n))
    r = np.array([rf[p, q] for (p, q) in sites])
    # exact diagonal derivative: r' = c'/c00 - r c'_00/c00 with c' = (1/6) sum over neighbours (full lattice)
    Bn = rf.shape[0]
    if rprime_mode == "fund":          # wrong: only the three fundamental-weight steps in c'
        cp = np.array([sum(rf[p + dp, q + dq] for dp, dq in STEPS[:3] if 0 <= p + dp < Bn and 0 <= q + dq < Bn) / 6.0
                       for (p, q) in sites])
    elif rprime_mode == "region":      # the runner's form: neighbours restricted to the operator region
        cp = np.array([sum(rf[p + dp, q + dq] for dp, dq in STEPS if (p + dp, q + dq) in idx) / 6.0 for (p, q) in sites])
    else:                              # the exact character recurrence on the full lattice
        cp = np.array([sum(rf[p + dp, q + dq] for dp, dq in STEPS if 0 <= p + dp < Bn and 0 <= q + dq < Bn) / 6.0
                       for (p, q) in sites])
    cp00 = sum(rf[dp, dq] for dp, dq in (STEPS[:3] if rprime_mode == "fund" else STEPS) if dp >= 0 and dq >= 0) / 6.0
    rprime = cp if rprime_mode == "wrong" else cp - r * cp00
    return J, r, rprime, idx


def top2(beta, J, r, rprime):
    Jd = J.toarray()
    w, V = np.linalg.eigh(Jd)
    E = (V * np.exp(beta / 2 * (w - w.max()))) @ V.T       # scalar rescaling leaves c_J, c_D unchanged
    T = E @ (r[:, None] * E)
    lam, W = np.linalg.eigh(T)
    o = np.argsort(lam)[::-1][:2]
    out = []
    for kk in o:
        v = W[:, kk]
        Ev = E @ v
        out.append((lam[kk], v @ (Jd @ v), Ev @ (rprime * Ev), v))
    (l0, j0, b0, v0), (l1, j1, b1, v1) = out
    return l0, l1, j1 - j0, b1 / l1 - b0 / l0, v0, v1


def box_sites(shell):
    return [(p, q) for p in range(shell + 1) for q in range(shell + 1)]


def ellipse_sites(R):
    return [(p, q) for p in range(int(R) + 1) for q in range(int(R) + 1)
            if (p + 1) ** 2 + (p + 1) * (q + 1) + (q + 1) ** 2 <= R * R]


def sym_sector(sites, J, r, rprime):
    """restrict to the swap-symmetric sector (orthonormal symmetric combinations)"""
    idx = {s: i for i, s in enumerate(sites)}
    cols, rows, vals, m = [], [], [], 0
    for (p, q) in sites:
        if p < q and (q, p) in idx:
            rows += [idx[(p, q)], idx[(q, p)]]
            cols += [m, m]
            vals += [1 / sqrt(2), 1 / sqrt(2)]
            m += 1
        elif p == q:
            rows.append(idx[(p, p)])
            cols.append(m)
            vals.append(1.0)
            m += 1
    U = sparse.csr_matrix((vals, (rows, cols)), shape=(len(sites), m))
    Js = sparse.csr_matrix(U.T @ J @ U)
    rs = (U.T @ sparse.diags(r) @ U).diagonal()
    rps = (U.T @ sparse.diags(rprime) @ U).diagonal()
    return Js, rs, rps


TABLE = {15: (16, 0.811415, 0.702465, 0.108950, 0.86573, 0.21634),
         30: (21, 0.834363, 0.779367, 0.054996, 0.93409, 0.20481),
         60: (28, 0.847469, 0.819819, 0.027651, 0.96737, 0.19925),
         120: (37, 0.854701, 0.840331, 0.014369, 0.98319, 0.19650),
         180: (45, 0.857260, 0.847168, 0.010093, 0.98823, 0.19559)}


def run_table():
    print("=" * 78)
    print("T  the note's rows on its own box regions")
    worst = 0.0
    rows = {}
    for beta, (shell, cJt, cDt, mt, ratt, lrt) in TABLE.items():
        rf = coefficients(beta, 6 * sqrt(beta) + 60)
        sites = box_sites(shell)
        J, r, rp, idx = region_ops(sites, rf, rprime_mode="region")
        l0, l1, dj, dd, v0, v1 = top2(beta, J, r, rp)
        cJ, cD = -beta * dj, beta * dd
        Jx, rx, rpx, _ = region_ops(sites, rf, rprime_mode="exact")
        cDx = beta * top2(beta, Jx, rx, rpx)[3]
        print(f"    (same box with the full-lattice exact r': c_D {cDx:.6f}, margin {cJ - cDx:.6f})")
        dev = max(abs(cJ - cJt), abs(cD - cDt), abs(cJ - cD - mt), abs(cD / cJ - ratt) / 10, abs(l1 / l0 - lrt) / 10)
        worst = max(worst, dev)
        rows[beta] = (shell, cJ, cD, l1 / l0)
        print(f"  beta={beta:3d} box [0,{shell}]^2: c_J {cJ:.6f} (note {cJt}), c_D {cD:.6f} (note {cDt}), margin {cJ - cD:.6f} "
              f"(note {mt}), c_D/c_J {cD / cJ:.5f}, l1/l0 {l1 / l0:.5f}")
    print(f"  max deviation from the printed rows (six-digit entries; ratios scaled by 1/10): {worst:.1e}")
    if worst > 2e-6:
        hit(f"the note's table rows do not reproduce on their own box regions (max dev {worst:.1e})")
    return rows, worst


def run_converged(betas=(15, 30, 60, 120, 180, 240, 480)):
    print("=" * 78)
    print("C  converged rows (elliptical regions, symmetric sector, two radii)")
    rows = {}
    for beta in betas:
        Ra, Rb = 5.0 * sqrt(beta) + 8, 5.6 * sqrt(beta) + 10
        rf = coefficients(beta, Rb + 5)
        vals = []
        for R in (Ra, Rb):
            sites = ellipse_sites(R)
            J, r, rp, idx = region_ops(sites, rf)
            Js, rs, rps = sym_sector(sites, J, r, rp)
            l0, l1, dj, dd, v0, v1 = top2(beta, Js, rs, rps)
            vals.append((-beta * dj, beta * dd, l1 / l0, len(sites)))
        rows[beta] = vals
        (cJa, cDa, lra, na), (cJb, cDb, lrb, nb) = vals
        print(f"  beta={beta:3d}: R={Ra:.1f} ({na} sites): c_J {cJa:.8f} c_D {cDa:.8f} margin {cJa - cDa:.8f}; R={Rb:.1f} "
              f"({nb}): margin {cJb - cDb:.8f}; beta*margin {beta * (cJb - cDb):.6f}; c_D/c_J {cDb / cJb:.6f}; l1/l0 {lrb:.6f}")
    return rows


def run_falsifiers(beta=30):
    print("=" * 78)
    print("F  the note's falsifiers at beta = 30 (converged region)")
    R = 5.6 * sqrt(beta) + 10
    rf = coefficients(beta, R + 5)
    sites = ellipse_sites(R)
    res = {}
    for label, kappa in (("/6 (note)", 1 / 6), ("/3", 1 / 3), ("/12", 1 / 12)):
        J, r, rp, idx = region_ops(sites, rf, kappa=kappa)
        Js, rs, rps = sym_sector(sites, J, r, rp)
        l0, l1, dj, dd, v0, v1 = top2(beta, Js, rs, rps)
        res[label] = (-beta * dj, beta * dd)
    J, r, rp_wrong, idx = region_ops(sites, rf, rprime_mode="wrong")
    Js, rs, rps = sym_sector(sites, J, r, rp_wrong)
    l0, l1, dj, dd, v0, v1 = top2(beta, Js, rs, rps)
    res["wrong r'"] = (-beta * dj, beta * dd)
    J, r, rp_f, idx = region_ops(sites, rf, rprime_mode="fund")
    Js, rs, rps = sym_sector(sites, J, r, rp_f)
    l0, l1, dj, dd, v0, v1 = top2(beta, Js, rs, rps)
    res["fund-only r'"] = (-beta * dj, beta * dd)
    # exact r' against a central difference of r(beta)
    d = 0.25
    rp_minus = coefficients(beta - d, R + 5)
    rp_plus = coefficients(beta + d, R + 5)
    J, r, rp_exact, idx = region_ops(sites, rf)
    fd = np.array([(rp_plus[p, q] - rp_minus[p, q]) / (2 * d) for (p, q) in sites])
    scale = np.max(np.abs(rp_exact))
    fd_dev = float(np.max(np.abs(fd - rp_exact)) / scale)
    for k, (a, b) in res.items():
        print(f"  variant {k:>13s}: c_J {a:.6f}, c_D {b:.6f}, c_J - c_D {a - b:+.6f}")
    print(f"  exact recurrence r' vs central difference of r(beta) (h = 1/4): max rel dev {fd_dev:.2e} (O(h^2) difference error)")
    ok_changes = (res["/3"][0] - res["/3"][1]) * (res["/12"][0] - res["/12"][1]) < 0 or \
        abs((res["/3"][0] - res["/3"][1]) - (res["/6 (note)"][0] - res["/6 (note)"][1])) > 0.01
    ok_wrong = abs(res["fund-only r'"][1] - res["/6 (note)"][1]) > 0.01
    print(f"  wrong r' without -r c'00/c00: c_D change {abs(res[chr(119) + 'rong r' + chr(39)][1] - res['/6 (note)'][1]):.1e} "
          f"(exactly invariant: adding alpha r to r' shifts both b_i/lambda_i by alpha); fundamental-neighbours-only c': "
          f"c_D {res['fund-only r' + chr(39)][1]:.6f} (visible: {ok_wrong})")
    if fd_dev > 1e-3:
        hit(f"the exact character-recurrence r' disagrees with the beta-derivative of r (rel dev {fd_dev:.2e})")
    return res, fd_dev, ok_changes, ok_wrong


def main():
    t0 = time.time()
    trows, worst = run_table()
    summary(f"T box rows reproduced from walk-sum coefficients: max deviation from the printed six-digit rows {worst:.1e}; box "
            f"beta*(c_J - c_D) = {', '.join(f'{b * (trows[b][1] - trows[b][2]):.4f}' for b in sorted(trows))} at beta = "
            f"{', '.join(str(b) for b in sorted(trows))}")
    crows = run_converged()
    betas = sorted(crows)
    marg = [crows[b][1][0] - crows[b][1][1] for b in betas]
    rat = [crows[b][1][1] / crows[b][1][0] for b in betas]
    bm = [b * m for b, m in zip(betas, marg)]
    conv = max(b * abs((crows[b][0][0] - crows[b][0][1]) - (crows[b][1][0] - crows[b][1][1])) for b in betas)
    pos = all(m > 0 for m in marg)
    shrink = all(marg[i + 1] < marg[i] for i in range(len(marg) - 1))
    rises = all(rat[i + 1] > rat[i] for i in range(len(rat) - 1))
    flat = max(bm) / min(bm) < 1.6
    print(f"  converged: margins positive {pos}, shrinking {shrink}, c_D/c_J rising {rises}, beta*margin max/min {max(bm) / min(bm):.4f}; "
          f"radius convergence of beta*margin {conv:.1e}")
    if not (pos and shrink and rises and flat):
        hit(f"a trend claim fails on converged rows: positive {pos}, shrinking {shrink}, rising {rises}, O(1) {flat}")
    summary(f"C converged (two radii agree to {conv:.1e} in beta*margin): c_J - c_D = "
            f"{', '.join(f'{m:.6f}' for m in marg)} at beta = {', '.join(str(b) for b in betas)}; beta*(c_J - c_D) = "
            f"{', '.join(f'{x:.4f}' for x in bm)}; c_D/c_J = {', '.join(f'{x:.5f}' for x in rat)}; box vs converged beta*margin at "
            f"beta = 120, 180: {120 * (trows[120][1] - trows[120][2]):.4f} vs {bm[betas.index(120)]:.4f}, "
            f"{180 * (trows[180][1] - trows[180][2]):.4f} vs {bm[betas.index(180)]:.4f}")
    res, fd_dev, ok_changes, ok_wrong = run_falsifiers()
    summary(f"F falsifiers at beta = 30: J normalization /6 -> c_J - c_D {res['/6 (note)'][0] - res['/6 (note)'][1]:+.6f}, /3 -> "
            f"{res['/3'][0] - res['/3'][1]:+.6f}, /12 -> {res['/12'][0] - res['/12'][1]:+.6f} (comparison changes: {ok_changes}); "
            f"wrong r' without the -r c'00/c00 term gives c_D {res[chr(119) + 'rong r' + chr(39)][1]:.6f} = the exact "
            f"{res['/6 (note)'][1]:.6f} (that term is exactly invisible in Delta_D, so this wrong form does not change c_D), "
            f"while a fundamental-neighbours-only c' gives c_D {res['fund-only r' + chr(39)][1]:.6f} (visible: {ok_wrong}); "
            f"exact r' vs d r/d beta rel dev {fd_dev:.1e}")
    print("=" * 78)
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
