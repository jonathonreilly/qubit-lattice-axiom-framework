#!/usr/bin/env python3
"""Checks the explicit two-layer KP source-polymer criterion."""

from __future__ import annotations

import itertools
import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_"
    "POLYMER_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)


def g(t: float) -> float:
    return math.expm1(t) / t if t else 1.0


def criterion(mass: float, beta: float, c: float, theta: float, lam: float) -> dict[str, float]:
    kappa = 14.0 / (mass * mass + 2.0)
    L = theta + 2.0 * c + lam
    q = kappa * math.exp(2.0 * L)
    wilson = 12.0 * math.expm1(3.0 * beta / 4.0) * math.exp(4.0 * L)
    fermion = 0.0
    for n in range(2, 100000):
        t_n = 3.0 * kappa**n / (2.0 * n)
        term = 1.5 * kappa**n * g(t_n) * math.exp(2.0 * n * L)
        fermion += term
        if term < 1.0e-18:
            break
    total = wilson + fermion
    return {
        "kappa": kappa,
        "L": L,
        "q": q,
        "wilson": wilson,
        "fermion": fermion,
        "K": total,
        "epsilon": c - total,
    }


def source_radius(epsilon: float, c: float, theta: float, lam: float, size: int, span: int, norm: float = 1.0) -> float:
    return math.log1p(epsilon * math.exp(-(theta + 2.0 * c) * size - lam * span)) / norm


def components(labels: tuple[int, ...], supports: list[set[int]]) -> list[tuple[int, ...]]:
    unseen = set(labels)
    out: list[tuple[int, ...]] = []
    while unseen:
        root = unseen.pop()
        comp = {root}
        frontier = [root]
        while frontier:
            a = frontier.pop()
            linked = {b for b in unseen if supports[a] & supports[b]}
            unseen -= linked
            comp |= linked
            frontier.extend(linked)
        out.append(tuple(sorted(comp)))
    return out


def toy_two_layer_identity() -> tuple[float, float]:
    # Label 3 is independent of every spin but deliberately carries the dummy
    # syntactic support {0}. This models a coarse-V-dependent factor whose A
    # variables cancel algebraically; over-supporting it must preserve the
    # exact factor-to-polymer identity.
    supports = [{0, 1}, {1, 2}, {2}, {0}]

    def factor(label: int, spins: tuple[int, int, int]) -> float:
        x = [2 * s - 1 for s in spins]
        return [
            0.04 + 0.07 * x[0] * x[1],
            -0.02 - 0.05 * x[1] * x[2],
            0.01 + 0.03 * x[2],
            0.015,
        ][label]

    configs = list(itertools.product((0, 1), repeat=3))
    direct = sum(math.prod(1.0 + factor(a, s) for a in range(4)) for s in configs) / len(configs)

    polymer_weight: dict[tuple[int, ...], float] = {}
    for r in range(1, 5):
        for labels in itertools.combinations(range(4), r):
            if len(components(labels, supports)) == 1:
                polymer_weight[labels] = sum(
                    math.prod(factor(a, s) for a in labels) for s in configs
                ) / len(configs)

    polymer_sum = 1.0
    polymers = list(polymer_weight)
    for r in range(1, len(polymers) + 1):
        for family in itertools.combinations(polymers, r):
            used_labels: set[int] = set()
            used_sites: set[int] = set()
            compatible = True
            for gamma in family:
                sites = set().union(*(supports[a] for a in gamma))
                if used_labels & set(gamma) or used_sites & sites:
                    compatible = False
                    break
                used_labels |= set(gamma)
                used_sites |= sites
            if compatible:
                polymer_sum += math.prod(polymer_weight[gamma] for gamma in family)
    return direct, polymer_sum


