#!/usr/bin/env python3
"""J:attack-d:PR8178 — QUANTIFIER SCOPE.

T1 claims, for every mode k, 1-|φ(k)|² = (4/9)[sin²(k1/2)+sin²(k2/2)+sin²((k1-k2)/2)]
and |φ|<1 off zero. This is an identity in real (k1,k2), not only L=2,3,4.
Check it symbolically and on every mode of L=2..16. Also A(κ)∈(0,1) for κ>0
so τ_L=3βL²/A(3β) is finite for every β>0, L≥1.

Do not re-find the known T1.1 φ vs e^{-ik} conjugation HIT or the D1 1.165 HIT.
"""
from __future__ import annotations

from itertools import product

import sympy as sp

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def main() -> int:
    k1, k2 = sp.symbols("k1 k2", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    u = sp.simplify(sp.expand_complex(phi * sp.conjugate(phi)))
    one_u = sp.simplify(1 - u)
    rhs = sp.simplify(
        (4 * (sp.sin(k1 / 2) ** 2 + sp.sin(k2 / 2) ** 2 + sp.sin((k1 - k2) / 2) ** 2))
        / 9
    )
    gap = sp.simplify(one_u - rhs)
    print(f"symbolic 1-|φ|² − (4/9)[sin²…] = {gap}")
    if gap != 0:
        hit(f"T1 identity not identically 0: {gap}")
    # also vs (2/9)(3-cos-cos-cos)
    rhs2 = sp.simplify(
        (2 * (3 - sp.cos(k1) - sp.cos(k2) - sp.cos(k1 - k2))) / 9
    )
    if sp.simplify(one_u - rhs2) != 0:
        hit("1-|φ|² != (2/9)(3-cos k1-cos k2-cos(k1-k2))")
    else:
        print("  also = (2/9)(3-cos k1-cos k2-cos(k1-k2))")

    print("== every mode of L=2..16: |φ|<1 off zero, identity holds ==")
    for L in range(2, 17):
        nfail = 0
        nmode = 0
        umax = 0
        for n1, n2 in product(range(L), repeat=2):
            kk1 = 2 * sp.pi * n1 / L
            kk2 = 2 * sp.pi * n2 / L
            ph = (1 + sp.exp(sp.I * kk1) + sp.exp(sp.I * kk2)) / 3
            uu = float(sp.re(sp.N(sp.expand_complex(ph * sp.conjugate(ph)), 25)))
            want = (4 / 9) * (
                sp.sin(kk1 / 2) ** 2
                + sp.sin(kk2 / 2) ** 2
                + sp.sin((kk1 - kk2) / 2) ** 2
            )
            want = float(sp.N(want, 25))
            if abs((1 - uu) - want) > 1e-12:
                nfail += 1
            if (n1, n2) == (0, 0):
                if abs(uu - 1) > 1e-12:
                    hit(f"L={L} zero mode u={uu} != 1")
            else:
                nmode += 1
                umax = max(umax, uu)
                if uu >= 1 - 1e-14:
                    hit(f"L={L} n=({n1},{n2}) has u={uu} >= 1")
        print(f"  L={L}: nonzero={nmode} ident_fail={nfail} max_u={umax:.12f}")
        if nfail:
            hit(f"L={L}: identity failed on {nfail} modes")

    print("== A(κ)∈(0,1) for κ>0 so τ_L finite at every β>0 ==")
    kap = sp.symbols("kappa", positive=True)
    A = sp.coth(kap) - 1 / kap
    # A'(κ) = -csch² + 1/κ² < 0 for κ>0? known A∈(0,1)
    for kv in (sp.Rational(1, 100), sp.Rational(1, 10), 1, 3, 6, 12, 24, 48, 100):
        val = sp.N(A.subs(kap, kv), 20)
        print(f"  A({kv})={val}")
        if not (0 < val < 1):
            hit(f"A({kv})={val} not in (0,1)")

    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: QUANTIFIER SCOPE (PR #8178): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: QUANTIFIER SCOPE (PR #8178): T1 1-|φ|²=(4/9)[sin²(k1/2)+…] "
        "holds identically in real k and on every mode of L=2..16 with |φ|<1 "
        "off zero; A(κ)∈(0,1) so τ_L=3βL²/A(3β) is finite for every β>0; "
        "pattern has purchase (known φ-conjugation and D1 1.165 not re-claimed)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
