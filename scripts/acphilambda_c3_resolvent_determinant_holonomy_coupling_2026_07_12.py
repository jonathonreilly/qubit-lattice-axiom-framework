#!/usr/bin/env python3
"""Exact C3 resolvent and determinant-holonomy coupling checks."""

from __future__ import annotations

import sympy as sp


PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if bool(condition):
        PASS_COUNT += 1
        print(f"PASS  {label}")
    else:
        FAIL_COUNT += 1
        suffix = f" -- {detail}" if detail != "" else ""
        print(f"FAIL  {label}{suffix}")


def realification(matrix: sp.Matrix) -> sp.Matrix:
    real = matrix.applyfunc(sp.re)
    imag = matrix.applyfunc(sp.im)
    return real.row_join(-imag).col_join(imag.row_join(real))


def pfaffian4(matrix: sp.Matrix) -> sp.Expr:
    return sp.expand(
        matrix[0, 1] * matrix[2, 3]
        - matrix[0, 2] * matrix[1, 3]
        + matrix[0, 3] * matrix[1, 2]
    )


def main() -> int:
    print("AC_phi_lambda C3 resolvent determinant-holonomy coupling")
    print()

    print("Part A: normal representation and resolvents")
    P3 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    basis = sp.Matrix([[1, 0], [-1, 1], [0, -1]])
    normal = sp.Matrix([[0, -1], [1, -1]])
    check("normal basis is P3-invariant with the displayed action",
          P3 * basis == basis * normal)
    check("normal action has order three", normal**3 == sp.eye(2))
    check("normal action has determinant one", normal.det() == 1)
    R1 = (sp.eye(2) - normal).inv()
    R2 = (sp.eye(2) - normal**2).inv()
    expected_R1 = sp.Rational(1, 3) * sp.Matrix([[2, -1], [1, 1]])
    expected_R2 = sp.Rational(1, 3) * sp.Matrix([[1, 1], [-1, 2]])
    check("first resolvent is exact", R1 == expected_R1, R1)
    check("second resolvent is exact", R2 == expected_R2, R2)
    check("the two resolvents sum to identity", R1 + R2 == sp.eye(2))
    B = sp.Rational(1, 3) * (R1 + R2)
    check("group-order-normalized nonidentity resolvent sum B equals I/3",
          B == sp.eye(2) / 3, B)
    print()

    print("Part B: fixed-locus density and trace coupling")
    d1 = (sp.eye(2) - normal).det()
    d2 = (sp.eye(2) - normal**2).det()
    h = sp.Rational(1, 3) * (1 / d1 + 1 / d2)
    check("both inverse-normal determinants have denominator three",
          d1 == 3 and d2 == 3, (d1, d2))
    check("fixed-locus density h equals 2/9", h == sp.Rational(2, 9), h)
    check("trace(B) equals 2/3", sp.trace(B) == sp.Rational(2, 3))
    check("trace(B) equals three times h", sp.trace(B) == 3 * h)
    check("B is unchanged under generator reversal",
          sp.Rational(1, 3) * (R2 + R1) == B)
    print()

    print("Part C: determinant holonomy and symmetric three-step root")
    beta = sp.symbols("beta", real=True)
    U_beta = sp.exp(sp.I * beta / 3) * sp.eye(2)
    check("exp(i beta B) reduces to a scalar unitary",
          (sp.I * beta * B).exp() == U_beta)
    check("det U_beta is exp(2 i beta/3)",
          sp.simplify(U_beta.det() - sp.exp(2 * sp.I * beta / 3)) == 0)
    U1 = U_beta.subs(beta, 1)
    edge = sp.exp(sp.I / 9) * sp.eye(2)
    check("symmetric edge root cubes to U1", sp.simplify(edge**3 - U1) == sp.zeros(2))
    check("cycle determinant phase is 2/3",
          sp.arg(U1.det()).equals(sp.Rational(2, 3)))
    check("edge determinant phase is h",
          sp.arg(edge.det()).equals(h))
    check("three edge phases add to the cycle phase", 3 * h == sp.Rational(2, 3))
    check("U1 is unitary", sp.simplify(U1.H * U1) == sp.eye(2))
    print()

    print("Part D: single sector, conjugate pair, and realification")
    K = U1
    A_K = sp.zeros(4)
    A_K[:2, 2:] = K
    A_K[2:, :2] = -K.T
    pf = pfaffian4(A_K)
    check("rank-two Pfaffian has the retained raw sign",
          sp.simplify(pf + K.det()) == 0)
    z_single = sp.simplify(K.det())
    z_pair = sp.simplify(z_single * sp.conjugate(z_single))
    check("single-sector determinant carries the cycle phase",
          sp.arg(z_single).equals(sp.Rational(2, 3)))
    check("independent conjugate-paired determinant equals one", z_pair == 1)
    check("ordinary realification determinant equals one",
          sp.simplify(realification(K).det()) == 1)
    check("conjugate pairing cancels the determinant phase",
          sp.arg(z_pair) == 0)
    check("complex conjugation reverses the single-sector phase",
          sp.simplify(sp.conjugate(z_single) - sp.exp(-2 * sp.I / 3)) == 0)
    print()

    print("Part E: determinant-character weights and remaining normalization")
    k = sp.symbols("k", integer=True)
    character = sp.exp(2 * sp.I * k * beta / 3)
    check("character formula at k=1,beta=1 gives cycle phase 2/3",
          sp.arg(character.subs({k: 1, beta: 1})).equals(sp.Rational(2, 3)))
    check("conjugate character k=-1 reverses orientation",
          sp.simplify(character.subs({k: -1, beta: 1})
                      - sp.exp(-2 * sp.I / 3)) == 0)
    check("paired net weight k+(-k) is phase-trivial",
          sp.simplify(character * character.subs(k, -k)) == 1)
    check("k=2 character has a nontrivial kernel witness z=-1",
          (-sp.Integer(1))**2 == 1 and -sp.Integer(1) != 1)
    z = sp.symbols("z", nonzero=True)
    check("k=1 is the identity and k=-1 inversion is bijective",
          sp.simplify(z**1 - z) == 0
          and sp.simplify(1 / (1 / z) - z) == 0)
    root_kernel_checks = []
    for weight in (-4, -3, -2, 2, 3, 4):
        root = sp.exp(2 * sp.pi * sp.I / abs(weight))
        root_kernel_checks.append(
            sp.simplify(root**weight - 1) == 0
            and sp.simplify(root - 1) != 0
        )
    check("sample nonfundamental characters have nontrivial root kernels",
          all(root_kernel_checks))
    edge_character = (sp.I * k * beta * B / 3).exp().det()
    check("edge determinant character is derived from exp(i k beta B/3)",
          sp.simplify(edge_character - sp.exp(2 * sp.I * k * beta / 9)) == 0)
    edge_lift = sp.Rational(2, 9) * k * beta
    check("edge lift at k=1,beta=1 equals h",
          edge_lift.subs({k: 1, beta: 1}) == h)
    check("beta=2 remains a distinct exact normalization",
          edge_lift.subs({k: 1, beta: 2}) == 2 * h)
    print()

    print("=" * 72)
    print(f"SCORECARD: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 72)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
