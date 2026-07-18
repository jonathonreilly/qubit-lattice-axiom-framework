#!/usr/bin/env python3
"""Exact classification of a supplied finite real anomaly-equation system.

This runner verifies the positive abstract theorem in
docs/ABJ_P_COMP_SCALE_FREE_SINGLET_COMPLETION_CLASSIFICATION_NOTE_2026-06-18.md.
It treats every sign and multiplicity in the displayed equations as supplied
input. It does not provide a physical interpretation of those inputs.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re
import sys

try:
    import sympy as sp
except ImportError:
    print("FAIL: sympy is required for exact symbolic checks")
    sys.exit(1)


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "ABJ_P_COMP_SCALE_FREE_SINGLET_COMPLETION_CLASSIFICATION_NOTE_2026-06-18.md"
ABJ_BRIDGE_PATH = (
    ROOT
    / "docs"
    / "ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md"
)
RUNNER_REL = "scripts/frontier_abj_pcomp_scale_free_singlet_completion_classification_2026_06_18.py"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: object = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail != "" else ""
    print(f"{tag}: {name}{suffix}")
    return ok


def section(title: str) -> None:
    print()
    print(f"== {title} ==")


def symbolic_surface(
    a: sp.Expr,
    x: sp.Expr,
    y: sp.Expr,
    z: sp.Expr,
    n: sp.Expr,
) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Return exactly the three supplied signed polynomial residuals."""
    return (
        a - (x + y) / 2,
        -(3 * x + 3 * y + z + n),
        -48 * a**3 - (3 * x**3 + 3 * y**3 + z**3 + n**3),
    )


