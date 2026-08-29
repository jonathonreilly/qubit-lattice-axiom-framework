#!/usr/bin/env python3
"""Independent bit-word and matrix checks for the interval endpoint automaton."""

from __future__ import annotations

from fractions import Fraction as F

import sympy as sp


AUDIT_TIMEOUT_SEC = 120


def interval_masks(q_cells: int) -> tuple[int, ...]:
    masks = [0]
    for left in range(q_cells):
        mask = 0
        for right in range(left, q_cells):
            mask |= 1 << right
            masks.append(mask)
    return tuple(masks)


def repeated_fine_word(mask: int, q_cells: int) -> int:
    word = 0
    for cell in range(q_cells):
        if mask & (1 << cell):
            word |= 3 << (2 * cell)
    return word


def selector_matches(left: int, right: int, q_cells: int) -> tuple[tuple[int, int], ...]:
    difference = repeated_fine_word(left ^ right, q_cells)
    return tuple(
        (p_left, p_right)
        for p_left in range(2 * q_cells)
        for p_right in range(2 * q_cells)
        if p_left != p_right
        and difference == (1 << p_left) ^ (1 << p_right)
    )


def endpoint_cell(shorter: int, longer: int, q_cells: int) -> int | None:
    if shorter & ~longer:
        return None
    difference = shorter ^ longer
    if difference == 0 or difference & (difference - 1):
        return None
    cell = difference.bit_length() - 1
    # The mask dictionary already restricts both words to intervals; a
    # one-cell nested difference is necessarily an endpoint extension.
    return cell if cell < q_cells else None


def beta_zero(t):
    return sp.expand((1 + t**4) * (t**4 + t**6) / 6)


def beta_one(t):
    return sp.expand(t**14 * (1 + 4 * t**2 + t**4 + 2 * t**6) / 36)


def expected_weight(shorter: int, longer: int, q_cells: int, t, amplitudes):
    cell = endpoint_cell(shorter, longer, q_cells)
    if cell is None:
        return sp.Integer(0)
    length = shorter.bit_count()
    base = beta_zero(t) if length == 0 else beta_one(t) * t ** (8 * (length - 1))
    return sp.expand(amplitudes[cell] * base)


def transition_matrix(symbol: tuple[int, int], amplitude, t):
    """Row-to-column weighted transition on B,U,C0,C1,D,X."""

    matrix = sp.zeros(6, 6)
    B, U, C0, C1, D, X = range(6)
    matrix[X, X] = 1
    if symbol == (0, 0):
        matrix[B, B] = 1
        matrix[U, D] = beta_zero(t)
        matrix[C0, X] = 1
        matrix[C1, D] = 1
        matrix[D, D] = 1
    elif symbol == (0, 1):
        matrix[B, U] = amplitude
        matrix[U, X] = 1
        matrix[C0, D] = amplitude
        matrix[C1, X] = 1
        matrix[D, X] = 1
    elif symbol == (1, 1):
        matrix[B, C0] = beta_one(t)
        matrix[U, C1] = beta_one(t)
        matrix[C0, C0] = t**8
        matrix[C1, C1] = t**8
        matrix[D, X] = 1
    else:
        for state in range(5):
            matrix[state, X] = 1
    return matrix


def matrix_automaton(shorter: int, longer: int, q_cells: int, t, amplitudes):
    row = sp.zeros(1, 6)
    row[0, 0] = 1
    for cell in range(q_cells):
        symbol = (
            int(bool(shorter & (1 << cell))),
            int(bool(longer & (1 << cell))),
        )
        row = row * transition_matrix(symbol, amplitudes[cell], t)
    # End marker has the same accepting effect as the first trailing 00,
    # without allowing B to become accepted.
    B, U, C0, C1, D, X = range(6)
    return sp.expand(row[0, U] * beta_zero(t) + row[0, C1] + row[0, D])


