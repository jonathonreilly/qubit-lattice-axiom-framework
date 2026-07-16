#!/usr/bin/env python3
"""Exact certificate for a formal two-equation normalization system.

This runner proves only the following implication over ``Fraction`` values:

    n_sym * alpha + n_anti * beta = 0
    q = t + beta / 2

If ``n_sym != 0``, the coefficient matrix has determinant ``n_sym / 2``
and hence a unique solution

    beta = 2 * (q - t)
    alpha = -(n_anti / n_sym) * beta.

The specialization ``(n_sym, n_anti, q, t) = (6, 2, -1, -1/2)`` gives
``(alpha, beta) = (1/3, -1)``.  The symbols and packet are formal theorem
data.  No physical branch, particle, charge, isospin, or hypercharge readout
is inferred by this module.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from typing import Callable


PASS = 0
FAIL = 0


class SingularLinearSystem(ValueError):
    """Raised when a 2x2 system has no unique solution."""


class CertificateMismatch(ValueError):
    """Raised when a mutant is presented as the stated specialization."""


class PhysicalReadoutInference(ValueError):
    """Raised when formal arithmetic is asked to assert a physical bridge."""


@dataclass(frozen=True)
class FormalInputs:
    n_sym: Fraction
    n_anti: Fraction
    q: Fraction
    t: Fraction


@dataclass(frozen=True)
class LinearCertificate:
    matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
    rhs: tuple[Fraction, Fraction]
    determinant: Fraction
    rank: int
    alpha: Fraction
    beta: Fraction
    residuals: tuple[Fraction, Fraction]


@dataclass(frozen=True)
class FormalCertificate:
    inputs: FormalInputs
    linear: LinearCertificate


CANONICAL_INPUTS = FormalInputs(
    n_sym=Fraction(6),
    n_anti=Fraction(2),
    q=Fraction(-1),
    t=Fraction(-1, 2),
)
CANONICAL_ALPHA = Fraction(1, 3)
CANONICAL_BETA = Fraction(-1)


def check(name: str, condition: bool, detail: str = "") -> None:
    """Record one computed assertion."""
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: [A] {name}{suffix}")


def as_fraction(value: Fraction | int) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def solve_exact_2x2(
    matrix: tuple[
        tuple[Fraction | int, Fraction | int],
        tuple[Fraction | int, Fraction | int],
    ],
    rhs: tuple[Fraction | int, Fraction | int],
) -> LinearCertificate:
    """Solve a 2x2 rational system by Cramer's rule and certify residuals."""
    a11, a12 = (as_fraction(value) for value in matrix[0])
    a21, a22 = (as_fraction(value) for value in matrix[1])
    b1, b2 = (as_fraction(value) for value in rhs)
    determinant = a11 * a22 - a12 * a21
    if determinant == 0:
        raise SingularLinearSystem(
            "determinant is zero, so existence/uniqueness is not certified"
        )

    alpha = (b1 * a22 - a12 * b2) / determinant
    beta = (a11 * b2 - b1 * a21) / determinant
    residuals = (
        a11 * alpha + a12 * beta - b1,
        a21 * alpha + a22 * beta - b2,
    )
    return LinearCertificate(
        matrix=((a11, a12), (a21, a22)),
        rhs=(b1, b2),
        determinant=determinant,
        rank=2,
        alpha=alpha,
        beta=beta,
        residuals=residuals,
    )


def solve_formal_system(inputs: FormalInputs) -> FormalCertificate:
    """Build and solve exactly the two equations in the theorem statement."""
    linear = solve_exact_2x2(
        (
            (inputs.n_sym, inputs.n_anti),
            (Fraction(0), Fraction(1, 2)),
        ),
        (Fraction(0), inputs.q - inputs.t),
    )
    return FormalCertificate(inputs=inputs, linear=linear)


