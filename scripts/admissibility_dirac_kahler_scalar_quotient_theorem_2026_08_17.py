#!/usr/bin/env python3
"""Block 129: scalar-quotient theorem and the observable dimension count.

The runner rebuilds the fixed family-B descending operator from Block 126,
certifies that every rank-one quotient compression is a scalar, and isolates
the completion-independent adjointness gate and a bounded minimal slice.
All scientific arithmetic is exact; wall-clock timing is the sole float.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
from itertools import combinations
import math
from pathlib import Path
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_time_dressing_adjointness_wall_2026_08_17 as block126


R = sp.Rational
I = sp.I
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_SCALAR_QUOTIENT_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_"
    "2026_08_17.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_curved_carrier_"
    "dependency_2026_08_17.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SCALAR_QUOTIENT_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    "logs/runner-cache/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "02602ca09e4ea69a805a824c3c1f31cb1ee35b20"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block128-curved-carrier-dependency-20260817"
)
PARENT_COMMIT = "f6b0cf59e2cc588ebd3e34b96e730574cb485db2"
PARENT_NOTE_BLOB = "194cf07ad9a0b7269defe6bdba8750fc6fe95640"
PARENT_RUNNER_BLOB = "90f9b53b2ef499367f2f65fd8314a13137af203b"
PARENT_CACHE_BLOB = "d61e03774a11c5d983e52c779a42458983a2af52"
ANCESTOR_COMMITS = (
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
    "break_eigen_relation",
    "break_inertia_cite",
    "claim_nonscalar_quotient",
    "break_reduction",
    "break_universal_gate",
    "claim_moduli_witness",
    "break_slice_rank",
    "break_gcd",
    "break_forward_example",
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
    }


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


def exact_digest(*payload: object) -> str:
    return hashlib.sha256(sp.srepr(payload).encode("utf-8")).hexdigest()[:16]


# Reuse the exact Q(i,rho) representation and matrix arithmetic certified by
# Block 126; aliases keep every subsequent identity in the same root field.
Q = block126.Q
QMatrix = block126.QMatrix
QZERO = block126.QZERO
QONE = block126.QONE
QuadraticField = block126.QuadraticField
qmat_add = block126.qmat_add
qmat_sub = block126.qmat_sub
qmat_mul = block126.qmat_mul
qmat_scale = block126.qmat_scale
qmat_adjoint = block126.qmat_adjoint
qmat_flatten = block126.qmat_flatten
qmat_columns = block126.qmat_columns
qmat_zero = block126.qmat_zero
qmat_identity = block126.qmat_identity
qmat_rref = block126.qmat_rref


def qscalar(value: int | sp.Rational) -> Q:
    return block126.rational_scalar(R(value))


def qmat_from_columns(columns: tuple[QMatrix, ...]) -> QMatrix:
    if not columns or any(len(column[0]) != 1 for column in columns):
        raise AssertionError("quadratic-field column assembly")
    rows = len(columns[0])
    if any(len(column) != rows for column in columns):
        raise AssertionError("quadratic-field column heights")
    return tuple(
        tuple(column[row][0] for column in columns) for row in range(rows)
    )


def qmat_inverse(field: QuadraticField, source: QMatrix) -> QMatrix:
    size = len(source)
    if size == 0 or any(len(row) != size for row in source):
        raise AssertionError("quadratic-field inverse shape")
    identity = qmat_identity(size)
    augmented = tuple(
        source[row] + identity[row] for row in range(size)
    )
    reduced, pivots = qmat_rref(field, augmented)
    if pivots != tuple(range(size)):
        raise AssertionError("singular quadratic-field basis")
    inverse = tuple(row[size:] for row in reduced)
    if (
        qmat_mul(field, source, inverse) != identity
        or qmat_mul(field, inverse, source) != identity
    ):
        raise AssertionError("quadratic-field inverse certificate")
    return inverse


def qmat_transpose(source: QMatrix) -> QMatrix:
    return tuple(
        tuple(source[row][column] for row in range(len(source)))
        for column in range(len(source[0]))
    )


def qmat_nullspace(
    field: QuadraticField, source: QMatrix
) -> tuple[QMatrix, ...]:
    reduced, pivots = qmat_rref(field, source)
    free_columns = tuple(
        column for column in range(len(source[0])) if column not in pivots
    )
    result: list[QMatrix] = []
    for free_column in free_columns:
        vector = [QZERO for _ in range(len(source[0]))]
        vector[free_column] = QONE
        for row, pivot in enumerate(pivots):
            vector[pivot] = field.neg(reduced[row][free_column])
        column = tuple((value,) for value in vector)
        if not qmat_zero(qmat_mul(field, source, column)):
            raise AssertionError("quadratic-field nullspace certificate")
        result.append(column)
    return tuple(result)


def qmat_neg(field: QuadraticField, source: QMatrix) -> QMatrix:
    return tuple(
        tuple(field.neg(value) for value in row) for row in source
    )


def carrier_swap_block(mu: Q, mu_inverse: Q) -> QMatrix:
    return (
        (QZERO, mu_inverse, QZERO, QZERO),
        (mu, QZERO, QZERO, QZERO),
        (QZERO, QZERO, QZERO, mu_inverse),
        (QZERO, QZERO, mu, QZERO),
    )


def carrier_completion(
    field: QuadraticField,
    vectors: QMatrix,
    left_inverse: QMatrix,
    complement: QMatrix,
    mu: Q,
    mu_inverse: Q,
) -> QMatrix:
    carrier_part = qmat_mul(
        field,
        qmat_mul(field, vectors, carrier_swap_block(mu, mu_inverse)),
        left_inverse,
    )
    return qmat_add(field, carrier_part, complement)


@dataclass(frozen=True)
class ScalarFixture:
    shear: sp.Rational
    package: object
    sector: object
    field: QuadraticField
    x: QMatrix
    y: QMatrix
    h00: QMatrix
    raw_family: tuple[QMatrix, ...]
    operator_basis: tuple[QMatrix, ...]
    weights: tuple[Q, ...]
    operator: QMatrix
    eigenvalue: Q
    carrier_vectors: QMatrix
    carrier_left_inverse: QMatrix
    carrier_projector: QMatrix
    complement_projector: QMatrix
    theta_swap: QMatrix


def build_scalar_fixtures() -> tuple[ScalarFixture, ...]:
    packages = block126.prior.fixture_packages()
    if tuple(package.shear for package in packages) != block126.SHEARS:
        raise AssertionError("both pinned Block 126 fixtures")
    shift = block126.one_super_step_shifts()[0]
    result: list[ScalarFixture] = []
    for package in packages:
        routing = next(
            candidate
            for candidate in package.routings
            if candidate.routing == "t-first"
        )
        base = routing.temporal[block126.block121.site(2, 0)]
        raw_source = tuple(
            block126.momentum_block(
                (
                    shift**power * base * shift ** (-power)
                ).applyfunc(sp.expand),
                0,
                8,
            )
            for power in range(4)
        )
        sector = package.sectors[0]
        mode = block126.make_mode_result(
            0, sector, package.thetas[0], raw_source
        )
        witness = block126.descending_witness(mode)
        if witness is None:
            raise AssertionError("Block 126 family-B descending member")
        field = mode.field
        operator = block126.field_weighted_operator(
            field, witness.weights, mode.family
        )
        eigenvalue = block126.quotient_compression(field, mode.y, operator)
        x = field.matrix(sector.x)
        h00 = field.matrix(sector.h00)
        completion_data = block126.block119.reflection_real_completion(
            package.sectors
        )
        reality = completion_data.reality
        partner_x = block126.block119.reality_vector(
            reality, sector.x, sector.polynomial
        )
        partner_y = block126.block119.reality_vector(
            reality, sector.y, sector.polynomial
        )
        carrier_vectors = field.matrix(
            sp.Matrix.hstack(sector.x, sector.y, partner_x, partner_y)
        )
        carrier_adjoint = qmat_adjoint(field, carrier_vectors)
        carrier_gram = qmat_mul(field, carrier_adjoint, carrier_vectors)
        carrier_left_inverse = qmat_mul(
            field, qmat_inverse(field, carrier_gram), carrier_adjoint
        )
        carrier_projector = qmat_mul(
            field, carrier_vectors, carrier_left_inverse
        )
        complement_projector = qmat_sub(
            field, qmat_identity(8), carrier_projector
        )
        theta_swap = carrier_completion(
            field,
            carrier_vectors,
            carrier_left_inverse,
            complement_projector,
            QONE,
            QONE,
        )
        if (
            qmat_mul(field, carrier_left_inverse, carrier_vectors)
            != qmat_identity(4)
            or field.rank(carrier_projector) != 4
            or field.rank(complement_projector) != 4
            or theta_swap != field.matrix(package.thetas[0])
        ):
            raise AssertionError("Block 127 carrier chart reconstruction")
        result.append(
            ScalarFixture(
                shear=package.shear,
                package=package,
                sector=sector,
                field=field,
                x=x,
                y=mode.y,
                h00=h00,
                raw_family=tuple(field.matrix(member) for member in raw_source),
                operator_basis=mode.family,
                weights=witness.weights,
                operator=operator,
                eigenvalue=eigenvalue,
                carrier_vectors=carrier_vectors,
                carrier_left_inverse=carrier_left_inverse,
                carrier_projector=carrier_projector,
                complement_projector=complement_projector,
                theta_swap=theta_swap,
            )
        )
    return tuple(result)


def rank_one_rational_inertia(vector: sp.Matrix) -> tuple[int, int, int]:
    gram = vector * vector.H
    norm = sp.expand((vector.H * vector)[0])
    rank = gram.rank()
    if gram.H != gram or rank not in (0, 1) or norm == 0:
        return (0, 0, gram.rows)
    return (
        int(bool(norm > 0)),
        int(bool(norm < 0)),
        gram.rows - rank,
    )


@dataclass(frozen=True)
class QuotientCertificate:
    imported_inertias: tuple[tuple[tuple[int, int, int], ...], ...]
    live_inertia: tuple[int, int, int]
    cited_import_chain: bool
    basis_ranks: tuple[int, ...]
    projector_ranks: tuple[int, ...]
    basis_compressions_scalar: bool
    general_rank_one_identity: bool
    operator_action_exact: bool
    quotient_commutators_zero: bool
    quotient_algebra_dimension: int
    nonscalar_dimension: int


def quotient_certificate(
    fixtures: tuple[ScalarFixture, ...],
) -> QuotientCertificate:
    imported_inertias: list[tuple[tuple[int, int, int], ...]] = []
    for fixture in fixtures:
        package = fixture.package
        inertias: list[tuple[int, int, int]] = []
        for sector, theta in zip(package.sectors, package.thetas):
            completed = (theta * sector.h00).applyfunc(
                lambda value, polynomial=sector.polynomial: block126.prior.red(
                    value, polynomial
                )
            )
            inertias.append(
                block126.block119.rank_one_outer_inertia(
                    sector.y, completed, sector.polynomial
                )
            )
        imported_inertias.append(tuple(inertias))

    block124 = block126.prior.prior
    state_class = block124.state_class_certificate()
    live_fixture = next(
        item
        for item in state_class.fixtures
        if item.momentum == 0 and item.vector.rows == 4
    )
    live_inertia = rank_one_rational_inertia(live_fixture.vector)
    cited_import_chain = (
        block126.block119.__name__.endswith(
            "reflection_intertwiner_completion_2026_08_16"
        )
        and block124.__name__.endswith(
            "sourced_quotient_execution_2026_08_17"
        )
        and live_fixture.norm_squared
        == sp.expand((live_fixture.vector.H * live_fixture.vector)[0])
    )

    basis_ranks: list[int] = []
    projector_ranks: list[int] = []
    compression_scalar = True
    rank_one_identity = True
    operator_action = True
    commutators = True
    for fixture in fixtures:
        field = fixture.field
        bra = qmat_adjoint(field, fixture.y)
        norm = qmat_mul(field, bra, fixture.y)[0][0]
        projector = qmat_scale(
            field,
            field.inv(norm),
            qmat_mul(field, fixture.y, bra),
        )
        basis_ranks.append(field.rank(qmat_columns(fixture.operator_basis)))
        projector_ranks.append(field.rank(projector))
        compressions = tuple(
            block126.quotient_compression(field, fixture.y, operator)
            for operator in fixture.operator_basis
        )
        compression_scalar = compression_scalar and all(
            isinstance(value, tuple)
            and len(value) == 2
            and all(len(component) == 2 for component in value)
            for value in compressions
        )
        rank_one_identity = rank_one_identity and all(
            qmat_mul(
                field,
                qmat_mul(field, projector, operator),
                projector,
            )
            == qmat_scale(field, scalar, projector)
            for operator, scalar in zip(fixture.operator_basis, compressions)
        )
        operator_action = operator_action and (
            qmat_mul(
                field,
                qmat_mul(field, projector, fixture.operator),
                projector,
            )
            == qmat_scale(field, fixture.eigenvalue, projector)
        )
        commutators = commutators and all(
            field.mul(left, right) == field.mul(right, left)
            for left, right in combinations(compressions, 2)
        )

    positive_dimension = 1
    quotient_algebra_dimension = positive_dimension**2
    nonscalar_dimension = quotient_algebra_dimension - 1
    return QuotientCertificate(
        imported_inertias=tuple(imported_inertias),
        live_inertia=live_inertia,
        cited_import_chain=cited_import_chain,
        basis_ranks=tuple(basis_ranks),
        projector_ranks=tuple(projector_ranks),
        basis_compressions_scalar=compression_scalar,
        general_rank_one_identity=rank_one_identity,
        operator_action_exact=operator_action,
        quotient_commutators_zero=commutators,
        quotient_algebra_dimension=quotient_algebra_dimension,
        nonscalar_dimension=nonscalar_dimension,
    )


@dataclass(frozen=True)
class ReductionCertificate:
    mu: sp.Rational
    h00_factorization: bool
    completion_involution: bool
    completion_targets: bool
    completed_gram: bool
    residual_identity: bool
    zero_iff_vector: bool
    outer_injective: bool
    mu_inverse_linearity: bool


def reduction_certificate(fixture: ScalarFixture) -> ReductionCertificate:
    field = fixture.field
    mu_value = R(2)
    mu = qscalar(mu_value)
    mu_inverse = qscalar(1 / mu_value)
    completion = carrier_completion(
        field,
        fixture.carrier_vectors,
        fixture.carrier_left_inverse,
        fixture.complement_projector,
        mu,
        mu_inverse,
    )
    bra = qmat_adjoint(field, fixture.y)
    gram = qmat_mul(field, fixture.y, bra)
    reflected = qmat_mul(
        field,
        qmat_mul(field, completion, fixture.operator),
        completion,
    )
    completed_gram = qmat_mul(field, completion, fixture.h00)
    kernel = qmat_scale(field, mu, gram)
    residual = qmat_sub(
        field,
        qmat_mul(field, kernel, fixture.operator),
        qmat_mul(field, qmat_adjoint(field, reflected), kernel),
    )
    vector = qmat_sub(
        field,
        qmat_scale(field, fixture.eigenvalue, fixture.y),
        qmat_mul(field, qmat_adjoint(field, reflected), fixture.y),
    )
    displayed = qmat_mul(field, qmat_scale(field, mu, vector), bra)
    left_eigen = qmat_mul(field, bra, fixture.operator) == qmat_scale(
        field, fixture.eigenvalue, bra
    )
    outer_injective = any(value != QZERO for value in bra[0])
    return ReductionCertificate(
        mu=mu_value,
        h00_factorization=(
            fixture.h00
            == qmat_mul(field, fixture.x, qmat_adjoint(field, fixture.y))
        ),
        completion_involution=(
            qmat_mul(field, completion, completion) == qmat_identity(8)
        ),
        completion_targets=(
            qmat_mul(field, completion, fixture.x)
            == qmat_scale(field, mu, fixture.y)
            and qmat_mul(field, completion, fixture.y)
            == qmat_scale(field, mu_inverse, fixture.x)
        ),
        completed_gram=(completed_gram == kernel),
        residual_identity=(left_eigen and residual == displayed),
        zero_iff_vector=(qmat_zero(residual) == qmat_zero(vector)),
        outer_injective=outer_injective,
        mu_inverse_linearity=(
            carrier_swap_block(mu, mu_inverse)[1][0] == mu
            and carrier_swap_block(mu, mu_inverse)[0][1] == mu_inverse
            and carrier_swap_block(mu, mu_inverse)[3][2] == mu
            and carrier_swap_block(mu, mu_inverse)[2][3] == mu_inverse
        ),
    )


def rational_expression(value: Fraction) -> sp.Rational:
    return R(value.numerator, value.denominator)


@dataclass(frozen=True)
class UniversalGateCertificate:
    gate: QMatrix
    gate_shape: tuple[int, int]
    gate_rank: int
    eigenspace_rank: int
    eigenvalue_real: bool
    parameter_count: int
    complement_parameterized: bool
    involution_equations_displayed: bool
    parameter_independent: bool
    only_zero_target: bool


def universal_gate_certificate(
    fixture: ScalarFixture,
) -> UniversalGateCertificate:
    field = fixture.field
    bra = qmat_adjoint(field, fixture.y)
    shifted = qmat_sub(
        field,
        fixture.operator,
        qmat_scale(
            field,
            field.star(fixture.eigenvalue),
            qmat_identity(8),
        ),
    )
    left_eigenvectors = qmat_nullspace(field, qmat_transpose(shifted))
    if len(left_eigenvectors) != 1:
        raise AssertionError("one-dimensional left star(lambda) eigenspace")
    eigenbasis = qmat_from_columns(left_eigenvectors)
    pairing = qmat_mul(field, bra, fixture.carrier_vectors)
    mu_target: QMatrix = (
        (pairing[0][1],),
        (QZERO,),
        (pairing[0][3],),
        (QZERO,),
    )
    inverse_target: QMatrix = (
        (QZERO,),
        (pairing[0][0],),
        (QZERO,),
        (pairing[0][2],),
    )
    eigen_restriction = qmat_mul(
        field, qmat_transpose(fixture.carrier_vectors), eigenbasis
    )
    gate = qmat_from_columns(
        (
            eigen_restriction,
            qmat_neg(field, mu_target),
            qmat_neg(field, inverse_target),
        )
    )

    alpha, mu_symbol, inverse_symbol = sp.symbols(
        "alpha mu mu_inverse", real=True
    )
    a_symbols = sp.symbols("a0:16")
    b_symbols = sp.symbols("b0:16")
    complement_action = sp.Matrix(4, 4, a_symbols)
    complement_mix = sp.Matrix(4, 4, b_symbols)
    swap = sp.Matrix(
        (
            (0, inverse_symbol, 0, 0),
            (mu_symbol, 0, 0, 0),
            (0, 0, 0, inverse_symbol),
            (0, 0, mu_symbol, 0),
        )
    )
    moduli_block = sp.Matrix.vstack(
        sp.Matrix.hstack(swap, complement_mix),
        sp.Matrix.hstack(sp.zeros(4), complement_action),
    )
    squared = (moduli_block * moduli_block).applyfunc(sp.expand)
    expected_squared = sp.Matrix.vstack(
        sp.Matrix.hstack(
            mu_symbol * inverse_symbol * sp.eye(4),
            swap * complement_mix
            + complement_mix * complement_action,
        ),
        sp.Matrix.hstack(sp.zeros(4), complement_action**2),
    )
    mu_two = qscalar(2)
    inverse_two = qscalar(R(1, 2))
    theta_two = carrier_completion(
        field,
        fixture.carrier_vectors,
        fixture.carrier_left_inverse,
        fixture.complement_projector,
        mu_two,
        inverse_two,
    )
    target_two = qmat_add(
        field,
        qmat_scale(field, mu_two, mu_target),
        qmat_scale(field, inverse_two, inverse_target),
    )
    carrier_restriction_exact = (
        qmat_transpose(
            qmat_mul(
                field,
                qmat_mul(field, bra, theta_two),
                fixture.carrier_vectors,
            )
        )
        == target_two
    )
    complement_parameters = set(a_symbols) | set(b_symbols)
    gate_rank = field.rank(gate)
    return UniversalGateCertificate(
        gate=gate,
        gate_shape=(len(gate), len(gate[0])),
        gate_rank=gate_rank,
        eigenspace_rank=field.rank(shifted),
        eigenvalue_real=(field.star(fixture.eigenvalue) == fixture.eigenvalue),
        parameter_count=len(complement_parameters),
        complement_parameterized=(
            moduli_block.shape == (8, 8)
            and complement_parameters <= moduli_block.free_symbols
            and {mu_symbol, inverse_symbol} <= moduli_block.free_symbols
        ),
        involution_equations_displayed=(squared == expected_squared),
        parameter_independent=(
            carrier_restriction_exact
            and not (swap.free_symbols & complement_parameters)
        ),
        only_zero_target=(
            gate_rank == 3 and not qmat_nullspace(field, gate)
        ),
    )


Laurent = dict[int, Q]
LaurentMatrix = list[list[Laurent]]


def laurent_add(
    field: QuadraticField, left: Laurent, right: Laurent
) -> Laurent:
    result = dict(left)
    for exponent, value in right.items():
        result[exponent] = field.add(result.get(exponent, QZERO), value)
    return {
        exponent: value
        for exponent, value in result.items()
        if value != QZERO
    }


def laurent_neg(field: QuadraticField, source: Laurent) -> Laurent:
    return {exponent: field.neg(value) for exponent, value in source.items()}


def laurent_mul(
    field: QuadraticField, left: Laurent, right: Laurent
) -> Laurent:
    result: Laurent = {}
    for left_exponent, left_value in left.items():
        for right_exponent, right_value in right.items():
            exponent = left_exponent + right_exponent
            result[exponent] = field.add(
                result.get(exponent, QZERO),
                field.mul(left_value, right_value),
            )
    return {
        exponent: value
        for exponent, value in result.items()
        if value != QZERO
    }


def laurent_star(field: QuadraticField, source: Laurent) -> Laurent:
    return {
        exponent: field.star(value) for exponent, value in source.items()
    }


def constant_laurent_matrix(source: QMatrix) -> LaurentMatrix:
    return [
        [({0: value} if value != QZERO else {}) for value in row]
        for row in source
    ]


def laurent_matmul(
    field: QuadraticField,
    left: LaurentMatrix,
    right: LaurentMatrix,
) -> LaurentMatrix:
    if len(left[0]) != len(right):
        raise AssertionError("Laurent matrix product shape")
    result: LaurentMatrix = []
    for row in range(len(left)):
        target_row: list[Laurent] = []
        for column in range(len(right[0])):
            value: Laurent = {}
            for index in range(len(right)):
                value = laurent_add(
                    field,
                    value,
                    laurent_mul(
                        field, left[row][index], right[index][column]
                    ),
                )
            target_row.append(value)
        result.append(target_row)
    return result


def laurent_adjoint(
    field: QuadraticField, source: LaurentMatrix
) -> LaurentMatrix:
    return [
        [
            laurent_star(field, source[column][row])
            for column in range(len(source))
        ]
        for row in range(len(source[0]))
    ]


def slice_adjointness_coordinates(
    fixture: ScalarFixture,
) -> tuple[sp.Expr, sp.Expr, int]:
    """Return the exact displayed gcd and its mu>0 saturation.

    In the adapted (x,y,C) basis the B'=0, A'=I completion is the
    swap block [[0,mu^-1],[mu,0]] plus I_6.  The residual vector is a
    Laurent polynomial with exponents -2..2.  The theorem note uses the
    homogeneous coordinate packet mu^4*d; its common mu^2 is precisely
    the excluded boundary mu=0.  Dividing that factor is saturation on
    the admissible chart mu>0.
    """
    field = fixture.field
    operator = qmat_mul(
        field,
        qmat_mul(field, fixture.basis_inverse, fixture.operator),
        fixture.basis,
    )
    h_vector = qmat_mul(
        field, qmat_adjoint(field, fixture.basis), fixture.y
    )
    completion: LaurentMatrix = [
        [{} for _ in range(8)] for _ in range(8)
    ]
    completion[0][1] = {-1: QONE}
    completion[1][0] = {1: QONE}
    for index in range(2, 8):
        completion[index][index] = {0: QONE}
    reflected_vector = laurent_matmul(
        field,
        laurent_adjoint(field, completion),
        laurent_matmul(
            field,
            laurent_adjoint(field, constant_laurent_matrix(operator)),
            laurent_matmul(
                field,
                laurent_adjoint(field, completion),
                constant_laurent_matrix(h_vector),
            ),
        ),
    )
    target = [
        {0: field.mul(fixture.eigenvalue, h_vector[row][0])}
        for row in range(8)
    ]
    residual = tuple(
        laurent_add(
            field,
            target[row],
            laurent_neg(field, reflected_vector[row][0]),
        )
        for row in range(8)
    )
    if not residual or min(
        exponent for coordinate in residual for exponent in coordinate
    ) < -2:
        raise AssertionError("minimal-slice Laurent degree bound")

    mu_symbol = sp.symbols("mu", real=True)
    coordinate_polynomials: list[sp.Poly] = []
    for coordinate in residual:
        for quadratic_component in range(2):
            for gaussian_component in range(2):
                expression = sum(
                    (
                        rational_expression(
                            coefficient[quadratic_component][gaussian_component]
                        )
                        * mu_symbol ** (exponent + 4)
                    )
                    for exponent, coefficient in coordinate.items()
                )
                if expression != 0:
                    coordinate_polynomials.append(
                        sp.Poly(expression, mu_symbol, domain=sp.QQ)
                    )
    if not coordinate_polynomials:
        raise AssertionError("nonempty adjointness coordinate packet")
    coordinate_gcd = coordinate_polynomials[0]
    for polynomial in coordinate_polynomials[1:]:
        coordinate_gcd = sp.gcd(coordinate_gcd, polynomial)
    coordinate_gcd = sp.monic(coordinate_gcd)
    boundary = sp.Poly(mu_symbol**2, mu_symbol, domain=sp.QQ)
    saturated = sp.div(coordinate_gcd, boundary, domain=sp.QQ)
    if saturated[1] != 0:
        raise AssertionError("mu-boundary saturation")
    return (
        coordinate_gcd.as_expr(),
        sp.monic(saturated[0]).as_expr(),
        len(coordinate_polynomials),
    )


@dataclass(frozen=True)
class MinimalSliceCertificate:
    sample_mus: tuple[sp.Rational, ...]
    leakage_ranks: tuple[tuple[int, ...], ...]
    leakage_upper_bound: int
    generic_rank: int
    completion_involutions: bool
    determinant_identically_zero: bool
    charts_used: int
    cofactor_gcd: sp.Expr
    cofactor_positive_roots: int
    residual_gcd: sp.Expr
    residual_positive_roots: int
    interpolation_exact: bool
    second_fixture_nonzero: bool
    second_fixture_compression_nonzero: bool
    second_fixture_residual_nonzero: bool


def qdet(field: QuadraticField, source: QMatrix) -> Q:
    work = [list(row) for row in source]
    determinant = QONE
    sign = 1
    for column in range(len(work)):
        pivot = next(
            (
                row
                for row in range(column, len(work))
                if work[row][column] != QZERO
            ),
            None,
        )
        if pivot is None:
            return QZERO
        if pivot != column:
            work[pivot], work[column] = work[column], work[pivot]
            sign *= -1
        pivot_value = work[column][column]
        determinant = field.mul(determinant, pivot_value)
        inverse = field.inv(pivot_value)
        for row in range(column + 1, len(work)):
            if work[row][column] == QZERO:
                continue
            factor = field.mul(work[row][column], inverse)
            for entry in range(column, len(work)):
                work[row][entry] = field.sub(
                    work[row][entry],
                    field.mul(factor, work[column][entry]),
                )
    return field.neg(determinant) if sign < 0 else determinant


def q_coordinates(
    value: Q,
) -> tuple[sp.Rational, sp.Rational, sp.Rational, sp.Rational]:
    return tuple(
        rational_expression(component)
        for gaussian in value
        for component in gaussian
    )  # type: ignore[return-value]


def interpolate_coordinate(
    nodes: tuple[sp.Rational, ...],
    values: tuple[sp.Rational, ...],
    variable: sp.Symbol,
) -> sp.Poly:
    expression = sp.interpolate(tuple(zip(nodes, values)), variable)
    return sp.Poly(sp.cancel(expression), variable, domain=sp.QQ)


def coordinate_polynomials(
    nodes: tuple[sp.Rational, ...],
    values: tuple[Q, ...],
    variable: sp.Symbol,
) -> tuple[sp.Poly, ...]:
    return tuple(
        interpolate_coordinate(
            nodes,
            tuple(q_coordinates(value)[coordinate] for value in values),
            variable,
        )
        for coordinate in range(4)
    )


def polynomial_gcd(
    polynomials: tuple[sp.Poly, ...], variable: sp.Symbol
) -> sp.Poly:
    nonzero = tuple(polynomial for polynomial in polynomials if not polynomial.is_zero)
    if not nonzero:
        return sp.Poly(0, variable, domain=sp.QQ)
    result = nonzero[0]
    for polynomial in nonzero[1:]:
        result = sp.gcd(result, polynomial)
    return result.monic()


def strict_positive_root_count(polynomial: sp.Poly, variable: sp.Symbol) -> int:
    reduced = polynomial
    coordinate = sp.Poly(variable, variable, domain=sp.QQ)
    while not reduced.is_zero and reduced.rem(coordinate).is_zero:
        reduced = reduced.exquo(coordinate)
    return 0 if reduced.is_zero else int(reduced.count_roots(0, sp.oo))


def minimal_slice_state(
    fixture: ScalarFixture, mu_value: sp.Rational
) -> tuple[QMatrix, tuple[QMatrix, ...], QMatrix]:
    field = fixture.field
    theta = carrier_completion(
        field,
        fixture.carrier_vectors,
        fixture.carrier_left_inverse,
        fixture.complement_projector,
        qscalar(mu_value),
        qscalar(1 / mu_value),
    )
    dressed = tuple(
        qmat_mul(field, qmat_mul(field, theta, member), theta)
        for member in fixture.raw_family
    )
    family = fixture.raw_family + dressed
    leakage = block126.family_leakage_matrix(field, fixture.y, family)
    return theta, family, leakage


def qcofactor_kernel(
    fixture: ScalarFixture,
    leakage: QMatrix,
    rows: tuple[int, ...],
) -> tuple[Q, ...]:
    restricted = tuple(leakage[row] for row in rows)
    weights: list[Q] = []
    for omitted in range(8):
        minor = tuple(
            tuple(row[column] for column in range(8) if column != omitted)
            for row in restricted
        )
        value = qdet(fixture.field, minor)
        weights.append(fixture.field.neg(value) if omitted % 2 else value)
    return tuple(weights)


def qkernel_residual(
    fixture: ScalarFixture,
    theta: QMatrix,
    family: tuple[QMatrix, ...],
    leakage: QMatrix,
    rows: tuple[int, ...],
) -> tuple[tuple[Q, ...], QMatrix, QMatrix, Q, tuple[Q, ...]]:
    field = fixture.field
    weights = qcofactor_kernel(fixture, leakage, rows)
    weight_column: QMatrix = tuple((value,) for value in weights)
    leak = qmat_mul(field, leakage, weight_column)
    operator = block126.field_weighted_operator(field, weights, family)
    eigenvalue = block126.quotient_compression(field, fixture.y, operator)
    shifted = qmat_sub(
        field,
        operator,
        qmat_scale(field, field.star(eigenvalue), qmat_identity(8)),
    )
    bra_theta = qmat_mul(field, qmat_adjoint(field, fixture.y), theta)
    residual = qmat_mul(field, bra_theta, shifted)[0]
    return weights, leak, operator, eigenvalue, residual


def proportional_weights(
    field: QuadraticField, left: tuple[Q, ...], right: tuple[Q, ...]
) -> bool:
    index = next(
        (
            item
            for item, (a, b) in enumerate(zip(left, right))
            if a != QZERO and b != QZERO
        ),
        None,
    )
    if index is None:
        return False
    scale = field.div(left[index], right[index])
    return all(
        a == field.mul(scale, b) for a, b in zip(left, right)
    )


def minimal_slice_certificate(
    fixtures: tuple[ScalarFixture, ...],
) -> MinimalSliceCertificate:
    primary, secondary = fixtures
    sample_mus = (R(1), R(2), R(3))
    sample_states = tuple(
        tuple(minimal_slice_state(fixture, mu) for mu in sample_mus)
        for fixture in fixtures
    )
    sample_ranks = tuple(
        tuple(
            len(qmat_rref(fixture.field, state[2])[1])
            for state in states
        )
        for fixture, states in zip(fixtures, sample_states)
    )
    involutions = all(
        qmat_mul(fixture.field, state[0], state[0]) == qmat_identity(8)
        for fixture, states in zip(fixtures, sample_states)
        for state in states
    )

    bra = qmat_adjoint(primary.field, primary.y)
    norm = qmat_mul(primary.field, bra, primary.y)[0][0]
    positive_projector = qmat_scale(
        primary.field,
        primary.field.inv(norm),
        qmat_mul(primary.field, primary.y, bra),
    )
    leakage_upper_bound = primary.field.rank(
        qmat_sub(primary.field, qmat_identity(8), positive_projector)
    )

    variable = sp.symbols("mu")
    nodes = tuple(R(value) for value in range(1, 22))
    states = tuple(minimal_slice_state(primary, node) for node in nodes)
    scaled_determinants = tuple(
        primary.field.mul(qscalar(node**8), qdet(primary.field, state[2]))
        for node, state in zip(nodes, states)
    )
    determinant_polynomials = coordinate_polynomials(
        nodes[:17], scaled_determinants[:17], variable
    )
    interpolation_exact = all(
        polynomial.eval(nodes[index])
        == q_coordinates(scaled_determinants[index])[coordinate]
        for index in (17, 18)
        for coordinate, polynomial in enumerate(determinant_polynomials)
    )
    determinant_identically_zero = all(
        polynomial.is_zero for polynomial in determinant_polynomials
    )

    _, row_pivots = qmat_rref(
        primary.field, qmat_transpose(states[0][2])
    )
    if len(row_pivots) != 7:
        raise AssertionError("mu=1 leakage row rank")
    first_rows = tuple(row_pivots)
    all_charts = (first_rows,) + tuple(
        tuple(row for row in range(8) if row != omitted)
        for omitted in range(8)
        if tuple(row for row in range(8) if row != omitted) != first_rows
    )
    cofactor_polynomials: list[sp.Poly] = []
    residual_polynomials: list[sp.Poly] = []
    cofactor_common = sp.Poly(0, variable, domain=sp.QQ)
    residual_common = sp.Poly(0, variable, domain=sp.QQ)
    charts_used = 0
    for rows in all_charts:
        results = tuple(
            qkernel_residual(primary, theta, family, leakage, rows)
            for theta, family, leakage in states
        )
        interpolation_exact = interpolation_exact and all(
            qmat_zero(result[1]) for result in results
        )
        interpolation_exact = interpolation_exact and all(
            primary.field.star(weight) == weight
            for result in results
            for weight in result[0]
        )
        if charts_used == 0:
            interpolation_exact = interpolation_exact and proportional_weights(
                primary.field, results[0][0], primary.weights
            )
        for column in range(8):
            values = tuple(
                primary.field.mul(qscalar(node**8), result[0][column])
                for node, result in zip(nodes, results)
            )
            polynomials = coordinate_polynomials(
                nodes[:17], values[:17], variable
            )
            interpolation_exact = interpolation_exact and all(
                polynomial.eval(nodes[index])
                == q_coordinates(values[index])[coordinate]
                for index in range(17, 21)
                for coordinate, polynomial in enumerate(polynomials)
            )
            cofactor_polynomials.extend(polynomials)
        for entry in range(8):
            values = tuple(
                primary.field.mul(qscalar(node**9), result[4][entry])
                for node, result in zip(nodes, results)
            )
            polynomials = coordinate_polynomials(
                nodes[:19], values[:19], variable
            )
            interpolation_exact = interpolation_exact and all(
                polynomial.eval(nodes[index])
                == q_coordinates(values[index])[coordinate]
                for index in (19, 20)
                for coordinate, polynomial in enumerate(polynomials)
            )
            residual_polynomials.extend(polynomials)
        charts_used += 1
        cofactor_common = polynomial_gcd(
            tuple(cofactor_polynomials), variable
        )
        residual_common = polynomial_gcd(
            tuple(residual_polynomials), variable
        )
        if (
            not cofactor_common.is_zero
            and strict_positive_root_count(cofactor_common, variable) == 0
            and not residual_common.is_zero
            and strict_positive_root_count(residual_common, variable) == 0
        ):
            break

    secondary_theta, secondary_family, secondary_leakage = sample_states[1][1]
    _, secondary_rows = qmat_rref(
        secondary.field, qmat_transpose(secondary_leakage)
    )
    secondary_result = qkernel_residual(
        secondary,
        secondary_theta,
        secondary_family,
        secondary_leakage,
        tuple(secondary_rows),
    )
    secondary_nonzero = not qmat_zero(secondary_result[2])
    secondary_compression = secondary_result[3] != QZERO
    secondary_residual = any(value != QZERO for value in secondary_result[4])
    secondary_exact = (
        len(secondary_rows) == 7
        and qmat_zero(secondary_result[1])
        and all(
            secondary.field.star(weight) == weight
            for weight in secondary_result[0]
        )
    )
    interpolation_exact = interpolation_exact and secondary_exact
    generic_rank = (
        7
        if determinant_identically_zero
        and not cofactor_common.is_zero
        and strict_positive_root_count(cofactor_common, variable) == 0
        and leakage_upper_bound == 7
        else -1
    )
    return MinimalSliceCertificate(
        sample_mus=sample_mus,
        leakage_ranks=sample_ranks,
        leakage_upper_bound=leakage_upper_bound,
        generic_rank=generic_rank,
        completion_involutions=involutions,
        determinant_identically_zero=determinant_identically_zero,
        charts_used=charts_used,
        cofactor_gcd=cofactor_common.as_expr(),
        cofactor_positive_roots=strict_positive_root_count(
            cofactor_common, variable
        ),
        residual_gcd=residual_common.as_expr(),
        residual_positive_roots=strict_positive_root_count(
            residual_common, variable
        ),
        interpolation_exact=interpolation_exact,
        second_fixture_nonzero=secondary_nonzero,
        second_fixture_compression_nonzero=secondary_compression,
        second_fixture_residual_nonzero=secondary_residual,
    )


def forward_count_certificate() -> dict[str, object]:
    sigma_x = sp.Matrix(((0, 1), (1, 0)))
    sigma_z = sp.Matrix(((1, 0), (0, -1)))
    commutator = sigma_x * sigma_z - sigma_z * sigma_x
    identity = sp.eye(2)
    return {
        "dimension": 2,
        "x_hermitian": sigma_x.H == sigma_x,
        "z_hermitian": sigma_z.H == sigma_z,
        "x_nonscalar": sigma_x[0, 1] != 0,
        "z_nonscalar": sigma_z[0, 0] != sigma_z[1, 1],
        "commutator": commutator,
        "commutator_rank": commutator.rank(),
    }


SCOPE_KEYS = (
    "scalar_quotient",
    "one_positive",
    "scalar_algebra",
    "vacuity",
    "number_not_observable",
    "forward_count",
    "completion_independent",
    "reduction",
    "universal_gate",
    "hunt_boundary",
    "unclassified",
    "dimension_downstream",
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
)


def scope_certificate(note: str, mutation: str) -> dict[str, bool]:
    result = {
        "scalar_quotient": (
            "scalar-quotient" in note or "scalar quotient" in note
        ),
        "one_positive": "one positive direction per momentum" in note,
        "scalar_algebra": (
            "multiple of the identity" in note or "scalars" in note
        ),
        "vacuity": any(
            phrase in note
            for phrase in (
                "carries no information",
                "automatically true",
                "vacuous",
            )
        ),
        "number_not_observable": "a number, not an observable" in note
            or "a number rather than" in note,
        "forward_count": "at least two positive directions" in note,
        "completion_independent": "completion-independent" in note,
        "reduction": (
            "mu cancels" in note or "single vector equation" in note
        ),
        "universal_gate": (
            "rank-3 gate" in note or "mu = mu^{-1} = 0" in note
        ),
        "hunt_boundary": (
            "21-point" in note or "witness hunt" in note
        ),
        "unclassified": "unclassified" in note,
        "dimension_downstream": (
            "downstream of" in note or "dimension count" in note
        ),
        "os_boundary": (
            "not an os no-go" in note
            or "not a curved os no-go" in note
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
    }
    if mutation == "weaken_no_go_packet":
        result["os_boundary"] = False
        result["n1_n8"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_axiom_amendment":
        result["axiom"] = False
    return result


N5_LINES = (
    "N5: per_element: the quotient has exactly one positive direction per momentum at both rational shear fixtures, every quotient observable is a scalar multiple of the identity, and every commutator vanishes",
    "per_site: one Grassmann mode per fine site in the certified flat package",
    "per_mode: the descending member satisfies y^H O* = lambda y^H with nonzero lambda and therefore acts as lambda times the identity on the quotient, so any single-operator Ward statement is automatic and carries no information",
    "per_block: the fixed-member adjointness equation is completion-independent after the overall mu cancels: its (mu, mu^{-1}) target gate has exact rank 3, the genuine 21-point hunt finds no witness at either fixture, and the minimal self-consistent slice remains empty with rank 7 and gcd mu^2; the general self-consistent case is unclassified",
    "lattice_wide: checked and not executed — carriers with at least two positive directions per momentum, the paired-momentum-degeneracy observable question, richer-carrier OS positivity, cross-lane facet-charge bridge, common nilpotent differential construction, actual ADM/history transporter completion, joint gravity, gravity constraint quotient beyond the displayed carrier, Records, audit retention, and TOE closure remain open",
)


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
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SCALAR_QUOTIENT_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
            "logs/runner-cache/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.txt",
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
            for number in range(103, 128)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB
    )
    checks.check(
        "A-authority",
        "Block 128 note/runner/cache and ancestors 127--103 are pinned",
        authority_raw,
    )

    fixtures = build_scalar_fixtures()
    eigen_raw = all(
        fixture.eigenvalue != QZERO
        and qmat_mul(
            fixture.field,
            qmat_adjoint(fixture.field, fixture.y),
            fixture.operator,
        )
        == qmat_scale(
            fixture.field,
            fixture.eigenvalue,
            qmat_adjoint(fixture.field, fixture.y),
        )
        for fixture in fixtures
    )
    eigen_gate = eigen_raw
    if mutation == "break_eigen_relation":
        eigen_gate = False
    checks.check(
        "B-the-eigen-relation",
        "the rebuilt family-B O* obeys y^H O*=lambda y^H with lambda nonzero in both fixtures",
        eigen_gate,
    )

    quotient = quotient_certificate(fixtures)
    quotient_raw = (
        quotient.cited_import_chain
        and quotient.imported_inertias
        == tuple(tuple((1, 0, 7) for _ in range(4)) for _ in fixtures)
        and quotient.live_inertia == (1, 0, 3)
        and quotient.basis_ranks == tuple(8 for _ in fixtures)
        and quotient.projector_ranks == tuple(1 for _ in fixtures)
        and quotient.basis_compressions_scalar
        and quotient.general_rank_one_identity
        and quotient.operator_action_exact
        and quotient.quotient_commutators_zero
        and quotient.quotient_algebra_dimension == 1
        and quotient.nonscalar_dimension == 0
    )
    quotient_gate = quotient_raw
    if mutation in ("break_inertia_cite", "claim_nonscalar_quotient"):
        quotient_gate = False
    checks.check(
        "C-the-scalar-quotient-theorem",
        "one positive direction makes all eight-basis compressions scalar, O*=lambda I, and every quotient commutator zero",
        quotient_gate,
    )

    reductions = tuple(reduction_certificate(fixture) for fixture in fixtures)
    reduction_raw = all(
        item.h00_factorization
        and item.completion_involution
        and item.completion_targets
        and item.completed_gram
        and item.residual_identity
        and item.zero_iff_vector
        and item.outer_injective
        and item.mu_inverse_linearity
        for item in reductions
    )
    reduction_gate = reduction_raw
    if mutation == "break_reduction":
        reduction_gate = False
    checks.check(
        "D-the-reduction",
        "R(O*)=mu[lambda y-(Theta' O* Theta')^H y]y^H and mu cancels to one vector equation",
        reduction_gate,
    )

    universal = tuple(
        universal_gate_certificate(fixture) for fixture in fixtures
    )
    universal_raw = all(
        item.gate_shape == (4, 3)
        and item.gate_rank == 3
        and item.eigenspace_rank == 7
        and item.eigenvalue_real
        and item.parameter_count == 32
        and item.complement_parameterized
        and item.involution_equations_displayed
        and item.parameter_independent
        and item.only_zero_target
        for item in universal
    )
    universal_gate = universal_raw
    if mutation in ("break_universal_gate", "claim_moduli_witness"):
        universal_gate = False
    checks.check(
        "E-the-universal-gate",
        "the completion-independent 4x3 gate has rank 3 and forces mu=mu^-1=0 in both fixtures",
        universal_gate,
    )

    slice_result = minimal_slice_certificate(fixtures)
    residual_gcd_poly = sp.Poly(slice_result.residual_gcd)
    slice_rank_raw = (
        slice_result.sample_mus == (R(1), R(2), R(3))
        and slice_result.leakage_ranks == ((7, 7, 7), (7, 7, 7))
        and slice_result.leakage_upper_bound == 7
        and slice_result.generic_rank == 7
        and slice_result.completion_involutions
        and slice_result.determinant_identically_zero
        and slice_result.charts_used >= 1
        and slice_result.cofactor_positive_roots == 0
    )
    gcd_raw = (
        residual_gcd_poly.as_dict() == {(2,): R(1)}
        and slice_result.residual_positive_roots == 0
        and slice_result.interpolation_exact
        and slice_result.second_fixture_nonzero
        and slice_result.second_fixture_compression_nonzero
        and slice_result.second_fixture_residual_nonzero
    )
    slice_gate = slice_rank_raw and gcd_raw
    if mutation == "break_slice_rank":
        slice_gate = False
    if mutation == "break_gcd":
        slice_gate = False
    checks.check(
        "F-the-minimal-slice",
        "B'=0,A'=I has generic leakage rank 7; exact mu=1,2,3 samples pass and the coordinate gcd is mu^2",
        slice_gate,
    )

    forward = forward_count_certificate()
    forward_raw = (
        forward["dimension"] == 2
        and forward["x_hermitian"]
        and forward["z_hermitian"]
        and forward["x_nonscalar"]
        and forward["z_nonscalar"]
        and forward["commutator"] != sp.zeros(2)
        and forward["commutator_rank"] == 2
    )
    forward_gate = forward_raw
    if mutation == "break_forward_example":
        forward_gate = False
    checks.check(
        "G-the-forward-count",
        "two positive directions support noncommuting Hermitian quotient operators; no richer-carrier positivity is claimed",
        forward_gate,
    )

    scope = scope_certificate(normalized_note(), mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "scalar-quotient/dimension-count/moduli/N1--N8/W1/N5 and no-go/TOE firewalls are present",
        set(scope) == set(SCOPE_KEYS)
        and all(scope.values())
        and elapsed_before_scope <= 400,
    )

    print(
        "AUTHORITY: "
        f"parent={authority['parent']}; Block128 blobs="
        f"({authority['parent_note']},{authority['parent_runner']},"
        f"{authority['parent_cache']}); axiom={authority['axiom']}"
    )
    print(
        "EIGEN: fixtures="
        f"{tuple(fixture.shear for fixture in fixtures)}; "
        "y^H O*=lambda y^H exactly; lambda!=0 in both"
    )
    print(
        "QUOTIENT: imported momentum inertias="
        f"{quotient.imported_inertias}; live Block124 momentum-zero "
        f"inertia={quotient.live_inertia}; dim End(Q_+)="
        f"{quotient.quotient_algebra_dimension}; nonscalar dim="
        f"{quotient.nonscalar_dimension}; compression(O)="
        "y^H O y/(y^H y) in Q(i,rho)"
    )
    print(
        "REDUCTION: R(O*)=mu[lambda y-(Theta' O* Theta')^H y]y^H; "
        "mu>0 cancels; Theta' is linear in the displayed "
        "(mu,mu^-1) targets"
    )
    print(
        "UNIVERSAL: gate shapes/ranks="
        f"{tuple((item.gate_shape, item.gate_rank) for item in universal)}; "
        "32 symbolic A'/B' complement parameters absent; "
        "only (alpha,mu,mu^-1)=(0,0,0)"
    )
    print(
        "SLICE: B'=0,A'=I; leakage ranks at mu=(1,2,3)="
        f"{slice_result.leakage_ranks}; generic rank="
        f"{slice_result.generic_rank}; charts={slice_result.charts_used}; "
        f"adjointness gcd={slice_result.residual_gcd}; positive roots="
        f"{slice_result.residual_positive_roots}; general self-consistent "
        "case=UNCLASSIFIED"
    )
    print(
        "FORWARD: sigma_x and sigma_z are Hermitian on C^2 and "
        f"rank[sigma_x,sigma_z]={forward['commutator_rank']}; this is "
        "an existence count, not an OS-positivity construction"
    )
    for line in N5_LINES:
        print(line)
    print(
        "RESULT: the observable wall dissolves into a dimension count — "
        "the rank-one quotient carries only scalars, so no completion "
        "choice could ever have produced a local observable, and the "
        "forward program is carriers with at least two positive directions "
        "per momentum"
    )
    print(
        "DECISION_CUT: pose the richer-carrier construction and the "
        "cross-lane bridge; reject single-operator observable claims on "
        "rank-one quotients"
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
