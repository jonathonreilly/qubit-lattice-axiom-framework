#!/usr/bin/env python3
"""Exact verifier for the universal scalar boundary-transfer theorem.

The load-bearing equation is

    y'(t) = a(t) y(t) + b y(t)^3,

with continuous real ``a`` on a finite interval and ``b > 0``.  This runner
checks the exact solution, maximal endpoint domain, monotonicity, range, and
inverse without importing any physical boundary values.  Its independent mode
uses synthetic numerical functions only; those computations are corroboration,
not proof.

Modes:
  default / --mode exact       symbolic identities, source firewall, strict API
  --independent                independent synthetic numerical oracles
  --hostile                    adversarial formula/source/API mutations
  --mode intentional-failure   install one named mutation and exit nonzero

The one-loop Yukawa specialization in the companion note is conditional
symbolic context and is deliberately absent from every numerical test here.
"""

from __future__ import annotations

import argparse
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/YT_BOUNDARY_BC_TRANSFER_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-17.md"
RUNNER = Path(__file__).resolve()

FORMULA_MUTATIONS = (
    "formula_denominator_sign",
    "formula_j_integrand",
    "formula_inverse_sign",
    "formula_derivative_power",
)
SOURCE_MUTATIONS = (
    "source_numeric_import",
    "source_helper_import",
    "source_physical_closure",
    "source_independent_audit_deletion",
)
API_MUTATIONS = (
    "api_nonpositive_b",
    "api_nonpositive_j",
    "api_nonpositive_x",
    "api_nonpositive_y",
    "api_nonfinite",
    "api_supercritical_x",
)
ALL_MUTATIONS = FORMULA_MUTATIONS + SOURCE_MUTATIONS + API_MUTATIONS
ACTIVE_MUTATION: str | None = None


@dataclass
class Check:
    name: str
    passed: bool
    detail: str


class Recorder:
    def __init__(self) -> None:
        self.checks: list[Check] = []

    def add(self, name: str, passed: bool, detail: str) -> None:
        self.checks.append(Check(name, bool(passed), detail))
        label = "PASS" if passed else "FAIL"
        print(f"  [{label}] {name}")
        print(f"         {detail}")

    @property
    def failures(self) -> list[Check]:
        return [check for check in self.checks if not check.passed]

    def finish(self, mode: str) -> int:
        print("\n" + "=" * 78)
        print(f"SCORECARD: {mode}")
        print("=" * 78)
        print(f"  checks: {len(self.checks)}")
        print(f"  pass:   {len(self.checks) - len(self.failures)}")
        print(f"  fail:   {len(self.failures)}")
        if self.failures:
            print("RESULT: FAIL")
            return 1
        print("RESULT: PASS")
        return 0


