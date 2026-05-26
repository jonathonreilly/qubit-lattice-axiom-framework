"""Narrow bridge runner: rho_delta = 2 / d^2 from retained circulant DOF counts.

Verifies the bounded bridge in
docs/KOIDE_RHO_DELTA_DIMENSIONLESS_DOF_RATIO_BRIDGE_BOUNDED_NOTE_2026-05-25.md
by exact rational arithmetic on integer dimensions only (no lattice
action, no Monte Carlo, no fitted observational value, no radian
reading).
"""

from fractions import Fraction


def dim_R_Herm_d(d: int) -> int:
    """Real dimension of d x d Hermitian matrices.

    Real diagonal entries: d.
    Complex off-diagonal entries: d * (d - 1) / 2, each carrying 2 real DOF.
    Total real DOF: d + d * (d - 1) = d^2.
    """
    return d + d * (d - 1)


def dim_R_C() -> int:
    """Real dimension of the complex line (the circulant phase parameter b)."""
    return 2


def rho_delta(d: int) -> Fraction:
    """The dimensionless ratio rho_delta = dim_R(C) / dim_R(Herm_d) = 2 / d^2."""
    return Fraction(dim_R_C(), dim_R_Herm_d(d))


def main() -> int:
    PASS = 0
    FAIL = 0

    # ---- Step (B3) consistency: dim_R Herm_d == d^2 ----
    for d in [2, 3, 4, 5, 7, 11]:
        observed = dim_R_Herm_d(d)
        expected = d * d
        if observed == expected:
            PASS += 1
        else:
            print(f"FAIL (B3, d={d}): dim_R Herm_d = {observed}, expected {expected}")
            FAIL += 1
    if FAIL == 0:
        print("PASS (B3): dim_R Herm_d = d^2 for d in {2, 3, 4, 5, 7, 11}.")

    # ---- Step (B4) main identity: rho_delta = 2 / d^2 ----
    for d in [2, 3, 4, 5, 7, 11]:
        observed = rho_delta(d)
        expected = Fraction(2, d * d)
        if observed != expected:
            print(f"FAIL (B4, d={d}): rho_delta = {observed}, expected {expected}")
            FAIL += 1

    # ---- Step (B5) main physics value at d = 3: rho_delta = 2 / 9 ----
    rho_at_3 = rho_delta(3)
    if rho_at_3 == Fraction(2, 9):
        print("PASS (B4, B5): rho_delta = 2 / d^2 for d in {2, 3, 4, 5, 7, 11}; "
              "at d=3, rho_delta = 2/9.")
        PASS += 1
    else:
        print(f"FAIL (B5): rho_delta at d=3 = {rho_at_3}, expected 2/9")
        FAIL += 1

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded bridge passes; rho_delta = 2 / d^2 is exact "
            "rational arithmetic on the retained circulant Hermitian DOF "
            "count for all tested d in {2, 3, 4, 5, 7, 11}."
        )
        return 0
    print("VERDICT: bounded bridge FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
