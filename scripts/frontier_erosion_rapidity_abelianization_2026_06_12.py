#!/usr/bin/env python3
"""Class-A finite-dimensional verification for the source note

    docs/EROSION_RAPIDITY_ABELIANIZATION_COMPLETE_LAW_BOUNDED_THEOREM_NOTE_2026-06-12.md

Scope: the landed erosion recurrence model, rewritten in rapidity variables.
The audit lane grades.

Run:
    python3 scripts/frontier_erosion_rapidity_abelianization_2026_06_12.py
"""

from __future__ import annotations

import math
import random
import sys
from dataclasses import dataclass

import mpmath as mp
import sympy as sp


# S0 frozen anchors. These gates run first.
ANCHOR_UNIFORM_EPS = 0.2
ANCHOR_UNIFORM_P0 = 0.0
ANCHOR_UNIFORM_WARMUP_STEPS = 100
ANCHOR_UNIFORM_RATE_EPS02 = 0.6666666666666666
ANCHOR_UNIFORM_RATE_TOL = 1.0e-14
ANCHOR_ALTERNATING_EPS = 0.2
ANCHOR_ALTERNATING_P0 = 0.0
ANCHOR_ALTERNATING_SIGNS = (1, -1)
ANCHOR_ALTERNATING_PRODUCT = 1.0
ANCHOR_ALTERNATING_PRODUCT_TOL = 1.0e-14
ANCHOR_TRAJECTORY_EPS = 0.2
ANCHOR_TRAJECTORY_P0 = 0.125
ANCHOR_TRAJECTORY_SIGNS = (1, 1, -1, 1)
ANCHOR_TRAJECTORY_MIN_STEP_SPREAD = 5.0e-2

# R1 symbolic constants.
SYMPY_ZERO = sp.Integer(0)
R1_SIGNS = (1, -1)

# R2/R3 fixed finite grids.
RAPIDITY_NUMERIC_TOL = 1.0e-13
EPS_GRID = (0.05, 0.2, 0.45)
P0_GRID = (-0.72, -0.21, 0.0, 0.63)
RAPIDITY_WORDS = (
    (1,),
    (-1,),
    (1, 1, -1, 1, -1, -1, 1),
    (-1, 1, -1, -1, 1, 1, -1, 1),
    (1, -1, 1, 1, -1, 1, -1, -1, 1),
    (-1, -1, 1, 1, 1, -1, -1, 1, -1, 1, 1),
)
WAVE10_PERIODIC_WORDS = (
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, -1, 1, -1, 1, -1, 1, -1, 1, -1),
    (1, 1, 1, 1, 1, 1, -1, -1, -1, -1),
    (1, 1, 1, 1, 1, 1, 1, -1, -1, -1),
    (-1, -1, -1, -1, -1, -1, 1, 1, 1, 1),
    (1, 1, -1, 1, -1, -1, 1, -1, 1, -1),
)
R3_FIXED_WORDS = RAPIDITY_WORDS + WAVE10_PERIODIC_WORDS

# R3/R4 periodic-rate gates.
PERIODIC_RATE_TOL = 1.0e-13
PERIODIC_RATE_P0 = 0.123
PERIODIC_RATE_WARMUP_PERIODS = 600
R4_PERIODIC_WORDS = (
    (1,),
    (-1,),
    (1, -1),
    (1, 1, -1),
    (1, -1, -1),
    (1, 1, 1, -1),
    (1, 1, -1, -1),
) + WAVE10_PERIODIC_WORDS
R4_UNIFORM_PERIOD = (1, 1, 1, 1, 1)
R4_ALTERNATING_PERIOD = (1, -1, 1, -1, 1, -1, 1, -1, 1, -1)

# R5 fixed seeded zero-drift random-walk probes.
R5_MP_DPS = 80
R5_LOG_ID_TOL = 1.0e-12
R5_EPS = 0.2
R5_P0 = 0.18
R5_N = 4000
R5_SEEDS = (314159, 271828, 161803)
R5_PRINT_SEED = 314159
R5_PRINT_STEPS = (250, 1000, 4000)

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


def sech(x: float) -> float:
    return 1.0 / math.cosh(x)


@dataclass(frozen=True)
class PathRun:
    p_values: tuple[float, ...]
    c_ratio: float


def run_path(eps: float, p0: float, signs: tuple[int, ...]) -> PathRun:
    p = p0
    c = 1.0
    p_values = [p]
    for s in signs:
        c *= c_factor(p, eps, s)
        p = next_p(p, eps, s)
        p_values.append(p)
    return PathRun(tuple(p_values), c)


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


