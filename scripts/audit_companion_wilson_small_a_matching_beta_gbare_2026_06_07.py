#!/usr/bin/env python3
"""Exact certificate for a defined matrix-trace Taylor theorem.

Let n >= 2, let Hermitian traceless matrices T_a satisfy
Tr(T_a T_b)=delta_ab/2, let A=sum_a f_a T_a for real f_a, and define

    D(x) = 1 - Re Tr exp(i x A) / n.

This module certifies D(0)=D'(0)=0,
D''(0)=Tr(A^2)/n=sum_a f_a^2/(2n), and the x^2 coefficient
sum_a f_a^2/(4n).  For formal positive beta and g it also certifies

    beta*g^2/(4n) = 1/2  <=>  beta*g^2 = 2n.

No physical action, plaquette, continuum, gauge-field, or coupling
identification is inferred.  Modes ``normal``, ``independent``, ``hostile``,
and ``intentional-failure`` provide distinct proof and falsification routes.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from typing import Callable

import sympy as sp


PASS = 0
FAIL = 0


class HypothesisViolation(ValueError):
    """Raised when a matrix packet violates the theorem hypotheses."""


class CoefficientMismatch(ValueError):
    """Raised when a proposed coefficient identity is not the theorem's."""


class PhysicalInferenceError(ValueError):
    """Raised when formal algebra is asked to make a physical inference."""


@dataclass(frozen=True)
class MatrixPacket:
    dimension: int
    generators: tuple[sp.Matrix, ...]
    coefficients: tuple[sp.Expr, ...]


@dataclass(frozen=True)
class TaylorCertificate:
    dimension: int
    coefficient_norm: sp.Expr
    trace_a: sp.Expr
    trace_a2: sp.Expr
    d0: sp.Expr
    d1: sp.Expr
    d2: sp.Expr
    quadratic_coefficient: sp.Expr
    complex_linear_coefficient: sp.Expr


FIXTURES = (
    "wrong-trace-normalization",
    "nontraceless-linear-term",
    "wrong-one-over-n",
    "wrong-second-derivative-half",
    "wrong-quarter-vs-half",
    "beta-g2-equals-n",
    "beta-equals-2n-over-g",
    "wrong-remainder-constant",
    "illicit-physical-inference",
)


def check(label: str, condition: object, detail: str = "") -> bool:
    """Record one computed assertion."""
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        status = "PASS (A)"
    else:
        FAIL += 1
        status = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")
    return ok


def section(title: str) -> None:
    print()
    print("-" * 96)
    print(title)
    print("-" * 96)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(left[row, col] - right[row, col]) == 0
        for row in range(left.rows)
        for col in range(left.cols)
    )


def pauli_packet() -> MatrixPacket:
    """A noncommuting exact packet with symbolic real coefficients."""
    f1, f2, f3 = sp.symbols("f1 f2 f3", real=True)
    generators = (
        sp.Matrix([[0, 1], [1, 0]]) / 2,
        sp.Matrix([[0, -sp.I], [sp.I, 0]]) / 2,
        sp.Matrix([[1, 0], [0, -1]]) / 2,
    )
    return MatrixPacket(2, generators, (f1, f2, f3))


def diagonal_independent_packet() -> MatrixPacket:
    """A separate n=3 spectral fixture, not constructed from Pauli matrices."""
    generator = sp.diag(sp.Rational(1, 2), sp.Rational(-1, 2), 0)
    return MatrixPacket(3, (generator,), (sp.Integer(1),))


def complex_offdiagonal_packet() -> MatrixPacket:
    """An independent n=4 packet with two complex off-diagonal generators."""
    real = sp.zeros(4)
    real[0, 3] = real[3, 0] = sp.Rational(1, 2)
    imag = sp.zeros(4)
    imag[0, 3] = -sp.I / 2
    imag[3, 0] = sp.I / 2
    return MatrixPacket(4, (real, imag), (sp.Integer(2), sp.Integer(-3)))


