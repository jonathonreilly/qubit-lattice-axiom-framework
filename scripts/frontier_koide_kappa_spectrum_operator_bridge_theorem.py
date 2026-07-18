#!/usr/bin/env python3
"""Exact checks for the abstract Hermitian-circulant Fourier invariant.

The companion note is
``docs/KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md``.
This runner has no physical mass, carrier, selector, P1, MRU, or empirical
comparison input.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import sympy as sp


@dataclass
class Score:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        status = "PASS" if condition else "FAIL"
        self.passed += int(condition)
        self.failed += int(not condition)
        suffix = f"  ({detail})" if detail else ""
        print(f"  [{status}] {label}{suffix}")


def matrix_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def matrix_nonzero(matrix: sp.Matrix) -> bool:
    return any(sp.simplify(entry) != 0 for entry in matrix)


def exact_zero(expr: sp.Expr) -> bool:
    return sp.simplify(sp.expand_complex(expr)) == 0


def exact_nonzero(expr: sp.Expr) -> bool:
    return sp.simplify(sp.expand_complex(expr)) != 0


def normal_mode(score: Score) -> None:
    """Roots-of-unity diagonalization in the declared complex DFT basis."""

    print("NORMAL — complex Fourier derivation")
    a, x, y = sp.symbols("a x y", real=True)
    b = x + sp.I * y
    bbar = sp.conjugate(b)
    sqrt3 = sp.sqrt(3)
    omega = -sp.Rational(1, 2) + sp.I * sqrt3 / 2
    identity = sp.eye(3)
    cyclic_shift = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])

    score.check(
        "N1 shift algebra C^3=I and C^dagger=C^2",
        matrix_zero(cyclic_shift**3 - identity)
        and matrix_zero(cyclic_shift.H - cyclic_shift**2),
    )

    h_matrix = a * identity + b * cyclic_shift + bbar * cyclic_shift**2
    score.check(
        "N2 H=aI+bC+conjugate(b)C^2 is Hermitian and circulant",
        matrix_zero(h_matrix - h_matrix.H)
        and matrix_zero(h_matrix * cyclic_shift - cyclic_shift * h_matrix),
    )

    fourier = sp.Matrix.hstack(
        *[
            sp.Matrix([1, omega**k, omega ** (2 * k)]) / sqrt3
            for k in range(3)
        ]
    )
    shift_spectrum = sp.diag(1, omega, omega**2)
    score.check(
        "N3 declared DFT orientation has C f_k=omega^k f_k",
        matrix_zero(fourier.H * fourier - identity)
        and matrix_zero(cyclic_shift * fourier - fourier * shift_spectrum),
    )

    eigenvalues = [
        a + 2 * x,
        a - x - sqrt3 * y,
        a - x + sqrt3 * y,
    ]
    score.check(
        "N4 Fourier basis exactly diagonalizes H",
        matrix_zero(fourier.H * h_matrix * fourier - sp.diag(*eigenvalues)),
    )
    score.check(
        "N5 the three eigenvalues are real",
        all(exact_zero(sp.im(value)) for value in eigenvalues),
        detail=str(eigenvalues),
    )

    a0 = sp.simplify(sum(eigenvalues) / sqrt3)
    z = sp.simplify(
        sum(eigenvalues[k] * omega ** (-k) for k in range(3)) / sqrt3
    )
    z_abs_sq = sp.simplify(sp.re(z) ** 2 + sp.im(z) ** 2)
    radius_sq = x**2 + y**2

    score.check("N6 a_0=sqrt(3)a", exact_zero(a0 - sqrt3 * a), detail=f"a_0={a0}")
    score.check("N7 z=sqrt(3)b with the declared orientation", exact_zero(z - sqrt3 * b))
    score.check("N8 |z|^2=3|b|^2", exact_zero(z_abs_sq - 3 * radius_sq))

    fourier_residual = sp.expand(a0**2 - 2 * z_abs_sq)
    coordinate_residual = sp.expand(a**2 - 2 * radius_sq)
    score.check(
        "N9 global polynomial invariant has exact factor 3",
        exact_zero(fourier_residual - 3 * coordinate_residual),
    )
    score.check(
        "N10 b=0 boundary reduces to 3a^2 and meets the zero locus only at a=0",
        exact_zero(fourier_residual.subs({x: 0, y: 0}) - 3 * a**2)
        and sp.solve(sp.Eq(3 * a**2, 0), a) == [0],
    )

    radius_nonzero = sp.symbols("rho", positive=True)
    kappa = a**2 / radius_nonzero
    score.check(
        "N11 ratio form is equivalent only on the nonzero-denominator domain",
        radius_nonzero.is_nonzero
        and exact_zero((a**2 - 2 * radius_nonzero) / radius_nonzero - (kappa - 2)),
    )

    trace_h3 = sp.expand(sp.trace(h_matrix**3))
    expected_trace_h3 = sp.expand(
        3 * a**3 + 18 * a * radius_sq + 3 * (b**3 + bbar**3)
    )
    score.check(
        "N12 tr(H^3)=3a^3+18a|b|^2+3(b^3+conjugate(b)^3)",
        exact_zero(trace_h3 - expected_trace_h3),
    )


def independent_mode(score: Score) -> None:
    """Direct matrix/characteristic-polynomial and real-DFT reconstruction."""

    print("INDEPENDENT — characteristic polynomial, traces, and real DFT")
    c, u, v = sp.symbols("c u v", real=True)
    t = sp.Symbol("t")
    sqrt3 = sp.sqrt(3)
    rho = u**2 + v**2
    beta = u + sp.I * v
    beta_bar = u - sp.I * v

    # Construct the matrix entry by entry; do not call the normal route or use
    # its C/F tables.
    h_direct = sp.Matrix(
        [
            [c, beta, beta_bar],
            [beta_bar, c, beta],
            [beta, beta_bar, c],
        ]
    )
    characteristic = sp.expand(h_direct.charpoly(t).as_expr())
    expected_characteristic = sp.expand(
        (t - c) ** 3 - 3 * rho * (t - c) - (beta**3 + beta_bar**3)
    )
    score.check(
        "I1 direct characteristic polynomial reconstruction",
        exact_zero(characteristic - expected_characteristic),
    )

    score.check(
        "I2 direct traces tr(H) and tr(H^2)",
        exact_zero(sp.trace(h_direct) - 3 * c)
        and exact_zero(sp.trace(h_direct**2) - (3 * c**2 + 6 * rho)),
    )
    direct_trace_h3 = sp.expand(sp.trace(h_direct**3))
    score.check(
        "I3 direct cubic trace including phase coefficient",
        exact_zero(
            direct_trace_h3
            - (3 * c**3 + 18 * c * rho + 3 * (beta**3 + beta_bar**3))
        ),
    )

    real_roots = sp.Matrix(
        [
            c + 2 * u,
            c - u - sqrt3 * v,
            c - u + sqrt3 * v,
        ]
    )
    root_residues = [
        sp.expand(characteristic.subs(t, root)) for root in real_roots
    ]
    score.check(
        "I4 the three explicit real values are roots of the direct characteristic polynomial",
        all(exact_zero(residue) for residue in root_residues),
    )

    real_dft = sp.Matrix(
        [
            [1 / sqrt3, 1 / sqrt3, 1 / sqrt3],
            [1 / sqrt3, -1 / (2 * sqrt3), -1 / (2 * sqrt3)],
            [0, -sp.Rational(1, 2), sp.Rational(1, 2)],
        ]
    )
    weighted_metric = sp.diag(1, 2, 2)
    score.check(
        "I5 explicit real DFT obeys R^T diag(1,2,2) R=I",
        matrix_zero(real_dft.T * weighted_metric * real_dft - sp.eye(3)),
    )

    real_coordinates = sp.simplify(real_dft * real_roots)
    expected_coordinates = sp.Matrix([sqrt3 * c, sqrt3 * u, sqrt3 * v])
    score.check(
        "I6 explicit real DFT reconstructs (a_0,Re z,Im z)",
        matrix_zero(real_coordinates - expected_coordinates),
        detail=str(real_coordinates.T),
    )

    independent_a0 = real_coordinates[0]
    independent_z_sq = real_coordinates[1] ** 2 + real_coordinates[2] ** 2
    score.check("I7 independent a_0 identity", exact_zero(independent_a0 - sqrt3 * c))
    score.check("I8 independent |z|^2 identity", exact_zero(independent_z_sq - 3 * rho))
    score.check(
        "I9 independent polynomial invariant",
        exact_zero(
            independent_a0**2
            - 2 * independent_z_sq
            - 3 * (c**2 - 2 * rho)
        ),
    )
    score.check(
        "I10 spectral cubic sum equals the direct matrix trace",
        exact_zero(sum(root**3 for root in real_roots) - direct_trace_h3),
    )


def hostile_mode(score: Score) -> None:
    """Require each named load-bearing mutation to be detected exactly."""

    print("HOSTILE — mutation-kill checks")
    a, x, y = sp.symbols("a x y", real=True)
    b = x + sp.I * y
    bbar = x - sp.I * y
    sqrt3 = sp.sqrt(3)
    omega = -sp.Rational(1, 2) + sp.I * sqrt3 / 2
    identity = sp.eye(3)
    cyclic_shift = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    eigenvalues = [
        a + b * omega**k + bbar * omega ** (-k) for k in range(3)
    ]
    correct_z = sp.simplify(
        sum(eigenvalues[k] * omega ** (-k) for k in range(3)) / sqrt3
    )
    radius_sq = x**2 + y**2
    correct_a0 = sp.simplify(sum(eigenvalues) / sqrt3)
    correct_z_sq = sp.simplify(sp.re(correct_z) ** 2 + sp.im(correct_z) ** 2)
    coordinate_residual = a**2 - 2 * radius_sq
    fourier_residual = sp.expand(correct_a0**2 - 2 * correct_z_sq)

    reversed_z = sp.simplify(
        sum(eigenvalues[k] * omega**k for k in range(3)) / sqrt3
    )
    score.check(
        "H1 KILL reversed DFT orientation (it returns conjugate(b), not b)",
        exact_nonzero(reversed_z - sqrt3 * b),
    )

    unnormalized_z = sp.simplify(
        sum(eigenvalues[k] * omega ** (-k) for k in range(3))
    )
    score.check(
        "H2 KILL missing 1/sqrt(3) Fourier normalization",
        exact_nonzero(unnormalized_z - sqrt3 * b),
    )

    missing_conjugation = a * identity + b * cyclic_shift + b * cyclic_shift**2
    score.check(
        "H3 KILL missing conjugation in H",
        matrix_nonzero(missing_conjugation - missing_conjugation.H),
    )

    inverse_shift = cyclic_shift**2
    inverse_h = a * identity + b * inverse_shift + bbar * inverse_shift**2
    inverse_fourier_diagonal = sp.simplify(
        sp.Matrix.hstack(
            *[
                sp.Matrix([1, omega**k, omega ** (2 * k)]) / sqrt3
                for k in range(3)
            ]
        ).H
        * inverse_h
        * sp.Matrix.hstack(
            *[
                sp.Matrix([1, omega**k, omega ** (2 * k)]) / sqrt3
                for k in range(3)
            ]
        )
    )
    inverse_lambdas = [inverse_fourier_diagonal[k, k] for k in range(3)]
    inverse_z = sp.simplify(
        sum(inverse_lambdas[k] * omega ** (-k) for k in range(3)) / sqrt3
    )
    score.check(
        "H4 KILL inverse cyclic shift under the declared DFT orientation",
        exact_nonzero(inverse_z - sqrt3 * b),
    )

    score.check(
        "H5 KILL wrong invariant prefactor 3/2",
        exact_nonzero(
            fourier_residual - sp.Rational(3, 2) * coordinate_residual
        ),
    )
    score.check(
        "H6 KILL wrong modulus factor |z|^2=(3/2)|b|^2",
        exact_nonzero(correct_z_sq - sp.Rational(3, 2) * radius_sq),
    )

    origin = {a: 0, x: 0, y: 0}
    score.check(
        "H7 KILL global kappa-ratio extension using the b=0 origin counterexample",
        exact_zero(fourier_residual.subs(origin))
        and exact_zero(radius_sq.subs(origin)),
        detail="polynomial residual=0 while the proposed ratio denominator=0",
    )

    h_matrix = a * identity + b * cyclic_shift + bbar * cyclic_shift**2
    trace_h3 = sp.expand(sp.trace(h_matrix**3))
    wrong_cubic_coefficient = sp.expand(
        3 * a**3 + 18 * a * radius_sq + (b**3 + bbar**3)
    )
    score.check(
        "H8 KILL cubic phase coefficient 1 in place of 3",
        exact_nonzero(trace_h3 - wrong_cubic_coefficient),
    )
    wrong_a_scaled_cubic = sp.expand(
        3 * a**3 + 18 * a * radius_sq + 3 * a * (b**3 + bbar**3)
    )
    score.check(
        "H9 KILL an a-scaled cubic phase term",
        exact_nonzero(trace_h3 - wrong_a_scaled_cubic),
    )

    missing_conjugate_eigenvalues = [
        a + b * omega**k + b * omega ** (-k) for k in range(3)
    ]
    score.check(
        "H10 KILL missing conjugation in the eigenvalue formula",
        any(exact_nonzero(sp.im(value)) for value in missing_conjugate_eigenvalues),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("all", "normal", "independent", "hostile"),
        default="all",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    modes = {
        "normal": normal_mode,
        "independent": independent_mode,
        "hostile": hostile_mode,
    }
    selected = tuple(modes) if args.mode == "all" else (args.mode,)
    total = Score()
    for mode in selected:
        score = Score()
        modes[mode](score)
        print(f"TOTAL mode={mode} PASS={score.passed} FAIL={score.failed}")
        total.passed += score.passed
        total.failed += score.failed
    if args.mode == "all":
        print(f"TOTAL mode=all PASS={total.passed} FAIL={total.failed}")
    return int(total.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
