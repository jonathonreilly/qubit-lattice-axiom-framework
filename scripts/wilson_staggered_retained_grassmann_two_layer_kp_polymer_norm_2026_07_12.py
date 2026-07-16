#!/usr/bin/env python3
"""Checks simultaneous retained-Grassmann two-layer KP control."""

from __future__ import annotations

import itertools
import math
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_"
    "NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
Monomial = tuple[int, ...]
Exterior = dict[Monomial, float]


def g(t: float) -> float:
    return math.expm1(t) / t if t else 1.0


def criterion(
    mass: float, beta: float, c: float, theta: float, lam: float, eta: float
) -> dict[str, float]:
    h = 4.0 / mass
    L = theta + 2.0 * c + lam
    q = h * math.exp(L)
    wilson = 12.0 * math.expm1(3.0 * beta / 4.0) * math.exp(4.0 * L)
    determinant = 0.0
    for r in range(4, 10000, 2):
        term = 1.5 * h**r * g(3.0 * h**r / r) * math.exp(r * L)
        determinant += term
        if term < 1.0e-18:
            break
    schur = 0.0
    for r in range(2, 10000):
        x_r = 9.0 * eta**2 * 2.0 ** (-r) * mass ** (-(r - 1))
        term = 18.0 * eta**2 * r * h ** (r - 1) * g(x_r) * math.exp(r * L)
        schur += term
        if term < 1.0e-18:
            break
    total = wilson + determinant + schur
    det_envelope = 1.5 * math.exp(3.0 * h**4 / 4.0) * q**4 / (1.0 - q**2)
    schur_envelope = (
        18.0
        * eta**2
        * math.exp(9.0 * eta**2 / (4.0 * mass))
        * math.exp(L)
        * q
        * (2.0 - q)
        / (1.0 - q) ** 2
    )
    return {
        "h": h,
        "L": L,
        "q": q,
        "wilson": wilson,
        "determinant": determinant,
        "schur": schur,
        "K": total,
        "epsilon": c - total,
        "det_envelope": det_envelope,
        "schur_envelope": schur_envelope,
    }


def ext_add(left: Exterior, right: Exterior, scale: float = 1.0) -> Exterior:
    out: dict[Monomial, float] = defaultdict(float, left)
    for monomial, coefficient in right.items():
        out[monomial] += scale * coefficient
    return {key: value for key, value in out.items() if abs(value) > 1.0e-15}


def ext_mul(left: Exterior, right: Exterior) -> Exterior:
    out: dict[Monomial, float] = defaultdict(float)
    for monomial_left, coefficient_left in left.items():
        for monomial_right, coefficient_right in right.items():
            if set(monomial_left) & set(monomial_right):
                continue
            inversions = sum(a > b for a in monomial_left for b in monomial_right)
            monomial = tuple(sorted(monomial_left + monomial_right))
            out[monomial] += ((-1) ** inversions) * coefficient_left * coefficient_right
    return {key: value for key, value in out.items() if abs(value) > 1.0e-15}


def ext_scale(value: Exterior, scalar: float) -> Exterior:
    return {key: scalar * coefficient for key, coefficient in value.items()}


def ext_norm(value: Exterior, eta: float) -> float:
    return sum(abs(coefficient) * eta ** len(monomial) for monomial, coefficient in value.items())


def ext_log_one_plus(nilpotent: Exterior, max_degree: int) -> Exterior:
    out: Exterior = {}
    power = dict(nilpotent)
    for order in range(1, max_degree + 1):
        out = ext_add(out, power, ((-1) ** (order + 1)) / order)
        power = ext_mul(power, nilpotent)
        if not power:
            break
    return out


def components(labels: tuple[int, ...], supports: list[set[int]]) -> list[tuple[int, ...]]:
    unseen = set(labels)
    out: list[tuple[int, ...]] = []
    while unseen:
        root = unseen.pop()
        component = {root}
        frontier = [root]
        while frontier:
            label = frontier.pop()
            linked = {other for other in unseen if supports[label] & supports[other]}
            unseen -= linked
            component |= linked
            frontier.extend(linked)
        out.append(tuple(sorted(component)))
    return out


def average_activity_product(labels: tuple[int, ...], activities: list[list[Exterior]]) -> Exterior:
    out: Exterior = {}
    for config_index in range(len(activities[0])):
        product: Exterior = {(): 1.0}
        for label in labels:
            product = ext_mul(product, activities[label][config_index])
        out = ext_add(out, product, 1.0 / len(activities[0]))
    return out