def validate_packet(packet: MatrixPacket) -> None:
    """Enforce exactly the algebraic hypotheses appearing in the theorem."""
    n = packet.dimension
    if n < 2:
        raise HypothesisViolation("dimension n must be at least two")
    if len(packet.generators) != len(packet.coefficients):
        raise HypothesisViolation("generator and coefficient counts differ")
    for index, generator in enumerate(packet.generators):
        if generator.shape != (n, n):
            raise HypothesisViolation(f"T_{index} has the wrong dimension")
        if not matrix_equal(generator, generator.conjugate().T):
            raise HypothesisViolation(f"T_{index} is not Hermitian")
        if sp.simplify(sp.trace(generator)) != 0:
            raise HypothesisViolation(f"T_{index} is not traceless")
    gram = sp.Matrix(
        [
            [sp.simplify(sp.trace(left * right)) for right in packet.generators]
            for left in packet.generators
        ]
    )
    expected = sp.eye(len(packet.generators)) / 2
    if not matrix_equal(gram, expected):
        raise HypothesisViolation(
            f"trace Gram is {gram}, expected delta_ab/2"
        )


def packet_hypotheses_hold(packet: MatrixPacket) -> bool:
    """Boolean wrapper used only after the exception route is available."""
    try:
        validate_packet(packet)
    except HypothesisViolation:
        return False
    return (
        packet.dimension >= 2
        and len(packet.generators) == len(packet.coefficients)
    )


def matrix_from_packet(packet: MatrixPacket) -> sp.Matrix:
    out = sp.zeros(packet.dimension)
    for coefficient, generator in zip(packet.coefficients, packet.generators):
        out += coefficient * generator
    return out.applyfunc(sp.simplify)


def certify_by_derivatives(packet: MatrixPacket) -> TaylorCertificate:
    """Normal route: exact matrix traces and derivatives at x=0."""
    validate_packet(packet)
    n = sp.Integer(packet.dimension)
    matrix_a = matrix_from_packet(packet)
    coefficient_norm = sp.expand(sum(value**2 for value in packet.coefficients))
    trace_a = sp.simplify(sp.trace(matrix_a))
    trace_a2 = sp.expand(sp.trace(matrix_a**2))

    # For Z(x)=1-Tr exp(i x A)/n, Z^(k)(0)=-(i^k/n)Tr(A^k).
    # D=Re Z.  Hermiticity makes Tr(A) real, hence Re(-i Tr(A)/n)=0.
    d0 = sp.Integer(0)
    d1 = sp.simplify(sp.re(-sp.I * trace_a / n))
    d2 = sp.simplify(sp.re(sp.trace(matrix_a**2) / n))
    quadratic = sp.simplify(d2 / 2)
    complex_linear = sp.simplify(-sp.I * trace_a / n)
    return TaylorCertificate(
        dimension=packet.dimension,
        coefficient_norm=coefficient_norm,
        trace_a=trace_a,
        trace_a2=trace_a2,
        d0=d0,
        d1=d1,
        d2=d2,
        quadratic_coefficient=quadratic,
        complex_linear_coefficient=complex_linear,
    )


def formal_coefficient_residual(
    beta: sp.Expr, g: sp.Expr, n: sp.Expr, right: sp.Expr = sp.Rational(1, 2)
) -> sp.Expr:
    return sp.factor(beta * g**2 / (4 * n) - right)


