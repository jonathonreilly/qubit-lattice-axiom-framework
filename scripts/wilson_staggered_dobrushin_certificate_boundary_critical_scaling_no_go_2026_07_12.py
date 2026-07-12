#!/usr/bin/env python3
"""Certificate for Dobrushin-boundary non-identification and scaling rates."""

from __future__ import annotations

from math import exp, isclose
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_DOBRUSHIN_CERTIFICATE_BOUNDARY_CRITICAL_SCALING_"
    "NO_GO_2026-07-12.md"
)
PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name}: {detail}")


def series(q: float) -> float:
    return q * q * (2.0 - q) / (1.0 - q) ** 2


def series_prime(q: float) -> float:
    return (4.0 * q - 3.0 * q * q + q**3) / (1.0 - q) ** 3


def kappa(mass: float) -> float:
    return 14.0 / (mass * mass + 2.0)


def alpha_f(mass: float) -> float:
    return 1.5 * series(kappa(mass))


def alpha_old(beta: float, mass: float) -> float:
    return 18.0 * beta + alpha_f(mass)


def alpha_sharp(beta: float, mass: float) -> float:
    return 13.5 * beta + alpha_f(mass)


def weighted_alpha(beta: float, mass: float, weight: float) -> float:
    factor = exp(2.0 * weight)
    return 13.5 * beta * factor + 1.5 * series(kappa(mass) * factor)


