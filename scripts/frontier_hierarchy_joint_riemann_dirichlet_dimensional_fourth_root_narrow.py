#!/usr/bin/env python3
"""Evidence runner for the joint eta/zeta and dimensional-exponent theorem.

The source theorem has four exact parts:

* eta(s)/zeta(s) = 1 - 2^(1-s) on the stated series domain;
* g(s) = (eta(s)/zeta(s))^(1/s) is strictly increasing on integer s >= 2
  and tends to one;
* g(s) = (7/8)^(1/4) on that integer domain iff s = 4;
* a nontrivial monomial nonnegative-magnitude map from a mass^d quantity to
  a mass scale has exponent p = 1/d, leaving the supplied dimensionless
  coefficient and sign/magnitude convention unselected.

Modes are deliberately distinct:

* normal builds the odd/even split, Taylor-coefficient, limit, exact-value,
  dimension-equation, coefficient-freedom, and zero-boundary objects;
* independent uses a real-derivative proof, rigorous rational partial-sum
  brackets, and exact unit-rescaling covariance;
* hostile rejects the known sign, dimension, normalization, domain, and
  physical-inference overreads.

Every universal claim is carried by an analytic certificate. Finite scans are
labelled numerical support and never substitute for those certificates.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/HIERARCHY_JOINT_RIEMANN_DIRICHLET_DIMENSIONAL_FOURTH_ROOT_NARROW_THEOREM_NOTE_2026-05-10.md",
    "docs/audit/data/premise_decision_history.json",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
)

try:
    import sympy as sp
except ImportError:
    print("FAIL: sympy is required for exact symbolic certificates")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = (
    ROOT
    / "docs"
    / "HIERARCHY_JOINT_RIEMANN_DIRICHLET_DIMENSIONAL_FOURTH_ROOT_NARROW_THEOREM_NOTE_2026-05-10.md"
)
PREMISE_HISTORY_PATH = ROOT / "docs" / "audit" / "data" / "premise_decision_history.json"
SCALE_REFERENCE_PATH = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"

PASS_COUNT = 0
FAIL_COUNT = 0
EVIDENCE_COUNTS: Counter[str] = Counter()
CLASS_COUNTS: Counter[str] = Counter()
MODE_COUNTS: Counter[str] = Counter()

# Per-check evidence tags are abbreviated on the printed line and expanded by the
# TAGS legend below the mode banner; the EVIDENCE summary still names them in full.
# An unmapped tag prints unabbreviated rather than being dropped.
EVIDENCE_TAGS = {
    "theorem": "thm",
    "conditional": "cond",
    "numerical": "num",
    "boundary": "bnd",
    "hygiene": "hyg",
}


def check(
    mode: str,
    evidence: str,
    label: str,
    condition: object,
    detail: str = "",
    klass: str = "A",
) -> bool:
    """Record one computed check without relying on Python assert."""

    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS_COUNT += 1
        EVIDENCE_COUNTS[evidence] += 1
        CLASS_COUNTS[klass] += 1
        MODE_COUNTS[mode] += 1
    else:
        FAIL_COUNT += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"[{tag}][{klass}][{EVIDENCE_TAGS.get(evidence, evidence)}] {label}{suffix}")
    return ok


def section(title: str) -> None:
    print(title)


def closed_ratio(s: int) -> Fraction:
    return Fraction(1) - Fraction(1, 2 ** (s - 1))


def g_decimal(s: int) -> Decimal:
    inner = Decimal(1) - Decimal(1) / (Decimal(2) ** (s - 1))
    return (inner.ln() / Decimal(s)).exp()


def eta_zeta_ratio_bracket(s: int, terms: int) -> tuple[Fraction, Fraction]:
    """Rigorous bracket from positive-series integral bounds and the
    alternating-series remainder. ``terms`` must be positive and even.
    """

    if s <= 1 or terms <= 0 or terms % 2:
        raise ValueError("require s > 1 and a positive even term count")
    zeta_part = sum(Fraction(1, n**s) for n in range(1, terms + 1))
    zeta_tail_lo = Fraction(1, (s - 1) * (terms + 1) ** (s - 1))
    zeta_tail_hi = Fraction(1, (s - 1) * terms ** (s - 1))
    zeta_lo = zeta_part + zeta_tail_lo
    zeta_hi = zeta_part + zeta_tail_hi

    eta_part = sum(
        Fraction(1 if n % 2 else -1, n**s) for n in range(1, terms + 1)
    )
    eta_lo = eta_part
    eta_hi = eta_part + Fraction(1, (terms + 1) ** s)
    return eta_lo / zeta_hi, eta_hi / zeta_lo


@dataclass(frozen=True)
class ScaleMapCase:
    d: int
    p: Fraction
    kappa: Fraction = Fraction(1)
    kappa_mass_dimension: Fraction = Fraction(0)
    f: Fraction | None = Fraction(16)
    magnitude_convention: bool = True
    kappa_supplied: bool = True
    carrier_supplied: bool = True
    infer_physical_value: bool = False

    def dimension_residual(self) -> Fraction | None:
        if self.d <= 0:
            return None
        return self.kappa_mass_dimension + self.d * self.p - 1

    def issues(self) -> set[str]:
        issues: set[str] = set()
        if self.d <= 0:
            issues.add("invalid_dimension")
            return issues

        residual = self.dimension_residual()
        if self.kappa_mass_dimension != 0:
            issues.add("dimensionful_kappa")
        if self.kappa < 0:
            issues.add("negative_magnitude_coefficient")
        if residual != 0:
            issues.add("dimension_covariance_failure")
        if self.d * self.p != 1:
            issues.add("wrong_exponent")

        if self.f is not None and self.f < 0 and not self.magnitude_convention:
            issues.add("nonreal_even_root" if self.d % 2 == 0 else "signed_not_magnitude")
        if not self.kappa_supplied:
            issues.add("unsupplied_coefficient")
        if self.infer_physical_value and (
            self.f is None or not self.carrier_supplied
        ):
            issues.add("unsupported_physical_inference")
        return issues

    def supplied_conditions(self) -> set[str]:
        conditions: set[str] = set()
        if self.kappa_supplied:
            conditions.add("coefficient")
        if self.magnitude_convention:
            conditions.add("magnitude_convention")
        if self.carrier_supplied:
            conditions.add("carrier")
        if self.f is not None:
            conditions.add("value")
        return conditions

    def magnitude_value(self) -> sp.Expr | None:
        if self.d <= 0 or self.f is None:
            return None
        return sp.Rational(self.kappa.numerator, self.kappa.denominator) * sp.Pow(
            abs(self.f), sp.Rational(self.p.numerator, self.p.denominator)
        )


def normal_mode() -> None:
    mode = "normal"
    section("NORMAL")

    s = sp.symbols("s", real=True)
    closed_base = 1 - sp.Pow(2, 1 - s)
    positive_domain = sp.solve_univariate_inequality(
        closed_base > 0, s, relational=False
    )
    below_one_domain = sp.solve_univariate_inequality(
        closed_base < 1, s, relational=False
    )
    check(
        mode,
        "theorem",
        "exact real domain of the eta/zeta base is 0 < 1-2^(1-s) < 1 for s>1",
        positive_domain == sp.Interval.open(1, sp.oo)
        and below_one_domain == sp.S.Reals
        and closed_base.subs(s, 2) == sp.Rational(1, 2)
        and closed_base.subs(s, 4) == sp.Rational(7, 8)
        and sp.simplify(
            sp.Pow(closed_base.subs(s, 2), sp.Rational(1, 2))
            - 1 / sp.sqrt(2)
        )
        == 0,
        detail=(
            f"positive domain={positive_domain}; below-one domain={below_one_domain}; "
            "g(2)=1/sqrt(2); s=4 base -> 7/8"
        ),
    )

    z = sp.symbols("Z", nonzero=True)
    even = sp.Pow(2, -s) * z
    odd = (1 - sp.Pow(2, -s)) * z
    split_residual = sp.simplify((odd - even) / z - (1 - sp.Pow(2, 1 - s)))
    check(
        mode,
        "theorem",
        "odd/even series split has zero eta/zeta closed-form residual",
        split_residual == 0,
        detail=f"residual = {split_residual}",
    )

    s_i, k_i = sp.symbols("s_i k_i", positive=True, integer=True)
    coefficient_residual = (s_i + 1) * sp.Pow(2, k_i) - s_i
    base_residual = sp.simplify(coefficient_residual.subs(k_i, 1))
    recurrence_residual = sp.simplify(
        coefficient_residual.subs(k_i, k_i + 1) - 2 * coefficient_residual
    )
    decomposition_residual = sp.simplify(
        coefficient_residual
        - ((s_i + 1) * (sp.Pow(2, k_i) - 2) + (s_i + 2))
    )
    check(
        mode,
        "theorem",
        "Taylor-coefficient comparison has a positive induction certificate",
        base_residual == s_i + 2
        and recurrence_residual == s_i
        and decomposition_residual == 0,
        detail=(
            f"R_1={base_residual}; R_(k+1)-2R_k={recurrence_residual}; "
            f"decomposition residual={decomposition_residual}"
        ),
    )

    log_g = sp.log(1 - sp.Pow(2, 1 - s)) / s
    log_limit = sp.limit(log_g, s, sp.oo)
    check(
        mode,
        "theorem",
        "log g(s) tends to zero, so g(s) tends to one",
        log_limit == 0,
        detail=f"lim log(g) = {log_limit}",
    )

    value_at_four = closed_ratio(4)
    check(
        mode,
        "theorem",
        "the exact target base at s=4 is 7/8",
        value_at_four == Fraction(7, 8),
        detail=f"1 - 2^(-3) = {value_at_four}",
    )

    d, p = sp.symbols("d p", positive=True)
    exponent_solutions = sp.solve(sp.Eq(d * p, 1), p)
    check(
        mode,
        "conditional",
        "mass-dimension equation d*p=1 has exponent p=1/d",
        exponent_solutions == [1 / d],
        detail=f"solutions = {exponent_solutions}",
    )

    valid_cases = [
        ScaleMapCase(d=d0, p=Fraction(1, d0), kappa=kappa)
        for d0 in range(1, 9)
        for kappa in (Fraction(1, 3), Fraction(1), Fraction(5, 2))
    ]
    residuals = [case.dimension_residual() for case in valid_cases]
    check(
        mode,
        "conditional",
        "all supplied dimensionless coefficients share zero dimension residual at p=1/d",
        set(residuals) == {Fraction(0)} and all(not case.issues() for case in valid_cases),
        detail=f"cases={len(valid_cases)}, residual set={set(residuals)}",
    )

    coefficient_witnesses = [
        ScaleMapCase(d=4, p=Fraction(1, 4), kappa=Fraction(1, 3)),
        ScaleMapCase(d=4, p=Fraction(1, 4), kappa=Fraction(5, 2)),
    ]
    witness_values = [sp.simplify(case.magnitude_value()) for case in coefficient_witnesses]
    check(
        mode,
        "boundary",
        "distinct positive dimensionless coefficients remain covariant and give distinct scales",
        all(case.dimension_residual() == 0 for case in coefficient_witnesses)
        and witness_values[0] != witness_values[1],
        detail=f"at |f|=16: values={witness_values}",
    )

    zero_cases = [
        ScaleMapCase(d=d0, p=Fraction(1, d0), kappa=kappa, f=Fraction(0))
        for d0 in (1, 2, 4, 7)
        for kappa in (Fraction(0), Fraction(1, 3), Fraction(2))
    ]
    zero_values = [sp.simplify(case.magnitude_value()) for case in zero_cases]
    check(
        mode,
        "boundary",
        "finite-kappa p=1/d family extends to M(0)=0 for d>0",
        set(zero_values) == {sp.Integer(0)},
        detail=f"cases={len(zero_cases)}, values={set(zero_values)}",
    )

    thermal_values = [
        sp.Pow(sp.Rational(c0) * sp.Pow(2, 4), sp.Rational(1, 4))
        for c0 in (1, 16)
    ]
    check(
        mode,
        "boundary",
        "a dimensionless thermal coefficient changes the magnitude without changing covariance",
        [sp.simplify(value) for value in thermal_values] == [2, 4],
        detail=f"for T=2 and c_4=(1,16), fourth roots={thermal_values}",
    )

    fully_supplied = ScaleMapCase(
        d=4,
        p=Fraction(1, 4),
        kappa=Fraction(3, 2),
        f=Fraction(-16),
        magnitude_convention=True,
        kappa_supplied=True,
        carrier_supplied=True,
    )
    check(
        mode,
        "conditional",
        "fully supplied coefficient, magnitude rule, carrier, and value close the map conditionally",
        not fully_supplied.issues()
        and fully_supplied.supplied_conditions()
        == {"coefficient", "magnitude_convention", "carrier", "value"}
        and sp.simplify(fully_supplied.magnitude_value()) == 3,
        detail=(
            f"conditions={sorted(fully_supplied.supplied_conditions())}; "
            f"M={fully_supplied.magnitude_value()}"
        ),
    )

    with localcontext() as ctx:
        ctx.prec = 70
        values = [(s0, g_decimal(s0)) for s0 in range(2, 51)]
        target = g_decimal(4)
        hits = [s0 for s0, value in values if abs(value - target) < Decimal("1e-50")]
        monotone = all(values[i + 1][1] > values[i][1] for i in range(len(values) - 1))
    check(
        mode,
        "numerical",
        "high-precision integer sweep supports monotonicity and the unique s=4 hit",
        monotone and hits == [4],
        detail=f"sweep=2..50, hits={hits}, g(50)={values[-1][1]}",
    )


def independent_mode() -> None:
    mode = "independent"
    section("INDEPENDENT")

    s = sp.symbols("s", real=True)
    x = sp.Pow(2, 1 - s)
    log_g = sp.log(1 - x) / s
    derivative_certificate = (
        s * sp.log(2) * x / (1 - x) - sp.log(1 - x)
    ) / s**2
    derivative_residual = sp.simplify(sp.diff(log_g, s) - derivative_certificate)
    x_symbol = sp.symbols("x", real=True)
    rational_term_domain = sp.solve_univariate_inequality(
        x_symbol / (1 - x_symbol) > 0, x_symbol, relational=False
    )
    logarithm_term_domain = sp.solve_univariate_inequality(
        -sp.log(1 - x_symbol) > 0, x_symbol, relational=False
    )
    x_below_one_domain = sp.solve_univariate_inequality(
        x < 1, s, relational=False
    )
    x_positive_domain = sp.solve_univariate_inequality(
        x > 0, s, relational=False
    )
    check(
        mode,
        "theorem",
        "independent derivative is strictly positive on the exact real domain s>1",
        derivative_residual == 0
        and rational_term_domain == sp.Interval.open(0, 1)
        and logarithm_term_domain == sp.Interval.open(0, 1)
        and x_below_one_domain == sp.Interval.open(1, sp.oo)
        and x_positive_domain == sp.S.Reals,
        detail=(
            f"formula residual={derivative_residual}; x/(1-x)>0 and -log(1-x)>0 "
            f"on {rational_term_domain}; 0<x<1 exactly when s>1"
        ),
    )

    derivative_samples = [
        sp.N(derivative_certificate.subs(s, q), 50)
        for q in (sp.Rational(1001, 1000), 2, 3, 4, 10, 100)
    ]
    check(
        mode,
        "numerical",
        "derivative samples support but do not carry the real-domain proof",
        all(value > 0 for value in derivative_samples),
        detail=f"sampled minimum={min(derivative_samples)}",
    )

    brackets = {s0: eta_zeta_ratio_bracket(s0, 200) for s0 in range(2, 9)}
    contained = all(lo <= closed_ratio(s0) <= hi for s0, (lo, hi) in brackets.items())
    widths = {s0: float(hi - lo) for s0, (lo, hi) in brackets.items()}
    check(
        mode,
        "numerical",
        "independent rigorous eta/zeta partial-sum brackets contain every exact ratio",
        contained and max(widths.values()) < 2e-4,
        detail=f"s=2..8, max width={max(widths.values()):.3e}",
    )

    d = sp.symbols("d", positive=True)
    p = sp.symbols("p", real=True)
    lam = sp.symbols("lambda", positive=True)
    covariance_residual = sp.simplify(sp.Pow(lam, d * p) / lam - 1)
    solved_residual = sp.simplify(covariance_residual.subs(p, 1 / d))
    check(
        mode,
        "theorem",
        "unit-rescaling covariance lambda^(d*p)=lambda vanishes exactly at p=1/d",
        solved_residual == 0 and sp.solve(sp.Eq(d * p, 1), p) == [1 / d],
        detail=f"covariance residual={covariance_residual}; solved={solved_residual}",
    )

    q = sp.symbols("q", real=True)
    dimensionful_solutions = sp.solve(sp.Eq(q + d * p, 1), p)
    check(
        mode,
        "boundary",
        "a coefficient of mass dimension q changes the exponent outside the stated map class",
        dimensionful_solutions == [(1 - q) / d]
        and sp.simplify(dimensionful_solutions[0].subs(q, 0) - 1 / d) == 0
        and sp.simplify(dimensionful_solutions[0].subs(q, sp.Rational(1, 2)) - 1 / (2 * d)) == 0,
        detail=f"q+d*p=1 gives p={dimensionful_solutions}",
    )

    exact_rescalings = []
    for d0 in (1, 2, 3, 4, 7, 8):
        for lam0 in (sp.Rational(1, 4), sp.Rational(1, 2), 2, 3):
            lhs = sp.Pow(sp.Pow(lam0, d0), sp.Rational(1, d0))
            exact_rescalings.append(sp.simplify(lhs - lam0))
    check(
        mode,
        "conditional",
        "exact positive unit rescalings reproduce M -> lambda M for several d and lambda",
        set(exact_rescalings) == {sp.Integer(0)},
        detail=f"residuals={set(exact_rescalings)}, cases={len(exact_rescalings)}",
    )

    naive_even_root = sp.Pow(-16, sp.Rational(1, 4))
    magnitude_root = sp.Pow(abs(-16), sp.Rational(1, 4))
    odd_signed_root = sp.real_root(-8, 3)
    check(
        mode,
        "boundary",
        "absolute-value route is real nonnegative where naive signed roots are not magnitudes",
        naive_even_root.is_real is False
        and sp.simplify(magnitude_root - 2) == 0
        and odd_signed_root == -2,
        detail=(
            f"(-16)^(1/4)={naive_even_root}; |−16|^(1/4)={magnitude_root}; "
            f"real_root(-8,3)={odd_signed_root}"
        ),
    )


def hostile_mode() -> None:
    mode = "hostile"
    section("HOSTILE")

    invalid_dimensions = [
        ScaleMapCase(d=d0, p=Fraction(1, 4)) for d0 in (0, -1, -4)
    ]
    check(
        mode,
        "boundary",
        "d <= 0 is rejected by the positive mass-dimension theorem domain",
        all(case.issues() == {"invalid_dimension"} for case in invalid_dimensions),
        detail=f"issues={[sorted(case.issues()) for case in invalid_dimensions]}",
    )

    wrong_exponent = ScaleMapCase(d=4, p=Fraction(1, 3))
    check(
        mode,
        "boundary",
        "p != 1/d produces a nonzero dimension residual",
        wrong_exponent.dimension_residual() == Fraction(1, 3)
        and {"wrong_exponent", "dimension_covariance_failure"}
        <= wrong_exponent.issues(),
        detail=(
            f"residual={wrong_exponent.dimension_residual()}, "
            f"issues={sorted(wrong_exponent.issues())}"
        ),
    )

    dimensionful_kappa = ScaleMapCase(
        d=4,
        p=Fraction(1, 4),
        kappa_mass_dimension=Fraction(1, 2),
    )
    check(
        mode,
        "boundary",
        "a dimensionful kappa violates the stated dimensionless-coefficient map class",
        dimensionful_kappa.dimension_residual() == Fraction(1, 2)
        and "dimensionful_kappa" in dimensionful_kappa.issues()
        and "dimension_covariance_failure" in dimensionful_kappa.issues(),
        detail=(
            f"residual={dimensionful_kappa.dimension_residual()}, "
            f"issues={sorted(dimensionful_kappa.issues())}"
        ),
    )

    negative_even = ScaleMapCase(
        d=4,
        p=Fraction(1, 4),
        f=Fraction(-16),
        magnitude_convention=False,
    )
    check(
        mode,
        "boundary",
        "negative f with even d rejects the naive real-positive root",
        "nonreal_even_root" in negative_even.issues(),
        detail=f"issues={sorted(negative_even.issues())}",
    )

    negative_odd = ScaleMapCase(
        d=3,
        p=Fraction(1, 3),
        f=Fraction(-8),
        magnitude_convention=False,
    )
    check(
        mode,
        "boundary",
        "negative f with odd d has a signed root, not a nonnegative magnitude",
        "signed_not_magnitude" in negative_odd.issues()
        and sp.real_root(-8, 3) < 0,
        detail=f"issues={sorted(negative_odd.issues())}, root={sp.real_root(-8, 3)}",
    )

    unit_coefficient = ScaleMapCase(
        d=4,
        p=Fraction(1, 4),
        kappa=Fraction(1),
        kappa_supplied=False,
    )
    check(
        mode,
        "boundary",
        "unit coefficient is rejected when kappa=1 was not supplied",
        "unsupplied_coefficient" in unit_coefficient.issues(),
        detail=f"issues={sorted(unit_coefficient.issues())}",
    )

    alternate_unsupplied = ScaleMapCase(
        d=4,
        p=Fraction(1, 4),
        kappa=Fraction(5, 2),
        kappa_supplied=False,
    )
    check(
        mode,
        "boundary",
        "an alternate coefficient is also rejected when it was not supplied",
        "unsupplied_coefficient" in alternate_unsupplied.issues(),
        detail=f"issues={sorted(alternate_unsupplied.issues())}",
    )

    negative_coefficient = ScaleMapCase(
        d=4,
        p=Fraction(1, 4),
        kappa=Fraction(-1),
    )
    check(
        mode,
        "boundary",
        "a negative coefficient is rejected for a nonnegative magnitude map",
        "negative_magnitude_coefficient" in negative_coefficient.issues()
        and negative_coefficient.magnitude_value() < 0,
        detail=f"issues={sorted(negative_coefficient.issues())}",
    )

    challenged_power = ScaleMapCase(
        d=4,
        p=Fraction(1, 3),
        f=Fraction(81),
    )
    check(
        mode,
        "boundary",
        "the hostile evaluator preserves a challenged exponent instead of hard-coding 1/d",
        sp.simplify(challenged_power.magnitude_value() - sp.real_root(81, 3)) == 0
        and challenged_power.magnitude_value() != 3,
        detail=f"M={challenged_power.magnitude_value()}",
    )

    condition_witnesses = {
        "coefficient": ScaleMapCase(
            d=4,
            p=Fraction(1, 4),
            kappa=Fraction(3, 2),
            f=None,
            magnitude_convention=False,
            kappa_supplied=True,
            carrier_supplied=False,
        ),
        "magnitude_convention": ScaleMapCase(
            d=4,
            p=Fraction(1, 4),
            f=None,
            magnitude_convention=True,
            kappa_supplied=False,
            carrier_supplied=False,
        ),
        "carrier": ScaleMapCase(
            d=4,
            p=Fraction(1, 4),
            f=None,
            magnitude_convention=False,
            kappa_supplied=False,
            carrier_supplied=True,
        ),
        "value": ScaleMapCase(
            d=4,
            p=Fraction(1, 4),
            f=Fraction(16),
            magnitude_convention=False,
            kappa_supplied=False,
            carrier_supplied=False,
        ),
    }
    check(
        mode,
        "boundary",
        "singleton witnesses refute every directed implication among the four supplied conditions",
        all(
            case.supplied_conditions() == {name}
            for name, case in condition_witnesses.items()
        ),
        detail=(
            "witnesses="
            + str(
                {
                    name: sorted(case.supplied_conditions())
                    for name, case in condition_witnesses.items()
                }
            )
        ),
    )

    physical_inference = ScaleMapCase(
        d=4,
        p=Fraction(1, 4),
        f=None,
        carrier_supplied=False,
        infer_physical_value=True,
    )
    check(
        mode,
        "boundary",
        "physical-value inference is rejected without a carrier and value for f",
        "unsupported_physical_inference" in physical_inference.issues(),
        detail=f"issues={sorted(physical_inference.issues())}",
    )

    zero_map_covariance = []
    for p0 in (sp.Rational(1, 7), sp.Rational(1, 4), sp.Rational(3, 2)):
        for lam0 in (sp.Rational(1, 2), 2, 5):
            lhs = 0 * sp.Pow(sp.Pow(lam0, 4) * 16, p0)
            rhs = lam0 * 0 * sp.Pow(16, p0)
            zero_map_covariance.append(sp.simplify(lhs - rhs))
    check(
        mode,
        "boundary",
        "kappa=0 is covariant for multiple wrong exponents and cannot witness exponent uniqueness",
        set(zero_map_covariance) == {sp.Integer(0)},
        detail=f"tested residuals={set(zero_map_covariance)}, cases={len(zero_map_covariance)}",
    )


def hygiene_mode() -> None:
    mode = "hygiene"
    section("HYGIENE")

    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.exists() else ""
    claim_types = re.findall(
        r"^\*\*(?:Claim type|Type):\*\*\s*([a-z_]+)\s*$",
        note_text,
        flags=re.MULTILINE,
    )
    check(
        mode,
        "hygiene",
        "source note has one explicit positive_theorem author hint",
        claim_types == ["positive_theorem"],
        detail=f"parsed claim types={claim_types}",
        klass="B",
    )

    premise_history = (
        json.loads(PREMISE_HISTORY_PATH.read_text(encoding="utf-8"))
        if PREMISE_HISTORY_PATH.exists()
        else {}
    )
    conventions = premise_history.get("conventions", {})
    scale_text = (
        SCALE_REFERENCE_PATH.read_text(encoding="utf-8")
        if SCALE_REFERENCE_PATH.exists()
        else ""
    )
    check(
        mode,
        "hygiene",
        "cross-cycle echoes are provenance-only conventions or a units-only primitive",
        premise_history.get("genuine_admitted_input_count") == 0
        and "Non-authoritative" in premise_history.get("description", "")
        and conventions.get("hypercharge_identification_note", {}).get("class")
        == "vacuous normalization convention"
        and "vacuous rescaling convention"
        in conventions.get("g_bare_rigidity_theorem_note", {}).get("class", "")
        and re.search(r"zero\s+dimensionless\s+content", scale_text) is not None,
        detail="Y0/g0 are provenance-only; scale reference is units-only",
        klass="B",
    )

    n2_match = re.search(
        r"### Condition independence \(No-Go Discipline N2\)(.*?)"
        r"### Hidden-condition scan \(No-Go Discipline N3\)",
        note_text,
        flags=re.DOTALL,
    )
    condition_names = {"coefficient", "sign/magnitude convention", "carrier", "value"}
    n2_pairs = set(
        re.findall(
            r"^\| (coefficient|sign/magnitude convention|carrier|value) "
            r"\| (coefficient|sign/magnitude convention|carrier|value) \|",
            n2_match.group(1) if n2_match else "",
            flags=re.MULTILINE,
        )
    )
    expected_pairs = {
        (source, target)
        for source in condition_names
        for target in condition_names
        if source != target
    }
    no_go_headings = all(
        f"No-Go Discipline N{index}" in note_text for index in range(1, 9)
    )
    check(
        mode,
        "hygiene",
        "N1-N8 packet has current-cycle markers, all directed N2 pairs, and concrete N8 paths",
        no_go_headings
        and note_text.count("`ATTEMPTED`") == 6
        and n2_pairs == expected_pairs
        and "`docs/audit/data/premise_decision_history.json`" in note_text
        and "`docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`" in note_text,
        detail=(
            f"headings={no_go_headings}; N1 attempted=6; "
            f"N2 directed pairs={len(n2_pairs)}; N8 paths=2"
        ),
        klass="B",
    )

    links = re.findall(r"\]\(([^)]+)\)", note_text)
    local_links = [link for link in links if not re.match(r"^[a-z]+://", link)]
    resolved = [
        (NOTE_PATH.parent / link).resolve().is_file()
        for link in local_links
    ]
    check(
        mode,
        "hygiene",
        "every local markdown link in the source note resolves to a file",
        bool(local_links) and all(resolved),
        detail=f"local links={local_links}",
        klass="B",
    )

    bare_map_hits = re.findall(r"M\s*=\s*f\^\(1/d\)", note_text)
    unique_map_hits = re.findall(r"unique\s+(?:simple-power\s+)?(?:inverse\s+)?map", note_text, re.I)
    check(
        mode,
        "hygiene",
        "source note contains no bare M=f^(1/d) or unique-map normalization overread",
        not bare_map_hits and not unique_map_hits,
        detail=f"bare-map hits={len(bare_map_hits)}, unique-map hits={len(unique_map_hits)}",
        klass="B",
    )

    forbidden_inferences = {
        "unique_unit_normalization": re.findall(r"unique unit normalization", note_text, re.I),
        "physical_mass_prediction": re.findall(r"is a physical mass prediction", note_text, re.I),
        "dimensions_select_kappa": re.findall(r"dimensions? (?:fix|select)s? kappa", note_text, re.I),
    }
    inference_hit_counts = {
        name: len(hits) for name, hits in forbidden_inferences.items()
    }
    check(
        mode,
        "hygiene",
        "source rhetoric does not promote coefficient, physical-value, or empirical authority",
        all(not hits for hits in forbidden_inferences.values()),
        detail=f"hits={inference_hit_counts}",
        klass="B",
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
    print(f"mode={args.mode};eta/zeta exact;dimensional exponent only")
    print("TAGS: " + " ".join(f"{v}={k}" for k, v in EVIDENCE_TAGS.items()))

    if args.mode in ("normal", "all"):
        normal_mode()
    if args.mode in ("independent", "all"):
        independent_mode()
    if args.mode in ("hostile", "all"):
        hostile_mode()
    hygiene_mode()

    print(
        "EVIDENCE: "
        + " ".join(
            f"{name}={EVIDENCE_COUNTS[name]}"
            for name in ("theorem", "conditional", "numerical", "boundary", "hygiene")
        )
    )
    print(
        "CLASSES: "
        + " ".join(f"{name}={CLASS_COUNTS[name]}" for name in ("A", "B", "C", "D"))
    )
    print("MODES: " + " ".join(f"{name}={count}" for name, count in sorted(MODE_COUNTS.items())))
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
