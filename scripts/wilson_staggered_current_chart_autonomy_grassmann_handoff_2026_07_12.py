#!/usr/bin/env python3
"""Checks current-chart spatial and Grassmann autonomy boundaries."""

from __future__ import annotations

import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_CURRENT_CHART_AUTONOMY_AND_NEXT_SCALE_"
    "GRASSMANN_HANDOFF_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)


def straight_path(start: tuple[int, ...], axis: int, length: int) -> tuple[tuple[int, ...], ...]:
    points = []
    for step in range(length + 1):
        point = list(start)
        point[axis] += step
        points.append(tuple(point))
    return tuple(points)


def compose_straight_path(axis: int, q: int, r: int, dimension: int = 4) -> tuple[tuple[int, ...], ...]:
    start = (0,) * dimension
    pieces = []
    for outer in range(r):
        piece_start = list(start)
        piece_start[axis] = outer * q
        piece = straight_path(tuple(piece_start), axis, q)
        pieces.extend(piece if outer == 0 else piece[1:])
    return tuple(pieces)


def weak_to_strong_ratio(size: int, lam: float, theta: float, c: float) -> float:
    diameter = size // 2
    return math.exp((lam / 2.0) * diameter + (theta / 2.0 + 2.0 * c) * size)


def rectangular_loop(length: int) -> tuple[tuple[tuple[int, ...], int], ...]:
    """Canonical positive links of an L-by-L loop at odd spectator x_2=1."""
    links: list[tuple[tuple[int, ...], int]] = []
    for step in range(length):
        links.append(((step, 0, 1, 0), 0))
        links.append(((length, step, 1, 0), 1))
        links.append(((step, length, 1, 0), 0))
        links.append(((0, step, 1, 0), 1))
    return tuple(links)


def is_skeleton_link(link: tuple[tuple[int, ...], int]) -> bool:
    start, axis = link
    return all(coordinate % 2 == 0 for index, coordinate in enumerate(start) if index != axis)


def nilpotent_mul(left: dict[int, float], right: dict[int, float]) -> dict[int, float]:
    out: dict[int, float] = {}
    for left_mask, left_value in left.items():
        for right_mask, right_value in right.items():
            if left_mask & right_mask:
                continue
            mask = left_mask | right_mask
            out[mask] = out.get(mask, 0.0) + left_value * right_value
    return out


