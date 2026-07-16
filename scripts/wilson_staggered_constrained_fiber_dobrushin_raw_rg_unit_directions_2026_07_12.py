#!/usr/bin/env python3
"""Certificate for constrained-fiber Dobrushin control and raw RG directions."""

from __future__ import annotations

from collections import defaultdict
from math import exp
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_"
    "DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md"
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


def fermion_row(mass: float) -> float:
    kappa = 14.0 / (mass * mass + 2.0)
    return 1.5 * kappa**2 * (2.0 - kappa) / (1.0 - kappa) ** 2


def alpha(beta: float, mass: float) -> float:
    return 18.0 * beta + fermion_row(mass)


def bisect_mass_for_half_row() -> float:
    lo, hi = 4.0, 20.0
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if fermion_row(mid) > 0.5:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def exterior_mul(
    left: dict[tuple[int, ...], complex], right: dict[tuple[int, ...], complex]
) -> dict[tuple[int, ...], complex]:
    result: dict[tuple[int, ...], complex] = defaultdict(complex)
    for monomial_left, coefficient_left in left.items():
        for monomial_right, coefficient_right in right.items():
            if set(monomial_left) & set(monomial_right):
                continue
            inversions = sum(a > b for a in monomial_left for b in monomial_right)
            monomial = tuple(sorted(monomial_left + monomial_right))
            result[monomial] += ((-1) ** inversions) * coefficient_left * coefficient_right
    return {key: value for key, value in result.items() if abs(value) > 1.0e-15}


def exterior_add(
    left: dict[tuple[int, ...], complex], right: dict[tuple[int, ...], complex], scale: complex = 1.0
) -> dict[tuple[int, ...], complex]:
    result: dict[tuple[int, ...], complex] = defaultdict(complex, left)
    for key, value in right.items():
        result[key] += scale * value
    return {key: value for key, value in result.items() if abs(value) > 1.0e-15}


def exterior_log_one_plus(nilpotent: dict[tuple[int, ...], complex], degree: int) -> dict[tuple[int, ...], complex]:
    result: dict[tuple[int, ...], complex] = {}
    power = dict(nilpotent)
    for order in range(1, degree + 1):
        result = exterior_add(result, power, ((-1) ** (order + 1)) / order)
        power = exterior_mul(power, nilpotent)
        if not power:
            break
    return result


