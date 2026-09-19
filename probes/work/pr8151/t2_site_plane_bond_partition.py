#!/usr/bin/env python3
"""J:attack-g:PR8151 — brute-force T2's finite bond-split, NOT the known T3 chessboard HIT.

Note T2 proof (PR #8151): for θ = θ_{1,0} on a torus of even side n=2L,
P = {x : x_1 ∈ {0, L}}, H+ = {0 ≤ x_1 ≤ L}, H- = θ H+,
split the nearest-neighbour bonds into
  W_P  both ends in P,
  W+   both ends in H+ not both in P,
  W-   the mirror set (both ends in H- not both in P);
'every bond is in exactly one class, and W^-(v) = W^+(θ v)'.

This script enumerates the nn undirected bonds on even tori and checks the
partition and the θ-bijection W+ → W- literally. It then checks the weight
identity W^-(v) = W^+(θ v) by full enumeration of six-axis configurations on
the ring of 4 and the 4×2 torus at (3,1,2) and the indefinite (5,2,4).

HIT if a bond is missing from the three classes, sits in two, θ fails to
bijection W+ onto W-, or the weight identity fails for any configuration.
Do not recompute the T3 chessboard orbit (KNOWN HIT).
"""
from __future__ import annotations

import itertools


AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def phi_pair(a, b, p, q, r):
    if a == b:
        return p
    if a == (b[0] * -1, b[1] * -1, b[2] * -1):
        return q
    return r


def sites(shape):
    ranges = [range(n) for n in shape]
    return list(itertools.product(*ranges))


def theta_site(x, n0):
    y = list(x)
    y[0] = (-x[0]) % n0
    return tuple(y)


def nn_bonds(shape):
    d = len(shape)
    out = set()
    for x in sites(shape):
        for i in range(d):
            y = list(x)
            y[i] = (x[i] + 1) % shape[i]
            out.add(frozenset((x, tuple(y))))
        if d < 3:
            # 2-d / 1-d lattice: no extra axes
            pass
    return out


def classify(shape):
    n0 = shape[0]
    if n0 % 2:
        raise ValueError("even side required")
    L = n0 // 2
    B = nn_bonds(shape)
    Wp, Wplus, Wminus = set(), set(), set()
    leftover = []
    double = []
    for b in B:
        ends = list(b)
        xs = [p[0] for p in ends]
        in_p = [xi in (0, L) for xi in xs]
        in_hp = [0 <= xi <= L for xi in xs]
        in_hm = [xi in (0, L) or xi > L for xi in xs]
        both_p = all(in_p)
        both_hp = all(in_hp)
        both_hm = all(in_hm)
        classes = []
        if both_p:
            classes.append("P")
            Wp.add(b)
        if both_hp and not both_p:
            classes.append("+")
            Wplus.add(b)
        if both_hm and not both_p:
            classes.append("-")
            Wminus.add(b)
        if len(classes) == 0:
            leftover.append(b)
        if len(classes) > 1:
            double.append((b, classes))
    return B, Wp, Wplus, Wminus, leftover, double, L


def theta_bond(b, n0):
    return frozenset(theta_site(p, n0) for p in b)


def partition_report(shape):
    B, Wp, Wplus, Wminus, leftover, double, L = classify(shape)
    n0 = shape[0]
    image = {theta_bond(b, n0) for b in Wplus}
    bij = image == Wminus and len(image) == len(Wplus)
    disjoint = (
        not (Wp & Wplus)
        and not (Wp & Wminus)
        and not (Wplus & Wminus)
        and not leftover
        and not double
        and Wp | Wplus | Wminus == B
    )
    # θ involution on sites and on the bond set
    involution = all(theta_site(theta_site(p, n0), n0) == p for p in sites(shape))
    preserves = {theta_bond(b, n0) for b in B} == B
    print(
        f"shape {shape}: |B|={len(B)} |W_P|={len(Wp)} |W+|={len(Wplus)} |W-|={len(Wminus)} "
        f"leftover={len(leftover)} double={len(double)} bijection={bij} "
        f"partition={disjoint} involution={involution} preserves_B={preserves}"
    )
    return leftover, double, bij, disjoint, involution, preserves, (Wp, Wplus, Wminus)


def config_weight_identity(shape, p, q, r, plus, minus):
    n0 = shape[0]
    loc = sites(shape)
    n = len(loc)
    fails = 0
    checked = 0
    for vals in itertools.product(AXES, repeat=n):
        v = dict(zip(loc, vals))
        tv = {x: v[theta_site(x, n0)] for x in loc}

        def W(bonds, cfg):
            acc = 1
            for b in bonds:
                a, c = tuple(b)
                acc *= phi_pair(cfg[a], cfg[c], p, q, r)
            return acc

        wm = W(minus, v)
        wp_th = W(plus, tv)
        checked += 1
        if wm != wp_th:
            fails += 1
            if fails <= 3:
                print("HIT: W^-(v) != W^+(θv)", shape, (p, q, r), wm, wp_th)
    return checked, fails


def main():
    shapes = [(4,), (4, 2), (4, 4), (6, 2), (4, 2, 2), (6, 4), (8, 2)]
    leftover_all = []
    double_all = []
    bij_ok = True
    part_ok = True
    inv_ok = True
    pres_ok = True
    classes = {}
    for sh in shapes:
        leftover, double, bij, disjoint, involution, preserves, cls = partition_report(sh)
        classes[sh] = cls
        leftover_all.extend((sh, b) for b in leftover)
        double_all.extend((sh, b, c) for b, c in double)
        bij_ok = bij_ok and bij
        part_ok = part_ok and disjoint
        inv_ok = inv_ok and involution
        pres_ok = pres_ok and preserves

    # exact weight identity on the note's executed sizes
    weight_fails = 0
    weight_checked = 0
    for sh in ((4,), (4, 2)):
        _, plus, minus = classes[sh]
        for pqr in ((3, 1, 2), (5, 2, 4)):
            n, f = config_weight_identity(sh, *pqr, plus, minus)
            weight_checked += n
            weight_fails += f
            print(f"weight identity {sh} {pqr}: configs={n} fails={f}")

    if leftover_all:
        print("HIT: bonds in none of W_P, W+, W-", leftover_all[:8])
    if double_all:
        print("HIT: bonds in more than one class", double_all[:8])
    if not bij_ok:
        print("HIT: θ does not bijection W+ onto W- on some even torus")
    if not part_ok:
        print("HIT: T2 bond partition is not a partition of the nn bond set")
    if not inv_ok:
        print("HIT: θ_{1,0} is not an involution on sites")
    if not pres_ok:
        print("HIT: θ does not preserve the nn bond set")
    if weight_fails:
        print(f"HIT: W^-(v) != W^+(θv) on {weight_fails} of {weight_checked} configs")

    ok = (
        not leftover_all
        and not double_all
        and bij_ok
        and part_ok
        and inv_ok
        and pres_ok
        and weight_fails == 0
    )
    if ok:
        print(
            "SUMMARY: pattern has no purchase on this note beyond the known T3 chessboard "
            "HIT — T2's finite bond-split (every nn bond in exactly one of W_P, W+, W-; "
            "θ bijection W+ → W-; W^-(v)=W^+(θv) on the ring of 4 and the 4×2 torus at "
            "(3,1,2) and (5,2,4), "
            f"{weight_checked} configs) holds literally by enumeration"
        )
        return 0
    print("SUMMARY: T2 finite bond-split fails under brute force")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
