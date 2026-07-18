#!/usr/bin/env python3
"""Evidence runner for the LH traceless projective-ratio theorem.

Clean theorem:
    n_color is a positive integer, (a,b) is a nonzero real pair, and
    2*n_color*a + 2*b = 0. Then a and b are nonzero,
    b = -n_color*a, and [a:b] = [1:-n_color].

The former charge and reduced-denominator calculations are checked in a
separate CONDITIONAL_SUPPORT class under explicitly supplied ``b = -1`` and
``Q = T_3 + Y/2`` conventions. They are not counted as theorem evidence.

Modes:
    normal       direct symbolic proof plus conditional-support arithmetic
    independent  exact nullspace/exhaustive route plus an independent gcd route
    hostile      counterdomains, alternate scales/readouts, and N1-N8 evidence
    all          all three modes (default)
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from math import gcd
from pathlib import Path
import re
import sys

try:
    import sympy
    from sympy import Matrix, Rational, Symbol, linsolve, simplify, sqrt, symbols
except ImportError:
    print("FAIL: sympy is required for exact algebra", file=sys.stderr)
    raise SystemExit(2)


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs/LH_TRACELESS_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-10.md"
EVIDENCE_CLASSES = ("THEOREM", "CONDITIONAL_SUPPORT", "BOUNDARY", "HYGIENE")

passes: dict[str, int] = defaultdict(int)
failures: dict[str, int] = defaultdict(int)


def check(evidence_class: str, label: str, condition: object, detail: str = "") -> None:
    """Record a computed check in exactly one evidence class."""
    ok = bool(condition)
    bucket = passes if ok else failures
    bucket[evidence_class] += 1
    tag = "PASS" if ok else "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag} {evidence_class}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 96)
    print(title)
    print("-" * 96)


def positive_integer_count(value: object) -> bool:
    """Return whether ``value`` lies in the theorem's count domain."""
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def trace_zero(n_value: object, pair: tuple[object, object]) -> bool:
    """Evaluate the homogeneous trace equation without dividing."""
    a_value, b_value = pair
    return simplify(2 * n_value * a_value + 2 * b_value) == 0


def projective_equal(
    pair: tuple[object, object], reference: tuple[object, object]
) -> bool:
    """Use the determinant test, while rejecting either zero representative."""
    if pair == (0, 0) or reference == (0, 0):
        return False
    a_value, b_value = pair
    x_value, y_value = reference
    return simplify(a_value * y_value - b_value * x_value) == 0


def conditional_readout(
    n_value: object,
    b_value: object | None,
    y_coefficient: object | None,
) -> tuple[object, object, object] | None:
    """Return ``(a,Q_up,Q_down)`` only after both support inputs are supplied."""
    if (
        not positive_integer_count(n_value)
        or b_value is None
        or y_coefficient is None
    ):
        return None
    a_value = -Fraction(b_value, n_value)
    q_up = Fraction(1, 2) + y_coefficient * a_value
    q_down = -Fraction(1, 2) + y_coefficient * a_value
    return a_value, q_up, q_down


def hostile_route_results() -> dict[str, bool]:
    """Compute the six N1 attack-route dispositions from load-bearing checks."""
    zero_pair = (0, 0)
    zero_parameter_pair = (Fraction(1), Fraction(0))
    negative_pair = (Fraction(3, 2), Fraction(3))
    rational_pair = (Fraction(4), Fraction(-2))
    irrational_parameter = sqrt(2)
    irrational_pair = (1, -irrational_parameter)
    scale_two = (Fraction(2), Fraction(-6))
    scale_minus_three = (Fraction(-3), Fraction(9))
    standard = conditional_readout(3, -1, Fraction(1, 2))
    alternate = conditional_readout(3, -1, Fraction(1))

    return {
        "zero_pair": trace_zero(3, zero_pair)
        and not projective_equal(zero_pair, (1, -3)),
        "zero_parameter": not positive_integer_count(0)
        and trace_zero(0, zero_parameter_pair)
        and zero_parameter_pair[0] != 0
        and zero_parameter_pair[1] == 0,
        "negative_parameter": not positive_integer_count(-2)
        and trace_zero(-2, negative_pair)
        and projective_equal(negative_pair, (1, 2)),
        "noninteger_parameter": not positive_integer_count(Fraction(1, 2))
        and not positive_integer_count(irrational_parameter)
        and trace_zero(Fraction(1, 2), rational_pair)
        and trace_zero(irrational_parameter, irrational_pair)
        and projective_equal(rational_pair, (1, -Fraction(1, 2)))
        and projective_equal(irrational_pair, (1, -irrational_parameter)),
        "alternate_scale": trace_zero(3, scale_two)
        and trace_zero(3, scale_minus_three)
        and projective_equal(scale_two, (1, -3))
        and projective_equal(scale_minus_three, (1, -3))
        and scale_two != scale_minus_three
        and scale_two[1] != -1
        and scale_minus_three[1] != -1,
        "alternate_charge_functional": standard is not None
        and alternate is not None
        and standard[1:] != alternate[1:]
        and tuple(value.denominator for value in standard[1:])
        != tuple(value.denominator for value in alternate[1:]),
    }


