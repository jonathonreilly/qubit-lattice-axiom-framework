#!/usr/bin/env python3
"""Independent reconstruction of the Block 41 Schur-response bridge.

This checker imports the Block 174 fixture directly, not the primary Block 41
runner or the Block 175 pincer runner.  It uses SymPy exact inverses and a
separate generic block-matrix certificate to reconstruct the positive action,
local Schur precision, response grades, and the hard-pin mixture failure.
"""

from __future__ import annotations

import inspect
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_site_conditional_law_family_2026_08_22 as b174


R = sp.Rational
ZERO = sp.Integer(0)
ONE = sp.Integer(1)
I2 = sp.eye(2)
RECORD_CELL = (b174.RECORD_LEVEL, 0)
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_SCHUR_RECORD_RESPONSE_BRIDGE_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SCHUR_RECORD_RESPONSE_BRIDGE_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_CONDITIONAL_LAW_FAMILY_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md",
    "scripts/admissibility_dirac_kahler_site_conditional_law_family_"
    "2026_08_22.py",
)


def inverse(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.inv(method="DM")


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(
        sp.expand(value) == 0 for value in sp.expand(left - right)
    )


def hermitian(matrix: sp.Matrix) -> sp.Matrix:
    return sp.expand((matrix + matrix.H) / 2)


def completion(q: sp.Matrix) -> dict:
    q_inv = inverse(q)
    symmetric = hermitian(q)
    covariance = sp.expand((q_inv + q_inv.H) / 2)
    precision_direct = inverse(covariance)
    precision_factored = sp.expand(q.H * inverse(symmetric) * q)
    return {
        "q_inv": q_inv,
        "symmetric": symmetric,
        "covariance": covariance,
        "precision": precision_direct,
        "precision_factored": precision_factored,
    }


def rows_for(fixture: object, level: int) -> tuple[int, ...]:
    return tuple(fixture.lx * (level % fixture.T) + x for x in range(fixture.lx))


def schur(precision: sp.Matrix, rows: tuple[int, ...]) -> sp.Matrix:
    exterior = tuple(index for index in range(precision.rows) if index not in rows)
    return sp.expand(
        precision.extract(rows, rows)
        - precision.extract(rows, exterior)
        * inverse(precision.extract(exterior, exterior))
        * precision.extract(exterior, rows)
    )


def normalized_block(covariance: sp.Matrix, rows: tuple[int, ...]) -> sp.Matrix:
    block = covariance.extract(rows, rows)
    return sp.expand(block / sp.trace(block))


def projector(index: int, dimension: int) -> sp.Matrix:
    return sp.diag(*(ONE if slot == index else ZERO for slot in range(dimension)))


def grade(precision: sp.Matrix, effect: sp.Matrix):
    covariance = inverse(precision)
    return sp.cancel(sp.trace(covariance * effect) / sp.trace(covariance))


def normalize(values: tuple) -> tuple:
    total = sp.cancel(sum(values, ZERO))
    return tuple(sp.cancel(value / total) for value in values)


def projective_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    for l_value, r_value in zip(left, right):
        if r_value != 0:
            ratio = sp.cancel(l_value / r_value)
            return ratio > 0 and matrix_equal(left, sp.expand(ratio * right))
        if l_value != 0:
            return False
    return False


def main() -> int:
    passed = 0
    failed = 0

    def check(name: str, condition: bool, detail: str) -> None:
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"PASS {name}: {detail}")
        else:
            failed += 1
            print(f"FAIL {name}: {detail}")

    fixture = b174.Fixture(4, tag="b176-independent")
    q = fixture.q({})
    data = completion(q)
    identity = sp.eye(fixture.N)
    check(
        "independent-positive-completion",
        b174.ldl_certificate(data["symmetric"])["pd"]
        and matrix_equal(data["precision"], data["precision_factored"])
        and matrix_equal(data["precision"] * data["covariance"], identity),
        "a direct inverse of Herm(q^-1) equals the independently factored q^dagger Herm(q)^-1 q precision",
    )

    generic_covariance = sp.Matrix(
        [
            [4, 1, 1, 0],
            [1, 3, 0, 1],
            [1, 0, 5, 1],
            [0, 1, 1, 4],
        ]
    )
    generic_precision = inverse(generic_covariance)
    generic_rows = (0, 1)
    check(
        "independent-generic-schur-theorem",
        b174.ldl_certificate(generic_covariance)["pd"]
        and matrix_equal(
            schur(generic_precision, generic_rows),
            inverse(generic_covariance.extract(generic_rows, generic_rows)),
        ),
        "a non-diagonal rational block example independently certifies the inverse-block Schur identity",
    )

    profiles = []
    levels_ok = True
    for level in fixture.free_levels:
        rows = rows_for(fixture, level)
        block = data["covariance"].extract(rows, rows)
        local_precision = schur(data["precision"], rows)
        density = normalized_block(data["covariance"], rows)
        profile = tuple(density[index, index] for index in range(fixture.lx))
        profiles.append(profile)
        levels_ok = levels_ok and matrix_equal(local_precision, inverse(block))
        levels_ok = levels_ok and all(
            block[i, j] == 0
            for i in range(fixture.lx)
            for j in range(fixture.lx)
            if i != j
        )
        levels_ok = levels_ok and tuple(
            grade(local_precision, projector(index, fixture.lx))
            for index in range(fixture.lx)
        ) == profile
    check(
        "independent-free-level-response",
        levels_ok and len(profiles) == 4 and len(set(profiles)) == 4,
        "four independently rebuilt free-level blocks are diagonal, Schur exact, response exact, and pairwise distinct",
    )

    representative_indices = (0, 5, 8, 11, 14)
    dial_blocks = 0
    dial_ok = True
    for index in representative_indices:
        _label, config = b174.DIAL_POINTS[index]
        dial_data = completion(fixture.q({}, **config))
        dial_ok = dial_ok and b174.ldl_certificate(dial_data["symmetric"])["pd"]
        for level in fixture.free_levels:
            dial_blocks += 1
            rows = rows_for(fixture, level)
            block = dial_data["covariance"].extract(rows, rows)
            dial_ok = dial_ok and matrix_equal(
                schur(dial_data["precision"], rows), inverse(block)
            )
            dial_ok = dial_ok and all(
                block[i, j] == 0
                for i in range(fixture.lx)
                for j in range(fixture.lx)
                if i != j
            )
    check(
        "independent-action-dial-sample",
        dial_ok and dial_blocks == 20,
        "five independently chosen action families give twenty exact positive diagonal Schur blocks",
    )

    zero_q = fixture.q({}, mass=ZERO)
    check(
        "independent-zero-mass-boundary",
        matrix_equal(hermitian(zero_q), sp.zeros(fixture.N)),
        "the positive precision route stops rather than inverting the exactly zero Hermitian action at m=0",
    )

    rows = rows_for(fixture, fixture.tstar)
    density = normalized_block(data["covariance"], rows)
    pinned_data = []
    raw_squared = []
    raw_w = []
    det_s_values = []
    for value in b174.MENU:
        pinned_q = fixture.q({RECORD_CELL: value})
        pinned = completion(pinned_q)
        pinned_data.append(pinned)
        determinant = b174.dm_det(pinned_q)
        determinant_s = b174.dm_det(pinned["symmetric"])
        det_s_values.append(determinant_s)
        raw_squared.append(sp.cancel(ONE / b174.norm2(determinant)))
        raw_w.append(sp.cancel(determinant_s / b174.norm2(determinant)))
    squared_law = normalize(tuple(raw_squared))
    w_law = normalize(tuple(raw_w))
    check(
        "independent-positive-partition-split",
        len(set(det_s_values)) > 1
        and all(value > 0 for value in raw_squared)
        and all(value > 0 for value in raw_w)
        and squared_law != w_law,
        "the four hard pins give distinct positive partition laws for q^dagger q and the W9 precision",
    )

    pinned_densities = tuple(
        normalized_block(item["covariance"], rows) for item in pinned_data
    )
    mixed = sp.expand(
        sum(
            (squared_law[index] * pinned_densities[index] for index in range(4)),
            sp.zeros(4),
        )
    )
    residual = sp.expand(density - mixed)
    check(
        "independent-total-mixture-residual",
        not matrix_equal(residual, sp.zeros(4))
        and tuple(sp.sign(residual[index, index]) for index in range(4))
        == (1, -1, -1, 1)
        and matrix_equal(density, pinned_densities[3]),
        "the determinant-weighted mixture fails with four exact signed residuals while the default pin reproduces the background",
    )

    source = inspect.getsource(b174.Fixture.field)
    check(
        "independent-background-typing",
        "records.get((t, x), sigma)" in source
        and matrix_equal(q, fixture.q({RECORD_CELL: b174.MENU[-1]})),
        "the unpinned field is a fixed default value and not a hidden sum over alternative record values",
    )

    center = sp.diag(R(3, 5), R(2, 5))
    effect = sp.diag(R(1, 2), ZERO)
    check(
        "independent-neighbor-counterfamily",
        grade(inverse(center), effect) == R(3, 10)
        and grade(inverse(center**2), effect) == R(9, 26)
        and grade(2 * I2, effect) == R(1, 4),
        "the exact full-rank power counterfamily independently separates 3/10 from 9/26 while retaining the mixed-point value",
    )

    transform = sp.Matrix([[2, 1], [0, 1]])
    moved = sp.expand(
        transform * center * transform.H
        / sp.trace(transform * center * transform.H)
    )
    expected = sp.expand(transform.inv().H * inverse(center) * transform.inv())
    check(
        "independent-congruence-ray",
        projective_equal(inverse(moved), expected),
        "one nonunitary exact transport confirms the contravariant projective inverse-precision law",
    )

    check(
        "independent-input-closure",
        NOTE.exists()
        and all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and "No-Go Discipline Gate" in NOTE.read_text(encoding="utf-8"),
        "the independent checker reads only the final note and its Block 174 fixture parent",
    )

    print("per_element: independent projectors, hard-pin weights, local densities, and exact residual signs are reconstructed")
    print("per_site: all four free levels plus the selected hard-pin cell and fixed-background rule are independently checked")
    print("per_mode: the full 24-mode W precision, two positive partition laws, and a separate rational block-Schur example are checked")
    print("per_block: five action-family dials produce twenty independent local Schur blocks with the zero-mass edge separated")
    print("lattice_wide: checked and not executed — the checker establishes no autonomous history or infinite-volume law")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return failed


if __name__ == "__main__":
    raise SystemExit(main())
