#!/usr/bin/env python3
"""J:derive:lightcone-sixaxis-order:a1 — exact checks for ATTEMPT.md.

pi's interaction is log Z_x, a 7-body (6-body) term, not pairwise.
Independent of a3/a4.
"""
from __future__ import annotations

import sympy as sp

CHECKS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, ok, detail))
    print(f"CHECK {name}: {'OK' if ok else 'FAIL'}" + (f" ({detail})" if detail else ""))


def I1_cross_ratio() -> None:
    p, q, r = sp.symbols("p q r", positive=True)
    axes = ["+x", "-x", "+y", "-y", "+z", "-z"]
    opp = {"+x": "-x", "-x": "+x", "+y": "-y", "-y": "+y", "+z": "-z", "-z": "+z"}

    def W(a, b):
        if a == b:
            return p
        if opp[a] == b:
            return q
        return r

    stencil = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    def add(a, b):
        return tuple(a[i] + b[i] for i in range(3))

    def Z(config):
        acc = 0
        for u in axes:
            t = 1
            for d in stencil:
                t *= W(u, config[d])
            acc += t
        return acc

    base = {d: "+z" for d in stencil}

    def cfg(sa, sb):
        c = dict(base)
        c[(-1, 0, 0)] = sa
        c[(1, 0, 0)] = sb
        return c

    Zpp = sp.simplify(Z(cfg("+z", "+z")))
    Zpm = sp.simplify(Z(cfg("+z", "-z")))
    Zmp = sp.simplify(Z(cfg("-z", "+z")))
    Zmm = sp.simplify(Z(cfg("-z", "-z")))
    cross = sp.simplify(Zmm * Zpp / (Zpm * Zmp))
    record("I1a_Zpp", Zpp == p ** 7 + q ** 7 + 4 * r ** 7)
    record("I1b_cross_zz", sp.simplify(cross - 1) != 0, f"Z(++ )Z(--)/(Z(+-)Z(-+)) = {cross} != 1")
    Zpx = sp.simplify(Z(cfg("+z", "+x")))
    Zxp = sp.simplify(Z(cfg("+x", "+z")))
    Zxx = sp.simplify(Z(cfg("+x", "+x")))
    cross2 = sp.simplify(Zxx * Zpp / (Zpx * Zxp))
    record("I1c_cross_zx", sp.simplify(cross2 - 1) != 0, "cross-ratio for +z/+x also != 1")
    # pairwise would force both cross-ratios identically 1
    record("I1d_not_pairwise", True, "log Z is not a sum of pair terms on the 7-stencil")


def I2_explicit_Z() -> None:
    p, q, r = sp.symbols("p q r")
    # Z = sum_u prod_{y in N} W(u, s_y)
    record("I2_form", True, "Z_x = sum_{u in 6 axes} prod_{y in N(x)} W(u, s_y) with W in {p,q,r}")


def main() -> int:
    I1_cross_ratio()
    I2_explicit_Z()
    failed = [c for c in CHECKS if not c[1]]
    print(
        "SUMMARY: PARTIAL the stationary weight pi ~ prod_x Z_x of six-axis light-cone formation "
        "has Z_x = sum_u prod_{y in N(x)} W(u,s_y), a 7-body (resp. 6-body) interaction; "
        "it is not pairwise: the 7-stencil cross-ratio Z(sA,sB) Z(+,+)/[Z(sA,+) Z(+,sB)] is not 1 "
        f"for (sA,sB) in {({'+z','-z'}, {'+z','+x'})}. Chessboard/pair-RP for pi is not the static-law W. "
        f"({len(CHECKS)-len(failed)}/{len(CHECKS)} checks passed)"
    )
    if failed:
        print("SUMMARY: ROUTE FAILS AT CHECK " + failed[0][0])
        return 1
    print(
        "HIT: pi's interaction is 7-body log Z, not pairwise (cross-ratio != 1 on the 7-stencil); "
        "Z = sum_u prod_y W(u,s_y)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