def coefficient_terms(length: int) -> dict[int, F]:
    if length == 0:
        return {4: F(1, 6), 6: F(1, 6), 8: F(1, 6), 10: F(1, 6)}
    shift = 8 * (length - 1)
    return {
        shift + 14: F(1, 36),
        shift + 16: F(4, 36),
        shift + 18: F(1, 36),
        shift + 20: F(2, 36),
    }


def evaluate(terms: dict[int, F], t_value: F) -> F:
    return sum((coefficient * t_value**power for power, coefficient in terms.items()), F(0))


def fixture() -> dict[str, object]:
    t = sp.symbols("t_V", positive=True)
    selector_ok = True
    edge_counts = []
    automaton_ok = True
    reflection_ok = True
    zero_falsifiers_ok = True

    for q_cells in range(1, 7):
        masks = interval_masks(q_cells)
        amplitudes = tuple(sp.symbols(f"A0:{q_cells}"))
        edges = 0
        for index, left in enumerate(masks):
            for right in masks[index + 1:]:
                matches = selector_matches(left, right, q_cells)
                nested_cell = endpoint_cell(left, right, q_cells)
                if nested_cell is None:
                    nested_cell = endpoint_cell(right, left, q_cells)
                expected_matches = () if nested_cell is None else (
                    (2 * nested_cell, 2 * nested_cell + 1),
                    (2 * nested_cell + 1, 2 * nested_cell),
                )
                selector_ok &= matches == expected_matches
                edges += int(bool(matches))

        for shorter in masks:
            for longer in masks:
                if shorter == longer:
                    continue
                expected = expected_weight(shorter, longer, q_cells, t, amplitudes)
                actual = matrix_automaton(shorter, longer, q_cells, t, amplitudes)
                automaton_ok &= sp.expand(actual - expected) == 0
        edge_counts.append(edges)

        # Mirror every interval and compare the unit-amplitude coefficient.
        def reflect(mask: int) -> int:
            result = 0
            for cell in range(q_cells):
                if mask & (1 << cell):
                    result |= 1 << (q_cells - 1 - cell)
            return result

        unit = tuple(sp.Integer(1) for _ in range(q_cells))
        for shorter in masks:
            for longer in masks:
                reflection_ok &= (
                    expected_weight(shorter, longer, q_cells, t, unit)
                    == expected_weight(reflect(shorter), reflect(longer), q_cells, t, unit)
                )

    vacuum_split_ok = coefficient_terms(0) != coefficient_terms(1)
    dressing_ok = all(
        evaluate(coefficient_terms(length + 1), F(1, 2))
        == F(1, 2) ** 8 * evaluate(coefficient_terms(length), F(1, 2))
        for length in range(1, 6)
    )
    # Shifted intervals and a length-two jump are explicit hostile controls.
    zero_falsifiers_ok &= selector_matches(0b001, 0b010, 3) == ()
    zero_falsifiers_ok &= selector_matches(0b011, 0b110, 3) == ()
    zero_falsifiers_ok &= selector_matches(0, 0b011, 3) == ()

    return {
        "selector_ok": selector_ok,
        "edge_counts": tuple(edge_counts),
        "automaton_ok": automaton_ok,
        "vacuum_split_ok": vacuum_split_ok,
        "dressing_ok": dressing_ok,
        "reflection_ok": reflection_ok,
        "zero_falsifiers_ok": zero_falsifiers_ok,
    }


def main() -> int:
    data = fixture()
    checks = (
        ("repeated fine-bit selector is exact", data["selector_ok"]),
        ("the interval endpoint graph has q squared edges",
         data["edge_counts"] == tuple(q * q for q in range(1, 7))),
        ("six-state matrix automaton equals direct endpoint weights", data["automaton_ok"]),
        ("vacuum and occupied recouplings remain distinct", data["vacuum_split_ok"]),
        ("each added common cell gives t^8", data["dressing_ok"]),
        ("left and right endpoint extensions agree under reflection", data["reflection_ok"]),
        ("shifted and multi-cell differences vanish", data["zero_falsifiers_ok"]),
    )
    failures = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(checks) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
