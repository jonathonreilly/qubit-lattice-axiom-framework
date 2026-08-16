#!/usr/bin/env python3
"""Block 120: exact antiperiodic-torus wrap-defect certificate.

The literal Z8 reflection torus is compared, momentum by momentum, with
Block 119's completed half-space kernel.  The comparison isolates the exact
wrap defect, its finite-size spectral channels, and the corrected positive
contractive package.  Every algebraic check is performed in the stable-root
field; wall-clock timing is the only floating-point computation.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import combinations, permutations
from pathlib import Path
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16 as prior


R = sp.Rational
I = sp.I
A = prior.RHO
block118 = prior.prior
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_TORUS_WRAP_DEFECT_"
    "BOUNDED_THEOREM_NOTE_2026-08-16.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_"
    "BOUNDED_THEOREM_NOTE_2026-08-16.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_reflection_"
    "intertwiner_completion_2026_08_16.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_reflection_"
    "intertwiner_completion_2026_08_16.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TORUS_WRAP_DEFECT_BOUNDED_THEOREM_NOTE_2026-08-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md",
    "scripts/admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16.py",
    "logs/runner-cache/admissibility_dirac_kahler_reflection_intertwiner_completion_2026_08_16.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "4e566b14a6352a9a62590252a9755c7a103c1b9e"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block119-reflection-intertwiner-completion-20260816"
)
PARENT_COMMIT = "33fd2d21558604718f3a88713fe1976aff8f9dbb"
PARENT_NOTE_BLOB = "ed660c106e8e97f6ce85deef95228170e483e8e5"
PARENT_RUNNER_BLOB = "952494a18ba13b7d25fb144b8569687813d9bddc"
PARENT_CACHE_BLOB = "f7a9b09538c8787ed88885c04cdea3e5cff70104"
ANCESTOR_COMMITS = (
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
    "claim_theta_transfers",
    "break_split",
    "claim_hermitian_defect",
    "break_zero_pencil",
    "break_projector_law",
    "break_wrap_coefficient",
    "claim_full_decay",
    "break_corrected_inertia",
    "break_power_reconciliation",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_axiom_amendment",
    "claim_toe_progress",
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


def red(value: sp.Expr, polynomial: sp.Poly) -> sp.Expr:
    return prior.red(value, polynomial)


def star(value: sp.Expr, polynomial: sp.Poly) -> sp.Expr:
    return prior.star(value, polynomial)


def field_matrix(matrix: sp.Matrix, polynomial: sp.Poly) -> sp.Matrix:
    return prior.field_matrix(matrix, polynomial)


def field_equal(
    left: sp.Matrix, right: sp.Matrix, polynomial: sp.Poly
) -> bool:
    return prior.field_equal(left, right, polynomial)


def field_adjoint(matrix: sp.Matrix, polynomial: sp.Poly) -> sp.Matrix:
    return prior.field_adjoint(matrix, polynomial)


def field_det(matrix: sp.Matrix, polynomial: sp.Poly) -> sp.Expr:
    """Exact small determinant with reduction after every operation."""
    if matrix.rows != matrix.cols:
        raise AssertionError("field determinant requires a square matrix")
    total = sp.S.Zero
    for permutation in permutations(range(matrix.rows)):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(matrix.rows)
            for right in range(left + 1, matrix.rows)
        )
        term = sp.S.NegativeOne if inversions % 2 else sp.S.One
        for row, column in enumerate(permutation):
            term = red(term * matrix[row, column], polynomial)
        total = red(total + term, polynomial)
    return total


def field_rank(matrix: sp.Matrix, polynomial: sp.Poly) -> int:
    for size in range(min(matrix.rows, matrix.cols), 0, -1):
        for rows in combinations(range(matrix.rows), size):
            for columns in combinations(range(matrix.cols), size):
                if field_det(matrix.extract(rows, columns), polynomial) != 0:
                    return size
    return 0


def polynomial_add(
    left: tuple[sp.Expr, ...],
    right: tuple[sp.Expr, ...],
    polynomial: sp.Poly,
) -> tuple[sp.Expr, ...]:
    size = max(len(left), len(right))
    return tuple(
        red(
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0),
            polynomial,
        )
        for index in range(size)
    )


def polynomial_multiply(
    left: tuple[sp.Expr, ...],
    right: tuple[sp.Expr, ...],
    polynomial: sp.Poly,
) -> tuple[sp.Expr, ...]:
    result = [sp.S.Zero] * (len(left) + len(right) - 1)
    for left_power, left_value in enumerate(left):
        for right_power, right_value in enumerate(right):
            target = left_power + right_power
            result[target] = red(
                result[target] + red(left_value * right_value, polynomial),
                polynomial,
            )
    return tuple(result)


def window_pencil_coefficients(
    source: sp.Matrix, shifted: sp.Matrix, polynomial: sp.Poly
) -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    """Coefficients of det(lambda*source-shifted), low power first."""
    if source.shape != (3, 3) or shifted.shape != (3, 3):
        raise AssertionError("window pencil requires two 3 by 3 matrices")
    total: tuple[sp.Expr, ...] = (sp.S.Zero,)
    for permutation in permutations(range(3)):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(3)
            for right in range(left + 1, 3)
        )
        term: tuple[sp.Expr, ...] = (
            sp.S.NegativeOne if inversions % 2 else sp.S.One,
        )
        for row, column in enumerate(permutation):
            term = polynomial_multiply(
                term,
                (-shifted[row, column], source[row, column]),
                polynomial,
            )
        total = polynomial_add(total, term, polynomial)
    if len(total) != 4:
        raise AssertionError("cubic window pencil has four coefficients")
    return total  # type: ignore[return-value]


def reverse_conjugate(matrix: sp.Matrix, polynomial: sp.Poly) -> sp.Matrix:
    if matrix.shape != (8, 8):
        raise AssertionError("reflection kernel requires an 8 by 8 matrix")
    return sp.Matrix(
        8,
        8,
        lambda row, column: red(
            star(matrix[row, 7 - column], polynomial), polynomial
        ),
    )


@dataclass(frozen=True)
class CovarianceParts:
    open_covariance: sp.Matrix
    ap_tail: sp.Matrix
    stored_covariance: sp.Matrix
    reduced_source: sp.Matrix
    q_vu: sp.Matrix
    q_vv_inverse: sp.Matrix
    injections: tuple[sp.Matrix, ...]
    split_exact: bool


def tail_covariance_from_sandwich(
    transfer: block118.Transfer,
    polynomial: sp.Poly,
    reduced_source: sp.Matrix,
    q_vu: sp.Matrix,
    q_vv_inverse: sp.Matrix,
    injections: tuple[sp.Matrix, ...],
    sandwich: sp.Matrix,
) -> sp.Matrix:
    """Response induced by -U[n,0] sandwich U[4,j+1] e/C_j."""
    schur_tail = sp.zeros(4)
    local_transfers = transfer.local_transfers
    for row in range(4):
        for source in range(4):
            state = (
                -block118.fundamental(local_transfers, row, 0)
                * sandwich
                * block118.fundamental(local_transfers, 4, source + 1)
                * injections[source]
            )
            schur_tail[row, source] = sp.cancel(state[0])
    u_response = field_matrix(schur_tail * reduced_source, polynomial)
    v_response = field_matrix(
        -q_vv_inverse * q_vu * u_response, polynomial
    )
    covariance = sp.zeros(8)
    for index in range(4):
        covariance[2 * index, :] = u_response[index, :]
        covariance[2 * index + 1, :] = v_response[index, :]
    return field_matrix(covariance, polynomial)


def finite_covariance_parts(
    action: sp.Matrix,
    transfer: block118.Transfer,
    polynomial: sp.Poly,
) -> CovarianceParts:
    """Rebuild the open response and literal antiperiodic wrap response."""
    even = (0, 2, 4, 6)
    odd = (1, 3, 5, 7)
    q_uv = action.extract(even, odd)
    q_vu = action.extract(odd, even)
    q_vv = action.extract(odd, odd)
    q_vv_inverse = q_vv.inv(method="DM")

    source_u = sp.zeros(4, 8)
    source_v = sp.zeros(4, 8)
    for index in range(4):
        source_u[index, 2 * index] = 1
        source_v[index, 2 * index + 1] = 1
    reduced_source = (
        source_u - q_uv * q_vv_inverse * source_v
    ).applyfunc(sp.cancel)

    injections = []
    for slice_now in transfer.slices:
        diagonal = slice_now.diagonal
        forward = slice_now.forward
        b_entry = diagonal[0, 1]
        d_entry = diagonal[1, 1]
        e_entry = forward[0, 0]
        f_entry = forward[1, 0]
        injections.append(
            sp.Matrix((sp.cancel(1 / (e_entry - b_entry * f_entry / d_entry)), 0))
        )
    resolved_injections = tuple(injections)

    open_schur = sp.zeros(4)
    local_transfers = transfer.local_transfers
    for row in range(4):
        for source in range(4):
            if row > source:
                open_schur[row, source] = (
                    block118.fundamental(local_transfers, row, source + 1)
                    * resolved_injections[source]
                )[0]

    open_u = field_matrix(open_schur * reduced_source, polynomial)
    open_v = field_matrix(
        q_vv_inverse * (source_v - q_vu * open_u), polynomial
    )
    open_covariance = sp.zeros(8)
    for index in range(4):
        open_covariance[2 * index, :] = open_u[index, :]
        open_covariance[2 * index + 1, :] = open_v[index, :]
    open_covariance = field_matrix(open_covariance, polynomial)

    transfer_square = block118.fundamental(local_transfers, 4, 0)
    boundary = field_matrix(
        (sp.eye(2) + transfer_square).inv(method="DM"), polynomial
    )
    ap_tail = tail_covariance_from_sandwich(
        transfer,
        polynomial,
        reduced_source,
        q_vu,
        q_vv_inverse,
        resolved_injections,
        boundary,
    )
    stored_covariance = field_matrix(
        block118.thermal_two_point(action, transfer).covariance, polynomial
    )
    split_exact = field_equal(
        open_covariance + ap_tail, stored_covariance, polynomial
    )
    return CovarianceParts(
        open_covariance,
        ap_tail,
        stored_covariance,
        reduced_source,
        q_vu,
        q_vv_inverse,
        resolved_injections,
        split_exact,
    )


@dataclass(frozen=True)
class SpectralData:
    period_transfer: sp.Matrix
    transfer_square: sp.Matrix
    stable: sp.Matrix
    unstable: sp.Matrix
    stable_interval: tuple[sp.Rational, sp.Rational]
    characteristic_exact: bool
    projectors_exact: bool
    isolation_exact: bool


def transfer_spectral_data(
    transfer: block118.Transfer,
    polynomial: sp.Poly,
    stable_interval: tuple[int, int],
) -> SpectralData:
    """Construct T=M^2 and its two exact root-field projectors."""
    period_transfer = block118.fundamental(
        transfer.local_transfers, 2, 0
    )
    transfer_square = block118.fundamental(transfer.local_transfers, 4, 0)
    shifted_period_transfer = block118.fundamental(
        transfer.local_transfers, 4, 2
    )
    stable = field_matrix(
        (transfer_square - (1 / A) * sp.eye(2)) / (A - 1 / A),
        polynomial,
    )
    unstable = field_matrix(sp.eye(2) - stable, polynomial)
    zero = sp.zeros(2)
    characteristic_exact = (
        block118.matrix_equal(
            transfer_square, shifted_period_transfer * period_transfer
        )
        and block118.matrix_equal(transfer_square, transfer.cycle_product)
        and block118.matrix_equal(transfer_square, -transfer.monodromy)
        and field_det(transfer_square - A * sp.eye(2), polynomial) == 0
        and field_det(transfer_square - (1 / A) * sp.eye(2), polynomial)
        == 0
    )
    projectors_exact = (
        field_equal(stable * stable, stable, polynomial)
        and field_equal(unstable * unstable, unstable, polynomial)
        and field_equal(stable * unstable, zero, polynomial)
        and field_equal(unstable * stable, zero, polynomial)
        and field_equal(stable + unstable, sp.eye(2), polynomial)
        and field_equal(transfer_square * stable, A * stable, polynomial)
        and field_equal(
            transfer_square * unstable, (1 / A) * unstable, polynomial
        )
        and field_rank(stable, polynomial) == 1
        and field_rank(unstable, polynomial) == 1
    )
    lower, upper = stable_interval
    scale = 10**12
    interval = (R(lower, scale), R(upper, scale))
    isolation_exact = (
        0 < interval[0] < interval[1] < 1
        and polynomial.count_roots(*interval) == 1
    )
    return SpectralData(
        period_transfer,
        transfer_square,
        stable,
        unstable,
        interval,
        characteristic_exact,
        projectors_exact,
        isolation_exact,
    )


def torus_gram(
    covariance: sp.Matrix, theta_cut: sp.Matrix, polynomial: sp.Poly
) -> sp.Matrix:
    """Theta-dressed OS Gram on positive slices 4,5,6,7.

    In the literal antiperiodic chart theta(t)=-1-t sends those slices to
    3,2,1,0.  The Block 119 intertwiner is already in the cut chart, so its
    A-slot representative is field-conjugated before transport.
    """
    cut = prior.cut_shift()
    theta_a_slot = prior.field_conjugate(theta_cut, polynomial)
    theta_extended = field_matrix(
        cut.T * theta_a_slot * cut, polynomial
    )
    dressed = field_matrix(theta_extended * covariance, polynomial)
    return sp.Matrix(
        4,
        4,
        lambda row, column: red(
            star(dressed[4 + row, 3 - column], polynomial), polynomial
        ),
    )


def dress_cut_wrap(
    raw_cut_wrap: sp.Matrix, theta: sp.Matrix, polynomial: sp.Poly
) -> sp.Matrix:
    return field_matrix(
        -theta * reverse_conjugate(raw_cut_wrap, polynomial), polynomial
    )[:4, :4]


@dataclass(frozen=True)
class TorusSector:
    shear: sp.Rational
    momentum: int
    sector: prior.Sector
    polynomial: sp.Poly
    theta: sp.Matrix
    transfer: block118.Transfer
    covariance_parts: CovarianceParts
    spectral: SpectralData
    gram: sp.Matrix
    anti_residual: sp.Matrix
    anti_rank: int
    half_completed: sp.Matrix
    defect: sp.Matrix
    open_bridge: sp.Matrix
    stable_tail: sp.Matrix
    unstable_tail: sp.Matrix
    construction_exact: bool
    half_rebuilt: bool
    half_hermitian: bool
    residual_localized: bool
    wrap_induced: bool


def build_torus_sectors(shear: sp.Rational) -> tuple[TorusSector, ...]:
    """Reuse Block 119's swap and rebuild every torus/half-space split live."""
    sectors = prior.make_sectors(shear)
    completion = prior.reflection_real_completion(sectors)
    fixture = block118.build_fixture(shear)
    cut = prior.cut_shift()
    cut_actions = tuple(
        block118.reflection_cut(action)[0] for action in fixture.action_blocks
    )
    cut_transfers = tuple(
        block118.transfer_from_action(action) for action in cut_actions
    )
    result = []
    for momentum in range(4):
        opposite = (-momentum) % 4
        sector = sectors[momentum]
        polynomial = sector.polynomial
        theta = completion.thetas[momentum]
        action_cut = cut_actions[opposite]
        transfer = cut_transfers[opposite]
        covariance_cut = field_matrix(
            cut * fixture.propagator_blocks[opposite] * cut.T, polynomial
        )
        parts = finite_covariance_parts(action_cut, transfer, polynomial)
        stable_record = block118.stable_residue(transfer)
        stable_covariance = field_matrix(stable_record.matrix, polynomial)
        rebuilt_h00 = reverse_conjugate(stable_covariance, polynomial)
        half_completed = field_matrix(theta * rebuilt_h00, polynomial)

        gram = field_matrix(
            torus_gram(
                fixture.propagator_blocks[opposite], theta, polynomial
            ),
            polynomial,
        )
        torus_cut_kernel = reverse_conjugate(covariance_cut, polynomial)
        gram_from_cut = field_matrix(
            -theta * torus_cut_kernel, polynomial
        )[:4, :4]
        defect = field_matrix(
            gram - half_completed[:4, :4], polynomial
        )
        anti_residual = field_matrix(
            gram - field_adjoint(gram, polynomial), polynomial
        )

        open_bridge = field_matrix(
            parts.open_covariance + stable_covariance, polynomial
        )
        raw_wrap = field_matrix(covariance_cut + stable_covariance, polynomial)
        induced_defect = dress_cut_wrap(raw_wrap, theta, polynomial)
        spectral = transfer_spectral_data(
            transfer, polynomial, sector.stable_interval
        )
        transfer_inverse = field_matrix(
            spectral.transfer_square.inv(method="DM"), polynomial
        )
        stable_tail = tail_covariance_from_sandwich(
            transfer,
            polynomial,
            parts.reduced_source,
            parts.q_vu,
            parts.q_vv_inverse,
            parts.injections,
            field_matrix(spectral.stable * transfer_inverse, polynomial),
        )
        unstable_tail = tail_covariance_from_sandwich(
            transfer,
            polynomial,
            parts.reduced_source,
            parts.q_vu,
            parts.q_vv_inverse,
            parts.injections,
            field_matrix(spectral.unstable * transfer_inverse, polynomial),
        )

        half_rebuilt = (
            transfer.magnitude_polynomial == polynomial
            and stable_record.polynomial_valid
            and stable_record.regular_at_zero
            and stable_record.rank_one
            and field_equal(rebuilt_h00, sector.h00, polynomial)
        )
        half_hermitian = field_equal(
            half_completed,
            field_adjoint(half_completed, polynomial),
            polynomial,
        )
        residual_localized = (
            half_hermitian
            and field_equal(
                anti_residual,
                defect - field_adjoint(defect, polynomial),
                polynomial,
            )
        )
        construction_exact = (
            parts.split_exact
            and field_equal(parts.stored_covariance, covariance_cut, polynomial)
            and field_equal(gram, gram_from_cut, polynomial)
            and field_equal(
                gram, half_completed[:4, :4] + defect, polynomial
            )
        )
        wrap_induced = (
            field_equal(
                raw_wrap, open_bridge + parts.ap_tail, polynomial
            )
            and field_equal(induced_defect, defect, polynomial)
        )
        result.append(
            TorusSector(
                shear,
                momentum,
                sector,
                polynomial,
                theta,
                transfer,
                parts,
                spectral,
                gram,
                anti_residual,
                field_rank(anti_residual, polynomial),
                half_completed,
                defect,
                open_bridge,
                stable_tail,
                unstable_tail,
                construction_exact,
                half_rebuilt,
                half_hermitian,
                residual_localized,
                wrap_induced,
            )
        )
    return tuple(result)


