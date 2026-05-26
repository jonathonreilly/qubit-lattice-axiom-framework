"""Narrow bridge runner: alpha = 1/3 from retained ratio + admitted GMN
+ admitted Q(electron) = -1.

This script verifies the bounded bridge in
docs/HYPERCHARGE_ALPHA_THIRD_NORMALIZATION_BRIDGE_BOUNDED_NOTE_2026-05-25.md
by exact rational arithmetic only (no lattice action, no Monte Carlo,
no fitted observational value).
"""

from fractions import Fraction


def main() -> int:
    PASS = 0
    FAIL = 0

    # ---- Admitted inputs ----
    # Admitted: Gell-Mann-Nishijima relation Q = T_3 + Y/2 (SM convention).
    # Admitted: weak-isospin assignment T_3(e_L) = -1/2.
    # Admitted: empirical Q(electron) = -1 (electron-charge unit).
    T3_eL = Fraction(-1, 2)
    Q_eL_admitted = Fraction(-1, 1)

    # ---- Retained input ----
    # Retained: eigenvalue ratio +1 : (-3) on (Sym^2, Anti^2) sub-blocks
    # implies Y(L_L) = -3 * alpha and Y(Q_L) = +alpha for the one-parameter
    # traceless U(1) generator family Y_alpha = alpha (P_sym - 3 P_anti).
    # The ratio is the load-bearing input from
    # LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md.

    # ---- (B5)/(B6) solve for alpha ----
    # Q(e_L) = T_3(e_L) + Y(L_L)/2
    #        = T_3(e_L) + (-3 alpha)/2
    # -1 = -1/2 + (-3 alpha)/2  =>  alpha = 1/3.
    alpha_rhs = (Q_eL_admitted - T3_eL) * Fraction(-2, 3)
    alpha = alpha_rhs
    if alpha == Fraction(1, 3):
        print(
            "PASS (B6): alpha = 1/3 follows from "
            "Q(e_L) = -1, T_3(e_L) = -1/2, Y(L_L) = -3 alpha."
        )
        PASS += 1
    else:
        print(f"FAIL (B6): expected alpha = 1/3, got alpha = {alpha}")
        FAIL += 1

    # ---- Independent consistency check: Y(L_L) at alpha = 1/3 ----
    Y_LL = -3 * alpha
    if Y_LL == Fraction(-1, 1):
        print("PASS (L_L sub-block): Y(L_L) = -1 at alpha = 1/3.")
        PASS += 1
    else:
        print(f"FAIL (L_L sub-block): expected Y(L_L) = -1, got {Y_LL}")
        FAIL += 1

    # ---- Independent consistency check on (2, 3) sub-block ----
    # Y(Q_L) = +alpha; Q(u_L) = T_3(u_L) + Y(Q_L)/2 with T_3(u_L) = +1/2.
    Y_QL = alpha
    T3_uL = Fraction(1, 2)
    Q_uL = T3_uL + Y_QL / 2
    if Q_uL == Fraction(2, 3):
        print("PASS (u_L cross-check): Q(u_L) = +2/3 at alpha = 1/3.")
        PASS += 1
    else:
        print(f"FAIL (u_L cross-check): expected Q(u_L) = +2/3, got {Q_uL}")
        FAIL += 1

    # ---- Independent consistency check: Q(d_L) ----
    T3_dL = Fraction(-1, 2)
    Q_dL = T3_dL + Y_QL / 2
    if Q_dL == Fraction(-1, 3):
        print("PASS (d_L cross-check): Q(d_L) = -1/3 at alpha = 1/3.")
        PASS += 1
    else:
        print(f"FAIL (d_L cross-check): expected Q(d_L) = -1/3, got {Q_dL}")
        FAIL += 1

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded bridge passes; alpha = 1/3 follows from "
            "retained ratio + admitted GMN + admitted Q(electron) = -1 "
            "by rational arithmetic."
        )
        return 0
    print("VERDICT: bounded bridge FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
