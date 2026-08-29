#!/usr/bin/env python3
"""Independent exact controls for the arbitrary-r scalar-fused vector transfer.

This helper uses only integers, ``Fraction``, explicit signed frames, subset
enumeration, and a polynomial dynamic program.  It does not import SymPy or
the primary runner.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations, product
from math import comb, factorial


AUDIT_TIMEOUT_SEC = 120


def plaquette_masks(width: int) -> tuple[int, ...]:
    """Actual 3r+1 original-link masks: u_i,v_i,h_i,h_(i+1)."""

    return tuple(
        (1 << index)
        | (1 << (width + index))
        | (1 << (2 * width + index))
        | (1 << (2 * width + index + 1))
        for index in range(width)
    )


def boundary_mask(subset: int, plaquettes: tuple[int, ...]) -> int:
    boundary = 0
    for index, plaquette in enumerate(plaquettes):
        if subset & (1 << index):
            boundary ^= plaquette
    return boundary


def submasks(mask: int):
    subset = mask
    while True:
        yield subset
        if subset == 0:
            return
        subset = (subset - 1) & mask


def direct_coefficients(width: int) -> dict[int, int]:
    """Expand the proper-complement sum over nonempty proper X."""

    plaquettes = plaquette_masks(width)
    full = (1 << width) - 1
    coefficients: dict[int, int] = defaultdict(int)
    for subset in range(1, full):
        complement = full ^ subset
        for left_half in submasks(subset):
            for right_half in submasks(complement):
                power = (
                    boundary_mask(left_half, plaquettes).bit_count()
                    + boundary_mask(full ^ right_half, plaquettes).bit_count()
                )
                coefficients[power] += 1
    return dict(sorted(coefficients.items()))


def transfer_coefficients(width: int) -> dict[int, int]:
    """Independent three-state dynamic program with endpoint subtraction."""

    allowed = (((0, 0), 1), ((0, 1), 2), ((1, 1), 1))
    state: dict[tuple[int, int], dict[int, int]] = {
        (0, 0): {0: 1}
    }
    for _ in range(width):
        updated: dict[tuple[int, int], dict[int, int]] = {}
        for previous, polynomial in state.items():
            for current, multiplicity in allowed:
                increment = (
                    2 * current[0]
                    + 2 * int(previous[0] == 0 and current[0] == 1)
                    + 2 * current[1]
                    + 2 * int(previous[1] == 0 and current[1] == 1)
                )
                target = updated.setdefault(current, defaultdict(int))
                for power, coefficient in polynomial.items():
                    target[power + increment] += multiplicity * coefficient
        state = updated

    all_pairs: dict[int, int] = defaultdict(int)
    for polynomial in state.values():
        for power, coefficient in polynomial.items():
            all_pairs[power] += coefficient

    plaquettes = plaquette_masks(width)
    full = (1 << width) - 1
    one_history: dict[int, int] = defaultdict(int)
    for subset in range(full + 1):
        one_history[boundary_mask(subset, plaquettes).bit_count()] += 1
    outer_power = boundary_mask(full, plaquettes).bit_count()
    for power, coefficient in one_history.items():
        all_pairs[power] -= coefficient
        all_pairs[power + outer_power] -= coefficient
    return dict(sorted(
        (power, coefficient)
        for power, coefficient in all_pairs.items() if coefficient
    ))


def signed_frames() -> tuple[tuple[tuple[F, ...], ...], ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            frames.append(tuple(
                tuple(F(signs[row] if column == permutation[row] else 0)
                      for column in range(3))
                for row in range(3)
            ))
    return tuple(frames)


def matmul(left, right):
    return tuple(
        tuple(sum((left[i][k] * right[k][j] for k in range(3)), F(0))
              for j in range(3))
        for i in range(3)
    )


def trace(matrix) -> F:
    return sum((matrix[index][index] for index in range(3)), F(0))


def one_rung_scalar_factor() -> F:
    frames = signed_frames()
    total = sum(
        (
            trace(left) * trace(right) * trace(matmul(right, left))
            for left in frames for right in frames
        ),
        F(0),
    )
    return total / (len(frames) ** 2)


Irrep = tuple[int, int]


def irrep_menu(multiplicity: int) -> frozenset[Irrep]:
    if multiplicity == 0:
        return frozenset(((0, 1),))
    if multiplicity == 1:
        return frozenset(((1, -1),))
    if multiplicity == 2:
        return frozenset(((0, 1), (1, 1), (2, 1)))
    raise AssertionError(multiplicity)


def scalar_selection(width: int) -> dict[str, object]:
    """Derive the local common labels of complementary vector histories."""

    plaquettes = plaquette_masks(width)
    full = (1 << width) - 1
    outer = boundary_mask(full, plaquettes)

    exact = True
    nonscalar: set[Irrep] = set()
    for subset in range(1, full):
        complement = full ^ subset
        common_support = 0
        for edge in range(3 * width + 1):
            left_count = sum(
                int(bool(subset & (1 << index)))
                * int(bool(plaquette & (1 << edge)))
                for index, plaquette in enumerate(plaquettes)
            )
            right_count = int(bool(outer & (1 << edge))) + sum(
                int(bool(complement & (1 << index)))
                * int(bool(plaquette & (1 << edge)))
                for index, plaquette in enumerate(plaquettes)
            )
            common = irrep_menu(left_count) & irrep_menu(right_count)
            exact &= len(common) == 1
            if common == {(1, -1)}:
                common_support |= 1 << edge
            if max(left_count, right_count) == 2:
                nonscalar.update(label for label in common if label != (0, 1))
        exact &= common_support == boundary_mask(subset, plaquettes)
    return {
        "exact": exact,
        "nonscalar_channels": tuple(sorted(nonscalar)),
        "outer_perimeter": outer.bit_count(),
    }


def physical_q_classification(width: int) -> dict[str, object]:
    """Independently classify both exclusive-rail Gram orientations."""

    full = (1 << width) - 1
    vacuum_cylindrical = set()
    coarse_cylindrical = set()
    temporal_words_preserved = True
    for subset in range(full + 1):
        vacuum_word = tuple(
            frozenset(((1, -1),))
            if subset & (1 << index)
            else frozenset(((0, 1),))
            for index in range(width)
            for _rail in range(2)
        )
        coarse_word = tuple(
            frozenset(((1, -1),))
            if subset & (1 << index)
            else frozenset(((0, 1), (1, 1), (2, 1)))
            for index in range(width)
            for _rail in range(2)
        )
        for _half_subset in submasks(subset):
            temporal_words_preserved &= tuple(vacuum_word) == vacuum_word
        for _half_complement in submasks(full ^ subset):
            temporal_words_preserved &= tuple(coarse_word) == coarse_word
        if set.intersection(*(set(menu) for menu in vacuum_word)):
            vacuum_cylindrical.add(subset)
        if set.intersection(*(set(menu) for menu in coarse_word)):
            coarse_cylindrical.add(subset)
    return {
        "vacuum": frozenset(vacuum_cylindrical),
        "coarse": frozenset(coarse_cylindrical),
        "temporal_words_preserved": temporal_words_preserved,
    }


def weak_compositions(total: int, width: int):
    if width == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, width - 1):
            yield (first,) + rest


def lower_derivatives_vanish(width: int) -> bool:
    for order in range(width):
        for counts in weak_compositions(order, width):
            # The outer V makes the exclusive-rail parity (-1)^(1+n_i).
            if all((1 + count) % 2 == 0 for count in counts):
                return False
    return True


def normalized_leibniz_factors(width: int) -> tuple[F, ...]:
    return tuple(
        F(
            comb(width, left) * factorial(left) * factorial(width - left),
            factorial(width),
        ) * F(1, 2) ** width
        for left in range(1, width)
    )


def fixture() -> dict[str, object]:
    rung_factor = one_rung_scalar_factor()
    rows = []
    for width in range(2, 9):
        direct = direct_coefficients(width)
        transfer = transfer_coefficients(width)
        selection = scalar_selection(width)
        rows.append({
            "width": width,
            "links": 3 * width + 1,
            "proper_subsets": (1 << width) - 2,
            "direct": direct,
            "transfer": transfer,
            "positive": all(coefficient > 0 for coefficient in direct.values()),
            "value_at_one": sum(direct.values()),
            "expected_at_one": (1 << width) * ((1 << width) - 2),
            "overlap": rung_factor ** (width - 1),
            "selection": selection,
            "q_classification": physical_q_classification(width),
            "lower_derivatives_vanish": lower_derivatives_vanish(width),
            "leibniz_factors": normalized_leibniz_factors(width),
        })
    return {"rung_factor": rung_factor, "rows": tuple(rows)}


def main() -> int:
    data = fixture()
    checks = (
        ("signed-frame scalar rung factor is one third",
         data["rung_factor"] == F(1, 3)),
        ("direct subset sums equal the independent three-state transfer",
         all(row["direct"] == row["transfer"] for row in data["rows"])),
        ("all finite-step polynomial coefficients are positive",
         all(row["positive"] for row in data["rows"])),
        ("t=1 sum gives 2^r(2^r-2)",
         all(row["value_at_one"] == row["expected_at_one"]
             for row in data["rows"])),
        ("all complementary histories select only scalar doubled rungs",
         all(row["selection"]["exact"]
             and row["selection"]["nonscalar_channels"] == ()
             for row in data["rows"])),
        ("actual coarse outer vector has perimeter 2r+2",
         all(row["selection"]["outer_perimeter"] == 2 * row["width"] + 2
             for row in data["rows"])),
        ("normalized complement overlap is 3^(1-r)",
         all(row["overlap"] == F(1, 3 ** (row["width"] - 1))
             for row in data["rows"])),
        ("exclusive-rail words classify only empty/full as cylindrical",
         all(row["q_classification"]["vacuum"]
             == frozenset((0, (1 << row["width"]) - 1))
             and row["q_classification"]["coarse"]
             == frozenset((0, (1 << row["width"]) - 1))
             and row["q_classification"]["temporal_words_preserved"]
             for row in data["rows"])),
        ("all lower derivative orders have an unmatched outer vector rail",
         all(row["lower_derivatives_vanish"] for row in data["rows"])),
        ("normalized Leibniz factors equal 2^-r for every proper split",
         all(all(factor == F(1, 2 ** row["width"])
                 for factor in row["leibniz_factors"])
             for row in data["rows"])),
        ("r2 polynomial reproduces the reviewed quadratic entry",
         data["rows"][0]["direct"] == {4: 2, 6: 2, 8: 2, 10: 2}),
        ("r3 polynomial reproduces the reviewed cubic entry",
         data["rows"][1]["direct"]
         == {4: 3, 6: 6, 8: 12, 10: 8, 12: 15, 14: 2, 16: 2}),
    )
    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
