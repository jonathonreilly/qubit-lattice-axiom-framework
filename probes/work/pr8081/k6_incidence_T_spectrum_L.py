#!/usr/bin/env python3
"""J:attack-g:PR8081 — brute-force T2's finite K6 / T / L(E,F) identities.

Note: N is the 6×15 vertex-edge incidence of K6; NN* = 4I+J6;
T = J15+I-N*N is adjacency of disjoint 2-subsets of six labels;
eigenvalues of T are 6, −3, 1 with multiplicities 1, 5, 9;
hence T² ≤ 3T+18I. T² weights are 6 (equal pairs), 1 (disjoint pairs),
3 (distinct intersecting pairs). Minimizing a²m − a F sqrt(3m+18) over
−3≤m≤6, 0≤a≤E yields the three L(E,F) branches, agreeing at F=2E and F=4E.

HIT if any identity fails at this finite size. Exact integers / Fraction / sympy.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations

import sympy as sp


def L_note(E, F):
    if F <= 2 * E:
        return -3 * E * E - 3 * E * F
    if F <= 4 * E:
        return -6 * E * E - 3 * F * F / 4
    return 6 * E * E - 6 * E * F


def main():
    hits = []
    verts = range(6)
    edges = list(combinations(verts, 2))
    assert len(edges) == 15

    # N: 6×15 incidence
    N = sp.zeros(6, 15)
    for j, e in enumerate(edges):
        N[e[0], j] = 1
        N[e[1], j] = 1
    I6 = sp.eye(6)
    J6 = sp.ones(6)
    nnstar = N * N.T
    claimed_nn = 4 * I6 + J6
    if nnstar != claimed_nn:
        hits.append("HIT: NN* != 4I+J6")
        print("HIT: NN* != 4I+J6")
        print(nnstar)
    else:
        print("NN* = 4I+J6: ok")

    I15 = sp.eye(15)
    J15 = sp.ones(15)
    T_from_N = J15 + I15 - N.T * N
    T_adj = sp.zeros(15)
    for i, a in enumerate(edges):
        for j, b in enumerate(edges):
            if i != j and set(a).isdisjoint(b):
                T_adj[i, j] = 1
    if T_from_N != T_adj:
        hits.append("HIT: J15+I-N*N is not disjoint-pair adjacency")
        print("HIT: T_from_N != T_adj")
    else:
        print("T = J15+I-N*N = disjoint-pair adjacency: ok")

    T = T_adj
    ev = T.eigenvals()
    # eigenvals maps eigenvalue -> multiplicity
    got = {int(lam): int(mult) for lam, mult in ev.items()}
    want = {6: 1, -3: 5, 1: 9}
    if got != want:
        hits.append(f"HIT: T spectrum {got} != {want}")
        print("HIT: T spectrum", got)
    else:
        print("T spectrum 6,-3,1 mult 1,5,9: ok")

    # T² pair weights
    T2 = T * T
    eq_w, inter_w, disj_w, other_w = [], [], [], []
    for i, a in enumerate(edges):
        for j, b in enumerate(edges):
            w = int(T2[i, j])
            sa, sb = set(a), set(b)
            if i == j:
                eq_w.append(w)
            elif sa.isdisjoint(sb):
                disj_w.append(w)
            elif sa & sb:
                inter_w.append(w)
            else:
                other_w.append(w)
    if set(eq_w) != {6}:
        hits.append(f"HIT: T² equal-pair weights {Counter(eq_w)} != {{6:15}}")
        print("HIT: T² equal", Counter(eq_w))
    else:
        print(f"T² equal pairs: 6 (n={len(eq_w)})")
    if set(disj_w) != {1}:
        hits.append(f"HIT: T² disjoint-pair weights {Counter(disj_w)} != {{1}}")
        print("HIT: T² disjoint", Counter(disj_w))
    else:
        print(f"T² disjoint pairs: 1 (n={len(disj_w)})")
    if set(inter_w) != {3}:
        hits.append(f"HIT: T² intersecting-pair weights {Counter(inter_w)} != {{3}}")
        print("HIT: T² intersecting", Counter(inter_w))
    else:
        print(f"T² distinct intersecting pairs: 3 (n={len(inter_w)})")
    if other_w:
        hits.append(f"HIT: unclassified T² pairs {other_w}")
        print("HIT: unclassified T²", other_w)

    gap = 3 * T + 18 * I15 - T2
    gev = gap.eigenvals()
    if any(sp.sympify(lam) < 0 for lam in gev):
        hits.append(f"HIT: 3T+18I-T² has negative eigenvalue {gev}")
        print("HIT: T² not <= 3T+18I", gev)
    else:
        print("T² <= 3T+18I (exact PSD of 3T+18I-T²):", {int(k): int(v) for k, v in gev.items()})

    # L(E,F) branch joins at F=2E and F=4E
    E = Fraction(3, 7)
    a = -3 * E * E - 3 * E * (2 * E)
    b = -6 * E * E - 3 * (2 * E) * (2 * E) / 4
    c = -6 * E * E - 3 * (4 * E) * (4 * E) / 4
    d = 6 * E * E - 6 * E * (4 * E)
    if a != b:
        hits.append(f"HIT: L join at F=2E: {a} vs {b}")
        print("HIT: L join 2E", a, b)
    else:
        print(f"L join F=2E: {a}")
    if c != d:
        hits.append(f"HIT: L join at F=4E: {c} vs {d}")
        print("HIT: L join 4E", c, d)
    else:
        print(f"L join F=4E: {c}")

    # calculus: min of g=a²m − a F sqrt(3m+18) on the rectangle equals L
    # critical m on a=E is m = 3 F²/(4 E²) − 6, in [-3,6] iff 2E≤F≤4E,
    # value −6E² − 3F²/4; endpoints give the other two branches.
    m_sym = sp.symbols("m", real=True)
    E_sym, F_sym = sp.symbols("E F", positive=True)
    h = E_sym ** 2 * m_sym - E_sym * F_sym * sp.sqrt(3 * m_sym + 18)
    dh = sp.diff(h, m_sym)
    crit = sp.solve(dh, m_sym)
    print("dh/dm=0 solutions:", crit)
    expected_m = 3 * F_sym ** 2 / (4 * E_sym ** 2) - 6
    ok_crit = False
    for sol in crit:
        if sp.simplify(sol - expected_m) == 0:
            ok_crit = True
    if not ok_crit:
        hits.append(f"HIT: critical m of h(m) is {crit}, not 3F^2/(4E^2)-6")
        print("HIT: critical m", crit)
    h_at = sp.simplify(h.subs(m_sym, expected_m))
    want_mid = -6 * E_sym ** 2 - 3 * F_sym ** 2 / 4
    if sp.simplify(h_at - want_mid) != 0:
        hits.append(f"HIT: h(m_crit)={h_at} != -6E^2-3F^2/4")
        print("HIT: h at crit", h_at)
    else:
        print("h(m_crit) = -6E^2-3F^2/4: ok")

    # dense exact samples: L is a lower bound, and is attained at the claimed corners
    samples_ok = True
    attained = 0
    ratios = [
        (Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(1, 2)),
        (Fraction(1), Fraction(1)),
        (Fraction(1), Fraction(2)),
        (Fraction(1), Fraction(3)),
        (Fraction(1), Fraction(4)),
        (Fraction(1), Fraction(5)),
        (Fraction(1), Fraction(8)),
        (Fraction(5, 3), Fraction(7, 2)),
        (Fraction(7, 2), Fraction(5, 3)),
        (Fraction(4, 11), Fraction(9, 5)),
    ]
    m_grid = [Fraction(-3)] + [Fraction(k, 4) for k in range(-11, 25)] + [Fraction(6)]
    a_grid_n = 9
    for E0, F0 in ratios:
        L0 = L_note(E0, F0)
        for m0 in m_grid:
            s2 = 3 * m0 + 18
            # s = sqrt(s2); compare g = m a^2 - a F sqrt(s2) via (L - m a^2)^2 vs (a F)^2 s2
            # when L is the claimed min, we need g >= L i.e. m a^2 - L >= a F sqrt(s2) >= 0
            # skip m with s2 < 0 (none in range)
            for t in range(a_grid_n):
                a0 = E0 * Fraction(t, a_grid_n - 1)
                # g as algebraic number: compare using squares when a F >= 0
                # g - L0 = m a^2 - L0 - a F sqrt(s2). Need this >= 0.
                left = m0 * a0 * a0 - L0  # should be >= a F sqrt(s2) >= 0
                right_sq = (a0 * F0) ** 2 * s2
                if left < 0:
                    # then g - L0 < -a F sqrt <= 0 so g < L0 unless both zero
                    if left * left > right_sq or (left < 0 and right_sq >= 0 and not (left == 0 and right_sq == 0)):
                        # left < 0 => left - sqrt(right) < 0 => g < L
                        samples_ok = False
                        hits.append(
                            f"HIT: g(a,m)<L at E={E0} F={F0} a={a0} m={m0} left={left}"
                        )
                        print("HIT: sample g<L", E0, F0, a0, m0, left)
                        break
                else:
                    # left >= sqrt(right) iff left^2 >= right_sq
                    if left * left < right_sq:
                        samples_ok = False
                        hits.append(
                            f"HIT: g(a,m)<L at E={E0} F={F0} a={a0} m={m0}"
                        )
                        print("HIT: sample g<L", E0, F0, a0, m0)
                        break
            if not samples_ok:
                break
        # attainment: plug the claimed (a,m)
        if F0 <= 2 * E0:
            a_att, m_att = E0, Fraction(-3)
        elif F0 <= 4 * E0:
            a_att, m_att = E0, 3 * F0 * F0 / (4 * E0 * E0) - 6
        else:
            a_att, m_att = E0, Fraction(6)
        s2 = 3 * m_att + 18
        # g = m a^2 - a F sqrt(s2); check g == L by (m a^2 - L)^2 == (a F)^2 s2 and ma^2-L >= 0
        left = m_att * a_att * a_att - L0
        right_sq = (a_att * F0) ** 2 * s2
        if left < 0 or left * left != right_sq:
            hits.append(f"HIT: L not attained at claimed (a,m) E={E0} F={F0} left={left} right_sq={right_sq}")
            print("HIT: L not attained", E0, F0, left, right_sq)
        else:
            attained += 1
        if not samples_ok:
            break
    print(f"L lower-bound samples ok={samples_ok}; attained at claimed points {attained}/{len(ratios)}")

    # decrease in each nonnegative error bound: L(E+d,F)<=L(E,F) and L(E,F+d)<=L(E,F)
    mono_ok = True
    for E0, F0 in ratios:
        for d in (Fraction(1, 10), Fraction(1)):
            if L_note(E0 + d, F0) > L_note(E0, F0) or L_note(E0, F0 + d) > L_note(E0, F0):
                mono_ok = False
                hits.append(f"HIT: L not decreasing at E={E0} F={F0} d={d}")
                print("HIT: L not decreasing", E0, F0, d)
    print(f"L decreasing in E and F: {mono_ok}")

    if hits:
        print("SUMMARY: T2 finite K6/T/L identities fail under brute force")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — K6 incidence NN*=4I+J6, "
        "T=J15+I-N*N is disjoint-pair adjacency with exact spectrum 6,-3,1 (1,5,9), "
        "T² weights 6/1/3, T²<=3T+18I, and L(E,F) branches (joins at F=2E,4E; "
        "critical m=3F²/(4E²)-6; attained on 11 exact (E,F) ratios) hold literally"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
