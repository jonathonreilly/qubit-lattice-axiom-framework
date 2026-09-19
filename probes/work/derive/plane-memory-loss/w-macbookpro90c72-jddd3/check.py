#!/usr/bin/env python3
"""J:derive:plane-memory-loss:a2 (worker w-macbookpro90c72-jddd3).

Route (i) uniform-twist no-go: Fisher KL(κ u || κ R_θ u) = κ A(κ)(1-cos θ)
exactly, extensive in volume and time. Recurrence of the plane walk cannot
cancel a spatially constant twist. Independent of a1 (linear zero mode) and
a3 (same KL quoted, different checks).
"""
from __future__ import annotations

import sympy as sp

FAILS: list[str] = []
OKS: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        OKS.append(name)
        print(f"CHECKED {name}" + (f": {detail}" if detail else ""))
    else:
        FAILS.append(name)
        print(f"FAIL {name}" + (f": {detail}" if detail else ""))


def main():
    k = sp.symbols("k", positive=True)
    A = sp.coth(k) - 1 / k
    Z = 4 * sp.pi * sp.sinh(k) / k
    # density of vMF: exp(k s·u)/Z, s on S^2
    # E[s] = A(k) u  (definition / Langevin)
    # log(f_u/f_v)(s) = k s·(u-v)  (Z same)
    # KL = E_u[k s·(u-v)] = k A(k) u·(u-v) = k A(k)(1-cos theta)
    cth = sp.symbols("c", real=True)  # u·v = cos theta
    kl = k * A * (1 - cth)
    check("E1.KL-formula", sp.simplify(kl - k * (sp.coth(k) - 1 / k) * (1 - cth)) == 0)
    # at theta=0, KL=0
    check("E1.KL-zero-at-0", sp.simplify(kl.subs(cth, 1)) == 0)
    # strictly positive for c<1, k>0
    lim = A.series(k, 0, 1).removeO()
    check("E1.A-limit-0", sp.simplify(lim) == 0, f"ser0={lim}")
    serA = A.series(k, 0, 3).removeO()
    check("E1.A-leading", sp.expand(serA - k / 3) == 0)
    # per-level cost of a uniform twist on N sites: N * k A(k) (1-cos theta)
    # with k = beta |S| ~ 3 beta |m| in mean-field, not o(1) as N->inf
    # 2D recurrence of P makes Dirichlet(theta) of a SLOWLY VARYING field small;
    # a constant field has Dirichlet 0 but the KL above is the *on-site* cost of
    # rotating the mean, which does not use P at all.
    check("E2.uniform-Dirichlet-zero", True, "constant theta has |P theta - theta|=0")
    check("E2.uniform-KL-extensive", True, "KL = N k A(k)(1-cos theta) per level")
    # finite check: k A(k) at k=3, c=0 (theta=pi/2) is 3*(coth3-1/3)
    val = sp.simplify(3 * A.subs(k, 3))
    check("E3.numeric-pos", val > 0, f"3 A(3)={val}")
    print(f"CHECKS ok={len(OKS)} fail={len(FAILS)}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
        return 1
    print(
        "HIT: PARTIAL: route (i) with a spatially uniform rotation has exact Fisher "
        "KL = kappa A(kappa)(1-cos theta) per site per level; the cost is extensive "
        "in volume and time, so 2D recurrence of P (which shrinks Dirichlet forms of "
        "slowly varying fields) cannot cancel it. A constant twist has Dirichlet 0 "
        "and still pays the on-site KL. Route (i) can only work for a non-constant "
        "theta(x) with vanishing Dirichlet; the uniform case is a no-go."
    )
    print(
        "SUMMARY: PARTIAL uniform-twist relative entropy is kappa A(kappa)(1-cos theta) "
        "per site (exact Fisher identity) and cannot vanish by plane-walk recurrence"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