def validate_canonical_specialization(
    certificate: FormalCertificate,
) -> FormalCertificate:
    """Reject any changed equation, packet entry, or resulting solution."""
    expected_matrix = (
        (CANONICAL_INPUTS.n_sym, CANONICAL_INPUTS.n_anti),
        (Fraction(0), Fraction(1, 2)),
    )
    expected_rhs = (Fraction(0), CANONICAL_INPUTS.q - CANONICAL_INPUTS.t)
    mismatches: list[str] = []
    if certificate.inputs != CANONICAL_INPUTS:
        mismatches.append("formal input packet changed")
    if certificate.linear.matrix != expected_matrix:
        mismatches.append("equation coefficients or signs changed")
    if certificate.linear.rhs != expected_rhs:
        mismatches.append("charge-minus-isospin sign or values changed")
    if certificate.linear.alpha != CANONICAL_ALPHA:
        mismatches.append("alpha is not 1/3")
    if certificate.linear.beta != CANONICAL_BETA:
        mismatches.append("beta is not -1")
    if mismatches:
        raise CertificateMismatch("; ".join(mismatches))
    return certificate


def infer_physical_readout(
    certificate: FormalCertificate, requested_identification: str
) -> None:
    """Fail closed: physical semantics are outside the formal theorem."""
    raise PhysicalReadoutInference(
        f"cannot infer {requested_identification!r} from formal certificate "
        f"(alpha={certificate.linear.alpha}, beta={certificate.linear.beta})"
    )


def expect_rejection(
    name: str,
    exception_type: type[Exception],
    operation: Callable[[], object],
) -> None:
    """Pass only when a hostile mutation raises the expected exception."""
    caught: Exception | None = None
    try:
        operation()
    except Exception as exc:  # the exact type is checked below
        caught = exc
    detail = str(caught) if caught is not None else "mutation was incorrectly accepted"
    check(name, isinstance(caught, exception_type), detail)


def general_solution_checks() -> None:
    print("\n== Part 1: exact general solution certificate ==")
    inputs = FormalInputs(
        n_sym=Fraction(5),
        n_anti=Fraction(3),
        q=Fraction(7, 4),
        t=Fraction(-1, 4),
    )
    certificate = solve_formal_system(inputs).linear
    expected_beta = 2 * (inputs.q - inputs.t)
    expected_alpha = -(inputs.n_anti / inputs.n_sym) * expected_beta

    check(
        "coefficient matrix is the stated formal system",
        certificate.matrix
        == ((inputs.n_sym, inputs.n_anti), (Fraction(0), Fraction(1, 2))),
        str(certificate.matrix),
    )
    check(
        "determinant equals n_sym/2",
        certificate.determinant == inputs.n_sym / 2,
        str(certificate.determinant),
    )
    check(
        "nonzero determinant certifies rank two and uniqueness",
        certificate.determinant != 0 and certificate.rank == 2,
        f"det={certificate.determinant}, rank={certificate.rank}",
    )
    check(
        "beta equals 2(q-t)",
        certificate.beta == expected_beta,
        str(certificate.beta),
    )
    check(
        "alpha equals -(n_anti/n_sym) beta",
        certificate.alpha == expected_alpha,
        str(certificate.alpha),
    )
    check(
        "both defining equations have zero exact residual",
        certificate.residuals == (Fraction(0), Fraction(0)),
        str(certificate.residuals),
    )


def specialization_checks() -> FormalCertificate:
    print("\n== Part 2: supplied rational specialization ==")
    certificate = validate_canonical_specialization(
        solve_formal_system(CANONICAL_INPUTS)
    )
    linear = certificate.linear
    check(
        "the specialization packet is exactly (6,2,-1,-1/2)",
        certificate.inputs == CANONICAL_INPUTS,
        str(certificate.inputs),
    )
    check(
        "specialized determinant is 3 and the system is unique",
        linear.determinant == Fraction(3) and linear.rank == 2,
        f"det={linear.determinant}, rank={linear.rank}",
    )
    check("specialized beta is -1", linear.beta == CANONICAL_BETA, str(linear.beta))
    check(
        "specialized alpha is 1/3",
        linear.alpha == CANONICAL_ALPHA,
        str(linear.alpha),
    )
    check(
        "specialized equations have zero exact residual",
        linear.residuals == (Fraction(0), Fraction(0)),
        str(linear.residuals),
    )
    return certificate


