#!/usr/bin/env python3
"""Exact checks for the single-clock uniqueness scope boundary.

The narrow finite-dimensional Stone theorem says:
  given one positive Hermitian transfer T and a fixed positive time scale tau,
  H = -(1/tau) log(T) is unique and U(t)=exp(-itH) is unique for that H.

It does not by itself prove:
  * T determines the physical clock unit;
  * no other positive transfer / reflection axis exists;
  * no independent commuting one-parameter group exists on a tensor factor.

This runner verifies those scope boundaries exactly with sympy matrices.
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


def msimplify(M: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(M.rows, M.cols, lambda i, j: sp.simplify(M[i, j]))


def is_zero(M: sp.Matrix) -> bool:
    return all(sp.simplify(M[i, j]) == 0 for i in range(M.rows) for j in range(M.cols))


def diag_log_generator(T: sp.Matrix, tau: sp.Rational) -> sp.Matrix:
    return sp.diag(*[-sp.log(T[i, i]) / tau for i in range(T.rows)])


def exp_diag_neg_tau(H: sp.Matrix, tau: sp.Rational) -> sp.Matrix:
    return sp.diag(*[sp.exp(-tau * H[i, i]) for i in range(H.rows)])


def kron(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(A, B)


def comm(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    return msimplify(A * B - B * A)


def main() -> int:
    section("Fixed T and fixed tau give a unique Stone generator")
    tau1 = sp.Rational(1)
    T = sp.diag(sp.Rational(1, 2), sp.Rational(1, 3))
    H1 = diag_log_generator(T, tau1)
    check("S1 T is positive Hermitian with eigenvalues in (0,1]",
          T == T.T and all(0 < T[i, i] <= 1 for i in range(T.rows)),
          f"T={T}")
    check("S2 H=-(1/tau)log(T) reconstructs T for fixed tau",
          exp_diag_neg_tau(H1, tau1) == T, f"H={H1}")
    t, s = sp.symbols("t s", real=True)
    U_t = sp.diag(*[sp.exp(-sp.I * t * H1[i, i]) for i in range(H1.rows)])
    U_s = sp.diag(*[sp.exp(-sp.I * s * H1[i, i]) for i in range(H1.rows)])
    U_st = sp.diag(*[sp.exp(-sp.I * (s + t) * H1[i, i]) for i in range(H1.rows)])
    check("S3 U(t) is unitary", msimplify(U_t.conjugate().T * U_t) == sp.eye(2))
    check("S4 U(s)U(t)=U(s+t)", is_zero(msimplify(U_s * U_t - U_st)))
    check("S5 generator identity dU/dt|0=-iH holds",
          msimplify(sp.diff(U_t, t).subs(t, 0) + sp.I * H1) == sp.zeros(2))

    section("The time scale tau is not determined by T alone")
    tau2 = sp.Rational(2)
    H2 = diag_log_generator(T, tau2)
    check("N1 same T is reconstructed by tau=2 with H rescaled",
          exp_diag_neg_tau(H2, tau2) == T, f"H_tau1={H1}, H_tau2={H2}")
    check("N2 H_tau2 is not equal to H_tau1",
          H2 != H1)
    check("N3 H_tau2 equals H_tau1/2 exactly",
          msimplify(H2 - H1 / 2) == sp.zeros(2))
    check("N4 Stone uniqueness is therefore relative to fixed tau",
          True,
          "T fixes tau*H, not the physical clock unit by itself")

    section("Multiple supplied transfers give multiple commuting one-parameter groups")
    T_A = sp.diag(sp.Rational(1, 2), sp.Rational(1, 3))
    T_B = sp.diag(sp.Rational(1, 5), sp.Rational(1, 7))
    H_A = diag_log_generator(T_A, tau1)
    H_B = diag_log_generator(T_B, tau1)
    I2 = sp.eye(2)
    H_A_lift = kron(H_A, I2)
    H_B_lift = kron(I2, H_B)
    T_A_lift = kron(T_A, I2)
    T_B_lift = kron(I2, T_B)
    check("M1 lifted transfers are positive Hermitian",
          T_A_lift == T_A_lift.T and T_B_lift == T_B_lift.T
          and all(T_A_lift[i, i] > 0 for i in range(4))
          and all(T_B_lift[i, i] > 0 for i in range(4)))
    check("M2 lifted generators commute",
          is_zero(comm(H_A_lift, H_B_lift)))
    check("M3 lifted transfers commute",
          is_zero(comm(T_A_lift, T_B_lift)))
    u, v = sp.symbols("u v", real=True)
    U_A = sp.diag(*[sp.exp(-sp.I * u * H_A_lift[i, i]) for i in range(4)])
    U_B = sp.diag(*[sp.exp(-sp.I * v * H_B_lift[i, i]) for i in range(4)])
    check("M4 two supplied commuting groups are distinct",
          U_A != U_B and H_A_lift != H_B_lift)
    check("M5 the product transfer has the summed generator for a chosen common tau",
          exp_diag_neg_tau(H_A_lift + H_B_lift, tau1) == T_A_lift * T_B_lift)
    check("M6 Stone theorem for the product transfer does not erase the factor groups",
          is_zero(comm(H_A_lift, H_A_lift + H_B_lift))
          and is_zero(comm(H_B_lift, H_A_lift + H_B_lift)))

    section("No-second-clock wording needs extra premises")
    check("B1 fixed T,tau gives uniqueness of H only for that transfer",
          exp_diag_neg_tau(H1, tau1) == T)
    check("B2 T alone leaves clock-unit normalization open",
          H2 != H1)
    check("B3 finite Stone theorem permits multiple supplied commuting transfers",
          is_zero(comm(T_A_lift, T_B_lift)) and T_A_lift != T_B_lift)
    check("B4 excluding a second clock requires a separate axis/transfer uniqueness premise",
          True,
          "e.g. unique reflection-positive axis or no independent positive transfer")

    section("Scorecard")
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "FINDING: finite-dimensional Stone uniqueness is relative to a supplied "
        "positive transfer T and fixed time scale tau. It does not by itself "
        "fix tau, exclude other supplied positive transfers, or prove a broad "
        "framework-wide one-clock exclusion theorem."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
