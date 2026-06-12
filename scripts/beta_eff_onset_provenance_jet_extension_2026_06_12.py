#!/usr/bin/env python3
"""Exact jet composition for the beta_eff onset provenance follow-up.

The exact checks use only Fraction-declared inputs and sympy Rational algebra.
The final numeric response-spread diagnostic reuses the existing SU(3)
one-plaquette Bessel evaluator from the bridge no-go runner.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from frontier_gauge_vacuum_plaquette_bridge_support import plaquette_from_bessel  # noqa: E402


BETA = sp.Symbol("beta")
ORDER = 11
C_SCALE = Fraction(1, 10_000_000)
PASS_COUNT = 0
FAIL_COUNT = 0


DELTA_FRACTIONS: dict[int, Fraction] = {
    5: Fraction(1, 472392),
    6: Fraction(7, 5668704),
    7: Fraction(5, 17006112),
    8: Fraction(5, 272097792),
    9: Fraction(-2035, 264479053824),
    10: Fraction(-10483, 5289581076480),
    11: Fraction(-13, 3967185807360),
}

EXPECTED_BETA_EFF: dict[int, Fraction] = {
    5: Fraction(1, 26244),
    6: Fraction(5, 314928),
    7: Fraction(5, 1889568),
    8: Fraction(5, 136048896),
    9: Fraction(-955, 14693280768),
    10: Fraction(-4207, 528958107648),
    11: Fraction(5579, 3173748645888),
}

COEFFICIENT_SOURCE_FILES: dict[int, str] = {
    6: "BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md",
    7: "BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md",
    8: "BETA6_PLAQUETTE_D8_COEFFICIENT_AND_SINGLE_PAIR_VERDICT_BOUNDED_NOTE_2026-05-30.md",
    9: "BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md",
    10: "BETA6_PLAQUETTE_D10_COEFFICIENT_AND_RADIUS_EVIDENCE_BOUNDED_NOTE_2026-06-04.md",
    11: "BETA6_PLAQUETTE_D11_COEFFICIENT_AND_CONTINUATION_SPREAD_BOUNDED_NOTE_2026-06-04.md",
}


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"PASS: {name}")
    else:
        FAIL_COUNT += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def rational_from_fraction(value: Fraction) -> sp.Rational:
    return sp.Rational(value.numerator, value.denominator)


def has_no_float_atoms(expr: sp.Expr) -> bool:
    return not bool(expr.atoms(sp.Float))


def bessel_i_series(index: int, max_order: int) -> sp.Expr:
    """Truncated exact series for I_index(beta/3)."""
    n = abs(index)
    total = sp.Rational(0)
    for r in range((max_order - n) // 2 + 1):
        power = 2 * r + n
        denom = (2**power) * (3**power) * sp.factorial(r) * sp.factorial(r + n)
        total += sp.Rational(1, denom) * BETA**power
    return total


def su3_partition_jet(max_order: int, mode_bound: int) -> sp.Expr:
    total = sp.Rational(0)
    for mode in range(-mode_bound, mode_bound + 1):
        matrix = sp.Matrix(
            [
                [bessel_i_series(mode + i - j, max_order) for j in range(3)]
                for i in range(3)
            ]
        )
        total += sp.series(matrix.det(), BETA, 0, max_order + 1).removeO()
    return sp.series(total, BETA, 0, max_order + 1).removeO().expand()


def local_response_jet(max_order: int, mode_bound: int) -> sp.Expr:
    partition = su3_partition_jet(max_order + 1, mode_bound)
    response = sp.diff(partition, BETA) / partition
    return sp.series(response, BETA, 0, max_order + 1).removeO().expand()


def solve_beta_eff_coefficients(response_jet: sp.Expr, delta_jet: sp.Expr) -> dict[int, sp.Rational]:
    unknowns = {n: sp.Symbol(f"a{n}") for n in range(5, ORDER + 1)}
    beta_eff = BETA + sum(unknowns[n] * BETA**n for n in range(5, ORDER + 1))
    residual = sp.series(
        response_jet.subs(BETA, beta_eff) - response_jet - delta_jet,
        BETA,
        0,
        ORDER + 1,
    ).removeO().expand()

    solution: dict[int, sp.Rational] = {}
    substitutions: dict[sp.Symbol, sp.Rational] = {}
    for n in range(5, ORDER + 1):
        coefficient = sp.expand(residual.subs(substitutions)).coeff(BETA, n)
        solved = sp.solve(sp.Eq(coefficient, 0), unknowns[n])
        if len(solved) != 1:
            raise RuntimeError(f"could not solve coefficient a{n}: {coefficient}")
        value = sp.Rational(solved[0])
        solution[n] = value
        substitutions[unknowns[n]] = value
    return solution


def beta_eff_polynomial(coefficients: dict[int, sp.Rational]) -> sp.Expr:
    return BETA + sum(coefficients[n] * BETA**n for n in range(5, ORDER + 1))


def fmt_rational_dict(values: dict[int, sp.Rational]) -> str:
    return ", ".join(f"a{n}={values[n]}" for n in sorted(values))


def main() -> int:
    source_note = ROOT / "docs" / "GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md"
    no_go_note = ROOT / "docs" / "GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md"
    source_text = source_note.read_text(encoding="utf-8")
    no_go_text = no_go_note.read_text(encoding="utf-8")

    response_jet = local_response_jet(ORDER, mode_bound=20)
    response_jet_wide = local_response_jet(ORDER, mode_bound=24)
    delta_jet = sum(
        rational_from_fraction(value) * BETA**n
        for n, value in DELTA_FRACTIONS.items()
    )
    beta_eff_coeffs = solve_beta_eff_coefficients(response_jet, delta_jet)
    beta_eff = beta_eff_polynomial(beta_eff_coeffs)
    residual = sp.series(
        response_jet.subs(BETA, beta_eff) - response_jet - delta_jet,
        BETA,
        0,
        ORDER + 1,
    ).removeO().expand()

    expected = {
        n: rational_from_fraction(value)
        for n, value in EXPECTED_BETA_EFF.items()
    }
    beta6_minus = sp.simplify(beta_eff.subs(BETA, 6))
    beta6_gap_new = rational_from_fraction(C_SCALE) * sp.Integer(6) ** 12
    beta6_plus = sp.simplify(beta6_minus + beta6_gap_new)
    beta6_gap_old = rational_from_fraction(C_SCALE) * sp.Integer(6) ** 6

    old_minus = sp.Integer(6) + expected[5] * sp.Integer(6) ** 5
    old_plus = old_minus + beta6_gap_old

    response_old_minus = plaquette_from_bessel(float(old_minus))[0]
    response_old_plus = plaquette_from_bessel(float(old_plus))[0]
    response_new_minus = plaquette_from_bessel(float(beta6_minus))[0]
    response_new_plus = plaquette_from_bessel(float(beta6_plus))[0]

    print("BETA_EFF ONSET PROVENANCE AND JET EXTENSION")
    print(f"R_O jet through beta^{ORDER}: {response_jet}")
    print(f"Delta jet d5..d11: {delta_jet}")
    print(f"beta_eff jet coefficients: {fmt_rational_dict(beta_eff_coeffs)}")
    print(f"beta_eff^-(6): {beta6_minus}")
    print(f"beta_eff^+(6) - beta_eff^-(6): {beta6_gap_new}")
    print(f"beta_eff^+(6): {beta6_plus}")
    print("Numeric R_O spread diagnostic using existing Bessel evaluator:")
    print(f"  original order-6 gap beta_eff: {beta6_gap_old}")
    print(f"  refreshed order-12 gap beta_eff: {beta6_gap_new}")
    print(f"  exact beta_eff gap ratio: {sp.simplify(beta6_gap_new / beta6_gap_old)}")
    print(f"  original R_O gap: {response_old_plus - response_old_minus:.15e}")
    print(f"  refreshed R_O gap: {response_new_plus - response_new_minus:.15e}")
    print()

    check(
        "source note contains the formal reduction-law derivation lines",
        "P_full(beta) = P_1plaq(beta_eff(beta))" in source_text
        and "P_1plaq'(0) = 1 / 18" in source_text
        and "beta_eff(beta) = beta + (1 / 26244) beta^5 + O(beta^6)" in source_text,
        "case (a) provenance: beta_eff onset is obtained by local-response composition",
    )
    check(
        "no-go note names inverse-response definition as the forbidden finite-beta route",
        "beta_eff = R_O^{-1}(<P>_full)" in no_go_text
        and "If `beta_eff` is defined by this inverse equation" in no_go_text,
        "the present runner performs only finite jet composition from declared series inputs",
    )
    check(
        "Delta coefficients d5 through d11 are exact Fraction-declared inputs",
        all(isinstance(value, Fraction) for value in DELTA_FRACTIONS.values()),
        ", ".join(f"d{n}={v}" for n, v in sorted(DELTA_FRACTIONS.items())),
    )
    source_fraction_hits = []
    for n, file_name in sorted(COEFFICIENT_SOURCE_FILES.items()):
        source = (ROOT / "docs" / file_name).read_text(encoding="utf-8")
        compact_source = source.replace(" ", "").replace("\n", "")
        fraction = DELTA_FRACTIONS[n]
        marker = f"d_{n}={fraction.numerator}/{fraction.denominator}"
        source_fraction_hits.append(marker in compact_source)
    check(
        "linked coefficient source notes contain the consumed d6 through d11 fractions",
        all(source_fraction_hits),
        ", ".join(f"d{n} from {file_name}" for n, file_name in sorted(COEFFICIENT_SOURCE_FILES.items())),
    )
    check(
        "local one-plaquette response jet is stable under a wider mode cutoff",
        response_jet == response_jet_wide,
        "mode_bound 20 equals mode_bound 24 through beta^11",
    )
    check(
        "local response slope is exactly 1/18",
        response_jet.coeff(BETA, 1) == sp.Rational(1, 18),
        f"slope={response_jet.coeff(BETA, 1)}",
    )
    check(
        "all exact jet expressions contain no sympy Float atoms",
        has_no_float_atoms(response_jet)
        and has_no_float_atoms(delta_jet)
        and all(has_no_float_atoms(value) for value in beta_eff_coeffs.values()),
        "R_O jet, Delta jet, and beta_eff coefficients are Rational-only",
    )
    check(
        "beta_eff coefficients match the exact triangular inversion result",
        beta_eff_coeffs == expected,
        fmt_rational_dict(beta_eff_coeffs),
    )
    check(
        "composition residual R_O(beta_eff(beta))-R_O(beta)-Delta(beta) vanishes through beta^11",
        residual == 0,
        f"residual={residual}",
    )
    check(
        "onset coefficient reproduces 1/26244",
        beta_eff_coeffs[5] == sp.Rational(1, 26244),
        f"a5={beta_eff_coeffs[5]}",
    )
    check(
        "refreshed minimal witnesses first differ at beta^12 for the c-scale analog",
        beta6_gap_new == sp.Rational(17006112, 78125)
        and beta6_gap_new / beta6_gap_old == sp.Integer(46656),
        f"new_gap={beta6_gap_new}, old_gap={beta6_gap_old}",
    )
    check(
        "framework-point beta_eff polynomial value is exact",
        beta6_minus == sp.Rational(32111, 4374)
        and beta6_plus == sp.Rational(76893405763, 341718750),
        f"minus={beta6_minus}, plus={beta6_plus}",
    )

    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