def hostile_controls(canonical: FormalCertificate) -> None:
    print("\n== Part 3: hostile mutation controls ==")
    expect_rejection(
        "zero n_sym is rejected as non-unique",
        SingularLinearSystem,
        lambda: solve_formal_system(
            FormalInputs(Fraction(0), Fraction(2), Fraction(-1), Fraction(-1, 2))
        ),
    )
    expect_rejection(
        "a generic rank-one 2x2 system is rejected",
        SingularLinearSystem,
        lambda: solve_exact_2x2(((1, 2), (2, 4)), (3, 6)),
    )

    wrong_trace_linear = solve_exact_2x2(
        ((6, -2), (0, Fraction(1, 2))),
        (0, CANONICAL_INPUTS.q - CANONICAL_INPUTS.t),
    )
    expect_rejection(
        "the wrong trace sign is rejected",
        CertificateMismatch,
        lambda: validate_canonical_specialization(
            FormalCertificate(CANONICAL_INPUTS, wrong_trace_linear)
        ),
    )

    wrong_readout_linear = solve_exact_2x2(
        ((6, 2), (0, Fraction(1, 2))),
        (0, CANONICAL_INPUTS.t - CANONICAL_INPUTS.q),
    )
    expect_rejection(
        "the wrong charge-minus-isospin sign is rejected",
        CertificateMismatch,
        lambda: validate_canonical_specialization(
            FormalCertificate(CANONICAL_INPUTS, wrong_readout_linear)
        ),
    )
    expect_rejection(
        "a changed multiplicity packet is rejected",
        CertificateMismatch,
        lambda: validate_canonical_specialization(
            solve_formal_system(
                FormalInputs(Fraction(7), Fraction(2), Fraction(-1), Fraction(-1, 2))
            )
        ),
    )
    expect_rejection(
        "a changed q/t packet is rejected",
        CertificateMismatch,
        lambda: validate_canonical_specialization(
            solve_formal_system(
                FormalInputs(Fraction(6), Fraction(2), Fraction(-1), Fraction(-1, 3))
            )
        ),
    )
    expect_rejection(
        "an illicit physical-readout inference is rejected",
        PhysicalReadoutInference,
        lambda: infer_physical_readout(canonical, "Anti^2 is physical L_L"),
    )


def run_normal() -> int:
    print("FORMAL TWO-EQUATION NORMALIZATION ARITHMETIC")
    general_solution_checks()
    canonical = specialization_checks()
    hostile_controls(canonical)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: exact formal implication verified; the supplied packet "
            "gives beta=-1 and alpha=1/3, with no physical readout inferred."
        )
        return 0
    print("VERDICT: formal arithmetic certificate FAILED.")
    return 1


def run_intentional_failure() -> int:
    """Demonstrate fail-closed behavior with a changed q/t packet."""
    print("INTENTIONAL-FAILURE PROBE")
    mutant = solve_formal_system(
        FormalInputs(Fraction(6), Fraction(2), Fraction(-1), Fraction(-1, 3))
    )
    try:
        validate_canonical_specialization(mutant)
    except CertificateMismatch as exc:
        print(f"INTENTIONAL FAIL: changed packet rejected ({exc})")
        return 1
    print("UNEXPECTED PASS: changed packet was accepted")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--intentional-failure",
        action="store_true",
        help="run a changed-packet probe that must exit nonzero",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return run_intentional_failure() if args.intentional_failure else run_normal()


if __name__ == "__main__":
    raise SystemExit(main())