def banner(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def _finite_real(name: str, value: float, mutation_key: str | None = None) -> float:
    if ACTIVE_MUTATION == mutation_key:
        return float(value)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a finite real number")
    converted = float(value)
    if not math.isfinite(converted):
        raise ValueError(f"{name} must be finite")
    return converted


def _positive(name: str, value: float, mutation_key: str | None = None) -> float:
    converted = _finite_real(name, value, mutation_key)
    if ACTIVE_MUTATION != mutation_key and converted <= 0.0:
        raise ValueError(f"{name} must be positive")
    return converted


def endpoint_from_integrals(A_T: float, J_T: float, b: float, X: float) -> float:
    """Evaluate the exact endpoint on its strict finite-solution domain."""

    A_T = _finite_real("A_T", A_T, "api_nonfinite")
    J_T = _positive("J_T", J_T, "api_nonpositive_j")
    b = _positive("b", b, "api_nonpositive_b")
    X = _positive("X", X, "api_nonpositive_x")
    if ACTIVE_MUTATION == "api_nonpositive_b" and b <= 0.0:
        return X * math.exp(A_T)
    if ACTIVE_MUTATION == "api_nonpositive_j" and J_T <= 0.0:
        return X * math.exp(A_T)
    xcrit = 1.0 / math.sqrt(2.0 * b * J_T)
    if ACTIVE_MUTATION != "api_supercritical_x" and not X < xcrit:
        raise ValueError("X lies outside the finite endpoint domain")
    denominator = 1.0 - 2.0 * b * X * X * J_T
    if ACTIVE_MUTATION == "formula_denominator_sign":
        denominator = 1.0 + 2.0 * b * X * X * J_T
    if ACTIVE_MUTATION != "api_supercritical_x" and denominator <= 0.0:
        raise ValueError("X lies outside the finite endpoint domain")
    return X * math.exp(A_T) / math.sqrt(abs(denominator))


def inverse_from_integrals(A_T: float, J_T: float, b: float, Y: float) -> float:
    """Evaluate the exact inverse for a positive endpoint target."""

    A_T = _finite_real("A_T", A_T, "api_nonfinite")
    J_T = _positive("J_T", J_T, "api_nonpositive_j")
    b = _positive("b", b, "api_nonpositive_b")
    Y = _positive("Y", Y, "api_nonpositive_y")
    sign = -1.0 if ACTIVE_MUTATION == "formula_inverse_sign" else 1.0
    radicand = math.exp(2.0 * A_T) + sign * 2.0 * b * J_T * Y * Y
    if radicand <= 0.0:
        raise ValueError("inverse radicand must be positive")
    return Y / math.sqrt(radicand)


def symbolic_identities(rec: Recorder) -> None:
    banner("SECTION 1: exact symbolic theorem")
    t = sp.symbols("t", real=True)
    X, b, J, Y = sp.symbols("X b J Y", positive=True)
    A = sp.symbols("A", real=True)
    a_fun = sp.Function("a")(t)
    A_fun = sp.Function("A")(t)
    J_fun = sp.Function("J")(t)

    sign = 1 if ACTIVE_MUTATION == "formula_denominator_sign" else -1
    D_fun = 1 + sign * 2 * b * X**2 * J_fun
    y_fun = X * sp.exp(A_fun) / sp.sqrt(D_fun)
    j_prime = sp.exp(A_fun) if ACTIVE_MUTATION == "formula_j_integrand" else sp.exp(2 * A_fun)
    residual = sp.diff(y_fun, t) - a_fun * y_fun - b * y_fun**3
    residual = residual.subs(
        {
            sp.diff(A_fun, t): a_fun,
            sp.diff(J_fun, t): j_prime,
        }
    )
    residual = sp.factor(sp.simplify(residual))
    rec.add(
        "exact_ode_residual",
        residual == 0,
        f"closed-form substitution leaves residual {residual}",
    )

    z_fun = sp.exp(-2 * A_fun) * (X**-2 - 2 * b * J_fun)
    z_residual = sp.diff(z_fun, t) + 2 * a_fun * z_fun + 2 * b
    z_residual = z_residual.subs(
        {
            sp.diff(A_fun, t): a_fun,
            sp.diff(J_fun, t): sp.exp(2 * A_fun),
        }
    )
    z_residual = sp.simplify(z_residual)
    rec.add(
        "linearized_z_equation",
        z_residual == 0,
        f"z=y^(-2) satisfies z'+2az=-2b exactly; residual {z_residual}",
    )

    initial = sp.simplify(y_fun.subs({A_fun: 0, J_fun: 0}) - X)
    rec.add("exact_initial_value", initial == 0, f"y(t0)-X simplifies to {initial}")

    D = 1 + sign * 2 * b * J * X**2
    phi = X * sp.exp(A) / sp.sqrt(D)
    derivative_claim = sp.exp(A) * D ** (
        -sp.Rational(1, 2) if ACTIVE_MUTATION == "formula_derivative_power" else -sp.Rational(3, 2)
    )
    derivative_residual = sp.factor(sp.simplify(sp.diff(phi, X) - derivative_claim))
    rec.add(
        "exact_positive_derivative",
        derivative_residual == 0 and sign == -1,
        f"dPhi/dX matches exp(A) D^(-3/2); residual {derivative_residual}",
    )

    q = sp.symbols("q", positive=True)
    e2A = sp.exp(2 * A)
    transfer_squared = q * e2A / (1 - 2 * b * J * q)
    inverse_sign = -1 if ACTIVE_MUTATION == "formula_inverse_sign" else 1
    inverse_squared = Y**2 / (e2A + inverse_sign * 2 * b * J * Y**2)
    right_inverse = sp.factor(sp.simplify(transfer_squared.subs(q, inverse_squared) - Y**2))
    rec.add(
        "exact_right_inverse",
        right_inverse == 0,
        f"Phi(X*(Y))^2-Y^2 simplifies to {right_inverse}",
    )
    inverse_of_transfer = sp.factor(
        sp.simplify(
            inverse_squared.subs(Y**2, transfer_squared) - q,
        )
    )
    rec.add(
        "exact_left_inverse",
        inverse_of_transfer == 0,
        f"X*(Phi(X))^2-X^2 simplifies to {inverse_of_transfer}",
    )

    xcrit_squared = 1 / (2 * b * J)
    inverse_gap = sp.factor(sp.simplify(xcrit_squared - inverse_squared))
    expected_gap = e2A / (2 * b * J * (e2A + 2 * b * J * Y**2))
    gap_residual = sp.factor(sp.simplify(inverse_gap - expected_gap))
    rec.add(
        "inverse_inside_exact_domain",
        gap_residual == 0,
        f"Xcrit^2-X*(Y)^2 equals a manifestly positive expression; residual {gap_residual}",
    )

    epsilon = sp.symbols("epsilon", positive=True)
    lower_limit = sp.simplify(sp.limit(X * sp.exp(A) / sp.sqrt(1 - 2 * b * J * X**2), X, 0, dir="+"))
    # Set X^2=(1-epsilon)Xcrit^2.  The positive endpoint's square is then
    # manifestly positive, avoiding an ambiguous complex square-root branch.
    upper_squared = sp.exp(2 * A) * (1 - epsilon) / (2 * b * J * epsilon)
    upper_limit_squared = sp.limit(upper_squared, epsilon, 0, dir="+")
    rec.add(
        "exact_range_limits",
        lower_limit == 0 and upper_limit_squared == sp.oo,
        f"lower endpoint limit is {lower_limit}; positive endpoint square tends to {upper_limit_squared}",
    )

    fixture_subcritical = sp.simplify(
        endpoint_symbolic(sp.Integer(0), sp.Integer(1), sp.Integer(1), sp.Rational(1, 2))
        - 1 / sp.sqrt(2)
    )
    rec.add(
        "exact_subcritical_fixture",
        fixture_subcritical == 0,
        f"a=0, b=1, interval length 1 gives the exact subcritical endpoint; residual {fixture_subcritical}",
    )
    rec.add(
        "exact_critical_and_supercritical_boundary",
        (1 - 2 * sp.Rational(1, 2)) == 0 and (1 - 2 * sp.Rational(4, 5)) < 0,
        "the denominator is zero at X=1/sqrt(2) and negative at X=sqrt(4/5)",
    )
    negative_b_limit = sp.limit(X / sp.sqrt(1 + 2 * X**2), X, sp.oo)
    rec.add(
        "sign_boundary_counterfixture",
        negative_b_limit == 1 / sp.sqrt(2),
        f"for b=-1 the increasing transfer has finite limiting range {negative_b_limit}, so b>0 is load-bearing",
    )


def endpoint_symbolic(A_T: sp.Expr, J_T: sp.Expr, b: sp.Expr, X: sp.Expr) -> sp.Expr:
    sign = 1 if ACTIVE_MUTATION == "formula_denominator_sign" else -1
    return X * sp.exp(A_T) / sp.sqrt(1 + sign * 2 * b * X**2 * J_T)


def _forbidden_source_tokens() -> tuple[str, ...]:
    # Split literals keep the runner itself from matching its hostile fixtures.
    numeric_imports = (
        "0.59" + "34",
        "0.43" + "577",
        "0.97" + "267",
        "246" + "." + "28",
        "1.2209" + "e19",
        "91." + "1876",
        "172" + "." + "69",
        "127" + "." + "951",
        "0.231" + "22",
    )
    helper_imports = (
        "canonical" + "_" + "plaquette_surface",
        "WARD" + "_" + "TARGET",
        "M" + "_" + "PL",
        "run" + "_" + "with_thresholds",
        "beta" + "_" + "2loop",
    )
    physical_overclaims = (
        "closes the parent " + "YT boundary theorem",
        "proves the " + "Standard Model boundary condition",
        "derives the " + "Ward target",
    )
    return numeric_imports + helper_imports + physical_overclaims


def source_firewall_violations(note_text: str, runner_text: str) -> list[str]:
    combined = note_text + "\n" + runner_text
    violations = [token for token in _forbidden_source_tokens() if token in combined]
    normalized_note = " ".join(note_text.split())
    required_note_phrases = (
        "independent review and independent audit are required",
        "This theorem supplies no Planck-scale, Ward-target, Standard-Model, or parent-lane closure.",
        "conditional symbolic context only",
        "strictly increasing bijection",
        "X_crit",
    )
    violations.extend(f"missing:{phrase}" for phrase in required_note_phrases if phrase not in normalized_note)
    return violations


def mutated_sources(fixture: str, note_text: str, runner_text: str) -> tuple[str, str]:
    if fixture == "source_numeric_import":
        note_text += "\nimported benchmark = " + ("0.43" + "577")
    elif fixture == "source_helper_import":
        runner_text += "\nfrom " + ("canonical" + "_" + "plaquette_surface") + " import value"
    elif fixture == "source_physical_closure":
        note_text += "\n" + ("closes the parent " + "YT boundary theorem")
    elif fixture == "source_independent_audit_deletion":
        note_text = re.sub(
            r"independent review and independent audit are\s+required",
            "review pending",
            note_text,
            count=1,
        )
    return note_text, runner_text


def source_firewall(rec: Recorder) -> None:
    banner("SECTION 2: source and import firewall")
    note_text = NOTE.read_text(encoding="utf-8")
    runner_text = RUNNER.read_text(encoding="utf-8")
    if ACTIVE_MUTATION in SOURCE_MUTATIONS:
        note_text, runner_text = mutated_sources(ACTIVE_MUTATION, note_text, runner_text)
    violations = source_firewall_violations(note_text, runner_text)
    rec.add(
        "source_firewall",
        not violations,
        "no physical boundary values/helpers/closure claims enter the theorem source"
        if not violations
        else "violations: " + ", ".join(violations),
    )
    rec.add(
        "source_graph_is_self_contained",
        ("canonical" + "_" + "plaquette_surface") not in runner_text
        and ("frontier" + "_" + "yt_boundary_consistency") not in runner_text,
        "runner imports no parent or physical-value helper",
    )


def strict_api_checks(rec: Recorder) -> None:
    banner("SECTION 3: strict theorem API")
    endpoint = endpoint_from_integrals(0.2, 0.7, 0.4, 0.5)
    inverse = inverse_from_integrals(0.2, 0.7, 0.4, endpoint)
    rec.add(
        "api_roundtrip",
        math.isclose(inverse, 0.5, rel_tol=2e-14, abs_tol=2e-14),
        f"valid endpoint/inverse roundtrip error {abs(inverse - 0.5):.3e}",
    )

    invalid_calls: list[tuple[str, Callable[[], float]]] = [
        ("nonpositive_b", lambda: endpoint_from_integrals(0.0, 1.0, 0.0, 0.2)),
        ("nonpositive_j", lambda: endpoint_from_integrals(0.0, 0.0, 1.0, 0.2)),
        ("nonpositive_x", lambda: endpoint_from_integrals(0.0, 1.0, 1.0, 0.0)),
        ("nonpositive_y", lambda: inverse_from_integrals(0.0, 1.0, 1.0, 0.0)),
        ("nonfinite", lambda: endpoint_from_integrals(math.nan, 1.0, 1.0, 0.2)),
        ("boolean", lambda: endpoint_from_integrals(0.0, 1.0, True, 0.2)),
        ("outside_domain", lambda: endpoint_from_integrals(0.0, 1.0, 1.0, 1.0)),
    ]
    for name, call in invalid_calls:
        rejected = False
        try:
            call()
        except (TypeError, ValueError):
            rejected = True
        rec.add(
            f"api_rejects_{name}",
            rejected,
            "invalid input rejected before theorem evaluation" if rejected else "invalid input was accepted",
        )


def independent_numerical_oracles(rec: Recorder) -> None:
    banner("SECTION 4: independent synthetic numerical oracles")
    try:
        from scipy.integrate import quad, solve_ivp
    except ImportError as exc:  # pragma: no cover - dependency failure is explicit
        rec.add("scipy_available", False, str(exc))
        return

    profiles: tuple[tuple[str, Callable[[float], float], float, float, float], ...] = (
        ("affine", lambda t: 0.12 - 0.08 * t, 0.0, 1.3, 0.45),
        ("oscillatory", lambda t: -0.17 + 0.09 * math.sin(2.3 * t), -0.4, 0.9, 0.7),
        ("quadratic", lambda t: 0.05 + 0.04 * t * t, 0.2, 1.1, 0.35),
    )
    for label, a_function, t0, T, b_value in profiles:
        A_T = quad(a_function, t0, T, epsabs=2e-13, epsrel=2e-13, limit=200)[0]

        def A_at(s: float) -> float:
            return quad(a_function, t0, s, epsabs=3e-13, epsrel=3e-13, limit=200)[0]

        J_T = quad(lambda s: math.exp(2.0 * A_at(s)), t0, T, epsabs=3e-12, epsrel=3e-12, limit=200)[0]
        xcrit = 1.0 / math.sqrt(2.0 * b_value * J_T)
        fractions = (0.12, 0.31, 0.57, 0.79)
        formula_values: list[float] = []
        max_error = 0.0
        for fraction in fractions:
            X = fraction * xcrit
            direct = solve_ivp(
                lambda t, state: [a_function(t) * state[0] + b_value * state[0] ** 3],
                (t0, T),
                [X],
                method="DOP853",
                rtol=2e-12,
                atol=2e-14,
            )
            if not direct.success:
                max_error = math.inf
                break
            formula = endpoint_from_integrals(A_T, J_T, b_value, X)
            formula_values.append(formula)
            max_error = max(max_error, abs(direct.y[0, -1] - formula))
        rec.add(
            f"numeric_direct_ode_{label}",
            max_error < 2e-9,
            f"independent solve_ivp versus quadrature formula max error {max_error:.3e}",
        )
        rec.add(
            f"numeric_monotonicity_{label}",
            len(formula_values) == len(fractions)
            and all(left < right for left, right in zip(formula_values, formula_values[1:])),
            "synthetic endpoint values increase across the independent grid",
        )

        X = 0.43 * xcrit
        step = 2e-6 * xcrit
        finite_difference = (
            endpoint_from_integrals(A_T, J_T, b_value, X + step)
            - endpoint_from_integrals(A_T, J_T, b_value, X - step)
        ) / (2.0 * step)
        derivative = math.exp(A_T) / (1.0 - 2.0 * b_value * J_T * X * X) ** 1.5
        rec.add(
            f"numeric_derivative_{label}",
            math.isclose(finite_difference, derivative, rel_tol=2e-9, abs_tol=2e-9),
            f"finite-difference versus exact derivative relative error {abs(finite_difference / derivative - 1.0):.3e}",
        )

        targets = (0.08, 0.6, 2.4, 9.0)
        roundtrip_error = 0.0
        for target in targets:
            preimage = inverse_from_integrals(A_T, J_T, b_value, target)
            roundtrip_error = max(
                roundtrip_error,
                abs(endpoint_from_integrals(A_T, J_T, b_value, preimage) - target),
            )
        rec.add(
            f"numeric_inverse_{label}",
            roundtrip_error < 2e-12,
            f"positive-target inverse roundtrip max error {roundtrip_error:.3e}",
        )


def hostile_formula_checks(rec: Recorder) -> None:
    banner("SECTION 5: hostile formula mutations")
    X, b, J, Y = sp.symbols("X b J Y", positive=True)
    A = sp.symbols("A", real=True)
    e2A = sp.exp(2 * A)
    exact_squared = X**2 * e2A / (1 - 2 * b * J * X**2)
    mutations = {
        "denominator_plus_sign": X**2 * e2A / (1 + 2 * b * J * X**2),
        "missing_factor_two_in_J": X**2 * e2A / (1 - b * J * X**2),
        "wrong_inverse_sign": Y**2 / (e2A - 2 * b * J * Y**2),
        "wrong_derivative_power": sp.exp(A) / sp.sqrt(1 - 2 * b * J * X**2),
    }
    exact_derivative = sp.diff(sp.sqrt(exact_squared), X)
    for name, mutation in mutations.items():
        if name == "wrong_inverse_sign":
            composed = sp.factor(sp.simplify(exact_squared.subs(X**2, mutation) - Y**2))
            detected = composed != 0
            detail = f"wrong inverse leaves composition residual {composed}"
        elif name == "wrong_derivative_power":
            residual = sp.factor(sp.simplify(exact_derivative - mutation))
            detected = residual != 0
            detail = f"wrong derivative leaves residual {residual}"
        else:
            residual = sp.factor(sp.simplify(exact_squared - mutation))
            detected = residual != 0
            detail = f"mutated transfer differs exactly; residual {residual}"
        rec.add(f"rejects_{name}", detected, detail)


def hostile_source_checks(rec: Recorder) -> None:
    banner("SECTION 6: hostile source mutations")
    note_text = NOTE.read_text(encoding="utf-8")
    runner_text = RUNNER.read_text(encoding="utf-8")
    for fixture in SOURCE_MUTATIONS:
        changed_note, changed_runner = mutated_sources(fixture, note_text, runner_text)
        violations = source_firewall_violations(changed_note, changed_runner)
        rec.add(
            f"rejects_{fixture}",
            bool(violations),
            "source firewall reports: " + ", ".join(violations),
        )


def hostile_api_checks(rec: Recorder) -> None:
    banner("SECTION 7: hostile API mutations")
    calls: tuple[tuple[str, Callable[[], float]], ...] = (
        ("zero_b", lambda: endpoint_from_integrals(0.0, 1.0, 0.0, 0.2)),
        ("negative_b", lambda: endpoint_from_integrals(0.0, 1.0, -1.0, 0.2)),
        ("zero_j", lambda: endpoint_from_integrals(0.0, 0.0, 1.0, 0.2)),
        ("zero_x", lambda: endpoint_from_integrals(0.0, 1.0, 1.0, 0.0)),
        ("zero_y", lambda: inverse_from_integrals(0.0, 1.0, 1.0, 0.0)),
        ("nan", lambda: endpoint_from_integrals(math.nan, 1.0, 1.0, 0.2)),
        ("infinity", lambda: inverse_from_integrals(0.0, math.inf, 1.0, 0.2)),
        ("boolean", lambda: endpoint_from_integrals(0.0, 1.0, True, 0.2)),
        ("critical", lambda: endpoint_from_integrals(0.0, 1.0, 1.0, 1.0 / math.sqrt(2.0))),
        ("supercritical", lambda: endpoint_from_integrals(0.0, 1.0, 1.0, 1.0)),
    )
    for name, call in calls:
        rejected = False
        try:
            call()
        except (TypeError, ValueError):
            rejected = True
        rec.add(
            f"rejects_api_{name}",
            rejected,
            "invalid theorem input rejected" if rejected else "invalid theorem input was accepted",
        )


def run_exact() -> int:
    rec = Recorder()
    banner("UNIVERSAL SCALAR BOUNDARY-TRANSFER EXACT VERIFIER")
    symbolic_identities(rec)
    source_firewall(rec)
    strict_api_checks(rec)
    return rec.finish("exact")


def run_independent() -> int:
    rec = Recorder()
    banner("INDEPENDENT SYNTHETIC NUMERICAL ORACLES")
    independent_numerical_oracles(rec)
    return rec.finish("independent")


def run_hostile() -> int:
    rec = Recorder()
    banner("HOSTILE MUTATION SUITE")
    hostile_formula_checks(rec)
    hostile_source_checks(rec)
    hostile_api_checks(rec)
    return rec.finish("hostile")


def run_intentional_failure(fixture: str) -> int:
    global ACTIVE_MUTATION
    fixtures = ALL_MUTATIONS if fixture == "all" else (fixture,)
    detected = 0
    banner("INTENTIONAL-FAILURE MUTATION INSTALLER")
    for installed in fixtures:
        ACTIVE_MUTATION = installed
        rec = Recorder()
        if installed in FORMULA_MUTATIONS:
            symbolic_identities(rec)
        elif installed in SOURCE_MUTATIONS:
            source_firewall(rec)
        else:
            strict_api_checks(rec)
        if rec.failures:
            detected += 1
            print(f"  [DETECTED] {installed}: {len(rec.failures)} theorem check(s) failed")
        else:
            print(f"  [UNDETECTED] {installed}: mutation escaped all theorem checks")
        ACTIVE_MUTATION = None
    print(f"\nmutations installed: {len(fixtures)}; detected: {detected}")
    if detected != len(fixtures):
        print("RESULT: MUTATION ESCAPED")
        return 2
    print("RESULT: INTENTIONAL FAILURE (all installed mutations detected)")
    return 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("exact", "independent", "hostile", "intentional-failure"),
        default="exact",
    )
    parser.add_argument("--independent", action="store_true", help="alias for --mode independent")
    parser.add_argument("--hostile", action="store_true", help="alias for --mode hostile")
    parser.add_argument(
        "--fixture",
        choices=("all",) + ALL_MUTATIONS,
        default="all",
        help="mutation fixture for intentional-failure mode",
    )
    args = parser.parse_args()
    aliases = int(args.independent) + int(args.hostile)
    if aliases > 1:
        parser.error("choose at most one mode alias")
    if args.independent:
        args.mode = "independent"
    if args.hostile:
        args.mode = "hostile"
    if args.fixture != "all" and args.mode != "intentional-failure":
        parser.error("--fixture requires --mode intentional-failure")
    return args


def main() -> int:
    args = parse_args()
    if args.mode == "exact":
        return run_exact()
    if args.mode == "independent":
        return run_independent()
    if args.mode == "hostile":
        return run_hostile()
    return run_intentional_failure(args.fixture)


if __name__ == "__main__":
    raise SystemExit(main())
