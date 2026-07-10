#!/usr/bin/env python3
"""Validate the conditional formation-rate logarithmic chain rule.

For a supplied differentiable availability profile A(r) and a supplied rate
law F differentiable at A0=A(r0), with A0>0 and F(A0)>0,

    (d/dr F(A(r)) / F(A(r)))|r0
      = [F'(A0) A0 / F(A0)] [A'(r0) / A0].

The runner checks closed-form logarithmic derivatives and independently
compares the analytic identity with a five-point finite-difference derivative
of each composed example. It selects no physical rate law, clock, dynamics, or
gravity interpretation and sets no audit result.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from typing import Callable


R0 = 1.0
FD_STEP = 1.0e-4
TOL = 2.0e-9

FloatFn = Callable[[float], float]


@dataclass(frozen=True)
class RateLaw:
    name: str
    value: FloatFn
    derivative: FloatFn
    expected_g: FloatFn


@dataclass(frozen=True)
class Profile:
    name: str
    value: FloatFn
    derivative: FloatFn


RATE_LAWS = (
    RateLaw("linear", lambda a: a, lambda _a: 1.0, lambda _a: 1.0),
    RateLaw(
        "square_root",
        math.sqrt,
        lambda a: 0.5 / math.sqrt(a),
        lambda _a: 0.5,
    ),
    RateLaw("quadratic", lambda a: a * a, lambda a: 2.0 * a, lambda _a: 2.0),
    RateLaw(
        "saturating",
        lambda a: a / (1.0 + a),
        lambda a: 1.0 / (1.0 + a) ** 2,
        lambda a: 1.0 / (1.0 + a),
    ),
    RateLaw(
        "exponential",
        lambda a: -math.expm1(-a),
        lambda a: math.exp(-a),
        lambda a: a / math.expm1(a),
    ),
)

PROFILES = (
    Profile("linear6", lambda r: 6.0 - r, lambda _r: -1.0),
    Profile("convex6", lambda r: (6.0 - r) ** 2 / 6.0, lambda r: -(6.0 - r) / 3.0),
    Profile(
        "horizon6",
        lambda r: (6.0 - r) ** 4 / 125.0,
        lambda r: -4.0 * (6.0 - r) ** 3 / 125.0,
    ),
)


def fd5_first(function: FloatFn, x: float, h: float = FD_STEP) -> float:
    """Five-point central derivative, independent of the analytic derivatives."""

    return (
        function(x - 2.0 * h)
        - 8.0 * function(x - h)
        + 8.0 * function(x + h)
        - function(x + 2.0 * h)
    ) / (12.0 * h)


def run() -> tuple[list[str], int]:
    maximum_identity_error = 0.0
    maximum_closed_form_error = 0.0
    rows: list[str] = []

    for profile in PROFILES:
        a0 = profile.value(R0)
        da0 = profile.derivative(R0)
        if not a0 > 0.0:
            raise AssertionError(f"{profile.name}: A0 must be positive")

        for law in RATE_LAWS:
            f0 = law.value(a0)
            if not f0 > 0.0:
                raise AssertionError(f"{law.name}/{profile.name}: F(A0) must be positive")

            g_value = law.derivative(a0) * a0 / f0
            expected_g = law.expected_g(a0)
            closed_form_error = abs(g_value - expected_g)
            maximum_closed_form_error = max(maximum_closed_form_error, closed_form_error)

            analytic_response = law.derivative(a0) * da0 / f0
            factored_response = g_value * da0 / a0
            algebra_error = abs(analytic_response - factored_response)

            composed = lambda r, law=law, profile=profile: law.value(profile.value(r))
            numeric_response = fd5_first(composed, R0) / f0
            numeric_error = abs(numeric_response - factored_response)
            identity_error = max(algebra_error, numeric_error)
            maximum_identity_error = max(maximum_identity_error, identity_error)

            rows.append(
                f"{profile.name}/{law.name}:A0={a0:.12g},F0={f0:.12g},"
                f"g={g_value:.12g},response={factored_response:.12g},"
                f"fd_error={numeric_error:.3e}"
            )

    passed = maximum_identity_error <= TOL and maximum_closed_form_error <= TOL
    lines = [
        (
            "HYPOTHESES: A differentiable at r0; A0>0; F differentiable at A0; "
            "F(A0)>0; supplied examples only"
        ),
        "EXAMPLES: " + " | ".join(rows),
        (
            f"CHECKS: chain_rule={passed} max_identity_error={maximum_identity_error:.3e} "
            f"closed_forms={maximum_closed_form_error <= TOL} "
            f"max_closed_form_error={maximum_closed_form_error:.3e}"
        ),
        (
            "TOTAL: CHAIN-RULE-VALIDATED"
            if passed
            else "TOTAL: MACHINERY-FAIL"
        ),
    ]
    return lines, 0 if passed else 1


def main() -> int:
    try:
        lines, exit_code = run()
    except Exception as exc:  # noqa: BLE001
        print(f"TOTAL: MACHINERY-FAIL {type(exc).__name__}: {exc}")
        return 1
    for line in lines:
        print(line)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
