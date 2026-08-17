#!/usr/bin/env python3
"""Block 123: exact momentum-population definiteness split.

The committed Block 122 quotient-observable obstruction is transferred to
the spatial-shift current, while the closed-carrier Gauss population test is
repeated for the indefinite principal Z4 momentum charge.  Every scientific
calculation uses exact SymPy arithmetic; wall-clock timing is the sole
floating-point quantity.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
from pathlib import Path
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_quotient_observable_obstruction_2026_08_16 as prior


R = sp.Rational
I = sp.I
block121 = prior.prior
block120 = block121.prior
block119 = block120.prior
DK = prior.DK
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_POPULATION_DEFINITENESS_"
    "BOUNDED_THEOREM_NOTE_2026-08-16.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_"
    "BOUNDED_THEOREM_NOTE_2026-08-16.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_quotient_observable_obstruction_"
    "2026_08_16.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_quotient_observable_"
    "obstruction_2026_08_16.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_POPULATION_DEFINITENESS_BOUNDED_THEOREM_NOTE_2026-08-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md",
    "scripts/admissibility_dirac_kahler_quotient_observable_obstruction_2026_08_16.py",
    "logs/runner-cache/admissibility_dirac_kahler_quotient_observable_obstruction_2026_08_16.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "31e4c7ff7d41db6a78feef19dba2bfbea3dc1830"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block122-quotient-observable-obstruction-20260816"
)
PARENT_COMMIT = "f067b99be7eb49fc46ea8dffccab5e20e6052d88"
PARENT_NOTE_BLOB = "ef9f1b2037c8b470c821ed27572a81c6cb9ac9a4"
PARENT_RUNNER_BLOB = "08eeb0b1742cbf1c33646cda7993835423d8f357"
PARENT_CACHE_BLOB = "5f303dcfa39eb23c407d363464ae308bfa1de30a"
ANCESTOR_COMMITS = (
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
    "break_shift_commutation",
    "break_phase_reduction",
    "break_definiteness",
    "claim_eigenstate",
    "break_gauss_image",
    "claim_u1_populates",
    "break_pin_transfer",
    "claim_slice_energy",
    "claim_energy_content",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_toe_progress",
    "claim_axiom_amendment",
)

NT = prior.NT
NX = prior.NX
NS = prior.NS
SHEARS = prior.SHEARS


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


def matrix_zero(matrix: sp.Matrix) -> bool:
    return all(sp.expand(value) == 0 for value in matrix)


def exact_digest(*payload: object) -> str:
    return hashlib.sha256(sp.srepr(payload).encode("utf-8")).hexdigest()[:16]


def spatial_shift() -> sp.ImmutableSparseMatrix:
    """Active +x shift U_x|t,x>=|t,x+1>."""
    return sp.ImmutableSparseMatrix(
        NS,
        NS,
        {
            (block121.site(time_index, space_index + 1),
             block121.site(time_index, space_index)): 1
            for time_index in range(NT)
            for space_index in range(NX)
        },
    )


def antiperiodic_time_shift() -> sp.ImmutableSparseMatrix:
    """Active one-microslice shift with the exact antiperiodic seam sign."""
    entries: dict[tuple[int, int], int] = {}
    for time_index in range(NT):
        sign = -1 if time_index == NT - 1 else 1
        for space_index in range(NX):
            entries[
                (
                    block121.site(time_index + 1, space_index),
                    block121.site(time_index, space_index),
                )
            ] = sign
    return sp.ImmutableSparseMatrix(NS, NS, entries)


def spatial_fourier() -> sp.Matrix:
    fourier = sp.Matrix(
        NX, NX, lambda row, column: I ** (-row * column)
    ) / 2
    return sp.kronecker_product(sp.eye(NT), fourier)


def momentum_cross_block(
    matrix: sp.Matrix,
    row_momentum: int,
    column_momentum: int,
    transform: sp.Matrix,
) -> sp.Matrix:
    row_indices = tuple(row_momentum + NX * time for time in range(NT))
    column_indices = tuple(
        column_momentum + NX * time for time in range(NT)
    )
    return (transform.H * matrix * transform).extract(
        row_indices, column_indices
    )


def transformed_momentum_block(
    transformed: sp.Matrix,
    row_momentum: int,
    column_momentum: int | None = None,
) -> sp.Matrix:
    if column_momentum is None:
        column_momentum = row_momentum
    row_indices = tuple(row_momentum + NX * time for time in range(NT))
    column_indices = tuple(
        column_momentum + NX * time for time in range(NT)
    )
    return transformed.extract(row_indices, column_indices)


def principal_charge(phase: sp.Expr) -> int:
    """Invert i**p on the principal integer representatives {-1,0,1,2}."""
    candidates = tuple(
        value for value in (-1, 0, 1, 2) if sp.expand(I**value - phase) == 0
    )
    if len(candidates) != 1:
        raise AssertionError(f"phase {phase!r} lacks a unique principal charge")
    return candidates[0]


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


MatrixGrid = tuple[tuple[sp.Matrix, ...], ...]
ValueGrid = tuple[tuple[sp.Expr, ...], ...]


@dataclass(frozen=True)
class FixtureCertificate:
    shear: sp.Rational
    shift_commutation_exact: bool
    routed_identity_exact: bool
    routing_distinct: bool
    seam_exact: bool
    phase_structure_exact: bool
    phase_reduction_exact: bool
    quotient_positive_exact: bool
    phase_form: sp.Matrix
    momentum_form: sp.Matrix
    pin_transfer_exact: bool
    residual_zero_counts: tuple[int, ...]
    residual_digests: tuple[str, ...]
    density_descent_left: tuple[int, ...]
    density_descent_right: tuple[int, ...]
    flux_descent_left: tuple[int, ...]
    flux_descent_right: tuple[int, ...]
    adjoint_density: tuple[int, ...]
    adjoint_flux: tuple[int, ...]
    time_shift_nnz: int
    time_shift_digest: str
    scalar_transfer_exact: bool
    conservation_vacuous: bool
    contractivity_pinned: bool
    interval_digest: str


@dataclass(frozen=True)
class DefinitenessCertificate:
    u1_total_identity: bool
    u1_definite_norm: bool
    phase_form_exact: bool
    momentum_form_exact: bool
    momentum_indefinite: bool
    witness_nonzero: bool
    witness_positive: bool
    integer_sum: sp.Expr
    integer_expectation: sp.Expr
    modular_sum: int
    momentum_action: sp.Matrix
    not_eigenstate: bool


@dataclass(frozen=True)
class GaussCertificate:
    divergence: sp.Matrix
    image_zero_sum_exact: bool
    momentum_constraint_row: sp.Matrix
    source: sp.Matrix
    solution: sp.Matrix
    solution_exact: bool
    momentum_population_passes: bool
    u1_population_fails: bool


def restricted_block(
    kernel: sp.Matrix,
    momentum: int,
    transform: sp.Matrix,
    cut: sp.Matrix,
    polynomial: sp.Poly,
) -> sp.Matrix:
    return block120.field_matrix(
        prior.momentum_restriction(
            kernel, momentum, transform, cut, polynomial
        ),
        polynomial,
    )


def transformed_kernels(
    kernels: tuple[sp.Matrix, ...], transform: sp.Matrix
) -> tuple[sp.Matrix, ...]:
    """Fourier-conjugate each local kernel once, before the four k reads."""
    return tuple(transform.H * kernel * transform for kernel in kernels)


def observable_grid_from_transformed(
    kernels: tuple[sp.Matrix, ...],
    momentum: int,
    cut: sp.Matrix,
    polynomial: sp.Poly,
    bra: sp.Matrix,
    vector: sp.Matrix,
    norm: sp.Expr,
) -> tuple[MatrixGrid, ValueGrid]:
    block_rows: list[tuple[sp.Matrix, ...]] = []
    value_rows: list[tuple[sp.Expr, ...]] = []
    for local_time in range(NT):
        old_time = (local_time + NT // 2) % NT
        blocks: list[sp.Matrix] = []
        values: list[sp.Expr] = []
        for space_index in range(NX):
            diagonal = transformed_momentum_block(
                kernels[block121.site(old_time, space_index)], momentum
            )
            block = block120.field_matrix(
                cut * diagonal * cut.T, polynomial
            )
            blocks.append(block)
            values.append(
                prior.compression(bra, vector, block, norm, polynomial)
            )
        block_rows.append(tuple(blocks))
        value_rows.append(tuple(values))
    return tuple(block_rows), tuple(value_rows)


def descent_counts(
    blocks: MatrixGrid,
    values: ValueGrid,
    bra: sp.Matrix,
    vector: sp.Matrix,
    polynomial: sp.Poly,
) -> tuple[int, int]:
    left = 0
    right = 0
    for local_time in range(NT):
        for space_index in range(NX):
            operator = blocks[local_time][space_index]
            scalar = values[local_time][space_index]
            left += block120.field_equal(
                block120.field_matrix(bra * operator, polynomial),
                block120.field_matrix(scalar * bra, polynomial),
                polynomial,
            )
            right += block120.field_equal(
                block120.field_matrix(operator * vector, polynomial),
                block120.field_matrix(scalar * vector, polynomial),
                polynomial,
            )
    return left, right


def adjoint_count(
    name: str,
    blocks: MatrixGrid,
    gram: sp.Matrix,
    polynomial: sp.Poly,
) -> int:
    zeros = 0
    for local_time in range(NT):
        reflected_time = prior.momentum_reflect_time(name, local_time)
        for space_index in range(NX):
            operator = blocks[local_time][space_index]
            reflected = blocks[reflected_time][space_index]
            residual = block120.field_matrix(
                gram * operator
                - block120.field_adjoint(reflected, polynomial) * gram,
                polynomial,
            )
            zeros += block120.field_equal(
                residual, sp.zeros(NT), polynomial
            )
    return zeros


def quotient_positivity(
    sector,
    theta: sp.Matrix,
) -> bool:
    polynomial = sector.polynomial
    vector = sector.y
    bra = block120.field_adjoint(vector, polynomial)
    norm = block120.red((bra * vector)[0], polynomial)
    gram = block120.field_matrix(theta * sector.h00, polynomial)
    rank_one = block120.field_matrix(vector * bra, polynomial)
    if norm == 0 or not block120.field_equal(gram, rank_one, polynomial):
        return False
    unit = block120.field_matrix(vector / norm, polynomial)
    unit_bra = block120.field_adjoint(unit, polynomial)
    return block120.red((unit_bra * gram * unit)[0] - 1, polynomial) == 0


def make_shift_routings(
    shifted_action: sp.Matrix,
) -> tuple[block121.RoutedCurrent, ...]:
    routed: list[block121.RoutedCurrent] = []
    for routing in block121.ROUTINGS:
        temporal, spatial = block121.current_kernels(shifted_action, routing)
        identity_exact = all(
            matrix_zero(
                block121.backward_divergence(
                    temporal, spatial, time_index, space_index
                )
                - (
                    block121.projector(block121.site(time_index, space_index))
                    * shifted_action
                    - shifted_action
                    * block121.projector(block121.site(time_index, space_index))
                )
            )
            for time_index in range(NT)
            for space_index in range(NX)
        )
        routed.append(
            block121.RoutedCurrent(
                routing, temporal, spatial, identity_exact
            )
        )
    return tuple(routed)


def fixture_certificate(
    shear: sp.Rational,
    fixture_index: int,
    shift: sp.Matrix,
    transform: sp.Matrix,
    cut: sp.Matrix,
    time_shift: sp.Matrix,
) -> FixtureCertificate:
    current = block121.certify_current(shear)
    action = current.action
    shifted_action = shift * action
    shift_commutation_exact = (
        matrix_zero(shift.H * shift - sp.eye(NS))
        and matrix_zero(shift**NX - sp.eye(NS))
        and matrix_zero(shift * action - action * shift)
        and matrix_zero(shifted_action - shift * action)
        and matrix_zero(shifted_action - action * shift)
    )

    shift_routings = make_shift_routings(shifted_action)
    _, curl_exact, routing_distinct = block121.curl_reconstruction(
        shift_routings[0], shift_routings[1]
    )
    routed_identity_exact = (
        len(shift_routings) == 2
        and all(routed.identity_exact for routed in shift_routings)
        and curl_exact
    )
    seam_exact = all(
        matrix_zero(
            block121.backward_divergence(
                routed.temporal,
                routed.spatial,
                time_index,
                space_index,
            )
            - (
                block121.projector(block121.site(time_index, space_index))
                * shifted_action
                - shifted_action
                * block121.projector(block121.site(time_index, space_index))
            )
        )
        for routed in shift_routings
        for time_index in range(NT)
        for space_index in range(NX)
        if time_index == 0 or space_index == 0
    )

    transformed_shift = transform.H * shift * transform
    transformed_action = transform.H * action * transform
    transformed_shifted = transform.H * shifted_action * transform
    expected_phases = tuple(I**momentum for momentum in range(NX))
    expected_shift = sp.kronecker_product(
        sp.eye(NT), sp.diag(*expected_phases)
    )
    phase_structure_exact = (
        matrix_zero(transform.H * transform - sp.eye(NS))
        and matrix_zero(transformed_shift - expected_shift)
        and all(
            matrix_zero(
                transformed_momentum_block(
                    transformed_action, row_momentum, column_momentum
                )
            )
            and matrix_zero(
                transformed_momentum_block(
                    transformed_shifted, row_momentum, column_momentum
                )
            )
            for row_momentum in range(NX)
            for column_momentum in range(NX)
            if row_momentum != column_momentum
        )
        and all(
            matrix_zero(
                transformed_momentum_block(transformed_shifted, momentum)
                - I**momentum
                * transformed_momentum_block(transformed_action, momentum)
            )
            for momentum in range(NX)
        )
    )

    phase_reduction_exact = True
    for time_index in range(NT):
        for space_index in range(NX):
            projector = block121.projector(
                block121.site(time_index, space_index)
            )
            transformed_projector = transform.H * projector * transform
            transformed_shifted_residual = (
                transformed_projector * transformed_shifted
                - transformed_shifted * transformed_projector
            )
            transformed_u1_residual = (
                transformed_projector * transformed_action
                - transformed_action * transformed_projector
            )
            for momentum in range(NX):
                phase_reduction_exact = (
                    phase_reduction_exact
                    and matrix_zero(
                        transformed_momentum_block(
                            transformed_shifted_residual, momentum
                        )
                        - I**momentum
                        * transformed_momentum_block(
                            transformed_u1_residual, momentum
                        )
                    )
                )

    sectors = block119.make_sectors(shear)
    completion = block119.reflection_real_completion(sectors)
    if len(sectors) != NX or len(completion.thetas) != NX:
        raise AssertionError("the completed quotient must contain four lines")
    quotient_positive_exact = all(
        quotient_positivity(sector, completion.thetas[momentum])
        for momentum, sector in enumerate(sectors)
    )

    phase_values: list[sp.Expr] = []
    for momentum, sector in enumerate(sectors):
        polynomial = sector.polynomial
        shift_block = restricted_block(
            shift, momentum, transform, cut, polynomial
        )
        phase_value = prior.quotient_element(
            sector.y, shift_block, polynomial
        )
        phase_structure_exact = (
            phase_structure_exact
            and block120.red(
                phase_value - I**momentum, polynomial
            )
            == 0
        )
        phase_values.append(phase_value)
    phase_form = sp.diag(*phase_values)
    charges = tuple(principal_charge(value) for value in phase_values)
    momentum_form = sp.diag(*charges)
    momentum_operator = (
        transform
        * sp.kronecker_product(sp.eye(NT), momentum_form)
        * transform.H
    )
    phase_structure_exact = (
        phase_structure_exact
        and matrix_zero(phase_form - sp.diag(1, I, -1, -I))
        and charges == (0, 1, 2, -1)
        and matrix_zero(momentum_operator.H - momentum_operator)
        and matrix_zero(momentum_operator * shift - shift * momentum_operator)
        and matrix_zero(momentum_operator * action - action * momentum_operator)
    )
    for momentum, sector in enumerate(sectors):
        polynomial = sector.polynomial
        momentum_block = restricted_block(
            momentum_operator, momentum, transform, cut, polynomial
        )
        momentum_value = prior.quotient_element(
            sector.y, momentum_block, polynomial
        )
        phase_structure_exact = (
            phase_structure_exact
            and block120.red(
                momentum_value - charges[momentum], polynomial
            )
            == 0
        )

    residual_zero_counts: list[int] = []
    residual_digests: list[str] = []
    density_descent_left: list[int] = []
    density_descent_right: list[int] = []
    flux_descent_left: list[int] = []
    flux_descent_right: list[int] = []
    adjoint_density: list[int] = []
    adjoint_flux: list[int] = []
    pin_transfer_exact = True
    u1_routing = current.routings[0]
    shift_routing = shift_routings[0]
    transformed_u1_kernels = {
        "J": transformed_kernels(u1_routing.temporal, transform),
        "S": transformed_kernels(u1_routing.spatial, transform),
    }
    transformed_shift_kernels = {
        "J": transformed_kernels(shift_routing.temporal, transform),
        "S": transformed_kernels(shift_routing.spatial, transform),
    }

    for momentum, sector in enumerate(sectors):
        polynomial = sector.polynomial
        vector = sector.y
        bra = block120.field_adjoint(vector, polynomial)
        norm = block120.red((bra * vector)[0], polynomial)
        gram = block120.field_matrix(
            completion.thetas[momentum] * sector.h00, polynomial
        )
        u1_grids: dict[str, tuple[MatrixGrid, ValueGrid]] = {}
        shift_grids: dict[str, tuple[MatrixGrid, ValueGrid]] = {}
        for name in ("J", "S"):
            u1_grids[name] = observable_grid_from_transformed(
                transformed_u1_kernels[name],
                momentum,
                cut,
                polynomial,
                bra,
                vector,
                norm,
            )
            shift_grids[name] = observable_grid_from_transformed(
                transformed_shift_kernels[name],
                momentum,
                cut,
                polynomial,
                bra,
                vector,
                norm,
            )

        u1_j_blocks, u1_j_values = u1_grids["J"]
        u1_s_blocks, u1_s_values = u1_grids["S"]
        shift_j_blocks, shift_j_values = shift_grids["J"]
        shift_s_blocks, shift_s_values = shift_grids["S"]
        residuals: list[sp.Expr] = []
        for local_time in range(NT):
            for space_index in range(NX):
                shifted_divergence = block120.field_matrix(
                    shift_j_blocks[local_time][space_index]
                    - shift_j_blocks[(local_time - 1) % NT][space_index]
                    + shift_s_blocks[local_time][space_index]
                    - shift_s_blocks[local_time][(space_index - 1) % NX],
                    polynomial,
                )
                u1_divergence = block120.field_matrix(
                    u1_j_blocks[local_time][space_index]
                    - u1_j_blocks[(local_time - 1) % NT][space_index]
                    + u1_s_blocks[local_time][space_index]
                    - u1_s_blocks[local_time][(space_index - 1) % NX],
                    polynomial,
                )
                shifted_block = shifted_divergence
                u1_block = u1_divergence
                shifted_scalar = prior.quotient_element(
                    vector, shifted_block, polynomial
                )
                u1_scalar = prior.quotient_element(
                    vector, u1_block, polynomial
                )
                scalar_divergence = block120.red(
                    shift_j_values[local_time][space_index]
                    - shift_j_values[(local_time - 1) % NT][space_index]
                    + shift_s_values[local_time][space_index]
                    - shift_s_values[local_time][(space_index - 1) % NX],
                    polynomial,
                )
                pin_transfer_exact = (
                    pin_transfer_exact
                    and block120.field_equal(
                        shifted_divergence, shifted_block, polynomial
                    )
                    and block120.field_equal(
                        shifted_block,
                        block120.field_matrix(
                            I**momentum * u1_block, polynomial
                        ),
                        polynomial,
                    )
                    and block120.field_equal(
                        u1_divergence, u1_block, polynomial
                    )
                    and block120.red(
                        scalar_divergence - shifted_scalar, polynomial
                    )
                    == 0
                    and block120.red(
                        shifted_scalar - I**momentum * u1_scalar,
                        polynomial,
                    )
                    == 0
                    and I**momentum != 0
                )
                residuals.append(shifted_scalar)
        residual_zero_counts.append(sum(value == 0 for value in residuals))
        residual_digests.append(exact_digest(tuple(residuals)))

        for name, shift_blocks, shift_values in (
            (
                "J",
                shift_j_blocks,
                shift_j_values,
            ),
            (
                "S",
                shift_s_blocks,
                shift_s_values,
            ),
        ):
            shift_left, shift_right = descent_counts(
                shift_blocks, shift_values, bra, vector, polynomial
            )
            shift_adjoint = adjoint_count(
                name, shift_blocks, gram, polynomial
            )
            pin_transfer_exact = (
                pin_transfer_exact
                and shift_left == 0
                and shift_right == 0
                and shift_adjoint == 0
            )
            if name == "J":
                density_descent_left.append(shift_left)
                density_descent_right.append(shift_right)
                adjoint_density.append(shift_adjoint)
            else:
                flux_descent_left.append(shift_left)
                flux_descent_right.append(shift_right)
                adjoint_flux.append(shift_adjoint)

    pin_transfer_exact = (
        pin_transfer_exact
        and tuple(residual_zero_counts) == (0, 0, 0, 0)
    )

    time_commutator = action * time_shift - time_shift * action
    time_shift_nnz = sum(value != 0 for value in time_commutator)
    time_structure_exact = (
        matrix_zero(time_shift.H * time_shift - sp.eye(NS))
        and matrix_zero(time_shift**NT + sp.eye(NS))
        and time_shift_nnz > 0
    )
    pinned_intervals = block119.EXPECTED_BETA_INTERVALS[fixture_index]
    contractivity_pinned = (
        len(pinned_intervals) == 2
        and all(0 < lower < upper < 1 for lower, upper in pinned_intervals)
    )
    scalar_transfer_exact = True
    conservation_vacuous = True
    for momentum, sector in enumerate(sectors):
        polynomial = sector.polynomial
        beta = block120.red(block119.RHO**2, polynomial)
        vector = sector.y
        bra = block120.field_adjoint(vector, polynomial)
        scalar_operator = block120.field_matrix(
            beta * sp.eye(NT), polynomial
        )
        scalar_transfer_exact = (
            scalar_transfer_exact
            and sector.geometric_hankel
            and block120.field_equal(
                scalar_operator * vector,
                block120.field_matrix(beta * vector, polynomial),
                polynomial,
            )
            and block120.field_equal(
                bra * scalar_operator,
                block120.field_matrix(beta * bra, polynomial),
                polynomial,
            )
        )
        transfer = sp.Matrix([[beta]])
        cell_energy = sp.Matrix([[-sp.log(beta)]])
        conservation_vacuous = (
            conservation_vacuous
            and matrix_zero(transfer * cell_energy - cell_energy * transfer)
            and transfer.rows == transfer.cols == 1
        )

    return FixtureCertificate(
        shear=shear,
        shift_commutation_exact=shift_commutation_exact,
        routed_identity_exact=routed_identity_exact,
        routing_distinct=routing_distinct,
        seam_exact=seam_exact,
        phase_structure_exact=phase_structure_exact,
        phase_reduction_exact=phase_reduction_exact,
        quotient_positive_exact=quotient_positive_exact,
        phase_form=phase_form,
        momentum_form=momentum_form,
        pin_transfer_exact=pin_transfer_exact,
        residual_zero_counts=tuple(residual_zero_counts),
        residual_digests=tuple(residual_digests),
        density_descent_left=tuple(density_descent_left),
        density_descent_right=tuple(density_descent_right),
        flux_descent_left=tuple(flux_descent_left),
        flux_descent_right=tuple(flux_descent_right),
        adjoint_density=tuple(adjoint_density),
        adjoint_flux=tuple(adjoint_flux),
        time_shift_nnz=time_shift_nnz if time_structure_exact else 0,
        time_shift_digest=exact_digest(time_commutator),
        scalar_transfer_exact=scalar_transfer_exact,
        conservation_vacuous=conservation_vacuous,
        contractivity_pinned=contractivity_pinned,
        interval_digest=exact_digest(pinned_intervals),
    )


def definiteness_certificate(
    fixtures: tuple[FixtureCertificate, ...]
) -> DefinitenessCertificate:
    total_u1 = sum(
        (
            block121.projector(block121.site(time_index, space_index))
            for time_index in range(NT)
            for space_index in range(NX)
        ),
        sp.zeros(NS),
    )
    witness = sp.Matrix((0, 1, 0, 1))
    norm = (witness.H * witness)[0]
    phase_form = fixtures[0].phase_form
    momentum_form = fixtures[0].momentum_form
    phase_form_exact = (
        all(matrix_zero(fixture.phase_form - phase_form) for fixture in fixtures)
        and matrix_zero(phase_form - sp.diag(1, I, -1, -I))
        and all(
            phase_form[momentum, momentum] == I**momentum
            for momentum in range(NX)
        )
    )
    derived_charges = tuple(
        principal_charge(phase_form[momentum, momentum])
        for momentum in range(NX)
    )
    momentum_form_exact = (
        all(
            matrix_zero(fixture.momentum_form - momentum_form)
            for fixture in fixtures
        )
        and derived_charges == (0, 1, 2, -1)
        and matrix_zero(momentum_form - sp.diag(*derived_charges))
        and matrix_zero(momentum_form.H - momentum_form)
    )
    eigenvalues = tuple(momentum_form[entry, entry] for entry in range(NX))
    integer_sum = sum(
        momentum_form[index, index]
        for index in range(NX)
        if witness[index] != 0
    )
    integer_expectation = sp.cancel(
        (witness.H * momentum_form * witness)[0] / norm
    )
    modular_sum = sum(
        index for index in range(NX) if witness[index] != 0
    ) % NX
    momentum_action = momentum_form * witness
    return DefinitenessCertificate(
        u1_total_identity=matrix_zero(total_u1 - sp.eye(NS)),
        u1_definite_norm=(
            matrix_zero(total_u1 - sp.eye(NS))
            and norm == 2
            and (witness.H * sp.eye(NX) * witness)[0] == norm
            and norm > 0
        ),
        phase_form_exact=phase_form_exact,
        momentum_form_exact=momentum_form_exact,
        momentum_indefinite=(
            any(value > 0 for value in eigenvalues)
            and any(value < 0 for value in eigenvalues)
        ),
        witness_nonzero=(witness != sp.zeros(NX, 1)),
        witness_positive=(
            norm == 2
            and norm > 0
            and all(fixture.quotient_positive_exact for fixture in fixtures)
        ),
        integer_sum=integer_sum,
        integer_expectation=integer_expectation,
        modular_sum=modular_sum,
        momentum_action=momentum_action,
        not_eigenstate=(
            momentum_action != sp.zeros(NX, 1)
            and sp.Matrix.hstack(witness, momentum_action).rank() == 2
        ),
    )


def gauss_certificate(
    definiteness: DefinitenessCertificate,
) -> GaussCertificate:
    divergence = sp.Matrix(
        NX,
        NX,
        lambda row, column: (
            int(column == row) - int(column == (row - 1) % NX)
        ),
    )
    total_row = sp.ones(1, NX)
    zero_sum_basis = sp.Matrix.hstack(
        *(sp.eye(NX).col(index) - sp.eye(NX).col(NX - 1)
          for index in range(NX - 1))
    )
    image_zero_sum_exact = (
        divergence.rank() == NX - 1
        and matrix_zero(total_row * divergence)
        and zero_sum_basis.rank() == NX - 1
        and divergence.row_join(zero_sum_basis).rank() == NX - 1
    )
    population = sp.Matrix((0, 1, 0, 1))
    momentum_constraint_row = sp.Matrix([[0, 1, 2, -1]])
    modular_constraint_row = sp.Matrix([[0, 1, 2, 3]])
    u1_constraint_row = sp.ones(1, NX)
    source = sp.Matrix(
        tuple(
            momentum_constraint_row[0, index] * population[index]
            for index in range(NX)
        )
    )
    solution = sp.Matrix((0, 1, 1, 0))
    solution_exact = (
        matrix_zero(divergence * solution - source)
        and (total_row * source)[0] == 0
    )
    momentum_population_passes = (
        definiteness.integer_expectation == 0
        and (momentum_constraint_row * population)[0] == 0
        and int((modular_constraint_row * population)[0]) % NX == 0
        and solution_exact
    )
    u1_population_fails = (
        definiteness.u1_total_identity
        and (u1_constraint_row * population)[0] == 2
        and (u1_constraint_row * population)[0] != 0
    )
    return GaussCertificate(
        divergence=divergence,
        image_zero_sum_exact=image_zero_sum_exact,
        momentum_constraint_row=momentum_constraint_row,
        source=source,
        solution=solution,
        solution_exact=solution_exact,
        momentum_population_passes=momentum_population_passes,
        u1_population_fails=u1_population_fails,
    )


SCOPE_KEYS = (
    "definiteness",
    "expected_momentum",
    "state_caveat",
    "population",
    "momentum_constraint",
    "sector_phase",
    "pin_transfer",
    "energy_vacuity",
    "energy_scope",
    "os_boundary",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity",
    "adm",
    "n1_n8",
    "w1",
    "n5_resolution",
)


def scope_certificate(note: str, mutation: str) -> dict[str, bool]:
    result = {
        "definiteness": (
            "definiteness" in note or "indefinite" in note
        ),
        "expected_momentum": (
            "expected total momentum" in note
            or "expectation value" in note
        ),
        "state_caveat": (
            "not an eigenstate" in note or "does not annihilate" in note
        ),
        "population": "population" in note,
        "momentum_constraint": "momentum constraint" in note,
        "sector_phase": "i^k" in note or "sector phase" in note,
        "pin_transfer": (
            "momentum-blind" in note or "transfers verbatim" in note
        ),
        "energy_vacuity": "vacuous" in note or "contentless" in note,
        "energy_scope": "per-period" in note or "per-cell" in note,
        "os_boundary": (
            "not an os no-go" in note or "not a curved os no-go" in note
        ),
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "gravity": "gravity constraint quotient remains unexecuted" in note,
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
        "Block 122 note/runner/cache and ancestors 121--103 are pinned",
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_MOMENTUM_POPULATION_DEFINITENESS_BOUNDED_THEOREM_NOTE_2026-08-16.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md",
            "scripts/admissibility_dirac_kahler_quotient_observable_obstruction_2026_08_16.py",
            "logs/runner-cache/admissibility_dirac_kahler_quotient_observable_obstruction_2026_08_16.txt",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(
            authority[f"ancestor_{number}"] for number in range(103, 122)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    shift = spatial_shift()
    transform = spatial_fourier()
    cut = prior.cut_shift()
    time_shift = antiperiodic_time_shift()
    fixtures = tuple(
        fixture_certificate(
            shear, fixture_index, shift, transform, cut, time_shift
        )
        for fixture_index, shear in enumerate(SHEARS)
    )

    shift_exact = all(
        fixture.shift_commutation_exact
        and fixture.routed_identity_exact
        and fixture.routing_distinct
        and fixture.seam_exact
        for fixture in fixtures
    )
    if mutation == "break_shift_commutation":
        shift_exact = False
    checks.check(
        "B-the-shift-identity",
        "[U_x,Q]=0, R_x=U_x Q, and both routed divergences equal [E_z,R_x] at all 32 sites including seams",
        shift_exact,
    )

    phase_exact = all(
        fixture.phase_structure_exact and fixture.phase_reduction_exact
        for fixture in fixtures
    )
    if mutation == "break_phase_reduction":
        phase_exact = False
    checks.check(
        "C-the-sector-phase-reduction",
        "Q and R_x are momentum diagonal and each (k,k) site block obeys [E_z,R_x]_kk=i^k[E_z,Q]_kk",
        phase_exact,
    )

    definiteness = definiteness_certificate(fixtures)
    definiteness_exact = (
        definiteness.u1_total_identity
        and definiteness.u1_definite_norm
        and definiteness.phase_form_exact
        and definiteness.momentum_form_exact
        and definiteness.momentum_indefinite
        and definiteness.witness_nonzero
        and definiteness.witness_positive
        and definiteness.integer_sum == 0
        and definiteness.integer_expectation == 0
        and definiteness.modular_sum == 0
        and definiteness.momentum_action == sp.Matrix((0, 1, 0, -1))
        and definiteness.not_eigenstate
    )
    if mutation == "break_definiteness":
        definiteness_exact = False
    eigenstate_claimed = mutation == "claim_eigenstate"
    checks.check(
        "D-the-definiteness-split",
        "sum_z E_z=I is definite, while P_x=diag(0,1,2,-1) is indefinite and e1+e3 has zero expected momentum but is not an eigenstate",
        definiteness_exact and not eigenstate_claimed,
    )

    gauss = gauss_certificate(definiteness)
    gauss_exact = (
        gauss.image_zero_sum_exact
        and gauss.solution_exact
        and gauss.momentum_population_passes
        and gauss.u1_population_fails
    )
    if mutation == "break_gauss_image":
        gauss_exact = False
    u1_population_claimed = mutation == "claim_u1_populates"
    checks.check(
        "E-the-gauss-population",
        "the closed-Z4 divergence image is exactly zero-sum, so the momentum source is populatable iff its expected total charge vanishes",
        gauss_exact and not u1_population_claimed,
    )

    pin_exact = all(
        fixture.pin_transfer_exact
        and fixture.residual_zero_counts == (0, 0, 0, 0)
        and fixture.density_descent_left == (0, 0, 0, 0)
        and fixture.density_descent_right == (0, 0, 0, 0)
        and fixture.flux_descent_left == (0, 0, 0, 0)
        and fixture.flux_descent_right == (0, 0, 0, 0)
        and fixture.adjoint_density == (0, 0, 0, 0)
        and fixture.adjoint_flux == (0, 0, 0, 0)
        for fixture in fixtures
    )
    if mutation == "break_pin_transfer":
        pin_exact = False
    checks.check(
        "F-the-pin-transfer",
        "the invertible i^k phase transfers every nonzero quotient residual and the 0/32 density/flux descent and adjointness failures verbatim",
        pin_exact,
    )

    energy_exact = all(
        fixture.time_shift_nnz > 0
        and fixture.scalar_transfer_exact
        and fixture.conservation_vacuous
        and fixture.contractivity_pinned
        for fixture in fixtures
    )
    slice_energy_claimed = mutation == "claim_slice_energy"
    conservation_content_claimed = mutation == "claim_energy_content"
    checks.check(
        "G-the-energy-scope",
        "one-slice time translation fails; h_k conservation is vacuous for scalar rho_k^2 transfer, while h_k>0 is the pinned Block 119 contractivity fact",
        energy_exact
        and not slice_energy_claimed
        and not conservation_content_claimed,
    )

    note_scope = scope_certificate(normalized_note(), mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "required definiteness/population/phase/pin/energy/N1--N8/W1/N5 firewalls and runtime bound are present",
        set(note_scope) == set(SCOPE_KEYS)
        and all(note_scope.values())
        and elapsed_before_scope <= 400,
    )

    phase_diagonal = tuple(
        fixtures[0].phase_form[index, index]
        for index in range(NX)
    )
    momentum_diagonal = tuple(
        fixtures[0].momentum_form[index, index] for index in range(NX)
    )
    print(
        "SHIFT/SECTOR PHASE: [U_x,Q]=0 and R_x=U_xQ for two exact routings; "
        f"U_x^phys diag={phase_diagonal}, P_x/(pi/2)={momentum_diagonal}."
    )
    print(
        "DEFINITENESS: sum_z E_z=I_32 gives the norm; P_x has both signs; "
        "a=e1+e3 has ||a||^2=2, integer charge 1+(-1)=0, mod-4 charge "
        f"1+3=0, while P_x a={tuple(definiteness.momentum_action)} !=0 — not an eigenstate; zero is an expectation."
    )
    print(
        "GAUSS POPULATION: im(div_Z4)=ker(1,1,1,1); source="
        f"{tuple(gauss.source)}, exact flux={tuple(gauss.solution)}; the momentum constraint is populatable but the identity U(1) charge is not."
    )
    print(
        "PIN TRANSFER: residual zeros/32 per k are "
        f"{fixtures[0].residual_zero_counts}/{fixtures[1].residual_zero_counts}; "
        f"density/flux descent and adjointness are all {fixtures[0].adjoint_density}/{fixtures[0].adjoint_flux}."
    )
    print(
        "TIME-SYMMETRY FAILURE: one-step AP [Q,V] nnz="
        f"{fixtures[0].time_shift_nnz}/{fixtures[1].time_shift_nnz}, "
        f"witness sha={fixtures[0].time_shift_digest}/{fixtures[1].time_shift_digest}; no per-slice energy exists."
    )
    print(
        "ENERGY STRUCTURAL FACT (VACUOUS): on each one-dimensional quotient line B_k=rho_k^2 I, so h_k=-log(rho_k^2) commutes with B_k identically and constancy could not fail."
    )
    print(
        "ENERGY CONTENTFUL RESIDUE: h_k>0 is precisely the imported Block 119 per-period contractivity certificate; pinned-interval sha="
        f"{fixtures[0].interval_digest}/{fixtures[1].interval_digest}."
    )
    print(
        "N5: per_element: exact shift-commutation, routed-identity, phase-reduction, definiteness, gauss-image, pin-transfer, and vacuity certificates are checked"
    )
    print(
        "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus"
    )
    print(
        "per_mode: every momentum sector's shift residual is the invertible phase i^k times the u(1) residual while the quotient momentum charge is indefinite diag(0,1,2,-1)"
    )
    print(
        "per_block: the closed-carrier population wall is a definiteness statement — the identity-valued u(1) charge can never vanish on a positive package but the indefinite momentum charge admits nonzero states of vanishing expected total momentum"
    )
    print(
        "lattice_wide: checked and not executed — the momentum-sourced gauss quotient execution, non-local dressings for the observable wall, the naturality classification, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: the momentum constraint is populatable on the closed carrier because its charge is indefinite — the first population break of the campaign — while the local-observable wall transfers verbatim under the invertible sector phase and the only energy object is the already-certified per-period contraction"
    )
    print(
        "DECISION_CUT: execute the momentum-sourced gauss quotient with the vanishing-expectation state class; reject per-slice energy constructions"
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