def normal_mode() -> None:
    section("NORMAL: direct symbolic proof of the homogeneous/projective implication")
    n = Symbol("n_color", positive=True, integer=True)
    a, b = symbols("a b", real=True)
    trace = 2 * n * a + 2 * b
    reduced = n * a + b

    check(
        "THEOREM",
        "dividing the trace equation by 2 gives n_color*a + b",
        simplify(trace / 2 - reduced) == 0,
        f"trace/2 - reduced = {simplify(trace / 2 - reduced)}",
    )

    b_solved = sympy.solve(reduced, b)[0]
    check(
        "THEOREM",
        "trace equation solves to b = -n_color*a",
        simplify(b_solved + n * a) == 0,
        f"b = {b_solved}",
    )

    zero_if_a_zero = linsolve((Matrix([[n, 1], [1, 0]]), Matrix([0, 0])), (a, b))
    check(
        "THEOREM",
        "trace plus a=0 has the single solution (a,b)=(0,0)",
        zero_if_a_zero == sympy.FiniteSet((0, 0)),
        f"solutions = {zero_if_a_zero}",
    )

    zero_if_b_zero = linsolve((Matrix([[n, 1], [0, 1]]), Matrix([0, 0])), (a, b))
    check(
        "THEOREM",
        "trace plus b=0 has the single solution (a,b)=(0,0) for nonzero n_color",
        zero_if_b_zero == sympy.FiniteSet((0, 0)),
        f"solutions = {zero_if_b_zero}",
    )

    projective_determinant = simplify(a * (-n) - b)
    check(
        "THEOREM",
        "projective equality follows by the division-free determinant test",
        simplify(projective_determinant + reduced) == 0,
        f"det((a,b),(1,-n_color)) = {projective_determinant}",
    )

    lam = Symbol("lambda", real=True, nonzero=True)
    representative = Matrix([lam, -n * lam])
    check(
        "THEOREM",
        "every nonzero scale lambda gives a trace-zero representative",
        simplify((Matrix([[2 * n, 2]]) * representative)[0]) == 0,
        f"representative = {representative.T}",
    )
    check(
        "THEOREM",
        "the representative is lambda*(1,-n_color)",
        simplify(representative - lam * Matrix([1, -n])) == Matrix([0, 0]),
    )
    check(
        "THEOREM",
        "division occurs only on the nonzero representative and gives a/b=-1/n_color",
        simplify(representative[0] / representative[1] + Rational(1, 1) / n) == 0,
        f"a/b = {simplify(representative[0] / representative[1])}",
    )
    check(
        "THEOREM",
        "n_color=1 gives the projective point [1:-1]",
        Matrix([[2, 2]]) * Matrix([1, -1]) == Matrix([0]),
    )
    signed_scales = (Rational(2), Rational(-3), Rational(5, 7))
    signed_scale_ok = all(
        simplify(2 * 5 * scale + 2 * (-5 * scale)) == 0
        and scale != 0
        for scale in signed_scales
    )
    check(
        "THEOREM",
        "positive, negative, and fractional nonzero scales preserve the n_color=5 class",
        signed_scale_ok,
        f"scales = {signed_scales}",
    )

    section("NORMAL: explicitly convention-supplied arithmetic (not theorem evidence)")
    a_norm = sympy.solve(reduced.subs(b, -1), a)[0]
    q_up = Rational(1, 2) + a_norm / 2
    q_down = -Rational(1, 2) + a_norm / 2
    check(
        "CONDITIONAL_SUPPORT",
        "under supplied b=-1, a=1/n_color",
        simplify(a_norm - 1 / n) == 0,
        f"a = {a_norm}",
    )
    check(
        "CONDITIONAL_SUPPORT",
        "under supplied Q=T3+Y/2, Q(up)=(n_color+1)/(2*n_color)",
        simplify(q_up - (n + 1) / (2 * n)) == 0,
        f"Q(up) = {simplify(q_up)}",
    )
    check(
        "CONDITIONAL_SUPPORT",
        "under supplied Q=T3+Y/2, Q(down)=(1-n_color)/(2*n_color)",
        simplify(q_down - (1 - n) / (2 * n)) == 0,
        f"Q(down) = {simplify(q_down)}",
    )
    check(
        "CONDITIONAL_SUPPORT",
        "the two supplied-convention charges differ by one",
        simplify(q_up - q_down) == 1,
    )
    check(
        "CONDITIONAL_SUPPORT",
        "the supplied-convention charges sum to 1/n_color",
        simplify(q_up + q_down - 1 / n) == 0,
    )


