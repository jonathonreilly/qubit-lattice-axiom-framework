#!/usr/bin/env python3
"""Conditional diagnostics for the SU(3) beta=6 fixed-lattice gap reduction.

This runner supports a conditional reduction only. It does not prove an
unconditional beta=6 gap, a continuum mass-gap theorem, an all-coupling
confinement statement, or the no-second-order-bulk-point premise.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "SU3_BETA6_GAP_BULK_CRITICALITY_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-09.md"

np.seterr(all="ignore")
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if condition else 'FAIL'}] {label}")
    if detail:
        print(f"       {detail}")
    PASS += int(condition)
    FAIL += int(not condition)
    return condition


def su3_class_quad(function, beta: float, n: int = 400) -> float:
    angles = (np.arange(n) + 0.5) / n * 2.0 * np.pi - np.pi
    t1, t2 = np.meshgrid(angles, angles, indexing="ij")
    t3 = -t1 - t2
    e1 = np.exp(1j * t1)
    e2 = np.exp(1j * t2)
    e3 = np.exp(1j * t3)
    haar_density = (
        np.abs(e1 - e2) ** 2
        * np.abs(e1 - e3) ** 2
        * np.abs(e2 - e3) ** 2
    )
    character = e1 + e2 + e3
    weight = haar_density * np.exp((beta / 3.0) * character.real)
    return float(np.sum(function(character) * weight) / np.sum(weight))


def su3_u(beta: float, n: int = 400) -> float:
    return su3_class_quad(lambda character: character.real / 3.0, beta, n=n)


def finite_positive_kernel_gaps() -> np.ndarray:
    points = np.linspace(-np.pi, np.pi, 24, endpoint=False)

    def transfer_gap(beta: float) -> float:
        kernel = np.exp(
            (beta / 3.0) * np.add.outer(np.cos(points), np.cos(points)) / 2.0
            - 0.3 * np.subtract.outer(points, points) ** 2
        )
        kernel = 0.5 * (kernel + kernel.T)
        eigenvalues = np.linalg.eigvalsh(kernel)
        return float(-np.log(eigenvalues[-2] / eigenvalues[-1]))

    return np.array([transfer_gap(beta) for beta in np.linspace(0.1, 6.0, 60)])


def note_guardrails() -> tuple[bool, list[str]]:
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "2026-06-12 audit firewall: reduction, not beta=6 gap theorem",
        "**Claim type:** open_gate / conditional fixed-lattice reduction",
        "one explicit premise",
        "The premise is not proven here",
        "Not an unconditional `beta=6` gap",
        "Not an axiom, primitive, or Tier-A admission",
        "physical scale through the scale-reference primitive",
        "comparators only",
        "Cited rather than reproven here",
        "turn the conditional result",
        "adds no new axiom, no Tier-A admission, and no audit-status change",
        "2026-06-16 transfer-kernel dependency-edge repair",
        "WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md",
        "AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
        "close only the source-graph route to the Wilson",
        "They do not prove",
        "the no-second-order-bulk-critical-point premise",
    ]
    missing = [phrase for phrase in required if phrase not in text]
    forbidden = ["**Claim type:** bounded_theorem"]
    present_forbidden = [phrase for phrase in forbidden if phrase in text]
    return not missing and not present_forbidden, missing + [f"forbidden:{p}" for p in present_forbidden]


def main() -> int:
    print("SU(3) BETA=6 FIXED-LATTICE GAP REDUCTION DIAGNOSTIC")
    print("=" * 72)

    normalized = su3_class_quad(lambda character: np.ones_like(character.real), 6.0)
    check(
        "SU(3) Weyl class quadrature normalizes the one-plaquette integral",
        np.isfinite(normalized) and abs(normalized - 1.0) < 1e-12,
        f"normalized integral = {normalized:.16f}",
    )

    beta_small = 0.05
    slope = su3_u(beta_small) / beta_small
    check(
        "small-beta character convention matches u(beta)/beta -> 1/18",
        abs(slope - 1.0 / 18.0) < 2e-3,
        f"u({beta_small})/{beta_small} = {slope:.5f}; 1/18 = {1/18:.5f}",
    )

    strong_betas = (0.5, 1.0, 1.5, 2.0)
    strong_values = [su3_u(beta) for beta in strong_betas]
    strong_sigmas = [-np.log(value) for value in strong_values]
    check(
        "leading strong-coupling coefficient is positive in the checked window",
        all(0.0 < value < 1.0 and sigma > 0.0 for value, sigma in zip(strong_values, strong_sigmas)),
        "; ".join(f"beta={beta}: u={value:.5f}, sigma_lead={sigma:.4f}" for beta, value, sigma in zip(strong_betas, strong_values, strong_sigmas)),
    )

    monotone_betas = (0.5, 2.0, 4.0, 6.0, 9.0)
    monotone_values = [su3_u(beta) for beta in monotone_betas]
    check(
        "leading coefficient weakens monotonically toward weaker coupling",
        all(monotone_values[i] < monotone_values[i + 1] for i in range(len(monotone_values) - 1)),
        "u(beta): " + ", ".join(f"{value:.4f}" for value in monotone_values),
    )

    gaps = finite_positive_kernel_gaps()
    check(
        "finite positive-kernel illustration has a positive Perron-Frobenius gap",
        bool(np.all(gaps > 0.0)),
        f"min illustrated gap = {gaps.min():.4f}",
    )
    max_jump = float(np.max(np.abs(np.diff(gaps))))
    check(
        "finite positive-kernel illustration varies continuously on the beta grid",
        max_jump < 0.2 * float(gaps.max()),
        f"max grid jump = {max_jump:.4f}; max gap = {gaps.max():.4f}",
    )

    b0 = 11.0 / (16.0 * np.pi**2)
    b1 = 102.0 / (16.0 * np.pi**2) ** 2
    g2 = 1.0
    a_lambda = (b0 * g2) ** (-b1 / (2.0 * b0**2)) * np.exp(-1.0 / (2.0 * b0 * g2))
    all_orders_hidden = all(
        np.exp(-1.0 / (2.0 * b0 * x)) / x**n < 1e-8
        for n in range(1, 8)
        for x in (1e-3, 1e-2)
    )
    check(
        "weak-side non-perturbative scale is invisible to checked perturbative orders",
        all_orders_hidden,
        f"checked n=1..7 near g^2=0; two-loop scale at g^2=1 is {a_lambda:.2e}",
    )

    u6 = su3_u(6.0)
    sigma_sc_6 = -np.log(u6)
    sigma_comparator_6 = 0.2189**2
    ratio = sigma_sc_6 / sigma_comparator_6
    check(
        "leading strong-coupling extrapolation misses the beta=6 comparator window",
        ratio > 5.0,
        f"sigma_lead={sigma_sc_6:.4f}; comparator sigma*a^2={sigma_comparator_6:.4f}; ratio={ratio:.1f}x",
    )

    guardrails_ok, missing = note_guardrails()
    check(
        "source note states the conditional boundary and forbidden imports",
        guardrails_ok,
        "missing guardrails: " + ", ".join(missing) if missing else "all required guardrails present",
    )

    text = NOTE.read_text(encoding="utf-8")
    check(
        "comparator values are labeled as comparators, not derivation inputs",
        text.count("comparators only") >= 1 and "they do not prove it inside the framework" in text,
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "SCOPE: conditional fixed-lattice reduction plus diagnostics only; "
        "the no-second-order-bulk-point premise remains open."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