@dataclass(frozen=True)
class PencilFacts:
    coefficients: tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]
    endpoints_zero: bool
    cross_zero: bool
    zero_polynomial: bool
    split_at_one: bool
    torus_equals_wrap_at_one: bool
    wrap_nonzero: bool


def pencil_facts(item: TorusSector) -> PencilFacts:
    polynomial = item.polynomial
    half_source = item.half_completed[:3, :3]
    half_shifted = item.half_completed[1:4, 1:4]
    coefficients = window_pencil_coefficients(
        half_source, half_shifted, polynomial
    )
    source_determinant = field_det(half_source, polynomial)
    shifted_determinant = field_det(half_shifted, polynomial)
    endpoints_zero = (
        source_determinant == 0
        and shifted_determinant == 0
        and coefficients[3] == source_determinant
        and coefficients[0] == -shifted_determinant
    )
    cross_zero = coefficients[1] == 0 and coefficients[2] == 0

    torus_source = item.gram[:3, :3]
    torus_shifted = item.gram[1:4, 1:4]
    defect_source = item.defect[:3, :3]
    defect_shifted = item.defect[1:4, 1:4]
    torus_at_one_matrix = field_matrix(
        torus_source - torus_shifted, polynomial
    )
    half_at_one_matrix = field_matrix(
        half_source - half_shifted, polynomial
    )
    defect_at_one_matrix = field_matrix(
        defect_source - defect_shifted, polynomial
    )
    split_at_one = field_equal(
        torus_at_one_matrix,
        half_at_one_matrix + defect_at_one_matrix,
        polynomial,
    )
    torus_at_one = field_det(torus_at_one_matrix, polynomial)
    half_at_one = field_det(half_at_one_matrix, polynomial)
    wrap_contribution = red(torus_at_one - half_at_one, polynomial)
    torus_coefficients = window_pencil_coefficients(
        torus_source, torus_shifted, polynomial
    )
    stored_torus_value = red(sum(torus_coefficients), polynomial)
    return PencilFacts(
        coefficients,
        endpoints_zero,
        cross_zero,
        all(value == 0 for value in coefficients),
        split_at_one and stored_torus_value == torus_at_one,
        half_at_one == 0 and wrap_contribution == torus_at_one,
        wrap_contribution != 0,
    )