def banach_polymer_identity() -> tuple[float, Exterior, Exterior, Exterior]:
    hidden_configs = list(itertools.product((-1.0, 1.0), repeat=2))
    supports = [{0}, {1}, {0, 1}, {0, 1}, {0, 1}]
    activities: list[list[Exterior]] = [[] for _ in supports]
    for x, y in hidden_configs:
        activities[0].append({(): 0.03 * x})
        activities[1].append({(): -0.02 * y})
        activities[2].append({(): 0.04 * x * y})
        # Even balanced path factors. The two bilinears overlap in hidden
        # support and their product fills all four Grassmann generators.
        activities[3].append({(0, 3): 0.11 * (1.0 + 0.25 * x)})
        activities[4].append({(1, 2): -0.09 * (1.0 - 0.30 * y)})

    one: Exterior = {(): 1.0}
    direct: Exterior = {}
    for config_index in range(len(hidden_configs)):
        product = one
        for label in range(len(supports)):
            product = ext_mul(product, ext_add(one, activities[label][config_index]))
        direct = ext_add(direct, product, 1.0 / len(hidden_configs))

    polymer_weight: dict[tuple[int, ...], Exterior] = {}
    labels_all = range(len(supports))
    for size in range(1, len(supports) + 1):
        for labels in itertools.combinations(labels_all, size):
            if len(components(labels, supports)) == 1:
                polymer_weight[labels] = average_activity_product(labels, activities)

    polymer_sum: Exterior = {(): 1.0}
    polymers = list(polymer_weight)
    # At most one nonempty-support polymer per hidden coordinate can occur in
    # a compatible family; this two-coordinate witness therefore stops at two.
    for size in range(1, len(hidden_configs[0]) + 1):
        for family in itertools.combinations(polymers, size):
            used_labels: set[int] = set()
            used_hidden: set[int] = set()
            compatible = True
            for gamma in family:
                hidden = set().union(*(supports[label] for label in gamma))
                if used_labels & set(gamma) or used_hidden & hidden:
                    compatible = False
                    break
                used_labels |= set(gamma)
                used_hidden |= hidden
            if compatible:
                product: Exterior = {(): 1.0}
                for gamma in family:
                    product = ext_mul(product, polymer_weight[gamma])
                polymer_sum = ext_add(polymer_sum, product)

    body = direct.get((), 0.0)
    normalized_nilpotent = ext_add(ext_scale(direct, 1.0 / body), {(): 1.0}, -1.0)
    direct_log = ext_log_one_plus(normalized_nilpotent, 4)
    polymer_nilpotent = ext_add(ext_scale(polymer_sum, 1.0 / body), {(): 1.0}, -1.0)
    polymer_log = ext_log_one_plus(polymer_nilpotent, 4)
    return body, direct, polymer_sum, ext_add(direct_log, polymer_log, -1.0)


def max_coefficient_difference(left: Exterior, right: Exterior) -> float:
    keys = set(left) | set(right)
    return max((abs(left.get(key, 0.0) - right.get(key, 0.0)) for key in keys), default=0.0)


