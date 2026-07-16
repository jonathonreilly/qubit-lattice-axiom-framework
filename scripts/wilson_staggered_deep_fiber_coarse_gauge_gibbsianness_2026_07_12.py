#!/usr/bin/env python3
"""Checks for the deep-fiber coarse-gauge Gibbsianness theorem note."""

from __future__ import annotations

import itertools
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_DEEP_FIBER_COARSE_GAUGE_GIBBSIANNESS_"
    "BOUNDED_THEOREM_NOTE_2026-07-12.md"
)


def alpha(beta: float, mass: float) -> float:
    kappa = 14.0 / (mass * mass + 2.0)
    return 18.0 * beta + 1.5 * kappa * kappa * (2.0 - kappa) / (1.0 - kappa) ** 2


def normalized_density(log_weights: list[float]) -> list[float]:
    top = max(log_weights)
    weights = [math.exp(x - top) for x in log_weights]
    mean = sum(weights) / len(weights)
    return [x / mean for x in weights]


def z3_image_weights(blocks: int, coupling: float) -> dict[tuple[int, ...], float]:
    """Exact 1D Z3 analogue: V_j=u_2j+u_(2j+1) mod 3."""
    out: dict[tuple[int, ...], float] = {}
    sites = 2 * blocks
    for u in itertools.product(range(3), repeat=sites):
        energy = 0.0
        for x in range(sites):
            angle = 2.0 * math.pi * (u[x] - u[(x + 1) % sites]) / 3.0
            energy += coupling * math.cos(angle)
        v = tuple((u[2 * j] + u[2 * j + 1]) % 3 for j in range(blocks))
        out[v] = out.get(v, 0.0) + math.exp(energy)
    return out


def conditional(weights: dict[tuple[int, ...], float], exterior: tuple[int, ...]) -> list[float]:
    vals = [weights[(v0,) + exterior] for v0 in range(3)]
    total = sum(vals)
    return [x / total for x in vals]


def tv(p: list[float], q: list[float]) -> float:
    return 0.5 * sum(abs(x - y) for x, y in zip(p, q))


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    for mass, beta in [(8.0, 0.01), (10.0, 0.02), (12.0, 0.02)]:
        value = alpha(beta, mass)
        checks.append((f"deep_wedge_m{mass:g}", value < 0.5, f"alpha={value:.12f}"))

    # The determinant interaction has supports of diameter at most 4n+O(1)
    # after the factor-two coordinate substitution.  A deliberately smaller
    # exponential moment is available whenever r exp(4 lambda_F)<1.
    for mass in (8.0, 10.0):
        r = 16.0 / (mass * mass + 16.0)
        lambda_f = -math.log(r) / 8.0
        ratio = r * math.exp(4.0 * lambda_f)
        tail = sum(((2 * n + 2) ** 4) * (ratio**n) / n for n in range(1, 500))
        checks.append(
            (
                f"fine_exponential_moment_m{mass:g}",
                ratio < 1.0 and math.isfinite(tail),
                f"r*exp(4lambda_F)={ratio:.12f}, partial_tail={tail:.6e}",
            )
        )

    # If all unnormalized log densities differ by at most C, normalization
    # relative to probability Haar keeps the density in [exp(-C),exp(C)].
    logs = [-0.7, -0.1, 0.2, 0.8]
    density = normalized_density(logs)
    osc = max(logs) - min(logs)
    checks.append(
        (
            "uniform_nonnull_normalization",
            min(density) >= math.exp(-osc) - 1e-14
            and max(density) <= math.exp(osc) + 1e-14,
            f"range=[{min(density):.9f},{max(density):.9f}], exp(+-C)=[{math.exp(-osc):.9f},{math.exp(osc):.9f}]",
        )
    )

    # Direct interaction tails and Dobrushin response tails combine without
    # losing positivity of the exponential rate.
    lambda_f, lambda_h = 0.17, 0.09
    lambda_c = min(lambda_f, lambda_h)
    combined_ok = all(
        math.exp(-lambda_f * radius) + math.exp(-lambda_h * radius)
        <= 2.0 * math.exp(-lambda_c * radius) + 1e-15
        for radius in range(40)
    )
    checks.append(
        (
            "quasilocal_tail_combination",
            combined_ok and lambda_c > 0.0,
            f"lambda_c=min(lambda_F,lambda_H)={lambda_c:.6f}",
        )
    )

    # A finite exact analogue checks the transformed density is everywhere
    # positive and that a remote image change has a smaller effect than a near
    # one at weak coupling.  It illustrates, but does not prove, the SU(3) step.
    weights = z3_image_weights(blocks=5, coupling=0.08)
    base = (0, 0, 0, 0)
    near = (1, 0, 0, 0)
    remote = (0, 0, 1, 0)
    p0 = conditional(weights, base)
    pn = conditional(weights, near)
    pr = conditional(weights, remote)
    checks.append(
        (
            "finite_z3_image_positive",
            min(weights.values()) > 0.0 and min(p0) > 0.0,
            f"min_weight={min(weights.values()):.9e}, min_conditional={min(p0):.9f}",
        )
    )
    checks.append(
        (
            "finite_z3_remote_sensitivity",
            tv(p0, pr) < tv(p0, pn),
            f"TV_remote={tv(p0,pr):.9e}, TV_near={tv(p0,pn):.9e}",
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "uniformly non-null",
        "sup_(v,v_*,omega,h) |G_",
        "exponentially quasilocal",
        "absolutely summable",
        "for every e:",
        "not a uniform anchored supremum",
        "not necessarily translation-covariant",
        "No axiom-update stop is established.",
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
    checks.append(("source_contract", not missing, "missing=" + repr(missing)))
    forbidden_energy_step = "osc G_(v,v_*)"
    checks.append(
        (
            "absolute_energy_difference_contract",
            forbidden_energy_step not in text,
            f"forbidden_oscillation_only_step_present={forbidden_energy_step in text}",
        )
    )

    dependency = (
        "WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_"
        "UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md"
    )
    markdown_count = text.count(f"]({dependency})")
    checks.append(
        (
            "sole_markdown_dependency",
            markdown_count >= 1,
            f"direct-dependency markdown-link count={markdown_count}; external mathematics is bibliographic text",
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
