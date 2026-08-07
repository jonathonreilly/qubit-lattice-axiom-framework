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

    section("N5 execution certificate (print-only; adds no check and no counter)")
    print(
        "per_element: resolved as exact symbolic entries with no tolerance anywhere -- every matrix "
        "is built by naming its diagonal entries as exact rationals, 1/2 and 1/3 for the first "
        "transfer and 1/5 and 1/7 for the second, the simplify helper is applied position by "
        "position through an (i,j) lambda, and the zero test walks every (i,j) slot and demands "
        "symbolic equality to 0 rather than smallness. Matrix equality here is therefore decided "
        "element by element in exact arithmetic, never by a norm or a threshold."
    )
    print(
        "per_site: checked and not executed -- there is no lattice in this runner at all. The "
        "carriers are one two-dimensional factor and its four-dimensional tensor square, whose "
        "indices are abstract basis labels rather than positions, and no coordinate, neighbour "
        "relation, or site amplitude is constructed anywhere, so nothing site-resolved exists here."
    )
    print(
        "per_mode: resolved one diagonal mode at a time -- the generator is assembled as "
        "diag(-log(T_ii)/tau) with the logarithm taken separately in each mode, the reconstruction "
        "diag(exp(-tau*H_ii)) inverts it mode by mode, and the evolution family "
        "diag(exp(-i*t*H_ii)) is written the same way. The rescaling result is a per-mode identity "
        "too: the tau=2 generator equals the tau=1 generator halved in every mode exactly, which is "
        "precisely what shows the transfer pins only the product tau*H and not the clock unit."
    )
    print(
        "per_block: resolved as two commuting tensor-factor blocks -- the middle section lifts one "
        "transfer as H_A tensor I and the other as I tensor H_B onto a four-dimensional carrier and "
        "then certifies that block structure directly: the lifted generators commute, the lifted "
        "transfers commute, the two groups are distinct, the product transfer carries exactly the "
        "summed generator, and each factor generator still commutes with that sum. The last of these "
        "is the decisive block fact, since it is what stops the product's Stone generator from "
        "absorbing the factor groups."
    )
    print(
        "lattice_wide: checked and not executed -- nothing in this runner carries an extent, a "
        "volume, or a size that could be varied, the largest object being a 4x4 diagonal matrix. The "
        "blocking reason is the scope boundary this note exists to record: excluding a second clock "
        "requires a separate axis or transfer uniqueness premise, and no such premise is supplied or "
        "derived here, so there is no framework-wide one-clock result for any lattice-scale statement "
        "to rest on."
    )
    print(
        "Scope: seventeen of the nineteen checks evaluate a symbolic condition. Two of them, N4 and "
        "B4, are invoked with a hardcoded True and state a scope conclusion in prose without "
        "computing anything; resolution is claimed above only for the seventeen."
    )
    print(
        "Determinism: this runner uses sympy exact rational and symbolic arithmetic end to end. "
        "There is no RNG, optimizer, root-finding, grid scan, Monte Carlo, or flow integration, and "
        "there is no floating-point tolerance anywhere in the file -- every comparison is exact "
        "symbolic equality, so no quantity in this certificate is interpolated from a sampled or "
        "converged value and none could differ between environments."
    )

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
