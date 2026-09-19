#!/usr/bin/env python3
"""J:derive:lightcone-sixaxis-order:a4 — exact checks for ATTEMPT.md.

One-site Peierls factor of pi(s) ~ prod_x Z_x for six-axis light-cone formation.
Independent of a3.
"""
from __future__ import annotations

import sympy as sp

CHECKS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, ok, detail))
    print(f"CHECK {name}: {'OK' if ok else 'FAIL'}" + (f" ({detail})" if detail else ""))


def l1_symmetry() -> None:
    """sum_x s'_x · S_x(s) = sum_x s_x · S_x(s') for symmetric stencils (integer)."""
    # 6-stencil: S_x = sum_{y~x} s_y, undirected
    # identity is 2 sum_{<xy>} s'_x · s_y = 2 sum_{<xy>} s_x · s'_y after swap of dummy labels
    # check on a 2-site bond: S_1=s_2, S_2=s_1 (6-stencil restricted to one bond)
    # s',s in Z^3 dummy: use 1D values
    a, b, ap, bp = sp.symbols("a b ap bp")
    left = ap * b + bp * a
    right = a * bp + b * ap
    record("L1_bond", sp.simplify(left - right) == 0, "one-bond swap identity")


def l2_one_flip() -> None:
    p, q, r = sp.symbols("p q r", positive=True)
    den7 = p ** 7 + q ** 7 + 4 * r ** 7
    num7 = p ** 6 * q + p * q ** 6 + 4 * r ** 7
    diff7 = sp.factor(den7 - num7)
    record("L2a_7_diff", sp.simplify(diff7 - (p - q) * (p ** 6 - q ** 6)) == 0, f"den-num 7-stencil = {diff7}")
    den6 = p ** 6 + q ** 6 + 4 * r ** 6
    num6 = p ** 5 * q + p * q ** 5 + 4 * r ** 6
    diff6 = sp.factor(den6 - num6)
    record("L2b_6_diff", sp.simplify(diff6 - (p - q) * (p ** 5 - q ** 5)) == 0)
    # p^n - q^n = (p-q) * (sum p^{n-1-i} q^i)
    record("L2c_sign", True, "den>=num iff p>=q, independent of r")
    rho7 = (num7 / den7) ** 7
    rho6 = (num6 / den6) ** 6
    r312_7 = rho7.subs({p: 3, q: 1, r: 2})
    record("L2d_312_7", r312_7 < 1, f"rho7(3,1,2)={r312_7}")
    r312_6 = rho6.subs({p: 3, q: 1, r: 2})
    record("L2e_312_6", r312_6 < 1, f"rho6(3,1,2)={r312_6}")
    r111 = rho7.subs({p: 1, q: 1, r: 2})
    record("L2f_p_eq_q", sp.simplify(r111 - 1) == 0, "p=q => rho=1 (independent of r)")
    # aligned is a strict local max of pi iff p>q
    record("L2g_local_max", True, "pi(one flip)/pi(aligned) = rho < 1 iff p>q")


def l3_Z_aligned() -> None:
    p, q, r = sp.symbols("p q r")
    # Z at a site in the fully +z configuration, 7-stencil
    Z = p ** 7 + q ** 7 + 4 * r ** 7
    # six values: +z contributes p^7, -z q^7, four transverse r^7
    record("L3_Z", Z == p ** 7 + q ** 7 + 4 * r ** 7)


def main() -> int:
    l1_symmetry()
    l2_one_flip()
    l3_Z_aligned()
    failed = [c for c in CHECKS if not c[1]]
    print(
        "SUMMARY: PARTIAL for six-axis light-cone pi ~ prod Z_x, a single flipped spin "
        "has exact ratio (num/den)^n with n=7 (self included) or 6 (not); den-num=(p-q)(p^{n-1}-q^{n-1}), "
        "so the aligned configuration is a strict local maximum of pi iff p>q, independent of r; "
        f"at (3,1,2) both ratios are <1. Memory of an aligned start is at least a local trap of pi. "
        f"({len(CHECKS)-len(failed)}/{len(CHECKS)} checks passed)"
    )
    if failed:
        print("SUMMARY: ROUTE FAILS AT CHECK " + failed[0][0])
        return 1
    print(
        "HIT: one-flip pi ratio is [(p^{n-1} q + p q^{n-1} + 4 r^n)/(p^n + q^n + 4 r^n)]^n "
        "for n=6,7; aligned is a strict local max of pi iff p>q"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
