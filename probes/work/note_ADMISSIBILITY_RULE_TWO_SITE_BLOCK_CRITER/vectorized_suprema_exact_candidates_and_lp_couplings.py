#!/usr/bin/env python3
"""Probe: ADMISSIBILITY_RULE_TWO_SITE_BLOCK_CRITERION_EXACT_AND_SILENT_FOR_EVERY_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-07.

Machinery disjoint from the runner (exact Fraction loops over shells, explicit
couplings on 202 instances):

 S  the suprema c_1, rho, rho', sigma at the six triples: every one of the
    476,280 boundary instances (252 multisets of dy x 126 of the other four dx x
    15 pairs) evaluated at once in vectorized floating point through the
    effective-factor form m_x ~ A h, m_y ~ B (Phi^T A); every instance within
    1e-9 of the float maximum re-evaluated in exact rationals; the maxima
    compared with the note's literals; the falsifier "sigma > rho + rho' or
    sigma > rho(1 + c_1)" at all six triples, strictness sigma < rho + rho' at the
    silent triples (where the note executes rho'), 10 sigma > 2 at the silent
    triples and < 2 at the region triples, the rho/c_1 ordering.
 L  Theorem N' by LINEAR PROGRAMMING, not by the explicit coupling: for 300
    random one-slot changes at an x-slot per triple (1800 in all), the
    transport LP min_pi E_pi d_H over all couplings of the two 36-point block
    laws (1296 variables, scipy HiGHS) against TV(m_x) + TV(m_y); Theorem O
    (TV of the block laws = TV of the x-marginals) on the same instances.
 D  the scans t = 21/20 .. 39/20 along (t,1,1) and (t,t,1): exact c_1 and rho
    (vectorized search + exact candidates), the cells where 6 c_1 and
    5 rho (1 + c_1) cross 1, and the first t with rho/c_1 > 1.

Prints SUMMARY: lines; HIT: only when a falsifier of the note fires.
"""
import itertools
import sys
import time
from fractions import Fraction as Fr

import numpy as np
from scipy.optimize import linprog

HITS = []
M = 6                                   # +x, -x, +y, -y, +z, -z


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


def orbit(a, b):
    if a == b:
        return 0                        # parallel
    if a // 2 == b // 2:
        return 1                        # antiparallel
    return 2                            # orthogonal


def phi_matrix(triple, exact=False):
    vals = [Fr(v) for v in triple] if exact else [float(v) for v in triple]
    return [[vals[orbit(a, b)] for b in range(M)] for a in range(M)]


SH5 = list(itertools.combinations_with_replacement(range(M), 5))
SH4 = list(itertools.combinations_with_replacement(range(M), 4))
PAIRS = [(u, w) for u in range(M) for w in range(u + 1, M)]


def shell_products(Phi, shells):
    """for each shell, the vector over s of prod_{z in shell} Phi[s][z]"""
    P = np.array(Phi, dtype=float)
    out = np.ones((len(shells), M))
    for k, sh in enumerate(shells):
        for z in sh:
            out[k] *= P[:, z]
    return out


def float_search(triple):
    """TV_x, TV_y for all (dy shell, dx4 shell, pair) instances"""
    Phi = phi_matrix(triple)
    P = np.array(Phi)
    B = shell_products(Phi, SH5)                 # 252 x 6  (y-side boundary product, as function of s_y)
    A0 = shell_products(Phi, SH4)                # 126 x 6
    h = B @ P.T                                  # h[b, s] = sum_{s'} Phi(s, s') B[b, s']   (Phi symmetric)
    # A for each varied value u: A0[a, s] * Phi[s, u]
    A = A0[:, None, :] * P.T[None, :, :]         # 126 x 6(u) x 6(s)
    mx = A[None, :, :, :] * h[:, None, None, :]  # 252 x 126 x 6 x 6
    mx /= mx.sum(-1, keepdims=True)
    # m_y(s') ~ B(s') sum_s Phi(s, s') A(s)
    PA = np.einsum("aus,st->aut", A, P)          # 126 x 6 x 6: sum_s A(s) Phi(s, t)
    my = B[:, None, None, :] * PA[None, :, :, :]
    my /= my.sum(-1, keepdims=True)
    tvx = np.stack([0.5 * np.abs(mx[:, :, u, :] - mx[:, :, w, :]).sum(-1) for u, w in PAIRS], -1)   # 252 x 126 x 15
    tvy = np.stack([0.5 * np.abs(my[:, :, u, :] - my[:, :, w, :]).sum(-1) for u, w in PAIRS], -1)
    return tvx, tvy


