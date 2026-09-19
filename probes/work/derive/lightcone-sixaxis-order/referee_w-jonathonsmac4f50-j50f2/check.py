#!/usr/bin/env python3
"""Referee check for J:derive:lightcone-sixaxis-order:a4 (author w-macbookpro90c72-j7b47, grok-4.6); referee w-jonathonsmac4f50-j50f2.

Independent code. pi(s) = prod_x Z_x(s), Z_x(s) = sum_u prod_{y in N(x)} W(u, s_y), W = p (same), q (antipodal), r (orthogonal) on the six
axes; stencil N(x) = {x, x +- e_j} (n = 7) or {x +- e_j} (n = 6), on the nondegenerate 3^3 torus.

R1  the one-flip ratio: pi(origin flipped)/pi(aligned) by direct products over all 27 sites, against the attempt's
    rho_n = [(p^(n-1) q + p q^(n-1) + 4 r^n)/(p^n + q^n + 4 r^n)]^n, at (3,1,2) (the stated rho_7) and at couplings with p < q.
R2  the sign: D - N = (p - q)(p^(n-1) - q^(n-1)) >= 0 for ALL p, q (both factors carry the sign of p - q), so rho_n < 1 iff p != q, not iff
    p > q; the orthogonal flip (never considered by the attempt): D - Z_o = (p - r)(p^(n-1) - r^(n-1)) + (q - r)(q^(n-1) - r^(n-1)) >= 0.
R3  globally: by Hoelder, Z_x(s) <= p^n + q^n + 4 r^n at every site for every s, so the six constants maximise pi for every (p, q, r);
    checked on random configurations and by hill-climbing on the 3^3 torus at couplings with p > q and with p < q.
"""
from __future__ import annotations

import itertools
import random
from fractions import Fraction as F

import sympy as sp

AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
L = 3
SITES = list(itertools.product(range(L), repeat=3))


def W(a, b, p, q, r):
    d = sum(x * y for x, y in zip(AXES[a], AXES[b]))
    return p if d == 1 else (q if d == -1 else r)


def stencil(x, n):
    nb = [tuple((x[i] + (d if i == j else 0)) % L for i in range(3)) for j in range(3) for d in (1, -1)]
    return ([x] + nb) if n == 7 else nb


def Zx(s, x, n, p, q, r):
    return sum(F(1) * _prod(W(u, s[y], p, q, r) for y in stencil(x, n)) for u in range(6))


def _prod(it):
    out = F(1)
    for v in it:
        out *= v
    return out


def log_pi_ratio(s, n, p, q, r, base):
    """pi(s)/pi(base) as an exact Fraction."""
    out = F(1)
    for x in SITES:
        out *= Zx(s, x, n, p, q, r) / Zx(base, x, n, p, q, r)
    return out


def r1():
    PZ, MZ, PX = 4, 5, 0
    rows = []
    for (p, q, r) in ((3, 1, 2), (1, 3, 2), (1, 2, 1), (2, 3, 5), (2, 2, 1)):
        p, q, r = F(p), F(q), F(r)
        for n in (7, 6):
            aligned = {x: PZ for x in SITES}
            flip = dict(aligned)
            flip[(0, 0, 0)] = MZ
            orth = dict(aligned)
            orth[(0, 0, 0)] = PX
            direct = log_pi_ratio(flip, n, p, q, r, aligned)
            formula = ((p ** (n - 1) * q + p * q ** (n - 1) + 4 * r ** n) / (p ** n + q ** n + 4 * r ** n)) ** n
            orth_ratio = log_pi_ratio(orth, n, p, q, r, aligned)
            rows.append(((int(p), int(q), int(r)), n, direct, direct == formula, orth_ratio))
    return rows


def r2():
    p, q, r = sp.symbols("p q r", positive=True)
    out = []
    for n in (6, 7):
        D = p ** n + q ** n + 4 * r ** n
        N = p ** (n - 1) * q + p * q ** (n - 1) + 4 * r ** n
        Zo = r * p ** (n - 1) + r * q ** (n - 1) + p * r ** (n - 1) + q * r ** (n - 1) + 2 * r ** n
        g1 = sp.expand(D - N - (p - q) * (p ** (n - 1) - q ** (n - 1))) == 0
        g2 = sp.expand(D - Zo - ((p - r) * (p ** (n - 1) - r ** (n - 1)) + (q - r) * (q ** (n - 1) - r ** (n - 1)))) == 0
        out.append((n, g1, g2))
    return out


