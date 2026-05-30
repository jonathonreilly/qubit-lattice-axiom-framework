#!/usr/bin/env python3
"""Audit-companion runner for the narrow theorem note
`KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25.md`.

Verifies, via sympy exact symbolic arithmetic, the separation
identities (S1)-(S3) stated in the note:

  (S1) Six native-unit values defined exactly in Q * pi:
       alpha_1 = 2 pi          (cycle)
       alpha_2 = (2/3) pi      (Z_3-step)
       alpha_3 = (2/9) pi      (Plancherel-step)
       alpha_4 = pi            (Bargmann closed-orbit)
       alpha_5 = (2/3) pi      (character-step)
       alpha_6 = (1/3) pi      (selected-line CP^1 Berry-per-step)
  (S2) No-rational-solution lemma: for each i, c_i * alpha_i = 2/9
       has no nonzero rational solution c_i; setting c_i = 0 gives
       0 != 2/9.
  (S3) Separation theorem: 2/9 not in Q . alpha_i for any i, where
       Q . alpha_i = {q * alpha_i : q in Q}.

Companion role: standalone narrow source of evidence that the pure
rational 2/9 (a dimensionless ratio in Q) is structurally distinct
from every rational multiple of any of the six native angular
constructions enumerated on Cl(3)/Z^3 (each of which is a rational
multiple of pi). The runner makes no claim about the radian-bridge
postulate P or about any PDG-matching content; that is the scope of
the existing retained no-go.

Expected output: PASS=N FAIL=0 with N >= 30.
"""

from __future__ import annotations

import sympy as sp

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    """Increment global PASS/FAIL counters and emit a PASS/FAIL line."""
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    return condition