@dataclass(frozen=True)
class FiniteSizeFacts:
    coefficients: tuple[sp.Expr, sp.Expr, sp.Expr]
    boundary_laws: bool
    sandwich_laws: bool
    wrap_coefficients: bool


def finite_size_facts(item: TorusSector) -> FiniteSizeFacts:
    polynomial = item.polynomial
    spectral = item.spectral
    coefficients = []
    boundary_laws = True
    sandwich_laws = True
    wrap_coefficients = True
    for copies in (1, 2, 3):
        transfer_power = field_matrix(
            spectral.transfer_square**copies, polynomial
        )
        boundary = field_matrix(
            (sp.eye(2) + spectral.transfer_square**copies).inv(method="DM"),
            polynomial,
        )
        a_power = red(A**copies, polynomial)
        coefficient = red(a_power / (1 + a_power), polynomial)
        coefficients.append(coefficient)
        expected_boundary = field_matrix(
            spectral.stable / (1 + a_power)
            + spectral.unstable / (1 + 1 / a_power),
            polynomial,
        )
        expected_sandwich = field_matrix(
            coefficient * spectral.stable
            + (1 - coefficient) * spectral.unstable,
            polynomial,
        )
        boundary_laws = boundary_laws and field_equal(
            boundary, expected_boundary, polynomial
        )
        sandwich_laws = (
            sandwich_laws
            and field_equal(
                boundary * transfer_power, expected_sandwich, polynomial
            )
            and field_equal(
                boundary * transfer_power - spectral.unstable,
                coefficient * (spectral.stable - spectral.unstable),
                polynomial,
            )
        )
        wrap_coefficients = wrap_coefficients and (
            red(coefficient * (1 + A**copies) - A**copies, polynomial)
            == 0
            and red(1 - coefficient - 1 / (1 + A**copies), polynomial)
            == 0
        )
    return FiniteSizeFacts(
        (coefficients[0], coefficients[1], coefficients[2]),
        boundary_laws,
        sandwich_laws,
        wrap_coefficients,
    )


