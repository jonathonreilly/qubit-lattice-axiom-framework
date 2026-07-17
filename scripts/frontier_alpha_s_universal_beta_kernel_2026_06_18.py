#!/usr/bin/env python3
"""Exact certificate for a defined two-coefficient polynomial vector field.

The objects in this module are formal theorem data.  The module does not infer
QCD, loop, scheme, active-flavour, threshold, or physical-running semantics.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
from fractions import Fraction
from typing import Callable

import sympy as sp


PASS = 0
FAIL = 0


class CertificateMismatch(ValueError):
    """Raised when a mutated packet fails the exact canonical certificate."""


class PhysicalInterpretationError(ValueError):
    """Raised when formal data are asked to supply physical semantics."""


@dataclass(frozen=True)
class KernelPacket:
    """All defining constants for the formal coefficient/vector-field packet."""

    capital_n: Fraction = Fraction(3)
    t_f: Fraction = Fraction(1, 2)
    b0_ca_coefficient: Fraction = Fraction(11, 3)
    b0_tf_coefficient: Fraction = Fraction(4, 3)
    b1_ca2_coefficient: Fraction = Fraction(34, 3)
    b1_cf_coefficient: Fraction = Fraction(4)
    b1_ca_coefficient: Fraction = Fraction(20, 3)
    g_cubic_denominator: Fraction = Fraction(16)
    g_quintic_denominator: Fraction = Fraction(16) ** 2
    alpha_scale: Fraction = Fraction(4)
    alpha_chain_numerator: Fraction = Fraction(1)
    alpha_chain_denominator: Fraction = Fraction(2)
    a_scale: Fraction = Fraction(4)
    b0_sign: Fraction = Fraction(-1)
    b1_sign: Fraction = Fraction(-1)


CANONICAL = KernelPacket()


@dataclass(frozen=True)
class ExactCertificate:
    """Exact symbolic output of one packet."""

    packet: KernelPacket
    c_a: Fraction
    c_f: Fraction
    b0: sp.Expr
    b1: sp.Expr
    v_g: sp.Expr
    induced_alpha: sp.Expr
    expected_alpha: sp.Expr
    induced_a: sp.Expr
    expected_a: sp.Expr


def check(name: str, condition: bool, detail: str = "") -> None:
    """Record one computed condition."""
    global PASS, FAIL
    if condition:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def exact_fraction(value: sp.Expr) -> Fraction:
    """Convert an exact SymPy rational to ``Fraction``."""
    value = sp.cancel(value)
    if not value.is_Rational:
        raise TypeError(f"expected an exact rational, got {value!r}")
    return Fraction(int(value.p), int(value.q))


def build_certificate(packet: KernelPacket = CANONICAL) -> ExactCertificate:
    """Construct the symbolic certificate from the packet definitions."""
    n, g, alpha, a = sp.symbols("n g alpha a", real=True)
    pi = sp.pi

    capital_n = sp.Rational(
        packet.capital_n.numerator, packet.capital_n.denominator
    )
    t_f = sp.Rational(packet.t_f.numerator, packet.t_f.denominator)
    c_a = capital_n
    c_f = (capital_n**2 - 1) / (2 * capital_n)

    b0 = (
        sp.Rational(packet.b0_ca_coefficient.numerator, packet.b0_ca_coefficient.denominator)
        * c_a
        - sp.Rational(packet.b0_tf_coefficient.numerator, packet.b0_tf_coefficient.denominator)
        * t_f
        * n
    )
    b1 = (
        sp.Rational(packet.b1_ca2_coefficient.numerator, packet.b1_ca2_coefficient.denominator)
        * c_a**2
        - sp.Rational(packet.b1_cf_coefficient.numerator, packet.b1_cf_coefficient.denominator)
        * c_f
        * t_f
        * n
        - sp.Rational(packet.b1_ca_coefficient.numerator, packet.b1_ca_coefficient.denominator)
        * c_a
        * t_f
        * n
    )

    sign0 = sp.Rational(packet.b0_sign.numerator, packet.b0_sign.denominator)
    sign1 = sp.Rational(packet.b1_sign.numerator, packet.b1_sign.denominator)
    d3 = sp.Rational(
        packet.g_cubic_denominator.numerator, packet.g_cubic_denominator.denominator
    )
    d5 = sp.Rational(
        packet.g_quintic_denominator.numerator,
        packet.g_quintic_denominator.denominator,
    )
    v_g = sign0 * b0 * g**3 / (d3 * pi**2) + sign1 * b1 * g**5 / (d5 * pi**4)

    alpha_scale = sp.Rational(
        packet.alpha_scale.numerator, packet.alpha_scale.denominator
    )
    chain_num = sp.Rational(
        packet.alpha_chain_numerator.numerator,
        packet.alpha_chain_numerator.denominator,
    )
    chain_den = sp.Rational(
        packet.alpha_chain_denominator.numerator,
        packet.alpha_chain_denominator.denominator,
    )
    alpha_chain = chain_num * g / (chain_den * pi)
    induced_alpha_g = sp.expand(alpha_chain * v_g)
    induced_alpha = sp.expand(
        induced_alpha_g.subs(
            {
                g**6: (alpha_scale * pi * alpha) ** 3,
                g**4: (alpha_scale * pi * alpha) ** 2,
            },
            simultaneous=True,
        )
    )
    expected_alpha = -b0 * alpha**2 / (2 * pi) - b1 * alpha**3 / (8 * pi**2)

    a_scale = sp.Rational(packet.a_scale.numerator, packet.a_scale.denominator)
    induced_a = sp.expand((induced_alpha / (a_scale * pi)).subs(alpha, a_scale * pi * a))
    expected_a = -2 * b0 * a**2 - 2 * b1 * a**3

    return ExactCertificate(
        packet=packet,
        c_a=exact_fraction(c_a),
        c_f=exact_fraction(c_f),
        b0=sp.expand(b0),
        b1=sp.expand(b1),
        v_g=sp.expand(v_g),
        induced_alpha=sp.expand(induced_alpha),
        expected_alpha=sp.expand(expected_alpha),
        induced_a=sp.expand(induced_a),
        expected_a=sp.expand(expected_a),
    )


def validate_canonical(certificate: ExactCertificate) -> ExactCertificate:
    """Require every canonical coefficient and change-of-variable identity."""
    n = sp.symbols("n", real=True)
    errors: list[str] = []
    if certificate.packet != CANONICAL:
        errors.append("defining packet changed")
    if certificate.c_a != Fraction(3):
        errors.append("C_A changed")
    if certificate.c_f != Fraction(4, 3):
        errors.append("C_F changed")
    if sp.cancel(certificate.b0 - (11 - sp.Rational(2, 3) * n)) != 0:
        errors.append("b0 polynomial changed")
    if sp.cancel(certificate.b1 - (102 - sp.Rational(38, 3) * n)) != 0:
        errors.append("b1 polynomial changed")
    if sp.cancel(certificate.induced_alpha - certificate.expected_alpha) != 0:
        errors.append("g-to-alpha chain-rule identity changed")
    if sp.cancel(certificate.induced_a - certificate.expected_a) != 0:
        errors.append("alpha-to-a chain-rule identity changed")
    if errors:
        raise CertificateMismatch("; ".join(errors))
    return certificate


def request_physical_interpretation(label: str) -> None:
    """Fail closed because physical/QFT semantics are absent from the packet."""
    formal_fields = set(KernelPacket.__dataclass_fields__)
    requested_fields = {
        "qcd_origin",
        "scheme_independence",
        "active_flavour_selector",
        "physical_running",
    }
    missing = requested_fields - formal_fields
    if missing:
        raise PhysicalInterpretationError(
            f"cannot infer {label!r}; formal packet lacks {sorted(missing)}"
        )


def expect_rejection(
    name: str,
    exception_type: type[Exception],
    operation: Callable[[], object],
) -> None:
    """Pass only when a hostile operation raises the expected exception."""
    caught: Exception | None = None
    try:
        operation()
    except Exception as exc:  # exact type is checked below
        caught = exc
    check(
        name,
        isinstance(caught, exception_type),
        str(caught) if caught is not None else "mutation was accepted",
    )


def normal_checks() -> int:
    """Prove the packet theorem by exact symbolic identities."""
    n = sp.symbols("n", real=True)
    certificate = validate_canonical(build_certificate())

    print("== Defined coefficient packet ==")
    check("C_A is exactly 3", certificate.c_a == Fraction(3), str(certificate.c_a))
    check("C_F is exactly 4/3", certificate.c_f == Fraction(4, 3), str(certificate.c_f))
    check("b0 simplifies exactly", sp.cancel(certificate.b0 - (11 - sp.Rational(2, 3) * n)) == 0, str(certificate.b0))
    check("b1 simplifies exactly", sp.cancel(certificate.b1 - (102 - sp.Rational(38, 3) * n)) == 0, str(certificate.b1))

    values = {
        ("b0", 6): Fraction(7),
        ("b0", 5): Fraction(23, 3),
        ("b1", 6): Fraction(26),
        ("b1", 5): Fraction(116, 3),
        ("b1", 4): Fraction(154, 3),
        ("b1", 3): Fraction(64),
    }
    for (which, n_value), expected in values.items():
        expression = certificate.b0 if which == "b0" else certificate.b1
        actual = exact_fraction(expression.subs(n, n_value))
        check(f"{which}({n_value}) exact value", actual == expected, str(actual))

    print("\n== Slopes, roots, and signs ==")
    check("b0 unit slope is -2/3", sp.cancel(certificate.b0.subs(n, n + 1) - certificate.b0 + sp.Rational(2, 3)) == 0)
    check("b1 unit slope is -38/3", sp.cancel(certificate.b1.subs(n, n + 1) - certificate.b1 + sp.Rational(38, 3)) == 0)
    check("b0 root is 33/2", sp.solve(certificate.b0, n) == [sp.Rational(33, 2)])
    check("b1 root is 153/19", sp.solve(certificate.b1, n) == [sp.Rational(153, 19)])
    m = sp.symbols("m", integer=True, nonnegative=True)
    b0_tail = sp.expand(certificate.b0.subs(n, 17 + m))
    b1_tail = sp.expand(certificate.b1.subs(n, 9 + m))
    b0_tail_negative = sp.ask(sp.Q.negative(b0_tail))
    b1_tail_negative = sp.ask(sp.Q.negative(b1_tail))
    check(
        "b0 integer sign window",
        all(certificate.b0.subs(n, k) > 0 for k in range(17))
        and bool(b0_tail_negative),
        f"tail={b0_tail}",
    )
    check(
        "b1 integer sign window",
        all(certificate.b1.subs(n, k) > 0 for k in range(9))
        and bool(b1_tail_negative),
        f"tail={b1_tail}",
    )

    print("\n== Defined coordinate identities ==")
    check("g-to-alpha vector-field identity", sp.cancel(certificate.induced_alpha - certificate.expected_alpha) == 0)
    check("alpha-to-a vector-field identity", sp.cancel(certificate.induced_a - certificate.expected_a) == 0)

    print(f"\nSUMMARY: MODE=normal PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


def independent_checks() -> int:
    """Reconstruct the theorem without calling the canonical builder."""
    n, g, alpha, a = sp.symbols("n g alpha a", real=True)
    pi = sp.pi
    c_a = sp.Rational(3)
    c_f = (c_a**2 - 1) / (2 * c_a)
    t_f = sp.Rational(1, 2)
    independently_built = [
        sp.Rational(11, 3) * c_a - sp.Rational(4, 3) * t_f * n,
        sp.Rational(34, 3) * c_a**2
        - 4 * c_f * t_f * n
        - sp.Rational(20, 3) * c_a * t_f * n,
    ]

    print("== Independent symbolic reconstruction ==")
    check("independent b0 reconstruction", sp.cancel(independently_built[0] - (11 - sp.Rational(2, 3) * n)) == 0)
    check("independent b1 reconstruction", sp.cancel(independently_built[1] - (102 - sp.Rational(38, 3) * n)) == 0)

    v_g = -independently_built[0] * g**3 / (16 * pi**2) - independently_built[1] * g**5 / (16 * pi**2) ** 2
    alpha_rate_from_g = sp.expand(g * v_g / (2 * pi))
    expected_alpha_g = sp.expand(
        (
            -independently_built[0] * alpha**2 / (2 * pi)
            - independently_built[1] * alpha**3 / (8 * pi**2)
        ).subs(alpha, g**2 / (4 * pi))
    )
    check("independent chain rule before eliminating g", sp.cancel(alpha_rate_from_g - expected_alpha_g) == 0)

    expected_a_g = sp.expand(
        (-2 * independently_built[0] * a**2 - 2 * independently_built[1] * a**3).subs(
            a, g**2 / (16 * pi**2)
        )
    )
    check("independent a-coordinate chain rule", sp.cancel(alpha_rate_from_g / (4 * pi) - expected_a_g) == 0)

    examples = [
        (sp.Rational(0), sp.Rational(1, 3)),
        (sp.Rational(5), sp.Rational(2, 5)),
        (sp.Rational(13, 2), sp.Rational(-3, 7)),
        (sp.Rational(17), sp.Rational(5, 4)),
    ]
    for index, (n_value, g_value) in enumerate(examples, start=1):
        residual_alpha = sp.cancel((alpha_rate_from_g - expected_alpha_g).subs({n: n_value, g: g_value}))
        residual_a = sp.cancel((alpha_rate_from_g / (4 * pi) - expected_a_g).subs({n: n_value, g: g_value}))
        check(f"rational example {index} alpha residual", residual_alpha == 0, str(residual_alpha))
        check(f"rational example {index} a residual", residual_a == 0, str(residual_a))

    print(f"\nSUMMARY: MODE=independent PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


MUTATIONS: dict[str, KernelPacket] = {
    "missing-cf-term": replace(CANONICAL, b1_cf_coefficient=Fraction(0)),
    "tf-drift": replace(CANONICAL, t_f=Fraction(1)),
    "wrong-g-cubic-factor": replace(CANONICAL, g_cubic_denominator=Fraction(8)),
    "wrong-g-quintic-factor": replace(CANONICAL, g_quintic_denominator=Fraction(128)),
    "wrong-chain-factor": replace(CANONICAL, alpha_chain_denominator=Fraction(1)),
    "wrong-alpha-scale": replace(CANONICAL, alpha_scale=Fraction(2)),
    "wrong-a-scale": replace(CANONICAL, a_scale=Fraction(2)),
    "wrong-b0-sign": replace(CANONICAL, b0_sign=Fraction(1)),
    "wrong-b1-sign": replace(CANONICAL, b1_sign=Fraction(1)),
    "wrong-b0-slope": replace(CANONICAL, b0_tf_coefficient=Fraction(2, 3)),
    "wrong-b1-slope": replace(CANONICAL, b1_ca_coefficient=Fraction(10, 3)),
}


def hostile_checks() -> int:
    """Verify that every named mutation and semantic promotion is rejected."""
    print("== Hostile mutation controls ==")
    for name, packet in MUTATIONS.items():
        expect_rejection(
            f"reject {name}",
            CertificateMismatch,
            lambda packet=packet: validate_canonical(build_certificate(packet)),
        )
    expect_rejection(
        "reject physical QCD interpretation",
        PhysicalInterpretationError,
        lambda: request_physical_interpretation("universal QCD beta function"),
    )
    expect_rejection(
        "reject active-flavour interpretation",
        PhysicalInterpretationError,
        lambda: request_physical_interpretation("n is the active-flavour count"),
    )
    print(f"\nSUMMARY: MODE=hostile PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


def intentional_failure(fixture: str) -> int:
    """Run one or all mutations and exit nonzero when they are detected."""
    selected = MUTATIONS if fixture == "all" else {fixture: MUTATIONS[fixture]}
    undetected: list[str] = []
    for name, packet in selected.items():
        try:
            validate_canonical(build_certificate(packet))
        except CertificateMismatch as exc:
            print(f"INTENTIONAL FAIL: {name} rejected ({exc})")
        else:
            undetected.append(name)
            print(f"UNEXPECTED PASS: {name} was accepted")
    if undetected:
        print(f"INTENTIONAL-FAILURE HARNESS BROKEN: undetected={undetected}")
        return 0
    print(f"INTENTIONAL-FAILURE DETECTED: fixtures={len(selected)}")
    return 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("normal", "independent", "hostile", "intentional-failure"),
        default="normal",
    )
    parser.add_argument(
        "--fixture",
        choices=("all", *MUTATIONS),
        default="all",
        help="mutation selected by intentional-failure mode",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.mode == "normal":
        return normal_checks()
    if args.mode == "independent":
        return independent_checks()
    if args.mode == "hostile":
        return hostile_checks()
    return intentional_failure(args.fixture)


if __name__ == "__main__":
    raise SystemExit(main())
