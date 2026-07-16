#!/usr/bin/env python3
"""Checks K-retaining marked attachment and a strong-to-weak contraction point."""

from __future__ import annotations

import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_"
    "CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)


def g(value: float) -> float:
    return math.expm1(value) / value if value else 1.0


def criterion(
    mass: float, beta: float, c: float, theta: float, lam: float, eta: float
) -> dict[str, float]:
    h = 4.0 / mass
    total_weight = theta + 2.0 * c + lam
    q_hop = h * math.exp(total_weight)
    wilson = 12.0 * math.expm1(3.0 * beta / 4.0) * math.exp(4.0 * total_weight)
    determinant = 0.0
    for length in range(4, 10000, 2):
        term = 1.5 * h**length * g(3.0 * h**length / length) * math.exp(length * total_weight)
        determinant += term
        if term < 1.0e-20:
            break
    schur = 0.0
    for length in range(2, 10000):
        x_length = 9.0 * eta**2 * 2.0 ** (-length) * mass ** (-(length - 1))
        term = (
            18.0
            * eta**2
            * length
            * h ** (length - 1)
            * g(x_length)
            * math.exp(length * total_weight)
        )
        schur += term
        if term < 1.0e-20:
            break
    activity = wilson + determinant + schur
    return {
        "q_hop": q_hop,
        "K_W": wilson,
        "K_I": determinant,
        "K_S": schur,
        "K": activity,
        "epsilon": c - activity,
    }


def integer_sup_n_exp(s: float) -> tuple[int, float]:
    if s <= 0.0:
        return 0, math.inf
    critical = 1.0 / s
    candidates = {max(1, math.floor(critical)), max(1, math.ceil(critical))}
    values = [(int(n), n * math.exp(-s * n)) for n in candidates]
    return max(values, key=lambda item: item[1])


def integer_sup_attachment(k_value: float, c: float) -> tuple[int, float]:
    if not 0.0 < k_value < c:
        return 0, math.inf
    critical = -math.log1p(-k_value / c) / k_value
    candidates = {max(1, math.floor(critical)), max(1, math.ceil(critical))}
    values = [
        (int(n), math.exp(-c * n) * math.expm1(k_value * n))
        for n in candidates
    ]
    return max(values, key=lambda item: item[1])


