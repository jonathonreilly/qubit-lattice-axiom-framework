#!/usr/bin/env python3
"""Verify the exact b-eigenvalue determinant of a paired-direction coin."""

from __future__ import annotations

import sys

import sympy as sym


def paired_direction_coin(b: sym.Symbol) -> sym.Matrix:
    """Return Q(b) = 2P + (b-1)I/2 - (b+1)R/2."""
    identity = sym.eye(6)
    opposite_swap = sym.zeros(6)
    for row, column in enumerate((1, 0, 3, 2, 5, 4)):
        opposite_swap[row, column] = 1
    scalar_projector = sym.ones(6) / 6
    return (
        2 * scalar_projector
        + (b - 1) * identity / 2
        - (b + 1) * opposite_swap / 2
    )


def direct_full_determinant(
    b: sym.Symbol, x: sym.Symbol, y: sym.Symbol, z: sym.Symbol
) -> sym.Expr:
    """Compute the target from the full 6 x 6 matrix."""
    stream = sym.diag(x, 1 / x, y, 1 / y, z, 1 / z)
    return sym.factor((stream @ paired_direction_coin(b) - b * sym.eye(6)).det())


def block_rank_one_determinant(
    b: sym.Symbol, x: sym.Symbol, y: sym.Symbol, z: sym.Symbol
) -> tuple[sym.Expr, tuple[sym.Expr, ...], tuple[sym.Expr, ...]]:
    """Recompute by independent 2 x 2 blocks and a rank-one update."""
    a = (b - 1) / 2
    c = (b + 1) / 2
    block_determinants = []
    block_inverse_contributions = []
    for t in (x, y, z):
        block = sym.Matrix(
            (
                (t * a - b, -t * c),
                (-c / t, a / t - b),
            )
        )
        direction_pair = sym.Matrix((t, 1 / t))
        block_determinants.append(sym.factor(block.det()))
        block_inverse_contributions.append(
            sym.factor((sym.ones(1, 2) * block.inv() * direction_pair)[0])
        )

    determinant_of_blocks = sym.prod(block_determinants)
    rank_one_multiplier = 1 + sum(block_inverse_contributions) / 3
    result = sym.factor(determinant_of_blocks * rank_one_multiplier)
    return result, tuple(block_determinants), tuple(block_inverse_contributions)


def main() -> int:
    b, lam = sym.symbols("b lambda")
    x, y, z = sym.symbols("x y z", nonzero=True)
    checks: list[tuple[str, bool, object]] = []

    expected = sym.factor(
        -b**3
        * (b - 1) ** 2
        * (b + 1)
        * (x - 1) ** 2
        * (y - 1) ** 2
        * (z - 1) ** 2
        / (8 * x * y * z)
    )

    direct = direct_full_determinant(b, x, y, z)
    block_result, block_determinants, block_contributions = (
        block_rank_one_determinant(b, x, y, z)
    )

    checks.append(
        (
            "direct full determinant equals the stated Laurent factorization",
            sym.cancel(direct - expected) == 0,
            direct,
        )
    )
    checks.append(
        (
            "independent block/rank-one route equals the full determinant",
            sym.cancel(block_result - direct) == 0,
            block_result,
        )
    )

    expected_blocks = tuple(
        sym.factor(-b * (b - 1) * (t - 1) ** 2 / (2 * t))
        for t in (x, y, z)
    )
    checks.append(
        (
            "all three 2 x 2 block determinants have the required factor",
            all(
                sym.cancel(actual - target) == 0
                for actual, target in zip(block_determinants, expected_blocks)
            ),
            block_determinants,
        )
    )
    checks.append(
        (
            "each block supplies 2/(b-1) to the rank-one multiplier",
            all(
                sym.cancel(value - 2 / (b - 1)) == 0
                for value in block_contributions
            ),
            block_contributions,
        )
    )

    coin = paired_direction_coin(b)
    characteristic = sym.factor((lam * sym.eye(6) - coin).det())
    expected_characteristic = (lam - 1) * (lam + 1) ** 2 * (lam - b) ** 3
    checks.append(
        (
            "zero-momentum characteristic multiplicities are 1, 2, and 3",
            sym.expand(characteristic - expected_characteristic) == 0,
            characteristic,
        )
    )

    witness = {b: 7, x: 2, y: 3, z: 5}
    witness_value = sym.factor(direct.subs(witness))
    checks.append(
        (
            "generic exact witness is nonzero",
            witness_value == sym.Rational(-131712, 5),
            witness_value,
        )
    )
    checks.append(
        (
            "wrong-sign control is rejected",
            sym.factor((direct + expected).subs(witness)) != 0,
            sym.factor((direct + expected).subs(witness)),
        )
    )
    missing_b_plus_one = expected / (b + 1)
    checks.append(
        (
            "missing-(b+1) control is rejected",
            sym.factor((direct - missing_b_plus_one).subs(witness)) != 0,
            sym.factor((direct - missing_b_plus_one).subs(witness)),
        )
    )

    specializations = (
        ({b: 0, x: 2, y: 3, z: 5}, 0),
        ({b: 1, x: 2, y: 3, z: 5}, 0),
        ({b: -1, x: 2, y: 3, z: 5}, 0),
        ({b: 7, x: 1, y: 3, z: 5}, 0),
    )
    checks.append(
        (
            "singular-parameter and coordinate-factor specializations agree exactly",
            all(
                sym.factor(direct.subs(values)) == target
                and sym.factor(expected.subs(values)) == target
                for values, target in specializations
            ),
            specializations,
        )
    )

    failures = 0
    for label, passed, detail in checks:
        print("PASS" if passed else "FAIL", label, "::", detail)
        failures += int(not passed)
    print(f"RESULT pass={len(checks) - failures} fail={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
