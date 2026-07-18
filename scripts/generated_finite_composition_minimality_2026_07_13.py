#!/usr/bin/env python3
"""Exact finite checks for generated complex-qubit composition."""

from __future__ import annotations

from functools import reduce
from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GENERATED_FINITE_COMPOSITION_MINIMALITY_THEOREM_2026-07-13.md"

PASS = 0
FAIL = 0

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
PAULIS = (I2, X, Y, Z)


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    suffix = f" :: {detail}" if detail else ""
    if condition:
        PASS += 1
        print(f"PASS {label}{suffix}")
    else:
        FAIL += 1
        print(f"FAIL {label}{suffix}")


def tensor_all(factors: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return reduce(sp.kronecker_product, factors)


def pauli_products(site_count: int) -> tuple[sp.Matrix, ...]:
    return tuple(tensor_all(factors) for factors in product(PAULIS, repeat=site_count))


def span_rank(matrices: tuple[sp.Matrix, ...]) -> int:
    dimension = matrices[0].rows * matrices[0].cols
    return sp.Matrix.hstack(*(matrix.reshape(dimension, 1) for matrix in matrices)).rank()


def matrix_units(dim: int) -> tuple[sp.Matrix, ...]:
    units = []
    for row in range(dim):
        for column in range(dim):
            unit = sp.zeros(dim)
            unit[row, column] = 1
            units.append(unit)
    return tuple(units)


def source_contract() -> None:
    section("A - Theorem-note contract")
    raw = NOTE.read_text()
    note = " ".join(raw.lower().replace("**", "").split())
    check("A note is authority-free", "authority: none" in note)
    check("A theorem states faithful commuting embeddings", "faithful unital embeddings" in note and "images commute" in note)
    check("A theorem states generatedness", "generated as a `c*`-algebra" in note)
    check("A proof uses matrix-algebra simplicity", "simple matrix algebra" in note)
    check("A note contains N1-N8", all(f"### N{i}" in raw for i in range(1, 9)))


def generated_blocks() -> None:
    section("B - Generated finite blocks")
    for site_count in (1, 2, 3):
        products_n = pauli_products(site_count)
        expected = 4 ** site_count
        check(
            f"B {site_count}-site Pauli products have full rank {expected}",
            len(products_n) == expected and span_rank(products_n) == expected,
        )
        gram = sp.Matrix(
            [
                [sp.trace(left.conjugate().T * right) for right in products_n]
                for left in products_n
            ]
        )
        check(
            f"B {site_count}-site products are exactly Hilbert-Schmidt orthogonal",
            gram == (2 ** site_count) * sp.eye(expected),
        )

    two_site = pauli_products(2)
    local_a = tuple(sp.kronecker_product(pauli, I2) for pauli in PAULIS)
    local_b = tuple(sp.kronecker_product(I2, pauli) for pauli in PAULIS)
    check("B distinct local images commute", all(a * b == b * a for a in local_a for b in local_b))
    check("B products of local images reproduce the full Pauli basis", {tuple(a * b) for a in local_a for b in local_b} == {tuple(matrix) for matrix in two_site})


def extra_sector_controls() -> None:
    section("C - Generatedness excludes two independent extension types")
    products_2 = pauli_products(2)

    direct_sum_products = tuple(sp.diag(matrix, matrix) for matrix in products_2)
    direct_rank = span_rank(direct_sum_products)
    direct_center = sp.diag(sp.eye(4), -sp.eye(4))
    direct_span = sp.Matrix.hstack(*(matrix.reshape(64, 1) for matrix in direct_sum_products))
    check("C direct-sum local-product rank remains 16", direct_rank == 16)
    direct_sum_basis = tuple(
        candidate
        for unit in matrix_units(4)
        for candidate in (sp.diag(unit, sp.zeros(4)), sp.diag(sp.zeros(4), unit))
    )
    check("C direct-sum physical algebra has constructed complex dimension 32", span_rank(direct_sum_basis) == 32)
    check("C direct-sum central sector is outside generated span", sp.Matrix.hstack(direct_span, direct_center.reshape(64, 1)).rank() == 17)

    spectator_products = tuple(sp.kronecker_product(matrix, I2) for matrix in products_2)
    spectator_rank = span_rank(spectator_products)
    spectator_observable = sp.kronecker_product(sp.eye(4), Z)
    spectator_span = sp.Matrix.hstack(*(matrix.reshape(64, 1) for matrix in spectator_products))
    check("C spectator-factor local-product rank remains 16", spectator_rank == 16)
    check("C spectator physical algebra M8 has constructed complex dimension 64", span_rank(matrix_units(8)) == 64)
    check("C spectator observable is outside generated span", sp.Matrix.hstack(spectator_span, spectator_observable.reshape(64, 1)).rank() == 17)


def category_classification() -> None:
    section("D - Category-relative equivalence classification")
    note = " ".join(NOTE.read_text().lower().replace("**", "").replace("`", "").split())
    for marker in (
        "necessary and sufficient for the ordinary abstract tensor product",
        "category-relative algebraic equivalence",
        "canonical-law domain",
        "operational extensionality",
        "irreducibility/duality theorem",
        "no universal physical-minimality claim",
    ):
        check(f"D note marker: {marker}", marker in note)


def main() -> None:
    source_contract()
    generated_blocks()
    extra_sector_controls()
    category_classification()
    print("\n" + "=" * 79)
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        raise SystemExit(1)
    print("RESULT: PASS")
    print("BOUNDARY: finite-dimensional complex C*-algebra theorem; no axiom edit is made")


if __name__ == "__main__":
    main()