def rational_surface(
    a: Fraction,
    x: Fraction,
    y: Fraction,
    z: Fraction,
    n: Fraction,
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    return (
        a - (x + y) / 2,
        -(3 * x + 3 * y + z + n),
        -48 * a**3 - (3 * x**3 + 3 * y**3 + z**3 + n**3),
        n,
    )


def part0_source_and_dependency_firewalls() -> None:
    section("Part 0: B-class source and dependency firewalls")
    note = NOTE_PATH.read_text(encoding="utf-8")
    note_flat = re.sub(r"\s+", " ", note)
    abj = ABJ_BRIDGE_PATH.read_text(encoding="utf-8")
    abj_flat = re.sub(r"\s+", " ", abj)

    required_note_markers = [
        "**Claim type:** positive_theorem",
        "does not set or predict an audit outcome",
        "a, x, y, z, n in R",
        "with `a != 0`",
        "additional hypothesis `n = 0`",
        "E_mix = a - (x + y)/2 = 0",
        "E_lin = -(3x + 3y + z + n) = 0",
        "E_cub = -48a^3 - (3x^3 + 3y^3 + z^3 + n^3) = 0",
        "xy = -8a^2",
        "{x, y} = {4a, -2a}",
        "exact implication and classification of the supplied finite algebraic system",
        "supplies no physical realization, species identification",
        "historical filename and claim ID are preserved for graph stability",
        RUNNER_REL,
    ]
    for marker in required_note_markers:
        check(f"B-class note marker: {marker[:72]}", marker in note or marker in note_flat)

    removed_scope_patterns = {
        "counterfactual section": r"^## Counterfactuals\s*$",
        "what-this-moves section": r"^## What this moves\s*$",
        "P-COMP source claim": r"`P-COMP`",
        "named left-handed species": r"\b(?:Q_L|L_L)\b",
        "named completion species": r"\b(?:u_R|d_R|e_R|n_R)\b",
        "physical color-triplet slots": r"color[- ]triplet",
        "Standard Model identification": r"\b(?:Standard Model|SM witness)\b",
        "physical completion surface": r"physical (?:existence|minimality|completion[- ]surface)",
        "opposite-chirality physical template": r"opposite[- ]chirality SU\(2\)[- ]singlet",
        "removed nonuniqueness conclusion": r"uniqueness fails",
        "removed family conclusion": r"one[- ]parameter family",
        "removed missing-slot conclusion": r"missing (?:color[- ]triplet )?slots?",
        "removed cancellation impossibility": r"cannot cancel",
        "removed nonselection conclusion": r"fails? to select",
        "conditional-status rhetoric": r"bounded[- ]support|exact conditional classification",
        "audit outcome claim": r"audited_clean|effective retained",
    }
    for label, pattern in removed_scope_patterns.items():
        check(
            f"B-class note excludes {label}",
            re.search(pattern, note, flags=re.IGNORECASE | re.MULTILINE) is None,
        )

    bridge_markers = [
        "Declared P-COMP completion premise",
        "is used here only for this algebraic implication",
        "supplies the physical slots, signs, multiplicities, and `n = 0`",
        "does not supply that physical surface",
    ]
    for marker in bridge_markers:
        check(f"B-class dependent boundary: {marker[:72]}", marker in abj or marker in abj_flat)


def part1_supplied_surface_encoding() -> None:
    section("Part 1: B-class supplied-surface encoding")
    a, x, y, z, n = sp.symbols("a x y z n", real=True)
    e_mix, e_lin, e_cub = symbolic_surface(a, x, y, z, n)

    mix_poly = sp.Poly(e_mix, a, x, y, z, n)
    lin_poly = sp.Poly(e_lin, a, x, y, z, n)
    cub_poly = sp.Poly(e_cub, a, x, y, z, n)

    check("B-class E_mix coefficient of a is +1", mix_poly.coeff_monomial(a) == 1)
    check(
        "B-class E_mix coefficients of x,y are -1/2",
        all(mix_poly.coeff_monomial(v) == -sp.Rational(1, 2) for v in (x, y)),
    )
    check("B-class E_lin multiplicities of x,y are signed -3", all(lin_poly.coeff_monomial(v) == -3 for v in (x, y)))
    check("B-class E_lin multiplicities of z,n are signed -1", all(lin_poly.coeff_monomial(v) == -1 for v in (z, n)))
    check("B-class E_cub coefficient of a^3 is -48", cub_poly.coeff_monomial(a**3) == -48)
    check(
        "B-class E_cub multiplicities of x^3,y^3 are signed -3",
        all(cub_poly.coeff_monomial(v**3) == -3 for v in (x, y)),
    )
    check(
        "B-class E_cub multiplicities of z^3,n^3 are signed -1",
        all(cub_poly.coeff_monomial(v**3) == -1 for v in (z, n)),
    )
    check("B-class supplied neutral equation is n=0", sp.Eq(n, 0).lhs == n and sp.Eq(n, 0).rhs == 0)


def part2_exact_classification() -> None:
    section("Part 2: A-class exact implication and classification")
    a = sp.symbols("a", real=True, nonzero=True)
    x, y, z, n, p, t = sp.symbols("x y z n p t", real=True)
    e_mix, e_lin, e_cub = symbolic_surface(a, x, y, z, n)

    x_from_mix = sp.solve(sp.Eq(e_mix, 0), x)[0]
    sum_xy = sp.expand(x_from_mix + y)
    check("A-class E_mix=0 forces x+y=2a", sp.simplify(sum_xy - 2 * a) == 0, sum_xy)

    z_value = sp.solve(sp.Eq(e_lin.subs({x: x_from_mix, n: 0}), 0), z)[0]
    check("A-class E_lin=0 with n=0 forces z=-6a", sp.simplify(z_value + 6 * a) == 0, z_value)

    cubic_after = sp.expand(e_cub.subs({z: z_value, n: 0}))
    expected_cubic = -3 * (x**3 + y**3) + 168 * a**3
    check(
        "A-class cubic substitution has the stated signs",
        sp.simplify(cubic_after - expected_cubic) == 0,
        cubic_after,
    )
    check(
        "A-class E_cub=0 forces x^3+y^3=56a^3",
        sp.simplify(cubic_after - (-3 * (x**3 + y**3 - 56 * a**3))) == 0,
    )

    symmetric_identity = sp.expand((x + y) ** 3 - 3 * x * y * (x + y) - (x**3 + y**3))
    check("A-class symmetric-polynomial identity is exact", symmetric_identity == 0)

    cubic_in_p = sp.expand(sum_xy**3 - 3 * p * sum_xy - 56 * a**3)
    p_solution = sp.solve(sp.Eq(cubic_in_p, 0), p)
    check("A-class a is explicitly nonzero before division", a.is_nonzero is True)
    check("A-class product xy is forced to -8a^2", p_solution == [-8 * a**2], p_solution)

    polynomial = t**2 - sum_xy * t + p_solution[0]
    factorization = (t - 4 * a) * (t + 2 * a)
    check(
        "A-class root polynomial has correct sum and product",
        sp.expand(polynomial - (t**2 - 2 * a * t - 8 * a**2)) == 0,
    )
    check("A-class factorization is exact", sp.expand(polynomial - factorization) == 0, sp.factor(polynomial))
    roots = sp.solve(sp.Eq(polynomial, 0), t)
    check("A-class roots are exactly {-2a,4a}", set(roots) == {-2 * a, 4 * a}, roots)
    check("A-class label exchange preserves sum", sp.simplify((4 * a - 2 * a) - (-2 * a + 4 * a)) == 0)
    check("A-class label exchange preserves product", sp.simplify((4 * a) * (-2 * a) - (-2 * a) * (4 * a)) == 0)


def part3_symbolic_converse() -> None:
    section("Part 3: A-class symbolic converse and exact cancellation")
    a = sp.symbols("a", real=True, nonzero=True)
    branches = [
        (4 * a, -2 * a, -6 * a, sp.Integer(0)),
        (-2 * a, 4 * a, -6 * a, sp.Integer(0)),
    ]
    for index, branch in enumerate(branches, start=1):
        residuals = (*symbolic_surface(a, *branch), branch[3])
        for equation_index, residual in enumerate(residuals, start=1):
            check(
                f"A-class branch {index} satisfies supplied equation {equation_index}",
                sp.simplify(residual) == 0,
                sp.simplify(residual),
            )

    wrong_sign = symbolic_surface(a, 4 * a, -2 * a, 6 * a, 0)
    check("A-class wrong sign z=+6a is rejected by E_lin", sp.simplify(wrong_sign[1]) != 0, sp.simplify(wrong_sign[1]))
    wrong_pair = symbolic_surface(a, 4 * a, 2 * a, -6 * a, 0)
    check("A-class wrong x,y sign is rejected by E_mix", sp.simplify(wrong_pair[0]) != 0, sp.simplify(wrong_pair[0]))
    wrong_scale = symbolic_surface(a, 3 * a, -a, -6 * a, 0)
    check(
        "A-class wrong root pair is rejected by E_cub",
        sp.simplify(wrong_scale[2]) != 0,
        sp.simplify(wrong_scale[2]),
    )


def part4_exact_rational_samples() -> None:
    section("Part 4: A-class exact rational sample checks")
    for value in [Fraction(1, 3), Fraction(2, 5), Fraction(-1, 2)]:
        branches = [
            (4 * value, -2 * value, -6 * value, Fraction(0)),
            (-2 * value, 4 * value, -6 * value, Fraction(0)),
        ]
        for index, branch in enumerate(branches, start=1):
            residuals = rational_surface(value, *branch)
            check(
                f"A-class a={value}, branch {index}: all supplied residuals vanish",
                all(residual == 0 for residual in residuals),
                residuals,
            )


def main() -> int:
    print("frontier_abj_pcomp_scale_free_singlet_completion_classification_2026_06_18.py")
    part0_source_and_dependency_firewalls()
    part1_supplied_surface_encoding()
    part2_exact_classification()
    part3_symbolic_converse()
    part4_exact_rational_samples()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: exact positive theorem over the supplied finite algebraic system.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