def attachment_constants(k_value: float, c: float) -> dict[str, float]:
    slack = c - k_value
    n_d, d_slack = integer_sup_n_exp(slack)
    n_a, a_zero = integer_sup_attachment(k_value, c)
    tau = k_value * d_slack
    anchored = math.inf
    if tau < 1.0:
        anchored = (a_zero + tau / (1.0 - tau)) / (1.0 - tau)
    return {
        "slack": slack,
        "n_d": float(n_d),
        "d_slack": d_slack,
        "n_a": float(n_a),
        "a_zero": a_zero,
        "tau": tau,
        "A_att": anchored,
    }


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    displayed = [
        (12.0, 0.0005, 0.12, 0.001, 0.001, 0.02),
        (16.0, 0.0010, 0.12, 0.001, 0.001, 0.05),
        (20.0, 0.0025, 0.125, 0.001, 0.001, 0.04),
    ]
    for mass, beta, c, theta, lam, eta in displayed:
        row = criterion(mass, beta, c, theta, lam, eta)
        old_bound = 68.0 * math.exp(lam / 2.0) * c
        new_bound = 68.0 * math.exp(lam / 2.0) * row["K"]
        checks.append(
            (
                f"k_retaining_base_bound_m{mass:g}",
                row["q_hop"] < 1.0
                and 0.0 < row["K"] < c
                and 0.0 < new_bound < old_bound,
                "K={:.12f}, c={:.12f}, old={:.12f}, sharpened={:.12f}".format(
                    row["K"], c, old_bound, new_bound
                ),
            )
        )

    ultra = (1.0e4, 0.0, 0.001, 1.0e-6, 1.0, 1.0e-10)
    mass, beta, c, theta, lam, eta = ultra
    row = criterion(*ultra)
    attachment = attachment_constants(row["K"], c)
    conversion = 68.0 * math.exp(lam / 2.0)
    q_raw = math.exp(-lam / 2.0)
    q_centered = conversion * attachment["A_att"]
    q_strong_weak = max(q_raw, q_centered)
    base_defect = conversion * row["K"]
    checks.append(
        (
            "ultra_deep_anchored_attachment",
            row["q_hop"] < 1.0
            and row["epsilon"] > 0.0
            and attachment["tau"] < 1.0
            and 0.0 < attachment["A_att"] < 2.0e-9
            and q_centered < 2.0e-7,
            "K={:.15e}, slack={:.15e}, d_s={:.12f}@n={}, "
            "a0={:.15e}@n={}, tau={:.15e}, A_att={:.15e}, q_centered={:.15e}".format(
                row["K"],
                attachment["slack"],
                attachment["d_slack"],
                int(attachment["n_d"]),
                attachment["a_zero"],
                int(attachment["n_a"]),
                attachment["tau"],
                attachment["A_att"],
                q_centered,
            ),
        )
    )
    checks.append(
        (
            "strong_to_weak_linear_contraction",
            q_strong_weak < 1.0 and base_defect < 3.0e-10,
            f"q_raw={q_raw:.12f}, q_centered={q_centered:.15e}, q=max={q_strong_weak:.12f}, B_weak={base_defect:.15e}",
        )
    )

    # Independently check the two path-resolvent sums against the closed
    # geometric factors used in the analytic marked-tree rerooting.
    tau = attachment["tau"]
    depth = 12
    first_path_partial = sum(tau**length for length in range(1, depth + 1))
    first_path_closed = tau / (1.0 - tau)
    second_layer_partial = (
        attachment["a_zero"] + first_path_partial
    ) * sum(tau**length for length in range(0, depth + 1))
    checks.append(
        (
            "two_layer_marked_path_resolvent",
            first_path_partial <= first_path_closed + 1.0e-30
            and second_layer_partial <= attachment["A_att"] + 1.0e-30,
            f"tau={tau:.15e}, first_partial={first_path_partial:.15e}, first_closed={first_path_closed:.15e}, two_layer_partial={second_layer_partial:.15e}, A_att={attachment['A_att']:.15e}",
        )
    )

    # Conditional nonlinear feasibility diagnostic. It is deliberately not
    # part of the theorem's autonomous self-map claim.
    source_radius = math.log1p(row["epsilon"])
    delta = 1.0e-8
    hessian = 2.0 * conversion * c / (source_radius - delta) ** 2
    ball_left = base_defect + q_strong_weak * delta + 0.5 * hessian * delta**2
    checks.append(
        (
            "conditional_ball_scalar_feasibility",
            delta < source_radius and ball_left < delta,
            f"r_src={source_radius:.15e}, delta={delta:.1e}, M_delta={hessian:.9f}, lhs={ball_left:.15e}",
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "A_att(K,c)",
        "strong-to-weak",
        "not an autonomous invariant ball",
        "No axiom-update stop",
        "### N1",
        "### N2",
        "### N3",
        "### N4",
        "### N5",
        "### N6",
        "### N7",
        "### N8",
    ]
    missing = [item for item in required if item not in text]
    forbidden = ["proves the critical trajectory", "is a physical fixed point", "NOT_TESTED"]
    hits = [item for item in forbidden if item in text]
    checks.append(("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}"))

    expected_dependencies = sorted(
        [
            "WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_SPLIT_DERIVATIVE_AND_UNLOCALIZED_CAUCHY_CERTIFICATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md",
        ]
    )
    dependencies = sorted(set(re.findall(r"\]\(([^)#?]+\.md)\)", text)))
    checks.append(
        (
            "repository_dependency_set",
            dependencies == expected_dependencies,
            f"markdown_dependency_set={dependencies}",
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