def imbalance_rate_law(eps: float, signs: tuple[int, ...]) -> float:
    r = (1.0 - eps) / (1.0 + eps)
    return r ** abs(sum(signs))


def periodic_rate_after_warmup(eps: float, signs: tuple[int, ...]) -> float:
    p = PERIODIC_RATE_P0
    for _ in range(PERIODIC_RATE_WARMUP_PERIODS):
        p = run_path(eps, p, signs).p_values[-1]
    return run_path(eps, p, signs).c_ratio


def word_label(signs: tuple[int, ...]) -> str:
    return "".join("+" if s > 0 else "-" for s in signs)


def s0_anchors() -> None:
    section("S0 anchors first")

    p = ANCHOR_UNIFORM_P0
    for _ in range(ANCHOR_UNIFORM_WARMUP_STEPS):
        p = next_p(p, ANCHOR_UNIFORM_EPS, 1)
    uniform_rate = c_factor(p, ANCHOR_UNIFORM_EPS, 1)
    uniform_err = abs(uniform_rate - ANCHOR_UNIFORM_RATE_EPS02)

    alternating = run_path(
        ANCHOR_ALTERNATING_EPS,
        ANCHOR_ALTERNATING_P0,
        ANCHOR_ALTERNATING_SIGNS,
    )
    alternating_err = abs(alternating.c_ratio - ANCHOR_ALTERNATING_PRODUCT)

    trajectory = run_path(
        ANCHOR_TRAJECTORY_EPS,
        ANCHOR_TRAJECTORY_P0,
        ANCHOR_TRAJECTORY_SIGNS,
    )
    max_step_spread = max(
        abs(trajectory.p_values[j + 1] - trajectory.p_values[j])
        for j in range(len(trajectory.p_values) - 1)
    )

    print(
        f"landed uniform anchor via recurrence warmup: eps={ANCHOR_UNIFORM_EPS}, "
        f"rate={uniform_rate:.16g}, frozen={ANCHOR_UNIFORM_RATE_EPS02:.16g}"
    )
    check(
        "S0 landed uniform rate at eps=0.2 is reproduced",
        uniform_err <= ANCHOR_UNIFORM_RATE_TOL,
        f"abs_err={uniform_err:.3e}, tol={ANCHOR_UNIFORM_RATE_TOL:.1e}",
    )

    print(
        f"landed alternating anchor via recurrence: eps={ANCHOR_ALTERNATING_EPS}, "
        f"product={alternating.c_ratio:.16g}, frozen={ANCHOR_ALTERNATING_PRODUCT:.16g}"
    )
    check(
        "S0 landed alternating two-step c-product is 1",
        alternating_err <= ANCHOR_ALTERNATING_PRODUCT_TOL,
        f"abs_err={alternating_err:.3e}, tol={ANCHOR_ALTERNATING_PRODUCT_TOL:.1e}",
    )

    print(
        f"anti-fabrication trajectory: eps={ANCHOR_TRAJECTORY_EPS}, "
        f"p_values={[f'{x:.6g}' for x in trajectory.p_values]}, "
        f"max_step_spread={max_step_spread:.6g}"
    )
    check(
        "S0 anti-fabrication: p-trajectory is nonconstant on the frozen word",
        max_step_spread >= ANCHOR_TRAJECTORY_MIN_STEP_SPREAD,
        (
            f"max_step_spread={max_step_spread:.3e}, "
            f"min_required={ANCHOR_TRAJECTORY_MIN_STEP_SPREAD:.1e}"
        ),
    )


def r1_substitution_identity() -> None:
    section("R1 rapidity substitution")
    phi, theta = sp.symbols("phi theta")
    residuals = []
    for s in R1_SIGNS:
        step_after_substitution = (sp.tanh(phi) + s * sp.tanh(theta)) / (
            1 + s * sp.tanh(theta) * sp.tanh(phi)
        )
        target = sp.tanh(phi + s * theta)
        residuals.append(sp.trigsimp(step_after_substitution - target))

    print(f"sympy tanh-addition residuals: {residuals}")
    check(
        "R1 sympy: p -> (p+s eps)/(1+s eps p) is tanh(phi+s theta)",
        residuals[0] == SYMPY_ZERO and residuals[1] == SYMPY_ZERO,
        f"s=+ residual={residuals[0]}, s=- residual={residuals[1]}",
    )