def require_canonical_coefficient_equation(
    beta: sp.Expr,
    g: sp.Expr,
    n: sp.Expr,
    proposed_product: sp.Expr,
    proposed_beta: sp.Expr,
    right: sp.Expr = sp.Rational(1, 2),
) -> None:
    """Reject altered coefficient, product, or solved-beta formulas."""
    canonical_product = 2 * n
    canonical_beta = 2 * n / g**2
    reasons: list[str] = []
    if sp.simplify(right - sp.Rational(1, 2)) != 0:
        reasons.append("C_right is not 1/2")
    if sp.simplify(proposed_product - canonical_product) != 0:
        reasons.append("proposed beta*g^2 product is not 2n")
    if sp.simplify(proposed_beta - canonical_beta) != 0:
        reasons.append("proposed beta solution is not 2n/g^2")
    if reasons:
        raise CoefficientMismatch("; ".join(reasons))
    residual = formal_coefficient_residual(
        proposed_beta, g, n, right=right
    )
    if sp.simplify(residual) != 0:
        raise CoefficientMismatch("proposed formulas do not zero the residual")


def infer_physical_meaning(label: str) -> None:
    """Fail closed: no physical dictionary is part of the theorem packet."""
    raise PhysicalInferenceError(
        f"formal coefficient certificate cannot infer physical label {label!r}"
    )


def expect_rejection(
    label: str,
    exception_type: type[Exception],
    operation: Callable[[], object],
) -> tuple[bool, str]:
    caught: Exception | None = None
    try:
        operation()
    except Exception as exc:  # exact type checked below
        caught = exc
    ok = isinstance(caught, exception_type)
    detail = str(caught) if caught is not None else "mutation was accepted"
    check(label, ok, detail)
    return ok, detail


def normal_route() -> None:
    section("Part A: normal exact derivative and Gram-contraction route")
    packet = pauli_packet()
    certificate = certify_by_derivatives(packet)
    n = sp.Integer(packet.dimension)
    expected_trace_a2 = certificate.coefficient_norm / 2
    expected_d2 = certificate.coefficient_norm / (2 * n)
    expected_quadratic = certificate.coefficient_norm / (4 * n)

    check("A1 packet dimension is n=2", packet.dimension == 2)
    check("A2 all matrices satisfy the theorem hypotheses", packet_hypotheses_hold(packet))
    check("A3 Tr(A)=0", certificate.trace_a == 0, str(certificate.trace_a))
    check(
        "A4 Gram contraction gives Tr(A^2)=sum f_a^2/2",
        sp.simplify(certificate.trace_a2 - expected_trace_a2) == 0,
        str(certificate.trace_a2),
    )
    check("A5 D(0)=0", certificate.d0 == 0)
    check("A6 D'(0)=0", certificate.d1 == 0)
    check(
        "A7 D''(0)=sum f_a^2/(2n)",
        sp.simplify(certificate.d2 - expected_d2) == 0,
        str(certificate.d2),
    )
    check(
        "A8 [x^2]D=D''(0)/2=sum f_a^2/(4n)",
        sp.simplify(certificate.quadratic_coefficient - expected_quadratic) == 0,
        str(certificate.quadratic_coefficient),
    )
    check(
        "A9 complex deficit has no linear term on the traceless packet",
        certificate.complex_linear_coefficient == 0,
    )

    y = sp.symbols("y", real=True)
    scalar_deficit = 1 - sp.cos(y)
    check(
        "A10 the scalar deficit has fourth derivative -cos(y)",
        sp.diff(scalar_deficit, y, 4) == -sp.cos(y),
    )
    check(
        "A11 the fourth derivative has absolute value at most one for real y",
        y.is_real is True
        and sp.trigsimp(1 - sp.cos(y) ** 2) == sp.sin(y) ** 2,
        "1-cos(y)^2=sin(y)^2>=0",
    )
    matrix_a = matrix_from_packet(packet)
    eigenvalue_fourth_sum = sum(
        eigenvalue**4 * multiplicity
        for eigenvalue, multiplicity in matrix_a.eigenvals().items()
    )
    check(
        "A12 spectral fourth moment equals Tr(A^4)",
        sp.simplify(eigenvalue_fourth_sum - sp.trace(matrix_a**4)) == 0,
    )

    zero_packet = MatrixPacket(
        packet.dimension,
        packet.generators,
        tuple(sp.Integer(0) for _ in packet.coefficients),
    )
    zero_certificate = certify_by_derivatives(zero_packet)
    check(
        "A13 zero A has zero derivative, quadratic coefficient, and fourth moment",
        zero_certificate.d2 == 0
        and zero_certificate.quadratic_coefficient == 0
        and sp.trace(matrix_from_packet(zero_packet) ** 4) == 0,
    )

    beta, g, dimension = sp.symbols("beta g n", positive=True)
    residual = formal_coefficient_residual(beta, g, dimension)
    check(
        "A14 coefficient residual factors as (beta*g^2-2n)/(4n)",
        sp.simplify(residual - (beta * g**2 - 2 * dimension) / (4 * dimension)) == 0,
        str(residual),
    )
    solved = sp.solve(sp.Eq(residual, 0), beta)
    check(
        "A15 coefficient equality solves uniquely to beta=2n/g^2",
        len(solved) == 1 and sp.simplify(solved[0] - 2 * dimension / g**2) == 0,
        str(solved),
    )
    require_canonical_coefficient_equation(
        beta=2 * dimension / g**2,
        g=g,
        n=dimension,
        proposed_product=2 * dimension,
        proposed_beta=2 * dimension / g**2,
    )
    canonical_residual = formal_coefficient_residual(
        2 * dimension / g**2, g, dimension
    )
    check(
        "A16 canonical coefficient packet has zero exact residual",
        sp.simplify(canonical_residual) == 0,
        str(canonical_residual),
    )