def r3(seed=17):
    rng = random.Random(seed)
    res = []
    for (p, q, r) in ((F(3), F(1), F(2)), (F(1), F(3), F(2)), (F(5, 4), F(2), F(1, 2))):
        for n in (7,):
            aligned = {x: 4 for x in SITES}
            Dz = Zx(aligned, (0, 0, 0), n, p, q, r)
            # per-site Hoelder bound on random stencils
            bound_ok = True
            for _ in range(300):
                s = {x: rng.randrange(6) for x in SITES}
                x = rng.choice(SITES)
                bound_ok &= Zx(s, x, n, p, q, r) <= Dz
            # hill-climb for a configuration beating the aligned one
            best = F(0)
            for _ in range(4):
                s = {x: rng.randrange(6) for x in SITES}
                cur = log_pi_ratio(s, n, p, q, r, aligned)
                for _ in range(120):
                    x = rng.choice(SITES)
                    t = dict(s)
                    t[x] = rng.randrange(6)
                    val = log_pi_ratio(t, n, p, q, r, aligned)
                    if val >= cur:
                        s, cur = t, val
                best = max(best, cur)
            res.append(((p, q, r), bound_ok, best))
    return res


def main():
    rows = r1()
    for pqr, n, direct, same, orth in rows:
        print(f"R1 (p,q,r)={pqr}, n={n}: antipodal one-flip pi ratio = {direct} ({float(direct):.4g}); = attempt's rho_n: {same}; "
              f"orthogonal one-flip ratio = {float(orth):.4g}")
    for n, g1, g2 in r2():
        print(f"R2 n={n}: D - N = (p-q)(p^(n-1) - q^(n-1)) identically: {g1}; D - Z_o = (p-r)(p^(n-1)-r^(n-1)) + (q-r)(q^(n-1)-r^(n-1)): {g2}")
    for pqr, bound_ok, best in r3():
        print(f"R3 (p,q,r)={tuple(str(v) for v in pqr)}: Z_x <= p^7+q^7+4r^7 on 300 random stencils: {bound_ok}; best pi(s)/pi(aligned) "
              f"found by hill-climbing = {float(best):.4g}")
    stated = [d for pqr, n, d, same, o in rows if pqr == (3, 1, 2) and n == 7][0]
    formula_ok = all(same for _, _, _, same, _ in rows)
    below_for_p_lt_q = all(d < 1 for pqr, n, d, same, o in rows if pqr[0] < pqr[1])
    equal_at_p_eq_q = all(d == 1 for pqr, n, d, same, o in rows if pqr[0] == pqr[1])
    orth_below = all(o < 1 for pqr, n, d, same, o in rows)
    if formula_ok and stated == F(281399112371155271, 63844929217529296875) and below_for_p_lt_q and equal_at_p_eq_q:
        print("SUMMARY: fails at step 3 - the one-flip formula rho_n and the stated rho_7 at (3,1,2) re-derive by direct products on the 3^3 "
              "torus, but the gap (p-q)(p^(n-1)-q^(n-1)) is a product of two factors with the sign of p-q, so it is >= 0 for every p, q: "
              "rho_n < 1 iff p != q, not iff p > q (e.g. (1,3,2): rho_7 = " +
              f"{float([d for pqr, n, d, s_, o in rows if pqr == (1, 3, 2) and n == 7][0]):.3g}); 'strict local maximum' also needs the orthogonal "
              f"flips, which the attempt never checks (their gap (p-r)(p^(n-1)-r^(n-1)) + (q-r)(q^(n-1)-r^(n-1)) >= 0; ratios below 1: "
              f"{orth_below}); by Hoelder Z_x <= p^n + q^n + 4r^n at every site, so the six constants maximise pi for every coupling, "
              "and the local condition says nothing about p > q")
    else:
        print(f"SUMMARY: fails - formula {formula_ok}, stated {stated}, p<q {below_for_p_lt_q}, p=q {equal_at_p_eq_q}")


if __name__ == "__main__":
    main()
