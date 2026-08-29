#!/usr/bin/env python3
"""Independent Laurent-character reconstruction of the Block247 tower.

This module imports no Block247 primary code.  It restricts O(3) characters to
the SO(3) maximal torus, decomposes symmetric Laurent polynomials greedily into
spin characters, tracks inversion parity separately, performs the physical
trivial-character subtraction, and applies the original-link crossing weights.
"""

from __future__ import annotations

from fractions import Fraction as F


AUDIT_TIMEOUT_SEC = 30
MAX_LAYER = 8
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_PHYSICAL_Q_ACTION_CROSSING_TOWER_NO_GO_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_SECOND_CROSSING_ACTION_LEAKAGE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def character(spin):
    return {weight: F(1) for weight in range(-spin, spin + 1)}


def polynomial_add(left, right, scale=F(1)):
    result = dict(left)
    for weight, coefficient in right.items():
        result[weight] = result.get(weight, F(0)) + scale * coefficient
        if not result[weight]:
            result.pop(weight)
    return result


def polynomial_scale(polynomial, scale):
    return {weight: scale * coefficient for weight, coefficient in polynomial.items()
            if scale * coefficient}


def polynomial_multiply(left, right):
    result = {}
    for left_weight, left_coefficient in left.items():
        for right_weight, right_coefficient in right.items():
            weight = left_weight + right_weight
            result[weight] = result.get(weight, F(0)) + left_coefficient * right_coefficient
    return {weight: coefficient for weight, coefficient in result.items() if coefficient}


def decompose(polynomial):
    """Greedily decompose an exact symmetric Laurent polynomial into chi_l."""
    work = dict(polynomial)
    result = {}
    while work:
        maximum = max(abs(weight) for weight in work)
        coefficient = work.get(maximum, F(0))
        if not coefficient:
            coefficient = work.get(-maximum, F(0))
        if not coefficient:
            raise AssertionError("Laurent polynomial is not an SO(3) character sum")
        result[maximum] = result.get(maximum, F(0)) + coefficient
        work = polynomial_add(work, character(maximum), -coefficient)
    return {spin: coefficient for spin, coefficient in result.items() if coefficient}


def reconstruct(decomposition):
    result = {}
    for spin, coefficient in decomposition.items():
        result = polynomial_add(result, character(spin), coefficient)
    return result


def sample_a():
    return {
        "det": F(1, 5),
        **{spin: F(spin + 2, 2 * spin + 5) for spin in range(1, MAX_LAYER + 1)},
    }


def crossing_eigenvalue(spin, parity, sample):
    if spin == 0:
        local = F(1) if parity == 1 else sample["det"]
    else:
        local = sample[spin]
    return local**4 * sample[1]**8


def physical_action(polynomial, parity):
    output_parity = -parity
    product = polynomial_multiply(polynomial, character(1))
    decomposition = decompose(product)
    if output_parity == 1:
        decomposition.pop(0, None)
    return reconstruct(decomposition), output_parity, decomposition


def crossing(polynomial, parity, sample):
    decomposition = decompose(polynomial)
    crossed = {
        spin: coefficient * crossing_eigenvalue(spin, parity, sample)
        for spin, coefficient in decomposition.items()
    }
    return reconstruct(crossed), crossed


def layer(polynomial, parity, sample):
    residual, output_parity, _decomposition = physical_action(polynomial, parity)
    crossed, decomposition = crossing(residual, output_parity, sample)
    return crossed, output_parity, decomposition


def tower(sample, count=MAX_LAYER):
    polynomial = character(1)
    parity = -1
    levels = [(polynomial, parity, {1: F(1)})]
    while len(levels) < count:
        polynomial, parity, decomposition = layer(polynomial, parity, sample)
        levels.append((polynomial, parity, decomposition))
    return levels


def top_formula(sample, layer_index):
    result = F(1)
    for spin in range(2, layer_index + 1):
        result *= crossing_eigenvalue(spin, (-1) ** spin, sample)
    return result


def run_checks():
    checks = []
    identity = {"det": F(1), **{spin: F(1) for spin in range(1, MAX_LAYER + 1)}}
    expected = (
        ({1: F(1)}, -1),
        ({1: F(1), 2: F(1)}, 1),
        ({0: F(1), 1: F(2), 2: F(2), 3: F(1)}, -1),
        ({1: F(5), 2: F(5), 3: F(3), 4: F(1)}, 1),
    )
    identity_levels = tower(identity, 4)
    checks.append((
        "Laurent reconstruction gives the first four identity layers",
        tuple((decomposition, parity) for _polynomial, parity, decomposition in identity_levels)
        == expected,
    ))
    checks.append((
        "physical Q removes the even scalar at layers two and four",
        0 not in identity_levels[1][2] and 0 not in identity_levels[3][2],
    ))
    checks.append((
        "the odd determinant character survives physical Q at layer three",
        identity_levels[2][2].get(0) == 1 and identity_levels[2][1] == -1,
    ))

    exact_sample = sample_a()
    levels = tower(exact_sample)
    checks.append((
        "every Laurent layer has the universal top spin and coefficient",
        all(
            decomposition.get(index) == top_formula(exact_sample, index)
            for index, (_polynomial, _parity, decomposition) in enumerate(levels, start=1)
        ),
    ))
    checks.append((
        "every crossed physical layer has zero conditional Haar mean",
        all(not (parity == 1 and decomposition.get(0, F(0)))
            for _polynomial, parity, decomposition in levels),
    ))
    checks.append((
        "reconstruction and decomposition are inverse on every layer",
        all(reconstruct(decomposition) == polynomial
            for polynomial, _parity, decomposition in levels),
    ))

    seed = character(1)
    correct_polynomial, correct_parity, _correct_decomposition = layer(seed, -1, exact_sample)
    crossed_seed, _crossed_decomposition = crossing(seed, -1, exact_sample)
    reversed_polynomial, reversed_parity, _reversed_decomposition = physical_action(
        crossed_seed, -1
    )
    checks.append((
        "action/Q/crossing order differs from crossing/action/Q",
        correct_parity == reversed_parity and correct_polynomial != reversed_polynomial,
    ))
    return checks


def all_checks_pass():
    return all(passed for _label, passed in run_checks())


def main():
    checks = run_checks()
    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks)-failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
