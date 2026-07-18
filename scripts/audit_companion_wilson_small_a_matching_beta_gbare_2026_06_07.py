#!/usr/bin/env python3
"""Certificate for an abstract Hermitian matrix-trace deficit theorem.

Let n >= 1, let Hermitian matrices T_a satisfy
Tr(T_a T_b)=delta_ab/2, let A=sum_a f_a T_a for real f_a, and define

    D(x) = 1 - Re Tr exp(i x A) / n.

The runner reconstructs the derivatives, quadratic coefficient, global
fourth-order remainder bound, and the coefficient of w D(sx).  Normal,
independent, hostile, and intentional-failure modes provide distinct exact,
numerical, and falsification routes.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Callable

import numpy as np
import sympy as sp


PASS = 0
FAIL = 0


class HypothesisViolation(ValueError):
    """Raised when a matrix packet violates the theorem hypotheses."""


class FormulaMismatch(ValueError):
    """Raised when a recomputed mutation disagrees with the theorem."""


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
    trace_a4: sp.Expr
    d0: sp.Expr
    d1: sp.Expr
    d2: sp.Expr
    quadratic_coefficient: sp.Expr
    complex_linear_coefficient: sp.Expr


FIXTURES = (
    "wrong-gram-factor",
    "omitted-one-over-n",
    "derivative-vs-coefficient",
    "false-remainder-constant",
    "non-hermitian-input",
    "false-complex-linear-zero",
    "wrong-rescaling-power",
    "illicit-target-inference",
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


def one_dimensional_packet() -> MatrixPacket:
    """A valid n=1, nontraceless packet."""
    return MatrixPacket(
        1,
        (sp.Matrix([[1 / sp.sqrt(2)]]),),
        (sp.sqrt(2),),
    )


def diagonal_independent_packet() -> MatrixPacket:
    """An n=4 fixture with repeated, zero, positive, and negative spectrum."""
    t1 = sp.diag(sp.Rational(1, 2), sp.Rational(-1, 2), 0, 0)
    t2 = sp.diag(0, 0, sp.Rational(1, 2), sp.Rational(-1, 2))
    return MatrixPacket(4, (t1, t2), (sp.Integer(2), sp.Integer(2)))


def complex_offdiagonal_packet() -> MatrixPacket:
    """An n=4 packet with genuinely complex off-diagonal entries."""
    real = sp.zeros(4)
    real[0, 3] = real[3, 0] = sp.Rational(1, 2)
    imag = sp.zeros(4)
    imag[0, 3] = -sp.I / 2
    imag[3, 0] = sp.I / 2
    return MatrixPacket(4, (real, imag), (sp.Integer(2), sp.Integer(-3)))


def validate_packet(packet: MatrixPacket) -> None:
    """Enforce exactly the hypotheses used by the theorem."""
    n = packet.dimension
    if n < 1:
        raise HypothesisViolation("dimension n must be positive")
    if len(packet.generators) != len(packet.coefficients):
        raise HypothesisViolation("generator and coefficient counts differ")
    for index, generator in enumerate(packet.generators):
        if generator.shape != (n, n):
            raise HypothesisViolation(f"T_{index} has the wrong dimension")
        if not matrix_equal(generator, generator.conjugate().T):
            raise HypothesisViolation(f"T_{index} is not Hermitian")
    for index, coefficient in enumerate(packet.coefficients):
        if sp.simplify(coefficient).is_real is not True:
            raise HypothesisViolation(
                f"f_{index} is not a provably real coefficient"
            )
    gram = sp.Matrix(
        [
            [sp.simplify(sp.trace(left * right)) for right in packet.generators]
            for left in packet.generators
        ]
    )
    expected = sp.eye(len(packet.generators)) / 2
    if not matrix_equal(gram, expected):
        raise HypothesisViolation(f"trace Gram is {gram}, expected delta_ab/2")


def packet_hypotheses_hold(packet: MatrixPacket) -> bool:
    try:
        validate_packet(packet)
    except HypothesisViolation:
        return False
    return packet.dimension >= 1 and len(packet.generators) == len(packet.coefficients)


def matrix_from_packet(packet: MatrixPacket) -> sp.Matrix:
    out = sp.zeros(packet.dimension)
    for coefficient, generator in zip(packet.coefficients, packet.generators):
        out += coefficient * generator
    return out.applyfunc(sp.simplify)


def certify_by_derivatives(packet: MatrixPacket) -> TaylorCertificate:
    """Normal route: exact matrix traces and derivatives at zero."""
    validate_packet(packet)
    n = sp.Integer(packet.dimension)
    matrix_a = matrix_from_packet(packet)
    coefficient_norm = sp.expand(sum(value**2 for value in packet.coefficients))
    trace_a = sp.simplify(sp.trace(matrix_a))
    trace_a2 = sp.expand(sp.trace(matrix_a**2))
    trace_a4 = sp.expand(sp.trace(matrix_a**4))
    # For Z(x)=1-Tr exp(i x A)/n, Z^(k)(0)=-(i^k/n)Tr(A^k).
    # D=Re Z.  Hermiticity makes Tr(A) real, hence Re(-i Tr(A)/n)=0.
    # D(0) is evaluated from the defining deficit at x=0, not assigned.
    zero_exponential = (sp.I * sp.Integer(0) * matrix_a).exp()
    d0 = sp.simplify(1 - sp.re(sp.trace(zero_exponential)) / n)
    d1 = sp.simplify(sp.re(-sp.I * trace_a / n))
    d2 = sp.simplify(sp.re(trace_a2 / n))
    return TaylorCertificate(
        dimension=packet.dimension,
        coefficient_norm=coefficient_norm,
        trace_a=trace_a,
        trace_a2=trace_a2,
        trace_a4=trace_a4,
        d0=d0,
        d1=d1,
        d2=d2,
        quadratic_coefficient=sp.simplify(d2 / 2),
        complex_linear_coefficient=sp.simplify(-sp.I * trace_a / n),
    )


def expect_rejection(
    label: str,
    exception_type: type[Exception],
    operation: Callable[[], object],
    record_check: bool = True,
) -> tuple[bool, str]:
    caught: Exception | None = None
    try:
        operation()
    except Exception as exc:
        caught = exc
    ok = isinstance(caught, exception_type)
    detail = str(caught) if caught is not None else "mutation was accepted"
    if record_check:
        check(label, ok, detail)
    return ok, detail


def formal_rescaled_quadratic_term() -> tuple[sp.Expr, sp.Expr, tuple[sp.Symbol, ...]]:
    """Derive the rescaled x^2 F2 term from D''=Tr(A^2)/n and Tr(A^2)=F2/2."""
    x, f2_symbol, w, s = sp.symbols("x F2 w s", real=True)
    dimension = sp.symbols("n", integer=True, positive=True)
    trace_a2 = sp.symbols("trace_A2", real=True)
    d2_from_trace = trace_a2 / dimension
    quadratic_term = (d2_from_trace / 2) * x**2
    rescaled = sp.expand(w * quadratic_term.subs(x, s * x)).subs(
        trace_a2, f2_symbol / 2
    )
    coefficient = sp.Poly(rescaled, x, f2_symbol).coeff_monomial(x**2 * f2_symbol)
    return rescaled, sp.simplify(coefficient), (x, f2_symbol, w, s, dimension)


def normal_route() -> None:
    section("Part A: exact derivative, Gram, remainder, and rescaling route")
    packet = pauli_packet()
    certificate = certify_by_derivatives(packet)
    n = sp.Integer(packet.dimension)
    expected_trace_a2 = certificate.coefficient_norm / 2
    expected_d2 = certificate.coefficient_norm / (2 * n)
    expected_quadratic = certificate.coefficient_norm / (4 * n)

    check("A1 packet has positive dimension", packet.dimension > 0)
    check("A2 supplied packet satisfies Hermiticity and the half-Gram relation", packet_hypotheses_hold(packet))
    check("A3 assembled A is Hermitian", matrix_equal(matrix_from_packet(packet), matrix_from_packet(packet).conjugate().T))
    check(
        "A4 Gram contraction gives Tr(A^2)=F2/2",
        sp.simplify(certificate.trace_a2 - expected_trace_a2) == 0,
        str(certificate.trace_a2),
    )
    check("A5 D(0)=0", certificate.d0 == 0)
    check("A6 D'(0)=0", certificate.d1 == 0)
    check(
        "A7 D''(0)=Tr(A^2)/n=F2/(2n)",
        sp.simplify(certificate.d2 - expected_d2) == 0,
        str(certificate.d2),
    )
    check(
        "A8 [x^2]D=D''(0)/2=F2/(4n)",
        sp.simplify(certificate.quadratic_coefficient - expected_quadratic) == 0,
        str(certificate.quadratic_coefficient),
    )

    y = sp.symbols("y", real=True)
    scalar_deficit = 1 - sp.cos(y)
    check("A9 the scalar deficit has fourth derivative -cos(y)", sp.diff(scalar_deficit, y, 4) == -sp.cos(y))
    check(
        "A10 the fourth derivative is globally bounded by one on the real line",
        sp.trigsimp(1 - sp.cos(y) ** 2) == sp.sin(y) ** 2
        and sp.ask(sp.Q.nonnegative(sp.sin(y) ** 2)) is True,
        "1-cos(y)^2=sin(y)^2>=0",
    )
    matrix_a = matrix_from_packet(packet)
    eigenvalue_fourth_sum = sum(
        eigenvalue**4 * multiplicity
        for eigenvalue, multiplicity in matrix_a.eigenvals().items()
    )
    check(
        "A11 the spectral fourth moment equals Tr(A^4)",
        sp.simplify(eigenvalue_fourth_sum - certificate.trace_a4) == 0,
    )

    zero_packet = MatrixPacket(
        packet.dimension,
        packet.generators,
        tuple(sp.Integer(0) for _ in packet.coefficients),
    )
    zero_certificate = certify_by_derivatives(zero_packet)
    check(
        "A12 zero A saturates the identities and bound at zero",
        zero_certificate.d2 == 0
        and zero_certificate.quadratic_coefficient == 0
        and zero_certificate.trace_a4 == 0,
    )

    one_packet = one_dimensional_packet()
    one_certificate = certify_by_derivatives(one_packet)
    check("A13 n=1 is allowed when the supplied Gram relation holds", packet_hypotheses_hold(one_packet))
    check(
        "A14 tracelessness is unnecessary for the real deficit derivative",
        one_certificate.trace_a == 1 and one_certificate.d1 == 0,
        f"Tr(A)={one_certificate.trace_a}, D'(0)={one_certificate.d1}",
    )
    check(
        "A15 the n=1 packet has D''(0)=1 and [x^2]D=1/2",
        one_certificate.d2 == 1 and one_certificate.quadratic_coefficient == sp.Rational(1, 2),
    )
    check(
        "A16 its complex deficit retains the nonzero linear coefficient -i",
        one_certificate.complex_linear_coefficient == -sp.I,
        str(one_certificate.complex_linear_coefficient),
    )

    rescaled_term, native, formal_symbols = formal_rescaled_quadratic_term()
    _, _, w, s, dimension = formal_symbols
    check(
        "A17 extracting x^2*F2 after substitution in w D(sx) gives w*s^2/(4n)",
        sp.simplify(native - w * s**2 / (4 * dimension)) == 0,
        f"term={rescaled_term}, coefficient={native}",
    )
    check(
        "A18 scalar rescaling is quadratic in s",
        sp.simplify(native.subs(s, 3 * s) - 9 * native) == 0,
    )


def independent_route() -> None:
    section("Part B: independent spectral power-series and numerical route")
    packet = diagonal_independent_packet()
    validate_packet(packet)
    matrix_a = matrix_from_packet(packet)
    spectrum = matrix_a.eigenvals()
    x = sp.symbols("x", real=True)

    # Read the spectrum directly.  This route does not call the normal
    # derivative certificate or import its expected-value table.
    spectral_d = 1 - sum(
        multiplicity * sp.cos(x * eigenvalue)
        for eigenvalue, multiplicity in spectrum.items()
    ) / packet.dimension
    series = sp.series(spectral_d, x, 0, 6).removeO().expand()
    trace_a2 = sp.trace(matrix_a**2)
    trace_a4 = sp.trace(matrix_a**4)

    check("B1 independent packet satisfies the supplied hypotheses", packet_hypotheses_hold(packet))
    check(
        "B2 spectrum contains repeated positive/negative eigenvalues and no missing multiplicity",
        spectrum == {sp.Integer(1): 2, sp.Integer(-1): 2},
        str(spectrum),
    )
    check("B3 spectral formula gives D(0)=0", spectral_d.subs(x, 0) == 0)
    check("B4 spectral formula gives D'(0)=0", sp.diff(spectral_d, x).subs(x, 0) == 0)
    check("B5 direct spectrum gives D''(0)=1", sp.diff(spectral_d, x, 2).subs(x, 0) == 1)
    check("B6 direct power series gives [x^2]D=1/2", series.coeff(x, 2) == sp.Rational(1, 2), str(series))
    check("B7 direct power series gives [x^4]D=-1/24", series.coeff(x, 4) == -sp.Rational(1, 24))
    check("B8 spectrum reconstructs Tr(A^2)=4", trace_a2 == 4)
    check("B9 spectrum reconstructs Tr(A^4)=4", trace_a4 == 4)
    check(
        "B10 signed fourth coefficient reaches -Tr(A^4)/(24n)",
        series.coeff(x, 4) == -trace_a4 / (24 * packet.dimension),
    )

    # Rank-deficient, repeated-zero, and negative-eigenvalue case.
    rank_packet = MatrixPacket(4, packet.generators, (sp.Integer(2), sp.Integer(0)))
    validate_packet(rank_packet)
    rank_a = matrix_from_packet(rank_packet)
    rank_spectrum = rank_a.eigenvals()
    check(
        "B11 rank-deficient spectrum keeps repeated zeros and both signs",
        rank_spectrum == {sp.Integer(1): 1, sp.Integer(-1): 1, sp.Integer(0): 2},
        str(rank_spectrum),
    )

    # Genuinely complex-off-diagonal Hermitian packet, reconstructed with
    # NumPy eigenvalues and scalar cosine rather than SymPy derivatives.
    complex_packet = complex_offdiagonal_packet()
    validate_packet(complex_packet)
    complex_a_sp = matrix_from_packet(complex_packet)
    complex_a = np.array(complex_a_sp.tolist(), dtype=complex)
    eigenvalues = np.linalg.eigvalsh(complex_a)
    f2 = float(sum(float(value) ** 2 for value in complex_packet.coefficients))
    check(
        "B12 complex-off-diagonal A is Hermitian and non-real",
        np.linalg.norm(complex_a - complex_a.conj().T) < 1e-14
        and np.linalg.norm(complex_a.imag) > 1.0,
    )
    check(
        "B13 numerical spectrum is {-sqrt(13)/2,0,0,+sqrt(13)/2}",
        np.allclose(eigenvalues, [-np.sqrt(13) / 2, 0.0, 0.0, np.sqrt(13) / 2], atol=1e-12),
        str(eigenvalues),
    )
    reconstructions = []
    for h in (1e-2, 1e-3, 1e-4):
        # 1-cos(z)=2 sin^2(z/2) avoids cancellation at small z.
        d_h = float(np.mean(2.0 * np.sin(0.5 * h * eigenvalues) ** 2))
        d_2h = float(np.mean(2.0 * np.sin(h * eigenvalues) ** 2))
        reconstructions.append((16.0 * d_h - d_2h) / (6.0 * h**2))
    expected_d2 = f2 / (2.0 * complex_packet.dimension)
    check(
        "B14 stable finite differences across three step sizes give D''(0)=F2/(2n)",
        max(abs(value - expected_d2) for value in reconstructions) < 3e-9,
        "reconstructed=" + ",".join(f"{value:.12f}" for value in reconstructions),
    )
    fourth_moment = float(np.sum(eigenvalues**4))
    test_points = (-9.0, -2.5, -0.1, 0.0, 0.3, 4.0, 11.0)
    residuals = []
    bounds = []
    for point in test_points:
        d_value = float(np.mean(2.0 * np.sin(0.5 * point * eigenvalues) ** 2))
        residuals.append(abs(d_value - point**2 * float(np.sum(eigenvalues**2)) / (2.0 * complex_packet.dimension)))
        bounds.append(abs(point) ** 4 * fourth_moment / (24.0 * complex_packet.dimension))
    check(
        "B15 global fourth-order bound holds on wide signed numerical points",
        all(residual <= bound + 1e-12 for residual, bound in zip(residuals, bounds)),
        f"max ratio={max((r / b) if b else 0.0 for r, b in zip(residuals, bounds)):.6f}",
    )


def hostile_rejections(record_checks: bool = True) -> dict[str, tuple[bool, str]]:
    """Recompute and reject every named mutation."""
    results: dict[str, tuple[bool, str]] = {}

    def record(name: str, operation: Callable[[], object]) -> None:
        result = expect_rejection(
            f"H reject hostile fixture: {name}",
            (HypothesisViolation, FormulaMismatch),
            operation,
            record_check=record_checks,
        )
        results[name] = result

    pauli = pauli_packet()
    wrong_gram = MatrixPacket(
        dimension=2,
        generators=tuple(sp.sqrt(2) * generator for generator in pauli.generators),
        coefficients=pauli.coefficients,
    )

    def reject_wrong_gram() -> None:
        matrix_a = matrix_from_packet(wrong_gram)
        actual = sp.expand(sp.trace(matrix_a**2))
        f2 = sp.expand(sum(value**2 for value in wrong_gram.coefficients))
        if sp.simplify(actual - f2 / 2) != 0:
            raise FormulaMismatch(f"Gram delta gives Tr(A^2)={actual}, not F2/2")
        validate_packet(wrong_gram)

    record("wrong-gram-factor", reject_wrong_gram)

    canonical = certify_by_derivatives(pauli)

    def reject_omitted_normalization() -> None:
        proposed = canonical.trace_a2
        actual = canonical.trace_a2 / pauli.dimension
        if sp.simplify(proposed - actual) != 0:
            raise FormulaMismatch("omitting 1/n changes D''(0)")

    record("omitted-one-over-n", reject_omitted_normalization)

    def reject_derivative_confusion() -> None:
        proposed = canonical.d2
        actual = canonical.d2 / 2
        if sp.simplify(proposed - actual) != 0:
            raise FormulaMismatch("D''(0) is twice the quadratic Taylor coefficient")

    record("derivative-vs-coefficient", reject_derivative_confusion)

    def reject_false_remainder_constant() -> None:
        y = sp.symbols("y", real=True)
        leading = sp.limit((sp.cos(y) - 1 + y**2 / 2) / y**4, y, 0)
        if leading > sp.Rational(1, 48):
            raise FormulaMismatch(f"exact small-y residual ratio is {leading}, exceeding 1/48")

    record("false-remainder-constant", reject_false_remainder_constant)

    nonhermitian = MatrixPacket(
        1,
        (sp.Matrix([[1 / sp.sqrt(2)]]),),
        (sp.I * sp.sqrt(2),),
    )

    def reject_nonhermitian() -> None:
        matrix_a = matrix_from_packet(nonhermitian)
        d1 = sp.simplify(sp.re(-sp.I * sp.trace(matrix_a)))
        if d1 != 0:
            try:
                validate_packet(nonhermitian)
            except HypothesisViolation as exc:
                raise HypothesisViolation(f"{exc}; recomputed D'(0)={d1}") from exc

    record("non-hermitian-input", reject_nonhermitian)

    def reject_false_complex_linear_zero() -> None:
        certificate = certify_by_derivatives(one_dimensional_packet())
        if certificate.complex_linear_coefficient != 0:
            raise FormulaMismatch(
                "valid nontraceless Hermitian packet has complex linear coefficient "
                f"{certificate.complex_linear_coefficient}"
            )

    record("false-complex-linear-zero", reject_false_complex_linear_zero)

    def reject_wrong_rescaling_power() -> None:
        _, actual, formal_symbols = formal_rescaled_quadratic_term()
        _, _, w, s, n = formal_symbols
        proposed = w * s / (4 * n)
        if sp.simplify(actual - proposed) != 0:
            raise FormulaMismatch("substitution x->s*x is quadratic in s")

    record("wrong-rescaling-power", reject_wrong_rescaling_power)

    def reject_illicit_target_inference() -> None:
        _, actual, formal_symbols = formal_rescaled_quadratic_term()
        _, _, w, _, _ = formal_symbols
        target_1, target_2 = sp.Rational(1, 3), sp.Rational(5, 7)
        solution_1 = sp.solve(sp.Eq(actual, target_1), w)[0]
        solution_2 = sp.solve(sp.Eq(actual, target_2), w)[0]
        if sp.simplify(solution_1 - solution_2) != 0:
            raise FormulaMismatch(
                "native coefficient admits distinct external targets and cannot select one"
            )

    record("illicit-target-inference", reject_illicit_target_inference)
    return results


def run_hostile() -> None:
    section("Part C: hostile mutation controls")
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
    print("ABSTRACT HERMITIAN MATRIX-TRACE DEFICIT CERTIFICATE")
    print("Arithmetic: exact symbolic plus independent numerical reconstruction")
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
        print("VERDICT: native matrix Taylor, global remainder, and rescaling theorem verified.")
        return 0
    print("VERDICT: certificate FAILED closed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
