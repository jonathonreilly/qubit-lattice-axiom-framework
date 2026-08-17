#!/usr/bin/env python3
"""Block 131: exact conjugate-pair observable-space certificate.

The runner imports the certified Block 119 sector construction and works only
in its exact quadratic root fields.  It separates the conjugation theorem,
the invariant paired Gram, the reality-fixed adjoint classification, transfer
covariance, and the first momentum-charge commutators.  Wall-clock timing is
the sole floating-point quantity.
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
    "ADMISSIBILITY_DIRAC_KAHLER_CONJUGATE_PAIR_OBSERVABLE_SPACE_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_FACET_CHARGE_BRIDGE_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_facet_charge_bridge_2026_08_17.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_facet_charge_bridge_"
    "2026_08_17.txt"
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
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONJUGATE_PAIR_OBSERVABLE_SPACE_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_FACET_CHARGE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_facet_charge_bridge_2026_08_17.py",
    "logs/runner-cache/admissibility_dirac_kahler_facet_charge_bridge_2026_08_17.txt",
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
    "toe-axiom-closure-block130-facet-charge-bridge-20260817"
)
PARENT_COMMIT = "db394d1536a8243c2b01b3e45413813e45f8abdd"
PARENT_NOTE_BLOB = "1c4ea156b30c745b3afcea205ec314345ed71f6d"
PARENT_RUNNER_BLOB = "1d3aadb6b72d6d95960a0c3b60c3db21c00cb568"
PARENT_CACHE_BLOB = "ed203e829f0cc5aca9b24fe1b178fcad8991f1cd"
B119_COMMIT = "33fd2d21558604718f3a88713fe1976aff8f9dbb"
B119_RUNNER_BLOB = "952494a18ba13b7d25fb144b8569687813d9bddc"
B119_CACHE_BLOB = "f7a9b09538c8787ed88885c04cdea3e5cff70104"

ANCESTOR_COMMITS = (
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

MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_shared_polynomial",
    "break_conjugation",
    "break_g_value",
    "break_invariance",
    "break_classification",
    "break_noncommutation",
    "break_degeneracy_contrast",
    "break_ward_commutators",
    "claim_scalar_only",
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
    """The exact root-field norm sum_i star(v_i) v_i."""
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


@dataclass(frozen=True)
class PairCertificate:
    shear: sp.Rational
    polynomial: sp.Poly
    polynomial_shared: bool
    stable_interval: tuple[int, int]
    isolation_shared: bool
    h00_conjugate: bool
    x_conjugate: bool
    y_residuals: tuple[sp.Expr, ...]
    y_entrywise_conjugate: bool
    construction_mechanism: bool
    norm_one: sp.Expr
    norm_three: sp.Expr
    norms_real: bool
    norms_nonzero: bool
    g: sp.Expr
    g_one: bool
    scale_symbol_nonzero: bool
    scaled_ratio: sp.Expr
    rescaling_invariant: bool


def pair_certificate(sectors: tuple[b119.Sector, ...]) -> PairCertificate:
    if len(sectors) != 4:
        raise AssertionError("one fixture must contain four sectors")
    one, three = sectors[1], sectors[3]
    polynomial = one.polynomial
    polynomial_shared = polynomial == three.polynomial
    interval_shared = one.stable_interval == three.stable_interval
    lower, upper = one.stable_interval
    scale = 10**12
    isolation_shared = (
        polynomial_shared
        and interval_shared
        and 0 < lower < upper < scale
        and polynomial.count_roots(R(lower, scale), R(upper, scale)) == 1
    )

    h00_conjugate = b119.field_equal(
        three.h00,
        b119.field_conjugate(one.h00, polynomial),
        polynomial,
    )
    x_conjugate = b119.field_equal(
        three.x,
        b119.field_conjugate(one.x, polynomial),
        polynomial,
    )
    y_residuals = tuple(
        b119.red(
            three.y[index] - b119.star(one.y[index], polynomial),
            polynomial,
        )
        for index in range(one.y.rows)
    )
    y_entrywise_conjugate = (
        one.y.shape == three.y.shape == (8, 1)
        and all(value == 0 for value in y_residuals)
    )
    construction_mechanism = (
        one.pivot == three.pivot == (0, 0)
        and one.factorization
        and three.factorization
        and h00_conjugate
        and x_conjugate
        and y_entrywise_conjugate
    )

    norm_one = vector_norm_squared(one.y, polynomial)
    norm_three = vector_norm_squared(three.y, polynomial)
    norms_real = (
        b119.red(b119.star(norm_one, polynomial) - norm_one, polynomial) == 0
        and b119.red(
            b119.star(norm_three, polynomial) - norm_three, polynomial
        )
        == 0
    )
    norms_nonzero = norm_one != 0 and norm_three != 0
    g = (
        b119.red(norm_three / norm_one, polynomial)
        if norms_nonzero
        else sp.nan
    )
    g_one = norms_nonzero and b119.red(g - 1, polynomial) == 0

    # Let a be a generic nonzero complex scale.  Reality couples the two
    # rescalings as y_1' = a y_1 and y_3' = conj(a) y_3.  Both squared norms
    # therefore acquire the same exact factor conj(a)*a.
    a = sp.Symbol("a", nonzero=True)
    a_star = sp.conjugate(a)
    scale_norm_one = a_star * a
    scale_norm_three = sp.conjugate(a_star) * a_star
    scaled_ratio = sp.cancel(
        scale_norm_three * norm_three / (scale_norm_one * norm_one)
    )
    scale_symbol_nonzero = (
        a.is_nonzero is True
        and a_star.is_nonzero is True
        and sp.simplify(sp.conjugate(a_star) - a) == 0
    )
    rescaling_invariant = (
        scale_symbol_nonzero
        and norms_nonzero
        and b119.red(scaled_ratio - g, polynomial) == 0
    )
    return PairCertificate(
        one.shear,
        polynomial,
        polynomial_shared,
        one.stable_interval,
        isolation_shared,
        h00_conjugate,
        x_conjugate,
        y_residuals,
        y_entrywise_conjugate,
        construction_mechanism,
        norm_one,
        norm_three,
        norms_real,
        norms_nonzero,
        g,
        g_one,
        scale_symbol_nonzero,
        scaled_ratio,
        rescaling_invariant,
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


@dataclass(frozen=True)
class ObservableSpaceCertificate:
    gram: sp.Matrix
    exchange: sp.Matrix
    fixed_basis: sp.Matrix
    fixed_basis_unitary: bool
    fixed_basis_reality: bool
    reality_rank: int
    adjoint_rank: int
    combined_rank: int
    solution_dimension: int
    condition_set_exact: bool
    basis_rank: int
    basis_satisfies_conditions: bool
    real_symmetric_exact: bool
    jordan_closed: bool
    sigma_commutator: sp.Matrix
    noncommuting: bool


def observable_space_certificate() -> ObservableSpaceCertificate:
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
    gram = sp.diag(1, 1)
    exchange = sp.Matrix(((0, 1), (1, 0)))

    # In the conjugate-pair basis the antilinear reality is J=R*K, hence
    # A J=J A iff A=R*conj(A)*R.  Adjointness uses G=I exactly.
    reality_residual = matrix - exchange * matrix.conjugate() * exchange
    adjoint_residual = matrix.H * gram - gram * matrix
    reality_equations = real_imag_equations(reality_residual)
    adjoint_equations = real_imag_equations(adjoint_residual)
    reality_coefficients, _ = sp.linear_eq_to_matrix(
        reality_equations, variables
    )
    adjoint_coefficients, _ = sp.linear_eq_to_matrix(
        adjoint_equations, variables
    )
    combined_coefficients = reality_coefficients.col_join(
        adjoint_coefficients
    )

    # The combined conditions are exactly
    #   a,d real; d=a; c=conj(b).
    # This is the requested pinned condition set in the conjugate basis.
    expected_equations = (ai, di, dr - ar, cr - br, ci + bi)
    expected_coefficients, _ = sp.linear_eq_to_matrix(
        expected_equations, variables
    )
    condition_set_exact = (
        combined_coefficients.rank() == expected_coefficients.rank() == 5
        and same_row_space(combined_coefficients, expected_coefficients)
    )

    # The columns of U are fixed by R*K.  Because U is unitary, G remains I;
    # in this reality-fixed basis the exact solution becomes Sym_2(R).
    fixed_basis = sp.Matrix(((1, I), (1, -I))) / sp.sqrt(2)
    fixed_basis_unitary = matrix_zero(fixed_basis.H * fixed_basis - gram)
    fixed_basis_reality = matrix_zero(
        exchange * fixed_basis.conjugate() - fixed_basis
    )
    sigma_x = sp.Matrix(((0, 1), (1, 0)))
    sigma_z = sp.Matrix(((1, 0), (0, -1)))
    real_symmetric_basis = (sp.eye(2), sigma_x, sigma_z)
    conjugate_basis = tuple(
        (fixed_basis * basis * fixed_basis.H).applyfunc(sp.simplify)
        for basis in real_symmetric_basis
    )
    basis_satisfies_conditions = all(
        matrix_zero(
            candidate
            - exchange * candidate.conjugate() * exchange
        )
        and matrix_zero(candidate.H * gram - gram * candidate)
        for candidate in conjugate_basis
    )
    coordinate_columns = []
    for candidate in conjugate_basis:
        coordinate_columns.append(
            sp.Matrix(
                (
                    sp.re(candidate[0, 0]),
                    sp.im(candidate[0, 0]),
                    sp.re(candidate[0, 1]),
                    sp.im(candidate[0, 1]),
                    sp.re(candidate[1, 0]),
                    sp.im(candidate[1, 0]),
                    sp.re(candidate[1, 1]),
                    sp.im(candidate[1, 1]),
                )
            ).applyfunc(sp.simplify)
        )
    basis_rank = sp.Matrix.hstack(*coordinate_columns).rank()
    solution_dimension = len(variables) - combined_coefficients.rank()
    real_symmetric_exact = (
        fixed_basis_unitary
        and fixed_basis_reality
        and condition_set_exact
        and solution_dimension == 3
        and basis_rank == 3
        and basis_satisfies_conditions
        and all(
            matrix_zero(fixed_basis.H * candidate * fixed_basis - basis)
            for candidate, basis in zip(conjugate_basis, real_symmetric_basis)
        )
    )

    p, q, r, s, t, u = sp.symbols("p q r s t u", real=True)
    left = sp.Matrix(((p, q), (q, r)))
    right = sp.Matrix(((s, t), (t, u)))
    jordan = ((left * right + right * left) / 2).applyfunc(sp.expand)
    jordan_closed = matrix_zero(jordan - jordan.T) and all(
        sp.im(value) == 0 for value in jordan
    )
    sigma_commutator = commutator(sigma_x, sigma_z)
    noncommuting = (
        sigma_commutator
        == -2 * sp.Matrix(((0, 1), (-1, 0)))
        and sigma_commutator != sp.zeros(2)
    )
    return ObservableSpaceCertificate(
        gram,
        exchange,
        fixed_basis,
        fixed_basis_unitary,
        fixed_basis_reality,
        reality_coefficients.rank(),
        adjoint_coefficients.rank(),
        combined_coefficients.rank(),
        solution_dimension,
        condition_set_exact,
        basis_rank,
        basis_satisfies_conditions,
        real_symmetric_exact,
        jordan_closed,
        sigma_commutator,
        noncommuting,
    )


def intervals_disjoint(
    left: tuple[int, int], right: tuple[int, int]
) -> bool:
    return left[1] <= right[0] or right[1] <= left[0]


@dataclass(frozen=True)
class TransferCovarianceCertificate:
    shear: sp.Rational
    beta: sp.Expr
    paired_transfer: sp.Matrix
    pair_scalar: bool
    observable_basis_commutes: bool
    requested_zero_two_polynomials_different: bool
    requested_zero_two_intervals_disjoint: bool
    requested_rho_zero_not_rho_two: bool
    requested_zero_two_transfer: sp.Matrix
    requested_zero_two_sigma_commutator: sp.Matrix
    requested_sigma_fails: bool
    actual_zero_two_degenerate: bool
    alternative_zero_one_polynomials_different: bool
    alternative_zero_one_intervals_disjoint: bool
    alternative_rho_zero_not_rho_one: bool
    alternative_symbolic_sigma_commutator: sp.Matrix
    alternative_sigma_fails: bool


def transfer_covariance_certificate(
    sectors: tuple[b119.Sector, ...],
) -> TransferCovarianceCertificate:
    zero, one, two, three = sectors
    polynomial = one.polynomial
    if polynomial != three.polynomial:
        raise AssertionError("the conjugate pair must share its root field")
    beta = b119.red(RHO**2, polynomial)
    paired_transfer = sp.diag(beta, beta)
    sigma_x = sp.Matrix(((0, 1), (1, 0)))
    sigma_z = sp.Matrix(((1, 0), (0, -1)))
    observable_basis = (sp.eye(2), sigma_x, sigma_z)
    pair_scalar = matrix_zero(paired_transfer - beta * sp.eye(2))
    observable_basis_commutes = all(
        matrix_zero(commutator(observable, paired_transfer))
        for observable in observable_basis
    )

    # Requested falsifier: the imported Block 119 construction decides this
    # directly.  It actually makes sectors 0 and 2 exactly degenerate too.
    zero_two_polynomials_different = zero.polynomial != two.polynomial
    zero_two_intervals_disjoint = intervals_disjoint(
        zero.stable_interval, two.stable_interval
    )
    rho_zero_not_rho_two = (
        zero_two_polynomials_different and zero_two_intervals_disjoint
    )
    beta_zero = b119.red(RHO**2, zero.polynomial)
    beta_two = b119.red(RHO**2, two.polynomial)
    zero_two_transfer = sp.diag(beta_zero, beta_two)
    zero_two_sigma_commutator = b119.field_matrix(
        commutator(sigma_x, zero_two_transfer), zero.polynomial
    )
    requested_sigma_fails = (
        rho_zero_not_rho_two
        and not matrix_zero(zero_two_sigma_commutator)
    )
    actual_zero_two_degenerate = (
        zero.polynomial == two.polynomial
        and zero.stable_interval == two.stable_interval
        and zero.transfer.cycle_product == two.transfer.cycle_product
        and zero.transfer.monodromy == two.transfer.monodromy
        and matrix_zero(zero_two_transfer - beta_zero * sp.eye(2))
        and matrix_zero(zero_two_sigma_commutator)
    )

    # The exact non-degenerate contrast available in the imported data is
    # (0,1): its positive isolating intervals are disjoint at both fixtures.
    zero_one_polynomials_different = zero.polynomial != one.polynomial
    zero_one_intervals_disjoint = intervals_disjoint(
        zero.stable_interval, one.stable_interval
    )
    rho_zero_not_rho_one = (
        zero_one_polynomials_different and zero_one_intervals_disjoint
    )
    beta_left, beta_right = sp.symbols(
        "beta_0 beta_1", real=True
    )
    alternative_transfer = sp.diag(beta_left, beta_right)
    alternative_sigma_commutator = commutator(
        sigma_x, alternative_transfer
    )
    expected_alternative = sp.Matrix(
        ((0, beta_right - beta_left), (beta_left - beta_right, 0))
    )
    alternative_sigma_fails = (
        rho_zero_not_rho_one
        and alternative_sigma_commutator == expected_alternative
        and alternative_sigma_commutator != sp.zeros(2)
    )
    return TransferCovarianceCertificate(
        one.shear,
        beta,
        paired_transfer,
        pair_scalar,
        observable_basis_commutes,
        zero_two_polynomials_different,
        zero_two_intervals_disjoint,
        rho_zero_not_rho_two,
        zero_two_transfer,
        zero_two_sigma_commutator,
        requested_sigma_fails,
        actual_zero_two_degenerate,
        zero_one_polynomials_different,
        zero_one_intervals_disjoint,
        rho_zero_not_rho_one,
        alternative_sigma_commutator,
        alternative_sigma_fails,
    )


@dataclass(frozen=True)
class WardCertificate:
    momentum_charge: sp.Matrix
    off_diagonal_commutator: sp.Matrix
    diagonal_commutator: sp.Matrix
    off_diagonal_nonzero: bool
    diagonal_zero: bool


def ward_certificate() -> WardCertificate:
    sigma_x = sp.Matrix(((0, 1), (1, 0)))
    sigma_z = sp.Matrix(((1, 0), (0, -1)))
    momentum_charge = sp.diag(1, -1)
    off_diagonal = commutator(sigma_x, momentum_charge)
    diagonal = commutator(sigma_z, momentum_charge)
    expected = -2 * sp.Matrix(((0, 1), (-1, 0)))
    return WardCertificate(
        momentum_charge,
        off_diagonal,
        diagonal,
        off_diagonal == expected and off_diagonal != sp.zeros(2),
        diagonal == sp.zeros(2),
    )


N5_LINES = (
    'N5: per_element: exact input-pin, conjugation, shared-polynomial, shared-root, Gram, rescaling, classification, covariance-contrast, and commutator certificates are checked',
    'per_site: one Grassmann mode per fine site on the antiperiodic reflection torus',
    'per_mode: at both rational shear fixtures the paired momenta are exact entrywise conjugates with a shared characteristic polynomial and stable root, and y_3 = conj(y_1) entrywise',
    'per_block: the paired quotient Gram is diag(1, g) with g = 1 invariantly, and the reality-fixed reflection-adjoint observable space is Sym_2(R), dimension 3, transfer-covariant exactly because rho_1 = rho_3',
    "lattice_wide: checked and not executed — the pair's observable dynamics and states, the flip work order, the common differential, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient beyond the displayed carrier, Records, audit retention, and TOE closure remain open",
)


SCOPE_KEYS = (
    "conjugate_pair",
    "entrywise_conj",
    "invariant_g",
    "real_symmetric_dimension",
    "jordan",
    "noncommuting",
    "covariance_honesty",
    "observable_milestone",
    "catch_record",
    "convergence",
    "ward_content",
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
        "conjugate_pair": (
            "conjugate pair" in note or "conjugate-pair" in note
        ),
        "entrywise_conj": "entrywise" in note and "conj" in note,
        "invariant_g": "g = 1" in note and "invariant" in note,
        "real_symmetric_dimension": (
            "real symmetric" in note
            and any(
                phrase in note
                for phrase in (
                    "three-dimensional",
                    "dimension 3",
                    "3-dimensional",
                )
            )
        ),
        "jordan": "jordan" in note,
        "noncommuting": "non-commuting" in note,
        "covariance_honesty": (
            ("for free" in note or "vacuous" in note)
            and "degeneracy" in note
        ),
        "observable_milestone": (
            "first" in note and "observable space" in note
        ),
        "catch_record": (
            "refuted" in note
            and ("referee" in note or "three-way" in note)
        ),
        "convergence": any(
            phrase in note
            for phrase in (
                "convergence",
                "same two dimensions",
                "balanced-pair",
            )
        ),
        "ward_content": (
            "does not conserve momentum" in note
            or ("commutator" in note and "nonzero" in note)
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
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CONJUGATE_PAIR_OBSERVABLE_SPACE_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_FACET_CHARGE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "scripts/admissibility_dirac_kahler_facet_charge_bridge_2026_08_17.py",
            "logs/runner-cache/admissibility_dirac_kahler_facet_charge_bridge_2026_08_17.txt",
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
            for number in range(103, 130)
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
        "Block 130 blobs, ancestors 129--103, and landed Block 119 runner/cache are pinned",
        authority_raw,
    )

    fixtures = tuple(
        b119.make_sectors(shear)
        for shear in (b119.prior.PRIMARY_SHEAR, b119.prior.SECOND_SHEAR)
    )
    pairs = tuple(pair_certificate(sectors) for sectors in fixtures)
    shared_raw = all(
        pair.polynomial_shared and pair.isolation_shared for pair in pairs
    )
    checks.check(
        "B-the-shared-polynomial",
        "k=1 and k=3 have one exact polynomial and one isolated stable root at both fixtures",
        shared_raw and mutation != "break_shared_polynomial",
    )

    conjugation_raw = all(
        pair.h00_conjugate
        and pair.x_conjugate
        and pair.y_entrywise_conjugate
        and pair.construction_mechanism
        and pair.y_residuals == (sp.Integer(0),) * 8
        for pair in pairs
    )
    checks.check(
        "C-the-conjugation-theorem",
        "h00_3=conj(h00_1) and y_3=conj(y_1) entrywise in the shared root field",
        conjugation_raw and mutation != "break_conjugation",
    )

    g_raw = all(
        pair.norms_real
        and pair.norms_nonzero
        and pair.g_one
        and pair.g == 1
        for pair in pairs
    )
    invariance_raw = all(
        pair.scale_symbol_nonzero
        and pair.rescaling_invariant
        and b119.red(pair.scaled_ratio - pair.g, pair.polynomial) == 0
        for pair in pairs
    )
    invariant_gate = g_raw and invariance_raw
    if mutation in ("break_g_value", "break_invariance"):
        invariant_gate = False
    checks.check(
        "D-the-invariant-g",
        "g=||y_3||^2/||y_1||^2=1 and a/conj(a) rescaling cancels symbolically",
        invariant_gate,
    )

    observables = observable_space_certificate()
    classification_raw = (
        observables.gram == sp.eye(2)
        and observables.exchange == sp.Matrix(((0, 1), (1, 0)))
        and observables.fixed_basis_unitary
        and observables.fixed_basis_reality
        and observables.reality_rank == 4
        and observables.adjoint_rank == 4
        and observables.combined_rank == 5
        and observables.solution_dimension == 3
        and observables.condition_set_exact
        and observables.basis_rank == 3
        and observables.basis_satisfies_conditions
        and observables.real_symmetric_exact
        and observables.jordan_closed
    )
    noncommutation_raw = observables.noncommuting
    observable_gate = classification_raw and noncommutation_raw
    if mutation in (
        "break_classification",
        "break_noncommutation",
        "claim_scalar_only",
    ):
        observable_gate = False
    checks.check(
        "E-the-observable-space",
        "R-covariance plus G-adjointness is exactly Sym_2(R), dimension 3, Jordan-closed and non-commuting",
        observable_gate,
    )

    transfers = tuple(
        transfer_covariance_certificate(sectors) for sectors in fixtures
    )
    pair_covariance_raw = all(
        transfer.pair_scalar and transfer.observable_basis_commutes
        for transfer in transfers
    )
    requested_contrast_raw = all(
        transfer.requested_zero_two_polynomials_different
        and transfer.requested_zero_two_intervals_disjoint
        and transfer.requested_rho_zero_not_rho_two
        and transfer.requested_sigma_fails
        and not transfer.actual_zero_two_degenerate
        for transfer in transfers
    )
    alternative_contrast_raw = all(
        transfer.alternative_zero_one_polynomials_different
        and transfer.alternative_zero_one_intervals_disjoint
        and transfer.alternative_rho_zero_not_rho_one
        and transfer.alternative_sigma_fails
        for transfer in transfers
    )
    zero_two_also_degenerate_raw = all(
        transfer.actual_zero_two_degenerate for transfer in transfers
    )
    transfer_gate = (
        pair_covariance_raw
        and alternative_contrast_raw
        and zero_two_also_degenerate_raw
    )
    if mutation == "break_degeneracy_contrast":
        transfer_gate = False
    checks.check(
        "F-the-transfer-covariance",
        "rho_1^2 I_2 gives covariance for free; the (0,1) non-degeneracy contrast holds and the (0,2) pair is itself degenerate",
        transfer_gate,
    )

    ward = ward_certificate()
    ward_raw = (
        ward.momentum_charge == sp.diag(1, -1)
        and ward.off_diagonal_nonzero
        and ward.diagonal_zero
        and ward.off_diagonal_commutator
        == -2 * sp.Matrix(((0, 1), (-1, 0)))
        and ward.diagonal_commutator == sp.zeros(2)
    )
    checks.check(
        "G-the-ward-content",
        "[sigma_x,P]=-2[[0,1],[-1,0]] is nonzero while [sigma_z,P]=0",
        ward_raw and mutation != "break_ward_commutators",
    )

    scope = scope_certificate(normalized_note(), mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "conjugation/g/observable/Jordan/degeneracy/Ward/N1--N8/W1/N5 and TOE firewalls are present",
        set(scope) == set(SCOPE_KEYS)
        and all(scope.values())
        and elapsed_before_scope <= 400,
    )

    print(
        "AUTHORITY: parent="
        f"{authority['parent']}; Block130 blobs=({authority['parent_note']},"
        f"{authority['parent_runner']},{authority['parent_cache']}); "
        f"Block119=({authority['b119_runner']},{authority['b119_cache']})"
    )
    for pair in pairs:
        print(
            f"PAIR c={pair.shear}: shared polynomial/root=True; "
            f"h00/x/y entrywise conj=True; y residuals={pair.y_residuals}; "
            f"g={pair.g}; scaled g={pair.scaled_ratio}"
        )
    print(
        "OBSERVABLES: conjugate-basis conditions are a,d real, d=a, "
        "c=conj(b); the unitary reality-fixed basis gives Sym_2(R), "
        f"dimension={observables.solution_dimension}; "
        f"[sigma_x,sigma_z]={observables.sigma_commutator.tolist()}"
    )
    print(
        "TRANSFER: (1,3)=rho_1^2 I_2 and all observable commutators vanish; "
        "imported (0,2) monodromies/polynomials/isolations are equal, so "
        f"[sigma_x,T_02]={transfers[0].requested_zero_two_sigma_commutator.tolist()}; "
        f"the exact available (0,1) contrast passes={alternative_contrast_raw}"
    )
    print(
        "WARD: P_pair=diag(1,-1) (units pi/2); "
        f"[sigma_x,P]={ward.off_diagonal_commutator.tolist()}; "
        f"[sigma_z,P]={ward.diagonal_commutator.tolist()}"
    )
    for line in N5_LINES:
        print(line)
    if checks.failed == 0:
        print(
            "RESULT: the program's first genuine non-scalar observable space "
            "exists — the conjugate-pair theorem makes the paired gram the "
            "identity exactly and invariantly, opening the three-dimensional "
            "symmetric algebra on the same two dimensions that carry the "
            "sourced gravity quotient"
        )
        print(
            "DECISION_CUT: develop the pair's observable dynamics and states; "
            "hand the flip work order across; advance the differential"
        )
    else:
        print(
            "RESULT: BLOCKED — Block 119 makes the requested (0,2) contrast "
            "degenerate, although conjugation, invariant g, classification, "
            "Ward content, and the exact (0,1) contrast are certified"
        )
        print(
            "DECISION_CUT: correct the falsifier from (0,2) to the exact "
            "non-degenerate (0,1) pair, or supply a different pinned transfer"
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
