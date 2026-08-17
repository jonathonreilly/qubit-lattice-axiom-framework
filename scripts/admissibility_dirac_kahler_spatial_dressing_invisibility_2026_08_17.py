#!/usr/bin/env python3
"""Block 125: exact spatial-dressing invisibility at the quotient wall.

The checker keeps only momentum-diagonal quotient blocks.  On those blocks
the spatial shift is the scalar ``i**k`` times the eight-dimensional
identity, so translated densities collapse exactly to two weight sums after
including their Theta conjugates.  Every scientific computation uses exact
SymPy arithmetic; wall-clock timing is the sole floating-point quantity.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
from pathlib import Path
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_sourced_quotient_execution_2026_08_17 as prior


R = sp.Rational
I = sp.I
block123 = prior.prior
block121 = prior.block121
block119 = prior.block119
RHO = block119.RHO
SHEARS = prior.SHEARS
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_DRESSING_INVISIBILITY_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SOURCED_QUOTIENT_EXECUTION_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_sourced_quotient_execution_"
    "2026_08_17.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_sourced_quotient_"
    "execution_2026_08_17.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_DRESSING_INVISIBILITY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SOURCED_QUOTIENT_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_sourced_quotient_execution_2026_08_17.py",
    "logs/runner-cache/admissibility_dirac_kahler_sourced_quotient_execution_2026_08_17.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "31e4c7ff7d41db6a78feef19dba2bfbea3dc1830"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block124-sourced-quotient-execution-20260817"
)
PARENT_COMMIT = "da2b9020e9f15ac55640ef87a0798a78e3c9a0d0"
PARENT_NOTE_BLOB = "f31c1e10219d8cd85cbd24644f0e5f4dfbba90d5"
PARENT_RUNNER_BLOB = "e105a17baa2cae6e1b032f32163ec53c53509a20"
PARENT_CACHE_BLOB = "589f7b4a3ef55bc298c048f8d252e188ba66e68d"
ANCESTOR_COMMITS = (
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
    "break_invisibility_lemma",
    "break_collapse",
    "break_rank_two",
    "claim_nonzero_descent",
    "break_dimension_counts",
    "claim_same_spaces",
    "break_time_visibility",
    "claim_counterterm_theorem",
    "break_refutation_record",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_toe_progress",
    "claim_axiom_amendment",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition) -> None:
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
    ancestors = {
        f"ancestor_{number}": is_ancestor(commit, "HEAD")
        for number, commit in ANCESTOR_COMMITS
    }
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        **ancestors,
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
    }


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.expand(value) == 0 for value in matrix)


def exact_digest(*payload: object) -> str:
    return hashlib.sha256(sp.srepr(payload).encode("utf-8")).hexdigest()[:16]


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


def red(value: sp.Expr, polynomial: sp.Poly) -> sp.Expr:
    """Reduce exactly in Q(i,rho_k)."""
    return block119.red(value, polynomial)


def field_matrix(matrix: sp.MatrixBase, polynomial: sp.Poly) -> sp.Matrix:
    return block119.field_matrix(sp.Matrix(matrix), polynomial)


def field_equal(
    left: sp.MatrixBase, right: sp.MatrixBase, polynomial: sp.Poly
) -> bool:
    return block119.field_equal(sp.Matrix(left), sp.Matrix(right), polynomial)


def field_rank(matrix: sp.MatrixBase, polynomial: sp.Poly) -> int:
    """Gaussian rank over Q(i)[rho]/(polynomial), reducing every operation."""
    work = field_matrix(matrix, polynomial)
    pivot_row = 0
    for column in range(work.cols):
        pivot = next(
            (
                candidate
                for candidate in range(pivot_row, work.rows)
                if red(work[candidate, column], polynomial) != 0
            ),
            None,
        )
        if pivot is None:
            continue
        if pivot != pivot_row:
            work.row_swap(pivot, pivot_row)
        inverse = red(1 / work[pivot_row, column], polynomial)
        for entry in range(column, work.cols):
            work[pivot_row, entry] = red(
                work[pivot_row, entry] * inverse, polynomial
            )
        for other in range(work.rows):
            if other == pivot_row:
                continue
            factor = red(work[other, column], polynomial)
            if factor == 0:
                continue
            for entry in range(column, work.cols):
                work[other, entry] = red(
                    work[other, entry]
                    - factor * work[pivot_row, entry],
                    polynomial,
                )
        pivot_row += 1
        if pivot_row == work.rows:
            break
    return pivot_row


def split_fixed(
    value: sp.Expr, polynomial: sp.Poly
) -> tuple[sp.Expr, sp.Expr]:
    """Write a field value as a+i*b with a,b fixed by the field star."""
    value = red(value, polynomial)
    conjugate = block119.star(value, polynomial)
    return (
        red((value + conjugate) / 2, polynomial),
        red((value - conjugate) / (2 * I), polynomial),
    )


def realify(matrix: sp.MatrixBase, polynomial: sp.Poly) -> sp.Matrix:
    """Realification over the star-fixed root field."""
    matrix = sp.Matrix(matrix)
    result = sp.zeros(2 * matrix.rows, 2 * matrix.cols)
    for row in range(matrix.rows):
        for column in range(matrix.cols):
            real, imag = split_fixed(matrix[row, column], polynomial)
            result[2 * row, 2 * column] = real
            result[2 * row, 2 * column + 1] = -imag
            result[2 * row + 1, 2 * column] = imag
            result[2 * row + 1, 2 * column + 1] = real
    return result


def descent_constraints(y: sp.Matrix, polynomial: sp.Poly) -> sp.Matrix:
    """The seven independent equations y^H O (I-P_y)=0 on 64 entries."""
    bra = block119.field_adjoint(y, polynomial)
    if red(bra[0], polynomial) == 0:
        raise AssertionError("the pinned descent pivot must be nonzero")
    constraints = sp.zeros(7, 64)
    for equation, output in enumerate(range(1, 8)):
        for input_row in range(8):
            constraints[equation, 8 * input_row + output] = red(
                bra[input_row] * bra[0], polynomial
            )
            constraints[equation, 8 * input_row] = red(
                -bra[input_row] * bra[output], polynomial
            )
    return constraints


def adjoint_constraints(y: sp.Matrix, polynomial: sp.Poly) -> sp.Matrix:
    """Descent realified, plus reality of its induced quotient scalar."""
    result = realify(descent_constraints(y, polynomial), polynomial).col_join(
        sp.zeros(1, 128)
    )
    bra = block119.field_adjoint(y, polynomial)
    last = result.rows - 1
    for input_row in range(8):
        coefficient = red(bra[input_row] / bra[0], polynomial)
        real, imag = split_fixed(coefficient, polynomial)
        result[last, 2 * (8 * input_row)] = imag
        result[last, 2 * (8 * input_row) + 1] = real
    return result


@dataclass(frozen=True)
class AdmissibleSpaceCertificate:
    descent_ranks: tuple[tuple[int, ...], ...]
    real_descent_ranks: tuple[tuple[int, ...], ...]
    adjoint_ranks: tuple[tuple[int, ...], ...]
    descent_dimensions: tuple[tuple[int, ...], ...]
    adjoint_dimensions: tuple[tuple[int, ...], ...]
    projector_witnesses_descend: bool
    projector_witnesses_not_intertwiners: bool


def admissible_space_certificate(
    sector_packages: tuple[tuple[object, ...], ...]
) -> AdmissibleSpaceCertificate:
    descent_rank_rows: list[tuple[int, ...]] = []
    real_descent_rank_rows: list[tuple[int, ...]] = []
    adjoint_rank_rows: list[tuple[int, ...]] = []
    projector_descents: list[bool] = []
    projector_nonintertwiners: list[bool] = []
    for sectors in sector_packages:
        descent_ranks: list[int] = []
        real_descent_ranks: list[int] = []
        adjoint_ranks: list[int] = []
        for sector in sectors:
            polynomial = sector.polynomial
            y = field_matrix(sector.y, polynomial)
            bra = block119.field_adjoint(y, polynomial)
            norm = red((bra * y)[0], polynomial)
            rank_one = field_matrix(y * bra / norm, polynomial)
            complement = field_matrix(sp.eye(8) - rank_one, polynomial)

            descent_system = descent_constraints(y, polynomial)
            descent_minor = descent_system[:, tuple(range(1, 8))]
            descent_ranks.append(
                7
                if field_equal(descent_minor, sp.eye(7), polynomial)
                else field_rank(descent_system, polynomial)
            )

            real_descent_system = realify(descent_system, polynomial)
            real_pivots = tuple(
                coordinate
                for column in range(1, 8)
                for coordinate in (2 * column, 2 * column + 1)
            )
            real_descent_minor = real_descent_system[:, real_pivots]
            real_descent_ranks.append(
                14
                if field_equal(real_descent_minor, sp.eye(14), polynomial)
                else field_rank(real_descent_system, polynomial)
            )

            adjoint_system = adjoint_constraints(y, polynomial)
            adjoint_minor = adjoint_system[:, real_pivots + (1,)]
            adjoint_ranks.append(
                15
                if field_equal(adjoint_minor, sp.eye(15), polynomial)
                else field_rank(adjoint_system, polynomial)
            )
            projector_descents.append(
                field_equal(bra * rank_one * complement, sp.zeros(1, 8), polynomial)
                and field_equal(rank_one * rank_one, rank_one, polynomial)
                and field_equal(rank_one * y, y, polynomial)
            )
            projector_nonintertwiners.append(
                not field_equal(
                    rank_one * field_matrix(sector.x, polynomial),
                    y,
                    polynomial,
                )
            )
        descent_rank_rows.append(tuple(descent_ranks))
        real_descent_rank_rows.append(tuple(real_descent_ranks))
        adjoint_rank_rows.append(tuple(adjoint_ranks))

    descent_rank_tuple = tuple(descent_rank_rows)
    adjoint_rank_tuple = tuple(adjoint_rank_rows)
    return AdmissibleSpaceCertificate(
        descent_ranks=descent_rank_tuple,
        real_descent_ranks=tuple(real_descent_rank_rows),
        adjoint_ranks=adjoint_rank_tuple,
        descent_dimensions=tuple(
            tuple(64 - rank for rank in row) for row in descent_rank_tuple
        ),
        adjoint_dimensions=tuple(
            tuple(128 - rank for rank in row) for row in adjoint_rank_tuple
        ),
        projector_witnesses_descend=all(projector_descents),
        projector_witnesses_not_intertwiners=all(projector_nonintertwiners),
    )


@dataclass(frozen=True)
class FixturePackage:
    shear: sp.Rational
    sectors: tuple[object, ...]
    thetas: tuple[sp.Matrix, ...]
    routings: tuple[object, ...]


def fixture_packages() -> tuple[FixturePackage, ...]:
    packages: list[FixturePackage] = []
    for shear in SHEARS:
        sectors = tuple(block119.make_sectors(shear))
        completion = block119.reflection_real_completion(sectors)
        current = block121.certify_current(shear)
        if len(sectors) != 4 or len(completion.thetas) != 4:
            raise AssertionError("each fixture must have four momentum sectors")
        packages.append(
            FixturePackage(
                shear=shear,
                sectors=sectors,
                thetas=tuple(completion.thetas),
                routings=tuple(current.routings),
            )
        )
    return tuple(packages)


MOMENTUM_INDICES = tuple(
    tuple(momentum + 4 * time_index for time_index in range(8))
    for momentum in range(4)
)
WEIGHT_SUM_MAP = sp.Matrix(
    (
        (1, 1, 1, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 1, 1, 1),
    )
)


def zero_sum_kernel_basis() -> sp.Matrix:
    identity = sp.eye(8)
    return sp.Matrix.hstack(
        *(identity.col(index) - identity.col(3) for index in range(3)),
        *(identity.col(4 + index) - identity.col(7) for index in range(3)),
    )


def momentum_diagonal_blocks(
    operator: sp.Matrix, transform: sp.Matrix, cut: sp.Matrix
) -> tuple[sp.Matrix, ...]:
    transformed = (transform.H * operator * transform).applyfunc(sp.expand)
    return tuple(
        (
            cut
            * transformed.extract(
                MOMENTUM_INDICES[momentum], MOMENTUM_INDICES[momentum]
            )
            * cut.T
        ).applyfunc(sp.expand)
        for momentum in range(4)
    )


def flattened(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(tuple(sp.Matrix(matrix)))


def family_descent_constraints(
    y: sp.Matrix,
    family: tuple[sp.Matrix, ...],
    polynomial: sp.Poly,
) -> sp.Matrix:
    """Weight constraints obtained directly from momentum-diagonal blocks."""
    bra = block119.field_adjoint(y, polynomial)
    columns: list[sp.Matrix] = []
    for operator in family:
        row = field_matrix(bra * operator, polynomial)
        columns.append(
            sp.Matrix(
                tuple(
                    red(
                        row[output] * bra[0] - row[0] * bra[output],
                        polynomial,
                    )
                    for output in range(1, 8)
                )
            )
        )
    return field_matrix(sp.Matrix.hstack(*columns), polynomial)


@dataclass(frozen=True)
class DressingCertificate:
    spatial_shift_scalar_blocks: bool
    arbitrary_operator_cancellation: bool
    routed_translate_identity: bool
    entrywise_invisibility: bool
    theta_involutions: bool
    collapse_factorization: bool
    effective_parameter_ranks: tuple[int, ...]
    collapsed_descent_ranks: tuple[int, ...]
    naive_eight_weight_ranks: tuple[int, ...]
    kernel_dimensions: tuple[int, ...]
    kernel_exact: bool
    kernel_blocks_zero: bool
    no_nonzero_descent: bool
    time_visible: bool
    case_count: int
    constraint_digest: str


def dressing_certificate(
    packages: tuple[FixturePackage, ...]
) -> DressingCertificate:
    transform = block123.spatial_fourier()
    cut = block119.cut_shift()
    spatial_shift = block123.spatial_shift()
    time_shift = block123.antiperiodic_time_shift()
    expected_shift = sp.diag(*(I ** (index % 4) for index in range(32)))
    transformed_shift = (transform.H * spatial_shift * transform).applyfunc(
        sp.expand
    )
    spatial_shift_scalar_blocks = (
        matrix_zero(transform.H * transform - sp.eye(32))
        and matrix_zero(spatial_shift.T * spatial_shift - sp.eye(32))
        and matrix_zero(transformed_shift - expected_shift)
    )

    arbitrary_entries = sp.symbols("arbitrary0:64")
    arbitrary = sp.Matrix(8, 8, arbitrary_entries)
    arbitrary_operator_cancellation = all(
        matrix_zero(
            (
                (I ** momentum * sp.eye(8)) ** power
                * arbitrary
                * (I ** momentum * sp.eye(8)) ** (-power)
                - arbitrary
            ).applyfunc(sp.simplify)
        )
        for momentum in range(4)
        for power in range(1, 4)
    )

    kernel_basis = zero_sum_kernel_basis()
    kernel_basis_exact = (
        WEIGHT_SUM_MAP.rank() == 2
        and kernel_basis.rank() == 6
        and matrix_zero(WEIGHT_SUM_MAP * kernel_basis)
    )
    routed_translate_flags: list[bool] = []
    invisibility_flags: list[bool] = []
    theta_flags: list[bool] = []
    collapse_flags: list[bool] = []
    effective_ranks: list[int] = []
    collapsed_ranks: list[int] = []
    naive_ranks: list[int] = []
    kernel_dimensions: list[int] = []
    kernel_flags: list[bool] = []
    kernel_block_flags: list[bool] = []
    no_nonzero_flags: list[bool] = []
    time_visibility_flags: list[bool] = []
    constraint_payload: list[sp.Matrix] = []

    for package in packages:
        for routing in package.routings:
            base_density = routing.temporal[block121.site(7, 0)]
            routed_densities = tuple(
                routing.temporal[block121.site(7, spatial_site)]
                for spatial_site in range(4)
            )
            routed_translate_flags.extend(
                matrix_zero(
                    routed_densities[power]
                    - spatial_shift**power
                    * base_density
                    * spatial_shift.T**power
                )
                for power in range(4)
            )
            plain_orbit = tuple(
                momentum_diagonal_blocks(density, transform, cut)
                for density in routed_densities
            )
            time_translated = momentum_diagonal_blocks(
                time_shift * base_density * time_shift.T,
                transform,
                cut,
            )

            for momentum, sector in enumerate(package.sectors):
                polynomial = sector.polynomial
                plain = tuple(
                    field_matrix(orbit[momentum], polynomial)
                    for orbit in plain_orbit
                )
                density = plain[0]
                invisibility_flags.extend(
                    field_equal(plain[power], density, polynomial)
                    for power in range(1, 4)
                )
                theta = field_matrix(package.thetas[momentum], polynomial)
                theta_flags.append(
                    field_equal(theta * theta, sp.eye(8), polynomial)
                )
                conjugated = field_matrix(theta * density * theta, polynomial)
                full_family = plain + (conjugated,) * 4
                collapsed_family = (density, conjugated)

                full_map = field_matrix(
                    sp.Matrix.hstack(
                        *(flattened(operator) for operator in full_family)
                    ),
                    polynomial,
                )
                collapsed_map = field_matrix(
                    sp.Matrix.hstack(
                        *(flattened(operator) for operator in collapsed_family)
                    ),
                    polynomial,
                )
                collapse_flags.append(
                    field_equal(
                        full_map,
                        collapsed_map * WEIGHT_SUM_MAP,
                        polynomial,
                    )
                )
                effective_rank = field_rank(collapsed_map, polynomial)
                effective_ranks.append(effective_rank)

                collapsed_constraints = family_descent_constraints(
                    field_matrix(sector.y, polynomial),
                    collapsed_family,
                    polynomial,
                )
                naive_constraints = family_descent_constraints(
                    field_matrix(sector.y, polynomial),
                    full_family,
                    polynomial,
                )
                constraint_payload.append(naive_constraints)
                collapsed_rank = field_rank(collapsed_constraints, polynomial)
                naive_rank = field_rank(naive_constraints, polynomial)
                collapsed_ranks.append(collapsed_rank)
                naive_ranks.append(naive_rank)
                kernel_dimensions.append(8 - naive_rank)
                factors_exactly = field_equal(
                    naive_constraints,
                    collapsed_constraints * WEIGHT_SUM_MAP,
                    polynomial,
                )
                kernel_flags.append(
                    kernel_basis_exact
                    and factors_exactly
                    and naive_rank == 2
                    and field_equal(
                        naive_constraints * kernel_basis,
                        sp.zeros(naive_constraints.rows, 6),
                        polynomial,
                    )
                )
                kernel_block_flags.append(
                    field_equal(
                        full_map * kernel_basis,
                        sp.zeros(full_map.rows, 6),
                        polynomial,
                    )
                )
                no_nonzero_flags.append(
                    effective_rank == 2
                    and collapsed_rank == 2
                    and naive_rank == 2
                    and factors_exactly
                )
                time_visibility_flags.append(
                    not matrix_zero(
                        plain_orbit[0][momentum]
                        - time_translated[momentum]
                    )
                )

    return DressingCertificate(
        spatial_shift_scalar_blocks=spatial_shift_scalar_blocks,
        arbitrary_operator_cancellation=arbitrary_operator_cancellation,
        routed_translate_identity=all(routed_translate_flags),
        entrywise_invisibility=all(invisibility_flags),
        theta_involutions=all(theta_flags),
        collapse_factorization=all(collapse_flags),
        effective_parameter_ranks=tuple(effective_ranks),
        collapsed_descent_ranks=tuple(collapsed_ranks),
        naive_eight_weight_ranks=tuple(naive_ranks),
        kernel_dimensions=tuple(kernel_dimensions),
        kernel_exact=all(kernel_flags),
        kernel_blocks_zero=all(kernel_block_flags),
        no_nonzero_descent=all(no_nonzero_flags),
        time_visible=all(time_visibility_flags),
        case_count=len(naive_ranks),
        constraint_digest=exact_digest(tuple(constraint_payload)),
    )


N5_LINES = (
    "N5: per_element: scalar-phase cancellation, diagonal-block equality, family-factorization, corrected-rank-two, zero-sum-kernel, zero-compression, admissible-space-dimension, time-visibility, and catch certificates are checked",
    "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus",
    "per_mode: at fixed momentum every spatial shift is a scalar phase that cancels under conjugation, so all spatial translates have the same momentum-diagonal block",
    "per_block: the displayed eight-weight smeared-and-conjugated family collapses to two effective weight-sums whose descent kernel is exactly the zero-sum subspace compressing to the zero observable; no nonzero-compression member descends",
    "lattice_wide: checked and not executed — time-smeared and transfer-conjugated dressings for the observable wall, the naturality classification, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient beyond the displayed carrier, Records, audit retention, and TOE closure remain open",
)

SCOPE_KEYS = (
    "invisibility",
    "scalar_phase",
    "collapse",
    "zero_observable",
    "structural_powerlessness",
    "rank_one_geometry",
    "nonconflation",
    "time_smeared_live",
    "counterterm_inference",
    "catch_record",
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
        "invisibility": (
            "invisibility" in note or "invisible to the quotient" in note
        ),
        "scalar_phase": (
            "scalar phase" in note or "cancels under conjugation" in note
        ),
        "collapse": (
            "collapses to two effective parameters" in note
            or "two weight-sums" in note
        ),
        "zero_observable": (
            "zero observable" in note or "compresses to zero" in note
        ),
        "structural_powerlessness": (
            "structurally powerless" in note
            or "structural, not delicate" in note
            or "for a structural reason" in note
        ),
        "rank_one_geometry": (
            "rank-one geometry" in note or "n^2 - (n-1)" in note
        ),
        "nonconflation": (
            "not conflated" in note
            or "different subspaces" in note
            or "non-conflation" in note
            or "without conflat" in note
        ),
        "time_smeared_live": "time-smeared" in note and "live" in note,
        "counterterm_inference": (
            "plausible inference" in note
            or "not forced" in note
            or "an inference, not a theorem" in note
        ),
        "catch_record": "refuted" in note or "corrected" in note,
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started = time.monotonic()
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-authority",
        "Block 124 note/runner/cache and ancestors 123--103 are pinned",
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_DRESSING_INVISIBILITY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SOURCED_QUOTIENT_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "scripts/admissibility_dirac_kahler_sourced_quotient_execution_2026_08_17.py",
            "logs/runner-cache/admissibility_dirac_kahler_sourced_quotient_execution_2026_08_17.txt",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(
            authority[f"ancestor_{number}"] for number in range(103, 124)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    packages = fixture_packages()
    dressing = dressing_certificate(packages)
    spaces = admissible_space_certificate(
        tuple(package.sectors for package in packages)
    )
    note_scope = scope_certificate(normalized_note(), mutation)

    invisibility_exact = (
        dressing.spatial_shift_scalar_blocks
        and dressing.arbitrary_operator_cancellation
        and dressing.routed_translate_identity
        and dressing.entrywise_invisibility
        and dressing.case_count == 16
    )
    if mutation == "break_invisibility_lemma":
        invisibility_exact = False
    checks.check(
        "B-the-invisibility-lemma",
        "[U_x]kk=i^k I8, so conjugation cancels for every operator; w=1,2,3 is entrywise invisible for every routed density and momentum",
        invisibility_exact,
    )

    collapse_exact = (
        dressing.theta_involutions
        and dressing.collapse_factorization
        and dressing.effective_parameter_ranks == (2,) * dressing.case_count
    )
    if mutation == "break_collapse":
        collapse_exact = False
    checks.check(
        "C-the-family-collapse",
        "the eight weights factor exactly through the plain and Theta-conjugated weight sums, giving two effective parameters",
        collapse_exact,
    )

    rank_two_exact = (
        dressing.collapsed_descent_ranks == (2,) * dressing.case_count
        and dressing.naive_eight_weight_ranks == (2,) * dressing.case_count
        and dressing.kernel_dimensions == (6,) * dressing.case_count
        and dressing.kernel_exact
    )
    if mutation == "break_rank_two":
        rank_two_exact = False
    zero_descent_exact = (
        dressing.kernel_blocks_zero and dressing.no_nonzero_descent
    )
    if mutation == "claim_nonzero_descent":
        zero_descent_exact = False
    checks.check(
        "D-the-wall-extension",
        "rank=2 and ker=the six zero-sum directions; every descended weight vector has identically zero momentum blocks and zero quotient compression",
        rank_two_exact and zero_descent_exact,
    )

    dimensions_exact = (
        spaces.descent_ranks == ((7,) * 4,) * 2
        and spaces.real_descent_ranks == ((14,) * 4,) * 2
        and spaces.adjoint_ranks == ((15,) * 4,) * 2
        and spaces.descent_dimensions == ((57,) * 4,) * 2
        and spaces.adjoint_dimensions == ((113,) * 4,) * 2
    )
    if mutation == "break_dimension_counts":
        dimensions_exact = False
    nonconflation_exact = (
        spaces.projector_witnesses_descend
        and spaces.projector_witnesses_not_intertwiners
    )
    if mutation == "claim_same_spaces":
        nonconflation_exact = False
    checks.check(
        "E-the-admissible-spaces",
        "descent has rank 7 and dim_F 57; adjointness adds one real condition to rank 14, giving dim_real 113; P_y proves non-conflation with x->y intertwiners",
        dimensions_exact and nonconflation_exact,
    )

    time_visibility_exact = dressing.time_visible
    if mutation == "break_time_visibility":
        time_visibility_exact = False
    counterterm_is_inference = note_scope["counterterm_inference"]
    if mutation == "claim_counterterm_theorem":
        counterterm_is_inference = False
    checks.check(
        "F-the-scope-split",
        "spatial smearing is structurally powerless, while every tested T J T^-1 diagonal block differs from J; time-smeared dressings remain live and counterterms are only an inference",
        time_visibility_exact and counterterm_is_inference,
    )

    refutation_exact = (
        dressing.case_count == 16
        and dressing.naive_eight_weight_ranks == (2,) * 16
        and dressing.kernel_dimensions == (6,) * 16
        and note_scope["catch_record"]
    )
    if mutation == "break_refutation_record":
        refutation_exact = False
    checks.check(
        "G-the-catch-record",
        "the naive full-eight-weight diagonal-block constraint matrix has rank 2, not the refuted rank 8, and kernel dimension 6",
        refutation_exact,
    )

    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "required invisibility/collapse/wall/non-conflation/time-live/catch/N1--N8/W1/N5 firewalls and runtime bound are present",
        set(note_scope) == set(SCOPE_KEYS)
        and all(note_scope.values())
        and elapsed_before_scope <= 400,
    )

    print(
        "LEMMA: [U_x]_{kk}=i^k I_8, hence (i^k I_8)^w A (i^k I_8)^(-w)=A for every operator A and every integer w."
    )
    print(
        "FAMILY: 16 routed momentum cases factor through two weight-sums; descent rank=2, kernel dimension=6, zero-block compression; constraint sha="
        f"{dressing.constraint_digest}."
    )
    print(
        "ADMISSIBLE SPACES: every k in both fixtures has ranks 7/14/15 and dimensions 57 complex, 114 before adjoint reality, 113 real after it; P_y is the separating witness."
    )
    print(
        "TIME VISIBILITY: T J T^-1 differs entrywise from J on every tested momentum-diagonal block; the time-smeared class is live."
    )
    for line in N5_LINES:
        print(line)
    print(
        "RESULT: spatial dressing cannot pierce the observable wall because the quotient is blind to it — the family collapses to two parameters compressing to zero — while the time direction is provably visible, making time-smeared dressings the live route"
    )
    print(
        "DECISION_CUT: advance time-smeared/transfer-conjugated dressings and the naturality classification; reject further spatial-smearing constructions"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves"
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
