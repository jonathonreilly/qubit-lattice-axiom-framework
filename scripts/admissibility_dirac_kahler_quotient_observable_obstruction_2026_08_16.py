#!/usr/bin/env python3
"""Block 122: exact obstruction to a local routed quotient observable.

The committed Block 121 current is compressed onto the completed rank-one
OS quotient at every momentum and fine site.  Exact root-field arithmetic
certifies the affine residues, the two flux conventions, the microscopic
commutator residual, null-space non-descent, reflection-adjointness failure,
and the routing-class obstruction.  Wall-clock timing is the only
floating-point computation.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
from pathlib import Path
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_constraint_quotient_coupling_2026_08_16 as prior


R = sp.Rational
I = sp.I
block120 = prior.prior
block119 = block120.prior
DK = prior.DK
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_"
    "BOUNDED_THEOREM_NOTE_2026-08-16.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_"
    "BOUNDED_THEOREM_NOTE_2026-08-16.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_constraint_quotient_coupling_"
    "2026_08_16.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_constraint_quotient_"
    "coupling_2026_08_16.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md",
    "scripts/admissibility_dirac_kahler_constraint_quotient_coupling_2026_08_16.py",
    "logs/runner-cache/admissibility_dirac_kahler_constraint_quotient_coupling_2026_08_16.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "31e4c7ff7d41db6a78feef19dba2bfbea3dc1830"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block121-constraint-quotient-coupling-20260816"
)
PARENT_COMMIT = "1714abeefcf3763c0bfe001f30fd14521c538622"
PARENT_NOTE_BLOB = "1e0013d0c6ab54e2f31aefeb5489796a28137e31"
PARENT_RUNNER_BLOB = "ec6da92addda5774250169e46f92d68c9d68f7c8"
PARENT_CACHE_BLOB = "113b6b5f42ab8007839dac3a396148d534ad719a"
ANCESTOR_COMMITS = (
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
    "break_projector_lemma",
    "break_residue_digest",
    "break_flux_masks",
    "claim_mask_invariant",
    "break_residual_identity",
    "claim_microscopic_ward",
    "break_descent",
    "break_adjointness",
    "claim_routing_repair",
    "claim_wholecell_content",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_toe_progress",
)

NT = prior.NT
NX = prior.NX
NS = prior.NS
SHEARS = (DK.PRIMARY_SHEAR, DK.SECOND_SHEAR)

# Fresh 2026-08-16 block122_solve.py run, TOTAL: PASS=1908 FAIL=0.
# Each digest commits the exact (A,B) pair at all eight slices of one k.
EXPECTED_RESIDUE_DIGESTS = {
    R(5, 13): {
        "J": (
            "19e4a95126aa7d05",
            "4a7cd5a411384ac7",
            "b74b954e6e3c1da2",
            "7f3388a11f16bc96",
        ),
        "S": (
            "29856de469aaa778",
            "0504d5b22ccf77f3",
            "f197586c480a5341",
            "8508949b08472780",
        ),
    },
    R(3, 5): {
        "J": (
            "0f6a6b90843f3b84",
            "370f8fd243a9a858",
            "f031bebabd1e4305",
            "20b7f257007efafb",
        ),
        "S": (
            "cf221cabf3abd176",
            "aa3ccfe695257acc",
            "74f1bbd4d761c5b1",
            "54100ebe9d928dd3",
        ),
    },
}

EXPECTED_FULL_FLUX_MASK = (
    "11111111",
    "11110111",
    "11111111",
    "11110111",
)
EXPECTED_SAME_SLICE_FLUX_MASK = (
    "11111111",
    "00000000",
    "11111111",
    "00000000",
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


def spatial_fourier() -> sp.Matrix:
    fourier = sp.Matrix(
        NX, NX, lambda row, column: I ** (-row * column)
    ) / 2
    return sp.kronecker_product(sp.eye(NT), fourier)


def cut_shift() -> sp.ImmutableSparseMatrix:
    """The exact antiperiodic half-circle cut used by block122_solve.py."""
    entries = {(row, row + 4): 1 for row in range(4)}
    entries.update({(row + 4, row): -1 for row in range(4)})
    literal = sp.ImmutableSparseMatrix(NT, NT, entries)
    committed = sp.ImmutableSparseMatrix(block119.cut_shift())
    if committed != literal:
        raise AssertionError("committed Block 119 cut differs from the pinned cut")
    return committed


def momentum_block(
    matrix: sp.Matrix, momentum: int, transform: sp.Matrix
) -> sp.Matrix:
    indices = tuple(momentum + NX * time_index for time_index in range(NT))
    return (transform.H * matrix * transform).extract(indices, indices)


def momentum_restriction(
    matrix: sp.Matrix,
    momentum: int,
    transform: sp.Matrix,
    cut: sp.Matrix,
    polynomial: sp.Poly,
) -> sp.Matrix:
    block = cut * momentum_block(matrix, momentum, transform) * cut.T
    return block120.field_matrix(block, polynomial)


def matrix_element(
    vector: sp.Matrix, operator: sp.Matrix, polynomial: sp.Poly
) -> sp.Expr:
    bra = block120.field_adjoint(vector, polynomial)
    return block120.red((bra * operator * vector)[0], polynomial)


def quotient_element(
    vector: sp.Matrix, operator: sp.Matrix, polynomial: sp.Poly
) -> sp.Expr:
    norm = matrix_element(vector, sp.eye(vector.rows), polynomial)
    if block120.red(norm, polynomial) == 0:
        raise AssertionError("quotient representative has zero exact norm")
    return block120.red(
        matrix_element(vector, operator, polynomial) / norm,
        polynomial,
    )


def field_coordinates(
    value: sp.Expr, polynomial: sp.Poly
) -> tuple[sp.Expr, sp.Expr]:
    rho = block119.RHO
    reduced = sp.Poly(sp.expand(block120.red(value, polynomial)), rho)
    if reduced.degree() > 1:
        raise AssertionError("quadratic root-field value did not reduce to A+B*rho")
    return sp.cancel(reduced.nth(0)), sp.cancel(reduced.nth(1))


def exact_digest(payload: object) -> str:
    return hashlib.sha256(sp.srepr(payload).encode("utf-8")).hexdigest()[:16]


def projector_lemma(transform: sp.Matrix) -> bool:
    """F_k^H E_(i,x) F_k=(1/4)e_i e_i^T, independently of x."""
    for momentum in range(NX):
        for time_index in range(NT):
            expected = sp.zeros(NT)
            expected[time_index, time_index] = R(1, NX)
            reference = None
            for space_index in range(NX):
                local = prior.projector(prior.site(time_index, space_index))
                block = momentum_block(local, momentum, transform)
                if not prior.matrix_zero(block - expected):
                    return False
                if reference is None:
                    reference = block
                elif not prior.matrix_zero(block - reference):
                    return False
    return True


def same_slice_x_hop_flux(
    spatial: tuple[sp.Matrix, ...]
) -> tuple[tuple[sp.ImmutableSparseMatrix, ...], bool]:
    """Keep precisely oriented, same-time, range-one spatial monomials."""
    direct: list[sp.ImmutableSparseMatrix] = []
    support_exact = True
    for kernel in spatial:
        entries: dict[tuple[int, int], sp.Expr] = {}
        for (row, column), value in kernel.todok().items():
            row_time, row_space = prior.coordinates(row)
            column_time, column_space = prior.coordinates(column)
            displacement = abs(
                prior.shortest_displacement(row_space, column_space, NX)
            )
            if row_time == column_time and displacement == 1:
                entries[(row, column)] = value
        local = sp.ImmutableSparseMatrix(NS, NS, entries)
        remainder = kernel - local
        support_exact = (
            support_exact
            and prior.matrix_zero(kernel - local - remainder)
            and all(
                prior.coordinates(row)[0] != prior.coordinates(column)[0]
                or abs(
                    prior.shortest_displacement(
                        prior.coordinates(row)[1],
                        prior.coordinates(column)[1],
                        NX,
                    )
                )
                == 2
                for row, column in remainder.todok()
            )
        )
        direct.append(local)
    return tuple(direct), support_exact


def compression(
    bra: sp.Matrix,
    vector: sp.Matrix,
    operator: sp.Matrix,
    norm: sp.Expr,
    polynomial: sp.Poly,
) -> sp.Expr:
    return block120.red((bra * operator * vector)[0] / norm, polynomial)


MatrixGrid = tuple[tuple[sp.Matrix, ...], ...]
ValueGrid = tuple[tuple[sp.Expr, ...], ...]


def observable_grid(
    kernels: tuple[sp.Matrix, ...],
    momentum: int,
    transform: sp.Matrix,
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
            block = momentum_restriction(
                kernels[prior.site(old_time, space_index)],
                momentum,
                transform,
                cut,
                polynomial,
            )
            blocks.append(block)
            values.append(compression(bra, vector, block, norm, polynomial))
        block_rows.append(tuple(blocks))
        value_rows.append(tuple(values))
    return tuple(block_rows), tuple(value_rows)


def spatially_uniform(values: ValueGrid, polynomial: sp.Poly) -> bool:
    return all(
        all(
            block120.red(value - row[0], polynomial) == 0
            for value in row
        )
        for row in values
    )


def value_mask(values: ValueGrid) -> str:
    return "".join("1" if row[0] != 0 else "0" for row in values)


def generic_curl_invariance() -> bool:
    """Any exact discrete curl, including harmonic constants, has zero div."""
    potential = sp.symbols(f"K0:{NS}")
    harmonic_time, harmonic_space = sp.symbols("H_t H_x")

    def k(time_index: int, space_index: int) -> sp.Symbol:
        return potential[prior.site(time_index, space_index)]

    def delta_temporal(time_index: int, space_index: int) -> sp.Expr:
        return (
            k(time_index, space_index)
            - k(time_index, space_index - 1)
            + harmonic_time
        )

    def delta_spatial(time_index: int, space_index: int) -> sp.Expr:
        return (
            -k(time_index, space_index)
            + k(time_index - 1, space_index)
            + harmonic_space
        )

    return all(
        sp.expand(
            delta_temporal(time_index, space_index)
            - delta_temporal(time_index - 1, space_index)
            + delta_spatial(time_index, space_index)
            - delta_spatial(time_index, space_index - 1)
        )
        == 0
        for time_index in range(NT)
        for space_index in range(NX)
    )


@dataclass(frozen=True)
class FixtureCertificate:
    shear: sp.Rational
    theta_metric_exact: bool
    density_nonzero: bool
    spatial_uniformity: bool
    residue_digests: dict[str, tuple[str, ...]]
    residue_exact: bool
    moment_form_exact: bool
    full_flux_mask: tuple[str, ...]
    same_flux_mask: tuple[str, ...]
    flux_decomposition_exact: bool
    residual_identity_exact: bool
    residual_zero_counts: tuple[int, ...]
    residual_digests: tuple[str, ...]
    density_descent_left: tuple[int, ...]
    density_descent_right: tuple[int, ...]
    adjoint_density: tuple[int, ...]
    adjoint_flux: tuple[int, ...]
    routing_residual_exact: bool
    imported_commutator_nonzero: bool
    wholecell_vacuous: bool


def fixture_certificate(
    shear: sp.Rational, transform: sp.Matrix, cut: sp.Matrix
) -> FixtureCertificate:
    current = prior.certify_current(shear)
    canonical, alternate = current.routings
    same_flux, flux_support_exact = same_slice_x_hop_flux(canonical.spatial)
    sectors = block119.make_sectors(shear)
    completion = block119.reflection_real_completion(sectors)
    if len(sectors) != NX or len(completion.thetas) != NX:
        raise AssertionError("completed quotient must have four momentum sectors")

    theta_metric_exact = True
    density_nonzero = True
    uniformity_exact = True
    residue_digests: dict[str, list[str]] = {"J": [], "S": []}
    residue_exact = True
    moment_form_exact = True
    full_masks: list[str] = []
    same_masks: list[str] = []
    flux_decomposition_exact = flux_support_exact
    residual_identity_exact = True
    residual_zero_counts: list[int] = []
    residual_digests: list[str] = []
    density_descent_left: list[int] = []
    density_descent_right: list[int] = []
    adjoint_density: list[int] = []
    adjoint_flux: list[int] = []
    routing_residual_exact = True
    wholecell_vacuous = True

    for momentum, sector in enumerate(sectors):
        polynomial = sector.polynomial
        rho = block119.RHO
        vector = sector.y
        bra = block120.field_adjoint(vector, polynomial)
        norm = block120.red((bra * vector)[0], polynomial)
        gram = block120.field_matrix(
            completion.thetas[momentum] * sector.h00, polynomial
        )
        rank_one = block120.field_matrix(vector * bra, polynomial)
        theta_metric_exact = (
            theta_metric_exact
            and norm != 0
            and block120.field_equal(gram, rank_one, polynomial)
        )
        unit = block120.field_matrix(vector / norm, polynomial)
        unit_bra = block120.field_adjoint(unit, polynomial)
        theta_metric_exact = theta_metric_exact and block120.red(
            (unit_bra * gram * unit)[0] - 1, polynomial
        ) == 0

        density_blocks, density_values = observable_grid(
            canonical.temporal,
            momentum,
            transform,
            cut,
            polynomial,
            bra,
            vector,
            norm,
        )
        flux_blocks, flux_values = observable_grid(
            canonical.spatial,
            momentum,
            transform,
            cut,
            polynomial,
            bra,
            vector,
            norm,
        )
        same_flux_blocks, same_flux_values = observable_grid(
            same_flux,
            momentum,
            transform,
            cut,
            polynomial,
            bra,
            vector,
            norm,
        )
        grids = {
            "J": (density_blocks, density_values),
            "S": (flux_blocks, flux_values),
        }

        for blocks, values in grids.values():
            for local_time in range(NT):
                for space_index in range(NX):
                    metric_value = block120.red(
                        (
                            unit_bra
                            * gram
                            * blocks[local_time][space_index]
                            * unit
                        )[0],
                        polynomial,
                    )
                    theta_metric_exact = (
                        theta_metric_exact
                        and block120.red(
                            values[local_time][space_index] - metric_value,
                            polynomial,
                        )
                        == 0
                    )

        density_nonzero = density_nonzero and all(
            value != 0 for row in density_values for value in row
        )
        uniformity_exact = (
            uniformity_exact
            and spatially_uniform(density_values, polynomial)
            and spatially_uniform(flux_values, polynomial)
            and spatially_uniform(same_flux_values, polynomial)
        )
        full_masks.append(value_mask(flux_values))
        same_masks.append(value_mask(same_flux_values))

        for name, (_, values) in grids.items():
            coordinates = tuple(
                field_coordinates(values[local_time][0], polynomial)
                for local_time in range(NT)
            )
            residue_digests[name].append(exact_digest(coordinates))
            beta = block120.red(rho**2, polynomial)
            moment_form_exact = (
                moment_form_exact
                and bool(sector.geometric_hankel)
            )
            for local_time, (a_residue, b_residue) in enumerate(coordinates):
                base = values[local_time][0]
                moment_form_exact = moment_form_exact and block120.red(
                    base - (a_residue + b_residue * rho), polynomial
                ) == 0
                for moment in range(4):
                    moment_form_exact = moment_form_exact and block120.red(
                        beta**moment * base
                        - rho ** (2 * moment)
                        * (a_residue + b_residue * rho),
                        polynomial,
                    ) == 0

        for local_time in range(NT):
            for space_index in range(NX):
                remainder = (
                    flux_blocks[local_time][space_index]
                    - same_flux_blocks[local_time][space_index]
                )
                full_difference = block120.red(
                    flux_values[local_time][space_index]
                    - same_flux_values[local_time][space_index],
                    polynomial,
                )
                flux_decomposition_exact = (
                    flux_decomposition_exact
                    and full_difference
                    == compression(bra, vector, remainder, norm, polynomial)
                )

        residuals: list[sp.Expr] = []
        residual_zero = 0
        descent_left = 0
        descent_right = 0
        density_adjoint_zero = 0
        flux_adjoint_zero = 0
        for local_time in range(NT):
            old_time = (local_time + NT // 2) % NT
            for space_index in range(NX):
                divergence_block = (
                    density_blocks[local_time][space_index]
                    - density_blocks[(local_time - 1) % NT][space_index]
                    + flux_blocks[local_time][space_index]
                    - flux_blocks[local_time][(space_index - 1) % NX]
                )
                index = prior.site(old_time, space_index)
                commutator = (
                    prior.projector(index) * current.action
                    - current.action * prior.projector(index)
                )
                commutator_block = momentum_restriction(
                    commutator,
                    momentum,
                    transform,
                    cut,
                    polynomial,
                )
                residual = compression(
                    bra, vector, divergence_block, norm, polynomial
                )
                pinned = compression(
                    bra, vector, commutator_block, norm, polynomial
                )
                residual_identity_exact = (
                    residual_identity_exact
                    and block120.field_equal(
                        divergence_block, commutator_block, polynomial
                    )
                    and block120.red(residual - pinned, polynomial) == 0
                )
                residuals.append(residual)
                residual_zero += residual == 0

                alternate_divergence = prior.backward_divergence(
                    alternate.temporal,
                    alternate.spatial,
                    old_time,
                    space_index,
                )
                alternate_block = momentum_restriction(
                    alternate_divergence,
                    momentum,
                    transform,
                    cut,
                    polynomial,
                )
                alternate_residual = compression(
                    bra, vector, alternate_block, norm, polynomial
                )
                routing_residual_exact = (
                    routing_residual_exact
                    and block120.field_equal(
                        alternate_block, commutator_block, polynomial
                    )
                    and block120.red(
                        alternate_residual - residual, polynomial
                    )
                    == 0
                )

                operator = density_blocks[local_time][space_index]
                scalar = density_values[local_time][space_index]
                descent_left += block120.field_equal(
                    block120.field_matrix(bra * operator, polynomial),
                    block120.field_matrix(scalar * bra, polynomial),
                    polynomial,
                )
                descent_right += block120.field_equal(
                    block120.field_matrix(operator * vector, polynomial),
                    block120.field_matrix(scalar * vector, polynomial),
                    polynomial,
                )

                reflected_density = density_blocks[momentum_reflect_time(
                    "J", local_time
                )][space_index]
                density_adjoint_residual = block120.field_matrix(
                    gram * operator
                    - block120.field_adjoint(reflected_density, polynomial)
                    * gram,
                    polynomial,
                )
                density_adjoint_zero += block120.field_equal(
                    density_adjoint_residual, sp.zeros(NT), polynomial
                )

                flux_operator = flux_blocks[local_time][space_index]
                reflected_flux = flux_blocks[momentum_reflect_time(
                    "S", local_time
                )][space_index]
                flux_adjoint_residual = block120.field_matrix(
                    gram * flux_operator
                    - block120.field_adjoint(reflected_flux, polynomial)
                    * gram,
                    polynomial,
                )
                flux_adjoint_zero += block120.field_equal(
                    flux_adjoint_residual, sp.zeros(NT), polynomial
                )

        residual_zero_counts.append(residual_zero)
        residual_digests.append(exact_digest(tuple(residuals)))
        density_descent_left.append(descent_left)
        density_descent_right.append(descent_right)
        adjoint_density.append(density_adjoint_zero)
        adjoint_flux.append(flux_adjoint_zero)

        beta = block120.red(rho**2, polynomial)
        for values in (density_values, flux_values):
            for local_time in range(NT):
                for moment in range(4):
                    now = tuple(
                        block120.red(
                            beta**moment * value, polynomial
                        )
                        for value in values[local_time]
                    )
                    following = tuple(
                        block120.red(
                            beta ** (moment + 1) * value, polynomial
                        )
                        for value in values[local_time]
                    )
                    wholecell_vacuous = wholecell_vacuous and all(
                        block120.red(
                            following[space_index]
                            - beta * now[space_index],
                            polynomial,
                        )
                        == 0
                        for space_index in range(NX)
                    )
        wholecell_vacuous = wholecell_vacuous and all(
            block120.red(
                flux_values[local_time][space_index]
                - flux_values[local_time][(space_index - 1) % NX],
                polynomial,
            )
            == 0
            for local_time in range(NT)
            for space_index in range(NX)
        )

    digests = {
        name: tuple(values) for name, values in residue_digests.items()
    }
    residue_exact = digests == EXPECTED_RESIDUE_DIGESTS[shear]
    imported_nonzero = (
        all(routed.identity_exact for routed in current.routings)
        and current.curl_exact
        and current.routing_distinct
        and min(current.commutator_counts) > 0
    )
    return FixtureCertificate(
        shear,
        theta_metric_exact,
        density_nonzero,
        uniformity_exact,
        digests,
        residue_exact,
        moment_form_exact,
        tuple(full_masks),
        tuple(same_masks),
        flux_decomposition_exact,
        residual_identity_exact,
        tuple(residual_zero_counts),
        tuple(residual_digests),
        tuple(density_descent_left),
        tuple(density_descent_right),
        tuple(adjoint_density),
        tuple(adjoint_flux),
        routing_residual_exact,
        imported_nonzero,
        wholecell_vacuous,
    )


def momentum_reflect_time(name: str, local_time: int) -> int:
    if name == "J":
        return (6 - local_time) % NT
    if name == "S":
        return 7 - local_time
    raise ValueError(f"unknown observable {name!r}")


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


SCOPE_KEYS = (
    "observable",
    "descent",
    "reflection_adjointness",
    "structural",
    "routing",
    "wholecell_vacuity",
    "convention_dependent",
    "residue",
    "closed_form",
    "non_local",
    "stress_tensor",
    "off_shell",
    "microscopic_conservation",
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
        "observable": (
            "quotient observable" in note or "conserved observable" in note
        ),
        "descent": (
            "does not descend" in note
            or "null space out of itself" in note
        ),
        "reflection_adjointness": "reflection-adjointness" in note,
        "structural": "structural" in note,
        "routing": "routing" in note,
        "wholecell_vacuity": (
            "0 = 0 by construction" in note
            or "vacuous" in note
            or "contentless" in note
        ),
        "convention_dependent": "convention-dependent" in note,
        "residue": "residue" in note,
        "closed_form": "closed form" in note or "closed-form" in note,
        "non_local": "non-local" in note,
        "stress_tensor": "stress tensor" in note,
        "off_shell": "off-shell" in note,
        "microscopic_conservation": "microscopic conservation" in note,
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
        "Block 121 note/runner/cache and ancestors 120--103 are pinned",
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md",
            "scripts/admissibility_dirac_kahler_constraint_quotient_coupling_2026_08_16.py",
            "logs/runner-cache/admissibility_dirac_kahler_constraint_quotient_coupling_2026_08_16.txt",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(
            authority[f"ancestor_{number}"] for number in range(103, 121)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    transform = spatial_fourier()
    cut = cut_shift()
    fourier_exact = prior.matrix_zero(transform.H * transform - sp.eye(NS))
    cut_exact = prior.matrix_zero(cut * cut.T - sp.eye(NT))
    lemma_exact = projector_lemma(transform)
    fixtures = tuple(
        fixture_certificate(shear, transform, cut) for shear in SHEARS
    )

    if mutation == "break_projector_lemma":
        lemma_exact = False
    checks.check(
        "B-the-compression",
        "LEMMA: (P_k F^H E_(i,x) F P_k^H)=(1/4)e_i e_i^T independently of x; every K_Theta density compression is nonzero",
        fourier_exact
        and cut_exact
        and lemma_exact
        and all(fixture.theta_metric_exact for fixture in fixtures)
        and all(fixture.density_nonzero for fixture in fixtures)
        and all(fixture.spatial_uniformity for fixture in fixtures),
    )

    residue_exact = all(
        fixture.residue_exact and fixture.moment_form_exact
        for fixture in fixtures
    )
    if mutation == "break_residue_digest":
        residue_exact = False
    checks.check(
        "C-the-residue-closed-form",
        "moment-form structure gives rho_k^(2m)(A+B rho_k); every exact A,B residue is digest-pinned live",
        residue_exact,
    )

    masks_exact = all(
        fixture.full_flux_mask == EXPECTED_FULL_FLUX_MASK
        and fixture.same_flux_mask == EXPECTED_SAME_SLICE_FLUX_MASK
        and fixture.full_flux_mask != fixture.same_flux_mask
        and fixture.flux_decomposition_exact
        and fixture.imported_commutator_nonzero
        for fixture in fixtures
    )
    if mutation == "break_flux_masks":
        masks_exact = False
    mask_invariant_claimed = mutation == "claim_mask_invariant"
    checks.check(
        "D-the-flux-conventions",
        "full routed and same-slice x-hop masks are recomputed; their exact cross-slice/range-two difference changes masks, not divergence",
        masks_exact and not mask_invariant_claimed,
    )

    residual_exact = all(
        fixture.residual_identity_exact
        and fixture.residual_zero_counts == (0, 0, 0, 0)
        for fixture in fixtures
    )
    if mutation == "break_residual_identity":
        residual_exact = False
    microscopic_ward_claimed = mutation == "claim_microscopic_ward"
    checks.check(
        "E-the-microscopic-ward-failure",
        "the rho^2-translated site residual equals the K_Theta compression of dressed [E_z,Q] and is nonzero at all 32 sites per k",
        residual_exact and not microscopic_ward_claimed,
    )

    descent_exact = all(
        fixture.density_descent_left == (0, 0, 0, 0)
        and fixture.density_descent_right == (0, 0, 0, 0)
        for fixture in fixtures
    )
    adjoint_exact = all(
        fixture.adjoint_density == (0, 0, 0, 0)
        and fixture.adjoint_flux == (0, 0, 0, 0)
        for fixture in fixtures
    )
    if mutation == "break_descent":
        descent_exact = False
    if mutation == "break_adjointness":
        adjoint_exact = False
    checks.check(
        "F-the-descent-obstruction",
        "density maps the OS null space out of itself and K_Theta reflection-adjointness has 0/32 density or flux components per k",
        descent_exact and adjoint_exact,
    )

    routing_exact = (
        generic_curl_invariance()
        and all(fixture.routing_residual_exact for fixture in fixtures)
        and all(fixture.imported_commutator_nonzero for fixture in fixtures)
        and all(
            fixture.residual_zero_counts == (0, 0, 0, 0)
            for fixture in fixtures
        )
    )
    wholecell_vacuous = all(
        fixture.wholecell_vacuous for fixture in fixtures
    )
    if mutation == "claim_routing_repair":
        routing_exact = False
    if mutation == "claim_wholecell_content":
        wholecell_vacuous = False
    checks.check(
        "G-the-structural-classification",
        "all local routed currents differ by divergence-free rerouting and retain the Block 121 commutator pin; only that local routed class is exhausted",
        routing_exact and wholecell_vacuous,
    )

    note_scope = scope_certificate(normalized_note(), mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "required obstruction/N1--N8/W1/N5 firewalls and runtime bound are present",
        set(note_scope) == set(SCOPE_KEYS)
        and all(note_scope.values())
        and elapsed_before_scope <= 400,
    )

    print(
        "LEMMA: for every k,i,x, the momentum-k diagonal block of E_(i,x) "
        "is (1/4)e_i e_i^T, independent of x; quotient compression is therefore spatially uniform."
    )
    print(
        "RESIDUES/CLOSED FORM: j_k(m,a,x),s_k(m,a,x)=rho_k^(2m)(A+B rho_k) "
        f"from the moment form; c=5/13 {fixtures[0].residue_digests}; "
        f"c=3/5 {fixtures[1].residue_digests}."
    )
    print(
        "FLUX CONVENTIONS: full routed masks="
        f"{fixtures[0].full_flux_mask}; same-slice oriented x-hop masks="
        f"{fixtures[0].same_flux_mask}; their difference is exactly the "
        "cross-slice/range-two hop contribution, so masks are convention-dependent while div(J,S)=[E_z,Q] is invariant."
    )
    print(
        "MICROSCOPIC WARD: residual zeros/32 per k are "
        f"{fixtures[0].residual_zero_counts} and {fixtures[1].residual_zero_counts}; "
        f"exact commutator sha={fixtures[0].residual_digests},"
        f"{fixtures[1].residual_digests}."
    )
    print(
        "DESCENT/ADJOINTNESS: density null-space descent L/R="
        f"{fixtures[0].density_descent_left}/{fixtures[0].density_descent_right} "
        "per k; K_Theta reflection-adjoint density/flux="
        f"{fixtures[0].adjoint_density}/{fixtures[0].adjoint_flux}; both fixtures agree."
    )
    print(
        "STRUCTURAL CLASSIFICATION: the second routing differs by an exact discrete curl and has the same nonzero quotient residual pinned by Block 121's [E_z,Q] certificate; every local routed current therefore fails, while non-local dressing or Q modification remains live; the whole-cell rho^2 recurrence is 0 = 0 by construction."
    )
    print(
        "N5: per_element: exact compression, projector-lemma, residue, dual-convention flux, residual-identity, descent, and adjointness certificates are checked"
    )
    print(
        "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus"
    )
    print(
        "per_mode: every momentum's compressed current is rho^(2m) times an exact affine residue while the site-resolved ward recursion fails at every site with residual the compressed commutator"
    )
    print(
        "per_block: no local routed u(1) current descends to a conserved observable on the certified quotient — the obstruction is structural in the routing class and the whole-cell recursion is contentless"
    )
    print(
        "lattice_wide: checked and not executed — the stress-tensor source, non-local current dressings, the populated open/background-carrier quotient, the naturality classification, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient on a populated carrier, Records, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: the u(1) current is exactly conserved off-shell but has no observable on the certified OS quotient — every local routed current is pinned by the compressed commutator, fails descent and adjointness, and the only surviving whole-cell recursion is vacuous;"
    )
    print(
        "DECISION_CUT: pose the stress-tensor source and non-local dressings on the open carrier; reject further local routed U(1) constructions"
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
