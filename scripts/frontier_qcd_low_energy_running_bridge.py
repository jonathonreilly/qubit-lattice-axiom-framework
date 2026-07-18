#!/usr/bin/env python3
"""QCD v -> M_Z supplied-input transfer-map theorem.

The exact one-loop result is analytic on D = [0.085, 0.130].  The two-loop
object is the explicitly defined piecewise QCD EFT map

    d alpha_s / d ln(mu)
      = -beta_0 alpha_s^2/(2 pi) - beta_1 alpha_s^3/(8 pi^2),

with n_f=6 from v to m_t, n_f=5 from m_t to M_Z, and the supplied identity
matching prescription alpha_s^(5)(m_t) := alpha_s^(6)(m_t).  No electroweak
coupling or un-decoupled top Yukawa is evolved below the threshold.

Normal mode checks the group factors, coefficient/factor conventions, exact
one-loop formula, the complete declared ten-point grid, two independent
solve_ivp methods, and the implicit analytic two-loop solution on each
constant-n_f segment.  ``--independent`` reconstructs the key values with a
separate fixed-step RK4 implementation.  ``--hostile`` verifies that seven
computed mutations are detected, including a counterexample to interpreting
the one-loop-to-two-loop difference as a remainder bound.

Deterministic; self-contained except for NumPy and SciPy.
"""
from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass
from fractions import Fraction

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


PASS_COUNT = 0
FAIL_COUNT = 0

PI = math.pi
V_SCALE = 246.282818290129
M_T = 172.69
M_Z = 91.1876

A_MIN = 0.085
A_MAX = 0.130
A_CENTER = (A_MIN + A_MAX) / 2.0
GRID = np.linspace(A_MIN, A_MAX, 10)


@dataclass(frozen=True)
class Segment:
    mu_start: float
    mu_end: float
    n_f: int


MATCHED_SEGMENTS = (
    Segment(V_SCALE, M_T, 6),
    Segment(M_T, M_Z, 5),
)
NF6_ONLY_SEGMENTS = (Segment(V_SCALE, M_Z, 6),)
NF5_ONLY_SEGMENTS = (Segment(V_SCALE, M_Z, 5),)
WRONG_FLAVOR_SEGMENTS = (
    Segment(V_SCALE, M_T, 5),
    Segment(M_T, M_Z, 6),
)
REVERSED_SEGMENTS = (
    Segment(M_Z, M_T, 5),
    Segment(M_T, V_SCALE, 6),
)


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")
    return condition


# ---------------------------------------------------------------------------
# SU(3) factors and beta-function conventions
# ---------------------------------------------------------------------------

def gell_mann_generators() -> list[np.ndarray]:
    """Return T^a=lambda^a/2 in the fundamental representation."""
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    l3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    l8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / math.sqrt(3.0)
    return [matrix / 2.0 for matrix in (l1, l2, l3, l4, l5, l6, l7, l8)]


def derive_group_factors() -> tuple[float, float, float, float, float, float]:
    """Compute T_F, C_A, and C_F, returning their matrix residuals too."""
    generators = gell_mann_generators()
    count = len(generators)
    traces = np.array(
        [[np.trace(generators[a] @ generators[b]) for b in range(count)]
         for a in range(count)]
    )
    t_f = float(np.real(traces[0, 0]))
    trace_residual = float(np.max(np.abs(traces - t_f * np.eye(count))))

    structure = np.zeros((count, count, count))
    for a in range(count):
        for b in range(count):
            commutator = generators[a] @ generators[b] - generators[b] @ generators[a]
            for c in range(count):
                structure[a, b, c] = float(
                    np.real(-1j * np.trace(commutator @ generators[c]) / t_f)
                )
    adjoint = np.einsum("acd,bcd->ab", structure, structure)
    c_a = float(adjoint[0, 0])
    adjoint_residual = float(np.max(np.abs(adjoint - c_a * np.eye(count))))

    casimir = sum(generator @ generator for generator in generators)
    c_f = float(np.real(casimir[0, 0]))
    fundamental_residual = float(np.max(np.abs(casimir - c_f * np.eye(3))))
    return t_f, c_a, c_f, trace_residual, adjoint_residual, fundamental_residual


