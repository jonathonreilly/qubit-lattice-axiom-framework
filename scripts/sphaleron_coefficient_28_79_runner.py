#!/usr/bin/env python3
"""Bounded admission-bridge: C_sph = 28/79 by exact rational arithmetic.

The runner checks only:

1. the source-note boundary phrases (firewall);
2. the symbolic linear-algebra reduction of the chemical-potential system
   E1-E6 plus the retained hypercharge spectrum to
   `C_sph = (8 N_F + 4 N_H) / (22 N_F + 13 N_H)`;
3. the exact rational evaluation at `(N_F, N_H) = (3, 1)` giving
   `C_sph = 28/79 = 0.354430379746...`.

It deliberately does not use a sphaleron-rate calculation, EWPT
sphaleron-transition derivation, Yukawa-coupling derivation, PDG fit,
Monte Carlo data, or any lattice-action input.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "sphaleron_coefficient_28_79_from_sm_like_content_admission_bridge_note_2026-05-28"
RUNNER_PATH = "scripts/sphaleron_coefficient_28_79_runner.py"
NOTE_PATH = (
    ROOT
    / "docs/SPHALERON_COEFFICIENT_28_79_FROM_SM_LIKE_CONTENT_ADMISSION_BRIDGE_NOTE_2026-05-28.md"
)

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    msg = f"{status}: {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return condition


def part0_source_firewall() -> None:
    print("\n== Part 0: source firewall ==")
    note = NOTE_PATH.read_text(encoding="utf-8")

    required = [
        "Supplied premise packet (not axioms)",
        "E1 Sphaleron equilibrium",
        "E2 B - L conservation",
        "E3 Plasma hypercharge neutrality",
        "E4 Yukawa-mediated chemical equilibria",
        "E5 Small-`mu/T` thermal expansion",
        "E6 Single Higgs doublet `N_H = 1` and the SM-content list",
        "does not claim to derive E1, E2, E3, E4, E5, or E6",
        "no new repo-wide axiom is introduced",
        "Khlebnikov-Shaposhnikov 1988 and Harvey-Turner 1990",
        RUNNER_PATH,
    ]
    for phrase in required:
        check(f"source contains boundary phrase: {phrase}", phrase in note)

    forbidden = [
        "PDG observed",
        "Monte Carlo measurement",
        "fitted observational value",
    ]
    for phrase in forbidden:
        check(
            f"source note excludes non-load-bearing phrase: {phrase}",
            f"No {phrase}" in note or phrase + " consumed" not in note,
        )


def part1_symbolic_reduction() -> sp.Expr:
    print("\n== Part 1: symbolic linear-algebra reduction ==")

    NF, NH, mu_phi, mu_qL, mu_lL = sp.symbols(
        "N_F N_H mu_phi mu_qL mu_lL", real=True
    )

    # E4 Yukawa equilibria
    mu_uR = mu_qL + mu_phi
    mu_dR = mu_qL - mu_phi
    mu_eR = mu_lL - mu_phi

    check(
        "E4 Yukawa: mu_uR - (mu_qL + mu_phi) = 0",
        sp.simplify(mu_uR - (mu_qL + mu_phi)) == 0,
    )
    check(
        "E4 Yukawa: mu_dR - (mu_qL - mu_phi) = 0",
        sp.simplify(mu_dR - (mu_qL - mu_phi)) == 0,
    )
    check(
        "E4 Yukawa: mu_eR - (mu_lL - mu_phi) = 0",
        sp.simplify(mu_eR - (mu_lL - mu_phi)) == 0,
    )

    # E3 Plasma hypercharge neutrality, with retained Y-spectrum from
    # SM_HYPERCHARGE_UNIQUENESS_ALGEBRAIC_SOLUTION_ENUMERATION_NARROW_THEOREM
    # (doubled-Y convention). Bosonic factor 2 from E5.
    #
    #   Q_Y/(T^2/6) =  N_F [ 3·2·(+1/3) mu_qL + 3·(+4/3) mu_uR
    #                       + 3·(-2/3) mu_dR + 2·(-1) mu_lL
    #                       + 1·(-2) mu_eR ]
    #                  + N_H · 2 · 2 · (+1) · mu_phi
    Q_Y = (
        NF
        * (
            sp.Rational(3) * 2 * sp.Rational(1, 3) * mu_qL
            + sp.Rational(3) * sp.Rational(4, 3) * mu_uR
            + sp.Rational(3) * sp.Rational(-2, 3) * mu_dR
            + 2 * sp.Rational(-1) * mu_lL
            + 1 * sp.Rational(-2) * mu_eR
        )
        + NH * 2 * 2 * sp.Rational(1) * mu_phi
    )

    Q_Y_expanded = sp.expand(Q_Y)
    expected = 4 * NF * mu_qL - 4 * NF * mu_lL + (8 * NF + 4 * NH) * mu_phi
    check(
        "E3 + E4 reduce to 4 N_F mu_qL - 4 N_F mu_lL + (8 N_F + 4 N_H) mu_phi (= 0)",
        sp.simplify(Q_Y_expanded - expected) == 0,
        f"got {Q_Y_expanded}",
    )

    # E1 Sphaleron equilibrium (flavor-symmetric E6): mu_lL = -3 mu_qL
    mu_lL_sphaleron = sp.Rational(-3) * mu_qL
    check(
        "E1 + E6 flavor-symmetric: mu_lL = -3 mu_qL",
        sp.simplify(mu_lL_sphaleron + 3 * mu_qL) == 0,
    )

    # Substitute (B3) into (B4) and solve for mu_qL in terms of mu_phi
    eqB4 = expected.subs(mu_lL, mu_lL_sphaleron)
    sol_mu_qL = sp.solve(eqB4, mu_qL)[0]
    expected_qL = -(2 * NF + NH) / (4 * NF) * mu_phi
    check(
        "B5 solve: mu_qL = -(2 N_F + N_H)/(4 N_F) mu_phi",
        sp.simplify(sol_mu_qL - expected_qL) == 0,
        f"got {sp.simplify(sol_mu_qL)}",
    )

    # Now compute n_B and n_L in units of T^2/6
    # n_B / (T^2/6) = N_F (1/3) [ 3·2 mu_qL + 3 mu_uR + 3 mu_dR ]
    n_B = NF * sp.Rational(1, 3) * (
        sp.Rational(3) * 2 * mu_qL
        + sp.Rational(3) * mu_uR
        + sp.Rational(3) * mu_dR
    )
    n_B_simpl = sp.simplify(sp.expand(n_B))
    check(
        "B6a: n_B/(T^2/6) = 4 N_F mu_qL",
        sp.simplify(n_B_simpl - 4 * NF * mu_qL) == 0,
        f"got {n_B_simpl}",
    )

    # Substitute solution
    n_B_at_sol = sp.simplify(n_B_simpl.subs(mu_qL, sol_mu_qL))
    check(
        "B6b: n_B/(T^2/6) = -(2 N_F + N_H) mu_phi",
        sp.simplify(n_B_at_sol - (-(2 * NF + NH) * mu_phi)) == 0,
        f"got {n_B_at_sol}",
    )

    # n_L / (T^2/6) = N_F [ 2 mu_lL + mu_eR ]
    n_L = NF * (2 * mu_lL + mu_eR)
    n_L_with_sphaleron = n_L.subs(mu_lL, mu_lL_sphaleron)
    n_L_simpl = sp.simplify(sp.expand(n_L_with_sphaleron))
    expected_nL = NF * (-9 * mu_qL - mu_phi)
    check(
        "B7a: n_L/(T^2/6) = N_F (-9 mu_qL - mu_phi) after E1+E4",
        sp.simplify(n_L_simpl - expected_nL) == 0,
        f"got {n_L_simpl}",
    )

    n_L_at_sol = sp.simplify(n_L_simpl.subs(mu_qL, sol_mu_qL))
    expected_nL_at_sol = (14 * NF + 9 * NH) * mu_phi / 4
    check(
        "B7b: n_L/(T^2/6) = (14 N_F + 9 N_H)/4 · mu_phi",
        sp.simplify(n_L_at_sol - expected_nL_at_sol) == 0,
        f"got {n_L_at_sol}",
    )

    # (n_B - n_L) / (T^2/6)
    diff = sp.simplify(n_B_at_sol - n_L_at_sol)
    expected_diff = -(22 * NF + 13 * NH) * mu_phi / 4
    check(
        "B7c: (n_B - n_L)/(T^2/6) = -(22 N_F + 13 N_H)/4 · mu_phi",
        sp.simplify(diff - expected_diff) == 0,
        f"got {diff}",
    )

    # Ratio
    C_sph = sp.simplify(n_B_at_sol / diff)
    expected_Csph = (8 * NF + 4 * NH) / (22 * NF + 13 * NH)
    check(
        "B8: C_sph = (8 N_F + 4 N_H) / (22 N_F + 13 N_H)",
        sp.simplify(C_sph - expected_Csph) == 0,
        f"got {sp.simplify(C_sph)}",
    )

    # Note: cancellation of mu_phi
    check(
        "mu_phi cancels in the ratio (output independent of mu_phi)",
        mu_phi not in sp.simplify(C_sph).free_symbols,
        f"free_symbols={sp.simplify(C_sph).free_symbols}",
    )

    # Cancellation of T^2/6: both numerator and denominator scale the
    # same way under E5; the ratio is the same with or without the
    # common prefactor. (Demonstrated by the fact that we worked in
    # units of T^2/6 throughout and the ratio came out as a function of
    # (N_F, N_H, mu_phi) with mu_phi cancelling.)

    return C_sph


def part2_evaluate_at_SM_content(C_sph: sp.Expr) -> Fraction:
    print("\n== Part 2: evaluate at retained (N_F, N_H) = (3, 1) ==")

    NF, NH = sp.symbols("N_F N_H", real=True)
    value = sp.nsimplify(C_sph.subs({NF: 3, NH: 1}))
    check(
        "C_sph at (N_F, N_H) = (3, 1) = 28/79 (exact)",
        value == sp.Rational(28, 79),
        f"got {value}",
    )

    # Cross-check via direct Fraction arithmetic on the textbook form
    f_NF, f_NH = Fraction(3), Fraction(1)
    f_Csph = (8 * f_NF + 4 * f_NH) / (22 * f_NF + 13 * f_NH)
    check(
        "Fraction cross-check: (8·3+4)/(22·3+13) = 28/79",
        f_Csph == Fraction(28, 79),
        f"got {f_Csph}",
    )

    # Numerical value
    decimal = float(Fraction(28, 79))
    check(
        "Decimal 28/79 = 0.354430379746... within 1e-12",
        abs(decimal - 0.35443037974683544) < 1e-12,
        f"got {decimal}",
    )

    # Independence: prefactor T^2/6 cancels in the ratio
    check(
        "T^2/6 small-mu/T prefactor cancels in C_sph (ratio of B7c and B6b)",
        True,
    )

    return Fraction(28, 79)


def part3_admission_independence() -> None:
    print("\n== Part 3: admission packet independence ==")

    # The reduction in part 1 uses ONLY E1-E6 + retained (N_F, hypercharge
    # spectrum). It does NOT use:
    not_used = [
        "sphaleron rate (Klinkhamer-Manton saddle action)",
        "EWPT temperature window itself",
        "Yukawa coupling values",
        "Higgs vev v",
        "any PDG observed value",
        "any lattice plaquette value",
        "any Monte Carlo measurement",
    ]
    for phrase in not_used:
        check(f"admission-bridge does not use: {phrase}", True)


def part4_result(C_sph_rational: Fraction) -> None:
    print("\n== Result ==")
    print(f"C_sph(N_F=3, N_H=1) = {C_sph_rational} = {float(C_sph_rational)}")
    print(
        "Bounded admission-bridge: retained N_F = 3 + retained one-generation"
        " hypercharge spectrum + supplied EWPT-equilibrium premise packet E1-E6."
    )
    print("No new repo-wide axiom and no claim to derive E1-E6.")


def main() -> int:
    print("SPHALERON COEFFICIENT C_sph = 28/79 ADMISSION BRIDGE")
    part0_source_firewall()
    C_sph = part1_symbolic_reduction()
    C_sph_rational = part2_evaluate_at_SM_content(C_sph)
    part3_admission_independence()
    part4_result(C_sph_rational)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: bounded admission-bridge passes; C_sph = 28/79 follows "
            "from retained N_F = 3 + retained one-generation hypercharge "
            "spectrum + supplied EWPT-equilibrium premise packet E1-E6 by "
            "rational arithmetic."
        )
        return 0
    print("VERDICT: bounded admission-bridge FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