@dataclass(frozen=True)
class SaturationFacts:
    physical_tail_split: bool
    physical_defect_split: bool
    limiting_operator_nonzero: bool
    projector_rank_one: bool
    stable_geometric: bool


def saturation_facts(
    item: TorusSector, finite: FiniteSizeFacts
) -> SaturationFacts:
    polynomial = item.polynomial
    c_one = finite.coefficients[0]
    physical_tail_split = field_equal(
        item.covariance_parts.ap_tail,
        c_one * item.stable_tail + (1 - c_one) * item.unstable_tail,
        polynomial,
    )
    stable_channel = dress_cut_wrap(
        field_matrix(item.open_bridge + item.stable_tail, polynomial),
        item.theta,
        polynomial,
    )
    unstable_channel = dress_cut_wrap(
        field_matrix(item.open_bridge + item.unstable_tail, polynomial),
        item.theta,
        polynomial,
    )
    physical_defect_split = field_equal(
        item.defect,
        c_one * stable_channel + (1 - c_one) * unstable_channel,
        polynomial,
    ) and all(
        field_equal(
            dress_cut_wrap(
                field_matrix(
                    item.open_bridge
                    + coefficient * item.stable_tail
                    + (1 - coefficient) * item.unstable_tail,
                    polynomial,
                ),
                item.theta,
                polynomial,
            ),
            coefficient * stable_channel
            + (1 - coefficient) * unstable_channel,
            polynomial,
        )
        for coefficient in finite.coefficients
    )
    limiting_operator_nonzero = any(
        red(value, polynomial) != 0 for value in unstable_channel
    )
    projector_rank_one = (
        field_rank(item.spectral.stable, polynomial) == 1
        and field_rank(item.spectral.unstable, polynomial) == 1
    )
    stable_geometric = (
        item.spectral.isolation_exact
        and all(
            red(
                finite.coefficients[index] * (1 + A ** (index + 1))
                - A ** (index + 1),
                polynomial,
            )
            == 0
            for index in range(3)
        )
    )
    return SaturationFacts(
        physical_tail_split,
        physical_defect_split,
        limiting_operator_nonzero,
        projector_rank_one,
        stable_geometric,
    )