def bisect_kappa_zero() -> float:
    lo, hi = 0.0, 0.9
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if 1.5 * series(mid) < 1.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def main() -> int:
    # The angle reduction is min_{x in [0,1]} 2x^2-2x-1.
    vertex = 0.5
    trace_min = 2.0 * vertex**2 - 2.0 * vertex - 1.0
    trace_endpoints = (-1.0, -1.0)
    check(
        "The exact SU(3) real-trace range has minimum -3/2 and maximum 3",
        isclose(trace_min, -1.5) and all(trace_min <= value for value in trace_endpoints),
        f"quadratic vertex={vertex:.1f}, min={trace_min:.6f}, max(identity)=3",
    )

    per_plaquette_oscillation = (3.0 - (-1.5)) / 3.0
    mixed_oscillation = 2.0 * per_plaquette_oscillation
    per_incidence_tv_linear = mixed_oscillation / 4.0
    wilson_row_coefficient = 18.0 * per_incidence_tv_linear
    check(
        "Exact oscillation sharpens the Wilson row coefficient to 27/2",
        isclose(per_plaquette_oscillation, 1.5)
        and isclose(mixed_oscillation, 3.0)
        and isclose(wilson_row_coefficient, 13.5),
        f"osc(phi)/beta={per_plaquette_oscillation:.3f}, "
        f"osc(change)/beta={mixed_oscillation:.3f}, row/beta={wilson_row_coefficient:.3f}",
    )

    mass = 8.0
    beta_boundary = (1.0 - alpha_f(mass)) / 18.0
    old_value = alpha_old(beta_boundary, mass)
    sharp_value = alpha_sharp(beta_boundary, mass)
    predicted = 1.0 - 4.5 * beta_boundary
    check(
        "A positive-beta point on the old equality curve is strictly inside the sharp wedge",
        isclose(old_value, 1.0, abs_tol=1.0e-14)
        and isclose(sharp_value, predicted, abs_tol=1.0e-14)
        and sharp_value < 0.8,
        f"m=8, beta={beta_boundary:.10f}, old={old_value:.9f}, sharp={sharp_value:.9f}",
    )

    kappa_zero = bisect_kappa_zero()
    q_max = kappa_zero * exp(0.02)
    derivative_bound = 2.0 * exp(0.02) + 3.0 * q_max * series_prime(q_max)
    check(
        "The full sharp-wedge weighted-row derivative is universally below nine",
        0.3916 < kappa_zero < 0.3917 and q_max < 0.4 and derivative_bound < 9.0,
        f"kappa0={kappa_zero:.10f}, qmax={q_max:.10f}, derivative<{derivative_bound:.6f}<9",
    )

    # Sample the exact mean-value consequence throughout the allowed rectangle,
    # retaining only points in the sharp wedge.
    weighted_checks = []
    for mass_sample in (5.82, 6.0, 7.0, 8.0, 10.0, 20.0):
        for beta_fraction in (0.0, 0.2, 0.5, 0.8, 0.99):
            ceiling = max(0.0, (1.0 - alpha_f(mass_sample)) / 13.5)
            beta_sample = beta_fraction * ceiling
            base = alpha_sharp(beta_sample, mass_sample)
            delta = 1.0 - base
            if delta <= 0.0:
                continue
            value = weighted_alpha(beta_sample, mass_sample, delta / 100.0)
            weighted_checks.append((value, 1.0 - delta / 2.0))
    check(
        "Weight lambda=delta/100 retains at least half of every sampled sharp margin",
        weighted_checks and all(value < limit for value, limit in weighted_checks),
        f"checked={len(weighted_checks)}, max(value-limit)="
        f"{max(value - limit for value, limit in weighted_checks):.3e}",
    )

    spacings = (1.0e-2, 1.0e-3, 1.0e-4, 1.0e-5)
    gap_slow = [spacing**0.5 / (100.0 * spacing) for spacing in spacings]
    gap_linear = [spacing / (100.0 * spacing) for spacing in spacings]
    gap_fast = [spacing**1.5 / (100.0 * spacing) for spacing in spacings]
    check(
        "The delta=a^p gap certificate separates divergent, finite, and uninformative regimes",
        all(gap_slow[index + 1] > gap_slow[index] for index in range(3))
        and all(isclose(value, 0.01) for value in gap_linear)
        and all(gap_fast[index + 1] < gap_fast[index] for index in range(3)),
        f"p=.5:{gap_slow[-1]:.3e}, p=1:{gap_linear[-1]:.3e}, p=1.5:{gap_fast[-1]:.3e}",
    )

    mass_floor = (14.0 / kappa_zero - 2.0) ** 0.5
    check(
        "The sharp certificate remains disjoint from weak-beta/light-lattice-mass scaling",
        2.0 / 27.0 < 0.075 and mass_floor > 5.809,
        f"beta<2/27={2.0/27.0:.9f}, m>{mass_floor:.9f}",
    )

    # A product specification has true influence zero. Any nonnegative looser
    # row majorant is valid, including a sequence that tends to one.
    reported_majorants = [1.0 - 1.0 / n for n in (2, 10, 100, 1000)]
    actual_influences = [0.0 for _ in reported_majorants]
    check(
        "Certificate saturation has a zero-influence non-saturation countermodel",
        all(actual <= reported < 1.0 for actual, reported in zip(actual_influences, reported_majorants))
        and reported_majorants[-1] > 0.999 - 1.0e-14,
        "actual rows=0; reported rows=" + ",".join(f"{value:.3f}" for value in reported_majorants),
    )

    text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    required = [
        "**Type:** no_go",
        "alpha_sharp(beta,m)=(27/2)beta+alpha_F(m)",
        "alpha_old=1  implies  alpha_sharp=1-(9/2)beta",
        "delta(a)=O(a)",
        "A worsening upper bound is not a lower bound",
        "does not prove that no physical phase boundary can ever intersect",
        "a product specification has actual",
        "does not trigger an axiom-update stop",
        "No-Go Discipline N1--N8",
        "### N3 — hidden-condition phrase scan",
        "### N4 — citation/residual matching",
        "### N5 — rhetoric and resolution audit",
        "### N6 — partial-closure and primitive scan",
        "### N7 — hostile steelman",
        "### N8 — cross-cycle echo",
        "**No-Go Discipline status: PASS.**",
    ]
    missing = [item for item in required if item not in text]
    attempted = text.count("| `ATTEMPTED` |")
    n2_conditions = [
        "certificate equality",
        "actual correlation-length or spectral scaling",
        "controlled observable normalization",
        "line of constant physics and action trajectory",
    ]
    n2_pairs = [
        f"| {n2_conditions[left]} | {n2_conditions[right]} |"
        for left in range(len(n2_conditions))
        for right in range(left + 1, len(n2_conditions))
    ]
    missing_pairs = [item for item in n2_pairs if item not in text]
    check(
        "Source-note narrow no-go and N1-N8 contract",
        not missing and not missing_pairs and attempted >= 8,
        f"missing={missing}; missing N2 pairs={missing_pairs}; attempted={attempted}",
    )

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