def beta_coefficients(
    n_f: int,
    c_a: float = 3.0,
    c_f: float = 4.0 / 3.0,
    t_f: float = 0.5,
) -> tuple[float, float]:
    """Return beta_0 and beta_1 in dg/dln(mu)'s standard convention."""
    beta_0 = (11.0 / 3.0) * c_a - (4.0 / 3.0) * t_f * n_f
    beta_1 = ((34.0 / 3.0) * c_a ** 2
              - ((20.0 / 3.0) * c_a + 4.0 * c_f) * t_f * n_f)
    return beta_0, beta_1


def beta_g(g: float, n_f: int) -> float:
    """Two-loop dg/dln(mu) convention used for the conversion check."""
    beta_0, beta_1 = beta_coefficients(n_f)
    loop = 16.0 * PI ** 2
    return -beta_0 * g ** 3 / loop - beta_1 * g ** 5 / loop ** 2


def beta_alpha(
    alpha: float,
    n_f: int,
    *,
    beta1_multiplier: float = 1.0,
    two_loop_factor: float = 1.0,
    flow_sign: float = -1.0,
) -> float:
    """Two-loop d alpha_s/dln(mu); optional controls are hostile fixtures."""
    beta_0, beta_1 = beta_coefficients(n_f)
    magnitude = (beta_0 * alpha ** 2 / (2.0 * PI)
                 + two_loop_factor * beta1_multiplier
                 * beta_1 * alpha ** 3 / (8.0 * PI ** 2))
    return flow_sign * magnitude


# ---------------------------------------------------------------------------
# Exact one-loop and numerical/implicit two-loop transfer maps
# ---------------------------------------------------------------------------

def one_loop_L() -> float:
    beta0_6, _ = beta_coefficients(6)
    beta0_5, _ = beta_coefficients(5)
    return (beta0_6 * math.log(V_SCALE / M_T)
            + beta0_5 * math.log(M_T / M_Z)) / (2.0 * PI)


def t1_closed(alpha: float) -> float:
    return alpha / (1.0 - one_loop_L() * alpha)


def t1_jacobian(alpha: float) -> float:
    return 1.0 / (1.0 - one_loop_L() * alpha) ** 2


def transfer_numeric(
    alpha: float,
    segments: tuple[Segment, ...] = MATCHED_SEGMENTS,
    *,
    method: str = "RK45",
    beta1_multiplier: float = 1.0,
    two_loop_factor: float = 1.0,
    flow_sign: float = -1.0,
) -> float:
    """Integrate the declared piecewise map, carrying alpha identically at markers."""
    current = float(alpha)
    for segment in segments:
        solution = solve_ivp(
            lambda _t, y: [
                beta_alpha(
                    float(y[0]),
                    segment.n_f,
                    beta1_multiplier=beta1_multiplier,
                    two_loop_factor=two_loop_factor,
                    flow_sign=flow_sign,
                )
            ],
            (math.log(segment.mu_start), math.log(segment.mu_end)),
            [current],
            method=method,
            rtol=1e-12,
            atol=1e-14,
        )
        if not solution.success:
            raise RuntimeError(f"two-loop segment failed: {solution.message}")
        current = float(solution.y[0, -1])
    return current


def transfer_one_loop_numeric(alpha: float) -> float:
    current = float(alpha)
    for segment in MATCHED_SEGMENTS:
        beta_0, _ = beta_coefficients(segment.n_f)
        solution = solve_ivp(
            lambda _t, y: [-beta_0 * float(y[0]) ** 2 / (2.0 * PI)],
            (math.log(segment.mu_start), math.log(segment.mu_end)),
            [current],
            rtol=1e-13,
            atol=1e-15,
        )
        if not solution.success:
            raise RuntimeError(f"one-loop segment failed: {solution.message}")
        current = float(solution.y[0, -1])
    return current