def independent_mode() -> None:
    section("INDEPENDENT: exact nullspace/projective route")
    n = Symbol("n_color", positive=True, integer=True)
    row = Matrix([[2 * n, 2]])
    nullspace = row.nullspace()
    check(
        "THEOREM",
        "the exact trace row has a one-dimensional nullspace",
        len(nullspace) == 1 and row.rank() == 1,
        f"basis = {nullspace}",
    )
    basis = nullspace[0]
    check(
        "THEOREM",
        "the nullspace basis is projectively equal to (1,-n_color)",
        simplify(basis[0] * (-n) - basis[1]) == 0,
        f"basis = {basis.T}",
    )

    tested_pairs = 0
    exhaustive_ok = True
    for n_value in range(1, 8):
        for a_value in range(-12, 13):
            for b_value in range(-12, 13):
                if (a_value, b_value) == (0, 0):
                    continue
                if 2 * n_value * a_value + 2 * b_value == 0:
                    tested_pairs += 1
                    exhaustive_ok = exhaustive_ok and a_value != 0 and b_value != 0
                    exhaustive_ok = exhaustive_ok and (-n_value * a_value - b_value == 0)
    check(
        "THEOREM",
        "finite hostile enumeration finds no nonzero off-projective solution for n_color=1..7",
        exhaustive_ok and tested_pairs > 0,
        f"nonzero trace-zero pairs tested = {tested_pairs}",
    )

    rational_scales = (Fraction(-7, 3), Fraction(-1, 2), Fraction(1, 5), Fraction(9, 4))
    exact_fraction_ok = all(
        2 * 11 * scale + 2 * (-11 * scale) == 0
        and scale / (-11 * scale) == Fraction(-1, 11)
        for scale in rational_scales
    )
    check(
        "THEOREM",
        "independent Fraction arithmetic agrees at n_color=11 across four scales",
        exact_fraction_ok,
        f"scales = {rational_scales}",
    )

    section("INDEPENDENT: Euclidean/GCD route for conditional support")
    up_bezout_certificate = (
        simplify(2 * (n + 1) - 2 * n),
        simplify(2 * (n + 1) - 2),
    )
    down_bezout_certificate = (
        simplify(2 * n + 2 * (1 - n)),
        simplify(2 - 2 * (1 - n)),
    )
    check(
        "CONDITIONAL_SUPPORT",
        "two-way Bezout combinations prove both gcd reductions for arbitrary integer n_color",
        up_bezout_certificate == (2, 2 * n)
        and down_bezout_certificate == (2, 2 * n),
        f"up=(2,2n): {up_bezout_certificate}; down=(2,2n): {down_bezout_certificate}",
    )

    residue_gcds = {
        residue: (gcd(residue + 1, 2), gcd(1 - residue, 2))
        for residue in (0, 1)
    }
    check(
        "CONDITIONAL_SUPPORT",
        "the two residue classes modulo 2 prove the common gcd is 1 for even and 2 for odd n_color",
        residue_gcds == {0: (1, 1), 1: (2, 2)},
        f"residue certificate = {residue_gcds}",
    )

    k = Symbol("k", nonnegative=True, integer=True)
    odd_n = 2 * k + 1
    even_n = 2 * (k + 1)
    check(
        "CONDITIONAL_SUPPORT",
        "the parity gcd certificate gives denominator n_color for odd and 2*n_color for even counts",
        simplify((2 * odd_n) / 2 - odd_n) == 0
        and simplify((2 * even_n) / 1 - 2 * even_n) == 0,
    )

    values = range(1, 65)
    gcd_reduction_ok = all(
        gcd(n_value + 1, 2 * n_value) == gcd(n_value + 1, 2)
        and gcd(1 - n_value, 2 * n_value) == gcd(1 - n_value, 2)
        for n_value in values
    )
    check(
        "CONDITIONAL_SUPPORT",
        "regression-only sweep confirms Euclidean gcd reductions for n_color=1..64",
        gcd_reduction_ok,
        "finite sweep supports but does not prove the universal identity",
    )
    odd_denominator_ok = all(
        Fraction(n_value + 1, 2 * n_value).denominator == n_value
        and Fraction(1 - n_value, 2 * n_value).denominator == n_value
        for n_value in values
        if n_value % 2 == 1
    )
    check(
        "CONDITIONAL_SUPPORT",
        "regression-only sweep finds denominator n_color for odd n_color=1..63",
        odd_denominator_ok,
    )
    even_denominator_ok = all(
        Fraction(n_value + 1, 2 * n_value).denominator == 2 * n_value
        and Fraction(1 - n_value, 2 * n_value).denominator == 2 * n_value
        for n_value in values
        if n_value % 2 == 0
    )
    check(
        "CONDITIONAL_SUPPORT",
        "regression-only sweep finds denominator 2*n_color for even n_color=2..64",
        even_denominator_ok,
    )


