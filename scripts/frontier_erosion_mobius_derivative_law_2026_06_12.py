#!/usr/bin/env python3
"""Class-A finite-dimensional verification for the source note

    docs/EROSION_MOBIUS_DERIVATIVE_CHAIN_RULE_LAW_BOUNDED_THEOREM_NOTE_2026-06-12.md

Scope: the landed erosion recurrence model, its Moebius step map, and the
bounded periodic-word derivative/rate law. The audit lane grades.

Run:
    python3 scripts/frontier_erosion_mobius_derivative_law_2026_06_12.py
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass

import sympy as sp


EPS_DOMAIN = (0.0, 1.0)

# S0 fixed anchors, frozen before evaluation.
ANCHOR_UNIFORM_EPS = 0.2
ANCHOR_UNIFORM_RATE_EPS02 = 0.6666666666666666
ANCHOR_UNIFORM_RATE_TOL = 1.0e-10
ANCHOR_ALTERNATING_EPS = 0.2
ANCHOR_ALTERNATING_P0 = 0.0
ANCHOR_ALTERNATING_C0 = 1.0
ANCHOR_ALTERNATING_SIGNS = (1, -1)
ANCHOR_ALTERNATING_PRODUCT = 1.0
ANCHOR_ALTERNATING_PRODUCT_TOL = 1.0e-14
ANCHOR_LAMBDA_EPS = 0.2
ANCHOR_LAMBDA_UNIFORM_WORD = (1,)
ANCHOR_LAMBDA_STRICT_MIN = 1.0

# I2 fixed chain-rule gates.
CHAIN_RULE_NUMERIC_TOL = 1.0e-12
CHAIN_RULE_P0 = -0.27
CHAIN_RULE_EPS_GRID = (0.1, 0.2, 0.3, 0.4)
CHAIN_RULE_WORDS = (
    (1,),
    (1, -1),
    (1, 1, -1),
    (1, -1, -1),
    (1, 1, 1, -1),
    (1, 1, -1, -1),
    (1, -1, 1, 1, -1, 1),
)
SYMBOLIC_TRIPLES = (
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, 1),
    (1, -1, -1),
    (-1, 1, 1),
    (-1, 1, -1),
    (-1, -1, 1),
    (-1, -1, -1),
)

# I3 fixed periodic-word rate-law gates.
PERIODIC_RATE_TOL = 1.0e-10
PERIODIC_RATE_EPS_GRID = (0.1, 0.2, 0.3, 0.4)
PERIODIC_RATE_WORDS = (
    (1, 1),
    (1, -1),
    (1, 1, -1),
    (1, -1, -1),
    (1, 1, 1, -1),
    (1, 1, -1, -1),
    (1, -1, 1, 1, -1, 1),
)
PERIODIC_RATE_INITIAL_P0 = 0.123
PERIODIC_RATE_WARMUP_PERIODS = 1600

# I4 and I5 fixed gates.
SPECIAL_UNIFORM_TOL = 1.0e-15
SPECIAL_ALTERNATING_NUMERIC_TOL = 1.0e-14
PARABOLIC_TRACE_TOL = 1.0e-12
HYPERBOLIC_TRACE_GAP_TOL = 1.0e-12
FROZEN_PARABOLIC_CASES = 8
FROZEN_HYPERBOLIC_CASES = 20

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        print(f"PASS: {name}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL: {name}" + (f" :: {detail}" if detail else ""))


def section(name: str) -> None:
    print("=" * 78)
    print(name)
    print("=" * 78)


def next_p(p: float, eps: float, s: int) -> float:
    return (p + s * eps) / (1.0 + s * eps * p)


def c_factor(p: float, eps: float, s: int) -> float:
    return (1.0 - eps * eps) / (1.0 + s * eps * p) ** 2


def closed_rate(eps: float) -> float:
    return (1.0 - eps) / (1.0 + eps)


@dataclass(frozen=True)
class PathRun:
    p_values: tuple[float, ...]
    factors: tuple[float, ...]
    product_c: float


def run_path(eps: float, p0: float, c0: float, signs: tuple[int, ...]) -> PathRun:
    p = p0
    c = c0
    p_values = [p]
    factors = []
    for s in signs:
        factor = c_factor(p, eps, s)
        factors.append(factor)
        c *= factor
        p = next_p(p, eps, s)
        p_values.append(p)
    return PathRun(tuple(p_values), tuple(factors), c)


Matrix2 = tuple[tuple[float, float], tuple[float, float]]


def matmul(left: Matrix2, right: Matrix2) -> Matrix2:
    a, b = left[0]
    c, d = left[1]
    e, f = right[0]
    g, h = right[1]
    return ((a * e + b * g, a * f + b * h), (c * e + d * g, c * f + d * h))


def step_matrix(eps: float, s: int) -> Matrix2:
    return ((1.0, s * eps), (s * eps, 1.0))


def word_matrix(eps: float, signs: tuple[int, ...]) -> Matrix2:
    matrix: Matrix2 = ((1.0, 0.0), (0.0, 1.0))
    for s in signs:
        matrix = matmul(step_matrix(eps, s), matrix)
    return matrix


def det2(matrix: Matrix2) -> float:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def trace2(matrix: Matrix2) -> float:
    return matrix[0][0] + matrix[1][1]


def projective_action(matrix: Matrix2, p: float) -> float:
    a, b = matrix[0]
    c, d = matrix[1]
    return (a * p + b) / (c * p + d)


def derivative_from_matrix(matrix: Matrix2, p: float) -> float:
    c, d = matrix[1]
    return det2(matrix) / (c * p + d) ** 2


def lambda_max_abs(matrix: Matrix2) -> float:
    trace = trace2(matrix)
    determinant = det2(matrix)
    discriminant = trace * trace - 4.0 * determinant
    root = math.sqrt(max(0.0, discriminant))
    eig_a = 0.5 * (trace + root)
    eig_b = 0.5 * (trace - root)
    return max(abs(eig_a), abs(eig_b))


def matrix_rate_law(eps: float, signs: tuple[int, ...]) -> float:
    matrix = word_matrix(eps, signs)
    lam = lambda_max_abs(matrix)
    return det2(matrix) / (lam * lam)


def apply_word(p: float, eps: float, signs: tuple[int, ...]) -> tuple[float, float]:
    product = 1.0
    for s in signs:
        product *= c_factor(p, eps, s)
        p = next_p(p, eps, s)
    return p, product


def periodic_rate_after_warmup(eps: float, signs: tuple[int, ...]) -> float:
    p = PERIODIC_RATE_INITIAL_P0
    for _ in range(PERIODIC_RATE_WARMUP_PERIODS):
        p, _ = apply_word(p, eps, signs)
    _, product = apply_word(p, eps, signs)
    return product


def word_label(signs: tuple[int, ...]) -> str:
    return "".join("+" if s > 0 else "-" for s in signs)


def s0_anchors() -> None:
    section("S0 anchors first")
    uniform_rate = closed_rate(ANCHOR_UNIFORM_EPS)
    uniform_err = abs(uniform_rate - ANCHOR_UNIFORM_RATE_EPS02)
    print(
        f"landed uniform anchor: eps={ANCHOR_UNIFORM_EPS}, "
        f"closed_rate={uniform_rate:.16g}, frozen={ANCHOR_UNIFORM_RATE_EPS02:.16g}"
    )
    check(
        "S0 landed uniform rate at eps=0.2 is reproduced",
        uniform_err <= ANCHOR_UNIFORM_RATE_TOL,
        f"abs_err={uniform_err:.3e}, tol={ANCHOR_UNIFORM_RATE_TOL:.1e}",
    )

    alternating = run_path(
        ANCHOR_ALTERNATING_EPS,
        ANCHOR_ALTERNATING_P0,
        ANCHOR_ALTERNATING_C0,
        ANCHOR_ALTERNATING_SIGNS,
    )
    alternating_err = abs(alternating.product_c - ANCHOR_ALTERNATING_PRODUCT)
    print(
        f"landed alternating two-step anchor: eps={ANCHOR_ALTERNATING_EPS}, "
        f"p0={ANCHOR_ALTERNATING_P0}, product={alternating.product_c:.16g}"
    )
    check(
        "S0 landed alternating two-step c-product is 1",
        alternating_err <= ANCHOR_ALTERNATING_PRODUCT_TOL,
        f"abs_err={alternating_err:.3e}, tol={ANCHOR_ALTERNATING_PRODUCT_TOL:.1e}",
    )

    lam = lambda_max_abs(word_matrix(ANCHOR_LAMBDA_EPS, ANCHOR_LAMBDA_UNIFORM_WORD))
    print(
        f"anti-fabrication uniform lambda_max: eps={ANCHOR_LAMBDA_EPS}, "
        f"word={word_label(ANCHOR_LAMBDA_UNIFORM_WORD)}, lambda_max={lam:.16g}"
    )
    check(
        "S0 anti-fabrication: uniform-word lambda_max is strictly nontrivial",
        lam > ANCHOR_LAMBDA_STRICT_MIN,
        f"lambda_max={lam:.16g}, strict_min={ANCHOR_LAMBDA_STRICT_MIN:.1f}",
    )


def i1_pointwise_derivative_identity() -> None:
    section("I1 pointwise derivative identity")
    eps, p = sp.symbols("eps p")
    f_plus = (p + eps) / (1 + eps * p)
    f_minus = (p - eps) / (1 - eps * p)
    c_plus = (1 - eps**2) / (1 + eps * p) ** 2
    c_minus = (1 - eps**2) / (1 - eps * p) ** 2
    plus_num = sp.factor(sp.together(sp.diff(f_plus, p) - c_plus).as_numer_denom()[0])
    minus_num = sp.factor(sp.together(sp.diff(f_minus, p) - c_minus).as_numer_denom()[0])
    print(f"sympy derivative residuals: plus={plus_num}, minus={minus_num}")
    check(
        "I1 sympy: c-factor equals f_s'(p) pointwise for s=+1 and s=-1",
        plus_num == 0 and minus_num == 0,
        f"plus_residual={plus_num}, minus_residual={minus_num}",
    )


def i2_chain_rule() -> None:
    section("I2 chain rule")
    max_derivative_err = 0.0
    max_action_err = 0.0
    for eps in CHAIN_RULE_EPS_GRID:
        for signs in CHAIN_RULE_WORDS:
            path = run_path(eps, CHAIN_RULE_P0, 1.0, signs)
            matrix = word_matrix(eps, signs)
            chain_derivative = derivative_from_matrix(matrix, CHAIN_RULE_P0)
            chain_action = projective_action(matrix, CHAIN_RULE_P0)
            max_derivative_err = max(max_derivative_err, abs(path.product_c - chain_derivative))
            max_action_err = max(max_action_err, abs(path.p_values[-1] - chain_action))
    print(
        f"numeric chain grid: p0={CHAIN_RULE_P0}, "
        f"max_derivative_err={max_derivative_err:.3e}, max_action_err={max_action_err:.3e}"
    )
    check(
        "I2 numeric: c_n/c_0 equals the matrix derivative of F_n on the fixed grid",
        max_derivative_err <= CHAIN_RULE_NUMERIC_TOL,
        f"max_err={max_derivative_err:.3e}, tol={CHAIN_RULE_NUMERIC_TOL:.1e}",
    )
    check(
        "I2 numeric: recurrence composition matches the projective matrix action",
        max_action_err <= CHAIN_RULE_NUMERIC_TOL,
        f"max_err={max_action_err:.3e}, tol={CHAIN_RULE_NUMERIC_TOL:.1e}",
    )

    eps, p = sp.symbols("eps p")
    symbolic_failures = 0
    first_residual = sp.Integer(0)
    for signs in SYMBOLIC_TRIPLES:
        q = p
        product = sp.Integer(1)
        for s in signs:
            product = sp.simplify(product * (1 - eps**2) / (1 + s * eps * q) ** 2)
            q = sp.simplify((q + s * eps) / (1 + s * eps * q))
        residual_num = sp.factor(sp.together(sp.diff(q, p) - product).as_numer_denom()[0])
        if residual_num != 0:
            symbolic_failures += 1
            first_residual = residual_num
    print(
        "symbolic n=3 chain-rule sweep: "
        f"fixed_triples={len(SYMBOLIC_TRIPLES)}, failures={symbolic_failures}"
    )
    check(
        "I2 sympy: n=3 chain rule closes for all fixed sign triples",
        symbolic_failures == 0,
        f"first_residual={first_residual}",
    )


def i3_matrix_periodic_rate_law() -> None:
    section("I3 matrix periodic-word rate law")
    max_rate_err = 0.0
    worst_label = ""
    for eps in PERIODIC_RATE_EPS_GRID:
        for signs in PERIODIC_RATE_WORDS:
            measured = periodic_rate_after_warmup(eps, signs)
            law = matrix_rate_law(eps, signs)
            err = abs(measured - law)
            if err > max_rate_err:
                max_rate_err = err
                worst_label = f"eps={eps:g}, word={word_label(signs)}"
            print(
                f"eps={eps:.1f}, word={word_label(signs):6s}: "
                f"period_rate={measured:.16g}, det/lambda^2={law:.16g}, err={err:.3e}"
            )
    check(
        "I3 numeric: periodic per-word erosion rate equals det(M_w)/lambda_max(M_w)^2",
        max_rate_err <= PERIODIC_RATE_TOL,
        f"max_err={max_rate_err:.3e}, worst={worst_label}, tol={PERIODIC_RATE_TOL:.1e}",
    )


def i4_special_cases() -> None:
    section("I4 special cases recovered")
    max_uniform_err = 0.0
    for eps in PERIODIC_RATE_EPS_GRID:
        law = matrix_rate_law(eps, (1,))
        uniform = closed_rate(eps)
        max_uniform_err = max(max_uniform_err, abs(law - uniform))
    print(f"uniform T=1 matrix law max_err={max_uniform_err:.3e}")
    check(
        "I4 uniform T=1 gives det/lambda^2 = (1-eps)/(1+eps)",
        max_uniform_err <= SPECIAL_UNIFORM_TOL,
        f"max_err={max_uniform_err:.3e}, tol={SPECIAL_UNIFORM_TOL:.1e}",
    )

    eps = sp.symbols("eps")
    m_plus = sp.Matrix([[1, eps], [eps, 1]])
    m_minus = sp.Matrix([[1, -eps], [-eps, 1]])
    alternating_residual = sp.simplify(m_minus * m_plus - (1 - eps**2) * sp.eye(2))
    alternating_entries_zero = all(
        sp.simplify(alternating_residual[row, col]) == 0
        for row in range(2)
        for col in range(2)
    )
    max_alternating_numeric_err = 0.0
    for eps_value in PERIODIC_RATE_EPS_GRID:
        max_alternating_numeric_err = max(
            max_alternating_numeric_err,
            abs(matrix_rate_law(eps_value, (1, -1)) - 1.0),
        )
    print(
        "alternating matrix residual: "
        f"{alternating_residual}, numeric_rate_err={max_alternating_numeric_err:.3e}"
    )
    check(
        "I4 alternating matrix identity M_- M_+ = (1-eps^2) I gives rate 1",
        alternating_entries_zero and max_alternating_numeric_err <= SPECIAL_ALTERNATING_NUMERIC_TOL,
        (
            f"entries_zero={alternating_entries_zero}, "
            f"numeric_err={max_alternating_numeric_err:.3e}"
        ),
    )


def i5_edge_case_census() -> None:
    section("I5 parabolic/edge-case census")
    parabolic_cases = 0
    hyperbolic_cases = 0
    min_hyperbolic_trace_gap = math.inf
    for eps in PERIODIC_RATE_EPS_GRID:
        for signs in PERIODIC_RATE_WORDS:
            matrix = word_matrix(eps, signs)
            trace_gap = trace2(matrix) ** 2 - 4.0 * det2(matrix)
            if abs(trace_gap) <= PARABOLIC_TRACE_TOL:
                parabolic_cases += 1
            else:
                hyperbolic_cases += 1
                min_hyperbolic_trace_gap = min(min_hyperbolic_trace_gap, trace_gap)
    print(
        "fixed-set census: "
        f"parabolic_or_scalar_cases={parabolic_cases}, "
        f"hyperbolic_cases={hyperbolic_cases}, "
        f"min_hyperbolic_trace_gap={min_hyperbolic_trace_gap:.3e}"
    )
    check(
        "I5 fixed set contains the frozen scalar-edge cases and hyperbolic cases clear trace^2 > 4 det",
        parabolic_cases == FROZEN_PARABOLIC_CASES
        and hyperbolic_cases == FROZEN_HYPERBOLIC_CASES
        and min_hyperbolic_trace_gap > HYPERBOLIC_TRACE_GAP_TOL,
        (
            f"parabolic={parabolic_cases}, hyperbolic={hyperbolic_cases}, "
            f"min_gap={min_hyperbolic_trace_gap:.3e}"
        ),
    )


def main() -> int:
    print("Erosion Moebius derivative chain-rule verification")
    print("Recurrence: p_s=(p+s eps)/(1+s eps p), c_s=c*(1-eps^2)/(1+s eps p)^2")
    s0_anchors()
    i1_pointwise_derivative_identity()
    i2_chain_rule()
    i3_matrix_periodic_rate_law()
    i4_special_cases()
    i5_edge_case_census()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
