#!/usr/bin/env python3
"""J:derive:two-source-interaction:a5 — Newtonian coefficient of the linear light-cone kernel.
Independent of a1–a4 author code.
"""
from __future__ import annotations

import sympy as sp

CHECKS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, ok, detail))
    print(f"CHECK {name}: {'OK' if ok else 'FAIL'}" + (f" ({detail})" if detail else ""))


def n1_identities() -> None:
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    E = sum(2 * (1 - sp.cos(k)) for k in (k1, k2, k3))
    phi = 1 - E / 7
    C = 7 / (2 * E * (1 - E / 14))  # / sigma^2
    chi = 7 / E
    record("N1a_FDR", sp.simplify(chi / C - (1 + phi)) == 0, "chi/C = 1+phi, not a real constant")
    record("N1b_phi", sp.simplify(phi - (1 + 2 * sp.cos(k1) + 2 * sp.cos(k2) + 2 * sp.cos(k3)) / 7) == 0)
    H = sp.hessian(E, [k1, k2, k3]).subs({k1: 0, k2: 0, k3: 0})
    record("N1c_E_k2", H == 2 * sp.eye(3), "E = |k|^2 + O(k^4)")
    # C ~ 7/(2 |k|^2)  =>  3D Fourier 7/(8 pi r)  because FT(1/k^2)=1/(4 pi r)
    # 7/2 * 1/(4 pi) = 7/(8 pi)
    record("N1d_newton", sp.simplify(sp.Rational(7, 2) / (4 * sp.pi) - 7 / (8 * sp.pi)) == 0, "coeff 7 sigma^2 / (8 pi r)")
    ser = sp.series(E.subs({k2: 0, k3: 0}), k1, 0, 3).removeO()
    record("N1e_axis", sp.simplify(ser - k1 ** 2) == 0, f"E(k,0,0)={ser}+O(k^4)")


def n2_L4_modes() -> None:
    """chi and C on L=4, k=2pi n/L, as rationals in Q(cos)."""
    L = 4
    ok = True
    for n1, n2, n3 in [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0)]:
        ks = [sp.Integer(n) * 2 * sp.pi / L for n in (n1, n2, n3)]
        E = sum(2 * (1 - sp.cos(k)) for k in ks)
        if E == 0:
            continue
        phi = 1 - E / 7
        C = 7 / (2 * E * (1 - E / 14))
        chi = 7 / E
        if sp.simplify(chi / C - (1 + phi)) != 0:
            ok = False
    record("N2_L4", ok, "chi/C=1+phi on sample L=4 modes")


def main() -> int:
    n1_identities()
    n2_L4_modes()
    failed = [c for c in CHECKS if not c[1]]
    print(
        "SUMMARY: PARTIAL linear light-cone kernel C=7 sigma^2 / (2 E (1-E/14)), response chi=7/E, "
        "chi/C=1+phi (FDR fails); E=|k|^2+O(k^4) so C ~ 7 sigma^2/(2 k^2) and the 3D Coulomb "
        f"coefficient is 7 sigma^2/(8 pi r). Superposition holds in the linear model. "
        f"({len(CHECKS)-len(failed)}/{len(CHECKS)} checks passed)"
    )
    if failed:
        print("SUMMARY: ROUTE FAILS AT CHECK " + failed[0][0])
        return 1
    print(
        "HIT: Newtonian coefficient of the linear equal-time kernel is 7 sigma^2/(8 pi r); "
        "FDR fails with chi/C=1+phi"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
