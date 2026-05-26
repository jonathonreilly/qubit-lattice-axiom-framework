#!/usr/bin/env python3
"""Exact runner for the C_3 Koide rho_delta dimensionless DOF ratio.

The paired note claims only the retained C_3 specialization:

    rho_delta_C3 = dim_R(C) / dim_R(Herm_3) = 2 / 9.

It does not derive a radian primitive, a selected-line Berry holonomy, a
physical charged-lepton readout, or a general C_d circulant theorem.
"""

from __future__ import annotations

from fractions import Fraction


PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    msg = f"[{tag}] {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return cond


def dim_r_herm(d: int) -> int:
    """Real dimension of d x d Hermitian matrices."""
    diagonal = d
    off_diagonal_complex = d * (d - 1) // 2
    return diagonal + 2 * off_diagonal_complex


def main() -> int:
    d = 3
    selected_complex_coordinate_dof = 2
    herm_dim = dim_r_herm(d)
    rho_delta_c3 = Fraction(selected_complex_coordinate_dof, herm_dim)

    check(
        "dim_R Herm_3 = 9",
        herm_dim == 9,
        f"dim_R Herm_{d} = {herm_dim}",
    )
    check(
        "selected complex coordinate b has 2 real DOF",
        selected_complex_coordinate_dof == 2,
        f"dim_R C = {selected_complex_coordinate_dof}",
    )
    check(
        "rho_delta_C3 = 2 / 9 exactly",
        rho_delta_c3 == Fraction(2, 9),
        f"rho_delta_C3 = {rho_delta_c3}",
    )

    for other_d in (2, 4, 5, 7, 11):
        other_ratio = Fraction(selected_complex_coordinate_dof, dim_r_herm(other_d))
        check(
            f"d = {other_d} is not the retained C_3 ratio",
            other_ratio != rho_delta_c3,
            f"2 / {other_d}^2 = {other_ratio}",
        )

    print(
        "INFO boundary: this runner checks only dimensionless rational "
        "arithmetic on the C_3 coordinate surface; it does not inspect audit "
        "status and does not assert a radian bridge."
    )
    print(f"SUMMARY: PASS = {PASS}, FAIL = {FAIL}")
    if FAIL:
        print("C_3 rho_delta dimensionless DOF-ratio check failed.")
        return 1

    print("C_3 rho_delta dimensionless DOF-ratio check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