def independent_route() -> None:
    section("Part B: independent spectral and power-series route")
    packet = diagonal_independent_packet()
    validate_packet(packet)
    certificate = certify_by_derivatives(packet)
    x = sp.symbols("x", real=True)
    # The spectrum is read directly from the independently supplied diagonal
    # matrix: {1/2,-1/2,0}.  Hence D=2(1-cos(x/2))/3.
    spectral_d = sp.Rational(2, 3) * (1 - sp.cos(x / 2))
    series = sp.series(spectral_d, x, 0, 6).removeO().expand()
    x2 = sp.expand(series).coeff(x, 2)
    x4 = sp.expand(series).coeff(x, 4)
    expected_x2 = sp.Rational(1, 12)
    expected_x4 = -sp.Rational(1, 576)
    check("B1 independent packet satisfies all hypotheses", packet_hypotheses_hold(packet))
    check(
        "B2 spectrum is exactly {1/2,-1/2,0}",
        matrix_from_packet(packet).eigenvals()
        == {sp.Rational(1, 2): 1, sp.Rational(-1, 2): 1, sp.Integer(0): 1},
    )
    check("B3 spectral formula gives D(0)=0", spectral_d.subs(x, 0) == 0)
    check("B4 spectral formula gives D'(0)=0", sp.diff(spectral_d, x).subs(x, 0) == 0)
    check(
        "B5 spectral formula gives D''(0)=1/6",
        sp.diff(spectral_d, x, 2).subs(x, 0) == sp.Rational(1, 6),
    )
    check("B6 independent x^2 coefficient is 1/12", x2 == expected_x2, str(series))
    check("B7 independent x^4 coefficient is -1/576", x4 == expected_x4, str(series))
    check(
        "B8 matrix-derivative and spectral routes agree on D''(0)",
        certificate.d2 == sp.Rational(1, 6),
        str(certificate.d2),
    )
    check(
        "B9 matrix-derivative and power-series routes agree on [x^2]D",
        certificate.quadratic_coefficient == x2,
    )
    # The fourth-order coefficient equals -Tr(A^4)/(24n), which is the
    # signed leading remainder and lies at the universal absolute bound.
    matrix_a = matrix_from_packet(packet)
    remainder_x4 = -sp.trace(matrix_a**4) / (24 * packet.dimension)
    check("B10 x^4 coefficient equals -Tr(A^4)/(24n)", x4 == remainder_x4)

    complex_packet = complex_offdiagonal_packet()
    validate_packet(complex_packet)
    complex_a = matrix_from_packet(complex_packet)
    complex_spectrum = complex_a.eigenvals()
    check(
        "B11 independent n=4 complex off-diagonal packet satisfies all hypotheses",
        packet_hypotheses_hold(complex_packet),
    )
    check(
        "B12 n=4 packet spectrum is {+sqrt(13)/2,-sqrt(13)/2,0,0}",
        complex_spectrum
        == {
            sp.sqrt(13) / 2: 1,
            -sp.sqrt(13) / 2: 1,
            sp.Integer(0): 2,
        },
        str(complex_spectrum),
    )
    complex_spectral_d = sp.Rational(1, 2) * (
        1 - sp.cos(sp.sqrt(13) * x / 2)
    )
    complex_series = sp.series(complex_spectral_d, x, 0, 6).removeO().expand()
    complex_certificate = certify_by_derivatives(complex_packet)
    check(
        "B13 n=4 spectral route gives D''(0)=13/8",
        sp.diff(complex_spectral_d, x, 2).subs(x, 0) == sp.Rational(13, 8)
        and complex_certificate.d2 == sp.Rational(13, 8),
    )
    check(
        "B14 n=4 spectral route gives [x^2]D=13/16",
        complex_series.coeff(x, 2) == sp.Rational(13, 16)
        and complex_certificate.quadratic_coefficient == sp.Rational(13, 16),
    )