def r2_abelianization() -> None:
    section("R2 abelianization on fixed words")
    max_path_err = 0.0
    worst = ""

    for eps in EPS_GRID:
        theta = math.atanh(eps)
        for p0 in P0_GRID:
            phi0 = math.atanh(p0)
            for signs in RAPIDITY_WORDS:
                path = run_path(eps, p0, signs)
                sign_sum = 0
                for j, s in enumerate(signs, start=1):
                    sign_sum += s
                    target = math.tanh(phi0 + sign_sum * theta)
                    err = abs(path.p_values[j] - target)
                    if err > max_path_err:
                        max_path_err = err
                        worst = (
                            f"eps={eps:g}, p0={p0:g}, word={word_label(signs)}, "
                            f"j={j}, S_j={sign_sum}"
                        )

    print(f"fixed-grid abelianized path max_err={max_path_err:.3e}, worst={worst}")
    check(
        "R2 numeric: p_j = tanh(phi_0 + S_j theta) on fixed nonperiodic words",
        max_path_err <= RAPIDITY_NUMERIC_TOL,
        f"max_err={max_path_err:.3e}, tol={RAPIDITY_NUMERIC_TOL:.1e}",
    )


def r3_complete_c_law() -> None:
    section("R3 complete c-law")
    x = sp.symbols("x")
    sech_residual = sp.trigsimp(1 - sp.tanh(x) ** 2 - sp.sech(x) ** 2)
    print(f"sympy sech residual: {sech_residual}")
    check(
        "R3 sympy: 1 - tanh(x)^2 equals sech(x)^2",
        sech_residual == SYMPY_ZERO,
        f"residual={sech_residual}",
    )

    max_c_err = 0.0
    worst_c = ""
    for eps in EPS_GRID:
        theta = math.atanh(eps)
        for p0 in P0_GRID:
            phi0 = math.atanh(p0)
            sech_phi0 = sech(phi0)
            for signs in R3_FIXED_WORDS:
                path = run_path(eps, p0, signs)
                sign_sum = sum(signs)
                endpoint_ratio = (1.0 - path.p_values[-1] ** 2) / (1.0 - p0 * p0)
                sech_ratio = (sech(phi0 + sign_sum * theta) / sech_phi0) ** 2
                err = max(
                    abs(path.c_ratio - endpoint_ratio),
                    abs(path.c_ratio - sech_ratio),
                    abs(endpoint_ratio - sech_ratio),
                )
                if err > max_c_err:
                    max_c_err = err
                    worst_c = f"eps={eps:g}, p0={p0:g}, word={word_label(signs)}"

    print(f"fixed-grid c-law max_err={max_c_err:.3e}, worst={worst_c}")
    check(
        "R3 numeric: recurrence c_n/c_0 equals endpoint and sech-square laws",
        max_c_err <= RAPIDITY_NUMERIC_TOL,
        f"max_err={max_c_err:.3e}, tol={RAPIDITY_NUMERIC_TOL:.1e}",
    )

    max_wave_rate_err = 0.0
    worst_rate = ""
    for eps in EPS_GRID:
        for signs in WAVE10_PERIODIC_WORDS:
            measured = periodic_rate_after_warmup(eps, signs)
            matrix = matrix_rate_law(eps, signs)
            imbalance = imbalance_rate_law(eps, signs)
            err = max(abs(measured - matrix), abs(measured - imbalance), abs(matrix - imbalance))
            if err > max_wave_rate_err:
                max_wave_rate_err = err
                worst_rate = (
                    f"eps={eps:g}, word={word_label(signs)}, "
                    f"D={sum(signs)}, measured={measured:.16g}, "
                    f"matrix={matrix:.16g}, imbalance={imbalance:.16g}"
                )

    print(f"wave-10 periodic rate max_err={max_wave_rate_err:.3e}, worst={worst_rate}")
    check(
        "R3 wave-10 rates reproduce recurrence, det(M_w)/lambda_max^2, and r^|D|",
        max_wave_rate_err <= PERIODIC_RATE_TOL,
        f"max_err={max_wave_rate_err:.3e}, tol={PERIODIC_RATE_TOL:.1e}",
    )


