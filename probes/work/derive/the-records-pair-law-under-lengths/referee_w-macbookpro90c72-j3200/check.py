#!/usr/bin/env python3
"""Referee for the-records-pair-law-under-lengths a1. Own balance checks.

Author w-jonathonsmac4f50-jf594 (claude-opus-5-5). Does not call their script.
"""
import itertools
from fractions import Fraction as Fr
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def held_balance():
    """One generic hop: w_x * s(chi_x*chi_y) cancels against pi ~ W/w, for any symmetric s."""
    W, Wp, wx, s = sp.symbols("W Wp w_x s", positive=True)
    # pi * rate, with the 1/w_x in the law and h = Wp/(W+Wp)
    fwd = (W / wx) * (wx * s * Wp / (W + Wp))
    rev = (Wp / sp.symbols("w_y", positive=True)) * (sp.symbols("w_y", positive=True) * s * W / (W + Wp))
    ok = sp.simplify(fwd - rev) == 0
    # own-site length l_x = chi_x**2 does not cancel: leftover chi_y**2/chi_x**2
    cx, cy = sp.symbols("chi_x chi_y", positive=True)
    fwd_own = (W / wx) * (wx / cx**2) * Wp / (W + Wp)
    rev_own = (Wp / sp.symbols("w_y", positive=True)) * (sp.symbols("w_y", positive=True) / cy**2) * W / (W + Wp)
    ratio = sp.simplify(fwd_own / rev_own)
    ok_own = ratio == cy**2 / cx**2
    # ring of 4, two records, s(u) = u**2 + 3, rational weights, every legal hop
    n = 4
    w = [Fr(2), Fr(5), Fr(1, 3), Fr(7)]
    chi = [Fr(4), Fr(1, 2), Fr(3), Fr(9)]
    pair = Fr(5, 2)

    def weight(C):
        val = Fr(1)
        for a, b in itertools.combinations(C, 2):
            if (a - b) % n in (1, n - 1):
                val *= pair
        return val

    def law(C):
        val = weight(C)
        for z in C:
            val /= w[z]
        return val

    def s_bond(x, y):
        u = chi[x] * chi[y]
        return u * u + 3

    bad = 0
    seen = 0
    for C in itertools.combinations(range(n), 2):
        for x in C:
            for y in ((x + 1) % n, (x - 1) % n):
                if y in C:
                    continue
                Cp = tuple(sorted(z for z in C if z != x) + [y])
                h = weight(Cp) / (weight(C) + weight(Cp))
                r1 = w[x] * s_bond(x, y) * h
                r2 = w[y] * s_bond(y, x) * (weight(C) / (weight(C) + weight(Cp)))
                seen += 1
                if law(C) * r1 != law(Cp) * r2:
                    bad += 1
    # direction odds on the ring: s = 1/(chi_x chi_y) cancels chi_x
    x0 = 1
    left, right = (x0 - 1) % n, (x0 + 1) % n
    p_right = (1 / chi[right]) / (1 / chi[left] + 1 / chi[right])
    odds_ok = p_right == chi[left] / (chi[left] + chi[right])
    report(
        "held field",
        bool(ok and ok_own and bad == 0 and seen > 0 and odds_ok),
        f"generic hop balances for any symmetric bond factor; own-site length leaves chi_y^2/chi_x^2; "
        f"ring of 4, two records, {seen} hops, {bad} failures",
    )


def slaved():
    """L=2 torus, even rational kernels, every hop of two and three records."""
    L = 2
    sites = list(itertools.product(range(L), repeat=3))

    def delta(a, b):
        return tuple((a[i] - b[i]) % L for i in range(3))

    def canonical(d):
        return min(d, tuple((-c) % L for c in d))

    keys = sorted({canonical(d) for d in sites})
    # different rationals from the author's 3^3 table
    om = {k: Fr(i + 2, i + 5) for i, k in enumerate(keys)}
    lam = {k: Fr(3 * i + 1, i + 4) for i, k in enumerate(keys)}

    def factor(table, C, z):
        val = Fr(1)
        for r in C:
            val *= table[canonical(delta(z, r))]
        return val

    def nbrs(x):
        out = []
        for j in range(3):
            for sgn in (1, -1):
                y = list(x)
                y[j] = (y[j] + sgn) % L
                out.append(tuple(y))
        return out

    def pair_law(C):
        val = Fr(1)
        for a, b in itertools.combinations(C, 2):
            val /= om[canonical(delta(a, b))]
        return val

    def check_bond(nrec, bond, law):
        bad = 0
        seen = 0
        for C in itertools.combinations(sites, nrec):
            for x in C:
                for y in nbrs(x):
                    if y in C:
                        continue
                    Cp = tuple(sorted([z for z in C if z != x] + [y]))
                    r1 = factor(om, C, x) * bond(C, x, y)
                    r2 = factor(om, Cp, y) * bond(Cp, y, x)
                    seen += 1
                    if law(C) * r1 != law(Cp) * r2:
                        bad += 1
        return bad, seen

    bond = lambda C, x, y: 1 / (factor(lam, C, x) * factor(lam, C, y))
    b2, n2 = check_bond(2, bond, pair_law)
    b3, n3 = check_bond(3, bond, pair_law)
    # non-product symmetric factor must fail somewhere
    bsum = lambda C, x, y: 1 / (factor(lam, C, x) + factor(lam, C, y))
    bs, _ = check_bond(2, bsum, pair_law)
    def dbl_law(C):
        val = Fr(1)
        for z in C:
            val /= factor(om, C, z)
        return val

    bd, _ = check_bond(2, bond, dbl_law)
    report(
        "slaved field",
        b2 == 0 and b3 == 0 and bs > 0 and bd > 0 and n2 > 0 and n3 > 0,
        f"L=2 exhaustive: two-record failures {b2}/{n2}, three-record {b3}/{n3}; "
        f"non-product bond failures {bs}; double-counted 1/w failures {bd}",
    )