def hostile_rejections(record_checks: bool = True) -> dict[str, tuple[bool, str]]:
    """Construct and reject every named mutation through substantive residuals."""
    results: dict[str, tuple[bool, str]] = {}

    def record(
        name: str,
        exception_type: type[Exception],
        operation: Callable[[], object],
    ) -> None:
        caught: Exception | None = None
        try:
            operation()
        except Exception as exc:
            caught = exc
        ok = isinstance(caught, exception_type)
        detail = str(caught) if caught is not None else "mutation was accepted"
        results[name] = (ok, detail)
        if record_checks:
            check(f"H reject hostile fixture: {name}", ok, detail)

    pauli = pauli_packet()
    wrong_scale = MatrixPacket(
        dimension=2,
        generators=tuple(2 * generator for generator in pauli.generators),
        coefficients=pauli.coefficients,
    )
    record(
        "wrong-trace-normalization",
        HypothesisViolation,
        lambda: validate_packet(wrong_scale),
    )

    identity_packet = MatrixPacket(
        dimension=2,
        generators=(sp.eye(2) / 2,),
        coefficients=(sp.Integer(1),),
    )
    record(
        "nontraceless-linear-term",
        HypothesisViolation,
        lambda: validate_packet(identity_packet),
    )

    canonical = certify_by_derivatives(pauli)
    wrong_denominator_d2 = sp.simplify(
        canonical.trace_a2 / (pauli.dimension - 1)
    )

    def reject_wrong_denominator() -> None:
        expected = canonical.coefficient_norm / (2 * pauli.dimension)
        if sp.simplify(wrong_denominator_d2 - expected) != 0:
            raise CoefficientMismatch("omitting 1/n changes D''(0)")

    record("wrong-one-over-n", CoefficientMismatch, reject_wrong_denominator)

    def reject_derivative_half_confusion() -> None:
        expected_quadratic = canonical.d2 / 2
        proposed_quadratic = canonical.d2
        if sp.simplify(proposed_quadratic - expected_quadratic) != 0:
            raise CoefficientMismatch("D''(0) was confused with [x^2]D=D''(0)/2")

    record(
        "wrong-second-derivative-half",
        CoefficientMismatch,
        reject_derivative_half_confusion,
    )

    beta, g, n = sp.symbols("beta g n", positive=True)
    record(
        "wrong-quarter-vs-half",
        CoefficientMismatch,
        lambda: require_canonical_coefficient_equation(
            beta=n / g**2,
            g=g,
            n=n,
            proposed_product=n,
            proposed_beta=n / g**2,
            right=sp.Rational(1, 4),
        ),
    )
    record(
        "beta-g2-equals-n",
        CoefficientMismatch,
        lambda: require_canonical_coefficient_equation(
            beta=n / g**2,
            g=g,
            n=n,
            proposed_product=n,
            proposed_beta=n / g**2,
        ),
    )
    record(
        "beta-equals-2n-over-g",
        CoefficientMismatch,
        lambda: require_canonical_coefficient_equation(
            beta=2 * n / g,
            g=g,
            n=n,
            proposed_product=2 * n,
            proposed_beta=2 * n / g,
        ),
    )

    def reject_wrong_remainder_constant() -> None:
        y = sp.symbols("y", real=True)
        # Near zero the absolute scalar residual has leading coefficient 1/24,
        # so replacing the theorem's 1/24 by 1/48 is decisively false.
        leading = sp.limit(
            (sp.cos(y) - 1 + y**2 / 2) / y**4,
            y,
            0,
        )
        if leading > sp.Rational(1, 48):
            raise CoefficientMismatch(
                "the proposed 1/48 remainder constant is below the exact 1/24 limit"
            )

    record(
        "wrong-remainder-constant",
        CoefficientMismatch,
        reject_wrong_remainder_constant,
    )
    record(
        "illicit-physical-inference",
        PhysicalInferenceError,
        lambda: infer_physical_meaning("Wilson/Yang-Mills coupling match"),
    )
    return results