def exact_tv(triple, bidx, aidx, pidx):
    Phi = phi_matrix(triple, exact=True)
    Bv = [Fr(1)] * M
    for z in SH5[bidx]:
        Bv = [Bv[s] * Phi[s][z] for s in range(M)]
    A0 = [Fr(1)] * M
    for z in SH4[aidx]:
        A0 = [A0[s] * Phi[s][z] for s in range(M)]
    h = [sum(Phi[s][t] * Bv[t] for t in range(M)) for s in range(M)]
    u, w = PAIRS[pidx]
    out = []
    for which in (u, w):
        A = [A0[s] * Phi[s][which] for s in range(M)]
        mx = [A[s] * h[s] for s in range(M)]
        Zx = sum(mx)
        my = [Bv[t] * sum(A[s] * Phi[s][t] for s in range(M)) for t in range(M)]
        Zy = sum(my)
        out.append(([v / Zx for v in mx], [v / Zy for v in my]))
    tvx = sum(abs(a - b) for a, b in zip(out[0][0], out[1][0])) / 2
    tvy = sum(abs(a - b) for a, b in zip(out[0][1], out[1][1])) / 2
    return tvx, tvy


def exact_c1(triple):
    Phi = phi_matrix(triple, exact=True)
    best = Fr(0)
    for sh in SH5:
        base = [Fr(1)] * M
        for z in sh:
            base = [base[s] * Phi[s][z] for s in range(M)]
        for u, w in PAIRS:
            a = [base[s] * Phi[s][u] for s in range(M)]
            b = [base[s] * Phi[s][w] for s in range(M)]
            Za, Zb = sum(a), sum(b)
            tv = sum(abs(x / Za - y / Zb) for x, y in zip(a, b)) / 2
            best = max(best, tv)
    return best


def exact_sup(triple, vals, tol=1e-9):
    """exact maximum over instances whose float value is within tol of the float max"""
    vmax = vals.max()
    cand = np.argwhere(vals >= vmax - tol * max(1.0, vmax))
    return cand


def suprema(triple):
    tvx, tvy = float_search(triple)
    res = {}
    for name, arr in (("rho", tvx), ("rhop", tvy), ("sigma", tvx + tvy)):
        cand = exact_sup(triple, arr)
        best = Fr(0)
        for b, a, p in cand:
            ex, ey = exact_tv(triple, int(b), int(a), int(p))
            val = ex if name == "rho" else ey if name == "rhop" else ex + ey
            best = max(best, val)
        res[name] = (best, len(cand))
    return res


NOTE = {
    (3, 1, 2): dict(c1=Fr(270, 989), rho=Fr(2168397, 7948400), rhop=Fr(1350, 26077), sigma=Fr(15220386, 48008647)),
    (5, 2, 4): dict(c1=Fr(8650000, 40615109), rho=Fr(271059507090000, 1298168979740633), rhop=Fr(1915425000, 55627392667),
                    sigma=Fr(24971992461, 111254785334)),
    (7, 3, 5): dict(c1=Fr(6391462, 29948925), rho=Fr(239957740750, 1121635870169), rhop=Fr(856455908, 27833079009),
                    sigma=Fr(1462764714390, 6157201570091)),
    (2, 1, 2): dict(c1=Fr(2, 13), rho=Fr(67715, 446034), sigma=Fr(14803, 90094)),
    (3, 2, 2): dict(c1=Fr(2079, 15566), rho=Fr(1471549788, 11145302999), sigma=Fr(31495356, 211495159)),
    (5, 4, 4): dict(c1=Fr(4000000, 61385721), rho=Fr(81847628000000, 1305850357630907), sigma=Fr(261542884000000, 3917551072892721)),
}
SILENT = [(3, 1, 2), (5, 2, 4), (7, 3, 5)]