@dataclass(frozen=True)
class CorrectedFacts:
    outer_square: bool
    inertia: tuple[int, int, int]
    quotient: sp.Expr
    quotient_interval: tuple[sp.Rational, sp.Rational]
    contraction: bool
    power_reconciliation: bool


def corrected_facts(item: TorusSector) -> CorrectedFacts:
    polynomial = item.polynomial
    corrected = field_matrix(item.gram - item.defect, polynomial)
    positive_vector = item.sector.y[:4, :]
    square = prior.root_outer(positive_vector, polynomial)
    outer_square = (
        field_equal(corrected, item.half_completed[:4, :4], polynomial)
        and field_equal(corrected, square, polynomial)
        and field_equal(corrected, field_adjoint(corrected, polynomial), polynomial)
    )
    inertia = prior.rank_one_outer_inertia(
        positive_vector, corrected, polynomial
    )
    quotient = red(A**2, polynomial)
    lower_integer, upper_integer = item.sector.stable_interval
    scale = 10**12
    quotient_interval = (
        R(lower_integer**2, scale**2),
        R(upper_integer**2, scale**2),
    )
    quotient_polynomial = block118.square_root_polynomial(polynomial)
    contraction = (
        0 < quotient_interval[0] < quotient_interval[1] < 1
        and quotient_polynomial.count_roots(*quotient_interval) == 1
        and red(
            quotient_polynomial.as_expr().subs(block118.BETA, quotient),
            polynomial,
        )
        == 0
    )
    power_reconciliation = (
        red(quotient - A * A, polynomial) == 0
        and all(
            red(quotient**steps - A ** (2 * steps), polynomial) == 0
            for steps in (1, 2, 3)
        )
    )
    return CorrectedFacts(
        outer_square,
        inertia,
        quotient,
        quotient_interval,
        contraction,
        power_reconciliation,
    )


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