def r4_imbalance_law() -> None:
    section("R4 periodic imbalance law")
    max_rate_err = 0.0
    worst = ""

    for eps in EPS_GRID:
        for signs in R4_PERIODIC_WORDS:
            matrix = matrix_rate_law(eps, signs)
            imbalance = imbalance_rate_law(eps, signs)
            err = abs(matrix - imbalance)
            if err > max_rate_err:
                max_rate_err = err
                worst = (
                    f"eps={eps:g}, word={word_label(signs)}, D={sum(signs)}, "
                    f"matrix={matrix:.16g}, imbalance={imbalance:.16g}"
                )

    print(f"periodic imbalance-law max_err={max_rate_err:.3e}, worst={worst}")
    check(
        "R4 numeric: per-period rate is r(eps)^|D| on the fixed periodic set",
        max_rate_err <= PERIODIC_RATE_TOL,
        f"max_err={max_rate_err:.3e}, tol={PERIODIC_RATE_TOL:.1e}",
    )

    max_uniform_err = 0.0
    max_alternating_err = 0.0
    for eps in EPS_GRID:
        uniform_matrix = matrix_rate_law(eps, R4_UNIFORM_PERIOD)
        uniform_target = imbalance_rate_law(eps, R4_UNIFORM_PERIOD)
        alternating_matrix = matrix_rate_law(eps, R4_ALTERNATING_PERIOD)
        max_uniform_err = max(max_uniform_err, abs(uniform_matrix - uniform_target))
        max_alternating_err = max(max_alternating_err, abs(alternating_matrix - 1.0))

    print(
        f"uniform D=T max_err={max_uniform_err:.3e}; "
        f"alternating D=0 max_err={max_alternating_err:.3e}"
    )
    check(
        "R4 uniform words recover D=T, rate r(eps)^T",
        max_uniform_err <= PERIODIC_RATE_TOL,
        f"max_err={max_uniform_err:.3e}, tol={PERIODIC_RATE_TOL:.1e}",
    )
    check(
        "R4 alternating words recover D=0, rate 1",
        max_alternating_err <= PERIODIC_RATE_TOL,
        f"max_err={max_alternating_err:.3e}, tol={PERIODIC_RATE_TOL:.1e}",
    )


def r5_seeded_stretched_decay_identity() -> None:
    section("R5 seeded stretched-decay identity")
    mp.mp.dps = R5_MP_DPS
    eps = mp.mpf(str(R5_EPS))
    p0 = mp.mpf(str(R5_P0))
    theta = mp.atanh(eps)
    phi0 = mp.atanh(p0)
    sech_phi0 = 1 / mp.cosh(phi0)
    max_log_err = mp.mpf("0")
    worst = ""
    illustration: dict[int, tuple[int, float, float, float]] = {}

    for seed in R5_SEEDS:
        rng = random.Random(seed)
        p = p0
        c = mp.mpf("1")
        sign_sum = 0
        for n in range(1, R5_N + 1):
            s = 1 if rng.random() < 0.5 else -1
            c *= (1 - eps * eps) / (1 + s * eps * p) ** 2
            p = (p + s * eps) / (1 + s * eps * p)
            sign_sum += s
            log_recurrence = mp.log(c)
            log_closed = 2 * mp.log((1 / mp.cosh(phi0 + sign_sum * theta)) / sech_phi0)
            err = abs(log_recurrence - log_closed)
            if err > max_log_err:
                max_log_err = err
                worst = f"seed={seed}, n={n}, S_n={sign_sum}"
            if seed == R5_PRINT_SEED and n in R5_PRINT_STEPS:
                sqrt_ratio = abs(sign_sum) / math.sqrt(float(n))
                lead = float(-2 * theta * abs(sign_sum))
                illustration[n] = (sign_sum, sqrt_ratio, float(log_closed), lead)

    print(
        f"fixed seeds={R5_SEEDS}, eps={R5_EPS}, p0={R5_P0}, "
        f"N={R5_N}, max_log_err={float(max_log_err):.3e}, worst={worst}"
    )
    for n in R5_PRINT_STEPS:
        sign_sum, sqrt_ratio, log_closed, lead = illustration[n]
        print(
            f"seed {R5_PRINT_SEED} trajectory n={n}: S_n={sign_sum}, "
            f"|S_n|/sqrt(n)={sqrt_ratio:.6g}, log(c_n/c_0)={log_closed:.6g}, "
            f"-2 theta |S_n|={lead:.6g}"
        )

    check(
        "R5 high-precision recurrence log(c_n/c_0) equals the sech-square identity",
        float(max_log_err) <= R5_LOG_ID_TOL,
        f"max_err={float(max_log_err):.3e}, tol={R5_LOG_ID_TOL:.1e}",
    )


def main() -> int:
    print("Erosion rapidity abelianization verification")
    print("Recurrence: p_s=(p+s eps)/(1+s eps p), c_s=c*(1-eps^2)/(1+s eps p)^2")
    s0_anchors()
    r1_substitution_identity()
    r2_abelianization()
    r3_complete_c_law()
    r4_imbalance_law()
    r5_seeded_stretched_decay_identity()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