def implicit_primitive(alpha: float, n_f: int) -> float:
    """Primitive Phi with Phi(alpha_out)-Phi(alpha_in)=A ln(mu_out/mu_in)."""
    beta_0, beta_1 = beta_coefficients(n_f)
    c = beta_1 / (4.0 * PI * beta_0)
    return 1.0 / alpha + c * math.log(alpha / (1.0 + c * alpha))


def implicit_segment(alpha: float, segment: Segment) -> float:
    """Solve one constant-n_f two-loop segment from its implicit formula."""
    beta_0, _ = beta_coefficients(segment.n_f)
    target = (implicit_primitive(alpha, segment.n_f)
              + beta_0 * math.log(segment.mu_end / segment.mu_start) / (2.0 * PI))

    def residual(candidate: float) -> float:
        return implicit_primitive(candidate, segment.n_f) - target

    if segment.mu_end < segment.mu_start:
        lower = alpha
        upper = max(2.0 * alpha, alpha + 0.05)
        while residual(lower) * residual(upper) > 0.0:
            upper *= 1.5
            if upper > 10.0:
                raise RuntimeError("failed to bracket downward implicit solution")
    else:
        lower = max(1e-12, alpha / 2.0)
        upper = alpha
        while residual(lower) * residual(upper) > 0.0:
            lower /= 2.0
            if lower < 1e-15:
                raise RuntimeError("failed to bracket upward implicit solution")
    return float(brentq(residual, lower, upper, xtol=1e-14, rtol=1e-14))


def transfer_implicit(
    alpha: float,
    segments: tuple[Segment, ...] = MATCHED_SEGMENTS,
) -> float:
    current = float(alpha)
    for segment in segments:
        current = implicit_segment(current, segment)
    return current


def transfer_with_unconstrained_third_coefficient(alpha: float, coefficient: float) -> float:
    """Hostile counterexample family; coefficient is not a physical beta_2 input."""
    current = float(alpha)
    for segment in MATCHED_SEGMENTS:
        def rhs(_t: float, y: np.ndarray) -> list[float]:
            value = float(y[0])
            return [beta_alpha(value, segment.n_f)
                    - coefficient * value ** 4 / (32.0 * PI ** 3)]

        solution = solve_ivp(
            rhs,
            (math.log(segment.mu_start), math.log(segment.mu_end)),
            [current],
            rtol=1e-12,
            atol=1e-14,
        )
        if not solution.success:
            raise RuntimeError(f"hostile higher-term segment failed: {solution.message}")
        current = float(solution.y[0, -1])
    return current


# ---------------------------------------------------------------------------
# Normal certificate
# ---------------------------------------------------------------------------

