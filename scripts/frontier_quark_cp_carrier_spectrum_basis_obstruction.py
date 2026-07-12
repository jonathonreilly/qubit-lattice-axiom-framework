#!/usr/bin/env python3
"""Exact obstruction to promoting the fitted quark CP carrier coordinates.

The historical completion runner optimized diagonal mass labels and two complex
1-3 coordinates against imported comparators.  This deterministic companion
checks the load-bearing negative result:

* nonzero off-diagonal entries prevent the diagonal labels from being the
  singular-value mass spectrum;
* a common weak-basis rotation preserves spectra, CKM invariants, and
  determinants while changing the normalized carrier coordinates; and
* Hermiticity makes each determinant real without fixing the carrier phase.

Historical fitted/comparator values are used only for a replay witness.  The
symbolic obstruction does not depend on them.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
import sympy as sp


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")


def check_close(
    name: str,
    actual: np.ndarray | complex | float,
    expected: np.ndarray | complex | float,
    *,
    atol: float = 1.0e-12,
    rtol: float = 1.0e-12,
) -> None:
    delta = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    check(name, bool(np.allclose(actual, expected, atol=atol, rtol=rtol)), f"max delta={delta:.3e}")


@dataclass(frozen=True)
class SectorWitness:
    name: str
    matrix: np.ndarray
    expected_xi: complex


# Historical non-load-bearing replay constants from the old fit surface.
R_UC_FIT = 1.688494e-3
R_CT_FIT = 7.400356e-3
R_UC_COMPARATOR = 1.696779261586803e-3
R_CT_COMPARATOR = 7.376716694674624e-3

C12_U = 1.48
C23_U = 0.65
C12_D = 0.91
C23_D = 0.65
R_DB = 0.001156472358941232
R_SB = 0.02238973161596408

XI_U_FIT = complex(0.340735, -0.063203)
XI_D_FIT = complex(0.078186, 0.108371)


def build_real_tree_matrix(
    diagonal: tuple[float, float, float],
    c12: float,
    c23: float,
    xi: complex,
) -> np.ndarray:
    a, b, c = diagonal
    c13_base = c12 * c23 * math.sqrt(a / c)
    c13_total = c13_base + xi
    matrix = np.array(
        [
            [a, c12 * math.sqrt(a * b), c13_total * math.sqrt(a * c)],
            [c12 * math.sqrt(a * b), b, c23 * math.sqrt(b * c)],
            [np.conj(c13_total) * math.sqrt(a * c), c23 * math.sqrt(b * c), c],
        ],
        dtype=complex,
    )
    return matrix


def historical_witnesses() -> tuple[SectorWitness, SectorWitness]:
    up_diagonal = (R_UC_FIT * R_CT_FIT, R_CT_FIT, 1.0)
    down_diagonal = (R_DB, R_SB, 1.0)
    return (
        SectorWitness(
            "up",
            build_real_tree_matrix(up_diagonal, C12_U, C23_U, XI_U_FIT),
            XI_U_FIT,
        ),
        SectorWitness(
            "down",
            build_real_tree_matrix(down_diagonal, C12_D, C23_D, XI_D_FIT),
            XI_D_FIT,
        ),
    )


def extract_real_tree_xi(matrix: np.ndarray) -> complex:
    diagonal = np.real(np.diag(matrix))
    if np.min(diagonal) <= 0.0:
        raise ValueError("real-tree normalization requires positive diagonal labels")
    a, b, c = diagonal
    x = float(np.real(matrix[0, 1]))
    y = float(np.real(matrix[1, 2]))
    if abs(np.imag(matrix[0, 1])) > 1.0e-12 or abs(np.imag(matrix[1, 2])) > 1.0e-12:
        raise ValueError("tree edges are not real")
    c12 = x / math.sqrt(a * b)
    c23 = y / math.sqrt(b * c)
    c13_total = matrix[0, 2] / math.sqrt(a * c)
    c13_base = c12 * c23 * math.sqrt(a / c)
    return complex(c13_total - c13_base)


def singular_values(matrix: np.ndarray) -> np.ndarray:
    return np.sort(np.linalg.svd(matrix, compute_uv=False))


def diagonalizer(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    h = matrix @ matrix.conj().T
    eigenvalues, eigenvectors = np.linalg.eigh(h)
    order = np.argsort(eigenvalues)
    return eigenvalues[order], eigenvectors[:, order]


def ckm_observables(up: np.ndarray, down: np.ndarray) -> tuple[np.ndarray, float]:
    _, u_up = diagonalizer(up)
    _, u_down = diagonalizer(down)
    ckm = u_up.conj().T @ u_down
    jarlskog = float(
        np.imag(ckm[0, 1] * ckm[1, 2] * np.conj(ckm[0, 2]) * np.conj(ckm[1, 1]))
    )
    return np.abs(ckm), jarlskog


def rotation_13(theta: float) -> np.ndarray:
    cosine = math.cos(theta)
    sine = math.sin(theta)
    return np.array(
        [[cosine, 0.0, sine], [0.0, 1.0, 0.0], [-sine, 0.0, cosine]],
        dtype=complex,
    )


def part1_symbolic_identities() -> None:
    print("\n" + "=" * 78)
    print("PART 1: Exact spectrum, determinant, and real-tree orbit identities")
    print("=" * 78)

    a, b, c, x, y, p, q = sp.symbols("a b c x y p q", real=True)
    matrix = sp.Matrix(
        [[a, x, p + sp.I * q], [x, b, y], [p - sp.I * q, y, c]]
    )

    expected_frobenius = a**2 + b**2 + c**2 + 2 * (x**2 + y**2 + p**2 + q**2)
    frobenius = sp.expand(sp.trace(matrix * matrix.conjugate().T))
    check(
        "Frobenius/singular-spectrum identity is exact",
        sp.simplify(frobenius - expected_frobenius) == 0,
    )
    check(
        "off-diagonal excess is exactly 2(x^2+y^2+|z|^2)",
        sp.simplify(frobenius - (a**2 + b**2 + c**2) - 2 * (x**2 + y**2 + p**2 + q**2)) == 0,
    )

    expected_determinant = a * b * c - a * y**2 - b * (p**2 + q**2) - c * x**2 + 2 * x * y * p
    determinant = sp.expand(matrix.det())
    check(
        "Hermitian determinant formula is exact",
        sp.simplify(determinant - expected_determinant) == 0,
    )
    check(
        "Hermitian determinant has zero symbolic imaginary part",
        sp.simplify(sp.im(determinant)) == 0,
    )

    theta = sp.symbols("theta", real=True)
    cosine = sp.cos(theta)
    sine = sp.sin(theta)
    rotation = sp.Matrix(
        [[cosine, 0, sine], [0, 1, 0], [-sine, 0, cosine]]
    )
    rotated = sp.simplify(rotation.T * matrix * rotation)
    expected_12 = cosine * x - sine * y
    expected_23 = sine * x + cosine * y
    expected_13 = sine * cosine * (a - c) + sp.cos(2 * theta) * p + sp.I * q
    check(
        "common 1-3 rotation keeps the 1-2 tree edge real with the stated formula",
        sp.trigsimp(rotated[0, 1] - expected_12) == 0,
    )
    check(
        "common 1-3 rotation keeps the 2-3 tree edge real with the stated formula",
        sp.trigsimp(rotated[1, 2] - expected_23) == 0,
    )
    check(
        "common 1-3 rotation changes the 1-3 coordinate by the stated formula",
        sp.trigsimp(rotated[0, 2] - expected_13) == 0,
    )
    derivative_at_zero = sp.simplify(sp.diff(sp.re(rotated[0, 2]), theta).subs(theta, 0))
    check("d Re(M13')/dtheta at zero equals a-c", derivative_at_zero == a - c)


def part2_exact_rational_similarity_control() -> None:
    print("\n" + "=" * 78)
    print("PART 2: Independent exact rational similarity control")
    print("=" * 78)

    matrix = sp.Matrix(
        [
            [sp.Rational(1, 5), sp.Rational(2, 7), sp.Rational(3, 11) + sp.I / 13],
            [sp.Rational(2, 7), sp.Rational(4, 9), sp.Rational(5, 12)],
            [sp.Rational(3, 11) - sp.I / 13, sp.Rational(5, 12), sp.Rational(7, 6)],
        ]
    )
    rotation = sp.Matrix(
        [[sp.Rational(3, 5), 0, sp.Rational(4, 5)], [0, 1, 0], [-sp.Rational(4, 5), 0, sp.Rational(3, 5)]]
    )
    rotated = sp.simplify(rotation.T * matrix * rotation)

    check("rational 1-3 control is exactly orthogonal", rotation.T * rotation == sp.eye(3))
    check("exact similarity preserves determinant", sp.simplify(rotated.det() - matrix.det()) == 0)
    check("exact similarity preserves trace", sp.simplify(sp.trace(rotated) - sp.trace(matrix)) == 0)
    check(
        "exact similarity preserves the characteristic polynomial",
        sp.expand(rotated.charpoly().as_expr() - matrix.charpoly().as_expr()) == 0,
    )
    check(
        "exact similarity preserves tr(M M^dagger)",
        sp.simplify(
            sp.trace(rotated * rotated.conjugate().T)
            - sp.trace(matrix * matrix.conjugate().T)
        )
        == 0,
    )


def part3_historical_spectrum_witness(up: SectorWitness, down: SectorWitness) -> None:
    print("\n" + "=" * 78)
    print("PART 3: Historical fitted point reads diagonal labels, not masses")
    print("=" * 78)

    check_close("up matrix is Hermitian", up.matrix, up.matrix.conj().T)
    check_close("down matrix is Hermitian", down.matrix, down.matrix.conj().T)
    check_close("up normalized coordinate reproduces historical xi_u", extract_real_tree_xi(up.matrix), up.expected_xi)
    check_close(
        "down normalized coordinate reproduces historical xi_d",
        extract_real_tree_xi(down.matrix),
        down.expected_xi,
    )

    # Exact certificate for the decimal point printed in the source note.
    # The characteristic polynomial has algebraic coefficients, but SymPy
    # decides its sign exactly at rational endpoints.  Three disjoint sign-
    # change brackets contain all three real roots because the matrix is
    # Hermitian and the polynomial is cubic.
    r_uc_exact = sp.Rational("0.001688494")
    r_ct_exact = sp.Rational("0.007400356")
    a_exact = r_uc_exact * r_ct_exact
    b_exact = r_ct_exact
    c12_exact = sp.Rational("1.48")
    c23_exact = sp.Rational("0.65")
    xi_re_exact = sp.Rational("0.340735")
    xi_im_exact = sp.Rational("-0.063203")
    x_exact = c12_exact * sp.sqrt(a_exact * b_exact)
    y_exact = c23_exact * sp.sqrt(b_exact)
    z_exact = (
        c12_exact * c23_exact * sp.sqrt(a_exact)
        + xi_re_exact
        + sp.I * xi_im_exact
    ) * sp.sqrt(a_exact)
    exact_matrix = sp.Matrix(
        [
            [a_exact, x_exact, z_exact],
            [x_exact, b_exact, y_exact],
            [sp.conjugate(z_exact), y_exact, 1],
        ]
    )
    characteristic_poly = exact_matrix.charpoly()
    eigenvalue_symbol = characteristic_poly.gen
    characteristic = sp.expand(characteristic_poly.as_expr())
    root_brackets = (
        (sp.Rational(-24, 10**6), sp.Rational(-23, 10**6)),
        (sp.Rational(429, 10**5), sp.Rational(430, 10**5)),
        (sp.Rational(1003, 1000), sp.Rational(1004, 1000)),
    )
    bracket_signs = [
        (
            sp.sign(characteristic.subs(eigenvalue_symbol, lower)),
            sp.sign(characteristic.subs(eigenvalue_symbol, upper)),
        )
        for lower, upper in root_brackets
    ]
    check(
        "exact rational brackets isolate all three Hermitian eigenvalues",
        bracket_signs == [(-1, 1), (1, -1), (-1, 1)],
        f"endpoint signs={bracket_signs}",
    )

    ratio_uc_lower = sp.Rational(23, 10**6) / sp.Rational(430, 10**5)
    ratio_uc_upper = sp.Rational(24, 10**6) / sp.Rational(429, 10**5)
    ratio_ct_lower = sp.Rational(429, 10**5) / sp.Rational(1004, 1000)
    ratio_ct_upper = sp.Rational(430, 10**5) / sp.Rational(1003, 1000)
    comparator_uc_exact = sp.Rational("0.001696779261586803")
    comparator_ct_exact = sp.Rational("0.007376716694674624")
    check(
        "exact sigma_u/sigma_c bracket excludes its imported comparator",
        comparator_uc_exact < ratio_uc_lower < ratio_uc_upper,
        f"bracket=[{float(ratio_uc_lower):.9e},{float(ratio_uc_upper):.9e}]",
    )
    check(
        "exact sigma_c/sigma_t bracket excludes its imported comparator",
        ratio_ct_lower < ratio_ct_upper < comparator_ct_exact,
        f"bracket=[{float(ratio_ct_lower):.9e},{float(ratio_ct_upper):.9e}]",
    )

    up_singular = singular_values(up.matrix)
    down_singular = singular_values(down.matrix)
    up_ratios = np.array([up_singular[0] / up_singular[1], up_singular[1] / up_singular[2]])
    input_ratios = np.array([R_UC_FIT, R_CT_FIT])
    comparator_ratios = np.array([R_UC_COMPARATOR, R_CT_COMPARATOR])

    print(f"\n  up diagonal labels: {np.real(np.diag(up.matrix))}")
    print(f"  up singular values: {up_singular}")
    print(f"  up singular ratios: {up_ratios}")
    print(f"  imported comparators: {comparator_ratios}")
    print(f"  down singular values (context only): {down_singular}")

    trace_excess_up = float(
        np.trace(up.matrix @ up.matrix.conj().T).real
        - np.sum(np.real(np.diag(up.matrix)) ** 2)
    )
    explicit_excess_up = 2.0 * (
        abs(up.matrix[0, 1]) ** 2 + abs(up.matrix[1, 2]) ** 2 + abs(up.matrix[0, 2]) ** 2
    )
    check_close("up numerical trace excess matches exact off-diagonal formula", trace_excess_up, explicit_excess_up)
    check(
        "up singular ratios are not the optimizer's diagonal ratios",
        bool(np.max(np.abs(up_ratios / input_ratios - 1.0)) > 0.4),
    )
    check(
        "up singular ratios miss both imported comparators materially",
        bool(np.min(np.abs(up_ratios / comparator_ratios - 1.0)) > 0.4),
    )


def part4_common_orbit_witness(up: SectorWitness, down: SectorWitness) -> None:
    print("\n" + "=" * 78)
    print("PART 4: Common weak-basis orbit preserves observables and changes xi")
    print("=" * 78)

    theta = 1.0e-3
    rotation = rotation_13(theta)
    up_rotated = rotation.conj().T @ up.matrix @ rotation
    down_rotated = rotation.conj().T @ down.matrix @ rotation

    check_close("numeric common rotation is unitary", rotation.conj().T @ rotation, np.eye(3))
    check_close("rotated up tree edges remain real", np.imag(up_rotated[[0, 1], [1, 2]]), np.zeros(2))
    check_close("rotated down tree edges remain real", np.imag(down_rotated[[0, 1], [1, 2]]), np.zeros(2))
    check_close("up singular spectrum is orbit-invariant", singular_values(up_rotated), singular_values(up.matrix))
    check_close(
        "down singular spectrum is orbit-invariant",
        singular_values(down_rotated),
        singular_values(down.matrix),
    )

    old_moduli, old_j = ckm_observables(up.matrix, down.matrix)
    new_moduli, new_j = ckm_observables(up_rotated, down_rotated)
    check_close("all CKM moduli are orbit-invariant", new_moduli, old_moduli, atol=3.0e-12, rtol=3.0e-12)
    check_close("signed Jarlskog invariant is orbit-invariant", new_j, old_j, atol=3.0e-12, rtol=3.0e-12)
    check_close("up determinant is orbit-invariant", np.linalg.det(up_rotated), np.linalg.det(up.matrix))
    check_close("down determinant is orbit-invariant", np.linalg.det(down_rotated), np.linalg.det(down.matrix))

    old_xi_up = extract_real_tree_xi(up.matrix)
    old_xi_down = extract_real_tree_xi(down.matrix)
    new_xi_up = extract_real_tree_xi(up_rotated)
    new_xi_down = extract_real_tree_xi(down_rotated)
    print(f"\n  theta = {theta:.3e}")
    print(f"  xi_u: {old_xi_up} -> {new_xi_up}")
    print(f"  xi_d: {old_xi_down} -> {new_xi_down}")
    check("xi_u changes on an observable-preserving orbit", abs(new_xi_up - old_xi_up) > 1.0e-2)
    check("xi_d changes on an observable-preserving orbit", abs(new_xi_down - old_xi_down) > 1.0e-3)

    det_up = np.linalg.det(up.matrix)
    det_down = np.linalg.det(down.matrix)
    check(
        "both historical Hermitian sector determinants are real",
        abs(det_up.imag) < 1.0e-18 and abs(det_down.imag) < 1.0e-18,
    )
    check(
        "the historical determinant product is positive by a discrete sign pairing",
        det_up.real < 0.0 and det_down.real < 0.0 and (det_up * det_down).real > 0.0,
    )


def part5_summary() -> None:
    print("\n" + "=" * 78)
    print("PART 5: Honest endpoint")
    print("=" * 78)
    print(
        "\n  Exact no-go: the current diagonal-mass/fitted-xi route cannot be\n"
        "  promoted as a first-principles physical completion.  A positive\n"
        "  reopening needs a singular-spectrum readout and a derived joint\n"
        "  weak-basis/texture selector (or invariant carrier replacement).\n"
        "  No claim is made that every corrected quark-CP completion fails."
    )


def main() -> int:
    print("=" * 78)
    print("QUARK CP CARRIER: EXACT SPECTRUM AND BASIS OBSTRUCTION")
    print("=" * 78)
    up, down = historical_witnesses()
    part1_symbolic_identities()
    part2_exact_rational_similarity_control()
    part3_historical_spectrum_witness(up, down)
    part4_common_orbit_witness(up, down)
    part5_summary()
    print("\n" + "=" * 78)
    print(f"TOTAL PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