def odd_control():
    """On L=3 a hop along an odd axis changes chi_x chi_y. The same hop with an even kernel does not."""
    L = 3
    x, y = (0, 0, 0), (1, 0, 0)
    C, Cp = (x,), (y,)

    def product(lam, conf, a, b):
        def chi(z):
            val = Fr(1)
            for r in conf:
                off = tuple((z[i] - r[i]) % L for i in range(3))
                val *= lam(off)
            return val
        return chi(a) * chi(b)

    def lam_odd(d):
        signed = (d[0] + 1) % L - 1
        return Fr(2 + signed, 3)

    def lam_even(d):
        signed = (d[0] + 1) % L - 1
        return Fr(2 + abs(signed), 3)

    before_odd = product(lam_odd, C, x, y)
    after_odd = product(lam_odd, Cp, y, x)
    before_even = product(lam_even, C, x, y)
    after_even = product(lam_even, Cp, y, x)
    report(
        "evenness",
        before_odd != after_odd and before_even == after_even,
        f"odd kernel {before_odd} -> {after_odd}; even kernel {before_even} -> {after_even}",
    )


def turn():
    b = sp.symbols("b", positive=True)
    x = sp.symbols("x", real=True)
    # transverse derivative of 1/(4 pi r), integrated on the line at impact b
    g = 1 / (4 * sp.pi * sp.sqrt(x**2 + b**2))
    integ = sp.integrate(sp.diff(g, b), (x, -sp.oo, sp.oo))
    ok_line = sp.simplify(integ + 2 / (4 * sp.pi * b)) == 0
    eps, Q, gb = sp.symbols("epsilon Q g", positive=True)
    chi = 1 + eps * Q * gb
    N = 1 - eps * Q * gb
    logw = sp.series(sp.log(N / chi), eps, 0, 2).removeO()
    logl = sp.series(sp.log(chi**2), eps, 0, 2).removeO()
    ok_logs = sp.simplify(logw + 2 * eps * Q * gb) == 0 and sp.simplify(logl - 2 * eps * Q * gb) == 0
    logc = logw - logl
    # deflection = - integral of d_perp log c = -2 * log c_1 when log c = (log c_1/g) * g
    delta = -2 * logc
    logg = -logw
    ok_four = sp.simplify(delta / logg - 4) == 0
    beta, lw = sp.symbols("beta lw")
    logc_beta = (1 + beta) * lw
    delta_beta = -2 * logc_beta
    logg_beta = -lw
    ok_beta = sp.simplify(delta_beta / logg_beta - 2 * (1 + beta)) == 0
    # own-site length: pair excess picks up +log l as well, and log l_1 = -log w_1 at beta=1
    logg_own = -logw + logl
    ok_own = sp.simplify(delta / logg_own - 2) == 0
    logg_vol = logg - 3 * logl
    ok_vol = sp.simplify(logg_vol + delta / 2) == 0
    report(
        "turn",
        bool(ok_line and ok_logs and ok_four and ok_beta and ok_own and ok_vol),
        "line integral is -2/(4 pi b); log w_1=-2Qg, log l_1=+2Qg; "
        "delta = 4 log g at beta=1, 2(1+beta) log g in general; own-site reading gives 2 log g; "
        "per volume l^3, log g_vol = -delta/2",
    )


def main():
    held_balance()
    slaved()
    odd_control()
    turn()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - hops timed by the occupied site and crossing a bond at any function of chi_x chi_y "
        "have stationary law W(C) prod 1/w in a held field, and pair law W(C) exp(-sum_pairs log w_1) "
        "in an even first-order slaved field. Under block 60, beta=1, the turn is 4 log g; "
        "a hop that reads its own site's length gives 2 log g."
    )
    print(
        "SUMMARY: confirmed on a generic hop, a ring of 4, and every hop of two and three records on the L=2 torus. "
        "The author's 3^3 sample was not replayed. An odd length kernel does not cancel, so evenness is necessary. "
        "Second order in the slaved field was left open by the attempt and was not claimed."
    )


if __name__ == "__main__":
    main()
