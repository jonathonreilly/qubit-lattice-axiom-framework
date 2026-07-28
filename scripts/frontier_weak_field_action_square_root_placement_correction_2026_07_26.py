#!/usr/bin/env python3
"""Verify the square-root placement in the weak-field action comparison.

The runner checks five load-bearing statements:

1. ``L*sqrt(1-f)`` and ``L*(1-f)`` have order-one normalized depths,
   whereas ``L*(1-sqrt(f))`` has order-one-half depth.
2. The existing fixed-family probe actually evaluates its ``valley_sqrt``
   branch as ``L*(1-sqrt(f))``.
3. Injecting ``L*sqrt(1-f)`` into the otherwise unchanged fixed-family
   harness gives an order-one response exponent on that tested family.
4. The geometric spent-delay action has order-one-half normalized depth.
5. Rationalized formulas agree with direct evaluation where subtraction is
   numerically safe, including the next coefficient of the stated form.

The fixed-family response check is a bounded replay, not a universal response
law.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

try:
    import numpy as np
except ModuleNotFoundError as exc:  # pragma: no cover - environment-dependent
    raise SystemExit("numpy is required because the reviewed source uses numpy") from exc

import scripts.action_universality_probe as probe


PASSES: list[str] = []
FAILURES: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    (PASSES if ok else FAILURES).append(name)
    suffix = f"  --  {detail}" if detail else ""
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{suffix}")


def estimate_order(depth, x: float, ratio: float = 10.0) -> float:
    return math.log(depth(x * ratio) / depth(x)) / math.log(ratio)


def stated_depth(f: float) -> float:
    """Stable form of 1-sqrt(1-f)."""
    return f / (1.0 + math.sqrt(1.0 - f))


def measured_depth(f: float) -> float:
    return math.sqrt(f)


def valley_linear_depth(f: float) -> float:
    return f


def check_leading_orders() -> None:
    p_linear = estimate_order(valley_linear_depth, 1e-10)
    p_stated = estimate_order(stated_depth, 1e-10)
    p_measured = estimate_order(measured_depth, 1e-10)
    coeff_stated = stated_depth(1e-10) / 1e-10

    ok = (
        abs(p_linear - 1.0) < 1e-9
        and abs(p_stated - 1.0) < 1e-9
        and abs(p_measured - 0.5) < 1e-9
        and abs(coeff_stated - 0.5) < 1e-9
    )
    check(
        "leading normalized-depth orders distinguish the two square-root placements",
        ok,
        (
            f"p[linear]={p_linear:.9f}, p[L*sqrt(1-f)]={p_stated:.9f}, "
            f"p[L*(1-sqrt(f))]={p_measured:.9f}, stated depth/f={coeff_stated:.9f}"
        ),
    )


def check_reviewed_source_branch() -> None:
    f = np.array([1e-8, 1e-7, 1e-6], dtype=float)
    length = 2.75
    actual = np.asarray(probe.action_value(length, f, "valley_sqrt"), dtype=float)
    expected = length * (1.0 - np.sqrt(f))
    source_matches = np.array_equal(actual, expected)

    normalized_depth = 1.0 - actual / length
    p_source = math.log(normalized_depth[1] / normalized_depth[0]) / math.log(f[1] / f[0])
    depth_matches = np.allclose(normalized_depth, np.sqrt(f), rtol=0.0, atol=2e-16)

    check(
        "the reviewed probe source evaluates valley_sqrt as L*(1-sqrt(f))",
        bool(source_matches and depth_matches and abs(p_source - 0.5) < 1e-10),
        f"source-derived order={p_source:.9f}",
    )


def check_stated_formula_on_fixed_family() -> None:
    """Run L*sqrt(1-f) through the unchanged fixed-family measurement code."""
    original_action_value = probe.action_value

    def action_value_with_stated_form(length, field, mode):
        if mode == "stated_sqrt":
            field = np.maximum(field, 0.0)
            return length * np.sqrt(1.0 - field)
        return original_action_value(length, field, mode)

    probe.action_value = action_value_with_stated_form
    try:
        lattice = probe.Lattice3D(probe.PHYS_L, probe.PHYS_W, probe.H)
        row = probe.measure_action(lattice, probe.detector(lattice), "stated_sqrt")
    finally:
        probe.action_value = original_action_value

    ok = (
        row.born < 1e-12
        and row.gravity_z3 > 0.0
        and row.toward_count == 7
        and abs(row.fm_alpha - 1.0) < 1e-3
    )
    check(
        "L*sqrt(1-f) gives an order-one response on the reviewed fixed family",
        ok,
        (
            f"Born={row.born:.3e}, gravity={row.gravity_z3:+.9f}, "
            f"TOWARD={row.toward_count}/7, F~M={row.fm_alpha:.9f}"
        ),
    )


def geometric_depth(epsilon: float) -> float:
    """Normalized depth for dl=L(1+epsilon), in a stable exact form."""
    return math.sqrt(2.0 * epsilon + epsilon * epsilon) - epsilon


def check_geometric_spent_delay() -> None:
    p_geo = estimate_order(geometric_depth, 1e-10)
    epsilons = (1e-5, 1e-7, 1e-9)
    coefficients = [geometric_depth(e) / math.sqrt(2.0 * e) for e in epsilons]
    approaches_one = (
        abs(coefficients[-1] - 1.0) < abs(coefficients[0] - 1.0)
        and abs(coefficients[-1] - 1.0) < 1e-4
    )

    check(
        "the geometric spent-delay depth has leading order one-half",
        abs(p_geo - 0.5) < 1e-4 and approaches_one,
        f"order={p_geo:.9f}, depth/sqrt(2*epsilon)={coefficients[-1]:.9f}",
    )


def check_exact_forms_and_next_coefficient() -> None:
    moderate_points = (1e-3, 1e-2, 0.1, 0.25)
    worst_stated = max(
        abs(stated_depth(f) - (1.0 - math.sqrt(1.0 - f)))
        for f in moderate_points
    )
    worst_measured = max(
        abs(measured_depth(f) - (1.0 - (1.0 - math.sqrt(f))))
        for f in moderate_points
    )

    # From 1-sqrt(1-f) = f/2 + f^2/8 + O(f^3).
    series_points = (1e-3, 5e-4, 2.5e-4)
    second_coefficients = [
        (stated_depth(f) - 0.5 * f) / (f * f)
        for f in series_points
    ]
    next_coefficient_ok = (
        abs(second_coefficients[-1] - 0.125) < abs(second_coefficients[0] - 0.125)
        and abs(second_coefficients[-1] - 0.125) < 1e-4
    )

    check(
        "exact depth formulas and the f^2/8 coefficient agree independently",
        worst_stated < 2e-16 and worst_measured < 2e-16 and next_coefficient_ok,
        (
            f"worst direct mismatch={max(worst_stated, worst_measured):.3e}, "
            f"second coefficient={second_coefficients[-1]:.9f}"
        ),
    )


def main() -> int:
    print("Weak-field action correction: square-root placement and leading order")
    print("=" * 78)
    check_leading_orders()
    check_reviewed_source_branch()
    check_stated_formula_on_fixed_family()
    check_geometric_spent_delay()
    check_exact_forms_and_next_coefficient()
    print("=" * 78)
    print(f"{len(PASSES)} PASS / {len(FAILURES)} FAIL")
    for failure in FAILURES:
        print(f"  FAILED: {failure}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())