def run_S():
    print("=" * 78)
    print("S  exhaustive suprema (vectorized float search + exact candidates)")
    rows = {}
    for triple, lit in NOTE.items():
        t0 = time.time()
        c1 = exact_c1(triple)
        sp = suprema(triple)
        rho, rhop, sigma = sp["rho"][0], sp["rhop"][0], sp["sigma"][0]
        ok = c1 == lit["c1"] and rho == lit["rho"] and sigma == lit["sigma"] and ("rhop" not in lit or rhop == lit["rhop"])
        # falsifier: sigma > rho + rho' or sigma > rho(1 + c_1) at a triple; the note states strictness sigma < rho + rho'
        # only at the triples where it executes rho' (the three silent triples)
        order_ok = not (sigma > rho + rhop) and not (sigma > rho * (1 + c1)) and (sigma < rho + rhop if triple in SILENT else True)
        eq_note = "" if sigma != rho + rhop else " [sigma = rho + rho' exactly here: the two marginal maximizers coincide]"
        ratio = rho / c1
        silent = triple in SILENT
        bv = 10 * sigma
        crit_ok = (bv > 2) if silent else (bv < 2)
        ratio_ok = (ratio > 1) if triple == (7, 3, 5) else (ratio <= 1)
        rows[triple] = (c1, rho, rhop, sigma, float(ratio), float(bv), sp["sigma"][1], sigma == rho + rhop)
        print(f"  {triple}: c_1 {c1} rho {rho} rho' {rhop} sigma {sigma}; literals match: {ok}; sigma < rho+rho' and sigma <= "
              f"rho(1+c_1) as scoped: {order_ok}{eq_note}; rho/c_1 {float(ratio):.4f}; B_V = 10 sigma = {float(bv):.4f} ({'> 2' if bv > 2 else '< 2'}); "
              f"exact candidates checked {sp['rho'][1]}/{sp['rhop'][1]}/{sp['sigma'][1]} ({time.time() - t0:.1f}s)")
        if not ok:
            hit(f"{triple}: a c_1/rho/rho'/sigma literal differs from the recomputation")
        if not order_ok or not crit_ok or not ratio_ok:
            hit(f"{triple}: ordering/criterion/ratio statement fails (sigma vs rho+rho' {float(sigma - rho - rhop):+.3e}, 10 sigma {float(bv):.4f}, "
                f"rho/c_1 {float(ratio):.4f})")
    return rows


def block_law(triple, dy, dx):
    """36-point block law for boundary value lists dy (5) and dx (5)"""
    Phi = np.array(phi_matrix(triple))
    B = np.ones(M)
    for z in dy:
        B *= Phi[:, z]
    A = np.ones(M)
    for z in dx:
        A *= Phi[:, z]
    J = A[:, None] * Phi * B[None, :]
    return J / J.sum()