def nontraceless_diagnostic() -> None:
    """Show the precise role of tracelessness without accepting the fixture."""
    section("Part C: nontraceless linear-term diagnostic")
    matrix_a = sp.eye(2) / 2
    n = sp.Integer(2)
    real_d1 = sp.re(-sp.I * sp.trace(matrix_a) / n)
    complex_z1 = -sp.I * sp.trace(matrix_a) / n
    check(
        "C1 Hermiticity alone keeps the real deficit derivative zero",
        sp.simplify(real_d1) == 0,
        str(real_d1),
    )
    check(
        "C2 nontracelessness produces a nonzero complex-deficit linear term",
        sp.simplify(complex_z1) != 0,
        str(complex_z1),
    )


def run_hostile() -> None:
    section("Part D: hostile mutation controls")
    nontraceless_diagnostic()
    hostile_rejections(record_checks=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("normal", "independent", "hostile", "intentional-failure"),
        default="normal",
        help="certificate route (default: normal)",
    )
    parser.add_argument(
        "--inject-failure",
        choices=FIXTURES,
        help="hostile fixture promoted by intentional-failure mode",
    )
    args = parser.parse_args()
    if args.inject_failure and args.mode != "intentional-failure":
        parser.error("--inject-failure requires --mode intentional-failure")
    return args


def main() -> int:
    args = parse_args()
    print("=" * 96)
    print("DEFINED MATRIX-TRACE TAYLOR AND FORMAL COEFFICIENT CERTIFICATE")
    print("Arithmetic: exact SymPy symbolic; no physical dictionary")
    print(f"Mode: {args.mode}")
    print("=" * 96)

    if args.mode == "normal":
        normal_route()
    elif args.mode == "independent":
        independent_route()
    elif args.mode == "hostile":
        run_hostile()
    else:
        fixture = args.inject_failure or FIXTURES[0]
        results = hostile_rejections(record_checks=False)
        rejected, detail = results[fixture]
        section("Intentional failure promotion")
        check(
            f"INTENTIONAL FAILURE fixture promoted: {fixture}",
            not rejected,
            detail=f"rejection was expected and observed: {detail}",
        )

    print()
    print("=" * 96)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 96)
    if FAIL == 0:
        print(
            "VERDICT: exact finite-dimensional Taylor/coefficient theorem "
            "verified; no physical interpretation inferred."
        )
        return 0
    print("VERDICT: certificate FAILED closed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