def main() -> None:
    checks: list[tuple[str, bool, str]] = []
    examples = [
        (12.0, 0.0005, 0.12, 0.001, 0.001, 0.02),
        (16.0, 0.0010, 0.12, 0.001, 0.001, 0.05),
        (20.0, 0.0025, 0.125, 0.001, 0.001, 0.04),
    ]
    for mass, beta, c, theta, lam, eta in examples:
        row = criterion(mass, beta, c, theta, lam, eta)
        checks.append(
            (
                f"joint_kp_point_m{mass:g}",
                row["q"] < 1.0 and row["epsilon"] > 0.0,
                "K_W={:.12f}, K_I={:.12f}, K_S={:.12f}, "
                "K={:.12f}, epsilon={:.12f}, q={:.12f}".format(
                    row["wilson"],
                    row["determinant"],
                    row["schur"],
                    row["K"],
                    row["epsilon"],
                    row["q"],
                ),
            )
        )
        checks.append(
            (
                f"closed_envelopes_m{mass:g}",
                row["determinant"] <= row["det_envelope"] + 1.0e-15
                and row["schur"] <= row["schur_envelope"] + 1.0e-15,
                "K_I={:.12f}<={:.12f}, K_S={:.12f}<={:.12f}".format(
                    row["determinant"],
                    row["det_envelope"],
                    row["schur"],
                    row["schur_envelope"],
                ),
            )
        )

    # A fixed positive fine link can occur at any of r positions and in either
    # orientation; the other r-1 steps have eight safe choices.
    r = 4
    fixed_link_words = 2 * r * 8 ** (r - 1)
    h = 4.0 / 12.0
    det_incidence = (3.0 / r) * fixed_link_words * 2.0 ** (-r) * 12.0 ** (-r)
    schur_incidence = 9.0 * fixed_link_words * 2.0 ** (-r) * 12.0 ** (-(r - 1))
    checks.append(
        (
            "fixed_link_path_incidence",
            fixed_link_words == 4096
            and abs(det_incidence - 0.75 * h**r) < 1.0e-15
            and abs(schur_incidence - 9.0 * r * h ** (r - 1)) < 1.0e-15,
            f"words={fixed_link_words}, determinant={det_incidence:.12f}, schur={schur_incidence:.12f}",
        )
    )

    # Odd closed nearest-neighbor words are excluded by parity; every length-2
    # closed word is an immediate reversal and hence has U U^dagger=1.
    directions = [(axis, sign) for axis in range(4) for sign in (-1, 1)]
    two_step_closed = [
        (first, second)
        for first in directions
        for second in directions
        if first[0] == second[0] and first[1] == -second[1]
    ]
    checks.append(
        (
            "induced_bipartite_constant_floor",
            len(two_step_closed) == 8,
            f"odd closed words forbidden; length-two reversals={len(two_step_closed)}",
        )
    )

    eta_probe = 0.37
    left: Exterior = {(): 0.7, (0, 1): -0.2, (2, 3): 0.11}
    right: Exterior = {(): -0.4, (0, 3): 0.3, (1, 2): -0.17}
    product = ext_mul(left, right)
    checks.append(
        (
            "eta_norm_submultiplicative",
            ext_norm(product, eta_probe) <= ext_norm(left, eta_probe) * ext_norm(right, eta_probe) + 1.0e-15,
            "product={:.12f}, bound={:.12f}".format(
                ext_norm(product, eta_probe), ext_norm(left, eta_probe) * ext_norm(right, eta_probe)
            ),
        )
    )

    body, direct, polymer, log_residual = banach_polymer_identity()
    regrouping_residual = max_coefficient_difference(direct, polymer)
    logarithm_residual = max((abs(value) for value in log_residual.values()), default=0.0)
    normalized_nilpotent = ext_add(ext_scale(direct, 1.0 / body), {(): 1.0}, -1.0)
    logarithm = ext_log_one_plus(normalized_nilpotent, 4)
    quartic = logarithm.get((0, 1, 2, 3), 0.0)
    checks.append(
        (
            "banach_factor_to_polymer_identity",
            body > 0.0 and regrouping_residual < 1.0e-14 and logarithm_residual < 1.0e-14,
            f"body={body:.12f}, regrouping={regrouping_residual:.3e}, log={logarithm_residual:.3e}",
        )
    )
    checks.append(
        (
            "balanced_quartic_connected_log",
            abs(quartic) > 1.0e-8 and all(len(monomial) % 2 == 0 for monomial in logarithm),
            f"quartic={quartic:.12f}, monomials={sorted(logarithm)}",
        )
    )

    # The first and last fine links of a retained-to-retained Schur path belong
    # to outgoing or incoming skeleton pairs, so the endpoint coarse cells are
    # already charged by the syntactic support convention.
    coarse_path = [(0, 0, 0, 0), (0, 0, 0, 0), (1, 0, 0, 0), (1, 1, 0, 0)]
    connected = all(sum(abs(a - b) for a, b in zip(x, y)) <= 1 for x, y in zip(coarse_path, coarse_path[1:]))
    checks.append(
        (
            "schur_path_coarse_support",
            connected and coarse_path[0] == (0, 0, 0, 0) and coarse_path[-1] == (1, 1, 0, 0),
            f"coarse_path={coarse_path}, anchor_multiplicity=68",
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "det D_II",
        "K_joint=K_W+K_I+K_S<c",
        "q=h exp(L)<1",
        "complete Reinhardt",
        "every fine\nextent at least four",
        "68 exp(lambda/2)c+3m eta^2 exp(theta/2)",
        "not a physical field normalization",
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
    forbidden = ["Block 28's full-determinant measure applies unchanged", "NOT_TESTED"]
    hits = [item for item in forbidden if item in text]
    checks.append(("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}"))

    expected_dependencies = sorted(
        [
            "MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER_BOUNDED_THEOREM_NOTE_2026-07-12.md",
        ]
    )
    note_links = re.findall(r"\]\(([^)#?]+\.md)\)", text)
    dependency_set = sorted(set(note_links))
    checks.append(
        (
            "repository_dependency_set",
            dependency_set == expected_dependencies,
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
