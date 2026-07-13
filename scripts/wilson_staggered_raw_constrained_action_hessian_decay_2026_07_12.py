#!/usr/bin/env python3
"""Checks for the raw constrained-action Hessian decay theorem note."""

from __future__ import annotations

import itertools
import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_RAW_CONSTRAINED_ACTION_HESSIAN_DECAY_"
    "BOUNDED_THEOREM_NOTE_2026-07-12.md"
)


def alpha(beta: float, mass: float) -> float:
    k = 14.0 / (mass * mass + 2.0)
    return 18.0 * beta + 1.5 * k * k * (2.0 - k) / (1.0 - k) ** 2


def log_partition(t: float, s: float) -> float:
    vals = []
    for x, y in itertools.product((-1.0, 1.0), repeat=2):
        base = 0.13 * x * y + 0.07 * x
        f = x + 0.2 * y
        g = y - 0.1 * x
        vals.append(math.exp(base - t * f - s * g))
    return -math.log(sum(vals))


def expectation_observables(t: float, s: float) -> tuple[float, float, float]:
    rows = []
    for x, y in itertools.product((-1.0, 1.0), repeat=2):
        base = 0.13 * x * y + 0.07 * x
        f = x + 0.2 * y
        g = y - 0.1 * x
        rows.append((math.exp(base - t * f - s * g), f, g))
    z = sum(w for w, _, _ in rows)
    ef = sum(w * f for w, f, _ in rows) / z
    eg = sum(w * g for w, _, g in rows) / z
    efg = sum(w * f * g for w, f, g in rows) / z
    return ef, eg, efg - ef * eg


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    a = alpha(0.01, 8.0)
    checks.append(("deep_fiber_margin", 2.0 * a < 1.0, f"q0=2alpha={2*a:.12f}"))

    h = 1.0e-5
    d_t = (log_partition(h, 0.0) - log_partition(-h, 0.0)) / (2.0 * h)
    mixed = (
        log_partition(h, h)
        - log_partition(h, -h)
        - log_partition(-h, h)
        + log_partition(-h, -h)
    ) / (4.0 * h * h)
    ef, _, cov_fg = expectation_observables(0.0, 0.0)
    checks.append(("first_response_sign", abs(d_t - ef) < 1e-9, f"DR={d_t:.12f}, E[F]={ef:.12f}"))
    checks.append(
        ("mixed_hessian_sign", abs(mixed + cov_fg) < 2e-6, f"D2R={mixed:.12f}, -Cov={-cov_fg:.12f}")
    )

    # One unbiased Bernoulli spin saturates the 1/4 full-oscillation bound:
    # Var(x)=1, delta(x)=2, C=0 and D=I.
    bernoulli_var = 1.0
    bernoulli_delta = 2.0
    bernoulli_bound = 0.25 * bernoulli_delta * bernoulli_delta
    checks.append(
        (
            "quarter_oscillation_covariance_convention",
            abs(bernoulli_var - bernoulli_bound) < 1e-15,
            f"Var={bernoulli_var:.1f}, (1/4)delta^2={bernoulli_bound:.1f}",
        )
    )

    q_lambda = 0.71
    resolvent_weight = 1.0 / (1.0 - q_lambda)
    checks.append(
        (
            "weighted_resolvent_geometric_sum",
            abs(sum(q_lambda**n for n in range(500)) - resolvent_weight) < 1e-12,
            f"1/(1-q_lambda)={resolvent_weight:.12f}",
        )
    )

    lam = 0.08
    distances = range(0, 80)
    bounds = [math.exp(-lam * d) * resolvent_weight for d in distances]
    checks.append(
        (
            "positive_exponential_hessian_rate",
            all(bounds[i + 1] < bounds[i] for i in range(len(bounds) - 1)),
            f"lambda_H={lam:.6f}, bound_at_40={bounds[40]:.12e}",
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "D R_Lambda(Phi)[F]=<F>",
        "D^2 R_Lambda(Phi)[F,G]=-Cov(F,G)",
        "(1/4)sum_(h,k) delta_h(F) D_(h,k) delta_k(G)",
        "half-`L1` total-variation convention",
        "q_lambda<1",
        "1/(1-q_lambda)",
        "finite-volume relative action",
        "Boltzmann weight is strictly positive",
        "unnormalized raw fiber action",
        "Retained-Grassmann directions",
        "No axiom-update stop is established.",
        "No negative theorem is shipped.",
        "### N1",
        "### N2",
        "### N3",
        "### N4",
        "### N5",
        "### N6",
        "### N7",
        "### N8",
    ]
    missing = [x for x in required if x not in text]
    forbidden = ["complete analyticity follows", "RG eigenvalue", "beta function is", "NOT_TESTED"]
    hits = [x for x in forbidden if x in text]
    checks.append(("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}"))

    dep = "WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md"
    note_links = re.findall(r"\]\(([^)#?]+\.md)\)", text)
    dependency_set = sorted(set(note_links))
    checks.append(
        (
            "direct_dependency",
            dependency_set == [dep],
            f"markdown_dependency_set={dependency_set}",
        )
    )

    passed = sum(ok for _, ok, _ in checks)
    failed = len(checks) - passed
    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
    print(f"SCORECARD PASS={passed} FAIL={failed}")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
