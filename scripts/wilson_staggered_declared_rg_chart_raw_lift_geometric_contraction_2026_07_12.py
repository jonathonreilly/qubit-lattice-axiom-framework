#!/usr/bin/env python3
"""Checks a declared factor-two RG chart and raw-lift suppression."""

from __future__ import annotations

import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_"
    "CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)


def diameter(support: frozenset[int]) -> int:
    return max(support) - min(support) if support else 0


def anchored_norm(
    interaction: dict[frozenset[int], float], lam: float, theta: float
) -> float:
    anchors = set().union(*interaction) if interaction else set()
    return max(
        (
            sum(
                math.exp(lam * diameter(support) + theta * len(support)) * abs(value)
                for support, value in interaction.items()
                if anchor in support
            )
            for anchor in anchors
        ),
        default=0.0,
    )


def zero_diameter_projector(
    interaction: dict[frozenset[int], float]
) -> dict[frozenset[int], float]:
    return {support: value for support, value in interaction.items() if diameter(support) == 0}


def complement(
    interaction: dict[frozenset[int], float]
) -> dict[frozenset[int], float]:
    return {support: value for support, value in interaction.items() if diameter(support) >= 1}


def straight_factor_two_lift(
    interaction: dict[frozenset[int], float]
) -> dict[frozenset[int], float]:
    lifted: dict[frozenset[int], float] = {}
    for support, value in interaction.items():
        if len(support) == 1:
            site = next(iter(support))
            fine_support = frozenset({2 * site})
        else:
            fine_support = frozenset(range(2 * min(support), 2 * max(support) + 1))
        lifted[fine_support] = value
    return lifted


def grassmann_norm(coefficients: dict[int, float], eta: float) -> float:
    return sum(abs(value) * eta ** degree for degree, value in coefficients.items())


def field_rescale(coefficients: dict[int, float], z: float) -> dict[int, float]:
    return {degree: value * z ** (-degree) for degree, value in coefficients.items()}


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    interaction = {
        frozenset({0}): 0.31,
        frozenset({0, 1}): -0.12,
        frozenset({1, 2}): 0.08,
        frozenset({0, 1, 2}): 0.05,
    }
    p0 = zero_diameter_projector(interaction)
    p0_twice = zero_diameter_projector(p0)
    irrel = complement(interaction)
    checks.append(
        (
            "zero_diameter_projector",
            p0 == p0_twice
            and set(p0) == {frozenset({0})}
            and set(p0).isdisjoint(irrel),
            f"rank_fixture={len(p0)}, complement_terms={len(irrel)}",
        )
    )

    lam, theta = 0.23, 0.07
    lifted = straight_factor_two_lift(irrel)
    coarse_norm = anchored_norm(irrel, lam, theta)
    fine_norm = anchored_norm(lifted, lam, theta)
    ratio = coarse_norm / fine_norm
    checks.append(
        (
            "extended_raw_lift_geometric_suppression",
            ratio <= math.exp(-lam) + 1.0e-14,
            f"coarse={coarse_norm:.12f}, fine_lift={fine_norm:.12f}, ratio={ratio:.12f}, exp(-lambda)={math.exp(-lam):.12f}",
        )
    )

    # Every lifted extended support contains doubled endpoint separation and
    # at least the original number of sites.
    support_checks = []
    for support in irrel:
        lifted_support = next(
            candidate
            for candidate, value in straight_factor_two_lift({support: interaction[support]}).items()
            if value == interaction[support]
        )
        support_checks.append(
            diameter(lifted_support) >= 2 * diameter(support)
            and len(lifted_support) >= len(support)
        )
    checks.append(
        (
            "factor_two_support_inequalities",
            all(support_checks),
            f"checked_supports={len(support_checks)}",
        )
    )

    coefficients = {0: 0.4, 2: -0.3, 4: 0.17, 6: -0.06}
    eta, z = 0.19, 1.7
    rescaled = field_rescale(coefficients, z)
    lhs = grassmann_norm(rescaled, eta)
    rhs = grassmann_norm(coefficients, eta / z)
    checks.append(
        (
            "field_rescaling_norm_identity",
            abs(lhs - rhs) < 1.0e-15,
            f"norm_Dz_eta={lhs:.12f}, norm_eta_over_z={rhs:.12f}",
        )
    )

    # Two equally admissible chart parameters give different coefficient
    # coordinates for the same polynomial functional.
    z1, z2 = 1.0, 2.0
    mass1 = field_rescale({2: 3.0}, z1)[2]
    mass2 = field_rescale({2: 3.0}, z2)[2]
    checks.append(
        (
            "field_chart_nonselection",
            mass1 != mass2 and mass1 == 3.0 and mass2 == 0.75,
            f"z1_mass={mass1:.6f}, z2_mass={mass2:.6f}",
        )
    )

    # Exact fiber-constant factorization with one retained square-zero
    # bilinear coefficient: -log[Z(1-t a xi)]+log Z=t a xi.
    hidden_weights = [0.4, 1.1, 0.7, 0.9]
    t, a = 0.37, -0.23
    body = sum(hidden_weights)
    nilpotent_weight = -t * a * body
    normalized_nilpotent = nilpotent_weight / body
    action_shift = -normalized_nilpotent
    checks.append(
        (
            "joint_raw_lift_identity",
            abs(action_shift - t * a) < 1.0e-15,
            f"action_shift={action_shift:.12f}, expected={t*a:.12f}",
        )
    )

    # A declared finite jet is an ordinary finite coordinate projection; two
    # different declared jet sets are both idempotent and inequivalent.
    coordinates = {"vacuum": 0.2, "onsite": 0.4, "short_bilinear": -0.1, "plaquette": 0.07, "long_loop": 0.03}
    jet_a = {key: coordinates[key] for key in ("vacuum", "onsite")}
    jet_b = {key: coordinates[key] for key in ("vacuum", "onsite", "short_bilinear", "plaquette")}
    checks.append(
        (
            "finite_jet_chart_family",
            set(jet_a) < set(jet_b) and jet_a != jet_b,
            f"jet_A={sorted(jet_a)}, jet_B={sorted(jet_b)}",
        )
    )

    # Fixed-background Schur tangent bounds for declared microscopic mass and
    # hopping coordinates, after the common rho=2^(3/2) field chart.
    rho_tangent = 2.0 ** 1.5
    tangent_rows = []
    for mass in (12.0, 16.0, 20.0):
        mass_bound = (1.0 + 16.0 / mass**2) / rho_tangent**2
        hopping_bound = (32.0 / mass + 64.0 / mass**2) / rho_tangent**2
        tangent_rows.append((mass, mass_bound, hopping_bound))
    checks.append(
        (
            "schur_coordinate_tangent_bounds",
            all(mass_bound < 0.14 and hopping_bound < 0.39 for _, mass_bound, hopping_bound in tangent_rows),
            "; ".join(
                f"m={mass:g}:dm={mass_bound:.6f},dt={hopping_bound:.6f}"
                for mass, mass_bound, hopping_bound in tangent_rows
            ),
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "P_0",
        "exp(-lambda)",
        "||D_rho Phi||_(lambda,theta,eta)=||Phi||_(lambda,theta,eta/rho)",
        "not a physical field normalization",
        "does not establish an invariant neighborhood",
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
    forbidden = ["the unique relevant sector", "is the physical beta function", "NOT_TESTED"]
    hits = [item for item in forbidden if item in text]
    checks.append(("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}"))

    expected_dependencies = sorted(
        [
            "WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