def main() -> int:
    # A toy footprint partition with four skeleton pairs and four single links.
    footprints = {
        "a0": (0, 1),
        "a1": (2, 3),
        "a2": (4, 5),
        "a3": (6, 7),
        "n0": (8,),
        "n1": (9,),
        "n2": (10,),
        "n3": (11,),
    }
    flattened = [link for footprint in footprints.values() for link in footprint]
    check(
        "Hidden-coordinate footprints partition fine links and have size at most two",
        sorted(flattened) == list(range(12)) and max(map(len, footprints.values())) == 2,
        f"coordinates={len(footprints)}, links={len(flattened)}, max footprint={max(map(len, footprints.values()))}",
    )

    rng = np.random.default_rng(20260712)
    fine = rng.random((12, 12))
    np.fill_diagonal(fine, 0.0)
    target_row = 0.37
    fine *= target_row / fine.sum(axis=1).max()
    hidden_names = list(footprints)
    hidden = np.zeros((len(hidden_names), len(hidden_names)))
    for i, name_i in enumerate(hidden_names):
        for j, name_j in enumerate(hidden_names):
            hidden[i, j] = sum(fine[e, f] for e in footprints[name_i] for f in footprints[name_j])
    fine_row = fine.sum(axis=1).max()
    hidden_row = hidden.sum(axis=1).max()
    check(
        "Footprint aggregation bounds the hidden Dobrushin row by twice the fine row",
        hidden_row <= 2.0 * fine_row + 1.0e-14 and hidden_row > fine_row,
        f"fine={fine_row:.6f}, hidden={hidden_row:.6f}, ratio={hidden_row/fine_row:.6f}",
    )

    mass_floor = bisect_mass_for_half_row()
    examples = []
    for mass in (8.0, 10.0):
        ceiling = (0.5 - fermion_row(mass)) / 18.0
        examples.append((mass, ceiling))
    check(
        "The deep constrained-fiber wedge has the stated exact numerical examples",
        6.5990 < mass_floor < 6.5992
        and abs(examples[0][1] - 0.0169782141) < 1.0e-10
        and abs(examples[1][1] - 0.0238489507) < 1.0e-10,
        f"m0={mass_floor:.10f}, beta8={examples[0][1]:.10f}, beta10={examples[1][1]:.10f}",
    )

    deep_points = ((0.0, 7.0), (0.01, 8.0), (0.02, 10.0))
    rows = [2.0 * alpha(beta, mass) for beta, mass in deep_points]
    check(
        "Sampled deep-wedge fibers have a strict uniform hidden-row margin",
        max(rows) < 1.0,
        "2alpha=" + ",".join(f"{value:.6f}" for value in rows),
    )

    # A finite Grassmann mixture: N has bilinear pieces whose logarithm gains a
    # quartic connected term unless the product factorizes exactly.
    nilpotent = {(0, 1): 0.30, (2, 3): -0.20, (0, 3): 0.11}
    logarithm = exterior_log_one_plus(nilpotent, 4)
    quartic = logarithm.get((0, 1, 2, 3), 0.0)
    check(
        "Finite Grassmann logarithm generates a balanced quartic connected coefficient",
        abs(quartic) > 1.0e-4,
        f"quartic coefficient={quartic.real:.6f}",
    )

    # Exact fiber-constant factorization on a finite hidden set.
    hidden_weights = rng.uniform(0.2, 1.5, size=(5, 9))
    coarse_function = rng.normal(size=5)
    coupling = 0.37
    base_weight = hidden_weights.sum(axis=1)
    shifted_weight = (hidden_weights * np.exp(-coupling * coarse_function)[:, None]).sum(axis=1)
    action_shift = -np.log(shifted_weight) + np.log(base_weight)
    check(
        "A fiber-measurable perturbation passes exactly through raw integration",
        np.linalg.norm(action_shift - coupling * coarse_function) < 1.0e-13,
        f"maximum residual={np.max(np.abs(action_shift-coupling*coarse_function)):.2e}",
    )

    input_difference = np.max(np.abs(coupling * coarse_function))
    output_difference = np.max(np.abs(action_shift))
    check(
        "The common unrescaled sup coefficient norm has an exact directional ratio one",
        abs(output_difference / input_difference - 1.0) < 1.0e-13,
        f"input={input_difference:.6f}, output={output_difference:.6f}, ratio={output_difference/input_difference:.12f}",
    )

    # Sample an anchored polymer tail: number of one-dimensional intervals of
    # diameter n containing a root is n+1.
    lam, theta, extra = 0.3, 0.2, 0.8
    partials = []
    total = 0.0
    for diameter in range(80):
        size = diameter + 1
        activity = exp(-(lam + extra) * diameter - (theta + extra) * size)
        total += (diameter + 1) * exp(lam * diameter + theta * size) * activity
        partials.append(total)
    tail = partials[-1] - partials[39]
    check(
        "The candidate anchored norm is finite on a sampled exponential polymer tail",
        total < 10.0 and tail < 1.0e-10,
        f"partial80={total:.6f}, tail40to80={tail:.3e}",
    )

    text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    required = [
        "**Type:** bounded_theorem",
        "alpha_fiber<=2alpha",
        "alpha(beta,m)<1/2",
        "R(Phi+t Lf)=R(Phi)+t f",
        "not yet\nconstruct a volume-uniform coarse interaction",
        "does not yet\nconstruct a volume-uniform coarse interaction",
        "not called an eigenvalue-one",
        "pair covariance decay alone does not automatically",
        "No axiom-update stop",
        "No-Go Discipline N1--N8",
        "### N3 — hidden-condition phrase scan",
        "### N4 — citation/residual matching",
        "### N5 — rhetoric and resolution audit",
        "### N6 — partial-closure and primitive scan",
        "### N7 — hostile steelman",
        "### N8 — cross-cycle echo",
        "**No-Go Discipline status: PASS.**",
    ]
    # Either line-wrapping form of the volume-uniform boundary is enough.
    volume_needles = required[4:6]
    required = required[:4] + required[6:]
    missing = [item for item in required if item not in text]
    if not any(item in text for item in volume_needles):
        missing.append("volume-uniform coarse interaction boundary")
    attempted = text.count("| `ATTEMPTED` |")
    n2_conditions = [
        "uniform connected-polymer/cumulant bound",
        "relevant-coordinate extraction and rescaling",
        "physical critical trajectory/observable identification",
    ]
    n2_pairs = [
        f"| {n2_conditions[left]} | {n2_conditions[right]} |"
        for left in range(len(n2_conditions))
        for right in range(left + 1, len(n2_conditions))
    ]
    missing_pairs = [item for item in n2_pairs if item not in text]
    check(
        "Source-note bounded theorem and N1-N8 contract",
        not missing and not missing_pairs and attempted >= 8,
        f"missing={missing}; missing N2 pairs={missing_pairs}; attempted={attempted}",
    )

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
