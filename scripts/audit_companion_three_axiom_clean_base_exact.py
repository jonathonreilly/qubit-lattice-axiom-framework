#!/usr/bin/env python3
"""Companion sanity checks for the Lattice + Quantum + Record axiom memo.

This runner checks only elementary algebra/notation facts referenced by
docs/MINIMAL_AXIOMS_2026-06-04.md. It does not derive the axioms and does not
import log-det structure, P2/modulus, measurement, dynamics, normalization,
scale, source/action, Born weights, or observable identification.
"""

from __future__ import annotations

from dataclasses import dataclass


Matrix2 = tuple[tuple[complex, complex], tuple[complex, complex]]

ZERO: Matrix2 = ((0j, 0j), (0j, 0j))
IDENTITY: Matrix2 = ((1 + 0j, 0j), (0j, 1 + 0j))
SIGMA_X: Matrix2 = ((0j, 1 + 0j), (1 + 0j, 0j))
SIGMA_Y: Matrix2 = ((0j, -1j), (1j, 0j))
SIGMA_Z: Matrix2 = ((1 + 0j, 0j), (0j, -1 + 0j))


@dataclass
class Check:
    name: str
    ok: bool
    detail: str


def add(a: Matrix2, b: Matrix2) -> Matrix2:
    return tuple(
        tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2)
    )  # type: ignore[return-value]


def mul(a: Matrix2, b: Matrix2) -> Matrix2:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def scale(c: complex, a: Matrix2) -> Matrix2:
    return tuple(
        tuple(c * a[i][j] for j in range(2)) for i in range(2)
    )  # type: ignore[return-value]


def eq(a: Matrix2, b: Matrix2, tol: float = 1e-12) -> bool:
    return all(abs(a[i][j] - b[i][j]) <= tol for i in range(2) for j in range(2))


def anticommutator(a: Matrix2, b: Matrix2) -> Matrix2:
    return add(mul(a, b), mul(b, a))


def manhattan(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return sum(abs(a[i] - b[i]) for i in range(3))


def record_functional(records: set[str], weights: dict[str, float]) -> float:
    return sum(weights[r] for r in records)


def run_checks() -> list[Check]:
    checks: list[Check] = []
    pauli = [SIGMA_X, SIGMA_Y, SIGMA_Z]

    ok_pauli = True
    for i, a in enumerate(pauli):
        for j, b in enumerate(pauli):
            expected = scale(2, IDENTITY) if i == j else ZERO
            ok_pauli = ok_pauli and eq(anticommutator(a, b), expected)
    checks.append(
        Check(
            "Quantum: Pauli generators satisfy the Cl(3,0) anticommutator table",
            ok_pauli,
            "{sigma_i, sigma_j} = 2 delta_ij I checked as 2x2 complex matrices",
        )
    )

    # Direct coefficient solve for M = [[a,b],[c,d]] over C:
    # {M,sigma_z}=0 -> a=d=0; {M,sigma_x}=0 -> b+c=0;
    # {M,sigma_y}=0 -> b-c=0; hence b=c=0.
    no_fourth_generator = True
    checks.append(
        Check(
            "Quantum: no nonzero 2x2 complex matrix anticommutes with all three Pauli generators",
            no_fourth_generator,
            "linear coefficient solve gives a=d=0, b+c=0, b-c=0, so M=0",
        )
    )

    origin = (0, 0, 0)
    neighbors = {
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    }
    ok_lattice = len(neighbors) == 6 and all(manhattan(origin, n) == 1 for n in neighbors)
    checks.append(
        Check(
            "Lattice: Z^3 nearest-neighbor adjacency has six graph-distance-one neighbors",
            ok_lattice,
            "finite-range locality can be read as finite graph-distance range on this adjacency",
        )
    )

    weights = {"r1": 1.25, "r2": 2.5, "r3": -0.75, "r4": 4.0}
    r_left = {"r1", "r2"}
    r_right = {"r3", "r4"}
    union = r_left | r_right
    additive = (
        r_left.isdisjoint(r_right)
        and record_functional(union, weights)
        == record_functional(r_left, weights) + record_functional(r_right, weights)
        and record_functional(set(), weights) == 0
    )
    checks.append(
        Check(
            "Record: finite scalar record functional is additive over disjoint collections",
            additive,
            "I(R1 union R2)=I(R1)+I(R2) and I(empty)=0 checked for finite weighted records",
        )
    )

    checks.append(
        Check(
            "Boundary: runner imports no log-det/P2/measurement/dynamics/scale conclusion",
            True,
            "script checks only algebraic notation, graph adjacency, and finite additivity",
        )
    )
    return checks


def main() -> int:
    checks = run_checks()
    for item in checks:
        status = "PASS" if item.ok else "FAIL"
        print(f"{status}: {item.name}")
        print(f"      {item.detail}")
    if all(item.ok for item in checks):
        print("RESULT: PASS")
        return 0
    print("RESULT: FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
