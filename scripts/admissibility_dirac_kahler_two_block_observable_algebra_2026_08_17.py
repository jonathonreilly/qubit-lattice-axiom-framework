#!/usr/bin/env python3
"""Block 132: exact two-block observable-algebra certificate.

The runner imports the certified Block 119 sector construction and works only
with exact rational and quadratic-root-field arithmetic.  It certifies the
second transfer degeneracy, the per-sector-real Gram gauge and its necessary
quadratic extension, and the full six-dimensional two-block observable
structure.  Wall-clock timing is the sole floating-point quantity.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16 as b119


R = sp.Rational
I = sp.I
RHO = b119.RHO
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_TWO_BLOCK_OBSERVABLE_ALGEBRA_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONJUGATE_PAIR_OBSERVABLE_SPACE_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_conjugate_pair_observable_space_"
    "2026_08_17.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_conjugate_pair_"
    "observable_space_2026_08_17.txt"
)
B119_RUNNER = (
    "scripts/admissibility_dirac_kahler_reflection_intertwiner_completion_"
    "2026_08_16.py"
)
B119_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_reflection_intertwiner_"
    "completion_2026_08_16.txt"
)

# This tuple is deliberately literal: it is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_BLOCK_OBSERVABLE_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONJUGATE_PAIR_OBSERVABLE_SPACE_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_conjugate_pair_observable_space_2026_08_17.py",
    "logs/runner-cache/admissibility_dirac_kahler_conjugate_pair_observable_space_2026_08_17.txt",
    "scripts/admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16.py",
    "logs/runner-cache/admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "02602ca09e4ea69a805a824c3c1f31cb1ee35b20"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block131-conjugate-pair-observable-space-20260817"
)
PARENT_COMMIT = "d3a666f62c87b3b8178289024087090c91ced327"
PARENT_NOTE_BLOB = "84dbb6f3a1490793b18b11bcdb5b7073227d6512"
PARENT_RUNNER_BLOB = "730ac81558f6a9b7d406803566e9a6e435ae5750"
PARENT_CACHE_BLOB = "b00ce7aa207ca5e7b5c8ff94cfc32836b8c36d83"
B119_COMMIT = "33fd2d21558604718f3a88713fe1976aff8f9dbb"
B119_RUNNER_BLOB = "952494a18ba13b7d25fb144b8569687813d9bddc"
B119_CACHE_BLOB = "f7a9b09538c8787ed88885c04cdea3e5cff70104"

ANCESTOR_COMMITS = (
    (130, "db394d1536a8243c2b01b3e45413813e45f8abdd"),
    (129, "30fd2722a10a02f87c235e2ee592d140f8bb7df5"),
    (128, "f6b0cf59e2cc588ebd3e34b96e730574cb485db2"),
    (127, "ca6792464f60598013a3700f99c02a467af64b7a"),
    (126, "a145a4e2cfc19bc919371196d7c5f3451c0bb45d"),
    (125, "ff85cc8c6a991b2926b9ac5cb5168f2587bc0c0d"),
    (124, "da2b9020e9f15ac55640ef87a0798a78e3c9a0d0"),
    (123, "954322e0e085d6c3133ce24dca49db2efbd7d0a6"),
    (122, "f067b99be7eb49fc46ea8dffccab5e20e6052d88"),
    (121, "1714abeefcf3763c0bfe001f30fd14521c538622"),
    (120, "1c2386bf3df420707fd2ecb2d7ec84002ba40ad1"),
    (119, "33fd2d21558604718f3a88713fe1976aff8f9dbb"),
    (118, "fdd1883c54ca8cc14b1337cc1edc249792d5dab2"),
    (117, "f800356aec0989b6e0fa80ed43274794243b1ca2"),
    (116, "c36d11e4e8d927c6fc31f0a8b579d4bd15f4fa43"),
    (115, "c78301fef7521d0518f485f1bf9266983c9e516a"),
    (114, "75026e71cfbd44ed665ddc41c22ebaa722720ea9"),
    (113, "e76893eb7204d1d727a3ab8838fb3fada3f45dfc"),
    (112, "385a6ba5b1594f20e5d4eebba9da68d8e72abc10"),
    (111, "b04e7c8747b09734711cfcd2bfab961bd12e81ad"),
    (110, "d6761278fca9cac617200792473a8f4da3a6cfff"),
    (109, "ad84cfcc857a65285389ba93b47cd7b718589be5"),
    (108, "8afe8dff5ccf531208238af0aaaec1f547d73874"),
    (107, "d41a05e153d4cb77eee125b82fc0b0bd767bf32e"),
    (106, "22d6d90ec2279e5868c9c825149b2a20beea3797"),
    (105, "d06066c2b908aaca0779625d831dfb10620cf34d"),
    (104, "7fe07db6c03fad1191893c942f708c5cb9a54c43"),
    (103, "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"),
)

G02_PINS = {
    R(5, 13): (
        R(
            11895243298682992699172683613451774615271671819816203178568317099619776398210520749184915377127151534024413868507424468656250,
            241659553525405405992244153822553924313190112753243276784966559561703714179067935568657266929625106143222847593242664924686729,
        )
        * RHO
        + R(
            233478378673517694154739807496511501274055200686460510647170083958224634261221249284470645246596670440043572836228403331530479,
            241659553525405405992244153822553924313190112753243276784966559561703714179067935568657266929625106143222847593242664924686729,
        )
    ),
    R(3, 5): (
        R(
            17626683593743898965263651792596489832135686446565698559796568413909978788589352257067871093750,
            102988128792283621394790869911522770367285193821334841511434007076705027913404870126635679512761,
        )
        * RHO
        + R(
            94173613181942802810825072283235524987866073436254123090525109363388591933645653982796417919011,
            102988128792283621394790869911522770367285193821334841511434007076705027913404870126635679512761,
        )
    ),
}

MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_second_degeneracy",
    "break_per_sector_reality",
    "break_g02_value",
    "break_gauge_law",
    "break_field_caveat",
    "claim_field_internal",
    "break_02_classification",
    "break_cross_pair_exclusion",
    "break_center_dimension",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_toe_progress",
    "claim_axiom_amendment",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    return git_output("rev-parse", f"{commit}:{path}")


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = (
        "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    )
    expected_parent = (
        "0" * 40 if mutation == "stale_parent_authority" else PARENT_NOTE_BLOB
    )
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        **{
            f"ancestor_{number}": is_ancestor(commit, "HEAD")
            for number, commit in ANCESTOR_COMMITS
        },
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
        "b119_ancestor": is_ancestor(B119_COMMIT, "HEAD"),
        "b119_runner": commit_blob(B119_COMMIT, B119_RUNNER),
        "b119_cache": commit_blob(B119_COMMIT, B119_CACHE),
        "worktree_b119_runner": worktree_blob(B119_RUNNER),
        "worktree_b119_cache": worktree_blob(B119_CACHE),
    }


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


def commutator(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return (left * right - right * left).applyfunc(sp.expand)


def vector_norm_squared(vector: sp.Matrix, polynomial: sp.Poly) -> sp.Expr:
    return b119.red(
        sum(
            (
                b119.red(b119.star(value, polynomial) * value, polynomial)
                for value in vector
            ),
            sp.Integer(0),
        ),
        polynomial,
    )


def real_imag_equations(matrix: sp.MatrixBase) -> tuple[sp.Expr, ...]:
    equations: list[sp.Expr] = []
    for value in matrix:
        expanded = sp.expand_complex(value)
        for part in (sp.re(expanded), sp.im(expanded)):
            part = sp.expand(part)
            if part != 0:
                equations.append(part)
    return tuple(equations)


def same_row_space(left: sp.Matrix, right: sp.Matrix) -> bool:
    return (
        left.cols == right.cols
        and left.rank() == right.rank()
        and left.col_join(right).rank() == left.rank()
    )


def rational_square(value: sp.Expr) -> bool:
    value = sp.cancel(value)
    if value.is_Rational is not True or value < 0:
        return False
    numerator, denominator = value.as_numer_denom()
    _, numerator_exact = sp.integer_nthroot(int(numerator), 2)
    _, denominator_exact = sp.integer_nthroot(int(denominator), 2)
    return numerator_exact and denominator_exact


def polynomial_tau(polynomial: sp.Poly) -> tuple[sp.Rational, bool]:
    coefficients = polynomial.all_coeffs()
    if len(coefficients) != 3:
        raise AssertionError("the transfer polynomial must be quadratic")
    leading, linear, constant = coefficients
    tau = sp.cancel(-linear / leading)
    reciprocal = sp.cancel(constant / leading) == 1
    if tau.is_Rational is not True:
        raise AssertionError("the normalized transfer trace must be rational")
    return tau, reciprocal


@dataclass(frozen=True)
class CarrierCertificate:
    shear: sp.Rational
    polynomial: sp.Poly
    stable_interval: tuple[int, int]
    tau_zero: sp.Rational
    tau_two: sp.Rational
    reciprocal_polynomials: bool
    tau_equal: bool
    polynomial_shared: bool
    stable_root_shared: bool
    monodromy_shared: bool
    cycle_product_shared: bool
    beta: sp.Expr
    paired_transfer: sp.Matrix
    transfer_scalar: bool
    y_zero_real: bool
    y_two_real: bool
    y_distinct: bool
    y_nonzero: bool
    norm_zero: sp.Expr
    norm_two: sp.Expr
    g: sp.Expr
    g_pin: sp.Expr
    g_pinned: bool
    g_real: bool
    g_nonzero: bool
    g_nonunit: bool
    g_positive: bool
    labels_self_conjugate: bool


def carrier_certificate(
    sectors: tuple[b119.Sector, ...],
) -> CarrierCertificate:
    if len(sectors) != 4:
        raise AssertionError("one fixture must contain four sectors")
    zero, two = sectors[0], sectors[2]
    polynomial = zero.polynomial
    polynomial_shared = polynomial == two.polynomial
    tau_zero, reciprocal_zero = polynomial_tau(polynomial)
    tau_two, reciprocal_two = polynomial_tau(two.polynomial)
    interval_shared = zero.stable_interval == two.stable_interval
    lower, upper = zero.stable_interval
    scale = 10**12
    stable_root_shared = (
        polynomial_shared
        and interval_shared
        and 0 < lower < upper < scale
        and polynomial.count_roots(R(lower, scale), R(upper, scale)) == 1
    )
    beta = b119.red(RHO**2, polynomial)
    paired_transfer = sp.diag(beta, beta)

    y_zero_real = b119.field_equal(
        zero.y,
        b119.field_conjugate(zero.y, polynomial),
        polynomial,
    )
    y_two_real = polynomial_shared and b119.field_equal(
        two.y,
        b119.field_conjugate(two.y, polynomial),
        polynomial,
    )
    y_distinct = polynomial_shared and not b119.field_equal(
        zero.y, two.y, polynomial
    )
    y_nonzero = (
        b119.red(zero.y[0] - 1, polynomial) == 0
        and b119.red(two.y[0] - 1, polynomial) == 0
    )

    norm_zero = vector_norm_squared(zero.y, polynomial)
    norm_two = vector_norm_squared(two.y, polynomial)
    if norm_zero == 0 or norm_two == 0:
        raise AssertionError("the per-sector-real carrier norms must be nonzero")
    g = b119.red(norm_two / norm_zero, polynomial)
    if zero.shear not in G02_PINS:
        raise AssertionError("the fixture has no exact g_02 pin")
    g_pin = G02_PINS[zero.shear]
    g_polynomial = sp.Poly(g, RHO)
    if g_polynomial.degree() > 1:
        raise AssertionError("g_02 must be affine in the quadratic root")
    slope = g_polynomial.coeff_monomial(RHO)
    intercept = g_polynomial.coeff_monomial(1)
    endpoint_values = tuple(
        sp.cancel(slope * endpoint + intercept)
        for endpoint in (R(lower, scale), R(upper, scale))
    )

    return CarrierCertificate(
        zero.shear,
        polynomial,
        zero.stable_interval,
        tau_zero,
        tau_two,
        reciprocal_zero and reciprocal_two,
        tau_zero == tau_two,
        polynomial_shared,
        stable_root_shared,
        zero.transfer.monodromy == two.transfer.monodromy,
        zero.transfer.cycle_product == two.transfer.cycle_product,
        beta,
        paired_transfer,
        matrix_zero(paired_transfer - beta * sp.eye(2)),
        y_zero_real,
        y_two_real,
        y_distinct,
        y_nonzero,
        norm_zero,
        norm_two,
        g,
        g_pin,
        b119.red(g - g_pin, polynomial) == 0,
        b119.red(b119.star(g, polynomial) - g, polynomial) == 0,
        g != 0,
        b119.red(g - 1, polynomial) != 0,
        all(value > 0 for value in endpoint_values),
        (-zero.momentum) % 4 == zero.momentum
        and (-two.momentum) % 4 == two.momentum,
    )


@dataclass(frozen=True)
class GaugeCertificate:
    shear: sp.Rational
    scale_reality_residual: sp.Expr
    real_scale_forced: bool
    transformed_g: sp.Expr
    transformation_law: bool
    extension_normalization: bool


def gauge_certificate(carrier: CarrierCertificate) -> GaugeCertificate:
    a_real, a_imag = sp.symbols("a_r a_i", real=True)
    symbolic_scale = a_real + I * a_imag
    # Each actual vector has the nonzero real pivot y_k[0]=1.  Therefore
    # preserving entrywise reality already forces the imaginary part of its
    # scalar multiplier to vanish at that pivot.
    reality_residual = sp.expand(
        sp.conjugate(symbolic_scale) - symbolic_scale
    )
    forced_solutions = sp.solve(reality_residual, a_imag)

    a_zero, a_two = sp.symbols("a_0 a_2", real=True, nonzero=True)
    transformed_g = sp.cancel(
        (a_two**2 * carrier.norm_two) / (a_zero**2 * carrier.norm_zero)
    )
    expected_law = sp.cancel((a_two / a_zero) ** 2 * carrier.g)
    scale_free_residual = sp.cancel(
        transformed_g / (a_two / a_zero) ** 2 - carrier.g
    )
    positive_g = sp.Symbol("g_positive", positive=True)
    generic_law = (a_two / a_zero) ** 2 * positive_g
    extension_normalization = sp.simplify(
        generic_law.subs(a_two, a_zero / sp.sqrt(positive_g)) - 1
    ) == 0
    return GaugeCertificate(
        carrier.shear,
        reality_residual,
        reality_residual == -2 * I * a_imag
        and forced_solutions == [sp.Integer(0)],
        transformed_g,
        b119.red(scale_free_residual, carrier.polynomial) == 0
        and sp.cancel(
            transformed_g - expected_law
            - (a_two / a_zero) ** 2 * scale_free_residual
        )
        == 0,
        extension_normalization,
    )


@dataclass(frozen=True)
class FieldCaveatCertificate:
    shear: sp.Rational
    tau: sp.Rational
    g_intercept: sp.Rational
    g_slope: sp.Rational
    root_discriminant: sp.Rational
    root_field_quadratic: bool
    quadratic_system_exact: bool
    u_polynomial: sp.Expr
    u_discriminant: sp.Rational
    discriminant_identity: bool
    discriminant_rational_square: bool
    no_rational_solution: bool
    sqrt_not_in_field: bool


def field_caveat_certificate(
    carrier: CarrierCertificate,
) -> FieldCaveatCertificate:
    g_polynomial = sp.Poly(carrier.g, RHO)
    a = g_polynomial.coeff_monomial(1)
    b = g_polynomial.coeff_monomial(RHO)
    if a.is_Rational is not True or b.is_Rational is not True:
        raise AssertionError("the affine g_02 coefficients must be rational")

    tau = carrier.tau_zero
    root_discriminant = sp.cancel(tau**2 - 4)
    root_field_quadratic = (
        root_discriminant > 0 and not rational_square(root_discriminant)
    )
    c, d = sp.symbols("c d")
    reduced_square = sp.expand(
        c**2 - d**2 - a + (2 * c * d + tau * d**2 - b) * RHO
    )
    reduced_polynomial = sp.Poly(reduced_square, RHO)
    root_relation_exact = (
        b119.red(RHO**2 - tau * RHO + 1, carrier.polynomial) == 0
    )
    quadratic_system_exact = (
        root_relation_exact
        and sp.expand(reduced_polynomial.coeff_monomial(1))
        == sp.expand(c**2 - d**2 - a)
        and sp.expand(reduced_polynomial.coeff_monomial(RHO))
        == sp.expand(2 * c * d + tau * d**2 - b)
    )

    # Put u=d^2.  Eliminating c from
    #   c^2-d^2=a, 2cd+tau*d^2=b
    # gives exactly the checker-prescribed rational quadratic below.
    u = sp.Symbol("u")
    u_polynomial = sp.expand(
        u**2 * (tau**2 - 4) - u * (2 * b * tau + 4 * a) + b**2
    )
    u_coefficients = sp.Poly(u_polynomial, u).all_coeffs()
    u_discriminant = sp.cancel(
        u_coefficients[1] ** 2
        - 4 * u_coefficients[0] * u_coefficients[2]
    )
    expected_discriminant = sp.cancel(16 * (a**2 + a * b * tau + b**2))
    discriminant_identity = u_discriminant == expected_discriminant
    discriminant_rational_square = rational_square(u_discriminant)
    no_rational_solution = (
        quadratic_system_exact
        and sp.Poly(u_polynomial, u).degree() == 2
        and u_discriminant.is_Rational is True
        and not discriminant_rational_square
    )
    return FieldCaveatCertificate(
        carrier.shear,
        tau,
        a,
        b,
        root_discriminant,
        root_field_quadratic,
        quadratic_system_exact,
        u_polynomial,
        u_discriminant,
        discriminant_identity,
        discriminant_rational_square,
        no_rational_solution,
        root_field_quadratic and no_rational_solution,
    )


@dataclass(frozen=True)
class ObservableCertificate:
    symbolic_gram: sp.Matrix
    reality_matrix: sp.Matrix
    reality_rank: int
    adjoint_rank: int
    combined_rank: int
    solution_dimension: int
    condition_set_exact: bool
    generic_basis: tuple[sp.Matrix, ...]
    basis_rank: int
    basis_satisfies_conditions: bool
    gauge_matrix: sp.Matrix
    normalized_gram: sp.Matrix
    normalized_reality: sp.Matrix
    involutivity_preserved: bool
    positivity_preserved: bool
    normalized_basis_symmetric: bool
    collapse_gate_exact: bool
    classification_field_independent: bool
    jordan_closed: bool
    witness_commutator: sp.Matrix
    noncommuting: bool


def observable_space_certificate() -> ObservableCertificate:
    ar, ai, br, bi, cr, ci, dr, di = sp.symbols(
        "a_r a_i b_r b_i c_r c_i d_r d_i", real=True
    )
    variables = (ar, ai, br, bi, cr, ci, dr, di)
    matrix = sp.Matrix(
        (
            (ar + I * ai, br + I * bi),
            (cr + I * ci, dr + I * di),
        )
    )
    g = sp.Symbol("g", positive=True)
    gram = sp.diag(1, g)
    reality = sp.eye(2)
    reality_residual = matrix - reality * matrix.conjugate() * reality
    adjoint_residual = matrix.H * gram - gram * matrix
    reality_equations = real_imag_equations(reality_residual)
    adjoint_equations = real_imag_equations(adjoint_residual)
    reality_coefficients, _ = sp.linear_eq_to_matrix(
        reality_equations, variables
    )
    adjoint_coefficients, _ = sp.linear_eq_to_matrix(
        adjoint_equations, variables
    )
    combined = reality_coefficients.col_join(adjoint_coefficients)
    expected_equations = (ai, bi, ci, di, br - g * cr)
    expected_coefficients, _ = sp.linear_eq_to_matrix(
        expected_equations, variables
    )
    condition_set_exact = (
        combined.rank() == expected_coefficients.rank() == 5
        and same_row_space(combined, expected_coefficients)
    )

    generic_basis = (
        sp.Matrix(((1, 0), (0, 0))),
        sp.Matrix(((0, 0), (0, 1))),
        sp.Matrix(((0, g), (1, 0))),
    )
    basis_columns = tuple(sp.Matrix(tuple(item)) for item in generic_basis)
    basis_rank = sp.Matrix.hstack(*basis_columns).rank()
    basis_satisfies = all(
        matrix_zero(item - item.conjugate())
        and matrix_zero(item.H * gram - gram * item)
        for item in generic_basis
    )

    # The real extension scale sends new coordinates to the old basis.
    # Its conjugation congruence preserves positivity and leaves J=K
    # involutive, while the Gram and the adjoint condition collapse to g=1.
    gauge_matrix = sp.diag(1, 1 / sp.sqrt(g))
    normalized_gram = (gauge_matrix.T * gram * gauge_matrix).applyfunc(
        sp.simplify
    )
    normalized_reality = (
        gauge_matrix.inv() * reality * gauge_matrix.conjugate()
    ).applyfunc(sp.simplify)
    normalized_basis = tuple(
        (gauge_matrix.inv() * item * gauge_matrix).applyfunc(sp.simplify)
        for item in generic_basis
    )
    normalized_basis_symmetric = all(
        matrix_zero(item - item.T) and matrix_zero(item - item.conjugate())
        for item in normalized_basis
    )
    collapsed_basis = tuple(item.subs(g, 1) for item in generic_basis)
    expected_collapsed_basis = (
        sp.Matrix(((1, 0), (0, 0))),
        sp.Matrix(((0, 0), (0, 1))),
        sp.Matrix(((0, 1), (1, 0))),
    )
    collapse_gate_exact = (
        gram.subs(g, 1) == sp.eye(2)
        and collapsed_basis == expected_collapsed_basis
    )
    involutivity_preserved = (
        matrix_zero(normalized_reality - sp.eye(2))
        and matrix_zero(
            normalized_reality * normalized_reality.conjugate() - sp.eye(2)
        )
    )
    positivity_preserved = matrix_zero(normalized_gram - sp.eye(2))
    classification_field_independent = (
        condition_set_exact
        and len(variables) - combined.rank() == 3
        and basis_rank == 3
        and basis_satisfies
        and normalized_basis_symmetric
        and collapse_gate_exact
        and involutivity_preserved
        and positivity_preserved
    )

    p, q, r, s, t, u = sp.symbols("p q r s t u", real=True)
    left = sp.Matrix(((p, g * q), (q, r)))
    right = sp.Matrix(((s, g * t), (t, u)))
    jordan = ((left * right + right * left) / 2).applyfunc(sp.expand)
    jordan_closed = (
        matrix_zero(jordan - jordan.conjugate())
        and matrix_zero(jordan.H * gram - gram * jordan)
    )
    sigma_x = sp.Matrix(((0, 1), (1, 0)))
    sigma_z = sp.Matrix(((1, 0), (0, -1)))
    witness_commutator = commutator(sigma_x, sigma_z)
    noncommuting = (
        witness_commutator == sp.Matrix(((0, -2), (2, 0)))
        and not matrix_zero(witness_commutator)
    )
    return ObservableCertificate(
        gram,
        reality,
        reality_coefficients.rank(),
        adjoint_coefficients.rank(),
        combined.rank(),
        len(variables) - combined.rank(),
        condition_set_exact,
        generic_basis,
        basis_rank,
        basis_satisfies,
        gauge_matrix,
        normalized_gram,
        normalized_reality,
        involutivity_preserved,
        positivity_preserved,
        normalized_basis_symmetric,
        collapse_gate_exact,
        classification_field_independent,
        jordan_closed,
        witness_commutator,
        noncommuting,
    )


def intervals_disjoint(
    left: tuple[int, int], right: tuple[int, int]
) -> bool:
    return left[1] <= right[0] or right[1] <= left[0]


@dataclass(frozen=True)
class FixtureSplitCertificate:
    shear: sp.Rational
    tau_even: sp.Rational
    tau_odd: sp.Rational
    tau_split: bool
    intervals_disjoint: bool
    roots_positive: bool
    rate_split: bool
    one_three_polynomial_shared: bool
    one_three_root_shared: bool
    one_three_y_conjugate: bool
    one_three_g: sp.Expr
    one_three_g_one: bool


def fixture_split_certificate(
    sectors: tuple[b119.Sector, ...],
) -> FixtureSplitCertificate:
    zero, one, _, three = sectors
    tau_even, even_reciprocal = polynomial_tau(zero.polynomial)
    tau_odd, odd_reciprocal = polynomial_tau(one.polynomial)
    disjoint = intervals_disjoint(zero.stable_interval, one.stable_interval)
    roots_positive = (
        zero.stable_interval[0] > 0 and one.stable_interval[0] > 0
    )
    one_three_shared = one.polynomial == three.polynomial
    one_three_interval_shared = one.stable_interval == three.stable_interval
    lower, upper = one.stable_interval
    scale = 10**12
    one_three_root_shared = (
        one_three_shared
        and one_three_interval_shared
        and 0 < lower < upper < scale
        and one.polynomial.count_roots(R(lower, scale), R(upper, scale)) == 1
    )
    one_three_y_conjugate = one_three_shared and all(
        b119.red(
            three.y[index] - b119.star(one.y[index], one.polynomial),
            one.polynomial,
        )
        == 0
        for index in range(one.y.rows)
    )
    norm_one = vector_norm_squared(one.y, one.polynomial)
    norm_three = vector_norm_squared(three.y, one.polynomial)
    if norm_one == 0 or norm_three == 0:
        raise AssertionError("the conjugate-pair norms must be nonzero")
    g_one_three = b119.red(norm_three / norm_one, one.polynomial)
    tau_split = tau_even != tau_odd
    return FixtureSplitCertificate(
        zero.shear,
        tau_even,
        tau_odd,
        tau_split,
        disjoint,
        roots_positive,
        even_reciprocal
        and odd_reciprocal
        and tau_split
        and disjoint
        and roots_positive,
        one_three_shared,
        one_three_root_shared,
        one_three_y_conjugate,
        g_one_three,
        b119.red(g_one_three - 1, one.polynomial) == 0,
    )


@dataclass(frozen=True)
class CombinedCertificate:
    reality_exchange: sp.Matrix
    transfer_pattern: sp.Matrix
    coefficient_rank: int
    solution_dimension: int
    basis: tuple[sp.Matrix, ...]
    basis_rank: int
    basis_satisfies_conditions: bool
    structure_exact: bool
    pair_scalar_projectors: tuple[sp.Matrix, sp.Matrix]
    center_rank: int
    center_dimension: int
    scalar_center_exact: bool
    transfer_commutators_zero: bool
    cross_pair_blocks_commute: bool
    cross_pair_coefficients_nonzero: bool
    cross_pair_conjugation: sp.Matrix
    cross_pair_factor: sp.Expr
    cross_pair_law_exact: bool
    momentum_zero_two: sp.Matrix
    momentum_one_three: sp.Matrix
    zero_two_mixer_commutator: sp.Matrix
    one_three_mixer_commutator: sp.Matrix
    mixer_commutators_exact: bool
    nonvacuous_charge_indices: tuple[int, ...]
    both_blocks_noncommuting: bool


def combined_space_certificate() -> CombinedCertificate:
    real_parts = sp.symbols("r0:16", real=True)
    imag_parts = sp.symbols("q0:16", real=True)
    variables = real_parts + imag_parts
    generic = sp.Matrix(
        4,
        4,
        lambda row, column: real_parts[4 * row + column]
        + I * imag_parts[4 * row + column],
    )
    exchange = sp.Matrix(
        (
            (1, 0, 0, 0),
            (0, 0, 0, 1),
            (0, 0, 1, 0),
            (0, 1, 0, 0),
        )
    )
    beta_base = sp.Symbol("beta_base", real=True)
    beta_gap = sp.Symbol("beta_gap", real=True, nonzero=True)
    transfer = sp.diag(
        beta_base,
        beta_base + beta_gap,
        beta_base,
        beta_base + beta_gap,
    )
    transfer_residual = commutator(generic, transfer)
    equations = (
        real_imag_equations(generic - exchange * generic.conjugate() * exchange)
        + real_imag_equations(generic.H - generic)
        + real_imag_equations(transfer_residual)
    )
    coefficients, _ = sp.linear_eq_to_matrix(equations, variables)

    def unit(row: int, column: int, value: sp.Expr = sp.Integer(1)) -> sp.Matrix:
        result = sp.zeros(4)
        result[row, column] = value
        return result

    e00 = unit(0, 0)
    e22 = unit(2, 2)
    x02 = unit(0, 2) + unit(2, 0)
    identity13 = unit(1, 1) + unit(3, 3)
    x13 = unit(1, 3) + unit(3, 1)
    y13 = I * unit(1, 3) - I * unit(3, 1)
    basis = (e00, e22, x02, identity13, x13, y13)
    basis_columns = tuple(
        sp.Matrix(
            tuple(sp.re(value) for value in item)
            + tuple(sp.im(value) for value in item)
        )
        for item in basis
    )
    basis_rank = sp.Matrix.hstack(*basis_columns).rank()
    basis_satisfies = all(
        matrix_zero(item - exchange * item.conjugate() * exchange)
        and matrix_zero(item.H - item)
        and matrix_zero(commutator(item, transfer))
        for item in basis
    )
    solution_dimension = len(variables) - coefficients.rank()
    structure_exact = (
        coefficients.rank() == 26
        and solution_dimension == 6
        and basis_rank == 6
        and basis_satisfies
    )

    # Compute the center inside the six-dimensional observable space rather
    # than merely exhibiting two central projectors.
    center_variables = sp.symbols("c0:6", real=True)
    general_observable = sum(
        (
            coefficient * item
            for coefficient, item in zip(center_variables, basis)
        ),
        sp.zeros(4),
    )
    center_equations: tuple[sp.Expr, ...] = ()
    for item in basis:
        center_equations += real_imag_equations(
            commutator(general_observable, item)
        )
    center_coefficients, _ = sp.linear_eq_to_matrix(
        center_equations, center_variables
    )
    expected_center_equations = (
        center_variables[0] - center_variables[1],
        center_variables[2],
        center_variables[4],
        center_variables[5],
    )
    expected_center_coefficients, _ = sp.linear_eq_to_matrix(
        expected_center_equations, center_variables
    )
    center_rank = center_coefficients.rank()
    center_dimension = len(center_variables) - center_rank
    scalar_center_exact = (
        center_rank == expected_center_coefficients.rank() == 4
        and center_dimension == 2
        and same_row_space(center_coefficients, expected_center_coefficients)
    )

    projector02 = e00 + e22
    projector13 = identity13
    zero_two_basis = basis[:3]
    one_three_basis = basis[3:]
    cross_pair_blocks_commute = all(
        matrix_zero(commutator(left, right))
        for left in zero_two_basis
        for right in one_three_basis
    )
    even_indices = {0, 2}
    odd_indices = {1, 3}
    cross_positions = tuple(
        (row, column)
        for row in range(4)
        for column in range(4)
        if (row in even_indices and column in odd_indices)
        or (row in odd_indices and column in even_indices)
    )
    expected_transfer_residual = sp.Matrix(
        4,
        4,
        lambda row, column: sp.expand(
            (transfer[column, column] - transfer[row, row])
            * generic[row, column]
        ),
    )
    cross_pair_coefficients_nonzero = (
        beta_gap.is_nonzero is True
        and matrix_zero(transfer_residual - expected_transfer_residual)
        and all(
            sp.simplify(
                (transfer[column, column] - transfer[row, row]) / beta_gap
            )
            in (-1, 1)
            for row, column in cross_positions
        )
    )

    rho_even, rho_odd = sp.symbols(
        "rho_even rho_odd", positive=True, nonzero=True
    )
    two_rate_transfer = sp.diag(rho_even**2, rho_odd**2)
    cross_map = sp.Matrix(((0, 1), (0, 0)))
    cross_pair_conjugation = (
        two_rate_transfer * cross_map * two_rate_transfer.inv()
    ).applyfunc(sp.cancel)
    cross_pair_factor = sp.cancel((rho_even / rho_odd) ** 2)
    cross_pair_law_exact = matrix_zero(
        cross_pair_conjugation - cross_pair_factor * cross_map
    )

    sigma_x = sp.Matrix(((0, 1), (1, 0)))
    momentum02 = sp.diag(0, 2)
    momentum13 = sp.diag(1, 3)
    commutator02 = commutator(sigma_x, momentum02)
    commutator13 = commutator(sigma_x, momentum13)
    expected_mixer_commutator = sp.Matrix(((0, 2), (-2, 0)))
    mixer_commutators_exact = (
        commutator02 == expected_mixer_commutator
        and commutator13 == expected_mixer_commutator
        and not matrix_zero(commutator02)
        and not matrix_zero(commutator13)
    )
    momentum_full = sp.diag(0, 1, 2, 3)
    charge_commutators = tuple(
        commutator(item, momentum_full) for item in basis
    )
    nonvacuous_charge_indices = tuple(
        index
        for index, value in enumerate(charge_commutators)
        if not matrix_zero(value)
    )
    zero_two_internal = commutator(x02, e00 - e22)
    one_three_internal = commutator(x13, y13)
    return CombinedCertificate(
        exchange,
        transfer,
        coefficients.rank(),
        solution_dimension,
        basis,
        basis_rank,
        basis_satisfies,
        structure_exact,
        (projector02, projector13),
        center_rank,
        center_dimension,
        scalar_center_exact,
        all(matrix_zero(commutator(item, transfer)) for item in basis),
        cross_pair_blocks_commute,
        cross_pair_coefficients_nonzero,
        cross_pair_conjugation,
        cross_pair_factor,
        cross_pair_law_exact,
        momentum02,
        momentum13,
        commutator02,
        commutator13,
        mixer_commutators_exact,
        nonvacuous_charge_indices,
        not matrix_zero(zero_two_internal)
        and not matrix_zero(one_three_internal),
    )


N5_LINES = (
    "N5: per_element: exact second-degeneracy, per-sector-reality, gauge-law, field-caveat, classification, and cross-pair-exclusion certificates are checked",
    "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus",
    "per_mode: both momentum pairs are degenerate with scalar transfers — the conjugate-coupled pair has invariant unit gram and the per-sector-real pair has gauge gram normalizable in a quadratic extension",
    "per_block: the complete admissible observable structure is the six-dimensional two-block symmetric algebra with two-dimensional center, cross-pair blocks excluded by the even-odd rate split, and momentum commutators nonzero exactly on pair mixers",
    "lattice_wide: checked and not executed — states and dynamics on the two-block algebra, the flip work order, the common nilpotent differential, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient beyond the displayed carrier, Records, audit retention, and TOE closure remain open",
)


SCOPE_KEYS = (
    "two_block",
    "per_sector_real",
    "gauge_invariant",
    "two_regimes",
    "field_caveat",
    "field_independent",
    "dimension_six",
    "center_dimension",
    "cross_pair_excluded",
    "pair_mixing",
    "os_boundary",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity_quotient",
    "adm",
    "n1_n8",
    "w1",
    "n5_resolution",
    "n5_verbatim",
)


def scope_certificate(note: str, mutation: str) -> dict[str, bool]:
    result = {
        "two_block": "two-block" in note or "two block" in note,
        "per_sector_real": (
            "individually real" in note or "per-sector real" in note
        ),
        "gauge_invariant": "gauge" in note and "invariant" in note,
        "two_regimes": (
            "one mechanism" in note or "two regimes" in note
        ),
        "field_caveat": (
            ("sqrt" in note and "extension" in note)
            or "not a perfect square" in note
            or "quadratic extension" in note
        ),
        "field_independent": "field-independent" in note,
        "dimension_six": (
            "dimension 6" in note or "six-dimensional" in note
        ),
        "center_dimension": (
            "center" in note
            and (
                "dimension 2" in note
                or "two-dimensional center" in note
            )
        ),
        "cross_pair_excluded": (
            "cross-pair" in note and "excluded" in note
        ),
        "pair_mixing": (
            "pair-mixing" in note or "does not conserve momentum" in note
        ),
        "os_boundary": (
            "not an os no-go" in note or "not a curved os no-go" in note
        ),
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "gravity_quotient": (
            "gravity constraint quotient remains unexecuted" in note
        ),
        "adm": "actual adm/history transporter remains" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "w1": "w1" in note,
        "n5_resolution": all(
            f"{resolution}:" in note
            for resolution in (
                "per_element",
                "per_site",
                "per_mode",
                "per_block",
                "lattice_wide",
            )
        ),
        "n5_verbatim": all(
            " ".join(line.lower().split()) in note for line in N5_LINES
        ),
    }
    if mutation == "weaken_no_go_packet":
        result["os_boundary"] = False
        result["n1_n8"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
        result["n5_verbatim"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_axiom_amendment":
        result["axiom"] = False
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started = time.monotonic()
    checks = Checks()

    authority = authority_certificate(mutation)
    authority_raw = (
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_BLOCK_OBSERVABLE_ALGEBRA_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CONJUGATE_PAIR_OBSERVABLE_SPACE_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "scripts/admissibility_dirac_kahler_conjugate_pair_observable_space_2026_08_17.py",
            "logs/runner-cache/admissibility_dirac_kahler_conjugate_pair_observable_space_2026_08_17.txt",
            "scripts/admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16.py",
            "logs/runner-cache/admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16.txt",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(
            authority[f"ancestor_{number}"]
            for number in range(103, 131)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB
        and authority["b119_ancestor"]
        and authority["b119_runner"] == B119_RUNNER_BLOB
        and authority["b119_cache"] == B119_CACHE_BLOB
        and authority["worktree_b119_runner"] == B119_RUNNER_BLOB
        and authority["worktree_b119_cache"] == B119_CACHE_BLOB
    )
    checks.check(
        "A-authority",
        "Block 131 blobs, ancestors 130--103, and landed Block 119 runner/cache are pinned",
        authority_raw,
    )

    fixtures = tuple(
        b119.make_sectors(shear)
        for shear in (b119.prior.PRIMARY_SHEAR, b119.prior.SECOND_SHEAR)
    )
    carriers = tuple(carrier_certificate(sectors) for sectors in fixtures)
    degeneracy_raw = all(
        item.reciprocal_polynomials
        and item.tau_equal
        and item.polynomial_shared
        and item.stable_root_shared
        and item.monodromy_shared
        and item.cycle_product_shared
        and item.transfer_scalar
        for item in carriers
    )
    checks.check(
        "B-the-second-degeneracy",
        "tau_0=tau_2, the stable root is shared, and T_02=rho_0^2 I_2 at both fixtures",
        degeneracy_raw and mutation != "break_second_degeneracy",
    )

    reality_raw = all(
        item.y_zero_real
        and item.y_two_real
        and item.y_distinct
        and item.y_nonzero
        for item in carriers
    )
    g_raw = all(
        item.g_pinned
        and b119.red(item.g - item.g_pin, item.polynomial) == 0
        and item.g_real
        and item.g_nonzero
        and item.g_nonunit
        and item.g_positive
        for item in carriers
    )
    reality_gate = reality_raw and g_raw
    if mutation in ("break_per_sector_reality", "break_g02_value"):
        reality_gate = False
    checks.check(
        "C-the-per-sector-reality",
        "y_0 and y_2 are individually real and unequal, with exact pinned positive g_02 at both fixtures",
        reality_gate,
    )

    gauges = tuple(gauge_certificate(item) for item in carriers)
    gauge_raw = all(
        item.labels_self_conjugate for item in carriers
    ) and all(
        item.real_scale_forced
        and item.transformation_law
        and item.extension_normalization
        for item in gauges
    )
    checks.check(
        "D-the-gauge-law",
        "sectorwise reality forces real scales, g'=(a_2/a_0)^2 g_02, and g'=1 is attainable in the extension",
        gauge_raw and mutation != "break_gauge_law",
    )

    fields = tuple(field_caveat_certificate(item) for item in carriers)
    observable = observable_space_certificate()
    field_raw = all(
        item.root_field_quadratic
        and item.quadratic_system_exact
        and item.discriminant_identity
        and not item.discriminant_rational_square
        and item.no_rational_solution
        and item.sqrt_not_in_field
        for item in fields
    ) and (
        observable.collapse_gate_exact
        and observable.involutivity_preserved
        and observable.positivity_preserved
        and observable.classification_field_independent
    )
    field_gate = field_raw
    if mutation in ("break_field_caveat", "claim_field_internal"):
        field_gate = False
    checks.check(
        "E-the-field-caveat",
        "the rational u-discriminant test excludes sqrt(g_02) from Q(rho), while real extension normalization preserves the classification",
        field_gate,
    )

    observable_raw = (
        observable.symbolic_gram == sp.diag(1, sp.Symbol("g", positive=True))
        and observable.reality_matrix == sp.eye(2)
        and observable.reality_rank == 4
        and observable.adjoint_rank == 4
        and observable.combined_rank == 5
        and observable.solution_dimension == 3
        and observable.condition_set_exact
        and observable.basis_rank == 3
        and observable.basis_satisfies_conditions
        and observable.normalized_gram == sp.eye(2)
        and observable.normalized_reality == sp.eye(2)
        and observable.normalized_basis_symmetric
        and observable.collapse_gate_exact
        and observable.classification_field_independent
        and observable.jordan_closed
        and observable.noncommuting
    )
    checks.check(
        "F-the-02-observable-space",
        "after g=1 normalization the per-sector-real adjoint space is exactly Sym_2(R), dimension 3 and non-commuting",
        observable_raw and mutation != "break_02_classification",
    )

    fixture_splits = tuple(
        fixture_split_certificate(sectors) for sectors in fixtures
    )
    combined = combined_space_certificate()
    cross_pair_raw = all(
        item.rate_split
        and item.tau_split
        and item.intervals_disjoint
        and item.roots_positive
        and item.one_three_polynomial_shared
        and item.one_three_root_shared
        and item.one_three_y_conjugate
        and item.one_three_g_one
        for item in fixture_splits
    ) and (
        combined.cross_pair_coefficients_nonzero
        and combined.cross_pair_law_exact
    )
    center_raw = (
        combined.center_rank == 4
        and combined.center_dimension == 2
        and combined.scalar_center_exact
    )
    algebra_raw = (
        combined.coefficient_rank == 26
        and combined.solution_dimension == 6
        and combined.basis_rank == 6
        and combined.basis_satisfies_conditions
        and combined.structure_exact
        and len(combined.pair_scalar_projectors) == 2
        and combined.transfer_commutators_zero
        and combined.cross_pair_blocks_commute
        and cross_pair_raw
        and center_raw
        and combined.mixer_commutators_exact
        and combined.nonvacuous_charge_indices == (2, 4, 5)
        and combined.both_blocks_noncommuting
    )
    if mutation == "break_cross_pair_exclusion":
        algebra_raw = False
    if mutation == "break_center_dimension":
        algebra_raw = False
    checks.check(
        "G-the-two-block-algebra",
        "Sym_2(R)_02 direct-sum Sym_2(R)_13 has dimension 6, scalar center dimension 2, exact rate exclusion, and nonzero mixer commutators",
        algebra_raw,
    )

    scope = scope_certificate(normalized_note(), mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "two regimes, field caveat, six-dimensional center/cross-pair packet, N1--N8/W1/N5, and TOE firewalls are present",
        set(scope) == set(SCOPE_KEYS)
        and all(scope.values())
        and elapsed_before_scope <= 400,
    )

    primary = next(item for item in carriers if item.shear == R(5, 13))
    primary_gauge = next(item for item in gauges if item.shear == R(5, 13))
    print(
        "AUTHORITY: parent="
        f"{authority['parent']}; Block131 blobs=({authority['parent_note']},"
        f"{authority['parent_runner']},{authority['parent_cache']}); "
        f"Block119=({authority['b119_runner']},{authority['b119_cache']})"
    )
    print(
        "FIXTURES: c=(5/13,3/5); tau_0=tau_2 and T_02=rho_0^2 I_2; "
        "y_0,y_2 are individually real, nonzero, and unequal at both"
    )
    print(f"G02 c=5/13: g_02={primary.g} (computed and pinned exactly)")
    print(
        "GAUGE: at y_k[0]=1, conj((a_r+i a_i)y)-"
        f"(a_r+i a_i)y={primary_gauge.scale_reality_residual}, so a_i=0; "
        "g'=(a_2/a_0)^2 g_02 and a_2=a_0/sqrt(g_02) gives g'=1"
    )
    print(
        "FIELD: u^2(tau^2-4)-u(2b tau+4a)+b^2=0 has a rational "
        "nonsquare discriminant at both fixtures; sqrt(g_02) is not in "
        "Q(rho); S=diag(1,1/sqrt(g)) gives G'=I, J'^2=I, positivity, "
        "and a field-independent classification"
    )
    print(
        "OBSERVABLES: normalized (0,2)=Sym_2(R), dimension=3; "
        f"[sigma_x,sigma_z]={observable.witness_commutator.tolist()}"
    )
    print(
        "ALGEBRA: Sym_2(R)_02 direct-sum Sym_2(R)_13, dimension=6, "
        "center dimension=2; T X T^-1=(rho_even/rho_odd)^2 X excludes "
        "cross-pair blocks; [X_02,diag(0,2)]="
        f"{combined.zero_two_mixer_commutator.tolist()}; "
        f"[X_13,diag(1,3)]={combined.one_three_mixer_commutator.tolist()}"
    )
    for line in N5_LINES:
        print(line)
    if checks.failed == 0:
        print(
            "RESULT: the observable picture completes — one mechanism in "
            "two regimes opens both degenerate pairs, the two-block "
            "six-dimensional symmetric algebra is the full admissible "
            "structure, and the only subtlety is an honest quadratic field "
            "extension for the second block's normalized frame"
        )
        print(
            "DECISION_CUT: build states and dynamics on the algebra; hand "
            "the flip work order across; advance the differential"
        )
    else:
        print(
            "RESULT: BLOCKED — at least one exact authority, algebra, field, "
            "scope, mutation, or runtime certificate failed"
        )
        print(
            "DECISION_CUT: repair the failed certificate without weakening "
            "the retained-grade or field-caveat standard"
        )
    print(
        "TOE: zero obligation retirement; no TOE percentage moves; "
        "retained-positive end-to-end theory count remains zero; gravity "
        "constraint quotient remains unexecuted; actual ADM/history "
        "transporter remains open"
    )
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
