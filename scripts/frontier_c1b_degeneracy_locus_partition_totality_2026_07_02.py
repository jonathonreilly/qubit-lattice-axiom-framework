#!/usr/bin/env python3
"""Exact finite checks for the Block05 C1b degeneracy-locus note."""

from __future__ import annotations

import sys

import sympy as sp


I = sp.I
sqrt = sp.sqrt
pi = sp.pi


def clean(x):
    return sp.simplify(sp.expand(x))


def matrix_zero(M):
    return all(clean(entry) == 0 for entry in M)


def scalar_eq(x, y):
    return clean(x - y) == 0


checks: list[tuple[str, bool]] = []


def check(name: str, condition: bool) -> None:
    checks.append((name, bool(condition)))


a, rho = sp.symbols("a rho", nonzero=True)
omega = sp.Rational(-1, 2) + I * sqrt(3) / 2

U = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
Id = sp.eye(3)
Uinv = U**2
Y0 = a * Id + rho * (U + Uinv)


def f(k: int) -> sp.Matrix:
    return sp.Matrix([1, omega ** (-k), omega ** (-2 * k)]) / sqrt(3)


def proj(v: sp.Matrix) -> sp.Matrix:
    return sp.simplify(v * v.conjugate().T)


P = [proj(f(k)) for k in range(3)]
P0, P1, P2 = P
P12 = sp.simplify(P1 + P2)

g1 = sp.simplify((f(1) + f(2)) / sqrt(2))
g2 = sp.simplify((f(1) - f(2)) / sqrt(2))
Q1 = proj(g1)
Q2 = proj(g2)


# T1: exact residue enumeration for lambda_j = lambda_k.
expected_pairs = {
    0: {(1, 2)},
    1: {(0, 2)},
    2: {(0, 1)},
    3: {(1, 2)},
    4: {(0, 2)},
    5: {(0, 1)},
}

actual_pairs = {}
for m in range(6):
    lambdas = [
        clean(a + 2 * rho * sp.cos(m * pi / 3 + 2 * pi * k / 3))
        for k in range(3)
    ]
    pairs = set()
    for j in range(3):
        for k in range(j + 1, 3):
            if scalar_eq(lambdas[j], lambdas[k]):
                pairs.add((j, k))
    actual_pairs[m] = pairs

check("T1 residue collision pairs match", actual_pairs == expected_pairs)

formula_residues = set()
for j in range(3):
    for k in range(j + 1, 3):
        for n in range(6):
            residue = clean(pi * n - pi * sp.Rational(j + k, 3))
            formula_residues.add(int(clean((residue / (pi / 3)) % 6)))

check("T1 collision formula gives only pi/3 residues", formula_residues == set(range(6)))

check("T1 delta=0 witness lambda1=lambda2", actual_pairs[0] == {(1, 2)})


# Algebra-common Fourier projectors.
for k, Pk in enumerate(P):
    eig = omega**k
    check(f"Fourier projector P{k} idempotent", matrix_zero(Pk * Pk - Pk))
    check(f"Fourier projector P{k} diagonalizes U", matrix_zero(U * Pk - eig * Pk))


# T2: Fourier and rotated fine splits of the degenerate eigenspace.
for name, A in [("P1", P1), ("P2", P2), ("Q1", Q1), ("Q2", Q2)]:
    check(f"T2 {name} idempotent", matrix_zero(A * A - A))
    check(f"T2 {name} commutes with degenerate Y", matrix_zero(Y0 * A - A * Y0))
    check(f"T2 {name} has degenerate eigenvalue", matrix_zero(Y0 * A - (a - rho) * A))

check("T2 Fourier split orthogonal", matrix_zero(P1 * P2))
check("T2 rotated split orthogonal", matrix_zero(Q1 * Q2))
check("T2 rotated split sums to degenerate projector", matrix_zero(Q1 + Q2 - P12))


# T2/T3: per-cell Hilbert-Schmidt content differs while coarse content agrees.
T = P1
TstarT = sp.simplify(T.conjugate().T * T)


def content(E):
    return clean(sp.trace(E * TstarT * E))


fourier_content = (content(P1), content(P2))
rotated_content = (content(Q1), content(Q2))
coarse_content = content(P12)

check("T2 Fourier per-cell content is (1,0)", fourier_content == (sp.Integer(1), sp.Integer(0)))
check(
    "T2 rotated per-cell content is (1/2,1/2)",
    rotated_content == (sp.Rational(1, 2), sp.Rational(1, 2)),
)
check("T2 coarse content is shared total 1", scalar_eq(coarse_content, sum(fourier_content)) and scalar_eq(coarse_content, sum(rotated_content)))
check("T2 fine contents differ across valid splits", fourier_content != rotated_content)


# T3: Y does not select the Fourier split on the locus; U does.
check("T3 rotated Q1 is not Fourier P1", not matrix_zero(Q1 - P1))
check("T3 rotated Q2 is not Fourier P2", not matrix_zero(Q2 - P2))
check("T3 U distinguishes P1 from P2", not matrix_zero(U * P1 - U * P2))
check("T3 Y has same eigenvalue on P1 and P2", matrix_zero(Y0 * P1 - (a - rho) * P1) and matrix_zero(Y0 * P2 - (a - rho) * P2))


pass_count = sum(1 for _, ok in checks if ok)
failures = [name for name, ok in checks if not ok]
fail_count = len(failures)

print("frontier_c1b_degeneracy_locus_partition_totality_2026_07_02")
print(f"PASS checks: {pass_count}; FAIL checks: {fail_count}; first_failure: {failures[0] if failures else 'none'}")
print(f"TOTAL: PASS={pass_count} FAIL={fail_count}")

if fail_count:
    sys.exit(1)
