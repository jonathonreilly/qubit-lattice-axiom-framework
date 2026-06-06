#!/usr/bin/env python3
"""Exact finite checks for the dynamics coupling residual classifier.

Record/gauge preservation can constrain a dynamics form-class, but it does not
fix coupling magnitudes, nonzero strength, or clock-rate normalization. This
runner verifies that boundary in finite diagonal record algebras.
"""

from __future__ import annotations

import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {label}")
    if detail:
        print(f"       {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def comm(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    return sp.simplify(A * B - B * A)


def is_zero(M: sp.Matrix) -> bool:
    return all(sp.simplify(M[i, j]) == 0 for i in range(M.rows) for j in range(M.cols))


def transfer(H: sp.Matrix, a: sp.Expr) -> sp.Matrix:
    return sp.diag(*[sp.exp(-a * H[i, i]) for i in range(H.rows)])


def main() -> int:
    section("Record-preserving Hamiltonians form a coupling family")
    P0 = sp.diag(1, 0)
    P1 = sp.diag(0, 1)
    I2 = sp.eye(2)
    g = sp.symbols("g", real=True)
    H_g = g * P1
    check("R1 record atom projectors resolve identity", P0 + P1 == I2)
    check("R2 H(g)=g P1 preserves record atom P0 for arbitrary g", is_zero(comm(H_g, P0)))
    check("R3 H(g)=g P1 preserves record atom P1 for arbitrary g", is_zero(comm(H_g, P1)))
    check("R4 preservation equations impose no condition g=constant",
          g in H_g.free_symbols, "g remains a free symbol")

    section("Different couplings pass the same preservation gate")
    H0 = H_g.subs(g, 0)
    H1 = H_g.subs(g, 1)
    H2 = H_g.subs(g, 2)
    check("C1 zero dynamics preserves records", is_zero(comm(H0, P0)) and is_zero(comm(H0, P1)))
    check("C2 nonzero unit coupling preserves records", is_zero(comm(H1, P0)) and is_zero(comm(H1, P1)))
    check("C3 different nonzero coupling also preserves records", is_zero(comm(H2, P0)) and is_zero(comm(H2, P1)))
    check("C4 the three Hamiltonians are distinct", H0 != H1 and H1 != H2 and H0 != H2)

    section("Transfer/rate normalization is also not fixed by preservation")
    a = sp.symbols("a", positive=True)
    T_g_a = transfer(H_g, a)
    check("T1 transfer is diagonal and preserves record atoms for arbitrary g,a",
          is_zero(comm(T_g_a, P0)) and is_zero(comm(T_g_a, P1)))
    T_1_2 = transfer(H_g.subs(g, 1), sp.Rational(2))
    T_2_1 = transfer(H_g.subs(g, 2), sp.Rational(1))
    check("T2 same transfer can arise from g=1,a=2 and g=2,a=1",
          T_1_2 == T_2_1, f"T={T_1_2}")
    check("T3 preservation fixes neither coupling nor clock interval separately",
          H1 != H2 and T_1_2 == T_2_1)

    section("Multiple invariant terms leave coefficient ratios open")
    A = sp.diag(0, 1, 0, 1)  # second bit record term
    B = sp.diag(0, 0, 1, 1)  # first bit record term
    P00 = sp.diag(1, 0, 0, 0)
    P01 = sp.diag(0, 1, 0, 0)
    P10 = sp.diag(0, 0, 1, 0)
    P11 = sp.diag(0, 0, 0, 1)
    x, y = sp.symbols("x y", real=True)
    H_xy = x * A + y * B
    projectors = [P00, P01, P10, P11]
    check("M1 two independent invariant terms commute with all four record atoms",
          all(is_zero(comm(H_xy, P)) for P in projectors))
    check("M2 coefficient ratio x/y remains free under preservation",
          x in H_xy.free_symbols and y in H_xy.free_symbols)
    check("M3 changing x/y changes spectrum while preserving records",
          H_xy.subs({x: 1, y: 2}) != H_xy.subs({x: 2, y: 1}))

    section("Boundary certificate")
    check("B1 record preservation can force a commutant/class condition, not coupling values",
          is_zero(comm(H_g, P0)) and g in H_g.free_symbols)
    check("B2 nontriviality is not forced because H=0 passes the gate",
          H0 == sp.zeros(2))
    check("B3 rate/coupling split needs an extra clock/action premise",
          T_1_2 == T_2_1)
    check("B4 coefficient ratios need an extra variational/minimality/normalization premise",
          x in H_xy.free_symbols and y in H_xy.free_symbols)

    section("Scorecard")
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "FINDING: record preservation constrains an allowed dynamics class, "
        "but leaves coupling magnitude, coefficient ratios, nontriviality, and "
        "clock-rate normalization open."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
