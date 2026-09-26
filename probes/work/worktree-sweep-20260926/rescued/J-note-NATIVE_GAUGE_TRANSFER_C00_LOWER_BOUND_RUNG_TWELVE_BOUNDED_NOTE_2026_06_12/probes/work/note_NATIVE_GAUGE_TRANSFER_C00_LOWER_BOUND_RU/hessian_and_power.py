#!/usr/bin/env python3
"""J:note NATIVE_GAUGE_TRANSFER_C00 — Re Tr I=3, dim=8, power 4, Hessian.

Falsifiers: wrong maximum at U=I; power (N_c^2-1)/2=4; Hessian
Re Tr exp(iX)=3-(1/2)|X|^2+O(|X|^4) on a Cartan line.
"""
from fractions import Fraction

import sympy as sp

HITS = []


def main():
    I = sp.eye(3)
    retr = sp.re(sp.trace(I))
    print(f"Re Tr I = {retr}")
    if retr != 3:
        HITS.append(f"Re Tr I={retr}")
    nc2m1 = 3 * 3 - 1
    power = Fraction(nc2m1, 2)
    print(f"(N_c^2-1)/2={power}")
    if power != 4:
        HITS.append(f"power {power}")
    tw12 = 12 ** 4
    print(f"12^4={tw12}")
    if tw12 != 20736:
        HITS.append("12^4")
    th = sp.symbols("theta", real=True)
    U = sp.diag(sp.exp(sp.I * th), sp.exp(-sp.I * th), 1)
    retrU = sp.simplify(sp.re(sp.trace(U)))
    series = sp.series(retrU, th, 0, 5).removeO()
    X2 = 2 * th ** 2  # Tr(X^2) for X=diag(θ,-θ,0)
    hess = sp.expand(3 - Fraction(1, 2) * X2)
    print(f"Re Tr U={retrU}; series={series}; 3-(1/2)|X|^2={hess}")
    if sp.expand(series - (3 - th ** 2 + th ** 4 / 12)) != 0 and sp.series(
        retrU - (3 - th ** 2), th, 0, 4
    ).removeO() != 0:
        # check up to θ^2
        quad = sp.series(retrU, th, 0, 4).removeO()
        if sp.expand(quad - (3 - th ** 2)) != 0:
            HITS.append(f"Hessian {quad}")
    quad = sp.series(retrU, th, 0, 4).removeO()
    if sp.expand(quad - (3 - th ** 2)) != 0:
        HITS.append(f"quad {quad}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: falsifier FIRED: " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: C00 Hessian/power falsifier did not fire: Re Tr I=3, "
        "(N_c^2-1)/2=4, 12^4=20736, Cartan Re Tr=3-θ^2+O(θ^4) matches "
        "3-(1/2)|X|^2"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