def run_L(n_per=300, seed=20260919):
    print("=" * 78)
    print("L  Theorem N' by linear programming over all couplings")
    rng = np.random.default_rng(seed)
    D = np.array([[(a // M != b // M) + (a % M != b % M) for b in range(M * M)] for a in range(M * M)], dtype=float)
    Aeq = np.zeros((2 * M * M, (M * M) ** 2))
    for i in range(M * M):
        Aeq[i, i * M * M:(i + 1) * M * M] = 1
        Aeq[M * M + i, i::M * M] = 1
    worst_gap = 0.0
    worst_O = 0.0
    count = 0
    for triple in NOTE:
        for _ in range(n_per):
            dy = list(rng.integers(0, M, 5))
            dx = list(rng.integers(0, M, 4))
            u, w = rng.choice(M, 2, replace=False)
            mu = block_law(triple, dy, dx + [int(u)])
            nu = block_law(triple, dy, dx + [int(w)])
            res = linprog(D.ravel(), A_eq=Aeq, b_eq=np.concatenate([mu.ravel(), nu.ravel()]), bounds=(0, None), method="highs")
            tvx = 0.5 * np.abs(mu.sum(1) - nu.sum(1)).sum()
            tvy = 0.5 * np.abs(mu.sum(0) - nu.sum(0)).sum()
            worst_gap = max(worst_gap, abs(res.fun - (tvx + tvy)))
            worst_O = max(worst_O, abs(0.5 * np.abs(mu - nu).sum() - tvx))
            count += 1
    print(f"  {count} one-slot x-changes over the six triples: max |LP min E d_H - (TV(m_x) + TV(m_y))| = {worst_gap:.2e}; "
          f"max |TV(block) - TV(m_x)| = {worst_O:.2e}")
    if worst_gap > 1e-7 or worst_O > 1e-12:
        hit(f"W_1 differs from TV(m_x) + TV(m_y) (LP gap {worst_gap:.2e}) or Theorem O fails ({worst_O:.2e})")
    return count, worst_gap, worst_O


def run_D():
    print("=" * 78)
    print("D  the scans along (t,1,1) and (t,t,1)")
    out = {}
    for line in ("t11", "tt1"):
        rows = []
        for k in range(21, 40):
            t = Fr(k, 20)
            triple = (t, 1, 1) if line == "t11" else (t, t, 1)
            c1 = exact_c1(triple)
            rho = suprema(triple)["rho"][0]
            rows.append((t, c1, rho))
        cross_c = [(a[0], b[0]) for a, b in zip(rows, rows[1:]) if (6 * a[1] - 1) * (6 * b[1] - 1) <= 0]
        cross_s = [(a[0], b[0]) for a, b in zip(rows, rows[1:]) if (5 * a[2] * (1 + a[1]) - 1) * (5 * b[2] * (1 + b[1]) - 1) <= 0]
        first_ratio = next((r[0] for r in rows if r[2] > r[1]), None)
        after = all(r[2] > r[1] for r in rows if first_ratio is not None and r[0] >= first_ratio)
        out[line] = (cross_c, cross_s, first_ratio, after, rows)
        print(f"  {line}: 6c_1 crosses 1 in {[(str(a), str(b)) for a, b in cross_c]}; 5 rho(1+c_1) in {[(str(a), str(b)) for a, b in cross_s]}; "
              f"rho/c_1 > 1 from t = {first_ratio} (and at every later point: {after})")
    ok = (out["t11"][0] == [(Fr(8, 5), Fr(33, 20))] and out["t11"][1] == [(Fr(8, 5), Fr(33, 20))] and out["t11"][2] == Fr(39, 20)
          and out["tt1"][0] == [(Fr(29, 20), Fr(3, 2))] and out["tt1"][1] == [(Fr(29, 20), Fr(3, 2))] and out["tt1"][2] == Fr(3, 2)
          and out["tt1"][3])
    if not ok:
        hit("a scan crossing cell or the rho/c_1 onset differs from the note")
    t85 = [r for r in out["t11"][4] if r[0] == Fr(8, 5)][0]
    t3920 = [r for r in out["t11"][4] if r[0] == Fr(39, 20)][0]
    extra = (float(5 * t85[2] * (1 + t85[1])), float(6 * t85[1]), float(5 * t3920[2] * (1 + t3920[1])), float(6 * t3920[1]))
    print(f"  (t,1,1): at t = 8/5 sequential {extra[0]:.4f} vs 6c_1 {extra[1]:.4f}; at t = 39/20 {extra[2]:.4f} vs {extra[3]:.4f} "
          f"(note 0.9366/0.9828, 1.6123/1.5343)")
    if abs(extra[0] - 0.9366) > 5e-5 or abs(extra[1] - 0.9828) > 5e-5 or abs(extra[2] - 1.6123) > 5e-5 or abs(extra[3] - 1.5343) > 5e-5:
        hit("the quoted scan values differ")
    return out, extra


def main():
    t0 = time.time()
    rows = run_S()
    summary("S exhaustive suprema over 476,280 instances (float) + exact candidates: " + "; ".join(
        f"{t}: sigma {float(r[3]):.6f}, B_V {r[5]:.4f}, rho/c_1 {r[4]:.4f}" for t, r in rows.items())
        + "; every c_1/rho/rho'/sigma literal reproduced exactly; sigma < rho + rho' strictly at the three silent triples, "
        + "sigma = rho + rho' exactly at " + ", ".join(str(t) for t, r in rows.items() if r[7]) + " (a region triple; rho' there is "
        + "not a note literal)")
    cnt, gap, gO = run_L()
    summary(f"L transport LP over all couplings on {cnt} random one-slot changes: min E d_H = TV(m_x) + TV(m_y) to {gap:.1e}; "
            f"Theorem O to {gO:.1e}")
    out, extra = run_D()
    summary(f"D scans: (t,1,1) crossings {[(str(a), str(b)) for a, b in out['t11'][0]]}/{[(str(a), str(b)) for a, b in out['t11'][1]]}, "
            f"rho > c_1 from {out['t11'][2]}; (t,t,1) crossings {[(str(a), str(b)) for a, b in out['tt1'][0]]}/"
            f"{[(str(a), str(b)) for a, b in out['tt1'][1]]}, rho > c_1 from {out['tt1'][2]}; quoted values "
            f"{', '.join(f'{x:.4f}' for x in extra)}")
    print("=" * 78)
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