def run_normal() -> None:
    print("=== Coefficients and convention conversion ===")
    t_f, c_a, c_f, tr_res, ca_res, cf_res = derive_group_factors()
    check(
        "Gell-Mann matrices give T_F=1/2, C_A=3, C_F=4/3",
        abs(t_f - 0.5) < 1e-14
        and abs(c_a - 3.0) < 1e-12
        and abs(c_f - 4.0 / 3.0) < 1e-14
        and max(tr_res, ca_res, cf_res) < 2e-12,
        f"T_F={t_f:.15f}, C_A={c_a:.15f}, C_F={c_f:.15f}",
    )
    beta0_6, beta1_6 = beta_coefficients(6, c_a, c_f, t_f)
    beta0_5, beta1_5 = beta_coefficients(5, c_a, c_f, t_f)
    check(
        "derived coefficients are (beta_0,beta_1)_6=(7,26) and "
        "(beta_0,beta_1)_5=(23/3,116/3)",
        abs(beta0_6 - 7.0) < 1e-12
        and abs(beta1_6 - 26.0) < 1e-12
        and abs(beta0_5 - 23.0 / 3.0) < 1e-12
        and abs(beta1_5 - 116.0 / 3.0) < 1e-12,
        f"nf6=({beta0_6:.12f},{beta1_6:.12f}), "
        f"nf5=({beta0_5:.12f},{beta1_5:.12f})",
    )
    conversion_residuals = []
    for n_f in (5, 6):
        for alpha in GRID:
            g = math.sqrt(4.0 * PI * float(alpha))
            converted = g * beta_g(g, n_f) / (2.0 * PI)
            conversion_residuals.append(abs(converted - beta_alpha(float(alpha), n_f)))
    check(
        "alpha_s=g^2/(4 pi) converts the g RGE to the declared alpha_s RGE",
        max(conversion_residuals) < 2e-16,
        f"max chain-rule residual={max(conversion_residuals):.3e}",
    )

    print("\n=== Exact one-loop theorem on D ===")
    length = one_loop_L()
    pole = 1.0 / length
    check(
        "exact one-loop denominator stays positive on all of D",
        1.0 - length * A_MAX > 0.0,
        f"L={length:.13f}, 1/L={pole:.6f}, pole/a_max={pole/A_MAX:.4f}",
    )
    one_loop_residual = max(
        abs(t1_closed(float(alpha)) - transfer_one_loop_numeric(float(alpha)))
        for alpha in GRID
    )
    check(
        "1/T_1=1/a-L matches independent one-loop integration at every grid point",
        one_loop_residual < 2e-12,
        f"max residual={one_loop_residual:.3e}",
    )
    check(
        "T_1 is strictly increasing and expansive everywhere on D",
        t1_jacobian(A_MIN) > 1.0,
        f"min analytic Jacobian={t1_jacobian(A_MIN):.6f}",
    )

    print("\n=== Piecewise two-loop QCD finite-grid certificate ===")
    rk45 = [transfer_numeric(float(alpha), method="RK45") for alpha in GRID]
    dop853 = [transfer_numeric(float(alpha), method="DOP853") for alpha in GRID]
    implicit = [transfer_implicit(float(alpha)) for alpha in GRID]
    cross_integrator = max(abs(left - right) for left, right in zip(rk45, dop853))
    cross_implicit = max(abs(left - right) for left, right in zip(rk45, implicit))
    check(
        "T_2 is finite and positive at every point of the declared ten-point grid",
        all(math.isfinite(value) and value > 0.0 for value in rk45),
        f"grid image=[{rk45[0]:.9f},{rk45[-1]:.9f}]",
    )
    check(
        "RK45 and DOP853 agree at every declared grid point",
        cross_integrator < 2e-11,
        f"max residual={cross_integrator:.3e}",
    )
    check(
        "numerical integration matches the implicit analytic solution segment by segment",
        cross_implicit < 2e-11,
        f"max grid residual={cross_implicit:.3e}",
    )
    slopes = [
        (rk45[index + 1] - rk45[index]) / (GRID[index + 1] - GRID[index])
        for index in range(len(GRID) - 1)
    ]
    check(
        "finite observation: T_2 values increase and all adjacent grid secants exceed one",
        all(rk45[index + 1] > rk45[index] for index in range(len(rk45) - 1))
        and min(slopes) > 1.0,
        f"min adjacent secant={min(slopes):.6f}",
    )
    center_target = transfer_numeric(A_CENTER)
    center_back = brentq(
        lambda alpha: transfer_numeric(alpha) - center_target,
        A_MIN,
        A_MAX,
        xtol=1e-12,
    )
    check(
        "finite observation: center inverse round-trip recovers the supplied input",
        abs(center_back - A_CENTER) < 1e-9,
        f"round-trip residual={abs(center_back-A_CENTER):.3e}",
    )

    print("\n=== Threshold observations and order-to-order shift ===")
    nf6_only = [transfer_numeric(float(alpha), NF6_ONLY_SEGMENTS) for alpha in GRID]
    nf5_only = [transfer_numeric(float(alpha), NF5_ONLY_SEGMENTS) for alpha in GRID]
    lower_gaps = [matched - lower for matched, lower in zip(rk45, nf6_only)]
    upper_gaps = [upper - matched for upper, matched in zip(nf5_only, rk45)]
    check(
        "finite observation on all ten grid points: nf6-only < matched < nf5-only",
        min(lower_gaps) > 0.0 and min(upper_gaps) > 0.0,
        f"minimum lower/upper gaps={min(lower_gaps):.3e}/{min(upper_gaps):.3e}",
    )
    check(
        "removing the threshold changes every declared grid value well above integration residual",
        min(lower_gaps) > 1000.0 * max(cross_integrator, 1e-15),
        f"minimum shift={min(lower_gaps):.3e}",
    )
    shifts = [value - t1_closed(float(alpha)) for value, alpha in zip(rk45, GRID)]
    check(
        "observed one-loop-to-two-loop shift is positive at every declared grid point",
        min(shifts) > 0.0,
        f"observed shift range=[{min(shifts):.3e},{max(shifts):.3e}]",
    )
    hostile_third = transfer_with_unconstrained_third_coefficient(A_CENTER, 5000.0)
    center_shift = center_target - t1_closed(A_CENTER)
    hostile_change = abs(hostile_third - center_target)
    check(
        "counterexample: adjacent-order shift does not bound an unconstrained omitted term",
        hostile_change > abs(center_shift),
        f"hostile next-term change={hostile_change:.3e} > observed shift={abs(center_shift):.3e}",
    )
    print(
        f"\n  center: T_1={t1_closed(A_CENTER):.9f}, "
        f"T_2={center_target:.9f}, observed shift={center_shift:+.3e}"
    )