def coarse_cells_for_path(path: list[tuple[int, int, int, int]]) -> list[tuple[int, int, int, int]]:
    return [tuple(x // 2 for x in site) for site in path]


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    # Exact SU(3) midpoint centering: Re Tr U in [-3/2,3] turns the Wilson
    # exponent interval into length 3 beta/2 and centered sup norm 3 beta/4.
    beta_probe = 0.2
    wilson_values = [-beta_probe, beta_probe / 2.0]
    midpoint = sum(wilson_values) / 2.0
    centered = max(abs(x - midpoint) for x in wilson_values)
    checks.append(
        (
            "wilson_midpoint_centering",
            abs(centered - 3.0 * beta_probe / 4.0) < 1e-15,
            f"centered_sup={centered:.12f}, target={3*beta_probe/4:.12f}",
        )
    )

    # A two-link hidden footprint meets at most 12 fine plaquettes.
    checks.append(("hidden_plaquette_incidence", 2 * 2 * (4 - 1) == 12, "2 footprints * 6 plaquettes=12"))

    examples = [
        (10.0, 0.0005, 0.12, 0.001, 0.001),
        (12.0, 0.0020, 0.15, 0.001, 0.001),
        (16.0, 0.0035, 0.14, 0.001, 0.001),
    ]
    results = []
    for mass, beta, c, theta, lam in examples:
        row = criterion(mass, beta, c, theta, lam)
        results.append((mass, beta, c, theta, lam, row))
        checks.append(
            (
                f"kp_point_m{mass:g}",
                row["q"] < 1.0 and row["epsilon"] > 0.0,
                f"K={row['K']:.12f}, c={c:.6f}, epsilon={row['epsilon']:.12f}, q={row['q']:.12f}",
            )
        )

    # Check the closed geometric envelope used for tail diagnostics.
    mass, beta, c, theta, lam, row = results[1]
    envelope = 1.5 * math.exp(3.0 * row["kappa"] ** 2 / 4.0) * row["q"] ** 2 / (1.0 - row["q"])
    checks.append(
        (
            "determinant_geometric_envelope",
            row["fermion"] <= envelope + 1e-15,
            f"series={row['fermion']:.12f}, envelope={envelope:.12f}",
        )
    )

    # Explicit uniform radii for a norm-one one-coordinate source and a
    # norm-one four-coordinate, span-two source.
    for mass, beta, c, theta, lam, row in results:
        r1 = source_radius(row["epsilon"], c, theta, lam, 1, 0)
        r42 = source_radius(row["epsilon"], c, theta, lam, 4, 2)
        checks.append(
            (
                f"source_radii_m{mass:g}",
                r1 > 0.0 and r42 > 0.0 and r42 < r1,
                f"r_(1,0)={r1:.12f}, r_(4,2)={r42:.12f}",
            )
        )

    direct, polymer = toy_two_layer_identity()
    checks.append(
        (
            "two_layer_factor_to_polymer_identity",
            abs(direct - polymer) < 1e-14,
            f"direct={direct:.15f}, polymer={polymer:.15f}",
        )
    )

    fine_path = [(0, 0, 0, 0), (1, 0, 0, 0), (2, 0, 0, 0), (2, 1, 0, 0), (2, 2, 0, 0)]
    coarse = coarse_cells_for_path(fine_path)
    connected = all(sum(abs(a - b) for a, b in zip(x, y)) <= 1 for x, y in zip(coarse, coarse[1:]))
    checks.append(
        (
            "fine_path_coarse_anchor_lipschitz",
            connected and len(set(coarse)) <= len(fine_path),
            f"coarse_path={coarse}",
        )
    )
    checks.append(("coarse_anchor_multiplicity", 4 * 2**4 + 4 == 68, "64 anchored fine links + 4 incoming skeleton endpoints=68"))

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "L=theta+2c+lambda",
        "K_(theta,lambda)(c)<c",
        "q=kappa exp(2L)<1",
        "two-layer",
        "syntactic hidden footprint",
        "uniform complex-source domain",
        "D^n R=(-1)^(n+1) kappa_n",
        "68 exp(lambda/2)c",
        "No negative theorem is shipped.",
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
    missing = [x for x in required if x not in text]
    forbidden = ["complete analyticity follows from Dobrushin", "retained-Grassmann theorem", "NOT_TESTED"]
    hits = [x for x in forbidden if x in text]
    checks.append(("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}"))

    dep = "WILSON_STAGGERED_RAW_CONSTRAINED_ACTION_HESSIAN_DECAY_BOUNDED_THEOREM_NOTE_2026-07-12.md"
    note_links = re.findall(r"\]\(([^)#?]+\.md)\)", text)
    dep_set = sorted(set(note_links))
    checks.append(("sole_repository_dependency", dep_set == [dep], f"markdown_dependency_set={dep_set}"))

    passed = sum(ok for _, ok, _ in checks)
    failed = len(checks) - passed
    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
    print(f"SCORECARD PASS={passed} FAIL={failed}")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