def gaussian_expectation(mask: int, mass: float) -> float:
    gaussian = {0: 1.0}
    for color in range(3):
        gaussian = nilpotent_mul(gaussian, {0: 1.0, 1 << color: -mass})
    numerator = nilpotent_mul(gaussian, {mask: 1.0}).get(0b111, 0.0)
    denominator = gaussian[0b111]
    return numerator / denominator


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    semigroup_rows = []
    for axis in range(4):
        direct = straight_path((0, 0, 0, 0), axis, 8)
        composed = compose_straight_path(axis, 2, 4)
        semigroup_rows.append(direct == composed)
    checks.append(
        (
            "straight_dyadic_support_semigroup",
            all(semigroup_rows),
            f"axes={len(semigroup_rows)}, H_2_after_H_4=H_8",
        )
    )

    coarse_chain = {(site, 0, 0, 0) for site in range(5)}
    q_support = 4
    lifted_chain: set[tuple[int, ...]] = set()
    for site in range(4):
        lifted_chain.update(straight_path((q_support * site, 0, 0, 0), 0, q_support))
    coarse_diameter = 4
    lifted_diameter = max(point[0] for point in lifted_chain) - min(point[0] for point in lifted_chain)
    checks.append(
        (
            "straight_support_size_diameter",
            len(coarse_chain) == 5
            and len(lifted_chain) == 17
            and lifted_diameter == q_support * coarse_diameter
            and len(lifted_chain) <= (1 + 4 * (q_support - 1)) * len(coarse_chain),
            f"q={q_support}, coarse=(size=5,diam=4), lifted=(size={len(lifted_chain)},diam={lifted_diameter}), general_size_cap=65",
        )
    )

    # A one-dimensional full-cell saturation with origin zero is not
    # equivariant under reflection x -> -x.
    saturation = {0, 1}
    reflected_saturation = {-x for x in saturation}
    saturation_of_reflected_seed = {0, 1}
    checks.append(
        (
            "origin_cell_saturation_reflection_failure",
            reflected_saturation != saturation_of_reflected_seed,
            f"theta(Sat({{0}}))={sorted(reflected_saturation)}, Sat(theta({{0}}))={sorted(saturation_of_reflected_seed)}",
        )
    )

    lam, theta, c = 1.0, 1.0e-6, 0.001
    lengths = (1, 2, 4, 8, 16, 32)
    loops = [rectangular_loop(length) for length in lengths]
    sizes = tuple(len(loop) for loop in loops)
    ratios = [weak_to_strong_ratio(size, lam, theta, c) for size in sizes]
    omega = complex(-0.5, math.sqrt(3.0) / 2.0)
    fundamental_center_average = sum(omega**power for power in range(3)) / 3.0
    checks.append(
        (
            "current_weak_to_strong_unbounded_family",
            all(len(loop) == len(set(loop)) == 4 * length for length, loop in zip(lengths, loops))
            and all(not is_skeleton_link(link) for loop in loops for link in loop)
            and all(right > left for left, right in zip(ratios, ratios[1:]))
            and ratios[-1] > 1.0e13
            and abs(fundamental_center_average) < 1.0e-15,
            "all_hidden=True, unique=True, |T_L|=|X_L|=4L; center_average={:.3e}; ".format(
                abs(fundamental_center_average)
            )
            + "; ".join(f"L={length}:ratio={ratio:.6e}" for length, ratio in zip(lengths, ratios)),
        )
    )

    # Normalized one-site, three-color Gaussian Berezin expectation sends a
    # balanced p-pair monomial to an m^{-p} contraction. Relative to the
    # eta^(2p) coefficient weight its exact operator ratio is (m eta^2)^(-p).
    mass, eta = 1.0e4, 1.0e-10
    expectations = [abs(gaussian_expectation((1 << pairs) - 1, mass)) for pairs in range(4)]
    pair_ratios = [expectation / eta ** (2 * pairs) for pairs, expectation in enumerate(expectations)]
    one_site = max(pair_ratios)
    block_log10 = 15.0 * math.log10(one_site)
    checks.append(
        (
            "gaussian_berezin_eta_norm_handoff",
            all(
                math.isclose(math.log10(value), 16.0 * pairs, abs_tol=1.0e-12)
                for pairs, value in enumerate(pair_ratios)
            )
            and abs(block_log10 - 720.0) < 1.0e-12,
            f"expectations={expectations}, pair_ratios={pair_ratios}, one_site={one_site:.1e}, fifteen_site=1e{block_log10:.0f}",
        )
    )

    # Naive one-index martingale weights that contract a level shift cannot
    # have a uniform algebra constant when centered products return coarse
    # modulation.
    q = 0.5
    a_h = 1.0 / 9.0
    depths = (2, 4, 8, 12)
    lower_bounds = [a_h * q ** (-depth) for depth in depths]
    checks.append(
        (
            "one_index_martingale_algebra_boundary",
            all(right > left for left, right in zip(lower_bounds, lower_bounds[1:])),
            "a_h=1/9; " + "; ".join(f"J={depth}:C_alg>={bound:g}" for depth, bound in zip(depths, lower_bounds)),
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "scale-independent handoff constant",
        "10^720",
        "not a model noncontraction theorem",
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
    forbidden = ["all autonomous norms fail", "requires a new axiom", "NOT_TESTED"]
    hits = [item for item in forbidden if item in text]
    checks.append(("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}"))

    expected_dependencies = sorted(
        [
            "MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