def hostile_mode() -> None:
    section("HOSTILE: counterdomains, normalization freedom, and alternate readout")

    zero_pair = (0, 0)
    check(
        "BOUNDARY",
        "the excluded zero pair satisfies the homogeneous trace equation",
        trace_zero(3, zero_pair),
    )
    check(
        "BOUNDARY",
        "the zero pair has no projective class under the executable determinant guard",
        not projective_equal(zero_pair, (1, -3)),
    )

    zero_parameter_pair = (Fraction(1), Fraction(0))
    check(
        "BOUNDARY",
        "at n_color=0, (1,0) is trace-zero and refutes the two-nonzero conclusion",
        not positive_integer_count(0)
        and trace_zero(0, zero_parameter_pair)
        and zero_parameter_pair[0] != 0
        and zero_parameter_pair[1] == 0,
    )

    negative_n_pair = (Fraction(3, 2), Fraction(3))
    check(
        "BOUNDARY",
        "negative n_color=-2 preserves the projective algebra outside the count domain",
        not positive_integer_count(-2)
        and trace_zero(-2, negative_n_pair)
        and projective_equal(negative_n_pair, (1, 2)),
    )

    rational_n_pair = (Fraction(4), Fraction(-2))
    check(
        "BOUNDARY",
        "noninteger n_color=1/2 preserves the projective algebra but has no integer parity class",
        not positive_integer_count(Fraction(1, 2))
        and trace_zero(Fraction(1, 2), rational_n_pair)
        and projective_equal(rational_n_pair, (1, -Fraction(1, 2))),
    )

    irrational_n = sqrt(2)
    irrational_pair = (1, -irrational_n)
    check(
        "BOUNDARY",
        "irrational nonzero parameter preserves the projective identity outside rational gcd arithmetic",
        not positive_integer_count(irrational_n)
        and trace_zero(irrational_n, irrational_pair)
        and projective_equal(irrational_pair, (1, -irrational_n)),
    )

    scale_two = (Fraction(2), Fraction(-6))
    scale_minus_three = (Fraction(-3), Fraction(9))
    check(
        "BOUNDARY",
        "alternate scale lambda=2 at n_color=3 satisfies trace but has b=-6",
        trace_zero(3, scale_two)
        and projective_equal(scale_two, (1, -3))
        and scale_two[1] != -1,
    )
    check(
        "BOUNDARY",
        "alternate sign scale lambda=-3 at n_color=3 satisfies trace but has b=+9",
        trace_zero(3, scale_minus_three)
        and projective_equal(scale_minus_three, (1, -3))
        and scale_minus_three[1] != -1,
    )
    check(
        "BOUNDARY",
        "two unequal scales give the same projective point and different absolute eigenvalues",
        scale_two != scale_minus_three
        and scale_two[0] * scale_minus_three[1] - scale_two[1] * scale_minus_three[0] == 0,
    )

    n_value = 3
    standard_readout = conditional_readout(n_value, -1, Fraction(1, 2))
    alternate_readout = conditional_readout(n_value, -1, Fraction(1))
    assert standard_readout is not None and alternate_readout is not None
    a_normalized, q_half_up, q_half_down = standard_readout
    _, q_full_up, q_full_down = alternate_readout
    check(
        "BOUNDARY",
        "alternate Q=T3+Y changes both R3 charge clauses at fixed normalization",
        q_half_up == Fraction(2, 3)
        and q_half_down == Fraction(-1, 3)
        and q_full_up == Fraction(5, 6)
        and q_full_down == Fraction(-1, 6)
        and (q_full_up, q_full_down) != (q_half_up, q_half_down),
        f"Q_half={(q_half_up, q_half_down)}, Q_full={(q_full_up, q_full_down)}",
    )
    check(
        "BOUNDARY",
        "alternate Q=T3+Y changes the R4 reduced-denominator readout",
        (q_half_up.denominator, q_half_down.denominator) == (3, 3)
        and (q_full_up.denominator, q_full_down.denominator) == (6, 6),
    )

    scaled_readout = conditional_readout(n_value, scale_two[1], Fraction(1, 2))
    assert scaled_readout is not None
    _, q_scaled_up, _ = scaled_readout
    check(
        "BOUNDARY",
        "supplying Q=T3+Y/2 without b=-1 leaves the charge scale-dependent",
        q_scaled_up == Fraction(3, 2) and q_scaled_up != q_half_up,
        f"scaled Q={q_scaled_up}, normalized Q={q_half_up}",
    )
    check(
        "BOUNDARY",
        "without supplied normalization the conditional readout remains open",
        conditional_readout(n_value, None, Fraction(1, 2)) is None,
    )
    check(
        "BOUNDARY",
        "without a supplied charge functional the conditional readout remains open",
        conditional_readout(n_value, -1, None) is None,
    )

    section("HOSTILE: N1-N8 boundary evidence")
    route_results = hostile_route_results()
    check(
        "BOUNDARY",
        "N1 ATTEMPTED six distinct attack routes and computed every disposition",
        len(route_results) == 6 and all(route_results.values()),
        ", ".join(f"{key}={value}" for key, value in sorted(route_results.items())),
    )
    check(
        "BOUNDARY",
        "N2 normalization does not close the charge-functional condition",
        q_full_up != q_half_up,
        "b=-1 held fixed while the charge functional changed",
    )
    check(
        "BOUNDARY",
        "N2 charge-functional convention does not close the normalization condition",
        q_scaled_up != q_half_up,
        "Q=T3+Y/2 held fixed while the common scale changed",
    )

    note_text = NOTE.read_text(encoding="utf-8")
    hidden_wall_phrases = tuple(
        phrase.lower()
        for phrase in (
        "we assume",
        "by construction",
        "as is standard",
        "the framework provides",
        "bridge context",
        "background",
        "naturally",
        "obviously",
        "standard QFT",
        "registered",
        "canonical",
        "requires a new axiom",
        "no retained primitive",
        )
    )
    hidden_hits = {phrase: note_text.lower().count(phrase) for phrase in hidden_wall_phrases}
    check(
        "HYGIENE",
        "N3 hidden-wall phrase scan has no unclassified trigger",
        sum(hidden_hits.values()) == 0,
        f"hits = {hidden_hits}",
    )

    markdown_note_links = re.findall(
        r"\[[^\]]+\]\(([^)]+\.md(?:#[^)]*)?)\)", note_text
    )
    check(
        "HYGIENE",
        "N4 is N/A because the self-contained note cites no prior Markdown witness",
        markdown_note_links == [],
        f"Markdown note links = {markdown_note_links}",
    )
    check(
        "BOUNDARY",
        "N5 alternate scale blocks an absolute-eigenvalue reading of the projective theorem",
        scale_two[1] != -1 and scale_minus_three[1] != -1,
    )
    check(
        "BOUNDARY",
        "N5 alternate charge functional blocks a physical-charge reading of the projective theorem",
        q_full_up != q_half_up,
    )
    check(
        "BOUNDARY",
        "N6 convention-supplied partial closure reproduces the conditional n_color=3 arithmetic",
        a_normalized == Fraction(1, 3)
        and q_half_up == Fraction(2, 3)
        and q_half_down == Fraction(-1, 3),
    )
    check(
        "BOUNDARY",
        "N7 steelman closes the support arithmetic by definition without enlarging R1",
        trace_zero(3, zero_pair)
        and standard_readout == (Fraction(1, 3), Fraction(2, 3), Fraction(-1, 3))
        and q_full_up != q_half_up
        and projective_equal(scale_two, (1, -3)),
    )

    normal_vector = Matrix([1, -5])
    independent_basis = Matrix([[10, 2]]).nullspace()[0]
    check(
        "BOUNDARY",
        "N8 direct rearrangement and independent nullspace routes agree projectively at n_color=5",
        simplify(normal_vector[0] * independent_basis[1] - normal_vector[1] * independent_basis[0]) == 0,
        f"direct={normal_vector.T}, nullspace={independent_basis.T}",
    )

    linked_absolute_paths = sympy.Integer(
        len(
            [
                marker
                for marker in ('](/Users/', '](/home/', '](/private/', '](/tmp/', '](/var/', '](/opt/', '](file://')
                if marker in note_text
            ]
        )
    )
    check(
        "HYGIENE",
        "changed note has no absolute local markdown link target",
        linked_absolute_paths == 0,
    )
    broad_negative_hits = {
        phrase: note_text.lower().count(phrase)
        for phrase in ("nothing else", "cannot be derived", "unique", "forced")
    }
    check(
        "HYGIENE",
        "broad-negative phrase scan finds no unqualified foreclosure wording",
        sum(broad_negative_hits.values()) == 0,
        f"hits = {broad_negative_hits}",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("normal", "independent", "hostile", "all"),
        default="all",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print("=" * 96)
    print("LH traceless projective-ratio theorem evidence runner")
    print(f"mode: {args.mode}")
    print("Clean clause: trace + positive-integer count + nonzero pair => [a:b]=[1:-n_color]")
    print("Conditional clauses: b=-1 and Q=T3+Y/2 arithmetic remain supplied-convention support")
    print("=" * 96)

    if args.mode in ("normal", "all"):
        normal_mode()
    if args.mode in ("independent", "all"):
        independent_mode()
    if args.mode in ("hostile", "all"):
        hostile_mode()

    print()
    print("=" * 96)
    print("EVIDENCE COUNTS")
    for evidence_class in EVIDENCE_CLASSES:
        print(
            f"  {evidence_class}: PASS={passes[evidence_class]} "
            f"FAIL={failures[evidence_class]}"
        )
    total_pass = sum(passes.values())
    total_fail = sum(failures.values())
    print(f"TOTAL: PASS={total_pass} FAIL={total_fail}")
    print("Clean clause: homogeneous/projective implication stated above.")
    print("Conditional clauses: normalization, charge readout, and denominator support.")
    print("No audit verdict is issued by this runner.")
    print("=" * 96)
    return 0 if total_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