# ---------------------------------------------------------------------------
# Independent fixed-step reconstruction
# ---------------------------------------------------------------------------

def run_independent() -> None:
    print("=== Independent coefficient and fixed-step RK4 reconstruction ===")

    def independent_coefficients(n_f: int) -> tuple[float, float]:
        c_a = Fraction(3, 1)
        c_f = Fraction(4, 3)
        t_f = Fraction(1, 2)
        beta_0 = Fraction(11, 3) * c_a - Fraction(4, 3) * t_f * n_f
        beta_1 = (Fraction(34, 3) * c_a ** 2
                  - (Fraction(20, 3) * c_a + 4 * c_f) * t_f * n_f)
        return float(beta_0), float(beta_1)

    def independent_rhs(alpha: float, n_f: int) -> float:
        beta_0, beta_1 = independent_coefficients(n_f)
        return (-beta_0 * alpha ** 2 / (2.0 * PI)
                - beta_1 * alpha ** 3 / (8.0 * PI ** 2))

    def fixed_segment(alpha: float, segment: Segment, steps: int = 12000) -> float:
        start = math.log(segment.mu_start)
        end = math.log(segment.mu_end)
        step = (end - start) / steps
        current = alpha
        for _ in range(steps):
            k1 = independent_rhs(current, segment.n_f)
            k2 = independent_rhs(current + 0.5 * step * k1, segment.n_f)
            k3 = independent_rhs(current + 0.5 * step * k2, segment.n_f)
            k4 = independent_rhs(current + step * k3, segment.n_f)
            current += step * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        return current

    def fixed_transfer(alpha: float, segments: tuple[Segment, ...]) -> float:
        current = alpha
        for segment in segments:
            current = fixed_segment(current, segment)
        return current

    reconstructed = [fixed_transfer(float(alpha), MATCHED_SEGMENTS) for alpha in GRID]
    implicit = [transfer_implicit(float(alpha)) for alpha in GRID]
    primary = [transfer_numeric(float(alpha)) for alpha in GRID]
    coeff_residual = max(
        abs(left - right)
        for n_f in (5, 6)
        for left, right in zip(independent_coefficients(n_f), beta_coefficients(n_f))
    )
    check(
        "independent rational group-factor substitution reconstructs beta_0 and beta_1",
        coeff_residual < 1e-14,
        f"max coefficient residual={coeff_residual:.3e}",
    )
    fixed_vs_primary = max(abs(left - right) for left, right in zip(reconstructed, primary))
    fixed_vs_implicit = max(abs(left - right) for left, right in zip(reconstructed, implicit))
    check(
        "independent fixed-step RK4 matches solve_ivp at every declared grid point",
        fixed_vs_primary < 2e-10,
        f"max residual={fixed_vs_primary:.3e}",
    )
    check(
        "independent fixed-step RK4 matches the implicit segment solution",
        fixed_vs_implicit < 2e-10,
        f"max residual={fixed_vs_implicit:.3e}",
    )
    nf6 = [fixed_transfer(float(alpha), NF6_ONLY_SEGMENTS) for alpha in GRID]
    nf5 = [fixed_transfer(float(alpha), NF5_ONLY_SEGMENTS) for alpha in GRID]
    check(
        "independent reconstruction observes the threshold ordering at all ten points",
        all(low < middle < high for low, middle, high in zip(nf6, reconstructed, nf5)),
        f"center triple={nf6[4]:.9f}/{reconstructed[4]:.9f}/{nf5[4]:.9f}",
    )
    check(
        "independent grid is strictly increasing",
        all(reconstructed[index + 1] > reconstructed[index]
            for index in range(len(reconstructed) - 1)),
        f"grid image=[{reconstructed[0]:.9f},{reconstructed[-1]:.9f}]",
    )
    print("\n  independently reconstructed grid:")
    for alpha, value in zip(GRID, reconstructed):
        print(f"    a={float(alpha):.6f} -> T_2(a)={value:.9f}")