SCOPE_KEYS = (
    "wrap_defect",
    "wrap_operator",
    "antiperiodic",
    "torus_nonhermiticity",
    "zero_pencil",
    "unstable_saturation",
    "geometric_decay",
    "half_space_carrier",
    "torus_limit",
    "rank_one",
    "power_bookkeeping",
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
        "wrap_defect": "wrap defect" in note,
        "wrap_operator": "wrap operator" in note,
        "antiperiodic": "antiperiodic" in note,
        "torus_nonhermiticity": (
            "residual rank 4" in note
            or "residual rank four" in note
            or "non-hermitian on the torus" in note
        ),
        "zero_pencil": (
            "vanishes identically" in note or "zero polynomial" in note
        ),
        "unstable_saturation": "unstable" in note and "saturat" in note,
        "geometric_decay": (
            "geometrically" in note or "geometric decay" in note
        ),
        "half_space_carrier": "half-space carrier" in note,
        "torus_limit": (
            "large-torus limit" in note or "fixed torus" in note
        ),
        "rank_one": "rank-one" in note,
        "power_bookkeeping": "bookkeeping" in note or "double period" in note,
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
    if mutation == "claim_axiom_amendment":
        result["axiom"] = False
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
        "Block 119 blobs and ancestors 118--103 are pinned",
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_TORUS_WRAP_DEFECT_BOUNDED_THEOREM_NOTE_2026-08-16.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md",
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
            authority[f"ancestor_{number}"] for number in range(103, 119)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    fixtures = (
        build_torus_sectors(block118.PRIMARY_SHEAR),
        build_torus_sectors(block118.SECOND_SHEAR),
    )
    all_items = tuple(item for fixture in fixtures for item in fixture)

    theta_transfers_claimed = mutation == "claim_theta_transfers"
    torus_failure = all(
        item.anti_rank == 4
        and not field_equal(
            item.gram, field_adjoint(item.gram, item.polynomial), item.polynomial
        )
        for item in all_items
    )
    checks.check(
        "B-theta-fails-on-the-torus",
        "theta(t)=-1-t gives non-Hermitian Z8 Grams with residual rank 4; inertia is undefined",
        tuple((-1 - (4 + index)) % 8 for index in range(4)) == (3, 2, 1, 0)
        and torus_failure
        and not theta_transfers_claimed,
    )

    split_facts = all(
        item.construction_exact
        and item.half_rebuilt
        and item.half_hermitian
        and item.residual_localized
        and item.wrap_induced
        and not field_equal(
            item.defect,
            field_adjoint(item.defect, item.polynomial),
            item.polynomial,
        )
        for item in all_items
    )
    if mutation == "break_split":
        split_facts = False
    hermitian_defect_claimed = mutation == "claim_hermitian_defect"
    checks.check(
        "C-the-keystone-split",
        "K_torus=K_half+D entrywise; R_AP=-U[n,0](I+M^2)^-1U[4,j+1]e/C_j; all residual lies in D",
        split_facts and not hermitian_defect_claimed,
    )

    pencils = tuple(pencil_facts(item) for item in all_items)
    zero_pencil = all(
        fact.endpoints_zero
        and fact.cross_zero
        and fact.zero_polynomial
        and fact.split_at_one
        and fact.torus_equals_wrap_at_one
        and fact.wrap_nonzero
        for fact in pencils
    )
    if mutation == "break_zero_pencil":
        zero_pencil = False
    checks.check(
        "D-the-vanishing-pencil",
        "both half-window determinants and both cross coefficients vanish; f_torus(1)=W_f(1)!=0",
        zero_pencil,
    )

    finite = tuple(finite_size_facts(item) for item in all_items)
    projector_law = all(
        item.spectral.characteristic_exact
        and item.spectral.projectors_exact
        and item.spectral.isolation_exact
        and facts.boundary_laws
        for item, facts in zip(all_items, finite)
    )
    wrap_coefficients = all(
        facts.sandwich_laws and facts.wrap_coefficients for facts in finite
    )
    if mutation == "break_projector_law":
        projector_law = False
    if mutation == "break_wrap_coefficient":
        wrap_coefficients = False
    checks.check(
        "E-the-finite-size-law",
        "T=M^2 has root a in (0,1); B_N=P_s/(1+a^N)+P_u/(1+a^-N), c_N=a^N/(1+a^N), N=1,2,3",
        projector_law and wrap_coefficients,
    )

    saturations = tuple(
        saturation_facts(item, facts)
        for item, facts in zip(all_items, finite)
    )
    saturation = all(
        facts.physical_tail_split
        and facts.physical_defect_split
        and facts.limiting_operator_nonzero
        and facts.projector_rank_one
        and facts.stable_geometric
        for facts in saturations
    )
    full_decay_claimed = mutation == "claim_full_decay"
    checks.check(
        "F-the-unstable-saturation",
        "B_N T^N=c_N P_s+(1-c_N)P_u tends to rank-one P_u; D_1 and D_infinity are exact and nonzero",
        saturation and not full_decay_claimed,
    )

    corrected = tuple(corrected_facts(item) for item in all_items)
    corrected_inertia = all(
        facts.outer_square and facts.inertia == (1, 0, 3)
        for facts in corrected
    )
    power_reconciliation = all(
        facts.contraction and facts.power_reconciliation for facts in corrected
    )
    beta_pins = tuple(
        tuple(
            corrected[4 * fixture_index + momentum].quotient_interval
            for momentum in (0, 1)
        )
        for fixture_index in range(2)
    )
    if mutation == "break_corrected_inertia":
        corrected_inertia = False
    if mutation == "break_power_reconciliation":
        power_reconciliation = False
    checks.check(
        "G-the-corrected-completion",
        "Theta(K_torus-D)=y y^H has inertia (1,0,3); double-period factor a^2=(rho_F^2)^2=rho_F^4",
        corrected_inertia
        and power_reconciliation
        and beta_pins == prior.EXPECTED_BETA_INTERVALS,
    )

    note_scope = scope_certificate(normalized_note(), mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "required wrap/no-go/N1--N8/W1/N5 firewalls and runtime bound are present",
        set(note_scope) == set(SCOPE_KEYS)
        and all(note_scope.values())
        and elapsed_before_scope <= 400,
    )

    for fixture in fixtures:
        shear = fixture[0].shear
        interval_pins = tuple(
            item.sector.stable_interval for item in fixture[:2]
        )
        print(
            f"TORUS c={shear}: residual_ranks="
            f"{tuple(item.anti_rank for item in fixture)}; "
            f"a_even/odd={interval_pins}/10^12; no inertia"
        )
    print(
        "SATURATION: c_1=a/(1+a), c_2=a^2/(1+a^2), "
        "c_3=a^3/(1+a^3); D_1=c_1 D_s+(1-c_1)D_u; "
        "D_infinity=D_u=-Theta R[(G_open+B_-1)+G(P_u T^-1)]_+ "
        "from the rank-one P_u channel"
    )
    for fixture in fixtures:
        squared_pins = tuple(
            tuple(bound**2 for bound in item.sector.stable_interval)
            for item in fixture[:2]
        )
        print(
            f"CORRECTED c={fixture[0].shear}: per_k=((1,0,3),)*4; "
            f"a^2_even/odd={squared_pins}/10^24; "
            f"runtime={time.monotonic() - started:.3f}s"
        )
    print(
        "N5: per_element: exact torus/half-space split, anti-Hermitian residual rank, all-non-Hermiticity-in-D, zero-pencil, projector, subtraction, Hermiticity, inertia, and quotient identities are checked"
    )
    print(
        "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus"
    )
    print(
        "per_mode: all four fixed momenta at c=5/13 and c=3/5 have rank(K-K*)=4 before subtraction and corrected inertia (1,0,3) after exact defect subtraction"
    )
    print(
        "per_block: the literal Z8 torus pairing splits as K_T=K_H+D; D carries all dressed non-Hermiticity, while K_T-D=K_H=y_+y_+^H has quotient beta=a^2 in (0,1)"
    )
    print(
        "lattice_wide: checked and not executed — torus completion without the displayed subtraction, naturality classification, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: the literal torus rejects the completion exactly through the antiperiodic wrap — whose stable channel decays geometrically while its rank-one unstable channel saturates — and subtracting the displayed defect restores the positive contractive package"
    )
    print(
        "DECISION_CUT: pose OS on the half-space or large-torus carrier; classify naturality; then the curved carrier and the gravity constraint quotient"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