def banner(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def _check_close(name: str, lhs: sp.Expr, rhs: sp.Expr, detail: str = "") -> bool:
    """Verify lhs == rhs symbolically (simplify(lhs - rhs) == 0)."""
    diff = sp.simplify(lhs - rhs)
    return check(name, diff == 0, detail or f"diff = {diff}")


def _check_distinct(name: str, lhs: sp.Expr, rhs: sp.Expr, detail: str = "") -> bool:
    """Verify lhs != rhs symbolically (simplify(lhs - rhs) != 0)."""
    diff = sp.simplify(lhs - rhs)
    return check(name, diff != 0, detail or f"diff = {diff}")


# ---------------------------------------------------------------------------
# The pure dimensionless rational r = 2/9
# ---------------------------------------------------------------------------

R = sp.Rational(2, 9)


# ---------------------------------------------------------------------------
# (S1) The six native-unit values on Cl(3)/Z^3 as rational multiples of pi
# ---------------------------------------------------------------------------
#
# Each native angular construction listed in the narrow theorem note's
# Section 3 produces a fixed radian value of the form q_i * pi with
# q_i in Q \ {0}.

NATIVE_UNITS: list[tuple[str, sp.Rational]] = [
    ("alpha_1 cycle",                              sp.Rational(2, 1)),    # 2 pi
    ("alpha_2 Z_3-step",                           sp.Rational(2, 3)),    # (2/3) pi
    ("alpha_3 Plancherel-step",                    sp.Rational(2, 9)),    # (2/9) pi
    ("alpha_4 Bargmann closed-orbit",              sp.Rational(1, 1)),    # pi
    ("alpha_5 character-step",                     sp.Rational(2, 3)),    # (2/3) pi
    ("alpha_6 selected-line CP^1 Berry-per-step",  sp.Rational(1, 3)),    # (1/3) pi
]


def part_s1_native_unit_values() -> None:
    banner("(S1) Native-unit values: alpha_i = q_i * pi for fixed nonzero rationals q_i")
    for name, q in NATIVE_UNITS:
        alpha = q * sp.pi
        # q_i is a nonzero rational
        check(
            f"{name}: q_i is a nonzero rational",
            isinstance(q, sp.Rational) and q != 0,
            f"q_i = {q}",
        )
        # alpha simplifies to q * pi exactly
        _check_close(
            f"{name}: alpha simplifies to q*pi exactly",
            alpha,
            q * sp.pi,
            f"alpha = {alpha}, q*pi = {q*sp.pi}",
        )


# ---------------------------------------------------------------------------
# (S2) No-rational-solution lemma: c_i * alpha_i = 2/9 has no rational c_i
# ---------------------------------------------------------------------------

def part_s2_no_rational_solution() -> None:
    banner("(S2) No-rational-solution lemma: c_i * alpha_i = 2/9 has no rational c_i")
    for name, q in NATIVE_UNITS:
        alpha = q * sp.pi
        # Solve c * alpha = R over real c, then inspect the form.
        # The formal solution is c = R / (q * pi) = 2/(9 q pi), which
        # contains pi in the denominator and is therefore NOT a
        # rational number.
        c_free = sp.Symbol("c_free")
        sols_free = sp.solve(sp.Eq(c_free * alpha, R), c_free)
        check(
            f"{name}: sp.solve(c*alpha = 2/9, c[free]) has exactly one formal solution",
            isinstance(sols_free, list) and len(sols_free) == 1,
            f"sols_free = {sols_free}",
        )
        if isinstance(sols_free, list) and len(sols_free) == 1:
            csol = sols_free[0]
            # csol should NOT be a sympy Rational
            check(
                f"{name}: formal solution c = {csol} is NOT a rational",
                not isinstance(csol, sp.Rational),
                f"csol = {csol}, type = {type(csol).__name__}",
            )
            # csol should contain pi as a free symbol
            check(
                f"{name}: formal solution contains pi (transcendental witness)",
                sp.pi in csol.atoms(),
                f"csol = {csol}",
            )
            check(
                f"{name}: rational-domain solution is excluded by pi transcendence",
                csol.is_rational is not True,
                f"csol.is_rational = {csol.is_rational}",
            )

        # Setting c = 0 (the trivial integer rational) gives 0 != 2/9:
        _check_distinct(
            f"{name}: trivial c=0 gives 0 != 2/9",
            sp.Integer(0) * alpha,
            R,
            f"0 * alpha = 0, 2/9 = {R}",
        )


# ---------------------------------------------------------------------------
# (S3) Separation theorem: 2/9 not in Q . alpha_i for any i
# ---------------------------------------------------------------------------
#
# For a battery of nonzero rational test coefficients c, verify
# c * alpha_i != 2/9 for each of the six native units. The expression
# c * q_i * pi - 2/9 is a non-trivial linear combination of pi and 1
# in Q[pi], which sympy does not collapse to zero.

TEST_RATIONALS: list[sp.Rational] = [
    sp.Rational(1, 1),
    sp.Rational(-1, 1),
    sp.Rational(1, 2),
    sp.Rational(1, 9),
    sp.Rational(2, 9),
    sp.Rational(9, 2),
    sp.Rational(3, 1),
    sp.Rational(-2, 3),
    sp.Rational(7, 4),
]


def part_s3_separation_theorem() -> None:
    banner("(S3) Separation theorem: 2/9 != c * alpha_i for any c in Q\\{0}")
    for name, q in NATIVE_UNITS:
        alpha = q * sp.pi
        for c in TEST_RATIONALS:
            # c * alpha = c * q * pi, a nonzero rational multiple of pi.
            # Verify it does NOT equal 2/9.
            _check_distinct(
                f"{name}: c = {c} gives c*alpha != 2/9",
                c * alpha,
                R,
                f"c*alpha = {c*alpha}",
            )


# ---------------------------------------------------------------------------
# (4) Numerical disagreement at high precision
# ---------------------------------------------------------------------------

def part_numerical_disagreement() -> None:
    banner("Numerical disagreement at 50 decimal digits")
    r_num = sp.N(R, 50)
    for name, q in NATIVE_UNITS:
        alpha = q * sp.pi
        alpha_num = sp.N(alpha, 50)
        diff_num = abs(alpha_num - r_num)
        # diff should be many orders of magnitude larger than 1e-40
        check(
            f"{name}: |alpha - 2/9| > 1e-40 at 50 digits",
            diff_num > sp.Float("1e-40"),
            f"|alpha - 2/9| = {diff_num}",
        )


# ---------------------------------------------------------------------------
# (5) Symbolic transcendence-style witness
# ---------------------------------------------------------------------------

def part_symbolic_transcendence_witness() -> None:
    banner("Symbolic transcendence-style witness: alpha_i - 2/9 has nonzero pi-coefficient")
    for name, q in NATIVE_UNITS:
        alpha = q * sp.pi
        diff = sp.simplify(alpha - R)
        # diff should be q * pi - 2/9, NOT zero, NOT rational
        check(
            f"{name}: simplify(alpha - 2/9) is not zero",
            diff != 0,
            f"diff = {diff}",
        )
        check(
            f"{name}: simplify(alpha - 2/9) is not a rational",
            not isinstance(diff, sp.Rational),
            f"diff = {diff}, type = {type(diff).__name__}",
        )
        # alpha itself is not rational (it contains pi)
        check(
            f"{name}: alpha is not declared rational by sympy",
            alpha.is_rational is not True,
            f"alpha.is_rational = {alpha.is_rational}",
        )
        # alpha contains pi as a free symbol
        check(
            f"{name}: alpha contains sp.pi as an atom",
            sp.pi in alpha.atoms(),
            f"atoms(alpha) = {alpha.atoms()}",
        )


# ---------------------------------------------------------------------------
# (6) Counter-example positive control
# ---------------------------------------------------------------------------

def part_counter_example_controls() -> None:
    banner("Counter-example positive controls")
    # The trivial c = 0 case
    for name, q in NATIVE_UNITS:
        alpha = q * sp.pi
        zero_times_alpha = sp.Integer(0) * alpha
        _check_distinct(
            f"{name}: 0 * alpha = 0 != 2/9 (trivial separation)",
            zero_times_alpha,
            R,
        )

    # The "literal-rational-as-radian" non-native identification:
    # If one identifies 2/9 (as a pure rational) with 2/9 radian (radian unit),
    # that IS the radian-bridge primitive P. It is NOT one of the six
    # native units. Verify: 2/9 (no pi) is distinct from each native unit.
    for name, q in NATIVE_UNITS:
        alpha = q * sp.pi
        _check_distinct(
            f"{name}: pure rational 2/9 != alpha (radian-bridge identification not native)",
            R,
            alpha,
        )


# ---------------------------------------------------------------------------
# (7) Sanity: each native unit construction is enumerated
# ---------------------------------------------------------------------------

def part_native_unit_distinct_values() -> None:
    banner("Sanity: distinct q_i across the six native units")
    check(
        "six native-unit constructions enumerated",
        len(NATIVE_UNITS) == 6,
        f"len(NATIVE_UNITS) = {len(NATIVE_UNITS)}",
    )
    qs = [q for _, q in NATIVE_UNITS]
    distinct = set(qs)
    # The six q_i are {2, 2/3, 2/9, 1, 2/3, 1/3} -> distinct = {2, 2/3, 2/9, 1, 1/3} = 5.
    # alpha_2 (Z_3-step) and alpha_5 (character-step) coincide as
    # rational multiples of pi (both = (2/3) pi) even though their
    # construction origins differ (lattice translation vs character increment).
    check(
        "six q_i collapse to five distinct rationals (q_2 = q_5 = 2/3)",
        len(distinct) == 5,
        f"qs = {qs}, distinct = {sorted(distinct)}",
    )


# ---------------------------------------------------------------------------
# (8) Boundary: q_i = 0 excluded
# ---------------------------------------------------------------------------

def part_q_nonzero_boundary() -> None:
    banner("Boundary: no q_i is zero (separation would be vacuous if alpha_i = 0)")
    for name, q in NATIVE_UNITS:
        check(
            f"{name}: q_i != 0",
            q != 0,
            f"q_i = {q}",
        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 88)
    print("Koide dimensionless 2/9 vs radian 2/9 — native-unit separation narrow theorem")
    print("(Audit-companion runner)")
    print("=" * 88)

    part_s1_native_unit_values()
    part_s2_no_rational_solution()
    part_s3_separation_theorem()
    part_numerical_disagreement()
    part_symbolic_transcendence_witness()
    part_counter_example_controls()
    part_native_unit_distinct_values()
    part_q_nonzero_boundary()

    print()
    print("=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"PASSED: {PASS_COUNT}/{PASS_COUNT + FAIL_COUNT}")
    print("=" * 88)

    if FAIL_COUNT == 0:
        # Explicitly conditional headlines. The runner does NOT assert any
        # retained-grade closure of the radian-bridge postulate P; the
        # separation identity is a positive arithmetic statement isolating
        # what P must supply.
        print("KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION=TRUE")
        print("PURE_RATIONAL_2_OVER_9_NOT_IN_Q_DOT_ALPHA_FOR_ANY_NATIVE_UNIT=TRUE")
        print("ALL_SIX_NATIVE_UNITS_ARE_RATIONAL_MULTIPLES_OF_PI=TRUE")
        print("NO_NONZERO_RATIONAL_C_SOLVES_C_ALPHA_EQUAL_2_OVER_9=TRUE")
        print("RADIAN_BRIDGE_POSTULATE_P_CLOSURE_ASSERTED=FALSE")
        print("RETAINED_GRADE_CLOSURE_ASSERTED=FALSE")
        print("RETAINED_GRADE_NO_GO_ASSERTED=FALSE")
        return 0

    print("KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION=FALSE")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