# ---------------------------------------------------------------------------
# Hostile computed mutations
# ---------------------------------------------------------------------------

def run_hostile() -> None:
    print("=== Hostile computed mutation kills ===")
    correct = [transfer_implicit(float(alpha)) for alpha in GRID]
    separation = 1e-7

    wrong_beta1 = [
        transfer_numeric(float(alpha), beta1_multiplier=0.0) for alpha in GRID
    ]
    check(
        "kills wrong beta_1 (omitted two-loop coefficient)",
        max(abs(left - right) for left, right in zip(correct, wrong_beta1)) > separation,
    )

    wrong_factor = [
        transfer_numeric(float(alpha), two_loop_factor=2.0) for alpha in GRID
    ]
    check(
        "kills wrong factor of two in the two-loop alpha_s term",
        max(abs(left - right) for left, right in zip(correct, wrong_factor)) > separation,
    )

    wrong_sign = [
        transfer_numeric(float(alpha), flow_sign=1.0) for alpha in GRID
    ]
    check(
        "kills the beta-function sign flip",
        all(value < float(alpha) for value, alpha in zip(wrong_sign, GRID)),
    )

    missing_threshold = [
        transfer_numeric(float(alpha), NF6_ONLY_SEGMENTS) for alpha in GRID
    ]
    check(
        "kills the missing-threshold mutation",
        min(abs(left - right) for left, right in zip(correct, missing_threshold)) > separation,
    )

    wrong_flavor = [
        transfer_numeric(float(alpha), WRONG_FLAVOR_SEGMENTS) for alpha in GRID
    ]
    check(
        "kills wrong segment flavor assignment (n_f=5 above, n_f=6 below)",
        min(abs(left - right) for left, right in zip(correct, wrong_flavor)) > separation,
    )

    reversed_direction = [
        transfer_numeric(float(alpha), REVERSED_SEGMENTS) for alpha in GRID
    ]
    check(
        "kills reversed scale direction",
        all(value < float(alpha) for value, alpha in zip(reversed_direction, GRID)),
    )

    two_loop = transfer_implicit(A_CENTER)
    observed_shift = abs(two_loop - t1_closed(A_CENTER))
    unconstrained_next = transfer_with_unconstrained_third_coefficient(A_CENTER, 5000.0)
    check(
        "kills false remainder/envelope semantics with a computed higher-term counterexample",
        abs(unconstrained_next - two_loop) > observed_shift,
        f"counterexample change={abs(unconstrained_next-two_loop):.3e}, "
        f"adjacent-order shift={observed_shift:.3e}",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--independent", action="store_true")
    mode.add_argument("--hostile", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print("=" * 78)
    print("QCD v -> M_Z supplied-input transfer-map theorem")
    print("=" * 78)
    if args.independent:
        run_independent()
    elif args.hostile:
        run_hostile()
    else:
        run_normal()
    print(f"\nSUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
